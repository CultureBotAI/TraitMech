---
name: audit-schema-gaps
description: Canonical TraitMech schema, instance, and writer audit. Uses the repository's maintained strict validator and audit commands, derives all corpus state live, and turns current findings into a prioritized backlog.
version: 2.0.0
tags: [validation, linkml, schema, data-quality, audit, qc]
author: TraitMech Team
created: 2026-05-19
---

# Audit schema gaps

This is the authoritative schema-audit procedure. The older
`schema-gap-analysis` skill is a compatibility pointer to this file; do not
maintain a second set of commands or corpus assumptions there.

## Ground rules

- Treat command output and tracked data as authoritative. Never copy record
  counts, writer lists, cohort versions, or error totals from prose.
- `just validate-all` delegates to the same closed-schema implementation as
  `just validate-strict`; both reject unknown fields and fail on errors.
- Do not reconstruct validators or audit scripts from this document. Inspect
  and use the maintained implementations under `scripts/`.
- `src/traitmech/schema/traitmech_dataclasses.py` is generated and ignored.
  Regenerate it only for a local smoke test; do not commit it.
- Preserve curation provenance. Trait-record mutations require a matching
  history record; follow `history/README.md` and use `just new-history`.

## Quick health check

Run the repository-owned gate first:

```bash
just validate-all
```

For the complete local CI-equivalent quality pass:

```bash
just qc
```

Do not infer health from a previous report. A successful live command is the
current answer.

## Three-axis audit

### 1. Instances

```bash
find data/traits -type f -name '*.yaml' | sort | wc -l
just validate-strict
```

Read `reports/instance_validation_failures.tsv` after the run. Classify and
prioritize current errors by category and affected file count; do not embed the
totals back into this skill.

For a focused investigation, pass the supported arguments shown by:

```bash
uv run python scripts/validate_strict.py --help
```

### 2. Schema

```bash
just audit-schema
```

The maintained audit checks identifier policy, suspicious untyped strings,
term-field naming, requiredness, unused enums, undefined ranges, and enum
casing. Compare live output with `reports/schema_gap_audit.md`; update the
report only when the evidence has changed.

After changing the LinkML schema, run:

```bash
just validate-all
just gen-schema
git status --short --ignored src/traitmech/schema/traitmech_dataclasses.py
```

The last command should show the local generated file as ignored. Delete the
local generated copy when it is no longer useful.

### 3. Writers and process

```bash
just audit-writers
```

Read the generated writer audit instead of assuming which scripts write trait
YAML. Any production writer should:

- require an explicit write action or provide a safe dry run;
- append provenance with `record_curation_event`;
- validate through `write_validated_trait` before replacing a record; and
- have focused tests and an appropriate `just` entry point.

Confirm suspected false positives by reading the writer before changing the
auditor.

## Turning findings into work

Use the current audit outputs to update the schema, pipeline, and backlog
reports under `reports/`. Each actionable item should state its evidence,
impact, effort, target files, dependencies, and verification command. Rank
correctness or provenance loss above cleanup and presentation issues.

When fixing records in bulk, make the transformation idempotent, default to a
dry run or require `--apply`, use the shared write/provenance helpers, scaffold
the required history record, and rerun `just qc`.

## Anti-patterns

- Do not silence validator findings or weaken a schema pattern solely to make a
  gate pass.
- Do not hand-edit generated audit outputs without running their producer.
- Do not present a snapshot count as current repository state.
- Do not bypass `write_validated_trait` or hand-build curation-history entries
  when shared helpers exist.

## Current sources of truth

- `scripts/validate_strict.py`
- `scripts/audit_schema.py`
- `scripts/audit_writers.py`
- `src/traitmech/validation/write_validated.py`
- `src/traitmech/curate/curation_event.py`
- `history/README.md`
- `justfile`

If these disagree with this skill, verify the tests and update the skill in the
same change; executable behavior wins over prose.
