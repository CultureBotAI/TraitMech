# Lipophagy: METPO Proposal v520

## Context

Add `traitmech:000644 lipophagy`, a PROPOSED PHYSIOLOGY class, on base
`9da924e26bd33778eafd859be3872ff996b901a4`. This is microbial autophagic
lipid-droplet degradation, not a sequence feature, lipid-storage structure,
gene inventory or uptake-only observation.

Whole-tree novelty searches included ignored and hidden files, CommunityMech
proposals, lipophagy and micro/macro spelling variants, lipid-droplet
turnover/degradation/autophagy, all three DOI/PMID bundles and available PMC
IDs, GO:0061724/0140504, local identifier and the complete 1059700-1059799
block. An initially unbounded numeric search matched unrelated D3/IDNA
constants, not allocations; CURIE/IRI-bounded checks found no collision.
A multiline broader lipid-droplet search found PHA-granule and pink-pigment
research boundaries, not an exact degradation node or unresolved synonym.
The PHA report explicitly separates droplets from PHA inclusions; the pigment
report defers an unsupported sequestration edge. Neither is an exact trait.

The structured live review found `traitmech:000190 lipolysis`, which concerns
triacylglycerol hydrolysis rather than autophagic organelle delivery. Its
definition, evidence and open xref discussion remain unchanged. All-state
GitHub searches found only #1755's research lead locally, and no lipophagy
or proposed-ID hit upstream; results were not marked incomplete.

Before addition, the live corpus had 1,038 records. A fresh 399-record seed
shares 344 identifiers; 55 absent terms are 38 supporting-field terms and
17 previously reviewed duplicates. All 38 formerly unselected classes are
already live. The complete 1,546-row release delta, 153-row active review
and 12,617-triple pinned METPO graph contain no candidate or prospective
block hit. These establish novelty for this candidate, not exhaustion.

## Scope and Hierarchy

| Scope | New Classes | Parent |
| --- | ---: | --- |
| A: synthetic trait | 1 | traitmech:000638 autophagy / METPO:1059100 |
| B: predicates | 0 | Not applicable |
| C: schema enums | 0 | Not applicable |

Lipid-droplet cargo narrows the existing autophagy phenotype. The definition
retains completed degradation through lysosomal/vacuolar delivery, without
imposing a universal route, selectivity mechanism, starvation trigger or ATG
inventory. A droplet's presence or formation does not establish its turnover.
Lipolysis can overlap this phenotype but is not an exact synonym or a required
broader parent for all droplet cargo. Cargo-specific autophagy siblings and
shared contact machinery do not make the traits equivalent.

The 2014 study supports a microautophagy-like catabolic route. The 2024 papers
also use lipophagy operationally for uptake. Their wording is attributed,
not silently equated with the present degradative endpoint. Current,
nonobsolete [GO:0061724](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0061724)
instead restricts lipophagy to selective macroautophagy, while
[GO:0140504](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0140504)
separately denotes microlipophagy. Both were resolved directly at QuickGO.
These process classes are not exact organismal-phenotype equivalents; the
source/GO scope difference remains an OPEN discussion. No exact synonyms,
xrefs or SSSOM mappings are asserted.

## Evidence and Limits

| DOI | PMID | Quote Words | Role |
| --- | --- | ---: | --- |
| 10.1091/mbc.e13-08-0448 | 24258026 | 15 | Vacuolar droplet turnover and definition |
| 10.1016/j.devcel.2024.01.014 | 38354739 | 21 | Contact-dependent uptake and terminology boundary |
| 10.1080/15548627.2024.2325297 | 38425021 | 18 | Protein-marker independence and condition-specific dependence |

All three snippets exactly match directly retrieved scientific text with
matching DOIs. The live resolver reports **two VERIFIED, one NOT_IN_ABSTRACT**.
The third verdict is retained: Europe PMC and PubMed abstract fields return
only abbreviations, whereas directly retrieved NCBI PMC XML contains the
scientific ABSTRACT paragraph. Manual exact-substring and section checks
confirm that quote; a successful resolver exit does not make it VERIFIED.
That XML contains no body, so retrieving it did not establish full-text access.

For the 2014 source, scientific XML abstract2 is distinct from the precis.
Results sec9 and Methods sec12-sec15 were read. Uptake, lipid breakdown and
surface-protein processing are distinguished, with cytosolic compensation
and BY4742-derived assay-host limits retained. Actual figures and supplements
were not inspected. The 2024 contact study was read as a scientific abstract;
full Methods and figures were not read. No quantitative panel-level claim is
curated. Canonical examples and protein graphs remain unset pending independent
natural-strain and native accession evidence. Two OPEN discussions preserve
the outstanding scope and mechanism questions.

## Relationship to v519

The v520 TSV copies v519's corrected `METPO:1059100` parent context unchanged.
This is dependency context, not a new parent allocation or definition repair.
The autophagy YAML and all historical proposal TSVs remain unchanged. Do not
reintroduce v514-v518's superseded cytoplasmic-only wording when combining
cohorts; v519 already documented that correction under #1754.

The writer guards the complete current parent record and full v519 template,
defaults to a dry run, refuses target/proposal drift, and validates before
production writes. It never writes the parent or historical template. Tests
use separate controlled fixtures without weakening production preimage guards.

## ID Space and Files

Reserve `METPO:1059700` in fresh 1059700-1059799, following v519.
The local identifier is `traitmech:000644`; subset `metpo_traitmech_2026_10`.
The upstream kg-microbe contract and canonical templates were freshly retrieved
at `1408e7099d039026d7611c240938d8e177753406`: class headers have 11 columns,
canonical properties have 13. CommunityMech v1's three reference files were
read end-to-end. No candidate/block collision was found in ignored/hidden
local, CommunityMech or upstream checks. METPO IRIs use w3id.

| Artifact | Rows |
| --- | ---: |
| metpo_proposal_classes_robot.tsv | 1 new class + 1 unchanged parent-context class |
| property template | Omitted |
| SSSOM mappings | Omitted |

## Verification

The guarded writer dry run and 43 controlled-fixture tests pass. Tests cover
identity, endpoint/scope limits, replay, parent/template/target drift refusal,
parent preservation and validation-before-write. Source matching and resolver
verdicts are described above. The live corpus has 1,039 unique records,
524 PROPOSED, 158 PHYSIOLOGY, and 580 discussions across 510 records.
Direct LinkML/strict validation, proposal verification, ROBOT/ELK and history
validation pass. Parsed RDF counts are 25 class-template triples, 12,638 merged
triples and 12,642 reasoned triples; the w3id child-parent-phenotype-quality
hierarchy and the single corrected parent definition were checked explicitly.

The artifact audit confirms that all 1,038 existing YAML records, all 524
historical proposal TSVs and their narratives remain unchanged. Of the existing
trait pages, 1,037 change only in their corpus footer; the autophagy page also
gains the new child. Its priority child count changes from five to six, with no
other existing priority-row delta. Shared discussion templates and the
protected spore-germination record remain unchanged.

Playwright checks at 1,440 and 390 pixels pass for identity, three quotes,
two OPEN discussions, source-access limits, parent navigation and the 1,039-record
dashboard with its coverage image loaded. Actual desktop/mobile screenshots
were inspected; no overflow or page errors were found. Embeddings were not
regenerated because both configured source paths are absent.

`just validate-products`, `just qc`, Ruff and the full suite pass: **2,640
tests passed in 622.85 seconds**, with two dependency deprecation warnings.
Staged PR sanity passes. Ordinary whitespace checking flags only the three
required trailing empty ROBOT directive cells; canonical header widths and
exact-path scoped whitespace checks pass. Committed-history, exact-head review,
CI and landing outcomes will be recorded on the PR after verification. No
frozen baseline is changed to accept this record.

## Upstream and Round Trip

Submit the new child with the unchanged corrected parent context and the
source-scope discussion. After upstream acceptance, refresh METPO, migrate
the local identity and parent links to accepted IDs, preserve history and
regenerate without creating duplicate records. Keep the independent OPEN
interpretation and exemplar/mechanism questions until separately resolved.

## Change Log

- v520, 2026-10-06: propose microbial lipid-droplet autophagy with three
  source-matched snippets and explicit route, endpoint and resolver limits.
