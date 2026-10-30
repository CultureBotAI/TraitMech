# Stage 6 Infrastructure Validation Report — `mech-goal-sequence-20261019` (Cycle 6, Stage 6, Revision 1)

## 1. Frozen Snapshot Verification

- **Frozen `INFRA_TASKS.md` Cutoff (`frozen_at`)**: `2026-10-30T05:39:16Z`
- **Source Revision (`HEAD` at freeze)**: `a77de264a91152ca1ee92e9ee484159b47154254`
- **Snapshot Path**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000006/stage-06/revision-0001/infra_snapshot.md`
- **Snapshot SHA-256**: `3baacd70e660e445040c9711228118816e196897a27dcdd192a7e1d22c406dd6` (exact match to supervisor-frozen `status.json` `infra_scope.sha256`)

## 2. Task-Level Verification (`traitmech-infra-0008`)

### `traitmech-infra-0008` — DOI↔PMID reference alias resolution from `data/raw/defense_finder/wiki/List_system_article.md` (`#2002`)
- **Code modified**: `scripts/audit_evidence_snippets.py`
  - Added `DEFENSE_FINDER_ARTICLES_MD = ROOT / "data" / "raw" / "defense_finder" / "wiki" / "List_system_article.md"` and `aes_defense_finder_articles_md()`.
  - Added `_extract_wiki_dois()`, `_load_defense_finder_ref_aliases()`, and `_record_wiki_doi_aliases()` to resolve bidirectional `DOI:`↔`PMID:` reference aliases from `data/raw/defense_finder/wiki/List_system_article.md` (when present) and from in-record `List_system_article.md` table-row snippets paired with a single quoted `PMID:`.
  - Updated the `UNQUOTED_DEFINITION_SOURCE` check in `audit(check_definition_sources=True)` to compute `has_alias_quote` and flag non-`OBJECT_PROPERTY` records whose `definition_source` is omitted from `record_refs` while a mapped `PMID:`/`DOI:` alias is already quoted in `record_refs`, `family_quoted`, or `corpus_quoted_refs_16`.
- **Unit tests**: `tests/test_audit_evidence_snippets.py`
  - Updated `_write_trait` to isolate `aes.DEFENSE_FINDER_ARTICLES_MD` under `tmp_path`.
  - Added `test_unquoted_definition_source_defense_finder_wiki_doi_to_pmid_alias_file` and `test_unquoted_definition_source_in_record_list_system_article_doi_pmid_pair`, verifying that:
    - `_load_defense_finder_ref_aliases()` parses Markdown-escaped DOIs (`10\.1093/nar/gky781`, `10\.1016/s1097-2765(03)00409-x`) and PMIDs (`PMID:30202937`, `12962616`) into bidirectional `DOI:`↔`PMID:` alias sets;
    - A `CLASS` record with `definition_source: DOI:10.1093/nar/gky781` and `evidence[0].reference: PMID:30202937` is flagged with `UNQUOTED_DEFINITION_SOURCE` both when `List_system_article.md` is on disk and when only the in-record `List_system_article.md` table row is present;
    - Records whose `List_system_article.md` row cites a different review DOI (`10\.1016/j.mib.2005.06.006`) than the primary paper `PMID:` in `definition_source` (`PMID:2937000`) are not falsely aliased;
    - Aligning `evidence[0].reference` to `DOI:10.1093/nar/gky781` clears the `UNQUOTED_DEFINITION_SOURCE` finding.
  - Executed `pytest tests/test_audit_evidence_snippets.py`: `41 passed`.
- **Corpus-wide verification**:
  - Executed `audit(check_reports=False, check_definition_sources=True)` across all 1,130 `data/traits/**/*.yaml` records: `0` `UNQUOTED_DEFINITION_SOURCE` findings across all 1,102 `CLASS` records and all 28 `OBJECT_PROPERTY` records.
  - Executed `python3 scripts/audit_evidence_snippets.py`: `0 new finding(s) beyond baseline`.

## 3. Repository & Workflow Gate Summary

| Gate | Command | Result |
|---|---|---|
| Workflow profile validation | `PYTHONPATH=../culturebotai-claw/src ../culturebotai-claw/.venv/bin/python -m kg_microbe_workflows validate workflow/mech-workflow.yaml --cycle workflow/parent/mech-cycle.yaml --parent workflow/parent/workflow.yaml` | `Workflow profile valid` (exit 0) |
| Stage 6 evidence manifest validation | `PYTHONPATH=../culturebotai-claw/src ../culturebotai-claw/.venv/bin/python -m kg_microbe_workflows validate-evidence --root . --required-output infra_snapshot --required-output implementation_plan --required-output validation reviews/workflow/mech-goal-sequence-20261019/cycle-000006/stage-06/revision-0001/evidence.yaml` | `Evidence manifest valid` (exit 0) |
| Strict schema & ontology validation | `python3 scripts/validate_strict.py` | `1130 valid, 0 with errors` (exit 0) |
| Causal graph audit | `python3 scripts/audit_causal_graphs.py` | `0 new finding(s) beyond baseline` (exit 0) |
| Evidence snippet audit | `python3 scripts/audit_evidence_snippets.py` | `0 new finding(s) beyond baseline` (exit 0) |
| Graph protein taxa audit | `python3 scripts/audit_graph_protein_taxa.py` | `0 error(s)` (exit 0) |
| Record review integrity check | `python3 scripts/record_review.py check` | `valid_reviews: 104` (exit 0) |
| History link validation | `python3 scripts/validate_history_links.py history/` | `history links: 1307 record(s), 0 invalid` (exit 0) |
| History record audit | `python3 scripts/audit_history_records.py --base origin/main` | `0 finding(s)` (exit 0) |
| Writer guard audit | `python3 scripts/audit_writers.py` | `753 writers audited` (exit 0) |
| PR sanity check | `python3 scripts/pr_sanity.py` | `0 finding(s), all clear` (exit 0) |
| Ruff linter | `ruff check scripts/audit_evidence_snippets.py tests/test_audit_evidence_snippets.py` | `All checks passed!` (exit 0) |
| Pytest suite | `pytest tests/test_audit_evidence_snippets.py` | `41 passed` (exit 0) |
