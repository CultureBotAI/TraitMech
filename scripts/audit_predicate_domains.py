#!/usr/bin/env python3
"""Predicate domain/range audit for TraitMech causal graphs.

`validate-strict` checks that ``predicate_id`` is a string; it cannot check
that the CURIE's ontological *domain* and *range* are satisfiable by the node
types on either end of the edge. `predicate_id` is an unbound string in the
schema, so a false type entailment sails through every other gate. This audit
walks every ``data/traits/**/*.yaml`` causal graph and flags three such classes:

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

  PREDICATE_GATE_VIOLATION        a GROUNDED edge whose subject or object node
                                  type is not admitted by its predicate's
                                  ``subject_types``/``object_types`` in
                                  mappings/predicate_grounding.tsv.
                                  ``ground_causal_predicates`` consults those
                                  columns only when it FIRST grounds an edge --
                                  it returns early on any edge that already has
                                  a ``predicate_id`` -- so the gate was a
                                  write-time check with no read-time
                                  counterpart, and every retyping migration
                                  since #351 could move an edge out of range
                                  silently. Two did: #382 shipped one to main
                                  undetected, #392's was caught by hand in
                                  review. ERROR, because the table is a rule
                                  this repo sets itself, so a violation is the
                                  corpus disagreeing with us rather than a
                                  judgement call. (#393)                  [ERROR]

  ENABLES_RANGE_VIOLATION         an edge with ``predicate_id: RO:0002327``
                                  (enables) whose object node is NOT a
                                  'biological process or activity'. biolink
                                  declares that range
                                  (data/raw/biolink-model.yaml), and only
                                  BIOLOGICAL_PROCESS, PATHWAY and
                                  MOLECULAR_FUNCTION satisfy it, so any other
                                  object entails a false type. Began as a
                                  TRAIT-only test (#302, 164 edges, since
                                  migrated); widened to the full range in #315,
                                  which surfaced 33 more.                    [WARN]

The three classes are at different stages, and the configuration reflects that.

MICROBE_DOMAIN_ON_NONORGANISM is **burned down**: 530 findings shipped as a
ratchet in #314 because nothing was fixable without decisions that had not been
made; those landed (v8 for #302/#303 in #320/#323, v9 for #301 in #326/#328/#329,
final edge in #327) and the count is **0**. It is therefore ERROR severity, which
makes ``--write-baseline`` REFUSE to freeze one — a regression cannot be
baselined away, even by accident, while re-freezing the other class.

ENABLES_RANGE_VIOLATION IS NOW BURNED DOWN TOO. Widening the enables test from
TRAIT-only to the full biolink range (#315) surfaced 33 pre-existing edges
needing per-edge biological judgement (#334); #341 and #355 repaired the last of
them, so the class is at 0 and the baseline is header-only. It stays WARN and
baselineable rather than being promoted, because unlike the two ERROR classes its
authority is an UPSTREAM range (biolink's) that can widen under us — but the
condition for promotion is now met, and doing so is a deliberate decision rather
than a pending chore.

The rule this encodes: **a baseline is for a class that has never been clean,
never for one that has.** Do not add rows to excuse a regression; for the domain
class the severity now stops you.

The microbe-domain predicate set is derived at run time by walking the
``subPropertyOf`` closure to METPO:2000001 in ``data/raw/metpo.owl`` — NOT from
a hand-maintained list, so a new METPO subproperty is covered the moment it is
vendored, the same reasoning audit-qc-paths uses for its read-set.

Writes ``reports/predicate_domain_audit.tsv``. Exit code is governed by
``--fail-on``:

  any    (argparse DEFAULT) every finding fails and the baseline is ignored. A
         bare invocation is exit 0 today because all three classes are at 0;
         it would exit 1 on any finding, baselined or not, so a stray baseline
         file can never weaken an ad-hoc run (#327). The justfile recipe passes
         ``--fail-on new`` explicitly.
  new    any finding NOT in the baseline fails — the ratchet, and what `just
         audit-predicate-domains` uses today. For a class that has never been
         clean; not for excusing a regression in one that has.
  error  only new ERROR-severity findings fail — i.e. only the burned-down
         domain class.

Usage:
    just audit-predicate-domains                                 # --fail-on new
    python scripts/audit_predicate_domains.py --fail-on new      # same, directly
    python scripts/audit_predicate_domains.py                    # strict; exits 1
                                                                 # while #334 stands
    python scripts/audit_predicate_domains.py --write-baseline   # refuses on ERROR
"""
from __future__ import annotations

import argparse
import csv
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))

from ground_causal_predicates import (  # noqa: E402
    SCHEMA_PATH as _GCP_SCHEMA_PATH,
    _node_type_values,
    _types,
)

REPO_ROOT = Path(__file__).resolve().parent.parent
TRAITS_DIR = REPO_ROOT / "data" / "traits"
METPO_OWL = REPO_ROOT / "data" / "raw" / "metpo.owl"
DEFAULT_OUT = REPO_ROOT / "reports" / "predicate_domain_audit.tsv"
DEFAULT_BASELINE = REPO_ROOT / "conf" / "predicate_domain_audit_baseline.tsv"
PREDICATE_MAPPING = REPO_ROOT / "mappings" / "predicate_grounding.tsv"
# Read from the schema, not hardcoded, for the reason _node_type_values gives:
# a schema change must not leave this file silently disagreeing with it.
VALID_NODE_TYPES = _node_type_values(_GCP_SCHEMA_PATH)

# The microbe-domain root. Every object property transitively subPropertyOf this
# inherits its rdfs:domain of METPO:1000525 (microbe). See #295/#301.
MICROBE_DOMAIN_ROOT = "METPO:2000001"
# enables: biolink gives it range 'biological process or activity'
# (data/raw/biolink-model.yaml). ANY object that is not an activity violates it.
# This began as a TRAIT-only check (#302) because a trait is a disposition and
# that was the 164-edge case; generalising it to the whole range (#315) surfaced
# 33 further edges pointing at proteins, states, qualities, capacities,
# chemicals and locations, which the narrower test could never see.
ENABLES = "RO:0002327"
# The CausalNodeTypeEnum members that ARE a 'biological process or activity'.
# Everything else fails the range.
ACTIVITY_NODE_TYPES = frozenset({"BIOLOGICAL_PROCESS", "PATHWAY", "MOLECULAR_FUNCTION"})

ERROR = "ERROR"
WARN = "WARN"

# MICROBE_DOMAIN_ON_NONORGANISM is ERROR because it is BURNED DOWN (#301): there
# are zero of them and there must stay zero. `--write-baseline` refuses to freeze
# an ERROR, so a regression cannot be silently baselined away by someone running
# it to re-freeze the other class. That makes "a baseline is only for a class
# that has never been clean" a structural guarantee rather than a convention
# nobody enforces (#315 review).
#
# ENABLES_RANGE_VIOLATION stays WARN even though #341/#355 burned its 33 edges
# (#334) down to 0. Not an oversight: its authority is biolink's range, which is
# UPSTREAM and can widen under us, so a regression there may be someone else's
# change rather than ours. The two ERROR classes are both locally authored — a
# METPO domain we mint, and a gate table we write.
# PREDICATE_GATE_VIOLATION is ERROR for the same reason as the first: it is
# clean today (#392 cleared the last one, by adding STATE to METPO:2007800's
# object_types) and must stay clean. It is also the only
# class here whose authority is LOCAL — mappings/predicate_grounding.tsv is a
# table this repo writes, so a violation means the corpus disagrees with a rule
# we set ourselves, which is never a judgement call needing a baseline.
SEVERITY = {
    "MICROBE_DOMAIN_ON_NONORGANISM": ERROR,
    "ENABLES_RANGE_VIOLATION": WARN,
    "PREDICATE_GATE_VIOLATION": ERROR,
}

FIELDNAMES = ["file", "graph_id", "defect", "severity", "detail"]

_METPO_IRI = "https://w3id.org/metpo/"
_OBO_PURL = "http://purl.obolibrary.org/obo/"
_RDF = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
_RDFS = "{http://www.w3.org/2000/01/rdf-schema#}"
_OWL = "{http://www.w3.org/2002/07/owl#}"


def _curie(iri: str | None) -> str | None:
    """Normalise an ontology IRI to the CURIE form the corpus writes.

    Both METPO's w3id IRIs and OBO PURLs are handled. The OBO case is not
    reachable today — every ObjectProperty in the vendored metpo.owl is a w3id
    METPO IRI — but it is the exact scenario the subPropertyOf walk advertises
    support for: if METPO ever asserts an RO or BFO property under
    METPO:2000001, the closure would hold
    ``http://purl.obolibrary.org/obo/RO_0002327`` and never match the corpus's
    ``RO:0002327``, silently under-reporting a class that is now ERROR severity
    and must stay at zero (#316).

    Anything else is returned unchanged rather than guessed at, so an
    unrecognised namespace fails to match loudly rather than matching wrongly.
    """
    if not iri:
        return iri
    if iri.startswith(_METPO_IRI):
        return "METPO:" + iri.rsplit("/", 1)[1]
    if iri.startswith(_OBO_PURL):
        # OBO PURLs are <prefix>_<local>, e.g. RO_0002327 -> RO:0002327.
        local = iri[len(_OBO_PURL):]
        prefix, sep, rest = local.partition("_")
        if sep and prefix.isalnum():
            return f"{prefix}:{rest}"
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


def predicate_gates(mapping_path: Path = PREDICATE_MAPPING
                    ) -> dict[str, tuple[frozenset | None, frozenset | None]]:
    """``{target CURIE: (subject_types, object_types)}`` from the grounding table.

    ``ground_causal_predicates`` consults these columns when it FIRST grounds an
    edge, and never again: it returns early on any edge that already carries a
    ``predicate_id`` (#393). So the gate is a write-time check with no read-time
    counterpart, and every retyping migration since #351 has been able to move a
    grounded edge out of range silently.

    Two did. #382 retyped ``proton_motive_force`` to STATE, putting
    ``terminal_oxidases -produces-> proton_motive_force`` outside METPO:2007800;
    it shipped to main undetected. #392 retyped ``phenazine_biosynthesis`` to
    PATHWAY, putting an ``encodes`` edge outside METPO:2007813; that one was
    caught in review, by hand. This function is what makes the hand-check
    unnecessary.
    """
    gates: dict[str, tuple[frozenset | None, frozenset | None]] = {}
    with mapping_path.open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            curie = (row.get("target_curie") or "").strip()
            if not curie:
                continue
            # Parsed by the WRITER's own function, not a second implementation.
            # Parity kept by duplication drifts, and the two had already diverged
            # in review: `NONE` (METPO:2000008/2000009, "no node type can satisfy
            # this") worked here only by accident, because "NONE" happens not to
            # be a CausalNodeTypeEnum member. `_types` returns None for `*`/empty
            # and an EMPTY SET for NONE, which are opposite meanings that a
            # string compare cannot tell apart.
            gate = (_types(row.get("subject_types"), VALID_NODE_TYPES),
                    _types(row.get("object_types"), VALID_NODE_TYPES))
            # 110 rows collapse to 76 CURIEs — the table is keyed by LABEL and
            # 14 CURIEs carry several rows. Identical gates are fine; disagreeing
            # ones are not, and the last row would silently win. This class is
            # ERROR and unbaselineable, so the wrong gate would hard-block CI on
            # a legitimate edge. load_mapping raises on the mirror-image conflict
            # (one label, two CURIEs); this is the same guard (#398 review).
            if curie in gates and gates[curie] != gate:
                raise ValueError(
                    f"conflicting gates for {curie} in {mapping_path}: "
                    f"{gates[curie]} vs {gate}"
                )
            gates[curie] = gate
    return gates


def _gate_admits(allowed: frozenset | None, actual: str | None) -> bool:
    """Does a parsed gate cell admit ``actual``?

    ``None`` means the cell was ``*`` or empty — any type. An EMPTY SET means the
    cell was ``NONE``: nothing satisfies it, so every edge is refused. Those are
    opposite meanings, which is why the cell is parsed by the writer's ``_types``
    rather than string-compared here — the first hand-run of this check compared
    ``*`` as a literal type name and reported 3385 violations against a corpus
    that had one.

    An untyped node (``actual is None``) is admitted, and the writer REFUSES it.
    The asymmetry is deliberate: ``node_type`` is required by the schema and
    DANGLING_EDGE is at 0, so it is unreachable — and if it ever became
    reachable, this audit should not be the thing that reports it.
    """
    if allowed is None:
        return True
    if actual is None:
        return True
    return actual in allowed


def audit(traits_dir: Path, owl_path: Path = METPO_OWL,
          mapping_path: Path = PREDICATE_MAPPING) -> list[dict[str, str]]:
    microbe_domain = microbe_domain_predicates(owl_path)
    gates = predicate_gates(mapping_path)
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

                # The corpus against a rule this repo set itself, re-tested at
                # read time. Both ends, because a retype can move either.
                if pid in gates:
                    subj_ok, obj_ok = gates[pid]
                    for end, allowed, actual in (("subject", subj_ok, node_type.get(subj)),
                                                 ("object", obj_ok, node_type.get(obj))):
                        if not _gate_admits(allowed, actual):
                            findings.append({
                                "file": rel, "graph_id": gid,
                                "defect": "PREDICATE_GATE_VIOLATION",
                                "severity": SEVERITY["PREDICATE_GATE_VIOLATION"],
                                "detail": (f"{edge_key} {end}_type={actual} — "
                                           f"mappings/predicate_grounding.tsv gates "
                                           f"{pid} to {end}_types="
                                           f"{'|'.join(sorted(allowed)) if allowed else '*'}"),
                            })

                ot = node_type.get(obj)
                if pid == ENABLES and ot is not None and ot not in ACTIVITY_NODE_TYPES:
                    findings.append({
                        "file": rel, "graph_id": gid,
                        "defect": "ENABLES_RANGE_VIOLATION",
                        "severity": SEVERITY["ENABLES_RANGE_VIOLATION"],
                        "detail": (f"{edge_key} object_type={ot} — enables range is "
                                   "'biological process or activity', which only "
                                   "BIOLOGICAL_PROCESS, PATHWAY and MOLECULAR_FUNCTION "
                                   "satisfy"),
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
    ap.add_argument("--mapping", type=Path, default=PREDICATE_MAPPING,
                    help="predicate gate table (default: mappings/predicate_grounding.tsv)")
    ap.add_argument("--baseline", type=Path, default=DEFAULT_BASELINE,
                    help="TSV of known findings to suppress from the exit code.")
    ap.add_argument("--no-baseline", action="store_true",
                    help="Ignore the baseline file; report everything.")
    ap.add_argument("--write-baseline", action="store_true",
                    help="Freeze current WARN findings into --baseline and exit 0. "
                         "Refuses if any ERROR-severity finding exists.")
    ap.add_argument("--fail-on", choices=["new", "error", "any"], default="any",
                    help="any (default, post-burndown): every finding fails and the "
                         "baseline is ignored. new: only findings not in the baseline "
                         "fail — the ratchet, for reintroducing this check over a NEW "
                         "class of violation. error: only new ERROR-severity findings "
                         "fail.")
    args = ap.parse_args()

    findings = audit(args.traits_dir, args.owl, args.mapping)
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
