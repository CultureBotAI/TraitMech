"""Unit tests for the malformed-CURIE scan in scripts/run_trait_graph_audit.py.

The scan exists because the sweep produced double-prefixed CURIEs twice, and the
second time the manual grep for them raced a report still being generated. It is
wired into `--verify` and therefore into `just qc`, where it currently reports
zero hits across all 354 tracked artifacts (707 before #388 dropped the
citation sidecars).

A gate whose corpus is already clean is exactly the kind that can be silently
broken — a mistyped pattern would keep reporting zero forever. These tests are
what distinguishes "found nothing" from "cannot find anything".
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from run_trait_graph_audit import (  # noqa: E402
    MANIFEST,
    MIN_ARTIFACT_BYTES,
    RESEARCH_DIR,
    audit_pilot_artifacts,
    hand_supplied,
    is_pipeline_report,
    missing_artifacts,
    ok_outputs,
    orphan_reports,
    output_path,
    preflight_error,
    report_done,
    scan_malformed_curies,
    undersized_artifacts,
)


def _scan(tmp_path: Path, text: str):
    path = tmp_path / "report.md"
    path.write_text(text)
    return scan_malformed_curies([path])


@pytest.mark.parametrize("line,expected", [
    # The shape that actually shipped: the template hands the provider an
    # already-prefixed identifier and asks it to quote it verbatim; it prefixed
    # it again. Seen for METPO, and reachable for any ontology.
    ("| phenotype | `METPO:METPO:1000059` |", "double prefix"),
    ("grounded to GO:GO:0009860 where applicable", "double prefix"),
    ("see chebi:chebi:15378 for the proton", "double prefix"),
    # CURIE prefixes are case-sensitive; nothing downstream normalises them.
    ("candidate grounding go:0009860", "lowercase prefix"),
    ("candidate grounding Chebi:15378", "lowercase prefix"),
    # The OBO underscore form used where a CURIE was expected.
    ("candidate grounding GO_0009860", "underscore form"),
    # Short local ids. The corpus carries 65 of these across 42 files, so a
    # four-digit floor would have made the gate blind to the malformed forms of
    # the taxon ids the reports use most (#251).
    ("organism ncbitaxon:562", "lowercase prefix"),
    ("organism NCBITaxon_562", "underscore form"),
    ("organism ncbitaxon:2", "lowercase prefix"),
    ("chemical CHEBI_422", "underscore form"),
])
def test_malformed_shapes_are_caught(tmp_path, line, expected):
    hits = _scan(tmp_path, line)
    # A string can be wrong in more than one way at once — `chebi:chebi:15378`
    # is both double-prefixed and lowercased — so this asserts the shape is
    # named, not that it is named exactly once.
    assert expected in [name for _, _, name, _ in hits], hits
    assert all(line_no == 1 for _, line_no, _, _ in hits)


@pytest.mark.parametrize("line", [
    # Correctly-cased CURIEs, which the case-insensitive lowercase pattern must
    # match internally and then discard.
    "| infection thread | `GO:0009860` | canonical entry route |",
    "CHEBI:15378 is the proton; ENVO:01000992 the environment",
    "METPO:1000059 and NCBITaxon:562 and PATO:0000384",
    # The underscore form is legitimate inside a real PURL — the pattern's
    # negative lookbehind has to spare this one.
    "http://purl.obolibrary.org/obo/GO_0009860",
    "see <http://purl.obolibrary.org/obo/CHEBI_15378>",
    # Prose colons that are not CURIEs at all.
    "Note: note: this is a repeated word, not a prefix, and has no id",
    # Short local ids are real (NCBITaxon:562), so the patterns carry no digit
    # floor. What keeps prose out is the prefix list, not the digit count:
    # neither of these has an ontology prefix, at any length.
    "see step 3_2024 and section 4:17 for the assay",
    # Correctly-cased short CURIEs stay clean, same as the long ones.
    "NCBITaxon:562 and NCBITaxon:2 and CHEBI:422",
])
def test_well_formed_content_is_not_flagged(tmp_path, line):
    assert _scan(tmp_path, line) == []


def test_reports_path_and_line_number(tmp_path):
    hits = _scan(tmp_path, "clean line\nanother clean line\nbad METPO:METPO:1000059 here\n")
    assert len(hits) == 1
    path, line_no, name, text = hits[0]
    assert path == tmp_path / "report.md"
    assert line_no == 3
    assert name == "double prefix"
    assert text.startswith("METPO:METPO:")


def test_the_tracked_corpus_is_clean():
    """The invariant #241 asserted in prose, asserted from the tree instead."""
    artifacts = sorted((REPO_ROOT / "research" / "traits").rglob("*.md"))
    assert artifacts, "no research artifacts found — research/ should be tracked"
    hits = scan_malformed_curies(artifacts)
    assert hits == [], f"malformed CURIEs in tracked artifacts: {hits[:5]}"


# ------------------------------------------------ artifact integrity (#244)
#
# Same argument as the CURIE scan above: these gates report zero on a clean
# corpus, so without tests "found nothing" and "cannot find anything" look
# identical. Each one below is made to FIRE.


def _manifest(tmp_path: Path, rows: list[tuple[str, str, str]]) -> Path:
    path = tmp_path / "manifest.tsv"
    lines = ["run_id\tcategory\tslug\tstatus\toutput"]
    for run_id, status, out in rows:
        lines.append(f"{run_id}\tcat\tslug\t{status}\t{out}")
    path.write_text("\n".join(lines) + "\n")
    return path


def test_ok_outputs_keeps_one_entry_per_artifact(tmp_path):
    m = _manifest(tmp_path, [
        ("r1", "ok", "research/a.md"),
        ("r2", "ok", "research/a.md"),      # the re-run
        ("r3", "error", "research/b.md"),   # not ok
    ])
    recorded = ok_outputs(m)
    assert recorded == {"research/a.md": "r1"}


def test_missing_artifact_is_reported_once_not_per_row(tmp_path):
    m = _manifest(tmp_path, [("r1", "ok", "gone.md"), ("r2", "ok", "gone.md")])
    assert missing_artifacts(ok_outputs(m), tmp_path) == [("r1", "gone.md")]


def test_zero_byte_artifact_is_caught_though_it_exists(tmp_path):
    """`.exists()` passes for a truncated write; that is the whole point."""
    (tmp_path / "empty.md").write_text("")
    m = _manifest(tmp_path, [("r1", "ok", "empty.md")])
    found = undersized_artifacts(ok_outputs(m), tmp_path)
    assert found == [("r1", "empty.md", 0)]


def test_a_real_sized_artifact_passes(tmp_path):
    (tmp_path / "full.md").write_text("x" * (MIN_ARTIFACT_BYTES + 1))
    m = _manifest(tmp_path, [("r1", "ok", "full.md")])
    assert undersized_artifacts(ok_outputs(m), tmp_path) == []


def test_floor_is_far_below_the_smallest_real_report():
    """Set from the corpus, not guessed: the smallest real report is 20,785
    bytes, so the floor must leave room rather than track it."""
    assert MIN_ARTIFACT_BYTES < 20_785 / 10


def test_report_with_no_ok_row_is_an_orphan(tmp_path):
    research = tmp_path / "research" / "traits" / "ecology"
    research.mkdir(parents=True)
    (research / "stray-deep-research-falcon.md").write_text("x")
    recorded = {"research/traits/ecology/known-deep-research-falcon.md": "r1"}
    found = orphan_reports(tmp_path / "research" / "traits", tmp_path, recorded)
    assert found == ["research/traits/ecology/stray-deep-research-falcon.md"]


def test_other_providers_are_outside_the_resume_namespace(tmp_path):
    """The gate must match its own invariant. Resume keys on
    `{slug}-deep-research-{default provider}.md`, so a report from another
    provider cannot suppress a call — and blocking on one would turn qc red on
    the documented `--provider openai` and `research-trait-edison` paths, fixable
    only by adding a filename to a constant (#396 review)."""
    research = tmp_path / "research" / "traits" / "metabolism"
    research.mkdir(parents=True)
    for name in ("cellulolysis-deep-research-codex.md",
                 "cellulolysis-deep-research-openai.md",
                 "cellulolysis-edison-literature.md"):
        (research / name).write_text("x")
    assert orphan_reports(tmp_path / "research" / "traits", tmp_path, {}) == []


def test_dry_run_meta_yaml_is_not_counted_as_a_report(tmp_path):
    """A --dry-run writes <stem>-meta.yaml with status: dry-run, cost: None and
    task_id: None (#246). Counting it would let a plan nobody paid for satisfy
    an existence check."""
    research = tmp_path / "research" / "traits" / "environment"
    research.mkdir(parents=True)
    (research / "psychrotolerant-edison-literature-meta.yaml").write_text("status: dry-run\n")
    assert orphan_reports(tmp_path / "research" / "traits", tmp_path, {}) == []


# ------------------------------------------ dry-run pilot provenance (#525)


def _pilot(tmp_path: Path, targets=("metabolism/example",)) -> tuple[Path, Path]:
    research = tmp_path / "research"
    research.mkdir()
    manifest = research / "2026-08-23-protein-taxon-pilot.json"
    manifest.write_text(json.dumps(list(targets)), encoding="utf-8")

    query = "offline pilot query"
    meta_path = (
        research
        / "traits"
        / "metabolism"
        / "example-edison-literature-protein-taxon-pilot-meta.yaml"
    )
    meta_path.parent.mkdir(parents=True)
    meta_path.write_text(
        yaml.safe_dump(
            {
                "slug": "example",
                "trait_category": "metabolism",
                "trait_path": "data/traits/metabolism/example.yaml",
                "job": "LITERATURE",
                "label": "protein-taxon-pilot",
                "template_path": "templates/trait_protein_taxon_research.md",
                "query": query,
                "submitted_at": "2026-08-23T00:00:00+00:00",
                "status": "dry-run",
                "query_sha256": hashlib.sha256(query.encode()).hexdigest(),
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    return research, meta_path


def test_pilot_manifest_and_dry_run_sidecar_are_checked_together(tmp_path):
    research, _ = _pilot(tmp_path)
    errors, manifests, sidecars = audit_pilot_artifacts(research)

    assert errors == []
    assert (manifests, sidecars) == (1, 1)


def test_pilot_manifest_missing_and_undeclared_sidecars_are_errors(tmp_path):
    research, meta = _pilot(tmp_path, targets=("metabolism/missing",))

    errors, _, _ = audit_pilot_artifacts(research)

    assert any("has 0 matching meta sidecars" in error for error in errors)
    assert any(f"undeclared meta sidecar {meta}" in error for error in errors)


def test_pilot_sidecar_hash_and_no_cost_claim_are_enforced(tmp_path):
    research, meta_path = _pilot(tmp_path)
    meta = yaml.safe_load(meta_path.read_text(encoding="utf-8"))
    meta["query_sha256"] = "0" * 64
    meta["total_cost"] = 1.25
    meta_path.write_text(yaml.safe_dump(meta, sort_keys=False), encoding="utf-8")

    errors, _, _ = audit_pilot_artifacts(research)

    assert any("query_sha256 does not match query" in error for error in errors)
    assert any("dry-run unexpectedly has total_cost" in error for error in errors)


def test_tracked_pilot_manifest_and_all_ten_sidecars_are_clean():
    errors, manifests, sidecars = audit_pilot_artifacts(REPO_ROOT / "research")

    assert errors == []
    assert (manifests, sidecars) == (1, 10)


# ------------------------------------------ the rosalind namespace and preflight


def test_rosalind_reports_have_their_own_resume_namespace():
    assert output_path("ecology", "gut_associated", "rosalind").name == (
        "gut_associated-deep-research-rosalind.md"
    )
    assert output_path("ecology", "gut_associated", "gpt-rosalind").name == (
        "gut_associated-deep-research-rosalind.md"
    )


def test_a_hand_supplied_report_is_neither_done_nor_pending(tmp_path):
    """`pipeline_run: false` marks a pasted-in artifact. It must not suppress a
    call the pipeline never made -- and must not be queued for one either,
    since that would overwrite it (#638)."""
    path = tmp_path / "x-deep-research-rosalind.md"
    path.write_text("---\nprovider: gpt-rosalind\npipeline_run: false\n---\n\n# body\n" + "x" * 5000)
    assert not is_pipeline_report(path)
    assert not report_done(path)
    assert hand_supplied(path)


def test_a_pipeline_report_is_done_for_resume(tmp_path):
    path = tmp_path / "x-deep-research-rosalind.md"
    path.write_text("---\nprovider: openai\nmodel: gpt-rosalind\n---\n\n# body\n")
    assert is_pipeline_report(path)
    assert report_done(path)
    assert not hand_supplied(path)
    assert not report_done(tmp_path / "absent-deep-research-rosalind.md")
    assert not hand_supplied(tmp_path / "absent-deep-research-rosalind.md")


def test_a_hand_supplied_report_is_not_an_orphan(tmp_path):
    research = tmp_path / "research" / "traits" / "ecology"
    research.mkdir(parents=True)
    (research / "pasted-deep-research-rosalind.md").write_text(
        "---\npipeline_run: false\n---\n\nbody\n")
    (research / "stray-deep-research-rosalind.md").write_text("---\nprovider: openai\n---\nbody\n")
    found = orphan_reports(tmp_path / "research" / "traits", tmp_path, {}, "rosalind")
    assert found == ["research/traits/ecology/stray-deep-research-rosalind.md"]


def test_the_rosalind_namespace_has_no_unaccounted_pipeline_report():
    """The invariant the docs promise: nothing in the rosalind namespace claims
    to be a pipeline run that the manifest cannot account for. Phrased as the
    orphan gate rather than "every file is hand-supplied", so the lane's first
    real report (with its `ok` row) does not turn this red (#639)."""
    tracked = sorted(RESEARCH_DIR.rglob("*-deep-research-rosalind.md"))
    assert tracked, "expected the hand-supplied Rosalind artifacts"
    recorded = ok_outputs(MANIFEST) if MANIFEST.exists() else {}
    assert orphan_reports(RESEARCH_DIR, REPO_ROOT, recorded, "rosalind") == []


@pytest.mark.parametrize("provider,env,expected", [
    ("edison", {}, "EDISON_API_KEY"),
    ("edison", {"FUTUREHOUSE_API_KEY": "x"}, None),
    ("edison", {"EDISON_PLATFORM_API_KEY": "x"}, None),  # #646: research_env aliases it
    ("rosalind", {}, "ROSALIND_API_KEY"),
    ("rosalind", {"OPENAI_API_KEY": "x"}, "ROSALIND_API_KEY"),  # #641: not the lane's key
    ("gpt-rosalind", {"ROSALIND_API_KEY": "x"}, None),
    ("rosalind", {"EDISON_API_KEY": "x"}, "ROSALIND_API_KEY"),
    ("openai", {}, "OPENAI_API_KEY"),
    ("perplexity", {}, None),  # not preflighted: the client reports it
])
def test_preflight_is_provider_aware(provider, env, expected):
    """Before this, `--provider rosalind` demanded EDISON_API_KEY and then ran
    without checking the key it actually needed."""
    error = preflight_error(provider, env)
    if expected is None:
        assert error is None
    else:
        assert error is not None and expected in error
