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
    new, blocking = partition(findings, baseline=set(), fail_on="new")
    assert len(new) == 2
    assert len(blocking) == 2
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
    assert len(new) == 2
    assert blocking == []


def test_fail_on_any_ignores_the_baseline(tmp_path):
    """Post-burndown mode: baselined findings stop being forgiven."""
    d = _write(tmp_path, "island.yaml", ISLAND)
    findings = audit(d)
    frozen = {_key(f) for f in findings}
    _new, blocking = partition(findings, baseline=frozen, fail_on="any")
    assert len(blocking) == len(findings) == 2


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
