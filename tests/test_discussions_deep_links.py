"""Every deep link the discussions index emits must resolve (#409).

Two independent things have to line up for a row in the corpus-wide index to
reach the gap it names, and both were broken:

  * the PATH -- `conf/discussions_config.yaml` built `../pages/...` relative to
    `app/discussions/index.html`, which is two levels below the repo root, so
    every link resolved to the non-existent `app/pages/...`;
  * the ANCHOR -- `trait.html` rendered each discussion in a `<div>` with no
    `id`, so even a correct path landed at the top of the page.

Neither shows up in any audit: the pages generate, the index generates, and the
links are simply dead. The test walks the generated artifacts the way a browser
would, which is the only way to catch a two-sided mismatch like this.
"""

from __future__ import annotations

import re
from pathlib import Path

INDEX_DIR = Path("app/discussions")
DATA_JS = INDEX_DIR / "data.js"


def _page_urls() -> list[str]:
    return re.findall(r'"page_url":\s*"([^"]+)"', DATA_JS.read_text())


def test_data_js_exists_and_has_rows():
    assert DATA_JS.exists(), "run `just gen-discussions-data`"
    assert _page_urls(), "the index carries no rows"


def test_every_deep_link_resolves_to_a_page_and_an_anchor():
    broken = []
    for url in _page_urls():
        path, _, fragment = url.partition("#")
        page = (INDEX_DIR / path).resolve()
        if not page.exists():
            broken.append(f"{url} -> no such page")
            continue
        if fragment and f'id="{fragment}"' not in page.read_text():
            broken.append(f"{url} -> page has no id={fragment}")
    assert not broken, "dead links from the discussions index: " + "; ".join(broken)


def test_links_are_relative_and_stay_inside_the_site():
    """Absolute or scheme-qualified links would break the static deployment."""
    for url in _page_urls():
        assert not url.startswith(("/", "http://", "https://")), url
