---
name: manage-identifiers
description: TraitMech identifier policy and workflow — METPO-first by default, with a reserved `traitmech:NNNNNN` prefix for accepted traits lacking an active exact METPO term. Covers active and deprecated matches, fallback minting, and corpus identifier hygiene.
category: workflow
requires_database: false
requires_internet: true
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

There is no TraitMech-side sequential numbering for the seeded majority: IDs
come from the upstream ontology. The minted-ID workflow exists only as a
fallback for accepted traits that do not have an active exact METPO term. A
deprecated historical match requires the assessment below; it is not automatic
permission to mint or reactivate an ID.

This is the inverse of CultureMech / MediaIngredientMech / CommunityMech, all of which mint their own `<RepoName>:NNNNNN` sequential IDs. If you're coming from one of those repos, **don't reach for the minting workflow first** — almost every TraitMech change should pick up the existing METPO CURIE.

## When to use this skill

| Trigger | Decision |
|---|---|
| Re-seeding from a new METPO release | Use active METPO CURIEs directly. Preserve the seeder's deprecated-term exclusion. |
| Adding an organism-level trait with an active exact match in METPO | Look up the METPO CURIE; use that as `identifier:`. |
| Finding only deprecated historical matches | Assess status, replacements and scope below; do not reuse or reactivate a deprecated CURIE for a new record. |
| Adding an accepted trait with no active exact METPO match | Complete the historical-match assessment if applicable, mint `traitmech:NNNNNN`, add a same-PR METPO ROBOT-template proposal, and document the round-trip path. Reference any pre-existing upstream METPO issue, but do not use an issue link instead of the proposal artifact. |
| Validating that no two trait YAMLs share an identifier | Use the duplicate-check snippet below. |
| Curating a renamed active METPO term | Keep its METPO CURIE. A label change alone does not change identity; deprecation or replacement requires a separate migration assessment. |

## Looking up the right METPO CURIE

METPO is mirrored at `data/raw/metpo.owl`. Search lexical variants as well as
the requested label; historical labels may be prefixed with `obsolete ` (for
example, `obsolete sliding`). These are search leads, not exact mappings.

```bash
# Find lexical leads, including ignored and hidden files
rg --no-ignore --hidden -n -i 'YOUR_TRAIT_HERE' data/raw/metpo.owl data/traits history proposals
```

Inspect candidate subjects with an RDF parser, not a label-only grep. For each
exact candidate CURIE, preserve its full numeric spelling, including leading
zeros, and inspect its own `owl:deprecated` and related annotations:

```bash
.venv/bin/python - <<'PY'
from rdflib import Graph, OWL, RDF, RDFS, URIRef

curie = "METPO:1000388"  # Replace with the candidate being assessed.
term = URIRef("https://w3id.org/metpo/" + curie.split(":", 1)[1])
graph = Graph().parse("data/raw/metpo.owl")
for predicate in (
    RDF.type,
    RDFS.label,
    URIRef("http://purl.obolibrary.org/obo/IAO_0000115"),  # definition
    OWL.deprecated,
    URIRef("http://purl.obolibrary.org/obo/IAO_0000231"),  # obsolescence reason
    URIRef("http://purl.obolibrary.org/obo/IAO_0100001"),  # term replaced by
    URIRef("http://www.geneontology.org/formats/oboInOwl#consider"),
):
    print(predicate, list(graph.objects(term, predicate)))
PY
```

An active exact match must have the right class/property kind and biological
scope, not just the same label. Resolve any `IAO:0100001` replacement's own
status and meaning before using it; a `consider` suggestion does not assert
equivalence. Follow replacement chains without treating a cycle, missing
target, several alternatives or a broader successor as a resolved exact match.

For deprecated-only matches, inspect the obsolescence rationale and current
upstream ontology/issues without silently replacing the pinned mirror. Reason
codes may themselves be disputed (for example,
[METPO #521](https://github.com/berkeleybop/metpo/issues/521)); do not infer that
the biology is invalid, reactivate an ID, or mint a duplicate from the label or
reason code alone. If scope or replacement identity remains unresolved, keep
the candidate in research. Document the exact historical IDs, status,
replacements, rationale and unresolved questions in research notes. If the
candidate is independently accepted as evidence-backed and in scope without
an active exact replacement, carry that assessment into the new record's
`discussions` and proposal before completing the usual novelty and reservation
checks. Do not put historical IDs in exact `xrefs` (#1874).

For active terms, the seeder (`scripts/seed_from_metpo.py`) projects definitions,
synonyms and other slots from the pinned `data/raw/metpo.owl`; it does not fetch
unreleased upstream changes. It deliberately skips deprecated terms. An empty
seed target does not justify hand-creating a record with a retired identifier.

## Minting `traitmech:NNNNNN` (fallback path)

Only when METPO has no active exact match, any historical matches have been
assessed above, and the trait has independently passed the add-trait scope,
evidence and novelty checks. Every new fallback ID
must be paired with a `proposals/metpo_traitmech_v<N>/` cohort in the same PR
that reserves the proposed `METPO:` placeholder.

### 1. Find a candidate, then check reservations

```bash
# Highest live traitmech: number in this checkout, not a global reservation
rg --no-ignore --hidden -o "^identifier: traitmech:[0-9]{6}" data/traits/ \
  | awk -F: '{print $NF}' \
  | sort -n | tail -1
# No output only means this checkout has no live fallback IDs.
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
print(f"Candidate requiring reservation checks: traitmech:{max_id + 1:06d}")
```

Before assigning that candidate, check current main, local worktrees, and every
relevant open PR, including drafts. A clean checkout can omit in-flight IDs,
cohort names and whole reserved METPO blocks (#1785).

```bash
git fetch origin main
git worktree list --porcelain
gh api --paginate 'repos/CultureBotAI/TraitMech/pulls?state=open&per_page=100' \
  --jq '.[] | [.number, .head.sha, .head.ref] | @tsv'
```

Inspect each PR's paginated changed-file list to identify trait/proposal
changes; do not filter only by its title. Read the affected YAML, proposal TSVs
and narratives at the reported head SHA, without switching another worktree.
Check local worktrees' records, history and proposals with ignored-and-hidden
searches as well. Treat published in-flight reservations as occupied even when
the record is not on main, and account for the entire declared block, not just
populated rows. Historical IDs are not freed by an absent live YAML file.

Record the allocation evidence and relevant PR numbers in the new proposal.
Recheck main and open PR heads immediately before publishing; this narrows but
does not eliminate concurrent-allocation races. If remote reservation state is
unavailable, continue research but do not claim a candidate is free or publish
a new allocation until checked. Resolve any detected collision before merge.

### 2. Write the YAML

Place the new file under the appropriate `data/traits/<category>/` directory. Categories:

```
ecology, environment, genomics, metabolism,
morphology, observation, physiology,
quantitative_property, upper
```

Build the record in Python and write it through `write_validated_trait`; do not
hand-serialize YAML. Minimum-viable shape:

```yaml
identifier: traitmech:000001          # Six-digit zero-padded
label: <your trait label>
definition: >-
  <one-or-two-sentence definition>
definition_source: DOI:10.xxxx/yyy    # DOI, PMID, or stable URL citation
trait_category: PHYSIOLOGY            # Must match a TraitCategoryEnum value
term_kind: CLASS
mapping_status: PROPOSED
synonyms: []
evidence: []                          # DOI/PMID/stable-URL refs supporting the trait
curation_history:
  - timestamp: '2026-05-19T00:00:00+00:00'
    curator: <your name or handle>    # match an existing convention: seed_from_metpo, codex, or your name
    action: MINTED_TRAITMECH_ID
    changes: 'No active exact METPO match after identity assessment; reserved in proposals/metpo_traitmech_v<N>'
    llm_assisted: false
```

The `CurationEvent` schema only permits `timestamp`, `curator`, `action`, `changes`, and `llm_assisted` — no free-text `notes:` slot. If you want to add free-form prose, use `changes:`.

### 3. Validate

```bash
just validate path/to/new_trait.yaml      # single file, open mode
just validate-strict path/to/new_trait.yaml  # closed mode (rejects unknown fields)
```

### 4. Add a METPO proposal

The minted `traitmech:` ID is meant to be **temporary**. Add or extend a
`proposals/metpo_traitmech_v<N>/` cohort in the same PR so the term has a real
upstream ontology home reserved. If a separate METPO issue already exists,
reference it from the proposal narrative; otherwise the ROBOT template plus
round-trip plan is the review artifact. Once upstream lands, re-seed and migrate
the YAML's `identifier:` to the METPO CURIE while preserving the old
`traitmech:` CURIE for traceability.

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
# Interpret the live distribution. Each traitmech entry represents an
# intentional upstream gap and should carry provenance for that decision.
```

## Anti-patterns

- **Don't mint a `traitmech:NNNNNN` ID for a trait with an active exact METPO match.** Search labels and synonyms, then check status, kind and scope. Deprecated-only matches require the assessment above, not automatic reuse or fallback.
- **Don't change an existing `identifier:` value.** Identifiers are stable. If a trait's *meaning* drifts, deprecate the old record and create a new one with a new identifier. If only the *label* changes, edit `label:` / `synonyms:` and leave `identifier:` alone.
- **Don't backfill `traitmech:` over `METPO:`** when re-seeding. The seeder is the source of truth for METPO-mapped traits; never overwrite a METPO CURIE with a TraitMech-minted one.
- **Don't infer namespace or availability from digit width.** Historical METPO IDs include six-digit numeric suffixes such as `METPO:000097`, as well as seven-digit forms. The full CURIE, including its prefix and unchanged local ID, determines identity; matching numeric suffixes in different namespaces are not identifier collisions. Preserve leading zeros and check each candidate CURIE, cohort and entire reserved METPO block through the reservation workflow above (#1876).

## Cross-references

- Schema: `src/traitmech/schema/traitmech.yaml` — `TraitRecord.identifier` slot.
- Seeder: `scripts/seed_from_metpo.py` — the canonical METPO → YAML pipeline.
- Schema audit: [`audit-schema-gaps`](../audit-schema-gaps/SKILL.md) is the
  canonical procedure and surfaces malformed identifiers as
  `pattern_mismatch` or `missing_required` errors.
- Cross-Mech reference (for repos that *do* mint their own IDs): [CultureMech's manage-identifiers](https://github.com/CultureBotAI/CultureMech/blob/main/.claude/skills/manage-identifiers/SKILL.md) — covers single-file collection, multi-file collection, registry workflows, and batch ID assignment.
