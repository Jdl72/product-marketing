import unittest
from pathlib import Path

from tests.test_helpers import REPO_ROOT


class ParsingWorkflowTests(unittest.TestCase):
    def setUp(self):
        self.job_spec = REPO_ROOT / "jobs/parse-single-conversation.md"
        self.job_text = self.job_spec.read_text()

        self.schema = REPO_ROOT / "schemas/conversation-record.md"
        self.schema_text = self.schema.read_text()

        self.ejam_example = REPO_ROOT / "examples/conversations/parsed-fireflies-ejam-pricing-follow-up.md"
        self.schleich_example = REPO_ROOT / "examples/conversations/parsed-fireflies-schleich-copenhagen-dsp.md"

    # --- Parsed example existence ---

    def test_at_least_one_parsed_example_exists(self):
        examples_dir = REPO_ROOT / "examples/conversations"
        parsed_files = [
            f for f in examples_dir.iterdir()
            if f.is_file() and "parsed" in f.name and f.suffix == ".md"
        ]
        self.assertGreater(
            len(parsed_files),
            0,
            "At least one parsed conversation example must exist in examples/conversations/",
        )

    def test_ejam_example_exists(self):
        self.assertTrue(
            self.ejam_example.exists(),
            "examples/conversations/parsed-fireflies-ejam-pricing-follow-up.md must exist",
        )

    # --- Job spec: stakeholder mapping ---

    def test_job_spec_requires_stakeholder_mapping(self):
        text_lower = self.job_text.lower()
        self.assertIn(
            "stakeholder",
            text_lower,
            "parse-single-conversation.md must mention stakeholder mapping",
        )

    def test_job_spec_stakeholder_map_applies_to_multi_party_calls(self):
        text_lower = self.job_text.lower()
        self.assertTrue(
            "multiple external stakeholders" in text_lower
            or "multi-party" in text_lower
            or "stakeholder_map" in text_lower,
            "job spec must address stakeholder mapping for multi-party or multi-stakeholder calls",
        )

    # --- Job spec: quote attribution ---

    def test_job_spec_requires_speaker_attribution(self):
        text_lower = self.job_text.lower()
        self.assertTrue(
            "speaker attribution" in text_lower or "attribute quotes" in text_lower,
            "job spec must require speaker attribution on quoted language",
        )

    # --- Job spec: transcript anchors ---

    def test_job_spec_requires_transcript_anchors(self):
        text_lower = self.job_text.lower()
        self.assertTrue(
            "sentence-level" in text_lower or "timestamp-level" in text_lower or "citation anchor" in text_lower,
            "job spec must require sentence-level or timestamp-level citation anchors on notable quotes",
        )

    # --- Job spec: evidence vs interpretation separation ---

    def test_job_spec_requires_evidence_interpretation_separation(self):
        text_lower = self.job_text.lower()
        self.assertTrue(
            "evidence vs interpretation" in text_lower
            or "separate" in text_lower,
            "job spec must require separation of evidence and interpretation",
        )

    # --- Job spec: review gate covers term normalization ---

    def test_job_spec_review_gate_covers_term_normalization(self):
        self.assertIn(
            "Term normalization",
            self.job_text,
            "human review gate must explicitly cover term normalization as an active check",
        )

    def test_job_spec_review_gate_covers_quote_fidelity(self):
        self.assertIn(
            "Quote fidelity",
            self.job_text,
            "human review gate must explicitly cover quote fidelity",
        )

    def test_job_spec_review_gate_covers_speaker_attribution(self):
        self.assertIn(
            "Speaker attribution",
            self.job_text,
            "human review gate must explicitly cover speaker attribution",
        )

    def test_job_spec_review_gate_covers_transcript_citation_anchors(self):
        self.assertIn(
            "Transcript citation anchors",
            self.job_text,
            "human review gate must explicitly cover transcript citation anchors",
        )

    def test_job_spec_review_gate_covers_evidence_vs_interpretation(self):
        self.assertIn(
            "Evidence vs interpretation",
            self.job_text,
            "human review gate must explicitly cover evidence vs interpretation separation",
        )

    def test_job_spec_review_gate_covers_stakeholder_mapping(self):
        self.assertIn(
            "Stakeholder mapping",
            self.job_text,
            "human review gate must explicitly cover stakeholder mapping for multi-party calls",
        )

    # --- Schema: required fields ---

    def test_schema_has_stakeholder_map_field(self):
        self.assertIn(
            "stakeholder_map",
            self.schema_text,
            "conversation-record schema must include stakeholder_map field",
        )

    def test_schema_has_notable_quotes_with_citation_guidance(self):
        self.assertIn(
            "notable_quotes",
            self.schema_text,
            "schema must include notable_quotes field",
        )
        self.assertTrue(
            "sentence" in self.schema_text.lower() or "timestamp" in self.schema_text.lower(),
            "schema notable_quotes guidance must mention sentence or timestamp citation format",
        )

    def test_schema_has_term_normalization_notes_field(self):
        self.assertIn(
            "term_normalization_notes",
            self.schema_text,
            "schema must include term_normalization_notes field",
        )

    # --- Example: schema completeness ---

    def test_ejam_example_has_record_id(self):
        text = self.ejam_example.read_text()
        self.assertIn("record_id", text)

    def test_ejam_example_has_notable_quotes_with_speaker_attribution(self):
        text = self.ejam_example.read_text()
        self.assertIn("notable_quotes", text)
        self.assertIn("Sam Sutcu", text, "quoted language must be attributed to a named speaker")

    def test_ejam_example_has_transcript_citation_anchors(self):
        text = self.ejam_example.read_text()
        self.assertTrue(
            "sentence" in text.lower() or "timestamp" in text.lower(),
            "parsed example must include sentence-level or timestamp citation anchors on quotes",
        )

    def test_ejam_example_has_term_normalization_notes(self):
        text = self.ejam_example.read_text()
        self.assertIn(
            "term_normalization_notes",
            text,
            "parsed example must include term_normalization_notes field",
        )

    def test_ejam_example_has_stakeholder_map(self):
        text = self.ejam_example.read_text()
        self.assertIn(
            "stakeholder_map",
            text,
            "parsed example must include stakeholder_map field",
        )

    def test_ejam_example_can_feed_synthesis(self):
        """
        Confirm the parsed example has the fields synthesis needs:
        record_id, primary_pains, notable_quotes, evidence_strength.
        """
        text = self.ejam_example.read_text()
        for field in ["record_id", "primary_pains", "notable_quotes", "evidence_strength"]:
            self.assertIn(
                field,
                text,
                f"parsed example must include '{field}' so it can feed the synthesis job",
            )

    def test_schleich_example_has_multi_stakeholder_map(self):
        """
        The Schleich call has two named external stakeholders — the stakeholder_map must
        reflect both rather than collapsing them.
        """
        text = self.schleich_example.read_text()
        self.assertIn("stakeholder_map", text)
        # Both stakeholder names should appear
        self.assertIn("Silas", text, "multi-party example must name Silas as a stakeholder")
        self.assertIn("Larysa", text, "multi-party example must name Larysa as a stakeholder")


if __name__ == "__main__":
    unittest.main()
