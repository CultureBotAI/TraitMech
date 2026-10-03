from pathlib import Path
from html.parser import HTMLParser
import subprocess
import shutil
import pytest
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "src/traitmech/templates"


class Page(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.tags = []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))


@pytest.mark.parametrize("template", ["browse.html", "category.html"])
def test_catalogue_has_escaped_definitions_and_progressive_controls(template):
    env = Environment(loader=FileSystemLoader(TEMPLATES), autoescape=select_autoescape(["html"]))
    record = {
        "label": "Needle <script>",
        "definition": "Specific <biology> & detail",
        "identifier": "GO:123",
        "curie": "METPO:123",
        "page": "records/needle.html",
        "category": "TEST",
        "kind": "COMPLEX",
        "term_kind": "CLASS",
        "status": "PROPOSED",
        "synonyms": "alternate name",
        "synonyms_count": 1,
        "n_kgm_nodes": 0,
    }
    context = dict(
        root="../",
        records=[record],
        traits=[record],
        category={"name": "TEST", "blurb": "Example"},
        category_counts={"TEST": 1},
        embedding_per_category={},
        total_traits=1,
    )
    context["category"] = "TEST"
    html = env.get_template(template).render(**context)
    parsed = Page(html)
    assert "Specific &lt;biology&gt; &amp; detail" in html
    assert any(t == "form" and "hidden" in a for t, a in parsed.tags)
    assert any(
        t == "input" and a.get("type") == "search" and a.get("id") == "record-query"
        for t, a in parsed.tags
    )
    assert any(t == "label" and a.get("for") == "record-query" for t, a in parsed.tags)
    assert any(t == "button" and a.get("type") == "reset" for t, a in parsed.tags)
    assert any(a.get("role") == "status" and a.get("aria-live") == "polite" for _, a in parsed.tags)
    assert any(t == "a" and a.get("href") == "../records/needle.html" for t, a in parsed.tags)
    assert not any(t == "tr" and "hidden" in a for t, a in parsed.tags)
    assert "record-browser.js" in html


def test_filter_behavior_and_reset():
    node = shutil.which("node")
    if not node:
        pytest.skip("Node is required for browser behavior checks")
    script = r"""
const fs = require('fs'), vm = require('vm'), assert = require('assert');
const events = {}; const query = {value:''}; const category = {value:''}; const kind = {value:''};
const form = {hidden:true, addEventListener:(name, fn)=>events[name]=fn};
const count = {textContent:''}, empty = {hidden:true};
const rows = [
 {textContent:'Needle Specific biology METPO:123',
  dataset:{category:'TEST',kind:'CLASS',synonyms:'Alternate'},hidden:false},
 {textContent:'Other unrelated GO:456',dataset:{category:'OTHER',kind:'COMPLEX',synonyms:''},hidden:false}
];
const map = {'record-filters':form,'record-query':query,'record-category':category,
  'record-kind':kind,'record-count':count,'record-empty':empty};
const document = {getElementById:id=>map[id],querySelectorAll:()=>rows};
vm.runInNewContext(fs.readFileSync(process.argv[1], 'utf8'), {document, setTimeout:fn=>fn()});
assert.equal(form.hidden,false); assert.match(count.textContent,/2 of 2/);
query.value='BIOLOGY'; events.input(); assert.equal(rows[0].hidden,false); assert.equal(rows[1].hidden,true);
query.value='alternate'; events.input(); assert.equal(rows[0].hidden,false);
query.value='';category.value='OTHER';events.change();assert.equal(rows[0].hidden,true);assert.equal(rows[1].hidden,false);
kind.value='CLASS';events.change();assert.equal(empty.hidden,false);assert.match(count.textContent,/0 of 2/);
query.value='';category.value='';kind.value='';events.reset();assert.ok(rows.every(r=>!r.hidden));assert.equal(empty.hidden,true);
query.value='no-result';events.input();assert.equal(empty.hidden,false);
"""
    subprocess.run([node, "-e", script, str(TEMPLATES / "record-browser.js")], check=True)
