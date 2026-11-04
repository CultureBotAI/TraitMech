# Stage 6 (`infrastructure`) Implementation Plan — Cycle 9

## 1. Frozen Snapshot (`INFRA_TASKS.md`)

- **Frozen at**: `2026-11-04T13:01:27Z`
- **Source revision**: `be688e11b51e5e428db1e118944bdc5c90ce806a`
- **Source path**: `INFRA_TASKS.md`
- **Snapshot artifact**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000009/stage-06/revision-0001/infra_snapshot.md`
- **SHA-256**: `801753500782790b7f82089d1a9236286d062795b0af2f1b813edad885081cf1`
- **Frozen task IDs (`12`)**: `traitmech-infra-0001`, `traitmech-infra-0002`, `traitmech-infra-0003`, `traitmech-infra-0004`, `traitmech-infra-0005`, `traitmech-infra-0006`, `traitmech-infra-0007`, `traitmech-infra-0008`, `traitmech-infra-0009`, `traitmech-infra-0010`, `traitmech-infra-0011`, `traitmech-infra-0012`

No tasks arrived after the `2026-11-04T13:01:27Z` cutoff; the frozen task-ID scope is fixed at `traitmech-infra-0001` through `traitmech-infra-0012`.

## 2. Dependency-Aware Task Triage & Selection

| Task ID | Issue | Status at Freeze | Dependencies | Cycle 9 Stage 6 Action | Target Disposition |
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
| `traitmech-infra-0010` | `#2002` | `resolved` | None | Retain resolved state from Cycle 8 Stage 6 (`PR #2056`) | `resolved` |
| `traitmech-infra-0011` | `#1988` | `open` | None | Add bounded exponential-backoff retry (`RETRYABLE_HTTP_CODES = {429, 500, 502, 503, 504}`) to `fetch()` in `scripts/audit_uniprot_grounding.py`, plus unit tests in `tests/test_audit_uniprot_grounding.py` | `resolved` |
| `traitmech-infra-0012` | `#2002` | `open` | None | Add `_norm_ref()` to `scripts/audit_evidence_snippets.py` to canonicalize `DOI:` CURIEs to `DOI:<lowercase>` across `quoted`, `corpus_quoted_refs_16`, `refs_by_record_id`, `refs_by_parent_id`, `record_refs`, `record_any_refs`, `def_source`, `_load_defense_finder_ref_aliases()`, `_record_wiki_doi_aliases()`, and `_record_repeats_def_source()`, plus unit tests in `tests/test_audit_evidence_snippets.py` | `resolved` |

## 3. Selected Implementation Work (`traitmech-infra-0011` & `traitmech-infra-0012`)

### 3.1 `traitmech-infra-0011` (`scripts/audit_uniprot_grounding.py`, `tests/test_audit_uniprot_grounding.py`)
- **Root Cause**: `fetch(accession, delay=0.1)` in `scripts/audit_uniprot_grounding.py` executed a single `urllib.request.urlopen` call and immediately returned `{"status": "error", "uniprot_name": f"HTTP {exc.code}"}` on transient HTTP 5xx/429 responses from `rest.uniprot.org` (observed on 3 accessions during Cycle 9 Stage 3 full-corpus refresh).
- **Design**:
  1. Add `RETRYABLE_HTTP_CODES = frozenset({429, 500, 502, 503, 504})`.
  2. Update `fetch(accession: str, delay: float = 0.1, *, max_retries: int = 3, retry_delay: float | None = None)` to retry transient `urllib.error.HTTPError` codes in `RETRYABLE_HTTP_CODES` and transient `urllib.error.URLError`/`TimeoutError` exceptions up to `max_retries` times with exponential backoff (`base_backoff * (2 ** (attempt - 1))`), while returning immediately on `HTTP 404` (`{"status": "deleted"}`) and non-retryable 4xx responses.
  3. Add unit tests `test_fetch_retries_transient_http_5xx_and_429_then_succeeds` and `test_fetch_does_not_retry_http_404_or_400_and_retries_urlerror` in `tests/test_audit_uniprot_grounding.py`.

### 3.2 `traitmech-infra-0012` (`scripts/audit_evidence_snippets.py`, `tests/test_audit_evidence_snippets.py`)
- **Root Cause**: In `scripts/audit_evidence_snippets.py`, `quoted`, `corpus_quoted_refs_16`, `record_refs`, `record_any_refs`, and `def_source` stored `_norm()` strings without canonicalizing `DOI:` prefix/suffix casing (e.g. `DOI:10.1002/(SICI)...` vs `DOI:10.1002/(sici)...`), causing set lookups in `UNQUOTED_DEFINITION_SOURCE` to miss case-variant DOI citations.
- **Design**:
  1. Add `_norm_ref(text: str) -> str` to collapse whitespace via `_norm(text)` and canonicalize `DOI:` CURIEs to `f"DOI:{val[4:].strip().lower()}"` while preserving non-DOI schemes (`PMID:`, `https://...`).
  2. Apply `_norm_ref()` across `quoted`, `corpus_quoted_refs_16`, `refs_by_record_id`, `refs_by_parent_id`, `record_refs`, `record_any_refs`, `def_source`, `_load_defense_finder_ref_aliases()`, `_record_wiki_doi_aliases()`, and `_record_repeats_def_source()`.
  3. Add unit test `test_unquoted_definition_source_canonicalizes_doi_casing_across_sets` in `tests/test_audit_evidence_snippets.py`.

## 4. Acceptance Criteria
1. `reviews/workflow/mech-goal-sequence-20261019/cycle-000009/stage-06/revision-0001/infra_snapshot.md` matches the exact supervisor-frozen `INFRA_TASKS.md` content (`sha256: 801753500782790b7f82089d1a9236286d062795b0af2f1b813edad885081cf1`).
2. `INFRA_TASKS.md` marks `traitmech-infra-0011` and `traitmech-infra-0012` as `status: resolved` with full dispositions and retains `traitmech-infra-0001`..`0010` as `resolved`.
3. `tests/test_audit_uniprot_grounding.py` (13 tests) and `tests/test_audit_evidence_snippets.py` (44 tests) pass all 57 unit tests.
4. Full-corpus `audit(check_reports=False, check_definition_sources=True)` runs cleanly with `0` `UNQUOTED_DEFINITION_SOURCE` warnings across all 1,130 records.
5. `just qc`, `just validate-strict`, `just validate-history`, `just audit-history-records`, `just pr-sanity`, and `.venv/bin/ruff check` pass with exit code `0`.
