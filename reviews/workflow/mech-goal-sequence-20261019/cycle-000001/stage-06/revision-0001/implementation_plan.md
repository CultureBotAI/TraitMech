# Stage 6 Infrastructure Implementation Plan (`mech-goal-sequence-20261019`, Cycle 1, Stage 6)

## 1. Frozen Intake Scope

- **Repository**: `CultureBotAI/TraitMech` (`traitmech`)
- **Run / Cycle / Stage**: `mech-goal-sequence-20261019`, Cycle `1`, Stage `6` (`infrastructure`)
- **Implementation PR**: https://github.com/CultureBotAI/TraitMech/pull/1989
- **Source revision (`main`)**: `7d4b750774051b4678d16114438ee34ed126f25c`
- **Supervisor cutoff (`scope_frozen_at`)**: `2026-10-22T07:14:11Z`
- **Frozen snapshot path**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-06/revision-0001/infra_snapshot.md`
- **Frozen snapshot SHA-256**: `bbf6969d714c5f2b51c5933da30429aceea259f20ebc0cf95caa73a87e99d200`

### Frozen Task Inventory Summary

| Task ID | Origin | Frozen Status | Issue URL | Stage 6 Target Status |
|---|---|---|---|---|
| `traitmech-infra-0001` | Cycle 1, Stage 1 (`add_records`) | `resolved` (PR #1961) | https://github.com/CultureBotAI/TraitMech/issues/1962 | Already resolved prior to Stage 6 |
| `traitmech-infra-0002` | Cycle 1, Stage 2 (`causal_graphs`) | `note` | https://github.com/CultureBotAI/TraitMech/issues/1988 | `resolved` |
| `traitmech-infra-0003` | Cycle 1, Stage 3 (`protein_examples`) | `note` | https://github.com/CultureBotAI/TraitMech/issues/1988 | `resolved` |
| `traitmech-infra-0004` | Cycle 1, Stage 4 (`record_review`) / Stage 5 (`resolve_review_findings`) | `note` | https://github.com/CultureBotAI/TraitMech/issues/1981 | `resolved` |

---

## 2. Issue Grouping and Dependency Analysis

All 3 pending infrastructure notes (`traitmech-infra-0002`, `traitmech-infra-0003`, `traitmech-infra-0004`) are offline QC/audit enhancements in `scripts/`, `justfile`, and `tests/` with zero external blockers and zero inter-task dependencies:

1. **Issue [#1988](https://github.com/CultureBotAI/TraitMech/issues/1988)** (*Stage 6 infrastructure plan: offline QC audit enhancements (`traitmech-infra-0002`, `traitmech-infra-0003`, `traitmech-infra-0004`)*):
   - Groups `traitmech-infra-0002` and `traitmech-infra-0003` (both recorded with `status: note` and no pre-existing issue link at freeze time) and cross-references `traitmech-infra-0004`.
2. **Issue [#1981](https://github.com/CultureBotAI/TraitMech/issues/1981)** (*Stage 5 review remediation: add record-level `evidence` snippets for `definition_source` on `cyanophycin_granule`, `cadmium_tolerant`, `cobalt_tolerant`, and `zinc_tolerant`*):
   - Preserved on `traitmech-infra-0004` because `traitmech-infra-0004` was frozen at `2026-10-22T07:14:11Z` with `issue_url: https://github.com/CultureBotAI/TraitMech/issues/1981` after Stage 5 remediated the 4 corpus instances and queued the preventive `scripts/audit_evidence_snippets.py` warning for Stage 6.

### Dependency Graph

- `traitmech-infra-0002` (`scripts/audit_discussion_anchors.py`, `tests/test_audit_discussion_anchors.py`) — independent.
- `traitmech-infra-0003` (`scripts/audit_uniprot_grounding.py`, `justfile`, `tests/test_audit_uniprot_grounding.py`) — independent; depends only on Stage 3's refreshed `reports/uniprot_grounding_audit.tsv` (already merged in PR #1977).
- `traitmech-infra-0004` (`scripts/audit_evidence_snippets.py`, `tests/test_audit_evidence_snippets.py`) — depends on Stage 5's corpus remediation of `F-DEF-SRC-CYANOPHYCIN-001`..`004` (already merged in PR #1986).

---

## 3. Implementation Specifications and Acceptance Criteria

### 3.1 `traitmech-infra-0002` — Section-level `attaches_to` anchors on `Discussion` entries when target sections are empty
- **Changes**:
  - Update `scripts/audit_discussion_anchors.py` to define `EMPTY_SECTION_ANCHORS` (`{"causal_graphs", "ontology_mapping", "ecological_interactions"}`) and allow bare `<section>` tokens in `discussions[].attaches_to` when that target section is empty on the record, while continuing to reject bare `<section>` tokens (as well as empty-prefix or empty-target `#` tokens) with `MALFORMED_ANCHOR` once the section is populated.
  - Add unit tests in `tests/test_audit_discussion_anchors.py` (`test_section_level_anchor_allowed_when_target_section_empty`, `test_section_level_anchor_rejected_when_target_section_populated`).
- **Acceptance Criteria**:
  - `uv run python scripts/audit_discussion_anchors.py` exits `0` on the live corpus (`discussion anchors: 0 error(s), 0 warning(s)`).
  - `pytest tests/test_audit_discussion_anchors.py` passes all 10 unit tests.

### 3.2 `traitmech-infra-0003` — Offline structural consistency check for `reports/uniprot_grounding_audit.tsv` in `audit-derived-reports`
- **Changes**:
  - Update `scripts/audit_uniprot_grounding.py` to add `INVENTORY_FIELDS`, `declared_inventory_row()`, `check_inventory()`, and `--check-inventory` CLI flag.
  - Expose `REPO_ROOT` in `scripts/audit_uniprot_grounding.py` so `scripts/audit_qc_paths_coverage.py` (`just audit-qc-paths`) statically verifies `data` and `reports` path coverage in `.github/workflows/qc.yaml`.
  - Wire `uv run python scripts/audit_uniprot_grounding.py --check-inventory --out "$tmp/committed_$uga"` into `audit-derived-reports` in `justfile` comparing against `git show "HEAD:reports/uniprot_grounding_audit.tsv"`.
  - Add unit tests in `tests/test_audit_uniprot_grounding.py` (`test_check_inventory_detects_missing_or_drifted_report_rows`, `test_committed_uniprot_grounding_audit_matches_corpus_inventory`).
- **Acceptance Criteria**:
  - `uv run python scripts/audit_uniprot_grounding.py --check-inventory` exits `0` (`163 uses match reports/uniprot_grounding_audit.tsv`).
  - `just audit-derived-reports` and `just audit-qc-paths` exit `0`.
  - `pytest tests/test_audit_uniprot_grounding.py` passes all 11 unit tests.

### 3.3 `traitmech-infra-0004` — Advisory `UNQUOTED_DEFINITION_SOURCE` check in `scripts/audit_evidence_snippets.py`
- **Changes**:
  - Update `scripts/audit_evidence_snippets.py` to add `UNQUOTED_DEFINITION_SOURCE` (`WARN`) and `--check-definition-sources` (`audit(check_definition_sources=True)`), flagging any record whose `definition_source` (`PMID:` or `DOI:`) is omitted from record-level `evidence[].reference` despite already carrying a verified verbatim snippet on the record's own `causal_graphs` edges or on its `parent_traits`/sibling records.
  - Add unit tests in `tests/test_audit_evidence_snippets.py` (`test_unquoted_definition_source_flagged_when_quoted_on_edge_or_sibling`, `test_unquoted_definition_source_parent_sibling_propagation_and_short_snippet_filter`).
- **Acceptance Criteria**:
  - `uv run python scripts/audit_evidence_snippets.py --check-definition-sources` exits `0` with `0` `UNQUOTED_DEFINITION_SOURCE` findings across the live 1,130-record corpus.
  - `pytest tests/test_audit_evidence_snippets.py` passes all 36 unit tests.

---

## 4. Carry-Forward Summary

- **Resolved tasks in Stage 6**: `3` (`traitmech-infra-0002`, `traitmech-infra-0003`, `traitmech-infra-0004`)
- **Previously resolved tasks in Cycle 1**: `1` (`traitmech-infra-0001` in PR #1961)
- **Deferred / blocked tasks carried forward**: `0` (`carry_forward_ids: []`)
