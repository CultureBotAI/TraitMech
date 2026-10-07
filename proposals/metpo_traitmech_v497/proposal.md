# Anisogamy and Oogamy: METPO Proposal v497

## Context

Lift `traitmech:000620 anisogamy`, a PROPOSED PHYSIOLOGY class.
Pre-write searches included ignored and hidden files, labels, lexical variants,
source identifiers, taxon names and the proposed identifier block. The only
biological matches were isogamy's scope notes and corresponding artifacts;
there was no exact primary record, proposal or allocation collision. The
available CommunityMech proposal tree was also checked for block collisions.

A fresh METPO seed emits 399 records: 344 identifiers occur in the 1,014-record
pre-addition corpus and 55 are absent. The frozen active-review table assigns
those 55 to 38 supporting-field entries and 17 duplicate entries. Neither the
pinned ontology nor the seed contains an anisogamy, oogamy or heterogamy match.
The release tables' obsolete reproductive-process/structure entries do not
provide an active, exact phenotype parent.

The all-state upstream anisogamy issue search returned no result on 2026-10-05.
Open upstream PRs #639, #638, #637 and #629 have no competing term allocation.
TraitMech open-PR file inventories (#1477, #1476, #973 and paginated #924)
likewise contain no overlapping trait/proposal reservation. This is not a
claim that microbial trait discovery is exhausted.

The v497.1 extension adds `traitmech:000621 oogamy`. A fresh 399-record
seed against the 1,015-record pre-extension corpus again had 344 overlaps and
55 absent identifiers (38 supporting fields, 17 duplicates). Ignored-and-hidden
whole-repository searches found only anisogamy's oogamy scope mentions, not an
exact record or proposal. Searches also covered the available CommunityMech
proposals and found no `traitmech:000621` or `METPO:1057410` collision. The
all-state upstream oogamy issue search and the same open-PR file inventories
were rechecked on 2026-10-05 with no competing allocation. The parent discussion
now links the child while retaining its other unresolved scope questions.

## Scope

| Scope | Count | Parent | Leaves |
| --- | ---: | --- | ---: |
| A: synthetic traits | 2 | METPO:1000059 phenotype; METPO:1057400 anisogamy | 1 |
| B: predicates | 0 | Not applicable | 0 |
| C: schema enums | 0 | Not applicable | 0 |

## Hierarchy Decisions

The class denotes size dimorphism between fusing gamete types. It is not a
literal mating locus, vegetative-cell size variation, self-fertility or a
compatibility-locus system. The broad scope includes oogamy, following the
explicit terminology in Lindsey et al. (2024). Nozaki et al. (2014) use a
narrower, motility-qualified classification. Preserve that difference rather
than declaring disjointness or universal motility requirements. No numerical
size cutoff, fertilization-location restriction or causal dependency is imposed.

Kaczmarska et al. (2017), DOI:10.1371/journal.pone.0181413, also use
physiological/behavioural anisogamy for approximately equal-sized gametes in
diatoms. That is not equivalent to this size-based sense: behavioural or
physiological differences alone do not establish size dimorphism. Keep that
usage out of exact synonyms and review its relationship separately, without
asserting organism-level disjointness. This addresses review finding #1711.

The anisogamy record and template use released `METPO:1000059 phenotype`, beneath
`METPO:1000188 quality`. A narrower reproductive-phenotype parent remains a
TODO. PHYSIOLOGY is a filesystem category, not an ontology superclass.
Keep PROPOSED status pending human curator signoff.

Oogamy is the narrower phenotype with larger nonmotile female gametes and
smaller male gametes. Its local parent is `traitmech:000620`, mapped here to
the existing `METPO:1057400` proposal row. Vranken et al. (2023), Figure 2,
explicitly allow nonmotile male red-algal gametes; the typical motile-male
formulation in Lindsey et al. is therefore not a universal condition. Size
compares gamete types, not a sperm packet with an egg. Neither heterothallism,
monoecy/dioecy, a numerical size ratio nor a MID/MAT sequence feature defines
this class. The parent-child relation follows the broad size-based anisogamy
sense already selected above.

## Evidence and Limitations

- `DOI:10.1038/s42003-018-0019-5`, `PMID:30271904`, `PMC6123790`:
  definition authority and independent phenotype observations; the record
  preserves an unresolved Results/Methods strain discrepancy.
- `DOI:10.1186/1471-2148-14-37`, `PMID:24589311`, `PMC4015742`:
  direct phenotype evidence and a qualified `NCBITaxon:51706`
  Colemanosphaera charkowiensis example. Collection provenance is not
  counted as independent experimental evidence.
- `DOI:10.1186/s12915-024-01878-1`, `PMID:38600528`, `PMC11007952`:
  explicit broad terminology, not experimental replication.
- `DOI:10.1371/journal.pone.0181413`: diatom terminology caveat, not an
  additional size-dimorphism experiment or canonical example. The scope clause
  directly matches publisher HTML and manuscript XML; only the relevant
  Discussion passage and opening live-cell Results paragraphs were inspected.

The record documents inspected sections, figures and strain provenance, plus
unread source material and collection-date conflicts. Genomic association and
expression data are not promoted to a gamete-size mechanism. No causal graph,
protein accession, synonym, xref or SSSOM mapping is asserted.

The original three snippets exactly match the raw full-text XML. The maintained abstract
resolver returns LIKELY_PARAPHRASE for the 2018 clause (its returned abstract
uses hyphens where the article XML uses em dashes), VERIFIED for the 2014
abstract sentence, and NOT_IN_ABSTRACT for the 2024 Background clause. These
verdicts are retained, not relabeled as successful resolver checks.
The fourth snippet is a source-verified Discussion clause; its maintained
resolver verdict is also NOT_IN_ABSTRACT, not VERIFIED.

Oogamy adds these evidence roles (four citations, not four replications):

- `DOI:10.5194/essd-15-2711-2023`: definition authority, inspected Figure 2
  and caption, including the nonmotile-male exception. This seaweed trait
  compilation supports terminology, not a canonical microbial experiment.
- `DOI:10.1186/s12915-024-01878-1`: broad anisogamy hierarchy; the same
  directly checked Background clause used above.
- `DOI:10.1186/s40529-018-0227-9`, `PMID:29616358`, `PMC5882469`:
  natural Volvox reference-strain observations, actual Figure 2, Table 1 and
  relevant main text. `NCBITaxon:3068` is the verified forma-level name
  Volvox carteri f. nagariensis. NIES-4206/4208 collection entries corroborate
  aliases and ITS2 LC376032/LC376034, but their May 25 collection date
  conflicts with the paper's June 9/10 dates. Their 2022 axenic status is not
  evidence of 2018 culture status. Zygotes after possible fertilization are
  not directly tracked fusion events. PCR absence is not demonstrated deletion.
- `DOI:10.1371/journal.pbio.1001904`, `PMID:25003332`, `PMC4086717`:
  MID perturbation evidence in engineered backgrounds, distinguished from
  native controls in actual Figure 2 and Table S3 extracted text. This is a
  mechanism lead, not a universal mechanism or a natural engineered-strain
  exemplar. Protein grounding and unread material remain explicit TODOs.

The new record preserves exact snippet locations, inspection limits and
collection URLs. Its four snippets were directly checked against retrieved
publisher HTML or raw XML. The maintained abstract verifier returned VERIFIED
for Geng, NOT_IN_ABSTRACT for Lindsey and Nozaki, and UNRESOLVED for Vranken.
A direct unquoted DOI query to Europe PMC returned zero records for Vranken;
Crossref confirmed the exact DOI, title and 2023-07-04 publication date. Manual
full-text checks are not renamed resolver successes.

## ID Space and Subset

Reserve `METPO:1057400` in `1057400-1057499`, after v496's block, with
subset `metpo_traitmech_2026_10`. This is outside CommunityMech v1's
`1007100-1007220` block. The proposed identifier is not released;
`traitmech:000620` remains the primary identifier until upstream acceptance.

Extension v497.1 reserves `METPO:1057410`, ten above the existing identifier,
inside the same `1057400-1057499` block and with the same subset. This is Path B
(extend in place): the original row is byte-identical and the child row is
appended. `traitmech:000621` remains the child's primary identifier. Keeping
both rows in one cohort preserves the actual parent in standalone ROBOT output.

## Files

| Artifact | Rows | Purpose |
| --- | ---: | --- |
| `metpo_proposal_classes_robot.tsv` | 2 classes + 2 headers | Scope-A parent and child |
| `proposal.md` | Not applicable | Scope, evidence and migration |

No property or mapping template is required. The 11-column class header follows
Knowledge-Graph-Hub/kg-microbe commit
`ea1c5f15e6c4dba6c72165367162b354e215f018`, including three empty trailing
directive cells. Its pinned contract was retrieved because the expected local
checkout is unavailable; CommunityMech v1 is the worked reference. Legacy
OBO-prefix examples do not override the pinned ontology's w3id IRIs.

## Verification

```bash
just verify-proposal metpo_traitmech_v497
just robot-validate-proposal metpo_traitmech_v497
just audit-proposal-coverage
just qc
```

Require label, definition and parent parity between record and template. Inspect
the actual proposed w3id class and labeled phenotype/quality ancestry, not only
the ELK exit status. Before the extension, local verification passed with zero proposal failures.
ROBOT/ELK passed without UNSAT (23,322 merged lines; 23,326 reasoned lines).
Structured inspection confirmed `https://w3id.org/metpo/1057400` below the
labeled phenotype and quality classes, without legacy OBO-prefix parent stubs.
The NCBI API canonical-example audit resolved all 714 examples with zero errors
and 24 pre-existing label warnings; none concerned the anisogamy example.
The extension passed with zero proposal failures and no UNSAT (23,339 merged
lines; 23,343 reasoned lines). Structured OWL inspection verified the labeled
oogamy-to-anisogamy-to-phenotype-to-quality chain at the w3id IRIs, without
legacy-prefix parent stubs. The NCBI API audit resolved all 715 examples with
zero errors and the same 24 pre-existing label warnings; none concerns oogamy.
Desktop (1440 px) and mobile (390 px) browser checks verified the rendered
evidence, example, local identifier provenance and refreshed 1,016-record QC
dashboard, with no horizontal overflow or JavaScript errors. Exact embedding
source paths were absent, so embedding artifacts were not regenerated.

## Upstream Path

Submit the validated template to `berkeleybop/metpo` after local review.

## Round-Trip Plan

After acceptance and release, refresh the pinned ontology and migrate the
records to their accepted METPO CURIEs, including the child's parent reference.
Preserve both local identifiers in an explicit
migration artifact and append-only history, regenerate dependent artifacts,
and do not create a second primary record for the same phenotype.

## Change Log

- v497, 2026-10-05: propose anisogamy with three cited sources, exact snippets,
  explicit size-based scope and a provenance-qualified canonical example.
- Review correction #1711: add a fourth cited source documenting behavioural
  usage without size dimorphism; preserve the selected definition and example.
- v497.1, 2026-10-05: extended with oogamy (+1 class, +0 properties),
  preserving the original row and subset; link the child from anisogamy's
  discussion and retain nonmotile-male and strain-provenance qualifications.
- Review correction #1713: distinguish the mature cross-derived zygote in
  Geng Figure 2E from the engineered parent and sperm in D/G/I. No definition,
  hierarchy, snippet or template-row change.
