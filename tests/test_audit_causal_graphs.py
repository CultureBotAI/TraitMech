"""Unit tests for scripts/audit_causal_graphs.py.

Locks in that audit() flags:
- ORPHAN_NODE: a declared node no edge references.
- DANGLING_EDGE: an edge whose subject/object is not a declared node.
- and is silent on a fully-connected graph.
"""

from __future__ import annotations

import sys
import textwrap
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from audit_causal_graphs import audit  # noqa: E402


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
