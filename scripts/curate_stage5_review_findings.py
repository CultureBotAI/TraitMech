#!/usr/bin/env python3
"""Curate Stage 5 grouped review remediation (G-STAGE4-RECORD-LEVEL-DEFINITION-SOURCE).

Resolves the 4 actionable open findings from the Stage 4 corpus-wide record and
cohort review (`reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-04/revision-0001/evidence.yaml`,
tracked in GitHub issue #1981):
- `F-DEF-SRC-CYANOPHYCIN-001` (`data/traits/morphology/cyanophycin_granule.yaml`, `traitmech:000673`):
  Adds verified verbatim record-level `evidence` for `definition_source: DOI:10.1128/AEM.01298-18`.
- `F-DEF-SRC-CADMIUM-002` (`data/traits/environment/cadmium_tolerant.yaml`, `traitmech:000013`):
  Adds verified verbatim record-level `evidence` for `definition_source: PMID:12829273` (Nies 2003).
- `F-DEF-SRC-COBALT-003` (`data/traits/environment/cobalt_tolerant.yaml`, `traitmech:000015`):
  Adds verified verbatim record-level `evidence` for `definition_source: PMID:12829273` (Nies 2003).
- `F-DEF-SRC-ZINC-004` (`data/traits/environment/zinc_tolerant.yaml`, `traitmech:000014`):
  Adds verified verbatim record-level `evidence` for `definition_source: PMID:12829273` (Nies 2003).

Default is dry-run; pass `--apply` to write changes via `write_validated_trait`
and `record_curation_event`.

Usage:
    python scripts/curate_stage5_review_findings.py
    python scripts/curate_stage5_review_findings.py --apply
"""

from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import (  # noqa: E402
    ValidationFailedError,
    validate_trait,
    write_validated_trait,
)

DO_NOT_WORK_PATH = REPO_ROOT / "DO_NOT_WORK.md"
CURATOR = "claude"
TIMESTAMP = "2026-10-22T05:20:00Z"
ACTION = "ADD_RECORD_LEVEL_DEFINITION_SOURCE_EVIDENCE"

REMEDIATION_SPECS: dict[str, dict[str, Any]] = {
    "data/traits/morphology/cyanophycin_granule.yaml": {
        "identifier": "traitmech:000673",
        "finding_id": "F-DEF-SRC-CYANOPHYCIN-001",
        "definition_source": "DOI:10.1128/AEM.01298-18",
        "evidence_entry": {
            "reference": "DOI:10.1128/AEM.01298-18",
            "snippet": (
                "Cyanophycin accumulates in the form of opaque and light-scattering "
                "granules in the cell"
            ),
            "notes": (
                "Watzer and Forchhammer (2018), Introduction and Abstract, directly "
                "read in publisher HTML: cyanophycin accumulates as opaque, "
                "light-scattering intracellular storage granules serving as a "
                'temporary nitrogen reserve (abstract: "cyanophycin can be used as a '
                'temporary nitrogen storage"). Supports the record definition and '
                "definition_source."
            ),
        },
        "changes": (
            "Added DOI:10.1128/AEM.01298-18 with verified verbatim snippet to "
            "record-level evidence to match definition_source (Stage 5 remediation "
            "of F-DEF-SRC-CYANOPHYCIN-001 in group G-STAGE4-RECORD-LEVEL-DEFINITION-SOURCE, "
            "issue #1981)."
        ),
    },
    "data/traits/environment/cadmium_tolerant.yaml": {
        "identifier": "traitmech:000013",
        "finding_id": "F-DEF-SRC-CADMIUM-002",
        "definition_source": "PMID:12829273",
        "evidence_entry": {
            "reference": "PMID:12829273",
            "snippet": (
                "CBA efflux pumps driven by proteins of the resistance-nodulation-cell "
                "division superfamily, P-type ATPases, cation diffusion facilitator "
                "and chromate proteins"
            ),
            "notes": (
                "Nies (2003, FEMS Microbiol Rev 27:313-339) reviews prokaryotic "
                "heavy-metal resistance mediated by RND-family CBA efflux pumps "
                "(including CzcCBA), P-type ATPases, and cation diffusion facilitators, "
                "supporting the record definition and definition_source for cadmium tolerance."
            ),
        },
        "changes": (
            "Added PMID:12829273 (Nies 2003) with verified verbatim snippet to "
            "record-level evidence to match definition_source (Stage 5 remediation "
            "of F-DEF-SRC-CADMIUM-002 in group G-STAGE4-RECORD-LEVEL-DEFINITION-SOURCE, "
            "issue #1981)."
        ),
    },
    "data/traits/environment/cobalt_tolerant.yaml": {
        "identifier": "traitmech:000015",
        "finding_id": "F-DEF-SRC-COBALT-003",
        "definition_source": "PMID:12829273",
        "evidence_entry": {
            "reference": "PMID:12829273",
            "snippet": (
                "CBA efflux pumps driven by proteins of the resistance-nodulation-cell "
                "division superfamily, P-type ATPases, cation diffusion facilitator "
                "and chromate proteins"
            ),
            "notes": (
                "Nies (2003, FEMS Microbiol Rev 27:313-339) reviews prokaryotic "
                "heavy-metal resistance mediated by RND-family CBA efflux pumps "
                "(including CzcCBA and CnrCBA) and cation diffusion facilitators, "
                "supporting the record definition and definition_source for cobalt tolerance."
            ),
        },
        "changes": (
            "Added PMID:12829273 (Nies 2003) with verified verbatim snippet to "
            "record-level evidence to match definition_source (Stage 5 remediation "
            "of F-DEF-SRC-COBALT-003 in group G-STAGE4-RECORD-LEVEL-DEFINITION-SOURCE, "
            "issue #1981)."
        ),
    },
    "data/traits/environment/zinc_tolerant.yaml": {
        "identifier": "traitmech:000014",
        "finding_id": "F-DEF-SRC-ZINC-004",
        "definition_source": "PMID:12829273",
        "evidence_entry": {
            "reference": "PMID:12829273",
            "snippet": (
                "CBA efflux pumps driven by proteins of the resistance-nodulation-cell "
                "division superfamily, P-type ATPases, cation diffusion facilitator "
                "and chromate proteins"
            ),
            "notes": (
                "Nies (2003, FEMS Microbiol Rev 27:313-339) reviews prokaryotic "
                "heavy-metal resistance mediated by RND-family CBA efflux pumps "
                "(including CzcCBA), P-type ATPases (including ZntA), and cation "
                "diffusion facilitators, supporting the record definition and "
                "definition_source for zinc tolerance."
            ),
        },
        "changes": (
            "Added PMID:12829273 (Nies 2003) with verified verbatim snippet to "
            "record-level evidence to match definition_source (Stage 5 remediation "
            "of F-DEF-SRC-ZINC-004 in group G-STAGE4-RECORD-LEVEL-DEFINITION-SOURCE, "
            "issue #1981)."
        ),
    },
}


def load_do_not_work(path: Path = DO_NOT_WORK_PATH) -> set[str]:
    """Return relative paths listed in DO_NOT_WORK.md."""
    excluded: set[str] = set()
    if not path.exists():
        return excluded
    for line in path.read_text(encoding="utf-8").splitlines():
        if "data/traits/" in line:
            for token in line.replace("`", " ").split():
                if token.startswith("data/traits/") and token.endswith(".yaml"):
                    excluded.add(token)
    return excluded


def apply_remediation_to_doc(doc: dict[str, Any], spec: dict[str, Any]) -> bool:
    """Ensure the specified definition_source evidence entry is present on doc."""
    if doc.get("identifier") != spec["identifier"]:
        raise ValueError(f"Identifier mismatch: {doc.get('identifier')} != {spec['identifier']}")
    if doc.get("definition_source") != spec["definition_source"]:
        raise ValueError(
            f"definition_source mismatch on {spec['identifier']}: "
            f"{doc.get('definition_source')} != {spec['definition_source']}"
        )

    evidence_list = list(doc.get("evidence") or [])
    target_ref = spec["evidence_entry"]["reference"]
    desired_entry = copy.deepcopy(spec["evidence_entry"])

    changed = False
    existing_idx = next(
        (i for i, item in enumerate(evidence_list) if item.get("reference") == target_ref),
        None,
    )
    if existing_idx is None:
        evidence_list.append(desired_entry)
        doc["evidence"] = evidence_list
        changed = True
    elif evidence_list[existing_idx] != desired_entry:
        evidence_list[existing_idx] = desired_entry
        doc["evidence"] = evidence_list
        changed = True

    existing_events = [
        ev
        for ev in (doc.get("curation_history") or [])
        if ev.get("timestamp") == TIMESTAMP and ev.get("curator") == CURATOR
    ]
    if not existing_events or existing_events[-1].get("changes") != spec["changes"]:
        changed = True

    if changed:
        record_curation_event(
            doc,
            curator=CURATOR,
            action=ACTION,
            changes=spec["changes"],
            llm_assisted=True,
            timestamp=TIMESTAMP,
            upsert=True,
        )

    return changed


def process_all(
    repo_root: Path = REPO_ROOT,
    *,
    apply: bool = False,
) -> tuple[int, int]:
    """Process all 4 Stage 5 remediation targets. Returns (findings_resolved, files_updated)."""
    excluded = load_do_not_work(repo_root / "DO_NOT_WORK.md")
    findings_resolved = 0
    files_updated = 0

    for rel_path, spec in sorted(REMEDIATION_SPECS.items()):
        if rel_path in excluded:
            raise ValueError(f"Refusing to touch DO_NOT_WORK.md excluded file: {rel_path}")
        path = repo_root / rel_path
        if not path.is_file():
            raise FileNotFoundError(f"Missing target file: {path}")
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        changed = apply_remediation_to_doc(doc, spec)
        findings_resolved += 1
        if changed:
            errors = validate_trait(doc)
            if errors:
                raise ValidationFailedError(path, errors)
            if apply:
                write_validated_trait(doc, path)
            files_updated += 1

    return findings_resolved, files_updated


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Write changes to data/traits/ via write_validated_trait (default: dry-run).",
    )
    args = parser.parse_args(argv)
    resolved, updated = process_all(apply=args.apply)
    mode = "APPLIED" if args.apply else "DRY-RUN"
    print(f"[{mode}] Stage 4 open findings resolved: {resolved}; files updated: {updated}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
