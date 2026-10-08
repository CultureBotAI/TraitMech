# Fungal Auxiliary Cell Formation: METPO Proposal v547

## Scope and Hierarchy

Propose `traitmech:000671 fungal auxiliary cell formation`, a PROPOSED
MORPHOLOGY class, from main `fcb766bf5876204e0c7b6308939322ca492480bc`.
Scope A contains one organismal phenotype; Scopes B and C are empty.
This is neither a structure record nor a sequence-profile assignment.

Use active `METPO:1000059 phenotype`, below `METPO:1000188 quality`.
The pinned ontology has 12,617 parsed triples and no exact matching class.
`METPO:1000198 mycorrhization` is obsolete, not a usable active parent.
A closer morphological parent remains an OPEN discussion.

The definition concerns auxiliary hyphal swellings outside plant tissue.
Clustering is typical rather than a minimum count for each observation;
ornamentation, storage and propagule function are not compulsory criteria.
Arbuscular mycorrhizal names the fungal context, not current host contact.
Internal vesicle formation (`000670`), arbuscule formation (`000664`), BAS
formation (`000665`) and chlamydospore formation (`000658`) are not exact
substitutes. Existing records and their histories remain unchanged.
Structure labels such as external vesicles are not silently converted to
exact organismal synonyms. No xrefs, SSSOM equivalences, new predicates,
universal disjointness or unsupported protein graph is asserted.

## Evidence and Example

- [Brundrett terminology](https://www.mycorrhizas.info/vam.html), version 2
  (2008), C.1 and F: directly read external-swellings terminology. The
  unnamed Scutellospora micrograph and separate line illustration were
  viewed, not treated as independent primary experiments or named strains.
- [Kuga et al. 2008](https://doi.org/10.1111/j.1469-8137.2007.02345.x),
  PMID:18194149: directly read Results supports formation on germ tubes.
  Methods and captions were read; actual paper figures/supplements were
  not inspected. Preserve the HTML temperature-glyph uncertainty and
  distinguish formation from subcellular localization and function.
- [Declerck et al. 2004](https://doi.org/10.1017/S0953756203008761),
  PMID:15035509: directly retrieved scientific abstract supports a separate
  root-organ-culture observation and conditional regrowth/colonization
  distinction. Full paper, images and isolate provenance are unread.

All three entries carry concise contiguous snippets. Run the maintained
resolver and retain its actual outcomes separately from manual body/URL
checks; a body quote need not occur in the scientific abstract.

The canonical example is `NCBITaxon:4874 Gigaspora margarita`, MAFF520054
(designation C), qualified to the primary germ-tube observation. Direct
[NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=4874)
and [NARO provenance](https://www.gene.affrc.go.jp/databases-micro_search_detail_en.php?maff=520054)
checks are name and collection evidence, not independent phenotype assays
or culture reidentification. Collection fields remain separate from quotes.
[Ohtomo 2025](https://doi.org/10.1264/jsme2.ME25040), Table 1, retains C/520054
and reports primer-specific ASVs; these are not independent culture counts
or auxiliary-cell observations. Its figures/supplements were not inspected.

The 1986 DAOM194757 material and its later reidentification, 2003 development
paper, and 2026 count-unit study remain separately documented research
leads, not additional accepted evidence or substitutes for MAFF520054.
No claim is made that this bundle exhausts auxiliary-cell research.

## Novelty and Allocation

The pre-branch search included ignored and hidden files across all 13
current worktrees, CommunityMech and a complete immutable open-PR snapshot
(15 roots). Auxiliary-cell/body, accessory-cell/body/vesicle, external-vesicle
aliases, likely slugs, misspellings and primary DOI/PMID variants produced
20 lines in six relative paths. These were the internal-vesicle record's
explicit scope exclusions and its supporting/derived artifacts, not an
existing auxiliary-cell TraitRecord. Neighbor definitions, histories and
the METPO release-delta/active-review artifacts were also checked.

Reserve local `000671`, cohort v547 and the entire `1062400-1062499` block,
using row `METPO:1062400` and subset `metpo_traitmech_2026_10`.
The separate whole-root allocation scan found 51 incidental numeric lines
in 16 relative files (dependency test data, scientific numeric tables,
accession substrings and genome coordinates), not a competing reservation.
The local maximum alone was not used as proof of availability.

Complete pending-head inventory, including drafts:

| PR | Immutable head | Changed files | Curation artifacts |
| --- | --- | ---: | ---: |
| 1782 | 35099af2b7d5347f2ca6e418c4a139979071644d | 1 | 0 |
| 1476 | a138e46f803b5af9d48969217b86cf7c9a3b61bd | 8 | 0 |
| 973 | 331f9517bbdf4d2c9fa97b338ee59a8986f2f174 | 3 | 0 |
| 924 (draft) | e61ce120b8da953da097b9f94bfed7f292e5675a | 692 | 0 |

Changed-file lists were fully paginated and checked against reported totals;
the final head set was rechecked. No pending curation reservation appeared.
CommunityMech v1/extension blocks are separate. Recheck remote main, all
worktrees and complete pending heads immediately before publication.

The publication refresh retained the four heads above and added PR 1800,
head `bd4f996dd63681ad067117aa37c157dd5860c789`, with one changed file and
no curation artifacts. All five lists were fully paginated and the final
head set rechecked. Remote main remained the base above. An additional
ignored-and-hidden search for extramatrical/extraradical-vesicle aliases
across 15 worktrees, CommunityMech and the snapshot returned no matches.

## Template and Validation

The upstream contract is pinned to kg-microbe
`1408e7099d039026d7611c240938d8e177753406`. Rechecked class-template blob
`b590cf303dc2fbdd57bed021668641cd0c32396d` has 11 columns; property-template
blob `b2f9f4ceb6b6893a8b27d7fe41e859f08c4b2990` has 13. Emit only the
single-row class template and this narrative, preserving the directive
row's three trailing empty cells. The METPO IRI must expand to
`https://w3id.org/metpo/`, not a legacy OBO stub.

The dry-run-first writer guards the reviewed parent projection and exact
target/template replay, prevalidates, uses `write_validated_trait` and
records an LLM-assisted curation event. All 20 focused writer tests passed
in 5.71 seconds; dry run and apply passed. Controlled fixture tests cover
parent/target/template drift, replay and validation failure before writes.
Repository history is scaffolded with the actual Codex actor and append-only.

Broader validation is pending at this initial narrative checkpoint, not
claimed passed. Require LinkML/strict, proposal/ROBOT and parsed RDF,
snippet and online taxonomy checks, complete tests, committed QC,
history/products, preservation and desktop/mobile rendered-page checks.
Regenerate the citation audit separately from discussion, QC-dashboard,
page and priority products. Check only the configured embedding source
paths before deciding whether to rebuild embeddings.

After validation, publish a trait-scoped PR, request review and perform an
adversarial source/scope/diff review. File and fix actual defects; independent
reviewer availability is separate from approval. Require all eight exact-head
gates, clean late feedback, native-queue membership and combined-candidate
checks, actual MERGED state and actual-parent tree reconstruction before
deleting either feature branch. Final validation receipts belong on the PR.

## Upstream Round Trip

Submit the reviewed single-class template and closer-parent question to
METPO or kg-microbe's proposal pipeline. The placeholder is not a released
METPO identifier. On acceptance, refresh the pinned ontology, seed a temporary
tree, confirm scope and migrate references, preserving the local identifier
as provenance rather than a lexical synonym. Append history, regenerate
products and repeat validation.

## Change Log

- v547, 2026-10-08: auxiliary-cell formation phenotype, with external
  morphology separated from cellular organelles and functional hypotheses.
