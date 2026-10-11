# METPO proposal v572: bacterial mycophagy

## Context and scope

Lift `traitmech:000696` to placeholder `METPO:1064900`: one reusable
ECOLOGY CLASS, PROPOSED pending human signoff, not an interaction instance,
assay column, gene, protein or chemical-use pair.

| Scope | Parent | Classes | Properties |
| --- | --- | ---: | ---: |
| A: local trophic phenotype | phenotype `METPO:1000059` | 1 | 0 |
| B/C: predicates/schema | Not included | 0 | 0 |

## Hierarchy and boundaries

Use phenotype `METPO:1000059`, below quality `METPO:1000188`.
The definition follows Leveau and Preston's active nutritional criterion,
including their explicit oomycete scope without calling oomycetes true fungi.
Killing and obligate dependence are not required. Mere fungal inhibition,
lysis, passive exudate consumption and digestion of unrelated dead material
do not suffice. Nutritional growth must be supported, not inferred from a
sequence annotation or enzyme activity alone.

Predatory bacterium `traitmech:000054` requires bacterial prey; saprotrophy
`traitmech:000055` concerns dead material; parasitism `traitmech:000043`
requires host harm; phagotrophy `traitmech:000628` requires ingestion.
None is an established broader parent of this source-defined class.
No organism-level disjointness is asserted. Unqualified mycophagy, fungivory
and mycetophagy are broader actor-scope terms, not exact synonyms.
No existing exact mention requires repair; mappings remain open.

## Evidence and limits

- [Leveau and Preston 2008](https://doi.org/10.1111/j.1469-8137.2007.02325.x),
  PMID:18086226: directly read definition authority, not experimental replication.
- [de Boer et al. 2004](https://doi.org/10.1099/ijs.0.02920-0), PMID:15143036:
  natural isolates and hyphal-growth testing; Ter6-qualified canonical example.
- [Hoppener-Ogawa et al. 2009](https://doi.org/10.1038/ismej.2008.97),
  PMID:18923455: microcosm growth and no significant Absidia biomass reduction.

Each evidence item has a short contiguous quotation directly checked against
the author full text. Record notes distinguish inspected sections/figures,
qualified bibliographic resolution, abstract matching, experimental inference,
and unread material. The two primary studies have overlapping authors, not
independent-group replication. No isotope-traced transfer is asserted.
The 2009 Methods/caption sampling-time discrepancy remains explicit.

NCBI independently resolves `NCBITaxon:158899` as Collimonas fungivorans,
with Ter6 type material. The primary species description supplies natural
provenance and phenotype, not an assertion about all species members.
The sclerotia assay in DOI:10.1093/ismejo/wrag201, PMID:42523014,
PMC13615538 remains a qualified discussion lead from CommunityMech:000364,
not a fourth counted source or unverified taxon example. Mechanistic graphs
and protein examples are deferred, not claimed absent.

## ID space, subset and novelty

Reserve `traitmech:000696`, cohort v572 and the complete
`METPO:1064900-1064999` block; populate only 1064900. Subset:
`metpo_traitmech_2026_10`. Allocation base:
`7ce464b0a4a9012527aefb16f80577a36462d8d7`.

Searches included ignored and hidden files across all 22 pre-existing
TraitMech worktrees: labels, mycophagy/mycetophagy/fungivory/mycolysis,
Collimonas, living-fungal feeding, citations, local ID, cohort and whole block.
No matching candidate or reservation was found. CommunityMech's related
assay record is not an organism-level TraitRecord; its reservation search
had no conflict. The block is outside CommunityMech v1 and its extensions.

The pinned ontology has 12,617 triples and no matching term. Temporary
seeding yielded 399 records and 55 exact IDs absent from 1,090 live records;
absence alone does not establish novelty. The release-delta and active-review
tables and their policy were inspected, with no matching candidate row.
This search is bounded, not global discovery exhaustion.

Complete paginated file lists for every open PR, including drafts, were
checked; none changes traits, history or proposals. Heads were unchanged
on the expanded pre-write recheck on 2026-10-11:

| PR | Head | Reservation |
| --- | --- | --- |
| #1782 | `35099af2b7d5347f2ca6e418c4a139979071644d` | No curation paths |
| #1476 | `b4b8d1280e25bd3e340241e7ac23b51bbe7aaec3` | No curation paths |
| #973 | `331f9517bbdf4d2c9fa97b338ee59a8986f2f174` | No curation paths |
| #924 (draft) | `e61ce120b8da953da097b9f94bfed7f292e5675a` | No curation paths |

Recheck before publication. Preserve all unowned worktrees and protected
spore germination. No add-trait skill change is required by this curation:
its existing scope, evidence, provenance and sequence-inference rules apply.

## Files and verification

| File | Content |
| --- | --- |
| `metpo_proposal_classes_robot.tsv` | Two headers, one class, 11 columns |
| `proposal.md` | Scope, evidence, allocation and round trip |
| Properties/SSSOM | Not emitted: no predicate or established equivalence |

Pinned upstream headers were checked at
`1408e7099d039026d7611c240938d8e177753406`, blobs
`b590cf303dc2fbdd57bed021668641cd0c32396d` (classes) and
`b2f9f4ceb6b6893a8b27d7fe41e859f08c4b2990` (properties).
Required trailing directive cells must remain intact. METPO IRIs use w3id,
not legacy OBO stubs. The writer prevalidates and guards parent/target/proposal
drift; it defaults to dry run and allows exact replay.

Required checks: native LinkML/strict/history, proposal/ROBOT/ELK, snippets,
live canonical taxonomy, QC/products, focused/full tests, preservation,
rendered pages and immutable scientific review. Actual outcomes belong in
the PR and saved review, not an assumed pass here.

## Upstream and round trip

After human signoff, submit the TSV to berkeleybop/metpo; no upstream issue
or acceptance is claimed. After official minting, refresh the ontology,
migrate the identifier and references, retain `traitmech:000696` as a
provenance synonym, and preserve append-only history without duplicating
the primary record.

## Change log

- v572, 2026-10-11: propose bacterial mycophagy.
