#!/usr/bin/env python3
import argparse
from pathlib import Path


REQUIRED_DIRS = ("briefs", "config", "decisions", "evidence", "records", "syntheses")
REQUIRED_CONFIG_FILES = (
    "client-profile.md",
    "segment-taxonomy.md",
    "funnel-stages.md",
    "competitor-map.md",
    "coding-rules.md",
    "strategic-questions.md",
    "metrics-scorecard.md",
)
REQUIRED_DECISION_FILES = (
    "insight-to-action-tracker.md",
    "open-questions.md",
    "cross-functional-action-log.md",
)
REPO_ROOT = Path(__file__).resolve().parents[1]
WORKSPACE_KIND_MARKER = ".workspace-kind"
MARKDOWN_CONTENT_EXTENSIONS = {".md"}


def detect_workspace_kind(root: Path, explicit_kind: str | None = None) -> str:
    if explicit_kind:
        return explicit_kind

    marker_path = root / WORKSPACE_KIND_MARKER
    if marker_path.is_file():
        marker_value = marker_path.read_text(encoding="utf-8").strip().lower()
        if marker_value in {"template", "client"}:
            return marker_value
        raise ValueError(
            f"{_readable_path(marker_path)} must contain either 'template' or 'client'"
        )

    raise ValueError(
        f"Could not determine workspace kind for {_readable_path(root)}. "
        f"Add a {WORKSPACE_KIND_MARKER} marker file or pass --workspace-kind."
    )


def _readable_path(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _is_nonempty_file(path: Path) -> bool:
    return path.is_file() and bool(path.read_text(encoding="utf-8").strip())


def _list_substantive_files(directory: Path) -> list[str]:
    if not directory.is_dir():
        return []
    return sorted(
        path.name
        for path in directory.iterdir()
        if path.is_file()
        and path.name != "README.md"
        and path.suffix.lower() in MARKDOWN_CONTENT_EXTENSIONS
    )


def collect_workspace_facts(root: Path, *, workspace_kind: str | None = None) -> dict:
    root = root.resolve()
    kind = detect_workspace_kind(root, explicit_kind=workspace_kind)

    dir_presence = {name: (root / name).is_dir() for name in REQUIRED_DIRS}

    config_status = {}
    for name in REQUIRED_CONFIG_FILES:
        path = root / "config" / name
        config_status[name] = {"exists": path.is_file(), "nonempty": _is_nonempty_file(path)}

    decision_status = {}
    for name in REQUIRED_DECISION_FILES:
        path = root / "decisions" / name
        decision_status[name] = {"exists": path.is_file(), "nonempty": _is_nonempty_file(path)}

    facts = {
        "workspace_name": root.name,
        "workspace_path": _readable_path(root),
        "workspace_kind": kind,
        "missing_dirs": [name for name, present in dir_presence.items() if not present],
        "missing_config_files": [name for name, meta in config_status.items() if not meta["exists"]],
        "empty_config_files": [name for name, meta in config_status.items() if meta["exists"] and not meta["nonempty"]],
        "missing_decision_files": [name for name, meta in decision_status.items() if not meta["exists"]],
        "empty_decision_files": [name for name, meta in decision_status.items() if meta["exists"] and not meta["nonempty"]],
        "has_evidence_readme": _is_nonempty_file(root / "evidence" / "README.md"),
        "has_source_inventory": _is_nonempty_file(root / "evidence" / "source-inventory.md"),
        "records_files": _list_substantive_files(root / "records"),
        "syntheses_files": _list_substantive_files(root / "syntheses"),
        "brief_files": _list_substantive_files(root / "briefs"),
        "decision_files": _list_substantive_files(root / "decisions"),
    }
    return facts


def _dimension(dimension_id: str, label: str, status: str, why_it_matters: str, evidence: list[str], next_action: str) -> dict:
    return {
        "dimension_id": dimension_id,
        "label": label,
        "status": status,
        "why_it_matters": why_it_matters,
        "evidence": evidence,
        "next_action": next_action,
    }


def evaluate_workspace(facts: dict) -> dict:
    dimensions = []

    missing_contract = (
        facts["missing_dirs"] or facts["missing_config_files"] or facts["missing_decision_files"]
    )
    contract_status = "FAIL" if missing_contract else "PASS"
    contract_evidence = [
        f"missing_dirs={facts['missing_dirs'] or 'none'}",
        f"missing_config_files={facts['missing_config_files'] or 'none'}",
        f"missing_decision_files={facts['missing_decision_files'] or 'none'}",
    ]
    dimensions.append(
        _dimension(
            "contract_completeness",
            "Contract Completeness",
            contract_status,
            "The workspace must satisfy the core directory and file contract before downstream workflows can rely on it.",
            contract_evidence,
            "Create the missing directories or files required by the workspace contract." if contract_status == "FAIL" else "Keep the contract stable as the workspace grows.",
        )
    )

    config_status = "FAIL"
    if not facts["missing_config_files"] and not facts["empty_config_files"]:
        config_status = "PASS"
    elif not facts["missing_config_files"]:
        config_status = "CONDITIONAL"
    dimensions.append(
        _dimension(
            "config_pack_readiness",
            "Config Pack Readiness",
            config_status,
            "Client config should guide workflow behavior without forcing edits to core jobs, skills, or schemas.",
            [
                f"empty_config_files={facts['empty_config_files'] or 'none'}",
                f"workspace_kind={facts['workspace_kind']}",
            ],
            "Fill in the remaining config placeholders so the workspace can guide scoping and tagging consistently."
            if config_status != "PASS"
            else "Use the config pack as the source of client-specific vocabulary and rules.",
        )
    )

    evidence_status = "FAIL"
    if facts["workspace_kind"] == "template":
        evidence_status = "PASS" if facts["has_evidence_readme"] or facts["has_source_inventory"] else "FAIL"
    else:
        if facts["has_source_inventory"]:
            evidence_status = "PASS"
        elif facts["has_evidence_readme"]:
            evidence_status = "CONDITIONAL"
    dimensions.append(
        _dimension(
            "evidence_readiness",
            "Evidence Readiness",
            evidence_status,
            "A client workspace needs a defined home for provenance so downstream strategy and briefs stay traceable.",
            [
                f"has_evidence_readme={facts['has_evidence_readme']}",
                f"has_source_inventory={facts['has_source_inventory']}",
            ],
            "Add or complete the evidence inventory so sources can be traced before deeper synthesis work."
            if evidence_status != "PASS"
            else "Keep evidence inventories current as new source material is added.",
        )
    )

    decision_status = "FAIL"
    if not facts["missing_decision_files"] and not facts["empty_decision_files"]:
        decision_status = "PASS"
    elif not facts["missing_decision_files"]:
        decision_status = "CONDITIONAL"
    dimensions.append(
        _dimension(
            "decision_layer_readiness",
            "Decision Layer Readiness",
            decision_status,
            "The workspace should provide a stable handoff from evidence and synthesis into action and open questions.",
            [
                f"empty_decision_files={facts['empty_decision_files'] or 'none'}",
                f"decision_file_count={len(facts['decision_files'])}",
            ],
            "Fill in the action and question trackers so evidence can route into operational follow-up."
            if decision_status != "PASS"
            else "Use the tracker files as the durable handoff into decision-making.",
        )
    )

    maturity_status = "CONDITIONAL"
    if facts["workspace_kind"] == "template":
        if (
            facts["has_evidence_readme"]
            and not facts["missing_config_files"]
            and not facts["missing_decision_files"]
        ):
            maturity_status = "PASS"
    else:
        if facts["has_source_inventory"] and (
            facts["decision_files"] or facts["records_files"] or facts["syntheses_files"] or facts["brief_files"]
        ):
            maturity_status = "PASS"
    dimensions.append(
        _dimension(
            "workspace_maturity",
            "Workspace Maturity",
            maturity_status,
            "The evaluation should distinguish a valid scaffold from a workspace that is ready for sustained client use.",
            [
                f"records_files={facts['records_files'] or 'none'}",
                f"syntheses_files={facts['syntheses_files'] or 'none'}",
                f"brief_files={facts['brief_files'] or 'none'}",
            ],
            "Add more live workspace artifacts as evidence work advances."
            if maturity_status != "PASS"
            else "The workspace has enough structure and signal to support recurring use at its current stage.",
        )
    )

    statuses = [dimension["status"] for dimension in dimensions]
    if "FAIL" in statuses:
        overall = "FAIL"
    elif "CONDITIONAL" in statuses:
        overall = "CONDITIONAL"
    else:
        overall = "PASS"

    summary = {
        "PASS": "The workspace satisfies the current contract and is ready for its intended use stage.",
        "CONDITIONAL": "The workspace is structurally usable but still has follow-up gaps before broader scaling.",
        "FAIL": "The workspace is missing required contract elements and should not be treated as ready.",
    }[overall]

    return {
        "workspace_name": facts["workspace_name"],
        "workspace_path": facts["workspace_path"],
        "workspace_kind": facts["workspace_kind"],
        "overall_result": overall,
        "summary": summary,
        "dimensions": dimensions,
    }


def render_markdown(evaluation: dict) -> str:
    lines = [
        "# Client Workspace Evaluation",
        "",
        "## Workspace",
        "",
        f"- `workspace_name`: `{evaluation['workspace_name']}`",
        f"- `workspace_path`: `{evaluation['workspace_path']}`",
        f"- `workspace_kind`: `{evaluation['workspace_kind']}`",
        f"- `overall_result`: `{evaluation['overall_result']}`",
        "",
        "## Summary",
        "",
        evaluation["summary"],
        "",
        "## Dimensions",
        "",
    ]

    for dimension in evaluation["dimensions"]:
        lines.extend(
            [
                f"### `{dimension['dimension_id']}` — {dimension['label']}",
                "",
                f"- `status`: `{dimension['status']}`",
                f"- `why_it_matters`: {dimension['why_it_matters']}",
                "- `evidence`:",
            ]
        )
        for item in dimension["evidence"]:
            lines.append(f"  - {item}")
        lines.extend(
            [
                f"- `next_action`: {dimension['next_action']}",
                "",
            ]
        )

    lines.extend(
        [
            "## Review notes",
            "",
            "- strongest dimension:",
            "- weakest dimension:",
            "- blocking gap:",
            "- recommended next improvement:",
            "",
        ]
    )
    return "\n".join(lines)


def build_parser():
    parser = argparse.ArgumentParser(
        description="Evaluate a client workspace against the reusable Product Marketing workspace contract."
    )
    parser.add_argument("workspace", help="Path to the client workspace root")
    parser.add_argument(
        "--workspace-kind",
        choices=("template", "client"),
        help="Override workspace kind detection when a marker file is not present.",
    )
    parser.add_argument("--output", help="Optional markdown output path")
    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)

    workspace_root = Path(args.workspace)
    facts = collect_workspace_facts(workspace_root, workspace_kind=args.workspace_kind)
    evaluation = evaluate_workspace(facts)
    text = render_markdown(evaluation)

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(text, encoding="utf-8")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
