"""Local trait identifiers must not be presented as released METPO IDs (#1645)."""

import sys
from html.parser import HTMLParser
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from render_trait_pages import template_environment  # noqa: E402

YAML_URL = "https://github.com/CultureBotAI/TraitMech/blob/main/data/traits/physiology/test.yaml"


class IdentityPage(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.links = []
        self.identifier_links = []
        self.text = []
        self.footer = []
        self.in_footer = False
        self.in_identifier = False
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "dl" and "rail-meta" in attrs.get("class", "").split():
            self.in_identifier = True
        if tag == "a":
            self.links.append(attrs.get("href"))
            if self.in_identifier:
                self.identifier_links.append(attrs.get("href"))
        if tag == "footer":
            self.in_footer = True

    def handle_endtag(self, tag):
        if tag == "dl":
            self.in_identifier = False
        if tag == "footer":
            self.in_footer = False

    def handle_data(self, data):
        self.text.append(data)
        if self.in_footer:
            self.footer.append(data)


def render(identifier, status="PROPOSED"):
    return IdentityPage(template_environment().get_template("trait.html").render(
        trait={"identifier": identifier, "label": "Test", "trait_category": "PHYSIOLOGY",
               "mapping_status": status, "term_kind": "CLASS"},
        causal_graphs=[], kgm_match={"n_kgm_nodes": 0}, parent_pages={}, parent_labels={},
        yaml_blob_url=YAML_URL, metpo_version="2026-06-12", embedding_release="2026-04-25",
        generated_at="2026-10-04 00:17 UTC", stamp_scope="Record",
    ))


@pytest.mark.parametrize("status", ["PROPOSED", "REVIEWED", "SEEDED", "DEPRECATED"])
def test_local_identity_is_namespace_based_and_links_to_record(status):
    page = render("traitmech:000582", status)
    text = " ".join("".join(page.text).split())
    assert "TraitMech CURIE" in text
    assert "METPO CURIE" not in text
    assert "Identifier source TraitMech local identifier" in text
    assert page.identifier_links == [YAML_URL]
    assert not any(link and link.startswith("https://w3id.org/metpo/traitmech:")
                   for link in page.links)


@pytest.mark.parametrize("status", ["PROPOSED", "REVIEWED", "SEEDED", "DEPRECATED"])
def test_metpo_identity_keeps_authority_link_and_version(status):
    page = render("METPO:1000702", status)
    text = " ".join("".join(page.text).split())
    assert "METPO CURIE" in text
    assert page.identifier_links == ["https://w3id.org/metpo/1000702"]
    assert "Identifier source METPO (2026-06-12)" in text
    assert "TraitMech local identifier" not in text


@pytest.mark.parametrize("identifier", ["EXAMPLE:123", ""])
def test_unknown_or_missing_namespace_does_not_invent_an_authority(identifier):
    page = render(identifier)
    text = " ".join("".join(page.text).split())
    assert "Identifier source Record YAML" in text
    assert "METPO CURIE" not in text and "TraitMech CURIE" not in text
    assert page.identifier_links == []
    assert not any(link and link.startswith("https://w3id.org/metpo/")
                   for link in page.links)


@pytest.mark.parametrize("identifier", ["traitmech:000582", "METPO:1000702"])
def test_embedding_absence_and_footer_do_not_misstate_record_origin(identifier):
    page = render(identifier)
    text = " ".join("".join(page.text).split())
    footer = " ".join("".join(page.footer).split())
    assert "No kg-microbe node embedding matched this record" in text
    assert "Most unmatched terms are DatatypeProperties" not in text
    assert "Record as of 2026-10-04 00:17 UTC" in footer
    assert "Ontology baseline: METPO 2026-06-12" in footer
    assert "from METPO" not in footer
