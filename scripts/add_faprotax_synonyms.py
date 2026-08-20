#!/usr/bin/env python3
"""Make three high-frequency FAPROTAX labels resolve to traits we already have (#453).

microbedecoder's unmapped-label residual carries FAPROTAX metabolic-strategy and
ecology strings. Most of them need new terms, which is a METPO proposal
round-trip. These three do not — TraitMech already has the trait, under a
different name, so the fix is a synonym rather than a record.

    oxygenic_photoautotrophy  5,221  -> oxygenic photosynthesis  traitmech:000034
    ureolysis                   600  -> urease activity          traitmech:000077
    human_pathogens_all         291  -> human pathogen           METPO:1004004

6,112 occurrences, no new identifiers, nothing to mint.

## Why the raw underscored string

The synonym is written exactly as the ingest emits it, underscores and all,
because that is the string a consumer has to resolve. A tidied
`oxygenic photoautotrophy` would read better and match nothing. Same reasoning
as MediaIngredientMech's "correct the label, keep the raw string" rule.

## Why RELATED and not EXACT

All three are FAPROTAX *group* names, which classify an organism by an inferred
functional capability, rather than alternative names for the phenotype itself.
`human_pathogens_all` is the clearest case: it is the union of FAPROTAX's
per-disease pathogen groups, so it denotes a category boundary rather than a
synonym of "human pathogen". RELATED is also the corpus default (400 of 499).

## What this does NOT claim

Adding a synonym makes the label resolvable in the exported vocabulary and in
`build_embedding_index.py`, which reads synonyms. It does not ground a causal
graph node — that is keyed on (label, node_type) in `node_grounding.tsv` and is
a separate mechanism, as #458 established the hard way.

    python scripts/add_faprotax_synonyms.py            # dry-run
    python scripts/add_faprotax_synonyms.py --apply
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
from traitmech.validation.write_validated import (  # noqa: E402
    validate_trait, write_validated_trait)

CURATOR = "add_faprotax_synonyms"
STAMP = "2026-08-19T00:00:00+00:00"
SOURCE = "FAPROTAX (via microbedecoder unmapped labels)"

# (path, synonym text, occurrences, why this trait is the right target)
ADDITIONS = [
    ("data/traits/metabolism/oxygenic_photosynthesis.yaml",
     "oxygenic_photoautotrophy", 5221,
     "FAPROTAX's oxygenic_photoautotrophy is autotrophic growth driven by "
     "oxygenic photosynthesis — the record's own definition is 'uses light "
     "energy to fix CO2, oxidizing water as the electron donor and releasing "
     "molecular oxygen', which is that phenotype."),
    ("data/traits/physiology/urease_activity.yaml",
     "ureolysis", 600,
     "FAPROTAX's ureolysis is urea hydrolysis, which this record already "
     "defines as its mechanism: 'produces urease, which hydrolyzes urea to "
     "ammonia and carbon dioxide'."),
    ("data/traits/ecology/human_pathogen.yaml",
     "human_pathogens_all", 291,
     "FAPROTAX's human_pathogens_all is the union of its per-disease human "
     "pathogen groups, so it denotes the same set as 'a pathogen that infects "
     "organisms of the species Homo sapiens'."),
]

# `synonyms` sits after `parent_traits` and before `created_by`/`evidence`
# (docs/CURATION_PLAYBOOK.md, "File-level structure"). Rebuild the mapping in
# that order rather than appending, so a record that lacks the key does not get
# it tacked on at the end.
FIELD_ORDER = [
    "identifier", "label", "definition", "definition_source", "trait_category",
    "term_kind", "mapping_status", "parent_traits", "synonyms", "created_by",
    "domain", "range_", "evidence", "canonical_examples", "causal_graphs",
    "curation_history",
]


def _ordered(doc: dict) -> dict:
    out = {k: doc[k] for k in FIELD_ORDER if k in doc}
    out.update({k: v for k, v in doc.items() if k not in out})
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args(argv)

    changed, skipped, invalid = [], [], []
    for rel, text, occ, why in ADDITIONS:
        path = ROOT / rel
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        syns = doc.get("synonyms") or []
        if any(str(s.get("synonym_text", "")).lower() == text.lower() for s in syns):
            skipped.append(text)
            continue
        syns.append({"synonym_text": text, "synonym_type": "RELATED_SYNONYM",
                     "source": SOURCE})
        doc["synonyms"] = syns
        doc.setdefault("curation_history", []).append({
            "timestamp": STAMP, "curator": CURATOR, "action": "ADDED_SYNONYM",
            "changes": (f"Added {text!r} ({occ} occurrences in microbedecoder's "
                        f"unmapped labels) as a RELATED_SYNONYM (#453). {why} "
                        f"Written with the source's underscores because that is "
                        f"the string a consumer must resolve."),
            "llm_assisted": False})
        doc = _ordered(doc)
        errs = validate_trait(doc)
        if errs:
            invalid.append((text, [str(e.message)[:90] for e in errs[:2]]))
            continue
        if args.apply:
            write_validated_trait(doc, path)
        changed.append((text, doc["label"], occ))

    print(f"{'APPLIED' if args.apply else 'DRY RUN (re-run with --apply)'}\n")
    for text, label, occ in changed:
        print(f"  + {text!r} -> {label!r}  ({occ} occurrences)")
    if skipped:
        print(f"  already present: {skipped}")
    if invalid:
        print(f"  SCHEMA ERRORS (not written): {invalid}")
    print(f"\n  {sum(o for _, _, o in changed)} occurrences newly resolvable")
    return 1 if invalid else 0


if __name__ == "__main__":
    sys.exit(main())
