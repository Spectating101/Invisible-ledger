from pathlib import Path
import sys
import unittest
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts/analysis'))
import longitudinal_review as c
import reviewed_longitudinal as r
import paper_review_tables as p

class PaperTableTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        original=[]
        for path in c.FILES:
            records,digest=c.read_rows(ROOT,path)
            original.extend(c.normalize(x,path,digest) for x in records)
        decisions,digest=c.read_rows(ROOT,r.REVIEW)
        cls.rows,_=r.apply_review(original,decisions,digest)
        cls.annual=p.select_annual(cls.rows)
        cls.changes=[x for x in r.annual_changes(cls.rows) if x['scope']=='3P Retail']
    def test_seven_years_not_seven_firms(self):
        self.assertEqual([x['year'] for x in self.annual],list(range(2019,2026)))
        self.assertTrue(all(x['main_sample_status']=='not_approved' for x in self.annual))
    def test_negative_2019_is_preserved(self):
        self.assertLess(c.number(self.annual[0]['net_revenue_idr_billion']),0)
        self.assertEqual(self.annual[0]['ecosystem_ratio'],'')
    def test_2023_vintage_explicit(self):
        x=next(x for x in self.annual if x['year']==2023)
        self.assertEqual(x['source_url'],p.F24)
        self.assertEqual(c.number(x['tpv_idr_billion']),c.D(49912))
        self.assertIn('unresolved',x['selection_note'])
    def test_three_same_release_comparisons(self):
        self.assertEqual([(x['from_year'],x['to_year']) for x in self.changes],[(2021,2022),(2023,2024),(2024,2025)])
        self.assertLess(c.number(self.changes[-1]['tv_growth_percent']),0)
        self.assertGreater(c.number(self.changes[-1]['net_revenue_growth_percent']),0)
    def test_no_tpv_derived_from_revenue(self):
        self.assertEqual(c.number(self.annual[-1]['tpv_idr_billion']),c.D(53187))
        self.assertEqual(c.number(self.annual[-1]['net_revenue_idr_billion']),c.D(1551))
    def test_rendered_markdown_contains_scope_and_source(self):
        text=p.paper_text(self.annual,self.changes)
        self.assertIn('one business segment, not seven firms',text)
        self.assertIn('not an approved Indonesia-only main sample',text)
        self.assertIn(p.F25,text)

if __name__=='__main__':unittest.main()
