import importlib.util
import copy
from pathlib import Path
import sys
import unittest
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts/analysis'))
import reviewed_longitudinal as r
import longitudinal_review as c

class SourceReviewTests(unittest.TestCase):
    def row(self,period='2023Q1',tv='100',rev='10',scope='3P Retail',basis='reported',url='https://issuer.example/a.pdf'):
        x=c.normalize(dict(platform='Blibli/GDN',period=period,scope=scope,unit='IDR billion',tpv=tv,revenue=rev,gpbd='20',source_url=url,status='candidate',_line=2),c.BLIBLI_FILES[0],'sourcehash')
        x['source_basis']=basis
        return x
    def decision(self,**kw):
        x=dict(action='relabel',scope='3P Retail',original_period='2023Q1',reviewed_period='2022FY',tv='100',revenue='10',gpbd='20',source_url='https://issuer.example/a.pdf',source_page='2',review_note='Column order verified')
        x.update(kw);return x
    def test_relabel_changes_period_not_values(self):
        old=self.row();out,log=r.apply_review([old],[self.decision()],'reviewhash')
        self.assertEqual((out[0]['period'],out[0]['frequency'],out[0]['tv_months']),('2022FY','annual',12))
        self.assertEqual(out[0]['tv'],old['tv']);self.assertEqual(old['period'],'2023Q1');self.assertEqual(len(log),1)
    def test_relabel_fails_on_changed_values(self):
        with self.assertRaises(ValueError):r.apply_review([self.row(tv='101')],[self.decision()],'hash')
    def test_relabel_fails_on_absent_target(self):
        with self.assertRaises(ValueError):r.apply_review([],[self.decision()],'hash')
    def test_relabel_fails_on_duplicate_target(self):
        x=self.row()
        with self.assertRaises(ValueError):r.apply_review([x,x],[self.decision()],'hash')
    def test_duplicate_decisions_rejected(self):
        with self.assertRaises(ValueError):r.apply_review([self.row()],[self.decision(),self.decision()],'hash')
    def test_recovery_keeps_source_lineage(self):
        out,log=r.apply_review([],[self.decision(action='recover',original_period='',reviewed_period='2022Q1')],'hash')
        self.assertEqual(out[0]['period'],'2022Q1');self.assertEqual(out[0]['source_csv'],r.REVIEW)
        self.assertIn('recovered_omitted_source_column',out[0]['flags']);self.assertEqual(log[0]['action'],'recover')
    def test_actual_and_proforma_not_conflicts(self):
        a=self.row('2024FY',basis='FY actual');b=self.row('2024FY',tv='90',basis='FY pro-forma comparable')
        out,conflicts=r.reconcile([a,b]);self.assertEqual(len(out),2);self.assertFalse(conflicts)
        cov=r.coverage([a,b],out)[0];self.assertEqual(cov['period_matched_periods'],1);self.assertEqual(cov['basis_variant_keys'],2)
    def test_genuine_value_conflict_still_blocks(self):
        out,conflicts=r.reconcile([self.row(),self.row(tv='101')]);self.assertEqual(len(conflicts),2);self.assertEqual(out[0]['tv'],'')
    def test_rollup_detects_annual_as_quarter(self):
        rows=[self.row('2023H1',tv='30'),self.row('2023Q1',tv='100'),self.row('2023Q2',tv='20')]
        check=next(x for x in r.rollups(rows) if x['metric']=='tv')
        self.assertEqual(check['status'],'unreconciled_above_rounding_tolerance')
    def test_rollup_rounding_tolerance(self):
        rows=[self.row('2023H1',tv='31'),self.row('2023Q1',tv='10'),self.row('2023Q2',tv='20')]
        check=next(x for x in r.rollups(rows) if x['metric']=='tv');self.assertEqual(check['status'],'within_rounding_tolerance')
    def test_missing_quarter_not_interpolated(self):
        rows=[self.row('2023H1',tv='30'),self.row('2023Q1',tv='10')]
        self.assertFalse(r.rollups(rows));self.assertEqual(len(rows),2)
    def test_rollup_conflict_not_arbitrarily_resolved(self):
        rows=[self.row('2023H1',tv='30'),self.row('2023Q1',tv='10'),self.row('2023Q1',tv='11'),self.row('2023Q2',tv='20')]
        check=next(x for x in r.rollups(rows) if x['metric']=='tv');self.assertEqual(check['status'],'blocked_by_missing_or_conflicting_vintage')
    def test_changes_block_same_source_conflict(self):
        rows=[self.row('2022FY'),self.row('2023FY',tv='110'),self.row('2023FY',tv='111')]
        self.assertFalse(r.annual_changes(rows))
    def test_changes_require_same_source(self):
        self.assertFalse(r.annual_changes([self.row('2022FY'),self.row('2023FY',url='different')]))
    def test_no_geographic_approval_from_period_fix(self):
        out,_=r.apply_review([self.row()],[self.decision()],'h');can,_=r.reconcile(out)
        self.assertEqual(can[0]['main_admission'],'not_approved');self.assertEqual(can[0]['geography_status'],'not_country_isolated_pending_review')

class ActualRepositoryTests(unittest.TestCase):
    def test_real_correction_ledger_and_3p_rollups(self):
        rows=[]
        for path in c.FILES:
            records,digest=c.read_rows(ROOT,path);rows.extend(c.normalize(x,path,digest) for x in records)
        decisions,digest=c.read_rows(ROOT,r.REVIEW);reviewed,logs=r.apply_review(rows,decisions,digest)
        self.assertEqual(sum(x['action']=='relabel' for x in logs),10)
        self.assertEqual(sum(x['action']=='recover' for x in logs),5)
        selected=[x for x in r.rollups(reviewed) if x['scope']=='3P Retail' and x['year'] in ('2022','2023')]
        self.assertTrue(selected);self.assertTrue(all(x['status']=='within_rounding_tolerance' for x in selected))
        q=[x for x in reviewed if x['issuer']=='Blibli/GDN' and x['scope']=='3P Retail' and x['period']=='2022Q1']
        self.assertEqual(len(q),1);self.assertEqual(c.number(q[0]['tv']),c.D(5632))

if __name__=='__main__':unittest.main()
