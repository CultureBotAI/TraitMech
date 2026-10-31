# Stage 6 (`infrastructure`) Implementation Plan — Cycle 8

## 1. Frozen Snapshot (`INFRA_TASKS.md`)

- **Frozen at**: `2026-10-31T14:58:49Z`
- **Source revision**: `f3e2ff60c3f71ca005667575c3c6a76743080b5a`
- **Source path**: `INFRA_TASKS.md`
- **Snapshot artifact**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000008/stage-06/revision-0001/infra_snapshot.md`
- **SHA-256**: `645800fcacee5bfc7c08a84880efb75eb8f92b5ff04a74660307c4a1a202f5de`
- **Frozen task IDs (`10`)**: `traitmech-infra-0001`, `traitmech-infra-0002`, `traitmech-infra-0003`, `traitmech-infra-0004`, `traitmech-infra-0005`, `traitmech-infra-0006`, `traitmech-infra-0007`, `traitmech-infra-0008`, `traitmech-infra-0009`, `traitmech-infra-0010`

No tasks arrived after the `2026-10-31T14:58:49Z` cutoff; the frozen task-ID scope is fixed at `traitmech-infra-0001` through `traitmech-infra-0010`.

## 2. Dependency-Aware Task Triage & Selection

| Task ID | Issue | Status at Freeze | Dependencies | Cycle 8 Stage 6 Action | Target Disposition |
|---|---|---|---|---|---|
| `traitmech-infra-0001` | `#1962` | `resolved` | None | Retain resolved state from PR `#1961` | `resolved` |
| `traitmech-infra-0002` | `#1988` | `resolved` | None | Retain resolved state from Cycle 1 Stage 6 (`PR #1989`) | `resolved` |
| `traitmech-infra-0003` | `#1988` | `resolved` | None | Retain resolved state from Cycle 1 Stage 6 (`PR #1989`) | `resolved` |
| `traitmech-infra-0004` | `#1981` | `resolved` | None | Retain resolved state from Cycle 1 Stage 6 (`PR #1989`) | `resolved` |
| `traitmech-infra-0005` | `#2002` | `resolved` | None | Retain resolved state from Cycle 3 Stage 6 (`PR #2012`) | `resolved` |
| `traitmech-infra-0006` | `#2002` | `resolved` | None | Retain resolved state from Cycle 4 Stage 6 (`PR #2022`) | `resolved` |
| `traitmech-infra-0007` | `#2002` | `resolved` | None | Retain resolved state from Cycle 5 Stage 6 (`PR #2032`) | `resolved` |
| `traitmech-infra-0008` | `#2002` | `resolved` | None | Retain resolved state from Cycle 6 Stage 6 (`PR #2042`) | `resolved` |
| `traitmech-infra-0009` | `#2002` | `resolved` | None | Retain resolved state from Cycle 7 Stage 6 (`PR #2048`) | `resolved` |
| `traitmech-infra-0010` | `#2002` | `open` | None | Extend `_record_repeats_def_source` to inspect `causal_graphs[].edges[].evidence[].reference` and update `has_corpus_16_quote` in `scripts/audit_evidence_snippets.py` so `UNQUOTED_DEFINITION_SOURCE` also checks `corpus_quoted_refs_16` when a `CLASS` record repeats `definition_source` in `canonical_examples[].reference`, `synonyms[].source`, or `causal_graphs[].edges[].evidence[].reference`, plus unit tests in `tests/test_audit_evidence_snippets.py` | `resolved` |

## 3. Selected Implementation Work (`traitmech-infra-0010`)

### Root Cause
In `scripts/audit_evidence_snippets.py`, `has_corpus_16_quote` previously checked `not is_object_property and def_source_in_ev and def_source in corpus_quoted_refs_16`, requiring `def_source_in_ev == True` (`definition_source` already listed in `evidence[].reference`), while `_record_repeats_def_source(doc, def_source)` only inspected `canonical_examples[].reference` and `synonyms[].source` (not `causal_graphs[].edges[].evidence[].reference`). During Cycle 8 Stage 4 frozen-inventory review of the `ecology` and `metabolism` cohorts, 12 `ecology` `CLASS` records were found to cite `definition_source` in `evidence[0].reference` without a `snippet` (remediated in Cycle 8 Stage 5, `PR #2055`), and 14 FAPROTAX `metabolism` `CLASS` records (`traitmech:000121`..`traitmech:000134`) were found to repeat `definition_source` in `synonyms[0].source` while omitting it from `evidence[].reference` (`def_source_in_ev == False`). If any of a record's repeated `definition_source` references (in `canonical_examples[].reference`, `synonyms[].source`, or `causal_graphs[].edges[].evidence[].reference`) acquires a `>= 16`-char quote anywhere in `corpus_quoted_refs_16` across a non-sibling cohort while `def_source_in_ev` is `False`, `has_corpus_16_quote` previously failed to flag `UNQUOTED_DEFINITION_SOURCE`.

### Design
1. **Extended `_record_repeats_def_source(doc, def_source)`**:
   - Extend `_record_repeats_def_source(doc, def_source)` in `scripts/audit_evidence_snippets.py` to also iterate over `causal_graphs[].edges[].evidence[].reference` in addition to `canonical_examples[].reference` and `synonyms[].source`.
2. **Extended `has_corpus_16_quote`**:
   - Update `has_corpus_16_quote` in `scripts/audit_evidence_snippets.py` to check `not is_object_property and (def_source_in_ev or _record_repeats_def_source(doc, def_source)) and def_source in corpus_quoted_refs_16`.
3. **Unit tests (`tests/test_audit_evidence_snippets.py`)**:
   - Add `test_unquoted_definition_source_corpus_16_when_def_source_repeated_outside_evidence`:
     - Cross-cohort donor record (`x.yaml`) provides `>= 16`-char non-elliptical quotes for `DOI:10.1126/science.1254070`, `DOI:10.1038/nrmicro1852`, and `DOI:10.1146/annurev.micro.62.081307.162918` in `corpus_quoted_refs_16`.
     - Record A (`faprotax_syn.yaml`): `definition_source: DOI:10.1126/science.1254070` absent from `evidence[].reference` (`def_source_in_ev == False`) and repeated in `synonyms[0].source` -> flagged with `UNQUOTED_DEFINITION_SOURCE` (`is absent from record-level evidence[].reference`).
     - Record B (`faprotax_ex.yaml`): `definition_source: DOI:10.1038/nrmicro1852` absent from `evidence[].reference` (`def_source_in_ev == False`) and repeated in `canonical_examples[0].reference` -> flagged with `UNQUOTED_DEFINITION_SOURCE`.
     - Record C (`edge_repeat.yaml`): `definition_source: DOI:10.1146/annurev.micro.62.081307.162918` absent from `evidence[].reference` (`def_source_in_ev == False`) and repeated on `causal_graphs[0].edges[0].evidence[0].reference` without a snippet -> flagged with `UNQUOTED_DEFINITION_SOURCE`.
     - Record D (`unrepeated.yaml`): `definition_source: DOI:10.1126/science.1254070` absent from `evidence[].reference` and not repeated in `synonyms`, `canonical_examples`, or `causal_graphs` -> not flagged.

## 4. Acceptance Criteria
1. `reviews/workflow/mech-goal-sequence-20261019/cycle-000008/stage-06/revision-0001/infra_snapshot.md` matches the exact supervisor-frozen `INFRA_TASKS.md` content (`sha256: 645800fcacee5bfc7c08a84880efb75eb8f92b5ff04a74660307c4a1a202f5de`).
2. `INFRA_TASKS.md` marks `traitmech-infra-0010` as `status: resolved` with full disposition and retains `traitmech-infra-0001`..`0009` as `resolved`.
3. `tests/test_audit_evidence_snippets.py` passes all 43 unit tests.
4. Full-corpus `audit(check_reports=False, check_definition_sources=True)` runs cleanly with `0` `UNQUOTED_DEFINITION_SOURCE` warnings across all 1,130 records.
5. `just qc`, `just validate-strict`, `just validate-history`, `just audit-history-records`, `just pr-sanity`, and `.venv/bin/ruff check` pass with exit code `0`.
