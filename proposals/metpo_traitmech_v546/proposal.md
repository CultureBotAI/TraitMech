# Fungal Internal Mycorrhizal Vesicle Formation: METPO Proposal v546

## Scope and Hierarchy

Propose `traitmech:000670 fungal internal mycorrhizal vesicle formation`,
a PROPOSED MORPHOLOGY class, from main
`4e7e8cd1ceaf7e74f9cfce18f8174c3edfe9b4dd`. Scope A contains one class;
Scopes B and C contain no predicates or schema vocabulary. This is a fungal
phenotype, not a structure record, sequence feature or plant observation.

Use active `METPO:1000059 phenotype`, below `METPO:1000188 quality`.
Parsed pinned METPO contains 12,617 triples and no exact active class;
`METPO:1000198 mycorrhization` and `METPO:1000126 gas vesicle` are obsolete,
as also recorded in the release-delta review. The former is not a usable
active parent. A closer phenotype parent remains an OPEN discussion.

Internal refers to plant-tissue location, including intracellular and
intercellular structures. It does not mean free in host cytoplasm or a
membrane-trafficking vesicle. Root-only wording would exclude the directly
observed liverwort example. The qualified label separates these structures
from Brundrett's external/accessory vesicle usage for auxiliary bodies.
Gas vesicles (`000070`), extracellular membrane vesicles and branched
arbuscules (`000664`) are different structures. Chlamydospore formation
(`000658`) is not equivalent to every hyphal storage swelling; historical
spore/vesicle boundaries are not resolved by this addition. No exact
synonyms, xrefs, SSSOM, subclass or disjointness claim to these neighbors
is asserted. Formation alone does not establish reciprocal benefit.

## Evidence and Example

- [Brundrett's author resource](https://www.mycorrhizas.info/vam.html),
  version 2 (2008), C.5 and glossary F: directly read terminology, not an
  independent experiment. Its root-context formulation is broadened by
  the primary thallus observation below. The resource's images were not
  inspected, and historic genus-level statements are not universal absences.
- [Kinden and Brown, 1975](https://doi.org/10.1139/m75-258), PMID:172206:
  directly retrieved scientific abstract reports electron microscopy of
  intracellular, lipid-filled vesicles in yellow-poplar roots. The fungal
  species is unnamed in the abstract. Full text and actual images were
  not inspected; wall layers and hypothesized nutrient release are not
  universal morphology or demonstrated transfer claims.
- [Kobae et al., 2019](https://doi.org/10.3390/plants8060142),
  PMID:31151150, PMC6631804: Results 2.2, Methods 3.1-3.3 and actual S1
  were checked in the [primary manuscript](https://rakuno.repo.nii.ac.jp/record/6472/files/R-2020-321_kobae.pdf)
  and [publisher supplement](https://mdpi-res.com/d_attachment/plants/plants-08-00142/article_deploy/plants-08-00142-s001.zip).
  S1 labels vesicles separately from arbuscules in MAFF520053 and
  MAFF520059. Cell-wall staining is not a lipid assay. The 25-day observation
  is not a universal onset; the separate DAOM197198 arbuscule timing
  discrepancy remains separate. ZIP SHA256:
  `90ed36f494305b789cb275c69e0bfd487cf0f1134de512f5d3203b020c838400`.

The canonical example is `NCBITaxon:937382 Entrophospora etunicata`,
MAFF520053/H1-1, under the paper's name Claroideoglomus etunicatum.
The live [NARO record](https://www.gene.affrc.go.jp/databases-micro_search_detail_en.php?maff=520053)
provides field-isolate provenance in separate fields, not a trait quote.
[NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=937382&lvl=4&mode=Info)
confirms the current name and homotypic synonym, not culture reidentification.
The newer [Ohtomo 2025 paper](https://doi.org/10.1264/jsme2.ME25040),
Table 1 and Methods/Results/Discussion, retains H1-1/520053 while describing
primer-dependent ASV resolution. Its figures and supplements were not
inspected. This is provenance context, not independent vesicle evidence;
unknown ASVs do not by themselves establish culture contamination.

No fungal protein mechanism is asserted from host mutations or morphology.
Pooled spores-and-vesicles, root-length colonization and vesicle counts must
remain distinct readouts. Lifespan, propagule function, nutrient transfer
and formation pathways remain explicit research questions.

## Novelty and Allocation

Whole-root searches included ignored and hidden files in the original
checkout, all ten other worktrees, CommunityMech and a complete paginated
open-PR snapshot (13 roots, before this branch was created). The initial
novelty query yielded 638 lines in 37 relative paths, chiefly existing
arbuscule citations, unrelated gas/defense/membrane vesicles and cached
references. Their contexts and neighboring definitions were inspected.
Additional internal/intraradical/mycorrhizal-storage/vesicular-mycorrhizal
aliases, the chosen slug and the 2025 DOI returned no matches across the
same roots. This is not a claim of global trait exhaustion.

Reserve local ID `000670`, cohort v546 and the entire `1062300-1062399`
METPO block, with populated row `METPO:1062300` and subset
`metpo_traitmech_2026_10`. The block/ID/cohort search found 86 incidental
numeric matches in 10 relative paths, not competing reservations.
Pending allocations remain occupied: Hartig #1794 reserves 000667/v543/
1062000-1062099, mantle #1796 reserves 000668/v544/1062100-1062199,
and cord #1798 reserves 000669/v545/1062200-1062299.

Immutable open heads inspected, including drafts:

| PR | Head | Changed files | Curation artifacts |
| --- | --- | ---: | ---: |
| 1798 | 219a0f4b1f5a531759477168e54a1d5c11ea31a6 | 1091 | 6 |
| 1796 | d058d9e1e546e7549fdc2085860fc47524f60c23 | 1096 | 8 |
| 1794 | 7b10b76e22fa48cd82cdf4a52b78955e95f25b1b | 1089 | 4 |
| 1782 | 35099af2b7d5347f2ca6e418c4a139979071644d | 1 | 0 |
| 1476 | a138e46f803b5af9d48969217b86cf7c9a3b61bd | 8 | 0 |
| 973 | 331f9517bbdf4d2c9fa97b338ee59a8986f2f174 | 3 | 0 |
| 924 (draft) | e61ce120b8da953da097b9f94bfed7f292e5675a | 692 | 0 |

All downloaded curation artifacts were Git-blob-hash checked, and the final
head set was rechecked. Main was unchanged before branch creation. Repeat
the reservation check immediately before publishing.

## Template and Verification

The upstream contract is pinned to kg-microbe
`1408e7099d039026d7611c240938d8e177753406`. Hash-checked class template
`b590cf303dc2fbdd57bed021668641cd0c32396d` has 11 columns, and property
template `b2f9f4ceb6b6893a8b27d7fe41e859f08c4b2990` has 13. Only the
one-row class template and this narrative are emitted. Its directive row
preserves three trailing empty cells. CommunityMech's v1/extension blocks
were inspected and do not overlap this reservation.

The dry-run-first writer guards the phenotype projection, exact target and
template replay, prevalidates and uses the validated mutation/history APIs.
Existing records stay unchanged. Controlled fixture tests cover refusal of
drift, dry run, replay and validation failure before writes. The initial
writer dry run and all 20 writer tests pass. On the independent checkpoint
`7d803fd1ee2b43794d9aa779d5426077f2de3ad5`, all 65 expanded focused tests
passed in 1028.19 seconds and all 3,212 full-suite tests passed in 1094.95
seconds. LinkML/strict, proposal/ROBOT/RDF, Ruff, committed QC,
history/products and PR sanity passed. Online taxonomy resolved 744 examples
with zero errors and 24 existing warnings. The maintained snippet resolver
returned VERIFIED for the 1975 abstract and NOT_IN_ABSTRACT for the 2019
body quote; manual primary-source and URL checks are separate, not renamed
resolver passes. Desktop/mobile checks at 1440/390 and inspected screenshots
passed, including the qualified example, evidence, hierarchy and dashboard.

Against its original main, preservation checked all 1,061 prior YAMLs,
547 proposal TSVs, old history, narratives, discussion templates and
embedding products. Existing pages changed only in their count footer,
except phenotype's added child; its priority child count rose from 162
to 163. The protected record is unchanged. Parsed ROBOT graphs contain
15, 12,628 and 12,632 triples with the expected w3id.org hierarchy.
Neither configured embedding source path exists, so no rebuild is claimed.
The ordinary whitespace check flagged only the required three trailing
empty TSV cells; exact-path-scoped checks passed.

Hartig subsequently landed as `f9bd6b23517bc85f27af8dfdaae7d1d14a0e0454`.
The receipts above apply to the independent checkpoint, not a future
combined tree. Incorporate actual main and pending dependencies, regenerate
all affected products and validate the combined corpus before publishing;
keep any dependency draft out of the queue until its predecessors land.
Repository history is scaffolded and append-only. Regenerate the citation
audit separately from discussion, QC, page and priority products. Preserve
actual resolver outcomes rather than relabeling manual source checks.

Before merging, require LinkML/strict, full tests and QC, proposal/ROBOT/RDF,
online taxonomy, snippet, history/product, preservation and desktop/mobile
checks, exact-head CI, adversarial review and clean late feedback. Use the
native merge queue, inspect its combined candidate, confirm actual MERGED
state and reconstruct the landed tree before deleting the branch.

## Upstream Round Trip

After TraitMech review, submit the one-class template and open hierarchy
question to METPO or the kg-microbe proposal pipeline. The placeholder is
not a released METPO ID. On acceptance, refresh the pinned ontology, seed
a temporary tree, confirm accepted scope and migrate references while
preserving the local ID as provenance, not as a lexical synonym. Append
history, regenerate products and rerun validation.

## Change Log

- v546, 2026-10-07: one internal mycorrhizal vesicle-formation phenotype,
  explicitly including thalli and separating morphology from mechanisms.
