# Stage 6 Infrastructure Implementation Plan — `mech-goal-sequence-20261019` (Cycle 5, Stage 6, Revision 1)

## 1. Frozen Intake Scope & Cutoff

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage / Revision**: Cycle 5, Stage 6 (`infrastructure`), Revision 1
- **Source Revision (`HEAD` at freeze)**: `bc1dfa795cce63059bc4744d06aa371aa335e423`
- **Supervisor-Frozen Cutoff (`frozen_at`)**: `2026-10-25T23:20:15Z`
- **Frozen `INFRA_TASKS.md` Snapshot**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000005/stage-06/revision-0001/infra_snapshot.md`
- **Frozen Snapshot SHA-256**: `255b181dfdb8d8da5e057b2440b1eb95ba91f7db63f4530ded6144f49770db34`

### Inventory Summary at Cutoff (`7` total tasks)

| Task ID | Issue | Status at Freeze | Action in Cycle 5 Stage 6 |
|---|---|---|---|
| `traitmech-infra-0001` | [CultureBotAI/TraitMech#1962](https://github.com/CultureBotAI/TraitMech/issues/1962) | `resolved` (PR #1961) | Retain resolved disposition unchanged |
| `traitmech-infra-0002` | [CultureBotAI/TraitMech#1988](https://github.com/CultureBotAI/TraitMech/issues/1988) | `resolved` (PR #1989) | Retain resolved disposition unchanged |
| `traitmech-infra-0003` | [CultureBotAI/TraitMech#1988](https://github.com/CultureBotAI/TraitMech/issues/1988) | `resolved` (PR #1989) | Retain resolved disposition unchanged |
| `traitmech-infra-0004` | [CultureBotAI/TraitMech#1981](https://github.com/CultureBotAI/TraitMech/issues/1981) | `resolved` (PR #1989) | Retain resolved disposition unchanged |
| `traitmech-infra-0005` | [CultureBotAI/TraitMech#2002](https://github.com/CultureBotAI/TraitMech/issues/2002) | `resolved` (PR #2004) | Retain resolved disposition unchanged |
| `traitmech-infra-0006` | [CultureBotAI/TraitMech#2002](https://github.com/CultureBotAI/TraitMech/issues/2002) | `resolved` (PR #2010) | Retain resolved disposition unchanged |
| `traitmech-infra-0007` | [CultureBotAI/TraitMech#2002](https://github.com/CultureBotAI/TraitMech/issues/2002) | `open` | Implement & validate in Cycle 5 Stage 6 (`resolved`) |

---

## 2. Dependency-Aware Implementation Plan

### Selected Task: `traitmech-infra-0007` (linked to `#2002`, follow-up to `#1981`)

- **Origin**: `mech-goal-sequence-20261019`, Cycle 5, Stage 4 (`record_review`)
- **Dependencies**: None (`0` blocking tasks; the 5 `CLASS` records `genome_streamlining.yaml`, `biopolymer_degradation.yaml`, `denitrification.yaml`, `sulfur_oxidation.yaml`, and `catalase_activity.yaml` that surfaced this gap were remediated in Cycle 5 Stage 5, PR #2026).
- **Problem Statement**:
  In `scripts/audit_evidence_snippets.py`, `UNQUOTED_DEFINITION_SOURCE` previously only checked whether a record's `definition_source` (`PMID:` or `DOI:`) carried a non-elliptical verbatim quote (`>= 12` chars) on the same record, its immediate 1-hop `parent_traits` (`refs_by_record_id`), its immediate children (`refs_by_parent_id`), or direct siblings sharing an immediate `parent_traits` entry. During Cycle 5 Stage 4 frozen-inventory review, 5 `CLASS` records (`data/traits/genomics/genome_streamlining.yaml`, `data/traits/metabolism/biopolymer_degradation.yaml`, `data/traits/metabolism/denitrification.yaml`, `data/traits/metabolism/sulfur_oxidation.yaml`, and `data/traits/physiology/catalase_activity.yaml`) were found to declare a primary `definition_source` and cite that exact reference in record-level `evidence[0]` without a `snippet`, while a verified non-elliptical verbatim quote (`>= 16` chars) from the exact same `definition_source` already existed on a 2-hop ancestor (`nitrogen_respiration.yaml` / `anaerobic_respiration.yaml`) or on a cross-cohort `TraitRecord` (`oligotrophic.yaml`, `saprotrophy.yaml`, `lithotrophic.yaml`, `oxidative_stress_response.yaml`).
- **Implementation Design**:
  1. Define `MIN_CORPUS_QUOTE_CHARS = 16` in `scripts/audit_evidence_snippets.py` alongside `MIN_SNIPPET_CHARS = 12`.
  2. In the first pass of `audit()` in `scripts/audit_evidence_snippets.py` (when `check_definition_sources` is `True` and `not is_object_property`), track `corpus_quoted_refs_16: set[str] = set()` containing every reference that carries a non-elliptical quote of length `>= MIN_CORPUS_QUOTE_CHARS` (`16`).
  3. In the second pass of `audit()` in `scripts/audit_evidence_snippets.py` (when `check_definition_sources` is `True`), compute `def_source_in_ev = def_source in record_any_refs` and `has_corpus_16_quote = (not is_object_property and def_source_in_ev and def_source in corpus_quoted_refs_16)`, flagging `UNQUOTED_DEFINITION_SOURCE` whenever `def_source.startswith(("PMID:", "DOI:")) and (def_source in family_quoted or has_corpus_16_quote) and def_source not in record_refs`.
  4. Add unit test `test_unquoted_definition_source_corpus_wide_16char_quote_when_in_evidence` in `tests/test_audit_evidence_snippets.py` covering:
     - Cross-cohort `< 16`-char quote does not trigger corpus-wide propagation;
     - Cross-cohort `>= 16`-char non-elliptical quote on a `CLASS` record triggers `UNQUOTED_DEFINITION_SOURCE` on a `CLASS` record that cites `definition_source` in `evidence[].reference` without a snippet (`def_source_in_ev == True`);
     - Unrelated `CLASS` record that does not cite `definition_source` in `evidence[].reference` (`def_source_in_ev == False`) is not flagged by distant corpus-wide quotes;
     - Adding a verbatim snippet to the record clears `UNQUOTED_DEFINITION_SOURCE`.
  5. Update `INFRA_TASKS.md` to mark `traitmech-infra-0007` as `status: resolved` with its verification disposition and record repository history in `history/infrastructure/stage6_infrastructure_plan/2026-10-25T233000Z-antigravity-c5s601.yaml`.

### Acceptance Criteria

1. `pytest tests/test_audit_evidence_snippets.py` passes (including `test_unquoted_definition_source_corpus_wide_16char_quote_when_in_evidence`).
2. Running `audit(check_reports=False, check_definition_sources=True)` across all 1,130 `data/traits/**/*.yaml` records reports `0` `UNQUOTED_DEFINITION_SOURCE` findings across all 1,102 `CLASS` records and all 28 `OBJECT_PROPERTY` records.
3. `python3 scripts/audit_evidence_snippets.py` passes against `conf/evidence_snippet_baseline.tsv` (`0 new finding(s) beyond baseline`).
4. All repository QC and workflow validation gates (`validate-evidence`, `pytest`, `ruff`, `validate_strict.py`, `audit_causal_graphs.py`, `audit_evidence_snippets.py`, `audit_graph_protein_taxa.py`, `record_review.py check`, `validate_history_links.py history/`, `audit_history_records.py`, `audit_writers.py`, `pr_sanity.py`) pass with exit code `0`.

---

## 3. Deferred / Blocked Tasks

- **None (`0` deferred or blocked tasks)**. All 7 tasks in the frozen `INFRA_TASKS.md` inventory (`traitmech-infra-0001` through `traitmech-infra-0007`) are now `resolved`.
