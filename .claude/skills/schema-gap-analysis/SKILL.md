---
name: schema-gap-analysis
description: Compatibility entry point for TraitMech schema-gap requests. Routes to the canonical audit-schema-gaps skill so validation commands and repository assumptions stay in one maintained place.
category: quality
requires_database: false
requires_internet: false
version: 3.0.0
---

# Schema gap analysis

Use [`audit-schema-gaps`](../audit-schema-gaps/SKILL.md) for the complete and
authoritative procedure. This alias remains so older prompts still resolve,
but it intentionally contains no duplicate audit logic or repository snapshot.

For a quick current-state check:

```bash
just validate-all
```

For all maintained schema, instance, writer, and repository quality checks:

```bash
just qc
```

Read live command output and the artifacts those commands regenerate. Do not
infer corpus size, writer coverage, or validation status from prose.
