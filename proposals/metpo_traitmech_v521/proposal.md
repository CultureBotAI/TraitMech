# Proteaphagy: METPO Proposal v521

## Context

Add `traitmech:000645 proteaphagy`, a PROPOSED PHYSIOLOGY class, on base
`8c076226fbfe1c67bf022ef218b88d71e70c7e62`. This is autophagic degradation
of proteasomes as cargo, not proteolysis performed by a proteasome, a gene
inventory or a sequence feature.

Whole-tree searches included ignored and hidden files, likely spellings,
proteasome autophagy/degradation, the three primary DOI/PMID bundles,
the correction DOI/PMID, a later 2022 study, available PMC IDs, GO:0061816,
the local identifier and complete 1059800-1059899 block. CommunityMech
proposals were searched with the same candidate/block scope. No exact record
or allocation was found. A broad multiline search found a human-pathogen
research report's host gasdermin-D proteasomal degradation: a substrate being
degraded by a proteasome, not the proteasome cargo phenotype. No existing
exact graph node, synonym or discussion needs migration.

All-state indexed GitHub searches returned no proteaphagy issue/PR match in
TraitMech or upstream METPO, and no prospective-ID hit upstream; results were
not marked incomplete. Separately, #1756's directly read landing comment
already named proteaphagy as a research lead, not an accepted allocation.
Search-index silence does not erase that known comment.

The pre-addition corpus contains 1,039 records. A fresh 399-record METPO seed
shares 344 identifiers; the 55 absent terms comprise 38 supporting-field
terms and 17 reviewed duplicates. All 38 formerly unselected classes are
already live. The complete 1,546-row release delta, 153-row active review
and 12,617-triple pinned METPO graph contain no candidate or prospective
block hit. These checks establish candidate novelty, not frontier exhaustion.

## Scope and Hierarchy

| Scope | New Classes | Parent |
| --- | ---: | --- |
| A: synthetic trait | 1 | traitmech:000638 autophagy / METPO:1059100 |
| B: predicates | 0 | Not applicable |
| C: schema enums | 0 | Not applicable |

Proteasome cargo narrows the existing autophagy phenotype. The 2016
starvation paper supports independent targeting of core and regulatory
particles, so the definition includes subcomplexes rather than requiring
intact 26S holoenzyme uptake. Free-subunit loss, storage granules, nuclear
localization, ATG genes and total abundance changes alone do not establish
completed autophagic degradation. Ribophagy and nucleophagy are distinct
cargo phenotypes, not synonyms inferred from shared machinery or location.

[GO:0061816](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0061816)
was resolved directly at QuickGO: it is nonobsolete and denotes selective
proteasome degradation by macroautophagy. This biological process is not an
exact organismal-phenotype equivalent. The cargo-defined local phenotype
does not impose a universal route, trigger or selectivity mechanism; the
scope distinction remains explicit for human review. No exact synonyms,
xrefs or SSSOM mappings are asserted.

## Evidence and Limits

| DOI | PMID | Role |
| --- | --- | --- |
| 10.1074/jbc.M115.699124 | 26670610 | Definition, vacuolar turnover and separate core/regulatory cargo |
| 10.1016/j.celrep.2016.07.015 | 27477278 | Starvation versus inactive-particle quality-control routes |
| 10.1016/j.jbc.2021.101494 | 34919962 | Cargo-specific regulation and conditional ATG11 dependence |

All three snippets match directly retrieved scientific abstracts with matching
DOIs. The maintained live resolver reports **three VERIFIED**. The papers are
three primary publications, not three independent research groups or a
correction counted as replication.

For the first study, XML scientific abstract, yeast-strain and immunoblot
Methods, autophagy-dependence and core/regulatory-particle Results, Table 1
and relevant captions were read. Figure 6D's Rpn10 caption conflicts with
its title and body; no Rpn10 requirement is asserted. Actual figures and
supplements were not inspected. The Cell Reports study was read through its
scientific abstract, not full Methods or actual figures.

The Cell Reports metadata links correction DOI
`10.1016/j.celrep.2022.110552`, PMID `35294886`. Its text was directly read
at the [authors' institutional record](https://profiles.wustl.edu/en/publications/erratum-autophagic-turnover-of-inactive-26s-proteasomes-in-yeast-/):
a duplicated anti-histone H3 control blot in Figure S3 was replaced, and the
authors report unchanged conclusions. The actual corrected figure was not
inspected. The correction remains cited in evidence notes and the mechanism
discussion, not treated as separate trait evidence.

For the later Waite study, XML scientific abstract, Results sec1.1-sec1.3,
Discussion sec2 and Methods sec3.1-sec3.4 were read. The ATG11 result concerns
residual starvation-induced turnover in an ATG17 deletion background. The
rapamycin ATG11 single-deletion comparison shows no detected difference,
with a detection-limit caveat. This is not a blanket contradiction of the
earlier single-deletion result, nor a universal ATG11 presence requirement.
Native gels and vacuolar reporter processing strengthen the cargo-turnover
interpretation; general-autophagy reporters are not sufficient alone.
Captions were read, but actual figures and supplements were not inspected.

No unqualified quantitative panel claim, canonical natural-strain exemplar
or accession-level causal graph is added. W303-derived reporter/deletion
hosts do not establish independent natural-strain provenance. Two OPEN
discussions retain mapping, source-panel, exemplar and mechanism gaps.

## Relationship to v520

The v521 TSV copies the corrected `METPO:1059100` parent context from v520
unchanged. This is dependency context, not a new parent allocation. The
autophagy YAML and historical proposals remain unchanged. v519 originally
corrected the older cytoplasmic-only parent wording under #1754; do not
reintroduce the superseded definition when combining cohorts.

The writer guards the complete current parent and v520 template, defaults
to dry run, rejects target/proposal drift and validates before production
writes. It never writes the parent or historical template. Controlled test
fixtures use separate hashes without weakening production guards.

## ID Space and Files

Reserve `METPO:1059800` in fresh block 1059800-1059899, following v520.
Local identifier: `traitmech:000645`; subset: `metpo_traitmech_2026_10`.
The current upstream kg-microbe contract and templates were freshly retrieved
at `1408e7099d039026d7611c240938d8e177753406`. Classes use the canonical
11-column header; canonical properties have 13 columns. CommunityMech v1's
three reference files were read end-to-end. Local, CommunityMech and pinned
upstream checks found no candidate/block collision. METPO IRIs use w3id.

| Artifact | Rows |
| --- | ---: |
| metpo_proposal_classes_robot.tsv | 1 new class + 1 unchanged parent-context class |
| property template | Omitted |
| SSSOM mappings | Omitted |

## Verification

Guarded writer dry run and 43 focused tests pass. They cover cargo identity,
correction and conditional dependence, dry-run/apply/replay, parent/template
preservation, drift refusal and validation before writing. Direct LinkML and
strict validation, proposal verification, ROBOT/ELK and history validation
pass. Parsed RDF counts are 25 class-template triples, 12,638 merged triples
and 12,642 reasoned triples. The w3id child-parent-phenotype-quality hierarchy
and single corrected parent definition were checked explicitly.

The corpus now has 1,040 unique records, 525 PROPOSED, 159 PHYSIOLOGY, and
582 discussions across 511 records. The artifact audit confirms that all
1,039 existing YAML records and all 525 historical proposal TSVs and their
narratives remain unchanged. Of the existing pages, 1,038 change only in
their corpus footer; autophagy also gains the child link. Its priority child
count changes from six to seven, with no other existing priority-row delta.
Shared discussion templates and the protected spore-germination record
remain unchanged.

Playwright checks at 1,440 and 390 pixels pass for identity, three quotes,
two OPEN discussions, correction/context limits, parent navigation and
the 1,040-record dashboard with its coverage image loaded. Actual screenshots
were inspected, with no overflow or page errors. Embeddings were not
regenerated because both configured source paths are absent.

`just qc`, `just validate-products`, Ruff, canonical-example offline audit
and full-suite validation pass: **2,683 tests passed in 614.68 seconds**,
with two dependency deprecation warnings. The separate README, priority and
QC-dashboard run passed 45 tests. Staged PR sanity passes. Ordinary staged
whitespace checking flags only the three required empty ROBOT directive cells;
canonical header widths and exact-path scoped whitespace checks pass.
No frozen baseline was changed. Committed-history, exact-head review, CI
and landing results will be recorded on the PR after verification.

## Upstream and Round Trip

Submit the child plus unchanged corrected parent context and scope discussion
to upstream METPO after review. Once accepted, refresh METPO and migrate the
local identity and parent references to accepted identifiers while retaining
the old local identifier's provenance and history. Regenerate derived data
without creating duplicate records. Resolve the independent scientific
discussions separately rather than treating upstream minting as proof.

## Change Log

- v521, 2026-10-06: propose microbial proteasome-cargo autophagy with three
  source-matched snippets and explicit subcomplex, mechanism and correction limits.
