"""Unit tests for scripts/audit_causal_graphs.py.

Locks in that audit() flags:
- ORPHAN_NODE: a declared node no edge references.
- DANGLING_EDGE: an edge whose subject/object is not a declared node.
- UNREACHABLE_FROM_TRAIT: a node with edges, but in an island that has no
  undirected path back to a TRAIT node.
- NO_TRAIT_NODE: a graph with nothing to anchor reachability to.
- and is silent on a fully-connected graph.

Also locks in the baseline ratchet: a frozen finding is suppressed, while a
newly-introduced one is not.
"""

from __future__ import annotations

import subprocess
import sys
import textwrap
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from audit_causal_graphs import (  # noqa: E402
    ERROR,
    SEVERITY,
    _key,
    audit,
    connectivity_rows,
    load_corpus,
    node_type_index,
    partition,
)


def _write(tmp_path: Path, name: str, body: str) -> Path:
    d = tmp_path / "traits"
    d.mkdir(exist_ok=True)
    (d / name).write_text(textwrap.dedent(body))
    return d


CLEAN = """\
identifier: traitmech:000001
label: t
causal_graphs:
- graph_id: g
  nodes:
  - {node_id: a, label: A, node_type: TRAIT}
  - {node_id: b, label: B, node_type: CHEMICAL}
  edges:
  - {subject: a, predicate: produces, object: b}
"""

ORPHAN = """\
identifier: traitmech:000002
label: t
causal_graphs:
- graph_id: g
  nodes:
  - {node_id: a, label: A, node_type: TRAIT}
  - {node_id: b, label: B, node_type: CHEMICAL}
  - {node_id: c, label: C, node_type: CHEMICAL}
  edges:
  - {subject: a, predicate: produces, object: b}
"""

DANGLING = """\
identifier: traitmech:000003
label: t
causal_graphs:
- graph_id: g
  nodes:
  - {node_id: a, label: A, node_type: TRAIT}
  edges:
  - {subject: a, predicate: produces, object: ghost}
"""


def test_clean_graph_has_no_findings(tmp_path):
    d = _write(tmp_path, "clean.yaml", CLEAN)
    assert audit(d) == []


def test_orphan_node_flagged(tmp_path):
    d = _write(tmp_path, "orphan.yaml", ORPHAN)
    findings = audit(d)
    assert len(findings) == 1
    assert findings[0]["defect"] == "ORPHAN_NODE"
    assert "node_id='c'" in findings[0]["detail"]


def test_dangling_edge_flagged(tmp_path):
    d = _write(tmp_path, "dangling.yaml", DANGLING)
    findings = audit(d)
    # 'ghost' object is dangling; node 'a' is referenced (subject) so not orphan.
    assert any(f["defect"] == "DANGLING_EDGE" and "ghost" in f["detail"] for f in findings)


ISLAND = """\
identifier: traitmech:000004
label: t
causal_graphs:
- graph_id: g
  nodes:
  - {node_id: a, label: A, node_type: TRAIT}
  - {node_id: b, label: B, node_type: CHEMICAL}
  - {node_id: c, label: C, node_type: CHEMICAL}
  - {node_id: d, label: D, node_type: CHEMICAL}
  edges:
  - {subject: a, predicate: produces, object: b}
  - {subject: c, predicate: produces, object: d}
"""

NO_TRAIT = """\
identifier: traitmech:000005
label: t
causal_graphs:
- graph_id: g
  nodes:
  - {node_id: a, label: A, node_type: CHEMICAL}
  - {node_id: b, label: B, node_type: CHEMICAL}
  edges:
  - {subject: a, predicate: produces, object: b}
"""

REVERSED_EDGE = """\
identifier: traitmech:000006
label: t
causal_graphs:
- graph_id: g
  nodes:
  - {node_id: a, label: A, node_type: TRAIT}
  - {node_id: b, label: B, node_type: GENE_OR_PROTEIN}
  edges:
  - {subject: b, predicate: enables, object: a}
"""


def test_island_unreachable_from_trait(tmp_path):
    """c/d form a connected island; both have edges, so ORPHAN_NODE misses them."""
    d = _write(tmp_path, "island.yaml", ISLAND)
    findings = audit(d)
    unreachable = {f["detail"].split("'")[1] for f in findings
                   if f["defect"] == "UNREACHABLE_FROM_TRAIT"}
    assert unreachable == {"c", "d"}
    assert not any(f["defect"] == "ORPHAN_NODE" for f in findings)


def test_reachability_is_undirected(tmp_path):
    """`b -enables-> a` must not flag b: direction is a modelling choice."""
    d = _write(tmp_path, "reversed.yaml", REVERSED_EDGE)
    assert audit(d) == []


def test_no_trait_node_flagged(tmp_path):
    d = _write(tmp_path, "notrait.yaml", NO_TRAIT)
    findings = audit(d)
    assert [f["defect"] for f in findings] == ["NO_TRAIT_NODE"]


def test_unreachable_not_double_reported_as_orphan(tmp_path):
    """A zero-edge node is ORPHAN_NODE only, never also UNREACHABLE_FROM_TRAIT."""
    d = _write(tmp_path, "orphan2.yaml", ORPHAN)
    findings = audit(d)
    assert len(findings) == 1
    assert findings[0]["defect"] == "ORPHAN_NODE"


def test_baseline_suppresses_known_but_not_new(tmp_path):
    d = _write(tmp_path, "island.yaml", ISLAND)
    findings = audit(d)
    # Freeze only node 'c'; 'd' must remain unbaselined.
    frozen = {_key(f) for f in findings if "'c'" in f["detail"]}
    new = [f for f in findings if _key(f) not in frozen]
    assert all("'c'" not in f["detail"] for f in new)
    assert any("'d'" in f["detail"] for f in new)


def test_severity_assigned(tmp_path):
    d = _write(tmp_path, "island.yaml", ISLAND)
    for f in audit(d):
        assert f["severity"] in {"ERROR", "WARN"}
        assert f["severity"] == SEVERITY[f["defect"]]


# --- the ratchet's blocking contract (issue #186) ---------------------------
#
# The first cut of this check defaulted --fail-on to "error", so a newly
# introduced WARN island was reported and then ignored: the ratchet did not
# ratchet. These lock the exit-code contract for each mode.


def test_ratchet_blocks_new_warn_findings(tmp_path):
    """Default mode: a new WARN island blocks even though it is not an ERROR."""
    d = _write(tmp_path, "island.yaml", ISLAND)
    findings = audit(d)
    # ISLAND yields two UNREACHABLE_FROM_TRAIT plus one FRAGMENTED_GRAPH (#220).
    # Asserted as a set rather than a count so adding a defect cannot silently
    # weaken this into "some findings block".
    assert {f["defect"] for f in findings} == {
        "UNREACHABLE_FROM_TRAIT", "FRAGMENTED_GRAPH"}
    new, blocking = partition(findings, baseline=set(), fail_on="new")
    assert len(new) == len(blocking) == len(findings) == 3
    assert all(r["severity"] != ERROR for r in blocking)


def test_ratchet_passes_when_everything_is_baselined(tmp_path):
    d = _write(tmp_path, "island.yaml", ISLAND)
    findings = audit(d)
    frozen = {_key(f) for f in findings}
    new, blocking = partition(findings, baseline=frozen, fail_on="new")
    assert new == []
    assert blocking == []


def test_fail_on_error_does_not_block_new_warns(tmp_path):
    """The documented looser mode: report new fragmentation, do not fail on it."""
    d = _write(tmp_path, "island.yaml", ISLAND)
    findings = audit(d)
    new, blocking = partition(findings, baseline=set(), fail_on="error")
    assert len(new) == len(findings) == 3
    assert blocking == []


def test_fail_on_any_ignores_the_baseline(tmp_path):
    """Post-burndown mode: baselined findings stop being forgiven."""
    d = _write(tmp_path, "island.yaml", ISLAND)
    findings = audit(d)
    frozen = {_key(f) for f in findings}
    _new, blocking = partition(findings, baseline=frozen, fail_on="any")
    assert len(blocking) == len(findings) == 3


TWO_DANGLING = """\
identifier: traitmech:000007
label: t
causal_graphs:
- graph_id: g
  nodes:
  - {node_id: a, label: A, node_type: TRAIT}
  edges:
  - {subject: a, predicate: produces, object: ghost1}
  - {subject: a, predicate: produces, object: ghost2}
"""


def test_dangling_edges_get_distinct_baseline_keys(tmp_path):
    """Issue #187: baselining one dangling edge must not suppress the others."""
    d = _write(tmp_path, "twodangling.yaml", TWO_DANGLING)
    dangling = [f for f in audit(d) if f["defect"] == "DANGLING_EDGE"]
    assert len(dangling) == 2
    assert len({_key(f) for f in dangling}) == 2

    frozen = {_key(dangling[0])}
    new, _blocking = partition(dangling, baseline=frozen, fail_on="new")
    assert [_key(r) for r in new] == [_key(dangling[1])]


def _run_cli(traits_dir, out, baseline, *extra):
    return subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "audit_causal_graphs.py"),
         "--traits-dir", str(traits_dir), "--out", str(out),
         "--baseline", str(baseline), *extra],
        capture_output=True, text=True,
    )


def test_write_baseline_refuses_to_freeze_errors(tmp_path):
    """Issue #188: the baseline parks the WARN backlog, not structural errors."""
    d = _write(tmp_path, "twodangling.yaml", TWO_DANGLING)
    baseline = tmp_path / "baseline.tsv"
    r = _run_cli(d, tmp_path / "out.tsv", baseline, "--write-baseline")
    assert r.returncode == 1
    assert "Refusing to write baseline" in r.stderr
    assert not baseline.exists()


def test_write_baseline_freezes_warns_then_passes(tmp_path):
    d = _write(tmp_path, "island.yaml", ISLAND)
    baseline = tmp_path / "baseline.tsv"
    out = tmp_path / "out.tsv"

    assert _run_cli(d, out, baseline).returncode == 1  # new island blocks
    assert _run_cli(d, out, baseline, "--write-baseline").returncode == 0
    assert baseline.exists()
    assert _run_cli(d, out, baseline).returncode == 0  # now forgiven
    assert _run_cli(d, out, baseline, "--fail-on", "any").returncode == 1


# --- FRAGMENTED_GRAPH (#220) -------------------------------------------------
#
# UNREACHABLE_FROM_TRAIT anchors on ANY node typed TRAIT, which is correct —
# 85 of 353 real graphs carry several, because a record links its parent and
# child traits as nodes. The consequence is that a graph splitting into
# components that EACH contain a TRAIT node reports clean, which is how
# morphology/dumbbell_shaped.yaml hid 7 of its 11 nodes from the audit.

TWO_TRAIT_BEARING_COMPONENTS = """\
identifier: traitmech:000010
label: t
causal_graphs:
- graph_id: g
  nodes:
  - {node_id: own_trait, label: Own, node_type: TRAIT}
  - {node_id: cause, label: Cause, node_type: BIOLOGICAL_PROCESS}
  - {node_id: other_trait, label: Other, node_type: TRAIT}
  - {node_id: far_a, label: FarA, node_type: BIOLOGICAL_PROCESS}
  - {node_id: far_b, label: FarB, node_type: CHEMICAL}
  edges:
  - {subject: cause, predicate: manifests as, object: own_trait}
  - {subject: far_a, predicate: produces, object: other_trait}
  - {subject: far_b, predicate: enables, object: far_a}
"""


def test_two_trait_bearing_components_flagged(tmp_path):
    """The #220 case: the split the old audit could not see."""
    d = _write(tmp_path, "split.yaml", TWO_TRAIT_BEARING_COMPONENTS)
    findings = audit(d)
    frag = [f for f in findings if f["defect"] == "FRAGMENTED_GRAPH"]
    assert len(frag) == 1
    assert frag[0]["detail"].startswith("components=2 ")
    assert "sizes: 3, 2" in frag[0]["detail"]


def test_the_old_check_stays_silent_on_it(tmp_path):
    """Pins WHY the new defect is needed rather than just that it fires.

    Every node reaches *a* TRAIT node, so UNREACHABLE_FROM_TRAIT is correctly
    silent — if this ever starts firing, FRAGMENTED_GRAPH has stopped being the
    thing that catches this shape and the rationale needs revisiting.
    """
    d = _write(tmp_path, "split.yaml", TWO_TRAIT_BEARING_COMPONENTS)
    assert [f for f in audit(d) if f["defect"] == "UNREACHABLE_FROM_TRAIT"] == []


def test_connected_graph_is_not_fragmented(tmp_path):
    d = _write(tmp_path, "clean.yaml", CLEAN)
    assert [f for f in audit(d) if f["defect"] == "FRAGMENTED_GRAPH"] == []


def test_orphan_node_is_not_also_reported_as_fragmented(tmp_path):
    """A zero-edge node is its own component, but ORPHAN_NODE already owns it.

    Components are computed over edge-referenced nodes for exactly this reason —
    two findings for one defect is the noise that gets a check switched off.
    """
    d = _write(tmp_path, "orphan.yaml", ORPHAN)
    assert [f["defect"] for f in audit(d)] == ["ORPHAN_NODE"]


def test_island_is_reported_by_both_checks(tmp_path):
    """An island with no TRAIT node trips the old check AND the new one.

    They answer different questions — "can this node reach the trait?" and "is
    this one graph?" — so overlap here is correct, not duplication.
    """
    d = _write(tmp_path, "island.yaml", ISLAND)
    defects = {f["defect"] for f in audit(d)}
    assert "UNREACHABLE_FROM_TRAIT" in defects
    assert "FRAGMENTED_GRAPH" in defects


def test_fragmented_graph_severity_is_warn(tmp_path):
    """WARN, like UNREACHABLE_FROM_TRAIT: 220 graphs are fragmented today, so
    ERROR would be un-landable under --fail-on error."""
    assert SEVERITY["FRAGMENTED_GRAPH"] == "WARN"


# The baseline discriminator is the leading token of `detail` (see _key), so
# what that token carries decides whether the ratchet works. For
# FRAGMENTED_GRAPH it has to be the component count: leading with the node count
# let a baselined graph go from 3 components to 4 without changing its key.

FRAG_3_COMPONENTS = """\
identifier: traitmech:000011
label: t
causal_graphs:
- graph_id: g
  nodes:
  - {node_id: a, label: A, node_type: TRAIT}
  - {node_id: b, label: B, node_type: CHEMICAL}
  - {node_id: c, label: C, node_type: CHEMICAL}
  - {node_id: d, label: D, node_type: CHEMICAL}
  - {node_id: e, label: E, node_type: CHEMICAL}
  - {node_id: f, label: F, node_type: CHEMICAL}
  edges:
  - {subject: a, predicate: produces, object: b}
  - {subject: c, predicate: produces, object: d}
  - {subject: e, predicate: produces, object: f}
"""

# Same six nodes, but the c-d bridge is gone: c and d each stand alone, so the
# graph goes 3 components -> 4 with the node count unchanged.
FRAG_4_COMPONENTS = FRAG_3_COMPONENTS.replace(
    "  - {subject: c, predicate: produces, object: d}\n", "")

# 3 components still, but one extra node inside an existing component — the
# ordinary shape of #183's evidence backfill.
FRAG_3_COMPONENTS_EXTRA_NODE = FRAG_3_COMPONENTS.replace(
    "  edges:",
    "  - {node_id: g2, label: G, node_type: CHEMICAL}\n  edges:",
).replace(
    "  - {subject: e, predicate: produces, object: f}\n",
    "  - {subject: e, predicate: produces, object: f}\n"
    "  - {subject: a, predicate: produces, object: g2}\n")


def _frag_finding(tmp_path, body):
    """Audit `body` at a FIXED path and return its FRAGMENTED_GRAPH finding.

    Same path every time on purpose: `_key` includes the file and graph_id, so
    fixtures in different temp dirs would differ by path and these tests would
    pass without ever exercising the discriminator they exist to pin.
    """
    d = _write(tmp_path, "g.yaml", body)
    frag = [f for f in audit(d) if f["defect"] == "FRAGMENTED_GRAPH"]
    assert len(frag) == 1, frag
    return frag[0]


def test_more_components_changes_the_baseline_key(tmp_path):
    """Losing a bridging edge must un-suppress a baselined fragmented graph.

    Node count is identical across these two, so a node-count discriminator
    keeps the key stable and the regression stays silent — the ratchet failing
    open exactly where it is supposed to bite.
    """
    three = _key(_frag_finding(tmp_path, FRAG_3_COMPONENTS))
    four = _key(_frag_finding(tmp_path, FRAG_4_COMPONENTS))
    assert three != four
    assert three[:3] == four[:3], "only the discriminator may differ"


def test_adding_a_node_does_not_change_the_baseline_key(tmp_path):
    """The other direction: growing an already-fragmented graph must not block.

    Component count is unchanged, so a baselined finding stays baselined and
    #183's backfill does not trip `--fail-on new` for standing fragmentation.
    """
    before = _key(_frag_finding(tmp_path, FRAG_3_COMPONENTS))
    after = _key(_frag_finding(tmp_path, FRAG_3_COMPONENTS_EXTRA_NODE))
    assert before == after


def test_ratchet_catches_worsening_fragmentation_end_to_end(tmp_path):
    """The property the two key tests protect, through partition()."""
    frozen = {_key(_frag_finding(tmp_path, FRAG_3_COMPONENTS))}
    d = _write(tmp_path, "g.yaml", FRAG_4_COMPONENTS)
    new, blocking = partition(audit(d), baseline=frozen, fail_on="new")
    assert any(f["defect"] == "FRAGMENTED_GRAPH" for f in new)
    assert any(f["defect"] == "FRAGMENTED_GRAPH" for f in blocking)


def test_ratchet_stays_quiet_when_only_a_node_was_added(tmp_path):
    """Same harness, opposite direction — no FRAGMENTED_GRAPH in `new`."""
    frozen = {_key(f) for f in audit(_write(tmp_path, "g.yaml", FRAG_3_COMPONENTS))}
    d = _write(tmp_path, "g.yaml", FRAG_3_COMPONENTS_EXTRA_NODE)
    new, _blocking = partition(audit(d), baseline=frozen, fail_on="new")
    assert not any(f["defect"] == "FRAGMENTED_GRAPH" for f in new)


# --- DUPLICATE_GROUNDING and DISPOSITION_MISTYPED (#352) ---------------------

DUPLICATE_GROUNDING_YAML = """\
identifier: traitmech:000020
label: t
causal_graphs:
- graph_id: g
  nodes:
  - {node_id: a, label: A, node_type: TRAIT, grounding: 'METPO:1000478'}
  - {node_id: b, label: B, node_type: TRAIT, grounding: 'METPO:1000478'}
  edges:
  - {subject: a, predicate: x, object: b}
"""

DISPOSITION_YAML = """\
identifier: traitmech:000021
label: t
causal_graphs:
- graph_id: g
  nodes:
  - {node_id: tr, label: T, node_type: TRAIT}
  - {node_id: cap, label: salt tolerance, node_type: CAPACITY,
     description: Capacity to grow and survive under elevated salinity.}
  edges:
  - {subject: cap, predicate: x, object: tr}
"""


def test_two_nodes_sharing_a_grounding_are_flagged(tmp_path):
    """One concept modelled twice -- the machine-readable signature #352 wanted."""
    d = _write(tmp_path, "dup.yaml", DUPLICATE_GROUNDING_YAML)
    dup = [f for f in audit(d) if f["defect"] == "DUPLICATE_GROUNDING"]
    assert len(dup) == 1
    assert "METPO:1000478" in dup[0]["detail"]
    assert "a" in dup[0]["detail"] and "b" in dup[0]["detail"]


def test_distinct_groundings_are_not_flagged(tmp_path):
    d = _write(tmp_path, "ok.yaml", DUPLICATE_GROUNDING_YAML.replace(
        "grounding: 'METPO:1000478'}\n  - {node_id: b", "grounding: 'METPO:1000479'}\n  - {node_id: b"))
    assert [f for f in audit(d) if f["defect"] == "DUPLICATE_GROUNDING"] == []


def test_an_ungrounded_pair_is_not_flagged(tmp_path):
    """Absent groundings must not collapse onto one another as ''."""
    d = _write(tmp_path, "none.yaml", """\
identifier: traitmech:000022
label: t
causal_graphs:
- graph_id: g
  nodes:
  - {node_id: a, label: A, node_type: TRAIT}
  - {node_id: b, label: B, node_type: TRAIT}
  edges:
  - {subject: a, predicate: x, object: b}
""")
    assert [f for f in audit(d) if f["defect"] == "DUPLICATE_GROUNDING"] == []


def test_a_capacity_described_as_a_disposition_is_flagged(tmp_path):
    d = _write(tmp_path, "disp.yaml", DISPOSITION_YAML)
    mis = [f for f in audit(d) if f["defect"] == "DISPOSITION_MISTYPED"]
    assert len(mis) == 1 and "salt_tolerance" not in mis[0]["detail"]
    assert "cap" in mis[0]["detail"]


def test_capacity_of_a_cell_to_is_also_caught(tmp_path):
    """The phrasing a hand-written sweep missed: 'Capacity OF A CELL to ...'."""
    d = _write(tmp_path, "d2.yaml", DISPOSITION_YAML.replace(
        "Capacity to grow", "Capacity of a cell to grow"))
    assert [f["defect"] for f in audit(d) if f["defect"] == "DISPOSITION_MISTYPED"] == [
        "DISPOSITION_MISTYPED"]


def test_a_plain_state_is_not_flagged(tmp_path):
    """A gradient or an environment is a genuine STATE, not a disposition."""
    d = _write(tmp_path, "d3.yaml", DISPOSITION_YAML.replace(
        "Capacity to grow and survive under elevated salinity.",
        "Transmembrane proton gradient generated by light-driven pumping."))
    assert [f for f in audit(d) if f["defect"] == "DISPOSITION_MISTYPED"] == []


def test_a_non_organism_capacity_is_not_flagged():
    """#353 review: a reservoir CAPACITY must not read as a disposition.

    ph_optimum.yaml has "Capacity of cytoplasmic buffers ... to absorb pH
    fluctuations". A looser pattern let it through only because the dots in
    "e.g." stopped a character class -- a right answer for an accidental reason.
    This pins that it stays right WITHOUT the parenthetical.
    """
    from audit_causal_graphs import _DISPOSITION_RE
    assert not _DISPOSITION_RE.search(
        "Capacity of cytoplasmic buffers to absorb pH fluctuations")
    assert _DISPOSITION_RE.search("Capacity of a cell to survive exposure to oxygen")


def test_the_label_is_not_scanned(tmp_path):
    """The docstring says description-only, so the code must be too."""
    d = _write(tmp_path, "lbl.yaml", """\
identifier: traitmech:000023
label: t
causal_graphs:
- graph_id: g
  nodes:
  - {node_id: tr, label: T, node_type: TRAIT}
  - {node_id: c, label: tolerance of salt, node_type: CAPACITY,
     description: A transmembrane gradient.}
  edges:
  - {subject: c, predicate: x, object: tr}
""")
    assert [f for f in audit(d) if f["defect"] == "DISPOSITION_MISTYPED"] == []


def test_a_third_node_joining_a_grounding_re_keys(tmp_path):
    """#353 review: leading the detail with the CURIE would keep the baseline
    key stable, so freezing two nodes would silently forgive three."""
    two = _write(tmp_path, "g.yaml", DUPLICATE_GROUNDING_YAML)
    k2 = {_key(f) for f in audit(two) if f["defect"] == "DUPLICATE_GROUNDING"}
    three = _write(tmp_path, "g.yaml", DUPLICATE_GROUNDING_YAML.replace(
        "  edges:",
        "  - {node_id: c, label: C, node_type: TRAIT, grounding: 'METPO:1000478'}\n  edges:"))
    k3 = {_key(f) for f in audit(three) if f["defect"] == "DUPLICATE_GROUNDING"}
    assert k2 and k3 and k2 != k3


def test_two_groundings_of_equal_size_do_not_collide(tmp_path):
    """#353 review round 2: the mirror of the above. Leading the detail with the
    COUNT alone would key two different 2-node groundings identically, so
    freezing one would forgive the other. Both parts must vary."""
    d = _write(tmp_path, "g.yaml", DUPLICATE_GROUNDING_YAML.replace(
        "  edges:",
        "  - {node_id: c, label: C, node_type: TRAIT, grounding: 'METPO:1000999'}\n"
        "  - {node_id: d, label: D, node_type: TRAIT, grounding: 'METPO:1000999'}\n"
        "  edges:"))
    dupes = [f for f in audit(d) if f["defect"] == "DUPLICATE_GROUNDING"]
    assert len(dupes) == 2
    assert len({_key(f) for f in dupes}) == 2


# ------------------------------------------------- connectivity metric (#359)
#
# The property under test is the one #359 was filed for: a node RETYPED into a
# TRAIT anchor inside an existing island moves UNREACHABLE_FROM_TRAIT without
# connecting anything, while MERGING that node attaches the island for real.
# The fixtures below are the shape of oxygen_preference.yaml reduced to its
# essentials -- a trait with one wired-in phenotype, plus a detached two-node
# island whose member is the candidate.

ISLAND_BEFORE = """\
identifier: traitmech:000900
label: t
causal_graphs:
- graph_id: g
  nodes:
  - {node_id: trait, label: trait, node_type: TRAIT}
  - {node_id: pheno, label: pheno, node_type: TRAIT}
  - {node_id: tolerance, label: tolerance, node_type: CAPACITY}
  - {node_id: enzyme, label: enzyme, node_type: GENE_OR_PROTEIN}
  edges:
  - {subject: pheno, object: trait, predicate: is a}
  - {subject: enzyme, object: tolerance, predicate: increases}
"""

# The wrong fix: `tolerance` becomes a TRAIT. Nothing is rewired.
ISLAND_RETYPED = ISLAND_BEFORE.replace(
    "{node_id: tolerance, label: tolerance, node_type: CAPACITY}",
    "{node_id: tolerance, label: tolerance, node_type: TRAIT}")

# The right fix: `tolerance` is merged away and its edge repointed at `trait`.
ISLAND_MERGED = """\
identifier: traitmech:000900
label: t
causal_graphs:
- graph_id: g
  nodes:
  - {node_id: trait, label: trait, node_type: TRAIT}
  - {node_id: pheno, label: pheno, node_type: TRAIT}
  - {node_id: enzyme, label: enzyme, node_type: GENE_OR_PROTEIN}
  edges:
  - {subject: pheno, object: trait, predicate: is a}
  - {subject: enzyme, object: trait, predicate: increases}
"""


def _isolated(tmp_path: Path, sub: str, body: str) -> Path:
    """A corpus dir of its own.

    ``_write`` reuses one directory, so two fixtures in a single test would
    land in the same corpus and every walk would see both.
    """
    d = tmp_path / sub / "traits"
    d.mkdir(parents=True)
    (d / "rec.yaml").write_text(textwrap.dedent(body))
    return d


def _conn(tmp_path: Path, sub: str, body: str) -> dict:
    row, = connectivity_rows(_isolated(tmp_path, sub, body))
    return row


def test_connectivity_reports_components_and_largest(tmp_path):
    row = _conn(tmp_path, "before", ISLAND_BEFORE)
    assert row["wired_nodes"] == "4"
    assert row["components"] == "2"
    assert row["largest_component"] == "2"
    assert row["component_sizes"] == "2,2"


def test_retyping_into_an_anchor_does_not_move_connectivity(tmp_path):
    """#359's whole point. The retype silences UNREACHABLE_FROM_TRAIT for the
    island -- and leaves the connectivity metric bit-for-bit unchanged,
    because nothing was actually joined."""
    before = _conn(tmp_path, "before", ISLAND_BEFORE)
    after = _conn(tmp_path, "after", ISLAND_RETYPED)

    assert {k: v for k, v in after.items() if k != "file"} == \
           {k: v for k, v in before.items() if k != "file"}

    # ... while the finding count DOES move, which is the trap.
    unreachable_before = [f for f in audit(_isolated(tmp_path, "b2", ISLAND_BEFORE))
                          if f["defect"] == "UNREACHABLE_FROM_TRAIT"]
    unreachable_after = [f for f in audit(_isolated(tmp_path, "a2", ISLAND_RETYPED))
                         if f["defect"] == "UNREACHABLE_FROM_TRAIT"]
    assert len(unreachable_before) > len(unreachable_after)


def test_merging_the_node_does_move_connectivity(tmp_path):
    before = _conn(tmp_path, "before", ISLAND_BEFORE)
    after = _conn(tmp_path, "after", ISLAND_MERGED)
    assert before["components"] == "2" and after["components"] == "1"
    assert before["largest_component"] == "2" and after["largest_component"] == "3"


def test_connectivity_skips_unwired_nodes(tmp_path):
    """An edgeless node is ORPHAN_NODE's business; counting it here would let
    one defect depress two metrics."""
    body = ISLAND_BEFORE.replace(
        "  edges:",
        "  - {node_id: lonely, label: lonely, node_type: CHEMICAL}\n  edges:", 1)
    row = _conn(tmp_path, "orphan", body)
    assert row["wired_nodes"] == "4"
    assert row["component_sizes"] == "2,2"


def test_connectivity_row_per_graph_not_per_file(tmp_path):
    two = ISLAND_BEFORE + textwrap.dedent("""\
        - graph_id: g2
          nodes:
          - {node_id: t2, label: t2, node_type: TRAIT}
          - {node_id: x2, label: x2, node_type: CHEMICAL}
          edges:
          - {subject: x2, object: t2, predicate: affects}
        """)
    rows = connectivity_rows(_isolated(tmp_path, "two", two))
    assert [r["graph_id"] for r in rows] == ["g", "g2"]
    assert [r["components"] for r in rows] == ["2", "1"]


def test_connectivity_out_defaults_next_to_out_not_into_the_repo(tmp_path):
    """Regression: the connectivity report must follow --out.

    With a fixed repo default, every subprocess test that redirected --out to a
    tmpdir still wrote this file into the working tree -- one of them clobbered
    the committed report with a single row naming a pytest tmpdir, and only the
    staleness gate noticed. A side effect that ignores --out is a side effect
    that lands in the repo.
    """
    d = _isolated(tmp_path, "corpus", ISLAND_BEFORE)
    out = tmp_path / "elsewhere" / "audit.tsv"
    subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "audit_causal_graphs.py"),
         "--traits-dir", str(d), "--out", str(out), "--no-baseline"],
        check=False, capture_output=True,
    )
    assert (out.parent / "causal_graph_connectivity.tsv").exists()
    assert not (REPO_ROOT / "reports" / "causal_graph_connectivity.tsv").samefile(
        out.parent / "causal_graph_connectivity.tsv")


# --------------------------------------------- INCONSISTENT_NODE_TYPE (#356)

TYPED_STATE = """\
identifier: traitmech:000910
label: a
causal_graphs:
- graph_id: ga
  nodes:
  - {node_id: trait_a, label: a, node_type: TRAIT}
  - {node_id: proton_motive_force, label: pmf, node_type: STATE}
  edges:
  - {subject: proton_motive_force, object: trait_a, predicate: confers}
"""

TYPED_CAPACITY = TYPED_STATE.replace("traitmech:000910", "traitmech:000911") \
                            .replace("graph_id: ga", "graph_id: gb") \
                            .replace("node_type: STATE", "node_type: CAPACITY")


def _multi_record(tmp_path: Path, *bodies: str) -> Path:
    d = tmp_path / "traits"
    d.mkdir(exist_ok=True)
    for i, body in enumerate(bodies):
        (d / f"rec{i}.yaml").write_text(textwrap.dedent(body))
    return d


def test_inconsistent_node_type_is_cross_record(tmp_path):
    """Neither record is wrong read alone — which is why nothing caught this
    before. Each occurrence is reported, so the family clears together."""
    d = _multi_record(tmp_path, TYPED_STATE, TYPED_CAPACITY)
    hits = [f for f in audit(d) if f["defect"] == "INCONSISTENT_NODE_TYPE"]

    assert len(hits) == 2
    assert {f["file"].split("/")[-1] for f in hits} == {"rec0.yaml", "rec1.yaml"}
    for f in hits:
        assert f["detail"].startswith("node_id='proton_motive_force'")
        assert f["severity"] == SEVERITY["INCONSISTENT_NODE_TYPE"]
    # Each row names the OTHER typing, so a row is actionable on its own.
    assert "CAPACITY×1" in next(f["detail"] for f in hits if f["file"].endswith("rec0.yaml"))
    assert "STATE×1" in next(f["detail"] for f in hits if f["file"].endswith("rec1.yaml"))


def test_consistent_node_type_across_records_is_silent(tmp_path):
    """One id used in twenty records with one type is not a finding — the
    check is about disagreement, not about reuse."""
    d = _multi_record(tmp_path, TYPED_STATE,
                      TYPED_STATE.replace("traitmech:000910", "traitmech:000912")
                                 .replace("graph_id: ga", "graph_id: gc"))
    assert [f for f in audit(d) if f["defect"] == "INCONSISTENT_NODE_TYPE"] == []


def test_inconsistent_node_type_keys_on_node_id_not_the_type_set(tmp_path):
    """The baseline discriminator must be the node_id.

    Leading with the type set would re-key every row of a family each time one
    member is fixed, un-suppressing rows nobody has reached yet — a burn-down
    that fights itself.
    """
    d = _multi_record(tmp_path, TYPED_STATE, TYPED_CAPACITY)
    before = {_key(f) for f in audit(d) if f["defect"] == "INCONSISTENT_NODE_TYPE"}

    # A third record joins with yet another type: the type SET changes, so the
    # detail text changes, but the existing rows must keep their identity.
    third = TYPED_STATE.replace("traitmech:000910", "traitmech:000913") \
                       .replace("graph_id: ga", "graph_id: gd") \
                       .replace("node_type: STATE", "node_type: CHEMICAL")
    (tmp_path / "traits" / "rec2.yaml").write_text(textwrap.dedent(third))
    after = {_key(f) for f in audit(d) if f["defect"] == "INCONSISTENT_NODE_TYPE"}

    assert before < after          # old keys survive verbatim
    assert len(after) == len(before) + 1


def test_node_type_index_counts_occurrences_per_type(tmp_path):
    d = _multi_record(tmp_path, TYPED_STATE, TYPED_CAPACITY)
    idx = node_type_index(d)
    assert idx["proton_motive_force"] == {"STATE": 1, "CAPACITY": 1}
    assert idx["trait_a"] == {"TRAIT": 2}


def test_node_type_index_counts_occurrences_not_records(tmp_path):
    """Pins the distinction the old fixtures could not see (#374).

    Every fixture above has one graph per record, so occurrence-counting and
    record-counting agree and either implementation passes. This record carries
    the same node_id in TWO graphs, which is where they diverge — and the count
    is quoted into the finding text, so it has to mean what it says.
    """
    two_graphs = """\
        identifier: traitmech:000920
        label: a
        causal_graphs:
        - graph_id: g1
          nodes:
          - {node_id: t1, label: t1, node_type: TRAIT}
          - {node_id: pmf, label: pmf, node_type: STATE}
          edges:
          - {subject: pmf, object: t1, predicate: confers}
        - graph_id: g2
          nodes:
          - {node_id: t2, label: t2, node_type: TRAIT}
          - {node_id: pmf, label: pmf, node_type: STATE}
          edges:
          - {subject: pmf, object: t2, predicate: confers}
        """
    idx = node_type_index(_isolated(tmp_path, "two_graphs", two_graphs))
    # One RECORD, two OCCURRENCES.
    assert idx["pmf"] == {"STATE": 2}


# ------------------------------------------------- one corpus walk (#373)


def test_load_corpus_returns_relative_path_and_doc(tmp_path):
    d = _isolated(tmp_path, "c", ISLAND_BEFORE)
    corpus = load_corpus(d)
    assert len(corpus) == 1
    rel, doc = corpus[0]
    assert rel.endswith("rec.yaml")
    assert doc["identifier"] == "traitmech:000900"


def test_load_corpus_skips_unparseable_and_non_mapping(tmp_path):
    """The skip lived in three places before; it lives here now, so every
    projection sees the same file set by construction."""
    d = _isolated(tmp_path, "c", ISLAND_BEFORE)
    (d / "broken.yaml").write_text("nodes: [unclosed\n")
    (d / "scalar.yaml").write_text("just a string\n")
    rels = [rel for rel, _ in load_corpus(d)]
    assert len(rels) == 1
    assert rels[0].endswith("rec.yaml")


def test_passes_accept_a_preloaded_corpus_and_agree_with_the_path_form(tmp_path):
    """The whole point of #373: main() parses once and hands the same list to
    all three passes, so they must give identical answers either way."""
    d = _isolated(tmp_path, "c", ISLAND_BEFORE)
    corpus = load_corpus(d)

    assert audit(corpus) == audit(d)
    assert connectivity_rows(corpus) == connectivity_rows(d)
    assert node_type_index(corpus) == node_type_index(d)


def test_audit_does_not_reparse_when_given_a_corpus(tmp_path, monkeypatch):
    """audit() runs the INCONSISTENT_NODE_TYPE pre-pass internally. Handed a
    corpus it must reuse it rather than walking again — otherwise the caller's
    single load is undone one level down."""
    import audit_causal_graphs as mod
    d = _isolated(tmp_path, "c", ISLAND_BEFORE)
    corpus = load_corpus(d)

    calls = []
    monkeypatch.setattr(mod, "load_corpus", lambda p: calls.append(p) or [])
    mod.audit(corpus)
    assert calls == []
