import unittest
from pathlib import Path

from tests.test_helpers import REPO_ROOT


XNURTA_ROOT = REPO_ROOT / "clients" / "xnurta"


class XnurtaWorkspaceTests(unittest.TestCase):
    def test_workspace_has_required_directories(self):
        for relative_dir in ("briefs", "config", "decisions", "evidence", "records", "syntheses"):
            path = XNURTA_ROOT / relative_dir
            self.assertTrue(path.is_dir(), f"{path} must exist")

    def test_workspace_has_required_config_files(self):
        expected_files = (
            "client-profile.md",
            "segment-taxonomy.md",
            "funnel-stages.md",
            "competitor-map.md",
            "coding-rules.md",
            "strategic-questions.md",
            "metrics-scorecard.md",
        )

        for filename in expected_files:
            path = XNURTA_ROOT / "config" / filename
            self.assertTrue(path.is_file(), f"{path} must exist")
            self.assertTrue(path.read_text(encoding="utf-8").strip(), f"{path} must not be empty")

    def test_segment_taxonomy_defines_all_four_segments(self):
        content = (XNURTA_ROOT / "config" / "segment-taxonomy.md").read_text(encoding="utf-8")
        for segment_id in ("`S1`", "`S2`", "`S3`", "`S4`"):
            self.assertIn(segment_id, content)

    def test_decision_tracker_rows_have_owner_and_function(self):
        tracker = (XNURTA_ROOT / "decisions" / "insight-to-action-tracker.md").read_text(encoding="utf-8")
        rows = [line for line in tracker.splitlines() if line.startswith("| XN-I-")]
        self.assertGreaterEqual(len(rows), 4)

        for row in rows:
            cells = [cell.strip() for cell in row.strip("|").split("|")]
            self.assertNotEqual(cells[3], "", f"Owner missing in row: {row}")
            self.assertNotEqual(cells[4], "", f"Function missing in row: {row}")

    def test_source_inventory_has_at_least_one_real_source_row(self):
        inventory = (XNURTA_ROOT / "evidence" / "source-inventory.md").read_text(encoding="utf-8")
        rows = [line for line in inventory.splitlines() if line.startswith("| ") and "source_id" not in line and "---" not in line]
        non_placeholder_rows = [row for row in rows if "TBD" not in row]
        self.assertTrue(non_placeholder_rows, "source inventory must contain at least one non-placeholder source")

    def test_records_readme_only_references_existing_repo_paths(self):
        content = (XNURTA_ROOT / "records" / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/architecture/parse-single-conversation-runbook.md", content)
        self.assertNotIn("config-aware-customer-conversation-runbook.md", content)


if __name__ == "__main__":
    unittest.main()
