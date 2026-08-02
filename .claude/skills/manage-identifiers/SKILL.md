---
name: manage-identifiers
description: TraitMech identifier policy and workflow — METPO-first by default, with a reserved `traitmech:NNNNNN` prefix for synthetic traits that aren't in METPO. Covers looking up the right ID, minting a fallback when needed, and validating ID hygiene across the corpus.
category: workflow
requires_database: false
requires_internet: false
version: 1.0.0
tags: [identifiers, metpo, ontology, curation]
author: TraitMech Team
created: 2026-05-19
---

# Identifier Management for TraitMech

## Identifier policy (read this first)

**TraitMech is METPO-first.** Every seeded trait carries the **upstream METPO CURIE** as its `identifier`, e.g.:

```yaml
identifier: METPO:1000430
label: GC mid1
```

The schema captures this explicitly:

```yaml
# src/traitmech/schema/traitmech.yaml
identifier:
  description: >-
    Stable CURIE for this trait. Seeded records use the METPO CURIE
    directly (e.g. METPO:1000331). Curator-minted records may use
    the `traitmech:` prefix.
  identifier: true
  required: true
```

There is no TraitMech-side sequential numbering for the seeded majority — IDs come from the upstream ontology. The minted-ID workflow exists only as a fallback for synthetic traits that don't yet have a METPO term.

This is the inverse of CultureMech / MediaIngredientMech / CommunityMech, all of which mint their own `<RepoName>:NNNNNN` sequential IDs. If you're coming from one of those repos, **don't reach for the minting workflow first** — almost every TraitMech change should pick up the existing METPO CURIE.

## When to use this skill

| Trigger | Decision |
|---|---|
| Re-seeding from a new METPO release | Use the METPO CURIE directly. No minting. |
| Adding an organism-level trait that exists in METPO | Look up the METPO CURIE; use that as `identifier:`. |
| Adding a trait that **does not yet exist** in METPO | Two options. Prefer (1): file a METPO ticket so the trait gets an upstream ID. Fall back to (2): mint `traitmech:NNNNNN` and document the gap. |
| Validating that no two trait YAMLs share an identifier | Use the duplicate-check snippet below. |
| Curating a renamed METPO term | Keep the old METPO CURIE in `identifier:`; add the new label to `synonyms:`. Identifiers don't change. |

## Looking up the right METPO CURIE

METPO is mirrored at `data/raw/metpo.owl`. To find a CURIE for a trait you want to add:

```bash
# Search the OWL for a label
grep -B2 "rdfs:label.*\"YOUR_TRAIT_HERE\"" data/raw/metpo.owl | head

# Or scan already-seeded traits for similar concepts
grep -rh "label:" data/traits/ | grep -i "YOUR_TRAIT_HERE"
```

For the `definition`, `synonyms`, and other slots, the seeder (`scripts/seed_from_metpo.py`) is the canonical source — re-running the seed pulls every change METPO has accepted upstream.

## Minting `traitmech:NNNNNN` (fallback path)

Only when METPO truly has no matching term and the curator wants to record the trait now rather than wait on the upstream PR.

### 1. Find the next available number

```bash
# Highest existing traitmech: number across all trait YAMLs
grep -rh "^identifier: traitmech:" data/traits/ \
  | awk -F: '{print $NF}' \
  | sort -n | tail -1
# (no output = 000000 is free; mint 000001)
```

Or in Python:

```python
import re
from pathlib import Path

max_id = 0
for yaml_file in Path("data/traits").rglob("*.yaml"):
    text = yaml_file.read_text()
    for m in re.finditer(r"^identifier:\s*traitmech:(\d+)", text, re.MULTILINE):
        max_id = max(max_id, int(m.group(1)))
print(f"Next traitmech ID: traitmech:{max_id + 1:06d}")
```

### 2. Hand-author the YAML

Place the new file under the appropriate `data/traits/<category>/` directory. Categories:

```
ecology, environment, genomics, metabolism,
morphology, observation, physiology,
quantitative_property, upper
```

Minimum-viable shape:

```yaml
identifier: traitmech:000001          # Six-digit zero-padded
label: <your trait label>
definition: >-
  <one-or-two-sentence definition>
definition_source: DOI:10.xxxx/yyy    # Citation or "curator-supplied"
trait_category: PHYSIOLOGY            # Must match a TraitCategoryEnum value
synonyms: []
evidence: []                          # PMID:/DOI: refs supporting the trait
curation_history:
  - timestamp: '2026-05-19T00:00:00+00:00'
    curator: <your name or handle>    # match an existing convention: seed_from_metpo, codex, or your name
    action: MINTED_TRAITMECH_ID
    changes: 'METPO has no matching term yet; tracked in METPO issue #N'
    llm_assisted: false
```

The `CurationEvent` schema only permits `timestamp`, `curator`, `action`, `changes`, and `llm_assisted` — no free-text `notes:` slot. If you want to add free-form prose, use `changes:`.

### 3. Validate

```bash
just validate path/to/new_trait.yaml      # single file, open mode
just validate-strict path/to/new_trait.yaml  # closed mode (rejects unknown fields)
```

### 4. Open a METPO upstream ticket

The minted `traitmech:` ID is meant to be **temporary**. File a METPO issue so the term gets a real ontology home; once upstream lands, re-seed and migrate the YAML's `identifier:` to the METPO CURIE (keep the old `traitmech:` in `synonyms:` so external references don't break).

## Validation snippets

### Duplicate-identifier check (full corpus)

```bash
grep -rh "^identifier:" data/traits/ \
  | sort | uniq -c | sort -rn | awk '$1 > 1'
# Empty output = no duplicates
```

### Identifier-shape check (must be CURIE)

```bash
grep -rh "^identifier:" data/traits/ \
  | awk '{print $2}' \
  | grep -vE '^[A-Za-z][A-Za-z0-9._-]*:[A-Za-z0-9._-]+$'
# Empty output = every identifier is a well-formed CURIE
```

### Prefix-distribution audit

```bash
grep -rh "^identifier:" data/traits/ \
  | awk -F: '{print $2}' \
  | sort | uniq -c | sort -rn
# Expected today:
#   357  METPO
#     0  traitmech    (target: keep low; each one means an upstream gap)
```

## Anti-patterns

- **Don't mint a `traitmech:NNNNNN` ID for a trait that already exists in METPO.** Look it up first. Run a search across `data/raw/metpo.owl` or `data/traits/` for the label / synonym before minting.
- **Don't change an existing `identifier:` value.** Identifiers are stable. If a trait's *meaning* drifts, deprecate the old record and create a new one with a new identifier. If only the *label* changes, edit `label:` / `synonyms:` and leave `identifier:` alone.
- **Don't backfill `traitmech:` over `METPO:`** when re-seeding. The seeder is the source of truth for METPO-mapped traits; never overwrite a METPO CURIE with a TraitMech-minted one.
- **Don't use a sequential number that collides with an in-flight METPO ID range.** METPO uses 7-digit numerics (`METPO:1000430`); TraitMech-minted IDs use 6-digit zero-padded under the `traitmech:` prefix to avoid any visual collision.

## Cross-references

- Schema: `src/traitmech/schema/traitmech.yaml` — `TraitRecord.identifier` slot.
- Seeder: `scripts/seed_from_metpo.py` — the canonical METPO → YAML pipeline.
- Audit skills: [`schema-gap-analysis`](../schema-gap-analysis/SKILL.md) (quick check) and [`audit-schema-gaps`](../audit-schema-gaps/SKILL.md) (deep audit). Both run `linkml-validate` over `data/traits/` and will surface any malformed identifier as `pattern_mismatch` or `missing_required` errors.
- Cross-Mech reference (for repos that *do* mint their own IDs): [CultureMech's manage-identifiers](https://github.com/CultureBotAI/CultureMech/blob/main/.claude/skills/manage-identifiers/SKILL.md) — covers single-file collection, multi-file collection, registry workflows, and batch ID assignment.
