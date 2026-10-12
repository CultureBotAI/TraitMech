# Full successor review of aggregate inheritance after reporter qualification

- Review: 20261012T184416Z-aggregate-inheritance-reporter-successor
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-12T18:43:22Z
- Finished UTC: 2026-10-12T18:44:16Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Reassessed the complete corrected record and associated changes. The one confirmed reporter-evidence finding is resolved; no new actionable defect was identified. The broad phenotype remains PROPOSED with explicit assay and mechanism limits.

## Scope And Provenance

Complete new record and maintained/generated change set; no whole-corpus scientific review.

Selection: One exact newly curated trait, no sampling.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base de5cdeb55090af00e5313ac03482a8ace9136a21.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| traitmech:000711 | data/traits/physiology/unequal_protein_aggregate_inheritance.yaml | maintained | unequal protein aggregate inheritance at cell division |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python -m pytest -q tests/test_add_unequal_protein_aggregate_inheritance_trait.py tests/test_qualify_aggregate_inheritance_reporter.py | passed | True | traitmech:000711 | 32 focused tests pass, including historical preservation, correction replay, preimage guards, proposal/source consistency and prevalidation failure without writes. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate -s src/traitmech/schema/traitmech.yaml --target-class TraitRecord data/traits/physiology/unequal_protein_aggregate_inheritance.yaml | passed | True | traitmech:000711 | Executed native gate passed on the corrected content; deterministic corpus validation is not whole-corpus scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/validate_strict.py data/traits/physiology/unequal_protein_aggregate_inheritance.yaml | passed | True | traitmech:000711 | Executed native gate passed on the corrected content; deterministic corpus validation is not whole-corpus scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/verify_snippets.py --record data/traits/physiology/unequal_protein_aggregate_inheritance.yaml --out /tmp/traitmech-aggregate-inheritance-reporter-checks-20261012/snippet-results.tsv | passed | True | traitmech:000711 | Four snippets: two VERIFIED scientific-abstract matches and two NOT_IN_ABSTRACT Results quotations checked directly in primary full text. Native outcomes are not relabeled. |
| just audit-proposals | passed | True | traitmech:000711 | Executed native gate passed on the corrected content; deterministic corpus validation is not whole-corpus scientific review. |
| just ground-predicates | passed | True | traitmech:000711 | Executed native gate passed on the corrected content; deterministic corpus validation is not whole-corpus scientific review. |
| just ground-nodes | passed | True | traitmech:000711 | Executed native gate passed on the corrected content; deterministic corpus validation is not whole-corpus scientific review. |
| just audit-graphs | passed | True | traitmech:000711 | Executed native gate passed on the corrected content; deterministic corpus validation is not whole-corpus scientific review. |
| just audit-graph-protein-taxa | passed | True | traitmech:000711 | Executed native gate passed on the corrected content; deterministic corpus validation is not whole-corpus scientific review. |
| just audit-predicate-domains | passed | True | traitmech:000711 | Executed native gate passed on the corrected content; deterministic corpus validation is not whole-corpus scientific review. |
| just check-biolink-coverage | passed | True | traitmech:000711 | Executed native gate passed on the corrected content; deterministic corpus validation is not whole-corpus scientific review. |
| just audit-snippets | passed | True | traitmech:000711 | Executed native gate passed on the corrected content; deterministic corpus validation is not whole-corpus scientific review. |
| just gen-discussions-data | passed | True | traitmech:000711 | Executed native gate passed on the corrected content; deterministic corpus validation is not whole-corpus scientific review. |
| just gen-qc-dashboard | passed | True | traitmech:000711 | Executed native gate passed on the corrected content; deterministic corpus validation is not whole-corpus scientific review. |
| just gen-pages | passed | True | traitmech:000711 | Executed native gate passed on the corrected content; deterministic corpus validation is not whole-corpus scientific review. |
| just gen-priority-dashboard | passed | True | traitmech:000711 | Executed native gate passed on the corrected content; deterministic corpus validation is not whole-corpus scientific review. |
| just qc | passed | True | traitmech:000711 | Executed native gate passed on the corrected content; deterministic corpus validation is not whole-corpus scientific review. |
| just validate-history | passed | True | traitmech:000711 | Executed native gate passed on the corrected content; deterministic corpus validation is not whole-corpus scientific review. |
| just validate-products | passed | True | traitmech:000711 | Executed native gate passed on the corrected content; deterministic corpus validation is not whole-corpus scientific review. |
| just verify-proposal metpo_traitmech_v587 | passed | True | traitmech:000711 | Executed native gate passed on the corrected content; deterministic corpus validation is not whole-corpus scientific review. |
| just robot-validate-proposal metpo_traitmech_v587 | passed | True | traitmech:000711 | Executed native gate passed on the corrected content; deterministic corpus validation is not whole-corpus scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/ruff check src scripts tests | passed | True | traitmech:000711 | Executed native gate passed on the corrected content; deterministic corpus validation is not whole-corpus scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python -m pytest -q --junitxml=/tmp/traitmech-aggregate-inheritance-reporter-checks-20261012/pytest.xml | passed | True | traitmech:000711 | 4274 full-suite tests passed without skips, failures or errors. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/validate_history_links.py history/records/unequal_protein_aggregate_inheritance | passed | True | traitmech:000711 | Executed native gate passed on the corrected content; deterministic corpus validation is not whole-corpus scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate --schema src/traitmech/schema/history.yaml --target-class HistoryRecord history/records/unequal_protein_aggregate_inheritance/2026-10-12T144228Z-codex-c658f7.yaml | passed | True | traitmech:000711 | Executed native gate passed on the corrected content; deterministic corpus validation is not whole-corpus scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate --schema src/traitmech/schema/history.yaml --target-class HistoryRecord history/records/unequal_protein_aggregate_inheritance/2026-10-12T182646Z-codex-9c4b15.yaml | passed | True | traitmech:000711 | Executed native gate passed on the corrected content; deterministic corpus validation is not whole-corpus scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/audit_canonical_examples.py --no-resolve | passed | True | traitmech:000711 | 761 existing examples across 576 records passed shape checks with zero errors/warnings. --no-resolve does not verify taxonomy existence or labels; no canonical example was added or changed. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/run_trait_graph_audit.py --verify | passed | True | traitmech:000711 | Executed native gate passed on the corrected content; deterministic corpus validation is not whole-corpus scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/audit_history_records.py --base a57b006b32f2313579650d105d7da245a99a5b95 | passed | True | traitmech:000711 | Executed native gate passed on the corrected content; deterministic corpus validation is not whole-corpus scientific review. |
| git diff --check a57b006b32f2313579650d105d7da245a99a5b95 HEAD -- . ':(exclude)proposals/metpo_traitmech_v587/metpo_proposal_classes_robot.tsv' | passed | True | traitmech:000711 | Executed native gate passed on the corrected content; deterministic corpus validation is not whole-corpus scientific review. |
| git -c core.whitespace=-blank-at-eol diff --check a57b006b32f2313579650d105d7da245a99a5b95 HEAD -- proposals/metpo_traitmech_v587/metpo_proposal_classes_robot.tsv | passed | True | traitmech:000711 | Executed native gate passed on the corrected content; deterministic corpus validation is not whole-corpus scientific review. |
| Corrected desktop/mobile generated products | passed | True | traitmech:000711 | 1440/390 px assertions passed: four quotations, three discussions, two history links, correct local identity, navigation and dashboard. Ten screenshots, including the fourth evidence item, visually inspected; no horizontal overflow or page errors. |
| Pinned generator and exact embedding-source applicability | passed | True | traitmech:000711 | 152 pinned generator blobs verified. Neither configured embedding source exists in the primary/owned layouts; existing embeddings retained. |

## Scientific And Domain Assessments

### Recurrent inheritance phenotype

identity: supported. Targets: traitmech:000711.

The unchanged definition describes recurrent inherited count/amount differences, not aggregate formation, reporter presence or a single split.

### Reporter-dependent clustering and separately validated conditions

evidence: supported. Targets: traitmech:000711.

The older reporter readout is retained as historical focus behavior, not independent proof of endogenous unstressed aggregation; the later study is qualified by reporter and stress context.

### Cargo amount versus concentration and population bias

quantity: supported. Targets: traitmech:000711.

Within-pair inequality, cell-type allocation, exclusion, concentration, projected area and volume remain distinguished. No fixed pole bias or universal harm/benefit is inferred.

### Active broader parent and historical lexical hit

grounding: supported. Targets: traitmech:000711.

Phenotype remains the broader parent; neighboring processes are not equated. Obsolete aggregate remains historical context, not a reused or exact-cross-referenced term.

### Append-only correction lineage

provenance: supported. Targets: traitmech:000711.

Original event, sidecar assessment and prior saved reviews remain; the correction has issue-linked history and a guarded writer. All four snippets have direct source support.

### Generated products and guarded writes

consistency: supported. Targets: traitmech:000711.

Native gates, full regression tests, RDF inspection and responsive browser checks pass with preserved prior records and no unrelated maintained changes.

### Unresolved optional scope and mechanism work

completeness: unknown. Targets: traitmech:000711.

Natural strain exemplars, universal thresholds and a shared causal graph remain deliberately unasserted. Coelho panel/temperature source discrepancies remain explicit.

## Findings

### reporter-bias: Unstressed reporter foci need a label-induced clustering qualification

major / resolved / confirmed; issue key: aggregate-inheritance-ibpa-yfp-reporter-bias.

The notes overstate the evidential role of the older reporter experiment without the later primary assay limitation. Retain the historical quote, qualify the readout and cite the later evidence.

Disposition: The older quote is explicitly restricted to reporter-focus behavior, the later assay challenge and distinct post-stress evidence are cited, and guarded regression/validation/product checks pass. Scientific content correction is complete; external review, CI, queue and issue closure remain subsequent lifecycle gates.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| source-0 | DOI:10.1073/pnas.0708931105; Results: Inclusion Bodies Are Formed in Discrete Cellular Positions and Accumulate in Old Poles Under Nonstressing Conditions; /html/body/div[2]/div[2]/div/div[1]/div/div[2]/main/article/section[2]/section/section[2]/section[2]/p | partial | Lindner et al. 2008, PMID:18287048, PMC2268587; Results, Inclusion Bodies Are Formed in Discrete Cellular Positions and Accumulate in Old Poles Under Nonstressing Conditions. Primary PMC Results and Methods directly read. The quoted position is that of an IbpA-YFP focus. MGAY is an engineered MG1655 reporter strain, grown on LB-agarose at 37 C without imposed stress. Figure 2 is the inspected localization measurement; Figure 3 is an inspected lineage schematic, not another experiment. Pole identity changes across divisions. These observations describe reporter-focus inheritance and eventual older-pole accumulation. Govers et al. 2018 (DOI:10.1371/journal.pbio.2003853) subsequently demonstrated label-induced clustering with IbpA-YFP. The older readout is not independent proof of endogenous unstressed aggregation; naming the engineered strain alone does not resolve this assay bias. Neither active transport, universal aggregate toxicity nor a natural canonical exemplar is established. Supplements were not inspected. The full-text span retains the native abstract resolver verdict NOT_IN_ABSTRACT. |
| source-1 | DOI:10.1371/journal.pbio.1001886; Scientific abstract, not Author Summary; /article/front/article-meta/abstract[2]/p | supports | Coelho et al. 2014, PMID:24936793, PMC4061010; scientific abstract, not Author Summary. Primary XML and actual Figures 3, 4 and S4 were inspected. Hsp104-GFP fission-yeast imaging supports stress-associated unequal inheritance without consistent old/new-pole bias. Figure 3C measures an absolute sibling difference in aggregate-associated fluorescence, not concentration; S4I measures count asymmetry. Figure 4B is fusion and 4C is nucleation: the caption reverses them. A Results pointer to 4C for stress-dependent asymmetry disagrees with the plotted endpoints. Figure 3C describes continuous 40 C, whereas Methods describes 40 C for one hour followed by 37 C; this remains unresolved. Text S1 experimental methods and strain table were text-extracted, not visually rendered. No universal transport, death threshold or rejuvenation mechanism is inferred. The scientific-abstract span matches the native resolver text (VERIFIED). |
| source-2 | DOI:10.1111/mmi.14228; Results: The aggregate load does not sort to swarmer or stalked daughter cells in C. crescentus; /article/body/sec[2]/sec[5]/p[5] | supports | Schramm et al. 2019, PMID:30779464, PMC6850343; Results, The aggregate load does not sort to swarmer or stalked daughter cells in C. crescentus. Primary XML Results, Discussion and relevant Methods were read; actual Figure 6 was inspected. DnaK-mVenus, delta-clpB cells recovered at 30 C after 10 minutes at 40 C. Figure 6G reports aggregate allocation across daughter cell types over successive divisions, not the fraction of all sibling pairs with unequal counts. Figure 6F measures projected cell area, not volume. Unequal shared inheritance is compatible with the broad phenotype; it contradicts neither sharing nor a stable allocation ratio. The paper limits universal exclusive old-pole retention, not every form of quantitative inequality. Supplements and independent strain provenance were not inspected; no natural canonical example is asserted. The full-text span retains the native abstract resolver verdict NOT_IN_ABSTRACT. |
| source-3 | DOI:10.1371/journal.pbio.2003853; article/front/article-meta/abstract/p; Scientific abstract; Results sec003, sec004 and sec006; Methods sec014, sec017, sec018 and sec021; actual Figures 1 and 3. | supports | Govers et al. 2018, PMID:30153247, PMC6112618; scientific abstract, directly matched in primary XML and source-qualified MED. Results on reporter validation and post-stress inheritance, relevant Methods and actual Figures 1 and 3 were inspected. Figure 1 shows reporter-dependent clustering; Figure 3 separately follows engineered MG1655 IbpA-msfGFP lineages after 47 C for 15 minutes, with microscopy at 37 C. Focus inheritance is distinct from the fluorescence concentration and growth readouts. This does not validate unstressed IbpA-YFP foci as endogenous aggregates or imply universal harm, benefit, aging or rejuvenation. Supplementary controls were read only where described in Results; their images, raw data and independent strain provenance were not assessed. |
| novelty | proposals/metpo_traitmech_v587/proposal.md; Discovery and accepted-scope receipts, pre-allocation audit and successful stable publication refresh. | supports | No exact trait or competing reservation in inspected scope. Namespace envelope is guarded by exact file hash/context, not treated as a term/cohort reservation. No deprecation override, exact xref or silent ontology upgrade. Retained original acceptance assessment: this correction changes neither identity, parent nor reserved IDs; publication freshness is a separate gate. |
| obsolete | METPO:1000011; Pinned/current released RDF and frozen release review, captured in source sidecar. | supports | Deprecated obsolete aggregate has no definition/replacement/consider in inspected snapshots; reason annotation OMO:0001000 is not independently interpreted. Lexical similarity does not establish inheritance-phenotype identity; historical ID is neither reused nor xrefed. Retained original acceptance assessment: this correction changes neither identity, parent nor reserved IDs; publication freshness is a separate gate. |
| content | data/traits/physiology/unequal_protein_aggregate_inheritance.yaml; Complete corrected YAML, both guarded writers, tests, proposal, history, sidecar, skill and generated page. | supports | Four source-qualified evidence items; identity, definition, parent and PROPOSED status unchanged. Original event, historical source assessment and both prior reviews are preserved. |
| products | reports/proposal_citation_audit.tsv; Native gates, preservation checks, parsed ROBOT RDF and desktop/mobile views. | supports | All 1105 earlier YAMLs, prior history/reviews/proposals/embeddings and shared templates are preserved. One new trait remains; parsed RDF counts {'classes': 15, 'merged': 12628, 'reasoned': 12632}. Required trailing ROBOT header cells are preserved. |
| finding | reviews/structured/20261012T182317Z-aggregate-reporter-bias-finding/review.yaml; findings[reporter-bias] | supports | The previously open source-qualification finding is reassessed against the guarded correction and newly inspected primary evidence. This supersedes its content disposition, not its historical record. |

## Limits And Additional Notes

- Author self-review, not independent or human scientific sign-off; native status remains PROPOSED.
- No universal reporter validity, recurrence threshold, pole preference, toxicity, benefit, aging or rejuvenation mechanism is asserted.
- No raw-data reanalysis. New primary Figures 1 and 3 inspected; supplementary images/movies and independent strain provenance not assessed. Earlier source-specific access and figure limits remain.
- Original novelty and reservation coverage remains bounded and included ignored/hidden files; fresh publication checks are separate. No global discovery-exhaustion claim.
- The full-suite and QC baseline warnings/skipped adapters remain baseline limitations; embeddings were not regenerated because configured sources are absent.
- The proposed TSV keeps required trailing empty header cells; exact-path scoped whitespace checks accompany the original whole-PR header finding.
- Resolving the source-qualification finding does not certify future external approval, PR/merge-group CI, issue closure, landed integrity or branch cleanup.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T184416Z-aggregate-inheritance-reporter-successor
kind: record
repository: CultureBotAI/TraitMech
title: Full successor review of aggregate inheritance after reporter qualification
started_at: '2026-10-12T18:43:22Z'
finished_at: '2026-10-12T18:44:16Z'
reviewer:
  identity: codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Author source-based adversarial assessment, not independent
    review or human sign-off.
skill: .claude/skills/add-trait/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Reassessed the complete corrected record and associated changes. The one
  confirmed reporter-evidence finding is resolved; no new actionable defect was identified.
  The broad phenotype remains PROPOSED with explicit assay and mechanism limits.
source:
  git_revision: de5cdeb55090af00e5313ac03482a8ace9136a21
  state: working_tree
  inputs:
  - path: .claude/skills/add-trait/SKILL.md
    sha256: 672311dea080c70cac71654bedf49f2a6e21250b67e2cff4ad1962778b80e00a
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
    sha256: 723cf346902793deff8ccbeb48ce76025112810ef10317f25df7100fa3eb5c44
    role: context
  - path: app/dashboard/priority.html
    sha256: 0696ae824ad8b1387da9d5b7d32569f25359e7cea54225f7a5fc6b3fd0826ff9
    role: context
  - path: app/dashboard/priority.json
    sha256: 91fc69d5e62764adb9255ed579a2490ea02a1b79bdaaaeb39ad5ef1589d04724
    role: context
  - path: app/discussions/data.js
    sha256: c68ec2f514a5c13fd22c7cffe62657d2ee7500e483f995c04e0b3bb652efcaa2
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
    sha256: 5a2c6128fa017fc2cb6f69e3894091a3e26e58d65c875572b3682c4ce8f115f0
    role: context
  - path: dashboard/index.html
    sha256: 534223d8e542d834dd1168982fc38fed2c0ee8d3d77b5d017a7ec3ad72f673b6
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
    role: target
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
  - path: history/records/unequal_protein_aggregate_inheritance/2026-10-12T144228Z-codex-c658f7.yaml
    sha256: 96826a4c43fb14daa9d14d3376e5dc79aea390a49c9622b237062b0ae623d0b8
    role: context
  - path: history/records/unequal_protein_aggregate_inheritance/2026-10-12T182646Z-codex-9c4b15.yaml
    sha256: 35b0aca1707d798efbed6c17802fc659790c3a235231ed675ab2a6ffb226ae0f
    role: context
  - path: justfile
    sha256: e6047ea612115a6a78d100b281483ba824c860c3def59bcd0d40e7fb56b3526a
    role: context
  - path: pages/browse.html
    sha256: be5147531b53037218ec53693c3a958fa1f0a96788b711255e6fc8844768c253
    role: context
  - path: pages/category/ecology.html
    sha256: 811e8b59e98880aaa779f9b4329e68dd28776a8747bbd352402ff604ffb5163a
    role: context
  - path: pages/category/environment.html
    sha256: 7d3808df64848794f2ef4e613b189765f5d5db854da977bca94ca3dbb5fa7847
    role: context
  - path: pages/category/genomics.html
    sha256: 6fcbecd55b04f5ad862cb66d3de9811cd07e6777464d58caa077ea81dabb6ac3
    role: context
  - path: pages/category/metabolism.html
    sha256: ba7f6ac80afe59756ca16a9eb2aae9723d0b0bbb6ee0b841346b522b310a8f0b
    role: context
  - path: pages/category/morphology.html
    sha256: cb56608f29a50f692355ecd778e42e033891f84172be07d3ca655d3f0bad1d5a
    role: context
  - path: pages/category/observation.html
    sha256: 224f77736d1e62f3cf5286803a54f8e2c3f8e9d8c5fa014c70036324ec1d44af
    role: context
  - path: pages/category/other.html
    sha256: 1a45151f860a8ec8d3808ce2373fcb033af0bb28f6bc22d2d7f022731f33782b
    role: context
  - path: pages/category/physiology.html
    sha256: 43582fe8f284071b8bb2021d8b035539f1173bcbb5d1568bd17df109dbfa311d
    role: context
  - path: pages/category/quantitative_property.html
    sha256: dc55daafdd06d8be0ae2d6ebfc2a6202c8fdf5c27002d3936440002a3fbfe79e
    role: context
  - path: pages/category/upper.html
    sha256: 877625cefb7ee13bcb546326309ab68f275278019acc949fc6a45fcfd353cf1a
    role: context
  - path: pages/graph.html
    sha256: ead034a0dd94ff042d586f9c467d98515fb62ad2dce9870f1d4ee28e73853813
    role: context
  - path: pages/index.html
    sha256: 52d8dc1e3861baf97a4fb836de6f120b3b8e0be6b314adaabb318ae81bd3cbd0
    role: context
  - path: pages/traits/ecology/animal_pathogen.html
    sha256: 989591acb84f5c7179a398b6fb304772a07a7faf1e4683bba8143538aa5bcc8c
    role: context
  - path: pages/traits/ecology/bacterial_cannibalism.html
    sha256: 36924dd0d13443f9635a5c7bc49629b78cb35011130be879e0fd8aed285dd173
    role: context
  - path: pages/traits/ecology/bacterial_mycophagy.html
    sha256: c76a07258f195780394db8da419bcdeadf6dd18d7ee973570155b139e76de018
    role: context
  - path: pages/traits/ecology/biofilm_formation.html
    sha256: 8b2dfe0ff684b7531788163c7eeaddf464397f03ea242b055be20eaa8980a2d2
    role: context
  - path: pages/traits/ecology/biosafety_level.html
    sha256: 68cf4825a2913fe8e300550e7751ede4a831b23cdf854af8e78807630c7c5fbc
    role: context
  - path: pages/traits/ecology/biosafety_level_1.html
    sha256: ce48a8a25c7eb711c3020fd928e501b6a7bd9334e378a131eefcfdc3b910d0f0
    role: context
  - path: pages/traits/ecology/biosafety_level_2.html
    sha256: 6e389bc4a5a7597da0135eec07e239a9feea7895bd7e4bce01116dcfba7fe6fb
    role: context
  - path: pages/traits/ecology/biosafety_level_3.html
    sha256: b2458dde42311f42dbfd9ca9bface0026af8f2bdab92f6091c013e8f7fc51906
    role: context
  - path: pages/traits/ecology/biosafety_level_4.html
    sha256: 5760e50cd3a8b7b8683a84f8bfd10d7e5ffd799b36dcb777cc68f3c5f7017add
    role: context
  - path: pages/traits/ecology/biosafety_level_5.html
    sha256: 17cc385d2154bb2ef003f95cf9a6403cfaf924f550dcfec5a29222d0133b1a2b
    role: context
  - path: pages/traits/ecology/collective_bacterial_predation.html
    sha256: f7daa6df7badf33d827bc1bc0fc17c65d9b9d712466180d730a150808d52c7fc
    role: context
  - path: pages/traits/ecology/commensalism.html
    sha256: c03aea32a5f44f4c2b109a1b448cb98d30536936d3bf43d77e42115d4ff15ce2
    role: context
  - path: pages/traits/ecology/cytoplasmic_bacterial_predation.html
    sha256: 850763b21463626cbf67536fe92af618e9b4337d688ad047d0f4f08079e804fe
    role: context
  - path: pages/traits/ecology/endophytic.html
    sha256: c66ba6a4ce5d484c8f625f17a64b9118309d8840466996d11742cf2fac8be8d3
    role: context
  - path: pages/traits/ecology/endosymbiosis.html
    sha256: 2923f3e9098675d4519efe5b309e7029ea599a7fd7cbbc38a2cfe9b52d61d204
    role: context
  - path: pages/traits/ecology/epibiotic_bacterial_predation.html
    sha256: c63740531271fe9a2594c2157f1203170f9790f9eba43b1f282de046b78a3505
    role: context
  - path: pages/traits/ecology/epiphytic.html
    sha256: fbf92247b19b7d7b2eb7897d7ff4dfca7ff5b2db5e916fb705515c401258581d
    role: context
  - path: pages/traits/ecology/free_living.html
    sha256: f4843b62318c62841156a280a9bbe67e2ae013555f8d1346384a34c05b16f778
    role: context
  - path: pages/traits/ecology/gut_associated.html
    sha256: 0df8fbb0ace96ad1bdb38b822c30baa73b233a6ba98ed1ecd95fc8472df37e16
    role: context
  - path: pages/traits/ecology/habitat_association.html
    sha256: f0fc31bdb1318a652bfda2242716e905d08c56bd7b8afc99ad59ee9f772b306f
    role: context
  - path: pages/traits/ecology/host_associated.html
    sha256: 15f2da198f10a45c7a3f71a50a7265fd05ab6aa8de39bf4e9fe801814ab014ca
    role: context
  - path: pages/traits/ecology/human_pathogen.html
    sha256: e75dbef09723e8a94fb7e7eda9fd05024a75b6a4d207ecdcc9c900601b17627a
    role: context
  - path: pages/traits/ecology/ixotrophy.html
    sha256: a53781869acb3e798eb5588c44546e4fd2c1c119b5fb3c4479bbdcd92d56583e
    role: context
  - path: pages/traits/ecology/mutualism.html
    sha256: 32914c030156c4b31f5524bffbac2a77493bbd154b55c6193a35991c25a45668
    role: context
  - path: pages/traits/ecology/nitrogen_fixing_symbiosis.html
    sha256: de6dcb04bab85978c24f6d568e084bf5c88c927163d307d39096a51335e71b7a
    role: context
  - path: pages/traits/ecology/opportunistic_pathogen.html
    sha256: 8d0f72b18daf27d4f487193742363110220c54107b148f8801361b80fe72c777
    role: context
  - path: pages/traits/ecology/parasitism.html
    sha256: 048a8c5dc7a4476548205fd7ea73a54e12af23117548e4eaca3ba841509f0615
    role: context
  - path: pages/traits/ecology/pathogenic_to_host.html
    sha256: 91c3c06bc84dc1b1e8c1a5fa054879be9241e65a7c8fdeee5663fa8cdf7c0692
    role: context
  - path: pages/traits/ecology/periplasmic_bacterial_predation.html
    sha256: 9a7eaf80f7aa0bae0e1d64af9c8f7af33b6bbf01041bb9b2d37cd37ef8039267
    role: context
  - path: pages/traits/ecology/plant_pathogen.html
    sha256: 0f4b397879fac2bdab9c2bf593fadfbb477bc5a8e939d2bfc6386c61eb93ba0d
    role: context
  - path: pages/traits/ecology/predatory_bacterium.html
    sha256: 27bf90f92e01a5aa7bdd1cb6d121d63c1ce71024638654cc6938d8337f30ccec
    role: context
  - path: pages/traits/ecology/rhizosphere_association.html
    sha256: 6eb28bf436665c7c86b93f93a5ffcc4923c10ec360047c3fcfd30180382b1ebe
    role: context
  - path: pages/traits/ecology/saprotrophy.html
    sha256: 1a9e0c5b3b178f04b564d5dd00e64d3107e93cfcf9e2eecfbef6a8370afc63e1
    role: context
  - path: pages/traits/ecology/soil_dwelling.html
    sha256: 58d07b5cd91f2a4d1cb874c4d6d5036e8504ba08a22d42ce3f4ee7b5e6262fed
    role: context
  - path: pages/traits/ecology/symbiosis.html
    sha256: 2c991014f277e6ba7ab39665d900d0383570c3b0c038d40796d0b26ca651e583
    role: context
  - path: pages/traits/environment/acidophilic.html
    sha256: ee7da595f206246b1a8b327da108a025f6277b31bbcf28553bf0ad64afceba5f
    role: context
  - path: pages/traits/environment/acidotolerant.html
    sha256: f1c3b37d1950a2bb56a32e3ddac3da8fc306762fed8b7ac697c26f67e56dff81
    role: context
  - path: pages/traits/environment/aerobic.html
    sha256: 42b9490fc6a808589e6e0e3c4175850fbbe5c1c924c294e58b8178b6f7f3761c
    role: context
  - path: pages/traits/environment/aerotolerant.html
    sha256: 4fad8d26e1309e5cdd6263140acd89267c25cbd0bf9a1eebddd41243e735bea0
    role: context
  - path: pages/traits/environment/alkalotolerant.html
    sha256: 0d1b8815bb295c72afd150d666025f892d4d65574990af90a7a9c3aa556ff1f1
    role: context
  - path: pages/traits/environment/alkaphilic.html
    sha256: cb6907ca34d3573b8428701f579de664cca2a2cc8665c98aa2c720053cdd6d16
    role: context
  - path: pages/traits/environment/anaerobic.html
    sha256: 5445e21735520dbd461294b819e473cd3b8bc997622df838104a107149d87e47
    role: context
  - path: pages/traits/environment/arsenic_tolerant.html
    sha256: 1a4ece74f1cbe611b305ace6cad08b53763a7da864dd3c2d177b8a70bebd0f82
    role: context
  - path: pages/traits/environment/cadmium_tolerant.html
    sha256: efd75df10350c2365de8bb0f38ba3ee603c97166194013904fb20aa1c8625036
    role: context
  - path: pages/traits/environment/capnophilic.html
    sha256: 0867cdb8982d0052f9d915d810dc3dd07198586f616798eabfa42baaa515ab37
    role: context
  - path: pages/traits/environment/cobalt_tolerant.html
    sha256: 824c38974f6ac6ffb3fe4845255c88af4f55483da9cb3bf963068f7437a0935e
    role: context
  - path: pages/traits/environment/copper_tolerant.html
    sha256: 94404afc19d522502f54ac72c02f612cb25290f00ad64a879b47e10005239bb3
    role: context
  - path: pages/traits/environment/delta_phenotype_with_numerical_limits.html
    sha256: 81192ee09aa9e220c94010403ecd0c68d9ff3fe8d3f490837dced06dac0a185c
    role: context
  - path: pages/traits/environment/desiccation_tolerant.html
    sha256: 875a52373a2d0c32185d92c8df9f8d1105db3ef5d4b8a0f4f8dbfdd8ed7bd881
    role: context
  - path: pages/traits/environment/euryhaline.html
    sha256: 543d72e2da40927861809b809ac56672b7dab8799f6b809e3f3825f88111c7b8
    role: context
  - path: pages/traits/environment/extreme_hyperthermophilic.html
    sha256: 2daba14844b4ae28cdcfcf3a34d352079d841e01cdd4b796461058e1c4122f6f
    role: context
  - path: pages/traits/environment/extremely_halophilic.html
    sha256: 803acd0dc6b5b67aee0f36e62a00c08d5d8ba3f9782c70f7218bc8ed3055bd0e
    role: context
  - path: pages/traits/environment/facultative_oxygen_preference.html
    sha256: 8884c397fd26795aaae3c7bc058eb13d535956b2d459fc9b39d656e564899eab
    role: context
  - path: pages/traits/environment/facultative_psychrophilic.html
    sha256: e161f551d45fdc722ead1793a6f6ebfa21ab31346d8ef0c2292a080d107a43a8
    role: context
  - path: pages/traits/environment/facultatively_acidophilic.html
    sha256: a13bbbde5cf23ff8b3a8e599b34228880abb92bac3a5dff82dead7b86e832113
    role: context
  - path: pages/traits/environment/facultatively_aerobic.html
    sha256: f43417503d8d3919c431b3c4e4b0ff6a5ea7a2cfc5e8a37873ec28a988b5cfb8
    role: context
  - path: pages/traits/environment/facultatively_alkaphilic.html
    sha256: 3d4300f708af7a327db929b4e9a6a8d7eca58a00a4c323b4db3efd8dcad3cd5f
    role: context
  - path: pages/traits/environment/facultatively_anaerobic.html
    sha256: fe708cdaf55248f08ab364d356cb97e867f08f0c9417e007c3d29876e4d28762
    role: context
  - path: pages/traits/environment/growth_range_phenotype_with_numerical_limits.html
    sha256: acb13236e655b0b8426c44774bd03a403e04b486ecbbdece71eae037182ffb85
    role: context
  - path: pages/traits/environment/haloalkaliphilic.html
    sha256: c6a6e1a0012163e57aa5bad232ebf6e78a6a9336fe486d3cb9a8c2354aef53c9
    role: context
  - path: pages/traits/environment/halophilic.html
    sha256: cf7d46d9fc53c20f3a8aac0fd3fab9577137e49fe5f3a0c8cb7922325cf528aa
    role: context
  - path: pages/traits/environment/halophily_preference.html
    sha256: a6ad16c9a738b416a61bb8a6fce3bc2dabc1f9a32cb67f1295e6c1c6fdabdca1
    role: context
  - path: pages/traits/environment/halotolerant.html
    sha256: 518a88f00fa94e162ad40588bdb8319e3088f86b28ead702200ee1bed1951bd9
    role: context
  - path: pages/traits/environment/hyperthermophilic.html
    sha256: 3b0320f7c01d15d85ab89589be81b4b9c2446d842589638594ec37060041a607
    role: context
  - path: pages/traits/environment/ionizing_radiation_tolerant.html
    sha256: 585286b8bf8b52c2233ed32cee7ad85a65df13b52839f8f6b1f91f17bfc30e21
    role: context
  - path: pages/traits/environment/mercury_tolerant.html
    sha256: a5a54d5de99f7905015306dc5be5b4da2da2fdd0f53472707f2aae7ffe789296
    role: context
  - path: pages/traits/environment/mesophilic.html
    sha256: a4d136e92ebd67fd2b58c9d787a498b8444f26c88921ae95d8e22be57f5f8365
    role: context
  - path: pages/traits/environment/metal_tolerant.html
    sha256: 95a4a84f8fa7f83386d6cad701ae65a6e6b37caef55937356106ef51231646ae
    role: context
  - path: pages/traits/environment/microaerophilic.html
    sha256: 610aec3fdd3b58224ded1af05a201cdf11f20f181aa0f1f75056ed4d21a56a09
    role: context
  - path: pages/traits/environment/microaerotolerant.html
    sha256: 2461158da2d9230f02ebdb56a8c3883b104ebd5ae0925f77d7e2edd55fc37bfe
    role: context
  - path: pages/traits/environment/moderately_halophilic.html
    sha256: f995db48e2568695d75486ba2f28f3ae8cd4db71666ac886ffd1766595336fe4
    role: context
  - path: pages/traits/environment/nacl_delta.html
    sha256: 257b0f98adfb190411ae8036073e25672871e634995ef21b43cb3473d2bb2af2
    role: context
  - path: pages/traits/environment/nacl_delta_high.html
    sha256: b6961a63740b5afadf1c49a51d581a3ac46efdfcd9a1b2e71644ecb6d3c4ed57
    role: context
  - path: pages/traits/environment/nacl_delta_low.html
    sha256: ef7291e3d2edfb522a587e0b4c8de859ecdb5efaac8979e8c1077092ee795eb8
    role: context
  - path: pages/traits/environment/nacl_delta_mid1.html
    sha256: c59c388632d4543fa8b2d6f6576dcdebbfdc8f9a2c81c180578c9685863acaec
    role: context
  - path: pages/traits/environment/nacl_delta_mid2.html
    sha256: 99b43bf8b7657bd7468a4ac71a43ef0f3a238e110f7fa3d56048738e49da7d46
    role: context
  - path: pages/traits/environment/nacl_optimum.html
    sha256: e4200041e5e09ee224bbdb78f56a3d7fd8cbc0f2abaece18fc1e5f964ca08627
    role: context
  - path: pages/traits/environment/nacl_optimum_high.html
    sha256: 59e12dfcd0ad311fbe5090501954e7159f106b6757fda3df8e89ce8b0d432bc8
    role: context
  - path: pages/traits/environment/nacl_optimum_low.html
    sha256: 28ff04f27cc18a567183cf8c38794338b460fb0aa70a662d4e8524cdb3debefe
    role: context
  - path: pages/traits/environment/nacl_optimum_mid1.html
    sha256: 37676d2999ed3a36bd07aa03d0bedf8bbbae97f257f2157e0587397f4f187161
    role: context
  - path: pages/traits/environment/nacl_optimum_mid2.html
    sha256: 30017ea08a0b815a5a2423be2fab472f653ae1db498a541650bfd704150b542d
    role: context
  - path: pages/traits/environment/nacl_range.html
    sha256: d173666885e00a6ad9e9ff72970508f6a8718af8c8f14dbe1ee6575926b2e4e2
    role: context
  - path: pages/traits/environment/nacl_range_high.html
    sha256: db3d97b7716dffbd8ac45434e060872da52e34bbbd59d9a3462aca971ae17e19
    role: context
  - path: pages/traits/environment/nacl_range_low.html
    sha256: 62587d5c471bf3e20cfb92da9a61dbaa045ecc5e4a100230a76a749cbd56460f
    role: context
  - path: pages/traits/environment/nacl_range_mid1.html
    sha256: 79cb177c1658d0e0f6975a75a1ebcbc1f6c2e4846557523bbfeffb3670c9d4a8
    role: context
  - path: pages/traits/environment/nacl_range_mid2.html
    sha256: 7c28671455c97b9d15408cc10850eee55e1fc0d87610e3a0185823e488320f99
    role: context
  - path: pages/traits/environment/neutrophilic.html
    sha256: 2199ee16bb245435389d8f44f5b98e6473a71da9e55848284058f560be532db7
    role: context
  - path: pages/traits/environment/non_halophilic.html
    sha256: 8aec5aca5cdbf3ab1c1b2ee4d0a77247f55beca3c8785171bf6e811aefc879cf
    role: context
  - path: pages/traits/environment/obligately_acidophilic.html
    sha256: d8e6b697263d17cfb5536b3058693a20e519753e5700e4d96004ba61292ec880
    role: context
  - path: pages/traits/environment/obligately_aerobic.html
    sha256: ea250eb64ed1791c747cd79d6e8cd2282a954df50e6b0b002e5ef9cbd2ccb18a
    role: context
  - path: pages/traits/environment/obligately_alkaphilic.html
    sha256: fe9a9b82d4b0cd6fc458bc2036f0568c629b1fd3bc97d95a3387bdfbee555e04
    role: context
  - path: pages/traits/environment/obligately_anaerobic.html
    sha256: 2bedc5229a72f3361fcd053da2e3d8a3d29088bcf98f65bf99fbda655966d145
    role: context
  - path: pages/traits/environment/obligately_piezophilic.html
    sha256: 1ad910359354298970782454300923e826162e3a3ec64a3cef075821e5171680
    role: context
  - path: pages/traits/environment/optimum_phenotype_with_numerical_limits.html
    sha256: e68a39d5ec29950676a1645fea95f9d5cdd2cd1f6b3487fea1d5e841f4166d43
    role: context
  - path: pages/traits/environment/oxygen_preference.html
    sha256: 57ab3d072c3cc68ef968d31fbde7f4feb14889296aa890ec33e6ed721f49b8bc
    role: context
  - path: pages/traits/environment/ph_delta.html
    sha256: 14bfdba80d85c216536004b9c0a1be1ecac061629b9503616413c1020b919d70
    role: context
  - path: pages/traits/environment/ph_delta_high.html
    sha256: fe05242884811f711e24bafca8b7c31b865e82b3b2a33229b812cb9d3b68e7fb
    role: context
  - path: pages/traits/environment/ph_delta_low.html
    sha256: 8a3710e7027cf6cfe9af9b3e7583e09a9d591fb7c46877cf82ec91a17d43c5d7
    role: context
  - path: pages/traits/environment/ph_delta_mid1.html
    sha256: a833988a7ef83989112c0d99a5bf50ca29d9fa157297ded3c01bab408bc46cc0
    role: context
  - path: pages/traits/environment/ph_delta_mid2.html
    sha256: 130bc02d77b29ea02371c7d9be0d7d32eac1f59c869dd19ff09b3d854486bf32
    role: context
  - path: pages/traits/environment/ph_delta_mid3.html
    sha256: 097450e38d94e2471098ce6e2540a7667fe655ae03b22df347ec0c92e76b7203
    role: context
  - path: pages/traits/environment/ph_delta_very_low.html
    sha256: d3beb82c36e6ff48cd4694377a99b293c8721729ce94cfc5a35ae344ef2d5baa
    role: context
  - path: pages/traits/environment/ph_growth_preference.html
    sha256: 4a3c2b2777a1acd5a5dc12c06f0767cc10ec020dfe035d3f604830380796f8e6
    role: context
  - path: pages/traits/environment/ph_optimum.html
    sha256: ed290e7fdeb22b1ee8792b039f7e316700bfd84050f2604ede8117a8395432eb
    role: context
  - path: pages/traits/environment/ph_optimum_high.html
    sha256: 8f26ab51615a1a5a623f778e31d49fe530ea9f674fd322c03110d3b57ddde1ad
    role: context
  - path: pages/traits/environment/ph_optimum_low.html
    sha256: fa5bad2522953a9047ee02754a8fbe9040ef586d911e6e3f41f6d50b2cb60b60
    role: context
  - path: pages/traits/environment/ph_optimum_mid1.html
    sha256: 4a5b4e9f7729500df75720d81ad714e189eec3fec750b5b03e8af962b2e75369
    role: context
  - path: pages/traits/environment/ph_optimum_mid2.html
    sha256: dabd600fe62fb74d9fb6f13f3689fe9de2a9b8ed30e4855daa2c01219705d88e
    role: context
  - path: pages/traits/environment/ph_phenotype_with_numerical_limits.html
    sha256: 9dcd1df86a92f8d62556c9f9888f42d549ab533be05693ba73da3b7f85be5284
    role: context
  - path: pages/traits/environment/ph_range.html
    sha256: 96895cef14ced75bb72a0d93f2434a39811ee92234e2373f741fdfd0e034382c
    role: context
  - path: pages/traits/environment/ph_range_high.html
    sha256: 6b888a80540fd179e5fafe26f209b4888a8c727eca30ff34f7a7a9e5da6765d8
    role: context
  - path: pages/traits/environment/ph_range_low.html
    sha256: 636b7dcc09061fc3f45ee3d1a2835584cecfef985e99dbb286d788bf5c9fb049
    role: context
  - path: pages/traits/environment/ph_range_mid1.html
    sha256: 56ec35ea32d6a884cc73216bc0013979895e57e7ab145b77995eb892227904bf
    role: context
  - path: pages/traits/environment/ph_range_mid2.html
    sha256: f724a6670b1323aee7d72f8f45b14519fe7f06846dceabe84b135b5d80ad1aa2
    role: context
  - path: pages/traits/environment/ph_range_mid3.html
    sha256: a2404389dd5a6bb985f03558214d50e05bd7262eb10a229c09eccfa64ae63226
    role: context
  - path: pages/traits/environment/ph_range_very_low.html
    sha256: ddbc33101e909518ef6ca78bf9499372e58d3cd97dc466987e5f9af2b124ec8a
    role: context
  - path: pages/traits/environment/piezophilic.html
    sha256: da5171d42507db7f70c3a20f70207ca28f2630ac919ed2ea38204b841ec6d36a
    role: context
  - path: pages/traits/environment/piezotolerant.html
    sha256: 92833250577a8892f3ffa68d1ec588c65d070e83a3bec768a4761428249bd740
    role: context
  - path: pages/traits/environment/pressure_delta.html
    sha256: 10c9ac4d6f52783434c38abe79b7ec657da057af60ba83704f9ba38a04ee9753
    role: context
  - path: pages/traits/environment/pressure_optimum.html
    sha256: 5b8c6c6bdcd76715531f08f1f3245ea7d0e791ff5b670148c3e7b43422c999fc
    role: context
  - path: pages/traits/environment/pressure_range.html
    sha256: 6e80833787c3c8c02789a43f2390d99a01d5ad3b8d3ad1c6fe8d2b1e1bb88dbf
    role: context
  - path: pages/traits/environment/psychrophilic.html
    sha256: d007e1adb54c191cef972279bd714c847cde3e5fdec29282c3a6ddbf2fe37bf5
    role: context
  - path: pages/traits/environment/psychrotolerant.html
    sha256: a3d6a950c19ec490c1bf60dfe353ee78328769c6535749b3053f7f8e7e03e18f
    role: context
  - path: pages/traits/environment/radiotolerant.html
    sha256: 5fb3fc820642464c59e0eb5d8511875022d18a710c65014b9183e48b7a498406
    role: context
  - path: pages/traits/environment/salinity_phenotype_with_numerical_limits.html
    sha256: 4220f461d7dc8cb21a2ea053b33ffecf05bfa5aeaf4c5f9b67fb3d3073a92974
    role: context
  - path: pages/traits/environment/slightly_halophilic.html
    sha256: ed22db4e5a70b2372ecdf26693db16cb82ad7fdd06f2ead7f6a7969a80cea03d
    role: context
  - path: pages/traits/environment/stenohaline.html
    sha256: fc209491d1fb806cc3f4d0cd3951e4dc7e34b94477a2ae6da9cd7c77987e3fd4
    role: context
  - path: pages/traits/environment/strictly_anaerobic.html
    sha256: 320059c395dde63b2c5d082da8394adfad382067c6b36f1ab638058afc44d229
    role: context
  - path: pages/traits/environment/temperature_delta.html
    sha256: 2da122d5bb35616b256d3e8e405d1c1519550c657102f7c94aceca3e1e36647b
    role: context
  - path: pages/traits/environment/temperature_delta_high.html
    sha256: 1e492b263e9dc0bc620bb52537002399e01827389ba622437925ddbb371fbaef
    role: context
  - path: pages/traits/environment/temperature_delta_low.html
    sha256: c3368390d5060f258cc6a73e571f2b4ca425b26ec3eb05f473c9d6fa97a4caf1
    role: context
  - path: pages/traits/environment/temperature_delta_mid1.html
    sha256: 98a3f0c9709f4954546132e36ba183f3745d6569cec8184f9bf638ebf3e6b770
    role: context
  - path: pages/traits/environment/temperature_delta_mid2.html
    sha256: e471e9a309b9eb1975915db7c2acff559a5e40046a3a043273de9c36e214eafa
    role: context
  - path: pages/traits/environment/temperature_delta_very_low.html
    sha256: 4ae15386752afc25cf907fc6cc55c714b9f498f3b990a1400a2dd1e0c488f4c2
    role: context
  - path: pages/traits/environment/temperature_optimum.html
    sha256: a4ef2a234bcd6b095df4a45ff18075f4fdb8c99c27c875c470bd5c9a4ec2a87f
    role: context
  - path: pages/traits/environment/temperature_optimum_high.html
    sha256: c6138de5db0b5cfcb125f4ab0af775707bb9a7cef7d0850df434d0b781700c78
    role: context
  - path: pages/traits/environment/temperature_optimum_low.html
    sha256: f6418327022ba8c79e18982d627e16437a8e2e22b74517ae0807a2e992280505
    role: context
  - path: pages/traits/environment/temperature_optimum_mid1.html
    sha256: ac8e4308f635023b390714300e3ecdbb7e1648792e477949fbb5cfe359e8bf7f
    role: context
  - path: pages/traits/environment/temperature_optimum_mid2.html
    sha256: d528e5140e225b6cb56f9a03c5d8ccc3e660d1474cb86ddfbe76e076930895a4
    role: context
  - path: pages/traits/environment/temperature_optimum_mid3.html
    sha256: eb54c6ffb9297caac7eb19294d6a6836f638c9c76eaa61809b10aa734c4fefb2
    role: context
  - path: pages/traits/environment/temperature_optimum_mid4.html
    sha256: 22519dd1743c7d880b6f07cf4a419e969b6a931eee72361d8ac760db74bbef0c
    role: context
  - path: pages/traits/environment/temperature_optimum_very_low.html
    sha256: 003993bccf906bd43a1210432e385c32ddf59cabe1c4bce0689dcb0a059e9c9b
    role: context
  - path: pages/traits/environment/temperature_phenotype_with_numerical_limits.html
    sha256: 1550714091806861a743e4ade836f54aca7ccbc36cde02e7f3b21db10d7ee742
    role: context
  - path: pages/traits/environment/temperature_preference.html
    sha256: 5811a6129dcca077b509a97f6167d1f25046a68ce0005afe02cb4d4aba33dbd6
    role: context
  - path: pages/traits/environment/temperature_range.html
    sha256: fca954f6dbaeed509be0bfb191eeae6d1446a8ad0310d46b4bc8c4cda852f364
    role: context
  - path: pages/traits/environment/temperature_range_high.html
    sha256: 4cbf86bd468323af7196e75e1097178c5ca6c41a43294d1f3924f1a9bff36797
    role: context
  - path: pages/traits/environment/temperature_range_low.html
    sha256: 9e7559c47c6a05f496d2434751880a8b3dbe224ff0ae7d178a492bb2aaa7478f
    role: context
  - path: pages/traits/environment/temperature_range_mid1.html
    sha256: f1ebd5c57878380f4a268bbd7d7586b0b48cbf08a24e799a2c1672d224e75d99
    role: context
  - path: pages/traits/environment/temperature_range_mid2.html
    sha256: d3ead961dbb6909a67941330f31d291083db4d5a091d3197c8adcb3568e2044c
    role: context
  - path: pages/traits/environment/temperature_range_mid3.html
    sha256: 63b51154a48416970a78f82ed89aa2db309b6f77c6f2b57f126056418b7ba7c3
    role: context
  - path: pages/traits/environment/temperature_range_mid4.html
    sha256: fa147e59c88d85aee723de5aba78ddd32da78dbdc84a042f20b467bdb5ad505f
    role: context
  - path: pages/traits/environment/temperature_range_very_low.html
    sha256: 3b773e7dd5826a2e2139cbcffba72071dd1bc918d4bb381cffad212965836494
    role: context
  - path: pages/traits/environment/thermophilic.html
    sha256: 6d9d4f874c631e7fc732983d8067b137ee827a69d02a2798fa728b8ce8c46340
    role: context
  - path: pages/traits/environment/thermotolerant.html
    sha256: 4febf8f74574c103be5bef75971569b2c844086386f3707e9a7bf225e53b0600
    role: context
  - path: pages/traits/environment/uv_radiation_tolerant.html
    sha256: 88a54e342f53c602c7a7e60650ca703aca837fc678d33995b5a67a7c6a34c7c2
    role: context
  - path: pages/traits/environment/xerophilic.html
    sha256: 15d3e9fa5cd96153e77f06b1d695c283300cd153728b1ea81e972cd269a9f375
    role: context
  - path: pages/traits/environment/zinc_tolerant.html
    sha256: b401a6032a1098453d58b711d88becb5ea39b8f1f92d6c9958088d84c65fa2eb
    role: context
  - path: pages/traits/genomics/abi2_system.html
    sha256: 3a6368e8eaf4fd31a45cf2910e6aa8b7bba54ee3f1faaad05d1c3bc7a8ccaf7a
    role: context
  - path: pages/traits/genomics/abia_system.html
    sha256: eab0fa1a5e48b04b8349ddea4b1205aaf97767cb17253ba146a93be61036e0c1
    role: context
  - path: pages/traits/genomics/abialpha_system.html
    sha256: d4ee10b775ee6abfbda60fae4deb31b9d0c56b2971681db6a8e2ae3273654def
    role: context
  - path: pages/traits/genomics/abib_system.html
    sha256: 745302f6b06a0718178374bb95a6dc68b1dd502f8410fafb896874a1dbdd3837
    role: context
  - path: pages/traits/genomics/abic_system.html
    sha256: 811b14b6b5964fe8237f86965bb86d35f2ceb5dd4bd42c35e977963e08400fae
    role: context
  - path: pages/traits/genomics/abid_system.html
    sha256: dfc437100c015b4b98586a48412847ff1d4d7da157e51bc6c0e374fe4042f780
    role: context
  - path: pages/traits/genomics/abie_system.html
    sha256: d6c9c2233c52b7f523ab96eb6847bb6e6f9ed05db6622d99aa18e5089f4542ec
    role: context
  - path: pages/traits/genomics/abif_system.html
    sha256: 77261e957c66a65dcc06d9cc21747ee391198948e42ccc0cca4634abf3bec1e5
    role: context
  - path: pages/traits/genomics/abig_system.html
    sha256: 5f43652f08e0cf4bcd7d2505c6429f1eb57469840daa1a6fdf0e88999705592f
    role: context
  - path: pages/traits/genomics/abih_system.html
    sha256: a58699d081ee14e7ca7996f2ba3d2b56b4b5b5e06ffa3277454fa233955686f0
    role: context
  - path: pages/traits/genomics/abii_system.html
    sha256: ba1efa086bf0f18c7f59e9a94f167e67932ff678c5f5f42ca0b500546ba2e9f7
    role: context
  - path: pages/traits/genomics/abij_system.html
    sha256: fb8a23afd92cf15bff08056574d92451f62d31c0afaaee69cab84e043d17284f
    role: context
  - path: pages/traits/genomics/abik_system.html
    sha256: 5458769a4e5f0bfde3314e55d13d9f8052762292a2650e3f963ef2b4be44375c
    role: context
  - path: pages/traits/genomics/abil_system.html
    sha256: 6023fec4b89c21850e48d9a1817e8eb46bc42d70b51c28554371fc3622490e86
    role: context
  - path: pages/traits/genomics/abin_system.html
    sha256: bd6adcaa4a14b1f29ac0e8e477b94f0cd01274d39153d7e202b78ce24b64f23b
    role: context
  - path: pages/traits/genomics/abio_system.html
    sha256: dcde752e3924f77d926316499c33d5c09411ec26ab3fa3c592c7872f8bcf019c
    role: context
  - path: pages/traits/genomics/abip2_system.html
    sha256: f69934a0e3cad1384528cac0ac944ca3b5fbd58fe43dcca6f1689fa55c2a737c
    role: context
  - path: pages/traits/genomics/abiq_system.html
    sha256: 40409f4cd7644db3daef209047e3b778030481af37e29b4ca550ede651904d73
    role: context
  - path: pages/traits/genomics/abir_system.html
    sha256: 1d73a6f902fdce4668a871aa84c2da7e275b4fbd9e56c0d2e8facb5eed6a3034
    role: context
  - path: pages/traits/genomics/abit_system.html
    sha256: 628449f9aa2dd718c66130de749d3a0910c48728ede9ce93562b282cd466e185
    role: context
  - path: pages/traits/genomics/abiu_system.html
    sha256: cbe7a53974b88f958f1d0a196bddb0e4cb39bba358328afe7cb51b5f2ee0e447
    role: context
  - path: pages/traits/genomics/abiv_system.html
    sha256: 0b2fc4340c0135b9640d9d1c9b0b7dbc2fdcea5ef714b806f8ccba657b2259a7
    role: context
  - path: pages/traits/genomics/abiz_system.html
    sha256: f4e32a631d0c701ca28ad8d90744d26cfd7c15b5cfbe1ec48c0722c88acc2cf9
    role: context
  - path: pages/traits/genomics/abortive_infection_system.html
    sha256: f37faef79fc6c798f4b66ab63284195d7a6756fbcac6d3019d3104353b6eb346
    role: context
  - path: pages/traits/genomics/aditi_system.html
    sha256: 99ab013a8591ca4a480525da64c7630943e407e3ecfaee247ab4235af0c1dd1f
    role: context
  - path: pages/traits/genomics/ambrosia_system.html
    sha256: b3724d1d59b9b022234bd5271ad6f966a0c8c52fcababde733de9e2837db54b9
    role: context
  - path: pages/traits/genomics/apsab_system.html
    sha256: 700d4fb51993e66f9662f374119e8200ba0cad54f4219bad48fc23e3283567e6
    role: context
  - path: pages/traits/genomics/aristaios_system.html
    sha256: 1fb9556b97521ef85fbee40a04be1615f0658d95e385ce05a88fd79c8e54db1c
    role: context
  - path: pages/traits/genomics/armada_system.html
    sha256: aacf1706a12dc05822b85ad2cee541e300bb5d6d5dc52733e3c75d32145ce74a
    role: context
  - path: pages/traits/genomics/audmula_system.html
    sha256: 97b18221f5f5771af59ebd167f92f05b709dc8c1dff61498a9217faf035489e0
    role: context
  - path: pages/traits/genomics/avast_system.html
    sha256: ae0cbe921714e4d21f85739f256f434286a44ea8317625b45e744cd0875adfaa
    role: context
  - path: pages/traits/genomics/avs_i_system.html
    sha256: ae4dc8be7a4e3eee929701d1d31a880747b69b67da9686c76770b2d2c140de2c
    role: context
  - path: pages/traits/genomics/avs_ii_system.html
    sha256: 6109aa76e2e1b45397dba7a2c7175b5d81dcc1355d9238f0c24234eece03a845
    role: context
  - path: pages/traits/genomics/avs_iii_system.html
    sha256: 1920190e8c08bde6a3012cd6bd207e5d7fdc3bf812eafb77ac3c42c8aac104ea
    role: context
  - path: pages/traits/genomics/avs_iv_system.html
    sha256: 62adf0b64f138f7d3d728168764065a9908fb0bb499d92cc7b324f538538f1a1
    role: context
  - path: pages/traits/genomics/avs_v_system.html
    sha256: 4a8e7c1e6f0cad48ea0993c6e40ec4b8c37c9b1b0e3b474d090f60db536e4a34
    role: context
  - path: pages/traits/genomics/azaca_system.html
    sha256: 61f413823295d49a54fb3ea7000d1e2d52f73733d8fe76539d6453556b002a56
    role: context
  - path: pages/traits/genomics/belenos_system.html
    sha256: 50b72df7886c80cec92107b36740e32b822428536ddab9f3bc35c3fd5cdb6075
    role: context
  - path: pages/traits/genomics/belisama_system.html
    sha256: f3f81db62770882ff0b8d652ae770b4a3604acce078d787b5931955a7848303a
    role: context
  - path: pages/traits/genomics/bil_system.html
    sha256: b1b9b36f6b139eec97cd14278c81a106af3fca9ea5a64b18d7473c35360f4e0a
    role: context
  - path: pages/traits/genomics/borvo_system.html
    sha256: 22ed6004203a9cf24f03dcb801f909ddf2fbd325a321e6964c23974960326b12
    role: context
  - path: pages/traits/genomics/brc113_system.html
    sha256: f08645849133c59ed641bb91b3bbb10ec6907e801219283391542c90d9977cc1
    role: context
  - path: pages/traits/genomics/brc142_system.html
    sha256: 01ac7cb19b60e230e3ee56feb9d4717a757fa72cbd7fb16f63d44f2f241afab1
    role: context
  - path: pages/traits/genomics/brc167_system.html
    sha256: 1e8fe90a7acabfb6dc5a26e4ec7838e6d99d7773f22b7dd63ea0b4b204b7bc4d
    role: context
  - path: pages/traits/genomics/brc217_system.html
    sha256: 760ecc5e880bfc7e6b466c9e7af11eb5c1633ef3fdf77c9054cdb289893f60d8
    role: context
  - path: pages/traits/genomics/brc22_system.html
    sha256: 11ea975850e63d51ba55db4e4327f44172f53313ca3292c28dfe06260cc2ac58
    role: context
  - path: pages/traits/genomics/brc233_system.html
    sha256: 33a536db70caac2205bfbc122a41389f05247c696a510bd189d3518b01ab5503
    role: context
  - path: pages/traits/genomics/brc23_system.html
    sha256: e2e40cd4ff1d8cf7421af7b56e66ba5832107a8ed27dd78c608fe55f290016c4
    role: context
  - path: pages/traits/genomics/brc24_system.html
    sha256: eb81fb56084a11f6fcf82def04600e60e88377e66ddb09c02f1f3a035a0874a9
    role: context
  - path: pages/traits/genomics/brc59_system.html
    sha256: e43145bd3f7efed4ee5e7c21d4515c56116b6af8a209955282a76528814b60fc
    role: context
  - path: pages/traits/genomics/brc76_system.html
    sha256: fc969174562de594c9082e722a5d6037a978f4cbf02073c9675a5dad96a59dcd
    role: context
  - path: pages/traits/genomics/brcwgs21_system.html
    sha256: d0b6f30050a6d60124c4e7b37f47b64cca59fd64585b1fcf5e5528d7ef32fffd
    role: context
  - path: pages/traits/genomics/brex_system.html
    sha256: 137f34feae10a09578aa5edfe9986418af1d0475b9ffbf3f0442d09179bab884
    role: context
  - path: pages/traits/genomics/brig1_system.html
    sha256: 5553579bdb01d00140b401d8b46f3ba2a120bc30f2e9f3cbb13092232ccbb4ae
    role: context
  - path: pages/traits/genomics/brigantia_system.html
    sha256: 0bbd08f77adb05c85cfbd4aeaa8c2e4e4a1a1039c30f90ff4894c96d0077c1a7
    role: context
  - path: pages/traits/genomics/bsta_system.html
    sha256: b948fc9de8ead88d388472e850d0b7910d0881c348aa59846b159f9516d714cd
    role: context
  - path: pages/traits/genomics/bunzi_system.html
    sha256: 7d50405cd2033461421bba9fea89666f4bb88b76eb2d40ba3814ed77f8795e8d
    role: context
  - path: pages/traits/genomics/butters_gp30_gp31_system.html
    sha256: 31a8038087f6a832bf5074e8a2757ba9e6e4db68cf9c527396bbca10db474512
    role: context
  - path: pages/traits/genomics/butters_gp57r_system.html
    sha256: b825213e34f22a03c9e937866e7b6096b03669b2a23fc24834e977e216152885
    role: context
  - path: pages/traits/genomics/caprel_system.html
    sha256: 72474e3cd8ce6ad592277ce069b96ade479ccd82b5236d57e9645e9629b38bfa
    role: context
  - path: pages/traits/genomics/card_nlr_endonuclease_system.html
    sha256: 29f1ffe535372ef56b322c9c6697c17cc85b69a8ac60a136b613fac485b84787
    role: context
  - path: pages/traits/genomics/card_nlr_gasdermin_system.html
    sha256: ce664d256b3bcca17eba660d94bb01ea90449a3a37e24c3b642ead6536b86303
    role: context
  - path: pages/traits/genomics/card_nlr_like_system.html
    sha256: 339642a14286258cadbafd60e920c39a7abf2fe2f7e893bccbddf489eed7c8b8
    role: context
  - path: pages/traits/genomics/card_nlr_phospho_system.html
    sha256: 4b0809518986c1cbe6b3047df2ae0f492e26d19857c2691e699d9e5db3be8b9c
    role: context
  - path: pages/traits/genomics/card_nlr_subtilase_system.html
    sha256: ca8a6e8ca860c60e397e5584ccad210f3a049932c2ba8018a409412bbb98b1cd
    role: context
  - path: pages/traits/genomics/card_nlr_system.html
    sha256: ae6c4f828b715bd1dd5097c74201f89d84dc19c4d607821c480b8d579c08419d
    role: context
  - path: pages/traits/genomics/cbass_system.html
    sha256: 58ee2d42418b42350630b420a02a2638186644e6c0a5adaf22bbf963464d06a5
    role: context
  - path: pages/traits/genomics/ceres_system.html
    sha256: 5d862ea08b5bd518918e2a31c5343c92f58ecd702f02a6cb84d7fa888d5cb14c
    role: context
  - path: pages/traits/genomics/cernunnos_system.html
    sha256: 2c27dc4442beb70b32885124910f256a5d18e3d08949907419e5bf425db7bf7a
    role: context
  - path: pages/traits/genomics/charlie_gp32_system.html
    sha256: 0044a5ce98cf8970c3baa4f99e12d3ad87e6c9f75673dfeae3255455610618ba
    role: context
  - path: pages/traits/genomics/clover_system.html
    sha256: 57f4c0d9df6d794ab5ebdf9b39985c5419fbb566f910132d274e9c578983d14d
    role: context
  - path: pages/traits/genomics/cmdtac_system.html
    sha256: 6aad032ac1b2de76f0271032fd3dd784dd16f6a629b9d11c5da9ed6a224041ac
    role: context
  - path: pages/traits/genomics/coconut_system.html
    sha256: 5994a78a64361bde6d4b6009fb9cc76fb9320af43799421fe97bef552c38bc57
    role: context
  - path: pages/traits/genomics/codon_usage_bias.html
    sha256: f6e5e4d4e02e75f94b1edb9d7deef63f57958c8e9fd00098ab53fab26981ac3e
    role: context
  - path: pages/traits/genomics/crispr_cas_system.html
    sha256: ef27baad3949f826c12c7d6cb04fb5b2e0e3fee1be2c2e7032acc291965b9ec0
    role: context
  - path: pages/traits/genomics/crouga_system.html
    sha256: aaa88cf0cafb678b61db4ef24f328089c4d2994431fb71d211f53d8ba00ab488
    role: context
  - path: pages/traits/genomics/dag_system.html
    sha256: 0fb7746cfcdea9c225dd0b097897ba9c9a7749ed5cd487474f97f41c06370b03
    role: context
  - path: pages/traits/genomics/damona_system.html
    sha256: ce2afac595a9fe828f0e4f6994436a362716d154d68119a55d9997b27ddc2d64
    role: context
  - path: pages/traits/genomics/darna_system.html
    sha256: bab7373a4a7b941fc36708b0450f3e06835ca51da039f6f4291c0a0087a23557
    role: context
  - path: pages/traits/genomics/dartg_system.html
    sha256: 6baced54dc6b661ef9955163fde0add045149914934259af61fb16d830f88c9f
    role: context
  - path: pages/traits/genomics/dazbog_system.html
    sha256: a91a5a2bfecc97772ace4d8b44469a56a3baa34e1e5e22f3bdc581f388b40b74
    role: context
  - path: pages/traits/genomics/dctpdeaminase_system.html
    sha256: 52c76645c4fad2168f00b67f4663741c1c60256ec97080a84b718b3c8612ef95
    role: context
  - path: pages/traits/genomics/ddmde_system.html
    sha256: 8a4e48564ec1bb1f0cd04f70d5bab464c049bea760bd6660bccb17636b5650cf
    role: context
  - path: pages/traits/genomics/detocs_system.html
    sha256: 15f8728a13609c22e31a0d2d34a44933dfdcf85b4e91c28d2a666b92b5d03b5a
    role: context
  - path: pages/traits/genomics/dgtpase_system.html
    sha256: d570ecbb0c14cab5f4dd3acad6517c9b451d160d223ecdd0066e448277cc4b59
    role: context
  - path: pages/traits/genomics/dionysus_system.html
    sha256: 128e2f44dbd5100725fed3123cd38d8dda625fea7d5d909f1e5072ed26cf5a3f
    role: context
  - path: pages/traits/genomics/disarm1_system.html
    sha256: 2da9814e7f2c0a4e4bf3c2d023e128a12852bfd2bce0e27304e4d8a0ab60cabd
    role: context
  - path: pages/traits/genomics/disarm2_system.html
    sha256: b38f04fea2898756e420dda80a459e05aace8885c01d9280ec468977f04bf6e9
    role: context
  - path: pages/traits/genomics/disarm_system.html
    sha256: 76b91c9295e96954eed48243707d3798685990bf2e8742bd9ae6279481f6ab51
    role: context
  - path: pages/traits/genomics/divona_system.html
    sha256: dbfddb41d4d40db141d7ce816287b09172d961c59c24bc3c4a54cf6ee8921652
    role: context
  - path: pages/traits/genomics/dnd_system.html
    sha256: 9d0c67133032c1ee622beb0b7707f13884d0059268814029a5f4dfc023ed4f9f
    role: context
  - path: pages/traits/genomics/dndcdea_pbeabcd_system.html
    sha256: 01e28c2906d1cfd87be4aeaa3638ad54138727ac7dbaa01f6fda1cb4faa9b0a8
    role: context
  - path: pages/traits/genomics/dodola_system.html
    sha256: da3fb17b0b440bc2fe414b2ab96ad1b9cd6dea45073a0639c7eb6fc948611e43
    role: context
  - path: pages/traits/genomics/dpd_system.html
    sha256: 2dadad1005b8bc52edc0462bd5354e8a0bc1df4cb1dfcf03a84d8eef98f421a9
    role: context
  - path: pages/traits/genomics/drt1_system.html
    sha256: 229a1658c516bf2e934a45db5b4883981f40cdb487847e014e97fdb3009d9ae3
    role: context
  - path: pages/traits/genomics/drt2_system.html
    sha256: e04d0fbcc9f2ef3232e9c7c9e805bf321bb1f44626ae6070960d2ac20213feca
    role: context
  - path: pages/traits/genomics/drt3_system.html
    sha256: f1052ba9c9ccf5baeecdced095af32a776dd1e37a9eed221704405844500eeb2
    role: context
  - path: pages/traits/genomics/drt4_system.html
    sha256: 8980ff2124ffce16a6f317e803ec1ad869c6f40c1af34ac69c494368a4801ebd
    role: context
  - path: pages/traits/genomics/drt5_system.html
    sha256: 239da3b45639f80b8b5dcc51991352afff0131a89ffe6eed6a1b64b913572aea
    role: context
  - path: pages/traits/genomics/drt6_system.html
    sha256: 4b43ae781efb7d238411181b2e64d55e8ae6c5be23210087f56c603806d81837
    role: context
  - path: pages/traits/genomics/drt7_system.html
    sha256: 21aff41555c303d8cb29b2ce861bce6c8a5381b785696f87a31a41dd3d69e2a9
    role: context
  - path: pages/traits/genomics/drt8_system.html
    sha256: 6d3d8cdf62642f3d775de9271fedf4a9b19e4909b6b055107dec55cd7a344c6a
    role: context
  - path: pages/traits/genomics/drt9_system.html
    sha256: eea6183a04c67e9c8af82bbb80a7d4ce412be77d5be5339804b4435b8697c8ce
    role: context
  - path: pages/traits/genomics/drt_system.html
    sha256: 1ea660a14072a9e2728c49d82ffffe63294637dc1e686d38db0e9d95172d2708
    role: context
  - path: pages/traits/genomics/druantia_iii_system.html
    sha256: 165969f725a8a57ef4aad4f7a2ed6f5dec18ab8ca0178d96771743b01648aa26
    role: context
  - path: pages/traits/genomics/druantia_system.html
    sha256: 3a51aee9d5b9f6f90afb06a16fdeefc4fb2551972320203a94fa556ed4301840
    role: context
  - path: pages/traits/genomics/druantia_type_i_system.html
    sha256: bf26072504b20f78a98d6309d6f2f37dea77386c29a9bb145ca6a86d99e7882e
    role: context
  - path: pages/traits/genomics/druantia_type_ii_system.html
    sha256: ea442444a09a17a78dd18524a0b3cb1498469865e011f6823776efbe3fcc29f2
    role: context
  - path: pages/traits/genomics/druantia_type_iv_system.html
    sha256: 52faf84c4cc995f44d49390c381dd6e24f9753053632ef4f04dd205566a2e0ac
    role: context
  - path: pages/traits/genomics/ds_10_system.html
    sha256: cdc0267867fcefef773b11357877e1954e5a7c47dd2279840f9bfcc06aa9e505
    role: context
  - path: pages/traits/genomics/ds_11_system.html
    sha256: e014e38dfe39f100f495f5da83fa8da248d9af9e9ea0321659c5ec2d7e3638d0
    role: context
  - path: pages/traits/genomics/ds_12_system.html
    sha256: 7844b742ecb32021ed12dd3b1b63eb534f76e7201334eb40e29c27fd0f99e4f5
    role: context
  - path: pages/traits/genomics/ds_13_system.html
    sha256: 26a0ae09070074d1e9d85eff07d401d5308081ecdbbe8da9bedf5fcf7921b3c4
    role: context
  - path: pages/traits/genomics/ds_14_system.html
    sha256: 7edb2acee720fc7be9dc717e6648ca9beb95261a2b4c00864e867010eba6ff4c
    role: context
  - path: pages/traits/genomics/ds_15_system.html
    sha256: 0f9bca4e1c0162ea316c387391a9ff9f7e68cbe1543cd2b6c5af5312bfa9c563
    role: context
  - path: pages/traits/genomics/ds_16_system.html
    sha256: f3f731922b0823426e02be8c5c8ff619f531e968fe0f127f6de4516544842632
    role: context
  - path: pages/traits/genomics/ds_17_system.html
    sha256: f090d4dc6562a7f1acebd430155bebd4d4cf3c86c8b2396b26d24c46beab831b
    role: context
  - path: pages/traits/genomics/ds_18_system.html
    sha256: a97812ab8d84b7f491d6318de1aaf80bf7c9707869404ba46bc27edca6db384e
    role: context
  - path: pages/traits/genomics/ds_19_system.html
    sha256: 8c6cc68cd2fe44b94389b7000cbe21eb605ae0782e4046eb42047e66a68a9298
    role: context
  - path: pages/traits/genomics/ds_1_system.html
    sha256: 959d6df09a0776f82e1d58baf20946ddd6399ff2735c8fd209377e2a34ac330b
    role: context
  - path: pages/traits/genomics/ds_20_system.html
    sha256: 4a4d796ef76c79b9bdf9e569a72130e654e94947f965f5671bd9865052764f42
    role: context
  - path: pages/traits/genomics/ds_21_system.html
    sha256: f06548e66a5ea8eb0269aeda31b345776439e3e3a03bd99a1f4ff050f1bba8b3
    role: context
  - path: pages/traits/genomics/ds_22_system.html
    sha256: eb56a8da12ffa7323a9051a53792ecd9d8aea21e81a04a6c184f77702b2d2317
    role: context
  - path: pages/traits/genomics/ds_23_system.html
    sha256: e0e445444f8aff1f166411e0b66001738704722586822b5e28bef86f4401b539
    role: context
  - path: pages/traits/genomics/ds_24_system.html
    sha256: e084748020283435399d8761ec03b2c58b3936da4c0859bd9ffec6abfdaced89
    role: context
  - path: pages/traits/genomics/ds_25_system.html
    sha256: 4fd11adabd6d609ff364043b6038d8d0a516c8ed51f6a04952f90d40a8f05470
    role: context
  - path: pages/traits/genomics/ds_26_system.html
    sha256: 3dfddf819555bb10203cb2fa0b4a5538a7c308c36ea3168d63d699b4acbccbc5
    role: context
  - path: pages/traits/genomics/ds_27_system.html
    sha256: 6349592c4ba84bb328743bad4000a8679c7e0000562a1d57d790095571a44d94
    role: context
  - path: pages/traits/genomics/ds_28_system.html
    sha256: 20d466c00e1e530789c4d6338f1bf04303c2c623f9c0312b2b4bc483da2ece4e
    role: context
  - path: pages/traits/genomics/ds_29_system.html
    sha256: 1b5f49e8b4015c790d57c57dc0e0db845123fe41791a7cf745b1970e453b0cf4
    role: context
  - path: pages/traits/genomics/ds_2_system.html
    sha256: 8b55a8cb63f5fc4f8e301839e4721d6049f354e160cd4149f9da13941239c768
    role: context
  - path: pages/traits/genomics/ds_30_system.html
    sha256: e0ed987a5d4b0dedcb0aa160cda419de9ec6dad96403a285c25b98a1c6fed8d9
    role: context
  - path: pages/traits/genomics/ds_31_system.html
    sha256: 59e6ffcf4597d1e316f32471fafc1797cf3b005e04d04f65cef69bfbc70031a6
    role: context
  - path: pages/traits/genomics/ds_32_system.html
    sha256: a4f5269bb69652143e16b67439158f5b2435e42528dd1e53422e90d82cb4a50c
    role: context
  - path: pages/traits/genomics/ds_33_system.html
    sha256: 210228d27f18b06845995603b205b7820b740d15c75fc3840db4f13ce11085dc
    role: context
  - path: pages/traits/genomics/ds_34_system.html
    sha256: cb26a246a4d2bb297f165412886eb8554ff6373a656a2e02f960c4efd0043831
    role: context
  - path: pages/traits/genomics/ds_35_system.html
    sha256: d62f3473949233eb40a209dbc45e9494be54c9c7b1dda04884505b8bd25eeee5
    role: context
  - path: pages/traits/genomics/ds_36_system.html
    sha256: 91e60b606f407676469f076567b661a4af671d6da1421fca19ed33dca8409a64
    role: context
  - path: pages/traits/genomics/ds_37_system.html
    sha256: cf616b9d4a2dd0a96af0e5549443e2fa0369c3bc5154f5766db760db3a9663f2
    role: context
  - path: pages/traits/genomics/ds_38_system.html
    sha256: 323efc3d59a22f3d5707ecbe5315684b68551ac622a58dc466df1008d8218758
    role: context
  - path: pages/traits/genomics/ds_39_system.html
    sha256: e941b54e16ecb86858ea88d83cbe2218b1018dcfaeac5c63745d7dadee0fc201
    role: context
  - path: pages/traits/genomics/ds_3_system.html
    sha256: 3cfc46af5747516db591a6db02b7b96f70cb4caaafbb3c5d13efde290612be75
    role: context
  - path: pages/traits/genomics/ds_40_system.html
    sha256: 87038a4eae5681e0654da8c991dc0b509bda7782a4cd0c63f2724946c1e96bbf
    role: context
  - path: pages/traits/genomics/ds_41_system.html
    sha256: 15dce398b1b60073203e7be4b0ce1d6eee59375b698d605bdf16654a5ec179dd
    role: context
  - path: pages/traits/genomics/ds_42_system.html
    sha256: 64224a691db03a64d3f5791ab5f0be44f9704b0924e9c7714304a777a00b4491
    role: context
  - path: pages/traits/genomics/ds_43_system.html
    sha256: 1fc7d4fd408001cd0cfc16242c7fea856e6f5dbd39d6e6ca7b59182bb9217fe4
    role: context
  - path: pages/traits/genomics/ds_44_system.html
    sha256: 4ac0c917613a9ab1dd3e7da218ba10756dd339c61de34c7ae19cd4c6d1fd172a
    role: context
  - path: pages/traits/genomics/ds_45_system.html
    sha256: 04a3808317cf1701bbdb74f9d54d55ae0dc83b01812ef7e0dd7540d5b9d1262d
    role: context
  - path: pages/traits/genomics/ds_46_system.html
    sha256: ee191e75603a6624930924813fa9ed4c5012622ddf0f575799caa603d5d43fbd
    role: context
  - path: pages/traits/genomics/ds_4_system.html
    sha256: 10bbf854f5579f18095ad973987905f31bfce4d433f5bb9f815dff211966e6b9
    role: context
  - path: pages/traits/genomics/ds_5_system.html
    sha256: c0932f964a0d2686169217224975deabe3142f0aaddb34a93401de9089f801e9
    role: context
  - path: pages/traits/genomics/ds_6_system.html
    sha256: b0476edbbeaebe90f6584707e6da15b8aaf9933c5a9c3d2d686003f463984aa9
    role: context
  - path: pages/traits/genomics/ds_7_system.html
    sha256: fde45e15a5c06b27856c5423176ec2bbeacb7aaffcbe490e0cdbaaeb5ea9abf6
    role: context
  - path: pages/traits/genomics/ds_8_system.html
    sha256: 78b3ac5a3da85a2894219d97280280c01d7f96bfab480993ccce2ddbc45126fb
    role: context
  - path: pages/traits/genomics/ds_9_system.html
    sha256: 2f7582e0b92a94f288a4780883c74dc62f437be15aa8a07c5902f9369bcdc0bf
    role: context
  - path: pages/traits/genomics/dsr_system.html
    sha256: bdbd43c23ee67305d47e1f5d52b20e16a871c284355dd76a271d4a410a9c1de8
    role: context
  - path: pages/traits/genomics/duf262_schlafen_system.html
    sha256: 0f31715efa21acf91e656c465ebe9d1d7b8d26181559cd14421cd317ba5a061e
    role: context
  - path: pages/traits/genomics/ecokmcra_system.html
    sha256: a848fdbf856e1a9fc476f4520527694cc5c634025fcdef0f0e118d10b1b40e3a
    role: context
  - path: pages/traits/genomics/eleos_system.html
    sha256: 819de223165b1c12bd7a4209321ee91365404c37e2632baec2d2b8135c255782
    role: context
  - path: pages/traits/genomics/endpacf1_system.html
    sha256: d1dbfbf79d5c42ae57cf469861b5f900e209baf143e7ff7f7cb0ca6cfcf2856b
    role: context
  - path: pages/traits/genomics/epona_system.html
    sha256: 4e6efcf17303de65f6853df13dfa3d6050f36db95556087c037a56eff4c35708
    role: context
  - path: pages/traits/genomics/erebus_system.html
    sha256: 1f7621addbdb6f9d8b60b723bc2e3b1f52f934438da4e23767cd1e9c38230876
    role: context
  - path: pages/traits/genomics/esos_system.html
    sha256: 8a548de1677dbb84a372a48e9c7cb81b64c6fd08b434d1d80f8773f19dce7afa
    role: context
  - path: pages/traits/genomics/fliodhais_system.html
    sha256: 01df2e5c5473f2971a87a7d974d8db94214fbd84f44033ec1076c2d3f5ce224f
    role: context
  - path: pages/traits/genomics/fs_giy_yig_system.html
    sha256: e7423de9f3c84de1f3e864cecf9e8c9931560629c82fcddddaafb495cb58bfe3
    role: context
  - path: pages/traits/genomics/fs_hepn_tm_system.html
    sha256: 6ffb6e475b4fe7b9521d11342034f45350a563155a6d714823dfecf56916e78c
    role: context
  - path: pages/traits/genomics/fs_hp_sdh_sah_system.html
    sha256: 682bd29838789fcb375e58fc563f4717e2e66d644125b23cbfa64155997421d0
    role: context
  - path: pages/traits/genomics/fs_hp_system.html
    sha256: ff14329b0bfac1f1b7e1302d2ed5687773c170a269ecbdac707330acb4f35fe2
    role: context
  - path: pages/traits/genomics/fs_hsdr_like_system.html
    sha256: b4daeae49ac2cc98239a7c86bda6db3e87ad7b4795d20abc957723c2a15f72d1
    role: context
  - path: pages/traits/genomics/fs_sma_system.html
    sha256: 0ece61ac5a3059ea9877192a79d7ef28771eef077ce9e7f3470d2f15eb02da34
    role: context
  - path: pages/traits/genomics/gabija_system.html
    sha256: 65eb4bd0b8fef9a3fbcb7a015098821660fed5712a369c75ba28ac5b9334a533
    role: context
  - path: pages/traits/genomics/gao_ape_system.html
    sha256: add5c11c8bd45998fb5aaedc9b090a8f6f469481e8b413b9ef5cd22bbc501a32
    role: context
  - path: pages/traits/genomics/gao_her_duf_system.html
    sha256: 75f826911345a91f9e6cd4b51a74737a46663930f386816a1c0b1ae6fcdaa005
    role: context
  - path: pages/traits/genomics/gao_her_sir_system.html
    sha256: ea82ad8c02adfd2eb0be2cd2c1e29d3f17f41a3ce17414b3dd2e5a600baca110
    role: context
  - path: pages/traits/genomics/gao_her_system.html
    sha256: 8f2dddaeef5c769a006b5c3576ce2cc3878e8b11da7d0beae00681e09f4ab991
    role: context
  - path: pages/traits/genomics/gao_hhe_system.html
    sha256: 9a8ce6978fe8cc58f81f82479af688c2ca6b5b7ac41732c686ea3aee85d38624
    role: context
  - path: pages/traits/genomics/gao_iet_system.html
    sha256: 436c0f8d8ac2aa39e81f8eb071c2a7d299f868603c28598559525107d9d9653f
    role: context
  - path: pages/traits/genomics/gao_mza_system.html
    sha256: 4f00aef9f23f5014c27a4570e17923fe585a9939a995394a00a32dad8dac5b95
    role: context
  - path: pages/traits/genomics/gao_ppl_system.html
    sha256: ad4371657a4711ad53f6774eea2e0a82f931a3a105a5b69c1c8ff3fe1bbb9ce2
    role: context
  - path: pages/traits/genomics/gao_qat_system.html
    sha256: 4fbc86e7e2de8a656ac6aef9174f5e347391395354258a10d89c996c2701526b
    role: context
  - path: pages/traits/genomics/gao_rl_system.html
    sha256: ff0d729a0b4a05498277e1039f82d6a29cd7025643abe3f57108da92ca0fd071
    role: context
  - path: pages/traits/genomics/gao_tery_system.html
    sha256: 0a0bc5120806b6a2fa995e77d2423ae0ce279fa10504fbcec2d10c0b622db2dc
    role: context
  - path: pages/traits/genomics/gao_tmn_system.html
    sha256: 2fdde83b4853d4ef346ed992db3bd1914e779ce2ca0b6a67cc48431bf93be278
    role: context
  - path: pages/traits/genomics/gao_upx_system.html
    sha256: f7da286eab8f592ae6f9ff99766921fea8c84a6f8d94af0f8b4a1f62f6077df6
    role: context
  - path: pages/traits/genomics/gaps1_system.html
    sha256: c4b8d8438609eb25b7643ecd3fea0ea549671f5c28548bd709aa3ee2b7ec5c13
    role: context
  - path: pages/traits/genomics/gaps2_system.html
    sha256: 67a1a4f816f1fb84e57631b906884ed3c365ac7ac496d66675de84a75821f70d
    role: context
  - path: pages/traits/genomics/gaps4_system.html
    sha256: db03384c90826e23ff432f5ece3e5b70657aa57e47e92eed2abbff9a589f9172
    role: context
  - path: pages/traits/genomics/gaps6_system.html
    sha256: 54eb91172cad363d8eca3fed91e3e6fe258935262415e0910f91ce3be27e16fa
    role: context
  - path: pages/traits/genomics/gasdermin_system.html
    sha256: 548000d658c3533de39c1b7b3d9a3e33bef421716fd3f298612e789b33a96b87
    role: context
  - path: pages/traits/genomics/gc_content.html
    sha256: 8fb5a197449e6c087559ed42acbc6d6f76a30ae4480cfea1409db3550b0f39c4
    role: context
  - path: pages/traits/genomics/gc_high.html
    sha256: f8cd226655cec74e7e6e5282a545a06030b3ebe47dacff342aa3c72b28995a04
    role: context
  - path: pages/traits/genomics/gc_low.html
    sha256: c20467cc0e5e88ed2ceb072028bb1589c178abd9d67722a0054d7a82bb8c67b5
    role: context
  - path: pages/traits/genomics/gc_mid1.html
    sha256: 797694d4457f7834328d9b058df1f0d505842d603e830bc33ec34ae45c2cefc7
    role: context
  - path: pages/traits/genomics/gc_mid2.html
    sha256: 996f9f5b291a5254fc4cc932276ee021b03e4fc92c6766ca7e9cc7f761c3eab5
    role: context
  - path: pages/traits/genomics/gc_skew.html
    sha256: 96e54a6efa548ed1e99f1590aa939b13d4f3a44389d4b9780460aa44a30e6aa9
    role: context
  - path: pages/traits/genomics/geb_system.html
    sha256: dd8409e0942fb2e4b02bd82a3d7d4f2ef8d8482c04741e2d9a59688d529caafa
    role: context
  - path: pages/traits/genomics/genome_size.html
    sha256: 4fe9d992b586a9c835d492e241554a90ac030c8156196efcb51f74896fd0d234
    role: context
  - path: pages/traits/genomics/genome_streamlining.html
    sha256: c7bc1a41ab249a6fd2e17676f2f1241f24d3b6b8ce93ccaff79b580b10b81995
    role: context
  - path: pages/traits/genomics/genomic_island.html
    sha256: cf7d767b7c612722d98df8c95f7620c1ab43e15dbf370dc09b0e9920c37c3793
    role: context
  - path: pages/traits/genomics/gmrsd_system.html
    sha256: b2001dca188eea2adaa7368769ac4c2c9f4c375377237c899971da7dc9f73869
    role: context
  - path: pages/traits/genomics/hachiman_system.html
    sha256: 7380e77d50e196b70fc4a0199219d8988b2cf261f5c2a7aa3d2b0f470e77ecd4
    role: context
  - path: pages/traits/genomics/hachiman_type_i_system.html
    sha256: 692c02d18f0f191ff9fe868217d096e646b031fbeff1a83d3194f7b72be2a1e4
    role: context
  - path: pages/traits/genomics/hachiman_type_ii_system.html
    sha256: 601e9707ae87de3a96082a0f30b1f6f82134404ca7407c843583b2b12a2b4252
    role: context
  - path: pages/traits/genomics/hailong_system.html
    sha256: a0abde3cda555764d24fa89b9e74d713076d330b954e612f4f30c4ce9850a1df
    role: context
  - path: pages/traits/genomics/hec_02_system.html
    sha256: a6c5e9bf999b865fb4baf92eecbefbc4542ef956ab3ff0a3afd818b6bc924fea
    role: context
  - path: pages/traits/genomics/hec_03_system.html
    sha256: c53441dd5964250845a30d93939f5f0283af464d69f9f221ee1b5120f3fbd432
    role: context
  - path: pages/traits/genomics/hec_04_system.html
    sha256: 31067863a0d6df3ec4ddeb3d3dd4792190c9f1565d737c253a59463172191aee
    role: context
  - path: pages/traits/genomics/hec_05_system.html
    sha256: 501fde46668e0ec9eb2c644a0ab1829cf2609e42692c86e77ca288243f35b49e
    role: context
  - path: pages/traits/genomics/hec_06_system.html
    sha256: 431e1a9649aed7123ff13783dce47f14666099536a390abfe4dd37f917e6528f
    role: context
  - path: pages/traits/genomics/hec_07_system.html
    sha256: 39eed35be149aa467a3c9ab373370e1b3c349873ff8e1438e0a95398cf3dd43f
    role: context
  - path: pages/traits/genomics/hec_08_system.html
    sha256: 437a5a61db1c1fd6f9e857095a2e57f24b5d33085211d99b7d20589b428b2490
    role: context
  - path: pages/traits/genomics/hesat_system.html
    sha256: df838047ff228f61c05dd6d276a75fbad03ed6de375e8540ea7dbda5fd53c8c0
    role: context
  - path: pages/traits/genomics/heterokaryosis.html
    sha256: e71236b324610df8cc7c6c7a92d41c4eeb61ce8eba5b01a3625125386c20c293
    role: context
  - path: pages/traits/genomics/hma_system.html
    sha256: cae469c1ebadf6087b0dc4df089a57328efe905051e70bca44ff886d10f842cb
    role: context
  - path: pages/traits/genomics/hna_system.html
    sha256: 2648da500a4a5bb46ecb5ec590aa6a7ee9c9262927819b55c883b3d00b000857
    role: context
  - path: pages/traits/genomics/hypnos_system.html
    sha256: ff95feefa2cbf5f89d22db2e593ec87d44ca6a270436de6abce9c43a7416b167
    role: context
  - path: pages/traits/genomics/ig_like_schlafen_system.html
    sha256: 01555c5d81fcd9b1e0ed813ec7bba7905a95ee4f78865bb882864d92e52426b4
    role: context
  - path: pages/traits/genomics/integrative_conjugative_element.html
    sha256: f1c868eb32aa1b3e538d33a017eadebd5b62190e3f076d52bf7452e4bde45d25
    role: context
  - path: pages/traits/genomics/jukab_system.html
    sha256: de350f1c6ca5cb6695901df6c5307af6f3296f1da2cb9dee95faa343b646f779
    role: context
  - path: pages/traits/genomics/kamadhenu_system.html
    sha256: e0c3ff0b4b8f0df13b63186d88615606128bb9567a033edbfdd046ac93f74cfd
    role: context
  - path: pages/traits/genomics/kiwa_system.html
    sha256: 81e91fd62f40e96b4c6af6555e682e82ed49b2bb8915436e436bc408ef97e4bf
    role: context
  - path: pages/traits/genomics/kongming_system.html
    sha256: eb1469d6cb6e1f6fcbb04eb1b26427f5b7a8cc5eabdddac0ffcad1aa2e5518e6
    role: context
  - path: pages/traits/genomics/lamassu_amidase_system.html
    sha256: 9c649aa48ff9a3b533c05ce45717ffa95f72e86e43a2cdfbc56411478179af53
    role: context
  - path: pages/traits/genomics/lamassu_cap4_nuclease_system.html
    sha256: 32073160596eb4643c2a362c773eac46a94c6a6aa1253172eeb1f99fddad136a
    role: context
  - path: pages/traits/genomics/lamassu_fmo_system.html
    sha256: 8ea38d6461b079fac685566b6e6e70093c626c8c33a5c19815dc9977bf17db2b
    role: context
  - path: pages/traits/genomics/lamassu_hnh_system.html
    sha256: 648c63bb426a3fe7164644e86216268d735df46bc5dc99f4c282ebe4583a8359
    role: context
  - path: pages/traits/genomics/lamassu_hydrolase_protease_system.html
    sha256: 1885de78100aa551df54c2f135f003ec20185df881ab28a931d3bf279faded58
    role: context
  - path: pages/traits/genomics/lamassu_hydrolase_system.html
    sha256: c40384cbf15343184a38ca8d32ada802882a79bd0a756242f10928695fe182fb
    role: context
  - path: pages/traits/genomics/lamassu_lipase_system.html
    sha256: 180c75ead589f0f0cdbb31b36761ffd92dc5e4c2ce0910b4cd07d0d3d02657da
    role: context
  - path: pages/traits/genomics/lamassu_mrr_system.html
    sha256: fb5a4af80e1ca12155d4674b65bf5b513b3c4925694eba320cea428f7927235b
    role: context
  - path: pages/traits/genomics/lamassu_pddexk_system.html
    sha256: 120f508ad0d3f140728f65a24708918753b38332160f68776adb5f11118716d0
    role: context
  - path: pages/traits/genomics/lamassu_protease_system.html
    sha256: b5ce2f1f263c2cbb53b8e4fff8855cef290260f73b62287f2958ecfc6c67ae9a
    role: context
  - path: pages/traits/genomics/lamassu_sir2_system.html
    sha256: 7275ed97655bd4df7eb8df1aa06f3e54418c45385644529dd91db4f3420aaeec
    role: context
  - path: pages/traits/genomics/lamassu_smek_system.html
    sha256: a9614796b8736fc9e55626af32fe8f877d16e4a735751d5144364a109631996c
    role: context
  - path: pages/traits/genomics/lamassu_system.html
    sha256: 1f20f64f48dad45e5b787cd3442600ba8673d021ee8e350ca105c667439c25af
    role: context
  - path: pages/traits/genomics/lamassu_type_i_system.html
    sha256: b5973990181f60dd046fd8f38bc9d1f4d5ccd9e960e9a89804334de288d2e956
    role: context
  - path: pages/traits/genomics/lamassu_type_ii_system.html
    sha256: e7b664b7be6e88e2b6a7cded8f4757c3aa72ee4f9b71d646247c00bdfb4e349e
    role: context
  - path: pages/traits/genomics/lanthivirin_system.html
    sha256: 6517184e3e3795b1efcf7557117f1c95fef6a351b6b783727b0920fb4683a7d8
    role: context
  - path: pages/traits/genomics/lit_system.html
    sha256: 55a576ed32bd8b0764de4d454424c8f2a8944e4d7f75d855664212350752714c
    role: context
  - path: pages/traits/genomics/long_lamassu_system.html
    sha256: 8fec5ff8f623e0b525f18fe14aa0e96768e4dd9560205ce6726c4082b07583ce
    role: context
  - path: pages/traits/genomics/lugos_system.html
    sha256: 38b73b48f620935c9db18fb6ebdd1bd658b9a5926af1cb79244bafa58b7f4ee5
    role: context
  - path: pages/traits/genomics/mads_system.html
    sha256: 66f06932e12ff804e90ce4889f82f0e248c2f0ad466fe5f3c508f30ce84d2882
    role: context
  - path: pages/traits/genomics/mazef_system.html
    sha256: 7a2aa6afa959f481cb2aa46d464b2733c120481cfa9d85e7732999028034046e
    role: context
  - path: pages/traits/genomics/mcrbc_system.html
    sha256: b83e66e9041ef99f3f1c71329c6622800c0ecc251d0da1ee443c6bb586314d36
    role: context
  - path: pages/traits/genomics/menshen_system.html
    sha256: eb745ea8c17356466a125fd347beaaa4f0c21d540aafbea1e8f29d82315df7a1
    role: context
  - path: pages/traits/genomics/metis_system.html
    sha256: 8fa79ce2616da7c94c3b94f63c763eb7c1914756b383073ed030ab397d52c931
    role: context
  - path: pages/traits/genomics/mksbefg_system.html
    sha256: 644473db4b56dc9db3100263361b0c5676d341c4624659f5efe93c8665f5cf2d
    role: context
  - path: pages/traits/genomics/mmb_gp29_gp30_system.html
    sha256: 620ba4ff498832b91c7a513fd0313c22fae9ea40145dd513a7764752c40d6d5b
    role: context
  - path: pages/traits/genomics/mobile_genetic_element.html
    sha256: 8a0e8d873eeb55710c5643d40781a7ff7dad732fc33b57b857538a009ab82c97
    role: context
  - path: pages/traits/genomics/mok_hok_sok_system.html
    sha256: 078b90e87bef76e51107da4b53b937d8c0555d30a16c139bda55b568c556e751
    role: context
  - path: pages/traits/genomics/mokosh_system.html
    sha256: 95378f7c96aafbf0725ffc0a83de5e04b4ddd3c83e4c2f2b50dbd6636d149d3d
    role: context
  - path: pages/traits/genomics/mqsrac_system.html
    sha256: 4b16a66ca6fd29d697e0f420c4d383cb39b1c647d10a53dc47a57bfe7fba7ee8
    role: context
  - path: pages/traits/genomics/mspji_system.html
    sha256: df2da74999da8febc0fa69451e586e999e991f59c33e175d742685bb32074b34
    role: context
  - path: pages/traits/genomics/nantosuelta_system.html
    sha256: a2c272406203a6da5b311b0df27bf00f1768ece99ca2eed85e154b3601b3ae00
    role: context
  - path: pages/traits/genomics/nemetona_system.html
    sha256: c8dfdf61b48a5da4f242f0234bbe152706e5f18dd5cc2ced7b65015d244edaf3
    role: context
  - path: pages/traits/genomics/nhi_system.html
    sha256: 835f6a4dd47b5c53733fde3b867ffe6a25f429a13dd5b34f0f96a1d21d5ec592
    role: context
  - path: pages/traits/genomics/nixi_system.html
    sha256: 90641a1801624f574c20c3dfb9889dcd3f109f0e779d3008baab95de5ce47329
    role: context
  - path: pages/traits/genomics/nlr_like_bnacht_system.html
    sha256: c4ea26675cb5e567efb0713085304547fcbe6c69884f9ef2e1403f2954bf87b9
    role: context
  - path: pages/traits/genomics/ogmios_system.html
    sha256: 729e7cdf65a5d4a6a85ac5ff6e2e3ad8c83cb1626202cb095334a43dd65cbe3a
    role: context
  - path: pages/traits/genomics/old_exonuclease_system.html
    sha256: 7ee52813b1ae3ba165765ac33467094d89fb8fcd6ea7fce825b02d58190f5023
    role: context
  - path: pages/traits/genomics/olokun_system.html
    sha256: b2371e7a2da5c8fbf1f06916a8bcb0f530e172c42c50e94f2fe7c6840871c4e5
    role: context
  - path: pages/traits/genomics/ophion_system.html
    sha256: 8b17dc7ea49fc9e4ff827d7f75f9b98e6a009609cbb03f7fc932d0aa453f8c81
    role: context
  - path: pages/traits/genomics/oshun_system.html
    sha256: 19b99882d51a8955234b1c412baab606e78a9afe16b48f8c6adf5284ffd2125c
    role: context
  - path: pages/traits/genomics/pago_system.html
    sha256: d7b706e806e59858814616a1f7e332c34377f720d7e7201750f3fe8b9433fda0
    role: context
  - path: pages/traits/genomics/panchino_gp28_system.html
    sha256: 1cb0a9d9734b428465c730d58c45b66bada48c6b2eb94c6f8ea87f51349e2d8c
    role: context
  - path: pages/traits/genomics/pangenome_openness.html
    sha256: 0d306c8a75ee7ba3577c71c0c9e226f773ffb3705969335d3b52fc6dcc404683
    role: context
  - path: pages/traits/genomics/panoptes_system.html
    sha256: dd8ee3b6dca0118a0e39a4da95c11c3e01640c7499f22e0bffc6a0d6bc035a69
    role: context
  - path: pages/traits/genomics/paris_system.html
    sha256: 950bacc83fd85e40acc86bfed0160bf23bc2efea64ec293acf9eefdd63d9c7cf
    role: context
  - path: pages/traits/genomics/pd_lambda_1_system.html
    sha256: 1f067f3ca7630413a1e0720acf69106dba73b9ab1a70ac91e052709a40b29787
    role: context
  - path: pages/traits/genomics/pd_lambda_2_system.html
    sha256: 90b611278ad2826da574b110bfe602348f6e4c84e0ad96730488151bf7808144
    role: context
  - path: pages/traits/genomics/pd_lambda_3_system.html
    sha256: e26da2b9170513b6e732a5f5d6f2eb6e90c9832112b4e74cb701851290a5db09
    role: context
  - path: pages/traits/genomics/pd_lambda_4_system.html
    sha256: 132317d7f4dc434e3400337a28e1ae2f2a5bfbe3b4293e0f0d97f637c0565a06
    role: context
  - path: pages/traits/genomics/pd_lambda_5_system.html
    sha256: 4766d8ea568db20cbee1fa90ad6612cd87dd584f18a87364b2290721d26c02ea
    role: context
  - path: pages/traits/genomics/pd_lambda_6_system.html
    sha256: 870effe45ddd73fbe57c7c3093a7f77ee54c8592ea5e5b152c23b78bc691f67b
    role: context
  - path: pages/traits/genomics/pd_t2_1_system.html
    sha256: 416b0fdb44e8260222d53f8ea6dc7af05cafdb7550ebf0e26689fa0153177590
    role: context
  - path: pages/traits/genomics/pd_t4_10_system.html
    sha256: f0592da391f5a8d8b6a06b6546743e483d27ee4e9ef4d4bedef67c72f010cdba
    role: context
  - path: pages/traits/genomics/pd_t4_1_system.html
    sha256: 9ff4a3521ce92e6057377ae8adf9e353653ce1cd8505f870f751057c6cd636ce
    role: context
  - path: pages/traits/genomics/pd_t4_2_system.html
    sha256: 0b23f4feda73573bcae67fd45d8d6e59360aaf2d341cb6a8b4cd7b7c4fd7bbc7
    role: context
  - path: pages/traits/genomics/pd_t4_3_system.html
    sha256: 2570de7c134f27d726ffa2735859b62558fdfcb08d0879eb31ef78f086b209b8
    role: context
  - path: pages/traits/genomics/pd_t4_4_system.html
    sha256: c9af7bd55ab787bc3be0af9ba734912cfa5d6ef04298b432999d6bb183465e2b
    role: context
  - path: pages/traits/genomics/pd_t4_5_system.html
    sha256: de42e5c480891b481757a334b5bcc657f7269aabfa3deb396ce12bbedda3cd4a
    role: context
  - path: pages/traits/genomics/pd_t4_6_system.html
    sha256: d0a438b5f203358518831e8a5c3e1adba873123d0ec5d1b0bfd400d4991cd8c0
    role: context
  - path: pages/traits/genomics/pd_t4_7_system.html
    sha256: d78fe7cddc8ec525504537a618bef045f2f03258a0c00fa0e30ba7c7e141aa2a
    role: context
  - path: pages/traits/genomics/pd_t4_8_system.html
    sha256: e80d09b5cad67a8312e718a43080a93fd8e9036b29943ac8feab2655b85642e5
    role: context
  - path: pages/traits/genomics/pd_t7_1_system.html
    sha256: 342cb7b275d802400ed412d332ed9ddeb562d101b8529966360e7dbf862f7bfe
    role: context
  - path: pages/traits/genomics/pd_t7_2_system.html
    sha256: 9e372e4e5a4f022810fbd1f6d3dc4f378635af331f61806b5579b722cabecb76
    role: context
  - path: pages/traits/genomics/pd_t7_3_system.html
    sha256: df04b14e9ca6446fecad0a7e6a90044641b54647b42d386db4c507dc2c6dc901
    role: context
  - path: pages/traits/genomics/pd_t7_4_system.html
    sha256: 08cb45750503345731d55a4021322a2ee547bf8f40510f7edbd2de90395c1e84
    role: context
  - path: pages/traits/genomics/pd_t7_5_system.html
    sha256: cdc181ca4a1edd4711d9a22b7b11945424014aa5b202e5e697e71230e02997db
    role: context
  - path: pages/traits/genomics/pfiat_system.html
    sha256: c335c687280266f13879730580f1b3b63fadba89a09461516bde46f2ba8afa8b
    role: context
  - path: pages/traits/genomics/phage_defense_system.html
    sha256: 322a807066b304c2631ec72575c7d0c7aeb54f5bf64778e371b6653addf11317
    role: context
  - path: pages/traits/genomics/phosphorothioate_defense_system.html
    sha256: 977512df2277c056a74cf22ee7cc2e3f6689c779edff7218396d0968a783d6ac
    role: context
  - path: pages/traits/genomics/phrann_gp29_gp30_system.html
    sha256: e83076134f9d7e539e8fdf6f786305c22b54fbb72d7e0da7080dc7a0e6c23d15
    role: context
  - path: pages/traits/genomics/pif_system.html
    sha256: 4ddb185029d991e9c9a0f886f5ed2cfde89304bc0be2fb0bc08652a5fa70249e
    role: context
  - path: pages/traits/genomics/plasmid_carriage.html
    sha256: aaebd030b9a17d0044421f6a9726dcbe22cb790b2a354d8693d5a4a8d449f540
    role: context
  - path: pages/traits/genomics/ploidy.html
    sha256: e9dc8788b2bc239b7c8caefe2332cf9266061ef1d13354c82f4d3db995d7eae8
    role: context
  - path: pages/traits/genomics/prithvi_system.html
    sha256: ac1b26fdc480b39849067ddc89b258b88a51325d01eeb3f7adc4bcfee451e471
    role: context
  - path: pages/traits/genomics/prometheus_system.html
    sha256: 898e3df3b0c6b192cc5a9def15376fc8a9bfe1103f2843af6da2f4381062f5a2
    role: context
  - path: pages/traits/genomics/prophage.html
    sha256: 5bbad1d4e4c0c95bd910944c1f06f95e1a983747f6f42413d8fadc3ae6aa57d5
    role: context
  - path: pages/traits/genomics/prrc_system.html
    sha256: c63052a1c7dcb0ac28af89c2b04cb35a877e5be292e9ebb59134c06b36a9f2a4
    role: context
  - path: pages/traits/genomics/psyrta_system.html
    sha256: bca28b3fc2d7d45800f45953d8cb074595ede7dfc9daa6eac9f317a8b57b6e37
    role: context
  - path: pages/traits/genomics/pvurts1i_system.html
    sha256: 1e4981935384ed79724dab1f8f0691f70a078565a63e7e108a972c56ec7a2920
    role: context
  - path: pages/traits/genomics/pycsar_system.html
    sha256: 2fe72c24a2420e80fbf4fd6fabebd8f01421779dc2479a1eb0f02d30ea4f01b3
    role: context
  - path: pages/traits/genomics/radar_system.html
    sha256: fdddc72ce52bcd31f8c13ac6ad50984d356e8b577307696e2ee66d77577c379d
    role: context
  - path: pages/traits/genomics/razr_system.html
    sha256: 7c64b667a0b9bb763f633894bd87130c3cc2761efa745516a7f14b6afc9030f2
    role: context
  - path: pages/traits/genomics/resolvase_duf5677_system.html
    sha256: 2a3ea562c0b78898b47483fed8eb76a88197bbd58d4864b5aafdda12ea2363c0
    role: context
  - path: pages/traits/genomics/resolvase_kap_ntpase_system.html
    sha256: 8aec343b24c6d742909e79221b6f798ea6c306a8089f55adf9df25d61ffcf699
    role: context
  - path: pages/traits/genomics/resolvase_schlafen_system.html
    sha256: 465d1e0a4a688108529aedc97fa5bc88b769d42ed9f2044186696bf57a23b5cc
    role: context
  - path: pages/traits/genomics/restriction_modification_system.html
    sha256: 86e0452aa63079f9714ad1581995c9bcb29661028bbc22b4c54341cffa079ae6
    role: context
  - path: pages/traits/genomics/retron_system.html
    sha256: 43f8710ed4a07410ff96f8bb4b0a804c19487c1f0042b6ec452ecd7d1a9c564a
    role: context
  - path: pages/traits/genomics/reve_system.html
    sha256: 44a263f708ff3c7ee9239d58c479019834e46d8137bdf1fb4420ece04034a680
    role: context
  - path: pages/traits/genomics/rexab_system.html
    sha256: fd772b9fe70e38e3d7def19ebd85fbd2dc394fac49573f8aafefd7c74b48b237
    role: context
  - path: pages/traits/genomics/rhea_system.html
    sha256: d3d2d28a7a07ab223e8595e542ab584f269e22bd73cefea7f3b3d87037e9a41e
    role: context
  - path: pages/traits/genomics/rloc_system.html
    sha256: 8da679e0d4ac4c76890a25a193e26442ab73ed5796d25bad6fae6d4f326651f1
    role: context
  - path: pages/traits/genomics/rnlab_system.html
    sha256: c0398ba03ca110c4a68c21510a69fef105d886cc39145070c6a4a9d2e503ed53
    role: context
  - path: pages/traits/genomics/rosmerta_system.html
    sha256: c75d574342b5a849e1d1b3d55f1e290de50141a610d7c02abfb53f4035c7692e
    role: context
  - path: pages/traits/genomics/rrna_operon_copy_number.html
    sha256: 303f2d986f7fe2e113d6d87376b7610cf20c2002f655a34aaa5c2aea8aafe3ed
    role: context
  - path: pages/traits/genomics/rst_2tm_1tm_tir_system.html
    sha256: 331496cc7123c019c0383aea9a02d8c9f2cb4bf6f6bc5b91fae5c2da4e8901ed
    role: context
  - path: pages/traits/genomics/rst_3hp_system.html
    sha256: 551e663a7a5f2db4854bb252b3db4b410be745903159b56b8884bb90e2a08eb9
    role: context
  - path: pages/traits/genomics/rst_duf4238_system.html
    sha256: f14c258c02d76b2cf23d56a810b3bbb199fb0474c6c5d9727cf68b6b6cc87096
    role: context
  - path: pages/traits/genomics/rst_gop_beta_cll_system.html
    sha256: efbbced70bacf394ab594ce54e3364327d8e82d31df82d460f6a2333df121902
    role: context
  - path: pages/traits/genomics/rst_helicaseduf2290_system.html
    sha256: c0cd5f147e92d7bbc16045907bf297b4761c759f8c182f27641529701d909255
    role: context
  - path: pages/traits/genomics/rst_hydrolase_3tm_system.html
    sha256: bedec4005f20ad90316fa5cdf7a05976bdb4175eb383cf18968edf8774616463
    role: context
  - path: pages/traits/genomics/rst_rt_nitrilase_tm_system.html
    sha256: 48c1b3a492ca15c17c5cc9b54c0c90c7cc9c583f9e131a29ab2edc9e40bb6532
    role: context
  - path: pages/traits/genomics/rst_tir_nlr_system.html
    sha256: 8e1278b6caf2884922de23bcb9280edf3c3c64a2cddc524680fae351f6797c39
    role: context
  - path: pages/traits/genomics/rugutis_system.html
    sha256: ecd7f8e6c81bf050300e98c57692a7f758354640c9d0e8412a7752e055b08b5b
    role: context
  - path: pages/traits/genomics/sanata_system.html
    sha256: 348176fe3b7ce98a995ff8c0635e260b9d9aad33c609c858b369616790f3ee1d
    role: context
  - path: pages/traits/genomics/scomcra_system.html
    sha256: abd965717c9204a38eaf2f2c84de96ac30dfa81bcd0d217cc980fe50d8d0ce91
    role: context
  - path: pages/traits/genomics/sdic1_system.html
    sha256: 8a2fa9d724119171b6478126bf72adfdcd2da7a98b51a2c7be353c9bf11489f4
    role: context
  - path: pages/traits/genomics/sdic3_system.html
    sha256: 34e07cce7979b002a3ccb20e58ebf34da5e6fcdc5e62c5a59301a19840089afb
    role: context
  - path: pages/traits/genomics/sdic4_system.html
    sha256: 5dbd5e1c5d73e81c6a8d12e8dfa73dd32d6876819d6c449c81eaa7e451b4849b
    role: context
  - path: pages/traits/genomics/sefir_system.html
    sha256: 75fbc83842cebbad7148668ee3955e0df9276981801659862dfb76d887707a34
    role: context
  - path: pages/traits/genomics/septu_system.html
    sha256: 99e17a28621a8606e8323324668df06bc471d038c7861d3947844325d2f57390
    role: context
  - path: pages/traits/genomics/shango_system.html
    sha256: c76a6db2c89e1d9087396e03a1721503d5516c35b0c789cad4f1160157caab6b
    role: context
  - path: pages/traits/genomics/shedu_system.html
    sha256: cd89f56d71906293483f22e5521fa55574506e78dacfd38a530eaaa93571da3e
    role: context
  - path: pages/traits/genomics/short_lamassu_system.html
    sha256: 48d883bb7d86b57964089e09bdfead2345e1698d7876e0b3bcbf5c8d3f17a546
    role: context
  - path: pages/traits/genomics/shosta_system.html
    sha256: 6ccfde19466ec56805d4befd4a3b0e309be0808e68c6a005eab44f87b4f98dd2
    role: context
  - path: pages/traits/genomics/sirona_system.html
    sha256: f1ea0012937bb1c8634222dca8334c5c0e6bf892adb38c38eeb3e818dff78a78
    role: context
  - path: pages/traits/genomics/six_a_mbl_system.html
    sha256: 7ec53f16997749b3a3a20d72100c66e66d467b318384a54622a452cba227aa06
    role: context
  - path: pages/traits/genomics/snipe_system.html
    sha256: 07b162fb90de6c3c30720b327c300b070c321f74d7d422edd47ef719a003397e
    role: context
  - path: pages/traits/genomics/sofic_system.html
    sha256: fbfb0b411e09a35f2d6b0041b6cc89fe3cee306eb2f23f8e5aec29cd62e39a71
    role: context
  - path: pages/traits/genomics/sparta_system.html
    sha256: 3e1b2a1e2ccc2afba87a0a5c5e080901034e4e5bccba0f1daa8d48fb41d1ef7d
    role: context
  - path: pages/traits/genomics/spbk_system.html
    sha256: 823218c93f83f5e224d2647ce061788e02ec7571fe5defb817fa2797188aabd5
    role: context
  - path: pages/traits/genomics/sspabcd_sspe_system.html
    sha256: 0b513395180066a02f27817c1e266728e5f5ce079325a426216844c3be527475
    role: context
  - path: pages/traits/genomics/sspabcd_sspfgh_system.html
    sha256: 4d613f0c1648a34101b188d6517b15776d8d270c38aa4d24523fce4b941dab59
    role: context
  - path: pages/traits/genomics/stk2_system.html
    sha256: 0ebac779fed79daadf5505631ffc9832f43744496b123caae6f9e84729884385
    role: context
  - path: pages/traits/genomics/sucellos_system.html
    sha256: 90965d848ebbe1d95827f3a66379f28a877944527c6249730f0679fceaf3336f
    role: context
  - path: pages/traits/genomics/tab_system.html
    sha256: c6455f5e1d11073d6d0f9ffe33b6ad7cff64a3088f4a4b672fe0ba1f0ee73472
    role: context
  - path: pages/traits/genomics/tagi_system.html
    sha256: 3f039c8f95c907b89fcb85874539dbbb9ac15f1c544df570b63d4b28a2eae7c9
    role: context
  - path: pages/traits/genomics/taranis_system.html
    sha256: c61a6fdbdcd4d638200fef0dbd103da0a43ab5d707f7bf70666a890e1bead010
    role: context
  - path: pages/traits/genomics/tgvab_system.html
    sha256: c6f8d4fab795f7b9644c5b8e12d9ecc88b34b1d4e3d7534a9c3ca390bc670941
    role: context
  - path: pages/traits/genomics/tha_system.html
    sha256: 5978de5aa83b018dec5ebc9766523ae5159de398be3fa26e479582364e09c0e4
    role: context
  - path: pages/traits/genomics/thoeris_system.html
    sha256: 4344b9c9159022caa5ecabe2752199f0ed80b070de032a1cdee79dad1bba2423
    role: context
  - path: pages/traits/genomics/tiamat_system.html
    sha256: 6f68f3171f428de2bff3767393a67a7c846b519994a1b5a85d50c74dcf83789e
    role: context
  - path: pages/traits/genomics/tir_i_system.html
    sha256: 63611bd8d474d93f4954a33e72083297bfcd851296ca76b2e70823ba1dfd67f4
    role: context
  - path: pages/traits/genomics/tir_iii_system.html
    sha256: d57f16d52fd60d377b249a865bf78b1d398e3d111e9a8fa55c41d7e804033f02
    role: context
  - path: pages/traits/genomics/tir_iv_system.html
    sha256: e3e080642471123e3c819693b128e439441c0d7facee78809703adf4895ced2d
    role: context
  - path: pages/traits/genomics/tir_vii_system.html
    sha256: d8659371fbed9ff17c189e0a5bc8d27525e4bdeab45cf954e2f79e892e0939a7
    role: context
  - path: pages/traits/genomics/tir_viii_system.html
    sha256: 21acb406dba6e68e941af71e278b95e58300d80be6f984faa6e46002eb9163e5
    role: context
  - path: pages/traits/genomics/toga_system.html
    sha256: 2a6c07de2eb4e4dee94108788a9caaf7ac893117e573548dad5f42dde02c7354
    role: context
  - path: pages/traits/genomics/toutatis_system.html
    sha256: 8f673a31f2d1a8748862ad92e80e66f572db00843412f4ba61ecb73520050276
    role: context
  - path: pages/traits/genomics/toxin_system.html
    sha256: c6d9935dc787a468bc05ba199654036f133ea373a5e555b0722c50c498939331
    role: context
  - path: pages/traits/genomics/transposable_element.html
    sha256: 0e676e7d2e8fc14da71aa6b8553d8113d0c1426309d05856c4cf7f8f1b992817
    role: context
  - path: pages/traits/genomics/type_i_restriction_modification_system.html
    sha256: 788b33c20ff89fcaa45d6a890b23636d77c0130401b264b05596e474ed48a4f3
    role: context
  - path: pages/traits/genomics/type_ii_restriction_modification_system.html
    sha256: 971e66a6800689561e574cf7eeb247a2742ce9c1ac718871193c951fc77b8db1
    role: context
  - path: pages/traits/genomics/type_iig_restriction_modification_system.html
    sha256: 9b5d5d015cd3ed90c51f9abdd347e84ea40c1108524cd8c824d5b9e21cbd7535
    role: context
  - path: pages/traits/genomics/type_iii_restriction_modification_system.html
    sha256: 95a5240cb1ebef812eab89099d8f81385135cce6a15ffa909e29538b87ad331d
    role: context
  - path: pages/traits/genomics/type_iv_modification_dependent_restriction_system.html
    sha256: f69c6fd80a0ec08b4e53230d3b2eaf7daa831b4b36c55c77212ad7a20c1ce0e4
    role: context
  - path: pages/traits/genomics/ukko_system.html
    sha256: 32a2430f2fb98cd8f64e7c1c0ff9ed697c3d7cab1bbfd52c5207d6a57a9afe47
    role: context
  - path: pages/traits/genomics/uzume_system.html
    sha256: ad42084467040f66039cef9ebf68b7e646e96881d88e1eec89bbd197c6f02e1b
    role: context
  - path: pages/traits/genomics/vcam4i_system.html
    sha256: 58437471bea4414d1d9b110c05b665fbf02f4cb86f2f27b58d5aebeb041764cc
    role: context
  - path: pages/traits/genomics/veles_system.html
    sha256: fa95fe29275529b5150807967bb434986587714d72bc116a80cd31948376bd4b
    role: context
  - path: pages/traits/genomics/viperin_system.html
    sha256: ef19a03e1a288635f8936ee59e14592bce067b6c9afa06b6ee11aba453c80330
    role: context
  - path: pages/traits/genomics/vp1796_system.html
    sha256: eb9c125432ad661f4bc104e14ec5c3e7920bd53b31e518e8f4040a8256c8e2aa
    role: context
  - path: pages/traits/genomics/vp1817_system.html
    sha256: c8271490ea576576d370f3bbb55e33200ec6fd35e2ec0c047a5927ccb486c679
    role: context
  - path: pages/traits/genomics/vp1823_system.html
    sha256: e3ffc5297e0237bffecf294771272b112724cabe427147d1d303666e6793a8ff
    role: context
  - path: pages/traits/genomics/vp1826_system.html
    sha256: 68ec38445c5d9b705a33302d71640179d85879e760db7b8b47d1db466bf4ce0b
    role: context
  - path: pages/traits/genomics/vp1839_system.html
    sha256: 26fc28b657c3dc0eefde36b3769b5e053e7dd1b0925f12df8f87a0dfd7b40286
    role: context
  - path: pages/traits/genomics/vp1840_system.html
    sha256: 3f4a64e419551e668ee6d13b9b6581e45fe6b65f7e6654dbfbc63f550e20428b
    role: context
  - path: pages/traits/genomics/vp1848_system.html
    sha256: 7a4e8dd54cd983dcce3944eaec26f4fda457e13364ff360a3bddcccc6221a724
    role: context
  - path: pages/traits/genomics/vp1851_system.html
    sha256: 131d2456e4a76ae51a5498f525d13339f1c4c60f13de443a6cd1c6e5b8042f8d
    role: context
  - path: pages/traits/genomics/vp1853_system.html
    sha256: 2f0cd9108f97fa026c4880eb17962f854a71d4918e6217c192bc1d52c91688f8
    role: context
  - path: pages/traits/genomics/wadjet_system.html
    sha256: 216a0d64e3e275bd295559b324c89cdefa8f3abb54332cd2768f3978d831b350
    role: context
  - path: pages/traits/genomics/zorya_system.html
    sha256: 0aabb36f6ec118901a9ba46157ad00295a421da4f25bae5c8331868e9805a5b8
    role: context
  - path: pages/traits/genomics/zorya_type_i_system.html
    sha256: debc1fb56be4f529bcca2ea869a7b02c232449d04152d7d24807f402e0cb70c7
    role: context
  - path: pages/traits/genomics/zorya_type_ii_system.html
    sha256: 538fc92b9b10e264f4a1a296ad41084143045abceb682d7e36b3fced5ceafd8f
    role: context
  - path: pages/traits/genomics/zorya_type_iii_system.html
    sha256: d2138ecde84e53e8591aa3f160acd25da270be5e2c0e92e2d8b22c790889baf8
    role: context
  - path: pages/traits/metabolism/accumulates.html
    sha256: 3b4e20826d5944e475a4d22e92d1eb5d4eb4d26cf349da375e98400e1f64820b
    role: context
  - path: pages/traits/metabolism/acetoclastic_methanogenesis.html
    sha256: 05346866478c7f4428b8df5a8ae5b6ecce8c9ce6d3f1123d28795c2e8970a4e4
    role: context
  - path: pages/traits/metabolism/acetogenesis.html
    sha256: d2be49e89634e399ca2cafab69511f1b78de088d5be1eddc3b2c268c8c5ac17f
    role: context
  - path: pages/traits/metabolism/acetone_butanol_ethanol_fermentation.html
    sha256: 67e343c3d2af386315b630e09391f492716fc3911bc58fd9b4edccd7be70a577
    role: context
  - path: pages/traits/metabolism/aerobic_respiration.html
    sha256: 1992598489b915d9640995d60c8f4258947178bea2cc940d5c4fbd6ea42fba99
    role: context
  - path: pages/traits/metabolism/anaerobic_ammonium_oxidation.html
    sha256: f75d9e9c9a592be1dd29749ff29987bd083322986381668ce1204d9a7e906307
    role: context
  - path: pages/traits/metabolism/anaerobic_oxidation_of_methane.html
    sha256: 260bc75246ee0ca381a91ca40eb0609f4e943932957e6289a945fc7439cc950c
    role: context
  - path: pages/traits/metabolism/anaerobic_respiration.html
    sha256: 3c951788d278772b2fe566e2d5da7ad7dcd45dda17cabdaae12d215dc0f47c7b
    role: context
  - path: pages/traits/metabolism/anoxygenic_photosynthesis.html
    sha256: 2d39a0ccc8aca47a6ea0b7359b52900320e65d4675adc320efb29bc37ad367a3
    role: context
  - path: pages/traits/metabolism/aromatic_compound_degradation.html
    sha256: 2d1351a20a68a082da251b86f28dd9b6245870202b597aaa838e40cd3526ce40
    role: context
  - path: pages/traits/metabolism/aromatic_hydrocarbon_degradation.html
    sha256: f89c8bb8974c5802bf07da4c9bd7008ae8fcd787cc403fb00284f04938575c4b
    role: context
  - path: pages/traits/metabolism/arsenate_respiration.html
    sha256: 8ed915c0db36aea0d7ab0bdccb199ea60eeed4191d50e5c22a416c76a28cc99b
    role: context
  - path: pages/traits/metabolism/arsenite_oxidation.html
    sha256: 8a680dacaf192646e6f94aea823cf72ddf31756e1f79ffb7f25b4b0f5aaa772b
    role: context
  - path: pages/traits/metabolism/assimilates.html
    sha256: f47af44bc8630b8c3a8c42d475dc03670b597ae8351969485ae8eeb03112d0db
    role: context
  - path: pages/traits/metabolism/biopolymer_degradation.html
    sha256: ae79c53932fbcd6e8ea4dec06fc91b170732418ce64091bbcf6901c4a1ea52dd
    role: context
  - path: pages/traits/metabolism/builds_acid_from.html
    sha256: 9c493b712e7ecb749bb95983e34776644bf66a6672f0f478d869cf5d343dbddc
    role: context
  - path: pages/traits/metabolism/builds_base_from.html
    sha256: ee80a9717efe408a5c53581e7fd67816789e427de96d6e28ebec6730d09438f0
    role: context
  - path: pages/traits/metabolism/builds_gas_from.html
    sha256: 4cf8f83fe0b1c3d06849932401a5e300b278039e4bd9dc9ff4d31183076cc807
    role: context
  - path: pages/traits/metabolism/butanediol_fermentation.html
    sha256: 3762eaa457f0d35a7ddbe2cd801fecff384fffd18b82b98427eea599ddcd9c5e
    role: context
  - path: pages/traits/metabolism/butyric_acid_fermentation.html
    sha256: 2a1e9f40fb0871a2ceb95850997fefa1c15e81c7035faf5537578312cb216b2a
    role: context
  - path: pages/traits/metabolism/cable_bacteria_metabolism.html
    sha256: dece564a4a095cf89da8af5ae34d81d1577f922ff7560aca1602f9d0518c26f7
    role: context
  - path: pages/traits/metabolism/calvin_benson_bassham_cycle.html
    sha256: 8132c8d678cc854a6786cb11ad3175e33c231aeb7934ce9ae5dcf0f4c6e1353d
    role: context
  - path: pages/traits/metabolism/capable_of.html
    sha256: de373a2088786246e5251a5da127772212098b40bc9c789370d81bf464d4f157
    role: context
  - path: pages/traits/metabolism/carbon_fixation.html
    sha256: 1db9c44177d0d535708a80b39ba768b0512168812deb17c05adb90e21e06869d
    role: context
  - path: pages/traits/metabolism/cellulolysis.html
    sha256: 2352d6b861c36d6294865c0936da4c48c1ba7f04664d98dacf77a77e67a09aaf
    role: context
  - path: pages/traits/metabolism/chitinolysis.html
    sha256: 2eae4c627ad8485f0af4ba55ea5a6eb3cbaca9ac310a837fa3a3444f76c56b5f
    role: context
  - path: pages/traits/metabolism/chlorate_respiration.html
    sha256: 7375d4e820e5995a1dddbe9d35d53d27c920d40da8f149c4a5e85dbe7f0137f1
    role: context
  - path: pages/traits/metabolism/citrate_fermentation.html
    sha256: 4f8a3fe427069502a632d10afe39e4e7c1d6e2d76a336cdc90fe606d218e497c
    role: context
  - path: pages/traits/metabolism/compartmentalizes.html
    sha256: 62f48a429366cc233b63a4cdcac97e6cbc3bffe5e1f56a3f7770c65a6e5bddbf
    role: context
  - path: pages/traits/metabolism/complete_ammonia_oxidation.html
    sha256: 8a120980b2bac4a52b514dbc92ad884d4f011cbd9098db84421d10b22b2ecefa
    role: context
  - path: pages/traits/metabolism/dark_hydrogen_oxidation.html
    sha256: 8e1c5969980e17a5e78b0e5f1ad5be28efaee7dff1a61770deecfe6f61a30d41
    role: context
  - path: pages/traits/metabolism/dark_oxidation_of_sulfur_compounds.html
    sha256: f2a43bec16ee54473dc10598d53ad595cefdc19b75c823a9b587839bfbff314b
    role: context
  - path: pages/traits/metabolism/degrades.html
    sha256: e6f3b73d62ed96686f2f77a85d58f7c0eec1d960ec539e2e7730e486b6ac59df
    role: context
  - path: pages/traits/metabolism/denitrification.html
    sha256: 2bcb3091e69518da5e6018926d8852641f0f7897693ceaea6b6dd95898c5ead9
    role: context
  - path: pages/traits/metabolism/dicarboxylate_four_hydroxybutyrate_cycle.html
    sha256: da77ba5bab4ee2e8c4767d2ddba27f5a2b85e4d4cf58fc86bca34e97958072be
    role: context
  - path: pages/traits/metabolism/dimethyl_sulfoxide_respiration.html
    sha256: f0ed0da55e90d856c5211d0f8565fcd7434c78a7b103d9c1ff0c8d85fe458d9c
    role: context
  - path: pages/traits/metabolism/disproportionates.html
    sha256: d4debd373e94b3e02db2f34c5aec8ccc031421e2e6a606cd476edcc859d86d10
    role: context
  - path: pages/traits/metabolism/disproportionation.html
    sha256: 6ffa5cc70003fbaea4094bf4ed982fb51831bc38fa8b85a1dab9b76fdfadc2e4
    role: context
  - path: pages/traits/metabolism/dissimilatory_iron_reduction.html
    sha256: 0debd28b2f04d6a5b9c1dbeeb94aa51bc0c9baf3067108a174373e0d518ac4b2
    role: context
  - path: pages/traits/metabolism/dissimilatory_manganese_reduction.html
    sha256: 2dd85db9349057478167e9274a57020cfa024809527c7b50d7a3cc1eb9fbaf42
    role: context
  - path: pages/traits/metabolism/dissimilatory_metal_reduction.html
    sha256: 5ce5189721ba4d5367d2970a26bef952426c5b78c0c99403ee22764a574dad72
    role: context
  - path: pages/traits/metabolism/dissimilatory_nitrate_reduction_to_ammonium.html
    sha256: e8067d79254a309625861b9cdf20970e6ccecdaaaeecf1c2db43e11ae8b3a27a
    role: context
  - path: pages/traits/metabolism/dissimilatory_sulfate_reduction.html
    sha256: 5abe0a37802dc30f56dc2b5ca84e2874d08d98cb28e548f936b7c97bdb0e9835
    role: context
  - path: pages/traits/metabolism/does_not_accumulate.html
    sha256: e0c2d28d1db32adbf7bdb17a9c88422eb3718b477c36a07a2468d8effaee9d41
    role: context
  - path: pages/traits/metabolism/does_not_assimilate.html
    sha256: 5d57d8b66fe63ea10a3201373e3b05a6fac350ec007d2e3e1a14a9a0c6121d2e
    role: context
  - path: pages/traits/metabolism/does_not_build_acid_from.html
    sha256: ab91cd966f118cc682feffcc40a7c4087e3200d88f71758d97ba9e36c2a6a355
    role: context
  - path: pages/traits/metabolism/does_not_build_base_from.html
    sha256: 8c49e3f17b7c8c5c28d0a36ddf1c2536546dec0950c02848a054a61f89b3f05c
    role: context
  - path: pages/traits/metabolism/does_not_build_gas_from.html
    sha256: 0d2fa49c65e8d92ba92ff3a99ac302b3974dc0a08c1724787dc25ca10e6e9ba7
    role: context
  - path: pages/traits/metabolism/does_not_compartmentalize.html
    sha256: 5ec317a79eb92d45fa8d4019903746caced6939e04abd5d86eecffbbf57e51e5
    role: context
  - path: pages/traits/metabolism/does_not_degrade.html
    sha256: 27561cad36143c1fbfce6e4e375fb65b5bba520fcde404a7f03cef3c286cffc7
    role: context
  - path: pages/traits/metabolism/does_not_disproportionate.html
    sha256: 52b803036f5c3ece0230ed00c4f23bf744b3b7cf0cf71c4805907010b7da57e0
    role: context
  - path: pages/traits/metabolism/does_not_export.html
    sha256: 788708ee0e4e8769ba83ff3b56198e212fd27218fd7bd7dfef3ae5642c24fa93
    role: context
  - path: pages/traits/metabolism/does_not_ferment.html
    sha256: 7e32392dbec3b7d695fbc89d38dfe9d1dbb039a80e2c2272165975b8438285ae
    role: context
  - path: pages/traits/metabolism/does_not_hydrolyze.html
    sha256: af8970d8d6f1d34c9c5396a2a8968e44fe0b8e1354661374dc8888c363e645ee
    role: context
  - path: pages/traits/metabolism/does_not_import.html
    sha256: 8fde28d79596108d44ee8e00e4fc93ba970b954bee1a7c3f712c4422c7068350
    role: context
  - path: pages/traits/metabolism/does_not_oxidize.html
    sha256: b6419102de27aaaf925236463ed8d27e96809dfdc9ce53d8b5b5e4d845bd80d2
    role: context
  - path: pages/traits/metabolism/does_not_produce.html
    sha256: 3da3059ffb79dadc4f80a175884c66c0d95a5612a5a7546a21ca8268d11fdb68
    role: context
  - path: pages/traits/metabolism/does_not_reduce.html
    sha256: 5841a85471138e81cd2daa482434d0429f69ca00dc16dd1e9b3ff87b69276c81
    role: context
  - path: pages/traits/metabolism/does_not_sequester.html
    sha256: a0fe84a6e94d66a4c96efa782850dcf25f327e681f221fbf58152077a7fb31ca
    role: context
  - path: pages/traits/metabolism/does_not_show_activity_of.html
    sha256: 64b27c3c905640e12b5302d73f330c046cbaa24be51ef7f52b387e6b98799485
    role: context
  - path: pages/traits/metabolism/does_not_transport.html
    sha256: e7fb3b18cabbb10cc72a724e252d002761aec435a5a34bcfd729ef1c9397d0d7
    role: context
  - path: pages/traits/metabolism/does_not_use_as_carbon_source.html
    sha256: f136c9e96227f8d201044d74c04da01dd18a91f20e2ce728100aaab81b8c85ec
    role: context
  - path: pages/traits/metabolism/does_not_use_as_electron_acceptor.html
    sha256: b0910321732ebf7e77e1a5007ee8e4b52f3e6cf939fe6aeb2661bc37473524ae
    role: context
  - path: pages/traits/metabolism/does_not_use_as_electron_donor.html
    sha256: 4cd6ddce21bbee128791bf4080e7230621d7cd2a2e96fb612eda228b5c9273fd
    role: context
  - path: pages/traits/metabolism/does_not_use_as_energy_source.html
    sha256: d42e49acf2262c67d9f74f2c5f535402f02ff51e87f1168cba1910e0f0869759
    role: context
  - path: pages/traits/metabolism/does_not_use_as_nitrogen_source.html
    sha256: f3857568e5ad130a925e722f0308faa0dc1455f05496581bd162a2d0b33c1fea
    role: context
  - path: pages/traits/metabolism/does_not_use_as_sulfur_source.html
    sha256: be316c722661ad0b87f6e25f84c4d15bb536aba4340809caab487521ed29a4b1
    role: context
  - path: pages/traits/metabolism/does_not_use_for_aerobic_catabolization.html
    sha256: cdf81f65c968d97680153c0b7b20eb7d5bb9d7b0357471df13e710d8dc50c33f
    role: context
  - path: pages/traits/metabolism/does_not_use_for_aerobic_growth.html
    sha256: d62efbba1a61ae59cf8a1585c01672b9dff129b012ab9aaf4c14e8734962603e
    role: context
  - path: pages/traits/metabolism/does_not_use_for_anaerobic_catabolization.html
    sha256: 227480a8f5a13e2fbca3b57b8c73039f870c1563f55310aafb96b148536d09f2
    role: context
  - path: pages/traits/metabolism/does_not_use_for_anaerobic_growth.html
    sha256: 78e2e48fa0c455c92e92bf293cf5bf611129cb4d3d5f5c9385d46c90749afac1
    role: context
  - path: pages/traits/metabolism/does_not_use_for_anaerobic_growth_in_the_dark.html
    sha256: 53e63e5aa9787c3a7828b510ee60e42cecab03d847f0468a403ffd9d2bb61e14
    role: context
  - path: pages/traits/metabolism/does_not_use_for_anaerobic_growth_with_light.html
    sha256: dacd7629f3071854beb4962f8224f0f214453d828a9623050ba37f5e2a012757
    role: context
  - path: pages/traits/metabolism/does_not_use_for_growth.html
    sha256: be8710362f79294f103dd6f1c1ecf24f8081a8f2548c08ff7cc724702b063900
    role: context
  - path: pages/traits/metabolism/does_not_use_for_respiration.html
    sha256: 6ed009a5bbaabb51b8856c763598ec8694df2ff4d969ae226226650c3416dee4
    role: context
  - path: pages/traits/metabolism/does_not_use_in_other_way.html
    sha256: 771a00366b18a84c8deae308d913c397552f1829b149feb57cdaf3aea1397d0f
    role: context
  - path: pages/traits/metabolism/electron_transfer.html
    sha256: ff3593e30b52d024b0fa9c629385ca87fa9d60a77257ff93c4223dfd3ddc8308
    role: context
  - path: pages/traits/metabolism/enzyme_activity_analyzed.html
    sha256: 072afc32312bd7e02e6f24176fcaa6f23a2fd7e8634e3fe01211f8d437885125
    role: context
  - path: pages/traits/metabolism/ethanol_fermentation.html
    sha256: 1e459e93861974d20484ab965445bdb424f94dad5cb421cbca0938dd0101aa36
    role: context
  - path: pages/traits/metabolism/exports.html
    sha256: dc3eb58e587e4ff694e060df01ce46ad3cf1f54aa45a613fd57579bf82c3d581
    role: context
  - path: pages/traits/metabolism/fermentation.html
    sha256: 49d88e1973385591cd7edfaa1e1d1e061f96a09b12ce0093574d89c0ffd3e772
    role: context
  - path: pages/traits/metabolism/fermentative_hydrogen_production.html
    sha256: 8c36bebbade6af2c540b9e3cb142a7cb9d7c4512f504c14343752bf8aa708e96
    role: context
  - path: pages/traits/metabolism/ferments.html
    sha256: 03494f302fef20d5f89e56ea7dd82f35ebde9a484dd0760d829fc4251ea786f3
    role: context
  - path: pages/traits/metabolism/fumarate_respiration.html
    sha256: 2bce1194bced53e73103233a92decc8e0a0589a8047f56471a102f3494cd9978
    role: context
  - path: pages/traits/metabolism/has_growth_nacl_observation.html
    sha256: 566049508a4eb05ec6df17ae86e4699584f5a8d26c4cc24457e86e689695a675
    role: context
  - path: pages/traits/metabolism/has_growth_oxygen_observation.html
    sha256: 11fca959350a3a6d65f9a1883e9a89bb21cda4be1724876d0a50f391babbf66a
    role: context
  - path: pages/traits/metabolism/has_growth_ph_observation.html
    sha256: f0623c20ee4ca9b9a082ad9a155b80b66b863856f6b44478fb5232d82cfd1cf5
    role: context
  - path: pages/traits/metabolism/has_growth_temperature_observation.html
    sha256: 513a4006a554a015fdf36eb21a2b200400393ef9a8eb896fe87f31309c07aa8c
    role: context
  - path: pages/traits/metabolism/has_nacl_delta_observation.html
    sha256: 92f203e69f2d9385390ba8ba54970e1a579f35e4d2838ef91b979762b2f74ba7
    role: context
  - path: pages/traits/metabolism/has_nacl_observation.html
    sha256: bbf3d4506fc5a89acb92693e31ab4eabd2d6fe3d69a09dd72df6d95042d8dec7
    role: context
  - path: pages/traits/metabolism/has_observation.html
    sha256: d6dd8b29d32922e20acd684e4dcf7d0bbc1d82624a58f85fe4de858cae0b1930
    role: context
  - path: pages/traits/metabolism/has_optimum_nacl_observation.html
    sha256: 21c674296bbb547a0b9596dab51a37112cdd4ff07b21021b9a7491e965f00194
    role: context
  - path: pages/traits/metabolism/has_optimum_oxygen_observation.html
    sha256: 173fed4ac2ae24dea9069edcb364d64623df047e3dbb4e50c7fcad4c1d410e55
    role: context
  - path: pages/traits/metabolism/has_optimum_ph_observation.html
    sha256: edb19e0fa472c8c886d1a7237a89711d274c19d802d21fc3bb640f01b221f8c0
    role: context
  - path: pages/traits/metabolism/has_optimum_temperature_observation.html
    sha256: 95cd18a109fd015eac54a50856206784854dffa9b2f3594a14601db630647745
    role: context
  - path: pages/traits/metabolism/has_oxygen_delta_observation.html
    sha256: 3becd09fc3b5368498dbf42e1d73955bc7d934a5c9cbaed4bf13f5c87b1059e8
    role: context
  - path: pages/traits/metabolism/has_oxygen_observation.html
    sha256: d18351a97009fa9c2a35acf5673ebbf43004e5d55e2da4e2286d280c43fe52b7
    role: context
  - path: pages/traits/metabolism/has_ph_delta_observation.html
    sha256: f0fc77f1893c37b86dcff14ede60ef0edc5b23758103d3f65458342bbae4f85e
    role: context
  - path: pages/traits/metabolism/has_ph_observation.html
    sha256: 6ff84a2a525c435dbfc66f630fd9ea9fdc197e20955479ddfb817054bc3bf1bc
    role: context
  - path: pages/traits/metabolism/has_phenotype.html
    sha256: 47b7d22f76ebd647f460c502ee7da30a366d627420328d6856a2fbf9ea04a821
    role: context
  - path: pages/traits/metabolism/has_quality.html
    sha256: fc2b1d5049558c32bb5f5202ca2415d4724195b4a189cb1793d6ae8131c8204e
    role: context
  - path: pages/traits/metabolism/has_range_nacl_observation.html
    sha256: da8f3989a4b33cf611854058efed1e6243c0c427317f1a3ee22e51db7022cca0
    role: context
  - path: pages/traits/metabolism/has_range_oxygen_observation.html
    sha256: d170bdbf42783db6c5fa4432a5a52b138cdfc1fe9c89d1eb67e4ea8a13e811cd
    role: context
  - path: pages/traits/metabolism/has_range_ph_observation.html
    sha256: 46801cda7d389013486c01c23a052fa6a8d05d1bef1737b1cd9b5e479b15bb1d
    role: context
  - path: pages/traits/metabolism/has_range_temperature_observation.html
    sha256: 765785b562a69aa68102ee438b9df2ffca2196fa4e32aa35ad368552f87fda16
    role: context
  - path: pages/traits/metabolism/has_temperature_delta_observation.html
    sha256: 59dc00fc9c6dce6ef3d8c390c4de5a52ca9b87cc9388f2898108d0abf7951afa
    role: context
  - path: pages/traits/metabolism/has_temperature_observation.html
    sha256: dce14a00368edd24027cdb97e6be40358e870877006a87ca6bceaeff2e69506a
    role: context
  - path: pages/traits/metabolism/homoacetogenesis.html
    sha256: 5f0d4b8c45debc56f0eea7819a7c2a0f99073e3aafa197d7c29127fe6c2526d9
    role: context
  - path: pages/traits/metabolism/hydrocarbon_degradation.html
    sha256: 2d4b96e84e07a7f456ea88a8e786dd57e052cb1a35a6afac947293d2a789f967
    role: context
  - path: pages/traits/metabolism/hydrogenotrophic_methanogenesis.html
    sha256: b30fb33b956cd35252694b033f59bc9df1ebd100b77d073d5a596c4362679819
    role: context
  - path: pages/traits/metabolism/hydrolyzes.html
    sha256: 493bcce7db1e5d28ab238bcb1b41637477df8b1753184bd804a313391b4dd9f8
    role: context
  - path: pages/traits/metabolism/imports.html
    sha256: b23be9d5e98aa6d2055766e383623b29f4b2d8a981e41e83eb411b8038a11bd6
    role: context
  - path: pages/traits/metabolism/iodate_respiration.html
    sha256: 771e3545322199a42fc04ea6a39d139b13ed00edae5b29f89b889946e6c7ef40
    role: context
  - path: pages/traits/metabolism/iron_oxidation.html
    sha256: 920ce55a5989dd36bfb724c2f75d7809ac14d03e0d3869f56dd4ab15d0e5a476
    role: context
  - path: pages/traits/metabolism/is_not_required_for_growth.html
    sha256: bb021e1999ebb47d7a05a9986f571a34afdc3b709abde07cc0d41b6355d2f9ad
    role: context
  - path: pages/traits/metabolism/lactic_acid_fermentation.html
    sha256: aaa798d1c4bc93de594e69e36455944635fad7aedf90b73bbdfcc8761454d612
    role: context
  - path: pages/traits/metabolism/lignin_degradation.html
    sha256: 25ff8b56bd639364b0fa7e638ee517d3184474838bb8f4fefbd91aba20574321
    role: context
  - path: pages/traits/metabolism/lipolysis.html
    sha256: 7202caa62e7aad13ea9dc4ad0fd3e5fa79ae1aa26d0c79b57284d2c4b57e66ed
    role: context
  - path: pages/traits/metabolism/manganese_oxidation.html
    sha256: 096a9dd0cc8b25e1c3f910056e2f30270b5c7e892b16e6d213f8afb4bee66694
    role: context
  - path: pages/traits/metabolism/metabolism.html
    sha256: af7164efbea833e1e2d611b7e636da91027ba6dceecc542fb3ed2875a43eb9ef
    role: context
  - path: pages/traits/metabolism/methanogenesis.html
    sha256: adc845268c688f34616e1a37b63bf19d9ba6a57ed5ae038d08da8fcf03a5960b
    role: context
  - path: pages/traits/metabolism/methanol_oxidation.html
    sha256: 90a968746dd2655886118cc4df1da276cf6cb94b4c8a023035a9db9c63d3ea83
    role: context
  - path: pages/traits/metabolism/methyl_based_methanogenesis.html
    sha256: 5bf1e47e657eef5fb4c35362c6041ebd43c526a5f7edb836c9fd999e2b151794
    role: context
  - path: pages/traits/metabolism/mixed_acid_fermentation.html
    sha256: 819062d36ec30e178d66ba3c4c2528522ea6698369fecc1188a7a663e0e2c792
    role: context
  - path: pages/traits/metabolism/nitrate_reduction.html
    sha256: e870434f45f2caa044f158bedc263e8e415d9bffc2f3bf4e387e2ba6a40cb69a
    role: context
  - path: pages/traits/metabolism/nitrate_respiration.html
    sha256: 81d0ce8def9e37aa60e75bae778c7cf7120da179eda9ac8a9e269851e3f5a675
    role: context
  - path: pages/traits/metabolism/nitrification.html
    sha256: 8e94820d9fc5cbac6c7d67996d28abb0f278e18d1990eee032905d7484b49f12
    role: context
  - path: pages/traits/metabolism/nitrite_respiration.html
    sha256: 6b5a14e6ea2b004f8b4dde23c1360871663aee6240ec09f2a1a66e40b0533c7f
    role: context
  - path: pages/traits/metabolism/nitrogen_fixation.html
    sha256: c88cccf78f00d326d2b65abe2c1f0f405359dc44d78b2da9db3d36dc4ff0ad8b
    role: context
  - path: pages/traits/metabolism/nitrogen_respiration.html
    sha256: b62c921ba09ddf4359cc6ac5c32fcb676de252ae9a1d98cf9e8dc4a3843cd0e0
    role: context
  - path: pages/traits/metabolism/organism_interacts_with_chemical.html
    sha256: 4a8d514ea9b5873423505f1cbf577b71a210253473162c2b35fb8f337d853011
    role: context
  - path: pages/traits/metabolism/organohalide_respiration.html
    sha256: d1e281ceb368063d4bf8b3a3ed5ccfc57e6da3f7ca1381d46c92e518696d13b4
    role: context
  - path: pages/traits/metabolism/oxidative_phosphorylation.html
    sha256: 95914e126bfcf0fdf758a5b8cd10e8907e7e0b68beef586ef46c3df76536d91c
    role: context
  - path: pages/traits/metabolism/oxidizes.html
    sha256: d85f471b008b654b6ada73fe905cbd2044c617b70012655e6f6675635ac299e6
    role: context
  - path: pages/traits/metabolism/oxygenic_photosynthesis.html
    sha256: f90722523e9bbac4c2f43481794854bd8480ea52bc71cf11d426bfe63cc18643
    role: context
  - path: pages/traits/metabolism/pectin_degradation.html
    sha256: d0723e245fc204842af96784646a8b5a74af7172879bab99be9f50516b321c0f
    role: context
  - path: pages/traits/metabolism/perchlorate_respiration.html
    sha256: 0030d9d53db4ce4d060d8f604ad5cd84f4a83448580f472a51b8a782f04466de
    role: context
  - path: pages/traits/metabolism/photoferrotrophy.html
    sha256: 7b618ab6b2d0ac9df8c4f5e9eac24e524a151b43d4572818ee69aa27841845ea
    role: context
  - path: pages/traits/metabolism/photosynthesis.html
    sha256: c02b12bd2a775a206b270a124efffaa2471e73f188588ab8a410b89e8f949e2e
    role: context
  - path: pages/traits/metabolism/phototrophy.html
    sha256: 201d955af439d7f465402eb8998524f9a691dd428a43dfb641ba2173948f708c
    role: context
  - path: pages/traits/metabolism/produces.html
    sha256: b628301417b7551ec9480c949e7088afa03414fa8130e976c9fb9aafc6772b6a
    role: context
  - path: pages/traits/metabolism/propionic_acid_fermentation.html
    sha256: 7e89de2776e3ed70253585aa99869334a127ea21629bcc7eaa2f90582d7ba51f
    role: context
  - path: pages/traits/metabolism/proteolysis.html
    sha256: 0452bf5a35a8b0a3206f5d3bc954c27216bfff4c76f543d02f8632c7aadbe132
    role: context
  - path: pages/traits/metabolism/proteorhodopsin_phototrophy.html
    sha256: 2b78c6e3fe03e3277c9d56d79460556d2d23f064b1edf1682f8d094f8130c50d
    role: context
  - path: pages/traits/metabolism/reduces.html
    sha256: 7fc9c50b9e5b99760a9ee6731cea8842b4110e6bda14b4766ac3b6f0e7daa904
    role: context
  - path: pages/traits/metabolism/reductive_tca_cycle.html
    sha256: b139fdb1c6b02ab7171196cebaa570aeee0c5d38868414ef36feb4a94878e073
    role: context
  - path: pages/traits/metabolism/requires_for_growth.html
    sha256: 93070c3b7ba150c59cc3768d6432e8cde4097f38d1f8cfeb13cd68e416dff6a0
    role: context
  - path: pages/traits/metabolism/respiration.html
    sha256: 91b2aab4d912e9313af3e5141cd65325c5e4b28998c87326d5991dcbe9897e14
    role: context
  - path: pages/traits/metabolism/respiration_of_sulfur_compounds.html
    sha256: e9f36fe72aebea8d67dd7af91d3ceac9ba47f554809d9ee91231e802c2c6b23a
    role: context
  - path: pages/traits/metabolism/selenate_respiration.html
    sha256: 3805b1e039e9743c93d72b0f6140ff8aa980da85f480ac8bbe3ccf826412b49b
    role: context
  - path: pages/traits/metabolism/sequesters.html
    sha256: 507b6d9104937292b5a8734e6fa7b52ee7e70e887bd1be99ccd3646b02a686b4
    role: context
  - path: pages/traits/metabolism/shows_activity_of.html
    sha256: 39bd8d63213a8197ca77b1fc59e3c8090417259b559f7b7a5cab3d8fde5251db
    role: context
  - path: pages/traits/metabolism/starch_degradation.html
    sha256: 1ece9b5e0141e03e95c0c7209863dac8d5927daa478fd11170f27f3dc841d08b
    role: context
  - path: pages/traits/metabolism/substrate_level_phosphorylation.html
    sha256: ddab3c72f9f78fe64a846f6148b70aba3c18c3af8a47f3d22d5597cc4d3291ec
    role: context
  - path: pages/traits/metabolism/sulfur_oxidation.html
    sha256: 3db40d0a2c769f0a5ae44ed29665e3e46a727c00bf8bf48b527c7cfdddb0b4a7
    role: context
  - path: pages/traits/metabolism/sulfur_respiration.html
    sha256: 0c343cc937cdc6144db9114ab1122e799cc5f3695f961e89c3ec764912b27453
    role: context
  - path: pages/traits/metabolism/syntrophy.html
    sha256: 0d26c35be7e266a603a9fa13836edf5371800475020b4ad4ae50bd72d8615262
    role: context
  - path: pages/traits/metabolism/tetrathionate_respiration.html
    sha256: 092627bc651f319b291d6d302d754595745a37c2ffbe6c532b23f0831d951a32
    role: context
  - path: pages/traits/metabolism/thiosulfate_respiration.html
    sha256: 72e44781d8305eed631f09219497857e354363232f0f3bf88ca235e3fd1635a4
    role: context
  - path: pages/traits/metabolism/three_hydroxypropionate_bicycle.html
    sha256: 78ce1ddd5c791b3fce989174ca6859c18c874d267171146d703d7e3b7048915f
    role: context
  - path: pages/traits/metabolism/three_hydroxypropionate_four_hydroxybutyrate_cycle.html
    sha256: 0c20c94218be45d95ef69e150690db103928df01b546c570d695c4b3c4522e91
    role: context
  - path: pages/traits/metabolism/transports.html
    sha256: 73b1649a33158fd181ced53e30b872d426e7ea4b2674c11a0808c3c4a9bfdbe8
    role: context
  - path: pages/traits/metabolism/trimethylamine_n_oxide_respiration.html
    sha256: 3e1d292ed571ee78d9b69b34193706c0f697ec5e231ad384ac8d6dc2b55943ad
    role: context
  - path: pages/traits/metabolism/uses_as_carbon_source.html
    sha256: 413e25229e3654068441a145e01387f47a01e0724e166c424131635735272642
    role: context
  - path: pages/traits/metabolism/uses_as_electron_acceptor.html
    sha256: 44bb22d6a7ca23010f9940d8f4d7e9bc71055098d70815cc3a9840cd264a652a
    role: context
  - path: pages/traits/metabolism/uses_as_electron_donor.html
    sha256: 1cfb96439226aad37afa8afee70498af54262da3b99cdff1d4fa95a955ae9da6
    role: context
  - path: pages/traits/metabolism/uses_as_energy_source.html
    sha256: 3176fef3f5238defd368cc2956bdf0c44aa0bf04069d9ae3059421f2dc3ed703
    role: context
  - path: pages/traits/metabolism/uses_as_nitrogen_source.html
    sha256: 87122c31ee44484a84e1d7fae17a4867cdf463157a11b0f4b3d698a702119326
    role: context
  - path: pages/traits/metabolism/uses_as_sulfur_source.html
    sha256: 1c6ff36bd5f17c18fd9e9f2a5026894134e3b6ed315b10321a6f631dd36ece41
    role: context
  - path: pages/traits/metabolism/uses_for_aerobic_catabolization.html
    sha256: 7ba8810aadf4b34d955b6a672086fe8554eeb09a1cbc11a5e0d9292e2f9e877b
    role: context
  - path: pages/traits/metabolism/uses_for_aerobic_growth.html
    sha256: 212d28592aa9f9768ae2c1eefd80f00c1dd0771bf5468e7cd9fb40daf3dc414f
    role: context
  - path: pages/traits/metabolism/uses_for_anaerobic_catabolization.html
    sha256: 2ebdf687b5747db839299749c5ba02cac046b6a01fccceae1cedf4aacc41bc6a
    role: context
  - path: pages/traits/metabolism/uses_for_anaerobic_growth.html
    sha256: 2578267b2e2ee8c2dd3782e3bab6346902948a1080166b6d8b9584290d0a02b1
    role: context
  - path: pages/traits/metabolism/uses_for_anaerobic_growth_in_the_dark.html
    sha256: 9f7d05bb8dd99e5e5f0b1276f6088452a08d3176e86902bc0834a6efcbe51433
    role: context
  - path: pages/traits/metabolism/uses_for_anaerobic_growth_with_light.html
    sha256: fc1b2bbd81205f6f5b7553c800aa1474f7db9d8c7519841286a35b52d93f8eda
    role: context
  - path: pages/traits/metabolism/uses_for_growth.html
    sha256: 4d020de69f5ad72dc84d5680a0fc37bbe0238d1f51ca71665b9eeadcdb90aca8
    role: context
  - path: pages/traits/metabolism/uses_for_respiration.html
    sha256: d524bdd139dd19925887b5e417e5dc6b43a825d89ea04a6f8c014325d37b35b4
    role: context
  - path: pages/traits/metabolism/uses_in_other_way.html
    sha256: 74dc77eb9cb6a39359f5cabe60eb0763fa7fb9008f4cbc31e61d87e1c1f9afa9
    role: context
  - path: pages/traits/metabolism/wood_ljungdahl_pathway.html
    sha256: e7db241f36da17351bfdacaf23e1f6cffa6f346bb79fb4e844748347c0818dd7
    role: context
  - path: pages/traits/metabolism/xylan_degradation.html
    sha256: 00b88b3e7c52956337c72fcd6a9c2651daa449027e1edb3ec85081b9c899268a
    role: context
  - path: pages/traits/morphology/akinete.html
    sha256: 179270976f9f414be23328dd818438a291bc513de4d05210bda05e162f553af3
    role: context
  - path: pages/traits/morphology/amphitrichous.html
    sha256: 2b5cfcaa7c8ab9dc913ba1ca751e16c90a3ca3cc80d1a50613fc25e4cb4ae04f
    role: context
  - path: pages/traits/morphology/axially_filamented.html
    sha256: b35161dd0310e62114f0f593e4b0afac70e0a8a7905fc0827d05e8aa665bc8ad
    role: context
  - path: pages/traits/morphology/bacillus_shaped.html
    sha256: a3ec6cfe26798c4a95b8d969e590ee92fd437a2d9494c3289869d6121bea269e
    role: context
  - path: pages/traits/morphology/baeocyte_formation.html
    sha256: 03aa4e0dd08663fbe0c633530f101ff4b65285a20a416022d2c31599fe7140a0
    role: context
  - path: pages/traits/morphology/black_pigmented.html
    sha256: 8f0cccf8568ff7b128335a1798dfa56f98edc2e14d550edcce413808bd42e020
    role: context
  - path: pages/traits/morphology/branched_shaped.html
    sha256: 5a4a406e7a8dda525f9268a8b74e66bd0b322ab7ae9a1ce82570d0fd840b195d
    role: context
  - path: pages/traits/morphology/brown_pigmented.html
    sha256: 13ba06e1b9632ca5e57aac41d3aefca59b4ead85f3374a66936f533a812be46a
    role: context
  - path: pages/traits/morphology/capsule.html
    sha256: 5189d55cb3b428d74c3c3ee77eb3f8794a954a4b8dbd8c62d88e7e0d2d47c5b8
    role: context
  - path: pages/traits/morphology/carboxysome.html
    sha256: 51ef20439633feee29cd181329f63574cf2ee9cfa60f5bcf63728166ac6561cc
    role: context
  - path: pages/traits/morphology/carotenoid_pigmentation.html
    sha256: a17a9a0e2c6c700970d4941bf80132a30942deb29075793ddeefbe55037bbcdf
    role: context
  - path: pages/traits/morphology/cell_length.html
    sha256: 1bf7d0bde7ac3cd0f423f02ec89cef5d8151de7a0ece2795f13c60f6ca739ffd
    role: context
  - path: pages/traits/morphology/cell_length_large.html
    sha256: 1e05397d9457eaf8dcd2f2af823c1935b0e634b2266e9e22f6e1e362c1506c86
    role: context
  - path: pages/traits/morphology/cell_length_medium.html
    sha256: d272256559a938aa78092975d6cf726668992f73abe8f7def4f263dc141001d7
    role: context
  - path: pages/traits/morphology/cell_length_small.html
    sha256: bc5bf676da331b5dee5ad7ee91e98f2f755a8dd359e18dfc27ef5b3c9b8948a1
    role: context
  - path: pages/traits/morphology/cell_length_very_small.html
    sha256: 157d4c01961110e0c6a569af6a6a5a86fbe4004e97c52dbfb9b47c864e8e00bf
    role: context
  - path: pages/traits/morphology/cell_shape.html
    sha256: c1d18b40823817650b67693b33226127dc704efd168f3eec279e1a72573a0bee
    role: context
  - path: pages/traits/morphology/cell_width.html
    sha256: de5e970ba67a8aef177a57a030915d37475958dd3dbd6343598056df89004335
    role: context
  - path: pages/traits/morphology/cell_width_large.html
    sha256: b764414737e7ed0ee7a46852cd65f791fc322ba2c8342708e8db1b9539d62ec0
    role: context
  - path: pages/traits/morphology/cell_width_medium.html
    sha256: 6805568431b615519bc381e69d7963647d9309d52f32bb77ebdae4ec670d4808
    role: context
  - path: pages/traits/morphology/cell_width_small.html
    sha256: 5b8aac580244edf4378f41607dbff0ee48f3a40b463babe847f1770073e8e2dd
    role: context
  - path: pages/traits/morphology/cell_width_very_small.html
    sha256: ddbb42401f3469209ce7607f213bff90a9d79082f1b8bc52a2199c62e83f1979
    role: context
  - path: pages/traits/morphology/coccobacillus_shaped.html
    sha256: b3bcef4574a74e9bda5ef07e273f0084b08a3da0950041dd0cee3adb698eacf7
    role: context
  - path: pages/traits/morphology/coccus_shaped.html
    sha256: 3e03112ccd37e1fba1945cebd94c5a6adebcfe0038d213d1c15ae84d5951b65a
    role: context
  - path: pages/traits/morphology/coenobium_formation.html
    sha256: bb061839a8be8c9b823f979373dbc1b6635599eb4d13ec823299295e5ec79469
    role: context
  - path: pages/traits/morphology/cream_pigmented.html
    sha256: bf7a2067d7695be75d8b37cc15cc1cbcc56c0cadeef8749f7d198d551317839b
    role: context
  - path: pages/traits/morphology/crescent_shaped.html
    sha256: 3674f251127fad74fc828b05b3e8c570e6386b4a680c04833ea1f200e02164d3
    role: context
  - path: pages/traits/morphology/curved_shaped.html
    sha256: a2c642dc2fb5e26a10139c944f9503ed36dda8347ed2b2b829402bf432b8e0a4
    role: context
  - path: pages/traits/morphology/cyanobacterial_multiseriate_trichome_formation.html
    sha256: 2bc8e0d0182084098f4c3c98c2cffd221e00347e2773a0acc11aab40e14b922c
    role: context
  - path: pages/traits/morphology/cyanophycin_granule.html
    sha256: b1aad062f137eecc25a598e946cc44fda1ebb90b60efa3ea6dc797339ec91110
    role: context
  - path: pages/traits/morphology/diplococcus_shaped.html
    sha256: 0ec7402c3d49a2f9548fe3ca8ce286145a74152521af8f74ab16f00bd13a34de
    role: context
  - path: pages/traits/morphology/disc_shaped.html
    sha256: fe305ffb7f62e7425fe45505b1633861311b72943316fa71309eaf127f79106f
    role: context
  - path: pages/traits/morphology/dumbbell_shaped.html
    sha256: a16e2fb328d9bb1a452ab5db06ec966af9539e71d411d0d477f500472f40c246
    role: context
  - path: pages/traits/morphology/ellipsoidal.html
    sha256: c30cd8e26657f43d460a315f5f53225cd8b187c22dcf7a87c4bee6362d500f5e
    role: context
  - path: pages/traits/morphology/expansion_driven_sliding_motility.html
    sha256: c3095598b9d920b33a3c7fe63014d2eec921be09a9344760f0593e05cfc749a5
    role: context
  - path: pages/traits/morphology/false_branching.html
    sha256: b620dfe224874f523ea6b91fb08b4cbe264602fa7938a0e7c30f947618cc6cb3
    role: context
  - path: pages/traits/morphology/ferrosome.html
    sha256: a57fb84a0b27ed6164bc6f27d2cbbeb9fc1c8bc529c02e8f0c3250d1bc72398c
    role: context
  - path: pages/traits/morphology/filament_shaped.html
    sha256: 28cd91f36ce7626f36b85e112deff6a8630173af408158bf391e8f9875144cf2
    role: context
  - path: pages/traits/morphology/flagellar_arrangement.html
    sha256: 6d69e6886e42652a0fa6ea518924ab1ed88ea23e6612d6410e6f0b7af1abfcca
    role: context
  - path: pages/traits/morphology/flagellated.html
    sha256: d4342b745c47d1650a51ff2047bfa55be7767fce4b8a6a59ca5ca516904f4f4b
    role: context
  - path: pages/traits/morphology/flask_shaped.html
    sha256: 84f07136343cde41bd7d2b59dc4046188418afd0040212f716d77d83bd8e5ec3
    role: context
  - path: pages/traits/morphology/fungal_adhesive_column_trap_formation.html
    sha256: d166939c11be20b5040256443f07dfa556e74cbcb192c780b8103416f2134af6
    role: context
  - path: pages/traits/morphology/fungal_adhesive_knob_trap_formation.html
    sha256: 8fd25faa6fd9e5dffaad61c939655b8bebaa217f7f573637fe176b73dac9fb99
    role: context
  - path: pages/traits/morphology/fungal_adhesive_net_trap_formation.html
    sha256: 0e49feab68c499e80778732c08b703b9b6c1594df268d5b128f05b40db5579b6
    role: context
  - path: pages/traits/morphology/fungal_appressorium_formation.html
    sha256: 3c7230d5685d89946271315e93c367c6f36c940ae3d9c44194613d29df6b017b
    role: context
  - path: pages/traits/morphology/fungal_arbuscule_formation.html
    sha256: ace83eb8746cb95d77aeb6d5c754bf2ffaf4b9d6d0daa8b897abd3e0a35195bf
    role: context
  - path: pages/traits/morphology/fungal_auxiliary_cell_formation.html
    sha256: d94fcb53464a8d87751f055b9efe89b7538ede05d0dfb048c51784993249eb00
    role: context
  - path: pages/traits/morphology/fungal_branched_absorbing_structure_formation.html
    sha256: 7932fe204597f18641e2b4a59366e5a017049aa4eef08c91efd17ac8e7417a5b
    role: context
  - path: pages/traits/morphology/fungal_chlamydospore_formation.html
    sha256: 2f00ebb8abbccf5b9bec0020c82b2306207325f822afeac020e29161ec869faa
    role: context
  - path: pages/traits/morphology/fungal_conidiation.html
    sha256: 7cbdc4d5929d9fbd29773f786fb28ff22e86e02a1e430f07718371ad571eb378
    role: context
  - path: pages/traits/morphology/fungal_constricting_ring_formation.html
    sha256: bc248d56c6a05d82158236ce1810ac14ff1f9f8522386fab6131f076329ce004
    role: context
  - path: pages/traits/morphology/fungal_hartig_net_formation.html
    sha256: 23554d67fb5bbd36bca333aaedc0d107611b32fc68830858567c005f71f8cb40
    role: context
  - path: pages/traits/morphology/fungal_internal_mycorrhizal_vesicle_formation.html
    sha256: 2c245fbbcef5ea87617b4c67ba5101732afd92ae4260955953d1d16fc8e08299
    role: context
  - path: pages/traits/morphology/fungal_mycelial_cord_formation.html
    sha256: 378b5fc51f94eeef66171703a6d2ba1e9056bfbc7a6a728cb158a074f3873a74
    role: context
  - path: pages/traits/morphology/fungal_nonconstricting_ring_trap_formation.html
    sha256: 0183b6f8fae3a94b449c8f65b78cb0b8e06dd56e8f1bdfacce910606051ef403
    role: context
  - path: pages/traits/morphology/fungal_peloton_formation.html
    sha256: f7e7c18085be6a299002cd472dc465b126234c4ea015d61710b375cadcf9a2f4
    role: context
  - path: pages/traits/morphology/fungal_rhizomorph_formation.html
    sha256: fee5125d0857e969ae9f7aecb07a21e69deacf781274b0e41b50743b32301ee2
    role: context
  - path: pages/traits/morphology/fungal_root_mantle_formation.html
    sha256: 305d7730eedc67f52321536d9ccbe90b61a91c5b744ae319df694b3f159aa2ad
    role: context
  - path: pages/traits/morphology/fungal_sclerotium_formation.html
    sha256: f9920aae1a64dae90099ba3130b53436cccd38c25ee072a1b926bf1049cd3208
    role: context
  - path: pages/traits/morphology/fusiform_shaped.html
    sha256: 68ac5dfbcee144559da1173628938d99ebc57d873dc0cdc0be571eebc7c074a5
    role: context
  - path: pages/traits/morphology/gas_vesicle.html
    sha256: ec93b6b5d80edd225a488b14acc7964f8f1881819517659dae882dcc31a9c9a7
    role: context
  - path: pages/traits/morphology/gliding.html
    sha256: bf78ddfddd5021276a167c36f419e737ce67aaabcdab0443d34b17b9cd3c1301
    role: context
  - path: pages/traits/morphology/gram_negative.html
    sha256: cf7b027cbdd26f1d95e27049cad2db1fdc09e8ae304e6887f7b41bb19531bbd6
    role: context
  - path: pages/traits/morphology/gram_positive.html
    sha256: e9a74e94a5913cec20f72a89c5825ebf4daa0619c0959a7805ba588497a7207d
    role: context
  - path: pages/traits/morphology/gram_stain.html
    sha256: 7b435e6544acb4c2e199664ab454d043eecba881dc9544f2a50a73b383223539
    role: context
  - path: pages/traits/morphology/gram_variable.html
    sha256: f142d0ed9ce4ff906d94567be22814c5a0a1db2d4eedc7b740d498742eb38280
    role: context
  - path: pages/traits/morphology/green_pigmented.html
    sha256: a5169cdc51fe4464302b52be4c02b9d924cda4827e4c69d535245cb67ad2481f
    role: context
  - path: pages/traits/morphology/helical_shaped.html
    sha256: 9b68bdc7cf4c7871f54ceefa12675784286eda957541d0baec160df8f7f4dff4
    role: context
  - path: pages/traits/morphology/heterocyst.html
    sha256: 5fb38481f7ff142dfd3e41f65c22e4479af74c7926a242a87f2ebf5abc212193
    role: context
  - path: pages/traits/morphology/holdfast.html
    sha256: d355453294a12f9541da885b224574e70cb4943f89e63ca7156685a844578fdf
    role: context
  - path: pages/traits/morphology/hormogonium_formation.html
    sha256: d4a775a8c2cf52939d2f6067a92b6d5e45d1e0a7480778734ac1e219f1849579
    role: context
  - path: pages/traits/morphology/intracellular_inclusion.html
    sha256: 35ff0f820c3cd211d43c472b460d08bba9450529b222104cfc16ae5ba703467c
    role: context
  - path: pages/traits/morphology/irregular_shaped.html
    sha256: b759469942830ffe24524bf182e8a73a643586425f8f81741b9aa1dcf8b103e1
    role: context
  - path: pages/traits/morphology/lateral_flagellation.html
    sha256: bc09a1b328b4824d5d02b4b32245cd5447f8e205642aa94395c6466ebbffe2ee
    role: context
  - path: pages/traits/morphology/lophotrichous.html
    sha256: 438d2c3caf2fb4dfcb7e12dc5293ef3c17868f333641c34ee373456d6786d0f3
    role: context
  - path: pages/traits/morphology/magnetosome.html
    sha256: 667f06190b4b64102c86b0dcf3c39aae013c31798d32a91176e666bf7c811465
    role: context
  - path: pages/traits/morphology/microbial_haustorium_formation.html
    sha256: 0a7b6535082a85e723db8662a58f921092803a2386bbcdc80de0251db77dd2ef
    role: context
  - path: pages/traits/morphology/monotrichous.html
    sha256: 5253c9249aadedfa6da2e1db17a3eab8b567c39328cb7fe18dd16f748e56ecc4
    role: context
  - path: pages/traits/morphology/motile.html
    sha256: ebbc11a338487b3449b2c1d23b36eb3aaef2982dd0470168bf72fc53f9caf337
    role: context
  - path: pages/traits/morphology/motility.html
    sha256: 38ea63e55ff0ba9e8a2447612a6756bf9f47287fd5d0e259bfaa2e0fc7123b58
    role: context
  - path: pages/traits/morphology/mycelial_growth.html
    sha256: 116ba8261c8af02df3e4186135b6838bea038442b4c9dd819c776c5ae00096d7
    role: context
  - path: pages/traits/morphology/necridium_formation.html
    sha256: 5eb345db9270d6d94c0110e5948060da3bb70c7056353f60ed12a58f9de3444a
    role: context
  - path: pages/traits/morphology/non_motile.html
    sha256: f00d3e2b5c979bb02f0c40f0dcd12da581706ba29d467a6040adb9c7f58f89ad
    role: context
  - path: pages/traits/morphology/non_spore_forming.html
    sha256: de85913df7e75cddb9860bf48804a211ce93f96ff1a1f34eaa3eaf880bcd92f1
    role: context
  - path: pages/traits/morphology/orange_pigmented.html
    sha256: 0d558a2a180c493f88710d90c9c110332d3ce1dfaf403382fc68489d7aef848e
    role: context
  - path: pages/traits/morphology/oval_shaped.html
    sha256: a7afbb690b221046105f8f96d9494ae80ac06420f07e9b59318a107da9a5dd83
    role: context
  - path: pages/traits/morphology/ovoid_shaped.html
    sha256: 58993875f7520b0f824b263546c80aae99b9fc17519e19ffdb6d41573e4cad74
    role: context
  - path: pages/traits/morphology/palmelloid_formation.html
    sha256: f9b95e5c56be3bcb2529be464aaa4daa0d92c2542e6664a8ab871a47394e2f59
    role: context
  - path: pages/traits/morphology/peritrichous.html
    sha256: a3eaf9598bc027a65c2876b63d46784b7a10df70e50cce1c47b8cc6d8cfd435a
    role: context
  - path: pages/traits/morphology/pigmentation.html
    sha256: 3a43b2775a5bb17123266f514f1424dbe208676aa703e9adf9178b38c2e67920
    role: context
  - path: pages/traits/morphology/pink_pigmented.html
    sha256: 15dbcc862dd4bccfef96f48fa0dec8c026e02b6c49a36350219c01d33d7aed84
    role: context
  - path: pages/traits/morphology/pleomorphic_shaped.html
    sha256: c4c063bb6bb50621a21cd0f6de29171c096ecea1a765e476707cb09d6288f532
    role: context
  - path: pages/traits/morphology/polar_flagellation.html
    sha256: 9b35b52e0c6cb1216fab6c7818439f4c747dc4781596b94b9178899d713b28f4
    role: context
  - path: pages/traits/morphology/polyhydroxyalkanoate_granule.html
    sha256: d4e093790eec3462e91d69a55baaa8094219da4a75dc6c195d5ef1cf79400ec8
    role: context
  - path: pages/traits/morphology/polyphosphate_granule.html
    sha256: c9a8adca21dd637b3649f69c03ff84e779f256a67e9c82c7a62773a089a85cf4
    role: context
  - path: pages/traits/morphology/polytrichous_flagellation.html
    sha256: ebcae3e08d333373b2a889d49b3da92581c9b46b0b4ec50b26b0f3a70384b0c9
    role: context
  - path: pages/traits/morphology/prosthecate.html
    sha256: 2172980a65d81610e676337e0b29f3193e56700f4e38c81fbfb29c53fe2a78dc
    role: context
  - path: pages/traits/morphology/pseudohyphal_growth.html
    sha256: eedd0d276c87e4f80a49e1f429768d43d440ca7c4896ea0f1d625be652302d46
    role: context
  - path: pages/traits/morphology/red_pigmented.html
    sha256: d5926fe7f5da0ab0ecfcb6a7d878504c2f7551d8d11bc822b76029ab2f873cbf
    role: context
  - path: pages/traits/morphology/ring_shaped.html
    sha256: 3c4410d06c85b27f68f50badbaeaf9dee70dce039830756221d6faf330d4552e
    role: context
  - path: pages/traits/morphology/rod_shaped.html
    sha256: f9d168f621aefc9952314d8c1cff2b4824b71aa7065873901bc527b49a60dc78
    role: context
  - path: pages/traits/morphology/rosette_cell_arrangement.html
    sha256: 4f8bba58c4d88e1c9d4a7f8f1cc173fcdbcebe35e2d9fcab426b11222c030fc8
    role: context
  - path: pages/traits/morphology/s_layer.html
    sha256: 510a25ffbab84c115afaf8fd8027975a98cb1aa6425aa27398e4af1947710171
    role: context
  - path: pages/traits/morphology/sarcina_arrangement.html
    sha256: e83ccdb15e8b4dfbc7e8f8635abd0126b736c53deb328613b5e74c593e3ce6f9
    role: context
  - path: pages/traits/morphology/sphere_shaped.html
    sha256: 8a80b1c154aeb8d297615c0e5906d676a16190399bb27d4369ff9fafc865d2bf
    role: context
  - path: pages/traits/morphology/spindle_shaped.html
    sha256: 98c7f0e251d4c3817a39aa0d234c1b7ddb769b1a8d6351905f884e5e15e25789
    role: context
  - path: pages/traits/morphology/spiral_shaped.html
    sha256: 6c337caa721b624818410779ad8d30e798291d0b2449eb11cb7146137dbf6dde
    role: context
  - path: pages/traits/morphology/spirochete_shaped.html
    sha256: d3eb3a6213a15759ace96d7cf708a1346cf50c4d50a373ff8e64d2ddd24c22d1
    role: context
  - path: pages/traits/morphology/spore_forming.html
    sha256: 99a8ef21aeef56e471c4d6cdb2fe0d7942249628fdb32a9e0bc3b82f80a6aa8f
    role: context
  - path: pages/traits/morphology/spore_shaped.html
    sha256: 97e3d4164964e0b9cc86d67bd613bfea5d9da1643ac8d750909561a8b8673a2c
    role: context
  - path: pages/traits/morphology/sporulation.html
    sha256: d7feec8c8e6a1b45818e6ddacd99004087e3a27900dd1af132f6eb5cd71400e6
    role: context
  - path: pages/traits/morphology/square_shaped.html
    sha256: e625f1ac982e564d591d0d058462a9bd551661649faad341894b03cf1619b348
    role: context
  - path: pages/traits/morphology/staphylococcus_arrangement.html
    sha256: 7c6e5285fbb46a9c776430ba49f6a4bf6d8ed26f9a09b381e437b8d57e7f1edf
    role: context
  - path: pages/traits/morphology/star_shaped.html
    sha256: b1769e1050220142a83a988c5aac156ee91574ab672a143c0f8085171418c058
    role: context
  - path: pages/traits/morphology/streptococcus_arrangement.html
    sha256: 7682182cbc335e655f9d0fb341f4dbeb4f05b79cc14a12d3ee7f2f7a6ddbc1d5
    role: context
  - path: pages/traits/morphology/subpolar_flagellation.html
    sha256: 32da0c34650c27a7322b446052684a9b47728fa25db1831156fde2d9fd87f37a
    role: context
  - path: pages/traits/morphology/sulfur_globule.html
    sha256: 0016f8440ec4aae41bf9dc1b22059308b3cb97fce235fa481de1fc6f2fde0987
    role: context
  - path: pages/traits/morphology/swarming_motility.html
    sha256: 10e36dce045a805a684b4db095a3be683f225bde7f16820ee075c70ad2f70e98
    role: context
  - path: pages/traits/morphology/swimming_motility.html
    sha256: 334a1832b9d2355feeb6c3da442426830d39f866fa531976920d5233c78f2f21
    role: context
  - path: pages/traits/morphology/synnema_formation.html
    sha256: 606dc5dc22fd6af4d2156491e7e43998e20a0f8f4bf97173c7c1d7f97c32fbbb
    role: context
  - path: pages/traits/morphology/tailed_shaped.html
    sha256: 416a0a04c154793fddfd5b9399c9a97daefdf2911c0c16c8f8ca7c11166960c1
    role: context
  - path: pages/traits/morphology/tetrad_arrangement.html
    sha256: 91a9f7aab2e1fb94eb5f5b2d1f51b45ec1f00184cdd23f592844a54ab91ad49f
    role: context
  - path: pages/traits/morphology/triangular_shaped.html
    sha256: c03aa6180823ff92c33d5b75e7ab708df3c7b8530b335ae3f1cc462dfa5439e2
    role: context
  - path: pages/traits/morphology/twitching_motility.html
    sha256: 82377059b9ed0d813313323e0765d1d8f279adcc5e92a700d7159c30e1bcd498
    role: context
  - path: pages/traits/morphology/type_iv_pilus.html
    sha256: e435951a2658c799d0b6928a7f8d8f2bdfebb31b0b73f528cae9890c044d1cc7
    role: context
  - path: pages/traits/morphology/vibrio_shaped.html
    sha256: bbf502bbac62e9fb164e7ba15495f1a3ed33f861d9257ee7d9593a811188c322
    role: context
  - path: pages/traits/morphology/white_pigmented.html
    sha256: fc5cd2aa04aae7d93fffc997725a22834144d35b6bba0d888eb1c33065129aef
    role: context
  - path: pages/traits/morphology/yellow_pigmented.html
    sha256: 2849b40f19154485fe0730ac705e855e84c3349aedd1388401535c2dfa6c73fd
    role: context
  - path: pages/traits/observation/growth_nacl_observation.html
    sha256: 9ce4b2e66a73c3866dfcaa1b457f59c8b48ef6500cfab0d28c7d8469ebebe34f
    role: context
  - path: pages/traits/observation/growth_oxygen_observation.html
    sha256: 4496aad7201aaaacb49715412a87c81f72ff975da6c0c58e6a0ba1dc593953e3
    role: context
  - path: pages/traits/observation/growth_ph_observation.html
    sha256: 96c79a61288787f8db20321480bc4b23f2d3265da5c131f6556905cab0476a2d
    role: context
  - path: pages/traits/observation/growth_temperature_observation.html
    sha256: 9c87a952327a32a2678a691154c2678ae089d3fadebb5e033c6cd50dcae9f1ab
    role: context
  - path: pages/traits/observation/nacl_delta_observation.html
    sha256: 3001a3010019dd65cfbcdb6643fc0f9753ebca9f2024863279e346711d141919
    role: context
  - path: pages/traits/observation/nacl_observation.html
    sha256: aaebef55eabef381752f982d3909c2afc8246fa74a349aec1fa18ba5989895b9
    role: context
  - path: pages/traits/observation/nacl_range_observation.html
    sha256: 07d98326af6193909392b2106f9be6296d452eb3314bd470ba9cfd8247dc1762
    role: context
  - path: pages/traits/observation/optimum_nacl_observation.html
    sha256: 281535b73a9506605793381fc6a4090250fb19e74406084094579ddde31c695b
    role: context
  - path: pages/traits/observation/optimum_oxygen_observation.html
    sha256: c0eaa937cb9ece7f57ff063b8255569308bdd001ab1c1d64f75eaf1c209c7e59
    role: context
  - path: pages/traits/observation/optimum_ph_observation.html
    sha256: ed6794037a86123ccae61a5d0c75a423627db7281cb9eb97d9a6c689ff951768
    role: context
  - path: pages/traits/observation/optimum_temperature_observation.html
    sha256: 6bc4d08e802964d14f0c8a569960061b04d8f4650ef3c17733e1a0fb2af9754d
    role: context
  - path: pages/traits/observation/oxygen_delta_observation.html
    sha256: 6e5e18cdba0da98d91b7a830a10be906d9ab8723c52f45ef81c58b2147dd022e
    role: context
  - path: pages/traits/observation/oxygen_observation.html
    sha256: 6a0b46d50bb779f801178c3d101d50a0edb381b0391dc606086486de23f2fdbc
    role: context
  - path: pages/traits/observation/oxygen_range_observation.html
    sha256: 1601d21816da5860af7b76cee91e8aeeaece6d2efc04c732aa92578371639f76
    role: context
  - path: pages/traits/observation/ph_delta_observation.html
    sha256: a2bf0812538a0d6c6ccb8663c392667f5ace9060e9b63724e8038852cc40fd6f
    role: context
  - path: pages/traits/observation/ph_observation.html
    sha256: d4db3174e77d4b65bcc1472e8b24c6def436d117488099c84b07ba46aa8a11bd
    role: context
  - path: pages/traits/observation/ph_range_observation.html
    sha256: 23f0eebd552e75ec2242f5f4f5ea2b4daae36a503039734248af51ccdc0ca76a
    role: context
  - path: pages/traits/observation/temperature_delta_observation.html
    sha256: 91fab43f9d49e9b35eb84fb0031333e19e7eb7aa0aec1d6b640b7bae93a1976c
    role: context
  - path: pages/traits/observation/temperature_observation.html
    sha256: 3e42fb83cd9bf30e60b04db613dfcc2cfd16ed59d5172922ef9e83776510d83d
    role: context
  - path: pages/traits/observation/temperature_range_observation.html
    sha256: c07929ea4c81ce853d2821e113610255aaf6e2aa670f769f7ddbf8fd7990cb83
    role: context
  - path: pages/traits/other/catalase_negative.html
    sha256: 642ac3881d3803c0999432cccfd5cac8a93b608f7abd030a45c86394a78a0807
    role: context
  - path: pages/traits/other/catalase_test.html
    sha256: 96220ba31e2012620b8e65c091de8afde202b70f6dedd7dcc630e23e4179ad4e
    role: context
  - path: pages/traits/other/circular_colony.html
    sha256: a636195344e2e804d70f8e7f7424b9ec0e8594ef1f898dbb8619043aea326908
    role: context
  - path: pages/traits/other/coagulase_negative.html
    sha256: 0d80a4beb0ce8a9e7a02391e2c8aaa4fbce163fa408c99a72f07994d710dba28
    role: context
  - path: pages/traits/other/coagulase_positive.html
    sha256: b7792a7dfb15206a83874510eea1645d99dd9baed83993fce3a2daf08334794b
    role: context
  - path: pages/traits/other/colony_morphology.html
    sha256: e0cc6d2588095171b12eacf3e79442dc4b585560fde778178a04c18425d97e24
    role: context
  - path: pages/traits/other/colony_shape.html
    sha256: 3320f554f8e924d27d32a91ea0f9b65053a1536263abda419655c4e767c4e543
    role: context
  - path: pages/traits/other/epibiont_phenotype.html
    sha256: f02bd1af95a0b2131de3cda526329cf529ba734f96e5915792266bc6c30aedf4
    role: context
  - path: pages/traits/other/filamentous_colony.html
    sha256: e197ee4aa690737869df0800f1d168f16f1fb87190d5bb7519c1de6ffd2bfd48
    role: context
  - path: pages/traits/other/fried_egg_shaped_colony.html
    sha256: 7eb4b3beece9d51fd4ba31b49b53b4e0cedb9b958670b7ece88c52e0f05f2cd6
    role: context
  - path: pages/traits/other/generalist.html
    sha256: ad1a33cea88b35b487f4320ae526dfc24555877c93869d66fe1379c7651bdf0f
    role: context
  - path: pages/traits/other/hemolysis.html
    sha256: afa76449a7cac58d038ea5fbc489a349dcd1645a1dbf5cd8e75f2f7d1abf610a
    role: context
  - path: pages/traits/other/hemolytic.html
    sha256: 8ddbf932485ab760952bac0cbb9187d57e425f5c2d75750222e11f5635967678
    role: context
  - path: pages/traits/other/indole_test.html
    sha256: 57edbfc668650982d37bfd6f2006e13ca7a9712268b70320b8e24642ec663eb3
    role: context
  - path: pages/traits/other/indole_test_negative.html
    sha256: 7206115d1968fdca60615078f78a3f21f83c4cd43d76c06ea761a210812e3141
    role: context
  - path: pages/traits/other/indole_test_positive.html
    sha256: 34b7b2ddd1bb378a5eb9a3aa2852c9bc424616ace813c59afbd947156eca2405
    role: context
  - path: pages/traits/other/irregular_colony.html
    sha256: f655c4268ef2c62f1e80dd65d398bbeb8c0399c21d6e024e5f9fae0a384d7a7c
    role: context
  - path: pages/traits/other/methyl_red_test.html
    sha256: e24fd6eb58f52a16f936d62299c411915965f3efa9267fe9a52ab2b9dcbc1b95
    role: context
  - path: pages/traits/other/methyl_red_test_negative.html
    sha256: 93cdb6683f9f1fa37a9cb086b93c130cbcdb4f717b9d0f750ddaa1d7b35d5db2
    role: context
  - path: pages/traits/other/methyl_red_test_positive.html
    sha256: cb0a788adb8710cabc205095d651ec545b28c229dbc1f0b3a9a6db1d319b4f02
    role: context
  - path: pages/traits/other/non_hemolytic.html
    sha256: 80d314829d53cbd7a2be20b148a05e8fab3bbfd29fa9b5f777c6df1ebf46d4c3
    role: context
  - path: pages/traits/other/osmotic_tolerance.html
    sha256: 34155f92e97f2e905fadae68267965a6f60add464ec57f7f3bf16c01516c947f
    role: context
  - path: pages/traits/other/oxidase_negative.html
    sha256: 8864d461c15614b253c3f7abdb471d67d95b923a29aa1372614da8445d9b29fe
    role: context
  - path: pages/traits/other/oxidase_test.html
    sha256: a29bc569502b2abff427c903625393d4358c972e727bec0ad4b1ed5ffe4ce303
    role: context
  - path: pages/traits/other/punctiform_colony.html
    sha256: 444d7029f012db4603e174c38d4e23725a5b4e52c26894d1f9bd30a7e2493b5f
    role: context
  - path: pages/traits/other/rhizoid_colony.html
    sha256: 4a509fbf09fe67e2393677e0dee9920846dedd287569e12e3e43970d54781b2f
    role: context
  - path: pages/traits/other/specialist.html
    sha256: 19667e98a4d8a692b9e6e2f2e12d7f80780214956d4e483c3805afe62c087a4a
    role: context
  - path: pages/traits/other/urease_negative.html
    sha256: f33661f3e42f9b810bccc45667541728cbc2e02e97279ebd08250fbc848bb6bf
    role: context
  - path: pages/traits/other/urease_test.html
    sha256: 947f3a594d4ec33bbf6216d228b8e57949e6513c0650339c72308c7baabc99ec
    role: context
  - path: pages/traits/other/voges_proskauer_test.html
    sha256: a74af2c0c5107bcaf3be3a10ad23805ccdf17dd56cc56515c26db7516e2b33b3
    role: context
  - path: pages/traits/other/voges_proskauer_test_negative.html
    sha256: 2191b201721f698eb6e594be33df056a9119547b088435cc4cb80ce520cd274f
    role: context
  - path: pages/traits/other/voges_proskauer_test_positive.html
    sha256: a2577c58cf64e56468fe69444cdc9bcd63775205107a52cbba262d7bb80d8b42
    role: context
  - path: pages/traits/physiology/acid_phosphatase_activity.html
    sha256: 98fe3ba213c6fecc10a0dd78540a111b0e146f4bcd9881c667be67a49d761793
    role: context
  - path: pages/traits/physiology/aerobic_anoxygenic_phototrophy.html
    sha256: 6fa389063cf0fd72f917a8553459cc83f0d48e464e7c67214d4e64167939b997
    role: context
  - path: pages/traits/physiology/aerobic_overflow_metabolism.html
    sha256: f642c5780592c5fb947e38177941e9f6aaf0bedb3f72df896127c8afd6d09f61
    role: context
  - path: pages/traits/physiology/aerotaxis.html
    sha256: 303d6ab009f339162eb5d1eeb217c43402d501aa846e8a11a063e809c2c9d35e
    role: context
  - path: pages/traits/physiology/aerotropism.html
    sha256: 4081abfbe78c531c6320a31bfb4dc5fa8b5812fa44eef4c606eb140681ce1b0d
    role: context
  - path: pages/traits/physiology/aggrephagy.html
    sha256: 2583d0b82fc70982cba9ee76f583071c73e987bf0334f9c1234b4dd31730ea0a
    role: context
  - path: pages/traits/physiology/alanine_arylamidase_activity.html
    sha256: ddeafbedfc9245db3fb77d1ff7678001814b2683244ecc947655c340a9c61b54
    role: context
  - path: pages/traits/physiology/alkaline_phosphatase_activity.html
    sha256: fb7dc2e5eb5d521867210e16fa518851ef18c45da17dee2ee265cce23b1c5684
    role: context
  - path: pages/traits/physiology/alpha_chymotrypsin_activity.html
    sha256: 1ef1f182e610f0008c866e8d03eb4c815c7827f81e8e3c8b4baa0bfcef1f198a
    role: context
  - path: pages/traits/physiology/alpha_fucosidase_activity.html
    sha256: 959baa7fd1b1cbeeda72bb4117a5d8d485b389c6ab004fed8277fc0ce09a0025
    role: context
  - path: pages/traits/physiology/alpha_galactosidase_activity.html
    sha256: c8c20725679c017133afabbac8d2e7ded92b39301ceabd7db4b3ea3598f3d834
    role: context
  - path: pages/traits/physiology/alpha_glucosidase_activity.html
    sha256: f7d9ffb24934d9e25bb5b3c323e84089961680e208f1625ce401007817e075b9
    role: context
  - path: pages/traits/physiology/alpha_mannosidase_activity.html
    sha256: 61e23c9b0fa41bbd34fcbae9bb70838994720a12901bc41deec23fca60c9a55b
    role: context
  - path: pages/traits/physiology/amylase_activity.html
    sha256: 9a54457b8061f8731eadb085d3e52d263884a73d9d0750812aaa9904e3d6a797
    role: context
  - path: pages/traits/physiology/anisogamy.html
    sha256: 0752a8ae81b4725f7bd7837dd2356e0bdb51ed03a5b3ef4e9b4034a5f9f606a0
    role: context
  - path: pages/traits/physiology/antibiotic_resistance.html
    sha256: f9a5d344ab3e3a0680727f057d5213624d654c79fb08512a6fce8dad705e2062
    role: context
  - path: pages/traits/physiology/arginine_arylamidase_activity.html
    sha256: fc9c455b535c3b5307c25e2c924d27d4daffc03ecfeddf4d7f5d7ff56fa893c6
    role: context
  - path: pages/traits/physiology/arginine_dihydrolase_activity.html
    sha256: 1b7747296058f6a07efb328a9f212cf6891f1a2dfe30cd2c89ba63b7140ff93b
    role: context
  - path: pages/traits/physiology/autogamy.html
    sha256: a2800f8f8179ed12f5619e202644cb2d53af719ce64dddbb4da580a7bda5f5a6
    role: context
  - path: pages/traits/physiology/automixis.html
    sha256: 3da7742a3fe43dc54024ff4350db5c9e28a5e1f2c74faf48a0d9356ef970a57d
    role: context
  - path: pages/traits/physiology/autophagic_glycogen_degradation.html
    sha256: d1e7f6669886fd89800476a97e6212242127a3bade8b116a414484ac598067d5
    role: context
  - path: pages/traits/physiology/autophagy.html
    sha256: 39e8e78210ab9b7fc061c79d16ccfce0019c0d04f0da111f24baba01986f957b
    role: context
  - path: pages/traits/physiology/autotrophic.html
    sha256: 13d67afa41e08124848bb4453202853e8545089b77827ea25ef7b7f2680e0b61
    role: context
  - path: pages/traits/physiology/bacteriocin_production.html
    sha256: 08241f70cb37a22d6e12b96ffb7042aff2d1e9bacdeafa85f5c58263f50ae300
    role: context
  - path: pages/traits/physiology/ballistospore_discharge.html
    sha256: ce40a498967bcd2ff9f503f253670e0629f56c324d4ee2187369df2a4f81f52f
    role: context
  - path: pages/traits/physiology/beta_galactosidase_activity.html
    sha256: 51a4227929c2df050c20ddf3f153390dd52cf672ec42b22484b2223833811118
    role: context
  - path: pages/traits/physiology/beta_glucosidase_activity.html
    sha256: 1de4c9b458676750e1a7cce7f0f9381a343ec209fb51467f3016adbde361a901
    role: context
  - path: pages/traits/physiology/beta_glucuronidase_activity.html
    sha256: 21a2d28ae05074fed59b071958c43fc5ff1b608054719db6a3a9d94edca11f1a
    role: context
  - path: pages/traits/physiology/beta_n_acetylhexosaminidase_activity.html
    sha256: 894b1e4db262a05d4c0179eb16fe5495810552ca5f71e7b682c4007434791f67
    role: context
  - path: pages/traits/physiology/bioluminescence.html
    sha256: bf5bce9db4541c3f55502582bdf742e3d3dcc81ce450bf75b812459a7b0502c7
    role: context
  - path: pages/traits/physiology/biomineralization.html
    sha256: ddb5eb471b67e69bb812149325ca41ae789387c72e19b64d14e1ba382c6898ea
    role: context
  - path: pages/traits/physiology/bipolar_mating_system.html
    sha256: f2e2239c02cfe75d5a51f5115b797643c9c74cbab49e6165bf0d83314b544633
    role: context
  - path: pages/traits/physiology/carbon_source_memory.html
    sha256: a5ea12ed406b8c8cfa1b3804de9e2cf30a22e3c5a5a486b4a9d9fcbeab61ec9d
    role: context
  - path: pages/traits/physiology/carboxydotrophic.html
    sha256: 74f5f5dce0dced9c832d3a2694a82baded5f7d4cbcc9ef5a3e23c2444da57577
    role: context
  - path: pages/traits/physiology/carboxylesterase_activity.html
    sha256: 037c8959aa6cc583b124edb79833ee2c4662c7e551a2b6c814f639e4b4dbdfc6
    role: context
  - path: pages/traits/physiology/caseinase_activity.html
    sha256: 779dd8a308bdc57897d72488e852936921427eadef27f4865da4dc7086ac8395
    role: context
  - path: pages/traits/physiology/catalase_activity.html
    sha256: 162ffda75cce927edfc6541da55e3cb7fb87efbafe2c10af4b79e21139764c66
    role: context
  - path: pages/traits/physiology/cellular_buoyancy.html
    sha256: 101c2a5e2a05f596938ff6663e33c3caf3bda26784a47d16f4f097040e68c202
    role: context
  - path: pages/traits/physiology/cellular_rejuvenation.html
    sha256: 6863b4751bc6c28dedd82f1581bd9032cdc7604dc554380bcc36e7cea4f0c3b9
    role: context
  - path: pages/traits/physiology/chemoautolithotrophic.html
    sha256: 50fade4d5127a0e787ca5c0d3399f2e8b9a3eb286d102b66143d5e05455c08bb
    role: context
  - path: pages/traits/physiology/chemoautotrophic.html
    sha256: 6144bcecd98eacf200320570c89379dae1e1545d6d7308137ee34f7803006b5e
    role: context
  - path: pages/traits/physiology/chemoheterotrophic.html
    sha256: 71447ef17bdc98863d4efc53e4b312e7627878e8d621c9fdcc3dbb0ff5a2d81e
    role: context
  - path: pages/traits/physiology/chemokinesis.html
    sha256: 417c1d25ec60e51a29cf8d50b592d2267a2fa724e0ec6280a1724cc43381135c
    role: context
  - path: pages/traits/physiology/chemolithoautotrophic.html
    sha256: 81d0f14bff0cbea113686e4bc8f5c57f8f7bec9d3f07b299bf13d675821e86e0
    role: context
  - path: pages/traits/physiology/chemolithoheterotrophic.html
    sha256: 86ef532e54120071298cba92b86bcdcc0ec61110be3219ddf91c77524815da3a
    role: context
  - path: pages/traits/physiology/chemolithotrophic.html
    sha256: 0b74cf0016dd9cd1ecf4e509114cf30055fcbdcbccbbf36f026fc98794b46a71
    role: context
  - path: pages/traits/physiology/chemoorganoheterotrophic.html
    sha256: adf72065b1fc6e3476a977a2ce6ed31234c23e66c9b2c8d47b41e43b60875687
    role: context
  - path: pages/traits/physiology/chemoorganotrophic.html
    sha256: 18034bbd6876545b87a76c516705754e0476bbf764778fed0c26aaf2199cd5e6
    role: context
  - path: pages/traits/physiology/chemotaxis.html
    sha256: f51a3fef674488f6004166044951bf830b659c273da8bab897a908beb242d2c0
    role: context
  - path: pages/traits/physiology/chemotrophic.html
    sha256: 98496eca1d613602a2db28fc62cf73dae26629c5a50cdd5eb1ddf37041442765
    role: context
  - path: pages/traits/physiology/chemotropism.html
    sha256: 92fac13a0b696fef25bc63240e9f2e3e30abd729b8d1075b7d28229c1e91e0fa
    role: context
  - path: pages/traits/physiology/coagulase_activity.html
    sha256: f894031dd022c6038a09eeb9bb0afd2e7228bc0ba75584499a0f9bcc44556d24
    role: context
  - path: pages/traits/physiology/coccolith_production.html
    sha256: 3df3910352acaf15730f4bdd32d0f54164e451ac0ce2d5179b4915bf48a52e16
    role: context
  - path: pages/traits/physiology/cold_shock_response.html
    sha256: e48ee7076e267b3e1ea8b1a3247fd5ae8598058422232501514846426f044af0
    role: context
  - path: pages/traits/physiology/contact_dependent_outer_membrane_exchange.html
    sha256: 78d7eaedae98c6c427561bed18e2b12b9fddb601cc6e5cf6ed809778e2d8876c
    role: context
  - path: pages/traits/physiology/copiotrophic.html
    sha256: 98165bac46ca7472d2c239c198d60ea1fbe7d96240f1008d311d50f961d6ca35
    role: context
  - path: pages/traits/physiology/cue_triggered_environmental_anticipation.html
    sha256: 3cf237d9e595ebf0609a8ac23ac477b491300b151a718bc60be0db03a02ca478
    role: context
  - path: pages/traits/physiology/cystine_arylamidase_activity.html
    sha256: 232ccdae1eff5def237d2a11538b9711206fd0e4393bf3e284760afc2df5a354
    role: context
  - path: pages/traits/physiology/cytogamy.html
    sha256: fc0d64b0346f458e23e3b8d5fe1152df1a8385e56fd75f5462623a02ee8cc370
    role: context
  - path: pages/traits/physiology/diatom_frustule_production.html
    sha256: 40a1f5f2a558e5a5798fd080d6fefbdfda42df032431488b5fdcf73f4d751391
    role: context
  - path: pages/traits/physiology/diatom_perizonium_production.html
    sha256: 85c75f3dd65b45d94a357357a00ef43157428f5fd4a089e93b0da10011efd245
    role: context
  - path: pages/traits/physiology/diatom_seta_production.html
    sha256: 8437eb45d91c519149af0fb3d62b5738c42fc2f3e9e0699253e07e4590f62fd5
    role: context
  - path: pages/traits/physiology/diauxic_growth.html
    sha256: e548b121495f9caa4780380a13f424bfb18643c92b5faa134511c863daa91604
    role: context
  - path: pages/traits/physiology/diversifying_bet_hedging.html
    sha256: 0c7be81ad5243eabff05d0bdb4b72f0b5da01f5d2b5c02315d6c06ff80eded6c
    role: context
  - path: pages/traits/physiology/dnase_activity.html
    sha256: 319f2028bdc30d25f503ffecb113183e13a45fe8b289a19efdde6dbf9353bb69
    role: context
  - path: pages/traits/physiology/dormancy.html
    sha256: 0409f90584bb03d6b886feeabf4acc9dc033321f26a20a28f671ec7629f3fa23
    role: context
  - path: pages/traits/physiology/durotaxis.html
    sha256: 11ca5f93723203de258518289ceceff81b2bde4da90f5405d97a35bfce85efd1
    role: context
  - path: pages/traits/physiology/endocytosis.html
    sha256: f76c2c386c926223ea567dff2b099fd3d8e0bfa68479e9e91fecc045798540cd
    role: context
  - path: pages/traits/physiology/energy_taxis.html
    sha256: 591292b3e302ed69a1ccb1ddab0b51e9be12b05c072ac47980f84081c2f53948
    role: context
  - path: pages/traits/physiology/er_phagy.html
    sha256: ed12188968ff1f576c9b7ef1edc7923e766116c4b5c9e2908519139496f4d799
    role: context
  - path: pages/traits/physiology/exocytosis.html
    sha256: dd21ca965eb73917b063fc225d7fb9ed7fe8095d03b9a5f0125b4102e7cdd147
    role: context
  - path: pages/traits/physiology/extracellular_membrane_vesicle_production.html
    sha256: 9f49f20782e16a2ccf7193ddca98452c23f2b8621c180d570dff8fda4bb0e94c
    role: context
  - path: pages/traits/physiology/galvanotaxis.html
    sha256: 4995f4dbce6f08d7f590306756ce3f1c8c76719627ce8afbff49a5a2c43736c1
    role: context
  - path: pages/traits/physiology/galvanotropism.html
    sha256: 1393705a2450cca221f55c284e8355f2880a4652a587eb3d6978966b48426873
    role: context
  - path: pages/traits/physiology/gamma_glutamyltransferase_activity.html
    sha256: 3fab21c77b03de139e8dd7c7e4bab4e70de08e7e2df6f3517070013b86e213af
    role: context
  - path: pages/traits/physiology/gelatinase_activity.html
    sha256: 0173e6fedf78af8dc3583ee3f233f64c437158d1fae664279e5a4d4cd9a5b4f9
    role: context
  - path: pages/traits/physiology/glutamyl_glutamic_acid_arylamidase_activity.html
    sha256: 87a81cdd4c3475303bdac567adbbd1cdf47c915e77b3f1959a01cd8fd0bcaf84
    role: context
  - path: pages/traits/physiology/glycine_arylamidase_activity.html
    sha256: 507d1955c201880d08e1f63df64304b2f6f6be8eee7d54f075aed3b253d2f9c1
    role: context
  - path: pages/traits/physiology/gravikinesis.html
    sha256: 9ad26ba9f296e995b8bcb33ba2fb22aea0c4efddb4a77e0a3ca0902ad34cee08
    role: context
  - path: pages/traits/physiology/gravitaxis.html
    sha256: 2e4f7fb74e713ba89fbbe75d53d7cc8e1c1282a72150664bdea7528fbe4f0ac9
    role: context
  - path: pages/traits/physiology/gravitropism.html
    sha256: f46816aaab669ddd88d811626c29c535d796788fa11a662b8164d537b1134666
    role: context
  - path: pages/traits/physiology/gyrotaxis.html
    sha256: 620bfc08cfd0cb0a7367e251690f488f2bb5dcd3daa095dac888edcb042a3277
    role: context
  - path: pages/traits/physiology/haptocyst_discharge.html
    sha256: 3724419e870f584abbbbca6c9b96d6c432f24ff3414d0f4e3e9a2aa58f85bacc
    role: context
  - path: pages/traits/physiology/heat_shock_response.html
    sha256: ca9d1071f95dc0b3a536bd5fb729f7acef4b7623b7922b9aaae34c72d2b6a8bf
    role: context
  - path: pages/traits/physiology/heterokaryon_incompatibility.html
    sha256: 596381d09515d8e3596198ce1401b2d3f75c0735781958f8c30c0f0d0432183d
    role: context
  - path: pages/traits/physiology/heterothallism.html
    sha256: 69f98c92fa6316ccfa41252f865c300b442a3ab5427af99f79982b9838f9885c
    role: context
  - path: pages/traits/physiology/heterotrophic.html
    sha256: 2b377ec0fa20950d160de00d32648329dd0ff7d50f9cd8d4182e1366bdbbc281
    role: context
  - path: pages/traits/physiology/histidine_arylamidase_activity.html
    sha256: 0fc721533aac5116f2f578484630475b660eb3497f8f2ea2299aeb2d453de008
    role: context
  - path: pages/traits/physiology/homeoviscous_adaptation.html
    sha256: b8eca64169fb5075590535550c6101fb50452f7df89a24b91eba324969759cf6
    role: context
  - path: pages/traits/physiology/homothallism.html
    sha256: 989d9bb0f049e2ce73db11f1d671b9aceff1df558b91f63e65d699c8fc69d001
    role: context
  - path: pages/traits/physiology/hydrogenotrophic.html
    sha256: dca8398d7fc0f83c3afb65ce1c91951d237be9d4f53efbb9f8cede264a9a7013
    role: context
  - path: pages/traits/physiology/hyphal_anastomosis.html
    sha256: 147e154cb28f67bfdcf7ef8ad172b687c6be9d6395e20812d52476a2ed9cbc64
    role: context
  - path: pages/traits/physiology/isogamy.html
    sha256: 647225be5b375d186a92e40294ee922547e734f84305915fc5c3120bcf1604da
    role: context
  - path: pages/traits/physiology/karyoklepty.html
    sha256: 6183befec526349a920de675535eee65212e955c6750094cc573e0ace22da3ac
    role: context
  - path: pages/traits/physiology/kinetocyst_discharge.html
    sha256: fec9f6928adc24dd3e3d8ef3a045cf18ae8d5c936bda8cd01df7197e02f6b7bd
    role: context
  - path: pages/traits/physiology/kleptoplasty.html
    sha256: 1fe139730a335894d1a62b3233f0927bcfb9ee1667ab6cc703019bbd7bf235c1
    role: context
  - path: pages/traits/physiology/lecithinase_activity.html
    sha256: c77cc4f2be140b1ccd52c5b349b255794cdd8e4a8039a2179d1efe6df810220c
    role: context
  - path: pages/traits/physiology/lethal_algicidal_activity.html
    sha256: 60532bbb08f18a5e69da9420fb2a26fd8962432f98c0dc339d624bfcacd87623
    role: context
  - path: pages/traits/physiology/leucine_arylamidase_activity.html
    sha256: 8cbb9e7d4e45e0ab733ae860fb5e000d186f8bbe8aa4e4c35775692ee0b57063
    role: context
  - path: pages/traits/physiology/leucyl_glycine_arylamidase_activity.html
    sha256: 60af3be1e6b89fe8b69a24419cb3b0151b07bccefd8c256da9f9c464b09cdc7e
    role: context
  - path: pages/traits/physiology/lipase_activity.html
    sha256: 0ff25a385caa6fae0a1ec1193932a8ff908deda2e18aaccb461728a1903e9bc6
    role: context
  - path: pages/traits/physiology/lipophagy.html
    sha256: 13739169dd8851335b390f651a876738566bc1db6f9ef8a9f4d74047ec38f30e
    role: context
  - path: pages/traits/physiology/lithoautotrophic.html
    sha256: eb4df3b2f82e9d2763a3cb43b8d9096f864b25ed0ec385c443aeac96e7be3cc9
    role: context
  - path: pages/traits/physiology/lithoheterotrophic.html
    sha256: af717e44e1813a917dffc21a5ac76ea37f3e20ed453961b9a85a98863f1c6722
    role: context
  - path: pages/traits/physiology/lithotrophic.html
    sha256: 25fe54a629c413c59b786eaea67bbfd2feceb0fe8ce3efdba7c84cd421b27223
    role: context
  - path: pages/traits/physiology/lysine_decarboxylase_activity.html
    sha256: ee42efde620fd3a64f8ab079367c3c6f35dfb989a310b122c2b2697831aaf697
    role: context
  - path: pages/traits/physiology/macropinocytosis.html
    sha256: 132410487a66af7d0bc982684a8c025adb35523368fb2c0011322cb3a59e71f0
    role: context
  - path: pages/traits/physiology/magnetotaxis.html
    sha256: 6264818f8ff8cdb29cc66f535d0638b91f17a255c0c71232dac5f4b2a9ae144e
    role: context
  - path: pages/traits/physiology/mating_type_switching.html
    sha256: 0791ec89e5e632d4b39a6268cefcc0b6f303aed6091a7395ae345709f0c86986
    role: context
  - path: pages/traits/physiology/methanotrophic.html
    sha256: 5c400045aced4b1d0883b32181ee2dc2a20423dfb69d3910ccf79416d30eba08
    role: context
  - path: pages/traits/physiology/methylotrophic.html
    sha256: a9490f5b54f6745f02c4f9bee313d26d5f6a28cf7b1bbafca60c97ef7c5ec557
    role: context
  - path: pages/traits/physiology/mitophagy.html
    sha256: 7ff9c39be52afb42e96c0df384dd2c96b7222e9a435b36b71d49400ce012c704
    role: context
  - path: pages/traits/physiology/mixotrophic.html
    sha256: cb6ce1924800e0b44a05d6b1f1beb157b13d39afd7a7f9b059307dff347f1455
    role: context
  - path: pages/traits/physiology/mucocyst_discharge.html
    sha256: cf1de9d47de5d3070dafbf9dd2f74837f1cf099d7d54dacb16eaf6407760ada6
    role: context
  - path: pages/traits/physiology/myzocytosis.html
    sha256: dcb3a4ba16c8c7b4d999e6856358c3dfbfae410b3e2c27a0948367372cf8677c
    role: context
  - path: pages/traits/physiology/nad_dependent_alcohol_dehydrogenase_activity.html
    sha256: 5fd8aa5a7a1e5cf8768076ee76b553a1528ad0b6cdd2c61a227176a8470ae0ad
    role: context
  - path: pages/traits/physiology/naphthol_as_bi_phosphohydrolase_activity.html
    sha256: 33fb3d25d716ea9f6f7f0538d9bb421ba6378d17b43b62cde478118ffa97321c
    role: context
  - path: pages/traits/physiology/natural_competence.html
    sha256: e7c7ac58ba08f5384e3880408666126143eefec8fc4d064cd97abb0cb7fa23dc
    role: context
  - path: pages/traits/physiology/negative_autotropism.html
    sha256: 17402f0f17fef82f895ccf543ae6f301d7bf9368ea4bcf105415ee8b9062234f
    role: context
  - path: pages/traits/physiology/nucleophagy.html
    sha256: fd195d8c4f19504e9eb4d2ab4938e93542e5cb748dcd4ca0a6ddbbc74e0326e7
    role: context
  - path: pages/traits/physiology/nutrient_adaptation.html
    sha256: 67eb3bb357512f580853dc307285af5967d775e08160999ac833ee0c673f22f8
    role: context
  - path: pages/traits/physiology/oligotrophic.html
    sha256: ce8168746c8812dbc9ca4e8cb4a8dffad097595d73957ee18578608f9ca631a8
    role: context
  - path: pages/traits/physiology/oogamy.html
    sha256: ba5b78d24f11d66d45dfc7f346c5183b800d04eec28854f841bef1957cc621f2
    role: context
  - path: pages/traits/physiology/organoheterotrophic.html
    sha256: e5d175a2e4399efe3f99cf49414dacd676cf64d63d5ef9fe3d58731c2fd00407
    role: context
  - path: pages/traits/physiology/organotrophic.html
    sha256: 881dd60126d1c5d92516e67e22e01ba6895833d26401caf65ff5f54bd25ed8f8
    role: context
  - path: pages/traits/physiology/ornithine_decarboxylase_activity.html
    sha256: 32ae6d9c7c4e7193b828cc2346d0ce4b2a095d63172ebe63e47748fae7040c12
    role: context
  - path: pages/traits/physiology/osmotaxis.html
    sha256: fa995030d8acda61b211ec354e9a92849fd642f488b90bca7285afbb6842c37c
    role: context
  - path: pages/traits/physiology/oxidase_activity.html
    sha256: b3e2e6725408bfe80931b27ef202adb7a5195b58ce2a67e622c9c38e5d9e9ad5
    role: context
  - path: pages/traits/physiology/oxidative_stress_response.html
    sha256: 8ac2f78907d5cbb863391c6a9be81efb900998184ad7fae83451a677e20eb168
    role: context
  - path: pages/traits/physiology/paedogamy.html
    sha256: 7bc79f93daaacc14a95630dca5b23efc3c6341cadd11cfef308f507f011c8940
    role: context
  - path: pages/traits/physiology/pallium_feeding.html
    sha256: 12c786fcacf91f15eadfb6eaa0ad2357267367664d3d96c4dc7ec8db65f2a538
    role: context
  - path: pages/traits/physiology/parasexuality.html
    sha256: 0cee082db7224eb7316d8617afcf3186972f407cec8de87276e51d8189d41025
    role: context
  - path: pages/traits/physiology/persister_cell_formation.html
    sha256: b6c871a031e5a3fb2e880c5059abda7931442a219c6e2a94295cdad953457d7e
    role: context
  - path: pages/traits/physiology/pexophagy.html
    sha256: f5b2a32996467e98d56e9c32e6db0da8bad7d9b5aef924d91fb37b2989091e63
    role: context
  - path: pages/traits/physiology/ph_taxis.html
    sha256: cf034bfa83d434344a6ce6801128aa365ae61c2d72b38acdadd3c9b6f52692d0
    role: context
  - path: pages/traits/physiology/ph_tropism.html
    sha256: d7042bd8959d2facd1d561b0df917b99af6a00eabce687d6af31941f7c5ab8fe
    role: context
  - path: pages/traits/physiology/phagocytosis.html
    sha256: dccbf6ac348e8d3a1fbcd0ce55071d2310fcabcd5103f3772863aa73d0c26391
    role: context
  - path: pages/traits/physiology/phagotrophy.html
    sha256: 6bcb36937d458151757c0c134526190d7d8062cb33d67a29c4fa418546acdb87
    role: context
  - path: pages/traits/physiology/phenylalanine_arylamidase_activity.html
    sha256: c48c5b9bc24870bc9c27764022eaea532a91fa32082557fd6cd3a3b7a9422de6
    role: context
  - path: pages/traits/physiology/photoautotrophic.html
    sha256: 2136f99a21bf2794326f236d0f683d420b0d06221049a15c941d36009a266207
    role: context
  - path: pages/traits/physiology/photoheterotrophic.html
    sha256: 9a058248afee4a86248a7b88681edd8bf1784661b64f2d3d45b3b71a643b6511
    role: context
  - path: pages/traits/physiology/photokinesis.html
    sha256: a2f6b6f5e132df5b2b40a17a7c568dbccee480b8e8862b660bbe65135b145468
    role: context
  - path: pages/traits/physiology/photolithoautotrophic.html
    sha256: 29e91eaed3e2f3d521118f0a667c3f6304578f58d236b0d179b2d27afc962716
    role: context
  - path: pages/traits/physiology/photolithotrophic.html
    sha256: 34b7df8fd9b8564cb1eb6a0380f0dcd8cd64072af8fe9db039aacbad24af56df
    role: context
  - path: pages/traits/physiology/photoorganoheterotrophic.html
    sha256: c6fdc8bd00aa4090560b06098f9a3161276733fa721b14868877ab34b3b9b60d
    role: context
  - path: pages/traits/physiology/phototaxis.html
    sha256: de785f70e567f66967da8ed5f52f6271fd51ef44d4e70bc8358c98020781bd9d
    role: context
  - path: pages/traits/physiology/phototrophic.html
    sha256: 6fb59c9c4cf6803e1c71fdb8e3e5ffce66fb83c401388d762afb098374a5fe25
    role: context
  - path: pages/traits/physiology/phototropism.html
    sha256: 08094611a17bf579fdef89455c57332cee6294e82024a2263ea72a801681f09d
    role: context
  - path: pages/traits/physiology/pinocytosis.html
    sha256: 57029e33646aef15488f65645b7d0968df58bdf93d989dcc01806f33a1a80d1a
    role: context
  - path: pages/traits/physiology/positive_autotropism.html
    sha256: 502bc4f69a3e54740fe39f1c0f2a81aa6014079c48be9a8846151cf946766155
    role: context
  - path: pages/traits/physiology/primary_homothallism.html
    sha256: f5dec5c8f45e7ca3ef5ef62fa783b1c23d78b1f3eb45821fe46ab754736e8d1d
    role: context
  - path: pages/traits/physiology/prolyl_aminopeptidase_activity.html
    sha256: a9f7ac7ae3fb49fd4f05300ca8b8460c3556c1baa87e3a16ef03da0731289b96
    role: context
  - path: pages/traits/physiology/proteaphagy.html
    sha256: 7991ea3db21de9d513ddb30ccb380d737adafc037d4addfa0a8defb7c827c819
    role: context
  - path: pages/traits/physiology/pseudobipolar_mating_system.html
    sha256: f05f5306beb8d29ecfd01cb08518620e4692eeb2a3f5f14d13f13dcb29ae474d
    role: context
  - path: pages/traits/physiology/pseudohomothallism.html
    sha256: d2566aa2764ee30ba5f693c1d80fda7759f5eb46fb8e2945c6b2c88881d99615
    role: context
  - path: pages/traits/physiology/pyrazinamidase_activity.html
    sha256: 2e41b761b16bc4beb2676d628d8bd3fb2270ba6fcbe8583fa4da7a2d37fe01be
    role: context
  - path: pages/traits/physiology/pyrrolidonyl_arylamidase_activity.html
    sha256: f77714b2ef5d2e3cdd7bece7c907e850c17503c904ee87827bb155879d9000e8
    role: context
  - path: pages/traits/physiology/quorum_quenching.html
    sha256: 97189f87c98142a95a3fceee4fc915de45e9f70899fa1cf954a910452f25f145
    role: context
  - path: pages/traits/physiology/quorum_sensing.html
    sha256: ed789a2e2e9c448dbddce3f1a138855683d397ad52545aa30ce87c737888f3a8
    role: context
  - path: pages/traits/physiology/rapid_axopodial_contraction.html
    sha256: b78728f4727daef13bcfb49ad208fcbf4889f3e62cb684d572509ebb205694a4
    role: context
  - path: pages/traits/physiology/replicative_aging.html
    sha256: c45ec192b98059ff27c2699f0d2c7205b5b5bb2f28006134327eb1cebd71e588
    role: context
  - path: pages/traits/physiology/rheotaxis.html
    sha256: 797a588b18c7f636721b16f8d61cb9ef824dc2c1edd27aa35a43dcfe33ac5d2a
    role: context
  - path: pages/traits/physiology/rheotropism.html
    sha256: 2366d782aeaa0c2591feaea37833f54ad4e27519efeb544a3a2eb00c198781d8
    role: context
  - path: pages/traits/physiology/ribophagy.html
    sha256: 3e9d24831075614d354362d12eadb590da4ae9574a606849d39b3885339da951
    role: context
  - path: pages/traits/physiology/serine_arylamidase_activity.html
    sha256: fcbc538123785ce1119984bed03afa0dfbf5540606d74d665873120eca7e4b70
    role: context
  - path: pages/traits/physiology/siderophore_production.html
    sha256: cf5259d53305d6ff3ebc8b428af43fabfd86175ea432b221bff553bf1722f838
    role: context
  - path: pages/traits/physiology/siliceous_scale_production.html
    sha256: 9a9738fdef3565d0f5a7ab9bf02faed5e6c5142b009ce81b0b0db4269a2a3603
    role: context
  - path: pages/traits/physiology/sos_response.html
    sha256: d1fd75fba1bee7758b45705d3d37f8299afe6a6ae08734430bef29ecb105d3c6
    role: context
  - path: pages/traits/physiology/spore_germination.html
    sha256: cf8104b5de24270719f8d52fbefa3e0845cd7bfa0bdea74dbef7181a213786da
    role: context
  - path: pages/traits/physiology/stress_response.html
    sha256: 2076514c16a5d09852908ad3a04d77ac2d3bdcb5a1d52c66cab4d1be65a42b39
    role: context
  - path: pages/traits/physiology/tetrapolar_mating_system.html
    sha256: c087ba1d0178b287970d63727b56fdc3809ef6b29650a3d5c25f5684de5422a9
    role: context
  - path: pages/traits/physiology/thermotaxis.html
    sha256: 8a38552578d08dcd6a403a20c667a95474f1ef48ca63faa4ea9151dce4606610
    role: context
  - path: pages/traits/physiology/thigmotropism.html
    sha256: 19ad3905fa4fad23cd308503a03bebdd295fa5b7f60ce2b8c0108770fb90b913
    role: context
  - path: pages/traits/physiology/toxicyst_discharge.html
    sha256: 028883b498f80246ea483e2d378dc558f0e48c09d811d39e9fd15a32d3d1e480
    role: context
  - path: pages/traits/physiology/trichocyst_discharge.html
    sha256: 2c80924006d7ec265c6bc0e51c3ea68c8e60e61f1e4911a6d066b78921a075fb
    role: context
  - path: pages/traits/physiology/tripolar_mating_system.html
    sha256: cc46e2a6e496b9762e7a58938d5f8069bf7ef67780ca7390718b9604dafeead8
    role: context
  - path: pages/traits/physiology/trogocytosis.html
    sha256: c0f1060141f6927c1952c2e15803788344957d90535ab5119f7b9cf328ea37a9
    role: context
  - path: pages/traits/physiology/trophic_type.html
    sha256: ec2c70e85534e6e76c30058c1454e57ef84f7803a70acaae4d0b1b82e4d11098
    role: context
  - path: pages/traits/physiology/trypsin_activity.html
    sha256: 3319b09e3d84dcb2f31638821bc959fddf76c6d7f42f06d4ddd55042de4e8ec1
    role: context
  - path: pages/traits/physiology/tyrosine_arylamidase_activity.html
    sha256: 137f162ef0a6f4050fe826721a38af0bf568b84dd48aa0da9c6392aa7b0ce96e
    role: context
  - path: pages/traits/physiology/unconventional_protein_secretion.html
    sha256: 74a47163d28e88ca52ce76bff81fc8e4f352a0b79b6937dda9ee14364ca04442
    role: context
  - path: pages/traits/physiology/unequal_protein_aggregate_inheritance.html
    sha256: ec5703edd36264dfcd1b8d1d6533debf0462481ead1c54386ced7eeef17045e4
    role: context
  - path: pages/traits/physiology/unisexual_reproduction.html
    sha256: ec2b4c33aa3f445673a714eca61a5ff45eeaa7308a1d3a51504e51b3879449c4
    role: context
  - path: pages/traits/physiology/urease_activity.html
    sha256: 0ae900e3aa3ea7a620cd289701f052432380945789f37664d215d201f41b048e
    role: context
  - path: pages/traits/physiology/valine_arylamidase_activity.html
    sha256: 3a2b927547463ca4ce6fcc791ee0f74814d6bf7d38e82eb8aee12c1415a4eece
    role: context
  - path: pages/traits/physiology/viable_but_nonculturable_state.html
    sha256: 629d94db65d208144c291040165e9b546102680f810c7ee0457f61323233e92e
    role: context
  - path: pages/traits/physiology/viscotaxis.html
    sha256: 710bbc25648f20508b081eaf12398d2ccb459ce65181a8d3df07349a1cd6b4dd
    role: context
  - path: pages/traits/quantitative_property/has_maximum_observed_value.html
    sha256: fc805e428fdf4136850229954e3ed2a277fe9da22ba8e109d6e7591a9b9b35b5
    role: context
  - path: pages/traits/quantitative_property/has_minimum_observed_value.html
    sha256: f21090937352c74f03eb5c3a30af7e5517744443980138186ebf8d6a50e10811
    role: context
  - path: pages/traits/quantitative_property/has_observed_spot_value.html
    sha256: be9b87b6968f46f8490a258e2727a9243e66ab4cf226fa17d15cfb6dff2dab68
    role: context
  - path: pages/traits/quantitative_property/has_value.html
    sha256: 9052f4c14ee9a384a5774de0945bc0a378496654c8b351ee7c80cdc7ccca3904
    role: context
  - path: pages/traits/quantitative_property/has_value_comments.html
    sha256: bb5f553b71563054c1a3477a5de505e222cbe2c6953f79cc80ee4aba4c5af67d
    role: context
  - path: pages/traits/quantitative_property/is_negative_data.html
    sha256: 07878f9bbc0e60811cb545ea80680852b6ac8c92e5a8367389d9a39eb44d9858
    role: context
  - path: pages/traits/quantitative_property/observation_data_property.html
    sha256: a037bb458f9eca3e6756285e99a6bb5f1fc5db7343fbdc289f8c6032709a8c6e
    role: context
  - path: pages/traits/upper/biological_process.html
    sha256: 595a01fca7d4a5115d5e4e4543868c43a00af16318e8f159175ed3c7a0ac649c
    role: context
  - path: pages/traits/upper/chemical_entity.html
    sha256: 69878a177441c1ac96bfe0ef190df2a0f73d802a7381bdd4f95a8cbfc166e378
    role: context
  - path: pages/traits/upper/enzyme.html
    sha256: d6c8b698497bab760d041423bfb421f5ad39793f5e1a6b10f8c3778842e71dc9
    role: context
  - path: pages/traits/upper/material_entity.html
    sha256: 53cbfa9c6d7f824f3c566392f6d1f8363b3252cd12bddb1ae485e16ede4df005
    role: context
  - path: pages/traits/upper/microbe.html
    sha256: e11a9475eb7d93de220ec2858697c6dddb7776224bcfad15406f96704250050e
    role: context
  - path: pages/traits/upper/observation.html
    sha256: 717771c289b37e1e5b0cd77096e2a284770e5ce51fbd0b0f67dfe60971df9b7f
    role: context
  - path: pages/traits/upper/phenotype.html
    sha256: 40afe2e93646a6feffa49a81b9845c66739f88f4995075cb3bd8bc1c8ade568b
    role: context
  - path: pages/traits/upper/quality.html
    sha256: fb5530ea7c1b5092f66f5516ab3e5221a1ba1dccb3aa9bf5f4285f0de8872774
    role: context
  - path: pages/umap.html
    sha256: 0cb03b433e0169eaf4185adf3a16fd3057012825c1f7db2c038396b5bad50a96
    role: context
  - path: proposals/metpo_traitmech_v587/metpo_proposal_classes_robot.tsv
    sha256: 014010d8a37af494a84bb34d874c5cf59dc000e1ca56067f6710023294d9b921
    role: context
  - path: proposals/metpo_traitmech_v587/proposal.md
    sha256: 3aae03e2ed9b358e3228cf90eadcc612b94a2bd12e24e2c1acc978eea865e19c
    role: context
  - path: reports/metpo_2026_06_12_active_review.tsv
    sha256: 45e9c6471475635ba1f2602cd636a119d490f5dbd8dd6ac8af1aab89a321379f
    role: context
  - path: reports/metpo_2026_06_12_release_delta.tsv
    sha256: afe858d2aa0ade08322c7808d5917ff370e069ba02c2642d483342db8e9323ac
    role: context
  - path: reports/proposal_citation_audit.tsv
    sha256: 4ab6df7d3b4e1c19a13202ca6c665022c15ef18c10b5bf249162d5c402d6f369
    role: context
  - path: reports/robot/metpo_traitmech_v587/classes.owl
    sha256: 5b7c66e0891da40b8395ccc989c27962dfd61879b27110d04864acbb24ae2b21
    role: context
  - path: reports/robot/metpo_traitmech_v587/merged.owl
    sha256: 9482ac4d9f6eeb6bae44b31bbea636c5d344998076ef0ca80c2b2eb289436509
    role: context
  - path: reports/robot/metpo_traitmech_v587/reasoned.owl
    sha256: ec0a4d3aea035e5e3d33a85f13ac250b2cb82fe3890c21980b9032ea42a3dbdd
    role: context
  - path: research/traits/physiology/unequal_protein_aggregate_inheritance-source-verification.json
    sha256: 9b70713c700e8b6d0dbe7fe532b2189628cba107e86fac48580d6c31c464426b
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
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/.vendored_canon_ref
    sha256: 698af47e96e93fe96e81910bb140593a79c2b92c4688892edeab9b63244ec5bf
    role: context
  - path: scripts/add_unequal_protein_aggregate_inheritance_trait.py
    sha256: 3ed72340598442ed8632d9c796e36fc163b0fefe386d64f84f3eb0e87e709325
    role: context
  - path: scripts/audit_canonical_examples.py
    sha256: 367b9a1759b81e545b06c8dc0c22419ae8d478e3fcd8de6d0bc0cacbb9eacf54
    role: context
  - path: scripts/qualify_aggregate_inheritance_reporter.py
    sha256: 4e2083c49e07a48fa1420a5f7943e9f2c8b1b2fb1097b0eca93e25675f73d8e8
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
  - path: tests/test_add_unequal_protein_aggregate_inheritance_trait.py
    sha256: c3ff26b1c33d67770e08bd7d3d77c71c0b18c5acfd1af103feafddf86275d1c9
    role: context
  - path: tests/test_qualify_aggregate_inheritance_reporter.py
    sha256: b71aeff89f8ca1350824b343bc81fefbaece3a2eed87aab12375e95fde82fc7d
    role: context
targets:
- target_id: traitmech:000711
  path: data/traits/physiology/unequal_protein_aggregate_inheritance.yaml
  label: unequal protein aggregate inheritance at cell division
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: scripts/add_unequal_protein_aggregate_inheritance_trait.py
    role: original guarded curation writer
  - repository: CultureBotAI/TraitMech
    path: scripts/qualify_aggregate_inheritance_reporter.py
    role: guarded evidence correction
  - repository: CultureBotAI/TraitMech
    path: data/traits/physiology/unequal_protein_aggregate_inheritance.yaml
    role: maintained trait record
  - repository: CultureBotAI/TraitMech
    path: proposals/metpo_traitmech_v587/metpo_proposal_classes_robot.tsv
    role: companion METPO proposal
  - repository: CultureBotAI/TraitMech
    path: research/traits/physiology/unequal_protein_aggregate_inheritance-source-verification.json
    role: historical source assessment and appended correction
scope:
  description: Complete new record and maintained/generated change set; no whole-corpus
    scientific review.
  selection: One exact newly curated trait, no sampling.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - traitmech:000711
  exclusions:
  - target: Other1105 TraitRecords
    reason: Novelty, byte preservation and deterministic validation only.
  - target: data/traits/physiology/spore_germination.yaml
    reason: Protected; unchanged.
checks:
- check_id: writer-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q tests/test_add_unequal_protein_aggregate_inheritance_trait.py tests/test_qualify_aggregate_inheritance_reporter.py
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q tests/test_add_unequal_protein_aggregate_inheritance_trait.py tests/test_qualify_aggregate_inheritance_reporter.py
  status: passed
  required: true
  target_ids:
  - traitmech:000711
  exit_code: 0
  expected_exit_code: 0
  summary: 32 focused tests pass, including historical preservation, correction replay,
    preimage guards, proposal/source consistency and prevalidation failure without
    writes.
- check_id: records-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate
    -s src/traitmech/schema/traitmech.yaml --target-class TraitRecord data/traits/physiology/unequal_protein_aggregate_inheritance.yaml
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate
    -s src/traitmech/schema/traitmech.yaml --target-class TraitRecord data/traits/physiology/unequal_protein_aggregate_inheritance.yaml
  status: passed
  required: true
  target_ids:
  - traitmech:000711
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed on the corrected content; deterministic corpus
    validation is not whole-corpus scientific review.
- check_id: records-1
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_strict.py data/traits/physiology/unequal_protein_aggregate_inheritance.yaml
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_strict.py data/traits/physiology/unequal_protein_aggregate_inheritance.yaml
  status: passed
  required: true
  target_ids:
  - traitmech:000711
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed on the corrected content; deterministic corpus
    validation is not whole-corpus scientific review.
- check_id: records-2
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/verify_snippets.py --record data/traits/physiology/unequal_protein_aggregate_inheritance.yaml
    --out /tmp/traitmech-aggregate-inheritance-reporter-checks-20261012/snippet-results.tsv
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/verify_snippets.py --record data/traits/physiology/unequal_protein_aggregate_inheritance.yaml
    --out /tmp/traitmech-aggregate-inheritance-reporter-checks-20261012/snippet-results.tsv
  status: passed
  required: true
  target_ids:
  - traitmech:000711
  exit_code: 0
  expected_exit_code: 0
  summary: 'Four snippets: two VERIFIED scientific-abstract matches and two NOT_IN_ABSTRACT
    Results quotations checked directly in primary full text. Native outcomes are
    not relabeled.'
- check_id: generate-0
  name: just audit-proposals
  command: just audit-proposals
  status: passed
  required: true
  target_ids:
  - traitmech:000711
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed on the corrected content; deterministic corpus
    validation is not whole-corpus scientific review.
- check_id: generate-1
  name: just ground-predicates
  command: just ground-predicates
  status: passed
  required: true
  target_ids:
  - traitmech:000711
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed on the corrected content; deterministic corpus
    validation is not whole-corpus scientific review.
- check_id: generate-2
  name: just ground-nodes
  command: just ground-nodes
  status: passed
  required: true
  target_ids:
  - traitmech:000711
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed on the corrected content; deterministic corpus
    validation is not whole-corpus scientific review.
- check_id: generate-3
  name: just audit-graphs
  command: just audit-graphs
  status: passed
  required: true
  target_ids:
  - traitmech:000711
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed on the corrected content; deterministic corpus
    validation is not whole-corpus scientific review.
- check_id: generate-4
  name: just audit-graph-protein-taxa
  command: just audit-graph-protein-taxa
  status: passed
  required: true
  target_ids:
  - traitmech:000711
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed on the corrected content; deterministic corpus
    validation is not whole-corpus scientific review.
- check_id: generate-5
  name: just audit-predicate-domains
  command: just audit-predicate-domains
  status: passed
  required: true
  target_ids:
  - traitmech:000711
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed on the corrected content; deterministic corpus
    validation is not whole-corpus scientific review.
- check_id: generate-6
  name: just check-biolink-coverage
  command: just check-biolink-coverage
  status: passed
  required: true
  target_ids:
  - traitmech:000711
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed on the corrected content; deterministic corpus
    validation is not whole-corpus scientific review.
- check_id: generate-7
  name: just audit-snippets
  command: just audit-snippets
  status: passed
  required: true
  target_ids:
  - traitmech:000711
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed on the corrected content; deterministic corpus
    validation is not whole-corpus scientific review.
- check_id: generate-8
  name: just gen-discussions-data
  command: just gen-discussions-data
  status: passed
  required: true
  target_ids:
  - traitmech:000711
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed on the corrected content; deterministic corpus
    validation is not whole-corpus scientific review.
- check_id: generate-9
  name: just gen-qc-dashboard
  command: just gen-qc-dashboard
  status: passed
  required: true
  target_ids:
  - traitmech:000711
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed on the corrected content; deterministic corpus
    validation is not whole-corpus scientific review.
- check_id: generate-10
  name: just gen-pages
  command: just gen-pages
  status: passed
  required: true
  target_ids:
  - traitmech:000711
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed on the corrected content; deterministic corpus
    validation is not whole-corpus scientific review.
- check_id: generate-11
  name: just gen-priority-dashboard
  command: just gen-priority-dashboard
  status: passed
  required: true
  target_ids:
  - traitmech:000711
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed on the corrected content; deterministic corpus
    validation is not whole-corpus scientific review.
- check_id: verify-0
  name: just qc
  command: just qc
  status: passed
  required: true
  target_ids:
  - traitmech:000711
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed on the corrected content; deterministic corpus
    validation is not whole-corpus scientific review.
- check_id: verify-1
  name: just validate-history
  command: just validate-history
  status: passed
  required: true
  target_ids:
  - traitmech:000711
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed on the corrected content; deterministic corpus
    validation is not whole-corpus scientific review.
- check_id: verify-2
  name: just validate-products
  command: just validate-products
  status: passed
  required: true
  target_ids:
  - traitmech:000711
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed on the corrected content; deterministic corpus
    validation is not whole-corpus scientific review.
- check_id: verify-3
  name: just verify-proposal metpo_traitmech_v587
  command: just verify-proposal metpo_traitmech_v587
  status: passed
  required: true
  target_ids:
  - traitmech:000711
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed on the corrected content; deterministic corpus
    validation is not whole-corpus scientific review.
- check_id: verify-4
  name: just robot-validate-proposal metpo_traitmech_v587
  command: just robot-validate-proposal metpo_traitmech_v587
  status: passed
  required: true
  target_ids:
  - traitmech:000711
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed on the corrected content; deterministic corpus
    validation is not whole-corpus scientific review.
- check_id: verify-5
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/ruff
    check src scripts tests
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/ruff
    check src scripts tests
  status: passed
  required: true
  target_ids:
  - traitmech:000711
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed on the corrected content; deterministic corpus
    validation is not whole-corpus scientific review.
- check_id: tests-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q --junitxml=/tmp/traitmech-aggregate-inheritance-reporter-checks-20261012/pytest.xml
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q --junitxml=/tmp/traitmech-aggregate-inheritance-reporter-checks-20261012/pytest.xml
  status: passed
  required: true
  target_ids:
  - traitmech:000711
  exit_code: 0
  expected_exit_code: 0
  summary: 4274 full-suite tests passed without skips, failures or errors.
- check_id: supplemental-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_history_links.py history/records/unequal_protein_aggregate_inheritance
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_history_links.py history/records/unequal_protein_aggregate_inheritance
  status: passed
  required: true
  target_ids:
  - traitmech:000711
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed on the corrected content; deterministic corpus
    validation is not whole-corpus scientific review.
- check_id: supplemental-1
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate
    --schema src/traitmech/schema/history.yaml --target-class HistoryRecord history/records/unequal_protein_aggregate_inheritance/2026-10-12T144228Z-codex-c658f7.yaml
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate
    --schema src/traitmech/schema/history.yaml --target-class HistoryRecord history/records/unequal_protein_aggregate_inheritance/2026-10-12T144228Z-codex-c658f7.yaml
  status: passed
  required: true
  target_ids:
  - traitmech:000711
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed on the corrected content; deterministic corpus
    validation is not whole-corpus scientific review.
- check_id: supplemental-2
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate
    --schema src/traitmech/schema/history.yaml --target-class HistoryRecord history/records/unequal_protein_aggregate_inheritance/2026-10-12T182646Z-codex-9c4b15.yaml
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate
    --schema src/traitmech/schema/history.yaml --target-class HistoryRecord history/records/unequal_protein_aggregate_inheritance/2026-10-12T182646Z-codex-9c4b15.yaml
  status: passed
  required: true
  target_ids:
  - traitmech:000711
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed on the corrected content; deterministic corpus
    validation is not whole-corpus scientific review.
- check_id: supplemental-3
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/audit_canonical_examples.py --no-resolve
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/audit_canonical_examples.py --no-resolve
  status: passed
  required: true
  target_ids:
  - traitmech:000711
  exit_code: 0
  expected_exit_code: 0
  summary: 761 existing examples across 576 records passed shape checks with zero
    errors/warnings. --no-resolve does not verify taxonomy existence or labels; no
    canonical example was added or changed.
- check_id: supplemental-4
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/run_trait_graph_audit.py --verify
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/run_trait_graph_audit.py --verify
  status: passed
  required: true
  target_ids:
  - traitmech:000711
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed on the corrected content; deterministic corpus
    validation is not whole-corpus scientific review.
- check_id: supplemental-5
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/audit_history_records.py --base a57b006b32f2313579650d105d7da245a99a5b95
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/audit_history_records.py --base a57b006b32f2313579650d105d7da245a99a5b95
  status: passed
  required: true
  target_ids:
  - traitmech:000711
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed on the corrected content; deterministic corpus
    validation is not whole-corpus scientific review.
- check_id: supplemental-6
  name: git diff --check a57b006b32f2313579650d105d7da245a99a5b95 HEAD -- . ':(exclude)proposals/metpo_traitmech_v587/metpo_proposal_classes_robot.tsv'
  command: git diff --check a57b006b32f2313579650d105d7da245a99a5b95 HEAD -- . ':(exclude)proposals/metpo_traitmech_v587/metpo_proposal_classes_robot.tsv'
  status: passed
  required: true
  target_ids:
  - traitmech:000711
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed on the corrected content; deterministic corpus
    validation is not whole-corpus scientific review.
- check_id: supplemental-7
  name: git -c core.whitespace=-blank-at-eol diff --check a57b006b32f2313579650d105d7da245a99a5b95
    HEAD -- proposals/metpo_traitmech_v587/metpo_proposal_classes_robot.tsv
  command: git -c core.whitespace=-blank-at-eol diff --check a57b006b32f2313579650d105d7da245a99a5b95
    HEAD -- proposals/metpo_traitmech_v587/metpo_proposal_classes_robot.tsv
  status: passed
  required: true
  target_ids:
  - traitmech:000711
  exit_code: 0
  expected_exit_code: 0
  summary: Executed native gate passed on the corrected content; deterministic corpus
    validation is not whole-corpus scientific review.
- check_id: browser
  name: Corrected desktop/mobile generated products
  command: node /tmp/traitmech-aggregate-inheritance-reporter-browser-20261012.cjs
  status: passed
  required: true
  target_ids:
  - traitmech:000711
  exit_code: 0
  expected_exit_code: 0
  summary: '1440/390 px assertions passed: four quotations, three discussions, two
    history links, correct local identity, navigation and dashboard. Ten screenshots,
    including the fourth evidence item, visually inspected; no horizontal overflow
    or page errors.'
- check_id: embedding-sources
  name: Pinned generator and exact embedding-source applicability
  status: passed
  required: true
  target_ids:
  - traitmech:000711
  summary: 152 pinned generator blobs verified. Neither configured embedding source
    exists in the primary/owned layouts; existing embeddings retained.
evidence:
- evidence_id: source-0
  kind: primary_source
  reference: DOI:10.1073/pnas.0708931105
  locator: 'Results: Inclusion Bodies Are Formed in Discrete Cellular Positions and
    Accumulate in Old Poles Under Nonstressing Conditions; /html/body/div[2]/div[2]/div/div[1]/div/div[2]/main/article/section[2]/section/section[2]/section[2]/p'
  accessed_at: '2026-10-12T18:44:16Z'
  support: partial
  summary: Lindner et al. 2008, PMID:18287048, PMC2268587; Results, Inclusion Bodies
    Are Formed in Discrete Cellular Positions and Accumulate in Old Poles Under Nonstressing
    Conditions. Primary PMC Results and Methods directly read. The quoted position
    is that of an IbpA-YFP focus. MGAY is an engineered MG1655 reporter strain, grown
    on LB-agarose at 37 C without imposed stress. Figure 2 is the inspected localization
    measurement; Figure 3 is an inspected lineage schematic, not another experiment.
    Pole identity changes across divisions. These observations describe reporter-focus
    inheritance and eventual older-pole accumulation. Govers et al. 2018 (DOI:10.1371/journal.pbio.2003853)
    subsequently demonstrated label-induced clustering with IbpA-YFP. The older readout
    is not independent proof of endogenous unstressed aggregation; naming the engineered
    strain alone does not resolve this assay bias. Neither active transport, universal
    aggregate toxicity nor a natural canonical exemplar is established. Supplements
    were not inspected. The full-text span retains the native abstract resolver verdict
    NOT_IN_ABSTRACT.
  snapshot_sha256: 0c6ab062a08a77b24637fc5dba99c0022749bd66b298159ef4b37d96f206e494
- evidence_id: source-1
  kind: primary_source
  reference: DOI:10.1371/journal.pbio.1001886
  locator: Scientific abstract, not Author Summary; /article/front/article-meta/abstract[2]/p
  accessed_at: '2026-10-12T18:44:16Z'
  support: supports
  summary: 'Coelho et al. 2014, PMID:24936793, PMC4061010; scientific abstract, not
    Author Summary. Primary XML and actual Figures 3, 4 and S4 were inspected. Hsp104-GFP
    fission-yeast imaging supports stress-associated unequal inheritance without consistent
    old/new-pole bias. Figure 3C measures an absolute sibling difference in aggregate-associated
    fluorescence, not concentration; S4I measures count asymmetry. Figure 4B is fusion
    and 4C is nucleation: the caption reverses them. A Results pointer to 4C for stress-dependent
    asymmetry disagrees with the plotted endpoints. Figure 3C describes continuous
    40 C, whereas Methods describes 40 C for one hour followed by 37 C; this remains
    unresolved. Text S1 experimental methods and strain table were text-extracted,
    not visually rendered. No universal transport, death threshold or rejuvenation
    mechanism is inferred. The scientific-abstract span matches the native resolver
    text (VERIFIED).'
  snapshot_sha256: 9a5214b58556a06248e3aa2235e73b3dd604ccc82234a2f3f7e6a539d24a2666
- evidence_id: source-2
  kind: primary_source
  reference: DOI:10.1111/mmi.14228
  locator: 'Results: The aggregate load does not sort to swarmer or stalked daughter
    cells in C. crescentus; /article/body/sec[2]/sec[5]/p[5]'
  accessed_at: '2026-10-12T18:44:16Z'
  support: supports
  summary: Schramm et al. 2019, PMID:30779464, PMC6850343; Results, The aggregate
    load does not sort to swarmer or stalked daughter cells in C. crescentus. Primary
    XML Results, Discussion and relevant Methods were read; actual Figure 6 was inspected.
    DnaK-mVenus, delta-clpB cells recovered at 30 C after 10 minutes at 40 C. Figure
    6G reports aggregate allocation across daughter cell types over successive divisions,
    not the fraction of all sibling pairs with unequal counts. Figure 6F measures
    projected cell area, not volume. Unequal shared inheritance is compatible with
    the broad phenotype; it contradicts neither sharing nor a stable allocation ratio.
    The paper limits universal exclusive old-pole retention, not every form of quantitative
    inequality. Supplements and independent strain provenance were not inspected;
    no natural canonical example is asserted. The full-text span retains the native
    abstract resolver verdict NOT_IN_ABSTRACT.
  snapshot_sha256: 184c2029dbe93137ef46e5dc3de03c59814f1617771bf956856b2529f2c08eb0
- evidence_id: source-3
  kind: primary_source
  reference: DOI:10.1371/journal.pbio.2003853
  locator: article/front/article-meta/abstract/p; Scientific abstract; Results sec003,
    sec004 and sec006; Methods sec014, sec017, sec018 and sec021; actual Figures 1
    and 3.
  accessed_at: '2026-10-12T18:44:16Z'
  support: supports
  summary: Govers et al. 2018, PMID:30153247, PMC6112618; scientific abstract, directly
    matched in primary XML and source-qualified MED. Results on reporter validation
    and post-stress inheritance, relevant Methods and actual Figures 1 and 3 were
    inspected. Figure 1 shows reporter-dependent clustering; Figure 3 separately follows
    engineered MG1655 IbpA-msfGFP lineages after 47 C for 15 minutes, with microscopy
    at 37 C. Focus inheritance is distinct from the fluorescence concentration and
    growth readouts. This does not validate unstressed IbpA-YFP foci as endogenous
    aggregates or imply universal harm, benefit, aging or rejuvenation. Supplementary
    controls were read only where described in Results; their images, raw data and
    independent strain provenance were not assessed.
  snapshot_sha256: f5e8ed02e307d9153f512ea747a9a0c109eb9ac4b7bc4070a68cb7aba82cdd91
- evidence_id: novelty
  kind: search
  reference: proposals/metpo_traitmech_v587/proposal.md
  locator: Discovery and accepted-scope receipts, pre-allocation audit and successful
    stable publication refresh.
  accessed_at: '2026-10-12T15:01:15Z'
  support: supports
  summary: 'No exact trait or competing reservation in inspected scope. Namespace
    envelope is guarded by exact file hash/context, not treated as a term/cohort reservation.
    No deprecation override, exact xref or silent ontology upgrade. Retained original
    acceptance assessment: this correction changes neither identity, parent nor reserved
    IDs; publication freshness is a separate gate.'
  search_scope: 'Ignored and hidden files were included in available roots, with multiline
    raw searches and structured YAML normalization. Normal binary handling; archives
    were not unpacked and symlink directories were not traversed. Unavailable historical
    ignored/untracked bytes cannot be reconstructed. Known independent clones were
    checked, not every unregistered clone on the computer. Novelty is bounded by these
    snapshots and patterns, not a proof of universal absence. Baseline: 22 registered
    TraitMech roots, 1120 distinct YAML versions, 3 known independent main copies,
    127 CommunityMech registrations, complete pending/draft files and both released
    RDF snapshots; publication refresh adds only the owned worktree. 586 prior cohorts
    and 7143 narrower interval occurrences checked. 55 seed-only leads remain unadjudicated.'
- evidence_id: obsolete
  kind: authority
  reference: METPO:1000011
  locator: Pinned/current released RDF and frozen release review, captured in source
    sidecar.
  accessed_at: '2026-10-12T15:01:15Z'
  support: supports
  summary: 'Deprecated obsolete aggregate has no definition/replacement/consider in
    inspected snapshots; reason annotation OMO:0001000 is not independently interpreted.
    Lexical similarity does not establish inheritance-phenotype identity; historical
    ID is neither reused nor xrefed. Retained original acceptance assessment: this
    correction changes neither identity, parent nor reserved IDs; publication freshness
    is a separate gate.'
- evidence_id: content
  kind: record_content
  reference: data/traits/physiology/unequal_protein_aggregate_inheritance.yaml
  locator: Complete corrected YAML, both guarded writers, tests, proposal, history,
    sidecar, skill and generated page.
  accessed_at: '2026-10-12T18:44:16Z'
  support: supports
  summary: Four source-qualified evidence items; identity, definition, parent and
    PROPOSED status unchanged. Original event, historical source assessment and both
    prior reviews are preserved.
- evidence_id: products
  kind: validation
  reference: reports/proposal_citation_audit.tsv
  locator: Native gates, preservation checks, parsed ROBOT RDF and desktop/mobile
    views.
  accessed_at: '2026-10-12T18:44:16Z'
  support: supports
  summary: 'All 1105 earlier YAMLs, prior history/reviews/proposals/embeddings and
    shared templates are preserved. One new trait remains; parsed RDF counts {''classes'':
    15, ''merged'': 12628, ''reasoned'': 12632}. Required trailing ROBOT header cells
    are preserved.'
- evidence_id: finding
  kind: prior_review
  reference: reviews/structured/20261012T182317Z-aggregate-reporter-bias-finding/review.yaml
  locator: findings[reporter-bias]
  accessed_at: '2026-10-12T18:44:16Z'
  support: supports
  summary: The previously open source-qualification finding is reassessed against
    the guarded correction and newly inspected primary evidence. This supersedes its
    content disposition, not its historical record.
assessments:
- assessment_id: identity
  area: identity
  topic: Recurrent inheritance phenotype
  summary: The unchanged definition describes recurrent inherited count/amount differences,
    not aggregate formation, reporter presence or a single split.
  target_ids:
  - traitmech:000711
  evidence_ids:
  - content
  - source-1
  - source-2
  - source-3
  outcome: supported
- assessment_id: reporter
  area: evidence
  topic: Reporter-dependent clustering and separately validated conditions
  summary: The older reporter readout is retained as historical focus behavior, not
    independent proof of endogenous unstressed aggregation; the later study is qualified
    by reporter and stress context.
  target_ids:
  - traitmech:000711
  evidence_ids:
  - source-0
  - source-3
  - content
  - finding
  outcome: supported
- assessment_id: quantities
  area: quantity
  topic: Cargo amount versus concentration and population bias
  summary: Within-pair inequality, cell-type allocation, exclusion, concentration,
    projected area and volume remain distinguished. No fixed pole bias or universal
    harm/benefit is inferred.
  target_ids:
  - traitmech:000711
  evidence_ids:
  - source-1
  - source-2
  - source-3
  - content
  outcome: supported
- assessment_id: grounding
  area: grounding
  topic: Active broader parent and historical lexical hit
  summary: Phenotype remains the broader parent; neighboring processes are not equated.
    Obsolete aggregate remains historical context, not a reused or exact-cross-referenced
    term.
  target_ids:
  - traitmech:000711
  evidence_ids:
  - content
  - novelty
  - obsolete
  - products
  outcome: supported
- assessment_id: provenance
  area: provenance
  topic: Append-only correction lineage
  summary: Original event, sidecar assessment and prior saved reviews remain; the
    correction has issue-linked history and a guarded writer. All four snippets have
    direct source support.
  target_ids:
  - traitmech:000711
  evidence_ids:
  - content
  - finding
  - source-0
  - source-1
  - source-2
  - source-3
  outcome: supported
- assessment_id: products
  area: consistency
  topic: Generated products and guarded writes
  summary: Native gates, full regression tests, RDF inspection and responsive browser
    checks pass with preserved prior records and no unrelated maintained changes.
  target_ids:
  - traitmech:000711
  evidence_ids:
  - content
  - products
  outcome: supported
- assessment_id: gaps
  area: completeness
  topic: Unresolved optional scope and mechanism work
  summary: Natural strain exemplars, universal thresholds and a shared causal graph
    remain deliberately unasserted. Coelho panel/temperature source discrepancies
    remain explicit.
  target_ids:
  - traitmech:000711
  evidence_ids:
  - content
  - source-1
  - source-2
  - source-3
  outcome: unknown
findings:
- finding_id: reporter-bias
  issue_key: aggregate-inheritance-ibpa-yfp-reporter-bias
  category: evidence
  severity: major
  status: resolved
  certainty: confirmed
  title: Unstressed reporter foci need a label-induced clustering qualification
  description: The notes overstate the evidential role of the older reporter experiment
    without the later primary assay limitation. Retain the historical quote, qualify
    the readout and cite the later evidence.
  target_ids:
  - traitmech:000711
  field_paths:
  - evidence[0].notes
  - discussions[1].rationale
  evidence_ids:
  - source-0
  - source-3
  - content
  - products
  - finding
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: scripts/add_unequal_protein_aggregate_inheritance_trait.py
    role: original guarded curation writer
  - repository: CultureBotAI/TraitMech
    path: scripts/qualify_aggregate_inheritance_reporter.py
    role: guarded evidence correction
  - repository: CultureBotAI/TraitMech
    path: data/traits/physiology/unequal_protein_aggregate_inheritance.yaml
    role: maintained trait record
  - repository: CultureBotAI/TraitMech
    path: proposals/metpo_traitmech_v587/metpo_proposal_classes_robot.tsv
    role: companion METPO proposal
  - repository: CultureBotAI/TraitMech
    path: research/traits/physiology/unequal_protein_aggregate_inheritance-source-verification.json
    role: historical source assessment and appended correction
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/1896
  normalization_reason: Material evidence interpretation, not a label/style preference;
    trait identity itself is not rejected.
  disposition_reason: The older quote is explicitly restricted to reporter-focus behavior,
    the later assay challenge and distinct post-stress evidence are cited, and guarded
    regression/validation/product checks pass. Scientific content correction is complete;
    external review, CI, queue and issue closure remain subsequent lifecycle gates.
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261012T182317Z-aggregate-reporter-bias-finding
    finding_id: reporter-bias
actions: []
limitations:
- Author self-review, not independent or human scientific sign-off; native status
  remains PROPOSED.
- No universal reporter validity, recurrence threshold, pole preference, toxicity,
  benefit, aging or rejuvenation mechanism is asserted.
- No raw-data reanalysis. New primary Figures 1 and 3 inspected; supplementary images/movies
  and independent strain provenance not assessed. Earlier source-specific access and
  figure limits remain.
- Original novelty and reservation coverage remains bounded and included ignored/hidden
  files; fresh publication checks are separate. No global discovery-exhaustion claim.
- The full-suite and QC baseline warnings/skipped adapters remain baseline limitations;
  embeddings were not regenerated because configured sources are absent.
- The proposed TSV keeps required trailing empty header cells; exact-path scoped whitespace
  checks accompany the original whole-PR header finding.
- Resolving the source-qualification finding does not certify future external approval,
  PR/merge-group CI, issue closure, landed integrity or branch cleanup.
related_reviews:
- repository: CultureBotAI/TraitMech
  review_id: 20261012T150115Z-unequal-protein-aggregate-inheritance
  relationship: Reassesses the complete record with newly acquired primary evidence.
- repository: CultureBotAI/TraitMech
  review_id: 20261012T182317Z-aggregate-reporter-bias-finding
  relationship: Resolves the same reporter-bias finding with preserved issue key and
    predecessor identity.
links:
- https://github.com/CultureBotAI/TraitMech/issues/1896
- https://github.com/CultureBotAI/TraitMech/pull/1895
tags:
- add-trait
- aggregate-inheritance
- self-review
- reporter-qualification
```
