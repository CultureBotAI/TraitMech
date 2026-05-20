---
name: audit-schema-gaps
description: Systematic gap-and-inconsistency audit for the TraitMech LinkML schema, the trait YAML corpus, and the scripts that generate them — produces a re-runnable validation harness, schema + writer audits, and a prioritized fix backlog. Invoke when you suspect schema drift, when records are silently failing validation, after a new seeder/migration pass, or whenever the user asks to "audit the schema", "find data quality issues", or similar.
version: 1.0.0
tags: [validation, linkml, schema, data-quality, audit, qc]
author: TraitMech Team
created: 2026-05-19
---

# Audit schema gaps (schema · instances · pipeline)

## Why this skill exists

TraitMech's default `just validate-all` target runs `linkml-validate` per-file in open-schema mode and swallows non-zero exits — so unknown fields (the most common form of seeder drift) silently pass. Use this skill when you need a strict, all-files-in-one-pass health check, plus structural audits over the schema and the writers that emit YAML.

This skill is the deep counterpart to `schema-gap-analysis` (the lightweight quick-check). Use `schema-gap-analysis` for a ~5-min smoke test; use this one when you suspect systemic drift or before a release.

The skill is built around three orthogonal lenses:

1. **Instance-record validation** — every YAML under `data/traits/**` is validated with `linkml-validate` in *closed* mode (unknown fields rejected). Errors are categorized into a TSV.
2. **Schema audit** — programmatic probes over `src/traitmech/schema/traitmech.yaml` for identifier policy, untyped `string` slots, divergent term-field naming, inconsistent `required:`, orphan enums, and range references to undefined types.
3. **Pipeline / writer audit** — every Python module that writes a YAML is checked for: appends to `curation_history`?, has `--dry-run`?, validates before writing?, wired into a `just` target?

Output is reports under `reports/` plus a re-runnable validation harness at `scripts/validate_strict.py`, all version-controlled.

## When to use

| Trigger | Why |
|---|---|
| User asks to "audit the schema / records / pipeline" | Direct ask. |
| User reports records "silently fail" or "validation passes but the data is wrong" | The signature symptom of open-schema validation. |
| A new seeder/migration is added | Run after to confirm it didn't introduce drift. |
| Schema changes (`src/traitmech/schema/traitmech.yaml` modified) | Refresh the audits against the new schema. |
| You're picking up a TraitMech repo cold and want to know its actual health | The harness gives a single-number answer (`files with ERROR`). |

**Don't** invoke this skill for:
- Single-file validation — use `just validate FILE` directly (open-mode, fast).
- A 5-minute quick check — use the `schema-gap-analysis` skill instead.
- Tweaking a renderer / page template — out of scope.

## Required tooling

All already present in the repo; no new dependencies needed:

- `uv` (Python runner)
- `linkml-validate` CLI **and** `linkml.validator.Validator` Python API (already a dev dep)
- `just` (existing target wrapper)
- Standard `pyyaml`

If `scripts/validate_strict.py` is missing, this skill recreates it from spec (see "Step 1" below).

## Workflow

The skill is a five-step pipeline. Each step produces an artifact; later steps reuse earlier outputs. Re-run independently as needed.

### Step 1 — Strict validation harness

**File:** `scripts/validate_strict.py`
**Just target:** `just validate-strict`

Critical implementation requirements (these are what `just validate-all` gets wrong):

- Use `linkml.validator.Validator` in-process (much faster than subprocess per-file), not the CLI.
- Configure with `JsonschemaValidationPlugin(closed=True)` so unknown fields are flagged. **This is the central correctness requirement.** Without `closed=True`, unexpected-field errors hide.
- Parallel via `ProcessPoolExecutor` with `ncpu - 1` workers; per-worker singleton Validator (init once, validate many).
- Classify each message into a category via narrow regexes:
  - `unexpected_field`, `missing_required`, `enum_mismatch`, `type_mismatch`, `pattern_mismatch`, `format_mismatch`, `range_violation`, and a catch-all `other`.
- TraitMech has a single root class (`TraitRecord`); validate every record against it. (No class-routing needed — unlike CultureMech, which routes between MediaRecipe and SolutionRecipe.)
- Output TSV with columns `file`, `category`, `detail`, `path`, `message`. Use `lineterminator="\n"` to avoid CRLF on macOS.
- Exit code 1 if any ERROR rows; 0 if clean. Don't ever exit 0 on errors.
- Flags: `--sample N`, `--out PATH`, `--workers N`, `--quiet`, `--fail-on=error|never`.

Smoke-test on `--sample 5` before any full-corpus run.

### Step 2 — Full-corpus validation

```bash
just validate-strict
```

Walks every `data/traits/**/*.yaml`. Currently ~357 files; runs in ~10 s on 9 workers.

**Outputs:**
- `reports/instance_validation_failures.tsv` — one row per ERROR.
- Console summary by category.

If the previous run was clean and this one isn't, the recent commits did it. `git log -- data/traits/ src/traitmech/schema/` is your starting point.

### Step 3 — Schema probes

**File:** `scripts/audit_schema.py`
Run: `uv run python scripts/audit_schema.py > /tmp/schema_probes.md`

Probes (all programmatic, no LLM):

| Probe | What it finds |
|---|---|
| Classes without `identifier: true` slot | Descriptors with no stable cross-reference handle. (Sub-objects like `CausalEdge`, `EvidenceItem` are *expected* to lack one; the value is in flagging root-level classes that drop it.) |
| Slots with `range: string` whose name suggests enum/term | Drift opportunities — e.g. `*_mode`, `*_type`, `*_kind`. |
| Term/ontology slot naming divergence | `term_kind` vs `node_id` vs `predicate_id` vs `graph_id` — when they should be uniform. |
| `required: true` inconsistency for analogous attributes | E.g. `evidence` required on `CausalEdge` but optional on `TraitRecord`. |
| Orphan enums (declared but never used as `range:`) | Dead schema. |
| `range:` references to undefined classes/types/enums | Broken schema. |
| Enum casing audit | Mixed UPPER/lower/mixed values within a single enum. |

Hand-compose `reports/schema_gap_audit.md` from the probe output. The composition is the value-add — explaining *why* each finding matters and citing instance counts from Step 2.

### Step 4 — Pipeline / writer audit

**File:** `scripts/audit_writers.py`
Run: `uv run python scripts/audit_writers.py --out reports/pipeline_writers_audit.tsv`

Walks `scripts/` and `src/traitmech/`. For each module that writes YAML (heuristic: `yaml.safe_dump` / `yaml.dump` / `.write_text(` with a `.yaml` path hint), records:

- `appends_curation_history` — regex match on `curation_history.*append` or `record_curation_event` or `'curator':`
- `has_dry_run` — regex match on `--dry-run` or `dry_run\s*[:=]`
- `validates_before_write` — regex match on `linkml-validate` or `TraitValidator` or `validator.validate(`
- `wired_into_just` — filename appears in `justfile`

Hand-compose `reports/pipeline_gap_audit.md` from the TSV. Highlight writers missing safeguards, especially the seeder (`scripts/seed_from_metpo.py`) since it's the only path that creates new trait YAMLs.

**Heads-up false positives**: `audit_writers.py` itself and `render_trait_pages.py` will match the writer heuristic but aren't trait-YAML writers (the auditor reads, the renderer writes HTML). Note in the report rather than re-tune the regex.

### Step 5 — Prioritized fix backlog

Compose `reports/gap_fix_backlog.tsv` (machine-readable) + `reports/gap_fix_backlog.md` (narrative). One row per actionable gap:

| column | example |
|---|---|
| id | G01 |
| category | pipeline / schema / instance |
| title | Add `--dry-run` to seed_from_metpo.py |
| impact | Prevents accidental over-write of curator edits |
| effort | S / M / L |
| suggested_fix_path | `scripts/seed_from_metpo.py` |
| blocking | comma-separated upstream G-ids |

Rank by impact × (1/effort). Group narrative by tier so an implementer can pick the easiest big-wins first. Always lead with **G01: enable the CI gate** — without it, every other fix can regress on the next merge.

## Outputs (the deliverable surface)

```
scripts/
  validate_strict.py        # harness (in-process closed-schema validator)
  audit_schema.py           # schema probes
  audit_writers.py          # writer audit
reports/
  instance_validation_failures.tsv   # one row per ERROR (regenerable)
  instance_validation_summary.md     # human report; counts + drivers
  schema_gap_audit.md                # human report on schema findings
  pipeline_writers_audit.tsv         # writer/script audit (regenerable)
  pipeline_gap_audit.md              # human report on pipeline gaps
  gap_fix_backlog.tsv                # backlog rows
  gap_fix_backlog.md                 # narrative, ranked
justfile
  validate-strict           # new target wrapping the harness
  audit-schema              # convenience target around audit_schema.py
  audit-writers             # convenience target around audit_writers.py
.github/workflows/
  validate-strict.yaml      # CI gate on PRs touching schema or YAMLs (optional)
```

## How to follow up an audit with cleanup

The audit *finds* drift; cleanup fixes it. Typical post-audit work, in dependency order:

1. **CI gate first (G01).** Without it, the rest can regress. Add `.github/workflows/validate-strict.yaml` calling `just validate-strict`.
2. **Bulk field renames** (if instance-axis errors appear). Each is a one-file Python script that mirrors the pattern in the schema-gap-analysis skill: idempotent, appends a `CurationEvent`, supports `--dry-run`.
3. **Schema-shape fixes.** If a finding is "schema is too narrow for real data", broaden the schema (e.g. extend `pattern:` to admit additional CURIE prefixes) rather than migrate the data.
4. **Regenerate dataclasses after schema changes:** `just gen-schema`. Always commit the regenerated file in the same commit as the schema change.
5. **Revalidate.** Re-run `just validate-strict`, confirm the failing count drops, update `reports/instance_validation_summary.md` with before/after numbers.

## Anti-patterns (don't do these)

- **Don't use the existing `just validate-all` to decide if the corpus is clean.** It runs the CLI in open mode and ignores per-file exit codes; it will report success even when records have unknown fields. Use `just validate-strict`.
- **Don't add `# noqa` / try/except blocks around validator results.** If a record fails, the right move is to fix the schema or migrate the data, not silence the failure.
- **Don't pile findings into a single dump.** The split (instance / schema / pipeline / backlog) is so a reader can scan one section at a time.
- **Don't run a full corpus pass when investigating a single regression.** Use `just validate-strict --sample 20` or pass the specific file path.
- **Don't broaden a regex pattern in the schema to "make tests pass" without understanding what the new values mean.** Bake the explanation into the schema description.
- **Don't forget to commit the regenerated `traitmech_dataclasses.py`** alongside any schema change.

## Cross-references

- `reports/instance_validation_summary.md` — the most recent run's full numbers and what's left.
- `reports/gap_fix_backlog.md` — the open items.
- `reports/schema_gap_audit.md` — schema findings with file:line refs.
- `reports/pipeline_gap_audit.md` — writer audit with safeguard table.
- Existing complementary skills:
  - `schema-gap-analysis` — the lightweight version of this skill; ~5 min total.
- Cross-Mech framework + new-Mech bootstrap template: [claw/.claude/skills/schema-gap-analysis](https://github.com/CultureBotAI/culturebotai-claw/blob/main/.claude/skills/schema-gap-analysis/skill.md)

## One-liner runbook

```bash
# Generate everything from a clean repo
just validate-strict                                       # Step 2
uv run python scripts/audit_schema.py > /tmp/probes.md     # Step 3 probes
uv run python scripts/audit_writers.py \
    --out reports/pipeline_writers_audit.tsv               # Step 4 probes

# Then hand-compose schema_gap_audit.md, pipeline_gap_audit.md,
# instance_validation_summary.md, gap_fix_backlog.{tsv,md}
# using the TSVs as evidence.
```
