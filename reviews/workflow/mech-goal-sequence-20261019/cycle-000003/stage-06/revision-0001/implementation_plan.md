# Cycle 3 Stage 6 Infrastructure Implementation Plan (`mech-goal-sequence-20261019`, Cycle 3, Stage 6, Revision 1)

## 1. Frozen Scope & Provenance

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage / Revision**: `3` / `6` (`infrastructure`) / `1`
- **Source Revision**: `bb0ac42d67b473316af3f154dafc1162a9a973c4` (merged `main` after Cycle 3 Stage 5 PR `#2003`)
- **Supervisor-Frozen Cutoff (`scope_frozen_at`)**: `2026-10-24T06:05:25Z`
- **Frozen `INFRA_TASKS.md` Snapshot**:
  - Path: `reviews/workflow/mech-goal-sequence-20261019/cycle-000003/stage-06/revision-0001/infra_snapshot.md`
  - SHA-256: `f0ec81378be99a5e846068def8894db101fc208d26ef099022e3e8d4843422d4`
- **Task Inventory at Cutoff**:
  - Total tasks in `INFRA_TASKS.md`: `5` (`traitmech-infra-0001` through `traitmech-infra-0005`)
  - Previously resolved tasks (`status: resolved`): `4`
    - `traitmech-infra-0001` (Issue `#1962`, PR `#1961`) — Replace workstation-absolute paths in `.claude/skills/traitmech-evolve-workflow/SKILL.md`
    - `traitmech-infra-0002` (Issue `#1988`, PR `#1989`) — Support bare section-level `attaches_to` anchors on `Discussion` entries when target sections are empty
    - `traitmech-infra-0003` (Issue `#1988`, PR `#1989`) — Offline `--check-inventory` structural check for `reports/uniprot_grounding_audit.tsv` in `audit-derived-reports`
    - `traitmech-infra-0004` (Issue `#1981`, PR `#1989`) — Optional `--check-definition-sources` (`UNQUOTED_DEFINITION_SOURCE` warning) in `scripts/audit_evidence_snippets.py`
  - Open tasks in frozen scope (`status: open`): `1`
    - `traitmech-infra-0005` (Issue `#2002`, follow-up to `#1981`) — Fix parent-record CURIE lookup (`doc.get("identifier")`) and snippet-presence check in `scripts/audit_evidence_snippets.py` so `UNQUOTED_DEFINITION_SOURCE` detects unquoted or snippet-less `definition_source` entries when an in-corpus verbatim quote exists.

---

## 2. Issue Grouping & Deduplication

| Task ID | Issue | Origin | Priority | Dependencies | Target Files | Selected Action |
|---|---|---|---|---|---|---|
| `traitmech-infra-0005` | [CultureBotAI/TraitMech#2002](https://github.com/CultureBotAI/TraitMech/issues/2002) (follow-up to [#1981](https://github.com/CultureBotAI/TraitMech/issues/1981)) | Cycle 3 Stage 4 / Stage 5 (`resolve_review`) | Medium | None (Cycle 3 Stage 5 remediation of `F-C3S4-DEF-SRC-001`..`017` merged in PR `#2003`) | `scripts/audit_evidence_snippets.py`, `tests/test_audit_evidence_snippets.py`, `INFRA_TASKS.md` | **Implement & resolve in Cycle 3 Stage 6** |

- **Deduplication rationale**: `traitmech-infra-0005` was logged during Cycle 3 Stage 5 and linked directly to [CultureBotAI/TraitMech#2002](https://github.com/CultureBotAI/TraitMech/issues/2002) (with lineage to [#1981](https://github.com/CultureBotAI/TraitMech/issues/1981), which introduced `--check-definition-sources` in Cycle 1 Stage 6). Reusing `#2002` preserves the exact supervisor-frozen `issue_url` in `infra_snapshot.md` and keeps the Stage 5 data remediation and Stage 6 audit-script hardening linked on a single issue thread.

---

## 3. Root-Cause Analysis & Dependency-Ordered Implementation Plan

### `traitmech-infra-0005` (`#2002`) — `scripts/audit_evidence_snippets.py` (`UNQUOTED_DEFINITION_SOURCE`)

1. **Root Cause 1 — Record CURIE Field Lookup (`identifier` vs `id`)**:
   - In `scripts/audit_evidence_snippets.py`, both the first pass (indexing `refs_by_record_id`) and the second pass (resolving `family_quoted` for each record) previously computed `rec_id = _norm(str(doc.get("id") or path.stem))`.
   - However, curated `TraitRecord` YAML files in `data/traits/` store their primary ontology/synthetic CURIE in `identifier` (e.g. `identifier: METPO:1000605` or `identifier: traitmech:000001`), while `parent_traits` lists those CURIEs (`METPO:...` / `traitmech:...`).
   - As a result, `refs_by_record_id.get(parent_id, set())` never matched a real parent record's `identifier`, and parent records never inherited valid quotes from direct child records (`refs_by_parent_id.get(rec_id, set())`).
2. **Root Cause 2 — Snippet-less `evidence[]` Entries vs Absent References**:
   - In Cycle 3 Stage 4/5 (`#2002`), 16 of the 17 affected records already listed `definition_source` in `evidence[].reference` (`supports: SUPPORT`, `evidence_source: IN_VITRO`), but omitted `snippet:` on that record-level `evidence[]` item while a verified verbatim quote for the same PMID/DOI existed on a parent/sibling/child record or on `causal_graphs`.
   - While `record_refs` in `scripts/audit_evidence_snippets.py` already filtered for valid non-elliptical snippets (`len(snip) >= MIN_SNIPPET_CHARS and "..." not in snip and "…" not in snip`), the `UNQUOTED_DEFINITION_SOURCE` detail string unconditionally stated `"is absent from record-level evidence[].reference"`, obscuring whether the reference was missing entirely or present without a non-elliptical verbatim snippet.
3. **Implementation Steps**:
   - Update `scripts/audit_evidence_snippets.py`:
     - Compute `rec_id = _norm(str(doc.get("identifier") or doc.get("id") or path.stem))` and index `refs_by_record_id` under all non-empty keys in `{doc.get("identifier"), doc.get("id"), path.stem}` so both real `TraitRecord` CURIEs (`identifier:`) and minimal unit-test fixtures (`id:` or filename stem) resolve cleanly.
     - Include `refs_by_parent_id.get(rec_id, set())` in `family_quoted` so parent records also see valid verbatim quotes present on their direct child records.
     - Track `record_any_refs` alongside `record_refs` and emit a clear diagnostic detail distinguishing `"lacks a non-elliptical verbatim snippet in record-level evidence[]"` (when `def_source in record_any_refs`) from `"is absent from record-level evidence[].reference"` (when `def_source not in record_any_refs`).
   - Update `tests/test_audit_evidence_snippets.py`:
     - Add `test_unquoted_definition_source_identifier_field_and_snippet_less_evidence` testing both child-to-parent and parent-to-child propagation across `identifier: METPO:...` records with snippet-less `evidence[]` entries.
   - Update `INFRA_TASKS.md`:
     - Mark `traitmech-infra-0005` as `status: resolved` with full disposition and evidence paths.
   - Record repository history in `history/infrastructure/stage6_infrastructure_plan/2026-10-24T062200Z-antigravity-c3s601.yaml`.

---

## 4. Acceptance Criteria

1. `uv run python -m pytest tests/test_audit_evidence_snippets.py` passes (37/37 tests, including `test_unquoted_definition_source_identifier_field_and_snippet_less_evidence`).
2. All 17 records remediated in Cycle 3 Stage 5 (`#2002`) pass `uv run python scripts/audit_evidence_snippets.py --check-definition-sources` with `0` `UNQUOTED_DEFINITION_SOURCE` findings.
3. `uv run python scripts/audit_evidence_snippets.py`, `just validate-strict`, `just audit-derived-reports`, `uv run python scripts/validate_history_links.py`, `uv run python scripts/pr_sanity.py`, `uv run ruff check`, `uv run python -m pytest`, and `kg_microbe_workflows validate-evidence` all pass with exit code `0`.
4. `INFRA_TASKS.md` retains all 5 task IDs (`traitmech-infra-0001`..`0005`), all with `status: resolved`, and `0` open, deferred, or blocked tasks remain.
