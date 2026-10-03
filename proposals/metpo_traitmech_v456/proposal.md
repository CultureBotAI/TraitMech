# METPO Proposal v456: Druantia Type II

## Context

This cohort lifts `traitmech:000579 Druantia type II system`, an organism-level
DruM/F/G/E locus-possession class, not a gene, profile hit, or assay result.
The definition is supported by Payne et al. (DOI:10.1093/nar/gkab883).
Hou et al. (DOI:10.65215/LTSpreprints.2026.06.18.000273) adds a natural
Pf-5 source and carefully bounded protein experiments.

Fresh METPO seeding emitted 399 identifiers, 344 already in the 973-record
pre-change corpus and 55 absent. Absence was not taken as proof of novelty.
Whole-repository `rg -uu` searches included ignored and hidden files, the OWL,
history, research, proposals and generated content. Type-II mentions were
family/sibling context, not an exact child. No exact METPO term was found.
The existing family discussion explicitly identified the architectural gap.

## Scope

| Scope | Rows | Parent | Leaves |
|---|---:|---|---:|
| A: local trait lift | 1 | Druantia system | 1 |
| B: predicates | 0 | Not needed | 0 |
| C: schema enums | 0 | Not biological trait proposals | 0 |

## Hierarchy Decisions

| Proposed ID | Local ID | Label | Parent |
|---|---|---|---|
| METPO:1053300 | traitmech:000579 | Druantia type II system | METPO:1053100 |

The local parent remains `traitmech:000234`. Its corrected family proposal is
v454 `METPO:1053100`, which supersedes the unminted v111 family row. Historical
proposals are unchanged. Type I, III and IV remain siblings; multiple loci can
coexist in one genome, so organism-level possession classes are not disjoint.
No gene, helicase-activity or experimental resistance child is minted.

## Evidence Boundaries

- Payne's comparison identifies type-II DruE/F/M/G and distinguishes type IV
  by replacement of M/G with DruL. It supports architecture, not component
  essentiality across all taxa. The snippet was matched to primary PMC8565338
  XML, not a generated research summary.
- Hou version 2, posted July 8, 2026, is an unreviewed preprint. The primary
  [PDF](https://langtaosha.org.cn/lts/en/preprint/download/273/1236) and
  [supplement](https://langtaosha.org.cn/lts/en/preprint/download/273/1235)
  were inspected, including the Results and Limitations pages. The version-1
  June abstract is not the evidence version used here.
- The preprint supplies Pf-5 locus possession and isolated DruE biochemistry.
  Its limited heterologous infection assays do not validate native-host or
  reconstituted full-system defense. Accordingly, the record preserves the
  protein findings in evidence notes without a full-system causal graph.
- Protein anchors are available, not an alleged missing-data barrier:
  RCSB [9WAE entity 1](https://data.rcsb.org/rest/v1/core/polymer_entity/9WAE/1)
  links PFL_3016 to [Q4KCB1](https://rest.uniprot.org/uniprotkb/Q4KCB1.json).
  On October 3 the UniProt entry is live and unreviewed, entry version 115,
  sequence version 1, taxon 220664. NCBI independently resolves that taxon to
  Pseudomonas protegens Pf-5. Neither accession is a trait xref.
- Pinned DefenseFinder XML at `afb0e5a8b466be53586b13266f5d38d98c3ac268`
  requires one mandatory DruE slot and three total matches, with M/F/G
  accessory. DruF accepts DruF4; DruE accepts E2/E3/E4. Spacing is five genes;
  there are no forbidden slots. A call can therefore be incomplete relative
  to the four-component biological definition.
- Pinned PADLOC YAML at `9e380165633a8d6aef93b5a164cea0f3359bd33f`
  requires four core/total profiles E2/F2/G2/M2. DruK is secondary, spacing
  is three genes, strand is unrestricted, and neutral/prohibited lists are NA.
  Both model files were parsed structurally. The detector namespace is not an
  exact synonym and no detector call is treated as experimental defense.

## ID Space And Subset

The fresh v456 block is `METPO:1053300-1053399`; only `1053300` is used.
Whole-repository ignored-and-hidden collision searches found no allocation
before writing. This follows v455's `1053200` block and does not collide with
CommunityMech v1 `1007100-1007220`. The subset is
`metpo_traitmech_2026_10`. These remain proposal placeholders, not released
METPO IDs.

## Files

| File | Data rows |
|---|---:|
| metpo_proposal_classes_robot.tsv | 1 |
| proposal.md | Narrative |
| Property and SSSOM templates | Omitted: no predicate or equivalent mapping |

The 11-column header follows the live kg-microbe `master` class template.
The empty trailing ROBOT cells are intentional. The exact synonym is a lexical
variant; raw profile names and the bare protein name are not exact synonyms.

## Verification

Run `scripts/verify_metpo_proposal.py proposals/metpo_traitmech_v456`,
`scripts/robot_validate_proposal.py proposals/metpo_traitmech_v456` and
`scripts/verify_metpo_proposal.py --coverage`. The PR records the actual
results of these checks, corpus QC, writer tests, snippet checks and rendering.

## Upstream Path

Submit the verified template through the existing
[METPO tracking issue #535](https://github.com/berkeleybop/metpo/issues/535),
verified OPEN on 2026-10-03. Include the corrected v454 family parent rather
than the superseded v111 meaning. This local artifact reserves a proposal,
not an upstream acceptance.

## Round-Trip Plan

After upstream acceptance, refresh the METPO snapshot, seed into a temporary
tree, migrate the local identifier to the released METPO CURIE, and preserve
`traitmech:000579` in provenance. Update parent references, dashboards and
rendered pages through maintained generators. Do not emit unminted IDs as if
they were released METPO terms.

## Change Log

- v456, 2026-10-03: add Druantia II possession with version-pinned experimental
  limits, a natural locus exemplar and independently parsed detector rules.
