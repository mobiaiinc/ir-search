import io
import json
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import diff_surveys  # noqa: E402


def write_jsonl(path, records):
    with open(path, "w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def ks(sn, deadline, title="t"):
    return {"pbancSn": sn, "title": title, "deadline": deadline, "url": f"u{sn}"}


def src(source, id_, end, title="t"):
    return {"source": source, "id": id_, "title": title, "apply_end": end, "url": f"u{id_}"}


class DiffTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.prev = Path(self.tmp.name) / "prev"
        self.curr = Path(self.tmp.name) / "curr"
        self.prev.mkdir()
        self.curr.mkdir()

    def tearDown(self):
        self.tmp.cleanup()

    def run_diff(self, out=None):
        argv = [str(self.prev), str(self.curr)] + (["--out", str(out)] if out else [])
        buf = io.StringIO()
        old = sys.argv
        sys.argv = ["diff_surveys.py"] + argv
        try:
            with redirect_stdout(buf):
                diff_surveys.main()
        finally:
            sys.argv = old
        return buf.getvalue()

    def test_classification(self):
        write_jsonl(self.prev / "kstartup.jsonl", [ks("1", "2026-09-10"), ks("2", "2026-09-12"), ks("3", "2026-09-01")])
        write_jsonl(self.prev / "bizinfo.jsonl", [src("bizinfo", "B1", "2026-09-30")])
        write_jsonl(self.curr / "kstartup.jsonl", [ks("1", "2026-09-10"), ks("2", "2026-09-20"), ks("4", "2026-10-01")])
        write_jsonl(self.curr / "bizinfo.jsonl", [src("bizinfo", "B1", "2026-09-30")])
        write_jsonl(self.curr / "nipa.jsonl", [src("nipa", "N1", "2026-10-05")])
        out = Path(self.tmp.name) / "new.jsonl"
        text = self.run_diff(out)
        self.assertIn("## NEW (1)", text)
        self.assertIn("## DEADLINE CHANGED (1)", text)
        self.assertIn("(was: 2026-09-12)", text)
        self.assertIn("## CLOSED (1)", text)
        self.assertIn("UNCHANGED: 2", text)
        self.assertIn("NEW SOURCES this run (nipa): 1 items", text)
        self.assertNotIn("WARNING", text)
        new_items = [json.loads(l) for l in out.read_text(encoding="utf-8").splitlines()]
        self.assertEqual({r.get("pbancSn") or r.get("id") for r in new_items}, {"4", "N1"})

    def test_dropped_source_is_not_closed(self):
        write_jsonl(self.prev / "kstartup.jsonl", [ks("1", "2026-09-10")])
        write_jsonl(self.prev / "bizinfo.jsonl", [src("bizinfo", "B1", "2026-09-30"), src("bizinfo", "B2", "2026-09-30")])
        write_jsonl(self.curr / "kstartup.jsonl", [ks("1", "2026-09-10")])
        text = self.run_diff()
        self.assertIn("## CLOSED (0)", text)
        self.assertIn("WARNING — sources in previous run but not re-crawled: bizinfo", text)

    def test_derived_files_are_ignored(self):
        write_jsonl(self.prev / "bizinfo.jsonl", [src("bizinfo", "B1", "2026-09-30")])
        write_jsonl(self.curr / "bizinfo.jsonl", [src("bizinfo", "B1", "2026-09-30")])
        # verified.jsonl carries the same id with a different field set — must not
        # register as a deadline change; new_items.jsonl must not double-count.
        write_jsonl(self.curr / "verified.jsonl", [{"source": "bizinfo", "id": "B1", "deadline": "2026-09-30 18:00"}])
        write_jsonl(self.curr / "new_items.jsonl", [src("bizinfo", "B1", "2026-01-01")])
        text = self.run_diff()
        self.assertIn("## DEADLINE CHANGED (0)", text)
        self.assertIn("UNCHANGED: 1", text)

    def test_missing_dir_exits(self):
        with self.assertRaises(SystemExit):
            sys.argv = ["diff_surveys.py", str(self.prev), str(self.curr / "nope")]
            diff_surveys.main()


if __name__ == "__main__":
    unittest.main()
