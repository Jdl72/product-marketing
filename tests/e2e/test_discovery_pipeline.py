import re
import subprocess
import tempfile
import unittest
from pathlib import Path

from tests.test_helpers import REPO_ROOT


class DiscoveryPipelineEndToEndTests(unittest.TestCase):
    def setUp(self):
        self.builder_script = REPO_ROOT / "scripts/build_conversation_synthesis_input.py"
        self.validator_script = REPO_ROOT / "scripts/validate_conversation_synthesis.py"
        self.ejam = REPO_ROOT / "examples/conversations/parsed-fireflies-ejam-pricing-follow-up.md"
        self.schleich = REPO_ROOT / "examples/conversations/parsed-fireflies-schleich-copenhagen-dsp.md"
        self.synthesis_example = REPO_ROOT / "examples/conversations/conversation-synthesis-example.md"

    def test_records_to_pack_and_validation_flow(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            generated = Path(tmpdir) / "generated-pack.md"
            build_result = subprocess.run(
                [
                    "python3",
                    str(self.builder_script),
                    str(self.ejam),
                    str(self.schleich),
                    "--objective",
                    "e2e synthesis",
                    "--segment",
                    "e2e segment",
                    "--persona-scope",
                    "e2e persona",
                    "--time-window",
                    "2026-03-20 to 2026-03-23",
                    "--output",
                    str(generated),
                ],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(build_result.returncode, 0, build_result.stderr)
            generated_text = generated.read_text()
            self.assertIn("convrec-fireflies-01KM6GSRBZNXNSKQW5BQNDG2M9", generated_text)
            self.assertIn("Sam Sutcu [sentence 231, 14:15-14:24]", generated_text)

            validate_result = subprocess.run(
                ["python3", str(self.validator_script), str(self.synthesis_example)],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(validate_result.returncode, 0, validate_result.stderr)
            self.assertIn("PASS:", validate_result.stdout)

    def test_generated_pack_carries_both_record_ids(self):
        """
        The generated input pack must carry both record IDs so the synthesis step
        can produce record-level citations for every pattern.
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            generated = Path(tmpdir) / "pack-record-ids.md"
            build_result = subprocess.run(
                [
                    "python3",
                    str(self.builder_script),
                    str(self.ejam),
                    str(self.schleich),
                    "--objective",
                    "record id traceability test",
                    "--segment",
                    "e2e segment",
                    "--persona-scope",
                    "e2e persona",
                    "--time-window",
                    "2026-03-20 to 2026-03-23",
                    "--output",
                    str(generated),
                ],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(build_result.returncode, 0, build_result.stderr)
            text = generated.read_text()
            self.assertIn(
                "convrec-fireflies-01KM6GSRBZNXNSKQW5BQNDG2M9",
                text,
                "generated pack must include Ejam record ID for downstream pattern citation",
            )
            self.assertIn(
                "convrec-fireflies-01KMDFR8SB2ZEPT3452AFH85F9",
                text,
                "generated pack must include Schleich record ID for downstream pattern citation",
            )

    def test_generated_pack_preserves_quote_citation_anchors(self):
        """
        Quote citation anchors (sentence number and timestamp) must survive the build step
        so the synthesis has traceable representative quotes.
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            generated = Path(tmpdir) / "pack-quote-anchors.md"
            build_result = subprocess.run(
                [
                    "python3",
                    str(self.builder_script),
                    str(self.ejam),
                    str(self.schleich),
                    "--objective",
                    "quote anchor traceability test",
                    "--segment",
                    "e2e segment",
                    "--persona-scope",
                    "e2e persona",
                    "--time-window",
                    "2026-03-20 to 2026-03-23",
                    "--output",
                    str(generated),
                ],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(build_result.returncode, 0, build_result.stderr)
            text = generated.read_text()
            # Sentence-level anchor from the Ejam example
            self.assertIn(
                "sentence 231",
                text,
                "generated pack must preserve sentence-level citation anchors from parsed records",
            )
            # Timestamp anchor from the Ejam example
            self.assertIn(
                "14:15-14:24",
                text,
                "generated pack must preserve timestamp anchors from parsed records",
            )

    def test_synthesis_example_record_citations_are_traceable_to_parsed_examples(self):
        """
        Every convrec-ID in the synthesis example must correspond to a record_id
        that appears in the parsed example files, confirming end-to-end traceability.
        """
        synthesis_text = self.synthesis_example.read_text()
        ejam_text = self.ejam.read_text()
        schleich_text = self.schleich.read_text()

        # Extract all convrec-IDs from the synthesis
        cited_ids = set(re.findall(r"convrec-[\w-]+", synthesis_text))
        self.assertGreater(len(cited_ids), 0, "synthesis example must cite at least one convrec-ID")

        # Each cited ID must appear in one of the parsed source files
        all_source_text = ejam_text + schleich_text
        for convrec_id in cited_ids:
            self.assertIn(
                convrec_id,
                all_source_text,
                f"synthesis cites '{convrec_id}' but that record ID does not appear in the parsed example files",
            )

    def test_synthesis_example_passes_validator(self):
        """
        The synthesis example must pass the automated validator, confirming that every
        strongly_supported and emerging pattern has a record-level citation.
        """
        validate_result = subprocess.run(
            ["python3", str(self.validator_script), str(self.synthesis_example)],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(validate_result.returncode, 0, validate_result.stderr)
        self.assertIn("PASS:", validate_result.stdout)

    def test_synthesis_example_representative_quotes_have_record_and_anchor(self):
        """
        Representative quotes in the synthesis example must include both a record ID
        and a citation anchor (sentence number or timestamp).
        """
        synthesis_text = self.synthesis_example.read_text()
        # Find the representative_quotes section
        match = re.search(
            r"### `representative_quotes`(.*?)##",
            synthesis_text,
            re.DOTALL,
        )
        self.assertIsNotNone(match, "synthesis example must have a representative_quotes section")
        quotes_section = match.group(1)

        # Each quote line that has a convrec- citation should also have a sentence or timestamp anchor
        quote_lines = [
            line for line in quotes_section.splitlines()
            if "convrec-" in line
        ]
        self.assertGreater(
            len(quote_lines),
            0,
            "at least one representative quote must include a record ID citation",
        )
        for line in quote_lines:
            has_anchor = "sentence" in line.lower() or re.search(r"\d+:\d+-\d+:\d+", line)
            self.assertTrue(
                has_anchor,
                f"representative quote missing citation anchor (sentence or timestamp): {line.strip()}",
            )


if __name__ == "__main__":
    unittest.main()
