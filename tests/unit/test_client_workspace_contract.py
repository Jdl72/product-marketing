import unittest
from pathlib import Path
import subprocess

from tests.test_helpers import REPO_ROOT


EXAMPLE_ROOT = REPO_ROOT / "examples" / "client-workspace" / "generic-example"


class ClientWorkspaceContractTests(unittest.TestCase):
    def test_example_workspace_has_required_directories(self):
        for relative_dir in ("briefs", "config", "decisions", "evidence", "records", "syntheses"):
            path = EXAMPLE_ROOT / relative_dir
            self.assertTrue(path.is_dir(), f"{path} must exist")

    def test_example_workspace_has_required_config_files(self):
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
            path = EXAMPLE_ROOT / "config" / filename
            self.assertTrue(path.is_file(), f"{path} must exist")
            self.assertTrue(path.read_text(encoding="utf-8").strip(), f"{path} must not be empty")

    def test_example_workspace_has_required_decisions_files(self):
        expected_files = (
            "insight-to-action-tracker.md",
            "open-questions.md",
            "cross-functional-action-log.md",
        )

        for filename in expected_files:
            path = EXAMPLE_ROOT / "decisions" / filename
            self.assertTrue(path.is_file(), f"{path} must exist")
            self.assertTrue(path.read_text(encoding="utf-8").strip(), f"{path} must not be empty")

    def test_example_workspace_has_evidence_readme(self):
        readme = EXAMPLE_ROOT / "evidence" / "README.md"
        self.assertTrue(readme.is_file(), f"{readme} must exist")
        self.assertIn("source inventories", readme.read_text(encoding="utf-8").lower())

    def test_pr_keeps_jobs_skills_and_schemas_boundary_clean(self):
        result = subprocess.run(
            ["git", "diff", "--name-only", "origin/main...HEAD", "--", "jobs", "skills", "schemas"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertEqual(
            result.stdout.strip(),
            "",
            "core jobs/skills/schemas paths should not be modified by this client-workspace PR",
        )


if __name__ == "__main__":
    unittest.main()
