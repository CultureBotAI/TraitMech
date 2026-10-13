# Nutritional Fungal Mycoparasitism

## Context And Scope

One Scope-A ecological CLASS, `traitmech:000717`, proposed as `METPO:1067000`:
**nutritional fungal mycoparasitism**. A fungus obtains nutrients at the
expense of another fungus, either from the living host or after killing it.

| Scope | Rows | Parent | Leaves |
|---|---:|---|---:|
| A: new phenotype | 1 | METPO:1000059 phenotype | 1 |
| B: causal predicates | 0 | Not applicable | 0 |
| C: schema enums | 0 | Not applicable | 0 |

This is a reusable trophic phenotype, not a pairing observation or gene.
Nutrition at host expense is essential; killing, penetration, obligacy and
one molecular mechanism are not universal requirements. Both actor and host
are fungi; historical oomycete examples are not imported. Fungicolous
association, antagonism or scavenging preexisting dead material alone is
insufficient. The nutritional qualifier preserves the strict sense without
claiming that all uses of bare mycoparasitism denote the same phenotype.
No exact synonyms, xrefs, SSSOM mappings, canonical taxa, protein examples or
causal graph are asserted. The record remains `PROPOSED`.

## Evidence And Definition Authority

- [Jeffries 1995](https://doi.org/10.1139/b95-389): directly read review
  defining strict nutritional mycoparasitism, not experimental replication.
  Its [institutional abstract](https://kar.kent.ac.uk/19621/) supports the
  contiguous excerpt. Native resolution remains `UNRESOLVED`.
- [Pellegrini et al. 2012](https://doi.org/10.1002/rcm.6131), PMID:22302490:
  scientific Results abstract supports labeled host-carbon assimilation in
  contacting fungal mycelium. It does not alone prove killing or a transfer
  route. Native excerpt verification: `VERIFIED`; full text unread.
- [Pellegrini et al. 2013](https://doi.org/10.1016/j.apsoil.2012.12.005):
  directly read [institutional scientific abstract](https://iris.unipv.it/handle/11571/604013?mode=complete),
  also returned as AGR:IND500606635, not PubMed. Native match: `VERIFIED`.
  The selected soil experiment uses a sterile microcosm and culture-out
  before isotope analysis, not direct field flux.

The [author-deposited thesis](https://openpub.fmach.it/retrieve/handle/10449/23970/10775/Doctoral%20THESIS%20Corneo%20no%2021127.pdf)
identifies the 2013 DOI for Chapter 3; journal-version identity is unverified.
Selected main text and actual figure/table pages were inspected, not all raw
data or supplements. It qualifies the soil endpoint and separates plate
inhibition from broth viability. Source numerical and sampling-day conflicts
remain explicit in the record. PCR and washing controls do not exclude every
alternative carbon-transfer route. The two experimental papers share all six
authors. The thesis is not a third independent experiment.

The [source sidecar](../../research/traits/ecology/nutritional_fungal_mycoparasitism-source-verification.json)
retains source identities, short excerpts, hashes, locators, assay/version
limits and actual native outcomes. Full publications are not redistributed.
Notice checks were bounded; failed publisher routes are not notice clearance.

## Hierarchy Decisions

`METPO:1000059` phenotype is the conservative parent; its existing parent is
`METPO:1000188`. Local parasitism (000043) inherits persistent physical
association from symbiosis (000040). Jeffries' destructive encounters do not
necessarily satisfy that narrower local umbrella. This hierarchy question
remains attributed and open rather than silently reparenting either record.

Bacterial mycophagy (000696) has a different actor. Microbial haustorium
formation (000663) denotes an interface, not nutritional proof. Saprotrophy
(000055) does not alone demonstrate attack on a living host. None is exact,
and no organism-level disjointness is implied. No exact older node, synonym
or parent TODO requiring migration was identified in the inspected scope.

Pinned and current METPO broad lexical matches `METPO:0000261`,
`METPO:000262`, `METPO:1000125`, `METPO:1000197`, `METPO:1000198` and
`METPO:1000227` are deprecated with an `OMO:0001000` obsolescence reason,
not exact active counterparts. No replacement or consider annotation was
observed. That reason does not invalidate the biology or authorize reuse.
No historical CURIE is added as an exact xref; the pinned ontology is unchanged.

## Novelty And Reservation

Acceptance: `2026-10-13T11:20:51Z`. Refreshed main:
`4de96161ea95221bb978bf816d94613230b65cf3`.
Novelty and reservation searches included ignored and hidden available files
in 166 registered or retained locations. Unavailable registered worktrees
received tracked-history fallback: 139 unique heads, with CommunityMech
reservation fallback restricted to proposals. Supplemental novelty screening
covered all unique UTF-8 blobs of the retained TraitMech and CommunityMech
heads; binary exclusions and regex positive controls are recorded.

Remote checks covered 11 open/draft PRs, all 783 nonremoved changed-file
blobs and 587 selected upstream blobs. Relevant pending heads: TraitMech
#1782, #1476, #973 and draft #924; CommunityMech draft #935; METPO #644,
#643, #641, #640, #638 and #629. Pagination, file counts, blob/SHA-256
identities and stable before/after heads were checked.

- METPO main: `1efc8c73009200b9cb74d125df6a0ea5dc36cb93`.
- CommunityMech main: `8df89370be840a4b58a9d8a7407c66c7471a5085`.
- KG-Microbe main: `bb3072f59f6d9e098ae40c4dce2c60a9dec9af42`.

Two bare-number hits, `-2.1067007` and `-1.1067002`, are embedding values
for METPO:1000658 and METPO:1000805 in draft #924, not identifiers.
All 203 interval overlaps concern the formal editor namespace envelope
or retained documentation of it, not competing narrower reservations.
No conflicting reservation remained in the checked scope. Lost untracked
or ignored files, symlink directories and archives are not reconstructed;
pending-file checks do not inspect unchanged files in every pending tree.
This is bounded screening, not global novelty proof or atomic allocation.
Recheck current heads before publication.

## ID Space And Files

- Local identifier: `traitmech:000717`.
- Cohort: `metpo_traitmech_v593`.
- Reserved block: `METPO:1067000`-`METPO:1067099`.
- Only populated placeholder: `METPO:1067000`, not a released identifier.
- Subset: `metpo_traitmech_2026_10`; curator: codex.
- No overlap with CommunityMech v1 or its inspected extensions.

| Artifact | Rows |
|---|---:|
| `metpo_proposal_classes_robot.tsv` | 2 headers + 1 class |
| Property template | 0; omitted |
| SSSOM mapping template | 0; omitted |

The two 11-column headers follow the pinned upstream class template,
including required blank ROBOT cells. Citations are provenance, not exact
external equivalence. Local ROBOT expansion must use `https://w3id.org/metpo/`.

## Verification And Upstream Path

Before publication: schema/strict validation, focused/full tests, snippet
checks, proposal verification, ROBOT/ELK and RDF parent inspection, generated
products, full QC, history and a saved adversarial review. This list is a
requirement, not a claim that unfinished checks passed.

After curator sign-off, submit the narrative and TSV to METPO or KG-Microbe.
Adoption requires a separately reviewed pinned release refresh and migration
preserving local-identifier provenance and incoming references. The placeholder
does not authorize an automatic ID swap or `REVIEWED` promotion.

## Change Log

- 2026-10-13, v593: one fungal nutritional phenotype with three DOI excerpts.
