#!/usr/bin/env python3
"""Predicate domain/range audit for TraitMech causal graphs.

`validate-strict` checks that ``predicate_id`` is a string; it cannot check
that the CURIE's ontological *domain* and *range* are satisfiable by the node
types on either end of the edge. `predicate_id` is an unbound string in the
schema, so a false type entailment sails through every other gate. This audit
walks every ``data/traits/**/*.yaml`` causal graph and flags two such classes:

  MICROBE_DOMAIN_ON_NONORGANISM   an edge whose ``predicate_id`` is (transitively)
                                  ``rdfs:subPropertyOf METPO:2000001`` — whose
                                  ``rdfs:domain`` is METPO:1000525 (microbe).
                                  OWL domain is an inference rule, not a
                                  constraint: such an edge does not fail, it
                                  *entails that the subject node IS a microbe*.
                                  ``CausalNodeTypeEnum`` has no organism member,
                                  so NO causal-graph edge can satisfy the domain
                                  — every one of these is a false entailment.
                                  (#301, generalising #295)                [WARN]

  ENABLES_RANGE_ON_TRAIT          an edge with ``predicate_id: RO:0002327``
                                  (enables) whose object node is a ``TRAIT``.
                                  biolink gives enables range 'biological process
                                  or activity' (data/raw/biolink-model.yaml), and
                                  a TRAIT is a disposition, not a process, so the
                                  edge entails ``trait ⊑ BiologicalProcessOrActivity``
                                  — the same shape as the RO:0002411 defect in
                                  #235.                                     (#302) [WARN]

Neither is machine-fixable without a biological decision per predicate family
(#301) or an ontology decision on the enables range (#302, #303), so a blocking
check would be un-landable today: 366 + 164 edges already carry these shapes.
This is therefore a **ratchet**, identical in mechanics to audit-graphs and
audit-snippets: ``--write-baseline`` freezes the known set, pre-existing
violations stay non-blocking, and any *new* violation fails the build. Burn the
baseline down family by family, then tighten to ``--fail-on any``.

The microbe-domain predicate set is derived at run time by walking the
``subPropertyOf`` closure to METPO:2000001 in ``data/raw/metpo.owl`` — NOT from
a hand-maintained list, so a new METPO subproperty is covered the moment it is
vendored, the same reasoning audit-qc-paths uses for its read-set.

Writes ``reports/predicate_domain_audit.tsv``. Exit code is governed by
``--fail-on``:

  new    (default) any finding NOT in the baseline fails. The ratchet.
  error  only new ERROR-severity findings fail (there are none today; both
         defects are WARN until their families are resolved).
  any    every finding fails and the baseline is ignored. Use post-burndown.

Usage:
    python scripts/audit_predicate_domains.py
    python scripts/audit_predicate_domains.py --write-baseline   # freeze today
    python scripts/audit_predicate_domains.py --fail-on any      # once burned down
"""
from __future__ import annotations

import argparse
import csv
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
TRAITS_DIR = REPO_ROOT / "data" / "traits"
METPO_OWL = REPO_ROOT / "data" / "raw" / "metpo.owl"
DEFAULT_OUT = REPO_ROOT / "reports" / "predicate_domain_audit.tsv"
DEFAULT_BASELINE = REPO_ROOT / "conf" / "predicate_domain_audit_baseline.tsv"

# The microbe-domain root. Every object property transitively subPropertyOf this
# inherits its rdfs:domain of METPO:1000525 (microbe). See #295/#301.
MICROBE_DOMAIN_ROOT = "METPO:2000001"
# enables: biolink range is 'biological process or activity'; a TRAIT object is
# a disposition, not a process. See #302.
ENABLES = "RO:0002327"

ERROR = "ERROR"
WARN = "WARN"

# Both WARN: pre-existing at scale, so they must be baselineable (write-baseline
# refuses to freeze an ERROR). Promote to ERROR once a family is burned down, or
# just run that family with --fail-on any.
SEVERITY = {
    "MICROBE_DOMAIN_ON_NONORGANISM": WARN,
    "ENABLES_RANGE_ON_TRAIT": WARN,
}

FIELDNAMES = ["file", "graph_id", "defect", "severity", "detail"]

_METPO_IRI = "https://w3id.org/metpo/"
_RDF = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
_RDFS = "{http://www.w3.org/2000/01/rdf-schema#}"
_OWL = "{http://www.w3.org/2002/07/owl#}"


def _curie(iri: str | None) -> str | None:
    if iri and iri.startswith(_METPO_IRI):
        return "METPO:" + iri.rsplit("/", 1)[1]
    return iri


def microbe_domain_predicates(owl_path: Path, root: str = MICROBE_DOMAIN_ROOT) -> set[str]:
    """CURIEs of every object property transitively ``subPropertyOf`` ``root``.

    Includes ``root`` itself. Built from the OWL rather than hard-coded so a new
    METPO subproperty is covered automatically; falls back to just ``{root}`` if
    the OWL is unreadable, which fails safe (fewer findings, never a crash).
    """
    parent: dict[str, set[str]] = {}
    try:
        tree = ET.parse(owl_path)
    except (ET.ParseError, OSError):
        return {root}
    for op in tree.getroot().iter(f"{_OWL}ObjectProperty"):
        child = _curie(op.get(f"{_RDF}about"))
        if not child:
            continue
        for sp in op.findall(f"{_RDFS}subPropertyOf"):
            p = _curie(sp.get(f"{_RDF}resource"))
            if p:
                parent.setdefault(child, set()).add(p)

    def reaches(c: str, seen: set[str]) -> bool:
        for p in parent.get(c, ()):
            if p == root:
                return True
            if p not in seen:
                seen.add(p)
                if reaches(p, seen):
                    return True
        return False

    return {c for c in parent if reaches(c, set())} | {root}


def audit(traits_dir: Path, owl_path: Path = METPO_OWL) -> list[dict[str, str]]:
    microbe_domain = microbe_domain_predicates(owl_path)
    findings: list[dict[str, str]] = []
    for path in sorted(traits_dir.rglob("*.yaml")):
        try:
            doc = yaml.safe_load(path.read_text())
        except yaml.YAMLError:
            continue
        if not isinstance(doc, dict):
            continue
        try:
            rel = str(path.relative_to(REPO_ROOT))
        except ValueError:
            rel = str(path)
        for graph in (doc.get("causal_graphs") or []):
            gid = graph.get("graph_id", "")
            node_type = {n.get("node_id"): n.get("node_type")
                         for n in (graph.get("nodes") or [])}
            for e in (graph.get("edges") or []):
                pid = e.get("predicate_id")
                subj, obj = e.get("subject"), e.get("object")
                # Lead the detail with a space-free per-edge discriminator so
                # `_key` keys each edge independently (predicate_id is a CURIE,
                # node_ids are slugs — none contain spaces), the same contract
                # audit_causal_graphs._key relies on.
                edge_key = f"{subj}--{pid}-->{obj}"

                if pid in microbe_domain:
                    findings.append({
                        "file": rel, "graph_id": gid,
                        "defect": "MICROBE_DOMAIN_ON_NONORGANISM",
                        "severity": SEVERITY["MICROBE_DOMAIN_ON_NONORGANISM"],
                        "detail": (f"{edge_key} subject_type={node_type.get(subj)} "
                                   f"predicate={e.get('predicate')!r} — subject entails "
                                   f"⊑ microbe (METPO:1000525) via {MICROBE_DOMAIN_ROOT}"),
                    })

                if pid == ENABLES and node_type.get(obj) == "TRAIT":
                    findings.append({
                        "file": rel, "graph_id": gid,
                        "defect": "ENABLES_RANGE_ON_TRAIT",
                        "severity": SEVERITY["ENABLES_RANGE_ON_TRAIT"],
                        "detail": (f"{edge_key} object_type=TRAIT — enables range is "
                                   "'biological process or activity'; a disposition "
                                   "cannot satisfy it"),
                    })
    return findings


def _key(row: dict[str, str]) -> tuple[str, str, str, str]:
    """Baseline identity: (file, graph, defect, per-edge discriminator).

    The discriminator is the leading whitespace-delimited fragment of ``detail``
    — ``subject--predicate_id-->object`` — so each violating edge keys
    independently and editing an edge's human-readable tail (its ``predicate``
    label or a node's type) does not silently un-suppress it. Same contract as
    audit_causal_graphs._key.
    """
    detail = row.get("detail", "")
    disc = detail.split(" ", 1)[0] if detail else ""
    return (row["file"], row["graph_id"], row["defect"], disc)


def partition(
    findings: list[dict[str, str]],
    baseline: set[tuple[str, str, str, str]],
    fail_on: str,
) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    """Split ``findings`` into (not-in-baseline, blocking) for a ``--fail-on``.

    Kept separate from ``main`` so the exit-code contract is unit-testable — a
    regression here silently disarms the ratchet.
    """
    new = [r for r in findings if _key(r) not in baseline]
    if fail_on == "any":
        blocking = list(findings)
    elif fail_on == "error":
        blocking = [r for r in new if r["severity"] == ERROR]
    else:  # "new" — the ratchet.
        blocking = list(new)
    return new, blocking


def load_baseline(path: Path) -> set[tuple[str, str, str, str]]:
    if not path.exists():
        return set()
    # encoding pinned: the detail column carries a non-ASCII '⊑', so the default
    # (locale) encoding would crash reading the baseline on a non-UTF-8 locale.
    with path.open(newline="", encoding="utf-8") as f:
        return {_key(r) for r in csv.DictReader(f, delimiter="\t")}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--traits-dir", type=Path, default=TRAITS_DIR)
    ap.add_argument("--owl", type=Path, default=METPO_OWL)
    ap.add_argument("--baseline", type=Path, default=DEFAULT_BASELINE,
                    help="TSV of known findings to suppress from the exit code.")
    ap.add_argument("--no-baseline", action="store_true",
                    help="Ignore the baseline file; report everything.")
    ap.add_argument("--write-baseline", action="store_true",
                    help="Freeze current WARN findings into --baseline and exit 0. "
                         "Refuses if any ERROR-severity finding exists.")
    ap.add_argument("--fail-on", choices=["new", "error", "any"], default="new",
                    help="new (default): any finding not in the baseline fails — the "
                         "ratchet. error: only new ERROR-severity findings fail. "
                         "any: every finding fails, baseline ignored (post-burndown).")
    args = ap.parse_args()

    findings = audit(args.traits_dir, args.owl)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    # encoding pinned: details carry a non-ASCII '⊑' — see load_baseline.
    with args.out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDNAMES, delimiter="\t",
                           lineterminator="\n")
        w.writeheader()
        w.writerows(findings)

    if args.write_baseline:
        errors = [r for r in findings if r["severity"] == ERROR]
        if errors:
            print(f"Refusing to write baseline: {len(errors)} ERROR-severity "
                  f"finding(s) present. Fix these first — the baseline is for "
                  f"the WARN backlog only.", file=sys.stderr)
            for r in errors[:20]:
                print(f"  {r['defect']}  {r['file']} [{r['graph_id']}]  "
                      f"{r['detail']}", file=sys.stderr)
            return 1
        warns = [r for r in findings if r["severity"] != ERROR]
        args.baseline.parent.mkdir(parents=True, exist_ok=True)
        with args.baseline.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=FIELDNAMES, delimiter="\t",
                               lineterminator="\n")
            w.writeheader()
            w.writerows(warns)
        print(f"Wrote baseline: {args.baseline} ({len(warns)} finding(s))",
              file=sys.stderr)
        return 0

    baseline = set() if args.no_baseline else load_baseline(args.baseline)
    new, blocking = partition(findings, baseline, args.fail_on)

    by_defect: dict[str, int] = {}
    for r in findings:
        by_defect[r["defect"]] = by_defect.get(r["defect"], 0) + 1
    print("=== predicate domain/range audit ===", file=sys.stderr)
    print(f"  findings: {len(findings)}"
          f"  (baselined: {len(findings) - len(new)}, new: {len(new)},"
          f" blocking: {len(blocking)})", file=sys.stderr)
    for d, n in sorted(by_defect.items()):
        print(f"    {d:<32} {n:>5}  [{SEVERITY.get(d, WARN)}]", file=sys.stderr)
    print(f"  TSV: {args.out}", file=sys.stderr)
    for r in (blocking or new)[:20]:
        print(f"  {r['severity']}  {r['defect']}  {r['file']} [{r['graph_id']}]"
              f"  {r['detail']}", file=sys.stderr)
    return 1 if blocking else 0


if __name__ == "__main__":
    sys.exit(main())
