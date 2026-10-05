#!/usr/bin/env python3
"""Apply TraitMech navigation/theme to the shared discussions browser output.

Run after kg_microbe_discussions; leave its data payload and shared checkout
untouched. Anchors are checked so an upstream layout change fails explicitly.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
START = "<!-- TraitMech shell -->"
END = "<!-- /TraitMech shell -->"


def render_shell(text: str) -> str:
    text = re.sub(re.escape(START) + r".*?" + re.escape(END) + r"\n?", "", text, flags=re.S)
    if text.count("</head>") != 1 or text.count('<nav aria-label="Project navigation">') != 1:
        raise ValueError("Shared discussions template changed: check head/navigation anchors")
    head = (f'{START}\n<link rel="stylesheet" href="style.css">\n'
            '<script src="../../pages/theme-toggle.js"></script>\n'
            f'{END}\n')
    navigation = (f'{START}<a href="../../pages/index.html">TraitMech Home</a> · '
                  f'<a href="../../pages/browse.html">Browse</a> · {END}')
    return text.replace('</head>', head + '</head>').replace(
        '<nav aria-label="Project navigation">',
        '<nav aria-label="Project navigation">' + navigation,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=REPO_ROOT / 'app/discussions')
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    index = args.output / 'index.html'
    expected = render_shell(index.read_text())
    stylesheet = (REPO_ROOT / 'src/traitmech/templates/discussions.css').read_text()
    target_css = args.output / 'style.css'
    if args.check:
        if (index.read_text() != expected or not target_css.exists()
                or target_css.read_text() != stylesheet):
            print('Discussion navigation/theme is stale; run just gen-discussions-data')
            return 1
    else:
        index.write_text(expected)
        target_css.write_text(stylesheet)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
