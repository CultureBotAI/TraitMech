# METPO proposal v555: fungal adhesive-knob trap formation

## Context and scope

Lift `traitmech:000679` as `METPO:1063200`: one morphological phenotype,
kept `PROPOSED` pending human review. Scope A: one class. Scope B: zero
predicates. Scope C: zero schema enums.

Parent: phenotype `METPO:1000059`, below quality `METPO:1000188`.
The distinctive structure is a unicellular adhesive knob at a hyphal apex,
not a multicellular net, column, nonconstricting ring, mechanically
constricting ring, auxiliary cell or appressorium. Existing mycelial growth
is explicitly bacterial; hyphal anastomosis denotes fusion, not a trap.
Neither detachment, a specific stalk length nor prey induction defines
this class. Morphogenesis does not establish capture in every condition.
No exact synonym, xref, SSSOM equivalence or organism-level disjointness is
asserted. The closer morphology parent remains an open curation question.

## Evidence and limits

- [Andersson et al. 2013](https://doi.org/10.1128/AEM.01390-13): directly
  read publisher HTML, scientific Abstract, Introduction, Culture Methods,
  relevant Results/Discussion and Conclusion, and actual Figure 1. The
  contiguous snippet is from the scientific Abstract. CBS 200.50 forms
  knobs in aerated liquid culture; the image shows attached residual and
  filtered isolated knobs, not time-resolved capture. Sequence domains and
  expression changes do not establish causal protein functions. Supplements
  were not used to assign mechanisms. PMC/XML access failures do not imply
  that the source lacks the observation.
- [Liu, Liu and Zhuang 2005](https://doi.org/10.1016/j.femsle.2005.02.027):
  primary publisher scientific Abstract directly retrieved through its
  minimal-article redirect. Full Methods and figures were not retrieved.
  Independent ascosporic culture from rotten Quercus wood is reported to
  capture nematodes with adhesive stalked knobs, with frequent formation
  on nutritional agar without challenging nematodes. The abstract snippet
  supports that bounded observation, not universal induction conditions.
  The source's anamorph naming is not a verified current equivalence.

Canonical example: `NCBITaxon:1284197`, live exact strain label
**Dactylellina haptotyla CBS 200.50**. The NCBI taxonomy XML also lists the
historical Monacrosporium haptotylum strain name used in the 2013 study.
[Zhou et al. 2018](https://doi.org/10.1080/23802359.2018.1507650), directly
read primary XML, body paragraph 2, reports a decaying-leaf pond collection
at Chelsea Physic Garden, London, in 1948 by M.P. Peach. This genome study
provides provenance, not a third independent phenotype experiment. The
example does not imply all strains or field biocontrol efficacy.

Formation, adhesion, capture, penetration and digestion are separate
endpoints. No protein graph is asserted: perturbation/complementation,
relevant remaining figures/supplements and taxon-paired accession review
are required. Mechanism is deferred, not claimed absent.

## Allocation and novelty

Reserve **traitmech:000679**, cohort **v555**, and the whole
**METPO:1063200-1063299** block; only 1063200 is populated. This follows
v554's 1063100-1063199 block without overlap with CommunityMech v1.
Subset: `metpo_traitmech_2026_10`.

Allocation main: `efdd23e9e99ea200321a39a2ec12eaa583b73e15`.
Ignored-and-hidden searches covered all 20 then-existing TraitMech
worktrees, the entire CommunityMech checkout and a complete fresh open-PR
curation snapshot: 22 roots. Queries included knob, haptotyl, querci,
Dactylellina, source DOI/PMID/PMC identifiers, strain identifiers, local
ID, cohort and the full hundred block. Inspected matches were scope
exclusions, unrelated auxiliary-cell swellings, cached surname/clinical
surface mentions, dependency lexical coincidences and numeric values,
not an exact record or reservation. Parsed pinned METPO has no exact
class. A fresh 399-record seed contains 55 IDs absent from the 1,073-record
corpus, none an adhesive-knob term; it is not a curation queue or evidence
of exhausted discovery.

Complete paginated open-head inventory, including drafts, at allocation:

| PR | Head | Reservation |
| --- | --- | --- |
| #1802 | `a74d9278b3ce5971d773a4e81616373f795f2816` | existing Shedu; no new ID/block |
| #1782 | `35099af2b7d5347f2ca6e418c4a139979071644d` | none in changed curation paths |
| #1476 | `a138e46f803b5af9d48969217b86cf7c9a3b61bd` | none in changed curation paths |
| #973 | `331f9517bbdf4d2c9fa97b338ee59a8986f2f174` | none in changed curation paths |
| #924 (draft) | `e61ce120b8da953da097b9f94bfed7f292e5675a` | none in changed curation paths |

File counts, selected immutable curation blobs and head stability checked.
Recheck main and reservations before publication.

## Artifacts and verification

One class TSV has two 11-column headers and one class row. No property or
SSSOM file is needed. Preserve three empty trailing ROBOT directive cells.
Upstream skill and templates at `1408e7099d039026d7611c240938d8e177753406`
were read and revalidated against immutable GitHub blobs: class
`b590cf303dc2fbdd57bed021668641cd0c32396d`, property
`b2f9f4ceb6b6893a8b27d7fe41e859f08c4b2990` (11/13 columns).
CommunityMech v1's three worked-example files were read end to end.
Use maintained w3id METPO expansion, not the upstream legacy OBO example.

Required checks: proposal verifier, ROBOT/ELK and parsed OWL identities,
LinkML/strict/history/QC/products, snippet resolver and direct-source
checks, live NCBI, focused/full tests and desktop/mobile browser QA.
Actual outcomes belong in the PR receipt. The add-trait skill already
covers scope, provenance, source access and sequence-feature uncertainty;
no instruction change is required for this record.

## Upstream and round trip

After human signoff submit the TSV to berkeleybop/metpo. No upstream
issue or accepted term is claimed. After release, refresh the pinned
ontology, seed the accepted term and migrate the local identifier while
retaining provenance. Do not emit the reserved ID as a released term.

## Change log

- v555, 2026-10-08: initial proposal.
