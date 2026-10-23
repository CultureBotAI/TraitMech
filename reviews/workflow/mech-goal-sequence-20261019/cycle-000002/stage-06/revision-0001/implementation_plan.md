# Stage 6 Infrastructure Implementation Plan (`mech-goal-sequence-20261019`, Cycle 2, Stage 6)

## 1. Frozen Intake Scope

- **Repository**: `CultureBotAI/TraitMech` (`traitmech`)
- **Run / Cycle / Stage**: `mech-goal-sequence-20261019`, Cycle `2`, Stage `6` (`infrastructure`)
- **Source revision (`main`)**: `1a00d990f70bab5f11c077fe0c764c1f03ab928b`
- **Supervisor cutoff (`scope_frozen_at`)**: `2026-10-23T18:11:47Z`
- **Frozen snapshot path**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-06/revision-0001/infra_snapshot.md`
- **Frozen snapshot SHA-256**: `d6116631e4d3c248b8b05b5b33b6d3a5d4e9f4244eebea5f0a36dd755324eefa`

### Frozen Task Inventory Summary

| Task ID | Origin | Frozen Status | Issue URL | Stage 6 Disposition |
|---|---|---|---|---|
| `traitmech-infra-0001` | Cycle 1, Stage 1 (`add_records`) | `resolved` (PR #1961) | https://github.com/CultureBotAI/TraitMech/issues/1962 | Already resolved prior to Cycle 2 Stage 6 |
| `traitmech-infra-0002` | Cycle 1, Stage 2 (`causal_graphs`) | `resolved` (PR #1989) | https://github.com/CultureBotAI/TraitMech/issues/1988 | Already resolved in Cycle 1 Stage 6 |
| `traitmech-infra-0003` | Cycle 1, Stage 3 (`protein_examples`) | `resolved` (PR #1989) | https://github.com/CultureBotAI/TraitMech/issues/1988 | Already resolved in Cycle 1 Stage 6 |
| `traitmech-infra-0004` | Cycle 1, Stage 4 (`record_review`) / Stage 5 (`resolve_review_findings`) | `resolved` (PR #1989) | https://github.com/CultureBotAI/TraitMech/issues/1981 | Already resolved in Cycle 1 Stage 6 |

---

## 2. Intake and Dependency Analysis

Across Cycle 2 Stages 1–5:
- **Stage 1 (`add_records`, PR #1991)**: Repeated bounded-frontier discovery search across all 6 frontier sources confirmed 0 new admissible standalone traits and surfaced 0 new infrastructure blockers or requirements.
- **Stage 2 (`causal_graphs`, PR #1992)**: Added 7 new literature-grounded causal graphs across 7 traits (`arsenate_reducing`, `betaine_synthesizing`, `deep_biosphere_inhabiting`, `heavy_metal_tolerant`, `intertidal_zone_inhabiting`, `L-arginine_degrading`, `sulfate_reducing_granular_sludge`) using the native guarded writer (`scripts/curate_stage2_causal_graphs.py`) with 0 schema, writer, or validator blockers.
- **Stage 3 (`protein_examples`, PR #1993)**: Added 11 verified UniProt `protein_examples` across those 7 new Cycle 2 Stage 2 graphs (`174` total uses across `139` records, `0` grounding findings) and verified the Cycle 1 Stage 6 offline inventory check (`scripts/audit_uniprot_grounding.py --check-inventory` in `just audit-derived-reports`) operated cleanly without new infrastructure requirements.
- **Stage 4 (`record_review`, PR #1994)**: Reviewed all 1,129 eligible records across 9 domain cohorts (`11` medium-severity `EVIDENCE` findings across 11 records; `0` critical/high findings) with 0 review-infrastructure defects.
- **Stage 5 (`resolve_review_findings`, PR #1996, issue #1995)**: Remediated all 11 Cycle 2 Stage 4 `EVIDENCE` findings via `scripts/curate_stage5_review_findings.py` and verified 0 remaining findings on fresh structured review (`reviews/structured/20261023T161500Z-cycle2-stage5-remediated-records-review/review.yaml`). The Cycle 1 Stage 6 advisory check (`scripts/audit_evidence_snippets.py --check-definition-sources`) passed with `0` `UNQUOTED_DEFINITION_SOURCE` warnings before and after Stage 5 remediation.

Consequently, the supervisor-frozen `INFRA_TASKS.md` inventory at `2026-10-23T18:11:47Z` (`sha256: d6116631e4d3c248b8b05b5b33b6d3a5d4e9f4244eebea5f0a36dd755324eefa`) contains 4 historical Cycle 1 tasks (`traitmech-infra-0001` through `traitmech-infra-0004`), all 4 already in `status: resolved`, and **0 pending (`note`, `open`, or `deferred`) tasks**.

Per the Stage 6 workflow contract (`.claude/skills/traitmech-evolve-workflow/SKILL.md` and `kg_microbe_workflows` `InfrastructurePlan` validation):
- An empty pending intake at the Stage 6 freeze cutoff is recorded as a verified `outcome: no_findings` (`infra_tasks: []`, `carry_forward_ids: []`) rather than inventing artificial infrastructure tasks.
- No new GitHub issues are required because all 4 historical tasks in `INFRA_TASKS.md` already link to verified resolved issues (`#1962`, `#1988`, `#1981`) and 0 pending tasks exist at the cutoff.

---

## 3. Stage 6 Deliverables and Acceptance Criteria

1. **Sync verified Cycle 2 Stage 5 closure index (`reviews/workflow/latest.yaml`)**:
   - Update `reviews/workflow/latest.yaml` from the supervisor-provided `verified-evidence-index.json` to add the verified Cycle 2 Stage 5 closure entry (`reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-05/revision-0001/evidence.yaml`, PR #1996, merge commit `1a00d990f70bab5f11c077fe0c764c1f03ab928b`).
2. **Persist frozen Stage 6 notebook snapshot and plan/validation artifacts (`reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-06/revision-0001/`)**:
   - `infra_snapshot.md`: exact byte match to supervisor-frozen `INFRA_TASKS.md` (`sha256: d6116631e4d3c248b8b05b5b33b6d3a5d4e9f4244eebea5f0a36dd755324eefa`).
   - `implementation_plan.md`: this dependency-aware intake assessment and deliverable specification.
   - `validation.md`: verification report across all repository QC and workflow contract gates.
   - `stage6_coverage_full.json`: machine-readable coverage summary of the frozen `INFRA_TASKS.md` inventory (`4` total tasks, `4` previously resolved, `0` pending at freeze, `0` deferred).
   - `evidence.yaml`: validated `InfrastructurePlan` manifest (`outcome: no_findings`, `infra_tasks: []`, `scope_frozen_at: '2026-10-23T18:11:47Z'`, `source_revision: 1a00d990f70bab5f11c077fe0c764c1f03ab928b`).
3. **Record repository curation/infrastructure history (`history/infrastructure/stage6_infrastructure_plan/`)**:
   - Add an immutable `AUDIT` / `EDIT` history record documenting the Cycle 2 Stage 6 frozen-intake audit and `reviews/workflow/latest.yaml` sync.

---

## 4. Carry-Forward Summary

- **Total tasks in frozen `INFRA_TASKS.md`**: `4` (`traitmech-infra-0001`..`0004`)
- **Previously resolved tasks**: `4` (`traitmech-infra-0001` in PR #1961; `traitmech-infra-0002`, `traitmech-infra-0003`, `traitmech-infra-0004` in PR #1989)
- **Pending tasks at Cycle 2 Stage 6 freeze**: `0`
- **Resolved tasks in Cycle 2 Stage 6**: `0` (`outcome: no_findings`, `infra_tasks: []`)
- **Deferred / blocked tasks carried forward**: `0` (`carry_forward_ids: []`)
