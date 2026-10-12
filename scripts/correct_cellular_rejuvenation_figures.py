"""Correct the yeast figure attribution without rewriting the original curation event."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import tempfile
from pathlib import Path

import yaml

import add_cellular_rejuvenation_trait as initial
from traitmech.curate.curation_event import record_curation_event
from traitmech.validation.write_validated import write_validated_trait

ROOT = Path(__file__).resolve().parent.parent
TARGET = ROOT / "data/traits/physiology/cellular_rejuvenation.yaml"
SIDECAR = ROOT / "research/traits/physiology/cellular_rejuvenation-source-verification.json"
TIMESTAMP = "2026-10-12T12:40:17Z"
ISSUE = "https://github.com/CultureBotAI/TraitMech/issues/1893"
EXPECTED_SOURCE_HASH = "2c3c278d76753306bcb72b8aca7ea13ed59824610143aa966af34ab7880bf28f"
OLD = "Main text and Figures 1 and 4 support gamete replicative-potential reset."
NEW = (
    "Main text and Figure 1 support gamete replicative-potential reset. "
    "Figure 4 concerns the separate vegetative lifespan-extension experiment."
)


def digest(document: dict) -> str:
    return hashlib.sha256(json.dumps(document, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def build_record() -> dict:
    record = initial.build_record()
    notes = record["evidence"][2]["notes"]
    assert notes.count(OLD) == 1
    record["evidence"][2]["notes"] = notes.replace(OLD, NEW)
    record_curation_event(
        record, curator="codex", action="CORRECTED_FIGURE_ATTRIBUTION",
        changes=(
            "Corrected issue #1893: Figure 1 supports gamete replicative-potential "
            "reset; Figure 4 tests vegetative lifespan extension. Preserved "
            "definition, DOI, snippet, status, checksum limitation and original "
            "event. The source sidecar retains its historical assessment with "
            "an explicit superseding correction. Timestamp is the observed UTC "
            "correction decision."
        ),
        llm_assisted=True, timestamp=TIMESTAMP,
    )
    return record


def corrected_sidecar(document: dict) -> dict:
    if not isinstance(document, dict):
        raise SystemExit("Source sidecar differs from reviewed preimage")
    base = copy.deepcopy(document)
    prior = base.pop("assessment_corrections", None)
    if digest(base) != EXPECTED_SOURCE_HASH:
        raise SystemExit("Source sidecar differs from reviewed preimage")
    correction = {
        "timestamp": TIMESTAMP,
        "issue": ISSUE,
        "source_doi": initial.GAMETE_RESET.removeprefix("DOI:"),
        "supersedes_field": "sources[2].source_read_scope",
        "corrected_source_read_scope": build_record()["evidence"][2]["notes"],
        "reason": "Figure 1 tests gamete reset; Figure 4 tests vegetative extension. Original snapshot interpretation is retained, not silently rewritten.",
    }
    if prior is not None and prior != [correction]:
        raise SystemExit("Existing sidecar correction differs from reviewed result")
    base["assessment_corrections"] = [correction]
    return base


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    current = yaml.safe_load(TARGET.read_text())
    record = build_record()
    if current != initial.build_record() and current != record:
        raise SystemExit("Existing trait differs from reviewed preimage or result")
    sidecar = corrected_sidecar(json.loads(SIDECAR.read_text()))
    with tempfile.TemporaryDirectory() as tmp:
        write_validated_trait(record, Path(tmp) / TARGET.name)
    if args.apply:
        write_validated_trait(record, TARGET)
        SIDECAR.write_text(json.dumps(sidecar, indent=2) + "\n")
    print("Applied" if args.apply else "Validated dry run; pass --apply to write")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
