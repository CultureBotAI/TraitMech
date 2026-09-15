"""Both graph views must disclose borrowed vectors without changing map data."""

import json
import re
import shutil
import subprocess
from pathlib import Path

import pytest
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "src/traitmech/templates"


def render(name):
    env = Environment(loader=FileSystemLoader(TEMPLATES), autoescape=select_autoescape())
    return env.get_template(name).render(
        title="Graph", root="", projection={"label": "PaCMAP", "source": "fixture",
                                           "dimensions": 16},
        n_points=6, n_edges=0, href_by_id="{}", graph_edges="[]",
        data_url="data/points.json", total_traits=6,
    )


@pytest.mark.parametrize("name", ["umap.html", "graph.html"])
def test_both_views_connect_matching_metadata_to_visible_ui(name):
    html = render(name)
    assert "METPO trait embeddings" not in html
    assert "not an independently learned vector" in html
    assert 'id="matching-summary"' in html
    assert "showMatchingSummary(points);" in html
    assert "showMatchingTooltip(tooltip.node(), d);" in html
    assert "<th>Matching method</th><th>Source graph nodes</th>" in html
    assert "esc(matchingLabel(d))" in html and "esc(matchingNodes(d))" in html
    assert '["label", "id", "category", "match_method", "source_nodes", "x", "y"]' in html
    assert "matchingLabel(d), matchingNodes(d), d.umap_x" in html
    assert 'const activeCategories = new Set(cats)' in html
    assert 'const href = HREF_BY_ID[d.id]' in html


@pytest.mark.skipif(shutil.which("node") is None, reason="Node is optional for browser controls")
@pytest.mark.parametrize("name", ["umap.html", "graph.html"])
def test_actual_browser_matching_logic_and_safe_tooltip(name):
    html = render(name)
    script = re.search(r'<script id="graph-matching-provenance">(.*?)</script>', html, re.S)[1]
    control = r'''
const assert = require("node:assert/strict");
class Element {
  constructor(tag) { this.tag = tag; this.children = []; this.textContent = ""; }
  appendChild(child) { this.children.push(child); }
  replaceChildren() { this.children = []; }
  set innerHTML(value) { throw new Error("untrusted HTML insertion"); }
}
const summary = new Element("p");
global.document = {createElement: tag => new Element(tag),
  getElementById: id => { assert.equal(id, "matching-summary"); return summary; }};
const hostile = "<img src=x onerror=alert(1)>";
const points = [
 {id:"own", label:"Own", category:"test", match_method:"direct_metpo", kgm_nodes:["METPO:1"]},
 {id:"child", label:hostile, category:"test", match_method:"parent_proxy", kgm_nodes:["METPO:2"]},
 {id:"alias", match_method:"alias_table", kgm_nodes:["CHEBI:1", "CHEBI:2"]},
 {id:"label", match_method:"label_match", kgm_nodes:[hostile]},
 {id:"legacy"}, {id:"future", match_method:"new_method", kgm_nodes:[]}
];
showMatchingSummary(points);
assert.equal(summary.textContent,
 "1 Direct METPO match; 1 Parent proxy (borrowed parent vector); 1 Alias match; " +
 "1 Label match; 2 Unknown matching provenance.");
const box = new Element("div");
for (const point of points) {
 showMatchingTooltip(box, point);
 assert.equal(box.children.length, 4);
 assert.equal(box.children[2].textContent, matchingLabel(point));
 assert.equal(box.children[3].textContent, "Source graph nodes: " + matchingNodes(point));
}
showMatchingTooltip(box, points[1]);
assert.equal(box.children[0].textContent, hostile);
assert.equal(box.children[2].textContent, "Parent proxy (borrowed parent vector)");
assert.equal(box.children[3].textContent, "Source graph nodes: METPO:2");
showMatchingTooltip(box, points[3]);
assert.equal(box.children[3].textContent, "Source graph nodes: " + hostile);
assert.equal(matchingNodes(points[2]), "CHEBI:1, CHEBI:2");
assert.equal(matchingNodes(points[4]), "Not recorded");
assert.equal(matchingLabel(points[4]), "Unknown matching provenance");
console.log(JSON.stringify({status:"passed", methods:5, points:points.length}));
'''
    result = subprocess.run([shutil.which("node"), "-e", script + control],
                            capture_output=True, text=True, check=True)
    assert json.loads(result.stdout)["points"] == 6
