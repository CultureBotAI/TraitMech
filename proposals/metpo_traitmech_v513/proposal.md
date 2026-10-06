# Exocytosis: METPO Proposal v513

## Context

Add `traitmech:000637 exocytosis`, a PROPOSED PHYSIOLOGY class for a
microbial cell's secretion phenotype. Base:
`073f0afa35a4a13ff5f8aa0948fc4007dcb56c36`.

Ignored-and-hidden whole-repository searches covered label variants,
source identifiers, the local ID, cohort and prospective METPO block.
CommunityMech proposals were included in the reservation search. No exact
record or reservation was found. All-state GitHub issue/PR searches in
TraitMech and METPO returned no exocytosis result; the upstream placeholder
query was also empty, with complete search results.

A fresh seed contains 399 records, sharing 344 identifiers with the
1,031-record pre-addition corpus. The 55 absent IDs reconcile to 38
supporting-field terms and 17 reviewed duplicates. The complete 1,546-row
release delta and 153-row active review were parsed; all 38 formerly
unselected classes are live. All 12,617 pinned METPO triples were searched
for the candidate and prospective block. The related `METPO:1000274`
obsolete secretion and `METPO:1000275` obsolete secretion system are
deprecated, broader concepts, not equivalent identifiers to revive.
This establishes local novelty, not literature exhaustion.

## Scope and Hierarchy

| Scope | New Classes | Parent |
| --- | ---: | --- |
| A: synthetic trait | 1 | METPO:1000059 phenotype |
| B: predicates | 0 | Not applicable |
| C: schema enums | 0 | Not applicable |

Material release through an organelle-plasma-membrane fusion pore is the
defining endpoint. Docking or fusion without release does not alone
establish the secretion phenotype. Constitutive and stimulus-regulated
events are included; complete emptying, permanent vesicle collapse and a
universal calcium response are not required. This is neither a sequence
feature nor a host-cell response.

The live QuickGO record for `GO:0006887` provides terminology context,
including partial release through transient pores:
https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0006887.
It denotes a biological process, not an equivalent organismal phenotype;
no xref, SSSOM mapping or synonym is asserted. Nonmicrobial examples in
that definition are not independent microbial evidence.

Structured label/definition/synonym review distinguishes the existing
uptake, hyphal-fusion, gas-vesicle, phage-defense, conjugative-element,
polymer-degradation and surfactant-associated motility records. Secretion
of an enzyme does not establish its route. The contextual ER-Golgi
apoplastic-effector pathway in `plant_pathogen` is not an exact phenotype
node to re-ground. No older record is reparented or modified. Existing
organism-level traits are not declared mutually disjoint.

## Evidence and Limits

- `DOI:10.1083/jcb.56.1.153`, `PMID:4629881`, `PMC2108847`:
  Satir, Schooley and Satir (1973), definition authority. A 15-word
  scientific Abstract span was directly checked in Europe PMC XML and
  PubMed; its missing terminal punctuation is retained. The abstract
  connects mucocyst membrane fusion, pore enlargement and discharge.
  Some discharge is fixation-triggered. Historical Tetrahymena taxonomy
  and strain provenance remain unresolved. Sparse XML and an HTML
  response to the PDF endpoint do not constitute full-method or figure
  access. https://pubmed.ncbi.nlm.nih.gov/4629881/
- `DOI:10.1007/BF01870409`, `PMID:1744905`: Lew and Simon (1991).
  A 16-word scientific Abstract span was directly checked in NCBI PubMed
  XML and Europe PMC metadata. Conditional yeast mutants allow release
  of accumulated vesicle contents at permissive temperature. This
  supports constitutive scope; measured calcium independence is
  condition-specific. Full methods, figures and strain provenance were
  not read. https://pubmed.ncbi.nlm.nih.gov/1744905/
- `DOI:10.1016/s0143-4160(98)90030-6`, `PMID:9681197`: Klauke et al.
  (1998). A 20-word scientific Abstract span was checked in both APIs.
  Relevant primary Methods, Results and Discussion were read; PDF pages
  349-350 and 354-356, including Figures 6-9, were visually inspected at
  https://d-nb.info/1107191386/34. The tnd1 mutant separates fusion from
  normal cargo discharge. It is boundary evidence, not a positive example
  of completed secretion. Other figures/tables were not visually audited.

The first two studies support secretion; the third constrains endpoint
interpretation. No reference is counted merely because it supplies strain
provenance. Three short quotes are independently exact-matched to directly
retrieved scientific abstracts and return VERIFIED at 1.00 with the
maintained resolver. Canonical examples, protein accessions and causal
graphs remain unset; two OPEN discussions retain mapping and
exemplar/mechanism gaps. No shared molecular machinery is inferred from
cross-system phenotype evidence. The two-citation gate is not relaxed.

## ID Space and Files

Reserve `METPO:1059000` in the free 1059000-1059099 block, following v512.
Local ID: `traitmech:000637`; subset: `metpo_traitmech_2026_10`.
No overlap with CommunityMech proposals was found, including ignored
files. The Knowledge-Graph-Hub/kg-microbe contract was rechecked at
`1408e7099d039026d7611c240938d8e177753406`. Its class template has 11
columns; the 13-column property template is irrelevant to this class-only
cohort. Use the pinned ontology's w3id namespace, not the legacy purl
example. Definition provenance cites the local codex minting record and
the three primary DOIs; the boundary paper is not positive secretion
evidence by itself.

| Artifact | Rows |
| --- | ---: |
| metpo_proposal_classes_robot.tsv | 1 |
| property template | Omitted |
| SSSOM mappings | Omitted |

## Verification

The guarded dry run and all 19 focused tests passed before application.
Tests cover secretion scope, source/access limits, parent projection
guards, target/proposal drift, controlled temporary fixtures, immutable
dry runs, exact replay and validation-before-write. The new record has a
curation event and append-only repository history. Broader gates and
exact-head CI results are distinguished below.

Local validation passed: LinkML and strict validation, all 1,032 corpus
records under `just qc`, `just validate-history`, `just validate-products`,
proposal verification and cross-cohort coverage, ROBOT/ELK, Ruff, and the
full suite (2,439 passed, two warnings, 622.88 seconds). The three snippet
resolver rows are VERIFIED at 1.00. The canonical-example shape audit and
research-artifact verification also passed; no new canonical examples
were added and that local shape audit did not resolve NCBI taxonomy.

RDF parsing found 15 class-template, 12,628 merged and 12,632 reasoned
triples. The proposed class and its labeled parent use the w3id namespace
and retain the expected hierarchy. The class template exactly matches
the upstream 11-column headers; its directive header requires three
trailing tabs. Whitespace checks use the documented exception for that
exact TSV only.

Generated artifacts were audited against the base: all 1,031 existing
trait YAMLs are unchanged, 1,030 old trait pages change only in their
corpus footer, and the phenotype page adds the new child (141 to 142).
Discussion browser templates and navigation are unchanged. The QC
dashboard reports 1,032 records and zero FAIL slots; the discussion data
has 566 discussions across 503 records. Browser checks at 1,440 and 390
pixels passed for local-ID provenance, all three quotes, access limits,
two OPEN discussions, hierarchy navigation, image loading and overflow,
with no page errors. Desktop and mobile screenshots were inspected.
Neither configured embedding source is present; embedding data was not
regenerated. The protected spore-germination YAML remains byte-identical.

PR review, exact-head CI and merge-queue results will be recorded on the
pull request after submission; no independent approval is claimed here.

## Upstream and Round Trip

Submit this cohort for METPO review after TraitMech signoff. Upon upstream
acceptance, refresh the pinned ontology, migrate the local identifier and
references to the accepted METPO ID, preserve minting provenance and
append-only history, and regenerate without a duplicate primary record.
PROPOSED status awaits human curator signoff. The mapping and
exemplar/mechanism discussions remain OPEN.

## Change Log

- v513, 2026-10-06: propose microbial exocytosis with three DOI-backed
  snippets, a secretion endpoint and explicit limits on fusion-only evidence.
