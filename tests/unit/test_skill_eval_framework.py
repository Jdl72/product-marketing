import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SKILL_PATH = REPO_ROOT / "skills/lpa-eval-framework/SKILL.md"


class TestSkillEvalFramework(unittest.TestCase):
    def setUp(self):
        self.text = SKILL_PATH.read_text()

    def test_section_1_present(self):
        self.assertIn("Section 1", self.text)

    def test_section_2_present(self):
        self.assertIn("Section 2", self.text)

    def test_section_3_present(self):
        self.assertIn("Section 3", self.text)

    def test_section_4_present(self):
        self.assertIn("Section 4", self.text)

    def test_section_5_present(self):
        self.assertIn("Section 5", self.text)

    def test_section_6_present(self):
        self.assertIn("Section 6", self.text)

    def test_fm_id_field_present(self):
        self.assertIn("FM-ID", self.text)

    def test_ev_id_field_present(self):
        self.assertIn("EV-ID", self.text)

    def test_binary_success_criterion_present(self):
        self.assertIn("Binary Success Criterion", self.text)

    def test_likert_prohibition_present(self):
        self.assertIn("Likert", self.text)

    def test_100_pair_minimum_present(self):
        self.assertIn("100", self.text)

    def test_true_positives_present(self):
        self.assertIn("True Positives", self.text)

    def test_false_positives_present(self):
        self.assertIn("False Positives", self.text)

    def test_precision_present(self):
        self.assertIn("Precision", self.text)

    def test_recall_present(self):
        self.assertIn("Recall", self.text)

    def test_90_percent_alignment_threshold_present(self):
        self.assertIn("90%", self.text)

    def test_claims_to_avoid_present(self):
        self.assertIn("Claims to Avoid", self.text)

    def test_ev_id_citation_requirement_explicit(self):
        # Section 5 must state the EV-ID citation requirement for downstream artifacts
        self.assertIn("EV-ID", self.text)
        # Downstream artifact citation rule must reference Battle Cards or equivalent
        self.assertTrue(
            "Battle Cards" in self.text or "downstream artifact" in self.text.lower(),
            "EV-ID citation requirement for downstream artifacts not found",
        )


if __name__ == "__main__":
    unittest.main()
