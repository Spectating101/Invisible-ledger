"""Tests for period, value, provenance and sample-count safeguards."""
import csv
import importlib.util
import tempfile
import unittest
from decimal import Decimal as D
from pathlib import Path

SCRIPT=Path(__file__).resolve().parents[1]/'scripts/analysis/longitudinal_review.py'
spec=importlib.util.spec_from_file_location('review',SCRIPT)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

class LongitudinalReviewTests(unittest.TestCase):
    def raw(self, **changes):
        r=dict(platform='Blibli/GDN',period='2023FY',scope='3P Retail',unit='IDR billion',
               tpv='100',revenue='10',gpbd='15',source_url='https://issuer.example/2024/03/a.pdf',
               source_file='source.pdf',source_page='2',status='pending',_line=2)
        r.update(changes);return r
    def normalized(self, **changes):
        return m.normalize(self.raw(**changes),m.BLIBLI_FILES[0],'abc')
    def test_numbers_preserve_negative(self):
        self.assertEqual(m.number('(219,189)'),D(-219189))
    def test_missing_is_not_zero(self):
        self.assertIsNone(m.number('NA'));self.assertEqual(m.number('0'),D(0))
    def test_nonfinite_rejected(self):
        with self.assertRaises(ValueError):m.number('Infinity')
    def test_periods_separated(self):
        self.assertEqual(m.period_info('FY2023'),('2023FY','annual',12))
        self.assertEqual(m.period_info('2023Q4'),('2023Q4','quarter',3))
        self.assertEqual(m.period_info('2023H1'),('2023H1','cumulative',6))
        self.assertEqual(m.period_info('9M2023'),('20239M','cumulative',9))
    def test_unknown_period_fails_closed(self):
        with self.assertRaises(ValueError):m.period_info('2023YTD')
    def test_ratio_identity(self):
        a=m.metrics(D(100),D(10));self.assertEqual(D(a['ecosystem_ratio']),D(9))
        self.assertEqual(D(a['monetization_rate']),D('.1'))
    def test_gpbd_not_treated_as_revenue(self):
        a=self.normalized(gpbd='70');self.assertEqual(D(a['ecosystem_ratio']),D(9))
    def test_zero_denominator_not_ratio(self):
        a=self.normalized(revenue='-0.0');self.assertEqual(a['ecosystem_ratio'],'')
        self.assertEqual(D(a['difference']),D(100))
    def test_negative_revenue_not_zeroed(self):
        a=self.normalized(revenue='-3');self.assertEqual(D(a['revenue']),D(-3))
        self.assertEqual(a['ecosystem_ratio'],'')
    def test_duplicates_do_not_inflate_periods(self):
        a=self.normalized();b=self.normalized(source_url='https://issuer.example/new.pdf')
        can,conf=m.reconcile([a,b]);self.assertEqual(len(can),1);self.assertFalse(conf)
        self.assertEqual(can[0]['source_records'],2)
    def test_conflict_blocks_choice(self):
        a=self.normalized();b=self.normalized(tpv='101')
        can,conf=m.reconcile([a,b]);self.assertEqual(len(conf),2)
        self.assertEqual(can[0]['tv'],'');self.assertEqual(can[0]['value_status'],'unresolved_value_conflict')
    def test_annual_quarter_not_deduplicated_together(self):
        can,_=m.reconcile([self.normalized(),self.normalized(period='2023Q4')]);self.assertEqual(len(can),2)
    def test_group_segment_not_same_key(self):
        can,_=m.reconcile([self.normalized(),self.normalized(scope='Group')]);self.assertEqual(len(can),2)
    def test_currency_conversion_only(self):
        a=self.normalized(unit='IDR million',tpv='100000',revenue='10000',gpbd='15000')
        self.assertEqual(D(a['tv']),D(100));self.assertEqual(a['currency'],'IDR')
    def test_bukalapak_partial_year_excluded(self):
        raw=dict(platform='Bukalapak',year='2024',tpv_idr_million='124076664',revenue_idr_million='4460266',tpv_months='9',revenue_months='12',_line=2)
        a=m.normalize(raw,'data/longitudinal/bukalapak_annual_candidates.csv','abc')
        self.assertEqual(a['technical_status'],'exclude_period_mismatch');self.assertEqual(a['difference'],'')
    def test_tokopedia_bad_year_excluded(self):
        raw=dict(platform='Tokopedia e-commerce segment',period='FY2021',transaction_value_native='230598613',platform_revenue_native='1997222',unit='IDR_million',_line=2)
        a=m.normalize(raw,'data/longitudinal/indonesia_platform_year_extension.csv','abc')
        self.assertEqual(a['technical_status'],'exclude_period_mismatch')
    def test_country_allocation_not_direct_pair(self):
        raw=dict(platform='Grab',period='FY2023',transaction_value_native='5.38',platform_revenue_native='.605',unit='USD_billion',_line=2)
        a=m.normalize(raw,'data/longitudinal/indonesia_platform_year_extension.csv','abc')
        self.assertEqual(a['directness'],'derived_country_construction')
    def test_changes_do_not_bridge_different_releases(self):
        a=self.normalized(period='2022FY');b=self.normalized(period='2023FY',source_url='https://other.example/b.pdf')
        self.assertFalse(m.within_release_changes([a,b]))
    def test_changes_from_same_release(self):
        a=self.normalized(period='2022FY',tpv='100',revenue='10');b=self.normalized(period='2023FY',tpv='90',revenue='12')
        out=m.within_release_changes([a,b]);self.assertEqual(len(out),1)
        self.assertEqual(D(out[0]['tv_growth_percent']),D(-10))
        self.assertEqual(D(out[0]['net_revenue_growth_percent']),D(20))
    def test_no_main_approval_inferred(self):
        c,_=m.reconcile([self.normalized()]);self.assertEqual(c[0]['main_admission'],'pending_researcher_and_advisor_review')
    def test_provenance_kept(self):
        a=self.normalized();self.assertEqual(a['source_csv_sha256'],'abc');self.assertEqual(a['source_csv_row'],2)
    def test_malformed_csv_fails(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'bad.csv';p.write_text('a,b\n1,2,3\n')
            with self.assertRaises(ValueError):m.read_rows(Path(d),'bad.csv')
    def test_write_read_deterministic(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'a.csv';rows=[{'a':'1','b':'text,comma'}]
            m.write_csv(p,rows);first=p.read_bytes();m.write_csv(p,rows);self.assertEqual(p.read_bytes(),first)

if __name__=='__main__':unittest.main()
