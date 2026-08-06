"""Unit tests for scripts/audit_predicate_domains.py.

Locks in that audit() flags:
- MICROBE_DOMAIN_ON_NONORGANISM: an edge whose predicate_id is (transitively)
  subPropertyOf METPO:2000001, whose rdfs:domain is microbe, so no causal node
  type can satisfy it (#301).
- ENABLES_RANGE_VIOLATION: an enables/RO:0002327 edge whose object is not an activity,
  whose range is 'biological process or activity' (#302).
- and is silent on predicates outside the microbe-domain closure and on enables
  pointed at a process.

Also locks in the subPropertyOf closure (direct + transitive), the fail-safe
fallback when the OWL is unreadable, and the baseline ratchet's exit-code
contract — a frozen finding is suppressed, a new one is not.
"""

from __future__ import annotations

import subprocess
import sys
import textwrap
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from audit_predicate_domains import (  # noqa: E402
    ERROR,
    SEVERITY,
    _key,
    audit,
    microbe_domain_predicates,
    partition,
)

# A minimal METPO OWL: 2000001 is the microbe-domain root; 2000202 is a direct
# child, 9999999 a transitive grandchild, and 3000000 an unrelated property.
OWL = """\
<?xml version="1.0"?>
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
         xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
         xmlns:owl="http://www.w3.org/2002/07/owl#">
  <owl:ObjectProperty rdf:about="https://w3id.org/metpo/2000001"/>
  <owl:ObjectProperty rdf:about="https://w3id.org/metpo/2000202">
    <rdfs:subPropertyOf rdf:resource="https://w3id.org/metpo/2000001"/>
  </owl:ObjectProperty>
  <owl:ObjectProperty rdf:about="https://w3id.org/metpo/9999999">
    <rdfs:subPropertyOf rdf:resource="https://w3id.org/metpo/2000202"/>
  </owl:ObjectProperty>
  <owl:ObjectProperty rdf:about="https://w3id.org/metpo/3000000"/>
</rdf:RDF>
"""


def _write_owl(tmp_path: Path) -> Path:
    p = tmp_path / "metpo.owl"
    p.write_text(OWL)
    return p


def _write(tmp_path: Path, name: str, body: str) -> Path:
    d = tmp_path / "traits"
    d.mkdir(exist_ok=True)
    (d / name).write_text(textwrap.dedent(body))
    return d


# --- subPropertyOf closure ---------------------------------------------------


def test_closure_includes_direct_and_transitive_children(tmp_path):
    owl = _write_owl(tmp_path)
    got = microbe_domain_predicates(owl)
    assert got == {"METPO:2000001", "METPO:2000202", "METPO:9999999"}


def test_closure_excludes_unrelated_property(tmp_path):
    owl = _write_owl(tmp_path)
    assert "METPO:3000000" not in microbe_domain_predicates(owl)


def test_unreadable_owl_falls_back_to_root(tmp_path):
    """A missing OWL must fail safe: only the root, never a crash."""
    assert microbe_domain_predicates(tmp_path / "does_not_exist.owl") == {"METPO:2000001"}


# --- MICROBE_DOMAIN_ON_NONORGANISM (#301) ------------------------------------

MICROBE_DOMAIN_EDGE = """\
identifier: traitmech:000001
label: t
causal_graphs:
- graph_id: g
  nodes:
  - {node_id: proc, label: P, node_type: BIOLOGICAL_PROCESS}
  - {node_id: chem, label: C, node_type: CHEMICAL}
  edges:
  - {subject: proc, predicate: produces, object: chem, predicate_id: METPO:2000202}
"""

TRANSITIVE_DOMAIN_EDGE = """\
identifier: traitmech:000002
label: t
causal_graphs:
- graph_id: g
  nodes:
  - {node_id: proc, label: P, node_type: BIOLOGICAL_PROCESS}
  - {node_id: chem, label: C, node_type: CHEMICAL}
  edges:
  - {subject: proc, predicate: x, object: chem, predicate_id: METPO:9999999}
"""

NON_MICROBE_EDGE = """\
identifier: traitmech:000003
label: t
causal_graphs:
- graph_id: g
  nodes:
  - {node_id: proc, label: P, node_type: BIOLOGICAL_PROCESS}
  - {node_id: chem, label: C, node_type: CHEMICAL}
  edges:
  - {subject: proc, predicate: y, object: chem, predicate_id: METPO:3000000}
"""


def test_microbe_domain_predicate_flagged(tmp_path):
    owl = _write_owl(tmp_path)
    d = _write(tmp_path, "md.yaml", MICROBE_DOMAIN_EDGE)
    findings = audit(d, owl)
    assert [f["defect"] for f in findings] == ["MICROBE_DOMAIN_ON_NONORGANISM"]
    assert "subject_type=BIOLOGICAL_PROCESS" in findings[0]["detail"]
    assert findings[0]["detail"].startswith("proc--METPO:2000202-->chem")


def test_transitive_microbe_domain_predicate_flagged(tmp_path):
    """A grandchild predicate inherits the domain and must flag too."""
    owl = _write_owl(tmp_path)
    d = _write(tmp_path, "tr.yaml", TRANSITIVE_DOMAIN_EDGE)
    assert [f["defect"] for f in audit(d, owl)] == ["MICROBE_DOMAIN_ON_NONORGANISM"]


def test_non_microbe_predicate_not_flagged(tmp_path):
    owl = _write_owl(tmp_path)
    d = _write(tmp_path, "nm.yaml", NON_MICROBE_EDGE)
    assert audit(d, owl) == []


# --- ENABLES_RANGE_VIOLATION (#302, widened in #315) --------------------------

ENABLES_ON_TRAIT = """\
identifier: traitmech:000004
label: t
causal_graphs:
- graph_id: g
  nodes:
  - {node_id: chem, label: C, node_type: CHEMICAL}
  - {node_id: tr, label: T, node_type: TRAIT}
  edges:
  - {subject: chem, predicate: enables, object: tr, predicate_id: RO:0002327}
"""

ENABLES_ON_PROCESS = """\
identifier: traitmech:000005
label: t
causal_graphs:
- graph_id: g
  nodes:
  - {node_id: chem, label: C, node_type: CHEMICAL}
  - {node_id: proc, label: P, node_type: BIOLOGICAL_PROCESS}
  edges:
  - {subject: chem, predicate: enables, object: proc, predicate_id: RO:0002327}
"""


def test_enables_on_trait_flagged(tmp_path):
    owl = _write_owl(tmp_path)
    d = _write(tmp_path, "et.yaml", ENABLES_ON_TRAIT)
    findings = audit(d, owl)
    assert [f["defect"] for f in findings] == ["ENABLES_RANGE_VIOLATION"]
    assert "object_type=TRAIT" in findings[0]["detail"]


ENABLES_ON_QUALITY = """\
identifier: traitmech:000050
label: t
causal_graphs:
- graph_id: g
  nodes:
  - {node_id: proc, label: P, node_type: BIOLOGICAL_PROCESS}
  - {node_id: q, label: Q, node_type: QUALITY}
  edges:
  - {subject: proc, predicate: enables, object: q, predicate_id: RO:0002327}
"""


def test_enables_on_non_activity_object_flagged(tmp_path):
    """#315: the range is the whole 'biological process or activity', not just TRAIT.

    A QUALITY object violates it exactly as a TRAIT does. The original TRAIT-only
    test could not see the 33 corpus edges pointing at proteins, states,
    qualities, capacities, chemicals and locations.
    """
    owl = _write_owl(tmp_path)
    d = _write(tmp_path, "eq.yaml", ENABLES_ON_QUALITY)
    findings = audit(d, owl)
    assert [f["defect"] for f in findings] == ["ENABLES_RANGE_VIOLATION"]
    assert "object_type=QUALITY" in findings[0]["detail"]


def test_enables_on_pathway_and_molecular_function_not_flagged(tmp_path):
    """PATHWAY and MOLECULAR_FUNCTION are activities and must stay clean."""
    owl = _write_owl(tmp_path)
    for i, nt in enumerate(("PATHWAY", "MOLECULAR_FUNCTION")):
        d = _write(tmp_path, f"ok{i}.yaml", f"""\
identifier: traitmech:00006{i}
label: t
causal_graphs:
- graph_id: g
  nodes:
  - {{node_id: a, label: A, node_type: CHEMICAL}}
  - {{node_id: b, label: B, node_type: {nt}}}
  edges:
  - {{subject: a, predicate: enables, object: b, predicate_id: RO:0002327}}
""")
    assert [f for f in audit(d, owl) if f["defect"] == "ENABLES_RANGE_VIOLATION"] == []


def test_enables_on_process_not_flagged(tmp_path):
    """enables pointed at a process satisfies its range — no finding."""
    owl = _write_owl(tmp_path)
    d = _write(tmp_path, "ep.yaml", ENABLES_ON_PROCESS)
    assert audit(d, owl) == []


# --- clean corpus ------------------------------------------------------------

# Genuinely clean: enables points at a process (satisfies its range), and the
# second edge's predicate is outside the microbe-domain closure. Neither defect
# fires, so audit() must return [] with no filtering.
CLEAN = """\
identifier: traitmech:000006
label: t
causal_graphs:
- graph_id: g
  nodes:
  - {node_id: tr, label: T, node_type: TRAIT}
  - {node_id: proc, label: P, node_type: BIOLOGICAL_PROCESS}
  - {node_id: chem, label: C, node_type: CHEMICAL}
  edges:
  - {subject: chem, predicate: enables, object: proc, predicate_id: RO:0002327}
  - {subject: proc, predicate: y, object: tr, predicate_id: METPO:3000000}
"""


def test_clean_graph_has_no_findings(tmp_path):
    owl = _write_owl(tmp_path)
    d = _write(tmp_path, "clean.yaml", CLEAN)
    assert audit(d, owl) == []


def test_severity_assigned(tmp_path):
    owl = _write_owl(tmp_path)
    d = _write(tmp_path, "md.yaml", MICROBE_DOMAIN_EDGE)
    for f in audit(d, owl):
        assert f["severity"] in {"ERROR", "WARN"}
        assert f["severity"] == SEVERITY[f["defect"]]


# --- the ratchet's blocking contract -----------------------------------------

TWO_MICROBE_EDGES = """\
identifier: traitmech:000007
label: t
causal_graphs:
- graph_id: g
  nodes:
  - {node_id: proc, label: P, node_type: BIOLOGICAL_PROCESS}
  - {node_id: chem, label: C, node_type: CHEMICAL}
  - {node_id: gene, label: G, node_type: GENE_OR_PROTEIN}
  edges:
  - {subject: proc, predicate: produces, object: chem, predicate_id: METPO:2000202}
  - {subject: gene, predicate: produces, object: chem, predicate_id: METPO:2000202}
"""


def test_two_edges_get_distinct_baseline_keys(tmp_path):
    """Baselining one violating edge must not suppress the other."""
    owl = _write_owl(tmp_path)
    d = _write(tmp_path, "two.yaml", TWO_MICROBE_EDGES)
    findings = audit(d, owl)
    assert len(findings) == 2
    assert len({_key(f) for f in findings}) == 2
    frozen = {_key(findings[0])}
    new, _blocking = partition(findings, baseline=frozen, fail_on="new")
    assert [_key(r) for r in new] == [_key(findings[1])]


def test_ratchet_blocks_new_findings(tmp_path):
    """The ratchet blocks on severity-independent grounds: `new` means new."""
    owl = _write_owl(tmp_path)
    d = _write(tmp_path, "two.yaml", TWO_MICROBE_EDGES)
    findings = audit(d, owl)
    new, blocking = partition(findings, baseline=set(), fail_on="new")
    assert len(new) == len(blocking) == len(findings) == 2


def test_domain_class_is_error_so_it_cannot_be_baselined(tmp_path):
    """#315 review: the class distinction must be structural, not conventional.

    MICROBE_DOMAIN_ON_NONORGANISM is burned down (#301), so it is ERROR and
    `--write-baseline` refuses to freeze it. Without this, one `--write-baseline`
    run intended to re-freeze the ENABLES_RANGE_VIOLATION backlog would silently
    swallow a domain regression too.
    """
    owl = _write_owl(tmp_path)
    d = _write(tmp_path, "two.yaml", TWO_MICROBE_EDGES)
    assert all(f["severity"] == ERROR for f in audit(d, owl))
    baseline = tmp_path / "b.tsv"
    r = _run_cli(d, owl, tmp_path / "o.tsv", baseline, "--write-baseline")
    assert r.returncode == 1
    assert "Refusing to write baseline" in r.stderr
    assert not baseline.exists()


def test_ratchet_passes_when_everything_is_baselined(tmp_path):
    owl = _write_owl(tmp_path)
    d = _write(tmp_path, "two.yaml", TWO_MICROBE_EDGES)
    findings = audit(d, owl)
    frozen = {_key(f) for f in findings}
    new, blocking = partition(findings, baseline=frozen, fail_on="new")
    assert new == []
    assert blocking == []


def test_fail_on_any_ignores_the_baseline(tmp_path):
    owl = _write_owl(tmp_path)
    d = _write(tmp_path, "two.yaml", TWO_MICROBE_EDGES)
    findings = audit(d, owl)
    frozen = {_key(f) for f in findings}
    _new, blocking = partition(findings, baseline=frozen, fail_on="any")
    assert len(blocking) == len(findings) == 2


# --- CLI contract ------------------------------------------------------------


def _run_cli(traits_dir, owl, out, baseline, *extra):
    return subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "audit_predicate_domains.py"),
         "--traits-dir", str(traits_dir), "--owl", str(owl), "--out", str(out),
         "--baseline", str(baseline), *extra],
        capture_output=True, text=True,
    )


def test_write_baseline_freezes_then_passes(tmp_path):
    """The ratchet still works, but now only when asked for explicitly (#327).

    `--fail-on` defaults to `any` since the backlog reached zero, so a baseline
    no longer forgives anything by default — that is the whole point of the
    hardening. Reintroducing the ratchet for a NEW class of violation means
    passing `--fail-on new` alongside `--write-baseline`.
    """
    owl = _write_owl(tmp_path)
    # A WARN-class fixture: only ENABLES_RANGE_VIOLATION is baselineable now.
    d = _write(tmp_path, "eq.yaml", ENABLES_ON_QUALITY)
    baseline = tmp_path / "baseline.tsv"
    out = tmp_path / "out.tsv"

    assert _run_cli(d, owl, out, baseline).returncode == 1  # violations block
    assert _run_cli(d, owl, out, baseline, "--write-baseline").returncode == 0
    assert baseline.exists()
    # Explicit ratchet mode forgives the frozen set...
    assert _run_cli(d, owl, out, baseline, "--fail-on", "new").returncode == 0
    # ...but the DEFAULT does not, even with that baseline sitting there.
    assert _run_cli(d, owl, out, baseline).returncode == 1
    assert _run_cli(d, owl, out, baseline, "--fail-on", "any").returncode == 1


def test_default_fail_on_is_any(tmp_path):
    """#327: a stray baseline file must not silently weaken a default run.

    The 🔵 raised in review — `--write-baseline` can still recreate the deleted
    file, and before this change a non-recipe invocation would have loaded it and
    passed. Pinned here so the hardening cannot be undone by an argparse edit.
    """
    owl = _write_owl(tmp_path)
    d = _write(tmp_path, "eq.yaml", ENABLES_ON_QUALITY)  # WARN class, baselineable
    baseline = tmp_path / "baseline.tsv"
    out = tmp_path / "out.tsv"
    _run_cli(d, owl, out, baseline, "--write-baseline")
    assert baseline.exists()
    assert _run_cli(d, owl, out, baseline).returncode == 1
