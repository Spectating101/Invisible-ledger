"""Reproduction tests and algebraic safeguards; no claim to validate survey design."""
import importlib.util
from decimal import Decimal as D, localcontext
from pathlib import Path
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('bridge',ROOT/'scripts/analysis/build_contribution_bridge.py')
b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)

class AlgebraTests(unittest.TestCase):
    def test_number_preserves_zero(self):self.assertEqual(b.number('0'),D(0))
    def test_nonfinite_rejected(self):
        for x in ('NaN','Infinity','-Infinity'):
            with self.subTest(x=x), self.assertRaises(ValueError):b.number(x)
    def test_missing_not_zero(self):
        with self.assertRaises(ValueError):b.number('')
    def test_invalid_probability_rejected(self):
        for x in (D('-.01'),D('1.01'),D('NaN')):
            with self.subTest(x=x), self.assertRaises(ValueError):b.probability(x)
    def test_growth_zero_base_rejected(self):
        with self.assertRaises(ValueError):b.growth(D(0),D(2))
    def test_growth_negative_base_rejected(self):
        with self.assertRaises(ValueError):b.growth(D(-1),D(2))
    def test_decomposition_pure_count(self):
        r=b.symmetric_decomposition(D(100),D(200),D(10),D(20))
        self.assertEqual(r['count_component_idr_trillion'],D(100));self.assertEqual(r['average_component_idr_trillion'],0)
    def test_decomposition_pure_average(self):
        r=b.symmetric_decomposition(D(100),D(200),D(10),D(10))
        self.assertEqual(r['count_component_idr_trillion'],0);self.assertEqual(r['average_component_idr_trillion'],100)
    def test_decomposition_zero_change_share_missing(self):
        r=b.symmetric_decomposition(D(100),D(100),D(10),D(20));self.assertIsNone(r['count_component_share_pct'])
    def test_decomposition_negative_counts_rejected(self):
        with self.assertRaises(ValueError):b.symmetric_decomposition(D(1),D(2),D(-1),D(2))
    def test_decomposition_grid_reconciles(self):
        for v1 in (D(50),D(100),D(150)):
            for n1 in (D(7),D(10),D(17)):
                r=b.symmetric_decomposition(D(100),v1,D(10),n1)
                self.assertLess(abs(r['reconciliation_residual']),D('1e-20'))
    def test_neither_2024(self):self.assertEqual(b.neither_bounds(D('.1723'),D('.1715')),(D('.6562'),D('.8277')))
    def test_neither_2023(self):self.assertEqual(b.neither_bounds(D('.178'),D('.1519')),(D('.6701'),D('.822')))
    def test_joint_bounds_do_not_assume_independence(self):
        lo,hi=b.neither_bounds(D('.2'),D('.3'));ind=D('.8')*D('.7')
        self.assertLess(lo,ind);self.assertGreater(hi,ind)
    def test_witness_grid_is_feasible_and_sharp(self):
        for i in range(21):
            for j in range(21):
                p,q=D(i)/20,D(j)/20
                for w in b.witnesses(p,q):
                    cells=[w[k] for k in ('both','only_first','only_second','neither')]
                    self.assertTrue(all(x>=0 for x in cells));self.assertEqual(sum(cells),1)
                    self.assertEqual(w['both']+w['only_first'],p);self.assertEqual(w['both']+w['only_second'],q)
                lo,hi=b.neither_bounds(p,q)
                # Values outside endpoints necessarily violate at least one 2x2 cell constraint.
                for n in (lo-D('.0001'),hi+D('.0001')):
                    joint=n-1+p+q
                    self.assertTrue(any(x<0 for x in (joint,p-joint,q-joint,n)))
    def test_csv_missing_value_is_empty(self):self.assertEqual(b.value_string(None),'')

class RepositoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data,cls.lineage=b.load(ROOT/b.INPUT)
    def test_exact_source_blob(self):self.assertEqual(b.blob_hash((ROOT/b.INPUT).read_bytes()),b.INPUT_BLOB)
    def test_source_has_27_records(self):self.assertEqual(len(self.lineage),27)
    def test_source_lineage_has_locators(self):self.assertTrue(all(x['source_url'] and x['source_locator'] for x in self.lineage))
    def test_missing_indicator_fails(self):
        with self.assertRaises(KeyError):b.get(self.data,2022,b.REPORTS,'percent')
    def test_unit_mismatch_fails(self):
        with self.assertRaises(ValueError):b.get(self.data,2024,b.MARKET,'IDR_trillion')
    def test_tampered_input_fails(self):
        with tempfile.TemporaryDirectory() as temp:
            p=Path(temp)/'input.csv';p.write_bytes((ROOT/b.INPUT).read_bytes()+b'\n')
            with self.assertRaises(ValueError):b.load(p)
    def test_2024_channel_value_is_derived_not_copied(self):
        _,_,ch=b.economic_tables(self.data)
        self.assertEqual(ch[0]['value_2024_derived_idr_trillion'],D('203.522047'))
        self.assertEqual(sum(x['value_2024_derived_idr_trillion'] for x in ch),D('1288.93'))
        self.assertEqual(sum(x['share_of_total_change_pct'] for x in ch),100)
    def test_business_share_not_value_share(self):
        self.assertEqual(b.get(self.data,2024,b.MARKET,'percent'),D('17.23'))
        self.assertEqual(b.get(self.data,2024,'marketplace_share_of_transaction_value','percent'),D('15.79'))
    def test_growth_sensitivity_is_separate(self):
        exp,_,_=b.economic_tables(self.data)
        self.assertEqual(len(exp),4)
        z=[x for x in exp if x['start_year']==2023]
        self.assertEqual(z[0]['initial_businesses'],D(3816750));self.assertEqual(z[1]['initial_businesses'],D(3934981))
        self.assertGreater(z[1]['average_value_growth_pct'],z[0]['average_value_growth_pct'])
    def test_recordkeeping_count_vs_share(self):
        _,r,_=b.economic_tables(self.data)
        self.assertEqual(r[0]['ownership_change_pp'],D('1.96'))
        self.assertGreater(r[0]['have_growth_pct'],0);self.assertGreater(r[0]['not_have_growth_pct'],0)
    def test_rounding_only_encloses_plugin_bounds(self):
        bounds,_=b.joint_bounds(self.data)
        for x in bounds:
            self.assertLessEqual(x['rounding_outer_lower_pct'],x['lower_pct'])
            self.assertGreaterEqual(x['rounding_outer_upper_pct'],x['upper_pct'])
    def test_no_approval_or_sampling_inference(self):
        with tempfile.TemporaryDirectory() as tmp:
            manifest=b.build(ROOT,Path(tmp))
            self.assertFalse(manifest['sampling_uncertainty_included'])
            self.assertIn('not_approved',manifest['status'])
    def test_regeneration_and_source_immutability(self):
        before=(ROOT/b.INPUT).read_bytes()
        with tempfile.TemporaryDirectory() as tmp:
            a,bdir=Path(tmp)/'a',Path(tmp)/'b'
            b.build(ROOT,a);b.build(ROOT,bdir)
            self.assertEqual(sorted(p.name for p in a.iterdir()),sorted(p.name for p in bdir.iterdir()))
            self.assertTrue(all(p.read_bytes()==(bdir/p.name).read_bytes() for p in a.iterdir()))
        self.assertEqual((ROOT/b.INPUT).read_bytes(),before)
    def test_overlapping_output_rejected(self):
        with self.assertRaises(ValueError):b.build(ROOT,ROOT)
    def test_results_are_supplementary_not_issuer_rows(self):
        with tempfile.TemporaryDirectory() as tmp:
            b.build(ROOT,Path(tmp));s=(Path(tmp)/'RESULTS.md').read_text()
            self.assertIn('no main-sample approval',s);self.assertIn('no first-in-literature claim',s)

if __name__=='__main__':unittest.main()
