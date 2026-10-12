# Unequal Protein Aggregate Inheritance At Cell Division (v587)

## Context And Scope

Propose an ontology home for `traitmech:000711`,
`data/traits/physiology/unequal_protein_aggregate_inheritance.yaml`.
The first-pass record remains `PROPOSED`, pending human scientific sign-off.
Its definition is a physiological phenotype in which microbial cell division
recurrently yields sibling cells with unequal numbers or amounts of inherited
protein aggregates. It is not a gene, reporter, sequence feature, individual
observation, aggregation process or requirement for active transport.

| Scope | Records | Parent | Leaves |
| --- | ---: | --- | ---: |
| A: accepted local trait | 1 | `METPO:1000059` phenotype | 1 |
| B: causal predicates | 0 | Not applicable | 0 |
| C: schema vocabulary | 0 | Not applicable | 0 |

No exact synonym, external equivalence, canonical taxon, protein mechanism,
graph or negative companion is asserted. Property and SSSOM files are omitted.

## Primary Evidence

[Lindner et al. 2008](https://doi.org/10.1073/pnas.0708931105), PMID:18287048,
PMC2268587, reports position-dependent reporter-focus inheritance and eventual
older-pole accumulation in engineered MGAY (MG1655 IbpA-YFP) at 37 C on LB-agarose without
imposed stress. Primary Results and Methods, actual localization Figure 2 and
lineage schematic Figure 3 were inspected. The schematic is not another
experiment. Pole identities change across divisions. Supplements were not read.
Initial XML/PDF access failures did not persist as a full-text blocker: primary
PMC HTML was subsequently retrieved successfully.
Govers 2018's later reporter comparison identifies IbpA-YFP label-induced
clustering. These older foci are not independent evidence of endogenous
unstressed aggregation; this limitation is retained beside the historical quote.

[Coelho et al. 2014](https://doi.org/10.1371/journal.pbio.1001886), PMID:24936793,
PMC4061010, is the definition anchor. Hsp104-GFP fission-yeast imaging shows
stress-associated unequal inheritance without consistent old/new-pole bias.
Primary XML and actual Figures 3, 4 and S4 were inspected. Figure 3C measures
absolute sibling differences in aggregate-associated fluorescence; S4I measures
count asymmetry. Neither is a concentration measurement. Actual Figure 4B is
fusion and 4C is nucleation, contrary to the caption; a Results pointer to 4C
for stress-dependent asymmetry also conflicts with its plotted endpoint.
Figure 3C describes continuous 40 C, whereas Methods describes 40 C for one hour
then 37 C. This unresolved condition discrepancy is retained, not silently
resolved. Text S1 experimental methods and strain table were text-extracted;
visual layout and model equations were not validated.

[Schramm et al. 2019](https://doi.org/10.1111/mmi.14228), PMID:30779464,
PMC6850343, supports unequal shared inheritance and limits universal exclusive
old-pole retention. Primary Results, Discussion, relevant Methods and actual
Figure 6 were inspected. DnaK-mVenus delta-clpB cells recovered at 30 C after
10 minutes at 40 C. Figure 6G reports roughly 75% versus 25% aggregate allocation
across stalked/swarmer cell types over divisions, not the proportion of unequal
sibling pairs. Figure 6F uses projected cell area, not volume. Sharing and a
stable allocation ratio do not establish equal inheritance. Supplements and
independent strain provenance were not inspected.

[Govers et al. 2018](https://doi.org/10.1371/journal.pbio.2003853), PMID:30153247,
PMC6112618, separates reporter bias (actual Figure 1) from post-heat-shock
inheritance in engineered MG1655 IbpA-msfGFP lineages (actual Figure 3).
Relevant primary Results and Methods were read. The latter assay uses 47 C for
15 minutes followed by microscopy at 37 C; fluorescence concentration and
growth readouts are not substituted for focus inheritance. Supplementary controls
were read where described in Results, not independently inspected as images or
raw data. No universal reporter validity, harm, benefit or natural exemplar is
inferred. This issue #1896 correction preserves the original source assessment
with an explicit successor, rather than rewriting historical provenance.

All four snippets are concise contiguous primary-source spans. Scientific
abstract quotations are distinct from Author Summaries. The two full-text
quotes retain native `NOT_IN_ABSTRACT` verdicts; direct source matches do not
relabel those resolver outcomes. Hashes, locators, source checks and access limits
are retained in
`research/traits/physiology/unequal_protein_aggregate_inheritance-source-verification.json`.
MED/Crossref notice fields and accessible publisher pages were checked, with
bounded access; no exhaustive absence of notices is claimed.

## Interpretation And Hierarchy

Require repeated lineage/population evidence in a stated context, not one
unequal sibling pair. Retain count versus amount, timepoint, reporter, strain
and detection limits. Amount is not concentration and cell area is not volume.
Within-pair inequality, population cell-type bias and complete exclusion are
different endpoints. No universal threshold, fixed pole bias, programmed
asymmetry, toxic damage, aging or rejuvenation is implied. Bare asymmetric
segregation has narrower source usages and is not an exact synonym.

Use active `METPO:1000059` phenotype under `METPO:1000188` quality, expanded
through `https://w3id.org/metpo/`, not a legacy OBO stub. Aggrephagy
(`traitmech:000646`), heat-shock response (`traitmech:000205`), intracellular
inclusion (`traitmech:000066`), replicative aging (`traitmech:000709`) and
functional rejuvenation (`traitmech:000710`) are related but not equivalent.
No existing record is reparented or exact unresolved node left ungrounded in
the inspected scope. Protected spore-germination content is untouched.

Pinned and current released METPO contain lexical hit `METPO:1000011`,
**obsolete aggregate**, deprecated and below ObsoleteClass. Its
`IAO:0000231` value is `OMO:0001000`; no definition, replacement or consider
annotation was available in those releases. Original scope and reason-code
meaning remain unresolved. This is not evidence of equivalence to the
independently literature-defined inheritance phenotype. Do not reactivate the
historical ID or use it as an exact xref.

## Novelty And Reservation

Baseline main: `a57b006b32f2313579650d105d7da245a99a5b95`, 1,105 live records.
Ignored and hidden files were included across 22 registered TraitMech roots,
including 18 retained historical tracked trees without usable Git metadata,
and three known independent clean-main copies. Structured normalization covered
1,120 distinct YAML versions. No exact trait or same-scope unresolved graph node
was identified. Unavailable historical ignored/untracked bytes cannot be
recovered; searches did not traverse symlink directories, unpack archives or
inspect binary internals. This is not universal absence or discovery exhaustion.

A fresh 399-ID seed projection overlapped 344 live IDs, leaving 55 unadjudicated
leads. The 1,546-row release delta and 153-row active review are frozen snapshots,
not current absence decisions. Pinned/current released RDF contained 12,617 and
12,649 triples respectively; sparse editable metadata was not the sole check.

Complete paginated pending changes covered TraitMech #1782, #1476, #973 and
draft #924 (692 files), CommunityMech draft #935, and METPO #644, #643, #641,
#640, #638 and #629. All 15 full changed METPO #629 files were additionally
read, including range documents. Fresh matching upstream snapshot heads were:

- METPO: `1efc8c73009200b9cb74d125df6a0ea5dc36cb93`.
- CommunityMech: `80049bcc9195480a58633236169b62f86c23489a`.
- KG-Microbe: `bac582f4e131a7ba96b585996ae1fa759403f0b6` (`master`).

Allocation checked 586 existing cohorts, 7,143 narrower interval occurrences
and 127 registered CommunityMech roots plus available historical proposals.
The raw scan also found `1000000-1999999` in METPO #629's
`docs/metpo_id_ranges_research.md`, line 14, SHA-256
`07a56007ac0e60e77095ffbf5ea6017f40d80cabcbdc40c7fc0357aa5140ca6c`.
This is the formal ADDITIONAL EDITOR namespace envelope, not a competing
term/cohort reservation. A hash- and context-guarded adjudication retains the
raw hit while all narrower reserved, retired and used ranges remain checked.
Recheck reservations before publication; the audit cannot eliminate races.

## ID Space And Round Trip

- Local identifier: `traitmech:000711`.
- Cohort: `metpo_traitmech_v587`.
- Full reserved block: `METPO:1066400`-`METPO:1066499`.
- Only populated placeholder: `METPO:1066400`, not a released identifier.
- Subset: `metpo_traitmech_2026_10`.

`metpo_proposal_classes_robot.tsv` uses the canonical two headers, three
trailing empty directive cells and one 11-column class row. The guarded writer
defaults to a validated dry run; it refuses target, parent or proposal drift.

```bash
just verify-proposal metpo_traitmech_v587
just robot-validate-proposal metpo_traitmech_v587
just qc
just validate-history
just validate-products
```

Actual outcomes belong in the structured review and PR. Inspect emitted RDF
as well as ROBOT exits; apply only the scoped required-header-tab exception
to whitespace checks. No ontology is silently upgraded.

After local review, submit the template/rationale to `berkeleybop/metpo` or
the KG-Microbe proposal pipeline. Upstream maintainers choose the final ID,
label and hierarchy. After an explicitly reviewed ontology update, re-seed
and migrate references, retaining `traitmech:000711` as a traceable alias and
preserving append-only history. Curator `codex` is LLM-assisted, not human sign-off.

## Change Log

- v587, 2026-10-12: propose quantity-qualified protein aggregate inheritance
  with three primary DOI sources and explicit measurement/source limitations.
- Same-PR issue #1896 correction: qualify the historical reporter readout and
  add a fourth primary DOI source without changing the definition or ID reservation.
