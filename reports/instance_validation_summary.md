# Instance validation summary

Run: `just validate-strict` (in-process `linkml.validator.Validator` with `JsonschemaValidationPlugin(closed=True)`).

| Metric | Count |
|---|---|
| Files scanned (`data/traits/**/*.yaml`) | 357 |
| Files with ERROR | **0** |
| Total ERROR rows | **0** |
| TSV | `reports/instance_validation_failures.tsv` |

## Reading

The corpus passes strict, closed-schema validation against `src/traitmech/schema/traitmech.yaml::TraitRecord`. No unknown fields, no missing required attributes, no enum/pattern violations, no parse errors.

This is a stronger signal than `just validate-all` provides — that target runs the CLI in open mode and swallows non-zero exits, so it reports "success" even when records contain unknown keys. The fact that strict mode is also clean means the seeder is currently emitting records that the schema accepts as written.

## What this run does not tell us

- **It only validates structure, not content.** A trait can be schema-valid and still semantically wrong (e.g., wrong METPO term, wrong polarity on a causal edge). Validation guarantees nothing about correctness of references or causal claims.
- **It will regress silently without a CI gate.** Nothing today blocks a PR that introduces a schema-breaking record. See backlog item G01.
- **The seeder doesn't validate its output before writing.** Today this happens to be fine because the schema and the seeder template are in sync. If either drifts, the first signal will be a manual `just validate-strict` run — by which point unvalidated records have already been committed. See backlog item G03.

## Reproduce

```bash
just validate-strict                          # full corpus
just validate-strict --sample 20              # smoke test
just validate-strict data/traits/physiology   # one category
```

The TSV (`reports/instance_validation_failures.tsv`) carries columns `file`, `category`, `detail`, `path`, `message`. When the corpus has errors, sort/filter on `category` to see whether the failure mode is schema-drift (`unexpected_field`), required-attribute drift (`missing_required`), or value-shape (`enum_mismatch`, `pattern_mismatch`).
