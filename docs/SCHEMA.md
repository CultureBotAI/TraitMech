# TraitMech schema

The full LinkML schema lives at `src/traitmech/schema/traitmech.yaml`.
This page is a quick reference.

## TraitRecord (root)

One YAML file per record under `data/traits/<category>/<slug>.yaml`.

| Slot | Range | Required | Notes |
|---|---|---|---|
| `identifier` | string (CURIE) | ✓ | Stable METPO/traitmech CURIE; primary key |
| `label` | string | ✓ | rdfs:label of the source class |
| `definition` | string |  | IAO:0000115 from METPO |
| `definition_source` | string |  | IAO:0000119 — citation for the definition |
| `synonyms` | TraitSynonym[] |  | hasExactSynonym / hasRelatedSynonym / etc. |
| `parent_traits` | string[] (CURIE) |  | rdfs:subClassOf parents |
| `xrefs` | string[] (CURIE) |  | hasDbXref to PATO/GO/NCIT/etc. |
| `trait_category` | TraitCategoryEnum |  | Coarse bucket (drives filesystem path) |
| `term_kind` | TermKindEnum |  | CLASS / DATATYPE_PROPERTY / OBJECT_PROPERTY |
| `domain` | string |  | For properties — typed subject |
| `range_` | string |  | For properties — value range |
| `priority` | PriorityEnum |  | CRITICAL/HIGH/MEDIUM/LOW |
| `subset` | string |  | oboInOwl:inSubset tag |
| `observation_count` | int |  | Underlying observation count from METPO proposals |
| `created_by` | string |  | IAO:0000117 — original author |
| `contributors` | string[] |  | Local curator names |
| `evidence` | EvidenceItem[] |  | Optional literature support |
| `mapping_status` | MappingStatusEnum |  | SEEDED / REVIEWED / DEPRECATED |
| `curation_history` | CurationEvent[] |  | Append-only audit trail |

## Enums

### TraitCategoryEnum
- `MORPHOLOGY` — cell shape, motility, Gram, sporulation, pigmentation
- `PHYSIOLOGY` — trophic type, generic phenotype
- `ENVIRONMENT` — pH/temperature/salinity/oxygen tolerance + optima
- `METABOLISM` — biological process subtree + object properties
  ("uses as carbon source" etc.)
- `GENOMICS` — GC content, genome-scale traits
- `ECOLOGY` — pathogenic to host, biosafety level
- `DETECTION` — selective/differential media growth (no records yet)
- `QUANTITATIVE_PROPERTY` — DatatypeProperty entries (numeric carriers)
- `OBSERVATION` — observation-class entries (data-collection units)
- `UPPER` — METPO upper-level roots (material entity, quality, etc.)
- `OTHER`

### TermKindEnum
`CLASS` / `DATATYPE_PROPERTY` / `OBJECT_PROPERTY` / `ANNOTATION_PROPERTY`

### MappingStatusEnum
- `SEEDED` — fresh from `metpo.owl`, not yet curator-reviewed
- `REVIEWED` — curator has signed off
- `DEPRECATED` — superseded; retained for traceability

## Categorisation rules (seeder)

Implemented in `scripts/seed_from_metpo.py:CATEGORY_BY_ANCESTOR`.

The seeder walks each class's ancestor chain BFS-from-self; the first
ancestor matching a known anchor wins. DatatypeProperties → always
`QUANTITATIVE_PROPERTY`. ObjectProperties → always `METABOLISM`
(METPO's object properties all describe metabolic relationships:
"assimilates", "uses as electron acceptor", "ferments", etc.).

The `material entity` subtree (chemical entity / enzyme / microbe) is
**not** seeded — those belong in MIM / kg-microbe, not TraitMech.
