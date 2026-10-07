# Contact-Dependent Outer Membrane Exchange: METPO Proposal v526

## Context

Add `traitmech:000650 contact-dependent outer membrane exchange`, a PROPOSED
PHYSIOLOGY class, on base `b06c5edf42976277b619c480d16cf1e852db96b4`.
The record denotes an organismal membrane-transfer phenotype, not an outer
membrane material entity, a gene/domain feature or a universal social function.

Ignored-and-hidden whole-repository searches covered candidate terminology,
protein names, source DOI/PMID bundles and prospective identifiers. No exact
record, unresolved exact causal node or conflicting reservation was found.
An initially broad numeric search also matched unrelated ontology identifiers;
the exact DOI and word-bounded terminology search was rerun across the full
tree, not inferred from that noisy result.

A fresh seed contains 399 records; 344 identifiers occur in the pre-addition
1,044-record corpus. The 55 absent seed terms are 38 supporting-field terms
and 17 reviewed duplicates. All 38 formerly unselected classes are now live.
Structured review covered 1,546 release-delta rows, 153 active-review rows
and the 12,617-triple ontology. No exact exchange class or block collision
was found. Conjugation and secretion neighbors are deprecated and not exact.
This establishes candidate novelty, not exhaustion of trait discovery.

The all-state GitHub search returned upstream
[#268](https://github.com/berkeleybop/metpo/issues/268), about membrane/cell-wall
structures, and historical TraitMech PRs #19, #66 and #73, about Gram stain,
generic node grounding and a numerical-axis predicate. Their bodies and
comments do not propose this exchange trait. The
[PR #1762 receipt](https://github.com/CultureBotAI/TraitMech/pull/1762#issuecomment-6025061922)
names this unallocated research lead. No indexed reservation for 1060300 was
found; search-index absence is not proof that a discussion never occurred.

## Scope and Hierarchy

| Scope | New Classes | Parent |
| --- | ---: | --- |
| A: synthetic trait | 1 | METPO:1000059 phenotype |
| B: predicates | 0 | Not applicable |
| C: schema enums | 0 | Not applicable |

The endpoint is contact-dependent exchange of outer-membrane lipids and
proteins. It does not require equal reciprocal flux, every cargo moving at
every contact, killing, cooperation, kin discrimination or development.
It is distinct from cytoplasmic fusion, conjugative DNA transfer and a
generic secretion phenotype. Exocytosis (`traitmech:000637`) and extracellular
vesicle production (`traitmech:000649`) are not broader classes for it.
Cell-free vesicle transfer and slime-trail deposition alone are insufficient.
Co-occurrence is possible; no organism-level disjointness is asserted.

Keep the explicit contact qualifier and conservative phenotype parent.
Omit exact synonyms, xrefs and SSSOM mappings until equivalence is established.
No existing record needs reparenting or same-scope grounding repair.

## Evidence and Limits

| DOI | PMID | Role |
| --- | --- | --- |
| 10.7554/eLife.00868 | 23898400 | Definition and live material transfer; PMC3721248 |
| 10.1371/journal.pgen.1002626 | 22511878 | Genetic and dye-transfer evidence; PMC3325183 |
| 10.1128/jb.00850-13 | 24391054 | Tube abundance is not the exchange endpoint; PMC4011004 |
| 10.1371/journal.pone.0224817 | 31774841 | Limits on ecological-function claims; PMC6880969 |

The 2012, 2013 and 2019 snippets come from directly read scientific abstracts
in Europe PMC XML. The 2014 snippet comes from the directly retrieved core-API
abstract; full-text XML retrieval failed, and no full-text verification is
claimed for that paper. Search-result text was used only as a lead.

Selected Results and Methods of the positive studies were read. Actual 2013
Figures 2 and 4 were inspected with their captions: fluorescent protein
transfer, lipid-dye transfer and tube continuity are distinct observations.
Significant protein transfer through the tubes was not detected. Videos and
the remaining panels/supplements were not inspected. The 2012 and 2014 studies
share investigators and are not independent-laboratory replications.

The 2019 Results sec012/sec014 were also read. Their mutant controls and
negative colony-boundary result do not establish direct membrane transfer in
every natural isolate. The directly read correction
DOI:10.1371/journal.pone.0228697 (PMID:31999808, PMC6991971) concerns Table 3
typesetting; no numerical Table 3 claim is used. It is not an independent
trait-evidence item.

No canonical natural-strain example or accession-resolved causal graph is
asserted. Two OPEN discussions retain mapping, strain provenance and protein
grounding tasks. TraA/TraB dependence is known; remaining work must distinguish
that evidence from universal fusogen chemistry. Sequence-domain resemblance
alone cannot establish the phenotype or the role of a paralog.

## ID Space and Files

Reserve fresh block 1060300-1060399, using `METPO:1060300`, after v525's
1060200 block. Local ID: `traitmech:000650`.
Subset: `metpo_traitmech_2026_10`. Earlier cohorts remain unchanged.

The upstream contract remains pinned to
`Knowledge-Graph-Hub/kg-microbe@1408e7099d039026d7611c240938d8e177753406`.
The previously read skill and canonical 11/13-column template blobs were
rehash-verified against that unchanged current commit. The relevant local
guidance and worked examples remain unchanged from the preceding reviewed
cohort. Local, CommunityMech-proposal and pinned-upstream checks found no
candidate/block collision. The writer guards reviewed parent scope and
target/template preimages, prevalidates and defaults to dry run.

| Artifact | Rows |
| --- | ---: |
| metpo_proposal_classes_robot.tsv | 1 new class |
| property template | Omitted |
| SSSOM mappings | Omitted |

## Verification

Direct LinkML and strict validation, `just qc`, history/products, Ruff,
proposal verification/coverage and ROBOT ELK passed. All 20 writer tests,
45 artifact-focused tests and the full 2,830-test suite passed. The full suite
reported two dependency deprecation warnings. The online snippet resolver
returned four VERIFIED results; all four quotes also matched directly retrieved
scientific-abstract spans. The initial sandbox DNS failure was retried with
network access rather than represented as verification.

Parsed RDF contains 15 class-template, 12,628 merged and 12,632 reasoned triples.
The new class has real w3id METPO phenotype/quality ancestry, not legacy
METPO stubs. Both header rows and the data row retain the canonical 11 columns.
The ordinary staged whitespace check flags only the three required empty
trailing ROBOT directive cells; inspected exact-path scoped checks passed.

The corpus has 1,045 records and 592 discussions. README counts, pages,
priority, discussion data, citation report and the published QC dashboard
were regenerated. All 1,044 prior YAML files and 530 historical proposal
templates remain byte-identical. Of the existing trait pages, 1,043 change
only in their footer; phenotype gains its child and changes its child count
from 145 to 146. Historical narratives and discussion templates are unchanged.
The shared generator matches all 139 source blobs of reviewed claw commit
`6d0a6fbbaeec47f42c6f999233b460e3f56bae89`. Both configured embedding inputs
are absent, so embedding regeneration is not claimed.

Browser checks at 1440/390 px passed identity, provenance, four quotes,
source limits, parent navigation, dashboard counts and image loading, with
no page errors or overflow. Screenshots were visually inspected. No canonical
example or protein-example change triggers a new accession API audit.
The committed-history gate, exact-head review and actual CI/merge outcomes
will be recorded on the PR; they are not preclaimed here.

## Upstream and Round Trip

Submit the class and scope notes to upstream METPO after review. No new upstream
issue is claimed. After acceptance, refresh the ontology, migrate the local
identifier and references to the accepted METPO ID, preserve provenance and
append-only history, and regenerate products without creating a duplicate.
Scientific discussions require separate review.

## Change Log

- v526, 2026-10-06: propose contact-dependent outer membrane exchange with
  direct transfer evidence and explicit tube, ecological and sequence limits.
