# Functional Cellular Rejuvenation (v586)

## Context And Scope

Propose an ontology home for `traitmech:000710`,
`data/traits/physiology/cellular_rejuvenation.yaml`. It remains `PROPOSED`,
pending human scientific sign-off. This is a reusable physiological outcome,
not an intervention, gene, marker, lifespan value or individual observation.

| Scope | Records | Parent | Leaves |
| --- | ---: | --- | ---: |
| A: accepted local trait | 1 | `METPO:1000059` phenotype | 1 |
| B: causal predicates | 0 | Not applicable | 0 |
| C: schema vocabulary | 0 | Not applicable | 0 |

No exact synonym, external equivalence, canonical taxon, protein-resolved
graph or negative companion is asserted. Property and SSSOM files are omitted.

## Evidence And Boundaries

[Haga and Karino 1986](https://doi.org/10.1242/jcs.86.1.263)
(PMID:3654779) supplies the definition's same-cell functional-restoration
anchor. Its directly read scientific abstract reports restored sexual activity
after young cytoplasm was injected into senescent Paramecium. Other tested
functions did not improve. Full methods and figures were unavailable.

[Proenca et al. 2018](https://doi.org/10.1038/s41467-018-06154-9)
(PMID:30213942, PMC6137065) supplies bacterial descendant-lineage recovery.
Primary XML Results Sec6 and actual Figure 4d show new-daughter lineages from
the old-cell equilibrium converging toward faster growth. Doubling times are
derived from elongation, not direct interdivision intervals. This is not repair
of the same old mother, and the damage-partition model is not direct chemical
damage measurement. Some Discussion panel pointers are inconsistent with the
actual Figure 4; use the Results and inspected figure for the locator.

[Unal et al. 2011](https://doi.org/10.1126/science.1204349)
(PMID:21700873, PMC3923466) supplies gamete replicative-potential reset, distinct
from its vegetative NDT80 lifespan-extension result. The scientific abstract,
author-manuscript main text and Figures 1 and 4 were assessed. Supplements and
strain tables were not. The [MIT item](https://hdl.handle.net/1721.1/96160)
identifies the manuscript, but returned PDF bytes differ from bitstream
metadata size/checksum. The added cover is not an established explanation;
original deposited-byte identity remains unresolved.

Following adversarial issue #1893, the record explicitly attributes gamete
reset to Figure 1 and the separate vegetative-extension experiment to Figure 4.
The source-verification sidecar retains its original snapshot interpretation
with an explicit `assessment_corrections` successor; the original curation
event is preserved.

[Haga 2023](https://doi.org/10.3390/microorganisms11010082)
(PMID:36677375, PMC9865852) also uses sexual rejuvenation for mature-cell
return to immaturity. That Results 3.1 usage is outside the defined functional
phenotype; Results 3.2 reports recovery of old-cell mating activity. Figure 6C
measures four-day cell counts, not direct division times, without a young-cell
growth comparator. Engineered treatment is not a natural canonical example.

[Cesar et al. 2022](https://doi.org/10.1016/j.isci.2022.103765)
(PMID:35243217, PMC8858994) is boundary evidence: stationary-phase culture age
is not individual division age, and immediate regrowth can reflect preserved
function rather than reversal of a demonstrated deficit. Nongrowth within the
observation window does not prove irreversible death. Primary abstract,
selected Results, Discussion, limitations and classification methods were
read; actual figures and raw data were not independently assessed.

Each record snippet is a short contiguous primary-source quotation, not a
paraphrase. Source locators, identity checks, hashes and read-scope limits are
retained in `research/traits/physiology/cellular_rejuvenation-source-verification.json`.
MED/Crossref notice fields were checked; incomplete publisher access prevents
an exhaustive notice-absence claim. Reanalysis and model papers are not counted
as new independent experiments.

The label's **functional** qualifier is necessary: marker-only changes,
lifespan extension alone, prevention without prior loss, dormancy exit and
sexual immaturity alone do not establish this trait. Recovery can be partial
and transient. Retain the same-cell versus descendant unit, age axis, measured
endpoint, conditions, intervention and comparator. No common mechanism or
universal microbial recovery is claimed.

## Hierarchy Decisions

Use active `METPO:1000059` phenotype, under `METPO:1000188` quality. Pinned
and current released RDF resolve the parent to
`https://w3id.org/metpo/1000059`, not a legacy OBO-namespace stub.
Autogamy, gametogenesis, endospore formation, dormancy and replicative aging
are not exact equivalents or demonstrated narrower parents. No existing
record is reparented. No same-scope unresolved node was found in the inspected
corpus; protected spore-germination content remains unchanged.

## Novelty And Reservation

The 2026-10-12 baseline was main
`d5ade193d52ce90dfd8cd46adb6b28aa0871eb06`, with 1,104 live records.
Ignored and hidden files were included across 22 registered TraitMech roots.
Four had usable Git metadata; 18 registered historical tracked trees were
also checked. Unavailable current ignored/untracked bytes cannot be recovered.
The searches do not traverse symlink directories, unpack archives or inspect
binary internals. No unregistered-workspace or discovery-exhaustion claim follows.

The expanded vocabulary and citation search found no exact trait among 1,106
distinct available YAML versions. The existing aging source verification
mentions rejuvenation only as a boundary. Related autogamy, dormancy, aging,
stress-response and sporulation records were semantically inspected. The
1,546-row release delta and 153-row active review remain frozen decisions;
a fresh 399-ID seed projection overlaps 344 live IDs and leaves 55 absent
leads, none an exact candidate. Pinned and current released METPO RDF had
12,617 and 12,649 triples respectively; neither exposed an exact term. Sparse
editable metadata alone was not used to establish absence.

Stable, paginated pending changes covered TraitMech #1782, #1476, #973 and
draft #924 (692 files over seven pages), CommunityMech draft #935, and METPO
#644, #643, #641, #640, #638 and #629. Complete changed ontology/template
blobs were read, not just patches. METPO discovery also checked 644 issue/PR
bodies and 654 comments. Immutable upstream snapshot bytes were reverified
against Git blob hashes and SHA-256 at fresh matching heads:

- METPO: `1efc8c73009200b9cb74d125df6a0ea5dc36cb93`.
- CommunityMech: `80049bcc9195480a58633236169b62f86c23489a`.
- KG-Microbe: `bac582f4e131a7ba96b585996ae1fa759403f0b6` (`master`).

Reservation checks covered 585 TraitMech cohorts, 6,296 interval occurrences
and proposals from 127 registered CommunityMech roots plus available historical
trees. A first local query failed on unsupported regex syntax and a first remote
attempt failed on an API connection. Neither failure was absence evidence;
fresh corrected checks passed before allocation. Recheck main and pending
reservations before publication; this does not eliminate allocation races.

## ID Space And Subset

- Local identifier: `traitmech:000710`.
- Cohort: `metpo_traitmech_v586`.
- Reserved full block: `METPO:1066300`-`METPO:1066399`.
- Only populated placeholder: `METPO:1066300`, not a released METPO ID.
- Subset: `metpo_traitmech_2026_10`.
- No previous block is reused; inspected CommunityMech reservations are separate.

## Files And Verification

| File | Content |
| --- | --- |
| `metpo_proposal_classes_robot.tsv` | Canonical two headers and one class row, 11 columns |
| `proposal.md` | Scope, sources, hierarchy, allocation and migration rationale |

The guarded `scripts/add_cellular_rejuvenation_trait.py` defaults to a
validated dry run and rejects parent, target or template drift. Definition
source citations express provenance, not ontology equivalence. Required gates:

```bash
just verify-proposal metpo_traitmech_v586
just robot-validate-proposal metpo_traitmech_v586
just qc
just validate-history
just validate-products
```

Actual outcomes belong in the saved structured review and PR. Inspect emitted
RDF as well as ROBOT exits. Preserve required trailing header cells, applying
only a scoped whitespace exception to this inspected TSV.

## Upstream Path And Round Trip

After local review, submit the template and rationale to `berkeleybop/metpo`
or the KG-Microbe proposal pipeline. Curator `codex`, the LLM-assisted event
and append-only history record authorship. Upstream maintainers choose the
final label, hierarchy and identifier. Following an explicitly reviewed ontology
update containing the accepted term, re-seed and migrate references while
retaining `traitmech:000710` as a traceable alias and preserving history.
Do not silently refresh the ontology or present the placeholder as released.

## Change Log

- v586, 2026-10-12: propose functional cellular rejuvenation with five primary
  DOI references, checked snippets and explicit functional-unit boundaries.
