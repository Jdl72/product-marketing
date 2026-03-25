import re
import unittest
from pathlib import Path

from tests.test_helpers import REPO_ROOT


class SynthesisWorkflowTests(unittest.TestCase):
    def setUp(self):
        self.job_spec = REPO_ROOT / "jobs/synthesize-conversation-set.md"
        self.job_text = self.job_spec.read_text()

        self.schema = REPO_ROOT / "schemas/conversation-synthesis.md"
        self.schema_text = self.schema.read_text()

        self.synthesis_example = REPO_ROOT / "examples/conversations/conversation-synthesis-example.md"
        self.synthesis_text = self.synthesis_example.read_text()

    # --- Synthesis example existence ---

    def test_synthesis_example_exists(self):
        self.assertTrue(
            self.synthesis_example.exists(),
            "examples/conversations/conversation-synthesis-example.md must exist",
        )

    # --- Job spec: record-level citations ---

    def test_job_spec_requires_record_level_citations(self):
        text_lower = self.job_text.lower()
        self.assertTrue(
            "convrec-" in text_lower or "record-level citation" in text_lower or "convrec-id" in text_lower,
            "synthesize-conversation-set.md must require record-level citations (convrec-ID) on patterns",
        )

    def test_job_spec_no_pattern_without_citation_rule(self):
        self.assertIn(
            "No pattern",
            self.job_text,
            "job spec must state that no pattern claim is allowed without a record citation",
        )

    # --- Job spec: pattern separation ---

    def test_job_spec_requires_strongly_supported_patterns(self):
        self.assertIn(
            "strongly supported",
            self.job_text.lower(),
            "job spec must require a strongly_supported_patterns section",
        )

    def test_job_spec_requires_emerging_patterns(self):
        self.assertIn(
            "emerging",
            self.job_text.lower(),
            "job spec must require an emerging_patterns section",
        )

    def test_job_spec_requires_contradictory_signals(self):
        self.assertIn(
            "contradiction",
            self.job_text.lower(),
            "job spec must require contradictory signals to be preserved",
        )

    # --- Job spec: overgeneralization guard ---

    def test_job_spec_has_overgeneralization_guard(self):
        self.assertIn(
            "Overgeneralization guard",
            self.job_text,
            "job spec must have an explicit overgeneralization guard section",
        )

    def test_job_spec_requires_minimum_records_for_strongly_supported(self):
        self.assertIn(
            "two or more independent records",
            self.job_text,
            "overgeneralization guard must state a minimum of two records for strongly_supported patterns",
        )

    def test_job_spec_requires_five_records_for_segment_level_claims(self):
        self.assertIn(
            "five independent records",
            self.job_text,
            "overgeneralization guard must require at least five records before making segment-level claims",
        )

    def test_job_spec_requires_coverage_notes_field(self):
        self.assertIn(
            "coverage_notes",
            self.job_text,
            "job spec must require a coverage_notes field with record count and sampling limitations",
        )

    # --- Job spec: downstream linkage ---

    def test_job_spec_links_to_persona_downstream_artifact(self):
        text_lower = self.job_text.lower()
        self.assertIn(
            "persona",
            text_lower,
            "job spec must link to persona as a downstream artifact",
        )

    def test_job_spec_links_to_positioning_downstream_artifact(self):
        text_lower = self.job_text.lower()
        self.assertIn(
            "positioning",
            text_lower,
            "job spec must link to positioning as a downstream artifact",
        )

    def test_job_spec_downstream_section_references_issue_numbers(self):
        """
        The downstream linkage section should reference specific downstream artifacts
        (e.g., issue #10 for persona, issue #12 for positioning).
        """
        self.assertTrue(
            "#10" in self.job_text or "#12" in self.job_text,
            "downstream linkage section should reference specific downstream issues (#10, #12) so users know where synthesis feeds",
        )

    # --- Job spec: review gate ---

    def test_job_spec_review_gate_covers_record_level_traceability(self):
        self.assertIn(
            "Record-level traceability",
            self.job_text,
            "human review gate must explicitly check record-level traceability",
        )

    def test_job_spec_review_gate_covers_overgeneralization(self):
        self.assertIn(
            "Overgeneralization",
            self.job_text,
            "human review gate must explicitly check overgeneralization",
        )

    def test_job_spec_review_gate_covers_quote_traceability(self):
        self.assertIn(
            "Quote traceability",
            self.job_text,
            "human review gate must explicitly check quote traceability including record ID citation",
        )

    # --- Schema: required fields ---

    def test_schema_has_strongly_supported_patterns(self):
        self.assertIn("strongly_supported_patterns", self.schema_text)

    def test_schema_has_emerging_patterns(self):
        self.assertIn("emerging_patterns", self.schema_text)

    def test_schema_has_contradictory_signals(self):
        self.assertIn("contradictory_signals", self.schema_text)

    def test_schema_representative_quotes_require_record_citation(self):
        self.assertIn(
            "convrec-",
            self.schema_text,
            "schema representative_quotes format must include record citation (convrec-...)",
        )

    def test_schema_has_recommended_downstream_artifacts(self):
        self.assertIn(
            "recommended_downstream_artifacts",
            self.schema_text,
            "schema must include recommended_downstream_artifacts field",
        )

    # --- Synthesis example: record-level citations ---

    def test_synthesis_example_has_convrec_citations(self):
        self.assertIn(
            "convrec-",
            self.synthesis_text,
            "synthesis example must contain convrec- record citations",
        )

    def test_synthesis_example_strongly_supported_patterns_have_citations(self):
        # Find the strongly_supported_patterns section and verify at least one convrec-ID is present
        match = re.search(
            r"### `strongly_supported_patterns`(.*?)###",
            self.synthesis_text,
            re.DOTALL,
        )
        self.assertIsNotNone(match, "synthesis example must have strongly_supported_patterns section")
        section_text = match.group(1)
        self.assertIn(
            "convrec-",
            section_text,
            "every strongly_supported pattern must cite at least one convrec-ID",
        )

    def test_synthesis_example_emerging_patterns_have_citations(self):
        match = re.search(
            r"### `emerging_patterns`(.*?)###",
            self.synthesis_text,
            re.DOTALL,
        )
        self.assertIsNotNone(match, "synthesis example must have emerging_patterns section")
        section_text = match.group(1)
        self.assertIn(
            "convrec-",
            section_text,
            "every emerging pattern must cite at least one convrec-ID",
        )

    def test_synthesis_example_representative_quotes_have_record_citation(self):
        match = re.search(
            r"### `representative_quotes`(.*?)##",
            self.synthesis_text,
            re.DOTALL,
        )
        self.assertIsNotNone(match, "synthesis example must have representative_quotes section")
        section_text = match.group(1)
        self.assertIn(
            "convrec-",
            section_text,
            "representative quotes must include record-level citations",
        )

    def test_synthesis_example_has_contradictory_signals(self):
        self.assertIn(
            "contradictory_signals",
            self.synthesis_text,
            "synthesis example must have a contradictory_signals section",
        )

    def test_synthesis_example_has_coverage_notes(self):
        self.assertIn(
            "coverage_notes",
            self.synthesis_text,
            "synthesis example must include coverage_notes",
        )

    def test_synthesis_example_has_recommended_downstream_artifacts(self):
        self.assertIn(
            "recommended_downstream_artifacts",
            self.synthesis_text,
            "synthesis example must include recommended_downstream_artifacts",
        )

    def test_synthesis_example_downstream_artifacts_include_persona(self):
        text_lower = self.synthesis_text.lower()
        self.assertIn(
            "persona",
            text_lower,
            "synthesis example recommended_downstream_artifacts must include persona",
        )

    def test_synthesis_example_downstream_artifacts_include_positioning(self):
        text_lower = self.synthesis_text.lower()
        self.assertIn(
            "positioning",
            text_lower,
            "synthesis example recommended_downstream_artifacts must include positioning",
        )


if __name__ == "__main__":
    unittest.main()
