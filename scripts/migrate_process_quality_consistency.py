#!/usr/bin/env python3
"""#356 tranche 5: settle process/quality families and merge clear aliases.

The remaining BIOLOGICAL_PROCESS/QUALITY splits are mostly measurable
properties that were typed as processes, plus two genuine processes typed as
qualities. Reading the descriptions and edges also exposes four duplicate ids
for the same senses. Retyping those aliases in place would leave one concept
under two ids, so this migration folds them into the existing canonical ids.

Default is a dry run. Pass ``--apply`` to validate and write every in-scope
record. A fixed, upserted curation event is recorded for the whole scope so the
script and shipped rationale cannot diverge on a re-run.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import (  # noqa: E402
    ValidationFailedError,
    emit_trait_yaml,
    validate_trait,
    write_validated_trait,
)

TRAITS = REPO_ROOT / "data" / "traits"
SCHEMA = REPO_ROOT / "src" / "traitmech" / "schema" / "traitmech.yaml"
TARGET_CLASS = "TraitRecord"
TIMESTAMP = "2026-08-21T08:00:00Z"
ACTION = "NORMALISE_NODE_TYPE"


@dataclass(frozen=True)
class Decision:
    canonical_id: str
    node_type: str
    rationale: str
    canonical_label: str | None = None


DECISIONS: dict[str, Decision] = {
    "immune_evasion": Decision(
        "immune_evasion",
        "BIOLOGICAL_PROCESS",
        "Immune evasion is the avoidance or subversion of host defenses. The edges "
        "treat it as an enabled action that in turn enables colonization; capsule.yaml's "
        "'reduced recognition and clearance' is the outcome of that same process, not "
        "a separate measurable axis.",
    ),
    "inside_positive_membrane_potential": Decision(
        "reversed_membrane_potential",
        "STATE",
        "An inside-positive membrane potential is the reversed membrane-potential "
        "state already modelled under reversed_membrane_potential. The schema separates "
        "a gradient or steady value (STATE) from its establishment (process); every "
        "description here names the electrical state opposing proton influx.",
        "inside-positive (reversed) membrane potential",
    ),
    "reversed_membrane_potential": Decision(
        "reversed_membrane_potential",
        "STATE",
        "A reversed membrane potential is an inside-positive electrical state, not "
        "the process that establishes it. The schema names this gradient/steady-value "
        "distinction explicitly.",
        "inside-positive (reversed) membrane potential",
    ),
    "membrane_proton_permeability": Decision(
        "proton_permeability",
        "QUALITY",
        "Membrane proton permeability is the measurable leakiness of the membrane. "
        "The corpus already models the identical label and description under the "
        "shorter proton_permeability id as QUALITY, so the duplicate id is merged.",
        "membrane proton permeability",
    ),
    "proton_permeability": Decision(
        "proton_permeability",
        "QUALITY",
        "Proton permeability is a measurable membrane property, which is the schema's "
        "QUALITY sense rather than a biological process.",
        "membrane proton permeability",
    ),
    "maximal_growth_rate": Decision(
        "maximal_growth_rate",
        "QUALITY",
        "A maximal growth rate is a measured upper bound or peak specific rate. Its "
        "edges associate, enable, or manifest that value; none describe the process of "
        "cell growth itself. An edge cannot enable a QUALITY under RO:0002327's "
        "biological-process range, so edges that causally support the rate use "
        "promotes (RO:0002213) instead.",
    ),
    "phosphate_buffering": Decision(
        "phosphate_buffering",
        "BIOLOGICAL_PROCESS",
        "Both occurrences describe cytoplasmic phosphate pools buffering protons and "
        "stabilizing pH: the buffering action, not the size of a buffer reservoir. The "
        "distinct cytoplasmic_buffering_capacity id remains CAPACITY for that quantity "
        "sense.",
        "cytoplasmic phosphate buffering",
    ),
    "membrane_rigidification": Decision(
        "membrane_rigidity",
        "QUALITY",
        "These nodes describe reduced bilayer fluidity, increased order/thickness, and "
        "the resulting physical trigger. That is the same membrane-rigidity QUALITY "
        "already modelled under membrane_rigidity, so the process-shaped alias is merged.",
    ),
    "membrane_rigidity": Decision(
        "membrane_rigidity",
        "QUALITY",
        "Membrane rigidity is a physical attribute of the bilayer and therefore a "
        "QUALITY under the schema's membrane-fluidity example.",
    ),
    "positive_dna_supercoiling": Decision(
        "dna_positive_supercoiling",
        "BIOLOGICAL_PROCESS",
        "This is the GO:0160097 process in which reverse gyrase introduces positive "
        "supercoils. It is distinct from the general dna_supercoiling topological-state "
        "QUALITY and is merged into the existing dna_positive_supercoiling id.",
        "DNA positive supercoiling",
    ),
    "dna_positive_supercoiling": Decision(
        "dna_positive_supercoiling",
        "BIOLOGICAL_PROCESS",
        "GO:0160097 denotes the process of introducing positive supercoils into DNA. "
        "The general DNA-topology state remains separately modelled as dna_supercoiling.",
        "DNA positive supercoiling",
    ),
    "stress_resistance": Decision(
        "stress_resistance",
        "QUALITY",
        "Stress resistance here is enhanced tolerance or resistance of a cell or mature "
        "endospore, a measurable protective attribute. The nodes do not describe the "
        "general stress-response process.",
    ),
}


def normalize_document(doc: dict[str, Any]) -> tuple[list[str], list[str]]:
    """Normalize one document; return (in-scope canonical ids, actual changes)."""
    in_scope: list[str] = []
    changes: list[str] = []
    for graph in doc.get("causal_graphs") or []:
        nodes = graph.get("nodes") or []
        ids = {node.get("node_id") for node in nodes}
        for node in nodes:
            old_id = node.get("node_id")
            decision = DECISIONS.get(old_id)
            if decision is None:
                continue
            in_scope.append(decision.canonical_id)
            if decision.canonical_id != old_id:
                if decision.canonical_id in ids:
                    raise ValueError(
                        f"cannot rename {old_id} to {decision.canonical_id}: id already in graph"
                    )
                node["node_id"] = decision.canonical_id
                ids.discard(old_id)
                ids.add(decision.canonical_id)
                for edge in graph.get("edges") or []:
                    if edge.get("subject") == old_id:
                        edge["subject"] = decision.canonical_id
                    if edge.get("object") == old_id:
                        edge["object"] = decision.canonical_id
                changes.append(f"{old_id} -> {decision.canonical_id}")
            if node.get("node_type") != decision.node_type:
                previous = node.get("node_type")
                node["node_type"] = decision.node_type
                changes.append(
                    f"{decision.canonical_id}: {previous} -> {decision.node_type}"
                )
            if decision.canonical_label and node.get("label") != decision.canonical_label:
                previous = node.get("label")
                node["label"] = decision.canonical_label
                changes.append(
                    f"{decision.canonical_id}: label {previous!r} -> {decision.canonical_label!r}"
                )
        for edge in graph.get("edges") or []:
            if edge.get("object") != "maximal_growth_rate" or edge.get("predicate") != "enables":
                continue
            edge["predicate"] = "promotes"
            edge["predicate_id"] = "RO:0002213"
            description = edge.get("description")
            if description:
                edge["description"] = description.replace(" enables ", " promotes ").replace(
                    " enable ", " promote "
                )
            changes.append("maximal_growth_rate in-edge: enables -> promotes (RO:0002213)")
    return list(dict.fromkeys(in_scope)), changes


def apply(*, write: bool = False, traits_dir: Path = TRAITS) -> int:
    files_in_scope = 0
    files_changed = 0
    changes_total = 0
    for path in sorted(traits_dir.rglob("*.yaml")):
        source_text = path.read_text()
        try:
            doc = yaml.safe_load(source_text)
        except yaml.YAMLError as exc:
            print(f"SKIP parse error: {path}: {exc}", file=sys.stderr)
            continue
        if not isinstance(doc, dict):
            continue
        try:
            in_scope, changes = normalize_document(doc)
        except ValueError as exc:
            print(f"ERROR {path}: {exc}", file=sys.stderr)
            return 1
        if not in_scope:
            continue
        files_in_scope += 1

        settled = ", ".join(
            f"{node_id} is {DECISIONS[node_id].node_type}" for node_id in in_scope
        )
        rationale = " ".join(DECISIONS[node_id].rationale for node_id in in_scope)
        record_curation_event(
            doc,
            curator="codex",
            action=ACTION,
            changes=(
                "Tranche 5 of issue 356 settles the process/quality families and "
                f"merges ids that meant the same sense: {settled}. {rationale}"
            ),
            llm_assisted=True,
            timestamp=TIMESTAMP,
            upsert=True,
        )

        if emit_trait_yaml(doc) == source_text:
            print(f"current {path.relative_to(traits_dir)}")
            continue

        if write:
            try:
                write_validated_trait(
                    doc, path, target_class=TARGET_CLASS, schema_path=SCHEMA
                )
            except ValidationFailedError as exc:
                detail = exc.errors[0].message if exc.errors else str(exc)
                print(f"ERROR validation: {path}: {detail}", file=sys.stderr)
                return 1
        else:
            errors = validate_trait(doc, target_class=TARGET_CLASS, schema_path=SCHEMA)
            if errors:
                print(f"ERROR validation: {path}: {errors[0].message}", file=sys.stderr)
                return 1

        files_changed += 1
        changes_total += len(changes)
        mode = "write" if write else "plan"
        print(f"{mode:5s} {path.relative_to(traits_dir)}: {', '.join(changes) or 'history refresh'}")

    print(
        f"{files_in_scope} in-scope file(s), {files_changed} file(s) changed, "
        f"{changes_total} field change(s)"
        f"{' written' if write else ' (dry run)'}",
        file=sys.stderr,
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="validate and write changes")
    parser.add_argument("--traits-dir", type=Path, default=TRAITS)
    args = parser.parse_args()
    return apply(write=args.apply, traits_dir=args.traits_dir)


if __name__ == "__main__":
    raise SystemExit(main())
