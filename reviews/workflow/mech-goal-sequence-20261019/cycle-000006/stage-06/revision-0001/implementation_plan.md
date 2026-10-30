# Cycle 6 Stage 6 Infrastructure Implementation Plan

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `6`
- **Stage**: `6` (`infrastructure`)
- **Source Revision**: `a77de264a91152ca1ee92e9ee484159b47154254`
- **Frozen `INFRA_TASKS.md` Snapshot**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000006/stage-06/revision-0001/infra_snapshot.md`
- **Frozen `INFRA_TASKS.md` SHA-256**: `3baacd70e660e445040c9711228118816e196897a27dcdd192a7e1d22c406dd6`
- **Scope Frozen At**: `2026-10-30T05:39:16Z`

## 1. Frozen `INFRA_TASKS.md` Task Inventory

At `scope_frozen_at` (`2026-10-30T05:39:16Z`), `INFRA_TASKS.md` contains 8 tasks (`traitmech-infra-0001` through `traitmech-infra-0008`), of which 7 were resolved in Cycles 1–5 (`traitmech-infra-0001` through `traitmech-infra-0007`) and 1 is non-resolved (`traitmech-infra-0008`, status `open`):

| Task ID | Status in Snapshot | Linked Issue | Summary & Disposition |
| --- | --- | --- | --- |
| `traitmech-infra-0001` | `resolved` (Cycle 1 Stage 6, PR `#1989`) | [#1981](https://github.com/CultureBotAI/TraitMech/issues/1981) | Pre-resolved in Cycle 1 Stage 6 (`d624afd2edd2c0d404e148718f1bc1f150686cc4`). |
| `traitmech-infra-0002` | `resolved` (Cycle 1 Stage 6, PR `#1989`) | [#1982](https://github.com/CultureBotAI/TraitMech/issues/1982) | Pre-resolved in Cycle 1 Stage 6 (`d624afd2edd2c0d404e148718f1bc1f150686cc4`). |
| `traitmech-infra-0003` | `resolved` (Cycle 1 Stage 6, PR `#1989`) | [#1983](https://github.com/CultureBotAI/TraitMech/issues/1983) | Pre-resolved in Cycle 1 Stage 6 (`d624afd2edd2c0d404e148718f1bc1f150686cc4`). |
| `traitmech-infra-0004` | `resolved` (Cycle 2 Stage 6, PR `#1997`) | [#1982](https://github.com/CultureBotAI/TraitMech/issues/1982) | Pre-resolved in Cycle 2 Stage 6 (`82e72b23a51cbefb450ad2ecd3999936604f3db4`). |
| `traitmech-infra-0005` | `resolved` (Cycle 3 Stage 6, PR `#2004`) | [#2002](https://github.com/CultureBotAI/TraitMech/issues/2002) | Pre-resolved in Cycle 3 Stage 6 (`538e0144fb41016c5511e7d8b5a0ead1b5483052`). |
| `traitmech-infra-0006` | `resolved` (Cycle 4 Stage 6, PR `#2010`) | [#2002](https://github.com/CultureBotAI/TraitMech/issues/2002) | Pre-resolved in Cycle 4 Stage 6 (`4ac486c7a0d35a8b2587eb7e421eb69b2740fd88`). |
| `traitmech-infra-0007` | `resolved` (Cycle 5 Stage 6, PR `#2029`) | [#2002](https://github.com/CultureBotAI/TraitMech/issues/2002) | Pre-resolved in Cycle 5 Stage 6 (`206928d63484eb4dd0b7d21633e0f752b7da18cf`). |
| `traitmech-infra-0008` | `open` -> **To resolve in Cycle 6 Stage 6** | [#2002](https://github.com/CultureBotAI/TraitMech/issues/2002) | Extend `UNQUOTED_DEFINITION_SOURCE` in `scripts/audit_evidence_snippets.py` to resolve `DOI:`↔`PMID:` reference aliases from `data/raw/defense_finder/wiki/List_system_article.md` and in-record `List_system_article.md` DOI/PMID pairs. |

## 2. Implementation Design for `traitmech-infra-0008`

### Problem Statement
In Cycle 6 Stage 4 corpus review (`reviews/structured/20261026T053500Z-cycle6-stage4-corpus-record-and-cohort-review/review.yaml`), all 13 remediated `CLASS` records in the DefenseFinder genomics cohort (`data/traits/genomics/fs_giy_yig_system.yaml`, `fs_hepn_tm_system.yaml`, `fs_hp_system.yaml`, `fs_hp_sdh_sah_system.yaml`, `fs_hsdr_like_system.yaml`, `fs_sma_system.yaml`, `mazef_system.yaml`, `mok_hok_sok_system.yaml`, `pfiat_system.yaml`, `prrc_system.yaml`, `rloc_system.yaml`, `rnlab_system.yaml`, and `tagi_system.yaml`) declared a `DOI:` `definition_source` (e.g. `DOI:10.1093/nar/gky781` or `DOI:10.1016/s1097-2765(03)00409-x`) while their record-level `evidence[0].reference` cited the corresponding `PMID:` for the exact same publication alongside the DefenseFinder wiki `List_system_article.md` DOI row. Because `UNQUOTED_DEFINITION_SOURCE` in `scripts/audit_evidence_snippets.py` matched reference CURIE strings literally without resolving `DOI:`↔`PMID:` aliases from `data/raw/defense_finder/wiki/List_system_article.md` or in-record `List_system_article.md` DOI/PMID pairs, all 13 records escaped automated detection until line-by-line review.

### Planned Changes
1. **`scripts/audit_evidence_snippets.py`**:
   - Add `DEFENSE_FINDER_ARTICLES_MD = REPO_ROOT / "data" / "raw" / "defense_finder" / "wiki" / "List_system_article.md"` and `aes_defense_finder_articles_md() -> Path` so unit tests can redirect the path via `monkeypatch`.
   - Implement `_load_defense_finder_ref_aliases(path: Path | None = None) -> dict[str, set[str]]`:
     - Optionally reads `path` (defaulting to `aes_defense_finder_articles_md()`) when present on disk.
     - Unescapes markdown backslash-escaped dots (`\.` -> `.`) on each line and extracts `DOI:` (`10.\d{4,9}/...`) and `PMID:` (`PMID:\d+`, PubMed URLs, or standalone numeric PMID columns in pipe-delimited markdown table rows) appearing on the same line, returning a bidirectional `DOI:`↔`PMID:` alias dictionary.
   - Implement `_record_wiki_doi_aliases(doc: dict, record_refs: set[str]) -> dict[str, set[str]]`:
     - Inspects `doc.get("evidence")`: when a record includes an evidence item whose `reference` cites `List_system_article.md` and whose `snippet` contains a DOI `10.\d{4,9}/...` (after unescaping `\.` -> `.`), pairs that `DOI:<doi>` with any quoted `PMID:` references in `record_refs` on the same record.
   - In `audit(check_definition_sources=True)`:
     - Resolve aliases for `def_source` from both `_load_defense_finder_ref_aliases()` and `_record_wiki_doi_aliases(doc, record_refs)`.
     - Flag `UNQUOTED_DEFINITION_SOURCE` when `def_source.startswith(("PMID:", "DOI:"))` and `def_source not in record_refs` and either:
       - `def_source in family_quoted`,
       - `has_corpus_16_quote` (`not is_object_property and def_source_in_ev and def_source in corpus_quoted_refs_16`), or
       - `has_alias_quote` (any alias of `def_source` is in `record_refs`, `family_quoted`, or, for non-`OBJECT_PROPERTY` records, `corpus_quoted_refs_16`).
2. **`tests/test_audit_evidence_snippets.py`**:
   - Redirect `aes.DEFENSE_FINDER_ARTICLES_MD` in `_write_trait` so tests are isolated from workspace files.
   - Add unit tests verifying:
     - `_load_defense_finder_ref_aliases` parses `DOI:`↔`PMID:` equivalence pairs (including markdown-escaped `10\.1093/...` DOIs) from `data/raw/defense_finder/wiki/List_system_article.md` and `audit(check_reports=False, check_definition_sources=True)` flags a `CLASS` record whose `definition_source` is absent from `evidence[].reference` while its mapped `PMID:`/`DOI:` alias is quoted on the same record or in-corpus.
     - In-record `List_system_article.md` DOI row + `PMID:` quote detection flags the pre-C6S5 DefenseFinder genomics record shape (e.g. `definition_source: DOI:10.1093/nar/gky781` with `evidence[0].reference: PMID:30202937` and `evidence[1].reference: .../List_system_article.md`) and clears once `evidence[0].reference` is aligned to `definition_source`.
3. **`INFRA_TASKS.md` and Repository History**:
   - Update `traitmech-infra-0008` in `INFRA_TASKS.md` from `status: open` to `status: resolved` with full verification disposition.
   - Record repository history entry under `history/infrastructure/stage6_infrastructure_plan/`.
   - Run all repository and workflow validation gates and record results in `validation.md` and `evidence.yaml`.
