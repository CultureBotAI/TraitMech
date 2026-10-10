# METPO proposal v565: coccolith production

## Context and scope

Lift `traitmech:000689` as `METPO:1064200`: one physiological phenotype
in one new record, kept `PROPOSED` pending human review. Scope A: one class.
Scope B: zero predicates. Scope C: zero schema enums. The record denotes
an assayable cellular production phenotype, not a coccolith material entity,
a gene, a sequence annotation or a precomposed chemical-use relation.

## Hierarchy decisions

Parent: phenotype `METPO:1000059`, below quality `METPO:1000188`.
A broader biomineralization phenotype remains unresolved. Production differs
from possession, secretion and arrangement of preformed elements. Malformed
coccoliths still count; a complete coccosphere is not required. Generic
calcification, urease-associated precipitation, siliceous scale production
and magnetosome/ferrosome possession are not equivalent. No universal
silicon requirement, ploidy restriction, fitness effect, photosynthetic benefit,
growth dependence or molecular mechanism is asserted. No exact synonyms,
xrefs, SSSOM equivalences or organism-level disjointness are proposed.

## Evidence and limits

- [Sviben et al. 2016](https://doi.org/10.1038/ncomms11228),
  PMID:27075521, PMC4834641: calcium-resupply experiments and ultrastructure
  support production in historical E. huxleyi AWI1516. The separate
  calcium-rich compartment is not established as a necessary direct precursor.
- [Walker et al. 2018](https://doi.org/10.1111/nph.15272),
  PMID:29916209, PMC6175242: time-lapse observations in Ge-treated
  C. braarudii PLY182g distinguish ongoing production from covering integrity.
  Species-specific growth effects are not generalized.

Both primary articles' scientific text was directly read in official Europe
PMC XML. Actual Sviben Figures 1/3 and Walker Figures 5/8 were inspected;
other images, supplements and movies were not visually inspected. The first
snippet is scientific-abstract text; the second is Results text, not an
abstract quote. Keep automated resolver outcomes separate from direct checks.
The record retains the Sviben detector-panel caption inconsistency and
Walker's conflicting stage temperature, HEDP concentration and low-Si
threshold descriptions; no quantitative claim silently chooses one version.

Canonical examples await joint strain-provenance and current-taxonomy
verification. [Skeffington et al.](https://doi.org/10.1111/jpy.12942),
full paper, p. 239, identifies AWI1516 as derived from CCMP1516. Print year
2020 and online dates in 2019 are one paper, not separate evidence. The
[current CCMP1516 catalog](https://ncma.bigelow.org/CCMP1516), directly read
2026-10-10, reports lost coccolith production under Gephyrocapsa huxleyi.
Neither current catalog state nor historical experiment overwrites the other.
The catalog is provenance context, not independent production evidence.
PLY182g provenance is unresolved here. Molecular graphs need functional
evidence, taxon-paired accessions and separate deposition/transport/secretion
claims; neither sequence features nor perturbation correlations supply them.

## Allocation and novelty

Reserve **traitmech:000689**, cohort **v565**, and the full
**METPO:1064200-1064299** block; only 1064200 is populated.
Subset: `metpo_traitmech_2026_10`. Allocation main:
`a1f1996f8e6f20d0c9677d13b0e0cd0aa2f20a54`.

Ignored-and-hidden searches covered all 22 pre-existing TraitMech worktrees,
including ontology, records, graph nodes, synonyms, discussions, research,
history, proposals and generated files. Search terms included coccolith,
coccosphere, calcification, calcifying, biomineralization spelling variants,
calcite production/precipitation, all three cited DOIs, the additional
research lead DOI:10.1111/nph.17230, local ID, cohort and whole METPO block.
There was no exact record or reservation. Hits concern phagocytosis and
decalcification, urease-associated precipitation, other mineral structures
and the broader biomineralization TODO, not this exact production phenotype.
No exact unresolved node, misplaced synonym or same-scope TODO needs an
existing-record edit. The broad parent TODO remains valid and unresolved.

The full block was also searched across CommunityMech, including ignored
and hidden files. Its only numeric match was an unrelated package byte size
in `uv.lock`, not an ID reservation; no CommunityMech v1 overlap exists.
The pinned METPO contains 12,617 RDF triples and no matching candidate
literal. Fresh seeding emitted 399 records, with 55 exact IDs absent from
the 1,083-record live corpus. The full release-delta and active-review tables
and their policy were consulted; absent seed IDs remain leads, not novelty
or exhaustion proof. This candidate was independently source-backed.

All open PRs, including drafts, were inspected through paginated changed-file
lists and immutable curation blobs on 2026-10-10:

| PR | Head | Reservation |
| --- | --- | --- |
| #1802 | `a74d9278b3ce5971d773a4e81616373f795f2816` | existing Shedu 000220; no new ID/block |
| #1782 | `35099af2b7d5347f2ca6e418c4a139979071644d` | no changed curation paths |
| #1476 | `b4b8d1280e25bd3e340241e7ac23b51bbe7aaec3` | no changed curation paths |
| #973 | `331f9517bbdf4d2c9fa97b338ee59a8986f2f174` | no changed curation paths |
| #924 (draft) | `e61ce120b8da953da097b9f94bfed7f292e5675a` | no changed curation paths |

Recheck main and reservations immediately before publication. Existing trait
YAMLs, including protected spore germination, must remain byte-identical.

## Artifacts and verification

One class TSV: two 11-column headers and one class row. No property or SSSOM
file. Preserve the three empty trailing directive cells. Upstream contract
and templates were rechecked at `1408e7099d039026d7611c240938d8e177753406`:
skill `680062049932730096a96dfb1cca1b69ddf2cb92`, class template
`b590cf303dc2fbdd57bed021668641cd0c32396d`, property template
`b2f9f4ceb6b6893a8b27d7fe41e859f08c4b2990` (11/13 columns).
CommunityMech v1 supplies the worked convention. Use the maintained w3id
METPO expansion, not the upstream legacy OBO example.

```sh
PYTHONPATH=src .venv/bin/python scripts/verify_metpo_proposal.py proposals/metpo_traitmech_v565
PYTHONPATH=src .venv/bin/python scripts/robot_validate_proposal.py proposals/metpo_traitmech_v565
```

Parse emitted RDF to check 1064200 -> labeled 1000059 -> 1000188 under
`https://w3id.org/metpo/`. The writer guards parent identity and scope,
defaults to dry run and refuses conflicting target/proposal preimages.
Require strict/LinkML/history/QC/products, source/snippet checks, focused/full
tests, retained adversarial review and desktop/mobile page inspection.
Actual results belong in the PR and review, not a pre-execution pass claim.

## Upstream and round trip

After human signoff submit the TSV to berkeleybop/metpo. No upstream issue
or accepted term is claimed. Following release, refresh the pinned ontology,
seed the accepted term and migrate the local identifier while preserving
provenance. The placeholder is not a released METPO identifier.

## Change log

- v565, 2026-10-10: initial source-bounded coccolith-production proposal.
