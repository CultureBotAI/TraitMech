# Adversarial review of fungal nematophagy

- Review: 20261013T160405Z-fungal-nematophagy
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-13T15:50:53Z
- Finished UTC: 2026-10-13T16:04:05Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Direct sources support the fungal feeding phenotype and bounded example. Identity, evidence, parent, allocation, provenance and generated outputs withstand this author adversarial pass. No actionable defect identified; three explicit discussions remain OPEN and status remains PROPOSED.

## Scope And Provenance

Entire one-record change and maintained/generated owners, not whole-corpus scientific review.

Selection: One exact newly authored trait; no sampling.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 47007725fa6b28f4e5f307ebed01d61301558dd5.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| traitmech:000719 | data/traits/ecology/fungal_nematophagy.yaml | maintained | fungal nematophagy |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python -m pytest -q tests/test_add_fungal_nematophagy_trait.py tests/test_readme_artifacts.py tests/test_trait_priority.py tests/test_qc_dashboard_artifacts.py | passed | True | traitmech:000719 | Actual maintained command passed; corpus diagnostics are not whole-corpus scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/ruff check src scripts tests | passed | True | traitmech:000719 | Actual maintained command passed; corpus diagnostics are not whole-corpus scientific review. |
| just audit-proposals | passed | True | traitmech:000719 | Actual maintained command passed; corpus diagnostics are not whole-corpus scientific review. |
| just ground-predicates | passed | True | traitmech:000719 | Actual maintained command passed; corpus diagnostics are not whole-corpus scientific review. |
| just ground-nodes | passed | True | traitmech:000719 | Actual maintained command passed; corpus diagnostics are not whole-corpus scientific review. |
| just audit-graphs | passed | True | traitmech:000719 | Actual maintained command passed; corpus diagnostics are not whole-corpus scientific review. |
| just audit-graph-protein-taxa | passed | True | traitmech:000719 | Actual maintained command passed; corpus diagnostics are not whole-corpus scientific review. |
| just audit-predicate-domains | passed | True | traitmech:000719 | Actual maintained command passed; corpus diagnostics are not whole-corpus scientific review. |
| just check-biolink-coverage | passed | True | traitmech:000719 | Actual maintained command passed; corpus diagnostics are not whole-corpus scientific review. |
| just audit-snippets | passed | True | traitmech:000719 | Actual maintained command passed; corpus diagnostics are not whole-corpus scientific review. |
| just gen-discussions-data | passed | True | traitmech:000719 | Actual maintained command passed; corpus diagnostics are not whole-corpus scientific review. |
| just gen-qc-dashboard | passed | True | traitmech:000719 | Actual maintained command passed; corpus diagnostics are not whole-corpus scientific review. |
| just gen-pages | passed | True | traitmech:000719 | Actual maintained command passed; corpus diagnostics are not whole-corpus scientific review. |
| just gen-priority-dashboard | passed | True | traitmech:000719 | Actual maintained command passed; corpus diagnostics are not whole-corpus scientific review. |
| just qc | passed | True | traitmech:000719 | Actual maintained command passed; corpus diagnostics are not whole-corpus scientific review. |
| just validate-history | passed | True | traitmech:000719 | Actual maintained command passed; corpus diagnostics are not whole-corpus scientific review. |
| just validate-products | passed | True | traitmech:000719 | Actual maintained command passed; corpus diagnostics are not whole-corpus scientific review. |
| just verify-proposal metpo_traitmech_v595 | passed | True | traitmech:000719 | Actual maintained command passed; corpus diagnostics are not whole-corpus scientific review. |
| just robot-validate-proposal metpo_traitmech_v595 | passed | True | traitmech:000719 | Actual maintained command passed; corpus diagnostics are not whole-corpus scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/audit_canonical_examples.py --no-resolve | passed | True | traitmech:000719 | Actual maintained command passed; corpus diagnostics are not whole-corpus scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/run_trait_graph_audit.py --verify | passed | True | traitmech:000719 | Actual maintained command passed; corpus diagnostics are not whole-corpus scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/audit_history_records.py --base e0f3176847fe446a5af3322fe6d0864c03db42d2 | passed | True | traitmech:000719 | Actual maintained command passed; corpus diagnostics are not whole-corpus scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python -m pytest -q --junitxml=/tmp/traitmech-nematophagy-checks-20261013/pytest.xml | passed | True | traitmech:000719 | 4534 tests passed without failures, errors or skips. |
| schema | passed | True | traitmech:000719 | Direct LinkML record validation passed. |
| strict | passed | True | traitmech:000719 | Direct closed-schema record validation passed. |
| snippets | passed | True | traitmech:000719 | Native result: two UNRESOLVED and one NOT_IN_ABSTRACT; URL evidence not run. All four excerpts separately matched directly inspected original sources, not relabeled VERIFIED. |
| taxonomy | passed | True | traitmech:000719 | 762 canonical examples resolved, zero errors, 24 existing label warnings outside the new record. Pleurotus ostreatus 5322 agrees with NCBI; this does not independently identify the experimental isolate. |
| products | passed | True | traitmech:000719 | All 1113 previous records and prior history/reviews/proposals/embeddings/templates/snippet baseline byte-preserved. Existing pages are footer-only except the phenotype child link. Parent priority child count changes 196 to 197. Parsed RDF retains exact w3id identifiers and parent/grandparent. |
| browser | passed | True | traitmech:000719 | 1440/390 px checks pass: four excerpts, three discussions, one history, local identifier, example, hierarchy and browse navigation, dashboard 1114 and loaded coverage image. Eight screenshots visually inspected. No horizontal overflow or page errors. |

## Scientific And Domain Assessments

### Fungal feeding, not capture morphology

identity: supported. Targets: traitmech:000719.

The definition requires fungal consumption of nematodes as food. A living-prey attack or specific capture apparatus is not imposed; paralysis alone remains insufficient. Fungal qualification avoids nonfungal actors.

### Direct feeding observations and assay limits

evidence: supported. Targets: traitmech:000719.

Consumption observations and source-defined internal digestion support the scoped phenotype. Hyphal occupancy is not quantified assimilation; no universal host range, exclusive nutrition or complete inhibitor-induced loss is claimed.

### Contiguous source spans and actual resolver outcomes

provenance: supported. Targets: traitmech:000719.

Four self-contained excerpts directly match original retrieved sources. Two quotes from Marlin are one study; native unresolved/full-text verdicts and URL exclusion are retained. A later Update Article is not a correction.

### Hierarchy, taxonomy and reservation

grounding: supported. Targets: traitmech:000719.

Phenotype is broader; carbon-specific trophic axes and trap morphologies are not asserted as parents. Deprecated terms are not reused. The example is source-qualified and taxon-authority checked. Ignored/hidden and live pending-head refreshes support bounded novelty/allocation.

### Validated writes and faithful derived outputs

consistency: supported. Targets: traitmech:000719.

Guarded dry-run, replay/drift tests, full QC/test suite, history, proposal, RDF and browser checks pass. Existing records and immutable provenance are byte-preserved. Current counts agree across README and dashboards.

### Explicit scientific uncertainties

completeness: unknown. Targets: traitmech:000719.

Source table/caption/gene-name inconsistencies, partial figure/supplement access, morphology-only isolate identification and bounded notice checks remain explicit. They do not negate the modest feeding phenotype; no causal graph or exact molecular assignment is invented.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| source-0 | DOI:10.3390/f10050404; Introduction, PDF page 1 | supports | Marlin et al. 2019, Introduction, PDF page 1: directly read terminology, not an independent experiment. The fungal actor qualifies the term; consumption, not paralysis alone, defines the endpoint. Publisher PDF visually checked. Native DOI abstract verifier: UNRESOLVED, retained separately from the direct match. Crossref and USDA identify the same DOI/title. |
| source-1 | DOI:10.3390/f10050404; Figure 2a caption, PDF page 6 | supports | Figure 2a caption, actual PDF page 6 and panel inspected, with Methods 2.1-2.3 and Results 3.2. This is a source-named feeding observation, not measured nutrient flux. Native verifier: UNRESOLVED. Host susceptibility is differential; neither all nematodes nor all Pleurotus isolates are asserted. The two excerpts from this paper total 17 words. |
| source-2 | https://horizon.documentation.ird.fr/exl-doc/pleins_textes/fan/40780.pdf; Summary, PDF page 1 | supports | den Belder and Jansen 1994, Summary, PDF page 1, directly and visually matched. Selected Methods, Results and Discussion, including actual pages 6-8, describe Arthrobotrys oligospora CBS 289.82 feeding on living and previously killed Meloidogyne hapla juveniles. Internal hyphal occupancy is not a tracer assimilation assay. The excerpt supports nonexclusive feeding modes, not an exact rate. URL evidence is not run by the native DOI/PMID abstract verifier. |
| source-3 | DOI:10.1371/journal.pbio.3002400; Results, Late time point induced protease and its potential role in digesting nematodes | supports | Lin et al. 2023, PMID:37988381; Results subsection on late-time protease induction, publisher XML sec018. Native verifier: NOT_IN_ABSTRACT; exact full-text match. Actual Figure 5, Table 1 and S7 inspected. GFP-labeled reference TWF3407 is engineered, not an unmodified natural exemplar. Protease inhibition delays internal growth at 12 h without proving complete feeding loss or quantifying assimilation. Remaining figures and raw S1 spreadsheet were not fully audited. |
| content | data/traits/ecology/fungal_nematophagy.yaml; Entire new record, writer, tests, sidecar, proposal, history and generated diff. | supports | One fungal feeding phenotype. Neither nematode trapping, toxicity, sequence annotation, taxonomic membership nor mere hyphal contact substitutes for feeding. Four excerpts are three sources, not four independent studies. |
| scope | https://horizon.documentation.ird.fr/exl-doc/pleins_textes/fan/40780.pdf; Selected Methods/Results/Discussion; actual PDF pages 1, 6, 7, 8. | supports | Direct observations include live and previously killed juveniles. This challenges a compulsory-killing or strict starvation definition; it does not establish nutrient flux, universal host range or a single molecular mechanism. Disputed rates and caption/table directions remain excluded. |
| taxonomy | NCBITaxon:5322; NCBI EFetch top-level species record; Marlin Methods 2.1-2.3 and Figure 2a. | supports | Authority label agrees with Pleurotus ostreatus. The example is limited to an unnamed grocery-store mushroom isolate with morphological identification. No deposit, genotype or unmodified natural laboratory strain is invented. Lin GFP imaging strains are explicitly engineered and not canonical examples. |
| ontology | data/raw/metpo.owl; Pinned/current RDF, editor metadata shell, upstream template screening and live neighboring definitions. | supports | Phenotype is a true broader parent. Deprecated trophic terms replace to a broader carbon/energy axis, not an exact feeding term; fungal-spore and parasitism hits are not exact. Trap morphology and other uptake modes are not is-a parents. No historical identifier reuse or unverified exact xref. |
| novelty | research/traits/ecology/fungal_nematophagy-source-verification.json; Ignored/hidden local files, positive-controlled retained heads, full pending changed blobs and selected upstream owners. | supports | No exact feeding record/proposal or same-scope unresolved node/synonym needing migration found within recorded bounds. Canonical local matches are trap morphology, autophagy and myzocytosis; CommunityMech matches are bacterial host/biocontrol/taxonomy contexts. KG-Microbe matches concern taxonomy, isolation source and life stage. |
| status | research/traits/ecology/fungal_nematophagy-source-verification.json; Crossref DOI records, PubMed linked-update metadata, directly read PLOS publisher pages; recorded MDPI access failure. | supports | The linked PLOS 2025 Update Article adds research, not a correction or independent-laboratory replication. Crossref metadata does not expose a linked notice in retrieved records; MDPI status-page 403 and limited IRD metadata preclude exhaustive notice clearance. |
| products | reports/proposal_citation_audit.tsv; Maintained gates, full tests, generated diffs, current counts, RDF and browser checks. | supports | All required local gates pass. Parsed RDF graph sizes are {'classes': 15, 'merged': 12628, 'reasoned': 12632}. Shared generator matches 645 source blobs; exact configured embedding inputs absent, so existing embeddings retained. Only inspected ROBOT TSV header trailing tabs receive a path-scoped whitespace exception. |
| history | history/records/fungal_nematophagy; CREATE event and LLM-assisted per-record minting event. | supports | Observed acceptance time is distinguished from write time. Sections identity, evidence, canonical_examples and discussions match the actual change. Actor codex, model gpt-5, tool codex; no human sign-off or REVIEWED promotion. |
| publication | /tmp/traitmech-nematophagy-publication-20261013/accepted.json; Refreshed ignored/hidden local searches and live pending/upstream Git identities. | supports | 171 locations rechecked; owned additions separated from competing allocations. All remote heads unchanged; prior full blobs retain their identities. No competing reservation found. Historical heads unchanged; package sizes and broad editor envelopes remain nonreservations. |

## Limits And Additional Notes

- Author self-review. Exact-head external review, CI and merge-queue/integrity checks are separate gates, not claimed complete here.
- Selected actual PDF pages, Figure 5, Table 1 and S7 were inspected, not every figure/supplement or raw S1 data. Conflicting host ranges, numerical rates and mep1/mcp1 identities are not reconciled by assertion.
- Internal hyphal growth is not quantitative nutrient flux. Isotope measurements are not required to recognize feeding, but no carbon/nitrogen contribution or universal mechanism is inferred.
- The Pleurotus example is an unnamed morphology-identified grocery-store culture, not a deposited or molecularly authenticated strain. NCBI validates the taxon name, not the specimen identity.
- Two native snippet rows are UNRESOLVED and one NOT_IN_ABSTRACT; URL evidence is not run by that verifier. Direct matching is reported separately. Notice checks are bounded, including MDPI 403.
- Ignored/hidden available files were searched; lost ignored/untracked history, symlink directories, local archives and unchanged pending-tree files are not reconstructed. Discovery is not exhausted.
- Configured embedding sources are absent; existing embedding artifacts, shared templates and frozen baselines remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T160405Z-fungal-nematophagy
kind: record
repository: CultureBotAI/TraitMech
title: Adversarial review of fungal nematophagy
started_at: '2026-10-13T15:50:53Z'
finished_at: '2026-10-13T16:04:05Z'
reviewer:
  identity: codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Author source-based adversarial assessment; no separate-agent
    or human independence claimed.
skill: .claude/skills/add-trait/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Direct sources support the fungal feeding phenotype and bounded example.
  Identity, evidence, parent, allocation, provenance and generated outputs withstand
  this author adversarial pass. No actionable defect identified; three explicit discussions
  remain OPEN and status remains PROPOSED.
source:
  git_revision: 47007725fa6b28f4e5f307ebed01d61301558dd5
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
    sha256: ee4e3ce3da46b2ee20711a9165fd311e75fb0ebc02e51f7f82800f99d02dc2d3
    role: context
  - path: app/dashboard/priority.html
    sha256: 18d6d46d18bbefd96c2584ab1f11c81e509c2d586d1f7a60172ed2dd68207afb
    role: context
  - path: app/dashboard/priority.json
    sha256: 80488d319ac6af05b625b27e8b4c308162ab1957162867e1f6aaae3a1b072d79
    role: context
  - path: app/discussions/data.js
    sha256: 4e6164ba671f1ed98c9272009a86b3244fc5847989ffd9d13b278aa810fc8b83
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
    sha256: 65ff3ed9869b9eb0182f0100d9c2522a005ba0b67e562fdafb62bb98f9ff441d
    role: context
  - path: dashboard/index.html
    sha256: f25b8d5be3f0137e4efa6e744f0a953c4676a9c2ca0cef6b2fd6b040e257dbd7
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
    role: target
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
  - path: docs/record-review-profile.md
    sha256: cac714488cad03263ca3847737d5f70d174d40b5be677a09e0c1d9c814d9bc6a
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: history/README.md
    sha256: f795a191e17978454a8bb80da91ed6873a9405a240e6e5758837dd9bdc3b5c07
    role: context
  - path: history/records/fungal_nematophagy/2026-10-13T153654Z-codex-2ac7d3.yaml
    sha256: 139acb7d4dd2abce88ccaf5e264d97fb6529554e99fab2dfe972844f5178396c
    role: context
  - path: justfile
    sha256: e6047ea612115a6a78d100b281483ba824c860c3def59bcd0d40e7fb56b3526a
    role: context
  - path: pages/browse.html
    sha256: 471b79cb84d6670ab237690c9dc4cf958ab815175039052ea7dcecb2f1a6d71c
    role: context
  - path: pages/category/ecology.html
    sha256: 73b4dc19ba91ee0184d74989c9eefe21c6b2c5407575c33fa0b0dadee8c5a178
    role: context
  - path: pages/category/environment.html
    sha256: d94c5d042c827f1bb6e74f342edd33f9f8df6c68fe2d3cf782f6a30de9f4135a
    role: context
  - path: pages/category/genomics.html
    sha256: f2ce6e27c8867bc1044d128e43798c7cdf0d8cbd1a083362785ebfc61909d7f2
    role: context
  - path: pages/category/metabolism.html
    sha256: 35021dc5ea11a51c407f9766e768227b41257cb78e1c49285a89e79e8bdbf228
    role: context
  - path: pages/category/morphology.html
    sha256: 784aa5bbd2097a8eaf1eda1205813922d658894b122ad4f1435c2f0db4fafde9
    role: context
  - path: pages/category/observation.html
    sha256: 409364381bf13382939a0b5cad3327e477c351dbf8709a1ad76e8615b3e310c1
    role: context
  - path: pages/category/other.html
    sha256: 62ad8325ce7f973c158314e5888a2b0f8cf28e61fc26074efc7a7520e2153fb9
    role: context
  - path: pages/category/physiology.html
    sha256: 3aef5d8ab9bd0b94b6f5d885e7d0b40ca0e7b73d77d4625c0a2e138c72dbcb19
    role: context
  - path: pages/category/quantitative_property.html
    sha256: 800d6be28a473972d6d5d9fb652301a11a5b0aa918a204928ca2cbe87fad1a85
    role: context
  - path: pages/category/upper.html
    sha256: f0584db017ac88950994d194d605a145277dd42c9bd149f1578831340bf61fdc
    role: context
  - path: pages/graph.html
    sha256: d3f219a2487d383c46de0831ea9963808d882600ece0d791db9dd72f30d10ed2
    role: context
  - path: pages/index.html
    sha256: cb1d46e54080acfb6de6ba8d3e1ffbeae0ad63a7475caedd70a410207995cb88
    role: context
  - path: pages/traits/ecology/animal_pathogen.html
    sha256: 43b2fef86b0ca1961a61917a5e7a7e22f56359386ec9033466c4598d236ec1f1
    role: context
  - path: pages/traits/ecology/bacterial_cannibalism.html
    sha256: 3a83775119af3fb9e1c4d875970dcff582716a8d0ce11bae4ab6a6f5c3a066ff
    role: context
  - path: pages/traits/ecology/bacterial_mycophagy.html
    sha256: 3fcd4e7b0d78b18948a456490a82c13b4fe546c8e1d583987e8aa36603f3ada1
    role: context
  - path: pages/traits/ecology/biofilm_formation.html
    sha256: 23a096221417fb84242bd1ce074ceb78fb1a993d00756d51ef54bfe330bec917
    role: context
  - path: pages/traits/ecology/biosafety_level.html
    sha256: 55b5dced252ec76cc24c336150921cee409d0e573acaaa1d13184d732aa94ddc
    role: context
  - path: pages/traits/ecology/biosafety_level_1.html
    sha256: 93a20c2885693594a8f721e9e06c353440552124da1d766e75b90de668461ba3
    role: context
  - path: pages/traits/ecology/biosafety_level_2.html
    sha256: a624e7b831fb87763d5500e67e4754a26eed7193a150fcaf638b197813805381
    role: context
  - path: pages/traits/ecology/biosafety_level_3.html
    sha256: 1e59d801cc6c92b0eaaa9bcabd1760e4ed479d43bc05c311721e6ab6e7dd7ecc
    role: context
  - path: pages/traits/ecology/biosafety_level_4.html
    sha256: df4ce3857c8a2d56dcf6f61cfe12e0dc637cb86d34f704adf7670f9eed38ebc4
    role: context
  - path: pages/traits/ecology/biosafety_level_5.html
    sha256: 30adf79fee1b553d6eb2da3036c85a2a2f94f5c9a09dd2412ce9c59bc1dcb6e6
    role: context
  - path: pages/traits/ecology/collective_bacterial_predation.html
    sha256: 75707ea724f94bbef9785ed2a12e1fede34d244f16dae2fc6865b51ab9b6b64a
    role: context
  - path: pages/traits/ecology/commensalism.html
    sha256: 6cc1a26208a5e976956c53249ce23878cc10164ebee714aaa6a7938d1b613f77
    role: context
  - path: pages/traits/ecology/cytoplasmic_bacterial_predation.html
    sha256: 9832dda9184d941eb26428cfd74b510c9996b5b036b36d0c369ef164e5efe667
    role: context
  - path: pages/traits/ecology/endophytic.html
    sha256: b530c807d8089b5a4f4c11eac37933e73dcfe5e33ae750ee3b9897b195fcf1c1
    role: context
  - path: pages/traits/ecology/endosymbiosis.html
    sha256: 30d4a30b0f1be934aad77d3a47404dda8d29c060fe4d351997867018ed511984
    role: context
  - path: pages/traits/ecology/epibiotic_bacterial_predation.html
    sha256: 8906c500198ae9f823228f4693265707b42a0487681358e20e39edfd26dacf8b
    role: context
  - path: pages/traits/ecology/epiphytic.html
    sha256: f6f5367b2958db95de4b6c77f75433f53c538aad696215871042d51767244ebf
    role: context
  - path: pages/traits/ecology/free_living.html
    sha256: 7b2846e70d6f1a446f2be1001b8ff208f0e53f64dc604527ab7fe440051aadb1
    role: context
  - path: pages/traits/ecology/fungal_nematophagy.html
    sha256: c6bc8f9cccfa8722df95e9a51e671d6ba0068699635ceaf1951f110e41c0dd64
    role: context
  - path: pages/traits/ecology/gut_associated.html
    sha256: bfde5b9304d90445cbead24e0cbb2fc29f99649d7752b4c0a012a06bf2bbcb36
    role: context
  - path: pages/traits/ecology/habitat_association.html
    sha256: 869baf63288b7128bfdaeb79ba36a950d2709e31c3aac0d5f0ff52315751d502
    role: context
  - path: pages/traits/ecology/host_associated.html
    sha256: 3c4cb1575aab95dcc701b640aa2284e6842ba25c8a919bff3bdcb99535d0f9ed
    role: context
  - path: pages/traits/ecology/human_pathogen.html
    sha256: 3fb099d22686d2baa071f15de90131ef49fda2bd03eef274232962c06834dbbf
    role: context
  - path: pages/traits/ecology/ixotrophy.html
    sha256: 4b6402b386705836d401aff1d74a6b99f4bb5388a06966f7535118a261afba70
    role: context
  - path: pages/traits/ecology/kin_discrimination.html
    sha256: bca2a18ad5225c70e20df17fa78441e7d418dcc7c8e92ad4c5c4d7654f9c76c5
    role: context
  - path: pages/traits/ecology/mutualism.html
    sha256: 467231a0a7b8b9526cc49c79536b2aeb532c0b23c68fbaa89233a63da5fadb4a
    role: context
  - path: pages/traits/ecology/nitrogen_fixing_symbiosis.html
    sha256: b4bef7e0367d42ef1c01834f7759a09e29dd196d4ae22a0c241dbfc22213fa73
    role: context
  - path: pages/traits/ecology/nutritional_fungal_mycoparasitism.html
    sha256: 90e4a1bb92834db53e770906270e8645d91a287ac29bdfa1fab4a01251308952
    role: context
  - path: pages/traits/ecology/opportunistic_pathogen.html
    sha256: 2cfc178bf214b0a721ac7618d8751f9336e3a2ffaf14a0532208426992368822
    role: context
  - path: pages/traits/ecology/parasitism.html
    sha256: 4df4a033ca1be048f0f35e10dda7ca2ff314c36736020bf7887c281cd5fde4dc
    role: context
  - path: pages/traits/ecology/pathogenic_to_host.html
    sha256: 00c0e68d9886fef20bdef6a7c756028853a0e39a8d63048c04ad60c8adfee7b5
    role: context
  - path: pages/traits/ecology/periplasmic_bacterial_predation.html
    sha256: 97acfd92b0e2d93e68a2c8888949af7f17e39126f40dbd02e1d403a4e46f3346
    role: context
  - path: pages/traits/ecology/plant_pathogen.html
    sha256: b457d80379b6eb1498ebd4dc9db214d32e686659a4d083f040b30053a71333d9
    role: context
  - path: pages/traits/ecology/predatory_bacterium.html
    sha256: 323e681e128d7bba7b3d0d2d83356f56b1160e53db9344cb2cea8bab8ebcbf9b
    role: context
  - path: pages/traits/ecology/rhizosphere_association.html
    sha256: f8ffd372d814fed8d7aff127666a1dc4be62ae0f5838f0b6f3f4a9760ba7c82c
    role: context
  - path: pages/traits/ecology/saprotrophy.html
    sha256: a9ce422494f8c4406894acd12b0407ffed8470c26f2012816871ce4073e9dcb3
    role: context
  - path: pages/traits/ecology/soil_dwelling.html
    sha256: 0dd6b571762a0d99e464fefaa141c632a486763759b7d103f348f115e620a725
    role: context
  - path: pages/traits/ecology/symbiosis.html
    sha256: 90c4723c8be937a20e95d8cb0e105aa4c34d1626cd57765f5ac5ce076fa7acde
    role: context
  - path: pages/traits/environment/acidophilic.html
    sha256: b6666890f812b30de3e0d092bcc3f79a60b4a49f54159dc5871733f1340a17ef
    role: context
  - path: pages/traits/environment/acidotolerant.html
    sha256: 0784ca9a045dddcbf4d62e549d03dd16867f9ddb68b5bfa4b219e1edc7982c25
    role: context
  - path: pages/traits/environment/aerobic.html
    sha256: e95ce09fad0627d27067796bc59c6738bb5dbbbb99f5258e0dc8f1c22455367e
    role: context
  - path: pages/traits/environment/aerotolerant.html
    sha256: 9e0b601e58123ed54f8285127e66f3d5e9da73a7c43ab8a208eb3d5e8bbdb77d
    role: context
  - path: pages/traits/environment/alkalotolerant.html
    sha256: 045562219326c5145ce71792e780e6faed9d62798f08a104dd7edcbf499620b4
    role: context
  - path: pages/traits/environment/alkaphilic.html
    sha256: 7d461d56c26fa6f237e90964882da8d93ab65caf2c9721f826e4527f03bf351d
    role: context
  - path: pages/traits/environment/anaerobic.html
    sha256: aa5d7455b47c4ba60ef63791b2dc7a9927e95826ba734890b9d3fe79e5e30537
    role: context
  - path: pages/traits/environment/arsenic_tolerant.html
    sha256: 0f1b21651403550e6865a60df3b3cbf732f224830812d789ba34b95ef0c865d8
    role: context
  - path: pages/traits/environment/cadmium_tolerant.html
    sha256: 2ac2852e7787abfd98a06986236e8b87d93005aefa5bbc91f3fc413b1ebddc65
    role: context
  - path: pages/traits/environment/capnophilic.html
    sha256: 81ea58c8ceb85619cb8cfe4533eb1329edf13ae4d6fe5602de59cb33d6259a0e
    role: context
  - path: pages/traits/environment/cobalt_tolerant.html
    sha256: af73dcee19bfbd3f9caa7a713103f188bec3ab21db693f52bc3e9d57de501d08
    role: context
  - path: pages/traits/environment/copper_tolerant.html
    sha256: ae1ed0acfa7870084ff164280a897cf4c4933e3f4a7bc8ea68b049759dd07e5e
    role: context
  - path: pages/traits/environment/delta_phenotype_with_numerical_limits.html
    sha256: b0a76622efc18c449b7ef6b4438739198819b277d19dd53ccfc0a291e49747de
    role: context
  - path: pages/traits/environment/desiccation_tolerant.html
    sha256: 041e9401dec9913748abfb647be8491a6c34e5ed14a45187104ac5b887f1b09d
    role: context
  - path: pages/traits/environment/euryhaline.html
    sha256: 2380b5125260f69f292a13705ad22e7b9ce63619e6a6e8f9d613f996037e34b1
    role: context
  - path: pages/traits/environment/extreme_hyperthermophilic.html
    sha256: 5b50bc3402a45361a0952c1a55519d27ff9b28898a3ce7022ee794e845b82259
    role: context
  - path: pages/traits/environment/extremely_halophilic.html
    sha256: 726090045e44c44de1a0733fde0b19b27ad3f23c7768221285a637a3abbe5696
    role: context
  - path: pages/traits/environment/facultative_oxygen_preference.html
    sha256: 74a2d7f00a79012668cb04e85d3d92a6ca7f6d5b84431710a94c47a2bbd20848
    role: context
  - path: pages/traits/environment/facultative_psychrophilic.html
    sha256: 77203722142bc02a0f0f1ea1d9a3f543b1113faaca0919fc54e85c8bac3c67bd
    role: context
  - path: pages/traits/environment/facultatively_acidophilic.html
    sha256: b777d89388ba00af2a80c2161759b98d8dc22b3dfe01af62869bf664bfe1821b
    role: context
  - path: pages/traits/environment/facultatively_aerobic.html
    sha256: 8b4eb770a1c7ec35db3372047599a48c96c2801e0effc374e4252ea54f4a36ac
    role: context
  - path: pages/traits/environment/facultatively_alkaphilic.html
    sha256: e9da30cf9feca40ffaec6c0ed48a3ac8190b34f1e0def8201730f2c7252126cc
    role: context
  - path: pages/traits/environment/facultatively_anaerobic.html
    sha256: cbe8ab5b443b6aa4e9fea24665f0ec797538a744082e6f8087e6bbc7f69bafd4
    role: context
  - path: pages/traits/environment/growth_range_phenotype_with_numerical_limits.html
    sha256: 8dda06d0b4a6964981266553591595c56268c2c239e5cc05f9fcd0601a1276d2
    role: context
  - path: pages/traits/environment/haloalkaliphilic.html
    sha256: aef2a281367a0c512eb6eb73226381b6a72664bb8c576ae2ebb9108f6e5c6f1c
    role: context
  - path: pages/traits/environment/halophilic.html
    sha256: ba0e20b9f9663d7b4b574fbf733aef28f8b769c70be2a9c6c5ae8dbb377def2f
    role: context
  - path: pages/traits/environment/halophily_preference.html
    sha256: 4967b7d7be800fdedb2b8d694fb95319382045b5500764657ce72b964e6e017a
    role: context
  - path: pages/traits/environment/halotolerant.html
    sha256: d51ccf87906821201dc914046aa75486d9b5b087b4a38604e459e8b970f8ffd2
    role: context
  - path: pages/traits/environment/hyperthermophilic.html
    sha256: c5e767eabc10ec9239b56b38f4b30582059456e73074f36564f3c7a15521d1aa
    role: context
  - path: pages/traits/environment/ionizing_radiation_tolerant.html
    sha256: c962589d6f0ca59182ffbb4ca8677bd08d27eea6ceac3190806349edf423daff
    role: context
  - path: pages/traits/environment/mercury_tolerant.html
    sha256: 33174d7da0b28d0fc97e7f044934ee279ea598f21aeb720db05932e3fb3066cc
    role: context
  - path: pages/traits/environment/mesophilic.html
    sha256: 4ddf72ba85d8de75b76e5e619cf1a336f680bcbf16249a563b7c5e90afe258d1
    role: context
  - path: pages/traits/environment/metal_tolerant.html
    sha256: a05afd176472433e16ca83999278fdcc2d5fc71b758b7199ea7126aa2ea998c8
    role: context
  - path: pages/traits/environment/microaerophilic.html
    sha256: e678a6fff016cfbc4f44c90111f1aec136f9fb48a2059681f309bebc623fc10b
    role: context
  - path: pages/traits/environment/microaerotolerant.html
    sha256: 0c678b4ec9e7dcbfa19f1527b7297ea77f1270b9590264a56a30b0aa56918c38
    role: context
  - path: pages/traits/environment/moderately_halophilic.html
    sha256: 50040ba7d6df95e45a171485f9db0fdc31cff208cbf21f84909d0c14f54a0d69
    role: context
  - path: pages/traits/environment/nacl_delta.html
    sha256: 4e6470ce023ff396d4f12a42d998edba07d5495bd1b03913fa86b4c56fe1627d
    role: context
  - path: pages/traits/environment/nacl_delta_high.html
    sha256: 2867ad78f099e27b85f8c112886b9362276b4e77027d55ff2c974ed507362f29
    role: context
  - path: pages/traits/environment/nacl_delta_low.html
    sha256: 808179174ecc1d304bf713acc0de827b18b4b4a46c5caa98ca72bd973f8055ce
    role: context
  - path: pages/traits/environment/nacl_delta_mid1.html
    sha256: 64ddda9e0cd06d63f00acaa249f30ed53090f8f6f745e067130865f530e8a027
    role: context
  - path: pages/traits/environment/nacl_delta_mid2.html
    sha256: 09af89e1c0b414d4ebbb0430e4c89b810de5048c513e962ec5976612acd99544
    role: context
  - path: pages/traits/environment/nacl_optimum.html
    sha256: daaad351842b0e039bff09e1c2a8e8c4b4a4c76d3a9e105cd9110d0620c6da1d
    role: context
  - path: pages/traits/environment/nacl_optimum_high.html
    sha256: 2cd7557ab50b7d2ddfbcd5c59807e4d7fa5e7db7c02df9d4fbea5d38dd9538fa
    role: context
  - path: pages/traits/environment/nacl_optimum_low.html
    sha256: 71810014d4eabc277eb3f8d2105bf49dc0e74ad035005b4eed0bfa63d909f8ac
    role: context
  - path: pages/traits/environment/nacl_optimum_mid1.html
    sha256: 36774d2e959a10285eae7baf1f945a78578d5dc21910dce852081a4745a545bf
    role: context
  - path: pages/traits/environment/nacl_optimum_mid2.html
    sha256: 2f80b6510174c43e40e9f7f9623010b3a92b674cfb401af08700092fe8769e9b
    role: context
  - path: pages/traits/environment/nacl_range.html
    sha256: 5803a4a4e29f5f923ac3a5f0b688166d70576ec1a9e64f265e076087ac646bed
    role: context
  - path: pages/traits/environment/nacl_range_high.html
    sha256: 987e178c184818444ee48fd8478ea3127f28cd98fc8fe3ab74d211febe88070d
    role: context
  - path: pages/traits/environment/nacl_range_low.html
    sha256: 11fafaf539c4fcd5df6a2a6d4ba827b7295c29774174ef3495636f1d3db1ca1a
    role: context
  - path: pages/traits/environment/nacl_range_mid1.html
    sha256: 0209dabbf9c8f5f910ef9f06e94c139e91033fb399c7de841f49a6efcdc0c91b
    role: context
  - path: pages/traits/environment/nacl_range_mid2.html
    sha256: 9eca1c272ec0100c1e5421634319c968ca4e758fcbe7a23ed9048b2bd32fbd22
    role: context
  - path: pages/traits/environment/neutrophilic.html
    sha256: db5e1385272eedf6d2032291f4ab8d317ff0f43100c6e40cc2f0cf64d000806d
    role: context
  - path: pages/traits/environment/non_halophilic.html
    sha256: 3c73c62d7956b025be4dc43a940b2575c937a35f60bff023a209d2813b3050da
    role: context
  - path: pages/traits/environment/obligately_acidophilic.html
    sha256: 6b7affe2425ab1dc9aca641d4da10bc4d4b4647ad25f1d6cb8d65e89babbd301
    role: context
  - path: pages/traits/environment/obligately_aerobic.html
    sha256: 44c23f672191a148397d9ab2788d1a38094b2b6ec1442667cd718763dd9b12c0
    role: context
  - path: pages/traits/environment/obligately_alkaphilic.html
    sha256: cb4bc89476e0070a1775fb5834ce5532cf9f0a184ec45fa97af321a82c4d3026
    role: context
  - path: pages/traits/environment/obligately_anaerobic.html
    sha256: d044bba60469aff97a7fd7c51c51deda74b48506e6f41adb11751547367ff789
    role: context
  - path: pages/traits/environment/obligately_piezophilic.html
    sha256: 7aba5211e081aeba0d2d8f7815637bda9d9937819b227407f4bdc58d10a46fcb
    role: context
  - path: pages/traits/environment/optimum_phenotype_with_numerical_limits.html
    sha256: 808cfcbdd608f158ee49149d9717a69ed973f927c17d9c3b2d44127577eb19b4
    role: context
  - path: pages/traits/environment/oxygen_preference.html
    sha256: 88348140a660360113cba3d2075e8c5162b85ee6bd4997399b703546beb9f96f
    role: context
  - path: pages/traits/environment/ph_delta.html
    sha256: 36577e63de854be27a806878e378b0875f5049b3f55837d4a097a663512704a4
    role: context
  - path: pages/traits/environment/ph_delta_high.html
    sha256: 0f52df00d315e0197fb465b155fd6baa8e36b95cad8b5310c4a11633eaa99f9a
    role: context
  - path: pages/traits/environment/ph_delta_low.html
    sha256: 8b1d396db9de2e04c8874ef30ca73694ab0322149e7e4fe068cc8cee7b433159
    role: context
  - path: pages/traits/environment/ph_delta_mid1.html
    sha256: dceb3c165b5ebd3d4792ce027a3d721dcef2572c3554ecdda8601cfd48d2e2d3
    role: context
  - path: pages/traits/environment/ph_delta_mid2.html
    sha256: 14d3489b8ccfbb57b9e2a478eed0acaf917384a6e34b930634827535872687e0
    role: context
  - path: pages/traits/environment/ph_delta_mid3.html
    sha256: 0c79897ea0c65bf76180cc495ff6ad89fde61ef3253d090d539bac0dd143fc27
    role: context
  - path: pages/traits/environment/ph_delta_very_low.html
    sha256: 02f8cafa762c4b0cc4e0bf0fb5bf6f858dd49561f52186afe64f4065d4e25a0e
    role: context
  - path: pages/traits/environment/ph_growth_preference.html
    sha256: 1a31d5ee24e083b981436d8625a00c881c009689ebcbb0fd6845a3c377aed0ea
    role: context
  - path: pages/traits/environment/ph_optimum.html
    sha256: cf9249cc4bbc5c7eb350221d4f00efbf3b364e9a55d226e7ab22de0357c574b8
    role: context
  - path: pages/traits/environment/ph_optimum_high.html
    sha256: 8a6a7878a5159962df577d9f281388fd8000ebef6fcc407c5cf683be6e3f2580
    role: context
  - path: pages/traits/environment/ph_optimum_low.html
    sha256: 8cf4ebc27793298945428eccd93f2df418bb879bfdf1931b03f8755f0530c0cd
    role: context
  - path: pages/traits/environment/ph_optimum_mid1.html
    sha256: d2dd992d0fbd99870cb95836d639dcfa765bb6d6004b22500955171e479e044e
    role: context
  - path: pages/traits/environment/ph_optimum_mid2.html
    sha256: 96e1fd57223f06f0ce6b43f71c8e4be89b807c24c2cf8b5b67400a9ec2a07767
    role: context
  - path: pages/traits/environment/ph_phenotype_with_numerical_limits.html
    sha256: a19073c5d475189cc956be61040704e9ae2e8053b90511e9f2ac84e559bcf1bd
    role: context
  - path: pages/traits/environment/ph_range.html
    sha256: c818f3d47754fe720f68941f63d31206d55497febf6d1018029ffe7a97e2e544
    role: context
  - path: pages/traits/environment/ph_range_high.html
    sha256: 388d5eaec805c9dad7f6d30bcf04568997eaa5cafccb4797abe18eb3aec95f69
    role: context
  - path: pages/traits/environment/ph_range_low.html
    sha256: ede913624e5cced592c1a42877718d9811df5e1ab5d053343a4159106a41bbe6
    role: context
  - path: pages/traits/environment/ph_range_mid1.html
    sha256: e04c90fb7d4104e9a789189d5b4fe8c1ab273e71f4cedfb001136853ab95e04b
    role: context
  - path: pages/traits/environment/ph_range_mid2.html
    sha256: 9c0c63249d4201f8866bdd95d77911003a5c286d5eb077dc70f6b9f6e56f7a78
    role: context
  - path: pages/traits/environment/ph_range_mid3.html
    sha256: a297deb08d82421f43c389661253033d21051b8e3710a0b54673285650596a00
    role: context
  - path: pages/traits/environment/ph_range_very_low.html
    sha256: fa578bc59cfcf47f1b3bff1199bc34691dcaab63d85bbc3b25aef24e6c0f7870
    role: context
  - path: pages/traits/environment/piezophilic.html
    sha256: 04367f62389da34117deee8b2c3c76e1472281e8abf6dea2f84aae82966758e2
    role: context
  - path: pages/traits/environment/piezotolerant.html
    sha256: a8428e6781a08e125072901f201d6993bb323e95efac72642afc559213a3056d
    role: context
  - path: pages/traits/environment/pressure_delta.html
    sha256: 99e7f72fb18de5bcf549a0dedf6d54fb2224dd7a9caba144b6f62bce7e1c4bea
    role: context
  - path: pages/traits/environment/pressure_optimum.html
    sha256: c7a16b339cb6f69630df19ea74335d5ae803779d42886aaefa409d74040f7a75
    role: context
  - path: pages/traits/environment/pressure_range.html
    sha256: 171193eea72b90e87fe0c2fdeec1ee90c23f82edd395ce59f6d739ab77bc71ab
    role: context
  - path: pages/traits/environment/psychrophilic.html
    sha256: 4c0b0b1feab7abb803e99ece54b11bde06ba8f200a0a4581e06d429e86c688df
    role: context
  - path: pages/traits/environment/psychrotolerant.html
    sha256: f9df1782da79d63cc59f0bd5660607e41cb7ebd8d1435b1243320bb423510709
    role: context
  - path: pages/traits/environment/radiotolerant.html
    sha256: 1e2bfed8e7de758a545795c41745c6add5c11051f8b600a1b3b0c9437d4f51a8
    role: context
  - path: pages/traits/environment/salinity_phenotype_with_numerical_limits.html
    sha256: 93b2c00759027d446a66358414dda0eaa974cb72fd7555490a60582268436685
    role: context
  - path: pages/traits/environment/slightly_halophilic.html
    sha256: b1c28e3cf245d2db23235d88e4669c06e5739651fae85262ca675df70436b928
    role: context
  - path: pages/traits/environment/stenohaline.html
    sha256: 11c5aa462b85ea3a9cc4a3e08dc187776c4bbb77aa304a16f1212bb32b2b7244
    role: context
  - path: pages/traits/environment/strictly_anaerobic.html
    sha256: fbaec9e7c43ae7a74cf9dada0b0363b360dc1bf8e7e79e7f013717bc7ba99c98
    role: context
  - path: pages/traits/environment/temperature_delta.html
    sha256: a078bc47977b6ae46f89ea67f393ed5e509c866262eb4781825b421dffc2ea4e
    role: context
  - path: pages/traits/environment/temperature_delta_high.html
    sha256: 641e94db8e7f94ee2e37598e217d904fd73fac88b1dec43d4bf6c10e631aeda6
    role: context
  - path: pages/traits/environment/temperature_delta_low.html
    sha256: 5c5543c935ebf810dbda3c50aa26de6b60c476dc9e19588654feccda683841ef
    role: context
  - path: pages/traits/environment/temperature_delta_mid1.html
    sha256: 003bbf81edb2b38c01a211e1c6002bdea6c99e7b01c4c59baf65746fc8c459cc
    role: context
  - path: pages/traits/environment/temperature_delta_mid2.html
    sha256: 8ec6a02bd4401ce90dd53e3b5c41af8b2c1b59210a916c8f49e58f8b020d67f8
    role: context
  - path: pages/traits/environment/temperature_delta_very_low.html
    sha256: 1caddca630ecfa60ceb3e4deea7885bf513e29eef3a9e202448da0c671187ec3
    role: context
  - path: pages/traits/environment/temperature_optimum.html
    sha256: 4ada5d0db3667f8ac5b46b5ed6a7f3882e253e925fdd63adaa7b6948a78e82b6
    role: context
  - path: pages/traits/environment/temperature_optimum_high.html
    sha256: a76b688272b81031a8dc0a94bce55ec854d2b67e13f495e9c5e841f80b97790f
    role: context
  - path: pages/traits/environment/temperature_optimum_low.html
    sha256: 9f3e9c23e5da9c360790db526e4737e011d9a411f4280f52a48a9c136ef53dc7
    role: context
  - path: pages/traits/environment/temperature_optimum_mid1.html
    sha256: 02a0c52048f33ca027618295ceb686a137095758f3159ae25e524309b6f49253
    role: context
  - path: pages/traits/environment/temperature_optimum_mid2.html
    sha256: 898b5ea85b3c476c410ac249ebd0077b0fbcd15b95f30e4c8ba09c59c2c32d56
    role: context
  - path: pages/traits/environment/temperature_optimum_mid3.html
    sha256: 5cd747dfdb494289f0b344a84347f25aa1728a8c8e7b0f2b12562861c1443fb6
    role: context
  - path: pages/traits/environment/temperature_optimum_mid4.html
    sha256: 83e5c8e66446373c0b595d10968bd9e6db5b2f7232c5ce1a70034ff62a0fc7a0
    role: context
  - path: pages/traits/environment/temperature_optimum_very_low.html
    sha256: d68d00ce5d2dacfd65917d3bb0b1d0f2058fb895c39fe615ec743b7ab06dcd9d
    role: context
  - path: pages/traits/environment/temperature_phenotype_with_numerical_limits.html
    sha256: 9b99dcf199aac07ba5f4833f301327e0cc092a9744d50084dfd422683236648c
    role: context
  - path: pages/traits/environment/temperature_preference.html
    sha256: b1e922abf9216928906fd7c20151c06ba87abbc065b5c8f859e42d2b4987e508
    role: context
  - path: pages/traits/environment/temperature_range.html
    sha256: 0db57d3c039eea3e2c0694d7c391cf7333fa005e0cabd6bc4411501b5decdc5f
    role: context
  - path: pages/traits/environment/temperature_range_high.html
    sha256: e03fe44aad0958ad8f212adb4561b26326e3d3d90136a3bbae5ed3676217da23
    role: context
  - path: pages/traits/environment/temperature_range_low.html
    sha256: 8d1089d017a70d212194dc683454b2048ad26fa93f82ab40bdbfc1692dede656
    role: context
  - path: pages/traits/environment/temperature_range_mid1.html
    sha256: 84618441fa9825fb8fad6fb36c3f6551884c0f8d2e88c29e697a3c30b76e78e9
    role: context
  - path: pages/traits/environment/temperature_range_mid2.html
    sha256: 6bf6ed28cd1e201ac139459a711bdc802e804525c363b4fab1de646ac7e8e60e
    role: context
  - path: pages/traits/environment/temperature_range_mid3.html
    sha256: ac0118ca70195d3e93b86032dc19b2e062de8c3479bd09a3f27a0ad4787800d0
    role: context
  - path: pages/traits/environment/temperature_range_mid4.html
    sha256: 66e405e0a454e79bbd667de7c42d19ba635f58cbb1f796e8f97693a2f52b7683
    role: context
  - path: pages/traits/environment/temperature_range_very_low.html
    sha256: 28e525287a3c7e72c8afa7bae32d0ff32855788fe16cc09d639ebc0b86255cc9
    role: context
  - path: pages/traits/environment/thermophilic.html
    sha256: 90ce489b23716434b424ec8ddce587b696893f06854bf861c5df4e1f7d0eef48
    role: context
  - path: pages/traits/environment/thermotolerant.html
    sha256: 3eec331d314f869e61a662f20b230e1da54afb5f2c6ad6ef514e3e9ef8e4003d
    role: context
  - path: pages/traits/environment/uv_radiation_tolerant.html
    sha256: c9732e3a08a28a4a46535e61f2a81669d6405a3fd3783e1e35482717626b65b7
    role: context
  - path: pages/traits/environment/xerophilic.html
    sha256: 954f611231658f25bf40429b08ce857044bb294bd4cecee9b48848a43ef13842
    role: context
  - path: pages/traits/environment/zinc_tolerant.html
    sha256: b5536e6193d5ebd93105ae2edfbb4e29883cc230add747ff73e2b381009cbf43
    role: context
  - path: pages/traits/genomics/abi2_system.html
    sha256: dc46c96a0add3707dc87ea053f3555274425ecc15b1a532c5e0ae44c5ec26d32
    role: context
  - path: pages/traits/genomics/abia_system.html
    sha256: cab716220f9f7bb67be06b5321e1ce53015ac722046efe653bec7fb65ce34817
    role: context
  - path: pages/traits/genomics/abialpha_system.html
    sha256: e401e4ace65b697fbfb87d5f8fa604777e0191e12d3df4a67352d3439db26ca6
    role: context
  - path: pages/traits/genomics/abib_system.html
    sha256: fef80657e1c65812af9833a6898308b8d7bbe27f99f5b96808d8b2f1fc6aa027
    role: context
  - path: pages/traits/genomics/abic_system.html
    sha256: 9993394c013e2f68540b50b14ac4bbfbf9a5ed6ac825a3697670e7267c95ed41
    role: context
  - path: pages/traits/genomics/abid_system.html
    sha256: 019476b7fe318f584c4e24ed8468bdb2b7aaa0239f4bae0e321f2215d8a5eb20
    role: context
  - path: pages/traits/genomics/abie_system.html
    sha256: 3cc492ac12f441cba5035d5b1f32faa515c1a46730fbc27586198c60f69aa79f
    role: context
  - path: pages/traits/genomics/abif_system.html
    sha256: 7fdbc06e8f7f1ca1cd5e13da17b975e70c198450a3d69439742a3e6c9a617982
    role: context
  - path: pages/traits/genomics/abig_system.html
    sha256: 567ef25306684868f0b9fc036e138d5862534e9559c20067f55ca0a09795572d
    role: context
  - path: pages/traits/genomics/abih_system.html
    sha256: c93803f1c3f58034d64d55dcbcca59954a5b6989c57505b8de95639449cb27db
    role: context
  - path: pages/traits/genomics/abii_system.html
    sha256: 0c05755174f2c0b77de232f963cc52829335339bf97a6065370a5e64b84864a6
    role: context
  - path: pages/traits/genomics/abij_system.html
    sha256: 162e76b8d63f47baca8d60a7ca1c6caff230fe06c85149e7297c5324d58e378d
    role: context
  - path: pages/traits/genomics/abik_system.html
    sha256: c0cec7accea5f2e837fe45089954fcb15bf128101f9f96084c049f88b5245dd8
    role: context
  - path: pages/traits/genomics/abil_system.html
    sha256: e7933dd52e35aa50b254c7f99e81498a30dc02931eee7319cd7cd93d0fa815bf
    role: context
  - path: pages/traits/genomics/abin_system.html
    sha256: e72452675443cf70d301a212e21ac66f27e1b2f9fdff25db7b9ecae4b27762e9
    role: context
  - path: pages/traits/genomics/abio_system.html
    sha256: 9f3624aad9e6097ade63bbb885548d7ec1f6da1d64c56595cd544304ff127b82
    role: context
  - path: pages/traits/genomics/abip2_system.html
    sha256: 521748a65be248dac7d30937846fbe92f1524a04ee3ab72f38107a47cc522b51
    role: context
  - path: pages/traits/genomics/abiq_system.html
    sha256: f3e89547e4cb4075d8495385fc7cdec7fec9b26c1495b82023913c3745b74bab
    role: context
  - path: pages/traits/genomics/abir_system.html
    sha256: d79646519d236a3d6ec8c1186497a487e7217c34baaa88ba1a4020a7d4a6c9f7
    role: context
  - path: pages/traits/genomics/abit_system.html
    sha256: 800c9e4238c51212f26db4485ab4d087835de1d39405464632fecf44ed3da6af
    role: context
  - path: pages/traits/genomics/abiu_system.html
    sha256: f516ef4e93aa74865479f02026b10a7040e43907a22968c922a2ef841461389b
    role: context
  - path: pages/traits/genomics/abiv_system.html
    sha256: 5c361b1c0d74ffe5811225c5071a29ecd5197b10af015872da5b199642b65646
    role: context
  - path: pages/traits/genomics/abiz_system.html
    sha256: 118bda35efcddfc5d618f44dc80236f7735a7c6202907f9d3011be8a06353fd2
    role: context
  - path: pages/traits/genomics/abortive_infection_system.html
    sha256: 91c4d9ccf7aa8b2ced2414bf980352ddf300d866d6bedd1922fd082988a6507a
    role: context
  - path: pages/traits/genomics/aditi_system.html
    sha256: a675e475e155f84e710f57cf28b7686f820358ba61dfa8d0aa45d75da6758c6a
    role: context
  - path: pages/traits/genomics/ambrosia_system.html
    sha256: 0e1cafc4ebbafdcdaea16c9e365c28c9012f38fa503cf73ea5266d36186c445f
    role: context
  - path: pages/traits/genomics/apsab_system.html
    sha256: 1f80d193316018eed8e9ac2cb0ef752ded3862b4f3a99f93a3370c284c4641f7
    role: context
  - path: pages/traits/genomics/aristaios_system.html
    sha256: 604b6021acc9ff8f90d544b1183461e9d454d5385238715d63852b75e2e3dbab
    role: context
  - path: pages/traits/genomics/armada_system.html
    sha256: 38220966212f8d56d858e9af7ed0d0a626fb0f7980f1f2f66299bf15f9144488
    role: context
  - path: pages/traits/genomics/audmula_system.html
    sha256: 49f02bbebbbe6b77d1ea3c9a09924127f612536b852b207b2fd238e1eb3a848a
    role: context
  - path: pages/traits/genomics/avast_system.html
    sha256: e8267b9cdbea8a88ee1bfce7106a02bf2d0384bd846e19bc773e63accf991a85
    role: context
  - path: pages/traits/genomics/avs_i_system.html
    sha256: 72b291145e0bedcefdd37d4caa4923072d50963f4722c02213bc78736f1fc4d6
    role: context
  - path: pages/traits/genomics/avs_ii_system.html
    sha256: 6eeafe719c0e3930ce3ed3cc6b6ed344d5d50de48f3790931f6d2594377c9943
    role: context
  - path: pages/traits/genomics/avs_iii_system.html
    sha256: 08ea74043cb81b5ee21347543c3e29eb37c281f2b47c59b2db475dd73b6a6dac
    role: context
  - path: pages/traits/genomics/avs_iv_system.html
    sha256: 3b0781b4eaafe7db858c16183d1118777ea7ed270ceafb99ab785b124949da06
    role: context
  - path: pages/traits/genomics/avs_v_system.html
    sha256: bf8651eb46c9e7ae41a685143bbbfca8126ffa5bc2671e11674ae4d36a5b42d6
    role: context
  - path: pages/traits/genomics/azaca_system.html
    sha256: 9ac99fa9f4b0466c418c169a39c6478b738254871f16631a11571c3790402f40
    role: context
  - path: pages/traits/genomics/belenos_system.html
    sha256: 783a168ab8189b288b0396cec4f9c16d68461d3d1240dfe0432cbfe5de9e08d9
    role: context
  - path: pages/traits/genomics/belisama_system.html
    sha256: 4f0a6b62dc79d578587c9ee855f34130e76ae8e661bb41f69c0eba0706f45b64
    role: context
  - path: pages/traits/genomics/bil_system.html
    sha256: 2e0f2ac40a695fe2b71425980a61766d8ee36e335e140a97fbe6c265d9547396
    role: context
  - path: pages/traits/genomics/borvo_system.html
    sha256: a803d3d4efddf88cc72846c2f00b6af71ccd729401682e7716f76c0a3691cb9a
    role: context
  - path: pages/traits/genomics/brc113_system.html
    sha256: 8f324031bf6199322122315f4270eb30355538a80f825a253521e2bb88407548
    role: context
  - path: pages/traits/genomics/brc142_system.html
    sha256: ccd168499746b1bae5c54e6fe1b659c9839b62a6ce6e5a0554610758665139bf
    role: context
  - path: pages/traits/genomics/brc167_system.html
    sha256: f1696a055da85ecce4690ce2a8e241091e7f0b311547e09a04060596bcfd47b3
    role: context
  - path: pages/traits/genomics/brc217_system.html
    sha256: 2f92d4908d330885a45565572f618892f8a9677b584e73519624315dc368e16e
    role: context
  - path: pages/traits/genomics/brc22_system.html
    sha256: 4e85bac59612a14dae5af06b5d7e506173e1f86ff8547069120be9a7060b7e28
    role: context
  - path: pages/traits/genomics/brc233_system.html
    sha256: 43e20dba119d004375a3eabd3f68f17dd60eca518a9dfe1e3851ae8bc1870e3f
    role: context
  - path: pages/traits/genomics/brc23_system.html
    sha256: f66ba8f772c17e8702aa8aeb272b5f0e75639e675f964fb4ef0e2d1701e76d0d
    role: context
  - path: pages/traits/genomics/brc24_system.html
    sha256: bd8eb09645ff4feb8f41cd490cd839536266c90912a04563199f4354cd5d9553
    role: context
  - path: pages/traits/genomics/brc59_system.html
    sha256: 3a14c52aa317c3483fb209eb4ea26ee597564912d32e0e24b447a30419072864
    role: context
  - path: pages/traits/genomics/brc76_system.html
    sha256: 9db859509218267d0cbdd068c8b288c7bae36351391098aeef6c2bc2bc367a1c
    role: context
  - path: pages/traits/genomics/brcwgs21_system.html
    sha256: 386684daeb3f33e8fea05b6e946bda9f3973bcbaafe26e83cefb8c1ca64cbf80
    role: context
  - path: pages/traits/genomics/brex_system.html
    sha256: 8d4e4d7a11fc73eea374bbbaf9b5dbb15023ca21201f903cb1d824b0075a9683
    role: context
  - path: pages/traits/genomics/brig1_system.html
    sha256: e6aaca46637c45fc5bc92c80a04bb73a546fcb0743d66460d28d8efe258d24b9
    role: context
  - path: pages/traits/genomics/brigantia_system.html
    sha256: 714ed3ad85bf4febe75ee7ed6cc9533982f3a7209ee51525ee13786e21cf003c
    role: context
  - path: pages/traits/genomics/bsta_system.html
    sha256: 6122966a2648266c567c7e4d26e77991c5e9983d310519c26073eeeebbfde412
    role: context
  - path: pages/traits/genomics/bunzi_system.html
    sha256: 785361108caa21734175ebcc28bb4040b4a55ba785996bfbafdc43651cf67a46
    role: context
  - path: pages/traits/genomics/butters_gp30_gp31_system.html
    sha256: 1736d37f3e79b5ab30b1aa49ac6eb40978dc170a7b05b1c8f859dfc82098379c
    role: context
  - path: pages/traits/genomics/butters_gp57r_system.html
    sha256: a1a014ca9fa4273ef29c509fae359854d55b239cd2f0edbbcadffb671505c6c7
    role: context
  - path: pages/traits/genomics/caprel_system.html
    sha256: b9e8ca66b65bf305405ee7bc24ed649477a67e31b2b9e441012bd9fe91ee1b07
    role: context
  - path: pages/traits/genomics/card_nlr_endonuclease_system.html
    sha256: ea85bd0575f336aa5feed7370d262e67df32d689c2d07db414ffb386924055af
    role: context
  - path: pages/traits/genomics/card_nlr_gasdermin_system.html
    sha256: a5e59265106478ebaba4cf8732e6ebf6627410fb993b21957b5be404372922c0
    role: context
  - path: pages/traits/genomics/card_nlr_like_system.html
    sha256: bbaeab5609a48349657a51bcc8f1b3b3b586bfeb9c89e123b1d9f5f5f6d58b0a
    role: context
  - path: pages/traits/genomics/card_nlr_phospho_system.html
    sha256: fa986891d150790bfb4bc2a07d6fb702f46102ae6fde413f2fa3ffa655323cb9
    role: context
  - path: pages/traits/genomics/card_nlr_subtilase_system.html
    sha256: 617d90cc022d565097d4dda938c04792b4b16a4e9b26443bdcb2eb00c210fdd0
    role: context
  - path: pages/traits/genomics/card_nlr_system.html
    sha256: 5c740d29b4ef3cac3911379a0deac5b08d1f3ccb6116b3a65a14c125a8d410b2
    role: context
  - path: pages/traits/genomics/cbass_system.html
    sha256: 94800c35b6e7864f27d2ebdac75e5607704ce7ef3e667d9ce616696cf46a85d6
    role: context
  - path: pages/traits/genomics/ceres_system.html
    sha256: 5df730b975200f15e06dd7cedd718e11b1ea25aa884118865d94cb560f349437
    role: context
  - path: pages/traits/genomics/cernunnos_system.html
    sha256: b123d5de31ea193443e1b82492ac060fb69d24b12cce5f0ed4ea6d8c097b1752
    role: context
  - path: pages/traits/genomics/charlie_gp32_system.html
    sha256: 35e7f23a51b785ff8b102315457097a075e602831d4680a6654eda502cea5608
    role: context
  - path: pages/traits/genomics/clover_system.html
    sha256: bbe1df220496577f4e2b930c372fe12b3a23e836bb7aefa1cf86e609cca7c8e7
    role: context
  - path: pages/traits/genomics/cmdtac_system.html
    sha256: 651dd5b6a35d4241ffcdf86f9485d6d8dccbc264e0e477acb1e8d646b8a7a7e5
    role: context
  - path: pages/traits/genomics/coconut_system.html
    sha256: fece668cf654196b7bea14095b9a5966e7ee7b30d29ca4e40a5762ec4213cb2b
    role: context
  - path: pages/traits/genomics/codon_usage_bias.html
    sha256: 4f310d15dc639cfa14dea507d769a4fd6cd18520e53629e9ca85f34c53da1e03
    role: context
  - path: pages/traits/genomics/crispr_cas_system.html
    sha256: c7614e9dbb47dcd15abc786b3f10c1ff4301c4b8c72eeafb049645a191803c65
    role: context
  - path: pages/traits/genomics/crouga_system.html
    sha256: 7b5aee0b3e463bf9b3d9402281072ab785cb49990d5a1c38945df1f26e0b973c
    role: context
  - path: pages/traits/genomics/dag_system.html
    sha256: b937ce5cf405796e83f464b460efd448a03ff869fd4f903525df2f3efd55cce3
    role: context
  - path: pages/traits/genomics/damona_system.html
    sha256: 71477deb3b1a8a5cc132836b00233db252c531fd0080832fbd62316378f951a4
    role: context
  - path: pages/traits/genomics/darna_system.html
    sha256: 33aa4064f163766a265a0a33dd55555ee4d41ed802434631936831b3d5cb5aa4
    role: context
  - path: pages/traits/genomics/dartg_system.html
    sha256: ae89185f992b951d03e4e569dfba242867d9764f25c786639efac16ebf995efa
    role: context
  - path: pages/traits/genomics/dazbog_system.html
    sha256: 6efdfa57a932caa1dd653d94ef0f9703a1b87716a776cb9ed012f61519cd8d1e
    role: context
  - path: pages/traits/genomics/dctpdeaminase_system.html
    sha256: 0f0ae2aa09cc779ebc869e4b88283675e6f20e692c33be7923f1283406462e39
    role: context
  - path: pages/traits/genomics/ddmde_system.html
    sha256: 25dfcd882816b4b856f59d4ccd991dc09465586b2918cdd4b9dd6712077beba9
    role: context
  - path: pages/traits/genomics/detocs_system.html
    sha256: 70ac7c6034de22d697de5afd4ed814c3eb6fb6b73b1eb215723461ca1241a148
    role: context
  - path: pages/traits/genomics/dgtpase_system.html
    sha256: 05a2511d66a86119eaa9e52b36d1802b8ba5aa34149d7e09b552f129d9e13785
    role: context
  - path: pages/traits/genomics/dionysus_system.html
    sha256: dfc21307c3fd91052f48737fb7e98d9925c116817a7361bbd0676e12ac5380c7
    role: context
  - path: pages/traits/genomics/disarm1_system.html
    sha256: 72b4cb6ca8c869a3c8595457be1f28ac4f8b8a1fe75c10ef95a8f54e526857a0
    role: context
  - path: pages/traits/genomics/disarm2_system.html
    sha256: b39e8feedf323008daad4273209b2c2988de07acaaa55cee87ce3b27b73a47f4
    role: context
  - path: pages/traits/genomics/disarm_system.html
    sha256: cd3eaea5ee197a9a9fa0a4e0bde92f4790f452529fbdfb3aa1220d5751597643
    role: context
  - path: pages/traits/genomics/divona_system.html
    sha256: fe099b4b0bec5b3696664f616e0e24c090223098535a3a2bf6fb1d1fa63c8cd5
    role: context
  - path: pages/traits/genomics/dnd_system.html
    sha256: 915e1c70fbc2bc58e77958357a305de2101ee75db954a48bd6a82bbfb2f8c143
    role: context
  - path: pages/traits/genomics/dndcdea_pbeabcd_system.html
    sha256: 510c23e093c1f117423fe855e55037537049a7a6cc0739bf4dcf1e9fb8959d07
    role: context
  - path: pages/traits/genomics/dodola_system.html
    sha256: 43c6da91129e1eea35b6e22d9746f56d07385e5a4e86ec7d9751ecb39e0975c8
    role: context
  - path: pages/traits/genomics/dpd_system.html
    sha256: bd16989a2fe8885e776de1abda65e5d50d49f193c344084c6f3330f37aa6f9fc
    role: context
  - path: pages/traits/genomics/drt1_system.html
    sha256: 91faf9d8480140a56a9e9755ae3e6d1d4946f5f668f4e8467302274c7cc83e4d
    role: context
  - path: pages/traits/genomics/drt2_system.html
    sha256: d660cf944f58241a98bfa06e55db135f50b656899478dd4015e3a9c48accbda7
    role: context
  - path: pages/traits/genomics/drt3_system.html
    sha256: 43236711545646242715010ee788d7b9c0d93e057d8a1c971a805ccf0c34e169
    role: context
  - path: pages/traits/genomics/drt4_system.html
    sha256: 395260d5ae8f99e1917371801a0e41a3184d3736ed409a9e8af546ecd946cd40
    role: context
  - path: pages/traits/genomics/drt5_system.html
    sha256: dcf3cfdc9bbbc18f1920226b79799bc6386dc5441cc1d259b83983e6ad4f378d
    role: context
  - path: pages/traits/genomics/drt6_system.html
    sha256: 3c789bbdde3c240c9aeacd407c88729f57a547500aaf3cffa456ae072ee2b389
    role: context
  - path: pages/traits/genomics/drt7_system.html
    sha256: 5a6ca0811ddf1e4967720ecdc1d109aa3c45e8074f076756b9d8eec98b6b1538
    role: context
  - path: pages/traits/genomics/drt8_system.html
    sha256: 30c53d8fe5d2528193f958ee3457400469f1b7a3f58f92304cc34d7186a1e899
    role: context
  - path: pages/traits/genomics/drt9_system.html
    sha256: 3abb352547deb57a7fcd581503765be4dfcf68c5f2d7153cd185526e9c2fbfca
    role: context
  - path: pages/traits/genomics/drt_system.html
    sha256: fe8d1f11948fa083d10256b392ecd271bb8268ad0343ce4cb0f00e2c10dbd886
    role: context
  - path: pages/traits/genomics/druantia_iii_system.html
    sha256: 19a1d3dd65d4b740c2f6c7e880de4e7a8a9e56484dfdaa73b87701e63b7710e0
    role: context
  - path: pages/traits/genomics/druantia_system.html
    sha256: 40d38d948f704c692f16c5b805e72e940cc683751c1bc5872e787f05e6a33324
    role: context
  - path: pages/traits/genomics/druantia_type_i_system.html
    sha256: 20adb25b9eef7fef48f76d8138116aad37db7cf9bfdf745dff2ce8eff192ac11
    role: context
  - path: pages/traits/genomics/druantia_type_ii_system.html
    sha256: a4cce09e18e90e77bca76e2055e5e5344b7114aaf3eca99c34c071a524eaf4b6
    role: context
  - path: pages/traits/genomics/druantia_type_iv_system.html
    sha256: 7be0747fe22cdeb2fcd6be881f56645a5829d0a2c55f22ade6189a66d5bf8b51
    role: context
  - path: pages/traits/genomics/ds_10_system.html
    sha256: b879ea6d416bcff6531f44f4751858b6e5036bf82a9b395eb5dc95d7c612e72d
    role: context
  - path: pages/traits/genomics/ds_11_system.html
    sha256: 0df7680348ee33466571e8eadfac1d3a00a91c2a90114ca0e237efde3fa4ea4a
    role: context
  - path: pages/traits/genomics/ds_12_system.html
    sha256: 5957d66e9c11b05366a054a94cce0e648e65a0a679b755089e63412dc7ac8296
    role: context
  - path: pages/traits/genomics/ds_13_system.html
    sha256: 93e167f12263f515c282b224491b489227f0c2a826c53732daeaa32f8e716d50
    role: context
  - path: pages/traits/genomics/ds_14_system.html
    sha256: 877e8d251f8045092a17fdea376d58659e5771d0bc0846ef50306cbf633c5bb1
    role: context
  - path: pages/traits/genomics/ds_15_system.html
    sha256: 464182d99d6a118ee14cda722ece178ea4d3bbb4cb959813ae0c3a0493f0200c
    role: context
  - path: pages/traits/genomics/ds_16_system.html
    sha256: 8946477b1f727d085b96ba9b89161fc695b22f936d4018910fc559fbdc322e25
    role: context
  - path: pages/traits/genomics/ds_17_system.html
    sha256: abd70f2e7ba2df373351e060f978f17c0c5f9aa2d2d873391920433448f88cb6
    role: context
  - path: pages/traits/genomics/ds_18_system.html
    sha256: 8c314321a7db3fa9014c216669e0c1fe8c6a0a269ed6e65272d36d8677576715
    role: context
  - path: pages/traits/genomics/ds_19_system.html
    sha256: bdd57608af22302e88095527baeb3b77608ce82b86ccd94889f9147969f9f302
    role: context
  - path: pages/traits/genomics/ds_1_system.html
    sha256: 23526d2133863bfa48e2d782a739259ff480daddf50273f2a8516ba4f5bfe076
    role: context
  - path: pages/traits/genomics/ds_20_system.html
    sha256: 2bbd506f66d4f3a4518da864fd7c94c5040431a5de18d03407fc4b4bd3ba0b0e
    role: context
  - path: pages/traits/genomics/ds_21_system.html
    sha256: 148fd83e21219e17bbf89ca5a808ca89c91d26d894badbae03d44798252a43d5
    role: context
  - path: pages/traits/genomics/ds_22_system.html
    sha256: bf121127b8c8345c59a97034e9ead31e767787221dbf5a7b176eaafd859d2826
    role: context
  - path: pages/traits/genomics/ds_23_system.html
    sha256: 02063e07fe212c7aefdd445bfdbdab2089339447ad55638d2af38d28113c33d5
    role: context
  - path: pages/traits/genomics/ds_24_system.html
    sha256: deb92867ead5e7d098ac390087dcce59c4d7407c3c62827ee8164a92428b2820
    role: context
  - path: pages/traits/genomics/ds_25_system.html
    sha256: 48af26ec635cf3092f041fe30f49a23fa9764ea61b19c212fa2c7780e5f694ff
    role: context
  - path: pages/traits/genomics/ds_26_system.html
    sha256: b63dea9119b460c97e26cf02a49994f07b2ae2c847336c7c7efe46d96c5b71b7
    role: context
  - path: pages/traits/genomics/ds_27_system.html
    sha256: 9f783d049cf782da64e2bc132724e3f9992620d9691bdff87f8e319454fd1328
    role: context
  - path: pages/traits/genomics/ds_28_system.html
    sha256: b2f2542149c640447a127afbd3c1bd1f199b151d3ea4a90f0d508a94f9c829f5
    role: context
  - path: pages/traits/genomics/ds_29_system.html
    sha256: b85ba3bf62af2d1c24caef31313356b7d61e33b81e334067c0709f1835aab6d2
    role: context
  - path: pages/traits/genomics/ds_2_system.html
    sha256: 3b0560cfa9207166134de534132bb4e8e8b44198e321ad189354e87790b77111
    role: context
  - path: pages/traits/genomics/ds_30_system.html
    sha256: 4f9150c130dfcd8af661ec6f349af42a5d728339cf4bee2b132c99b63a71ebfb
    role: context
  - path: pages/traits/genomics/ds_31_system.html
    sha256: 84fb6b68843db55d43d804b236f1c7d1d38b37906aaf5ad4d9793c73c7bd7b92
    role: context
  - path: pages/traits/genomics/ds_32_system.html
    sha256: a2704a63c6be2a2ed6a2f32317bf8bcb3cb7e38d06fcfa7be3e93b3131e0684d
    role: context
  - path: pages/traits/genomics/ds_33_system.html
    sha256: f75412eb552319cd4693b5281c7524d0d9eea1bd4c0610054eab1e8ad4a47f8d
    role: context
  - path: pages/traits/genomics/ds_34_system.html
    sha256: d38a689df0bc47ba1f9d11143da802303e775532f552e1bed1ba34a041c5529d
    role: context
  - path: pages/traits/genomics/ds_35_system.html
    sha256: d26893fd28b918e82ad6dc56f69911b3db13d7053dfe43d43c254a4bb84d705f
    role: context
  - path: pages/traits/genomics/ds_36_system.html
    sha256: 1a166182fa7355bfe157cff196b5b7b22329d841beba9a6484fac14b1b2f9b89
    role: context
  - path: pages/traits/genomics/ds_37_system.html
    sha256: 3e8e3717668d11fb1038c92c6d3631b2b5c7f4f1f9ce54f64c1d158e7e4901c8
    role: context
  - path: pages/traits/genomics/ds_38_system.html
    sha256: f50b8759479d1a77c662c7099e50d9f1bec737b84063c586a848185afd247836
    role: context
  - path: pages/traits/genomics/ds_39_system.html
    sha256: aa46d1a4a5e58a96f5c4f81bee4d036a7a13f64a58738f29a9ecbe9c84694671
    role: context
  - path: pages/traits/genomics/ds_3_system.html
    sha256: 5cabf79134b653eda0bfab24e85a5c8f49125a3164e43d6044808d9b79793aa7
    role: context
  - path: pages/traits/genomics/ds_40_system.html
    sha256: ef4b5852df7c360cc05db51058222536d56216a07cbd343c67b4b2589680e436
    role: context
  - path: pages/traits/genomics/ds_41_system.html
    sha256: 4512a1fec1c873f58b2061f769074d23421b707e5af3224e2b21c14969c8fad1
    role: context
  - path: pages/traits/genomics/ds_42_system.html
    sha256: ba5b2ad0399be1c1175e6d1fad7ca69bc317203f267fc500a16ae69cf2193218
    role: context
  - path: pages/traits/genomics/ds_43_system.html
    sha256: 959279bf1193166e076345a7ccad45ae9a0d2e9ccbe88fec944db90c1534cd97
    role: context
  - path: pages/traits/genomics/ds_44_system.html
    sha256: 4fa40abcebe1892b70fc737c737b40e155a5613a3733a1cdd85ecd1f4e0b1964
    role: context
  - path: pages/traits/genomics/ds_45_system.html
    sha256: 5152a952caf9ce52003bdfc81e6996914ff24609c256a4c2a2dabc9f8b42076a
    role: context
  - path: pages/traits/genomics/ds_46_system.html
    sha256: cfbc97df31975c5f9b5ed0001da82539b1b86a39afe77be7a4f5d7dfe2c1121b
    role: context
  - path: pages/traits/genomics/ds_4_system.html
    sha256: 64e073e583fcc65b0d3f6707eb337b299ab617ca4e3b5b8ad8ac4df0106aa442
    role: context
  - path: pages/traits/genomics/ds_5_system.html
    sha256: 69a84e466c275ee76130c1cdda4777ed25283c41390d4b7f37a7174eeab5ca63
    role: context
  - path: pages/traits/genomics/ds_6_system.html
    sha256: b84739a0d206139bfa86d6148a544985f03b2b00df6fc72aeae3dc4258e9e343
    role: context
  - path: pages/traits/genomics/ds_7_system.html
    sha256: bd8076ac491af505eee1e8551f9ec860a50eca0e8505b8f250499a6350547827
    role: context
  - path: pages/traits/genomics/ds_8_system.html
    sha256: 2d20ded418f45d8c1af59f8be8f57ca1eb39610d14d6bfc08d22fa604049e2eb
    role: context
  - path: pages/traits/genomics/ds_9_system.html
    sha256: 0c86a8a5c4670a91d2c90abdbbe689a91bd43b4797ee8ffdb3eb8258593787f9
    role: context
  - path: pages/traits/genomics/dsr_system.html
    sha256: 210a061a8e0c5202fb92f75d90cadd6f4f1736614e25ce2ce735c70df392eb7c
    role: context
  - path: pages/traits/genomics/duf262_schlafen_system.html
    sha256: 1718abba5cd8f7446f08f9a163a9b2dac4d451e412e778b15039ff9a6287371e
    role: context
  - path: pages/traits/genomics/ecokmcra_system.html
    sha256: 94dd3dd1dc7ee41a3715883f81cf9ea4292b75ec096f3e4413db47de6bc61c7b
    role: context
  - path: pages/traits/genomics/eleos_system.html
    sha256: 7cea192b9b6fa0598ca7044ab5acae54f0373cabe1d6a37e0350fe47d2170a77
    role: context
  - path: pages/traits/genomics/endpacf1_system.html
    sha256: 105885412a3b5b1f39f7576ba4299d4ea8623c504b729192e7a72bd41d77b265
    role: context
  - path: pages/traits/genomics/epona_system.html
    sha256: dfbd93577e572056878447fb68d3ab26a0b739e86c29986474a4c318505af9fc
    role: context
  - path: pages/traits/genomics/erebus_system.html
    sha256: 388ddf01ed9c3df1312cb91393ed986bed91a9ddfe7a27d3425559ca2c875132
    role: context
  - path: pages/traits/genomics/esos_system.html
    sha256: 04d1656a4b887d7c0f3f035b8ef2d31e405352c3bceee6477a5cca5f8d5195a0
    role: context
  - path: pages/traits/genomics/fliodhais_system.html
    sha256: 72984cfabfe253e6e4686344989a432241681e622292fc2f69375b8e47e3858c
    role: context
  - path: pages/traits/genomics/fs_giy_yig_system.html
    sha256: 7cf11f439cc7e83d4cf4c7c100ed3cc1b3c18f17e8d7742f58fe10aa5237ac44
    role: context
  - path: pages/traits/genomics/fs_hepn_tm_system.html
    sha256: 8c970910c6af21dee3f4c2135e198a3761008646b3e4dbfc067e8d521dfe5ede
    role: context
  - path: pages/traits/genomics/fs_hp_sdh_sah_system.html
    sha256: 2f8163cd9b68b43ff1e564b30d0f6095c879a194b9d264016230725bf7cc2516
    role: context
  - path: pages/traits/genomics/fs_hp_system.html
    sha256: 3820f134ff6d3c13d5271c65b72c9cfc8554ab31d790fa2345324b23885b638e
    role: context
  - path: pages/traits/genomics/fs_hsdr_like_system.html
    sha256: 6a596ed6aa517299b2c1a9705672b694ee0bc00ecf714cf6b19ea38047e1ce33
    role: context
  - path: pages/traits/genomics/fs_sma_system.html
    sha256: 61502f4e00af8164fe98fdffaff22a7d636f784d63bd4b53d1fffff128f80ee8
    role: context
  - path: pages/traits/genomics/gabija_system.html
    sha256: 3f66b84f45acf3473d2c2d4b1a3f25c8b8eccf1390a025b768a236705e6944d3
    role: context
  - path: pages/traits/genomics/gao_ape_system.html
    sha256: 8bf96994593f0d479bf32a42df7de425c2b202039edeba44d03ffb2ea90a531c
    role: context
  - path: pages/traits/genomics/gao_her_duf_system.html
    sha256: 9c39c69a5942b506c9cb4ec51b27f513ba90e9848fbd85e38b3957a65fc0034c
    role: context
  - path: pages/traits/genomics/gao_her_sir_system.html
    sha256: 79c126fbc7d45855316b335fa584553735255e5a90c8b60e883dc55cf03950a3
    role: context
  - path: pages/traits/genomics/gao_her_system.html
    sha256: 3ce4e34ad1bf9e4665dd8d061ad3094cf1a977f3590c1549856c6f753d494eb0
    role: context
  - path: pages/traits/genomics/gao_hhe_system.html
    sha256: 71218be4a85d4df8c48a2a0bb631f2dfb1ab352d87e5e955c810ac686b14dfcc
    role: context
  - path: pages/traits/genomics/gao_iet_system.html
    sha256: 22131e5083e6cde67f8bb51dbdd59ea04493937249533e454548c9f23fe502bf
    role: context
  - path: pages/traits/genomics/gao_mza_system.html
    sha256: bb9cb4ab5b9773d7066cc377a07098c8ad8d17598fe97be97198e62dc3ecd1fe
    role: context
  - path: pages/traits/genomics/gao_ppl_system.html
    sha256: 8e4243d859c50ba641228834002f5354a7d31d4e00578c6718d7199384899e03
    role: context
  - path: pages/traits/genomics/gao_qat_system.html
    sha256: 18788a75a5fb214d18b59fb7e819af7598b503fb6e65a769083bab00037ffecc
    role: context
  - path: pages/traits/genomics/gao_rl_system.html
    sha256: f06e5fff1ec1ed346abc72d195353646af9ca8e1a8efc018f393b6e350c68fe8
    role: context
  - path: pages/traits/genomics/gao_tery_system.html
    sha256: ab47285adc1691a3081cf03641cac1f62217ec136a49d7e93f259ad2c66ac536
    role: context
  - path: pages/traits/genomics/gao_tmn_system.html
    sha256: 5a23d769c87696320bbb187cba586f4ea5b01bd2ff3f21f185af2a5bfac1a6f6
    role: context
  - path: pages/traits/genomics/gao_upx_system.html
    sha256: 7c784be2315a19558ee6469e1443f00bbe285376c3b8199adced197e62894a96
    role: context
  - path: pages/traits/genomics/gaps1_system.html
    sha256: adc5d1e64b3368454963c6060e6f65c08ae5c19f6d72898f2663c9c3b34c96be
    role: context
  - path: pages/traits/genomics/gaps2_system.html
    sha256: 2146321c70b999f68b8c61338d8eea42c565a1e93119642e0c6d3b499bc822e9
    role: context
  - path: pages/traits/genomics/gaps4_system.html
    sha256: 2b2e7e2ca570f460c1a536941c66cb43793c19dcaf5b060ba25226ec8b938fa4
    role: context
  - path: pages/traits/genomics/gaps6_system.html
    sha256: c38e698d56a885fd77053d63dc54c1d99b5920b29fe4fec9cb1cd40c04d24e81
    role: context
  - path: pages/traits/genomics/gasdermin_system.html
    sha256: 8da0c2bbf8e2f587889e9b1be5364f84150ead308c70af2f0d2e0a25197825fc
    role: context
  - path: pages/traits/genomics/gc_content.html
    sha256: 05b4c996699d2be7b89ca31bee8ccd39799997366edd3931088b26112e5c7270
    role: context
  - path: pages/traits/genomics/gc_high.html
    sha256: fd38cc65a856a05cbc79ccd17f8da52213d518bae0616eb25e638ac252d92753
    role: context
  - path: pages/traits/genomics/gc_low.html
    sha256: a4cfcf2850ebafc2a19148f1e5b49208ef50938ea6e5ebb10c652a6b172d5d01
    role: context
  - path: pages/traits/genomics/gc_mid1.html
    sha256: 26b62bb5e3b9df92dae153e94bebb5a8f8181ee2b2b6a94115a46197087698c2
    role: context
  - path: pages/traits/genomics/gc_mid2.html
    sha256: 41fdba76b334bad1723a3c850f2434d074ccf7cba4db6ed2ce33e15a9a8920e1
    role: context
  - path: pages/traits/genomics/gc_skew.html
    sha256: 970630e69a811c4c1e61423ad8d8c4354765bb71f60f7362f730549953234103
    role: context
  - path: pages/traits/genomics/geb_system.html
    sha256: 9b221cb731ac2afe5c71de579925057f86596d292d23b5548d5dbac750adc1a4
    role: context
  - path: pages/traits/genomics/genome_size.html
    sha256: 9e08b3fde62d1942b5e4c59c56d831406d2720859857bd522bf6ceab221ee053
    role: context
  - path: pages/traits/genomics/genome_streamlining.html
    sha256: caab884ee1860c9be0466c61a5b07cb1257c8381d5d9af6a2b3bef696c1df196
    role: context
  - path: pages/traits/genomics/genomic_island.html
    sha256: 92ef62e1165e8219d15b9bc4f1c79a2ef02485111eee3bdfa59bc406db35f2cf
    role: context
  - path: pages/traits/genomics/gmrsd_system.html
    sha256: 4f0bd804beb44cf7a6580092a252f64de12ad562a169e7d973d1ac189756431c
    role: context
  - path: pages/traits/genomics/hachiman_system.html
    sha256: aba3ad6c12fa0791c1d2931df291ca3ff56cfd6419dd435e0e1703e7dadabb88
    role: context
  - path: pages/traits/genomics/hachiman_type_i_system.html
    sha256: 99dbc4d0ad942a8c57acc7b8c31dab5003c12ad024c3ea50ecdb0e28a5d0888d
    role: context
  - path: pages/traits/genomics/hachiman_type_ii_system.html
    sha256: 733fde6966371a1b0c66cdc107afc83a5df0969003e8b9b701a5b8545e8fa387
    role: context
  - path: pages/traits/genomics/hailong_system.html
    sha256: 5a1c8b71e3607522b8a8e38a8408d6f5d1adda252544e160a7e2392b16b31cf2
    role: context
  - path: pages/traits/genomics/hec_02_system.html
    sha256: 13bef371ee40cd9b249f95df5e9d37df5fbed04f2e35f539c4c2876e8ed08b6a
    role: context
  - path: pages/traits/genomics/hec_03_system.html
    sha256: 38bdc659368ccc558fc037a628c79336372ebf7e6035cc62d1e9303598e0f9f0
    role: context
  - path: pages/traits/genomics/hec_04_system.html
    sha256: 9c6ecb633394b68218273c25b26dc7fac9035efb48524a1cdf16fa4af587432c
    role: context
  - path: pages/traits/genomics/hec_05_system.html
    sha256: a0510b39ddb965242adad1716bf90f854e442bb6ce93c739f0464c2f5cc0e204
    role: context
  - path: pages/traits/genomics/hec_06_system.html
    sha256: 6584568974caa10c111dd63a043f21c900e1f6329179e87fec54a487585b1c86
    role: context
  - path: pages/traits/genomics/hec_07_system.html
    sha256: 8827a577567c33c16c2e72c4b5fcf97e84af86c735ddabac2ca767abe3f88875
    role: context
  - path: pages/traits/genomics/hec_08_system.html
    sha256: 4c9287f925f9d84335c3eec11af7accec31eb56f308ce975f71c01ffc8d825c9
    role: context
  - path: pages/traits/genomics/hesat_system.html
    sha256: e08d424cce00f9d2e376fc2a71f0a92e0d427830582fb7641c3111d0fdd78516
    role: context
  - path: pages/traits/genomics/heterokaryosis.html
    sha256: 8166883e06e39ffa3b5976fd14fd12e22d85dc13b19c87d62364a2ce67edee90
    role: context
  - path: pages/traits/genomics/hma_system.html
    sha256: d855d51ef3ad0300840c05ac7161db7dba24b80cca5cabce60e0a4f11d93b12b
    role: context
  - path: pages/traits/genomics/hna_system.html
    sha256: 83f9ec44360987a47cd39ebd92c076f646ee2bc30ecd4cd1a2d1afc8e2d2175e
    role: context
  - path: pages/traits/genomics/hypnos_system.html
    sha256: fd333ced2214ad908c5541e26de6ec28c7c766dbbfa2e47fabc49675f0759ad5
    role: context
  - path: pages/traits/genomics/ig_like_schlafen_system.html
    sha256: 2141e823fb5e6cdab46ae14f0ed97c32a7f6d163ae0fbdf53983d976a2ba2b43
    role: context
  - path: pages/traits/genomics/integrative_conjugative_element.html
    sha256: 981b5924b36d943869df398e205fd1170524b17433ed4b74d2be58298df898b8
    role: context
  - path: pages/traits/genomics/jukab_system.html
    sha256: f1ac68c3d1b4ae085b2191deeae10e0746c36b64ecb113a78daad006f39e7cf0
    role: context
  - path: pages/traits/genomics/kamadhenu_system.html
    sha256: ad2784145234605f49a9070f2f04a8c125a026727040ef49cc29ae098aa29864
    role: context
  - path: pages/traits/genomics/kiwa_system.html
    sha256: 4f5f20624c1af82c255b0a7dd708cabef110b2c3225b177bf33302edebf005b5
    role: context
  - path: pages/traits/genomics/kongming_system.html
    sha256: 90e37d8aa338f8d1ee43add28a8505f1f40b20ed6aba9672e2912db3861e997b
    role: context
  - path: pages/traits/genomics/lamassu_amidase_system.html
    sha256: 98c209d5a4843766a6f6495b0f6b3744aed486ea2600144df4cb24fcadc78244
    role: context
  - path: pages/traits/genomics/lamassu_cap4_nuclease_system.html
    sha256: 86e8915f8667412229e61b589fb1b01e58b25f23e6033af0d3cc7773f616dc29
    role: context
  - path: pages/traits/genomics/lamassu_fmo_system.html
    sha256: 3a47161cd5165e1935677be7f26f809c4acedeb84dbe3129bfa4a9f6bd7c7c3a
    role: context
  - path: pages/traits/genomics/lamassu_hnh_system.html
    sha256: 066c7c06ca6f5c39d1d0ee01135df23d8d0329649099338926a72e3000e46d93
    role: context
  - path: pages/traits/genomics/lamassu_hydrolase_protease_system.html
    sha256: ce6bfa3d94aef8dd194e6126036cb5deea0bc1f95b78a152b30297a98755ba06
    role: context
  - path: pages/traits/genomics/lamassu_hydrolase_system.html
    sha256: 3fb896d640f9a26d8a3894edbe229d2a28e5a54d75b75c1094ad4b77fe7b80e4
    role: context
  - path: pages/traits/genomics/lamassu_lipase_system.html
    sha256: ff216a760eaa70a657e1030dd4c8e8b56f2c612736c5de2838b24e4c54272863
    role: context
  - path: pages/traits/genomics/lamassu_mrr_system.html
    sha256: b4541d8e84c9a14b3a4b26a004e211664a0bbed1aa5ba4aabf0149730b67b2a4
    role: context
  - path: pages/traits/genomics/lamassu_pddexk_system.html
    sha256: b42dad2d86c156021c3bba66a3fa6ceb6b275bd298251a975881b82306581fe2
    role: context
  - path: pages/traits/genomics/lamassu_protease_system.html
    sha256: 8999a8d1ee75db45d14c42d9a7d279ef9f7b109677838c59d1e556556c221e67
    role: context
  - path: pages/traits/genomics/lamassu_sir2_system.html
    sha256: b50f4b940cbe070938ab707e97aac6c8458cbc085e2d87e5cdd87c4f47a8efd0
    role: context
  - path: pages/traits/genomics/lamassu_smek_system.html
    sha256: f1cc463567f3f673a4c68791f1fe0fa9c42334ba8ed63f8edfc354af74ad423e
    role: context
  - path: pages/traits/genomics/lamassu_system.html
    sha256: 66122a36071680c201fd5c4fd46c3d4b2a7104926197702d8fa130c9d34a9eb4
    role: context
  - path: pages/traits/genomics/lamassu_type_i_system.html
    sha256: 55de78050bda50088c2c89decfe7f03f1b8f383a39642d17d30f69ab8ef4e9fa
    role: context
  - path: pages/traits/genomics/lamassu_type_ii_system.html
    sha256: 34871217a2d4c46286473c372f59067d81a6d8457878bb31e3517fb155535c3d
    role: context
  - path: pages/traits/genomics/lanthivirin_system.html
    sha256: 0fa89947b28b8bdf8aa6c7b69fc06e6fe6f06b18150e7f108a2f2f0149990913
    role: context
  - path: pages/traits/genomics/lit_system.html
    sha256: 6446b12fd4142e278d2c52e4f0665f7d7d413375bf8fd11a8193327587362a2e
    role: context
  - path: pages/traits/genomics/long_lamassu_system.html
    sha256: 76f0aa9bd460687e916cd95fdc28f0cd98b2f5853f30e748485f520187d9c056
    role: context
  - path: pages/traits/genomics/lugos_system.html
    sha256: 3d862015b0326bae93a7f1459019ae00e201b47b21813b6e3789227ac6c11bca
    role: context
  - path: pages/traits/genomics/mads_system.html
    sha256: 2e1f7ecbef86f3519cb372c8e65be5f7033281473eddd56909ee41c3c464ca35
    role: context
  - path: pages/traits/genomics/mazef_system.html
    sha256: efe96af3afa2f8f708d1adbbeedd8f4adc7ace44633d7fcb421637f000405c67
    role: context
  - path: pages/traits/genomics/mcrbc_system.html
    sha256: 1d683ff5f7c57107a9044e0b4d88a57edece3aec3a44a16a8c638109571ae4f9
    role: context
  - path: pages/traits/genomics/menshen_system.html
    sha256: 52402625aaceb56b3d19c9a4be7f36fcc340b6cbca4d535188c40b3dd6034c5d
    role: context
  - path: pages/traits/genomics/metis_system.html
    sha256: 7b4d3fbf0d9970e1f6ab6834fa3b92530dd23329443517a3674f0a19c0f3772e
    role: context
  - path: pages/traits/genomics/mksbefg_system.html
    sha256: 46235767a1fee84c59fd57d7c47511faa2684bad6f4457c3d25103bcd4d36d8b
    role: context
  - path: pages/traits/genomics/mmb_gp29_gp30_system.html
    sha256: 3d95f0af4bde7431e36fa28f9c8f57c37cee45a913220404c6c34ffc6be85843
    role: context
  - path: pages/traits/genomics/mobile_genetic_element.html
    sha256: 9de893133661bfc27d63cf85264d7445058a9047a3a67666ae2a7bdffd415491
    role: context
  - path: pages/traits/genomics/mok_hok_sok_system.html
    sha256: 4f5a44a2eceb2625ac87ba0790cf12216f1bdc20d8ee4c2c9d2ffee631c0623a
    role: context
  - path: pages/traits/genomics/mokosh_system.html
    sha256: 33a6eb5b6ac43b788378ff31a882b2dd8f4697b815ccfefbc7ecc9a7fe4c8b9a
    role: context
  - path: pages/traits/genomics/mqsrac_system.html
    sha256: 9ab907bcdf8585f776e1cdfb8a51c1f33fb39ecf91f8f8fa8ae1b0a20ae89c34
    role: context
  - path: pages/traits/genomics/mspji_system.html
    sha256: 5f2d4b9208587e56f8ead9c5673d06743478eea4a034358b928366304d8931f2
    role: context
  - path: pages/traits/genomics/nantosuelta_system.html
    sha256: a1cbb391d697c2500b37c7ffa7ec288f1f79be10b09ec3eb7905c9d044bed22b
    role: context
  - path: pages/traits/genomics/nemetona_system.html
    sha256: 7708f767b4d54e0a6399396c5ed83c5ae400c9dfecfba6ae53372a6313a664a4
    role: context
  - path: pages/traits/genomics/nhi_system.html
    sha256: 8075c8d7b4d81700860bb4e73927cb7d95044210a6feb0075f63fffd6c1795d8
    role: context
  - path: pages/traits/genomics/nixi_system.html
    sha256: 309c63fdb478f9f8dc0e46c87db3c1597f982ed34ceb4aa7038ca6424dda584a
    role: context
  - path: pages/traits/genomics/nlr_like_bnacht_system.html
    sha256: 6d049b4db7ef979f79da49dff2ef1390f2b70d4b88c63ddaa81f3dce49381b2c
    role: context
  - path: pages/traits/genomics/ogmios_system.html
    sha256: c7682d66eced8ba7e9532231f9ac3abc2a9a1ca199b1b25a52ca2515266840ec
    role: context
  - path: pages/traits/genomics/old_exonuclease_system.html
    sha256: ca44ea37a6ed3b092b3a2a01efe618afafac39ecdde23bfd9aac104e10300547
    role: context
  - path: pages/traits/genomics/olokun_system.html
    sha256: 3125351dbd90329bce7f9142dc8761bbe3ca87f883f68c8c7ad428df9dc2e1c3
    role: context
  - path: pages/traits/genomics/ophion_system.html
    sha256: c9c8335a1cc8942cb25942815212710d63b96d97f06fad884cc89f6d9b9224e7
    role: context
  - path: pages/traits/genomics/oshun_system.html
    sha256: b3b7109f280b466929a4b2b624845fb5661484288bf0aac543b0da54719da652
    role: context
  - path: pages/traits/genomics/pago_system.html
    sha256: 73908c4b03658c44fbe991ed1e060a12ac2b5b6429b6f9dbedee062e061262a3
    role: context
  - path: pages/traits/genomics/panchino_gp28_system.html
    sha256: 67d6870bf51cb063f09afd6362edc96debb6bd51b81ba055fd586f4dc20e8265
    role: context
  - path: pages/traits/genomics/pangenome_openness.html
    sha256: 432da7456abbf45c2476860319b4d14508e6d9134912f7d59fd8b2e41abfcf20
    role: context
  - path: pages/traits/genomics/panoptes_system.html
    sha256: 861fc42afa9fae339f7fe3a439cc3cf1abb4bcfc777651939910fbf7f0277200
    role: context
  - path: pages/traits/genomics/paris_system.html
    sha256: 46fdecced3cdd66695ca1679e58b3902b8a56d92a3737f4384126f77241b3dfa
    role: context
  - path: pages/traits/genomics/pd_lambda_1_system.html
    sha256: 36d1803a9f970b1f3b871fe6c382d22121c8caf61cbceac205c701d63d3402a1
    role: context
  - path: pages/traits/genomics/pd_lambda_2_system.html
    sha256: 4e2c10016057c7b1c434a1afab684cd8830e19ed8d148cc6e8da71495445c75b
    role: context
  - path: pages/traits/genomics/pd_lambda_3_system.html
    sha256: a89168aa0bcd111b73e5586ad5610475c7700d2a1a358d92e6fd1b843bfaf752
    role: context
  - path: pages/traits/genomics/pd_lambda_4_system.html
    sha256: 06bddccfa6c327d68cc951c898d2eaf57b332c4fe9b70d8a43090afc03b49ca7
    role: context
  - path: pages/traits/genomics/pd_lambda_5_system.html
    sha256: d48893e9057eeb7244a23549a5d5679c6fe5e67c4d522d241f1351b62c69aea9
    role: context
  - path: pages/traits/genomics/pd_lambda_6_system.html
    sha256: 2709f8d1d4e970eeeb7679506d94de4c6a58971ebae8691a635a0a6cd9dd1dc8
    role: context
  - path: pages/traits/genomics/pd_t2_1_system.html
    sha256: ecf61f28cb179192bfc00abc026369cd9fb51a13d5387cf638c794c39e80a401
    role: context
  - path: pages/traits/genomics/pd_t4_10_system.html
    sha256: ac8a7cc76f33d6edffb4caaa8a3f638b87ad5e063bba7df9445a2dc7d302c892
    role: context
  - path: pages/traits/genomics/pd_t4_1_system.html
    sha256: 05d46fa36c38384e5ba24b9accef9b7c777e07b508e09688366a3c9c614b4cb0
    role: context
  - path: pages/traits/genomics/pd_t4_2_system.html
    sha256: ac66eeaa5a7439ba90682769e5e70dbba31190cac55aca587139743dea737945
    role: context
  - path: pages/traits/genomics/pd_t4_3_system.html
    sha256: e951b4b1333183f761dba7adbfe0a9de172fb1a85adf3cba358c9aaa742af6f8
    role: context
  - path: pages/traits/genomics/pd_t4_4_system.html
    sha256: 42a3239aef4872e86d57ba60950961f86b10decd3aa35a48a2d153c905604534
    role: context
  - path: pages/traits/genomics/pd_t4_5_system.html
    sha256: b79a0543e735346b400f2138fe78cb265f7e77d03bd21e50a63230d734de1182
    role: context
  - path: pages/traits/genomics/pd_t4_6_system.html
    sha256: 8378a48470fa15c9cc8a48e9899d83768d6b226eedd8519fe698a95af025fbe0
    role: context
  - path: pages/traits/genomics/pd_t4_7_system.html
    sha256: 038dc3ba3de4d4697fdc9645e8f448d47973922b3360fee2ec08084124553dca
    role: context
  - path: pages/traits/genomics/pd_t4_8_system.html
    sha256: c73f5f04e84501be29648b04ff653a5d81931df4d9dc02d8a6fe37ca5585e633
    role: context
  - path: pages/traits/genomics/pd_t7_1_system.html
    sha256: f9770b79f8df794b6d23759c91a1ebb16a9419b2701079e7d871f96c7217d15f
    role: context
  - path: pages/traits/genomics/pd_t7_2_system.html
    sha256: 7573bdd844fb81684ed9ca8d81cee5adfa8139b94484f00d24b14dd518edb942
    role: context
  - path: pages/traits/genomics/pd_t7_3_system.html
    sha256: 87d232cf4889e5fa454183993e43ef1deebc7e89e63f25c851673a357fbc73f4
    role: context
  - path: pages/traits/genomics/pd_t7_4_system.html
    sha256: acf10f94707b8bccd873b09f42e32b38e9a6f68df7858cef904f446717ef806c
    role: context
  - path: pages/traits/genomics/pd_t7_5_system.html
    sha256: c501845f477dfea27c0bab91dc867114060f56f454cd86f6b18d361332d6054b
    role: context
  - path: pages/traits/genomics/pfiat_system.html
    sha256: 015f2eb6cc964a2f43a0e8a4459ffef51cdabb2e17df25b5f704521b535397f4
    role: context
  - path: pages/traits/genomics/phage_defense_system.html
    sha256: 2131e46d949f530385b43920e821c6d3dd8317c9b1aeb767250d0fa98cd2a012
    role: context
  - path: pages/traits/genomics/phosphorothioate_defense_system.html
    sha256: 5da71f79b6373940223983d3ce5ecb25d70a794d9325bdc2841809b6603abc11
    role: context
  - path: pages/traits/genomics/phrann_gp29_gp30_system.html
    sha256: ea22ba7594e6975c1a877a1e37bd324d238fea21de862d3fd113b0a08537079f
    role: context
  - path: pages/traits/genomics/pif_system.html
    sha256: 48b8433fde025a939c30a6c2d8bdb3ae67a35cd03e7333f1ffa6f1f72f2f368f
    role: context
  - path: pages/traits/genomics/plasmid_carriage.html
    sha256: 0fb9023b5c4cce899a3ed6447b47d4a12bcb2feb8230a4e73dc45d9449055542
    role: context
  - path: pages/traits/genomics/ploidy.html
    sha256: 151a039ad8e7459ae1fd16db94f2401dee1db8822848de28b612ee1a0d7c7d2b
    role: context
  - path: pages/traits/genomics/prithvi_system.html
    sha256: 6662686606229d02fbda005adcbdd96e48a27aef5fcf2547482e0219ebe2363a
    role: context
  - path: pages/traits/genomics/prometheus_system.html
    sha256: 67a2e296ab0a404793f6929e33b86e8e3831fb66f7bbd01394a6e8d667800b38
    role: context
  - path: pages/traits/genomics/prophage.html
    sha256: 68b624ca02d48e828dedec32904a4773ce721718831005f495d0afd95f91c992
    role: context
  - path: pages/traits/genomics/prrc_system.html
    sha256: 1e8347d4aa6dbfc109fb76832086163f1bd95dd7b7967a2592a077052fb5e511
    role: context
  - path: pages/traits/genomics/psyrta_system.html
    sha256: 20ab2655d34b3059709e6588afca78d7a6e53eb02c96a04634c59529ea66a497
    role: context
  - path: pages/traits/genomics/pvurts1i_system.html
    sha256: 6b5ec0cb4e1565b033c715563dd530184f5ced0cdd35aca08baf46539ec2b2fb
    role: context
  - path: pages/traits/genomics/pycsar_system.html
    sha256: 9b6885228b137987f53b18d46df826ec6438aebe41a56ff9c1be5fd50f0833d4
    role: context
  - path: pages/traits/genomics/radar_system.html
    sha256: 51ef7f60697b78b642708b297093ccdc87bc11068d0d0fc2c2aed9d06bf88ff6
    role: context
  - path: pages/traits/genomics/razr_system.html
    sha256: 251e644ad5e2fa687faae430110634ca0259c0087f8d37cae1da3a3c39853e91
    role: context
  - path: pages/traits/genomics/resolvase_duf5677_system.html
    sha256: e4563edbbb4d5e9e93373699a61c5f40e08c220e9001ecaccbe429505f3962d6
    role: context
  - path: pages/traits/genomics/resolvase_kap_ntpase_system.html
    sha256: 77bc7229af428dae61191ba17f5f7da921ac4542b06f4944102016251db667df
    role: context
  - path: pages/traits/genomics/resolvase_schlafen_system.html
    sha256: de79b5bcd2031d70fd2211c6234bd30e6611c4468387ad9e688971a481f18324
    role: context
  - path: pages/traits/genomics/restriction_modification_system.html
    sha256: 29b2cf2c9708df5fbc1a16fdbb822a439e9756793e148deaacdec8880877a879
    role: context
  - path: pages/traits/genomics/retron_system.html
    sha256: 7ecc4734495efd4a1c56fb9f8ad4aaf8dd7cc05c53f937b5416694324081232a
    role: context
  - path: pages/traits/genomics/reve_system.html
    sha256: d1dcbad48cc06922c65fba0304d219da8df5b33f60cf0feb4428c916aa3738f4
    role: context
  - path: pages/traits/genomics/rexab_system.html
    sha256: ee221f8721d68c73ccbf71207ee8146db623d41ac9e0558b932807af6568b20f
    role: context
  - path: pages/traits/genomics/rhea_system.html
    sha256: a3b8bed6d670096da30ddd1375977dae4f914dbab4988a7c0c7252a3da74b91e
    role: context
  - path: pages/traits/genomics/rloc_system.html
    sha256: f99e6911834ab959d1812fa9a1ede0023f0c7670210d64e54b22f8903ec76d89
    role: context
  - path: pages/traits/genomics/rnlab_system.html
    sha256: 1c98241c0be1e23b0b29832ebd09942bddccb16121ebfa92eb7a2798d3e0cca0
    role: context
  - path: pages/traits/genomics/rosmerta_system.html
    sha256: 7a776fa6bcea57f2ab3097a2ddb9adb587914578c320a4b4b7cd1c4ed4c6d333
    role: context
  - path: pages/traits/genomics/rrna_operon_copy_number.html
    sha256: a7fce7e9924d1d07b2fc0dbe24c032c5b239d700a21ba7bb47c38af2af7c70b8
    role: context
  - path: pages/traits/genomics/rst_2tm_1tm_tir_system.html
    sha256: b3b87c5bb38fe0932ca52e526352af042e05e9252ad261afdbd69616543daf8b
    role: context
  - path: pages/traits/genomics/rst_3hp_system.html
    sha256: 68f5620bf1dd0f60bb907757254522b19e3510db0bf57c607765c463c7253713
    role: context
  - path: pages/traits/genomics/rst_duf4238_system.html
    sha256: 70b622119f2d1fac9c5c4d0283b0716f9b1cab8797c96c88ade8b29df4d00c8c
    role: context
  - path: pages/traits/genomics/rst_gop_beta_cll_system.html
    sha256: 3c78233cd58b634d5d4843c71aea11d142cc7bba70602fc22efea81b8c5c7a6d
    role: context
  - path: pages/traits/genomics/rst_helicaseduf2290_system.html
    sha256: 316d290317b55e180fc14d212025256466347279aab867cd18bc779c13df340d
    role: context
  - path: pages/traits/genomics/rst_hydrolase_3tm_system.html
    sha256: 35c463e97616455b07e9828d104f9823c0cc3a9fde86b0a471a23d3c8d64e0c0
    role: context
  - path: pages/traits/genomics/rst_rt_nitrilase_tm_system.html
    sha256: 9016d4a231ed1ccc8816726ee900ff14d3e176f1fd7c0a1ebcec1d58928813fa
    role: context
  - path: pages/traits/genomics/rst_tir_nlr_system.html
    sha256: 626751c4ecfee6a121e3c67e40480bd490a7b9494645f115bb3a9ce26d9ebf49
    role: context
  - path: pages/traits/genomics/rugutis_system.html
    sha256: ef06fd898096e06b5720dcfa67ce5c9c921743fecf9eb5731aae47570e84e52a
    role: context
  - path: pages/traits/genomics/sanata_system.html
    sha256: de9006714dec04e4eb6a6584e79711842bc9ee0d4115356ce4388ca4346394ad
    role: context
  - path: pages/traits/genomics/scomcra_system.html
    sha256: 7e7257ab9af0a001bd2dee06d56974109e9e91f4969195915dd6352fd9cb8f21
    role: context
  - path: pages/traits/genomics/sdic1_system.html
    sha256: 8aa880f44b91f51b52b425ae6466dd0b9b7e18e34ac173317ab5ea3e7361c11a
    role: context
  - path: pages/traits/genomics/sdic3_system.html
    sha256: cdba284d5d9667d1d5fe711f7c03b2e07db49f41ee2b5bbfc5a710566ba1ff58
    role: context
  - path: pages/traits/genomics/sdic4_system.html
    sha256: 3e5a9c7956bf9cf62141945efb4de9647b2599751d4d8044cb7a5ebefdac5f5c
    role: context
  - path: pages/traits/genomics/sefir_system.html
    sha256: 7152aefe2c7ac71a5a9c04f6a07f9d3f3cfa029c80dfd5a500949a6c2256720d
    role: context
  - path: pages/traits/genomics/septu_system.html
    sha256: d6852e245bfde272572aa7c60063bb6c8e31cb191809cf092e761015361503f6
    role: context
  - path: pages/traits/genomics/shango_system.html
    sha256: 503d3d2fdcad6f439a3e8c9e6ef103cf35d96aa62752e97257a3cb5f2ec76279
    role: context
  - path: pages/traits/genomics/shedu_system.html
    sha256: a2653bf21aacb344f00e04de8b68cdc52373a643125de4656378ee916a4427a5
    role: context
  - path: pages/traits/genomics/short_lamassu_system.html
    sha256: ec8f58cf50ee7e972583ba56ac40d703fc7a52105ce0af08cbc3f0e3b008b7a4
    role: context
  - path: pages/traits/genomics/shosta_system.html
    sha256: 0af8f66c316668eacc099af8097d7e60555e3e32eff267ee8c9267eb4209580f
    role: context
  - path: pages/traits/genomics/sirona_system.html
    sha256: 753a95d857eaf9380e946ac7d4ae77975aed4bb37d9a74e57e024b96eb9945ee
    role: context
  - path: pages/traits/genomics/six_a_mbl_system.html
    sha256: cf66979e68633c0c4313752158109385ae6277bdf0e8a8fcd25f122cc8aa0165
    role: context
  - path: pages/traits/genomics/snipe_system.html
    sha256: 6534df4c352e2b19ab7e0616de6e4feedb997e3baefa26c55b187ca545153d0b
    role: context
  - path: pages/traits/genomics/sofic_system.html
    sha256: a6d122034c4182f98dea922d53219a7586a878032101dd36070b51e7de5225b7
    role: context
  - path: pages/traits/genomics/sparta_system.html
    sha256: 57b661ea8558e50b3ac95b445fe28575021c5d5c2a0377422842b6d22a4bf730
    role: context
  - path: pages/traits/genomics/spbk_system.html
    sha256: 98162eebfa6e467d970df4ff02735225b68ce6faaf9851e3ab8c0f0e5e88511f
    role: context
  - path: pages/traits/genomics/sspabcd_sspe_system.html
    sha256: 10fae68df037b54e9400e17f40a3160a4374da6312ab774258e206ac32b2bc98
    role: context
  - path: pages/traits/genomics/sspabcd_sspfgh_system.html
    sha256: 67b7738c1a57e3c53ff474c69e85fba6f9a1ee8bd7822de799cdbb003fcc5922
    role: context
  - path: pages/traits/genomics/stk2_system.html
    sha256: 0dc5ae0e959cf0b0adf548185508c0bbba96b42b8ba129a31ced6e55e3e271f0
    role: context
  - path: pages/traits/genomics/sucellos_system.html
    sha256: 7d6f19f849c15e38c6f14dd68f175ea96dac93f411b05691671a61ede9045dc0
    role: context
  - path: pages/traits/genomics/tab_system.html
    sha256: 0587ec046c609caee716059052f74fbe1e216147122c53ae3fe649410c668a6d
    role: context
  - path: pages/traits/genomics/tagi_system.html
    sha256: 21c505b50d91c80a310e3a7d21b47b256b368648bc5d47cbfbceda815e928b1d
    role: context
  - path: pages/traits/genomics/taranis_system.html
    sha256: bf6dc39103f8c473399211f50d093d40bb71a4ad845597bbce31ab38901d7446
    role: context
  - path: pages/traits/genomics/tgvab_system.html
    sha256: ed9c7f2176438bca5310d63494d9e9af7157e438137306d8fd9350a9f5389ca9
    role: context
  - path: pages/traits/genomics/tha_system.html
    sha256: dd139b2df23307e322eb821df09ea1364610ea683650c69078be020d2094c6a3
    role: context
  - path: pages/traits/genomics/thoeris_system.html
    sha256: 528d61ddd9d89eee3f6a869c5f6de30aa2f86b6d17b77f1cd0a55ea2e0790762
    role: context
  - path: pages/traits/genomics/tiamat_system.html
    sha256: 22fe9bf6540ac79f249199e834c93c060a8cb78472c33b32104894c816c8f526
    role: context
  - path: pages/traits/genomics/tir_i_system.html
    sha256: 45e1786434e495f8f7f8399a30c32960ddaafbbf391411a63e4cc66af748c1d4
    role: context
  - path: pages/traits/genomics/tir_iii_system.html
    sha256: 3a68356a786c2d0d8dcd6c47cde76b83d2b6154a1abb89fe1ad59711dc083e74
    role: context
  - path: pages/traits/genomics/tir_iv_system.html
    sha256: 84576a80e2769e881bca2260d066dcc6767ffc1983739a763fa0bfbd3d06c772
    role: context
  - path: pages/traits/genomics/tir_vii_system.html
    sha256: a2b021e8e5ebfdab3a7ee8ec408d6f3d5158312d72650be4c8e500019467fa3a
    role: context
  - path: pages/traits/genomics/tir_viii_system.html
    sha256: 4e00bc91abeaaa25ceb710a42f1165b8ca04aeee0041539b34252a7c861e472b
    role: context
  - path: pages/traits/genomics/toga_system.html
    sha256: 861b9b9de9385330dec6a609b05448ef22ee0ca0e288afcb8aabfcd9f2f48087
    role: context
  - path: pages/traits/genomics/toutatis_system.html
    sha256: 80266c309a30b7caa75be68482f8bae1791a130c719fbd11f693d34836ae8bf0
    role: context
  - path: pages/traits/genomics/toxin_system.html
    sha256: 5cf03a453adb9d13b32c7ae46e862e34cc521cbdfa653bcd3d2ae4ee01391386
    role: context
  - path: pages/traits/genomics/transposable_element.html
    sha256: 76a862c31f20a9e892b70cf0d8ba409ecf26cdf5707d0eddc05c267ab6b3105d
    role: context
  - path: pages/traits/genomics/type_i_restriction_modification_system.html
    sha256: 64996f41d67dcc360456374b6af16456749b487ee0605978ffc73c77de901557
    role: context
  - path: pages/traits/genomics/type_ii_restriction_modification_system.html
    sha256: 3d9f0fdf48b08c21db22d49e6c1149e5e1c0c5cb6578bfb9cb476e6d513f7f2b
    role: context
  - path: pages/traits/genomics/type_iig_restriction_modification_system.html
    sha256: d8ebc00843181037ab5335a2e25126b6310a0cd872d754179617d45b4fc65a3a
    role: context
  - path: pages/traits/genomics/type_iii_restriction_modification_system.html
    sha256: 3a9f00a108889517b4feccb3835c2e5c00d859778f1d88369b3617c757b3a823
    role: context
  - path: pages/traits/genomics/type_iv_modification_dependent_restriction_system.html
    sha256: ceebfba29242c881c406dc416525f1c292916e4d93b9961ed9844031b8f1bbc2
    role: context
  - path: pages/traits/genomics/ukko_system.html
    sha256: 2108a993080357275d0ed6a47d4fd05aba36b49fe60975a97a5085ef6186afe1
    role: context
  - path: pages/traits/genomics/uzume_system.html
    sha256: bd4c9b78f0072f7bff2c1ef2248c5b53388e91b9598292c65af8bdcfbe66413a
    role: context
  - path: pages/traits/genomics/vcam4i_system.html
    sha256: 62886f83656e3610633e0fd32fc650c91e5a8a478b82df9812a31c8333f0e834
    role: context
  - path: pages/traits/genomics/veles_system.html
    sha256: c20ccbc483bd88f5a0d23094f207db484fb74d12b19c2d0dbfcb1b95b224386c
    role: context
  - path: pages/traits/genomics/viperin_system.html
    sha256: 6c5cc8360dd33a71d05d44503dae55518115c24babf6de562537701ff5b4d1a8
    role: context
  - path: pages/traits/genomics/vp1796_system.html
    sha256: a61e2d7029974232a08106e2c71407fc5d36b4cc30faac1e999fc6b435e4f782
    role: context
  - path: pages/traits/genomics/vp1817_system.html
    sha256: 4d1bcb5f76e90bc17e3e3203c8f8265a728cc1444629d594abef90cd861a735c
    role: context
  - path: pages/traits/genomics/vp1823_system.html
    sha256: 1b21220ca17de3fcf3277a6ae17909e8e17cb95ac865a2859ddaba7395e60374
    role: context
  - path: pages/traits/genomics/vp1826_system.html
    sha256: f619de538fd3506cbdb4922a4785af453955dc11253b19e9935526ae92ac4745
    role: context
  - path: pages/traits/genomics/vp1839_system.html
    sha256: aa718326974e833521546a4bbf5595556bbbb6698ca736877fdfd14f489bfca7
    role: context
  - path: pages/traits/genomics/vp1840_system.html
    sha256: 023848bb9408165270c943ed06b1ecab360f6b70ae5e3631be9ba9ea727b9553
    role: context
  - path: pages/traits/genomics/vp1848_system.html
    sha256: c606d59ea9bbc83953c91773a184c79f5da3e7caa2897656be80c5c652dc30d0
    role: context
  - path: pages/traits/genomics/vp1851_system.html
    sha256: bfb97cd6d872b2d0cce63243070e300c37fa9bf5cf056166981a9703fd3d556a
    role: context
  - path: pages/traits/genomics/vp1853_system.html
    sha256: b419a06ec35d5a3cb5cb9ed1fdb24157d0b42f0d0ab19efd5fde77d87d385b24
    role: context
  - path: pages/traits/genomics/wadjet_system.html
    sha256: 1fb06d5eb0fbe083461bff85e1986fa83000759bbb90c4c3b43fe32f5a7a75e4
    role: context
  - path: pages/traits/genomics/zorya_system.html
    sha256: 5fd29301253907d68e7606a0b55d68ef8ef0cca5cde0d88ac97fe5753c7f85ab
    role: context
  - path: pages/traits/genomics/zorya_type_i_system.html
    sha256: 5d2c9688047e9fda4baa28fa4dd4085d741e7f7c3f4baf21c5f11b421035d6ec
    role: context
  - path: pages/traits/genomics/zorya_type_ii_system.html
    sha256: c75cbb61c2645652014bcbdc58b94c36ce2b1eb69a3a109f91597799b7b65509
    role: context
  - path: pages/traits/genomics/zorya_type_iii_system.html
    sha256: 93bf467bc0bd7fcf859b82179801129c27d6b1306a3888ee6d8ca65245e6c689
    role: context
  - path: pages/traits/metabolism/accumulates.html
    sha256: 2c4834a5a1698f3912c235bc59cd654dc8ff1433fb3d3f269c02fea29b66e3e0
    role: context
  - path: pages/traits/metabolism/acetoclastic_methanogenesis.html
    sha256: e33429cc58b425ae9505069f1299ef363d76d51668d91fbdccd8d2ae247b7c29
    role: context
  - path: pages/traits/metabolism/acetogenesis.html
    sha256: 00fbf0e18bdadf8e7ff108ea469b99722f1021a02dc1e4117cd11a8f89e56c46
    role: context
  - path: pages/traits/metabolism/acetone_butanol_ethanol_fermentation.html
    sha256: 8c4a8232d7a2f1859156161c1c87e8259b7d77c7b9a4f3546ca55c876cd8673d
    role: context
  - path: pages/traits/metabolism/aerobic_respiration.html
    sha256: 497d843a4f675c03bf73f63c230c372f39cd11990940dac34cd92a4e67b23fc2
    role: context
  - path: pages/traits/metabolism/anaerobic_ammonium_oxidation.html
    sha256: 953299d5ad420d9a7880d1a774d1246a916d86d591f5310ad399881d5f4f83c1
    role: context
  - path: pages/traits/metabolism/anaerobic_oxidation_of_methane.html
    sha256: db9d9a8aeaa2a1a7c1859d7dc68b4c8b2fb74cee9f3e28bca7be8e50ca1b23d5
    role: context
  - path: pages/traits/metabolism/anaerobic_respiration.html
    sha256: 3d1e7de1bf014b558d0bca100ae5d673cd06473f32d9a2b6590f5aa7392f764c
    role: context
  - path: pages/traits/metabolism/anoxygenic_photosynthesis.html
    sha256: f2c3dfa3ec05c315352888174ae8763c2bd1c9e8b0ebade0f5e6789b835ba569
    role: context
  - path: pages/traits/metabolism/aromatic_compound_degradation.html
    sha256: 927492054f7b88f4d0c60cd189d59749b48618af70653e86bd91163d766ce19f
    role: context
  - path: pages/traits/metabolism/aromatic_hydrocarbon_degradation.html
    sha256: 24128f9cfcf4bd0c3ce7d7331e9e0d380f72cdf0c59b4d43ce7f00811ac3ce83
    role: context
  - path: pages/traits/metabolism/arsenate_respiration.html
    sha256: ce8c479ebae9af5c90e378643cd59777305b373153f1ac844c456de88daf3838
    role: context
  - path: pages/traits/metabolism/arsenite_oxidation.html
    sha256: 45c8b5aa86f7aa3ed98611b24d23ea40ace3b66634c059ea8ec03eaf4fba895c
    role: context
  - path: pages/traits/metabolism/assimilates.html
    sha256: a6ba578e88c5c82d6912196b3d9f33c1aa1c0daf83a0ce1533240424d43834c3
    role: context
  - path: pages/traits/metabolism/biopolymer_degradation.html
    sha256: 161880364ccf661648abb2e26fc85f4b3b7d5ec48f013d052b8175a66e34a790
    role: context
  - path: pages/traits/metabolism/builds_acid_from.html
    sha256: 3b60685a8ecbd2fdb6667d0cd549755d0db468a44848854b70c71d095fc09f63
    role: context
  - path: pages/traits/metabolism/builds_base_from.html
    sha256: cab952f0c36a65941cfc69f4b501d00b9591b71617c2c9ae255ff514f45a5be7
    role: context
  - path: pages/traits/metabolism/builds_gas_from.html
    sha256: d0344fd53a397f0e66dc69564a1aadef2dd7d27f18e0871ace3548f6037c5df9
    role: context
  - path: pages/traits/metabolism/butanediol_fermentation.html
    sha256: a389aa658b89e80fe797769a3ec28b22887271c0b81167b37ca32657754b569b
    role: context
  - path: pages/traits/metabolism/butyric_acid_fermentation.html
    sha256: 8fcde0aa6896f74cc52935ecc820cbc1e1046c4d79777ab45babb8d29f986f81
    role: context
  - path: pages/traits/metabolism/cable_bacteria_metabolism.html
    sha256: 05fa3c8d9623355dc7f8fcf2dfaec82f3f192521531b3161f714043782968f5c
    role: context
  - path: pages/traits/metabolism/calvin_benson_bassham_cycle.html
    sha256: b19373d5a3960efa42e665ea746e9a3b73c50b3534940b5b1a178489ea74a543
    role: context
  - path: pages/traits/metabolism/capable_of.html
    sha256: 5469c1fbac5c3d20cdba9ee0b141e9327b464d64030c2d494869f9ef38f99bf6
    role: context
  - path: pages/traits/metabolism/carbon_fixation.html
    sha256: bd67b09f12d71fbcb500e3aa574e29e86e734dbc774b8dd5e0bd298f833c78a0
    role: context
  - path: pages/traits/metabolism/cellulolysis.html
    sha256: 14e711be31f54ac193d53af1e9ec8ba16ad7ec6673cc32c5b84ad89454e785ad
    role: context
  - path: pages/traits/metabolism/chitinolysis.html
    sha256: 0f83350f9497cfc1fba88b10b60cabbd626f86c4f6da494d8ec79faf4207fbc2
    role: context
  - path: pages/traits/metabolism/chlorate_respiration.html
    sha256: 1877e3774462f4cff13d9d9efe34c1306e2e520d36eb1eaca2741f999ae3bf2e
    role: context
  - path: pages/traits/metabolism/citrate_fermentation.html
    sha256: 752f0e0c1ecdfb8df7baaf39ba5daf0b00b5b40ba66ed7f125b7edadf2511e99
    role: context
  - path: pages/traits/metabolism/compartmentalizes.html
    sha256: c8bc4d96b0efca118f9803214e969fca7c4181c456ad6d81eeecaf86f14f613a
    role: context
  - path: pages/traits/metabolism/complete_ammonia_oxidation.html
    sha256: c5a538e13e02468ac7a902facc8f6fc72f1d49bb6efd9f74ae3fa4c2ad5deeda
    role: context
  - path: pages/traits/metabolism/dark_hydrogen_oxidation.html
    sha256: a8ef54739ea43f6c71dca62959dff1548bb4484f546df30b1077f2906c7fee6f
    role: context
  - path: pages/traits/metabolism/dark_oxidation_of_sulfur_compounds.html
    sha256: e4821a2406412d9bdfac9dc456fd1dd662b7ab87058e09fb15ef6342aee5bf09
    role: context
  - path: pages/traits/metabolism/degrades.html
    sha256: 56f2b4173e54a47c025e666264106b8d32ca58486a72988c11719ef9568ea024
    role: context
  - path: pages/traits/metabolism/denitrification.html
    sha256: dab22e76efd8dfa7c9b99e355aca8f1cd278cb4e9f154a48d97e1306db46f341
    role: context
  - path: pages/traits/metabolism/dicarboxylate_four_hydroxybutyrate_cycle.html
    sha256: eeb36596d5f944dc5163b89c5411655da9d5a26afe57b2fcdfc2cbb3dea991f6
    role: context
  - path: pages/traits/metabolism/dimethyl_sulfoxide_respiration.html
    sha256: f8ef9440321f07d618c35655d2fd5ff08ea6dee04f4ce70528c649a78e69bb45
    role: context
  - path: pages/traits/metabolism/disproportionates.html
    sha256: 978d35c4ed22ff52d681b1d5275e5807df3827899616e05edb6c8349f0f74fe2
    role: context
  - path: pages/traits/metabolism/disproportionation.html
    sha256: b30bf025d80effe167a56a9afcf69e67cf8e52b27dacf0990600769aef104212
    role: context
  - path: pages/traits/metabolism/dissimilatory_iron_reduction.html
    sha256: 3b6fe99a0306e45cd9571dc7ff4abf2e2b4eae1af5f15b4be0c459f1cba4f4ae
    role: context
  - path: pages/traits/metabolism/dissimilatory_manganese_reduction.html
    sha256: d4e175948cc949498aa12612bc59224dffb7e22e9125efc42a2fb456764d57ad
    role: context
  - path: pages/traits/metabolism/dissimilatory_metal_reduction.html
    sha256: 7e35b83c253929a0990c96aee0a2d3674d8cd8bd98054e429321929422cab1d2
    role: context
  - path: pages/traits/metabolism/dissimilatory_nitrate_reduction_to_ammonium.html
    sha256: 6300fc7d154de44ff35929d0f3443b7727c19171309840e261e2127f46a74530
    role: context
  - path: pages/traits/metabolism/dissimilatory_sulfate_reduction.html
    sha256: 1e48f02fe7ecbe558a84d4f1377ad2015d35f4803126ecdbd25a37e483c2e6bf
    role: context
  - path: pages/traits/metabolism/does_not_accumulate.html
    sha256: 3923c37ae7806b08ff09e8a6301ec91606611f5f7a6a4a22e35b0e0c02a27e17
    role: context
  - path: pages/traits/metabolism/does_not_assimilate.html
    sha256: ddc66038a9dfc416b55dafe955ac4ff7621e4160cf220577049ea7a3bce024d4
    role: context
  - path: pages/traits/metabolism/does_not_build_acid_from.html
    sha256: 57527e671459c462f2101c652d0dc760ceb3eca02bb4c0d7f2560cc2e782c87e
    role: context
  - path: pages/traits/metabolism/does_not_build_base_from.html
    sha256: 6ddaca42b09326ae39020d832f3ae5cf9679a5f6b2f21c685a21b91e37d6ac23
    role: context
  - path: pages/traits/metabolism/does_not_build_gas_from.html
    sha256: b0feaae6726ff580f7a53790c8ad2ab734d0b91cf3210b029cd03b7389c5686f
    role: context
  - path: pages/traits/metabolism/does_not_compartmentalize.html
    sha256: 30de58513e9f3890ef871d9c57add63c2f70734de874bd90e8553a37b7c9a3c5
    role: context
  - path: pages/traits/metabolism/does_not_degrade.html
    sha256: 42da63e485892929a1b6f5a8e35e4d1c304d7607031a2b581ada67b12a35d82e
    role: context
  - path: pages/traits/metabolism/does_not_disproportionate.html
    sha256: 250e5916a494676f2087582f8f436079ed5fbe72f93d201f57b540ba14ae8ee5
    role: context
  - path: pages/traits/metabolism/does_not_export.html
    sha256: da53ca1e1ae9b8b4812cd31344872904e65c46479610045b374add1717681419
    role: context
  - path: pages/traits/metabolism/does_not_ferment.html
    sha256: 5827cbd6c3c5e7e43ae8839fe89f97e80d4b29a2c1abb3b35e34ed301ac8111f
    role: context
  - path: pages/traits/metabolism/does_not_hydrolyze.html
    sha256: 8856a1034a41b02557ed38e66d534f4bb214de10979eb1f0d6c7a521ea57cbcd
    role: context
  - path: pages/traits/metabolism/does_not_import.html
    sha256: 8c0bde6847823ef1916b409abbf40ffad84daa105345c10996bcad7ee8f1cca5
    role: context
  - path: pages/traits/metabolism/does_not_oxidize.html
    sha256: 6ddb7cae769841db87ecfec9443df9f200e10227c48f93ea39f81c6cd09fc6a2
    role: context
  - path: pages/traits/metabolism/does_not_produce.html
    sha256: fa2d701086fa3fe0f6eac93a435d4830d718e5268a705171086268a401d017a3
    role: context
  - path: pages/traits/metabolism/does_not_reduce.html
    sha256: 27e89c0826a63212fb8840ac8d45519aeb7a32c382f02432cea7ab81a4bc5e42
    role: context
  - path: pages/traits/metabolism/does_not_sequester.html
    sha256: c777e1a6b9ab8b71b2c571623b88b2dfc93e576b12e9dee3594b384345abf874
    role: context
  - path: pages/traits/metabolism/does_not_show_activity_of.html
    sha256: e781235225329227d2111d8c90a33edbda0a823ff31b12b6d35ec41d33df9b7e
    role: context
  - path: pages/traits/metabolism/does_not_transport.html
    sha256: 922cd645b4c932bf35c974104346892db69dedc4554a543336b12b36e00a59cd
    role: context
  - path: pages/traits/metabolism/does_not_use_as_carbon_source.html
    sha256: ae78f1f9b9dc6d8ddd2cde6a275513412b056300ebc746db5e744b5f3809ba1c
    role: context
  - path: pages/traits/metabolism/does_not_use_as_electron_acceptor.html
    sha256: 2f60de9217f388c8fc8609974017fa1772cc47ad12006cb0ba5a6dbf05e0b1b1
    role: context
  - path: pages/traits/metabolism/does_not_use_as_electron_donor.html
    sha256: b11924411efff887259d69b0d65411c99cc7512513e2d4396f59fb20dc0a00ad
    role: context
  - path: pages/traits/metabolism/does_not_use_as_energy_source.html
    sha256: 2677199df9586070306003950895bc018f537f68548c28f2dbea04125a56d51d
    role: context
  - path: pages/traits/metabolism/does_not_use_as_nitrogen_source.html
    sha256: 8fa8cb3f77f541258560dbdf243338be5e29d71b46ff76a61f7bbccb50a114b5
    role: context
  - path: pages/traits/metabolism/does_not_use_as_sulfur_source.html
    sha256: c625c69a04115296e27e459c581b69f9990978557b9695c440d4099e9e8f3955
    role: context
  - path: pages/traits/metabolism/does_not_use_for_aerobic_catabolization.html
    sha256: 7845eb6c027c258de03c79b3bee1961cdbf5583e54df90472a5b445fee9682f1
    role: context
  - path: pages/traits/metabolism/does_not_use_for_aerobic_growth.html
    sha256: cb1acc3c17432666450088bcf1bec57e280ed9180c2e91f3e28cf28291bd57ec
    role: context
  - path: pages/traits/metabolism/does_not_use_for_anaerobic_catabolization.html
    sha256: add0377b8b5f353aa92760210198a16c7e871095eb6c929e0694f295d2d51999
    role: context
  - path: pages/traits/metabolism/does_not_use_for_anaerobic_growth.html
    sha256: 6f3d875ea883667b1dd9d3af68dfac5fe0cf68b392fa5b7f2fbb2dcaa1f16b2f
    role: context
  - path: pages/traits/metabolism/does_not_use_for_anaerobic_growth_in_the_dark.html
    sha256: fd90ab01f4beb7bd129508cd389e6347b1481b266a17914822eaabd0c24402fd
    role: context
  - path: pages/traits/metabolism/does_not_use_for_anaerobic_growth_with_light.html
    sha256: 25027cec17896a1cc8f004f5a0b877e1df04bc1120f9e12d4888866bb8051471
    role: context
  - path: pages/traits/metabolism/does_not_use_for_growth.html
    sha256: b01bba53e19e003cfe35e8686bc6a08d9c8098ceea04308d9bdb4a0d75579bd7
    role: context
  - path: pages/traits/metabolism/does_not_use_for_respiration.html
    sha256: ff2c7e37796802cd076877b0ca40ba82b16262be26b691ebe3094ce3de5ae996
    role: context
  - path: pages/traits/metabolism/does_not_use_in_other_way.html
    sha256: 13ac1e26e6e2ccd7d46924f05aaf92099f53b1a6e2ef8bfbca8b5261530b0add
    role: context
  - path: pages/traits/metabolism/electron_transfer.html
    sha256: b0a3d336bc6d19001256bcdec3d414d956a001ebb04143fc036667aeaf6c1d02
    role: context
  - path: pages/traits/metabolism/enzyme_activity_analyzed.html
    sha256: 6aeed0a8329303a7d4749959e500f9718c5cbc7f7be4e4b7220e60955a772eb2
    role: context
  - path: pages/traits/metabolism/ethanol_fermentation.html
    sha256: 11d4827e46da4853e9cd112e6c78ef60ff96006893876f026ea235e0d12414ab
    role: context
  - path: pages/traits/metabolism/exports.html
    sha256: 4a15971358e1ba5006bd9f68e7418491f1360e7b137a13554d56c2558ed63543
    role: context
  - path: pages/traits/metabolism/fermentation.html
    sha256: f9e0cd5f6725bda9df7e534a3fe00fb209b42758dfc473ec8cf66f64fe7e1c10
    role: context
  - path: pages/traits/metabolism/fermentative_hydrogen_production.html
    sha256: 8e0123a4d70dcd2cf52943bb24bbff53f662a16eb0f3e587c4005f545c0c2cd0
    role: context
  - path: pages/traits/metabolism/ferments.html
    sha256: c71f5177adef8748858009da7144d4739de8cec9c3f363e202c486ebaa241e7a
    role: context
  - path: pages/traits/metabolism/fumarate_respiration.html
    sha256: 8be3d2a370945193b5979bbe10dcbb5c5731fb407c792d3b7f5022f864c596ef
    role: context
  - path: pages/traits/metabolism/has_growth_nacl_observation.html
    sha256: 615b36b35fa27d24e7c36df4a37aad0874e62990187399a7ef0a6953ce9fe56f
    role: context
  - path: pages/traits/metabolism/has_growth_oxygen_observation.html
    sha256: daaac8500b3d9b2cc8794efe758045c44a3fbd4c0ca76e7882218c2094084d75
    role: context
  - path: pages/traits/metabolism/has_growth_ph_observation.html
    sha256: 079488ba24b3086dd7ea5ba6e6f08a0ba8cbe068238957ed60a7609545c49b04
    role: context
  - path: pages/traits/metabolism/has_growth_temperature_observation.html
    sha256: 6aca087de5f011e2ee1e653981ca4c1b56276c2edea49ee37bc6d5067d48556e
    role: context
  - path: pages/traits/metabolism/has_nacl_delta_observation.html
    sha256: 4724fefd8dd88fa5e9e65d6414b592ded0f7805e79f25ad003b5968236046d50
    role: context
  - path: pages/traits/metabolism/has_nacl_observation.html
    sha256: 17cf5c0b2e8519168a91db33d89cba758926f3cf540f34523e56f74cd0dec833
    role: context
  - path: pages/traits/metabolism/has_observation.html
    sha256: 3bf5272ee93eb581046502e1b2d1d4293aa342a3dd7740e52f8c8a5bd5799764
    role: context
  - path: pages/traits/metabolism/has_optimum_nacl_observation.html
    sha256: 6a8f2d1e265140cd580d9e9ff80168909fa1e0eea784aeee64244a7318ab4d27
    role: context
  - path: pages/traits/metabolism/has_optimum_oxygen_observation.html
    sha256: c9f722abb9c1baf85b807e003d19e2911daa3a17e5342d71a8700336b3759bb5
    role: context
  - path: pages/traits/metabolism/has_optimum_ph_observation.html
    sha256: eaae3764edd83b0c98c9fa2ccc95e36ae591bcd2e2f2cc25389f0955341734fa
    role: context
  - path: pages/traits/metabolism/has_optimum_temperature_observation.html
    sha256: 746bd1722839065eae5af3db76f6519490f71a1e9312ce11fd30afab4d6e6936
    role: context
  - path: pages/traits/metabolism/has_oxygen_delta_observation.html
    sha256: 8ffbee1ba7d8acbd0646b53f045a59ff924aabafa22c79f84b8b0746452cdc15
    role: context
  - path: pages/traits/metabolism/has_oxygen_observation.html
    sha256: f46cd46b9cf3240d586aaeb7d77bc0674b42dffe4172edba87dd36482c25c96c
    role: context
  - path: pages/traits/metabolism/has_ph_delta_observation.html
    sha256: b573fa811788f34ead2c3b1e3462ec6fddd51e948484103fe5ca78f0e8e6c819
    role: context
  - path: pages/traits/metabolism/has_ph_observation.html
    sha256: beae4aee7b192688ae54cb536131ccbebf48f6abc6939a16c67dd7639ccc19e9
    role: context
  - path: pages/traits/metabolism/has_phenotype.html
    sha256: 74744725e81cbf093c340ff417023617561162a0b474b69b74f33d8bfd738d50
    role: context
  - path: pages/traits/metabolism/has_quality.html
    sha256: 3e096fa9fa8d4bf843134e882aa06c1b49bb5ac3c1915532d557a0a202d7942f
    role: context
  - path: pages/traits/metabolism/has_range_nacl_observation.html
    sha256: 02e876824475c1889421f3b5df0f0f95954111bdd5be0584cf4d1b135e6bea5f
    role: context
  - path: pages/traits/metabolism/has_range_oxygen_observation.html
    sha256: c3ae3b8444c0ac253d30e3f014150be49965712a48228ab10d73432321894900
    role: context
  - path: pages/traits/metabolism/has_range_ph_observation.html
    sha256: aa1e5d618dc5cf1ed50390bb384dced2aff92595dc2fdc5e2e23cddfe183a5b6
    role: context
  - path: pages/traits/metabolism/has_range_temperature_observation.html
    sha256: 3cd3709d63c4ec347d1d7087dfbb26da8ed52c923d434eecf9e73003c34026bc
    role: context
  - path: pages/traits/metabolism/has_temperature_delta_observation.html
    sha256: b9ba97a3cad9de351148d970b8fb3892584f4aaf7fd2ec1713f3f5514c2845e6
    role: context
  - path: pages/traits/metabolism/has_temperature_observation.html
    sha256: d73e664e9e3f98c6bcc921fcd742d9be8503d54a94912492f8fd96a67016e304
    role: context
  - path: pages/traits/metabolism/homoacetogenesis.html
    sha256: 959162cb0c5537b81edd59869cf1045f8a164f553736d3900e303d23ffd27f6f
    role: context
  - path: pages/traits/metabolism/hydrocarbon_degradation.html
    sha256: eb31bae267abd812290a491ea4fe1b3d43968f0ad8c8294fbd2806a68126a2d9
    role: context
  - path: pages/traits/metabolism/hydrogenotrophic_methanogenesis.html
    sha256: 9bd8163ed8b82c18e1e9576903eaefa6ce5dc4292801f41e3cff48bd91bd70d6
    role: context
  - path: pages/traits/metabolism/hydrolyzes.html
    sha256: 7790d63b4f7e1c7dc46404ba51384a9796ef916fb2f25292bd710ae7393aa181
    role: context
  - path: pages/traits/metabolism/imports.html
    sha256: fd3883ffc41d0797e8a15f3ba7497c6c242df608976c9d8117787cfd061514ba
    role: context
  - path: pages/traits/metabolism/iodate_respiration.html
    sha256: 8645908a0f4b2cd894fac34524f661ce53b20e4e46f40e970a058ac8820dc01f
    role: context
  - path: pages/traits/metabolism/iron_oxidation.html
    sha256: 9a098bd95d63b0b2a80b4ce25c5202e1f530445381250d47f27673674329a873
    role: context
  - path: pages/traits/metabolism/is_not_required_for_growth.html
    sha256: 2f9226b1301290ec36e36f2a1142afca3a86ff0487853598f1b6e6f3adecb564
    role: context
  - path: pages/traits/metabolism/lactic_acid_fermentation.html
    sha256: cf9393fccf7097bc0544594eccabbb60ff77f8d1e25d5c484d9cac1562f119c2
    role: context
  - path: pages/traits/metabolism/lignin_degradation.html
    sha256: 76f78917531bb3d171f394185c73fedf5a0fd231fedd649ebe2c2e5c3f217e2e
    role: context
  - path: pages/traits/metabolism/lipolysis.html
    sha256: 74dcab74a13c639bed41f1dabbbd1d82ee3168466c6408c5954ca72ebb5cc971
    role: context
  - path: pages/traits/metabolism/manganese_oxidation.html
    sha256: d62922aefbfc51358429266f37da57b9c803d7eee43e93fc8a6442eadd825683
    role: context
  - path: pages/traits/metabolism/metabolism.html
    sha256: 87a7e1e6d22013e12d21be40e50a929f6a0ec48491fecc90e7e9ec1873b7ed56
    role: context
  - path: pages/traits/metabolism/methanogenesis.html
    sha256: 64ef44d69f3377e83ef99be8dc1e92ea14084ba94a9d794835922c091624fe10
    role: context
  - path: pages/traits/metabolism/methanol_oxidation.html
    sha256: 492899d0b9e1c527507495da80a77fb0437ddd9ba48f5581fa960b66e021fea1
    role: context
  - path: pages/traits/metabolism/methyl_based_methanogenesis.html
    sha256: 89d595a4eef122bef3da36702e537cbcb76b548feb58077c73d162f19e07ce53
    role: context
  - path: pages/traits/metabolism/mixed_acid_fermentation.html
    sha256: 96463617a04e36ffad1035a4cd1f1d06eaae1a06a42e5ad4a5f15908732f566e
    role: context
  - path: pages/traits/metabolism/nitrate_reduction.html
    sha256: 964c48af2ad0bc5585d5f29914d6a224a3de64d61ae448cbc2bf2000937ea94f
    role: context
  - path: pages/traits/metabolism/nitrate_respiration.html
    sha256: 85e7ba02b7c65c9913967a390cf27bf6282e50c21aba9b108dbba2a3629ae8f5
    role: context
  - path: pages/traits/metabolism/nitrification.html
    sha256: fb0d04dc288eb48218e8580d01b600b2032a53932961350453eab2948085f9fb
    role: context
  - path: pages/traits/metabolism/nitrite_respiration.html
    sha256: 12bd598ab2fe9e061b209c5dc6e18a8e280a2e76cecbb45dc16bfd4e210e75c3
    role: context
  - path: pages/traits/metabolism/nitrogen_fixation.html
    sha256: 728cccfc011516a556da673a1885941099d6a6cb5b5673d5c0659d1a56750cfc
    role: context
  - path: pages/traits/metabolism/nitrogen_respiration.html
    sha256: bb9efc2c03447417abb3dc996e71de0f326e4857f0b362500309c0c806c8f49b
    role: context
  - path: pages/traits/metabolism/organism_interacts_with_chemical.html
    sha256: 223bf545512179ab3ca43b82c64f0353974def47e141a4228e1d5f52c9afafe2
    role: context
  - path: pages/traits/metabolism/organohalide_respiration.html
    sha256: 75af54c9f455d2f9e4e1a48544a98ab87c886ce7e2e950def03af6efea525c53
    role: context
  - path: pages/traits/metabolism/oxidative_phosphorylation.html
    sha256: 6091f5b1a9ba5f80013b808697f16143aff489f7e39f9c6dff748fea2837c924
    role: context
  - path: pages/traits/metabolism/oxidizes.html
    sha256: fc6407095d20947bd67c42b7bc28bbeaad311a2389154b934ade234a8b07e1e7
    role: context
  - path: pages/traits/metabolism/oxygenic_photosynthesis.html
    sha256: 53418ce60c4a99f47657828a56a85c2d1ce813387c9811c877e736f5e579cc2b
    role: context
  - path: pages/traits/metabolism/pectin_degradation.html
    sha256: e8eb8895825c1f8d0af9b5c4a349054db8e97657d8d90bf0147b1ac343346dee
    role: context
  - path: pages/traits/metabolism/perchlorate_respiration.html
    sha256: 38f7666c53e4796babc87f1b6c3834812ecf7fb4b4bdfea6ac764cf23a4033f7
    role: context
  - path: pages/traits/metabolism/photoferrotrophy.html
    sha256: e276590492414af95743a1796e46b956e9b29a8717d30d6fcdb9613a37468de6
    role: context
  - path: pages/traits/metabolism/photosynthesis.html
    sha256: b74fa5339d2a32889bb5abe2d13faa6b091790425db0ba4e6d8f105bbb068308
    role: context
  - path: pages/traits/metabolism/phototrophy.html
    sha256: 3eec02f2b57a73d5b25761a1558400861a56837d228f19e8a4ba47f05cccb0fc
    role: context
  - path: pages/traits/metabolism/produces.html
    sha256: 1563be00d239f3699f3afbeb84c06e255cedc0b68764138f04f84849c984e9d0
    role: context
  - path: pages/traits/metabolism/propionic_acid_fermentation.html
    sha256: 432f34c19133173e132bcc68149f83c4d76b0992b1ed4c8ca38f4ffd1483bf1d
    role: context
  - path: pages/traits/metabolism/proteolysis.html
    sha256: 17fe0be5a570c73bd63b998148e2c8dad6ba8f84ca328430b431be5f0fb490bb
    role: context
  - path: pages/traits/metabolism/proteorhodopsin_phototrophy.html
    sha256: 334a60393d6784fffeb44aff28633ee64266524cf492667dbead260aa3b97bb9
    role: context
  - path: pages/traits/metabolism/reduces.html
    sha256: 80e2711359354504c2a843f1ea7c2feda3626018ecb7d9ad442a1fbd1978bed1
    role: context
  - path: pages/traits/metabolism/reductive_tca_cycle.html
    sha256: a24743da8ae42d861525462af986cfffc853abc96eff71f176bcdb75068a5912
    role: context
  - path: pages/traits/metabolism/requires_for_growth.html
    sha256: d8e37dbc27da9a01404625d23c92f7fc7de602c9e7934f85577d12382aae3b97
    role: context
  - path: pages/traits/metabolism/respiration.html
    sha256: ffb595b1569156c7e4dc6adbecdd6f2a02c1b85ec6c165964303abfef3599433
    role: context
  - path: pages/traits/metabolism/respiration_of_sulfur_compounds.html
    sha256: da1672151331583c1b0680302965b22ad9bcc6c73a1a9117c1774470648eb570
    role: context
  - path: pages/traits/metabolism/selenate_respiration.html
    sha256: f07785647909c9e574b2f9effbe7699c0b51988ff38ac6ff6e25c561adcec067
    role: context
  - path: pages/traits/metabolism/sequesters.html
    sha256: 7d03cf871c674977182fedf3052480b4506952006822b28c809a71141c6d3cfb
    role: context
  - path: pages/traits/metabolism/shows_activity_of.html
    sha256: dbf3fc85c1b89c9a4e59db013a8825e72eb9c036585455abf56cb7f87f35fd51
    role: context
  - path: pages/traits/metabolism/starch_degradation.html
    sha256: eb7cda0551f79194d6c75e29b5959880802d24a392a793bc8c81067cf4932773
    role: context
  - path: pages/traits/metabolism/substrate_level_phosphorylation.html
    sha256: dee9220fd0fc7901b02f6b136815029ea3515a2831ca170d8266b077babb039d
    role: context
  - path: pages/traits/metabolism/sulfur_oxidation.html
    sha256: 23c91ba5bde32da74801849ebe909dd25e3cb2de61f8d31d60ebfd5f7ab8adcc
    role: context
  - path: pages/traits/metabolism/sulfur_respiration.html
    sha256: 5c7207b56a8b7e389c5371fc4d06f5e016503540c7cb2ca3f6916cf95c4a1db6
    role: context
  - path: pages/traits/metabolism/syntrophy.html
    sha256: 77b9f4419a82949f24c7448dfd074540aba867f2ce366136f80f425466216de7
    role: context
  - path: pages/traits/metabolism/tetrathionate_respiration.html
    sha256: 02c5e27b16a7fb925a7d62886b24e40d50147e4b19e46b43860186c49382bfa1
    role: context
  - path: pages/traits/metabolism/thiosulfate_respiration.html
    sha256: 6ed0add2cba711f9b44d3cfbc8c0cd5fb8d6ac528611d17daa0cd26cec3c20ac
    role: context
  - path: pages/traits/metabolism/three_hydroxypropionate_bicycle.html
    sha256: fc8226734d5785c04881b21dea5183650e18204788618946e4ab4ce834eec0e0
    role: context
  - path: pages/traits/metabolism/three_hydroxypropionate_four_hydroxybutyrate_cycle.html
    sha256: a51abed2f490ad3b4c21714fc0111752021111c29126705dce15c08a14bd65a7
    role: context
  - path: pages/traits/metabolism/transports.html
    sha256: bab7e33e3e8738baacea9820943362aea03f7a5268c994d611c5e5854cf1a318
    role: context
  - path: pages/traits/metabolism/trimethylamine_n_oxide_respiration.html
    sha256: 9d218003f53afff9a1540a13ebb7e9af28781d4a7a435128983a0d5612a67b0c
    role: context
  - path: pages/traits/metabolism/uses_as_carbon_source.html
    sha256: 23507e61d7d09fd56dcfa7341f200c9aa7fa2f2cba1ac6ff3233bf7c050a793f
    role: context
  - path: pages/traits/metabolism/uses_as_electron_acceptor.html
    sha256: 9acd821af7ba4da2695555cd19e0a7d18019882695590fef9741b1071e7fb8b0
    role: context
  - path: pages/traits/metabolism/uses_as_electron_donor.html
    sha256: d974e0f13ab4589a24e4f9da40a748da0d6b4b37e7c1e3c2533334b022bb937f
    role: context
  - path: pages/traits/metabolism/uses_as_energy_source.html
    sha256: 282f4dd83c09f6abb8e37730b506540b620c5c7a2c69f63626efd1e7c6755a93
    role: context
  - path: pages/traits/metabolism/uses_as_nitrogen_source.html
    sha256: 31975dbb4ddfad54c72b3671ad8ab4c82bfb96143ebb4e195d70c4100d07d10f
    role: context
  - path: pages/traits/metabolism/uses_as_sulfur_source.html
    sha256: 310cf0c34c2898274fed2512d6a9907772a85dce53633f6872f9cba7ffb518b3
    role: context
  - path: pages/traits/metabolism/uses_for_aerobic_catabolization.html
    sha256: 22eaa0fe4662e49672171a149a602655b6c8543614cf6a1e7229210bfc5b0e16
    role: context
  - path: pages/traits/metabolism/uses_for_aerobic_growth.html
    sha256: a38aa92dfb5aa9715c350e9e865924a23798c829f0adea3710c6d7d7b583fd7a
    role: context
  - path: pages/traits/metabolism/uses_for_anaerobic_catabolization.html
    sha256: d2d399104a0115c41625030e9644a2b3bb8a19e3634809f0e28070fce0f62e60
    role: context
  - path: pages/traits/metabolism/uses_for_anaerobic_growth.html
    sha256: 79b9ec2febaa0f039b96e1cc2bbb0aafccb0d1b1dbee653c3ed02c5eccf39c62
    role: context
  - path: pages/traits/metabolism/uses_for_anaerobic_growth_in_the_dark.html
    sha256: 4779ad83357c957680fe5537def9821bc2d3d77c7697764f158808235e0c94a3
    role: context
  - path: pages/traits/metabolism/uses_for_anaerobic_growth_with_light.html
    sha256: bb000c496250653d47fb8aa8d195cc9a3d8dd5197c732e8e0d975ca5be433f3e
    role: context
  - path: pages/traits/metabolism/uses_for_growth.html
    sha256: ec2d54fe182a50bcc429822b913a87642cd5e3b4afe5a645bfd8717f5ba5298c
    role: context
  - path: pages/traits/metabolism/uses_for_respiration.html
    sha256: f2d0b3bce2445c4257833fc1e1450360a909a86232b7a7058065ede20425edde
    role: context
  - path: pages/traits/metabolism/uses_in_other_way.html
    sha256: 3f97fe999ddca5f686b674d79791b4fbd55618c0fac94e81c9ff9e6164f818f5
    role: context
  - path: pages/traits/metabolism/wood_ljungdahl_pathway.html
    sha256: aaf97a3d3f956ac1bda19b7f9248904b6e4c24ea07702d7d1a15d416dcd471f3
    role: context
  - path: pages/traits/metabolism/xylan_degradation.html
    sha256: 2f5ee2d10870fbd39367fc4e8ca4759100f8b7fd7432459217a9d7ef717ac186
    role: context
  - path: pages/traits/morphology/akinete.html
    sha256: edf5865a897005f0b200561af92150a3d8ce030b38d909b91c0ad63a6667d5b6
    role: context
  - path: pages/traits/morphology/amphitrichous.html
    sha256: 94657f9eb946d77352560a7b49cc19fc7e6e314107e1defdeab9778e1e490e34
    role: context
  - path: pages/traits/morphology/axially_filamented.html
    sha256: 4d896e3f1d5cd463ff756d6a6f22f9804a644fab2d5e77bca3b538184fc88a5d
    role: context
  - path: pages/traits/morphology/bacillus_shaped.html
    sha256: 62c1b82f970db40309cf7a456d481b136f567d64bc38812e3dd1a15c62779236
    role: context
  - path: pages/traits/morphology/baeocyte_formation.html
    sha256: 01be51ac8297cbf281131b0e13bf5aec4c8610289da551cf2358a29f56b10154
    role: context
  - path: pages/traits/morphology/black_pigmented.html
    sha256: 046acae9105078ec7a21ba7d923d8dfcce2a65842490db6fac9bbf09ad54fdde
    role: context
  - path: pages/traits/morphology/branched_shaped.html
    sha256: 69777d27b98becffa71a2e8d6a7b1ce93d1eceb9f106565dc519d3d8f5416e5f
    role: context
  - path: pages/traits/morphology/brown_pigmented.html
    sha256: 92fdddf757893b408803400b077a50578c65ab93c8550b58b3750344b0444d55
    role: context
  - path: pages/traits/morphology/capsule.html
    sha256: 8d2cf643aed76af12892d99b679197bedae3af48277386a0f43b6c5983d91963
    role: context
  - path: pages/traits/morphology/carboxysome.html
    sha256: 1cb615df4b3fed5b61ea4e499f42610b669489c31e2ba71283168b64ed821c1d
    role: context
  - path: pages/traits/morphology/carotenoid_pigmentation.html
    sha256: 6800d2d17a41568cf0d12ce738e38e0d86ab881759dc8f35c95fc44532daddaf
    role: context
  - path: pages/traits/morphology/cell_length.html
    sha256: 9d7e37749b003f58ebec8711a10a77cfdf184bae7eaf2f77749ba07cbc7592f6
    role: context
  - path: pages/traits/morphology/cell_length_large.html
    sha256: 648fa143a4c4fe5ccc57a594eec63ce45f8c687029ac8ef6ed45a01b7c4b50d0
    role: context
  - path: pages/traits/morphology/cell_length_medium.html
    sha256: 9d586d8cc88c34ec99ebcd78798d791c5f666c3e00caa54630ac224cd780c9ec
    role: context
  - path: pages/traits/morphology/cell_length_small.html
    sha256: b82da1f25694975649c773f36001a126de82749e1d7ca9158f98219f114eddf7
    role: context
  - path: pages/traits/morphology/cell_length_very_small.html
    sha256: 894cc7ed815291ce2b7e1fc83b92be9912ffdf8b1948c31a0f29f1376c0f4a79
    role: context
  - path: pages/traits/morphology/cell_shape.html
    sha256: 86eb833bf434178017e06605ea1bd5480036c2f002536dec285d1c20d5d3b9ea
    role: context
  - path: pages/traits/morphology/cell_width.html
    sha256: aacaac29bb8d3d7bfa358ecff24a276e2ce62320807d1367c6ed34aef6250a0e
    role: context
  - path: pages/traits/morphology/cell_width_large.html
    sha256: 1cb4bef79be09fccf78ab9a6c2548cca1c62d5b98e6175a48932c123d5bc1596
    role: context
  - path: pages/traits/morphology/cell_width_medium.html
    sha256: 5ee94a7a0b6a60522d8234324d06b03044d60671ad2879c271d7ecc121da8eec
    role: context
  - path: pages/traits/morphology/cell_width_small.html
    sha256: 4d27adecd77f60084ec4ec881a7a852948c63b757007ef7ecd54c70e31a7ce6e
    role: context
  - path: pages/traits/morphology/cell_width_very_small.html
    sha256: 6155c248883113549afbb68045762f70cd1afec9b9635392d4b95afba0b35137
    role: context
  - path: pages/traits/morphology/coccobacillus_shaped.html
    sha256: bcbfe202c3f183004819059c0524bd752a3828a3b69c14645ac76ca020faaa39
    role: context
  - path: pages/traits/morphology/coccus_shaped.html
    sha256: b1d4f651388f5f05b4f7a9d74d2c792c50cfb98b3c9eb0e4c35efeb608973b4a
    role: context
  - path: pages/traits/morphology/coenobium_formation.html
    sha256: 546e6f2040eef8615f5fdff69fd0fa84d83099fdade7b8d67a9c36cc6131dd7c
    role: context
  - path: pages/traits/morphology/cream_pigmented.html
    sha256: a59c642e797a510896274e204317a18c412f07741b8d7b88680352356c1f3929
    role: context
  - path: pages/traits/morphology/crescent_shaped.html
    sha256: 22597a8a6567cc124333fc2c9322edb196ef3544bb75c5954f13872655c3fcaa
    role: context
  - path: pages/traits/morphology/curved_shaped.html
    sha256: 48d4208ea434f4b3d434a3e8163d1447fcb150072915bfa31a971b93f2437dd9
    role: context
  - path: pages/traits/morphology/cyanobacterial_multiseriate_trichome_formation.html
    sha256: 93e4299f457610f3bb93d2f1187da5e5dd388502cd5c34db7144409e12f5b2cd
    role: context
  - path: pages/traits/morphology/cyanophycin_granule.html
    sha256: 405307a3ffc1220d43670ca25cdb0aac1759e70d90ac21e6f13549fd11e81d7e
    role: context
  - path: pages/traits/morphology/diplococcus_shaped.html
    sha256: 83713a5453661a4bb388b3dfa74ba780f1a654d001cd09cd7ee60be8e407fae4
    role: context
  - path: pages/traits/morphology/disc_shaped.html
    sha256: 024e19f60cce4f809262ec06a228570fe60401e96aecde98a7834c5bd45cff62
    role: context
  - path: pages/traits/morphology/dumbbell_shaped.html
    sha256: 31ed91ad3fc250881ae7df4a4be26fdde9c445fc5f0117b2ffd327d16e6b177b
    role: context
  - path: pages/traits/morphology/ellipsoidal.html
    sha256: 3b774cbed345ea7d888d046a87b8e89c288ee80f21868d76d4e62b161e60f1bf
    role: context
  - path: pages/traits/morphology/expansion_driven_sliding_motility.html
    sha256: 98bd2f7d439c6e6241a3547e3cd53e3a5519cd432c5b2c1e92c4c81b4fb52997
    role: context
  - path: pages/traits/morphology/false_branching.html
    sha256: c74dc832f6569f259703293076514a84b3c1d2c6e4d98e0567c0c23b37dde568
    role: context
  - path: pages/traits/morphology/ferrosome.html
    sha256: 2595ce897d8490e73f5a03ba77154846b5cde1bd8db784b6926b65c7e086a8e2
    role: context
  - path: pages/traits/morphology/filament_shaped.html
    sha256: 72617c2ee824e12547d16ada7687fd3a7b96761452c44de93bbe6586c4e0588c
    role: context
  - path: pages/traits/morphology/flagellar_arrangement.html
    sha256: 37668c878cc08ee10a6f014f95be5ce8100c645ff131226b3fd7c47d89a19027
    role: context
  - path: pages/traits/morphology/flagellated.html
    sha256: 362a6ca39a96b1f8ba4437b5a5ec6335d7ed7d37a25f824f0377f00698ef53cb
    role: context
  - path: pages/traits/morphology/flask_shaped.html
    sha256: 058b8bfa0dc43b1dce734837fa41b5986087d10285ab1a6925eead6d62a71821
    role: context
  - path: pages/traits/morphology/fungal_adhesive_column_trap_formation.html
    sha256: ef428a893f5924381f371afc9bae0bc27ddd2a950de8cee59a67ec5d9d28bb3b
    role: context
  - path: pages/traits/morphology/fungal_adhesive_knob_trap_formation.html
    sha256: 92f37133bcd1345c9df6d1a2676631660d79ea1fe3424a8d4adfed03d98649c1
    role: context
  - path: pages/traits/morphology/fungal_adhesive_net_trap_formation.html
    sha256: 5b176aa12413608a857684925704ff39ae03af739d1251106ce43f970258bf8c
    role: context
  - path: pages/traits/morphology/fungal_appressorium_formation.html
    sha256: e017f42dd0fec686b14e5537ee88f96c2192d910a6316265801acf490648189c
    role: context
  - path: pages/traits/morphology/fungal_arbuscule_formation.html
    sha256: 17fdfc607759a1b8e9564e9550270668c8eb4e195717d1fed64e263cced1c870
    role: context
  - path: pages/traits/morphology/fungal_auxiliary_cell_formation.html
    sha256: e1477b41e898a891013db26c131903d57693ffd88e6f5da9a89140471f66fab1
    role: context
  - path: pages/traits/morphology/fungal_branched_absorbing_structure_formation.html
    sha256: ffb689202a5b3f9ddafc053f403a00eaa38247440c0728f683bf0f5037cb9584
    role: context
  - path: pages/traits/morphology/fungal_chlamydospore_formation.html
    sha256: c2f89ffd533d3b872911eb74bef9e7fe917a565ddcb1359ebcfe3c5c8d4b72ba
    role: context
  - path: pages/traits/morphology/fungal_conidiation.html
    sha256: 0783a9edbb1f797bbbafa565ff1671a9b9ddfbc143701e266a15d8736eff5671
    role: context
  - path: pages/traits/morphology/fungal_constricting_ring_formation.html
    sha256: 84e7d287db218d4cd923ae1b20841b5c9cbee90ec3a5ec0319664f130a01b825
    role: context
  - path: pages/traits/morphology/fungal_hartig_net_formation.html
    sha256: 3710b35821fb270ea044da2c1cb867c7a981bae80763d585df0d47e63a1e4d71
    role: context
  - path: pages/traits/morphology/fungal_internal_mycorrhizal_vesicle_formation.html
    sha256: b2495d7aa62caac851e147dc96c9882e361c4c7943a289fff0757f05824a2978
    role: context
  - path: pages/traits/morphology/fungal_mycelial_cord_formation.html
    sha256: a5ed8119ac9358e30ad4e303553e520ee25eb42ab03e0f8140c657de8af14543
    role: context
  - path: pages/traits/morphology/fungal_nematode_trap_formation.html
    sha256: 18d728ba9d6a6c7c538f57f96e41caf2c7055e2e9ee3cedae7138920683f9dd7
    role: context
  - path: pages/traits/morphology/fungal_nonconstricting_ring_trap_formation.html
    sha256: 9df14ef8a8497dd3735177772c9cb83764710de9d3916eb7f621077a13dbdf1b
    role: context
  - path: pages/traits/morphology/fungal_peloton_formation.html
    sha256: 8fc1e9c96577f92dc6f7910119731a38ccb4470d63071fb1e47ff37eb44c7c23
    role: context
  - path: pages/traits/morphology/fungal_rhizomorph_formation.html
    sha256: b6855cf422274f8792446fbc1c9ed2914bb191772c1ae2c1c9cd58b0197584d8
    role: context
  - path: pages/traits/morphology/fungal_root_mantle_formation.html
    sha256: 5b870c3a47c14df38f36c503a38d77a9fa2d12ac3a6a5187b90b3542b9668e91
    role: context
  - path: pages/traits/morphology/fungal_sclerotium_formation.html
    sha256: 14df1a5c9ea8dd57b31641662e76f8724bac870eb9f16efdbc00f5f501e8b418
    role: context
  - path: pages/traits/morphology/fusiform_shaped.html
    sha256: db916cbdbe2f4222aa515e19d854445fbf2199a5bccb9f0e4c7896a1bca761c5
    role: context
  - path: pages/traits/morphology/gas_vesicle.html
    sha256: aa17f93b91d79a1f8d78bf8831545ca18fa174ab8ceda1a83e1bad90507c914e
    role: context
  - path: pages/traits/morphology/gliding.html
    sha256: d1225c6cb00117e5981a19596b56e531fd84b83544b86ca63fe6eb907eaec37d
    role: context
  - path: pages/traits/morphology/gram_negative.html
    sha256: 0e1d0db040d9cabc33e3e2b36ee007da89d2dd418c836f2cd45be3e5b5cf2242
    role: context
  - path: pages/traits/morphology/gram_positive.html
    sha256: 429c3c3343e1e8b456658952d2b3d7ee214a9d86d8cb09660c79256d6612c4df
    role: context
  - path: pages/traits/morphology/gram_stain.html
    sha256: 922e7f5f852980289af611d84b8bb5f8474f87eac9d2f81efc7c5c7db3a92b48
    role: context
  - path: pages/traits/morphology/gram_variable.html
    sha256: c227dee721e3380df84c0ede82ee10fb4daba92bb42337615679cf967f8f7dbb
    role: context
  - path: pages/traits/morphology/green_pigmented.html
    sha256: ed20244a6e299cb6ce29751e0d072e65ebac7d2621ecfaea64394553ff22af4a
    role: context
  - path: pages/traits/morphology/helical_shaped.html
    sha256: 00b64e2c6f7ce5be6a6ad4949547d4ee39037e0072fe0e1477e226d0a74f1cb7
    role: context
  - path: pages/traits/morphology/heterocyst.html
    sha256: 06601d3ae327e771278a5a23df5d933eaa0af742da5edb2218ce3ecdef5ad602
    role: context
  - path: pages/traits/morphology/holdfast.html
    sha256: 74af6307c7667c5e9c8f7ecde3c9342e562a186f1482edc06707a1b6a780d3be
    role: context
  - path: pages/traits/morphology/hormogonium_formation.html
    sha256: b18f9ff5e5e6fcda1b112b92c7cf8e602b3e5758042a1977d7ff26d6eab31be7
    role: context
  - path: pages/traits/morphology/intracellular_inclusion.html
    sha256: 78efafdf11cd335a536948aeb782821628351e327d6b476786541051d42bbc5a
    role: context
  - path: pages/traits/morphology/irregular_shaped.html
    sha256: 1458a01982bc48657ee4f0627584d68b79a03874de25c1edd3185f1df52d5de6
    role: context
  - path: pages/traits/morphology/lateral_flagellation.html
    sha256: b8d8983fb31bd8b91136929d365a74c5cf908ff770cf1b9469925f83019b9da5
    role: context
  - path: pages/traits/morphology/lophotrichous.html
    sha256: 1303afcd1a59076912fea7b9ec9dbd37589249a4257a121a707d5277749a0583
    role: context
  - path: pages/traits/morphology/magnetosome.html
    sha256: 95fd5ac25f2acebf4fe7e6b04ad3a3b15c667ed8c4caf8ea622e7f580380d560
    role: context
  - path: pages/traits/morphology/microbial_haustorium_formation.html
    sha256: 47686a6102f02adb42950da5cd551179fddadc5390d576f41ea7f16ab1983717
    role: context
  - path: pages/traits/morphology/monotrichous.html
    sha256: 2cadc1d31a9090742fc5fcec14bee4d7877aeb9da6adba5c9b0c18a59c17f4ad
    role: context
  - path: pages/traits/morphology/motile.html
    sha256: 074c31a18d344266701cfe013b7a9a59cf6fc780076c9d1b915493c261849cc8
    role: context
  - path: pages/traits/morphology/motility.html
    sha256: 2813e861d68943a68218580d96e85d3b22ef19472b692d813933e0b35c781de1
    role: context
  - path: pages/traits/morphology/mycelial_growth.html
    sha256: 9b36c71968f706aef721e9b4d5b65fe4c1ed1531b881782be955c4b9478d55c3
    role: context
  - path: pages/traits/morphology/necridium_formation.html
    sha256: d6638b0ac18802a07877f50f910102f6b53b593a95bb5999bfe492da9cf4b6f0
    role: context
  - path: pages/traits/morphology/non_motile.html
    sha256: effb4071d6075c6307210e09eae0ae87a8e3bf99eb504f8172156dfdc76ee079
    role: context
  - path: pages/traits/morphology/non_spore_forming.html
    sha256: a50423d462969f04ec15aac2b9b2a63035fe9e833835f6f178b434453fedeefc
    role: context
  - path: pages/traits/morphology/orange_pigmented.html
    sha256: c938fcf70998281416d6f54d4578c635a6e1f8b594a207310220b449048b0dc1
    role: context
  - path: pages/traits/morphology/oval_shaped.html
    sha256: b0d3be5488ed05bcc1a9f7a9210c37cf315b217e6efbf5cd2c541a2fb1598731
    role: context
  - path: pages/traits/morphology/ovoid_shaped.html
    sha256: 6c405ba0f557a87635605fa5594356e2e22fe7a3d9bb7b143a31332162ab1d61
    role: context
  - path: pages/traits/morphology/palmelloid_formation.html
    sha256: edf9a76c28fb9ea55492f493e2fe3ed98fbc126adcf888c486863ca6a8209452
    role: context
  - path: pages/traits/morphology/peritrichous.html
    sha256: 5dfe00dc104917704d52b128fc45a81f408d3da324f08d9704d8c8170d9978ef
    role: context
  - path: pages/traits/morphology/pigmentation.html
    sha256: 2336f8e5e359c0b180a26cfe9163980c7cff0bc22e782c4124474e9f5bf6121b
    role: context
  - path: pages/traits/morphology/pink_pigmented.html
    sha256: 5d73aba973a6656969d0ee298a9278dddd1646d174089acad92a4d1b171859ea
    role: context
  - path: pages/traits/morphology/pleomorphic_shaped.html
    sha256: f4df2e8bb6c296cc44ed4ff7d2a74b68482d1a8287348cf879ed666001b626b4
    role: context
  - path: pages/traits/morphology/polar_flagellation.html
    sha256: a186fd6b62a3adb926d557da21d6feb74f31d365d0f21731b8194e733d8c7181
    role: context
  - path: pages/traits/morphology/polyhydroxyalkanoate_granule.html
    sha256: be785805a3a132365e8a06ab35436eca7d24d55c3455b8670c0f81787d5fbb3a
    role: context
  - path: pages/traits/morphology/polyphosphate_granule.html
    sha256: 59d9a221249c25f443385b3cbafeba76ef42a3761b2c8bd9a65f69c2a96d3815
    role: context
  - path: pages/traits/morphology/polytrichous_flagellation.html
    sha256: 9cf4f541aafbe703f1cd63260799f7e83d9ad7f11ca7d219d67b96a8f7744bae
    role: context
  - path: pages/traits/morphology/prosthecate.html
    sha256: ef2322ca51e576ec63819f219e278fd62c3fd433783ec70b205e4d1ff7226ad1
    role: context
  - path: pages/traits/morphology/pseudohyphal_growth.html
    sha256: 694bd0c62f7797d260b3c50c834b330d579bb259b8512ea7451d3c75472afaa5
    role: context
  - path: pages/traits/morphology/red_pigmented.html
    sha256: 74cefb24f2154e9f217cec019aeb8a675ecfc2d6e9d7af343e706f96678f9735
    role: context
  - path: pages/traits/morphology/ring_shaped.html
    sha256: 2613fb3c372d819f686732ba02d4219a48bd0b767674115be221e4b1a7a3a869
    role: context
  - path: pages/traits/morphology/rod_shaped.html
    sha256: 92d4af3714f8be3b6707aaa42b1237c9744284ad3d0832ab1efd785a41954865
    role: context
  - path: pages/traits/morphology/rosette_cell_arrangement.html
    sha256: 26fefd3dd0908d028323ff5df496e8e1f6b2028aef3cda61df6038e4259f1db8
    role: context
  - path: pages/traits/morphology/s_layer.html
    sha256: 9f1eeac002382ad61e754200074b97fc8e578dc14adad80f6383390c0f9621bf
    role: context
  - path: pages/traits/morphology/sarcina_arrangement.html
    sha256: d953f347a4006b8de7d820344ab02f8d417a79d9ff71c100cfd1e915d3ab1ac5
    role: context
  - path: pages/traits/morphology/sphere_shaped.html
    sha256: 1fdf784bec953c54bc39215ee38cd37f25cd8deb2390b9cb03686f5b70b0dc2d
    role: context
  - path: pages/traits/morphology/spindle_shaped.html
    sha256: e736d7352f83714ad1320b082241df29cdd7d4a5478501160bc0e253ed628b36
    role: context
  - path: pages/traits/morphology/spiral_shaped.html
    sha256: 6f0197839077f23665a2bdadf467a35764571a617358e522afb027d35a19664d
    role: context
  - path: pages/traits/morphology/spirochete_shaped.html
    sha256: 5e6ba4bb4ab6e7851742881543366d28837966d578709af621797b443a4e7633
    role: context
  - path: pages/traits/morphology/spore_forming.html
    sha256: 216684d90113b6deb5449354c6fea5f1bbeb843d7306eace0c8a00f0eb1b37c1
    role: context
  - path: pages/traits/morphology/spore_shaped.html
    sha256: 5219cf769be5a110134538e6d27f57c4cca32cd12dc97ea18bb34b35e1af6a24
    role: context
  - path: pages/traits/morphology/sporulation.html
    sha256: 0f9a92cbff5507061713769db7ba54409ca006fc794821d0c1568e3f6b1730f6
    role: context
  - path: pages/traits/morphology/square_shaped.html
    sha256: 578c94d36d56e0cd7270f0874467b5b76f882b789506b98f492a8e2146816631
    role: context
  - path: pages/traits/morphology/staphylococcus_arrangement.html
    sha256: 218911dc1e1dc84ea2fa467c529fd2d261125a02ee8d158f352d028bef8f20a7
    role: context
  - path: pages/traits/morphology/star_shaped.html
    sha256: 838351e1eb476f3086b6262dfe9d953b158218ff8424e447be8f7241d50d2d81
    role: context
  - path: pages/traits/morphology/streptococcus_arrangement.html
    sha256: eddf169676ec9153a702e36ed64ab88d6bc3f7908c71d491443a81ed4a47e2c4
    role: context
  - path: pages/traits/morphology/subpolar_flagellation.html
    sha256: a743c7fbc440e03ffede74e1ea29e2b8cd2c93fc3970e9a774119f12fad2f2bc
    role: context
  - path: pages/traits/morphology/sulfur_globule.html
    sha256: 54340a2b6269fd32031b07fb27b169da26ffb55f1f3d94140ae10539be3668af
    role: context
  - path: pages/traits/morphology/swarming_motility.html
    sha256: 4515ca8abf2b3e7cf292566dae1fac906b969c1a037b66b8d504ad9ca891d291
    role: context
  - path: pages/traits/morphology/swimming_motility.html
    sha256: 8236d71079ca2cbae83fa1e425d4e775f7f7b614a227c9522ed12172be9a4b9e
    role: context
  - path: pages/traits/morphology/synnema_formation.html
    sha256: 5470e92215bb53051eef874dcbc6dc5f5004e29f21b6a1c890ef83795b6544b0
    role: context
  - path: pages/traits/morphology/tailed_shaped.html
    sha256: d1158125653a1e64961bdf18fd48c2ecb0a079aa6e9be26803775abb0a254b7b
    role: context
  - path: pages/traits/morphology/tetrad_arrangement.html
    sha256: 81804fddb3b601139fd68d8d62af6fe960e185a0709e6304de274309390d2391
    role: context
  - path: pages/traits/morphology/triangular_shaped.html
    sha256: 29e2c770389a704daba877c9e0525388545ef5098be25899abd9e7c6eb51d3f2
    role: context
  - path: pages/traits/morphology/twitching_motility.html
    sha256: c9b720493da59df717f324ed6d3daa84401cee29db2567ff3f568765d420fe9b
    role: context
  - path: pages/traits/morphology/type_iv_pilus.html
    sha256: 3386494bd00d272897ac0fefcd75e29e3686a0780b92c81d2ccc57fb5737be28
    role: context
  - path: pages/traits/morphology/vibrio_shaped.html
    sha256: 0555812ab603872a3957017bea18d8d58ef58cabf95f939a622287e478fc4c8b
    role: context
  - path: pages/traits/morphology/white_pigmented.html
    sha256: c60b36ba1ab8ce371688f1f30b654a9e3627f544dba9963dfc0da21ef8949bf5
    role: context
  - path: pages/traits/morphology/yellow_pigmented.html
    sha256: 2e58e96795f43e329524ec28f9a875503dc02f53976418b4c720898427db7a57
    role: context
  - path: pages/traits/observation/growth_nacl_observation.html
    sha256: 910d2fbaef73bae79ffd72dcc670f78d255f62d83f95de8d90f1f7b1aad6875c
    role: context
  - path: pages/traits/observation/growth_oxygen_observation.html
    sha256: 740c31035a17495b36580029d66ac7f13c4a1b19a7f822eedcca13137a6e6639
    role: context
  - path: pages/traits/observation/growth_ph_observation.html
    sha256: bd7ae209af91dc21d4ac8e652dbdaaf663c9d6fad471f14721003590022936e4
    role: context
  - path: pages/traits/observation/growth_temperature_observation.html
    sha256: 0eab50efd06c79d84f520cc91ddef20cb27ab06bf5dda9c048a85e865c9b6cdb
    role: context
  - path: pages/traits/observation/nacl_delta_observation.html
    sha256: bf8801c86c17bbe7ac30747bb1ef059f505441bde297bb19bda45cd5ed9f4530
    role: context
  - path: pages/traits/observation/nacl_observation.html
    sha256: b73d709413d4a266b3bf9cb84c09607afdbdd008a9a28794b866a51180669fd2
    role: context
  - path: pages/traits/observation/nacl_range_observation.html
    sha256: be4cc21bec67fefe686817e9dcc176424f53d2734224efaa5848c16a6fabe605
    role: context
  - path: pages/traits/observation/optimum_nacl_observation.html
    sha256: d0867663ca0e996dd85a75796416ea8c0da9540b70b03ae25af1fe610857891f
    role: context
  - path: pages/traits/observation/optimum_oxygen_observation.html
    sha256: f57caea2ab54cf44797b1d4f8d51c63a9796190be38baedb45f97eea22e3a314
    role: context
  - path: pages/traits/observation/optimum_ph_observation.html
    sha256: 117911b63e4769d958c7d46637e57d1629b70a5803f2f37ff9e7cb2c95af9295
    role: context
  - path: pages/traits/observation/optimum_temperature_observation.html
    sha256: 6df8c48bfdf513d3395e302e7d11fa434a113b47f0fb998befbe6316d932af5c
    role: context
  - path: pages/traits/observation/oxygen_delta_observation.html
    sha256: 669e96b4eea5fe524d2c94695a0eea7a050e0239bad7ce60643874581a59a7ef
    role: context
  - path: pages/traits/observation/oxygen_observation.html
    sha256: 0d103c7fdb16cd27f0bc137653620020f4d992d10ab16a3c789b1257eebf5d39
    role: context
  - path: pages/traits/observation/oxygen_range_observation.html
    sha256: cedde94517144ced148e15f1636b5b7018445e8856a27a85d92ca46286fa7b6a
    role: context
  - path: pages/traits/observation/ph_delta_observation.html
    sha256: e39ff767287ac56dc5e23ee21535151efb51f3a176ca406af962fe4a17919e47
    role: context
  - path: pages/traits/observation/ph_observation.html
    sha256: 8855d17b85021f81c77fcc0d86cd80c89f8bc723994d0863c9cc11bb7b0caa8c
    role: context
  - path: pages/traits/observation/ph_range_observation.html
    sha256: c4fedcb379b0e7865420f43fb530d9a129d3ff50a7f9aece19967a0cbff46cf9
    role: context
  - path: pages/traits/observation/temperature_delta_observation.html
    sha256: 4db260226a5743f658c7ce7cbf83522466238935193b46c499a410899fd90ce3
    role: context
  - path: pages/traits/observation/temperature_observation.html
    sha256: 168762141101c1516056913eb76a57a9f175c4cf10311074d64655d6286d1473
    role: context
  - path: pages/traits/observation/temperature_range_observation.html
    sha256: a0aa4187dfa616778dee6672693f1c6baed2fa1dcc28cd09ecb8fb915a1d8bde
    role: context
  - path: pages/traits/other/catalase_negative.html
    sha256: 4ff695756f130678f848219ca2c731e93104159de5a238538c5f9e1ac96a0449
    role: context
  - path: pages/traits/other/catalase_test.html
    sha256: a0db92737fa4356a45fcc65e5530c423a4738c6b4495b637363c67b5f531e64a
    role: context
  - path: pages/traits/other/circular_colony.html
    sha256: 3927151abfb7793457368416b471d3f4e79198e9dd033f7565fb12b700bcc84d
    role: context
  - path: pages/traits/other/coagulase_negative.html
    sha256: 51e17829550cf2c9d1b22379d1487a2a51194c1163cb586c2822153fc2a60784
    role: context
  - path: pages/traits/other/coagulase_positive.html
    sha256: 34350f2c920aaf2fa575821d227c01c8c8f2f1de22002acb3165500d15938ebe
    role: context
  - path: pages/traits/other/colony_morphology.html
    sha256: cb2915b86fa4304d8905deb8aed9952cf6e86c0971edf1f970601e373a0bc928
    role: context
  - path: pages/traits/other/colony_shape.html
    sha256: 0675d7185d78d3f2f1e5be16bec99697514dd0238e1b0356ee870fd277a00bb5
    role: context
  - path: pages/traits/other/epibiont_phenotype.html
    sha256: 8eb28972beb88c4d208f23c8009329042d5d2b1e1632b6f4bb50358a832ab6f5
    role: context
  - path: pages/traits/other/filamentous_colony.html
    sha256: 23f3a53a5e1795ec9abc1caf6316055bd65797e3e16b99ffac2e460ca0e30944
    role: context
  - path: pages/traits/other/fried_egg_shaped_colony.html
    sha256: f24e6806218f71c9b3c6c8d184837880aa7e533216f33cd7b0a1bdb8b79d2a56
    role: context
  - path: pages/traits/other/generalist.html
    sha256: b9dcd8d090c80a2080fe5395f240d0917ffa3e47c0d2568254f3da1b041612d1
    role: context
  - path: pages/traits/other/hemolysis.html
    sha256: 860cdec5cf74166764320ff7647c2330cce85bcbb6a67778c75957ad0a5b16b0
    role: context
  - path: pages/traits/other/hemolytic.html
    sha256: 4aa0c5f91d8d0063563351bd2edba84bdcca7a39e191da746551a90b3b44d116
    role: context
  - path: pages/traits/other/indole_test.html
    sha256: 47601883676c5ab691a94353f23b8719206ac813f56123cb36794bada18a3c44
    role: context
  - path: pages/traits/other/indole_test_negative.html
    sha256: ba3be5c667391937744c410aaeac0b843a92ea456df74169a7e8af32eb6bc8e6
    role: context
  - path: pages/traits/other/indole_test_positive.html
    sha256: ed503a21010348254cce4f5851c6ef1b0bec6565f788fe2c5486aba5866ed5de
    role: context
  - path: pages/traits/other/irregular_colony.html
    sha256: e100e775a503236c14fcb23ca274cb5f47960b01180d2c0ce14b652b7cfb4fad
    role: context
  - path: pages/traits/other/methyl_red_test.html
    sha256: 34656cef3fd0fff8ac01fa7766edb95a8763423720c797e7553a557078ed1460
    role: context
  - path: pages/traits/other/methyl_red_test_negative.html
    sha256: c919232221664dac3a2aee4850c7a03ec84ff4f28a3a685a51c413b7bcb0c56b
    role: context
  - path: pages/traits/other/methyl_red_test_positive.html
    sha256: 6b91ff6ccd7ba4aac8b5dd0703cec3c48f05a9d0bc69d4f5232606d8b9582c94
    role: context
  - path: pages/traits/other/non_hemolytic.html
    sha256: 6abbf3485aabf8ff03a9b47439cb5ca03bde460afa4ca528ac1990543c68c3a6
    role: context
  - path: pages/traits/other/osmotic_tolerance.html
    sha256: 0676d11b802ef5534c9f94fa5ce70b726ddd02ad31a2184837ef079183f89952
    role: context
  - path: pages/traits/other/oxidase_negative.html
    sha256: 6bbd5412a05a4a02dd9d11c7d31e71997a3e445fed56867df8c04f4246da61f0
    role: context
  - path: pages/traits/other/oxidase_test.html
    sha256: f15c0832142480cbc123afb52fdd2229dcff4453626555fac9a5ceb85410af26
    role: context
  - path: pages/traits/other/punctiform_colony.html
    sha256: 3a0b8cbb54440922b3a05f3645ff9a344a81481dd7a1649f58eecc2c0070ddd6
    role: context
  - path: pages/traits/other/rhizoid_colony.html
    sha256: 4ae8fcb5cce1fcffaf73e949197616fdf390a690a49501c3cd576ce589c3dc1e
    role: context
  - path: pages/traits/other/specialist.html
    sha256: 6a97de58711b7038c2830ed0d8f56fb358ea7b20de4efbbbdd865e17b144447c
    role: context
  - path: pages/traits/other/urease_negative.html
    sha256: ceb50302dc1c0c78a928a7a9cf7d240fd67e6bb740e4b993131ff1b19fc6bb37
    role: context
  - path: pages/traits/other/urease_test.html
    sha256: 1fdb4bd358df8dab33e3cbb6bdcfd6b08ab5fa5201693d4ad979b75659cc84fd
    role: context
  - path: pages/traits/other/voges_proskauer_test.html
    sha256: ef23f4a706fe4c222b346cd4781edab173451f58587148ab82e5b8949c6117b9
    role: context
  - path: pages/traits/other/voges_proskauer_test_negative.html
    sha256: aefc58575255f69da197a22df1c5f09ea32cb16dc86b08e64bba9dcfca3cfc3e
    role: context
  - path: pages/traits/other/voges_proskauer_test_positive.html
    sha256: 4f9a79c05ff994a4db3bca2e07e86c212366e72a60b024d85ac4995b00d4148f
    role: context
  - path: pages/traits/physiology/acid_phosphatase_activity.html
    sha256: a38c77e1b8d2947671014fe722797a8370f232adcfb13ae26c6800b2d81dee40
    role: context
  - path: pages/traits/physiology/acquired_stress_resistance_memory.html
    sha256: 2ba1f5218462ffa47cf929f36df439b9bdecab64932daadf931787294a6ac51c
    role: context
  - path: pages/traits/physiology/aerobic_anoxygenic_phototrophy.html
    sha256: 0ef6ec919514fc50f6f4c957fd17582af6ee84c657f5914f3ee42a5d15b2424d
    role: context
  - path: pages/traits/physiology/aerobic_overflow_metabolism.html
    sha256: 87c5437c8986398670968bd81cec60e1925e6647447f546bdf3034e21653076f
    role: context
  - path: pages/traits/physiology/aerotaxis.html
    sha256: 9653804d1b5234deb5ba9beb3d1610cde3a180bae8c6ed0e25305b2ba548d2f5
    role: context
  - path: pages/traits/physiology/aerotropism.html
    sha256: 67503f125ce86a9f740860f994398f90317757a38a9167fa120a620cc19ba06c
    role: context
  - path: pages/traits/physiology/aggrephagy.html
    sha256: e14661a263441b1964afa5c783666106c43c064abfdf0fd711dea2fb8e352ae3
    role: context
  - path: pages/traits/physiology/alanine_arylamidase_activity.html
    sha256: 538b8197aace2a8a19650f74adeea308f094c7fed02fd97b25c5270cea19b838
    role: context
  - path: pages/traits/physiology/alkaline_phosphatase_activity.html
    sha256: ddc103679813956ddeb2f5f67f377779b0bf9720d1a6a5a9c095bb65593e219a
    role: context
  - path: pages/traits/physiology/alpha_chymotrypsin_activity.html
    sha256: 7642e086065c997860565f3b09d53743ac47564d0d570bad615b891abeab2278
    role: context
  - path: pages/traits/physiology/alpha_fucosidase_activity.html
    sha256: ac0d6cf555fb6241998978a70198e75aeb0720bbb4896966ef4d6818efaeaf45
    role: context
  - path: pages/traits/physiology/alpha_galactosidase_activity.html
    sha256: 7d9d9314623054d0d68014a3e363e9ff4d905a6044d01726c3318e9951f66781
    role: context
  - path: pages/traits/physiology/alpha_glucosidase_activity.html
    sha256: 7b147a472a5bbd51eefaefaeaf1f83c28fd247213af6f4858aeb57c321cd354f
    role: context
  - path: pages/traits/physiology/alpha_mannosidase_activity.html
    sha256: cbc82623c1ae2ce2da866ab0023eb904a95b9169d20a1f6649f7755e27153c78
    role: context
  - path: pages/traits/physiology/amylase_activity.html
    sha256: c98166cd61470a57e405faaf28c2c345dd13dc7b62f42e058c0224e60ceae5c1
    role: context
  - path: pages/traits/physiology/anisogamy.html
    sha256: 1eafc9651b404d1a852c3d31625ca25764a691a8969d6a1c2a5aceb502441f1d
    role: context
  - path: pages/traits/physiology/antibiotic_resistance.html
    sha256: d6721725f0526b29b9883c5f5d421df96fb91d954a25b7606deea4bd709eae28
    role: context
  - path: pages/traits/physiology/arginine_arylamidase_activity.html
    sha256: 36bcf1ecf26498624a9612c487e120cdef72a094f0ee7fe80bba0657ee503532
    role: context
  - path: pages/traits/physiology/arginine_dihydrolase_activity.html
    sha256: bc8ccb5dcbcd44c85616177a57f8c1f5de3832502ee32112fc2e9281242794ff
    role: context
  - path: pages/traits/physiology/autogamy.html
    sha256: 56178f3b525ba3510726177eb110721fd4af5812c2861b1db9665b21e6f42976
    role: context
  - path: pages/traits/physiology/automixis.html
    sha256: 8fcbcee389669c3204de9170889dbee1da463057ce4435cdb398944a46a02346
    role: context
  - path: pages/traits/physiology/autophagic_glycogen_degradation.html
    sha256: 6f71b829ff336cdd3c63cbf495b6e76fbc70a9b25a5524c9b160c94f0a84d60d
    role: context
  - path: pages/traits/physiology/autophagy.html
    sha256: c294a5451e4c697470bfa4267eb6a446ff4869aa89e8e7387f02fdf9b607d049
    role: context
  - path: pages/traits/physiology/autotrophic.html
    sha256: 296ac676a22a1ecb1021ee7850a5d60c3d72a02a4f303c74ead20660f5ba3500
    role: context
  - path: pages/traits/physiology/bacteriocin_production.html
    sha256: 8cf61127e2685d8c2257f28250eb30fadf4f6593b17207aa1d28c64a866485f1
    role: context
  - path: pages/traits/physiology/ballistospore_discharge.html
    sha256: 2f5674e3aab924a93b5f0cc3f00b9ad536e83c3c79a72b681b0710c4d4ecb6c0
    role: context
  - path: pages/traits/physiology/behavioral_habituation.html
    sha256: d34e0e0f75805611a4de53575b75b4d940fffbd8d3aa3524e0d263ded72ca5b2
    role: context
  - path: pages/traits/physiology/beta_galactosidase_activity.html
    sha256: f97249535ee86dcea33c53d2a03d1e37fcbd06b70b26083926951cf119bbaf8c
    role: context
  - path: pages/traits/physiology/beta_glucosidase_activity.html
    sha256: 9f8c9cea924e11561546b504720c25af4d9471a7996b60ca9d86e56540a51182
    role: context
  - path: pages/traits/physiology/beta_glucuronidase_activity.html
    sha256: 3acb7fa8804173e4fc949ee3ceac60baf05af2e3fd9f4bb838d5e55ba6298bc9
    role: context
  - path: pages/traits/physiology/beta_n_acetylhexosaminidase_activity.html
    sha256: 9becaa4de0544c7dc687b5c51f51a3156fc128f918b6f9461e47abc0c4d5f395
    role: context
  - path: pages/traits/physiology/bioluminescence.html
    sha256: 7c15e3712ffe4f230aa1195663f1378cd8d3ba3d0bca285e862c94985faffa41
    role: context
  - path: pages/traits/physiology/biomineralization.html
    sha256: 25ebce1e5073a18aa24dac10f21ca079e1cc930fa5f88d06381cd8c0e20cbf73
    role: context
  - path: pages/traits/physiology/bipolar_mating_system.html
    sha256: efa29b6b112844a72096bacd8bddc14a341961f73345c0133e70d8e813864141
    role: context
  - path: pages/traits/physiology/carbon_source_memory.html
    sha256: 7fca1a0984112d1494b10b831429e5282e577003015985cec9bf87cfdbcd8dcc
    role: context
  - path: pages/traits/physiology/carboxydotrophic.html
    sha256: 6fbca10a6a39bd2a8463fc224d419030bf65f3f1fa43934e0de3a2f9175de268
    role: context
  - path: pages/traits/physiology/carboxylesterase_activity.html
    sha256: aa8c0c4d78b180877c66a0735a885f1e87e30fbaa26f4bd56389b4594ea7104b
    role: context
  - path: pages/traits/physiology/caseinase_activity.html
    sha256: 94409ec1000323bc15d2130f43af6fb1a85eaa95ff228905f3b8d61b14a09a2e
    role: context
  - path: pages/traits/physiology/catalase_activity.html
    sha256: 9aff062f47568fd352413c184e496029bce411a984071f5c068f652c7d77705e
    role: context
  - path: pages/traits/physiology/cellular_buoyancy.html
    sha256: 270c0ce6f3ea8508dc8299a9acae4425b2df2203f53330e4d36a449e28500186
    role: context
  - path: pages/traits/physiology/cellular_rejuvenation.html
    sha256: 072d4684d99dd18763e77846002e6ab7c9a2e61c002a97b29d88ce184c2e9c66
    role: context
  - path: pages/traits/physiology/chemoautolithotrophic.html
    sha256: dc15e0556b090309a49ede63204d0764a93ce38f2015675b9c179d70f70ce4f0
    role: context
  - path: pages/traits/physiology/chemoautotrophic.html
    sha256: 1faeb9a917db0cbaa105c5985c7fe153d05693fb9faa5a943ad056099df87970
    role: context
  - path: pages/traits/physiology/chemoheterotrophic.html
    sha256: fc3ea8d434cd096709b26c05649817350eb8147c741b8b56ca39d843a9cfaef3
    role: context
  - path: pages/traits/physiology/chemokinesis.html
    sha256: 44da7ef44d5db1388b3999f7ada559a9961b35f654c5d7510800b4c7ee92013b
    role: context
  - path: pages/traits/physiology/chemolithoautotrophic.html
    sha256: 7a582b3744fa8301c1ae344d1143b82a2302936d0bc85527588653b6e74ded8f
    role: context
  - path: pages/traits/physiology/chemolithoheterotrophic.html
    sha256: 469c080507b72a262987d03584f27671ee9587ec2a5de9a07c7c4c1bb8b86a04
    role: context
  - path: pages/traits/physiology/chemolithotrophic.html
    sha256: 7fb9f6c385827c003fcf4216988a0f19c285048fda3beb4b75e4bc3c14726125
    role: context
  - path: pages/traits/physiology/chemoorganoheterotrophic.html
    sha256: e7ed5fadb24432e3dcd2e9093ebffa8b2791a5da3977ac9b67367a13460b1c05
    role: context
  - path: pages/traits/physiology/chemoorganotrophic.html
    sha256: a0a817547fa8958aff25b64c61b584353256b29e29c29b06129898c82bfa6aba
    role: context
  - path: pages/traits/physiology/chemotaxis.html
    sha256: caf6cfdb1060b55cb40ee8d473e40d02f95cfd9d7151da39e27788441089dea8
    role: context
  - path: pages/traits/physiology/chemotrophic.html
    sha256: b414ae4d63d3b331ab42cbd2cd1290dc16d546d36f99d75d4a43074785eb2fd1
    role: context
  - path: pages/traits/physiology/chemotropism.html
    sha256: f47c1ad29a4771460e9c44997479e36031b918d2955924bf842de306f6f628d9
    role: context
  - path: pages/traits/physiology/coagulase_activity.html
    sha256: 9ba2fc040a0051925cdb5c6ca3fb8e66387f246887ad6a37aa38f2a8d99901fd
    role: context
  - path: pages/traits/physiology/coccolith_production.html
    sha256: 16dc44ba7de99273f689ede5c9bae36f90b671d7e7dfb03a7cc2a2bea5a6a04f
    role: context
  - path: pages/traits/physiology/cold_shock_response.html
    sha256: 8ae87f7bccfa2c083400e5ecf629b77e75001751b3151d532563d8a24055ff1e
    role: context
  - path: pages/traits/physiology/contact_dependent_outer_membrane_exchange.html
    sha256: 72189199874c982d30b4daf2d66c2eb3abcb188d117d5757b5f0ed90b2fe9a79
    role: context
  - path: pages/traits/physiology/copiotrophic.html
    sha256: 849216cd0b371a500ee335fc8d9c9e0b167e4fe0b91be076d2b26d8b03e2b701
    role: context
  - path: pages/traits/physiology/cue_triggered_environmental_anticipation.html
    sha256: a855e4d9dd89ca661f0171c8611b132b701f712b82c8edd45c5b5d8080d1166b
    role: context
  - path: pages/traits/physiology/cystine_arylamidase_activity.html
    sha256: ea00f293e21be44d39a6c122b9d1be60909f778e253e15cf18afd720bf3d38db
    role: context
  - path: pages/traits/physiology/cytogamy.html
    sha256: 1f5b57236e1a039b0eeb3cd4f0635e27c505260b2faa1fa880f1368ab0ffd1ef
    role: context
  - path: pages/traits/physiology/diatom_frustule_production.html
    sha256: ee2ec972dd97cda2f4e52420d9248783c2ca8e3347a1b6c3f3873ee9dd79c05c
    role: context
  - path: pages/traits/physiology/diatom_perizonium_production.html
    sha256: 4af0c6aeb35d32d07d99bbe7ead4323e590eb1869e70633c3d879a13104e0eb9
    role: context
  - path: pages/traits/physiology/diatom_seta_production.html
    sha256: edd916a8bb1303122e87a45891f29f31d3810c60b1b0c68df1d173fb05b22f96
    role: context
  - path: pages/traits/physiology/diauxic_growth.html
    sha256: dbe9e038e9dac0980ed8d15c158621bbb8574dccf0c4dfabff207c2fad2f7525
    role: context
  - path: pages/traits/physiology/diversifying_bet_hedging.html
    sha256: ab75e0af3c73051c378da974e1f29221e24b74aace8459720a8e94fdd066e280
    role: context
  - path: pages/traits/physiology/dnase_activity.html
    sha256: ee614a37b32c820bb5f04cf4b1816910f00db432315a6c9b60a15fd98b63481d
    role: context
  - path: pages/traits/physiology/dormancy.html
    sha256: 4b2013b3fba0cc2629476077d7403e54f5c823edaff49a11a9db0f3b64c884f2
    role: context
  - path: pages/traits/physiology/durotaxis.html
    sha256: 9a33acdbf3ae412c5ccd6fcf2eea9910dd1b0f5a4522a8e3b6599a75edafe82c
    role: context
  - path: pages/traits/physiology/endocytosis.html
    sha256: 4451f56adc37867655c1f2573062b5a509c7816bf345139ed28f18930a1b7661
    role: context
  - path: pages/traits/physiology/energy_taxis.html
    sha256: ba04fe8f956df2831d4c1b3bb2db2377905f0ee1d06b0a0382e31434329574d2
    role: context
  - path: pages/traits/physiology/enhanced_transcriptional_reactivation_memory.html
    sha256: 418f8b1713df85ba06184b7cefb934ce9ea9166259ebcf8c05fb53069ba967be
    role: context
  - path: pages/traits/physiology/er_phagy.html
    sha256: 32d4dfac5616eeb422880ed0f614a81395ddeb5f05d9e2467313e2d22f23f9ae
    role: context
  - path: pages/traits/physiology/exocytosis.html
    sha256: 1f8466c8c2b83e77e88a5bb403ee49a1c404f2c8874d9667303c5034597c87b6
    role: context
  - path: pages/traits/physiology/extracellular_membrane_vesicle_production.html
    sha256: e602573f4d04e63a732dc3714e8cd524f7fbbe42c78b7234a07df1c0c9e7b9e1
    role: context
  - path: pages/traits/physiology/extracellular_trail_based_spatial_memory.html
    sha256: 8e74621326aa2a498341dc1e07e9c983e036b8020d1f962960a1279fd5cb5818
    role: context
  - path: pages/traits/physiology/galvanotaxis.html
    sha256: 1ab86e8bfb97af0f27cf4be3d0434d79e4caea20587f274d1c468f8fdeb6692e
    role: context
  - path: pages/traits/physiology/galvanotropism.html
    sha256: 4d2f5f589267e345dc73054c6f430ffb8968cc1671b047ee2d9befc6e68b4ce3
    role: context
  - path: pages/traits/physiology/gamma_glutamyltransferase_activity.html
    sha256: fd583624506e2c175f2c2216041707fdc9a5dd63576784e94dd442315db6fcac
    role: context
  - path: pages/traits/physiology/gelatinase_activity.html
    sha256: e086ccf72e0a9e0ebef1701a380f71236b0635d0f7f1e292edddc52ff5f068a1
    role: context
  - path: pages/traits/physiology/glutamyl_glutamic_acid_arylamidase_activity.html
    sha256: fdd4b8dffe231b40db9f2ae577a1f7f675f7cd7a5c4d6af24d4990897cd5f7b9
    role: context
  - path: pages/traits/physiology/glycine_arylamidase_activity.html
    sha256: 7aca8228fee9d9ba243638bc97541aa34e7073b4def44baf9ab9d0d0438f341b
    role: context
  - path: pages/traits/physiology/gravikinesis.html
    sha256: 8fabf9bfbe003a3ea8e48207dc37d55e9c08faa32c3afa0e3f684cf0510967d6
    role: context
  - path: pages/traits/physiology/gravitaxis.html
    sha256: 36ff75d0fb209bfb32e0912bceb8405b4acbfd30dec6312a67fb602f6957e8ae
    role: context
  - path: pages/traits/physiology/gravitropism.html
    sha256: 1f949b20ba902550dbd307db4efcdcaa3ccef1b67ae1c1a5a324c7ef1bb85c8f
    role: context
  - path: pages/traits/physiology/gyrotaxis.html
    sha256: b32c9fbf3867e85435a9416365d58add7c3c6ad085529b7cdcdf2be1326516d3
    role: context
  - path: pages/traits/physiology/haptocyst_discharge.html
    sha256: 5c07e6b5c55a8446548c2dc09c08655fc5cbbe3481acdb7ffd3307cf08953699
    role: context
  - path: pages/traits/physiology/heat_shock_response.html
    sha256: 3f5278e0bc926dc7c0073dbb3911d205f252dbd65cc2c9ed43fbd2c0a6a2dd72
    role: context
  - path: pages/traits/physiology/heterokaryon_incompatibility.html
    sha256: 7ff559963b3fb31d3646caae6a1eb420affe9c0b398a574e9dbd94e3d789787e
    role: context
  - path: pages/traits/physiology/heterothallism.html
    sha256: e2c2a20e4e5cebfdd08b1908f86c953af22120c1d1652e88eaa4df469e46507d
    role: context
  - path: pages/traits/physiology/heterotrophic.html
    sha256: d43b5abb6fed92c7dc4007a3dcf93fe25be0508fa60a63a35703af9a348785cb
    role: context
  - path: pages/traits/physiology/histidine_arylamidase_activity.html
    sha256: 540cdd4897b5a017bed3d8b8efcdb906196254f22abdef2d0ef1879cf5b1d1ea
    role: context
  - path: pages/traits/physiology/homeoviscous_adaptation.html
    sha256: 7d701f82e69216857b2e5184ee2b4e63cbd81f656364801e81d007578874bd4a
    role: context
  - path: pages/traits/physiology/homothallism.html
    sha256: ddc6e2801d89158a623b6baa06a92937c37a8cb7fc3a654a0f5e1e7a6edd44b8
    role: context
  - path: pages/traits/physiology/hydrogenotrophic.html
    sha256: 1fd7d51afdc2ebd6c0b35f93127f5ba81d7efa377e55afe68d063426e9b8fe56
    role: context
  - path: pages/traits/physiology/hyphal_anastomosis.html
    sha256: 5fa4e539131c7b78e6ced3a693aa6abf0a509b4dcf8e7c6837a5701ae01bba8c
    role: context
  - path: pages/traits/physiology/isogamy.html
    sha256: e91f8936a6d86028b536936ea273f19bdaa7ab415586520854bbc8772d0904a6
    role: context
  - path: pages/traits/physiology/karyoklepty.html
    sha256: a49dc5534a25ef6171a699d7fc6a6e4009002265f28d70ba68f2e77d456677bd
    role: context
  - path: pages/traits/physiology/kinetocyst_discharge.html
    sha256: 9f6d2107c1afe75eead2a3f73b18297ca2635b5ed60f27c358be1827ee61ad0f
    role: context
  - path: pages/traits/physiology/kleptoplasty.html
    sha256: d2466d955375553b3184617ca1180f2cbd4f0ca848d8e9b61f00d21651ce68e4
    role: context
  - path: pages/traits/physiology/lecithinase_activity.html
    sha256: f6fcae2554cd9d12c59364f1dc80a1c170794b77ea07c9915e8ee51435699f6e
    role: context
  - path: pages/traits/physiology/lethal_algicidal_activity.html
    sha256: cf0c86251e0d9a53e24079bce57ff80750e164378c89fc98d8c3a0e7b65cbd76
    role: context
  - path: pages/traits/physiology/leucine_arylamidase_activity.html
    sha256: 4b38b99f6dfa5b4a5ff2bc287d664563d45f4d92f7edc41e299261ad86b8f351
    role: context
  - path: pages/traits/physiology/leucyl_glycine_arylamidase_activity.html
    sha256: a6b0c31d6ae377a14bf5b664c8a58f993a0abfc9f6433fd52cc128b24d0b935a
    role: context
  - path: pages/traits/physiology/lipase_activity.html
    sha256: 324fa7b6f7120fb280672323a4dc7e70565ddbef7623e8482c751a1c5234f3ec
    role: context
  - path: pages/traits/physiology/lipophagy.html
    sha256: 1ac8875e7bbb4db6eafb8cd3fe0323d12bfb907932b8e4da2920197d6a9aa479
    role: context
  - path: pages/traits/physiology/lithoautotrophic.html
    sha256: 5e9bed9ac50c9dc5e063193055600b89fa0dabab71d0bd3afae45a943e7deda6
    role: context
  - path: pages/traits/physiology/lithoheterotrophic.html
    sha256: fd5155404c105f2514ff19ab2f236c4894b4420644d9955df92f768373181e44
    role: context
  - path: pages/traits/physiology/lithotrophic.html
    sha256: d155005c6e98da289c6d9b98a26409379819174cf2e0b2446f84b3893eed33c5
    role: context
  - path: pages/traits/physiology/lysine_decarboxylase_activity.html
    sha256: 62ad5d423f8cb0e275c620b9e5bf94527136c879a4c6b9b121817e4f2dafa20f
    role: context
  - path: pages/traits/physiology/macropinocytosis.html
    sha256: e24c00314d1a805291b610a737f6f70bd56ab752329d6f6c9e10f2a2a7d1dd6c
    role: context
  - path: pages/traits/physiology/magnetotaxis.html
    sha256: 8990547e858cb27804f7e827d43b5e5e55594906b7fa913a48deec789b674af7
    role: context
  - path: pages/traits/physiology/mating_type_switching.html
    sha256: 4d0425e53096dfee5f41405ffa29015cd0d28b517d26d2cdfee2cfadc0d2f2d2
    role: context
  - path: pages/traits/physiology/methanotrophic.html
    sha256: 50f4e5658e8ea3f55ba5657708b8c70bb5de8a9bcb16e67d45bf54c24d324a8b
    role: context
  - path: pages/traits/physiology/methylotrophic.html
    sha256: a9aab83535f7ab31d025c094d8975f5743143534991fa3c6bd016d71a437084e
    role: context
  - path: pages/traits/physiology/mitophagy.html
    sha256: 703394ecf1933c15e7062e72b56649d39f95d165a19cfe7ebd5892aed0e4feb8
    role: context
  - path: pages/traits/physiology/mixotrophic.html
    sha256: 33164ee9f861a908d2ee2f5de2d025d08c344c69449b0c2123517ba9979522ab
    role: context
  - path: pages/traits/physiology/mucocyst_discharge.html
    sha256: dd34f8dfa96b38101eb672f52752fe6afe7d1ad0dcf42546a78252632fe4fa70
    role: context
  - path: pages/traits/physiology/myzocytosis.html
    sha256: 4f473ab1b704f6ef004b571c9999efa44db1406721e1684bebb2c5a0817d207c
    role: context
  - path: pages/traits/physiology/nad_dependent_alcohol_dehydrogenase_activity.html
    sha256: 3653069ed8baf44ba8bc9c957e71a5b44361190091036991b6aa0e8de6618c4e
    role: context
  - path: pages/traits/physiology/naphthol_as_bi_phosphohydrolase_activity.html
    sha256: 26a4f8bc4b9491d5da5e2a9aaaff47e123354844b52c27fdda846ad48876913a
    role: context
  - path: pages/traits/physiology/natural_competence.html
    sha256: 8e7aba477d8c7175a8d9644fafcc75d43e406f123fdb9abc8fe79c8e8cc7ca7f
    role: context
  - path: pages/traits/physiology/negative_autotropism.html
    sha256: 452bd6b2fdbbe7f638cb7eaa0a73b5b6185f2cd402dacca1425de1a05200852c
    role: context
  - path: pages/traits/physiology/nucleophagy.html
    sha256: 1e2977bc34a0ac621060d793305554160ed9bda4d31173c054e7a20eefc98447
    role: context
  - path: pages/traits/physiology/nutrient_adaptation.html
    sha256: 1c64bdde439819f25e758101f8cfe21c5302d3cd381351d1fa39484f85d0ff4d
    role: context
  - path: pages/traits/physiology/oligotrophic.html
    sha256: 45c76f5c99a35da113ad7556a76750e487a2b525616be92c3c02e8ec71a718b4
    role: context
  - path: pages/traits/physiology/oogamy.html
    sha256: 1340b94cfc6ffc1dd518b214ab00c535019ad95467a2d740ba46ba969f9e681a
    role: context
  - path: pages/traits/physiology/organoheterotrophic.html
    sha256: 467993eaf4f1918c46eca533f20f375b73ee7eebaf02c2a383d51b179cc20ff8
    role: context
  - path: pages/traits/physiology/organotrophic.html
    sha256: 87d2a9117d3bcc417cdfe619a88a350c4559766c2c0a82e768f1f0e95d15cff5
    role: context
  - path: pages/traits/physiology/ornithine_decarboxylase_activity.html
    sha256: aa2c5e96f12d7805408068499bf96a5040a5261e942ce019f288f27824dee1a7
    role: context
  - path: pages/traits/physiology/osmotaxis.html
    sha256: 524e89cc81d049649057332d466a0e0bf88e255fdd414afe326385a7b8443b88
    role: context
  - path: pages/traits/physiology/oxidase_activity.html
    sha256: 4b42039d3f5099c19b7f5120c6612dede95d1973b05859aa9ff2db49ec8509cb
    role: context
  - path: pages/traits/physiology/oxidative_stress_response.html
    sha256: 08f0c85d5c16e690b0874e852a4b39b58cf6b7c37c5513ae2b18b0c9b1ed8665
    role: context
  - path: pages/traits/physiology/paedogamy.html
    sha256: bcea7c6f38b543386ee0d72e23f6aabb7f152002cb4fe2a80ead94b4049a65e6
    role: context
  - path: pages/traits/physiology/pallium_feeding.html
    sha256: 4bc71ad3f294e687ed7f428f74f6f1e591cee26c652304649ec52d35aa9694be
    role: context
  - path: pages/traits/physiology/parasexuality.html
    sha256: a9a121466966935ee6a58f20a01742ac3baae04a7a8d097678a49348915d633c
    role: context
  - path: pages/traits/physiology/persister_cell_formation.html
    sha256: 81234f32b2d389f69a74715570b92e51d97ddb6d00d1b17058bb35017e2b8eb0
    role: context
  - path: pages/traits/physiology/pexophagy.html
    sha256: 6ff71eeb1cd722fca60ed582874ed9eebb15cb800ef785dfa89babdcddb17cd0
    role: context
  - path: pages/traits/physiology/ph_taxis.html
    sha256: 5baca440dcf8e2667ba204f078dfe8afe08aea5e9f8fe6eb8f55a802a41b62e3
    role: context
  - path: pages/traits/physiology/ph_tropism.html
    sha256: f89b33e44e5102905c502b30551cbe5cd9dbfa293439db9512b9c34001eaf9c2
    role: context
  - path: pages/traits/physiology/phagocytosis.html
    sha256: fad1c6dedc7b7acd655aac954bdc0c96939ee7efcee3f9e4935936f29cab62ad
    role: context
  - path: pages/traits/physiology/phagotrophy.html
    sha256: b23e50d536d63ef9b0e11bab72ed30f9d2b53847a90bb7e99dded0d6ce7303a8
    role: context
  - path: pages/traits/physiology/phenylalanine_arylamidase_activity.html
    sha256: 15b41596409011d8aa1a449a6b5cb3e1e1e5c7ce94d6e5588785cc35d9dff1f4
    role: context
  - path: pages/traits/physiology/photoautotrophic.html
    sha256: e6294b7d63e406508b1928305b4266aa9dda1b0f0106f986737bba84c6a76191
    role: context
  - path: pages/traits/physiology/photoheterotrophic.html
    sha256: 5818a5de28aa0591aafb5c2f671b1af3b5849ac3b66e8ab2601fcbd4bf6ba4d4
    role: context
  - path: pages/traits/physiology/photokinesis.html
    sha256: 395308dce4494abc9fbb7b1cf63f590cb7556d026317959fd3463ca6ace08394
    role: context
  - path: pages/traits/physiology/photolithoautotrophic.html
    sha256: d50a5ffbf60d9742e1cd42ebdf079e82a208faa1e60d72ae408cae7bfabb165f
    role: context
  - path: pages/traits/physiology/photolithotrophic.html
    sha256: 60a15443f6d59458a699f41d4f000c6f784185dc15c7d82ea3aea9796fe817ed
    role: context
  - path: pages/traits/physiology/photoorganoheterotrophic.html
    sha256: aeb4aa88dcb2d841e7ff461db30697d38451eb50398f5e0201ba14ef92db56eb
    role: context
  - path: pages/traits/physiology/phototaxis.html
    sha256: 6d2bce60ce57871eda91d707fe345604b7528cded77f15f0501a73a07496161d
    role: context
  - path: pages/traits/physiology/phototrophic.html
    sha256: f78c1896d9f08cb217fa06a31b4822ca587ae2e2ad677d3031951bbccd568963
    role: context
  - path: pages/traits/physiology/phototropism.html
    sha256: 110dcd54ec48908686abd61216a8c170b23204ff83a7c5c7d36ddb12a84d472d
    role: context
  - path: pages/traits/physiology/pinocytosis.html
    sha256: b0741e0f24f2694544f45033ad854148b7e121be9f6543dc12cfe6514004e484
    role: context
  - path: pages/traits/physiology/positive_autotropism.html
    sha256: 481d70a959484ff39dc0541f9524f3a0ade5b893978aa9726548277067e7ff5c
    role: context
  - path: pages/traits/physiology/primary_homothallism.html
    sha256: cbd396629e640a3db7417061083dea00a8ad94a55a74f02e57c9b2388d39cd3c
    role: context
  - path: pages/traits/physiology/prolyl_aminopeptidase_activity.html
    sha256: 50c20021ee05f6ab00b86d5a284b51d878275d5dd0ec510ba6f59c5b74459872
    role: context
  - path: pages/traits/physiology/proteaphagy.html
    sha256: 0cad1c3432f907b04f929006cce0e3c6c26bbbb4d318284f4ffbff1be767cc80
    role: context
  - path: pages/traits/physiology/pseudobipolar_mating_system.html
    sha256: 6f3c316917da32725b0211b85982b07fbe12103177977e4fdaf749ee8a63a407
    role: context
  - path: pages/traits/physiology/pseudohomothallism.html
    sha256: 89672ba809e0b5f4d90d7a5fc196239ea4ffb15e3d4915df7f7a01a9c4887576
    role: context
  - path: pages/traits/physiology/pyrazinamidase_activity.html
    sha256: f97b8c836cf61bb1ec5f5be0d93661372b3e5cedcce686066b7f20ec975d82a2
    role: context
  - path: pages/traits/physiology/pyrrolidonyl_arylamidase_activity.html
    sha256: 9d8e64579101db538ca6c0811deacefbc1ce674a8525b3ed422a19b0fbfd5b24
    role: context
  - path: pages/traits/physiology/quorum_quenching.html
    sha256: d95c7c9bd80414d6a0691f808696d09fc56295a228486b128eab2d370846768f
    role: context
  - path: pages/traits/physiology/quorum_sensing.html
    sha256: 22811e5534ed3424c72b474ddd6e864f6462af734dbb554f621c360f3b385c67
    role: context
  - path: pages/traits/physiology/rapid_axopodial_contraction.html
    sha256: 25bce49187f05f1314bc5dac0671a711b1e112a87170881d4861050fe7151ce6
    role: context
  - path: pages/traits/physiology/replicative_aging.html
    sha256: 78c2ddd1275b49eb2cf3210f8b8161dcc13c4d4c0adf77b072fe81fabed3994a
    role: context
  - path: pages/traits/physiology/rheotaxis.html
    sha256: 077dd783a4597c644396e84f9c133ea2c7d47ab158b06c3ee4a687c77b6de541
    role: context
  - path: pages/traits/physiology/rheotropism.html
    sha256: aa67b63b57530a4f3acd5ca45adc04d4662b977c487e2433cdbc8f767cefc1f3
    role: context
  - path: pages/traits/physiology/ribophagy.html
    sha256: 7747dfc2bad5df44ac22574f6923912eb54187415fb596e16d72dcec1a68fef2
    role: context
  - path: pages/traits/physiology/serine_arylamidase_activity.html
    sha256: 46b03f38e683c446991d9e479b9525220eb6cae2cd723096a3e1d0919d94b476
    role: context
  - path: pages/traits/physiology/siderophore_production.html
    sha256: f64addc87a71b682abce577539c005af864154f0571e5df8a7efc6749581c07a
    role: context
  - path: pages/traits/physiology/siliceous_scale_production.html
    sha256: 5747d17cbae1f5f3ec8a11e71f03ffdbb4282a46986e9cb93203ca910ffedc3b
    role: context
  - path: pages/traits/physiology/sos_response.html
    sha256: 9ede547f2df8261d56b789c85a762ff9b608aa5538172360d091dfbf9437950a
    role: context
  - path: pages/traits/physiology/spore_germination.html
    sha256: f6e02dd15bdcae488dd1ea1008c3f4d71dbd4be053096881a717bd2ffc365978
    role: context
  - path: pages/traits/physiology/stress_response.html
    sha256: 8d54476fdef77f10227a728e8073badf0703774b4cb277992805cc7aa1081fa0
    role: context
  - path: pages/traits/physiology/tetrapolar_mating_system.html
    sha256: f20aef1e8a01d2c995bb5ea65e12a76c7edaa400d018b0ebb56b86e8de6125b5
    role: context
  - path: pages/traits/physiology/thermotaxis.html
    sha256: 21c36ce2554b40988263059bff1032107bb2085091637069f1394be2009d26ad
    role: context
  - path: pages/traits/physiology/thigmotropism.html
    sha256: 69373bf65f9b7c12e9d80657c32d45b9b798c3385f87baf7dc35d606b9877c2d
    role: context
  - path: pages/traits/physiology/toxicyst_discharge.html
    sha256: 2e36e39e3ea68c8936aa8660c67baa5b183233c9afd043b93504d8bb5d7c737b
    role: context
  - path: pages/traits/physiology/trichocyst_discharge.html
    sha256: 2b04dc2be4e8207d49bca42c54ef2097e0988f0bd7577b7bf698db40efc33d51
    role: context
  - path: pages/traits/physiology/tripolar_mating_system.html
    sha256: 90bdb9e237db8d1ed3c518d325f54f97d9f3b2f39c76cb3459ab3e96d971e032
    role: context
  - path: pages/traits/physiology/trogocytosis.html
    sha256: 56ab2ba519a307ebd21102ef6726168079dd08bbdd63d3cdc572d84b688010aa
    role: context
  - path: pages/traits/physiology/trophic_type.html
    sha256: 3501d687300287ca6a6edede57bd117fed559147a60cd2b51334456fa6627792
    role: context
  - path: pages/traits/physiology/trypsin_activity.html
    sha256: 5f6a4c61bdb5a129cb43ea9682cdd1276d91b8ed4b59d34660b40d35300ecfbe
    role: context
  - path: pages/traits/physiology/tyrosine_arylamidase_activity.html
    sha256: 635918a347d1acd4f85f272e5a97e8b0f98246d422eaa582a9121a715dff4911
    role: context
  - path: pages/traits/physiology/unconventional_protein_secretion.html
    sha256: 051a4b2ede7a8b3c03f8e33c41acad5361d44b8f110f4f6334f320d833ff7a21
    role: context
  - path: pages/traits/physiology/unequal_protein_aggregate_inheritance.html
    sha256: e303cbd8b75e65e65e09b0338f217ec02e18a2a7ae4329e4960246a65fbe698c
    role: context
  - path: pages/traits/physiology/unisexual_reproduction.html
    sha256: 721cf9b227ad647899522dfe3cd7f870534b9bee49a4e47484710845ed1a4651
    role: context
  - path: pages/traits/physiology/urease_activity.html
    sha256: a077d2e595bd011e62f267f556c89eb8db83d9458db925450488b918b0269486
    role: context
  - path: pages/traits/physiology/valine_arylamidase_activity.html
    sha256: 6d5b2dd3d527b12c4eef7b0083fee77455b0a61481a308b1ed17f5512cd7732b
    role: context
  - path: pages/traits/physiology/viable_but_nonculturable_state.html
    sha256: 2746442a5a1b2aa1aa359e7767a54aefa0f434a0ecd49744324f413b75481313
    role: context
  - path: pages/traits/physiology/viscotaxis.html
    sha256: fc08d8c1a04754227c09fa70628dc383bf912d61a866b749326f164f37130a7c
    role: context
  - path: pages/traits/quantitative_property/has_maximum_observed_value.html
    sha256: dccb0eaff16daeaae7c75c439b03a803830bbc1923746a6a7e0020f2f8335cf1
    role: context
  - path: pages/traits/quantitative_property/has_minimum_observed_value.html
    sha256: ba7087f6d8cee78b92d26885e24f8c9c15f1c1ded7fc96e07c21d23627d8ce81
    role: context
  - path: pages/traits/quantitative_property/has_observed_spot_value.html
    sha256: 7ffdb2eb485d644cc952c77b9ab1129a08d2f0449a762496e224ab2c8a5332c8
    role: context
  - path: pages/traits/quantitative_property/has_value.html
    sha256: bd5a33492466d213c9953d9e845e5ed96a47b11cee96b05da325837d876500eb
    role: context
  - path: pages/traits/quantitative_property/has_value_comments.html
    sha256: 4f286305e390b7f82fe8d04de544509065e69c379e4e0e37d06678334637fef6
    role: context
  - path: pages/traits/quantitative_property/is_negative_data.html
    sha256: 36317816521a80951c840d6b64f496ff55afc5f3bd04245e6c85ae0f357afe54
    role: context
  - path: pages/traits/quantitative_property/observation_data_property.html
    sha256: 20700bb8abf2700a1f437878fdf149059a6bab215e7033d0429d77b4bd5a9a97
    role: context
  - path: pages/traits/upper/biological_process.html
    sha256: 1b7fb13fedca7e80f8793332dae11567473628728179dd7f44af486d7f405130
    role: context
  - path: pages/traits/upper/chemical_entity.html
    sha256: 19b55171c48112b639e152195f7433ad14e158879ea281be897284b30fe13dff
    role: context
  - path: pages/traits/upper/enzyme.html
    sha256: 299a5bb89bd06f6797c9e2621d2345c96e18368fe0b14fd1cdc0070b37b77317
    role: context
  - path: pages/traits/upper/material_entity.html
    sha256: 5f585ab37fde5ccb754c56f96720f4695cfd7a83380b035b483a08616bf81563
    role: context
  - path: pages/traits/upper/microbe.html
    sha256: f42728d95c4def0fb47f1179f40da8a5c88356f4179f6b6eb1bab4550392fae0
    role: context
  - path: pages/traits/upper/observation.html
    sha256: 8d21f7523f543466360feef1e829d42161508c62b5662db62783de26028957cd
    role: context
  - path: pages/traits/upper/phenotype.html
    sha256: d7275b4da48291e4e583a4bab35ce8add80e5f65d25f503cebc679eabe4c3ad4
    role: context
  - path: pages/traits/upper/quality.html
    sha256: 44d4150cbb94c3ef6bc58beb76f845693a3feda9433216db739c2ac5030d420f
    role: context
  - path: pages/umap.html
    sha256: 4c885866fdb6062491da7f89e17d5ee677310d8b95b606b931a9b242140f9901
    role: context
  - path: proposals/metpo_traitmech_v595/metpo_proposal_classes_robot.tsv
    sha256: 772aa3a8e6f11cf589e6a96870f256d571f6c47d39c64d60b0c402e2537d309b
    role: context
  - path: proposals/metpo_traitmech_v595/proposal.md
    sha256: 2cdd6f7e7c5453c6f5acc8641ed73eb3e091cbf9da987095b47100b469b4d971
    role: context
  - path: reports/proposal_citation_audit.tsv
    sha256: 527b77694dadb55f775572448bfbff0ac2c7e18e41590c8ce74d8850b41c7baa
    role: context
  - path: reports/robot/metpo_traitmech_v595/classes.owl
    sha256: 0c66ef91a16fa2fe381c0e6085665c409a03b1f3d2507eafccbf5f1c9391e26a
    role: context
  - path: reports/robot/metpo_traitmech_v595/merged.owl
    sha256: 0540cbdc977012e7af9599044d57f2d24c40e4653b8fceada929b45bb00fbd8b
    role: context
  - path: reports/robot/metpo_traitmech_v595/reasoned.owl
    sha256: c4ac4f7a8709b8cea9d911af586ee797cbfdd4796b0811ec99072069cc0297ff
    role: context
  - path: research/traits/ecology/fungal_nematophagy-source-verification.json
    sha256: 2272fc26a35846eb25fe5f15ec6e3f155e63fcab279ac9b63c19b112e3753ff5
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/add_fungal_nematophagy_trait.py
    sha256: 25d795459263fc08b7e8dcc2169056c7af0c5d86dc530638f9d7b69676608711
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
  - path: tests/test_add_fungal_nematophagy_trait.py
    sha256: 86eae0fc4be009ceca1950ce085fdc7440be30296c5c366af74683aa5e689016
    role: context
targets:
- target_id: traitmech:000719
  path: data/traits/ecology/fungal_nematophagy.yaml
  label: fungal nematophagy
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/ecology/fungal_nematophagy.yaml
    role: maintained record
  - repository: CultureBotAI/TraitMech
    path: scripts/add_fungal_nematophagy_trait.py
    role: guarded curation writer
scope:
  description: Entire one-record change and maintained/generated owners, not whole-corpus
    scientific review.
  selection: One exact newly authored trait; no sampling.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - traitmech:000719
  exclusions:
  - target: Other 1113 TraitRecords
    reason: Novelty context, deterministic checks and byte preservation only.
  - target: data/traits/physiology/spore_germination.yaml
    reason: Protected and byte-preserved.
checks:
- check_id: focused-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q tests/test_add_fungal_nematophagy_trait.py tests/test_readme_artifacts.py
    tests/test_trait_priority.py tests/test_qc_dashboard_artifacts.py
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q tests/test_add_fungal_nematophagy_trait.py tests/test_readme_artifacts.py
    tests/test_trait_priority.py tests/test_qc_dashboard_artifacts.py
  status: passed
  required: true
  target_ids:
  - traitmech:000719
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; corpus diagnostics are not whole-corpus
    scientific review.
- check_id: focused-1
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/ruff
    check src scripts tests
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/ruff
    check src scripts tests
  status: passed
  required: true
  target_ids:
  - traitmech:000719
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; corpus diagnostics are not whole-corpus
    scientific review.
- check_id: generate-0
  name: just audit-proposals
  command: just audit-proposals
  status: passed
  required: true
  target_ids:
  - traitmech:000719
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; corpus diagnostics are not whole-corpus
    scientific review.
- check_id: generate-1
  name: just ground-predicates
  command: just ground-predicates
  status: passed
  required: true
  target_ids:
  - traitmech:000719
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; corpus diagnostics are not whole-corpus
    scientific review.
- check_id: generate-2
  name: just ground-nodes
  command: just ground-nodes
  status: passed
  required: true
  target_ids:
  - traitmech:000719
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; corpus diagnostics are not whole-corpus
    scientific review.
- check_id: generate-3
  name: just audit-graphs
  command: just audit-graphs
  status: passed
  required: true
  target_ids:
  - traitmech:000719
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; corpus diagnostics are not whole-corpus
    scientific review.
- check_id: generate-4
  name: just audit-graph-protein-taxa
  command: just audit-graph-protein-taxa
  status: passed
  required: true
  target_ids:
  - traitmech:000719
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; corpus diagnostics are not whole-corpus
    scientific review.
- check_id: generate-5
  name: just audit-predicate-domains
  command: just audit-predicate-domains
  status: passed
  required: true
  target_ids:
  - traitmech:000719
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; corpus diagnostics are not whole-corpus
    scientific review.
- check_id: generate-6
  name: just check-biolink-coverage
  command: just check-biolink-coverage
  status: passed
  required: true
  target_ids:
  - traitmech:000719
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; corpus diagnostics are not whole-corpus
    scientific review.
- check_id: generate-7
  name: just audit-snippets
  command: just audit-snippets
  status: passed
  required: true
  target_ids:
  - traitmech:000719
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; corpus diagnostics are not whole-corpus
    scientific review.
- check_id: generate-8
  name: just gen-discussions-data
  command: just gen-discussions-data
  status: passed
  required: true
  target_ids:
  - traitmech:000719
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; corpus diagnostics are not whole-corpus
    scientific review.
- check_id: generate-9
  name: just gen-qc-dashboard
  command: just gen-qc-dashboard
  status: passed
  required: true
  target_ids:
  - traitmech:000719
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; corpus diagnostics are not whole-corpus
    scientific review.
- check_id: generate-10
  name: just gen-pages
  command: just gen-pages
  status: passed
  required: true
  target_ids:
  - traitmech:000719
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; corpus diagnostics are not whole-corpus
    scientific review.
- check_id: generate-11
  name: just gen-priority-dashboard
  command: just gen-priority-dashboard
  status: passed
  required: true
  target_ids:
  - traitmech:000719
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; corpus diagnostics are not whole-corpus
    scientific review.
- check_id: verify-0
  name: just qc
  command: just qc
  status: passed
  required: true
  target_ids:
  - traitmech:000719
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; corpus diagnostics are not whole-corpus
    scientific review.
- check_id: verify-1
  name: just validate-history
  command: just validate-history
  status: passed
  required: true
  target_ids:
  - traitmech:000719
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; corpus diagnostics are not whole-corpus
    scientific review.
- check_id: verify-2
  name: just validate-products
  command: just validate-products
  status: passed
  required: true
  target_ids:
  - traitmech:000719
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; corpus diagnostics are not whole-corpus
    scientific review.
- check_id: verify-3
  name: just verify-proposal metpo_traitmech_v595
  command: just verify-proposal metpo_traitmech_v595
  status: passed
  required: true
  target_ids:
  - traitmech:000719
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; corpus diagnostics are not whole-corpus
    scientific review.
- check_id: verify-4
  name: just robot-validate-proposal metpo_traitmech_v595
  command: just robot-validate-proposal metpo_traitmech_v595
  status: passed
  required: true
  target_ids:
  - traitmech:000719
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; corpus diagnostics are not whole-corpus
    scientific review.
- check_id: verify-5
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/audit_canonical_examples.py --no-resolve
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/audit_canonical_examples.py --no-resolve
  status: passed
  required: true
  target_ids:
  - traitmech:000719
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; corpus diagnostics are not whole-corpus
    scientific review.
- check_id: verify-6
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/run_trait_graph_audit.py --verify
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/run_trait_graph_audit.py --verify
  status: passed
  required: true
  target_ids:
  - traitmech:000719
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; corpus diagnostics are not whole-corpus
    scientific review.
- check_id: verify-7
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/audit_history_records.py --base e0f3176847fe446a5af3322fe6d0864c03db42d2
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/audit_history_records.py --base e0f3176847fe446a5af3322fe6d0864c03db42d2
  status: passed
  required: true
  target_ids:
  - traitmech:000719
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; corpus diagnostics are not whole-corpus
    scientific review.
- check_id: tests-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q --junitxml=/tmp/traitmech-nematophagy-checks-20261013/pytest.xml
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q --junitxml=/tmp/traitmech-nematophagy-checks-20261013/pytest.xml
  status: passed
  required: true
  target_ids:
  - traitmech:000719
  exit_code: 0
  expected_exit_code: 0
  summary: 4534 tests passed without failures, errors or skips.
- check_id: schema
  name: schema
  command: PYTHONPATH=src .venv/bin/linkml-validate -s src/traitmech/schema/traitmech.yaml
    --target-class TraitRecord data/traits/ecology/fungal_nematophagy.yaml
  status: passed
  required: true
  target_ids:
  - traitmech:000719
  exit_code: 0
  expected_exit_code: 0
  summary: Direct LinkML record validation passed.
- check_id: strict
  name: strict
  command: PYTHONPATH=src .venv/bin/python scripts/validate_strict.py data/traits/ecology/fungal_nematophagy.yaml
  status: passed
  required: true
  target_ids:
  - traitmech:000719
  exit_code: 0
  expected_exit_code: 0
  summary: Direct closed-schema record validation passed.
- check_id: snippets
  name: snippets
  command: PYTHONPATH=src .venv/bin/python scripts/verify_snippets.py --record data/traits/ecology/fungal_nematophagy.yaml
    --out /tmp/traitmech-nematophagy-native-record-20261013.tsv
  status: passed
  required: true
  target_ids:
  - traitmech:000719
  exit_code: 0
  expected_exit_code: 0
  summary: 'Native result: two UNRESOLVED and one NOT_IN_ABSTRACT; URL evidence not
    run. All four excerpts separately matched directly inspected original sources,
    not relabeled VERIFIED.'
- check_id: taxonomy
  name: taxonomy
  command: PYTHONPATH=src .venv/bin/python scripts/audit_canonical_examples.py --ncbi-api
  status: passed
  required: true
  target_ids:
  - traitmech:000719
  exit_code: 0
  expected_exit_code: 0
  summary: 762 canonical examples resolved, zero errors, 24 existing label warnings
    outside the new record. Pleurotus ostreatus 5322 agrees with NCBI; this does not
    independently identify the experimental isolate.
- check_id: products
  name: products
  command: PYTHONPATH=src .venv/bin/python /tmp/traitmech-nematophagy-products-20261013.py
  status: passed
  required: true
  target_ids:
  - traitmech:000719
  exit_code: 0
  expected_exit_code: 0
  summary: All 1113 previous records and prior history/reviews/proposals/embeddings/templates/snippet
    baseline byte-preserved. Existing pages are footer-only except the phenotype child
    link. Parent priority child count changes 196 to 197. Parsed RDF retains exact
    w3id identifiers and parent/grandparent.
- check_id: browser
  name: browser
  command: node /tmp/traitmech-nematophagy-browser-20261013.cjs
  status: passed
  required: true
  target_ids:
  - traitmech:000719
  exit_code: 0
  expected_exit_code: 0
  summary: '1440/390 px checks pass: four excerpts, three discussions, one history,
    local identifier, example, hierarchy and browse navigation, dashboard 1114 and
    loaded coverage image. Eight screenshots visually inspected. No horizontal overflow
    or page errors.'
evidence:
- evidence_id: source-0
  kind: authority
  reference: DOI:10.3390/f10050404
  locator: Introduction, PDF page 1
  accessed_at: '2026-10-13T16:04:05Z'
  support: supports
  snapshot_sha256: e16280002fd201d488efc030089c02e1bf942d456451ffef75d4e2dd26edbcd4
  summary: 'Marlin et al. 2019, Introduction, PDF page 1: directly read terminology,
    not an independent experiment. The fungal actor qualifies the term; consumption,
    not paralysis alone, defines the endpoint. Publisher PDF visually checked. Native
    DOI abstract verifier: UNRESOLVED, retained separately from the direct match.
    Crossref and USDA identify the same DOI/title.'
- evidence_id: source-1
  kind: primary_source
  reference: DOI:10.3390/f10050404
  locator: Figure 2a caption, PDF page 6
  accessed_at: '2026-10-13T16:04:05Z'
  support: supports
  snapshot_sha256: e16280002fd201d488efc030089c02e1bf942d456451ffef75d4e2dd26edbcd4
  summary: 'Figure 2a caption, actual PDF page 6 and panel inspected, with Methods
    2.1-2.3 and Results 3.2. This is a source-named feeding observation, not measured
    nutrient flux. Native verifier: UNRESOLVED. Host susceptibility is differential;
    neither all nematodes nor all Pleurotus isolates are asserted. The two excerpts
    from this paper total 17 words.'
- evidence_id: source-2
  kind: primary_source
  reference: https://horizon.documentation.ird.fr/exl-doc/pleins_textes/fan/40780.pdf
  locator: Summary, PDF page 1
  accessed_at: '2026-10-13T16:04:05Z'
  support: supports
  snapshot_sha256: 01d264b0095706d95726c2c5067e0a1fde95b092b115ea7d68378e22d83ef42b
  summary: den Belder and Jansen 1994, Summary, PDF page 1, directly and visually
    matched. Selected Methods, Results and Discussion, including actual pages 6-8,
    describe Arthrobotrys oligospora CBS 289.82 feeding on living and previously killed
    Meloidogyne hapla juveniles. Internal hyphal occupancy is not a tracer assimilation
    assay. The excerpt supports nonexclusive feeding modes, not an exact rate. URL
    evidence is not run by the native DOI/PMID abstract verifier.
- evidence_id: source-3
  kind: primary_source
  reference: DOI:10.1371/journal.pbio.3002400
  locator: Results, Late time point induced protease and its potential role in digesting
    nematodes
  accessed_at: '2026-10-13T16:04:05Z'
  support: supports
  snapshot_sha256: b3248b3dd4be8c3aa405882d0d530c28964bccee3156a2c48862be34fa5e1eee
  summary: 'Lin et al. 2023, PMID:37988381; Results subsection on late-time protease
    induction, publisher XML sec018. Native verifier: NOT_IN_ABSTRACT; exact full-text
    match. Actual Figure 5, Table 1 and S7 inspected. GFP-labeled reference TWF3407
    is engineered, not an unmodified natural exemplar. Protease inhibition delays
    internal growth at 12 h without proving complete feeding loss or quantifying assimilation.
    Remaining figures and raw S1 spreadsheet were not fully audited.'
- evidence_id: content
  kind: record_content
  reference: data/traits/ecology/fungal_nematophagy.yaml
  locator: Entire new record, writer, tests, sidecar, proposal, history and generated
    diff.
  accessed_at: '2026-10-13T16:04:05Z'
  support: supports
  summary: One fungal feeding phenotype. Neither nematode trapping, toxicity, sequence
    annotation, taxonomic membership nor mere hyphal contact substitutes for feeding.
    Four excerpts are three sources, not four independent studies.
- evidence_id: scope
  kind: primary_source
  reference: https://horizon.documentation.ird.fr/exl-doc/pleins_textes/fan/40780.pdf
  locator: Selected Methods/Results/Discussion; actual PDF pages 1, 6, 7, 8.
  accessed_at: '2026-10-13T16:04:05Z'
  support: supports
  summary: Direct observations include live and previously killed juveniles. This
    challenges a compulsory-killing or strict starvation definition; it does not establish
    nutrient flux, universal host range or a single molecular mechanism. Disputed
    rates and caption/table directions remain excluded.
- evidence_id: taxonomy
  kind: database
  reference: NCBITaxon:5322
  locator: NCBI EFetch top-level species record; Marlin Methods 2.1-2.3 and Figure
    2a.
  accessed_at: '2026-10-13T16:04:05Z'
  support: supports
  summary: Authority label agrees with Pleurotus ostreatus. The example is limited
    to an unnamed grocery-store mushroom isolate with morphological identification.
    No deposit, genotype or unmodified natural laboratory strain is invented. Lin
    GFP imaging strains are explicitly engineered and not canonical examples.
- evidence_id: ontology
  kind: database
  reference: data/raw/metpo.owl
  locator: Pinned/current RDF, editor metadata shell, upstream template screening
    and live neighboring definitions.
  accessed_at: '2026-10-13T16:04:05Z'
  support: supports
  summary: Phenotype is a true broader parent. Deprecated trophic terms replace to
    a broader carbon/energy axis, not an exact feeding term; fungal-spore and parasitism
    hits are not exact. Trap morphology and other uptake modes are not is-a parents.
    No historical identifier reuse or unverified exact xref.
- evidence_id: novelty
  kind: search
  reference: research/traits/ecology/fungal_nematophagy-source-verification.json
  locator: Ignored/hidden local files, positive-controlled retained heads, full pending
    changed blobs and selected upstream owners.
  accessed_at: '2026-10-13T16:04:05Z'
  support: supports
  summary: No exact feeding record/proposal or same-scope unresolved node/synonym
    needing migration found within recorded bounds. Canonical local matches are trap
    morphology, autophagy and myzocytosis; CommunityMech matches are bacterial host/biocontrol/taxonomy
    contexts. KG-Microbe matches concern taxonomy, isolation source and life stage.
  search_scope: 'Available ignored/hidden files included; no unavailable ignored/untracked
    reconstruction, symlink following or local archive decoding. This is not atomic
    allocation. Initial screen: 170 locations, 139 retained heads, 11 open/draft PRs,
    783 pending blobs and 587 selected upstream blobs.'
- evidence_id: status
  kind: authority
  reference: research/traits/ecology/fungal_nematophagy-source-verification.json
  locator: Crossref DOI records, PubMed linked-update metadata, directly read PLOS
    publisher pages; recorded MDPI access failure.
  accessed_at: '2026-10-13T16:04:05Z'
  support: supports
  summary: The linked PLOS 2025 Update Article adds research, not a correction or
    independent-laboratory replication. Crossref metadata does not expose a linked
    notice in retrieved records; MDPI status-page 403 and limited IRD metadata preclude
    exhaustive notice clearance.
- evidence_id: products
  kind: validation
  reference: reports/proposal_citation_audit.tsv
  locator: Maintained gates, full tests, generated diffs, current counts, RDF and
    browser checks.
  accessed_at: '2026-10-13T16:04:05Z'
  support: supports
  summary: 'All required local gates pass. Parsed RDF graph sizes are {''classes'':
    15, ''merged'': 12628, ''reasoned'': 12632}. Shared generator matches 645 source
    blobs; exact configured embedding inputs absent, so existing embeddings retained.
    Only inspected ROBOT TSV header trailing tabs receive a path-scoped whitespace
    exception.'
- evidence_id: history
  kind: record_content
  reference: history/records/fungal_nematophagy
  locator: CREATE event and LLM-assisted per-record minting event.
  accessed_at: '2026-10-13T16:04:05Z'
  support: supports
  summary: Observed acceptance time is distinguished from write time. Sections identity,
    evidence, canonical_examples and discussions match the actual change. Actor codex,
    model gpt-5, tool codex; no human sign-off or REVIEWED promotion.
- evidence_id: publication
  kind: search
  reference: /tmp/traitmech-nematophagy-publication-20261013/accepted.json
  locator: Refreshed ignored/hidden local searches and live pending/upstream Git identities.
  accessed_at: '2026-10-13T16:04:05Z'
  support: supports
  snapshot_sha256: 79f2ba86093f9aca67aafd0bf88599de0d70df8b5ac198c44f73eefe312b41bd
  summary: 171 locations rechecked; owned additions separated from competing allocations.
    All remote heads unchanged; prior full blobs retain their identities. No competing
    reservation found. Historical heads unchanged; package sizes and broad editor
    envelopes remain nonreservations.
  search_scope: Available ignored/hidden files included; no unavailable ignored/untracked
    reconstruction, symlink following or local archive decoding. This is not atomic
    allocation.
assessments:
- assessment_id: identity
  area: identity
  topic: Fungal feeding, not capture morphology
  summary: The definition requires fungal consumption of nematodes as food. A living-prey
    attack or specific capture apparatus is not imposed; paralysis alone remains insufficient.
    Fungal qualification avoids nonfungal actors.
  target_ids:
  - traitmech:000719
  evidence_ids:
  - content
  - source-0
  - source-1
  - scope
  outcome: supported
- assessment_id: evidence
  area: evidence
  topic: Direct feeding observations and assay limits
  summary: Consumption observations and source-defined internal digestion support
    the scoped phenotype. Hyphal occupancy is not quantified assimilation; no universal
    host range, exclusive nutrition or complete inhibitor-induced loss is claimed.
  target_ids:
  - traitmech:000719
  evidence_ids:
  - source-1
  - source-2
  - source-3
  - scope
  outcome: supported
- assessment_id: provenance
  area: provenance
  topic: Contiguous source spans and actual resolver outcomes
  summary: Four self-contained excerpts directly match original retrieved sources.
    Two quotes from Marlin are one study; native unresolved/full-text verdicts and
    URL exclusion are retained. A later Update Article is not a correction.
  target_ids:
  - traitmech:000719
  evidence_ids:
  - source-0
  - source-1
  - source-2
  - source-3
  - status
  outcome: supported
- assessment_id: grounding
  area: grounding
  topic: Hierarchy, taxonomy and reservation
  summary: Phenotype is broader; carbon-specific trophic axes and trap morphologies
    are not asserted as parents. Deprecated terms are not reused. The example is source-qualified
    and taxon-authority checked. Ignored/hidden and live pending-head refreshes support
    bounded novelty/allocation.
  target_ids:
  - traitmech:000719
  evidence_ids:
  - ontology
  - taxonomy
  - novelty
  - publication
  - content
  outcome: supported
- assessment_id: products
  area: consistency
  topic: Validated writes and faithful derived outputs
  summary: Guarded dry-run, replay/drift tests, full QC/test suite, history, proposal,
    RDF and browser checks pass. Existing records and immutable provenance are byte-preserved.
    Current counts agree across README and dashboards.
  target_ids:
  - traitmech:000719
  evidence_ids:
  - products
  - history
  - content
  outcome: supported
- assessment_id: limits
  area: completeness
  topic: Explicit scientific uncertainties
  summary: Source table/caption/gene-name inconsistencies, partial figure/supplement
    access, morphology-only isolate identification and bounded notice checks remain
    explicit. They do not negate the modest feeding phenotype; no causal graph or
    exact molecular assignment is invented.
  target_ids:
  - traitmech:000719
  evidence_ids:
  - content
  - source-1
  - source-2
  - source-3
  - status
  outcome: unknown
findings: []
actions: []
limitations:
- Author self-review. Exact-head external review, CI and merge-queue/integrity checks
  are separate gates, not claimed complete here.
- Selected actual PDF pages, Figure 5, Table 1 and S7 were inspected, not every figure/supplement
  or raw S1 data. Conflicting host ranges, numerical rates and mep1/mcp1 identities
  are not reconciled by assertion.
- Internal hyphal growth is not quantitative nutrient flux. Isotope measurements are
  not required to recognize feeding, but no carbon/nitrogen contribution or universal
  mechanism is inferred.
- The Pleurotus example is an unnamed morphology-identified grocery-store culture,
  not a deposited or molecularly authenticated strain. NCBI validates the taxon name,
  not the specimen identity.
- Two native snippet rows are UNRESOLVED and one NOT_IN_ABSTRACT; URL evidence is
  not run by that verifier. Direct matching is reported separately. Notice checks
  are bounded, including MDPI 403.
- Ignored/hidden available files were searched; lost ignored/untracked history, symlink
  directories, local archives and unchanged pending-tree files are not reconstructed.
  Discovery is not exhausted.
- Configured embedding sources are absent; existing embedding artifacts, shared templates
  and frozen baselines remain unchanged.
tags:
- add-trait
- fungal-nematophagy
- self-review
```
