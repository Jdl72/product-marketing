import tempfile
import unittest
from contextlib import redirect_stdout
import io
from pathlib import Path

from tests.test_helpers import REPO_ROOT, load_module


validator = load_module(
    "validate_conversation_synthesis",
    "scripts/validate_conversation_synthesis.py",
)


class ValidateConversationSynthesisUnitTests(unittest.TestCase):
    def setUp(self):
        self.example_path = REPO_ROOT / "examples/conversations/conversation-synthesis-example.md"
        self.example_text = self.example_path.read_text()

    def test_extract_sections_finds_required_sections(self):
        sections = validator.extract_sections(self.example_text)
        self.assertIn("top_recurring_pains", sections)
        self.assertIn("strongly_supported_patterns", sections)
        self.assertIn("contradictory_signals", sections)

    def test_split_bullets_preserves_multiline_entries(self):
        section = "- one\n  Support:\n  `convrec-a`\n- two\n  Support:\n  `convrec-b`\n"
        entries = validator.split_bullets(section)
        self.assertEqual(len(entries), 2)
        self.assertIn("Support:", " ".join(entries[0]))

    def test_validate_text_passes_for_current_example(self):
        errors = validator.validate_text(self.example_text)
        self.assertEqual(errors, [])

    def test_validate_text_fails_when_support_line_missing_record_id(self):
        bad_text = self.example_text.replace(
            "`convrec-fireflies-01KM6GSRBZNXNSKQW5BQNDG2M9`, `convrec-fireflies-01KMDFR8SB2ZEPT3452AFH85F9`",
            "two records",
            1,
        )
        errors = validator.validate_text(bad_text)
        self.assertTrue(any("missing record id citation" in error for error in errors))

    def test_main_returns_nonzero_for_invalid_file(self):
        invalid = """### `top_recurring_pains`\n- Something important\n  Support:\n  no ids here\n"""
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "invalid.md"
            path.write_text(invalid)
            buffer = io.StringIO()
            with redirect_stdout(buffer):
                exit_code = validator.main([str(path)])
            self.assertEqual(exit_code, 1)
            self.assertIn("FAIL:", buffer.getvalue())


if __name__ == "__main__":
    unittest.main()
