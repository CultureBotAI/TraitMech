# Stage 6 (`infrastructure`) Implementation Plan — Cycle 7

## 1. Frozen Snapshot (`INFRA_TASKS.md`)

- **Frozen at**: `2026-10-31T00:24:29Z`
- **Source revision**: `631087f24fec9e00bd969d8827fd642207b61f9b`
- **Source path**: `INFRA_TASKS.md`
- **Snapshot artifact**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000007/stage-06/revision-0001/infra_snapshot.md`
- **SHA-256**: `e05b7cea505cfd01a4ee6338cd39ceb53e25982e72f1909a5c90e32a7ef4c2c4`
- **Frozen task IDs (`9`)**: `traitmech-infra-0001`, `traitmech-infra-0002`, `traitmech-infra-0003`, `traitmech-infra-0004`, `traitmech-infra-0005`, `traitmech-infra-0006`, `traitmech-infra-0007`, `traitmech-infra-0008`, `traitmech-infra-0009`

No tasks arrived after the `2026-10-31T00:24:29Z` cutoff; the frozen task-ID scope is fixed at `traitmech-infra-0001` through `traitmech-infra-0009`.

## 2. Dependency-Aware Task Triage & Selection

| Task ID | Issue | Status at Freeze | Dependencies | Cycle 7 Stage 6 Action | Target Disposition |
|---|---|---|---|---|---|
| `traitmech-infra-0001` | `#1962` | `resolved` | None | Retain resolved state from PR `#1961` | `resolved` |
| `traitmech-infra-0002` | `#1988` | `resolved` | None | Retain resolved state from Cycle 1 Stage 6 (`PR #1989`) | `resolved` |
| `traitmech-infra-0003` | `#1988` | `resolved` | None | Retain resolved state from Cycle 1 Stage 6 (`PR #1989`) | `resolved` |
| `traitmech-infra-0004` | `#1981` | `resolved` | None | Retain resolved state from Cycle 1 Stage 6 (`PR #1989`) | `resolved` |
| `traitmech-infra-0005` | `#2002` | `resolved` | None | Retain resolved state from Cycle 3 Stage 6 (`PR #2012`) | `resolved` |
| `traitmech-infra-0006` | `#2002` | `resolved` | None | Retain resolved state from Cycle 4 Stage 6 (`PR #2022`) | `resolved` |
| `traitmech-infra-0007` | `#2002` | `resolved` | None | Retain resolved state from Cycle 5 Stage 6 (`PR #2032`) | `resolved` |
| `traitmech-infra-0008` | `#2002` | `resolved` | None | Retain resolved state from Cycle 6 Stage 6 (`PR #2042`) | `resolved` |
| `traitmech-infra-0009` | `#2002` | `open` | None | Implement PMC / EuropePMC PPR primary reference alias resolution and repeated `definition_source` pairing for `UNQUOTED_DEFINITION_SOURCE` in `scripts/audit_evidence_snippets.py` + unit tests in `tests/test_audit_evidence_snippets.py` | `resolved` |

## 3. Selected Implementation Work (`traitmech-infra-0009`)

### Root Cause
In `scripts/audit_evidence_snippets.py`, `_record_wiki_doi_aliases()` previously only extracted `PMID:...` references from `record_refs` and paired a record's `definition_source: DOI:...` with a single quoted `PMID:` only when `DOI:...` appeared inside a `List_system_article.md` markdown table snippet. During Cycle 7 Stage 4 frozen-inventory review, all 15 remaining DefenseFinder `CLASS` records in `data/traits/genomics/` (`abia_system.yaml`, `abib_system.yaml`, `abic_system.yaml`, `abid_system.yaml`, `abii_system.yaml`, `abir_system.yaml`, `abiu_system.yaml`, `lit_system.yaml`, `card_nlr_endonuclease_system.yaml`, `card_nlr_gasdermin_system.yaml`, `card_nlr_phospho_system.yaml`, `card_nlr_subtilase_system.yaml`, `card_nlr_system.yaml`, `nlr_like_bnacht_system.yaml`, and `pd_t2_1_system.yaml`) whose `definition_source: DOI:...` was absent from `evidence[].reference` (`MISSING_DEFINITION_SOURCE_EVIDENCE` in `scripts/record_review.py inspect`) were found to already carry a verified non-elliptical verbatim quote from that exact `definition_source` publication in `evidence[0]`, cited under its `PMID:`, `https://europepmc.org/article/PPR/PPR668921`, or `https://pmc.ncbi.nlm.nih.gov/articles/PMC.../` alias (with `List_system_article.md` cited in `evidence[]` and/or `definition_source` repeated in `canonical_examples[].reference` or `synonyms[].source`). All 15 records were remediated in Cycle 7 Stage 5 (`PR #2047`).

### Design
1. **Primary publication reference prefix recognition (`_PRIMARY_REF_PREFIXES`)**:
   - Define `_PRIMARY_REF_PREFIXES = ("PMID:", "https://pmc.ncbi.nlm.nih.gov/articles/PMC", "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC", "https://europepmc.org/article/PPR/")` so `_record_wiki_doi_aliases()` recognizes `PMC` and `EuropePMC PPR` primary publication references in `record_refs` alongside `PMID:`.
2. **Repeated `definition_source` confirmation (`_record_repeats_def_source`)**:
   - Add `_record_repeats_def_source(doc, def_source)` to check whether `def_source` is also cited in `canonical_examples[].reference` or `synonyms[].source` on the same record.
3. **Extended in-record alias pairing (`_record_wiki_doi_aliases`)**:
   - When `len(primary_refs) == 1`, pair each `DOI:...` extracted from `List_system_article.md` table-row snippets with the single quoted primary `PMID:`/`PMC`/`EuropePMC` reference, and if `def_source` starts with `"DOI:"` and the record either cites `List_system_article.md` or repeats `def_source` in `canonical_examples[].reference` or `synonyms[].source`, also map `def_source` to that single quoted primary reference.
4. **Unit tests (`tests/test_audit_evidence_snippets.py`)**:
   - Add `test_unquoted_definition_source_pmc_europepmc_and_repeated_def_source_aliases`:
     - Record A (`card_nlr.yaml`): `definition_source: DOI:10.1093/nar/gkad789` absent from `evidence[].reference`, while `evidence[]` quotes `https://pmc.ncbi.nlm.nih.gov/articles/PMC10639090/` alongside a `List_system_article.md` entry -> flagged with `UNQUOTED_DEFINITION_SOURCE`.
     - Record B (`pdt2.yaml`): `definition_source: DOI:10.1101/2023.05.31.542950` absent from `evidence[].reference`, while `evidence[]` quotes `https://europepmc.org/article/PPR/PPR668921` and `canonical_examples[0].reference` repeats `DOI:10.1101/2023.05.31.542950` -> flagged with `UNQUOTED_DEFINITION_SOURCE`.
     - Record C (`abic.yaml`): `definition_source: DOI:10.1111/j.1574-6968.1992.tb05882.x` absent from `evidence[].reference`, while `evidence[]` quotes `PMID:1335946` and `synonyms[0].source` repeats `DOI:10.1111/j.1574-6968.1992.tb05882.x` -> flagged with `UNQUOTED_DEFINITION_SOURCE`.
     - Record D (`clean.yaml`): `definition_source` quoted directly in `evidence[0]` alongside its `PMC` alias -> not flagged.

## 4. Acceptance Criteria
1. `reviews/workflow/mech-goal-sequence-20261019/cycle-000007/stage-06/revision-0001/infra_snapshot.md` matches the exact supervisor-frozen `INFRA_TASKS.md` content (`sha256: e05b7cea505cfd01a4ee6338cd39ceb53e25982e72f1909a5c90e32a7ef4c2c4`).
2. `INFRA_TASKS.md` marks `traitmech-infra-0009` as `status: resolved` with full disposition and retains `traitmech-infra-0001`..`0008` as `resolved`.
3. `tests/test_audit_evidence_snippets.py` passes all 42 unit tests.
4. Full-corpus `audit(check_reports=False, check_definition_sources=True)` runs cleanly with `0` `UNQUOTED_DEFINITION_SOURCE` warnings across all 1,130 records.
5. `just qc`, `just validate-strict`, `just validate-history`, `just audit-history-records`, `just pr-sanity`, and `.venv/bin/ruff check` pass with exit code `0`.
