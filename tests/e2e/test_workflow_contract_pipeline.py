import subprocess
import tempfile
import unittest
from pathlib import Path

from tests.test_helpers import REPO_ROOT


class WorkflowContractPipelineEndToEndTests(unittest.TestCase):
    def setUp(self):
        self.script = REPO_ROOT / "scripts" / "validate_workflow_contracts.py"
        self.contracts_dir = REPO_ROOT / "docs" / "contracts"

    def test_validator_runs_via_subprocess_on_contract_directory(self):
        result = subprocess.run(
            ["python3", str(self.script), str(self.contracts_dir)],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("PASS:", result.stdout)

    def test_validator_runs_via_subprocess_on_single_contract_file(self):
        contract = self.contracts_dir / "positioning-brief-workflow-contract.md"
        result = subprocess.run(
            ["python3", str(self.script), str(contract)],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("PASS:", result.stdout)


if __name__ == "__main__":
    unittest.main()
