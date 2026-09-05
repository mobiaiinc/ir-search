"""Parser tests on synthetic HTML shaped like the live markup (verified 2026-07-11).

If a site redesign changes the markup, update the fixture here *and* the parser —
a fixture that no longer matches the site makes a green test meaningless.
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import kstartup_crawl  # noqa: E402
import sources_crawl  # noqa: E402

KSTARTUP = """
<div class="carousel"><li><a onclick="go_view(999)"><p class="tit">캐러셀 추천</p></a></li></div>
<div id="bizPbancList"><ul>
<li><a onclick="go_view(178481)">
  <span class="flag type1">사업화</span><span class="flag day">D-3</span>
  <p class="tit">2026 청년창업사관학교 &amp; 추가모집</p>
  <span class="list"><i class="ico"></i>청년창업사관학교</span>
  <span class="list"><i class="ico"></i>중소벤처기업진흥공단</span>
  <span class="list"><i class="ico"></i>시작일자 2026-08-20</span>
  <span class="list"><i class="ico"></i>마감일자 2026-09-08</span>
  <span class="flag_agency">공공</span></a></li>
<li class="notice"><a onclick="go_view(178200)"><span class="flag type3">시설·공간</span>
  <p class="tit">충남 콘텐츠 입주기업 모집</p>
  <span class="list"><i></i>입주지원</span><span class="list"><i></i>충남콘텐츠진흥원</span>
  <span class="list"><i></i>마감일자 2026-08-01</span></a></li>
<li><div>no link here</div></li>
</ul></div>
"""

BIZINFO = """
<table><tr><th>번호</th><th>분야</th></tr>
<tr><td>1</td><td>창업</td><td><a href="/sii/siia/selectSIIA200Detail.do?pblancId=PBLN_000000000112233">
  2026 초기창업패키지</a></td><td>2026-08-01 ~ 2026-09-10</td><td>중소벤처기업부</td><td>창업진흥원</td><td>2026-08-01</td><td>12</td></tr>
<tr><td>2</td><td>기술</td><td><a href="/sii/siia/selectSIIA200Detail.do?pblancId=PBLN_000000000112234">AI 바우처</a></td>
  <td>~ 2026-07-01</td><td>과기정통부</td><td></td><td>2026-06-01</td><td>3</td></tr>
</table>
"""

NIPA = """
<table><tr><td>10</td><td>D-5</td><td><a href="/home/2-2/12345"><!-- c -->2026 AI 융합 혁신 지원</a>
  <span class="box tag">AI</span><p>신청기간 : 2026-08-15 ~ 2026-09-10</p></td>
  <td>담당자</td><td><span class="bco">120</span><span class="bco">2026-08-15</span></td></tr></table>
"""

KOCCA = """
<table><tr><td><span class="category_color2">제작지원</span></td>
<td><a href="/kocca/pims/view.do?intcNo=ABC123&amp;menuNo=204104">2026 오디오 콘텐츠 제작지원</a></td>
<td data-label="공고일"> 26.07.10 </td><td data-label="접수기간"> 26.07.10 ~ 26.07.31 </td><td>55</td></tr></table>
"""

SMTECH = """
<table><tr><td>창업성장기술개발</td>
<td><a href="/front/ifg/no/notice02_detail.do;jsessionid=ABCDEF?ancmId=S02001&amp;buclCd=S2101">2026 디딤돌 2차</a></td>
<td>2026-08-20 ~ 2026-09-20 18:00</td><td>2026-08-20</td><td><img alt="접수중"></td></tr></table>
"""


def fetch_returning(html):
    def fetch(url, data=None):
        fetch.last = (url, data)
        return 200, html

    return fetch


class KStartupTests(unittest.TestCase):
    def test_parse_list_skips_carousel_and_reads_fields(self):
        items = kstartup_crawl.parse_list(KSTARTUP)
        ids = [i["pbancSn"] for i in items]
        self.assertEqual(ids, ["178481", "178200"])  # carousel 999 excluded, linkless li skipped
        a = items[0]
        self.assertEqual(a["title"], "2026 청년창업사관학교 & 추가모집")
        self.assertEqual(a["category"], "사업화")
        self.assertEqual(a["dday"], "D-3")
        self.assertEqual(a["program"], "청년창업사관학교")
        self.assertEqual(a["org"], "중소벤처기업진흥공단")
        self.assertEqual(a["start"], "2026-08-20")
        self.assertEqual(a["deadline"], "2026-09-08")
        self.assertEqual(a["agency_type"], "공공")
        self.assertTrue(a["url"].endswith("pbancSn=178481"))
        self.assertEqual(items[1]["start"], "")  # missing field → empty, not guessed

    def test_parse_list_without_main_block_is_empty(self):
        self.assertEqual(kstartup_crawl.parse_list("<html>Access Denied</html>"), [])


class SourcesTests(unittest.TestCase):
    def test_bizinfo(self):
        items, more = sources_crawl.page_bizinfo(fetch_returning(BIZINFO), 1)
        self.assertTrue(more)
        self.assertEqual(len(items), 2)
        a = items[0]
        self.assertEqual(a["id"], "PBLN_000000000112233")
        self.assertEqual(a["title"], "2026 초기창업패키지")
        self.assertEqual(a["field"], "창업")
        self.assertEqual(a["org"], "중소벤처기업부 / 창업진흥원")
        self.assertEqual((a["apply_start"], a["apply_end"]), ("2026-08-01", "2026-09-10"))
        self.assertEqual(a["reg_date"], "2026-08-01")
        self.assertEqual(items[1]["apply_end"], "2026-07-01")
        self.assertEqual(items[1]["org"], "과기정통부")

    def test_nipa(self):
        items, _ = sources_crawl.page_nipa(fetch_returning(NIPA), 1)
        a = items[0]
        self.assertEqual(a["id"], "12345")
        self.assertEqual(a["title"], "2026 AI 융합 혁신 지원")  # HTML comment stripped
        self.assertEqual(a["field"], "AI")
        self.assertEqual((a["apply_start"], a["apply_end"]), ("2026-08-15", "2026-09-10"))
        self.assertEqual(a["reg_date"], "2026-08-15")  # last .bco, not the view count
        self.assertEqual(a["url"], "https://www.nipa.kr/home/2-2/12345")

    def test_kocca_uses_post_and_two_digit_years(self):
        fetch = fetch_returning(KOCCA)
        items, _ = sources_crawl.page_kocca(fetch, 3)
        self.assertEqual(fetch.last[1], {"menuNo": "204104", "pageIndex": "3"})
        a = items[0]
        self.assertEqual(a["id"], "ABC123")
        self.assertEqual(a["field"], "제작지원")
        self.assertEqual((a["apply_start"], a["apply_end"]), ("2026-07-10", "2026-07-31"))
        self.assertEqual(a["reg_date"], "2026-07-10")
        self.assertIn("intcNo=ABC123&menuNo=204104", a["url"])

    def test_smtech_strips_jsessionid(self):
        items, _ = sources_crawl.page_smtech(fetch_returning(SMTECH), 1)
        a = items[0]
        self.assertEqual(a["id"], "S02001")
        self.assertNotIn("jsessionid", a["url"])
        self.assertIn("ancmId=S02001&buclCd=S2101", a["url"])
        self.assertEqual((a["apply_start"], a["apply_end"]), ("2026-08-20", "2026-09-20"))
        self.assertEqual(a["reg_date"], "2026-08-20")

    def test_empty_page_stops(self):
        for pager in sources_crawl.SOURCES.values():
            items, more = pager(fetch_returning("<html></html>"), 1)
            self.assertEqual(items, [])
            self.assertFalse(more)

    def test_non_200_stops(self):
        def fetch(url, data=None):
            return 500, ""

        self.assertEqual(sources_crawl.page_bizinfo(fetch, 1), ([], False))

    def test_crawl_dedups_and_reports_block(self):
        pages = {1: BIZINFO, 2: BIZINFO}  # page 2 repeats page 1 → 0 new → stop

        def fetch(url, data=None):
            n = int(url.split("cpage=")[1].split("&")[0])
            return 200, pages.get(n, "")

        items, blocked = sources_crawl.crawl("bizinfo", fetch, 5)
        self.assertEqual(len(items), 2)
        self.assertFalse(blocked)

        import fetchlib

        def blocked_fetch(url, data=None):
            raise fetchlib.Blocked(url, ["safari@www"])

        items, blocked = sources_crawl.crawl("nipa", blocked_fetch, 5)
        self.assertEqual(items, [])
        self.assertTrue(blocked)


if __name__ == "__main__":
    unittest.main()
