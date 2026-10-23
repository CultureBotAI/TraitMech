#!/usr/bin/env python3
"""Curate Stage 5 grouped review remediation (Cycle 1 #1981 and Cycle 2 #1995).

Resolves the 4 actionable open findings from the Cycle 1 Stage 4 corpus-wide
record and cohort review (`reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-04/revision-0001/evidence.yaml`,
tracked in GitHub issue #1981) and the 6 actionable open findings from the
Cycle 2 Stage 4 corpus-wide record and cohort review
(`reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-04/revision-0001/evidence.yaml`,
tracked in GitHub issue #1995):
- `F-DEF-SRC-CYANOPHYCIN-001` (`data/traits/morphology/cyanophycin_granule.yaml`, `traitmech:000673`):
  Adds verified verbatim record-level `evidence` for `definition_source: DOI:10.1128/AEM.01298-18`.
- `F-DEF-SRC-CADMIUM-002` (`data/traits/environment/cadmium_tolerant.yaml`, `traitmech:000013`):
  Adds verified verbatim record-level `evidence` for `definition_source: PMID:12829273` (Nies 2003).
- `F-DEF-SRC-COBALT-003` (`data/traits/environment/cobalt_tolerant.yaml`, `traitmech:000015`):
  Adds verified verbatim record-level `evidence` for `definition_source: PMID:12829273` (Nies 2003).
- `F-DEF-SRC-ZINC-004` (`data/traits/environment/zinc_tolerant.yaml`, `traitmech:000014`):
  Adds verified verbatim record-level `evidence` for `definition_source: PMID:12829273` (Nies 2003).
- `F-DEF-SRC-CARBON-FIXATION-010` (`data/traits/metabolism/carbon_fixation.yaml`, `traitmech:000019`):
  Promotes verified verbatim `snippet` for `definition_source: DOI:10.1128/AEM.02473-10` into `evidence[0]`.
- `F-DEF-SRC-WOOD-LJUNGDAHL-011` (`data/traits/metabolism/wood_ljungdahl_pathway.yaml`, `traitmech:000022`):
  Promotes verified verbatim `snippet` for `definition_source: DOI:10.1016/j.bbapap.2008.08.012` into `evidence[0]`.
- `F-DEF-SRC-PROPIONIC-FERM-012` (`data/traits/metabolism/propionic_acid_fermentation.yaml`, `traitmech:000029`):
  Promotes verified verbatim `snippet` for `definition_source: DOI:10.3390/molecules31020333` into `evidence[0]`.
- `F-DEF-SRC-MANGANESE-OX-013` (`data/traits/metabolism/manganese_oxidation.yaml`, `traitmech:000032`):
  Promotes verified verbatim `snippet` for `definition_source: DOI:10.1016/j.tim.2005.07.009` into `evidence[0]`.
- `F-DEF-SRC-CELLULOLYSIS-014` (`data/traits/metabolism/cellulolysis.yaml`, `traitmech:000111`):
  Promotes verified verbatim `snippet` for `definition_source: DOI:10.1128/MMBR.66.3.506-577.2002` into `evidence[0]`.
- `F-DEF-SRC-CHITINOLYSIS-015` (`data/traits/metabolism/chitinolysis.yaml`, `traitmech:000112`):
  Promotes verified verbatim `snippet` for `definition_source: DOI:10.3389/fmicb.2013.00149` into `evidence[0]`.

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
CYCLE2_TIMESTAMP = "2026-10-23T16:05:00Z"
ACTION = "ADD_RECORD_LEVEL_DEFINITION_SOURCE_EVIDENCE"

REMEDIATION_SPECS: dict[str, dict[str, Any]] = {
    "data/traits/morphology/cyanophycin_granule.yaml": {
        "identifier": "traitmech:000673",
        "finding_id": "F-DEF-SRC-CYANOPHYCIN-001",
        "timestamp": TIMESTAMP,
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
        "timestamp": TIMESTAMP,
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
        "timestamp": TIMESTAMP,
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
        "timestamp": TIMESTAMP,
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
    "data/traits/metabolism/carbon_fixation.yaml": {
        "identifier": "traitmech:000019",
        "finding_id": "F-DEF-SRC-CARBON-FIXATION-010",
        "timestamp": CYCLE2_TIMESTAMP,
        "definition_source": "DOI:10.1128/AEM.02473-10",
        "evidence_entry": {
            "reference": "DOI:10.1128/AEM.02473-10",
            "snippet": (
                "The reductive pentose phosphate cycle is the quantitatively most "
                "important mechanism of autotrophic CO2 fixation in nature."
            ),
            "notes": (
                'Berg (2011) "Ecological aspects of the distribution of different '
                'autotrophic CO2 fixation pathways" — authoritative review of the '
                "six known pathways."
            ),
        },
        "changes": (
            "Added verified verbatim snippet from DOI:10.1128/AEM.02473-10 (already "
            "present on causal_graphs[0].edges[11]) to record-level evidence[0] to "
            "match definition_source (Cycle 2 Stage 5 remediation of "
            "F-DEF-SRC-CARBON-FIXATION-010 in group "
            "G-C2S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #1995)."
        ),
    },
    "data/traits/metabolism/wood_ljungdahl_pathway.yaml": {
        "identifier": "traitmech:000022",
        "finding_id": "F-DEF-SRC-WOOD-LJUNGDAHL-011",
        "timestamp": CYCLE2_TIMESTAMP,
        "definition_source": "DOI:10.1016/j.bbapap.2008.08.012",
        "evidence_entry": {
            "reference": "DOI:10.1016/j.bbapap.2008.08.012",
            "snippet": (
                "use the reductive acetyl-CoA or Wood-Ljungdahl pathway as their "
                "main mechanism for energy conservation and for synthesis of "
                "acetyl-CoA and cell carbon from CO2"
            ),
            "notes": (
                "Ragsdale & Pierce (2008) review the enzymology and bioenergetics "
                "of the Wood–Ljungdahl pathway."
            ),
        },
        "changes": (
            "Added verified verbatim snippet from DOI:10.1016/j.bbapap.2008.08.012 "
            "(already present on causal_graphs[0].edges[0]) to record-level "
            "evidence[0] to match definition_source (Cycle 2 Stage 5 remediation of "
            "F-DEF-SRC-WOOD-LJUNGDAHL-011 in group "
            "G-C2S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #1995)."
        ),
    },
    "data/traits/metabolism/propionic_acid_fermentation.yaml": {
        "identifier": "traitmech:000029",
        "finding_id": "F-DEF-SRC-PROPIONIC-FERM-012",
        "timestamp": CYCLE2_TIMESTAMP,
        "definition_source": "DOI:10.3390/molecules31020333",
        "evidence_entry": {
            "reference": "DOI:10.3390/molecules31020333",
            "snippet": (
                "substrates such as glucose, glycerol or lactic acid are converted "
                "into propionic acid"
            ),
            "notes": (
                "Review of microbial propionic acid fermentation pathways "
                "(Wood-Werkman cycle and acrylate pathway), metabolic engineering, "
                "and bioprocess optimization."
            ),
        },
        "changes": (
            "Added verified verbatim snippet from DOI:10.3390/molecules31020333 "
            "(already present on causal_graphs[0].edges[1]) to record-level "
            "evidence[0] to match definition_source (Cycle 2 Stage 5 remediation of "
            "F-DEF-SRC-PROPIONIC-FERM-012 in group "
            "G-C2S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #1995)."
        ),
    },
    "data/traits/metabolism/manganese_oxidation.yaml": {
        "identifier": "traitmech:000032",
        "finding_id": "F-DEF-SRC-MANGANESE-OX-013",
        "timestamp": CYCLE2_TIMESTAMP,
        "definition_source": "DOI:10.1016/j.tim.2005.07.009",
        "evidence_entry": {
            "reference": "DOI:10.1016/j.tim.2005.07.009",
            "snippet": (
                "the reaction might involve a unique multicopper oxidase system "
                "capable of a two-electron oxidation of the substrate"
            ),
            "notes": (
                'Tebo et al., "Geomicrobiology of manganese(II) oxidation", supports '
                "bacterial Mn(II) oxidation to Mn oxides via a multicopper-oxidase "
                "mechanism."
            ),
        },
        "changes": (
            "Added verified verbatim snippet from DOI:10.1016/j.tim.2005.07.009 "
            "(already present on causal_graphs[0].edges[3]) to record-level "
            "evidence[0] to match definition_source (Cycle 2 Stage 5 remediation of "
            "F-DEF-SRC-MANGANESE-OX-013 in group "
            "G-C2S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #1995)."
        ),
    },
    "data/traits/metabolism/cellulolysis.yaml": {
        "identifier": "traitmech:000111",
        "finding_id": "F-DEF-SRC-CELLULOLYSIS-014",
        "timestamp": CYCLE2_TIMESTAMP,
        "definition_source": "DOI:10.1128/MMBR.66.3.506-577.2002",
        "evidence_entry": {
            "reference": "DOI:10.1128/MMBR.66.3.506-577.2002",
            "snippet": "complexed cellulase systems",
            "notes": (
                "Lynd et al. review microbial cellulose utilization, its enzymology, "
                "and cellulosome systems."
            ),
        },
        "changes": (
            "Added verified verbatim snippet from DOI:10.1128/MMBR.66.3.506-577.2002 "
            "(already present on causal_graphs[0].edges[15]) to record-level "
            "evidence[0] to match definition_source (Cycle 2 Stage 5 remediation of "
            "F-DEF-SRC-CELLULOLYSIS-014 in group "
            "G-C2S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #1995)."
        ),
    },
    "data/traits/metabolism/chitinolysis.yaml": {
        "identifier": "traitmech:000112",
        "finding_id": "F-DEF-SRC-CHITINOLYSIS-015",
        "timestamp": CYCLE2_TIMESTAMP,
        "definition_source": "DOI:10.3389/fmicb.2013.00149",
        "evidence_entry": {
            "reference": "DOI:10.3389/fmicb.2013.00149",
            "snippet": (
                "initial hydrolysis of the (1→4)-β-glycoside bond, as seen for "
                "chitinase-catalyzed chitin degradation"
            ),
            "notes": (
                "Beier & Bertilsson review bacterial chitin degradation mechanisms "
                "and ecophysiological strategies."
            ),
        },
        "changes": (
            "Added verified verbatim snippet from DOI:10.3389/fmicb.2013.00149 "
            "(already present on causal_graphs[0].edges[6]) to record-level "
            "evidence[0] to match definition_source (Cycle 2 Stage 5 remediation of "
            "F-DEF-SRC-CHITINOLYSIS-015 in group "
            "G-C2S4-RECORD-LEVEL-DEFINITION-SOURCE-SNIPPETS, issue #1995)."
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
    event_timestamp = str(spec.get("timestamp", TIMESTAMP))

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
        if ev.get("timestamp") == event_timestamp and ev.get("curator") == CURATOR
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
            timestamp=event_timestamp,
            upsert=True,
        )

    return changed


def process_all(
    repo_root: Path = REPO_ROOT,
    *,
    apply: bool = False,
) -> tuple[int, int]:
    """Process all 10 Stage 5 remediation targets. Returns (findings_resolved, files_updated)."""
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
