import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
RUBRIC_PATH = REPO_ROOT / "evals/lpa-eval-framework-rubric.md"


class TestEvalFrameworkRubric(unittest.TestCase):
    def setUp(self):
        self.text = RUBRIC_PATH.read_text()

    def test_rubric_file_exists(self):
        self.assertTrue(RUBRIC_PATH.exists(), "evals/lpa-eval-framework-rubric.md does not exist")

    def test_pass_fail_rule_section_present(self):
        self.assertIn("Pass / Fail Rule", self.text)

    def test_dimension_fm_coverage_present(self):
        self.assertIn("FM Coverage", self.text)

    def test_dimension_dataset_quality_present(self):
        self.assertIn("Dataset Quality", self.text)

    def test_dimension_evaluator_design_present(self):
        self.assertIn("Evaluator Design", self.text)

    def test_dimension_human_alignment_present(self):
        self.assertIn("Human Alignment", self.text)

    def test_dimension_marketing_translation_present(self):
        self.assertIn("Marketing Translation", self.text)

    def test_at_least_five_dimensions_present(self):
        # Count dimension headings (### numbered headings)
        import re
        dimensions = re.findall(r"^###\s+\d+\.", self.text, re.MULTILINE)
        self.assertGreaterEqual(
            len(dimensions),
            5,
            f"Expected at least 5 dimensions, found {len(dimensions)}",
        )

    def test_fail_condition_missing_ev_id_present(self):
        self.assertIn("EV-ID", self.text)

    def test_fail_condition_alignment_below_90_present(self):
        self.assertIn("90%", self.text)


if __name__ == "__main__":
    unittest.main()
