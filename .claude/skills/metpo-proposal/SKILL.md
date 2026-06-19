---
name: metpo-proposal
description: Generate a ROBOT-template METPO proposal that lifts TraitMech synthetic traits, causal-graph scaffolding, and schema-side controlled vocabularies into METPO classes and predicates. Use when a curator-minted `traitmech:NNNNNN` ID needs a METPO home, when a causal predicate (`CausalEdge.predicate_id`) has no upstream IRI, or when a TraitMech schema enum should become first-class METPO vocabulary.
category: workflow
requires_database: false
requires_internet: false
version: 1.0.0
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
| `metpo_proposal_mappings.sssom.tsv` | SSSOM mapping set — cross-ontology equivalents with `skos:exactMatch`/`closeMatch`/`narrowMatch` and match confidence. **Optional**: emit only when ≥1 proposed term aligns to an existing OMP/MICRO/PATO/GO/CHEBI/… class. See "Cross-ontology equivalents are mappings, not definition_source" below. |
| `proposal.md` | Reviewer narrative: scope, hierarchy decisions, predicate rationale, verification, upstream path |

**Run from `TraitMech/` directory.** Cross-Mech references:
- CultureMech/CommunityMech analogue: `CommunityMech/.claude/skills/metpo-proposal/skill.md` and reference cohort `proposals/metpo_communitymech_v1/`.
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

## Required reading

Before generating a proposal, read:

1. **`/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/.claude/skills/metpo-proposal/SKILL.md`** —
   the upstream metpo-proposal skill. Defines:
   - Aristotelian definition style (`<genus>: <differentia>`).
   - `definition_source` citation forms (PMID, DOI, BacDive, `TODO:add_citation`).
   - Family-aware numeric ID slotting (chemical-interaction predicates go in 2000001–2000056, value datatype properties in 2000700+, etc.).
   - Parent-class selection (audit for siblings before falling back to `METPO:1000000`).
   - The 12-point pre-submission checklist.
   - Paired predicate convention (`does not <stem>` + shared related-synonym).
2. **`/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/mappings/metpo_proposal_classes_robot.tsv`** —
   the canonical 11-column class template. Copy the two-row header verbatim.
3. **`/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/mappings/metpo_proposal_properties_robot.tsv`** —
   the canonical 12-column property template.
4. **`/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/CommunityMech/CommunityMech/proposals/metpo_communitymech_v1/`** —
   the most recent worked example. Read all three files end-to-end before
   writing a new cohort; the TraitMech v1 cohort follows the same conventions
   with a different ID block and subset tag.
5. **`TraitMech/.claude/skills/manage-identifiers/SKILL.md`** — the
   `traitmech:NNNNNN` allocation policy. Scope-A proposals are the upstream
   half of that fallback workflow.

---

## ROBOT template column conventions

Tab-separated, **two header rows**, no other column structures parse cleanly.

**Classes** (11 columns):

```
proposed_id<TAB>label<TAB>definition<TAB>definition_source<TAB>parent<TAB>synonyms<TAB>xrefs<TAB>subset<TAB>priority<TAB>observations<TAB>traits_addressed
ID<TAB>LABEL<TAB>A IAO:0000115<TAB>>A IAO:0000119<TAB>SC %<TAB>A oboInOwl:hasExactSynonym SPLIT=|<TAB>A oboInOwl:hasDbXref SPLIT=|<TAB>A oboInOwl:inSubset<TAB><TAB><TAB>
```

**Properties** (12 columns):

```
proposed_id<TAB>label<TAB>definition<TAB>definition_source<TAB>type<TAB>domain<TAB>range<TAB>xrefs<TAB>subset<TAB>priority<TAB>traits_addressed<TAB>observations
ID<TAB>LABEL<TAB>A IAO:0000115<TAB>>A IAO:0000119<TAB>TYPE<TAB>DOMAIN<TAB>RANGE<TAB>A oboInOwl:hasDbXref SPLIT=|<TAB>A oboInOwl:inSubset<TAB><TAB><TAB>
```

The **second row (ROBOT header) must have trailing tabs to reach the full
column count**, even when the trailing columns are blank. Validate with:

```bash
just verify-proposal <cohort>
# or manually:
awk -F'\t' 'NF != 11 {print NR": "NF" cols"}' proposals/<cohort>/metpo_proposal_classes_robot.tsv
awk -F'\t' 'NF != 12 {print NR": "NF" cols"}' proposals/<cohort>/metpo_proposal_properties_robot.tsv
```

Both commands should print nothing.

---

## Cross-ontology equivalents are mappings, not `definition_source`

(Tracks [CultureBotAI/TraitMech#83](https://github.com/CultureBotAI/TraitMech/issues/83);
cross-repo hub [berkeleybop/metpo#344](https://github.com/berkeleybop/metpo/issues/344).)

`definition_source` (column 4, ROBOT directive `>A IAO:0000119`) means **"where
the definition text came from"** — a *citation*. It takes only:

- a publication: `PMID:NNNNNNN`, `DOI:10.xxxx/...`, `ISBN:...`
- a reference DB record: `BacDive:NNNNN`
- the TraitMech curation event that minted the term:
  `TraitMech:data/traits/<category>/<slug>.yaml#<anchor>`
- `TODO:add_citation` as an explicit placeholder when none of the above is known

When a proposed term **aligns to an existing ontology class** (OMP, MICRO, PATO,
GO, CHEBI, ENVO, …), that alignment is a **mapping**, not definition provenance.
It must **never** appear in `definition_source`. An ontology IRI in column 4 is a
bug — fix it, don't carry it.

Emit equivalents in **two** places instead:

1. **ROBOT `xrefs` column** (`A oboInOwl:hasDbXref SPLIT=|`) — the lightweight
   per-row cross-reference, e.g. `GO:0008150|PATO:0000001`. `hasDbXref` carries
   **no** match strength; it is a hint, not an equivalence axiom.
2. **`metpo_proposal_mappings.sssom.tsv`** — the dedicated SSSOM mapping set that
   records *match strength* with a proper predicate. Emit this file whenever a
   row has a real semantic alignment (not just a loose xref). Columns (mirrors
   the canonical kg-microbe `metpo_proposal_audit` set):

   ```
   subject_id	subject_label	predicate_id	object_id	object_label	mapping_justification	confidence	mapping_source	comment
   ```

   - `subject_id` = the proposed `METPO:1007NNN` / `METPO:2007NNN` id (or the
     `traitmech:NNNNNN` fallback id if still un-minted).
   - `predicate_id` ∈ {`skos:exactMatch`, `skos:closeMatch`, `skos:narrowMatch`,
     `skos:broadMatch`}. Pick by **semantics**, not convenience:
     - `exactMatch` — same concept, interchangeable in assertions.
     - `closeMatch` — substantially the same, minor scope difference.
     - `narrowMatch` — the METPO term is **more specific** than the object.
     - `broadMatch` — the METPO term is **more general** than the object.
   - `mapping_justification` = a `semapv:` CURIE (e.g.
     `semapv:ManualMappingCuration`, `semapv:LexicalMatching`).
   - `confidence` = `high` | `medium` | `low` (or a 0–1 float).
   - `mapping_source` = `metpo_traitmech_<cohort>`.

This is the same split the upstream generator makes
(`kg-microbe/scripts/extract_metpo_proposals.py`): ROBOT templates default
`definition_source` to `TODO:add_citation`, and `skos:*Match` mappings are
written to a separate SSSOM file — never into `definition_source`.

> The data-side grounding tables (`mappings/node_grounding.tsv`,
> `mappings/predicate_grounding.tsv`) follow the same principle: the alignment
> they record is a mapping. Each carries a `predicate_id` column with the
> `skos:*Match` strength rather than burying it in free-text `notes`.

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
  file, never here (see "Cross-ontology equivalents are mappings" above).

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
# Convenience wrapper (recommended)
just verify-proposal <cohort>

# Manual equivalents:

# Column-count sanity (must print nothing)
awk -F'\t' 'NF != 11 {print NR": "NF" cols"}' proposals/<cohort>/metpo_proposal_classes_robot.tsv
awk -F'\t' 'NF != 12 {print NR": "NF" cols"}' proposals/<cohort>/metpo_proposal_properties_robot.tsv

# Enum coverage (Scope C only) — every CausalNodeTypeEnum value should appear
# as a leaf row whose definition_source matches the enum value.
uv run python -c "
import re, yaml
schema = yaml.safe_load(open('src/traitmech/schema/traitmech.yaml'))
values = list(schema['enums']['CausalNodeTypeEnum']['permissible_values'])
tsv = open('proposals/<cohort>/metpo_proposal_classes_robot.tsv').read()
missing = [v for v in values if f'CausalNodeTypeEnum.{v}' not in tsv]
print('Missing leaves:', missing or 'none')
"

# Scope-A coverage — every traitmech:NNNNNN in the corpus is either in the
# proposal or in a deliberately-deferred list.
uv run python -c "
import re, pathlib
ids = set()
for p in pathlib.Path('data/traits').rglob('*.yaml'):
    for m in re.finditer(r'^identifier:\s*(traitmech:\d+)', p.read_text(), re.MULTILINE):
        ids.add(m.group(1))
tsv = open('proposals/<cohort>/metpo_proposal_classes_robot.tsv').read()
covered = {i for i in ids if i in tsv}  # cited in definition_source
print('Corpus traitmech IDs:', len(ids))
print('Covered by proposal: ', len(covered))
print('Not covered:         ', sorted(ids - covered))
"

# definition_source hygiene (issue #83) — column 4 must be a citation, never
# a cross-ontology equivalence IRI. This must print nothing.
uv run python -c "
import csv, glob, re
EQUIV = re.compile(r'^(OMP|MICRO|PATO|GO|CHEBI|ENVO|EFO|SO|PR|UBERON|CL|RO|OBI):', re.I)
bad = []
for f in glob.glob('proposals/<cohort>/metpo_proposal_*_robot.tsv'):
    rows = list(csv.reader(open(f), delimiter='\t'))
    for r in rows[2:]:
        if len(r) > 3 and r[3]:
            for tok in r[3].split('|'):
                if EQUIV.match(tok.strip()):
                    bad.append((f, r[0], tok.strip()))
print('definition_source equivalence leaks:', bad or 'none')
"

# Parent integrity — every SC % parent resolves in-file or to a known METPO IRI
uv run python -c "
import re
tsv = open('proposals/<cohort>/metpo_proposal_classes_robot.tsv').read().splitlines()[2:]
ids_in_file = {r.split('\t')[0] for r in tsv}
parents = {r.split('\t')[4] for r in tsv if r.strip()}
external_ok = re.compile(r'^METPO:\d+$')
missing = [p for p in parents if p not in ids_in_file and not external_ok.match(p)]
print('Parents missing locally:', missing or 'none')
"
```

For full ROBOT + ELK validation use the wrapper, which mirrors the
canonical kg-microbe `validate_with_robot()` invocation
(`kg-microbe/scripts/extract_metpo_proposals.py:1643`):

```bash
just robot-validate-proposal <cohort>
```

The wrapper auto-discovers the `robot` binary in this order:
`$ROBOT` → `$ROBOT_BIN` → `which robot` → `../kg-microbe/data/raw/robot`.
It compiles the classes TSV (and the properties TSV if present), merges
with `data/raw/metpo.owl`, and runs ELK with axiom-generators `SubClass
EquivalentClass`. OWL artifacts land in `reports/robot/<cohort>/`.

Pass criteria: all `robot` commands exit zero with no `UNSAT` warnings.
A reasoned output line count much larger than the merged input signals
unintended inferred equivalences (the wrapper prints a WARN at +200
lines) — investigate before submitting.

If you need to run the raw commands yourself (e.g. for prefix tweaks
not yet in the wrapper):

```bash
robot template --template proposals/<cohort>/metpo_proposal_classes_robot.tsv \
    --prefix "METPO: http://purl.obolibrary.org/obo/METPO_" \
    --prefix "biolink: https://w3id.org/biolink/vocab/" \
    --prefix "RO: http://purl.obolibrary.org/obo/RO_" \
    --output /tmp/classes.owl
robot template --template proposals/<cohort>/metpo_proposal_properties_robot.tsv \
    --prefix "METPO: http://purl.obolibrary.org/obo/METPO_" \
    --prefix "biolink: https://w3id.org/biolink/vocab/" \
    --output /tmp/properties.owl
robot merge --input data/raw/metpo.owl --input /tmp/classes.owl --input /tmp/properties.owl \
    --output /tmp/merged.owl
robot reason --reasoner ELK --input /tmp/merged.owl \
    --axiom-generators "SubClass EquivalentClass" --output /tmp/reasoned.owl
```

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

## Updating an existing proposal

The workflow above produces a **new** cohort. When work on an existing cohort
isn't finished, pick one of three update paths instead of starting fresh.

### Decision rule

| Situation | Path | Why |
|---|---|---|
| Reviewer (human or Copilot) asks for changes on an open PR before merge | **Edit in place** | The IDs and subset tag are still proposal-stage; no downstream consumer has pinned them yet. |
| Cohort is merged on main and you want to add more lifts (e.g., a new wave of `traitmech:` synthetic IDs after the original cohort) | **Extend in place** | Append-only is non-breaking; reviewers can diff the new rows against the same cohort. |
| Cohort is merged and the underlying schema changed in a way that invalidates existing rows (e.g., a `CausalNodeTypeEnum` value was renamed or removed, or a `traitmech:` record was retracted before upstream minted its METPO ID) | **New cohort version** | A breaking semantic change needs a fresh subset tag and ID block so consumers can pin to the old or new version. |
| Real METPO IDs have been minted upstream and a row has been re-IDed | **New cohort version** | Mutating an already-minted ID is hostile to downstream consumers. Old cohort stays as the audit trail of what was proposed; new cohort tracks the post-mint state. |

### Path A — Edit in place (open PR)

Modify rows directly in `proposals/<cohort>/metpo_proposal_*.tsv`. Keep the
original `proposed_id`, `subset`, and column structure. Update
`definition`, `definition_source`, `parent`, `synonyms`, or `label` in
place. Re-run `just verify-proposal <cohort>`. Commit on the same branch and
let the Copilot review thread close.

If the edit is to the narrative only (no TSV change), edit `proposal.md`
and add a one-line note under the Change log section:
`- v1, 2026-05 (revised <date>): <one-line summary>`.

### Path B — Extend in place (merged cohort)

Add new rows to the **same** `metpo_proposal_*.tsv` files in the **same**
cohort directory. Append-only — never reorder or renumber existing rows.
Conventions:

- New rows use a **contiguous fresh block** within the same
  `METPO:1007NNN` / `METPO:2007NNN` range. Pick a block at least 10 above
  the highest existing ID to leave room for v1 patches. Document the new
  block in `proposal.md` under the ID space section.
- Same `subset` tag as the rest of the cohort. The tag identifies the
  cohort, not the round of additions.
- New `parent` references may point at existing rows in the cohort (this is
  the main reason to extend rather than re-version).
- Update `proposal.md`:
  - Add the new lift to the Scope table.
  - Add the new ID sub-block to the ID space section.
  - Append a Change log entry: `- v1.N, <date>: extended with <description>
    (+<row count> classes / +<row count> properties)`.

Open a new PR titled `Extend METPO proposal <cohort> with <description>`.
Re-request Copilot review.

### Path C — New cohort version

Create a fresh directory `proposals/<base-name>_v<N>/` (e.g.,
`metpo_traitmech_v2/`) with:

- Fresh `subset` tag: bump the month-year suffix
  (`metpo_traitmech_2026_05` → `metpo_traitmech_2026_07`).
- Fresh **ID block** in the `1007NNN` / `2007NNN` placeholder range, **not
  overlapping with v1**. Document the new block in v2's `proposal.md`.
- v2 `proposal.md` must include a `## Relationship to v1` section that
  names every v1 ID retired or redefined, with the reason.
- v1 stays on disk read-only. Add a top-of-file note to v1's `proposal.md`:
  `> Superseded by proposals/<base-name>_v<N>/proposal.md (<date>). v1 is
  retained for traceability.`

Use this path sparingly — the kg-microbe pipeline assumes one active cohort
per source repository at a time, and re-versioning forces downstream
consumers to switch their queries.

### What not to do

- Do **not** edit IDs after they've been merged on main (use Path B or C
  instead).
- Do **not** mix Path B (extend) and Path C (re-version) in the same PR —
  reviewers can't tell what's append-only vs. breaking.
- Do **not** delete rows in Path B. If a row is obsolete, mark it by
  setting `priority` to `LOW` and adding an `observations` note; let Path C
  retire it cleanly.

---

## Common pitfalls

| Symptom | Cause | Fix |
|---|---|---|
| `awk` reports row 2 has 8/9 columns | Trailing tabs missing on ROBOT header | Append `\t\t\t` to row 2 (see step 4) |
| ROBOT error "subject of axiom is not a class" | Property row referencing a class IRI in the `RANGE` column when ROBOT expects a class declaration | Declare the range class as its own row in the classes TSV first |
| ELK reports unsatisfiable class | Intermediate parent created with conflicting `SC %` axioms | Inspect the parent chain — usually a copy-paste error in the `parent` column |
| Copilot flags "schema lifted incorrectly" | The leaf's definition doesn't match the schema enum's description verbatim | Copy the schema description into the `definition` column, *then* edit only for Aristotelian form. Reword more freely in the proposal narrative. |
| Reviewer asks for an existing METPO ID | The lifted concept already exists in METPO under a different label | Use the existing IRI; remove the row from the proposal; record the alias in the next seeder run so the `traitmech:` ID gets retired. |
| `traitmech:` ID appears in `data/traits/` but not in the proposal TSV | Coverage gap — Scope-A enumeration drifted between cohorts | Re-run the Scope-A coverage check; either add the missing row or document why it was deferred to a later cohort. |
| An ontology IRI (`OMP:`, `PATO:`, `GO:`, …) sits in `definition_source` (col 4) | Cross-ontology equivalence mistaken for definition provenance (issue #83) | Move it: lightweight hint → `xrefs` (`hasDbXref`); semantic alignment → `metpo_proposal_mappings.sssom.tsv` with a `skos:*Match`. Keep col 4 for citations only. Catch with the `definition_source` hygiene check in step 5. |
| `CausalNodeTypeEnum` value renamed but proposal still cites old name | Schema drift after proposal was drafted | Use Path C (new cohort version) if v1 is merged; Path A otherwise. |

---

## Canonical example

`proposals/metpo_traitmech_v1/` — the first TraitMech cohort, lifting the
trait-causal-graph scaffold. Read it end-to-end before writing a new cohort;
every convention in this skill is instantiated there.

**v1 contents (14 class rows, 0 predicate rows):**

| ID block | Coverage |
|---|---|
| `METPO:1007400`–`1007402` | Top-level domain classes (`trait causal graph`, `trait causal node`, `trait causal edge`) lifting LinkML classes `CausalGraph`, `CausalNode`, `CausalEdge`. |
| `METPO:1007410` | Enum-parent (`trait causal node type`) under `trait causal node`. |
| `METPO:1007411`–`1007420` | All 10 `CausalNodeTypeEnum` permissible values as leaves (TRAIT, PATHWAY, ENVIRONMENTAL_FACTOR, EXPERIMENTAL_FACTOR, GENE_OR_PROTEIN, CHEMICAL, ORGANELLE, CELLULAR_LOCALIZATION, MOLECULAR_FUNCTION, BIOLOGICAL_PROCESS). |

Subset tag: `metpo_traitmech_2026_05`. Verified clean by
`just verify-proposal metpo_traitmech_v1` (column counts, header
directives, parent integrity, subset tag, Scope-A and Scope-C coverage all
pass).

**What v1 deliberately omits:**

- **Scope A** is empty — the corpus has zero `traitmech:NNNNNN` IDs at the
  time of drafting. As curators begin minting fallback IDs, add them via
  **Path B (extend in place)** with a contiguous block at `1007430+`.
- **Scope B** is empty — but **not because the corpus is well-grounded**.
  An audit at v1 time found `0/1019` causal edges have a `predicate_id`;
  the `predicate` field carries 218 distinct free-text labels. Most top
  labels (`enables`, `causes`, `contributes to`, …) have RO homes already,
  and a few (`produces`, `uses as carbon source`, `oxidizes`) already exist
  in METPO. Drafting a Scope-B cohort today would propose ~200 predicates
  alongside ones that should be RO-grounded — wrong direction.
  **The correct prerequisite is a data-side predicate-grounding migration**
  (populate `predicate_id` from RO/METPO where matches exist). Only the
  residual that has no upstream home (`manifests as`, `selects for`,
  `feeds electrons into`, `uses electron donor`, …) becomes a Scope-B
  candidate. Add those via Path B (extend v1) at `2007400+` after grounding
  completes.

The structural template — Aristotelian definitions, OBO xrefs without
equivalence claims, contiguous ID blocks per logical group, single subset
tag, flat hierarchy under the enum-parent — is exactly what subsequent
cohorts should follow. A cross-Mech reference for a heavier proposal (9
enums + 14 predicates) is
`CommunityMech/CommunityMech/proposals/metpo_communitymech_v1/`.
