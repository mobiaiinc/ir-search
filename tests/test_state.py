import io
import json
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stdout, redirect_stderr
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import survey_state  # noqa: E402

TODAY = "2026-09-05"


class StateTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.proj = Path(self.tmp.name)
        self.root = self.proj / ".ir-search"

    def tearDown(self):
        self.tmp.cleanup()

    def run_cmd(self, *argv, today=TODAY):
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            survey_state.main(["--root", str(self.root), "--today", today, *argv])
        return out.getvalue().strip()

    def init(self):
        return self.run_cmd("init", "--project-dir", str(self.proj))

    def test_init_creates_files_and_is_idempotent(self):
        self.init()
        for name in ("profile.md", "worklog.md", "queue.jsonl", "decisions.md"):
            self.assertTrue((self.root / name).exists(), name)
        self.assertTrue((self.root / "runs").is_dir())
        (self.root / "profile.md").write_text("# custom\n- 대상: X\n", encoding="utf-8")
        self.init()
        self.assertEqual((self.root / "profile.md").read_text(encoding="utf-8"), "# custom\n- 대상: X\n")

    def test_init_migrates_legacy_profile(self):
        legacy = self.proj / "ir-search-profile.md"
        legacy.write_text("# ir-search 프로필\n- 대상: 레거시\n- 마지막 조사: ~/Documents/x (2026-07-11)\n", encoding="utf-8")
        self.init()
        self.assertIn("레거시", (self.root / "profile.md").read_text(encoding="utf-8"))
        self.assertFalse(legacy.exists())
        self.assertTrue((self.proj / "ir-search-profile.md.migrated").exists())

    def test_run_lifecycle_and_worklog(self):
        self.init()
        run_dir = self.run_cmd("run", "new", "--sources", "kstartup,bizinfo")
        self.assertTrue(run_dir.endswith("runs/20260905"))
        meta = json.loads((Path(run_dir) / "run.json").read_text(encoding="utf-8"))
        self.assertEqual((meta["mode"], meta["stage"], meta["sources"]), ("full", "collect", ["kstartup", "bizinfo"]))

        # a second run is refused while one is in progress
        with self.assertRaises(SystemExit):
            self.run_cmd("run", "new")
        self.assertIn("20260905", self.run_cmd("run", "current"))

        self.run_cmd("run", "stage", run_dir, "verify")
        qid = self.run_cmd("queue", "add", "--type", "verify", "--title", "청창사", "--ref", "178481", "--deadline", "2026-09-08")
        self.assertEqual(qid, "q001")
        # duplicate (same type+ref) returns the existing id
        self.assertEqual(self.run_cmd("queue", "add", "--type", "verify", "--title", "dup", "--ref", "178481"), "q001")
        self.run_cmd("queue", "add", "--type", "apply", "--title", "프리팁스", "--deadline", "2026-09-07")

        (Path(run_dir) / "report.md").write_text("# r\n", encoding="utf-8")
        self.run_cmd("run", "finish", run_dir, "--report", str(Path(run_dir) / "report.md"),
                     "--counts", "kstartup=262,bizinfo=300", "--candidates", "31", "--verified", "31",
                     "--a", "5", "--b", "4", "--c", "6", "--note", "첫 조사")
        worklog = (self.root / "worklog.md").read_text(encoding="utf-8")
        self.assertIn("## 2026-09-05 — 전수조사 (full)", worklog)
        self.assertIn("kstartup 262 / bizinfo 300", worklog)
        self.assertIn("A 5 / B 4 / C 6", worklog)
        self.assertIn("메모: 첫 조사", worklog)
        profile = (self.root / "profile.md").read_text(encoding="utf-8")
        self.assertIn("- 마지막 조사: .ir-search/runs/20260905 (2026-09-05)", profile)

        # verify item auto-closed, apply item still open
        open_items = json.loads(self.run_cmd("queue", "list", "--json"))
        self.assertEqual([q["type"] for q in open_items], ["apply"])
        self.assertEqual(self.run_cmd("run", "last"), run_dir)
        with self.assertRaises(SystemExit):
            self.run_cmd("run", "current")

        # next run auto-selects diff with the finished run as baseline; same-day suffix
        info = json.loads(self.run_cmd("run", "new", "--json"))
        self.assertEqual(info["mode"], "diff")
        self.assertEqual(info["baseline"], run_dir)
        self.assertTrue(info["dir"].endswith("20260905-2"))

    def test_queue_dday_rendering(self):
        self.init()
        self.run_cmd("queue", "add", "--type", "apply", "--title", "임박", "--deadline", "2026-09-07")
        self.run_cmd("queue", "add", "--type", "apply", "--title", "지남", "--deadline", "2026-09-01")
        self.run_cmd("queue", "add", "--type", "manual", "--title", "CCEI")
        self.run_cmd("queue", "add", "--type", "resurvey", "--title", "재조사", "--deadline", "2026-09-05")
        table = self.run_cmd("queue", "list")
        self.assertIn("| D-2 ⚠️ |", table)
        self.assertIn("| D+4 (지남) |", table)
        self.assertIn("| 불명 |  |", table)
        self.assertIn("| D-Day ⚠️ |", table)
        self.run_cmd("queue", "done", "q002", "--note", "마감 지남")
        self.assertNotIn("지남 |", self.run_cmd("queue", "list"))
        self.assertIn("지남", self.run_cmd("queue", "list", "--all"))

    def test_decide_appends(self):
        self.init()
        self.run_cmd("decide", "--title", "프리팁스 A→B", "--decision", "B로", "--reason", "비수도권 법인 요건", "--ref", "1779")
        text = (self.root / "decisions.md").read_text(encoding="utf-8")
        self.assertIn("## 2026-09-05 — 프리팁스 A→B", text)
        self.assertIn("- 이유: 비수도권 법인 요건", text)

    def test_last_run_orders_by_started_not_folder_name(self):
        # runs/20260905-10 sorts before runs/20260905-2 as a string; `run last`
        # must still return the most recently *started* finished run.
        self.init()
        runs = self.root / "runs"
        for name, started in (("20260905", "2026-09-05T09:00:00"),
                              ("20260905-2", "2026-09-05T10:00:00"),
                              ("20260905-10", "2026-09-05T18:00:00")):
            d = runs / name
            d.mkdir(parents=True)
            (d / "run.json").write_text(json.dumps({
                "started": started, "mode": "full", "sources": ["kstartup"],
                "stage": "done", "finished": started, "report": f".ir-search/runs/{name}/report.md",
            }), encoding="utf-8")
        self.assertTrue(self.run_cmd("run", "last").endswith("20260905-10"))
        # and `run current` picks the most recently started open run the same way
        (runs / "20260905-3").mkdir()
        (runs / "20260905-3" / "run.json").write_text(json.dumps(
            {"started": "2026-09-05T19:00:00", "mode": "diff", "sources": [], "stage": "verify"}),
            encoding="utf-8")
        self.assertIn("20260905-3", self.run_cmd("run", "current"))

    def test_status_without_workspace_exits(self):
        with self.assertRaises(SystemExit):
            self.run_cmd("status")


if __name__ == "__main__":
    unittest.main()
