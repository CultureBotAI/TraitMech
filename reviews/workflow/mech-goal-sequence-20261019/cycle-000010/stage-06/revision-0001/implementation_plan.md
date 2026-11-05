# Stage 6 (`infrastructure`) Implementation Plan — Cycle 10

## 1. Frozen Snapshot (`INFRA_TASKS.md`)

- **Frozen at**: `2026-11-05T02:48:11Z`
- **Source revision**: `72c9a0b83000a38f3458f6bf22460799374d7ebc`
- **Source path**: `INFRA_TASKS.md`
- **Snapshot artifact**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000010/stage-06/revision-0001/infra_snapshot.md`
- **SHA-256**: `b2e3be6195140877390bf27ec7ca35b8f10090493d1fe1b85c97aec221324439`
- **Frozen task IDs (`13`)**: `traitmech-infra-0001`, `traitmech-infra-0002`, `traitmech-infra-0003`, `traitmech-infra-0004`, `traitmech-infra-0005`, `traitmech-infra-0006`, `traitmech-infra-0007`, `traitmech-infra-0008`, `traitmech-infra-0009`, `traitmech-infra-0010`, `traitmech-infra-0011`, `traitmech-infra-0012`, `traitmech-infra-0013`

No tasks arrived after the `2026-11-05T02:48:11Z` cutoff; the frozen task-ID scope is fixed at `traitmech-infra-0001` through `traitmech-infra-0013`.

## 2. Dependency-Aware Task Triage & Selection

| Task ID | Issue | Status at Freeze | Dependencies | Cycle 10 Stage 6 Action | Target Disposition |
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
| `traitmech-infra-0011` | `#1988` | `resolved` | None | Retain resolved state from Cycle 9 Stage 6 (`PR #2063`) | `resolved` |
| `traitmech-infra-0012` | `#2002` | `resolved` | None | Retain resolved state from Cycle 9 Stage 6 (`PR #2063`) | `resolved` |
| `traitmech-infra-0013` | `#1988` | `open` | None | Add incremental `--merge-existing` and `--accession` modes (`load_report_rows()`, `_is_reusable_existing_row()`, `_normalize_accessions()`) to `scripts/audit_uniprot_grounding.py` and unit tests in `tests/test_audit_uniprot_grounding.py` | `resolved` |

## 3. Selected Implementation Work (`traitmech-infra-0013`)

### 3.1 `traitmech-infra-0013` (`scripts/audit_uniprot_grounding.py`, `tests/test_audit_uniprot_grounding.py`)
- **Root Cause**: `main()` and `audit_uses()` in `scripts/audit_uniprot_grounding.py` always queried `rest.uniprot.org` for all `iter_uses(iter_nodes(args.traits_dir))` rows (206 uses across 171 unique accessions) and rewrote `reports/uniprot_grounding_audit.tsv` from scratch. When curating a small cohort of new `protein_examples` (such as Cohort M in Cycle 10 Stage 3) after an upstream UniProt release bump, there was no CLI mode to preserve unchanged clean rows in `reports/uniprot_grounding_audit.tsv` while live-auditing only newly added, modified, dirty, or explicitly selected accessions in `iter_uses()` corpus order.
- **Design**:
  1. Add `_normalize_accessions()`, `_is_reusable_existing_row()`, and `load_report_rows()` in `scripts/audit_uniprot_grounding.py`.
  2. Extend `audit_uses(uses, *, delay=0.1, resolver=None, existing_rows=None, accessions=None)` so that when `existing_rows` is provided, clean existing rows matching `declared_inventory_row(use)` and internal consistency checks (and not listed in `accessions`) are reused offline with updated `reused_in_n_files`, while newly added, modified, dirty, or `--accession`-selected uses are live-resolved via `resolver` and merged in `iter_uses()` order.
  3. Add `--merge-existing` and repeatable/comma-separated `--accession` CLI flags to `main()` in `scripts/audit_uniprot_grounding.py`.
  4. Add unit tests `test_merge_existing_reuses_unchanged_rows_and_audits_only_new_or_modified_in_corpus_order` and `test_accession_filter_and_cli_merge_existing` in `tests/test_audit_uniprot_grounding.py`.

## 4. Acceptance Criteria
1. `reviews/workflow/mech-goal-sequence-20261019/cycle-000010/stage-06/revision-0001/infra_snapshot.md` matches the exact supervisor-frozen `INFRA_TASKS.md` content (`sha256: b2e3be6195140877390bf27ec7ca35b8f10090493d1fe1b85c97aec221324439`).
2. `INFRA_TASKS.md` marks `traitmech-infra-0013` as `status: resolved` with full disposition and retains `traitmech-infra-0001`..`0012` as `resolved`.
3. `tests/test_audit_uniprot_grounding.py` passes all 15 unit tests.
4. `scripts/audit_uniprot_grounding.py --check-inventory` and `scripts/audit_uniprot_grounding.py --merge-existing` run cleanly on the full corpus (`206` uses across `171` unique accessions, `0` findings, `0` network calls when unchanged).
5. `just qc`, `just validate-strict`, `just validate-history`, `just audit-history-records`, `just pr-sanity`, and `.venv/bin/ruff check` pass with exit code `0`.
