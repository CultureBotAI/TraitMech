# ER-phagy: METPO Proposal v518

> Parent scope correction (2026-10-06, #1754): use v519's corrected
> `METPO:1059100` autophagy context when combining proposals. This cohort's
> TSV remains unchanged; its ER-phagy row and allocation are unaffected.

## Context

Add `traitmech:000642 ER-phagy`, a PROPOSED PHYSIOLOGY class, on base
`f6bb23c85ecc8d79e1ec3be3ca4f2201c1b9e987`. This is selective degradation
of portions of a microbial cell's endoplasmic reticulum through lysosomal
or vacuolar delivery, not a gene inventory, an ER-stress marker or mere uptake.

Whole-repository novelty searches included ignored and hidden files,
ER-phagy/reticulophagy and ER-degradation/autophagy variants, the three
DOI/PMID bundles, PMC identifiers, GO:0061709, the local identifier and the
prospective 1059500-1059599 block. CommunityMech proposals were included.
No exact record, synonym, causal node or earlier reservation requires repair.
Mitophagy's ER-turnover mention is an experimental cargo-selectivity control,
not an ER-phagy record or unresolved exact causal node.
All-state GitHub searches found one TraitMech ER-phagy hit: the #1751 landing
receipt listing this research lead, not a trait proposal. TraitMech
reticulophagy, upstream ER-phagy/reticulophagy and 1059500 searches returned
zero hits, with no incomplete-results flags.

The pre-addition corpus contained 1,036 records. A fresh 399-record seed
shares 344 identifiers; the 55 absent terms are 38 supporting-field terms
and 17 reviewed duplicates. All 38 formerly unselected classes are live.
The complete 1,546-row release delta, 153-row active review and 12,617
pinned METPO triples contain no candidate or prospective-block hit.
This establishes local novelty, not exhaustion of microbial traits.

## Scope and Hierarchy

| Scope | New Classes | Parent |
| --- | ---: | --- |
| A: synthetic trait | 1 | traitmech:000638 autophagy / METPO:1059100 |
| B: predicates | 0 | Not applicable |
| C: schema enums | 0 | Not applicable |

Selective ER degradation narrows autophagy. Mitophagy, pexophagy and
ribophagy are cargo-specific siblings, not parents. Extracellular
proteolysis, ER stress, the unfolded-protein response and ER-associated
protein degradation outside lysosomes/vacuoles are not equivalent traits.
Bulk turnover or accumulated ER whorls alone does not show selective flux.

Schuck et al. 2014 and Schafer et al. (online 2019, issue 2020) support
microautophagic ER turnover; the latter explicitly includes macro and micro
routes. Mochida et al. 2015 restrict their use of autophagy to macroautophagy.
That source-specific convention is not transferred to the whole phenotype.
Atg39's perinuclear/nuclear cargo can overlap nucleophagy without making
nucleophagy and ER-phagy synonyms. No universal stress trigger, receptor,
core-ATG requirement or macro/micro proportion is asserted.

Issuing [GO:0061709](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0061709)
is nonobsolete and lists ER-phagy as an exact synonym of reticulophagy.
Its definition specifies autophagosomes and denotes a biological process.
Both that route restriction and the process-to-phenotype shift prevent an
exact mapping here. The source-attributed mismatch remains an OPEN discussion;
no xrefs, synonyms or SSSOM mapping are asserted.

The TSV repeats the complete unchanged v514 autophagy row as dependency
context, not a new allocation. The writer guards the parent's eight
identity/scope fields and complete v514 template. Existing trait YAMLs and
v514 are not edited. Deduplicate the identical parent row when combining
cohorts upstream. Standalone ancestry is autophagy -> phenotype -> quality.

## Evidence and Limits

| DOI | PMID | Quote Words | Role |
| --- | --- | ---: | --- |
| 10.1242/jcs.154716 | 25052096 | 21 | Selective microautophagic ER degradation |
| 10.1038/nature14506 | 26040717 | 16 | Receptor-associated macroautophagic ER subdomains |
| 10.15252/embj.2019102586 | 31802527 | 14 | Route-inclusive definition and pathway distinctions |

All snippets were copied from directly retrieved Europe PMC scientific
abstracts with matching DOIs, not search-index text. The 2014 XML Results
s2c/s2e and Methods s4b/s4f were read. ER-targeted Pho8 reporters, cargo
comparisons and protease/Atg7 controls support selectivity and delivery.
DTT/tunicamycin impair vacuolar proteolysis, so accumulated whorls alone are
not a completed-degradation readout. Untreated opi1 cells have partially
disintegrated vacuolar whorls compared with the protease-deficient controls;
ER expansion can elicit the response without folding stress. Figure 5/7
captions were read, but actual figures and supplements were not inspected.
The W303 lineage is stated in Methods; natural provenance is unverified.

The 2015 paper was read as a scientific abstract only. Its Atg39/Atg40
assignments are source-specific, and its mammalian FAM134B counterpart
claim is qualified as probable. Full text, figures, supplements and strain
provenance were not inspected.

The ESCRT paper's XML Results sec-0005 and Methods sec-0011/sec-0018/sec-0019
were read. Macro/micro contributions are condition-dependent. ESCRTs also
affect nonselective autophagy and vacuolar function, so their disruption is
not a route-specific absence test. Atg40 is dispensable for the
Atg7-independent micro route. Pho8 background correction and
Pep4-dependent/Atg7-independent Sec63-GFP cleavage matter to interpretation.
Actual figures, supplements, full Methods and strain provenance were not
inspected. No panel-level or numerical experimental claim is curated.

No canonical examples or causal graph are added without natural-strain
provenance or native taxon-paired protein evidence. Two OPEN discussions
preserve these gaps and the route/flux boundary. The phenotype belongs to
the yeast doing the degradation, not a microbe eliciting an animal response.
PROPOSED status requires human signoff, not merely passing source matching.

## ID Space and Files

Reserve `METPO:1059500` in the fresh 1059500-1059599 block following v517;
local identifier `traitmech:000642`, subset `metpo_traitmech_2026_10`.
Parent `METPO:1059100` remains v514's allocation. Ignored-and-hidden checks
found no block collision, including CommunityMech proposals. The upstream
kg-microbe contract is pinned to `1408e7099d039026d7611c240938d8e177753406`;
its 11-column class headers are preserved. Use w3id METPO IRIs.

| Artifact | Rows |
| --- | ---: |
| metpo_proposal_classes_robot.tsv | 1 new class + 1 unchanged parent-context class |
| property template | Omitted |
| SSSOM mappings | Omitted |

## Verification

The guarded writer dry run and 22 controlled-fixture tests pass. Live snippet
verification reports three VERIFIED rows; direct abstract matching is checked
separately from the resolver. LinkML/strict validation, history, `just qc`,
Ruff and staged PR sanity pass. `validate-products` first failed because the
sandbox denied PATO/RO cache access; the rerun with cache access passed.
ROBOT/ELK and parsed RDF checks pass: classes/merged/reasoned have
25/12,638/12,642 triples and the expected labeled w3id ancestry.

All 1,036 prior YAMLs, v514 and shared discussion templates are unchanged.
The 1,035 unaffected old page bodies only change in the footer; autophagy
gains the child link. Its child count changes 3 -> 4 and its priority action
changes from BUILD_CAUSAL_GRAPH to CURATE_ROOT_WITH_SUBTYPES, as required by
the configured four-child threshold. No production code or test was changed
to suppress that expected classification. The live corpus contains 1,037
records, 522 PROPOSED, 156 PHYSIOLOGY, and 576 discussions across 508 records.
Both exact configured embedding sources are absent, so embeddings were not
regenerated. Playwright checks and actual screenshot inspection pass at
1440/390 pixels for identity, three quotes, two OPEN discussions, hierarchy
navigation, dashboard counts, loaded coverage image and no horizontal overflow.

The initial artifact tests found the draft's stale README prose count (#1752):
109 instead of 110 proposed physiology records. It is fixed without weakening
the test; all four README artifact tests pass afterward. The other 44 focused
artifact tests passed on the initial run. The ordinary staged whitespace check
flags only the required trailing empty ROBOT header cells; after inspecting
their widths/directives, exact-TSV scoped checks pass. The full suite passed
2,561 tests with two dependency warnings in 668.24 seconds after the README
fix. Committed-history, exact-head CI, independent-review availability,
native-queue and landing receipts are recorded on the PR separately.

## Upstream and Round Trip

Submit the new class and unchanged autophagy dependency for METPO review.
After acceptance, refresh the ontology, migrate identifiers and parent links
to accepted METPO IDs, retain minting provenance and append-only history,
and regenerate without duplicate primary records. Scope and exemplar/mechanism
discussions remain OPEN until their separate questions are resolved.

## Change Log

- v518, 2026-10-06: propose route-inclusive microbial ER-phagy with three
  DOI-backed snippets, selectivity/flux limits and unchanged parent context.
