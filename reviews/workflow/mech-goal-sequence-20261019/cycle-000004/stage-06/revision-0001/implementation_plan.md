# Cycle 4 Stage 6 Infrastructure Implementation Plan (`mech-goal-sequence-20261019`, Cycle 4, Stage 6, Revision 1)

## 1. Frozen Scope & Provenance

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage / Revision**: `4` / `6` (`infrastructure`) / `1`
- **Source Revision**: `51e1363e233cdeb08484f045ac1f2115d74171c2` (merged `main` after Cycle 4 Stage 5 PR `#2009`)
- **Supervisor-Frozen Cutoff (`scope_frozen_at`)**: `2026-10-25T14:45:19Z`
- **Frozen `INFRA_TASKS.md` Snapshot**:
  - Path: `reviews/workflow/mech-goal-sequence-20261019/cycle-000004/stage-06/revision-0001/infra_snapshot.md`
  - SHA-256: `c49c57fe6f650ba6e6950b184a8d12edc2f0d46ff58e05ff7ffd0bb73611caa5`
- **Task Inventory at Cutoff**:
  - Total tasks in `INFRA_TASKS.md`: `6` (`traitmech-infra-0001` through `traitmech-infra-0006`)
  - Previously resolved tasks (`status: resolved`): `5`
    - `traitmech-infra-0001` (Issue `#1962`, PR `#1961`) — Replace workstation-absolute paths in `.claude/skills/traitmech-evolve-workflow/SKILL.md`
    - `traitmech-infra-0002` (Issue `#1988`, PR `#1989`) — Support bare section-level `attaches_to` anchors on `Discussion` entries when target sections are empty
    - `traitmech-infra-0003` (Issue `#1988`, PR `#1989`) — Offline `--check-inventory` structural check for `reports/uniprot_grounding_audit.tsv` in `audit-derived-reports`
    - `traitmech-infra-0004` (Issue `#1981`, PR `#1989`) — Optional `--check-definition-sources` (`UNQUOTED_DEFINITION_SOURCE` warning) in `scripts/audit_evidence_snippets.py`
    - `traitmech-infra-0005` (Issue `#2002`, PR `#2004`) — Parent-record CURIE lookup (`doc.get("identifier")`) and snippet-less `evidence[]` check on `UNQUOTED_DEFINITION_SOURCE` in `scripts/audit_evidence_snippets.py`
  - Open tasks in frozen scope (`status: open`): `1`
    - `traitmech-infra-0006` (Issue `#2002`, follow-up to `#1981`) — Skip `term_kind: OBJECT_PROPERTY` records with non-empty predicate-stem snippets in `scripts/audit_evidence_snippets.py` `UNQUOTED_DEFINITION_SOURCE` so 1-word predicate stems are not flagged as missing when sibling `OBJECT_PROPERTY` records have `>=12`-char stems.

---

## 2. Issue Grouping & Deduplication

| Task ID | Issue | Origin | Priority | Dependencies | Target Files | Selected Action |
|---|---|---|---|---|---|---|
| `traitmech-infra-0006` | [CultureBotAI/TraitMech#2002](https://github.com/CultureBotAI/TraitMech/issues/2002) (follow-up to [#1981](https://github.com/CultureBotAI/TraitMech/issues/1981)) | Cycle 4 Stage 4 (`record_review`) | Medium | None | `scripts/audit_evidence_snippets.py`, `tests/test_audit_evidence_snippets.py`, `INFRA_TASKS.md` | **Implement & resolve in Cycle 4 Stage 6** |

- **Deduplication rationale**: `traitmech-infra-0006` was logged during Cycle 4 Stage 4 and linked directly to [CultureBotAI/TraitMech#2002](https://github.com/CultureBotAI/TraitMech/issues/2002) (with lineage to [#1981](https://github.com/CultureBotAI/TraitMech/issues/1981) and `traitmech-infra-0005`). Reusing `#2002` preserves the exact supervisor-frozen `issue_url` in `infra_snapshot.md` and keeps the `UNQUOTED_DEFINITION_SOURCE` audit refinement linked on the same issue thread.

---

## 3. Root-Cause Analysis & Dependency-Ordered Implementation Plan

### `traitmech-infra-0006` (`#2002`) — `scripts/audit_evidence_snippets.py` (`UNQUOTED_DEFINITION_SOURCE` on `OBJECT_PROPERTY` records)

1. **Root Cause**:
   - After Cycle 3 Stage 6 enabled parent/sibling CURIE propagation via `doc.get("identifier")` (`traitmech-infra-0005`), running `audit(check_definition_sources=True)` across the full corpus surfaced 26 `term_kind: OBJECT_PROPERTY` records in `data/traits/metabolism/` (`builds_base_from.yaml`, `compartmentalizes.yaml`, `degrades.yaml`, etc., all children of `METPO:2000001` sharing `definition_source: DOI:10.1099/ijsem.0.004332`).
   - Specifically, 2 sibling `OBJECT_PROPERTY` records (`produces_acid_from.yaml` with `"acid production"` and `disproportionates.yaml` with `"disproportionation"`) carry predicate-stem snippets `>= 12` characters (`MIN_SNIPPET_CHARS = 12`), which populated `refs_by_parent_id["METPO:2000001"]`.
   - Meanwhile, the other 26 `OBJECT_PROPERTY` records carry valid 1-word predicate-stem snippets (`"alkaline"`, `"compartment"`, `"degradation"`, `"oxidation"`, `"reduction"`, `"transport"`, `"growth"`, `"respiration"`, `< 12` characters) that `len(snip) >= MIN_SNIPPET_CHARS` treated as missing.
2. **Implementation Steps**:
   - Update `scripts/audit_evidence_snippets.py`:
     - In the first pass (`check_definition_sources`), check `is_object_property = _norm(str(doc.get("term_kind") or "")) == "OBJECT_PROPERTY"` and skip populating `quoted` when `is_object_property` is true so `OBJECT_PROPERTY` predicate-stem snippets (even those `>= 12` characters) never propagate into `refs_by_record_id` or `refs_by_parent_id` as full-sentence corpus quotes.
     - In the second pass (`check_definition_sources`), set `min_snip_chars = 1 if is_object_property else MIN_SNIPPET_CHARS` when computing `record_refs`, so any non-empty, non-elliptical predicate-stem snippet on a `term_kind: OBJECT_PROPERTY` record satisfies `definition_source` coverage (while still flagging snippet-less or elliptical `OBJECT_PROPERTY` entries if a `CLASS` record in the family provides a full-sentence quote).
   - Update `tests/test_audit_evidence_snippets.py`:
     - Add `test_unquoted_definition_source_object_property_predicate_stems` testing that `OBJECT_PROPERTY` siblings with `>=12`-char and `<12`-char predicate-stem snippets do not false-positive each other, while a snippet-less `OBJECT_PROPERTY` record is still flagged when a `CLASS` parent record provides a full-sentence verbatim quote.
   - Update `INFRA_TASKS.md`:
     - Mark `traitmech-infra-0006` as `status: resolved` with full disposition and evidence paths.
   - Record repository history in `history/infrastructure/stage6_infrastructure_plan/2026-10-25T150000Z-antigravity-c4s601.yaml`.

---

## 4. Acceptance Criteria

1. `.venv/bin/python -m pytest tests/test_audit_evidence_snippets.py` passes (`38 passed`, including `test_unquoted_definition_source_object_property_predicate_stems`).
2. All 28 `term_kind: OBJECT_PROPERTY` records in `data/traits/metabolism/` pass `audit(check_definition_sources=True)` with `0` `UNQUOTED_DEFINITION_SOURCE` findings.
3. `.venv/bin/python scripts/audit_evidence_snippets.py`, `.venv/bin/python scripts/validate_strict.py`, `.venv/bin/python scripts/audit_causal_graphs.py`, `.venv/bin/python scripts/audit_graph_protein_taxa.py`, `.venv/bin/python scripts/record_review.py --check`, `.venv/bin/python scripts/validate_history_links.py`, `.venv/bin/python scripts/pr_sanity.py`, `.venv/bin/python -m ruff check`, `.venv/bin/python -m pytest`, and `kg_microbe_workflows validate-evidence` all pass with exit code `0`.
4. `INFRA_TASKS.md` retains all 6 task IDs (`traitmech-infra-0001`..`0006`), all with `status: resolved`, and `0` open, deferred, or blocked tasks remain.
