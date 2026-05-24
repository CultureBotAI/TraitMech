#!/usr/bin/env python3
"""Match TraitMech GENE_OR_PROTEIN labels to UniProt CURIEs via the
kg-microbe UniProt transform.

Streams the kg-microbe `merged-kg_uniprot_nodes.tsv` (≈2.2 GB), for
each UniProtKB row checks whether any TraitMech residual
GENE_OR_PROTEIN label appears as a token in the protein name, and
emits a candidate-match TSV that lists representative UniProt CURIEs
per label.

Two outputs:
  - `reports/uniprot_match_candidates.tsv` — full audit trail, all
    candidate matches per label (subject of human review).
  - `mappings/node_grounding.tsv` (appended in place) — one row per
    label, picking a single representative.

Representative selection per label (see `pick_representative`):
  Tier 1 (best). The UniProt name (cleaned of trailing parens)
    equals the TraitMech label exactly. Pick the alphabetically-
    first UniProtKB CURIE for determinism.
  Tier 2. The cleaned name ends with " <label>" as the final
    whitespace-separated token (e.g. "Polarized growth protein Scy"
    for label "scy"). Pick the SHORTEST such name (fewer modifier
    words like *chaperone*, *maturation protein*, *assembly factor*),
    alphabetic CURIE as tiebreaker.
  Otherwise. Return None — too ambiguous to ground cleanly.

A separate hand-curated `SKIP_LABELS` blocklist suppresses abstract-
category labels (e.g. "gene product", "virulence factors") that
shouldn't be grounded to any single UniProt entry even when matches
are found.

CURIE prefix normalization:
  The kg-microbe source data uses `UniprotKB:` (lowercase p);
  the TraitMech LinkML schema declares `UniProtKB` (uppercase P).
  This script reads using the source-data spelling and emits the
  schema-canonical spelling in all downstream artifacts (mappings
  TSV, candidates TSV, YAMLs after running ground-nodes).

Default is **dry-run** (writes candidates TSV only). Pass `--apply`
to also append mappings rows.

Usage:
    python scripts/match_uniprot_to_proteins.py [--apply]
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
RESIDUAL_TSV = REPO_ROOT / "reports/node_grounding_residual.tsv"
MAPPING_TSV = REPO_ROOT / "mappings/node_grounding.tsv"
CANDIDATES_TSV = REPO_ROOT / "reports/uniprot_match_candidates.tsv"
KG_UNIPROT_NODES = Path(
    "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/"
    "kg-microbe/merged-kg_uniprot_nodes.tsv"
)

# Per-label cap to avoid overly-generic matches dominating the index.
# Set higher than the typical exact-match volume so the exact-match
# tier-1 representative selector has a real chance of finding a clean
# entry (alphabetically-first matches often skew toward "chaperone" /
# "assembly factor" hits that share the keyword but aren't THE protein).
MAX_MATCHES_PER_LABEL = 500

# Labels that are abstract categories rather than concrete protein names —
# grounding any of them to a single UniProt entry would be misleading.
# Curated by hand from the residual; "gene product", in particular, hits
# every UniProt entry whose name happens to end in "<gene_id> gene product".
SKIP_LABELS = {
    "gene product",
    "virulence factors",
    "chaperone proteins",
    "thermostable proteins",
    "salinity-adaptation genes",
    "cold-shock proteins",
    "proton export pumps and antiporters",
    "membrane transporters",
    "gliding motility machinery",
    "rod complex",
}


def load_target_labels() -> list[str]:
    """Read GENE_OR_PROTEIN labels with no grounding (lowercase)."""
    out: list[str] = []
    with RESIDUAL_TSV.open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            if row["node_type"] == "GENE_OR_PROTEIN":
                out.append(row["node_label"].strip().lower())
    return out


def build_regex(labels: list[str]) -> re.Pattern:
    """Build a single regex that matches any label as a word-bounded token."""
    parts = sorted({re.escape(lbl) for lbl in labels}, key=len, reverse=True)
    # Word boundaries can't reliably surround "+", "/", etc. Use (?<![A-Za-z0-9])
    # and (?![A-Za-z0-9]) to bracket alphanumeric runs only — that way
    # tokens like "na+/h+ antiporter" still match cleanly.
    return re.compile(
        r"(?<![A-Za-z0-9])(?:" + "|".join(parts) + r")(?![A-Za-z0-9])",
        re.IGNORECASE,
    )


def stream_uniprot_matches(
    labels: list[str],
) -> dict[str, list[tuple[str, str]]]:
    """Walk the kg-microbe UniProt nodes file, return label → [(curie, name)]."""
    if not KG_UNIPROT_NODES.exists():
        raise FileNotFoundError(KG_UNIPROT_NODES)

    regex = build_regex(labels)
    label_set = set(labels)
    matches: dict[str, list[tuple[str, str]]] = defaultdict(list)

    seen_rows = 0
    seen_uniprot = 0
    with KG_UNIPROT_NODES.open() as fh:
        next(fh)  # header
        for line in fh:
            seen_rows += 1
            if seen_rows % 2_000_000 == 0:
                print(f"  {seen_rows:>10,} rows scanned, "
                      f"{seen_uniprot:>9,} UniProtKB, "
                      f"{sum(len(v) for v in matches.values()):>7,} matches",
                      file=sys.stderr)
            cols = line.rstrip("\n").split("\t")
            # kg-microbe source uses the `UniprotKB:` prefix (lowercase p);
            # the TraitMech schema prefix-map declares `UniProtKB` (uppercase P).
            # Filter against the source-data spelling here, and normalize the
            # emitted CURIE just below so downstream artifacts (mappings,
            # YAMLs, reports) match the schema.
            if len(cols) < 3 or not cols[0].startswith("UniprotKB:"):
                continue
            seen_uniprot += 1
            curie = "UniProtKB:" + cols[0].split(":", 1)[1]
            name = cols[2]
            for m in regex.finditer(name):
                key = m.group(0).lower()
                if key not in label_set:
                    continue
                if len(matches[key]) < MAX_MATCHES_PER_LABEL:
                    matches[key].append((curie, name))

    return matches


def pick_representative(label: str, candidates: list[tuple[str, str]]) -> tuple[str, str] | None:
    """Pick a single representative UniProt entry for a label.

    Tier 1 (best): the cleaned name equals the label exactly.
    Tier 2: the cleaned name ends with " <label>" as the final
        whitespace-separated token — prefer the SHORTEST such name
        (fewer modifier words like "chaperone", "maturation protein",
        "assembly factor"), with alphabetic CURIE as tiebreaker.
    Otherwise: skip (return None) — too ambiguous to ground cleanly.
    """
    if not candidates:
        return None
    label_l = label.lower()

    def clean(name: str) -> str:
        return re.sub(r"\s*\([^)]*\)\s*$", "", name).strip()

    # Tier 1 — exact match.
    exact = [c for c in candidates if clean(c[1]).lower() == label_l]
    if exact:
        return sorted(exact, key=lambda x: x[0])[0]

    # Tier 2 — name ends with " <label>" (last whitespace-token).
    suffix_hits = [
        c for c in candidates
        if clean(c[1]).lower().endswith(" " + label_l)
    ]
    if suffix_hits:
        suffix_hits.sort(key=lambda x: (len(clean(x[1])), x[0]))
        return suffix_hits[0]

    # Otherwise — too ambiguous.
    return None


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true",
                    help="append picked mappings to mappings/node_grounding.tsv")
    args = ap.parse_args()

    labels = load_target_labels()
    print(f"Target GENE_OR_PROTEIN labels: {len(labels)}", file=sys.stderr)

    print(f"Streaming {KG_UNIPROT_NODES} ...", file=sys.stderr)
    matches = stream_uniprot_matches(labels)
    print(f"  labels with at least one match: {len(matches)} / {len(labels)}",
          file=sys.stderr)

    CANDIDATES_TSV.parent.mkdir(parents=True, exist_ok=True)
    with CANDIDATES_TSV.open("w") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["label", "match_count", "representative_curie",
                    "representative_name", "example_other_curies"])
        picked: list[tuple[str, str, str]] = []
        skipped_abstract: list[str] = []
        for lbl in labels:
            cands = matches.get(lbl, [])
            if lbl in SKIP_LABELS:
                w.writerow([lbl, len(cands), "", "(SKIPPED — abstract category)", ""])
                skipped_abstract.append(lbl)
                continue
            rep = pick_representative(lbl, cands)
            if rep is None:
                w.writerow([lbl, len(cands), "", "", ""])
                continue
            curie, name = rep
            others = "|".join(c for c, _ in cands[:5] if c != curie)
            w.writerow([lbl, len(cands), curie, name, others])
            picked.append((lbl, curie, name))

    print(f"  candidates TSV: {CANDIDATES_TSV.relative_to(REPO_ROOT)}",
          file=sys.stderr)
    print(f"  representatives picked: {len(picked)}", file=sys.stderr)
    if skipped_abstract:
        print(f"  abstract-category labels skipped: {len(skipped_abstract)}",
              file=sys.stderr)

    if args.apply and picked:
        with MAPPING_TSV.open("a") as fh:
            for label, curie, name in picked:
                short_name = name.replace("\t", " ").strip()
                fh.write(
                    f"{label}\tGENE_OR_PROTEIN\t{curie}\t{short_name}\t"
                    f"UniProt\thigh\trepresentative UniProt entry "
                    f"selected via kg-microbe merged-kg_uniprot_nodes.tsv "
                    f"(name-ends-with-label + alphabetic-first CURIE)\n"
                )
        print(f"  appended {len(picked)} rows to "
              f"{MAPPING_TSV.relative_to(REPO_ROOT)}", file=sys.stderr)
    elif not args.apply and picked:
        print("", file=sys.stderr)
        print("  Re-run with --apply to append the picked mappings.",
              file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
