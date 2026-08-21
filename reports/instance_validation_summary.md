# Instance validation summary

Trait records are validated in process with
`JsonschemaValidationPlugin(closed=True)`, so unknown fields are errors. Both
public entry points use the same implementation:

```bash
just validate-all
just validate-strict
```

The validator discovers `data/traits/**/*.yaml` on each run and writes current
errors to `reports/instance_validation_failures.tsv`. Use its console summary
for the live file and error counts; this narrative intentionally does not copy
those volatile values.

## Enforcement

- `.github/workflows/validate-strict.yaml` runs strict validation for relevant
  pull requests and pushes to `main`.
- `just qc` includes `validate-strict`.
- Production trait writers use `write_validated_trait`, which rejects invalid
  in-memory records before replacing files.

These layers complement one another: write-time validation prevents new drift,
while corpus validation catches hand edits, schema changes, and older records.

## What structural validation does not prove

A schema-valid trait can still be semantically wrong. Validation does not prove
that an ontology identifier names the intended concept, a citation supports a
claim, a causal edge has the correct direction, or a graph is complete. Use the
grounding, evidence, and graph audits in `just qc`, followed by curator review.

## Focused reproduction

```bash
just validate-strict --sample 20
just validate-strict data/traits/physiology
```

The TSV columns are `file`, `category`, `detail`, `path`, and `message`. When
errors exist, group by `category` to distinguish schema drift, missing required
fields, and invalid value shapes.
