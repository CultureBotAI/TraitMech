# Adversarial review of enhanced transcriptional reactivation memory

- Review: 20261013T010510Z-transcriptional-reactivation-memory
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-13T00:53:02Z
- Finished UTC: 2026-10-13T01:05:10Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The new endpoint-qualified record is supported with explicit assay and historical-identity limits. The identified attribution defect is corrected by an immutable successor, tracked in #1902. No remaining actionable defect was identified in the assessed change set; external review and merge gates remain separate.

## Scope And Provenance

Complete new record and maintained/generated change set, not whole-corpus scientific review.

Selection: One exact newly curated trait; no sampling.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 04ef8ed05cfd2ca2e7f13d87fd2633e269a84eac.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| traitmech:000713 | data/traits/physiology/enhanced_transcriptional_reactivation_memory.yaml | maintained | enhanced transcriptional reactivation memory |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python -m pytest -q tests/test_add_transcriptional_reactivation_memory_trait.py tests/test_readme_artifacts.py tests/test_trait_priority.py tests/test_qc_dashboard_artifacts.py | passed | True | traitmech:000713 | Writer, README, priority and QC-dashboard tests passed, including drift refusal, prevalidation without writes, replay, copy isolation and source/proposal consistency. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate -s src/traitmech/schema/traitmech.yaml --target-class TraitRecord data/traits/physiology/enhanced_transcriptional_reactivation_memory.yaml | passed | True | traitmech:000713 | Executed native gate passed; corpus diagnostics are not whole-corpus scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/validate_strict.py data/traits/physiology/enhanced_transcriptional_reactivation_memory.yaml | passed | True | traitmech:000713 | Executed native gate passed; corpus diagnostics are not whole-corpus scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/verify_snippets.py --record data/traits/physiology/enhanced_transcriptional_reactivation_memory.yaml --out /tmp/traitmech-transcriptional-memory-checks-20261013/snippet-results.tsv | passed | True | traitmech:000713 | Actual final-record verifier checked two DOI references: both NOT_IN_ABSTRACT. Separate exact contiguous full-text matches support the Results quotations; neither is mislabeled native VERIFIED. |
| just audit-proposals | passed | True | traitmech:000713 | Executed native gate passed; corpus diagnostics are not whole-corpus scientific review. |
| just ground-predicates | passed | True | traitmech:000713 | Executed native gate passed; corpus diagnostics are not whole-corpus scientific review. |
| just ground-nodes | passed | True | traitmech:000713 | Executed native gate passed; corpus diagnostics are not whole-corpus scientific review. |
| just audit-graphs | passed | True | traitmech:000713 | Executed native gate passed; corpus diagnostics are not whole-corpus scientific review. |
| just audit-graph-protein-taxa | passed | True | traitmech:000713 | Executed native gate passed; corpus diagnostics are not whole-corpus scientific review. |
| just audit-predicate-domains | passed | True | traitmech:000713 | Executed native gate passed; corpus diagnostics are not whole-corpus scientific review. |
| just check-biolink-coverage | passed | True | traitmech:000713 | Executed native gate passed; corpus diagnostics are not whole-corpus scientific review. |
| just audit-snippets | passed | True | traitmech:000713 | Executed native gate passed; corpus diagnostics are not whole-corpus scientific review. |
| just gen-discussions-data | passed | True | traitmech:000713 | Executed native gate passed; corpus diagnostics are not whole-corpus scientific review. |
| just gen-qc-dashboard | passed | True | traitmech:000713 | Executed native gate passed; corpus diagnostics are not whole-corpus scientific review. |
| just gen-pages | passed | True | traitmech:000713 | Executed native gate passed; corpus diagnostics are not whole-corpus scientific review. |
| just gen-priority-dashboard | passed | True | traitmech:000713 | Executed native gate passed; corpus diagnostics are not whole-corpus scientific review. |
| just qc | passed | True | traitmech:000713 | Executed native gate passed; corpus diagnostics are not whole-corpus scientific review. |
| just validate-history | passed | True | traitmech:000713 | Executed native gate passed; corpus diagnostics are not whole-corpus scientific review. |
| just validate-products | passed | True | traitmech:000713 | Executed native gate passed; corpus diagnostics are not whole-corpus scientific review. |
| just verify-proposal metpo_traitmech_v589 | passed | True | traitmech:000713 | Executed native gate passed; corpus diagnostics are not whole-corpus scientific review. |
| just robot-validate-proposal metpo_traitmech_v589 | passed | True | traitmech:000713 | Executed native gate passed; corpus diagnostics are not whole-corpus scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/ruff check src scripts tests | passed | True | traitmech:000713 | Executed native gate passed; corpus diagnostics are not whole-corpus scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python -m pytest -q --junitxml=/tmp/traitmech-transcriptional-memory-checks-20261013/pytest.xml | passed | True | traitmech:000713 | 4336 full-suite tests passed without skips, failures or errors. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/validate_history_links.py history/records/enhanced_transcriptional_reactivation_memory | passed | True | traitmech:000713 | Executed native gate passed; corpus diagnostics are not whole-corpus scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate --schema src/traitmech/schema/history.yaml --target-class HistoryRecord history/records/enhanced_transcriptional_reactivation_memory/2026-10-13T003746Z-claude-code-cf0b17.yaml | passed | True | traitmech:000713 | Executed native gate passed; corpus diagnostics are not whole-corpus scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate --schema src/traitmech/schema/history.yaml --target-class HistoryRecord history/records/enhanced_transcriptional_reactivation_memory/2026-10-13T003824Z-codex-8495dc.yaml | passed | True | traitmech:000713 | Executed native gate passed; corpus diagnostics are not whole-corpus scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/audit_canonical_examples.py --no-resolve | passed | True | traitmech:000713 | Existing canonical examples passed offline shape checks. --no-resolve does not verify remote taxon identity; this addition contains no canonical taxa. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/run_trait_graph_audit.py --verify | passed | True | traitmech:000713 | Executed native gate passed; corpus diagnostics are not whole-corpus scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/audit_history_records.py --base 62f45e1749fa3d3e5ca8b9a3a4ba5bb0361beb8b | passed | True | traitmech:000713 | Executed native gate passed; corpus diagnostics are not whole-corpus scientific review. |
| git diff --check 62f45e1749fa3d3e5ca8b9a3a4ba5bb0361beb8b HEAD -- . ':(exclude)proposals/metpo_traitmech_v589/metpo_proposal_classes_robot.tsv' | passed | True | traitmech:000713 | Executed native gate passed; corpus diagnostics are not whole-corpus scientific review. |
| git -c core.whitespace=-blank-at-eol diff --check 62f45e1749fa3d3e5ca8b9a3a4ba5bb0361beb8b HEAD -- proposals/metpo_traitmech_v589/metpo_proposal_classes_robot.tsv | passed | True | traitmech:000713 | Executed native gate passed; corpus diagnostics are not whole-corpus scientific review. |
| Rendered desktop/mobile products | passed | True | traitmech:000713 | 1440/390 px assertions passed: two quotes, three discussions, two history links including the attribution correction, local identity, hierarchy/browse navigation, dashboard count and loaded coverage image. Eight screenshots visually inspected; no horizontal overflow or page errors. |
| Pinned generator and embedding applicability | passed | True | traitmech:000713 | 152 pinned generator source blobs verified. Neither exact configured embedding source exists in primary/owned layouts; existing embedding bytes retained. |

## Scientific And Domain Assessments

### Enhanced transcript reactivation after repression

identity: supported. Targets: traitmech:000713.

The definition denotes an assayable physiological history effect, not a sequence feature, chromatin mark or persistent reporter. It is not equivalent to retained resistance or the full growth/induction scope of carbon-source memory.

### Ordinary versus synthetic induction and causal scope

evidence: supported. Targets: traitmech:000713.

Sump Figure 1D supports synthetic Opi1 Anchor-Away enhancement; Figure 1B does not establish clearly faster ordinary-starvation reactivation. Mutant defects alone do not establish a within-wild-type enhancement. mRNA kinetics, localization, fitness and chromatin inheritance are not interchanged.

### Measured recovery versus cited multigeneration persistence

quantity: supported. Targets: traitmech:000713.

D'Urso Figure 7A uses two-hour recovery and selected transcripts. The four-generation/gene-count sentence attributes Guan 2012, not a new measurement in that panel. Sump 18-hour localization is not an 18-hour enhanced-transcription assay. No universal duration is defined.

### Full-text snippets and source discrepancies

provenance: supported. Targets: traitmech:000713.

Two exact contiguous Results snippets support the qualified interpretation; native NOT_IN_ABSTRACT is retained. Selected version agreement does not erase the D'Urso panel-caption mismatch, Sump supplement locator or strain-description ambiguities. No independent-laboratory replication is claimed.

### Conservative parent and independent acceptance

grounding: supported. Targets: traitmech:000713.

The active phenotype parent is strictly broader. Original historical definitions remain unavailable; labels do not prove historical nonequivalence. The operational new phenotype is accepted from positive evidence without reusing or exactly mapping deprecated IDs.

### Append-only attribution correction

provenance: supported. Targets: traitmech:000713.

Codex is the correct record curator and creator. The accidental default name is explicitly corrected without deleting or rewriting the original. Both target-linked entries render, and the scoped skill change has separate correctly attributed history.

### Guarded ownership, proposal and generated products

consistency: supported. Targets: traitmech:000713.

Drift refusal, prevalidation, replay, schema/strict/QC gates, full tests, proposal RDF and responsive views pass. Only one trait is added; existing scientific records, review bundles and baselines are unchanged.

### Unasserted mechanisms and natural exemplars

completeness: unknown. Targets: traitmech:000713.

Natural strain provenance, universal molecular mechanisms, original deprecated-term semantics and some source discrepancies remain unresolved. No graph, canonical taxon or exact synonym pretends to close those optional extensions.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| source-0 | DOI:10.7554/eLife.77646; Results s2-1; selected Methods and actual figure panels qualified in notes. | supports | Sump et al. 2022, PMID:35579426, PMC9129879; Results s2-1, paragraph 2, contiguous in primary XML and publisher Version of Record HTML. Figure 1D uses synthetic Opi1 Anchor Away to bypass upstream induction control; enhancement is lost in mrs and nup100 mutants. Ordinary-starvation INO1 reactivation in Figure 1B is not clearly faster than activation. Figure 1 supplement 1C separately measures CHO1/ACT1 after three-hour repression; its generic statistical-comparator caption is ambiguous. Figure 1 supplement 2E measures 18-hour peripheral localization, not that duration of enhanced transcription; the main Results mispoints to supplement 1. Figure 1G competitive fitness is a different endpoint, not proof of transcriptional causality. Selected Results, Methods, scientific abstract, actual figures and strain-table rows were inspected. RT-qPCR mRNA kinetics are not direct measurements of initiation rate. Native abstract lookup returns NOT_IN_ABSTRACT; direct full-text matching supports the quotation, not a native VERIFIED verdict. |
| source-1 | DOI:10.7554/eLife.16691; Results s2-7; selected Methods and actual figure panels qualified in notes. | supports | D'Urso et al. 2016, PMID:27336723, PMC4951200; Results s2-7, paragraph 1, contiguous in primary XML and publisher Version of Record HTML. This sentence attributes the gene count and duration to Guan 2012; Figure 7A directly tests selected mRNA responses after 0.7 M NaCl for one hour, two-hour rich-medium recovery, then 0.5 mM H2O2. PGM2, PMT5 and YGP1 differ from the HSP31 control. Four-generation persistence is not measured in that panel. Actual Figure 7B is wild-type ChIP, C mutant ChIP, D mutant mRNA and E Ssn3 ChIP; caption B/C/D assignments conflict with the image. INO1 mutant reactivation defects in Figure 1E/F alone do not establish faster within-wild-type reactivation. Relevant Results, Methods, abstract and actual figures were inspected; raw data were not reanalyzed. Native abstract lookup returns NOT_IN_ABSTRACT, with the selected quotation independently matched in full text. |
| content | data/traits/physiology/enhanced_transcriptional_reactivation_memory.yaml; Complete record, guarded writer/tests, proposal, sidecar, history, skill and generated products. | supports | One qualified physiological CLASS, two DOI sources and full-text Results snippets; no canonical examples, causal graph, exact synonym or equivalence xref. Status remains PROPOSED. |
| novelty | research/traits/physiology/enhanced_transcriptional_reactivation_memory-source-verification.json; Bounded novelty, allocation and prepublication receipts. | supports | Ignored/hidden available files, 18 retained historical trees, nine independent copies, 1122 distinct normalized trait versions, current upstream snapshots and 11 stable pending PRs yielded no exact active record or competing reservation in scope. The new owned root is the only reservation delta; coordinate and namespace-envelope hits were hash/context-adjudicated. |
| ontology | data/raw/metpo.owl; Pinned/current released RDF; active phenotype parent; deprecated 1000108 and 1000310. | supports | Phenotype is broader and active. Deprecated lexical neighbors have no replacement/consider in inspected graphs, but original historical definitions/parents remain unassessed and the OMO reason assignment is disputed in METPO#521. Positive experimental scope supports independent acceptance; no revival or historical equivalence claim. |
| products | reports/proposal_citation_audit.tsv; Native checks, parsed RDF, byte preservation and browser inspection. | supports | All 1107 prior trait YAMLs and prior histories/reviews/proposals/embeddings/templates are unchanged. Prior trait pages differ only in footer count except the phenotype child link. Proposal RDF checks: {'classes': 15, 'merged': 12628, 'reasoned': 12632}; 11-column template and trailing blank directive cells retained. |
| history | history/records/enhanced_transcriptional_reactivation_memory/2026-10-13T003824Z-codex-8495dc.yaml; Successor and immutable original 2026-10-13T003746Z-claude-code-cf0b17.yaml; issue #1902. | supports | Initial CREATE used the default actor name despite correct gpt-5/codex model/tool fields. The preserved successor explicitly identifies Codex as the actual actor and states no Claude execution. No history rewrite occurred; validation and rendered links include both entries. Issue closure remains contingent on merge. |

## Limits And Additional Notes

- Author self-review; PROPOSED status is retained and no human scientific sign-off is asserted.
- Two papers share a research lineage. Selected actual figures and Results/Methods were inspected, not full raw-data reanalysis. Limited-resolution figures and selected strain-table rows constrain numerical/provenance claims.
- Original historical definitions and parent axioms for deprecated lexical neighbors remain unassessed. Independent acceptance does not establish historical exact equivalence or nonequivalence.
- Publisher access challenges, caption/locator discrepancies and bounded notice checks remain explicit; no exhaustive correction/retraction absence claim.
- Searches include ignored/hidden available files but exclude unavailable historical ignored/untracked bytes, symlink directories, arbitrary archives, unchanged pending trees and deleted historical blobs. Discovery is not exhausted.
- Existing QC baselines and skipped remote taxonomy adapters retain their limitations. Configured embedding sources are unavailable; existing embedding bytes are preserved.
- Issue #1902 is fixed on this branch by an append-only successor, not closed merely by this review. GitHub review, exact-head CI, actual merge integrity, independent recovery and cleanup remain separate gates.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T010510Z-transcriptional-reactivation-memory
kind: record
repository: CultureBotAI/TraitMech
title: Adversarial review of enhanced transcriptional reactivation memory
started_at: '2026-10-13T00:53:02Z'
finished_at: '2026-10-13T01:05:10Z'
reviewer:
  identity: codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Author source-based adversarial assessment; not independent
    review or human scientific sign-off.
skill: .claude/skills/add-trait/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'The new endpoint-qualified record is supported with explicit assay and historical-identity
  limits. The identified attribution defect is corrected by an immutable successor,
  tracked in #1902. No remaining actionable defect was identified in the assessed
  change set; external review and merge gates remain separate.'
source:
  git_revision: 04ef8ed05cfd2ca2e7f13d87fd2633e269a84eac
  state: working_tree
  inputs:
  - path: .claude/skills/add-trait/SKILL.md
    sha256: 6fbcb8190118a0c13ca81a1a49dbb1c2fd1e1aa6c2fb817cf07c2682acc3c073
    role: context
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: da8896328a0fd6cc92f1adf0d8be8980d0ddd41f3172c7936f2c7f119b293ac1
    role: context
  - path: .claude/skills/manage-identifiers/SKILL.md
    sha256: a5c5aaa10943ee6d15423a5878ed2189e4e0b28a5c6e09fda80ba299ab779ebb
    role: context
  - path: .claude/skills/metpo-proposal/SKILL.md
    sha256: 03f008c011e6f0d45cafb7516a01a3383c0a7e8d11bfc5c9cb31efaeca51275f
    role: context
  - path: .claude/skills/metpo-proposal/reference/conventions.md
    sha256: 8f0fb0093a8fad591148a4a72fcac4be3b44d0a1b5e96be5207ba817d07d6cd0
    role: context
  - path: CLAUDE.md
    sha256: 4d328127022388e1affe9b71be24bc93944a971636d0d0ea902f6511e0b405c5
    role: context
  - path: DO_NOT_WORK.md
    sha256: 9ae0b05cc06f4ce8938801287a568d535e471d06dda5e258fcdbbed222abf712
    role: context
  - path: README.md
    sha256: 562b73b119fce0c739ae9e08b5bea2d67cd7eca89382975ad2527c9f97cc6244
    role: context
  - path: app/dashboard/priority.html
    sha256: 986832de856dacf57735527a8a83473bfc698c6402f7fa7f66983e19aa7a442d
    role: context
  - path: app/dashboard/priority.json
    sha256: c3a634f94cc51adf81b2088536e905a62b42ef5d540613232e9703295b0b1e9a
    role: context
  - path: app/discussions/data.js
    sha256: 233e47617af53f1af4ce461e9e921667f30e63824080a497374c85ea4336d6ba
    role: context
  - path: app/discussions/index.html
    sha256: f9c315ab6577de4ac4153205d0edf7237ad1ddce769bdd983997f6d332c7850d
    role: context
  - path: app/discussions/theme-toggle.js
    sha256: 8b34063c7251d55e81f74da73bf8ac872f294bfab96acd7095036c7764af4f72
    role: context
  - path: conf/evidence_snippet_baseline.tsv
    sha256: cbe5c82379e796446366b292f15194d80625b928119b482a67d857a379ab31a7
    role: context
  - path: conf/record_review.yaml
    sha256: 5adc6244761fb2baf8a059d81f23b0c9b32a33f9426ab84094234c3ec417269d
    role: context
  - path: conf/trait_priority.yaml
    sha256: ec041710b63331902ac2730fe2b0d8d2b2d28626933b56fe8441407b26b218d0
    role: context
  - path: dashboard/coverage.png
    sha256: cdb0efbb19f4aa6581938cc29c1b16b1a52217d346085971a6c664e4d00600da
    role: context
  - path: dashboard/index.html
    sha256: 64eeb083ad10d9070b576af447e01a7ad04994a1c13368007784924f462092a0
    role: context
  - path: data/raw/metpo.owl
    sha256: 8b6f8fe0510a698579e532658c8ace05da2550093365df9ca83feb0741778415
    role: context
  - path: data/traits/ecology/animal_pathogen.yaml
    sha256: 7399724615acb04a48033bc6834025456a494b05ff26b3a1803b28619feb9cd4
    role: context
  - path: data/traits/ecology/bacterial_cannibalism.yaml
    sha256: d3e755e4acffde487bca3a004a558ae3d853436a7e975bfbce24ce9cb03bb74c
    role: context
  - path: data/traits/ecology/bacterial_mycophagy.yaml
    sha256: 49cf32a3a6c9e4f7a10f201bdba9c87801bc959aa5a70b5035f2c694fb7e56be
    role: context
  - path: data/traits/ecology/biofilm_formation.yaml
    sha256: 8936e72d19f99bb3f7bb7ad47037a421a1e94d2d1ee3528ee77edcf57c237964
    role: context
  - path: data/traits/ecology/biosafety_level.yaml
    sha256: 11d1e21fa511aedf4e453875ed0c2508b35e82d0e24399e9aa4aa5547c5aa39a
    role: context
  - path: data/traits/ecology/biosafety_level_1.yaml
    sha256: 09a7b97fefc0d6258cedac392707458e254c1b88881352b90dcc443f2a347a9c
    role: context
  - path: data/traits/ecology/biosafety_level_2.yaml
    sha256: cc0fd06d66a12cda1f4d229d91fd7f9c0dd98c69d9d77e756cce8fdfccfb3a8b
    role: context
  - path: data/traits/ecology/biosafety_level_3.yaml
    sha256: 0a0c3454b5eeae41f0e9f6c6202a22df48104afd6324897209ce3d908a475744
    role: context
  - path: data/traits/ecology/biosafety_level_4.yaml
    sha256: f98209531d6bfdab7433313f85d5dddc9a4107a324f40664dcfe32695f80ebcd
    role: context
  - path: data/traits/ecology/biosafety_level_5.yaml
    sha256: f8db13d6c7fb599669e552716227497ddee211173daac5a36a3aab7d58d0d464
    role: context
  - path: data/traits/ecology/collective_bacterial_predation.yaml
    sha256: b5120d8a445ba78bf3e79097f3317b0d6a47a7d8b62b9a7d0395a02f6797a79c
    role: context
  - path: data/traits/ecology/commensalism.yaml
    sha256: 145d5d82edb69ec596fe6b1fd068ee6eb686cfd6da37f0aff22427fa8ce5907d
    role: context
  - path: data/traits/ecology/cytoplasmic_bacterial_predation.yaml
    sha256: 64466cbcc5f4d73b194706fbdb84ae03b992a85f0aa4db9e360e8b3f4ab5db3f
    role: context
  - path: data/traits/ecology/endophytic.yaml
    sha256: a71d78c4bde350bd7941f5e5e7340207d67ee1d86cfa7ee76bc7236c10221d6a
    role: context
  - path: data/traits/ecology/endosymbiosis.yaml
    sha256: e42e413a5d2a662aabbd7add9be674718bfc392a1bcc16f1d55fdb8d3c37cb91
    role: context
  - path: data/traits/ecology/epibiotic_bacterial_predation.yaml
    sha256: 0432b57c23aef7f0f322378c4ab3bc36afbe01f2b712357c998b099fd5fa4c40
    role: context
  - path: data/traits/ecology/epiphytic.yaml
    sha256: 98678827caa570a3f00e302059beadbb8b72dc2341c8eb5322621ead264ac4b1
    role: context
  - path: data/traits/ecology/free_living.yaml
    sha256: d42d23af7ac02e192ba7a8783aeb9f28335a818c35c552526361b29f2c0a8ea0
    role: context
  - path: data/traits/ecology/gut_associated.yaml
    sha256: 7ff3a740499c51e2f2e4855f56c0f084cc0aa7334d48cdc4eff309d90eb15586
    role: context
  - path: data/traits/ecology/habitat_association.yaml
    sha256: 623d18cf295c01782024055b4dca534217f52d3ef18d46f086af27fe504bbd2a
    role: context
  - path: data/traits/ecology/host_associated.yaml
    sha256: 8f39eb631802725d79cec85d1d80e0a2f24b2fb74940473bc39b32a2c57d6384
    role: context
  - path: data/traits/ecology/human_pathogen.yaml
    sha256: 104a578c4be34231855c6e1ec0e963f58eb89f52cc70152fe4b004ce80ceae43
    role: context
  - path: data/traits/ecology/ixotrophy.yaml
    sha256: 4aaf8f3c27db918f64a98f1396afb185aa06ff4c5545c0b6530e719aabb01d2a
    role: context
  - path: data/traits/ecology/mutualism.yaml
    sha256: 7247ae4be59ce2eb7f1cc9d7303e1a338af82cd49d255c60aa1442f6dc1c48a3
    role: context
  - path: data/traits/ecology/nitrogen_fixing_symbiosis.yaml
    sha256: d4d85f1d5e370d5862b086ae52a716dee3fc5f8880639bffa4e2dff65e9d1574
    role: context
  - path: data/traits/ecology/opportunistic_pathogen.yaml
    sha256: 9dde5e43eafc86ecd22089841463a8d6bfa703a8200a7179375217ed6dd03b52
    role: context
  - path: data/traits/ecology/parasitism.yaml
    sha256: 06714e9bc42a3405dc4700e41a0d6a92ae814c0122375a40b3ad776fda1a6040
    role: context
  - path: data/traits/ecology/pathogenic_to_host.yaml
    sha256: 6086ef781d3871684a8a21c77330be972673657b83b5fa0d4ba9c52e376ca451
    role: context
  - path: data/traits/ecology/periplasmic_bacterial_predation.yaml
    sha256: 0873b32839700055ff8116c72a92fc33a8a09ed20358eb19f3fbc7ed4e3d0569
    role: context
  - path: data/traits/ecology/plant_pathogen.yaml
    sha256: 4c8c4cf20790c060a91495e96a13656c7d7b72ef0856b0fbc2598ff53a99eb00
    role: context
  - path: data/traits/ecology/predatory_bacterium.yaml
    sha256: adcef1a0693a766270509b039ec3d47cb2daa2f94bede513ba82959967d7366d
    role: context
  - path: data/traits/ecology/rhizosphere_association.yaml
    sha256: 311fe0327d4b289718e9fcd0f2e287e119a8274a4293c591a24e654b548a88e7
    role: context
  - path: data/traits/ecology/saprotrophy.yaml
    sha256: 74c1e3065e0ce9dfc86b1b8725061383de4e8800dd5e7c02f48179c85fa3b6f4
    role: context
  - path: data/traits/ecology/soil_dwelling.yaml
    sha256: 9560bc7f560f9f97dab1ffe2cb930feda57eac65ed732215425b1c1f0d434515
    role: context
  - path: data/traits/ecology/symbiosis.yaml
    sha256: 86ad9516ff0879731da3792de1495ba1d0e107394edfcc754be03d052a677b21
    role: context
  - path: data/traits/environment/acidophilic.yaml
    sha256: 4170ebccedecf6a0d53cd984fc98feb9a670ab224f6b66774e937f9ebd93486b
    role: context
  - path: data/traits/environment/acidotolerant.yaml
    sha256: d1b7ecf1ebcf8f9502a82f7ec4fe21ba299fbf0d300a2e4e4575549e2ae540b7
    role: context
  - path: data/traits/environment/aerobic.yaml
    sha256: 5dc5609f2fe58c2bc0b7a95a38a5593fa48dfb71a16b92c683311d79d0005768
    role: context
  - path: data/traits/environment/aerotolerant.yaml
    sha256: 4ae40096583868e5ab9b31f8aec3a81a09938faf24391f57a6a34b32b2efb3a8
    role: context
  - path: data/traits/environment/alkalotolerant.yaml
    sha256: 54f2507b6a29cbfcfe4158addebc27aa973f605374c89e526dc267100577ac63
    role: context
  - path: data/traits/environment/alkaphilic.yaml
    sha256: 9dd8c1ed07700d7960f64e7539118441a563cd71fe78b22d39ee70b058b0fa65
    role: context
  - path: data/traits/environment/anaerobic.yaml
    sha256: bdee031c6277b96ab3f66dbdf1e6782aa21fd74e02676fd287d2f2e70ee6773f
    role: context
  - path: data/traits/environment/arsenic_tolerant.yaml
    sha256: b7c4c9ee1b352e7194421d11f8ed653d6ff01f58ea29bd934f069632071bb320
    role: context
  - path: data/traits/environment/cadmium_tolerant.yaml
    sha256: 219579b7eab2bfdb4787cb3f168f0492fbc5b951f69ffe70d1c6ffdb51683c5b
    role: context
  - path: data/traits/environment/capnophilic.yaml
    sha256: 8cfe3a2ee391c292bd27122711bc3ca3abd9a1f9f7f9d2d79fdfc2daa85d05e5
    role: context
  - path: data/traits/environment/cobalt_tolerant.yaml
    sha256: 7cf345edc60c113f1a805d1a51325710092c7f881a32e7dff59965c5336aefb0
    role: context
  - path: data/traits/environment/copper_tolerant.yaml
    sha256: 2eb94c78ccb7f7c953aa25088585cb9fb46f22b4e2425f924beb82f6caaba5fa
    role: context
  - path: data/traits/environment/delta_phenotype_with_numerical_limits.yaml
    sha256: 3b26342531eb0edef94e6434c2b91a2d066e02d23a9bef03c626767c5fc19171
    role: context
  - path: data/traits/environment/desiccation_tolerant.yaml
    sha256: e5044ef67c4cf892aafe03b7da222c267aea1fdeeb546c3d95f57c13d4122e97
    role: context
  - path: data/traits/environment/euryhaline.yaml
    sha256: c2eece3fd30e76e558eb334fd1cc69c6528069f3a0e5f4219f5959315f14e850
    role: context
  - path: data/traits/environment/extreme_hyperthermophilic.yaml
    sha256: 1ff49bc4ee848f90b6a7e2e1fe17b51fad9c7b952f6c6a7c2e3a433b3de0266c
    role: context
  - path: data/traits/environment/extremely_halophilic.yaml
    sha256: 15bf8267ffc4b393d3db1a13fa0738240dc94f5f017cce8322783f297f35d0f0
    role: context
  - path: data/traits/environment/facultative_oxygen_preference.yaml
    sha256: 146151a10541d48d38410435c282cd022bbafa9630e1f004771c6b85c18c3e6f
    role: context
  - path: data/traits/environment/facultative_psychrophilic.yaml
    sha256: 7db04c3bc2c9e2abd1f006d8f3e7c3d09fa71bf3d881c4a4e78835f583b43c09
    role: context
  - path: data/traits/environment/facultatively_acidophilic.yaml
    sha256: 4aa90a75dc3f89215ac24f6283b52396abf0c4ff36c2917f2e5280ef71225993
    role: context
  - path: data/traits/environment/facultatively_aerobic.yaml
    sha256: 8cbdf86a001a282796f1a651e19f5408020bb44104409b1b69920cd7f87ac2cb
    role: context
  - path: data/traits/environment/facultatively_alkaphilic.yaml
    sha256: 33b818c17dd5f8e21cec644f4a5d64f23e28c7f8b9b8d66ccfff7fad460bad2a
    role: context
  - path: data/traits/environment/facultatively_anaerobic.yaml
    sha256: 705d29c245efc54d1c2df91e2bf8e69ab9be31ec09bf19c60acddbcd6a895ccf
    role: context
  - path: data/traits/environment/growth_range_phenotype_with_numerical_limits.yaml
    sha256: ad223791fa379c8f7302c8334153dbbd157fbf9a015a902a6ebb92f5513bfd9b
    role: context
  - path: data/traits/environment/haloalkaliphilic.yaml
    sha256: 4bf7e5d0ff24b684c356a91a625dcb883db2e80a58874e4a625a2f3b0fb19e7e
    role: context
  - path: data/traits/environment/halophilic.yaml
    sha256: 68be1a6259fcc0fe64db3da79a5d924b2930de1bf3a1a5ae42751f66dd641db2
    role: context
  - path: data/traits/environment/halophily_preference.yaml
    sha256: d9d43dfaca09069195f27bdf5ceee8aa3465909f862e4ecff07dd22252b2c5dc
    role: context
  - path: data/traits/environment/halotolerant.yaml
    sha256: e3319db0bcc6539233ad930833fe29cd78a515a30cdbc0dd9661283e16c3efb3
    role: context
  - path: data/traits/environment/hyperthermophilic.yaml
    sha256: e3270047a52bbd8bcfb13db0e638508eafb6983002a09a9e28a9aad1bb239890
    role: context
  - path: data/traits/environment/ionizing_radiation_tolerant.yaml
    sha256: 95ec210aa700b57b5e8235d6078fa04cb0621bf4fd96c46d6970788b400176ba
    role: context
  - path: data/traits/environment/mercury_tolerant.yaml
    sha256: d479ef78e58a331a1a3efef7f2adc3697872fa9bbc6679f4b68d89505d4ed372
    role: context
  - path: data/traits/environment/mesophilic.yaml
    sha256: f1426444bb92913662470e0c46fc2a48d03256ae5f8650a346efc11031bed7af
    role: context
  - path: data/traits/environment/metal_tolerant.yaml
    sha256: 907f78048e48c547d03e3b2b073216a32007a0c0608fb361fba976a3812710c5
    role: context
  - path: data/traits/environment/microaerophilic.yaml
    sha256: fa57dd75a35f503778e764df1e8980a48dbb22e599fe35b96a2102e28ca080a6
    role: context
  - path: data/traits/environment/microaerotolerant.yaml
    sha256: 10a2073270238f7569ea0b93d131438699d93217724f45547f840f707389cbe6
    role: context
  - path: data/traits/environment/moderately_halophilic.yaml
    sha256: d9573c420c8313649a367d48e1c45d391199f5cf2f3e65bae3c607dc2c40f31b
    role: context
  - path: data/traits/environment/nacl_delta.yaml
    sha256: 902bec51cfb3915906b69bd7d35db4b31740f1c7fc0d0e0dd4fa60f39823c553
    role: context
  - path: data/traits/environment/nacl_delta_high.yaml
    sha256: ae4a75f37ed0d38a0f2e6cb73a2590ab4fe2b0b608002d44003ca43d2152ab6e
    role: context
  - path: data/traits/environment/nacl_delta_low.yaml
    sha256: 0ee750074eb279942ebf6b0ea570a05caeebb0e22e101c69fc12c6c9f9e1b634
    role: context
  - path: data/traits/environment/nacl_delta_mid1.yaml
    sha256: 32adf7d95f8545d8c1582b469cb9ce0508c4fe9d8c785fcc46c1b620aeed68df
    role: context
  - path: data/traits/environment/nacl_delta_mid2.yaml
    sha256: 7ad53553e557330df5cc8f19f0253bb98414179fe122901c811c4f6b0ed828a0
    role: context
  - path: data/traits/environment/nacl_optimum.yaml
    sha256: 530e0dd8a618ebef463fc9de538bf3d3d08cccdec8aee025cfb5b42d7a821945
    role: context
  - path: data/traits/environment/nacl_optimum_high.yaml
    sha256: 736caa7d453a19ec5da671a49ef983fa903083741e4bfc04eacb814b75d7651a
    role: context
  - path: data/traits/environment/nacl_optimum_low.yaml
    sha256: fa4740cfe6d4c91ef2f4b7ab6f3c1116231ca8873f277bea70fc400dc00f3c25
    role: context
  - path: data/traits/environment/nacl_optimum_mid1.yaml
    sha256: 65574c9a11183facd18b584bcbfcc4a55252772bf633c2c525261df11e99eb5a
    role: context
  - path: data/traits/environment/nacl_optimum_mid2.yaml
    sha256: 677e3c8c826bfc3a0059c1f1e0ef577b887a5f05ef7546b189a16f4c4642269c
    role: context
  - path: data/traits/environment/nacl_range.yaml
    sha256: 7f2e247297c3053e2d800cb41a3bbf04c9cc362ed1f1fc927b84570ff56d315e
    role: context
  - path: data/traits/environment/nacl_range_high.yaml
    sha256: 7254fd641f856dcb3910dbc27403736b5a730c39e97c4cbca6d4321e5ead2b7b
    role: context
  - path: data/traits/environment/nacl_range_low.yaml
    sha256: d5888822469d24051644b54575da20f1eaba1a91b9ed409368fea310cd1d9b64
    role: context
  - path: data/traits/environment/nacl_range_mid1.yaml
    sha256: 77c2be0184361d837f8e769793033e51fcdb3822aac94da228fb5ec8da9d7e75
    role: context
  - path: data/traits/environment/nacl_range_mid2.yaml
    sha256: e0f008cdd10d8bccce70a55e865abff995277fd4dbd878cb75781f49dee5f80a
    role: context
  - path: data/traits/environment/neutrophilic.yaml
    sha256: 894a324fa882e13b072d209a1c04c6fbf9b313a5c65a23f4c54ef6af25c82d96
    role: context
  - path: data/traits/environment/non_halophilic.yaml
    sha256: d992ae2092eb41b4cb59c1a1d71e975664ee17eb75defede412b020efdaf7168
    role: context
  - path: data/traits/environment/obligately_acidophilic.yaml
    sha256: 17c84a09cbc425d5d0fffdd56929c7f53751c3ae3d426b4209585ea237a08b11
    role: context
  - path: data/traits/environment/obligately_aerobic.yaml
    sha256: fb0a50f675b9eb7bc7cec7229ec38af195351917d6cb62b3e5c6c751c1924289
    role: context
  - path: data/traits/environment/obligately_alkaphilic.yaml
    sha256: 25d692b3e9a7d6862f4620ce1e78d7ddd6cb7b51f462ed7b854c26885d85c359
    role: context
  - path: data/traits/environment/obligately_anaerobic.yaml
    sha256: 1b12125f8ec6d84631f89b837dd2568e670cdeca8997b3afabca31c122130a60
    role: context
  - path: data/traits/environment/obligately_piezophilic.yaml
    sha256: e5164b6120e2e0152d0b03d21e96cf3a66941b47e79909aa52c1c170a2840d44
    role: context
  - path: data/traits/environment/optimum_phenotype_with_numerical_limits.yaml
    sha256: 85423dbaa018cc557495fec708cde21decddd7f0fc0d674f62b09c510d2309ad
    role: context
  - path: data/traits/environment/oxygen_preference.yaml
    sha256: 16829173ea947f2fef083f673c51519aad962d6812fcd54826ea86f055c5a40b
    role: context
  - path: data/traits/environment/ph_delta.yaml
    sha256: bddd29a48492578a5125f903de74f2c5476444e1069cb105008bdaf7fd2eacbf
    role: context
  - path: data/traits/environment/ph_delta_high.yaml
    sha256: 7e7805986348e83258bb0781a6c012cd4f47a1cf1f482397a92ecc2a13cd05ed
    role: context
  - path: data/traits/environment/ph_delta_low.yaml
    sha256: e2b3dfda6c0476d8a79f5f1209f3ec255512c2c5833236df59a05b2563c2e381
    role: context
  - path: data/traits/environment/ph_delta_mid1.yaml
    sha256: 6bf2a4e42d390eed49271db9119209ddf7b6cd0a2290df11a030dc91097479af
    role: context
  - path: data/traits/environment/ph_delta_mid2.yaml
    sha256: 932211da3cea840185defc3a9a984f419dfa0b8a729184259702acb00392b93c
    role: context
  - path: data/traits/environment/ph_delta_mid3.yaml
    sha256: 89eb6743c52450c4a65005a3af42587000019fa496d7d4543d7371f2fd9bcf11
    role: context
  - path: data/traits/environment/ph_delta_very_low.yaml
    sha256: 9126ea29b81127efbc9631999fce6b7d9de5a8318c00160655d954921ad5a802
    role: context
  - path: data/traits/environment/ph_growth_preference.yaml
    sha256: e9ee5a74bff604a7b3ba06ff6610deb83d7df762d7e8b3647699b799be72201f
    role: context
  - path: data/traits/environment/ph_optimum.yaml
    sha256: 55981325e7e0e85fa5e1f52fc04cbc6de77b981783685c4bdab25e8bab26cfc4
    role: context
  - path: data/traits/environment/ph_optimum_high.yaml
    sha256: 7c60e5e61ddbde6b115fbe4be96386696385e87040fb5924daa6c7d4da12cf6f
    role: context
  - path: data/traits/environment/ph_optimum_low.yaml
    sha256: eda82a5cfdd4b820895dbe955872248a5ba07079b6aab93450d332b25498eb41
    role: context
  - path: data/traits/environment/ph_optimum_mid1.yaml
    sha256: a09c605ffca25eb7df2c14729eb53383109bf0c62d645780fd4d617220cf6a8b
    role: context
  - path: data/traits/environment/ph_optimum_mid2.yaml
    sha256: 6e2a9f141a0e75fc3f0f92643724bab5473f925edb95f778dbe9060a9b2e3506
    role: context
  - path: data/traits/environment/ph_phenotype_with_numerical_limits.yaml
    sha256: 643abb9898dc920fe3aeeb0fa337c1d3a7efa6f0b540cb4ad979a3a28e0702d4
    role: context
  - path: data/traits/environment/ph_range.yaml
    sha256: 8a9cac2ea39eaf0aaafb950fce9b8119713bbef55c43e84550f22c3ee9d13d1a
    role: context
  - path: data/traits/environment/ph_range_high.yaml
    sha256: 3bf384769f08dd98073a67742a098348aca91cfbea63ea35bcee2e9a1a1c1fec
    role: context
  - path: data/traits/environment/ph_range_low.yaml
    sha256: 56a1489044011c883b75e007e5eb0d6a67984b791e77d8f02cf70c64e7fccff0
    role: context
  - path: data/traits/environment/ph_range_mid1.yaml
    sha256: c02a7b617de60a26f91a1594b7e5b568399ea854efea6c810037d3d52f9db9e3
    role: context
  - path: data/traits/environment/ph_range_mid2.yaml
    sha256: e0f668a5ecd91396331c42031c0d07a78af4d5ba12a4a57a1a2ec6ffd0eaaf0d
    role: context
  - path: data/traits/environment/ph_range_mid3.yaml
    sha256: 187d4bf625135bbcc15ee2175a3a7c9495bf3c220149074299b20f3a44d798b8
    role: context
  - path: data/traits/environment/ph_range_very_low.yaml
    sha256: 0955dd61255a701972cd23984962e4b7ad32cb4139ecd6dae6b411d6d119eae4
    role: context
  - path: data/traits/environment/piezophilic.yaml
    sha256: 484e671b502c1c5ced9ff4d93d2a41f5ea025833dfb59edd784a9ea295503317
    role: context
  - path: data/traits/environment/piezotolerant.yaml
    sha256: 39c384c29f9ca7646a4f6c0533d317a8346703609e8c7634c517d4fb6c1546e9
    role: context
  - path: data/traits/environment/pressure_delta.yaml
    sha256: 6fd90cd9c1f1e1404a2fbf6cb0a0462582c0075ee255cb27b4d5d26320077f52
    role: context
  - path: data/traits/environment/pressure_optimum.yaml
    sha256: 98d6f055b4c928fa8d5a2992d82671920a4e7d5cd65d4b4166ab396c4015d0ea
    role: context
  - path: data/traits/environment/pressure_range.yaml
    sha256: 660d7961eb1c41bf856e45872894bc198e82563b035ed19592d20558b07bbe24
    role: context
  - path: data/traits/environment/psychrophilic.yaml
    sha256: 1efc37ea89af76558af8c0ddbba1d67e9c4e6ddb9876d1faf6b884309a274457
    role: context
  - path: data/traits/environment/psychrotolerant.yaml
    sha256: 313c668f6414ba4bc84ef8893c4db094d6037e458290a0354cb584b1767b129e
    role: context
  - path: data/traits/environment/radiotolerant.yaml
    sha256: f3bae2896b2801fcaaacdf9c6783ef0df7b96d441e8858b5e1fa0b10e3713bf6
    role: context
  - path: data/traits/environment/salinity_phenotype_with_numerical_limits.yaml
    sha256: 429c11858371b7d407914e75a632071c749e3be29f496b7555c75c7f19fbf5bb
    role: context
  - path: data/traits/environment/slightly_halophilic.yaml
    sha256: 439a1c6cc793eb4a66f9ce16ebd843e808d7dad7f763db81937f4fa65340edba
    role: context
  - path: data/traits/environment/stenohaline.yaml
    sha256: 174f204b4454f531e9d88ef23c144df9b1f10813e7638edf919ebbdb123cac85
    role: context
  - path: data/traits/environment/strictly_anaerobic.yaml
    sha256: f7872f0e68be32ac4e6ccb62c33212750018544dfe7ab67446f1e1b1b2893bd0
    role: context
  - path: data/traits/environment/temperature_delta.yaml
    sha256: 38d2a033d5966f366b6db1a671d9fc2fc1ae09f6f4297cef9894e5eeae23840a
    role: context
  - path: data/traits/environment/temperature_delta_high.yaml
    sha256: 5a14c751b66b3593df2f558e50cedd4983484d782915e1b167e1404eebf12418
    role: context
  - path: data/traits/environment/temperature_delta_low.yaml
    sha256: 53943367c4a023a8cb78d61cecd9c66eecb4c7d92f76db1716ef631e15a90979
    role: context
  - path: data/traits/environment/temperature_delta_mid1.yaml
    sha256: 3f43e2bb4daf2c44cb8b899c2ea09963e96ed83f5a5c0ab3348628955155e9dc
    role: context
  - path: data/traits/environment/temperature_delta_mid2.yaml
    sha256: 7d4ba17fb1f84d0308ebcc5e6980668f15723122acd545a7d64954697882afc1
    role: context
  - path: data/traits/environment/temperature_delta_very_low.yaml
    sha256: bac0524b211d9e86fe45829dcc5c9ff7fa412c5d4b3bab7de5d2ee20e2a5a956
    role: context
  - path: data/traits/environment/temperature_optimum.yaml
    sha256: e419e363fd4b2e26f2ce3f092b117fba3103e5155e6dafb95bb5ce5c76644a0d
    role: context
  - path: data/traits/environment/temperature_optimum_high.yaml
    sha256: 55c6a5d2c2b644a373eb0a21b5d4b7fa32fde87fb625017ae9cc98bf61977280
    role: context
  - path: data/traits/environment/temperature_optimum_low.yaml
    sha256: 77a124a8c80516c4e9e9035da3ed24ab9ffd69ca55e7a87a179b06ef8ae66976
    role: context
  - path: data/traits/environment/temperature_optimum_mid1.yaml
    sha256: 4e13ab907307d4c88f5e787c45400a820c8c12a04fe311717fed3f3c6920510f
    role: context
  - path: data/traits/environment/temperature_optimum_mid2.yaml
    sha256: f97f6bddb24d09ee6fb58c83b569a84f10da84a59cb983b1c917d5ea68242245
    role: context
  - path: data/traits/environment/temperature_optimum_mid3.yaml
    sha256: 123f1ff2b2b7fc37d43aad15d468d12b6ff59d89fab05ba726258cc7cadc02e0
    role: context
  - path: data/traits/environment/temperature_optimum_mid4.yaml
    sha256: 5d1dd70a97245a6878813189e2b01f0a9d94e260bffeb3baf97b08b0e4847f3f
    role: context
  - path: data/traits/environment/temperature_optimum_very_low.yaml
    sha256: 1248a6be1eec6a1c5b4fcaec1102617f04fdf4db70d017bd2f35daeaadc515fa
    role: context
  - path: data/traits/environment/temperature_phenotype_with_numerical_limits.yaml
    sha256: 0eb92c52b7672f072e404d18a007ad19c381367e07601c5cf9cf8445a8562591
    role: context
  - path: data/traits/environment/temperature_preference.yaml
    sha256: 124373347177201d4a2ed44d2d69d1160636e6a99aacc87b4b0ee71e73f0234f
    role: context
  - path: data/traits/environment/temperature_range.yaml
    sha256: e3f8f082de570a8fc3de3ef6a1fdf95a60bdf28a6e2f6dcc43d3558df0775818
    role: context
  - path: data/traits/environment/temperature_range_high.yaml
    sha256: da5c449e9cd2d545f75e7ea7ce3fdae84496d4b0deb5c5cce13b024d429b3c9b
    role: context
  - path: data/traits/environment/temperature_range_low.yaml
    sha256: 88f9b9beb20b6a02eb878596af1e2fefc2de88c9f79eabd8cf4a5ed07510a3c8
    role: context
  - path: data/traits/environment/temperature_range_mid1.yaml
    sha256: 8dcac15a491e204f1a336f20c9cd77c6ff4a28ba17c674056469dd89234f6aed
    role: context
  - path: data/traits/environment/temperature_range_mid2.yaml
    sha256: 8733cf17429fadfda65188c2dcf931a6b8d18de91f2556c5befb5fc993b0e6d6
    role: context
  - path: data/traits/environment/temperature_range_mid3.yaml
    sha256: b0cd559b2373e71d092e1645beef2a9ff17548a43f953fded0eeff3d848cb251
    role: context
  - path: data/traits/environment/temperature_range_mid4.yaml
    sha256: c93988bf8e90168445afa36972a6eae657207e947ae99a422c05cd745ed692d8
    role: context
  - path: data/traits/environment/temperature_range_very_low.yaml
    sha256: c7261e615cd23d77d07a8f71d0f11c81a56a0f2011b15676f2d6bce51812eb9d
    role: context
  - path: data/traits/environment/thermophilic.yaml
    sha256: 66452534ae9ae3fc26d6b427986f1528e48b7b82889dd545c626997e73e381df
    role: context
  - path: data/traits/environment/thermotolerant.yaml
    sha256: 7c362d2643c79b3b7d4e36662b040acef4dc57ef108b9651cae2627786e7b160
    role: context
  - path: data/traits/environment/uv_radiation_tolerant.yaml
    sha256: e797a774782d68d5e3e68f2abbda80b148209fbd1061df80c15e07a956e592e3
    role: context
  - path: data/traits/environment/xerophilic.yaml
    sha256: 63c677d89e869f4c8d40c1c956ece3cf3f1e62d77d9feeb67623cd768d607603
    role: context
  - path: data/traits/environment/zinc_tolerant.yaml
    sha256: 806e51b929896446c6e64221c03ca1b3766673c2012f98608b98de63f23a1975
    role: context
  - path: data/traits/genomics/abi2_system.yaml
    sha256: d237b238b510e2bf3c21c8d7e7d847bdae94d83ad35990824d32d8220798f4d1
    role: context
  - path: data/traits/genomics/abia_system.yaml
    sha256: d04f57bc82074f3225586f96b0c57351fc67c9aa120bc2f87f40e64f4898ddca
    role: context
  - path: data/traits/genomics/abialpha_system.yaml
    sha256: c376cd9ec6fc7a2fb6f0a5b7e92c3eb88c2c03a4856873776b1676007ea30281
    role: context
  - path: data/traits/genomics/abib_system.yaml
    sha256: c226789a1fd07b9f4cc6c7131ff283490d44c77f095232e9cd200a4362734044
    role: context
  - path: data/traits/genomics/abic_system.yaml
    sha256: f7047cf5f85a8ae7a73a84b97e7ffb34c2b8128e0464669d6b63293a2f2a778a
    role: context
  - path: data/traits/genomics/abid_system.yaml
    sha256: 94ac19ccbe0cfed7c5266b502a0c2d552ac25a9ca8fb05e57306daed0eb3a103
    role: context
  - path: data/traits/genomics/abie_system.yaml
    sha256: a52c78863b84b501c0756a8c7020ff9fae3b85da999699ac47035be3757a5bd4
    role: context
  - path: data/traits/genomics/abif_system.yaml
    sha256: ed219bc9054053827cc920c21c293e91c660bc9cb89adb624437b6b90ae9ae38
    role: context
  - path: data/traits/genomics/abig_system.yaml
    sha256: ff228fc702efa4463d2e2222fb5ffa875a81c07bffebdf3f859c29882f235da5
    role: context
  - path: data/traits/genomics/abih_system.yaml
    sha256: 9376b236eefe6f0a4af993b0a46c3f34d1a698ad93b8386ff0495f53ed6a52d7
    role: context
  - path: data/traits/genomics/abii_system.yaml
    sha256: 142e7ac4d805c9aace5e42b025c711614c83ae5cad921d3d4156dc3fb19ceb5c
    role: context
  - path: data/traits/genomics/abij_system.yaml
    sha256: 27e368c62474de912c80afeffad1b0ccd51c3db67a90252c02b31751855806be
    role: context
  - path: data/traits/genomics/abik_system.yaml
    sha256: f7118f09e518b5b2882f2e64c6dbf9e39019b9817082fcd16ba44ee7c4210d71
    role: context
  - path: data/traits/genomics/abil_system.yaml
    sha256: 01c6bd3ec06259578dd307d85339370f58528cefe0befbc30a8cc8d3d172b17d
    role: context
  - path: data/traits/genomics/abin_system.yaml
    sha256: 064ca62e6ed88e06a5cc26f419f14ca8270ae7b09d29b251aabe7c87d274c226
    role: context
  - path: data/traits/genomics/abio_system.yaml
    sha256: fd04b4e8055f59f760bf2a03d8e7b62365c767cce521978d3178c16a8387b981
    role: context
  - path: data/traits/genomics/abip2_system.yaml
    sha256: 32f12178df72761b346a549d35a2251f48cddb95ba1ea749e02ecf49882d0148
    role: context
  - path: data/traits/genomics/abiq_system.yaml
    sha256: d1cb68c549f91cdef6a0354a8dd9f75e181cad9b67bbc05e4ec395a1228dd2ad
    role: context
  - path: data/traits/genomics/abir_system.yaml
    sha256: fd88f9813b95ee68fb4c7184d3329ea9eaa25fe45ab70e9eee82c23283d14069
    role: context
  - path: data/traits/genomics/abit_system.yaml
    sha256: f30a1fa10305a1ed7f416f696c840512e14e6388848b87e9677386f13b3dffc3
    role: context
  - path: data/traits/genomics/abiu_system.yaml
    sha256: 74d0cd2bf49c414fbe6417995203fb91962b84ad5f7b44a71d784e8414caea94
    role: context
  - path: data/traits/genomics/abiv_system.yaml
    sha256: 41c2ac95f396e2f2feaf1cac142e0c15bb0ffd47c4ec5f5bfc9a4edbc15056ee
    role: context
  - path: data/traits/genomics/abiz_system.yaml
    sha256: 266a9edc78b5ded0bb69d42aa1e81d638dedb4420496ee0c3dba17fb15081a3e
    role: context
  - path: data/traits/genomics/abortive_infection_system.yaml
    sha256: a305af937aca9fae8972dbc7add4cd4a5cb913eedddf6b7ee06251d258e1df35
    role: context
  - path: data/traits/genomics/aditi_system.yaml
    sha256: d9b561e2d0bff4016a585ca7a79f45e0c7fea6dca47c9f1f281f0214ca7c14e7
    role: context
  - path: data/traits/genomics/ambrosia_system.yaml
    sha256: 3b0354f0a1710cbdf7c0bc1368073660b24898b6b000c7e75893b6b39b717d5c
    role: context
  - path: data/traits/genomics/apsab_system.yaml
    sha256: 8e342a1c36a768887ec5dee9c26a214040187b10873bc3b3209c3ae060cff2e0
    role: context
  - path: data/traits/genomics/aristaios_system.yaml
    sha256: a5a57c0804622d8839427e6c7bf6f2bfce07c9c7567a288c294627ef8014e8d3
    role: context
  - path: data/traits/genomics/armada_system.yaml
    sha256: cb665518c56977d048962e46de1f5bf34d9a49a36248fcec670c8748539e58ff
    role: context
  - path: data/traits/genomics/audmula_system.yaml
    sha256: 38c1da47841f35d83685290a2cf6155c3bd5c566c612f9e6c236e9bc945ac10e
    role: context
  - path: data/traits/genomics/avast_system.yaml
    sha256: 9228808051302431efb8a0d84406b75f253639eef7021694afa5fd3469aaff6e
    role: context
  - path: data/traits/genomics/avs_i_system.yaml
    sha256: 7c9c1814d611c5f9de1b7cd09ff51a51e2b6888635798e00999cc70d053a267f
    role: context
  - path: data/traits/genomics/avs_ii_system.yaml
    sha256: 0a15546a88bb5f1dbb0a8f421f86eb6a62b5d60fa362ed98a959b8c2906ad505
    role: context
  - path: data/traits/genomics/avs_iii_system.yaml
    sha256: d7417ee6832560ba7871be84f1fc798919ab9f89be2e5bff5421ece21bdb727c
    role: context
  - path: data/traits/genomics/avs_iv_system.yaml
    sha256: f085c3890637fe274f1b0cda02e2773c5ac3e440595e5905ef857452eaa541fa
    role: context
  - path: data/traits/genomics/avs_v_system.yaml
    sha256: 8e1870c6cc4f0f7d7c86348da2f1f6fcc610f4125423818c48a86f14dc365fe1
    role: context
  - path: data/traits/genomics/azaca_system.yaml
    sha256: fd1de4ca89734898d96b831a5a0d0831ecba29818a92ca979c87f42aae72d7d1
    role: context
  - path: data/traits/genomics/belenos_system.yaml
    sha256: ecdbbdde194085cc292c30a0dcca7c265ecaacbbbb0d24e371559afc2d57402a
    role: context
  - path: data/traits/genomics/belisama_system.yaml
    sha256: 463940af5505cbff32f1c8daf61bd93d0a1dedcfe11e9182029834a86b00c3a9
    role: context
  - path: data/traits/genomics/bil_system.yaml
    sha256: b0fca87f4164788c98d88a4f72b3f9081a2a1e579e735c36027584edf0113fc6
    role: context
  - path: data/traits/genomics/borvo_system.yaml
    sha256: 24b798b2c7bccc63bbc1040748d2500a60e38e8f12eddbd16814b1425b2d0eae
    role: context
  - path: data/traits/genomics/brc113_system.yaml
    sha256: ab83fe65c4e6996d1051359d412549677153d75c4f4d00be02fc3db8a89cc4e0
    role: context
  - path: data/traits/genomics/brc142_system.yaml
    sha256: ee14208e040bfe887e71c81a44a600f861a2926da1c962e598379ae828122535
    role: context
  - path: data/traits/genomics/brc167_system.yaml
    sha256: 2a3b06af4c0cb43febae84f0b8ba9c0350747ab287fb768a21e3813d7dcb6ba0
    role: context
  - path: data/traits/genomics/brc217_system.yaml
    sha256: 817c42a07fac318bb82d40d9f9a6e972c5b0dccdc47722534a37d45f248457bf
    role: context
  - path: data/traits/genomics/brc22_system.yaml
    sha256: df83d5e8ddd1f5f84114740418dca20e229d4b947245c352b85bd08d02d2ee50
    role: context
  - path: data/traits/genomics/brc233_system.yaml
    sha256: 90d5760e9622958d396d9bc45763e1a3e2c90331e4c28ad128c647b155328f69
    role: context
  - path: data/traits/genomics/brc23_system.yaml
    sha256: b112c39da29a575f9edc18467a807860bb86f9813da72f85b1405b0d2399240b
    role: context
  - path: data/traits/genomics/brc24_system.yaml
    sha256: dd7bbd9d3a250846222eb1136460b58d1c8b88fe58db3de8288f713b702fadeb
    role: context
  - path: data/traits/genomics/brc59_system.yaml
    sha256: d96700ac0ed9bd192a34f96206978fd7547b94d38b77e83ec56bc9b824b60487
    role: context
  - path: data/traits/genomics/brc76_system.yaml
    sha256: 8e5928c3f75761af15153c4a3d23ce53393457b014a22450a9f948c87150bbac
    role: context
  - path: data/traits/genomics/brcwgs21_system.yaml
    sha256: 19c4284768b052430373d59159733905a53a33954ffdefa0103b6a61b2379d26
    role: context
  - path: data/traits/genomics/brex_system.yaml
    sha256: f4125f3d65f5fcd3da6c7143ea516b154ae141dc89b3d9ac3e985d4d14bdc80c
    role: context
  - path: data/traits/genomics/brig1_system.yaml
    sha256: 489a62715bd4daaf978df18c1b25d860a491567a742bb8b59671dc002a3d5e0d
    role: context
  - path: data/traits/genomics/brigantia_system.yaml
    sha256: 8751825f36b2cbe0c484c6d7625f1c80e81762073a2cf2b269d10f9ab7350621
    role: context
  - path: data/traits/genomics/bsta_system.yaml
    sha256: d9380178a9f9ba4d405c845eaf315e8d71b8d57de7075ab2c946ab56ce8fe55c
    role: context
  - path: data/traits/genomics/bunzi_system.yaml
    sha256: acdcb244a1cc3c0ff0acccb77dbb0998b709a59afb8b28a169621eddfaaf3694
    role: context
  - path: data/traits/genomics/butters_gp30_gp31_system.yaml
    sha256: 3f5e2a4c9a5b8a181d7de9ed7347ff79671daf537fed735075b643d060713040
    role: context
  - path: data/traits/genomics/butters_gp57r_system.yaml
    sha256: 3fe0d4d1efc03b7de5bbb146aeb3c36f36fe30182565502fa78efd7d6b930fcb
    role: context
  - path: data/traits/genomics/caprel_system.yaml
    sha256: f8715d7ae25548c2f749a4456e1fce0d0bd16f9efa7980744b04106fe0aef1e3
    role: context
  - path: data/traits/genomics/card_nlr_endonuclease_system.yaml
    sha256: ee4a8cbb46eba0e735bba36c1e23c60f20f1412ccb5e40ae81e6f559c9408180
    role: context
  - path: data/traits/genomics/card_nlr_gasdermin_system.yaml
    sha256: cfedd559d4468d9d0dcc0d18c417f60fc31dd65a7661a490312bebfce9f6c7d1
    role: context
  - path: data/traits/genomics/card_nlr_like_system.yaml
    sha256: ed64531614ac915ed191f591bee4367987355e6e04848ba89787de53f19f456c
    role: context
  - path: data/traits/genomics/card_nlr_phospho_system.yaml
    sha256: 2b78f61244d35cf9d485df294be18537417b16857d74f0d456e0dbe65daca4a8
    role: context
  - path: data/traits/genomics/card_nlr_subtilase_system.yaml
    sha256: e916099156a4751502e1d3b3ece5aefe1c4a360773eea50047485e44c1da522d
    role: context
  - path: data/traits/genomics/card_nlr_system.yaml
    sha256: ac05a08e8644fceaf05eb549a4ce59bd7ccb390efcb5d3241a10a6cd59a63ba4
    role: context
  - path: data/traits/genomics/cbass_system.yaml
    sha256: 01a88dcaf79b52ee26f1e8cdbfbb2702e7db9bbd56a8e66899ea50ef6c65b206
    role: context
  - path: data/traits/genomics/ceres_system.yaml
    sha256: c9aed8fd7356180b36ddee7e04bcb3abc4c35d648988c2734252c84844774b1a
    role: context
  - path: data/traits/genomics/cernunnos_system.yaml
    sha256: c58f533e219144157da9811361e0ed791f67a5065c23e55f78673eb7d475112d
    role: context
  - path: data/traits/genomics/charlie_gp32_system.yaml
    sha256: 11ad310d0f298ec81ed5d4f6c934a4f6930419f18563c1ad03ab536e84a838c2
    role: context
  - path: data/traits/genomics/clover_system.yaml
    sha256: b57a3a0f268e5ac14d8b15f63d52668603d63013eebcfb731e3a4e9e8245fdb9
    role: context
  - path: data/traits/genomics/cmdtac_system.yaml
    sha256: c68cd0890bb21b490351de2ebba0723bccd3b36d22ddb36e35feba376ad2f840
    role: context
  - path: data/traits/genomics/coconut_system.yaml
    sha256: 551887228e76ed27123bd5931018fc266979ac4c4a04cb2b635192272a819883
    role: context
  - path: data/traits/genomics/codon_usage_bias.yaml
    sha256: d6a0e3764d9ae04c7dd89f0a64fbf31f4f671aebb3308d8e6f54c9529103fcef
    role: context
  - path: data/traits/genomics/crispr_cas_system.yaml
    sha256: ea82ce4078513d1eb07da7a8df76405dce72d48598bc6b05582404e035c28d47
    role: context
  - path: data/traits/genomics/crouga_system.yaml
    sha256: 70149e407c2c22774fe63ec3392fc93414da0598789f49a148fc387b19ecdd8b
    role: context
  - path: data/traits/genomics/dag_system.yaml
    sha256: c5ad9a144e4bfd5988a4126e885b0e37f58afbe7773196d09ac797e835ae2822
    role: context
  - path: data/traits/genomics/damona_system.yaml
    sha256: f84a733639ec63ea60d7223485d1a7d23f1260022d4310e747b4559fe9cdef8c
    role: context
  - path: data/traits/genomics/darna_system.yaml
    sha256: 809ac3d83055297d2f61376f4e82991c30b7e51ade9f5acc18158d395d2ed7ad
    role: context
  - path: data/traits/genomics/dartg_system.yaml
    sha256: f32f22bd3ad9ea9d010b634b5a7ef2f14bcba8461bbf66e4b025cb563bf557db
    role: context
  - path: data/traits/genomics/dazbog_system.yaml
    sha256: 358193066dff80be058f06ed3924f89ce72bd6a59ddf66a31c480aaf60750ba4
    role: context
  - path: data/traits/genomics/dctpdeaminase_system.yaml
    sha256: aa404bd13dbccc5b873b98cdf20985c3748050fdcea42f19160ffefbecb41da8
    role: context
  - path: data/traits/genomics/ddmde_system.yaml
    sha256: 00d5d9f3121861e57e913a8c90c01c58d349aab506cca7bb8f5d2a465efae04a
    role: context
  - path: data/traits/genomics/detocs_system.yaml
    sha256: 1032a85785fe06b7be59166e8ada5e371a6133708e970438a4bbd23be3fca91b
    role: context
  - path: data/traits/genomics/dgtpase_system.yaml
    sha256: f7edd532fbcf17e18ea5cf3ce474bd3ddae431760101b479fabbbeef70268863
    role: context
  - path: data/traits/genomics/dionysus_system.yaml
    sha256: 5bdbf9fa84b07f15e89411abaab67207b395a4a109ae059848451a2242846156
    role: context
  - path: data/traits/genomics/disarm1_system.yaml
    sha256: 1c0e320f5a196a610a9a733df04855a0766249ad5f771c8dfaaf5bc64db03fba
    role: context
  - path: data/traits/genomics/disarm2_system.yaml
    sha256: 3d2569a6316ed712234a3536f2c4156a2eeb63e76afa6e816c37ab37cb03121b
    role: context
  - path: data/traits/genomics/disarm_system.yaml
    sha256: 45d0ad8fc91949a82a90ac65eaf353ab2601754b4bbf2ff3d069f00801b3e969
    role: context
  - path: data/traits/genomics/divona_system.yaml
    sha256: be5034bff844ff9b6636f795578672fb64470468db7c185ac7820e2f0378e54d
    role: context
  - path: data/traits/genomics/dnd_system.yaml
    sha256: 018c13d37be786267669687a2577f98aa5809a1944d54665bcc137034ec64f6e
    role: context
  - path: data/traits/genomics/dndcdea_pbeabcd_system.yaml
    sha256: 0c85f83ac830a0d15702abd84c6d43a6786b0d19912d3c334874edfac9b5599f
    role: context
  - path: data/traits/genomics/dodola_system.yaml
    sha256: edfe88c56e7a30bd697a81c4d3d9c97166373906a1f04478690da414b63ee92c
    role: context
  - path: data/traits/genomics/dpd_system.yaml
    sha256: 24f4f624b97961dc052a52f22fc7ec24eb8b42e14bdeb8ecfb5095fa3d26770d
    role: context
  - path: data/traits/genomics/drt1_system.yaml
    sha256: 9eb5abec48cf9333c8935af6db17511e7813a61bdc1949aef539fe12eb1fe4bf
    role: context
  - path: data/traits/genomics/drt2_system.yaml
    sha256: f81da50a962261afe3326b8244153045f9fbf3ce991a696fc7aa5778e86a1561
    role: context
  - path: data/traits/genomics/drt3_system.yaml
    sha256: b54cc7ee754b09fd4cf4db60718add539c95a886637b0abc64e9ef46fd2ee282
    role: context
  - path: data/traits/genomics/drt4_system.yaml
    sha256: 7b9d1965fd83d54df598a4e6a52e3e80b3f54a2c0129a7533a1773c41a254a6c
    role: context
  - path: data/traits/genomics/drt5_system.yaml
    sha256: 6efa75b3219b2dde1539f39c01e6ea50120deb00f9dfb2157f855f439cd62b5c
    role: context
  - path: data/traits/genomics/drt6_system.yaml
    sha256: 20aac140da2d04166e3487844bc1ac0df5d73455f6e7babbf5fa4dbc19b138d9
    role: context
  - path: data/traits/genomics/drt7_system.yaml
    sha256: cc6b934cadb71e0b02af60c69ec6e752bf10f567a250f7b33c69b0b1b0e7e894
    role: context
  - path: data/traits/genomics/drt8_system.yaml
    sha256: c69c4b7993e7a8da1b3535dd40fe29af1b8332e94acfdb7c2e8738a9fb6aa78c
    role: context
  - path: data/traits/genomics/drt9_system.yaml
    sha256: 26943b43452c435bd77468f5004513a468b09e50069500de9b89e8c09a6495f6
    role: context
  - path: data/traits/genomics/drt_system.yaml
    sha256: 3d34e2025d20cd3f11956652defafcb7f8c55aeda6856ba33faddbb0e0be6a4d
    role: context
  - path: data/traits/genomics/druantia_iii_system.yaml
    sha256: 298ca60ed8e3b1fc79cfcbb7a06eeb598b017e7f50703b9a5da7f560abbcf661
    role: context
  - path: data/traits/genomics/druantia_system.yaml
    sha256: 4cdbaa24d4a0d5eee5ffff6e7d53789574be95fde53aaab880c082523e1781da
    role: context
  - path: data/traits/genomics/druantia_type_i_system.yaml
    sha256: e4061f8df0a889b0b83e93225deb03237013ee14bd58b84d55eed9c1cb5e3e5f
    role: context
  - path: data/traits/genomics/druantia_type_ii_system.yaml
    sha256: 2338e84944aeaaa7f90b660b384e18e6c0ab91036848fcb2ba2f6535a6d86a65
    role: context
  - path: data/traits/genomics/druantia_type_iv_system.yaml
    sha256: 830fd87c88a4b599b5e7c18ec980fd12dd925c12c24b880e3c627d87c8a56d57
    role: context
  - path: data/traits/genomics/ds_10_system.yaml
    sha256: 236b4b45941f65115a7b96a98a70680535fd5266133f0187c3b8091d10e754e5
    role: context
  - path: data/traits/genomics/ds_11_system.yaml
    sha256: 9de77b97b2c0fa5e45d8a7c5566c09fd00c7193c3ca23451c63290abcda0204b
    role: context
  - path: data/traits/genomics/ds_12_system.yaml
    sha256: 68203f89d385cf1e24748a8af86e895c7fe35423a51fffd49b811cc0f26c2607
    role: context
  - path: data/traits/genomics/ds_13_system.yaml
    sha256: db654079947008c30e03cfa4d4b057aa3b53548aa2ca0b585503516968ccaf4f
    role: context
  - path: data/traits/genomics/ds_14_system.yaml
    sha256: a7f7e2c587cfd6b98ecc34f7dc5374bcdcf7854a8cd3701546854b0c453f5946
    role: context
  - path: data/traits/genomics/ds_15_system.yaml
    sha256: 26ed87a1a976d6b2366e0a0e86c9435bd2fe261214d0a96ef149d4a914d22256
    role: context
  - path: data/traits/genomics/ds_16_system.yaml
    sha256: 23df8134f3fef77ba0fc4aa9bc9f9f661c06c1d30ce1754588e8a84f20d9dd9a
    role: context
  - path: data/traits/genomics/ds_17_system.yaml
    sha256: 3cd992e35c028346c332b4c37c7ac4afc8fd6b7c4cce8e276932e48b4c16afbe
    role: context
  - path: data/traits/genomics/ds_18_system.yaml
    sha256: 8d5364d1ebaf2afea19396ce51cf61dff15d53c9b6ccbb10232e20d32b2719d4
    role: context
  - path: data/traits/genomics/ds_19_system.yaml
    sha256: ada227774e0645eb0dbd75f281e8b4b531363b2488c8b44fa4665b93ecb2d7d9
    role: context
  - path: data/traits/genomics/ds_1_system.yaml
    sha256: 6e4ae45e7492468d42f1ed810b2f819d57f76ccf4671a1806e0bf31a465dc897
    role: context
  - path: data/traits/genomics/ds_20_system.yaml
    sha256: 07d1441c05401874d12900bf9d25be6ead46ca174e64595c214c79efb442d47e
    role: context
  - path: data/traits/genomics/ds_21_system.yaml
    sha256: 32a2f178e9a4f7177b707ae00bdefba18ae5632083ff57d0114be6c595268fe8
    role: context
  - path: data/traits/genomics/ds_22_system.yaml
    sha256: 97f963b8cf836ba49aa663ccfa81eba4962cc1812b84e34424c12ec393a04a80
    role: context
  - path: data/traits/genomics/ds_23_system.yaml
    sha256: 49137bb1c4ca1c297da62b4d09e2ac8a470c61dfabdbc9d662dce61bb948089f
    role: context
  - path: data/traits/genomics/ds_24_system.yaml
    sha256: d16d34a5f903cd1ba15fd18383cc0696882b3195e0434cf1ebb1b2a153d738cc
    role: context
  - path: data/traits/genomics/ds_25_system.yaml
    sha256: 4cef63104ee8117a556cb43c09311083a6f89368cf9b191183f5d7ffe67295f8
    role: context
  - path: data/traits/genomics/ds_26_system.yaml
    sha256: 40165c3e647d7c142ba95e155a3e506afa943db45e3e513a14b1ce9dce96a7f5
    role: context
  - path: data/traits/genomics/ds_27_system.yaml
    sha256: 8b964bc06d97c072c838aeaa0703e0c303bf6debcf958de0a4804a0c0ecc7f26
    role: context
  - path: data/traits/genomics/ds_28_system.yaml
    sha256: da5fc52657693612953d416a21e94e4e9b8ba72d49d22c1bc90a535e4dc0ad99
    role: context
  - path: data/traits/genomics/ds_29_system.yaml
    sha256: cf8e577746f7c530e7b29279c8ea687e817c35ab66e8c03298891cee6dcdf0a7
    role: context
  - path: data/traits/genomics/ds_2_system.yaml
    sha256: b8b2c648ae6a6fdc01faf50f321abfe522f394aea8bd14a505480a16245e848d
    role: context
  - path: data/traits/genomics/ds_30_system.yaml
    sha256: 49292ed77b73dac95abac9ac862d5e468abf95d44acde2e59ceed51b148daed3
    role: context
  - path: data/traits/genomics/ds_31_system.yaml
    sha256: d97d758386621a1288a45434711bd7218fba789102600937945f26a411c198bf
    role: context
  - path: data/traits/genomics/ds_32_system.yaml
    sha256: 0b86cb5d61bda0afd04ac27a2a2b5582d0fd76fe80c4f7526b1d2ee77b61464b
    role: context
  - path: data/traits/genomics/ds_33_system.yaml
    sha256: acbafc84509fd94f73b11c3f5b95d37165e6bfbd031dd4c6f3366c5e45ae605d
    role: context
  - path: data/traits/genomics/ds_34_system.yaml
    sha256: f76c88b70405f0552481280b004aa2e9d75d76bb7edfe6fc4b45d9b2d4b4ea55
    role: context
  - path: data/traits/genomics/ds_35_system.yaml
    sha256: 8aa79d65ff4d1e36550f69a7aedc661ce9026de41025fc9e6ddef5ce9887334a
    role: context
  - path: data/traits/genomics/ds_36_system.yaml
    sha256: c2becf6c23652d40dc45a9cf103e86b5a3e8bec6f73821438957fc5b25f5135a
    role: context
  - path: data/traits/genomics/ds_37_system.yaml
    sha256: 88cf7b70c90e0c06069ea4d54ddbd20d1b3d8cf73ef82d281ce131672dfe3649
    role: context
  - path: data/traits/genomics/ds_38_system.yaml
    sha256: 3c974f396cc8ce5d185632ab71aeb2519e63ac885d928a5f85e574e0a8ca6015
    role: context
  - path: data/traits/genomics/ds_39_system.yaml
    sha256: addf7a7b8e76fc6781db0a9478db9539c2d0d522ff61b6c4338b4e1e7296e21a
    role: context
  - path: data/traits/genomics/ds_3_system.yaml
    sha256: 7b345b2de555211aa48ce002bf90ac474f69f92e3972234561aafc2fea205997
    role: context
  - path: data/traits/genomics/ds_40_system.yaml
    sha256: aec809ca6e1847addcb92f879ee56fb7037d33220132ca1ed4765395c25a8d00
    role: context
  - path: data/traits/genomics/ds_41_system.yaml
    sha256: dfb1f220fc81081984434112a998fda5606fa07135cc77b8302a485e808620ab
    role: context
  - path: data/traits/genomics/ds_42_system.yaml
    sha256: 468cbc1317a616b01040adcd0521ebb046eceb1b6a1a75dec8dd38295a2a1f9f
    role: context
  - path: data/traits/genomics/ds_43_system.yaml
    sha256: a7c0db63560ab3ca39962536d0a665e28c7d2fe68afc4a473c58ef1aae55b555
    role: context
  - path: data/traits/genomics/ds_44_system.yaml
    sha256: 2e6da2b5c92bfaf12586b57fa77d2a2b20beccc7f9e38400c5da35bc74d6b598
    role: context
  - path: data/traits/genomics/ds_45_system.yaml
    sha256: 2c996a5ea3b0f8270f71c4fe4eb5713e878466f601fc60ba927af5fb15ba56dc
    role: context
  - path: data/traits/genomics/ds_46_system.yaml
    sha256: ac9459559d5e73774fd5397a4d34bf94a7595c2525f6fcad0267d812f189d593
    role: context
  - path: data/traits/genomics/ds_4_system.yaml
    sha256: 170673b9081c2cc1da288531f4162af1cf5ee7f49be3868896e240b3c797bb1d
    role: context
  - path: data/traits/genomics/ds_5_system.yaml
    sha256: 3e0f6b23722e59dda5a7cf137521a5da69c230f3bb58d7658bc46f3ab1cef48b
    role: context
  - path: data/traits/genomics/ds_6_system.yaml
    sha256: 92eb1f86884aa7a9017da846424f9884eca7972a5d33a84fd32d2401dddaac52
    role: context
  - path: data/traits/genomics/ds_7_system.yaml
    sha256: e532cf614c0a6a4560eb637b142796c88b2dd01ff5ada63c905102130c3b6b20
    role: context
  - path: data/traits/genomics/ds_8_system.yaml
    sha256: f9870987ea45cfe4b600444ce0e77996bab850c1a8a9ad9d5c5e052e4121bd1b
    role: context
  - path: data/traits/genomics/ds_9_system.yaml
    sha256: 583c02548cbdf658398151c0efc11703221d8da7e64591f95a6dec8c5dde8471
    role: context
  - path: data/traits/genomics/dsr_system.yaml
    sha256: 884b66c09abf6e6eddfd9f01a8f3c75f1119212073ad5a659e8e0847f1e8b13f
    role: context
  - path: data/traits/genomics/duf262_schlafen_system.yaml
    sha256: 9707d9f1abf27c465f7b2017b0ee2006a8278b2773a091f6b97d915f3a4321d5
    role: context
  - path: data/traits/genomics/ecokmcra_system.yaml
    sha256: eb09d141f8913c07d320df31d7d319b314717f7bdf018d051ec123cfd37d5cba
    role: context
  - path: data/traits/genomics/eleos_system.yaml
    sha256: a7c81436fa0c0668ae3021b0a15bd440aa3adb5e5b88ad88ec83d36cb4f89a26
    role: context
  - path: data/traits/genomics/endpacf1_system.yaml
    sha256: 9b437e56b4087ccaa81d9eccca24e0ac0245d0c3000651f5cedf467bb80aa22b
    role: context
  - path: data/traits/genomics/epona_system.yaml
    sha256: b18529c9d57dbadd29cdc9d60685e9bcc1f4c3ae302a465522a3f1832ba06271
    role: context
  - path: data/traits/genomics/erebus_system.yaml
    sha256: 71e701c1e3c88fc2802ba066c58c19408af3f6f1224af8a9adda1a98891a9993
    role: context
  - path: data/traits/genomics/esos_system.yaml
    sha256: b23a00809977afd22af412333b26b7ea378a2b1e2d0a2b808e9d9c01f915e9fa
    role: context
  - path: data/traits/genomics/fliodhais_system.yaml
    sha256: 512037fce5dee19c8da26db15d67e6ae0ab2e4d646ac519ea89d44df0d2feaba
    role: context
  - path: data/traits/genomics/fs_giy_yig_system.yaml
    sha256: 41dd2004ff4ecaac057f7e68cda107ada2e45efbf6dc7dcb934f43884d07a9f2
    role: context
  - path: data/traits/genomics/fs_hepn_tm_system.yaml
    sha256: 3b3fe568e37163a52138cfcca530a705cf7b2b4cdf2f8ab6570358ff8383f963
    role: context
  - path: data/traits/genomics/fs_hp_sdh_sah_system.yaml
    sha256: 0e8dbf6ba475f1bed519b3c144e286184450eb01a1824771f5654bece31b9986
    role: context
  - path: data/traits/genomics/fs_hp_system.yaml
    sha256: 8f446e18d66f4b26d0e43d528ae808aec6a21012d6c1e45686e98a676d09ff45
    role: context
  - path: data/traits/genomics/fs_hsdr_like_system.yaml
    sha256: 3c677cb9d7e078c19c0e39774eb0a4d7421ff51875bb36055c088dc831e515ad
    role: context
  - path: data/traits/genomics/fs_sma_system.yaml
    sha256: 5a70093a79eea1f5a86b13bae26501ed2feded25ae5e4fc51bd1567d176f513c
    role: context
  - path: data/traits/genomics/gabija_system.yaml
    sha256: 52a746815263e45bb79fbadec461d83d620bc46c6769656839216fec77f6c42f
    role: context
  - path: data/traits/genomics/gao_ape_system.yaml
    sha256: f2b56bd9f41afa87d8b0633c176398bef8a740a4c75018e4aaa553f4b3499913
    role: context
  - path: data/traits/genomics/gao_her_duf_system.yaml
    sha256: e3e5f8b73d06d3d2bf1238015d09606499850dbd5ef031504b09bd3b13be4b17
    role: context
  - path: data/traits/genomics/gao_her_sir_system.yaml
    sha256: 0be3134ffb384d125614b582cd61dc7594034eb857943ce7b9462b5378d1a193
    role: context
  - path: data/traits/genomics/gao_her_system.yaml
    sha256: b584c084a01b5fe7d5878dfd058412fc8d3bdee028c936ab1ef70caeb2a88921
    role: context
  - path: data/traits/genomics/gao_hhe_system.yaml
    sha256: e9b50ee1d969250b33d56dc3c35b6b0e5106c5ea746f5953e12c74c1981b6755
    role: context
  - path: data/traits/genomics/gao_iet_system.yaml
    sha256: d6751d43aea34fb9fd31232dd1e02bbcc3b68b21ee94a825ccca12b77e61ffed
    role: context
  - path: data/traits/genomics/gao_mza_system.yaml
    sha256: 57e66a7536901458cfe859aa589f257f8184370f9cae9c94dbf4399e7982535d
    role: context
  - path: data/traits/genomics/gao_ppl_system.yaml
    sha256: 4b63516ee624e1eebc4d8ff324d98a006078963238f5e918e0da333d90ebd50e
    role: context
  - path: data/traits/genomics/gao_qat_system.yaml
    sha256: 6fcb78cef9d44a9a7282fd9bb31c1e98bf5899ef62aca320f76132c9b431bc4b
    role: context
  - path: data/traits/genomics/gao_rl_system.yaml
    sha256: 4db346fa22f79f7600fe6c08ac6238adfc542f6f5b4cbbce016f5b5385018089
    role: context
  - path: data/traits/genomics/gao_tery_system.yaml
    sha256: 625e16bf24cbfcb0d99b8bccd078914245a81646ca7f972fb42a8c76eda5350f
    role: context
  - path: data/traits/genomics/gao_tmn_system.yaml
    sha256: 03764bc70687ac116d5b3e76270084fa8869aee504fe199be666b9aac4165807
    role: context
  - path: data/traits/genomics/gao_upx_system.yaml
    sha256: 1fe376ac9556b5b6ec6076329aacff182ad7ab44b5ae3cddac66abb103f7564f
    role: context
  - path: data/traits/genomics/gaps1_system.yaml
    sha256: 48bc97df8db46fc95182d2470f85943ef414070963a61261384276ead5663db3
    role: context
  - path: data/traits/genomics/gaps2_system.yaml
    sha256: fd91a6601ac9edf397b469e3df73ca556725cca1cab40f70ef71747b38e3428e
    role: context
  - path: data/traits/genomics/gaps4_system.yaml
    sha256: a9c2a90492969547cacd961ea46dc1335a04872623419b8fc273da5638b51879
    role: context
  - path: data/traits/genomics/gaps6_system.yaml
    sha256: 8561c9e47e5b7d90db74b8d1744e59a84efcc3e1bfd524c16c3852b84d48b251
    role: context
  - path: data/traits/genomics/gasdermin_system.yaml
    sha256: 1feff0112506f1cb2e822b2a5999192b7506114682735fee8ba04d53bab2365b
    role: context
  - path: data/traits/genomics/gc_content.yaml
    sha256: f1a3c0d833f53f4f147ac14fc1efcaa4dc4f1baf32ce86e2f86db14ec91f2c13
    role: context
  - path: data/traits/genomics/gc_high.yaml
    sha256: d8821b347303be612230f7d1a8cd601055fd877d743b372f86998a77bf48a821
    role: context
  - path: data/traits/genomics/gc_low.yaml
    sha256: 3a79789db689e62df642411d05e6b6eaf7ba30a7e767948b2a8a113426fe4a1e
    role: context
  - path: data/traits/genomics/gc_mid1.yaml
    sha256: 49045ae66ccd685bd0795d4a86923f83b3d8cbb6e12c8fe715b2626ff4fef65c
    role: context
  - path: data/traits/genomics/gc_mid2.yaml
    sha256: a41dda8d92f289f0548845e1f4e55a40318aa24aa438f3b1801e89f8762f3146
    role: context
  - path: data/traits/genomics/gc_skew.yaml
    sha256: 32d9848ade8b11e02e55e7214019b7aac0e05217356354a436cd86a913376090
    role: context
  - path: data/traits/genomics/geb_system.yaml
    sha256: 454932dae01f2a980ffaee1315f7bacebcff6f05a261396a25a07aa65517f903
    role: context
  - path: data/traits/genomics/genome_size.yaml
    sha256: b58f55ea874066ef65e7285e04c4fd7e91bd2dab1fa733da34f30404b5008d03
    role: context
  - path: data/traits/genomics/genome_streamlining.yaml
    sha256: ada8ec62ccbf539d2ddeea638fe21f22f231b5b3eb0a2552bbe5c3ad089732ae
    role: context
  - path: data/traits/genomics/genomic_island.yaml
    sha256: 08f201639a7ba95454ca0eba1e70c5caf179b4cc52527789077401bf028a49de
    role: context
  - path: data/traits/genomics/gmrsd_system.yaml
    sha256: 31d4f7167527b42da3dc6b8a0c5d1ab769495c34fc2a218ea6ef2268507b2e66
    role: context
  - path: data/traits/genomics/hachiman_system.yaml
    sha256: e2a8d9a722e0c52bf560662fb6c2277557ad1910c4ce4d18d32a63bee9185ba4
    role: context
  - path: data/traits/genomics/hachiman_type_i_system.yaml
    sha256: 0abedb1dcea6b34412adbabbe844b852c7c3ca1b18ad0b4dbf7248b1c614649c
    role: context
  - path: data/traits/genomics/hachiman_type_ii_system.yaml
    sha256: 501e02bbbeff161e0d80bec0dfeb4d5603b1d798e686be8ea0b4fc0b3a86d68d
    role: context
  - path: data/traits/genomics/hailong_system.yaml
    sha256: 93f39df79d7b75eb8c919350abe4981dcf8793df725e9356cafbc16c557e7848
    role: context
  - path: data/traits/genomics/hec_02_system.yaml
    sha256: 4f9b965e3b77adb85f809009c8e12c094818af0af9a3bdfa9cf90efed8c9decc
    role: context
  - path: data/traits/genomics/hec_03_system.yaml
    sha256: c0677f0c8b2b1d5d559a3a84513ccdb8ac20547c19b230d3410568d5e16088e0
    role: context
  - path: data/traits/genomics/hec_04_system.yaml
    sha256: 42d2ba249e692aae5bcd2af2a25c954fed585086f79d95d23dc1140dc541ad5d
    role: context
  - path: data/traits/genomics/hec_05_system.yaml
    sha256: 58656aafb5eb6ea57a47ecac61a2e4ab55be6bf43652e113330255d8388f7400
    role: context
  - path: data/traits/genomics/hec_06_system.yaml
    sha256: 0fdd3998455e1d481edf406bb395661ede80304a1207e6b0a3ed63d63b3efb14
    role: context
  - path: data/traits/genomics/hec_07_system.yaml
    sha256: 9cced1ed7728ac85ba37bd4e4a843c7f168777a8eb24cd2a9ebed55494071cbe
    role: context
  - path: data/traits/genomics/hec_08_system.yaml
    sha256: fb43f969e064d0c76727a2b61fff6dc7c7ab90723a63187aabf067cdb714b889
    role: context
  - path: data/traits/genomics/hesat_system.yaml
    sha256: c318d5ace92d8d0f80b9b84244b8c6b31350723675d542e8f4fe0d953062098f
    role: context
  - path: data/traits/genomics/heterokaryosis.yaml
    sha256: 3aedf3905da8e3c27c83aea69fbe9336a8662c899d9d63b81183ebbb35ce1ac2
    role: context
  - path: data/traits/genomics/hma_system.yaml
    sha256: b1b3115dc553272a984daab54d9a214c25520ad73d1477caf3628ac36a5fef60
    role: context
  - path: data/traits/genomics/hna_system.yaml
    sha256: 2775e11e9abcc9fdf6081605d4cbc31f32518b2f788a9343adaa9dc42b08f2a9
    role: context
  - path: data/traits/genomics/hypnos_system.yaml
    sha256: c29ec5782bce54357c5784c73e04d6462f102f4806ce98f7ce529661caa92eb2
    role: context
  - path: data/traits/genomics/ig_like_schlafen_system.yaml
    sha256: 3873a218714c3b5c202c55f49ed7366702ee4c2c648b9bf64157b2776c296c68
    role: context
  - path: data/traits/genomics/integrative_conjugative_element.yaml
    sha256: 4db281729ee587e95fb18d3c87026c93e8e8fd1b5e0cb38210787aa930f06c14
    role: context
  - path: data/traits/genomics/jukab_system.yaml
    sha256: eae952c87f770ca39b722570475ba26bf35570b73aff034765cc5bfd13d58cda
    role: context
  - path: data/traits/genomics/kamadhenu_system.yaml
    sha256: 547b11da4d1e89de31d78f56b30215d74454353d333d7d9dbc9fa0d058ff1d69
    role: context
  - path: data/traits/genomics/kiwa_system.yaml
    sha256: a76313fcd1e2b551d523f88e28dfe9ba797f00f2b750bdfaba97f82854545168
    role: context
  - path: data/traits/genomics/kongming_system.yaml
    sha256: 520c3b282ed1497905bb79c07f2875014204372d76b6588193854aeed3c8417a
    role: context
  - path: data/traits/genomics/lamassu_amidase_system.yaml
    sha256: f57e2ca5a98e22a3760ad7ea0294c68de922b9879dd8166efac823bd45a9cf2e
    role: context
  - path: data/traits/genomics/lamassu_cap4_nuclease_system.yaml
    sha256: bcf5b428da6404b8ecf40efbb16f1fee97adbe349b546469f384984504fd44e6
    role: context
  - path: data/traits/genomics/lamassu_fmo_system.yaml
    sha256: 3bd0e8d15cf27980300c8fc955ac847179283e5654b79ceb4c28874a624ba9ff
    role: context
  - path: data/traits/genomics/lamassu_hnh_system.yaml
    sha256: e39d6cc6e7b9ceafe9f9a453bcbe0a097f65fd9e2138a1fbb8d09d9ed3090c7c
    role: context
  - path: data/traits/genomics/lamassu_hydrolase_protease_system.yaml
    sha256: 8159361949372e39bcff86474dd4a389b69a827b47fa7936f93b876f69535ead
    role: context
  - path: data/traits/genomics/lamassu_hydrolase_system.yaml
    sha256: 6206c93e1beb63ef01db2bd1f94c0c4bcdaec896d17c122e6155163eee76ef35
    role: context
  - path: data/traits/genomics/lamassu_lipase_system.yaml
    sha256: f61a7b7a63e1d612262f4dae027594a038d75465f7d44ab591a54b1c49767d5a
    role: context
  - path: data/traits/genomics/lamassu_mrr_system.yaml
    sha256: f252420644fee7cf1cf2abf75300c1bded0c289805f6fd63a82d30c6d8c92f4c
    role: context
  - path: data/traits/genomics/lamassu_pddexk_system.yaml
    sha256: 708841b5fca19e2c68cea82ef16d87657b3650b04e68ca29f9ac646fe90b753d
    role: context
  - path: data/traits/genomics/lamassu_protease_system.yaml
    sha256: 3c9fd08cd8a3f87dcf984eb24fe9ec849ce8a54b5cd9a5934b883f29ea638a65
    role: context
  - path: data/traits/genomics/lamassu_sir2_system.yaml
    sha256: 4bc3ebb5bab5d68e79cd4b565fa23085835ce93b1b899506b41094fb27d4f483
    role: context
  - path: data/traits/genomics/lamassu_smek_system.yaml
    sha256: 4d8df1f059b146bb9ca465a7f77b4689d9a813dcd338523caf4055ac376bceaf
    role: context
  - path: data/traits/genomics/lamassu_system.yaml
    sha256: ceb6fc4ef2dc65655e801efc7395e61bf43a8600308c556249d2e5f3f3d5b6ed
    role: context
  - path: data/traits/genomics/lamassu_type_i_system.yaml
    sha256: 24bd7dddaad02674d17aabab9807d81fe6419606898393738daff203ebb2cdf0
    role: context
  - path: data/traits/genomics/lamassu_type_ii_system.yaml
    sha256: 108c96bbece6b2f36fb36edc0fdeb8f8b07634cad295a11a982630fc48dc6a68
    role: context
  - path: data/traits/genomics/lanthivirin_system.yaml
    sha256: 1def9e05ca7af8a4ec515fe88489f9b87514add51bea642fc8ce237c3f437a84
    role: context
  - path: data/traits/genomics/lit_system.yaml
    sha256: bde4b3d54e7ae8aeb912c56240587b6f7c504e78890a6fe569096bc2e3ec977e
    role: context
  - path: data/traits/genomics/long_lamassu_system.yaml
    sha256: e04e8ac028d8681ce39e820eebb09c04cc0cace74a926b2dac7d1d063801ae80
    role: context
  - path: data/traits/genomics/lugos_system.yaml
    sha256: d4d87544ae4fb3ac9f238b100b40f4d247e11f86ff020c27de45c797b55d1c20
    role: context
  - path: data/traits/genomics/mads_system.yaml
    sha256: e5006894255bd01dab3ce88fe804ed5012c01c6d3460f171f43f08eb0834cee1
    role: context
  - path: data/traits/genomics/mazef_system.yaml
    sha256: 3a656c9ea5b6a34e57106ac487a47bfc6ba7fb3ecfea6eb452e505fa327c7f3b
    role: context
  - path: data/traits/genomics/mcrbc_system.yaml
    sha256: d44ce382ffe246081003a9ec79268e08c9bba94913ab1805ed9c4a24e82b4f1a
    role: context
  - path: data/traits/genomics/menshen_system.yaml
    sha256: d2cb095f2c0655c0d239f8db3d2a1b1c9af8ae4766c88ed6e8ce3d17b5ba7ad9
    role: context
  - path: data/traits/genomics/metis_system.yaml
    sha256: 7320a02a919163cea1db5c272937f891605ac66ca95fef80ac06d6c9ce1e5805
    role: context
  - path: data/traits/genomics/mksbefg_system.yaml
    sha256: f6af182d9746304a8337bb6ec3115527e9119f8c1af6761e29f92062531bf5d2
    role: context
  - path: data/traits/genomics/mmb_gp29_gp30_system.yaml
    sha256: 57b63cb31bf104735fd997a34159cd592294e91e2883e245f32db28ce1d8f0e3
    role: context
  - path: data/traits/genomics/mobile_genetic_element.yaml
    sha256: 38af7e8dea74370592584be9854b82319612c0eabaf61fad062a5bf6fe07db85
    role: context
  - path: data/traits/genomics/mok_hok_sok_system.yaml
    sha256: b7213810d93fa315da3c3681146a9fa52ee808420e121bafe9714c2b520401bc
    role: context
  - path: data/traits/genomics/mokosh_system.yaml
    sha256: 5ebf21d2816250c189fc43e548132aed54ecb000c17328f634135daa2b9a1eb6
    role: context
  - path: data/traits/genomics/mqsrac_system.yaml
    sha256: bc46cd0a719102f5580e560aedba9b9eae8f30b1e159b1dbd2fbe1b80868de19
    role: context
  - path: data/traits/genomics/mspji_system.yaml
    sha256: d7988a198ff71f96986a342d51cf1363b5f127147d27c8d9ac89440a46df0081
    role: context
  - path: data/traits/genomics/nantosuelta_system.yaml
    sha256: 5e030397f5f470ec4e9b7cebf4059fc935f09d10c78dda59f54fc7926a8cf7f2
    role: context
  - path: data/traits/genomics/nemetona_system.yaml
    sha256: 3b5a77ef46ce663096eb4d1b1b835d582f568255bdaffa00bde83f86b9367464
    role: context
  - path: data/traits/genomics/nhi_system.yaml
    sha256: d67a61bcb94b712532ee38ebf438c6acb913e61f79efba8d8b429455dd55f1b3
    role: context
  - path: data/traits/genomics/nixi_system.yaml
    sha256: ffb69c9a600c1986a4dd414c9db84fa97174f008ed7ac1a99912110461cd7f41
    role: context
  - path: data/traits/genomics/nlr_like_bnacht_system.yaml
    sha256: 44abaf2ea5c8d147650075cbb19ec8a34b8a7de3204f1aada0e471ab48382a18
    role: context
  - path: data/traits/genomics/ogmios_system.yaml
    sha256: 3d1cecd49cd19d33f6d3aac3596b30c84b79193f80bba18d1c17e078043ec2c6
    role: context
  - path: data/traits/genomics/old_exonuclease_system.yaml
    sha256: 1206e440fabb7df1f1352b2d4f013dd8d4946da1c97553cad7ab780c3daf514f
    role: context
  - path: data/traits/genomics/olokun_system.yaml
    sha256: 01bbeba3d41a170d0ea5be9c313ecff59acf6a5adab81692a22042a0c2f7e728
    role: context
  - path: data/traits/genomics/ophion_system.yaml
    sha256: 95b15491202af2892fbca7535145654360e6933e3073a61739e47e95168cf8e5
    role: context
  - path: data/traits/genomics/oshun_system.yaml
    sha256: 0fd71aec6523648d358439abb66d1ab710b8421778cd70b239cf46b39edf89a2
    role: context
  - path: data/traits/genomics/pago_system.yaml
    sha256: da9e930028be01d928b470b716a83e87bfb60d02d8b4710cbc25b9e7a41f99d5
    role: context
  - path: data/traits/genomics/panchino_gp28_system.yaml
    sha256: c16a71144113971e71093e001ae3d2bdd52d19041dcc532a37d5523fa9005227
    role: context
  - path: data/traits/genomics/pangenome_openness.yaml
    sha256: 9ee365c3d174ec25926d9ebbe1d8ea0444832a4a82765e3f2e34367d27694279
    role: context
  - path: data/traits/genomics/panoptes_system.yaml
    sha256: d2f69521f930c6e6bf601751665dea1624dca393edb954ef0ce5fe9d4115001e
    role: context
  - path: data/traits/genomics/paris_system.yaml
    sha256: ca66c103eb77a004672db0b6b71c2fe752c6e5407fb33240989eb1e441e2375e
    role: context
  - path: data/traits/genomics/pd_lambda_1_system.yaml
    sha256: 94eb07dc2f75b0a9e82bde82c49fb5c6ae327cbcbba8b41c7d892a2d6ea1db56
    role: context
  - path: data/traits/genomics/pd_lambda_2_system.yaml
    sha256: c4fef9791d7198072b229a4f7c851d9b4f3e155b284cc2a0526d6bb1401c421e
    role: context
  - path: data/traits/genomics/pd_lambda_3_system.yaml
    sha256: e724fc95d6fcc86ba04b445dcb4e7a9e4901f9a973b1915f08056504cb31acc7
    role: context
  - path: data/traits/genomics/pd_lambda_4_system.yaml
    sha256: 5fd121636dd0402737ac21673a9e0a4d5a92017261f9d7e579c19e6fa695b03a
    role: context
  - path: data/traits/genomics/pd_lambda_5_system.yaml
    sha256: e990428f70f8e946e0b49a54bbe279683a655635a2692419375f8a4661169717
    role: context
  - path: data/traits/genomics/pd_lambda_6_system.yaml
    sha256: fc362672e49f8c7f758151be8893fac10000fda11ff1a0721031201d6735fe02
    role: context
  - path: data/traits/genomics/pd_t2_1_system.yaml
    sha256: 245b1909de8dce096a59386f507fec3cb7b36bf4599089fc8004d822e7f6735a
    role: context
  - path: data/traits/genomics/pd_t4_10_system.yaml
    sha256: 18a3cebc3dfe28776b96da96cd48ec7028942454e3e1d637adca028ac481d9ed
    role: context
  - path: data/traits/genomics/pd_t4_1_system.yaml
    sha256: 150ab2778745dbc7184f1078cb8df458bbeb0eaebf43f340ba8ae45d3cfbce85
    role: context
  - path: data/traits/genomics/pd_t4_2_system.yaml
    sha256: 1e590fbb44ecbf24ebc2c1b094029dbb72bf4c809e36e582a34d6a62a42f537b
    role: context
  - path: data/traits/genomics/pd_t4_3_system.yaml
    sha256: 01c2cab57bdb76e9db4d50aea9e0d9653333fd9ba6f114b4d03e4b29ecec7dd5
    role: context
  - path: data/traits/genomics/pd_t4_4_system.yaml
    sha256: 8768a9732c1f35b9f36231e28f62dc24a41ccf620a138584870481c24622ff81
    role: context
  - path: data/traits/genomics/pd_t4_5_system.yaml
    sha256: ecbb82ba7ae9e2e3897e56692073634ee0cf0866760b7273c56c776db66d4587
    role: context
  - path: data/traits/genomics/pd_t4_6_system.yaml
    sha256: baaabf8b2120905c320273c745c5cdccf09e6527b18ec24e8d38cda92dfd8d6c
    role: context
  - path: data/traits/genomics/pd_t4_7_system.yaml
    sha256: 088fa75371758ad61c47af9883292ed1aa00153927e313d4c81df054c74f861c
    role: context
  - path: data/traits/genomics/pd_t4_8_system.yaml
    sha256: 94536f195ed01935cbe5fa3bb2dade3dc080b22ef4d8473882e0c640260ab657
    role: context
  - path: data/traits/genomics/pd_t7_1_system.yaml
    sha256: 5959351795155b2f260fb1101fa565b43f3ff84d97ec57599216a2e2cc82cd3b
    role: context
  - path: data/traits/genomics/pd_t7_2_system.yaml
    sha256: 8fdbaa2d0e1136701aade0fbc588c16a657299849e7704ec0a7cd81a66286864
    role: context
  - path: data/traits/genomics/pd_t7_3_system.yaml
    sha256: 412774f7ffd7bd6163eb9834556d8fcd961edfc3d2e6d6b5b0974c86973a293f
    role: context
  - path: data/traits/genomics/pd_t7_4_system.yaml
    sha256: c448140eaefaaa7326ad6f45482bb61da0a4f27051b60ede42bf53c09ba6ecc8
    role: context
  - path: data/traits/genomics/pd_t7_5_system.yaml
    sha256: 95b69aa2ace4b26c6ecc961d79588cee05ddd1585abf55bf74d7388dbdd08869
    role: context
  - path: data/traits/genomics/pfiat_system.yaml
    sha256: bc5ba2f14d3b27d12c1758aaf248e2f8f782725b044f98b82156f8035ead3683
    role: context
  - path: data/traits/genomics/phage_defense_system.yaml
    sha256: 37e9acdb5482cc2ed8a9bda28cbc3d6f072008016dbc09f9cdecbd062f1856a6
    role: context
  - path: data/traits/genomics/phosphorothioate_defense_system.yaml
    sha256: dfca429e992f34e564afa0b1e554445f3658c9e16f6783a9867a934ea9c87b28
    role: context
  - path: data/traits/genomics/phrann_gp29_gp30_system.yaml
    sha256: 4a66c1035b6b0945463919185cdab227e0dae6dc90d76979e51f3d81c50ccd39
    role: context
  - path: data/traits/genomics/pif_system.yaml
    sha256: 2895d100ed9f5b2f697e54975664d4912e3b32ad52b6f1c5b4f24771c9715fd8
    role: context
  - path: data/traits/genomics/plasmid_carriage.yaml
    sha256: 79b5e908e06b00d63346d3ede0fd1986260c622bf74fc6a68e2526e299fac205
    role: context
  - path: data/traits/genomics/ploidy.yaml
    sha256: d3aef807f3c382736019d511e86e3f9d6574ebeb2a070c1458198c3e2bc01f45
    role: context
  - path: data/traits/genomics/prithvi_system.yaml
    sha256: 054bec62dd02012d0270be3d3da96f1f563258a648c44e36b5f3d1aa9e679899
    role: context
  - path: data/traits/genomics/prometheus_system.yaml
    sha256: 7f75f5c35aa279aa6c5059e9c8cf82c0ad68dbf9f1c9b4167cf30f5b6e8a5f6f
    role: context
  - path: data/traits/genomics/prophage.yaml
    sha256: ed6392cf2ff78fad8f572cd734afe14ae2875e796ca4ec7398eec3c3c968c121
    role: context
  - path: data/traits/genomics/prrc_system.yaml
    sha256: 8af2c3e79f80f8f4aac53edc6bc7d80befdba89bb1a94ebd4e9796222f3c03de
    role: context
  - path: data/traits/genomics/psyrta_system.yaml
    sha256: 0ea44932bd5bdc9983bb265ed3c95138ebb9c15f0960dcdd39c43572a41254c9
    role: context
  - path: data/traits/genomics/pvurts1i_system.yaml
    sha256: 1a5c831bf74ce82baf10f5da968da555d34d8baebf4d70554d26a3da96bb6f0b
    role: context
  - path: data/traits/genomics/pycsar_system.yaml
    sha256: 970431c93125c39c1cca11df3a8f6cf1b8f21ac6dac78ec057b14dc3b7460c9f
    role: context
  - path: data/traits/genomics/radar_system.yaml
    sha256: d3503a373ece5728b4aeb65fb288a5a32d28d4700036541b4d91073fecb94c87
    role: context
  - path: data/traits/genomics/razr_system.yaml
    sha256: 41c206a9eb9040b76b8783e72e3896269342df1df7baaa708436f99fad58f54f
    role: context
  - path: data/traits/genomics/resolvase_duf5677_system.yaml
    sha256: 0608af75cf8512bb103550d68d0225c9ae88350cea8a0ab2807b8aa32bc67475
    role: context
  - path: data/traits/genomics/resolvase_kap_ntpase_system.yaml
    sha256: f99e7d80b32bacf61ece9b21ed56656b13d678874c762b0d4e10581a3756a646
    role: context
  - path: data/traits/genomics/resolvase_schlafen_system.yaml
    sha256: da0859d7548b97d853a2691730696a2d85130ad37841c9c2e9074100d8e2497d
    role: context
  - path: data/traits/genomics/restriction_modification_system.yaml
    sha256: 64248b0295c9339aad7c18332b2bdc7795836359b981f5e51b13518f64dbcca9
    role: context
  - path: data/traits/genomics/retron_system.yaml
    sha256: acc132f5e715d383a83fbdb9b38065ad66ac9a8bbdd2e2cb00c9ba73e7fd09ab
    role: context
  - path: data/traits/genomics/reve_system.yaml
    sha256: 9bbc5e1139d450659083fc1712a0813bbcbb138aa71d63e2b4904ec7697b595a
    role: context
  - path: data/traits/genomics/rexab_system.yaml
    sha256: 0d4753908d3dca76ff760b254100cf5fc3dc262d6eacb887396d75ebba59418b
    role: context
  - path: data/traits/genomics/rhea_system.yaml
    sha256: a3baf947abefcffa373c9d4aa9290b03c169e9a58ef8a86be2cebd72ab4a869c
    role: context
  - path: data/traits/genomics/rloc_system.yaml
    sha256: 156bb7d8c8eb35e35409e9d737f15fd61fd031f4b5d907103370b6c05e291700
    role: context
  - path: data/traits/genomics/rnlab_system.yaml
    sha256: 50502ee1a7faed77b22b1333040548d7be4e3ac942e454207acffad0812c30a8
    role: context
  - path: data/traits/genomics/rosmerta_system.yaml
    sha256: 584756f418d2b008afa9b0d347a2e32187150cc8f341ea00651dbe73c4d9741b
    role: context
  - path: data/traits/genomics/rrna_operon_copy_number.yaml
    sha256: 18ba873b020cf7419d69ea68ab58eb9a36ec8f7cab19d9dd25169cf501339395
    role: context
  - path: data/traits/genomics/rst_2tm_1tm_tir_system.yaml
    sha256: 6adc9f35eb7f490749801d7cd225076c0e4382d0fb58add6feccaf714a13c062
    role: context
  - path: data/traits/genomics/rst_3hp_system.yaml
    sha256: f92672cd17b4df036185dfff658cd4dc5ab12f63750bc817212c1355f3567758
    role: context
  - path: data/traits/genomics/rst_duf4238_system.yaml
    sha256: 9386bce8625dbc39d527f1ef8ab9bbf9880b274f145b82195adf6e83b952caee
    role: context
  - path: data/traits/genomics/rst_gop_beta_cll_system.yaml
    sha256: c91b5632aa456d4980ca4fd6d0527d4ce2782723bf06cf0407d0105517008f97
    role: context
  - path: data/traits/genomics/rst_helicaseduf2290_system.yaml
    sha256: 5d2de1f2cd5ea724ddb3aa969db7f857287556e958929c239fc7f20b4462e6c9
    role: context
  - path: data/traits/genomics/rst_hydrolase_3tm_system.yaml
    sha256: 7ae9dbd78e05d63080af8dc614e6599bbd0a502e9d8ed1c37294d1342991115d
    role: context
  - path: data/traits/genomics/rst_rt_nitrilase_tm_system.yaml
    sha256: 8dc8ea9466d6d2586f855ef4cede3e8e8dd8107e8dc54d335942f4a53d701c85
    role: context
  - path: data/traits/genomics/rst_tir_nlr_system.yaml
    sha256: 4e8be6cc4c111bb24443352b8725c7fe6309e46a84a4a33d454811653bdb1b52
    role: context
  - path: data/traits/genomics/rugutis_system.yaml
    sha256: 3673ab58634623e02c9a042de8949c1760f4b068374fc5602e7b64aa68837171
    role: context
  - path: data/traits/genomics/sanata_system.yaml
    sha256: 5b4863d0e3de1b2b2df01dfc384b62458104e13adb9133fe8057b9c03402ce90
    role: context
  - path: data/traits/genomics/scomcra_system.yaml
    sha256: 4ab71e616b032db532a4f9eae99141fc2c4b83bc0b9466ceda175fc986c1f08f
    role: context
  - path: data/traits/genomics/sdic1_system.yaml
    sha256: d2f22197062705e49e9a2b294e7697ba83a64c357c2c6307cbafa6ea9021582c
    role: context
  - path: data/traits/genomics/sdic3_system.yaml
    sha256: 2ae819b1a25f182617bb7334b72a95c89b8277ba2c77bc8fff373018b0e293b4
    role: context
  - path: data/traits/genomics/sdic4_system.yaml
    sha256: 75cee2c50c0406e9d342b1797c4a26f1c03ac65c88d855ee5b6a14de2226ae94
    role: context
  - path: data/traits/genomics/sefir_system.yaml
    sha256: 6277c33fad2f8fa444a1303c39bc5fe91dc0b7c4faee5411705358aff5c14530
    role: context
  - path: data/traits/genomics/septu_system.yaml
    sha256: c0fb9b28f979c8ec9ac255ca6c0f3b0e59c4d30a482736b56b7692fc9e0d53f6
    role: context
  - path: data/traits/genomics/shango_system.yaml
    sha256: 303df378e21e8693447c3577eee428fb4451c499ed6e76b931d591f076b2cdcb
    role: context
  - path: data/traits/genomics/shedu_system.yaml
    sha256: 9df952041b86a4f29889901094b6053598779c97bc66b99279b5b4d8e31c002c
    role: context
  - path: data/traits/genomics/short_lamassu_system.yaml
    sha256: a7e9855de50259220ec0481eaa6f8e137318acf02e120c75df9b6a519a190a86
    role: context
  - path: data/traits/genomics/shosta_system.yaml
    sha256: 4db93a25e95d0729744ac5b64543405157f4a8910024b21b832fb7083f5f75fe
    role: context
  - path: data/traits/genomics/sirona_system.yaml
    sha256: c22c11b75e1b22b4d61e156a5469e433437deae80857907b6ff74c7637f0fbf5
    role: context
  - path: data/traits/genomics/six_a_mbl_system.yaml
    sha256: 2f126f5a57c8b04aa18a637dc3487b72efe4af6016ee7aec7ff0d956af449d73
    role: context
  - path: data/traits/genomics/snipe_system.yaml
    sha256: 70df2cbb86e06fe7f2346211c4ed5a476a22f0fd8cbe8057ebf206b9b2e71102
    role: context
  - path: data/traits/genomics/sofic_system.yaml
    sha256: c5383269efeaf368e590997cc935c19900e2b59d5e6629221e5693afc2836205
    role: context
  - path: data/traits/genomics/sparta_system.yaml
    sha256: 7e65bc7e375cd2de080b206caddcb535f91e926c325b55bbe1b71a29f4c0a843
    role: context
  - path: data/traits/genomics/spbk_system.yaml
    sha256: 163532c7f75063ac9936f69dc6b497c74f647cfeb66c9c9d5b987eba353de8eb
    role: context
  - path: data/traits/genomics/sspabcd_sspe_system.yaml
    sha256: b2831d6666b4f4e003e2939d6e978c3e85365b96aa5b57a94e28176fde1dd9fb
    role: context
  - path: data/traits/genomics/sspabcd_sspfgh_system.yaml
    sha256: 3c6a7b9c8ad01b783a714ad4b3ec670615922f60b00071ab08a79c592f6acd0b
    role: context
  - path: data/traits/genomics/stk2_system.yaml
    sha256: 5f640f3ca935698c08b16504439202e0b783473d787532e28dac586b91b9278b
    role: context
  - path: data/traits/genomics/sucellos_system.yaml
    sha256: e844f9c8d6a5937cb7f8f627f2284ee4094699de7d85e6ca03b80c8a4db685b8
    role: context
  - path: data/traits/genomics/tab_system.yaml
    sha256: daab000263cc58ac4ff4772914dee0a7ba89b3bdde7530289486685e31538322
    role: context
  - path: data/traits/genomics/tagi_system.yaml
    sha256: cfaf6f1e9bf31c8b01207c3ec3a8eb5eea5ecc609f89d6a2186275bbf6138a46
    role: context
  - path: data/traits/genomics/taranis_system.yaml
    sha256: 2d85758a810c62f58ba4381ac651d003b0f69dcb658b3a34422112fda0b28b2d
    role: context
  - path: data/traits/genomics/tgvab_system.yaml
    sha256: 96dd203a8eb1bb6e44a08fdf8e9f87277a214df26a5ce0fd6483eda72edf3d3c
    role: context
  - path: data/traits/genomics/tha_system.yaml
    sha256: f62dab569dd80807293b376c9cc86bffca958578f30c0e3610e968ec0086c9c4
    role: context
  - path: data/traits/genomics/thoeris_system.yaml
    sha256: 579806cc0c34050f958ea716d7ce7aa3870445f6d43e561bf5efca3a6942ef29
    role: context
  - path: data/traits/genomics/tiamat_system.yaml
    sha256: 56a738da9dd5e88afa6b49a7fe6cebd7d4a9a6e83c837911bac6f1482dcfc96c
    role: context
  - path: data/traits/genomics/tir_i_system.yaml
    sha256: 21214f091907d4a748dc949335f69bfcdd6d644043668b19b43109b337ce4ca1
    role: context
  - path: data/traits/genomics/tir_iii_system.yaml
    sha256: 564e1dece4d01c65ced2f16922f70983c1426b4a555751fa4f70abed40f547e3
    role: context
  - path: data/traits/genomics/tir_iv_system.yaml
    sha256: 5e94b95be395f8986b06fa505c8d4d407f4275b9b9c2800c02eda759d8db6f7d
    role: context
  - path: data/traits/genomics/tir_vii_system.yaml
    sha256: 0308ac75368bf5a9e7894f6ecfbe937f04f28f433073efdcc262e897d6947fdd
    role: context
  - path: data/traits/genomics/tir_viii_system.yaml
    sha256: c922fd81578b8d95d110082505453ac74b68c771e553f0599d00e68dc5c1b7cd
    role: context
  - path: data/traits/genomics/toga_system.yaml
    sha256: 273e044a5825d27805d7458f5ca105da05dda19a5d0778d303b1061eafbc18b7
    role: context
  - path: data/traits/genomics/toutatis_system.yaml
    sha256: c32a94e11f04e77b29dd5c3493ca8f62e6ae653f755f404001977f8f08dcf94b
    role: context
  - path: data/traits/genomics/toxin_system.yaml
    sha256: 91834cdee0678a71caa317b043d5dd22e76dcfcec63d7fe7eb97d10150be698a
    role: context
  - path: data/traits/genomics/transposable_element.yaml
    sha256: 25ecf253ff53d5ac847e11beb59651d6835f19b85b455d107bed4bf18fecb070
    role: context
  - path: data/traits/genomics/type_i_restriction_modification_system.yaml
    sha256: 3685bdbc500152278f2555116870a112fc1705e8d0b6ee0cb4c829a008d08e23
    role: context
  - path: data/traits/genomics/type_ii_restriction_modification_system.yaml
    sha256: 68d8e77b8091bfae1f8500a8041181154ce4b6f2f6d63230fcfa6aca9ed36559
    role: context
  - path: data/traits/genomics/type_iig_restriction_modification_system.yaml
    sha256: dce77865dd26114d2683ba827d0dd603f7becd0c8004c0f72c59b62458a85391
    role: context
  - path: data/traits/genomics/type_iii_restriction_modification_system.yaml
    sha256: 03a2e8f6b8acbfee0339bb4971e22d4f0f0611ff4ac073d1c235231f38db3509
    role: context
  - path: data/traits/genomics/type_iv_modification_dependent_restriction_system.yaml
    sha256: 6ca1de118cdf61f7621d72efecc8a47fe8d281fb167258bf47b7eb9b85ad9685
    role: context
  - path: data/traits/genomics/ukko_system.yaml
    sha256: 0a5e156c4fbd2593c33a8e50e305ac81b88503e67fca64359e15b81a858ffb9d
    role: context
  - path: data/traits/genomics/uzume_system.yaml
    sha256: 3d6fc2852e3f3a5a405dfde998452c2891293afee3cf7e3df9670b8624c8c11b
    role: context
  - path: data/traits/genomics/vcam4i_system.yaml
    sha256: 3b117c18428a46459fd6e9a36f2ead174ef39a8897b091691bafe38a6fe0e4f0
    role: context
  - path: data/traits/genomics/veles_system.yaml
    sha256: fb309ceb5f41cff36ae6b262369476b853b26a0f35eeca03a7824242818762e5
    role: context
  - path: data/traits/genomics/viperin_system.yaml
    sha256: c827ee964ae2dae05db3ee3b05433ec2dc4b6708c7079beff17a90dd2b4ba297
    role: context
  - path: data/traits/genomics/vp1796_system.yaml
    sha256: 23d8ca1a12492a3241241819aab78547bfa5e19e4154af2066e4494d247f1a50
    role: context
  - path: data/traits/genomics/vp1817_system.yaml
    sha256: 897f7bb8d9245a6798fd089a9ab0aa902a5a57c114988dd9a9d96dbcf7f9cce7
    role: context
  - path: data/traits/genomics/vp1823_system.yaml
    sha256: e4a4c750559da0329bc09af7f16e11e4f73bbb2254b13ffc6fe9c9bde0cfd22c
    role: context
  - path: data/traits/genomics/vp1826_system.yaml
    sha256: 1d4f16a78743d74890359a08f13a9fe61ac84a92febe520520049c7893fc91fe
    role: context
  - path: data/traits/genomics/vp1839_system.yaml
    sha256: 525d5263b1677fc52c91f30b37bf9c4e78a832f44aedbac294302124e21965af
    role: context
  - path: data/traits/genomics/vp1840_system.yaml
    sha256: 00b5017481927a4daa8fe5c1cbdffff627c349608e7706beee2b5bfb80df0880
    role: context
  - path: data/traits/genomics/vp1848_system.yaml
    sha256: 205b088f86f68a8316fe882c32d3a9e759bcb4822963962ba42287060d098322
    role: context
  - path: data/traits/genomics/vp1851_system.yaml
    sha256: 41a197db8c536214245a0a47d91d791efceabf6c3b323197d24a4ccb49ed2f2d
    role: context
  - path: data/traits/genomics/vp1853_system.yaml
    sha256: b81b3e869b3fe5000df0328e692a3dc4897a9f8e30efd053a8a582beaccd9d85
    role: context
  - path: data/traits/genomics/wadjet_system.yaml
    sha256: 204fa72a8d5648a60a0308ed7a8da1b45c9b672f3e225d8fa37d5603250b400c
    role: context
  - path: data/traits/genomics/zorya_system.yaml
    sha256: 4c4f3cfaf886a83b173aac64cc89f6545abdb8ef80494ff0f0f2bb297ef74b6a
    role: context
  - path: data/traits/genomics/zorya_type_i_system.yaml
    sha256: a1281526bbf44fc4cedd108d153db3798ac49b595f4c73564e7e7ef1225b5175
    role: context
  - path: data/traits/genomics/zorya_type_ii_system.yaml
    sha256: bb108cc165416f408832d4bdf3f4f584a21e0aaafb5e6316929293c6e4f567e2
    role: context
  - path: data/traits/genomics/zorya_type_iii_system.yaml
    sha256: 14989f4df55866261132114a31ae7b7743ca4609a059c868aacb2a6127ae5ec3
    role: context
  - path: data/traits/metabolism/accumulates.yaml
    sha256: d6e5fa65a557532bcaacf2702e50b247c9bbdc366d3bdc886836bbfd824be05f
    role: context
  - path: data/traits/metabolism/acetoclastic_methanogenesis.yaml
    sha256: e9da2ab8799ddeb56c6bfb1f02deb377945e4968ea1004460284381e95173346
    role: context
  - path: data/traits/metabolism/acetogenesis.yaml
    sha256: 205bdb945eb97d0c824367a08598a304cbd45940984d4fc400da60ad34f7e033
    role: context
  - path: data/traits/metabolism/acetone_butanol_ethanol_fermentation.yaml
    sha256: 05b7d4b439b06a5d593e8902a57d6d53fbe76933b85837e4bfb60766290a6c15
    role: context
  - path: data/traits/metabolism/aerobic_respiration.yaml
    sha256: 44848504809996f11e36036212a7345935056e0e1e4406ba456a2ddb30b8e482
    role: context
  - path: data/traits/metabolism/anaerobic_ammonium_oxidation.yaml
    sha256: ca25c9f3e10ccad967e4533f9b9a58d8cda52b6bd73d19962413f75bb5ef8671
    role: context
  - path: data/traits/metabolism/anaerobic_oxidation_of_methane.yaml
    sha256: e4defc8fddab496e6aedea62fec4a64eb8ffade77856641a3bb03e5d7c73cee1
    role: context
  - path: data/traits/metabolism/anaerobic_respiration.yaml
    sha256: a11d1f7561951a2bc5c96602c17c7f8212ae8298d702d2615d2dc8bc82099fea
    role: context
  - path: data/traits/metabolism/anoxygenic_photosynthesis.yaml
    sha256: 789bbf08a9917d03048898fe3584d2668ba4d3cabb04294459c2b8bc3d77596b
    role: context
  - path: data/traits/metabolism/aromatic_compound_degradation.yaml
    sha256: db7d025a61a0c8a84b9afdbd306e37fbaa6a79924229ae49c3153021f00a084d
    role: context
  - path: data/traits/metabolism/aromatic_hydrocarbon_degradation.yaml
    sha256: d0a29fad048bef22ba157ab0ca272ea1b4cfe832e4a646cdbfe0a5c05d25e849
    role: context
  - path: data/traits/metabolism/arsenate_respiration.yaml
    sha256: b192fb4ce85059dfd2bb26997ca60697f35c54b9429e0589a9a2da7176c57781
    role: context
  - path: data/traits/metabolism/arsenite_oxidation.yaml
    sha256: 165e50989bd8040dae587742a98936902af7b92d86d8e3bd1c9b5fd46232cbdb
    role: context
  - path: data/traits/metabolism/assimilates.yaml
    sha256: 6b2048d0c8b7c4fa15a38e04b81647aa5e85cd68fd89c445ab43c8644a710529
    role: context
  - path: data/traits/metabolism/biopolymer_degradation.yaml
    sha256: 96456515c2866c328ad1c10486b5bb6d076cbb51df442a57c812e36b3854cadb
    role: context
  - path: data/traits/metabolism/builds_acid_from.yaml
    sha256: 63e31fc6731a61afc95760566cd65cd354fc6b959c648a07a0c2d6904344ba50
    role: context
  - path: data/traits/metabolism/builds_base_from.yaml
    sha256: 3b09c3e816428b09b9f1702982b62f89632aacb1a9ed80c2d2627126e5c72b70
    role: context
  - path: data/traits/metabolism/builds_gas_from.yaml
    sha256: 43917275c0b96a3685ecc91586ddc2447fb91f31acf7280bbb241bbe18d4d0aa
    role: context
  - path: data/traits/metabolism/butanediol_fermentation.yaml
    sha256: 5b92451a9348f27301c5754ba67c3e211420b78cd9f4ddc80e955483d63ca73e
    role: context
  - path: data/traits/metabolism/butyric_acid_fermentation.yaml
    sha256: c34b3627fa305470695bbdaa9b0fe113cb9e3d6ee1ddc9628c5cb874f57fe479
    role: context
  - path: data/traits/metabolism/cable_bacteria_metabolism.yaml
    sha256: f30709637dce4edcb237a83c9e41e6e213c2dd169b9c174ed6f2f7efdd550550
    role: context
  - path: data/traits/metabolism/calvin_benson_bassham_cycle.yaml
    sha256: 8037067e8c05f3489de5425be62a118817c9afd1debd54e31b44dd32b121318b
    role: context
  - path: data/traits/metabolism/capable_of.yaml
    sha256: 0fa60bb5a6939a16487936d8d3a33278d13cfebfd24f4697f8c8b05870f11f0f
    role: context
  - path: data/traits/metabolism/carbon_fixation.yaml
    sha256: ace76f1492ebc1759c2623fdb9543d3edf4dc6d9d9696a9094a6ddb408d33979
    role: context
  - path: data/traits/metabolism/cellulolysis.yaml
    sha256: 10d40e341d1a3b283eb0612f82d11b712c199bdb1ba9b1340bcefd62983bfe79
    role: context
  - path: data/traits/metabolism/chitinolysis.yaml
    sha256: b8250664cb24f248f14c370c35377cf7c313876738b1a9976be3275b938d94e2
    role: context
  - path: data/traits/metabolism/chlorate_respiration.yaml
    sha256: 50102421f9a3e109ec9c77c82ee80cb0f9a6d4ca0c5297e0ac97ee01ce74f011
    role: context
  - path: data/traits/metabolism/citrate_fermentation.yaml
    sha256: 7e0f0492ffd5fc13cb68ec0a9afdf9ac0f017c60af7f65978754773e66944752
    role: context
  - path: data/traits/metabolism/compartmentalizes.yaml
    sha256: a3ac4dc67a80998ff008757c82c3edc9642430c50cd77642ac099c4743ca8dc7
    role: context
  - path: data/traits/metabolism/complete_ammonia_oxidation.yaml
    sha256: 3a62bf1de845e11fc738686d39f00b618c1fafb25cc0a8d21f9755250a0b0e90
    role: context
  - path: data/traits/metabolism/dark_hydrogen_oxidation.yaml
    sha256: ad887ad5f0ad65eada14811c87131947cff8e6c281498e11009d3e959e9aec70
    role: context
  - path: data/traits/metabolism/dark_oxidation_of_sulfur_compounds.yaml
    sha256: 89b05104a6e1f47a69595c1a07689d36c16b578bfdbfdf85b689b048565e9d9a
    role: context
  - path: data/traits/metabolism/degrades.yaml
    sha256: 967a2aa8edebbc5a91e2d6c378c7cc4ad03904c2cf98988f3419c591b6715ca8
    role: context
  - path: data/traits/metabolism/denitrification.yaml
    sha256: 81d81d128d269f6b864966e2e9f3db34d704bc83335b2df9cee80684ace7ccaf
    role: context
  - path: data/traits/metabolism/dicarboxylate_four_hydroxybutyrate_cycle.yaml
    sha256: b30db7d13c099842c9046ea51fae958df0857c493a8373f3e28793c1e0069ac1
    role: context
  - path: data/traits/metabolism/dimethyl_sulfoxide_respiration.yaml
    sha256: 04b955947811e26a3a96e3451709d195deeb0694c90d9d15004d763f94eaccb3
    role: context
  - path: data/traits/metabolism/disproportionates.yaml
    sha256: fe7545d98079437d03cbe5f9585da542bf0e484a7a013525f61279c14ae69e9e
    role: context
  - path: data/traits/metabolism/disproportionation.yaml
    sha256: f53b44743ff3630f699d50243a9dbc7a1f18325585725f7f63adaf92a1cf0378
    role: context
  - path: data/traits/metabolism/dissimilatory_iron_reduction.yaml
    sha256: e81cb257a8caa7219a63bf8ba04d0b595d70a85634f8fba77e0a3c16eaf5fa6e
    role: context
  - path: data/traits/metabolism/dissimilatory_manganese_reduction.yaml
    sha256: 6132ea6f2b13704e74de02bc8f6c7b2f943cd43733649d9e8f28fddddecd724c
    role: context
  - path: data/traits/metabolism/dissimilatory_metal_reduction.yaml
    sha256: f7802f40c2850871b1b1ea574d3d30e13358c28cc3f32356b90e8d4093beb65a
    role: context
  - path: data/traits/metabolism/dissimilatory_nitrate_reduction_to_ammonium.yaml
    sha256: 8ae952dad8af376036e96373ca0c913c58dd48e4b68c7fef2677da2448debf1f
    role: context
  - path: data/traits/metabolism/dissimilatory_sulfate_reduction.yaml
    sha256: 40590737fa1d21f476292b4415ceb6c99fdf1059dbf2a200a2a90f9ec661b1ad
    role: context
  - path: data/traits/metabolism/does_not_accumulate.yaml
    sha256: 79677593fc5ee5ef95f2015cc9a50af2f220953e84e00105445f2720af7e214c
    role: context
  - path: data/traits/metabolism/does_not_assimilate.yaml
    sha256: c14b6bd9f69d8eeb5f11648ae5f18cd4a8823d6aaadfa8fbf3e35c68e4a04765
    role: context
  - path: data/traits/metabolism/does_not_build_acid_from.yaml
    sha256: 55e49692c9db045ec8517578cdb494014d531eb9692390023cb5616dbf8941e6
    role: context
  - path: data/traits/metabolism/does_not_build_base_from.yaml
    sha256: f20724ca371588278653ad8486894dafabfee55e54b5f0189a445a871add3631
    role: context
  - path: data/traits/metabolism/does_not_build_gas_from.yaml
    sha256: a8e3b5eb1a64222dad40c27a6cf33218a9e01a3cf275defa154870fb00fc587b
    role: context
  - path: data/traits/metabolism/does_not_compartmentalize.yaml
    sha256: 3a1467edd3605861ab51b6210c98183fbc9eb18c04035d5001137df01b574284
    role: context
  - path: data/traits/metabolism/does_not_degrade.yaml
    sha256: 2584006bf77cd2218bab81100c08f80856a4835a4f0a30383a281089a9bf245b
    role: context
  - path: data/traits/metabolism/does_not_disproportionate.yaml
    sha256: a101b8bedbd417811a3ae45d5381e39de17940665876be308014199caf061199
    role: context
  - path: data/traits/metabolism/does_not_export.yaml
    sha256: 71067c027cfcf4334c613e4ea34244c7879587e97577aaba974f794917886f8f
    role: context
  - path: data/traits/metabolism/does_not_ferment.yaml
    sha256: a7e567a9d3382833bbc90406541bf7552f1ccabe69e981ae19e31f0b0f884305
    role: context
  - path: data/traits/metabolism/does_not_hydrolyze.yaml
    sha256: 40b9bae8d2253f88572a427c47185d7ccc7f15f3b7d28db9849147c39837a7ca
    role: context
  - path: data/traits/metabolism/does_not_import.yaml
    sha256: 98440f9d954b35200df7dbb301f32422289c9fcf26f9e8e4e644f00141935c36
    role: context
  - path: data/traits/metabolism/does_not_oxidize.yaml
    sha256: 47c8bf4b6422609e48adf985def1b09431fe6e35f85d5f203726f253e0e33302
    role: context
  - path: data/traits/metabolism/does_not_produce.yaml
    sha256: d81d2981d4c7eaa17c5a834eb0b4fe9c5aec4c41749da9776913c4bb08c26c27
    role: context
  - path: data/traits/metabolism/does_not_reduce.yaml
    sha256: 63e90b4efec9adec8751b1dffbf7e511e4a668476e951eee0522fbe4d4de0acc
    role: context
  - path: data/traits/metabolism/does_not_sequester.yaml
    sha256: 885e3457826daea8f5c90de57845ea5c2d6f2fb7ecd7b63687d30facc4e41181
    role: context
  - path: data/traits/metabolism/does_not_show_activity_of.yaml
    sha256: 7a5b9ca5c1608435dae4c487fbdc1ac9cc16d1cb3e7cca8d14460cd7560fb665
    role: context
  - path: data/traits/metabolism/does_not_transport.yaml
    sha256: 4ddba20b0e06e7727c5ee22f9083f4e98548fb8f042b9ac91b6597f3276a5007
    role: context
  - path: data/traits/metabolism/does_not_use_as_carbon_source.yaml
    sha256: 5a83c77e701aab153f0d4dc891d284372fa0d35c1b2d99448fb9b06e7dfcdac0
    role: context
  - path: data/traits/metabolism/does_not_use_as_electron_acceptor.yaml
    sha256: cd39a8ac147cf347f39e0487627b94adc7b6b6050c8e4da57676e3fff328ce8d
    role: context
  - path: data/traits/metabolism/does_not_use_as_electron_donor.yaml
    sha256: e5ce526a2572446152db31c72a3786f640bc6ab4bae8ba012e1853919858b507
    role: context
  - path: data/traits/metabolism/does_not_use_as_energy_source.yaml
    sha256: 86037f3f49096af61eb6ef53812ced9d0fce18d277231d219005ccea8a552faa
    role: context
  - path: data/traits/metabolism/does_not_use_as_nitrogen_source.yaml
    sha256: 6d43793d4be6d25c78859107f310cb1b69774e33eb5fab7f9bcd05acf381e86e
    role: context
  - path: data/traits/metabolism/does_not_use_as_sulfur_source.yaml
    sha256: 57e58f4dd74b297300540cdc757870cf2b53d47d0cee4b2902d071e644f35476
    role: context
  - path: data/traits/metabolism/does_not_use_for_aerobic_catabolization.yaml
    sha256: d32cdbcfd43743b502a20a2f3827dc1783b441258d2466f2b54cca0596827c3b
    role: context
  - path: data/traits/metabolism/does_not_use_for_aerobic_growth.yaml
    sha256: fac582abda2e19d68271515e74de7d3e632e73b1e0f2cca6bd37205929de1d11
    role: context
  - path: data/traits/metabolism/does_not_use_for_anaerobic_catabolization.yaml
    sha256: 9264cfeb2644911af116805feed3bb587ec6ecd68b75fadd27a03188a6743343
    role: context
  - path: data/traits/metabolism/does_not_use_for_anaerobic_growth.yaml
    sha256: be09bf3e7a573c18691e5a28d1e0eaeb5a4f0aa0dc5e2fbd43b86f5bc50bb4d8
    role: context
  - path: data/traits/metabolism/does_not_use_for_anaerobic_growth_in_the_dark.yaml
    sha256: 042f5c0069eafd8fd704a6acd76eb3658470bc06ac5c2c9833a2f73b95c1f8d4
    role: context
  - path: data/traits/metabolism/does_not_use_for_anaerobic_growth_with_light.yaml
    sha256: 0042eede1b6e2a01064cb239186e951897d06a3e9bf48489c2f2ac4bedc9c40d
    role: context
  - path: data/traits/metabolism/does_not_use_for_growth.yaml
    sha256: 46e1ffbd8890fec4f0e8ef4bce64cb7b373c1eb2493d42a23051e9707a34052f
    role: context
  - path: data/traits/metabolism/does_not_use_for_respiration.yaml
    sha256: 01b486cf7c3129600dc64d275982e875156d47fe60ed8f383489b2605296df61
    role: context
  - path: data/traits/metabolism/does_not_use_in_other_way.yaml
    sha256: f24aab3d7a03cea1d6a38d063a124df8bf8ff0e51a87e5cffe61fc08acef38f6
    role: context
  - path: data/traits/metabolism/electron_transfer.yaml
    sha256: 42b84f932a36b8d30c7c265d57ba59904f6c677f84f7199a06e1f4ca7f1f3820
    role: context
  - path: data/traits/metabolism/enzyme_activity_analyzed.yaml
    sha256: c338148cea98034b5d4f8f6c23d0c9a503736f4de42e1735c448747ae622e484
    role: context
  - path: data/traits/metabolism/ethanol_fermentation.yaml
    sha256: ad65836e4e31389358cd19fcf5b76ea7b3c9e0f151776cc11eaa3bf84178f855
    role: context
  - path: data/traits/metabolism/exports.yaml
    sha256: 21bd92ac6e2c5d56c9ce3e4b93027cd75b3228615e5dea95b9dee8e7a8af7005
    role: context
  - path: data/traits/metabolism/fermentation.yaml
    sha256: e02a622757b033dac2d1df9829a0cca9de9fddc4e9d1bb4db294738cea6f3efe
    role: context
  - path: data/traits/metabolism/fermentative_hydrogen_production.yaml
    sha256: dc0fb33e6af6050df76fb657b7982e1fe0924e659a982ec40c775f2aae50d584
    role: context
  - path: data/traits/metabolism/ferments.yaml
    sha256: 410e8f9cc453925db6d4da69ee95ceac9685bab92df2472099b414ee03938e4f
    role: context
  - path: data/traits/metabolism/fumarate_respiration.yaml
    sha256: 2df908706d702e6e54625f7b5f7cc1b268f10854887758f962cd2cf5aa3a800f
    role: context
  - path: data/traits/metabolism/has_growth_nacl_observation.yaml
    sha256: 9c066c29ede737a6017eb0cda6265835417065a3eb7714380d596d935e2748b5
    role: context
  - path: data/traits/metabolism/has_growth_oxygen_observation.yaml
    sha256: 6c3f3fe76c3dfcdc9cd3de2ef95a1840566d40273daffcc2a2a0a5e82fd51c4a
    role: context
  - path: data/traits/metabolism/has_growth_ph_observation.yaml
    sha256: 5dc6261743ce8a7b9e05543c7bd50caead263616a6b507d5e38d487b3df2721b
    role: context
  - path: data/traits/metabolism/has_growth_temperature_observation.yaml
    sha256: 262f26f4aec92969c5ebc05fa952ed2bf3c4d8da89dfe3e8a27680ff629baf80
    role: context
  - path: data/traits/metabolism/has_nacl_delta_observation.yaml
    sha256: d3375b89f9af58d408edb5d9d091162f716e8004ea8c62b68486dc3fa9ddac68
    role: context
  - path: data/traits/metabolism/has_nacl_observation.yaml
    sha256: 1c5fcd23ec84309267515a6a6bd0984c95276b952375d90318a76029360b95d7
    role: context
  - path: data/traits/metabolism/has_observation.yaml
    sha256: 88cba9b3e0ece41e5ab542bbb768af4593205196b194c82db0a2c1f3e40148d5
    role: context
  - path: data/traits/metabolism/has_optimum_nacl_observation.yaml
    sha256: 9f9f3c908406f8fac2064e54a448a2d7b39a57b77eea953a28550959cbed2b20
    role: context
  - path: data/traits/metabolism/has_optimum_oxygen_observation.yaml
    sha256: f064bad25008cc0c0811426c9f4027ddd5503dbc855186e5a31d4ac2129aa52c
    role: context
  - path: data/traits/metabolism/has_optimum_ph_observation.yaml
    sha256: a65a5b47f0b745a4a40fa51b9674c53923d0f32285b043f9a0d9a9225ca902fb
    role: context
  - path: data/traits/metabolism/has_optimum_temperature_observation.yaml
    sha256: cf275de74b96d2077eba690ae7f4257639d41e4f9cdaad4811352e93a66a6d31
    role: context
  - path: data/traits/metabolism/has_oxygen_delta_observation.yaml
    sha256: 1a8c26d145bfa2d8b1e36c3084fbfb71c83e846094d372858dbd04cbf3e15d17
    role: context
  - path: data/traits/metabolism/has_oxygen_observation.yaml
    sha256: 8d4be962de56ab8d862def9e16b946ae876b8cd7e588505cdfe2c003df9dfd1e
    role: context
  - path: data/traits/metabolism/has_ph_delta_observation.yaml
    sha256: df87fa98eadb9c0940b143fb02a9c350cfe1ec2580179c4207e312feb6794056
    role: context
  - path: data/traits/metabolism/has_ph_observation.yaml
    sha256: 73e5fb59ddc972294f3f46b816162c403c3c131a302884c072c1466b64c36021
    role: context
  - path: data/traits/metabolism/has_phenotype.yaml
    sha256: 02289ec9093bae2d08afdd9d2f8d97ec36ea3d40e9c8c7a1e4435176a5f579d9
    role: context
  - path: data/traits/metabolism/has_quality.yaml
    sha256: 7421df8d387b066c098461c3e0d917127042de95e927f421580ce0cb3edc026c
    role: context
  - path: data/traits/metabolism/has_range_nacl_observation.yaml
    sha256: 294f1576e640327160f8313c158f347b6e36ffd5e3aeada77c9601e95042250c
    role: context
  - path: data/traits/metabolism/has_range_oxygen_observation.yaml
    sha256: 9ac6d5a4e722664cb1dd9bfea957fffe6477d1fe0930b858083fd4f7fe82e739
    role: context
  - path: data/traits/metabolism/has_range_ph_observation.yaml
    sha256: e53bc1da3040ede86308598c7aa6ca33b68e46edf7256a2f3e1b258488409cee
    role: context
  - path: data/traits/metabolism/has_range_temperature_observation.yaml
    sha256: 69aca12b091bb4db7fac19ed63da99851725385c408533def15bf46c229459f4
    role: context
  - path: data/traits/metabolism/has_temperature_delta_observation.yaml
    sha256: be71c9544283c4bf5d43d7462edb963e2e633b34ab46cdc42ac857eeef515ee9
    role: context
  - path: data/traits/metabolism/has_temperature_observation.yaml
    sha256: b1bbdbbdb1f212ef1e2ed68dd4515eefc41705894e1fb1bc0f5229fff4b9b9af
    role: context
  - path: data/traits/metabolism/homoacetogenesis.yaml
    sha256: 7cc9bbc3c866babfba8255bcfc5b93544a02cf41af12fab37300aaf4a04dfb75
    role: context
  - path: data/traits/metabolism/hydrocarbon_degradation.yaml
    sha256: 59f4e83c615f35b49be537a475c731d779411d632bbe0dda642c1c4323b98734
    role: context
  - path: data/traits/metabolism/hydrogenotrophic_methanogenesis.yaml
    sha256: b054d8a8cc3b70f4028db5f2d8532071802dc46e02c1f52ff00db01461cdc58e
    role: context
  - path: data/traits/metabolism/hydrolyzes.yaml
    sha256: ff8837550eeb0eb9ce84bf4a5af973c4ca3f1f19b3186f21a1625bbc443fd571
    role: context
  - path: data/traits/metabolism/imports.yaml
    sha256: c2ad9a72fdbb5323f70932cb1b42d891078d6c8fa6f69ce0b7ae98baa2bd5ed1
    role: context
  - path: data/traits/metabolism/iodate_respiration.yaml
    sha256: c9baed93b80fc5a45ae5859ddd9081af51d77177dcf53a27e356f34dcb4e22fb
    role: context
  - path: data/traits/metabolism/iron_oxidation.yaml
    sha256: 4b760c61b3c72c01e8c1bab0a85b7e76d98efb08fb4bf532faea3f8a693db127
    role: context
  - path: data/traits/metabolism/is_not_required_for_growth.yaml
    sha256: 492df92e202406122c49b9490ba01b7b49f24d2a0abd0e0995fd2132384d22e4
    role: context
  - path: data/traits/metabolism/lactic_acid_fermentation.yaml
    sha256: dba6cdf1607eb842faffe9e4c591abf5ef6e072c1f3cfffb5170e030578e7cc8
    role: context
  - path: data/traits/metabolism/lignin_degradation.yaml
    sha256: 1713a83bc39f47a903a0ce34a08f3a2a0923fccb8d745fff03f7c362fbca2551
    role: context
  - path: data/traits/metabolism/lipolysis.yaml
    sha256: 125557336f1363d756f22c017fa62843228f8f8e1340d0546417a48945b2dee8
    role: context
  - path: data/traits/metabolism/manganese_oxidation.yaml
    sha256: 3c0bd68f2e666505e666ee7adb5e2585eca2e098927d482dc9689885a32f1ad2
    role: context
  - path: data/traits/metabolism/metabolism.yaml
    sha256: 070a8620979cc8adb3091cc6eb64ba04ead16475f45e500658d254ef33579d2f
    role: context
  - path: data/traits/metabolism/methanogenesis.yaml
    sha256: ce7a9c43bbbee899bccd675670df63a27eeefb07de2c4d7dac57acc5bf0cb0fa
    role: context
  - path: data/traits/metabolism/methanol_oxidation.yaml
    sha256: e2895b852ace06dfc2e5d02bae6bfeda1d87f00abcec08b82504ac0c5dc10377
    role: context
  - path: data/traits/metabolism/methyl_based_methanogenesis.yaml
    sha256: f5dba22c290fa6f84b31f433b296cad536e82d84a441c9853c9aae439fb077a2
    role: context
  - path: data/traits/metabolism/mixed_acid_fermentation.yaml
    sha256: d053ee03594e8308fe5c0a30a90aa3e7210872696a4e82a35935b42ae896b398
    role: context
  - path: data/traits/metabolism/nitrate_reduction.yaml
    sha256: b3b678fd461c2575e130a0428a1c48fc8e979f7d443542b889c05d30737e360c
    role: context
  - path: data/traits/metabolism/nitrate_respiration.yaml
    sha256: cb919fd2f22f485d7bbb542993e204c431cea2c7bbb9a418fda86ca9c7d35aea
    role: context
  - path: data/traits/metabolism/nitrification.yaml
    sha256: 9870b941334de2f54cfabbc656ab59c204f2a488d26f4651402a9997a17f0f26
    role: context
  - path: data/traits/metabolism/nitrite_respiration.yaml
    sha256: 8c1b82e2a64f78443cfe0497658d0a03dab9545f2b74a512f376e2865a7f84ec
    role: context
  - path: data/traits/metabolism/nitrogen_fixation.yaml
    sha256: b8134eed52124120441efcc16aecb59d1e37bc28bae0688547439c409bd6d68f
    role: context
  - path: data/traits/metabolism/nitrogen_respiration.yaml
    sha256: f52bc38bf8f54a90a623b9ab98fb5f07e9e2acbf4ae2fc5149030108f7b3a9bc
    role: context
  - path: data/traits/metabolism/organism_interacts_with_chemical.yaml
    sha256: 8aff2516a57de3cc6eb53f404b52a7a33db995dc1a4a5a02a1ee1e56eb967b96
    role: context
  - path: data/traits/metabolism/organohalide_respiration.yaml
    sha256: 781a5f38b7ba1940fa853430e1e60228c8a01f1f62c2782b3e0d52a0a1ae1c55
    role: context
  - path: data/traits/metabolism/oxidative_phosphorylation.yaml
    sha256: c85b2955ee86d9405f2a0f00392f56fbf7d8228aaf332807e9f7219bf145d33e
    role: context
  - path: data/traits/metabolism/oxidizes.yaml
    sha256: f443fdef4a1eb2707df70357c63d7d435c0802719234d790b6eca79fb0dc37de
    role: context
  - path: data/traits/metabolism/oxygenic_photosynthesis.yaml
    sha256: 62194e5b04076c1607c9a66890571013d5f239c042ea52e419f280aefaa3eb0d
    role: context
  - path: data/traits/metabolism/pectin_degradation.yaml
    sha256: fdc392de8588d0612ec0705989235e7f5949ef5c9cce09b1aab41e9fd88c63d0
    role: context
  - path: data/traits/metabolism/perchlorate_respiration.yaml
    sha256: 7d52e4a2c8eb273555621609c5a53e83e28047b30496238217080ef617964246
    role: context
  - path: data/traits/metabolism/photoferrotrophy.yaml
    sha256: f6d5a268ad7226b38f0f65dc02025f05b3f28c55ea5c24edc090b8b8f72f0bcc
    role: context
  - path: data/traits/metabolism/photosynthesis.yaml
    sha256: a47048bcfff53493dd6a65b3c0991ba9ee86f3841eb407e31948063045018dbe
    role: context
  - path: data/traits/metabolism/phototrophy.yaml
    sha256: 65a2abba6f246e0dbc7b2ac602cc46c54dab814d0b31ccb6383a004cb074b13f
    role: context
  - path: data/traits/metabolism/produces.yaml
    sha256: 90befb3fda80aa5ea07633171df9eaf26959c367e64f95ca2f0ab35cff1722fa
    role: context
  - path: data/traits/metabolism/propionic_acid_fermentation.yaml
    sha256: 980497f75b13527e04940ae5ada0fd37dd6be55ee057661a4fbc793e02a31585
    role: context
  - path: data/traits/metabolism/proteolysis.yaml
    sha256: 572dd5ea3c150574dace9ccfc4a8eb0f4564aa674bcc8ceae6f10e98da603e46
    role: context
  - path: data/traits/metabolism/proteorhodopsin_phototrophy.yaml
    sha256: 3c7009e19b8eaf3e827a0a087aef48b2f4efc62348ae203534df1610d1b65a95
    role: context
  - path: data/traits/metabolism/reduces.yaml
    sha256: 107334e374ad70a9ebf82e8594228a3099e524389e490e41d9094e05d8f2047c
    role: context
  - path: data/traits/metabolism/reductive_tca_cycle.yaml
    sha256: ca3e0afdfb6fba4f0dddc1c8dd002ea63946747ba296c0d74bb5dca024a0aa7a
    role: context
  - path: data/traits/metabolism/requires_for_growth.yaml
    sha256: e32092569ea21ca544f3eed4bc87d9fc8061370d7a5eb05724e9e2b9b6e79bbc
    role: context
  - path: data/traits/metabolism/respiration.yaml
    sha256: c16d0b76a342fc930c390e3e550e41f68853bbd5fb16839a6b9acb46b7a41445
    role: context
  - path: data/traits/metabolism/respiration_of_sulfur_compounds.yaml
    sha256: 0309e0e7850d59130a5261af0ab7440d01383ab144ee8776c36b080f6301d59b
    role: context
  - path: data/traits/metabolism/selenate_respiration.yaml
    sha256: c8e0d82064894e3fae5651b317d3bd37e947c52707c1489cafbbf492af80dfe8
    role: context
  - path: data/traits/metabolism/sequesters.yaml
    sha256: 4e9cc9d22abc35a5829817e19b16284868e57f5fba90fd71d2c0fe0576ec0258
    role: context
  - path: data/traits/metabolism/shows_activity_of.yaml
    sha256: d3afaf4a9b278f39b9454407b3516ab78348bfe7d801f99f8afc25295ca1d093
    role: context
  - path: data/traits/metabolism/starch_degradation.yaml
    sha256: aa84058bbc36302383a350751692881992f27ad84e7c8c639af12015bb012d41
    role: context
  - path: data/traits/metabolism/substrate_level_phosphorylation.yaml
    sha256: 4c6c59327a770c45db2d517629809d429ad92dd7aa02eecf1adeef95aa83f70d
    role: context
  - path: data/traits/metabolism/sulfur_oxidation.yaml
    sha256: bbd88856b408101974d4d18582e5f64cb8cc1ba6f5a5915a95fe60a0aa0c78d1
    role: context
  - path: data/traits/metabolism/sulfur_respiration.yaml
    sha256: 32f14b22bdc73c2da05374d318faad1b71325a612f542a87a31588404e0330f9
    role: context
  - path: data/traits/metabolism/syntrophy.yaml
    sha256: 7a16c591d9a3f9645f6f5a418163acd556e342e5735184fb3e6188bf5c9e5e08
    role: context
  - path: data/traits/metabolism/tetrathionate_respiration.yaml
    sha256: e928c378696494d2da00a0774895ff586cb290b7f295ee6f04e17eadbecd5c17
    role: context
  - path: data/traits/metabolism/thiosulfate_respiration.yaml
    sha256: f7f894e90b025ce03a56dfec6821882562e53a4a0afe9098921a350f3b1c9071
    role: context
  - path: data/traits/metabolism/three_hydroxypropionate_bicycle.yaml
    sha256: 7879b8de47f9a4611866432142c85b3bd412aafa1b74266a69cf407d4c7c9e24
    role: context
  - path: data/traits/metabolism/three_hydroxypropionate_four_hydroxybutyrate_cycle.yaml
    sha256: 877deb65fb8bfc690bdeceea33c7857a5d4585201b5afd6fe00714c0c1a03d82
    role: context
  - path: data/traits/metabolism/transports.yaml
    sha256: 2341b2e8aa85d60fa9e7d11314c7050aa5991bfef9df8d7b9dd492b714c88491
    role: context
  - path: data/traits/metabolism/trimethylamine_n_oxide_respiration.yaml
    sha256: 98e5512c0cf647329e6c424dc12d01d869a4a4ca228f847b30754ac455675d2f
    role: context
  - path: data/traits/metabolism/uses_as_carbon_source.yaml
    sha256: ac97b016972d92634c14fee787ab5f7dc1dca7ff1ed69873da6d8e5b1de49bc6
    role: context
  - path: data/traits/metabolism/uses_as_electron_acceptor.yaml
    sha256: fa47cc87d5e71f34b492617aa6c4503516148c0b5ff23fd5577c15bf11c436a7
    role: context
  - path: data/traits/metabolism/uses_as_electron_donor.yaml
    sha256: 9ccf703b0a1e11701ac5cf682bd2504f9b413e9e4ba42f78ff490dc9617b13e7
    role: context
  - path: data/traits/metabolism/uses_as_energy_source.yaml
    sha256: ac23b771826ed24ecd6771b2b2bb5efb4520abd132189f25d26afbb15648a689
    role: context
  - path: data/traits/metabolism/uses_as_nitrogen_source.yaml
    sha256: f2004b2fb6c8e6aaf9b1ec559734fa3c29ce9186a77ae8a32682209f0d07e99d
    role: context
  - path: data/traits/metabolism/uses_as_sulfur_source.yaml
    sha256: 1303c4ed24973dc9226cedbb2c2e451c2a08d2ea8e9d233062f04fd1d82eeee0
    role: context
  - path: data/traits/metabolism/uses_for_aerobic_catabolization.yaml
    sha256: b7180e949530dffe6269b6b304539ba5a54c300896064bdda7ef71802e64e1c0
    role: context
  - path: data/traits/metabolism/uses_for_aerobic_growth.yaml
    sha256: bb575651e5a8c6abef9a6ae8758e41118e72a64724ecf1e649360801fa09c39b
    role: context
  - path: data/traits/metabolism/uses_for_anaerobic_catabolization.yaml
    sha256: caf4fb7585711de6f80eb88c21db0744b7ded5b73cbbf77f56500ea2c25eedac
    role: context
  - path: data/traits/metabolism/uses_for_anaerobic_growth.yaml
    sha256: d4b59e0e8a54041a9b96785ef5dc6d87051faa4594b12c2ab63045cccc00b5d7
    role: context
  - path: data/traits/metabolism/uses_for_anaerobic_growth_in_the_dark.yaml
    sha256: 3e58cb91eb67ac76f0c322f6deaa6edb93c36358adb69778b452c4d25d87d6a8
    role: context
  - path: data/traits/metabolism/uses_for_anaerobic_growth_with_light.yaml
    sha256: 9362c51d8388ef7ca0d10468ab285cf2abedbdb6f28284a234a039595c6284dc
    role: context
  - path: data/traits/metabolism/uses_for_growth.yaml
    sha256: 47b73743e32e182ddffd99e1ec3e1d2c8c2562d716580aa5253ef989d17a7cdb
    role: context
  - path: data/traits/metabolism/uses_for_respiration.yaml
    sha256: bbd8e6e2e2a3819bdd412a953356b0bc950a11ec6739cc08bb70681b874e3fe7
    role: context
  - path: data/traits/metabolism/uses_in_other_way.yaml
    sha256: bbdddb80cad436ca4a2187826bd004954055294160fab8edb16759f45b396950
    role: context
  - path: data/traits/metabolism/wood_ljungdahl_pathway.yaml
    sha256: edb5de247572953f0e8ec61e8768be57d8d73b67ed48dea1c5208e9804bc3539
    role: context
  - path: data/traits/metabolism/xylan_degradation.yaml
    sha256: 90460d1496a1ecb2e04ae572067606806aa04d9bf45c2bc107252a7658ca1ce0
    role: context
  - path: data/traits/morphology/akinete.yaml
    sha256: fe282789abcd340ec581c43d6333d3541c4ff0a67724167f2f93aac28e832d1c
    role: context
  - path: data/traits/morphology/amphitrichous.yaml
    sha256: cfaba9d8f756dfccd30e85209b8bbffbd82ed6213d4b54c5d6cb2d5ab0f33abe
    role: context
  - path: data/traits/morphology/axially_filamented.yaml
    sha256: bbfff2a29558906f76ad4f5573eb070fb7e8134f9ec6e0bdba95b788699d434f
    role: context
  - path: data/traits/morphology/bacillus_shaped.yaml
    sha256: 0f5a73de26cd29c35fe234fcf561c7dd31c57f98e6256f54e0e199038d943d2f
    role: context
  - path: data/traits/morphology/baeocyte_formation.yaml
    sha256: c7f30422f83bf2d454fbec1e5aa28d676d243a25676e6acc5ffcbe5e0cdcc578
    role: context
  - path: data/traits/morphology/black_pigmented.yaml
    sha256: f4a75dab414a432188f0732196e17ff5c65db30b5fbb90b24c18473835bbb49e
    role: context
  - path: data/traits/morphology/branched_shaped.yaml
    sha256: 8f47c42623f3bba42b3ea1e5d16e0eb43f833348ad1bc7e5cc21fe114374f428
    role: context
  - path: data/traits/morphology/brown_pigmented.yaml
    sha256: e274c78a53afdc1ab48937ce3077e4950c1186179d9178cb452e557383f361a3
    role: context
  - path: data/traits/morphology/capsule.yaml
    sha256: f3abc80a712bde31112674f145ff48bba6909d35be2b2098c6c78292ed24435f
    role: context
  - path: data/traits/morphology/carboxysome.yaml
    sha256: 30c32b6616b8ca39a66040c9663ea827c60cd9dc21855000ba7f49234933b180
    role: context
  - path: data/traits/morphology/carotenoid_pigmentation.yaml
    sha256: 9b159d65df4aaf13413574e288c470033e45d7e4325155e069572fb0207df95b
    role: context
  - path: data/traits/morphology/cell_length.yaml
    sha256: ea72262d9dcfedf84332fb14ef9000d65158a825427766b592bc08638f77895f
    role: context
  - path: data/traits/morphology/cell_length_large.yaml
    sha256: 9bf98e6a9a0d370ca4fb67d6bb832f06ead457579754293560d785c7784b68fd
    role: context
  - path: data/traits/morphology/cell_length_medium.yaml
    sha256: 17d25ef97f344b52b933a65cb1be18ffdd9267e4ce884342cfc8edc649d17ac4
    role: context
  - path: data/traits/morphology/cell_length_small.yaml
    sha256: 0243a0bb5b7d5c4269d659ea0476d89caed00bad7a370e9e5d0f3b7b2b37ef44
    role: context
  - path: data/traits/morphology/cell_length_very_small.yaml
    sha256: ce82ae71a88e164e7b9b54ae6de25950a6e534b9da3ff4005f08fffb5d4993e0
    role: context
  - path: data/traits/morphology/cell_shape.yaml
    sha256: d9623499ad02929e34aaf6d4be61fe986518bce117457e6261edbe63b39cff59
    role: context
  - path: data/traits/morphology/cell_width.yaml
    sha256: d283a9c4c8cdbb6c86bf9620bc2553ed4813c720f23364c1e9ca3f85096e1a4f
    role: context
  - path: data/traits/morphology/cell_width_large.yaml
    sha256: 4a11564dd5b65be88b806c877ed6ce467d1530479cdf000669340936c4840c53
    role: context
  - path: data/traits/morphology/cell_width_medium.yaml
    sha256: 52ca8e618bf2296aff676f81c1427a8c6037070121accffea4b06d8b54763f2a
    role: context
  - path: data/traits/morphology/cell_width_small.yaml
    sha256: 3e4c1bae320209e4baf52e9f7c4f23b36358df35b4894a71ccb2a00319105f21
    role: context
  - path: data/traits/morphology/cell_width_very_small.yaml
    sha256: 0b3bc10b45899b411eeef4564b807c178f382fd3a7ff32cbfe19e7e905e8efc7
    role: context
  - path: data/traits/morphology/coccobacillus_shaped.yaml
    sha256: 6308a2f63b067c54df58ee5114ea3d40162a42697f2cf7be28a868c5dee63663
    role: context
  - path: data/traits/morphology/coccus_shaped.yaml
    sha256: 2a705c6da67afaa354d630dd4fa63569e9e8c8d8606bd9f90aaf217a3c348b96
    role: context
  - path: data/traits/morphology/coenobium_formation.yaml
    sha256: b600946ad1a3a43dc20d92aa2674714ac0cba6e371d17dd3e2e3ffbbadc8a062
    role: context
  - path: data/traits/morphology/cream_pigmented.yaml
    sha256: a3ba26c66b5df90d4e3e9a7af00730a917ac17914f99d243d794497bd6d56a5c
    role: context
  - path: data/traits/morphology/crescent_shaped.yaml
    sha256: 619d30596a9e6179724da7a788cd608d3cb30d390686971def9d031488060d5e
    role: context
  - path: data/traits/morphology/curved_shaped.yaml
    sha256: 498f4ff2a150b62bb60e900fa32685aa728ff4f1ced2600c9eb6909b80e5fd82
    role: context
  - path: data/traits/morphology/cyanobacterial_multiseriate_trichome_formation.yaml
    sha256: 0a598d258e1f6174e27ba4b951f998e60f2dc479ecac3cf2238897307b6dc087
    role: context
  - path: data/traits/morphology/cyanophycin_granule.yaml
    sha256: 2c171bf6fa13e57b716e45893bd36558aa5ffcf59d8d0559ea33f3e6377381f8
    role: context
  - path: data/traits/morphology/diplococcus_shaped.yaml
    sha256: f53f1860d9bfdcc3b4ba369eeb4a4fb77bd1f6e0aa694df26ade1127241e0cca
    role: context
  - path: data/traits/morphology/disc_shaped.yaml
    sha256: f65f965104bc4ad200354fd99f248ee7b09715caf8e300e6c2552d2251a03369
    role: context
  - path: data/traits/morphology/dumbbell_shaped.yaml
    sha256: 62a8c94ba3e5632d530d395247c7f77e9201e5cc7f3e0dda541480548fed98bd
    role: context
  - path: data/traits/morphology/ellipsoidal.yaml
    sha256: d7744a7e7410294f61fc56ae26eb7b1d173c6a5575dd608472294a62edd9ff92
    role: context
  - path: data/traits/morphology/expansion_driven_sliding_motility.yaml
    sha256: a1241019ea61c5b85c5dddb33b05c01738e0384f12de60d864dcb14d4d8a06cc
    role: context
  - path: data/traits/morphology/false_branching.yaml
    sha256: 8aa0c8486100950047ca65237512db18dab295c02414e55284e145d112351bba
    role: context
  - path: data/traits/morphology/ferrosome.yaml
    sha256: aee1ebd31daa71aba1f326fae2a584834f8e98b38a55d0a512baee0ed7c557d7
    role: context
  - path: data/traits/morphology/filament_shaped.yaml
    sha256: 34307c9384e8c33f3f73b9ae5f66c14218f3e1f8c70524639313f2f8d6427516
    role: context
  - path: data/traits/morphology/flagellar_arrangement.yaml
    sha256: 1b944448f88de4fa9ff773e155866a2c592f7e843a4c7dc152534676d4e4f329
    role: context
  - path: data/traits/morphology/flagellated.yaml
    sha256: ef50cfb498de5c66a4f2fb904a2038f4c97fa2615e6090a652758051ad25250b
    role: context
  - path: data/traits/morphology/flask_shaped.yaml
    sha256: 50af05acc9b12607517ffe77b3395641f4a03264a4a538e47845ac3688aea56e
    role: context
  - path: data/traits/morphology/fungal_adhesive_column_trap_formation.yaml
    sha256: a1ea209ca312201003f463ea2aee9f4de146879ca10dba838c7416797d4f0d5c
    role: context
  - path: data/traits/morphology/fungal_adhesive_knob_trap_formation.yaml
    sha256: 4404178edffe424b30bab385f9f62ff83d08853100f95e3b5185eddff1e2795f
    role: context
  - path: data/traits/morphology/fungal_adhesive_net_trap_formation.yaml
    sha256: 6a19dd422c4e687c83938fa16443419f3b5378c350934ebbaaa709d98f75bb2d
    role: context
  - path: data/traits/morphology/fungal_appressorium_formation.yaml
    sha256: 0a6d6008c4e018dd7a08613abcd8ef359e980ae974902f42fc9f4f0330a923d8
    role: context
  - path: data/traits/morphology/fungal_arbuscule_formation.yaml
    sha256: f857ed81b07cdc0c204f5a3e4322ccb9444ab64a37ee927150aa6ca9cbe2386e
    role: context
  - path: data/traits/morphology/fungal_auxiliary_cell_formation.yaml
    sha256: 7de9789e800a1aebfb3d4694fc2571727cbab08997e1c5b2b855f60278eaa4e5
    role: context
  - path: data/traits/morphology/fungal_branched_absorbing_structure_formation.yaml
    sha256: 10d6fa9b9eae5072e7875ac12346be653485756892b52fd4d62499282a7e8cf8
    role: context
  - path: data/traits/morphology/fungal_chlamydospore_formation.yaml
    sha256: 76383d6b5eff746680ca739b22537a610c80ea855c10026a27b79fc5470d64a5
    role: context
  - path: data/traits/morphology/fungal_conidiation.yaml
    sha256: d6435aad1ab68a64578b971bbfe89b89734caf39efe2c1fcdc1aba275480977e
    role: context
  - path: data/traits/morphology/fungal_constricting_ring_formation.yaml
    sha256: 46df30de3dcf02b13fc54cd7ddaef4d256c426a3207078dc860dd73c9f6e7fe2
    role: context
  - path: data/traits/morphology/fungal_hartig_net_formation.yaml
    sha256: c001c2e3d342d0c008942b69267cc32974c12067477d4a26cf80ed862aa9582b
    role: context
  - path: data/traits/morphology/fungal_internal_mycorrhizal_vesicle_formation.yaml
    sha256: c58bd3dc9646fe867b8d1927820dc26fbfe7011bf0ceff20abb598ca4707d89e
    role: context
  - path: data/traits/morphology/fungal_mycelial_cord_formation.yaml
    sha256: 42e6dffb6ce9a17d3f13490c9953c5312fafe616d802e5314649ad603103056f
    role: context
  - path: data/traits/morphology/fungal_nonconstricting_ring_trap_formation.yaml
    sha256: 342bbe3ba7473d88d4010313a01246fa13ae592ec02871aa30fad3efd570efbd
    role: context
  - path: data/traits/morphology/fungal_peloton_formation.yaml
    sha256: 2fd01c85d2549e487ed88f58730de4ea5d1c7d7fc3dcf180b7f816ac7cf236ae
    role: context
  - path: data/traits/morphology/fungal_rhizomorph_formation.yaml
    sha256: 9da4bef863c1ceee825a7f39ebc0195d90c981ed20f0a2d253d139dc7f156ad8
    role: context
  - path: data/traits/morphology/fungal_root_mantle_formation.yaml
    sha256: dcd5a60c222a7d5cca2c7714c66895204e0fddddeaf4136ee9929053e083897b
    role: context
  - path: data/traits/morphology/fungal_sclerotium_formation.yaml
    sha256: 57d3731c9664da47db59a493f40f3bdaf7a42cc39e7332839a64e94e871d5bd8
    role: context
  - path: data/traits/morphology/fusiform_shaped.yaml
    sha256: c300c8eaad2c5624d23590237ea3f1378ed65dbd89b7e63b04b4f7d99fe2523c
    role: context
  - path: data/traits/morphology/gas_vesicle.yaml
    sha256: bd0940162b23b952a56a87edf709dc39ffe205e0cccb78629811a01ede3be065
    role: context
  - path: data/traits/morphology/gliding.yaml
    sha256: 3aa51b4f644a24d02df199e3e9cb8c05fa4541b24896e2a20026371f5f2d44b0
    role: context
  - path: data/traits/morphology/gram_negative.yaml
    sha256: f799d2f3c60c1d771213124feed9fad55f41d23bf02c585d74630ae46180bf56
    role: context
  - path: data/traits/morphology/gram_positive.yaml
    sha256: 06ad8a9820215c8d572a710bb4bc4f73b6d959f6f9b09b170b4fc616df3b7480
    role: context
  - path: data/traits/morphology/gram_stain.yaml
    sha256: 60f83094e141e00f1a86bde7b23cab09bde9c53137bd1f82df2bc62ef9cf130a
    role: context
  - path: data/traits/morphology/gram_variable.yaml
    sha256: 1cbf332264d1fdc4e7073c2909f695f39fd9219eaca45376bad5fbfc1ee9db9e
    role: context
  - path: data/traits/morphology/green_pigmented.yaml
    sha256: 2419bc1a57801b19032db1f09f1b1bb8302e473a48751e4450d4c282426c7d58
    role: context
  - path: data/traits/morphology/helical_shaped.yaml
    sha256: 1ff2e11f213eeff72d8ca79beedbfe74b0d20b98cd9f70bbf63a307cda7cdc6b
    role: context
  - path: data/traits/morphology/heterocyst.yaml
    sha256: f04741f703a380ca8431db759cc7ad49618a45260b94ff17a42701d6e2091b4c
    role: context
  - path: data/traits/morphology/holdfast.yaml
    sha256: 1d624e357936be3c2b1f8a255b2102d4e9cb7141d77784f40fa1edca75238cb6
    role: context
  - path: data/traits/morphology/hormogonium_formation.yaml
    sha256: 7c9974012029aa553c56f5e2a140893f12e0098255339ed987ffd68ee50790bb
    role: context
  - path: data/traits/morphology/intracellular_inclusion.yaml
    sha256: a26a21e12585bcc8db1c744457fdafb2b662bf1ceaa359e01c37b39e7a664aa9
    role: context
  - path: data/traits/morphology/irregular_shaped.yaml
    sha256: bde4332583c7070adadf6be99a11b55145d61d764686c88e9a0d70c616910c63
    role: context
  - path: data/traits/morphology/lateral_flagellation.yaml
    sha256: 2aa1c5768b9ac667a44f11c1c31ab2f501392875753345a85085efa76e2976bb
    role: context
  - path: data/traits/morphology/lophotrichous.yaml
    sha256: f6b56d212311530319c368741831ebfab91a96a63447a8afb0e8969c8b584066
    role: context
  - path: data/traits/morphology/magnetosome.yaml
    sha256: 934ea1971ba4471c9c1c1da84dfe11a791955ab6583f4d2e4317a0b95505102c
    role: context
  - path: data/traits/morphology/microbial_haustorium_formation.yaml
    sha256: eed2f55fec6bec70d27b370bab38016dbaf27b3f5f33f7845e74d6642de2a479
    role: context
  - path: data/traits/morphology/monotrichous.yaml
    sha256: ac8bc6ba4c749b493755542f925140b177d9e4b8d963da6fdfaba97be115ce2e
    role: context
  - path: data/traits/morphology/motile.yaml
    sha256: 69473c9ebbd067e4091e63e3058b627dcdd55f241ce3348da672deb64e612465
    role: context
  - path: data/traits/morphology/motility.yaml
    sha256: 7286049368501afc606a7ddf1ec36fa3ac73dcb3213e7f72bdd94e89b7e71313
    role: context
  - path: data/traits/morphology/mycelial_growth.yaml
    sha256: 1c7e82d2ea218ab2c1595343193f606d9fa1262f36b180b67616bc27f6192eb6
    role: context
  - path: data/traits/morphology/necridium_formation.yaml
    sha256: 2f6a9d1ef83a6315da7833c85d37bae892b8d9d963708e02e5ff3a09161d5956
    role: context
  - path: data/traits/morphology/non_motile.yaml
    sha256: 62bdf647d9897eafd8c2ac577b3910248c66056892ac69b0b516e52516349b89
    role: context
  - path: data/traits/morphology/non_spore_forming.yaml
    sha256: 5384df1a84681d314257f07cbd9fbfed81846c97e0d11666427d57415d85102c
    role: context
  - path: data/traits/morphology/orange_pigmented.yaml
    sha256: a28328e761a8fb35ca970f7a2a3c95dda5175046b6982c4a4d77fdaa92f73b15
    role: context
  - path: data/traits/morphology/oval_shaped.yaml
    sha256: 8d5c8404e8e4dcd54305d85e8f64cbf588725b7f9b7b79dea274485a73d5b1de
    role: context
  - path: data/traits/morphology/ovoid_shaped.yaml
    sha256: e2b9e97a150ad13ce7214a276141ebf5e096e24f1c8b3ff8e9dbcfa598e628a1
    role: context
  - path: data/traits/morphology/palmelloid_formation.yaml
    sha256: 6fec9c7538d049e5301536724aa6ce611e41ebfcdd8d32a9155eeba384eefe1a
    role: context
  - path: data/traits/morphology/peritrichous.yaml
    sha256: 3955664c8ba987e03275311e89f01b8627e8b76f74fcc5e170a794f842d94bc4
    role: context
  - path: data/traits/morphology/pigmentation.yaml
    sha256: cf9a2b39e478a06e4c2683971f62079451067264691f065ea9bca58f6a74486d
    role: context
  - path: data/traits/morphology/pink_pigmented.yaml
    sha256: c171a08dae166dcab700d75cfdc2ea3ad3dfad5fbf6d394c64a31d2a03db88be
    role: context
  - path: data/traits/morphology/pleomorphic_shaped.yaml
    sha256: a831d22afaa49e4c2555001e119ce86bce45a64d5d0e269d8f88ec91749eb9fc
    role: context
  - path: data/traits/morphology/polar_flagellation.yaml
    sha256: 97dbdc1a11601a7802102e1e731c1d8bdd09019561cb01f788b7ea8be4ad7782
    role: context
  - path: data/traits/morphology/polyhydroxyalkanoate_granule.yaml
    sha256: d4b46d10c26ce349527ea0d1b5e856e1c3122f172556456bb3c0aa21bb7303df
    role: context
  - path: data/traits/morphology/polyphosphate_granule.yaml
    sha256: 16059bb919c1ede84a50bb513b4ddf1623bd3fc9f18c25761af03ff41a1def51
    role: context
  - path: data/traits/morphology/polytrichous_flagellation.yaml
    sha256: ce2a45b46c5cc16c11af5541685972dcf6a3ed185f2b1cd965a8786ba8c39ee8
    role: context
  - path: data/traits/morphology/prosthecate.yaml
    sha256: e638fdc43f3d222f063d30f753e460f914105ef565980d536b7fdb0da6c77d2b
    role: context
  - path: data/traits/morphology/pseudohyphal_growth.yaml
    sha256: 5c7b4655335f2b2b48992a15088c84882676cd284d5c0a93b94d34ade784fae9
    role: context
  - path: data/traits/morphology/red_pigmented.yaml
    sha256: bc0bb8263625dab957a9bcff4a6f412700caaa10f1c0d1d65e8124fc36a6c1b2
    role: context
  - path: data/traits/morphology/ring_shaped.yaml
    sha256: 4f45d66725da89fcd4a9a182a4afc069e430dca4a4f33f9fdce0b51ed6fb00a7
    role: context
  - path: data/traits/morphology/rod_shaped.yaml
    sha256: f0909f175e24510b0becfe864bbf01eedf93e92a7d02df31fe27b1c74b8a41c7
    role: context
  - path: data/traits/morphology/rosette_cell_arrangement.yaml
    sha256: 10f175831ec5b7fdc34bdefebec9611abac85617d68dc4f8cf50d4e8cbf137fa
    role: context
  - path: data/traits/morphology/s_layer.yaml
    sha256: 5dc05d23c31e1b3247ac63b94b39527e1e2568fb21584380b79886eb89921284
    role: context
  - path: data/traits/morphology/sarcina_arrangement.yaml
    sha256: 43376a1352ff66a800e534204ba593623307249f1c49271bc28eb6d3cbdf70d0
    role: context
  - path: data/traits/morphology/sphere_shaped.yaml
    sha256: b612bc1e9bddbf43289d78f4858de5de2ad162dfba0baa8f5c51a95b53d6ef6c
    role: context
  - path: data/traits/morphology/spindle_shaped.yaml
    sha256: 31b000d48c308b098436a284afd904297625639a8ee7846d7446c17ba9f2b2c3
    role: context
  - path: data/traits/morphology/spiral_shaped.yaml
    sha256: 3951da3095de8e19b0d3472eb58bb12b1f43d96b1f3daf7cc2c3c526683022ed
    role: context
  - path: data/traits/morphology/spirochete_shaped.yaml
    sha256: 256cd4fc35c002c502bdd9f6b6cf403c7362c9c44421f6de0acada5850e283ac
    role: context
  - path: data/traits/morphology/spore_forming.yaml
    sha256: 9ef9283d75814aa3a351bce46a88f873fd4bb48572b9d72497b1f6cdaefbdc19
    role: context
  - path: data/traits/morphology/spore_shaped.yaml
    sha256: 9c8ef4432b3c8c129a0795ef2024b9e653fb20b6d2020a6657ee6e606f0df913
    role: context
  - path: data/traits/morphology/sporulation.yaml
    sha256: 6f9511fd98b434e4d9667d090e41d4d2147be6d04c5fd9753d306051c7d079de
    role: context
  - path: data/traits/morphology/square_shaped.yaml
    sha256: 6f9e88c9f1c52d1a4b6e28bb6d5ac7b141256e9ed940fcc149276649ad9cf877
    role: context
  - path: data/traits/morphology/staphylococcus_arrangement.yaml
    sha256: f0b8c6b2caeadd109a1df2b6d64b378e75c952be65a29648497fa108dbf928ed
    role: context
  - path: data/traits/morphology/star_shaped.yaml
    sha256: 9361d877ac0340a93fac58488eba94220bacc89b9ca03a2a26c0da5e36b1fe8a
    role: context
  - path: data/traits/morphology/streptococcus_arrangement.yaml
    sha256: aa01a84ad2b70610a80884e9ec711b44d7428674c149b946008f62309d0d5a4f
    role: context
  - path: data/traits/morphology/subpolar_flagellation.yaml
    sha256: 9d4a684170334e88675880d205e2dc1875557a56f1aadf148c5ab9b0d0d29775
    role: context
  - path: data/traits/morphology/sulfur_globule.yaml
    sha256: 06607210a6281d3efd6d39d19fcb7cc2e66fd3c6fc56e2d5a4b01be3d49fe087
    role: context
  - path: data/traits/morphology/swarming_motility.yaml
    sha256: 08b751858460a58152dc799b6dc71d4e51739aed711b486e448d52e3e7a43fed
    role: context
  - path: data/traits/morphology/swimming_motility.yaml
    sha256: e74941cf9fe2a4ec4e8be09f5b3555084e7b120e133b75fcb1fb1ad8848059e2
    role: context
  - path: data/traits/morphology/synnema_formation.yaml
    sha256: bcfaf81a09385e32f2dccbef988598c4a9e48b7c0acf59fe39fcddfc2a933885
    role: context
  - path: data/traits/morphology/tailed_shaped.yaml
    sha256: b3b6e3ace7234906b77028ed86217c980145ab4732736ab1e659569596b1c596
    role: context
  - path: data/traits/morphology/tetrad_arrangement.yaml
    sha256: f0559a9e57e19133a4dfcb051222835b2406ff6fc80d51cc80b97a5f59395ab2
    role: context
  - path: data/traits/morphology/triangular_shaped.yaml
    sha256: 6137c3da3a95004eb2e63018c66ac2050a7aa321888840ba03f0018ed4f17cfc
    role: context
  - path: data/traits/morphology/twitching_motility.yaml
    sha256: c9f8b6796d14a81207c870319b4a46e53c4d2f56c9359e6e4e8caa5051ef19d1
    role: context
  - path: data/traits/morphology/type_iv_pilus.yaml
    sha256: 49a17f1e5551d9308fca143a5c0c81cfed0f85587b20404383cfe73715984cba
    role: context
  - path: data/traits/morphology/vibrio_shaped.yaml
    sha256: 2fab15498c06b57d946f92fd44e253c053faa6114693a8efe09c14bacecf7af1
    role: context
  - path: data/traits/morphology/white_pigmented.yaml
    sha256: 1d5837be5a27cf18a95087c938130ce0f824d087145a4a13f0c8ec48c137124e
    role: context
  - path: data/traits/morphology/yellow_pigmented.yaml
    sha256: 0199480534bfa7174118b19466c492557062b4c20051c3a844df0c34b6b3a964
    role: context
  - path: data/traits/observation/growth_nacl_observation.yaml
    sha256: 0dc18f4f6298a6c0466d2ca6e968853818797d860d4974a150103c9fe03b8d24
    role: context
  - path: data/traits/observation/growth_oxygen_observation.yaml
    sha256: a44f060d1f4873eb9fcde85f41d2295795132107153d936d78329fea63602ba4
    role: context
  - path: data/traits/observation/growth_ph_observation.yaml
    sha256: eccbdaa5e859a7faf7db25c1e3ba51ad014bf4bb0239140454ad12a05c7ba0c5
    role: context
  - path: data/traits/observation/growth_temperature_observation.yaml
    sha256: 723720f686e11734a1c2a1d695a3462bc22a524495719e86677ac3305a110d15
    role: context
  - path: data/traits/observation/nacl_delta_observation.yaml
    sha256: d7e30e9f97234a853da98906d9ad4be2e69159c2592af812bf8eeba493a0c7d8
    role: context
  - path: data/traits/observation/nacl_observation.yaml
    sha256: c56aa57150e28bcb74c87232c3cc4fc60bb88bb8313755e14ff9b2ce6e770562
    role: context
  - path: data/traits/observation/nacl_range_observation.yaml
    sha256: 48b153e6ed10333f46cea6c9ee5edc5c4f34393f96b6f06995d6fb02a026d642
    role: context
  - path: data/traits/observation/optimum_nacl_observation.yaml
    sha256: 6bb0c13bfe4da2e36cddf3df9ef111f0b1f14b3e5c79b3550453ce41cb6c99bc
    role: context
  - path: data/traits/observation/optimum_oxygen_observation.yaml
    sha256: c6d8f17c61c472d02028f7de59ff26c7d9c9943711faf648495ab15b4dd2fc24
    role: context
  - path: data/traits/observation/optimum_ph_observation.yaml
    sha256: b334582e26a21621895a19aae66f108c6b65baa0730ab37acfd22dfc0d74b38e
    role: context
  - path: data/traits/observation/optimum_temperature_observation.yaml
    sha256: 74ec5ec967fe65065257eb77b6708045a66d493ad10d4f1eb4a7914ec9e0ae2e
    role: context
  - path: data/traits/observation/oxygen_delta_observation.yaml
    sha256: 5d29ecd0decae61838a27b185fe4f46c3f8c522f71b1b90554978057fea3188d
    role: context
  - path: data/traits/observation/oxygen_observation.yaml
    sha256: 0722c0bd217ab048c5ee9cb2c5600ea73a0f00997eb555be61bee40c9b07cc59
    role: context
  - path: data/traits/observation/oxygen_range_observation.yaml
    sha256: 8ac192cdcb87cfebffade66f84e6a6a0ece4b2e7e0af1068f6bf9e45f91617da
    role: context
  - path: data/traits/observation/ph_delta_observation.yaml
    sha256: 75be0e45a5c86c5574a77ec4701246f8642909c0631b71882fa89e94bf44cce3
    role: context
  - path: data/traits/observation/ph_observation.yaml
    sha256: 1675530959aa396c4805fbdaa49960e236e4cb03d4a1e7ab4cb3bcba8f49fed3
    role: context
  - path: data/traits/observation/ph_range_observation.yaml
    sha256: cb3f8748ea7147e404153522e8bb4098a984da28cbf036ecc9e4925a1bffd54b
    role: context
  - path: data/traits/observation/temperature_delta_observation.yaml
    sha256: 043a2ce93daac078fd2169b63c25b0aa96836eead912141ba2fdfe59ce0c787d
    role: context
  - path: data/traits/observation/temperature_observation.yaml
    sha256: aa011522499c2853588e98fdf54e24478a5fffe090c5baf659be68f4d0bb472a
    role: context
  - path: data/traits/observation/temperature_range_observation.yaml
    sha256: 04d331b72bed1d33cd0b94aba8f6a9f33786801e545aaab4e753ffc55ffd2000
    role: context
  - path: data/traits/other/catalase_negative.yaml
    sha256: a8ee228a8687c7c5de9581e5a1389dd0d78f23097186592a60af14417367405c
    role: context
  - path: data/traits/other/catalase_test.yaml
    sha256: 170b809adf682d5fb3b82762ed7afe76d74d5511516e3aa61e8ba9a30b9cf588
    role: context
  - path: data/traits/other/circular_colony.yaml
    sha256: 43c499d92c03ab150f51605ae4a95ec85660d4036d742d78be8cc99fc312d9bc
    role: context
  - path: data/traits/other/coagulase_negative.yaml
    sha256: f80d4f8f045b11e931d85dad72b1c9097b195ae7cd170cd970993b7f3f7a05da
    role: context
  - path: data/traits/other/coagulase_positive.yaml
    sha256: fd530e2e96617b6c863ad3866de6f7c7a383ebc6dcd53165e361a6a7435e0f57
    role: context
  - path: data/traits/other/colony_morphology.yaml
    sha256: 814f63c1fdb8d38fe917c6c5a364319774ab6c099284033675ecb6b2a4ca5dde
    role: context
  - path: data/traits/other/colony_shape.yaml
    sha256: 0e8ec60c62d1c2f047d94b63c11bb6aa41c9bf2be22f970397061aee814cf060
    role: context
  - path: data/traits/other/epibiont_phenotype.yaml
    sha256: 1fecbbdd07dfb377a28d1a86814551c2c7b19766617c99293d59e263fb2c0f80
    role: context
  - path: data/traits/other/filamentous_colony.yaml
    sha256: c92e096d904c094b9318814e34c028bf1feb2c8b6597b46439cfced782febda0
    role: context
  - path: data/traits/other/fried_egg_shaped_colony.yaml
    sha256: b492580b6674f8761770d87dd0b2ec663ac940473414f38f9580c9f472e99624
    role: context
  - path: data/traits/other/generalist.yaml
    sha256: 7adc2b3c26b45879c12f50289eb54e3549781b76b5b3506702120f71201eadcc
    role: context
  - path: data/traits/other/hemolysis.yaml
    sha256: 265a4d37b1ca8da730ea3b6386cfcd2a4827cd22a08d404f75ac9dfc3fecf828
    role: context
  - path: data/traits/other/hemolytic.yaml
    sha256: 8858b5da0341f2bb3e5c16ba869cc60b99807062536f1f32cc12f02a26bdb005
    role: context
  - path: data/traits/other/indole_test.yaml
    sha256: e39404258872dd0bcd326f2887f0a25a5c1db11b60e2e9fada0f188882696cdb
    role: context
  - path: data/traits/other/indole_test_negative.yaml
    sha256: 52afa540906ab93023c8d6ffdc5c9add6072784e1b8abcb29dd963834ba0d64f
    role: context
  - path: data/traits/other/indole_test_positive.yaml
    sha256: a2c079a016630fd830863578b196e0d1d46129ad48f1cc15d31b37bc3257617a
    role: context
  - path: data/traits/other/irregular_colony.yaml
    sha256: 4dfd1a5af192c4d39d79d17493d8794e1c71ff8ddc207be2899c89a615638d06
    role: context
  - path: data/traits/other/methyl_red_test.yaml
    sha256: 8cd71269e30dc43ede751a36a37c31b5722c774e679a3181b7dab61ebd8aa471
    role: context
  - path: data/traits/other/methyl_red_test_negative.yaml
    sha256: 80934d2b30203589cb36d6937ba6d5a6f227c006c64fd0218452e90fdccc5a3e
    role: context
  - path: data/traits/other/methyl_red_test_positive.yaml
    sha256: d310b537dc31ac6d5c2459fcb33126d25de383893fae2674a93ad325988a3b45
    role: context
  - path: data/traits/other/non_hemolytic.yaml
    sha256: 84be52a8edd4f6547090d684b2041ed822b583e538eb49bd7e3b529241311b9b
    role: context
  - path: data/traits/other/osmotic_tolerance.yaml
    sha256: fdbc247b183c11c5ef92960ec8008131347e2758a13304b1ae7a494ed41e8914
    role: context
  - path: data/traits/other/oxidase_negative.yaml
    sha256: 0d48ecde43f82fe45e954283c610f7af88b884a5a968bf0352c8f4fc70840f4c
    role: context
  - path: data/traits/other/oxidase_test.yaml
    sha256: d0d4ea6afaf48d1390d25193e69afcc94936c751659494615ea6bb7bfe8dd243
    role: context
  - path: data/traits/other/punctiform_colony.yaml
    sha256: c345b293a6a415d5f187af5c0810f0bae10a4b92b7096c5f97fa5ced0fe696d1
    role: context
  - path: data/traits/other/rhizoid_colony.yaml
    sha256: f4c067f97ed870751b1237dc85a303793e2d55c331dd1eb0425a9de695da8762
    role: context
  - path: data/traits/other/specialist.yaml
    sha256: 8dd83259894f610e66e8744c3c4d210b8a93c40edb304bd79265266ff7ecc1b7
    role: context
  - path: data/traits/other/urease_negative.yaml
    sha256: 51c0948348defd6c735f316edaaddb4126731d8d19c058f385de3c1f3fffe32c
    role: context
  - path: data/traits/other/urease_test.yaml
    sha256: 661068086adb56d6e0c70e122fefc2afe4eb7d91f596d9717fdab268d00f1b8e
    role: context
  - path: data/traits/other/voges_proskauer_test.yaml
    sha256: 17271778e495a307147946393460336bcbe45d433548eb3c3d5f6ae35facb2e4
    role: context
  - path: data/traits/other/voges_proskauer_test_negative.yaml
    sha256: bbf6557bae5e6fe5581873af873004a93ffa20761f45c5012cc9078c33306897
    role: context
  - path: data/traits/other/voges_proskauer_test_positive.yaml
    sha256: e13160c888214dca714df5f5d0e7dc10f3fe0b3a9a955ad4ae75c21d76c4b317
    role: context
  - path: data/traits/physiology/acid_phosphatase_activity.yaml
    sha256: 251a535ee6d18d20738240a35814433c7bbce6386a5bf4dd7ea56d5a63b45303
    role: context
  - path: data/traits/physiology/acquired_stress_resistance_memory.yaml
    sha256: 0062287c6b39b2d03cf54e4fec73ca99299069c4bb33e9b9a63ef9e12b2bb099
    role: context
  - path: data/traits/physiology/aerobic_anoxygenic_phototrophy.yaml
    sha256: 456e996a9c4365b5c088fc57fe4fcc61cb7ec2ba508668cc787cb9fdbb2d3c88
    role: context
  - path: data/traits/physiology/aerobic_overflow_metabolism.yaml
    sha256: d1543a9e0f2efb02c9dcbf46d4828ce88fb26da035fb47d9f00a992cd9cfe5f8
    role: context
  - path: data/traits/physiology/aerotaxis.yaml
    sha256: 078da52149d300160661c6f0b0b313ae7ce86d532fac40cabb4cf892f328d2f3
    role: context
  - path: data/traits/physiology/aerotropism.yaml
    sha256: d546f3ad49b5caacca4d61a11fa793397af9e3b7c7a993942543cb773fd7bb74
    role: context
  - path: data/traits/physiology/aggrephagy.yaml
    sha256: 18b4b083891f667f33c361baaf2139d9675314d41ff058336411407a47e48033
    role: context
  - path: data/traits/physiology/alanine_arylamidase_activity.yaml
    sha256: b2169f96ccf63747827f29242fc681740fa371a5af19c0ee8b9bdf8948a5e377
    role: context
  - path: data/traits/physiology/alkaline_phosphatase_activity.yaml
    sha256: 50c8347e7d242c4e96905458a2c0dda13ec2968002f44d50b436150fed09c12b
    role: context
  - path: data/traits/physiology/alpha_chymotrypsin_activity.yaml
    sha256: ff984823c749c6e3459e3e303ace2f9c92eeaa8de70aec761339eb8bb23f0c8a
    role: context
  - path: data/traits/physiology/alpha_fucosidase_activity.yaml
    sha256: e742c4895cb31e72e7bcca6af5485e5bd46f492ae4c90861a5bd13b0a8de7557
    role: context
  - path: data/traits/physiology/alpha_galactosidase_activity.yaml
    sha256: ee901dd425e38aa55dca4b5d75c93827b59ff5f5f758d8f6a0628ffed3eab1d1
    role: context
  - path: data/traits/physiology/alpha_glucosidase_activity.yaml
    sha256: 5ff824cd5da4b6e7c9ea30f5f7824f5c4e17f9c672ad2c3eb66eca1e5fdd3d37
    role: context
  - path: data/traits/physiology/alpha_mannosidase_activity.yaml
    sha256: 9ccc58dace1b206af2b39c1e35437fd03a346fbed14f448cc5d035954d9c3083
    role: context
  - path: data/traits/physiology/amylase_activity.yaml
    sha256: a2367197cc79c1833ce9f92eac7e01efe320ceeced9149a4b7f8ce1527f87c4a
    role: context
  - path: data/traits/physiology/anisogamy.yaml
    sha256: defbaac955abfdfb7cc9551376aba7fb91f63b4523d682a90cbc0f3535e860c0
    role: context
  - path: data/traits/physiology/antibiotic_resistance.yaml
    sha256: 8956f2a9f32e70041b53e1484868871c80861691c708308819ffe653c98cd41b
    role: context
  - path: data/traits/physiology/arginine_arylamidase_activity.yaml
    sha256: 67d3edf79948bd467baee19d594800e774a85200e6998ce86375a068ba48053d
    role: context
  - path: data/traits/physiology/arginine_dihydrolase_activity.yaml
    sha256: 0a1486ba9f0afa2abe8f533fcfca14a9800b6306deb44fcbac4a90da4b51c57e
    role: context
  - path: data/traits/physiology/autogamy.yaml
    sha256: 005639fd2f8e6dc3fe98854856e23d73a3563c5acc742d8cae7cfc9ad66781fd
    role: context
  - path: data/traits/physiology/automixis.yaml
    sha256: 59d487d543fb9b726fe5bff4ff9909682dcd16a1aa2d3bd5ba72a4e4cdf69b50
    role: context
  - path: data/traits/physiology/autophagic_glycogen_degradation.yaml
    sha256: 0765be60b2a08685fe873863b03fa33c060be0ebf2a489996bdc4fa2c0846625
    role: context
  - path: data/traits/physiology/autophagy.yaml
    sha256: aa2ffeb553e2ad01f518db1c66865749655333966438919d5bbd76e800eaf549
    role: context
  - path: data/traits/physiology/autotrophic.yaml
    sha256: 8e34b68ed459c66a249d6d20078d3b5edd4b498a47766a9c45d08f9ab93dbd8c
    role: context
  - path: data/traits/physiology/bacteriocin_production.yaml
    sha256: 0bfc1b908cf5caf01d87f66ea6bf40077a47d00442c4d753cc8fc8ad3f03f2f1
    role: context
  - path: data/traits/physiology/ballistospore_discharge.yaml
    sha256: b740913a744caf8a6dfc3215dc2b7f0fb739bca8b58f86af35a14907559fa2c1
    role: context
  - path: data/traits/physiology/beta_galactosidase_activity.yaml
    sha256: 55c71b352fcffb616713b7e67fc97b7802994c704ec5be16fdd6ae3a0d0d2522
    role: context
  - path: data/traits/physiology/beta_glucosidase_activity.yaml
    sha256: 6164fd6ed98fd56e1b7d935ec038beebd4473d3fe082626bda3a95ea77a941ca
    role: context
  - path: data/traits/physiology/beta_glucuronidase_activity.yaml
    sha256: db9538210bea4ab1ef5e014de1e3c2a8e90b7abe0c98ac8051c5036ba390dfa3
    role: context
  - path: data/traits/physiology/beta_n_acetylhexosaminidase_activity.yaml
    sha256: b4c11418d8b31b3df99f81793a09f89941184bab4c25e3aac573c13cdb7e22c5
    role: context
  - path: data/traits/physiology/bioluminescence.yaml
    sha256: 0e8bbff3698f1e35bef7d6fc7548c3f454707bb302c0c8c7a8aeeac8d5fc2897
    role: context
  - path: data/traits/physiology/biomineralization.yaml
    sha256: 63389ce52b522f73f9924008306bc51a9280f912bfde285db7955fd348d3d017
    role: context
  - path: data/traits/physiology/bipolar_mating_system.yaml
    sha256: 5b1f4fbe2c501a517cf8928eb005baa2c0310b7437695f01ba1c00fe7e63123c
    role: context
  - path: data/traits/physiology/carbon_source_memory.yaml
    sha256: 43d834a0359fdfbc8e5883ac9098294788b5defad6e50b5664bfd08f471ca299
    role: context
  - path: data/traits/physiology/carboxydotrophic.yaml
    sha256: b09349aa136927ebac55927aba9710d0b651e566e5ae7c40ff458b77b55410c9
    role: context
  - path: data/traits/physiology/carboxylesterase_activity.yaml
    sha256: 31bdb583eb29f8042743c7beb8a42cdc279dcabddc4a754457a9ccec52b0281a
    role: context
  - path: data/traits/physiology/caseinase_activity.yaml
    sha256: 4490467c0ef8fd18926d125592b1a4d7ed2ae73f4cdb4d209df015d1e0c77217
    role: context
  - path: data/traits/physiology/catalase_activity.yaml
    sha256: 7721392a4851f8d82260d19faf96a415e137dbb0211701f9f14e2016c207db32
    role: context
  - path: data/traits/physiology/cellular_buoyancy.yaml
    sha256: 9c8c66fe229374210777b7d57bb49f661d5a02ea7b56c1169f94d1d69853f6c3
    role: context
  - path: data/traits/physiology/cellular_rejuvenation.yaml
    sha256: 9314389874084c07dcc0286f31c6b489f43ee3d8196b01dbed5233e4a63412d6
    role: context
  - path: data/traits/physiology/chemoautolithotrophic.yaml
    sha256: 0dbd9e11b4bf4e896641fa2f29a098e41243823d7361e96720a1415fc9c6de10
    role: context
  - path: data/traits/physiology/chemoautotrophic.yaml
    sha256: 3963c38a26f014536b9f05676131df378c2e0878d66b46ffa19a5e1ac9c913e8
    role: context
  - path: data/traits/physiology/chemoheterotrophic.yaml
    sha256: 87e425925b0addba600be5ab4a1f7157474951bfcc8b116283c9f034720b11b5
    role: context
  - path: data/traits/physiology/chemokinesis.yaml
    sha256: 110a966976ff64ac4591ed245423f096be61d2a63b019dfd29c55965896560c0
    role: context
  - path: data/traits/physiology/chemolithoautotrophic.yaml
    sha256: 05fb6585763ed12fed9d7bba5e4990a8271eada14519ee365cf289152a2d297e
    role: context
  - path: data/traits/physiology/chemolithoheterotrophic.yaml
    sha256: 4cd5679b619e3904a39b44660a0e440fe29deacd4c50d944354ee0337b65ec58
    role: context
  - path: data/traits/physiology/chemolithotrophic.yaml
    sha256: 7460783ca89f325f42d59dc99112db85143372359e77d0d95c92b0ad4d1b0274
    role: context
  - path: data/traits/physiology/chemoorganoheterotrophic.yaml
    sha256: 12903629521614b5d201d243712f0dffb0bedcdcf7502ad275e88a6772fab9f3
    role: context
  - path: data/traits/physiology/chemoorganotrophic.yaml
    sha256: a269225654ef32b9d9d62a3502f6c0967f0d13134ac90a8d86badc56de43dc44
    role: context
  - path: data/traits/physiology/chemotaxis.yaml
    sha256: 6ed2ca3f066c8b6920f9534c20cdfb94a5a6a4ffcf54e4fa672eb5a68391824d
    role: context
  - path: data/traits/physiology/chemotrophic.yaml
    sha256: 86e50378c96c3c40b6469f9c1c4b7237883a3051809e8381258b0013727c9f89
    role: context
  - path: data/traits/physiology/chemotropism.yaml
    sha256: 55fd76a30b9ab37c2709b3e9bdae7b67d3a82394b6defb37c977f7e418278c55
    role: context
  - path: data/traits/physiology/coagulase_activity.yaml
    sha256: 0702d06e5f94bfb7db4fe476fdeea9f1a7d37b5c259d2388104f3e40198b112c
    role: context
  - path: data/traits/physiology/coccolith_production.yaml
    sha256: fefe6965ce48f82c93ba5ead98b797553397f10bc6848d056e26d628141eb390
    role: context
  - path: data/traits/physiology/cold_shock_response.yaml
    sha256: 5e131592cffeb87cd2081b3c70a885c3a9d667a52c02cd82537691a1ca57be61
    role: context
  - path: data/traits/physiology/contact_dependent_outer_membrane_exchange.yaml
    sha256: 21b7ee1c94c655f01a420dd348c3b7d3b6224485d77ecb59d95e733b843c6cf5
    role: context
  - path: data/traits/physiology/copiotrophic.yaml
    sha256: eee97d46b470884bee759a04fa532185915fdd28b1e34552fd3d309afc3ce130
    role: context
  - path: data/traits/physiology/cue_triggered_environmental_anticipation.yaml
    sha256: b6f3701601a336e14e20dc8003fb4264d3ee029e170410563647e0dbd7a2c155
    role: context
  - path: data/traits/physiology/cystine_arylamidase_activity.yaml
    sha256: b9c11e5e7dbb4ab65841f58c8991d4a9252afa480dee2b485a745c0f0e3b4deb
    role: context
  - path: data/traits/physiology/cytogamy.yaml
    sha256: 4cda140d798f6404894db0528b2ebfad38960cf5c5a67867b9a862cbb87c34c8
    role: context
  - path: data/traits/physiology/diatom_frustule_production.yaml
    sha256: b6bfe04293ddd0b17f600b0fc68b8369364eec27d03b6d3dd6e39ac356f2ffb9
    role: context
  - path: data/traits/physiology/diatom_perizonium_production.yaml
    sha256: 25b6c9a02d399e1013aec179770deec4b6791a84748c2d40f6f9ce5537c37473
    role: context
  - path: data/traits/physiology/diatom_seta_production.yaml
    sha256: 69cf1e78c9b4d58f972b2e85fac8433b804bbcd69163f4b90cbdf2961f7ba8f6
    role: context
  - path: data/traits/physiology/diauxic_growth.yaml
    sha256: df91919b069436693e55a13ff97b2f2669062a198e4e6d18ce15eaf5a764313b
    role: context
  - path: data/traits/physiology/diversifying_bet_hedging.yaml
    sha256: 4f0a0c64729b1060791f6d33b148a10f2ea89197a4d4a73a15e990ca301e159a
    role: context
  - path: data/traits/physiology/dnase_activity.yaml
    sha256: 840a0c41f2f6f3cb418c0af690c92eedf40c46db7f0f9ec0148c6d1ef74736f9
    role: context
  - path: data/traits/physiology/dormancy.yaml
    sha256: 555f895de4b0de96b4f298d61720b359fcc41bdaf466fbc8c6b0e78c83c64c5d
    role: context
  - path: data/traits/physiology/durotaxis.yaml
    sha256: 75f70834444bee54e52edc46950e4675d86dfc5aa13834585504601c4889c556
    role: context
  - path: data/traits/physiology/endocytosis.yaml
    sha256: c7e4919a0034b286b4b5a19d1159ce1fc61ad60fa4ba0c348c598f4797103244
    role: context
  - path: data/traits/physiology/energy_taxis.yaml
    sha256: 73851f74fa423ebc3ac173f57418f87fd8fc62a961c0f577ced22074a99d3869
    role: context
  - path: data/traits/physiology/enhanced_transcriptional_reactivation_memory.yaml
    sha256: 3f788e83b77ad8c279f2b3e89a5e18796735730578d7d55d8accbbd19baad7cc
    role: target
  - path: data/traits/physiology/er_phagy.yaml
    sha256: eb4d35c8b13e79c916739e13a444c70bfb4bc146951c2c0b28bab3297854a840
    role: context
  - path: data/traits/physiology/exocytosis.yaml
    sha256: 419001cc5f36f27946299f1ac88e532fdb83c0e0f2be2d3ccedb43e60fa41a6f
    role: context
  - path: data/traits/physiology/extracellular_membrane_vesicle_production.yaml
    sha256: 92ca3c1690f09287dc914e597ada9d3d7ac70cc12f50fa52c2a8dd60c6bc12b2
    role: context
  - path: data/traits/physiology/galvanotaxis.yaml
    sha256: b5a80876b6e6d6eae972b83fbc152fd4cc6ee616dabcc6a34bcb35c1743e4f20
    role: context
  - path: data/traits/physiology/galvanotropism.yaml
    sha256: 5347a4d81ce6a3512bbb0cb724d9bf5afed115b5700656be9cdf3567cc38a7d5
    role: context
  - path: data/traits/physiology/gamma_glutamyltransferase_activity.yaml
    sha256: 22d800aa1fd95cafebc7e16953521f7321f4dda7ac8deb6667c51f616af1e79d
    role: context
  - path: data/traits/physiology/gelatinase_activity.yaml
    sha256: d8795c5e5eb3623135a1570acb2f2f2b48fa874a6f01730fa3c8f11838d68b67
    role: context
  - path: data/traits/physiology/glutamyl_glutamic_acid_arylamidase_activity.yaml
    sha256: 2fffbafb42e06f669e04c26564a0d2f234465b857a52a9e37f466e20b8497ab6
    role: context
  - path: data/traits/physiology/glycine_arylamidase_activity.yaml
    sha256: 69aac77a8be6ea33e9c6b459561d4915fb82edf77894fe25db0bf1cb80c5500e
    role: context
  - path: data/traits/physiology/gravikinesis.yaml
    sha256: 434d86a3ec8490eb0b008b2b4d6fe24ec5e37e10aeced9b0f050eb1743c09795
    role: context
  - path: data/traits/physiology/gravitaxis.yaml
    sha256: 7aca7807a1b5b8905ca3a50c947c89226eb193b946b20cfe98ba1737d5598efd
    role: context
  - path: data/traits/physiology/gravitropism.yaml
    sha256: 5a054d6bf27794f3c4352b35c5e143901094fd789a37301e5a5c165cd7f31850
    role: context
  - path: data/traits/physiology/gyrotaxis.yaml
    sha256: f407d4af4103a258d0ff8938196105ef9d1d145f3f836572c662733dc337b3e5
    role: context
  - path: data/traits/physiology/haptocyst_discharge.yaml
    sha256: bb52b273be59f347628c18aebfbd4ce2a9811eeab9188dd1964a4646633b4e49
    role: context
  - path: data/traits/physiology/heat_shock_response.yaml
    sha256: 61779b3752cfbc750611471851d6a4adb5d5e7c8c63ff12caf4ec9e57e3b69c8
    role: context
  - path: data/traits/physiology/heterokaryon_incompatibility.yaml
    sha256: 9c2403272ed11b204568668cc9a77595da5c31a0d352f9c76e626a694b7ea3af
    role: context
  - path: data/traits/physiology/heterothallism.yaml
    sha256: fc152f54a195e9634642623defbe0a940d17c7ba3816e9e694662e57113a8a6e
    role: context
  - path: data/traits/physiology/heterotrophic.yaml
    sha256: a2f641e2a351187689ebaaac737e29b66ec4a6e7f497ffc9dad105f21e6e70c5
    role: context
  - path: data/traits/physiology/histidine_arylamidase_activity.yaml
    sha256: cbf311cdebb3c4759a31e2eaf7a5e2888ea66e8b19a06db41776847fbea86c42
    role: context
  - path: data/traits/physiology/homeoviscous_adaptation.yaml
    sha256: 0cdd365c80dcb001ae0c3d7c76f3d9a5947226ad22ae253b24a57cfc9e520ad2
    role: context
  - path: data/traits/physiology/homothallism.yaml
    sha256: f1aecbb3bf8977f617f0ad31139e7eed7221f6c7dc488274775d1b58cabf6808
    role: context
  - path: data/traits/physiology/hydrogenotrophic.yaml
    sha256: a839dc8c18d10795dfcc1620abcbfa109a85b6e2faf63f1ab79d4225c62b7e6e
    role: context
  - path: data/traits/physiology/hyphal_anastomosis.yaml
    sha256: 549ed2e5048173053fc14cdc819e3753c85ed098055d49093fc46a3ad598d997
    role: context
  - path: data/traits/physiology/isogamy.yaml
    sha256: 3456ffc8ee259aa30d3406d2770845be4f3137f1b9f5eebee92f74db3b60d968
    role: context
  - path: data/traits/physiology/karyoklepty.yaml
    sha256: 117f62a3300097a6f49a7366d4d929bb0b45366b01a5d78ee861c240e7781d24
    role: context
  - path: data/traits/physiology/kinetocyst_discharge.yaml
    sha256: 1c64bf19f9b8386a8d465bb374c1d171e6f4c81ef73fe77cc0d0b43d0b4b1683
    role: context
  - path: data/traits/physiology/kleptoplasty.yaml
    sha256: b9c36f4801d962b7c2c1d5ef82529042ad6b3e080d2e346aaa187fbf0c2d5cbe
    role: context
  - path: data/traits/physiology/lecithinase_activity.yaml
    sha256: 93a5226921002a88ea0a32b4416165acdae074a45470d333a5c73424dac8c165
    role: context
  - path: data/traits/physiology/lethal_algicidal_activity.yaml
    sha256: 7b7982114ca8dc5e356271fffb515da4204814c9a9f4a605bb9948e74ee5663e
    role: context
  - path: data/traits/physiology/leucine_arylamidase_activity.yaml
    sha256: e05fed3abca3f598e85b2be649afaf0dd3d83b1787f2c5c0f538d11740e92cf8
    role: context
  - path: data/traits/physiology/leucyl_glycine_arylamidase_activity.yaml
    sha256: 3ceee417dae8eb7f8a5f6a9f8a70ec148002ef65e1b78581b4d46cf9e514cd2d
    role: context
  - path: data/traits/physiology/lipase_activity.yaml
    sha256: 71f5d6ce5d8f7df48eefeef137aef6c34adfcf79b08a73a8f2041c60516c50cc
    role: context
  - path: data/traits/physiology/lipophagy.yaml
    sha256: f316b5afa031191a65fae011498dbe20dfbb7e9ea04025a21e12edf783ef112b
    role: context
  - path: data/traits/physiology/lithoautotrophic.yaml
    sha256: e9d80a3af58f9a0683c9783af069b581ff119de5e822443631d2dd0d7834f83c
    role: context
  - path: data/traits/physiology/lithoheterotrophic.yaml
    sha256: 9ae167922594835b67b9dea612789baf8d759233618bcb585b533d79d1066737
    role: context
  - path: data/traits/physiology/lithotrophic.yaml
    sha256: 7dec83f3be65663ceff44f487bf90ed67c31435357a3cc56beb3ce10fd9acb16
    role: context
  - path: data/traits/physiology/lysine_decarboxylase_activity.yaml
    sha256: 1483e8a5057903569cb206cd231e22880d95bfc175ed502af38aaaaf946b3105
    role: context
  - path: data/traits/physiology/macropinocytosis.yaml
    sha256: a9d9b732bab38a666d99d50f50b7bc5056af17c0393d33d35636b1e1a7c753fa
    role: context
  - path: data/traits/physiology/magnetotaxis.yaml
    sha256: 7b56fbdde4da97892102f63d621ec8e28da96e622bbb0c83bb1b16af81a5910e
    role: context
  - path: data/traits/physiology/mating_type_switching.yaml
    sha256: 87a624a01cf324fdd11f70da926bfa7a4cd64a1d50318c85938650d2b55d0a73
    role: context
  - path: data/traits/physiology/methanotrophic.yaml
    sha256: e260f33a208bf379f496975ab86030f6bfad2582f68a9fbab4b77c6ee0667d0d
    role: context
  - path: data/traits/physiology/methylotrophic.yaml
    sha256: 9960b58efbaa69ce4c1a4e7d6d285f330d2792ecf5560f3f6d7badc42b238555
    role: context
  - path: data/traits/physiology/mitophagy.yaml
    sha256: a06f9fe1dc8b47566b808b03fd45ddec9dddfb96ba9a0068763ceeff5995e0bb
    role: context
  - path: data/traits/physiology/mixotrophic.yaml
    sha256: 548fe40353e1418db624fe6aa36fffff5643a2b37181f4cc240ecb812ccf0a49
    role: context
  - path: data/traits/physiology/mucocyst_discharge.yaml
    sha256: cd864028799ee22581df4591b88c5142c753366ece6a8ee7aafad4d131e4b336
    role: context
  - path: data/traits/physiology/myzocytosis.yaml
    sha256: f19a51c942d6a585ef44252829d84ff18d18fc95337b6264bfed9b44d31d2ef7
    role: context
  - path: data/traits/physiology/nad_dependent_alcohol_dehydrogenase_activity.yaml
    sha256: 744b2c7a2b7bab5a03c3b134938af1a21612996367b9cb1a43519886513b7fe7
    role: context
  - path: data/traits/physiology/naphthol_as_bi_phosphohydrolase_activity.yaml
    sha256: 063edb66c52d5dd7cc0495012ab317bba644f2ed19bc7eb34915db32d424e58b
    role: context
  - path: data/traits/physiology/natural_competence.yaml
    sha256: 772c83dc3be59a6ec2b6dbad97a94d3bf81759bf63ecab9a32ed2a7a170a6f4a
    role: context
  - path: data/traits/physiology/negative_autotropism.yaml
    sha256: 8f39ae14c6be35e0002c38baf142e91071b1f6468f84b36d04a85de19f8cb601
    role: context
  - path: data/traits/physiology/nucleophagy.yaml
    sha256: a51cece7b03ba7bb8588a840fd40dccaf00187770f6d528117cba8b8bc975439
    role: context
  - path: data/traits/physiology/nutrient_adaptation.yaml
    sha256: 7a452667f6d12a9bb508aaf1b48aeab9a99e5e4b9f5c76e914ce745eaf3aaafc
    role: context
  - path: data/traits/physiology/oligotrophic.yaml
    sha256: e958bf8f3e4fc18bfaf38f1f29c7a5949a1b0b521a63f5edab5ec0f60ec5f1be
    role: context
  - path: data/traits/physiology/oogamy.yaml
    sha256: 8a3e909be4c765aa897f07f852ddb32eb1c8e0426073dd7a1fdcc2a77065cfcc
    role: context
  - path: data/traits/physiology/organoheterotrophic.yaml
    sha256: 503a83e8c8fb1ce66c624c83489effac7d50cd5dd018c3149c401ccfe8420891
    role: context
  - path: data/traits/physiology/organotrophic.yaml
    sha256: 4a60a71ade48591ef946095062e2755eceea1df8072e2d6c168d4db096f0825f
    role: context
  - path: data/traits/physiology/ornithine_decarboxylase_activity.yaml
    sha256: 3921954abf5aeee763ff761c8483617314b4f970bb3e673e1b94ec0072c715d2
    role: context
  - path: data/traits/physiology/osmotaxis.yaml
    sha256: cf343c5b697a07cb8ed8c55eb02a4103b544460a14a5ab79f24ee21416e9b238
    role: context
  - path: data/traits/physiology/oxidase_activity.yaml
    sha256: 9c94622e022b67ba7bb02c7c4fdba8ac8bd3fa6f8a4697ab6c14545ed8c4fabe
    role: context
  - path: data/traits/physiology/oxidative_stress_response.yaml
    sha256: 982a30cf6189d2312da8c5f72a88e95ef8aba9d20e05f8b2f81d235c761c84cf
    role: context
  - path: data/traits/physiology/paedogamy.yaml
    sha256: 6e011b1512c4b30eb7e18546160b07226a789bcd3a31eb4b834baf7cc1d09423
    role: context
  - path: data/traits/physiology/pallium_feeding.yaml
    sha256: b7f7ecca3a98e12f001b07c6221a9d63b2a223ed4d2b21a49f184889721f4721
    role: context
  - path: data/traits/physiology/parasexuality.yaml
    sha256: de21f7f2940efdf2e7f86b362ab96b38d237a679895298a59df13a8ff278919a
    role: context
  - path: data/traits/physiology/persister_cell_formation.yaml
    sha256: 757c1c7214848454937636f009194d9d66eda190ecca93e6d2b98fc27907f26d
    role: context
  - path: data/traits/physiology/pexophagy.yaml
    sha256: 25e97eafd0bbf2a0170e624c3e7adb6bc7a4299b214432bfc0bc82d484fbcc87
    role: context
  - path: data/traits/physiology/ph_taxis.yaml
    sha256: ada2442dbe3db8f753af22497cd354da92a341c2ce4c0dae370935e987f8b7bb
    role: context
  - path: data/traits/physiology/ph_tropism.yaml
    sha256: d911e980a767fa3d88c6556aa697cd1024a47f79cb3197d72ae1b1efd57a1fb3
    role: context
  - path: data/traits/physiology/phagocytosis.yaml
    sha256: 19415ea7604722000e5416d490f7924d12eb90f78f6df66ff1fdb2ed8bcc4c99
    role: context
  - path: data/traits/physiology/phagotrophy.yaml
    sha256: b0a59b9889569ae3c57fe567668c43691ad7896640e5b59acc39c7b6bf66db4f
    role: context
  - path: data/traits/physiology/phenylalanine_arylamidase_activity.yaml
    sha256: 052c95df20aea1ba5730ea7f671e1727ce489201f68252a30045f98ee7613a52
    role: context
  - path: data/traits/physiology/photoautotrophic.yaml
    sha256: 16b9f09e1a4bd3f2168c6749bb0dfd7aba9b89ee888bca92515d86733437bb60
    role: context
  - path: data/traits/physiology/photoheterotrophic.yaml
    sha256: 1eb497ffb523830e239a69afe44d469858a3ff8afdfafdc8ac02787bf73b85a3
    role: context
  - path: data/traits/physiology/photokinesis.yaml
    sha256: c75fd43a6b84647ee8d97c07788eefa93e459b61f314f4982d41d8bcbeaf3e41
    role: context
  - path: data/traits/physiology/photolithoautotrophic.yaml
    sha256: af95d5be50fd0cde26b2005cbd37cdeb7dcddb583a219189fe7942f0935073c2
    role: context
  - path: data/traits/physiology/photolithotrophic.yaml
    sha256: aeb448f89b5e394d8c96dcfdbdd7fa976eeba8052886359c65fabe1746ea26ea
    role: context
  - path: data/traits/physiology/photoorganoheterotrophic.yaml
    sha256: 247ceb2fd84c46273f97638141141a3e350712633e43c2529c573e0920209190
    role: context
  - path: data/traits/physiology/phototaxis.yaml
    sha256: 9eb473356ec90119c209f016556b4eb971210802202268692f69cba002f51458
    role: context
  - path: data/traits/physiology/phototrophic.yaml
    sha256: 6a6cacc5cad6e122f104e9898ccdd5eed0d956197035c2d8a4b5c7ce324dc1fc
    role: context
  - path: data/traits/physiology/phototropism.yaml
    sha256: 4e8665bf7f989145d00831132aca90b7ecab35e0688a7ef608db1cb2fdba5c30
    role: context
  - path: data/traits/physiology/pinocytosis.yaml
    sha256: 9ba8da9ddc81b1a1761ec193df59d9d0da0368700a62060007d9e460f87f68d6
    role: context
  - path: data/traits/physiology/positive_autotropism.yaml
    sha256: af212add1359ab9b24c10a1b7866d10f51ee23963aaf16754a7c4726a2c09170
    role: context
  - path: data/traits/physiology/primary_homothallism.yaml
    sha256: 8f98d265f7354a8ce1ca5348080036963f5e0a31146367c5aaad0d2220de7ace
    role: context
  - path: data/traits/physiology/prolyl_aminopeptidase_activity.yaml
    sha256: ace1ced4b6e0ada19aaf7dfe6056124f84a8db89e1717f711afff97446baa8a8
    role: context
  - path: data/traits/physiology/proteaphagy.yaml
    sha256: cc090c9321c747ef4b30b9198babd6b8e03a0f80ea7c8952f3483e95278bfdc9
    role: context
  - path: data/traits/physiology/pseudobipolar_mating_system.yaml
    sha256: a167e3ee6663995c0dfb771df6419f3a586c8cf4e3d9121785e3255fcfce9a0c
    role: context
  - path: data/traits/physiology/pseudohomothallism.yaml
    sha256: c0531b4036c59c7ce6b0780aaab1a71f8e9a8703dce94bba867d7c71ec6850a8
    role: context
  - path: data/traits/physiology/pyrazinamidase_activity.yaml
    sha256: 8fae06a00aecbf265cbd4644eedf4a8dff9628e5bba4b6d5659d15c2d4e30ad0
    role: context
  - path: data/traits/physiology/pyrrolidonyl_arylamidase_activity.yaml
    sha256: 3f34fdc117e1a282529fd8d5ebd9e2814b142d80a824c9944871114c19951100
    role: context
  - path: data/traits/physiology/quorum_quenching.yaml
    sha256: d1b43dd752cf8b7468fdbf3f6d99e8442d38611f3b1e382b2aed2d3917e1379b
    role: context
  - path: data/traits/physiology/quorum_sensing.yaml
    sha256: 42f80b36e3d6493022a9b1424386d4015c556a33f51bc764c8facc5d9be8bdff
    role: context
  - path: data/traits/physiology/rapid_axopodial_contraction.yaml
    sha256: d47b91ea8671908e5d740e0d0e30c4b42b9739ec48f25fefda38338a3ae30728
    role: context
  - path: data/traits/physiology/replicative_aging.yaml
    sha256: 1d060a599291180cf3c68e5eb7bd335e6283f96393487b23d6390af7687aa0b8
    role: context
  - path: data/traits/physiology/rheotaxis.yaml
    sha256: cab4f28d4cd9e81be29ad852ace47064aaae5579fd1089451358db02c48bbf17
    role: context
  - path: data/traits/physiology/rheotropism.yaml
    sha256: 00f44f4af4627914c97fc6bc20cea4b819171831f744dec614e66792d0d2fbd3
    role: context
  - path: data/traits/physiology/ribophagy.yaml
    sha256: a891d3da5ade68c9b446205eb73d7efadbc3fbfc40a6baf7aa20bcfb048102a8
    role: context
  - path: data/traits/physiology/serine_arylamidase_activity.yaml
    sha256: 5c5b23360b62089496c5ed854287af7d9f3f7268d8621198fb6adf8cdff61db8
    role: context
  - path: data/traits/physiology/siderophore_production.yaml
    sha256: ed039a5696153b032170941bf0edf61989d8f72cfc65e40a7071d6a8cd432a87
    role: context
  - path: data/traits/physiology/siliceous_scale_production.yaml
    sha256: b7a45853488a07e0c7372f1fa0987de606914dde1a43e267792fbef463f43c77
    role: context
  - path: data/traits/physiology/sos_response.yaml
    sha256: 0a4f18289d61db084439951f81f4b8486201fb14a18c19cb3c3dbf3367b3f5b8
    role: context
  - path: data/traits/physiology/spore_germination.yaml
    sha256: b614eb85872d7301bf8cac01d04ff4688047b379e0c2a97fc39af0cfad1e8cdf
    role: context
  - path: data/traits/physiology/stress_response.yaml
    sha256: 893593024d19d52ac1174e02bafc5999f2e90a5e353dd26cd6b39f4e0ae43869
    role: context
  - path: data/traits/physiology/tetrapolar_mating_system.yaml
    sha256: 44515040da7f3011d0fb5b587f0e794fb7fdb637a8394c40dd3328e32c654b57
    role: context
  - path: data/traits/physiology/thermotaxis.yaml
    sha256: ec05ef17681845a69777b06a411f043942fd7693ce3049e0f9b25ee487b5977d
    role: context
  - path: data/traits/physiology/thigmotropism.yaml
    sha256: 520870e0134895cd020b093ca0105c193d9f5810b79490ffc065e4878a0b6172
    role: context
  - path: data/traits/physiology/toxicyst_discharge.yaml
    sha256: 8553dca5db86072e2f67dd98a6a9b62fdfa1f79867c86412bd633071d5969638
    role: context
  - path: data/traits/physiology/trichocyst_discharge.yaml
    sha256: 28fa02e24da45affcf679d8e538978a2aec2c7cc02d31e8ac07bd551e85735ad
    role: context
  - path: data/traits/physiology/tripolar_mating_system.yaml
    sha256: 9a59fd392498bd4654af4f9e8eeed61f67a22efb93412c277b8ddf826b6c7b54
    role: context
  - path: data/traits/physiology/trogocytosis.yaml
    sha256: 4216391d2fa2e78d1e0231da46349ba760c7307822f28bf4b473105984ef818d
    role: context
  - path: data/traits/physiology/trophic_type.yaml
    sha256: 3ab7f5c252d73b6c2418594b9ee019a23a8872a7e837f30668ab5278bd431822
    role: context
  - path: data/traits/physiology/trypsin_activity.yaml
    sha256: f765f433804224fd2d20e72d95dc9806205b24dff5f4acff368e95a3f74e459b
    role: context
  - path: data/traits/physiology/tyrosine_arylamidase_activity.yaml
    sha256: 2d6b86f593971371583c3f6b2e946d12993e43b376bf6e2c7c0d72e8404edfbc
    role: context
  - path: data/traits/physiology/unconventional_protein_secretion.yaml
    sha256: ee6348af35e9e65717ef65f18c26514bb4a6b886608d8b5fdbda97f99c5ffc00
    role: context
  - path: data/traits/physiology/unequal_protein_aggregate_inheritance.yaml
    sha256: 86186530c7d91267bc58928b5b11ee756a2680f86c98d3f55e7dfe33a6a2b228
    role: context
  - path: data/traits/physiology/unisexual_reproduction.yaml
    sha256: c81a642fbc9a5bccfe7fd3bfa2daa8fd4e4d229d4344b2db8958fa0511c7a317
    role: context
  - path: data/traits/physiology/urease_activity.yaml
    sha256: 26e9f7213b4b52ff906f5cfc191f4b74c06a188e85eb7a23bdec8670db6f6787
    role: context
  - path: data/traits/physiology/valine_arylamidase_activity.yaml
    sha256: 30432a644bb87a25d0ccafd4a0599fe938ed87b01654804a830cd74f9c365750
    role: context
  - path: data/traits/physiology/viable_but_nonculturable_state.yaml
    sha256: 42d6af9aacd5bd697a2363ffbfd7f5f300ca9dea054416dde45c57815718112f
    role: context
  - path: data/traits/physiology/viscotaxis.yaml
    sha256: 0c612901dffb6cb468180bf97e7cc891e31f723eb5aa55b65177837c86edd701
    role: context
  - path: data/traits/quantitative_property/has_maximum_observed_value.yaml
    sha256: dce7a6f58e5ad11f88d2800d2dc6b4ec261f2e5a7d6f7179ddfd60878b48e456
    role: context
  - path: data/traits/quantitative_property/has_minimum_observed_value.yaml
    sha256: e514f181bcc0484824d3f080367a64bbb161f8e04a39f73faad6307031192167
    role: context
  - path: data/traits/quantitative_property/has_observed_spot_value.yaml
    sha256: dcbaa25988272078a39f0c592245c29c134537467d020109536f8d6204e6093c
    role: context
  - path: data/traits/quantitative_property/has_value.yaml
    sha256: 19af535e04f3628b6f153c64595eb0c0f95d2160538caf19871cf224ed874dad
    role: context
  - path: data/traits/quantitative_property/has_value_comments.yaml
    sha256: efb61e59ec2568a68b431e63c9bfd8c852aec40b42a47da76dc04b516ac4e0a7
    role: context
  - path: data/traits/quantitative_property/is_negative_data.yaml
    sha256: dc5cc0f1c2262e49c8bae26a9a256b764438455afdb5a75bfde833c2cfb775f5
    role: context
  - path: data/traits/quantitative_property/observation_data_property.yaml
    sha256: b7d6a2365a499b42aef7afc9c92cf951c58dd745b1887cc57ecc55fee64c29b1
    role: context
  - path: data/traits/upper/biological_process.yaml
    sha256: 1cd0eec88f0d11c0fdfdbfb67b73ed32c781816fa1091d7629982e797aa4c2be
    role: context
  - path: data/traits/upper/chemical_entity.yaml
    sha256: e683cab94ac572acf84b51b498f170bf2761a7bae7a0ab2f4ddda43866153bb1
    role: context
  - path: data/traits/upper/enzyme.yaml
    sha256: 41519ed021c8c85f04f815fecc8b6ef3ad1110998704ae6a254eed8d36c643a8
    role: context
  - path: data/traits/upper/material_entity.yaml
    sha256: 6c114247286bbfe64a3f8dd97dcd70f4363ef54adcc11c356530142a0e26686e
    role: context
  - path: data/traits/upper/microbe.yaml
    sha256: e293dda2cd334eb0a6f383731cf5d2db5aa32d4e349c75846918fe87819fbd5e
    role: context
  - path: data/traits/upper/observation.yaml
    sha256: 86a08f2afddef08edd1b2927c1581f9e3575afc4789033449eecae432c2074d4
    role: context
  - path: data/traits/upper/phenotype.yaml
    sha256: 502760fa1b7179bf4e25ab56ecb91d0b25d5f50ed5cfe44133c63a9b821cc4a4
    role: context
  - path: data/traits/upper/quality.yaml
    sha256: 16a6aca8b74ea96e3c889d10264328e240e1b63729715ba99a9131ef7009c66d
    role: context
  - path: docs/CURATION_PLAYBOOK.md
    sha256: 735e9b810471da9f7d8364e35ffe1e741edb3421480dac01727db6ea5aa65da9
    role: context
  - path: docs/GROUNDING_POLICY.md
    sha256: 891678c983c2283a47c81c47950b35753981e9339d105f3bbdda92a1f5ab7f42
    role: context
  - path: docs/METPO_2026_06_12_ACTIVE_REVIEW.md
    sha256: 258b607c347a56e862dde7c54192b965ff06ba2c2f807944fb46f2226f39fdc3
    role: context
  - path: docs/record-review-profile.md
    sha256: cac714488cad03263ca3847737d5f70d174d40b5be677a09e0c1d9c814d9bc6a
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: history/README.md
    sha256: f795a191e17978454a8bb80da91ed6873a9405a240e6e5758837dd9bdc3b5c07
    role: context
  - path: history/infrastructure/add-trait-transcriptional-memory/2026-10-13T004059Z-codex-ff5aec.yaml
    sha256: 174e5aca9a315bbb08fa8fb9fb199ba9ec824666f7fdac9d9ac24f2b36b4a9cc
    role: context
  - path: history/records/enhanced_transcriptional_reactivation_memory/2026-10-13T003746Z-claude-code-cf0b17.yaml
    sha256: c143617c3b8d0a3abefd6daa3553ea2e826e587e09bb47d8af6220e3984eca13
    role: context
  - path: history/records/enhanced_transcriptional_reactivation_memory/2026-10-13T003824Z-codex-8495dc.yaml
    sha256: 30ed31fd21e2eb2e0c61d1765adc1eced0c968fda01ff9b919e7acdf60d5cd30
    role: context
  - path: justfile
    sha256: e6047ea612115a6a78d100b281483ba824c860c3def59bcd0d40e7fb56b3526a
    role: context
  - path: pages/browse.html
    sha256: 943697b7813c9932f72bddb4604d27ba14112fc658e61a6d1927163b00f1fdcb
    role: context
  - path: pages/category/ecology.html
    sha256: 541006f9f16638590aee7cf8a158eedb07170e3928e3f9214515adc931852ff8
    role: context
  - path: pages/category/environment.html
    sha256: fcbb07d52efbfbe89146410258877b730e38b909acd432b32a78c4eb89528100
    role: context
  - path: pages/category/genomics.html
    sha256: a2d6c3ce4e00c851bdb7a0ba1718b36f2077ca007bfa9fac2f7733e8f02f52a1
    role: context
  - path: pages/category/metabolism.html
    sha256: 257ce3c4a61f038f86c976462ace06654f71e4752833c4b8b3eaed06c25d1dee
    role: context
  - path: pages/category/morphology.html
    sha256: 9aefb1d418a0a945f8f86fbf870ec9ae9c809d09c89676ad5b2abd8c37c8e48b
    role: context
  - path: pages/category/observation.html
    sha256: 3bc4d89df93ae830f5bdd535631972df3adc607d4d79b4ad4e49b91c3330643f
    role: context
  - path: pages/category/other.html
    sha256: bdd1236751e6d60978fcb463f780768279c579f727f796cee296d1a9599b4917
    role: context
  - path: pages/category/physiology.html
    sha256: 6c4d4d267089f3d1bead5c07845b082ff29e1fd3ca1a63bf71eaa131f5638d31
    role: context
  - path: pages/category/quantitative_property.html
    sha256: 6a0c6aa866912f392e93a7fc09111e7ed224b14d3574f68d3ff6e1f4bd102c9f
    role: context
  - path: pages/category/upper.html
    sha256: f4dd790e5099ed1f7da02527874496dbf003857361395e0ff28426adf2972704
    role: context
  - path: pages/graph.html
    sha256: b3bcd743937b8e5771b64fcf4f65dd385b6f4e77730c276251b45b51898dab31
    role: context
  - path: pages/index.html
    sha256: e4295519b82050fa5eb8968af0006db2346375ad6d5aaa7423a745a6ece1ccec
    role: context
  - path: pages/traits/ecology/animal_pathogen.html
    sha256: 1c822bcc22bbfe92e56c3b0d7941a0172e7b501b2eeb64d0135cbf1ecafcc95d
    role: context
  - path: pages/traits/ecology/bacterial_cannibalism.html
    sha256: 751abd44aef767eb089dc1100cbccf02de52a1639141d00794f6aecea1c9bdf6
    role: context
  - path: pages/traits/ecology/bacterial_mycophagy.html
    sha256: d54b758b28c80bc54196b98dc2295b7e340bcf32ed61a2fe3c066cc43df59f88
    role: context
  - path: pages/traits/ecology/biofilm_formation.html
    sha256: 9321997e5b715a7691e2187586f94c701147aa3915c15233fbcc70f0f1df97fe
    role: context
  - path: pages/traits/ecology/biosafety_level.html
    sha256: b11411774dcbde3bc875bafc88d981889836307f14210a0e987c3d332f8d7db5
    role: context
  - path: pages/traits/ecology/biosafety_level_1.html
    sha256: e6858af9e6cd117b76d9a366f04b75d1f358b447a33f8ed77a2de26468de40a9
    role: context
  - path: pages/traits/ecology/biosafety_level_2.html
    sha256: a24ecaf70ff00e3a93927c83a4fdf5e4f7149998c259d8ea244dff476abd1e3e
    role: context
  - path: pages/traits/ecology/biosafety_level_3.html
    sha256: 4bae366edd60a2166db5aa75f94dbc2e79077abcf282312506d6914745805bb5
    role: context
  - path: pages/traits/ecology/biosafety_level_4.html
    sha256: f12e6e1e078abd71d596deb283d4d73dceb7bf1a065fdb6fab394f37221d49ba
    role: context
  - path: pages/traits/ecology/biosafety_level_5.html
    sha256: 061241b9537398d361812cfaeee97987306373001cfe085a5f77580c4b2572ef
    role: context
  - path: pages/traits/ecology/collective_bacterial_predation.html
    sha256: da32cfc90e9c86767d264040521415c9086114983868afd389cc5f19b3e8b949
    role: context
  - path: pages/traits/ecology/commensalism.html
    sha256: 41e17f75118add91ef9bd45340d951ac34183b02cc9627fb3b4b21647b5ecc62
    role: context
  - path: pages/traits/ecology/cytoplasmic_bacterial_predation.html
    sha256: 6181fd62c113fdaede17d8549499125a69e2e9136620c762148ed417ec10d36f
    role: context
  - path: pages/traits/ecology/endophytic.html
    sha256: 0ceb247be57af011a7cd66b4953ad906da0d8b3a5ff1cf14d425fec6fa1d7554
    role: context
  - path: pages/traits/ecology/endosymbiosis.html
    sha256: 69e750798da50c5c82319866bebdde824b55e5317d14ecba3e11f271ea47ce4a
    role: context
  - path: pages/traits/ecology/epibiotic_bacterial_predation.html
    sha256: bc30f5bac05a4b3e92249f2cc35ca8c572b76e8ed34c23c42a079edc70b97386
    role: context
  - path: pages/traits/ecology/epiphytic.html
    sha256: 5db7c80b4b0097a01c6716998e34e782b3f4f5a6657d5ce9447dd5d77d0a5aa1
    role: context
  - path: pages/traits/ecology/free_living.html
    sha256: e4c48f4161f483585ff981196bd4921b2969c9abc6bd1f64292eeb42a2cf7dd6
    role: context
  - path: pages/traits/ecology/gut_associated.html
    sha256: 8b043ecb2e9044732385aa40f5ab44d4ec1a2ab40152fb476d454674ae54edbb
    role: context
  - path: pages/traits/ecology/habitat_association.html
    sha256: a388a728162264b0c8dc7546954bd0fdf36c94f962adf8513b5fe1ed3fdb971e
    role: context
  - path: pages/traits/ecology/host_associated.html
    sha256: 4cd0318f23c9a5bb842f02d5ec42e3dab96c2067bd9549d009ed9be6334359fe
    role: context
  - path: pages/traits/ecology/human_pathogen.html
    sha256: 4cb3e0e74a175c173d0f322d150a0f2d556cb48f820c11bf8949e25258224767
    role: context
  - path: pages/traits/ecology/ixotrophy.html
    sha256: e4b60dda5569831b1c73eb60d71016671d62c663537f60a9fa5694e1db66d6ad
    role: context
  - path: pages/traits/ecology/mutualism.html
    sha256: aaa4b805d296ef4b05fe6d9ceb15de7e4c811d4ff7b3bb1d039394caa6087a36
    role: context
  - path: pages/traits/ecology/nitrogen_fixing_symbiosis.html
    sha256: ceb9c332f43651e3179d2e9efd658692c0a7160964acc595e3288fc6069bfbe7
    role: context
  - path: pages/traits/ecology/opportunistic_pathogen.html
    sha256: b8e07fcf95bdd39372c5bbe707702f81e3dbfa1ac47b235d5dc0c9214476917e
    role: context
  - path: pages/traits/ecology/parasitism.html
    sha256: 8e5271144a762d8a0ac3152b75f8610ad6bdb270498b2db812220fa235c5441d
    role: context
  - path: pages/traits/ecology/pathogenic_to_host.html
    sha256: fc3d4ce71d1950877bb6133d5f4a46fa8e2d348c1a2e989db6ab3ed2369c680a
    role: context
  - path: pages/traits/ecology/periplasmic_bacterial_predation.html
    sha256: dcbec3f5d123e8462ada19dab44745bccd5ee56c15dd2794daee713cd8cf7950
    role: context
  - path: pages/traits/ecology/plant_pathogen.html
    sha256: aacc94d2018e72807e6481297834c3a15d580de1c3378c3c1588a048712101fb
    role: context
  - path: pages/traits/ecology/predatory_bacterium.html
    sha256: c74851d269aeb55ee05f3b54bdc46034f78d4a303a04d3d8113558f7e551016e
    role: context
  - path: pages/traits/ecology/rhizosphere_association.html
    sha256: 1f016973652ecf01f4ffb49226d3b2ff5bc40373c8f7ffb6caac7a7573d85e6a
    role: context
  - path: pages/traits/ecology/saprotrophy.html
    sha256: 63487237750e1110794f2ced193725d83f11b7e02adc8f7870098d18868ec88d
    role: context
  - path: pages/traits/ecology/soil_dwelling.html
    sha256: e099d19b08fd13529c54afd2a40610c265d021bf2a3a89a98bf6a27720214326
    role: context
  - path: pages/traits/ecology/symbiosis.html
    sha256: dd406a075dc691113f5e9c1b7f372d5450847bbfe25ebc2903d22d97614c6217
    role: context
  - path: pages/traits/environment/acidophilic.html
    sha256: 8c7b1844563c54bd852c2e14346ce76c6f03a29e83acfc5f920991d272ed22cf
    role: context
  - path: pages/traits/environment/acidotolerant.html
    sha256: 118b51f9925452f80f055f4024fe6397eb2906e7ab1ac3015ed0b87c77cd20e5
    role: context
  - path: pages/traits/environment/aerobic.html
    sha256: 0ce3bd1648bfc6015e262a4e02960d0bda356595f90af12d5a3018c7be4264b2
    role: context
  - path: pages/traits/environment/aerotolerant.html
    sha256: fef02bfec3f5027d333b95e0424081a2db61d27676b4b88f425dc7e589dd3578
    role: context
  - path: pages/traits/environment/alkalotolerant.html
    sha256: 748d18a158d65703c04fb19a5b291f300d1e24309e0eae040337b5dc306fa879
    role: context
  - path: pages/traits/environment/alkaphilic.html
    sha256: 555d0cc4af061a9f03c974c23e1493e0ce6c19d69504480e8fc1904dcae787d0
    role: context
  - path: pages/traits/environment/anaerobic.html
    sha256: 662e90f5831ca031505cbd8d8afcedebfe580b1b5aa08b1a1cf0cf7f796a78ee
    role: context
  - path: pages/traits/environment/arsenic_tolerant.html
    sha256: 35ada06b75202b54af67230fb1dc6a101947377453692c0727654fbedf32bdbb
    role: context
  - path: pages/traits/environment/cadmium_tolerant.html
    sha256: f64799cd65e5849caeb2a2300f85374e0215057f60f3ddfb535e1b4d07c2ebf8
    role: context
  - path: pages/traits/environment/capnophilic.html
    sha256: 7db6ea7a756415755dac209a2859c40d21aced42ab8c81c2137606959115ebf8
    role: context
  - path: pages/traits/environment/cobalt_tolerant.html
    sha256: cb66f6606325ef00d3a5f842db0fa9568a75189f550f19d15ed232b9e81db260
    role: context
  - path: pages/traits/environment/copper_tolerant.html
    sha256: fb6d2d5732a548847a16b986e6875a050aa3222cdbc699cd29a64c67bc7db3a0
    role: context
  - path: pages/traits/environment/delta_phenotype_with_numerical_limits.html
    sha256: 8fe6794d8a3b10a46a87c8bcfece7ae73b7879028b21dbf42a4d027deb0f64dc
    role: context
  - path: pages/traits/environment/desiccation_tolerant.html
    sha256: 59c0924a565dfe45e87f179aa7da9afe8cdc901dc3725db4fe3b77fa77347a9f
    role: context
  - path: pages/traits/environment/euryhaline.html
    sha256: 2307b1fead7a0dbfc7ac7a5ce50440fb2f90203e3ac6c487eca875e9d837fdea
    role: context
  - path: pages/traits/environment/extreme_hyperthermophilic.html
    sha256: 83cba9291a88c3013597669b35e5ebada8d2a29179b9e7626416dc7bdb589994
    role: context
  - path: pages/traits/environment/extremely_halophilic.html
    sha256: 7a8202f2550fdf9b9949bf3eb0311e5ffb4c2e7545a2f62424dbdc01e90e203c
    role: context
  - path: pages/traits/environment/facultative_oxygen_preference.html
    sha256: f70e6f017d22e67e121dbba1bb3269e0089c17e662bb5260083e5f0c208dc500
    role: context
  - path: pages/traits/environment/facultative_psychrophilic.html
    sha256: e14cab9272a877329892d74528ade6e4e292231d0c84c9e5bb752a3f1678497d
    role: context
  - path: pages/traits/environment/facultatively_acidophilic.html
    sha256: 53ad9ab0fce46d4537de48836141738ce1a09fc60e950f0408c632b63fa453ca
    role: context
  - path: pages/traits/environment/facultatively_aerobic.html
    sha256: 87527be8d256593a0442a03a309082f987a2f8ec0894c6cee39e848288766ba2
    role: context
  - path: pages/traits/environment/facultatively_alkaphilic.html
    sha256: 5c7dfd792f851788d988c22e5a76f87fdd40fed869e3089ce00c7c9e2c3eb1f6
    role: context
  - path: pages/traits/environment/facultatively_anaerobic.html
    sha256: 2f25f1f206f67dd22c9d38460f677b52a021451986a0bf42d39b1ab5f0afebf0
    role: context
  - path: pages/traits/environment/growth_range_phenotype_with_numerical_limits.html
    sha256: b2ab3f87314ef0032187c45f446969e4de6c94a4e434d05c577fb95ff19a4a08
    role: context
  - path: pages/traits/environment/haloalkaliphilic.html
    sha256: 8de0e710fdc2074352124c36346002a82cbb996054ebb8203b04ddf9a204527c
    role: context
  - path: pages/traits/environment/halophilic.html
    sha256: 7e85c75101a95705c655c44e505a0d0e84bbac4e6974dfcb0d6d09679fd95116
    role: context
  - path: pages/traits/environment/halophily_preference.html
    sha256: f47a25a4491f60fd3e411a63a378bc51d9f8e477b97fb3ae685a0ebf078618c8
    role: context
  - path: pages/traits/environment/halotolerant.html
    sha256: 75526797b3e4a3931286d8a6fc167488ac4f6407e8b3b38c2139588f98e471a2
    role: context
  - path: pages/traits/environment/hyperthermophilic.html
    sha256: 71634d3b80b2fb0fff49fd780317293302ae699f83b826e0db251cae0affb828
    role: context
  - path: pages/traits/environment/ionizing_radiation_tolerant.html
    sha256: 875bc5618d4bc47544433174904319629bb8f3280d52add29d873324429aa751
    role: context
  - path: pages/traits/environment/mercury_tolerant.html
    sha256: fb0715d86eca995fa9bee9f4a62b317903adf719ab5e096c205685e6f3fd89e8
    role: context
  - path: pages/traits/environment/mesophilic.html
    sha256: 7dba50f7caa02355e95e6b71a37e57a8fa615ae3705b1b6de71e2203112c775d
    role: context
  - path: pages/traits/environment/metal_tolerant.html
    sha256: a730821e91ea8de04e837e9c33c9524424e99e0b088edcf595942e7d5a177c33
    role: context
  - path: pages/traits/environment/microaerophilic.html
    sha256: f03b4082a62f4fe174e35a74b9a376ce43dc82785ec1c9d023ba5c556dc2ecef
    role: context
  - path: pages/traits/environment/microaerotolerant.html
    sha256: 338837781ef9a766441ba3b7bc1b6fe6b7d162a4faffb27e204ce0a5c2eff0ea
    role: context
  - path: pages/traits/environment/moderately_halophilic.html
    sha256: c46c1973de619aead22a8bd129b574170a1a3bd69bd4b00df36efa85765f0606
    role: context
  - path: pages/traits/environment/nacl_delta.html
    sha256: a31f51c02e8c2940f217b519292eb77efed95158f47dc25924028f1e3a25b5a7
    role: context
  - path: pages/traits/environment/nacl_delta_high.html
    sha256: 4c49432fc4ecd974241979394583b10f1d37e935c28f72c129a8516c11bc3fee
    role: context
  - path: pages/traits/environment/nacl_delta_low.html
    sha256: adcd234d75f060ac9e8494b4243382cce2912375e32ffafc12e6345f12173dba
    role: context
  - path: pages/traits/environment/nacl_delta_mid1.html
    sha256: 6bf2cfcb3c76989ec136da31493140e2719a6451fbd74fe7b070db6ce6cf8153
    role: context
  - path: pages/traits/environment/nacl_delta_mid2.html
    sha256: 566290941f9a13b59fde5f6f51be3ec76254febf2f34bd3373d1e48ac9a075a7
    role: context
  - path: pages/traits/environment/nacl_optimum.html
    sha256: 700aaec00260053ed7b99044e566dca5a0118b603be0ef57d4a8675801a904b6
    role: context
  - path: pages/traits/environment/nacl_optimum_high.html
    sha256: 814d49793e668b8dcf0ca5ca5644b4fe0bcb813b451d8cca7396e5278554c6d5
    role: context
  - path: pages/traits/environment/nacl_optimum_low.html
    sha256: 18781b1d43b5f742cffaf4ccb0e7ef1342b463d1d7e84c90c62becdd40760d07
    role: context
  - path: pages/traits/environment/nacl_optimum_mid1.html
    sha256: 05e10f427f473fcfe3922724076a8c8cbef911cb8ddb30e6aa3e746aa6e99ddf
    role: context
  - path: pages/traits/environment/nacl_optimum_mid2.html
    sha256: 1d2cef0c7ec89f26cface3b88e2706edb464b9fd99fe14ecc5b3dea51f613bf8
    role: context
  - path: pages/traits/environment/nacl_range.html
    sha256: e13e482dfed687876bbf2cccf5289500e5a84e8f6aae12b917b4d1bdc824fb1c
    role: context
  - path: pages/traits/environment/nacl_range_high.html
    sha256: c79f52ff683fe94a6c2f3b0b53885edb96f05331276a3778d7da7147ceb9e734
    role: context
  - path: pages/traits/environment/nacl_range_low.html
    sha256: 887f9d138148c40ea92f1744986ed35a46f1b61441bca20629fd356212298492
    role: context
  - path: pages/traits/environment/nacl_range_mid1.html
    sha256: 4b260fa9c904e7174178ea3ba1d4295ac4aa4b098174b2dfdb08039ff5a655f3
    role: context
  - path: pages/traits/environment/nacl_range_mid2.html
    sha256: f40d5988ed0edb37512eaad1c45d047cd0606b191d917263ecb8a9408d866c2c
    role: context
  - path: pages/traits/environment/neutrophilic.html
    sha256: 9ba98d6235684053f3054ff8a828aedf42884c7a1f022669f89c8e8503287e8c
    role: context
  - path: pages/traits/environment/non_halophilic.html
    sha256: 5d813b383503dad2cfe492b7fe324e3f11eacb319a999d16a2cb81c7733705f1
    role: context
  - path: pages/traits/environment/obligately_acidophilic.html
    sha256: 7cbb685c4aa9648f7c3c0db4b80024e4a9b2dd6e0cfd07361c1a754c34de1af2
    role: context
  - path: pages/traits/environment/obligately_aerobic.html
    sha256: fb07846da2790e57a2abb6fef4f610f8efdd5892ef4414a8b97a6b1c579aada0
    role: context
  - path: pages/traits/environment/obligately_alkaphilic.html
    sha256: 7e8a22b1e67c4f04b9b335d45c26895296f135a402e488d31bcb2e3a37e8e820
    role: context
  - path: pages/traits/environment/obligately_anaerobic.html
    sha256: 461869fbf8501b0a308bc500cd7626e38231373612399fe08702ec6432e32a9d
    role: context
  - path: pages/traits/environment/obligately_piezophilic.html
    sha256: 50cf84134882ec2a70c937fecef1a7e8f69a4937defa856623a2c2466533fa83
    role: context
  - path: pages/traits/environment/optimum_phenotype_with_numerical_limits.html
    sha256: fd9933ad3d76841dda900d5361fd224b1515d7aeabd203f9cda966912f291e60
    role: context
  - path: pages/traits/environment/oxygen_preference.html
    sha256: f1b75a2e6a9c973c22cb43b8cdf02c564bbf3e89327c8b54c5f823fb4f83e66a
    role: context
  - path: pages/traits/environment/ph_delta.html
    sha256: 616ab9c8d547e1c2cb265d7b5b71c8151c727abe0829f101ea4676eabb387550
    role: context
  - path: pages/traits/environment/ph_delta_high.html
    sha256: 11ca045d99772270f1bc52c8e55bc7b3f4924e8a3a491494653f96786653dfbe
    role: context
  - path: pages/traits/environment/ph_delta_low.html
    sha256: 078f227e5886de04d8d7975a88bbc60af7fe2a1c2e276a66a927699b5d9114c3
    role: context
  - path: pages/traits/environment/ph_delta_mid1.html
    sha256: 9017bd735dcaa0185fc3255a5b1600b4d66fefcc386d4d996170fc83098a335d
    role: context
  - path: pages/traits/environment/ph_delta_mid2.html
    sha256: d938253a4e191a4a9d6510ed774c812ada710484cd3368ff4a02bdcb14f33495
    role: context
  - path: pages/traits/environment/ph_delta_mid3.html
    sha256: 547486f2ee384d55bd2294ac56ff260d8b974743fc6612f229f4e162390244ce
    role: context
  - path: pages/traits/environment/ph_delta_very_low.html
    sha256: 98b84c63a9d01baab0458efd0ed248292d0e167dd8545db88073836eabdf2e14
    role: context
  - path: pages/traits/environment/ph_growth_preference.html
    sha256: 9fe11c61a794d1f9fd46861879b5094a0e9be2591d8f0450e0a2f9095e0ea168
    role: context
  - path: pages/traits/environment/ph_optimum.html
    sha256: e2f5656e020c3355ea147078c7e13fc0ee07c0d59d71a947fa653e1d58d4d9ab
    role: context
  - path: pages/traits/environment/ph_optimum_high.html
    sha256: d56b2eb8250db32bca2ac1d6bd0c947e15115643d913afba05ee8fb92875aa8b
    role: context
  - path: pages/traits/environment/ph_optimum_low.html
    sha256: 34be14a03cf74e100713ac7a42a9cb03b6a69a4531bd448af963e6b015278df0
    role: context
  - path: pages/traits/environment/ph_optimum_mid1.html
    sha256: 1bf3d7a9a2c9ebdb661e27ead3f900293f6b242d80abab2506dba3aa043e7df6
    role: context
  - path: pages/traits/environment/ph_optimum_mid2.html
    sha256: 973309ff2ead50db489e03044c1312c03b55f256a3865aabbdbe4a90b9d5fc64
    role: context
  - path: pages/traits/environment/ph_phenotype_with_numerical_limits.html
    sha256: b3223530a03ba0459a3e6a045c7fac5de915a2b05acb21541aa58ea92d672bcc
    role: context
  - path: pages/traits/environment/ph_range.html
    sha256: b23c65c8e64f0494eaba895c38c7c0256a99c3e91f6cc9aa7c340ae878e1b63e
    role: context
  - path: pages/traits/environment/ph_range_high.html
    sha256: f5c584290127fd10ec3b2986020704ac576190ac6d7e2a15e0881876b2da5d17
    role: context
  - path: pages/traits/environment/ph_range_low.html
    sha256: 4568e7d123de92ef341c21f23babd9c87f45b7fc7e56ba052a0e0d46b5ab6d80
    role: context
  - path: pages/traits/environment/ph_range_mid1.html
    sha256: 3268fc8fc8330dbc9fb9974e9c066e85dc5188fd1776847dcab724b578b55e29
    role: context
  - path: pages/traits/environment/ph_range_mid2.html
    sha256: 0856bde402460c945c55d37292462fd422464eb9c036a94b6033a2553a8884b6
    role: context
  - path: pages/traits/environment/ph_range_mid3.html
    sha256: 4ead1f89c6e6fcaa28799e4ec5d67866258ccd1be2d159aa580ef07daf0e231a
    role: context
  - path: pages/traits/environment/ph_range_very_low.html
    sha256: 3be3bb721546eb59c9e901e14982a5480dae7a1d0b66031af6a7c869eecf374b
    role: context
  - path: pages/traits/environment/piezophilic.html
    sha256: b47f448690356f6f0da8b31f39400beed30a3eb1d649d5c0e658bb929dcd621a
    role: context
  - path: pages/traits/environment/piezotolerant.html
    sha256: 78c2f6c3d2fcc58d5130b1e8a011077617ae5655186a528662043a2deb5eda43
    role: context
  - path: pages/traits/environment/pressure_delta.html
    sha256: 34b7494a50158b43e03b7881aa54e2d595bbfdf6cc28a912fdece67095ab4cc6
    role: context
  - path: pages/traits/environment/pressure_optimum.html
    sha256: f15cfa10069e47482fdb23a41d577631283d015dd163069f898d4ddbe1f41358
    role: context
  - path: pages/traits/environment/pressure_range.html
    sha256: 9157359b8effa62b550979e295d6c3900458c24b4e51b9fc1714cf1b00986f89
    role: context
  - path: pages/traits/environment/psychrophilic.html
    sha256: eef691090a8705827cd898b9449fb7e2372e4dfd7690f8f47689a8646219aeab
    role: context
  - path: pages/traits/environment/psychrotolerant.html
    sha256: cfb6ab913521e81bf9acfe139083a6e401761f4914dd2df4c7d7c1f3d68043b9
    role: context
  - path: pages/traits/environment/radiotolerant.html
    sha256: b117cfa2867a0c053e3d3a2cf472f3d1826d29c7b6956fe6dfcd7ab6d4b7fc14
    role: context
  - path: pages/traits/environment/salinity_phenotype_with_numerical_limits.html
    sha256: 69a7718b3ab23943509b5267c4a31b2422901d9415f3e875839bdf800f04afdb
    role: context
  - path: pages/traits/environment/slightly_halophilic.html
    sha256: 809a673949fc77628c8f6ffc49afc9226314f46ee152ef4a7a79183776787555
    role: context
  - path: pages/traits/environment/stenohaline.html
    sha256: 0f34a25cc666ebc47c7d488101add899269048b6ea4703ee464b5eb743c2dfb8
    role: context
  - path: pages/traits/environment/strictly_anaerobic.html
    sha256: 3bd89d423a241de01025f28d70ac9c2bee49bc20158e491933549eedba00a265
    role: context
  - path: pages/traits/environment/temperature_delta.html
    sha256: ed23597794babdf28b4f01894c402db42a93d317aa8b41148aba540b5d07586d
    role: context
  - path: pages/traits/environment/temperature_delta_high.html
    sha256: 3ec6a7ae34ce084484d63f50efd662ceb95e368540538a867f056db31b633099
    role: context
  - path: pages/traits/environment/temperature_delta_low.html
    sha256: 7542583d229ea8d3ed183980c6a60ee82fb7b2824f7ef5f0b87a9c1a49c1c4c6
    role: context
  - path: pages/traits/environment/temperature_delta_mid1.html
    sha256: dd28733584fba4294f6a2b6830cb0039ce943d1113c858de21c5fa57127e997d
    role: context
  - path: pages/traits/environment/temperature_delta_mid2.html
    sha256: b08e0839659a62494faff5ef474d72dadbefb838561a4bb582afb0ee216bdeba
    role: context
  - path: pages/traits/environment/temperature_delta_very_low.html
    sha256: ad5a385bf4b29b34567af67e0f33e9384eeb407717e4525ff327977737a757d6
    role: context
  - path: pages/traits/environment/temperature_optimum.html
    sha256: 70e7244cdc7841262f95c13fc3b2ff38b314be949ba1b5340aac7f1e3a616b1b
    role: context
  - path: pages/traits/environment/temperature_optimum_high.html
    sha256: 626bd54246ed2d4fb8b5dd3c896df515c0b5f55c163d84a1b96ab63dc282721f
    role: context
  - path: pages/traits/environment/temperature_optimum_low.html
    sha256: e76e7ff57eb82ead75017719b59ef774404b490130afdff8507b223353cc511b
    role: context
  - path: pages/traits/environment/temperature_optimum_mid1.html
    sha256: d5ef7fe4ba8613c2564bb7d2b23c55b9aafb91ba223277cbcc0630e1dcb0dc89
    role: context
  - path: pages/traits/environment/temperature_optimum_mid2.html
    sha256: 94bcd87b3a7be5094b729ed9add519ccc81fe50d270223a13912f9cb41aa1d3e
    role: context
  - path: pages/traits/environment/temperature_optimum_mid3.html
    sha256: 6990bd2485c73c2e2ecd2d8f292e9f9b40fb4e86eb4f833a108f16508a6e6775
    role: context
  - path: pages/traits/environment/temperature_optimum_mid4.html
    sha256: f708a27be995bfb38ca50e0075bf0fc57cccee2006379d5647797163d6eb4078
    role: context
  - path: pages/traits/environment/temperature_optimum_very_low.html
    sha256: 6c1153433c07cce21946b407163d7c45be1170a299c9e52ede4ec10d225300e8
    role: context
  - path: pages/traits/environment/temperature_phenotype_with_numerical_limits.html
    sha256: 3caa5a5dbbb83564319865104ab746e501af3535135d390e717ec4b928713303
    role: context
  - path: pages/traits/environment/temperature_preference.html
    sha256: dbf98450a0d5726ee0fe5ff2edf96229e848ce73261efa536da575d51b7b3436
    role: context
  - path: pages/traits/environment/temperature_range.html
    sha256: 921e498a5f3b2206abcef57e91e705a7ace73724f9f59079eebc1512fc3c697a
    role: context
  - path: pages/traits/environment/temperature_range_high.html
    sha256: bb709f79c519da3ccae3e2c8ebc170ab21d35cc312f7f224001f3eefdb197e7f
    role: context
  - path: pages/traits/environment/temperature_range_low.html
    sha256: 3d1a0ac2b975c9be0c17a58e9a6bc570b312e0bede6bd52bcd33a9334e0a6c83
    role: context
  - path: pages/traits/environment/temperature_range_mid1.html
    sha256: 261b27dcea99296c7dcd2586b2ac322a9008efcfd0d1ea7d9fe2788d038684bc
    role: context
  - path: pages/traits/environment/temperature_range_mid2.html
    sha256: b363dc0d4e0d787b9d9d8c94022ff16be37f9e66c90e0fa69d95d92ad8f54aac
    role: context
  - path: pages/traits/environment/temperature_range_mid3.html
    sha256: 6b3b27caa356c3b64ffbd7d76ac7eda78b29b03430f0103356de851b89d8b82b
    role: context
  - path: pages/traits/environment/temperature_range_mid4.html
    sha256: 499e13a13868676cf14a173c0fa7825644559a26f7b4f1d10fc07424b02bb505
    role: context
  - path: pages/traits/environment/temperature_range_very_low.html
    sha256: d2b0cf5e066aa2da0a5144b80826f4b1096688f4f0d1acc6ecd8068341a6a0ac
    role: context
  - path: pages/traits/environment/thermophilic.html
    sha256: 64725168caf3fc895c8a9ca160045025f5d54075fa1303cd6b9e50ec849a0a56
    role: context
  - path: pages/traits/environment/thermotolerant.html
    sha256: c5b7bfb0ce95fe195aeadc4f56a51f8960a17adb3d3bd7b3a6982983f5baddff
    role: context
  - path: pages/traits/environment/uv_radiation_tolerant.html
    sha256: 5fe93e8e824d99923935c60bd4105437a90a0821429e19acd6e7d2c65776907d
    role: context
  - path: pages/traits/environment/xerophilic.html
    sha256: d7a7ab9eeee6d9ed338428ffa91f664b51668459a869005226aba4ac8c23e1f6
    role: context
  - path: pages/traits/environment/zinc_tolerant.html
    sha256: 80f750b192b7cb2d6e73bc08dd93b5aaec5b3d393fc85930b8f6d8a2c10e432e
    role: context
  - path: pages/traits/genomics/abi2_system.html
    sha256: 588120d794dd468ee01fea05b282893d0e8a0a2230eaae090cd81f2eed8f0d74
    role: context
  - path: pages/traits/genomics/abia_system.html
    sha256: b516b1034e5b58b434cab6863a0bd739203585ff05169c5f89b1bc38d8254036
    role: context
  - path: pages/traits/genomics/abialpha_system.html
    sha256: 66a2ca4673fdc1489f2fd142d8b51981440cfb692137137cdd39243db797ceee
    role: context
  - path: pages/traits/genomics/abib_system.html
    sha256: c6a6411aa782e3073c7e44a3a17596bf6f06e1ff172722ac7581070529e4f1e8
    role: context
  - path: pages/traits/genomics/abic_system.html
    sha256: 16ad767b1763048e477c299080b6022be7182b2683715db39d6a84d8e1fc4664
    role: context
  - path: pages/traits/genomics/abid_system.html
    sha256: 91e6bd3f45b51810d1225a1419a31f5538855fa57f4a3d42f69711c887dfe120
    role: context
  - path: pages/traits/genomics/abie_system.html
    sha256: 0d55e3512e97392f187704138b8751555752284b2d45560093b5f12447f5618f
    role: context
  - path: pages/traits/genomics/abif_system.html
    sha256: 90ec7e9de4cc14ffd25d86ee7d6bf54ce6cdfe1a530fbd030152a5f855df3dd0
    role: context
  - path: pages/traits/genomics/abig_system.html
    sha256: cb6c550fbdf6bddb51175e36c50772f3ec76ebc620e2e07a676965e4ff76b7a7
    role: context
  - path: pages/traits/genomics/abih_system.html
    sha256: 4705116517d5b9bbe2c162e4bdfc1bfe45201cc628ce291f8b8ad888bf490b81
    role: context
  - path: pages/traits/genomics/abii_system.html
    sha256: c439453b8de2fcc639de65f592ea14f009228ef9af6e6d0147cce1dc30618294
    role: context
  - path: pages/traits/genomics/abij_system.html
    sha256: c9d9b3efe1fbbedc7bc91b829dfc0eb6f2571e81e2ae2affaf6c67cc2713ac6c
    role: context
  - path: pages/traits/genomics/abik_system.html
    sha256: 480fe5d75f6f674d1b508993663b8abcdead4b62be429bd8f1ec9909d603cba0
    role: context
  - path: pages/traits/genomics/abil_system.html
    sha256: 49d3f66fa514d6f4432534541db35228a1c6abe58bbbe4ba374a374d7230bc85
    role: context
  - path: pages/traits/genomics/abin_system.html
    sha256: f63ed04ab903de8c63fd5c2e2cb07bf0eee067d68455793243326a6f519bec01
    role: context
  - path: pages/traits/genomics/abio_system.html
    sha256: 47fac4303a11951a257da98933ada63571094bfc592a061d013866e00d4ff5ef
    role: context
  - path: pages/traits/genomics/abip2_system.html
    sha256: 5ea7d94e1222340a701d55ab41eaa5aeaeff48508c2d56e3b347ef81999c2b1f
    role: context
  - path: pages/traits/genomics/abiq_system.html
    sha256: 8fed4b2d7a02cff70e0354545dc485dffe3f330cc6f2133c78bd9122f1e44e73
    role: context
  - path: pages/traits/genomics/abir_system.html
    sha256: 201d0523c8ca05000fd32044d8ca632c68af1c1e4b35b1bed9f255d9e1926ac4
    role: context
  - path: pages/traits/genomics/abit_system.html
    sha256: b13b3639415f1d72285c156d22ee71a050eb565883693e7aabd51f61d42a6c44
    role: context
  - path: pages/traits/genomics/abiu_system.html
    sha256: 4f566f4644208439ab4a3fdddb4de51f1a528396079f618528776e7222d591aa
    role: context
  - path: pages/traits/genomics/abiv_system.html
    sha256: e42b01e153a4b02d0790ff55b8fde1ab25024d12cd98e1792d8e8421e94dc82c
    role: context
  - path: pages/traits/genomics/abiz_system.html
    sha256: 9143901ba1a6d4efae210d22594e138f64d103fe6052cdceb26a9da902ecace5
    role: context
  - path: pages/traits/genomics/abortive_infection_system.html
    sha256: b77d34ce1506dcb42fd154b22b7d2ed8dd9635d7c85150f22faedc0549933875
    role: context
  - path: pages/traits/genomics/aditi_system.html
    sha256: 6fb3084a40669dd3e466f5c672aa904be9eb633c16472bca9d2bb4e351a29469
    role: context
  - path: pages/traits/genomics/ambrosia_system.html
    sha256: 2a3dc87781b44ee161237b5a253d453e208178ed05303401543859f67cb4c347
    role: context
  - path: pages/traits/genomics/apsab_system.html
    sha256: b5b51d4f894546b567b010f05a3809d64708644558d77d2d1dc823cbea71705a
    role: context
  - path: pages/traits/genomics/aristaios_system.html
    sha256: a52face3e96c6e9d95cac039535249d330615c101cf4c4bf6c174b1c31ef1d51
    role: context
  - path: pages/traits/genomics/armada_system.html
    sha256: 1fc0acddee2c30cedf09e680fb0a8f088779146143d9eaeefd8d4a88347d6547
    role: context
  - path: pages/traits/genomics/audmula_system.html
    sha256: d7138ad1050be8e40e9c01fc05a9f3a5d7e69d95d350e0f458fb6e7e37978cf0
    role: context
  - path: pages/traits/genomics/avast_system.html
    sha256: 525c4acb6ea326138ed1f82f1e69dd097800b31d9613d6d3615952385bfdea15
    role: context
  - path: pages/traits/genomics/avs_i_system.html
    sha256: 4dc8ae4f4b66063312ab7293aa34110294eb507ffb5a48c41ffa3443d2e15ca2
    role: context
  - path: pages/traits/genomics/avs_ii_system.html
    sha256: 633362ee172478f5811ab7be0d21abe798a82ba385a332bab95822c56e0beb29
    role: context
  - path: pages/traits/genomics/avs_iii_system.html
    sha256: a7220ac389ebd0d11d8b26a6e1b3b5ba78e778e1de0a07c9ef32f0a74e6803fc
    role: context
  - path: pages/traits/genomics/avs_iv_system.html
    sha256: 7cc4c0070a31317bb23b754f042aa7eed4a0ccbd66f33f1f9efd49e95bda52e7
    role: context
  - path: pages/traits/genomics/avs_v_system.html
    sha256: 97f0ba46e7f9aabbd7aa8173722ebfc7ab72c1f99ec6c6400932dada7c3067af
    role: context
  - path: pages/traits/genomics/azaca_system.html
    sha256: 466df4a3e2bd7d123a28cfb2d05a78fd88d2616d6c7e2bb4c4d50bf704d7f03d
    role: context
  - path: pages/traits/genomics/belenos_system.html
    sha256: 6d55d2eaf657486ef7fe774b4f718032c56353f3f36747e4b127770cca999aff
    role: context
  - path: pages/traits/genomics/belisama_system.html
    sha256: 1738f80d5ca94532fa01e6d777347bc2a589fc681d3990c5fe4f5af199a033d3
    role: context
  - path: pages/traits/genomics/bil_system.html
    sha256: 7a0c452495caf13e5e7ced42cb8f3b90ddb052136896d2d634edb02181075c31
    role: context
  - path: pages/traits/genomics/borvo_system.html
    sha256: 7ae21cba319cf8fe8b3fb6aa37bfbb6da052f2e3ae1e68192a437b0c2007507e
    role: context
  - path: pages/traits/genomics/brc113_system.html
    sha256: 8ef3d3438aa45d98ffe856a07b6f9a4df94393294495fe45e51938e463815a94
    role: context
  - path: pages/traits/genomics/brc142_system.html
    sha256: 0a244efa3891c5ff77f73b1a596ff5e1b967a9372378666b9ccfe9d2275cf291
    role: context
  - path: pages/traits/genomics/brc167_system.html
    sha256: 62c422b6c3955d8d2e49ebbff775e4105de463c85e52df33bbab2edf310255f8
    role: context
  - path: pages/traits/genomics/brc217_system.html
    sha256: 7475c65434db5f01d7f5b5e225d5f25d2e7d573fd8ad28e34257c049548ef2d6
    role: context
  - path: pages/traits/genomics/brc22_system.html
    sha256: c8d0db583ba977af9a18a6fa3b689725635edf97c1b6e203ada0594a36534b2c
    role: context
  - path: pages/traits/genomics/brc233_system.html
    sha256: 11f008891659d0a73bbbcc3f27c743fa129475e749da2b17eaebff8084a6d13d
    role: context
  - path: pages/traits/genomics/brc23_system.html
    sha256: be28f71ffea779239b53bf7dbc6616be656fc98947a10c63964c937a238a0b01
    role: context
  - path: pages/traits/genomics/brc24_system.html
    sha256: 0205deb87ea81720c87038293a04cc30705a25a9a5ffe4f6a91870fa7fdc1b84
    role: context
  - path: pages/traits/genomics/brc59_system.html
    sha256: 2020876c1aea417cb9599440625197aed80846a4942ae513afb9193acfdd1774
    role: context
  - path: pages/traits/genomics/brc76_system.html
    sha256: a87b43721079b847ee05a3fab96b175644d5b619a84545066013a83d81b3fd84
    role: context
  - path: pages/traits/genomics/brcwgs21_system.html
    sha256: ae9f3f100b3b8af53d7fb475ba786147e7d3ec5928b75464b4072a8e48f2c759
    role: context
  - path: pages/traits/genomics/brex_system.html
    sha256: 22fc60e5f6c491006887e46e563bd21e94dd8c135636732fc6a500c0aeee2913
    role: context
  - path: pages/traits/genomics/brig1_system.html
    sha256: fcf33b40a77504d510a5923289171872cf279b02df43391be6105b08eb643a99
    role: context
  - path: pages/traits/genomics/brigantia_system.html
    sha256: eec507fc11a2236018a243ec6fb61964fd996b35ddfbf497aa0877fef35088ed
    role: context
  - path: pages/traits/genomics/bsta_system.html
    sha256: c387a8902fc25d2571fa62c2c1ebe3725d72e9c25ba0787d571fd871e445a144
    role: context
  - path: pages/traits/genomics/bunzi_system.html
    sha256: 9cbd52fa69a759fb8ba5e69a4c6bb6fe21a57d9db891995680127f603c8ee703
    role: context
  - path: pages/traits/genomics/butters_gp30_gp31_system.html
    sha256: a5564a61c781d08457b24585b5c825a31afcd08b8d80f1693cc811621ec86318
    role: context
  - path: pages/traits/genomics/butters_gp57r_system.html
    sha256: 09f475ad59c2f30a72281cb4c9df669f6f29c2345c1003435545c0dd0fd38a6c
    role: context
  - path: pages/traits/genomics/caprel_system.html
    sha256: 1e9ea789236b1c9b541e42eb005d1dd69434cc4c2575f373367bb950abb4c87e
    role: context
  - path: pages/traits/genomics/card_nlr_endonuclease_system.html
    sha256: fd27ff155439dbccb71137ce3fed439052bf8a1043ebc49fae8a98a75accff46
    role: context
  - path: pages/traits/genomics/card_nlr_gasdermin_system.html
    sha256: 4cd578c5913bd8694860061e8b1ec079cb9035c8b36263ca3f106c98863865e4
    role: context
  - path: pages/traits/genomics/card_nlr_like_system.html
    sha256: 4bb3e586ccc4bab48ea3d65b47aaaef0705128dbfb1c2dd1d26368519d800f5d
    role: context
  - path: pages/traits/genomics/card_nlr_phospho_system.html
    sha256: 6aaa292ede4ba6bb95d5133cfd8f49722698f6f4330cefb56bfec8bc4e1ebff3
    role: context
  - path: pages/traits/genomics/card_nlr_subtilase_system.html
    sha256: 8817deb518f6e874128aa16d89fcdbf582d68a0d4c52d3fe2bd2436b5d9b6071
    role: context
  - path: pages/traits/genomics/card_nlr_system.html
    sha256: 363b60546ea4a089dfa847a000fd59911ddcdc5775770e5485250d8804da30b7
    role: context
  - path: pages/traits/genomics/cbass_system.html
    sha256: c75c0e098efdda48b6dc1dc13e2483e7b4550f28d0b6752504f903ad761a71c6
    role: context
  - path: pages/traits/genomics/ceres_system.html
    sha256: 7df4bfef0dd27eff4a608c73f2dacb23076e41ad2253877f62cb4d1b58e5b194
    role: context
  - path: pages/traits/genomics/cernunnos_system.html
    sha256: 8257f39ee952863994c5b5ed7c04e9990eab26b230a94fae3fc78ccd10cd6dea
    role: context
  - path: pages/traits/genomics/charlie_gp32_system.html
    sha256: e9e7a033aeda98aadc9c76fdbc72f209eb46b8ebbeb977835f5b966707d03380
    role: context
  - path: pages/traits/genomics/clover_system.html
    sha256: a96cc39fa9dcb47ea4778f616685b05a0956729779c7f44c90a0a044d92c66ce
    role: context
  - path: pages/traits/genomics/cmdtac_system.html
    sha256: 5c149ec14976964c1ee676ec7d11968780586a818e96e3544a739ae671152b57
    role: context
  - path: pages/traits/genomics/coconut_system.html
    sha256: 02c528b72ab900856c24405962635aec155a491c94b72a07c1b177b4a874c1ab
    role: context
  - path: pages/traits/genomics/codon_usage_bias.html
    sha256: 0f522d4d6ff50bd11261d13e1d7b87d8c809589adc23d6d86f09f18040f895cc
    role: context
  - path: pages/traits/genomics/crispr_cas_system.html
    sha256: ea6cc45733be560fd13d1a08ce812e5be959991e59da9bcafa17e903f7fc90e7
    role: context
  - path: pages/traits/genomics/crouga_system.html
    sha256: 946d33c5bf4d77d1e87a7d57f0886674688ca54c68f5b1f16f1d567131f62736
    role: context
  - path: pages/traits/genomics/dag_system.html
    sha256: 1825bdc54d6ebef0f8a34f467df8238e0ab1ca94db36fcc00798e077af45233b
    role: context
  - path: pages/traits/genomics/damona_system.html
    sha256: 233cb3d0aac5c6a3a92028e64a2dffb92dd887366d180f7080f6071bd0c08129
    role: context
  - path: pages/traits/genomics/darna_system.html
    sha256: 797f28f4880f252960c14dd101611a15fbb8260b9075148c0b30a4e9d64e6953
    role: context
  - path: pages/traits/genomics/dartg_system.html
    sha256: b7f6c03dc44ff6a5b036a3c099c82ca5b3dc68d35cb673611bc041372e9e709d
    role: context
  - path: pages/traits/genomics/dazbog_system.html
    sha256: 6289988eb9efb95e19ebf9409f8d656796875dfee143dcf1080fe56be9864269
    role: context
  - path: pages/traits/genomics/dctpdeaminase_system.html
    sha256: b07f9c23289bed595c480aaa1819bc192088848ccf0555bfca3d47caf13de9e3
    role: context
  - path: pages/traits/genomics/ddmde_system.html
    sha256: 38b98131cca3681213ec810a360b784c2ffdc950f457b5d6259e08b3d4bab238
    role: context
  - path: pages/traits/genomics/detocs_system.html
    sha256: ce043e27696d3892f96e58f18e1e198ee3e9c15fcc86c1c83a59ac10fb347b94
    role: context
  - path: pages/traits/genomics/dgtpase_system.html
    sha256: b68a822c58e7529a2f24f7f477b653d4ca1fb5bacd29aacfcb1dfd91f545187c
    role: context
  - path: pages/traits/genomics/dionysus_system.html
    sha256: 039c2a0b04cac1f899d71ae95d24e2310cc2a302b3abc20a19505a3e55696220
    role: context
  - path: pages/traits/genomics/disarm1_system.html
    sha256: 181c511d4e4f0356226a583ce34a51e0bcd283344e97f5673b96df54b2cdd6dc
    role: context
  - path: pages/traits/genomics/disarm2_system.html
    sha256: 7c5403095a789cb85398c986883de39130053ef98b655ac9d9c0a973758a6331
    role: context
  - path: pages/traits/genomics/disarm_system.html
    sha256: 46394cb0e3a90f61d676bec2a3585e5efa64ba508c7fff3019fb08f9add17e69
    role: context
  - path: pages/traits/genomics/divona_system.html
    sha256: 512dca37b827e3300fe840975c18bf8844729cc92aaf26a6b1f73bb8cbe5ff04
    role: context
  - path: pages/traits/genomics/dnd_system.html
    sha256: 4d78de6fd49591ccd19da88ef81d92c834850f0616b1f83a40bbfbf7646d000c
    role: context
  - path: pages/traits/genomics/dndcdea_pbeabcd_system.html
    sha256: 4396fac0a6dc2257091420c9c7aa943da81999436c605065dd884ff7a29726cb
    role: context
  - path: pages/traits/genomics/dodola_system.html
    sha256: ec288760c5625fc31a59f32251dc530b7e7c26d19c88679f9e24a0b8887984a3
    role: context
  - path: pages/traits/genomics/dpd_system.html
    sha256: 700814baccad70d13cbdade7412e83a8dfe6615235cd1ab0d98b85d8f0200ab1
    role: context
  - path: pages/traits/genomics/drt1_system.html
    sha256: 54686e6c3ab44a256f545240a40ae75d859b50c98c7903acf176c10dfb0f13d4
    role: context
  - path: pages/traits/genomics/drt2_system.html
    sha256: 951d8df413a31d088c74d68a63a9c384eed5ceeda7c75bb3a92ca16bd821c120
    role: context
  - path: pages/traits/genomics/drt3_system.html
    sha256: adc6158e4900c54f32b8eea0b38d0b7dab209c919677c3c34a6523e9898035b2
    role: context
  - path: pages/traits/genomics/drt4_system.html
    sha256: 03b1d1daee760ea49e694d0b3e50d706db3e028e9346e06cda75785c7cca79fe
    role: context
  - path: pages/traits/genomics/drt5_system.html
    sha256: c8c90f145276795ecf4da2ea9d5f440afac0ca70e6f7679ff93cff6da931e8b2
    role: context
  - path: pages/traits/genomics/drt6_system.html
    sha256: ab40c8d13848dd23b475b797253bf52af0e93fb539ce092d7d460162f9b1ea08
    role: context
  - path: pages/traits/genomics/drt7_system.html
    sha256: 38a180a3ebf2b7a5c9461adfce5604bac32bcdad80e6d5fbf8b97ace1c5d8976
    role: context
  - path: pages/traits/genomics/drt8_system.html
    sha256: 1e0074c06a8f1773915695971852dc5e5f0a2443ce27e4615be69140aff64347
    role: context
  - path: pages/traits/genomics/drt9_system.html
    sha256: 8a5440976b575dcc68dfd489ab08acf5f076f86d0029cf3927325cd69ef52f74
    role: context
  - path: pages/traits/genomics/drt_system.html
    sha256: ae1244a89f753954b60abd8585dcfe72233b9f2dcb00f0eea43898dd44a078b7
    role: context
  - path: pages/traits/genomics/druantia_iii_system.html
    sha256: b8c65966d2d3d4dd62d12763ef799d643e99b791ac72487e6a05ebffbef4cbe4
    role: context
  - path: pages/traits/genomics/druantia_system.html
    sha256: 77c8f2639885e69cb743879e096ccf42ecc64b4a3d213bcc374b3b29c7404ec8
    role: context
  - path: pages/traits/genomics/druantia_type_i_system.html
    sha256: 7b4afdb79939d1b1c19267d8e5d0501de171c4efdbd3c9a91e83eea0ba2bdc31
    role: context
  - path: pages/traits/genomics/druantia_type_ii_system.html
    sha256: ba81e270518f3b1f02ea23fca4229a2ec209e9fc7dcd6b853f61878a47fc79c3
    role: context
  - path: pages/traits/genomics/druantia_type_iv_system.html
    sha256: 42cd729359163770d9a678845246fd821fed88f044a8990e31c8020997f029ce
    role: context
  - path: pages/traits/genomics/ds_10_system.html
    sha256: d05607acec303ffc859aace3a32d4e540f7ded117772ee9d40c9b3fc6eec05da
    role: context
  - path: pages/traits/genomics/ds_11_system.html
    sha256: 1dc532bc685ddf73e3e5fa160d98d632a188ed6ec617bee4287a3838d926ac54
    role: context
  - path: pages/traits/genomics/ds_12_system.html
    sha256: c3161f90925a111945b51bce99402224cf0f9676dac4024f3b212b03ef66559a
    role: context
  - path: pages/traits/genomics/ds_13_system.html
    sha256: 62898b616bf6f8f2405cec5c81afd95ca2454a267009317e1c5f4c61b1c11bcc
    role: context
  - path: pages/traits/genomics/ds_14_system.html
    sha256: 8b07a4fc8f49f48bb14fd3a21c8e6655c21f628740f936d46e92783c679ad5fc
    role: context
  - path: pages/traits/genomics/ds_15_system.html
    sha256: a43bd9f35461707f48d09b5fc567585d07fc8e94dcee5cba24ec1b99f00c5dde
    role: context
  - path: pages/traits/genomics/ds_16_system.html
    sha256: 813f8ab4cc577a0d19725db9a963a6bb0ee9f6ae194ecb77f0ff4e67a9122b9f
    role: context
  - path: pages/traits/genomics/ds_17_system.html
    sha256: bd35436ebcfdbf70810ed771704a63eb34564e8d61c14911eeb6154b4dfa273e
    role: context
  - path: pages/traits/genomics/ds_18_system.html
    sha256: c12c7ac5992d3523d0434d2b7fa9d40f8f94eb05e67b1a9d0ab81e848f5e0643
    role: context
  - path: pages/traits/genomics/ds_19_system.html
    sha256: 851d95cff65351b773e31f427b5825a6533c45f10098a4a744e80d5d7967e9be
    role: context
  - path: pages/traits/genomics/ds_1_system.html
    sha256: 9256c468986395bc47f8d4afeea5c037c7329db1feb339a1f7005112eba6d1eb
    role: context
  - path: pages/traits/genomics/ds_20_system.html
    sha256: 0111f42dd269b8c7ef7f6e64deefd69dc82c3d27a89c6d9cb5fe52692220f34d
    role: context
  - path: pages/traits/genomics/ds_21_system.html
    sha256: 917988701d69546a1f667c36535608b0e884ad198ef592fd097cc55e99621594
    role: context
  - path: pages/traits/genomics/ds_22_system.html
    sha256: 60e2fcd30bbed4f28382decb9d7e862b5d41d79ff064d26f800417194864fb86
    role: context
  - path: pages/traits/genomics/ds_23_system.html
    sha256: be159b77f37a325b60d4f02cee36e327be55a7edd63a71b96e27e1d27fa32e87
    role: context
  - path: pages/traits/genomics/ds_24_system.html
    sha256: a9bbe9ecc0ed836f34e12389c9fb776dc7431d9ede02fcff30358b56be28adb6
    role: context
  - path: pages/traits/genomics/ds_25_system.html
    sha256: 1b82d9116dc648e2dca6b244395ef509ff8599088d6ed5316912865a657b34bd
    role: context
  - path: pages/traits/genomics/ds_26_system.html
    sha256: 9b38fb9cf940e6b2f61efb22d19412c90f4506c921f784d153e48dc5ed598f16
    role: context
  - path: pages/traits/genomics/ds_27_system.html
    sha256: 072128a0d040483e8a041c4ba6b1246f0cd14fb0a829b9cdbd3a88fdc74ca98c
    role: context
  - path: pages/traits/genomics/ds_28_system.html
    sha256: 986b2ca8bd065d1880a384a55d5d6c6217042e3ecf699dfb83a217541bac7e98
    role: context
  - path: pages/traits/genomics/ds_29_system.html
    sha256: 3c7841927ed719b19d840881bc3fbea1bf6196a8698cf7db5cefc46757433046
    role: context
  - path: pages/traits/genomics/ds_2_system.html
    sha256: a349191b4522776802676c68dac68b272c9c0064cd0e84901687fb924044a398
    role: context
  - path: pages/traits/genomics/ds_30_system.html
    sha256: f383d1b67473a0f5fa2949be608213277a808e04ee9166a53a60ef19c322264b
    role: context
  - path: pages/traits/genomics/ds_31_system.html
    sha256: d6ec5f0a24714e1f2ee88960800ab080d81ae8adb344c7efa40c24013fc4da6d
    role: context
  - path: pages/traits/genomics/ds_32_system.html
    sha256: f3022fba5ed9b50705644c6e7a5216d60f7e8c8cec1a8e3e51929f271ec21a59
    role: context
  - path: pages/traits/genomics/ds_33_system.html
    sha256: eb34fae81d1be9d5391d5c18c97abee57fc2f30a2ea5910d440fd06901a65d7c
    role: context
  - path: pages/traits/genomics/ds_34_system.html
    sha256: 3405e2fb6bd332f1c885439ea7bcb54282dbfc42bf5247dc46e1930ecc24b2b5
    role: context
  - path: pages/traits/genomics/ds_35_system.html
    sha256: e5e426703e979ad9e4384202cef4abbc9b3661e52ea3ed8f01ada3d93a64251e
    role: context
  - path: pages/traits/genomics/ds_36_system.html
    sha256: 7e5517b529df41bf04cbf1db12dcd3c74df5446d5ad3e9598192448f9e545a70
    role: context
  - path: pages/traits/genomics/ds_37_system.html
    sha256: cee48cffa6883fd93e62949c6ff17c463953c647de21e4f69fb06bc5ee51fa0a
    role: context
  - path: pages/traits/genomics/ds_38_system.html
    sha256: 360abda4151081a812d2d7eb39bddedb15589ac70c7972b545405259f11979fb
    role: context
  - path: pages/traits/genomics/ds_39_system.html
    sha256: 62f5dc3f7c9d8d64da3e491a42d84ca07443d5305a5eb9182f737fb2d5f1767a
    role: context
  - path: pages/traits/genomics/ds_3_system.html
    sha256: 332c5e3e35693c7b680f310f48be795c5d14d3e53540b1e836eb8eb572805c7a
    role: context
  - path: pages/traits/genomics/ds_40_system.html
    sha256: 29c3d384470187cb51ab30ed9391b4a4e342fa6c84c5ea1f92b60d188df58941
    role: context
  - path: pages/traits/genomics/ds_41_system.html
    sha256: 7d3daa3d6b712e6881eff92adf1be4acbb05562e0f27c1b0a48f7df6f17f5728
    role: context
  - path: pages/traits/genomics/ds_42_system.html
    sha256: 46db8f1a6ad07dc2d9662a08dd1d7bcf980724a47986668b4db458a388a8014d
    role: context
  - path: pages/traits/genomics/ds_43_system.html
    sha256: 7ede383a403b1b317b7b3fea9f9d1bd46e3340966f3383b759100260d130ff90
    role: context
  - path: pages/traits/genomics/ds_44_system.html
    sha256: e1f9f12f787c30dd9793f741f7bd5edc92c1483ddd6e2e3e3e0054557fd1e148
    role: context
  - path: pages/traits/genomics/ds_45_system.html
    sha256: 520ffc08bac41d9f5bd3e0da01197fe384e5e223126f44df781155cdb65c31a7
    role: context
  - path: pages/traits/genomics/ds_46_system.html
    sha256: 82c62e7266d9e4faa567e6851d8df3ce3abf2c4e9be8029dca383be14004cfee
    role: context
  - path: pages/traits/genomics/ds_4_system.html
    sha256: 06cd86d7032b3d4e01fb7fb420d5a535c020d25945006800a5d7ad4fd16f740b
    role: context
  - path: pages/traits/genomics/ds_5_system.html
    sha256: e6079c60ba5d48d271dc59de615f1cba8a00f82df2fa8451c9b3c1485ba4db7b
    role: context
  - path: pages/traits/genomics/ds_6_system.html
    sha256: 3500f2f1bd1eaf64e4ad1df062292b16b8f8bdf5dacbaaa7137f2cea9411e8b2
    role: context
  - path: pages/traits/genomics/ds_7_system.html
    sha256: dc510bb06f497305427e9a305a3a752e7e5ad5e79711f177bc38af1abdebe5d9
    role: context
  - path: pages/traits/genomics/ds_8_system.html
    sha256: 8576324cb89ac617491f2c5ce900ccfae228276b20023565fd3394003076b451
    role: context
  - path: pages/traits/genomics/ds_9_system.html
    sha256: b78a24f0df4851f45e7751fda41502cf78bbfba939d51ae06586d789fa3491bc
    role: context
  - path: pages/traits/genomics/dsr_system.html
    sha256: 941c3ac3b648b21740baf10e99576b228ac5d0e6a968ac9e2c168ecdd961ac21
    role: context
  - path: pages/traits/genomics/duf262_schlafen_system.html
    sha256: 4b17228c501ce1d17aa4942764db2fffdd405076389adde3c1dedd83bb6e168b
    role: context
  - path: pages/traits/genomics/ecokmcra_system.html
    sha256: ddb1c55eb2e6b93a64a067ed8de76766810586c194c369806697a579cdac140c
    role: context
  - path: pages/traits/genomics/eleos_system.html
    sha256: 83d94543a526a6198557b8bfeb78613139c1db46a191806930bbb8d46b283fbb
    role: context
  - path: pages/traits/genomics/endpacf1_system.html
    sha256: 3153440b77db6c735dfa184b1fc1fb4c6cf77b3472ca8227b7fa48578b16a27c
    role: context
  - path: pages/traits/genomics/epona_system.html
    sha256: fafe28c0d3a96b59b56d05681f0b48e7c59e7612670926ed71e35d3b9b1c171a
    role: context
  - path: pages/traits/genomics/erebus_system.html
    sha256: 7818a4d0d1d39f75d20e1c6c7c5e5e46f8e2a487070c08fe6128f90b11d41f42
    role: context
  - path: pages/traits/genomics/esos_system.html
    sha256: db7fe284fdca82425d6ca301fe3ec3fc86b6712337dafb46b11429f5a6b795c4
    role: context
  - path: pages/traits/genomics/fliodhais_system.html
    sha256: f24b3b8cca92c9ef7f0f88d47f24585d00b828eed75ca814fd1fe025579ed57a
    role: context
  - path: pages/traits/genomics/fs_giy_yig_system.html
    sha256: b5aff8283039734c810edf2158b55063f615d0db2e9d04c57ef47b1f390fc2d6
    role: context
  - path: pages/traits/genomics/fs_hepn_tm_system.html
    sha256: c856a241a66b575b08274c492e5a7d008969b51e496410ccefe8bfd3cc5e966f
    role: context
  - path: pages/traits/genomics/fs_hp_sdh_sah_system.html
    sha256: 758a30f174fad2432aadbfcf2986dfe1a032450c05d635151d63427e744b039d
    role: context
  - path: pages/traits/genomics/fs_hp_system.html
    sha256: 90876a87bb7d9871eb1f834142487a21260c6b2e6f0546b2aa79b9fc479bdf9e
    role: context
  - path: pages/traits/genomics/fs_hsdr_like_system.html
    sha256: bbf7f678a11ee1b6bbe042c355ce3c1f541e7d83e5c51536681c9ddc9848e048
    role: context
  - path: pages/traits/genomics/fs_sma_system.html
    sha256: 64cc43e8ec96597582e1d55988fb3ee78e70259e9ede00af6dc41b3171ea32e8
    role: context
  - path: pages/traits/genomics/gabija_system.html
    sha256: 5b0c002b0f87ad126d83f9034cea7b77797ad79f75e72909919a36b0393840c9
    role: context
  - path: pages/traits/genomics/gao_ape_system.html
    sha256: 6da57e6213bb9b578548ea716fabb0f9988a34971bf44d6c6bf2e5007c3579e6
    role: context
  - path: pages/traits/genomics/gao_her_duf_system.html
    sha256: 2c6062451a4824036705cf15d2ff02f8ce9dfa23ea73c0ca2ffcb7a4e297c6cc
    role: context
  - path: pages/traits/genomics/gao_her_sir_system.html
    sha256: e66dbdc22bf1e2140105c843c96c683a09d29d8228fd60dc97c329c2db3e6c09
    role: context
  - path: pages/traits/genomics/gao_her_system.html
    sha256: dfe538a60a50e81fe9e947724bc8f97bfe4669f38c3e54ff14adf9b82f7cb6ab
    role: context
  - path: pages/traits/genomics/gao_hhe_system.html
    sha256: 2e1b9e1f4d332e80932c4152851dde19da83198c1b84b2fba295f979f550ae99
    role: context
  - path: pages/traits/genomics/gao_iet_system.html
    sha256: 48e5adbb9550f0e4bdf4eddc74290be61933cac22d3347570b4a83c7dede8830
    role: context
  - path: pages/traits/genomics/gao_mza_system.html
    sha256: 2d9fb40cb3fefd1cc96701ba04be44cc29a4923610f9810e19db037906d01cec
    role: context
  - path: pages/traits/genomics/gao_ppl_system.html
    sha256: 52c1363e3eff24c6e8848d2e425fb065012cf53aa6514f88de10dcda3b4f4ea9
    role: context
  - path: pages/traits/genomics/gao_qat_system.html
    sha256: 1341b5130d4643fedbb2a026ddefa4ac8f82a98c0c9b7fd24db21042c23b616c
    role: context
  - path: pages/traits/genomics/gao_rl_system.html
    sha256: e6818b670fa05f0fd34373225c85e7ea99dfcdbc6150e4ff621a1939677da4d5
    role: context
  - path: pages/traits/genomics/gao_tery_system.html
    sha256: 46c7417400b584a52aaa2dbb635da9a31418b073260dbc65ebe68c119c2bf45b
    role: context
  - path: pages/traits/genomics/gao_tmn_system.html
    sha256: e0780d199cb0d1b2c18064549ce348aa0c57d7efea0132718d0ee50cb1c9763b
    role: context
  - path: pages/traits/genomics/gao_upx_system.html
    sha256: 30f6f17746cc00e09797b7bfd98153ff30fc0a6b62d6e5716f103a5518be08fa
    role: context
  - path: pages/traits/genomics/gaps1_system.html
    sha256: 9942821731d145640ef32bf5fb629c936642cbca08639dfd4009b3a51c51766a
    role: context
  - path: pages/traits/genomics/gaps2_system.html
    sha256: 9936724e8130e91ab2d523944530871593f0c8023260808563ef6b9001d67430
    role: context
  - path: pages/traits/genomics/gaps4_system.html
    sha256: 4fec2312ca14723ae8835ec10ecb50e9281de2daac0d4d27b35bce9234bd63a7
    role: context
  - path: pages/traits/genomics/gaps6_system.html
    sha256: a01b17664b652228f39b42f42525d55d40d4dfda9102e5bbf90a6b1cfd319267
    role: context
  - path: pages/traits/genomics/gasdermin_system.html
    sha256: d9d4fbc11abfe72412f30d9f64a402694991268421ba3d354c8a2152b5fe1a9a
    role: context
  - path: pages/traits/genomics/gc_content.html
    sha256: ae9ee47e42653b4d78fc91846cbf4f9976eb17743fa536c1fa49d58397919cc6
    role: context
  - path: pages/traits/genomics/gc_high.html
    sha256: 2d28b12dea72961270272c4043d600c970f59c1320e85adbb585c84e09841c22
    role: context
  - path: pages/traits/genomics/gc_low.html
    sha256: d80cfe7878a78ad2d58b5c980e4ad3e48934bf8a1230877d8040aedb91a7ddb7
    role: context
  - path: pages/traits/genomics/gc_mid1.html
    sha256: 309899a1c4546e4105667333675126297bc09b48c1a0dcb771d8f2c29f3ec345
    role: context
  - path: pages/traits/genomics/gc_mid2.html
    sha256: 659c1f65d5b011727f63435d23134b9f23f3c4e9dbc08e64f6ff216e2b3e1afd
    role: context
  - path: pages/traits/genomics/gc_skew.html
    sha256: 4574bcfa6ba5da94251d1e5005a67a535215fc6220ba2729f00f669f5e4af16c
    role: context
  - path: pages/traits/genomics/geb_system.html
    sha256: 7254b14d8115dad0c600062fe56235c481926ffcd4e330fba9702e929a7b5700
    role: context
  - path: pages/traits/genomics/genome_size.html
    sha256: 9401d78f472336b3b8858cc8416afb2426f1e07d3abdb87764b3e50da1931ce4
    role: context
  - path: pages/traits/genomics/genome_streamlining.html
    sha256: 1dc07d689636e0e83d3606e3a583d163926224b3dc4b6133fafc93e8d948ca13
    role: context
  - path: pages/traits/genomics/genomic_island.html
    sha256: 6c39254fb2878ace065e6f25f32fa686664786ae18ea11b197ac60634478429f
    role: context
  - path: pages/traits/genomics/gmrsd_system.html
    sha256: b3aa26fa1eb23133e760d48582b39f5c8221e233ada56ebca4417db1fae69058
    role: context
  - path: pages/traits/genomics/hachiman_system.html
    sha256: 657d5a2ae4af7214332758cec3c62c2ce878917a3011e8d7c5b7d32b0e229db0
    role: context
  - path: pages/traits/genomics/hachiman_type_i_system.html
    sha256: f16c14a90c6195108fe8909a0770643291a967f71dbeac20a818e46e10e4b91f
    role: context
  - path: pages/traits/genomics/hachiman_type_ii_system.html
    sha256: 82790bf2eff021aa6f6c8559a2238827b05ba9c6c2b9dd7f807f0e4d81824c2a
    role: context
  - path: pages/traits/genomics/hailong_system.html
    sha256: ef4a8c161fe3982300c2db44d86df32cb76ccb48bbd32c686e5991ca2a98142c
    role: context
  - path: pages/traits/genomics/hec_02_system.html
    sha256: c848f2d8d061860efbd70661f0807fe78a57d511c574809590b829afcd7d898d
    role: context
  - path: pages/traits/genomics/hec_03_system.html
    sha256: b4ebd6035e2a2bc2bfd54f530c3256989b86d1f99827c0a1cbc085f375f025f0
    role: context
  - path: pages/traits/genomics/hec_04_system.html
    sha256: 4e5e600d3915ef16b2f440fb590a2347a6b27a5fb2452f97522b494550f07be5
    role: context
  - path: pages/traits/genomics/hec_05_system.html
    sha256: bd20b62d54dd77f5a8a16831743df70f8707edfb60ee886973dac9a64469628d
    role: context
  - path: pages/traits/genomics/hec_06_system.html
    sha256: b8677f7c5770d3fde1404b76600ca9d5d3d1de064d6af13f8e2d7084493c38a8
    role: context
  - path: pages/traits/genomics/hec_07_system.html
    sha256: fbd60d53ce50436e7aa60b9632ae294faa464b474b2ab121af4646833c3a2fdd
    role: context
  - path: pages/traits/genomics/hec_08_system.html
    sha256: 45ed5a10e3f546470ef95e082668cf338b10fe98d4c657adecb4ff5bd6c1559f
    role: context
  - path: pages/traits/genomics/hesat_system.html
    sha256: 67863ec2b181bdad2f66fad9a0e99e3a9f752c569b9ab2da8da8668026de2738
    role: context
  - path: pages/traits/genomics/heterokaryosis.html
    sha256: 27406fff02ca9737f1ad5b95f87a437338d260fa049bc521d56d533505df8b34
    role: context
  - path: pages/traits/genomics/hma_system.html
    sha256: dcf3dd3d8ffcaa58c5ddbff441c35f262971c226cb7220ac867f31ffeecf70c2
    role: context
  - path: pages/traits/genomics/hna_system.html
    sha256: 9b88708e262c91de999a47062d6fb0a0e2ee10b2ba0d7ba73636ae484628575f
    role: context
  - path: pages/traits/genomics/hypnos_system.html
    sha256: f939b2d3dd96f38a4c63234c2a3ad69fd00506c8802546867c000d81b2bb2e4f
    role: context
  - path: pages/traits/genomics/ig_like_schlafen_system.html
    sha256: 605afad948cdfb89baba6ef66c4c3a016f67d87b6bd303f59050fc545c30bb2c
    role: context
  - path: pages/traits/genomics/integrative_conjugative_element.html
    sha256: 5a12607d4aa962c47a917c2d87181969c10857a1037cb160328ec26977caa34c
    role: context
  - path: pages/traits/genomics/jukab_system.html
    sha256: a5379dee0a8163097485a6e5b3adca3b0e17c50545536729c07783a91fba42bb
    role: context
  - path: pages/traits/genomics/kamadhenu_system.html
    sha256: 0ad16f4864d2ac55d60c963995355694783c80005f1131656727f823e380c923
    role: context
  - path: pages/traits/genomics/kiwa_system.html
    sha256: a92225c2b131f129e8b79ff0e7be45133ddb85350a6e5a429db8f2a10531071c
    role: context
  - path: pages/traits/genomics/kongming_system.html
    sha256: 94ad23ca038373c44f4d371fab37549e69eccae8a625ae7a5767a7e8e070a0cd
    role: context
  - path: pages/traits/genomics/lamassu_amidase_system.html
    sha256: e77f492466e8db271f2783955feda34b7b406c560bdd649a4d41b9ef4ed1359c
    role: context
  - path: pages/traits/genomics/lamassu_cap4_nuclease_system.html
    sha256: 2fb324db43bc1849698255086a3491a20704d974ca4f703631e05a246b706b5a
    role: context
  - path: pages/traits/genomics/lamassu_fmo_system.html
    sha256: acdbdaca7a2db92532efe79b42e467790735c5d03fa998f11fc944414874a290
    role: context
  - path: pages/traits/genomics/lamassu_hnh_system.html
    sha256: ad52d4dd92dc88c14bd85d69a5e764631b8cec3712aa29fc10ddd2eac3774bdd
    role: context
  - path: pages/traits/genomics/lamassu_hydrolase_protease_system.html
    sha256: 3c88092c780e01867f545db08d93706cd928735c51de721901634271176633ae
    role: context
  - path: pages/traits/genomics/lamassu_hydrolase_system.html
    sha256: 1aa74e96435a6b7c4ad40d67bcc9940c71ca2fd284831a75646a529e9bbca6b0
    role: context
  - path: pages/traits/genomics/lamassu_lipase_system.html
    sha256: 7851282a91e93818f979ef50c121de1875586ed0c7ac02c4d2f33ca56f74fdd7
    role: context
  - path: pages/traits/genomics/lamassu_mrr_system.html
    sha256: 8d43cfb732b95b140335767d0fad15b35623b5f35c6851f62fa61ed7a9b7c332
    role: context
  - path: pages/traits/genomics/lamassu_pddexk_system.html
    sha256: 27da79aa99c33c05592a3f7049fc47008ef7693280d413a88abe28f957615cc5
    role: context
  - path: pages/traits/genomics/lamassu_protease_system.html
    sha256: 92aa7e597dddaaffb2628052203eef0239dfaeabfcf5edbcaf7e0a5debb3f3a8
    role: context
  - path: pages/traits/genomics/lamassu_sir2_system.html
    sha256: 65d42c3d9fffe7fef0dbcfbe52e336d09c08f112b7f9654fae5183523040d3c2
    role: context
  - path: pages/traits/genomics/lamassu_smek_system.html
    sha256: c0c6f598b68da5e018d8f901bcd7573665e5bceff68852e671f6add8987ba2ae
    role: context
  - path: pages/traits/genomics/lamassu_system.html
    sha256: 9fc8016f623cb79c8ab8ffd018ff2be1af2d869c0bbb086f4f9acd202db2918c
    role: context
  - path: pages/traits/genomics/lamassu_type_i_system.html
    sha256: 1f70cd71a7e33555fdeef86dda443ce71f8e9792fd99f152527c1a41e80e78d1
    role: context
  - path: pages/traits/genomics/lamassu_type_ii_system.html
    sha256: 281d42cf7b444691803b114b7fb09f6af5167fa9af4ed380c34c9439b941a151
    role: context
  - path: pages/traits/genomics/lanthivirin_system.html
    sha256: 872910fdbce2373348207d1205784c726076162f9cbcca93b1d65a692615e66f
    role: context
  - path: pages/traits/genomics/lit_system.html
    sha256: 44241051e3f6a921dabebb896da0aa3c00dfec2db70ee1db0b92d2ef15a536e1
    role: context
  - path: pages/traits/genomics/long_lamassu_system.html
    sha256: f5ae2b95302b8c4bff67fdd51c8b7eedef89243fdb39319685d3255a084985b1
    role: context
  - path: pages/traits/genomics/lugos_system.html
    sha256: 5f4f448b15b749242f7ddecb4162204182b80efa479aad13964f9eedb271a968
    role: context
  - path: pages/traits/genomics/mads_system.html
    sha256: 06df2959175d20aeb31f6ba8c839457143df6a5349218768f59950eb258ef93b
    role: context
  - path: pages/traits/genomics/mazef_system.html
    sha256: 28abae5f6c7e41fa3ec6bbbc5f60027b890db66e3258c72c650ece2687ad30e5
    role: context
  - path: pages/traits/genomics/mcrbc_system.html
    sha256: cb993515b8f1da4b6c0375f776678d814113bc7fa05a6315325ce958cda23982
    role: context
  - path: pages/traits/genomics/menshen_system.html
    sha256: 581173b6a8746168e48d8a125ca93ff5ed3ea8e924577edf0c41b9c9123c0d20
    role: context
  - path: pages/traits/genomics/metis_system.html
    sha256: b013942bab18c58194814902b090e0b9cc008e8ea0d7434b0976b84c281f1dfb
    role: context
  - path: pages/traits/genomics/mksbefg_system.html
    sha256: d70e12e955dfdd6ec3bd285f7a4f8aa3cb85b08efaadf33b6ed563a6c7f8a487
    role: context
  - path: pages/traits/genomics/mmb_gp29_gp30_system.html
    sha256: 8b3524572016e7798664ce987d5dae5e063b31b1abc78a4c417bc0963ff72633
    role: context
  - path: pages/traits/genomics/mobile_genetic_element.html
    sha256: 516475c4077a7205f0da920bc811b3fe0d6efd6d05066f7799ed5c8d693b3e75
    role: context
  - path: pages/traits/genomics/mok_hok_sok_system.html
    sha256: a2b07f15a4a43eb50911d1a0d50aa0cafeff28472bd969b2dc85b197f6b4f943
    role: context
  - path: pages/traits/genomics/mokosh_system.html
    sha256: f9d7a773636fd3b007dfd0f1a6f69e7330c01f9cef6a21d239ff2f1572587932
    role: context
  - path: pages/traits/genomics/mqsrac_system.html
    sha256: f9442b8aae5d5511b8c15250d6dc15d264f60d0cc10d908cccdbc8762c6468ff
    role: context
  - path: pages/traits/genomics/mspji_system.html
    sha256: 3eaf94a10dd3a66a8cde2c2f9e981eef75867b1bbc230439d5788fd701dcabad
    role: context
  - path: pages/traits/genomics/nantosuelta_system.html
    sha256: 5f687dcc1a8d73d72beb03bfe6e679acf42a750912c15b16138a3ffca02e49c5
    role: context
  - path: pages/traits/genomics/nemetona_system.html
    sha256: c6c29eab3ca301cd9842f7ba74153c01e6d46e17321d2eba50d59f6eae4d4dae
    role: context
  - path: pages/traits/genomics/nhi_system.html
    sha256: 5de7135600021215f1833faeb3526097af1710f5823df4bf5bfa9e7547d0200f
    role: context
  - path: pages/traits/genomics/nixi_system.html
    sha256: 6374b360fbda2d6c7379b118f9b7f52ea9438723f1fddd5938ab2f979234985e
    role: context
  - path: pages/traits/genomics/nlr_like_bnacht_system.html
    sha256: d7db1514fa207f04112c21aacede74b858b1fbf68aba8199ffc058c6b804d5ae
    role: context
  - path: pages/traits/genomics/ogmios_system.html
    sha256: 1b0383dfb1584fbb606f9e927712d467925726a4a146cd4e0b452e0006813613
    role: context
  - path: pages/traits/genomics/old_exonuclease_system.html
    sha256: 3f97a382ceda16068f6bebf608ad3fdd888e2d8793c130b346d8d0923303ef8b
    role: context
  - path: pages/traits/genomics/olokun_system.html
    sha256: 081f3ac565cc33ba28e1672deb44161b22de2bd32ebfc45d94f76d4decc64dd8
    role: context
  - path: pages/traits/genomics/ophion_system.html
    sha256: 4ab6f4ef80712390a17a690a6d9a5974125fb25594a80678b9d16338e49d30ba
    role: context
  - path: pages/traits/genomics/oshun_system.html
    sha256: c891cbd9e649711e92a5d5aad64bf999670eef2972c456ba12159a5aeed55ec3
    role: context
  - path: pages/traits/genomics/pago_system.html
    sha256: aa7ae4b78ba2529699f380daee75a196bd298feeac811ea8834179d90ffc46e3
    role: context
  - path: pages/traits/genomics/panchino_gp28_system.html
    sha256: a164f5fb3b60dabfe68c50e1ac824eec0ca61dbed2eb4e8ff39fa3faeabf3499
    role: context
  - path: pages/traits/genomics/pangenome_openness.html
    sha256: 9ed574487c444d1e8ae4046700525f32a75fb85fbfeb3c034a6e44888935ae8b
    role: context
  - path: pages/traits/genomics/panoptes_system.html
    sha256: 3fcb9f53bc7c60d50a2215ee349d72ac4b3c4a437d99dc06c5bdd80509781a93
    role: context
  - path: pages/traits/genomics/paris_system.html
    sha256: 76773cd15263a161f3ebb112b48100c5adac5d2e5014d4d5a0780a968dfcb515
    role: context
  - path: pages/traits/genomics/pd_lambda_1_system.html
    sha256: 747eb13fed1dbc94bdc41e04d062e5f0400d787f22c7fa4b83b1647dec565915
    role: context
  - path: pages/traits/genomics/pd_lambda_2_system.html
    sha256: e1f270b8a03f098710081ce72ad57a132e9dd7791f012cdb85d30a7dcbd59f56
    role: context
  - path: pages/traits/genomics/pd_lambda_3_system.html
    sha256: f7af90659afc4b757f1b2a8fda7369878975d137c3ea822e6d7589ab6bc95893
    role: context
  - path: pages/traits/genomics/pd_lambda_4_system.html
    sha256: 5f67d17e007b2229e59fb0f63eb69852e41b78475189e47c1cbf3b2fecbc14b8
    role: context
  - path: pages/traits/genomics/pd_lambda_5_system.html
    sha256: c975abe79eefad0129bb16e5b1e46adc260eb4817425e94688989d92a4ab9516
    role: context
  - path: pages/traits/genomics/pd_lambda_6_system.html
    sha256: abeb1753fa907b391724543e2b64eee726611d8a5022be6836f96993502201c2
    role: context
  - path: pages/traits/genomics/pd_t2_1_system.html
    sha256: aa625925ab242b641a44253e593602434a285a3a22ba58d79cd392e5ec13e31a
    role: context
  - path: pages/traits/genomics/pd_t4_10_system.html
    sha256: 9cb05f44a6502a56c2a90cc058f2ed63236a1b3cddf8f61ebf4d75ba570292c0
    role: context
  - path: pages/traits/genomics/pd_t4_1_system.html
    sha256: 5302bdeeb426e7ffcbc4dd0907bbc9a0777a865c0b2b38705b9a8a70e3f21044
    role: context
  - path: pages/traits/genomics/pd_t4_2_system.html
    sha256: 291dadf8b60f784e51e232436bb44a7bf97fbd076ad975dbc2d32a43937969bd
    role: context
  - path: pages/traits/genomics/pd_t4_3_system.html
    sha256: 8850a6a113a97c1076c4fbec4d770369ff6fe54663a61502488fe2117171476a
    role: context
  - path: pages/traits/genomics/pd_t4_4_system.html
    sha256: 8eb3f2fd25769dfef27bfc23220e8312c7b4b048721f663b83a2b2e9c8104309
    role: context
  - path: pages/traits/genomics/pd_t4_5_system.html
    sha256: c5b3b65e5b047744364176bc70db7bbf4da23b9d3cace4abae457f81e3c2e3ae
    role: context
  - path: pages/traits/genomics/pd_t4_6_system.html
    sha256: 3dd2d6eecd98637839328f95b7d7b02c9166f50c6aba547d3ab4fd005b08e68e
    role: context
  - path: pages/traits/genomics/pd_t4_7_system.html
    sha256: aa6da6ab4d637e05654eacb43fb049e991e69e3d52952e839ef8b371c486f2d8
    role: context
  - path: pages/traits/genomics/pd_t4_8_system.html
    sha256: aa17bd7de814a2cd4634519d24b79c93cc2896047eb03a06a385e69d986905eb
    role: context
  - path: pages/traits/genomics/pd_t7_1_system.html
    sha256: 8a2df59a8bc89d1f6d90d48caa42802201a22733da9643c86f3e638c7f8091b8
    role: context
  - path: pages/traits/genomics/pd_t7_2_system.html
    sha256: 3a44c0e9fd4f1dab8f1bbaa283c18db029ca401333b1b71ce9b2f32dc9083269
    role: context
  - path: pages/traits/genomics/pd_t7_3_system.html
    sha256: c2975c05d7bff8803517ea988c82118be92be2ff63eda86e2b4d2328ea1eb93b
    role: context
  - path: pages/traits/genomics/pd_t7_4_system.html
    sha256: 1275092b2fa297959bae0de68c8148a585c5afed84a7bb1674a156e227bea7ba
    role: context
  - path: pages/traits/genomics/pd_t7_5_system.html
    sha256: 6321ccb94f5068b97c52c3aa9989052f35f9e2aa5f80da937993e97ee5034b62
    role: context
  - path: pages/traits/genomics/pfiat_system.html
    sha256: 3a4fb12b39252fb8a1a92288051796d766969be23fb73641f0121a1cb86aadca
    role: context
  - path: pages/traits/genomics/phage_defense_system.html
    sha256: 7ad3654e94a52f76b3667817873c6dc8094e6f0b4ed58253ff093307fde3928e
    role: context
  - path: pages/traits/genomics/phosphorothioate_defense_system.html
    sha256: 42c1db3fbe0245adfe42ffb9b5bd85d97669c400a4217824d9f69023148b225e
    role: context
  - path: pages/traits/genomics/phrann_gp29_gp30_system.html
    sha256: 0efd137f406e50d20716794dbb2009b473e17a6097125a35299a14b777e158e5
    role: context
  - path: pages/traits/genomics/pif_system.html
    sha256: e1b17e9f2a437292380a5c0a18b3950ff4dd42b0be96411339c5a2cbb5177514
    role: context
  - path: pages/traits/genomics/plasmid_carriage.html
    sha256: ecfa1058bda030f48cfb6fa212342f50b8d47a0ba795549cb3d11ec9e931a5dc
    role: context
  - path: pages/traits/genomics/ploidy.html
    sha256: 28b13ab202dfa0fd6b71ed6fe18b32ca6000493ff8e9066773ca3ece466704d6
    role: context
  - path: pages/traits/genomics/prithvi_system.html
    sha256: 7270eb9f871c212b52bfb0be5bffc8ff315f2e82d0ef38db30d0776b24e5b512
    role: context
  - path: pages/traits/genomics/prometheus_system.html
    sha256: 0bcb83fae7ad10317737224376e7704c73be554b525a1244cb29ad4ded06e836
    role: context
  - path: pages/traits/genomics/prophage.html
    sha256: b622db01786f045ee40e72824e57aa206fdcd0d9bb8521002e6b4bdcd594d855
    role: context
  - path: pages/traits/genomics/prrc_system.html
    sha256: 0e491463a3c3e4bb369b4199fd94a9a491170ae6ac6bde60fcd03617145f34a2
    role: context
  - path: pages/traits/genomics/psyrta_system.html
    sha256: 08a4266e8fe84367845524dd0f171ab45659dfecd64e0c0be61fb806ab354437
    role: context
  - path: pages/traits/genomics/pvurts1i_system.html
    sha256: e9610de9f825a5c3e2e804d8a20d92d08b1227c6a1ce1e68ad90b4780fab45c1
    role: context
  - path: pages/traits/genomics/pycsar_system.html
    sha256: ac3fff8db906e375b65b132ce2079a0e4060ec856148545a1f466078318dd98c
    role: context
  - path: pages/traits/genomics/radar_system.html
    sha256: 407622ed8f9c3a67866f0f232ab688d5f0a7825af292e7d21bef9eb1328eef38
    role: context
  - path: pages/traits/genomics/razr_system.html
    sha256: 94e4ab7824eaf3721a40106817312c9564532b2130bdd076cc441d3bd77c5fc7
    role: context
  - path: pages/traits/genomics/resolvase_duf5677_system.html
    sha256: 4e463bbfe7d0bc310d49b5f5a8d87411cd7a0d400c041089bb3a51717ff501b9
    role: context
  - path: pages/traits/genomics/resolvase_kap_ntpase_system.html
    sha256: f023ab18d667441c5c656e4057f50731e8d254330c0bb486df351c6d475a36c9
    role: context
  - path: pages/traits/genomics/resolvase_schlafen_system.html
    sha256: c98228fcd2b9be396217559949237aa5db641305cef23ee35b2a53c96dc8a237
    role: context
  - path: pages/traits/genomics/restriction_modification_system.html
    sha256: bec5f82acfbf2a4f0e598a515546bb3b95622ea7192be3677186716076ccbe90
    role: context
  - path: pages/traits/genomics/retron_system.html
    sha256: a296d83028d552fb0683ff3c6c69c2c65b6c7c0ea118cd4e1d3f93a29ab068b7
    role: context
  - path: pages/traits/genomics/reve_system.html
    sha256: 877810e576f829bedc0808fd48310fcb833243b5225a0bcb8ceb670bc432c365
    role: context
  - path: pages/traits/genomics/rexab_system.html
    sha256: f2c184e4b4b272c9adeb3fd93e1bf607b2a5ed05a870ad3c891d481cc212121c
    role: context
  - path: pages/traits/genomics/rhea_system.html
    sha256: bb042596ac94766e22cb8502ab7381d2ad30773ff923df8f869075167df448df
    role: context
  - path: pages/traits/genomics/rloc_system.html
    sha256: 00a259be21e9f1b0e6310438e90e5826eabf45776f839473dd511c8971cada73
    role: context
  - path: pages/traits/genomics/rnlab_system.html
    sha256: 295fbbcd885afc1982602e7ec5a78467c31610cb23609b3205244e2e924ad7f0
    role: context
  - path: pages/traits/genomics/rosmerta_system.html
    sha256: 5dc7267e342eb34014a44e2e68218b872caaaa5bed6f15e69502ca66e56e3942
    role: context
  - path: pages/traits/genomics/rrna_operon_copy_number.html
    sha256: 3f3f4b8488c90680d98d28ba78341c3631ad2d778c05f4ddaf4370521613162d
    role: context
  - path: pages/traits/genomics/rst_2tm_1tm_tir_system.html
    sha256: df51e29929e09329200fc1da090688d5f4ed472c6453b4214e6abda467f888ae
    role: context
  - path: pages/traits/genomics/rst_3hp_system.html
    sha256: aab2e18713d1ab970fa6aa0c075e457541d891e4bc11ad4acb6f7aa9e2be01d5
    role: context
  - path: pages/traits/genomics/rst_duf4238_system.html
    sha256: 9140effdc9de3567042fb59c64a8f47e806bef59e63adc9b0bc969f2b4f64ba5
    role: context
  - path: pages/traits/genomics/rst_gop_beta_cll_system.html
    sha256: b56c98b2bae65104b437961e293783be662fda61a24c10a835086462f7a5f6d8
    role: context
  - path: pages/traits/genomics/rst_helicaseduf2290_system.html
    sha256: c000c577a9619831172a637f729864d81e3b4032a3a2f17c09ee54edd7a7458e
    role: context
  - path: pages/traits/genomics/rst_hydrolase_3tm_system.html
    sha256: 009836ef3e3ea6724a102f9eb8e7b170aaced5825a3f6139da51569de84e4834
    role: context
  - path: pages/traits/genomics/rst_rt_nitrilase_tm_system.html
    sha256: b94222612a4f1ea24a9b05d4cffd51c32e1ba38871b7affe3b626243a02840ca
    role: context
  - path: pages/traits/genomics/rst_tir_nlr_system.html
    sha256: a2e1097eb259531994ca5da9d5e7cedb93bc350e48a352307404281777262250
    role: context
  - path: pages/traits/genomics/rugutis_system.html
    sha256: be085b823032f541b2a32a8a103d402b08af86df2a12caa11787101232b51b25
    role: context
  - path: pages/traits/genomics/sanata_system.html
    sha256: 189e418a6805b983f5f6d6ea174bd4508660aeff462c2bffa6acb8f36bcfc115
    role: context
  - path: pages/traits/genomics/scomcra_system.html
    sha256: 0c3f411c7bfefce34d5a46d95966ae72c21afe4fbda7095c1abd491570ac3fb9
    role: context
  - path: pages/traits/genomics/sdic1_system.html
    sha256: 0ae18aabc7bbfa28ccb5d82ced0152e945ac883b2d7d3a7d7bca11bb9cb84e7e
    role: context
  - path: pages/traits/genomics/sdic3_system.html
    sha256: e7986d86f5f3cffb8a63b676760e4448748268675a9f1ce009e9d46ebe3cab50
    role: context
  - path: pages/traits/genomics/sdic4_system.html
    sha256: 59f6e2749cbb0a8168af3aba6888f0fc9b70307959c38b896df0005b42da4d1e
    role: context
  - path: pages/traits/genomics/sefir_system.html
    sha256: 5ae03ba072784603401fe957b61e117cc026f45d069bf9382485c97226018763
    role: context
  - path: pages/traits/genomics/septu_system.html
    sha256: 298d4047bf8291a8cebe6ab8cbfdd98dd70a3d955d3124553a84e5beae467e63
    role: context
  - path: pages/traits/genomics/shango_system.html
    sha256: a1cf45c504741df9bcba5f679e5264c2caa19945275f836e9e3923995ec19142
    role: context
  - path: pages/traits/genomics/shedu_system.html
    sha256: 51c7d6dc415fcdb915ba0bd84eb4a98a387480756a25f6d6bc58fd4933fff86b
    role: context
  - path: pages/traits/genomics/short_lamassu_system.html
    sha256: 4ff054ab3034dcc75df3543b5b7172f56d8b72f948127b1f138296685989552c
    role: context
  - path: pages/traits/genomics/shosta_system.html
    sha256: a69cef7d414b76a8ceeaea50cceecea9070b2247a01cdc62318fc3de9ec183cb
    role: context
  - path: pages/traits/genomics/sirona_system.html
    sha256: cf63a032eb7ae4909e402990c56c99eaefa13c0ec90772f1121b6dc415ce19bb
    role: context
  - path: pages/traits/genomics/six_a_mbl_system.html
    sha256: 0ef7cd315c6f36451c5f627635fea58406c826a8173872e456b05a71998c04e3
    role: context
  - path: pages/traits/genomics/snipe_system.html
    sha256: d9c146c3d224d7adb999f1dab642624e0f1592ecdf9112131465fd7c49fbf2c8
    role: context
  - path: pages/traits/genomics/sofic_system.html
    sha256: 2dcbe9d22b1408b234966b5fe4b3279eec59709bfd0532d5b895e2d629ac5c83
    role: context
  - path: pages/traits/genomics/sparta_system.html
    sha256: 6144e81f9ba084da9cc6573fad34f604cdb273c9dd03ae28b752e19d272ebbd4
    role: context
  - path: pages/traits/genomics/spbk_system.html
    sha256: 44381096914808a88404958cd55ed556f606fadd084ea4c0b123887f3f2a6067
    role: context
  - path: pages/traits/genomics/sspabcd_sspe_system.html
    sha256: 94f33a25adaf4ef442fa8599ef63aa3d87af3929ba538da1672cbba8ade58ea8
    role: context
  - path: pages/traits/genomics/sspabcd_sspfgh_system.html
    sha256: 7ec81f457e40525ae306d5d85d18090322036412841a9cc8a63b0fc4aa914ba5
    role: context
  - path: pages/traits/genomics/stk2_system.html
    sha256: a10fe547dba815d3f50a4a595ff81e720cfd8dcb9f39dc6190e109c74ca0d968
    role: context
  - path: pages/traits/genomics/sucellos_system.html
    sha256: d2a9195ff2d8434a5319a8b5b5936d19e9c3e33dc03fbb508e29617d284b6dce
    role: context
  - path: pages/traits/genomics/tab_system.html
    sha256: 0543c3b9c5085ae512fb18ab4986946d26c3ec39bb92ed9a81c1d6a708a9eee2
    role: context
  - path: pages/traits/genomics/tagi_system.html
    sha256: 23a4be1224806f2ae682ef15c7a3870f917ac7bc76b38837ff0ff4cfcff66a94
    role: context
  - path: pages/traits/genomics/taranis_system.html
    sha256: a19efb6c81dac2d11dfcf624a7b912880048557584015dff643a4f6e2ebd2e02
    role: context
  - path: pages/traits/genomics/tgvab_system.html
    sha256: 21586ea89a6ffd714ac056f97dd82c5d80757c240539e2ffc66dd02f4b31e79b
    role: context
  - path: pages/traits/genomics/tha_system.html
    sha256: 920b67007b46fae0a2d18bf650d97d76f3925a792d61d7a9849cfe42ac109b43
    role: context
  - path: pages/traits/genomics/thoeris_system.html
    sha256: d48577dc58105d3f16ef5860e235a16677121ff464a5096059b88f18065f8f0a
    role: context
  - path: pages/traits/genomics/tiamat_system.html
    sha256: d5f5c90246f3c20c808357f89be4bbf1a2b748e1ce6414307e92aba93056033a
    role: context
  - path: pages/traits/genomics/tir_i_system.html
    sha256: 046d4d082c0990b3a45dc0d510bfd400e52840511ef8b189afae1b676f8a4975
    role: context
  - path: pages/traits/genomics/tir_iii_system.html
    sha256: 2be21c9333f304f17c23b90f8321923236d69109854764f058846db9ae4e4ffe
    role: context
  - path: pages/traits/genomics/tir_iv_system.html
    sha256: 1c60515367270d773f5d9086c9efa87e17cffe9fa0f26073bf96a47aeaf93c1b
    role: context
  - path: pages/traits/genomics/tir_vii_system.html
    sha256: 71d67571c5e9ed53f0af941d53f91184a49d7e41d20df176f91b19d8708d82cf
    role: context
  - path: pages/traits/genomics/tir_viii_system.html
    sha256: 03f395fa5502e2868d15bf6ca870f5131eb9e38d3178910de24c0023fb9f6110
    role: context
  - path: pages/traits/genomics/toga_system.html
    sha256: 17c892491e4ee72c7eb942615bdaaee68a092fa6b6a14cb3cd6f4ea4b6338f47
    role: context
  - path: pages/traits/genomics/toutatis_system.html
    sha256: 8ec9c12683d1be338f9115604f03f52e08a53cb3ac0add0f68ba95d56200790f
    role: context
  - path: pages/traits/genomics/toxin_system.html
    sha256: 10a86db9ac622cb0dfb8ef848575000a8507643c833e7a01ff25c7336155c1fd
    role: context
  - path: pages/traits/genomics/transposable_element.html
    sha256: 891d8fcd97af0de697ee7b8a6527d4830c48e7c05d7b49756933d8af6beb7bf5
    role: context
  - path: pages/traits/genomics/type_i_restriction_modification_system.html
    sha256: 692dee27e4796f11045d9cbd2f37bc797f7a1014f5bdda3b2d687d3f61202019
    role: context
  - path: pages/traits/genomics/type_ii_restriction_modification_system.html
    sha256: e76d9198f3d0c6986d626b758692bfca52bc9bd7e457e1a4703c8e2f0f9cfc01
    role: context
  - path: pages/traits/genomics/type_iig_restriction_modification_system.html
    sha256: 5d0ad2bd4761dda8e447738c8494959908d92064550a64eb95c39934b3639011
    role: context
  - path: pages/traits/genomics/type_iii_restriction_modification_system.html
    sha256: 5c691bf2f9b5467ab43188b781a8f29f902fb582a961d1083d751b31981a2188
    role: context
  - path: pages/traits/genomics/type_iv_modification_dependent_restriction_system.html
    sha256: 7928bf233cdea2f127071833babc9983a8f3f3fd973e683ac3a8c75196f497ba
    role: context
  - path: pages/traits/genomics/ukko_system.html
    sha256: 772622d7eddce56a369c5b906a7e48543325d6d63e4c6e8535f88c0a36cdb8f2
    role: context
  - path: pages/traits/genomics/uzume_system.html
    sha256: 435b15fd7a39a0b6245d4445874e1fc229865230607461f730c4cdc7a98179ba
    role: context
  - path: pages/traits/genomics/vcam4i_system.html
    sha256: 47f7aa7f61a0365f38d0fbb738dd209bdc7190571bd42aaaba4f8533d1db75f2
    role: context
  - path: pages/traits/genomics/veles_system.html
    sha256: bf1e000432dfe63d8cf4e90cad4ac6dd25682ed0d88df47b8b6764c429d94795
    role: context
  - path: pages/traits/genomics/viperin_system.html
    sha256: ee6ae658b12b0d9187b09cf4373cf4e54ab0c4ac2119fdf6a24fccfe3b0bee79
    role: context
  - path: pages/traits/genomics/vp1796_system.html
    sha256: 07b8f729a5887540986c316c1fc059240ee990070861bab2f0aec2664fe70dd5
    role: context
  - path: pages/traits/genomics/vp1817_system.html
    sha256: 54b3d7a79ac6f47a9adc04ffd5f829dc07787101e44e0a2efe4ab3f61ca46ecf
    role: context
  - path: pages/traits/genomics/vp1823_system.html
    sha256: 2ac331e5f9d2c854e2bebaf33993e4bfeef0db0d7bc0bac668a1147da776f3ec
    role: context
  - path: pages/traits/genomics/vp1826_system.html
    sha256: 440eaf615beeed49ca5c3bd6550afe22f08b01b2f4dc2c2e32c15c7b65ad846a
    role: context
  - path: pages/traits/genomics/vp1839_system.html
    sha256: 011af30da122e8477a26b65fad88c9fcc416cfaba6abc57d8b98a2b8efb7750f
    role: context
  - path: pages/traits/genomics/vp1840_system.html
    sha256: 6b28f5ca309b0bb283ffbe928e030ea955321c391f13041a3531da2c0291b16a
    role: context
  - path: pages/traits/genomics/vp1848_system.html
    sha256: b2f03f8ceb943094498a7a44d928cc35c3cd819e7edce355f58749a705c3daca
    role: context
  - path: pages/traits/genomics/vp1851_system.html
    sha256: 02664c6425a13755c4acf2de3c539cf833936e41d5680904ea02d27305b07571
    role: context
  - path: pages/traits/genomics/vp1853_system.html
    sha256: 09c286c31b2dff90a2dbac37cde2fe69cd204af3376bed960ef85087d48687b3
    role: context
  - path: pages/traits/genomics/wadjet_system.html
    sha256: 1e4b1d669cd595877599ce295a03c01385804c3e44b96729fde80a4234c47259
    role: context
  - path: pages/traits/genomics/zorya_system.html
    sha256: c42dd33a1163d573b045c8a110d0ecb09d25be696efc2ec1e8162373cf7fd964
    role: context
  - path: pages/traits/genomics/zorya_type_i_system.html
    sha256: a80e6f502218aa34c147f82aca347ca961140e788f0cc42b66a4cf653735d9ec
    role: context
  - path: pages/traits/genomics/zorya_type_ii_system.html
    sha256: 3fece525261321cb7846105b806dcb62b20d71e3777722f2342a740c2ff0d5dd
    role: context
  - path: pages/traits/genomics/zorya_type_iii_system.html
    sha256: a82c921d9ed9643539bca7b85d644d8f3f2a80b6c17f8f13d44cda787ae461d8
    role: context
  - path: pages/traits/metabolism/accumulates.html
    sha256: 4cb3a5d1b05a36348385f4338af1594f71360e92f242d1743467361558276f47
    role: context
  - path: pages/traits/metabolism/acetoclastic_methanogenesis.html
    sha256: c32c7c9fca9da6edd10cd5f726e2e3a7e05c3da87ef2dd720aea5e73a73965a6
    role: context
  - path: pages/traits/metabolism/acetogenesis.html
    sha256: 0b7f1ac8bb79ae9e5dfddc45452e70337888c9babc113c83454576bde193fdda
    role: context
  - path: pages/traits/metabolism/acetone_butanol_ethanol_fermentation.html
    sha256: e82fb2eb8e3db9e04cb089334234045b58deeb9de17bb0379604df27a4991d4a
    role: context
  - path: pages/traits/metabolism/aerobic_respiration.html
    sha256: 7844409092900a378f79641294a192ee88bc2d32ea2764558082210977842dbf
    role: context
  - path: pages/traits/metabolism/anaerobic_ammonium_oxidation.html
    sha256: 02e4a57deb7181a29da971d903826b2c758f8731878930ed5375f68e33f79550
    role: context
  - path: pages/traits/metabolism/anaerobic_oxidation_of_methane.html
    sha256: e891a4cfd0a0c6a87b98df161876c28b7d1fdd84f8dcafdd14666316b60b7482
    role: context
  - path: pages/traits/metabolism/anaerobic_respiration.html
    sha256: 8c383d9dee7663917cda13e8a2acd9bee16a7e32772f81792ce7238fa71cae3c
    role: context
  - path: pages/traits/metabolism/anoxygenic_photosynthesis.html
    sha256: 90d05c3d4ed8189dd332936ea622341e2676b243d021b60e3bbd31cbeed87fb8
    role: context
  - path: pages/traits/metabolism/aromatic_compound_degradation.html
    sha256: 9b6e5530c405a01fdb2e025c0c3f0a49b5e6755c26f61a43f92c714894fa5fcb
    role: context
  - path: pages/traits/metabolism/aromatic_hydrocarbon_degradation.html
    sha256: b68f4a99f3b010cf70cadce80f83f2bb210f7f904e8ad2bbaf7d6f0f81faa03a
    role: context
  - path: pages/traits/metabolism/arsenate_respiration.html
    sha256: b6f61bf1a080908084b146f96258841c6eeba29c77510b580288781ee203b5c1
    role: context
  - path: pages/traits/metabolism/arsenite_oxidation.html
    sha256: 0f2ebc7a223e61fb2d88e1d735c0bd3859029bdce98326f8bd76c1b945959a96
    role: context
  - path: pages/traits/metabolism/assimilates.html
    sha256: 8c7f79d485d43000d9a8d3db2eea0e73ad8af719c91e65da91caac33f6b0b936
    role: context
  - path: pages/traits/metabolism/biopolymer_degradation.html
    sha256: d4d452256f262b0b02705f81887fcd8978d88d0d9b6a4ab5ea388ce85e9e6684
    role: context
  - path: pages/traits/metabolism/builds_acid_from.html
    sha256: d33ead1b1f87217a75f4b9520df0cc9f4e2d2409d37e7b1424a3c71395d78138
    role: context
  - path: pages/traits/metabolism/builds_base_from.html
    sha256: 09fc376d40466f4b8ab8a67ab69115897fdf041d61745f608771a99033d33f45
    role: context
  - path: pages/traits/metabolism/builds_gas_from.html
    sha256: 62ae5690d369a3eec0cae2d3e26b9ff7436a1510638f9bf16ce86f2bf9103aee
    role: context
  - path: pages/traits/metabolism/butanediol_fermentation.html
    sha256: 3028e6ab2f55aede7ea50dc7d492c54df3e88821b449fe22d25831776212ef4b
    role: context
  - path: pages/traits/metabolism/butyric_acid_fermentation.html
    sha256: add6d0629f1b06cc96d9a3aac74dd15d1aa2fc241ba2edb75dd92b6dcbd2250a
    role: context
  - path: pages/traits/metabolism/cable_bacteria_metabolism.html
    sha256: e4b5c3351cf9a8c58f169f9a2f0e28afe81060c60eaedaaf8f97c18089965fbe
    role: context
  - path: pages/traits/metabolism/calvin_benson_bassham_cycle.html
    sha256: 1b39f50beefe671bb8f923ea1e511f15b78ce8a6d9a0ca7bc992fb4d417a8cb7
    role: context
  - path: pages/traits/metabolism/capable_of.html
    sha256: 3a019431b31815482edfa595d20444d290389da49b4c44c296bede4660d0faba
    role: context
  - path: pages/traits/metabolism/carbon_fixation.html
    sha256: a1a98247618a0914cd0674cb75cd40ba638a7b2b82b53a094c92b2d816a58650
    role: context
  - path: pages/traits/metabolism/cellulolysis.html
    sha256: 6bcb5afb34d2b497413e3b8511a59c3c1b28711ac6bdffe9cb8a5312e7e6607a
    role: context
  - path: pages/traits/metabolism/chitinolysis.html
    sha256: 5bb279eeb82eb1f7f138c88aa7c1646deb7dac5c4933df33a20673152d921403
    role: context
  - path: pages/traits/metabolism/chlorate_respiration.html
    sha256: e0127fa6f7fb81d53031f5e80323d7d6d8568fb5b7e7be9ca9eebbaebe901f7a
    role: context
  - path: pages/traits/metabolism/citrate_fermentation.html
    sha256: 5555c3ff9666f8658c3476b2b9f3ce27015c0e933729880f6e6d9f6d72cfcc49
    role: context
  - path: pages/traits/metabolism/compartmentalizes.html
    sha256: 1f9c84a5a524ca8031ef86089acce5eb3863b34ea982d04058b883026bce20d5
    role: context
  - path: pages/traits/metabolism/complete_ammonia_oxidation.html
    sha256: aecf428f5bd4305c4741ac964b3a1ed0b5fbbbce6a49e5932792fabf293361b7
    role: context
  - path: pages/traits/metabolism/dark_hydrogen_oxidation.html
    sha256: 7ad5412445d0e867860cc9ab3564115642ff78fc4e0cfafb3ac73116912638c3
    role: context
  - path: pages/traits/metabolism/dark_oxidation_of_sulfur_compounds.html
    sha256: 289e81d4a4f93a069357143d097e44f9338e41cf7694b34fac311bbe6e461a1d
    role: context
  - path: pages/traits/metabolism/degrades.html
    sha256: b8b1d24f3733374ee6a007dbe558b441039a7c95186c9c99453788d5dd131e19
    role: context
  - path: pages/traits/metabolism/denitrification.html
    sha256: 35c0153f2370a5d1284581fb828e541165d02837eff07e402bff3786de18e70c
    role: context
  - path: pages/traits/metabolism/dicarboxylate_four_hydroxybutyrate_cycle.html
    sha256: 99dc6cf35a3d3434455cdd08bb92044bb2c3eab83e7adcadf852c3fd2077c114
    role: context
  - path: pages/traits/metabolism/dimethyl_sulfoxide_respiration.html
    sha256: 0e1219ee7c0032ff7310e8c10a90d00534def7a0f5a6b66cba981e85557a240a
    role: context
  - path: pages/traits/metabolism/disproportionates.html
    sha256: 6da8f736e61140daeb1e9864cc6cd69086bbc86d327c097f4e5f7d45a71b48af
    role: context
  - path: pages/traits/metabolism/disproportionation.html
    sha256: 6bcff7c5dffa3dec6c38d57e043ce67bdee14d8e5718ed64318c15f8739fc92e
    role: context
  - path: pages/traits/metabolism/dissimilatory_iron_reduction.html
    sha256: 47a6e2246f43d40854d58d66ec5a796befe3ffdd67309d223b89385f30d2056c
    role: context
  - path: pages/traits/metabolism/dissimilatory_manganese_reduction.html
    sha256: 29758407c57c35787de4943e7eea9d2c5284e153f872e165e61c26d84a36f80c
    role: context
  - path: pages/traits/metabolism/dissimilatory_metal_reduction.html
    sha256: b268f942b2d126b58278af3833fcf1901f49324acdf6401f80859f44e6aae4e6
    role: context
  - path: pages/traits/metabolism/dissimilatory_nitrate_reduction_to_ammonium.html
    sha256: 23a218be52ca11d6ee4e4c4cfc4dc3cde2cf78fb1097543f39ef93b37ad64beb
    role: context
  - path: pages/traits/metabolism/dissimilatory_sulfate_reduction.html
    sha256: a7b830a15243d8009b88f39e1cbe17b731a12bc48c61e54f28a34704af89c174
    role: context
  - path: pages/traits/metabolism/does_not_accumulate.html
    sha256: a3f6da306367ff76c9f5b975f864466639be1a8e68600a92302ff43556b9ef9c
    role: context
  - path: pages/traits/metabolism/does_not_assimilate.html
    sha256: 4d4636826db9a42e17bb0f841a03235654349b188d36a0984c88f03c36f7014d
    role: context
  - path: pages/traits/metabolism/does_not_build_acid_from.html
    sha256: 1ebebc9f09d1ab2b3a1976f78faa5a852c38725e8375bb63c25b61c4af991f57
    role: context
  - path: pages/traits/metabolism/does_not_build_base_from.html
    sha256: 008f91d6947078b71b6f71c5cb88eb094e14d45c2624cf16f29731a4532acbf5
    role: context
  - path: pages/traits/metabolism/does_not_build_gas_from.html
    sha256: 4e889f9458190a0fe01d4c95d75f3c899eee3beee9a47eb25b2df35c4dfebb78
    role: context
  - path: pages/traits/metabolism/does_not_compartmentalize.html
    sha256: 9887d77580787e8a3fadd130633a3d7ab762eac5478f1aa03c8b6bb2392d6670
    role: context
  - path: pages/traits/metabolism/does_not_degrade.html
    sha256: f6922126b15a5e38845089c36a4bc758af39bce115b84666780ce20f87be1a1e
    role: context
  - path: pages/traits/metabolism/does_not_disproportionate.html
    sha256: e8978cd45e3bf78940685eeeb43666d9413f1439366f8b288e8479cbdde57714
    role: context
  - path: pages/traits/metabolism/does_not_export.html
    sha256: 72c892b52c396216ef1c3b0517bca0a7beb2f88d052b672a174cc9deb86a4e93
    role: context
  - path: pages/traits/metabolism/does_not_ferment.html
    sha256: fbf7feb7dfe629047ea9901366f6928fbed95ea934c84fd75135042c1289351e
    role: context
  - path: pages/traits/metabolism/does_not_hydrolyze.html
    sha256: 717a5ecf73fbc67a26f434821ff61c96419f7f168697b54b4b12a09aaca726b0
    role: context
  - path: pages/traits/metabolism/does_not_import.html
    sha256: 131f8c7e40f05fa734a2425fefdf7722d79bf1816f75e34007e6c92e10967b00
    role: context
  - path: pages/traits/metabolism/does_not_oxidize.html
    sha256: c6c33340aecb99a836dd4d2966bb068064f1e8342817fe6645a4781b0e3142d3
    role: context
  - path: pages/traits/metabolism/does_not_produce.html
    sha256: f4701b8ff7c3f5a1c17b5c67674c8faa3d9f8631dbd2ff0fd065ae3ca3ccca44
    role: context
  - path: pages/traits/metabolism/does_not_reduce.html
    sha256: 5a71d9c5186daedbe271be40746f1a9c2ed9906c45b573a944dd44de81f3311b
    role: context
  - path: pages/traits/metabolism/does_not_sequester.html
    sha256: 18875e740828652bbf75d7a0167a808841b699eef244f4fc39ba1f84937514c9
    role: context
  - path: pages/traits/metabolism/does_not_show_activity_of.html
    sha256: 4f77f9a9b281949315a759b1198672fe0ab895aa8a098084cba04b5b894fbb71
    role: context
  - path: pages/traits/metabolism/does_not_transport.html
    sha256: eca55f9b32149c8792b13d7d32e814e824649889e2cc1c5956f21f885abe1324
    role: context
  - path: pages/traits/metabolism/does_not_use_as_carbon_source.html
    sha256: 0e4f4fe6a234f194471b39e66a6f9c6709bbb3464c7487200d192c2b9131515d
    role: context
  - path: pages/traits/metabolism/does_not_use_as_electron_acceptor.html
    sha256: 4923cb0af2c4e805d799ad7b88552275593c39b4a95a9ca0b3f76f84445eeb9a
    role: context
  - path: pages/traits/metabolism/does_not_use_as_electron_donor.html
    sha256: 1cf07a748764d1f043aeae89f13a9d840e55959e1b0187f60a119f6112d393b1
    role: context
  - path: pages/traits/metabolism/does_not_use_as_energy_source.html
    sha256: f7936c40e68cc055e46b7d43d513882f12fbc46de70d5e153317ea7d1879cdd2
    role: context
  - path: pages/traits/metabolism/does_not_use_as_nitrogen_source.html
    sha256: 9e5b8d50f2191e4c8f29557c43f88fde2f746af21e7367e915c2e2961e3b6e05
    role: context
  - path: pages/traits/metabolism/does_not_use_as_sulfur_source.html
    sha256: 9296fd7dcf62ab2606c6d6e37ee807bd01772ab137182477f38c74be2362efb4
    role: context
  - path: pages/traits/metabolism/does_not_use_for_aerobic_catabolization.html
    sha256: 1e2707dfd8edee40935ea9dc0d353b31db2b30e03ac65498319806b628cafb6f
    role: context
  - path: pages/traits/metabolism/does_not_use_for_aerobic_growth.html
    sha256: 47150bb43bb923fee754787cda720028780a7f9c86b6331397e0f880a1049e6d
    role: context
  - path: pages/traits/metabolism/does_not_use_for_anaerobic_catabolization.html
    sha256: d081a6025a6b892cbb053c0293e052375ba046046065b69b54fd6b410ca0206d
    role: context
  - path: pages/traits/metabolism/does_not_use_for_anaerobic_growth.html
    sha256: ab0bb1aa0c1dcfd98fc746232494f9e228555537ccbf321ea9d4d22691144da2
    role: context
  - path: pages/traits/metabolism/does_not_use_for_anaerobic_growth_in_the_dark.html
    sha256: 59ed0a53f728bb676919dd1b74fd951bce243dd4479c739317cf67ac1bcb7fce
    role: context
  - path: pages/traits/metabolism/does_not_use_for_anaerobic_growth_with_light.html
    sha256: 29b1b90770010045926426e9bd9276e1b7a7210bacc972af579003ffbae18feb
    role: context
  - path: pages/traits/metabolism/does_not_use_for_growth.html
    sha256: cb0066ef18dcd1b17dfc3e8bf27c6997037a544f525e2fe2c6f6686f649f2d11
    role: context
  - path: pages/traits/metabolism/does_not_use_for_respiration.html
    sha256: 6a3928b194aadce5ff1cceb48b0f71b70f96fbb78928263b6d7256d5395cf6e9
    role: context
  - path: pages/traits/metabolism/does_not_use_in_other_way.html
    sha256: a956eeb5dae58bab78ab3bfb242946e1f99160b37e141fdd8cd36960f8050e65
    role: context
  - path: pages/traits/metabolism/electron_transfer.html
    sha256: 4d1f8c1dd1da48b1bead88976e31bb89def43ff66c4164a69deba3fe6267fac3
    role: context
  - path: pages/traits/metabolism/enzyme_activity_analyzed.html
    sha256: ea7d88cb1ed18e3c38eaa0a5d53af97fe3358431102f979248488a9ea12b469d
    role: context
  - path: pages/traits/metabolism/ethanol_fermentation.html
    sha256: 0401d37e4f15931e734b22cd5d272d81e67653c14735159a5a6d4ced85a688dc
    role: context
  - path: pages/traits/metabolism/exports.html
    sha256: 96f14a7c21534cf09ff46aa36e03ab010d94f21456b92a91ffe94334ba4a8ee7
    role: context
  - path: pages/traits/metabolism/fermentation.html
    sha256: b71dccd2866c660befacbc8d4627b4d6538bc23e796a63a757032a87f241c368
    role: context
  - path: pages/traits/metabolism/fermentative_hydrogen_production.html
    sha256: 2c0a999b99e840e6d36457959237a2e3842888b960097391964633310b8e706b
    role: context
  - path: pages/traits/metabolism/ferments.html
    sha256: a976501f66214edab88aff42fa2cdd27636b22fdb5c37f459ca8f7e29d37aa57
    role: context
  - path: pages/traits/metabolism/fumarate_respiration.html
    sha256: 095ce241a67b5e2ebb5c2edf1e12bba7ee819df1c1cbd4db02f8772e1317dcb9
    role: context
  - path: pages/traits/metabolism/has_growth_nacl_observation.html
    sha256: 87fbd94ca28396a2b08ccafcee6a2814eeb6fcdc4fbf2afe4698c4576f090b4a
    role: context
  - path: pages/traits/metabolism/has_growth_oxygen_observation.html
    sha256: 838784356e7ad5fd448d7781ff1ac3f718f1a060a33f19e5eb7cf83cb0176f8d
    role: context
  - path: pages/traits/metabolism/has_growth_ph_observation.html
    sha256: 7c13891f91a241b4ded906de43f689a5ffec78d638b766c128dca53689c9fe66
    role: context
  - path: pages/traits/metabolism/has_growth_temperature_observation.html
    sha256: 7c25e8effbc8cf40be3ac8b919b2cc6b1ab48433208715ecab974731ad621c21
    role: context
  - path: pages/traits/metabolism/has_nacl_delta_observation.html
    sha256: f95a87c69f14f31da8ce35cf0593d9b28aa93595025d5ab48e168292df8e9dfd
    role: context
  - path: pages/traits/metabolism/has_nacl_observation.html
    sha256: 742803a29a96fa9590fd192f078182c6629b1e9803630529a7b55d2ed7adaef9
    role: context
  - path: pages/traits/metabolism/has_observation.html
    sha256: 0bc3191cd5124fe993628e77e611596ae7b8ecd24e127b965f2958d808423d1f
    role: context
  - path: pages/traits/metabolism/has_optimum_nacl_observation.html
    sha256: 9c4520771ce23f50a4d1b741f29191e6e4ff90aefbc3f35bf35e3a0638dc58d9
    role: context
  - path: pages/traits/metabolism/has_optimum_oxygen_observation.html
    sha256: 592b22df1407fcf6a9af281bca7381ba7e9cba3a20ee4089f9538b7f44d243cf
    role: context
  - path: pages/traits/metabolism/has_optimum_ph_observation.html
    sha256: ab754ec1dff4ddf4c9e0882d673e631926bec4344800771ade7b684a9b54f492
    role: context
  - path: pages/traits/metabolism/has_optimum_temperature_observation.html
    sha256: 66fa08e32d5874d22dbf12707516fb47b67422975ae57c3787e37ca8f4834ddc
    role: context
  - path: pages/traits/metabolism/has_oxygen_delta_observation.html
    sha256: df9f8e596faebcadd12721f4ae284b9de4fc6136e0397dfd58087a2d355bd502
    role: context
  - path: pages/traits/metabolism/has_oxygen_observation.html
    sha256: 0550b97e080bbccdbb788f4665a159960d75f8b1e35f7f6c2ac2a1a2b384e895
    role: context
  - path: pages/traits/metabolism/has_ph_delta_observation.html
    sha256: 3208d9d0def22c89d0864d15d3822b45bee0ab220dad889928fb230c74d92cff
    role: context
  - path: pages/traits/metabolism/has_ph_observation.html
    sha256: 227d1a5add454b67a0bed32c683233c39a1fa28c69f0d69d57033a912105c352
    role: context
  - path: pages/traits/metabolism/has_phenotype.html
    sha256: 9ae2f9564a9485ee9a4bc24b903c6bc44ed55c7472db4dace13d672ec8c2582a
    role: context
  - path: pages/traits/metabolism/has_quality.html
    sha256: b78f6104874d610ea8ffc41ad1bbbb4ecad3c3928ade2e32af11500ca4ba20f0
    role: context
  - path: pages/traits/metabolism/has_range_nacl_observation.html
    sha256: 2ce47c1f823df2b64bd3291969f1725c868103b6a1651216a7c21ae35f2cbac9
    role: context
  - path: pages/traits/metabolism/has_range_oxygen_observation.html
    sha256: eb96896fcbadef81c5c5f535c06da984ffedb2bb2cd25880381b6507603ad1d0
    role: context
  - path: pages/traits/metabolism/has_range_ph_observation.html
    sha256: 1f11d36243687b1d979f481ded98e322d4ab571603892c3e640b6ed197e9ccbe
    role: context
  - path: pages/traits/metabolism/has_range_temperature_observation.html
    sha256: 047965475cbf83e62502bb526b595dbf21beed0522d24d72d1b80d76cc4c0a2a
    role: context
  - path: pages/traits/metabolism/has_temperature_delta_observation.html
    sha256: df79626ca802edf6e21415defba85b5423d72da6278c04f05fe634011aa04129
    role: context
  - path: pages/traits/metabolism/has_temperature_observation.html
    sha256: 6c86ef75418a72a9c7010e4271fa1dab56a350c5af0b491cfea608af70c86148
    role: context
  - path: pages/traits/metabolism/homoacetogenesis.html
    sha256: fc404dd240211b3e797189b8181ea7684a36045f45d79f0f6ea8f1df7652e322
    role: context
  - path: pages/traits/metabolism/hydrocarbon_degradation.html
    sha256: ac83c10e9388816434a37e9d188230e08282d411da9c333ed6a20bb5e7f415cd
    role: context
  - path: pages/traits/metabolism/hydrogenotrophic_methanogenesis.html
    sha256: 8ac51e2dfaa908374de1051acce9f1203e58a2f4f12d0b1059653798d9fe84a3
    role: context
  - path: pages/traits/metabolism/hydrolyzes.html
    sha256: 7bb5e356045f9a2afec23cf583e4366da3b00a7c8559bfd47eb31b0eac3fff8f
    role: context
  - path: pages/traits/metabolism/imports.html
    sha256: 7fd3718f52cc155d2b4ac682f37436f6e7e2fc8b78a000d423f1ddf18007b4de
    role: context
  - path: pages/traits/metabolism/iodate_respiration.html
    sha256: ef63774ca68cc4af759470e987bac91347fa34da1c62bd06bed60a67a4b52953
    role: context
  - path: pages/traits/metabolism/iron_oxidation.html
    sha256: e74297d3c5961875862b2fe4e2ad65f7de68b825107754ecff61168c7f76ec2d
    role: context
  - path: pages/traits/metabolism/is_not_required_for_growth.html
    sha256: f35286db860e1e4d0b6894a1d9444d0662d19ab1d52fb5670ce7744fef22cb86
    role: context
  - path: pages/traits/metabolism/lactic_acid_fermentation.html
    sha256: b2b439925fbf4e91808c9c26e24baf1d627da22ef5d5bfeb6e6e593dd876eb32
    role: context
  - path: pages/traits/metabolism/lignin_degradation.html
    sha256: 070a85c245d4142c3e06aad15a1b2702b7e2e882b1ebd8b9f6346f914986ca5f
    role: context
  - path: pages/traits/metabolism/lipolysis.html
    sha256: cafc5184a58ad225fbd4d3b85c7e49f35b36b00f3ff18195ab35042917fd61d1
    role: context
  - path: pages/traits/metabolism/manganese_oxidation.html
    sha256: 53f3ff4e0b6ea72931021321d6f4cd9fbbe33f78a83446e0afb0176304a25b1f
    role: context
  - path: pages/traits/metabolism/metabolism.html
    sha256: 3f8f31ef431d144da4f461ce6bea3a6833bc6206f50ab14af7dfe3f65a1954ad
    role: context
  - path: pages/traits/metabolism/methanogenesis.html
    sha256: 478209e4a8778d6998975a54d97b7a34aa12cba6d64339ee89842895c3c4f400
    role: context
  - path: pages/traits/metabolism/methanol_oxidation.html
    sha256: 5a0bd9b9728d2b01037733675b60507de27b4dac23bbe3d2d7e61fc5ddd38399
    role: context
  - path: pages/traits/metabolism/methyl_based_methanogenesis.html
    sha256: b1cc657b3d0215521a96923f44ef3bd2e82ce62041475f1fa4c82c3b89fa4726
    role: context
  - path: pages/traits/metabolism/mixed_acid_fermentation.html
    sha256: f4e277847ddda1f428ed4ba82133849b5c7fe0061d8bd7e34c864d1f6ad5e54b
    role: context
  - path: pages/traits/metabolism/nitrate_reduction.html
    sha256: 085ce70ebc9b6c63a258d8a87ddd07480294bb3bc0c77c10fcc1d28db820cb96
    role: context
  - path: pages/traits/metabolism/nitrate_respiration.html
    sha256: be847a4868c3da42f84681abbf9d341e84b3a3121f3ca45035700e5acfd6545e
    role: context
  - path: pages/traits/metabolism/nitrification.html
    sha256: 28bfae87206a551c60f6d08ff0d806038aaba6d43ba5ab9af7c7c3857622ea74
    role: context
  - path: pages/traits/metabolism/nitrite_respiration.html
    sha256: 473139c5b12500c5413aa79aa04e96288867ea172d870a30970a969967883f02
    role: context
  - path: pages/traits/metabolism/nitrogen_fixation.html
    sha256: 21bc912ba63e68823d9fc8977261502798a9de80d5b07ef8e8e11db8e627ff5f
    role: context
  - path: pages/traits/metabolism/nitrogen_respiration.html
    sha256: 157ed0563d044b92f72eb96235afb6e41c30b3182970303cfee955edde61a001
    role: context
  - path: pages/traits/metabolism/organism_interacts_with_chemical.html
    sha256: 8f27938db6674676c2508bcb5cba2ef838a2bf7b0bafbacf9798ef2a76e31f8d
    role: context
  - path: pages/traits/metabolism/organohalide_respiration.html
    sha256: 63e119c3c80727ec55479ef3b88902a304b064538a762907416d9d0916a356a3
    role: context
  - path: pages/traits/metabolism/oxidative_phosphorylation.html
    sha256: 4d30686807fd7157b7543937f3e58315fbf8b86f063c670ff41954f7dff776b3
    role: context
  - path: pages/traits/metabolism/oxidizes.html
    sha256: 20712f3a755ce03919be47ded75908f4a7ee4162cdb4bb50e80f0b1757944c45
    role: context
  - path: pages/traits/metabolism/oxygenic_photosynthesis.html
    sha256: 6efe1712f218bad719aaf1b2c3a14f57aee244e6168a677046415699bc613057
    role: context
  - path: pages/traits/metabolism/pectin_degradation.html
    sha256: f770747928d11fa16592f75db0a38e4e4a19f2e9f5abe9a20c0575f9da45d4a1
    role: context
  - path: pages/traits/metabolism/perchlorate_respiration.html
    sha256: e6280447fc131979befe8cecfab4a16a411e11c10ca5204727cd75db828f1d79
    role: context
  - path: pages/traits/metabolism/photoferrotrophy.html
    sha256: a71b4c9e317a813cc63c39bc489bb4ede6ce88f905a8cf32c76ed7c9e17e3a05
    role: context
  - path: pages/traits/metabolism/photosynthesis.html
    sha256: cce5394a721bc9690f95e4a851986b6ee14fd9a18b519625764ca618ce13ac1f
    role: context
  - path: pages/traits/metabolism/phototrophy.html
    sha256: fb25822ff372b0c28692c8e628ed8f523b36bf2619a9b859dbdf6a780ceca8d8
    role: context
  - path: pages/traits/metabolism/produces.html
    sha256: 3ebb67339af12b700f6ec726c2fa69d5a9da4834d3f2a0aa8422c31e272f2099
    role: context
  - path: pages/traits/metabolism/propionic_acid_fermentation.html
    sha256: b7c063841f6d2f21b003c721df445aeafd616dfd9e08bcb398e8b984cb71ceca
    role: context
  - path: pages/traits/metabolism/proteolysis.html
    sha256: 0ec243d0ac4e948f1fe1d24a019af8872e48346d79bb81b89f5a6568486af281
    role: context
  - path: pages/traits/metabolism/proteorhodopsin_phototrophy.html
    sha256: 8e64109762501aad3257c1965a9bdbf9fc76abb895bc1f79fffcac4a3b68b00e
    role: context
  - path: pages/traits/metabolism/reduces.html
    sha256: a4d16a1e43815590492b0ef3c7db87fa550cde252ba3394b49d2902428bffa9c
    role: context
  - path: pages/traits/metabolism/reductive_tca_cycle.html
    sha256: 633a64119de4e16f2cc539d9c611b414d69da0045517207b4022fb60a285767d
    role: context
  - path: pages/traits/metabolism/requires_for_growth.html
    sha256: 4eca1b1281255f205cbeda2f4cb144c6e0c8cfc5268937463cbabc9790ed652b
    role: context
  - path: pages/traits/metabolism/respiration.html
    sha256: 0d923ed22be5cefa65907afa5cfeff6f3c05879c1aa578ef87fb0fb192a04899
    role: context
  - path: pages/traits/metabolism/respiration_of_sulfur_compounds.html
    sha256: 0f68a87cb59cc95b1f510c566f95a022f8f80720c9d47338a25749d2f1dcca99
    role: context
  - path: pages/traits/metabolism/selenate_respiration.html
    sha256: 92bafadb7d1629f3ce517dbab38f4c6903e0297747461c184e48ab73cd0796c1
    role: context
  - path: pages/traits/metabolism/sequesters.html
    sha256: cfff7725099309235c930b7d56fc31a1b1c62ffffd00b28f3044189f56789224
    role: context
  - path: pages/traits/metabolism/shows_activity_of.html
    sha256: f13202a4decb4191703e9f170d21f6a95ece41fd19e012f73c3e8b95bcfc7b76
    role: context
  - path: pages/traits/metabolism/starch_degradation.html
    sha256: 6c2392f0cb504cb8024c83160db36fee53944dd8929c270f70c49b6f9b986d38
    role: context
  - path: pages/traits/metabolism/substrate_level_phosphorylation.html
    sha256: f9b34aaf425981b4207f5c0ae021a5098c48ffb59bdf238e70e79a9f6535238f
    role: context
  - path: pages/traits/metabolism/sulfur_oxidation.html
    sha256: cbf4ff7dd3d427ccd0c604620f41b8621977325f90ae145b7cf47a694e5bd85c
    role: context
  - path: pages/traits/metabolism/sulfur_respiration.html
    sha256: 9035381960cc3f4ad39bbcc4506a5f758bd1c5c89a0ba507e91001aa86c0d970
    role: context
  - path: pages/traits/metabolism/syntrophy.html
    sha256: bfc77806d24d03aa232ac48533ef325fb57c99dbd617f2fc6580725e9508ac37
    role: context
  - path: pages/traits/metabolism/tetrathionate_respiration.html
    sha256: 7767956bdff4c4856d2338529bbfbb2a79c3132cb412ad2b4119dbddc31e67fb
    role: context
  - path: pages/traits/metabolism/thiosulfate_respiration.html
    sha256: c3ee1e47c5048856360c7c60231ae0f02992df52c6588352e805a0e5833a2ef5
    role: context
  - path: pages/traits/metabolism/three_hydroxypropionate_bicycle.html
    sha256: 9c8f8e4fdaffd32838560d141f1c7e33ac4b96059ef658cb903ba4f3ee9da8fd
    role: context
  - path: pages/traits/metabolism/three_hydroxypropionate_four_hydroxybutyrate_cycle.html
    sha256: 2a5ad0a532adf783b385859d157d369856785f0796effc9f21c475efae44d25f
    role: context
  - path: pages/traits/metabolism/transports.html
    sha256: dc4fab2f5aa0c0990d988c29f4fe3c11efdcbf912441d8864d9e0f830e7c20a8
    role: context
  - path: pages/traits/metabolism/trimethylamine_n_oxide_respiration.html
    sha256: 183782f6fb33664744bd654b5bd19fb1b1ffa4d357c6177d3fdda61f454fd9b7
    role: context
  - path: pages/traits/metabolism/uses_as_carbon_source.html
    sha256: 7d8f3399c807770dcb20f47790fb9ee73043f9ec2169a5d7efdf88726fe9c16a
    role: context
  - path: pages/traits/metabolism/uses_as_electron_acceptor.html
    sha256: b8b44143b82594cd91ba4ae299c7e575d31594b324ac9edc047309b4a357f3ae
    role: context
  - path: pages/traits/metabolism/uses_as_electron_donor.html
    sha256: 558fd37c7ab67deb40af2e6d84bdfb117aa82b3e6d257063d7008792365288c0
    role: context
  - path: pages/traits/metabolism/uses_as_energy_source.html
    sha256: 5de175270faec7e3f16a841b65691e8fa2953f480e9e3e108aa1b83d6444cb8e
    role: context
  - path: pages/traits/metabolism/uses_as_nitrogen_source.html
    sha256: 4ae5dfc932f71dd66a9625037dfab95c86d6688ba91780ead805c79cbf1818e2
    role: context
  - path: pages/traits/metabolism/uses_as_sulfur_source.html
    sha256: d3952a9678ebee91bfcb77235431fdc410b72a1ba161bfea1a3f9b108965141a
    role: context
  - path: pages/traits/metabolism/uses_for_aerobic_catabolization.html
    sha256: e8fdd9f9cbc89ea30c3f715a4dfa67b6982fb39d35e6192e2b6e16530f1846f5
    role: context
  - path: pages/traits/metabolism/uses_for_aerobic_growth.html
    sha256: 0641f921ad28958bb4531bc0e2887c57480f0d6e90559f85da42528f13099647
    role: context
  - path: pages/traits/metabolism/uses_for_anaerobic_catabolization.html
    sha256: e3d5916d92a2a017c9ef89ff7d86f1ff8688f12f2772518b24e9cb05ee0c5015
    role: context
  - path: pages/traits/metabolism/uses_for_anaerobic_growth.html
    sha256: 27cbe9c82c00aeb76aae6f70dd9f85bb35fbaed51f051a1da719587136873693
    role: context
  - path: pages/traits/metabolism/uses_for_anaerobic_growth_in_the_dark.html
    sha256: 46a3e8026377db657912d7576dc6afe9ec2144d53a0c75dd765884364bd0c440
    role: context
  - path: pages/traits/metabolism/uses_for_anaerobic_growth_with_light.html
    sha256: d2ec2c8f2aa1417e790b9198926c49695fa884079c2a7d9569a60a5da7716f42
    role: context
  - path: pages/traits/metabolism/uses_for_growth.html
    sha256: 6287c6242748082db4daca57be003b597384706b3cc0f808ae3d160dbf7a18d9
    role: context
  - path: pages/traits/metabolism/uses_for_respiration.html
    sha256: 8d417405043a64831da5f0cead7fd117064a165a460432c4f5a26a3f2b40f8c1
    role: context
  - path: pages/traits/metabolism/uses_in_other_way.html
    sha256: c1361d5c508220313ade35b8351e371004d613f0f54224819815e875b207f499
    role: context
  - path: pages/traits/metabolism/wood_ljungdahl_pathway.html
    sha256: a8f311e1c212fdf3936f44c88921f9faaef96b905e88b1210bcb29080f7dfb3d
    role: context
  - path: pages/traits/metabolism/xylan_degradation.html
    sha256: bafed5e725e4403f057e54e084ff81fc5ce51c00ad6d696d959f51b40571157f
    role: context
  - path: pages/traits/morphology/akinete.html
    sha256: af36399cbd1696c892765441234843b129bd0731bfe863670b9cd98d4fc89d1c
    role: context
  - path: pages/traits/morphology/amphitrichous.html
    sha256: 2a43231c83f3d87247f47fb3527306e25aee236e120476a1f96510bffddaf3e3
    role: context
  - path: pages/traits/morphology/axially_filamented.html
    sha256: efe787297fd93300e601468ce5d46839ad0e064c7ad312d443ddebddc011e340
    role: context
  - path: pages/traits/morphology/bacillus_shaped.html
    sha256: 8284e87dd523bdb7274f28f513bf924b7ec03ccb60ebc79b664dcd8d01e216b9
    role: context
  - path: pages/traits/morphology/baeocyte_formation.html
    sha256: 4e3af5ecd14584bf5237a9f5bb7693014c119db5c52d11ffac6e38ca62a1cf9a
    role: context
  - path: pages/traits/morphology/black_pigmented.html
    sha256: 31d72403c11ffa02fde94d27e979943fb10006733af760fd17c0e092ef42ea45
    role: context
  - path: pages/traits/morphology/branched_shaped.html
    sha256: 04cf2b3655636b60336427fb050326298dc6074618b6355638a36f98a19045c2
    role: context
  - path: pages/traits/morphology/brown_pigmented.html
    sha256: bbe11245b7cd5bd52c309baf2f65c2d28350da40fd5849091af326f5a90b233d
    role: context
  - path: pages/traits/morphology/capsule.html
    sha256: f7fd40602e2c1bf9696c423442947d605d27eeb7d0ad512a8b5955c1b2ea4b2b
    role: context
  - path: pages/traits/morphology/carboxysome.html
    sha256: 0c4004a5f09c612e50986e8f0cee1136c290c403b86d7ef5a19c6ee44259fbab
    role: context
  - path: pages/traits/morphology/carotenoid_pigmentation.html
    sha256: 77b0c078acab054ba677e711df4ffdad027a528856e7b94a30e33e777bf8ef4b
    role: context
  - path: pages/traits/morphology/cell_length.html
    sha256: 47eff13719788e06c5463f0fcbcbcf45dff602c407b69a8c70aacbbee804a873
    role: context
  - path: pages/traits/morphology/cell_length_large.html
    sha256: 5a2ad0fe823ad9a4f1b66c545a80f3e9be45efdbb0743f7cf4c07db6ca777859
    role: context
  - path: pages/traits/morphology/cell_length_medium.html
    sha256: e6a5368c39d931a60886d0ffc6ba8541d726a0100f267ea4c4c7d8d468c7c9f3
    role: context
  - path: pages/traits/morphology/cell_length_small.html
    sha256: 2ba461399e877e340fe8f9c11ecdb8fa706bf06b7dd4d3d6cf51b024d4ab3ac9
    role: context
  - path: pages/traits/morphology/cell_length_very_small.html
    sha256: 6126997f445ffa234fb74c578148a73604121ef44ac96d684a83c98811d852f3
    role: context
  - path: pages/traits/morphology/cell_shape.html
    sha256: 5052424618aac48958b958a6608c615ddb690be19a43ecb652424759fa141f56
    role: context
  - path: pages/traits/morphology/cell_width.html
    sha256: 22c93501baec78fed819146a66a4087c769e7ff4ff36890ebba2a3689dfe4a49
    role: context
  - path: pages/traits/morphology/cell_width_large.html
    sha256: 78e750a70ab805a09c4ef104badbfabd4bf2769671a3efed90e4413a5033e949
    role: context
  - path: pages/traits/morphology/cell_width_medium.html
    sha256: 7c220c0ca44bea83ef57c8ea14c03e14cf7e1e0fa1bd793bd8280c95111ad239
    role: context
  - path: pages/traits/morphology/cell_width_small.html
    sha256: f63fc0658ecb237a87b6c54ad42048d975f7fe2c716a593e403b3850bde1f6f2
    role: context
  - path: pages/traits/morphology/cell_width_very_small.html
    sha256: 41aab167d12e60d32a281946a62f6864c5dbf17e4679d344a8acf8a2c0108fc6
    role: context
  - path: pages/traits/morphology/coccobacillus_shaped.html
    sha256: 85a5bb9979dc2650c2681f010a2c1cf010c6769d56b637dbb14da1057f716589
    role: context
  - path: pages/traits/morphology/coccus_shaped.html
    sha256: f0700a3f2a2b05e75a106fa5e374798113acde126b83c6974b2b783a0a1bb986
    role: context
  - path: pages/traits/morphology/coenobium_formation.html
    sha256: 984328d3ce9e554565e173169e9abc2feecb98b8ef39ae15432aac22f8d6249d
    role: context
  - path: pages/traits/morphology/cream_pigmented.html
    sha256: e13b61593683499b29ea0d53155eaf8722fad6c574bebd31840ec3551fa1e0f9
    role: context
  - path: pages/traits/morphology/crescent_shaped.html
    sha256: ad64920c6027e46ec9f8cf94940b36409fabbdbe02158d0cb59c4d2567250dc6
    role: context
  - path: pages/traits/morphology/curved_shaped.html
    sha256: 74013a7962050fd40159b682cd28dd6259188ae8984c93532dfe0a39cb2d0029
    role: context
  - path: pages/traits/morphology/cyanobacterial_multiseriate_trichome_formation.html
    sha256: ec0772e9725a9abe9a4f9d94f627806c5943df7c3e7f2b8ee59b044b42715409
    role: context
  - path: pages/traits/morphology/cyanophycin_granule.html
    sha256: 7ca9ca6a3867b0bacb5b5432fb32f14cea7c5ab8c310a7f8e6267a07b4aaf74f
    role: context
  - path: pages/traits/morphology/diplococcus_shaped.html
    sha256: 9cbeea12651af34e19b3dcbe99115c56e89909092b8542dcf2a4032e78029215
    role: context
  - path: pages/traits/morphology/disc_shaped.html
    sha256: b889aee7d80140ab7759ae1dfbea37be121e5689e9defdd9d18a9c7d8cd3390f
    role: context
  - path: pages/traits/morphology/dumbbell_shaped.html
    sha256: 738d5f3f7a8d7d7600856380e353f6f0e7f99f00160351215b2e1664d7a61495
    role: context
  - path: pages/traits/morphology/ellipsoidal.html
    sha256: 60056343971ce95751280d2c95a853f5bf332e03c498ec6612395ec871df0be0
    role: context
  - path: pages/traits/morphology/expansion_driven_sliding_motility.html
    sha256: 7c7e8f36c8ca9ffabb25435be857e9b500e47f83229fbe50d27c6903a06118ed
    role: context
  - path: pages/traits/morphology/false_branching.html
    sha256: 84500c81ab22085ebf42dad0fe9340c881f3aa6e8936759bc684516855bf9770
    role: context
  - path: pages/traits/morphology/ferrosome.html
    sha256: e77a0e1a844adbea41aa30d4bda83362f489ab310d04395bc170dc4ec143fe99
    role: context
  - path: pages/traits/morphology/filament_shaped.html
    sha256: 00a2ba735ada460569e5eda2464eb36409e604def96990e2416edd9907bdb5b2
    role: context
  - path: pages/traits/morphology/flagellar_arrangement.html
    sha256: fef19ff83f723210f2b95468f15f1b2e18e6e9686bbc118287115fc9041dac70
    role: context
  - path: pages/traits/morphology/flagellated.html
    sha256: d7a0350c5625dd4e0cc28ee4811c9a800b83ca46b6cb6c221657fafb966d01b9
    role: context
  - path: pages/traits/morphology/flask_shaped.html
    sha256: d395e8988496ad1b58c54bdd1b6a0df409546b135c19aa78b89f3304b5e642f4
    role: context
  - path: pages/traits/morphology/fungal_adhesive_column_trap_formation.html
    sha256: e0a5100dc0d2b1d8ced570133ecdd54efa4c523813e14c351d5b6c8033786b30
    role: context
  - path: pages/traits/morphology/fungal_adhesive_knob_trap_formation.html
    sha256: 0df965cd5e3f51f4bdc08a6165426fbe270fea2390d67346b5c0548f8e6f83f7
    role: context
  - path: pages/traits/morphology/fungal_adhesive_net_trap_formation.html
    sha256: 74681432164c6f13f948e583d9034da88ac964e4cd58f1eab2e8b2be1aa6559e
    role: context
  - path: pages/traits/morphology/fungal_appressorium_formation.html
    sha256: ace22b8c0d8a27b431175e2347ee8fcd755e03a6583e32a0f0d6297b3475255c
    role: context
  - path: pages/traits/morphology/fungal_arbuscule_formation.html
    sha256: 737c005945f1a3ec3f1fc0871fded0120d3881afe16f4fe4eda493ce262ee8ee
    role: context
  - path: pages/traits/morphology/fungal_auxiliary_cell_formation.html
    sha256: a05aff6cac12cc26f86e8c0cba99bbb29bd0de294969f3b82007682b7b421b9f
    role: context
  - path: pages/traits/morphology/fungal_branched_absorbing_structure_formation.html
    sha256: 24d48c2ae18e8a1ceab2a46d5df109616b0c136368389a03f1d3cd34d7d602e0
    role: context
  - path: pages/traits/morphology/fungal_chlamydospore_formation.html
    sha256: a0456f1baef672e38a179b0906b1d3c4cd62f429b0c3a1267ed7647e6dab2900
    role: context
  - path: pages/traits/morphology/fungal_conidiation.html
    sha256: 1e161cf18c3df6781c4603d99cebd7d7c370fcf49e2f2cd218795f21d66923a6
    role: context
  - path: pages/traits/morphology/fungal_constricting_ring_formation.html
    sha256: 8158b2eff7ffebc9b44431f17cd3a962bec2f4b7de69b1071d30319637aed026
    role: context
  - path: pages/traits/morphology/fungal_hartig_net_formation.html
    sha256: 9c942ff61e1e5b696095e6bf106089f4064e5747bfa963bf34e45a1c22c5b2d4
    role: context
  - path: pages/traits/morphology/fungal_internal_mycorrhizal_vesicle_formation.html
    sha256: 7c4ec54b73da7f1d997b36e732a0cdfd282244b2f553f1e59a326abf6009b76e
    role: context
  - path: pages/traits/morphology/fungal_mycelial_cord_formation.html
    sha256: c8aceb7b84232ff17de0b54b5e9368b674d3cece5715e961424adfe8d51c29a3
    role: context
  - path: pages/traits/morphology/fungal_nonconstricting_ring_trap_formation.html
    sha256: 6d0a095d66b1c63f2dc72d40dc83f6092e8ab946dca97f7c5567de5783699c16
    role: context
  - path: pages/traits/morphology/fungal_peloton_formation.html
    sha256: 974c8cab7180707d41a72389dd6480a3dadfb8316a1291099afdce7578d2e59c
    role: context
  - path: pages/traits/morphology/fungal_rhizomorph_formation.html
    sha256: 72689c34b58a3a127efc9a4cfd6079ad40b7ddda92c2a20db18e389e3efc3e7d
    role: context
  - path: pages/traits/morphology/fungal_root_mantle_formation.html
    sha256: 8445163c3da96804f94a6ebc1b6b61d669c6042e2a4a82a3d09e1be28e626ef0
    role: context
  - path: pages/traits/morphology/fungal_sclerotium_formation.html
    sha256: 0f42593a360b6dc8f1d3ea1cd20a79c3b60b1fe35a09c57a466b149eb9427031
    role: context
  - path: pages/traits/morphology/fusiform_shaped.html
    sha256: f7bb511a86067568a5514cdde531cd0c9dd555df177c2eafd05a613322df47d7
    role: context
  - path: pages/traits/morphology/gas_vesicle.html
    sha256: 999c65e837724d45b090787d9ac265b3bf4aa572232428a67b25e233cad0dcaf
    role: context
  - path: pages/traits/morphology/gliding.html
    sha256: 03f5e4b4479e0ce0f64c6b7aa7242aa6b476b1dd3d3d9e821864f3d77127ad53
    role: context
  - path: pages/traits/morphology/gram_negative.html
    sha256: 59b8f98692755996aedabce4f3e3555a2eb63ae1d7d7761c472ddc59ff8c2228
    role: context
  - path: pages/traits/morphology/gram_positive.html
    sha256: 7ae5cf8bc8c0b6107e5ae6268218f1e07ee092070e1e47b219e0ebf1c94d03ca
    role: context
  - path: pages/traits/morphology/gram_stain.html
    sha256: 893a08295cca1b796d544fbb2acd667ed891c680f119859c2a4a99163355c51a
    role: context
  - path: pages/traits/morphology/gram_variable.html
    sha256: 3a17ee9d0764280eef784b060439993d0c889c62a753f09129e7bef3f98949d2
    role: context
  - path: pages/traits/morphology/green_pigmented.html
    sha256: 09a8825b2df7ba1611c80364482dd6469e55d6f6981d82d4b6d3a0f274248f43
    role: context
  - path: pages/traits/morphology/helical_shaped.html
    sha256: 233ebcff855d07ba2d36efdd9eaaa6e9c52e37aaf95516576be49769dba59e74
    role: context
  - path: pages/traits/morphology/heterocyst.html
    sha256: 31495516fd477dd8dfe0afd9c241333c9419bb4d7a71d89e6abf17219da47175
    role: context
  - path: pages/traits/morphology/holdfast.html
    sha256: 5085f00d707a52e8bcbfde7fb17bc4746f88f7147bb724754347de25ba231ba2
    role: context
  - path: pages/traits/morphology/hormogonium_formation.html
    sha256: 832e80b8e6270c52f4ebb2b6d5fc9a3b9b2f66bcb98d4b9a8340fe1af29d16c8
    role: context
  - path: pages/traits/morphology/intracellular_inclusion.html
    sha256: e63b3fdc1d58d513af5483047513f8e2d8a1f949e83db2cd6c2cc41ef0487d6a
    role: context
  - path: pages/traits/morphology/irregular_shaped.html
    sha256: 44ffa7bc50cb11f49e37301bba9dc71f04efe672c9c5bac6ee11f06b8b48f382
    role: context
  - path: pages/traits/morphology/lateral_flagellation.html
    sha256: 2cfa1b4f04d7616850db25f00b4ca40afecd4dd7bb8de50862bf930449b06895
    role: context
  - path: pages/traits/morphology/lophotrichous.html
    sha256: 0b47ff5a9eb5497d4569500a3dafcca3e2e0cb60e072c775c361fce4153b99c7
    role: context
  - path: pages/traits/morphology/magnetosome.html
    sha256: e7ec916227c9c4c217439dfa997a8f62165fcf2a2b67c5326c940f4f926fa436
    role: context
  - path: pages/traits/morphology/microbial_haustorium_formation.html
    sha256: cd6e2919d8eec51c96ccd4ca3af8614ffbae457dbf61ef2fe7f8529c89660142
    role: context
  - path: pages/traits/morphology/monotrichous.html
    sha256: 92e132afadd758f23a6c8aabe1fbb946feae1d7ed9b794e7679292e5d554ee44
    role: context
  - path: pages/traits/morphology/motile.html
    sha256: 494f516051232b91400ef9bbeb12cd83b6dc2ce262419b92f24546d7a58df08c
    role: context
  - path: pages/traits/morphology/motility.html
    sha256: 01c4926a1884d9f26ed307271ecec9aa07a1ede852e43068740334ec50314747
    role: context
  - path: pages/traits/morphology/mycelial_growth.html
    sha256: eb84a88e9f5d156657152a3c3a071a343ead487d26daeea501de7b827cb39628
    role: context
  - path: pages/traits/morphology/necridium_formation.html
    sha256: 232c2d8122ea860ab521826523187752e3b14e8f8265ab3fef09a7790045d334
    role: context
  - path: pages/traits/morphology/non_motile.html
    sha256: 6554a011f12dd6e60a44bbd3d0dd2c936ec62624d51145c4a6788a0024f77a2e
    role: context
  - path: pages/traits/morphology/non_spore_forming.html
    sha256: 595023884b9e97d1c286114a5982689b337c3631c2ed53ea024f6ec09ac94f36
    role: context
  - path: pages/traits/morphology/orange_pigmented.html
    sha256: 07b67bb0119130863c6aaf018d81dc8cbbba496833c8cff7aa1bad6c24704453
    role: context
  - path: pages/traits/morphology/oval_shaped.html
    sha256: b6bcb17026eedd37325db96f48a32eb617bc224dd19cbe29d93c685f3a9e4116
    role: context
  - path: pages/traits/morphology/ovoid_shaped.html
    sha256: 83549fc844b021c069a9bf9bcb36352d5f060f6d557ab2c454b66856a2b8d167
    role: context
  - path: pages/traits/morphology/palmelloid_formation.html
    sha256: 4c290d8067609a36fead5cd7ff65e079aa7e7c954d99236610e37282c84c981f
    role: context
  - path: pages/traits/morphology/peritrichous.html
    sha256: ca5337e5664f5603d5f5154fd52dd1f8ec47c49578dc1ee310f43bd13f891479
    role: context
  - path: pages/traits/morphology/pigmentation.html
    sha256: c6f3f0ecdde1e50d8a9da9d12c7b7d2e4ff2be9880b24e845a0c7fa7dc4f5f00
    role: context
  - path: pages/traits/morphology/pink_pigmented.html
    sha256: 52b1a7bf747a94f237eeb58898a37fa68b5c191340c2803d5554acd5d2d805a1
    role: context
  - path: pages/traits/morphology/pleomorphic_shaped.html
    sha256: d205a470bab87a95ac717bd1809a373b371c620d66e449d6787dbc9ab5c41e3f
    role: context
  - path: pages/traits/morphology/polar_flagellation.html
    sha256: 6ea06cd81c78ac97db6017fc9c54b6e35e32cade085326e16d2a683a09baf95a
    role: context
  - path: pages/traits/morphology/polyhydroxyalkanoate_granule.html
    sha256: ff5bd64ee90b58d4f805ceb73c748382192ece38bcc7e39bfdac59645013e4e9
    role: context
  - path: pages/traits/morphology/polyphosphate_granule.html
    sha256: 325f64bb9da6fefe11798e12afc0cde962c15e2cbbaf44ab28b54e141135a415
    role: context
  - path: pages/traits/morphology/polytrichous_flagellation.html
    sha256: 465ce067e49a28e55357821a4bf0c87700fd84a684943317fdbd57472ff2bb5c
    role: context
  - path: pages/traits/morphology/prosthecate.html
    sha256: bf0bdcb81cd4a83d03f0cbe7d8b4c09a972e039f07d8378add733cbba0aace47
    role: context
  - path: pages/traits/morphology/pseudohyphal_growth.html
    sha256: 1ed7bb6f39db818fcb67fb5b04d50b39015e7d4e423691e87fc5ed470f797bc9
    role: context
  - path: pages/traits/morphology/red_pigmented.html
    sha256: bd14afe8a438ecc61ce8287d36296dd395a6f07bf5f49537bbe9a2003f3412ec
    role: context
  - path: pages/traits/morphology/ring_shaped.html
    sha256: b10ec1cce1218eee4e7235a7bcd9b1ce789f66b847f2b277686b1c50900eb21a
    role: context
  - path: pages/traits/morphology/rod_shaped.html
    sha256: 43503767a64995801f9021837bb698a5154ce0de857ec3f36a4ce18b6470439b
    role: context
  - path: pages/traits/morphology/rosette_cell_arrangement.html
    sha256: b9bcd62b9d395551f0d6587b9a239e4126252e4945bbbd50511cc6d6e335f4db
    role: context
  - path: pages/traits/morphology/s_layer.html
    sha256: bbaceb184822903bb418d872152bfca8067620bb98da40abc508cfbe65e9013e
    role: context
  - path: pages/traits/morphology/sarcina_arrangement.html
    sha256: 5a63516213736c01c86d9ddb997b95b9bbd0302cc12b9c2516145c222c40b403
    role: context
  - path: pages/traits/morphology/sphere_shaped.html
    sha256: 6c9b46431c1ee5a49e6f8d37722d32edc318e435cbbcc64ab575538990bdd499
    role: context
  - path: pages/traits/morphology/spindle_shaped.html
    sha256: 508f5fcd9256d7b97be57c61e7cf16b223f73ef5ad730b023d000d64684d61eb
    role: context
  - path: pages/traits/morphology/spiral_shaped.html
    sha256: e928bfb29b406ba7a5126ab66afd9186272fdd678f8f65c00015ad9548cf0302
    role: context
  - path: pages/traits/morphology/spirochete_shaped.html
    sha256: 9a368861de63547ae134a69c0148a19f7d31b4510f7a08b46389bed04e7dc7b3
    role: context
  - path: pages/traits/morphology/spore_forming.html
    sha256: 3fbd6c4755e7ea5b02cc3ab7d1829546f7d390cd80e07a418152b7f3c3b9aaab
    role: context
  - path: pages/traits/morphology/spore_shaped.html
    sha256: 7e5ab0921fd3067d6d74d3aa5b59e0595ad49bb2d0df3651bce5cc2005221e3e
    role: context
  - path: pages/traits/morphology/sporulation.html
    sha256: 0819c87abfe6bb768cc6be2cadf5460dbb5f85a81fd61c4c99589e569e77a02c
    role: context
  - path: pages/traits/morphology/square_shaped.html
    sha256: 53eb75a4f50697ec2bd4d7d01e511ad233e2b0c6ff2dc418436ed6de5c4c95c4
    role: context
  - path: pages/traits/morphology/staphylococcus_arrangement.html
    sha256: 1188c00d06ecaae207ad6ffb34129c179addf98e87e746b76d4f7c9e2284d2ff
    role: context
  - path: pages/traits/morphology/star_shaped.html
    sha256: b12c3af9fe079ca6b999c7339f09cfaff354fc2bba4b56637ea636a9ccfed105
    role: context
  - path: pages/traits/morphology/streptococcus_arrangement.html
    sha256: 05b85b179fefbacf79ad33a8168670da2bf873220a4d2c12130320256931e9ff
    role: context
  - path: pages/traits/morphology/subpolar_flagellation.html
    sha256: 5e43427b9bfd048247ec576fc34688e1adbca4fcd553b3be283595aaeeafcfe0
    role: context
  - path: pages/traits/morphology/sulfur_globule.html
    sha256: 68b876ebd8cb82bf0195d3971d7a7cfdbd0d6e2c28436ce3a2283bf93771ebc1
    role: context
  - path: pages/traits/morphology/swarming_motility.html
    sha256: 171ca0d0282fe63ac7435dcd4650408c0547a732e0c7eb8a19b7bfbe951058f2
    role: context
  - path: pages/traits/morphology/swimming_motility.html
    sha256: b8490274983af875adf9280804b0deb4f497777054d4b21fcd3e177025cea45f
    role: context
  - path: pages/traits/morphology/synnema_formation.html
    sha256: 2a30b987df564a6b1ae014819b1090b8fa1676f285b3dd4af611de8626429e88
    role: context
  - path: pages/traits/morphology/tailed_shaped.html
    sha256: 35cc628cc8a9e098d4c5916ff9af71985375957eafb185b4c0631aa2158479fe
    role: context
  - path: pages/traits/morphology/tetrad_arrangement.html
    sha256: 140bcd1fd3123f9a12bb1aef9efbac891df263a8ba5401b8c472fbcf9049a8df
    role: context
  - path: pages/traits/morphology/triangular_shaped.html
    sha256: 29ab6e099157cbb7e1532e2f97e9b73a69e17827912467c2a9eb5d3fefa2c944
    role: context
  - path: pages/traits/morphology/twitching_motility.html
    sha256: e0453d23ea9f71179181ca5be1d1ceb285d1c521aabc71b589ea0b5abbe11f41
    role: context
  - path: pages/traits/morphology/type_iv_pilus.html
    sha256: 994af87767a1c4a77df60d2b675999af20273616ee40b7adad4e080a1aba8a5c
    role: context
  - path: pages/traits/morphology/vibrio_shaped.html
    sha256: d8c40df7c0cfade73a5d64c1ece34d765a0f9b9dc65306bf6d08fd62417ab128
    role: context
  - path: pages/traits/morphology/white_pigmented.html
    sha256: 5356af29510430fdc4404350dd9864dd6267f1c675206220349c5bc9c69fe0f5
    role: context
  - path: pages/traits/morphology/yellow_pigmented.html
    sha256: f3b7af2da3481d4cf267ee4bb465fd7268c3d1aebf2dbf0737688bcbf4f3d281
    role: context
  - path: pages/traits/observation/growth_nacl_observation.html
    sha256: 49073c91c3caeb7937d6b5df72209230c68271129682f1126d01b1dbd5d76b00
    role: context
  - path: pages/traits/observation/growth_oxygen_observation.html
    sha256: 12f7257a0c7e31c525cbacecdc6482052a85f83801029db341371acd73f20205
    role: context
  - path: pages/traits/observation/growth_ph_observation.html
    sha256: 6b5ce59815ae1e274ce446f0c68259b461a868e30b5742dd4e16e1d9a7151442
    role: context
  - path: pages/traits/observation/growth_temperature_observation.html
    sha256: 3af823797c70c0e2352bb5893ce56885a3a946a6a1eb36d5d18ac3310295683f
    role: context
  - path: pages/traits/observation/nacl_delta_observation.html
    sha256: 3eb7218fbeb5f36ce375e72a210199f432512e2c15fb8c578b11ec41b402dfd0
    role: context
  - path: pages/traits/observation/nacl_observation.html
    sha256: 998ef9e1d230cccaf76b7755230bc50a9c565f58b1ec159c01a7cdea11202e53
    role: context
  - path: pages/traits/observation/nacl_range_observation.html
    sha256: 8b8b0c31e548cc0a74c5ccd0193a259e245f88d5fdab8d46224b36eb3e0120e9
    role: context
  - path: pages/traits/observation/optimum_nacl_observation.html
    sha256: 282787b21b0d6b70c1571f5c01e741fc98d713bd2a34e88b3a462cd39920a05e
    role: context
  - path: pages/traits/observation/optimum_oxygen_observation.html
    sha256: 6aba542586a91ae055e9cb017aec071d1ba256c08b144fd1e603bc504afcce68
    role: context
  - path: pages/traits/observation/optimum_ph_observation.html
    sha256: f24016060bdbb2f22feb48ae118ab7ed7bfc5ec735548b56c4b0080ccdb43042
    role: context
  - path: pages/traits/observation/optimum_temperature_observation.html
    sha256: 7943d5367b76eb8bbe896afb5b3145816f70eba74eb47fa3e24c1cc07f28c729
    role: context
  - path: pages/traits/observation/oxygen_delta_observation.html
    sha256: c8b3e9083d8fe52ab06d8034927827893c2b37a128e9d05ad6348987b4e4d8e9
    role: context
  - path: pages/traits/observation/oxygen_observation.html
    sha256: f2d9c6829f6caedc3a09728fa3b5dea9547fc4a7bbd1ab6f45b28a7bf79f1adc
    role: context
  - path: pages/traits/observation/oxygen_range_observation.html
    sha256: 75e9bbedd51226156e7be43c9bad06843e8112b5195935bb0d644f16c0fd18a3
    role: context
  - path: pages/traits/observation/ph_delta_observation.html
    sha256: 9089cd497222162732fa9ca0015c59f2e3fc1d662cfeaac93eefc9769b55b34c
    role: context
  - path: pages/traits/observation/ph_observation.html
    sha256: 04c9f20434baedebadda6c6eabacfad116b071d2125a1a576785583e24ed6a44
    role: context
  - path: pages/traits/observation/ph_range_observation.html
    sha256: 2bdd2df06e24fd244bfce451d66792cabad4ed8c94e3248669a0cf962b0927fd
    role: context
  - path: pages/traits/observation/temperature_delta_observation.html
    sha256: 6574878e491bd697a499a2aab0ccd7d9c7861834c28831b71123e9c54ebf0d3c
    role: context
  - path: pages/traits/observation/temperature_observation.html
    sha256: 31a3abae8f83697efdd4136d4dbcf8f638f32f4f726672a66254e2f8e813c71e
    role: context
  - path: pages/traits/observation/temperature_range_observation.html
    sha256: 2dac24987b3f62df621a96a627c21af25202286b8ae3473448787d037865c4fb
    role: context
  - path: pages/traits/other/catalase_negative.html
    sha256: 05ef6d409445f881adb093d34010693071f61c9af1c8e3100e834f4459fe8def
    role: context
  - path: pages/traits/other/catalase_test.html
    sha256: b2e9b3e3d41e55c1105ada6e0536158951846eba5d01dabca53d483833e130ea
    role: context
  - path: pages/traits/other/circular_colony.html
    sha256: 2af761eba8cf6e4625bf891ddc6a06e99c92259f1251ee53c6ade2ef575ef56a
    role: context
  - path: pages/traits/other/coagulase_negative.html
    sha256: 2cb7c3e4e7b4e5944eb73bdaf8c3bfd5255840883e85deab12541ad7e64966bf
    role: context
  - path: pages/traits/other/coagulase_positive.html
    sha256: e243b0ed3ace62ea1bfd44d3f18c427ffa70c99a0e147ce94ef85343faeb5b5d
    role: context
  - path: pages/traits/other/colony_morphology.html
    sha256: 7437a90cb713cb4645cbc3a249ca859ea48e1d66d43069823f4d1c6a7663a07a
    role: context
  - path: pages/traits/other/colony_shape.html
    sha256: f76128d5983d1c6c0ef89c469d14d4be07a9a5db27b359846ad1dd37b1ac48f7
    role: context
  - path: pages/traits/other/epibiont_phenotype.html
    sha256: 472fcca4cb9d4fa04c7c953032cec1cf6acc3e097eba5c231e033ee4dba82bd7
    role: context
  - path: pages/traits/other/filamentous_colony.html
    sha256: 1696913fa3f9370cf7fa53e8f0efefa9ee0b2027cfa66b07102152c3f6b6254a
    role: context
  - path: pages/traits/other/fried_egg_shaped_colony.html
    sha256: 77d863bf1e7d498ad564dff46efacaabbe70cedbb884bd726d8164ad046ea11f
    role: context
  - path: pages/traits/other/generalist.html
    sha256: da2fe33573c3f83a7a67df35c919eda511f63ece958bf2bb8881144d49f1e6b3
    role: context
  - path: pages/traits/other/hemolysis.html
    sha256: b131354cab35a7d557c6a4149bba8c82b7416d94a962cb1817415f254e28cbfc
    role: context
  - path: pages/traits/other/hemolytic.html
    sha256: cb0d8c9429ec7a61a30d917791d04663905fdf726c70b7aacc40c51d9aac3b05
    role: context
  - path: pages/traits/other/indole_test.html
    sha256: f8741db8a922182cdb4fb9319c7dd14bedf47b6a35ad7892b6c5df0293efb2f0
    role: context
  - path: pages/traits/other/indole_test_negative.html
    sha256: 398e2672be7b8e536f8de7551507eebb8d1c48235222f2a4cce54fd2fbbb2182
    role: context
  - path: pages/traits/other/indole_test_positive.html
    sha256: 3a39a98232c2d917b790cf9457c0744c5b15b0fe00c468ec076b287e69446b6a
    role: context
  - path: pages/traits/other/irregular_colony.html
    sha256: c7d9ba3141032fc70396154511cce0395b2859dcba96cbf68a49b2e15267bfc1
    role: context
  - path: pages/traits/other/methyl_red_test.html
    sha256: cfcf604939480bd6bf1ba6514891ccc5c33c04de681e8147ee72deda0d1df030
    role: context
  - path: pages/traits/other/methyl_red_test_negative.html
    sha256: 753055cc6da00531916dbe27e30a97b9559da92b8e6608f8b4187c59cda1fc0e
    role: context
  - path: pages/traits/other/methyl_red_test_positive.html
    sha256: c7b3e66a3c931d9d6e7c62a0ab65bb3c5c1fc49ab6e7024ebc1cf86e61573844
    role: context
  - path: pages/traits/other/non_hemolytic.html
    sha256: 43bf23b4effe589ba3920a2eccedc4b95690c8a80007a5881c54968e0044c258
    role: context
  - path: pages/traits/other/osmotic_tolerance.html
    sha256: b3cfb4ae8db0bffc41576c008e03ff6455c5d439a93dfd00f1419ddb945305f6
    role: context
  - path: pages/traits/other/oxidase_negative.html
    sha256: b301fc75fc6ad238c0490ce65989318c98fd5d09bdd7d4037c0b4b5aeae30978
    role: context
  - path: pages/traits/other/oxidase_test.html
    sha256: 7e6e40e502e3eaa4c3d53fe0341f8366feef88d37f8394158df310728608d3d2
    role: context
  - path: pages/traits/other/punctiform_colony.html
    sha256: db0476d0066efcea45a7cf654c114ecaf30ba853ebc9a00c6e0e49bca12fe23a
    role: context
  - path: pages/traits/other/rhizoid_colony.html
    sha256: 5e906808c5f40705e82332c183886955de51f0a8e9dce9a05e985a9a5678043b
    role: context
  - path: pages/traits/other/specialist.html
    sha256: 98964ef771d654cb659bf577729ca13461c26c32fb9d3c67f9f07220317be4f2
    role: context
  - path: pages/traits/other/urease_negative.html
    sha256: 82081b60eccd26cbf0eb16aa6610bfa12b3eece12f0bad8a7dc3208f89da171e
    role: context
  - path: pages/traits/other/urease_test.html
    sha256: 947b38a9dd3341a055b92e1df9f526bd014ec6ef29401015400a56f94aa052eb
    role: context
  - path: pages/traits/other/voges_proskauer_test.html
    sha256: d8ab685727e70cf7637ad30f0405b7b788b31d7f8f47b652da760df0778439e8
    role: context
  - path: pages/traits/other/voges_proskauer_test_negative.html
    sha256: e319736bbf138fa7b891fffcb9013b89806358a9fc6b3b88cea3aaddaeffa340
    role: context
  - path: pages/traits/other/voges_proskauer_test_positive.html
    sha256: f337ec917c8257dd9667fb157be86bfdb6d94f62e92fa59036cbbf0dabe183ea
    role: context
  - path: pages/traits/physiology/acid_phosphatase_activity.html
    sha256: 48157067f2beb33c6694a67e261b642e097ec7fa1ccd4df91f56a4d4ef0369e3
    role: context
  - path: pages/traits/physiology/acquired_stress_resistance_memory.html
    sha256: 51c7c4095559932744db5747fafdce685aaac43a294ab35c961602a6b70f8a57
    role: context
  - path: pages/traits/physiology/aerobic_anoxygenic_phototrophy.html
    sha256: 8b40c6418bd2b523d6c0cf0fdc11a7840514a7f1b6a5d48ff3a9e6c52a8675f3
    role: context
  - path: pages/traits/physiology/aerobic_overflow_metabolism.html
    sha256: c777972ec44bff21e8cc90f411b4639a13c8accb36d876ea98b9aab7f7bb6dab
    role: context
  - path: pages/traits/physiology/aerotaxis.html
    sha256: 3d50a12a6d97b44914109293ff6893bfbc31072838ab6736738dc72abebbff6e
    role: context
  - path: pages/traits/physiology/aerotropism.html
    sha256: d128a580625e2668b85bb5561a7dd0f8230b42e5519e85426daf7d0a390434d5
    role: context
  - path: pages/traits/physiology/aggrephagy.html
    sha256: bd262a0d1c5f856d65a965efb37258a363e63879197f78ca19f81c9c2cc85b92
    role: context
  - path: pages/traits/physiology/alanine_arylamidase_activity.html
    sha256: 34d002b9e15468b0c192797fdc3100e05a3ae7f10adb8df0ab351e6e44c0a809
    role: context
  - path: pages/traits/physiology/alkaline_phosphatase_activity.html
    sha256: 5e06588a29957f2977679fd0ccee2332cd86a23e16bb6997d3a6dbcccadc3431
    role: context
  - path: pages/traits/physiology/alpha_chymotrypsin_activity.html
    sha256: 6cb3787363dad0322af9d9f77ab9eed268d55a6824da4431331089302fca4066
    role: context
  - path: pages/traits/physiology/alpha_fucosidase_activity.html
    sha256: f46628140e714c692ea3902aebf9db87f29d955678e02af05655086c796ab0fc
    role: context
  - path: pages/traits/physiology/alpha_galactosidase_activity.html
    sha256: e3e55b50f9f73f2676fbd1812dfbc7183d9863dd6b4cdb39f91b15e1e96e94dc
    role: context
  - path: pages/traits/physiology/alpha_glucosidase_activity.html
    sha256: f02c594f85572320f73e20a053887bea27c1d586d3f6f9bbd326b46893c5124f
    role: context
  - path: pages/traits/physiology/alpha_mannosidase_activity.html
    sha256: 671e1a05c15cfd04e0da15456c8df60b97c9dd57e3ef94ebe10ce92865a6797b
    role: context
  - path: pages/traits/physiology/amylase_activity.html
    sha256: a1963f01c785f21a3f1ca9ebf9174d0b9d13363aa3a9feceb9df459b3b6177f6
    role: context
  - path: pages/traits/physiology/anisogamy.html
    sha256: 6bb382d0165e9f5029bd4a0481509e519b0e7e1bf08bb2e8420a5165110ccdc1
    role: context
  - path: pages/traits/physiology/antibiotic_resistance.html
    sha256: 13ecf1eca328e6a1aa5b7a192ca0e5cc8d548ae7b98d74d3da6c0ef783c72f4b
    role: context
  - path: pages/traits/physiology/arginine_arylamidase_activity.html
    sha256: f4ebeb29e11bb5ec92d74c6b6469797b5c1a32f3d48612ffc4074a7ec815f547
    role: context
  - path: pages/traits/physiology/arginine_dihydrolase_activity.html
    sha256: 108c1fe3a829315f30532aa5c1b37ede6de91efafe704193cc5bc3c154426ea4
    role: context
  - path: pages/traits/physiology/autogamy.html
    sha256: c41448be5217b0c8b469422758a48abed9d2b6324103a1dd31876ca9237d0060
    role: context
  - path: pages/traits/physiology/automixis.html
    sha256: 6465a3bb16dd617a9d08e6f0c9b3349b2e44f588f21e32fcda2a3435a63e4239
    role: context
  - path: pages/traits/physiology/autophagic_glycogen_degradation.html
    sha256: 66921a985529649a2f3b7334a1951a2fda3d32fed8b4dc9338e758e0da83d727
    role: context
  - path: pages/traits/physiology/autophagy.html
    sha256: f692a5f9d6f0adf983eed036154e29727d9e87446a917ba2e295291b542253a6
    role: context
  - path: pages/traits/physiology/autotrophic.html
    sha256: fc9bd9101fe0cb9cbd1ec3ad023bbfc557f14711dd52acad1ab95cfe8e75184e
    role: context
  - path: pages/traits/physiology/bacteriocin_production.html
    sha256: ee2e82c4e0e6ba10754f233d44a121b3a67a157250f1c34581dc122f34081656
    role: context
  - path: pages/traits/physiology/ballistospore_discharge.html
    sha256: 3c9b4c6a65c58b633e136fb8d9c804863b8c468965e7a864fdfeafc776fc569f
    role: context
  - path: pages/traits/physiology/beta_galactosidase_activity.html
    sha256: 123f8b3b356c850f3d516cd620e41ca7d74cbca4d8d50254e85b18bb5b6459fa
    role: context
  - path: pages/traits/physiology/beta_glucosidase_activity.html
    sha256: cbf0170860a7d1f50334ffe3f00142b6854762796649e2bae046acee1f5c8e9b
    role: context
  - path: pages/traits/physiology/beta_glucuronidase_activity.html
    sha256: bcd67d55c1b8db65af160538fc7b92b8846bba671019b8e16e33b5e5a0601a92
    role: context
  - path: pages/traits/physiology/beta_n_acetylhexosaminidase_activity.html
    sha256: fcd2777a7ed85e48e213b71a320be84a372bec07106a0fcfdea65051262a23cb
    role: context
  - path: pages/traits/physiology/bioluminescence.html
    sha256: 14405b27792f2d68d2c317e45b78a25698914a31950f8ffb748ee0f6cf0e9009
    role: context
  - path: pages/traits/physiology/biomineralization.html
    sha256: 87a48db908d5f58d84aca9ecd874f00cd7df121b19c3f618d7475e7e2d0c68ac
    role: context
  - path: pages/traits/physiology/bipolar_mating_system.html
    sha256: 81727a0fe6a3848df2b3a98453da2005a2654481ff9c51d9ea897133e7faf214
    role: context
  - path: pages/traits/physiology/carbon_source_memory.html
    sha256: 4d07515c16ff3522aabed2491e94c4b4b1e9d865e6f6ea87c06258be3ce47d91
    role: context
  - path: pages/traits/physiology/carboxydotrophic.html
    sha256: 74f1a38dad6a44f8473a6f406f39a93e1edc622f679998b7ef315fed8b6c1bd6
    role: context
  - path: pages/traits/physiology/carboxylesterase_activity.html
    sha256: 5703094f004ca14c11e5f44d05490673bf7d6a24312f30a9ca3716e0d543538b
    role: context
  - path: pages/traits/physiology/caseinase_activity.html
    sha256: b991aa156bad9e83b8e83c722a1e117d23ea94f8dcd2a4a60b94d9aef7031e73
    role: context
  - path: pages/traits/physiology/catalase_activity.html
    sha256: 21070d2aeaf9be12199f01b8aab865bccdaf700d00922b6d4790e6f54062f6c8
    role: context
  - path: pages/traits/physiology/cellular_buoyancy.html
    sha256: 19081e9b3d251effdf3557605845e80e87249b4089a9a02907c77bc697059e06
    role: context
  - path: pages/traits/physiology/cellular_rejuvenation.html
    sha256: 6e81533bdb830b65e9191ad1a2984d54c2f4256f6b6cd6bfc8cdaf8a372ed49c
    role: context
  - path: pages/traits/physiology/chemoautolithotrophic.html
    sha256: 62f2b2aeee868dda20f79e92a41443fd06dd52df06bb269a19d6d4e812901158
    role: context
  - path: pages/traits/physiology/chemoautotrophic.html
    sha256: e46522ee0d369c61fc1c9e637ebbc81103d8cd6f1d16452574bb5c198bb6f6c5
    role: context
  - path: pages/traits/physiology/chemoheterotrophic.html
    sha256: afea6b0fe93b5092b92f340b9fb41821bf1070393e1d2b9eb41f5f101d7f649a
    role: context
  - path: pages/traits/physiology/chemokinesis.html
    sha256: 318b30cbc3e7c8000c8b2d01ed2be70d99aedf3c398dca6e3001310f83b6506d
    role: context
  - path: pages/traits/physiology/chemolithoautotrophic.html
    sha256: ba784d48b568f0d487df4ab7ff0ca02cc03975b2a492893c11b17c08c008426c
    role: context
  - path: pages/traits/physiology/chemolithoheterotrophic.html
    sha256: b69ea123248d1fbb45ed7e2f197918f5fced54e0bdc1a4e6c5c2d43260583552
    role: context
  - path: pages/traits/physiology/chemolithotrophic.html
    sha256: f81bba49c318614a1bd0c98a3f5f5aecdfda75692a51fd002ad3e50e30bb6ac0
    role: context
  - path: pages/traits/physiology/chemoorganoheterotrophic.html
    sha256: 6e582a61d43f5dc2f8e0c3fe1b04271637f1b0fb0b33220d2f44b960558b86fc
    role: context
  - path: pages/traits/physiology/chemoorganotrophic.html
    sha256: d687df87c73fbb27fc416c5cb5e406a7f3605c067d2e3f49c95d4ab56ba1060a
    role: context
  - path: pages/traits/physiology/chemotaxis.html
    sha256: e4d8b9c19e0f55c618b6eb7aefec80ae3af3a116c9ab9bc0aa1955f721303035
    role: context
  - path: pages/traits/physiology/chemotrophic.html
    sha256: f1dd7fa63d9bc4f8512883edcf4fc535f4a28d40792a7b94c75965ec3c298812
    role: context
  - path: pages/traits/physiology/chemotropism.html
    sha256: 8082b14a154192a6501cd8938daf1ebdc7e164d1b008524269242814f8131330
    role: context
  - path: pages/traits/physiology/coagulase_activity.html
    sha256: 686bcb5680511c8ae4a84b64d5c507d369163298b09e6f2ff7eb18986b2fc1b0
    role: context
  - path: pages/traits/physiology/coccolith_production.html
    sha256: 7c491e6033dab7e2e981dbf87fbb875b5d2b3a238fc68553e7db069a0b37b48b
    role: context
  - path: pages/traits/physiology/cold_shock_response.html
    sha256: fe55617f3a03edf13aef6a91fb8d624e2fc23989a0a89129487f932a9804ea47
    role: context
  - path: pages/traits/physiology/contact_dependent_outer_membrane_exchange.html
    sha256: 511626d442766d9a2c6b292e1b3892cd5bd5116219927ec69fc73fcbf84a05ae
    role: context
  - path: pages/traits/physiology/copiotrophic.html
    sha256: e3685269a3e745609bc591970f2c4d016b93adbc638ad55919abac1f2f837211
    role: context
  - path: pages/traits/physiology/cue_triggered_environmental_anticipation.html
    sha256: 08ab4e9f67fea521ca6d1f52afcfbc7d044c94ee0018edb565b27d70d2c41fdd
    role: context
  - path: pages/traits/physiology/cystine_arylamidase_activity.html
    sha256: d559a35a96d8b38608b436c92e1d0a509f79f29abb4d2802a7d4f5a63727fc51
    role: context
  - path: pages/traits/physiology/cytogamy.html
    sha256: dfe94434926b5a17c65ff7b03af5d2a0d809ea1eeb5710de47fafb02b8118623
    role: context
  - path: pages/traits/physiology/diatom_frustule_production.html
    sha256: f32510b1ad237d1b5ef563be993040406c672d98200dfa7ce4c94cbeb2156edb
    role: context
  - path: pages/traits/physiology/diatom_perizonium_production.html
    sha256: 18b8f6c50f85b67a3d8bb9d335b821090e1841ef9f5c89016312df364cd9820f
    role: context
  - path: pages/traits/physiology/diatom_seta_production.html
    sha256: 249633babb308eb636aaf9ffa2edd59b3d43968e4736721fb12c5be925459e3d
    role: context
  - path: pages/traits/physiology/diauxic_growth.html
    sha256: a8a3fd719dd665e62ff10d9a755f471369af8cf74d140de06e8866208854c7e9
    role: context
  - path: pages/traits/physiology/diversifying_bet_hedging.html
    sha256: 8f0e831ee36da2c0a6440c88e1bc4c20805767e30a662755a7c1fc91cd20c220
    role: context
  - path: pages/traits/physiology/dnase_activity.html
    sha256: a3193f4298c393475164dbc694bede401044551cee496e423631afe75b3b23c5
    role: context
  - path: pages/traits/physiology/dormancy.html
    sha256: a57be4792faa5bc001c2c8c10126346f71802e5ec49037418cd6b1eb2635c86e
    role: context
  - path: pages/traits/physiology/durotaxis.html
    sha256: d1877c67f6893877592fa2aa8b46db090b0017a3062058df8238bbc49744f0e9
    role: context
  - path: pages/traits/physiology/endocytosis.html
    sha256: efeb3fa3171c4673d07fe7da17a81457d08d49d5c14b27ee5c03e0342cf3ccb8
    role: context
  - path: pages/traits/physiology/energy_taxis.html
    sha256: f3e793eaa62e38ed079271b785225b3de860b915f95f9adf4e0fcecebcd66187
    role: context
  - path: pages/traits/physiology/enhanced_transcriptional_reactivation_memory.html
    sha256: 53f1d604c25c26b993e0e93b72ac39b14a05b9ce34d89c1730c561720c3c5509
    role: context
  - path: pages/traits/physiology/er_phagy.html
    sha256: 41edf5bed4f259473d292ad60e97425f51f0eb48f604ec80b90ca3ea2196f841
    role: context
  - path: pages/traits/physiology/exocytosis.html
    sha256: 044e553c961b57120aabe97a59039ed5b67fac184d774c0607969605086d5c45
    role: context
  - path: pages/traits/physiology/extracellular_membrane_vesicle_production.html
    sha256: 0da0ff700f3aa84c51a25712f146e0d1beff7314a354d7f434cc9a69e14a611c
    role: context
  - path: pages/traits/physiology/galvanotaxis.html
    sha256: bcb4dcc31e1f0d0294df3d9c17efd494b91f5246a64cfd342ba4b17f6c8394b9
    role: context
  - path: pages/traits/physiology/galvanotropism.html
    sha256: aa809161530a470d05f04e8ae8d1bc03d8dc8aad5d459b8babecdf72963dc740
    role: context
  - path: pages/traits/physiology/gamma_glutamyltransferase_activity.html
    sha256: d572195b7e3c99b2c37f7d957384a29331d3c0c855cb06a2c76484f862cd45fd
    role: context
  - path: pages/traits/physiology/gelatinase_activity.html
    sha256: 20be9d3e80db36d46658b985e95e2deb3e9ba6d8e99669e6026947485f39b9df
    role: context
  - path: pages/traits/physiology/glutamyl_glutamic_acid_arylamidase_activity.html
    sha256: a9c1ef7e1f6bb7d05d68bb7b131159e5f4b278378d05179a45e6a5a9559da6e9
    role: context
  - path: pages/traits/physiology/glycine_arylamidase_activity.html
    sha256: e09f5e955a0881d11b08f93b48f2893bd58e2c2b2b12b0190eb45b7f250a95af
    role: context
  - path: pages/traits/physiology/gravikinesis.html
    sha256: 729623295558198afd04f28d03e9e2dc9bee424bbabbdd82221b2ed1e87663e2
    role: context
  - path: pages/traits/physiology/gravitaxis.html
    sha256: 1eca70945224ef33adb5924b834ce731174a161131fc98d6c566737ead76f3be
    role: context
  - path: pages/traits/physiology/gravitropism.html
    sha256: 23cca03adb60cd82cb89bac5fa859f99abde5499ab2609680a132dbcdef34d9a
    role: context
  - path: pages/traits/physiology/gyrotaxis.html
    sha256: 2ba15f1e9de60d8dfca6ee0431ae3cc6f3eb1ea6b9d2d94632e3ca6c4fe43767
    role: context
  - path: pages/traits/physiology/haptocyst_discharge.html
    sha256: 6979fc686d3d5832d68178bde44eb567876dca6d0f6cd176bdf1da7037d829b0
    role: context
  - path: pages/traits/physiology/heat_shock_response.html
    sha256: 527157a8fced03d9ae5b7933a23417383532be59de31ee05b776177ee9ddccac
    role: context
  - path: pages/traits/physiology/heterokaryon_incompatibility.html
    sha256: 969e0ce50d0be439160cd292919484c3ebd36d86035dac73a4a56fdbd3454cb7
    role: context
  - path: pages/traits/physiology/heterothallism.html
    sha256: 62a96fa7428d23d022d051909fc081fa06048b750b45402daa71cbc02562bd64
    role: context
  - path: pages/traits/physiology/heterotrophic.html
    sha256: 484e4cca1a858b861d05c6deaf6fc8af2f15bebe311abdf8ad821503a0757fcb
    role: context
  - path: pages/traits/physiology/histidine_arylamidase_activity.html
    sha256: 21cfb6ae3bdfc5eea88883418d8df7ce62d2db81e7a934f38c5f0fb3715a563b
    role: context
  - path: pages/traits/physiology/homeoviscous_adaptation.html
    sha256: 78c76dd18325126cdc9d792c363316a651305c3333b93e29cc9f00f51cbde8d8
    role: context
  - path: pages/traits/physiology/homothallism.html
    sha256: c1202331d620c68df1911805613b4ad67b573b9a13130b491c780c7824512fa5
    role: context
  - path: pages/traits/physiology/hydrogenotrophic.html
    sha256: e172b6feb46c3c7da6ba7e465db569b4b40fd252a72af662b4918655b6f7d574
    role: context
  - path: pages/traits/physiology/hyphal_anastomosis.html
    sha256: 4021913c8e2fdb50a1b1445f7de9b410b1559cc4d800ab3f8b0fd19a03f1e9e2
    role: context
  - path: pages/traits/physiology/isogamy.html
    sha256: 14f6199a6f50a3cf873bc7f24c04d16d9933c61159f4d0a96c3f42f153ba7cfe
    role: context
  - path: pages/traits/physiology/karyoklepty.html
    sha256: 7a0f2be4cc6934a1cc1ebc7fcb6deef79349b075058f75ccad3342ec5b9c9b57
    role: context
  - path: pages/traits/physiology/kinetocyst_discharge.html
    sha256: 7cd177084a2a2309b0465de68ff1031596eebf64ab6e777c4b8363a577a65e25
    role: context
  - path: pages/traits/physiology/kleptoplasty.html
    sha256: 0fd1d5c855a09d740513621f17b92728a8e8f68c623f7f6a130ba73e5e400cb9
    role: context
  - path: pages/traits/physiology/lecithinase_activity.html
    sha256: 5f5acb0dbffcc639be9a46c88851323e35b0d9372dfcd2970e8232c1e6cc0647
    role: context
  - path: pages/traits/physiology/lethal_algicidal_activity.html
    sha256: 5f9f4680e765a2352545090f2e5fc5319a77da3013247af3716daddaed65f750
    role: context
  - path: pages/traits/physiology/leucine_arylamidase_activity.html
    sha256: dfa8eef29ecf23916a0f00610e8bbeb5cae4cf7da60dd1e1fd863f5af932fa70
    role: context
  - path: pages/traits/physiology/leucyl_glycine_arylamidase_activity.html
    sha256: 61835c34c932196ad5f362a72ca3d6e7803997a2bad06069c4b986971aef644a
    role: context
  - path: pages/traits/physiology/lipase_activity.html
    sha256: 6f052cba45f8a413aaa998b70887a69f4a72d37b429d8dca9a7104bb0162b4c7
    role: context
  - path: pages/traits/physiology/lipophagy.html
    sha256: 45c34c6c47d23a087acb41fbacc8f2b02f5f786af9839ecf3c38e7fba2ca6d41
    role: context
  - path: pages/traits/physiology/lithoautotrophic.html
    sha256: 5032e34e70dd4256a1ab227377fa82582d233a1ae048b4ef4233fa1569cedf30
    role: context
  - path: pages/traits/physiology/lithoheterotrophic.html
    sha256: e0b868895e71a0021252475cd311e56037dff4da9a425799b1c8d4f92f733c76
    role: context
  - path: pages/traits/physiology/lithotrophic.html
    sha256: ec7b651c5e4ef1638177fe98ac7531d4f91d208ce3779b1fbde1e718cd929cdb
    role: context
  - path: pages/traits/physiology/lysine_decarboxylase_activity.html
    sha256: 53096118896033e00c118725295153ff1fd261f59242c85a3161e6df2bb8c519
    role: context
  - path: pages/traits/physiology/macropinocytosis.html
    sha256: 019003b6c0ed32b952527f5eb3358b3f67b4f6eb886e7123b428dc638747a4ee
    role: context
  - path: pages/traits/physiology/magnetotaxis.html
    sha256: 1a25717d3e2184b5870f96c432b2caeaee454b0ba527ee78edfa27d461db7d20
    role: context
  - path: pages/traits/physiology/mating_type_switching.html
    sha256: 8f8e4d8db60c1a3a5705475e5aa751c64a5d3716d4b1ea6e06896ef142ace1c9
    role: context
  - path: pages/traits/physiology/methanotrophic.html
    sha256: c9a5fad5c52b56539876b5f84ed672b6e2aa3fd5b8a45ae3cebcf6e2e52a006f
    role: context
  - path: pages/traits/physiology/methylotrophic.html
    sha256: 016bda44d96e823ec3e431ddf361d3bbd1f2449ec1adc1b759df64fbb8752413
    role: context
  - path: pages/traits/physiology/mitophagy.html
    sha256: 55fd79fe79ba2adab4566e7839386f3c35005a2620d0578d877293733e9f18e3
    role: context
  - path: pages/traits/physiology/mixotrophic.html
    sha256: a8758aa22f7201e756fa2b5b9ecf5093b9ffc2006fde8e009179f7dd307e8291
    role: context
  - path: pages/traits/physiology/mucocyst_discharge.html
    sha256: 711689eba0a9bde03df389ae531f617ee70b4a1051d8f625d344a87ea1efddbb
    role: context
  - path: pages/traits/physiology/myzocytosis.html
    sha256: 7c58159b54ac9285cc48323bc7bda775aa03b976f0c140eb3c8f5cec0892caee
    role: context
  - path: pages/traits/physiology/nad_dependent_alcohol_dehydrogenase_activity.html
    sha256: 2e11fb4f1900710890d3523c7cfb8f8be40a33cf90d09312a763b4f8db989232
    role: context
  - path: pages/traits/physiology/naphthol_as_bi_phosphohydrolase_activity.html
    sha256: ebd0cce3724e505e2dbf3b21975cfdf80987f0fbc57551ee9101d3e087dd273c
    role: context
  - path: pages/traits/physiology/natural_competence.html
    sha256: 37fefdcb7b3a1e0ac5e7f241e1d2168a557fdb9d901ee0771c98f98ecc06db2e
    role: context
  - path: pages/traits/physiology/negative_autotropism.html
    sha256: b24002009a1d57c0d292d53f4276aebe42f675643bf7db7976f87a027132bcc3
    role: context
  - path: pages/traits/physiology/nucleophagy.html
    sha256: 0ae8e981e1bc73f0a2e8b77c2f62924afd28524443cd0089f27302299058fa0f
    role: context
  - path: pages/traits/physiology/nutrient_adaptation.html
    sha256: b9ba9688f105846820eed0e03682c9b1c4383bd452fe342c17fcdd06a1283ef1
    role: context
  - path: pages/traits/physiology/oligotrophic.html
    sha256: b18362e41bdcd67f6e5f62b9b5cab7fc4298e434ffb06b79ad85026397ccb8fe
    role: context
  - path: pages/traits/physiology/oogamy.html
    sha256: 3c7e97cb7eb2be73876d88066cf19ff77663b150ce4951686ea9b0247507dcb6
    role: context
  - path: pages/traits/physiology/organoheterotrophic.html
    sha256: cdc9150d1b15f2b37194e02f13c392c8dd85f098f7e1a29a176a4f81d0460cb4
    role: context
  - path: pages/traits/physiology/organotrophic.html
    sha256: 17cc5bb4310f44bf73e2f860037d3265ad766d360e4833c724bc7ae150e56125
    role: context
  - path: pages/traits/physiology/ornithine_decarboxylase_activity.html
    sha256: c9a25aa654bf0a8d41fec554aaef0f5c25b04601b6590aa6f7b5d1bdfc82ca16
    role: context
  - path: pages/traits/physiology/osmotaxis.html
    sha256: 258a75892d043d7388a856b3de7a98003bc4fadd68e805e4026262dad0d30982
    role: context
  - path: pages/traits/physiology/oxidase_activity.html
    sha256: 307495ae6b6382dfafb1c3dc1db7fdd390b842ddbb12aef0161dc008ce4ce889
    role: context
  - path: pages/traits/physiology/oxidative_stress_response.html
    sha256: 6bf45e46bd24a74e96aca9f9d247e05999d8f21c4cc3b9b00507443a4dfee220
    role: context
  - path: pages/traits/physiology/paedogamy.html
    sha256: 7ba1c517d852d888fa30acc215f00226cc8160217d5ccfbcae5a7493002645c7
    role: context
  - path: pages/traits/physiology/pallium_feeding.html
    sha256: e32a68108abe5a3d1a96ded6c0847dfbd6652eb5a7b71ba2a768913d75587d79
    role: context
  - path: pages/traits/physiology/parasexuality.html
    sha256: 5526070a7237909cb24684de9f48e0136f7ec1a855569cffe33ef93ba6b37e30
    role: context
  - path: pages/traits/physiology/persister_cell_formation.html
    sha256: dbae6d790be79a8c93fd61e2f8312209a5bf2af6f06824047cebef4ee528f248
    role: context
  - path: pages/traits/physiology/pexophagy.html
    sha256: 8f5491c68d1bb38e09dbebde63798198c1dfe216fb3b2aaac026c194bc3fcd70
    role: context
  - path: pages/traits/physiology/ph_taxis.html
    sha256: 527170654d1ead0ed646e96f658bf68909af3e2f27801e141cac1b94a72de88d
    role: context
  - path: pages/traits/physiology/ph_tropism.html
    sha256: 5ae22cbafe829bda2ce29d02a45f9a0abdebc7d9b00d8d9d7ecebf00106bf224
    role: context
  - path: pages/traits/physiology/phagocytosis.html
    sha256: 3162a4caf228a196a7330cb252f0272b0595d637d839d17217221394326fcad3
    role: context
  - path: pages/traits/physiology/phagotrophy.html
    sha256: 7be4c862419c9913486a1f4369143cfc5779e0ed24d278c6857646ba20c16f83
    role: context
  - path: pages/traits/physiology/phenylalanine_arylamidase_activity.html
    sha256: d7f085b778be2ad86668863afee3af77e24c471ddacc48b280442d4fe8656ba9
    role: context
  - path: pages/traits/physiology/photoautotrophic.html
    sha256: 13a8d2278a024c5df23e8e42b2eb95208681ff922baa27a7c2df4b9730c07350
    role: context
  - path: pages/traits/physiology/photoheterotrophic.html
    sha256: fd08a3d712b8a980d325b2ac904ff04591a04b07a3481c3b93d2b73b5c5aac2d
    role: context
  - path: pages/traits/physiology/photokinesis.html
    sha256: f1598e822e606fc4356855fff5dfc93e931b8fe4fbfad7038fce181592f571d6
    role: context
  - path: pages/traits/physiology/photolithoautotrophic.html
    sha256: 5f3334a7d18572d129d97ec57fe9f11fd00ffb416a6cc33c5a76c863cb40f7b1
    role: context
  - path: pages/traits/physiology/photolithotrophic.html
    sha256: a67d89d56698f1c7f339d7f44e944e881ddcf6a8bb59b0ecb1c3ce57b4dd73b4
    role: context
  - path: pages/traits/physiology/photoorganoheterotrophic.html
    sha256: 8c22eac9e89cbfce9d4fa996899cd3c98d9a525b4e00bdff73a489a942346ca8
    role: context
  - path: pages/traits/physiology/phototaxis.html
    sha256: eba48a8be6b38b3b497df4115e0f8e0027d7f1944cf7f2d0dc5bd39a41d0174b
    role: context
  - path: pages/traits/physiology/phototrophic.html
    sha256: 6c6ead3a621e21721917864fa620661a6ebe286b07cee61aac41a161c8cd9338
    role: context
  - path: pages/traits/physiology/phototropism.html
    sha256: a7392ac1f89bc2a2241b3ed36335927ceb08c0092753dbe2d729e826f197be4d
    role: context
  - path: pages/traits/physiology/pinocytosis.html
    sha256: d64612b85a96e22d84eada75af27a310c20de101b94a0ded12336e23add3db7e
    role: context
  - path: pages/traits/physiology/positive_autotropism.html
    sha256: d09dd8df2c3f5eabf0812c0ea2a0580acbfe5806fa6611bcb4850a2db47359cb
    role: context
  - path: pages/traits/physiology/primary_homothallism.html
    sha256: 739ae17b781b61d9813fe6c92931fa9edf45a10020f5a4602eb6b8698112dd6f
    role: context
  - path: pages/traits/physiology/prolyl_aminopeptidase_activity.html
    sha256: 3e579999a953609ec712b5ddc84d7160a6a617624034f131e64679c8d7474e5a
    role: context
  - path: pages/traits/physiology/proteaphagy.html
    sha256: 6ee20b1baead659fac3f58fa15ab9c82efed4b41e198fa0c9b0947d2e7a73397
    role: context
  - path: pages/traits/physiology/pseudobipolar_mating_system.html
    sha256: b1ae96eede0393fc30e6a4b6b1529347406dd40790f1f56720e37937987b08b9
    role: context
  - path: pages/traits/physiology/pseudohomothallism.html
    sha256: 5ad8fb44dab8bd90c2ea34e7ac16333bbfe446196a0adf8349d98426022cf12e
    role: context
  - path: pages/traits/physiology/pyrazinamidase_activity.html
    sha256: ae5a2027ce3999611051279dbe2e418362f621e6e21835cdeda109a3f5a9559b
    role: context
  - path: pages/traits/physiology/pyrrolidonyl_arylamidase_activity.html
    sha256: dcfa2b332b1466b2a77b83b3f09ae1c02659c48e734152108128fb8842470c5c
    role: context
  - path: pages/traits/physiology/quorum_quenching.html
    sha256: b1337511051a2fbef366fcbfc642223229ec731b42e9c9af33e7dc5968f86a1a
    role: context
  - path: pages/traits/physiology/quorum_sensing.html
    sha256: 5a2520a510c29fa93ecd6dc790a8564ee3c824d5786676fcd5d9f117a375ffc4
    role: context
  - path: pages/traits/physiology/rapid_axopodial_contraction.html
    sha256: 8b5de8f573a9813b49d1b1eddf8abf7be85fa581443edd2e6bdd2f50c38067c0
    role: context
  - path: pages/traits/physiology/replicative_aging.html
    sha256: 43e3c97864e6b83b84f3534d8c3cf71a693824f827032f11f832cbe730079297
    role: context
  - path: pages/traits/physiology/rheotaxis.html
    sha256: d26e5a1e2ace361c986934e8b26c62f06c0a8a3d0d8e2fbc94ba60e339517093
    role: context
  - path: pages/traits/physiology/rheotropism.html
    sha256: 9dd170f21154a412668999c0e1719653b0583fe28eb4f34d57ff406cf0d1af85
    role: context
  - path: pages/traits/physiology/ribophagy.html
    sha256: edb4a46e211707c4970a8e48da30db90d4ca34149a64dce40547732b9d391f53
    role: context
  - path: pages/traits/physiology/serine_arylamidase_activity.html
    sha256: 408fdfc1cc056cab6749b4aa76b22be7b67855b713b3b5a0c1eb4f555aa22aa8
    role: context
  - path: pages/traits/physiology/siderophore_production.html
    sha256: e8309a345e0d8589c9653c2a05db26beed9de182f5e3142a83bf0f497493f2cc
    role: context
  - path: pages/traits/physiology/siliceous_scale_production.html
    sha256: 997892699314281276e3a50172d5204f64b71c464b9cca080c59e04eed8489b2
    role: context
  - path: pages/traits/physiology/sos_response.html
    sha256: 003c7f69567eb27d442093705fbdfadfbf9f916ccf6e1478fb741a4545969711
    role: context
  - path: pages/traits/physiology/spore_germination.html
    sha256: b729f0853cb2f0a363773c1a47170eaa1ad3ef58c4a2673bc9ed38ced98279b2
    role: context
  - path: pages/traits/physiology/stress_response.html
    sha256: 6669e30453fe20b2d1b12d14a7e99af64066be94ea99b33babe3c3db7440a11a
    role: context
  - path: pages/traits/physiology/tetrapolar_mating_system.html
    sha256: d00206a16177fc0f8ea15391106ce7b9f86fa634b0a2bcedd8143cb79c5a8aac
    role: context
  - path: pages/traits/physiology/thermotaxis.html
    sha256: 02cc6506cd4a676d06846df60fe21335ee6cf1611370871dc443c824bf7a4e55
    role: context
  - path: pages/traits/physiology/thigmotropism.html
    sha256: 2fb3f8e5e22977a6fe55372633d9de78105ff779b9eecf635c055a833bf5c6b6
    role: context
  - path: pages/traits/physiology/toxicyst_discharge.html
    sha256: d9cdc9f2dfba8aa774d62ceadc1ef5b9713b954fa9868308fb45dfda731ce975
    role: context
  - path: pages/traits/physiology/trichocyst_discharge.html
    sha256: 7c7d7fdbfecf1286ec0ea2a3d02170f18766edde75e5d9e6e0bd9cef71c59215
    role: context
  - path: pages/traits/physiology/tripolar_mating_system.html
    sha256: a3842e1a2d4dd6aa84949e5352f290a7ba1cc698f6800df5231151747d456f36
    role: context
  - path: pages/traits/physiology/trogocytosis.html
    sha256: 2e69dbf4ca63293f63a03aafc1490cf935b80bcf6c1d5a81dca1842d236b5365
    role: context
  - path: pages/traits/physiology/trophic_type.html
    sha256: 142379a20097d8005c73ec6cfa8a8d8818eb7ce3a81e3dfa0612297c7c7db737
    role: context
  - path: pages/traits/physiology/trypsin_activity.html
    sha256: 4c318ab8ba12a9a5925f675c3a2d1bac55518679afc2b7927a4ed19f11e1fae4
    role: context
  - path: pages/traits/physiology/tyrosine_arylamidase_activity.html
    sha256: 663e61333a3343038e669c4675b66e42bb3abc766e99be9665e3c94f9a3aecca
    role: context
  - path: pages/traits/physiology/unconventional_protein_secretion.html
    sha256: b5ae0e344eb0db9d084cdd8668270e061104fed23dd2a5f9f81d1ea8a09ffa71
    role: context
  - path: pages/traits/physiology/unequal_protein_aggregate_inheritance.html
    sha256: 5209406caa16e2f404ef732400806d196d1ac5a89f63d1dea3dcae997d341c4f
    role: context
  - path: pages/traits/physiology/unisexual_reproduction.html
    sha256: db7660c09c03ab9b598cfee1158dea2f663456faa73ec238ec1255c54d261389
    role: context
  - path: pages/traits/physiology/urease_activity.html
    sha256: b2e47fed0b810d9481cce0e02f61a97ce86efc23009dac86332a398c6642747f
    role: context
  - path: pages/traits/physiology/valine_arylamidase_activity.html
    sha256: ef37ad8a3b1b337768d40691fb5ca6bc01b9b69b5efd6b964d1e7865eaae77be
    role: context
  - path: pages/traits/physiology/viable_but_nonculturable_state.html
    sha256: d707580724403e672ea4fe0499e97659ade0318ccacb520ee3ab4495918f5552
    role: context
  - path: pages/traits/physiology/viscotaxis.html
    sha256: f2afb5869bfb048b6622ed5550b442ca8ec94bb63d410e83be46cb2724b8c31c
    role: context
  - path: pages/traits/quantitative_property/has_maximum_observed_value.html
    sha256: 6350ab288f66aafbb6d79414564819a05f407836b27d1de6247feedea241c679
    role: context
  - path: pages/traits/quantitative_property/has_minimum_observed_value.html
    sha256: 6f0506a61dd9244d4f7e11c6da2ff1e460cef474ee1b653b4f17ab8b1e3cd972
    role: context
  - path: pages/traits/quantitative_property/has_observed_spot_value.html
    sha256: a717e7366eea37f4d553bce99cd4e52579188d0baef9e6aa7043ae88db3dfe1e
    role: context
  - path: pages/traits/quantitative_property/has_value.html
    sha256: 958f8756aa6b44fd2956b3bf68a1fdd9df551e2f01542b7b89fcfefc61adf059
    role: context
  - path: pages/traits/quantitative_property/has_value_comments.html
    sha256: 7dd6905af8ebfe1223c160175daff8fda988369e454cc2a15f7772ed87762178
    role: context
  - path: pages/traits/quantitative_property/is_negative_data.html
    sha256: ff736154d22c88d318a6439a7446c179f4a39b1f755c2b7f7029c952e38d3369
    role: context
  - path: pages/traits/quantitative_property/observation_data_property.html
    sha256: 683c455a78c7c9031a79d930bade468246aabb1ae25d6363e196a14209aba023
    role: context
  - path: pages/traits/upper/biological_process.html
    sha256: 76adc0333c9bfa8072f9469b9af0463183d75db814abd3c51baf46ee967a4b5c
    role: context
  - path: pages/traits/upper/chemical_entity.html
    sha256: 15cf9604018c6328e7695d74c3ee1979f584f90d036c60713cdaa239511510b9
    role: context
  - path: pages/traits/upper/enzyme.html
    sha256: 471a911485668bf7bcc1b0533d2b3590aa28a764a2f46bd8fd5a98b1b6615bfe
    role: context
  - path: pages/traits/upper/material_entity.html
    sha256: 5dc100002a48400aa81e7ccef8a80f920c45ebabde1c43c3113238314db3471c
    role: context
  - path: pages/traits/upper/microbe.html
    sha256: ef23596ce8575fcd2b423e4332699bc36bcb7a6f91b591d446de9672f6ccac83
    role: context
  - path: pages/traits/upper/observation.html
    sha256: 58a7e582c2cb5add17412c2465d019f95abe314dead963cb081d7c781a7bfc5c
    role: context
  - path: pages/traits/upper/phenotype.html
    sha256: 1dee0cb74005e7c5b26744aff497fd04f9f7b29e4a40dc09afbf75b6c2820a7b
    role: context
  - path: pages/traits/upper/quality.html
    sha256: 7cf7289e66b1e8b1ba8d30ef906213b1a74d22e345bc8bc9520fbef0ad96b99c
    role: context
  - path: pages/umap.html
    sha256: d9f2254fdc8388a6d07b1499a68ad748103d31686567bb92dda93489d0f573dc
    role: context
  - path: proposals/metpo_traitmech_v589/metpo_proposal_classes_robot.tsv
    sha256: c0a1f1723fdab5db5e47a55e50c111f6026ddfea4471da0d40575aab1a8d53cd
    role: context
  - path: proposals/metpo_traitmech_v589/proposal.md
    sha256: f81a16f5bc8ab2eddd914e2add440133df6d942762bcedb37259eb67494ca5cb
    role: context
  - path: reports/metpo_2026_06_12_active_review.tsv
    sha256: 45e9c6471475635ba1f2602cd636a119d490f5dbd8dd6ac8af1aab89a321379f
    role: context
  - path: reports/metpo_2026_06_12_release_delta.tsv
    sha256: afe858d2aa0ade08322c7808d5917ff370e069ba02c2642d483342db8e9323ac
    role: context
  - path: reports/proposal_citation_audit.tsv
    sha256: 01ab468f51d81f527beef27fa70297410a5451ca970733f03dddc989dc9bb4be
    role: context
  - path: reports/robot/metpo_traitmech_v589/classes.owl
    sha256: 039151cbc5d8a103c723464087929da8d4eed6b18a735d5a47a7050d75a238e7
    role: context
  - path: reports/robot/metpo_traitmech_v589/merged.owl
    sha256: d1d3bce3a5c7d71ef78ead7d57524fd2a3c298586d4c6f105d1dd7bbe74e6f75
    role: context
  - path: reports/robot/metpo_traitmech_v589/reasoned.owl
    sha256: f5665ec57c68d11a682923e960a486ced38416b7c25c11b612c95ba9f6e54676
    role: context
  - path: research/traits/physiology/enhanced_transcriptional_reactivation_memory-source-verification.json
    sha256: d2d441472d8926885c38de0baf9d3dae031211032ea1a6151643e405fb1017cd
    role: context
  - path: reviews/structured/20261010T021647Z-haptocyst-discharge/review.md
    sha256: 9289dcb73273f15bc2cf3d0d30c18490d01979998ebcb7331fea085981e812a6
    role: context
  - path: reviews/structured/20261010T021647Z-haptocyst-discharge/review.yaml
    sha256: 15e7e11ec381f0b23716e92377c78ccb0aa7a4454cae4cd24076e9a8753ea976
    role: context
  - path: reviews/structured/20261010T042421Z-kinetocyst-discharge/review.md
    sha256: c6722b4a3103c925862c51a6b2127ba2b1402b156e423d5afe22d9bcbf87885f
    role: context
  - path: reviews/structured/20261010T042421Z-kinetocyst-discharge/review.yaml
    sha256: 760f28b25e7cf8c149e20cc93235767832b0a04b9007c1d9bccec7f90da594da
    role: context
  - path: reviews/structured/20261010T053738Z-siliceous-scale-production/review.md
    sha256: 546e0c28d8b650684b2147935a0d1294b118cfbb40cd4a3ddfddff6c72220f6f
    role: context
  - path: reviews/structured/20261010T053738Z-siliceous-scale-production/review.yaml
    sha256: e117d901411e6436ef426e66e8a95735924cce2842cdb446aaad485ab72e3e77
    role: context
  - path: reviews/structured/20261010T071627Z-coccolith-production/review.md
    sha256: 3c3d97614e407f45ef3fce7bc4c7e3b63373de3f94ebe69eb280b21d6e5f05e0
    role: context
  - path: reviews/structured/20261010T071627Z-coccolith-production/review.yaml
    sha256: 05692ff090c4d26e6ee9ab7ae4bee262face3e0b7200586ca629ebe1fb428376
    role: context
  - path: reviews/structured/20261010T193524Z-biomineralization/review.md
    sha256: 39e36cddb0734def77e4e424dc10b9c7d2c18eaf97b63628a32ce183ff3677bb
    role: context
  - path: reviews/structured/20261010T193524Z-biomineralization/review.yaml
    sha256: bd669f5b5d67ccbf4172bec46980805c7d8f19b0360e418b2b6cf38c369a1acb
    role: context
  - path: reviews/structured/20261010T210459Z-diatom-frustule-production/review.md
    sha256: b90ff2fba63a90603db4da17a3d0a8e7ff68f1bc1bc28d8e80825b7c17070854
    role: context
  - path: reviews/structured/20261010T210459Z-diatom-frustule-production/review.yaml
    sha256: cd65d0c232c23e1da4486c6a11948726240c98357e4bfc09f339c19b68e7a9bc
    role: context
  - path: reviews/structured/20261010T222230Z-diatom-seta-production/review.md
    sha256: ce351d55ee255b3c7683bd9888579bf66c96a0ed448156f48f0c64abc8a73f41
    role: context
  - path: reviews/structured/20261010T222230Z-diatom-seta-production/review.yaml
    sha256: 808995b7d3d5a971fd271168709d1144cec49e0b365f7ff97ec5f6415ce16ece
    role: context
  - path: reviews/structured/20261010T234601Z-diatom-perizonium-production/review.md
    sha256: 0d781eacc2963d5a2d68f9b4dd2b355e33b0cfe5bff8112392fa3862dce2cf05
    role: context
  - path: reviews/structured/20261010T234601Z-diatom-perizonium-production/review.yaml
    sha256: abb693026942abd0bd601e072785fa83a946479986066fb138be99db4518dbc2
    role: context
  - path: reviews/structured/20261011T032511Z-quorum-quenching/review.md
    sha256: 998e50c706558bbffbed6d316aebc80e70910da59cbb51af27deb2ee3f0ce7b3
    role: context
  - path: reviews/structured/20261011T032511Z-quorum-quenching/review.yaml
    sha256: 75e671d2be181c5ac4996d765c4c72da3ea5811f5579cb7ed804673ed187060b
    role: context
  - path: reviews/structured/20261011T093204Z-lethal-algicidal-activity/review.md
    sha256: c6b3ee9ac40e4f86b89493996fc6f3a058f8bf68e28b4245a5b8cae0d20c09aa
    role: context
  - path: reviews/structured/20261011T093204Z-lethal-algicidal-activity/review.yaml
    sha256: 01832620a5e5a5104cec5ad501a19ede4938bd90152336468f6bc05440f06cfd
    role: context
  - path: reviews/structured/20261011T105246Z-bacterial-mycophagy/review.md
    sha256: 4ccf22291e7addc0d9045808f0240389db1eb39079f11dd5ae3618a7f3f4b19e
    role: context
  - path: reviews/structured/20261011T105246Z-bacterial-mycophagy/review.yaml
    sha256: 7beaa07a76cae71790b1ff749c6609891cbe2d00cde6289d7ffbf0766e775234
    role: context
  - path: reviews/structured/20261011T121353Z-epibiotic-predation/review.md
    sha256: 7d1b2c676a55cc9664bbaa6ce3d9a0a781a18f52e4f75a3344030bb347460335
    role: context
  - path: reviews/structured/20261011T121353Z-epibiotic-predation/review.yaml
    sha256: c151545de842b21e90808fb02986de836e322bb49c00fa4884ebeffb2c4eb852
    role: context
  - path: reviews/structured/20261011T133104Z-ixotrophy/review.md
    sha256: 86f3d6ecca03044001a87e78ef8ad466081912b70c650d635192a3c0f21d302b
    role: context
  - path: reviews/structured/20261011T133104Z-ixotrophy/review.yaml
    sha256: 54b7bdbbc15054f28912b653716b48c9735ebd01cba70a086b8ea43971d8eeff
    role: context
  - path: reviews/structured/20261011T144951Z-periplasmic-predation/review.md
    sha256: eacbd9bf4e72b40ddbb954e6dc98b83c08f3804bb7a06464286c673e91505561
    role: context
  - path: reviews/structured/20261011T144951Z-periplasmic-predation/review.yaml
    sha256: 6e959efac9f9dd306661c06e6dadd57d15e30e94ee07ba91504838421ec9150f
    role: context
  - path: reviews/structured/20261011T161045Z-cytoplasmic-predation/review.md
    sha256: 548d5d4b0af368b34540f47ee8e73cdfc0360205e2d3e5eb7d9268100b300e5c
    role: context
  - path: reviews/structured/20261011T161045Z-cytoplasmic-predation/review.yaml
    sha256: 154228d6c946f3b2d77b0c158c23f0bd0357929503736418a443a0e3910c2924
    role: context
  - path: reviews/structured/20261011T173058Z-collective-predation/review.md
    sha256: 4c05866748bc7d066a7c83a0366be9ee3cd0e55de73e9a1edc7f2b466a012ac7
    role: context
  - path: reviews/structured/20261011T173058Z-collective-predation/review.yaml
    sha256: 0c44b211ae9e70ffb5b87319b1b5c7c0676657c0e7b852540eb8871223a5adce
    role: context
  - path: reviews/structured/20261011T182731Z-swimming-source-scope/review.md
    sha256: 9aba8d5bb88461b6e6537d5869cc1366ab18f4c1acb708ca3fa52c3c31124272
    role: context
  - path: reviews/structured/20261011T182731Z-swimming-source-scope/review.yaml
    sha256: 02048e478baaaecec91e4f8f31629c20b635cc1f7d3d6fd9f24516d9bc74abcf
    role: context
  - path: reviews/structured/20261011T185720Z-swimming-motility/review.md
    sha256: 97a817a7c2e0f38b67b0e52967cb1b4ed7753f464b295a682be8d7a84cbe372b
    role: context
  - path: reviews/structured/20261011T185720Z-swimming-motility/review.yaml
    sha256: 929768c4bd99c8644f0431ad0aa0cb036ba3428096678d5ed74d041b285361dc
    role: context
  - path: reviews/structured/20261011T215629Z-expansion-driven-sliding/review.md
    sha256: b6b2e2eb199217450a33b73135d93b6b4f64acb75e6c4606a02b84bf7ecf5088
    role: context
  - path: reviews/structured/20261011T215629Z-expansion-driven-sliding/review.yaml
    sha256: 4db69c73fc685f07e310bfd10c30e51862c33000c6a11d03f235a40ce295bdbf
    role: context
  - path: reviews/structured/20261012T001136Z-diauxic-growth/review.md
    sha256: c4ddc079f3c0cabdde81a1742660001ad67a9386ccb0e17fd4f7abe65fd3422f
    role: context
  - path: reviews/structured/20261012T001136Z-diauxic-growth/review.yaml
    sha256: 865912f155dd1348dca24b788ad51e4c086740f7c82f0e3c77ac618146a0723b
    role: context
  - path: reviews/structured/20261012T013705Z-aerobic-overflow/review.md
    sha256: 2d0fa708836d844c988b4f3c3221103bce5fb60de130b2ef00a37a01fc469252
    role: context
  - path: reviews/structured/20261012T013705Z-aerobic-overflow/review.yaml
    sha256: fc0dfebd1f96be39a42959d27d7c0b0c3ed4885c93230b96f6b40a3c92649b5b
    role: context
  - path: reviews/structured/20261012T015307Z-aerobic-overflow-snippet-finding/review.md
    sha256: e24de8986df92c05265a4859285cf0111449e4a09b00d2e6c0db32f62b483c75
    role: context
  - path: reviews/structured/20261012T015307Z-aerobic-overflow-snippet-finding/review.yaml
    sha256: aa2625f035f0ad08682e7bf7df769ce769ddc4c2853aa4928145c7b692cf405a
    role: context
  - path: reviews/structured/20261012T022143Z-aerobic-overflow-resolution/review.md
    sha256: 714abade335466d0ea974744ea68f4eb1029fe410e212ecbcb4c272339adf36d
    role: context
  - path: reviews/structured/20261012T022143Z-aerobic-overflow-resolution/review.yaml
    sha256: 47f9db2e7af35740c45108e1bbbf326c0831975c4411484eee2c1f33686eb94c
    role: context
  - path: reviews/structured/20261012T040100Z-carbon-source-memory/review.md
    sha256: 0ad8d3f73a325152f26d830cf2e5e25b8203b6571725f54a7580a1a6bf516e73
    role: context
  - path: reviews/structured/20261012T040100Z-carbon-source-memory/review.yaml
    sha256: 7b206ee8bb4dbd0d48c31cb1c6af95f97a30e85d35126649f75f679ea1e6029c
    role: context
  - path: reviews/structured/20261012T053931Z-environmental-anticipation/review.md
    sha256: e2b7e4696c29a4ecfa5b9b244225afbb49bd4ef8579d65a0444c2de345c70853
    role: context
  - path: reviews/structured/20261012T053931Z-environmental-anticipation/review.yaml
    sha256: 1b79a3e66623b8abeff87fd78ad6bb0fa6a3d8a726b5bd662b75855caaf5bd2a
    role: context
  - path: reviews/structured/20261012T070401Z-bet-hedging-scope/review.md
    sha256: f1fa2e323e0d33d623a66af4c6224d2df42063c14953db5a3f831d8b8e45d78b
    role: context
  - path: reviews/structured/20261012T070401Z-bet-hedging-scope/review.yaml
    sha256: afa5c03a9836829a78390f3439166d9edf6eec1e7941cbbbcc181d929d052d96
    role: context
  - path: reviews/structured/20261012T074314Z-diversifying-bet-hedging/review.md
    sha256: ba5578229a722b3237077583c2cf4547d9b4216ae0cf0b50b90fe03c70d0e0d1
    role: context
  - path: reviews/structured/20261012T074314Z-diversifying-bet-hedging/review.yaml
    sha256: fe8a5e774b1e88ab19ff62104bc983fee50fc80f8915c20d2286e5404cd47809
    role: context
  - path: reviews/structured/20261012T084748Z-bet-hedging-external-finding/review.md
    sha256: 0c8517172a9d2cf05fe8724fe9364880c8b14f5b1ee567ed8907de0580ea8bfe
    role: context
  - path: reviews/structured/20261012T084748Z-bet-hedging-external-finding/review.yaml
    sha256: 2cfee84ea03c7521ccc3c95881b32c0fe90103f5f184407b9cd3247a131f139a
    role: context
  - path: reviews/structured/20261012T084933Z-bet-hedging-external-fix/review.md
    sha256: bb1aed04f01daa6e44a051b2ef26af58eb7d3fa14d9b60572acc9b302c109da4
    role: context
  - path: reviews/structured/20261012T084933Z-bet-hedging-external-fix/review.yaml
    sha256: c40f25be0623803c3e0691d68665de3c07808c8771e7e90186039174744c853d
    role: context
  - path: reviews/structured/20261012T102912Z-aging-label-scope/review.md
    sha256: 4da4668619e696f0ad9e17ee69c92be27c820483584222b857b022c2d80a7a4e
    role: context
  - path: reviews/structured/20261012T102912Z-aging-label-scope/review.yaml
    sha256: adc8c12cf7bef84c812f8f2c01b26685b05662bde27a0c14d95d71d2595a0cfb
    role: context
  - path: reviews/structured/20261012T110106Z-replicative-aging/review.md
    sha256: aaf321dfd78725bb0f0fa2748fb0b595ac35b8ff68ee5fb5c3ab6bf0d6372b38
    role: context
  - path: reviews/structured/20261012T110106Z-replicative-aging/review.yaml
    sha256: 88c6beea172eff37a8adacc6e03b27f3c5c5f426eb5caf682ba0a9952ffe26cb
    role: context
  - path: reviews/structured/20261012T124741Z-cellular-rejuvenation/review.md
    sha256: 356af4214d5f5cadf168ce8518050c7a424c61c0502d67fd6b9a0280e913a54e
    role: context
  - path: reviews/structured/20261012T124741Z-cellular-rejuvenation/review.yaml
    sha256: ef771df43335d01efd4dc816471220c016d7f814fc7e1bba968ea56c74a01585
    role: context
  - path: reviews/structured/20261012T130746Z-rejuvenation-figure-resolution/review.md
    sha256: a093ffc67832d6dc43f558d4e533d0444305b53bf5c517965119338ab8dc82b3
    role: context
  - path: reviews/structured/20261012T130746Z-rejuvenation-figure-resolution/review.yaml
    sha256: 23ed446cf45c575cb096de84e6e220616f801df9fb986168ed5ade62790ee2e9
    role: context
  - path: reviews/structured/20261012T150115Z-unequal-protein-aggregate-inheritance/review.md
    sha256: 5257caf2efb154d78b0e0bafc62dd5e42bd02adfcfecfe37bb6df9df3a51dd9f
    role: context
  - path: reviews/structured/20261012T150115Z-unequal-protein-aggregate-inheritance/review.yaml
    sha256: a19ab148249e7d2a80a2be067f97f83afc210e6aa6d0f632582d891eb0f506c9
    role: context
  - path: reviews/structured/20261012T182317Z-aggregate-reporter-bias-finding/review.md
    sha256: 1d594c89c255e13258c7e273de219b26f061bc8f0e47aecf6131fb7bbf929b59
    role: context
  - path: reviews/structured/20261012T182317Z-aggregate-reporter-bias-finding/review.yaml
    sha256: 10f796bc88bf9e84ac349a1447c5e3d53fae11149d946f21d889f433d6664802
    role: context
  - path: reviews/structured/20261012T184416Z-aggregate-inheritance-reporter-successor/review.md
    sha256: 4b74eb3549a43db891469faf370fda6d8c77be75b5db919364fdf167c53e4d3c
    role: context
  - path: reviews/structured/20261012T184416Z-aggregate-inheritance-reporter-successor/review.yaml
    sha256: 2876cf52a343af5c8f86ec8ada3de242b14d4d1a371cd07284f5aba7b4965879
    role: context
  - path: reviews/structured/20261012T212659Z-acquired-stress-resistance-memory/review.md
    sha256: 9185b1e08bf359ff6cb409e479a8612ca00154377f283532c60302a1ceda3eba
    role: context
  - path: reviews/structured/20261012T212659Z-acquired-stress-resistance-memory/review.yaml
    sha256: 32de065a01b443379f28533f3eb909d5e740543f9b245ab9feec6a8ce27f72c7
    role: context
  - path: reviews/structured/20261012T215358Z-stress-memory-diagnostic-successor/review.md
    sha256: b1683f65649fadc7d129cf1f558713e3bf2922aa2c23ef3049e753bab80ac28c
    role: context
  - path: reviews/structured/20261012T215358Z-stress-memory-diagnostic-successor/review.yaml
    sha256: a15c07c938e8cc4b6cdcdd4e276721cbdb2465653967465cc43ca96d231886e8
    role: context
  - path: reviews/structured/20261012T225918Z-ncbi-truncated-error-body/review.md
    sha256: 2d71e15cc2e628dcfa4be996c5a2c8c19d1a440fcf301c81f24f0d3d10708309
    role: context
  - path: reviews/structured/20261012T225918Z-ncbi-truncated-error-body/review.yaml
    sha256: 6558d7a792d08b1d0b45689a79a07ba6cf4d117b637833b2d0c36910e0c6e2cb
    role: context
  - path: reviews/structured/20261012T232840Z-ncbi-http-read-successor/review.md
    sha256: 23736cfe14793b30a572ea8c5cb0cb3233c51d7a9811a863b39fa81e2f334d1f
    role: context
  - path: reviews/structured/20261012T232840Z-ncbi-http-read-successor/review.yaml
    sha256: fb4574eaa9dbfedd3b70b56a61fd7a31f5e86f791d291576967ca7f70441e4da
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/.vendored_canon_ref
    sha256: 698af47e96e93fe96e81910bb140593a79c2b92c4688892edeab9b63244ec5bf
    role: context
  - path: scripts/add_transcriptional_reactivation_memory_trait.py
    sha256: d6d5584811e4805b5bf295f2e9573285faa6e5726b73df2c5b8bb6cad2aebf02
    role: context
  - path: scripts/audit_canonical_examples.py
    sha256: 3b334e4ec3a5ee2b1c8af589354d400a8ae7c3fbc0d66f574b74345546147701
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/render_trait_pages.py
    sha256: e588477da7c22b7c8e6ae796dc53b5b16a3d4dc3ecfa3677ce8c16a7c1e112ea
    role: context
  - path: scripts/robot_validate_proposal.py
    sha256: 8b038824905e36ba7a7afd0ed3181e85255522e8e6eace7466a6b2416adef916
    role: context
  - path: scripts/trait_priority.py
    sha256: 96909390f0f55a76fe7161420813f072774a483797c29f96589be379c07892fb
    role: context
  - path: scripts/verify_metpo_proposal.py
    sha256: f58355151f7d6a807bb50dc8b732184994b0d6145d3c57f54e29fd0bb76268b6
    role: context
  - path: scripts/verify_snippets.py
    sha256: e235ef0a80ba564f929b8255e80ef1265bfdd016f74c627bcb7e7b86e033ddcc
    role: context
  - path: src/traitmech/curate/curation_event.py
    sha256: d9b3e70539bbf13f9130544e18ed7664ff2c3b7c60bcc2cae5185663fe25badd
    role: context
  - path: src/traitmech/schema/history.yaml
    sha256: b01b06f1b9a37db205c26c31ec0fd910690848507c7e1bfb73b424ac0829c52d
    role: context
  - path: src/traitmech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: src/traitmech/schema/traitmech.yaml
    sha256: 46c47fc627b80ccbba1e8ab3fb6f2aee93bc2aef7aaf72fe9aadc3257f2c02dd
    role: context
  - path: src/traitmech/validation/write_validated.py
    sha256: 68cfeb876a60d67fd72d5a2800cd29e41b5cf563be5a27b698398a5bb3e67231
    role: context
  - path: tests/test_add_transcriptional_reactivation_memory_trait.py
    sha256: 0bc9ab5f163c8e517852bff54e3426f02d88110f6deab51e43b3183e65cb575d
    role: context
targets:
- target_id: traitmech:000713
  path: data/traits/physiology/enhanced_transcriptional_reactivation_memory.yaml
  label: enhanced transcriptional reactivation memory
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: scripts/add_transcriptional_reactivation_memory_trait.py
    role: guarded writer
  - repository: CultureBotAI/TraitMech
    path: data/traits/physiology/enhanced_transcriptional_reactivation_memory.yaml
    role: curated record
  - repository: CultureBotAI/TraitMech
    path: proposals/metpo_traitmech_v589/metpo_proposal_classes_robot.tsv
    role: upstream proposal
scope:
  description: Complete new record and maintained/generated change set, not whole-corpus
    scientific review.
  selection: One exact newly curated trait; no sampling.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - traitmech:000713
  exclusions:
  - target: Other 1107 TraitRecords
    reason: Novelty, byte preservation and deterministic validation only.
  - target: data/traits/physiology/spore_germination.yaml
    reason: Protected; unchanged.
checks:
- check_id: focused-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q tests/test_add_transcriptional_reactivation_memory_trait.py tests/test_readme_artifacts.py
    tests/test_trait_priority.py tests/test_qc_dashboard_artifacts.py
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q tests/test_add_transcriptional_reactivation_memory_trait.py tests/test_readme_artifacts.py
    tests/test_trait_priority.py tests/test_qc_dashboard_artifacts.py
  status: passed
  required: true
  target_ids:
  - traitmech:000713
  exit_code: 0
  expected_exit_code: 0
  summary: Writer, README, priority and QC-dashboard tests passed, including drift
    refusal, prevalidation without writes, replay, copy isolation and source/proposal
    consistency.
- check_id: records-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate
    -s src/traitmech/schema/traitmech.yaml --target-class TraitRecord data/traits/physiology/enhanced_transcriptional_reactivation_memory.yaml
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate
    -s src/traitmech/schema/traitmech.yaml --target-class TraitRecord data/traits/physiology/enhanced_transcriptional_reactivation_memory.yaml
  status: passed
  required: true
  target_ids:
  - traitmech:000713
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed; corpus diagnostics are not whole-corpus scientific
    review.
- check_id: records-1
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_strict.py data/traits/physiology/enhanced_transcriptional_reactivation_memory.yaml
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_strict.py data/traits/physiology/enhanced_transcriptional_reactivation_memory.yaml
  status: passed
  required: true
  target_ids:
  - traitmech:000713
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed; corpus diagnostics are not whole-corpus scientific
    review.
- check_id: records-2
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/verify_snippets.py --record data/traits/physiology/enhanced_transcriptional_reactivation_memory.yaml
    --out /tmp/traitmech-transcriptional-memory-checks-20261013/snippet-results.tsv
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/verify_snippets.py --record data/traits/physiology/enhanced_transcriptional_reactivation_memory.yaml
    --out /tmp/traitmech-transcriptional-memory-checks-20261013/snippet-results.tsv
  status: passed
  required: true
  target_ids:
  - traitmech:000713
  exit_code: 0
  expected_exit_code: 0
  summary: 'Actual final-record verifier checked two DOI references: both NOT_IN_ABSTRACT.
    Separate exact contiguous full-text matches support the Results quotations; neither
    is mislabeled native VERIFIED.'
- check_id: generate-0
  name: just audit-proposals
  command: just audit-proposals
  status: passed
  required: true
  target_ids:
  - traitmech:000713
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed; corpus diagnostics are not whole-corpus scientific
    review.
- check_id: generate-1
  name: just ground-predicates
  command: just ground-predicates
  status: passed
  required: true
  target_ids:
  - traitmech:000713
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed; corpus diagnostics are not whole-corpus scientific
    review.
- check_id: generate-2
  name: just ground-nodes
  command: just ground-nodes
  status: passed
  required: true
  target_ids:
  - traitmech:000713
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed; corpus diagnostics are not whole-corpus scientific
    review.
- check_id: generate-3
  name: just audit-graphs
  command: just audit-graphs
  status: passed
  required: true
  target_ids:
  - traitmech:000713
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed; corpus diagnostics are not whole-corpus scientific
    review.
- check_id: generate-4
  name: just audit-graph-protein-taxa
  command: just audit-graph-protein-taxa
  status: passed
  required: true
  target_ids:
  - traitmech:000713
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed; corpus diagnostics are not whole-corpus scientific
    review.
- check_id: generate-5
  name: just audit-predicate-domains
  command: just audit-predicate-domains
  status: passed
  required: true
  target_ids:
  - traitmech:000713
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed; corpus diagnostics are not whole-corpus scientific
    review.
- check_id: generate-6
  name: just check-biolink-coverage
  command: just check-biolink-coverage
  status: passed
  required: true
  target_ids:
  - traitmech:000713
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed; corpus diagnostics are not whole-corpus scientific
    review.
- check_id: generate-7
  name: just audit-snippets
  command: just audit-snippets
  status: passed
  required: true
  target_ids:
  - traitmech:000713
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed; corpus diagnostics are not whole-corpus scientific
    review.
- check_id: generate-8
  name: just gen-discussions-data
  command: just gen-discussions-data
  status: passed
  required: true
  target_ids:
  - traitmech:000713
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed; corpus diagnostics are not whole-corpus scientific
    review.
- check_id: generate-9
  name: just gen-qc-dashboard
  command: just gen-qc-dashboard
  status: passed
  required: true
  target_ids:
  - traitmech:000713
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed; corpus diagnostics are not whole-corpus scientific
    review.
- check_id: generate-10
  name: just gen-pages
  command: just gen-pages
  status: passed
  required: true
  target_ids:
  - traitmech:000713
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed; corpus diagnostics are not whole-corpus scientific
    review.
- check_id: generate-11
  name: just gen-priority-dashboard
  command: just gen-priority-dashboard
  status: passed
  required: true
  target_ids:
  - traitmech:000713
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed; corpus diagnostics are not whole-corpus scientific
    review.
- check_id: verify-0
  name: just qc
  command: just qc
  status: passed
  required: true
  target_ids:
  - traitmech:000713
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed; corpus diagnostics are not whole-corpus scientific
    review.
- check_id: verify-1
  name: just validate-history
  command: just validate-history
  status: passed
  required: true
  target_ids:
  - traitmech:000713
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed; corpus diagnostics are not whole-corpus scientific
    review.
- check_id: verify-2
  name: just validate-products
  command: just validate-products
  status: passed
  required: true
  target_ids:
  - traitmech:000713
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed; corpus diagnostics are not whole-corpus scientific
    review.
- check_id: verify-3
  name: just verify-proposal metpo_traitmech_v589
  command: just verify-proposal metpo_traitmech_v589
  status: passed
  required: true
  target_ids:
  - traitmech:000713
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed; corpus diagnostics are not whole-corpus scientific
    review.
- check_id: verify-4
  name: just robot-validate-proposal metpo_traitmech_v589
  command: just robot-validate-proposal metpo_traitmech_v589
  status: passed
  required: true
  target_ids:
  - traitmech:000713
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed; corpus diagnostics are not whole-corpus scientific
    review.
- check_id: verify-5
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/ruff
    check src scripts tests
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/ruff
    check src scripts tests
  status: passed
  required: true
  target_ids:
  - traitmech:000713
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed; corpus diagnostics are not whole-corpus scientific
    review.
- check_id: tests-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q --junitxml=/tmp/traitmech-transcriptional-memory-checks-20261013/pytest.xml
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q --junitxml=/tmp/traitmech-transcriptional-memory-checks-20261013/pytest.xml
  status: passed
  required: true
  target_ids:
  - traitmech:000713
  exit_code: 0
  expected_exit_code: 0
  summary: 4336 full-suite tests passed without skips, failures or errors.
- check_id: supplemental-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_history_links.py history/records/enhanced_transcriptional_reactivation_memory
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_history_links.py history/records/enhanced_transcriptional_reactivation_memory
  status: passed
  required: true
  target_ids:
  - traitmech:000713
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed; corpus diagnostics are not whole-corpus scientific
    review.
- check_id: supplemental-1
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate
    --schema src/traitmech/schema/history.yaml --target-class HistoryRecord history/records/enhanced_transcriptional_reactivation_memory/2026-10-13T003746Z-claude-code-cf0b17.yaml
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate
    --schema src/traitmech/schema/history.yaml --target-class HistoryRecord history/records/enhanced_transcriptional_reactivation_memory/2026-10-13T003746Z-claude-code-cf0b17.yaml
  status: passed
  required: true
  target_ids:
  - traitmech:000713
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed; corpus diagnostics are not whole-corpus scientific
    review.
- check_id: supplemental-2
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate
    --schema src/traitmech/schema/history.yaml --target-class HistoryRecord history/records/enhanced_transcriptional_reactivation_memory/2026-10-13T003824Z-codex-8495dc.yaml
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate
    --schema src/traitmech/schema/history.yaml --target-class HistoryRecord history/records/enhanced_transcriptional_reactivation_memory/2026-10-13T003824Z-codex-8495dc.yaml
  status: passed
  required: true
  target_ids:
  - traitmech:000713
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed; corpus diagnostics are not whole-corpus scientific
    review.
- check_id: supplemental-3
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/audit_canonical_examples.py --no-resolve
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/audit_canonical_examples.py --no-resolve
  status: passed
  required: true
  target_ids:
  - traitmech:000713
  exit_code: 0
  expected_exit_code: 0
  summary: Existing canonical examples passed offline shape checks. --no-resolve does
    not verify remote taxon identity; this addition contains no canonical taxa.
- check_id: supplemental-4
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/run_trait_graph_audit.py --verify
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/run_trait_graph_audit.py --verify
  status: passed
  required: true
  target_ids:
  - traitmech:000713
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed; corpus diagnostics are not whole-corpus scientific
    review.
- check_id: supplemental-5
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/audit_history_records.py --base 62f45e1749fa3d3e5ca8b9a3a4ba5bb0361beb8b
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/audit_history_records.py --base 62f45e1749fa3d3e5ca8b9a3a4ba5bb0361beb8b
  status: passed
  required: true
  target_ids:
  - traitmech:000713
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed; corpus diagnostics are not whole-corpus scientific
    review.
- check_id: supplemental-6
  name: git diff --check 62f45e1749fa3d3e5ca8b9a3a4ba5bb0361beb8b HEAD -- . ':(exclude)proposals/metpo_traitmech_v589/metpo_proposal_classes_robot.tsv'
  command: git diff --check 62f45e1749fa3d3e5ca8b9a3a4ba5bb0361beb8b HEAD -- . ':(exclude)proposals/metpo_traitmech_v589/metpo_proposal_classes_robot.tsv'
  status: passed
  required: true
  target_ids:
  - traitmech:000713
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed; corpus diagnostics are not whole-corpus scientific
    review.
- check_id: supplemental-7
  name: git -c core.whitespace=-blank-at-eol diff --check 62f45e1749fa3d3e5ca8b9a3a4ba5bb0361beb8b
    HEAD -- proposals/metpo_traitmech_v589/metpo_proposal_classes_robot.tsv
  command: git -c core.whitespace=-blank-at-eol diff --check 62f45e1749fa3d3e5ca8b9a3a4ba5bb0361beb8b
    HEAD -- proposals/metpo_traitmech_v589/metpo_proposal_classes_robot.tsv
  status: passed
  required: true
  target_ids:
  - traitmech:000713
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed; corpus diagnostics are not whole-corpus scientific
    review.
- check_id: browser
  name: Rendered desktop/mobile products
  command: node /tmp/traitmech-transcriptional-memory-browser-20261013.cjs
  status: passed
  required: true
  target_ids:
  - traitmech:000713
  exit_code: 0
  expected_exit_code: 0
  summary: '1440/390 px assertions passed: two quotes, three discussions, two history
    links including the attribution correction, local identity, hierarchy/browse navigation,
    dashboard count and loaded coverage image. Eight screenshots visually inspected;
    no horizontal overflow or page errors.'
- check_id: generator
  name: Pinned generator and embedding applicability
  status: passed
  required: true
  target_ids:
  - traitmech:000713
  summary: 152 pinned generator source blobs verified. Neither exact configured embedding
    source exists in primary/owned layouts; existing embedding bytes retained.
evidence:
- evidence_id: source-0
  kind: primary_source
  reference: DOI:10.7554/eLife.77646
  locator: Results s2-1; selected Methods and actual figure panels qualified in notes.
  accessed_at: '2026-10-12T21:24:51.189605Z'
  support: supports
  summary: Sump et al. 2022, PMID:35579426, PMC9129879; Results s2-1, paragraph 2,
    contiguous in primary XML and publisher Version of Record HTML. Figure 1D uses
    synthetic Opi1 Anchor Away to bypass upstream induction control; enhancement is
    lost in mrs and nup100 mutants. Ordinary-starvation INO1 reactivation in Figure
    1B is not clearly faster than activation. Figure 1 supplement 1C separately measures
    CHO1/ACT1 after three-hour repression; its generic statistical-comparator caption
    is ambiguous. Figure 1 supplement 2E measures 18-hour peripheral localization,
    not that duration of enhanced transcription; the main Results mispoints to supplement
    1. Figure 1G competitive fitness is a different endpoint, not proof of transcriptional
    causality. Selected Results, Methods, scientific abstract, actual figures and
    strain-table rows were inspected. RT-qPCR mRNA kinetics are not direct measurements
    of initiation rate. Native abstract lookup returns NOT_IN_ABSTRACT; direct full-text
    matching supports the quotation, not a native VERIFIED verdict.
  snapshot_sha256: 4d895d6a7b79a8f94e4c9d9cc8177c96c090ff6a619916e57c12a75ea9ceac5e
- evidence_id: source-1
  kind: primary_source
  reference: DOI:10.7554/eLife.16691
  locator: Results s2-7; selected Methods and actual figure panels qualified in notes.
  accessed_at: '2026-10-12T21:24:48.138101Z'
  support: supports
  summary: D'Urso et al. 2016, PMID:27336723, PMC4951200; Results s2-7, paragraph
    1, contiguous in primary XML and publisher Version of Record HTML. This sentence
    attributes the gene count and duration to Guan 2012; Figure 7A directly tests
    selected mRNA responses after 0.7 M NaCl for one hour, two-hour rich-medium recovery,
    then 0.5 mM H2O2. PGM2, PMT5 and YGP1 differ from the HSP31 control. Four-generation
    persistence is not measured in that panel. Actual Figure 7B is wild-type ChIP,
    C mutant ChIP, D mutant mRNA and E Ssn3 ChIP; caption B/C/D assignments conflict
    with the image. INO1 mutant reactivation defects in Figure 1E/F alone do not establish
    faster within-wild-type reactivation. Relevant Results, Methods, abstract and
    actual figures were inspected; raw data were not reanalyzed. Native abstract lookup
    returns NOT_IN_ABSTRACT, with the selected quotation independently matched in
    full text.
  snapshot_sha256: 6f4871eee27285b38bf469d510688964b2c1ccf024d95c3a6f9fdce3a22a384d
- evidence_id: content
  kind: record_content
  reference: data/traits/physiology/enhanced_transcriptional_reactivation_memory.yaml
  locator: Complete record, guarded writer/tests, proposal, sidecar, history, skill
    and generated products.
  accessed_at: '2026-10-13T01:05:10Z'
  support: supports
  summary: One qualified physiological CLASS, two DOI sources and full-text Results
    snippets; no canonical examples, causal graph, exact synonym or equivalence xref.
    Status remains PROPOSED.
- evidence_id: novelty
  kind: search
  reference: research/traits/physiology/enhanced_transcriptional_reactivation_memory-source-verification.json
  locator: Bounded novelty, allocation and prepublication receipts.
  accessed_at: '2026-10-13T01:05:10Z'
  support: supports
  summary: Ignored/hidden available files, 18 retained historical trees, nine independent
    copies, 1122 distinct normalized trait versions, current upstream snapshots and
    11 stable pending PRs yielded no exact active record or competing reservation
    in scope. The new owned root is the only reservation delta; coordinate and namespace-envelope
    hits were hash/context-adjudicated.
  search_scope: Available ignored/hidden TraitMech files, retained registered historical
    tracked trees, nine known independent copies, normalized YAML semantics, full
    nonremoved changed blobs of TraitMech/CommunityMech/METPO pending PRs, current
    selected ontology/templates/mappings/proposals. Gzip embedding data were decoded.
    No inaccessible historical ignored/untracked bytes, symlink traversal, arbitrary
    archive expansion, unchanged PR trees, deleted historical blobs or global filesystem
    absence claim. Reproducible locators and hashes are retained in receipts.
- evidence_id: ontology
  kind: database
  reference: data/raw/metpo.owl
  locator: Pinned/current released RDF; active phenotype parent; deprecated 1000108
    and 1000310.
  accessed_at: '2026-10-13T01:05:10Z'
  support: supports
  summary: Phenotype is broader and active. Deprecated lexical neighbors have no replacement/consider
    in inspected graphs, but original historical definitions/parents remain unassessed
    and the OMO reason assignment is disputed in METPO#521. Positive experimental
    scope supports independent acceptance; no revival or historical equivalence claim.
- evidence_id: products
  kind: validation
  reference: reports/proposal_citation_audit.tsv
  locator: Native checks, parsed RDF, byte preservation and browser inspection.
  accessed_at: '2026-10-13T01:05:10Z'
  support: supports
  summary: 'All 1107 prior trait YAMLs and prior histories/reviews/proposals/embeddings/templates
    are unchanged. Prior trait pages differ only in footer count except the phenotype
    child link. Proposal RDF checks: {''classes'': 15, ''merged'': 12628, ''reasoned'':
    12632}; 11-column template and trailing blank directive cells retained.'
- evidence_id: history
  kind: record_content
  reference: history/records/enhanced_transcriptional_reactivation_memory/2026-10-13T003824Z-codex-8495dc.yaml
  locator: 'Successor and immutable original 2026-10-13T003746Z-claude-code-cf0b17.yaml;
    issue #1902.'
  accessed_at: '2026-10-13T01:05:10Z'
  support: supports
  summary: Initial CREATE used the default actor name despite correct gpt-5/codex
    model/tool fields. The preserved successor explicitly identifies Codex as the
    actual actor and states no Claude execution. No history rewrite occurred; validation
    and rendered links include both entries. Issue closure remains contingent on merge.
assessments:
- assessment_id: identity
  area: identity
  topic: Enhanced transcript reactivation after repression
  summary: The definition denotes an assayable physiological history effect, not a
    sequence feature, chromatin mark or persistent reporter. It is not equivalent
    to retained resistance or the full growth/induction scope of carbon-source memory.
  target_ids:
  - traitmech:000713
  evidence_ids:
  - content
  - source-0
  - source-1
  - novelty
  outcome: supported
- assessment_id: endpoint
  area: evidence
  topic: Ordinary versus synthetic induction and causal scope
  summary: Sump Figure 1D supports synthetic Opi1 Anchor-Away enhancement; Figure
    1B does not establish clearly faster ordinary-starvation reactivation. Mutant
    defects alone do not establish a within-wild-type enhancement. mRNA kinetics,
    localization, fitness and chromatin inheritance are not interchanged.
  target_ids:
  - traitmech:000713
  evidence_ids:
  - source-0
  - source-1
  - content
  outcome: supported
- assessment_id: duration
  area: quantity
  topic: Measured recovery versus cited multigeneration persistence
  summary: D'Urso Figure 7A uses two-hour recovery and selected transcripts. The four-generation/gene-count
    sentence attributes Guan 2012, not a new measurement in that panel. Sump 18-hour
    localization is not an 18-hour enhanced-transcription assay. No universal duration
    is defined.
  target_ids:
  - traitmech:000713
  evidence_ids:
  - source-0
  - source-1
  outcome: supported
- assessment_id: sources
  area: provenance
  topic: Full-text snippets and source discrepancies
  summary: Two exact contiguous Results snippets support the qualified interpretation;
    native NOT_IN_ABSTRACT is retained. Selected version agreement does not erase
    the D'Urso panel-caption mismatch, Sump supplement locator or strain-description
    ambiguities. No independent-laboratory replication is claimed.
  target_ids:
  - traitmech:000713
  evidence_ids:
  - source-0
  - source-1
  - content
  outcome: supported
- assessment_id: grounding
  area: grounding
  topic: Conservative parent and independent acceptance
  summary: The active phenotype parent is strictly broader. Original historical definitions
    remain unavailable; labels do not prove historical nonequivalence. The operational
    new phenotype is accepted from positive evidence without reusing or exactly mapping
    deprecated IDs.
  target_ids:
  - traitmech:000713
  evidence_ids:
  - ontology
  - content
  - novelty
  outcome: supported
- assessment_id: history
  area: provenance
  topic: Append-only attribution correction
  summary: Codex is the correct record curator and creator. The accidental default
    name is explicitly corrected without deleting or rewriting the original. Both
    target-linked entries render, and the scoped skill change has separate correctly
    attributed history.
  target_ids:
  - traitmech:000713
  evidence_ids:
  - history
  - products
  - content
  outcome: supported
- assessment_id: products
  area: consistency
  topic: Guarded ownership, proposal and generated products
  summary: Drift refusal, prevalidation, replay, schema/strict/QC gates, full tests,
    proposal RDF and responsive views pass. Only one trait is added; existing scientific
    records, review bundles and baselines are unchanged.
  target_ids:
  - traitmech:000713
  evidence_ids:
  - products
  - content
  outcome: supported
- assessment_id: limits
  area: completeness
  topic: Unasserted mechanisms and natural exemplars
  summary: Natural strain provenance, universal molecular mechanisms, original deprecated-term
    semantics and some source discrepancies remain unresolved. No graph, canonical
    taxon or exact synonym pretends to close those optional extensions.
  target_ids:
  - traitmech:000713
  evidence_ids:
  - content
  - source-0
  - source-1
  - ontology
  outcome: unknown
findings: []
actions: []
limitations:
- Author self-review; PROPOSED status is retained and no human scientific sign-off
  is asserted.
- Two papers share a research lineage. Selected actual figures and Results/Methods
  were inspected, not full raw-data reanalysis. Limited-resolution figures and selected
  strain-table rows constrain numerical/provenance claims.
- Original historical definitions and parent axioms for deprecated lexical neighbors
  remain unassessed. Independent acceptance does not establish historical exact equivalence
  or nonequivalence.
- Publisher access challenges, caption/locator discrepancies and bounded notice checks
  remain explicit; no exhaustive correction/retraction absence claim.
- Searches include ignored/hidden available files but exclude unavailable historical
  ignored/untracked bytes, symlink directories, arbitrary archives, unchanged pending
  trees and deleted historical blobs. Discovery is not exhausted.
- Existing QC baselines and skipped remote taxonomy adapters retain their limitations.
  Configured embedding sources are unavailable; existing embedding bytes are preserved.
- 'Issue #1902 is fixed on this branch by an append-only successor, not closed merely
  by this review. GitHub review, exact-head CI, actual merge integrity, independent
  recovery and cleanup remain separate gates.'
tags:
- add-trait
- transcriptional-memory
- self-review
```
