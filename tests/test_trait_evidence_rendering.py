"""Citation visibility and escaping on the real detail-page template (#1623)."""

import sys
from html.parser import HTMLParser
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from render_trait_pages import reference_url, template_environment  # noqa: E402


class Page(HTMLParser):
    def __init__(self, html, evidence_only=False):
        super().__init__()
        self.tags = []
        self.text = []
        self.evidence_only = evidence_only
        self.in_evidence = False
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id") == "trait-evidence":
            self.in_evidence = True
        if not self.evidence_only or self.in_evidence:
            self.tags.append((tag, attrs))

    def handle_endtag(self, tag):
        if tag == "section":
            self.in_evidence = False

    def handle_data(self, data):
        if not self.evidence_only or self.in_evidence:
            self.text.append(data)


def render(trait, graphs=None):
    return template_environment().get_template("trait.html").render(
        trait={"label": "Test trait", "trait_category": "GENOMICS", **trait},
        causal_graphs=graphs or [], kgm_match={"n_kgm_nodes": 0},
        parent_pages={}, parent_labels={},
    )


VALID = [
    ("DOI:10.1073/pnas.2519643122", "https://doi.org/10.1073/pnas.2519643122"),
    ("doi:10.1002/(SICI)X;1#2?3%4", "https://doi.org/10.1002/(SICI)X;1%232%3F3%254"),
    ("PMID:41252147", "https://pubmed.ncbi.nlm.nih.gov/41252147/"),
    ("pmid:123", "https://pubmed.ncbi.nlm.nih.gov/123/"),
    ("https://example.org/data?a=1&b=2#source", "https://example.org/data?a=1&b=2#source"),
    ("http://example.org/data", "http://example.org/data"),
    ("HTTPS://example.org/data", "HTTPS://example.org/data"),
    ("https://[::1]:8080/data", "https://[::1]:8080/data"),
]


@pytest.mark.parametrize("reference,expected", VALID)
def test_citations_link_consistently_in_every_evidence_context(reference, expected):
    evidence = {"reference": reference, "snippet": "Exact source text", "notes": "Scope note"}
    trait = {
        "definition_source": reference, "evidence": [evidence],
        "canonical_examples": [{"reference": reference}],
        "discussions": [{"discussion_id": "gap", "evidence": [evidence]}],
    }
    graphs = [{
        "title": "Mechanism", "evidence_rows": [{"edge_id": "e1", "evidence": [evidence]}],
        "protein_example_rows": [{
            "uniprot_id": "UniProtKB:P0DW44", "taxon_id": "NCBITaxon:1761765",
            "evidence": [evidence],
        }],
    }]
    page = Page(render(trait, graphs))
    links = [attrs for tag, attrs in page.tags if tag == "a" and attrs.get("href") == expected]
    assert len(links) == 6
    assert all(attrs["rel"] == "nofollow noreferrer" for attrs in links)
    assert reference_url(reference) == expected


UNLINKED = [
    None, 42, "", "GO:0008150", "curator observation", "DOI:", "DOI:10.1/x",
    "DOI:10.1000/space here", "PMID:no-id", "PMID:123/other", "PMID:123?x=1",
    "javascript:alert(1)", "JaVaScRiPt:alert(1)", "data:text/html,<script>alert(1)</script>",
    "file:///tmp/source", "//example.org/path", "/relative/path", "https:",
    "https:///missing-host", "https://", "https://[bad", "https://example.org:bad",
    "https://example.org:99999", "https://user:password@example.org/",
    "https://good.example\\@evil.example/", "https://exa mple.org/",
    "https://example.org/\npath", "\tjavascript:alert(1)", "https://example.org/\x00x",
    'https://example.org/" onclick="alert(1)',
]


@pytest.mark.parametrize("reference", UNLINKED)
def test_unknown_or_unsafe_references_stay_unlinked(reference):
    assert reference_url(reference) is None
    page = Page(render({"evidence": [{"reference": reference}]}), evidence_only=True)
    assert not any(tag == "a" and attrs.get("href") == reference for tag, attrs in page.tags)
    assert not any(tag == "a" and attrs.get("href", "").lower().startswith(
        ("javascript:", "data:", "file:", "//")
    ) for tag, attrs in page.tags)
    if reference:
        assert str(reference) in "".join(page.text)


def test_graph_free_evidence_is_visible_and_html_is_escaped():
    reference = "UNKNOWN:<img src=x onerror=alert(1)>"
    snippet = '<script>alert("snippet")</script> & literal source'
    notes = '<img src=x onerror=alert("notes")> & scope'
    page = Page(render({"evidence": [{"reference": reference, "snippet": snippet, "notes": notes}]}),
                evidence_only=True)
    assert any(attrs.get("id") == "trait-evidence" for _, attrs in page.tags)
    assert any(tag == "blockquote" for tag, _ in page.tags)
    assert all(value in "".join(page.text) for value in [reference, snippet, notes])
    assert not any(tag in {"script", "img"} for tag, _ in page.tags)
    assert not any(any(key.startswith("on") for key in attrs) for _, attrs in page.tags)


@pytest.mark.parametrize("evidence", [None, []])
def test_empty_evidence_does_not_create_a_section(evidence):
    assert 'id="trait-evidence"' not in render({"evidence": evidence})
    assert 'id="trait-evidence"' not in render({})


def test_optional_fields_can_be_absent_without_undefined_or_none_labels():
    html = render({"evidence": [{"reference": "PMID:123"}, {"notes": "Unlinked note"}]})
    page = Page(html)
    assert "Unlinked note" in "".join(page.text)
    assert not any(tag == "blockquote" for tag, _ in page.tags)
    assert "Undefined" not in html and ">None<" not in html


@pytest.mark.parametrize("slug", ["lamassu_type_i_system", "lamassu_type_ii_system"])
def test_lamassu_regression_preserves_all_stored_evidence(slug):
    trait = yaml.safe_load((ROOT / f"data/traits/genomics/{slug}.yaml").read_text())
    page = Page(render(trait))
    text = "".join(page.text)
    links = {attrs.get("href") for tag, attrs in page.tags if tag == "a"}
    for evidence in trait["evidence"]:
        assert reference_url(evidence["reference"]) in links
        assert evidence["snippet"] in text
        if evidence.get("notes"):
            assert evidence["notes"] in text
