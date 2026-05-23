# METPO ROBOT Template Proposal — TraitMech Lift (v1, 2026-05)

## Context

[TraitMech](https://github.com/CultureBotAI/TraitMech) is a microbial-trait
knowledge base whose records are seeded from `metpo.owl` — every one of its
357 current trait records carries a `METPO:` identifier, and the project's
[identifier policy](../../.claude/skills/manage-identifiers/SKILL.md) explicitly
mandates METPO-first IDs with a reserved `traitmech:NNNNNN` fallback only when
a trait has no upstream METPO home.

In addition to those seeded trait classes, TraitMech introduces a
**causal-graph subsystem** — every trait record may carry one or more
`causal_graphs:` entries (LinkML class `CausalGraph`) populated with typed
`nodes:` (`CausalNode`) and evidence-backed `edges:` (`CausalEdge`). The
node-type axis is governed by a controlled vocabulary called
`CausalNodeTypeEnum` (10 values: TRAIT, PATHWAY, ENVIRONMENTAL_FACTOR,
EXPERIMENTAL_FACTOR, GENE_OR_PROTEIN, CHEMICAL, ORGANELLE,
CELLULAR_LOCALIZATION, MOLECULAR_FUNCTION, BIOLOGICAL_PROCESS).

METPO currently has **zero** coverage of trait-causal-graph scaffolding — no
`causal graph`, no `causal node`, no node-type axis. This proposal closes that
gap by lifting three top-level domain classes plus the `CausalNodeTypeEnum`
permissible-value set (1 enum-parent + 10 leaves) into METPO. Once upstream
adopts these, downstream KG-Microbe consumers will be able to filter trait
records by causal-graph mechanism axis (e.g. "all traits whose causal graph
contains a `MOLECULAR_FUNCTION` node") using METPO-native queries instead of
TraitMech-internal LinkML enum codes.

## Scope

| Scope | Source | # rows | Lift status |
|---|---|---:|---|
| C (top-level domain classes) | `schema/traitmech.yaml` classes `CausalGraph`, `CausalNode`, `CausalEdge` | 3 | included |
| C (controlled vocabulary) | `schema/traitmech.yaml#CausalNodeTypeEnum` (10 permissible values) | 1 parent + 10 leaves | included |
| A (synthetic `traitmech:NNNNNN` trait classes) | `data/traits/**/*.yaml` records whose `identifier:` starts with `traitmech:` | 0 in corpus | **not applicable** — no curator-minted synthetic IDs exist yet |
| B (causal-graph predicates) | `CausalEdge` rows whose mechanism has no upstream home | 0/1019 edges currently *grounded*, 218 distinct free-text labels | **deferred — see Predicate proposals section** — proposal would be premature; predicate-grounding migration must run first |

Total class rows in v1: **14** (3 top-level + 1 enum-parent + 10 leaves).
No property (predicate) rows in v1; `metpo_proposal_properties_robot.tsv` is
intentionally omitted.

### Out of scope (and why)

The TraitMech LinkML schema declares 5 other enums that are *not* lifted:

| enum | why excluded |
|---|---|
| `TraitCategoryEnum` | Filesystem-layout discriminator (MORPHOLOGY/PHYSIOLOGY/…). Not a real ontology axis. |
| `TermKindEnum` | OWL meta-axis (Class vs DatatypeProperty). Not a domain concept. |
| `SynonymTypeEnum` | OBO already has `oboInOwl:hasExactSynonym|hasBroadSynonym|hasNarrowSynonym|hasRelatedSynonym`. No lift needed. |
| `PriorityEnum` | Editorial workflow knob. |
| `MappingStatusEnum` | Internal lifecycle flag (SEEDED → REVIEWED → DEPRECATED). |

The [skill](../../.claude/skills/metpo-proposal/SKILL.md#scope-c--schema-enum-lift-one-off-do-not-lift-workflow-internal-enums)
encodes this scope policy.

## Hierarchy decisions

### Top-level domain classes

All three sit directly under `METPO:1000000` because no closer METPO parent
exists today; the upstream maintainers may relocate them under a parent like
`mechanism` or `model` if METPO grows one. The siblings (graph / node /
edge) are intentionally *not* mutually disjoint — a future "trait causal
node = part_of some trait causal graph" axiom is left to a later cohort
once METPO is willing to encode the part-of relation.

### `CausalNodeTypeEnum` lift — flat under the enum-parent

`trait causal node type` (`METPO:1007410`) is a child of `trait causal node`
(`METPO:1007401`) so that an `instance-of` query downstream can either
filter at the node level ("all causal nodes") or the typed level ("only
`gene_or_protein` causal nodes").

The 10 enum values do **not** have intermediate parents in this cohort. The
schema description (`Broad categories for nodes in trait causal graphs.`)
treats them as siblings, and any plausible grouping (e.g. genetic-axis ⊃
GENE_OR_PROTEIN+MOLECULAR_FUNCTION+BIOLOGICAL_PROCESS) would impose a
taxonomy that the actual trait records don't yet need.

### External xrefs

Where an obvious upstream anchor exists, the leaf row carries it via
`oboInOwl:hasDbXref`. These are *not* equivalence axioms — a TraitMech
"chemical causal-graph node" is a *role*, not the chemical itself. The
xrefs make cross-walks easy for KG consumers without committing METPO to a
stronger semantic claim.

| leaf | xref | anchor type |
|---|---|---|
| `causal-graph environmental factor node` | `ENVO:01000254` | environmental system |
| `causal-graph experimental factor node` | `EFO:0000001` | EFO root |
| `causal-graph gene or protein node` | `SO:0000704`, `PR:000000001` | gene / protein |
| `causal-graph chemical node` | `CHEBI:24431` | chemical entity |
| `causal-graph organelle node` | `GO:0043226` | organelle |
| `causal-graph cellular localization node` | `GO:0005575` | cellular component |
| `causal-graph molecular function node` | `GO:0003674` | molecular function root |
| `causal-graph biological process node` | `GO:0008150` | biological process root |

`causal-graph trait node` and `causal-graph pathway node` have no xref — the
trait-node anchor is METPO itself (this proposal is the anchor), and pathway
has no single canonical OBO node-type root (CHEBI, GO, Reactome, KEGG all
disagree; defer to a curator).

## Predicate proposals

None in v1, but the corpus's current predicate state is worth recording
because it materially affects what a future Scope-B cohort should look
like.

### Causal-edge predicate grounding state (post-migration, 2026-05)

A curated **predicate-grounding migration** (`just ground-predicates --apply`,
backed by `mappings/predicate_grounding.tsv`) has now run over the corpus
twice — once with 10 METPO/RO/RDFS mappings, then again after extending the
table with 10 biolink predicates (cross-checked via
`just check-biolink-coverage` against `data/raw/biolink-model.yaml`).
Before/after:

| | edges grounded | edges ungrounded | distinct ungrounded labels |
|---|---:|---:|---:|
| Before migration | 0 / 1019 | 1019 | 218 |
| After METPO/RO pass (10 mappings) | 385 / 1019 | 634 | 209 |
| After biolink extension (20 mappings) | **433 / 1019** | **586** | **199** |

The 433 grounded edges break down by target CURIE and source:

| source | target CURIE | label | edges |
|---|---|---|---:|
| METPO | `METPO:2000202` | produces | 128 |
| RDFS | `rdfs:subClassOf` | is a | 104 |
| RO | `RO:0002327` | enables | 67 |
| RO | `RO:0002326` | contributes to | 37 |
| biolink | `biolink:causes` | causes | 21 |
| METPO | `METPO:2000009` | uses as electron donor | 13 |
| METPO | `METPO:2000006` | uses as carbon source | 12 |
| biolink | `biolink:catalyzes` | catalyzes | 10 |
| RO | `RO:0002211` | regulates | 8 |
| METPO | `METPO:2000016` | oxidizes | 8 |
| METPO | `METPO:2000010` | uses as energy source | 8 |
| biolink | `biolink:associated_with` | associated with | 4 |
| biolink | `biolink:located_in` | located in | 3 |
| biolink | `biolink:occurs_in` | occurs in | 2 |
| biolink | `biolink:participates_in` | participates in | 2 |
| biolink | `biolink:part_of` | part of | 2 |
| biolink | `biolink:interacts_with` | interacts with | 2 |
| biolink | `biolink:consumes` | consumes | 1 |
| biolink | `biolink:develops_into` | develops into | 1 |

By source: 169 METPO + 104 RDFS + 112 RO + 48 biolink = **433 / 1019 (42.5%)**
grounded.

The migration is idempotent (`predicate_id` is never overwritten once set)
and appends one `CurationEvent` of `action: GROUND_CAUSAL_PREDICATES` per
modified file. Biolink slot CURIEs validate cleanly against the schema's
`predicate_id` pattern, and the same `just validate-strict` pass over the
full corpus still reports 0 ERRORs.

### Residual is the Scope-B candidate list

The remaining 586 edges across 199 distinct labels are surfaced in
`reports/predicate_grounding_residual.tsv`. The top entries — labels that
now genuinely have no upstream home in METPO, RO, RDFS, or biolink — are
exactly the candidates a future METPO Scope-B cohort would propose:

| label | residual edges | likely action |
|---|---:|---|
| `manifests as` | 52 | METPO Scope-B candidate (no upstream home) |
| `supports` | 26 | curator call — likely `RO:0002326` (contributes to) or `biolink:supports` if added upstream |
| `selects for` | 20 | METPO Scope-B candidate |
| `drives` | 19 | curator call — likely `RO:0002411` (causally upstream of) |
| `example of` | 19 | curator call — likely `rdf:type` or split semantics |
| `generates` | 15 | curator call — synonym of `produces` or distinct? |
| `defines` | 14 | METPO Scope-B candidate |
| `maintains`, `mitigates`, `shapes`, `feeds electrons into` | 13/12/12/12 | METPO Scope-B candidates |
| `challenges`, `fixed by`, `oxidized to` | 9/9/8 | METPO Scope-B candidates |
| `influences`, `engages` | 7/7 | curator call — likely RO terms |

The biolink cross-check (see `scripts/check_biolink_coverage.py` and
`reports/biolink_coverage.tsv`) confirmed that none of the top remaining
labels above match a biolink slot name or alias, so the next round of
grounding work is genuinely a curator-led RO/biolink-extension pass
followed by the Scope-B METPO proposal at `METPO:2007400+`.

### Recommended next sequence

1. **Curator extends `mappings/predicate_grounding.tsv`** with the
   medium-confidence cases (`causes`, `drives`, `catalyzes`, `supports`,
   …). Re-running `just ground-predicates --apply` is idempotent and
   safe.
2. **Re-audit residual** — once curator-confirmable RO mappings are
   exhausted, the residual is the true Scope-B set.
3. **Scope-B cohort** — proposed as a Path B extension to v1 (subset tag
   stays `metpo_traitmech_2026_05`, new predicate IDs at
   `METPO:2007400+`). Labels like `manifests as`, `selects for`,
   `feeds electrons into` are the prime candidates.

v1 deliberately ships without Scope B because (a) 42.5% of the corpus has
now been grounded against existing upstream terms (METPO + RO + RDFS +
biolink) and that fraction will grow as curators extend the mapping TSV,
and (b) drafting METPO predicates against the *post-grounding* residual is
the only way to avoid proposing predicates that should have been
RO/biolink-grounded.

## ID space and subset

- **Class block:** `METPO:1007400`–`METPO:1007420` (placeholder range,
  pre-mint). Contiguous: `1007400`–`1007402` are top-level, `1007410`
  is the enum-parent, `1007411`–`1007420` are the 10 leaves.
- **Property block:** none in v1; first allocation will start at
  `METPO:2007400`.
- **Subset tag:** `metpo_traitmech_2026_05`.

### Collision check

- CommunityMech v1 occupies `1007100`–`1007220` and `2007100`–`2007113`.
- KG-Microbe proposals occupy `1007xxx` slots but `metpo.owl` had no
  `1007NNN` entries at the time of audit (`grep "METPO:100[67][0-9]{3}"
  data/raw/metpo.owl` returned empty).
- TraitMech's `1007400+` block sits in clear daylight above both. Future
  TraitMech cohorts should mint at `1007500+` and document the new block.

## Files

| file | rows |
|---|---:|
| `metpo_proposal_classes_robot.tsv` | 14 data + 2 header = 16 |
| `metpo_proposal_properties_robot.tsv` | (omitted — no predicate rows) |
| `proposal.md` (this file) | — |

## Verification

```bash
$ just verify-proposal metpo_traitmech_v1
Verifying proposals/metpo_traitmech_v1 ...
  classes TSV: 16 rows
  properties TSV: missing (skipped)
  scope-A: no traitmech:NNNNNN ids in corpus (nothing to cover)
  scope-C: all 10 CausalNodeTypeEnum values lifted

=== verify-proposal summary ===
  cohort:   proposals/metpo_traitmech_v1
  failures: 0
  status:   PASS
```

Checks performed by `scripts/verify_metpo_proposal.py`:

- Column counts: every row in the classes TSV has 11 columns.
- ROBOT header: row 2 declares `ID | LABEL | A IAO:0000115 | >A IAO:0000119 | SC % | … | A oboInOwl:inSubset`.
- Parent integrity: every `SC %` parent resolves either to an in-file row
  (e.g. `METPO:1007410` for the leaves) or to a recognized external METPO
  IRI (`METPO:1000000`).
- Subset tag: all 14 data rows carry `metpo_traitmech_2026_05`.
- Scope-A coverage: not applicable (0 `traitmech:NNNNNN` IDs in corpus).
- Scope-C coverage: all 10 `CausalNodeTypeEnum` permissible values appear
  as leaf rows whose `definition_source` contains
  `CausalNodeTypeEnum.<VALUE>`.

### ROBOT / ELK pass — PASSED

Run via `just robot-validate-proposal metpo_traitmech_v1` (wraps
`scripts/robot_validate_proposal.py`, which mirrors
`kg-microbe/scripts/extract_metpo_proposals.py::validate_with_robot`).
The script auto-discovers `robot` from `$ROBOT`, `$ROBOT_BIN`, `PATH`, or
`../kg-microbe/data/raw/robot`.

```
=== robot-validate-proposal summary ===
  merged.owl lines:    8589
  reasoned.owl lines:  8595
  delta:               +6
  status:              PASS (no UNSAT, ELK exited 0)
```

Pipeline: `robot template` on the classes TSV → `robot merge` with
`data/raw/metpo.owl` → `robot reason --reasoner ELK --axiom-generators
"SubClass EquivalentClass"`. All three commands exited 0 with no UNSAT
warnings. The +6-line delta is five trivial `subClassOf owl:Thing`
inferences and a whitespace tweak on the METPO root — no unintended
class collapses.

Outputs (regenerable): `reports/robot/metpo_traitmech_v1/{classes,merged,reasoned}.owl`.

## Upstream path

1. Open a PR / issue at [berkeleybop/metpo](https://github.com/berkeleybop/metpo)
   attaching `metpo_proposal_classes_robot.tsv` and this `proposal.md`.
   Reference the subset tag `metpo_traitmech_2026_05` so reviewers can
   filter the cohort.
2. METPO maintainers may renumber the IDs into a different block during
   minting; the `definition_source` and `subset` columns survive renumbering.
3. After METPO release with the minted IDs lands, refresh
   `data/raw/metpo.owl` via `just refresh-metpo` and re-seed
   (`just seed-from-metpo --apply`). The `CausalNodeTypeEnum` schema enum
   can then optionally be cross-walked to the new METPO IDs in a future
   schema commit.

## Round-trip plan (Scope A)

v1 has no Scope-A rows because no `traitmech:NNNNNN` IDs exist in the corpus
yet. The mechanism, when first needed, will be:

1. Curator mints `traitmech:NNNNNN` for a trait absent from METPO (per
   `manage-identifiers` skill).
2. A future TraitMech cohort (likely v1.1 via Path B "extend in place") adds
   the trait as a new class row, citing the original TraitMech record as
   `definition_source`.
3. After upstream mints the real METPO ID:
   - Update `data/raw/metpo.owl` (`just refresh-metpo`).
   - Re-seed and migrate the YAML's `identifier:` from `traitmech:NNNNNN`
     to the new `METPO:` CURIE.
   - Preserve the retired `traitmech:NNNNNN` in `synonyms:` so external
     references don't break.

## Change log

- v1, 2026-05: initial proposal. Lifts 3 top-level domain classes
  (`trait causal graph`, `trait causal node`, `trait causal edge`) plus the
  full `CausalNodeTypeEnum` permissible-value set (1 parent + 10 leaves).
  14 class rows total, no predicates.
