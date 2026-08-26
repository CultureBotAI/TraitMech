#!/usr/bin/env python3
"""Check `canonical_examples` taxon ids against NCBITaxon (#445).

`canonical_examples` is the slot that ties a trait to real organisms, which is
what makes this catalog usable from KG-Microbe. 226 records carry 315 of them and
nothing checked any of it: not that the CURIE is well formed, not that the id
exists, and not that the stored `taxon_label` still matches the ontology.

Label drift is the interesting case, because it is invisible and it is already
here: `morphology/heterocyst` stores `NCBITaxon:103690` as "Nostoc sp. PCC 7120"
while NCBITaxon now labels that node "Nostoc sp. PCC 7120 = FACHB-418". Neither
is wrong; they have simply diverged, and a curator comparing a record against
NCBI has no way to know which of the two they are looking at.

Defects:

  MALFORMED_TAXON_CURIE (ERROR)   Not `PREFIX:id`, or a non-numeric NCBITaxon id.
  MISSING_TAXON_ID (ERROR)        An example with no `taxon_id` at all.
  UNRESOLVED_TAXON (ERROR)        An NCBITaxon id the ontology does not know.
  TAXON_LABEL_DRIFT (WARN)        Stored label differs from the ontology label.
                                  WARN, not ERROR: NCBI relabels nodes for its
                                  own reasons (adding strain synonyms, as above),
                                  and a curator-chosen display label is not
                                  automatically wrong because upstream expanded
                                  it. Failing these would make every upstream
                                  rename a build break.

Deliberately NOT in `qc`, following `validate-products`: the default local
resolver needs the 13 GB OAK NCBITaxon build, which a bare CI runner will not
have. The dedicated canonical-example-taxonomy workflow uses `--ncbi-api` to
resolve the small set of exemplar ids directly against NCBI instead. Without a
resolver the id checks still run and resolution is reported as skipped, so the
recipe is useful offline rather than merely silent.
"""

from __future__ import annotations

import argparse
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections.abc import Sequence
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from audit_causal_graphs import Corpus, _as_corpus  # noqa: E402

DEFAULT_TRAITS = Path("data/traits")
CURIE = re.compile(r"^[A-Za-z][A-Za-z0-9_]*:[A-Za-z0-9_.\-]+$")
NCBITAXON = re.compile(r"^NCBITaxon:\d+$")
NCBI_TAXONOMY_EFETCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

ERRORS = {"MALFORMED_TAXON_CURIE", "MISSING_TAXON_ID", "UNRESOLVED_TAXON"}


class _LabelAdapter:
    """The tiny adapter surface `example_rows` needs."""

    def __init__(self, labels: dict[str, str]):
        self._labels = labels

    def label(self, curie: str) -> str | None:
        return self._labels.get(curie)


def _ncbitaxon_ids(corpus: Corpus) -> list[str]:
    return sorted({
        str(example.get("taxon_id"))
        for _rel, doc in corpus
        for example in (doc.get("canonical_examples") or [])
        if NCBITAXON.fullmatch(str(example.get("taxon_id") or ""))
    })


def _parse_ncbi_taxonomy(payload: bytes) -> dict[str, str]:
    """Return NCBITaxon CURIE -> current scientific name from EFetch XML."""
    root = ET.fromstring(payload)
    api_error = root.findtext(".//ERROR") or root.findtext(".//Error")
    if api_error:
        raise ValueError(f"NCBI EFetch error: {api_error}")
    labels: dict[str, str] = {}
    for taxon in root.findall(".//Taxon"):
        tax_id = taxon.findtext("TaxId")
        scientific_name = taxon.findtext("ScientificName")
        if tax_id and scientific_name:
            labels[f"NCBITaxon:{tax_id}"] = scientific_name
    if not labels:
        raise ValueError("NCBI EFetch returned no taxonomy records")
    return labels


def _ncbi_api_adapter(
    curies: Sequence[str], *, attempts: int = 3, timeout: float = 60.0
) -> _LabelAdapter:
    """Resolve a small CURIE set with one authoritative NCBI EFetch request.

    More than 200 ids should be sent by POST according to the E-utilities
    guidance. Retrying transient HTTP/network failures makes the scheduled gate
    useful without ever converting an unavailable service into a false clean
    result.
    """
    ids = [curie.removeprefix("NCBITaxon:") for curie in curies]
    if not ids:
        return _LabelAdapter({})
    body = urllib.parse.urlencode({
        "db": "taxonomy",
        "id": ",".join(ids),
        "retmode": "xml",
        "tool": "traitmech-canonical-example-audit",
    }).encode("ascii")
    request = urllib.request.Request(
        NCBI_TAXONOMY_EFETCH,
        data=body,
        headers={"User-Agent": "TraitMech canonical-example audit"},
        method="POST",
    )
    last_error: Exception | None = None
    for attempt in range(attempts):
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return _LabelAdapter(_parse_ncbi_taxonomy(response.read()))
        except (OSError, ET.ParseError, ValueError, urllib.error.HTTPError) as exc:
            last_error = exc
            if attempt + 1 < attempts:
                time.sleep(2**attempt)
    raise RuntimeError(
        f"NCBI taxonomy EFetch failed after {attempts} attempt(s): {last_error}"
    ) from last_error


def _adapter():
    """Return an NCBITaxon adapter, or None if it cannot be built.

    Returning None rather than raising keeps the id-shape checks useful on a
    machine with no ontology build, which is the common case in CI.
    """
    try:
        from oaklib import get_adapter

        adapter = get_adapter("sqlite:obo:ncbitaxon")
        adapter.label("NCBITaxon:2261")  # cheap probe; a partial build fails here
        return adapter
    except Exception:
        return None


def example_rows(
    source: Path | Corpus = DEFAULT_TRAITS, *, adapter=None, resolve: bool = True
) -> tuple[list[tuple[str, str, str]], dict[str, int]]:
    """Return (rows, counts) where each row is (file, defect, detail)."""
    # `resolve` is authoritative. Guarding only adapter CONSTRUCTION meant
    # resolve=False still resolved whenever a caller supplied an adapter, so the
    # flag did not do what its name says -- and a test asserting "resolution was
    # skipped" would have passed for the wrong reason (#451).
    if not resolve:
        adapter = None
    elif adapter is None:
        adapter = _adapter()
    rows: list[tuple[str, str, str]] = []
    counts = {"examples": 0, "records": 0, "resolved": 0, "resolution": 0}
    counts["resolution"] = 1 if adapter is not None else 0

    for rel, doc in _as_corpus(source):
        examples = doc.get("canonical_examples") or []
        if examples:
            counts["records"] += 1
        for ex in examples:
            counts["examples"] += 1
            tid = ex.get("taxon_id")
            label = ex.get("taxon_label")
            if not tid:
                rows.append((rel, "MISSING_TAXON_ID", f"{label or '<no label>'}"))
                continue
            if not CURIE.match(str(tid)):
                rows.append((rel, "MALFORMED_TAXON_CURIE", f"{tid} is not PREFIX:id"))
                continue
            if str(tid).startswith("NCBITaxon:") and not NCBITAXON.match(str(tid)):
                rows.append((rel, "MALFORMED_TAXON_CURIE", f"{tid} has a non-numeric id"))
                continue
            if adapter is None or not str(tid).startswith("NCBITaxon:"):
                continue
            actual = adapter.label(tid)
            if actual is None:
                rows.append((rel, "UNRESOLVED_TAXON", f"{tid} not found in NCBITaxon"))
                continue
            counts["resolved"] += 1
            if label and actual != label:
                rows.append(
                    (rel, "TAXON_LABEL_DRIFT", f"{tid} record={label!r} ncbitaxon={actual!r}")
                )
    return rows, counts


def main(argv: Sequence[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--traits-dir", type=Path, default=DEFAULT_TRAITS)
    resolution = ap.add_mutually_exclusive_group()
    resolution.add_argument(
        "--no-resolve", action="store_true", help="skip ontology lookups"
    )
    resolution.add_argument(
        "--ncbi-api",
        action="store_true",
        help="resolve NCBITaxon ids with one batched NCBI EFetch request",
    )
    args = ap.parse_args(argv)

    corpus = _as_corpus(args.traits_dir)
    if args.ncbi_api:
        try:
            adapter = _ncbi_api_adapter(_ncbitaxon_ids(corpus))
        except RuntimeError as exc:
            print(f"NCBITaxon resolution FAILED: {exc}", file=sys.stderr)
            return 2
        rows, counts = example_rows(corpus, adapter=adapter)
    else:
        rows, counts = example_rows(corpus, resolve=not args.no_resolve)
    for rel, defect, detail in rows:
        print(f"{defect}\t{rel}\t{detail}")

    errors = [r for r in rows if r[1] in ERRORS]
    warns = len(rows) - len(errors)
    print(
        f"\ncanonical_examples: {counts['examples']} example(s) across "
        f"{counts['records']} record(s); {len(errors)} error(s), {warns} warning(s)"
    )
    if counts["resolution"]:
        print(f"  resolved against NCBITaxon: {counts['resolved']}")
    else:
        # Say it, rather than reporting a clean run that checked half of what it
        # claims to check.
        print(
            "  NCBITaxon resolution SKIPPED (no usable ontology build) -- id shape "
            "was checked, existence and labels were not"
        )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
