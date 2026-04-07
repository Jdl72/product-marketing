import io
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from tests.test_helpers import REPO_ROOT, load_module


validator = load_module(
    "validate_workflow_contracts_integration",
    "scripts/validate_workflow_contracts.py",
)


class WorkflowContractValidatorIntegrationTests(unittest.TestCase):
    def test_main_passes_for_contract_directory(self):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            exit_code = validator.main([str(REPO_ROOT / "docs" / "contracts")])
        self.assertEqual(exit_code, 0)
        self.assertIn("PASS:", buffer.getvalue())

    def test_all_contracts_reference_existing_schemas(self):
        contracts_dir = REPO_ROOT / "docs" / "contracts"
        for path in contracts_dir.glob("*-workflow-contract.md"):
            text = path.read_text(encoding="utf-8")
            match = validator.SCHEMA_LINK_RE.search(text)
            self.assertIsNotNone(match, f"{path.name} should link a schema")
            schema_target = match.group(2)
            schema_path = (path.parent / Path(schema_target)).resolve()
            self.assertTrue(schema_path.exists(), f"{path.name} should point to an existing schema")
            self.assertTrue(schema_path.is_relative_to(REPO_ROOT), f"{path.name} should resolve inside the repo")


if __name__ == "__main__":
    unittest.main()
