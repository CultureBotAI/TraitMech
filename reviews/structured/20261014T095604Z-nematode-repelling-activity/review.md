# Adversarial review of nematode-repelling activity

- Review: 20261014T095604Z-nematode-repelling-activity
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-14T09:37:17Z
- Finished UTC: 2026-10-14T09:56:04Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Supports one bounded microbial repellence capability. No actionable defect found in reviewed final content; two OPEN discussions retain hierarchy and source/mechanism limits.

## Scope And Provenance

One complete new record and its maintained/generated owners; not whole-corpus scientific review.

Selection: One exact new trait, no sampling.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f031729ba146bec9befd12686507b1df13594d8d.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| traitmech:000725 | data/traits/physiology/nematode_repelling_activity.yaml | maintained | nematode-repelling activity |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate -s src/traitmech/schema/traitmech.yaml --target-class TraitRecord data/traits/physiology/nematode_repelling_activity.yaml | passed | True | traitmech:000725 | Actual maintained command passed; deterministic corpus diagnostics are not corpus-wide scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/validate_strict.py data/traits/physiology/nematode_repelling_activity.yaml | passed | True | traitmech:000725 | Actual maintained command passed; deterministic corpus diagnostics are not corpus-wide scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/validate_history_links.py history/records/nematode_repelling_activity | passed | True | traitmech:000725 | Actual maintained command passed; deterministic corpus diagnostics are not corpus-wide scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/verify_snippets.py --record data/traits/physiology/nematode_repelling_activity.yaml --out /tmp/traitmech-repellence-checks-20261014/native-record.tsv | passed | True | traitmech:000725 | Actual record CLI: Pradel VERIFIED; Prakash NOT_IN_ABSTRACT, separately matched in its own Discussion. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python -m pytest -q tests/test_add_nematode_repelling_activity_trait.py -k 'not source_receipt' | passed | True | traitmech:000725 | Actual maintained command passed; deterministic corpus diagnostics are not corpus-wide scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python -m pytest -q tests/test_add_nematode_repelling_activity_trait.py tests/test_readme_artifacts.py | passed | True | traitmech:000725 | Corrected README prose count and new writer tests pass. Earlier focused run retained one stale-count failure and 60 passes; it is not misreported as a pass. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/ruff check src scripts tests | passed | True | traitmech:000725 | Actual maintained command passed; deterministic corpus diagnostics are not corpus-wide scientific review. |
| just audit-proposals | passed | True | traitmech:000725 | Actual maintained command passed; deterministic corpus diagnostics are not corpus-wide scientific review. |
| just ground-predicates | passed | True | traitmech:000725 | Actual maintained command passed; deterministic corpus diagnostics are not corpus-wide scientific review. |
| just ground-nodes | passed | True | traitmech:000725 | Actual maintained command passed; deterministic corpus diagnostics are not corpus-wide scientific review. |
| just audit-graphs | passed | True | traitmech:000725 | Actual maintained command passed; deterministic corpus diagnostics are not corpus-wide scientific review. |
| just audit-graph-protein-taxa | passed | True | traitmech:000725 | Actual maintained command passed; deterministic corpus diagnostics are not corpus-wide scientific review. |
| just audit-predicate-domains | passed | True | traitmech:000725 | Actual maintained command passed; deterministic corpus diagnostics are not corpus-wide scientific review. |
| just check-biolink-coverage | passed | True | traitmech:000725 | Actual maintained command passed; deterministic corpus diagnostics are not corpus-wide scientific review. |
| just audit-snippets | passed | True | traitmech:000725 | Actual maintained command passed; deterministic corpus diagnostics are not corpus-wide scientific review. |
| just gen-discussions-data | passed | True | traitmech:000725 | Actual maintained command passed; deterministic corpus diagnostics are not corpus-wide scientific review. |
| just gen-qc-dashboard | passed | True | traitmech:000725 | Actual maintained command passed; deterministic corpus diagnostics are not corpus-wide scientific review. |
| just gen-pages | passed | True | traitmech:000725 | Actual maintained command passed; deterministic corpus diagnostics are not corpus-wide scientific review. |
| just gen-priority-dashboard | passed | True | traitmech:000725 | Actual maintained command passed; deterministic corpus diagnostics are not corpus-wide scientific review. |
| just qc | passed | True | traitmech:000725 | Actual maintained command passed; deterministic corpus diagnostics are not corpus-wide scientific review. |
| just validate-history | passed | True | traitmech:000725 | Actual maintained command passed; deterministic corpus diagnostics are not corpus-wide scientific review. |
| just validate-products | passed | True | traitmech:000725 | Actual maintained command passed; deterministic corpus diagnostics are not corpus-wide scientific review. |
| just verify-proposal metpo_traitmech_v601 | passed | True | traitmech:000725 | Actual maintained command passed; deterministic corpus diagnostics are not corpus-wide scientific review. |
| just robot-validate-proposal metpo_traitmech_v601 | passed | True | traitmech:000725 | Actual maintained command passed; deterministic corpus diagnostics are not corpus-wide scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/audit_canonical_examples.py --no-resolve | passed | True | traitmech:000725 | Canonical-example shape audit used --no-resolve, not live taxonomic validation; no examples asserted. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/run_trait_graph_audit.py --verify | passed | True | traitmech:000725 | Actual maintained command passed; deterministic corpus diagnostics are not corpus-wide scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/audit_history_records.py --base 55407337d8572f15d01f47bf6c9a99abc05d264a | passed | True | traitmech:000725 | Actual maintained command passed; deterministic corpus diagnostics are not corpus-wide scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python -m pytest -q --junitxml=/tmp/traitmech-repellence-checks-20261014/pytest.xml | passed | True | traitmech:000725 | 4637 tests passed with no failures, errors or skips. |
| template-format | passed | True | traitmech:000725 | Expected ordinary diagnostic: only the ROBOT directive header trailing empty cells. Not an unqualified whitespace pass. |
| template-scoped | passed | True | traitmech:000725 | Only this inspected template exempts trailing empty cells; global Git settings unchanged. |
| other-whitespace | passed | True | traitmech:000725 | All other committed paths pass the ordinary whitespace check. |
| products | passed | True | traitmech:000725 | All 1119 prior records, including protected spore germination, and prior history/reviews/proposals/embeddings/templates/baseline are byte-preserved. Old trait-page changes are footer-only except the phenotype child link. Parsed RDF uses real w3id hierarchy and definition annotations. |
| browser | passed | True | traitmech:000725 | 1440/390 px browser checks pass: two quotes, two discussions, one history, local identifier, working hierarchy/browse navigation, 1120 count and loaded coverage image. Eight screenshots visually inspected; no overflow or page errors. |

## Scientific And Domain Assessments

### Microbial actor and active movement endpoint

identity: supported. Targets: traitmech:000725.

Repellence is distinct from lack of attraction or relative preference alone. The definition does not require killing, feeding, infection or a shared chemical mechanism.

### Two primary behavioral studies

evidence: supported. Targets: traitmech:000725.

Initial lawn entry then leaving, acute reversal and pure-compound negative chemotaxis support the capability. Condition-, recipient- and strain-specific assays are not pooled into a universal response.

### Broader parent and local fallback

grounding: supported. Targets: traitmech:000725.

Phenotype is broader. Deprecated microbial chemotaxis is not equivalent. Ignored-inclusive novelty and reservation checks support this bounded local proposal; no exact coupled migration identified.

### Direct sections versus native abstract status

provenance: supported. Targets: traitmech:000725.

Both quotes are verbatim; full-text verification is not mislabeled native VERIFIED. Definition annotations exclude the second paper bibliography; actual figure and review limits are preserved.

### Guarded writers and native generated artifacts

consistency: supported. Targets: traitmech:000725.

Fail-closed drift/replay, schema, full tests, QC, history, RDF and responsive page checks pass. Prior records and immutable bundles remain byte-preserved.

### Mechanism, host range and protocol limits

completeness: unknown. Targets: traitmech:000725.

Chemical versus mechanical cue, varied bacterial cues, headspace protocol discrepancy and relative-choice limitations remain unresolved. No common mechanism, canonical examples, universal nonlethality, field efficacy or safety is established.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| source-0 | DOI:10.1073/pnas.0610281104; Scientific Abstract; /html/body/div[2]/div[2]/div/div[1]/div/div[2]/main/article/section[2]/section/section[1] | supports | Pradel et al. 2007, PMID:17267603, PMCID:PMC1892944, scientific Abstract; exact normalized PMC match and native VERIFIED. C. elegans denotes Caenorhabditis elegans. Own Results and actual Figures 1-4 distinguish initial entry followed by leaving Serratia marcescens lawns from absence of attraction. A swrA insertion mutant shows reduced lawn leaving but similar multiday killing; reduced avoidance is not loss of pathogenicity. Purified serrawettin W2 on E. coli OP50 lawns and acute drop-induced reversal are separate assays. The 16-hour bacterial-lawn endpoint, 60-minute supplemented-lawn endpoint and acute reversal are not one exposure. Chemical recognition versus a mechanical surfactant cue remains unresolved, and other bacterial cues can contribute. Serratia swrA is not the similarly named Bacillus motility regulator. |
| source-1 | DOI:10.15252/embj.2020106938; Discussion, first paragraph, own-study result; /article/body/sec[3]/p[1] | supports | Prakash et al. 2021, PMID:34086368, PMCID:PMC8246062, Discussion first paragraph, own-study result; directly matched JATS, PMC and publisher text. Native NOT_IN_ABSTRACT is retained, not relabeled VERIFIED. This is its own experiment, not a citation of Pradel. P. aeruginosa denotes Pseudomonas aeruginosa. Figure 1A-B measures PA14 lawn occupancy over 12 hours. Pure 1-undecene gives negative chemotaxis and omega turns in distinct Figure 2 and Appendix S2 assays. PA14-versus-undA odor choice establishes relative preference, not by itself repulsion or complete loss of bacterial repellence. Peer-review reply page 14 reports reversals but no complete lawn leaving after 1-undecene on OP50; the alternative adjacent-lawn crossing assay is not eviction from an occupied lawn. Roaming or higher mean square displacement alone is not directional avoidance. Recipient sensory genetics is not a microbial causal pathway. |
| content | data/traits/physiology/nematode_repelling_activity.yaml; Complete new record, guarded writer, tests, proposal, history, verification sidecar and generated diff. | supports | One microbial capability eliciting active nematode movement away. Own microbial taxis, absence of attraction, relative food preference alone, paralysis, killing, trapping, feeding and hatching are not substitutes. No organism-level disjointness from attraction or lethality. |
| ontology | data/raw/metpo.owl; Pinned/current releases, explicit editor and six TSV owners; existing nearby traits. | supports | Phenotype METPO:1000059 below quality METPO:1000188 is broader. Deprecated chemotaxis METPO:1000062 has no replacement/consider in inspected ontology and is not an exact counterpart; not revived or mapped. Explicit editor has 31 metadata triples and no imports. Pin unchanged. |
| novelty | research/traits/physiology/nematode_repelling_activity-source-verification.json; Ignored/hidden current copies, retained regular-file history, pending changed blobs and selected upstream owners. | supports | 188 locations, 143 retained heads, 23435 TraitMech and 5815 CommunityMech unique regular blobs; 719 unique path/text variants assessed. Remote: 11 open/draft PRs, 783 changed blobs, 587 selected owners and 21 matched files assessed. CeMbio member preference is not whole-consortium repulsion. Two decimal embedding hits and 857 broad editor-envelope occurrences are not competing reservations. No exact synonym/node/parent-gap migration found in bounded scope. |
| provenance | research/traits/physiology/nematode_repelling_activity-source-verification.json; Exact snippets, source sections, actual figures, supplement/reply checks, native CLI and notice receipts. | supports | Pradel is definition authority; Prakash reports its own experiment. The 18/21-word quotes match scientific Abstract and Discussion respectively; native VERIFIED/NOT_IN_ABSTRACT remain distinct. Prakash figure URL 404s were helper construction errors, corrected using exact published links. Bounded metadata/notice checks are not comprehensive clearance. |
| products | reports/proposal_citation_audit.tsv; Native gates, parsed OWL, byte preservation and responsive browser checks. | supports | Final required checks pass. RDF triple counts {'classes': 15, 'merged': 12628, 'reasoned': 12632}. Only Pradel and local record annotate the definition. README counts agree after the detected prose fix. Pinned CLAW 645 blobs verified; exact configured embedding inputs absent, so embeddings retained. |
| history | history/records/nematode_repelling_activity; Minting timestamp and append-only CREATE history. | supports | Observed acceptance at 2026-10-14T09:11:26Z precedes CREATE. Actor codex, GPT-5 and LLM assistance are explicit. Status remains PROPOSED, not human-reviewed. |
| publication | /tmp/traitmech-repellence-publication-20261014/accepted.json; Fresh local reservation scan and live remote heads/body/state guards. | supports | 189 current locations rechecked; owned hits separated, no conflict identified. |

## Limits And Additional Notes

- Author self-review only; exact-head external review, CI, queue and landed-tree verification remain separate unfinished publication gates at this timestamp.
- Own source sections and selected figures/supplement/replies were inspected, not all raw data or every figure. Prakash S3/table coverage is textual; reply pages 14 and 30 were visually checked.
- Compound production/gene presence is insufficient for organismal repellence. No universal host response, common mechanism, canonical taxonomy, safety or field efficacy.
- Prakash native NOT_IN_ABSTRACT is retained despite direct Discussion matching. Pradel publisher 403 and bounded correction/retraction searches are not comprehensive notice clearance.
- Canonical-example audit used --no-resolve; no canonical examples or proteins asserted.
- Known ignored/hidden copies included; lost ignored/untracked history, symlinks, submodules, arbitrary archives and unchanged pending PR files are not reconstructed. Allocation is not atomic; discovery is not exhausted.
- Earlier focused run found one stale README prose count; corrected before checkpoint and passing targeted/full reruns. No unresolved test failure is hidden.
- Exact configured embedding inputs absent; existing embeddings retained. Required empty ROBOT cells use a path-scoped whitespace exception.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T095604Z-nematode-repelling-activity
kind: record
repository: CultureBotAI/TraitMech
title: Adversarial review of nematode-repelling activity
started_at: '2026-10-14T09:37:17Z'
finished_at: '2026-10-14T09:56:04Z'
reviewer:
  identity: codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Source-based author adversarial assessment, not independent-agent
    or human review.
skill: .claude/skills/add-trait/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Supports one bounded microbial repellence capability. No actionable defect
  found in reviewed final content; two OPEN discussions retain hierarchy and source/mechanism
  limits.
source:
  git_revision: f031729ba146bec9befd12686507b1df13594d8d
  state: working_tree
  inputs:
  - path: .claude/skills/add-trait/SKILL.md
    sha256: c504f33f74f4a774258737ad08196fa858b2ee41ceefe85ad68d2209f2eee59f
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
    sha256: d29d08f3af74fb2acdd9125002f8571f68b2888230cd6253bfa9886cb7f29b4f
    role: context
  - path: app/dashboard/priority.html
    sha256: a41cb5b0599bd431ca53f043a8937b882bb73c606be8c24be83a9c19b51a1653
    role: context
  - path: app/dashboard/priority.json
    sha256: cb7384a345395877fbfd899c608b8a860f4fc35ce0b59aa5f768aade8a53ed80
    role: context
  - path: app/discussions/data.js
    sha256: 56673c13c483c64c8dfa89b8932b45a3fdc648bcdc2c8b1cecbd7b297becbf96
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
  - path: dashboard/index.html
    sha256: 1621610f96814523d0db4a0aa0b9ddb8e06e8ed1b50a7ca6fcdc36fad7f697bf
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
  - path: data/traits/ecology/fungal_nematophagy.yaml
    sha256: 7b1fd886e9ceb636abe8ab7a6ef857e59f98cdacd71293a740d1fc3fde05d3d3
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
  - path: data/traits/ecology/kin_discrimination.yaml
    sha256: a7592ae2262d91e3cc704b8406346b5c4c25570181f2040392e0bffee5b653a7
    role: context
  - path: data/traits/ecology/mutualism.yaml
    sha256: 7247ae4be59ce2eb7f1cc9d7303e1a338af82cd49d255c60aa1442f6dc1c48a3
    role: context
  - path: data/traits/ecology/nitrogen_fixing_symbiosis.yaml
    sha256: d4d85f1d5e370d5862b086ae52a716dee3fc5f8880639bffa4e2dff65e9d1574
    role: context
  - path: data/traits/ecology/nutritional_fungal_mycoparasitism.yaml
    sha256: 73cd69371a6be1067cd0177d442942445ec078cdddf37e250a42ff4e7682a901
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
    sha256: 2cba0abb6974aaa8d8f58114e4888ecece16c3ce2e8f8c459c9ca3f95e3917ae
    role: context
  - path: data/traits/morphology/fungal_adhesive_knob_trap_formation.yaml
    sha256: d831c127afa8763deab1e0a98c717382db6ecfac61ab98dbc9cdd735091725d5
    role: context
  - path: data/traits/morphology/fungal_adhesive_net_trap_formation.yaml
    sha256: 3692b5f5bed55ecdf5ccff262c8bc942c8989b19d33f83f398611f1dac069709
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
    sha256: b842af423a466d77ee9e0ef971be60ed92328cb1bc1532187bd2f2ceb57dd0d8
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
  - path: data/traits/morphology/fungal_nematode_trap_formation.yaml
    sha256: ff9bd6f9da47daa1ba2bf31ac7e2bd178119d76520acc26a9ab021e4c448f5b8
    role: context
  - path: data/traits/morphology/fungal_nonconstricting_ring_trap_formation.yaml
    sha256: 0f1246f40b4f2057db4f8ac03608e16f8ddf61279bd33d4a870ad1cce32ed0ff
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
  - path: data/traits/physiology/behavioral_habituation.yaml
    sha256: 1ca1d5d7ab7d479d42d0cc725272cffbfba09b3bacc3cc47d8fc6c81e36a0863
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
    sha256: 6fd8d2f12c0ef870bac46ee525f67dec06fbee04d9e0dad03b02df888f8b1f49
    role: context
  - path: data/traits/physiology/er_phagy.yaml
    sha256: eb4d35c8b13e79c916739e13a444c70bfb4bc146951c2c0b28bab3297854a840
    role: context
  - path: data/traits/physiology/exocytosis.yaml
    sha256: 419001cc5f36f27946299f1ac88e532fdb83c0e0f2be2d3ccedb43e60fa41a6f
    role: context
  - path: data/traits/physiology/extracellular_membrane_vesicle_production.yaml
    sha256: 92ca3c1690f09287dc914e597ada9d3d7ac70cc12f50fa52c2a8dd60c6bc12b2
    role: context
  - path: data/traits/physiology/extracellular_trail_based_spatial_memory.yaml
    sha256: 1fbb6c05fd9928cecf32e02604b4859b846fd7eafdc0897f49aed578d2da2b4e
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
  - path: data/traits/physiology/lethal_nematicidal_activity.yaml
    sha256: d78f028714561c4ae3f7aa9189a10cf43c8cee3d82e9999511d7e41788c4496f
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
  - path: data/traits/physiology/nematode_attracting_activity.yaml
    sha256: f14b2267ba41ba977659b0987f2a6eb9ae5883083408cecf88baec5724556258
    role: context
  - path: data/traits/physiology/nematode_egg_hatching_inhibitory_activity.yaml
    sha256: a81169517b303921c51a46feaf81257c7acf8eeaddaf40271c794e3ff360596a
    role: context
  - path: data/traits/physiology/nematode_egg_hatching_stimulatory_activity.yaml
    sha256: c88e8b6c7b30ba6215ab23cd7e20fdf0349192a43ce2e210a711f8b981435c95
    role: context
  - path: data/traits/physiology/nematode_repelling_activity.yaml
    sha256: f3d2243fb03220651479607c556f5d4e33c6defd6aa7dd56dcb5e12426eda82f
    role: target
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
  - path: data/traits/physiology/reversible_nematode_paralyzing_activity.yaml
    sha256: 8d362ad979cb65d806f2a76958753147f832caf656246469a206390a85d8362a
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
  - path: docs/record-review-profile.md
    sha256: cac714488cad03263ca3847737d5f70d174d40b5be677a09e0c1d9c814d9bc6a
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: history/README.md
    sha256: f795a191e17978454a8bb80da91ed6873a9405a240e6e5758837dd9bdc3b5c07
    role: context
  - path: history/records/nematode_repelling_activity/2026-10-14T091602Z-codex-145498.yaml
    sha256: 059a4efea230964a99db696f3b4272a8c9d4d4a73adb746d258225945fc3a496
    role: context
  - path: justfile
    sha256: e6047ea612115a6a78d100b281483ba824c860c3def59bcd0d40e7fb56b3526a
    role: context
  - path: pages/browse.html
    sha256: b41bddc0e8a43f3a3f7ae48f2a22b87af35d8d7ca9b2509e7770079bc0dbc5c3
    role: context
  - path: pages/category/ecology.html
    sha256: c7bdc53dde96716061186d1c73b90e01fd4714fefec10bb5df8e76e14f1a2511
    role: context
  - path: pages/category/environment.html
    sha256: 7ec21a0ea23bddb759c3bd60e9278a6d0c1f49d68e29a9c071e6802816e09d5f
    role: context
  - path: pages/category/genomics.html
    sha256: 2fdd66f4e32605ff051684eb751f26f926b20cec15749d9293af9a3d0a4c5e5b
    role: context
  - path: pages/category/metabolism.html
    sha256: cf3f410875a90a6addfad99386b326160215587652683a5ec0a4c27247bfc313
    role: context
  - path: pages/category/morphology.html
    sha256: 68dae2b2276a4e1c42c486d19373c90a1f1e9051441cb6921998764c9b87940f
    role: context
  - path: pages/category/observation.html
    sha256: ea94033cea2e3d344f8688551482d6a4030cfbb6bd9b67b9816ab05a105bd5f3
    role: context
  - path: pages/category/other.html
    sha256: 0c6db8ac01d7620bfe5bb78972db7291b640038f61667119cf9d31f3d949cae1
    role: context
  - path: pages/category/physiology.html
    sha256: cc216b42303fa6f0fb0e79f4d8c46e35ccecd93696aebabd7632e0d7d2f91124
    role: context
  - path: pages/category/quantitative_property.html
    sha256: 79d4646ce4a4d33d0069f36c0622054d06a0cb2cfe9aeddade96117974cf2ec2
    role: context
  - path: pages/category/upper.html
    sha256: a50148d54a6f34d7de7e6e6f0787554af6a6ec336be81b2f48b52e1399de9dc4
    role: context
  - path: pages/graph.html
    sha256: f17cef09ee2f41781d07e489e36364b3df7953c28c48b186a131487a150a5071
    role: context
  - path: pages/index.html
    sha256: 95b7b250346ae9e29e4591ef4e0a4b89ca7c2e855e0ab1398ca6f84317c78ac0
    role: context
  - path: pages/traits/ecology/animal_pathogen.html
    sha256: bc274feef3500539da10b006c32385d6f4c01dd776088d74ab922a9dd84a3ee2
    role: context
  - path: pages/traits/ecology/bacterial_cannibalism.html
    sha256: d7bb4d9a234df16d28c900998d5557228b638558c68990fec632919d47417478
    role: context
  - path: pages/traits/ecology/bacterial_mycophagy.html
    sha256: 9f9d73cbf5741f2ddaf1df888727f45976e865c02040aff904e754df03aa6ff3
    role: context
  - path: pages/traits/ecology/biofilm_formation.html
    sha256: 50ed4b3852f68c563e91a7eb7a578bccb3c8795c1d22a4d38709ddfa0bfa1fc1
    role: context
  - path: pages/traits/ecology/biosafety_level.html
    sha256: d5f08032cf9e21e909b456b5db5bfcf58f258ec89c33428a75166d17c05aa30e
    role: context
  - path: pages/traits/ecology/biosafety_level_1.html
    sha256: d1dec2cf14b3c468915159425fd04e28bce5ccc59e89f8a993419e0794504696
    role: context
  - path: pages/traits/ecology/biosafety_level_2.html
    sha256: 52e168237d1eb1c8eea6714596245c8a8820c42c74c8484d00a4fb1d66ade1cd
    role: context
  - path: pages/traits/ecology/biosafety_level_3.html
    sha256: 8c6bd5ce3e5116c6ef8d9b01ec09608168f0b43426d9f01249ae091552d22ee4
    role: context
  - path: pages/traits/ecology/biosafety_level_4.html
    sha256: ebafbbd717d2278e084357f9f22ed5780a810be1ed9677e06ed150575fa8bc0f
    role: context
  - path: pages/traits/ecology/biosafety_level_5.html
    sha256: 3d377ec462ded2b76bd7465f17e4adc89bb0bcfb4d678dada4a6926315e52eb8
    role: context
  - path: pages/traits/ecology/collective_bacterial_predation.html
    sha256: 474f25948ea629f44b90c21be76c3a2c9a874ea3351e1528933ffab462311f16
    role: context
  - path: pages/traits/ecology/commensalism.html
    sha256: 2ce82a56c1ac9443eeb1fb8beaf0f50c19aadf3d82f484b9964fb16734fefe88
    role: context
  - path: pages/traits/ecology/cytoplasmic_bacterial_predation.html
    sha256: 31ac9ab964d8426299853e943815c94249226a3de3d3ff28afea3dddc804bcfc
    role: context
  - path: pages/traits/ecology/endophytic.html
    sha256: 5ee398ba40695c75b1b84ad951bbf330ad52ba258a80094d4f406b1b54270299
    role: context
  - path: pages/traits/ecology/endosymbiosis.html
    sha256: e247185f98689ea3f57ce7750686909de56b79c2b329f6a7b899c7710fb22841
    role: context
  - path: pages/traits/ecology/epibiotic_bacterial_predation.html
    sha256: ff7c60e049cc3e600bc44399d8a7f2c666bbea87bbb84c707a132906ead1059d
    role: context
  - path: pages/traits/ecology/epiphytic.html
    sha256: eb2ec941ad5fa9f4328b249e9aa6c1a520cf344478b5fb307b2143506594d60a
    role: context
  - path: pages/traits/ecology/free_living.html
    sha256: 06eb8cc02f017fee2e4f5cdbf28a455e97634b966af21952a66237477f9c412b
    role: context
  - path: pages/traits/ecology/fungal_nematophagy.html
    sha256: 5aa5c73def7d11174e9e476f99c9efbbe46103af3c293adc307f7239cdb2a6f6
    role: context
  - path: pages/traits/ecology/gut_associated.html
    sha256: db8b5a9af302ae99685c18814788a9966757ca4715cdd21e9c84bbba2d37f89a
    role: context
  - path: pages/traits/ecology/habitat_association.html
    sha256: 45fe32af6c044954e02087518e5845e1f8aa9734ccaed2fc9636b1b7625355ef
    role: context
  - path: pages/traits/ecology/host_associated.html
    sha256: 37ed49ef0ead5d6d34ac1a103bfaf3e7f88c3e28bd7b04863336b293cd0b689b
    role: context
  - path: pages/traits/ecology/human_pathogen.html
    sha256: c8e7dd9a5c7237eb27ca685b4d440563aa30c14b3b9718dc72b485859ede8dd5
    role: context
  - path: pages/traits/ecology/ixotrophy.html
    sha256: 81cd095fc1429b7536bf80fbcdb2c77a6a5df3a7d893a4fcf73caff40cf4ecfd
    role: context
  - path: pages/traits/ecology/kin_discrimination.html
    sha256: 7946186d3833be8db515e856c4af305c2ad49b935a765e7bb8537cb45ca634b4
    role: context
  - path: pages/traits/ecology/mutualism.html
    sha256: 66b0c244daaeb064f67fdf37a3db96be689e931bd301ae31cdc83cb73b691f30
    role: context
  - path: pages/traits/ecology/nitrogen_fixing_symbiosis.html
    sha256: 902de53d904600eef51be72fb318b2e33878393ada054d10791f0bcbdcd0c96e
    role: context
  - path: pages/traits/ecology/nutritional_fungal_mycoparasitism.html
    sha256: 2cc3d7a9a4da10ef1679121046ff63a576f79fe8ee7b08644710fd2b04575d24
    role: context
  - path: pages/traits/ecology/opportunistic_pathogen.html
    sha256: 78abf8ee23501d7d495c0c8643bea61e96d68899ce8340ded3ee37de676c45b8
    role: context
  - path: pages/traits/ecology/parasitism.html
    sha256: d3aad4bbb2f029764d4bbb90e06773101711cbc038469eadb37e8718f85801b4
    role: context
  - path: pages/traits/ecology/pathogenic_to_host.html
    sha256: ed205d4034d6dda21c0bce871a03b49241a09329637b91775914b1e246764240
    role: context
  - path: pages/traits/ecology/periplasmic_bacterial_predation.html
    sha256: 48a1a93d47fa3dd5efe49224a3a1671b768ca993ec60689439b15e079bf6b2de
    role: context
  - path: pages/traits/ecology/plant_pathogen.html
    sha256: 265cf5d095ce651a0e10b1fdf4b8a938cc9a35cb3720364bc8c995949e7a02f7
    role: context
  - path: pages/traits/ecology/predatory_bacterium.html
    sha256: 317c04ea22edbc22aaa4ce9257f30642446f2977f5e69daa580c302146a9e1e0
    role: context
  - path: pages/traits/ecology/rhizosphere_association.html
    sha256: 9c47807a15b7778270d9fa3b1177af7831d91f786c03c1a814bb18af5a442303
    role: context
  - path: pages/traits/ecology/saprotrophy.html
    sha256: 50d6b6791a5d7d23d8377f0e6485dd249a40b72f0445a09aef540d93d62fa13b
    role: context
  - path: pages/traits/ecology/soil_dwelling.html
    sha256: 16c7f58a65510b634a42d5d0cf181ad56d1e06af7c2daf1d6cd2175ec01225eb
    role: context
  - path: pages/traits/ecology/symbiosis.html
    sha256: 0ef5af37737b860805b6d9437e86d41ef1f9afc3da876a874c0f526e313d771c
    role: context
  - path: pages/traits/environment/acidophilic.html
    sha256: 27a6de5bd7ab49e86e46456a4b3ebe6ea3ad7981f28732c55d38bba5b0a45e33
    role: context
  - path: pages/traits/environment/acidotolerant.html
    sha256: bb4e8ef9413a807453a9f532b17a0b00eeff10ff22065276e2cdcf6fdb464cef
    role: context
  - path: pages/traits/environment/aerobic.html
    sha256: 4a4d9c16d17ad56370fdb2136bb0f249210c120b0aa36fb1c48b7ad9167ba6cc
    role: context
  - path: pages/traits/environment/aerotolerant.html
    sha256: c06fd8a06acaeced49b4272fc343228f38a46f752ef76c4bd0a1f3ab1372a6b4
    role: context
  - path: pages/traits/environment/alkalotolerant.html
    sha256: dcf4c6be9f348a21f1815248edbc01ec5e17e7972c6e84ed3dccbe1663334897
    role: context
  - path: pages/traits/environment/alkaphilic.html
    sha256: cc77207f0d7e71c185a88cd410bff6ae34d4928701e0165c3c356edefa9e891d
    role: context
  - path: pages/traits/environment/anaerobic.html
    sha256: fb33090e2c8708214098054faa4e4966394fcd819e4f8591dafce961fb465755
    role: context
  - path: pages/traits/environment/arsenic_tolerant.html
    sha256: 24a2422cfb16d7b653e87c0b51736477e79f9f58f70b13a1f0db502e29cc90b5
    role: context
  - path: pages/traits/environment/cadmium_tolerant.html
    sha256: 5b4761a1220134e50d186cb329051d50a7dbe73ab8cfa8f2d7814696c5ca2589
    role: context
  - path: pages/traits/environment/capnophilic.html
    sha256: 7289f1c74b10057d6fec4c9032638075db506e592690600d15ace910b73a7732
    role: context
  - path: pages/traits/environment/cobalt_tolerant.html
    sha256: 1d1a6f7beebb0d2b30862bb4b0c9ea64ec3a89a38885152afe33fab75221a13f
    role: context
  - path: pages/traits/environment/copper_tolerant.html
    sha256: bcc0d83fb9242361b558986c76ce1d6ab2208a84faa08ab1a6a9c1a22d4e9f9b
    role: context
  - path: pages/traits/environment/delta_phenotype_with_numerical_limits.html
    sha256: 5ddb028538a9b0b248efa142d3275cde93ea4a55fae8790e22d7272177465cc0
    role: context
  - path: pages/traits/environment/desiccation_tolerant.html
    sha256: 7c1e2daf9392e18bc4a3a32d66d197579b57892b9eb895e8af0a999db5c435c0
    role: context
  - path: pages/traits/environment/euryhaline.html
    sha256: c1bf8fd90fe9c4ac9096cb74e20d3611ee34a40442b3ffd29f10124e0d81189d
    role: context
  - path: pages/traits/environment/extreme_hyperthermophilic.html
    sha256: 72790dba4a072fcda9d21be0c5dd799b5693785f18493405540222b266f246aa
    role: context
  - path: pages/traits/environment/extremely_halophilic.html
    sha256: f33ae147e930a992bf1065a7476ee7efe15f173e39720c4b42ed81854de7afc8
    role: context
  - path: pages/traits/environment/facultative_oxygen_preference.html
    sha256: f0ed03b2861aa19911121ed30f154fcab2dff9913fddcb9a26e1f12fc7e7315c
    role: context
  - path: pages/traits/environment/facultative_psychrophilic.html
    sha256: 96bc456ff1c57866fefd78c0c238a8ffd2f1d94dbd6c3f882a8a2741f1cd2883
    role: context
  - path: pages/traits/environment/facultatively_acidophilic.html
    sha256: 8d89b66ea3b8831e4d59b432ed7b38dabab7dc41d3011723cc419aee53c65855
    role: context
  - path: pages/traits/environment/facultatively_aerobic.html
    sha256: a38443631e58130c8cba659a2007e006774084a9c304e0adb445ebb65d7e6cb7
    role: context
  - path: pages/traits/environment/facultatively_alkaphilic.html
    sha256: 660a0bd68deac1a9b9532d931047a72e385a5fd53c2e0f2f0236aa1728879a2f
    role: context
  - path: pages/traits/environment/facultatively_anaerobic.html
    sha256: 482d6aebaa5b3fa59f3c7369b3ff0ee5d3b15dde3f9a2ebace686e2393f0e1fe
    role: context
  - path: pages/traits/environment/growth_range_phenotype_with_numerical_limits.html
    sha256: e529476b4477d0476edb0e925b8bbc28efda13d2490c02c9b10f303dc4b5e367
    role: context
  - path: pages/traits/environment/haloalkaliphilic.html
    sha256: 125aa0e2930618137db003066114fc8bf9d2f3912eda48934fdad844aba38040
    role: context
  - path: pages/traits/environment/halophilic.html
    sha256: ca8907647d780f7caf3bf697e0e7cf56aa7f234e1ab3bf008eb78cd30521bc7b
    role: context
  - path: pages/traits/environment/halophily_preference.html
    sha256: 5d7db3474449d511ccea43a2a075a541b14b354f99f7e335bf4fac2db1c5e043
    role: context
  - path: pages/traits/environment/halotolerant.html
    sha256: f8a0ca63c3d4944a2da4a357d61b1b650db4ac70d8acd86c51990f174756abca
    role: context
  - path: pages/traits/environment/hyperthermophilic.html
    sha256: d021ca2bb178c9026a69f405c63ee10c5f9e16779452ad2a06fca3ac2ce3dbc8
    role: context
  - path: pages/traits/environment/ionizing_radiation_tolerant.html
    sha256: f7c167d6f094aefd70d9aa2dd27792839f9c278876419dc7ed9d3446f60c7fec
    role: context
  - path: pages/traits/environment/mercury_tolerant.html
    sha256: f624db6381441d4917634c48a626566883b679af032dd68c8e2e4ad61768aebc
    role: context
  - path: pages/traits/environment/mesophilic.html
    sha256: c8fe5ed6ef3836782b5ba7bcd5e57b6d84c37fa5512b0c3eeb3b9bcf5ca6e651
    role: context
  - path: pages/traits/environment/metal_tolerant.html
    sha256: e3aafab47dff05f305c64330725d6cceeeba1180b278e271b81d89b594b2e38b
    role: context
  - path: pages/traits/environment/microaerophilic.html
    sha256: 7ba4c7bc4ed860c6c42468fd2a58b30a0fe47b0edfdee1e80ed9bdeca56a5803
    role: context
  - path: pages/traits/environment/microaerotolerant.html
    sha256: ad8b032d05214ff3b1b2c2ecb475c2a4984a1acc0d67c6542841fc8f2c5523f4
    role: context
  - path: pages/traits/environment/moderately_halophilic.html
    sha256: 8e419c06ad18b431034c4fe741f5dad2c1f55e992419184d00fbce7130e85421
    role: context
  - path: pages/traits/environment/nacl_delta.html
    sha256: 26604cc8db77f88f517e40bd8c8a1c0183fa2cd88f3b3f55f5ef65c72a0fd428
    role: context
  - path: pages/traits/environment/nacl_delta_high.html
    sha256: 27b3daa6e0bf0bede621fc52b8416d3ade8e12b36b9e0fabae1a54fe092972a1
    role: context
  - path: pages/traits/environment/nacl_delta_low.html
    sha256: ed08bca9285c09a5abc84c4d0ab02208388e12590ba08537b18902ec20fab0f5
    role: context
  - path: pages/traits/environment/nacl_delta_mid1.html
    sha256: 265df3009087cbf404ca2a1fd0284def2f67ef614be594dbb5f7964e8204731e
    role: context
  - path: pages/traits/environment/nacl_delta_mid2.html
    sha256: 077c12814d03a3d31b458fe8d3aff69bf864533a8cbae594644ed7a4a2a3264f
    role: context
  - path: pages/traits/environment/nacl_optimum.html
    sha256: eb30353e3f6d69df636b5c8f785ba9199a993f06cb700e198d26531ec0b06c0f
    role: context
  - path: pages/traits/environment/nacl_optimum_high.html
    sha256: e48e13ca1b478451e3ad02c813b035d0ecfb8127f069e3833573ad32c19f087f
    role: context
  - path: pages/traits/environment/nacl_optimum_low.html
    sha256: bf43e04cc87cb245b78a6d751956d08ae18c5ceb9c150bede10a7dcb6222eadb
    role: context
  - path: pages/traits/environment/nacl_optimum_mid1.html
    sha256: decd82745fa0e4a973e6c04fe789a34788757f830d99036cfecf29313e180787
    role: context
  - path: pages/traits/environment/nacl_optimum_mid2.html
    sha256: a54442c610fb8b53afad1527855f4d3181f84bf4eec370f5c0614631ee87429a
    role: context
  - path: pages/traits/environment/nacl_range.html
    sha256: 35841f5273b1eeb070e84a357f680b51b002c1f8629ba0dfec35d949325ef6f6
    role: context
  - path: pages/traits/environment/nacl_range_high.html
    sha256: 04d87a3eb7bf834448231c14125d577bbed89fde3ceb7f776d905169da647645
    role: context
  - path: pages/traits/environment/nacl_range_low.html
    sha256: d00425522ad052be40c219db493f065216a68062457a46afe162cf53220b20e4
    role: context
  - path: pages/traits/environment/nacl_range_mid1.html
    sha256: c33b5c08171f9e8cfe4d8641950e86ad0a1b11d51d24bc02d3779b0bcad5f684
    role: context
  - path: pages/traits/environment/nacl_range_mid2.html
    sha256: e3f2fd41e91968d8920bcb7c319daefa04f9c72d4a9a85f195b9eb3354bb2b13
    role: context
  - path: pages/traits/environment/neutrophilic.html
    sha256: 5e7b64b6f4511ecc083b7de10f09290f96236c0945a43cfedef8183ee1cd2f91
    role: context
  - path: pages/traits/environment/non_halophilic.html
    sha256: 5353764198932d1aff67e2ca6ef1a27d161f98e297908ce0a1c689f28e92a52c
    role: context
  - path: pages/traits/environment/obligately_acidophilic.html
    sha256: 3c892b3019ff85c5df726deb7120f3c2cbc98b6d350ca808455ca4a53c47ae73
    role: context
  - path: pages/traits/environment/obligately_aerobic.html
    sha256: 81407d08999994c2da201142c439aadaa906942776b546e574727d96477c9173
    role: context
  - path: pages/traits/environment/obligately_alkaphilic.html
    sha256: c02d05aede37cdd4b5da9cc7ee3c217f27ffb5988a551e5442728f19adcfbd20
    role: context
  - path: pages/traits/environment/obligately_anaerobic.html
    sha256: 9288be07a77f43037d71404eec88e6830661a5ff9915dc8f095bc6a63418a8c1
    role: context
  - path: pages/traits/environment/obligately_piezophilic.html
    sha256: 5154bd62adf72f26b71852507aa3f6e306a7d65e0ab1624d6f967f9d16c52655
    role: context
  - path: pages/traits/environment/optimum_phenotype_with_numerical_limits.html
    sha256: 65fa1d949bb3276dd46033bb63a2ec74b2f6b990fb0e2e40cfbd0666a0e2020f
    role: context
  - path: pages/traits/environment/oxygen_preference.html
    sha256: bc4851716c4f637a975b56ac4e8d39c19768d8305e2260276e420fe2235b3812
    role: context
  - path: pages/traits/environment/ph_delta.html
    sha256: b476ae4a285b1a98412d05c622298ff2b6b00890b59bd020b610f67275074109
    role: context
  - path: pages/traits/environment/ph_delta_high.html
    sha256: a87478eb09daacf9d34f91015a0a7620067a0b5a30b1aba441344d649c371009
    role: context
  - path: pages/traits/environment/ph_delta_low.html
    sha256: 48a2370000ff716887551621d0b40eebe350b5192abb2c1897ef50509b236aee
    role: context
  - path: pages/traits/environment/ph_delta_mid1.html
    sha256: 37fe915a1031d375b30110e3be95177053e8c3f6fc051a4cba75490e4ed29ed9
    role: context
  - path: pages/traits/environment/ph_delta_mid2.html
    sha256: 8fc28ab5557e74293ab6cdae43098f068472285684f248f8cc82377378a60911
    role: context
  - path: pages/traits/environment/ph_delta_mid3.html
    sha256: f989370f525e4689c2f2e3a3caac7158f0aed29dc6227e8ee070479405893bb6
    role: context
  - path: pages/traits/environment/ph_delta_very_low.html
    sha256: 091e79071c7d8bab2018d6ce230b57567fea78308ce449e5f35d5c5953bbd4c1
    role: context
  - path: pages/traits/environment/ph_growth_preference.html
    sha256: d49bbbba40db37b835a1c5ce54b39030b7566787e915db059017c92a704661a7
    role: context
  - path: pages/traits/environment/ph_optimum.html
    sha256: a154b475c311fff7bef283adc96f32f31fb980602548bd29d68522bbc014f16c
    role: context
  - path: pages/traits/environment/ph_optimum_high.html
    sha256: a40e532051732a6ab3b16f128d8b83d355d6ff35c6890d2f32eb4cdbcd173d89
    role: context
  - path: pages/traits/environment/ph_optimum_low.html
    sha256: 19af474860479607ff2d190668c6010062d0cf4bb453ab1a90488d2a03bac4eb
    role: context
  - path: pages/traits/environment/ph_optimum_mid1.html
    sha256: 499970761c08f26ca134d5bb4f162e0365734e10719b95bbb2cbc77821d8242a
    role: context
  - path: pages/traits/environment/ph_optimum_mid2.html
    sha256: c2edd48e53e6692cb9ad12404979f93206f54f823d9ff5fd129d04ea917e6abd
    role: context
  - path: pages/traits/environment/ph_phenotype_with_numerical_limits.html
    sha256: ca39f26281c35034ed6a1066c8ff8e5508cfc3749467a0a0fa339a2c55e0e0e1
    role: context
  - path: pages/traits/environment/ph_range.html
    sha256: 52cc69f3e6760c42cde6f4444170b6a0744207cfd4decd17373c73c39ca9d1e3
    role: context
  - path: pages/traits/environment/ph_range_high.html
    sha256: b1a63c26d7087799ffe0f4077cddd9ce1a829dea9629cb6a6aaf01d0c17fe016
    role: context
  - path: pages/traits/environment/ph_range_low.html
    sha256: 9e78f1070b467a7b52c52385e9a1b3477f20cebd1cae3eddeb72a6a6f1706276
    role: context
  - path: pages/traits/environment/ph_range_mid1.html
    sha256: f2363ba331f0866a2b41a43c63f55456077a1a0c1f40c03fd345553d76c0bdee
    role: context
  - path: pages/traits/environment/ph_range_mid2.html
    sha256: 15afa47509bbfa0cde03d8c4aec1ff62fab222ccbde9ed0dc1563997446c5ba3
    role: context
  - path: pages/traits/environment/ph_range_mid3.html
    sha256: 1693ff5078f2f52c852c7a22c215efa2b30cda2e0b26026c55f7d3d116a4e844
    role: context
  - path: pages/traits/environment/ph_range_very_low.html
    sha256: c4dd4ab5fcbef7b2cf00ea37266cd64bc616aa1d9a8b6b3dd5677d724e879c29
    role: context
  - path: pages/traits/environment/piezophilic.html
    sha256: f9fa94bf4a53158110297dc0f168b628ecfa2d2c9c347274f6aba915183f29ef
    role: context
  - path: pages/traits/environment/piezotolerant.html
    sha256: a47057cd0309e588dfbc294dae4c5a15c3839fe748200edfd8d697ddd51094a4
    role: context
  - path: pages/traits/environment/pressure_delta.html
    sha256: 148d50fc9ecd696b277a75623b0722db7b9c62b6e716a6ee7fbd633fe0d863b6
    role: context
  - path: pages/traits/environment/pressure_optimum.html
    sha256: acd7b14eadd9ed4316690b3d36f7d4600b2a54cd673bf04e0473b5e86081efc4
    role: context
  - path: pages/traits/environment/pressure_range.html
    sha256: 40a52880ecb5e69a3bbf05d1a4ca7497c4d4941f909b0889fbdf56311f2e6b7d
    role: context
  - path: pages/traits/environment/psychrophilic.html
    sha256: acca57a9beb237375b3ca2325eb6eaf76f06b3414656e2546f2052ed5fab3242
    role: context
  - path: pages/traits/environment/psychrotolerant.html
    sha256: beb3a9c1f57b679ca1826706f97ff3931bbce06bffe114c7be3864b9d8fdd7ba
    role: context
  - path: pages/traits/environment/radiotolerant.html
    sha256: f49fc4aeeca30a31dae7d70ca17a707efab4655a06d424ac07bf62791edaf1bd
    role: context
  - path: pages/traits/environment/salinity_phenotype_with_numerical_limits.html
    sha256: 112e2be88fd9533ecb03494121745d70346b83e4e9968ab89f990e09b0a9ce4e
    role: context
  - path: pages/traits/environment/slightly_halophilic.html
    sha256: 6c4aa74a96d534b87b576d0a2571237e6ec4ba07049f8c9afbefdee58774ebff
    role: context
  - path: pages/traits/environment/stenohaline.html
    sha256: 466514b72a812265ceaa722ed006cc5335b2b678af66017f0bb6c3de43d654da
    role: context
  - path: pages/traits/environment/strictly_anaerobic.html
    sha256: 77aa6a3cdc21be9c8c08ebb01b3950dafb3e16dc1bbbf75a518620adaa44f25b
    role: context
  - path: pages/traits/environment/temperature_delta.html
    sha256: 50f318956b38ad66808ffde0585654ab05bb62d547ed113faea91583aa20c496
    role: context
  - path: pages/traits/environment/temperature_delta_high.html
    sha256: 9cbbcd818317b4d24f2dff01b424d9e67782842322d0e0253399e7d06b727c17
    role: context
  - path: pages/traits/environment/temperature_delta_low.html
    sha256: 27cbbd561abc0bc088df738b3f1c8c94a53c015cbec50612546d246f28645ee9
    role: context
  - path: pages/traits/environment/temperature_delta_mid1.html
    sha256: 03d3228a78644804a3e6194489d9619c76bc3a43cf651e4f7ef87ff130fe845f
    role: context
  - path: pages/traits/environment/temperature_delta_mid2.html
    sha256: 7e8866d528f027a3c140e8c05f27c1460ea8b86ead4e7a09edf8160ef32e0691
    role: context
  - path: pages/traits/environment/temperature_delta_very_low.html
    sha256: 21a8657a9fb6b9f4e4979bbb942f4fd6ae649b4a27449a6a828d4e97a54487c0
    role: context
  - path: pages/traits/environment/temperature_optimum.html
    sha256: f9010eab48e55630f17a3d5972943b1fcc3d7ebba003b8b61abce91195dc23be
    role: context
  - path: pages/traits/environment/temperature_optimum_high.html
    sha256: 0074b5a374dec9307a89ec441fff15da9358fe606a2c3bd82cd0278ed85943e3
    role: context
  - path: pages/traits/environment/temperature_optimum_low.html
    sha256: 098d23ec4a1cf89729752a7d7861559740416d05e5d2211c8de28b69fa59eb1d
    role: context
  - path: pages/traits/environment/temperature_optimum_mid1.html
    sha256: e1dbaa5eeab93fb61169ec09d6c47698f6fe4fd11c4a364340a3bca1cce70590
    role: context
  - path: pages/traits/environment/temperature_optimum_mid2.html
    sha256: a2ede3f718ec2fae261b0f40481d78cb9556fb9dde6723181da16eca42fa7698
    role: context
  - path: pages/traits/environment/temperature_optimum_mid3.html
    sha256: 1ea7976e43c3b3e14abd4b73ac9b3d7014783b4190f950f3037d9ea5f964f189
    role: context
  - path: pages/traits/environment/temperature_optimum_mid4.html
    sha256: b5f472e9fe579f0545b64cffeb9570158b6ae471ad498e3f8d986ecd05af2011
    role: context
  - path: pages/traits/environment/temperature_optimum_very_low.html
    sha256: def395062d2ee7a13e3ab826571f7d2847dbe10f9aaba1dac881c0546a58e6a9
    role: context
  - path: pages/traits/environment/temperature_phenotype_with_numerical_limits.html
    sha256: fe24e9cbfd33ebf82fb85465a9ca2866d6ce27a201d8e075921cee992bab2e8a
    role: context
  - path: pages/traits/environment/temperature_preference.html
    sha256: 207e8acef65bb7464b16558e13623bc1bed8a0378e8b68ef09f8a3ca99c16a99
    role: context
  - path: pages/traits/environment/temperature_range.html
    sha256: 0c802156286c07e79a5437b78947162b0e24725abcb000ca76487fa3c1a1bf94
    role: context
  - path: pages/traits/environment/temperature_range_high.html
    sha256: 023f0409964b6d7750876eab0d2498e34adb1a9e6ecdda52556ab4f54091a812
    role: context
  - path: pages/traits/environment/temperature_range_low.html
    sha256: fa0ae8b9449dd98a39f30bb51c4969fc61e70a49b88a1d815523f86c94ac832d
    role: context
  - path: pages/traits/environment/temperature_range_mid1.html
    sha256: 07b62b80f9e595eafa7c2cb7d7f4f02a8a34cfc9ac3de92ad4b0112c5d1b6dcf
    role: context
  - path: pages/traits/environment/temperature_range_mid2.html
    sha256: c4e055c58aa2ed41149d170167d5691191c8b848117eaeda8bbeacace0db5492
    role: context
  - path: pages/traits/environment/temperature_range_mid3.html
    sha256: 408bc912b8a650e4e9abe8e46345e0f7bf9bc8641535fe6452d7103ef9b45788
    role: context
  - path: pages/traits/environment/temperature_range_mid4.html
    sha256: 77f348dd2a9bbd9797f933a2c11199e493ee911864fe500a951cd3781b6aac91
    role: context
  - path: pages/traits/environment/temperature_range_very_low.html
    sha256: 136b75a2d77c6fa6951936d9fb23e692752818018e5c367f2c479e513a4587c2
    role: context
  - path: pages/traits/environment/thermophilic.html
    sha256: 2e45ef0c71d51a4db5a005c8ce09a626da4472d73f44dc65bcfd17c76cef9436
    role: context
  - path: pages/traits/environment/thermotolerant.html
    sha256: 28dccc78f8711dde63fe5b3b8acc076ab7565a0750215a5a2e770e0025835c4e
    role: context
  - path: pages/traits/environment/uv_radiation_tolerant.html
    sha256: 67e688ae701f8dbe77f20ed627b55821942a724e30a483fa346456c2f79eac68
    role: context
  - path: pages/traits/environment/xerophilic.html
    sha256: 2d5b8f91ffad0620ee889110792dc1c70a2374203131055380720403b21a89ea
    role: context
  - path: pages/traits/environment/zinc_tolerant.html
    sha256: 47f1a47b66e4fabab7f54eec4ad56dcce1c37500e70ab2db6141b68ccec8b0c8
    role: context
  - path: pages/traits/genomics/abi2_system.html
    sha256: 7f9c32b98211f25c2de21ae112b574739abc96cdde20f9c19b4ec5964fa2a8e4
    role: context
  - path: pages/traits/genomics/abia_system.html
    sha256: af6fd8b334588f0abcd3635a38e85432d9ed9c48b8e16b6458cf327b3ca2a63b
    role: context
  - path: pages/traits/genomics/abialpha_system.html
    sha256: a620ae5946a032f0c47fa68a0c4392cc6156e8205145dc1f218115f937365691
    role: context
  - path: pages/traits/genomics/abib_system.html
    sha256: 865f73d1ffb200a199ff01d807b0feaffcd62908724f2e14b0d0c5bed5190c8c
    role: context
  - path: pages/traits/genomics/abic_system.html
    sha256: 7b87b7ad9a2de0e68167fa77d727aecd3ca6cadc356af6c50580fa485b36bd3a
    role: context
  - path: pages/traits/genomics/abid_system.html
    sha256: 9c3f78f0a207da0f721c08197cb7be2cbd95ce9a0ce7b7327d7c0c53f683e446
    role: context
  - path: pages/traits/genomics/abie_system.html
    sha256: 40348c9edd30e4deefa35946069920f24d28e6f37c59aee3164e49f1b7e017df
    role: context
  - path: pages/traits/genomics/abif_system.html
    sha256: 5ea4271ecea3132b12f9b78dbf24b57e655ac74e4c19a13616e1eed5098c721f
    role: context
  - path: pages/traits/genomics/abig_system.html
    sha256: e751500feaff6bef6ad72d507d8c4cb1c62a963a2bdbe43712bdcd8db31c606a
    role: context
  - path: pages/traits/genomics/abih_system.html
    sha256: 3d9bdaff77405a083d4f364920ba7d68c215317f6136979849cf646a950d87d2
    role: context
  - path: pages/traits/genomics/abii_system.html
    sha256: 5b66af6917294c811fe015deda3d65e7370825eabe3f2dc4e1fa92dcec45d88c
    role: context
  - path: pages/traits/genomics/abij_system.html
    sha256: 35bc66adee5b9d63949be07a671c81a0347b28f1438ae0844f09b8bdf4164598
    role: context
  - path: pages/traits/genomics/abik_system.html
    sha256: 872fa6b768b0d2e4dc140df421a249eb3582653b99e9769d4a4356ace47b2fdf
    role: context
  - path: pages/traits/genomics/abil_system.html
    sha256: e0fd4a770e33e99e6c591331241261aebcf42371ffc60e412ae8a18263e96aab
    role: context
  - path: pages/traits/genomics/abin_system.html
    sha256: da73eb1f6aa4bff0e41e9872a6c87187c455ae7289d6cae1ce0a6b0ab8fdbfb1
    role: context
  - path: pages/traits/genomics/abio_system.html
    sha256: 24ffd15be7dfbc7e9c689c673992da7f1740b2a9855056ed4dcf4b8395a05682
    role: context
  - path: pages/traits/genomics/abip2_system.html
    sha256: 239c79a75a5376024efa3e6f8f9a4377bb8bb2989626f3ca5e7bd0436b844ca7
    role: context
  - path: pages/traits/genomics/abiq_system.html
    sha256: ff9d0295fc496f9c92731f7602fe2ff5907c302ddc14850558cc9e41ded734ca
    role: context
  - path: pages/traits/genomics/abir_system.html
    sha256: 7cfae7bd33ffaa2c36364656df83b4bcfb7a41c00c1135f83aa1f9219665a860
    role: context
  - path: pages/traits/genomics/abit_system.html
    sha256: 1051b5d70a559cd246dd495b45983004c7340aaac04436949b91fb599baee1c9
    role: context
  - path: pages/traits/genomics/abiu_system.html
    sha256: 170e744cf48c23c57d5f4f69053a56d086d18922c612935ea50edeb45a3b42e5
    role: context
  - path: pages/traits/genomics/abiv_system.html
    sha256: 6d4c171db6009660d26f8304000aac60fbbd731f01b6bd1ee982d809b0a3ee52
    role: context
  - path: pages/traits/genomics/abiz_system.html
    sha256: c4676887569c4e736945b54ce353e32e42cfdf1e33e3459c817d437cc462f2f2
    role: context
  - path: pages/traits/genomics/abortive_infection_system.html
    sha256: 48469a51d85131326638443aa817a9e67eb74842bc612bce700a6a21b87d9352
    role: context
  - path: pages/traits/genomics/aditi_system.html
    sha256: b5d18b89c6ac75827ed1b7449da52371eae6b98f86c278bf5277241cc45115ef
    role: context
  - path: pages/traits/genomics/ambrosia_system.html
    sha256: 7b98f89c64290499959ac2207b4a38fcadbee0c58e6aa9c10a30ad740769be8d
    role: context
  - path: pages/traits/genomics/apsab_system.html
    sha256: 0c0b09c1b56612f5087600084b2dd9ef89041a0f4b99420f0b7b0fb2217a12c9
    role: context
  - path: pages/traits/genomics/aristaios_system.html
    sha256: 55a97405202fd45c2262d3bbfcfbbb72b99749ba2e631ca1f4265f5925975bfe
    role: context
  - path: pages/traits/genomics/armada_system.html
    sha256: 14bd28a3ba40549527a7bfc7def1b7f7d5dbf53ca1132ac48ab49798ca0218b5
    role: context
  - path: pages/traits/genomics/audmula_system.html
    sha256: f670c3ea384a517387775a27edb9640b739327c3ab9260095b45402bd30133ed
    role: context
  - path: pages/traits/genomics/avast_system.html
    sha256: d2b12d0def1c7d3ba37b29c90bd28911f2fcf879ec54b84a9779ef6d5d856338
    role: context
  - path: pages/traits/genomics/avs_i_system.html
    sha256: 471666004b98232797004f75430cc3ca811d0ee8d5c71af3f32cb2a820d8b991
    role: context
  - path: pages/traits/genomics/avs_ii_system.html
    sha256: 856651ee16d3fc94c086fa37fd81af90542d625b1f7dfafb7e3c54204f028df6
    role: context
  - path: pages/traits/genomics/avs_iii_system.html
    sha256: e223e01e49208387a597d9aed602dee43c51e6b31857783d88f35b262c2bb1e5
    role: context
  - path: pages/traits/genomics/avs_iv_system.html
    sha256: 9c0ff76c527b96fb526966f8c22140d06b736a0ea5874668e727d043e207ffa1
    role: context
  - path: pages/traits/genomics/avs_v_system.html
    sha256: 1c2c41e48d0ee93568557756042d0b1f8e460ca0a44a26f112292a01a9a4038c
    role: context
  - path: pages/traits/genomics/azaca_system.html
    sha256: f612bce6bd907cce25bd910ed8867154292d04db5a8eb571e7e509df26c9863f
    role: context
  - path: pages/traits/genomics/belenos_system.html
    sha256: 78a6ed6db69cb7db3c53c15c735b75b5bcaa62c2a2c3b415d8873e2736af4082
    role: context
  - path: pages/traits/genomics/belisama_system.html
    sha256: 5c60ad728388b11baacca15d18d704027ce22fe2e8dd2d5e90b13f669abaa0cf
    role: context
  - path: pages/traits/genomics/bil_system.html
    sha256: db59c4655e1c13a5281fd915c4166eb2184bb14e2e04a4542471d663fa7cd369
    role: context
  - path: pages/traits/genomics/borvo_system.html
    sha256: 316f6e12c9d395f63910cc192463bac4ebc496b1a91940f89dc1721ae7d41bb2
    role: context
  - path: pages/traits/genomics/brc113_system.html
    sha256: 159a28127d596700118e7e45f61594563166af3657d140e7697e6e3736415e3b
    role: context
  - path: pages/traits/genomics/brc142_system.html
    sha256: 7bd43e1e342ec35ab87708c8551adbd68b7bddbc6787577ea0edce8bb2f69aad
    role: context
  - path: pages/traits/genomics/brc167_system.html
    sha256: 497b96f33272c5117f3784494c1efa53d672b6f0c801df2727d1c0b821c03c35
    role: context
  - path: pages/traits/genomics/brc217_system.html
    sha256: 5664ef6f3dffe252d71a192bb1d5f34c1b595ca80a236bfe5b9a01883d0e8d0e
    role: context
  - path: pages/traits/genomics/brc22_system.html
    sha256: 2385f743c65e0d33a6a303aa8bf311e64ca324744db952525a9fbf8a75242505
    role: context
  - path: pages/traits/genomics/brc233_system.html
    sha256: 0ef1804818ee65b72b5d47f7486ab2fcbf0971265ad164a956509bae6482b3a8
    role: context
  - path: pages/traits/genomics/brc23_system.html
    sha256: 8f8095975250573dc36ae66ab2f9f1492d75ee6daedfe9c0edfc519ae5a36d09
    role: context
  - path: pages/traits/genomics/brc24_system.html
    sha256: eba6cf876a648b7a8b2f017966cf691025a8521e6f8a9bcc6c2639447bb48249
    role: context
  - path: pages/traits/genomics/brc59_system.html
    sha256: be25aab7ed882d3c64749103307609021cf1497651be7d06c54fd9fbd06e7721
    role: context
  - path: pages/traits/genomics/brc76_system.html
    sha256: 0219e7eeeba9c646567628289af716359665e46741c7034372fd44d388b7de9d
    role: context
  - path: pages/traits/genomics/brcwgs21_system.html
    sha256: 0c63199140d8efc762435acfc08108d2e8752fc943ae25bcba211b296fe59337
    role: context
  - path: pages/traits/genomics/brex_system.html
    sha256: 4c122811189c8204fcf3be0d8385ea317054a1c28ba31a002587f434b979572f
    role: context
  - path: pages/traits/genomics/brig1_system.html
    sha256: 1ceb0b646801912fefa2afc2424cd687c36b376a0011823b587a4d127e5e16da
    role: context
  - path: pages/traits/genomics/brigantia_system.html
    sha256: 1d4f3e1240dd57a128697543e30fb07e319db662cb9ed186da689b158ebf0d1c
    role: context
  - path: pages/traits/genomics/bsta_system.html
    sha256: 4839d46f8144845ab019816174af97b6d7277d7aa9d2baa3cad7e7e787455c01
    role: context
  - path: pages/traits/genomics/bunzi_system.html
    sha256: cd1e38f27b550fd059d84e55562420e63b87c078b8325c85b5c6ed4561b5ff30
    role: context
  - path: pages/traits/genomics/butters_gp30_gp31_system.html
    sha256: 2bf1c84d3d9a21c78f2b0acd8494d961e8acc0e5814da27edd7a7c80ab7ffd9e
    role: context
  - path: pages/traits/genomics/butters_gp57r_system.html
    sha256: 4881b8ddca625c1e5861cfa50acd7eeb689ad28022323d7a0a2ae4c39d506516
    role: context
  - path: pages/traits/genomics/caprel_system.html
    sha256: 1eb54a044e7364f8453d2b766ff0bf62eae78fd3aed6c43d250dcb2cdf6b1844
    role: context
  - path: pages/traits/genomics/card_nlr_endonuclease_system.html
    sha256: bca841fb98c27e6d95638c9cda3c0d69eb24120d8243d1a32182f596fbd69d11
    role: context
  - path: pages/traits/genomics/card_nlr_gasdermin_system.html
    sha256: 7ae51813cc5f0a4614c365211fe8afb6265aa0be13d80548be29b2069b4f85dc
    role: context
  - path: pages/traits/genomics/card_nlr_like_system.html
    sha256: bdbfef7f25004c7a522da72909ec401a7c2ec3ecb2979592ebdcad4da4745203
    role: context
  - path: pages/traits/genomics/card_nlr_phospho_system.html
    sha256: 721f463c7ba93d39ec70d7d26c613730ee19b9daccacb644b52af930e22de3d2
    role: context
  - path: pages/traits/genomics/card_nlr_subtilase_system.html
    sha256: 64b8f9d512defb306ca44613700c8916c1d88610e4b4e62fb74eb8bc305faaa9
    role: context
  - path: pages/traits/genomics/card_nlr_system.html
    sha256: 16f8c4b6e52155ac3fcf7186b527e71e7a29b19ded414f8aafc48c225c052705
    role: context
  - path: pages/traits/genomics/cbass_system.html
    sha256: 57d2552d050e426c6f3077d627dbe991493045d4f472c99304540e1d4de180a5
    role: context
  - path: pages/traits/genomics/ceres_system.html
    sha256: 48e9f6775bff0070bb03261c7b86cf46209591b552807ec3049625b6709489a1
    role: context
  - path: pages/traits/genomics/cernunnos_system.html
    sha256: 43dd91f252ea0259d41f1cc983b982adb40f1b111f6f2067a74027bc60709948
    role: context
  - path: pages/traits/genomics/charlie_gp32_system.html
    sha256: 186c7f225c717dd4576dcbc0c5ebf3b1deb8f2f137f4d11597aaa2e943ee63c5
    role: context
  - path: pages/traits/genomics/clover_system.html
    sha256: ee6c7dec96372cc2034ffa56b9b81a05b8d4d9293d985708bcc9531439281cd3
    role: context
  - path: pages/traits/genomics/cmdtac_system.html
    sha256: fa0242cadf1129232a46c54753f6dd05832b6914f38ff532ea9b1afc61699cf8
    role: context
  - path: pages/traits/genomics/coconut_system.html
    sha256: 30095af6c15933eb107a12819d698841959eababee2085d45d1e96a72416df75
    role: context
  - path: pages/traits/genomics/codon_usage_bias.html
    sha256: 122f330484c6f1d449ab7ca1063d913788ffb22fc0f79c12cff5282e704baf13
    role: context
  - path: pages/traits/genomics/crispr_cas_system.html
    sha256: e782828b85ebef8fb4882697a0b95d9505d38e5cefc9b629d0ad7121db5f166a
    role: context
  - path: pages/traits/genomics/crouga_system.html
    sha256: d3a791ba5b9b3bb758c42c2a42b759a6393e2ae1ee3a772f073e7bc499b23654
    role: context
  - path: pages/traits/genomics/dag_system.html
    sha256: 6f4e5c0c93529a95fc0e6b9898e7bbcadc45aeb365a798f4c032e414ff306fef
    role: context
  - path: pages/traits/genomics/damona_system.html
    sha256: 49cd4379cc5e0cfd877859d339621e653af36e9f53cd2e043a683f072daafab9
    role: context
  - path: pages/traits/genomics/darna_system.html
    sha256: b6d502cc086006c54ae26b453daa3ca85b02470e0956e9a2d859e761f8a1f994
    role: context
  - path: pages/traits/genomics/dartg_system.html
    sha256: 42d4687ae70f6efed7b570076edfc5ea8b5edb56f2e869c936129f308e0f20d2
    role: context
  - path: pages/traits/genomics/dazbog_system.html
    sha256: 0142290890e43a7dd8c14efd5bace761eaa7d37158c1bd598e5e3e7cfb4fc730
    role: context
  - path: pages/traits/genomics/dctpdeaminase_system.html
    sha256: b9eca3d8d5aafc6eb8955ae6dc09903163e08d1614587b56bd33bcdd099450b7
    role: context
  - path: pages/traits/genomics/ddmde_system.html
    sha256: 943fc4dc35224dbf8d76a41dc226f5ca319b3c0868e2dacad11a6470a3238c7b
    role: context
  - path: pages/traits/genomics/detocs_system.html
    sha256: 8150bbee8df4a480f9f8b9e737365fb3577554c1a245af86435ac011cd686355
    role: context
  - path: pages/traits/genomics/dgtpase_system.html
    sha256: 950ab875b4ef6570ffd561d2c1f8cd7a8b743d93e7963579aa743ca34361a127
    role: context
  - path: pages/traits/genomics/dionysus_system.html
    sha256: 643a2bd400eb26584baa8c91ead145946832c789a6939aa31e864fc65fdadb7b
    role: context
  - path: pages/traits/genomics/disarm1_system.html
    sha256: ce203c128f28cafb54bf1e41c3ef04a3d7c4038ba38c3df606f476e84a6cef9c
    role: context
  - path: pages/traits/genomics/disarm2_system.html
    sha256: 301550bbf1c6aacfa5cc78793df3fe0b04fef509fa8aebc4689f6d7b67821da6
    role: context
  - path: pages/traits/genomics/disarm_system.html
    sha256: d9c00549e5ee507c06d28dac86fb794ee49ff99d6f16408d142d3d13c005d4f2
    role: context
  - path: pages/traits/genomics/divona_system.html
    sha256: 54514d9ad3f80f35075d512941a7234cbd1d7f0f7d1b6bc9fbfafa781d70a9f7
    role: context
  - path: pages/traits/genomics/dnd_system.html
    sha256: 0f80302ffc967cc512ac772a47923ca2f20fb66418b396372465b4737d6f8e50
    role: context
  - path: pages/traits/genomics/dndcdea_pbeabcd_system.html
    sha256: aa39601f0cc002eb8901cb24728df4a3d2d174306886ddbd1ddf158b1269b2ad
    role: context
  - path: pages/traits/genomics/dodola_system.html
    sha256: e3835fef9bac1d4012e72fbb76c349e7da66ed2363c6bc35295bc79d87e62470
    role: context
  - path: pages/traits/genomics/dpd_system.html
    sha256: 970a5181f6bcb8a026e7c395e81e3b9d8ec84c2b7a877e15ce4917e32d071402
    role: context
  - path: pages/traits/genomics/drt1_system.html
    sha256: 8940ef9722b87f858b6d4f43da3e19dcece081ec854ba77e4d157d2294057f08
    role: context
  - path: pages/traits/genomics/drt2_system.html
    sha256: 533c2390cc5effa29fceb8b2033a400b955219513a2d7aedf35b3dacb99da222
    role: context
  - path: pages/traits/genomics/drt3_system.html
    sha256: d4e54b831ad356d94c35edd2627e692a9e1f787be9c2ff93b0da7eb0d13aa3a4
    role: context
  - path: pages/traits/genomics/drt4_system.html
    sha256: 42567534b57a85c56fa6b1ee023f8e935622cdb1b98c1b6bc245c6175b509577
    role: context
  - path: pages/traits/genomics/drt5_system.html
    sha256: a92e8d3355c08ee19c1fe225052aa7f827e6b2a4027da0924747a7f5ed711fff
    role: context
  - path: pages/traits/genomics/drt6_system.html
    sha256: 3d2e90eb00f48caaf4efb0f143872d5b23ae5da51b3188394a7d50577cac4ca1
    role: context
  - path: pages/traits/genomics/drt7_system.html
    sha256: 48bbd7e6822bc880ba04292b7e7490d531b5e45790aef1b3c1714a41ba83bcda
    role: context
  - path: pages/traits/genomics/drt8_system.html
    sha256: 8821b5e605c4c4de09c183e2f575b447322843423b02c7aca5f24fe76ad13e3a
    role: context
  - path: pages/traits/genomics/drt9_system.html
    sha256: 0315a1ad3cba6b8e1d91ff38efc9d0805477826d02190da6321c1d55d1f8fd05
    role: context
  - path: pages/traits/genomics/drt_system.html
    sha256: a9ebf14b5dc19f8078c8902b3260485391e5b1e57e9c2e36044eff22b579dc70
    role: context
  - path: pages/traits/genomics/druantia_iii_system.html
    sha256: 955ea7f97aaab7f53121c65618413f03458c6eda79f20e1c5a8fb9ddb2529b81
    role: context
  - path: pages/traits/genomics/druantia_system.html
    sha256: cbf8c257147e41730ead34cc69dc1fb70a10e0c0b15dacd7c286a94a67fa0120
    role: context
  - path: pages/traits/genomics/druantia_type_i_system.html
    sha256: 8110dd2c15747c57ddba233671859a22542e93e18ca21e8297530e5142b5eba6
    role: context
  - path: pages/traits/genomics/druantia_type_ii_system.html
    sha256: f46109d332d4d47de546357d1d8c68867343300d79f000d1c0e42f8079c4f4f5
    role: context
  - path: pages/traits/genomics/druantia_type_iv_system.html
    sha256: dc9f420911d57ee4c9076c5d8e37b938f4c44d2b3e91693661345de6e324dd15
    role: context
  - path: pages/traits/genomics/ds_10_system.html
    sha256: c05f4d6a324cd57dfb534c7ffd4f8362d25d06e7aa7ca987e7fcee1a247f64f8
    role: context
  - path: pages/traits/genomics/ds_11_system.html
    sha256: 3815bb4b67b6f4f5bb91a052e65ad510a144651d96ff8a763f6139a05dafe22a
    role: context
  - path: pages/traits/genomics/ds_12_system.html
    sha256: 19e061ab0c391226a2dced74215edee450afafafc96c1a1f8cc43d441fe7cedc
    role: context
  - path: pages/traits/genomics/ds_13_system.html
    sha256: 837e1e4c95d68c62b54ec1645c69b52f375bbe50ee9804dc2ed3060e97acc5c1
    role: context
  - path: pages/traits/genomics/ds_14_system.html
    sha256: 478f4dae6ab86a799e5c645e0daa37fa1ed456f34359aceb35194890aac98af7
    role: context
  - path: pages/traits/genomics/ds_15_system.html
    sha256: 18bdd0d5f270ef35b4679ca85a2c073346d4d21ea3e3f8d9bed489c2c357cfbe
    role: context
  - path: pages/traits/genomics/ds_16_system.html
    sha256: 2df64cb7a139fdb3e834dfa29bac370047b0f9fc65061f08e44dd927b5028618
    role: context
  - path: pages/traits/genomics/ds_17_system.html
    sha256: 39bf5f03af5110e7f3e9f19d8c08f7d73a05b45a572b5b28411d5ad93d06a3e0
    role: context
  - path: pages/traits/genomics/ds_18_system.html
    sha256: 062cdebb0e41f26450f2571cc112c578de16085bdbf19fafc47083718e9689fb
    role: context
  - path: pages/traits/genomics/ds_19_system.html
    sha256: 27c2927fb967b01737fb94f1dd9d96d3e40af4de6ea3d6a358243b516cbdb1f1
    role: context
  - path: pages/traits/genomics/ds_1_system.html
    sha256: 6a51c2eef9d2a47a8053b6bf09cc29a643a904c78310519ae61e1cd211f3d55c
    role: context
  - path: pages/traits/genomics/ds_20_system.html
    sha256: cb36ce9c3b5a3f8fae2620253f01132727fbc1715bbfe2c0e0800d8c9e4ef9c7
    role: context
  - path: pages/traits/genomics/ds_21_system.html
    sha256: e937c053562803e084bdeab7fb017f3a1371e9ad4bc279b06e76c86b03c0e8f2
    role: context
  - path: pages/traits/genomics/ds_22_system.html
    sha256: bbf8fc3fa8ebbc815f6b960dd1b74549c2530d0973a015e3a6ec704898426a89
    role: context
  - path: pages/traits/genomics/ds_23_system.html
    sha256: 2b4d81ae63f780589cb792862926fe0a07bf50c0f949d8a193dce61f80ba2e37
    role: context
  - path: pages/traits/genomics/ds_24_system.html
    sha256: e7659ee0a4a37562e8ed7bef2b42f274d56757d17da4f5bf886a5d795c8638d5
    role: context
  - path: pages/traits/genomics/ds_25_system.html
    sha256: ceb0bedb909fc172976f3422192da0e90052f4aa072f9f024ad198d9b7677f33
    role: context
  - path: pages/traits/genomics/ds_26_system.html
    sha256: 96b765496a7c9c5c3965192ae51fa676ded08bdb47072e36c914bd5361b7de3a
    role: context
  - path: pages/traits/genomics/ds_27_system.html
    sha256: 212b84788223f6d3d6d55ba51282a7c46841d67d1c4ed137d4d490fa12da660e
    role: context
  - path: pages/traits/genomics/ds_28_system.html
    sha256: d25f0224178ebbc06a977495872f77f61e0320fca5102eaa4ab9cd3e19bdf268
    role: context
  - path: pages/traits/genomics/ds_29_system.html
    sha256: d1b4a8ebec3499fd3baab72ebcc3ff62b44d67bccd756f5b307b890ecb0c9506
    role: context
  - path: pages/traits/genomics/ds_2_system.html
    sha256: ded1df9dd26b79e9857faf3992c521602abb33de1b6fdf2993872497e4987f21
    role: context
  - path: pages/traits/genomics/ds_30_system.html
    sha256: 9e85f8a8b4c41657beba68bf48462550d39ce7345c3f93e2d9c517d335f1f3d9
    role: context
  - path: pages/traits/genomics/ds_31_system.html
    sha256: 1080b5cbb9726e0146c0b962628bf4120ffb2e603dfcc505957e8842b97eeeb1
    role: context
  - path: pages/traits/genomics/ds_32_system.html
    sha256: 141aa653488c5ce097afb9524f5a3d1e10322a4909fd371925881c4ce677d162
    role: context
  - path: pages/traits/genomics/ds_33_system.html
    sha256: eae5291801288b24114f8e9805c3df88b10b8cb463ab71e6698f85dc607ade73
    role: context
  - path: pages/traits/genomics/ds_34_system.html
    sha256: 7749613dc1317ae71c690d1def700922fb7b28e7b6fc70f1d08a41495870723c
    role: context
  - path: pages/traits/genomics/ds_35_system.html
    sha256: 14866c183affabdb0ae7ffc26337404e5470043517f3f2e3fcc406142c64a60d
    role: context
  - path: pages/traits/genomics/ds_36_system.html
    sha256: c7c285aa66bc8a502cdb8e008335d7f75429ffdccb107086f1ad28830b4a026a
    role: context
  - path: pages/traits/genomics/ds_37_system.html
    sha256: 6da2a73b3e448d6e4668a07d011188b471c0e583d9289606c83118ac3c4572cc
    role: context
  - path: pages/traits/genomics/ds_38_system.html
    sha256: 8153fe37c3108d0317dec6d6ef7b17c4ad5d75389bbb5c057e71557684c6f86c
    role: context
  - path: pages/traits/genomics/ds_39_system.html
    sha256: 04a75daba82a092750cf23551ea8ae4acb4c5c449d632b1a6e311e92ba3fde28
    role: context
  - path: pages/traits/genomics/ds_3_system.html
    sha256: ce75e1320b491c3d3abcbeb591b6c255d8ce173ee429fb482470f25d5856c602
    role: context
  - path: pages/traits/genomics/ds_40_system.html
    sha256: fcf9db3755eee91615072ed26c8a0ed458f3f6b5c7c04962490dd0efe6b1186e
    role: context
  - path: pages/traits/genomics/ds_41_system.html
    sha256: ec0cb580fb3da53c2d801fe71a492827ac17b9cb9cf598ac22c651fd1a01d3eb
    role: context
  - path: pages/traits/genomics/ds_42_system.html
    sha256: 4d217d156a3b31dd181a71f40827688ac455657189e02261800ee80d4993fece
    role: context
  - path: pages/traits/genomics/ds_43_system.html
    sha256: 206b8ecf5e0305cdd0464867970de6149cb558d573d4c825d0c9483260176c25
    role: context
  - path: pages/traits/genomics/ds_44_system.html
    sha256: 6471bb187cd9a7d26e9d46afbda11ebbdeeed2d68b4dde2cff5982189eb33c57
    role: context
  - path: pages/traits/genomics/ds_45_system.html
    sha256: 014cc752f78592b8e8305354f0023acbca5b258665f9b57b3934f6997b5f4878
    role: context
  - path: pages/traits/genomics/ds_46_system.html
    sha256: 92bd6ed208c863d65f755dbbf431586b3789bbce4718ff9d1c9c0fa42e4d6769
    role: context
  - path: pages/traits/genomics/ds_4_system.html
    sha256: 3a8e4a3765ff34fdf397225ea9df6415fe9e6337078da040f4d7c0ee8bbdccee
    role: context
  - path: pages/traits/genomics/ds_5_system.html
    sha256: 36a0685c45da85e8c0f4ee0b30a6927e5e26e053114e92ec4a086db2c9ce8e76
    role: context
  - path: pages/traits/genomics/ds_6_system.html
    sha256: 2a15e0490b0575e7919c83b95f6d46a0abc0c582e2b6377c8493dc355b49ad8c
    role: context
  - path: pages/traits/genomics/ds_7_system.html
    sha256: fa53a858e95cbbe5fe4beb2ae5af34daf638835d461fd4cfd547a011be3db1aa
    role: context
  - path: pages/traits/genomics/ds_8_system.html
    sha256: fec92f838221c322ee99a29b279e27439167514e738166a49ecbf260d31703f4
    role: context
  - path: pages/traits/genomics/ds_9_system.html
    sha256: 1601e4d7eb04e2b3ce3a55eae95ecb6cf9035813efeb609d3dc86cb0c469fd33
    role: context
  - path: pages/traits/genomics/dsr_system.html
    sha256: 959a80ebe0585e5bfe532473e8252e1e9a10e1a5b4194fe04fbaec41049e5975
    role: context
  - path: pages/traits/genomics/duf262_schlafen_system.html
    sha256: 94c4b9c13ab8d1e405c53456d947e5d60710bd7bcfbba5191ce5756e4308801d
    role: context
  - path: pages/traits/genomics/ecokmcra_system.html
    sha256: abf7ec62b6e3ad1823dd3e99aa6c286ce54804dd2ee9feb6123bda106a213951
    role: context
  - path: pages/traits/genomics/eleos_system.html
    sha256: cab0159972f5c59d76678547b57b2931f8964c3b35e8c2379264716103948b16
    role: context
  - path: pages/traits/genomics/endpacf1_system.html
    sha256: 806e49eb60f1210c5102c6c09794090d6e9adf83b690dfcf4d23b989d71222a8
    role: context
  - path: pages/traits/genomics/epona_system.html
    sha256: 36f6284b0ecf357304c86b919459f0e9007ffed36e036563b9e2351e2de00e5f
    role: context
  - path: pages/traits/genomics/erebus_system.html
    sha256: 252957c8d1b21825488c732f5a444907df454e4c4accf00ae6f5335d63aae891
    role: context
  - path: pages/traits/genomics/esos_system.html
    sha256: 8c3c74c3721a55d772313f140c926135aede5ea56e19d89b1bc1f151f54fe086
    role: context
  - path: pages/traits/genomics/fliodhais_system.html
    sha256: 1467d13c1b40a5853960a5925e1c0797dc62c79e8b89557bb014828df76ab94f
    role: context
  - path: pages/traits/genomics/fs_giy_yig_system.html
    sha256: 00e34df9974b8e339bce0f1686d57b43bac8bcdfaac2b4be0544c24cf12e635f
    role: context
  - path: pages/traits/genomics/fs_hepn_tm_system.html
    sha256: f31c501f9add20b82823ea3390e292cebe8dfbe79da967d2cd685ce642167d6f
    role: context
  - path: pages/traits/genomics/fs_hp_sdh_sah_system.html
    sha256: 6fc8cebbd27f2a06331915f0f67efd90f2abd3a05c6757b2d8563937875a9603
    role: context
  - path: pages/traits/genomics/fs_hp_system.html
    sha256: dc78ae5d43ab91f6b32b4aefcf874acff585e97d831bdc78dfbca435c3b1a4da
    role: context
  - path: pages/traits/genomics/fs_hsdr_like_system.html
    sha256: 4826e425f71e6c5328aa0f20f7e33f3bd21a970d4fade7f24f27ccf769843d4d
    role: context
  - path: pages/traits/genomics/fs_sma_system.html
    sha256: 4d5d4ff70190914d6533c331bbd1c52f6d8e687a701b33ad2277168c2d05fa3a
    role: context
  - path: pages/traits/genomics/gabija_system.html
    sha256: b0916ae24274dd4ec30e953e1ef4f6a0b8a133f7bfa09a654fddd577fad3e050
    role: context
  - path: pages/traits/genomics/gao_ape_system.html
    sha256: b9b916e746454937e3982daf576a3ba274e5450b8df7de0922044f69e5b03a1f
    role: context
  - path: pages/traits/genomics/gao_her_duf_system.html
    sha256: 9554d99a06be40fcbb7d026d232e8d45e046a0eca5a5cfec700a5716ed5572f9
    role: context
  - path: pages/traits/genomics/gao_her_sir_system.html
    sha256: 19df97fee2c52034e5a61ea6f2681b7e73973cac016dccf316fabca1d5d58632
    role: context
  - path: pages/traits/genomics/gao_her_system.html
    sha256: 8a878aae44a468bb1fd217717cc51a97aeaac9a8df40a5b4354a85cee9c8d5c3
    role: context
  - path: pages/traits/genomics/gao_hhe_system.html
    sha256: 3398b086823fd791abf2496211e4d2aee666fc5fd2ea1e0c8c61e8450e5d507c
    role: context
  - path: pages/traits/genomics/gao_iet_system.html
    sha256: 6ba5371d9649cec29a7f222f4c0e8f732dcd7137ddb4da5583f80f0ac5978e18
    role: context
  - path: pages/traits/genomics/gao_mza_system.html
    sha256: 5de72edf1e7c1de30d4ccf8fa4e83a04f39f422fd2b421e730d577c43edf1981
    role: context
  - path: pages/traits/genomics/gao_ppl_system.html
    sha256: 24a1197b9f47e86c5b39ae0d1efbe5053a398c589cddf4608f6f9812097ff426
    role: context
  - path: pages/traits/genomics/gao_qat_system.html
    sha256: 67f449b893f9c720e4662f7bab01202dde78aa51f5a30a1eb6a5f5df0b508d9b
    role: context
  - path: pages/traits/genomics/gao_rl_system.html
    sha256: 7d84ebb25af85b0b99096be93414399243b966ad5958db312cd1fa7928d1e096
    role: context
  - path: pages/traits/genomics/gao_tery_system.html
    sha256: 5b8140def67616cb905929a7b22ff13b227a8eb8a4b67d06cc9e685e1106902b
    role: context
  - path: pages/traits/genomics/gao_tmn_system.html
    sha256: e9f249aa5b96da0889d907bf231fd93ca14a18efbf9714b6060202a1d9c21402
    role: context
  - path: pages/traits/genomics/gao_upx_system.html
    sha256: adfbff24639e50a206254c6ab31f1307562dc8813eac99e5c01cde4a8ab751d9
    role: context
  - path: pages/traits/genomics/gaps1_system.html
    sha256: 23076fdcfedb2cc31345a6f227b771109cfcb92415633bda5327b5c98d7ea9bc
    role: context
  - path: pages/traits/genomics/gaps2_system.html
    sha256: 5c1d5c9d84a7936fdbb5da8dc543436dce6407e5c9b8b36d50f44b9f4b5ead54
    role: context
  - path: pages/traits/genomics/gaps4_system.html
    sha256: 7d9c7e556d1a1947d86eee1b93fad797e0825cc07236f040c728a1b8687c5e18
    role: context
  - path: pages/traits/genomics/gaps6_system.html
    sha256: 56b8d8c7e24bc002572d7a6d44c567b8385152235406b45266f2d1a33a69ffd5
    role: context
  - path: pages/traits/genomics/gasdermin_system.html
    sha256: d3dfe5729229276a71e33a71998eadd4d591ba9ed00c966ea74c5d8c1cacfef7
    role: context
  - path: pages/traits/genomics/gc_content.html
    sha256: 579a703af7f15026a75dd0468051a215980128f50be226fc4aa40272533f8f0e
    role: context
  - path: pages/traits/genomics/gc_high.html
    sha256: 20609376cb77cbca4f3adb088ab1db4dda498c4d39d9bd6076cbef05c7cd8b6f
    role: context
  - path: pages/traits/genomics/gc_low.html
    sha256: d1ba5f7094a163ab41ba0d2a9a10abb09f4079acd3de24589b6ef24bf81ba673
    role: context
  - path: pages/traits/genomics/gc_mid1.html
    sha256: f51d85f10e3e26ebf1a23b0af3558097dc145d2f1214555f562a1f62d68df458
    role: context
  - path: pages/traits/genomics/gc_mid2.html
    sha256: 5537e92ba038113d06408a550fe2cdb293fa33229759abc1f3c24b0044d9b7ea
    role: context
  - path: pages/traits/genomics/gc_skew.html
    sha256: c28a0bdaeb41f1995861c5137e47018f10ea30bc1727f0fcfb87de4210f54a32
    role: context
  - path: pages/traits/genomics/geb_system.html
    sha256: df2dfc421bb285613b156292cabb5fb2b9d4fa42abf76c108a224f58916bc3dd
    role: context
  - path: pages/traits/genomics/genome_size.html
    sha256: b86cdce088181c5de3ec9aa8281858f11012fb1859e845a3af0e25f6b09c0c76
    role: context
  - path: pages/traits/genomics/genome_streamlining.html
    sha256: 5233c9120e0c41854f56c40fb29195bd378e6dc7e68bde28cafd335143867ac5
    role: context
  - path: pages/traits/genomics/genomic_island.html
    sha256: 60655294c15f37e5f3c4d607941e3a09a47da79b63ad4307d19093b321a43f62
    role: context
  - path: pages/traits/genomics/gmrsd_system.html
    sha256: af1a729aa42baee12d1fc2b302d2f186fc82b739fc202e57cdec951478c2754e
    role: context
  - path: pages/traits/genomics/hachiman_system.html
    sha256: 96280b08de55f78eedf7db1fa47f66e1863dcdc7424a5eeed480c7532cd07438
    role: context
  - path: pages/traits/genomics/hachiman_type_i_system.html
    sha256: abb0bbf032f2abda693adbbede638163fcf950633972ec27def73fb67182386c
    role: context
  - path: pages/traits/genomics/hachiman_type_ii_system.html
    sha256: eecb0d1c03997b2cf5acbbe32429cfb7e4d0a757f74c6a6dcc3454b3976b70d4
    role: context
  - path: pages/traits/genomics/hailong_system.html
    sha256: 356b49ee5b8ca295e7f190e484406e0e14b37012d733cc1792b15ae71f4a5098
    role: context
  - path: pages/traits/genomics/hec_02_system.html
    sha256: 491388223d7b1c93105d62027c1670509526485dc2b05581ac7b07a8d633555f
    role: context
  - path: pages/traits/genomics/hec_03_system.html
    sha256: 305df54f121f7d89301059137de42191eefc201c0f76433ee178e5571891f400
    role: context
  - path: pages/traits/genomics/hec_04_system.html
    sha256: 3c4618674e1e13d003b4d4c5318422a5f87260a39b197572944b17615c2390bc
    role: context
  - path: pages/traits/genomics/hec_05_system.html
    sha256: e34df1374759fac23d1dc73b579317aa53b7d0e7508affc37a8f0d9a90978392
    role: context
  - path: pages/traits/genomics/hec_06_system.html
    sha256: 963955b02519ccfc20fcdc1ce928b68d353c8ebb380c449204e9ac9d97fbe38b
    role: context
  - path: pages/traits/genomics/hec_07_system.html
    sha256: aa639489d15bc70a868007ce9d8496c95568d4b163b429d15eae489dfbcdbbc9
    role: context
  - path: pages/traits/genomics/hec_08_system.html
    sha256: 1ddccafea3f73c3a53b00cce89c0bd9032df612916dc99ee1c10d44aaf6e4d66
    role: context
  - path: pages/traits/genomics/hesat_system.html
    sha256: a76853a91ad598f89268486cb1a90686aa2697cf9b6b1f04493e8ec45cb38182
    role: context
  - path: pages/traits/genomics/heterokaryosis.html
    sha256: c43c6c620ff45ecc2f3c590d24bd6e65b20add8792501bfe0eeed3935a08994a
    role: context
  - path: pages/traits/genomics/hma_system.html
    sha256: f9c089ac245d053893d558abdd15da4487fe0b3de29030eae921a4b4e8dccd3d
    role: context
  - path: pages/traits/genomics/hna_system.html
    sha256: 6cd62cb03cd1bc287e9b08b28f0c7010830fd0e0d949a7055e38f885235a7975
    role: context
  - path: pages/traits/genomics/hypnos_system.html
    sha256: e3135ca0ae0a496fb469c2e28ea14bcbab4baea07df993475738f1a477eae514
    role: context
  - path: pages/traits/genomics/ig_like_schlafen_system.html
    sha256: 549b69b9e5d6bc99888871d0099cb3c7aa1222c45dd60000d807c60e5ab0c4b5
    role: context
  - path: pages/traits/genomics/integrative_conjugative_element.html
    sha256: 21ece9770d93a9ce56bd6caaba40185397d42fe6016e681d161ca3e46df622b2
    role: context
  - path: pages/traits/genomics/jukab_system.html
    sha256: e05fff05ad76d629346dad15b985cdead9769a13732ebd421a6056a67c304518
    role: context
  - path: pages/traits/genomics/kamadhenu_system.html
    sha256: 182dec3f094d3acbf5c33ef3c460a962f78025f8bdce4152e8a4287b3ab71c54
    role: context
  - path: pages/traits/genomics/kiwa_system.html
    sha256: c3a7c29cc96a179f282daa0aadc4f9a5568e96a556f22280ca1727bac8fa9cb1
    role: context
  - path: pages/traits/genomics/kongming_system.html
    sha256: f946008b68ba371f5db08185efb6408556462df64c277b2cef68be3986a92b29
    role: context
  - path: pages/traits/genomics/lamassu_amidase_system.html
    sha256: b2e2baba26866407ffc03bbe3166d4b4f7d07b844ee05caa1c0e7f920400149e
    role: context
  - path: pages/traits/genomics/lamassu_cap4_nuclease_system.html
    sha256: 52a93b580f7e08c6041b28fc467ce42dc02689239b934d27ad41ab065e0d763b
    role: context
  - path: pages/traits/genomics/lamassu_fmo_system.html
    sha256: d66f5af65acd67619fe2c30eb752645b151e76a00bac5919bfc2bcc40badb544
    role: context
  - path: pages/traits/genomics/lamassu_hnh_system.html
    sha256: d67863244735bdba2d52a80281a8620fc2e1fd1fe9e092dbf6c257c9551e4610
    role: context
  - path: pages/traits/genomics/lamassu_hydrolase_protease_system.html
    sha256: 0b5f404579bb1e6c2473e7062d762ce813fdb44779690de03965d7483b944972
    role: context
  - path: pages/traits/genomics/lamassu_hydrolase_system.html
    sha256: 690f49f8e82eda16bbb7a6429f9d3fb7dec8fb3026c13f07e2339434d3ae16f9
    role: context
  - path: pages/traits/genomics/lamassu_lipase_system.html
    sha256: 2d6ff3e20fb9b9b44b89aabcb5ad984b5e0c53f0c60de22ad6cab7ad1a8a1926
    role: context
  - path: pages/traits/genomics/lamassu_mrr_system.html
    sha256: f19cd2dfa6cea830555e743ebcc87bb0d44d0bc088ea154aeb1f99cdd99337a1
    role: context
  - path: pages/traits/genomics/lamassu_pddexk_system.html
    sha256: a0130bc53645bc9cc5c4261a028f9ae1513a7e2481a4763a05dba85fa9de3a20
    role: context
  - path: pages/traits/genomics/lamassu_protease_system.html
    sha256: 3dabeebb42ab95d61570fdd04e663f25550cbfad464a3bf5a20cf3c97f5cebeb
    role: context
  - path: pages/traits/genomics/lamassu_sir2_system.html
    sha256: 403a72f94469eaf5b3933fbd1b85737aec1da03517ae4d1f42b11a3c73f29148
    role: context
  - path: pages/traits/genomics/lamassu_smek_system.html
    sha256: 0ea064dd78c327283945f952f45458d6da54310059d7fca0c9ef0686d475daff
    role: context
  - path: pages/traits/genomics/lamassu_system.html
    sha256: 64f6e70b11af2691ebf4e2f14488469982e6e321b7460c650aa0c0fdf2f55385
    role: context
  - path: pages/traits/genomics/lamassu_type_i_system.html
    sha256: 8cc0db7bba7b004ac27831ffc4b75fa67fcf8f2d3ff00baaae18d9ae77daa507
    role: context
  - path: pages/traits/genomics/lamassu_type_ii_system.html
    sha256: 457c53afc5c334b2a2217e7346134abc430e47e04b924c66b769c0416f360cb3
    role: context
  - path: pages/traits/genomics/lanthivirin_system.html
    sha256: cfcb6f1cbee8de190a93729319728979ffa2eb6d12b8105b7fd5956872332cc9
    role: context
  - path: pages/traits/genomics/lit_system.html
    sha256: e46ba159227df40978367c736155b7de39ba5c221cc57c1f10f052428ecae72f
    role: context
  - path: pages/traits/genomics/long_lamassu_system.html
    sha256: d676decb9e26d538c754b70ff1b8c7e00876cb4e31c5eb44318d3d3078ae6371
    role: context
  - path: pages/traits/genomics/lugos_system.html
    sha256: b77242dcd4602e7ffa84e9a34fc75a956e04e63b8c19bf02de5f33748d2115c2
    role: context
  - path: pages/traits/genomics/mads_system.html
    sha256: 352eaaf701b18f0f4f66dfddeee1ce0975bdf0e0d60c5bb803df0f157d954cc9
    role: context
  - path: pages/traits/genomics/mazef_system.html
    sha256: b5d35c7e98300e9be856712ddf8f53315b14bef50031a1496b3def48a704f328
    role: context
  - path: pages/traits/genomics/mcrbc_system.html
    sha256: f6a4ff85067eacae381d564c5fb970dfc0a33bbd2869f92506acb5f29e72969b
    role: context
  - path: pages/traits/genomics/menshen_system.html
    sha256: 90d656d2c7272ae0ed47dae13e15530ac447cdec7271c24c548e8bf2e8ea3157
    role: context
  - path: pages/traits/genomics/metis_system.html
    sha256: 2dcc92fae4d3fe9b059cde1add817565555c52d181f4867dd4854b87fb3aed2c
    role: context
  - path: pages/traits/genomics/mksbefg_system.html
    sha256: 414afcfac14a23ed0a37d32d18dc6808f2e7b35669c030c7e781198812f4d4dc
    role: context
  - path: pages/traits/genomics/mmb_gp29_gp30_system.html
    sha256: cf339ecc3472d5edf4b9a8193f8da1d9da8b44a1c9c50189e567c8b0b5a4ce3c
    role: context
  - path: pages/traits/genomics/mobile_genetic_element.html
    sha256: ad22c89c6cec87906bb6ea89ad8cf4fdbfe4921fec08f1f543f15ad15fc21b73
    role: context
  - path: pages/traits/genomics/mok_hok_sok_system.html
    sha256: 5dd1823489c8c6ddd0fbfa90bc94d6ab20bc5a60acad6dbc35ce3978f5095113
    role: context
  - path: pages/traits/genomics/mokosh_system.html
    sha256: 4fe15135ad196c9e19184b8aab6945e6037a2e9e3cfde6bf37080e0752acba8a
    role: context
  - path: pages/traits/genomics/mqsrac_system.html
    sha256: 76ca28fd324543b3772822c0089a864baa1c59f6a97d26f2c6d23bd744cd70c5
    role: context
  - path: pages/traits/genomics/mspji_system.html
    sha256: 1e2eadd619b7d082be417e89bcffebfae6e4601e6f1b8306acfbd17f950664bc
    role: context
  - path: pages/traits/genomics/nantosuelta_system.html
    sha256: c588c0c2dccf0dbb65c4a7cc02df368ddeedca8ff1ee62747712d88a5d7abba3
    role: context
  - path: pages/traits/genomics/nemetona_system.html
    sha256: ccdaf184fb0f3be485b57d7d293fc3061febafc01cb37a9b106823516ed46a65
    role: context
  - path: pages/traits/genomics/nhi_system.html
    sha256: 7d4a45c1912ade2429da48c4627173af1f23161abb32866bf994903b2757df12
    role: context
  - path: pages/traits/genomics/nixi_system.html
    sha256: 1e33a25f60d3e3d9587ba06b14f94501d00c929857a25eb16730eb3181f0acd6
    role: context
  - path: pages/traits/genomics/nlr_like_bnacht_system.html
    sha256: 4396824e8258391a47005e3cd4307e4755f379a488fbfde1b653e23d2a21d59b
    role: context
  - path: pages/traits/genomics/ogmios_system.html
    sha256: 3ec24dd16cfbb7b3a45fedf657619352fd0cca0085387b6aa3a4f36a383422f9
    role: context
  - path: pages/traits/genomics/old_exonuclease_system.html
    sha256: 27467c1c7cb8826f5c290a121199d96b106291edc304698e4180d451437b5297
    role: context
  - path: pages/traits/genomics/olokun_system.html
    sha256: 7cfa4d33926ed6e478df9cb01b746d4c85e3235bb2915e34501a5254797010ea
    role: context
  - path: pages/traits/genomics/ophion_system.html
    sha256: cb379452b00e66d6c38062d2711862fade1a6d09bbf3d87b22bb5db1e4fe5fbc
    role: context
  - path: pages/traits/genomics/oshun_system.html
    sha256: 55a5bd438a9bb512861683f33a95065918b15998a340314a6af33e0a30a0cf86
    role: context
  - path: pages/traits/genomics/pago_system.html
    sha256: e944e00c2d67f90bb7c503f4bf86dd21372fd6eb1fbf415cf0267946a48fa74f
    role: context
  - path: pages/traits/genomics/panchino_gp28_system.html
    sha256: d2b9a5e1b9b8581f244b61f78dfff4cf1f07d9d1b75553f27c9f1803d7d72bb1
    role: context
  - path: pages/traits/genomics/pangenome_openness.html
    sha256: 2b75d8c166403f1f5b3f75ec4cd762bfb446c1cb43073d1bd337e1f8f0c5a7b5
    role: context
  - path: pages/traits/genomics/panoptes_system.html
    sha256: e7345e72e26f5c13a6673b34d1e3045c1c54769b27a63b36486abc89e18a61c9
    role: context
  - path: pages/traits/genomics/paris_system.html
    sha256: 87fbf798b2e1ae9b3986ab065c3066669a78deab0926b7b1cef95055d36fab56
    role: context
  - path: pages/traits/genomics/pd_lambda_1_system.html
    sha256: a6c4786a0513c78c2d3f59a779dc1f43a0638c433982275be8af4f8ecb1e9963
    role: context
  - path: pages/traits/genomics/pd_lambda_2_system.html
    sha256: 9d2a2f5baa521f0df64f5f7443946cb8afcb7f18f816fcc5a8fb3c434b36904f
    role: context
  - path: pages/traits/genomics/pd_lambda_3_system.html
    sha256: f26f56e161ee357b33fb1bf6f8ff9fed63f3efb75df65da19c79521f4277cd0f
    role: context
  - path: pages/traits/genomics/pd_lambda_4_system.html
    sha256: dac1b1f4c83dd0ec0f1d44249456395c054449c624374d584bc41b3bb21cb5ce
    role: context
  - path: pages/traits/genomics/pd_lambda_5_system.html
    sha256: b01864ea43c75d1306cb744264501b5fdb552c878262a95c183220259bfa0d85
    role: context
  - path: pages/traits/genomics/pd_lambda_6_system.html
    sha256: ef6c37def77559ccdf56d4ad1cdcbf5382d58097aace9f2601e73e0b14f5a2f3
    role: context
  - path: pages/traits/genomics/pd_t2_1_system.html
    sha256: 2aeb0f6fa7dd7fd38d07f7592f5636735b3909c8147f86a821494feaf8c5ec63
    role: context
  - path: pages/traits/genomics/pd_t4_10_system.html
    sha256: f062dea945b4588505393fadc04f436bf32aa7a31a2ac533d4ab8f3ef732277a
    role: context
  - path: pages/traits/genomics/pd_t4_1_system.html
    sha256: da467dcd759cdf95049d0786a5d8c1b43808158c6baaaf01be21ebd86f829327
    role: context
  - path: pages/traits/genomics/pd_t4_2_system.html
    sha256: f4624ddbb3e009cfc4532576aa5d9d3a517a9d06ed3e2625930d667ae1969792
    role: context
  - path: pages/traits/genomics/pd_t4_3_system.html
    sha256: 53b372d8189b97678c513c7aae21832afb61eba422a7a425f93a03f5064ba9c5
    role: context
  - path: pages/traits/genomics/pd_t4_4_system.html
    sha256: 0050401bc845947b287a427a7f522c7c220d6ab6aed2784672e05951821d7e0e
    role: context
  - path: pages/traits/genomics/pd_t4_5_system.html
    sha256: 26aa05fd3c54d1888bee0cbb787392ee8867d4bbd27ba57d60c07cdf4394b608
    role: context
  - path: pages/traits/genomics/pd_t4_6_system.html
    sha256: 4ef548ac165b42bb904a7652815ab8d4f6995a9c41912b5bad32ef4cfd93454d
    role: context
  - path: pages/traits/genomics/pd_t4_7_system.html
    sha256: 1fa6818595741a1bcb64fbfaf07d6171c3a3bbebc78fdc64b6928c12f1fa5e46
    role: context
  - path: pages/traits/genomics/pd_t4_8_system.html
    sha256: c5f96c4ddf76e574ec1f822402107abb8685ee772c6e28342d1c7788046fbe2a
    role: context
  - path: pages/traits/genomics/pd_t7_1_system.html
    sha256: 0fa24e7c07aeaa6f13e563d8e8c778166cc1777e760d4a1e94d6738fdef8525a
    role: context
  - path: pages/traits/genomics/pd_t7_2_system.html
    sha256: 7bf472e548fef0cec795640ba008f6b2b501bd23fd0f7aade222e9fb5a1d5cb3
    role: context
  - path: pages/traits/genomics/pd_t7_3_system.html
    sha256: 05297c4643c0cf0684aa9ce72eaacf76276191ef535e9371abbc1926807c407b
    role: context
  - path: pages/traits/genomics/pd_t7_4_system.html
    sha256: ccab39d88892e6af8a7b547acbf99630b8bc29c8fbad04ce54a458f731f70bb8
    role: context
  - path: pages/traits/genomics/pd_t7_5_system.html
    sha256: be56ce1343489c55ea4b5bbf14d798cec8de48b77efc4d67a86901aace4eb201
    role: context
  - path: pages/traits/genomics/pfiat_system.html
    sha256: 075fe9ceb3ed7bbf0ecacf689144ce00a2bb628c21f1b2176ed704531e565939
    role: context
  - path: pages/traits/genomics/phage_defense_system.html
    sha256: 7a3ebc34b757303f933a18bd0a5b777f85a6cd989f0f37c3a7aceac80752c307
    role: context
  - path: pages/traits/genomics/phosphorothioate_defense_system.html
    sha256: 44344b15256671bbc6d11d3c2d115bee71790a4e21795aa6d5b58119180b15a5
    role: context
  - path: pages/traits/genomics/phrann_gp29_gp30_system.html
    sha256: b2b81146d335cf57ffda0f58d35bf92fd28a2d09340a7ae191cd6c0e5ccc87c9
    role: context
  - path: pages/traits/genomics/pif_system.html
    sha256: f638d4a9642c1a3cea8853ee96855590c24aa05170074526f806edcda818443b
    role: context
  - path: pages/traits/genomics/plasmid_carriage.html
    sha256: 6bb0a2580db35f886bb5cb990d1c902b7533b3f3871b71f755ab0a821a76c313
    role: context
  - path: pages/traits/genomics/ploidy.html
    sha256: b8cd39e66032a8640dad4046887508a20c55a3bca4c145daf791ab638908e098
    role: context
  - path: pages/traits/genomics/prithvi_system.html
    sha256: 0eede9cd83414ce7c444e5b5bc3fd152531aa82dcb193ae05a60722c186f01a7
    role: context
  - path: pages/traits/genomics/prometheus_system.html
    sha256: a86a8ce9997263ea97b4afcdec8d827f953d992557f8e73fa8cc83965fbb248a
    role: context
  - path: pages/traits/genomics/prophage.html
    sha256: 3fabd4a8c223c9a063b9847ac94a05c53e66e475ff7ec99bd74cca51acd83232
    role: context
  - path: pages/traits/genomics/prrc_system.html
    sha256: 339e66fc4e6f9e20ff9beb65b6bbea2a4728ba768852a049d30d047edcf3bafc
    role: context
  - path: pages/traits/genomics/psyrta_system.html
    sha256: 2ac2d8d4a6708e9f5e519ce6d809214d4ac5b56418b84f2dc4a9ff2ad85eba42
    role: context
  - path: pages/traits/genomics/pvurts1i_system.html
    sha256: 7e86a42165abf8688be45efd9a0c3e21cd8a7ec9af97af2130238edbe03d77ac
    role: context
  - path: pages/traits/genomics/pycsar_system.html
    sha256: a982a5c9ea0cdcf209a548671b6aae47fa58b0ab4a656a4f61bbc292aa8a2cd1
    role: context
  - path: pages/traits/genomics/radar_system.html
    sha256: 5c72c6e3e3995c782b9ab2fc596c66c0d3477ed8cccb1de03d68136bcc872249
    role: context
  - path: pages/traits/genomics/razr_system.html
    sha256: c954de0f89630b39a2ff1f123306577a6cdaeef07d2f00aff2a9831df39ce594
    role: context
  - path: pages/traits/genomics/resolvase_duf5677_system.html
    sha256: 1c522a81ddce003862a3092f312e8308152b2461002b061cdaef4f53cbd95f72
    role: context
  - path: pages/traits/genomics/resolvase_kap_ntpase_system.html
    sha256: b834a4695ede708bba54dba1f2b6b4d318d12b0ba16ccfacb52fcb723f2f774e
    role: context
  - path: pages/traits/genomics/resolvase_schlafen_system.html
    sha256: 0b090c6ec30d310f4b9546d39ed804034c57b6410e0610ed34cf25a886cce61a
    role: context
  - path: pages/traits/genomics/restriction_modification_system.html
    sha256: 6c344bc8436ac68cb01f11693621c01e461426b2255152801b4b8144d9ca72ab
    role: context
  - path: pages/traits/genomics/retron_system.html
    sha256: 8c58486f99164562653cf2c6c3a5696678a549c829c78e84fc0e8d6aada3a2f7
    role: context
  - path: pages/traits/genomics/reve_system.html
    sha256: 3fa17484d4d6cf5b71a7dbb83d04f26763de2daf8becfebd683b765c510c19be
    role: context
  - path: pages/traits/genomics/rexab_system.html
    sha256: 4ddb7a492ea9eecdb7a4a5d23dee8d3196b3af8c425f3b58768bf194ed184585
    role: context
  - path: pages/traits/genomics/rhea_system.html
    sha256: e10cdfcc0663f44309d4962da5f3aa50783c6c577608060d37cb337978e5413e
    role: context
  - path: pages/traits/genomics/rloc_system.html
    sha256: 9cd5722ef3e798f53a821fde4c4fc9208588c222f2c829bc0d62953d291ed542
    role: context
  - path: pages/traits/genomics/rnlab_system.html
    sha256: 36a0c1a28c5089efae0e93c8205cbfccd234ca394b7d5fa5dce3d3b942aea2c6
    role: context
  - path: pages/traits/genomics/rosmerta_system.html
    sha256: cb81162decb97f5f3bc1671d75286e2ce0877d708cbadd7e0ab7441a4daae070
    role: context
  - path: pages/traits/genomics/rrna_operon_copy_number.html
    sha256: cefd35eb9c6d160c498802bae2fd13dfe5112436d819e224b6da6a99b08c087f
    role: context
  - path: pages/traits/genomics/rst_2tm_1tm_tir_system.html
    sha256: 27b3067124e1caf57209f979c458f728762751823b5606852027efb8aa5ec11e
    role: context
  - path: pages/traits/genomics/rst_3hp_system.html
    sha256: 7770db01ea67d80eda23e530eb97a163afd9f42d4462dd9187dedb9338f39761
    role: context
  - path: pages/traits/genomics/rst_duf4238_system.html
    sha256: b62f1304f726283127043d221678a3b9b16de006a442f9107c0684343f23b616
    role: context
  - path: pages/traits/genomics/rst_gop_beta_cll_system.html
    sha256: 878a1a2af838acf0c02eda5b085439228320d87ac5e94ac792eab935672f2f7c
    role: context
  - path: pages/traits/genomics/rst_helicaseduf2290_system.html
    sha256: 2f9ae74f9bc34fff5bf41840c2e248056a27c58a9dcdb15907764b594dd8666e
    role: context
  - path: pages/traits/genomics/rst_hydrolase_3tm_system.html
    sha256: a90e9378f995c0a731c1b425aa73b46127bb739417f538469dbb2b3470bea759
    role: context
  - path: pages/traits/genomics/rst_rt_nitrilase_tm_system.html
    sha256: 9219e7b687365df90ece7326ad2a0d8e0656710fdb18f60bb836f9d71a9ef35e
    role: context
  - path: pages/traits/genomics/rst_tir_nlr_system.html
    sha256: 389b98433311480d2db95827830cb36098aaf27848c16420915693263acaa95d
    role: context
  - path: pages/traits/genomics/rugutis_system.html
    sha256: 67c817aaa5e44fe3b40a5b42e4da069679323ce15c763b769792301d9309af3a
    role: context
  - path: pages/traits/genomics/sanata_system.html
    sha256: a995a5b90cdb15ae2cdef7abc1e0cbdd6512759551ebc9e4f6394a763c0de1cf
    role: context
  - path: pages/traits/genomics/scomcra_system.html
    sha256: 477606b835f13280febea1f2309700a38b2fe5a97d7712216157d28c11a6e786
    role: context
  - path: pages/traits/genomics/sdic1_system.html
    sha256: 5fb16899721e628e4c6bdff91b4b4f49e6418215ddf7549f8519b95bbb89d2f3
    role: context
  - path: pages/traits/genomics/sdic3_system.html
    sha256: 039bb5c522bc17aed73cc506e40a122da8dec2cf2bfbe9344725898953d7b63f
    role: context
  - path: pages/traits/genomics/sdic4_system.html
    sha256: 22877df17ae7d7d090c1fcb2a89cdfde8da4ac6e9d14ef05b5ae16e5a6093e85
    role: context
  - path: pages/traits/genomics/sefir_system.html
    sha256: d70d8ff1839cfbf873416c491f9a776ade1d80fd9fc5a91eeef5dd4d5490a540
    role: context
  - path: pages/traits/genomics/septu_system.html
    sha256: 16d984100d7cbbaeed779681491cbabb69afd416f2384408c6f80517464c29e0
    role: context
  - path: pages/traits/genomics/shango_system.html
    sha256: 5b47135197f5c87acd31b2639c652d4bdd758b97476a33373f64aeaedd76adb0
    role: context
  - path: pages/traits/genomics/shedu_system.html
    sha256: 057d1a378214e2ed6e5041465da48b86d08ea9f5ffb2585637f12aea362a72d0
    role: context
  - path: pages/traits/genomics/short_lamassu_system.html
    sha256: 0e865dbc1f21c0d55223279072b2c827657dd5b5177dd8e843533002a438f912
    role: context
  - path: pages/traits/genomics/shosta_system.html
    sha256: 157a6646e187045e763b677aa1b8acbfeb5f8ff88a765aed3ff6534c0164b2b5
    role: context
  - path: pages/traits/genomics/sirona_system.html
    sha256: ab30733fc1653af16f8c8a8139ae99c70de671f5522b691543df00eac81abbbd
    role: context
  - path: pages/traits/genomics/six_a_mbl_system.html
    sha256: fc1a8ee34eea42564bda07ebf1b3104d6fc4661bf89e0287e45ad74e91e11f01
    role: context
  - path: pages/traits/genomics/snipe_system.html
    sha256: c1c4b883767c52511b66b26d1473d2a4f9fc5c177c2e20355665caaf33c49e09
    role: context
  - path: pages/traits/genomics/sofic_system.html
    sha256: 697e79367405f8bb2d1a2bee02677d74b7f64ebb464a8c2e9e770ede31ce4ebe
    role: context
  - path: pages/traits/genomics/sparta_system.html
    sha256: c75e383c5393d7bc6991cdab93a22c4836c521470258726cada9d8d16494a1bf
    role: context
  - path: pages/traits/genomics/spbk_system.html
    sha256: a55e6394aefc7a38451ae0b782a9684b227583e73729be543784c45e7cf30b5a
    role: context
  - path: pages/traits/genomics/sspabcd_sspe_system.html
    sha256: c934477c106d6d6f1648eef96a1ccb3f9f829ebc7b1b93e73b96e6f58ef1e200
    role: context
  - path: pages/traits/genomics/sspabcd_sspfgh_system.html
    sha256: 3749ad1431e7a0004bafe6784f9186812f86a99a2990a40859b249748f1a8ed9
    role: context
  - path: pages/traits/genomics/stk2_system.html
    sha256: ddcf881ff48091a6b94d983071cefc36b02be3e6a3117d0070a2d5d1b5faa2ac
    role: context
  - path: pages/traits/genomics/sucellos_system.html
    sha256: 88ea6b1ad28368949d754281c3b30869ee9372b62938daad919ccee38753a5be
    role: context
  - path: pages/traits/genomics/tab_system.html
    sha256: 03e2034117f69ea59ce1ad06252ff22d6b88ca0299073609f323bc9ecc98a316
    role: context
  - path: pages/traits/genomics/tagi_system.html
    sha256: 673cd28328702c242c133085b025fa2ded853c958152d123f158083c8c46289d
    role: context
  - path: pages/traits/genomics/taranis_system.html
    sha256: 5a7c6872213dc81fc5820f95bca5c655d2b66bd9079cc994acab99fd97bc13c9
    role: context
  - path: pages/traits/genomics/tgvab_system.html
    sha256: f7e5463cbe38d7fee29deb97f997d227c6900866c249b1b24a99228eb932d0a8
    role: context
  - path: pages/traits/genomics/tha_system.html
    sha256: 5561f94f9b596969061fde27db847fe7a1d951047c4bf440a8d1719e56b097f3
    role: context
  - path: pages/traits/genomics/thoeris_system.html
    sha256: ae8feed24238dce9181a300fda8a1215c0a00f0bac47a7cbbe538096fb5f1c53
    role: context
  - path: pages/traits/genomics/tiamat_system.html
    sha256: 94c701d3eb1cca39e571537336a6d0c9e67145ea8c4c5ec83587afeefd349ed8
    role: context
  - path: pages/traits/genomics/tir_i_system.html
    sha256: 78149ce2fd2dacea8dbe9dbbcd6b9ea06db81560090f6bb31e7b819f85f3963a
    role: context
  - path: pages/traits/genomics/tir_iii_system.html
    sha256: 1895f163a86c1996f17098d577c66ba6304b165016abd278810c7e124dda150b
    role: context
  - path: pages/traits/genomics/tir_iv_system.html
    sha256: 019e4e7ce750205f45c28052b2c4cad395688345be60c30b37b4f0203cffe182
    role: context
  - path: pages/traits/genomics/tir_vii_system.html
    sha256: 1f0de9a0a56974cf25c15bb07ea91616fff69735b54cca9d355882602ea0d7df
    role: context
  - path: pages/traits/genomics/tir_viii_system.html
    sha256: 2f4e28c0b9c95f7d3beed5d7d3df75368f5b6c672833a7236bd83373a1be7da9
    role: context
  - path: pages/traits/genomics/toga_system.html
    sha256: 75c7e5cfb54b52d4c895cf1a72021469268f9986d5f6c2f1613d95e551868a7a
    role: context
  - path: pages/traits/genomics/toutatis_system.html
    sha256: 443d8fad6199f0d976ed84d72f91c01c3b11583bf7235a0a3080404715468cf3
    role: context
  - path: pages/traits/genomics/toxin_system.html
    sha256: f03504c03308e8e101b7a2a8a4214bb88a323e316db777711d12796b9603fc69
    role: context
  - path: pages/traits/genomics/transposable_element.html
    sha256: b6516df371632df613a7dcf4bbfe84a4c6a821f2c31cc5e819422fca334bedc1
    role: context
  - path: pages/traits/genomics/type_i_restriction_modification_system.html
    sha256: 75528c6c6430afad0be6db83847615943e072414dd9135449ee401c38e698874
    role: context
  - path: pages/traits/genomics/type_ii_restriction_modification_system.html
    sha256: 475ba7e9843a71ae1ca4ba1fc4a9a2c3494696c44064b0a9428bc3df26144d41
    role: context
  - path: pages/traits/genomics/type_iig_restriction_modification_system.html
    sha256: 12936f681163e5275f02350728df7d7213db06a94f7c74273164f500972ab590
    role: context
  - path: pages/traits/genomics/type_iii_restriction_modification_system.html
    sha256: 0d3795aa553964b5b1572a92324eab8e07e6fefc3ad42008ff333bf27beab18c
    role: context
  - path: pages/traits/genomics/type_iv_modification_dependent_restriction_system.html
    sha256: 33c9d6d2cb3aab9d1ad156bb5f844aa41cba4dea345772471271b2e9d2d80438
    role: context
  - path: pages/traits/genomics/ukko_system.html
    sha256: e877cc9d3132091d74b0c16acbf134e3316e80e565524611c1fdfe45c65f57f5
    role: context
  - path: pages/traits/genomics/uzume_system.html
    sha256: 47e6573b6f766850d3ec7b974d0494008ad8ceb0c1fe2ffb41726d2569fd2917
    role: context
  - path: pages/traits/genomics/vcam4i_system.html
    sha256: f3539127087ff8759deda9ff192fe392e58b70d2782e4145043a355e7cc4a707
    role: context
  - path: pages/traits/genomics/veles_system.html
    sha256: f3e2d1a0ebb54fd33353c1dfb46e612b8e8356286e37e138c4b380c37ecfdd38
    role: context
  - path: pages/traits/genomics/viperin_system.html
    sha256: c4dc22c213772af98b8393520cc0489d4c6c0b51f26d0ce1869ca2cb30681675
    role: context
  - path: pages/traits/genomics/vp1796_system.html
    sha256: 57613430c0d991c9c6ac126fc7064e603af38bf100221f5bb847e66b162dde2c
    role: context
  - path: pages/traits/genomics/vp1817_system.html
    sha256: c6996f374972c7cd6aa0526035c2240e802e20889cbac0dbfa53238aa36fcc2e
    role: context
  - path: pages/traits/genomics/vp1823_system.html
    sha256: 443f1d9f6913c7d69cd61b170bd92d95f5b21c5ccfd67068e53527de43e6fcec
    role: context
  - path: pages/traits/genomics/vp1826_system.html
    sha256: 650dc928b1fbf98be0b7737bad5ca576197be63b0ffc22ccbd09f0e641b1f5d2
    role: context
  - path: pages/traits/genomics/vp1839_system.html
    sha256: 04f94367d22c45c056f7dbfe3bd5a5b9e20dc66f1d2094d8749cbd05244d873e
    role: context
  - path: pages/traits/genomics/vp1840_system.html
    sha256: 5642f13e014a3314d7395ac29b6f4cd8c359d0af431fdd71ecafb04c6fc594c7
    role: context
  - path: pages/traits/genomics/vp1848_system.html
    sha256: f581efb0640942f1bb63a74b600f3eb5da1905a22dde951cd4a17a9b4a77b8d3
    role: context
  - path: pages/traits/genomics/vp1851_system.html
    sha256: 232a10b852ea8c899262adbf92a0a2cab29de45b9f30c427acee8fa0939251d7
    role: context
  - path: pages/traits/genomics/vp1853_system.html
    sha256: 1bd7699ea5e562ac0784a747ff665fffce34ae94e9b471bdb361fc1ae94b08a7
    role: context
  - path: pages/traits/genomics/wadjet_system.html
    sha256: 9a90c5ceb3e0342a79d58c429f0e600b9511bef3ad68e82b9cfe4fd80cd1cca9
    role: context
  - path: pages/traits/genomics/zorya_system.html
    sha256: 77d86d8fa85f0a1423d21d8d234f7351b8b003d87b2e07656bb0ff16e1e149c4
    role: context
  - path: pages/traits/genomics/zorya_type_i_system.html
    sha256: dd884766eeb08e7c07ec23913c6a841208627e28851f74e76e0e315dacd33b11
    role: context
  - path: pages/traits/genomics/zorya_type_ii_system.html
    sha256: 84dbd11ac7b78b010afcb2ecb6c413771c3a6331fee0bc301b01baa5657e4960
    role: context
  - path: pages/traits/genomics/zorya_type_iii_system.html
    sha256: 582f462f6fb6ac9270f82bdb6aa368fdbe3ab00550eff27b86d3c47f3b641217
    role: context
  - path: pages/traits/metabolism/accumulates.html
    sha256: 1d5b0d3561a1c76246fe437926de94b86ffe04761b7d51cf2f6966e913acdcf0
    role: context
  - path: pages/traits/metabolism/acetoclastic_methanogenesis.html
    sha256: aac8c8f106d339d638cdd15bdef7bbd4ee280b0eb47252534615c6b20767f772
    role: context
  - path: pages/traits/metabolism/acetogenesis.html
    sha256: 3c9433227e75a30dbcfbaecff5f6a47d3a632a3ab1eaacbde575dd3f6ab69ac4
    role: context
  - path: pages/traits/metabolism/acetone_butanol_ethanol_fermentation.html
    sha256: 67d56e2cba3a6cc04791db4797564291c283781f32a46e4cbeca31efdf603762
    role: context
  - path: pages/traits/metabolism/aerobic_respiration.html
    sha256: a22bf647806db63f8a2e090ad1a6fbde599ac7499e110b97af52cc04bd110f4a
    role: context
  - path: pages/traits/metabolism/anaerobic_ammonium_oxidation.html
    sha256: a1c63f7a53412d0c3d0c327136cbc1e54278bd1e389ee5492153d24fe353e17e
    role: context
  - path: pages/traits/metabolism/anaerobic_oxidation_of_methane.html
    sha256: 2c6a634e117955857be44313d31b919ca73a53692d38a5bdd2c88b59ec7dc117
    role: context
  - path: pages/traits/metabolism/anaerobic_respiration.html
    sha256: 1fe98c0af978c859ca3c8adb2844f5fb48d0df0f0c55404eb68f4fe9e222fa05
    role: context
  - path: pages/traits/metabolism/anoxygenic_photosynthesis.html
    sha256: e69c06e56a3b0e009c3e9598868efd23cef433d73c88f0735d5ba65d39e188db
    role: context
  - path: pages/traits/metabolism/aromatic_compound_degradation.html
    sha256: 5722ea764813b994ea54f81c2775771b1144b8b81d033763e233d690329640ea
    role: context
  - path: pages/traits/metabolism/aromatic_hydrocarbon_degradation.html
    sha256: 5027b751a93348b2c179e6b2c7d42380ea7ff16ee6b45c2a307694ba326f6dfb
    role: context
  - path: pages/traits/metabolism/arsenate_respiration.html
    sha256: 776cb711a34ac347a3e3fd82a298ff0de3dc6ce7f83b09efaccb39275a8e9f8a
    role: context
  - path: pages/traits/metabolism/arsenite_oxidation.html
    sha256: e27bd45c0d02b5bb3a9946f3ce1b17c39649757339e7fd43b8e7e22bb7496ec8
    role: context
  - path: pages/traits/metabolism/assimilates.html
    sha256: 4ff9e13c5d86b627cf3494d251168cc0fc35d98e4d778e3c375ff03e061b5782
    role: context
  - path: pages/traits/metabolism/biopolymer_degradation.html
    sha256: 710b9fb3154cfdb34f5f5adbcb6b73bbbf6ad7f93d7b3869aef064998513b79a
    role: context
  - path: pages/traits/metabolism/builds_acid_from.html
    sha256: 561b4bb9222a6663221d04263cf39adbae8669731fda4b4ed8d16a1281e7f2f4
    role: context
  - path: pages/traits/metabolism/builds_base_from.html
    sha256: 6ab482bd1ac7aac22ed216c54aed943d1b000ecb440616c6e956bfa155a3225d
    role: context
  - path: pages/traits/metabolism/builds_gas_from.html
    sha256: 4696da61491ed037debe8d596370f104ee51e11ee7e7124e3ea8ed01359a8c9f
    role: context
  - path: pages/traits/metabolism/butanediol_fermentation.html
    sha256: 8efe7f8ebb179013eddb9eef80cf576e8275a44d387e6d1d6732b817b6f950c2
    role: context
  - path: pages/traits/metabolism/butyric_acid_fermentation.html
    sha256: 060332b5ad467a163e23efabdfa3ba488f7816a7d707e56fc2daec7eab885df9
    role: context
  - path: pages/traits/metabolism/cable_bacteria_metabolism.html
    sha256: 9dfd9da1bf230de9a7210bb02cc4eb45c913d660eca4d05ef02ef3dfd0f10e35
    role: context
  - path: pages/traits/metabolism/calvin_benson_bassham_cycle.html
    sha256: 1366893f27f432e750fa456fbba2121008ba3849c2a03ae511f7a603252ce942
    role: context
  - path: pages/traits/metabolism/capable_of.html
    sha256: f96b5dfb2f82e7a53bc93ea549a770891554b1b79d185ffe43b0d5cc7507515b
    role: context
  - path: pages/traits/metabolism/carbon_fixation.html
    sha256: 7efa44743c17dc06343ad606f15b2327e1df7e7b8d3df7cf866ddba47ee52928
    role: context
  - path: pages/traits/metabolism/cellulolysis.html
    sha256: 781f6ebc828ae05ae21d7c00b0324efe4716f885e9959a3995dae44045fa5389
    role: context
  - path: pages/traits/metabolism/chitinolysis.html
    sha256: 562546425d16b4579cc626f504564af49a48b496d945e61a93bc8f18485bdaff
    role: context
  - path: pages/traits/metabolism/chlorate_respiration.html
    sha256: 417f79c45dda40e17ee2ec966b60f30d93d9a363bee3b528ba4779db2a5ae9e3
    role: context
  - path: pages/traits/metabolism/citrate_fermentation.html
    sha256: 75a106b56f7abe336850c58960c904e081c2162840553d1c8c228ab469ea61b7
    role: context
  - path: pages/traits/metabolism/compartmentalizes.html
    sha256: 343c8cf37942fd4d1366b194e56efbd9ca9dff5d1c5a885c989e9ce0001c6999
    role: context
  - path: pages/traits/metabolism/complete_ammonia_oxidation.html
    sha256: 97845127dc9f75ff37e7c63e2b72aa6770106592144a2d4b0ef65ea6a9204f5b
    role: context
  - path: pages/traits/metabolism/dark_hydrogen_oxidation.html
    sha256: 565255818dab8e77cd53e44e5236d29d6a1652040186ff93ef7d2ddafbc48977
    role: context
  - path: pages/traits/metabolism/dark_oxidation_of_sulfur_compounds.html
    sha256: 17b68b46bf65cc57897d8b50713a444e4bf7591b878832fad7ac191cda080d29
    role: context
  - path: pages/traits/metabolism/degrades.html
    sha256: 811058f9bcef2a0ad5b046e628fa2e4e02c88d79513cc05fc8bd58eb53715ce3
    role: context
  - path: pages/traits/metabolism/denitrification.html
    sha256: a08959910b5aa1fba05d8fa7ea164104c6805bdf48cf4670e87543442e8f6e7c
    role: context
  - path: pages/traits/metabolism/dicarboxylate_four_hydroxybutyrate_cycle.html
    sha256: e83dd5ff1f99a05cb82e84049b629ab941e3cc55dcef927e65a4890d27222d5f
    role: context
  - path: pages/traits/metabolism/dimethyl_sulfoxide_respiration.html
    sha256: d4085b05b36f49e4ebdc162070fa50449da7f0267f5b9da98e7c562ea6b7f3c5
    role: context
  - path: pages/traits/metabolism/disproportionates.html
    sha256: 7a2062587626108ad26b8fe05fc737194cb7907a9d66aae7e0128a42ed47d1d6
    role: context
  - path: pages/traits/metabolism/disproportionation.html
    sha256: 12865cb6a94bbc10b8afbbf6baa15e41e0434fca29b502064139e2080c403347
    role: context
  - path: pages/traits/metabolism/dissimilatory_iron_reduction.html
    sha256: c6fe8063932d17ddce878c39b4fe7a9f5ee80e64c8696237b582cf78a3a09237
    role: context
  - path: pages/traits/metabolism/dissimilatory_manganese_reduction.html
    sha256: e6b7423f32e20629efe0c1e2d8633b31b14699ec105d67d64818288f7ddf1f0d
    role: context
  - path: pages/traits/metabolism/dissimilatory_metal_reduction.html
    sha256: 2135e83e92f6e168fbe27b09cf9185c1094489faa8e72a5ad09b2a4190d20659
    role: context
  - path: pages/traits/metabolism/dissimilatory_nitrate_reduction_to_ammonium.html
    sha256: f3c32f05ff3d7c3e4c5a9eb3e28b1d0b33ce6c4abfc9ac85323160f91093cbcd
    role: context
  - path: pages/traits/metabolism/dissimilatory_sulfate_reduction.html
    sha256: e3e37c60ed2b7e7e1b0c0bc0ca58cc5cc3f05e409dc327ea33e95b25074f6010
    role: context
  - path: pages/traits/metabolism/does_not_accumulate.html
    sha256: c3ab57e2b4722f5acb87093567878ef3e5abd8952e2e4d8f39aef14df8b97524
    role: context
  - path: pages/traits/metabolism/does_not_assimilate.html
    sha256: cb92862e755ac90624c04357a8f46e657a56969b381b03a1c84d97efd330b911
    role: context
  - path: pages/traits/metabolism/does_not_build_acid_from.html
    sha256: 8b365d82e461c79a34aa35e49344188826ff74e052ec99c93e0aa7a53a9a5bdf
    role: context
  - path: pages/traits/metabolism/does_not_build_base_from.html
    sha256: e83e53c546b9a91f33f61cc447ce53a6914dbb98eceb232d5d1c6857132cf35f
    role: context
  - path: pages/traits/metabolism/does_not_build_gas_from.html
    sha256: 24e9db5c09756c09779f80bb1e428ab573f5ff89c2cadb7487a357dec4bdf6b5
    role: context
  - path: pages/traits/metabolism/does_not_compartmentalize.html
    sha256: 2f962de636441ac20dd375cc29556f85b4b2347733d0899b221fb125a74fb71e
    role: context
  - path: pages/traits/metabolism/does_not_degrade.html
    sha256: 0d30b1b27741f2670b63a620ce7ff2c9b55294839df52f16a3c767ec07fdcd18
    role: context
  - path: pages/traits/metabolism/does_not_disproportionate.html
    sha256: eeadf5848368043330119cb601d6bd833e67d3e974a9fc7ca1b671f726961ce5
    role: context
  - path: pages/traits/metabolism/does_not_export.html
    sha256: c6dddd66adf921ad94b79c265e88067581b950bd732521bff324382455d0071b
    role: context
  - path: pages/traits/metabolism/does_not_ferment.html
    sha256: e6f0f8b50ae6bad9ae15abbc47ad9fa3d9bf57498be075a880b2cdc5bc1f506f
    role: context
  - path: pages/traits/metabolism/does_not_hydrolyze.html
    sha256: a40e3f72a72c6eb680bfdf7bc96a393ea4c7e16f6bdf8fb15158b0076588c761
    role: context
  - path: pages/traits/metabolism/does_not_import.html
    sha256: 57df6b3366e0a958d5428e8a45f1feaf84fcb920db8b9368c64941a0ab583519
    role: context
  - path: pages/traits/metabolism/does_not_oxidize.html
    sha256: d527933d1dfd62f6172c3f4b73c8064fe6f755ebf5f2130c23b3fea64e40f63f
    role: context
  - path: pages/traits/metabolism/does_not_produce.html
    sha256: 2db3b6f49b4bc0439221b59922aed5c6b746fcbd8f85ddb5ace2b4dfce7e544d
    role: context
  - path: pages/traits/metabolism/does_not_reduce.html
    sha256: 3549e2c5cc97d675b07fdefb118ce22a53655c2063994585118bf49391d2f409
    role: context
  - path: pages/traits/metabolism/does_not_sequester.html
    sha256: d9387ee75b4e40cf334c4dfac93f3e3a9dbdf56980a4ece36772cbc1953e5841
    role: context
  - path: pages/traits/metabolism/does_not_show_activity_of.html
    sha256: 7b261a386ba5afc22e5c326aee7a2db74aab029f0e012bd864bbfa4cb25dd66b
    role: context
  - path: pages/traits/metabolism/does_not_transport.html
    sha256: ac769aad066f13b32630015c3a4b56e3e042ce7f0b2f3114eff53ffdf901e7cb
    role: context
  - path: pages/traits/metabolism/does_not_use_as_carbon_source.html
    sha256: fa16e79e4f891549612f2f1fdc78a10f5492210e4e0f10b029218d427ff84613
    role: context
  - path: pages/traits/metabolism/does_not_use_as_electron_acceptor.html
    sha256: 6468c2d29656beab5939b2bc905dc7e8d115761d6cf2e4d37e540940b3e20f4d
    role: context
  - path: pages/traits/metabolism/does_not_use_as_electron_donor.html
    sha256: 3414657ae11d494189605e4e9e8c86d1af6fe661030f880fca7f4079a3bfb4f9
    role: context
  - path: pages/traits/metabolism/does_not_use_as_energy_source.html
    sha256: 9cff9da43b01e68d9dee35658c5dbc49650d509fae3603e09eecd8f89b3286b9
    role: context
  - path: pages/traits/metabolism/does_not_use_as_nitrogen_source.html
    sha256: c06fa88ca5f74e8658399d177c881d62e485169783e3518ba0b838df4874789c
    role: context
  - path: pages/traits/metabolism/does_not_use_as_sulfur_source.html
    sha256: 1fc6a459292a757ff62c82693e4747eabc2c44193e3b0dc4343607179808c642
    role: context
  - path: pages/traits/metabolism/does_not_use_for_aerobic_catabolization.html
    sha256: 90f4cd8a38d16e54aed45f3f9061d5c9babe610f63de346bf3ff51e2e60c04cc
    role: context
  - path: pages/traits/metabolism/does_not_use_for_aerobic_growth.html
    sha256: 10d7befc45ea3a6e99a018d1cd8fe174c1902704a0579503ebe979d79b540653
    role: context
  - path: pages/traits/metabolism/does_not_use_for_anaerobic_catabolization.html
    sha256: 99a3d5638f9b52b0d94305318985f8947dcc1f95b50bd9b59532ca663e509dd5
    role: context
  - path: pages/traits/metabolism/does_not_use_for_anaerobic_growth.html
    sha256: 0efb0b0424743e9c50fbc28e6027ca3a616451963748bd58e3fd598590462c2c
    role: context
  - path: pages/traits/metabolism/does_not_use_for_anaerobic_growth_in_the_dark.html
    sha256: 048bac32e96d3f462818c0db7c704c2d88d0a8051bb68b7f0b705e98a9817dd4
    role: context
  - path: pages/traits/metabolism/does_not_use_for_anaerobic_growth_with_light.html
    sha256: 12afe8a447e5d360b9eb8c756b81f3681ad9d0572008add441d001266a07f5d0
    role: context
  - path: pages/traits/metabolism/does_not_use_for_growth.html
    sha256: cc2a024847798610665d0ffbdfbf16d60a9225008487e41a6dd0d631c504f9be
    role: context
  - path: pages/traits/metabolism/does_not_use_for_respiration.html
    sha256: e6416ae12af95af54bee60271d428b93c0833e7edbf8b1e88f02d4dcd3156521
    role: context
  - path: pages/traits/metabolism/does_not_use_in_other_way.html
    sha256: dbc037acd881e5a37fb1d53853265b8e6be889f1268938fdc4d1bffb29f26cce
    role: context
  - path: pages/traits/metabolism/electron_transfer.html
    sha256: bb1e7a28b2e4a7d5481c23cbba24dd9583ece7952be5bf5012488dd5c7913c65
    role: context
  - path: pages/traits/metabolism/enzyme_activity_analyzed.html
    sha256: 5cd63ce72e9c729d47b9fefa1de2f962f1a9e1a6e51663de68283697e3cd879a
    role: context
  - path: pages/traits/metabolism/ethanol_fermentation.html
    sha256: d5475461446d9b51eaad645e592a3bc5dd6bd8e0302c25b0ba90a2fabddacd1d
    role: context
  - path: pages/traits/metabolism/exports.html
    sha256: 94ca9cd399c950316cac87278b1011ff802ef709bbe967a56f28e2258650b8ae
    role: context
  - path: pages/traits/metabolism/fermentation.html
    sha256: 9557ae1c2bb3d0ea94e60f7cc5f763644e5e0c91ab9876d3c94dd3089278fd44
    role: context
  - path: pages/traits/metabolism/fermentative_hydrogen_production.html
    sha256: 8f5796c87d90f6532426a3f3f72e7cc68752db1f1c1e11ca1657a148d70f68ff
    role: context
  - path: pages/traits/metabolism/ferments.html
    sha256: 53231865882ed9eadd144dbbbdec17c07202aa88fc581ab36f4dd9a469da9aa3
    role: context
  - path: pages/traits/metabolism/fumarate_respiration.html
    sha256: f80691889c1bd6b20086deb20817f239a7765f4bbc49adb6274c3440c54854e5
    role: context
  - path: pages/traits/metabolism/has_growth_nacl_observation.html
    sha256: 650788f230218a9b9ef8d4b9185c8107865b38a3825cbb7b2e57161ec9db84db
    role: context
  - path: pages/traits/metabolism/has_growth_oxygen_observation.html
    sha256: 7acbfdd40294b1ae7deafc5e941dbd0ed0ca9f22d404b7799328a3c86643138c
    role: context
  - path: pages/traits/metabolism/has_growth_ph_observation.html
    sha256: f84327388a28041519885f81bf21546c0032e0fc1e7f78337a312e0e01591c10
    role: context
  - path: pages/traits/metabolism/has_growth_temperature_observation.html
    sha256: 2d7f4d8e5fd6859f565414f25a80063de4d791046102ade31fdf774a7f25e7c3
    role: context
  - path: pages/traits/metabolism/has_nacl_delta_observation.html
    sha256: a0b9af6d5c9d0f60905c7c889e764f89e4fa5153c0d7b7b7807e788066ebe580
    role: context
  - path: pages/traits/metabolism/has_nacl_observation.html
    sha256: 3e18165a5379aa29f3e8db27279e7b626bd2470a06a9c1272cae260f4ce38e3c
    role: context
  - path: pages/traits/metabolism/has_observation.html
    sha256: 27e71c096a48aca19ecaa42a891813cd4fd00b0a875f23756b875dcffcbcdcfe
    role: context
  - path: pages/traits/metabolism/has_optimum_nacl_observation.html
    sha256: d90f73bcc74d09b0cd1c9152f192a172154d7c9bd0129fb8214cdf20a0aaf6df
    role: context
  - path: pages/traits/metabolism/has_optimum_oxygen_observation.html
    sha256: 9c36127ecb0c7a91ca46017f8a72a5929ed5411264bbf5e7df377b591ec7690c
    role: context
  - path: pages/traits/metabolism/has_optimum_ph_observation.html
    sha256: 1929775b679314f8d408fd50d95ecef01e0d77e69d72d0e9f3c2df8356a7520d
    role: context
  - path: pages/traits/metabolism/has_optimum_temperature_observation.html
    sha256: 70e6fb0e5081053290290234d5cdd11dc24cb6df891bdfe2fd2d6f7b753afca8
    role: context
  - path: pages/traits/metabolism/has_oxygen_delta_observation.html
    sha256: 75deb67765eab3ae0349c102d938b1f9c914ceeb0bcaa096e3363f3d4e9f2c88
    role: context
  - path: pages/traits/metabolism/has_oxygen_observation.html
    sha256: 53ebf002870907cf88eddf2da50ad73ebb33795e0327ad0f17383e5f4a6499c1
    role: context
  - path: pages/traits/metabolism/has_ph_delta_observation.html
    sha256: cb250a9cbf5ce275b4ff3155517421bbbf751b5c3f6bb87d358bd84a8fef9507
    role: context
  - path: pages/traits/metabolism/has_ph_observation.html
    sha256: 5eeae93a1fccdf87689f24e465fa0a01cf91f2425cd966cd389e7e7f10256396
    role: context
  - path: pages/traits/metabolism/has_phenotype.html
    sha256: 0d8aca842caf484eb718b8aa9094239bf8457e568f1580ddd11bdf2664dff1c0
    role: context
  - path: pages/traits/metabolism/has_quality.html
    sha256: 61f151805a584ce69aca51f2d822be8d213181ac9c141388f9858b2081d9a43e
    role: context
  - path: pages/traits/metabolism/has_range_nacl_observation.html
    sha256: 0068a120b841acafdb0d4f72e69ae36036b66a63493c6737bf8a39331c57e834
    role: context
  - path: pages/traits/metabolism/has_range_oxygen_observation.html
    sha256: 7d9c76b3c9244d26f4c285e3690fe28a50b8c9c0c0ab8f82b9cc9ffaa8dc09f5
    role: context
  - path: pages/traits/metabolism/has_range_ph_observation.html
    sha256: 86060d486ac35900268bee00184955bc7d2e7596b9f9818fbb285112b0afda6d
    role: context
  - path: pages/traits/metabolism/has_range_temperature_observation.html
    sha256: c4c35bc5167462e304b3328dbd73d99a5882e3affc4b48c1d2a6e0cd17a4b0c2
    role: context
  - path: pages/traits/metabolism/has_temperature_delta_observation.html
    sha256: 6c8a62feaca35a62121593ce62d46dd295e188aba70e8b18a10146379132fb88
    role: context
  - path: pages/traits/metabolism/has_temperature_observation.html
    sha256: 00889e1b3848acb66b6d103751592e8f1451b3de4d293987bafd5781d87bcd11
    role: context
  - path: pages/traits/metabolism/homoacetogenesis.html
    sha256: c008d393af9204159de2ca5907715868ca89d8374525c508fe2d3d7735fa6e67
    role: context
  - path: pages/traits/metabolism/hydrocarbon_degradation.html
    sha256: b91768fdce45d2f06b66dd456d453a4d7021a14c89b55cbbd59ef8f7f6574dd2
    role: context
  - path: pages/traits/metabolism/hydrogenotrophic_methanogenesis.html
    sha256: 00f4946b57fe1648ee154430abf714558f82d8ec7ebb7a51879cc1b1fceec81b
    role: context
  - path: pages/traits/metabolism/hydrolyzes.html
    sha256: b9f417bdcd557abf52909b9359fc6d64e04c2b4a8d3f65a59a734699deb3bcf9
    role: context
  - path: pages/traits/metabolism/imports.html
    sha256: ebd0f7284e0524ae2e62549ddab23f47b91e8927e6b6dc964bd66baa926cfdb1
    role: context
  - path: pages/traits/metabolism/iodate_respiration.html
    sha256: b4f1cb8c97f409ac63adcdfd53acce1148ed60978a232a79129002aff41da280
    role: context
  - path: pages/traits/metabolism/iron_oxidation.html
    sha256: 96b52b5b860cd0ebcc98bbe31f2f835ed6e94cf152203dd62dee4d688ba3cbd3
    role: context
  - path: pages/traits/metabolism/is_not_required_for_growth.html
    sha256: a7c9d255400caaaf70cd637791963c479e59963ca72a70ffde7e5dff40d7f8d7
    role: context
  - path: pages/traits/metabolism/lactic_acid_fermentation.html
    sha256: d46734f323809f750e17608c8d708f94feb0ed3e55873484d4b6da0fb2b461bc
    role: context
  - path: pages/traits/metabolism/lignin_degradation.html
    sha256: e4039bfcfb8d6308c4616d2e36bea90dcaa2b416db69e587d54873544388115d
    role: context
  - path: pages/traits/metabolism/lipolysis.html
    sha256: 62e03e17bc139b42e76c4ba7117b1ef64a63733bfa4106ded1828d898ef676da
    role: context
  - path: pages/traits/metabolism/manganese_oxidation.html
    sha256: 03c6125d4aa83d4d23973a95ac001e0837e4f324f45381c275458e701f5da737
    role: context
  - path: pages/traits/metabolism/metabolism.html
    sha256: 47d19d78f80720b6ee7a3748e3219bdbf203035f9f9d990453e725cd2d02aa18
    role: context
  - path: pages/traits/metabolism/methanogenesis.html
    sha256: 6eb49c3f619abb351a65ee2c8d7bb12be0ea734d28757b50fe058f3e18f7f715
    role: context
  - path: pages/traits/metabolism/methanol_oxidation.html
    sha256: 0eaf8622f3725cd42cf0e74461fc1fc42b8ac5a74d46f23312947321b7d37048
    role: context
  - path: pages/traits/metabolism/methyl_based_methanogenesis.html
    sha256: 6e01687cd59760b2f858c3bf6fa513c2a6ed7071c1d333e92cbeda258e5f21e8
    role: context
  - path: pages/traits/metabolism/mixed_acid_fermentation.html
    sha256: df6a0f5023f280a3c9bb5c0857efb9b9a7ecdb2d1f6662dca701a62014f4cad3
    role: context
  - path: pages/traits/metabolism/nitrate_reduction.html
    sha256: 7f8af651297a42f4fc8f0570cd10a0b11c6faa0f1252fe57a7002859f64e8189
    role: context
  - path: pages/traits/metabolism/nitrate_respiration.html
    sha256: 27d964404667d2c0ea9b1a00958d72368f1fd276ad50e703804f33c4f65ea567
    role: context
  - path: pages/traits/metabolism/nitrification.html
    sha256: b1c817752203cd348901d52705366071776861435406181b531b57800444c38f
    role: context
  - path: pages/traits/metabolism/nitrite_respiration.html
    sha256: 258b02697d74bd3148245a9d13f46a8c48c2c78335285ac108a571f713e9aa13
    role: context
  - path: pages/traits/metabolism/nitrogen_fixation.html
    sha256: e9680399437c2e1c346c4c8d8755b912ebe1aeb0a943a8529754d085de14abed
    role: context
  - path: pages/traits/metabolism/nitrogen_respiration.html
    sha256: 19de4549730fb1848cc8afe82c463c917d5ef5dfbe69cc8273802ea11e3bdb47
    role: context
  - path: pages/traits/metabolism/organism_interacts_with_chemical.html
    sha256: 35d99b8277e8178723d03e1774c6e0f42679e7827d00b081945d2f33585edcf2
    role: context
  - path: pages/traits/metabolism/organohalide_respiration.html
    sha256: 3d096f11ceb87244fb20e812fce9f7ddd4d6e735704b0a3e8f0ad826d8a51534
    role: context
  - path: pages/traits/metabolism/oxidative_phosphorylation.html
    sha256: d3d5cfd4a1d4a6df0af00541ab5af528ec7e70b5e77be1d25918a885db5f3479
    role: context
  - path: pages/traits/metabolism/oxidizes.html
    sha256: 7a858e0d2f9d984820d56f246f95ef22588b5e53fd1c9fc37d45aa14e65fce54
    role: context
  - path: pages/traits/metabolism/oxygenic_photosynthesis.html
    sha256: 7369ba021d1258a633966172b411d224c7f870b98f44a190630ce6bd6541e762
    role: context
  - path: pages/traits/metabolism/pectin_degradation.html
    sha256: c445a35ca00093703ef769141a83531604e2c27ef192ddbc0fd3842e2923f772
    role: context
  - path: pages/traits/metabolism/perchlorate_respiration.html
    sha256: 7135bd84e0941698fd313cff636ce17e155c403111253a4feec5002ca8b0d368
    role: context
  - path: pages/traits/metabolism/photoferrotrophy.html
    sha256: f11d5eac6c6035e6121455a67c118288c472e08abbf03732f74ccaccdb14a6b5
    role: context
  - path: pages/traits/metabolism/photosynthesis.html
    sha256: 28e2bb75919c0f5967df853e0d34a91c9d6d83016de7b8ff5a02ba5ccd64e7e2
    role: context
  - path: pages/traits/metabolism/phototrophy.html
    sha256: de9aa7955cc4200ef16dbec9451dc3fe4246f7fb212508c00131254720447c65
    role: context
  - path: pages/traits/metabolism/produces.html
    sha256: b2a319f6162735b4fe2bdbde85c92741a8924343519351cbf3bfe1fb159c5c04
    role: context
  - path: pages/traits/metabolism/propionic_acid_fermentation.html
    sha256: 5a902ace3c6e6def16b189c65983db231809648a4c310c6e70ab6ac03c92a563
    role: context
  - path: pages/traits/metabolism/proteolysis.html
    sha256: 313d575c85cce14bcde6a4d871c157af56c6b530c1d1bf69c6a93db25c9d5abc
    role: context
  - path: pages/traits/metabolism/proteorhodopsin_phototrophy.html
    sha256: aa0c4c527f2c4d5f490aee3b770a9c1a93efd718fd185af1ded2a10c70850a57
    role: context
  - path: pages/traits/metabolism/reduces.html
    sha256: b02486123533aeac259f026d53c3ae12f1028cd0be6802528f8b2d2be67cc888
    role: context
  - path: pages/traits/metabolism/reductive_tca_cycle.html
    sha256: 40c6330ef06c8438634466bebd9376d458be10d50d59e641c0e372825e78f9ae
    role: context
  - path: pages/traits/metabolism/requires_for_growth.html
    sha256: abd3e13ad038897869c4f3c990d512bcfcbb1093eca659e7e81e899837961a7e
    role: context
  - path: pages/traits/metabolism/respiration.html
    sha256: 27715f4e1c77a7d96b0fc5a1ae4f6ccc816ee7c2f6494314f9613f8596cc750f
    role: context
  - path: pages/traits/metabolism/respiration_of_sulfur_compounds.html
    sha256: f0f1e2a9dc9406ab187ce63f9f4d80b465b2f5e7c2b5f06eae7aa022fc4a9b70
    role: context
  - path: pages/traits/metabolism/selenate_respiration.html
    sha256: a94a26828ce40c171c164443f6c9f68a481b93f1c25eb85c1ea6bdc1d357d8b4
    role: context
  - path: pages/traits/metabolism/sequesters.html
    sha256: d72eba8351551ae98a11bb300c09e8cf0bcfacd4ac5a97614d66ba004c39fc51
    role: context
  - path: pages/traits/metabolism/shows_activity_of.html
    sha256: 289c97dbb5b6bc3f6028afa9ef75f0a7a9fdb3bc7aabc5aff03d8a97a16b8733
    role: context
  - path: pages/traits/metabolism/starch_degradation.html
    sha256: fadafc17088b6e07ec4f3fdaa9fe5172fa8562b0a7de910d8c160d3923cca011
    role: context
  - path: pages/traits/metabolism/substrate_level_phosphorylation.html
    sha256: 36f9f3e824e80587dfbc93d6898cfc09c71f84f03c2a090f0ba2f6c4e6ecaff9
    role: context
  - path: pages/traits/metabolism/sulfur_oxidation.html
    sha256: 4353ddd770b7dad2c45a9d0166fd4b34d2129bf21eb291e5af9142a45cd899f4
    role: context
  - path: pages/traits/metabolism/sulfur_respiration.html
    sha256: b60ff3bf2370c9c7957c46122e50255f44279072308b41309551c568009cf787
    role: context
  - path: pages/traits/metabolism/syntrophy.html
    sha256: 608eb22f3fa5ad0012e1eee9335aef638b6eb0a287c92573021cd2ae2b4e8319
    role: context
  - path: pages/traits/metabolism/tetrathionate_respiration.html
    sha256: 22200c7686b212aac2efad8564d04e4dfe60abc298d1c9079b67fea252ae052e
    role: context
  - path: pages/traits/metabolism/thiosulfate_respiration.html
    sha256: 73dcb5d13133cd0c29dceb394fa5af86c6940fddc5eb123ee54012192d90fe63
    role: context
  - path: pages/traits/metabolism/three_hydroxypropionate_bicycle.html
    sha256: 130a4f63fe739512b259f989530416b80c92e05f3af4ea7c0d52b940cca7bc69
    role: context
  - path: pages/traits/metabolism/three_hydroxypropionate_four_hydroxybutyrate_cycle.html
    sha256: 82b7df0244d8e3b5d7f2c13c86a7131bc1ec19ef5f6cc9d4e424bcfa1cbfd0d2
    role: context
  - path: pages/traits/metabolism/transports.html
    sha256: f79c56c638edfa5ab01471b3ac39ea357969d035f67df0cdfcba7d0ab307016f
    role: context
  - path: pages/traits/metabolism/trimethylamine_n_oxide_respiration.html
    sha256: 211c05175ee6ade8a0dc504ec3134429e8788fc80f127cd0c82c0a738a0928ae
    role: context
  - path: pages/traits/metabolism/uses_as_carbon_source.html
    sha256: f6afd62de80807138cc1068ab26501b71eb0acb38bf6c449dd472d8851a35687
    role: context
  - path: pages/traits/metabolism/uses_as_electron_acceptor.html
    sha256: 37d6adecf389ae4407fc7727b09798b46f6e344bba9c0b387ccffb443c31eb38
    role: context
  - path: pages/traits/metabolism/uses_as_electron_donor.html
    sha256: 87ab298a73cd544dc2e1a0bea0e6b43dd69e7972b70f5426cb0e5095a64af625
    role: context
  - path: pages/traits/metabolism/uses_as_energy_source.html
    sha256: 6f144f2e91d51393bdf3444f395e0595acca885a08af15693965b97cb792668d
    role: context
  - path: pages/traits/metabolism/uses_as_nitrogen_source.html
    sha256: 4d7c05ba60f41e1811f56eaaff06c35703cdc42d20ddc82ce50c22203ebe88ae
    role: context
  - path: pages/traits/metabolism/uses_as_sulfur_source.html
    sha256: f7d90eda93682ac1b404355bca6b77d0dd104c89b15ba82c68e1a6179810a29f
    role: context
  - path: pages/traits/metabolism/uses_for_aerobic_catabolization.html
    sha256: de69d4086f46da0d4489ed09657a9361e8268477ebb69acdf890368134f785e7
    role: context
  - path: pages/traits/metabolism/uses_for_aerobic_growth.html
    sha256: e995923c24d88f60e289701db7258d072d75b21d6bd10450ffd9993d7de4d36d
    role: context
  - path: pages/traits/metabolism/uses_for_anaerobic_catabolization.html
    sha256: 919e92de30a550b43c453e895900dcf9175db883a22e3175a0f454377e990b18
    role: context
  - path: pages/traits/metabolism/uses_for_anaerobic_growth.html
    sha256: 722294392cd701fc7165328325eed12a6043c8a34c5ab9f3d03645b60e86abe1
    role: context
  - path: pages/traits/metabolism/uses_for_anaerobic_growth_in_the_dark.html
    sha256: 555b3f3ea1b833b4bb8f0fa5fcd5b71074a7386213b4eef232b9cee48d138042
    role: context
  - path: pages/traits/metabolism/uses_for_anaerobic_growth_with_light.html
    sha256: 2be17b76c5827937efa763b1c35853632753ca4910505b8986b65ff5c80befeb
    role: context
  - path: pages/traits/metabolism/uses_for_growth.html
    sha256: 9f26809f0a524796005f13c59a9cdce94944f55958258eac0c2b0c6dbbfc8a1d
    role: context
  - path: pages/traits/metabolism/uses_for_respiration.html
    sha256: bb40ec79be25af016281777e29ff7372bb47883f7ed57c7eff9975f9c85a6b4d
    role: context
  - path: pages/traits/metabolism/uses_in_other_way.html
    sha256: 411354c2aa011154a6942c8bb5307d88628b0ee10c8828cf29fa7951acee9f7d
    role: context
  - path: pages/traits/metabolism/wood_ljungdahl_pathway.html
    sha256: 71b2b086369b246ac8a9729a22ce3f8ada4f179f37f0fb0b93b14f691a3b0f77
    role: context
  - path: pages/traits/metabolism/xylan_degradation.html
    sha256: ac4f82ff4f6350cc1c7b69b97ea3b54e7efe15982b3f79d51839201052682390
    role: context
  - path: pages/traits/morphology/akinete.html
    sha256: 17528c4f60ae1c100a2e5cc940e141fc42de90a7d0c3f859579d8ba0729c58a2
    role: context
  - path: pages/traits/morphology/amphitrichous.html
    sha256: 2e2a894025df65557b0eb03cfe8bddc8283307d9d020ea52bd1f12e14099bb76
    role: context
  - path: pages/traits/morphology/axially_filamented.html
    sha256: b6056fb06644dd440f24ca89b96806f6187d9eaf1ab1168e662b6eaf40395fbf
    role: context
  - path: pages/traits/morphology/bacillus_shaped.html
    sha256: 39ceffed86665f7f54c7c0e5904f07232409779f8b5a8732981ba5aa81dc8beb
    role: context
  - path: pages/traits/morphology/baeocyte_formation.html
    sha256: 90927945d0077a043aa3113e0cc71a773d8d171ec470a71016c0aed9f732376f
    role: context
  - path: pages/traits/morphology/black_pigmented.html
    sha256: 82e9a30ccbef4d2bc0ebb245abc6bbadc9fe77b88f3e1f8cd409cf6c463c4cd1
    role: context
  - path: pages/traits/morphology/branched_shaped.html
    sha256: a9a66d3c6320f1cb573d6e21eee0faa06c5969b761caf9a44841885fbd7ec74b
    role: context
  - path: pages/traits/morphology/brown_pigmented.html
    sha256: 0a10557bdefde16349b6d5f4db76b28a080087f406aa211c5b0629c0f412564a
    role: context
  - path: pages/traits/morphology/capsule.html
    sha256: 14f05d279ff961ca977912d0024b611f758a9d6c9ed636ef07ee00b1d054961e
    role: context
  - path: pages/traits/morphology/carboxysome.html
    sha256: cc2cc0affe58f38f7f7a67dbd6f9e3a825f7bcdb553d6b473a33b97cc41bd861
    role: context
  - path: pages/traits/morphology/carotenoid_pigmentation.html
    sha256: e96d425021dc72089445900138c01f37d721d8d6b89ec5e9d72471311c2523f7
    role: context
  - path: pages/traits/morphology/cell_length.html
    sha256: 2559a03390e7c121827da58fdd278987a82bef10f3a1ff1cb6e8fba9c34c4271
    role: context
  - path: pages/traits/morphology/cell_length_large.html
    sha256: 2510d16cd3e0d43953c68f4a2e827080a03f8392eb7f22ec2308d39d58a1538e
    role: context
  - path: pages/traits/morphology/cell_length_medium.html
    sha256: 162b8c912c4cfcbdcbfdfa97889480d447b6559f208ba48f28699d043dc225f5
    role: context
  - path: pages/traits/morphology/cell_length_small.html
    sha256: 651237340af55aa29a79509fbe76bd199ece171c90f2f6bd35765e752e023a01
    role: context
  - path: pages/traits/morphology/cell_length_very_small.html
    sha256: 488e438b9d856da0d2000e2db89e5fb80dacf8af30054bb66d6f78c6499014ae
    role: context
  - path: pages/traits/morphology/cell_shape.html
    sha256: 0203fb59db065fef56ce5e9b33786677cb0c11f6c237b3db9be88c4643ae447e
    role: context
  - path: pages/traits/morphology/cell_width.html
    sha256: eb48127ff273cb02d9522fdc4771d81df69065d1e1f2f5475e98edb32562d680
    role: context
  - path: pages/traits/morphology/cell_width_large.html
    sha256: fea9cdb86cf2683ec0fc3690b552ea98899a15e73131dc38923de9c27693169a
    role: context
  - path: pages/traits/morphology/cell_width_medium.html
    sha256: 2b1650117d5598646fe9f491a0170ccb86faeeda401649d0a2b29046782abf62
    role: context
  - path: pages/traits/morphology/cell_width_small.html
    sha256: 3ef2e9c13799e038e5af7316cf0a8a34d71c5be9209c75c2729859efe8e07654
    role: context
  - path: pages/traits/morphology/cell_width_very_small.html
    sha256: e523ba681b0eb85886604056fd2ca1f70fa6859d0f206656f61dc7967d82f4b7
    role: context
  - path: pages/traits/morphology/coccobacillus_shaped.html
    sha256: db58af9e7c532743c68c51a64f7a859b30c8a0acb717fba627e90ca9bbe2b84d
    role: context
  - path: pages/traits/morphology/coccus_shaped.html
    sha256: 08431a59f9f9f6a6c6bba82f10d3f6ae773154cb9406e9aae079a826df78b60a
    role: context
  - path: pages/traits/morphology/coenobium_formation.html
    sha256: e181c385cb89b7865c29fa589c9a47ac5b79bc25199f3141bc3791c091464654
    role: context
  - path: pages/traits/morphology/cream_pigmented.html
    sha256: c6944d871121c80164d2e1b859a1a016f4753c6477e1d75167e0d4e5aeac533e
    role: context
  - path: pages/traits/morphology/crescent_shaped.html
    sha256: 4c916c9dcedeb9ceaf3f760924cabf6fe2f4393cb0dc2eb0ab0ff630dcd8bf0a
    role: context
  - path: pages/traits/morphology/curved_shaped.html
    sha256: 9d4845ceaccbc623bd6a4fcb249dbeff3f8ded158b2019623e5b208b189c8943
    role: context
  - path: pages/traits/morphology/cyanobacterial_multiseriate_trichome_formation.html
    sha256: 5b3da6a5780b77a990ddf92c5ce3f2bcfafa470781cf9a9e16c570edec5f2bce
    role: context
  - path: pages/traits/morphology/cyanophycin_granule.html
    sha256: 6045d89725f1729135925878316d7762db66d8168555399c2f0edfe200617649
    role: context
  - path: pages/traits/morphology/diplococcus_shaped.html
    sha256: e7f2c4c66eeb43791ad56c9024fb0b69eafa1e1378d84ce14c2537b288fb41e3
    role: context
  - path: pages/traits/morphology/disc_shaped.html
    sha256: 9ac4564893a66cbdd56b1379637d528beb22ade931279038114d731106df498a
    role: context
  - path: pages/traits/morphology/dumbbell_shaped.html
    sha256: e28ebee203dcc875685014264e207051ec5b43cb8291b94efefb2827b6dd50e0
    role: context
  - path: pages/traits/morphology/ellipsoidal.html
    sha256: 917905850afa31ed6a5b3475a9677fdb47bc1b07815e9124ec24416b6a4381c0
    role: context
  - path: pages/traits/morphology/expansion_driven_sliding_motility.html
    sha256: 4b86a1f9c9a7536ac8c2a0ee32137c46d2d164a270a2572a655474b63510d6fc
    role: context
  - path: pages/traits/morphology/false_branching.html
    sha256: b0111657f2535d3c3a805ecedbb90e1a1cf51e0f2747e08baba67bc93de42532
    role: context
  - path: pages/traits/morphology/ferrosome.html
    sha256: b02f26670944ccc8ddf9a3f79e32e7ac8684a3d1787ee0b281acfc5c83c69fec
    role: context
  - path: pages/traits/morphology/filament_shaped.html
    sha256: 9ad02835b6e229d072660d3e4d4685e5738a3b06cca3f57955724a42b5f55f3f
    role: context
  - path: pages/traits/morphology/flagellar_arrangement.html
    sha256: 90c32b490310963af6deb7c4a96c3f18fada05624f6b97cae6c2a155d16fec1e
    role: context
  - path: pages/traits/morphology/flagellated.html
    sha256: a63c612ddd54c010cc58c940eddd180b2be242589009adbe0068d71df5e9a6af
    role: context
  - path: pages/traits/morphology/flask_shaped.html
    sha256: 4f130e6bb8d6790d7568f9d34114b537719f5e09c76893c01fd1d4217a140793
    role: context
  - path: pages/traits/morphology/fungal_adhesive_column_trap_formation.html
    sha256: 1ec6d4b0580fae914fcd77c2471855778a73e38965ca96ab583b1ea5d623e890
    role: context
  - path: pages/traits/morphology/fungal_adhesive_knob_trap_formation.html
    sha256: 64c888df773eb8ab79b17991230c4af26940c0a48acabe90c67c0b311667c94c
    role: context
  - path: pages/traits/morphology/fungal_adhesive_net_trap_formation.html
    sha256: 9b6f7baa8b277ee96f4ac33db17f45052e80169e83277f258149b6a154806407
    role: context
  - path: pages/traits/morphology/fungal_appressorium_formation.html
    sha256: 72757a44155e9161d3bcccdb28662285227b4b921692052300dbaa3b68e9e275
    role: context
  - path: pages/traits/morphology/fungal_arbuscule_formation.html
    sha256: 8ab8f7f7c77a1c1d84111e3e8c118fd28d80bff5e66a5967288dcfc8ec9326f4
    role: context
  - path: pages/traits/morphology/fungal_auxiliary_cell_formation.html
    sha256: 2095092a4a1ef6a8b6da2b70791698c8819083b7b0d7c03f4412b054cea7b5f8
    role: context
  - path: pages/traits/morphology/fungal_branched_absorbing_structure_formation.html
    sha256: 16b29c620dbd719d637b1df02a93a781dc54b8fea237ea3cca965942fe0f5947
    role: context
  - path: pages/traits/morphology/fungal_chlamydospore_formation.html
    sha256: 33bd8bcf3e67e6ff1ac500401eb8c733670ac5a20e955f044cd91b07bf905a9c
    role: context
  - path: pages/traits/morphology/fungal_conidiation.html
    sha256: f49899393e07f725cc5eb237dbdbd3c3b16d97805ac36d37a150a8dbda1c0aea
    role: context
  - path: pages/traits/morphology/fungal_constricting_ring_formation.html
    sha256: 0783e25e40f84209e76e69d812444df1c3761c2da48999c236ab06f7bddacff1
    role: context
  - path: pages/traits/morphology/fungal_hartig_net_formation.html
    sha256: 49b4e1654fa0f182a069a31fc8f1311bd58b9945e66bca40198c3150b3d4e93b
    role: context
  - path: pages/traits/morphology/fungal_internal_mycorrhizal_vesicle_formation.html
    sha256: c611bed73873ef5e41b2b8f18db3cb02f96f5ca08030155b53bfc808cbe5a9fc
    role: context
  - path: pages/traits/morphology/fungal_mycelial_cord_formation.html
    sha256: 73a7640407991b9547a1d435a583a63a6eef1793a127710d89840a7a409b5c67
    role: context
  - path: pages/traits/morphology/fungal_nematode_trap_formation.html
    sha256: 1474959b1661e9a09c12dc82a2db39aebf730bc07eb04b0f7103f86eb6b881a1
    role: context
  - path: pages/traits/morphology/fungal_nonconstricting_ring_trap_formation.html
    sha256: 3a8ca1a19f8236d8f3320f19c25017b1515091f5e21700abfb1fd52b24b53664
    role: context
  - path: pages/traits/morphology/fungal_peloton_formation.html
    sha256: c575b8f421d75c4a53ff39a08678b80fdcee264304ea7d9a6f744430432eefda
    role: context
  - path: pages/traits/morphology/fungal_rhizomorph_formation.html
    sha256: 19b006af15c534ea7bbed073e49d800d9f304b337c5483b861935d2d2172b386
    role: context
  - path: pages/traits/morphology/fungal_root_mantle_formation.html
    sha256: e73b19d685f667c16871395501598a390e22636a39455774ceb2e9cf5e0270c4
    role: context
  - path: pages/traits/morphology/fungal_sclerotium_formation.html
    sha256: e471ce30136e20ecbdabae2e15a135353dddbb6174221ebca68b0db0f51757e6
    role: context
  - path: pages/traits/morphology/fusiform_shaped.html
    sha256: 1961605e31f48fb5bb619fa156d0b79e545956140551abc409d17bc36d836cc3
    role: context
  - path: pages/traits/morphology/gas_vesicle.html
    sha256: 5e9c58961374afc2ad430ba0ffaae9f3ef80c8248d9aa706be492a11a835023d
    role: context
  - path: pages/traits/morphology/gliding.html
    sha256: a30166d65e59a271000b2d2882e27ba364463f6e66b91351c4067b351bfe0b46
    role: context
  - path: pages/traits/morphology/gram_negative.html
    sha256: e769ba033bdedcc6728c9d8806ebf2c591acf9b41224884af845bd0cba307aa7
    role: context
  - path: pages/traits/morphology/gram_positive.html
    sha256: cbbf4af1b0e3e52b6f28e1dcbfc24920033f25e1c92ecdcf0c90cbf110fe2bf1
    role: context
  - path: pages/traits/morphology/gram_stain.html
    sha256: 8fd00aeb1e906c502a7e51ced94fa1bad0afaf14d16e8ca0632aed11c1b0c63c
    role: context
  - path: pages/traits/morphology/gram_variable.html
    sha256: ac9b802421c60d538f98f0124bf220b92dbf802606f3286967aaa6507bd6a70e
    role: context
  - path: pages/traits/morphology/green_pigmented.html
    sha256: 6436534c370ae59026f387cce98325b6b8b74bd46b4e61071e7a509cfae53dcb
    role: context
  - path: pages/traits/morphology/helical_shaped.html
    sha256: 11158c5245b03bee4dae31fe17026683cc2fb47ca3a702850ab128dad9c0b194
    role: context
  - path: pages/traits/morphology/heterocyst.html
    sha256: a6ed6c3bf181567307e71bda43f72e91501e65f34edfcbbbdd4f71cbf91ea04c
    role: context
  - path: pages/traits/morphology/holdfast.html
    sha256: 2e54b32909154ac6ecb55c326542038fdc0f482ba7a67427e09b587c5531a67b
    role: context
  - path: pages/traits/morphology/hormogonium_formation.html
    sha256: efec0441c6653f9e29eab810799fe93923d93310627887930e30f24d4947f977
    role: context
  - path: pages/traits/morphology/intracellular_inclusion.html
    sha256: da7e3329d0981fc73ac4f6f756bb14f108376e9743d108fefb225c0c44f31d28
    role: context
  - path: pages/traits/morphology/irregular_shaped.html
    sha256: 2d5ca6cd12d2cedf1d1c9376a148de0605e683ea7ee9cb9520f5905fa12bbeda
    role: context
  - path: pages/traits/morphology/lateral_flagellation.html
    sha256: 09b48ec23e3b301c24a2b600a3cef3df08678b10281e3f2b1e47f740aa45d27d
    role: context
  - path: pages/traits/morphology/lophotrichous.html
    sha256: c3769dbb12db16a737f9421c21eda2c2abcf42ef87c8a68bdd18ac162d2a7930
    role: context
  - path: pages/traits/morphology/magnetosome.html
    sha256: fe1453585b63f36dc0470a05207d2606c002f5692996014571d753d5a900dae2
    role: context
  - path: pages/traits/morphology/microbial_haustorium_formation.html
    sha256: 6a81436eb3aaffab8febb5781e41fc9645328e25501e887c636f1da7f043e246
    role: context
  - path: pages/traits/morphology/monotrichous.html
    sha256: 1c74232913ba5a59ea38d8f46272030734734ea735be0ace07996279b781d98f
    role: context
  - path: pages/traits/morphology/motile.html
    sha256: 08e61009b3f7206319e31ddde4a1645c1223a7529b76df236924fb864c7c32d1
    role: context
  - path: pages/traits/morphology/motility.html
    sha256: 4b36b7cbfa8c3546d08a5711e05968b6a315d8804ed9fa1950fbe0eb71cce7a2
    role: context
  - path: pages/traits/morphology/mycelial_growth.html
    sha256: 8b6712397b553d107afd7b55d265ab92e03784a6c5577bf2a182349e41a2e802
    role: context
  - path: pages/traits/morphology/necridium_formation.html
    sha256: 7258e2a4873a03fd695fe3040386ffd660c3b9b26a412f8549f7617ceb30d231
    role: context
  - path: pages/traits/morphology/non_motile.html
    sha256: 5c487078dbff2c2761cab25401757f53e65427301597ab79eabb196c35fe8dc7
    role: context
  - path: pages/traits/morphology/non_spore_forming.html
    sha256: ad1de6de1a7158fff2a7216c49df4dedffe3a0470f05fc32112dcb234461a5a7
    role: context
  - path: pages/traits/morphology/orange_pigmented.html
    sha256: c14f9e4d249da156b65d46d9366e6c43aea3a63f738385a04eff5d1e29e08dab
    role: context
  - path: pages/traits/morphology/oval_shaped.html
    sha256: bdd0a5be7f673d9af1bf0f7b99b6cf791dc91294e7d18e765dfd686cc71dfe23
    role: context
  - path: pages/traits/morphology/ovoid_shaped.html
    sha256: 43ee297adfcace18969c5bf11eda1c218a457a780550e4dc5ef1e74724424c14
    role: context
  - path: pages/traits/morphology/palmelloid_formation.html
    sha256: fb081b3d0cddfa7a9c7997d09a20ab266b033f7610f1e72639c94f0cb1310dd3
    role: context
  - path: pages/traits/morphology/peritrichous.html
    sha256: 2cf79d24ac58c0884ef834634bd2b094e04fa4ed11bb3384e8e35ecf171aa2a9
    role: context
  - path: pages/traits/morphology/pigmentation.html
    sha256: fae3e7384fea43b781b1612da1ab90dab895b853a72203b03bd12db4e82627c9
    role: context
  - path: pages/traits/morphology/pink_pigmented.html
    sha256: e343894a46728f53069eca902872d84605fd427d8c02a6b4e1bf6ed6fe8ce25c
    role: context
  - path: pages/traits/morphology/pleomorphic_shaped.html
    sha256: 8f720e763ad531bf3fd68ca177e9e948bd4fd9a22a076c7ce9b899f519732fbb
    role: context
  - path: pages/traits/morphology/polar_flagellation.html
    sha256: 50d728e7553338701c4ce000c069fc498d0066b12cb5504310a7ff1f07f63fb8
    role: context
  - path: pages/traits/morphology/polyhydroxyalkanoate_granule.html
    sha256: c5b9e3eac0409964ebade8a185bbd17670414cb191d0e0e56365d2bd9d5b7650
    role: context
  - path: pages/traits/morphology/polyphosphate_granule.html
    sha256: 51cddb31733ac9c6e83935e87bb1d48777343c3b08d49be99a6ddc9696402286
    role: context
  - path: pages/traits/morphology/polytrichous_flagellation.html
    sha256: b71e8ab987c13e4f8e9138a44f3a60f37cd7f05eafdb3b3a40e4e1c92d85f4e1
    role: context
  - path: pages/traits/morphology/prosthecate.html
    sha256: 92c75437b2516546fa0b0507c01e8ede36f645a15dda3706dfed87eec7d6ca98
    role: context
  - path: pages/traits/morphology/pseudohyphal_growth.html
    sha256: 679977660bc5a760ffae4645caf91e9061dc0629124198566ff3d5be3b2879f9
    role: context
  - path: pages/traits/morphology/red_pigmented.html
    sha256: 1d9b62810517ca24e939bc556b6ba4e8198713edeaceeaf858edeb0784954a53
    role: context
  - path: pages/traits/morphology/ring_shaped.html
    sha256: 05c4964766ea10727e9f3320a30c8c1c44f6f80ac0bfa9bbb84acd9e452c2664
    role: context
  - path: pages/traits/morphology/rod_shaped.html
    sha256: 646c109a285716afd790817cc3572a243d07eb93d54cf93f4c1362fbcce182d1
    role: context
  - path: pages/traits/morphology/rosette_cell_arrangement.html
    sha256: 595461cd701e8e584762903e5dc9b35e0668f00db9fa34e229482e798f718476
    role: context
  - path: pages/traits/morphology/s_layer.html
    sha256: a432800a945c9c45036fe4d677df1792e047434f308ebcf7d106d68238adee43
    role: context
  - path: pages/traits/morphology/sarcina_arrangement.html
    sha256: bbc247159b8aace07bee5a078e77c03ebf569e7157ace1f08f32804d0fe914ad
    role: context
  - path: pages/traits/morphology/sphere_shaped.html
    sha256: 3f3e09e17c384d1d32f304109e099fb662645c3340853379485b523521016648
    role: context
  - path: pages/traits/morphology/spindle_shaped.html
    sha256: 7e46e0bc9c007a854c5acf87b0b46d2cd572ab77be9ca065b47a15b3ca3918ea
    role: context
  - path: pages/traits/morphology/spiral_shaped.html
    sha256: 6ee73f9941346ea7430bdb55c88a2f4a85e7795c8d26d0315c3eebfede55aea4
    role: context
  - path: pages/traits/morphology/spirochete_shaped.html
    sha256: ce796bc48f35aed51b211106726b5dc7f69f667ef780bd2e73e160156cafa64e
    role: context
  - path: pages/traits/morphology/spore_forming.html
    sha256: a1c5ecfc7b6529809b4eec6e5ff60d3e8a9a9a187aed02e88891126815249669
    role: context
  - path: pages/traits/morphology/spore_shaped.html
    sha256: fac5bc1645482b913a00a7462290c5e76586b0e5b67a9b440787b229f0aa3447
    role: context
  - path: pages/traits/morphology/sporulation.html
    sha256: 8e56b6f8d2cc534b77b48ab2626b8c647a08b8fa60ed6f5d57500e8c2731b4a5
    role: context
  - path: pages/traits/morphology/square_shaped.html
    sha256: 056743a04f182e13a99772f444467edf8d1693bdb3054a78f7356d724815656c
    role: context
  - path: pages/traits/morphology/staphylococcus_arrangement.html
    sha256: add4e75bd1b9c9c988a7ee3f65248e24c5daad61ce4c52e3dc65453ec4620e4c
    role: context
  - path: pages/traits/morphology/star_shaped.html
    sha256: 2f84b2d488e35b030cad3b8b9c3857bc65651476364eb8b840fe94f367e211f0
    role: context
  - path: pages/traits/morphology/streptococcus_arrangement.html
    sha256: f85dcd38c9bd08724e1f1e68fdbb558b7de393f6ec4cbfddf9424d4fb8bd2072
    role: context
  - path: pages/traits/morphology/subpolar_flagellation.html
    sha256: d3294a3a962f8318bddc41f57989ffc305a9cebd2d3c2f5c0cb27aecbbb18b72
    role: context
  - path: pages/traits/morphology/sulfur_globule.html
    sha256: f7807e196bd8c6d87bfd43dcbf348063b45aab2580eb1ac2295a922b5a163a40
    role: context
  - path: pages/traits/morphology/swarming_motility.html
    sha256: 09db363f54240999d2aee43852d9a407d5a3ec3daa05f4c1c5d2c77aeb0a403b
    role: context
  - path: pages/traits/morphology/swimming_motility.html
    sha256: 7a8e4fc6d8713962576a8c1e73db21c56bfca85aa715817c0c47eb2db4e8effd
    role: context
  - path: pages/traits/morphology/synnema_formation.html
    sha256: 9c97b4b07b8784d586c262b894bd73a2e35e754c27a7b088cb6ad420b424fdc3
    role: context
  - path: pages/traits/morphology/tailed_shaped.html
    sha256: ce1322336ec4dfd3e96b54653e03bdf0acd34f1d2c1235d41b80634b2cde7d21
    role: context
  - path: pages/traits/morphology/tetrad_arrangement.html
    sha256: 311f32eadfb29bfed8e348e5d11a6887c6650b5029c19d3367774c64d2dd3caa
    role: context
  - path: pages/traits/morphology/triangular_shaped.html
    sha256: 8938b61523ef21ed83a3e938d7d89a00e7a11d58f4bdf4b0726588db957b5b9e
    role: context
  - path: pages/traits/morphology/twitching_motility.html
    sha256: 4c6430e6bdd5e93bd1731ba71c2ce4359b268a8e16cbb36c0045bcbf99e5241f
    role: context
  - path: pages/traits/morphology/type_iv_pilus.html
    sha256: f88735d9732145cf4bd5833e6888597d60eba65a2f01867a24abaa846df009aa
    role: context
  - path: pages/traits/morphology/vibrio_shaped.html
    sha256: 1bd5442e6141b57161f545c3f5b0101dc7dafa9a6cbc91e6b5e3bd330375752f
    role: context
  - path: pages/traits/morphology/white_pigmented.html
    sha256: 0caa16735e52abec52df804cfd6cefd6f40dc2d668a0b956a21058130e79b718
    role: context
  - path: pages/traits/morphology/yellow_pigmented.html
    sha256: 4451422294d3c1dd4ce2b33d81276224029fec16149da354eb43204440372c01
    role: context
  - path: pages/traits/observation/growth_nacl_observation.html
    sha256: 8d64423995ad56abf7c07b71bf20583ec106fcd5a01de388355e865a29f7ce3e
    role: context
  - path: pages/traits/observation/growth_oxygen_observation.html
    sha256: 375fce0859da50f68cf156b2b18df1bb426b632ebe566739768931f19fc65dcf
    role: context
  - path: pages/traits/observation/growth_ph_observation.html
    sha256: 48c6e31ba6ffae9df4b5af9ea0d5063d5b3139d458914be5f8340c17bca18b92
    role: context
  - path: pages/traits/observation/growth_temperature_observation.html
    sha256: 2f1166acb434126fc2b2451fb6e1ded37eae9e7a8b0faec01c91924dadcb69b0
    role: context
  - path: pages/traits/observation/nacl_delta_observation.html
    sha256: e0b9ce932cffe827718a86ff2ddf5f2c0cd1ed5c7e9a1812b9246978f7dc7eb9
    role: context
  - path: pages/traits/observation/nacl_observation.html
    sha256: e15f681f88b97ce045ae3c43c73519ba639215447397e6698b339bfd1ec64007
    role: context
  - path: pages/traits/observation/nacl_range_observation.html
    sha256: c072c4a32ea586afd39eb4f1d00c320ae51c689bac4cdbc26881e4246e92b3c9
    role: context
  - path: pages/traits/observation/optimum_nacl_observation.html
    sha256: 96668ade295890cc841f73fca75dd944f798f508c435ab7def0e822ca198c9f9
    role: context
  - path: pages/traits/observation/optimum_oxygen_observation.html
    sha256: 1861732e2d6af9dbdc861f0dc43f75df2a25ee9a21357ba467ab78c27f252755
    role: context
  - path: pages/traits/observation/optimum_ph_observation.html
    sha256: b292438425476f711965ae24f948ef4551f4ba6057b29611814b401d0a7b8a30
    role: context
  - path: pages/traits/observation/optimum_temperature_observation.html
    sha256: e01b7c06299d02cca553184811dbcc92f929367a59b948ed1d12ef19da2f9ada
    role: context
  - path: pages/traits/observation/oxygen_delta_observation.html
    sha256: 75a847f4570cfbaa4366ddc922eb026dd35e43a5e1ff4bda88d33bfabd89b8e9
    role: context
  - path: pages/traits/observation/oxygen_observation.html
    sha256: e6485f6c4026df4033cb4fc4eee828bcef5251478199efa90a7e4b565158d41b
    role: context
  - path: pages/traits/observation/oxygen_range_observation.html
    sha256: ec2d08a5d9af20b667f021fb2643abae729351e74aa641d224dea76512ad6d24
    role: context
  - path: pages/traits/observation/ph_delta_observation.html
    sha256: 77de47ec181e5e618e4792d33a29a1eb06e4c29d85b8fb703655f30168423ca4
    role: context
  - path: pages/traits/observation/ph_observation.html
    sha256: af28055b7ec9bb75f85009771438d9dde29f284e97e389736e51096054334a72
    role: context
  - path: pages/traits/observation/ph_range_observation.html
    sha256: dc156165f2f43bbd8bb1261ca71302868358b14fa788aec1bc694418f7d32f0b
    role: context
  - path: pages/traits/observation/temperature_delta_observation.html
    sha256: 539482e527a566e92d9e417defa764535ecc03709cec69a352b8af1cb3ce3702
    role: context
  - path: pages/traits/observation/temperature_observation.html
    sha256: 9fc1698e04c0df44af2cf7b81ac0c7658eccd7d237bc6665ae5739c2004cb4a0
    role: context
  - path: pages/traits/observation/temperature_range_observation.html
    sha256: f25126b49dedda87af3a4ee9388b61aa320f101556cdf605a35862c42e72b486
    role: context
  - path: pages/traits/other/catalase_negative.html
    sha256: 6d0e27954b1a3781b4c56d31a4d902b6180d779592a32b024a3b1c1fd947ddde
    role: context
  - path: pages/traits/other/catalase_test.html
    sha256: d54b735b55a6a9ff77404862ab2fbb8fba70fc110267380234f1fe38c59831fa
    role: context
  - path: pages/traits/other/circular_colony.html
    sha256: ee43c044af23d7a12356555fce9cd3b048d629a247745278a18072cd81208157
    role: context
  - path: pages/traits/other/coagulase_negative.html
    sha256: dbac8f2e43ba427178718ab003db4c858a4c174c3c900710eee56764534c935c
    role: context
  - path: pages/traits/other/coagulase_positive.html
    sha256: eac624d864f8ce38fe391acd6899fe41943e67bbbdaf26b8bbf031c29e2a4f31
    role: context
  - path: pages/traits/other/colony_morphology.html
    sha256: a14531d5c607ac6fa31191df1e3c1846ee06c4968485e0981031c936704f1087
    role: context
  - path: pages/traits/other/colony_shape.html
    sha256: 35907bab3a43cf155e80e77aeef50db94208290be0b49b7d0eca82f0466433ff
    role: context
  - path: pages/traits/other/epibiont_phenotype.html
    sha256: d21abd63e3b72967953c581ba7886bb60f9a7fadde60a556abd9ae54f761ffe0
    role: context
  - path: pages/traits/other/filamentous_colony.html
    sha256: dfbaf41ca93b0e0906297e1b3de69062ac1b5a971038274fd3a52caa9d769593
    role: context
  - path: pages/traits/other/fried_egg_shaped_colony.html
    sha256: 26a6186d5e8893111189d811ba41ac28dfbbdf2b6682b30c3518e0eeb3e64a26
    role: context
  - path: pages/traits/other/generalist.html
    sha256: dea4c2ef562694ecb2634af609c572555568a3d6b296b5cdc33af776b99c26c8
    role: context
  - path: pages/traits/other/hemolysis.html
    sha256: 793d710f9c6f7cee70295fb16c146984b2cce3f4a09158b3dd274ff3f8bb5e87
    role: context
  - path: pages/traits/other/hemolytic.html
    sha256: 2972be31b21889e590ca56e1463b43465f36486a635cae1e802a4c1b3b036e75
    role: context
  - path: pages/traits/other/indole_test.html
    sha256: de416ab9f4493615a297f3c47f4af24ca9dc7663900808b996d6dc64392dff0d
    role: context
  - path: pages/traits/other/indole_test_negative.html
    sha256: 791810e68957b75cd67f53c5f509f6bfef1995816230ec86f353b258194eb275
    role: context
  - path: pages/traits/other/indole_test_positive.html
    sha256: f56d91d70ddbf33aa11774713734a50fbf248c7ca84dc413d7330190fc5cb2bd
    role: context
  - path: pages/traits/other/irregular_colony.html
    sha256: 5c3143eae9031e90d753c625eacf2d264d3a238460745eabb137840b3a86cf52
    role: context
  - path: pages/traits/other/methyl_red_test.html
    sha256: 3c65cbacf994c2a5ac237f5b3ff92876623b45bb878c60b77412b255c19adcb5
    role: context
  - path: pages/traits/other/methyl_red_test_negative.html
    sha256: 6bd11f594aadbcaba7d88523369416456905904216d428ecb231a4f9ec931d2e
    role: context
  - path: pages/traits/other/methyl_red_test_positive.html
    sha256: f9bf503b5b95a0ce9e09e2fafde2989eb5ed5aa9202656096012007fa613ff6a
    role: context
  - path: pages/traits/other/non_hemolytic.html
    sha256: ddd6a3fb34bf85b796e2bbdbccb426bf308a22f4a8f2f6e9f023deb9f08822cc
    role: context
  - path: pages/traits/other/osmotic_tolerance.html
    sha256: 31bab046fa6c5d90e12de0b03162b3071046b059627c95a78f89300279862851
    role: context
  - path: pages/traits/other/oxidase_negative.html
    sha256: 547c603fa966748497deebb66ceb3eb155e438bfbc9205325ceb5118de415062
    role: context
  - path: pages/traits/other/oxidase_test.html
    sha256: c68806dc50171f435a703337134007128d5e95c5523956778c42388595c057a4
    role: context
  - path: pages/traits/other/punctiform_colony.html
    sha256: c838c45a8e38a29e653bc346aa107e51db0feb907a42883bd95a7a71f92e4fd2
    role: context
  - path: pages/traits/other/rhizoid_colony.html
    sha256: 4b439d1b2d621ce4d74eff5a8b428db0fdf057174197010ca207a78af8d23e14
    role: context
  - path: pages/traits/other/specialist.html
    sha256: 33d8562ed5bccf5b25ce14a03608409b5c73f96c2cadc6e3228c1cb8d06e4e8f
    role: context
  - path: pages/traits/other/urease_negative.html
    sha256: 6f36be2398f76d74b8fe8e2cba49c29e45d21a006a0cf5d8fec5e5bee5f22f8b
    role: context
  - path: pages/traits/other/urease_test.html
    sha256: 679b066a7206cdffc65978b6a97ee0475bad7791c72d271e07fbb8fa58d8235a
    role: context
  - path: pages/traits/other/voges_proskauer_test.html
    sha256: 1622acc6022b064e361240330621d27aa09a3be9d3fc43220925e598b2fbf5d7
    role: context
  - path: pages/traits/other/voges_proskauer_test_negative.html
    sha256: f40a9489012615ef888cee2029c2e4d70a7f4b5900bcc1b12406a1bf6ed9edaf
    role: context
  - path: pages/traits/other/voges_proskauer_test_positive.html
    sha256: 5b7fea284356aada2624294edb67a0f2bc0f65cbc2e009b55e867ab826846afb
    role: context
  - path: pages/traits/physiology/acid_phosphatase_activity.html
    sha256: 1725e78a19e87dd473dd90c004f3b346c2d787fd152aefe70edaac1171a6eb91
    role: context
  - path: pages/traits/physiology/acquired_stress_resistance_memory.html
    sha256: 730278b2be1fe929999a6e9db886d86dea05f9ae8fbfcb0b2b44d57b445e6603
    role: context
  - path: pages/traits/physiology/aerobic_anoxygenic_phototrophy.html
    sha256: 01399d1a71c034c92682b39682ff4cc8e9b98752e1505e872b91645ed0a23c43
    role: context
  - path: pages/traits/physiology/aerobic_overflow_metabolism.html
    sha256: 8d05408f767408d7c0e75f3d53b50a69e25c9a74922ae6f60d8955a81625cd7c
    role: context
  - path: pages/traits/physiology/aerotaxis.html
    sha256: f13a997327597643739efce011e9e3222abb6033bcf8379ac122e8b95bdf78ee
    role: context
  - path: pages/traits/physiology/aerotropism.html
    sha256: f36c3b7de5f54f4d8513b17f0502564d342ef33d59ad4e2b82437a3450ed73a1
    role: context
  - path: pages/traits/physiology/aggrephagy.html
    sha256: a2058f2df8e146f5ac0f80c692e6e3120859e082088abd793c1f6b2c11ffe279
    role: context
  - path: pages/traits/physiology/alanine_arylamidase_activity.html
    sha256: e9d59ea52e555d6d3e62c99a479907635c3669ec5e13a41dd77a6c5eae1b1c6f
    role: context
  - path: pages/traits/physiology/alkaline_phosphatase_activity.html
    sha256: 794100174aaa193e228893ed68ad596321183140c63635c60a1a10d8ef3eb38a
    role: context
  - path: pages/traits/physiology/alpha_chymotrypsin_activity.html
    sha256: ea2dafcb3d37582292f3b6d16a715d1569b781ca66f9dd9171bd4b17cbf24bea
    role: context
  - path: pages/traits/physiology/alpha_fucosidase_activity.html
    sha256: 8a852ec456d5b696fdd3da63f83fd28c20069aab6a6ae4f68b6b7704bc913518
    role: context
  - path: pages/traits/physiology/alpha_galactosidase_activity.html
    sha256: 443787936613c8deb434b17d7e5ba9e15ffffad9a6218c683b80e5fff84cdb72
    role: context
  - path: pages/traits/physiology/alpha_glucosidase_activity.html
    sha256: b3118d969ccaa856c652e3dd37d4a3b7568e1ea8e3183f3d5205901abae04ad2
    role: context
  - path: pages/traits/physiology/alpha_mannosidase_activity.html
    sha256: fa93ccfe6020f91befb39f73aa6834c2f99346d9aced653d1369100a28f2477f
    role: context
  - path: pages/traits/physiology/amylase_activity.html
    sha256: addd7d7e57595012ab60aa9c5a02b575c1aac6a1d9d79ea8c0780cad2e22899f
    role: context
  - path: pages/traits/physiology/anisogamy.html
    sha256: b0d2667b840e5b95491599cea58b1a3c300e4f83002fa87c38709c2129339e26
    role: context
  - path: pages/traits/physiology/antibiotic_resistance.html
    sha256: 2b9c4919473e1f5219b9ac4a0ffad6d2f0852f1a9a249ec4c932552463b848ff
    role: context
  - path: pages/traits/physiology/arginine_arylamidase_activity.html
    sha256: e33f61ada5d9954700eab52790432a4e43c0947f01d70d297a61bc7ca8b05582
    role: context
  - path: pages/traits/physiology/arginine_dihydrolase_activity.html
    sha256: a8edd10cdac57423a349aa0008ac446fe715229579f3a9d8184d81322ff85f85
    role: context
  - path: pages/traits/physiology/autogamy.html
    sha256: e02d9d38aa825092dadad261a19c3fd1705a91342f5e8150be4b3db8d2175e63
    role: context
  - path: pages/traits/physiology/automixis.html
    sha256: b0c807d6fc5e838a5ee488d55f4f3fa191386bbc8d3738c6ae14868cafe253ee
    role: context
  - path: pages/traits/physiology/autophagic_glycogen_degradation.html
    sha256: 804aee6f370b7a4b7b14e491e8cbd10fc5dabe00b889de089adca2b1707711f5
    role: context
  - path: pages/traits/physiology/autophagy.html
    sha256: ec71fc87fe41d5dd88001273ada382397d363a418980e6db8300540af9bc7ac5
    role: context
  - path: pages/traits/physiology/autotrophic.html
    sha256: c6425ad5c639643d861e97365e78ebf69750ec6c6c68c03838769eea699405bd
    role: context
  - path: pages/traits/physiology/bacteriocin_production.html
    sha256: 73f5bee9c4a0eb2a1354f792eb3b1f85e297b5f17d8d509aef88d3a13bcabac6
    role: context
  - path: pages/traits/physiology/ballistospore_discharge.html
    sha256: 97773161eef266e04aef390e587bd7cdcdb53749bcc141d8b8926513398a4c19
    role: context
  - path: pages/traits/physiology/behavioral_habituation.html
    sha256: dcfe21a89c9f7619351a512366d2b153abadb1b6e23f6c3fb601b07dc6916c82
    role: context
  - path: pages/traits/physiology/beta_galactosidase_activity.html
    sha256: cf4963f0d5303a70afa9eb7b82362aa0bf35b27552991439ed6fe861f71bfe06
    role: context
  - path: pages/traits/physiology/beta_glucosidase_activity.html
    sha256: 10143ac910b1eae83c0e5c4abab8c7bd45e9eff1198dc82c6f0b578f77d729f3
    role: context
  - path: pages/traits/physiology/beta_glucuronidase_activity.html
    sha256: 68f2728b968e32485e1ff282775fb85787a0477d9952b15fcf26fb389a07bdbe
    role: context
  - path: pages/traits/physiology/beta_n_acetylhexosaminidase_activity.html
    sha256: 5bb6fbfdc54e4c134adaf1422bd857c7afeaddf9baf669dfcd50673c418f19c0
    role: context
  - path: pages/traits/physiology/bioluminescence.html
    sha256: 7a50fa312ff0fb2d7a345edaed73a00a42f7c27e21add4353336aed61e316463
    role: context
  - path: pages/traits/physiology/biomineralization.html
    sha256: d91f8ec5b85819359d9419b17fd6e6a532add81cdb3eb66f8ab4200d2070db5e
    role: context
  - path: pages/traits/physiology/bipolar_mating_system.html
    sha256: ac587cc19d98a5149f13e567d09905ab7d0e698c0878ba1f9c50260da385921c
    role: context
  - path: pages/traits/physiology/carbon_source_memory.html
    sha256: c693361b636135ce02c211713d5708f9729fe425a2ce89fad23686f17544b154
    role: context
  - path: pages/traits/physiology/carboxydotrophic.html
    sha256: 6476e401faee30918a0620db0a6d052358a3777cf9b5445eca7146ac043fe6aa
    role: context
  - path: pages/traits/physiology/carboxylesterase_activity.html
    sha256: 29267c3f46845ad0b508e89fa62209afdd557b8cc841093c2d0b64ea7b3f568e
    role: context
  - path: pages/traits/physiology/caseinase_activity.html
    sha256: 17172ea35379a4970686fbbf87b2140e170a7ed64ef636b20747b2e62d1c75d6
    role: context
  - path: pages/traits/physiology/catalase_activity.html
    sha256: f21988e789a401728e48376561a810c971e13ebb2c833780142e6d6e3fb099b7
    role: context
  - path: pages/traits/physiology/cellular_buoyancy.html
    sha256: 4345a95d7456d1f9be862b23f45cf31161a894a52e62e6385ab255f971223d68
    role: context
  - path: pages/traits/physiology/cellular_rejuvenation.html
    sha256: da3a427e86342eb453df8150a18e2102af5602730b117f83925c6a900b212e4d
    role: context
  - path: pages/traits/physiology/chemoautolithotrophic.html
    sha256: 686d200c8e3d7d6503d2799a4ffdc8958860e157678978be611389bd1ad5e4d9
    role: context
  - path: pages/traits/physiology/chemoautotrophic.html
    sha256: 4b39f1810275086d3336ada37ec44bf3e168f9593dc37321df56389da317ad43
    role: context
  - path: pages/traits/physiology/chemoheterotrophic.html
    sha256: 8b193dcefa72cd75465442a12c61ff686b34a3c976ac41c951d23eb04a02913d
    role: context
  - path: pages/traits/physiology/chemokinesis.html
    sha256: 0869899fd10ccce96843d401d51abfb1cc8db67e6eac08682901eabb6622d70f
    role: context
  - path: pages/traits/physiology/chemolithoautotrophic.html
    sha256: 657634ac86e3b467fca9df8b00b0f17c56f9fb7d3a4aee6ea39c385d2b2dfe9a
    role: context
  - path: pages/traits/physiology/chemolithoheterotrophic.html
    sha256: 01f3be9b12e19085276195a0feaa75850e8c8496815e621f921461eac8268361
    role: context
  - path: pages/traits/physiology/chemolithotrophic.html
    sha256: 13b10d95f467f3dad87e89b6bb84e487504c4df49c3c212c189f3738f37408cc
    role: context
  - path: pages/traits/physiology/chemoorganoheterotrophic.html
    sha256: b114903516624decab8acc9100663f4cca543b07e1e6a88095b74bf587a03d9f
    role: context
  - path: pages/traits/physiology/chemoorganotrophic.html
    sha256: 6b7cb380a01f432ffea53de1a76eaea9ce228aeccd69ceb9f1984674bb45242d
    role: context
  - path: pages/traits/physiology/chemotaxis.html
    sha256: 71202f0b786f257ae39eebb62921b2098966f8643e85e6bd4e8dd4627e681be4
    role: context
  - path: pages/traits/physiology/chemotrophic.html
    sha256: 152a827a23dc02fd42dd70c003b0d36d3cbe2f7a0e990b158d06b527e5255917
    role: context
  - path: pages/traits/physiology/chemotropism.html
    sha256: 4e37fa00e4f96d9eae4997603c30a98dadbb09b904d3c6e2d430a818f12e3a58
    role: context
  - path: pages/traits/physiology/coagulase_activity.html
    sha256: 68ae34bd6413f56dfac31b2e6059b0ef657c605414e67e59d5d8a4fc113ed727
    role: context
  - path: pages/traits/physiology/coccolith_production.html
    sha256: e176422629269c01ef851e3d172ba994b46e9c8c85c3d0f8c960f3ece264047b
    role: context
  - path: pages/traits/physiology/cold_shock_response.html
    sha256: 7f83d78a500c37f0e4214189b5754491573cc3143a0eb3c193949e5a459b02a2
    role: context
  - path: pages/traits/physiology/contact_dependent_outer_membrane_exchange.html
    sha256: 932e0601357828db0e54f35e619f809d52bdadc3cfcce35fde39ec8ad3c586b4
    role: context
  - path: pages/traits/physiology/copiotrophic.html
    sha256: b50616cd606fcbfac21d3b9144ff97f74440de25b3a9a4687452fbdd12d3fe31
    role: context
  - path: pages/traits/physiology/cue_triggered_environmental_anticipation.html
    sha256: 126798696e74642f81f41f001cc043dc9978c74e07f9dc346d335c2b46ff2c53
    role: context
  - path: pages/traits/physiology/cystine_arylamidase_activity.html
    sha256: 5389f3526a8f581b794e4aa6f59e6524cc5fb7d3f79a9dc559ad98a1da571580
    role: context
  - path: pages/traits/physiology/cytogamy.html
    sha256: 042e91d0ca5a0074d80756a475095b40adf727b3bf8bb686d3c0d76a9e784c4c
    role: context
  - path: pages/traits/physiology/diatom_frustule_production.html
    sha256: 57de5f373fd2a979d29699c6395bf9600ea5b0e7edeeee62e2abeb63dda366fa
    role: context
  - path: pages/traits/physiology/diatom_perizonium_production.html
    sha256: 493d5d5e43f30101c3656745967a6609cf0e18be50b7681bbf5583ad900ecb4d
    role: context
  - path: pages/traits/physiology/diatom_seta_production.html
    sha256: 48e7198d7ca87a31df0d4f6c2413b9862d17d807342fad15a090f95a4094ba64
    role: context
  - path: pages/traits/physiology/diauxic_growth.html
    sha256: 8946af1361310d9cdf3e42961919ffd3e14bae45a90780b5322ef19685676565
    role: context
  - path: pages/traits/physiology/diversifying_bet_hedging.html
    sha256: 4448337f92ead93d82c9ec38571f4c5bcd0d5fabc7083680805092d04566b533
    role: context
  - path: pages/traits/physiology/dnase_activity.html
    sha256: 7b51e3f37f895e95de3cacda9ca3f9e829f46a48de46c67162cffd22261f8cfd
    role: context
  - path: pages/traits/physiology/dormancy.html
    sha256: 42733688a75486b7c31223714f34e845a031ed8e0e693ffc8df68959063754a8
    role: context
  - path: pages/traits/physiology/durotaxis.html
    sha256: 08bd79cec77d236b1348938313e0fd1e2d7acb768b6ceb49061493c12a8dda0b
    role: context
  - path: pages/traits/physiology/endocytosis.html
    sha256: 0d08e3586c5aee2a9b45c3a2466e18bf9f8cdeee9cec18a5fb46aff066756329
    role: context
  - path: pages/traits/physiology/energy_taxis.html
    sha256: 7e5a39057c1d5c615d5f2fdbe0aa7b878584d83761d6c59e2ba7caed2d151d04
    role: context
  - path: pages/traits/physiology/enhanced_transcriptional_reactivation_memory.html
    sha256: b1f38fcf977dc580538d4ad1ca56f3bfcc304b1d16f4761da3ef18c12f076f79
    role: context
  - path: pages/traits/physiology/er_phagy.html
    sha256: 9ac3e811de0d91d4509e00bb0b3c7247152c48dbec0698f305074692a748e2ff
    role: context
  - path: pages/traits/physiology/exocytosis.html
    sha256: fbff3d2cd74008a75e9aeceec9ebe61d951de1f886af2ed5bb9b3ef33be61c2c
    role: context
  - path: pages/traits/physiology/extracellular_membrane_vesicle_production.html
    sha256: 50995393c5b87a1c878cec7b79752b9922d8399dee58c10470ff5c21166f148b
    role: context
  - path: pages/traits/physiology/extracellular_trail_based_spatial_memory.html
    sha256: e0fb7a67cd8bb63494b588958166a211dc97792052e812bf9a021f012e359335
    role: context
  - path: pages/traits/physiology/galvanotaxis.html
    sha256: 0b702b182979316d17237d14ad200c6df57e7583e59e8e4a61e61adad34f2d32
    role: context
  - path: pages/traits/physiology/galvanotropism.html
    sha256: 6affe9ae32baca6b1e3c09abe989c05a84ef5ae9edc81ef6467b7a5e00402c09
    role: context
  - path: pages/traits/physiology/gamma_glutamyltransferase_activity.html
    sha256: 07b0a404350b5a576169b4630cb1a6de4cd9aecf57efd9e90bffadf6923bdf82
    role: context
  - path: pages/traits/physiology/gelatinase_activity.html
    sha256: 4737adcb7fa14aef603734b85bc8bdb7fb7bca273112893ca9447bf9a18d6566
    role: context
  - path: pages/traits/physiology/glutamyl_glutamic_acid_arylamidase_activity.html
    sha256: b5ef22a402775d8e1699d24a99a16ed1c66b93e74e210a3d8e6ee3389a46e73e
    role: context
  - path: pages/traits/physiology/glycine_arylamidase_activity.html
    sha256: c2377843217d8c44d181da1f650064ab4c17770bc8bb30805721a3d28924107d
    role: context
  - path: pages/traits/physiology/gravikinesis.html
    sha256: 833e1763050a8904a7cafb4240a982eaeac50204440d48b6bc72a6bdeff65df9
    role: context
  - path: pages/traits/physiology/gravitaxis.html
    sha256: cc1b0237b9f0088905596fdf8ca04f4edda7fed945ea5745be6f640279afa2ef
    role: context
  - path: pages/traits/physiology/gravitropism.html
    sha256: 6a09997548ac5fabf6102c229175eb69851c6bb939dc18c5279591a3acd26b95
    role: context
  - path: pages/traits/physiology/gyrotaxis.html
    sha256: 5e1b474da5984f452b07ef46a731aea80da0dd404ffce523eec5c32ce81ed721
    role: context
  - path: pages/traits/physiology/haptocyst_discharge.html
    sha256: 77ce02f76592705b1857c007be9ca2401063e31ce8c7dbd31b6263c1b559c5e7
    role: context
  - path: pages/traits/physiology/heat_shock_response.html
    sha256: a659c9e044a3f87fad52a8025c92f02fc39611b99c68e28dde96d052bfa4410a
    role: context
  - path: pages/traits/physiology/heterokaryon_incompatibility.html
    sha256: b9504c3814e97dc773609e25c09f314e9da2134f3d3dac89e828854a432d3e43
    role: context
  - path: pages/traits/physiology/heterothallism.html
    sha256: b64cf430557b3dcded46e486271559e286653f3047333923f13b48609e372ac7
    role: context
  - path: pages/traits/physiology/heterotrophic.html
    sha256: c61028442f608a3eaaabd0b47e690c47a5835b17a2ee2e5ebfdf28fd18d9ccf8
    role: context
  - path: pages/traits/physiology/histidine_arylamidase_activity.html
    sha256: 19d941c7c71f19609df70b706da1806a4aed94352cdbcaaecc74625f2e53a75b
    role: context
  - path: pages/traits/physiology/homeoviscous_adaptation.html
    sha256: 3be5919651d57c54e848f254c1b491a4f38ec7ce033bd55c6df871b1cf7f8d48
    role: context
  - path: pages/traits/physiology/homothallism.html
    sha256: 2ae544d4a6894bf8642ce53bfa43bac55eccbfeaf55319018afab8d648666026
    role: context
  - path: pages/traits/physiology/hydrogenotrophic.html
    sha256: e61301cb60d5b295ad89764b1913c36e72444df2c7a20a87eaf6067f33f37d71
    role: context
  - path: pages/traits/physiology/hyphal_anastomosis.html
    sha256: 516f0a92a3a1e9f781c6d0279c7d21932594a95b63faed5113da6513a5f38fde
    role: context
  - path: pages/traits/physiology/isogamy.html
    sha256: ad370f39c7f83c995c4ac36ad31b5a543dfb0572021fc40471380039c18d0212
    role: context
  - path: pages/traits/physiology/karyoklepty.html
    sha256: 0df634486b0b5e322fa50f12e305f5c6429c36ced413ebf8a7e44eeb035db8b4
    role: context
  - path: pages/traits/physiology/kinetocyst_discharge.html
    sha256: 7b23697277f3f9fcd7ccad33ee497d196e98cb15b75f3eaadc36fed7ad40af8d
    role: context
  - path: pages/traits/physiology/kleptoplasty.html
    sha256: a65318a70e26a9c6ce08f5fc83d9947ed8e59e92a03e056e1a9e8501603bd971
    role: context
  - path: pages/traits/physiology/lecithinase_activity.html
    sha256: c716cbdfb75370a9005523cff946dd6de0a57cc92e776a185e103be5c9b68a1c
    role: context
  - path: pages/traits/physiology/lethal_algicidal_activity.html
    sha256: 4c22aa96f3b3eb78c9b78a9c3050088a27f1adc5c8aa25581219aab0865956f3
    role: context
  - path: pages/traits/physiology/lethal_nematicidal_activity.html
    sha256: 6150c94297a483d852414c087c910a895156e47344e9301d626b7231d1eda30e
    role: context
  - path: pages/traits/physiology/leucine_arylamidase_activity.html
    sha256: 533791654b618c51b4e3ef7d7328ff54d72bc00f610042ed7e3d804887c667cb
    role: context
  - path: pages/traits/physiology/leucyl_glycine_arylamidase_activity.html
    sha256: ab0334b683fbb8a617d71a73c7c682db2d9ea2fcf39ba604620fcd0bbe4a5a59
    role: context
  - path: pages/traits/physiology/lipase_activity.html
    sha256: 686aa58b72a86218e120cfa517e48fdddb33235dd3cbadbe154288cf715fb5d0
    role: context
  - path: pages/traits/physiology/lipophagy.html
    sha256: 38e28b2de826228f13fd0967b807d50634185e0e8b109b973b3f6fa1d7dbef3a
    role: context
  - path: pages/traits/physiology/lithoautotrophic.html
    sha256: 2bd24d9890edda471203415d63d07149c5b2336b661c2ff588711a937fe7df61
    role: context
  - path: pages/traits/physiology/lithoheterotrophic.html
    sha256: 3cc6f79653807bdffb6acee5662d8f388b83363e492eb2123711f2bab50b309a
    role: context
  - path: pages/traits/physiology/lithotrophic.html
    sha256: a3a963a44630d8980db212deb1af2642a4f63a735919cdac33371c3f60d76e04
    role: context
  - path: pages/traits/physiology/lysine_decarboxylase_activity.html
    sha256: f9eaeef98e09081ee893b7ce6f506e304c41a649b60714e6e925edc329cde99c
    role: context
  - path: pages/traits/physiology/macropinocytosis.html
    sha256: c41a48350acb77eb743327b627e073166ae27f10edcc8c83e203b467e58169ff
    role: context
  - path: pages/traits/physiology/magnetotaxis.html
    sha256: ff8dda406cf11772185c1b01edf43693e549b5d3f424d9a761685b4451162151
    role: context
  - path: pages/traits/physiology/mating_type_switching.html
    sha256: 1f7ce39c7b8a51d73816ae36a3a7ab6522e7a028c563426d7024a020df3101eb
    role: context
  - path: pages/traits/physiology/methanotrophic.html
    sha256: 13ee344085ccd8bbb4773ac0a309d2651fd0e82ea6a0741f24949343157a1f41
    role: context
  - path: pages/traits/physiology/methylotrophic.html
    sha256: 7398679a55fab5546fb76b0fafb8dd3363495a58e31574b4ec9741cf6688339b
    role: context
  - path: pages/traits/physiology/mitophagy.html
    sha256: 732ff3d7507c8a5eec366832dbad85aeafade8b96d7af3f43081c869dac39526
    role: context
  - path: pages/traits/physiology/mixotrophic.html
    sha256: 880a90c52f5cdd9640348b5e7f92c82215634dd7c4d1a432b4e8a54eda8e7874
    role: context
  - path: pages/traits/physiology/mucocyst_discharge.html
    sha256: 211d12e6796953801d5b846b4712b0d7190885a727b23df2429a7592c95412ba
    role: context
  - path: pages/traits/physiology/myzocytosis.html
    sha256: 31e0270e6e0755708578c9c1a85861b5bfa1868509b4343199ee90f9692e75dc
    role: context
  - path: pages/traits/physiology/nad_dependent_alcohol_dehydrogenase_activity.html
    sha256: 335702dd57536fa29308f7ecadd8619f14129c912bfa1385223d594517426f53
    role: context
  - path: pages/traits/physiology/naphthol_as_bi_phosphohydrolase_activity.html
    sha256: 8fe1841b48102132e9fc34ea59d3c695d929e1f9560bd75c222b63b5b69051b2
    role: context
  - path: pages/traits/physiology/natural_competence.html
    sha256: eaa6372ea07d8148cf00f4120cb4c8ef3fe79e5879d9ce0a0364a1d96aa4ff86
    role: context
  - path: pages/traits/physiology/negative_autotropism.html
    sha256: 96f055e0849588cec03cfd4f424d1100b00e8783922a5870a76652aefc20abab
    role: context
  - path: pages/traits/physiology/nematode_attracting_activity.html
    sha256: a4608ae0a32cea461a971b5064f90ff5cb8aa283aa7acfcfab4616b9d322afd2
    role: context
  - path: pages/traits/physiology/nematode_egg_hatching_inhibitory_activity.html
    sha256: 42d2477a279cf8cc3581d88858d7d29600005dde9f12d6ef5ffb8bf7f5a3ec03
    role: context
  - path: pages/traits/physiology/nematode_egg_hatching_stimulatory_activity.html
    sha256: a5c10fd16259d2bd06a14268d9bf8262cfeca04ad8700f36a8df92fc2bb68f46
    role: context
  - path: pages/traits/physiology/nematode_repelling_activity.html
    sha256: b2e619626fbd7d22512c26add9e71241ad85772acd85aa406162ff0c206a9a98
    role: context
  - path: pages/traits/physiology/nucleophagy.html
    sha256: 0941f06477f51553bfee30bb426b73d431a7bdd49b7c6a185c389810f5e340f9
    role: context
  - path: pages/traits/physiology/nutrient_adaptation.html
    sha256: 24cf0a23e53d6cb946a62e37401a518ec4a3efe43b3f9c5e4a122bef0b7fa807
    role: context
  - path: pages/traits/physiology/oligotrophic.html
    sha256: 0e3d4701f426968f03380163de7372363d8a68ac2fd966ae58f423314218f154
    role: context
  - path: pages/traits/physiology/oogamy.html
    sha256: ef3114b47d248dfc3d5f0dd11b27bb655540f6756542aaa1242107de50fc1aa7
    role: context
  - path: pages/traits/physiology/organoheterotrophic.html
    sha256: 22dc6a1a4da8bf09c9539bdbab09fe34f2d211afac038603350db9f787ae9704
    role: context
  - path: pages/traits/physiology/organotrophic.html
    sha256: e4bb45edac7c9a7366fca7c73ba6a7f5f7280c61f911aa7326873036ba1b652f
    role: context
  - path: pages/traits/physiology/ornithine_decarboxylase_activity.html
    sha256: 11a9725fb6f0a2e95fc7d945e122fa0c311f40df0c0282e4432267c06e2c8a97
    role: context
  - path: pages/traits/physiology/osmotaxis.html
    sha256: 97358e09e2d80952c6c509a12e37d0ddd64306591a0d024792879555514a5ed5
    role: context
  - path: pages/traits/physiology/oxidase_activity.html
    sha256: e8f2c435c091e45226c4752d5b8e172ff9978b40b534ccd0bae1a6af58b3903f
    role: context
  - path: pages/traits/physiology/oxidative_stress_response.html
    sha256: 4eda77306fe7015339fde62bb4e55220362074f33247ee743dcf01516fbb780b
    role: context
  - path: pages/traits/physiology/paedogamy.html
    sha256: 0fa4301bdfed047338d88759895ab6ae66554aa55a9c6e2305c902516e659e27
    role: context
  - path: pages/traits/physiology/pallium_feeding.html
    sha256: 4107ad273b6b447605ffcfdc7f2373da3713c2b66f342ba87b472c8b5c379ca1
    role: context
  - path: pages/traits/physiology/parasexuality.html
    sha256: 9f6d6b0ef810dc0b22252a5f70ac605d13984f766e6dc13dc8a0d4fff9422e17
    role: context
  - path: pages/traits/physiology/persister_cell_formation.html
    sha256: 128025de20ec06fb13713ed24a0b399414018bf9b131b5c656f486729af92a5f
    role: context
  - path: pages/traits/physiology/pexophagy.html
    sha256: 749ac7a4b89744cc9b347680bef4b5c2d6e8a0087ca4d4dd3b76f06774444ead
    role: context
  - path: pages/traits/physiology/ph_taxis.html
    sha256: 3ff56cde337f4c832eff396276d029dc8015f86cf03d7f422f2b1f617934b155
    role: context
  - path: pages/traits/physiology/ph_tropism.html
    sha256: 53dcbcc1ed4c251a16bfbb990958eba0f1cca947298a5013a808f0b7e75eca52
    role: context
  - path: pages/traits/physiology/phagocytosis.html
    sha256: 3d6644a057891333c6951d05f2fc2ba71241ab364caefd6db17ec96e21fe55eb
    role: context
  - path: pages/traits/physiology/phagotrophy.html
    sha256: 039beb8e10c29d42026700b06cce37eedf1780858dcad3eb4046215db0eb0330
    role: context
  - path: pages/traits/physiology/phenylalanine_arylamidase_activity.html
    sha256: d5e2fdb6c5ddc6a78c70e4ee514ca2a561e3518fde544e1a39f623a37787569a
    role: context
  - path: pages/traits/physiology/photoautotrophic.html
    sha256: 44c04a741cd3f51bfb387463f2738c9411001b3196b4a50a827d8e0016056591
    role: context
  - path: pages/traits/physiology/photoheterotrophic.html
    sha256: 694593d9a953962ad721275154b83a9da233d638c63e91f5651a72281a01e9f2
    role: context
  - path: pages/traits/physiology/photokinesis.html
    sha256: d99a9832745e8648b67fd31c3eaaaef298251c9557ba6fe3c2b3e31bd5e98830
    role: context
  - path: pages/traits/physiology/photolithoautotrophic.html
    sha256: 142841ef4f389eedf627b83ad52cc3ff0bef33ecbed146fe8faa197cf0f3e966
    role: context
  - path: pages/traits/physiology/photolithotrophic.html
    sha256: ab843972e1f15493fefba52945d682627af77db54a38501406f4eae605fc6662
    role: context
  - path: pages/traits/physiology/photoorganoheterotrophic.html
    sha256: 9aa7ffaf7a4bfdecf22fc0017065cb7caebe0762f31724d8f1c2415cccf5cdbc
    role: context
  - path: pages/traits/physiology/phototaxis.html
    sha256: 3c4d1dfe77f8d36b9d8f9ad3590dcbb6d9b6a61f3fe742388fcbbc6fe0344be1
    role: context
  - path: pages/traits/physiology/phototrophic.html
    sha256: 373e494b851ce029c61c9587bfe21664bf6a382c3cb2c7952c13c41bcb5bea1d
    role: context
  - path: pages/traits/physiology/phototropism.html
    sha256: a6c47f775fb178e1b850aee76bc179de84fe95e65a948d8a2b7fab182f77019b
    role: context
  - path: pages/traits/physiology/pinocytosis.html
    sha256: 1e1fb86e5da33d23b52f2b7be146be6e55ac4ff855587ef4e671c610ddbbb708
    role: context
  - path: pages/traits/physiology/positive_autotropism.html
    sha256: b348ee04d301020d464e716f1a247c501cd8979809c600d9e7b2f57ffcf4b9b5
    role: context
  - path: pages/traits/physiology/primary_homothallism.html
    sha256: a85ac98429680a968af4f20ef78e4e848694697701d5dcc6c7769a2e522cd982
    role: context
  - path: pages/traits/physiology/prolyl_aminopeptidase_activity.html
    sha256: 9e9c34a946b2d906c8a6d4162ede62bbfac842853716c0933f84ce0e0e71cee3
    role: context
  - path: pages/traits/physiology/proteaphagy.html
    sha256: 0b0a610cc5a9c24e59963f984f0d494f70799fcd3670a1e0c07834889d0ad2a1
    role: context
  - path: pages/traits/physiology/pseudobipolar_mating_system.html
    sha256: c49f9eec367f1faa241abdda9b7772de3310c474c1d5145e9e30e9ec839f6048
    role: context
  - path: pages/traits/physiology/pseudohomothallism.html
    sha256: 2eb773f0399bf5c6be38a589572c57b123fdd917db102f092111fa384cacf503
    role: context
  - path: pages/traits/physiology/pyrazinamidase_activity.html
    sha256: 397511ca2d04337155ea8a3ff115b4640e018b0d81b23d47cd5eeccdc37488b1
    role: context
  - path: pages/traits/physiology/pyrrolidonyl_arylamidase_activity.html
    sha256: f9a6a61a3b3314a879dde3246e3e982c465a7cd7d67fe24f06b56ed2de5a391e
    role: context
  - path: pages/traits/physiology/quorum_quenching.html
    sha256: bab53da40c659d1f36eb20974f8fbe08e080041cab3ba99dd5c34990903d9a5b
    role: context
  - path: pages/traits/physiology/quorum_sensing.html
    sha256: 0617a9c1729835e067f7eb5f63f3fc24f8103ad097f5e949d84e06796486f75c
    role: context
  - path: pages/traits/physiology/rapid_axopodial_contraction.html
    sha256: 109b4bf2a90d4d11623ccb99cd1ba398b1f6b8f1a5824ce12f81ae0d04b75ea3
    role: context
  - path: pages/traits/physiology/replicative_aging.html
    sha256: 85843fbe50e12e4feecb92f36c5b7d57896de4d828d4d797e62d11ec114f76fb
    role: context
  - path: pages/traits/physiology/reversible_nematode_paralyzing_activity.html
    sha256: f6480e3ca27dea2f0d720e957b26c20fe18818b9ff70b7337fa2ce260c1a2cfd
    role: context
  - path: pages/traits/physiology/rheotaxis.html
    sha256: 4613d6c265faecf41bb6b7cd4e6d3da7aa491137c3ed523fda8346a585fe619a
    role: context
  - path: pages/traits/physiology/rheotropism.html
    sha256: c1d77d05a8bcfb05a3f89aafc6c75281ec08453b88d469342afcd814e2342f6e
    role: context
  - path: pages/traits/physiology/ribophagy.html
    sha256: b724eba974d410667b404b062c99cbf9c2cc976c0ed9e490d2686b99fef144fb
    role: context
  - path: pages/traits/physiology/serine_arylamidase_activity.html
    sha256: d31a5b354f801c735916dbbf73affcad2d4ba45e126aaf73e297cf48bb0a3ebe
    role: context
  - path: pages/traits/physiology/siderophore_production.html
    sha256: a13e2e54c1d6490a2dc9edc9fa0c2600731443461df8236808db31209b613044
    role: context
  - path: pages/traits/physiology/siliceous_scale_production.html
    sha256: 4149300a9a34ca69d9d7f6f5be1c65913a955fa1637b81d0bc231976b5b7cf3f
    role: context
  - path: pages/traits/physiology/sos_response.html
    sha256: 8bfeec9bf232950875588f16715abb258ad7ca86cbb74a2f5822e372944f28dd
    role: context
  - path: pages/traits/physiology/spore_germination.html
    sha256: df7f63441af0860794a036336e372e5fee0520514c63dc975863cbfd5b9e0e82
    role: context
  - path: pages/traits/physiology/stress_response.html
    sha256: 0eab606686a2aa1d56b9282fc25b3f99cb2ae9956447271f0779fefec0ea5698
    role: context
  - path: pages/traits/physiology/tetrapolar_mating_system.html
    sha256: e13fd73aa6ca0fc55077f3f2dceae5d6d00782e2c399b1d4d3bae5c34482ba66
    role: context
  - path: pages/traits/physiology/thermotaxis.html
    sha256: 87f89694ed697486a6e5af87ed214a8f5893adcdc65def77acf3433f2a2d4fc0
    role: context
  - path: pages/traits/physiology/thigmotropism.html
    sha256: 6e25b8949c306e42f4fb9a6ddc7894725e2af44f1847a8abdceb5b3ce9754c36
    role: context
  - path: pages/traits/physiology/toxicyst_discharge.html
    sha256: 923b80c44b05d7bdd8ae20bc414ccd4d5dcb2a1d26771ec49c5f325c2699426b
    role: context
  - path: pages/traits/physiology/trichocyst_discharge.html
    sha256: aa3ca2e312436d91dbaa99354ec9714b357aea6a1a25ace4a2c27cd7921308e8
    role: context
  - path: pages/traits/physiology/tripolar_mating_system.html
    sha256: e5f1efa3450a5b5a16ab56bf248cda3ecd4e70d05c72a257d72984e95780fbe5
    role: context
  - path: pages/traits/physiology/trogocytosis.html
    sha256: 072c11f60b85217d33f5692014d3a7d95c95b883208fcb1d3e3ccee4c1e61c64
    role: context
  - path: pages/traits/physiology/trophic_type.html
    sha256: 7f511190f31bf56f55bc6075358f54ecf89d88df78e6eb50131384e851b43a70
    role: context
  - path: pages/traits/physiology/trypsin_activity.html
    sha256: c74cb94daa46729808c7bad6db295f80391526008763b47cca0185c10cd4c093
    role: context
  - path: pages/traits/physiology/tyrosine_arylamidase_activity.html
    sha256: 0e52a0f0ffd09a5f980450adab287aa175028f019b776e75adb5443beb159cec
    role: context
  - path: pages/traits/physiology/unconventional_protein_secretion.html
    sha256: ab0b0dfd06847ea30cd55f8344ea6b7d6a7c7b56397f434f559dbfd92096a9e2
    role: context
  - path: pages/traits/physiology/unequal_protein_aggregate_inheritance.html
    sha256: 02722c295eca3557785cb3eb9ca5cfd6644edbf7274777428fd38fa73a2856ad
    role: context
  - path: pages/traits/physiology/unisexual_reproduction.html
    sha256: ac83d368a1e7d7072f1308c41167dc5c44901a870ab8ed80cdc890bf04ff0f6e
    role: context
  - path: pages/traits/physiology/urease_activity.html
    sha256: f674db606132a7e1ba1bb24ac602b8b6a72eefddfc0091c227b40dfc073a90f4
    role: context
  - path: pages/traits/physiology/valine_arylamidase_activity.html
    sha256: d93370a25f50cc290830653a9970a1bcf3103c91b5cfaedbe8972f51ab78a03a
    role: context
  - path: pages/traits/physiology/viable_but_nonculturable_state.html
    sha256: a58fe3efad2333408669ff65c42524d5629effe15e6f08379e71d9275d528dcc
    role: context
  - path: pages/traits/physiology/viscotaxis.html
    sha256: 382d126607432c81286e180ced9b82b59964ea047189bea2b73617017481399c
    role: context
  - path: pages/traits/quantitative_property/has_maximum_observed_value.html
    sha256: 300a094a4887ab04b053b8f0e05b67edfd8b24feb4fbf9dba5bfc52765fd8c5e
    role: context
  - path: pages/traits/quantitative_property/has_minimum_observed_value.html
    sha256: 008e3ffadd55dc38b6a3facc4d023b6c63c8f9194300801ba525de4f017bede9
    role: context
  - path: pages/traits/quantitative_property/has_observed_spot_value.html
    sha256: 2f4727365503caf324f9503119376681f19d481137dc5bf2cf30086e72466660
    role: context
  - path: pages/traits/quantitative_property/has_value.html
    sha256: 359473f1f4227b45d9bb2810e4894714687ae8092995fcb24a0150c34cc1ff81
    role: context
  - path: pages/traits/quantitative_property/has_value_comments.html
    sha256: caaf8d223b373112aae7ec40a42838f4f5d70003e8a39162c9a56c235027c449
    role: context
  - path: pages/traits/quantitative_property/is_negative_data.html
    sha256: dca9319492f143fddb4ed28b0b37b0e49b28bd08db8ff2373d683ba51896e93c
    role: context
  - path: pages/traits/quantitative_property/observation_data_property.html
    sha256: bd2a85f8d7a383afe2bdce8bc989546b489a5ad347cf643ab708319b3f72b104
    role: context
  - path: pages/traits/upper/biological_process.html
    sha256: e95e942e968dcc537c9b8498331ddf636a02c306048eaf0dec839779b21c78fe
    role: context
  - path: pages/traits/upper/chemical_entity.html
    sha256: 789e2551e67ae24fd3d3b9f3ee5fcbf651460ab9b5b7c9db1413c01d9ebd43a8
    role: context
  - path: pages/traits/upper/enzyme.html
    sha256: 87871cdd6a23dd780fe8c0e4ee0693a09296d4227735c5cb475b979eb9e61494
    role: context
  - path: pages/traits/upper/material_entity.html
    sha256: 00f51e2d7eac0b530ed9118347b269ed38f07ec35843c7503ad23de985bb1819
    role: context
  - path: pages/traits/upper/microbe.html
    sha256: 94a481f3a8d1f7ba44809504e76d3adaaa49493cdb80dc20892f7d05dee129d0
    role: context
  - path: pages/traits/upper/observation.html
    sha256: f52e070c20dc9783d26117e1c8451f16193fd59bfd79318dc9628104f1170627
    role: context
  - path: pages/traits/upper/phenotype.html
    sha256: 39c1427ae8a63cac29bd1bbf6c9704a5c5561964b267ecf67cd7fad4ada24802
    role: context
  - path: pages/traits/upper/quality.html
    sha256: 7819eb3b5b2c8419fa84ff92aace2cfdcec64b4af7ff135097ce9c2f67ddee71
    role: context
  - path: pages/umap.html
    sha256: 27eb45f1d8f6250a62bb85d7bf1a715381a628d0d30aa6166f1385824e2b4ee5
    role: context
  - path: proposals/metpo_traitmech_v601/metpo_proposal_classes_robot.tsv
    sha256: 421f536e6cb963aebd51538adfa86522fcb58cba9ebe867bdb4ced0da49a5f40
    role: context
  - path: proposals/metpo_traitmech_v601/proposal.md
    sha256: b3f0ed4c2c28aec793bba3690cfb6922dbdc2f963f52a1af8e3970ed029821a4
    role: context
  - path: reports/proposal_citation_audit.tsv
    sha256: c81130b02675f7ecdfa8c4039d01e233ada714e9ace5e549a232f8f2a34c7c56
    role: context
  - path: reports/robot/metpo_traitmech_v601/classes.owl
    sha256: 30d658276aca51f28b662aa01344e7938463aae47fbce05f3687e9fe240d9827
    role: context
  - path: reports/robot/metpo_traitmech_v601/merged.owl
    sha256: 740dfd191e54d99f5e9bd267e1145bd0ef8d622f449d556cdcb474d5fe33486b
    role: context
  - path: reports/robot/metpo_traitmech_v601/reasoned.owl
    sha256: a2b855f97e22335cfb173fc0d17c3fbd43192584a0e56f3d358e50c4e8d0847e
    role: context
  - path: research/traits/physiology/nematode_repelling_activity-source-verification.json
    sha256: 4e3f2529c9123d3612d62775fb3d5e850cdc9cde88d871b7c0dc8c05f7d8c48b
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/add_nematode_repelling_activity_trait.py
    sha256: c6ea8fc69f21b98efd581ad098c7888175becc412be14b87c630903c01e6e0e0
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
  - path: tests/test_add_nematode_repelling_activity_trait.py
    sha256: eb846cc3150a93962c0acd8495012bff4d79bb625e7ce5d12672ac31452bacdd
    role: context
targets:
- target_id: traitmech:000725
  path: data/traits/physiology/nematode_repelling_activity.yaml
  label: nematode-repelling activity
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/physiology/nematode_repelling_activity.yaml
    role: maintained record
  - repository: CultureBotAI/TraitMech
    path: scripts/add_nematode_repelling_activity_trait.py
    role: guarded curation writer
scope:
  description: One complete new record and its maintained/generated owners; not whole-corpus
    scientific review.
  selection: One exact new trait, no sampling.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - traitmech:000725
  exclusions:
  - target: Other 1119 TraitRecords
    reason: Novelty context, deterministic diagnostics and byte preservation only.
  - target: data/traits/physiology/spore_germination.yaml
    reason: Protected and unchanged.
checks:
- check_id: records-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate
    -s src/traitmech/schema/traitmech.yaml --target-class TraitRecord data/traits/physiology/nematode_repelling_activity.yaml
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate
    -s src/traitmech/schema/traitmech.yaml --target-class TraitRecord data/traits/physiology/nematode_repelling_activity.yaml
  status: passed
  required: true
  target_ids:
  - traitmech:000725
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; deterministic corpus diagnostics are
    not corpus-wide scientific review.
- check_id: records-1
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_strict.py data/traits/physiology/nematode_repelling_activity.yaml
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_strict.py data/traits/physiology/nematode_repelling_activity.yaml
  status: passed
  required: true
  target_ids:
  - traitmech:000725
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; deterministic corpus diagnostics are
    not corpus-wide scientific review.
- check_id: records-2
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_history_links.py history/records/nematode_repelling_activity
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_history_links.py history/records/nematode_repelling_activity
  status: passed
  required: true
  target_ids:
  - traitmech:000725
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; deterministic corpus diagnostics are
    not corpus-wide scientific review.
- check_id: records-3
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/verify_snippets.py --record data/traits/physiology/nematode_repelling_activity.yaml
    --out /tmp/traitmech-repellence-checks-20261014/native-record.tsv
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/verify_snippets.py --record data/traits/physiology/nematode_repelling_activity.yaml
    --out /tmp/traitmech-repellence-checks-20261014/native-record.tsv
  status: passed
  required: true
  target_ids:
  - traitmech:000725
  exit_code: 0
  expected_exit_code: 0
  summary: 'Actual record CLI: Pradel VERIFIED; Prakash NOT_IN_ABSTRACT, separately
    matched in its own Discussion.'
- check_id: records-4
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q tests/test_add_nematode_repelling_activity_trait.py -k 'not source_receipt'
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q tests/test_add_nematode_repelling_activity_trait.py -k 'not source_receipt'
  status: passed
  required: true
  target_ids:
  - traitmech:000725
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; deterministic corpus diagnostics are
    not corpus-wide scientific review.
- check_id: focused-recheck-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q tests/test_add_nematode_repelling_activity_trait.py tests/test_readme_artifacts.py
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q tests/test_add_nematode_repelling_activity_trait.py tests/test_readme_artifacts.py
  status: passed
  required: true
  target_ids:
  - traitmech:000725
  exit_code: 0
  expected_exit_code: 0
  summary: Corrected README prose count and new writer tests pass. Earlier focused
    run retained one stale-count failure and 60 passes; it is not misreported as a
    pass.
- check_id: focused-recheck-1
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/ruff
    check src scripts tests
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/ruff
    check src scripts tests
  status: passed
  required: true
  target_ids:
  - traitmech:000725
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; deterministic corpus diagnostics are
    not corpus-wide scientific review.
- check_id: generate-0
  name: just audit-proposals
  command: just audit-proposals
  status: passed
  required: true
  target_ids:
  - traitmech:000725
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; deterministic corpus diagnostics are
    not corpus-wide scientific review.
- check_id: generate-1
  name: just ground-predicates
  command: just ground-predicates
  status: passed
  required: true
  target_ids:
  - traitmech:000725
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; deterministic corpus diagnostics are
    not corpus-wide scientific review.
- check_id: generate-2
  name: just ground-nodes
  command: just ground-nodes
  status: passed
  required: true
  target_ids:
  - traitmech:000725
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; deterministic corpus diagnostics are
    not corpus-wide scientific review.
- check_id: generate-3
  name: just audit-graphs
  command: just audit-graphs
  status: passed
  required: true
  target_ids:
  - traitmech:000725
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; deterministic corpus diagnostics are
    not corpus-wide scientific review.
- check_id: generate-4
  name: just audit-graph-protein-taxa
  command: just audit-graph-protein-taxa
  status: passed
  required: true
  target_ids:
  - traitmech:000725
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; deterministic corpus diagnostics are
    not corpus-wide scientific review.
- check_id: generate-5
  name: just audit-predicate-domains
  command: just audit-predicate-domains
  status: passed
  required: true
  target_ids:
  - traitmech:000725
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; deterministic corpus diagnostics are
    not corpus-wide scientific review.
- check_id: generate-6
  name: just check-biolink-coverage
  command: just check-biolink-coverage
  status: passed
  required: true
  target_ids:
  - traitmech:000725
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; deterministic corpus diagnostics are
    not corpus-wide scientific review.
- check_id: generate-7
  name: just audit-snippets
  command: just audit-snippets
  status: passed
  required: true
  target_ids:
  - traitmech:000725
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; deterministic corpus diagnostics are
    not corpus-wide scientific review.
- check_id: generate-8
  name: just gen-discussions-data
  command: just gen-discussions-data
  status: passed
  required: true
  target_ids:
  - traitmech:000725
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; deterministic corpus diagnostics are
    not corpus-wide scientific review.
- check_id: generate-9
  name: just gen-qc-dashboard
  command: just gen-qc-dashboard
  status: passed
  required: true
  target_ids:
  - traitmech:000725
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; deterministic corpus diagnostics are
    not corpus-wide scientific review.
- check_id: generate-10
  name: just gen-pages
  command: just gen-pages
  status: passed
  required: true
  target_ids:
  - traitmech:000725
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; deterministic corpus diagnostics are
    not corpus-wide scientific review.
- check_id: generate-11
  name: just gen-priority-dashboard
  command: just gen-priority-dashboard
  status: passed
  required: true
  target_ids:
  - traitmech:000725
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; deterministic corpus diagnostics are
    not corpus-wide scientific review.
- check_id: verify-0
  name: just qc
  command: just qc
  status: passed
  required: true
  target_ids:
  - traitmech:000725
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; deterministic corpus diagnostics are
    not corpus-wide scientific review.
- check_id: verify-1
  name: just validate-history
  command: just validate-history
  status: passed
  required: true
  target_ids:
  - traitmech:000725
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; deterministic corpus diagnostics are
    not corpus-wide scientific review.
- check_id: verify-2
  name: just validate-products
  command: just validate-products
  status: passed
  required: true
  target_ids:
  - traitmech:000725
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; deterministic corpus diagnostics are
    not corpus-wide scientific review.
- check_id: verify-3
  name: just verify-proposal metpo_traitmech_v601
  command: just verify-proposal metpo_traitmech_v601
  status: passed
  required: true
  target_ids:
  - traitmech:000725
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; deterministic corpus diagnostics are
    not corpus-wide scientific review.
- check_id: verify-4
  name: just robot-validate-proposal metpo_traitmech_v601
  command: just robot-validate-proposal metpo_traitmech_v601
  status: passed
  required: true
  target_ids:
  - traitmech:000725
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; deterministic corpus diagnostics are
    not corpus-wide scientific review.
- check_id: verify-5
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/audit_canonical_examples.py --no-resolve
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/audit_canonical_examples.py --no-resolve
  status: passed
  required: true
  target_ids:
  - traitmech:000725
  exit_code: 0
  expected_exit_code: 0
  summary: Canonical-example shape audit used --no-resolve, not live taxonomic validation;
    no examples asserted.
- check_id: verify-6
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/run_trait_graph_audit.py --verify
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/run_trait_graph_audit.py --verify
  status: passed
  required: true
  target_ids:
  - traitmech:000725
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; deterministic corpus diagnostics are
    not corpus-wide scientific review.
- check_id: verify-7
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/audit_history_records.py --base 55407337d8572f15d01f47bf6c9a99abc05d264a
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/audit_history_records.py --base 55407337d8572f15d01f47bf6c9a99abc05d264a
  status: passed
  required: true
  target_ids:
  - traitmech:000725
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; deterministic corpus diagnostics are
    not corpus-wide scientific review.
- check_id: tests-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q --junitxml=/tmp/traitmech-repellence-checks-20261014/pytest.xml
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q --junitxml=/tmp/traitmech-repellence-checks-20261014/pytest.xml
  status: passed
  required: true
  target_ids:
  - traitmech:000725
  exit_code: 0
  expected_exit_code: 0
  summary: 4637 tests passed with no failures, errors or skips.
- check_id: template-format
  name: template-format
  command: git diff 55407337d8572f15d01f47bf6c9a99abc05d264a HEAD --check -- proposals/metpo_traitmech_v601/metpo_proposal_classes_robot.tsv
  status: passed
  required: true
  target_ids:
  - traitmech:000725
  exit_code: 2
  expected_exit_code: 2
  summary: 'Expected ordinary diagnostic: only the ROBOT directive header trailing
    empty cells. Not an unqualified whitespace pass.'
- check_id: template-scoped
  name: template-scoped
  command: git -c core.whitespace=-blank-at-eol diff 55407337d8572f15d01f47bf6c9a99abc05d264a
    HEAD --check -- proposals/metpo_traitmech_v601/metpo_proposal_classes_robot.tsv
  status: passed
  required: true
  target_ids:
  - traitmech:000725
  exit_code: 0
  expected_exit_code: 0
  summary: Only this inspected template exempts trailing empty cells; global Git settings
    unchanged.
- check_id: other-whitespace
  name: other-whitespace
  command: git diff 55407337d8572f15d01f47bf6c9a99abc05d264a HEAD --check -- . ':(exclude)proposals/metpo_traitmech_v601/metpo_proposal_classes_robot.tsv'
  status: passed
  required: true
  target_ids:
  - traitmech:000725
  exit_code: 0
  expected_exit_code: 0
  summary: All other committed paths pass the ordinary whitespace check.
- check_id: products
  name: products
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    /tmp/traitmech-repellence-products-20261014.py
  status: passed
  required: true
  target_ids:
  - traitmech:000725
  exit_code: 0
  expected_exit_code: 0
  summary: All 1119 prior records, including protected spore germination, and prior
    history/reviews/proposals/embeddings/templates/baseline are byte-preserved. Old
    trait-page changes are footer-only except the phenotype child link. Parsed RDF
    uses real w3id hierarchy and definition annotations.
- check_id: browser
  name: browser
  command: node /tmp/traitmech-repellence-browser-20261014.cjs
  status: passed
  required: true
  target_ids:
  - traitmech:000725
  exit_code: 0
  expected_exit_code: 0
  summary: '1440/390 px browser checks pass: two quotes, two discussions, one history,
    local identifier, working hierarchy/browse navigation, 1120 count and loaded coverage
    image. Eight screenshots visually inspected; no overflow or page errors.'
evidence:
- evidence_id: source-0
  kind: primary_source
  reference: DOI:10.1073/pnas.0610281104
  locator: Scientific Abstract; /html/body/div[2]/div[2]/div/div[1]/div/div[2]/main/article/section[2]/section/section[1]
  accessed_at: '2026-10-14T09:56:04Z'
  support: supports
  snapshot_sha256: f3fae8fd3c82bbf27a32294f7b461e75f74b06dd502a9e4998b90c1b42e2982f
  summary: Pradel et al. 2007, PMID:17267603, PMCID:PMC1892944, scientific Abstract;
    exact normalized PMC match and native VERIFIED. C. elegans denotes Caenorhabditis
    elegans. Own Results and actual Figures 1-4 distinguish initial entry followed
    by leaving Serratia marcescens lawns from absence of attraction. A swrA insertion
    mutant shows reduced lawn leaving but similar multiday killing; reduced avoidance
    is not loss of pathogenicity. Purified serrawettin W2 on E. coli OP50 lawns and
    acute drop-induced reversal are separate assays. The 16-hour bacterial-lawn endpoint,
    60-minute supplemented-lawn endpoint and acute reversal are not one exposure.
    Chemical recognition versus a mechanical surfactant cue remains unresolved, and
    other bacterial cues can contribute. Serratia swrA is not the similarly named
    Bacillus motility regulator.
- evidence_id: source-1
  kind: primary_source
  reference: DOI:10.15252/embj.2020106938
  locator: Discussion, first paragraph, own-study result; /article/body/sec[3]/p[1]
  accessed_at: '2026-10-14T09:56:04Z'
  support: supports
  snapshot_sha256: 0ee3bcb615186a5c80173172514423253bb7d89cec71cabf44832bb5e14fcf07
  summary: Prakash et al. 2021, PMID:34086368, PMCID:PMC8246062, Discussion first
    paragraph, own-study result; directly matched JATS, PMC and publisher text. Native
    NOT_IN_ABSTRACT is retained, not relabeled VERIFIED. This is its own experiment,
    not a citation of Pradel. P. aeruginosa denotes Pseudomonas aeruginosa. Figure
    1A-B measures PA14 lawn occupancy over 12 hours. Pure 1-undecene gives negative
    chemotaxis and omega turns in distinct Figure 2 and Appendix S2 assays. PA14-versus-undA
    odor choice establishes relative preference, not by itself repulsion or complete
    loss of bacterial repellence. Peer-review reply page 14 reports reversals but
    no complete lawn leaving after 1-undecene on OP50; the alternative adjacent-lawn
    crossing assay is not eviction from an occupied lawn. Roaming or higher mean square
    displacement alone is not directional avoidance. Recipient sensory genetics is
    not a microbial causal pathway.
- evidence_id: content
  kind: record_content
  reference: data/traits/physiology/nematode_repelling_activity.yaml
  locator: Complete new record, guarded writer, tests, proposal, history, verification
    sidecar and generated diff.
  accessed_at: '2026-10-14T09:56:04Z'
  support: supports
  summary: One microbial capability eliciting active nematode movement away. Own microbial
    taxis, absence of attraction, relative food preference alone, paralysis, killing,
    trapping, feeding and hatching are not substitutes. No organism-level disjointness
    from attraction or lethality.
- evidence_id: ontology
  kind: database
  reference: data/raw/metpo.owl
  locator: Pinned/current releases, explicit editor and six TSV owners; existing nearby
    traits.
  accessed_at: '2026-10-14T09:56:04Z'
  support: supports
  summary: Phenotype METPO:1000059 below quality METPO:1000188 is broader. Deprecated
    chemotaxis METPO:1000062 has no replacement/consider in inspected ontology and
    is not an exact counterpart; not revived or mapped. Explicit editor has 31 metadata
    triples and no imports. Pin unchanged.
- evidence_id: novelty
  kind: search
  reference: research/traits/physiology/nematode_repelling_activity-source-verification.json
  locator: Ignored/hidden current copies, retained regular-file history, pending changed
    blobs and selected upstream owners.
  accessed_at: '2026-10-14T09:56:04Z'
  support: supports
  summary: '188 locations, 143 retained heads, 23435 TraitMech and 5815 CommunityMech
    unique regular blobs; 719 unique path/text variants assessed. Remote: 11 open/draft
    PRs, 783 changed blobs, 587 selected owners and 21 matched files assessed. CeMbio
    member preference is not whole-consortium repulsion. Two decimal embedding hits
    and 857 broad editor-envelope occurrences are not competing reservations. No exact
    synonym/node/parent-gap migration found in bounded scope.'
  search_scope: Available ignored/hidden files included. No lost historical ignored/untracked
    reconstruction, symlink targets or arbitrary local archive decoding. Pending content
    scope is changed blobs, not entire PR trees. Not atomic allocation.
- evidence_id: provenance
  kind: authority
  reference: research/traits/physiology/nematode_repelling_activity-source-verification.json
  locator: Exact snippets, source sections, actual figures, supplement/reply checks,
    native CLI and notice receipts.
  accessed_at: '2026-10-14T09:56:04Z'
  support: supports
  summary: Pradel is definition authority; Prakash reports its own experiment. The
    18/21-word quotes match scientific Abstract and Discussion respectively; native
    VERIFIED/NOT_IN_ABSTRACT remain distinct. Prakash figure URL 404s were helper
    construction errors, corrected using exact published links. Bounded metadata/notice
    checks are not comprehensive clearance.
- evidence_id: products
  kind: validation
  reference: reports/proposal_citation_audit.tsv
  locator: Native gates, parsed OWL, byte preservation and responsive browser checks.
  accessed_at: '2026-10-14T09:56:04Z'
  support: supports
  summary: 'Final required checks pass. RDF triple counts {''classes'': 15, ''merged'':
    12628, ''reasoned'': 12632}. Only Pradel and local record annotate the definition.
    README counts agree after the detected prose fix. Pinned CLAW 645 blobs verified;
    exact configured embedding inputs absent, so embeddings retained.'
- evidence_id: history
  kind: record_content
  reference: history/records/nematode_repelling_activity
  locator: Minting timestamp and append-only CREATE history.
  accessed_at: '2026-10-14T09:56:04Z'
  support: supports
  summary: Observed acceptance at 2026-10-14T09:11:26Z precedes CREATE. Actor codex,
    GPT-5 and LLM assistance are explicit. Status remains PROPOSED, not human-reviewed.
- evidence_id: publication
  kind: search
  reference: /tmp/traitmech-repellence-publication-20261014/accepted.json
  locator: Fresh local reservation scan and live remote heads/body/state guards.
  accessed_at: '2026-10-14T09:56:04Z'
  support: supports
  snapshot_sha256: dca1263160207f96c8eccaf3a79e0b9a1a5a6e2427d915811513fcec18ec5bd6
  summary: 189 current locations rechecked; owned hits separated, no conflict identified.
  search_scope: Available ignored/hidden files included. No lost historical ignored/untracked
    reconstruction, symlink targets or arbitrary local archive decoding. Pending content
    scope is changed blobs, not entire PR trees. Not atomic allocation.
assessments:
- assessment_id: identity
  area: identity
  topic: Microbial actor and active movement endpoint
  summary: Repellence is distinct from lack of attraction or relative preference alone.
    The definition does not require killing, feeding, infection or a shared chemical
    mechanism.
  target_ids:
  - traitmech:000725
  evidence_ids:
  - content
  - source-0
  - source-1
  outcome: supported
- assessment_id: evidence
  area: evidence
  topic: Two primary behavioral studies
  summary: Initial lawn entry then leaving, acute reversal and pure-compound negative
    chemotaxis support the capability. Condition-, recipient- and strain-specific
    assays are not pooled into a universal response.
  target_ids:
  - traitmech:000725
  evidence_ids:
  - source-0
  - source-1
  - content
  outcome: supported
- assessment_id: grounding
  area: grounding
  topic: Broader parent and local fallback
  summary: Phenotype is broader. Deprecated microbial chemotaxis is not equivalent.
    Ignored-inclusive novelty and reservation checks support this bounded local proposal;
    no exact coupled migration identified.
  target_ids:
  - traitmech:000725
  evidence_ids:
  - ontology
  - novelty
  - publication
  - content
  outcome: supported
- assessment_id: provenance
  area: provenance
  topic: Direct sections versus native abstract status
  summary: Both quotes are verbatim; full-text verification is not mislabeled native
    VERIFIED. Definition annotations exclude the second paper bibliography; actual
    figure and review limits are preserved.
  target_ids:
  - traitmech:000725
  evidence_ids:
  - provenance
  - source-0
  - source-1
  - products
  outcome: supported
- assessment_id: products
  area: consistency
  topic: Guarded writers and native generated artifacts
  summary: Fail-closed drift/replay, schema, full tests, QC, history, RDF and responsive
    page checks pass. Prior records and immutable bundles remain byte-preserved.
  target_ids:
  - traitmech:000725
  evidence_ids:
  - products
  - history
  - content
  outcome: supported
- assessment_id: limits
  area: completeness
  topic: Mechanism, host range and protocol limits
  summary: Chemical versus mechanical cue, varied bacterial cues, headspace protocol
    discrepancy and relative-choice limitations remain unresolved. No common mechanism,
    canonical examples, universal nonlethality, field efficacy or safety is established.
  target_ids:
  - traitmech:000725
  evidence_ids:
  - source-0
  - source-1
  - content
  - provenance
  outcome: unknown
findings: []
actions: []
limitations:
- Author self-review only; exact-head external review, CI, queue and landed-tree verification
  remain separate unfinished publication gates at this timestamp.
- Own source sections and selected figures/supplement/replies were inspected, not
  all raw data or every figure. Prakash S3/table coverage is textual; reply pages
  14 and 30 were visually checked.
- Compound production/gene presence is insufficient for organismal repellence. No
  universal host response, common mechanism, canonical taxonomy, safety or field efficacy.
- Prakash native NOT_IN_ABSTRACT is retained despite direct Discussion matching. Pradel
  publisher 403 and bounded correction/retraction searches are not comprehensive notice
  clearance.
- Canonical-example audit used --no-resolve; no canonical examples or proteins asserted.
- Known ignored/hidden copies included; lost ignored/untracked history, symlinks,
  submodules, arbitrary archives and unchanged pending PR files are not reconstructed.
  Allocation is not atomic; discovery is not exhausted.
- Earlier focused run found one stale README prose count; corrected before checkpoint
  and passing targeted/full reruns. No unresolved test failure is hidden.
- Exact configured embedding inputs absent; existing embeddings retained. Required
  empty ROBOT cells use a path-scoped whitespace exception.
tags:
- add-trait
- nematode-repelling-activity
- self-review
```
