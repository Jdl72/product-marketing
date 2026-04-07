import tempfile
import unittest
from pathlib import Path

from tests.test_helpers import REPO_ROOT, load_module


validator = load_module(
    "validate_client_config_integration",
    "scripts/validate_client_config.py",
)


class ClientConfigValidationWorkflowIntegrationTests(unittest.TestCase):
    def test_checked_in_example_matches_rendered_template_report(self):
        report = validator.analyze_workspace(REPO_ROOT / "examples" / "client-workspace" / "generic-example")
        rendered = validator.render_markdown(report)
        expected = (
            REPO_ROOT / "examples" / "client-workspace" / "client-config-validation-example.md"
        ).read_text(encoding="utf-8")
        self.assertEqual(rendered, expected)

    def test_main_writes_markdown_report_to_output_path(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            workspace = Path(tmpdir) / "client-pass"
            config_dir = workspace / "config"
            config_dir.mkdir(parents=True)
            for name in validator.REQUIRED_FILES:
                source = REPO_ROOT / "clients" / "[client]" / "config" / name
                (config_dir / name).write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
            output_path = Path(tmpdir) / "reports" / "client-config-validation.md"
            exit_code = validator.main(
                [
                    str(workspace),
                    "--output",
                    str(output_path),
                ]
            )
            self.assertEqual(exit_code, 0)
            self.assertTrue(output_path.is_file())
            text = output_path.read_text(encoding="utf-8")
            self.assertIn("`workspace_name`: `client-pass`", text)
            self.assertIn("`overall_result`: `PASS`", text)

    def test_missing_config_file_surfaces_fail_state_and_missing_file_list(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            workspace = Path(tmpdir) / "client-a"
            config_dir = workspace / "config"
            config_dir.mkdir(parents=True)
            for name in validator.REQUIRED_FILES:
                if name == "metrics-scorecard.md":
                    continue
                source = REPO_ROOT / "clients" / "[client]" / "config" / name
                (config_dir / name).write_text(source.read_text(encoding="utf-8"), encoding="utf-8")

            report = validator.analyze_workspace(workspace)

        self.assertEqual(report["overall_result"], "FAIL")
        self.assertIn("metrics-scorecard.md", report["missing_files"])
        rendered = validator.render_markdown(report)
        self.assertIn("- `metrics-scorecard.md`", rendered)

    def test_placeholder_only_client_file_fails_live_validation(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            workspace = Path(tmpdir) / "client-b"
            config_dir = workspace / "config"
            config_dir.mkdir(parents=True)
            for name in validator.REQUIRED_FILES:
                source = REPO_ROOT / "clients" / "[client]" / "config" / name
                text = source.read_text(encoding="utf-8")
                if name == "segment-taxonomy.md":
                    text = (
                        "# Segment Taxonomy\n\n## Segments\n\n- `Segment ID`:\n"
                        "  - `Name`:\n  - `Description`:\n"
                    )
                (config_dir / name).write_text(text, encoding="utf-8")

            report = validator.analyze_workspace(workspace)

        self.assertEqual(report["overall_result"], "FAIL")
        by_name = {item["file"]: item for item in report["files"]}
        self.assertEqual(by_name["segment-taxonomy.md"]["status"], "FAIL")
        self.assertIn("unresolved", by_name["segment-taxonomy.md"]["fallback"])

    def test_mixed_real_and_placeholder_content_surfaces_conditional_state(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            workspace = Path(tmpdir) / "client-c"
            config_dir = workspace / "config"
            config_dir.mkdir(parents=True)
            for name in validator.REQUIRED_FILES:
                source = REPO_ROOT / "clients" / "[client]" / "config" / name
                text = source.read_text(encoding="utf-8")
                if name == "client-profile.md":
                    text += "\n- `Known Constraints`:\n"
                (config_dir / name).write_text(text, encoding="utf-8")

            report = validator.analyze_workspace(workspace)

        self.assertEqual(report["overall_result"], "CONDITIONAL")
        by_name = {item["file"]: item for item in report["files"]}
        self.assertEqual(by_name["client-profile.md"]["status"], "CONDITIONAL")


if __name__ == "__main__":
    unittest.main()
