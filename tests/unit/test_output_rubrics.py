import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]

EXPECTED_RUBRICS = {
    "conversation-record-rubric.md",
    "conversation-synthesis-rubric.md",
    "positioning-brief-rubric.md",
    "persona-pack-rubric.md",
    "gtm-plan-rubric.md",
    "battle-card-rubric.md",
    "content-calendar-rubric.md",
}


class OutputRubricsTests(unittest.TestCase):
    def test_schema_backed_output_rubrics_exist(self):
        existing = {path.name for path in (REPO_ROOT / "evals").glob("*-rubric.md")}
        for rubric_name in EXPECTED_RUBRICS:
            self.assertIn(rubric_name, existing, f"{rubric_name} should exist in evals/")

    def test_new_major_output_rubrics_have_pass_fail_rule_and_review_notes(self):
        rubric_names = (
            "positioning-brief-rubric.md",
            "persona-pack-rubric.md",
            "gtm-plan-rubric.md",
            "battle-card-rubric.md",
            "content-calendar-rubric.md",
        )
        for rubric_name in rubric_names:
            text = (REPO_ROOT / "evals" / rubric_name).read_text(encoding="utf-8")
            self.assertIn("## Pass / fail rule", text, f"{rubric_name} should define pass/fail logic")
            self.assertIn("## Review notes to capture every time", text, f"{rubric_name} should define review notes")
            dimension_count = len(re.findall(r"^### \d+\.", text, re.MULTILINE))
            self.assertGreaterEqual(dimension_count, 5, f"{rubric_name} should define at least five dimensions")

    def test_roadmap_marks_evaluation_coverage_as_current_task(self):
        text = (REPO_ROOT / "docs" / "architecture" / "pmm-agent-roadmap.md").read_text(encoding="utf-8")
        marker = "Current next task:"
        self.assertIn(marker, text)
        after_marker = text.split(marker, 1)[1]
        next_section = after_marker.split("After that:", 1)[0]
        self.assertIn("Add evaluation criteria for each major output type", next_section)


if __name__ == "__main__":
    unittest.main()
