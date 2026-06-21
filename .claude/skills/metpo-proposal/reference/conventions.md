# Conventions: Required Reading · ROBOT Template Columns · Cross-Ontology Mappings

*Reference for the **metpo-proposal** skill — see [`../SKILL.md`](../SKILL.md) for the overview, scopes, ID-space conventions, and workflow.*

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

