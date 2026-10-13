# Fungal Nematophagy

## Context And Scope

One Scope-A ecological CLASS, `traitmech:000719`, proposed as
`METPO:1067200`: **fungal nematophagy**. A nutritional phenotype in which a
fungus consumes nematodes as food. The record remains `PROPOSED`.

| Scope | Rows | Parent | Leaves |
|---|---:|---|---:|
| A: feeding phenotype | 1 | METPO:1000059 phenotype | 0 |
| B: causal predicates | 0 | Not applicable | 0 |
| C: schema enums | 0 | Not applicable | 0 |

Live and previously dead nematodes are included. Capture structures,
paralysis, killing, starvation, obligacy, a particular toxin and exclusive
nutrition are not universal requirements. Contact or paralysis alone does
not establish feeding. No protein mechanism or quantified assimilation is
asserted. No exact synonym, xref, SSSOM mapping or causal graph is added.

## Evidence

- [Marlin et al. 2019](https://doi.org/10.3390/f10050404): directly inspected
  Introduction terminology and Figure 2a support consumption and the
  qualified Pleurotus ostreatus example. Two excerpts total 17 words.
  Native abstract checks remain `UNRESOLVED`, not manually relabeled.
- [den Belder and Jansen 1994](https://horizon.documentation.ird.fr/exl-doc/pleins_textes/fan/40780.pdf):
  directly inspected Summary and feeding observations support nonexclusive
  modes, including previously killed prey. Native URL verification is not run.
- [Lin et al. 2023](https://doi.org/10.1371/journal.pbio.3002400),
  PMID:37988381: direct full-text result and inspected Figure 5, Table 1
  and S7 support internal growth interpreted as digestion. Native result:
  `NOT_IN_ABSTRACT`. Engineered imaging strains are not natural exemplars.

The [verification sidecar](../../research/traits/ecology/fungal_nematophagy-source-verification.json)
retains source URLs/hashes, section checks and native outcomes. Source
discrepancies remain explicit in the record; disputed host ranges, numerical
rates and gene identities are not adopted. PLOS's linked 2025 Update Article
is not a correction. MDPI notice-page access returned 403. Notice checks and
figure inspection are bounded, not comprehensive clearance or raw-data review.

## Hierarchy Decisions

Use `METPO:1000059` phenotype, below `METPO:1000188`, pending a closer
feeding hierarchy. Trap formation (000718) is structural; its five children
are not feeding subtypes. Mycoparasitism (000717) involves fungal prey;
predatory bacterium (000054) involves a bacterial actor and prey. Phagotrophy,
myzocytosis and pallium feeding specify different uptake modes. Local
parasitism inherits persistent association, which this definition does not
require. Saprotrophy can overlap; organism-level disjointness is not asserted.

Historical `METPO:0000005` and `METPO:000005` replace to active trophic type
`METPO:1000631`, a carbon/energy axis rather than exact nematode feeding.
Active `1000644` and `1000731` concern organic carbon and nutrient availability.
Deprecated `0000261`, `000262`, `1000125` and `1000227` concern fungal spores
or parasitism, with no replacement/consider observed. Their `OMO:0001000`
reasons do not invalidate biology or authorize reuse. No historical ID is an
exact xref. The pinned ontology is unchanged. Current editor OWL is a small
metadata skeleton; current class assessment uses the released OWL and templates.

## Novelty And Reservation

Acceptance: `2026-10-13T15:34:51Z`; base
`e0f3176847fe446a5af3322fe6d0864c03db42d2`.
Ignored and hidden files were included across 170 known locations, with
positive-controlled tracked-history checks for 139 retained heads. Canonical
matches were existing trap morphologies, autophagy, myzocytosis and bacterial
community contexts, not this fungal feeding phenotype. No exact unresolved
node or synonym required repair. Generated views were traced to their owners.

Remote novelty and reservation checks covered 11 open/draft PRs, 783
nonremoved pending blobs and 587 selected upstream blobs, with stable heads:

- TraitMech #1782, #1476, #973 and draft #924.
- CommunityMech draft #935; main `8df89370be840a4b58a9d8a7407c66c7471a5085`.
- METPO #644, #643, #641, #640, #638 and #629;
  main `1efc8c73009200b9cb74d125df6a0ea5dc36cb93`.
- KG-Microbe main `bb3072f59f6d9e098ae40c4dce2c60a9dec9af42`.

Three exact-number hits are `size = 1067267` wheel metadata in METPO lockfiles,
not term IDs. All 318 interval overlaps reference the broad
`1000000-1999999` editor envelope or documentation, not narrower reservations.
No competing allocation remained within this inspected scope. Recheck before
publishing; this is not atomic allocation.

Unavailable ignored/untracked history, directory symlinks and local archives
were not reconstructed. Pending-file screening does not inspect every
unchanged PR-tree file. These are bounded checks, not global novelty proof
or exhaustion of microbial-trait discovery.

## ID Space And Files

Reserve local `traitmech:000719`, cohort `metpo_traitmech_v595` and the whole
`METPO:1067200`-`METPO:1067299` block. Only `METPO:1067200` is populated;
it is not released. Subset: `metpo_traitmech_2026_10`. No overlap with
inspected CommunityMech v1 or extensions was found.

| Artifact | Rows |
|---|---:|
| `metpo_proposal_classes_robot.tsv` | 2 headers + 1 class |
| Property template | 0; omitted |
| SSSOM template | 0; omitted |

The 11-column headers preserve required empty cells. Citations are not
equivalence mappings. METPO IRIs must use `https://w3id.org/metpo/`.

## Verification And Upstream Path

Required before publication: guarded-writer tests, strict/schema validation,
native snippets with direct full-text checks, NCBI example resolution,
proposal coverage, ROBOT/ELK with RDF parent inspection, history, generated
products, full QC and a saved adversarial record review. This is a requirement,
not a claim that unfinished checks passed.

After curator sign-off, submit the template to METPO or KG-Microbe. Adoption
requires a separately reviewed pinned-release refresh and identifier migration,
preserving local provenance, the old identifier and incoming references.
Automated validation does not authorize human `REVIEWED` promotion.

## Change Log

- 2026-10-13, v595: fungal feeding phenotype, three sources, four excerpts,
  one qualified example and explicit hierarchy/mechanism limits.
