# Schema and writer gap backlog status

The original G01–G05 findings are resolved. This file retains their outcomes so
old references remain understandable without presenting completed work as an
active backlog.

| ID | Status | Resolution |
|---|---|---|
| G01 | RESOLVED | Strict closed-schema validation runs in CI and `just qc`. |
| G02 | RESOLVED | `just validate-all` delegates to `validate-strict`. |
| G03 | RESOLVED | The seeder validates writes through `write_validated_trait`. |
| G04 | RESOLVED | Schema descriptions document the intentional evidence-requiredness asymmetry. |
| G05 | RESOLVED | The writer auditor excludes its own source, with regression coverage. |

There is no active item in this historical backlog. Discover new work from live
commands rather than extending these IDs from an old snapshot:

```bash
just validate-all
just audit-schema
just audit-writers
just qc
```

When a new actionable gap appears, record its command output, impact, effort,
target files, dependencies, and verification command in the repository's
current issue tracker. Do not infer an open task merely because a resolved G-ID
is cited in an older code comment or test name.
