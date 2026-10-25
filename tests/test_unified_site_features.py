"""X-Mech unified website features on the TraitMech site (wave 1, 2026-10-25).

Covers the five features the 2026-10-25 review left partial: references in free
text are followable (evidence), displayed CURIEs resolve and own-record CURIEs
open their record page (term_links), readable schema documentation generated
from the schema (schema_docs), the licence footer on every page type (license),
and map plots that fit a phone (responsive). Each test is driven by an input on
which the old rendering and the new one differ.
"""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from render_discussions_shell import render_shell  # noqa: E402
from render_trait_pages import (  # noqa: E402
    autolink,
    curie_url,
    schema_reference,
    template_environment,
)

TEMPLATES = ROOT / "src" / "traitmech" / "templates"
GH = "https://github.com/CultureBotAI/TraitMech/blob/main"
LICENSE_LINKS = {f"{GH}/LICENSE-DATA", f"{GH}/LICENSE-CODE", f"{GH}/LICENSE"}
YAML_URL = f"{GH}/data/traits/ecology/example.yaml"


class Page(HTMLParser):
    """Anchors with their text, footer text and anchors, and visible text."""

    def __init__(self, html: str):
        super().__init__(convert_charrefs=True)
        self.anchors: list[tuple[dict, str]] = []
        self.footer_links: list[str] = []
        self.footer_text: list[str] = []
        self.text: list[str] = []
        self.ids: set[str] = set()
        self.tags: list[str] = []
        self._open: list[tuple[dict, list[str]]] = []
        self._footer = 0
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append(tag)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "footer":
            self._footer += 1
        if tag == "a":
            self._open.append((attrs, []))
            if self._footer:
                self.footer_links.append(attrs.get("href", ""))

    def handle_endtag(self, tag):
        if tag == "a" and self._open:
            attrs, text = self._open.pop()
            self.anchors.append((attrs, " ".join("".join(text).split())))
        if tag == "footer":
            self._footer -= 1

    def handle_data(self, data):
        self.text.append(data)
        for _, text in self._open:
            text.append(data)
        if self._footer:
            self.footer_text.append(data)

    def hrefs(self) -> list[str]:
        return [attrs.get("href", "") for attrs, _ in self.anchors]

    def anchor(self, href: str) -> tuple[dict, str]:
        matches = [(attrs, text) for attrs, text in self.anchors if attrs.get("href") == href]
        assert matches, f"no anchor to {href}"
        return matches[0]

    def plain_text(self) -> str:
        return " ".join("".join(self.text).split())

    def footer(self) -> str:
        return " ".join("".join(self.footer_text).split())


def render_trait(trait: dict, graphs=None, **context) -> Page:
    values = {
        "causal_graphs": graphs or [], "kgm_match": {"n_kgm_nodes": 0},
        "parent_pages": {}, "parent_labels": {}, "root": "../../",
        "yaml_blob_url": YAML_URL, **context,
    }
    return Page(template_environment().get_template("trait.html").render(
        trait={"label": "Example", "trait_category": "ECOLOGY", **trait}, **values,
    ))


# ---------------------------------------------------------------- evidence --

LINKED_TOKENS = [
    ("See PMID:40891913.", "https://pubmed.ncbi.nlm.nih.gov/40891913/", "PMID:40891913"),
    ("from PMID 12345;", "https://pubmed.ncbi.nlm.nih.gov/12345/", "PMID 12345"),
    ("full text PMC2983100.", "https://pmc.ncbi.nlm.nih.gov/articles/PMC2983100/", "PMC2983100"),
    ("(DOI:10.1128/mBio.00390-21).", "https://doi.org/10.1128/mBio.00390-21",
     "DOI:10.1128/mBio.00390-21"),
    ("cited as doi 10.3389/fmicb.2021.705326, here", "https://doi.org/10.3389/fmicb.2021.705326",
     "doi 10.3389/fmicb.2021.705326"),
    ("quote :ref{doi=10.1101/2023.03.28.534373} end", "https://doi.org/10.1101/2023.03.28.534373",
     "doi=10.1101/2023.03.28.534373"),
    ("bare 10.1371/journal.pbio.3002726.s002) here", "https://doi.org/10.1371/journal.pbio.3002726.s002",
     "10.1371/journal.pbio.3002726.s002"),
    ("pdf at https://example.org/a/Leveau2008.pdf.", "https://example.org/a/Leveau2008.pdf",
     "https://example.org/a/Leveau2008.pdf"),
    ("(https://en.wikipedia.org/wiki/Foo_(bar))", "https://en.wikipedia.org/wiki/Foo_(bar)",
     "https://en.wikipedia.org/wiki/Foo_(bar)"),
    ("q https://example.org/?a=1&b=2 end", "https://example.org/?a=1&b=2", "https://example.org/?a=1&b=2"),
]


@pytest.mark.parametrize("text,href,label", LINKED_TOKENS)
def test_autolink_links_reference_tokens_and_keeps_surrounding_text(text, href, label):
    page = Page(str(autolink(text)))
    attrs, anchor_text = page.anchor(href)
    assert anchor_text == label
    assert attrs["rel"] == "nofollow noreferrer"
    # The text a reader sees is unchanged: only the token became an anchor.
    assert page.plain_text() == " ".join(text.split())


UNLINKED_TEXT = [
    "javascript:alert(1)", "data:text/html,<b>x</b>", "https://user:pw@evil.example/",
    "https://", "version v10.1234/abc", "PMID:not-a-number", "see doi.org/10.1038/x",
    "ftp://example.org/file", "PMC12 is too short",
]


@pytest.mark.parametrize("text", UNLINKED_TEXT)
def test_autolink_leaves_unsafe_or_non_reference_text_unlinked(text):
    page = Page(str(autolink(text)))
    assert page.anchors == []
    assert page.plain_text() == " ".join(text.split())


def test_autolink_escapes_markup_and_cannot_break_out_of_the_attribute():
    html = str(autolink('<script>alert(1)</script> https://example.org/x" onclick="alert(2) &'))
    page = Page(html)
    assert "script" not in page.tags
    assert page.hrefs() == ["https://example.org/x"]
    assert not any(key.startswith("on") for attrs, _ in page.anchors for key in attrs)
    assert "<script>alert(1)</script>" in page.plain_text()
    assert autolink(None) == "" and str(autolink(42)) == "42"


def test_free_text_references_link_in_every_record_context():
    """Each surface the 2026-10-25 review found carrying plain-text references."""
    trait = {
        "synonyms": [{"synonym_text": "biofilm-forming", "synonym_type": "RELATED_SYNONYM",
                      "source": "DOI:10.1038/nrmicro.2016.94"}],
        "evidence": [{"reference": "PMID:1", "snippet": "verbatim https://example.org/snippet",
                      "notes": "Full text PMC2983100."}],
        "curation_history": [{"timestamp": "2026-10-01T00:00:00Z", "action": "UPDATE",
                              "changes": "Added PMID:40891913 as support."}],
        "canonical_examples": [{"taxon_label": "Bacillus subtilis", "taxon_id": "NCBITaxon:1423",
                                "note": "See DOI:10.1128/AEM.02483-09."}],
        "discussions": [{"discussion_id": "gap-1", "prompt": "Why?",
                         "rationale": "Raised by doi:10.1093/ismejo/wrag201",
                         "notes": "Scan sentence from PMID:42039744."}],
    }
    graphs = [{"title": "Mechanism", "description": "After :ref{doi=10.1101/2023.03.28.534373}",
               "evidence_rows": [{"edge_id": "edge-1", "source": "a", "target": "b",
                                  "description": "See https://example.org/edge",
                                  "evidence": [{"reference": "PMID:2",
                                                "notes": "PMID 777 discusses it"}]}]}]
    page = render_trait(trait, graphs, curation_sessions=[{
        "session": {"timestamp": "2026-10-02T00:00:00Z", "actors": [{"name": "codex"}]},
        "events": [{"type": "UPDATE", "summary": "Checked https://example.org/session",
                    "details": "Compared with PMID:31"}],
        "source_url": f"{GH}/history/records/x/y.yaml"}])
    hrefs = set(page.hrefs())
    for expected in [
        "https://doi.org/10.1038/nrmicro.2016.94",        # synonym source
        "https://example.org/snippet",                    # evidence snippet
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC2983100/",  # evidence notes
        "https://pubmed.ncbi.nlm.nih.gov/40891913/",      # curation history
        "https://doi.org/10.1128/AEM.02483-09",           # canonical example note
        "https://doi.org/10.1093/ismejo/wrag201",         # discussion rationale
        "https://pubmed.ncbi.nlm.nih.gov/42039744/",      # discussion provenance
        "https://doi.org/10.1101/2023.03.28.534373",      # graph description directive
        "https://example.org/edge",                       # edge description
        "https://pubmed.ncbi.nlm.nih.gov/777/",           # edge evidence notes
        "https://example.org/session",                    # session summary
        "https://pubmed.ncbi.nlm.nih.gov/31/",            # session details
    ]:
        assert expected in hrefs, expected


def test_real_synonym_source_from_the_review_is_linked():
    trait = yaml.safe_load((ROOT / "data/traits/ecology/biofilm_formation.yaml").read_text())
    sources = [s["source"] for s in trait["synonyms"] if str(s.get("source", "")).startswith("DOI:")]
    assert "DOI:10.1038/nrmicro.2016.94" in sources
    html = template_environment().get_template("trait.html").render(
        trait=trait, causal_graphs=[], kgm_match={"n_kgm_nodes": 0},
        parent_pages={}, parent_labels={}, root="../../")
    # The same DOI is also cited elsewhere on this page, so look inside the card.
    synonyms = Page(re.search(r'<ul class="synonyms">.*?</ul>', html, re.S).group(0))
    assert synonyms.anchor("https://doi.org/10.1038/nrmicro.2016.94")[1] == "DOI:10.1038/nrmicro.2016.94"


# -------------------------------------------------------------- term_links --

@pytest.mark.parametrize("curie,expected", [
    ("MICRO:0000001", "http://purl.obolibrary.org/obo/MICRO_0000001"),
    ("rdfs:subClassOf", "http://www.w3.org/2000/01/rdf-schema#subClassOf"),
    ("GO:0008150", "https://amigo.geneontology.org/amigo/term/GO:0008150"),
    ("NCIT:C12345", "https://bioregistry.io/NCIT:C12345"),
    ("traitmech:000123", None),
    ("not a curie", None),
    ("X:<y>", None),
    ("", None),
])
def test_curie_resolver_map_with_registry_fallback(curie, expected):
    assert curie_url(curie) == expected


def graph_with_groundings(*groundings):
    rows = [{"edge_id": f"edge-{i}", "source": f"node {i}", "source_grounding": grounding,
             "target": "trait", "target_grounding": None, "predicate": "affects",
             "predicate_id": "rdfs:subClassOf", "evidence": []}
            for i, grounding in enumerate(groundings, start=1)]
    return [{"title": "Mechanism", "evidence_rows": rows}]


def test_own_record_groundings_open_their_record_page():
    page_path = {"traitmech:000700": "traits/metabolism/other.html",
                 "METPO:1000059": "traits/upper/phenotype.html",
                 "traitmech:000001": "traits/ecology/example.html"}
    page = render_trait(
        {"identifier": "traitmech:000001"},
        graph_with_groundings("traitmech:000700", "METPO:1000059", "traitmech:000001",
                              "CHEBI:15377", "traitmech:999999", "NCIT:C1"),
        page_path=page_path)
    hrefs = page.hrefs()
    assert "../../traits/metabolism/other.html" in hrefs
    assert "../../traits/upper/phenotype.html" in hrefs
    # The page's own identifier resolves like its Identifier card, not to itself.
    assert "../../traits/ecology/example.html" not in hrefs
    assert YAML_URL in hrefs
    assert "https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:15377" in hrefs
    assert "https://bioregistry.io/NCIT:C1" in hrefs
    assert "http://www.w3.org/2000/01/rdf-schema#subClassOf" in hrefs
    # A local id with no record page stays visible but is not linked anywhere.
    assert "traitmech:999999" in page.plain_text()
    assert not any("999999" in href for href in hrefs)
    assert "#" not in hrefs


def test_kg_microbe_nodes_show_the_label_and_link_the_record():
    page = render_trait(
        {"identifier": "traitmech:000626"},
        kgm_match={"n_kgm_nodes": 1, "kgm_nodes": ["METPO:1000059"], "match_method": "parent_proxy"},
        parent_labels={"METPO:1000059": "phenotype"},
        page_path={"METPO:1000059": "traits/upper/phenotype.html"},
        node_dim_preview={})
    assert page.anchor("../../traits/upper/phenotype.html")[1] == "phenotype METPO:1000059"


def test_direct_metpo_node_resolves_to_the_authority_not_a_self_link():
    page = render_trait(
        {"identifier": "METPO:1004002"},
        kgm_match={"n_kgm_nodes": 1, "kgm_nodes": ["METPO:1004002"], "match_method": "direct_metpo"},
        parent_labels={"METPO:1004002": "animal pathogen"},
        page_path={"METPO:1004002": "traits/ecology/example.html"}, node_dim_preview={})
    assert page.anchor("https://w3id.org/metpo/1004002")[1] == "animal pathogen METPO:1004002"
    assert "../../traits/ecology/example.html" not in page.hrefs()


def test_cross_references_use_the_resolver_map():
    page = render_trait({"xrefs": ["MICRO:0000123", "GO:0009060"]})
    assert "http://purl.obolibrary.org/obo/MICRO_0000123" in page.hrefs()
    assert "https://amigo.geneontology.org/amigo/term/GO:0009060" in page.hrefs()


# ------------------------------------------------------------- schema_docs --

def test_schema_reference_documents_every_class_slot_and_enum():
    from linkml_runtime.utils.schemaview import SchemaView

    view = SchemaView(str(ROOT / "src/traitmech/schema/traitmech.yaml"))
    reference = schema_reference()
    assert [c["name"] for c in reference["classes"]][0] == "TraitRecord"
    assert {c["name"] for c in reference["classes"]} == set(view.all_classes())
    assert {e["name"] for e in reference["enums"]} == set(view.all_enums())
    record = next(c for c in reference["classes"] if c["name"] == "TraitRecord")
    induced = [slot.name for slot in view.class_induced_slots("TraitRecord")]
    assert [slot["name"] for slot in record["slots"]] == induced
    # Slots docs/SCHEMA.md never listed, so a hand-written page would be stale.
    for name in ("causal_graphs", "canonical_examples", "discussions", "datasets"):
        assert name in induced
    slots = {slot["name"]: slot for slot in record["slots"]}
    assert slots["identifier"]["required"] and slots["identifier"]["identifier"]
    assert slots["causal_graphs"]["multivalued"]
    assert slots["causal_graphs"]["ranges"] == [{"name": "CausalGraph", "kind": "class"}]
    status = next(e for e in reference["enums"] if e["name"] == "MappingStatusEnum")
    assert {"SEEDED", "PROPOSED", "REVIEWED", "DEPRECATED"} <= {v["text"] for v in status["permissible"]}


def render_schema_page() -> str:
    return template_environment().get_template("schema.html").render(
        title="LinkML schema", root="", schema=schema_reference(), gh_blob_base=GH,
        metpo_version="2026-06-12", generated_at="2026-10-25 00:00 UTC", total_traits=1,
        embedding_coverage_pct="100.0")


def test_schema_page_anchors_resolve_and_render_is_deterministic():
    html = render_schema_page()
    assert html == render_schema_page()
    page = Page(html)
    assert {"class-TraitRecord", "class-CausalGraph", "enum-MappingStatusEnum"} <= page.ids
    internal = [href[1:] for href in page.hrefs() if href.startswith("#")]
    assert internal and set(internal) <= page.ids
    assert f"{GH}/src/traitmech/schema/traitmech.yaml" in page.hrefs()
    assert "BSD-3-Clause" in page.anchor(f"{GH}/LICENSE-CODE")[1]
    # Schema prose cites format examples ("e.g. PMID:12345678"); they are not references.
    assert "PMID:12345678" in page.plain_text()
    assert not any("pubmed.ncbi.nlm.nih.gov" in href for href in page.hrefs())


@pytest.mark.parametrize("template,root", [
    ("index.html", ""), ("browse.html", ""), ("schema.html", ""), ("map.html", ""),
    ("trait.html", "../../"), ("category.html", "../"),
])
def test_schema_link_is_visible_from_every_page_type(template, root):
    html = template_environment().get_template(template).render(**page_context(template, root))
    nav = Page(re.search(r"<nav.*?</nav>", html, re.S).group(0))
    assert nav.anchor(f"{root}schema.html")[1] == "Schema"
    assert f"{root}schema.html" in Page(html).footer_links


# ----------------------------------------------------------------- license --

def page_context(template: str, root: str) -> dict:
    context = {"root": root, "title": "T", "total_traits": 1, "metpo_version": "2026-06-12",
               "generated_at": "2026-10-25 00:00 UTC", "embedding_coverage_pct": "100.0",
               "category_counts": {"ECOLOGY": 1}, "embedding_per_category": {}, "traits": [],
               "category": "ECOLOGY", "n_points": 0, "data_url": "data/x.json",
               "href_by_id": "{}", "graph_edges": "[]", "n_edges": 0}
    if template == "trait.html":
        context.update(trait={"label": "Example", "trait_category": "ECOLOGY"}, causal_graphs=[],
                       kgm_match={"n_kgm_nodes": 0}, parent_pages={}, parent_labels={})
    if template == "schema.html":
        context.update(schema=schema_reference(), gh_blob_base=GH)
    return context


PAGE_TYPES = [("index.html", ""), ("browse.html", ""), ("category.html", "../"),
              ("trait.html", "../../"), ("map.html", ""), ("sequence-map.html", ""),
              ("umap.html", ""), ("graph.html", ""), ("schema.html", "")]


@pytest.mark.parametrize("template,root", PAGE_TYPES)
def test_every_page_type_footer_states_the_repository_licences(template, root):
    page = Page(template_environment().get_template(template).render(**page_context(template, root)))
    assert LICENSE_LINKS <= set(page.footer_links)
    footer = page.footer()
    assert "Project data: CC BY 4.0." in footer
    assert "Code: BSD-3-Clause." in footer
    assert "Third-party source material keeps its own terms (licence scope)." in footer


def test_footer_licences_match_the_licence_files():
    scope = (ROOT / "LICENSE").read_text()
    assert "Creative Commons Attribution 4.0" in scope and "CC-BY-4.0" in scope
    assert "BSD-3-Clause" in scope and "retain their own licenses" in scope
    assert (ROOT / "LICENSE-DATA").read_text().startswith("Attribution 4.0 International")
    assert (ROOT / "LICENSE-CODE").read_text().startswith("BSD 3-Clause License")


RAW_DISCUSSIONS = ('<html><head></head><body><nav aria-label="Project navigation">'
                   '<a href="https://culturebotai.github.io/mechs/">All Mech projects</a>'
                   '</nav><main id="main-content">Content</main><script src="data.js"></script>'
                   '</body></html>')


def test_discussions_index_carries_the_licence_footer_once():
    result = render_shell(RAW_DISCUSSIONS)
    assert render_shell(result) == result
    page = Page(result)
    assert LICENSE_LINKS <= set(page.footer_links)
    assert result.count('class="shell-footer"') == 1
    assert "Third-party source material keeps its own terms" in page.footer()
    with pytest.raises(ValueError, match="template changed"):
        render_shell(RAW_DISCUSSIONS.replace("</body>", ""))


def test_committed_discussions_index_is_current_with_the_shell():
    index = (ROOT / "app/discussions/index.html").read_text()
    assert render_shell(index) == index
    assert LICENSE_LINKS <= set(Page(index).footer_links)


# -------------------------------------------------------------- responsive --

MAP_TEMPLATES = ["map.html", "sequence-map.html", "umap.html", "graph.html"]


@pytest.mark.parametrize("template", MAP_TEMPLATES)
def test_map_plot_scales_to_its_container(template):
    """A fixed-width SVG overflowed a 390 px viewport to 553 px (2026-10-25 review)."""
    source = (TEMPLATES / template).read_text()
    chain = re.search(r'append\("svg"\)(.*?);', source, re.S)
    assert chain, "plot SVG creation not found"
    assert '.attr("viewBox", "0 0 " + W + " " + H)' in chain.group(1)
    assert '.style("width", "100%")' in chain.group(1)
    assert '.style("height", "auto")' in chain.group(1)


def test_facet_sidebar_is_not_pinned_over_content_on_narrow_screens():
    """Stacked above the table or plot at 390 px, a sticky sidebar covered it while scrolling."""
    css = (TEMPLATES / "style.css").read_text()
    base = css.index(".facet-sidebar {\n  position: sticky;")
    override = re.search(r"@media \(max-width: 860px\) \{\s*\.facet-sidebar \{ position: static;", css)
    # Equal specificity, so the override only wins if it comes after the base rule.
    assert override and override.start() > base


@pytest.mark.parametrize("template", MAP_TEMPLATES)
def test_map_data_table_scrolls_in_a_named_focusable_region(template):
    html = template_environment().get_template(template).render(**page_context(template, ""))
    match = re.search(r'<div class="data-table-scroll"([^>]*)>', html)
    assert match
    attrs = match.group(1)
    assert 'role="region"' in attrs and 'tabindex="0"' in attrs and 'aria-label="' in attrs
