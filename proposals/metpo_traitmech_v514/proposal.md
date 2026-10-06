# Autophagy: METPO Proposal v514

## Context

Add `traitmech:000638 autophagy`, a PROPOSED PHYSIOLOGY class, on base
`2e9a3736502a8f8a43fc50e520169afe34215a82`.

Whole-repository searches included ignored and hidden files, candidate
labels, source identifiers, the local identifier and the prospective
1059100-1059199 block. CommunityMech proposals were included. No exact
record or reservation was found. All-state TraitMech and METPO GitHub
searches for autophagy returned zero results, as did the upstream
1059100 query; all responses reported complete results.

The current 1,032-record corpus shares 344 IDs with a fresh 399-record
seed. The 55 absent IDs reconcile to 38 supporting-field terms and 17
reviewed duplicates. All 38 formerly unselected classes are now live;
the full 1,546-row release delta and 153-row active review were parsed.
All 12,617 pinned METPO triples were checked for autophagy, xenophagy,
pexophagy and the proposed block, with no match. These checks establish
local novelty, not exhaustion of microbial traits.

## Scope and Hierarchy

| Scope | New Classes | Parent |
| --- | ---: | --- |
| A: synthetic trait | 1 | METPO:1000059 phenotype |
| B: predicates | 0 | Not applicable |
| C: schema enums | 0 | Not applicable |

This is the microbial cell's catabolic phenotype, not a gene, source
feature or animal host response. Delivery and degradation are required;
formation markers alone do not demonstrate the endpoint. The definition
does not impose a universal stimulus, route, cargo or protein inventory.

The issuing GO:0006914 record was directly resolved through
https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0006914.
Its biological-process scope includes self and intracellular non-self
material, but is not equivalent to an organismal phenotype. No exact
xref, synonym or SSSOM mapping is asserted.

Structured live label/definition/synonym review distinguishes uptake,
particulate feeding, extracellular proteolysis, secretion, gas vesicles
and phage-defense cell death. Endocytosis already excludes autophagy
alone from uptake evidence. The endosymbiosis research mention concerns
animal bacteriocytes, not an exact microbial phenotype node. No existing
YAML needs reparenting or same-scope grounding repair, and no organismal
disjointness is asserted. Ordinary phagolysosomal digestion alone does
not establish autophagy. Additional ignored-and-hidden self-digestion,
recycling and autolysis searches found cell-wall hydrolase and remodeling
contexts, not equivalent lysosomal/vacuolar catabolic phenotypes.

## Evidence and Limits

Four primary scientific abstracts were directly read; their short,
contiguous quotes independently exact-match the retrieved text and all
return VERIFIED from the maintained resolver:

| DOI | PMID | Quote Words | Role |
| --- | --- | ---: | --- |
| 10.1083/jcb.119.2.301 | 1400575 | 21 | Yeast vacuolar catabolism; definition authority |
| 10.1242/jcs.108.1.25 | 7738102 | 19 | Distinct routes and selective organelle turnover |
| 10.1073/pnas.0813319106 | 19667176 | 21 | Qualified amoeba infection perturbation |
| 10.1371/journal.ppat.1006344 | 28414774 | 17 | Flux-versus-formation boundary |

Europe PMC XML or core metadata supplied the scientific abstracts;
publisher HTML independently supplied the 1995 and 2017 abstracts.
The 1992 XML body is sparse. The 1995 full text requires access, and
2009 full-text attempts failed. No unread methods or figures from those
papers are presented as inspected. The 2009 abstract combines amoeba and
nematode results; its animal-lifespan and insulin claims are not assigned
to the amoeba, and perturbation alone is not direct degradative flux.

For 2017, the flux Results, flux-assay Methods and Discussion were read,
and actual Figure 6 and supplemental S6 Figure were inspected. The
reported infection-associated flux reduction is partial. This paper's
Author summary is distinct from the quoted scientific Abstract. Other
actual figures and supplements were not visually audited.

Qualified evidence, access limits and two OPEN discussions remain in the
record. No canonical examples, taxon IDs, protein accessions or causal
graph are added without independently checked provenance and functional
grounding. PROPOSED status requires human curation; neither automated
snippet matching nor structural validation supplies that signoff.

## ID Space and Files

Reserve `METPO:1059100` in the free 1059100-1059199 block, following v513.
Local ID: `traitmech:000638`; subset: `metpo_traitmech_2026_10`.
No collision with CommunityMech proposals was found, including ignored
files. The upstream Knowledge-Graph-Hub/kg-microbe contract remains at
`1408e7099d039026d7611c240938d8e177753406`; its class template has 11
columns. The property template is irrelevant to this class-only cohort.
Use the pinned ontology's w3id namespace, not the legacy purl example.
Definition provenance cites the local codex minting record and the four
DOIs; their distinct evidentiary roles are retained above.

| Artifact | Rows |
| --- | ---: |
| metpo_proposal_classes_robot.tsv | 1 |
| property template | Omitted |
| SSSOM mappings | Omitted |

## Verification

The guarded writer dry run, all 19 focused tests and all four maintained
snippet checks passed. Tests cover scope, access limits, parent
projection, dry-run immutability, exact replay, target/proposal drift
refusal and validation-before-write.

Local validation passed: LinkML, strict validation of all 1,033 records,
`just qc`, `just validate-history`, `just validate-products`, proposal
verification and cross-cohort coverage, ROBOT/ELK, Ruff and the full test
suite (2,458 passed, two dependency warnings, 613.23 seconds). The 45
focused dashboard/README/priority tests passed separately. All four
snippet resolver rows are VERIFIED at 1.00. Canonical-example shape and
research-artifact audits passed; the local shape audit did not resolve
NCBI taxonomy, and no new canonical example was added.

Parsed OWL has 15 class-template, 12,628 merged and 12,632 reasoned
triples, with the labeled w3id parent and expected hierarchy. The
11-column headers exactly match the pinned upstream template. Ordinary
whitespace checking flags its three required directive-header trailing
tabs; the documented exception is scoped to that exact TSV only.

All 1,032 old trait YAMLs are byte-identical. Among old trait pages,
1,031 change only in their corpus footer; phenotype adds the new child
(142 to 143). The priority parent-child delta is likewise isolated.
Discussion templates/navigation and the protected record are unchanged.
The QC dashboard reports 1,033 records and zero FAIL slots; discussion
data has 568 discussions across 504 records. Desktop/mobile browser
checks and screenshot review passed for identifier provenance, all four
quotes, access limits, OPEN discussions, hierarchy navigation, loaded
dashboard imagery and absence of overflow. Neither configured embedding
source is present, so embedding artifacts were not regenerated.

Exact-head PR review, CI and native queue results will be recorded on
the PR. No independent approval is claimed here.

## Upstream and Round Trip

Submit the cohort for METPO review after TraitMech signoff. When upstream
accepts the term, refresh the ontology, migrate the identifier and local
references to the accepted METPO ID, preserve minting provenance and
append-only history, and regenerate without a duplicate primary record.
The two scope/flux and exemplar/mechanism discussions remain OPEN.

## Change Log

- v514, 2026-10-06: propose microbial autophagy with four DOI-backed
  snippets and explicit separation of catabolic flux from marker abundance.
