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


