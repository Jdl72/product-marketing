"""Tests for the Campaign Messaging House artifact validator."""

import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tests.test_helpers import REPO_ROOT


VALIDATOR_PATH = (
    REPO_ROOT
    / "skills/lpa-campaign-messaging-house/scripts/validate_campaign_messaging_house.py"
)
SPEC = importlib.util.spec_from_file_location("campaign_house_validator", VALIDATOR_PATH)
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


def artifact(mode="Draft", claim_status="Provisional", include_stakeholders=True, include_ask=True):
    section_status = "Withheld — Draft mode" if mode == "Draft" else "Generated — Release Ready"
    proof_source = "SRC-01"
    proof_date = "2026-08-01"
    owner = "PMM"
    due = "2026-08-30"
    stakeholders = "Owner: PMM; approver: VP Marketing" if include_stakeholders else ""
    ask = "**Step 8 — Ask**\n\nBook a working session." if include_ask else ""
    derivative = ""
    if mode == "Release Ready":
        derivative = """### 4.1 PAISA Sequence
| Beat | Copy | Claim IDs |
|---|---|---|
| Problem | Buyer problem [CLM-P1.1] | CLM-P1.1 |
| Agitate | Cost of delay [CLM-P1.1] | CLM-P1.1 |
| Invalidate | Old approach fails [CLM-P2.1] | CLM-P2.1 |
| Solve | Product value [CLM-P2.1] | CLM-P2.1 |
| Ask | Take action [CLM-P3.1] | CLM-P3.1 |

### 4.2 Contrast Loop Beat Sheet
| Beat | State | Content | Claim IDs |
|---|---|---|---|
| 1 | What Is | Current pain | CLM-P1.1 |
| 2 | What Could Be | Better state | CLM-P2.1 |
| 3 | What Is | Current pain | CLM-P1.1 |
| 4 | What Could Be | Better state | CLM-P2.1 |
| 5 | What Is | Current pain | CLM-P1.1 |
| 6 | What Could Be | Better state | CLM-P2.1 |
| 7 | New Bliss | Outcome | CLM-P3.1 |

### 4.3 Hook Candidates
| # | Hook Type | Candidate | Claim IDs | Recommended? |
|---|---|---|---|---|
| 1 | Contrarian | Hook 1 | CLM-P1.1 | Yes |
| 2 | Contrarian | Hook 2 | CLM-P1.1 | Yes |
| 3 | Surprising | Hook 3 | CLM-P2.1 | Yes |
| 4 | Surprising | Hook 4 | CLM-P2.1 | No |
| 5 | Overcome Objections | Hook 5 | CLM-P3.1 | No |
| 6 | Overcome Objections | Hook 6 | CLM-P3.1 | No |
| 7 | Guarantee | Hook 7 | CLM-P1.1 | No |
| 8 | Guarantee | Hook 8 | CLM-P1.1 | No |
| 9 | Interest | Hook 9 | CLM-P2.1 | No |
| 10 | Interest | Hook 10 | CLM-P2.1 | No |
| 11 | How To with a Twist | Hook 11 | CLM-P3.1 | No |
| 12 | How To with a Twist | Hook 12 | CLM-P3.1 | No |

### Coverage Check
"""
    validation = "Pass" if mode == "Release Ready" else "Not run"
    return f"""# Campaign Messaging House

## SECTION 0 — CAMPAIGN HEADER & VERSION
| Field | Value |
|---|---|
| Campaign Name | Campaign |
| Campaign Theme | Theme |
| Operating Mode | {mode} |
| Artifact Status | {mode} |
| Version | v1.0 |
| Owner | PMM |
| Approvers | VP Marketing |

## SECTION 1 — GACCS BRIEF (GATE 1)
| GACCS Field | Requirement | Value |
|---|---|---|
| Goals | Metric | 100 demos by 2026-10-31 |
| Audience | ICP | Controllers at SaaS companies |
| Channels | Distribution | LinkedIn and email |
| Creative | Angle | Catch blockers before close week |
| Stakeholders | Team | {stakeholders} |
| Field | Value |
|---|---|
| Campaign Start | 2026-09-15 |
| Campaign End | 2026-10-31 |
| Creative Freeze | 2026-09-08 |
**GACCS Gate Status:** `Pass`

## SECTION 2 — NARRATIVE SPINE
**Narrative Grounding Status:** `Pass`
**Step 1 — Insight**
**Step 2 — Alternatives**
**Step 3 — Perfect World**
**Step 4 — Introduction**
**Step 5 — Differentiated Value**
**Step 6 — Proof**
**Step 7 — Objections**
{ask}

## SECTION 3 — MESSAGE PILLARS & CLAIM LEDGER
| ID | Pillar Name | Criterion ID | Audience Relevance | Status |
|---|---|---|---|---|
| P1 | Visibility | CRIT-01 | Controllers | Validated |
| P2 | Ownership | CRIT-02 | Controllers | Validated |
| P3 | Confidence | CRIT-03 | Controllers | Validated |
| Claim ID | Pillar | Claim text | Proof ID or source | Source date | Verified by | Status | Approved phrasing | Banned phrasing | Evidence owner | Due date |
|---|---|---|---|---|---|---|---|---|---|---|
| CLM-P1.1 | P1 | Claim one | {proof_source} | {proof_date} | Analyst | {claim_status} | Approved | Banned | {owner} | {due} |
| CLM-P2.1 | P2 | Claim two | {proof_source} | {proof_date} | Analyst | {claim_status} | Approved | Banned | {owner} | {due} |
| CLM-P3.1 | P3 | Claim three | {proof_source} | {proof_date} | Analyst | {claim_status} | Approved | Banned | {owner} | {due} |

## SECTION 4 — DERIVATIVE STRUCTURES
**Section Status:** `{section_status}`
{derivative}

## SECTION 5 — GOVERNANCE & CHANGE LOG
| Gate | Result | Evidence or blocker |
|---|---|---|
| Deterministic validator | Pass | local run |
| Message test | {validation} | test record |
| Campaign certification | {validation} | scorecard |
"""


class CampaignMessagingHouseValidatorTests(unittest.TestCase):
    def test_valid_draft_passes(self):
        self.assertEqual(VALIDATOR.validate(artifact()), [])

    def test_valid_release_ready_passes(self):
        self.assertEqual(
            VALIDATOR.validate(artifact(mode="Release Ready", claim_status="Proven")),
            [],
        )

    def test_requires_stakeholders_in_gaccs(self):
        errors = VALIDATOR.validate(artifact(include_stakeholders=False))
        self.assertIn("missing GACCS field: Stakeholders", errors)

    def test_requires_separate_ask_component(self):
        errors = VALIDATOR.validate(artifact(include_ask=False))
        self.assertIn("missing narrative component: Step 8 — Ask", errors)

    def test_release_ready_rejects_provisional_derivatives(self):
        errors = VALIDATOR.validate(
            artifact(mode="Release Ready", claim_status="Provisional")
        )
        self.assertTrue(any("lacks a Proven claim" in error for error in errors))
        self.assertTrue(any("cites non-Proven claim" in error for error in errors))

    def test_blocked_draft_does_not_require_invented_narrative(self):
        blocked = artifact().replace(
            "**Narrative Grounding Status:** `Pass`",
            "**Narrative Grounding Status:** `Blocked: no product or buyer evidence`",
        )
        blocked = blocked.replace("**Step 8 — Ask**\n\nBook a working session.", "")
        self.assertNotIn(
            "missing narrative component: Step 8 — Ask",
            VALIDATOR.validate(blocked),
        )

    def test_cli_accepts_valid_artifact(self):
        with tempfile.TemporaryDirectory() as directory:
            artifact_path = Path(directory) / "campaign-house.md"
            artifact_path.write_text(artifact(), encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(VALIDATOR_PATH), str(artifact_path)],
                capture_output=True,
                check=False,
                text=True,
            )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("validation passed", result.stdout)


if __name__ == "__main__":
    unittest.main()
