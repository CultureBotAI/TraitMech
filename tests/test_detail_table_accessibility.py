"""Populated detail tables remain named, keyboard-accessible scientific HTML."""

import sys
from html.parser import HTMLParser
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from render_trait_pages import causal_graphs_for_template, template_environment  # noqa: E402


class TableParents(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.divs = []
        self.tables = []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        if tag == "div":
            self.divs.append(dict(attrs))
        elif tag == "table":
            self.tables.append(self.divs[-1] if self.divs else {})

    def handle_endtag(self, tag):
        if tag == "div":
            self.divs.pop()


def test_detail_tables_keep_names_keyboard_access_and_scientific_links():
    trait = yaml.safe_load((ROOT / "data/traits/physiology/mixotrophic.yaml").read_text())
    graphs = causal_graphs_for_template(trait)
    assert graphs and graphs[0]["protein_example_rows"]
    graphs[0]["title"] = 'Graph "A" <B>'
    trait["datasets"] = [{
        "title": "Study", "dataset_type": "GENOME", "repository": "Example archive",
        "accession": "DATASET:123", "url": "https://example.org/study",
    }]
    env = template_environment()
    html = env.get_template("trait.html").render(
        trait=trait, causal_graphs=graphs, kgm_match={"n_kgm_nodes": 0},
        parent_pages={}, parent_labels={},
    )
    parents = TableParents(html).tables
    assert len(parents) == 2
    assert [p.get("aria-label") for p in parents] == [
        'Graph "A" <B>: protein and taxon examples', "Datasets",
    ]
    for parent in parents:
        assert parent.get("role") == "region"
        assert parent.get("tabindex") == "0"
    example = graphs[0]["protein_example_rows"][0]
    for value in [example["uniprot_id"], example["taxon_id"], "DATASET:123"]:
        assert value in html
    accession = example["uniprot_id"].removeprefix("UniProtKB:")
    assert f'href="https://www.uniprot.org/uniprotkb/{accession}/entry"' in html
    assert 'href="https://example.org/study"' in html
