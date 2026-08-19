#!/usr/bin/env python3
"""Validate a completed Campaign Messaging House Markdown artifact."""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path


CLAIM_RE = re.compile(r"CLM-P[1-4]\.[1-3]")
PILLAR_RE = re.compile(r"P[1-4]")


def clean(value: str) -> str:
    return value.strip().strip("*`").strip()


def missing(value: str) -> bool:
    normalized = clean(value).lower()
    return not normalized or normalized in {"-", "tbd", "none", "n/a", "not supplied"} or normalized.startswith("<")


def section(text: str, heading: str, next_heading: str | None = None) -> str:
    start = text.find(heading)
    if start < 0:
        return ""
    if next_heading:
        end = text.find(next_heading, start + len(heading))
        if end >= 0:
            return text[start:end]
    return text[start:]


def table_rows(text: str) -> list[list[str]]:
    rows = []
    for line in text.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [clean(cell) for cell in line.strip().strip("|").split("|")]
        if not cells or all(not cell or set(cell) <= {"-", ":"} for cell in cells):
            continue
        rows.append(cells)
    return rows


def two_column_fields(text: str) -> dict[str, str]:
    fields = {}
    for cells in table_rows(text):
        if len(cells) == 2 and cells[0].lower() != "field":
            fields[cells[0]] = cells[1]
    return fields


def gacss_fields(text: str) -> dict[str, str]:
    fields = {}
    for cells in table_rows(text):
        if len(cells) >= 3:
            key = clean(cells[0])
            if key in {"Goals", "Audience", "Channels", "Creative", "Stakeholders"}:
                fields[key] = cells[2]
    return fields


def claim_rows(text: str) -> dict[str, list[str]]:
    claims = {}
    for cells in table_rows(text):
        if len(cells) >= 11 and CLAIM_RE.fullmatch(cells[0]):
            claims[cells[0]] = cells
    return claims


def derivative_data_rows(section_four: str) -> list[list[str]]:
    rows = []
    known_first_cells = {
        "Problem", "Agitate", "Invalidate", "Solve", "Ask",
        "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12",
    }
    for cells in table_rows(section_four):
        if cells and cells[0] in known_first_cells and len(cells) >= 3:
            rows.append(cells)
    return rows


def subsection(text: str, heading: str, next_heading: str | None = None) -> str:
    return section(text, heading, next_heading)


def validate(text: str) -> list[str]:
    errors: list[str] = []
    required_sections = [
        "## SECTION 0 — CAMPAIGN HEADER & VERSION",
        "## SECTION 1 — GACCS BRIEF (GATE 1)",
        "## SECTION 2 — NARRATIVE SPINE",
        "## SECTION 3 — MESSAGE PILLARS & CLAIM LEDGER",
        "## SECTION 4 — DERIVATIVE STRUCTURES",
        "## SECTION 5 — GOVERNANCE & CHANGE LOG",
    ]
    for heading in required_sections:
        if heading not in text:
            errors.append(f"missing section: {heading}")

    s0 = section(text, required_sections[0], required_sections[1])
    s1 = section(text, required_sections[1], required_sections[2])
    s2 = section(text, required_sections[2], required_sections[3])
    s3 = section(text, required_sections[3], required_sections[4])
    s4 = section(text, required_sections[4], required_sections[5])
    s5 = section(text, required_sections[5])

    header = two_column_fields(s0)
    for field in ["Campaign Name", "Campaign Theme", "Operating Mode", "Artifact Status", "Version", "Owner", "Approvers"]:
        if missing(header.get(field, "")):
            errors.append(f"missing header field: {field}")

    mode = clean(header.get("Operating Mode", ""))
    artifact_status = clean(header.get("Artifact Status", ""))
    if mode not in {"Draft", "Release Ready"}:
        errors.append("Operating Mode must be Draft or Release Ready")
    elif not artifact_status.startswith(mode):
        errors.append(f"Artifact Status must begin with {mode!r} in {mode} mode")

    gacss = gacss_fields(s1)
    for field in ["Goals", "Audience", "Channels", "Creative", "Stakeholders"]:
        if missing(gacss.get(field, "")):
            errors.append(f"missing GACCS field: {field}")
    stakeholder_value = gacss.get("Stakeholders", "").lower()
    if stakeholder_value and ("owner" not in stakeholder_value or "approver" not in stakeholder_value):
        errors.append("Stakeholders must name an owner and approver")

    timeline = two_column_fields(s1)
    for field in ["Campaign Start", "Campaign End", "Creative Freeze"]:
        if missing(timeline.get(field, "")):
            errors.append(f"missing execution timeline field: {field}")

    gate_match = re.search(r"\*\*GACCS Gate Status:\*\*\s*`?([^`\n]+)", s1)
    gate_status = clean(gate_match.group(1)) if gate_match else ""
    if not gate_status:
        errors.append("missing GACCS Gate Status")

    grounding_match = re.search(r"\*\*Narrative Grounding Status:\*\*\s*`?([^`\n]+)", s2)
    grounding_status = clean(grounding_match.group(1)) if grounding_match else ""
    if not grounding_status:
        errors.append("missing Narrative Grounding Status")
    elif mode == "Release Ready" and not grounding_status.startswith("Pass"):
        errors.append("Release Ready requires passing narrative grounding")

    expected_steps = {
        1: "Insight", 2: "Alternatives", 3: "Perfect World", 4: "Introduction",
        5: "Differentiated Value", 6: "Proof", 7: "Objections", 8: "Ask",
    }
    if grounding_status.startswith("Pass"):
        for number, label in expected_steps.items():
            if not re.search(rf"\*\*Step {number} — {re.escape(label)}\*\*", s2):
                errors.append(f"missing narrative component: Step {number} — {label}")

    pillar_ids = []
    for cells in table_rows(s3):
        if len(cells) >= 5 and PILLAR_RE.fullmatch(cells[0]):
            pillar_ids.append(cells[0])
    if grounding_status.startswith("Pass") and not 3 <= len(set(pillar_ids)) <= 4:
        errors.append("a grounded narrative must contain 3–4 unique pillars")

    claims = claim_rows(s3)
    counts = Counter()
    for claim_id, cells in claims.items():
        pillar = cells[1]
        status = cells[6]
        counts[pillar] += 1
        if pillar not in pillar_ids:
            errors.append(f"{claim_id} references unknown pillar {pillar}")
        if status not in {"Proven", "Provisional", "Unsupported"}:
            errors.append(f"{claim_id} has invalid status {status!r}")
        if status == "Proven" and any(missing(cells[index]) for index in (3, 4, 5)):
            errors.append(
                f"{claim_id} is Proven but lacks proof source, source date, or verifier"
            )
        if status == "Provisional" and (missing(cells[9]) or missing(cells[10])):
            errors.append(f"{claim_id} is Provisional but lacks evidence owner or due date")
    for pillar, count in counts.items():
        if count > 3:
            errors.append(f"{pillar} has {count} claims; maximum is 3")

    if mode == "Draft":
        if "Withheld — Draft mode" not in s4:
            errors.append("Draft mode must mark Section 4 as Withheld — Draft mode")
        if derivative_data_rows(s4):
            populated = [row for row in derivative_data_rows(s4) if any(not missing(cell) for cell in row[2:])]
            if populated:
                errors.append("Draft mode must not contain populated derivative rows")

    if mode == "Release Ready":
        if not gate_status.startswith("Pass"):
            errors.append("Release Ready requires a passing GACCS gate")
        if "Generated — Release Ready" not in s4:
            errors.append("Release Ready must mark Section 4 as Generated — Release Ready")
        for pillar in set(pillar_ids):
            if not any(cells[1] == pillar and cells[6] == "Proven" for cells in claims.values()):
                errors.append(f"Release Ready pillar {pillar} lacks a Proven claim")

        derivative_refs = set(CLAIM_RE.findall(s4))
        for claim_id in sorted(derivative_refs):
            if claim_id not in claims:
                errors.append(f"Section 4 cites unknown claim {claim_id}")
            elif claims[claim_id][6] != "Proven":
                errors.append(f"Section 4 cites non-Proven claim {claim_id}")
        for claim_id, cells in claims.items():
            if cells[6] == "Proven" and claim_id not in derivative_refs:
                errors.append(f"Proven claim {claim_id} is not used in a derivative")

        paisa = subsection(s4, "### 4.1 PAISA Sequence", "### 4.2 Contrast Loop Beat Sheet")
        contrast = subsection(s4, "### 4.2 Contrast Loop Beat Sheet", "### 4.3 Hook Candidates")
        hooks = subsection(s4, "### 4.3 Hook Candidates", "### Coverage Check")
        paisa_rows = [row for row in table_rows(paisa) if row and row[0] in {"Problem", "Agitate", "Invalidate", "Solve", "Ask"}]
        contrast_rows = [row for row in table_rows(contrast) if row and row[0] in {str(i) for i in range(1, 8)}]
        hook_rows = [row for row in table_rows(hooks) if row and row[0] in {str(i) for i in range(1, 13)}]
        if len(paisa_rows) != 5:
            errors.append("Release Ready requires all 5 PAISA beats")
        if len(contrast_rows) != 7:
            errors.append("Release Ready requires all 7 Contrast Loop beats")
        if len(hook_rows) != 12:
            errors.append("Release Ready requires all 12 hook candidates")
        recommended = [row for row in hook_rows if len(row) >= 5 and clean(row[4]).lower() in {"yes", "recommended"}]
        if len(recommended) != 3:
            errors.append("Release Ready requires exactly 3 recommended hooks")

        rows = derivative_data_rows(s4)
        for row in rows:
            if row[0] in {"Problem", "Agitate", "Invalidate", "Solve", "Ask"}:
                content, claim_cell = row[1], row[2]
            elif len(row) == 4:  # Contrast Loop
                content, claim_cell = row[2], row[3]
            else:  # Hook candidates
                content, claim_cell = row[2], row[3]
            refs = CLAIM_RE.findall(claim_cell)
            if not missing(content) and not refs:
                errors.append(f"derivative row {row[0]} has copy but no claim ID")

        validation_rows = {cells[0]: cells[1] for cells in table_rows(s5) if len(cells) >= 2}
        if validation_rows.get("Message test") != "Pass":
            errors.append("Release Ready requires a passing Message test")
        if validation_rows.get("Campaign certification") != "Pass":
            errors.append("Release Ready requires passing Campaign certification")

    if "## SECTION 5 — GOVERNANCE & CHANGE LOG" not in s5:
        errors.append("governance must be completed in every mode")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("artifact", type=Path)
    args = parser.parse_args()
    text = args.artifact.read_text(encoding="utf-8")
    errors = validate(text)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Campaign Messaging House validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
