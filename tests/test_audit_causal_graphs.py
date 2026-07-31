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

import sys
import textwrap
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from audit_causal_graphs import SEVERITY, _key, audit  # noqa: E402


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
