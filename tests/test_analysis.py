"""Checks for actual failure modes, not just whether functions return values."""
import math
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from feature_engineering import score, edit_distance
from analyze_accuracy import analyze

class StudyTests(unittest.TestCase):
    def test_response_overrides_mislabeled_success(self):
        self.assertEqual(score('HSX6HZ','correct','HSX65Z'),0)
    def test_missing_wrong_human_string_is_not_excluded(self):
        self.assertEqual(score('','incorrect','ABC234',human=True),0)
    def test_unexplained_missing_answer_is_rejected(self):
        with self.assertRaises(ValueError):
            score('','correct','ABC234',human=True)
    def test_case_not_visual_confusions_normalized(self):
        self.assertEqual(score(' abc234 ','correct','ABC234'),1)
        self.assertEqual(score('ABCZ34','correct','ABC234'),0)
    def test_edit_distance_handles_insertions(self):
        self.assertEqual(edit_distance('ABC','AXBC'),1)
    def test_paired_test_uses_disagreements(self):
        rows=[dict(human_correct=h,ai_correct=a) for h,a,n in [(1,1,24),(1,0,15),(0,1,7),(0,0,4)] for _ in range(n)]
        result=analyze(rows)
        self.assertAlmostEqual(result['exact_mcnemar_one_sided_p'],sum(math.comb(22,k) for k in range(15,23))/2**22)
        self.assertEqual(result['decision'],'fail_to_reject')
    def test_no_disagreements_does_not_crash_or_claim_effect(self):
        result=analyze([dict(human_correct=1,ai_correct=1)]*10)
        self.assertEqual(result['exact_mcnemar_one_sided_p'],1)
        self.assertEqual(result['accuracy_difference'],0)

if __name__ == '__main__':
    unittest.main()
