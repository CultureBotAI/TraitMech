# METPO proposal v571: lethal algicidal activity

## Context and scope

Lift `traitmech:000695` as `METPO:1064800`: one reusable PHYSIOLOGY
CLASS, kept PROPOSED pending human signoff. TraitMech's fallback policy
requires this same-branch upstream proposal rather than an uncited local ID.

| Scope | Parent | Classes | Properties |
| --- | --- | ---: | ---: |
| A: local phenotype | phenotype `METPO:1000059` | 1 | 0 |
| B/C: predicates/schema | Not included | 0 | 0 |

The record concerns a microbial killing capability, not an algicide molecule,
gene, treated organism's susceptibility or source-specific assay column.

## Hierarchy and boundaries

Use phenotype `METPO:1000059`, below quality `METPO:1000188`, in the
record and standalone TSV. Predatory bacterium `traitmech:000054` requires
killing and consuming bacteria for nutrition and is not a broader class of
this capability. No consumption requirement or organism-level disjointness
is inferred. Grazing and algicidal killing can overlap without being synonyms.
No exact unresolved mention in an existing record needs repair.

The explicit **lethal** qualifier distinguishes the curated endpoint from
broader algicidal usage. Paul and Pohnert 2011
([DOI:10.1371/journal.pone.0021032](https://doi.org/10.1371/journal.pone.0021032)),
Methods "Monitoring algicidal activity" and Results, use fluorescence-based
growth inhibition as an algicidal readout. This terminology context is not
counted as a fourth killing study. Reduced fluorescence, growth arrest,
reversible ecdysis, passive removal and a protease sequence alone do not
establish this record's lethal endpoint. Target scope explicitly includes
cyanobacteria without classifying them as eukaryotic algae. Activity against
all algae is not required; no host-range or concentration threshold is imposed.

## Evidence and limits

- [Lovejoy et al. 1998](https://doi.org/10.1128/AEM.64.8.2806-2813.1998),
  PMID:9687434, PMC106776: strain Y and filtrate support lethal activity.
  The contiguous Results sec9 quote is directly checked against full text.
- [Lee et al. 2000](https://doi.org/10.1128/AEM.66.10.4334-4339.2000),
  PMID:11010878, PMC92304: definition authority distinguishing killing from
  algistatic action. The quotation is in the scientific Abstract.
- [Zhang et al. 2023](https://doi.org/10.3390/toxins15030220),
  PMID:36977111, PMC10058357: Results 2.4 and actual Figure 3 support
  cyanobacterial damage/lysis. The contiguous quote is from that subsection.

Record notes retain control, endpoint and strain-identity limits, actual
reading/figure coverage, and qualified `EXT_ID:<PMID> AND SRC:MED`
bibliographic checks on 2026-10-11. These are different study groups and
systems, not direct replications of a single strain. Direct quotations,
metadata verification and native abstract-resolver verdicts are distinct checks.

Canonical taxa, taxon-paired protein mechanisms and external mappings remain
OPEN. No graph, exact synonym, xref or SSSOM mapping is asserted. Mechanisms
are deferred, not claimed absent; the record does not establish environmental
safety or field bloom-control efficacy.

## ID space, subset and novelty

Reserve local `traitmech:000695`, cohort v571 and the complete
`METPO:1064800-1064899` block; populate only 1064800. Subset:
`metpo_traitmech_2026_10`. Allocation main:
`2dab429bf6f8d0d6764394acde4fec66a0d28f29`.

Whole-repository searches across all 22 pre-existing worktrees included
ignored and hidden files, algicidal/algistatic/algaecidal variants, killing,
lysis, cyanobacterial terminology, source identities, local ID, cohort and
the full proposed block. No candidate or reservation hit was found.
An equally inclusive CommunityMech reservation search found no conflict;
this block is outside CommunityMech v1 `1007100-1007220` and its extensions.

Fresh seeding produced 399 records; 55 exact IDs absent from the 1,089 live
records remain 38 supporting properties and 17 prior-review duplicates.
The complete 1,546-row release inventory, 153-row active-review table and
active policy were inspected as frozen snapshots, not a live missing-work
queue. The 12,617-triple pinned ontology yielded no matching candidate term.
This bounded search is not global discovery exhaustion.

All open PRs, including drafts, were inspected through complete paginated
file lists with unchanged immutable heads on 2026-10-11:

| PR | Head | Reservation |
| --- | --- | --- |
| #1782 | `35099af2b7d5347f2ca6e418c4a139979071644d` | No curation paths |
| #1476 | `b4b8d1280e25bd3e340241e7ac23b51bbe7aaec3` | No curation paths |
| #973 | `331f9517bbdf4d2c9fa97b338ee59a8986f2f174` | No curation paths |
| #924 (draft) | `e61ce120b8da953da097b9f94bfed7f292e5675a` | No curation paths |

Recheck immediately before publication. All unowned work and protected
spore germination remain excluded from modification.

## Files and verification

| File | Content |
| --- | --- |
| `metpo_proposal_classes_robot.tsv` | Two headers and one class; 11 columns |
| `proposal.md` | Scope, evidence, allocation and round trip |
| Properties/SSSOM | Not emitted: no predicate or justified equivalence |

Canonical headers were checked at upstream commit
`1408e7099d039026d7611c240938d8e177753406`, class/property blobs
`b590cf303dc2fbdd57bed021668641cd0c32396d` and
`b2f9f4ceb6b6893a8b27d7fe41e859f08c4b2990`. The three empty trailing
directive cells are required. CommunityMech's legacy 12-column property
table is not the canonical 13-column header. METPO IRIs must use w3id.

The writer prevalidates, guards parent scope and target/proposal drift,
defaults to dry run and permits exact replay. Required checks are native
LinkML/strict/history, proposal/ROBOT/ELK, QC/products, source/snippets,
focused/full tests, preservation and desktop/mobile rendered-page checks.
The PR and immutable review record actual outcomes; none is assumed here.

## Upstream and round trip

After human signoff, submit the class TSV to berkeleybop/metpo. No upstream
issue or acceptance is claimed. After official minting, refresh the pinned
ontology, migrate the identifier and its references, preserve the old
`traitmech:000695` identifier as a provenance synonym, retain append-only
history, and avoid a duplicate primary record.

## Change log

- v571, 2026-10-11: propose lethal algicidal activity.
