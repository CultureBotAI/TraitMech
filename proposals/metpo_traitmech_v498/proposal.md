# Autogamy: METPO Proposal v498

## Context

Lift `traitmech:000622 autogamy`, a PROPOSED PHYSIOLOGY class. Pre-write
searches included ignored and hidden files across the repository, pinned
ontology, history, research, proposals and generated artifacts, plus the
available CommunityMech proposal tree. Labels, related self-fertility terms,
source identifiers and the complete proposed block had no exact-record or
allocation collision. Existing fungal self-fertility records are not exact.

A fresh seed emits 399 records: 344 identifiers occur in the 1,016-record
pre-addition corpus and 55 are absent. The complete release-delta and active-
review tables assign those 55 to 38 supporting-field entries and 17 duplicates.
All 38 formerly unselected active classes now have live primary records.
Obsolete reproductive-process/structure entries do not supply an active,
exact phenotype parent. This does not exhaust microbial trait discovery.

On 2026-10-05 the all-state upstream autogamy issue search returned no result.
File inventories of upstream PRs #639, #638, #637 and #629 and TraitMech PRs
#1477, #1476, #973 and paginated #924 contained no competing allocation.

## Scope and Hierarchy

| Scope | Count | Parent | Leaves |
| --- | ---: | --- | ---: |
| A: synthetic traits | 1 | METPO:1000059 phenotype | 1 |
| B: predicates | 0 | Not applicable | 0 |
| C: schema enums | 0 | Not applicable | 0 |

The definition selects the unpaired-cell gametic-nuclear-fusion sense in the
cited ciliate studies. It is not all selfing, plant self-pollination, a literal
mating locus, or a gamete-size class. Existing homothallism, unisexual
reproduction and primary homothallism records are fungal-scoped; they are not
exact parents. Cytogamy in Nobili and Luporini p.39 concerns paired cells
without nuclear exchange, unlike the operational definition selected here.
No universal complete homozygosity, genetic identity of fusing nuclei,
starvation requirement, nuclear count or inability to outcross is imposed.

Use released phenotype `METPO:1000059`, beneath quality `METPO:1000188`,
pending a narrower reproductive-phenotype parent. PHYSIOLOGY is a filesystem
category. Keep PROPOSED pending human curator signoff. No synonym, xref,
SSSOM mapping, protein accession or causal graph is asserted.

## Evidence and Limits

- `DOI:10.1017/S0016672300010740`: definition and natural A-25 example.
  The record distinguishes fixed-cell observations from inferred nuclear
  genetic identity and mt-locus evidence from whole-genome measurements.
  Typeset pp.35-39 and Tables 1-2 were inspected; no Table 3 reanalysis.
- `DOI:10.1016/0014-4827(86)90492-1`, `PMID:3743667`: directly read
  scientific abstract supports unpaired-cell meiosis/fertilization and
  nutritional commitment in Paramecium. Full text and strain provenance
  remain unread; no canonical example or molecular pathway is inferred.
- `DOI:10.1093/gbe/evaa052`, `PMID:32163147`, `PMC7239694`: directly read
  full-text passages support the qualified Paramecium study. The operational
  readout is macronuclear fragmentation, not fusion in every scored cell.
  Stock d12 natural provenance and remaining source material are unresolved.

The qualified canonical example uses `NCBITaxon:74792 Moneuplotes minuta`;
NCBI EFetch confirms the source name Euplotes minuta as a synonym. Taxonomy
resolution does not identify a modern accession or genome for historical A-25.
Source provenance supports a naturally collected, subsequently maintained
strain, not every member of the species or the paper's nonautogamic controls.

Three directly checked contiguous snippets accompany the counted citations.
The diatom terminology source `DOI:10.1080/0269249X.2013.791344` remains only
a discussion research lead: the author repository supplied metadata, not the
required full-text passage. It does not count toward the evidence gate or
establish paedogamy/automixis equivalence. Retain actual resolver verdicts;
manual PDF/XML checks are not renamed resolver successes.

The maintained resolver returns VERIFIED for Berger, NOT_IN_ABSTRACT for
Thind and UNRESOLVED for Nobili and Luporini. An exact DOI query independently
retrieved `PMID:4964874`, matching the 1967 paper but without abstract text.
The last verdict is not evidence that the DOI is unindexed or invalid.

## ID Space and Artifacts

Reserve `METPO:1057500` in the fresh `1057500-1057599` block after v497,
with subset `metpo_traitmech_2026_10`. No merged block is reused. Scope A
has one newly minted local record and one class row; B and C are empty.

`metpo_proposal_classes_robot.tsv` has one class plus two 11-column headers.
The header follows Knowledge-Graph-Hub/kg-microbe commit
`ea1c5f15e6c4dba6c72165367162b354e215f018`; CommunityMech v1 is the worked
reference. Definition sources are citations, not ontology equivalences.
Neither property nor mapping templates are required.

## Verification

```bash
just verify-proposal metpo_traitmech_v498
just robot-validate-proposal metpo_traitmech_v498
just audit-proposal-coverage
just validate-history
just validate-products
just qc
.venv/bin/python -m pytest -q
```

Require record/template parity and inspect the actual w3id autogamy class,
labeled phenotype parent and quality ancestor, not merely ELK's exit status.
Run the maintained snippet verifier and NCBI API example audit. Regenerate
discussions, QC dashboard, trait pages, priority outputs and affected audits.

Local ROBOT/ELK passed without UNSAT (23,322 merged lines; 23,326 reasoned
lines). Structured OWL inspection confirmed the labeled w3id autogamy to
phenotype to quality chain without legacy OBO-prefix parent stubs. NCBI API
resolution passed for all 716 examples with zero errors and 24 pre-existing
label warnings, none concerning the new example. Desktop (1440 px) and mobile
(390 px) browser checks passed for identity provenance, three snippets, the
qualified example and the refreshed 1,017-record dashboard, without overflow
or JavaScript errors. Both exact configured embedding-source paths were
absent, so embedding artifacts were not regenerated.

## Upstream and Round Trip

Submit the verified template to `berkeleybop/metpo`. Until acceptance and
release, `traitmech:000622` remains primary; the proposed METPO ID is not a
released identifier. After release, refresh the pinned ontology, migrate to
the accepted CURIE, preserve the local ID in a migration artifact and
append-only history, and regenerate dependent products without creating a
second primary record.

## Change Log

- v498, 2026-10-05: propose autogamy with three cited snippets, a qualified
  natural example and explicit assay, taxonomy and genetic-outcome limits.
