# Adversarial review of extracellular-trail-based spatial memory

- Review: 20261013T070924Z-extracellular-trail-memory
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-13T06:53:53Z
- Finished UTC: 2026-10-13T07:09:24Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The qualified microbial phenotype is supported at the external spatial trace level. Source versions, assay controls, claim-bearing spans, semantic neighbors, historical identifiers, allocation and generated products were challenged. No actionable defect was identified in scope; three discussions stay OPEN and mapping remains PROPOSED.

## Scope And Provenance

Entire new record and maintained/generated change set, not whole-corpus scientific review.

Selection: One exact newly curated trait; no sampling.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base d2f20fbc560bbffee0e50a1194261202fbd13715.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| traitmech:000715 | data/traits/physiology/extracellular_trail_based_spatial_memory.yaml | maintained | extracellular-trail-based spatial memory |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate -s src/traitmech/schema/traitmech.yaml --target-class TraitRecord data/traits/physiology/extracellular_trail_based_spatial_memory.yaml | passed | True | traitmech:000715 | Actual maintained gate passed. Corpus diagnostics are not whole-corpus scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/validate_strict.py data/traits/physiology/extracellular_trail_based_spatial_memory.yaml | passed | True | traitmech:000715 | Actual maintained gate passed. Corpus diagnostics are not whole-corpus scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/validate_history_links.py history/records/extracellular_trail_based_spatial_memory | passed | True | traitmech:000715 | Actual maintained gate passed. Corpus diagnostics are not whole-corpus scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate -s src/traitmech/schema/history.yaml --target-class HistoryRecord history/records/extracellular_trail_based_spatial_memory/2026-10-13T064512Z-codex-64c936.yaml | passed | True | traitmech:000715 | Actual maintained gate passed. Corpus diagnostics are not whole-corpus scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/ruff check src scripts tests | passed | True | traitmech:000715 | Actual maintained gate passed. Corpus diagnostics are not whole-corpus scientific review. |
| just audit-proposals | passed | True | traitmech:000715 | Actual maintained gate passed. Corpus diagnostics are not whole-corpus scientific review. |
| just ground-predicates | passed | True | traitmech:000715 | Actual maintained gate passed. Corpus diagnostics are not whole-corpus scientific review. |
| just ground-nodes | passed | True | traitmech:000715 | Actual maintained gate passed. Corpus diagnostics are not whole-corpus scientific review. |
| just audit-graphs | passed | True | traitmech:000715 | Actual maintained gate passed. Corpus diagnostics are not whole-corpus scientific review. |
| just audit-graph-protein-taxa | passed | True | traitmech:000715 | Actual maintained gate passed. Corpus diagnostics are not whole-corpus scientific review. |
| just audit-predicate-domains | passed | True | traitmech:000715 | Actual maintained gate passed. Corpus diagnostics are not whole-corpus scientific review. |
| just check-biolink-coverage | passed | True | traitmech:000715 | Actual maintained gate passed. Corpus diagnostics are not whole-corpus scientific review. |
| just audit-snippets | passed | True | traitmech:000715 | Actual maintained gate passed. Corpus diagnostics are not whole-corpus scientific review. |
| just gen-discussions-data | passed | True | traitmech:000715 | Actual maintained gate passed. Corpus diagnostics are not whole-corpus scientific review. |
| just gen-qc-dashboard | passed | True | traitmech:000715 | Actual maintained gate passed. Corpus diagnostics are not whole-corpus scientific review. |
| just gen-pages | passed | True | traitmech:000715 | Actual maintained gate passed. Corpus diagnostics are not whole-corpus scientific review. |
| just gen-priority-dashboard | passed | True | traitmech:000715 | Actual maintained gate passed. Corpus diagnostics are not whole-corpus scientific review. |
| just qc | passed | True | traitmech:000715 | Actual maintained gate passed. Corpus diagnostics are not whole-corpus scientific review. |
| just validate-history | passed | True | traitmech:000715 | Actual maintained gate passed. Corpus diagnostics are not whole-corpus scientific review. |
| just validate-products | passed | True | traitmech:000715 | Actual maintained gate passed. Corpus diagnostics are not whole-corpus scientific review. |
| just verify-proposal metpo_traitmech_v591 | passed | True | traitmech:000715 | Actual maintained gate passed. Corpus diagnostics are not whole-corpus scientific review. |
| just robot-validate-proposal metpo_traitmech_v591 | passed | True | traitmech:000715 | Actual maintained gate passed. Corpus diagnostics are not whole-corpus scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/audit_canonical_examples.py --no-resolve | passed | True | traitmech:000715 | Actual maintained gate passed. Corpus diagnostics are not whole-corpus scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/run_trait_graph_audit.py --verify | passed | True | traitmech:000715 | Actual maintained gate passed. Corpus diagnostics are not whole-corpus scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/audit_history_records.py --base 496e026915723362abc58c3ab721d99548f0f784 | passed | True | traitmech:000715 | Actual maintained gate passed. Corpus diagnostics are not whole-corpus scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python -m pytest -q --junitxml=/tmp/traitmech-trail-memory-checks-20261013/pytest.xml | passed | True | traitmech:000715 | 4379 tests passed without skips, failures or errors. |
| native-snippets | passed | True | traitmech:000715 | Native resolver completed: two NOT_IN_ABSTRACT and one UNRESOLVED. All three direct PDF spans separately match. The 2017 exact DOI has Crossref/PDF identity and a zero-hit qualified MED query, not a global nonindexing claim. |
| browser | passed | True | traitmech:000715 | 1440/390 px: three excerpts, three discussions, one history link, local-ID provenance, hierarchy and browse navigation, dashboard 1110 and coverage image. Eight screenshots inspected; no horizontal overflow or page errors. |
| preservation | passed | True | traitmech:000715 | All 1109 prior trait YAMLs, prior history/reviews/proposals/embeddings/templates remain byte-identical. Existing pages change only footers except the phenotype child link; only its priority child count changes. |
| rdf | passed | True | traitmech:000715 | Parsed class, merged and reasoned RDF preserves exact identity and definition, w3id METPO IRIs, phenotype parent and quality grandparent; no legacy METPO stub. |

## Scientific And Domain Assessments

### External trace-guided exploration

identity: supported. Targets: traitmech:000715.

The label and definition bound information persisting in extracellular trails, not all memory, a secreted molecule, literal sequence feature or a single maze observation. Related memory classes concern distinct endpoints.

### Context-dependent experimental support

evidence: supported. Targets: traitmech:000715.

Coatings mask new spatial information but also change substrate conditions; they do not abolish secretion or lesion internal memory. Same-stock trails do not establish individual self-recognition. Success proportions and conditional completion times remain distinct, and no benefit is required in every maze.

### Observed behavior versus model mechanism

evidence: supported. Targets: traitmech:000715.

The 2024 result is the authors own trajectory observation, not merely cited background. Simulated forgetting is not a measured trail half-life or internal-memory duration; median size groups are not universal biological thresholds. No receptor-resolved graph is invented.

### Three contiguous source spans and source discrepancies

provenance: supported. Targets: traitmech:000715.

All excerpts match directly inspected PDF text and actual pages. The 2017 scientific abstract interprets maze performance, not measured fitness. Two NOT_IN_ABSTRACT and one UNRESOLVED native outcomes remain separate. Printed statistical and group-size discrepancies are retained; later arXiv wording does not silently correct the earlier PDF.

### Conservative parent and historical identity

grounding: supported. Targets: traitmech:000715.

Phenotype is strictly broader; no universal chemotaxis mechanism is imposed. Deprecated adaptation and chemotaxis IDs remain unresolved historical context, not revived identifiers or exact xrefs.

### Guarded writes, proposal and derived products

consistency: supported. Targets: traitmech:000715.

Dry run, fail-closed preimages, prevalidation, replay, full tests, QC, ROBOT RDF and responsive browse/navigation checks pass. The single 11-column proposal retains required blank cells. Existing records, histories, reviews, proposals and baselines are preserved.

### Explicit remaining research gaps

completeness: unknown. Targets: traitmech:000715.

Natural culture provenance, historical scopes, current corrected versions, unread supplements, source discrepancies and common molecular sensing remain unresolved. These are not obscured by examples, mappings, universal claims or REVIEWED status.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| source-0 | DOI:10.1073/pnas.1215037109; Results, first paragraph, printed page 17490 / PDF page 1 | supports | Reid et al. 2012, PMID:23045640, PMC3491460; Results opening paragraph, printed page 17490 / PDF page 1. Cultured Physarum polycephalum avoided previously deposited slime in a Y maze. Same-stock coatings do not demonstrate individual recognition of one's own trace. In the separate U-trap experiment, 23/24 plasmodia on blank agar versus 8/24 on slime-coated agar reached the target within 120 hours. Coating masks newly informative trails; it does not abolish secretion or lesion internal memory. Success, completion time among successful trials, speed, path length and revisitation are distinct endpoints. No-trap and speed controls do not exclude every environmental confound. Main Methods, Results, Discussion and all four figures were inspected in an author-hosted publisher-formatted PDF bearing a 2012 download stamp, not verified as the current corrected VoR. Supplements and raw data were not assessed. Southern Biological Supplies culture provenance remains unresolved. The contiguous result span was text-matched and visually checked. |
| source-1 | DOI:10.1088/1361-6463/aa87df; Scientific abstract, printed page 1 / PDF page 2 | supports | Smith-Ferguson et al. 2017; scientific abstract, printed page 1 / PDF page 2. This is the authors' interpretation of maze performance, not a measured fitness or natural-selection endpoint. Within 72 hours, blank versus extracellular-slime conditions yielded success in 24/24 versus 9/24 open trials, 12/15 versus 4/12 simple-maze trials and 11/17 versus 11/13 complex-maze trials; the last comparison showed no significant benefit. Completion times conditional on success were not significantly different. Escaped trials were excluded; split decisions used the dominant front. Printed page 6 pairs the same chi-square 0.802 with P=0.004 and P=0.371; this discrepancy is unresolved. Figure 8 is illustrative, not quantified trajectory evidence. Main Methods, Results, Discussion, Conclusion and all eight figures were inspected; supplements were not. The author-hosted PDF bears a 2017 download stamp, not verified current VoR equivalence. This study shares authors with Reid 2012, not an independent-laboratory replication. |
| source-2 | DOI:10.1073/pnas.2312611121; Results / Quantifying Run-and-Tumble and Self-Avoiding Behavior, page 3 | supports | Troger et al. 2024, PMID:38517977, PMC10990088; Results, Quantifying Run-and-Tumble and Self-Avoiding Behavior, page 3. The authors report their own Physarum observations, not only a background citation. Actual trajectories, including Figure 2A, are distinct from simulated-model panels. Page 5 describes 14 trajectories divided into groups of nine each; Figure 4 instead gives seven small and seven large. The discrepancy remains unresolved. The 0.65 square-millimeter median is a cohort split, not a universal threshold. Small plasmodia can cross trails; a modeled three-hour forgetting time is not a measured chemical half-life or internal-memory duration. Main text, Methods and all four main figures were inspected in the author-hosted publisher-formatted PDF with a March 2024 download stamp, not verified current corrected VoR equivalence. Publisher supplements and raw data were not reanalyzed. This different laboratory's assay is not a replication of the earlier maze experiments; no universal molecular receptor is established. |
| content | data/traits/physiology/extracellular_trail_based_spatial_memory.yaml; Entire maintained record, guarded writer/tests, proposal, sidecar and generated change set. | supports | One qualified physiological CLASS. Three primary DOI excerpts support external trace-guided exploration without canonical taxa, universal avoidance, internal recall, protein examples, graph edges or exact synonyms. |
| novelty | research/traits/physiology/extracellular_trail_based_spatial_memory-source-verification.json; Pre-creation local/remote novelty, semantic adjudication and RDF receipts; fresh publication audit. | supports | Ignored/hidden current files and retained tracked history were searched. Neighboring memory endpoints, autotropism, predation and membrane exchange are not exact. All 458 current CommunityMech community records were checked separately from isolate files. No exact active record or unresolved exact node requiring migration was identified in the bounded scope. |
| ontology | data/raw/metpo.owl; Active phenotype parent; deprecated 0000248, 000249, 1000004 and 1000062; current upstream main and open METPO issue 521. | supports | The active phenotype parent is broader. Deprecated adaptation/chemotaxis neighbors have no inspected replacement or consider annotations. Reason codes are provisional and original scope unresolved, not proof of invalid biology or exact identity. Pinned ontology remains unchanged. |
| products | reports/proposal_citation_audit.tsv; Native gates, generator pin, byte preservation, parsed RDF and browser observations. | supports | One trait and v591 class row added. All prior records, including protected spore germination, remain unchanged. Parsed RDF graph cardinalities: {'classes': 15, 'merged': 12628, 'reasoned': 12632}. Generator source has 645 checked blobs. Exact configured embedding sources absent; prior embeddings retained. Only required ROBOT trailing tabs use the inspected path-specific whitespace exception. |
| history | history/records/extracellular_trail_based_spatial_memory/2026-10-13T064512Z-codex-64c936.yaml; CREATE event, identity/evidence/discussions; actual codex/gpt-5/codex actor. | supports | One append-only history reflects written sections. Record event uses observed 06:32:45Z post-audit confirmation, explicitly not predicted write time. No REVIEWED status promotion. |
| publication | https://github.com/CultureBotAI/TraitMech/commit/d2f20fbc560bbffee0e50a1194261202fbd13715; /tmp/traitmech-trail-memory-publication-20261013/assessment.json | supports | Fresh publication audit: 828 nonremoved pending blobs, 129 selected upstream blobs, 10121 intervals and 58 explicit dispositions. No conflicting reservation remained. Numeric embedding/gmelin hits and editor envelopes are not competing IDs. |

## Limits And Additional Notes

- Author self-review. Exact-head external review and CI are separate publication gates, not yet covered by this local assessment.
- The primary evidence concerns cultured Physarum. The first two papers share authors; the third uses a different assay, not same-assay replication. No raw-data or simulation reanalysis.
- Author-hosted publisher-formatted copies are not verified current corrected VoRs. Publisher SI and other unread supplement assets remain gaps; bounded metadata and access failures do not prove notice absence.
- Original deprecated scopes remain unresolved. Independent positive acceptance does not establish historical equivalence or nonequivalence.
- Ignored/hidden current files were included, but unavailable historical ignored/untracked bytes, arbitrary archives, symlink directories and unchanged pending-tree files are not reconstructed. Discovery is not exhausted.
- Embedding inputs are absent at exact configured locations, so embeddings were preserved rather than regenerated. Existing frozen audit baselines are unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T070924Z-extracellular-trail-memory
kind: record
repository: CultureBotAI/TraitMech
title: Adversarial review of extracellular-trail-based spatial memory
started_at: '2026-10-13T06:53:53Z'
finished_at: '2026-10-13T07:09:24Z'
reviewer:
  identity: codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Source-based author adversarial assessment, not independent
    review or human sign-off.
skill: .claude/skills/add-trait/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The qualified microbial phenotype is supported at the external spatial trace
  level. Source versions, assay controls, claim-bearing spans, semantic neighbors,
  historical identifiers, allocation and generated products were challenged. No actionable
  defect was identified in scope; three discussions stay OPEN and mapping remains
  PROPOSED.
source:
  git_revision: d2f20fbc560bbffee0e50a1194261202fbd13715
  state: working_tree
  inputs:
  - path: .claude/skills/add-trait/SKILL.md
    sha256: a92f9d331d33a4a74147d834d38393b64edb97e6f2d1a157570ca201c0531dfa
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
    sha256: 4119f52c15e920cd0a1062c22b9bcb8e4effbe2ffd18113145c27e2892fc31cc
    role: context
  - path: app/dashboard/priority.html
    sha256: 3e8c88d4a4659ee8f434e6b6b2745d05ffc9169f87f60bdb025d8f34ef545692
    role: context
  - path: app/dashboard/priority.json
    sha256: ad34676e14ffae6582d25c621a8cee91343bda5b8e6620b2433ad74e30d82860
    role: context
  - path: app/discussions/data.js
    sha256: 8d8ef30429ea899c2b7c94bdaf55a9ec7ded99c8ab1fb63f32d011546806a9ca
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
    sha256: 0ce7c19142b9a0a124bee3a8d0a72cad72a405420c351dcfb1e0c33f7d97478e
    role: context
  - path: dashboard/index.html
    sha256: 90d0ca0ec03cea8a2b19026bc8b285dc9e4e5ac3ad6e9ed7bb3333de1a358a0d
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
    role: target
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
  - path: history/records/extracellular_trail_based_spatial_memory/2026-10-13T064512Z-codex-64c936.yaml
    sha256: 48a433d49659a32e3bfc02672a050d6ade947d8d24b8e2b8d55fc17d3125b476
    role: context
  - path: justfile
    sha256: e6047ea612115a6a78d100b281483ba824c860c3def59bcd0d40e7fb56b3526a
    role: context
  - path: pages/browse.html
    sha256: 02762d486e6ffa3fde83653e13ad16b5ae9726caea61553f400f4c39f4f49f62
    role: context
  - path: pages/category/ecology.html
    sha256: 4d1d97ca6544bbca2a4a4311901917624f35bf5163bc8e95705442605f500fe5
    role: context
  - path: pages/category/environment.html
    sha256: 2a67ba854064d1aef92c350347cbeb674b8196d97c28342d7c75f60e33c8e6e8
    role: context
  - path: pages/category/genomics.html
    sha256: 68d414841e2027713958089b5500067e7165b4c8c466e3a2613a4986f02dfc4c
    role: context
  - path: pages/category/metabolism.html
    sha256: 749a1a938303c285c50fd737e000d789fcd3555588efa5f0150bbdefb1ee7467
    role: context
  - path: pages/category/morphology.html
    sha256: 5e949936a4ba520738b7f3fd8d540dec1425bea4a6a9513b562d375130eb48a8
    role: context
  - path: pages/category/observation.html
    sha256: 2dc75261d7ffac46aca9e7a67345a278b0cc2e177223024bf46c248d464efeef
    role: context
  - path: pages/category/other.html
    sha256: 4e2470771ad2c34f371c149f124312e04e02d1c23e16b27a86b4971c5eb4e63f
    role: context
  - path: pages/category/physiology.html
    sha256: d6871f73f876bdd994328a1871c1ad50f2d1d70461b302286d024414fe9c11ac
    role: context
  - path: pages/category/quantitative_property.html
    sha256: 5f175c7566a3aa36d907b916c512130fc80e990bf088bf02ddb5cac651eb3e7f
    role: context
  - path: pages/category/upper.html
    sha256: 37cbea46c92aa44eb743aa8ded3abfc3f30b09d42c0ed9fd3fe12ae4213631cf
    role: context
  - path: pages/graph.html
    sha256: b1c912410f4f24a1cf07b7de32f557b03b548d1e6b50b747448993afdced6f73
    role: context
  - path: pages/index.html
    sha256: aa9611b6b8d1f56c1d5b13cb9b16b325bc6e81271b7a75496d07ea9e554842d3
    role: context
  - path: pages/traits/ecology/animal_pathogen.html
    sha256: eae7acac7f7f8c8816c83906838b09af8813394caa0a37dd53beeac35840cbff
    role: context
  - path: pages/traits/ecology/bacterial_cannibalism.html
    sha256: 2d38ecc4416933380e1c479ecb75bca341b29e9cfff17fbeff454bb668aa5731
    role: context
  - path: pages/traits/ecology/bacterial_mycophagy.html
    sha256: 23d5de51d3fc4261e469771f0b811ec40b827a5f9eac18e15a6d5656dddc328c
    role: context
  - path: pages/traits/ecology/biofilm_formation.html
    sha256: 1578c67020789e363334eb23aa7db874d7f3a8fc68de71711354f06f440da09e
    role: context
  - path: pages/traits/ecology/biosafety_level.html
    sha256: 3b8a0a346c0d9b5a3b0e6872c334cc78df3e4299fc268230015de46de5df599a
    role: context
  - path: pages/traits/ecology/biosafety_level_1.html
    sha256: 993de9cc7a687082ac4173532a745e6f14de10f41db7ff6611947dbe30dc66b3
    role: context
  - path: pages/traits/ecology/biosafety_level_2.html
    sha256: 0a01fa7ecd33dae83cabd10ac0bc25ec667032bff0a3f3a761458b671776228e
    role: context
  - path: pages/traits/ecology/biosafety_level_3.html
    sha256: 04ac5247caa8bf61952619e7d2d202a590d7cfbd5effaa8bd201bc72ce8d6554
    role: context
  - path: pages/traits/ecology/biosafety_level_4.html
    sha256: f445ba6416ba32dc8a9a4892df53f3ac53480bd88fab872dbeb959e29eeb69dc
    role: context
  - path: pages/traits/ecology/biosafety_level_5.html
    sha256: ce0439dc8189d85808bb0530329e447ed22d3032025ed76b28265e3b7b38385d
    role: context
  - path: pages/traits/ecology/collective_bacterial_predation.html
    sha256: fd287e2d4b28dff80627b3a7d2a08152405cbb4842bfd3be05e941e227033e9c
    role: context
  - path: pages/traits/ecology/commensalism.html
    sha256: 04a3cf966464b996c43fbe02b15946189453490ffa0aa2f04ab258f8714a61c0
    role: context
  - path: pages/traits/ecology/cytoplasmic_bacterial_predation.html
    sha256: 23eb49c9eeb01ca98e0867bb0a295976a09c5673d9281888b9dbf63908d5b261
    role: context
  - path: pages/traits/ecology/endophytic.html
    sha256: 590581ca9da4d5e57f04fa4f1afc557245f986ec8bafe658d7fb2b239f961591
    role: context
  - path: pages/traits/ecology/endosymbiosis.html
    sha256: 7ebe4a012aff6cc98bfa686d1b7690001e5d953f19e2463d93cc7a6384713f81
    role: context
  - path: pages/traits/ecology/epibiotic_bacterial_predation.html
    sha256: 88fe625172b9e33669e88fe2139e8d16e77361a43197cf5c0dc6e311b8d4d038
    role: context
  - path: pages/traits/ecology/epiphytic.html
    sha256: 4712a4d8df154ebcd339a14279e9aa3798679824db155306b86d4a0c42243794
    role: context
  - path: pages/traits/ecology/free_living.html
    sha256: 68251116ba52bb36d7ab3b72dcac307d56482eef17e3ea01d5bfd52fe98adbfb
    role: context
  - path: pages/traits/ecology/gut_associated.html
    sha256: 51cb774509dd7e612c9102536f6ac3f468e97d09234655cce3789007a1511b80
    role: context
  - path: pages/traits/ecology/habitat_association.html
    sha256: 650d3973f640f809ec7c6e192842f708bdb4e9ecb5345e741df5dc13fa510675
    role: context
  - path: pages/traits/ecology/host_associated.html
    sha256: 32f7ea1af95233648456b1efa5523a4edc26c3160732ab8cca01b21e750aa9fd
    role: context
  - path: pages/traits/ecology/human_pathogen.html
    sha256: ae80248930bacc14b5dc948ea9987e7311d4ac0cb3f9aa4654ba745e1cdb5bb4
    role: context
  - path: pages/traits/ecology/ixotrophy.html
    sha256: c3c87f65b92023478a6c83f74dd52769d4567fea6f09abd68b2586ef4934a80d
    role: context
  - path: pages/traits/ecology/mutualism.html
    sha256: 82168ea2b8b70627ecf803df9a7535a35753099c882e892358c28d3e564e4ef2
    role: context
  - path: pages/traits/ecology/nitrogen_fixing_symbiosis.html
    sha256: deb1c2bd4df58585de5944940e4ae963e6886e9fb4c06f2092b41a73226b576f
    role: context
  - path: pages/traits/ecology/opportunistic_pathogen.html
    sha256: 02ccb150172a7e19765b1775b866c439a3b7e0f26dc8d61a885000c6b112c19b
    role: context
  - path: pages/traits/ecology/parasitism.html
    sha256: e031800b6bbbc057d2f2f8a3a2d44fc7d47ccd2b99c5663a891ba29e0720b525
    role: context
  - path: pages/traits/ecology/pathogenic_to_host.html
    sha256: 43118112cd55ab74305bd36b4887414cb6ec5dd157ab3d8f1944f40ee715b903
    role: context
  - path: pages/traits/ecology/periplasmic_bacterial_predation.html
    sha256: bf2b8a6f6c986cf953f1772fc25cbadaea84abc6a40f1cd16950e99f85ff88ad
    role: context
  - path: pages/traits/ecology/plant_pathogen.html
    sha256: 436c277ce1d09132d9f6880eb2adb1a2f9c0c2c56f91478cdde064f6657cb385
    role: context
  - path: pages/traits/ecology/predatory_bacterium.html
    sha256: 3b09368078dbdb2ecffbe2bafd48d66628d1b36b9ec2ab78850e3c7045467619
    role: context
  - path: pages/traits/ecology/rhizosphere_association.html
    sha256: 9f605fe2522c94949cbd39c90f01d4e2f45a309ed90daa13e1269642485a1f26
    role: context
  - path: pages/traits/ecology/saprotrophy.html
    sha256: b7a40fe79d8dbe20cbf9bbb6cc015dff98781522eaaebc8dfbfc141eceade0b2
    role: context
  - path: pages/traits/ecology/soil_dwelling.html
    sha256: 99a898ba64753cf7aa9f721cfb909fd11792bfb41c4fc08c9aa568db40fa07cd
    role: context
  - path: pages/traits/ecology/symbiosis.html
    sha256: 0af209fc4787badb727293c01269495d8eea030ab5bd1edc618078e3b0d4a755
    role: context
  - path: pages/traits/environment/acidophilic.html
    sha256: addcd93bcd3691e026e3ad9d12d976ae30f67b60f2705656e391fe3094958605
    role: context
  - path: pages/traits/environment/acidotolerant.html
    sha256: 1e216d0b49555ba74d5aafc005d3522fa6052fd3ce1f520748548e27265fa6dc
    role: context
  - path: pages/traits/environment/aerobic.html
    sha256: 7a4bc410c9e80b0ea838656ddb77a30b5144d7fad3b4cb34bbab2c357521203f
    role: context
  - path: pages/traits/environment/aerotolerant.html
    sha256: 6fb93192c4039b73c7c1e7d6d2be1a1fbefd8f28f4d0b2e0da229aa66a75bb32
    role: context
  - path: pages/traits/environment/alkalotolerant.html
    sha256: 073f21cf61d86236785e5f87e2c253be154ec4c05fe5147122214a9147b19d31
    role: context
  - path: pages/traits/environment/alkaphilic.html
    sha256: 8bce12408ca99904d8d0a4b2a7731b1b29be7b7ce573f3b9bb238e0a163cf556
    role: context
  - path: pages/traits/environment/anaerobic.html
    sha256: d35aeb9d4f2cd2507951219f8e281fb853cadb19228d4bd358f21f9f487c56cd
    role: context
  - path: pages/traits/environment/arsenic_tolerant.html
    sha256: 358c148a615995bb36b8f3a46fea1e1826ea97a8188aae8527c39c0e9ee023a6
    role: context
  - path: pages/traits/environment/cadmium_tolerant.html
    sha256: 8d3fce9325503aaaa12ed79e560ba66f8aa637bfe1e235bb4bc475addc812f5d
    role: context
  - path: pages/traits/environment/capnophilic.html
    sha256: 4a23c927621431691440a4d6b3770cbb431129a5727c89330c81575f0c30ac23
    role: context
  - path: pages/traits/environment/cobalt_tolerant.html
    sha256: c9fa6b5f80df5b1b7bec9d0d7978039c243884bd9098b4166851e2df27e7a92e
    role: context
  - path: pages/traits/environment/copper_tolerant.html
    sha256: 2a569405e6d9efbf30b861e413d3ab06eafb42193728687eaf0bdedc98d3fd71
    role: context
  - path: pages/traits/environment/delta_phenotype_with_numerical_limits.html
    sha256: 92081b5885c64157b279e85f28d7bede433f155505e2a9313f3fed523e6f6936
    role: context
  - path: pages/traits/environment/desiccation_tolerant.html
    sha256: fc200498030345920eeb0e96d157011e40c6e877741333bb79f53e679d162336
    role: context
  - path: pages/traits/environment/euryhaline.html
    sha256: 489d977ab8dbc2e7b6e6a0b48226fb13668c3e482a6c928e09621ed7bde70aa5
    role: context
  - path: pages/traits/environment/extreme_hyperthermophilic.html
    sha256: 2a7884db56d4336cd61fff091feaa06d72f5a00aadac2da4da1c5e4b210cf334
    role: context
  - path: pages/traits/environment/extremely_halophilic.html
    sha256: 9a3bdb4a224340f28428c8d78cf9393ecc4a76aac9f907123b8a0bbcd456a462
    role: context
  - path: pages/traits/environment/facultative_oxygen_preference.html
    sha256: db8d243b930db01cdeb4ae222c84e9104e0c51206f0ff1dbf193a4acc52ef41a
    role: context
  - path: pages/traits/environment/facultative_psychrophilic.html
    sha256: f6a29ecc3401358ff10cc40d4b8dfdab0b61e43085f86640635ca12cdefe542a
    role: context
  - path: pages/traits/environment/facultatively_acidophilic.html
    sha256: e2ba6951ac04b899e452e14e0b1b162ebdeba72d13c6e1dbccdf620220d5d59c
    role: context
  - path: pages/traits/environment/facultatively_aerobic.html
    sha256: 559a1cc6ed3f18e97c94918a763fd7c1be0de308279f743b6923ecf4152e2288
    role: context
  - path: pages/traits/environment/facultatively_alkaphilic.html
    sha256: 4acd7ac685eff7e0cdf8b0db1a17b4ecf085572e54756227e0b552f1ed56f5cd
    role: context
  - path: pages/traits/environment/facultatively_anaerobic.html
    sha256: 3b6445beb5af281e1f6a1b8023157b8fca13133d82663f7373df68bba99966dd
    role: context
  - path: pages/traits/environment/growth_range_phenotype_with_numerical_limits.html
    sha256: 435e6aa988f3e622005fa2f3cad1b5db90ea65f3425267d036c6ab063409f88b
    role: context
  - path: pages/traits/environment/haloalkaliphilic.html
    sha256: 45746f880eddc2726a358ff34602115da42fd6570034887e81c563e103b34b31
    role: context
  - path: pages/traits/environment/halophilic.html
    sha256: abe211ba3cd341135e3aafc39dc5ba6c95f53ed56eade741f51cf61e5d45435e
    role: context
  - path: pages/traits/environment/halophily_preference.html
    sha256: 3e550e7bf49df03d5a2ff363a6340b2184656e1ade606b9c44af3045d15ef1a7
    role: context
  - path: pages/traits/environment/halotolerant.html
    sha256: 5386d272a6885dfe919a1b0a7ac30d7ad3bc94cb996643852c3b8bc65519d2e8
    role: context
  - path: pages/traits/environment/hyperthermophilic.html
    sha256: f91b6b400c06c0d42569cbdbd4a6f7ad244ff4eb38dee982854c006023d91f13
    role: context
  - path: pages/traits/environment/ionizing_radiation_tolerant.html
    sha256: 1d1d4fb90eb757715a87d6721b92222c36a9ee0373e1fbbfe15509d0053e2bcc
    role: context
  - path: pages/traits/environment/mercury_tolerant.html
    sha256: 080025d6864c5fe372f4f324467c88f9f342710857650d277280930aafef3951
    role: context
  - path: pages/traits/environment/mesophilic.html
    sha256: b4595eb029a8d4ccd76e5d1c7499fa22997e88a2b4b489d8a43f7c8669b36f5f
    role: context
  - path: pages/traits/environment/metal_tolerant.html
    sha256: dc90391ff7eac9a5a250e7402d6892a9a86045de141a896fd4303128d2c50bde
    role: context
  - path: pages/traits/environment/microaerophilic.html
    sha256: e2a1dbffe81b7542e476ff91f5d715d19a1e50e59a0a72120ff3534b854e1f8a
    role: context
  - path: pages/traits/environment/microaerotolerant.html
    sha256: 6526b68d26365c846bcc087428727eeacdeab996bcc1eb8a3ff3dbce4dd09137
    role: context
  - path: pages/traits/environment/moderately_halophilic.html
    sha256: 5ce92547d520a75d9f492f8554fe1213cbd025995656b856eebaa8bfd4eba745
    role: context
  - path: pages/traits/environment/nacl_delta.html
    sha256: e1d2ec30e90b3326459ac0330df37c444144376e1c0a8412827406783192a11a
    role: context
  - path: pages/traits/environment/nacl_delta_high.html
    sha256: 1ab27dcffb8d146eb630a9c834d2f9a5e61cd219a6ba985da66ec183c6fcd41c
    role: context
  - path: pages/traits/environment/nacl_delta_low.html
    sha256: 4c05879883e3bd92cd1540175e28d58ab51a587181155181c3b358a0985edd18
    role: context
  - path: pages/traits/environment/nacl_delta_mid1.html
    sha256: 3069e1201250a112842133b9b430caea8842ee54fba4624cd52ae3ffd5a0fefd
    role: context
  - path: pages/traits/environment/nacl_delta_mid2.html
    sha256: a483cce493433d3557c69f5630ec59f2fca17965fdd37b75b13d7af09dcd8ee0
    role: context
  - path: pages/traits/environment/nacl_optimum.html
    sha256: 758b77cf2a77da46c267cf3a34613b7f3be677c9ffd52575ba53e0111130c2bf
    role: context
  - path: pages/traits/environment/nacl_optimum_high.html
    sha256: 7188492fbfcefe33efd5255a9df7b2684ef379331ae0f57b5166aa269bb24aa5
    role: context
  - path: pages/traits/environment/nacl_optimum_low.html
    sha256: 15c411317be38af7a218569557971e6d94d2fa523ba1c610c0852266bca5d38c
    role: context
  - path: pages/traits/environment/nacl_optimum_mid1.html
    sha256: a11ed8c98cb8d889e6d40f34814cac38ddd7102aa3100fd1108b7e62dbf9b788
    role: context
  - path: pages/traits/environment/nacl_optimum_mid2.html
    sha256: a12deb01d30ac1084cafc64adf2048f1fb42fd0be4ca32824e1d94421e5d2d27
    role: context
  - path: pages/traits/environment/nacl_range.html
    sha256: 5b1bba81fa58c6ea6032117c8b951d9275166b6d9f9ed736f42e9f2762a03ab5
    role: context
  - path: pages/traits/environment/nacl_range_high.html
    sha256: 4eee5743cc62da49874242bc5078b0123011e29dd69748d4b4a67597d78fd767
    role: context
  - path: pages/traits/environment/nacl_range_low.html
    sha256: b105331246caaf5dba32376606be46b1c5d042a346c46fce4bbb27813325c0e4
    role: context
  - path: pages/traits/environment/nacl_range_mid1.html
    sha256: 9c5207f2dfd74185f5856bab83fc327638455b89e953b9fa529bc235b94ebf37
    role: context
  - path: pages/traits/environment/nacl_range_mid2.html
    sha256: 3b2d425df8740e562ca0405d60f307b05a3d1e583bf4719eee34d3b908757821
    role: context
  - path: pages/traits/environment/neutrophilic.html
    sha256: 03fe5b041bfc202305ecd2552fffe4d98b8123fc3685012e9ba029a75d3818f4
    role: context
  - path: pages/traits/environment/non_halophilic.html
    sha256: 663af13d29fd67ae0fc41abd616ac5e460d8ee87eb45ee662e4afa0fd95c2de3
    role: context
  - path: pages/traits/environment/obligately_acidophilic.html
    sha256: 3d5800406e6ab2a082cdbdf250971b55a798f0865abf0e3b86f1391695a4a1e6
    role: context
  - path: pages/traits/environment/obligately_aerobic.html
    sha256: d8fd19c54592797948b6545772277a58526b20b5725bb6ee355d557cc996583e
    role: context
  - path: pages/traits/environment/obligately_alkaphilic.html
    sha256: 5466f10dd6d5cb7993bd34111651a60a3b4c8e4de3aa36e94cb9873fc1b0db9e
    role: context
  - path: pages/traits/environment/obligately_anaerobic.html
    sha256: 25b47a64a277390feb2292c70776511de775a07be26dfdfece379187fa184f6e
    role: context
  - path: pages/traits/environment/obligately_piezophilic.html
    sha256: 9192dca3f593502b24d393ee92cfa29fb142f253463a1f47ae3cc8370472f742
    role: context
  - path: pages/traits/environment/optimum_phenotype_with_numerical_limits.html
    sha256: d589283d10a433fa31b8bb2788b738a7117ce97f4f919554c7cf4902c35c66b9
    role: context
  - path: pages/traits/environment/oxygen_preference.html
    sha256: 02e64a5baf33ad982e45277239eb4b9f8cf620162182eea0e2630fd34e05e774
    role: context
  - path: pages/traits/environment/ph_delta.html
    sha256: bc1f932807ff53d4ffe6638c501ad723a93095bd20c73cd5fb2ff593c1fb8472
    role: context
  - path: pages/traits/environment/ph_delta_high.html
    sha256: 0d01da77a01fdaefc3c9559218a6837196ad479f5d44feeb732193eba43fc8e3
    role: context
  - path: pages/traits/environment/ph_delta_low.html
    sha256: 24a88dca1b96f7e8eb201655f1b26439a6e4631a520a05b240f345409dfddfca
    role: context
  - path: pages/traits/environment/ph_delta_mid1.html
    sha256: 6248f5920cbf1b4582f0e09c671441cdee4e98b3f7322d8a34b0e4c18cff5e0b
    role: context
  - path: pages/traits/environment/ph_delta_mid2.html
    sha256: 092c7967b8f4e3cb4e45d30e2c525d3006d1067b07591328fe08813ae5d033c2
    role: context
  - path: pages/traits/environment/ph_delta_mid3.html
    sha256: fd6ca5409ee3753efb6379ea9bff7b4030e01e6b6e839bc18732761d06c6d4a3
    role: context
  - path: pages/traits/environment/ph_delta_very_low.html
    sha256: 2a60b35bbdd3b679421d0a44cba1f6e5dc82184b01f99c5d127d401f77d0952f
    role: context
  - path: pages/traits/environment/ph_growth_preference.html
    sha256: 35cbb092a2b668af7f1c7af3eabc40831f75bb8104c916edf9480b78d4c792bf
    role: context
  - path: pages/traits/environment/ph_optimum.html
    sha256: 08a837387a21f1f8b2bd6f0e88b7f94a5d3253f70feb5052be65070aaa54e58c
    role: context
  - path: pages/traits/environment/ph_optimum_high.html
    sha256: 432c0cd48a6de164021746a49a06fc29a25b3cbca55f84d231f2fd4e7b457451
    role: context
  - path: pages/traits/environment/ph_optimum_low.html
    sha256: cfb0046402d5b723b9a29753550e548695032b389dc28c1db282b4ad58abd8ef
    role: context
  - path: pages/traits/environment/ph_optimum_mid1.html
    sha256: 2200c3ad2f8ea8b5eef4b9c05c96bc5faa5731d9aaadb7dfdef57904f58e4b66
    role: context
  - path: pages/traits/environment/ph_optimum_mid2.html
    sha256: d42599e73ab1e731d253d0052a2f6ebd6f5bdce574921ffc9dbb3ac2e3ac3858
    role: context
  - path: pages/traits/environment/ph_phenotype_with_numerical_limits.html
    sha256: 0811e3398b48d8d9dd9f7558c2a2b17a49d3b21d2e212aed5a087e868ffafea9
    role: context
  - path: pages/traits/environment/ph_range.html
    sha256: f774686d51c9812ac728e4546598dfbb271193fb47b93f4b1ebfa586bd44c6c2
    role: context
  - path: pages/traits/environment/ph_range_high.html
    sha256: 1caca3f3f27cd3114fcb79bf3d726a239d18259d81d13fc24ab320cff2463c6d
    role: context
  - path: pages/traits/environment/ph_range_low.html
    sha256: 48e6a8eea287f7c6500de619af384f1e96fb3a71cfa5549711f950ceab337399
    role: context
  - path: pages/traits/environment/ph_range_mid1.html
    sha256: 8d7d16cd3c8f5436d7fde502cf8507a4357c56de25a3b40be82ace6d9e09a997
    role: context
  - path: pages/traits/environment/ph_range_mid2.html
    sha256: 7c36adc711762cf78d4b7c6362f2a53ea6911b37697802439f3c3e59c909ce70
    role: context
  - path: pages/traits/environment/ph_range_mid3.html
    sha256: 88a8e1ac91646eae798670fe462ed4ed5c8186885a5bab1a66aa11f3dd1feefc
    role: context
  - path: pages/traits/environment/ph_range_very_low.html
    sha256: 7ce876250bd521877918c6770beeaf2eec9a32c00934072d5e8e8d083181df02
    role: context
  - path: pages/traits/environment/piezophilic.html
    sha256: 183705404bb152343bbadff5c9b5be4d77561c01ef8b63a3e5fdee775ba60066
    role: context
  - path: pages/traits/environment/piezotolerant.html
    sha256: 4df3067cf142f5ce804e6898c87c5859492ef6e2d7a155f2a78b3f62267af2b2
    role: context
  - path: pages/traits/environment/pressure_delta.html
    sha256: 661c8fb317a047cdbade9e05b7af9a40abb7e741ad26b7bb3626d451bafcdf39
    role: context
  - path: pages/traits/environment/pressure_optimum.html
    sha256: bd706591f7943f33faae7f7f810264e55bef66ffdcd6c9a0e9c4cc22395fe4c7
    role: context
  - path: pages/traits/environment/pressure_range.html
    sha256: f086caae7843d7b50ef84459aa52bf549cd77bc33354c938d68770771f56d33c
    role: context
  - path: pages/traits/environment/psychrophilic.html
    sha256: 2c8ea41cae2ae7f1dfcf480853baafc7a0529d5dccb7ab63da0a28482ed623a2
    role: context
  - path: pages/traits/environment/psychrotolerant.html
    sha256: 21ee1bd188300025c4086648da25f84e4795ab0fb744a313cbe0476c3934e7ac
    role: context
  - path: pages/traits/environment/radiotolerant.html
    sha256: bbde96d0db26b6191c403a765bad1391dc4d35938f16e75c3a8b896f00108347
    role: context
  - path: pages/traits/environment/salinity_phenotype_with_numerical_limits.html
    sha256: 0dad8f95e0b506c3750b4b621561ff73fc6a5dec8579612a3efb85b2f3c493dc
    role: context
  - path: pages/traits/environment/slightly_halophilic.html
    sha256: 3bb60ef7b9129c96a50dd36662cbecff61e38c836defdba4c26c8071c4b7dc4b
    role: context
  - path: pages/traits/environment/stenohaline.html
    sha256: d641cd12909d3d7fabcde692d0b6db31eb876148afb0c6f2f8de1098291a89f6
    role: context
  - path: pages/traits/environment/strictly_anaerobic.html
    sha256: 8df50e869edffc659a7c4e6a344276273d7cc3ec483e96632fc130e821996625
    role: context
  - path: pages/traits/environment/temperature_delta.html
    sha256: d97d3c4c20310c9f19cf40d73c06c1c3f359c54078823468e413009918cbdb21
    role: context
  - path: pages/traits/environment/temperature_delta_high.html
    sha256: df2c38a2be3f7386731be2e0f3465d9c5e5163c1d63a6a9b9c14247706a5cf56
    role: context
  - path: pages/traits/environment/temperature_delta_low.html
    sha256: af88143587c4fc83c21bf64e0ea6b173881a01b17cbe3c0005832d926cbea7cd
    role: context
  - path: pages/traits/environment/temperature_delta_mid1.html
    sha256: 9ab78a9d6528c2f5925b09e125a6fd2445698a692b98e9dc0c8949f7dadf02cb
    role: context
  - path: pages/traits/environment/temperature_delta_mid2.html
    sha256: 8b4af86f55416a7f3a034d91316f13bd74c5db29daf483e960556340f960af66
    role: context
  - path: pages/traits/environment/temperature_delta_very_low.html
    sha256: ddb75f119792fa2afafcacf782fe1476f8375421016f362f588b9920905bcfc1
    role: context
  - path: pages/traits/environment/temperature_optimum.html
    sha256: 53ba03e821953f590926e07072388e08a4478ed5fbecb4b05823cba3713bc72a
    role: context
  - path: pages/traits/environment/temperature_optimum_high.html
    sha256: 4e115e9e48e7a6daefcbcb5298318d988380e4c20a8f646590070b33b9853384
    role: context
  - path: pages/traits/environment/temperature_optimum_low.html
    sha256: 7975a8fada10b8f5014df24356d14fb57a92d3001b6ef187c32b5f74e2c4765d
    role: context
  - path: pages/traits/environment/temperature_optimum_mid1.html
    sha256: 002b52ccfb1bfc65e951b98317d5066c2d6911a79d5586aacc2c9494ea73b8e5
    role: context
  - path: pages/traits/environment/temperature_optimum_mid2.html
    sha256: fb2478db7898af1db70c562d8e2033d8d171f085b6e2f3c6a62a4d24cecd8693
    role: context
  - path: pages/traits/environment/temperature_optimum_mid3.html
    sha256: a3424e696869eb77a4d40a6b2a615e333f053572cdc783301970bb1a090230d5
    role: context
  - path: pages/traits/environment/temperature_optimum_mid4.html
    sha256: 45876ea7d3f33613e495301be1b6d8742207622ee98c05d78fdb947448f4789b
    role: context
  - path: pages/traits/environment/temperature_optimum_very_low.html
    sha256: 6e72fa7ce1f06a1316cd7b7e26598c7af3785bc2890c03e795d0c3975f53e80f
    role: context
  - path: pages/traits/environment/temperature_phenotype_with_numerical_limits.html
    sha256: 44505c52d6b81cb94dca5b039db8dc742d36de261edea90d333874fe06e9439a
    role: context
  - path: pages/traits/environment/temperature_preference.html
    sha256: 6c0ad0d7c009d96c523ac358ec2dbbe70307c1c85fb1bc0619f9631446cbb53e
    role: context
  - path: pages/traits/environment/temperature_range.html
    sha256: 15109cbe12ed3aed19e77bc694b83b58a3ca782854b6fb142f3777aed1735292
    role: context
  - path: pages/traits/environment/temperature_range_high.html
    sha256: 5b82e6c49cdd5deb290c2a88a3ca73e1aa80d755cd5878f35a7bffc8cbd9fa6e
    role: context
  - path: pages/traits/environment/temperature_range_low.html
    sha256: 89a7545e781fe53eaf411c6c2b2c609f56157227761ae5514c7532a7c18cf626
    role: context
  - path: pages/traits/environment/temperature_range_mid1.html
    sha256: 05c3574f720bfd6632f2707a8b24d475949e02e344b76d1a55ec0383f4e77d98
    role: context
  - path: pages/traits/environment/temperature_range_mid2.html
    sha256: 3f094b337566716fe1d18717bc9fdfa140c752f094630d599242917acbcc1943
    role: context
  - path: pages/traits/environment/temperature_range_mid3.html
    sha256: f5538f2263cb0077ca7c454282af59a134ab205563dd9e8378391624abe0706c
    role: context
  - path: pages/traits/environment/temperature_range_mid4.html
    sha256: f663b3c1a927c9c918a6d095a46356f8e960811c6d2835a481930c27a94c8363
    role: context
  - path: pages/traits/environment/temperature_range_very_low.html
    sha256: 96acd60631723e055955b691f3d4fc7fff2d3d6ceaf7d230c478583733356bc4
    role: context
  - path: pages/traits/environment/thermophilic.html
    sha256: 9900c05208edb2d06b2f6f436e13d13c549a51259e1132ea630a0488e7a58e15
    role: context
  - path: pages/traits/environment/thermotolerant.html
    sha256: 0c033a0eafb1f1750cf05ae9e391835ca98a1046057c1da7a93fdb45be2fb1fb
    role: context
  - path: pages/traits/environment/uv_radiation_tolerant.html
    sha256: 9124b4109d19c16f388a743fb8841da84feb18e4b363ad69a01043a9a659c61b
    role: context
  - path: pages/traits/environment/xerophilic.html
    sha256: 4b3c5a9acca35b138be8b5848de22c69508469eaf5581e03dfe3304a5106bb62
    role: context
  - path: pages/traits/environment/zinc_tolerant.html
    sha256: e8fc6b0f9f48b5b8ae9cf46a811fed7c424162f53648cc6b3294be877185f4e3
    role: context
  - path: pages/traits/genomics/abi2_system.html
    sha256: 3eb5d9d1e35b62000259a45b555eeb680861fdfe489b9b8f67e3562a53bfe0b7
    role: context
  - path: pages/traits/genomics/abia_system.html
    sha256: b76065eb98f833ebed0373ad22d4717eb1d033feaf3684f530f139ff0c53c9dc
    role: context
  - path: pages/traits/genomics/abialpha_system.html
    sha256: cc5de75f3348c696cc9eca6aba74a788a768217ff165936af55842b2173d7886
    role: context
  - path: pages/traits/genomics/abib_system.html
    sha256: 98b6f17546132444b1c2a711c3860a475f6155be5d59ff129776ad00c8c82f8a
    role: context
  - path: pages/traits/genomics/abic_system.html
    sha256: ab32df0e5f48b095984c647bd5d87526baea8816e6cafeb41adc098ee88be53f
    role: context
  - path: pages/traits/genomics/abid_system.html
    sha256: 6ad375e3c11e9a7741970869b5d6f8bc8a304db0c92b3e8b2824d572b52bdfb2
    role: context
  - path: pages/traits/genomics/abie_system.html
    sha256: b99ea29bfbf6efc5718092fc469d11c181f89772557a149498b967c112b66e30
    role: context
  - path: pages/traits/genomics/abif_system.html
    sha256: 997087d82836614c4b956d0a6b241d296f837d09335351099287bada7597142b
    role: context
  - path: pages/traits/genomics/abig_system.html
    sha256: fefccb3d37e54563d8c1e13facdfa6e0e558b6e9d00083e15a3d839fb7a6a185
    role: context
  - path: pages/traits/genomics/abih_system.html
    sha256: d9a473399aae6bf8ab2fb8fce1a30f8eaf5f942bf35f0bcebfd1b054b439230a
    role: context
  - path: pages/traits/genomics/abii_system.html
    sha256: 54722f8666d947b7636c98a727bfbe2ac162b268315726212e033d83f52436b3
    role: context
  - path: pages/traits/genomics/abij_system.html
    sha256: ba3b74a9304f18b626c7a887f4305974b9ecc1a8cb26a03306b61534a790f10c
    role: context
  - path: pages/traits/genomics/abik_system.html
    sha256: ed8336ccdf41b96aca6547d8480ab1f7f4d0608d069d73d91b274fad7e51ffc8
    role: context
  - path: pages/traits/genomics/abil_system.html
    sha256: 090ccb2cd51d46d1b013222a063a1b628883337cbda3f16dc9e21ce4e0296622
    role: context
  - path: pages/traits/genomics/abin_system.html
    sha256: 9fda17ccacee9a25d86dd45a9e92bd210d7aba75c729d2560e317654585f8e83
    role: context
  - path: pages/traits/genomics/abio_system.html
    sha256: 276204d4988ba078ec04f223ca351bc3fd8a2526145086152ff2b3fdfcbf64d4
    role: context
  - path: pages/traits/genomics/abip2_system.html
    sha256: 9ee81905b41e7c3d085329ca42f2a4a2c642f55f6e9f0f323af3eb3ce554a283
    role: context
  - path: pages/traits/genomics/abiq_system.html
    sha256: cf58d28e44d44c12b6a191f822b4136fd6afc31b80171ec9eb67d0cd15f1fa3f
    role: context
  - path: pages/traits/genomics/abir_system.html
    sha256: 4af4a8bb9fe2b3c06a80959461d281cad2991a8f35c1b69c87bf6eb24a78dcea
    role: context
  - path: pages/traits/genomics/abit_system.html
    sha256: 46aeeac977a3e56fb6868a7d4557ac1524a02dc8367031c69e1a6874be224a24
    role: context
  - path: pages/traits/genomics/abiu_system.html
    sha256: 9441da6ed40c74a06638278ad87e57b312972cd30acaa6e18c727a4539ceae89
    role: context
  - path: pages/traits/genomics/abiv_system.html
    sha256: 7772da24353f9ec9873204e02b91da79c64271a9bb5377a8a5f5b77362fc5641
    role: context
  - path: pages/traits/genomics/abiz_system.html
    sha256: 7e864a834901fc6779da9148677729385088c7b3ad0a6545cbb2d49d42bbe5a4
    role: context
  - path: pages/traits/genomics/abortive_infection_system.html
    sha256: 99af299efcdf1082bb594443678971942b13cbf24a8878f63b47a39b5c8f2754
    role: context
  - path: pages/traits/genomics/aditi_system.html
    sha256: 03c027e41f6fe3ad9b3c3c50606f1b11cc6e62ac8177c2fcaae291de9fb86760
    role: context
  - path: pages/traits/genomics/ambrosia_system.html
    sha256: 56b5701a675f9bb2699888d579beb7de0348580645b171e9dfa10d468737ebb8
    role: context
  - path: pages/traits/genomics/apsab_system.html
    sha256: a64eda666efe8e3604a954f46117e8f6fa8d845b57285b90822c514aec2ef9a8
    role: context
  - path: pages/traits/genomics/aristaios_system.html
    sha256: ecb834b472d3121e037df1ec5153504f02af1f3bde8a6c9706ea147b0be8ee27
    role: context
  - path: pages/traits/genomics/armada_system.html
    sha256: 6b4cacf2f7e1d04d1d960d130f491ada47f7c44d5f56bf2d5b4e7c3aa372ed7b
    role: context
  - path: pages/traits/genomics/audmula_system.html
    sha256: 21bbd459be72446f64412b6add2c566b0808eeff4af5a47dca9c00ce774ca960
    role: context
  - path: pages/traits/genomics/avast_system.html
    sha256: 2813032047d59dcc055f24eb15ad3374ea0f950885f34fc94e5e7b0c2e200887
    role: context
  - path: pages/traits/genomics/avs_i_system.html
    sha256: c1966e1a22dc2ec0b0de17c826ddfdccf537e65637e13324d261a78b2f62a774
    role: context
  - path: pages/traits/genomics/avs_ii_system.html
    sha256: 803b70e42b00d67a4aad7e74b78af14f3b06e07f66cef0ecbf222600827936f2
    role: context
  - path: pages/traits/genomics/avs_iii_system.html
    sha256: b713519a038326bf0db5607ecdbb2409b8c4454f029d03252e9971e953d8ba3a
    role: context
  - path: pages/traits/genomics/avs_iv_system.html
    sha256: 39a29272fbc4f6acc2b049dc5480bd1ee3104817269b0a5c903063306420fd54
    role: context
  - path: pages/traits/genomics/avs_v_system.html
    sha256: 13482abe0c424eda82b0f3b695a690d91c2ba25c767d5a79bcd65830287df453
    role: context
  - path: pages/traits/genomics/azaca_system.html
    sha256: ef7b6ea2a16ba98260f1f13e8538a532422a341ede8a1b1d072d1d7ac1002ca9
    role: context
  - path: pages/traits/genomics/belenos_system.html
    sha256: 131f76776f338a7a371eb725933cabf29619f5d9b013c74d2a0a635c378a77c6
    role: context
  - path: pages/traits/genomics/belisama_system.html
    sha256: 354a8f12aa4ded639405fd20f8a937ed3feb3c6e6dd390ff1abf757e425ea7ce
    role: context
  - path: pages/traits/genomics/bil_system.html
    sha256: 21b3dd3cfa2f207f39fee6a880f468750cc2c9449015da2f48e54bde374855e7
    role: context
  - path: pages/traits/genomics/borvo_system.html
    sha256: 7ca6bb7d6758f75e14cb5927aeec62a4ae6cdf9f488c12883b835111f4d8a16b
    role: context
  - path: pages/traits/genomics/brc113_system.html
    sha256: 5a98e2af6b0f363e4940588a5d36e435c2b0ffb27446535d909135d42a0e6815
    role: context
  - path: pages/traits/genomics/brc142_system.html
    sha256: 4da68f5f070cc5da00cabc1a8d5c42cd572f8d31f6b001aadd5c86963c68dcf8
    role: context
  - path: pages/traits/genomics/brc167_system.html
    sha256: c00b91f1cfb16809d66d4123257776c79d3cc377bb546b89728ba1da4dd251f0
    role: context
  - path: pages/traits/genomics/brc217_system.html
    sha256: 96e9dcdfee54aab8b1a46c31cad675a7da8d9fd4f8f71ffc81a5faf77d8ffd65
    role: context
  - path: pages/traits/genomics/brc22_system.html
    sha256: d9b2dbf0c6bfc5a203279c25f87595e880b95b8e7533a7c72a1ed2de41f71337
    role: context
  - path: pages/traits/genomics/brc233_system.html
    sha256: 903eb22316cf55c815a18b34eb4cb484faaa40d6f21f90490501604d6381f039
    role: context
  - path: pages/traits/genomics/brc23_system.html
    sha256: 33ef724a333d0ad0cbf6eb00e1577afb72b611d5bce024f6cf8a1595cedfc1f2
    role: context
  - path: pages/traits/genomics/brc24_system.html
    sha256: 273d8aad82db8ff247b8fd659f377b7463c527ee2d2cb459f51be4f57fe98b2e
    role: context
  - path: pages/traits/genomics/brc59_system.html
    sha256: b09de148efb7d5d33c0652b3ebc806707b0c66cdc789150bc1db8c222448a4a3
    role: context
  - path: pages/traits/genomics/brc76_system.html
    sha256: e59fabd1f83a2d2137200ea1f4dba2c1ef3aafb446e0d08b7f9ffbb61c4881a4
    role: context
  - path: pages/traits/genomics/brcwgs21_system.html
    sha256: 11e3c0db29fa794198ac2a04fa26fc6f9082805a934cac51b80f4af001013790
    role: context
  - path: pages/traits/genomics/brex_system.html
    sha256: acdb13e8cb2d32bc262bf1372d8f78af3f2f4df477f66a972277f87e7fc8b2ed
    role: context
  - path: pages/traits/genomics/brig1_system.html
    sha256: 6755534f27f7d6324a4471d08c6595a0b9a1436c6b339b90c235e0a9cb85a92f
    role: context
  - path: pages/traits/genomics/brigantia_system.html
    sha256: 69e2b0fe91cc32a109e0e08f6bddd0316e79714888f29955e3348ddc8094f7e7
    role: context
  - path: pages/traits/genomics/bsta_system.html
    sha256: 3045cea3d444398a7a9cf4cedac775b71d02a467fbc006f56291f9e202ff3f50
    role: context
  - path: pages/traits/genomics/bunzi_system.html
    sha256: 872040db071c3fa0b751ed0199f9102b9d5ff3f174a19fb2065bf34b4f6dc216
    role: context
  - path: pages/traits/genomics/butters_gp30_gp31_system.html
    sha256: 2e38d65d9990c763eeb0b724ac63e2cb49069bafe2355f8ce7f9634e5a1c5101
    role: context
  - path: pages/traits/genomics/butters_gp57r_system.html
    sha256: ad6d9f96ffa8eea913130b937e777f031278506d1ba13671a897c946508b15b4
    role: context
  - path: pages/traits/genomics/caprel_system.html
    sha256: 06cf87809e68bba4697c27e68ed9786af946ed97176c19b524555f14ecb57b84
    role: context
  - path: pages/traits/genomics/card_nlr_endonuclease_system.html
    sha256: 399f9cb45bfee989f5df9e56760dab24cfa22b8f04a126ab30807a1177307ade
    role: context
  - path: pages/traits/genomics/card_nlr_gasdermin_system.html
    sha256: a0c0230a72eb30fac9b05ddf87d6ae0efd61cb0c6d15419433ca66a003cddb70
    role: context
  - path: pages/traits/genomics/card_nlr_like_system.html
    sha256: b9e399a087e8b92dbb4a3259d08b5192f5ae2478302c5b1f434022ba5a53413d
    role: context
  - path: pages/traits/genomics/card_nlr_phospho_system.html
    sha256: 6260aca0c37839116f21739dfbdd5d9c08bbea36e1bad3fae45a8800d29d4b3c
    role: context
  - path: pages/traits/genomics/card_nlr_subtilase_system.html
    sha256: b9f9df127c0fcadd9768cf351ba91bc8de7ba250f36a99546143543b2390b14b
    role: context
  - path: pages/traits/genomics/card_nlr_system.html
    sha256: b4edd7ae265197ff4214343a8d194b40b52dcd3bef73544fb5afa624bebfb287
    role: context
  - path: pages/traits/genomics/cbass_system.html
    sha256: e84b4437757f726f9f36e4d5bce646de5728eeb3c78f767069c4f98652a390b4
    role: context
  - path: pages/traits/genomics/ceres_system.html
    sha256: 610fd4b05b4739476c27f95dd6777ce630c26f946d1deec52f925c65f1e3f3cf
    role: context
  - path: pages/traits/genomics/cernunnos_system.html
    sha256: f6129dd15f3e0a713e22e1db63379b313573bdcfa69315839d56df84d25f80c1
    role: context
  - path: pages/traits/genomics/charlie_gp32_system.html
    sha256: b2676fb2cfd9fdc6df919cc25a836d688d4e91964bd8b14668fd930ae536d0a5
    role: context
  - path: pages/traits/genomics/clover_system.html
    sha256: ef524cee868e5e8eac8664bfd7556ebef64010ff1abbc2b2dbe7212b1148e50d
    role: context
  - path: pages/traits/genomics/cmdtac_system.html
    sha256: 3ed290adf2d57c420b3b059da6fd29f57fd0c081ef08f69f780cb3156e8e35bb
    role: context
  - path: pages/traits/genomics/coconut_system.html
    sha256: cfcd00f0b6799e71b3f778215a6a91b64725435133e3598a63164494b6935b4b
    role: context
  - path: pages/traits/genomics/codon_usage_bias.html
    sha256: e963aae9d0db7553458676b24ec179683c0df7bf50dc56a3f8ed983dfa3ab7f3
    role: context
  - path: pages/traits/genomics/crispr_cas_system.html
    sha256: 5789a563b11b6f233c1fdaa7eceb05c72b39bcb58cc92bf0546267b4f5cecc5e
    role: context
  - path: pages/traits/genomics/crouga_system.html
    sha256: 55a265bea43780a049de70a9e6983817125232c1f9967dd1a51b35aa23feda0a
    role: context
  - path: pages/traits/genomics/dag_system.html
    sha256: 72de9c7fe0a094a68590b84fc881fa3a0e0772b5ac65937dd634772d8f7ff80c
    role: context
  - path: pages/traits/genomics/damona_system.html
    sha256: 0e885520dad49dcc94cc4e90028b046f89cb0cc7cb235d4596cae597e43dc84c
    role: context
  - path: pages/traits/genomics/darna_system.html
    sha256: 62aea60f1408629e02e336c3df3a7520514e288a93e9203150f8019e5144f207
    role: context
  - path: pages/traits/genomics/dartg_system.html
    sha256: 87c40ddf3593a49c5677b38d19231d9b2b4aba72bf228030727bba1f3d9d1347
    role: context
  - path: pages/traits/genomics/dazbog_system.html
    sha256: 6f48af63188477231ad32bc82dc671f1893bff190232ce4f255cd959ec478e1b
    role: context
  - path: pages/traits/genomics/dctpdeaminase_system.html
    sha256: 073f48de44ea6a138e39c75e0de28f9df1891c79a47295efcaeea82bf82afa08
    role: context
  - path: pages/traits/genomics/ddmde_system.html
    sha256: e4521c20aeb5c47e367c123904cf770ccabf20183c996160e0ea717875982029
    role: context
  - path: pages/traits/genomics/detocs_system.html
    sha256: c3555c71279bd256b633d788d397dd8ca8e2bfcca1b462b40988862ffdb80ee1
    role: context
  - path: pages/traits/genomics/dgtpase_system.html
    sha256: 476cdbef83102ead9cf4336e4364331cb00d34a7abdd1dbabf8cbc4dfa33427f
    role: context
  - path: pages/traits/genomics/dionysus_system.html
    sha256: cfbe96b50b06f802cd9146ec3149f3e683eb3a88844a3484f9aca06d87b4a81f
    role: context
  - path: pages/traits/genomics/disarm1_system.html
    sha256: b897e04306b75e0c8c0b51366e772a4fd56d08751ffc621da4a8de9908301e28
    role: context
  - path: pages/traits/genomics/disarm2_system.html
    sha256: 6e188142cf160c6cf86f26f5cf538de0e7d4328e1bb85cca7698b31dcff396ca
    role: context
  - path: pages/traits/genomics/disarm_system.html
    sha256: ef699c960fff56a396309a0d4678478c5e894f16dbcc88034b0f4938ded9cd4a
    role: context
  - path: pages/traits/genomics/divona_system.html
    sha256: f36c34e71fb68d1ec0994a243f32788554a3552cdabcb3e48e129838557b5eb4
    role: context
  - path: pages/traits/genomics/dnd_system.html
    sha256: 29e15c6cb99227cdee7ade8eebb718d0c9bb6eba5bf9a1d7b40661b98fc8c40e
    role: context
  - path: pages/traits/genomics/dndcdea_pbeabcd_system.html
    sha256: 2e08928c9114f1f5dd25c2011774a2afff2ddf37e6c10b1b43ffd0b5baa3839d
    role: context
  - path: pages/traits/genomics/dodola_system.html
    sha256: 2621457dcdb102ccde72ab217807c825d0dfb130051c3b7302d4c1d1e1eb5ab5
    role: context
  - path: pages/traits/genomics/dpd_system.html
    sha256: 1e92f8d343697921abd209630e361d89a8ff76f23a4322572310193c95a4f299
    role: context
  - path: pages/traits/genomics/drt1_system.html
    sha256: 8b11f7e292ed1dd9b30cf6f8710d35fe08359622e3e5c1cc55e66f03844536d0
    role: context
  - path: pages/traits/genomics/drt2_system.html
    sha256: 9cbc1012ea8904630006fc87396b9e59940161c9b894d181f400c235cfa96fd2
    role: context
  - path: pages/traits/genomics/drt3_system.html
    sha256: f684b23e680b97bb8d7064d1894f412425f3f87c8fd3e89edaa99785d37edc10
    role: context
  - path: pages/traits/genomics/drt4_system.html
    sha256: df43ca1f0ca062ecd2eb420162e11e36cfdf20d3d1228609f39988d31a04b144
    role: context
  - path: pages/traits/genomics/drt5_system.html
    sha256: ff0a3609db2c13c7623c46a8f2afafbd541e33511f57123069f9d8393362ce22
    role: context
  - path: pages/traits/genomics/drt6_system.html
    sha256: a1ff9c5847c0234d8bf368704e0cb5e1178f788ae32a8142d7bfc8af2ece113f
    role: context
  - path: pages/traits/genomics/drt7_system.html
    sha256: 31e082a2381e01289f807ccc5077126b6344a89cbc3160be35866f1dfab46641
    role: context
  - path: pages/traits/genomics/drt8_system.html
    sha256: a9a2fc208cde64fb36a1f49d082cf7f0e7b55ef9e2489b6f7257708bfad65701
    role: context
  - path: pages/traits/genomics/drt9_system.html
    sha256: 0a31920895627d7aafcbce4d8512422a71ea2e861b62fda5a6ad0d1eb3a85542
    role: context
  - path: pages/traits/genomics/drt_system.html
    sha256: 626634a8cf44ad15efb5b41f744a806aa533774e73770988605308b4868a2e23
    role: context
  - path: pages/traits/genomics/druantia_iii_system.html
    sha256: 66138f589b43d83a7e1d9a6da1ee41c38c6d903dfadd7df2d2f9e791e85e55b5
    role: context
  - path: pages/traits/genomics/druantia_system.html
    sha256: 3530153653db3c8e89fe7583254434ea827027c3bd7d1555c6aa81fab8dbefb3
    role: context
  - path: pages/traits/genomics/druantia_type_i_system.html
    sha256: 9ebbd87f2be6c213f95a02d1f8253012f0055f629317d5d25b510248d8a4a132
    role: context
  - path: pages/traits/genomics/druantia_type_ii_system.html
    sha256: 32ab7d270e5b0620a2afc1885f8e6338a644e95abcb8401684c53e09b1a1ec2e
    role: context
  - path: pages/traits/genomics/druantia_type_iv_system.html
    sha256: 437eaef0593535252a60000dec77eb4ce21c080c50411c1351ce2e5d9ccea11d
    role: context
  - path: pages/traits/genomics/ds_10_system.html
    sha256: 9dd454b56259e5e17a244bfed8bf31a615a4ade2b877588ab88a3189b93b662b
    role: context
  - path: pages/traits/genomics/ds_11_system.html
    sha256: 2407dfe469bcf09bd52cea0c040c133109d26c538f8153c1a6992fa7247e0c59
    role: context
  - path: pages/traits/genomics/ds_12_system.html
    sha256: ab47b957afb93bb00ab0bd7e930f4a53b8064d473f9351e47a3afc783326d939
    role: context
  - path: pages/traits/genomics/ds_13_system.html
    sha256: d8272537745b1526cff27c23eaa5006e147f209d981cf716777241ce6a3f5bd9
    role: context
  - path: pages/traits/genomics/ds_14_system.html
    sha256: 0d9e53d57a13362bcd1f497669821fe9763aaacd296307002a4b1327396a448c
    role: context
  - path: pages/traits/genomics/ds_15_system.html
    sha256: 9e9df661db256cda164eff49459557b8e97cf2619cc8f2cca33fc317c91bd71e
    role: context
  - path: pages/traits/genomics/ds_16_system.html
    sha256: 223e9284fd4a7038c27c3f225eed1e79c6b2816b6d32d821f62e448bc8fd894e
    role: context
  - path: pages/traits/genomics/ds_17_system.html
    sha256: 279344caf106b1c25b3f4cc1eeecdbe5b5da4bd92ac63ac51dca203396c3c63c
    role: context
  - path: pages/traits/genomics/ds_18_system.html
    sha256: 797a6b7b38dead02a8e217f5bad81811ab302510ccaf111cf08d56e2028b280b
    role: context
  - path: pages/traits/genomics/ds_19_system.html
    sha256: 6e093aaaa2696d3f4844faa08f2e9f2cf8d6b72e3b4c835b2f05359824cb9563
    role: context
  - path: pages/traits/genomics/ds_1_system.html
    sha256: bd58dac30a62431487c5e92f29afc755b729cffa5838538809f0b689d60904e2
    role: context
  - path: pages/traits/genomics/ds_20_system.html
    sha256: 74de6a80f91245c5c6c40ac4186394779db2e12b65a7da42683762880971c36d
    role: context
  - path: pages/traits/genomics/ds_21_system.html
    sha256: e5a417d4d14ab1fe68db3ed9f3f91e08188682197eac816d05fb44b4cb08af6f
    role: context
  - path: pages/traits/genomics/ds_22_system.html
    sha256: c87caad565b49c3e3829254b7ef767e6dfe6565995dd5defd9638d4b72477ec2
    role: context
  - path: pages/traits/genomics/ds_23_system.html
    sha256: ce4ffae2e462b80e4eb4d64a941f010f278e38c53e3b5479bb41ab38f2598b8e
    role: context
  - path: pages/traits/genomics/ds_24_system.html
    sha256: 0d0ad8b4d18896f72bccaa14935d7d3eb33a329bc1d92264a207acf770509568
    role: context
  - path: pages/traits/genomics/ds_25_system.html
    sha256: 79634bd1f14f97de5516aad37d82e22fef6a51293c62a94bb34d45cf6a071e09
    role: context
  - path: pages/traits/genomics/ds_26_system.html
    sha256: 3cd2330dd1b7141e407898ef568a05fab80634201f4197643f339ac59128747f
    role: context
  - path: pages/traits/genomics/ds_27_system.html
    sha256: 5d62b23400f70b4bbed3b7403d85539d130e4968a5b691c26d5871f0fbb81ab3
    role: context
  - path: pages/traits/genomics/ds_28_system.html
    sha256: 9ea4b3a4ffc90d2be5baa76a3aba7fcf59866a397eb74327bbbe146e638a4ec7
    role: context
  - path: pages/traits/genomics/ds_29_system.html
    sha256: dd8334504eb64c893fc5297c5cffe47befefd36ef187370f7a7107c394338e7a
    role: context
  - path: pages/traits/genomics/ds_2_system.html
    sha256: f705da82c1586b13281736ebeed5d8474f443a5bec34883694b66989c22dcde6
    role: context
  - path: pages/traits/genomics/ds_30_system.html
    sha256: dab84b3309906c1afd2c15882e19c95b5dec14cba6b74f86b4f9292ff239bf9a
    role: context
  - path: pages/traits/genomics/ds_31_system.html
    sha256: 5d12c2910b984c606aa41be2c7e427267b9c0ae70902ccd18bddac2ef5208573
    role: context
  - path: pages/traits/genomics/ds_32_system.html
    sha256: 55b5b7f19e952a45789ee761b737094a0895928ab8b206ff988732a918b236cd
    role: context
  - path: pages/traits/genomics/ds_33_system.html
    sha256: c999e738df0d28e2588a1b89056d44e4b74935973c78628cd13934f9b53d43b9
    role: context
  - path: pages/traits/genomics/ds_34_system.html
    sha256: fad01c32d49d8e478c5e6d3fa18e1f7954702211690806e21a53689020fab19c
    role: context
  - path: pages/traits/genomics/ds_35_system.html
    sha256: b91dc041b1b2d3728fa3d68b24df25c68c37b917143ac15944883d66befbfeb5
    role: context
  - path: pages/traits/genomics/ds_36_system.html
    sha256: 11c8c356d7b6598c74d3a08804a2837a114e1703924a0b8661a48270103dbef9
    role: context
  - path: pages/traits/genomics/ds_37_system.html
    sha256: 8180f56fa679f1c2cc9e2fcca0a2207ea1bea7d5191ddfe605505f5db36760d0
    role: context
  - path: pages/traits/genomics/ds_38_system.html
    sha256: 60c42d90a03075ab7d3f5ee5d09fd51edabdcd5a05924b8ae8ba2b6730865ec5
    role: context
  - path: pages/traits/genomics/ds_39_system.html
    sha256: ff4b3c4aebe5466c8447e7e25ef2115b306729e491fba843568052b1c3decdfc
    role: context
  - path: pages/traits/genomics/ds_3_system.html
    sha256: 54873aa7f8a05dc2c12379fa7b826ae8b6195312d21659c0178f3230173d73b6
    role: context
  - path: pages/traits/genomics/ds_40_system.html
    sha256: 5a0191ec016616375e709a9ab5fc9508ad4695518f1b7f83103be0a34a1b6c53
    role: context
  - path: pages/traits/genomics/ds_41_system.html
    sha256: 3b9078669fe03b9ad4144385a6a37e573047f6475f24c4c1d5c1134c98e4bef7
    role: context
  - path: pages/traits/genomics/ds_42_system.html
    sha256: 3715fc75b7861142cde5519e732189817dad5400b9a5f079ca395cc49b0097f6
    role: context
  - path: pages/traits/genomics/ds_43_system.html
    sha256: 2ab2a2fb91cf0bae81e07826562b946a0cc80fec164eefc23fdc2f96a25ea7e2
    role: context
  - path: pages/traits/genomics/ds_44_system.html
    sha256: 61d49eefcdc001bd3bb4cf44e63b30bff54ce7bc159f5c987615f5607a549216
    role: context
  - path: pages/traits/genomics/ds_45_system.html
    sha256: 64ecd3deda07643e262f694c21c58a50bdc38d38075997f59c9f31050b3422ab
    role: context
  - path: pages/traits/genomics/ds_46_system.html
    sha256: b8dcc52c25c0ef13daceacb281c8636948bbf7f48a7052b447a13f76b5bd92cd
    role: context
  - path: pages/traits/genomics/ds_4_system.html
    sha256: 1840042fce113cbcf03080408ca4ab33c9049fdf794b47e1377ac14536a6cb23
    role: context
  - path: pages/traits/genomics/ds_5_system.html
    sha256: 6c16c29057d0a6afa66d2c893307792fbcb6db14309fe8540e4f7dc88d5c0533
    role: context
  - path: pages/traits/genomics/ds_6_system.html
    sha256: 53b08896dca2f65bb55cb13742a4ccee635a076732e7fbd51efd914f4dfed8df
    role: context
  - path: pages/traits/genomics/ds_7_system.html
    sha256: 5c29f266805e21bebffca8ccce6a034fcd77a09f2f55662f0183d07c118fd3d0
    role: context
  - path: pages/traits/genomics/ds_8_system.html
    sha256: c473bbe52e4e9cb5410e201a2748cdac252b081306f1bee2b67da3bb4550ca1b
    role: context
  - path: pages/traits/genomics/ds_9_system.html
    sha256: 3ed58e0e48f32f65410d2fde05e6439b3f364e67a29044d773a615518a10e6a1
    role: context
  - path: pages/traits/genomics/dsr_system.html
    sha256: 186a73133b8c155e1ac5684e0605c061a8fe782013f5b5dc4d39881b9bfab9b7
    role: context
  - path: pages/traits/genomics/duf262_schlafen_system.html
    sha256: 634f6bab3be5c46c71dcbc3d06d4238d6dca6a2c4fa90bb50c9dad25a8d7205f
    role: context
  - path: pages/traits/genomics/ecokmcra_system.html
    sha256: 849cb33f3fe016d8fc23cffc26eecd103faae90d37fc11f48e50787d6b0200e3
    role: context
  - path: pages/traits/genomics/eleos_system.html
    sha256: bd5d156203077e2eccb124c641b3ae534ff983be195b4ecc023bef1bef687932
    role: context
  - path: pages/traits/genomics/endpacf1_system.html
    sha256: 0fd59305b329420a5af82d80e2deebe2da2d3b26c4fed0180074021eb915bb14
    role: context
  - path: pages/traits/genomics/epona_system.html
    sha256: f75817a3f88995ea7ae143f1dd79752797b2cee5077271ffd51a20098e0bed00
    role: context
  - path: pages/traits/genomics/erebus_system.html
    sha256: ef49b6a98a3ca246b2e49ab768776a7a0b261033aa6bc4b411c29589a359e82d
    role: context
  - path: pages/traits/genomics/esos_system.html
    sha256: 16db80c78f2ae3de78490d648b35d9c4aee43014315ccd3531f8870e339c7c61
    role: context
  - path: pages/traits/genomics/fliodhais_system.html
    sha256: 0bb99f48742055320305bb58b537fb50d97e12ddb72401bc4736662bef736c41
    role: context
  - path: pages/traits/genomics/fs_giy_yig_system.html
    sha256: 8c47e1257d7c1e882e2fdb518bf385739931e7b712867025e4241007bb3d789e
    role: context
  - path: pages/traits/genomics/fs_hepn_tm_system.html
    sha256: 13f45cb00858076dc54510b772be2a6cf46d6241cd880fec22f0d66f3c7f7758
    role: context
  - path: pages/traits/genomics/fs_hp_sdh_sah_system.html
    sha256: 950846f4d9e1f6f9b346f3203d11d55adeb93355816978df16f950251c086c62
    role: context
  - path: pages/traits/genomics/fs_hp_system.html
    sha256: 30cae1c128ba3ca1036b2e3f569c5c63f40a8581d1de63be73451aa527609ee6
    role: context
  - path: pages/traits/genomics/fs_hsdr_like_system.html
    sha256: f3d433d4e0629145dc3b2a0df53103bb3f1e6ae129f7589c65122a801c75e5ed
    role: context
  - path: pages/traits/genomics/fs_sma_system.html
    sha256: 71417bb68be427cecd3374ae3d2b96137d8535802fb59600a3ed322566254d0d
    role: context
  - path: pages/traits/genomics/gabija_system.html
    sha256: 41a480074a992c5324ec7752caf89b3f5b52d32564457a382f4c8e21a6d01f05
    role: context
  - path: pages/traits/genomics/gao_ape_system.html
    sha256: ad8e508ad2dee15e5cbfc81238c243c9089f67c48f342a952b5844bbe3d9d264
    role: context
  - path: pages/traits/genomics/gao_her_duf_system.html
    sha256: 37ca97a63c135cd91248257c60369cb018049d09fdc5f7fe3e42ed63f1f8ac1a
    role: context
  - path: pages/traits/genomics/gao_her_sir_system.html
    sha256: 1ea4fd35e86578288392b82f8f028c49f65810e2e585a46ca33aed4dfafd51b0
    role: context
  - path: pages/traits/genomics/gao_her_system.html
    sha256: 0cddcfe54a1a015178890c3b8450fb9ad12c4f1ca6a8b784bd9efd0ab57f59d6
    role: context
  - path: pages/traits/genomics/gao_hhe_system.html
    sha256: 53d5a5f996d5ece2c8a472cbcbc1b69f525179c6ffe38dea3a9c63e175744c48
    role: context
  - path: pages/traits/genomics/gao_iet_system.html
    sha256: a5d466d57326e9acdf1b8cc2743a035325a8f8871d0dd22ef6d02ee88412b667
    role: context
  - path: pages/traits/genomics/gao_mza_system.html
    sha256: ee01d086094b0f61af9136f75a954d6c7b98b798fd7eba03f3f1a99e994bff7d
    role: context
  - path: pages/traits/genomics/gao_ppl_system.html
    sha256: 66e6c093b8fbbb168a59bb91e14637a00c35153ab145e29ed4d2e82d18736527
    role: context
  - path: pages/traits/genomics/gao_qat_system.html
    sha256: 595db045f7acb4222e2650c87f830d0ea187fa84f2da041c85526337c1db43a5
    role: context
  - path: pages/traits/genomics/gao_rl_system.html
    sha256: 47a7550d020cb8473e49c7b216004695bcd8b18f7304766417e363a016251619
    role: context
  - path: pages/traits/genomics/gao_tery_system.html
    sha256: 41d2d6ea8fb0caaa4bce29a5020f90f4b054050cc28226be25a8d4de47f0353e
    role: context
  - path: pages/traits/genomics/gao_tmn_system.html
    sha256: 8e35ae9e67abc76d91438094c335e7959bb1eb1a67c1e2903e84cdff57edcd43
    role: context
  - path: pages/traits/genomics/gao_upx_system.html
    sha256: f2823db1521e3eaaba24ebb4053a373559a484ac6537ccbb249c1a7005d5981c
    role: context
  - path: pages/traits/genomics/gaps1_system.html
    sha256: c582b2b426c17959c1173626b42a644e5d616fadc4bd85b9732c8bcfebb3d6ff
    role: context
  - path: pages/traits/genomics/gaps2_system.html
    sha256: 51e73735cb18bd59a2d3b5a37f1a677beae33bb419d79b4edae21ba432023191
    role: context
  - path: pages/traits/genomics/gaps4_system.html
    sha256: da04b5573a1f3c05f7f959a1cee47f2ca078d3091f19e6ad3aa1f34539a875de
    role: context
  - path: pages/traits/genomics/gaps6_system.html
    sha256: 738cfea63aca072114eb681d297daaee70f69423c3b5beffd6206717218ec08d
    role: context
  - path: pages/traits/genomics/gasdermin_system.html
    sha256: 85903baf8673183b9c822d9367a9553f3f829d9176ab29c545f856f6d7f78b6b
    role: context
  - path: pages/traits/genomics/gc_content.html
    sha256: 4d016ee9a108119eeab2ae7125d257e825b934cdb13c632e34dadfd7d2ad0ad6
    role: context
  - path: pages/traits/genomics/gc_high.html
    sha256: 91f99e6cff33a3ea02681867740672b6ac802ee8544eefcecf7bb50fb391026c
    role: context
  - path: pages/traits/genomics/gc_low.html
    sha256: fbcf647d5fdb3d80d2e1aae627b3a28dec22cc6c255c0e42daad949e63e9ea43
    role: context
  - path: pages/traits/genomics/gc_mid1.html
    sha256: 09b1ba5efe556b58805473ed99feb3b1077051066af2e5f602d3cfc971cea810
    role: context
  - path: pages/traits/genomics/gc_mid2.html
    sha256: 2404150888aee30bbfc7f773eca3139141d9c6ef237a947a9c368292cddc87f1
    role: context
  - path: pages/traits/genomics/gc_skew.html
    sha256: 9edb61bbe12dfb93ed21894ccc1a2d77d6f9706c1e06271204576891efe892e4
    role: context
  - path: pages/traits/genomics/geb_system.html
    sha256: 27b9a1997ca85ac4502bb09360501bf7d769206406e8ddbcb003ed824469fea9
    role: context
  - path: pages/traits/genomics/genome_size.html
    sha256: a992e6d7b299dc09aba0ca4982d37a132abdf17d909b814c6b04a3976ea092ba
    role: context
  - path: pages/traits/genomics/genome_streamlining.html
    sha256: 0ac492ce177132ddf1d477d249b8e024de668d42df42d29c28454209aeef38bf
    role: context
  - path: pages/traits/genomics/genomic_island.html
    sha256: afbb4c020ddb0e8a850c6a7735295ed80554ca2ee88d45ebca50e16891afb1ac
    role: context
  - path: pages/traits/genomics/gmrsd_system.html
    sha256: 47b1cd257c2c1befe8b8eb6ca52df72e15ab54d8f8919b6abd343e141e7f176d
    role: context
  - path: pages/traits/genomics/hachiman_system.html
    sha256: ba54de9ce1592fa46700f025280fe7f815df9e74878e32961098a3a15ca469ac
    role: context
  - path: pages/traits/genomics/hachiman_type_i_system.html
    sha256: b90094de529025389feb4ac5ce93bbb8dfc8b26e691b5afa8a2b1d8e11d00bfb
    role: context
  - path: pages/traits/genomics/hachiman_type_ii_system.html
    sha256: 5bd316aea6b711cbee7d33c44fb0acdc0f8af07d9ee8c7854cedd92f9c66decf
    role: context
  - path: pages/traits/genomics/hailong_system.html
    sha256: 5fe4285fc2b20d64336495b2e508f2fa5a6a73eeab20e3cdfeea4d88d0d2fb37
    role: context
  - path: pages/traits/genomics/hec_02_system.html
    sha256: 6eeb2ab81df1aee9ad0bc595db958f64f6b68c9e5fcc24851c6c288d1281ae3a
    role: context
  - path: pages/traits/genomics/hec_03_system.html
    sha256: dee1da075d93e06237b7ab661865a2a242bc6ad8e8fac067ce9fe83e569de81d
    role: context
  - path: pages/traits/genomics/hec_04_system.html
    sha256: 65e6e84e589e15800fd3c0d85a237ce817843f04d85b4c06f34b84bf720909a3
    role: context
  - path: pages/traits/genomics/hec_05_system.html
    sha256: 4433880dac29e80763b1ebc48ceb365b149cf25bad00d9ae1412dcd5236f127f
    role: context
  - path: pages/traits/genomics/hec_06_system.html
    sha256: 27f520a72bf3d19661b0da017a64278ab4eaa4dd65f585edc6d717b0fbaa2bd2
    role: context
  - path: pages/traits/genomics/hec_07_system.html
    sha256: 97caff10fbf02fa8a580d4565a4a5fcac583aebf9995bb138d3d103578bce151
    role: context
  - path: pages/traits/genomics/hec_08_system.html
    sha256: 0b2eb3079c4c6d7ef7be95ccc694ce2f1e3ee7d9761072ecbc1781dfae98ab81
    role: context
  - path: pages/traits/genomics/hesat_system.html
    sha256: 55b178603e08ff3726ecf84b9c87b5de4d1c93716106f551ce20600e6b0145e2
    role: context
  - path: pages/traits/genomics/heterokaryosis.html
    sha256: 069448af179858c2084edabe8dc2144069a5900698a0e9de65da1fe49d14c8da
    role: context
  - path: pages/traits/genomics/hma_system.html
    sha256: 56b931865280ab9587271e602552018249b82ea3a3179357f1168e497fd05eb9
    role: context
  - path: pages/traits/genomics/hna_system.html
    sha256: 199250f8ff0fdbf688f6f34d37223afa517bf8df775810b9a875d2e189432a0d
    role: context
  - path: pages/traits/genomics/hypnos_system.html
    sha256: d75ccb012f978c12a1ffe7b1dbb267ec4555627dcdb841034094fbddc5c8b51a
    role: context
  - path: pages/traits/genomics/ig_like_schlafen_system.html
    sha256: 1dd8c43e72c5e4cb76ea924d4dcd06bbfe2a29a509b979611b15bfbdbc1fe128
    role: context
  - path: pages/traits/genomics/integrative_conjugative_element.html
    sha256: a2290d8c5f5e97faccb44e0ecf9a4476fb51688559fb4f2071c75a907b10c22c
    role: context
  - path: pages/traits/genomics/jukab_system.html
    sha256: 7e828051e63a841f3f808cb6a80b2ea26b18f356882a7dc2d0037cd6af8d5c95
    role: context
  - path: pages/traits/genomics/kamadhenu_system.html
    sha256: f87718176e1437dfa315121bbf47eaacf8ba08a132ffdc79df45e0807a434a6d
    role: context
  - path: pages/traits/genomics/kiwa_system.html
    sha256: d4731233e7767ac405c1a36bf94cba2a511099ee2ab08fcfc1c40be187a1edb8
    role: context
  - path: pages/traits/genomics/kongming_system.html
    sha256: 1fce61bca1b785758d2444673170b1c293b69c339541e9b7622c45e1b8fd765d
    role: context
  - path: pages/traits/genomics/lamassu_amidase_system.html
    sha256: 265c05787f2da0fdde03ce398acfb6fadc89dd27fa161fc0b0210eed352f284d
    role: context
  - path: pages/traits/genomics/lamassu_cap4_nuclease_system.html
    sha256: 41b801f38fa033aace4395ba4ef986f6edd1a4baf44807e66b720a0692a36046
    role: context
  - path: pages/traits/genomics/lamassu_fmo_system.html
    sha256: a332b0ec7674366b981fbb468c16c454743a8d9bcc0f8a2e988524ac1d02dfbd
    role: context
  - path: pages/traits/genomics/lamassu_hnh_system.html
    sha256: 2ef0ee50a0bcdbe9115438fb8f89da39606c12a53be5fbdefb7fc6b297ec0014
    role: context
  - path: pages/traits/genomics/lamassu_hydrolase_protease_system.html
    sha256: 3b38faa8b97d329b0c848a2e1fb6de82a4910a0d9e3a96a902cdcfb4856085d1
    role: context
  - path: pages/traits/genomics/lamassu_hydrolase_system.html
    sha256: 251c42ab208bb934b8ee764c6853d1011bd7963b617352b43d344ae859088da8
    role: context
  - path: pages/traits/genomics/lamassu_lipase_system.html
    sha256: 38bcea8b5e149b892b076a937c4d4c29e5e09cc118c672794abf09296fd8dddf
    role: context
  - path: pages/traits/genomics/lamassu_mrr_system.html
    sha256: 7711aeef7056280a5933268a14bef1a08856900af942e04e418c1ac237721031
    role: context
  - path: pages/traits/genomics/lamassu_pddexk_system.html
    sha256: 5731dac74e3c4ad6c9659b7dd72f5240700f9a078b92befbe8077b2a69157ac9
    role: context
  - path: pages/traits/genomics/lamassu_protease_system.html
    sha256: 3122938270edc8a8ea99eb09567fb078d44ee5f10c49a26147a95e473c3bc544
    role: context
  - path: pages/traits/genomics/lamassu_sir2_system.html
    sha256: 467b7bf2c919dd1abd5b77cfc5dc7da258ddc056c8e68ee106d3d3a06bc4fca9
    role: context
  - path: pages/traits/genomics/lamassu_smek_system.html
    sha256: 7137a0e4319713e3fe840fd4957c35305a31134cac365b52bfb1ccf7630c07f9
    role: context
  - path: pages/traits/genomics/lamassu_system.html
    sha256: 29394c3749c38cbce9960c73483c07d573bd19486e33d4e231be03ac1e28ef7f
    role: context
  - path: pages/traits/genomics/lamassu_type_i_system.html
    sha256: 709ecd63404705a9980dbe7004332e591a4a3e184e1158aa8b2c201fffa4a541
    role: context
  - path: pages/traits/genomics/lamassu_type_ii_system.html
    sha256: 62af9ef5c8573f04fe5b6ad24605d3c2df9458bfff0d08adb4d7096a81ef4ec3
    role: context
  - path: pages/traits/genomics/lanthivirin_system.html
    sha256: c7390790561e1ff07d34f931ceede917d359153c48170bf57f80c94dfdc00977
    role: context
  - path: pages/traits/genomics/lit_system.html
    sha256: cc35c98a669fb62cca854bd8837eff131d3c51ca05b99ca7ccc93014ff22e7bc
    role: context
  - path: pages/traits/genomics/long_lamassu_system.html
    sha256: c9f084492bf3dd351bfad8dcbaadad9797ffc636e1f3f00c5a4513e5cbce37af
    role: context
  - path: pages/traits/genomics/lugos_system.html
    sha256: b4a8bce17202b9f69da26c8f05e401168dabd9fa9029faf35823fe0b42021302
    role: context
  - path: pages/traits/genomics/mads_system.html
    sha256: dcafc964e5c1e5c1eb6ed97dcdf7928ae5db90e216907c658ce3f539acb374b8
    role: context
  - path: pages/traits/genomics/mazef_system.html
    sha256: d961b8d86eee361a2840159366e6e5ac948aff6695dac86ccbd696c58f8b931a
    role: context
  - path: pages/traits/genomics/mcrbc_system.html
    sha256: f68698fa01fca7f8372f4fdb432c6cf758146c1b9ccea1380316f8e4c6b12e0b
    role: context
  - path: pages/traits/genomics/menshen_system.html
    sha256: 819c2e637f1bada83e8a90860756eb467d61e1d921e3946a999d53408143b4a6
    role: context
  - path: pages/traits/genomics/metis_system.html
    sha256: a3d9a6b6d5744775bfe11a3b065ebccb34b764504ec4198141cacf807bf4439f
    role: context
  - path: pages/traits/genomics/mksbefg_system.html
    sha256: cc759b8a09a7ec607184a0fdfa3547375dfba1fea6da3ff4f9abf36bc1ef9e3d
    role: context
  - path: pages/traits/genomics/mmb_gp29_gp30_system.html
    sha256: b192b6f1290a5815a2b257daef846ef095ca215d35f1c25ccd41c5bf40fcdff5
    role: context
  - path: pages/traits/genomics/mobile_genetic_element.html
    sha256: b272edba702aa8886a4ac4ee70ca1c281f78c025a4159c989d453f1f2b9668e5
    role: context
  - path: pages/traits/genomics/mok_hok_sok_system.html
    sha256: 22ea8159beed8d3452e0cdccd82a71ad46bac7accfa016e03a3c78269390c3cd
    role: context
  - path: pages/traits/genomics/mokosh_system.html
    sha256: ae5f0ddee1f3e18f72a4bb44e5e7332a5c3ea1d5838a3baec01b28906eacd9f9
    role: context
  - path: pages/traits/genomics/mqsrac_system.html
    sha256: d41169a0a5c7d19c9f4b0be205610e532ca7645d5b085309868a08e2eb699fb2
    role: context
  - path: pages/traits/genomics/mspji_system.html
    sha256: 542d9c03b64bfba5914501f67661ac79b8a512c5ac5caf5af7c05fe28110e3ce
    role: context
  - path: pages/traits/genomics/nantosuelta_system.html
    sha256: 7c4dc98dd8c514921ff4763481a1717ed8dae88c00dfb747c902440e9f57be26
    role: context
  - path: pages/traits/genomics/nemetona_system.html
    sha256: df206597b5fbc19762d823d7f46d0225b6ee3263893adc3be7dd20eb5874c73c
    role: context
  - path: pages/traits/genomics/nhi_system.html
    sha256: 9ea38ba19bde76a2e264d2c108265ba86420e0332bb08f8b414a63dddf12ae2b
    role: context
  - path: pages/traits/genomics/nixi_system.html
    sha256: 27c42323f9c54cbb7d46997625d2c564e79571fa63499abe2edbbb0f3c633488
    role: context
  - path: pages/traits/genomics/nlr_like_bnacht_system.html
    sha256: d41b7dc39fc26d1831a6abccccf2a4c981f66a379cdab627ec4576486d3d7a25
    role: context
  - path: pages/traits/genomics/ogmios_system.html
    sha256: 6ce7f0fec832687365b5075d854e9eb31882f3e01625ddc4be13a3f596b69dab
    role: context
  - path: pages/traits/genomics/old_exonuclease_system.html
    sha256: 83bfe8fc0c76639fa4137570ee14b94c3b4272617de1c07118f72b9d85e1e27c
    role: context
  - path: pages/traits/genomics/olokun_system.html
    sha256: de1dfe9c4c22549b0b5ec40885f4eff4ce404c238145d64fc3608e78b6736634
    role: context
  - path: pages/traits/genomics/ophion_system.html
    sha256: 1aa0f6011070e5cf2f712588b2e13184ab641821350fecc3936bf139a961da6e
    role: context
  - path: pages/traits/genomics/oshun_system.html
    sha256: 982ee6ae738b5fa7ce7c62191500c6f25dabbb07444a598da614f85842a20069
    role: context
  - path: pages/traits/genomics/pago_system.html
    sha256: 2507c00f2d8272a7ec648864f5bdb5d1d87893707bdf0abd2c3baa91484a3e7a
    role: context
  - path: pages/traits/genomics/panchino_gp28_system.html
    sha256: b63943d4b1727216633d264e9df49cd3ec0c45eb676caebae84376614fcecc08
    role: context
  - path: pages/traits/genomics/pangenome_openness.html
    sha256: e3948cbc73223f124de01c4ca92a30c91018ecf90548961464da233fff3bad2d
    role: context
  - path: pages/traits/genomics/panoptes_system.html
    sha256: a375913627255c08b939c63449e89344e865f708d3f2785f0e0b50b7dc24f7cf
    role: context
  - path: pages/traits/genomics/paris_system.html
    sha256: 4ec91a7eadb973148e0e06e018fa6adc6005a3aea1088e7bb306b3f5efbff5f2
    role: context
  - path: pages/traits/genomics/pd_lambda_1_system.html
    sha256: f244998ccccf08070b45e641ed5b0a84656b4e58ebc46fafe4bf3b0a7e4396cd
    role: context
  - path: pages/traits/genomics/pd_lambda_2_system.html
    sha256: 88c976bc7d9ccacf93e17a805bfdeb966da87f8f43634d3552b4fd528565877c
    role: context
  - path: pages/traits/genomics/pd_lambda_3_system.html
    sha256: b6f4eec86105ca119ddce2db95d5e490f96b3f74ab0dbbc19d70d72081988e38
    role: context
  - path: pages/traits/genomics/pd_lambda_4_system.html
    sha256: d2a0c0c7d52157de94b20ad5768529bc38b1af0558bf10bae150de78304a05a6
    role: context
  - path: pages/traits/genomics/pd_lambda_5_system.html
    sha256: 9081fd5a17fe48bb1c87545d11ed3871b92f85061e95e34cac3d25af6f5a4408
    role: context
  - path: pages/traits/genomics/pd_lambda_6_system.html
    sha256: 82212cc5500031378cd8baf1344369ca4bf81a26d13b155ea377e6dc8174a74f
    role: context
  - path: pages/traits/genomics/pd_t2_1_system.html
    sha256: ac2e8f9f2f84c52f00f882256715c05aad36271aabd00d5164a5aa43a60525b3
    role: context
  - path: pages/traits/genomics/pd_t4_10_system.html
    sha256: e54b08f88760babc9399893780fbd81866f100c1deef3130c4e9cd5cb3dde1fa
    role: context
  - path: pages/traits/genomics/pd_t4_1_system.html
    sha256: 2f65feb72d23fd4ad002c757d2637c3c908167c73bd2b7f58935cb347e39776a
    role: context
  - path: pages/traits/genomics/pd_t4_2_system.html
    sha256: f083e922e483d7959af9eb02aea29a27b59a50047674c2792e0902e252123233
    role: context
  - path: pages/traits/genomics/pd_t4_3_system.html
    sha256: 067a1c0ea4bf8051f942effd6f374a130c493ebcb095b564a8514675fcae96ee
    role: context
  - path: pages/traits/genomics/pd_t4_4_system.html
    sha256: 052c79a7012c155a30f013e5b4626ddf2841752dd40f215e27da797d9585aa16
    role: context
  - path: pages/traits/genomics/pd_t4_5_system.html
    sha256: bf90a8e1c46686ee487c6de520e25286e1803f24620d0127e0c84e5d346f885b
    role: context
  - path: pages/traits/genomics/pd_t4_6_system.html
    sha256: 6b3e63b84a4d2d8b541d85de738bb37a1a7538c25ea4ba55aff4022c64aef100
    role: context
  - path: pages/traits/genomics/pd_t4_7_system.html
    sha256: 7cb38fd041e19393fd219db1bcb9ff04dd9edcdcc3d4b097a79fbee1b373a566
    role: context
  - path: pages/traits/genomics/pd_t4_8_system.html
    sha256: e1b545eb68cc3f367ad7e32d6b08683de21503dfbdccfbe7b13e4c7952a47702
    role: context
  - path: pages/traits/genomics/pd_t7_1_system.html
    sha256: 4b7c1978c0b2d57db4efa21eb308e1477d2daf85b3c646d95dfea8634e88d507
    role: context
  - path: pages/traits/genomics/pd_t7_2_system.html
    sha256: f92dcf0e678b235cd82fc28841ced34aff57712ab4bdf7ed366496c0d19b4d07
    role: context
  - path: pages/traits/genomics/pd_t7_3_system.html
    sha256: 6b60c792400dbd4684cea0c90165bb0e9403029237c9dc9ad87a1d2d6d1dfaab
    role: context
  - path: pages/traits/genomics/pd_t7_4_system.html
    sha256: 6e074bf207d0b50ba9a8d9e5c6f5c6775aebc505750fe7a4551aac2b6aabcfe1
    role: context
  - path: pages/traits/genomics/pd_t7_5_system.html
    sha256: de7913ebc03fee36b65967e531e0e74ad5927657d2e3848298e16c8a9dfad43c
    role: context
  - path: pages/traits/genomics/pfiat_system.html
    sha256: 185f1c8e431eda84a2c0fbcce9dd95261f51e50b3000d028a0354b6476fe6d78
    role: context
  - path: pages/traits/genomics/phage_defense_system.html
    sha256: af43c390cdf962762aaf726f79688c660b46d1d8102ae701901ebee12d090f95
    role: context
  - path: pages/traits/genomics/phosphorothioate_defense_system.html
    sha256: 45cd63f9b2cde35e9195b0f8de711d5dccc9e53b6636d0b5f2c7118534a91cbb
    role: context
  - path: pages/traits/genomics/phrann_gp29_gp30_system.html
    sha256: 34701c8bce4b880dbd0335de6d9a7b6ed7771b86cfae3a22de3ce900c8ff6779
    role: context
  - path: pages/traits/genomics/pif_system.html
    sha256: db151493cd88b3a16f6c258fc0a14664cc40c750e06027a2f2fad2f6983ec3ac
    role: context
  - path: pages/traits/genomics/plasmid_carriage.html
    sha256: 1d0c0cf5ced9744e1c61caa84827d2445fee32eafe4a08dd1cb5bfbac7e22178
    role: context
  - path: pages/traits/genomics/ploidy.html
    sha256: caa8e1ce54d8968cb4a64c9c1c23d1cc221b496f5e9ea1983a3af218aff49470
    role: context
  - path: pages/traits/genomics/prithvi_system.html
    sha256: e1cde7f17cb276b89873b9dd7bfc0ae039ec0fdac3aa828b1de4b00cf8e619c7
    role: context
  - path: pages/traits/genomics/prometheus_system.html
    sha256: 443994247e3e4e2e2cd4698871c127833f0848d1e0d3ff773a87d32d515d9509
    role: context
  - path: pages/traits/genomics/prophage.html
    sha256: b709b1e305b070e0ca946c7c8bca0db7cb11257ce555b6cc52b805f5098ee4ee
    role: context
  - path: pages/traits/genomics/prrc_system.html
    sha256: 212d0faa351cf528aa42019f52d37d20e201dc6739f1545be625568732d7ddfc
    role: context
  - path: pages/traits/genomics/psyrta_system.html
    sha256: 096834be98cb370251d80fad49eea94903d04f122297abbfe27515617cb9d22c
    role: context
  - path: pages/traits/genomics/pvurts1i_system.html
    sha256: 87063b44a2740863538ff5974bcf58bb564bd4c79a6738effd6f3326247ec22e
    role: context
  - path: pages/traits/genomics/pycsar_system.html
    sha256: e1a032dc94933d1d705dc4b98e8b66d8d28b4c8d4e77568193c5de71c67742cc
    role: context
  - path: pages/traits/genomics/radar_system.html
    sha256: 4cfe34132b551d8e6a3c1e7dfa780b6ac10cc7b811765adbef37eed873565315
    role: context
  - path: pages/traits/genomics/razr_system.html
    sha256: 88d8480d9df8c45bfaa4d5390f54f7dd44a6b7c36459b2e5f07abde5c33ce935
    role: context
  - path: pages/traits/genomics/resolvase_duf5677_system.html
    sha256: e3ab8e7bd3455f6f5b268d651abcbeb0842da58a8569ce6cf73c0b59f1507bdd
    role: context
  - path: pages/traits/genomics/resolvase_kap_ntpase_system.html
    sha256: a55385e27e77321233d05ad5d60bf0a3d92c32d2024ca66c2af00a0ca9942a85
    role: context
  - path: pages/traits/genomics/resolvase_schlafen_system.html
    sha256: 4a07a959d701f0c3ff41f751c5fa44c1164e2750839b7a28cbb5e85e9760f5c3
    role: context
  - path: pages/traits/genomics/restriction_modification_system.html
    sha256: b999dd7ddaa152f10b3d425a06cd458bb3ae8747190e852abe83478393fec9f9
    role: context
  - path: pages/traits/genomics/retron_system.html
    sha256: 6f01125da5a143d983b9ef8cb278f1e5b06ac4a009f4a7cc2e61bfaa3f255dc1
    role: context
  - path: pages/traits/genomics/reve_system.html
    sha256: d081cada2d7fbddbb2ec4852b47bf69735fad85ea0ecd8da2532c2f4a99dbfeb
    role: context
  - path: pages/traits/genomics/rexab_system.html
    sha256: acea91279c479ecc1d50f75c5e2922408581bfe18bff5f8260ed8fd2b1531512
    role: context
  - path: pages/traits/genomics/rhea_system.html
    sha256: 34522fc46170d304b371cccce8d904c482f671b12a9a226e19a1e75b2be152fa
    role: context
  - path: pages/traits/genomics/rloc_system.html
    sha256: 8ff8a86fcabe744db0094403a80da935b757c8b1d813ff41e24ea457614fda20
    role: context
  - path: pages/traits/genomics/rnlab_system.html
    sha256: 2fed79618c21d10132b1828cc6d46b4e15a6f67a25faedc1d99368ba64d1d009
    role: context
  - path: pages/traits/genomics/rosmerta_system.html
    sha256: b6dc804ee4a1b864d2d3da01c914aa0aa6941cf17dd7f9509cc87f96456742ea
    role: context
  - path: pages/traits/genomics/rrna_operon_copy_number.html
    sha256: 3855d890cb8b210b119d56d3f89986a7d9fb793a4e2cc335d76a0ee84035efa9
    role: context
  - path: pages/traits/genomics/rst_2tm_1tm_tir_system.html
    sha256: 5b26e52efa2879c3331f723bf98a692154f7c54871325eded4d9ee453e678bae
    role: context
  - path: pages/traits/genomics/rst_3hp_system.html
    sha256: 3a46ea3a8155d2f5152da6a6b3abc75545fb7601d28188c93290acd76071a44e
    role: context
  - path: pages/traits/genomics/rst_duf4238_system.html
    sha256: 7876e11c7d8114552b1b6f9db37d953f11e1d29f0b78c7460fdccd95f4f284ff
    role: context
  - path: pages/traits/genomics/rst_gop_beta_cll_system.html
    sha256: 82f18988f0512ec5634e1d6317887b3ff8bdba66b231b146718e472508e76448
    role: context
  - path: pages/traits/genomics/rst_helicaseduf2290_system.html
    sha256: 4c721e6958af30f3e15c1423f7efcdb37e2fa9a4cc7ce81ce0e120e655e494fb
    role: context
  - path: pages/traits/genomics/rst_hydrolase_3tm_system.html
    sha256: cb5b697fd91c4a2b16546b8985e891bfda3cb2127b6c5f732abdb5ed9871a600
    role: context
  - path: pages/traits/genomics/rst_rt_nitrilase_tm_system.html
    sha256: e9c4c7e77ff5cb8e84fa1e980fdec0b5d1cfb841b2b55ab314dba8daffc4665e
    role: context
  - path: pages/traits/genomics/rst_tir_nlr_system.html
    sha256: d4c329a090bb383bc98bbe179b33491e829338e8aa0f2d3c62aea6a7ecce3ea1
    role: context
  - path: pages/traits/genomics/rugutis_system.html
    sha256: cf668e3629c4c7d380bf16bf100a38efa63f41710b548fd027d8c8f21d0011b1
    role: context
  - path: pages/traits/genomics/sanata_system.html
    sha256: c534cbf5a43ca1c57895c22ed674102e16430b8baeb5781b3b53158e49514ca5
    role: context
  - path: pages/traits/genomics/scomcra_system.html
    sha256: 6e50516371c99b7254ec79861e5bb010c9e2a3220b95c081fecda8d3fae959bb
    role: context
  - path: pages/traits/genomics/sdic1_system.html
    sha256: 6b8faa59825c8f1950d6aef94d720f4e94937182c67c3f89b58b0eeb268d4d0a
    role: context
  - path: pages/traits/genomics/sdic3_system.html
    sha256: 2f5a44345766b13c5142d677d05fe5d287341e5966c1b61b1a5d1f74c0ada1ca
    role: context
  - path: pages/traits/genomics/sdic4_system.html
    sha256: 1345fc8f065c877653964a43792f25177966deacf8810fc1552436b13612f945
    role: context
  - path: pages/traits/genomics/sefir_system.html
    sha256: 18bf91de3b41ba4c3991613fc7055659d9c2e92011fdbadf723959e0fbd3534d
    role: context
  - path: pages/traits/genomics/septu_system.html
    sha256: e1b90e8406d5400bccf063d5f2deb0f957c4cdbb3c83ce2dfe40cb8b591147cc
    role: context
  - path: pages/traits/genomics/shango_system.html
    sha256: 9e1ddc64a6ebb59962391e5347849ee7e48a304a25fe18c78e2e042a49a38463
    role: context
  - path: pages/traits/genomics/shedu_system.html
    sha256: c6721e1b28ccbccd9d358163ce86a5adc944f41961d9bea655395d9d17f24117
    role: context
  - path: pages/traits/genomics/short_lamassu_system.html
    sha256: cb544085bd5b20ad7288fdf32db6f6a4afe0eb19aecaa437b601743791b13d62
    role: context
  - path: pages/traits/genomics/shosta_system.html
    sha256: a81f92355123426144eca506973136c7f099bfe8f905e135a42ca4725f5a3f90
    role: context
  - path: pages/traits/genomics/sirona_system.html
    sha256: 3c5c10b68f355deddbbc804f3ea4fe501bc8dae0d0166d6fc3b6acbb8166f76d
    role: context
  - path: pages/traits/genomics/six_a_mbl_system.html
    sha256: 62a2bf9fdabec6e7becf8dde7c02e50dd75ab40d301295b0b8fd2902e7fc62a1
    role: context
  - path: pages/traits/genomics/snipe_system.html
    sha256: 9ed3d25990717624270420a509e049d8041272278d6f9f41441d5c1b874356f0
    role: context
  - path: pages/traits/genomics/sofic_system.html
    sha256: 1ee06d00f95bbbde86e86058c0a21c9aec497f4938cc3b07ca9b22695758e1c7
    role: context
  - path: pages/traits/genomics/sparta_system.html
    sha256: 32ab0362411cdfdff85349a71d5654fd6041482fe826fc1ac1db0dd2d0ab3c40
    role: context
  - path: pages/traits/genomics/spbk_system.html
    sha256: 246acf419592386f4b64616607de6b3ed95540a23156e341ac01ac589d3be2cf
    role: context
  - path: pages/traits/genomics/sspabcd_sspe_system.html
    sha256: 3cc94796225b640593b18dd45b819e6ec8fbcd5d8986d53e07a6c9614b4cb9c6
    role: context
  - path: pages/traits/genomics/sspabcd_sspfgh_system.html
    sha256: 658cfb9234dbe43486d88e07102cfb25dd4eaa4027994a409f82ccbeb523f25b
    role: context
  - path: pages/traits/genomics/stk2_system.html
    sha256: cdde052657ff8adbb97b4ae4ca85bbb6db281efb6abfe2c27be92fc6da5b7ee3
    role: context
  - path: pages/traits/genomics/sucellos_system.html
    sha256: 6e4cf4a6bfb6b454e01bb3b6e7e878a397776c486f523b35f4c47e8b565564dc
    role: context
  - path: pages/traits/genomics/tab_system.html
    sha256: 7a76fb79e40533a63f13b6a6f4eaae85ed176b84a4a84e06d608ef10bdfbbf29
    role: context
  - path: pages/traits/genomics/tagi_system.html
    sha256: add96ee13e30daab26cebd5a7c0dcb80a71c00b441d649b7b9b4fc214e102a30
    role: context
  - path: pages/traits/genomics/taranis_system.html
    sha256: 3f76bfe2ae2f8a9a7f1e43c836915ed76f3addd5e1a299af2ca38ec16e1ff335
    role: context
  - path: pages/traits/genomics/tgvab_system.html
    sha256: 9164e50e43c33e5a787ff0d722324268becb03868b18147b7ac0de9c15a35113
    role: context
  - path: pages/traits/genomics/tha_system.html
    sha256: c31f154ff04a89f86e1906c580961ac31265be2047ca8b5a4a5b53dbfc5adb53
    role: context
  - path: pages/traits/genomics/thoeris_system.html
    sha256: 461517502292aff5e91930d18b52383f0fad5c9754074575a7a8df67255093b7
    role: context
  - path: pages/traits/genomics/tiamat_system.html
    sha256: ea0f5a1cc6d882210c7a3114046f5634c97e5e8dfbb724f2afb81cc3decbe60d
    role: context
  - path: pages/traits/genomics/tir_i_system.html
    sha256: 4a67fb2de9ec23c15aa137324865068d858f08342031e9fe4ee557c0ab4b299d
    role: context
  - path: pages/traits/genomics/tir_iii_system.html
    sha256: 5857943da9fe7331bf74f3787184f0324bbd30cef05ef26e5c095228e8b6db7f
    role: context
  - path: pages/traits/genomics/tir_iv_system.html
    sha256: 20cdbe4c8c3e5b3a9ad30e0ad40e3e8c6a07be7a908c7bdabd8598c632feecad
    role: context
  - path: pages/traits/genomics/tir_vii_system.html
    sha256: 36851ad0aa874ce4390d5c00e6acbca55985d08d03da69f8b0f64be9cd9846fb
    role: context
  - path: pages/traits/genomics/tir_viii_system.html
    sha256: c8022c47700cf845eb6d8b114fb3fd806378bda2c560c14b6399d4af9eba4bf4
    role: context
  - path: pages/traits/genomics/toga_system.html
    sha256: 44df2cec8531bf66a5a93d6a2ce7b2c4e142c09b500cec752437493fa6f82ee2
    role: context
  - path: pages/traits/genomics/toutatis_system.html
    sha256: 73d185503053a564576fb9760f7b124eccf2801f5a2091b0c81be096ff6c06b0
    role: context
  - path: pages/traits/genomics/toxin_system.html
    sha256: 7752181fd429ee5ca57f2676ecbb44fdb5028f60477c015842f2c094a2bfc9a8
    role: context
  - path: pages/traits/genomics/transposable_element.html
    sha256: 437c71255887e1b719d3e5342b6af6779da342a9aad40cbc0f0a72d350c12f05
    role: context
  - path: pages/traits/genomics/type_i_restriction_modification_system.html
    sha256: 679f17368fe4af7632622da601de29c8d8b7045c2dd4dea5e3d822ccf300a7f6
    role: context
  - path: pages/traits/genomics/type_ii_restriction_modification_system.html
    sha256: 22589d097989a5356d4a91aa53f4e1d926ee07b69fffa77e90b5973a378f7b7d
    role: context
  - path: pages/traits/genomics/type_iig_restriction_modification_system.html
    sha256: 724b88df028055604c2bcad21c8b5c1c774236fc54ed6e29cddb3034232caa96
    role: context
  - path: pages/traits/genomics/type_iii_restriction_modification_system.html
    sha256: 66bc5dc45f0b013138a2b412caa2aec91ed57f16ee541caffc09facf40673ecb
    role: context
  - path: pages/traits/genomics/type_iv_modification_dependent_restriction_system.html
    sha256: b44801a570cbcc9b227b2983f838d83cd3c898a4c0e8d1db60f8db300bb1094b
    role: context
  - path: pages/traits/genomics/ukko_system.html
    sha256: 5d694ee6725ac4f3c602bf4d899d084da01c13e3f266019f919ba78e7b742907
    role: context
  - path: pages/traits/genomics/uzume_system.html
    sha256: 154f3dec0cbbebf808cd7c3f31898a80b123ca4eb7b20506655864503449043c
    role: context
  - path: pages/traits/genomics/vcam4i_system.html
    sha256: 4d89eca2123d91aa43c6e6396b8d5a8d938d67fa90bad86b7c8b38a6fd7a0e52
    role: context
  - path: pages/traits/genomics/veles_system.html
    sha256: 68d3120e237c1ae3ca0f3c63a58acae3c98a0c200350be36c7ab89e8ec3e5aaf
    role: context
  - path: pages/traits/genomics/viperin_system.html
    sha256: 6e1c5b65b9097712c58ce953ca4982c6467227c781ead89b5ac082b1bb886715
    role: context
  - path: pages/traits/genomics/vp1796_system.html
    sha256: 3cad91b90e46ff0e5e254548f2fcb680f950997b370382a100bcbd6ee80ea7d0
    role: context
  - path: pages/traits/genomics/vp1817_system.html
    sha256: 2271dd9d78d7aee9e27c165b6b32861bb8427c740df04226faf7a0a20da47711
    role: context
  - path: pages/traits/genomics/vp1823_system.html
    sha256: 0d038ddf2ad476a2f4126b41f9b2a812909c1920595ef058e9fd0fbb47f42ab0
    role: context
  - path: pages/traits/genomics/vp1826_system.html
    sha256: 6f640925d1c162ab3683225956d954c9a146ff456646379bdfd00812fac8b817
    role: context
  - path: pages/traits/genomics/vp1839_system.html
    sha256: 0d92dad40c22eecfe35883a189a49f45260fc058438e3782e141b01027fa2b0f
    role: context
  - path: pages/traits/genomics/vp1840_system.html
    sha256: 45578120fee1d870e0f78f671ee5645c2369621cfb98ec11619be001645ef1b0
    role: context
  - path: pages/traits/genomics/vp1848_system.html
    sha256: 9d6b085024dc9066a9eb021b18e8d3bd0b928f72ea13721b6254d3440121c49b
    role: context
  - path: pages/traits/genomics/vp1851_system.html
    sha256: d01fd0d5996e79bd65985656b966b78810b7956288b81e8e862cfda6d8d7bec2
    role: context
  - path: pages/traits/genomics/vp1853_system.html
    sha256: d29610bf5a373ebfa94e2c550cc95328a56607b71ab22b97aa68e5da0cfc121f
    role: context
  - path: pages/traits/genomics/wadjet_system.html
    sha256: 46766014788bf4cbc05f818183d6097ea2a865ee4f5b7f0b7a66363ada045ce8
    role: context
  - path: pages/traits/genomics/zorya_system.html
    sha256: db3953e713e64ece050aa78e0d88ddaed7842159066d77bb6b630774370eef6a
    role: context
  - path: pages/traits/genomics/zorya_type_i_system.html
    sha256: 73606335f1a5193bbd4ac1ba09d568ee843f23507ad91245d813ef13cf41f11f
    role: context
  - path: pages/traits/genomics/zorya_type_ii_system.html
    sha256: 598df515000686751398016459319ac62ff69a09d66ad2cc0867f2c1fc162481
    role: context
  - path: pages/traits/genomics/zorya_type_iii_system.html
    sha256: bd5e3b00f44a8beb4c91048c9783c21a22c9aac58976312398c36ed754a09b36
    role: context
  - path: pages/traits/metabolism/accumulates.html
    sha256: b38826cc9efa026db06b657d3265da3fadbbbd619f5c38b55340872f9587023e
    role: context
  - path: pages/traits/metabolism/acetoclastic_methanogenesis.html
    sha256: bbb8cabf6f729ebde16ee76c0f3300acc7b2ad9a21f60ebd3311a8e92be923ab
    role: context
  - path: pages/traits/metabolism/acetogenesis.html
    sha256: 8a5f79a021c6151d7e5024359077db6545311fd6b8bca557f00e90b916df72dd
    role: context
  - path: pages/traits/metabolism/acetone_butanol_ethanol_fermentation.html
    sha256: 7752b56c8b9d75e39608fdd87fb3271af3b2f8a644e8b49acd533b442e4b7a0b
    role: context
  - path: pages/traits/metabolism/aerobic_respiration.html
    sha256: 1d3492a90e8dde79477b6cda7877a79719ed376dc529e98c6c3864c9ea0293e8
    role: context
  - path: pages/traits/metabolism/anaerobic_ammonium_oxidation.html
    sha256: 955b43b3a3eb177c767354539c9a4564f949a01f27c2c355a9125cf9d6dc40ec
    role: context
  - path: pages/traits/metabolism/anaerobic_oxidation_of_methane.html
    sha256: 058e439227e71e720bd632066825f517dddd243a5047632c0d85007d8d3f9067
    role: context
  - path: pages/traits/metabolism/anaerobic_respiration.html
    sha256: 2f2a7023fc2f8d546a1f1349cc3dda26c14f26c66588b395cbc3438f94bc82ec
    role: context
  - path: pages/traits/metabolism/anoxygenic_photosynthesis.html
    sha256: 8666a1bfd0e530104997f0682e1dd57737d9fc3a22cd77e00b985255e3a1f256
    role: context
  - path: pages/traits/metabolism/aromatic_compound_degradation.html
    sha256: b94253c12fb75d224303e06b685f0474c144235a7b6a16ab78862111e107b615
    role: context
  - path: pages/traits/metabolism/aromatic_hydrocarbon_degradation.html
    sha256: 1623911b8779f27443dac39608b35411b4fa6cdd2a4bf9c470593880363f72e8
    role: context
  - path: pages/traits/metabolism/arsenate_respiration.html
    sha256: f7f0408d2eccbbe18ab9642888890952f3f35b9c0d236c5c67afb58942f58b24
    role: context
  - path: pages/traits/metabolism/arsenite_oxidation.html
    sha256: 9ce2a30f1797c5a644114a621c4b08aa8e29d7f16d314e6f5b225e8735dd5d1c
    role: context
  - path: pages/traits/metabolism/assimilates.html
    sha256: c81a3a5cf024060a3f677a20c3d91b25866724f8e5aec8a47c1cc9cf2c1410e2
    role: context
  - path: pages/traits/metabolism/biopolymer_degradation.html
    sha256: 7060eca8718210a6732f26c0064013f8f2773e421308ab7f1a8904c23f9c5acc
    role: context
  - path: pages/traits/metabolism/builds_acid_from.html
    sha256: 35851c817192181a8e272936aa95350f00d551f64e43592ca77583c8c25417d9
    role: context
  - path: pages/traits/metabolism/builds_base_from.html
    sha256: 97f1ccbe093e6eb7ba41eb1cbd9f254ac8c90e7fe8fd309c20c4c1713173bdf9
    role: context
  - path: pages/traits/metabolism/builds_gas_from.html
    sha256: bfcc9ff0c6b42eb9336b85c987181d5891648ee7113f1c6ea67c242d91b92332
    role: context
  - path: pages/traits/metabolism/butanediol_fermentation.html
    sha256: 66a104477fb7d5c74fcaf67a7287a2df9d1b1cf088bd24297bae4359e16abf3d
    role: context
  - path: pages/traits/metabolism/butyric_acid_fermentation.html
    sha256: 441253d43c2367ea3b905a16bd637b527a3aa5edd666a6124d36c2f1d60e282f
    role: context
  - path: pages/traits/metabolism/cable_bacteria_metabolism.html
    sha256: da3777fa2b9ae82d6b184c1907d4f89ca7f03af58d63094b74aed0c3b9f779f9
    role: context
  - path: pages/traits/metabolism/calvin_benson_bassham_cycle.html
    sha256: 1f70c466e669e19b098f8034412ffc2354699068fb8d0e655ad43426cda452ed
    role: context
  - path: pages/traits/metabolism/capable_of.html
    sha256: 8049826d74641b9a733b7331cac6274995cefb74a013aef37293f4d7fbf3826e
    role: context
  - path: pages/traits/metabolism/carbon_fixation.html
    sha256: 0c22b7c158a4a31ee2f2caffa6b337947c0637dc8d11eeb61349fac7252a8d38
    role: context
  - path: pages/traits/metabolism/cellulolysis.html
    sha256: e79c8834d735cced2338ac97a4b781c1607668151d6150ec1e9cebfda4c3bdec
    role: context
  - path: pages/traits/metabolism/chitinolysis.html
    sha256: 61b65a834a87ee3647bda3c479701ca1b1228e4812c059221a9b0a884ba0aa9b
    role: context
  - path: pages/traits/metabolism/chlorate_respiration.html
    sha256: 17748b249d23a88985a18f6018d8bc533d627cfa9368750d1834af4c727fbf96
    role: context
  - path: pages/traits/metabolism/citrate_fermentation.html
    sha256: cbec377f40f5792c04354df5a47225f7e27c83d267186033c7c5ed99ef3ad895
    role: context
  - path: pages/traits/metabolism/compartmentalizes.html
    sha256: 2cb9be5d2039744f507a2d2cc2d3d196e1a7cdf2e9e1c140f5da8b1c8c12c4f4
    role: context
  - path: pages/traits/metabolism/complete_ammonia_oxidation.html
    sha256: 72f0b598d4a4c9bbcaa790bde629d291f59f25aaf9ae747d2a44cbefb6430193
    role: context
  - path: pages/traits/metabolism/dark_hydrogen_oxidation.html
    sha256: aa5c514be65f5584e665fb13a282a97a330b88cca3c8133e58390fc1706fb1f7
    role: context
  - path: pages/traits/metabolism/dark_oxidation_of_sulfur_compounds.html
    sha256: 2d0e8e4773433138562d61c1a155600ed9acadf35584ff7340efc0ad01fc3093
    role: context
  - path: pages/traits/metabolism/degrades.html
    sha256: ed9d9b51bfc25abb8b8198781169d0fcd0f8b314fedc2d6b7cdcf6827e3ef11d
    role: context
  - path: pages/traits/metabolism/denitrification.html
    sha256: 0be24a7905091b3a0a9feafa2a1c77cb6883081b78906a30cb5c915227800782
    role: context
  - path: pages/traits/metabolism/dicarboxylate_four_hydroxybutyrate_cycle.html
    sha256: 7df9b1fb55403cccefb9e8820a3e7a1aff6204134fcbca791899d70ca39d7af3
    role: context
  - path: pages/traits/metabolism/dimethyl_sulfoxide_respiration.html
    sha256: 459e800753b790658f5f1baab3de8769a966991671784d96ab5e76fd312327b9
    role: context
  - path: pages/traits/metabolism/disproportionates.html
    sha256: 3f1ca8ce0f04fbb4770770fd1514aa4b298ea7f90713d590d954d8088284e1f4
    role: context
  - path: pages/traits/metabolism/disproportionation.html
    sha256: 87e3e80b3484302ca9528e98d95f8616b225005f584ef444022d86a0fe4bce6f
    role: context
  - path: pages/traits/metabolism/dissimilatory_iron_reduction.html
    sha256: 3bc0745a4a74d54e935cf1c6d25101132865741142aef265166ed5709f82359c
    role: context
  - path: pages/traits/metabolism/dissimilatory_manganese_reduction.html
    sha256: d1f7057429892d04276d0a4a15d33b97d6f85daf261eed75fa3b1ecc8f23cf9b
    role: context
  - path: pages/traits/metabolism/dissimilatory_metal_reduction.html
    sha256: e9e08fb44d4fff8a5936628772d91bdea5a64f9b61ebaa47684361c27b06ac25
    role: context
  - path: pages/traits/metabolism/dissimilatory_nitrate_reduction_to_ammonium.html
    sha256: d7714e68dcc8f4ed65352500a432024301db50455d71b79817bbaa9741b5960f
    role: context
  - path: pages/traits/metabolism/dissimilatory_sulfate_reduction.html
    sha256: 513b98e0366a5da1bbdf67ee973d107c0c0b9bea5a414564a1d384be38bf75f7
    role: context
  - path: pages/traits/metabolism/does_not_accumulate.html
    sha256: 9924de0abccec6b5fc722a65ec018adb4d654254d39b1f3ec50ff549b3f6e534
    role: context
  - path: pages/traits/metabolism/does_not_assimilate.html
    sha256: 9ef1095f8fb5247e51de16e79e09a8908538f922a032b7bf02a0fcd33632ce79
    role: context
  - path: pages/traits/metabolism/does_not_build_acid_from.html
    sha256: 3ccdf5d587c837d6a7b54debf8d5798a5e48607ec977e86ea25a436ba40ef69f
    role: context
  - path: pages/traits/metabolism/does_not_build_base_from.html
    sha256: 57186856ea88fde5a16e630131d53c31daf1693a0a3f1036d61b0a6cd5a7ddbb
    role: context
  - path: pages/traits/metabolism/does_not_build_gas_from.html
    sha256: ef0fa557e8f588a39284bb5dab9fccbf6c140199bb1e9d01d1078e02674a847d
    role: context
  - path: pages/traits/metabolism/does_not_compartmentalize.html
    sha256: 86de8f8c05b6f877b9a025c3fb2e32336f74eff6dacd4b4a3c62ab423ea9619c
    role: context
  - path: pages/traits/metabolism/does_not_degrade.html
    sha256: e324a2fc0cc6c8ae0bace2911372e7dc927d1c402cefed9d9c01c8671eda1e9a
    role: context
  - path: pages/traits/metabolism/does_not_disproportionate.html
    sha256: deb48e1d56d3e6d4bc40de65a154e19cef80ca80a39958149e267b31a3d5d102
    role: context
  - path: pages/traits/metabolism/does_not_export.html
    sha256: e2dc7797f7751d9832d4c6f2c4b6462718f8f6af4ec3ae5c6be38a684d88966d
    role: context
  - path: pages/traits/metabolism/does_not_ferment.html
    sha256: 5017b98911cf7c652024a0224df301818cbdfefae659871e386df28dc02c2064
    role: context
  - path: pages/traits/metabolism/does_not_hydrolyze.html
    sha256: a0673aceea15904f5e9812555d1fa672fc4eab3774b77594dd08f67a4546990c
    role: context
  - path: pages/traits/metabolism/does_not_import.html
    sha256: 2862fb75ea1a2b92b7fcd3d9911bbeb1f5fe945df75c5c386c3de92a9c158cf6
    role: context
  - path: pages/traits/metabolism/does_not_oxidize.html
    sha256: 890f852c9580b243b4ce63fbec1404be7fa33f3c037473b0854787c7126a2008
    role: context
  - path: pages/traits/metabolism/does_not_produce.html
    sha256: 6677d405828dfc5a129d15048c449b07be298f8b56ea3ea5895f9d4406c6d5e9
    role: context
  - path: pages/traits/metabolism/does_not_reduce.html
    sha256: 438f99372dffdd741ecb347d28032bbbf6a71aff109987ee97cd3a70b6c98e64
    role: context
  - path: pages/traits/metabolism/does_not_sequester.html
    sha256: 642674e3d5a4303532c6817bc2af4018da3090afb3b91ad183d5c16311a34c15
    role: context
  - path: pages/traits/metabolism/does_not_show_activity_of.html
    sha256: ed0404b0dfb8d75a81328c6c0e17e91722cce0362e80115dcc4e3fc4a02ac3b0
    role: context
  - path: pages/traits/metabolism/does_not_transport.html
    sha256: 26a0ce70f17eb62b591b40b7c943b7eddc7b183cca3655d5e6df5a6ed7308f52
    role: context
  - path: pages/traits/metabolism/does_not_use_as_carbon_source.html
    sha256: c4a10fcf6ee17ef430bc29fc05f300453a8e2837b50b9b51bcd999969bc4b618
    role: context
  - path: pages/traits/metabolism/does_not_use_as_electron_acceptor.html
    sha256: 8f5b99218bf0551587a239a6980ca22bc19110f63562ce8703d4ef4a944d22fb
    role: context
  - path: pages/traits/metabolism/does_not_use_as_electron_donor.html
    sha256: 89fc26c7b491e62bc6df61158c7bcf2cdcbc5ea80c52a976625bc8958d2f7f69
    role: context
  - path: pages/traits/metabolism/does_not_use_as_energy_source.html
    sha256: c7579bc07e92549a0b5e26b184a8eee1f17b269b1b43895e3b3927bae4f8edb4
    role: context
  - path: pages/traits/metabolism/does_not_use_as_nitrogen_source.html
    sha256: 50a27b6b187bac4cc4fd945e61b61f43880179d2eda31452429a07f4110191ed
    role: context
  - path: pages/traits/metabolism/does_not_use_as_sulfur_source.html
    sha256: c8e37be320d55c317a4bd14b5cee0526e5004922482a06165d89c3f2368831fa
    role: context
  - path: pages/traits/metabolism/does_not_use_for_aerobic_catabolization.html
    sha256: c1c974eee060962175e8ed1a2c23bcfcc4c8f7a611427fd387b47a8119cf06c1
    role: context
  - path: pages/traits/metabolism/does_not_use_for_aerobic_growth.html
    sha256: 5b0faeaf9378a8c2b5f216ab965b594dccc10ee9ea09135eb4bd763ec2268ed3
    role: context
  - path: pages/traits/metabolism/does_not_use_for_anaerobic_catabolization.html
    sha256: 46d49cf5a44b93a9e99172ccdee4f46a1cff509b50bf0e1db022ccc925118ae8
    role: context
  - path: pages/traits/metabolism/does_not_use_for_anaerobic_growth.html
    sha256: d569e87de051b6d74f2c7fa5f8bd2f26d7fa29675849b6cbc2458e59e53bad19
    role: context
  - path: pages/traits/metabolism/does_not_use_for_anaerobic_growth_in_the_dark.html
    sha256: 4481cd0e9289b898fe2b9d2f4b3e68d30696b571e33f3057f3a7509e200b07ff
    role: context
  - path: pages/traits/metabolism/does_not_use_for_anaerobic_growth_with_light.html
    sha256: a8625d0a0c25349e90200bc0f7c19e5ba84cd0b700f14329a3c89dd7b0975f97
    role: context
  - path: pages/traits/metabolism/does_not_use_for_growth.html
    sha256: e92414f177ebe73e502e5a6224f44adfb2142f49a99bac0f17061a5cb27c083a
    role: context
  - path: pages/traits/metabolism/does_not_use_for_respiration.html
    sha256: a91cbf04f559561d205638e774b45922d11d74c81401d71f0e17847edae6b1c0
    role: context
  - path: pages/traits/metabolism/does_not_use_in_other_way.html
    sha256: bdfc035fad10ae4cd03f75e6131c842ae1d21a1a944bd7cc33f676daa8b27854
    role: context
  - path: pages/traits/metabolism/electron_transfer.html
    sha256: fd0cc2c97560f11a774e7710b05ffd24b29dd61a9e3da65617e6befbf483278e
    role: context
  - path: pages/traits/metabolism/enzyme_activity_analyzed.html
    sha256: 8b182fbce3747f8ddbb95d15c523622186fbf964fc7c75a9a552f0e3c426b0f3
    role: context
  - path: pages/traits/metabolism/ethanol_fermentation.html
    sha256: 09a8dcb49ee8d6e740ff4406423797cbf4e18027011a5cd4bc4729f4da182396
    role: context
  - path: pages/traits/metabolism/exports.html
    sha256: cd80b791564f4cba6b0914bd66e737068d97a9899dd7bcf42756df269ff5665e
    role: context
  - path: pages/traits/metabolism/fermentation.html
    sha256: 22445ead0e2d2ae091d300a03fdde47556e0e63f1dd12d14e85570622eb2dbce
    role: context
  - path: pages/traits/metabolism/fermentative_hydrogen_production.html
    sha256: c493224031103dd71f61d2bc56cb4832477a6414304074cefecd901be3134300
    role: context
  - path: pages/traits/metabolism/ferments.html
    sha256: 7178def30082a3bd48adb3bee63e11de81a6bbc9beb03e5498fcff997f3ad153
    role: context
  - path: pages/traits/metabolism/fumarate_respiration.html
    sha256: 016e285853e916d5008db99a2f9b8174d93313d07b5665af46822a270940936f
    role: context
  - path: pages/traits/metabolism/has_growth_nacl_observation.html
    sha256: 07022cdb0ce7a6a6709ac1eccda9c8daa081057e4b819bfe11dd3c6cf0c3538f
    role: context
  - path: pages/traits/metabolism/has_growth_oxygen_observation.html
    sha256: 52d5ffc63251101cc8e01f9e1ada29b50b1715aa6edd48720a02f0f48aad0926
    role: context
  - path: pages/traits/metabolism/has_growth_ph_observation.html
    sha256: f5785fb2e421f2759d1fce66b89895b268e743c12652deb48b1fc9b48bfc19ba
    role: context
  - path: pages/traits/metabolism/has_growth_temperature_observation.html
    sha256: 98cc38eb53d9b08d9f84d1ea425a454df3881c8e32e3c0eb93bc81a56303ba99
    role: context
  - path: pages/traits/metabolism/has_nacl_delta_observation.html
    sha256: 80b3b408686ce7c86a75d2ee1a52f034c3111b91f9649753246e735ca1af3034
    role: context
  - path: pages/traits/metabolism/has_nacl_observation.html
    sha256: fa5e0f0ca41d62c94dd9ca0f0cdba926dd579921c32bf18124e1f9a6b63820fc
    role: context
  - path: pages/traits/metabolism/has_observation.html
    sha256: 8d44cd1191d3ff5726724739cc78e8e113f5aab1e3c8ea98a9bfbf008c9f8f94
    role: context
  - path: pages/traits/metabolism/has_optimum_nacl_observation.html
    sha256: b5f8d0d89d547b2e3683235583075b3d613abc8c5019d00cd81ed21ab154020a
    role: context
  - path: pages/traits/metabolism/has_optimum_oxygen_observation.html
    sha256: 8735237e5072548e87842b2b9e13f253aa337e2aeefd5f36b1fcef915e87d13b
    role: context
  - path: pages/traits/metabolism/has_optimum_ph_observation.html
    sha256: e81a7ccf34b5b711476c344d226de8c78683e0780b5626865ed52feac6f25276
    role: context
  - path: pages/traits/metabolism/has_optimum_temperature_observation.html
    sha256: 34f3afec138afb6ad9f9551d43f89f2a9f091e55fb7eead5955703a661be9d30
    role: context
  - path: pages/traits/metabolism/has_oxygen_delta_observation.html
    sha256: 1797091d0160957a27c1d29fefc397cea05b2781a06f8e075ff8c847aecdf188
    role: context
  - path: pages/traits/metabolism/has_oxygen_observation.html
    sha256: 28cfc00ca61d14cbd206339b22daea2b28af22a224465518e0b65d0b5fe49eaa
    role: context
  - path: pages/traits/metabolism/has_ph_delta_observation.html
    sha256: 5cffdf5269bf3cec311cb4899f50e17c22593d05a55541fd4ed8610ab3c7cd49
    role: context
  - path: pages/traits/metabolism/has_ph_observation.html
    sha256: 22f9b826757391b3fcaf5277d364d35f6133366f16db9ba65bfcaf5e76449115
    role: context
  - path: pages/traits/metabolism/has_phenotype.html
    sha256: 4d0c675bfdebd8a84a1bf14c7ec91ca2fe2823c9b4e9eb010dd558a842fcd748
    role: context
  - path: pages/traits/metabolism/has_quality.html
    sha256: 3cd6936d3728d6bfa2d59484601a84db65bf96e7c90f01eea77de5d23e40b5b3
    role: context
  - path: pages/traits/metabolism/has_range_nacl_observation.html
    sha256: 30ae8385cdf6a49578b10f4615074cd9c53fae432f5ccc8350a79964a5e61325
    role: context
  - path: pages/traits/metabolism/has_range_oxygen_observation.html
    sha256: 542a6d51d8f41520b2e28b90cdd9d42a47827c046312d8394d8adc3d5773d0cf
    role: context
  - path: pages/traits/metabolism/has_range_ph_observation.html
    sha256: 38a8969c22a5955498d28332cd00b3baa550bc2fab09df6bafa978a88735f145
    role: context
  - path: pages/traits/metabolism/has_range_temperature_observation.html
    sha256: f047becbf5e5b1cda8358bb47388e3f76655e26b3946693dc9f291cad504aa50
    role: context
  - path: pages/traits/metabolism/has_temperature_delta_observation.html
    sha256: aa0f75c35276bc96c2f9160143137fbe6e0b8d73c32e2a0e91db914bde732659
    role: context
  - path: pages/traits/metabolism/has_temperature_observation.html
    sha256: 95fb80c9e42c67ac2b7cbdc718601b5cb561b1050a7ef2ab9c7edd70b8f5a890
    role: context
  - path: pages/traits/metabolism/homoacetogenesis.html
    sha256: b254650bcc6dc0238afbb5f23d18e6eb948edf17ab0359d079e40c762987dc53
    role: context
  - path: pages/traits/metabolism/hydrocarbon_degradation.html
    sha256: 189c605b6f41b34d2e287044c1763514f9191fc0011393b766454bd11733dcb8
    role: context
  - path: pages/traits/metabolism/hydrogenotrophic_methanogenesis.html
    sha256: d68d7837ffca2372df40f66ac3099f2f080d8b6fee507d8e1e5cd3d4a77cdeb1
    role: context
  - path: pages/traits/metabolism/hydrolyzes.html
    sha256: dccf896fd4573209a84cc5d8442528a008039c916af14f59bcfa4b28552f1769
    role: context
  - path: pages/traits/metabolism/imports.html
    sha256: d0fbab938c8f6ebb0ccc27f6a05fc299da5c46bf4a8854405a126925901bed04
    role: context
  - path: pages/traits/metabolism/iodate_respiration.html
    sha256: b4db48171998ce29d28f2af36ac309c46fe9767ab759c5352ff270d042d001a7
    role: context
  - path: pages/traits/metabolism/iron_oxidation.html
    sha256: 45fae973b673fcd3aae3371159fdb10630fdb05110d1aec891ea203e858e0412
    role: context
  - path: pages/traits/metabolism/is_not_required_for_growth.html
    sha256: 2d8e4f35dab8c3c236e070628a8d978a92b49811f022ab0407aa0655501e4ae1
    role: context
  - path: pages/traits/metabolism/lactic_acid_fermentation.html
    sha256: a16da391eb12e19929305922284bd2d4c64aadc1ddd5b9ab487fcd04bac0ca99
    role: context
  - path: pages/traits/metabolism/lignin_degradation.html
    sha256: 6e71b57ba1be99a07e92c82c13967a040845037a802396c1297b113685296f20
    role: context
  - path: pages/traits/metabolism/lipolysis.html
    sha256: 2392e40f5b0b20e1c2d9cda0db4f102fc7a76010ac21012f176d2db9b4b96aba
    role: context
  - path: pages/traits/metabolism/manganese_oxidation.html
    sha256: 6b42543c010c24b355252544ca35ca4c5e091b44110a8323e371e45d79e95d47
    role: context
  - path: pages/traits/metabolism/metabolism.html
    sha256: 3eb277268d3dce76a824b0278febb6a3b9b7fa35f35f99158edcf2ab07c931b8
    role: context
  - path: pages/traits/metabolism/methanogenesis.html
    sha256: 7d849758a360fdf9a31f6768f614d5d18f4c3fc246d2ae702e9edf72c1e2d53a
    role: context
  - path: pages/traits/metabolism/methanol_oxidation.html
    sha256: 0a2dae1c73e88e7462a41e0acb05a4da5a43e1c1460bcbbb06f72fe9bc67df25
    role: context
  - path: pages/traits/metabolism/methyl_based_methanogenesis.html
    sha256: f5ed7cf58a3e4e560b224621460c24126430eca33d4b24c9fad65e4fc116dabf
    role: context
  - path: pages/traits/metabolism/mixed_acid_fermentation.html
    sha256: 4f472180f24b8b35118439ebf23038bdfea36b9a6dd84977f31b1391259bf3fe
    role: context
  - path: pages/traits/metabolism/nitrate_reduction.html
    sha256: 2d30b1046da29482a9a1a9fe102ad66813496b9f66def98c3b0e1650bf2eefa0
    role: context
  - path: pages/traits/metabolism/nitrate_respiration.html
    sha256: dba35add573aba53eb0157de0f049a2e4af76b8e339bc44746d0ce478961be6b
    role: context
  - path: pages/traits/metabolism/nitrification.html
    sha256: 8c099fa04b9909954ea6ce400a28db60dd081caf445aae328330ac3122c63557
    role: context
  - path: pages/traits/metabolism/nitrite_respiration.html
    sha256: df36dc20948791e40a892dfa896a38b51ace43b4b6da12bcacf4113a07bf1884
    role: context
  - path: pages/traits/metabolism/nitrogen_fixation.html
    sha256: 51a22ee22a1ea3c1b9867749faee34a1ec55555787dbded733a266d351111139
    role: context
  - path: pages/traits/metabolism/nitrogen_respiration.html
    sha256: b640c03557d74240eca633bc4fb63a628f8ccf6ec75c7ad0e366fbe3e851a551
    role: context
  - path: pages/traits/metabolism/organism_interacts_with_chemical.html
    sha256: c19fdbe8ee3bb1802e5572c3e08b7b3f687c807a51efd5bb3872d3879bd6e40a
    role: context
  - path: pages/traits/metabolism/organohalide_respiration.html
    sha256: 5463b3f2622e35a4ad67a1a3aed674b826489917bff6e9675cdbe659dbd290b8
    role: context
  - path: pages/traits/metabolism/oxidative_phosphorylation.html
    sha256: df66d268798876d317dd27a75038d72507298f8785da8feeb9b8330de2230943
    role: context
  - path: pages/traits/metabolism/oxidizes.html
    sha256: e17856366f8ffbe5704be2e7d865a0bba6c442e053c8f65c4404b75e5ef7d313
    role: context
  - path: pages/traits/metabolism/oxygenic_photosynthesis.html
    sha256: 7d6cf53c8a18a443eb21113425d1ddd76ecbb68390b9ad95f5926a98b07f7d94
    role: context
  - path: pages/traits/metabolism/pectin_degradation.html
    sha256: 5ce63b47bb30245f58ce82ead8702c8634954317077b7bb0853e0034da31a504
    role: context
  - path: pages/traits/metabolism/perchlorate_respiration.html
    sha256: 6aa0f6c1a4b5465d253f421b4d1c1c465cfb445454e9c1f2fc4ca7e9623454e4
    role: context
  - path: pages/traits/metabolism/photoferrotrophy.html
    sha256: cdd822ce9206137476b61beea77d2a079902b5bb88f7eb40b37f0722e39d87fb
    role: context
  - path: pages/traits/metabolism/photosynthesis.html
    sha256: 1be34add1304b3646a2a19991bdede298c9e12e3236c6b4e0b74decbb9bbf55d
    role: context
  - path: pages/traits/metabolism/phototrophy.html
    sha256: 10101a6bc4ad86829a4c8a1b28b02771d2b854741cb67dfc3a68c0af55abcc39
    role: context
  - path: pages/traits/metabolism/produces.html
    sha256: 690af9e7aff5d9a9c943cc5c71de10ceb14918ca6e559fbef625292e3ced0975
    role: context
  - path: pages/traits/metabolism/propionic_acid_fermentation.html
    sha256: 0e68a01a563e5771d1f230feb537a1f8654c6b02a78485c3b42c8baf94ae58ec
    role: context
  - path: pages/traits/metabolism/proteolysis.html
    sha256: 07c8c38e795c444f65ebf2b0d74b75408bc0e02f65ee7b7dae6dccb710c5be38
    role: context
  - path: pages/traits/metabolism/proteorhodopsin_phototrophy.html
    sha256: 4b66bc950f01575bcb3bda5b4b94e2225856bcd1005cfd8418eb4e15ecee86fa
    role: context
  - path: pages/traits/metabolism/reduces.html
    sha256: 35d7a948acc72dfd25eeb5d8bcc745bec052c1169c6975313d6aead54b9acdfa
    role: context
  - path: pages/traits/metabolism/reductive_tca_cycle.html
    sha256: 91b5c518b599a3261ec1a9108e6feb0b0bfcb77c38f260082dbe1138ae6e24f8
    role: context
  - path: pages/traits/metabolism/requires_for_growth.html
    sha256: f81413ac33f53813a93bab0f8b1733470d1e286968ed4e86580525bdac154237
    role: context
  - path: pages/traits/metabolism/respiration.html
    sha256: b8d7c2f1f6d2ae7363101e394f7a2338f8f2facd23abff610cbb68ed946b246e
    role: context
  - path: pages/traits/metabolism/respiration_of_sulfur_compounds.html
    sha256: 9ee34e380240ce7d9890204201f5b38524cc15d42a2d4a1618b1e31fff7de761
    role: context
  - path: pages/traits/metabolism/selenate_respiration.html
    sha256: 9a605754e08c4e71eda445ce6e5ff158b967e3b06f17d2eeef8c5f5c7ddebe22
    role: context
  - path: pages/traits/metabolism/sequesters.html
    sha256: 72e5f279ce327b61781677a101e155b6e5446f9fef9f32f8452ec9fc932a4f42
    role: context
  - path: pages/traits/metabolism/shows_activity_of.html
    sha256: 73092b6c189122c9461934a2ed330cdfae7067fdead30e61413e8e399551d4b6
    role: context
  - path: pages/traits/metabolism/starch_degradation.html
    sha256: 4ba27bcce713097284d4a5c848dca593268eea29a77174c9f048499f9d68978a
    role: context
  - path: pages/traits/metabolism/substrate_level_phosphorylation.html
    sha256: 7aa40f2f767017d55382356c0d43e00742ac2b64949beb6d1c454cc4855bf83e
    role: context
  - path: pages/traits/metabolism/sulfur_oxidation.html
    sha256: 2aed95699eec922a8d9dd18c334f26aec21cfb3fafadd4e18ddcb3a0725eb2cb
    role: context
  - path: pages/traits/metabolism/sulfur_respiration.html
    sha256: e0856f6f52118a1352d51e38b852271ae1b357ac1e158fe4e032b248e328dd45
    role: context
  - path: pages/traits/metabolism/syntrophy.html
    sha256: c5518f454d5f37da35de486126b10fba931d0862b269286574d957bfe5e82955
    role: context
  - path: pages/traits/metabolism/tetrathionate_respiration.html
    sha256: 530ead319143e7f4f732878589b5b370967684bd75d56faa13db210c0e33814c
    role: context
  - path: pages/traits/metabolism/thiosulfate_respiration.html
    sha256: b407008534b6ee5c83c81e86184bd6898a527315ff957fac05443060a9e1da51
    role: context
  - path: pages/traits/metabolism/three_hydroxypropionate_bicycle.html
    sha256: df1d72893d5d8d4655597be66ee38fe836bc567c8c4ea65986379950be50ac94
    role: context
  - path: pages/traits/metabolism/three_hydroxypropionate_four_hydroxybutyrate_cycle.html
    sha256: c4e6c3280a87996490a61593316cb61a4fd560f9e444a828121baa07d30633f3
    role: context
  - path: pages/traits/metabolism/transports.html
    sha256: 0070fdb4ecc8d846f5489f51afa4b8fdf0792c91488e0639d2c1a7200d16b402
    role: context
  - path: pages/traits/metabolism/trimethylamine_n_oxide_respiration.html
    sha256: a286121897cfb7dfb63c2d6e2dc4b30c5cf53d7a3b1267383735d312f657b53c
    role: context
  - path: pages/traits/metabolism/uses_as_carbon_source.html
    sha256: 66b98cbd49583d9b650ba02b5b859031d11f74ad7adda8d95c860fd6a5820084
    role: context
  - path: pages/traits/metabolism/uses_as_electron_acceptor.html
    sha256: 2243c25fe43069ab317d58f21b00d8b78bc722bdeadfdf37af90fa1d53affabb
    role: context
  - path: pages/traits/metabolism/uses_as_electron_donor.html
    sha256: 15e45d444b8feae81d728e078965fc957805c333a2e84d197eb457b77cb55a92
    role: context
  - path: pages/traits/metabolism/uses_as_energy_source.html
    sha256: c9579c88d8e2bb26bf96ce015740e77ba305f6712205b7cdec09183668c0acad
    role: context
  - path: pages/traits/metabolism/uses_as_nitrogen_source.html
    sha256: a5f68d2a129422377c901905e78b62c14038559eb7ed0a72b3d376a4645284ed
    role: context
  - path: pages/traits/metabolism/uses_as_sulfur_source.html
    sha256: fed211ab7b3fd3306449d8354500ffc8defd2d4f5a3ee3a36de51d4ad1f166be
    role: context
  - path: pages/traits/metabolism/uses_for_aerobic_catabolization.html
    sha256: b34cf5e91761704a554f2fb2353354488b99117c16b1d20b1a8e4b24af418700
    role: context
  - path: pages/traits/metabolism/uses_for_aerobic_growth.html
    sha256: 0f9f3fec989ce28b948b6f655fa0a15c8193ec3fab4d9dff1e23799193dbcb75
    role: context
  - path: pages/traits/metabolism/uses_for_anaerobic_catabolization.html
    sha256: a1806934082e9b2925b7800f22924c8a5047fa0e12d302ab79c159badf65b6f5
    role: context
  - path: pages/traits/metabolism/uses_for_anaerobic_growth.html
    sha256: 422ef0cf4222ebf640bdb1c2a975cc34febbe3782e84d7d077e5cddbbd290bde
    role: context
  - path: pages/traits/metabolism/uses_for_anaerobic_growth_in_the_dark.html
    sha256: ec09aeee2291ddae8b6b47c230d018bd7d28fcfab39d312a7333179443a57337
    role: context
  - path: pages/traits/metabolism/uses_for_anaerobic_growth_with_light.html
    sha256: 3bc6e254c4d516fb1cf7a70626131383209e34aa53eb4c1b240d3b44fbf94af8
    role: context
  - path: pages/traits/metabolism/uses_for_growth.html
    sha256: 2bd0289420c52daa9dc2b81fed2b2a34f02bf380c6cc49cb2e6cf7f40abfd197
    role: context
  - path: pages/traits/metabolism/uses_for_respiration.html
    sha256: 7bf89d6250d998bba8b7ee46346869998b85a0b9b4ea4a69c2f83ff820825f37
    role: context
  - path: pages/traits/metabolism/uses_in_other_way.html
    sha256: 97624c693ec22e8fe377e78dde5c453a9cc3ddb154da95055a0f1af86b1e32a2
    role: context
  - path: pages/traits/metabolism/wood_ljungdahl_pathway.html
    sha256: 2be4fff25d609b4ff99ff894636a950af50a8aae827cf81c0bad3688bf975c37
    role: context
  - path: pages/traits/metabolism/xylan_degradation.html
    sha256: 70d72650f866e2c98789077d41f927d3e09865de710c43112b711687db344272
    role: context
  - path: pages/traits/morphology/akinete.html
    sha256: 06b09962de20f7c1b151812c280290185fff3aef5efaed55f480a44ed5cbd0df
    role: context
  - path: pages/traits/morphology/amphitrichous.html
    sha256: 8164d24506fa29cfbe424336abe1c2a44e7559a4d2e5d06800facb812d976010
    role: context
  - path: pages/traits/morphology/axially_filamented.html
    sha256: c2f921171056882e883c75fc13fb11b8248f51f80bc5357e2772bcc7bd345629
    role: context
  - path: pages/traits/morphology/bacillus_shaped.html
    sha256: 08d346ba24d72a94ed45aa70ed1f28458a8285c6e8ea3155ece83460f3de6c0a
    role: context
  - path: pages/traits/morphology/baeocyte_formation.html
    sha256: f966fb1db4c17aaeb6aefe14377b6235d140d4b819248c3d46ae927d31ddfbf2
    role: context
  - path: pages/traits/morphology/black_pigmented.html
    sha256: 3fb8e1368ce23a1aae62e04628c928cf5368d41246dc4d31702f6fd13acfb5e5
    role: context
  - path: pages/traits/morphology/branched_shaped.html
    sha256: 12322776830067ca3eefbecb8ef0027d2e6731dfc3707e377b2a19f6c23c5c3c
    role: context
  - path: pages/traits/morphology/brown_pigmented.html
    sha256: e18e0fdd809be949ae986507355aa94bb85d45aa8336531fa262f13ac9e0c5a1
    role: context
  - path: pages/traits/morphology/capsule.html
    sha256: 47de3b526626f41a968b3fd05e00c9f81f08c8c094258a62cc46d0a6b693873a
    role: context
  - path: pages/traits/morphology/carboxysome.html
    sha256: 0d498860f3be935d1b292d54fa5191ceaf4d07635e0f189db7d60f9fc1617b46
    role: context
  - path: pages/traits/morphology/carotenoid_pigmentation.html
    sha256: ab75e1e5f5475c6cc05bad51a46b53e3a90373e8b26d83868af975f6fc654681
    role: context
  - path: pages/traits/morphology/cell_length.html
    sha256: 77bd3ca9f50d6135b9b6291998c6ef46bc290c16236330f10bb4be4f5106767e
    role: context
  - path: pages/traits/morphology/cell_length_large.html
    sha256: 9337aaf70f2bf39bdc5b8b7df8706b11622467aabc96e8c8d322268cce54669b
    role: context
  - path: pages/traits/morphology/cell_length_medium.html
    sha256: b5510e72293e171f1961962cd70199548bf63088927371161e48fe5b9821b81d
    role: context
  - path: pages/traits/morphology/cell_length_small.html
    sha256: ba3410660f63c1233ff0ee768de7383a6d98bde03fe1b67fc1ea179f35cc38ed
    role: context
  - path: pages/traits/morphology/cell_length_very_small.html
    sha256: 7acae5f0c3bf9d2b330a692b896bc2d949c37804b6cc6af97b9994fe982bd5d5
    role: context
  - path: pages/traits/morphology/cell_shape.html
    sha256: 87521ed15d4dbceb6e65b4a49809be77932bd933bb41e0b8589854dcf8e45daa
    role: context
  - path: pages/traits/morphology/cell_width.html
    sha256: 69a338b768a1a3c352f6ea0da987310e910a4f3be96d76600ab07996ef568626
    role: context
  - path: pages/traits/morphology/cell_width_large.html
    sha256: 854bcaa4caf9fc78f2b1197bc2f894459a2499821c79cca588693b78b0e36333
    role: context
  - path: pages/traits/morphology/cell_width_medium.html
    sha256: df7f3c9564d1eaeaad7d72b8646517e1d36622720732e7449a2c9df80314399c
    role: context
  - path: pages/traits/morphology/cell_width_small.html
    sha256: 8132020118deb5edaa9326b7f717e1ea5176b7250018227d5ca5d3c73bdef1d6
    role: context
  - path: pages/traits/morphology/cell_width_very_small.html
    sha256: 23b06d1ab3be1ae2e6bc29f8278268f52da1b2640720fd79393bf79d3849953f
    role: context
  - path: pages/traits/morphology/coccobacillus_shaped.html
    sha256: 72d77f53d4f55c3de48abb9af985d33c3a6d9e70099f4ec6d4594557355be7d6
    role: context
  - path: pages/traits/morphology/coccus_shaped.html
    sha256: a18486d77c17cde525915c124b629421e2eaa14cab9f072f72b6ccbfb5c7ddc8
    role: context
  - path: pages/traits/morphology/coenobium_formation.html
    sha256: 5666163a5eb527070d714b14d65eda5bb7cb8ca9f030f2a6d3ece7f03a481104
    role: context
  - path: pages/traits/morphology/cream_pigmented.html
    sha256: 125aae72da7c1e0c94ae064476e6d01968bf6ae9212462400fa2e9eb55f0294f
    role: context
  - path: pages/traits/morphology/crescent_shaped.html
    sha256: a96eb4d6031737dc8f5000252caeb2810be1f8e2602b41a86b64c48f9a8f04a4
    role: context
  - path: pages/traits/morphology/curved_shaped.html
    sha256: 0d0b4b161d03db69b0e7f4adf68ca018602b796f36ab83ac559615f08262864a
    role: context
  - path: pages/traits/morphology/cyanobacterial_multiseriate_trichome_formation.html
    sha256: 1ace024604bc4166eaf63b73d471628ac8ea046ecd38fbdc30f16379579d53d8
    role: context
  - path: pages/traits/morphology/cyanophycin_granule.html
    sha256: 36633b55181fb1ddabaf1675426395585fd720c10b0ce544198c65deb3eaa3e3
    role: context
  - path: pages/traits/morphology/diplococcus_shaped.html
    sha256: a30919de26401c3e39ad446bbb468da9850443c2ab96955b868ea9a15e6f5577
    role: context
  - path: pages/traits/morphology/disc_shaped.html
    sha256: 15855110c0e019a43c2cc24b23a9b5036232f17618683fd5c903260f8d1a795b
    role: context
  - path: pages/traits/morphology/dumbbell_shaped.html
    sha256: 768d2fbe70a7cf992d6350bbb1cefd66f82674bbebbb765617f5e011e048bbcf
    role: context
  - path: pages/traits/morphology/ellipsoidal.html
    sha256: e22f355d153224ad95002903026dce75eeed15a9f97d3cf7afbe5dfa551bd7c7
    role: context
  - path: pages/traits/morphology/expansion_driven_sliding_motility.html
    sha256: 269f4875e2efe1f57de89e249cd5f927f8a0c4221a75c00e7e3c7ba3b7936fb1
    role: context
  - path: pages/traits/morphology/false_branching.html
    sha256: 72b0e4de4d4f7c0062c2ef69d5a2f7e7fa9c8357dafb4760f72a7857f73f456d
    role: context
  - path: pages/traits/morphology/ferrosome.html
    sha256: c8070cba5d7c572041f104642969de37c16f291e5634d2f11f688c267e0b973c
    role: context
  - path: pages/traits/morphology/filament_shaped.html
    sha256: 665741e98b35d9f7a63e20e739781edba47a20170eed3595d530151d0c9bb974
    role: context
  - path: pages/traits/morphology/flagellar_arrangement.html
    sha256: d43b51d567ad94b0711f970aaefe09c210213a2e1c0427a67aa95572fdf93d8c
    role: context
  - path: pages/traits/morphology/flagellated.html
    sha256: b3125da55e52779bfa7e1c978fac2baca6f86decc3bb2ab66c57fbc83786697d
    role: context
  - path: pages/traits/morphology/flask_shaped.html
    sha256: d67fcc58a411fa79b2425cd65e5b433af04891daeccfda157b0bc9c56f8398a2
    role: context
  - path: pages/traits/morphology/fungal_adhesive_column_trap_formation.html
    sha256: d0e9aff08fa8d94cd77ebb89399d44aba92832da55f12ca0c7003aca487052af
    role: context
  - path: pages/traits/morphology/fungal_adhesive_knob_trap_formation.html
    sha256: 10f7b7e2e3e11904d60f3d202c088bdb476984e383ef9bf411ce6db99d28e9eb
    role: context
  - path: pages/traits/morphology/fungal_adhesive_net_trap_formation.html
    sha256: e18d45cff13a54543c5c715ec23775de5ee4bd5da64a997e1f02bcb780c9c60d
    role: context
  - path: pages/traits/morphology/fungal_appressorium_formation.html
    sha256: d25135ed071b54410d17419bab1d1240817703992de31a39cbf5413bb779921d
    role: context
  - path: pages/traits/morphology/fungal_arbuscule_formation.html
    sha256: d0fc3c71ccb07aae15286a172928029fbb94372003451e669223ec8ec92080d1
    role: context
  - path: pages/traits/morphology/fungal_auxiliary_cell_formation.html
    sha256: 749332f7a2abf20827226ef6215d1363b747d4c774d57a63b418d674c29618c4
    role: context
  - path: pages/traits/morphology/fungal_branched_absorbing_structure_formation.html
    sha256: f4c7e46cd9fda6d54fb33e39725faf66c9ed50a6506175b611db4fcef4885bb0
    role: context
  - path: pages/traits/morphology/fungal_chlamydospore_formation.html
    sha256: ae23b80068f9a4d53b7d52d136c506c25dd58b3c001a512c935768be4d2ab516
    role: context
  - path: pages/traits/morphology/fungal_conidiation.html
    sha256: 0d374c83da9ea7d30bb06e0ca97c81c54be905bc8fd45ab6934868b6c980d025
    role: context
  - path: pages/traits/morphology/fungal_constricting_ring_formation.html
    sha256: 2e8e7b2e611b8a52e127a37ff2550b74e2ee89c1a14bf4efcd9174cd635f24c4
    role: context
  - path: pages/traits/morphology/fungal_hartig_net_formation.html
    sha256: 10a45a98d2487d7833b58e52b77bd1157d47263ca30203fb68350fc51553766f
    role: context
  - path: pages/traits/morphology/fungal_internal_mycorrhizal_vesicle_formation.html
    sha256: 00007b586475a9f916fa0c558803d1caca26b48a8f1ff3c9aaca9401519682fd
    role: context
  - path: pages/traits/morphology/fungal_mycelial_cord_formation.html
    sha256: 3b9e3735df05e36bb6587abe5514926ee5a0edc53f100127cf82c213fb594a1e
    role: context
  - path: pages/traits/morphology/fungal_nonconstricting_ring_trap_formation.html
    sha256: 2ce357be0b14a00fc14ff544cf027e1bed9cf5b68acf039657228be083c41e51
    role: context
  - path: pages/traits/morphology/fungal_peloton_formation.html
    sha256: b1fe75e35a0e91ac346770701fed37290fd341e31948d274bb45d220c5cef8c4
    role: context
  - path: pages/traits/morphology/fungal_rhizomorph_formation.html
    sha256: 4444554dcaec904e170785d484128b984c1e88f716cddb567c27c1444566099c
    role: context
  - path: pages/traits/morphology/fungal_root_mantle_formation.html
    sha256: 9a23bec5578012e0057072c8264f848995168c4baf216a271a5cb270bcb3a0be
    role: context
  - path: pages/traits/morphology/fungal_sclerotium_formation.html
    sha256: 05b82f2afdd30e36491168e12335f0d9d8289948c2ef1e787bd02448f4635783
    role: context
  - path: pages/traits/morphology/fusiform_shaped.html
    sha256: 4a2561b3cb7728c9421c2a6bc2de410141d3a8c67604124f103e260f8765b841
    role: context
  - path: pages/traits/morphology/gas_vesicle.html
    sha256: 08fa7d7a196424e65e6b301285ddff029c7a4de7858975c3284838f3aa89f8f8
    role: context
  - path: pages/traits/morphology/gliding.html
    sha256: 9a185a96d5f551659f549fd380b291c367d404a83a8345de594bd3b5d5c6fa8c
    role: context
  - path: pages/traits/morphology/gram_negative.html
    sha256: e7199f9b7f9b9cad8d67d2160d6e1007e87068766cd15eaa0ec8f31519c1b5b2
    role: context
  - path: pages/traits/morphology/gram_positive.html
    sha256: 588b58640ed8a01a9011f8c5430472875e9aab4ffd7e217fc1465895a87e4b45
    role: context
  - path: pages/traits/morphology/gram_stain.html
    sha256: 53cf20f262fa0087a1bedca2c32ff5bb629a75264be66a0aea7e726cf1576cd8
    role: context
  - path: pages/traits/morphology/gram_variable.html
    sha256: 0b651b3191e06808ccab096d5a9f195a650447d633485241b7a3296d6b4e02fd
    role: context
  - path: pages/traits/morphology/green_pigmented.html
    sha256: a20da7fd6248763ed6f8843e080aef96639fa0fcad10fb8ba9b3bcd4cc95bb7b
    role: context
  - path: pages/traits/morphology/helical_shaped.html
    sha256: a4cfc4080b72012e2efb5006df443c3fe286e1fa8658d009e80037a27183f177
    role: context
  - path: pages/traits/morphology/heterocyst.html
    sha256: dc3b4f89bb21b6f8787d1b67632862b3473995cd068a680c98e93b5796bea696
    role: context
  - path: pages/traits/morphology/holdfast.html
    sha256: 16c613d0006c619f30124a38dd43246cf52950072f31b22d1509fb4934c9ad4d
    role: context
  - path: pages/traits/morphology/hormogonium_formation.html
    sha256: 65df2ce54a07b02b6ecbf3e204992bb0ddc953d171babf4d7323a2d6e240f80c
    role: context
  - path: pages/traits/morphology/intracellular_inclusion.html
    sha256: f5399ad2fa51d6fcc0de2d4d8135a6e5f44639f54ffd272d6837186ee41dc058
    role: context
  - path: pages/traits/morphology/irregular_shaped.html
    sha256: d87e78e3341e1c0e7a6531d07bdd02c808cce89a8a2b5c7b73cbb33f2131e910
    role: context
  - path: pages/traits/morphology/lateral_flagellation.html
    sha256: 93a962fc2c8a5edf9cdebb6d5c211f70eb463546be405bee5dacb24802930685
    role: context
  - path: pages/traits/morphology/lophotrichous.html
    sha256: 8501d7c226078ad9e2d78cb14795166ded7b2f23f8eb6b945f58200ec372fc8b
    role: context
  - path: pages/traits/morphology/magnetosome.html
    sha256: 3bf4620c670392b2d53c84e84ff8a93b12d91d89fc9b910fee71706a5371ca3f
    role: context
  - path: pages/traits/morphology/microbial_haustorium_formation.html
    sha256: 84f6eeb077b41bdfb09e584ae9a1e68055aadbea734610fbc51eb6a2da2d45a4
    role: context
  - path: pages/traits/morphology/monotrichous.html
    sha256: 491f293e4e4ade873bef3c97930a92531548a02f44d40b6fd7ce4bbe5443c187
    role: context
  - path: pages/traits/morphology/motile.html
    sha256: cb3827c27d586bdf9da079e4157ff3fddd20a5d158a021b491f07ca959480c2d
    role: context
  - path: pages/traits/morphology/motility.html
    sha256: e0be6b9ba0cf15192df117ad57b5e552241a8ab14ff0e54e110fd4bc39f6a4ad
    role: context
  - path: pages/traits/morphology/mycelial_growth.html
    sha256: 8e0f7867819f694606fddcd661494957020cf4801bde087d6a5d373479678ed7
    role: context
  - path: pages/traits/morphology/necridium_formation.html
    sha256: de82ac4c5403ca8eca50ef7b4a7da04c8f986bfb7ad4cb39a4ce1802ffe675ba
    role: context
  - path: pages/traits/morphology/non_motile.html
    sha256: f5006d60447d01b619de24d757951c182e45db878c8212b90b8b4cb5fb377ac3
    role: context
  - path: pages/traits/morphology/non_spore_forming.html
    sha256: 6d504bf1ef3f3df5bee622a46bc4bbc3c619f0897beea926a33f01a1f9d7c33f
    role: context
  - path: pages/traits/morphology/orange_pigmented.html
    sha256: 348b100d7890262d96ac3b13cec828365d72f774c45bdb087267dd3437e60bd1
    role: context
  - path: pages/traits/morphology/oval_shaped.html
    sha256: 8a21bb002b3f0d041b47e8017b235f755ce8e1c8327f19fc637c5fef3c6849cd
    role: context
  - path: pages/traits/morphology/ovoid_shaped.html
    sha256: 79f52373ea1085ab63e4760bc20d9b45919c9592f2a87b448af51b27b5699377
    role: context
  - path: pages/traits/morphology/palmelloid_formation.html
    sha256: 8920fdd7f7c9fae3f56f41f986434ea96385e8fd5a63d691a68c136734259a29
    role: context
  - path: pages/traits/morphology/peritrichous.html
    sha256: 92346174caa447fd7a4ca915bf69d78b884b92b2ba96879a9c1d9fcb6b11f25c
    role: context
  - path: pages/traits/morphology/pigmentation.html
    sha256: 35b891e81081ac9789e121a9a9dbdeecb9cdad7d0253293a0fd563295c55304e
    role: context
  - path: pages/traits/morphology/pink_pigmented.html
    sha256: 83ed295de5bf200792ebb278a24f6fb3bfb381bb05c82cfd98f38895703cda56
    role: context
  - path: pages/traits/morphology/pleomorphic_shaped.html
    sha256: f72a374f0b69d34466af70589f19ad836ce45f43bcda94bc3b49e0ebaa4b41c3
    role: context
  - path: pages/traits/morphology/polar_flagellation.html
    sha256: a699cb2066db0b5b42e26e7f46fd2c441358e2fa08edca65fbf964349f9b2e54
    role: context
  - path: pages/traits/morphology/polyhydroxyalkanoate_granule.html
    sha256: 9a25ff0dd41a87f96848bdc3e8d28327070c35962f7c8b35a15f4fe5a76d93d3
    role: context
  - path: pages/traits/morphology/polyphosphate_granule.html
    sha256: c1502dfdb4bf47c45922803f67255d943cd03bf53afb2d4c07b52f3a4e04f4b0
    role: context
  - path: pages/traits/morphology/polytrichous_flagellation.html
    sha256: a15181515089749fc742ae341107ee4688c54fb87942e7bc416fc14ee5bde491
    role: context
  - path: pages/traits/morphology/prosthecate.html
    sha256: fa04226ea55a50e8cd4395b4e63d3e682db7bd49c832fa72919ffd9d91a5fc8c
    role: context
  - path: pages/traits/morphology/pseudohyphal_growth.html
    sha256: fb67a82dc18341aa395cdad4d3cb8043cfb1d9e72573da5c38d852e097108551
    role: context
  - path: pages/traits/morphology/red_pigmented.html
    sha256: 34e4569a0006063f28393087627997bc82247a4f0621d54c270b4518ac4ca508
    role: context
  - path: pages/traits/morphology/ring_shaped.html
    sha256: c8fe76aaba9df5ba827be52cf492ef6c1249324599bfb4ac21cf8a49459f80d3
    role: context
  - path: pages/traits/morphology/rod_shaped.html
    sha256: c05f9fd687a6cbaea0ecf71c2bce19fc171f0a398e3e2afbf5e5397de342d88b
    role: context
  - path: pages/traits/morphology/rosette_cell_arrangement.html
    sha256: 7df106429c1d39959702174772c515a9fcd074df56700d54869224cca6cf3fc7
    role: context
  - path: pages/traits/morphology/s_layer.html
    sha256: 3d069c7728ecd847201571a19c3eb5c359c871b1915e8c0ef8152602094e9524
    role: context
  - path: pages/traits/morphology/sarcina_arrangement.html
    sha256: 7179e27212654c75fe34a4a189046322279781fd6bc31317e0ae8f51a26f481e
    role: context
  - path: pages/traits/morphology/sphere_shaped.html
    sha256: 31462af47b173385d3a01538ceb8839b2a09534ccf9b523879cc5db864c8a2b2
    role: context
  - path: pages/traits/morphology/spindle_shaped.html
    sha256: 43424ed4663eb56872bdcf03e98bd879fdbec00ccc680fd856f0ee968df937c4
    role: context
  - path: pages/traits/morphology/spiral_shaped.html
    sha256: c91640ce1071fddb44e04e4799364cdf4691cb57461976b320a12c32af555bff
    role: context
  - path: pages/traits/morphology/spirochete_shaped.html
    sha256: a07204ef9de33ce02a539404e8e3e6d952db3b4cb3856918cd5c80a3a2b1f375
    role: context
  - path: pages/traits/morphology/spore_forming.html
    sha256: 088336978d32ee13866b3e527cabb6199b79cda07478249e7a5afe2f5c5f0f7d
    role: context
  - path: pages/traits/morphology/spore_shaped.html
    sha256: 62f83d3d84d8a73f8e6bfa42e4979507c3c7b81e2783eebcde2fde413bdaa473
    role: context
  - path: pages/traits/morphology/sporulation.html
    sha256: cb56b0cb76b9d0a93a58dd6a84f347ebb86c951475ab9ee1ee0ce61941d45aa1
    role: context
  - path: pages/traits/morphology/square_shaped.html
    sha256: 697403a254c99cad9c891ece116888ce98472ef0425d2b4582e4d2ebe69b206d
    role: context
  - path: pages/traits/morphology/staphylococcus_arrangement.html
    sha256: 3fb83ebe17420e9f7f0c1cb7d778884aea5ece6a51e09203ab574e2973418ddc
    role: context
  - path: pages/traits/morphology/star_shaped.html
    sha256: 3d96b712c2d18dee95ab10b4de52e5c7ec670e1aaaceb1deb24e6b0537c12497
    role: context
  - path: pages/traits/morphology/streptococcus_arrangement.html
    sha256: ef77c3e9d9abc2fea1b6f6621d5d201cf9d5e3005373b887e6ed545f27a8c150
    role: context
  - path: pages/traits/morphology/subpolar_flagellation.html
    sha256: 9bcf3799e0195839004b2c233f97372b915dbc06a86aea7db925b92ff5b82d83
    role: context
  - path: pages/traits/morphology/sulfur_globule.html
    sha256: 4bccbd252b1722eb42a06014b72b47f4f5f0d27b073fefeed706501a16022968
    role: context
  - path: pages/traits/morphology/swarming_motility.html
    sha256: 13e5c92734e718985f7066a31a9739f505739db17c73ef70bc34ec9a5a9fbbcc
    role: context
  - path: pages/traits/morphology/swimming_motility.html
    sha256: 8ee015560774b32bf68f1f9166952d773ae687c83da488239f848af1ba47bc25
    role: context
  - path: pages/traits/morphology/synnema_formation.html
    sha256: 9f2722466ced0ad622c8e1e05e475a3bcd54dda5b47cb27bc285e4020cb08092
    role: context
  - path: pages/traits/morphology/tailed_shaped.html
    sha256: 270ec8e90700cab181d75f5e701157d2561b3c8f98a4a355131a1b3a97d83abb
    role: context
  - path: pages/traits/morphology/tetrad_arrangement.html
    sha256: ca133844643bfa1a7b506bfdc6535a42c1acb56a8ad92eae2e1b14d9e4a1cb4f
    role: context
  - path: pages/traits/morphology/triangular_shaped.html
    sha256: d553e69cad60e6fa619ebd67a2a5d4d0ad90602c4295324cc53f060cf7446d2f
    role: context
  - path: pages/traits/morphology/twitching_motility.html
    sha256: 26132375c467eca146c86a5634510f0d1bc28003fc0ca5248f6c98c674062f19
    role: context
  - path: pages/traits/morphology/type_iv_pilus.html
    sha256: cd68c16a56562a9059b45fa096ab5e6e80c0ca023be3341021d1b6c01836254d
    role: context
  - path: pages/traits/morphology/vibrio_shaped.html
    sha256: 3b2133f08002be6a2e8530397eaa123ea80bdb7302d399da36b177604aea5902
    role: context
  - path: pages/traits/morphology/white_pigmented.html
    sha256: 9c325ee1e502616e7b43cc6c0e9a314f69d79e5a51f37de1a7de50b171405fe4
    role: context
  - path: pages/traits/morphology/yellow_pigmented.html
    sha256: 736bed39965b13de1488afb82cb2da0c3b494623410336f334f3f959ece6a9ee
    role: context
  - path: pages/traits/observation/growth_nacl_observation.html
    sha256: 4221b1771610dc190a53232b6247e102cdef246598757a32d823821b042d260b
    role: context
  - path: pages/traits/observation/growth_oxygen_observation.html
    sha256: 520baac06ae7a9ca04b336c47b27e0cad47ea7f52d29ec06f75fecd8da927373
    role: context
  - path: pages/traits/observation/growth_ph_observation.html
    sha256: c1ccd6571a2b6a578ecd364a1def2195595bcbc286364ae8e5aca58e129e25f0
    role: context
  - path: pages/traits/observation/growth_temperature_observation.html
    sha256: 7d571e5909991fe6387877c02e300948b0ecb3203f4c8931e34b162ea64cfaca
    role: context
  - path: pages/traits/observation/nacl_delta_observation.html
    sha256: 85cc0cae906058c8aa190fff37917ed272caf55fb391e99da90b9a8e2a6b1a81
    role: context
  - path: pages/traits/observation/nacl_observation.html
    sha256: 59f5840c98a1f97561e0a29eba9f3c6ebe5a6ebc3cba5f6b4f55c52a5aec5a72
    role: context
  - path: pages/traits/observation/nacl_range_observation.html
    sha256: 30c8d9c3104ccaff575c2cf1b27a79c9bf0fb1f928c0969440803c680d94cf0e
    role: context
  - path: pages/traits/observation/optimum_nacl_observation.html
    sha256: 8b50ad1ad6a3ca707ba06ff85cb111d30dd5cbe9e379bc5c9c7aac40952b6b12
    role: context
  - path: pages/traits/observation/optimum_oxygen_observation.html
    sha256: f9fb578fb6bf386db06ede67cfda66f061064cb7fb3c5e8b883576c24fbb0ae0
    role: context
  - path: pages/traits/observation/optimum_ph_observation.html
    sha256: bf93447e84be92df8b06f4fe152fcc128c7e11b1df6f824ad03d54636286cf4b
    role: context
  - path: pages/traits/observation/optimum_temperature_observation.html
    sha256: d52c08596a2a6ede59c4cd66730a9e729301d7a5a5dcf6b3cdb28f7483184c2d
    role: context
  - path: pages/traits/observation/oxygen_delta_observation.html
    sha256: d254c7fa71a56a29269a81a369960547d31569921fc6a472426df5136290a408
    role: context
  - path: pages/traits/observation/oxygen_observation.html
    sha256: 2544fce6aac90be57054f76363ed0cd6a29118fe305f27be750dfcab9542fb62
    role: context
  - path: pages/traits/observation/oxygen_range_observation.html
    sha256: cdabdc926d2d97861cabec664ba6d1e7fd840e555c23fbc97fbd459d34279148
    role: context
  - path: pages/traits/observation/ph_delta_observation.html
    sha256: 80f6c343f91f824b254a6db79ab8d29b75892fbdc3abeeb7e9afb2b679bfb8df
    role: context
  - path: pages/traits/observation/ph_observation.html
    sha256: 8f8d4c3b7f496b602f076ec2d1b0c42e78fccb4054fc5157d05d79caf73dca25
    role: context
  - path: pages/traits/observation/ph_range_observation.html
    sha256: 36a3082fd35a49fe12a6b7cb9375dce78a104f522755c13a48b3dc14624c9092
    role: context
  - path: pages/traits/observation/temperature_delta_observation.html
    sha256: c4c695edd987d4239e8797efbab14d6767374742a63b2212cb7ce65123e24a56
    role: context
  - path: pages/traits/observation/temperature_observation.html
    sha256: ca22af8e73f396301ef8665d3d98af2c671245093de60ba00d63845226f2df44
    role: context
  - path: pages/traits/observation/temperature_range_observation.html
    sha256: b4bca3364a6820d5b8fdb08d1ed3d28197d69571fe29f7a8a931469bf0fdce41
    role: context
  - path: pages/traits/other/catalase_negative.html
    sha256: c606afc94741b30edf9aa77e9f755f94b7e721b7b257a0ae3153dd5ac94ea73f
    role: context
  - path: pages/traits/other/catalase_test.html
    sha256: b5447248d96aa847ee1597a2b34b396af0402325d63ab68fa1f054ada090c20f
    role: context
  - path: pages/traits/other/circular_colony.html
    sha256: d5618f6b3096077f6887af9d00515d631d2d3b1398e3e03e2bb8939b29fa2286
    role: context
  - path: pages/traits/other/coagulase_negative.html
    sha256: a8d5394be767a59da805685ba35113b276f7b94e9a3c7ff89e6357b97dedadb8
    role: context
  - path: pages/traits/other/coagulase_positive.html
    sha256: 792e0d0750f6115da33208f114210f2bb1821ee344b1e1ffe3c0584a497d1a3b
    role: context
  - path: pages/traits/other/colony_morphology.html
    sha256: b3b933a09d0c45268d2fe700efcfeea78331a022c673815512fec1387a86a747
    role: context
  - path: pages/traits/other/colony_shape.html
    sha256: 5c14ff259b8cc68b9bc6fbcd44c4a31b36f5d4c909db9ba224bd4b504aca55c2
    role: context
  - path: pages/traits/other/epibiont_phenotype.html
    sha256: 5edfb62d461f457ed0ab9d7708ec0efc94ea3e725e62264e3e438754e2d47143
    role: context
  - path: pages/traits/other/filamentous_colony.html
    sha256: c6ba5429b0c61796f709316a37bf8eee6f4d8e33cf7f4e0ae6ed0302f59f3449
    role: context
  - path: pages/traits/other/fried_egg_shaped_colony.html
    sha256: 1838f9e0681e2b0d8a90205f150804afa6a2bd15bd707531f5c65c1c10c6cd5d
    role: context
  - path: pages/traits/other/generalist.html
    sha256: 4c31288e3f5bb5bc2f14962956eb833d9175da5fe7b42996c8128682bdfd150f
    role: context
  - path: pages/traits/other/hemolysis.html
    sha256: 73f22462480a6650aa016dbf8e122bd89f12b38f14b4316ef11baad02b4c7dce
    role: context
  - path: pages/traits/other/hemolytic.html
    sha256: bb074d0580dbf970aaf1f138ecbb23b163cc8db520d80def20005d507fc4948b
    role: context
  - path: pages/traits/other/indole_test.html
    sha256: c8963327c39db770774e3f139dee297ed825cb0c7d6dfabb95c9ff8e05a9bb07
    role: context
  - path: pages/traits/other/indole_test_negative.html
    sha256: a15480e14e4b7051704f13bce6789596d8d8ab3d1d99ab661899b25ee57c8e81
    role: context
  - path: pages/traits/other/indole_test_positive.html
    sha256: 3943d51aa9a883f4998f5c9da24b03dc1c9014d42d870ef3abfb47d9c9efb162
    role: context
  - path: pages/traits/other/irregular_colony.html
    sha256: 14075312d2898951c4a4d4ef3571678d0cd96058ddf6b5d8fa037d85281a8954
    role: context
  - path: pages/traits/other/methyl_red_test.html
    sha256: d8adac055055636fc029795bc676d43b0e137975e92d815b6c0d2531d588f45b
    role: context
  - path: pages/traits/other/methyl_red_test_negative.html
    sha256: fc1cd9422479beccb159da19be0327c2fe384a81eeb1bcae87c03b7cf0246e06
    role: context
  - path: pages/traits/other/methyl_red_test_positive.html
    sha256: 1d03a7a4cb55f84cf0963d876ba63d26a5dce7c01f216aa5c3bb5f51ebcc1adc
    role: context
  - path: pages/traits/other/non_hemolytic.html
    sha256: 10fe876868ff17abb2caa0e1d5d0dc0d654560a0e09238813e477c3d7485a293
    role: context
  - path: pages/traits/other/osmotic_tolerance.html
    sha256: 780aff8174a24b8aaea446e0a04f11d7171a158b08851bf4bf8f115777c13223
    role: context
  - path: pages/traits/other/oxidase_negative.html
    sha256: 93a01bce29961cbf090a4b4af0ba4aabe4fe38aaf75684b06d5c6a7b19b32b80
    role: context
  - path: pages/traits/other/oxidase_test.html
    sha256: 3defa82dd7ccb3c19c35a0bfa022f3fc059b578cb8a9ee3abd5d5a694a8ef8e1
    role: context
  - path: pages/traits/other/punctiform_colony.html
    sha256: 7999794e69e92562b3b5b3ce5f1af89ff8010b2f22d66aeb1edd28ec76f1f22d
    role: context
  - path: pages/traits/other/rhizoid_colony.html
    sha256: badfd387c96eb5e186e02cc58f88733ff7a6010849d4c6f4a76d55cde940f0f7
    role: context
  - path: pages/traits/other/specialist.html
    sha256: f3587a2d97bbb9a35f4c6ae635d1acf9d669394b787864fd9699fcff14f5ee79
    role: context
  - path: pages/traits/other/urease_negative.html
    sha256: 7e12efb40a236495df8efb627a277f8f699be7cc07da0c6da18eeb0adb5a1251
    role: context
  - path: pages/traits/other/urease_test.html
    sha256: 45b8936605b8751f98629629c5f2c481f2df0ca13031917bc9079488d14f96c9
    role: context
  - path: pages/traits/other/voges_proskauer_test.html
    sha256: 282426b07e9603b9b43b7d7b32721a31dd058bb88183f3c1f7f2a632f49f6997
    role: context
  - path: pages/traits/other/voges_proskauer_test_negative.html
    sha256: 2fe00cd3e97c999a5bcd215b106ade53c02589dd7a8e7d79adf880f27d076c6d
    role: context
  - path: pages/traits/other/voges_proskauer_test_positive.html
    sha256: 4ae0be2499596d9ea2f772e7045aa4473944513bf27af1287ce171cf9bc7b593
    role: context
  - path: pages/traits/physiology/acid_phosphatase_activity.html
    sha256: f19d1a5d1a1f893ea9763905ba7d2463af23d453c81ba376ef6eda97e4aa837c
    role: context
  - path: pages/traits/physiology/acquired_stress_resistance_memory.html
    sha256: 62f05a6f0148324f8286a94af53bf0f3054c94328a550022c2b5ea78be7cce1f
    role: context
  - path: pages/traits/physiology/aerobic_anoxygenic_phototrophy.html
    sha256: cf04704eae2e0858dfeeb7679378efc60df349d8fb94ceecc74c1fa000222739
    role: context
  - path: pages/traits/physiology/aerobic_overflow_metabolism.html
    sha256: 80af1f205cc26e258d08dbc5368d5959c759899430c0b9da0333387b5390c2f4
    role: context
  - path: pages/traits/physiology/aerotaxis.html
    sha256: 44e5e16100b88aa50b06e2d61a2d6d177c326fac1e90c9b9e4487b974ae4060d
    role: context
  - path: pages/traits/physiology/aerotropism.html
    sha256: f0e3216cc3d1c3b5de945b710d0bd4bf9f1b89e9ea92eb3e396a4a0c03a33c41
    role: context
  - path: pages/traits/physiology/aggrephagy.html
    sha256: 41ea257b4d87454171a0db12f08917c4485f891d91b0371532d30417e6c866f8
    role: context
  - path: pages/traits/physiology/alanine_arylamidase_activity.html
    sha256: 24960caeb5ce84453f022ca4f420980f145ca974bf8bf33859a94d45b69f01a6
    role: context
  - path: pages/traits/physiology/alkaline_phosphatase_activity.html
    sha256: 45862c16f0b65418e7a3acd5a2b19f4b6ef9599f3c97a31159e29387e6f00f82
    role: context
  - path: pages/traits/physiology/alpha_chymotrypsin_activity.html
    sha256: ff8c3f11a3f9012fdd1f713bab57d79b716e3a618eb686e6911a1504b2db7359
    role: context
  - path: pages/traits/physiology/alpha_fucosidase_activity.html
    sha256: ec38012344429a7e0914761f08152fedc4133374c416660db579a46235d64207
    role: context
  - path: pages/traits/physiology/alpha_galactosidase_activity.html
    sha256: c6c19a8e3026ba88154780cf147a42a170e35c7636b51f384bc12ad0881eb856
    role: context
  - path: pages/traits/physiology/alpha_glucosidase_activity.html
    sha256: 7ae530d5e4989e67b9e9e86481df8107555c0989e2df52ab3c232915e2730733
    role: context
  - path: pages/traits/physiology/alpha_mannosidase_activity.html
    sha256: 43fa8480575a962240863ca1b28af65c424c5bf2055dea4266bb0b226faa84c4
    role: context
  - path: pages/traits/physiology/amylase_activity.html
    sha256: e42f3d2888c5e52657c580f4335c551fafb050001e19f2e26a84908a0272d7d4
    role: context
  - path: pages/traits/physiology/anisogamy.html
    sha256: dc8332c2095d7c5149c991bde1237414355724056a2bb2dff0dc36780e9630c8
    role: context
  - path: pages/traits/physiology/antibiotic_resistance.html
    sha256: 758f0a146db74480aaf70f8606a2b0033c165d486e130e3c577506f2a797d9c6
    role: context
  - path: pages/traits/physiology/arginine_arylamidase_activity.html
    sha256: 771a93745d012b10b101075d66fe087c0f3bd1e75e024500c2d0a3024b103dd2
    role: context
  - path: pages/traits/physiology/arginine_dihydrolase_activity.html
    sha256: 83f36b9b9a180faedcfcd2a48bc80042ba698624bc7d11c02a69b9e64ed0cacb
    role: context
  - path: pages/traits/physiology/autogamy.html
    sha256: af9b36d0b8d21f0685ef1f6a2e0074568d2b4ab594cecddbc0b9cb1d7397a9e6
    role: context
  - path: pages/traits/physiology/automixis.html
    sha256: 83750a47bf45256f037a8c880c539c09d1842ba4336003f07e3b13cb99daadca
    role: context
  - path: pages/traits/physiology/autophagic_glycogen_degradation.html
    sha256: 6616b4682772520cc4ee5061d6d3da69103cbed5bae856fd660391779a69c5e9
    role: context
  - path: pages/traits/physiology/autophagy.html
    sha256: 6e2e5dfa8e157ebbb07bf2ef4ab72a5bdcfbbf29f215cd0c5257e09a20209305
    role: context
  - path: pages/traits/physiology/autotrophic.html
    sha256: e98bb5a334f6af7e7e18d51f9dd147131548e3124159dfe09ee6894e6a38478b
    role: context
  - path: pages/traits/physiology/bacteriocin_production.html
    sha256: 11f4304f996d60ac770f6e161a5e1f9ce0599f64b3f485270e5107e1917762e4
    role: context
  - path: pages/traits/physiology/ballistospore_discharge.html
    sha256: b1dcae7d8bf1707fb3cb839e9d710ff63864660cedf2cf5952fa05d3cb9aa6a1
    role: context
  - path: pages/traits/physiology/behavioral_habituation.html
    sha256: 5ba5c51678f76c5bb1c7ec7a0598d1a994a35ad2adc3c813d2f430dcf35bd7fd
    role: context
  - path: pages/traits/physiology/beta_galactosidase_activity.html
    sha256: ebc2453a2939ec20725055f75d65524c1aa00273150a53eec484d6a405202331
    role: context
  - path: pages/traits/physiology/beta_glucosidase_activity.html
    sha256: 647120f10343ef874bf93ec4397c42c8e3749bf2c34b290c47e29260abdafd91
    role: context
  - path: pages/traits/physiology/beta_glucuronidase_activity.html
    sha256: 0281c203695fadb7aa7a3a80f251c585adc067b649b333cf5fd4780d9ade54ca
    role: context
  - path: pages/traits/physiology/beta_n_acetylhexosaminidase_activity.html
    sha256: 2c92051fffb7b2428154206fd9d21b6f335f1ecfb37fe5cbcddbdd7225f8c41d
    role: context
  - path: pages/traits/physiology/bioluminescence.html
    sha256: aef6d112dedd091c61471fe7d32a206de44560a59c566c0b1d0461f3f6659b4f
    role: context
  - path: pages/traits/physiology/biomineralization.html
    sha256: ea4d77dd03b57ef0295406a90d27f286aa26905905d236f32532c22ae164b865
    role: context
  - path: pages/traits/physiology/bipolar_mating_system.html
    sha256: 7fed8452d5cdf1a2e0fb7e2bd1c22e40d0860e7a7f05b93b34b7d0cb45ac7fae
    role: context
  - path: pages/traits/physiology/carbon_source_memory.html
    sha256: 57596c4faed666b26d9182cb57e7d09220ca7b770cc841a2d9eb8f300453ceb5
    role: context
  - path: pages/traits/physiology/carboxydotrophic.html
    sha256: a686a84ff2e7b3f3a077f4f9e7dfe77176f7ddba4daabbff86857ec99b93a517
    role: context
  - path: pages/traits/physiology/carboxylesterase_activity.html
    sha256: 2c07cefafe08693973ca2cc946e6c5dfa228b294fe158f4c9ca8bcb6baad5a42
    role: context
  - path: pages/traits/physiology/caseinase_activity.html
    sha256: 49eabbfe5d0dfc8dea79059f3ac0d924fb1b5dc67008536cfa6e12c103d2d853
    role: context
  - path: pages/traits/physiology/catalase_activity.html
    sha256: b8e44a2aa863447edb4d23ad6a2caec818f4d90b9eb2dc1ac58f4ac04c9bb2b4
    role: context
  - path: pages/traits/physiology/cellular_buoyancy.html
    sha256: 348a467e31cee6148f57a875d0cdf347c9d83e4357afc12f41a064706d0f5e7c
    role: context
  - path: pages/traits/physiology/cellular_rejuvenation.html
    sha256: 870d51c2ce74bc2f296a9774bdcf29512794749729c94ef94bf6a3ec5e8850af
    role: context
  - path: pages/traits/physiology/chemoautolithotrophic.html
    sha256: 7e2749c6a0ff65edbe9ab3f30d2c26c0d3e4c69efb98a261c93d782f724f8ce3
    role: context
  - path: pages/traits/physiology/chemoautotrophic.html
    sha256: d04afb23e28e213479fb86d321eeb867837f441defbdeaa1e52c39697ac20f7d
    role: context
  - path: pages/traits/physiology/chemoheterotrophic.html
    sha256: 02cec73986990c4bef35d5fb71e05951a9225bdc52e35363be0da60e19f9df48
    role: context
  - path: pages/traits/physiology/chemokinesis.html
    sha256: c5824a1331fca2f9b3e87613f9ef4573b98028f599b9f177b16e5b87329a1f1c
    role: context
  - path: pages/traits/physiology/chemolithoautotrophic.html
    sha256: cc27855f6541c09fd9d1822f25896069718a6d84e7427f0375e0897305e752ed
    role: context
  - path: pages/traits/physiology/chemolithoheterotrophic.html
    sha256: 0c3a33b80145cdbce05fbf710198d85492d5a880a8be969f488f58f062c39b53
    role: context
  - path: pages/traits/physiology/chemolithotrophic.html
    sha256: 4fb3b59e4974b293be0fd9d09165cccb326c0aab90aff61629f02a9edea2d6ef
    role: context
  - path: pages/traits/physiology/chemoorganoheterotrophic.html
    sha256: 4c00b3977018c56b0f7b2ea39dc1e3df50c0af433b0ab0b7c5c757acb952a2c3
    role: context
  - path: pages/traits/physiology/chemoorganotrophic.html
    sha256: 565ce9a0132f2da6a1a8613e30b80141ac29ac71985b0c4640062c33ef6d6484
    role: context
  - path: pages/traits/physiology/chemotaxis.html
    sha256: d334646330e6b9cff5812a46ad3c7e11b01b09f828f81047fc72d4c2116dcba1
    role: context
  - path: pages/traits/physiology/chemotrophic.html
    sha256: 1a2dfebea210f6fa6cfc409092dfc9e9654282904763d6610b54c070005b07cb
    role: context
  - path: pages/traits/physiology/chemotropism.html
    sha256: e2c9dd32a56e9f11e6ebecc3681276d30bc2deddca44674207356d1785980a38
    role: context
  - path: pages/traits/physiology/coagulase_activity.html
    sha256: ffb83e27f61d3e0e68e0cec944d12aec4be06813854d33d44f58447cd878c16f
    role: context
  - path: pages/traits/physiology/coccolith_production.html
    sha256: f92194bbebb723f7ed7c59271b8b1e89c5709113ae68625a41430c3feaa09729
    role: context
  - path: pages/traits/physiology/cold_shock_response.html
    sha256: 12b572f74d10dacdabcf6e56db015b1851b3f77fa2ac5a61b5a1f73bed2033ca
    role: context
  - path: pages/traits/physiology/contact_dependent_outer_membrane_exchange.html
    sha256: ebd294589a9dd6908d5fedbd4a50152894892b5efc9e2e39dafd3f55ff331efa
    role: context
  - path: pages/traits/physiology/copiotrophic.html
    sha256: 652444eda3c30cbe021cd04d67d9eab971322c57643b1fc6cc623ea392f304a0
    role: context
  - path: pages/traits/physiology/cue_triggered_environmental_anticipation.html
    sha256: c93aa2c4b288e7d0ed5bb434cbaa0d719fb62c69aecbb67bc7d078a35e4cf075
    role: context
  - path: pages/traits/physiology/cystine_arylamidase_activity.html
    sha256: 24fc82bb674e388e084620442c3646d97c0775cdc79314a59c8c2696210e6bf5
    role: context
  - path: pages/traits/physiology/cytogamy.html
    sha256: 30a19a6e40ae17d87c0fc83c7641e62a89cac1ebedb64f3290b6f47d96b8a290
    role: context
  - path: pages/traits/physiology/diatom_frustule_production.html
    sha256: c0055a5c2ee53354604646e15aaa58cf32371f1ff1ce22e82543d5efa6e118e9
    role: context
  - path: pages/traits/physiology/diatom_perizonium_production.html
    sha256: a8364b679ac25695a9347c351afbf7e83bcbe863b8e27bd573d8d5f5af051e5e
    role: context
  - path: pages/traits/physiology/diatom_seta_production.html
    sha256: 43c6152e898bb3860e573fc8c0d1fb52c96d90cc4251757aa67d2d59586ccc35
    role: context
  - path: pages/traits/physiology/diauxic_growth.html
    sha256: c3d666528d9e754ab7b2b5f04faf1fa1753f2bfe416d58b580dcec714fa0f1ca
    role: context
  - path: pages/traits/physiology/diversifying_bet_hedging.html
    sha256: 7847309956cd88dc2a2ca194791cd944711d70690d8515af83192c7f81ddfe6e
    role: context
  - path: pages/traits/physiology/dnase_activity.html
    sha256: b2491e9974368c97835799650730235eabf8d2a23f4bd86b380c336b6ce443bc
    role: context
  - path: pages/traits/physiology/dormancy.html
    sha256: 0c350bdef222241b7786bc1656a9ca7eae46952959dd88d469c202a93fa99c8e
    role: context
  - path: pages/traits/physiology/durotaxis.html
    sha256: b85d3f2d80f60e866853829cfaa0749c104e5cdaeb82419a206ccf31225fcd51
    role: context
  - path: pages/traits/physiology/endocytosis.html
    sha256: 4796b1819fe7e3eacd6aab1e4b0eaad31572f301b65bff6b232a41c684b0d7c7
    role: context
  - path: pages/traits/physiology/energy_taxis.html
    sha256: cdf980c5b9f28e4e257acbe2c32a700faf21421b066a9d01272f2053c8610f1b
    role: context
  - path: pages/traits/physiology/enhanced_transcriptional_reactivation_memory.html
    sha256: 1b8c59fa46e572b4a09a6e0a2aae4101da42a563611b9e1f449055907977532f
    role: context
  - path: pages/traits/physiology/er_phagy.html
    sha256: 298ea9cfc4a88df877bf5db24065e4c9cc61530142e371a9efe697b5da54da2f
    role: context
  - path: pages/traits/physiology/exocytosis.html
    sha256: 92e0f2d0b44bd340b4957b1b64423268cc5ee8e0e2a1cb3aaff7750445a01c45
    role: context
  - path: pages/traits/physiology/extracellular_membrane_vesicle_production.html
    sha256: 4a4f1361d1864631c1971aadc2ada9f37ce5ba32d1c88b1dc84c5887f9be4657
    role: context
  - path: pages/traits/physiology/extracellular_trail_based_spatial_memory.html
    sha256: cb8851a8980ddcf9407c6eb6b5fc8e3d7d6bed23c9d64901170b9774afb63cc2
    role: context
  - path: pages/traits/physiology/galvanotaxis.html
    sha256: 5de4991918f64ff3dcf216ad83aa732ad7711cb8320e0e67839c5a539162bef6
    role: context
  - path: pages/traits/physiology/galvanotropism.html
    sha256: 6add6b89e32daa75fa5c1c299076d1527e8157f447ae165ee6273d2382afd2e6
    role: context
  - path: pages/traits/physiology/gamma_glutamyltransferase_activity.html
    sha256: 3dbd9bac721cd4ff4aa5cf662c647f7830b97cfef9957eb2431a116112ee1fac
    role: context
  - path: pages/traits/physiology/gelatinase_activity.html
    sha256: 74f45604aa5b3ce96a33a238744e5e2b83a0b1ab1aa4404388d9fcfbbd57ee0c
    role: context
  - path: pages/traits/physiology/glutamyl_glutamic_acid_arylamidase_activity.html
    sha256: 289d7d7264a5453a14d7b1fa790ae6c65268326a97d08edacb7f449ba313b8fc
    role: context
  - path: pages/traits/physiology/glycine_arylamidase_activity.html
    sha256: 827e81b4b77e96c639392af39e00f85a8b42279e119e90d242c8fe2a2748e6c7
    role: context
  - path: pages/traits/physiology/gravikinesis.html
    sha256: 765688ac7c33d58eac3230dc9e5e7328d1624ba2f77e656eb8f6cf48dd56b143
    role: context
  - path: pages/traits/physiology/gravitaxis.html
    sha256: 1cae3ec2299be30af7c736284ee238ae3926b3abd7486a504c739691c2e06667
    role: context
  - path: pages/traits/physiology/gravitropism.html
    sha256: 5ac0aa8639191a1d5b17d4bff933d7d4b42f56b232abb78b5a8e5ea46bf8572f
    role: context
  - path: pages/traits/physiology/gyrotaxis.html
    sha256: 504f3baf5e46127546685b2a991be47d7e28f8df42cea1b92d5ceaf575402b51
    role: context
  - path: pages/traits/physiology/haptocyst_discharge.html
    sha256: 525a2b43225e67ab2ac4b96449b2337eaa05232e7f445b4f70777e6b9af3ed8a
    role: context
  - path: pages/traits/physiology/heat_shock_response.html
    sha256: 8935393662823e0f0e0b2589178837fb29e99c6e2edf99315b472f22e89d5093
    role: context
  - path: pages/traits/physiology/heterokaryon_incompatibility.html
    sha256: 3174bb4e3f8ec8991be0b3f83a45a1d22cd0e2c661f6ead387fd363c9b7bdf47
    role: context
  - path: pages/traits/physiology/heterothallism.html
    sha256: b46c0cb95ad0d6d547587b7d92b911ee6a11f49d796d44a94c67bfd83066e852
    role: context
  - path: pages/traits/physiology/heterotrophic.html
    sha256: d98e697f4d2c326cbe1b20c5264ea575959334e9723ff7ed1a62975e986fb4df
    role: context
  - path: pages/traits/physiology/histidine_arylamidase_activity.html
    sha256: b3611a036008654f8394189594da9edba1d0767817c462b52af38b2a785d91d7
    role: context
  - path: pages/traits/physiology/homeoviscous_adaptation.html
    sha256: 9ac7b0d1aaa0cdbcc427b0a623499bbc44e441187b67d8207c038aa0ca78b931
    role: context
  - path: pages/traits/physiology/homothallism.html
    sha256: ac854a9f998fd258b4bf45d3250d4ceb1fcd78593d3157615e64c5f43aa5c2fd
    role: context
  - path: pages/traits/physiology/hydrogenotrophic.html
    sha256: c87afec7dc9c1b3c2a4c25014138ba6a7ddc56529e439adafb964a4bea4feaea
    role: context
  - path: pages/traits/physiology/hyphal_anastomosis.html
    sha256: 9dbb5c10e39898ca99ffcf9e275fb7d35ff7de834e3a2be314875bd542196063
    role: context
  - path: pages/traits/physiology/isogamy.html
    sha256: 383717ba6eedf880839e4e4ee102d6cb6c0cca6b98f6a5503280db57dd1a02f9
    role: context
  - path: pages/traits/physiology/karyoklepty.html
    sha256: ef681ab8c0d1b3db3af9ec953b3b7f697fa631b88e3662c1b7e97a955b31c2ac
    role: context
  - path: pages/traits/physiology/kinetocyst_discharge.html
    sha256: 0091937c70ecd9a746658bb365890bf11b8ceba1649376bc5db8607c100448b8
    role: context
  - path: pages/traits/physiology/kleptoplasty.html
    sha256: 98ed3d38669f4ce42e77fb74996a8a230076bd0a1c72914f548614c01f677cd6
    role: context
  - path: pages/traits/physiology/lecithinase_activity.html
    sha256: 24980e6349a2fa738549f9cc1211a33e46333e608b79e4ec7a5368239a36eb02
    role: context
  - path: pages/traits/physiology/lethal_algicidal_activity.html
    sha256: a6e54a80211178bea90cca861258a584e370a0cf5326d8249cbc97cd60c46861
    role: context
  - path: pages/traits/physiology/leucine_arylamidase_activity.html
    sha256: 500be077fdd5b18933412c530685633aec0fa823be0c9f6260c08ab5373724d4
    role: context
  - path: pages/traits/physiology/leucyl_glycine_arylamidase_activity.html
    sha256: 67703e2c3771d1428612bbb45f25fba1bddb3672c839396aec623f6496c593a6
    role: context
  - path: pages/traits/physiology/lipase_activity.html
    sha256: bae8688a03c3af5213073c5a1cb2007730d17b26bf88edabae1cb23b731aae7b
    role: context
  - path: pages/traits/physiology/lipophagy.html
    sha256: 69e5eeaccb09a5296bebe99ab09b1f5b78dc40f8a05894b17eaac982bb02c53e
    role: context
  - path: pages/traits/physiology/lithoautotrophic.html
    sha256: 9885836fb114bb9824ddd54482dab4012de6a77bba03c288953ffc88e14b4de4
    role: context
  - path: pages/traits/physiology/lithoheterotrophic.html
    sha256: c9f46749568143dccc4b72a47eb5969d34642c44dc5351c8b5b38d0574dbbbdb
    role: context
  - path: pages/traits/physiology/lithotrophic.html
    sha256: 1873f71e56ca01585b477e880e8815cfa9d398aae1ea52551f43a5031d87e00b
    role: context
  - path: pages/traits/physiology/lysine_decarboxylase_activity.html
    sha256: 077f34ee2ff9e75ed2f163aaafcbd5d843447c1a9cf1b3172f3a84d4d56de0b2
    role: context
  - path: pages/traits/physiology/macropinocytosis.html
    sha256: fd2d9eb192ffa062d86fbf59163fb89cafca55a10a4632d09a9a5e518c7fe821
    role: context
  - path: pages/traits/physiology/magnetotaxis.html
    sha256: 90395902f214c90a1fa769c0aebd6044c570a2acf446bc9ac6a04540b1d008c9
    role: context
  - path: pages/traits/physiology/mating_type_switching.html
    sha256: d15a64a3496272dd05741333c9eef4ac49679473b9a44e81590f214be8842c1b
    role: context
  - path: pages/traits/physiology/methanotrophic.html
    sha256: 7a817f5b1b6455db9aabd997d80ea439a8f1e29411f0c94b856fbdea58354237
    role: context
  - path: pages/traits/physiology/methylotrophic.html
    sha256: c5a5c8d2ab687ca6667a679e8b1c5a9ca701ff5fce48840be899e75460d552a6
    role: context
  - path: pages/traits/physiology/mitophagy.html
    sha256: 252bdcf2eaf521b4146a382f4d9e850222302a8cadc42c7881f706640777fe75
    role: context
  - path: pages/traits/physiology/mixotrophic.html
    sha256: 6d2c0470339370691d7de3d921cc9ea6f30d0207451cbf1055a78bb0352669a0
    role: context
  - path: pages/traits/physiology/mucocyst_discharge.html
    sha256: d6772062e44caf8af0298b3982a16b28d6cad3ad8f9fa85e2eeb96b294fc3a1e
    role: context
  - path: pages/traits/physiology/myzocytosis.html
    sha256: d72359244afc2c5d6d741b071a2060f8ccf62338a2c38e8ebaa906e4e99d176a
    role: context
  - path: pages/traits/physiology/nad_dependent_alcohol_dehydrogenase_activity.html
    sha256: bdd5180fcc9b3d66cbfa7f3eb0dd44c3f99a557958bb78be4dbf6f66b306a5ac
    role: context
  - path: pages/traits/physiology/naphthol_as_bi_phosphohydrolase_activity.html
    sha256: 075d0c7d3fad36bcd7721152f2070dda70be2084042134dd4082077e240e8396
    role: context
  - path: pages/traits/physiology/natural_competence.html
    sha256: 08d99791ae2e9524b2e67642ff2dcf8eae0479e4e28ea041518422533cb17ad5
    role: context
  - path: pages/traits/physiology/negative_autotropism.html
    sha256: ce79a9e09de1cc3078af0321dce8e8d9b79d089adce76e7304941a36dbe70a47
    role: context
  - path: pages/traits/physiology/nucleophagy.html
    sha256: 7b416340216dff4ce0acb45583f174216775714bff049760631e5b0469cb472e
    role: context
  - path: pages/traits/physiology/nutrient_adaptation.html
    sha256: 34e20c29ac6c62f6e4260f94854f956759517363e5ff5d2a60d05080a131a52f
    role: context
  - path: pages/traits/physiology/oligotrophic.html
    sha256: ad10877fef44f236fbbfab67c0bd802486d028a155729603117f2692f5ba6b6e
    role: context
  - path: pages/traits/physiology/oogamy.html
    sha256: 5ed3c754c263e0bcacc42f6422ca5d87524fcef2c54f4168ffb3a06372aad2ce
    role: context
  - path: pages/traits/physiology/organoheterotrophic.html
    sha256: de70883626478c2f675cf198bc4f29e139f8f3193f64a51d353feac8b87f47bc
    role: context
  - path: pages/traits/physiology/organotrophic.html
    sha256: 8d72267447207143948e8dd0a40cae4032a840e18da6350bbaa184fe01096a5d
    role: context
  - path: pages/traits/physiology/ornithine_decarboxylase_activity.html
    sha256: ffe1de748c0f9433fbd82fa5245c33761dda0add0b5b02ba55ff0be03278d8bf
    role: context
  - path: pages/traits/physiology/osmotaxis.html
    sha256: f2f2e7775e794f7546b68cc961faac9c86de6d5783934ec79b68b4344e4187f8
    role: context
  - path: pages/traits/physiology/oxidase_activity.html
    sha256: 088841ddd585c7fac0371477ef8906ff56474ffd88b1f55f402b05ad1eca5b19
    role: context
  - path: pages/traits/physiology/oxidative_stress_response.html
    sha256: 1173b2d283352b64278584f3a3d2508c51ab5c49ef550b312440a9fccce12b79
    role: context
  - path: pages/traits/physiology/paedogamy.html
    sha256: 4a72f9bd6b72e5f0d257789a1347671e6d301872ed40e9337c967113493ca2d6
    role: context
  - path: pages/traits/physiology/pallium_feeding.html
    sha256: 72d2f8722c3e051aad6ce7454b55f56dcf87b1419e61dccdee4e8342dd8f51f3
    role: context
  - path: pages/traits/physiology/parasexuality.html
    sha256: a97251e6b472c9fa752fcac8d673935e21926b2c04b08cf2beedeba442098835
    role: context
  - path: pages/traits/physiology/persister_cell_formation.html
    sha256: 1b1a4c4d4261386845d9e4320c560fc3e29a5b5938f108e94dd046301cd1dc8a
    role: context
  - path: pages/traits/physiology/pexophagy.html
    sha256: ed1af959b6ae1f8f713b56d045c6f811a202f07f3e7be5fd8337545111c53bd8
    role: context
  - path: pages/traits/physiology/ph_taxis.html
    sha256: cddbd6bb599e074e4ab83991d34f51a6204adfae5f476e41640de75223f3c4bf
    role: context
  - path: pages/traits/physiology/ph_tropism.html
    sha256: b5c12ebf23a298239542b385af82b1230cd08e386d54e42d7bb2a705a614f0a9
    role: context
  - path: pages/traits/physiology/phagocytosis.html
    sha256: b02fefdb003a9c4d717c7d9fbf177c8336659519f6666c168662677c9da246c1
    role: context
  - path: pages/traits/physiology/phagotrophy.html
    sha256: 53296f425d23bd1e617fcbd91a0c550ac6cbb3b1c5bd3522159416b172eafdab
    role: context
  - path: pages/traits/physiology/phenylalanine_arylamidase_activity.html
    sha256: 5e6a3c5e150e09d138fbfa42a9cafd1702f5f548c5073ebbdc11f666cd7b324f
    role: context
  - path: pages/traits/physiology/photoautotrophic.html
    sha256: 8413a1e1b0c9aa48de1d2fcaf4ad37febc85dd515037437ab50f2eab3c39d857
    role: context
  - path: pages/traits/physiology/photoheterotrophic.html
    sha256: e051898b5fe8b3ac9f1d3c038024755f5b9decfc05f3a04251f1d42270e98f12
    role: context
  - path: pages/traits/physiology/photokinesis.html
    sha256: 97ea08bac5b2c0d61cacf2d0ee63ac1673749ddacbc46ac49e14af2ba6780a87
    role: context
  - path: pages/traits/physiology/photolithoautotrophic.html
    sha256: 643630266f1f462c0a7d98514a8b74553a2109002d98968981433f3a232683dc
    role: context
  - path: pages/traits/physiology/photolithotrophic.html
    sha256: 7c6438fb0e0e22178741f54d32d27b6da386b763fe1fe3352db2a8e9e717ac06
    role: context
  - path: pages/traits/physiology/photoorganoheterotrophic.html
    sha256: 4625571855556ee4060af0c3d1d6811df30ebcf183366977a09c061985db4494
    role: context
  - path: pages/traits/physiology/phototaxis.html
    sha256: cb3e58cac98035feb021511c724f62caefecfc884d1189c25a49bedb9afa9d45
    role: context
  - path: pages/traits/physiology/phototrophic.html
    sha256: 255cc6603c98ebd5fc2189949da49161c8009c19d2857ba7414b2bbec532e20f
    role: context
  - path: pages/traits/physiology/phototropism.html
    sha256: b1da86f82298deb9ab84087695a74cc673d406a6a5876c7ce92a11ea33e122bf
    role: context
  - path: pages/traits/physiology/pinocytosis.html
    sha256: 21a3c3e6be180f5256cd02df234724b256485621c43f2a9e6494c01184cf295c
    role: context
  - path: pages/traits/physiology/positive_autotropism.html
    sha256: 1a6e65b7b5262383b7c4aef6bcba56e06ac5a0c3622aaea68abd7555fc63f18f
    role: context
  - path: pages/traits/physiology/primary_homothallism.html
    sha256: 9e7dcc353ca8cda98dceb4eb5d7fd69eb27b12b49b2699634b0be87f10fa5254
    role: context
  - path: pages/traits/physiology/prolyl_aminopeptidase_activity.html
    sha256: 9341e8203fc72d928672107ee1b3f7a741d61a34873232d1d94c45f2fc7c0473
    role: context
  - path: pages/traits/physiology/proteaphagy.html
    sha256: 20d73571a2f0fd232b12ae7588478e777a483f9ccd4ed73df0358b6bbde5a40e
    role: context
  - path: pages/traits/physiology/pseudobipolar_mating_system.html
    sha256: 5c28cce92570a673b62c2a8eb43326c2402ac106927d28b33b36aeb0233edf55
    role: context
  - path: pages/traits/physiology/pseudohomothallism.html
    sha256: d52235f83fa4670156d2888a63ccb9f0a4396336285c8245df5c09d036fcb9d0
    role: context
  - path: pages/traits/physiology/pyrazinamidase_activity.html
    sha256: 0099f73c797c656256493da47f504c8eb01717e07c1909f323e43919b1e43525
    role: context
  - path: pages/traits/physiology/pyrrolidonyl_arylamidase_activity.html
    sha256: 5ec26e1b429d45dbfe6b9c97cf68e87e78b2a46c28d1b564960802cac1d3bb5c
    role: context
  - path: pages/traits/physiology/quorum_quenching.html
    sha256: 0faa8c9ad9d2cc10328eb1888b4f7c0ae7fe6c05e01c7394908aeb553424692d
    role: context
  - path: pages/traits/physiology/quorum_sensing.html
    sha256: 54bda34a221b228016c83d37f3fe26db93bd5e0e70acc443451feb8b31d76e72
    role: context
  - path: pages/traits/physiology/rapid_axopodial_contraction.html
    sha256: 4157629f966d76461e6087114c2164a36e30f8eadcd93cf468b1987793fad101
    role: context
  - path: pages/traits/physiology/replicative_aging.html
    sha256: 22808fb40806a3109c4dbec01422d94320ecb01995a1f18aade6b756459d950a
    role: context
  - path: pages/traits/physiology/rheotaxis.html
    sha256: bb81e7fbed999b6a1045e2026ac543ae2537698c7ce51b0aa9784f6e24648e70
    role: context
  - path: pages/traits/physiology/rheotropism.html
    sha256: 819d3492160f73b11daeba82ff2049d01016eba190fb5053a5e1edfac22d79ee
    role: context
  - path: pages/traits/physiology/ribophagy.html
    sha256: 3a59314a7a712c50a22d37d1e86e0efdc2d7ceff37a2ba94cbdd56c58651b87f
    role: context
  - path: pages/traits/physiology/serine_arylamidase_activity.html
    sha256: 5e24a1af69d720e79bc05ff2756a45a092f84a8674992355cd185f47948606c2
    role: context
  - path: pages/traits/physiology/siderophore_production.html
    sha256: a55a34f8d3ac47acc67a29a3387aebdf7d62dbb1768f504465c99275c4eb1563
    role: context
  - path: pages/traits/physiology/siliceous_scale_production.html
    sha256: 1d531c0792528e9fbb5fb605242480f97e1f51939110dcd9543841450abab1b3
    role: context
  - path: pages/traits/physiology/sos_response.html
    sha256: 749060897c533b3b7199bd73faa45292c3ea112f2b80f0cef93387611a36c8df
    role: context
  - path: pages/traits/physiology/spore_germination.html
    sha256: a35c2fbdba11e1f44fb9334df5ab98f47e7ddd8fef4656d82c6eb01d04c6998f
    role: context
  - path: pages/traits/physiology/stress_response.html
    sha256: 9bfe3d663dee2dfaedb43d1e51945d7fad4ff653dd3720b5d90f016ee17e25ca
    role: context
  - path: pages/traits/physiology/tetrapolar_mating_system.html
    sha256: ac3aca23f01d93f3176f2fdeae7b043cdebece398cc2de601919e753d34eb0a0
    role: context
  - path: pages/traits/physiology/thermotaxis.html
    sha256: c52318ec768f6193f57cbe1a82959daecd1a623ab1352ebbb85d80a17588e089
    role: context
  - path: pages/traits/physiology/thigmotropism.html
    sha256: aced9005de503bca4693cfce2f3bc897348aa89e64abef820a9cc3c2fc58d9ef
    role: context
  - path: pages/traits/physiology/toxicyst_discharge.html
    sha256: d89f8d88b2b7468a481fcbdcae05b1ce23bd03a62d316b07f1912c8de22d4c76
    role: context
  - path: pages/traits/physiology/trichocyst_discharge.html
    sha256: cf1805929350c4006aa672fe9951c681b729dc1287e573be93a84b6f269dbc7a
    role: context
  - path: pages/traits/physiology/tripolar_mating_system.html
    sha256: 001b09d63af90c290e598dcb2c8dd07ae92298722f15f4aeeceb2dc0b42e1d12
    role: context
  - path: pages/traits/physiology/trogocytosis.html
    sha256: ed610611ffd5d5e733d56a72c79a9beb86f2e4c7e808e7ed4bea6cc292e217e2
    role: context
  - path: pages/traits/physiology/trophic_type.html
    sha256: d93feb5e7f74bfc453144b692d238d57f1e90032f32bea0b04c85b01c2abf06a
    role: context
  - path: pages/traits/physiology/trypsin_activity.html
    sha256: f6c1f91d73a44c2d6f099d1e95071dddcdb111b4e3268ddd176615435bd7751b
    role: context
  - path: pages/traits/physiology/tyrosine_arylamidase_activity.html
    sha256: c9951b5044c439f295cb3b84292cb632a021ace8cd4225ee07568d10f73523fb
    role: context
  - path: pages/traits/physiology/unconventional_protein_secretion.html
    sha256: feaa22e0d872fe76d7d71a9db8ed67322c2c44b894bd09dd161e1f4e952115c8
    role: context
  - path: pages/traits/physiology/unequal_protein_aggregate_inheritance.html
    sha256: 25b4e8fe0938a933bf45c5582d4c783d12b4417e3d810ebc6d237556730e723c
    role: context
  - path: pages/traits/physiology/unisexual_reproduction.html
    sha256: a1702dc8e91e666dfd784232e9111f3399f5477362e1e754b147dd8219573d9d
    role: context
  - path: pages/traits/physiology/urease_activity.html
    sha256: 2112826d9f3c13d632574baaf71f359ecaa84cf8648828059898fc99a3c80cc7
    role: context
  - path: pages/traits/physiology/valine_arylamidase_activity.html
    sha256: 44f3c880fb25c123b4d38ef85d5b5e8ca6d703da7ea7fd514b04b1ef6d895746
    role: context
  - path: pages/traits/physiology/viable_but_nonculturable_state.html
    sha256: 58798fb385d97dc35035e3e78991ccfc1595789772a192fbc851ca30eeb9735a
    role: context
  - path: pages/traits/physiology/viscotaxis.html
    sha256: 16d61c02785bfcc6e4d0afa844b6266b8bdc5bccc8c158095e15f5ac2d6d6316
    role: context
  - path: pages/traits/quantitative_property/has_maximum_observed_value.html
    sha256: 839cbb2fc7ddf7d37690505e12f92575f722ca0bd7e41efb5dcea4a17791d47b
    role: context
  - path: pages/traits/quantitative_property/has_minimum_observed_value.html
    sha256: 66bd3af3ca76a8414054cf835e6cd8bdcbc30cfc25ccb28eed8f8031a6b0e680
    role: context
  - path: pages/traits/quantitative_property/has_observed_spot_value.html
    sha256: 6ff0d6d2fafe0ec1120a845dbb25b961e0ec6327384d4ef01792a5c81c8b294d
    role: context
  - path: pages/traits/quantitative_property/has_value.html
    sha256: 87788bca05a16c84f50684f82fa2700d340a42774a28f5d6628da23339d3f889
    role: context
  - path: pages/traits/quantitative_property/has_value_comments.html
    sha256: f756cc6e1b249999c9906aa0a09e214f67d5f762451a599e1b75155f38b9f02e
    role: context
  - path: pages/traits/quantitative_property/is_negative_data.html
    sha256: 93fcf7ee1ea84f554c113ac45525937a9b28750ce9ec80dc6301125c39efbca5
    role: context
  - path: pages/traits/quantitative_property/observation_data_property.html
    sha256: 13411b5b8880b990e635505feb1aafad71996626b169b5cf03468909d12a6fe4
    role: context
  - path: pages/traits/upper/biological_process.html
    sha256: cd90fece2fbe14cdbb93b0acf5158685c11022e5be9f880c0b2d8906d722396d
    role: context
  - path: pages/traits/upper/chemical_entity.html
    sha256: bc41c1c5f230e7bb96591f50b425fd5c635c17f90ed09dc0f594a28bea947095
    role: context
  - path: pages/traits/upper/enzyme.html
    sha256: 6b1fe96124e50f7d5b918bf8a564decd94bd3be128c8ba1fb42f7215e2343c20
    role: context
  - path: pages/traits/upper/material_entity.html
    sha256: d8a79fedf2988a271fca34bdc929497962f9358cc155e3ee75664a0873199be3
    role: context
  - path: pages/traits/upper/microbe.html
    sha256: d2cde124bd3eb72cab92754389affd89c29c657ea807dce7bebc546b97fe2b78
    role: context
  - path: pages/traits/upper/observation.html
    sha256: 41d74dd8ff4c77f3106d89307291407421cd62f6df24febce6e6dab5c0ed8629
    role: context
  - path: pages/traits/upper/phenotype.html
    sha256: 4a5f205e04973773ef55e62d4663f8bd3487d9dfe14c1468ef9fa23b3c762f7e
    role: context
  - path: pages/traits/upper/quality.html
    sha256: 6f53b6f4115adf7b4084db528cf5ebe640e6aebdfcdd1f06f601ebf017c331b6
    role: context
  - path: pages/umap.html
    sha256: 2954758eff336dc3b7b19700f4902f523aada7e7669b1986c192e66d3d9fd3c1
    role: context
  - path: proposals/metpo_traitmech_v591/metpo_proposal_classes_robot.tsv
    sha256: 070a7d007dd8bb303f962204a799ae997ce8da9bab5b39a509e6f61314914e98
    role: context
  - path: proposals/metpo_traitmech_v591/proposal.md
    sha256: 18af5011341f6ff2eaf933a2bb7601f788d987c081421b2616939138f97bad0d
    role: context
  - path: reports/metpo_2026_06_12_active_review.tsv
    sha256: 45e9c6471475635ba1f2602cd636a119d490f5dbd8dd6ac8af1aab89a321379f
    role: context
  - path: reports/metpo_2026_06_12_release_delta.tsv
    sha256: afe858d2aa0ade08322c7808d5917ff370e069ba02c2642d483342db8e9323ac
    role: context
  - path: reports/proposal_citation_audit.tsv
    sha256: 37fe48924a7b2504ab077c98d8d01d7036725a054dfe63c52b7788f9cdc926b9
    role: context
  - path: reports/robot/metpo_traitmech_v591/classes.owl
    sha256: 8b250649b2725e4a46ea2f67aab74a858c5bca8c821c4e4f881a65fe8d0e3cd6
    role: context
  - path: reports/robot/metpo_traitmech_v591/merged.owl
    sha256: 5b034a2a40619123c5dec7dc7a7d45fd617dd908060983aa5825ce64e2f54212
    role: context
  - path: reports/robot/metpo_traitmech_v591/reasoned.owl
    sha256: 7985e1f3c5087c0e4cb4a265702dcb94cda6ad4ed842853accada46d50a04b20
    role: context
  - path: research/traits/physiology/extracellular_trail_based_spatial_memory-source-verification.json
    sha256: 65b79ec4590e6c80749c703e392d6da9db26ff5068a07cffe43b13ab7e5f404e
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
  - path: reviews/structured/20261013T010510Z-transcriptional-reactivation-memory/review.md
    sha256: dcc64f35253d60c66e2948452a3d9ab88c3bc6a2cd3bdae90eff1dade2eba45e
    role: context
  - path: reviews/structured/20261013T010510Z-transcriptional-reactivation-memory/review.yaml
    sha256: c8a3eab5039ac0c50b26e87fb01b89fd2f588e71e9ef30c500c25565e7342012
    role: context
  - path: reviews/structured/20261013T012051Z-transcriptional-memory-primary-result-finding/review.md
    sha256: 0e1bff8e2d2fda248f737c118e794d7ffe8af08700bdb1c95954e1e2d29e6ecf
    role: context
  - path: reviews/structured/20261013T012051Z-transcriptional-memory-primary-result-finding/review.yaml
    sha256: b447ce0a2384fc8b1e5a80bf3c1cc7042deb7bb18c4244ff53ba82ddac741525
    role: context
  - path: reviews/structured/20261013T013510Z-transcriptional-memory-primary-result-resolution/review.md
    sha256: ec82b3c886eea7f3033b48f05f76224e36588e79007c1e320f025f279e7c4c49
    role: context
  - path: reviews/structured/20261013T013510Z-transcriptional-memory-primary-result-resolution/review.yaml
    sha256: 98aa2d3321dc5d0aeb572e5f379e7a76f813d7262f4e6bea375430abac2d6665
    role: context
  - path: reviews/structured/20261013T015129Z-transcriptional-memory-anaphora-finding/review.md
    sha256: 255c9e8b890e64d78930079062f1c440da77edfb8fffb8d28bfc518e37f32191
    role: context
  - path: reviews/structured/20261013T015129Z-transcriptional-memory-anaphora-finding/review.yaml
    sha256: 45763a0ad709c6a031c57338da2f0d8e38b2237e8cdabf204bd1ec1f7342afe9
    role: context
  - path: reviews/structured/20261013T022227Z-transcriptional-memory-self-contained-resolution/review.md
    sha256: 85546a8e0ecfce601e1abbf14c4167d5d6ec59e12eb8a2cf74b777025cb7d77a
    role: context
  - path: reviews/structured/20261013T022227Z-transcriptional-memory-self-contained-resolution/review.yaml
    sha256: 48e7047bd3783582f26b3a03eb1e1cbadabbae9bb59784c535224a18aca2a744
    role: context
  - path: reviews/structured/20261013T024613Z-transcriptional-memory-provenance-finding/review.md
    sha256: 79e592932652b55dd9935efa7927594cdd28f622c2bc8f788260e26a093c1790
    role: context
  - path: reviews/structured/20261013T024613Z-transcriptional-memory-provenance-finding/review.yaml
    sha256: 49dc863e375907a46ebb06724a980b31dfca65b8bac6180490328334bcabca9e
    role: context
  - path: reviews/structured/20261013T025727Z-transcriptional-memory-provenance-resolution/review.md
    sha256: 4cb6bca2c837881aa71f094115bfec41353f9f93fd0435b8dd5b74211f8003d1
    role: context
  - path: reviews/structured/20261013T025727Z-transcriptional-memory-provenance-resolution/review.yaml
    sha256: 41bdae75df73c06da3a6c2b99916aafa5fdf0d4cdaee915486beae0e018015c1
    role: context
  - path: reviews/structured/20261013T051306Z-behavioral-habituation/review.md
    sha256: 6a9da1604f43b13c781caef5ff15732d472685d178b5324148599889b24b8f12
    role: context
  - path: reviews/structured/20261013T051306Z-behavioral-habituation/review.yaml
    sha256: b398edb8587f517b38bc7383dc8e0e7309f86544573ae1c2dc39434f6e7e2836
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/.vendored_canon_ref
    sha256: 698af47e96e93fe96e81910bb140593a79c2b92c4688892edeab9b63244ec5bf
    role: context
  - path: scripts/add_extracellular_trail_memory_trait.py
    sha256: 58e03fc80e042b3ecababe7475503dd09bec64095fdfc9c82d977fb8ed266098
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
  - path: tests/test_add_extracellular_trail_memory_trait.py
    sha256: 6b910bbbbfc0cf327883a92fbecdc1eb457c857ad12762afcd452ce21c62bf35
    role: context
targets:
- target_id: traitmech:000715
  path: data/traits/physiology/extracellular_trail_based_spatial_memory.yaml
  label: extracellular-trail-based spatial memory
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/physiology/extracellular_trail_based_spatial_memory.yaml
    role: maintained scientific record
  - repository: CultureBotAI/TraitMech
    path: scripts/add_extracellular_trail_memory_trait.py
    role: guarded validated writer
  - repository: CultureBotAI/TraitMech
    path: proposals/metpo_traitmech_v591
    role: upstream reservation and evidence narrative
scope:
  description: Entire new record and maintained/generated change set, not whole-corpus
    scientific review.
  selection: One exact newly curated trait; no sampling.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - traitmech:000715
  exclusions:
  - target: Other 1109 TraitRecords
    reason: Semantic novelty, byte preservation and deterministic validation only.
  - target: data/traits/physiology/spore_germination.yaml
    reason: Protected; unchanged.
checks:
- check_id: records-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate
    -s src/traitmech/schema/traitmech.yaml --target-class TraitRecord data/traits/physiology/extracellular_trail_based_spatial_memory.yaml
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate
    -s src/traitmech/schema/traitmech.yaml --target-class TraitRecord data/traits/physiology/extracellular_trail_based_spatial_memory.yaml
  status: passed
  required: true
  target_ids:
  - traitmech:000715
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained gate passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: records-1
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_strict.py data/traits/physiology/extracellular_trail_based_spatial_memory.yaml
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_strict.py data/traits/physiology/extracellular_trail_based_spatial_memory.yaml
  status: passed
  required: true
  target_ids:
  - traitmech:000715
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained gate passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: records-2
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_history_links.py history/records/extracellular_trail_based_spatial_memory
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_history_links.py history/records/extracellular_trail_based_spatial_memory
  status: passed
  required: true
  target_ids:
  - traitmech:000715
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained gate passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: records-3
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate
    -s src/traitmech/schema/history.yaml --target-class HistoryRecord history/records/extracellular_trail_based_spatial_memory/2026-10-13T064512Z-codex-64c936.yaml
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate
    -s src/traitmech/schema/history.yaml --target-class HistoryRecord history/records/extracellular_trail_based_spatial_memory/2026-10-13T064512Z-codex-64c936.yaml
  status: passed
  required: true
  target_ids:
  - traitmech:000715
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained gate passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: records-4
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/ruff
    check src scripts tests
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/ruff
    check src scripts tests
  status: passed
  required: true
  target_ids:
  - traitmech:000715
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained gate passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: generate-0
  name: just audit-proposals
  command: just audit-proposals
  status: passed
  required: true
  target_ids:
  - traitmech:000715
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained gate passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: generate-1
  name: just ground-predicates
  command: just ground-predicates
  status: passed
  required: true
  target_ids:
  - traitmech:000715
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained gate passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: generate-2
  name: just ground-nodes
  command: just ground-nodes
  status: passed
  required: true
  target_ids:
  - traitmech:000715
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained gate passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: generate-3
  name: just audit-graphs
  command: just audit-graphs
  status: passed
  required: true
  target_ids:
  - traitmech:000715
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained gate passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: generate-4
  name: just audit-graph-protein-taxa
  command: just audit-graph-protein-taxa
  status: passed
  required: true
  target_ids:
  - traitmech:000715
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained gate passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: generate-5
  name: just audit-predicate-domains
  command: just audit-predicate-domains
  status: passed
  required: true
  target_ids:
  - traitmech:000715
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained gate passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: generate-6
  name: just check-biolink-coverage
  command: just check-biolink-coverage
  status: passed
  required: true
  target_ids:
  - traitmech:000715
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained gate passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: generate-7
  name: just audit-snippets
  command: just audit-snippets
  status: passed
  required: true
  target_ids:
  - traitmech:000715
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained gate passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: generate-8
  name: just gen-discussions-data
  command: just gen-discussions-data
  status: passed
  required: true
  target_ids:
  - traitmech:000715
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained gate passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: generate-9
  name: just gen-qc-dashboard
  command: just gen-qc-dashboard
  status: passed
  required: true
  target_ids:
  - traitmech:000715
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained gate passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: generate-10
  name: just gen-pages
  command: just gen-pages
  status: passed
  required: true
  target_ids:
  - traitmech:000715
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained gate passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: generate-11
  name: just gen-priority-dashboard
  command: just gen-priority-dashboard
  status: passed
  required: true
  target_ids:
  - traitmech:000715
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained gate passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: verify-0
  name: just qc
  command: just qc
  status: passed
  required: true
  target_ids:
  - traitmech:000715
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained gate passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: verify-1
  name: just validate-history
  command: just validate-history
  status: passed
  required: true
  target_ids:
  - traitmech:000715
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained gate passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: verify-2
  name: just validate-products
  command: just validate-products
  status: passed
  required: true
  target_ids:
  - traitmech:000715
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained gate passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: verify-3
  name: just verify-proposal metpo_traitmech_v591
  command: just verify-proposal metpo_traitmech_v591
  status: passed
  required: true
  target_ids:
  - traitmech:000715
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained gate passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: verify-4
  name: just robot-validate-proposal metpo_traitmech_v591
  command: just robot-validate-proposal metpo_traitmech_v591
  status: passed
  required: true
  target_ids:
  - traitmech:000715
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained gate passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: verify-5
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/audit_canonical_examples.py --no-resolve
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/audit_canonical_examples.py --no-resolve
  status: passed
  required: true
  target_ids:
  - traitmech:000715
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained gate passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: verify-6
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/run_trait_graph_audit.py --verify
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/run_trait_graph_audit.py --verify
  status: passed
  required: true
  target_ids:
  - traitmech:000715
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained gate passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: verify-7
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/audit_history_records.py --base 496e026915723362abc58c3ab721d99548f0f784
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/audit_history_records.py --base 496e026915723362abc58c3ab721d99548f0f784
  status: passed
  required: true
  target_ids:
  - traitmech:000715
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained gate passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: tests-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q --junitxml=/tmp/traitmech-trail-memory-checks-20261013/pytest.xml
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q --junitxml=/tmp/traitmech-trail-memory-checks-20261013/pytest.xml
  status: passed
  required: true
  target_ids:
  - traitmech:000715
  exit_code: 0
  expected_exit_code: 0
  summary: 4379 tests passed without skips, failures or errors.
- check_id: native-snippets
  name: native-snippets
  command: scripts/verify_snippets.py --record data/traits/physiology/extracellular_trail_based_spatial_memory.yaml
    --out /tmp/traitmech-trail-memory-native-snippets-20261013.tsv
  status: passed
  required: true
  target_ids:
  - traitmech:000715
  exit_code: 0
  expected_exit_code: 0
  summary: 'Native resolver completed: two NOT_IN_ABSTRACT and one UNRESOLVED. All
    three direct PDF spans separately match. The 2017 exact DOI has Crossref/PDF identity
    and a zero-hit qualified MED query, not a global nonindexing claim.'
- check_id: browser
  name: browser
  command: node /tmp/traitmech-trail-memory-browser-20261013.cjs
  status: passed
  required: true
  target_ids:
  - traitmech:000715
  exit_code: 0
  expected_exit_code: 0
  summary: '1440/390 px: three excerpts, three discussions, one history link, local-ID
    provenance, hierarchy and browse navigation, dashboard 1110 and coverage image.
    Eight screenshots inspected; no horizontal overflow or page errors.'
- check_id: preservation
  name: preservation
  command: python /tmp/traitmech-trail-memory-artifacts-20261013.py
  status: passed
  required: true
  target_ids:
  - traitmech:000715
  exit_code: 0
  expected_exit_code: 0
  summary: All 1109 prior trait YAMLs, prior history/reviews/proposals/embeddings/templates
    remain byte-identical. Existing pages change only footers except the phenotype
    child link; only its priority child count changes.
- check_id: rdf
  name: rdf
  command: python /tmp/traitmech-trail-memory-rdf-20261013.py
  status: passed
  required: true
  target_ids:
  - traitmech:000715
  exit_code: 0
  expected_exit_code: 0
  summary: Parsed class, merged and reasoned RDF preserves exact identity and definition,
    w3id METPO IRIs, phenotype parent and quality grandparent; no legacy METPO stub.
evidence:
- evidence_id: source-0
  kind: primary_source
  reference: DOI:10.1073/pnas.1215037109
  locator: Results, first paragraph, printed page 17490 / PDF page 1
  accessed_at: '2026-10-13T05:23:21.285604Z'
  support: supports
  snapshot_sha256: f690252a6bec2a70b77da8c9550d6b7245eecb009090d91a570f12e43482cccc
  summary: Reid et al. 2012, PMID:23045640, PMC3491460; Results opening paragraph,
    printed page 17490 / PDF page 1. Cultured Physarum polycephalum avoided previously
    deposited slime in a Y maze. Same-stock coatings do not demonstrate individual
    recognition of one's own trace. In the separate U-trap experiment, 23/24 plasmodia
    on blank agar versus 8/24 on slime-coated agar reached the target within 120 hours.
    Coating masks newly informative trails; it does not abolish secretion or lesion
    internal memory. Success, completion time among successful trials, speed, path
    length and revisitation are distinct endpoints. No-trap and speed controls do
    not exclude every environmental confound. Main Methods, Results, Discussion and
    all four figures were inspected in an author-hosted publisher-formatted PDF bearing
    a 2012 download stamp, not verified as the current corrected VoR. Supplements
    and raw data were not assessed. Southern Biological Supplies culture provenance
    remains unresolved. The contiguous result span was text-matched and visually checked.
- evidence_id: source-1
  kind: primary_source
  reference: DOI:10.1088/1361-6463/aa87df
  locator: Scientific abstract, printed page 1 / PDF page 2
  accessed_at: '2026-10-13T05:23:21.802416Z'
  support: supports
  snapshot_sha256: b5957278307eb67d93db865c5dc4776a036e731c491b28d363170e72b8256246
  summary: Smith-Ferguson et al. 2017; scientific abstract, printed page 1 / PDF page
    2. This is the authors' interpretation of maze performance, not a measured fitness
    or natural-selection endpoint. Within 72 hours, blank versus extracellular-slime
    conditions yielded success in 24/24 versus 9/24 open trials, 12/15 versus 4/12
    simple-maze trials and 11/17 versus 11/13 complex-maze trials; the last comparison
    showed no significant benefit. Completion times conditional on success were not
    significantly different. Escaped trials were excluded; split decisions used the
    dominant front. Printed page 6 pairs the same chi-square 0.802 with P=0.004 and
    P=0.371; this discrepancy is unresolved. Figure 8 is illustrative, not quantified
    trajectory evidence. Main Methods, Results, Discussion, Conclusion and all eight
    figures were inspected; supplements were not. The author-hosted PDF bears a 2017
    download stamp, not verified current VoR equivalence. This study shares authors
    with Reid 2012, not an independent-laboratory replication.
- evidence_id: source-2
  kind: primary_source
  reference: DOI:10.1073/pnas.2312611121
  locator: Results / Quantifying Run-and-Tumble and Self-Avoiding Behavior, page 3
  accessed_at: '2026-10-13T05:51:44.180981Z'
  support: supports
  snapshot_sha256: e6599911fa63b97cfc1895ccb124aa1ee098271fd2c5c64aecd4f00afdecadce
  summary: Troger et al. 2024, PMID:38517977, PMC10990088; Results, Quantifying Run-and-Tumble
    and Self-Avoiding Behavior, page 3. The authors report their own Physarum observations,
    not only a background citation. Actual trajectories, including Figure 2A, are
    distinct from simulated-model panels. Page 5 describes 14 trajectories divided
    into groups of nine each; Figure 4 instead gives seven small and seven large.
    The discrepancy remains unresolved. The 0.65 square-millimeter median is a cohort
    split, not a universal threshold. Small plasmodia can cross trails; a modeled
    three-hour forgetting time is not a measured chemical half-life or internal-memory
    duration. Main text, Methods and all four main figures were inspected in the author-hosted
    publisher-formatted PDF with a March 2024 download stamp, not verified current
    corrected VoR equivalence. Publisher supplements and raw data were not reanalyzed.
    This different laboratory's assay is not a replication of the earlier maze experiments;
    no universal molecular receptor is established.
- evidence_id: content
  kind: record_content
  reference: data/traits/physiology/extracellular_trail_based_spatial_memory.yaml
  locator: Entire maintained record, guarded writer/tests, proposal, sidecar and generated
    change set.
  accessed_at: '2026-10-13T07:09:24Z'
  support: supports
  summary: One qualified physiological CLASS. Three primary DOI excerpts support external
    trace-guided exploration without canonical taxa, universal avoidance, internal
    recall, protein examples, graph edges or exact synonyms.
- evidence_id: novelty
  kind: search
  reference: research/traits/physiology/extracellular_trail_based_spatial_memory-source-verification.json
  locator: Pre-creation local/remote novelty, semantic adjudication and RDF receipts;
    fresh publication audit.
  accessed_at: '2026-10-13T07:09:24Z'
  support: supports
  summary: Ignored/hidden current files and retained tracked history were searched.
    Neighboring memory endpoints, autotropism, predation and membrane exchange are
    not exact. All 458 current CommunityMech community records were checked separately
    from isolate files. No exact active record or unresolved exact node requiring
    migration was identified in the bounded scope.
  search_scope: '{"additional_community_records": 458, "disposition": "Completed lexical
    screens preceded acceptance. Full matched records and RDF neighbors were subsequently
    assessed; no exact active record or node requiring migration was identified in
    the bounded scope.", "ignored_hidden_included": true, "local_scope": {"accepted":
    false, "checked_at": "2026-10-13T06:14:53.484853+00:00", "identifier_reserved":
    false, "ignored_hidden_included": true, "independent_copies": 12, "limits": ["Bounded
    lexical search; semantic adjudication pending.", "Historical tracked HEADs cannot
    reconstruct unavailable ignored/untracked files.", "Archives and packed Git objects
    are not semantically unpacked; no symlink directory traversal.", "After-delete
    clone excluded while recovery checks run.", "Current sibling records are covered
    by the separate pinned remote audit, not all sibling worktrees.", "Sibling proposals
    describe the start catalog only; a changed catalog needs a refresh before any
    allocation."], "sibling_catalog_changed_during_scan": false, "sibling_historical_revisions":
    105, "sibling_proposal_roots": 129, "traitmech_registered": 22}, "remote_scope":
    {"body_hits": [], "checked_at": "2026-10-13T06:14:19.314943+00:00", "limits":
    "Lexical screen only. Binary limits recorded per file. Requires ontology and semantic
    adjudication; no reservation.", "main": "496e026915723362abc58c3ab721d99548f0f784",
    "pattern": "spatial[ _-]memor|external(i[sz]ed|i[sz]ation)?[ _-](spatial[ _-])?memor|stigmerg|trail[
    _-](avoid|follow|guid|memor|navig)|slime.{0,30}trail|(substrate|surface|environmental|foraging)[
    _-]memor|self[ _-]avoid|pnas[.]1215037109|beheco/art032|1361-6463/aa87df|pnas[.]2312611121|nature12155|23045640|38517977|23657259|PMC3491460|PMC10990088|PMC4109411",
    "pending_files": 828, "pending_hits": [], "prs": 12, "upstream_files": 129, "upstream_hits":
    []}}'
- evidence_id: ontology
  kind: database
  reference: data/raw/metpo.owl
  locator: Active phenotype parent; deprecated 0000248, 000249, 1000004 and 1000062;
    current upstream main and open METPO issue 521.
  accessed_at: '2026-10-13T07:09:24Z'
  support: supports
  summary: The active phenotype parent is broader. Deprecated adaptation/chemotaxis
    neighbors have no inspected replacement or consider annotations. Reason codes
    are provisional and original scope unresolved, not proof of invalid biology or
    exact identity. Pinned ontology remains unchanged.
- evidence_id: products
  kind: validation
  reference: reports/proposal_citation_audit.tsv
  locator: Native gates, generator pin, byte preservation, parsed RDF and browser
    observations.
  accessed_at: '2026-10-13T07:09:24Z'
  support: supports
  summary: 'One trait and v591 class row added. All prior records, including protected
    spore germination, remain unchanged. Parsed RDF graph cardinalities: {''classes'':
    15, ''merged'': 12628, ''reasoned'': 12632}. Generator source has 645 checked
    blobs. Exact configured embedding sources absent; prior embeddings retained. Only
    required ROBOT trailing tabs use the inspected path-specific whitespace exception.'
- evidence_id: history
  kind: record_content
  reference: history/records/extracellular_trail_based_spatial_memory/2026-10-13T064512Z-codex-64c936.yaml
  locator: CREATE event, identity/evidence/discussions; actual codex/gpt-5/codex actor.
  accessed_at: '2026-10-13T07:09:24Z'
  support: supports
  summary: One append-only history reflects written sections. Record event uses observed
    06:32:45Z post-audit confirmation, explicitly not predicted write time. No REVIEWED
    status promotion.
- evidence_id: publication
  kind: search
  reference: https://github.com/CultureBotAI/TraitMech/commit/d2f20fbc560bbffee0e50a1194261202fbd13715
  locator: /tmp/traitmech-trail-memory-publication-20261013/assessment.json
  accessed_at: '2026-10-13T06:56:46.269733Z'
  support: supports
  snapshot_sha256: 011964f31ed381fd2254094faa26abbf9d7b618acd90c52ba6809a28430cf2f7
  summary: 'Fresh publication audit: 828 nonremoved pending blobs, 129 selected upstream
    blobs, 10121 intervals and 58 explicit dispositions. No conflicting reservation
    remained. Numeric embedding/gmelin hits and editor envelopes are not competing
    IDs.'
  search_scope: '{"base": "496e026915723362abc58c3ab721d99548f0f784", "block": [1066800,
    1066899], "candidate": "traitmech:000715", "checked_at": "2026-10-13T06:56:46.269733+00:00",
    "cohort": "metpo_traitmech_v591", "conflicts": [], "dispositions": [{"disposition":
    "Exact current owned addition, not another reservation.", "hit_index": 0}, {"disposition":
    "Exact current owned addition, not another reservation.", "hit_index": 1}, {"disposition":
    "Exact current owned addition, not another reservation.", "hit_index": 2}, {"disposition":
    "Exact current owned addition, not another reservation.", "hit_index": 3}, {"disposition":
    "Exact current owned addition, not another reservation.", "hit_index": 4}, {"disposition":
    "Exact current owned addition, not another reservation.", "hit_index": 5}, {"disposition":
    "Exact current owned addition, not another reservation.", "hit_index": 6}, {"disposition":
    "Exact current owned addition, not another reservation.", "hit_index": 7}, {"disposition":
    "Exact current owned addition, not another reservation.", "hit_index": 8}, {"disposition":
    "Exact current owned addition, not another reservation.", "hit_index": 9}, {"disposition":
    "Exact current owned addition, not another reservation.", "hit_index": 10}, {"disposition":
    "Exact current owned addition, not another reservation.", "hit_index": 11}, {"disposition":
    "Exact current owned addition, not another reservation.", "hit_index": 12}, {"disposition":
    "Exact current owned addition, not another reservation.", "hit_index": 13}, {"disposition":
    "Exact current owned addition, not another reservation.", "hit_index": 14}, {"disposition":
    "Exact current owned addition, not another reservation.", "hit_index": 15}, {"disposition":
    "Exact current owned addition, not another reservation.", "hit_index": 16}, {"disposition":
    "Exact current owned addition, not another reservation.", "hit_index": 17}, {"disposition":
    "Exact current owned addition, not another reservation.", "hit_index": 18}, {"disposition":
    "Exact current owned addition, not another reservation.", "hit_index": 19}, {"disposition":
    "Exact current owned addition, not another reservation.", "hit_index": 20}, {"disposition":
    "Exact current owned addition, not another reservation.", "hit_index": 21}, {"disposition":
    "Exact current owned addition, not another reservation.", "hit_index": 22}, {"disposition":
    "Exact current owned addition, not another reservation.", "hit_index": 23}, {"disposition":
    "Exact current owned addition, not another reservation.", "hit_index": 24}, {"disposition":
    "Exact current owned addition, not another reservation.", "hit_index": 25}, {"disposition":
    "Exact current owned addition, not another reservation.", "hit_index": 26}, {"disposition":
    "Exact current owned addition, not another reservation.", "hit_index": 27}, {"disposition":
    "Exact current owned addition, not another reservation.", "hit_index": 28}, {"disposition":
    "Exact current owned addition, not another reservation.", "hit_index": 29}, {"disposition":
    "Exact current owned addition, not another reservation.", "hit_index": 30}, {"disposition":
    "Exact current owned addition, not another reservation.", "hit_index": 31}, {"disposition":
    "Exact current owned addition, not another reservation.", "hit_index": 32}, {"disposition":
    "Exact current owned addition, not another reservation.", "hit_index": 33}, {"disposition":
    "Exact current owned addition, not another reservation.", "hit_index": 34}, {"disposition":
    "Exact current owned addition, not another reservation.", "hit_index": 35}, {"disposition":
    "Owned v591 class row.", "hit_index": 36}, {"disposition": "Same hash-verified
    embedding coordinate or gmelin namespace hit explicitly adjudicated before creation.",
    "hit_index": 37}, {"disposition": "Same hash-verified embedding coordinate or
    gmelin namespace hit explicitly adjudicated before creation.", "hit_index": 38},
    {"disposition": "Formal editor namespace envelope or its explicit adjudication,
    not a competing exclusive block.", "overlap_index": 0}, {"disposition": "Formal
    editor namespace envelope or its explicit adjudication, not a competing exclusive
    block.", "overlap_index": 1}, {"disposition": "Formal editor namespace envelope
    or its explicit adjudication, not a competing exclusive block.", "overlap_index":
    2}, {"disposition": "Formal editor namespace envelope or its explicit adjudication,
    not a competing exclusive block.", "overlap_index": 3}, {"disposition": "Formal
    editor namespace envelope or its explicit adjudication, not a competing exclusive
    block.", "overlap_index": 4}, {"disposition": "Formal editor namespace envelope
    or its explicit adjudication, not a competing exclusive block.", "overlap_index":
    5}, {"disposition": "Owned full-block reservation.", "overlap_index": 6}, {"disposition":
    "Formal editor namespace envelope or its explicit adjudication, not a competing
    exclusive block.", "overlap_index": 7}, {"disposition": "Formal editor namespace
    envelope or its explicit adjudication, not a competing exclusive block.", "overlap_index":
    8}, {"disposition": "Formal editor namespace envelope or its explicit adjudication,
    not a competing exclusive block.", "overlap_index": 9}, {"disposition": "Formal
    editor namespace envelope or its explicit adjudication, not a competing exclusive
    block.", "overlap_index": 10}, {"disposition": "Formal editor namespace envelope
    or its explicit adjudication, not a competing exclusive block.", "overlap_index":
    11}, {"disposition": "Formal editor namespace envelope or its explicit adjudication,
    not a competing exclusive block.", "overlap_index": 12}, {"disposition": "Formal
    editor namespace envelope or its explicit adjudication, not a competing exclusive
    block.", "overlap_index": 13}, {"disposition": "Formal editor namespace envelope
    or its explicit adjudication, not a competing exclusive block.", "overlap_index":
    14}, {"disposition": "Formal editor namespace envelope or its explicit adjudication,
    not a competing exclusive block.", "overlap_index": 15}, {"disposition": "Formal
    editor namespace envelope or its explicit adjudication, not a competing exclusive
    block.", "overlap_index": 16}, {"disposition": "Formal editor namespace envelope
    or its explicit adjudication, not a competing exclusive block.", "overlap_index":
    17}, {"disposition": "Formal editor namespace envelope or its explicit adjudication,
    not a competing exclusive block.", "overlap_index": 18}], "ignored_hidden": true,
    "intervals_checked": 10121, "limits": "Current available files include ignored/hidden
    files. Retained tracked history does not recover unavailable ignored/untracked
    files; archives and symlink directories were not expanded. Fresh remote catalogs
    and candidate scans; generic interval parses reused only after dual hash verification.
    No atomic reservation or exhaustive novelty claim.", "owned_head": "d2f20fbc560bbffee0e50a1194261202fbd13715",
    "pending_files": 828, "pending_prs": [{"body_hits": {"hits": []}, "draft": false,
    "files": 1, "head": "35099af2b7d5347f2ca6e418c4a139979071644d", "number": 1782,
    "repository": "CultureBotAI/TraitMech"}, {"body_hits": {"hits": []}, "draft":
    false, "files": 8, "head": "b4b8d1280e25bd3e340241e7ac23b51bbe7aaec3", "number":
    1476, "repository": "CultureBotAI/TraitMech"}, {"body_hits": {"hits": []}, "draft":
    false, "files": 3, "head": "331f9517bbdf4d2c9fa97b338ee59a8986f2f174", "number":
    973, "repository": "CultureBotAI/TraitMech"}, {"body_hits": {"hits": []}, "draft":
    true, "files": 692, "head": "e61ce120b8da953da097b9f94bfed7f292e5675a", "number":
    924, "repository": "CultureBotAI/TraitMech"}, {"body_hits": {"hits": []}, "draft":
    false, "files": 45, "head": "109fb0d2c095c9fcc3379328f775493e41c65ab8", "number":
    1997, "repository": "CultureBotAI/CommunityMech"}, {"body_hits": {"hits": []},
    "draft": true, "files": 64, "head": "29995b01e01ecb392b0d217479f2c2453e49ffdb",
    "number": 935, "repository": "CultureBotAI/CommunityMech"}, {"body_hits": {"hits":
    []}, "draft": false, "files": 1, "head": "627963b839cd7fd993ec892da9d5f663dbc3963d",
    "number": 644, "repository": "berkeleybop/metpo"}, {"body_hits": {"hits": []},
    "draft": false, "files": 1, "head": "b5051800f0d46753e5cab17043e6740bc357917a",
    "number": 643, "repository": "berkeleybop/metpo"}, {"body_hits": {"hits": []},
    "draft": false, "files": 1, "head": "9681aeacff5ea06a0dd8907906475d270ad61285",
    "number": 641, "repository": "berkeleybop/metpo"}, {"body_hits": {"hits": []},
    "draft": false, "files": 1, "head": "653ac70425dba225bdbbfb1a46d03c4837bc4cab",
    "number": 640, "repository": "berkeleybop/metpo"}, {"body_hits": {"hits": []},
    "draft": false, "files": 1, "head": "d6005ffbab2fab328f118db4a5f1024d1d07be03",
    "number": 638, "repository": "berkeleybop/metpo"}, {"body_hits": {"hits": []},
    "draft": false, "files": 15, "head": "32e9fa86d36092156919b748dbe51b21df2bf702",
    "number": 629, "repository": "berkeleybop/metpo"}], "raw_receipt_sha256": "80bad9e3c8772485b41445767d65de4d7da7f7ba504bc58db0b234666fda9044",
    "upstream_files": 129}'
assessments:
- assessment_id: identity
  area: identity
  topic: External trace-guided exploration
  summary: The label and definition bound information persisting in extracellular
    trails, not all memory, a secreted molecule, literal sequence feature or a single
    maze observation. Related memory classes concern distinct endpoints.
  target_ids:
  - traitmech:000715
  evidence_ids:
  - content
  - source-0
  - source-1
  - source-2
  - novelty
  - publication
  outcome: supported
- assessment_id: controls
  area: evidence
  topic: Context-dependent experimental support
  summary: Coatings mask new spatial information but also change substrate conditions;
    they do not abolish secretion or lesion internal memory. Same-stock trails do
    not establish individual self-recognition. Success proportions and conditional
    completion times remain distinct, and no benefit is required in every maze.
  target_ids:
  - traitmech:000715
  evidence_ids:
  - source-0
  - source-1
  - content
  outcome: supported
- assessment_id: model
  area: evidence
  topic: Observed behavior versus model mechanism
  summary: The 2024 result is the authors own trajectory observation, not merely cited
    background. Simulated forgetting is not a measured trail half-life or internal-memory
    duration; median size groups are not universal biological thresholds. No receptor-resolved
    graph is invented.
  target_ids:
  - traitmech:000715
  evidence_ids:
  - source-2
  - content
  outcome: supported
- assessment_id: sources
  area: provenance
  topic: Three contiguous source spans and source discrepancies
  summary: All excerpts match directly inspected PDF text and actual pages. The 2017
    scientific abstract interprets maze performance, not measured fitness. Two NOT_IN_ABSTRACT
    and one UNRESOLVED native outcomes remain separate. Printed statistical and group-size
    discrepancies are retained; later arXiv wording does not silently correct the
    earlier PDF.
  target_ids:
  - traitmech:000715
  evidence_ids:
  - source-0
  - source-1
  - source-2
  - content
  outcome: supported
- assessment_id: grounding
  area: grounding
  topic: Conservative parent and historical identity
  summary: Phenotype is strictly broader; no universal chemotaxis mechanism is imposed.
    Deprecated adaptation and chemotaxis IDs remain unresolved historical context,
    not revived identifiers or exact xrefs.
  target_ids:
  - traitmech:000715
  evidence_ids:
  - ontology
  - content
  - novelty
  outcome: supported
- assessment_id: products
  area: consistency
  topic: Guarded writes, proposal and derived products
  summary: Dry run, fail-closed preimages, prevalidation, replay, full tests, QC,
    ROBOT RDF and responsive browse/navigation checks pass. The single 11-column proposal
    retains required blank cells. Existing records, histories, reviews, proposals
    and baselines are preserved.
  target_ids:
  - traitmech:000715
  evidence_ids:
  - products
  - history
  - content
  outcome: supported
- assessment_id: limits
  area: completeness
  topic: Explicit remaining research gaps
  summary: Natural culture provenance, historical scopes, current corrected versions,
    unread supplements, source discrepancies and common molecular sensing remain unresolved.
    These are not obscured by examples, mappings, universal claims or REVIEWED status.
  target_ids:
  - traitmech:000715
  evidence_ids:
  - content
  - ontology
  - source-0
  - source-1
  - source-2
  outcome: unknown
findings: []
actions: []
limitations:
- Author self-review. Exact-head external review and CI are separate publication gates,
  not yet covered by this local assessment.
- The primary evidence concerns cultured Physarum. The first two papers share authors;
  the third uses a different assay, not same-assay replication. No raw-data or simulation
  reanalysis.
- Author-hosted publisher-formatted copies are not verified current corrected VoRs.
  Publisher SI and other unread supplement assets remain gaps; bounded metadata and
  access failures do not prove notice absence.
- Original deprecated scopes remain unresolved. Independent positive acceptance does
  not establish historical equivalence or nonequivalence.
- Ignored/hidden current files were included, but unavailable historical ignored/untracked
  bytes, arbitrary archives, symlink directories and unchanged pending-tree files
  are not reconstructed. Discovery is not exhausted.
- Embedding inputs are absent at exact configured locations, so embeddings were preserved
  rather than regenerated. Existing frozen audit baselines are unchanged.
tags:
- add-trait
- extracellular-trail-memory
- self-review
```
