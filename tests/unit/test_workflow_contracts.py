import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from tests.test_helpers import REPO_ROOT, load_module


validator = load_module(
    "validate_workflow_contracts",
    "scripts/validate_workflow_contracts.py",
)


CONTRACTS_DIR = REPO_ROOT / "docs" / "contracts"
CONTRACT_FILES = (
    "positioning-brief-workflow-contract.md",
    "persona-pack-workflow-contract.md",
    "gtm-plan-workflow-contract.md",
    "battle-card-workflow-contract.md",
    "content-calendar-workflow-contract.md",
)


class WorkflowContractsUnitTests(unittest.TestCase):
    def test_template_has_all_required_sections(self):
        text = (CONTRACTS_DIR / "workflow-input-output-template.md").read_text(encoding="utf-8")
        for section in validator.REQUIRED_SECTIONS:
            self.assertIn(section, text)

    def test_contract_docs_exist(self):
        for name in CONTRACT_FILES:
            self.assertTrue((CONTRACTS_DIR / name).is_file(), f"{name} must exist")

    def test_validator_passes_for_current_contract_directory(self):
        errors = validator.validate_directory(CONTRACTS_DIR)
        self.assertEqual(errors, [])

    def test_validator_fails_when_required_section_missing(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            broken = Path(tmpdir) / "broken-workflow-contract.md"
            broken.write_text(
                "# Broken\n\n## Purpose\nx\n\n## Output artifact\n- schema: [foo.md](/tmp/schemas/foo.md)\n",
                encoding="utf-8",
            )
            errors = validator.validate_contract(broken)
            self.assertTrue(any("missing section" in error for error in errors))

    def test_main_returns_nonzero_for_invalid_contract(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            broken = Path(tmpdir) / "broken-workflow-contract.md"
            broken.write_text("# Broken\n", encoding="utf-8")
            buffer = io.StringIO()
            with redirect_stdout(buffer):
                exit_code = validator.main([str(broken)])
            self.assertEqual(exit_code, 1)
            self.assertIn("FAIL:", buffer.getvalue())


if __name__ == "__main__":
    unittest.main()
