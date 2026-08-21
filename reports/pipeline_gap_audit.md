# Pipeline and writer audit

Source: `scripts/audit_writers.py`, run through:

```bash
just audit-writers
uv run python scripts/audit_writers.py --out /tmp/traitmech-writers.tsv
```

The writer inventory changes as migrations, grounding tools, history tooling,
and research capture are added. Read the live TSV rather than treating a table
in this report as the current inventory.

## Trait-writer contract

A production writer that mutates `data/traits/` should:

- default to a dry run or require an explicit `--apply`/`--write` action;
- append per-record provenance with `record_curation_event`;
- validate and emit through `write_validated_trait`; and
- have focused tests and an appropriate `just` entry point.

The seeder and maintained migration/grounding writers use these shared helpers.
The repository-wide strict validator remains necessary because hand edits and
schema changes do not pass through writer code.

## Interpreting audit rows

The detector intentionally casts a wide net over YAML serialization and file
writes. A flagged script can emit history metadata or research provenance
rather than a `TraitRecord`; read it before applying the trait-writer rubric.
Library helpers can use the narrowly checked `audit-writers: library-helper`
marker, while the auditor excludes its own regex source explicitly.

Do not tune the detector merely to improve percentages. Fix a real trait writer
that lacks a safeguard, provenance, or validation; document a legitimate
non-trait writer when its responsibilities differ.

## Enforcement

- `just qc` runs the writer audit and strict corpus validation.
- `.github/workflows/validate-strict.yaml` prevents schema-invalid records from
  merging on relevant changes.
- Tests cover self-suppression, helper exemptions, and known writer shapes.

After adding or changing a writer, run:

```bash
just audit-writers
just validate-all
just qc
```
