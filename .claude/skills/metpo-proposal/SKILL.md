---
name: metpo-proposal
description: Generate a ROBOT-template METPO proposal that lifts TraitMech synthetic traits, causal-graph scaffolding, and schema-side controlled vocabularies into METPO classes and predicates. Use when a curator-minted `traitmech:NNNNNN` ID needs a METPO home, when a causal predicate (`CausalEdge.predicate_id`) has no upstream IRI, or when a TraitMech schema enum should become first-class METPO vocabulary.
category: workflow
requires_database: false
requires_internet: false
version: 1.1.0
tags: [metpo, ontology, robot, linkml, proposal, schema-lift, kg-microbe, traitmech]
---

# METPO Proposal Skill (TraitMech)

## Overview

TraitMech is a **consumer** of METPO: all 357 current trait records carry
`METPO:` identifiers seeded from `data/raw/metpo.owl`. This skill produces the
**reverse-direction** artifact — a ROBOT-template proposal that asks METPO to
adopt classes/predicates that originated locally in TraitMech, so that future
seeds round-trip without `traitmech:` fallback IDs.

Up to four artifacts are produced under `proposals/<cohort-name>/`:

| File | Format |
|---|---|
| `metpo_proposal_classes_robot.tsv` | 11-column ROBOT template (mirrors kg-microbe convention) |
| `metpo_proposal_properties_robot.tsv` | 12-column ROBOT template |
| `metpo_proposal_mappings.sssom.tsv` | SSSOM mapping set — cross-ontology equivalents with `skos:exactMatch`/`closeMatch`/`narrowMatch` and match confidence. **Optional**: emit only when ≥1 proposed term aligns to an existing OMP/MICRO/PATO/GO/CHEBI/… class. See "Cross-ontology equivalents are mappings, not definition_source" in [`reference/conventions.md`](reference/conventions.md). |
| `proposal.md` | Reviewer narrative: scope, hierarchy decisions, predicate rationale, verification, upstream path |

**Run from `TraitMech/` directory.** Cross-Mech references:
- CultureMech/CommunityMech analogue: `CommunityMech/.claude/skills/metpo-proposal/SKILL.md` and reference cohort `proposals/metpo_communitymech_v1/`.
- Upstream contract: `kg-microbe/.claude/skills/metpo-proposal/SKILL.md` — the canonical METPO-side rules (Aristotelian definitions, citation forms, family-aware ID slotting, paired predicate convention).

---

## When to use this skill

TraitMech-specific triggers. Each maps to one of three legitimate proposal scopes.

### Scope A — Synthetic trait class lift (most common)

A curator has minted a `traitmech:NNNNNN` ID for a trait that doesn't yet
exist in METPO (per `manage-identifiers` skill, fallback path). Until that
trait has an upstream METPO ID it can't be cross-referenced from kg-microbe.
Lift it via this skill so METPO maintainers can mint the real ID.

To find candidates:

```bash
grep -rh "^identifier: traitmech:" data/traits/ | sort -u
```

If that command returns nothing, no Scope A work is pending.

### Scope B — Causal-graph predicate lift (rare)

A `CausalEdge.predicate_id` in some trait YAML uses an opaque label without a
CURIE grounding because no RO / OBO / METPO predicate fits the mechanism. If
the mechanism is general enough to appear in multiple traits, propose a new
METPO predicate. **Prefer RO/OBI first** — only propose a METPO predicate
when the relation is microbe-trait-specific.

To find candidates:

```bash
# Edges that have a description but no predicate_id grounding
uv run python -c "
import yaml, pathlib
for p in pathlib.Path('data/traits').rglob('*.yaml'):
    doc = yaml.safe_load(p.read_text())
    for g in (doc.get('causal_graphs') or []):
        for e in (g.get('edges') or []):
            if not e.get('predicate_id') and e.get('predicate'):
                print(f'{p}:{e[\"predicate\"]}')" | sort -u | head -50
```

### Scope C — Schema enum lift (one-off; do not lift workflow-internal enums)

The TraitMech schema declares 6 enums. **Only one is a legitimate METPO-lift
candidate today:**

| enum | scope C lift? | reason |
|---|---|---|
| `TraitCategoryEnum` | **no** | Filesystem layout discriminator; not a real ontology axis. |
| `TermKindEnum` | **no** | OWL meta-axis (Class vs DatatypeProperty); not a domain concept. |
| `SynonymTypeEnum` | **no** | Already a standard OBO axis (`oboInOwl:hasExactSynonym` etc.); use upstream conventions. |
| `PriorityEnum` | **no** | Editorial workflow knob. |
| `MappingStatusEnum` | **no** | Internal lifecycle flag. |
| `CausalNodeTypeEnum` | **yes** | A controlled vocabulary for causal-graph nodes; would let consumers filter traits by mechanism axis (e.g. "all traits with `MOLECULAR_FUNCTION` nodes"). |

Do NOT batch the no-lift enums into a proposal "for completeness". The METPO
maintainers will reject anything that's a workflow concept, and rightly so.

Do NOT use this skill for: lifting PATO/GO/CHEBI cross-references (already
upstream), lifting tolerance ranges or paired chemical-interaction
predicates (use the upstream
[kg-microbe metpo-proposal skill](../../../../kg-microbe/.claude/skills/metpo-proposal/SKILL.md)
which handles the paired positive/negative convention).


---

## Required reading & conventions

Before generating a proposal, read the upstream contract and templates, and internalise the
ROBOT column structure and the citation-vs-mapping rule (issue #83) — all in
[`reference/conventions.md`](reference/conventions.md):

- **Required reading** — the upstream `kg-microbe` metpo-proposal SKILL.md (Aristotelian
  definitions, `definition_source` citation forms, family-aware ID slotting, the 12-point
  checklist, paired-predicate convention), the canonical 11/12-column ROBOT templates, the
  most recent worked cohort, and TraitMech's `manage-identifiers` allocation policy.
- **ROBOT template column conventions** — tab-separated, two header rows, trailing tabs on
  the ROBOT header to reach full column count.
- **Cross-ontology equivalents are mappings, not `definition_source`** — an ontology IRI in
  column 4 is a bug; emit alignments in `xrefs` (loose hint) and
  `metpo_proposal_mappings.sssom.tsv` (`skos:*Match` with strength).
---

## ID-space conventions

TraitMech proposes into the **`METPO:1007400+` and `METPO:2007400+` placeholder
ranges**, chosen to leave clear daylight above the CommunityMech v1 cohort
(which occupies `1007100`–`1007220` and `2007100`–`2007113`).

| Range | Use |
|---|---|
| `METPO:1000000` | METPO root (only as `SC %` parent when no closer parent exists) |
| `METPO:1000525` | "microbe" — DOMAIN for predicates whose subject is a microbial taxon |
| `METPO:1007400`–`METPO:1007499` | **Placeholder** range for TraitMech class proposals (cohort v1 starts here) |
| `METPO:2007400`–`METPO:2007499` | **Placeholder** range for TraitMech predicate proposals |

Within `1007400`–`1007499`, allocate contiguous numeric blocks per scope so
the file scans easily. Suggested v1 layout:

- `1007400`–`1007404` — top-level domain classes (`trait causal graph`, `trait causal node`, `trait causal edge`, optional)
- `1007410`–`1007429` — `CausalNodeTypeEnum` lift (Scope C): enum-parent + 10 leaves
- `1007430`–`1007499` — Scope-A synthetic trait classes (one per `traitmech:NNNNNN` row found in the corpus at audit time)

Future cohorts should pick a fresh block starting at `1007500+` and document
the new block in their `proposal.md`. **Never reuse a block from a merged
cohort, even if rows in the old block were rejected upstream.**

For Scope-B predicates, use `2007400+` and follow the
[kg-microbe SKILL.md paired predicate convention](../../../../kg-microbe/.claude/skills/metpo-proposal/SKILL.md#paired-predicates-positive--negative-via-shared-synonym)
only when the predicate is truly paired (microbe ↔ chemical capability). Most
causal-graph predicates are unidirectional and should NOT be paired.

### Collision check before minting

```bash
# Ensure your proposed block doesn't overlap any other Mech's cohort
grep -E "METPO:100(7[0-9]{3}|6[0-9]{3})" data/raw/metpo.owl | head
```

If the upstream METPO release has already minted IDs in `1007400+`, bump to
the next free block.

---

## Subset tag

Every row must carry the same `oboInOwl:inSubset` value in column 8 (classes)
or column 9 (properties). Format: `metpo_traitmech_<YYYY>_<MM>`.

Examples:
- `metpo_traitmech_2026_05` — initial TraitMech cohort (v1)
- `metpo_traitmech_2026_07` — hypothetical v2 cohort after a breaking change

Each new cohort directory gets a new subset tag. **Extending in place (Path B
below) keeps the same tag** — the tag identifies the cohort, not the round
of additions.

---

## Workflow

### 1. Pick the scope

Audit which of A / B / C apply for this cohort. Run the search commands in
the "When to use this skill" section and record counts in `proposal.md`'s
Scope section. **If all three counts are zero, abort — there's nothing to
propose.**

Write a one-line statement of why each candidate belongs in METPO:

- **Scope A** answer: "This trait was minted as `traitmech:NNNNNN` on
  `<date>` because METPO had no equivalent; it has been used in `N` trait
  records since."
- **Scope B** answer: "This predicate appears in `N` causal edges across `M`
  trait records; no RO/OBI relation fits because `<reason>`."
- **Scope C** answer: "This enum is referenced by `N` trait records via
  `<slot>`; lifting it to METPO lets downstream consumers query along the
  same axis."

If the answer is "because it's in the schema", reconsider — METPO is a
curated ontology, not a schema dump.

### 2. Design the hierarchy

#### Scope A (synthetic traits)

- **Parent**: read the original `traitmech:` record's `parent_classes:` slot;
  use the closest existing METPO class as the proposal's `SC %` parent.
  Never `SC METPO:1000000` directly for a Scope-A row unless the trait is
  genuinely top-level.
- **Label**: copy from the record's `label:` slot verbatim.
- **Definition**: rewrite the record's `description:` in Aristotelian form
  (`<genus>: <differentia>`). The original prose usually needs tightening.
- **Synonyms**: copy from `synonyms:` (only `EXACT_SYNONYM` entries — drop
  `BROAD_SYNONYM` / `NARROW_SYNONYM` per OBO convention since ROBOT writes
  only `hasExactSynonym` here).
- **Definition source**: cite the curation event that minted the
  `traitmech:` ID — `TraitMech:data/traits/<category>/<slug>.yaml` plus the
  curator name from `curation_history`. If the record cites a PMID/DOI,
  include both (`SPLIT=|`). **Citations only** — if the trait aligns to an
  existing OMP/MICRO/PATO/GO class, that goes in `xrefs` + the SSSOM mappings
  file, never here (see "Cross-ontology equivalents are mappings" in [`reference/conventions.md`](reference/conventions.md)).

#### Scope B (causal predicates)

- **Domain**: usually `METPO:1007402` (trait causal node) or a more specific
  upstream class.
- **Range**: another causal-node class, or an existing METPO/CHEBI/GO IRI if
  the predicate connects to an external concept.
- **Definition**: Aristotelian — `<genus relation>: <distinguishing
  feature>`.
- **Definition source**: any trait record whose causal graph uses this
  predicate (`TraitMech:data/traits/<...>#<graph_id>`). If the predicate maps
  to an existing RO/OBI/METPO relation, record that in the SSSOM mappings file
  as a `skos:*Match`, not in `definition_source`.
- Pair only when the relation has a meaningful negative form AND the
  negative is actually used in a trait YAML. Do not pair speculatively.

#### Scope C (`CausalNodeTypeEnum` lift)

- Declare one **enum-parent** class (e.g. `trait causal node type`,
  `METPO:1007410`) under a `trait causal node` domain class.
- Lift each permissible value as a leaf class with `SC %` = the enum-parent.
- Definition source: `TraitMech:src/traitmech/schema/traitmech.yaml#CausalNodeTypeEnum.<VALUE>`.
- No intermediate parents needed; the schema description is flat.

### 3. Design the predicates (Scope B only)

For each predicate, write one object-property row in
`metpo_proposal_properties_robot.tsv`. Domain and range MUST resolve either
to:

- another row in the same proposal, or
- an existing METPO IRI (`METPO:1000525` for microbe, `METPO:1007402` etc.), or
- an external IRI (`NCBITaxon:1`, `CHEBI:24431`, `GO:0008150`, `RO:0002410`).

Skip slots that just hold metadata (e.g., timestamps, curator IDs).

### 4. Write the TSVs

Write `metpo_proposal_classes_robot.tsv` and
`metpo_proposal_properties_robot.tsv` directly with the `Write` tool. Build
each row as a literal tab-separated string. After writing, fix the ROBOT
header row's trailing tabs (header row 2 needs to reach the full column
count):

```bash
python3 -c "
p = 'proposals/<cohort>/metpo_proposal_classes_robot.tsv'
lines = open(p).readlines()
lines[1] = lines[1].rstrip('\n') + '\t\t\t\n'  # 3 trailing tabs to reach 11 cols
open(p, 'w').writelines(lines)
"
```

(The classes template needs 3 trailing tabs; the properties template needs
3 trailing tabs to reach 12 cols when the header lists only the first 9
directives.)


### 5. Verify

```bash
just verify-proposal <cohort>          # column counts, header directives, parent integrity, coverage
just robot-validate-proposal <cohort>  # full ROBOT template+merge+ELK reasoning
```

Both must pass clean (exit zero, no `UNSAT`). The complete manual check suite —
column-count, Scope-C enum coverage, Scope-A citation resolution (whole-corpus coverage moved to `just audit-proposal-coverage`, #319), `definition_source` hygiene
(issue #83), parent integrity, and the raw ROBOT/ELK invocation with prefixes — is in
[`reference/verification-and-pitfalls.md`](reference/verification-and-pitfalls.md), which
also lists the common pitfalls and their fixes.
### 6. Write the narrative

`proposal.md` is the reviewer's entry point. Required sections:

| Section | Content |
|---|---|
| **Context** | Why this cohort exists; what gap it fills in METPO. Reference the TraitMech `traitmech:` fallback policy. |
| **Scope** | Table of A/B/C counts × parent class × leaf count. State explicitly which scopes are *not* covered and why. |
| **Hierarchy decisions** | Per intermediate-parent: why you grouped these together (cite schema comments / record curation_history). |
| **Predicate proposals** | Table of property rows × domain × range × source record (Scope B). Omit the section if no Scope-B rows. |
| **ID space and subset** | The blocks you allocated and the subset tag. Confirm no collision with CommunityMech v1 (`1007100`–`1007220`). |
| **Files** | Three-row table listing each artifact and row count. |
| **Verification** | The `just verify-proposal` output plus any ROBOT/ELK runs. |
| **Upstream path** | What happens after TraitMech sign-off — typically: copy TSVs to `kg-microbe/mappings/` or open a [berkeleybop/metpo](https://github.com/berkeleybop/metpo) issue with the TSVs attached. |
| **Round-trip plan (Scope A)** | After upstream mints the real METPO IDs, what migration runs in TraitMech: update `data/raw/metpo.owl`, re-seed, swap `identifier:` from `traitmech:NNNNNN` to the new `METPO:` CURIE while preserving the old one in `synonyms:`. |
| **Change log** | Version + date + headline change. |

### 7. Open a PR

Standard TraitMech workflow:

```bash
git checkout -b claude/metpo-<cohort>-proposal
git add proposals/<cohort>/ justfile           # justfile only if you added a target
git commit -m "Add METPO ROBOT-template proposal: <cohort>"
git push -u origin claude/metpo-<cohort>-proposal
gh pr create --title "METPO ROBOT-template proposal: <cohort>"
gh api repos/CultureBotAI/TraitMech/pulls/<n>/requested_reviewers -X POST -f "reviewers[]=Copilot"
```

---

## Reference Files

| File | Contents |
|------|----------|
| [`reference/conventions.md`](reference/conventions.md) | Required reading (upstream contract + templates), ROBOT template column conventions, and the cross-ontology-equivalents-are-mappings rule (issue #83) with the SSSOM column spec |
| [`reference/verification-and-pitfalls.md`](reference/verification-and-pitfalls.md) | The full step-5 verification suite (column counts, coverage checks, `definition_source` hygiene, parent integrity, raw ROBOT/ELK) and the common-pitfalls table |
| [`reference/updating-proposals.md`](reference/updating-proposals.md) | Decision rule and the three update paths — edit in place, extend in place, new cohort version — plus what not to do |
| [`reference/canonical-example.md`](reference/canonical-example.md) | The `metpo_traitmech_v1` worked cohort: ID-block layout, what it deliberately omits (Scope A/B), and why |
