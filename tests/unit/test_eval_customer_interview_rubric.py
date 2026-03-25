import unittest
from pathlib import Path

from tests.test_helpers import REPO_ROOT


RUBRIC_PATH = REPO_ROOT / "evals/lpa-customer-interview-rubric.md"


class TestEvalCustomerInterviewRubric(unittest.TestCase):
    def setUp(self):
        self.path = RUBRIC_PATH
        self.text = self.path.read_text()

    def test_rubric_file_exists(self):
        self.assertTrue(self.path.exists(), f"Rubric not found at {self.path}")

    def test_pass_fail_rule_section_present(self):
        self.assertIn("Pass / fail rule", self.text)

    def test_at_least_five_dimensions(self):
        # Each dimension is a level-3 heading (###)
        dimension_count = self.text.count("\n### ")
        self.assertGreaterEqual(
            dimension_count,
            5,
            f"Expected at least 5 dimensions, found {dimension_count}",
        )

    def test_screener_rigor_dimension_present(self):
        self.assertIn("Screener rigor", self.text)

    def test_preparation_quality_dimension_present(self):
        self.assertIn("Preparation quality", self.text)

    def test_learning_goal_alignment_dimension_present(self):
        self.assertIn("Learning goal alignment", self.text)

    def test_note_quality_dimension_present(self):
        self.assertIn("Note quality", self.text)

    def test_snapshot_completeness_dimension_present(self):
        self.assertIn("Snapshot completeness", self.text)

    def test_synthesis_contribution_dimension_present(self):
        self.assertIn("Synthesis contribution", self.text)

    def test_evidence_calibration_dimension_present(self):
        self.assertIn("Evidence calibration", self.text)

    def test_fail_condition_missing_snapshot_field_present(self):
        self.assertIn("§2F snapshot field is missing", self.text)

    def test_fail_condition_paraphrased_quotes_present(self):
        self.assertIn("paraphrased", self.text)

    def test_fail_condition_hypothesis_not_in_snapshot_present(self):
        self.assertIn("hypotheses tested", self.text.lower())


if __name__ == "__main__":
    unittest.main()
