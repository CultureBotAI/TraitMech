# METPO proposal v566: biomineralization

## Context and scope

Lift `traitmech:000690` as `METPO:1064300`: one PHYSIOLOGY class,
kept PROPOSED pending human signoff. Scope A: one class; B/C: zero.
The organismal phenotype is microbial mediation of mineral formation,
not the material, an isolated process, a gene or a sequence feature.
This closes two live production-trait parent gaps.

## Hierarchy and boundaries

Parent: phenotype `METPO:1000059`, below quality `METPO:1000188`.
The broad usage includes controlled, induced and organic-matrix-mediated
formation. Benzerara et al. section 2 explicitly includes passive organic
matter effects under biologically influenced biomineralization. That usage
is not silently narrowed to intracellular, carbonate-only or genetically
controlled production. Mere mineral association, ion adsorption, uptake of
preformed particles, dissolution or organic-substrate mineralization does
not establish the phenotype. Isolated nonliving-matrix experiments alone
do not establish an organism-level assignment. No universal urease,
benefit, growth dependence or shared molecular mechanism is asserted.

Coccolith production and siliceous scale production definitions entail
this broader formation phenotype. Reparent both to `traitmech:000690` and
resolve their parent TODOs while preserving historical rationales, evidence,
definitions and separate exemplar/mechanism gaps. This is definition-based
hierarchy inference, not new experimental evidence for either child.
No automatic cross-axis reparenting of magnetosome or ferrosome organelle
records is made. The magnetosome graph's node is specifically magnetosome
biomineralization, not an exact occurrence of this umbrella. The
iron-sulfide-formation node in disproportionation is also narrower.
No synonyms, xrefs, SSSOM equivalences or disjointness are asserted.

Additional upstream axioms requested on adoption:

- `METPO:1064100 SubClassOf METPO:1064300` (siliceous scale production, v564).
- `METPO:1064200 SubClassOf METPO:1064300` (coccolith production, v565).

Preserve historical v564/v565 templates: their phenotype axioms remain true.
Following v512, the refinements are explicit upstream curation requests,
not axioms emitted by the v566-only template. Do not re-emit old reserved IDs.

## Evidence and limits

- [Benzerara et al. 2011](https://doi.org/10.1016/j.crte.2010.09.002):
  terminology authority. Abstract, Introduction and section 2 directly read
  in publisher HTML. This review is not counted as independent experimental
  replication. Its remainder and actual figures were not audited here.
- [Rodriguez-Navarro et al. 2012](https://doi.org/10.1128/AEM.07044-11),
  PMID:22447589, PMC3346411: induced precipitation in inoculated cultures,
  contrasted with uninoculated substrate controls. Scientific Abstract,
  Introduction, Methods, Results and relevant Discussion read in publisher
  HTML; actual Figures 1/6 inspected. The snippet is Discussion text.
  Substrate and medium qualify phase selection; an amorphous precursor is
  suggested, not independently established by morphology. Other images were
  not inspected. Direct curl returned 403 despite readable publisher HTML
  through the browsing tool; this is not a claim of full-text inaccessibility.
- [Sviben et al. 2016](https://doi.org/10.1038/ncomms11228),
  PMID:27075521, PMC4834641: controlled coccolith calcite production.
  Scientific Abstract, Introduction, calcite-resupply Results and Discussion
  checked in official Europe PMC XML. The snippet is scientific-abstract
  text. Historical AWI1516 does not establish every strain's current phenotype;
  the separate calcium compartment is not a proven necessary direct precursor.
  No new figure/supplement audit is claimed for the parent.
- [Nomura and Ishida 2016](https://doi.org/10.1016/j.protis.2016.05.002),
  PMID:27348459: siliceous-scale formation, scientific abstract directly read
  at https://rrc.nbrp.jp/references/56432?lang=en. Full Methods and figures
  unread. Cytoskeletal association is not molecular necessity; production
  and later shell assembly remain distinct.

All four evidence items have short, contiguous source snippets. Keep native
abstract-resolver outcomes separate from direct full-text checks. Canonical
examples await joint assay-strain, provenance and taxonomy verification;
community results must not be attributed to every member. No universal
protein pathway or unverified accession is added. Two parent discussions
remain OPEN: scope/mapping and exemplar/mechanism review.

## Allocation and novelty

Reserve `traitmech:000690`, cohort v566 and the full
`METPO:1064300-1064399` block; populate only 1064300. Subset:
`metpo_traitmech_2026_10`. Allocation main:
`0e33d17c84b579d827db87e268f5b1780284a422`.

Ignored-and-hidden searches covered all 23 pre-existing TraitMech worktrees,
including ontology, traits, synonyms, graphs, discussions, research, history,
proposals and generated artifacts. Patterns included biomineralization/sation,
biogenic mineral, bioprecipitation, biosilicification, biologically induced/
controlled/influenced mineralization, mineral formation/production/precipitation,
the cited source identifiers and prospective local/cohort/full-block IDs.
No exact record or conflicting reservation was found. Existing hits concern
the two parent gaps, narrower mineral structures/processes and research
contexts, not an exact broad trait. All 12,617 pinned METPO triples were
parsed; mineral-related matches are two obsolete relation labels, not this
class. Fresh seeding emitted 399 records, 55 IDs absent from 1,084 live
records. The complete 1,546-row release delta, 153-row active review and
their policy were consulted; absent IDs are leads, not exhaustion evidence.
The full prospective block was also searched across CommunityMech including
ignored/hidden files. Its sole numeric hit was a Biopython test chromosome
length, not a reservation; the CommunityMech v1 blocks do not overlap.

Paginated changed-file lists and immutable curation blobs were inspected
for every open PR, including drafts, on 2026-10-10:

| PR | Head | Reservation |
| --- | --- | --- |
| #1802 | `a74d9278b3ce5971d773a4e81616373f795f2816` | Existing Shedu 000220; no new ID/block |
| #1782 | `35099af2b7d5347f2ca6e418c4a139979071644d` | No curation paths |
| #1476 | `b4b8d1280e25bd3e340241e7ac23b51bbe7aaec3` | No curation paths |
| #973 | `331f9517bbdf4d2c9fa97b338ee59a8986f2f174` | No curation paths |
| #924 (draft) | `e61ce120b8da953da097b9f94bfed7f292e5675a` | No curation paths |

Recheck main and reservations before publication. Only the two named child
records may change; protected spore germination and unrelated work are excluded.

## Artifacts and verification

One 11-column class TSV, no property or SSSOM file. Three trailing empty
directive cells are required. Upstream contract remains at
`1408e7099d039026d7611c240938d8e177753406`; class/property headers were
rechecked at blobs `b590cf303dc2fbdd57bed021668641cd0c32396d` and
`b2f9f4ceb6b6893a8b27d7fe41e859f08c4b2990` (11/13 columns).
Use the maintained w3id METPO namespace, not the upstream legacy OBO example.

The writer defaults to dry run, guards parent/child identity and discussion
preimages, prevalidates the complete coupled change and supports exact replay.
Tests use controlled historical preimages. Require proposal/ROBOT/ELK,
strict/LinkML/history/QC/products, snippet checks, focused/full tests,
retained adversarial review and desktop/mobile page inspection. Actual
outcomes belong in the PR and review; no unrun check is claimed here.

## Upstream and round trip

After human signoff submit the TSV and both child axioms to berkeleybop/metpo.
No upstream issue or accepted term is claimed. On acceptance, refresh the
pinned ontology, migrate the local identifier and references, and preserve
minting provenance and append-only history without duplicate primary records.

## Change log

- v566, 2026-10-10: propose biomineralization and refine two production parents.
