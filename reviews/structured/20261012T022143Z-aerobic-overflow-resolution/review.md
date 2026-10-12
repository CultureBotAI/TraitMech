# Aerobic overflow final reassessment and snippet-finding resolution

- Review: 20261012T022143Z-aerobic-overflow-resolution
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-12T02:06:35Z
- Finished UTC: 2026-10-12T02:21:43Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Full one-record author reassessment after external review: the corrected yeast snippet states a positive ethanol result, with oxygen and study qualifiers retained. Finding #1883 is resolved through an exact predecessor link; the earlier pass and finding remain immutable. No open actionable finding in this scope. Human signoff and upstream mapping remain outstanding.

## Scope And Provenance

Complete new aerobic-overflow record, writer/tests, proposal, history, README and directly generated artifacts. Includes the #1883 correction and add-trait evidence guidance.

Selection: One exact record; no sampling.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 45af1ddbf5093ca33145158bd5ae79101ae885ea.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| traitmech:000705 | data/traits/physiology/aerobic_overflow_metabolism.yaml | maintained | aerobic overflow metabolism |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| .venv/bin/linkml-validate -s src/traitmech/schema/traitmech.yaml --target-class TraitRecord data/traits/physiology/aerobic_overflow_metabolism.yaml | passed | True | traitmech:000705 | Rerun for the corrected record; native corpus checks are not whole-corpus scientific review. |
| .venv/bin/python scripts/validate_strict.py data/traits/physiology/aerobic_overflow_metabolism.yaml | passed | True | traitmech:000705 | Rerun for the corrected record; native corpus checks are not whole-corpus scientific review. |
| .venv/bin/python scripts/verify_snippets.py --record data/traits/physiology/aerobic_overflow_metabolism.yaml --out /tmp/traitmech-overflow-1883-checks-20261012/snippet-results.tsv | passed | True | traitmech:000705 | One scientific-abstract match VERIFIED (Basan); two body quotes NOT_IN_ABSTRACT (Molenaar, Hagman), directly checked in retrieved primary XML. Native outcomes retained. |
| just audit-snippets | passed | True | traitmech:000705 | Rerun for the corrected record; native corpus checks are not whole-corpus scientific review. |
| just gen-qc-dashboard | passed | True | traitmech:000705 | Rerun for the corrected record; native corpus checks are not whole-corpus scientific review. |
| just gen-pages | passed | True | traitmech:000705 | Rerun for the corrected record; native corpus checks are not whole-corpus scientific review. |
| just gen-priority-dashboard | passed | True | traitmech:000705 | Rerun for the corrected record; native corpus checks are not whole-corpus scientific review. |
| .venv/bin/python -m pytest -q tests/test_add_aerobic_overflow_trait.py | passed | True | traitmech:000705 | 22 guarded-writer tests passed, including one- and two-event preimage upgrades and unchanged prior evidence/history. |
| just qc | passed | True | traitmech:000705 | Full QC passed on the committed correction, including derived freshness; two existing ENIGMA licensing warnings remain. |
| just validate-history | passed | True | traitmech:000705 | Rerun for the corrected record; native corpus checks are not whole-corpus scientific review. |
| just validate-products | passed | True | traitmech:000705 | 361 canonical labels, two synonyms and one accepted exception; 123 existing SKIPPED_NO_ADAPTER rows. No new chemical or protein/taxon example. |
| just verify-proposal metpo_traitmech_v581 | passed | True | traitmech:000705 | Rerun for the corrected record; native corpus checks are not whole-corpus scientific review. |
| just robot-validate-proposal metpo_traitmech_v581 | passed | True | traitmech:000705 | Rerun for the corrected record; native corpus checks are not whole-corpus scientific review. |
| .venv/bin/ruff check src scripts tests | passed | True | traitmech:000705 | Rerun for the corrected record; native corpus checks are not whole-corpus scientific review. |
| .venv/bin/python -m pytest -q --junitxml=/tmp/traitmech-overflow-1883-checks-20261012/pytest.xml | passed | True | traitmech:000705 | 4099 tests passed; no failures, errors or skips. |
| .venv/bin/python scripts/validate_history_links.py history/records/aerobic_overflow_metabolism | passed | True | traitmech:000705 | Rerun for the corrected record; native corpus checks are not whole-corpus scientific review. |
| .venv/bin/linkml-validate --schema src/traitmech/schema/history.yaml --target-class HistoryRecord history/records/aerobic_overflow_metabolism/2026-10-12T010648Z-codex-c4f5f8.yaml | passed | True | traitmech:000705 | Rerun for the corrected record; native corpus checks are not whole-corpus scientific review. |
| .venv/bin/linkml-validate --schema src/traitmech/schema/history.yaml --target-class HistoryRecord history/records/aerobic_overflow_metabolism/2026-10-12T010851Z-codex-43a225.yaml | passed | True | traitmech:000705 | Rerun for the corrected record; native corpus checks are not whole-corpus scientific review. |
| .venv/bin/linkml-validate --schema src/traitmech/schema/history.yaml --target-class HistoryRecord history/records/aerobic_overflow_metabolism/2026-10-12T015455Z-codex-b0453d.yaml | passed | True | traitmech:000705 | Rerun for the corrected record; native corpus checks are not whole-corpus scientific review. |
| .venv/bin/python scripts/audit_canonical_examples.py --no-resolve | passed | True | traitmech:000705 | 761 examples across 576 records, zero shape errors/warnings; authority resolution not run because no examples changed. |
| .venv/bin/python scripts/run_trait_graph_audit.py --verify | passed | True | traitmech:000705 | Research-artifact integrity only; acquisition counts are not scientific review counts. |
| .venv/bin/python scripts/audit_history_records.py --base 8abebd0652f3de39d8de1d86a246cfe768df7bcc | passed | True | traitmech:000705 | Rerun for the corrected record; native corpus checks are not whole-corpus scientific review. |
| git diff --check 8abebd0652f3de39d8de1d86a246cfe768df7bcc HEAD -- . ':(exclude)proposals/metpo_traitmech_v581/metpo_proposal_classes_robot.tsv' | passed | True | traitmech:000705 | Rerun for the corrected record; native corpus checks are not whole-corpus scientific review. |
| git -c core.whitespace=-blank-at-eol diff --check 8abebd0652f3de39d8de1d86a246cfe768df7bcc HEAD -- proposals/metpo_traitmech_v581/metpo_proposal_classes_robot.tsv | passed | True | traitmech:000705 | Rerun for the corrected record; native corpus checks are not whole-corpus scientific review. |
| Manual claim support and direct source verification | passed | True | traitmech:000705 | Exact 18-word positive Results span, correct section locator and oxygen-control context verified. Molenaar body sentence and surrounding definition paragraph confirmed. |
| Desktop/mobile Playwright and visual inspection | passed | True | traitmech:000705 | 1440px and 390px: corrected third quote, three history links, browse/parent navigation, loaded coverage image, no horizontal overflow or page errors. Six screenshots visually inspected. Sandbox launch failed before navigation; approved retry passed. |
| Embedding applicability | not_applicable | False | traitmech:000705 | Exact configured sources absent; existing artifacts retained, not regenerated. |

## Scientific And Domain Assessments

### Conditional aerobic phenotype

identity: supported. Targets: traitmech:000705.

Organism-level physiological disposition, not a gene or universal pathway. The aerobic qualifier restricts broader overflow terminology.

### Oxygen and yield scope

identity: supported. Targets: traitmech:000705.

Sufficient oxygen and respiratory capacity distinguish the trait from oxygen limitation. No universal product, substrate, concentration or growth threshold is imposed.

### Bounded novelty and allocation

identity: supported. Targets: traitmech:000705.

No exact inspected match or occupied full block; prior butanediol evidence and research leads do not denote the same record.

### Phenotype parent

grounding: supported. Targets: traitmech:000705.

Process-shaped metabolism and donor/acceptor-defined fermentation are not treated as broader organismal traits. Frozen local/pinned differences and upstream issue468 are explicit. RDF has actual w3id phenotype-to-quality hierarchy.

### Exact section-qualified evidence

evidence: supported. Targets: traitmech:000705.

Three contiguous primary-source quotes: one scientific-abstract match and two directly confirmed body spans. Hagman now states the positive ethanol result; oxygen-control context is in notes. Molenaar access concern resolved by exact source location and publicly retrievable XML, not by changing its resolver verdict.

### Guarded writer and correction

provenance: supported. Targets: traitmech:000705.

Guarded dry run, exact one- and two-event preimages, parent/proposal drift rejection, prevalidation and replay are tested. Both corrections append history; all prior review bundles remain byte-preserved. No mapping-status promotion.

### Preservation and generated artifacts

consistency: supported. Targets: traitmech:000705.

Required gates and full tests pass. Counts, proposal width, RDF and browser views agree; unrelated records unchanged.

### Examples and mechanism deferred

completeness: unknown. Targets: traitmech:000705.

No natural canonical taxa, universal protein mechanism or exact external equivalence asserted without necessary evidence; upstream acceptance remains open.

## Findings

### yeast-snippet-support: Yeast snippet does not state the supporting phenotype result

minor / resolved / confirmed; issue key: github-1883-yeast-overflow-snippet.

The prior quotation was verbatim but only described data generation. The source supported the trait in other passages; this was a bounded snippet-selection defect, not a wrong citation or invalid trait. The current quotation states the positive result.

Disposition: The current exact 18-word Results quote reports significant ethanol formation after a glucose pulse. Its section and oxygen-controlled assay context were directly rechecked. Writer upgrade tests, schema, snippet, history, generated products, full suite and browser checks pass. Both previous events and review bundles remain unchanged.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | DOI:10.1038/msb.2009.82; Current growth models and their limitations: exact quoted sentence and full surrounding paragraph reinspected; broader modeling context retained from the earlier full review. | supports | Aerobic incomplete oxidation with retained respiration grounds the qualified phenotype. The quoted body sentence describes S. cerevisiae and E. coli; this original modeling Perspective is not new experimental replication. Its broader mixed-acid-to-lactate usage is not silently equated with the qualified label. |
| bacterial | DOI:10.1038/nature15765; Scientific abstract reinspected; selected Results, Methods, Extended Data Table 1, actual Figure 1 and Extended Data Figure 2 assessed in the earlier full review and unchanged. | supports | Acetate excretion during aerobic E. coli growth supports the phenotype. Proteome-allocation explanation and fitted threshold are system-specific. Oxidative accounting includes NADH oxidation using oxygen; net excretion does not exclude reuptake. Reference and engineered strains are not universal natural canonical examples. Complete supplements/equations and cited batch methods were not independently reanalyzed. |
| yeast | DOI:10.1111/febs.13019; Results and Discussion / Consumption of glucose and generation of biomass and ethanol; Experimental procedures. Actual Figures 1-2 inspected in the earlier full review. | supports | The replacement is an exact 18-word positive ethanol-formation Results span, not a measurement list. Its paragraph distinguishes responsive and nonresponsive tested yeasts. Methods maintain dissolved oxygen above 30% air saturation in initially respiratory, glucose-limited cultures. The respiratory-repression qualifier and replication/supplementation limits remain unchanged. Full supplementary time series and strain origins were not reviewed. |
| notices | https://europepmc.org/article/MED/25161062; Exact DOI Crossref and source-qualified MED metadata for all three citations; accessible publisher pages. | context_only | DOI/PMID/PMC identity and source sections checked. Retrieved metadata exposed no linked correction or retraction; this bounded result is not proof of absence. Basan publisher retrieval failed, while public XML/figure assets were accessible. |
| content | data/traits/physiology/aerobic_overflow_metabolism.yaml; Complete corrected record, full guarded writer and 22 tests, three append-only history records, v581 proposal and skill clarification. | supports | One PROPOSED PHYSIOLOGY class under phenotype. No exact synonyms, xrefs, canonical examples or graph. Two OPEN discussions preserve hierarchy and provenance/mechanism gaps. Oxygen presence or product detection alone is not diagnosis. Fermentation, product-specific traits, aerotolerance, facultative anaerobiosis, copiotrophy and diauxie are distinct axes. |
| correction | https://github.com/CultureBotAI/TraitMech/issues/1881; Corrected yeast evidence notes, CLARIFIED_EVIDENCE_SCOPE event, EDIT history and original-preimage upgrade regression test. | supports | The drafting defect was filed and corrected before this formal inspection. Original CREATE history and curation event remain unchanged. Current text attributes the authors' repression claim without asserting monotonic respiration. This is not a successor disposition of a nonexistent saved review. |
| novelty | proposals/metpo_traitmech_v581/proposal.md; Ignored/hidden searches, structured YAML comparisons, pinned/current ontology and templates, full paginated pending-PR files, fresh reservations. Fresh head/file/ignored-inclusive worktree comparison after correction; owned PR1882 excluded only from foreign-reservation comparisons. | supports | No exact active/deprecated match or overlapping allocation found in declared scope. Reserve local 000705, cohort v581, full METPO1065800-1065899 block; only 1065800 populated. Editable OWL root is imports-only and is not used alone to establish absence. |
| products | reports/proposal_citation_audit.tsv; Native QC/schema/history/products, full and focused tests, parsed RDF, byte comparisons, browser assertions and six visually inspected desktop/mobile screenshots. | supports | Correction gates and full tests passed; 4099 tests. All 1,099 old YAMLs and earlier histories/reviews preserved. 1,098 old pages have footer-only changes; phenotype gains one child. Three curation histories and corrected body snippet render at both widths. Parsed RDF: {'classes': 15, 'merged': 12628, 'reasoned': 12632}. |
| resolution | https://github.com/CultureBotAI/TraitMech/issues/1883; evidence[2], guarded build_record upgrade, new two-event regression, REPLACED_UNSUPPORTIVE_SNIPPET and third repository history; add-trait evidence guidance. | supports | Changed only the unsupportive quote and source locator within evidence; first two evidence entries and both old history events remain unchanged. Native resolver correctly changes Hagman from VERIFIED to NOT_IN_ABSTRACT. The 25-word limit is retained. Skill now requires claim-bearing snippets rather than accepting a methods-only statement. |
| external | https://github.com/CultureBotAI/TraitMech/pull/1882#pullrequestreview-5485934905; Yellow Hagman snippet finding; exact reviewed head c4e64607a1f072a3accd3eeeb8174b380be1c68a. | supports | The external reviewer identifies a real mismatch between measurement-description prose and a trait-supporting snippet. This successor confirms the defect and evaluates its correction, without treating the external request itself as approval of the new head. |

## Limits And Additional Notes

- Author self-review, not independent or human signoff; one complete trait assessed, not every hashed corpus input.
- Current changed record/writer/tests/skill/proposal/history and primary quotation contexts reinspected. Unchanged selected source figures, broader source analysis and novelty findings carry forward from the linked initial review; no new whole-paper or whole-corpus scientific review is claimed.
- Source access times denote inspection, not necessarily download. Molenaar and Hagman remain NOT_IN_ABSTRACT; direct full-text checks do not relabel native outcomes.
- Relevant sections and selected figures only; complete raw data, supplements, equations, strain origins and all cited methods were not reviewed. Basan publisher inaccessible; public full-text XML used.
- Canonical natural examples, protein mechanisms and upstream hierarchy acceptance remain explicit gaps. No authority-resolution claim from the no-resolve example audit.
- Product validation retains 123 existing SKIPPED_NO_ADAPTER rows; two existing ENIGMA licensing warnings remain.
- Ignored/hidden-inclusive novelty scope excludes archives, symlink-directory traversal and unregistered/private work; no global trait-exhaustion claim.
- Neither exact embedding source exists. Required trailing ROBOT directive cells use only the documented exact-path whitespace exception.
- Issue1881 was corrected before initial review; #1883 has an explicit predecessor finding and resolved successor. External approval of the new head and CI/queue admission remain later PR lifecycle gates.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T022143Z-aerobic-overflow-resolution
kind: record
repository: CultureBotAI/TraitMech
title: Aerobic overflow final reassessment and snippet-finding resolution
started_at: '2026-10-12T02:06:35Z'
finished_at: '2026-10-12T02:21:43Z'
reviewer:
  identity: codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Author source-based reassessment and implementation review of
    an external finding; self_review, not independent or human signoff.
skill: .claude/skills/add-trait/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'Full one-record author reassessment after external review: the corrected
  yeast snippet states a positive ethanol result, with oxygen and study qualifiers
  retained. Finding #1883 is resolved through an exact predecessor link; the earlier
  pass and finding remain immutable. No open actionable finding in this scope. Human
  signoff and upstream mapping remain outstanding.'
source:
  git_revision: 45af1ddbf5093ca33145158bd5ae79101ae885ea
  state: working_tree
  inputs:
  - path: .claude/skills/add-trait/SKILL.md
    sha256: 80361db3709fe1f98920d76202314cccfb9e34ae37c6ebe677f2aac069e2ebf6
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
    sha256: d1976cf09b2dccb5fa299306361bbffaa7db4d060c8de68d1cc03edfc32c2bfa
    role: context
  - path: app/dashboard/priority.html
    sha256: d2e4a03b8a8560ce6ca6d22b520653eb0ee10f61c6e5fa5eaa33f5ffeb4b3fdc
    role: context
  - path: app/dashboard/priority.json
    sha256: 4574d3972c76171aa3613b6966f66ccf9808bc6fc16c45b260b2ed476d053679
    role: context
  - path: app/discussions/data.js
    sha256: 21772c5536f761b65fec18ee33cf05446203a8d590902ef369cacf0754443a8f
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
    sha256: 9422deca4d84113760589445b1c253530ac70743c0aad6e2ef5268ae23715a2d
    role: context
  - path: dashboard/index.html
    sha256: 7c598ec34392da5de1d7c15ee88881c88025ec2b43061f2484ad7ca05d70b3bf
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
  - path: data/traits/physiology/aerobic_anoxygenic_phototrophy.yaml
    sha256: 456e996a9c4365b5c088fc57fe4fcc61cb7ec2ba508668cc787cb9fdbb2d3c88
    role: context
  - path: data/traits/physiology/aerobic_overflow_metabolism.yaml
    sha256: d1543a9e0f2efb02c9dcbf46d4828ce88fb26da035fb47d9f00a992cd9cfe5f8
    role: target
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
  - path: history/records/aerobic_overflow_metabolism/2026-10-12T010648Z-codex-c4f5f8.yaml
    sha256: f5990f9c9dd1941ed18aa88f596cda7c6402bae50ca62a6422613033d5e6d20d
    role: context
  - path: history/records/aerobic_overflow_metabolism/2026-10-12T010851Z-codex-43a225.yaml
    sha256: 62d2f1d415d52ef7da5bfddf72da186e92f0a3590921c1d32c75d2e67363a633
    role: context
  - path: history/records/aerobic_overflow_metabolism/2026-10-12T015455Z-codex-b0453d.yaml
    sha256: a520e9fd8d7568598ba887841659f21ad5948742d4e00acd7b52390ed324ee68
    role: context
  - path: justfile
    sha256: e6047ea612115a6a78d100b281483ba824c860c3def59bcd0d40e7fb56b3526a
    role: context
  - path: pages/browse.html
    sha256: d92fb656791ced3890cf67eab7f3ff7ad4a27327aec227c155f711dc27d93c6a
    role: context
  - path: pages/category/ecology.html
    sha256: fa83eeb914d397f6467e3992a5e33e8c0d30d9186a2a4bcb69a2db993ecf8199
    role: context
  - path: pages/category/environment.html
    sha256: f9d9108e102159390a877142d6c311af23453690a9a7416c4009a1242aa88638
    role: context
  - path: pages/category/genomics.html
    sha256: 9f601882c388d9240b95a9843fc9a4193fd5f58b08e4a48c627ec8063e0cb67b
    role: context
  - path: pages/category/metabolism.html
    sha256: 2495da0f5257000f8904663a28185ba3d2f64c8613d572ef7dbd1748e856c12e
    role: context
  - path: pages/category/morphology.html
    sha256: 05096112e507b315efd9f4d2a90f3053e0c531590bba9e98839b7f4e9b5aaf4d
    role: context
  - path: pages/category/observation.html
    sha256: 4b594079071fa8cba6ff7824f5f5e92ec484e2a3b6ef6cbff895d56f8e095bad
    role: context
  - path: pages/category/other.html
    sha256: 0e9b50dd9314edd0239be38dabc7e32f42aa06b8374a6a37d1e309e754e7e4dc
    role: context
  - path: pages/category/physiology.html
    sha256: 5f5739961978cf4a9652dc5f69a1c74c56c41142a82808cdba7c715715956b5a
    role: context
  - path: pages/category/quantitative_property.html
    sha256: 12b5027a2b9d0906be5352955253da67d3fc94973afd124f6e2f3b270b7ca6ec
    role: context
  - path: pages/category/upper.html
    sha256: 918e3be0717661d12f14f5f84b1bab26374c997c325555aa317a9fa0b3f323e0
    role: context
  - path: pages/graph.html
    sha256: 3a4be574956dbc203ca4afbb3a4fa4c790e2138cd4cb3a0cfea4a24d9d99adcb
    role: context
  - path: pages/index.html
    sha256: 974025e4ac292f4e487d82d5692a2fcc9a085d0f4d6abd4d178c076225db676b
    role: context
  - path: pages/traits/ecology/animal_pathogen.html
    sha256: 758e97aa7e8cd88e986d972763483e8b80aea58b93835d91fadebecd75df6e77
    role: context
  - path: pages/traits/ecology/bacterial_cannibalism.html
    sha256: 0b82396d55166247206da88995affe102ed29f78c40f3319ad60cb634f7e01b8
    role: context
  - path: pages/traits/ecology/bacterial_mycophagy.html
    sha256: fecf93ae9175326baa6705f49e8ee3d541e29375b2a319a21caea608b73cf0b8
    role: context
  - path: pages/traits/ecology/biofilm_formation.html
    sha256: 99c68b9408384912fe6b98035d95eb2860d2fe131c10546eb04da6d9ea75363c
    role: context
  - path: pages/traits/ecology/biosafety_level.html
    sha256: 69aece8075206a85e870dd42a897ce5c9ee0ee91cae979a32cf310bc802dfc7a
    role: context
  - path: pages/traits/ecology/biosafety_level_1.html
    sha256: 9786d76738a7ee3c2aea7c73fc933d7720b2022dcfcdfd600bf0dd429bfcac21
    role: context
  - path: pages/traits/ecology/biosafety_level_2.html
    sha256: a6915570a40b0f29bbf460dbe2cd04f04ea6c858647a874d9d6ee6f46f30f151
    role: context
  - path: pages/traits/ecology/biosafety_level_3.html
    sha256: 94e818f53a8a6101d8930c9f38b67ca22d56ccc0587a5b9b394ae6f28d4781f8
    role: context
  - path: pages/traits/ecology/biosafety_level_4.html
    sha256: 0f7ebef69a00e4a7c2f0b5a8767864f44c00998c45da4e5c49053cdbb7896346
    role: context
  - path: pages/traits/ecology/biosafety_level_5.html
    sha256: ad7a35dd488227c83f6bc999798138139ad86bdaef80206cb079adefefc52d66
    role: context
  - path: pages/traits/ecology/collective_bacterial_predation.html
    sha256: dc3a4c763aec372e2313ae516f2f837cbb26a085b031d647ff9851ee46342e5d
    role: context
  - path: pages/traits/ecology/commensalism.html
    sha256: dd95aa77cd3c29b83c42c64a6e4bcd3f3be1d6b06255b572308d8b2fa042046d
    role: context
  - path: pages/traits/ecology/cytoplasmic_bacterial_predation.html
    sha256: 6c4abf9204bae213dff0ad314ec32f2791ad1f77c6f3e7d3ec91d60d690f75c1
    role: context
  - path: pages/traits/ecology/endophytic.html
    sha256: da1dd07e80b71b658718b4018ad385ac481dd32bec7edb975f1da64c1481e9e7
    role: context
  - path: pages/traits/ecology/endosymbiosis.html
    sha256: 2a2ca72d00ac5d067d61b3bfc4a64f3100da8b1f863d8eba1a5f7ed4f031da86
    role: context
  - path: pages/traits/ecology/epibiotic_bacterial_predation.html
    sha256: 782fd41883c5af6425c541fa3cd823c76af8776205c34f6a36762f9547b3b80a
    role: context
  - path: pages/traits/ecology/epiphytic.html
    sha256: b5925099c8de86e3f27899f870e1eb424fcc88fe4af30346ff76cde87c68dfb8
    role: context
  - path: pages/traits/ecology/free_living.html
    sha256: 34b7d74d19d07ada6b09a5636e9cd3f3e56a808a90d16548429f6583c6888d74
    role: context
  - path: pages/traits/ecology/gut_associated.html
    sha256: 44e3217642ae6198d6953bf696122bebb224130e49bb77cab34ce4ee574dfe05
    role: context
  - path: pages/traits/ecology/habitat_association.html
    sha256: 440fa1d251669f63ba38945618555bc752a6c62bf0ad40850c48045b5207f3c7
    role: context
  - path: pages/traits/ecology/host_associated.html
    sha256: b5c3afc0025d1981355f728a6ea14a4be7c6f4d14580bf42b9c474dff58cb087
    role: context
  - path: pages/traits/ecology/human_pathogen.html
    sha256: e3f37993e7d4212cdf689b93db7c63a4626253fd01b0593d72a966cad8849374
    role: context
  - path: pages/traits/ecology/ixotrophy.html
    sha256: 24529d0d17d674a3342c19c8aff6306388ad328e36d3b8de01190e43f4f942ad
    role: context
  - path: pages/traits/ecology/mutualism.html
    sha256: 5b2d6d3f490cbe0bb6114086b8c92777851e789814e4cbc2762e2bd63d474334
    role: context
  - path: pages/traits/ecology/nitrogen_fixing_symbiosis.html
    sha256: 837a40af34258fb6727268573c7c17790891e847be536af4e6ce0036ce100dac
    role: context
  - path: pages/traits/ecology/opportunistic_pathogen.html
    sha256: 13c1d6a8137d1657e5ae1990bad8a84dd8554b302960f484166af0b957f3c0f7
    role: context
  - path: pages/traits/ecology/parasitism.html
    sha256: 795423ccf3ee326649a0571074ddea68b797afade5320f2475e836b1038fe52c
    role: context
  - path: pages/traits/ecology/pathogenic_to_host.html
    sha256: 5b3ab72d63ba61e5332ee5a1068762eb05db353f0646f946558893c0412acbc3
    role: context
  - path: pages/traits/ecology/periplasmic_bacterial_predation.html
    sha256: b47aa5c15f44ac1ad160ffd5e2d1e15c4e51c20181cc222dd5472361c469ea4a
    role: context
  - path: pages/traits/ecology/plant_pathogen.html
    sha256: bdda9e03652ac2c13c8ef010e2578e33e16ac4442977703fa71fb6c974909181
    role: context
  - path: pages/traits/ecology/predatory_bacterium.html
    sha256: 56538155088cec6b35353fa405414ad6065ab3d97e46d0055d83b12da835f49e
    role: context
  - path: pages/traits/ecology/rhizosphere_association.html
    sha256: dd3cc4b2114439794a7651c6ab43a9b25b6c5a3fbc208b117207ffd00dbbe4c0
    role: context
  - path: pages/traits/ecology/saprotrophy.html
    sha256: 5c228f8a71ec3b8402c0661f69eeb517f443f8a32f2b4dbbe6c6451a3c83fdac
    role: context
  - path: pages/traits/ecology/soil_dwelling.html
    sha256: 8a21e133aee82c1b1aa35dc200ef636384979dab5ab9f613a702cfdf830c1061
    role: context
  - path: pages/traits/ecology/symbiosis.html
    sha256: ef28642599d1a9abace57674981e547ea19a4cede1ed9b205c0d63485a914faa
    role: context
  - path: pages/traits/environment/acidophilic.html
    sha256: 5728004e7b40f0858458ed8a77d3106050b5d55415cc2a6912861983120525bf
    role: context
  - path: pages/traits/environment/acidotolerant.html
    sha256: 560194c3dfe885e7aa7a9f4fe27b137dddb64e772db04c0801b9c4bb2d4464a1
    role: context
  - path: pages/traits/environment/aerobic.html
    sha256: 8f7b5768411940575b41b088b9c7310ed6a234ddbd9d678c2fc8280301cf1358
    role: context
  - path: pages/traits/environment/aerotolerant.html
    sha256: 2810527db19b978bb3d98a494ec8af397bef02082a965c055116681176f2426e
    role: context
  - path: pages/traits/environment/alkalotolerant.html
    sha256: 5c5e21d0f6e27cca0f44297ff606a6cc89fcba85e0daf72a1aece745729a22f8
    role: context
  - path: pages/traits/environment/alkaphilic.html
    sha256: 659ccbaf8ee78d0627c98779911072897a74f2a8ca1bacd7c3ac6c99aa95171f
    role: context
  - path: pages/traits/environment/anaerobic.html
    sha256: 40fe62f277bb4f1d4edd41d473aaf95432a731a3586d0fefbceafd78fdc62dcf
    role: context
  - path: pages/traits/environment/arsenic_tolerant.html
    sha256: c27cf2b583b14f60ae77897ec5c2eb5a6e8c4eae0fbdb28eb45aeeb0562ecd97
    role: context
  - path: pages/traits/environment/cadmium_tolerant.html
    sha256: 9f3b5c82785e7f86701c0534a16ed4f795d9f41f5ff65286bb055c7e769d3ed8
    role: context
  - path: pages/traits/environment/capnophilic.html
    sha256: 841d0a3f7848e45cd397382362448e1b2e2540749fe461f305855a5701fedbb6
    role: context
  - path: pages/traits/environment/cobalt_tolerant.html
    sha256: 8f139c7cee175e42527c781f48d42eada31d250abf651a8f6a89705aa6d1b518
    role: context
  - path: pages/traits/environment/copper_tolerant.html
    sha256: e91164ed419705cc687bbd3453be29ef549131348beb093e0a9d2de3f304c5a3
    role: context
  - path: pages/traits/environment/delta_phenotype_with_numerical_limits.html
    sha256: 5c38dcf863d976d13f4c24c9da4b5db99094d656e49e2f303daf999a0e276749
    role: context
  - path: pages/traits/environment/desiccation_tolerant.html
    sha256: 2cdaf0617d1e2857aa74acd6ca72d13af25fe0bea1c8c6491407506e989d6680
    role: context
  - path: pages/traits/environment/euryhaline.html
    sha256: 622aaf62ef9832d11fd40d206e1d7c6bcf06a37148ee46c63c7438ba4bccf374
    role: context
  - path: pages/traits/environment/extreme_hyperthermophilic.html
    sha256: 7b82528e509407453650b0eaf70dcee2584b4266c68f53df2fc5748e2809a4e5
    role: context
  - path: pages/traits/environment/extremely_halophilic.html
    sha256: 8c637d09fcfd25b2737e3d406d141de23ecee2bf999f7f689a127f0125c0c25a
    role: context
  - path: pages/traits/environment/facultative_oxygen_preference.html
    sha256: 2410c9b6d47e32eee5bc423367d03f8a7d098f2da992cacef345add8a7749912
    role: context
  - path: pages/traits/environment/facultative_psychrophilic.html
    sha256: 7a8576226896c24c9dbdf71d50c20e5afd0ba37064deff9bb509de68fc8293af
    role: context
  - path: pages/traits/environment/facultatively_acidophilic.html
    sha256: 4310b918b07236aa7c04468c8dea6299a271f6cafeb796f3702b1d1be87c7bee
    role: context
  - path: pages/traits/environment/facultatively_aerobic.html
    sha256: 2793220f726bb2a15b03cd07c62c3987ced71ab53945b6d9b66cf77f6ec5991a
    role: context
  - path: pages/traits/environment/facultatively_alkaphilic.html
    sha256: 19881bb8c5e118d16240391027d307e602ed9565a34488f64567ebd8c5aab975
    role: context
  - path: pages/traits/environment/facultatively_anaerobic.html
    sha256: 7388ce0664c0258cfc6797f7d433186c92b8d2ad93fd6fbda309d58a069538bf
    role: context
  - path: pages/traits/environment/growth_range_phenotype_with_numerical_limits.html
    sha256: 8a7320dc85086bcf8ff9cab20d2970e5e2f0a3437962af001416397c3d3ab0f1
    role: context
  - path: pages/traits/environment/haloalkaliphilic.html
    sha256: 2c43ef2b69d28cc479fa8263be4fcb91781ac86074113956e50caf8d01cbbee2
    role: context
  - path: pages/traits/environment/halophilic.html
    sha256: 2c6219e23d7843b4902b4ebe53cadd0562a99ca6a8b6f6a33e2668e8dec9fe12
    role: context
  - path: pages/traits/environment/halophily_preference.html
    sha256: 67566841085c5dcf4cf024e09a676133f0a6112ca99a295968ba836e5f58130b
    role: context
  - path: pages/traits/environment/halotolerant.html
    sha256: bacc186ee22995f4053a83c7d8d0c325f029077e818ce9ccbfcdcae8fe49a130
    role: context
  - path: pages/traits/environment/hyperthermophilic.html
    sha256: 78c9020b8ff5678705cc735923fadd01eac5fa82465dd5facc9d24a45bf80337
    role: context
  - path: pages/traits/environment/ionizing_radiation_tolerant.html
    sha256: 03d62377322258e3dbcbec97dc84f2805dfb2f7320e5e29add62004b49254b0d
    role: context
  - path: pages/traits/environment/mercury_tolerant.html
    sha256: b8a00ed9cbd0f67e29081bdc534149e6b3f63e6c59feafd9453b7a7af08d36a4
    role: context
  - path: pages/traits/environment/mesophilic.html
    sha256: b8a7c1519f0d14a67941b5bcf594e80686afe67f64e87f2deb76cc6751df5e29
    role: context
  - path: pages/traits/environment/metal_tolerant.html
    sha256: 3f949da6025d708f97a51f8aaa261588260c519297f0e9ba6432cd49e623a672
    role: context
  - path: pages/traits/environment/microaerophilic.html
    sha256: 74ec6eaa1ad34de647f6e51c7e32907457337a60915e65333ee003f1286e9a2f
    role: context
  - path: pages/traits/environment/microaerotolerant.html
    sha256: 508570d41bf13e4246d8dcd2ba84dce7c300b01ff602abd3877c4b31b3771ad5
    role: context
  - path: pages/traits/environment/moderately_halophilic.html
    sha256: f8f8c9bba8219f2c10c39e21e6a4cfb56960956b87d1563b4ea10db154e4c527
    role: context
  - path: pages/traits/environment/nacl_delta.html
    sha256: 99188f21b7dd0019677e1cbb820df4c98c336c7f7214c05e8ff644c5eb6249cf
    role: context
  - path: pages/traits/environment/nacl_delta_high.html
    sha256: dc19c92164c2d91d9a42df842b583001d17735c14c07c87225250a02f87a1fb7
    role: context
  - path: pages/traits/environment/nacl_delta_low.html
    sha256: 8c335e04c0c22b1b70fb6294d8e772dee925b755420457396c9c736a41c7c629
    role: context
  - path: pages/traits/environment/nacl_delta_mid1.html
    sha256: f90206517c59f09c1fa8f2c7f9cf152afe21b96fead93526f3b44e531beac9dd
    role: context
  - path: pages/traits/environment/nacl_delta_mid2.html
    sha256: 079bcd24d95fdaea88de6243f7d2ab3ad8b78504b2ccd852aea8c033acdc154c
    role: context
  - path: pages/traits/environment/nacl_optimum.html
    sha256: 8b485a45244027937ad479ac1fa4dc47a80703a669542e11458a747d0d67502e
    role: context
  - path: pages/traits/environment/nacl_optimum_high.html
    sha256: 17d146043ee176e6d7189f74dae9734f1e887afe2c83fe9c434b532f9e7b80c0
    role: context
  - path: pages/traits/environment/nacl_optimum_low.html
    sha256: 1cabd7d4f780761513689c35edcec1a54867ffdc1e0d370839835122444ad4b0
    role: context
  - path: pages/traits/environment/nacl_optimum_mid1.html
    sha256: 5b880783bc107e748d25989cb6d56f00ee1f8fda901c1098ef359f5f06faed88
    role: context
  - path: pages/traits/environment/nacl_optimum_mid2.html
    sha256: d01ab9e0885b643ed3ef4e3ccb6a22583b50db848ba8595f42b18fec14e3f95d
    role: context
  - path: pages/traits/environment/nacl_range.html
    sha256: 521016a1645f3aa8737341d2a1ac182b1e00dc139332a0333245cfc6709cfd31
    role: context
  - path: pages/traits/environment/nacl_range_high.html
    sha256: babc983db9f2ea2ce6fb6e40d5cabbbfe5203f82b014aaac29b002eb95359794
    role: context
  - path: pages/traits/environment/nacl_range_low.html
    sha256: 553a1c2aeff41a1bf3826a7de1ca6e4991ada0a2ecf4bb0c64b464950fd16615
    role: context
  - path: pages/traits/environment/nacl_range_mid1.html
    sha256: 6ac6b0a3c8045b342342f1dc824216d866b056acb69a93f84a4cdf1c860f7ba0
    role: context
  - path: pages/traits/environment/nacl_range_mid2.html
    sha256: f97dca7ff1593c7fb867f760d64254a10947b3a20d1abe75f8de364e8c79e7b7
    role: context
  - path: pages/traits/environment/neutrophilic.html
    sha256: f694313c8e27d9f3815030b0a3b09ff744987a0d1a31f728d02e64b9cbc3f267
    role: context
  - path: pages/traits/environment/non_halophilic.html
    sha256: 73b975cefbce1f92826690471c0ab9635fad028877c278914e115b95bf4d161b
    role: context
  - path: pages/traits/environment/obligately_acidophilic.html
    sha256: b820cf7519a5c84d61fc3976b58e402742fd4a2a7b4032a36e05a4ceda1e191b
    role: context
  - path: pages/traits/environment/obligately_aerobic.html
    sha256: 348b3c13f0232e581a0f4cf373e56492a460064b562c7314c7cfe733f4f324da
    role: context
  - path: pages/traits/environment/obligately_alkaphilic.html
    sha256: 545a2131d6b61bd5a36b33d344a9493398ebb8fa8d0ba75555abb2ed009d3e3d
    role: context
  - path: pages/traits/environment/obligately_anaerobic.html
    sha256: 016e8caa47226c28dd107e51f568d0e8a6a0b1deba05e940816a006d55e14b56
    role: context
  - path: pages/traits/environment/obligately_piezophilic.html
    sha256: 19d98f5882b230ed98217394f52dd789195b166881cac77b435a0414f678e048
    role: context
  - path: pages/traits/environment/optimum_phenotype_with_numerical_limits.html
    sha256: 01cefefca41eff390e106fa2bfcf54a426125efb143981f483a4d692d92c4c09
    role: context
  - path: pages/traits/environment/oxygen_preference.html
    sha256: 20c51855b4ed11e00fc4050e898e2029c36ff5141d10d74011e4db94984db5b8
    role: context
  - path: pages/traits/environment/ph_delta.html
    sha256: 5eeecd950810ef681d65e458f81e0ad8c6456e8aa2d5f4cef8a1a8374ac5bf4d
    role: context
  - path: pages/traits/environment/ph_delta_high.html
    sha256: 7cab28d3aef8063810bc459b0c082f0f93d9e3d164aafec86bb80fcd05ec4c1f
    role: context
  - path: pages/traits/environment/ph_delta_low.html
    sha256: 8c95c775a463d98d0354fdc6bb764122af2b2cfe66a76f8c7fc0ad63ab447129
    role: context
  - path: pages/traits/environment/ph_delta_mid1.html
    sha256: 9740315946227bf7535f6b5bc9c6235655dcdf876d7b307d5413fc5aab46d4d0
    role: context
  - path: pages/traits/environment/ph_delta_mid2.html
    sha256: 6ceb5b67d4aae3f70b493317008db32d83d12730728ed7c2bc9c6394d77abad3
    role: context
  - path: pages/traits/environment/ph_delta_mid3.html
    sha256: b2ca4c849066e5035eb0fb8ef0633be68702bdd285e0296e5ce278526e7d5443
    role: context
  - path: pages/traits/environment/ph_delta_very_low.html
    sha256: b5fb5642c2516c55b08a678e440d876c4750d157a806f2551b9142ca07e5ea62
    role: context
  - path: pages/traits/environment/ph_growth_preference.html
    sha256: a25ff77a4ac5a17967314ea763d3325698d227cc0e9fc774f1c937804ebafe16
    role: context
  - path: pages/traits/environment/ph_optimum.html
    sha256: 54ed7702bdcfcfe6720c73b40fb5a660693c495facb91b3539299df40ebecfb7
    role: context
  - path: pages/traits/environment/ph_optimum_high.html
    sha256: 5e47cafe97b94bad5e9dff08aaec2e20a61a3ace33b3662f544e41d35dd91b04
    role: context
  - path: pages/traits/environment/ph_optimum_low.html
    sha256: 07c891b191c0fb6347c2c29709a7ca829f0af147bff7fe35adef36bca0808666
    role: context
  - path: pages/traits/environment/ph_optimum_mid1.html
    sha256: dd871162973fca73537b8ce2c7358f82693690039cf52b92607330112de7669a
    role: context
  - path: pages/traits/environment/ph_optimum_mid2.html
    sha256: 2e7b4635722c159381bfb3122fd2cac37534f501d604f5037c976eee832b5d35
    role: context
  - path: pages/traits/environment/ph_phenotype_with_numerical_limits.html
    sha256: f71181636b66b07091c8b1a63f3064e7a95197fdc226a181b6533487d778b0f2
    role: context
  - path: pages/traits/environment/ph_range.html
    sha256: 80e7a738d3fc5ca27823940e6d56056ef18b0aead97a944fbe14b3e76f2cd39b
    role: context
  - path: pages/traits/environment/ph_range_high.html
    sha256: 9f97e3f93b6793940f0bf540483c90333b2833e7266a2b6fab833f7c01a9e8dd
    role: context
  - path: pages/traits/environment/ph_range_low.html
    sha256: f33eed0a401ad552c8affdf54730cb6c14c1ea4d3965ca6d1d3fa3033fe0721b
    role: context
  - path: pages/traits/environment/ph_range_mid1.html
    sha256: 1d383355cc20a95b2644cd062cbca5145e4832d916b3d76f5bf47a3ad2f4d000
    role: context
  - path: pages/traits/environment/ph_range_mid2.html
    sha256: 7146dcd17bb45198c7551c430f4f71d2cd4867ae6f8e6dc4ed6326b5c846e391
    role: context
  - path: pages/traits/environment/ph_range_mid3.html
    sha256: c65009bdf6cfb3a88978beca1b773ff2ecc0b18bf57f8ae94d6a6489f44c95db
    role: context
  - path: pages/traits/environment/ph_range_very_low.html
    sha256: 22f4e9e278852dab3370b76d7e3bdcc006e1c64eeb9334be02e1c53e4e8e99d4
    role: context
  - path: pages/traits/environment/piezophilic.html
    sha256: 2e64861fa9118f842399c4d7439080abae48e06fda36c742fe6fd33698f0ff41
    role: context
  - path: pages/traits/environment/piezotolerant.html
    sha256: 6c87384dddd1a2c97b3e0d1a8e659aa52fe4634175e0e34f8edd55b7d016aa46
    role: context
  - path: pages/traits/environment/pressure_delta.html
    sha256: effe101e6ebb95474131007b9fadf6f4c1fe6ec4fc015f7586489862d6c0971a
    role: context
  - path: pages/traits/environment/pressure_optimum.html
    sha256: 69efb8c8b057f422464411d92a6bcdc4170666f6d63174ecd34a97733dd35699
    role: context
  - path: pages/traits/environment/pressure_range.html
    sha256: 88ba344292984da9601b5fb6dd0501e9abc14fbeec56901ecea7d164fba6b5d9
    role: context
  - path: pages/traits/environment/psychrophilic.html
    sha256: 72d402320d07a639ebb45b1df23e2c4d94633204fa81227b528391924f1f81ae
    role: context
  - path: pages/traits/environment/psychrotolerant.html
    sha256: 8864dcf18c11dd7d7676fdefe5507748576caa8345f4dd774d1a53ee72345bad
    role: context
  - path: pages/traits/environment/radiotolerant.html
    sha256: 0e4e4cc56e75ffd21b598f88f0872c438051e5c5effdddd275afd04c2a37e0bb
    role: context
  - path: pages/traits/environment/salinity_phenotype_with_numerical_limits.html
    sha256: b9d9ae3284a10fe9f3f5a8be73c04db078ddf5de359833bd60e7d76769a69911
    role: context
  - path: pages/traits/environment/slightly_halophilic.html
    sha256: bfd6f6d498bba159fb01225deb75e10244d78ff2bc708d1198c6a618365f188c
    role: context
  - path: pages/traits/environment/stenohaline.html
    sha256: 0ad039e8fc0f8ef55c1cd95eff24e2714dd48f9a5edf6dd5b70722098b37cb3e
    role: context
  - path: pages/traits/environment/strictly_anaerobic.html
    sha256: edec07f6ffa1a7707c42f5974aa930693fca0bdf9537c330d25704a8eb12ff09
    role: context
  - path: pages/traits/environment/temperature_delta.html
    sha256: 650268c6b3ef022ff7f621ee2086a6f77c046989627ad34d3cd3feeefc493bdd
    role: context
  - path: pages/traits/environment/temperature_delta_high.html
    sha256: 0afb6cabb6d456ff979b702fc0adc21f2f5e7093da2ab62617904e2dfb9bf2e9
    role: context
  - path: pages/traits/environment/temperature_delta_low.html
    sha256: a4473add07d86e3e6b37762b2bcb919852df6cddee6597f6db18f4d39caa17f2
    role: context
  - path: pages/traits/environment/temperature_delta_mid1.html
    sha256: ba94f43990686822deb2911517898d171030099d1127889d57c7269f24f86e46
    role: context
  - path: pages/traits/environment/temperature_delta_mid2.html
    sha256: edd8f26dd36652090ce81f29617c77b5c52cac36863f137134b3aac15e62e3fd
    role: context
  - path: pages/traits/environment/temperature_delta_very_low.html
    sha256: 65f2c9186667f967d1aa44340f233574fc05bf3921978cc2bb7a0da03bd6fdfc
    role: context
  - path: pages/traits/environment/temperature_optimum.html
    sha256: 8736d900281470b86b2e7982e4946b1d8942e4201592cc5e110e88b8274090a1
    role: context
  - path: pages/traits/environment/temperature_optimum_high.html
    sha256: a066586dc9decae9dfbae946dd55860aae43991e3f0e1c40616f9995f94294fd
    role: context
  - path: pages/traits/environment/temperature_optimum_low.html
    sha256: 1dcf14fa400a473551bad538d03acfe6b5fb0e8fc49981562cfb13d718ee96e5
    role: context
  - path: pages/traits/environment/temperature_optimum_mid1.html
    sha256: ef4c22c005895d1550dd5d3feac0e952de437f34362335602b8704d7f51b0564
    role: context
  - path: pages/traits/environment/temperature_optimum_mid2.html
    sha256: 98e28124c18454fbb327381c151d5968b8111fa1eb0d85a55c467e15027e6ddf
    role: context
  - path: pages/traits/environment/temperature_optimum_mid3.html
    sha256: 15336839081cf9ffd7e5e5d7629268645bc680c1263d2718cd46cc3e1351dd65
    role: context
  - path: pages/traits/environment/temperature_optimum_mid4.html
    sha256: 69cbc2ac82b106a7cf2a33ab49ec5dac78e6734c479cba34784f27534fc44b1e
    role: context
  - path: pages/traits/environment/temperature_optimum_very_low.html
    sha256: 5b643b02c9c311609b5515d17511cf311b454b6c032e021b6c391fac5aef9129
    role: context
  - path: pages/traits/environment/temperature_phenotype_with_numerical_limits.html
    sha256: f6da2330f4f365ccb6dab7b6de1f5067195ea23f37681c5a39df3627f74cc007
    role: context
  - path: pages/traits/environment/temperature_preference.html
    sha256: aa4ce5a65601b967c7e1e318c931dfb7bfa8e411088d23ddd30ddb5e5b37ec38
    role: context
  - path: pages/traits/environment/temperature_range.html
    sha256: 53a37230491c1c6ea849aeb716c5f81defdce8aae465927618fc8dc2ae44c535
    role: context
  - path: pages/traits/environment/temperature_range_high.html
    sha256: 482bcc71d26bba0181b61c92039815a56f9885e77e5cf827d8bd8da8e0d9a635
    role: context
  - path: pages/traits/environment/temperature_range_low.html
    sha256: a9288f2069fc68f00ee22f9dea5f85ebf8426129909e4201313abc5e14820b57
    role: context
  - path: pages/traits/environment/temperature_range_mid1.html
    sha256: 44e3cb6551aee7a01d99fcec1243f21dc815f42759198e86002cf75f1045fc7b
    role: context
  - path: pages/traits/environment/temperature_range_mid2.html
    sha256: eff677a250ffb9f270fddcc90696a6d35f52f5967831bd258e017580df69ca57
    role: context
  - path: pages/traits/environment/temperature_range_mid3.html
    sha256: e4b36ef8d15a22cb33df9e421272ae3bbe79b74a891bb49adb2540a5dcfbca84
    role: context
  - path: pages/traits/environment/temperature_range_mid4.html
    sha256: 996fbf18bac2fc0d2f2ca93a4fda7a96546833332f23f58c4eb86cc83582eae6
    role: context
  - path: pages/traits/environment/temperature_range_very_low.html
    sha256: 341a1de3cda96fbd548e796382cc9fe5a4d341704f98e5fe087de917666b62c5
    role: context
  - path: pages/traits/environment/thermophilic.html
    sha256: 633a1271ab3472b828be79cd694d55395f4fecbd1d9eb0df8de99c10f312d913
    role: context
  - path: pages/traits/environment/thermotolerant.html
    sha256: ca911ad614b5ec49ca1f2332aab6e7dd9d6563c273dec295dfee7032a2ca59d6
    role: context
  - path: pages/traits/environment/uv_radiation_tolerant.html
    sha256: 839212c2fc000b8fc01f7cc55a8b1c4464fea04fd36f7352a027f864f39142c1
    role: context
  - path: pages/traits/environment/xerophilic.html
    sha256: 707c714da6839965c07d8f382a0010a3c35a0e1544778ee2a1233456bed32511
    role: context
  - path: pages/traits/environment/zinc_tolerant.html
    sha256: 2edc7886aeb7bbf5f3b07da768d2f63fc3d85355df8c73cde882730b5c6e505e
    role: context
  - path: pages/traits/genomics/abi2_system.html
    sha256: a4fcddb4423eb4260b20107d07ef727f7a89e9c1fa461ed83532d243c6bf1b00
    role: context
  - path: pages/traits/genomics/abia_system.html
    sha256: 116626601bee29ae14d54651f6a97a4ace25551920b72bfa31d5285be24c3b85
    role: context
  - path: pages/traits/genomics/abialpha_system.html
    sha256: 046f6e289d9671e3344f1efc917543899860b715761264c0241c88f1c2c9c852
    role: context
  - path: pages/traits/genomics/abib_system.html
    sha256: e0c7eb12826dd956f1e658480f10dd653257dbb11cec0dc19595f95c87b6a046
    role: context
  - path: pages/traits/genomics/abic_system.html
    sha256: 518c2ae0e0110d26c22199583a9ff5693bbcc27d8912ee788741e956037aef23
    role: context
  - path: pages/traits/genomics/abid_system.html
    sha256: 5b6fdff4a43f97a40781c19010bd4272b28c93a0ad801938ae5dc3f6e695b12d
    role: context
  - path: pages/traits/genomics/abie_system.html
    sha256: 5de71459940de3bf22c65d470e89685f26b4d7e2803d5d5b3032128c4682b335
    role: context
  - path: pages/traits/genomics/abif_system.html
    sha256: cfecc575acff422230f1e4fd511566e826ab2fce36d89c80a195c734927afc71
    role: context
  - path: pages/traits/genomics/abig_system.html
    sha256: 2c3c44664b4b97bcea5cef70cf083ee119764d73aa0ca83475bc4933f6a5529f
    role: context
  - path: pages/traits/genomics/abih_system.html
    sha256: 58826abfc3da4fa3fa3b5f3cda4cddc6301c5782f435704981516fd865639eba
    role: context
  - path: pages/traits/genomics/abii_system.html
    sha256: f0a27e7db922095d83b69909c202f249a7cf7983c107c7e4acf55a4369307f94
    role: context
  - path: pages/traits/genomics/abij_system.html
    sha256: 7c12546d1bf17fadeab8dc069e874c4b77d1ba3247de6850983b66b96474f3b2
    role: context
  - path: pages/traits/genomics/abik_system.html
    sha256: a65db9f66b9ea48f8d895f400573f39f93df1ee2df5978f571db75317edabaa0
    role: context
  - path: pages/traits/genomics/abil_system.html
    sha256: 5c2f8ba5567a2ba7f6f2cab0bb73668ecd81deb17a68a89a695458059776d16a
    role: context
  - path: pages/traits/genomics/abin_system.html
    sha256: 01c32c4a585729b99fe41068492c32ce61299661c6815883639fcb26fef7f2d2
    role: context
  - path: pages/traits/genomics/abio_system.html
    sha256: bcf05f10c73345fde0160c2edf122dc01c07f4c562a18f09793a059e7a2882fc
    role: context
  - path: pages/traits/genomics/abip2_system.html
    sha256: 2fb8be3c0360ac5af53fb3cbb7d6c12a00c4607986c0aa09f8a50956fb6c915f
    role: context
  - path: pages/traits/genomics/abiq_system.html
    sha256: a9a9553bc009571ea80a11fc7129b6509a643901950b470a069fcf497d227193
    role: context
  - path: pages/traits/genomics/abir_system.html
    sha256: c4c838f8aaeb438a7f19bae14421409559908f13550d2abef77dbf949454fefb
    role: context
  - path: pages/traits/genomics/abit_system.html
    sha256: 343daf1ae7338a6b74b846fe65d1f7350567cd6b1f21b3da09cd7cf26371c9b9
    role: context
  - path: pages/traits/genomics/abiu_system.html
    sha256: 86e5a233cd25c060ce0f1c7a7cc82bf4f0e3d289a7f6c38f3bd18041f5b36827
    role: context
  - path: pages/traits/genomics/abiv_system.html
    sha256: a0a30c02c3bcb075db1b56535318d946e123d1b474c5f279167f4ff6c4f075c0
    role: context
  - path: pages/traits/genomics/abiz_system.html
    sha256: b776a6ed23b351624aba1685fa1f23d8abe1ddc3ec09e099219b2b5843c3f3a2
    role: context
  - path: pages/traits/genomics/abortive_infection_system.html
    sha256: 05fbaf6f714b95fd509c78f8ccff5d2749eb32497e181c6fe7acd9e4ad3c5f03
    role: context
  - path: pages/traits/genomics/aditi_system.html
    sha256: 8511a9ca1a074bd0797ff4fbee8ebe2b1b01b6fcac3da8b57f817311c958eda4
    role: context
  - path: pages/traits/genomics/ambrosia_system.html
    sha256: 546a321e60dc23b7ef368b31d3a9b6347785b3a6131dfb726e8889493ae4291a
    role: context
  - path: pages/traits/genomics/apsab_system.html
    sha256: f1e4a7f860357ecd9fa253f9c6243f02845f35943a7a64af8ca28b9d1a5de307
    role: context
  - path: pages/traits/genomics/aristaios_system.html
    sha256: b5832ff39d85892861ab056597df5d013a43e916839b33570b39786a8e40a899
    role: context
  - path: pages/traits/genomics/armada_system.html
    sha256: f9c66a9cb81035f8ae4166fd10b5a833c0d951d5b51480046d454ff11d37b10e
    role: context
  - path: pages/traits/genomics/audmula_system.html
    sha256: 1a17a3e660246edf89b122d7842eeb437756038b57245f2f2c95c4b170eafc45
    role: context
  - path: pages/traits/genomics/avast_system.html
    sha256: f7e42aa47fd823901c706dea1280d128522f8e72ef31ee4acbbfad0276fe78fe
    role: context
  - path: pages/traits/genomics/avs_i_system.html
    sha256: 10b0fd29c1ec13553c8ceac72b5db892f4b8c0509be3b613ae3019e6c0d200ae
    role: context
  - path: pages/traits/genomics/avs_ii_system.html
    sha256: f38d315dd278418d82d3c8a023406262d2f65fe78d23d694395f271ed96df8cc
    role: context
  - path: pages/traits/genomics/avs_iii_system.html
    sha256: ca8a3750546db417fc7d31ee8a90ef27e1c146b7d61bd467159e37a6ad4eccb9
    role: context
  - path: pages/traits/genomics/avs_iv_system.html
    sha256: c40cfb5a1c98f22ad0bb8a7bc07769597adc60c1ae6208651e07ca55172d152e
    role: context
  - path: pages/traits/genomics/avs_v_system.html
    sha256: 07eb6cfbfcc6fb7286d99009a4a847beb0444cdb1fbad81da9905d57ea71cb28
    role: context
  - path: pages/traits/genomics/azaca_system.html
    sha256: 29171c5d2533475200213bf6775c718d45f2c905b058a67c3bb56d2d6db56ef6
    role: context
  - path: pages/traits/genomics/belenos_system.html
    sha256: 509db7e3795ac2cd25eda02899a047bc9473cdd26580f48ace495e180bda20af
    role: context
  - path: pages/traits/genomics/belisama_system.html
    sha256: 8febae6287cf9fd7847628ec6ad263f0950ff8200928029fca9d505569783286
    role: context
  - path: pages/traits/genomics/bil_system.html
    sha256: 2239aac95429608077fd82d55825a31fdc12596e6e680ef8e7ba086e6265b148
    role: context
  - path: pages/traits/genomics/borvo_system.html
    sha256: 21265baf279a9a5732e27923fadbbce2af2d2f983e1c2d6b893e7cd4c614ccc2
    role: context
  - path: pages/traits/genomics/brc113_system.html
    sha256: 211e6337c01d65953f5cb0232f16e712d70d8715257e1e8dadd056904619269f
    role: context
  - path: pages/traits/genomics/brc142_system.html
    sha256: 750226836390e64dcc3dad45627e9d7fadb74cfe50b6323aea0ca351d0fff9df
    role: context
  - path: pages/traits/genomics/brc167_system.html
    sha256: 34bcbfa2444b52103a29f72ccd18d961874bebe182502d8e8cd04598c30ed0f8
    role: context
  - path: pages/traits/genomics/brc217_system.html
    sha256: fa163eadfdba1bfc3efa07eefe5ae5721cb8dab33ff0fc93b979152bce42222e
    role: context
  - path: pages/traits/genomics/brc22_system.html
    sha256: fc32c039a1230a2fd37b45678d10bca4f58bc1ef404858f1731f340a6c99c950
    role: context
  - path: pages/traits/genomics/brc233_system.html
    sha256: 609815e49d2cdacccfb712b381e118c7fd1485b58d222bef54036043765a36b0
    role: context
  - path: pages/traits/genomics/brc23_system.html
    sha256: 7f2e6ef48a1653f6014c8b1b6713c959d22fd7bb3cd4afe11fe889f6d6d9664f
    role: context
  - path: pages/traits/genomics/brc24_system.html
    sha256: 14a274ed0925a70e02f5b3429ed61f5158861bc22f5c958c725b79470967eae3
    role: context
  - path: pages/traits/genomics/brc59_system.html
    sha256: 6e02cbdc075c83a416fef5b09535d8351ce63cbe57f057e805f645a8302072ba
    role: context
  - path: pages/traits/genomics/brc76_system.html
    sha256: ad59b674c1f7143a3f3ba3c90a9b0580d7617afbcc290b856fa27d12ddf7e96f
    role: context
  - path: pages/traits/genomics/brcwgs21_system.html
    sha256: f6bf17b6459b1ff8d81491498e68a458a1e13eb54d0223f0521d0a6c0ff0da12
    role: context
  - path: pages/traits/genomics/brex_system.html
    sha256: 180f18a22935ee47eff32f3567e545b98a85285947763b8f62812a6d1653ae92
    role: context
  - path: pages/traits/genomics/brig1_system.html
    sha256: c6522d1467838badccdf9f8629b5b3157279bbadc88dedb6cad1ee93117a1ab5
    role: context
  - path: pages/traits/genomics/brigantia_system.html
    sha256: aab4b1577a82a4fe5552b37cfcfbca5a111e404a64c27b37af657dbf146d8dea
    role: context
  - path: pages/traits/genomics/bsta_system.html
    sha256: e235df05b65371a60dd2e165c2a66eaa359e9a32ccfc3e4815d1baef81f684e2
    role: context
  - path: pages/traits/genomics/bunzi_system.html
    sha256: a223e6ce5b23c8371b61fe87e959d7448e83ad10962467fbca1334f0bf1a8734
    role: context
  - path: pages/traits/genomics/butters_gp30_gp31_system.html
    sha256: bb33a7ef6ff9ded78a85482f778e79619398cd572f729b8c9eb7a309dacc6a4b
    role: context
  - path: pages/traits/genomics/butters_gp57r_system.html
    sha256: d8b2908bbe341f8ed4d56b260d8b94006a0d357bdd88ca6b03d7413f7a4ff3b1
    role: context
  - path: pages/traits/genomics/caprel_system.html
    sha256: d75ab81a6b9a548aec412f2a4e044c2514649d38df90c10b28c725d7b4805274
    role: context
  - path: pages/traits/genomics/card_nlr_endonuclease_system.html
    sha256: 0dfd3dc6e52faafea7b0257d3c2c6de3a56e0ec71a5a097180cd322bed335084
    role: context
  - path: pages/traits/genomics/card_nlr_gasdermin_system.html
    sha256: 1335e162b40642a1570c060b532ecd198314b201d5f53354bb9a0e6e1b8a7700
    role: context
  - path: pages/traits/genomics/card_nlr_like_system.html
    sha256: 86f4ffd4ddfe7e08ccaabfb1b4f4c1d8eea6581eb6e410a223abeca2142f42f5
    role: context
  - path: pages/traits/genomics/card_nlr_phospho_system.html
    sha256: 23aab5a839e4e37ec9eb8fed05f0eaf5809cb3a204d02bc64d0e10f09e91a5b0
    role: context
  - path: pages/traits/genomics/card_nlr_subtilase_system.html
    sha256: 663ac2ce39437cd5386cf554cb8447f5f4da595db7aa02312875696c6c464ca1
    role: context
  - path: pages/traits/genomics/card_nlr_system.html
    sha256: 5c9bd2a899a70129da3684e196c804a6f0575f120678a33fc154e1ac33d62569
    role: context
  - path: pages/traits/genomics/cbass_system.html
    sha256: c698055c7b0cb7fea3398e375a5202ce260c214a73faaea7c6a84ab7dfd3e69d
    role: context
  - path: pages/traits/genomics/ceres_system.html
    sha256: 10a04880abd1ed6198df694d649eb94d224b0d5af7672a4ddee477fc0be04e4f
    role: context
  - path: pages/traits/genomics/cernunnos_system.html
    sha256: 0853c2f21a3bcbbb823495ea63ca206f2d5cc0a6b06c05af37c02f961a979870
    role: context
  - path: pages/traits/genomics/charlie_gp32_system.html
    sha256: b7c37ecd6f479de797148edfcdffc8c420109f7db7057a7d14673ea5f8e6c520
    role: context
  - path: pages/traits/genomics/clover_system.html
    sha256: 805c1f5752e47116ae201aa37e6f0023c9cf133899917d9735057a18191b2c61
    role: context
  - path: pages/traits/genomics/cmdtac_system.html
    sha256: 6fad7913afbffe5767ccba3b23d45a276ff57456dfa9b34ae412bff710c25692
    role: context
  - path: pages/traits/genomics/coconut_system.html
    sha256: 23668fa0f1ea818106c4909ad0f8a5acd55126c5d5b9bf006b4d439c17249c63
    role: context
  - path: pages/traits/genomics/codon_usage_bias.html
    sha256: 4057e9f5d3d23b7e3ffd46554b8ad964a9a315605f52cd3f927f60897f35215c
    role: context
  - path: pages/traits/genomics/crispr_cas_system.html
    sha256: e0f029364802e3872fae8b05a94824a56392ac86d3639e6f93898872881a75f5
    role: context
  - path: pages/traits/genomics/crouga_system.html
    sha256: 2ce08610373a1082da28c3951f91f48e1fac8f76a23cc5b7a807223978b4bbce
    role: context
  - path: pages/traits/genomics/dag_system.html
    sha256: bde6dd858f5f81fb4a214bc10ec3e9b276b09cea10efeb776eceb5df2bfbab28
    role: context
  - path: pages/traits/genomics/damona_system.html
    sha256: a869ac3e6a2db5f0546b2cbe0feb83c29760b95c44a6cc3dd1f12ab52a63832b
    role: context
  - path: pages/traits/genomics/darna_system.html
    sha256: e4ddc8ccbf7fb90dc2fa9d36e9867e8704912ae98f29e72a78f9c0ad8e5686fe
    role: context
  - path: pages/traits/genomics/dartg_system.html
    sha256: 9ce2ede45a36d4742e1c58100f6519ec4799edad5193dd874e4f820284105c03
    role: context
  - path: pages/traits/genomics/dazbog_system.html
    sha256: dfff2c45d9836383a8e5d1d8762ded20c5347f7e53a781d2278e1b610c002cbb
    role: context
  - path: pages/traits/genomics/dctpdeaminase_system.html
    sha256: 10648d27a2ff1b42989c135d263aa147c84f6b3579d052a206718bd746aab41c
    role: context
  - path: pages/traits/genomics/ddmde_system.html
    sha256: 4d79cd93be4dce353d0b2a67dab95daac96de143c3467e89798f334d66b1cfd8
    role: context
  - path: pages/traits/genomics/detocs_system.html
    sha256: a18e1298dd64504b93fa70f1320d7b39a7c68547ace20d34ae47812f4329dc75
    role: context
  - path: pages/traits/genomics/dgtpase_system.html
    sha256: 234412884239fc808ec9f45651c89be47e4f350730dc741d2e50b8b402f9a8d7
    role: context
  - path: pages/traits/genomics/dionysus_system.html
    sha256: c036f23be6fc83d06a3ba35925b819870165b615c77c4984aa2131fa8bc906dd
    role: context
  - path: pages/traits/genomics/disarm1_system.html
    sha256: bf2f048c83af03b55a5fdb4d44b0b296eeea31d62ae64985bcf3d2e82adfda7c
    role: context
  - path: pages/traits/genomics/disarm2_system.html
    sha256: e4d85c0d45c6e9a22233f549b22d9d16ccceaefb2e8c455ef0b52b47843713b9
    role: context
  - path: pages/traits/genomics/disarm_system.html
    sha256: 9434c4ace28dcb525158c5236dd2f3b62d6cc45d55afede8fc14fa5deb8618ee
    role: context
  - path: pages/traits/genomics/divona_system.html
    sha256: 4c08c0d945bd51137836d05bfcd7ac59d0f2da0ee4ab66b705d9c312ab3e228c
    role: context
  - path: pages/traits/genomics/dnd_system.html
    sha256: 1ae154a7d50ec206f275c0ee7a5d9832245a51d4ee897d4b25511fbed236bbfe
    role: context
  - path: pages/traits/genomics/dndcdea_pbeabcd_system.html
    sha256: ccb88f75a52cf787593314fd740efe0426aaf63091d97818e91594f3c2386f11
    role: context
  - path: pages/traits/genomics/dodola_system.html
    sha256: 2c523624b9b499e87895ed7c7506f8db8c0df17dda41f79ff3c3164f0df4cc1f
    role: context
  - path: pages/traits/genomics/dpd_system.html
    sha256: a8da0ce47f248a7e9b0e65e0bee4a0033135b779d01ee0971158070e2c002717
    role: context
  - path: pages/traits/genomics/drt1_system.html
    sha256: f98c583500d7185eca50ef763282ee722eae990babe7bdc270b05062f0d6a635
    role: context
  - path: pages/traits/genomics/drt2_system.html
    sha256: 9d5093fe407f22ac47371677faccdfd903f1c5b43be23edb34a1398117835c96
    role: context
  - path: pages/traits/genomics/drt3_system.html
    sha256: be856438fde522e66ed13b981b5d6369699f81310bfbcc4f5d154fcb9e6b7290
    role: context
  - path: pages/traits/genomics/drt4_system.html
    sha256: 524cc1be3171eda9a78a308e1f979a59651eadd65e009828fc61f1dd6edabee4
    role: context
  - path: pages/traits/genomics/drt5_system.html
    sha256: dc85b97635293d2453c98d7625093f25385d5fee87a80d2d5407ea191510ddd5
    role: context
  - path: pages/traits/genomics/drt6_system.html
    sha256: d58312a5355746f6a9bb4beb1a2c254c73ce503dd6e51fc3159c5c93e12604cb
    role: context
  - path: pages/traits/genomics/drt7_system.html
    sha256: 959cc0f3bcb27dd379ed1ebc6e477a0e2d921bd6644f0ca1548bdbe176bbbff2
    role: context
  - path: pages/traits/genomics/drt8_system.html
    sha256: 3504954317e757c1e31a6777b804ce9b490d32dec2b6f4cc677a09782780023a
    role: context
  - path: pages/traits/genomics/drt9_system.html
    sha256: 55147ecba332ae3f8ef92ce1b6c7e928debc4327d1e1504165ad8faf670dcf9a
    role: context
  - path: pages/traits/genomics/drt_system.html
    sha256: c7c73c32aa242c57ab3a431dad9a6b8082b885606731cdf524feca936973f453
    role: context
  - path: pages/traits/genomics/druantia_iii_system.html
    sha256: 5fbbaf2b29e53d23edcf7e8650d1393f6856a8c687dd280fb2299ca89d3696e8
    role: context
  - path: pages/traits/genomics/druantia_system.html
    sha256: 11583d7e47722167f0d037f18c0a081b85f1ae7515e40fd897e359d525c4f76d
    role: context
  - path: pages/traits/genomics/druantia_type_i_system.html
    sha256: 31c6d7a58e46f30545112a4c29a0a24a8b915f4e9fabc530cf9cb3d9478ee79e
    role: context
  - path: pages/traits/genomics/druantia_type_ii_system.html
    sha256: 1ed2945e8c8f2efbbc15cbfa70b2deb78c8e3902e832f76a862924b212d50a96
    role: context
  - path: pages/traits/genomics/druantia_type_iv_system.html
    sha256: 8102b53b8b0f5a26dc13469efda3a7c8c3397dd00b8dff4f5acb54980268c217
    role: context
  - path: pages/traits/genomics/ds_10_system.html
    sha256: ae12a2c77f47d710bf247253321d08e94402167785902618ef5dde01882377ea
    role: context
  - path: pages/traits/genomics/ds_11_system.html
    sha256: e2efaf66a652ad68610261b5dd626cb9fa8405fdb096870f0c24f01aa8a7402d
    role: context
  - path: pages/traits/genomics/ds_12_system.html
    sha256: 1516da12285960076a9e33ec1a1292d0ed173fed44943e0bfa2f39e8655108d0
    role: context
  - path: pages/traits/genomics/ds_13_system.html
    sha256: dfc05bef6909050d2fdcf684804a1292d43661422eee32916914c846da256f4f
    role: context
  - path: pages/traits/genomics/ds_14_system.html
    sha256: 3fc93396a9aecf73c86db9f486cccd754c29761c5f10fc0892e497f7eef03fdc
    role: context
  - path: pages/traits/genomics/ds_15_system.html
    sha256: 55a9888b2a162481296d0997f83b07c1891ff5e4f9c0f0e49499702a0cc0f59a
    role: context
  - path: pages/traits/genomics/ds_16_system.html
    sha256: 60ac8dcb48ad9e545a39726a025a01a84f0f009bb1ef0fe9a6af70377753f2f5
    role: context
  - path: pages/traits/genomics/ds_17_system.html
    sha256: 5c67c96864f8b7e1ebae1b3b05d6b833fb075dcf732bcf57ebb363f2667521a9
    role: context
  - path: pages/traits/genomics/ds_18_system.html
    sha256: 7a16933e884243a31154e1e74cf5420eb27ea913f2c0371c62103e6076a86f22
    role: context
  - path: pages/traits/genomics/ds_19_system.html
    sha256: 71566971d90eaaa484077f117d13c5fbfe92f890fe179543f093cafdfe51eb83
    role: context
  - path: pages/traits/genomics/ds_1_system.html
    sha256: 18aaf0761e943a6557dbb8185c11a708ae253ee0f3166704ce0312b38e3e56f2
    role: context
  - path: pages/traits/genomics/ds_20_system.html
    sha256: 2324e76513fd4e4b474dfa190ecafa3b7cc499b623161a04ed74d3761c3c79a7
    role: context
  - path: pages/traits/genomics/ds_21_system.html
    sha256: ddc10fe08d03be4f6fd6be0c89dd80803612abd3267aff52a596c92adf964d4a
    role: context
  - path: pages/traits/genomics/ds_22_system.html
    sha256: 595fb95ed67f677f43606d309725b4987b34483fd16636f523bcfeb67bb6ced8
    role: context
  - path: pages/traits/genomics/ds_23_system.html
    sha256: e2b96a7267669c65cf1996e83c10f53ec8a7bc455ea6249118b6c81f254ba55c
    role: context
  - path: pages/traits/genomics/ds_24_system.html
    sha256: 87bbc438534809a790f0a7916063f36279d61a98192f6df617ceaf6d190fa5e4
    role: context
  - path: pages/traits/genomics/ds_25_system.html
    sha256: 634076d5107bd7a03afaab36fb0b280651537cfe0422effc794238d0ae8a2d07
    role: context
  - path: pages/traits/genomics/ds_26_system.html
    sha256: 7cdbbc03c174774c5e7bbb09dd2fd4756300e2cfb943a817a0fa48acacfa2ed3
    role: context
  - path: pages/traits/genomics/ds_27_system.html
    sha256: 9256cbbc72cc950fd17c132e036db6d8fa98cf125d28a44067434ea9eaab856c
    role: context
  - path: pages/traits/genomics/ds_28_system.html
    sha256: fef6ab5f28fcc19a6e8fd98c34c519b91f8e9bc0bc2eeeb426e4fcac39891b53
    role: context
  - path: pages/traits/genomics/ds_29_system.html
    sha256: ca05fc7dd9d8e1b18bec14635a22884705c12b7bcb77b6cdd399dd02693cde3c
    role: context
  - path: pages/traits/genomics/ds_2_system.html
    sha256: d0f8d4bd3f4378cba1c73651e64a67a286bfe35d9e2542442abc8d424d1b9d25
    role: context
  - path: pages/traits/genomics/ds_30_system.html
    sha256: f9fee0a4a3176482474b2eac1913760f097355e939d62556639baf123cc447cc
    role: context
  - path: pages/traits/genomics/ds_31_system.html
    sha256: db6b82417597e2e21273dcbb46287c8522129e02dbccbc46074e29cebafdb468
    role: context
  - path: pages/traits/genomics/ds_32_system.html
    sha256: 4a72daa54fd89565eea481c488375ed072158d48698bcf42382abf6e213c09d4
    role: context
  - path: pages/traits/genomics/ds_33_system.html
    sha256: 31c34521c222955e1b534e84a800c277f5d068c3a94e3b4b9bde0fbd540b1824
    role: context
  - path: pages/traits/genomics/ds_34_system.html
    sha256: 22ecab3d4bddd565b0b9019ca87e5ee42a8d048b460e0a0579e978da3a1a8d0e
    role: context
  - path: pages/traits/genomics/ds_35_system.html
    sha256: 7126da8852dbe20988c36f726ca78f1aba54b933849f6bd397c71817c8e959b1
    role: context
  - path: pages/traits/genomics/ds_36_system.html
    sha256: b032ab9e82a2d4376ea67f2d6e574f278c9f0f82d74c4e758f1e92704b7b7676
    role: context
  - path: pages/traits/genomics/ds_37_system.html
    sha256: 652782ab8e659a1c567ce225fa4819270e7057e6cdc4bc8bc61ea4a2c46fae7e
    role: context
  - path: pages/traits/genomics/ds_38_system.html
    sha256: 63e635851f77334a11c2403936b328c7d26ae83031b40e7d4fe378f7f9acbaf4
    role: context
  - path: pages/traits/genomics/ds_39_system.html
    sha256: dabd13ea9569e1387ef23127e52c3e64700922b5c6401bd2eb82a2ebd14faf4f
    role: context
  - path: pages/traits/genomics/ds_3_system.html
    sha256: 243dae84b2ee07b26920dc7c78121f6b22b9d2ef5405e4e79c349cc0dbbe72e6
    role: context
  - path: pages/traits/genomics/ds_40_system.html
    sha256: 3acb4eca86a9eb548fb9e4def139a7f859638e932d9e23317a2302e41fea52c1
    role: context
  - path: pages/traits/genomics/ds_41_system.html
    sha256: 430755317eecc9bf45105a8cc0183cf0876b378a2946ab186ab731bb40c5a853
    role: context
  - path: pages/traits/genomics/ds_42_system.html
    sha256: a1294206c67009f45c046a83cd0d3b8c46a58e74c07da29d4b3d5cea2e8496d2
    role: context
  - path: pages/traits/genomics/ds_43_system.html
    sha256: ab8357e314accff00b3c34f4e1b5f1a690ee27f7559554f8a0110d4e746cdf9c
    role: context
  - path: pages/traits/genomics/ds_44_system.html
    sha256: 3b088044cf46021be2a48b3134a1554da14fa796e90e29249734a989bbbe4ac8
    role: context
  - path: pages/traits/genomics/ds_45_system.html
    sha256: 13ce3b1f57577c2b34402ba7f6a96ac30076ee3e73acfb7b66ba6c15421678d9
    role: context
  - path: pages/traits/genomics/ds_46_system.html
    sha256: 3e63aa7162f312414da89618fd9c8d3f10af402aafa6b15c82a132e69f452dee
    role: context
  - path: pages/traits/genomics/ds_4_system.html
    sha256: 75001bbfa482356bb63cc91bbcdbd08ae32e1c5a29dc11f340e2e52866077015
    role: context
  - path: pages/traits/genomics/ds_5_system.html
    sha256: 32f2f7551c3caab2a548272ee7833160d1661e1f462e820c955a44b3789b5c76
    role: context
  - path: pages/traits/genomics/ds_6_system.html
    sha256: b1f3371c0ff0e152cf281c03c9a844415eff7cd71d27f5d3e9079a5266023e7b
    role: context
  - path: pages/traits/genomics/ds_7_system.html
    sha256: 9a39be6fdcc3ec6a4a27c87618b414488546f01e5d9d23fb89540c405e64a291
    role: context
  - path: pages/traits/genomics/ds_8_system.html
    sha256: fe7f071f22ce1196b0642e043527d88d54373fd60b0121d924c85959a8229c3d
    role: context
  - path: pages/traits/genomics/ds_9_system.html
    sha256: 5fcdcb7f03c95b7f4edbcadae4afcc01ef1797c564bf3b470094f6e7cdf6e6d3
    role: context
  - path: pages/traits/genomics/dsr_system.html
    sha256: 3a08b8c9c350d3b186a29b07a97fccd4bbfba9aa4d31ced12dce2a5ebc3df90b
    role: context
  - path: pages/traits/genomics/duf262_schlafen_system.html
    sha256: 256116ec0a081cb89bfe6abe9eae9e5ca6fc5cc5033ee9dc35cb9f2284382ec2
    role: context
  - path: pages/traits/genomics/ecokmcra_system.html
    sha256: 24410cf52ed00b4f3d9df37f93cd5d5019bb1ac8eb0a5d4a6fc044b72b9fb2e1
    role: context
  - path: pages/traits/genomics/eleos_system.html
    sha256: dac7d40e53d831a357f4356d0e7574deddce87dc303d8316a85a02cc612efbbf
    role: context
  - path: pages/traits/genomics/endpacf1_system.html
    sha256: 61942b745c9aedc4965f278287d74208f3df23abce3d2c6dbd5ea6573dabe998
    role: context
  - path: pages/traits/genomics/epona_system.html
    sha256: 6dc12e5f0a48d1c6d7fbf7d3f4046a56fd31c763eb68cdda0e71ee21b5c5833e
    role: context
  - path: pages/traits/genomics/erebus_system.html
    sha256: 0d5312587e903aadb6c08e63f820065b785842c808c5cb239a3021c597561c6d
    role: context
  - path: pages/traits/genomics/esos_system.html
    sha256: ed79c6a6181ad6fac5deb78774d372ab31c4e0d1b45852cfa3636f8a7efc67eb
    role: context
  - path: pages/traits/genomics/fliodhais_system.html
    sha256: eab493f64fb391206bba8ab69df824d21a92e0b89c3c4cce7a4db4f203988365
    role: context
  - path: pages/traits/genomics/fs_giy_yig_system.html
    sha256: 8dd8492acc129fc569ccc2d30d6f1370d61214100b0625afbc44fdec1ba5821b
    role: context
  - path: pages/traits/genomics/fs_hepn_tm_system.html
    sha256: 5b151d6b5cd6f7afbe5daa21f425f15177bbfcdb3ad62d980177d35cd47fd5c9
    role: context
  - path: pages/traits/genomics/fs_hp_sdh_sah_system.html
    sha256: 0f572d637f10ce362d2ee36629db8886a2074dc22e69e0659274cb6b12775a2a
    role: context
  - path: pages/traits/genomics/fs_hp_system.html
    sha256: 8bb227c35f67e9263383c061460eb491efd5159db27bd84a3155f6bf2d586b9c
    role: context
  - path: pages/traits/genomics/fs_hsdr_like_system.html
    sha256: 551d297fda7f90ce4a4005f5c4445c8b076fca04d07dd8b597b196caf576dbea
    role: context
  - path: pages/traits/genomics/fs_sma_system.html
    sha256: 8ef9b3ed938429db1a01c858847b6beea1e8c0ed8ad7f4b3d41dde8c0f904cc6
    role: context
  - path: pages/traits/genomics/gabija_system.html
    sha256: f816ef4ebf225ded25d541e0ffb01daad196fb27ba52807f49e649c6037c0081
    role: context
  - path: pages/traits/genomics/gao_ape_system.html
    sha256: 799655c62bf0576fc80eb9f492246ee38fcd5ff066201e69022e31d22fc4ec20
    role: context
  - path: pages/traits/genomics/gao_her_duf_system.html
    sha256: 6fa7e0dcef321286f992e681df16061f6ea6258baa1ec983978172e03d2d725b
    role: context
  - path: pages/traits/genomics/gao_her_sir_system.html
    sha256: 3e8a255e49a6fdfeb1fe6b6487f6d3131156d6b7531baaa07c96df7fab68e942
    role: context
  - path: pages/traits/genomics/gao_her_system.html
    sha256: 74961a0e754a99ee42c74768fb8f7c6f63729bceda42feaca2964699e403d840
    role: context
  - path: pages/traits/genomics/gao_hhe_system.html
    sha256: 90e9899cf5dc5dae481a19555cc2db3a382af692400ba402549fe7c047f5dc7c
    role: context
  - path: pages/traits/genomics/gao_iet_system.html
    sha256: 540c7d2e65192f472fc8896e2ef5c08c38dc398a30912587f47351998ae3c65e
    role: context
  - path: pages/traits/genomics/gao_mza_system.html
    sha256: 804d6ae32e4c7a7814bef5f79c31e48b9f589931cfff4128e9bab53250aa0d3f
    role: context
  - path: pages/traits/genomics/gao_ppl_system.html
    sha256: 1f581defc78d3d447b8fc67b45b53040bbed1aad37533eb4667cff939af4870d
    role: context
  - path: pages/traits/genomics/gao_qat_system.html
    sha256: efb834d349b101753dfbeaf1ad802827f1f1d0994239df9634f572759e662113
    role: context
  - path: pages/traits/genomics/gao_rl_system.html
    sha256: 3471c220cd1cbd47fae0faf7d6a2942dfb978e6c495aee90c21d911cdeb35848
    role: context
  - path: pages/traits/genomics/gao_tery_system.html
    sha256: 2f79fe96f7b9f22ddcf19136580722b3d17d0797307f7ea4998d5ac5ed2c22c7
    role: context
  - path: pages/traits/genomics/gao_tmn_system.html
    sha256: 66628e11b23600ffcc608eb970dff502f938d4de437e10008fbe0ba568804cd9
    role: context
  - path: pages/traits/genomics/gao_upx_system.html
    sha256: 235300bc7e9eaa2cc578a08531ebeb409844b91c07bd12692e293bc38b429472
    role: context
  - path: pages/traits/genomics/gaps1_system.html
    sha256: 7fd5f82b834ad42dd150ef5296a9562ab8abf5b41e1cfb1670187f6e6d08e98f
    role: context
  - path: pages/traits/genomics/gaps2_system.html
    sha256: 9f6ab41a535389be5df539737441eeb1f4990582dd2fde0a6620a0b1b873f916
    role: context
  - path: pages/traits/genomics/gaps4_system.html
    sha256: 52bf615e4e995839dfeaa46261148ac7b190f12f8563bd0f8c802dc2265f842c
    role: context
  - path: pages/traits/genomics/gaps6_system.html
    sha256: 8eee42dd095b9dd74565e3a2954523dd473b46d08da179460486f82ae8371e70
    role: context
  - path: pages/traits/genomics/gasdermin_system.html
    sha256: ea114e9f99203891d65f6a4eb9f43ff2b73fbe4df692e4daf6c0f4720a8a1c1b
    role: context
  - path: pages/traits/genomics/gc_content.html
    sha256: a638598a150de01a7f65cfd695611fa7556a5af5f7eed03423a358d7c6d621ce
    role: context
  - path: pages/traits/genomics/gc_high.html
    sha256: 2f53f4f7d1abf215c6dd5da98939bb196fc9ebe951b564a3ac6eb04f37a10c07
    role: context
  - path: pages/traits/genomics/gc_low.html
    sha256: bf4bbf739157ec3f2221a3ded03a2ee7e5b31393b8947321d2a672c93d059e3f
    role: context
  - path: pages/traits/genomics/gc_mid1.html
    sha256: 169323717dbf2324ca097c8687fc75fa5644dcee293f9e84d784d21c801992f8
    role: context
  - path: pages/traits/genomics/gc_mid2.html
    sha256: 8d4e4db3a300f06f7f886dd1851c66393156f821507ae6b122dec9f9e01785de
    role: context
  - path: pages/traits/genomics/gc_skew.html
    sha256: 2b562dc3bb39cfb4d88fcf0d83c05dcabbde0a6742daa9333ee2114e1a30898f
    role: context
  - path: pages/traits/genomics/geb_system.html
    sha256: 86e69487955a77fb271db9ffc3a8fe0da225ccdb787b9f211acb6758a792232f
    role: context
  - path: pages/traits/genomics/genome_size.html
    sha256: 30275d13e4a6fb613d25ee187985ba4b7bbb6da60d03d60bde735f63c3817797
    role: context
  - path: pages/traits/genomics/genome_streamlining.html
    sha256: 65eb0cc58824799fb4903e819cd46d587988556a5f61f6c079f00e260442adde
    role: context
  - path: pages/traits/genomics/genomic_island.html
    sha256: 6030c70a4c19c35432332e6a71e4dd6a9f4dbf88d15f3d59e5b1380b987b1272
    role: context
  - path: pages/traits/genomics/gmrsd_system.html
    sha256: cbe4343ced5e0bce218d83c2a3f93fd9bcf887c04847fd89a3fe8e86f4538695
    role: context
  - path: pages/traits/genomics/hachiman_system.html
    sha256: 0e42d10dfd6efcf8c9a6a7cefc3c685e0d269f00890bbe21cf648e1d698811d7
    role: context
  - path: pages/traits/genomics/hachiman_type_i_system.html
    sha256: da0ceacaa0ca8167c65597cea7c5d096b9dc895cbea8cfb496171928684499b1
    role: context
  - path: pages/traits/genomics/hachiman_type_ii_system.html
    sha256: a434aad24ecd420cc0b859729c8e78c05717ac6194c984d8b7c33c0606c085b0
    role: context
  - path: pages/traits/genomics/hailong_system.html
    sha256: e5540c6bffb8bb6a4b18f31a4cebf0932130cb0b852df8f93697f18f5e0bf5b3
    role: context
  - path: pages/traits/genomics/hec_02_system.html
    sha256: 4dbf69e730ca37fedaeeda16fbe209c4cb80fdba3229cd3c8a41a9baa16288ff
    role: context
  - path: pages/traits/genomics/hec_03_system.html
    sha256: a10879f4c9dd95a18c3ebf933aaadd7bdf206d184af1e221019d199ddff7df18
    role: context
  - path: pages/traits/genomics/hec_04_system.html
    sha256: edd66f665a7f110913096cd96f532c6df3654bf06cc6a6282ff2b6bd9c20406a
    role: context
  - path: pages/traits/genomics/hec_05_system.html
    sha256: 1f4b086cefaea4e80a1df547d08fe1a1224402f8aa6ab99007bba0e8d1941509
    role: context
  - path: pages/traits/genomics/hec_06_system.html
    sha256: 8aa6768c15938b1b483d3365bee27e7c6896db2553fe8ef1a3ef494ba8c7ba0a
    role: context
  - path: pages/traits/genomics/hec_07_system.html
    sha256: 72301e2e7fbda02e630f3a67c0be64a4d19e987ae72d4312453e92abaa1c8ec1
    role: context
  - path: pages/traits/genomics/hec_08_system.html
    sha256: 49c534cb7183185187756dd4cc7353fc32b1d9dfaede6b79f3c04e72cbd6022b
    role: context
  - path: pages/traits/genomics/hesat_system.html
    sha256: bedb8fd81f8d73ca5790085c267b7cfe5d2463988454d20be6e2d44b68a39630
    role: context
  - path: pages/traits/genomics/heterokaryosis.html
    sha256: 5f15a112248b55b315110617346e817dde74300d90e7a9869ba0105164a3f62b
    role: context
  - path: pages/traits/genomics/hma_system.html
    sha256: 21a662ae62c19e9bab3d2fd793a419382922321cbc7f81c167879a3260cbc937
    role: context
  - path: pages/traits/genomics/hna_system.html
    sha256: df1faeab0892d90d4488d69782e8846bbf6c98f629f202739606d62e33429e8a
    role: context
  - path: pages/traits/genomics/hypnos_system.html
    sha256: c2255668a3322dd195ad1af5564251243da2f57a442ce94e74506287d559d58a
    role: context
  - path: pages/traits/genomics/ig_like_schlafen_system.html
    sha256: 42e967d6c5409dd2944943ce1eefd7294e648d22075ae754b18812d7bd006b1d
    role: context
  - path: pages/traits/genomics/integrative_conjugative_element.html
    sha256: 549be7afc288d33e3c7a918db43acb56c0bef5694da24403070d9543955d9e86
    role: context
  - path: pages/traits/genomics/jukab_system.html
    sha256: 875bd06add78db3d72c493b357969e40a3895c0446fe4edcf53747edc2b04f80
    role: context
  - path: pages/traits/genomics/kamadhenu_system.html
    sha256: 9da2cfa39ec088bdafe15578688e21dfafd69c895dc37c69b5037dd7ab061def
    role: context
  - path: pages/traits/genomics/kiwa_system.html
    sha256: 2b49faedadb712020393a8b7a496df2a236adf20705df05edb0dcc851f5e35f0
    role: context
  - path: pages/traits/genomics/kongming_system.html
    sha256: db6d70e84277e5a2508e9d32e5d8a15d185f25ef6b2c98f20cdc75a5905d9ead
    role: context
  - path: pages/traits/genomics/lamassu_amidase_system.html
    sha256: 1d2846d55124c8b7fc23c892bdae9dda89df2620ef0c0180e394705e850b7cdf
    role: context
  - path: pages/traits/genomics/lamassu_cap4_nuclease_system.html
    sha256: c38b74572019d8cfe2939b3479c2c3df8e3ee6db6cdce0bf604fa01ca4346d7c
    role: context
  - path: pages/traits/genomics/lamassu_fmo_system.html
    sha256: eff01a59af2a29e2a628dbf9fb6c3ad8e86923506964aa47ba23500085346387
    role: context
  - path: pages/traits/genomics/lamassu_hnh_system.html
    sha256: 27e522a9ae781352296322a3368fa2079af628435bffb9a3cbcd52e37c470208
    role: context
  - path: pages/traits/genomics/lamassu_hydrolase_protease_system.html
    sha256: bac6ba4e28cc142e6bd1d89a345488ed15711ef7575d730d989470b333c3925f
    role: context
  - path: pages/traits/genomics/lamassu_hydrolase_system.html
    sha256: 96f77d67be132809bec54ed936e196bf93defdc99e44388cd4f5a330d1e125d3
    role: context
  - path: pages/traits/genomics/lamassu_lipase_system.html
    sha256: c101583e02953cb04f495eb3584b1ae34cac12aa4c25b52ba9dd1be0d51bbec6
    role: context
  - path: pages/traits/genomics/lamassu_mrr_system.html
    sha256: 86b0db4b684c9f8ddc5fbf9e1e55b48fc5950e43607ad3fa96e8e78bf5d6bdd1
    role: context
  - path: pages/traits/genomics/lamassu_pddexk_system.html
    sha256: cd1d1de243360c26ad2b5a5a5b979f55e183750696c86574e79d1d1c60f08340
    role: context
  - path: pages/traits/genomics/lamassu_protease_system.html
    sha256: eb8e5c81cd6d2e912a188bfb2cdcbc6b360c6e4f2db01d074d66fb241e6f0220
    role: context
  - path: pages/traits/genomics/lamassu_sir2_system.html
    sha256: c14738d2aa838c423119e033f2e6dea4e0dd70daaebc7f6a1198ed6c7e2cb75e
    role: context
  - path: pages/traits/genomics/lamassu_smek_system.html
    sha256: 558aea67a8733cb8e605bea6bd2eea5ec5b71f9eea557902f18746adbbbbe90a
    role: context
  - path: pages/traits/genomics/lamassu_system.html
    sha256: 970778ebf3baaa0f78c63bc795739d530724a3f7b14a12c09f0ea7a2f24820e6
    role: context
  - path: pages/traits/genomics/lamassu_type_i_system.html
    sha256: c4256d143bfb52f7515c60d8e54cbf4578da415e38db0d71dba68d6549fd4699
    role: context
  - path: pages/traits/genomics/lamassu_type_ii_system.html
    sha256: cb468c582b02519593bcec327af9095f4c545be9e9f5342b3f58d582fae9aa4c
    role: context
  - path: pages/traits/genomics/lanthivirin_system.html
    sha256: 7afff047303434f532fea8e55ae62124aa940c2662e5a87b204f91d105b25064
    role: context
  - path: pages/traits/genomics/lit_system.html
    sha256: 1a6b6365a036268d67b0b296ac05198bb0eac6e8983b4bb5c9f58b3280ad6227
    role: context
  - path: pages/traits/genomics/long_lamassu_system.html
    sha256: 6607f66ad4c807c93ce3f0a36acdc5559de84e1cc2952a148778f6e9575e2ea7
    role: context
  - path: pages/traits/genomics/lugos_system.html
    sha256: 3e873106227e4cdb0ff841f4fb5e50fa935fb9224325fd1ae1ee082ca3743ce6
    role: context
  - path: pages/traits/genomics/mads_system.html
    sha256: 6726147d4b9579c8f9e896292ae6bf283d6442e92a578ec1922b4502b405ad43
    role: context
  - path: pages/traits/genomics/mazef_system.html
    sha256: 0458bf9b2c7cea8fa8221ef0cd63331f9bab364fb18d24363d1cbbbeb3183afe
    role: context
  - path: pages/traits/genomics/mcrbc_system.html
    sha256: 0bfbdbe266301c20446738e3f1905715394c293b8401534a69828faeba8a5094
    role: context
  - path: pages/traits/genomics/menshen_system.html
    sha256: 187ec38ed4c5af8d63b9c7268baed293cf29e0dab577d592e2454f7d43754a81
    role: context
  - path: pages/traits/genomics/metis_system.html
    sha256: ccea2922f6c79dcad2d3a51b5acca6d82ea7ca41263914ad070afc006fed8baa
    role: context
  - path: pages/traits/genomics/mksbefg_system.html
    sha256: e0f6d27b1956b2939cfae62bed0775773a14779602bb008962eb75ffb326b000
    role: context
  - path: pages/traits/genomics/mmb_gp29_gp30_system.html
    sha256: f7c3044ddc5865d861222788a8c10d06565bb593918a84279cc7f2c645a21a63
    role: context
  - path: pages/traits/genomics/mobile_genetic_element.html
    sha256: b6ab7f45b707cd1f3dc00d8b32628dd6185f44b6fad33f5e6a4aad2d67512e6c
    role: context
  - path: pages/traits/genomics/mok_hok_sok_system.html
    sha256: 7ec330aad0f9ed9dd715f98f93dd25330591b24965b2bd2b2fdab5be39d9a57c
    role: context
  - path: pages/traits/genomics/mokosh_system.html
    sha256: 53d71acc5fb7735b92f3f750e2841fba16c3bed739d6566c1ad4c7989f878e19
    role: context
  - path: pages/traits/genomics/mqsrac_system.html
    sha256: a193d431be423f33cfec51576165205bd197af5fdaf253640ce4ff89135dea7a
    role: context
  - path: pages/traits/genomics/mspji_system.html
    sha256: 1993ce0b0d2a70132762070774cd3706d094c8ebe64cbdedc87b8f907d44149c
    role: context
  - path: pages/traits/genomics/nantosuelta_system.html
    sha256: e2f16c5f0301d33051db0c2b66016717a3418c7dc2ab609458b50977a8a742df
    role: context
  - path: pages/traits/genomics/nemetona_system.html
    sha256: 111b61d9fb567db32f15129729a7ae9b5da7b27d4f166f3f2408f8ee7d3d98a2
    role: context
  - path: pages/traits/genomics/nhi_system.html
    sha256: 2e5c31839658c263eb74908d356e1d55f43cf309e8ec4a9555305b829fe87412
    role: context
  - path: pages/traits/genomics/nixi_system.html
    sha256: d074d97002f7aaac50f7b47a652a7dfb9fcd223e945f58a5eeaa9d5123c0f719
    role: context
  - path: pages/traits/genomics/nlr_like_bnacht_system.html
    sha256: 3cd8f1a767c987f15c14bc08e082dec4047f257f6d3a8484ca350f89a100a5a8
    role: context
  - path: pages/traits/genomics/ogmios_system.html
    sha256: fd0c0cf9b6e60e63258a1e564d5743aa1237965abd778e55122ed0b48029bb6a
    role: context
  - path: pages/traits/genomics/old_exonuclease_system.html
    sha256: 832829c343e627f4ecbc9b37c78304b8ddb6daf9884e8bc9f81640b02949f6ce
    role: context
  - path: pages/traits/genomics/olokun_system.html
    sha256: a5f78bc813f7a775e247eada1f53161b410dcb541f0f68252b45c449b5d6cbea
    role: context
  - path: pages/traits/genomics/ophion_system.html
    sha256: b8a47110b1dfcfa02cbd403a6b8e55e490fe05f419cb356d82c6ebf65fb7326c
    role: context
  - path: pages/traits/genomics/oshun_system.html
    sha256: 282d90946b72d35207771356ac07dd63bf6b6a7094d752bde7b90ef0a83cd77b
    role: context
  - path: pages/traits/genomics/pago_system.html
    sha256: 8938da4d3923d283e00073ef86b84c2458d2bac9855df4e88f3b183a9ed6af50
    role: context
  - path: pages/traits/genomics/panchino_gp28_system.html
    sha256: 8faff6eea6a0953f9660a2807a8abc7b2d69eb9b80efe1c2b5cd1a883548a35f
    role: context
  - path: pages/traits/genomics/pangenome_openness.html
    sha256: d494d7bf4818cfc9cad4d22e89fc43c4156ee45313550b07d3d5c8f601f6605f
    role: context
  - path: pages/traits/genomics/panoptes_system.html
    sha256: e1d26d32723783868caed568765be39f457242ec5a5d763a0424b1de72851e0a
    role: context
  - path: pages/traits/genomics/paris_system.html
    sha256: 16de7d3191151d929f45aba9673ed2062d0f58b0f1a5b784040b4a84870540d0
    role: context
  - path: pages/traits/genomics/pd_lambda_1_system.html
    sha256: fe017c3fbb612f102f660da9cfcc79d130c6e2778c3b6092a9cf67af4c6c4a09
    role: context
  - path: pages/traits/genomics/pd_lambda_2_system.html
    sha256: ef6865be645a9122534240ac501af328bad290dc2c0f693cf063faf7d31ad42b
    role: context
  - path: pages/traits/genomics/pd_lambda_3_system.html
    sha256: d8fed07574fafc6d548f98e31d9f8a4ddb1112972cd04425d9ae2ae266e08431
    role: context
  - path: pages/traits/genomics/pd_lambda_4_system.html
    sha256: 0d457bdfbc636343b898f0d492b6a4f95fdaa4fa92b13fbe192b2ac287f0ea7f
    role: context
  - path: pages/traits/genomics/pd_lambda_5_system.html
    sha256: dfa1d525cac31ddc5579a9abf3fd68447d5486bf14024a5c4cb5a9624d964d49
    role: context
  - path: pages/traits/genomics/pd_lambda_6_system.html
    sha256: fe09fb42e7c49d8fa286d2caa56b6d406ef4837077945463a73664b5b30b5a08
    role: context
  - path: pages/traits/genomics/pd_t2_1_system.html
    sha256: 798cfb06f030f944de8b6535ef98e7c7f704d2a8733fde8817f7015277b5832a
    role: context
  - path: pages/traits/genomics/pd_t4_10_system.html
    sha256: 48f0a2dc02b09441de3cbe877542dbe77fb1009a3eb348b2a8a6d1ec96c2d35f
    role: context
  - path: pages/traits/genomics/pd_t4_1_system.html
    sha256: aa81e3223cf2317584ca1abd9b68501ff47cff667cc441ac1742f67314caad44
    role: context
  - path: pages/traits/genomics/pd_t4_2_system.html
    sha256: f22bd3645c92a6d0ba6b205c0815f01b5e5844d76241fbecc84cac113f642f16
    role: context
  - path: pages/traits/genomics/pd_t4_3_system.html
    sha256: 1269429941b59d90ea891b9016938e5bbca25966b39756fc6c05310022b3bcd1
    role: context
  - path: pages/traits/genomics/pd_t4_4_system.html
    sha256: f3c69f6772b288c8d1baeaebff598b43ca27a4bfd02b9f10c1875cd45e284b91
    role: context
  - path: pages/traits/genomics/pd_t4_5_system.html
    sha256: 39780c036b1fca81e7f09b2d1a8ee87b1ab2ef5c0f71af95d16236beba6a9c8c
    role: context
  - path: pages/traits/genomics/pd_t4_6_system.html
    sha256: 29eedd6954d769f54a0b21d36d0cc20c4a443baf279cc8047c3f4e5922c94b12
    role: context
  - path: pages/traits/genomics/pd_t4_7_system.html
    sha256: 4f97d9972cd689e218b351037c619197b010a4bf7279bfe8b54433fbbd2f27c8
    role: context
  - path: pages/traits/genomics/pd_t4_8_system.html
    sha256: 14f781a761dd73db420bfadcb1402f22e90dc2d5dfef6993edcf8d365bc69452
    role: context
  - path: pages/traits/genomics/pd_t7_1_system.html
    sha256: 6d35a308607da916a5f2b0c3970f5d5f216e2ff32a3802b639e4ab4e9b301b82
    role: context
  - path: pages/traits/genomics/pd_t7_2_system.html
    sha256: 43ec7b9f8b132cc55562052cabbae949d291877f364176c3d5b2e9c7b22bfeb4
    role: context
  - path: pages/traits/genomics/pd_t7_3_system.html
    sha256: b32e5b1ff83b86119bbc2e3de5ed5c7c578d569b71022a0b3e33735699a6370f
    role: context
  - path: pages/traits/genomics/pd_t7_4_system.html
    sha256: b3d9fcd41ddde92d5255d5658176b2cad40e56688e65cda070ab5ece95bdd1f4
    role: context
  - path: pages/traits/genomics/pd_t7_5_system.html
    sha256: 62ecf4c7427db06bc2495bb0ce8e128b69fe6960efb590fcffd6f843c4ee5ff5
    role: context
  - path: pages/traits/genomics/pfiat_system.html
    sha256: 267585be8903ef1f89434af3f2b4332b87bee332e248db120f72cf3ea386a376
    role: context
  - path: pages/traits/genomics/phage_defense_system.html
    sha256: e76b758bd3b5fe38b3739a45b15c8c32a19e0f3de55bb0b1a1767d0c414802a7
    role: context
  - path: pages/traits/genomics/phosphorothioate_defense_system.html
    sha256: a5eb11fa738e95b8e68ac7c6105dc9b214d14b3951b1bf9b3ddc4f31bb4948a6
    role: context
  - path: pages/traits/genomics/phrann_gp29_gp30_system.html
    sha256: 4f3201a0a0b230d2ce175b6803e46d550df718dbb047f3d54e007b95001941b8
    role: context
  - path: pages/traits/genomics/pif_system.html
    sha256: d5bb1e56b7bfe7bb9cb65f9375e6c4a7cb48cdf999c3aa196f8c6eca73888636
    role: context
  - path: pages/traits/genomics/plasmid_carriage.html
    sha256: 880e6673d364af7a83080a98d77bb245251aa93969ea063954dbbfa78d6962b5
    role: context
  - path: pages/traits/genomics/ploidy.html
    sha256: 66d53de02c227b304844ff15c4b1914a825d8c47721e9d420d8887c628dba231
    role: context
  - path: pages/traits/genomics/prithvi_system.html
    sha256: 9f6ab2da3edf326a478888e4409690ab1ecf105ad5f94a5c2f70b8c7b3570d19
    role: context
  - path: pages/traits/genomics/prometheus_system.html
    sha256: d1842c9cf1df82a19b7e6adf61f36a6bc4150d484e940d805c944b8dd9183cb9
    role: context
  - path: pages/traits/genomics/prophage.html
    sha256: 54997208f60ffa7cb84014ca91d626f1657fffd21c0f9855da23180ee549d7e6
    role: context
  - path: pages/traits/genomics/prrc_system.html
    sha256: 43d1c63c155a9f3dfb3d1f692fc4f3a581f5b3530a911d731af89e104170735d
    role: context
  - path: pages/traits/genomics/psyrta_system.html
    sha256: 339e29af9fdb72f6f323f547e66a90b694089f9848885285ae1c9d9268f8b572
    role: context
  - path: pages/traits/genomics/pvurts1i_system.html
    sha256: 0b9f7ede1f80a643905d3d595106841f816f635a22eacde754d0ffe646284118
    role: context
  - path: pages/traits/genomics/pycsar_system.html
    sha256: 5d62520f813b1a18eb439e054924a4b599757d43f54b1a773794670d9cb0f0d7
    role: context
  - path: pages/traits/genomics/radar_system.html
    sha256: 413be3020b0dcdab1041e302e7192c27937fa172708e82c2b9a690ddffb6ad2a
    role: context
  - path: pages/traits/genomics/razr_system.html
    sha256: 592d8287422dd63e6a23b67aa9f0e6578f70be5bdc52376f250f099f49d6419b
    role: context
  - path: pages/traits/genomics/resolvase_duf5677_system.html
    sha256: 11b8d2474e48407c2a321e7f31c213f6e3b89cd72ab2763e7c959c83edb3abc3
    role: context
  - path: pages/traits/genomics/resolvase_kap_ntpase_system.html
    sha256: 0c8657bc00c1d87dbddbbc9be8d1daa9a5522184170ee5b411a0fbfed45acaab
    role: context
  - path: pages/traits/genomics/resolvase_schlafen_system.html
    sha256: 7137c39a307fa8efc8a04268b1305fff7a3ce6a2e5d849927e6b72ea43dd7c48
    role: context
  - path: pages/traits/genomics/restriction_modification_system.html
    sha256: d74e22848780bba0222e8b9de431e7c85d744a91fbba8240d3b99c610f9484d4
    role: context
  - path: pages/traits/genomics/retron_system.html
    sha256: 8555ea7256c267b9d539faecde052742e06bd196e09b8317262747ea0e66a682
    role: context
  - path: pages/traits/genomics/reve_system.html
    sha256: 4e962ea386fab380de6e1815e67ae31ca76c5967042c3126f3ef3851540c7af1
    role: context
  - path: pages/traits/genomics/rexab_system.html
    sha256: c95404fed2c038bac8805a25b0dbedccf410fc995cee85631bf0733ff51a2ad4
    role: context
  - path: pages/traits/genomics/rhea_system.html
    sha256: d05c58a005e52e2ae95be4d2bc14d642c8064c893b7029f1795f5c230dfb6bc4
    role: context
  - path: pages/traits/genomics/rloc_system.html
    sha256: 1c3c48e2b30dc1d0c945a1b97eed2e39c8a5dfec7b818bebb3f5ab1c861bc551
    role: context
  - path: pages/traits/genomics/rnlab_system.html
    sha256: 6fe8069c6bb13f9ec17c511dd7259d64a521d41c70c4edb6eb701fef3c15fd17
    role: context
  - path: pages/traits/genomics/rosmerta_system.html
    sha256: 212590ed29729f7a5328a8536d3064b12888fc43820ee565c021f9c00dec162c
    role: context
  - path: pages/traits/genomics/rrna_operon_copy_number.html
    sha256: eb62b89b2efd49dff58596bba949f9ecb1dcb1d93febc92dd07385ef0f4a7c54
    role: context
  - path: pages/traits/genomics/rst_2tm_1tm_tir_system.html
    sha256: 14493f006b226c878ae08342a961c3497da5eef6dfa5c64902c0794d31fc6196
    role: context
  - path: pages/traits/genomics/rst_3hp_system.html
    sha256: 268d587e0b70beabcf152f5f3ec858f1a34280b51158adbd6b6bcf5d71013422
    role: context
  - path: pages/traits/genomics/rst_duf4238_system.html
    sha256: 1eb76c9c780efb5ea5169affaee767431e80471573962a13a9f804dd9dad309a
    role: context
  - path: pages/traits/genomics/rst_gop_beta_cll_system.html
    sha256: 20768838b90bdb58c3274935ffdbf5e4c361f53e5f8fca0bd32cab466c6fab6a
    role: context
  - path: pages/traits/genomics/rst_helicaseduf2290_system.html
    sha256: cd92e263c5344e037b34c681e563d6e6bdabd461ba57f97f5177062dcb96bea0
    role: context
  - path: pages/traits/genomics/rst_hydrolase_3tm_system.html
    sha256: b76dce80b1419d413bbd82321435e7e458496d8384a1d19aaad144b56a1d64a4
    role: context
  - path: pages/traits/genomics/rst_rt_nitrilase_tm_system.html
    sha256: 7844f78ab1dfa5a3a4ccba772784248a54e2042ada35b5b27f977c7cf77e58da
    role: context
  - path: pages/traits/genomics/rst_tir_nlr_system.html
    sha256: 6a42ec5c7eb594b96451f13d573c5d2f7d4e6d2e8609cbea17681caaabd80868
    role: context
  - path: pages/traits/genomics/rugutis_system.html
    sha256: 810896c1c867d0f35d999515dcff4db7ea6ec85bb323c498df4a05f9e50cda28
    role: context
  - path: pages/traits/genomics/sanata_system.html
    sha256: 3156534f72b107fac20a11cf2840da5f76f2f1c0fb1061cff15abedcb45481c6
    role: context
  - path: pages/traits/genomics/scomcra_system.html
    sha256: ec7d2cac0eab495814771272ae0eb7e88f5665ea762334d13bd555bfaa24c81f
    role: context
  - path: pages/traits/genomics/sdic1_system.html
    sha256: f0ac7e037e1b94210d898895e3b361efb2d72ee341340ddf1dc0b4e6be490d95
    role: context
  - path: pages/traits/genomics/sdic3_system.html
    sha256: 5410bca823a2ac3209f55e1a633dfbdc077f4eeccf4028712c2ed502bbaca911
    role: context
  - path: pages/traits/genomics/sdic4_system.html
    sha256: 7b6dd08e12b8393c3b93185fca779dfd26d5c0d49f7c8a9468d406dc99fc8676
    role: context
  - path: pages/traits/genomics/sefir_system.html
    sha256: e193667a5ebd8755f722766e91d6bdc6d632f661f72ea896ed1dc8c286b0f800
    role: context
  - path: pages/traits/genomics/septu_system.html
    sha256: 23cc23ce76394816cf5133579d104c558005196d0a0f93e282f83c4ef4512c37
    role: context
  - path: pages/traits/genomics/shango_system.html
    sha256: 06558febd3c4f60f6b74184792ced9a91e3ba2becc55a10651505841caa0cbf9
    role: context
  - path: pages/traits/genomics/shedu_system.html
    sha256: a12a4a62d595ea00d6a9e23a15f10caef5ef0e889023171b887a3a2a45532d89
    role: context
  - path: pages/traits/genomics/short_lamassu_system.html
    sha256: 34d42a3928c1806ca21c8d9a95111e151e43673c464d814923a883ac1664e14d
    role: context
  - path: pages/traits/genomics/shosta_system.html
    sha256: 29d8fab5fcdf9877d66a4da3bb25ddace6178c5da0e935c6157ed754cfa7eb16
    role: context
  - path: pages/traits/genomics/sirona_system.html
    sha256: 81c51f2574c5b44643fba4f3ebf73952ab49e135e6ee6f6d120352b6848f9c17
    role: context
  - path: pages/traits/genomics/six_a_mbl_system.html
    sha256: 396b5dff132d9a8c181d93673dee9a813ce7429fe26021846136da1e5e635313
    role: context
  - path: pages/traits/genomics/snipe_system.html
    sha256: 9a00eab1d0c68331253b02d8366ad025179b3c40482c663a10c42f4af92eb07a
    role: context
  - path: pages/traits/genomics/sofic_system.html
    sha256: b6cbbee4df31def453f5d2807237586a9e439e5a6b7dbec827692a7ed21915b2
    role: context
  - path: pages/traits/genomics/sparta_system.html
    sha256: 4242f1ada5054061ccba0cc3c2043d09f8c8895a95be83abc080ef63cb6a6675
    role: context
  - path: pages/traits/genomics/spbk_system.html
    sha256: 743dca4b92708c51f98f87762ec6442f1201135cf8417f529e77061c54199fc6
    role: context
  - path: pages/traits/genomics/sspabcd_sspe_system.html
    sha256: 0e7927fba851223549fd0d69a89e887d30fda9f3aa2e44e4d34fe74d759cf277
    role: context
  - path: pages/traits/genomics/sspabcd_sspfgh_system.html
    sha256: ebb89013de204e3e59dbe05ee5198dc2313a776b4c1612991142b226b057406f
    role: context
  - path: pages/traits/genomics/stk2_system.html
    sha256: 01e529f6c8f59bea7240dd8f11fcd0ef3669b56365116cef4884b8610e35f80f
    role: context
  - path: pages/traits/genomics/sucellos_system.html
    sha256: 0562b7da8f0738b4662171a543f59b63904dd6e4423632c20ab6e3f69570afc7
    role: context
  - path: pages/traits/genomics/tab_system.html
    sha256: d9178c6e2ea4debaf98710b7184f4f3cbdd001fa28f4e55f0205328215c24d09
    role: context
  - path: pages/traits/genomics/tagi_system.html
    sha256: 80c116387526303823372cb84eec69f88ffa8e9e65cb98bb993ce6ed15832df9
    role: context
  - path: pages/traits/genomics/taranis_system.html
    sha256: de58101c586bb036b9eb30edfb2536e205d00c88f6f28b0d7e418756f161e7e3
    role: context
  - path: pages/traits/genomics/tgvab_system.html
    sha256: 69dde35654f70cf59f6692c24c418e964bc5dc7f3528aef82ff75ed4dea75be1
    role: context
  - path: pages/traits/genomics/tha_system.html
    sha256: ec9c7d1a4f8e64516dfc59fc6103d20f284555bd8e46a66ce4056ee29e10598e
    role: context
  - path: pages/traits/genomics/thoeris_system.html
    sha256: a7674b8f76e8ecb0ecb0efad165162c36257297432d45efb439727696b3d3f4f
    role: context
  - path: pages/traits/genomics/tiamat_system.html
    sha256: 96aab32ca0492e0d3f63df7658e420e5b9ae573332269c2ddec06686a26731aa
    role: context
  - path: pages/traits/genomics/tir_i_system.html
    sha256: ec255ea994e4025607a6a82e3d1bb31d584d6e5c392586fc269ced3281a3cf8a
    role: context
  - path: pages/traits/genomics/tir_iii_system.html
    sha256: 25fae590eb097fb8a585da2e05f54200ed4036471e0a1e6f1033341f076a357a
    role: context
  - path: pages/traits/genomics/tir_iv_system.html
    sha256: 32bb2ca922952bd97eaf5d0d703b15230ed9669527dddfcaef71a73b1739352e
    role: context
  - path: pages/traits/genomics/tir_vii_system.html
    sha256: bbb5ab2362b0589cdf549f0be9a4b997b3f5e2476e03051112c4dd80e66e7034
    role: context
  - path: pages/traits/genomics/tir_viii_system.html
    sha256: 977d3835bac5047e6133061f0ab0359ebe666a3d498cf29fa3760e0d56846b47
    role: context
  - path: pages/traits/genomics/toga_system.html
    sha256: 1287923554a28cee1e9d1e220007d64d3e73889459fc96a46c979043c67bb808
    role: context
  - path: pages/traits/genomics/toutatis_system.html
    sha256: 2a62bce36092b9f402002deb8fb1e1e7a6f8b0182be3444872c3f8ed2daf389d
    role: context
  - path: pages/traits/genomics/toxin_system.html
    sha256: 74f3aea5d1c7bc714f9778501b8aa12461d3576b1b0d41731ad6ad7e5ba6da48
    role: context
  - path: pages/traits/genomics/transposable_element.html
    sha256: f1dbc61c05cdb047aeafe5872ad38c9b443b84d25e281fb6f4595e770b190541
    role: context
  - path: pages/traits/genomics/type_i_restriction_modification_system.html
    sha256: 96be90784ec3ba5f7a85ae5d2d50300f6cf39d36c019dfef99234a045c9e2229
    role: context
  - path: pages/traits/genomics/type_ii_restriction_modification_system.html
    sha256: 2e3c0fe2bd53b05d4eea4f322318a922cbfb5984a7d83113a9bf6f4c2943c985
    role: context
  - path: pages/traits/genomics/type_iig_restriction_modification_system.html
    sha256: 4cb087c458386b2d21f57c10cab9904417dc27125340ae6e5be6f82151b2181a
    role: context
  - path: pages/traits/genomics/type_iii_restriction_modification_system.html
    sha256: e08d7e43b84a02a17e4443ae2a600ef24983794b8d41c726b3a5aefb22cebf6b
    role: context
  - path: pages/traits/genomics/type_iv_modification_dependent_restriction_system.html
    sha256: bda7b8f53b67729a17e40c658e1cff0c11b61181ae36e8499e2409918c44077c
    role: context
  - path: pages/traits/genomics/ukko_system.html
    sha256: 61a8dfb1d879be00647e733aaaa6a068435426ee71845b551b4791794397692d
    role: context
  - path: pages/traits/genomics/uzume_system.html
    sha256: 8ba3721d34d1f351c2b36f85350ccca7d53cb3a5f6e6f19301dad1cab1717202
    role: context
  - path: pages/traits/genomics/vcam4i_system.html
    sha256: 5b93d2f8f72a61b3838546dede72ce6c8a3666a87efecf9ce5ad3d2225da8b26
    role: context
  - path: pages/traits/genomics/veles_system.html
    sha256: 7f50839d750d8bedfc251f719357a9981483bf63f333c0b79c70397aa12ddf3c
    role: context
  - path: pages/traits/genomics/viperin_system.html
    sha256: 261febcefc3f211d5d809a05b70a8ac1302f0fdfc044048e521029fcebc70ec9
    role: context
  - path: pages/traits/genomics/vp1796_system.html
    sha256: 9b195aa25604426bd4bdb897cc90c68fecb2854af2b3b1ed2775e7d3377d532f
    role: context
  - path: pages/traits/genomics/vp1817_system.html
    sha256: 44cb09aa66bdfd9cb267365678de9cbc4864e370e40e2d63a4279335affca17b
    role: context
  - path: pages/traits/genomics/vp1823_system.html
    sha256: 2ca39a8c288c3c1307508f3e2d23d8dd008f8fdb9c992d544b53cec86a9d4414
    role: context
  - path: pages/traits/genomics/vp1826_system.html
    sha256: 859c5ceeef720e19b101110e2ceca8d86f6a45dece659e18bf1b2281866a8fad
    role: context
  - path: pages/traits/genomics/vp1839_system.html
    sha256: b410cee8cdd9e32dc6f1623e42cee52f886cc82b23d82db8d34a8de2f3c8ea93
    role: context
  - path: pages/traits/genomics/vp1840_system.html
    sha256: 01601ac22158f8959b20137a2cded003d5c32e5645962068417663e15dd6318a
    role: context
  - path: pages/traits/genomics/vp1848_system.html
    sha256: 5dedfa7bee0955bd57a563a08b00ff0d7965ca1409d46320c705135a05492d76
    role: context
  - path: pages/traits/genomics/vp1851_system.html
    sha256: 459e2f418caf5b25c0929c07abbb5a2c682daa906b20d47b5e38f2cc8d8fa9b9
    role: context
  - path: pages/traits/genomics/vp1853_system.html
    sha256: 75bdd71f02bea961ac784f7714d390b67ecf79c6105b4b64358297ad5c2d6a6f
    role: context
  - path: pages/traits/genomics/wadjet_system.html
    sha256: 06590acb518dee8961019c10c81c29b0164480453e9d53f9521fb48c330b4216
    role: context
  - path: pages/traits/genomics/zorya_system.html
    sha256: b92afc43e5de72760ff0ee1e9b699df8978a5c77f6fa918c4a2baf99ccd96492
    role: context
  - path: pages/traits/genomics/zorya_type_i_system.html
    sha256: c39d2809027449dec156d8ea75a9072d0f3e01d29f186be0db4f8930ddb6fea3
    role: context
  - path: pages/traits/genomics/zorya_type_ii_system.html
    sha256: 730ddae4fc353e957632b7fa80b75d18a87544ca57b0d06ce69fd08d4635a02e
    role: context
  - path: pages/traits/genomics/zorya_type_iii_system.html
    sha256: 742b3ab9065fa8a543e2c16d5a91735f772916639d2442e5bfd54a0f888787d7
    role: context
  - path: pages/traits/metabolism/accumulates.html
    sha256: 5bbaab27cc9cd2889d5c245f49b898c6bb117fbd204d691f5bee63181d2764aa
    role: context
  - path: pages/traits/metabolism/acetoclastic_methanogenesis.html
    sha256: f05942a7ea494c46c1bfcc60f7668eaca27e17613b180b1a7f8ca36d5bb5a18d
    role: context
  - path: pages/traits/metabolism/acetogenesis.html
    sha256: 3e5383dee6709fab6ff675ba471a79d59757463e07b758e7f1134575dffe7a3b
    role: context
  - path: pages/traits/metabolism/acetone_butanol_ethanol_fermentation.html
    sha256: f6bce0cad440ab633cef4569e91d58fbf7c95ed1291b618922d544e9d110203c
    role: context
  - path: pages/traits/metabolism/aerobic_respiration.html
    sha256: 5fc81aabf08bb2875f26e756e8c644619705d6216b098d0c68466bfd6ff65d1e
    role: context
  - path: pages/traits/metabolism/anaerobic_ammonium_oxidation.html
    sha256: a56671cec1cf98d456da038b51d6eb08e2cd11dc1229564c42672f0980af4461
    role: context
  - path: pages/traits/metabolism/anaerobic_oxidation_of_methane.html
    sha256: d8dcd81402fa7bfd80a105aa2df8cc8489b28a4a818162b4d7f7b0bdf0d43eaf
    role: context
  - path: pages/traits/metabolism/anaerobic_respiration.html
    sha256: 6819ae559ab0e2e6bbfd1b4bb6c328772346dec6dc621136319046dd5539dec1
    role: context
  - path: pages/traits/metabolism/anoxygenic_photosynthesis.html
    sha256: f1bf1d29a99ea20bec15da1447856f75fb1aeeaca7e3a86561052cd41b31ae2c
    role: context
  - path: pages/traits/metabolism/aromatic_compound_degradation.html
    sha256: 2ad74e904d846409f881e6b42b6a97c971702260f4342454d3fa75529a4b5045
    role: context
  - path: pages/traits/metabolism/aromatic_hydrocarbon_degradation.html
    sha256: c36b402827e5e6f9f09a6fa6e3fa6f526137c56a18eb812def8d0de4011bac57
    role: context
  - path: pages/traits/metabolism/arsenate_respiration.html
    sha256: 5f03b182990c1cc981071c5281a1208dc2d5e86abbc2d30c7d3490d171282f8b
    role: context
  - path: pages/traits/metabolism/arsenite_oxidation.html
    sha256: 7c5bc080cd68a32db871282901ece5419d94d8f98af1a146cf2531cb3cfe8e72
    role: context
  - path: pages/traits/metabolism/assimilates.html
    sha256: 78e9e8442828e482cd25c5aa340eeced6230e2d19d9b6f5f9ec7e0ffd4c9501f
    role: context
  - path: pages/traits/metabolism/biopolymer_degradation.html
    sha256: e855944747cd30dd08807d8fb2e0cdcd44b8702015143b80df48848bb2396ddb
    role: context
  - path: pages/traits/metabolism/builds_acid_from.html
    sha256: 066bd855779ab3d52bd36ee5e0bd9332563cd6564b5b462d40b57982e05c04cb
    role: context
  - path: pages/traits/metabolism/builds_base_from.html
    sha256: 6c089a6607762fe5c19db9bc5504c59eaec26c6211dc995f7be8af538d56cf2e
    role: context
  - path: pages/traits/metabolism/builds_gas_from.html
    sha256: 1bf2c597da40b3d647e87451e4385c5aeb8758bb792d5a5bc398cf8816828688
    role: context
  - path: pages/traits/metabolism/butanediol_fermentation.html
    sha256: 326148e49c186a4d5c0af02570fe63edb62e09f68940e8fcd8b4babb294b1394
    role: context
  - path: pages/traits/metabolism/butyric_acid_fermentation.html
    sha256: b7f683213d715649fb24b571f94761dfa7f74fe18955d4e1370049867f840e17
    role: context
  - path: pages/traits/metabolism/cable_bacteria_metabolism.html
    sha256: 80668652d176c67aad4cf220b0e7e34c6d9449016b7cea42443457a3c703032d
    role: context
  - path: pages/traits/metabolism/calvin_benson_bassham_cycle.html
    sha256: 38e84b4625023fd40bdc21a9ce3644b86e11fac3ddf733e02b79af11e74a46cb
    role: context
  - path: pages/traits/metabolism/capable_of.html
    sha256: be69333102a6e632dc129eea0aa192f179905e3e274abd72a02170e46bb5176a
    role: context
  - path: pages/traits/metabolism/carbon_fixation.html
    sha256: 114e219a4deb5718bb76bd2ea85794870b83e5644596d92b51d879c2c4ca4e81
    role: context
  - path: pages/traits/metabolism/cellulolysis.html
    sha256: b7871c3ff5f9077065ab3e66d54c114bd806cb69a05eba08cbb9c81e724e8b8d
    role: context
  - path: pages/traits/metabolism/chitinolysis.html
    sha256: 789f182a845b822749f6e880f04facb1b8060b3b672d6eb33ab4c81301606508
    role: context
  - path: pages/traits/metabolism/chlorate_respiration.html
    sha256: c5937819a2bce21038f0701c4f7ea6705a6651dc9b41a202ac3ad2c8838576cb
    role: context
  - path: pages/traits/metabolism/citrate_fermentation.html
    sha256: 50a0f0369bba493b6f41e46868827c00d8117d94f9e2086cf1670bbf56526879
    role: context
  - path: pages/traits/metabolism/compartmentalizes.html
    sha256: c97d6ce861d2c3e9f1f257d5d4c18aaa8cc09348bbdd33861350473628336cab
    role: context
  - path: pages/traits/metabolism/complete_ammonia_oxidation.html
    sha256: fb46829d269cadbcc0f44c244be1d0669fa79584d3582c775070f5d0f9d83a5b
    role: context
  - path: pages/traits/metabolism/dark_hydrogen_oxidation.html
    sha256: e3935607fa44e30dd3cb953c13f7845f8e5d2653ba5e6cf8f4f5d390eb2f99ba
    role: context
  - path: pages/traits/metabolism/dark_oxidation_of_sulfur_compounds.html
    sha256: ca21fd17b35254d595c5c0d49199fb1309eed82491cf855e046ab748a9873e71
    role: context
  - path: pages/traits/metabolism/degrades.html
    sha256: e37bc166d97d8b9126bc1c264ec13f00ab1b6313e5fcd6eabe22639bd36e8e4d
    role: context
  - path: pages/traits/metabolism/denitrification.html
    sha256: c9b2fe57e6dcdc706a390ad72a056a1e64ab7b9f49664567fe748b3cc0cf6a95
    role: context
  - path: pages/traits/metabolism/dicarboxylate_four_hydroxybutyrate_cycle.html
    sha256: 7cdc570b9d65319fa5202d71d0be85c7d19710ff354376fb1bb773b5d8d5d648
    role: context
  - path: pages/traits/metabolism/dimethyl_sulfoxide_respiration.html
    sha256: 7cd70792d3e694527c93659c03c25d8fb3b1ef0da43b388b5d4323beea10d934
    role: context
  - path: pages/traits/metabolism/disproportionates.html
    sha256: f202bf9d061292928e757d58abe4bf7374df8fe807dd0015b4d6c0a80343dcb6
    role: context
  - path: pages/traits/metabolism/disproportionation.html
    sha256: 28fb6990d12e54eef9193f5f112a41d8bcfcedb29318d87e94cf7533533c373c
    role: context
  - path: pages/traits/metabolism/dissimilatory_iron_reduction.html
    sha256: 2ab2aeab322e43a8ffff91faa1d4fbc0442449d384c9cfd8c99fc7033c9ab639
    role: context
  - path: pages/traits/metabolism/dissimilatory_manganese_reduction.html
    sha256: 9baab621ec3093ee9469e635a7bfdafbf4780280137c4e90a14214fec17a9b4d
    role: context
  - path: pages/traits/metabolism/dissimilatory_metal_reduction.html
    sha256: a65ca336aa749441dae331a475295e43164e461f1118f4107e058776818f0c15
    role: context
  - path: pages/traits/metabolism/dissimilatory_nitrate_reduction_to_ammonium.html
    sha256: e9fda2550afc922794ea8e0547016ad09d87d586b3dd0aefe356a67b205ad89a
    role: context
  - path: pages/traits/metabolism/dissimilatory_sulfate_reduction.html
    sha256: 1b260e5961d84481fdc31484e4b5234399b49050d86233a9032a0265dc43434d
    role: context
  - path: pages/traits/metabolism/does_not_accumulate.html
    sha256: 4f8679875e58dad5c498f69ac4b892618353b592b7fdb41911c43eea639a7eb5
    role: context
  - path: pages/traits/metabolism/does_not_assimilate.html
    sha256: a71219c3b73b3965054d41021d2aef7b177b9fc12f9d4d937f730b78f023f04b
    role: context
  - path: pages/traits/metabolism/does_not_build_acid_from.html
    sha256: c219e8c9868d64876a84e58f158579c9673338bab1188be5c3a9c933589036ec
    role: context
  - path: pages/traits/metabolism/does_not_build_base_from.html
    sha256: a0cd333af7a248c7cbb668937d1870930be8e5072cbab58432cc58b3532dca3b
    role: context
  - path: pages/traits/metabolism/does_not_build_gas_from.html
    sha256: 928e958d72795150055dd90c5dfad9434e46de2bb68fedbe36ad4fa643331695
    role: context
  - path: pages/traits/metabolism/does_not_compartmentalize.html
    sha256: 6a13f71eef3b806f4cac8306ca6431bb240999cd14e939046f2d9e6a59258462
    role: context
  - path: pages/traits/metabolism/does_not_degrade.html
    sha256: 48d0e1ae0dae9cdf67b8e09b53e8e6e954e9bff08cb4db8da698cea93792c8e5
    role: context
  - path: pages/traits/metabolism/does_not_disproportionate.html
    sha256: f91599cd641b2b1812a8fedff1a345590229de145a5c8c26bdb207b3c0eb4d65
    role: context
  - path: pages/traits/metabolism/does_not_export.html
    sha256: 9c770d00e19cfecfe15b7177ca37355f2bd0479fd1602201bfbffb0b8d843d33
    role: context
  - path: pages/traits/metabolism/does_not_ferment.html
    sha256: 3495cc0fea4d81f0be01c14479f73a0e93adb90e4429bd1afc262296b25b440d
    role: context
  - path: pages/traits/metabolism/does_not_hydrolyze.html
    sha256: 60d2cf1a80349df7175a048163d5e29881341852239fcb5b34de67eac13aa1f6
    role: context
  - path: pages/traits/metabolism/does_not_import.html
    sha256: 5a8d47f09ef1def0bd039895a367ece839527ca9253e9ce9caa7c2487d4b4a4f
    role: context
  - path: pages/traits/metabolism/does_not_oxidize.html
    sha256: e3edc1243ce7440f793163e227aa417e6d70970a736ba6a158d275a46420accd
    role: context
  - path: pages/traits/metabolism/does_not_produce.html
    sha256: f2688848b571811643422ceb5da4a0a609262690fb73bb3eb436a1c9e72636d7
    role: context
  - path: pages/traits/metabolism/does_not_reduce.html
    sha256: ced729c07b735487499a34a6c945689877893eae7b2ae53370fa14760d444207
    role: context
  - path: pages/traits/metabolism/does_not_sequester.html
    sha256: 2297b07376c0b72a9a6e26f42420c57fa9c2ed472a228a316d0cfacabac4c16b
    role: context
  - path: pages/traits/metabolism/does_not_show_activity_of.html
    sha256: 61be290ec033a2fba2b94fd01f6a9bcbccbea248ed77c314ec4386774cabf616
    role: context
  - path: pages/traits/metabolism/does_not_transport.html
    sha256: 751c26bd9322301ae787079fad8b2d8a47eff960f49ad229e31ebe379b73f2b0
    role: context
  - path: pages/traits/metabolism/does_not_use_as_carbon_source.html
    sha256: f230a82e3772075047ba9b5b6e4f047c74ab7a7621bd31a9427112e3ba4cd9e5
    role: context
  - path: pages/traits/metabolism/does_not_use_as_electron_acceptor.html
    sha256: 0eda4009e5a0abba82e1a9f19c6793a5b6b31e31b12bc04f62d3f13edcdce690
    role: context
  - path: pages/traits/metabolism/does_not_use_as_electron_donor.html
    sha256: 1d8ecb8885afff5a8dec9f6db1f565d2784dd05d94d2a5376dff94e144b98a78
    role: context
  - path: pages/traits/metabolism/does_not_use_as_energy_source.html
    sha256: 2a4991f8e018989ad0c5b910ed9df2fd84348436247675f8b49a7eab3e2c30eb
    role: context
  - path: pages/traits/metabolism/does_not_use_as_nitrogen_source.html
    sha256: cdd401a7a70cb1ffbcafdb612edea164e9748e63926c607cf86c272bb8e99053
    role: context
  - path: pages/traits/metabolism/does_not_use_as_sulfur_source.html
    sha256: 86f0b5a67084f33adb174a1293d029fb82d863db9c057831ffe2ef3b81c4bd05
    role: context
  - path: pages/traits/metabolism/does_not_use_for_aerobic_catabolization.html
    sha256: fc9f7f4f383709213bd67bf68801dbc701a347d4b8a32afa7dac401e089c2960
    role: context
  - path: pages/traits/metabolism/does_not_use_for_aerobic_growth.html
    sha256: 79ed6c3c672136d5433e12f82f21d885f7e032caed7041618babdb71e2e79253
    role: context
  - path: pages/traits/metabolism/does_not_use_for_anaerobic_catabolization.html
    sha256: b83b5dd8edd09a7fd0b58529dd802232f233c0b0f32c02e564302867b61b1ebd
    role: context
  - path: pages/traits/metabolism/does_not_use_for_anaerobic_growth.html
    sha256: 441e150b014dd06053e24b4074a821316e4e745b28fb7b368d0da3eff3c2aee6
    role: context
  - path: pages/traits/metabolism/does_not_use_for_anaerobic_growth_in_the_dark.html
    sha256: 20b6d9e23e958548ac506842bcbb0d18ec391468270d06147a135f79e8a07fbf
    role: context
  - path: pages/traits/metabolism/does_not_use_for_anaerobic_growth_with_light.html
    sha256: d3cecee946ddcbdbe888dec57a67428bbcef38ff97fb5a0f78f67be430dec8a4
    role: context
  - path: pages/traits/metabolism/does_not_use_for_growth.html
    sha256: d399f00f9c2903df38cdaefc62f22e972b36591b710c79b1531998cae7c206b2
    role: context
  - path: pages/traits/metabolism/does_not_use_for_respiration.html
    sha256: e440e910ff9f1112b6553888c6bc36bfc8aee880846bcfb7e4d18b36095dbfcc
    role: context
  - path: pages/traits/metabolism/does_not_use_in_other_way.html
    sha256: dd6084f195e305db4ca51e5fa4bb9e665c9190e0a128618f6d3ddeaf56eaf134
    role: context
  - path: pages/traits/metabolism/electron_transfer.html
    sha256: bca59f3e8052522e927e3ea8b425467c07a8eec55b1bdfecb4e96b9dc1725894
    role: context
  - path: pages/traits/metabolism/enzyme_activity_analyzed.html
    sha256: 81683f1dd234d9732ada2d26392f99b037e0125f7f3b6978716e729a433a506a
    role: context
  - path: pages/traits/metabolism/ethanol_fermentation.html
    sha256: b62b1355bcf0db3ffe6641d97e460f5e4122452ea4e7223f44db59fc7b03edf1
    role: context
  - path: pages/traits/metabolism/exports.html
    sha256: 44d0cb511508b41362cfa33a559451b7a969ccffb9791a974f023a36251e06ef
    role: context
  - path: pages/traits/metabolism/fermentation.html
    sha256: b7f97af869d8fa6a3db5156caf384c94a88486fce67299c26cb232616abed1e0
    role: context
  - path: pages/traits/metabolism/fermentative_hydrogen_production.html
    sha256: d91763686fe315ddeaa684f6474767e6736487b529d613564b4fb8a2f5630422
    role: context
  - path: pages/traits/metabolism/ferments.html
    sha256: 6ab50b0e2d96be69f0ca680e7a962647006d66e0b18172b7143d7128468b17c4
    role: context
  - path: pages/traits/metabolism/fumarate_respiration.html
    sha256: 6583640845d1f485cd1ea271eae75ad2dfbd9993c76cc3cd5855563b0a5f523a
    role: context
  - path: pages/traits/metabolism/has_growth_nacl_observation.html
    sha256: f430e57e55cc991d568da8a4dc1250bbc67c8dc63eeacede6e8ae22e2cf96521
    role: context
  - path: pages/traits/metabolism/has_growth_oxygen_observation.html
    sha256: d21831f061663c8c0ca92b516daadb619520f50c77a655c8d5ffcec81af36d83
    role: context
  - path: pages/traits/metabolism/has_growth_ph_observation.html
    sha256: f5d6e296eb26975017076f27116ffec29070ebe0ecb18c7b9a02468742fff393
    role: context
  - path: pages/traits/metabolism/has_growth_temperature_observation.html
    sha256: 072fc0780fb3cea4b49902aa2774cb0c6f92867b5223aad010140b6d601e6689
    role: context
  - path: pages/traits/metabolism/has_nacl_delta_observation.html
    sha256: 341a3d62e8cfa1b3eef05994f2569db1ba682ee6f4931c67427513452b4093fe
    role: context
  - path: pages/traits/metabolism/has_nacl_observation.html
    sha256: 2499891238c308c20cfe3e3060f5361787b6dc1fd7ea957dbaf2a53e6348f42a
    role: context
  - path: pages/traits/metabolism/has_observation.html
    sha256: 4cf3ab3a87db45a4d693ba2650663fb5926c57144087edf91d692538ef25713e
    role: context
  - path: pages/traits/metabolism/has_optimum_nacl_observation.html
    sha256: 1b06a1f33ef37ed54e90c281e5433f753b2b3c335c5c5f3c4f4bf7bcf4ea52ec
    role: context
  - path: pages/traits/metabolism/has_optimum_oxygen_observation.html
    sha256: a49fb39327c6ee62487a20e6a2a31438f2ecf88fa1e36ef952048978df88ad29
    role: context
  - path: pages/traits/metabolism/has_optimum_ph_observation.html
    sha256: d63487bf39b48887c3b4d0d7a108a941e97aa9a3ba33df93f3f7e7f3ce56e771
    role: context
  - path: pages/traits/metabolism/has_optimum_temperature_observation.html
    sha256: 36d40166d8df3428b29c7c999bc69be474b2458807fd03ef239db9c026afbfc2
    role: context
  - path: pages/traits/metabolism/has_oxygen_delta_observation.html
    sha256: 0c703d138bc248de579a6986e383676150bef538e6350b3ea4e1d7e89b2d97e9
    role: context
  - path: pages/traits/metabolism/has_oxygen_observation.html
    sha256: fde3275341b93ba8dbbfe485873920385e604f537cbf6b1a4516d7bd824fbfdc
    role: context
  - path: pages/traits/metabolism/has_ph_delta_observation.html
    sha256: 3fb9ccaa047123d5379e3c6c78e71ecb83a3601b0dba7ce811f3a165f9092c99
    role: context
  - path: pages/traits/metabolism/has_ph_observation.html
    sha256: 9aace8591c856a2b2f071ac57df253873ec7dfb8d06da2fd38d0295a32a0e3ab
    role: context
  - path: pages/traits/metabolism/has_phenotype.html
    sha256: edb3047aab430af1c336c8d373d5498a1b57db43785ea66c05c15f6ddf12961b
    role: context
  - path: pages/traits/metabolism/has_quality.html
    sha256: 9219aeec52712e3e33c26671bb75bd383ae4285cf2a54b56921e059b8a1d0225
    role: context
  - path: pages/traits/metabolism/has_range_nacl_observation.html
    sha256: e0bcf89613f7aef220fa264c79fb0828298738d70af452cef56b049c11b701ba
    role: context
  - path: pages/traits/metabolism/has_range_oxygen_observation.html
    sha256: ee514a65171f081116b09c8f1fbae34d0431ba5cf476ba23771bd75bfdf3377b
    role: context
  - path: pages/traits/metabolism/has_range_ph_observation.html
    sha256: f6a07c305c019e1c511a04f0321eeeadaf17a7af6cb99312a10931d47d218322
    role: context
  - path: pages/traits/metabolism/has_range_temperature_observation.html
    sha256: a001374969ff7181daa459a3a74cf3a6604215b6a8cb05558e46ee5f5c1befe5
    role: context
  - path: pages/traits/metabolism/has_temperature_delta_observation.html
    sha256: 08a46264e8863daa8ea042cf5eedb49e1bbf83d5376141b97768fbf6b16294be
    role: context
  - path: pages/traits/metabolism/has_temperature_observation.html
    sha256: 431506ced2b2efd2510a96c0fa022f0021be0536fae19795d7dbde135fcae6c5
    role: context
  - path: pages/traits/metabolism/homoacetogenesis.html
    sha256: e1204b17f21eec2b6a52b5cb0a527a72714354b9b257067b1b6b330d5856d8e7
    role: context
  - path: pages/traits/metabolism/hydrocarbon_degradation.html
    sha256: be8cc09d5cd6fed63b5544598f5242f409c30853af4a0068f5b5d663671c0180
    role: context
  - path: pages/traits/metabolism/hydrogenotrophic_methanogenesis.html
    sha256: 4a49578ca9fb3c34cb641aa1c072634969979bd8b94155b050381b98f105c4d0
    role: context
  - path: pages/traits/metabolism/hydrolyzes.html
    sha256: 243db310774120a18312f2dd35ff7e515e23e6e450a443005c4c7cb979594fcd
    role: context
  - path: pages/traits/metabolism/imports.html
    sha256: f19a60fc2a21691eaa1ee780dffe3597f66cba4a9830ce71633c157223b17db8
    role: context
  - path: pages/traits/metabolism/iodate_respiration.html
    sha256: 73190724c07315c44ede27fddb502e3ae5ce36859e7fceb4d8fd7c315afce641
    role: context
  - path: pages/traits/metabolism/iron_oxidation.html
    sha256: 93b4659b8f46cdf5ab35c7638643b7b8daf3f0cd388efc16f2e73dd893c442a4
    role: context
  - path: pages/traits/metabolism/is_not_required_for_growth.html
    sha256: 41d7de466664c32b92a79ca9303254473efebda03b47899411a4971ed79b7618
    role: context
  - path: pages/traits/metabolism/lactic_acid_fermentation.html
    sha256: 813928d8fdf481999f5bff5c20c6b018b3538512be29f3ac37a5628178644aaf
    role: context
  - path: pages/traits/metabolism/lignin_degradation.html
    sha256: 83c7f265f92b5823a26a71b1504a887f49140084bd30ce5e109a7d1f905b4fe4
    role: context
  - path: pages/traits/metabolism/lipolysis.html
    sha256: f1f7c0b16ad56439d06ee3ce1d9e42fb17348bccdb64acf4d76cef7a97be678a
    role: context
  - path: pages/traits/metabolism/manganese_oxidation.html
    sha256: e16da07ec4167c7f6cc64bc51333cc11b64a741abcf3eab4d13ec3a8006f9313
    role: context
  - path: pages/traits/metabolism/metabolism.html
    sha256: d91b12d6e7464826ae897e75ae31048fc8c2ba485833fe7ff4288d198c882e41
    role: context
  - path: pages/traits/metabolism/methanogenesis.html
    sha256: 6d1c4b1d65d06c85d6038a0fbd6dc98b3b120b4153938ecc6d94d0efe8c69f8b
    role: context
  - path: pages/traits/metabolism/methanol_oxidation.html
    sha256: 963cc2954919708b34f2cb231f2f446d5f87d1e91c5546e5bdb20744ac361965
    role: context
  - path: pages/traits/metabolism/methyl_based_methanogenesis.html
    sha256: 0f5df077fa3944054e67692a6e0bd389a757c933a3f3b5c66908d3ead19bfbc8
    role: context
  - path: pages/traits/metabolism/mixed_acid_fermentation.html
    sha256: 9d433b70a491571663e5ee93d9804da1f1bf5646ac1a597ee77da168081d2034
    role: context
  - path: pages/traits/metabolism/nitrate_reduction.html
    sha256: 97a3c836dfcaf42641c9295fb55431b135f0a6185a19a91a417a22e3bf215584
    role: context
  - path: pages/traits/metabolism/nitrate_respiration.html
    sha256: 9a8563310f8db2f3b53566b2af76c4a72e9cf8834e21fc24118b204ff2787ad9
    role: context
  - path: pages/traits/metabolism/nitrification.html
    sha256: 7a6d66268d9a4dd7547f0dc047f67590c3b0056ce87f8e1a129d3421d2e0fbea
    role: context
  - path: pages/traits/metabolism/nitrite_respiration.html
    sha256: 4739b0755a1618dc234ea62bf68d1aa961250837244537798758309b1d3b5fbe
    role: context
  - path: pages/traits/metabolism/nitrogen_fixation.html
    sha256: 804f96c89d3d63d0cca606406a60ab14896a3f3c55b2d73ab78cd73e01188050
    role: context
  - path: pages/traits/metabolism/nitrogen_respiration.html
    sha256: 11899c987a9107f8e2e5fc17fe1c4f88c89064fd5e81a177adfb8142707076d7
    role: context
  - path: pages/traits/metabolism/organism_interacts_with_chemical.html
    sha256: 94b20dca8112f37d87460bbf53a96df1a854bf22769bdeb7b29e0967fbf7cb38
    role: context
  - path: pages/traits/metabolism/organohalide_respiration.html
    sha256: 0e9a4193a0c1d67003326b489112db72eb6315c75514cf8291960c83cc005a96
    role: context
  - path: pages/traits/metabolism/oxidative_phosphorylation.html
    sha256: 355f18173e658a52aeb29f23b2fab68f301cae93106afda4841ef6d0e9e6bdd4
    role: context
  - path: pages/traits/metabolism/oxidizes.html
    sha256: 1de5108f302cef3b6909097fad4c22dd456b14268b67a5245870163dd9e5303a
    role: context
  - path: pages/traits/metabolism/oxygenic_photosynthesis.html
    sha256: 32a28320a141fe226ea2d47bb64ede2890deb0637eba3e4bbbec768750f93727
    role: context
  - path: pages/traits/metabolism/pectin_degradation.html
    sha256: 3d7f5f4873251e2b4b4e02d27ea58b3d537ffd2bbd78472d366006dc8efaa6de
    role: context
  - path: pages/traits/metabolism/perchlorate_respiration.html
    sha256: 8ccfa59cb5cc7d6b1d2a2b304372794da059d71586f9b4a6dd8d1e6d7a712ffc
    role: context
  - path: pages/traits/metabolism/photoferrotrophy.html
    sha256: b047e88be988f36d002a00922fbf3c5d26281241aa08c1f2e83540b171388403
    role: context
  - path: pages/traits/metabolism/photosynthesis.html
    sha256: c5e6126f902f9eb3c93695d73de3e916818151f2143b0ce0de43bebdbfc7a70c
    role: context
  - path: pages/traits/metabolism/phototrophy.html
    sha256: ba00a4835d999e8e7ea77f8ad4788a6940f9da9079a01f25b321a4bf4992652a
    role: context
  - path: pages/traits/metabolism/produces.html
    sha256: 13eaa133b64536df4efb56ffaa541cf404fbac4bb735455d35ecdf4f9df5407c
    role: context
  - path: pages/traits/metabolism/propionic_acid_fermentation.html
    sha256: f6ff06282eff838d5aceb36bea8d32c489fa57a47a8ded6272532f64fdc554eb
    role: context
  - path: pages/traits/metabolism/proteolysis.html
    sha256: 07a8da9095a84dd8b0624156f5e2228d79906096c2dda3cc19d7ca50e71d3bea
    role: context
  - path: pages/traits/metabolism/proteorhodopsin_phototrophy.html
    sha256: ad0c19291f87d0c737acea81bc53bb3f2f5e866bc0a01061de694b4f065989c5
    role: context
  - path: pages/traits/metabolism/reduces.html
    sha256: 8c805757a64be0102af44f59f66550f04eb11b855fe4d22820b87cb21e849be2
    role: context
  - path: pages/traits/metabolism/reductive_tca_cycle.html
    sha256: 10a45eb867a2e10c3c0e2651021cb56c60a42b953303464ca1b47b744650dc57
    role: context
  - path: pages/traits/metabolism/requires_for_growth.html
    sha256: 85209dd57ce8c7d37e4474a33296979cf2cb7c8f5be75ccedce592663c0ad3e0
    role: context
  - path: pages/traits/metabolism/respiration.html
    sha256: eb91fd2aabcb7b16d04d25fba54209e199678379eab8a7bf45ab69aaa52c9222
    role: context
  - path: pages/traits/metabolism/respiration_of_sulfur_compounds.html
    sha256: c15cf17e7e5111d04b9b7312d297b4f4144855cf88a14cc8be5791cb82113665
    role: context
  - path: pages/traits/metabolism/selenate_respiration.html
    sha256: 94319ca02c24d2fc247b257f76d0b4ee17811c094919cdb735ab2ccceceb8d20
    role: context
  - path: pages/traits/metabolism/sequesters.html
    sha256: 125efe43da01be78ee1e2d3a1ad33c7e9b4f6642e5f0251af588684f6407d02c
    role: context
  - path: pages/traits/metabolism/shows_activity_of.html
    sha256: 79f0680913788924d2fa966ee2d02ffff575508387d89cdb3a7de44d09dfdeca
    role: context
  - path: pages/traits/metabolism/starch_degradation.html
    sha256: 492652d5d96690a0a0b07a45fdcdaa99c2dafe8bb98de40cdddbfcd7c6c74767
    role: context
  - path: pages/traits/metabolism/substrate_level_phosphorylation.html
    sha256: fdb65e35c579ff253f842d817e07498a3619011430e6d97b76be949f46ba5977
    role: context
  - path: pages/traits/metabolism/sulfur_oxidation.html
    sha256: e7d38b9ac63b62650cc94f8824691d2a21f167dd5a0b99bd1d1a2841646034a2
    role: context
  - path: pages/traits/metabolism/sulfur_respiration.html
    sha256: 42f06f3490d60d8bd85773b7f5dfbad8f6d04362cfefd802036a63c5b85da819
    role: context
  - path: pages/traits/metabolism/syntrophy.html
    sha256: 0280644a88bcf29a96d12536a95f400d22ebb8373aa9a05c7fa322fda819854f
    role: context
  - path: pages/traits/metabolism/tetrathionate_respiration.html
    sha256: 83a58233e8223582a125ec951e73456ebb1cded0c8d1ea016325e9799ebebb3a
    role: context
  - path: pages/traits/metabolism/thiosulfate_respiration.html
    sha256: 06832276fc185c34333c18e2ae1d3c03cb479c41d8de1477e1eedf393b25841d
    role: context
  - path: pages/traits/metabolism/three_hydroxypropionate_bicycle.html
    sha256: 7eafbdd123daa07e4c4d00b6dc430cbf68fa44214fe9437d5c755d1f1c3bb72f
    role: context
  - path: pages/traits/metabolism/three_hydroxypropionate_four_hydroxybutyrate_cycle.html
    sha256: a679af62b5a06961257769c2e684f49a75bcdeeb6f56f95070cd9d405458c040
    role: context
  - path: pages/traits/metabolism/transports.html
    sha256: f9b9e21bde9b01b11d07200958f7e77b2d4a7da7b7aad62617c43ec6962124e1
    role: context
  - path: pages/traits/metabolism/trimethylamine_n_oxide_respiration.html
    sha256: 18a2b32ba355406dcdced1cb6b6314541bc53903d87a52d75dfb2029af6d83ad
    role: context
  - path: pages/traits/metabolism/uses_as_carbon_source.html
    sha256: 9472d55f3f62bde520274690ec1448980f609b497de397dde533c27eb80d671e
    role: context
  - path: pages/traits/metabolism/uses_as_electron_acceptor.html
    sha256: 1bddf529a1de5b36176cf57073a4c915c1c07ca4f1598fa0c030c35f655beff1
    role: context
  - path: pages/traits/metabolism/uses_as_electron_donor.html
    sha256: e102f430b16d915061669aa4a43785201058e69d68ab6deb792fb090a616aa7d
    role: context
  - path: pages/traits/metabolism/uses_as_energy_source.html
    sha256: 4bde8abf0e6723f0c6c2478f76a4630adc81b3277a93bf0501ae3245f51332d7
    role: context
  - path: pages/traits/metabolism/uses_as_nitrogen_source.html
    sha256: ec08344c306ca2e0b58d59b20a7c6fb7719a4b6a35127c432e829f8f413a2c56
    role: context
  - path: pages/traits/metabolism/uses_as_sulfur_source.html
    sha256: b0c39a99946d89ef61356c51836805e1c060a0dc905ba338b6caf60411c0d1a9
    role: context
  - path: pages/traits/metabolism/uses_for_aerobic_catabolization.html
    sha256: 3ae5186a46b3ebeedd6bba230788138596f05c6c0251123ef61e4f6cab35b277
    role: context
  - path: pages/traits/metabolism/uses_for_aerobic_growth.html
    sha256: ce4b7bab5442d670356152e8d04a297c99b7962170e4100729baecc2deb54af0
    role: context
  - path: pages/traits/metabolism/uses_for_anaerobic_catabolization.html
    sha256: 9472ff18e87fa7b680b3b2c4383e3d58045f0f18712c08685c8ce3ac3a5a59d4
    role: context
  - path: pages/traits/metabolism/uses_for_anaerobic_growth.html
    sha256: 489b8bcd8f8c331788b4bbc417f1c68045d255a1a83dfc4602fc872de465c503
    role: context
  - path: pages/traits/metabolism/uses_for_anaerobic_growth_in_the_dark.html
    sha256: 5041c0313032681fc4e0f6c6f8137a41f9f65641255fc10d356627ced12a1b4e
    role: context
  - path: pages/traits/metabolism/uses_for_anaerobic_growth_with_light.html
    sha256: 9ce61d56635ca276f966c480d84ae1e101687f04b8ad05fbd85fcf253986878a
    role: context
  - path: pages/traits/metabolism/uses_for_growth.html
    sha256: e7e7ec77c7634356b0af2d938bd6fcea1a0f0dea88ae5a48a2e7293cf6ca1970
    role: context
  - path: pages/traits/metabolism/uses_for_respiration.html
    sha256: e429710674bda2146910e17e6675289330693bb96f95926f1e481f930c68a7ab
    role: context
  - path: pages/traits/metabolism/uses_in_other_way.html
    sha256: 61a5c8dd354f7c1c026a0bb06a47f1ea8660ef440dd88cfc9b775f6a53e69bf0
    role: context
  - path: pages/traits/metabolism/wood_ljungdahl_pathway.html
    sha256: f3893aa43a152dc5cc49961882abfed3b53f4d87fde6eddaf43ec45171bdcf12
    role: context
  - path: pages/traits/metabolism/xylan_degradation.html
    sha256: f2896d8d9c88190dbbcdd48c9a97434ccbb4ed602eee292d84f854db128a28ed
    role: context
  - path: pages/traits/morphology/akinete.html
    sha256: 4f2435af0362ec7b7c44d669dc54616445a6b0d50e9c0d70d149eb7bb82d780a
    role: context
  - path: pages/traits/morphology/amphitrichous.html
    sha256: fa922bc3bd6834a259617de8d39abaf457771a36e720b71ef6aa4712390b8185
    role: context
  - path: pages/traits/morphology/axially_filamented.html
    sha256: 22060ec2b265f36908fdc9c31a533e1f3242f73eb70dfbe6135f89da8806e0df
    role: context
  - path: pages/traits/morphology/bacillus_shaped.html
    sha256: 30b5f6f170b32f6071ea7cc34f06f5a9662607b2c428f646b9c9850e0ebcea32
    role: context
  - path: pages/traits/morphology/baeocyte_formation.html
    sha256: 54d810211682803ec0fd3870be953c8e1b777142f586d28d23318b28b769ec8c
    role: context
  - path: pages/traits/morphology/black_pigmented.html
    sha256: f6604f8db549c98a21e1bedaa5acc43356b0d0293a90221f58bc91eaf609b5fc
    role: context
  - path: pages/traits/morphology/branched_shaped.html
    sha256: 931429855c342ac6bc79681fb89c58749ed64ac37d024df26475fe4b818fecfe
    role: context
  - path: pages/traits/morphology/brown_pigmented.html
    sha256: b9be403151e84a417ef48c5e96ba11b02af7accd47d558a3bff6f5f05748edf6
    role: context
  - path: pages/traits/morphology/capsule.html
    sha256: 49cfc7f7e98f4f26cdb0728c0f6385feb95df6549bfb526dd299a7d552a01ee1
    role: context
  - path: pages/traits/morphology/carboxysome.html
    sha256: 819eded0fe58d554e904506a9cefe0943db093df8714edde11abee9a428e9eb3
    role: context
  - path: pages/traits/morphology/carotenoid_pigmentation.html
    sha256: 2b9f7a19511ccf3a21dde44ac6a3f488e86d5acc00c8c7cfa6845cd98c9be67e
    role: context
  - path: pages/traits/morphology/cell_length.html
    sha256: 34249f897837a3cd9e4df25f058dfa04e5b8014809c020b96c8b5d8d441463af
    role: context
  - path: pages/traits/morphology/cell_length_large.html
    sha256: e6bc3f5fb52c8cdb023a02f50715a28e80d71ea0e8a7105d78d16256cdc29a2c
    role: context
  - path: pages/traits/morphology/cell_length_medium.html
    sha256: 4854b5ce1d2299b4e200f536a9e854ab6031d75cbc8c92befcd5e224c2d03611
    role: context
  - path: pages/traits/morphology/cell_length_small.html
    sha256: fa34a71d7d1c53f1806c670058457ec8c7a26585bcf8e400e972776637f15ead
    role: context
  - path: pages/traits/morphology/cell_length_very_small.html
    sha256: 66e4d59632109c4a17a542d95a002defefb896b89c6f872e92176b82514f9a64
    role: context
  - path: pages/traits/morphology/cell_shape.html
    sha256: 877b22308793f94c177ba73b2c391e39500d546aa07250dcac761c5d3c006bc6
    role: context
  - path: pages/traits/morphology/cell_width.html
    sha256: 47203c2b91efe3b5542c6ed413bee62f8093df46e55d43fc0aafc78794e1a3ac
    role: context
  - path: pages/traits/morphology/cell_width_large.html
    sha256: 3e89fde8e85b02f4d32999897151bcd6c4fc545733b7e79ad781cfd16d6e73f1
    role: context
  - path: pages/traits/morphology/cell_width_medium.html
    sha256: 8473228b8c97a73db9416a51546d047457371159dad289ab1259e0052e26353a
    role: context
  - path: pages/traits/morphology/cell_width_small.html
    sha256: dfdc281e581ee789e8c9388d9dfcd2945ca7e051d4f1b908cf445097a7deebd0
    role: context
  - path: pages/traits/morphology/cell_width_very_small.html
    sha256: 2b8e555bee4e0bbb08bedd59c919790363e5b74f1e0636a84f77627778de22d0
    role: context
  - path: pages/traits/morphology/coccobacillus_shaped.html
    sha256: e73c6878f7ee0eecd7b9b54040455563e635f3de2ff89b01b85bf1b3f227fae8
    role: context
  - path: pages/traits/morphology/coccus_shaped.html
    sha256: 0336be578fd977e19221280e380fe39a6eb35885504723a3f72fb8c196a80dde
    role: context
  - path: pages/traits/morphology/coenobium_formation.html
    sha256: 1f4695abf035bda7e1d6736f5e164452b52d131b62debdba67fbb059e05f7bc8
    role: context
  - path: pages/traits/morphology/cream_pigmented.html
    sha256: 81508b006f07bfa23a7fd64a4e12d06b13d461f2f1be60081ad0c48669f43526
    role: context
  - path: pages/traits/morphology/crescent_shaped.html
    sha256: 3b0c5ba11b40c65a533a7f52a371c18bb98669577c1a777985c34f83429d6e08
    role: context
  - path: pages/traits/morphology/curved_shaped.html
    sha256: a35ae66bfa76445a7b3edd8b3d61f7314dc06a9c45c94051e97dd8c4efd1adf9
    role: context
  - path: pages/traits/morphology/cyanobacterial_multiseriate_trichome_formation.html
    sha256: 93730ac776981f421d4ee091ec89028a0ceb26abb44c32d3da0debe55428ecb7
    role: context
  - path: pages/traits/morphology/cyanophycin_granule.html
    sha256: 0c71ed2e1dd29daacc28b8051287f7886c3d86dc10865c212a5b31b6c6bbcbfb
    role: context
  - path: pages/traits/morphology/diplococcus_shaped.html
    sha256: e793f7afd32c5863c44496f033f175712a43aca35bf1f44d2c6c28fee8542667
    role: context
  - path: pages/traits/morphology/disc_shaped.html
    sha256: a7211658f872b384872b8ed07fa2af8ee850f653672d6b3a19443b9b4e162c00
    role: context
  - path: pages/traits/morphology/dumbbell_shaped.html
    sha256: e342a6419753ee0442e9feb3f639c83c1ed84dd5647abe2bc8a15677d7fbc71b
    role: context
  - path: pages/traits/morphology/ellipsoidal.html
    sha256: ac07e4d50b773840110f9e64d1b93a2ff4f5fba19a358d1a1ac3b1b893bfd6f7
    role: context
  - path: pages/traits/morphology/expansion_driven_sliding_motility.html
    sha256: 12a766623729b50cdac3fdc8508c7a1b8e2a18a23670cffb9276bf06f6a60f32
    role: context
  - path: pages/traits/morphology/false_branching.html
    sha256: 1cfd8dcb1cb32f3b86b0a534aeca5a96d9d87aefb803d70aecb959844dbdd14f
    role: context
  - path: pages/traits/morphology/ferrosome.html
    sha256: 6b19b936faa284fe7731a8a2d001ab9ca167a4d2612674b75b7415a82e68933c
    role: context
  - path: pages/traits/morphology/filament_shaped.html
    sha256: 0075c7ba9e39f8df1dc5f3e8738e96d9e6caa1417746fdbb136162fceb270f69
    role: context
  - path: pages/traits/morphology/flagellar_arrangement.html
    sha256: 56f5ed83cc8160e5e91fa80798860e6cac8d56a401dd4eae070a5b9428b92c68
    role: context
  - path: pages/traits/morphology/flagellated.html
    sha256: 88f9d8c9972aa4cec2d7f36acf71c1fd789a3974df7f4f937f1f51e1eb98f3a6
    role: context
  - path: pages/traits/morphology/flask_shaped.html
    sha256: 44f967acbed0cd95342b48581d3d9b129654e296a4fe0afdd77afab261707b5b
    role: context
  - path: pages/traits/morphology/fungal_adhesive_column_trap_formation.html
    sha256: 3763e2f3dd00fac0389a3ecac086444eec61ffa45c8a9732033c02345cd17f8c
    role: context
  - path: pages/traits/morphology/fungal_adhesive_knob_trap_formation.html
    sha256: 420164438e6dd43f7f47b207383b3a45df0e87a6b0fbc7f3bc24125fafbe43e1
    role: context
  - path: pages/traits/morphology/fungal_adhesive_net_trap_formation.html
    sha256: d81f8edc3bdb37a35d8048c9ad0883d562b74b40c4765f2d1f231237e68302e4
    role: context
  - path: pages/traits/morphology/fungal_appressorium_formation.html
    sha256: a93ffc89dd783fc383e1c397c28bf95f3b31237a48758ba98e33e4d1cf97c294
    role: context
  - path: pages/traits/morphology/fungal_arbuscule_formation.html
    sha256: 0e453c052d3c12dd8af09bd97f1e7b5c5fde8143975c2ee4e61d912338f42a07
    role: context
  - path: pages/traits/morphology/fungal_auxiliary_cell_formation.html
    sha256: ef51e2c0d4e03f368d9ddf90e5a277e3267ec2f0a509a555dff10b46d905255f
    role: context
  - path: pages/traits/morphology/fungal_branched_absorbing_structure_formation.html
    sha256: f1515816e9dc4b958293710e15ce57151260b9990dc73b1bdcdc0f322ecbb290
    role: context
  - path: pages/traits/morphology/fungal_chlamydospore_formation.html
    sha256: 4513b690118b2355179dac0b5e59a998a807d18a74f15c99e4763258874dc669
    role: context
  - path: pages/traits/morphology/fungal_conidiation.html
    sha256: 252f2435a0d248021b9b6b35ee71d7bd991a6428c23ddddafd115d3ea893962a
    role: context
  - path: pages/traits/morphology/fungal_constricting_ring_formation.html
    sha256: a28a4313e47eac2e3c6a7bee51fe6fd3f187d7608575971eb10e38c5575f8e06
    role: context
  - path: pages/traits/morphology/fungal_hartig_net_formation.html
    sha256: b87881c09934c4b011c89eb44dc4ef5a3ebea5c729990e17f3e8e46c5c676666
    role: context
  - path: pages/traits/morphology/fungal_internal_mycorrhizal_vesicle_formation.html
    sha256: b680f8202943e4c83c336617bee2794c5606b39f72aa0fd29d626dc620ad276a
    role: context
  - path: pages/traits/morphology/fungal_mycelial_cord_formation.html
    sha256: 47319d0d0fb585edfbc207bda43bf500e6b0fb7c2ed421f1d5f089dbca913525
    role: context
  - path: pages/traits/morphology/fungal_nonconstricting_ring_trap_formation.html
    sha256: 996577e794823fa5ac6babbc8e0784f1d42366aff2f0a68914a4718bb3eb9688
    role: context
  - path: pages/traits/morphology/fungal_peloton_formation.html
    sha256: e51f9ac7f4de0bf87e9ac3ce7933a92ac3d92b1ce49190d14a5e52913a1be676
    role: context
  - path: pages/traits/morphology/fungal_rhizomorph_formation.html
    sha256: 8ac8f80d3f0b0136e6b94dc1e212410a4b250341665ea7e2f8df6b224dd84108
    role: context
  - path: pages/traits/morphology/fungal_root_mantle_formation.html
    sha256: 66ba01fa2b314d9e03986bd9bc4d7701104496c221d56c4ae3832c8d6e4f3c10
    role: context
  - path: pages/traits/morphology/fungal_sclerotium_formation.html
    sha256: d17b9857cdbfd9a441c5163b7e32e408db17b2d8c4aa8633dabab2795a215fc7
    role: context
  - path: pages/traits/morphology/fusiform_shaped.html
    sha256: 50705564c7124d9b9623b44124e3958feffe26e203962a1a38a6c7c2d5e7163b
    role: context
  - path: pages/traits/morphology/gas_vesicle.html
    sha256: 5ddaf5bd794b372e04f4b25d18a81f4656d9d61c9047dc0aae0d1726a4a4bb5b
    role: context
  - path: pages/traits/morphology/gliding.html
    sha256: 2655c05296de1c321493148121c5c7732d1ba24847453d8aa1a86a743ea00486
    role: context
  - path: pages/traits/morphology/gram_negative.html
    sha256: 02cd564300bc84a7cd252307779a2e89e16ced0fb9ec952ef81c612360ee8450
    role: context
  - path: pages/traits/morphology/gram_positive.html
    sha256: c4b903d204491ea09b5c23ddbddd4e0c01e875e8431e9b35b50ca9edfe3e3742
    role: context
  - path: pages/traits/morphology/gram_stain.html
    sha256: 9a2251dd6df625876b8d6094719595de0f3faf484a3dcdf84715f2bd94d04971
    role: context
  - path: pages/traits/morphology/gram_variable.html
    sha256: b3d3d2848181ca47bfbf60bf3a3e6c4f40f638544f08a425b65eb686dd546959
    role: context
  - path: pages/traits/morphology/green_pigmented.html
    sha256: d6979f3ba3757ff355698db075cfe0a86174400a800fae0c85f59240dd4118d5
    role: context
  - path: pages/traits/morphology/helical_shaped.html
    sha256: 86bf08c593dc3e4e653570b21f22a82dc67e3bceb9867dd7c8b5419278c6acfc
    role: context
  - path: pages/traits/morphology/heterocyst.html
    sha256: c3df1ce344f600fb8f191aa0d939935f89200aa0b44039c52adf09a1e6f9eb02
    role: context
  - path: pages/traits/morphology/holdfast.html
    sha256: 395b1c47a31bba14e4da51318b9ae6451830bd8a0395d1d22bf4fcc746e0a570
    role: context
  - path: pages/traits/morphology/hormogonium_formation.html
    sha256: d94ba47cdeb9d6cb6db521a20971fe651c59c7f42c8c0cc021419bedce5daf37
    role: context
  - path: pages/traits/morphology/intracellular_inclusion.html
    sha256: 2ed0a20e838521f3ff44093674ef87bbf7a2f4f6a7a33430d89ef33783857b71
    role: context
  - path: pages/traits/morphology/irregular_shaped.html
    sha256: bad8c1c5b2dc54771a1406e8fcbf6a77b625f74a8a44cb8166a85eacc444a51a
    role: context
  - path: pages/traits/morphology/lateral_flagellation.html
    sha256: 6cda5fb511797bc0cc369e37150f619ef65a5d14df06e8b4f1e50fa0f0d6984e
    role: context
  - path: pages/traits/morphology/lophotrichous.html
    sha256: 5884a4c58cfb04b17b53816c4ed570275ccb2e5b6cf838f494fff22b5cd26151
    role: context
  - path: pages/traits/morphology/magnetosome.html
    sha256: 519310f4577a6e845b1034db4baef8ec7665aab86b4483bb499e4ae5f94ef157
    role: context
  - path: pages/traits/morphology/microbial_haustorium_formation.html
    sha256: f7802946117b0e5ce540ca0d29fbc428c5511bab8f40cfa2f074ab130adb90b4
    role: context
  - path: pages/traits/morphology/monotrichous.html
    sha256: 60b22c8441dc2f5190113b902fa9553f2795b586e408f4527019a8cfbf22afe2
    role: context
  - path: pages/traits/morphology/motile.html
    sha256: b4ff25420f9956050b04656858c89c256f466f8c37ab3dbefb15734407756f0f
    role: context
  - path: pages/traits/morphology/motility.html
    sha256: ed72f89dbeb442e2514eea8061412c19ac44a1c8b7f40d043231b19e14ba8417
    role: context
  - path: pages/traits/morphology/mycelial_growth.html
    sha256: 45d406cfc93af23dafaaadd2560422c2b898141625fa9f5ba75f71844c7a7207
    role: context
  - path: pages/traits/morphology/necridium_formation.html
    sha256: 38b9379cca83a00528db7ee45363d8d78c518a2c146d317f83b01e0a7e2e22a1
    role: context
  - path: pages/traits/morphology/non_motile.html
    sha256: d050b3d9b7fe57fd16c7478550ff9bf8a30fbe12db2168511b543adbe9f091fa
    role: context
  - path: pages/traits/morphology/non_spore_forming.html
    sha256: 2b60ac2bcee47ed936ae253acd7f59a8f2b287258b0e74dae8aca48f10b6ad2e
    role: context
  - path: pages/traits/morphology/orange_pigmented.html
    sha256: f9b3de483f7031b792d9e95d21882a76cb07aa85dca3d59f255271ce9f33eb38
    role: context
  - path: pages/traits/morphology/oval_shaped.html
    sha256: b1fa1981ba5212ab1efe409080817274bafe092b812df8d694076b852593e8be
    role: context
  - path: pages/traits/morphology/ovoid_shaped.html
    sha256: 27a662495ff81f30bcc5dac55f4a3ce0e1f906f45637d084b3f3841cfeddc258
    role: context
  - path: pages/traits/morphology/palmelloid_formation.html
    sha256: 9d6b12b51c5c3b42264b196d971a67d6b05a8b991486edbd9abf33a13f9c6105
    role: context
  - path: pages/traits/morphology/peritrichous.html
    sha256: 63530c631630cffc03c285953edd3404d0908dd528a6f0caa035ec33720fb122
    role: context
  - path: pages/traits/morphology/pigmentation.html
    sha256: 1265a36b8e0d0121d4537596e918aaaba5eb0f57755c15b9fa305ee6b61e1166
    role: context
  - path: pages/traits/morphology/pink_pigmented.html
    sha256: 873e149e40f47fc6b8d3c77dd02e595d294edd8ed584108790147621ecc782d1
    role: context
  - path: pages/traits/morphology/pleomorphic_shaped.html
    sha256: 924c3545f3675e0220691e47583b3f9351554400e160f4bc01ba63abe6f8c844
    role: context
  - path: pages/traits/morphology/polar_flagellation.html
    sha256: d3172d9e97e6e32e3843ef217ea675feeecc61351ff53bfdae895881646dfc37
    role: context
  - path: pages/traits/morphology/polyhydroxyalkanoate_granule.html
    sha256: 9a1b0be48de54a3a952e4ea2a4156b6d2d91a0e5250b153370d88dfc593c066c
    role: context
  - path: pages/traits/morphology/polyphosphate_granule.html
    sha256: dd56e77a3c7b2d94360161593db0413fba9c3b174e543dacdaa153f2b65f7fdc
    role: context
  - path: pages/traits/morphology/polytrichous_flagellation.html
    sha256: bead587289145d31366e1a7be5c8e9a0f0e13e1b744ed84eb47e0e63e2dad6c9
    role: context
  - path: pages/traits/morphology/prosthecate.html
    sha256: 81336c9d462df90ac48d80355afac1c3f07106eca134a8d7936507e075b46e6e
    role: context
  - path: pages/traits/morphology/pseudohyphal_growth.html
    sha256: 44c91944d195d61a137e14bed71280eb59f418c37c587ff64d9a544ffb29ee78
    role: context
  - path: pages/traits/morphology/red_pigmented.html
    sha256: ac63bec213ff880322e7917b841a5bfc053224692dfe412febf480af019af055
    role: context
  - path: pages/traits/morphology/ring_shaped.html
    sha256: 8c3923e1dce24b16fa21b70fa5ad255d35fa878b997936d06166a02b5bb92a75
    role: context
  - path: pages/traits/morphology/rod_shaped.html
    sha256: 85c51cbad5d3673ff0db504dc0424d45a9b401e9594d11aa5513ee55d93b0efd
    role: context
  - path: pages/traits/morphology/rosette_cell_arrangement.html
    sha256: 6d7294beed8fbc94ae6636c4c1df38f30fa6950e509d9ed1a123a073c9c69a26
    role: context
  - path: pages/traits/morphology/s_layer.html
    sha256: ab1291fff497318ccaa70a716b31d567b8804e2d350d19b526bb7186365460cf
    role: context
  - path: pages/traits/morphology/sarcina_arrangement.html
    sha256: ff7fee8603de27a9e7efd523e5d88c89fe11d447d6541ac306d80cf6bb4f12ee
    role: context
  - path: pages/traits/morphology/sphere_shaped.html
    sha256: 70a8b903d8908415302ec23c5a503c47cd49692b3dabe1fd208859e1aaddea9e
    role: context
  - path: pages/traits/morphology/spindle_shaped.html
    sha256: 0db46cb0b98c2111e7e842cd2c0701843cbcbbe7f04339ba8a4ca6aa0835e06b
    role: context
  - path: pages/traits/morphology/spiral_shaped.html
    sha256: 25669ddf6b2e3822d6f955b6621e155de314a97c086d2d69de7897f184a4ed9e
    role: context
  - path: pages/traits/morphology/spirochete_shaped.html
    sha256: 63ac144453fe3ac5ba45cfc6e5b92895594718e81e569460da826d46218bc54b
    role: context
  - path: pages/traits/morphology/spore_forming.html
    sha256: cac18e6f67b7b75540fd0b318da9e06d5934606b9116b5146e77776aef0b5e09
    role: context
  - path: pages/traits/morphology/spore_shaped.html
    sha256: cd14e72bc1d1b1014fe1d0a23d34d248024320d77d005601c6b0ac30901801f7
    role: context
  - path: pages/traits/morphology/sporulation.html
    sha256: 9a502d25745f38108becc6480932340dc2f8056f63b8c23e887ab1daa3202154
    role: context
  - path: pages/traits/morphology/square_shaped.html
    sha256: 328f582b34fe078a4f688904cdeee89bfcffc268c69a247bf0e13b1f397bde82
    role: context
  - path: pages/traits/morphology/staphylococcus_arrangement.html
    sha256: 239c3f2fdd9fd07daefff8d4d70af2913206accc046ad5d7ded3d020eb29bf08
    role: context
  - path: pages/traits/morphology/star_shaped.html
    sha256: cd969fd4fa5e423cac7d2420fe25da144ac22513cfc36837ca67db6020731b4d
    role: context
  - path: pages/traits/morphology/streptococcus_arrangement.html
    sha256: fdc07bddfe5e922b3d73f68b7e77009e749fd43792551a003a3ee0f7c842512d
    role: context
  - path: pages/traits/morphology/subpolar_flagellation.html
    sha256: fbd616e7e4da23c2203c9d2ca86191f03dfedce62a234ac5167c38020d7765b0
    role: context
  - path: pages/traits/morphology/sulfur_globule.html
    sha256: 63b7fb13cc48359b8c64c688344636d3222a7ea0e202da9d8f2057247cb3f37f
    role: context
  - path: pages/traits/morphology/swarming_motility.html
    sha256: 59884ca29e005845594a06bab937c5a40ec7728e13aa5b525c844bccf295707e
    role: context
  - path: pages/traits/morphology/swimming_motility.html
    sha256: 15633805511c17f60b625edcfcb0019fed86d9fdd226e2d7e0bf79f029b9af2d
    role: context
  - path: pages/traits/morphology/synnema_formation.html
    sha256: 8dc9f8cb00f45c14f0006f4bc923aaca4d4d1881f56bf4be9dde3860d3630fee
    role: context
  - path: pages/traits/morphology/tailed_shaped.html
    sha256: 6295b4ee6c908f43224e50d3f9896bfbfc93a5a3dce466359ae7462660e799ae
    role: context
  - path: pages/traits/morphology/tetrad_arrangement.html
    sha256: 9d04c08f6b4359641289ba17e3762e8f21b23d8339b79543b32e831e363083b7
    role: context
  - path: pages/traits/morphology/triangular_shaped.html
    sha256: 7328bab5cff7456dda5dd7a8a75ca581a6bcea0ac206c1042305e0db5f3754c8
    role: context
  - path: pages/traits/morphology/twitching_motility.html
    sha256: e62b1ab3d4b9d9fbedfc8fa8783e68387a6d0fe7c628b4a308346bcb00c7b2c7
    role: context
  - path: pages/traits/morphology/type_iv_pilus.html
    sha256: ae0a8c97e680b95e22a70084da467b82cbd4369db6499419cd04be07ff1749a3
    role: context
  - path: pages/traits/morphology/vibrio_shaped.html
    sha256: 029681db949e9596505e346da5434037ee62860327dd6f58fd1162280276434c
    role: context
  - path: pages/traits/morphology/white_pigmented.html
    sha256: 1cb7ed96fcba26431492d0205c364688749240a0e1fdf9eec5df5311055d244f
    role: context
  - path: pages/traits/morphology/yellow_pigmented.html
    sha256: e6d5917ff25948ff743edc57e66a133b306890e26c6b92f2b7cf1406558037ce
    role: context
  - path: pages/traits/observation/growth_nacl_observation.html
    sha256: ea2f55550b43bf2e7ac32ca57f511e8a396c8da808b50f41fc3a3e72e086dc0a
    role: context
  - path: pages/traits/observation/growth_oxygen_observation.html
    sha256: 963811615a13686647f9c46257cea79a0f741376cb4beac9f836307f59e58117
    role: context
  - path: pages/traits/observation/growth_ph_observation.html
    sha256: 5721f6a1e4f17a0943ecd9706f87355c9623327c1cfa72d80a4526727687e551
    role: context
  - path: pages/traits/observation/growth_temperature_observation.html
    sha256: ae2339cac668694523ce9421d1b75dcfd3e2f47371fbd7309639af08147e9159
    role: context
  - path: pages/traits/observation/nacl_delta_observation.html
    sha256: efe5a2e917ce388ee6cfb21342c7767d008f28db44b5b977528a53c8823ad957
    role: context
  - path: pages/traits/observation/nacl_observation.html
    sha256: cc9fa6c9e9e485b2551a2da9e6b55542ee7415e24fe37e4ac95c15a629b9529a
    role: context
  - path: pages/traits/observation/nacl_range_observation.html
    sha256: 756387e863e98243ce6dc7db51592af829ded6322123ab9bea956e3e6095250d
    role: context
  - path: pages/traits/observation/optimum_nacl_observation.html
    sha256: f4dee197d77c13bf1bafbe4ad5cfe96e3e9fc55c9dfdb0c1ce801201d445d499
    role: context
  - path: pages/traits/observation/optimum_oxygen_observation.html
    sha256: d4961502812724fa2673c5425e1f1a2849fb65babdf31a0a4ee2da228446bde1
    role: context
  - path: pages/traits/observation/optimum_ph_observation.html
    sha256: 57b98d020f70a3def584fea253048bdc70dd13a3046fbf71fa6364f1e6293bca
    role: context
  - path: pages/traits/observation/optimum_temperature_observation.html
    sha256: 46f8b600e5973cce59f0ac6cedaad58bf16a1285d40f7b27ab04511e202b0235
    role: context
  - path: pages/traits/observation/oxygen_delta_observation.html
    sha256: b033901ca853bfc948efd9ed607f98d35a5ba296abf06ebf6fd047fb3e28a9ce
    role: context
  - path: pages/traits/observation/oxygen_observation.html
    sha256: f9323a8f86b961fec8e9233ba566e60c9114b483a2ef15b05a1ce5961b73def1
    role: context
  - path: pages/traits/observation/oxygen_range_observation.html
    sha256: a9ebc38cb1c5ed69d5c08b2bd3669e1601483cf62602dbedf571f6df70bf0fcf
    role: context
  - path: pages/traits/observation/ph_delta_observation.html
    sha256: d8417c4d4ee0f3e97119f59fee59076ea9bc03c9612e01affca7fe571a0361be
    role: context
  - path: pages/traits/observation/ph_observation.html
    sha256: 743b1d36134e463a5a345c00f338de44bfcd9db0fadc6fcea2e3ac33fd17de2f
    role: context
  - path: pages/traits/observation/ph_range_observation.html
    sha256: 8c3388a565648485ca3894afd2c4d8b86c9a8c6a2415ad65f444deaace8ad9c8
    role: context
  - path: pages/traits/observation/temperature_delta_observation.html
    sha256: e2c435ba8282c2cf022f84fa21c0ba4fc9b19257dc609469f7788e15384f9d0a
    role: context
  - path: pages/traits/observation/temperature_observation.html
    sha256: e8ede0bd8beba3c0155124b8a5e28c89a14d0cc895d16c89ebe3605c82374cdf
    role: context
  - path: pages/traits/observation/temperature_range_observation.html
    sha256: 6e382814de005ad6e48fe62579ceffe83311a6aa75b29de79d8f148309aa4f0c
    role: context
  - path: pages/traits/other/catalase_negative.html
    sha256: 9d63ffbbdcd21b23d6bea99b0a794a3ab4cb19f648940747af3c33cdb964d23c
    role: context
  - path: pages/traits/other/catalase_test.html
    sha256: a478543adf42387deefe68c09d1f4387ede6aaefe2d8137e0c1976eed02f5434
    role: context
  - path: pages/traits/other/circular_colony.html
    sha256: 356637f13179da9717b49961d673e8c2bb1593b65b49bc561503f97d13b986fb
    role: context
  - path: pages/traits/other/coagulase_negative.html
    sha256: 3c4859e59d8a12d4d9b6d01c402d347a84a76fa392f3583e62006cbb71c334be
    role: context
  - path: pages/traits/other/coagulase_positive.html
    sha256: 323a08419e351e8660fb4aced8edbb26eb0a6019ec34d7aeab2f9613f29af136
    role: context
  - path: pages/traits/other/colony_morphology.html
    sha256: 1ba2dbb81b98e248c31f81e45fa3e4b4197058e59470bf3fb9612679ee67f7b0
    role: context
  - path: pages/traits/other/colony_shape.html
    sha256: dbb646877ef68135690068b821dcf69fefad412b61478d1261ab826720221cbe
    role: context
  - path: pages/traits/other/epibiont_phenotype.html
    sha256: 4f7740edfcf9ae4265671f3c3c4035c24371c09bc533e3bc7dd46eab7cd2dce8
    role: context
  - path: pages/traits/other/filamentous_colony.html
    sha256: a72a8537bc1d23e18992fcc4db495d71d189a66b8a547b10d74d8d4bc560aefb
    role: context
  - path: pages/traits/other/fried_egg_shaped_colony.html
    sha256: 17c3a44fb9cac360e3efbeba284a383bf48ec31dbc9b40d6501bda79f3d8caab
    role: context
  - path: pages/traits/other/generalist.html
    sha256: 913cd1e866bbc3302e3c47764a96ba906d0d57ac445824fdb3570027ba7a96fc
    role: context
  - path: pages/traits/other/hemolysis.html
    sha256: db225a8abe16a891b828c8ffd19078160e79a2d01b592cf1debbcc8fb55ce5dd
    role: context
  - path: pages/traits/other/hemolytic.html
    sha256: 1c5d98c586bc2b21a8d78ec8a98fdb0ee85852e7fd0ba84df38da8fb9ebf9c30
    role: context
  - path: pages/traits/other/indole_test.html
    sha256: cba06c69c8d23a48ad25eba4c4f358fe0be3d3205bb901f51f25a61fe5bd05da
    role: context
  - path: pages/traits/other/indole_test_negative.html
    sha256: ee57d2b45c63d7ccdc21e808bbdb6a7025a150693ca233e81f9cac61ae5e10c2
    role: context
  - path: pages/traits/other/indole_test_positive.html
    sha256: f51e84a814006005bbe21cd5b791d81c84493bc3684cee8b4e9534c871b36958
    role: context
  - path: pages/traits/other/irregular_colony.html
    sha256: f15778f9d43a738e050e73a389850ba6d0926ed05b56e79b059290e2cfdadc33
    role: context
  - path: pages/traits/other/methyl_red_test.html
    sha256: fd5c4882297a1322b7a6ba1f4ec6b0109797c82006f901fe37ae940918644b37
    role: context
  - path: pages/traits/other/methyl_red_test_negative.html
    sha256: 9d347d4b5012c7f577e22e1bcb0fcaab653ae81f42ab5dfea81d9eba19d16347
    role: context
  - path: pages/traits/other/methyl_red_test_positive.html
    sha256: bac2b0114236ff27b140e9329aea5a5584eb78eaf34dc23d8dd89018de3a0cfe
    role: context
  - path: pages/traits/other/non_hemolytic.html
    sha256: 2a7b5925ec194710364c1115eb7081cc1ce4897480d7077f587ae392d4c05a84
    role: context
  - path: pages/traits/other/osmotic_tolerance.html
    sha256: b3a0c52283d2e23270291d611ad769d8533e8085bd429fe71e41b10bfc45dfd8
    role: context
  - path: pages/traits/other/oxidase_negative.html
    sha256: 39c8033a628b0ed3cedd84bfef493c07a380de976704926eefca1c3f151ce99c
    role: context
  - path: pages/traits/other/oxidase_test.html
    sha256: 8646f41506abae4c4b2d27706c7b12ea62adeebe51259e7cf99d38a3160e5657
    role: context
  - path: pages/traits/other/punctiform_colony.html
    sha256: 5916ced2f38db15413ddd60c16621d52af3093d122a93d200f3ebb7c155cca2a
    role: context
  - path: pages/traits/other/rhizoid_colony.html
    sha256: 5ac229d4083e71ba974db158e68e3bbb720d6b78076dbeeb0176192d7d58f6e4
    role: context
  - path: pages/traits/other/specialist.html
    sha256: 130adf268ded994ba45daf09258941d99a2f41fb926b025181c6a9974f97aa48
    role: context
  - path: pages/traits/other/urease_negative.html
    sha256: c96090cd8c526f8dba49027eb19b5b8607131d7aa852566eadd16a35a2eab5d1
    role: context
  - path: pages/traits/other/urease_test.html
    sha256: 11762b7192678f70c815db0e8ef7d6190a86cfb9f4827e2f66fa9a79818e992b
    role: context
  - path: pages/traits/other/voges_proskauer_test.html
    sha256: 3219f6e699e1c2ac3e2d69472231093340ff8094a5d19dc5f102742f05fa215e
    role: context
  - path: pages/traits/other/voges_proskauer_test_negative.html
    sha256: 4a952051a8d68a3521a2e84f2b22fc9da5ed5bfc9c63f2f0d2e36df6f7d92e22
    role: context
  - path: pages/traits/other/voges_proskauer_test_positive.html
    sha256: 46905f08ad9a5701417432a85ef3495ca06c0cd51b90b3a71d4c1c6ace60a870
    role: context
  - path: pages/traits/physiology/acid_phosphatase_activity.html
    sha256: 62c580f15eeb751e166cdffb6a32d10acf3b75699b1b9aa36f00c1fef33a0473
    role: context
  - path: pages/traits/physiology/aerobic_anoxygenic_phototrophy.html
    sha256: 60b17c1b14d8d7bfc7d9085e0e2a8fb2c6f6d2d983ed1009f33daf42355a9591
    role: context
  - path: pages/traits/physiology/aerobic_overflow_metabolism.html
    sha256: a6f74ccfc48d1a4d8968bf0f4df93a327639659e583e41546a4b092b69a41940
    role: context
  - path: pages/traits/physiology/aerotaxis.html
    sha256: 5ab224be89aae9f518b598c54897157802013d11c2994ce0ba1605342a7cd2d7
    role: context
  - path: pages/traits/physiology/aerotropism.html
    sha256: 8417008e207b6538ac1bd75e651d64e0b23bed43e46cb9b7d4432b96cf16c9b0
    role: context
  - path: pages/traits/physiology/aggrephagy.html
    sha256: 2aacff6b014d4108ff66bcc3dd7e14aa7dbf4b22266de930ddef6f2c934f8d94
    role: context
  - path: pages/traits/physiology/alanine_arylamidase_activity.html
    sha256: fc7aaedbb1565866b1e0248f15f82f2f2e12fcbee4df1393486fae367c36d694
    role: context
  - path: pages/traits/physiology/alkaline_phosphatase_activity.html
    sha256: b82125ed80b583ba4c8824a8d293fcc3f369785d81e845ee16b06587fa9fe22e
    role: context
  - path: pages/traits/physiology/alpha_chymotrypsin_activity.html
    sha256: e87f2a2c95f1059477fd0f28683b491b814ca65bea654706c22e983b4510a26d
    role: context
  - path: pages/traits/physiology/alpha_fucosidase_activity.html
    sha256: 39f61844db5ff5bb2042515fa2c2da35022a6c05b00cf2e1e3f4c0ee47023ad9
    role: context
  - path: pages/traits/physiology/alpha_galactosidase_activity.html
    sha256: 3dc9ae1a9a335f2802582a803b08a4c00b080a1d1a4b733241af5147338b400c
    role: context
  - path: pages/traits/physiology/alpha_glucosidase_activity.html
    sha256: e4372c08710c3f8af434bd97b7debdec2f21851b7c86f37b5b5e144398f2e7ab
    role: context
  - path: pages/traits/physiology/alpha_mannosidase_activity.html
    sha256: 1dc7a21a6e21e79ad6777fbf348978c492de8c86f0d686ef72a88744015fe159
    role: context
  - path: pages/traits/physiology/amylase_activity.html
    sha256: b4c03545a4e070b124852cf9d96bb136201e50074040a9775d5041bd68f72608
    role: context
  - path: pages/traits/physiology/anisogamy.html
    sha256: e2a152baf24667a6825b09f90b7a0268dc491865422eaa71cb3fbd7d9ce7a03d
    role: context
  - path: pages/traits/physiology/antibiotic_resistance.html
    sha256: d7097fde37a26f0f3a7a2b5b4693ee134a433ecb09de24d7b7eebdfc8fd399d4
    role: context
  - path: pages/traits/physiology/arginine_arylamidase_activity.html
    sha256: 9b592bc947309c3ee968c17ac6a12da7b2f78d11c8c8656d67349793f19c12bb
    role: context
  - path: pages/traits/physiology/arginine_dihydrolase_activity.html
    sha256: 3da4ee2f48c2c0e4119e9d86fcd3c44fdc434a6dab928c22724248396da64898
    role: context
  - path: pages/traits/physiology/autogamy.html
    sha256: 6d26526363f3294d5405795a307bc1485d84351671b0166fee1a5cc0fde450bf
    role: context
  - path: pages/traits/physiology/automixis.html
    sha256: 50c6c7e30d37d92c6d7d3da0e278e86e531ea2e6fc282b657ed6bf5483fc3d5b
    role: context
  - path: pages/traits/physiology/autophagic_glycogen_degradation.html
    sha256: 73362f34850ff42e045f2d7ed8832a5ba73e20989c2b15c1fdac9794478371ed
    role: context
  - path: pages/traits/physiology/autophagy.html
    sha256: 3081b6590341d7465334698483f979bccabb01c2da268c729d3875f700988e1d
    role: context
  - path: pages/traits/physiology/autotrophic.html
    sha256: b5bf1fb31c3d3694258845ebcea151d50cf0ea370f727a4474c304a91f2b275a
    role: context
  - path: pages/traits/physiology/bacteriocin_production.html
    sha256: 3178fdc4a9f549df58bf22b16edd867f885ea3348db2cfb9920af8a231815520
    role: context
  - path: pages/traits/physiology/ballistospore_discharge.html
    sha256: 5e8c1a8b4665ed48686cd5295e32f62b5ed4a464a607f244c886578e926b89da
    role: context
  - path: pages/traits/physiology/beta_galactosidase_activity.html
    sha256: 435688fdf3ea78424a2b191b5456960a0e7dc9f98ff774b8f55aa4e66bff06d8
    role: context
  - path: pages/traits/physiology/beta_glucosidase_activity.html
    sha256: 37c5c68c4b5d1a93c6298b8610734102b39b4060c678660c0b60042e56488ea2
    role: context
  - path: pages/traits/physiology/beta_glucuronidase_activity.html
    sha256: 8a5923e6c17d73a048ea16773cb60192c225f63ef64b89d424240adf8206591f
    role: context
  - path: pages/traits/physiology/beta_n_acetylhexosaminidase_activity.html
    sha256: 65c6c9d36e427b62b8710b8c67e8d1f0155a13ec7e296bd020fa642d66330299
    role: context
  - path: pages/traits/physiology/bioluminescence.html
    sha256: 3e8e56e862a4e29b4fb40a1f70be233e33db10d5bbd085c583b570d6c1b122a1
    role: context
  - path: pages/traits/physiology/biomineralization.html
    sha256: f61eec7bea39f115535ac32b9580d68a1c5b33e6f47629cfed85aa6295d0f47d
    role: context
  - path: pages/traits/physiology/bipolar_mating_system.html
    sha256: 4b6917d3e58b7204648bf9b49b790f0b67e3db0824bfe701babc065337732ebf
    role: context
  - path: pages/traits/physiology/carboxydotrophic.html
    sha256: afbc891b5cf9270075c1f00740997a8472167384738d64b9c963e6b975ea0707
    role: context
  - path: pages/traits/physiology/carboxylesterase_activity.html
    sha256: 17f867cb312d90a247f8c586e6a2ca6fd69f0e9da00bb805609629db7336bbac
    role: context
  - path: pages/traits/physiology/caseinase_activity.html
    sha256: 3fe110e337c61fe359614fa67b47295a4188ce26ac6ef352e081b8c7023000bf
    role: context
  - path: pages/traits/physiology/catalase_activity.html
    sha256: f67fd75a929fdb7022fc61de7c99807bee46204f8746f8a1a569b0beab0b1610
    role: context
  - path: pages/traits/physiology/cellular_buoyancy.html
    sha256: 1728ebefed707559a5fda6e1ee5b5b36370093261a632a546248d24ce525e782
    role: context
  - path: pages/traits/physiology/chemoautolithotrophic.html
    sha256: f2b342d4fcf0ed1b4948f43b84d08c14116c3148e30cab77af249001a026a197
    role: context
  - path: pages/traits/physiology/chemoautotrophic.html
    sha256: 488d8843691d10c37acf72a0c2862600d727bd64ecdde200e6ca502f50d03672
    role: context
  - path: pages/traits/physiology/chemoheterotrophic.html
    sha256: cb190be6cdbb350ad0abdf8c43903083bd9b3b656fc9c9d087a9867e1c9069fd
    role: context
  - path: pages/traits/physiology/chemokinesis.html
    sha256: da009de57678db4724ee80e7ef9db956ad8bee27af0b8957abd615158d1f3a68
    role: context
  - path: pages/traits/physiology/chemolithoautotrophic.html
    sha256: 4dadd80b1513f76a42a2d031c983e89e93c66266ca7d7895e714cb110916e22c
    role: context
  - path: pages/traits/physiology/chemolithoheterotrophic.html
    sha256: 282292f7abae3f78bcf6dddb7b33839f22bfa67de1b725c923f55e8ddf18dd94
    role: context
  - path: pages/traits/physiology/chemolithotrophic.html
    sha256: febd3d1d0dfd1ad2d4897b77c488a8dd96403f1fda87837ba25478ec7f02503c
    role: context
  - path: pages/traits/physiology/chemoorganoheterotrophic.html
    sha256: 3d8cdb24b9c3a4514f90cf9ac6d87666c5f5637be252bd79f177ecd74b8d95bc
    role: context
  - path: pages/traits/physiology/chemoorganotrophic.html
    sha256: 3b966dd9589ab9b25715791d8a1a70fd6be7c0bd19243ebcd1b601178784adb8
    role: context
  - path: pages/traits/physiology/chemotaxis.html
    sha256: 9bff89d4e4f0308502ba84c0e21caf0c725bd199e2a7e38c89cbdbc6be8491ab
    role: context
  - path: pages/traits/physiology/chemotrophic.html
    sha256: ae9431fbece6fa4c8d710b067e8babf8c35eefa8f76a9e91f39f9bfa038a9708
    role: context
  - path: pages/traits/physiology/chemotropism.html
    sha256: 65d22b39074ca446605ee566f14a4d09064c1b4e0f37779e898a73b7a547b9c9
    role: context
  - path: pages/traits/physiology/coagulase_activity.html
    sha256: baaded35814613579523061dd3ad33f39f69a83e50836088b69db670b9a6b296
    role: context
  - path: pages/traits/physiology/coccolith_production.html
    sha256: 17e4bf01aaf2f706b32524c304ab4164c31c10a2d688634ee3f24d2956bd0a6a
    role: context
  - path: pages/traits/physiology/cold_shock_response.html
    sha256: 257916ed06aebb4f32191b29de0ed8d166d5fac61bce830fd9d4984233e951c3
    role: context
  - path: pages/traits/physiology/contact_dependent_outer_membrane_exchange.html
    sha256: 5fd7d924641955f6cc6f66e87091ad067c8263e310cf7cc15d69cf7d772ad0c5
    role: context
  - path: pages/traits/physiology/copiotrophic.html
    sha256: 116f5042ec40e845dd516b39805649c4f42863a71ac1e23120a7d2ab4f85838d
    role: context
  - path: pages/traits/physiology/cystine_arylamidase_activity.html
    sha256: 030b174f22660f921d5e5f66bf088536feedf1c92dec66b21266f54f79c34678
    role: context
  - path: pages/traits/physiology/cytogamy.html
    sha256: b23528817855c92fbd0bf6ef8dd490287ff8543daabb75b4488b811062c082bb
    role: context
  - path: pages/traits/physiology/diatom_frustule_production.html
    sha256: 6030c818e3c26095c34ef54a2c5571161f78234184b97c726e0abf3a9e376a2c
    role: context
  - path: pages/traits/physiology/diatom_perizonium_production.html
    sha256: c5d3dbe0f77194ede2feba1ab7cfe3986e418f33f733084ad1935fd0a667c9a9
    role: context
  - path: pages/traits/physiology/diatom_seta_production.html
    sha256: 180e3c43644666b27fcae175c4d501802619f4dd9d40a0a8a2f8a82dbfe4366d
    role: context
  - path: pages/traits/physiology/diauxic_growth.html
    sha256: a8dbe113fe524f1fbe2e2c6476bf876b5c9a64930fa0bd1d8a071c1f75fcafed
    role: context
  - path: pages/traits/physiology/dnase_activity.html
    sha256: 1cc5fca81b5d362360728207643952c1a47d07b43140190d7463d8822cabd819
    role: context
  - path: pages/traits/physiology/dormancy.html
    sha256: 398c9214a1ff946e8ba533036e937cf88bda88d735fd88cde9e8b091a8431f72
    role: context
  - path: pages/traits/physiology/durotaxis.html
    sha256: bafcef5cd3fec30a00997d110eb37d2327ed720026d42b708b0c4c65077e956a
    role: context
  - path: pages/traits/physiology/endocytosis.html
    sha256: d26ed3bdf7fffb9957617ae7c7d50bc7e4a0ec480eb6eb1f546d29591389833d
    role: context
  - path: pages/traits/physiology/energy_taxis.html
    sha256: c065db3f6cb1add97185814488e4ddf74257f808a1b576de142fe7f46a2bb518
    role: context
  - path: pages/traits/physiology/er_phagy.html
    sha256: e17f63d228b1f92a50efef3c4e26760746331711b0d88cd97e96033d1bdc7877
    role: context
  - path: pages/traits/physiology/exocytosis.html
    sha256: a32c5006a082ef48387f6120f6a955a6d539aea31c35aadffc06158cd3a97749
    role: context
  - path: pages/traits/physiology/extracellular_membrane_vesicle_production.html
    sha256: 827e2953caf3f1882c4c385a5d4d23d9badab3b1f6b3c9f1a5e67d131f6c9bc3
    role: context
  - path: pages/traits/physiology/galvanotaxis.html
    sha256: bf515d3cfe5a027ac69c52b1e42ac4e677f3d4cc08c687a10078c549740ccf65
    role: context
  - path: pages/traits/physiology/galvanotropism.html
    sha256: 51cd722feda35280217e874a8f39713f9e6ee2921c51d472a9cc980f26d9646c
    role: context
  - path: pages/traits/physiology/gamma_glutamyltransferase_activity.html
    sha256: 22f1102c6392d863dfd0e36b6e4acbc4124d449edf64bf9eaa4e5e90959c9317
    role: context
  - path: pages/traits/physiology/gelatinase_activity.html
    sha256: 8478cfb0027b935a06ba31e5e96bf8c46ada10b96aed74f821fe53f1c81ebb33
    role: context
  - path: pages/traits/physiology/glutamyl_glutamic_acid_arylamidase_activity.html
    sha256: 28cf8938a6c91d1d12dbdc4efc3b632b7aee163b4cf7a2795c364dd863895fd6
    role: context
  - path: pages/traits/physiology/glycine_arylamidase_activity.html
    sha256: 540a1b31e958fd0abd0b71d32a4e16542ffb5c04e4d840e5f1ea8a024c3f157d
    role: context
  - path: pages/traits/physiology/gravikinesis.html
    sha256: 4995d55cbeb1d1afec8713c0b1be7cc164d64e3f7e61e1db4c84214756a84332
    role: context
  - path: pages/traits/physiology/gravitaxis.html
    sha256: a18c891a0c1e013383aa77ba9faefbaeee88d146437fe6d8d00b2a5c22e48f24
    role: context
  - path: pages/traits/physiology/gravitropism.html
    sha256: 5cc98b1a1125ea6358d62d6e7287dfdbd021e848547c9decc09bc4cd88400cb3
    role: context
  - path: pages/traits/physiology/gyrotaxis.html
    sha256: a2fd506acb21f7826fddd1de8588d7df22b6bef08a7cb921ac4138ad0ed206a5
    role: context
  - path: pages/traits/physiology/haptocyst_discharge.html
    sha256: 4c9d636808dd60fc9bb850902e030a7a61dcbba4960caa6e70214beff8bbca39
    role: context
  - path: pages/traits/physiology/heat_shock_response.html
    sha256: 7ca0fcd22c1e474959781fb02d53a5bc65c126bc5d8c094ee55e10442d6a5892
    role: context
  - path: pages/traits/physiology/heterokaryon_incompatibility.html
    sha256: 43434b40e3544ddc4530685b20ec338f4ff201271a12275f77f15a5fe66181c3
    role: context
  - path: pages/traits/physiology/heterothallism.html
    sha256: 07a9c89e3376c0c29b6e712ce7d1bd7f0d31e66f337e5ece99e703964783f934
    role: context
  - path: pages/traits/physiology/heterotrophic.html
    sha256: dd20dc4de923febd1f4dc5a85f8868a161833e15cde498bfa978f7974ce3e3ae
    role: context
  - path: pages/traits/physiology/histidine_arylamidase_activity.html
    sha256: bf657501ea92deb0740ef7f4c49e91a2883800dc9de1c4d630c3265599b8a457
    role: context
  - path: pages/traits/physiology/homeoviscous_adaptation.html
    sha256: 27362664ac37ea06848339daa40283876eedd34152a3075759bd42dd1136d66f
    role: context
  - path: pages/traits/physiology/homothallism.html
    sha256: 7e3cdfae1ca1c2413a94ea04f87b16f5168481206b5fda0e31d0f3fcea7817f3
    role: context
  - path: pages/traits/physiology/hydrogenotrophic.html
    sha256: 7c6f74074a68fb960f02673d8c82e7eb5f7a02f10770d9ce78b25385f3fb465b
    role: context
  - path: pages/traits/physiology/hyphal_anastomosis.html
    sha256: 5e6b27f46d039299d55c367754eee5dfa740f5bc829e7c6ac8ebb2b0d26b9b25
    role: context
  - path: pages/traits/physiology/isogamy.html
    sha256: 74fe449721bbe9a65fa9e0a0feae6094e7ced6077ddd0429e9269a21ada86df1
    role: context
  - path: pages/traits/physiology/karyoklepty.html
    sha256: 0a26d16ecd3c851fcafea02d5dd263380b8d2fa465275d64d0bd58f801222c43
    role: context
  - path: pages/traits/physiology/kinetocyst_discharge.html
    sha256: b81479d51d1336aa92e92d0f0033225031c4f53cb64b7deefb4b03e7d72f3891
    role: context
  - path: pages/traits/physiology/kleptoplasty.html
    sha256: 24a2b81ba5131f08efa874805c450a641eeab04e2fa5f1b8556c1b6fde08dde0
    role: context
  - path: pages/traits/physiology/lecithinase_activity.html
    sha256: 3ff0471eb0c7e8e4e8f8b73262c47bf5c5ddd74ad229c6d0599d1dcb49b9a6ec
    role: context
  - path: pages/traits/physiology/lethal_algicidal_activity.html
    sha256: 6b5af008f2ad45161f27f69b7864be69f52d5e6b1be574031d72aea40faae3dc
    role: context
  - path: pages/traits/physiology/leucine_arylamidase_activity.html
    sha256: 86a96fc26129936fbd0ec5a6988c093751420abfc1950951d6b3edb6bd921bfd
    role: context
  - path: pages/traits/physiology/leucyl_glycine_arylamidase_activity.html
    sha256: cc729ff2e3a64044e738727d82e5d75fcfc93d2a68c2c118558b255977dd916a
    role: context
  - path: pages/traits/physiology/lipase_activity.html
    sha256: d62a5c4ed4dbafdc9f183cacf805a13c09090896e8a72956b08e8f1c7ca58bd3
    role: context
  - path: pages/traits/physiology/lipophagy.html
    sha256: 6be586294eaed8faec1bcf9351f41dd42e642566a782f4a1ccfb0b381970a45c
    role: context
  - path: pages/traits/physiology/lithoautotrophic.html
    sha256: e197dbb648a012296164caf48f78a93c65cf909ea35a27afbfa64f099643227a
    role: context
  - path: pages/traits/physiology/lithoheterotrophic.html
    sha256: fbb7c9ef5daa59f06c11cda80b2f9fbb59ab806c163e704889cc717ad6c99f28
    role: context
  - path: pages/traits/physiology/lithotrophic.html
    sha256: f22b448628ed7b719bfb2dc8b34afb9890b1155d599a3d9ad224b17710e62385
    role: context
  - path: pages/traits/physiology/lysine_decarboxylase_activity.html
    sha256: 9a30d1986da12bab3e4b8056904ab23bb879fb9dee60e44656462a4ca812ff86
    role: context
  - path: pages/traits/physiology/macropinocytosis.html
    sha256: 51d139e87f53eaebbd062048b3570cc5f6998bce72a95122e99d88eba93af65b
    role: context
  - path: pages/traits/physiology/magnetotaxis.html
    sha256: 5abadf2e9fd81ed132c596a8327e01639865c8c9582b1703a89f2289619e20d4
    role: context
  - path: pages/traits/physiology/mating_type_switching.html
    sha256: 21589e18ee23a8bb53015cb7ac20e9c01e36aebfb7c1ac8e4cce421013ffff86
    role: context
  - path: pages/traits/physiology/methanotrophic.html
    sha256: 88e5c198087278f4ec7fe76427c956d95898449f201a59ddc186eb522dbe384d
    role: context
  - path: pages/traits/physiology/methylotrophic.html
    sha256: cef2e441420040e8d59cd5b3438f28b4fae3cec2af1940289e9f63643d631b45
    role: context
  - path: pages/traits/physiology/mitophagy.html
    sha256: e7e445a1cab243b32c6be238b79dd9450f7d519dc8114df992d5c3f8a72437cb
    role: context
  - path: pages/traits/physiology/mixotrophic.html
    sha256: 03011c1bde73a39285d2b57db4a30ab55b342b1e9ec710404c99259c81411a91
    role: context
  - path: pages/traits/physiology/mucocyst_discharge.html
    sha256: e8a37afa01c997d1a4392189860c3f2ec3a29f7aa0f916e3f8d9122d130d875f
    role: context
  - path: pages/traits/physiology/myzocytosis.html
    sha256: f2eb901e2106139670048f70062bcfc193b0244eac616acefee226ac0d3f0d48
    role: context
  - path: pages/traits/physiology/nad_dependent_alcohol_dehydrogenase_activity.html
    sha256: fcd8f490d494d247037adc1214fa00f4d7d99ddd30e55054b4a24bef24f1ea04
    role: context
  - path: pages/traits/physiology/naphthol_as_bi_phosphohydrolase_activity.html
    sha256: 0234e2e103aa61135db62e5303cabfdc7610a1d52e05c2ec762fde584f6d6c41
    role: context
  - path: pages/traits/physiology/natural_competence.html
    sha256: fe1a3107ae4631312a56cad351e852bdd7918a93f966b8db2ef7495259a78bba
    role: context
  - path: pages/traits/physiology/negative_autotropism.html
    sha256: ba1a07c2becfa4d8d910bb0d6691086a5ab246337a9d2e9d15b833bc56b259ac
    role: context
  - path: pages/traits/physiology/nucleophagy.html
    sha256: 9c545ae1da1b87299d87c154be36b9a3516dfc1de88cbd1af9508c4dc13a6949
    role: context
  - path: pages/traits/physiology/nutrient_adaptation.html
    sha256: 13f3cb382ed1f607761ddce4144fed847782aa7b91e88fd97ff9e390fa87769e
    role: context
  - path: pages/traits/physiology/oligotrophic.html
    sha256: 7a597a0d9de4d473e8502ea82d6f16fbf79ca02c965d537b7c2bf6846598e9d6
    role: context
  - path: pages/traits/physiology/oogamy.html
    sha256: 5bd14f052a31d007f2d84d3f55aed70e85e341fe75d2b1ab6675b5f7a359bb05
    role: context
  - path: pages/traits/physiology/organoheterotrophic.html
    sha256: 99607c9498c23167ab6ae9db44447e2b8460d8f26060e3ca15c696b238fb070a
    role: context
  - path: pages/traits/physiology/organotrophic.html
    sha256: 364162881d57464a33d71eb7a71b8cd6f64c0331c24bbb55051592278086941c
    role: context
  - path: pages/traits/physiology/ornithine_decarboxylase_activity.html
    sha256: 719aac42fefe4c0526c3d3a36f350243e967932dab5891ea3767bb6b700ce824
    role: context
  - path: pages/traits/physiology/osmotaxis.html
    sha256: 9edc860ca4073a2aedabdd6cf485dd8d78480ee9b100b0a8a218fc40bf9e0a9b
    role: context
  - path: pages/traits/physiology/oxidase_activity.html
    sha256: 55d90266655e146dd593e3d8948f4d15645ba34bee33561a28f14c8fdcbdb477
    role: context
  - path: pages/traits/physiology/oxidative_stress_response.html
    sha256: 849fbd860240bdbc2207a72df4df7056b2fb11c40c6b5f10c338b17beaf99df6
    role: context
  - path: pages/traits/physiology/paedogamy.html
    sha256: f58a38547eb09c093e6c184ce6cbc5a1acd68f1fa3bfb2f10755aba6aa60e681
    role: context
  - path: pages/traits/physiology/pallium_feeding.html
    sha256: fbb5b800367c52b64f89b6a1daaca136ec241e0036ce3d2e6f03fa5149973104
    role: context
  - path: pages/traits/physiology/parasexuality.html
    sha256: 9349101a4f6c4538af7ef1a7599a4345aacef1ae5ebc99050f94a21c4314b67a
    role: context
  - path: pages/traits/physiology/persister_cell_formation.html
    sha256: 919237e32786ddcff948a75cd3170f182946de2236816b0cdc041f0ad535ad05
    role: context
  - path: pages/traits/physiology/pexophagy.html
    sha256: 1b2c5dcf922442ca65510ca47aa4fdd1d9fc4587c2d13324f32a6bd81fbda532
    role: context
  - path: pages/traits/physiology/ph_taxis.html
    sha256: 4734322f775ad01cd919dcb777f89ef1cb0d9a4bd6b2fb845460f854e58f0bb9
    role: context
  - path: pages/traits/physiology/ph_tropism.html
    sha256: 96bcb1d9b2bbd497cee8c6768a58d1f0ccf96b6597210cd3d77530f126489d3c
    role: context
  - path: pages/traits/physiology/phagocytosis.html
    sha256: ab43bc4943da5cb05dc2c81e25af528ab8227516003aa52d8c3d0a1097e75256
    role: context
  - path: pages/traits/physiology/phagotrophy.html
    sha256: f4594dbdb88f30f2e1d3b85e4209eacb61e247808c841c6cd4de5cb59873387d
    role: context
  - path: pages/traits/physiology/phenylalanine_arylamidase_activity.html
    sha256: 0a27a356a58f9e3bcd1bb64b671c1146c3d14401605f3547bf619785d9fa18b4
    role: context
  - path: pages/traits/physiology/photoautotrophic.html
    sha256: 5cc65a637215054920f7b7c92b6b9a5adc2ff144fabff70a81cb0b1ae7d492d2
    role: context
  - path: pages/traits/physiology/photoheterotrophic.html
    sha256: cb24da79027bf049d24ba1a5beec769a4eed4871f58dfd05e2b5221b7b138de2
    role: context
  - path: pages/traits/physiology/photokinesis.html
    sha256: 2c7f282352e97cd9b342a5dba8a38551c74cf62c3ffd2b780656976be5f50f4d
    role: context
  - path: pages/traits/physiology/photolithoautotrophic.html
    sha256: 75112bdaeca07ff4152f79131edba299d0e560730e81d94ad11156f7f45e3fe6
    role: context
  - path: pages/traits/physiology/photolithotrophic.html
    sha256: 58c681a80662d001fb7fc3dd0aa2310cd8ce6c6919ad5b139586bcc37da8a7ce
    role: context
  - path: pages/traits/physiology/photoorganoheterotrophic.html
    sha256: ba257273f4dc10bfad18b50997d81e5268b44cc2dd79dbb9d82c0d108acc187f
    role: context
  - path: pages/traits/physiology/phototaxis.html
    sha256: 164663c0d5ab9a375eaad9437cd38ed0591a21a5ef28c7b146a89d2c8a5ea04f
    role: context
  - path: pages/traits/physiology/phototrophic.html
    sha256: 690e38c2c87d99fc97dd1737b688e59137be4afa50aeb99b8e179cf5ca373286
    role: context
  - path: pages/traits/physiology/phototropism.html
    sha256: d5dc11f01b033322a5bfda0d6cacbcea682a0c4de2e0f5f5965ab629a6cb0db5
    role: context
  - path: pages/traits/physiology/pinocytosis.html
    sha256: c8e762b93f849ed58b09add5a94949341c2a6fa1f0be6f3ee8a067ff0f741912
    role: context
  - path: pages/traits/physiology/positive_autotropism.html
    sha256: 9c54076ebabf9694413a946d0a228b3bf90a3fa80dfa8107760c19dacf1e1ab8
    role: context
  - path: pages/traits/physiology/primary_homothallism.html
    sha256: bcd950abdd84074e1c219068362bfca0511fa767ae220eb8c5baea7de4c5869b
    role: context
  - path: pages/traits/physiology/prolyl_aminopeptidase_activity.html
    sha256: 108662a144dddfaeeb5d9c39a95967dda87c865e0991d23864a13239df4c8438
    role: context
  - path: pages/traits/physiology/proteaphagy.html
    sha256: 82220c62049345bea7b44eabb6e2e6d70b35da30104c4fe3cbb9f56b3dc2e5a8
    role: context
  - path: pages/traits/physiology/pseudobipolar_mating_system.html
    sha256: 16df552a9ba55f7a9b803ca30fae85d5b94da6646025eed06b151113beba6c3f
    role: context
  - path: pages/traits/physiology/pseudohomothallism.html
    sha256: fad5db01aecf59e9ff5a9e616f791a48e82badb36cb135b8896843cb61a8409f
    role: context
  - path: pages/traits/physiology/pyrazinamidase_activity.html
    sha256: ecb337143f7ab9c3891ef991e4bcd1496a06b82894bb46a8350b51ad1c0dc538
    role: context
  - path: pages/traits/physiology/pyrrolidonyl_arylamidase_activity.html
    sha256: 5a18c51e8fc0cab98f6abd71987c3d92db4a96d354cd469961c8206fd82dad53
    role: context
  - path: pages/traits/physiology/quorum_quenching.html
    sha256: 6dd6d716c1aaa6d45e57b283c7994b0fef790804b28cdaaa7dffe40d8d3ae5d5
    role: context
  - path: pages/traits/physiology/quorum_sensing.html
    sha256: eefaf41271899f41b5eb2dc284e5921ed99a0b70448f72682820ecdc2ce07de0
    role: context
  - path: pages/traits/physiology/rapid_axopodial_contraction.html
    sha256: c49cf02ef8873d4823d66b5409b65e6ce89920183f6b9939c00125504f902bbd
    role: context
  - path: pages/traits/physiology/rheotaxis.html
    sha256: 2da81bfb9bbccada24c8b7fb235d7f1d947447abf8659393187de0036fb339eb
    role: context
  - path: pages/traits/physiology/rheotropism.html
    sha256: 4b7ffcf0e86b70b4bdaf0676cd091049fdb926a6ac09f2735a9e8f962dc6228e
    role: context
  - path: pages/traits/physiology/ribophagy.html
    sha256: bd2113545c6c60788751788cc69088b2402881f41c2370017b85de7b08c3fecc
    role: context
  - path: pages/traits/physiology/serine_arylamidase_activity.html
    sha256: b285bc9982d540b09de72edd6bb9f39ff5e6f8eadfc396034e7452d0984db246
    role: context
  - path: pages/traits/physiology/siderophore_production.html
    sha256: 98cce412f0b8a8dc666a3d6dcc3c7b8e2a3191339e44c211532ef0bed03b3039
    role: context
  - path: pages/traits/physiology/siliceous_scale_production.html
    sha256: 82f71f79f5167a4e46d17a820a15b6e41ff6d4b6aa89b6dcd6b5fac9c2f4a802
    role: context
  - path: pages/traits/physiology/sos_response.html
    sha256: 6298bf5bebc026f241bb31a860d9d5ad1c25098b4cacc5f642aff4967da6a5a2
    role: context
  - path: pages/traits/physiology/spore_germination.html
    sha256: 9e8fe99ba3eef82ca6b27f5556b77ebce71cd7e1b461fb5a629b9a01cc526427
    role: context
  - path: pages/traits/physiology/stress_response.html
    sha256: e2e83e70c73b3aa7c530f9127fc69c439f0ddeb7848ac1c384bcef7db8d0e00d
    role: context
  - path: pages/traits/physiology/tetrapolar_mating_system.html
    sha256: b8a221c5c565c1e6d757fd09defbc5065250e3c260a82f07354ad910cbdccab4
    role: context
  - path: pages/traits/physiology/thermotaxis.html
    sha256: 6c4015eb5137faa4f0dd76b455434823f1975691f28893448f6a4475ca6ad62e
    role: context
  - path: pages/traits/physiology/thigmotropism.html
    sha256: 5ba8f80a4172ea3a7df7fdd8385c5f61c6683f4b92b216c032ec400c01a188bb
    role: context
  - path: pages/traits/physiology/toxicyst_discharge.html
    sha256: 2d5fe55b64c3c4bbc58c16781a4fac8252bf1f1ea64bda990cac2382ae4e6591
    role: context
  - path: pages/traits/physiology/trichocyst_discharge.html
    sha256: 4b34df9b3900066171d80ab0aea2ec32ac0924d28f6ff11a1485673fcdb65c9c
    role: context
  - path: pages/traits/physiology/tripolar_mating_system.html
    sha256: bdc701ea7f0626afb5d0577169fcc46e4bcad8bd19f157d4413484417044d377
    role: context
  - path: pages/traits/physiology/trogocytosis.html
    sha256: e026aede6adeab2286d197281c70a41eb582d77319c5ad7d3267a9e1d1b3ed36
    role: context
  - path: pages/traits/physiology/trophic_type.html
    sha256: d96184e49e813fe825c8dd91be0d65b65978cbf8b529d6e629b155cf03ed9775
    role: context
  - path: pages/traits/physiology/trypsin_activity.html
    sha256: 44cd7d0e3f0c14e0a589a8092f6d197f88a2baa2eba4deb7de38edf0b0d0648a
    role: context
  - path: pages/traits/physiology/tyrosine_arylamidase_activity.html
    sha256: 8ee0963087154d3b4ab9ee68f5da5888ad193745ab9708fbf395d7000492073e
    role: context
  - path: pages/traits/physiology/unconventional_protein_secretion.html
    sha256: 00ee3847a8aea954984b3cbb6df446d016c782af84912ddbbf8da1cf35e7d0f4
    role: context
  - path: pages/traits/physiology/unisexual_reproduction.html
    sha256: 7c4ca1f423ffdb1da2616dcb5711e2ea5ff0c96a07a1873b7280d8730bfc3c34
    role: context
  - path: pages/traits/physiology/urease_activity.html
    sha256: 38296823b0e6c3f284bea02f0bf5e4ae76a1baee490e9fdb7e705138de3b89c6
    role: context
  - path: pages/traits/physiology/valine_arylamidase_activity.html
    sha256: d9e3efcc46557a6eac224391294d1c982f341b2bbe385d47e52c09c165c28eec
    role: context
  - path: pages/traits/physiology/viable_but_nonculturable_state.html
    sha256: e7b655718148601aec1bb889557ba89d6bc9c29b04ea1f5010249df5f0de5ca3
    role: context
  - path: pages/traits/physiology/viscotaxis.html
    sha256: eb65d24a198220ad64b8bf9d7819b6c5c72e82ef68a3718852d74369b244b71a
    role: context
  - path: pages/traits/quantitative_property/has_maximum_observed_value.html
    sha256: 670f0c846fa8b54af0b9078512f68ef4c77012c9c01a2d96db5ff3d2bc4a3971
    role: context
  - path: pages/traits/quantitative_property/has_minimum_observed_value.html
    sha256: 20d6afc1ca01d59370a06f3b7aa21ec78b667aba53e8b59044ba21dee7eb4cfa
    role: context
  - path: pages/traits/quantitative_property/has_observed_spot_value.html
    sha256: fc64b6450574497051618284bc3574429584bb3afc944dd423bbf6b8a78b37dd
    role: context
  - path: pages/traits/quantitative_property/has_value.html
    sha256: e9f9efd6a1327deeef6eb6c2ad34b0c2fb906f46e1d1b64f9467b9f372f53bd8
    role: context
  - path: pages/traits/quantitative_property/has_value_comments.html
    sha256: aebf0868702a030629836210ca4e9cdbd1f9988e9eae4fd3e5db8b07220f0c66
    role: context
  - path: pages/traits/quantitative_property/is_negative_data.html
    sha256: 775ea67a7896f64900226fc1d9ab7fda74f2f8d5ddd5edd6a68ee8a225cf2cb0
    role: context
  - path: pages/traits/quantitative_property/observation_data_property.html
    sha256: bdef59d1231328e555866137a4cbf965168e4882fddeec3d32445481cfe09192
    role: context
  - path: pages/traits/upper/biological_process.html
    sha256: 48347a453d6729d1bb2d69a27df8248d32f72339b7274ce53aa754521b531da5
    role: context
  - path: pages/traits/upper/chemical_entity.html
    sha256: 75b658dc043af5b5f3feaec6748ecda4bbaf81f8c534faccdb6fba78f1b5c2b5
    role: context
  - path: pages/traits/upper/enzyme.html
    sha256: 3e54558010a9bc03071e1c1391fcb4fa6b5be1e8cfc59202974bd3ccb602ecac
    role: context
  - path: pages/traits/upper/material_entity.html
    sha256: 8c294c91ec50dde1ded08a0dbc18c39ff5cc65cca4ac5cf293157f1c1a4804eb
    role: context
  - path: pages/traits/upper/microbe.html
    sha256: 71c4e2d01812159f2bf4490cc26f3f966a62f97a01f819263c0b4394f50348ec
    role: context
  - path: pages/traits/upper/observation.html
    sha256: bfaff2c6bb883956795d3fdfa2344321a4aaf688dd8c544ec78d8adae6e83353
    role: context
  - path: pages/traits/upper/phenotype.html
    sha256: f70d7ab00fcc4a0b02b84163c88e8242a3a059f201367cead8c2ad10f510dc61
    role: context
  - path: pages/traits/upper/quality.html
    sha256: 24ff91ad69d1820b29bb2b02321651c66cfd6ee8d831f532e82bf25a78040dc8
    role: context
  - path: pages/umap.html
    sha256: d9e742f1f5e925185f054074725545cf4b95c3a6c0ca959802d839d262a25aa0
    role: context
  - path: proposals/metpo_traitmech_v581/metpo_proposal_classes_robot.tsv
    sha256: ad040c5ee87f7aad042404a122ac44adc9df2dae21ac84e5dd121d97cf01ea61
    role: context
  - path: proposals/metpo_traitmech_v581/proposal.md
    sha256: 78cb7dea7073ee37d74be0157cb65da0457f26e005dc40581cdc826e0bfeadfa
    role: context
  - path: reports/metpo_2026_06_12_active_review.tsv
    sha256: 45e9c6471475635ba1f2602cd636a119d490f5dbd8dd6ac8af1aab89a321379f
    role: context
  - path: reports/metpo_2026_06_12_release_delta.tsv
    sha256: afe858d2aa0ade08322c7808d5917ff370e069ba02c2642d483342db8e9323ac
    role: context
  - path: reports/proposal_citation_audit.tsv
    sha256: 064eaeb69ab68b60f0ad2e8ec68d851eeb2527a01a62353961aeaff743385bc3
    role: context
  - path: reports/robot/metpo_traitmech_v581/classes.owl
    sha256: 8175462d208d51b01cf98e57a72a2505e7230379ca1f22a679b40f1394b0fbe1
    role: context
  - path: reports/robot/metpo_traitmech_v581/merged.owl
    sha256: f2cd163414d91b6525b11e5335cc9b789139933323113e293b27ace2bd07c9ce
    role: context
  - path: reports/robot/metpo_traitmech_v581/reasoned.owl
    sha256: 77ad4fff73ecf045b73958712d04d6c1415afbf27a905ea004f98ea34456bc3e
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
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/.vendored_canon_ref
    sha256: 698af47e96e93fe96e81910bb140593a79c2b92c4688892edeab9b63244ec5bf
    role: context
  - path: scripts/add_aerobic_overflow_trait.py
    sha256: f61c52630b50cea16bb53935183b39837871acebaeede8d74bea97346f773f41
    role: context
  - path: scripts/audit_canonical_examples.py
    sha256: 367b9a1759b81e545b06c8dc0c22419ae8d478e3fcd8de6d0bc0cacbb9eacf54
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
  - path: tests/test_add_aerobic_overflow_trait.py
    sha256: 2666fa464b79d306bee07ab0d33332c646ed1d5466c6d90e00bd819838c05734
    role: context
targets:
- target_id: traitmech:000705
  path: data/traits/physiology/aerobic_overflow_metabolism.yaml
  label: aerobic overflow metabolism
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: scripts/add_aerobic_overflow_trait.py
    role: guarded curation writer
  - repository: CultureBotAI/TraitMech
    path: data/traits/physiology/aerobic_overflow_metabolism.yaml
    role: maintained trait record
  - repository: CultureBotAI/TraitMech
    path: proposals/metpo_traitmech_v581/metpo_proposal_classes_robot.tsv
    role: companion METPO proposal
scope:
  description: 'Complete new aerobic-overflow record, writer/tests, proposal, history,
    README and directly generated artifacts. Includes the #1883 correction and add-trait
    evidence guidance.'
  selection: One exact record; no sampling.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - traitmech:000705
  exclusions:
  - target: Other 1,099 TraitRecords
    reason: Novelty/preservation comparisons and deterministic gates, not scientific
      reassessment.
  - target: data/traits/physiology/spore_germination.yaml
    reason: DO_NOT_WORK protected; byte-preserved.
checks:
- check_id: records-0
  name: .venv/bin/linkml-validate -s src/traitmech/schema/traitmech.yaml --target-class
    TraitRecord data/traits/physiology/aerobic_overflow_metabolism.yaml
  command: .venv/bin/linkml-validate -s src/traitmech/schema/traitmech.yaml --target-class
    TraitRecord data/traits/physiology/aerobic_overflow_metabolism.yaml
  status: passed
  required: true
  target_ids:
  - traitmech:000705
  exit_code: 0
  expected_exit_code: 0
  summary: Rerun for the corrected record; native corpus checks are not whole-corpus
    scientific review.
- check_id: records-1
  name: .venv/bin/python scripts/validate_strict.py data/traits/physiology/aerobic_overflow_metabolism.yaml
  command: .venv/bin/python scripts/validate_strict.py data/traits/physiology/aerobic_overflow_metabolism.yaml
  status: passed
  required: true
  target_ids:
  - traitmech:000705
  exit_code: 0
  expected_exit_code: 0
  summary: Rerun for the corrected record; native corpus checks are not whole-corpus
    scientific review.
- check_id: records-2
  name: .venv/bin/python scripts/verify_snippets.py --record data/traits/physiology/aerobic_overflow_metabolism.yaml
    --out /tmp/traitmech-overflow-1883-checks-20261012/snippet-results.tsv
  command: .venv/bin/python scripts/verify_snippets.py --record data/traits/physiology/aerobic_overflow_metabolism.yaml
    --out /tmp/traitmech-overflow-1883-checks-20261012/snippet-results.tsv
  status: passed
  required: true
  target_ids:
  - traitmech:000705
  exit_code: 0
  expected_exit_code: 0
  summary: One scientific-abstract match VERIFIED (Basan); two body quotes NOT_IN_ABSTRACT
    (Molenaar, Hagman), directly checked in retrieved primary XML. Native outcomes
    retained.
- check_id: repair-generate-0
  name: just audit-snippets
  command: just audit-snippets
  status: passed
  required: true
  target_ids:
  - traitmech:000705
  exit_code: 0
  expected_exit_code: 0
  summary: Rerun for the corrected record; native corpus checks are not whole-corpus
    scientific review.
- check_id: repair-generate-1
  name: just gen-qc-dashboard
  command: just gen-qc-dashboard
  status: passed
  required: true
  target_ids:
  - traitmech:000705
  exit_code: 0
  expected_exit_code: 0
  summary: Rerun for the corrected record; native corpus checks are not whole-corpus
    scientific review.
- check_id: repair-generate-2
  name: just gen-pages
  command: just gen-pages
  status: passed
  required: true
  target_ids:
  - traitmech:000705
  exit_code: 0
  expected_exit_code: 0
  summary: Rerun for the corrected record; native corpus checks are not whole-corpus
    scientific review.
- check_id: repair-generate-3
  name: just gen-priority-dashboard
  command: just gen-priority-dashboard
  status: passed
  required: true
  target_ids:
  - traitmech:000705
  exit_code: 0
  expected_exit_code: 0
  summary: Rerun for the corrected record; native corpus checks are not whole-corpus
    scientific review.
- check_id: writer-0
  name: .venv/bin/python -m pytest -q tests/test_add_aerobic_overflow_trait.py
  command: .venv/bin/python -m pytest -q tests/test_add_aerobic_overflow_trait.py
  status: passed
  required: true
  target_ids:
  - traitmech:000705
  exit_code: 0
  expected_exit_code: 0
  summary: 22 guarded-writer tests passed, including one- and two-event preimage upgrades
    and unchanged prior evidence/history.
- check_id: verify-0
  name: just qc
  command: just qc
  status: passed
  required: true
  target_ids:
  - traitmech:000705
  exit_code: 0
  expected_exit_code: 0
  summary: Full QC passed on the committed correction, including derived freshness;
    two existing ENIGMA licensing warnings remain.
- check_id: verify-1
  name: just validate-history
  command: just validate-history
  status: passed
  required: true
  target_ids:
  - traitmech:000705
  exit_code: 0
  expected_exit_code: 0
  summary: Rerun for the corrected record; native corpus checks are not whole-corpus
    scientific review.
- check_id: verify-2
  name: just validate-products
  command: just validate-products
  status: passed
  required: true
  target_ids:
  - traitmech:000705
  exit_code: 0
  expected_exit_code: 0
  summary: 361 canonical labels, two synonyms and one accepted exception; 123 existing
    SKIPPED_NO_ADAPTER rows. No new chemical or protein/taxon example.
- check_id: verify-3
  name: just verify-proposal metpo_traitmech_v581
  command: just verify-proposal metpo_traitmech_v581
  status: passed
  required: true
  target_ids:
  - traitmech:000705
  exit_code: 0
  expected_exit_code: 0
  summary: Rerun for the corrected record; native corpus checks are not whole-corpus
    scientific review.
- check_id: verify-4
  name: just robot-validate-proposal metpo_traitmech_v581
  command: just robot-validate-proposal metpo_traitmech_v581
  status: passed
  required: true
  target_ids:
  - traitmech:000705
  exit_code: 0
  expected_exit_code: 0
  summary: Rerun for the corrected record; native corpus checks are not whole-corpus
    scientific review.
- check_id: verify-5
  name: .venv/bin/ruff check src scripts tests
  command: .venv/bin/ruff check src scripts tests
  status: passed
  required: true
  target_ids:
  - traitmech:000705
  exit_code: 0
  expected_exit_code: 0
  summary: Rerun for the corrected record; native corpus checks are not whole-corpus
    scientific review.
- check_id: tests-0
  name: .venv/bin/python -m pytest -q --junitxml=/tmp/traitmech-overflow-1883-checks-20261012/pytest.xml
  command: .venv/bin/python -m pytest -q --junitxml=/tmp/traitmech-overflow-1883-checks-20261012/pytest.xml
  status: passed
  required: true
  target_ids:
  - traitmech:000705
  exit_code: 0
  expected_exit_code: 0
  summary: 4099 tests passed; no failures, errors or skips.
- check_id: supplemental-0
  name: .venv/bin/python scripts/validate_history_links.py history/records/aerobic_overflow_metabolism
  command: .venv/bin/python scripts/validate_history_links.py history/records/aerobic_overflow_metabolism
  status: passed
  required: true
  target_ids:
  - traitmech:000705
  exit_code: 0
  expected_exit_code: 0
  summary: Rerun for the corrected record; native corpus checks are not whole-corpus
    scientific review.
- check_id: supplemental-1
  name: .venv/bin/linkml-validate --schema src/traitmech/schema/history.yaml --target-class
    HistoryRecord history/records/aerobic_overflow_metabolism/2026-10-12T010648Z-codex-c4f5f8.yaml
  command: .venv/bin/linkml-validate --schema src/traitmech/schema/history.yaml --target-class
    HistoryRecord history/records/aerobic_overflow_metabolism/2026-10-12T010648Z-codex-c4f5f8.yaml
  status: passed
  required: true
  target_ids:
  - traitmech:000705
  exit_code: 0
  expected_exit_code: 0
  summary: Rerun for the corrected record; native corpus checks are not whole-corpus
    scientific review.
- check_id: supplemental-2
  name: .venv/bin/linkml-validate --schema src/traitmech/schema/history.yaml --target-class
    HistoryRecord history/records/aerobic_overflow_metabolism/2026-10-12T010851Z-codex-43a225.yaml
  command: .venv/bin/linkml-validate --schema src/traitmech/schema/history.yaml --target-class
    HistoryRecord history/records/aerobic_overflow_metabolism/2026-10-12T010851Z-codex-43a225.yaml
  status: passed
  required: true
  target_ids:
  - traitmech:000705
  exit_code: 0
  expected_exit_code: 0
  summary: Rerun for the corrected record; native corpus checks are not whole-corpus
    scientific review.
- check_id: supplemental-3
  name: .venv/bin/linkml-validate --schema src/traitmech/schema/history.yaml --target-class
    HistoryRecord history/records/aerobic_overflow_metabolism/2026-10-12T015455Z-codex-b0453d.yaml
  command: .venv/bin/linkml-validate --schema src/traitmech/schema/history.yaml --target-class
    HistoryRecord history/records/aerobic_overflow_metabolism/2026-10-12T015455Z-codex-b0453d.yaml
  status: passed
  required: true
  target_ids:
  - traitmech:000705
  exit_code: 0
  expected_exit_code: 0
  summary: Rerun for the corrected record; native corpus checks are not whole-corpus
    scientific review.
- check_id: supplemental-4
  name: .venv/bin/python scripts/audit_canonical_examples.py --no-resolve
  command: .venv/bin/python scripts/audit_canonical_examples.py --no-resolve
  status: passed
  required: true
  target_ids:
  - traitmech:000705
  exit_code: 0
  expected_exit_code: 0
  summary: 761 examples across 576 records, zero shape errors/warnings; authority
    resolution not run because no examples changed.
- check_id: supplemental-5
  name: .venv/bin/python scripts/run_trait_graph_audit.py --verify
  command: .venv/bin/python scripts/run_trait_graph_audit.py --verify
  status: passed
  required: true
  target_ids:
  - traitmech:000705
  exit_code: 0
  expected_exit_code: 0
  summary: Research-artifact integrity only; acquisition counts are not scientific
    review counts.
- check_id: supplemental-6
  name: .venv/bin/python scripts/audit_history_records.py --base 8abebd0652f3de39d8de1d86a246cfe768df7bcc
  command: .venv/bin/python scripts/audit_history_records.py --base 8abebd0652f3de39d8de1d86a246cfe768df7bcc
  status: passed
  required: true
  target_ids:
  - traitmech:000705
  exit_code: 0
  expected_exit_code: 0
  summary: Rerun for the corrected record; native corpus checks are not whole-corpus
    scientific review.
- check_id: supplemental-7
  name: git diff --check 8abebd0652f3de39d8de1d86a246cfe768df7bcc HEAD -- . ':(exclude)proposals/metpo_traitmech_v581/metpo_proposal_classes_robot.tsv'
  command: git diff --check 8abebd0652f3de39d8de1d86a246cfe768df7bcc HEAD -- . ':(exclude)proposals/metpo_traitmech_v581/metpo_proposal_classes_robot.tsv'
  status: passed
  required: true
  target_ids:
  - traitmech:000705
  exit_code: 0
  expected_exit_code: 0
  summary: Rerun for the corrected record; native corpus checks are not whole-corpus
    scientific review.
- check_id: supplemental-8
  name: git -c core.whitespace=-blank-at-eol diff --check 8abebd0652f3de39d8de1d86a246cfe768df7bcc
    HEAD -- proposals/metpo_traitmech_v581/metpo_proposal_classes_robot.tsv
  command: git -c core.whitespace=-blank-at-eol diff --check 8abebd0652f3de39d8de1d86a246cfe768df7bcc
    HEAD -- proposals/metpo_traitmech_v581/metpo_proposal_classes_robot.tsv
  status: passed
  required: true
  target_ids:
  - traitmech:000705
  exit_code: 0
  expected_exit_code: 0
  summary: Rerun for the corrected record; native corpus checks are not whole-corpus
    scientific review.
- check_id: direct-source
  name: Manual claim support and direct source verification
  status: passed
  required: true
  target_ids:
  - traitmech:000705
  evidence_ids:
  - identity
  - bacterial
  - yeast
  - resolution
  summary: Exact 18-word positive Results span, correct section locator and oxygen-control
    context verified. Molenaar body sentence and surrounding definition paragraph
    confirmed.
- check_id: browser
  name: Desktop/mobile Playwright and visual inspection
  status: passed
  required: true
  target_ids:
  - traitmech:000705
  evidence_ids:
  - products
  command: TRAITMECH_HISTORY_COUNT=3 TRAITMECH_SCREEN_PREFIX=/tmp/traitmech-overflow-1883
    node /tmp/traitmech-overflow-browser-20261012.cjs
  exit_code: 0
  expected_exit_code: 0
  summary: '1440px and 390px: corrected third quote, three history links, browse/parent
    navigation, loaded coverage image, no horizontal overflow or page errors. Six
    screenshots visually inspected. Sandbox launch failed before navigation; approved
    retry passed.'
- check_id: embeddings
  name: Embedding applicability
  status: not_applicable
  required: false
  target_ids:
  - traitmech:000705
  summary: Exact configured sources absent; existing artifacts retained, not regenerated.
evidence:
- evidence_id: identity
  kind: primary_source
  reference: DOI:10.1038/msb.2009.82
  locator: 'Current growth models and their limitations: exact quoted sentence and
    full surrounding paragraph reinspected; broader modeling context retained from
    the earlier full review.'
  accessed_at: '2026-10-12T02:21:43Z'
  support: supports
  summary: Aerobic incomplete oxidation with retained respiration grounds the qualified
    phenotype. The quoted body sentence describes S. cerevisiae and E. coli; this
    original modeling Perspective is not new experimental replication. Its broader
    mixed-acid-to-lactate usage is not silently equated with the qualified label.
  snapshot_sha256: 613b89c59e3c7d4254450c443c9d4562adb15df54dcf20f02c19f67f1484c1f5
- evidence_id: bacterial
  kind: primary_source
  reference: DOI:10.1038/nature15765
  locator: Scientific abstract reinspected; selected Results, Methods, Extended Data
    Table 1, actual Figure 1 and Extended Data Figure 2 assessed in the earlier full
    review and unchanged.
  accessed_at: '2026-10-12T02:21:43Z'
  support: supports
  summary: Acetate excretion during aerobic E. coli growth supports the phenotype.
    Proteome-allocation explanation and fitted threshold are system-specific. Oxidative
    accounting includes NADH oxidation using oxygen; net excretion does not exclude
    reuptake. Reference and engineered strains are not universal natural canonical
    examples. Complete supplements/equations and cited batch methods were not independently
    reanalyzed.
  snapshot_sha256: 0c2d9c2b51d95be43e4b91bdcb5f64745cf22071349782eef422703176c8d3ba
- evidence_id: yeast
  kind: primary_source
  reference: DOI:10.1111/febs.13019
  locator: Results and Discussion / Consumption of glucose and generation of biomass
    and ethanol; Experimental procedures. Actual Figures 1-2 inspected in the earlier
    full review.
  accessed_at: '2026-10-12T02:21:43Z'
  support: supports
  summary: The replacement is an exact 18-word positive ethanol-formation Results
    span, not a measurement list. Its paragraph distinguishes responsive and nonresponsive
    tested yeasts. Methods maintain dissolved oxygen above 30% air saturation in initially
    respiratory, glucose-limited cultures. The respiratory-repression qualifier and
    replication/supplementation limits remain unchanged. Full supplementary time series
    and strain origins were not reviewed.
  snapshot_sha256: 1e7bfc8e5b6a5e0166874af6e4054537562740da7482523b8f54f31485a87e33
- evidence_id: notices
  kind: authority
  reference: https://europepmc.org/article/MED/25161062
  locator: Exact DOI Crossref and source-qualified MED metadata for all three citations;
    accessible publisher pages.
  accessed_at: '2026-10-12T01:37:05Z'
  support: context_only
  summary: DOI/PMID/PMC identity and source sections checked. Retrieved metadata exposed
    no linked correction or retraction; this bounded result is not proof of absence.
    Basan publisher retrieval failed, while public XML/figure assets were accessible.
- evidence_id: content
  kind: record_content
  reference: data/traits/physiology/aerobic_overflow_metabolism.yaml
  locator: Complete corrected record, full guarded writer and 22 tests, three append-only
    history records, v581 proposal and skill clarification.
  accessed_at: '2026-10-12T02:21:43Z'
  support: supports
  summary: One PROPOSED PHYSIOLOGY class under phenotype. No exact synonyms, xrefs,
    canonical examples or graph. Two OPEN discussions preserve hierarchy and provenance/mechanism
    gaps. Oxygen presence or product detection alone is not diagnosis. Fermentation,
    product-specific traits, aerotolerance, facultative anaerobiosis, copiotrophy
    and diauxie are distinct axes.
- evidence_id: correction
  kind: record_content
  reference: https://github.com/CultureBotAI/TraitMech/issues/1881
  locator: Corrected yeast evidence notes, CLARIFIED_EVIDENCE_SCOPE event, EDIT history
    and original-preimage upgrade regression test.
  accessed_at: '2026-10-12T01:37:05Z'
  support: supports
  summary: The drafting defect was filed and corrected before this formal inspection.
    Original CREATE history and curation event remain unchanged. Current text attributes
    the authors' repression claim without asserting monotonic respiration. This is
    not a successor disposition of a nonexistent saved review.
- evidence_id: novelty
  kind: search
  reference: proposals/metpo_traitmech_v581/proposal.md
  locator: Ignored/hidden searches, structured YAML comparisons, pinned/current ontology
    and templates, full paginated pending-PR files, fresh reservations. Fresh head/file/ignored-inclusive
    worktree comparison after correction; owned PR1882 excluded only from foreign-reservation
    comparisons.
  accessed_at: '2026-10-12T02:08:55.353841Z'
  support: supports
  summary: No exact active/deprecated match or overlapping allocation found in declared
    scope. Reserve local 000705, cohort v581, full METPO1065800-1065899 block; only
    1065800 populated. Editable OWL root is imports-only and is not used alone to
    establish absence.
  search_scope: '22 pre-existing TraitMech worktrees plus owned refresh; 1,114 distinct
    pre-addition YAML versions; 580 cohorts and 4,088 narrative intervals; 127 CommunityMech
    roots and 530 proposal files; 644 METPO issue/PR bodies and 654 issue comments.
    Fresh 399-record seed versus 1,099 existing records; 55 absent IDs are leads.
    Frozen 1,546-row and 153-row tables and complete pending METPO #629 documents
    checked. Ignored/hidden included, normal binary handling; no archive unpacking,
    symlink-directory traversal, unregistered/private work or exhaustive review-thread
    claim. Not global exhaustion.'
- evidence_id: products
  kind: validation
  reference: reports/proposal_citation_audit.tsv
  locator: Native QC/schema/history/products, full and focused tests, parsed RDF,
    byte comparisons, browser assertions and six visually inspected desktop/mobile
    screenshots.
  accessed_at: '2026-10-12T02:21:43Z'
  support: supports
  summary: 'Correction gates and full tests passed; 4099 tests. All 1,099 old YAMLs
    and earlier histories/reviews preserved. 1,098 old pages have footer-only changes;
    phenotype gains one child. Three curation histories and corrected body snippet
    render at both widths. Parsed RDF: {''classes'': 15, ''merged'': 12628, ''reasoned'':
    12632}.'
- evidence_id: resolution
  kind: record_content
  reference: https://github.com/CultureBotAI/TraitMech/issues/1883
  locator: evidence[2], guarded build_record upgrade, new two-event regression, REPLACED_UNSUPPORTIVE_SNIPPET
    and third repository history; add-trait evidence guidance.
  accessed_at: '2026-10-12T02:21:43Z'
  support: supports
  summary: Changed only the unsupportive quote and source locator within evidence;
    first two evidence entries and both old history events remain unchanged. Native
    resolver correctly changes Hagman from VERIFIED to NOT_IN_ABSTRACT. The 25-word
    limit is retained. Skill now requires claim-bearing snippets rather than accepting
    a methods-only statement.
- evidence_id: external
  kind: prior_review
  reference: https://github.com/CultureBotAI/TraitMech/pull/1882#pullrequestreview-5485934905
  locator: Yellow Hagman snippet finding; exact reviewed head c4e64607a1f072a3accd3eeeb8174b380be1c68a.
  accessed_at: '2026-10-12T01:53:07Z'
  support: supports
  summary: The external reviewer identifies a real mismatch between measurement-description
    prose and a trait-supporting snippet. This successor confirms the defect and evaluates
    its correction, without treating the external request itself as approval of the
    new head.
assessments:
- assessment_id: identity
  area: identity
  topic: Conditional aerobic phenotype
  summary: Organism-level physiological disposition, not a gene or universal pathway.
    The aerobic qualifier restricts broader overflow terminology.
  target_ids:
  - traitmech:000705
  evidence_ids:
  - identity
  - bacterial
  - yeast
  - content
  outcome: supported
- assessment_id: boundaries
  area: identity
  topic: Oxygen and yield scope
  summary: Sufficient oxygen and respiratory capacity distinguish the trait from oxygen
    limitation. No universal product, substrate, concentration or growth threshold
    is imposed.
  target_ids:
  - traitmech:000705
  evidence_ids:
  - identity
  - bacterial
  - yeast
  outcome: supported
- assessment_id: novelty
  area: identity
  topic: Bounded novelty and allocation
  summary: No exact inspected match or occupied full block; prior butanediol evidence
    and research leads do not denote the same record.
  target_ids:
  - traitmech:000705
  evidence_ids:
  - novelty
  outcome: supported
- assessment_id: hierarchy
  area: grounding
  topic: Phenotype parent
  summary: Process-shaped metabolism and donor/acceptor-defined fermentation are not
    treated as broader organismal traits. Frozen local/pinned differences and upstream
    issue468 are explicit. RDF has actual w3id phenotype-to-quality hierarchy.
  target_ids:
  - traitmech:000705
  evidence_ids:
  - content
  - products
  outcome: supported
- assessment_id: sources
  area: evidence
  topic: Exact section-qualified evidence
  summary: 'Three contiguous primary-source quotes: one scientific-abstract match
    and two directly confirmed body spans. Hagman now states the positive ethanol
    result; oxygen-control context is in notes. Molenaar access concern resolved by
    exact source location and publicly retrievable XML, not by changing its resolver
    verdict.'
  target_ids:
  - traitmech:000705
  evidence_ids:
  - identity
  - bacterial
  - yeast
  - notices
  - resolution
  - external
  outcome: supported
- assessment_id: history
  area: provenance
  topic: Guarded writer and correction
  summary: Guarded dry run, exact one- and two-event preimages, parent/proposal drift
    rejection, prevalidation and replay are tested. Both corrections append history;
    all prior review bundles remain byte-preserved. No mapping-status promotion.
  target_ids:
  - traitmech:000705
  evidence_ids:
  - content
  - correction
  - products
  - resolution
  outcome: supported
- assessment_id: products
  area: consistency
  topic: Preservation and generated artifacts
  summary: Required gates and full tests pass. Counts, proposal width, RDF and browser
    views agree; unrelated records unchanged.
  target_ids:
  - traitmech:000705
  evidence_ids:
  - products
  outcome: supported
- assessment_id: gaps
  area: completeness
  topic: Examples and mechanism deferred
  summary: No natural canonical taxa, universal protein mechanism or exact external
    equivalence asserted without necessary evidence; upstream acceptance remains open.
  target_ids:
  - traitmech:000705
  evidence_ids:
  - content
  - bacterial
  - yeast
  outcome: unknown
findings:
- finding_id: yeast-snippet-support
  issue_key: github-1883-yeast-overflow-snippet
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: Yeast snippet does not state the supporting phenotype result
  description: The prior quotation was verbatim but only described data generation.
    The source supported the trait in other passages; this was a bounded snippet-selection
    defect, not a wrong citation or invalid trait. The current quotation states the
    positive result.
  target_ids:
  - traitmech:000705
  field_paths:
  - evidence[2].snippet
  evidence_ids:
  - yeast
  - resolution
  - products
  - external
  rule_id: UNSUPPORTIVE_SNIPPET
  native_severity: yellow external review finding
  normalization_reason: Minor because the relevant source and qualified notes are
    sound and two other citations independently support the phenotype.
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: scripts/add_aerobic_overflow_trait.py
    role: guarded curation writer
  - repository: CultureBotAI/TraitMech
    path: data/traits/physiology/aerobic_overflow_metabolism.yaml
    role: maintained trait record
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/1883
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261012T015307Z-aerobic-overflow-snippet-finding
    finding_id: yeast-snippet-support
  disposition_reason: The current exact 18-word Results quote reports significant
    ethanol formation after a glucose pulse. Its section and oxygen-controlled assay
    context were directly rechecked. Writer upgrade tests, schema, snippet, history,
    generated products, full suite and browser checks pass. Both previous events and
    review bundles remain unchanged.
actions: []
limitations:
- Author self-review, not independent or human signoff; one complete trait assessed,
  not every hashed corpus input.
- Current changed record/writer/tests/skill/proposal/history and primary quotation
  contexts reinspected. Unchanged selected source figures, broader source analysis
  and novelty findings carry forward from the linked initial review; no new whole-paper
  or whole-corpus scientific review is claimed.
- Source access times denote inspection, not necessarily download. Molenaar and Hagman
  remain NOT_IN_ABSTRACT; direct full-text checks do not relabel native outcomes.
- Relevant sections and selected figures only; complete raw data, supplements, equations,
  strain origins and all cited methods were not reviewed. Basan publisher inaccessible;
  public full-text XML used.
- Canonical natural examples, protein mechanisms and upstream hierarchy acceptance
  remain explicit gaps. No authority-resolution claim from the no-resolve example
  audit.
- Product validation retains 123 existing SKIPPED_NO_ADAPTER rows; two existing ENIGMA
  licensing warnings remain.
- Ignored/hidden-inclusive novelty scope excludes archives, symlink-directory traversal
  and unregistered/private work; no global trait-exhaustion claim.
- Neither exact embedding source exists. Required trailing ROBOT directive cells use
  only the documented exact-path whitespace exception.
- 'Issue1881 was corrected before initial review; #1883 has an explicit predecessor
  finding and resolved successor. External approval of the new head and CI/queue admission
  remain later PR lifecycle gates.'
tags:
- add-trait
- aerobic-overflow
- self-review
related_reviews:
- repository: CultureBotAI/TraitMech
  review_id: 20261012T013705Z-aerobic-overflow
  relationship: Reassesses the full record after the snippet defect missed by the
    initial pass.
- repository: CultureBotAI/TraitMech
  review_id: 20261012T015307Z-aerobic-overflow-snippet-finding
  relationship: Resolves the confirmed yeast-snippet-support finding after source-based
    correction and validation.
```
