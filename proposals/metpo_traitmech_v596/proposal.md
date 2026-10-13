# Lethal Nematicidal Activity

## Context And Scope

One Scope-A physiological CLASS, `traitmech:000720`, proposed as
`METPO:1067300`: **lethal nematicidal activity**. A physiological capability
of a microorganism to kill nematodes. The record remains `PROPOSED`.

| Scope | Rows | Parent | Leaves |
|---|---:|---|---:|
| A: killing capability | 1 | METPO:1000059 phenotype | 0 |
| B: causal predicates | 0 | Not applicable | 0 |
| C: schema enums | 0 | Not applicable | 0 |

This is the acting microbe's capability, not an assay, pesticide molecule,
treated nematode's susceptibility or sequence feature. Reversible paralysis,
repellence, reduced hatching and plant defense induction alone are insufficient.
Feeding and infection are not required. No universal host range, life-stage
coverage, dose, secretion route, environmental efficacy or safety is asserted.

## Evidence

- [Kusakabe et al. 2022](https://doi.org/10.1128/spectrum.02577-21),
  PMID:35138171: culture-extract fractionation links microbial production to
  lethal activities of isolated compounds. Commercial standards were used
  for dose-response assays. Actual Figures 2/3 and Table 4 were inspected;
  Table 4 concerns reversible lower-dose indole paralysis. The 22-word
  Discussion excerpt (printed/PDF page 12) explicitly links nematicidal
  metabolites to Caborca cultures. It matches the XML and typeset PDF;
  native verification reports `NOT_IN_ABSTRACT`. Indole's lower-dose paralysis
  is not equated with the high-concentration killing reported separately.
- [Saharan et al. 2023](https://doi.org/10.1038/s41598-023-33669-z),
  PMID:37088805: fungal culture-filtrate juvenile mortality, with fresh-water
  recovery confirmation but unspecified recovery duration/criterion.
  Actual Figure 4, supplement text/tables and its image were inspected.
  The 15-word Results excerpt is directly matched, natively `NOT_IN_ABSTRACT`.
  Strain/accession contradictions remain explicit; no canonical taxon is added.
- Discussion-only [Harada and Yoshiga 2015](https://doi.org/10.3725/jjn.45.51):
  viability-assay limitations, not supporting trait evidence or a definition
  citation. The 13-word abstract
  excerpt is stored in structured discussion evidence with `NO_EVIDENCE` role
  and matches the publisher and PDF. Native result remains `UNRESOLVED`;
  the exact DOI query returned zero results, despite verified publisher and
  Crossref identity. This does not establish absence from all indexing services.

The [verification sidecar](../../research/traits/physiology/lethal_nematicidal_activity-source-verification.json)
separates the two supporting evidence rows from the discussion-only source,
retaining hashes, direct locators, source-status checks and limitations. No
complete supplement or raw-data audit is claimed. No causal graph or protein
example is proposed while strain identities and mechanisms remain unresolved.

## Hierarchy Decisions

Use `METPO:1000059` phenotype, below `METPO:1000188`. Animal pathogen
`METPO:1004002` requires infection; pathogenic-to-host `METPO:1004000`
does not replace this product-mediated killing endpoint. Fungal nematophagy
`traitmech:000719` requires consumption, whereas trap formation `000718`
is structural. Predatory bacterium `000054` requires bacterial prey and
nutrient acquisition. These can overlap without organism-level disjointness.

Pinned and current METPO annotation/status inspection found no exact active
or deprecated counterpart in the inspected scope. The current editor OWL
is a metadata skeleton; released OWL and templates provide the class context.
The pinned ontology is unchanged. Authority-resolved `CHEBI:25491` denotes
a nematicide chemical and is not an equivalent phenotype. No exact synonyms,
xrefs or SSSOM mappings are asserted.

## Novelty And Reservation

Acceptance: `2026-10-13T17:31:43Z`; base
`ac91b722fd0ab84cd7f68b0fae26cdca0290d471`.
Ignored and hidden files were included across 173 known locations
(172 available), plus positive-controlled tracked-tree searches of 139
retained heads. Existing TraitMech mentions distinguish trapping/feeding
from nematicidal activity; they are not exact records or ungrounded exact
causal nodes. CommunityMech TYQ1 observations, cached papers and generated
views are community context, not a competing TraitRecord or reservation.
KG-Microbe's nematicide mappings point to a chemical role, not this phenotype.

Remote checks covered 11 open/draft PRs, 783 nonremoved pending blobs and
587 selected upstream blobs with stable heads:

- TraitMech #1782, #1476, #973 and draft #924.
- CommunityMech draft #935; main `8df89370be840a4b58a9d8a7407c66c7471a5085`.
- METPO #644, #643, #641, #640, #638 and #629;
  main `1efc8c73009200b9cb74d125df6a0ea5dc36cb93`.
- KG-Microbe main `1804424c098337016889ed81a1b3eda01aedeaf0`.

Two exact-number hits are decimal embedding coordinates in draft #924,
not term identifiers. All 379 interval overlaps are the broad
`1000000-1999999` editor envelope or documentation, not narrower reservations.
No conflicting reservation remained in the inspected scope. Recheck current
main and pending heads before publication; this is not atomic allocation.

Unavailable ignored/untracked history, directory symlinks and arbitrary
local archives were not reconstructed. Pending checks cover changed, not
every unchanged, PR-tree file. This is bounded novelty assessment, not
exhaustion of microbial-trait discovery.

## ID Space And Files

Reserve local `traitmech:000720`, cohort `metpo_traitmech_v596` and the
whole `METPO:1067300`-`METPO:1067399` block. Only `METPO:1067300` is
populated; it is not released. Subset: `metpo_traitmech_2026_10`.
No overlap with inspected CommunityMech v1 or its extensions was found.

| Artifact | Rows |
|---|---:|
| `metpo_proposal_classes_robot.tsv` | 2 headers + 1 class |
| Property template | 0; omitted |
| SSSOM template | 0; omitted |

The 11-column headers retain required empty cells. Definition citations are
not equivalence mappings. METPO IRIs must expand to `https://w3id.org/metpo/`.

## Verification And Upstream Path

Required before publication: guarded-writer tests, schema/strict validation,
native snippet checks with direct-source verification, proposal coverage,
ROBOT/ELK with RDF inspection, history, generated products, full QC and
a saved adversarial record review. This lists requirements, not unfinished
checks as successes.

After curator sign-off, submit the template to METPO or KG-Microbe. Adoption
requires a separately reviewed pinned-release refresh and identifier migration,
preserving the old local ID, provenance and incoming references. Automated
validation does not authorize promotion to human `REVIEWED` status.

## Change Log

- 2026-10-13, v596: lethal microbial capability, two supporting excerpts and
  one discussion-only methodological excerpt, explicit assay/provenance
  limitations and two open discussions. Issue #1916 corrected the initial
  context citation's placement and excluded it from definition annotations.
- 2026-10-13, #1917: replaced the compound-only snippet with a producer-linked
  Discussion result and moved method context into structured discussion evidence.
  Identity, hierarchy, two-source definition provenance and prior history remain.
