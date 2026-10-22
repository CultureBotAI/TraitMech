# TraitMech infrastructure tasks

This versioned ledger collects repository requirements and upgrades discovered
during every goal. The workflow profile and its parent govern intake, stage 6
implementation, closure and cycle restart.

## Intake protocol

- Give each actionable task a stable ID such as `traitmech-infra-0001` and retain it
  across cycles. Record the originating run, cycle and goal, observation,
  desired outcome, evidence paths, priority, dependencies and status.
- Link each task to an actual issue in https://github.com/CultureBotAI/TraitMech/issues.
  Search existing open and closed issues before creating one. If access fails,
  retain an explicit pending-link blocker; never invent an issue number or URL.
- Preserve resolved and deferred entries with their issue, implementation PR,
  validation and disposition. Do not overwrite previous cycle evidence.
- At stage 6, freeze a bounded snapshot, write a dependency-aware plan and
  acceptance criteria, implement selected work, validate, and complete the
  commit sequence, write the closure receipt and stop; only the supervisor
  dispatches another goal. New arrivals after the cutoff enter the next cycle;
  never expand the frozen task-ID scope. A new blocking prerequisite requires
  an explicit deferred disposition for the selected task. Carry unfinished work
  forward explicitly.

## Machine-readable task inventory

This fenced mapping is the inventory stage 6 freezes and reconciles. Each task
uses `task_id`, `summary`, `status` (`note`, `open`, `deferred`, or `resolved`),
optional `issue_url`, and optional `disposition`. Status `note` may have a
pending issue link; all other statuses require a real issue URL. Keep richer
notes below keyed by the same stable task ID.

<!-- mech-infra-tasks:start -->
```yaml
schema_version: '1.0.0'
tasks:
  - task_id: traitmech-infra-0001
    summary: Replace workstation-absolute paths in .claude/skills/traitmech-evolve-workflow/SKILL.md:213 so pr-sanity and qc pass on clean checkouts
    status: resolved
    issue_url: https://github.com/CultureBotAI/TraitMech/issues/1962
    disposition: Resolved in PR #1961 (minimal blocker for Stage 1 bootstrap PR CI); upstream coordinator template should also emit configurable CLAW_SRC/CLAW_PYTHON and repository-relative paths.
  - task_id: traitmech-infra-0002
    summary: Document or support section-level attaches_to anchors on Discussion entries when target sections (e.g. causal_graphs) are not yet populated
    status: note
    disposition: Recorded during Cycle 1 Stage 2 (causal_graphs) for Stage 6 evaluation; scripts/audit_discussion_anchors.py currently requires <section>#<id> where <id> resolves to an existing item, so record-level causal_graphs gap discussions must omit attaches_to.
  - task_id: traitmech-infra-0003
    summary: Add an offline structural consistency check for reports/uniprot_grounding_audit.tsv in audit-derived-reports so new protein_examples cannot land without refreshing the tracked report
    status: note
    disposition: Recorded during Cycle 1 Stage 3 (protein_examples) for Stage 6 evaluation; reports/uniprot_grounding_audit.tsv was missing 6 Stage 2 protein_examples and had 110 ENTRY_VERSION_MISMATCH rows prior to Stage 3 because audit-derived-reports stays offline and does not verify that every in-corpus protein_examples row is present in the tracked TSV.
  - task_id: traitmech-infra-0004
    summary: Add an optional definition_source evidence-coverage warning to scripts/audit_evidence_snippets.py when a record's definition_source is already quoted in-repo on causal_graphs or parent/sibling records but omitted from record-level evidence
    status: note
    disposition: Recorded during Cycle 1 Stage 4 (record_review) for Stage 6 evaluation; corpus review identified 4 records (cyanophycin_granule, cadmium_tolerant, cobalt_tolerant, zinc_tolerant) whose definition_source is already quoted verbatim in-repo (on causal_graphs edges or parent/sibling records) yet omitted from record-level evidence.
```
<!-- mech-infra-tasks:end -->

## Tasks

### `traitmech-infra-0001` — Replace workstation-absolute paths in `.claude/skills/traitmech-evolve-workflow/SKILL.md:213`
- **Origin**: `mech-goal-sequence-20261019`, Cycle 1, Stage 1 (`add_records`)
- **Issue**: https://github.com/CultureBotAI/TraitMech/issues/1962
- **Implementation PR**: https://github.com/CultureBotAI/TraitMech/pull/1961
- **Status**: `resolved`
- **Observation**: The coordinator-installed `.claude/skills/traitmech-evolve-workflow/SKILL.md` embedded workstation-absolute paths on line 213, failing `scripts/pr_sanity.py` (`ABSOLUTE_REPO_PATH` and `SIBLING_ABSOLUTE_PATH`) and `just qc`.
- **Disposition**: Replaced with configurable `CLAW_SRC` / `CLAW_PYTHON` defaults (`../culturebotai-claw/src` and `../culturebotai-claw/.venv/bin/python`) and repository-relative paths (`workflow/mech-workflow.yaml`, `workflow/parent/mech-cycle.yaml`, `workflow/parent/workflow.yaml`) in PR #1961.

### `traitmech-infra-0002` — Document or support section-level `attaches_to` anchors on `Discussion` entries when target sections are not yet populated
- **Origin**: `mech-goal-sequence-20261019`, Cycle 1, Stage 2 (`causal_graphs`)
- **Status**: `note`
- **Observation**: `src/traitmech/schema/traitmech.yaml` defines `Discussion.attaches_to` as free-form strings, while `scripts/audit_discussion_anchors.py` enforces `<section>#<id>` where `<id>` resolves to an existing element inside `<section>`. When recording a `KNOWLEDGE_GAP` or `CURATION_TODO` explaining why an entire section (`causal_graphs`) is absent due to source-limited single-snippet evidence, `attaches_to: ["causal_graphs"]` fails with `MALFORMED_ANCHOR`.
- **Desired outcome**: In Stage 6, either document the `<section>#<id>` syntax constraint directly on `Discussion.attaches_to` in `src/traitmech/schema/traitmech.yaml` (so curators omit `attaches_to` for whole-record/missing-section gaps) or allow a section-level token when `causal_graphs` is empty.
- **Evidence paths**: `src/traitmech/schema/traitmech.yaml`, `scripts/audit_discussion_anchors.py`, `scripts/curate_stage2_causal_graphs.py`
- **Priority**: Low
- **Dependencies**: None

### `traitmech-infra-0003` — Add an offline structural consistency check for `reports/uniprot_grounding_audit.tsv` in `audit-derived-reports`
- **Origin**: `mech-goal-sequence-20261019`, Cycle 1, Stage 3 (`protein_examples`)
- **Status**: `note`
- **Observation**: `scripts/audit_uniprot_grounding.py` queries the live UniProt REST API, so `reports/uniprot_grounding_audit.tsv` is excluded from `audit-derived-reports` (which must remain offline). As a result, when Stage 2 added 6 new `protein_examples`, `reports/uniprot_grounding_audit.tsv` was not flagged as missing those 6 rows, and 110 `ENTRY_VERSION_MISMATCH` findings had accumulated in the tracked TSV. Stage 3 refreshed all 110 `entry_version` values and regenerated `reports/uniprot_grounding_audit.tsv` (163 uses, 0 findings).
- **Desired outcome**: In Stage 6, add an offline `--check-inventory` mode to `scripts/audit_uniprot_grounding.py` (or a lightweight check in `audit-derived-reports`) verifying that the set of `(file, graph_id, node_id, accession, declared_entry_version, declared_sequence_version)` tuples in `reports/uniprot_grounding_audit.tsv` matches the working-tree `data/traits/` YAML files without making network calls.
- **Evidence paths**: `scripts/audit_uniprot_grounding.py`, `reports/uniprot_grounding_audit.tsv`, `justfile`, `scripts/curate_stage3_protein_examples.py`
- **Priority**: Medium
- **Dependencies**: None

### `traitmech-infra-0004` — Add an optional `definition_source` evidence-coverage warning to `scripts/audit_evidence_snippets.py` when a record's `definition_source` is already quoted in-repo
- **Origin**: `mech-goal-sequence-20261019`, Cycle 1, Stage 4 (`record_review`)
- **Status**: `note`
- **Observation**: During Stage 4 frozen-inventory review of all 1,129 eligible records, 4 records (`data/traits/morphology/cyanophycin_granule.yaml`, `data/traits/environment/cadmium_tolerant.yaml`, `data/traits/environment/cobalt_tolerant.yaml`, and `data/traits/environment/zinc_tolerant.yaml`) were found to declare a primary `definition_source` (`DOI:10.1128/AEM.01298-18` or `PMID:12829273`) that already has a verified verbatim quote in-repo (on the record's own `causal_graphs` edges or on parent/sibling records `metal_tolerant.yaml`/`mercury_tolerant.yaml`) while omitting that reference from record-level `evidence`.
- **Desired outcome**: In Stage 6, add an advisory check in `scripts/audit_evidence_snippets.py` flagging records whose `definition_source` is absent from `evidence[].reference` whenever `definition_source` already has a verified verbatim snippet in the repository (either on `causal_graphs` edges or on sibling/parent records).
- **Evidence paths**: `scripts/audit_evidence_snippets.py`, `reviews/structured/20261022T033000Z-stage4-corpus-record-and-cohort-review/review.yaml`, `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-04/revision-0001/evidence.yaml`
- **Priority**: Low
- **Dependencies**: Stage 5 (`resolve_review_findings`) remediation of `F-DEF-SRC-CYANOPHYCIN-001`..`004`


