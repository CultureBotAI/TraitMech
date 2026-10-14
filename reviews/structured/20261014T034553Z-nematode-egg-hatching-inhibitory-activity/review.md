# Adversarial review of nematode egg-hatching inhibitory activity

- Review: 20261014T034553Z-nematode-egg-hatching-inhibitory-activity
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-14T03:39:21Z
- Finished UTC: 2026-10-14T03:45:53Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Source-based author review supports one hatch-inhibitory microbial capability. No current actionable defect identified; two OPEN discussions retain source, scope and mechanism limits. Earlier README count failures were corrected and tracked in issue 1924.

## Scope And Provenance

One complete new record and its maintained/generated owners, not whole-corpus scientific review.

Selection: One exact new trait, without sampling.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base a7830e6cefa7802c119c18bd33168863c1e54348.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| traitmech:000723 | data/traits/physiology/nematode_egg_hatching_inhibitory_activity.yaml | maintained | nematode egg-hatching inhibitory activity |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate -s src/traitmech/schema/traitmech.yaml --target-class TraitRecord data/traits/physiology/nematode_egg_hatching_inhibitory_activity.yaml | passed | True | traitmech:000723 | Actual maintained command passed; corpus diagnostics are not whole-corpus scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/validate_strict.py data/traits/physiology/nematode_egg_hatching_inhibitory_activity.yaml | passed | True | traitmech:000723 | Actual maintained command passed; corpus diagnostics are not whole-corpus scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/validate_history_links.py history/records/nematode_egg_hatching_inhibitory_activity | passed | True | traitmech:000723 | Actual maintained command passed; corpus diagnostics are not whole-corpus scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/verify_snippets.py --record data/traits/physiology/nematode_egg_hatching_inhibitory_activity.yaml --out /tmp/traitmech-egg-hatching-checks-20261014/native-record.tsv | passed | True | traitmech:000723 | Native snippet command exited zero with two rows: UNRESOLVED and NOT_IN_ABSTRACT. Neither is native VERIFIED. Direct source inspection is separately recorded. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python -m pytest -q tests/test_add_nematode_egg_hatching_inhibitory_activity_trait.py -k 'not source_receipt' | passed | True | traitmech:000723 | Actual maintained command passed; corpus diagnostics are not whole-corpus scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python -m pytest -q tests/test_add_nematode_egg_hatching_inhibitory_activity_trait.py tests/test_readme_artifacts.py tests/test_trait_priority.py tests/test_qc_dashboard_artifacts.py | passed | True | traitmech:000723 | Actual maintained command passed; corpus diagnostics are not whole-corpus scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/ruff check src scripts tests | passed | True | traitmech:000723 | Actual maintained command passed; corpus diagnostics are not whole-corpus scientific review. |
| just audit-proposals | passed | True | traitmech:000723 | Actual maintained command passed; corpus diagnostics are not whole-corpus scientific review. |
| just ground-predicates | passed | True | traitmech:000723 | Actual maintained command passed; corpus diagnostics are not whole-corpus scientific review. |
| just ground-nodes | passed | True | traitmech:000723 | Actual maintained command passed; corpus diagnostics are not whole-corpus scientific review. |
| just audit-graphs | passed | True | traitmech:000723 | Actual maintained command passed; corpus diagnostics are not whole-corpus scientific review. |
| just audit-graph-protein-taxa | passed | True | traitmech:000723 | Actual maintained command passed; corpus diagnostics are not whole-corpus scientific review. |
| just audit-predicate-domains | passed | True | traitmech:000723 | Actual maintained command passed; corpus diagnostics are not whole-corpus scientific review. |
| just check-biolink-coverage | passed | True | traitmech:000723 | Actual maintained command passed; corpus diagnostics are not whole-corpus scientific review. |
| just audit-snippets | passed | True | traitmech:000723 | Actual maintained command passed; corpus diagnostics are not whole-corpus scientific review. |
| just gen-discussions-data | passed | True | traitmech:000723 | Actual maintained command passed; corpus diagnostics are not whole-corpus scientific review. |
| just gen-qc-dashboard | passed | True | traitmech:000723 | Actual maintained command passed; corpus diagnostics are not whole-corpus scientific review. |
| just gen-pages | passed | True | traitmech:000723 | Actual maintained command passed; corpus diagnostics are not whole-corpus scientific review. |
| just gen-priority-dashboard | passed | True | traitmech:000723 | Actual maintained command passed; corpus diagnostics are not whole-corpus scientific review. |
| just qc | passed | True | traitmech:000723 | Actual maintained command passed; corpus diagnostics are not whole-corpus scientific review. |
| just validate-history | passed | True | traitmech:000723 | Actual maintained command passed; corpus diagnostics are not whole-corpus scientific review. |
| just validate-products | passed | True | traitmech:000723 | Actual maintained command passed; corpus diagnostics are not whole-corpus scientific review. |
| just verify-proposal metpo_traitmech_v599 | passed | True | traitmech:000723 | Actual maintained command passed; corpus diagnostics are not whole-corpus scientific review. |
| just robot-validate-proposal metpo_traitmech_v599 | passed | True | traitmech:000723 | Actual maintained command passed; corpus diagnostics are not whole-corpus scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/audit_canonical_examples.py --no-resolve | passed | True | traitmech:000723 | Canonical shape check used --no-resolve, not live taxonomy verification. This record has no canonical examples. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/run_trait_graph_audit.py --verify | passed | True | traitmech:000723 | Actual maintained command passed; corpus diagnostics are not whole-corpus scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/audit_history_records.py --base 4200c75a930654cfec7e635edcbcec896efef919 | passed | True | traitmech:000723 | Actual maintained command passed; corpus diagnostics are not whole-corpus scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python -m pytest -q --junitxml=/tmp/traitmech-egg-hatching-checks-20261014/pytest.xml | passed | True | traitmech:000723 | 4607 tests passed without failures, errors or skips. |
| products | passed | True | traitmech:000723 | All 1117 prior records, protected spore germination, prior history/reviews/proposals/embeddings/templates/baseline are byte-preserved. Old pages differ only in footer counts except the phenotype child link. Exact w3id RDF hierarchy and definition citations pass. |
| browser | passed | True | traitmech:000723 | 1440/390 px tests pass: two quotes, two discussions, one history, local identifier, parent/browse navigation, dashboard count 1118 and loaded coverage image. Eight screenshots visually inspected; no horizontal overflow or page errors. |

## Scientific And Domain Assessments

### Microbial bearer and measured hatch endpoint

identity: supported. Targets: traitmech:000723.

Reduced nematode hatching defines a capability of the microorganism. Egg susceptibility and microorganism development are different meanings. Controls and observation interval bound the phenotype. No killing/recovery mechanism is required.

### Primary hatch assays rather than adjacent endpoints

evidence: supported. Targets: traitmech:000723.

Both studies report their own hatch experiments. Host-specific concentration, denominators, timing and repeat scope remain explicit. Reduced root egg masses, juvenile paralysis, recovery or death cannot substitute for this evidence. Conflicting source details are retained.

### Broader phenotype parent and non-equivalent neighbors

grounding: supported. Targets: traitmech:000723.

Phenotype is broader. Existing related traits have distinct endpoints; a producer may possess several. Bounded ignored-inclusive and ontology checks support local fallback without a global novelty or disjointness claim. No coupled repair is indicated.

### Direct excerpts versus native abstract results

provenance: supported. Targets: traitmech:000723.

Actual typeset/HTML source spans support the quotes. Extraction and abstract-index limits are not concealed. Only definition authority enters ROBOT annotation. Strain/accession ambiguity remains uncorrected rather than being guessed into a canonical example.

### Guarded writer, exact RDF and preserved owners

consistency: supported. Targets: traitmech:000723.

Writer dry-run/replay/schema/drift tests, full QC, history, proposal and responsive browser checks pass. Existing records and immutable artifacts are preserved. README counts agree after the recorded correction.

### Unresolved source and mechanism gaps

completeness: unknown. Targets: traitmech:000723.

No egg-death/recovery inference, universal host or potency cutoff, shared active molecule, causal protein, field efficacy or environmental safety is established. These limits do not erase the narrower observed capability.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| source-0 | DOI:10.1163/156854104323072883; Results, printed page 28/PDF page 6, lower left column. All ten article pages, Methods, Results, Table 1 and Figure 1 inspected. Quoted page re-inspected during curation. No full raw-data reanalysis or canonical taxonomy verification. | supports | Results and Table 1 support reduced SCN/RKN hatch in fungal filtrates. Fourteen-day counts include motile and immotile juveniles; initial egg count and matched uninoculated PDB denominators are distinct. Seven days is culture age. Host assays use different filtrate concentrations. Only 40 of 253 isolates were retested. Hatch inhibition does not establish egg death, recovery or a molecule; unneutralized pH remains a condition. The separate USDA/paper motility-count discrepancy is retained. |
| source-1 | DOI:10.1038/s41598-023-33669-z; Results, egg-hatching paragraph; not a named egg-assay Results subsection. Original publisher HTML scientific Abstract, own hatch Results, culture-filtrate and hatch Methods, actual Figure 3 inspected. Prior qualified supplement/GenBank checks were reread; no full DOCX page render or complete field/raw-data audit. | supports | The quoted Results describe the study own hatch experiment, not its background Meyer summary. Five egg masses, 20/40/60/80% spore-checked filtrates, water/PDB controls and alternate-day counts through ten days support the endpoint. Results maximum at 120 h conflicts with Figure 3 time labels, so no exact maximum/time pair is adopted. Egg deformation and juvenile recovery do not establish egg death or recovery. GenBank/supplement strain inconsistencies preclude a canonical taxon. |
| content | data/traits/physiology/nematode_egg_hatching_inhibitory_activity.yaml; Whole record, guarded writer, tests, proposal, sidecar, history and generated diff. | supports | One microbial capability reducing nematode egg hatching over a defined observation interval versus comparable unexposed controls. The microorganism is the bearer. It is not a susceptibility trait, an assay, a chemical role or a sequence feature. No egg death, irreversible arrest, recovery, canonical examples, exact synonyms/xrefs, proteins or graph are inferred. |
| ontology | data/raw/metpo.owl; Three OWL inputs, six upstream TSV owners and current neighboring records. | supports | Phenotype METPO:1000059 below quality METPO:1000188 is a conservative broader parent. Infection, feeding, killing, trapping, attraction and paralysis are not required. The only egg lexical lead in active/deprecated/draft annotations was fried-egg-shaped colony, not an equivalent. The editor input has 31 metadata triples and is not an import closure. Pinned OWL is unchanged. |
| novelty | research/traits/physiology/nematode_egg_hatching_inhibitory_activity-source-verification.json; Known ignored/hidden current copies, retained regular-file history, changed pending blobs and selected upstream owners. | supports | 182 known locations, 178 available, 139 retained heads, 11 open/draft PRs, 783 pending nonremoved blobs and 587 selected upstream owners were screened. All 76 matched paths were adjudicated. Existing hatch mentions are exclusions or literature context, not exact synonyms/nodes/parent gaps. CommunityMech TYQ1 is a consortium, not this microbial trait. Sequence categories remain leads. Zero exact allocation hits and 665 broad editor-envelope intervals did not establish conflict. |
| provenance | research/traits/physiology/nematode_egg_hatching_inhibitory_activity-source-verification.json; Primary source bytes, typeset/HTML excerpts, native report, metadata and notice-check receipts. | supports | Meyer supplies definition authority; Saharan supplies an independent primary hatch assay, not an automatic definition citation. The 22/13-word quotes were directly checked. Meyer PDF extraction loses fi, so typeset fidelity is not text-layer or native verification. Native outcomes remain UNRESOLVED/NOT_IN_ABSTRACT. Original Nature HTML was reread after fresh web access failed; it is not called a fresh download. Meyer Crossmark has no data; other bounded checks are not comprehensive notice clearance. |
| products | reports/proposal_citation_audit.tsv; Actual native checks, parsed RDF, byte preservation and responsive browser receipts. | supports | All required local gates pass. RDF triple counts: {'classes': 15, 'merged': 12628, 'reasoned': 12632}. Only Meyer and the local record annotate the definition. All 645 pinned CLAW blobs match. Both configured embedding inputs are absent and existing embedding artifacts are retained. |
| history | history/records/nematode_egg_hatching_inhibitory_activity; Minting and append-only CREATE entries. | supports | Observed acceptance at 03:09:57Z precedes CREATE at 03:14:30Z. Codex/GPT-5 and LLM assistance are explicit. Record remains PROPOSED; no human sign-off is inferred. |
| readme | https://github.com/CultureBotAI/TraitMech/issues/1924; Initial failed focused receipt, corrected README and successful rerun/full suite. | supports | Pre-review validation found stale category/prose counts (59 passed, two failed). The maintained README category row, total, prose and layout were corrected without changing test assertions. The successful 61-test rerun and full suite supersede that failed attempt. Issue 1924 tracks the correction through PR merge; it is not a remaining reviewed-tree defect. |
| publication | /tmp/traitmech-egg-hatching-publication-20261014/accepted.json; Refreshed local ignored/hidden reservation and live remote identity guards. | supports | 183 known locations rechecked. Owned hits separated from competing reservations; no conflict identified. Remote and retained-head identities remain as inspected. |

## Limits And Additional Notes

- Author self-review only. Exact-head external review, CI, native queue and landed-tree verification remain separate publication gates unfinished at this timestamp.
- Meyer pages were visually inspected during research and the quoted page reread during curation/review. Saharan HTML and actual Figure 3 were read. No complete raw-data/statistical reanalysis or independent experimental replication was performed.
- Hatch inhibition does not establish death, irreversible arrest, later recovery, universal host/stage response, a dose threshold, canonical taxon, field efficacy, mechanism or safety.
- Native UNRESOLVED and NOT_IN_ABSTRACT outcomes are retained. Neither quote is native VERIFIED. Meyer text extraction loses a ligature. Nature fresh web access and PMC browser challenge limited live full-text access; original bytes remained readable. Bounded notice checks do not certify comprehensive clearance.
- Canonical-example auditing used --no-resolve for shape only. No canonical example is asserted here.
- Known ignored/hidden copies were included. Four unavailable locations, lost historical ignored/untracked files, symlink targets, arbitrary archives and unchanged pending-tree content were not reconstructed. Discovery is not exhausted and allocation is not atomic.
- Configured embedding inputs are absent; existing embeddings are unchanged. Required empty ROBOT cells use a path-scoped whitespace exception, not an unqualified clean-whitespace claim.
- The initial focused run failed two README assertions and is retained as a failure. Corrected counts pass unchanged tests; issue 1924 awaits the reviewed PR merge.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T034553Z-nematode-egg-hatching-inhibitory-activity
kind: record
repository: CultureBotAI/TraitMech
title: Adversarial review of nematode egg-hatching inhibitory activity
started_at: '2026-10-14T03:39:21Z'
finished_at: '2026-10-14T03:45:53Z'
reviewer:
  identity: codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Author source-based adversarial assessment, not independent-agent
    or human review.
skill: .claude/skills/add-trait/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Source-based author review supports one hatch-inhibitory microbial capability.
  No current actionable defect identified; two OPEN discussions retain source, scope
  and mechanism limits. Earlier README count failures were corrected and tracked in
  issue 1924.
source:
  git_revision: a7830e6cefa7802c119c18bd33168863c1e54348
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
    sha256: b75047c23f19f0a660c15909e6af7bec81d9a5e742019a4662911f28cdda7e11
    role: context
  - path: app/dashboard/priority.html
    sha256: 3dcfccc2e17a236d8534d6fc6be3517a1ef336ae6e19d2edad9b3e97546d2d53
    role: context
  - path: app/dashboard/priority.json
    sha256: 2feb3197fa08089a4530ec825c13485710ed0cead3b6f2df9331a1cd79d96a69
    role: context
  - path: app/discussions/data.js
    sha256: b791d0cf6830446f55291dc57d5f32c98c5f24f043ed1433b92969db14d63803
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
    sha256: 6bdf73be1861c9c14b79d839c93edf45e021a7196d56ffd24da15ffad39c5338
    role: context
  - path: dashboard/index.html
    sha256: 67cada02cdc182233351e8c28e802ef93f0a65344eadea2bd26d192b080cfe61
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
  - path: history/records/nematode_egg_hatching_inhibitory_activity/2026-10-14T031430Z-codex-f597d7.yaml
    sha256: ae365d285cf93c9e74a42e0b8f5c18e33cb9fb664765d97e5dd74162a285d61c
    role: context
  - path: justfile
    sha256: e6047ea612115a6a78d100b281483ba824c860c3def59bcd0d40e7fb56b3526a
    role: context
  - path: pages/browse.html
    sha256: d2976cf36d8770fca2fcb66b69f06b3121c3befae6fb33c87619774a621589e9
    role: context
  - path: pages/category/ecology.html
    sha256: a2505acc151c1eb8590914d9fa5506c4198775a06806addb0911955d3e82160f
    role: context
  - path: pages/category/environment.html
    sha256: ad62ab0231d20050c226105e547513ba13aa04c89b7595b0829003778b46b7e5
    role: context
  - path: pages/category/genomics.html
    sha256: 250cb72dadb41f61f5fdcb5d9e06cd4f1540ff2cca3bf0d109f22c92c8bcdf17
    role: context
  - path: pages/category/metabolism.html
    sha256: b33b82efdc0b99899602d81539b65c3a211f3b8b42a1955e7f7585be2a6b5ac1
    role: context
  - path: pages/category/morphology.html
    sha256: 431eae8a8b6cc9b14233f44d7183d58231690842b1334ac6cd88919d8df2688f
    role: context
  - path: pages/category/observation.html
    sha256: 4109ac0c255e11cc3b0c0c6541ea9f4106d1d995b2d61bb551d438298e354aa7
    role: context
  - path: pages/category/other.html
    sha256: 977c1ccdf1092e3a02af81f4f2f01fe97da4780bba5173ec6476f00ad4af3867
    role: context
  - path: pages/category/physiology.html
    sha256: 115a0a2b44bead13e02e354f141c39dcf77507e3b0f5df06cbbafb7e14cbfccd
    role: context
  - path: pages/category/quantitative_property.html
    sha256: faf44dc08090b965dff2e74bacfd914f89591da9abcbf4e9a3b3c4328ee92b88
    role: context
  - path: pages/category/upper.html
    sha256: 423f3f521c67de624e1b6e275fa0376fac3720472817523aec2cc98da71046f4
    role: context
  - path: pages/graph.html
    sha256: 731b6e21ca94d1656722f9477f652a6ac18855fba826c357d4002ffff1200546
    role: context
  - path: pages/index.html
    sha256: c5fba255bdbdca094eca944e2d5c9dba3bf314669200d06d237eeb61a85a4bb3
    role: context
  - path: pages/traits/ecology/animal_pathogen.html
    sha256: 45310a0286d35532565123fdefce2325ed3bcc49d4c7c9229736b0555fd6294d
    role: context
  - path: pages/traits/ecology/bacterial_cannibalism.html
    sha256: 52559a9b2534597a5ee7ff1b4eaf0823540cf149e9822fb46ede730c9770a206
    role: context
  - path: pages/traits/ecology/bacterial_mycophagy.html
    sha256: f1773d2c154bbd386389e7bddf8cd4e0b1e577207e620da9d09ca75c9aabf8ba
    role: context
  - path: pages/traits/ecology/biofilm_formation.html
    sha256: b09d44a540f9c535bb0a9033b71a4fc26d35ab1cbf1c246b0d478caa25e0816f
    role: context
  - path: pages/traits/ecology/biosafety_level.html
    sha256: 96f9c900f2b2271ac42f2a4f6fe5a5694d8988be05ca6aa2ea22f636d5f13435
    role: context
  - path: pages/traits/ecology/biosafety_level_1.html
    sha256: def5ef1f10229065335f05984cc346870f276a4aa32885f8ccf404d27e28b1fd
    role: context
  - path: pages/traits/ecology/biosafety_level_2.html
    sha256: d7c59d03e527706aa743bb0cb68ec766130cfcce89745d879c0b430ff34e6c3a
    role: context
  - path: pages/traits/ecology/biosafety_level_3.html
    sha256: 14377db73aebaeb9629a21700ae69c33d08ad803460e7e341ee1df3cd9619898
    role: context
  - path: pages/traits/ecology/biosafety_level_4.html
    sha256: 82a01446b20ffac3643f617850a31f44241ff42897fa78c8448e184bc71bbcbc
    role: context
  - path: pages/traits/ecology/biosafety_level_5.html
    sha256: eb53752f01bfbe1b40bb03f36db4bdf4c3286e1ebae1d7c32077c8ffd386eaec
    role: context
  - path: pages/traits/ecology/collective_bacterial_predation.html
    sha256: c26038bd429ff652035a728af8aaf770121d5b0b91493d48411df9352c1efa54
    role: context
  - path: pages/traits/ecology/commensalism.html
    sha256: e6e64d3290b3a6fc9c70fc108ed8100b25769c67a3d9c07f33474b84c3d115d8
    role: context
  - path: pages/traits/ecology/cytoplasmic_bacterial_predation.html
    sha256: 12d5af3316ba5534e55b027d3056ab4b39206662474b6adae87f28463ca4e4ab
    role: context
  - path: pages/traits/ecology/endophytic.html
    sha256: 92f0bd5b9bcade38465dc51c6c42675fbe6e440ce0138ffb42db7e8ffa2e835a
    role: context
  - path: pages/traits/ecology/endosymbiosis.html
    sha256: 3e3a1630540338e35fe78f61f91f6fffa680c14426f6c5dbfe2170c083386e2d
    role: context
  - path: pages/traits/ecology/epibiotic_bacterial_predation.html
    sha256: ae74827d78f214811a487f66d3adb76d7e65443251b825b9549fda28db766410
    role: context
  - path: pages/traits/ecology/epiphytic.html
    sha256: 75c42bf54ed35a75f7f2b4f0af3cead0efe91a2c112ddc557909e322ab3701f0
    role: context
  - path: pages/traits/ecology/free_living.html
    sha256: 41db00041e67be9c9864e4a1a7a00247ed6840e4b501b0260c8361ad0ab93dc6
    role: context
  - path: pages/traits/ecology/fungal_nematophagy.html
    sha256: c33235860134a3f3ae44d747c197010fc99d4b297fdbd510704025ba29fa09a2
    role: context
  - path: pages/traits/ecology/gut_associated.html
    sha256: 10abb7539a0b785cc777cd86841be7bb1f24c77ba8f016e6c5955fb5c9cf93bc
    role: context
  - path: pages/traits/ecology/habitat_association.html
    sha256: edfe77864d9257694474b9e2ad73757ad48ebecfe3e52a39b59baf751d11c658
    role: context
  - path: pages/traits/ecology/host_associated.html
    sha256: 31eb9408f1c6993a3f07d99ce590d4e1d46c2b0a588d653e68710848ff6ca300
    role: context
  - path: pages/traits/ecology/human_pathogen.html
    sha256: 73ee6927eb88f2e6fa21b138d0e847a0e3c28ecb553bd8be41041ccb41629e57
    role: context
  - path: pages/traits/ecology/ixotrophy.html
    sha256: 91b5b8db0a694e6eec7394605cfad0dd9b822cbd45c727315ab1dd17a640ef67
    role: context
  - path: pages/traits/ecology/kin_discrimination.html
    sha256: 8f27271f7fbee65f3f84dc86cc4da33b14bfffa2d2a90990c0eb3628b49cc8f6
    role: context
  - path: pages/traits/ecology/mutualism.html
    sha256: 82cf07d49c7ac46b5b69513ed5b3dba5134a8b87dba86488dde3e09ddb8e1255
    role: context
  - path: pages/traits/ecology/nitrogen_fixing_symbiosis.html
    sha256: f0a808abc1401ff509a8f419f17626f8a6c043dc0f63fdda3e4008db1d102582
    role: context
  - path: pages/traits/ecology/nutritional_fungal_mycoparasitism.html
    sha256: ceea83afe52cf6592141993a1d32adfe51f79f77fe129c410a031e03f72dbce1
    role: context
  - path: pages/traits/ecology/opportunistic_pathogen.html
    sha256: a124fdae7ad3fe26a906ce16da53be97426e72776919b892395a30846f6e1488
    role: context
  - path: pages/traits/ecology/parasitism.html
    sha256: 22a15bcaead8417d6a25e25b003d4c706ae3ca6115b503a46d9df1c62264cca9
    role: context
  - path: pages/traits/ecology/pathogenic_to_host.html
    sha256: 3f27de61ac2f111b39bb3e0194aa65e2253cc570eb083abfae239404c250c3c5
    role: context
  - path: pages/traits/ecology/periplasmic_bacterial_predation.html
    sha256: ea4d4a7c3c2748b82d48420e558f510f241416a967ad6a4ff4d25b7dcc6186bb
    role: context
  - path: pages/traits/ecology/plant_pathogen.html
    sha256: df659a1f41c5ab30b3c80bcefe935ffdbc89de35c6036005c7f3c0e675f7699b
    role: context
  - path: pages/traits/ecology/predatory_bacterium.html
    sha256: 5aefa6f4ec0c16f5c041457dd342151e03bc613e5ad4472c0043c17bb060f47d
    role: context
  - path: pages/traits/ecology/rhizosphere_association.html
    sha256: 9b12b5f83204c95ff712e32286492d176a71f1da9f1df8cf90c68b9b35d21aed
    role: context
  - path: pages/traits/ecology/saprotrophy.html
    sha256: ff000abc8451bdac1ec85c86fe50c952a966d590ca66432cc083f9ea6b77cdb1
    role: context
  - path: pages/traits/ecology/soil_dwelling.html
    sha256: 1e631f1ec836149d58b01be3f659eda230970f2f260d5cc979c3f400794064ab
    role: context
  - path: pages/traits/ecology/symbiosis.html
    sha256: 0e281d95896598f42d390a199220cc7c9ba7558003cc95dbc3e8282d4687f81a
    role: context
  - path: pages/traits/environment/acidophilic.html
    sha256: 4e0d0d975b027cc56bdbbec8feed6c44275dc886d353ed1f776114fe33e41dff
    role: context
  - path: pages/traits/environment/acidotolerant.html
    sha256: cf978f027b42ff8ff65d403e86edda3d8f8d582f5732343729b6cb7d8742fdfc
    role: context
  - path: pages/traits/environment/aerobic.html
    sha256: c7deb8fc9c5af27a54b5037a357664ed24dcb5f75fc931d19b111af89d7eca54
    role: context
  - path: pages/traits/environment/aerotolerant.html
    sha256: c5bd38942ae97d59c4abe317a0355fbc4702d74207c65caaed42a3547acc4f51
    role: context
  - path: pages/traits/environment/alkalotolerant.html
    sha256: 25a8b72691d2f785172dd28b822c476f6e18a477cad0a1536bc8e83949a30891
    role: context
  - path: pages/traits/environment/alkaphilic.html
    sha256: 092754b2a6cddf20ce9a6b4a78848273f77840b7c40910bb0a7583eb660d599c
    role: context
  - path: pages/traits/environment/anaerobic.html
    sha256: 4be96c9b8d1e1c9109ca618b37a917bb4427f7d25c57c8c9f1e6bdffcda60152
    role: context
  - path: pages/traits/environment/arsenic_tolerant.html
    sha256: 3ba1e961eb55a5b98e533630afb617f85f537ddd19216ad356f298c4c6ececf8
    role: context
  - path: pages/traits/environment/cadmium_tolerant.html
    sha256: 85a036d551e1f705f0702ed4154bde1ef771f6f6a7148cb684806b6edb3d9acf
    role: context
  - path: pages/traits/environment/capnophilic.html
    sha256: 6eb01550cded3c9cc436099957fa50c2b998faad5e5eeb915906d0b41e111ae3
    role: context
  - path: pages/traits/environment/cobalt_tolerant.html
    sha256: 8a49cc4a609173ed2289b177c8b0b045867cfec74f4f8d7ec180a04370920108
    role: context
  - path: pages/traits/environment/copper_tolerant.html
    sha256: aef0d6ef1c3f5018bc6cc8f6868a355b47de45540b7c84e64ab92bb0864233c5
    role: context
  - path: pages/traits/environment/delta_phenotype_with_numerical_limits.html
    sha256: 2c08d97d5aa71b527fbdc948e45a5323c2468bccb931620bfe26b9559860f62b
    role: context
  - path: pages/traits/environment/desiccation_tolerant.html
    sha256: 31d6c61b949a02a49fc8a790bef73bd70cadbb7d33883b2b5ecdc8fbd00f92a9
    role: context
  - path: pages/traits/environment/euryhaline.html
    sha256: 9aefeeceeab4995fe5f06ed55589f50647f12b87e7fadc980e79516f17c8bc3f
    role: context
  - path: pages/traits/environment/extreme_hyperthermophilic.html
    sha256: 3489b983a13e79121e5c66051f154fd20de44e3597bea8d83a9fbc0205e67d7c
    role: context
  - path: pages/traits/environment/extremely_halophilic.html
    sha256: 3cb79aa747a59e5123043c1bc34fc6a518a946a86a6204a7bdd9ef1e6d279f04
    role: context
  - path: pages/traits/environment/facultative_oxygen_preference.html
    sha256: d966cc105042621d68c61e92091c62fb2169d2f05fcd38b4704491fd597acc7e
    role: context
  - path: pages/traits/environment/facultative_psychrophilic.html
    sha256: 1b7034faf46e29b4d4cf06f7675cee3a8bc66f58fb2b1423f16316cb18beb269
    role: context
  - path: pages/traits/environment/facultatively_acidophilic.html
    sha256: e4b15fe86a858863aa2c8a069642b4627b244516e6cf36db05f333ccf74dd045
    role: context
  - path: pages/traits/environment/facultatively_aerobic.html
    sha256: 8b46b8941715f0cc48ffa8b656243055568fcb7c5081b775b137727ee9e48067
    role: context
  - path: pages/traits/environment/facultatively_alkaphilic.html
    sha256: c9b81200bee241434263839eed9001fc0b347b7aadef514ca57796f09700d5ad
    role: context
  - path: pages/traits/environment/facultatively_anaerobic.html
    sha256: df898a377da469af0b9e9e3a5f40e38b4d802f56a657d983b780e1a8a976c2fe
    role: context
  - path: pages/traits/environment/growth_range_phenotype_with_numerical_limits.html
    sha256: f5f2b848b1dbc36b529d65c39056ddd61fd9e7aa0889506a113d1bc1be4d9708
    role: context
  - path: pages/traits/environment/haloalkaliphilic.html
    sha256: d5b1fc4e75c10416b49a128760d3e0efd8978d9607546c260ad67b9b5088e418
    role: context
  - path: pages/traits/environment/halophilic.html
    sha256: 50eae4d77e6eff3f84792d954dce65d8180e6242366d8d94a0cf529d7ee1e598
    role: context
  - path: pages/traits/environment/halophily_preference.html
    sha256: 12cf5a90bf84218138e9a1bbd7f36e3112aeeb1fc2a421919605ab2629adccc7
    role: context
  - path: pages/traits/environment/halotolerant.html
    sha256: e0c212a20fa8ef28ab37c5538ca7b84f997a5f3d9c8abfa41ddefe39c51fc2d5
    role: context
  - path: pages/traits/environment/hyperthermophilic.html
    sha256: 9744b486c15d529b3b2a1623047aa33da67a1629843a4ec77eecd4970312afc7
    role: context
  - path: pages/traits/environment/ionizing_radiation_tolerant.html
    sha256: f60351fe5c48c8d406d4a542448032a1d0630e4cee804b82d2c5f2b7973e7744
    role: context
  - path: pages/traits/environment/mercury_tolerant.html
    sha256: 04efba55147ede17d8eab367c736fd5797490c625fab434c1030ff6fa168e5d1
    role: context
  - path: pages/traits/environment/mesophilic.html
    sha256: 3530cbf2dc460378a3833bf643de4d5edd96f99975011f8686adf720f833f0af
    role: context
  - path: pages/traits/environment/metal_tolerant.html
    sha256: a681b481d3dbad21afe87e3e934c07dc1847a91066761fc5cc40e7df48b4200b
    role: context
  - path: pages/traits/environment/microaerophilic.html
    sha256: af663945a3f17dfac0c69c4a8f60772f5bc21140d12caf4cb11df22279b28167
    role: context
  - path: pages/traits/environment/microaerotolerant.html
    sha256: b3162e91b722138d0cf4299d53c68b96d1cff24b3fca09867d1edb738194873a
    role: context
  - path: pages/traits/environment/moderately_halophilic.html
    sha256: 59ca49df9ad9898ae660376e27604d5754ef4f4827e87e88bcf3d23ea8c251bb
    role: context
  - path: pages/traits/environment/nacl_delta.html
    sha256: 2f15f2ce82118df09351b63fae086cb0f2e90c773c402de9329a03f97df1db31
    role: context
  - path: pages/traits/environment/nacl_delta_high.html
    sha256: 4625982e3760c517c2d9bf4d253dfa94dfd643567e6f49c56529e9a6840fb471
    role: context
  - path: pages/traits/environment/nacl_delta_low.html
    sha256: e5ae028526176edd832c483484cd9b91df4f056a4c407c803a7174db2da111e3
    role: context
  - path: pages/traits/environment/nacl_delta_mid1.html
    sha256: d4e9e13b0325cf7700db3052d1db144a30548ba37c3e5bfbc2f0c64bdd9419df
    role: context
  - path: pages/traits/environment/nacl_delta_mid2.html
    sha256: 90130c4b524bde9c3fdba1ef3106fccdeeea4acd98f458cfc944c17031930237
    role: context
  - path: pages/traits/environment/nacl_optimum.html
    sha256: e7dde4303c90f283c6b7b955a63c677ef867070750934abd92925180eeee4dee
    role: context
  - path: pages/traits/environment/nacl_optimum_high.html
    sha256: 2c9f3c51117a044b6e70034377ddc330bc034e717f245699c1e3d161b43a4a1a
    role: context
  - path: pages/traits/environment/nacl_optimum_low.html
    sha256: 18c5f7da6d79d694c0d8457d3331bd91646610ae68b9444e2f95720463e8582f
    role: context
  - path: pages/traits/environment/nacl_optimum_mid1.html
    sha256: e413240cb10d415aaf0f75110dfe5db4c83cf5592a5f4ae6a895fb333e55805d
    role: context
  - path: pages/traits/environment/nacl_optimum_mid2.html
    sha256: 9a87e9ca2e6e21e208b0837a1301ab884949e02c3665574dc645dcb0854ea9e3
    role: context
  - path: pages/traits/environment/nacl_range.html
    sha256: 7944f88d0c3218657f7bfa75d58b0564783785269aa418e4ad75bb1864e64f5b
    role: context
  - path: pages/traits/environment/nacl_range_high.html
    sha256: f5ef73ac36e4a610603dae7767fd121450cf4db8acaf982622e273353afd4fba
    role: context
  - path: pages/traits/environment/nacl_range_low.html
    sha256: 5aa8a16da673ed2f0208df91d2c43e327df64a57dfcdf62f1d6ca2ac1da326cd
    role: context
  - path: pages/traits/environment/nacl_range_mid1.html
    sha256: 9b0ab1444a3d7997fe0884d631efe43635775c4209dac433a8ad5c0ed1829ff9
    role: context
  - path: pages/traits/environment/nacl_range_mid2.html
    sha256: daa574969938e4aa9cc840ae8d3d488e3180afc3621ea66c4ac1f76557db2e7b
    role: context
  - path: pages/traits/environment/neutrophilic.html
    sha256: 71998caa3fb9c220147aaa25480f85658c4433ec333a1ac8adefcea1856227a5
    role: context
  - path: pages/traits/environment/non_halophilic.html
    sha256: f67cda4772d80fbd1b375a3790de0bdcd5be84cbfc8915b78d1b57a3815ab1fa
    role: context
  - path: pages/traits/environment/obligately_acidophilic.html
    sha256: 52c2626b4c2f8221083f7e075fe2c69a99d1cb4fb97d0de295fc9603c7eb280e
    role: context
  - path: pages/traits/environment/obligately_aerobic.html
    sha256: b9b534aa7a0591f54758084187666a8e7490f8c1bb958a4892fabcc2543dad6f
    role: context
  - path: pages/traits/environment/obligately_alkaphilic.html
    sha256: 87a6d369f611912257d722652bca4fbf5c36759125b569b92d978c0f4d77c71c
    role: context
  - path: pages/traits/environment/obligately_anaerobic.html
    sha256: 33c47c67c7352c40204bf5009698c0fd468ff73b47890cfa1e26e951a4bb50e7
    role: context
  - path: pages/traits/environment/obligately_piezophilic.html
    sha256: 818ab99cf21532854ebd90243ac1b9e5a1101af2f366bf7c8682f8952b4302bb
    role: context
  - path: pages/traits/environment/optimum_phenotype_with_numerical_limits.html
    sha256: 0b23973de37c954c386688bb5d2b6a15a60bc9cbe1d38dc69f149f4be2c94667
    role: context
  - path: pages/traits/environment/oxygen_preference.html
    sha256: 388a5c764cfaed7adbf9c08a36b76cd177e8762f270d9d7176acd6b2ecbe1ca6
    role: context
  - path: pages/traits/environment/ph_delta.html
    sha256: 91db39a5ac6f565ba9e0107a9cf7d9a00aee8e1dfdcd7ce1716fb12d36b862f4
    role: context
  - path: pages/traits/environment/ph_delta_high.html
    sha256: f1aa00a38b133f467e5670a3cca9490c10b05e839355db9205ca227abfdce2d9
    role: context
  - path: pages/traits/environment/ph_delta_low.html
    sha256: 5e5c879d01f148264814a851d8fc9a0564aaca9cd023200ac721e55701bf3628
    role: context
  - path: pages/traits/environment/ph_delta_mid1.html
    sha256: 5d369f8e851d5c1097dff313db3f2d02ea7e99f986fe5a636d2cbd298e17c291
    role: context
  - path: pages/traits/environment/ph_delta_mid2.html
    sha256: 5dd27efb7829e6e7e2f9f1d07ecc51431673800b6ed7d9c74f7f049e83e4787d
    role: context
  - path: pages/traits/environment/ph_delta_mid3.html
    sha256: fb999a99bca45714980f0e9413d9ea7cc20b979783ce4921d20e7b0baff04db3
    role: context
  - path: pages/traits/environment/ph_delta_very_low.html
    sha256: e8e2af06f5a3da023cb1342b89c1b3297544baa12e28ddc820651e565c3a4feb
    role: context
  - path: pages/traits/environment/ph_growth_preference.html
    sha256: 8825aad45c47170b6cf7c1656ff225c6095c6537c9657e9284917a2e13464fd4
    role: context
  - path: pages/traits/environment/ph_optimum.html
    sha256: 9ac7624ebb8ae97a6bc337b7717d2b9d9d5f25fd1daa96a894ed495dbbb8bc76
    role: context
  - path: pages/traits/environment/ph_optimum_high.html
    sha256: a7fa883144f20ae744390db0d02088ec54f895bb683911a790d2f9a764d55d7d
    role: context
  - path: pages/traits/environment/ph_optimum_low.html
    sha256: 174b7ab011c0845b138558329ecd70ffc42e6e87ca071eb397f582dfdcc06d07
    role: context
  - path: pages/traits/environment/ph_optimum_mid1.html
    sha256: 162d133691c991a4e3946621a959e9d6c94afb8b83c683bffeae07621d0fb737
    role: context
  - path: pages/traits/environment/ph_optimum_mid2.html
    sha256: 131834f8adfed86cb6de76bb5be1d4b89cc5682634829c7e7511475468f8e07b
    role: context
  - path: pages/traits/environment/ph_phenotype_with_numerical_limits.html
    sha256: 0baab2140a0f1473dc1b04d4c89ac46cbbfea524bb41e12f9bf8098ffa81148e
    role: context
  - path: pages/traits/environment/ph_range.html
    sha256: c3a1ecacb2914ab0a31bda5bb4c34bc11644b8fbd09a710a9f9fb99ad8e1bd78
    role: context
  - path: pages/traits/environment/ph_range_high.html
    sha256: 9947d094a3abf935e2a1eda0ceaaa718216049abcf7d4c9f555e44a5ec643ccc
    role: context
  - path: pages/traits/environment/ph_range_low.html
    sha256: 93ef81b388f76703cea8891c4d0f66c995202f69094504cd688141c38f7df044
    role: context
  - path: pages/traits/environment/ph_range_mid1.html
    sha256: 758aed0ec76f905ead7662c092383d5181470acac6bcbef821d4963e4ff8e2cb
    role: context
  - path: pages/traits/environment/ph_range_mid2.html
    sha256: 4eacd18e5b7f2fb09fb091568d2d33e7178d34dbeae15813fd33e0ceeb36218a
    role: context
  - path: pages/traits/environment/ph_range_mid3.html
    sha256: 771cca2d681162aa129ce3643e0f7dfd981fae6e907bcad74cbf8e3529eddd57
    role: context
  - path: pages/traits/environment/ph_range_very_low.html
    sha256: aea24a8b5a83ff3113c6199b7a5b4a7a3c042d7ccff22c740143e1757f27b61b
    role: context
  - path: pages/traits/environment/piezophilic.html
    sha256: 6aa950f3cb5401ed62b64a540c7aab06301f5c8d31dd3e18b0637f1887e8ef4d
    role: context
  - path: pages/traits/environment/piezotolerant.html
    sha256: 0e488aa0aa9073d6188c979ab5b804cc43b03f5c337c52435c32ae3d48dd1324
    role: context
  - path: pages/traits/environment/pressure_delta.html
    sha256: 46b0c56f754b4c12b80015f86d5218b7bcb8723de1ee71f3818524f597002be5
    role: context
  - path: pages/traits/environment/pressure_optimum.html
    sha256: 5f40c57cef8a547537805b524b2d1a3227c37d932a7c1313ec37885b2197ba40
    role: context
  - path: pages/traits/environment/pressure_range.html
    sha256: 4c43dea61e5618ea813ba430ee10476ad21df7cf09370123e1449a3fc67c8646
    role: context
  - path: pages/traits/environment/psychrophilic.html
    sha256: 7c5f080c161ae09e56c29e1743ea1566a212c50beaffc1ed9c029c9d5303332f
    role: context
  - path: pages/traits/environment/psychrotolerant.html
    sha256: 38a9debbbf800139d6e68e7395386ab19a3247284c6c0c5c0b8455ea6d36474f
    role: context
  - path: pages/traits/environment/radiotolerant.html
    sha256: 343edb828f0da44e29efe4ca178688a0c6939203afcab9a6dc7c4e6a347ac6b0
    role: context
  - path: pages/traits/environment/salinity_phenotype_with_numerical_limits.html
    sha256: 8b1f1660a375312ff78a017ce9d8dbb70e593df086063674dfca527c6a67136d
    role: context
  - path: pages/traits/environment/slightly_halophilic.html
    sha256: f1e6d028ff518b932b0cb0ba03c76e64fffd658bfbed306258fcfa17e016cfaa
    role: context
  - path: pages/traits/environment/stenohaline.html
    sha256: 151f7f6f552eb705a71bf4a12cc3962c99bec9181adbe8c56206093c7e47eeed
    role: context
  - path: pages/traits/environment/strictly_anaerobic.html
    sha256: 7b064f831da4b0a1588a16766c89984db84484a5c060fa77cb8eee27f5e2725f
    role: context
  - path: pages/traits/environment/temperature_delta.html
    sha256: 7b3d5ab3542bd5dc8246ed560be8d27d01552fb1ceadf61362719eb533f43f3e
    role: context
  - path: pages/traits/environment/temperature_delta_high.html
    sha256: 852257b387bdfe14b7ca570e173cd917fb49aa0434b7e53e95f62ca2c1189f59
    role: context
  - path: pages/traits/environment/temperature_delta_low.html
    sha256: 8b5a34182e24cb2e3e771b767b54965bffb2c43282459adf53f673dd4142e65d
    role: context
  - path: pages/traits/environment/temperature_delta_mid1.html
    sha256: 7655f5e6b910bfe4ad8292f42dbc263e3aac301d82104910a8f89bb17b5f206a
    role: context
  - path: pages/traits/environment/temperature_delta_mid2.html
    sha256: fac84d7821765adb6cafd62e3e25f93a72816a9f6efa7c221a139c231d3508b4
    role: context
  - path: pages/traits/environment/temperature_delta_very_low.html
    sha256: 08cfba73c9139a1be373b3b0e936bf15d888fad28c97126665ed278e3814644f
    role: context
  - path: pages/traits/environment/temperature_optimum.html
    sha256: 5d6ab263271a059269f77fc8a79e4e3857963ea940278e943e375cf678f00b12
    role: context
  - path: pages/traits/environment/temperature_optimum_high.html
    sha256: ac5f001b4341d2f879d953a6a0d676156f40b5b1a7b131f6acbe9bf83ebc7845
    role: context
  - path: pages/traits/environment/temperature_optimum_low.html
    sha256: 0947e3e18848100491005e6e532506ac5a59184ed2766650170653079cb47ae2
    role: context
  - path: pages/traits/environment/temperature_optimum_mid1.html
    sha256: 22d10c5beb9b6625acfe09eaef8f77722d811d11b77dc59a46cfde12ec09270a
    role: context
  - path: pages/traits/environment/temperature_optimum_mid2.html
    sha256: 462ca2185b81cf9f9e034900318319d3ecd0f6c2e524d83e6b65448ac2ae83f0
    role: context
  - path: pages/traits/environment/temperature_optimum_mid3.html
    sha256: 86d52946cd4ad43d1f77491dd803814f3f9059e469bce55df07cf6fe832d423e
    role: context
  - path: pages/traits/environment/temperature_optimum_mid4.html
    sha256: 9ecb5a2404c1e89982674ad7b4ca40a6793a026fb97fa3cdc8725690ef3e4f8f
    role: context
  - path: pages/traits/environment/temperature_optimum_very_low.html
    sha256: b0ecef5d140034b3e739830ab137259b09ef6eb520f80d3ef10b150c003e0683
    role: context
  - path: pages/traits/environment/temperature_phenotype_with_numerical_limits.html
    sha256: 6a3923d675e5827ec244703949b61387f24418aaf02de2ed31d2c30bec7e9eb9
    role: context
  - path: pages/traits/environment/temperature_preference.html
    sha256: 41d5f1241848d65226d2b927f6f3222ed9318b4df0d00eadc647cb2acf7845d5
    role: context
  - path: pages/traits/environment/temperature_range.html
    sha256: 82b71cfbfd2b5653332c814eae6786a23a81d7e815698ba287f00a65ab77864d
    role: context
  - path: pages/traits/environment/temperature_range_high.html
    sha256: d98c203de8e5ffdfaef77a4b09e5f727a0fe7f5d7a3af21e4de1c554c81422ad
    role: context
  - path: pages/traits/environment/temperature_range_low.html
    sha256: a7186cbc9463cc56f65f2ef7277e9da78990459280f3a420a9f37c987d3a6cd6
    role: context
  - path: pages/traits/environment/temperature_range_mid1.html
    sha256: 6b0dc144a063b0f1794e34f5c4a75bc10854a23afb6bc20dd7e7a8d47fb1b418
    role: context
  - path: pages/traits/environment/temperature_range_mid2.html
    sha256: f968dbb93edd6ea782a1726717cdd08c4899032f9babcc7723d80f128c8721ad
    role: context
  - path: pages/traits/environment/temperature_range_mid3.html
    sha256: 2c524ae745cf426ba6b519b99205c0e94e9b49e42384ac1e01e1121e3713631c
    role: context
  - path: pages/traits/environment/temperature_range_mid4.html
    sha256: 7fdd42583f73e9730b8ac9ad075817135f66f13900d40bfc6f70315d2dece584
    role: context
  - path: pages/traits/environment/temperature_range_very_low.html
    sha256: d54b6b69f158ad2948e18b4a651fdf5fb19f09b45d43ad1e6f8a0d87596f54b5
    role: context
  - path: pages/traits/environment/thermophilic.html
    sha256: c651e01865250b1128f8b4e5c8aee178465bee2d0e5f9dc4cbed7a1720aca110
    role: context
  - path: pages/traits/environment/thermotolerant.html
    sha256: 919b30e267a261581959fac9e4a03647ba74fbe89439e034d49c9a3299c90c6e
    role: context
  - path: pages/traits/environment/uv_radiation_tolerant.html
    sha256: aca415157dc72d1cecf946053ebf6fcf44227884151639237744ecb39c9c4961
    role: context
  - path: pages/traits/environment/xerophilic.html
    sha256: 98bb4b38c4b26b0002b315bc7e27b32eafa50eb14aa87d8ae4c3a7e606a46a5d
    role: context
  - path: pages/traits/environment/zinc_tolerant.html
    sha256: 0a5acbb9cacb6a8335f14837be52ded0f8445c24e38d3de7197e96f7aa6fd56e
    role: context
  - path: pages/traits/genomics/abi2_system.html
    sha256: 2f1eb5427407c5d94c36ebcd01a90f4a645d7c928503c61d2ef026b966f37f91
    role: context
  - path: pages/traits/genomics/abia_system.html
    sha256: f5a8a9e581e3714f5926a382fb22a9dbcbc5e6281222ca1ce038195af2cf620e
    role: context
  - path: pages/traits/genomics/abialpha_system.html
    sha256: 68dc3d1f5e03854899deff3dd2d7ba4f9f4ee4a30c786d26f5112586c6e7f32e
    role: context
  - path: pages/traits/genomics/abib_system.html
    sha256: 0b321e5a8c32995d5e813f14a6cd629332386efefc4f0b8c02475ea10f0c8fc8
    role: context
  - path: pages/traits/genomics/abic_system.html
    sha256: 1e6d6877bbfd654639b2712e2f638af25612ea7a3bb8d225b7e7aba965960626
    role: context
  - path: pages/traits/genomics/abid_system.html
    sha256: d31312996b1432eb577cd0b60a44a734ff56c1f11cb82dc3513f43fc669cf7df
    role: context
  - path: pages/traits/genomics/abie_system.html
    sha256: d365933e37aea9350748eb850bb3919c4af1f735e00e69353217d650048da833
    role: context
  - path: pages/traits/genomics/abif_system.html
    sha256: d84ac07b77867fa625d477467fe13545148466ac677f5b80759aa3610ff32b19
    role: context
  - path: pages/traits/genomics/abig_system.html
    sha256: c5eb93c363d67bd6f68344807368127adc74fbc5255a167f0d1b4843d8c1523b
    role: context
  - path: pages/traits/genomics/abih_system.html
    sha256: 23205c4d420367f79c67d74b53cd689fa06e3c6b14cc208780f28f201f683010
    role: context
  - path: pages/traits/genomics/abii_system.html
    sha256: d92618ccc9801e31beab77fb98c4add415db9fc9cbe2f5155a4558bef5cdb029
    role: context
  - path: pages/traits/genomics/abij_system.html
    sha256: 6c3f52fc2b55b60073b40ecd7c657bbcf24c3b96f183a9dc600020fd38d76c38
    role: context
  - path: pages/traits/genomics/abik_system.html
    sha256: 8ac49e8307816967cd95cb23479b25e5ddb27f3c0c01df4cfa3f48e7f1a51866
    role: context
  - path: pages/traits/genomics/abil_system.html
    sha256: aa04cf4f7e6b96caf115c2f3a9d51ec7405c5b98742c163b63647ec57ba965f6
    role: context
  - path: pages/traits/genomics/abin_system.html
    sha256: 33ea5c4f43b781cdc95a0533c3bb33d0acff6d437db908ed6a6313dc3c32fff1
    role: context
  - path: pages/traits/genomics/abio_system.html
    sha256: aff737fe2f45d7e95bbf0ba38907376ede7319fc4c7d7c85739f03bf25d39b1a
    role: context
  - path: pages/traits/genomics/abip2_system.html
    sha256: 8ca91075b85d77bfae76b09c5c93d04ad821243b5d9cb335973871d146adfc1d
    role: context
  - path: pages/traits/genomics/abiq_system.html
    sha256: f2f7792f02227357ddc44d102096a722a723b93b9a4d230da0710020f1664aaa
    role: context
  - path: pages/traits/genomics/abir_system.html
    sha256: fa8f6c783ece33bf2a82a535a8c41e08c053531e016c8cbb5ace8b177aa6078d
    role: context
  - path: pages/traits/genomics/abit_system.html
    sha256: 31365476f1fcb8ea25922a819fa862d42afe9b68290381df06186edd21db19ce
    role: context
  - path: pages/traits/genomics/abiu_system.html
    sha256: 7f79a9dc9838305742cd6a065e6d641f00d9fcec2472f890cc0da46c0e7b8c34
    role: context
  - path: pages/traits/genomics/abiv_system.html
    sha256: 9f1f5768f678a2d5954d69754e749d3e5b4eb7c326bec79c39d3301e922f85b6
    role: context
  - path: pages/traits/genomics/abiz_system.html
    sha256: ae8425f656dfdccd5afd6b6e3d220c86ead061901edcc87f0bbd5250c5eebb51
    role: context
  - path: pages/traits/genomics/abortive_infection_system.html
    sha256: fc373a125712874ff6208bc938d05bc26f20303a830d6f82d21c62f39ab8bf06
    role: context
  - path: pages/traits/genomics/aditi_system.html
    sha256: dfc71972bda08ec2e5e31f68c754849a6a085984cfe914ae1f8cfd4feb099fa2
    role: context
  - path: pages/traits/genomics/ambrosia_system.html
    sha256: 827e481df83e6a2dd6d32fb66ae5d804ae019482dfaaffdebb45af9f1fbdd036
    role: context
  - path: pages/traits/genomics/apsab_system.html
    sha256: fe7aab3449329b43c93df41522aa633c220324659432360566929a4c93532b8d
    role: context
  - path: pages/traits/genomics/aristaios_system.html
    sha256: 005cc455c9578264db6c0b561472ef5ae602eadd6fa38b269f83995930c2f369
    role: context
  - path: pages/traits/genomics/armada_system.html
    sha256: 59b7119e513b8881933a804f2f7b61bf5e5850011c04f76c3a09bab56dc32f8d
    role: context
  - path: pages/traits/genomics/audmula_system.html
    sha256: fc6c174c7f05a9849fadf99cdfdc5d28ed01d8146df498c10fa0d60dc637e244
    role: context
  - path: pages/traits/genomics/avast_system.html
    sha256: 43f75f7873e09ea4970dcfc1122e614d3b3b6138c864486246aab66e1c24c46e
    role: context
  - path: pages/traits/genomics/avs_i_system.html
    sha256: 061ca1331085f4564b2375d66f1eab09a2dc71cb67563da5321dac86a0c68793
    role: context
  - path: pages/traits/genomics/avs_ii_system.html
    sha256: 664bb1a4c8f1928b805ecdbc8d2461f9a2e71c40b1a3671a715b378eabb291eb
    role: context
  - path: pages/traits/genomics/avs_iii_system.html
    sha256: 48a64a0dadd85a2412d9d9c30edc5d70afbcaa64cee6d690d8085d331eaacdf0
    role: context
  - path: pages/traits/genomics/avs_iv_system.html
    sha256: 9bbbf4829dc4d1fef52fe5f98d59670f561a5f9e817f73029fcb8dba768feffc
    role: context
  - path: pages/traits/genomics/avs_v_system.html
    sha256: ff65aa97d2b8b52540bc308149ea7aca69195f61f176dbf9b0293f30fbf85ca9
    role: context
  - path: pages/traits/genomics/azaca_system.html
    sha256: aa3bd6d02dbdf0fee8985cdfa1855ce4c9e5be360dcbbf293b8442fd399370fe
    role: context
  - path: pages/traits/genomics/belenos_system.html
    sha256: f8e6822a9df21f4f8a5f755bde1579e52f5e12d8c9ba89049a01bfdf9c4cb440
    role: context
  - path: pages/traits/genomics/belisama_system.html
    sha256: 233fb0c88f3f5091d733893b2f8b000be78561fc1eb268bcbd115e55cbe85734
    role: context
  - path: pages/traits/genomics/bil_system.html
    sha256: 2623a82a14d9d0d72548e12e5909f32d1a00d28e794b0f1d816af7579f7cc5dc
    role: context
  - path: pages/traits/genomics/borvo_system.html
    sha256: 78f622f6b4eef9dd682433ea80d303257a973cef1fdf93df20dfe2e1fb587683
    role: context
  - path: pages/traits/genomics/brc113_system.html
    sha256: 80c47ab6121f837d22a7df57b5c2d6b0bbca21e8b8e7bd4af4853550fb8005cd
    role: context
  - path: pages/traits/genomics/brc142_system.html
    sha256: afbe90c40166350f142dd4342dfd3a51696f5364eec6aa809666a9ce1d6ebe37
    role: context
  - path: pages/traits/genomics/brc167_system.html
    sha256: ee7aca079098a0e55ccab28e9724c2e973cfe82d350b704967061931c200905f
    role: context
  - path: pages/traits/genomics/brc217_system.html
    sha256: 70581afb70d485ea10be6e31939ba5c752783f7996789ede6b159e8def9478b0
    role: context
  - path: pages/traits/genomics/brc22_system.html
    sha256: cea54106f4930313d2902d64a1848ff141afc7e133bd3930a89a25fda5c98118
    role: context
  - path: pages/traits/genomics/brc233_system.html
    sha256: a9af6668fd8448217c1c7bae829419acca4cdc9b823dfc571188000454fdd125
    role: context
  - path: pages/traits/genomics/brc23_system.html
    sha256: d73829b5c69a653ea35e84709ee8bb2fe291764f6c1b6d16019a8406685c7839
    role: context
  - path: pages/traits/genomics/brc24_system.html
    sha256: be72a630aa196727db232c191cfbc084fbc41a1e600f5db89c4c97eb73402403
    role: context
  - path: pages/traits/genomics/brc59_system.html
    sha256: df08cd12e5e4d0b58031151fcac458e0b8d6f41616faa50ae2f394fb5f0b0002
    role: context
  - path: pages/traits/genomics/brc76_system.html
    sha256: f7c002cc1ba6dbffd56d9a4eb9c8e18eaffd07b54d56f52a05a2941c11f5a0a4
    role: context
  - path: pages/traits/genomics/brcwgs21_system.html
    sha256: 0179cad5b8fb7e32021152e473b7721fa5a2ad9229c05a971d1918d18bda49d6
    role: context
  - path: pages/traits/genomics/brex_system.html
    sha256: 225fff66019c72606fe947a807ac7fce022358afe15d1a3c6361143e2618306d
    role: context
  - path: pages/traits/genomics/brig1_system.html
    sha256: ce379bd1b6aaaebed20a665451b17e4091e602e33914ab40457ce84ff57884bd
    role: context
  - path: pages/traits/genomics/brigantia_system.html
    sha256: dd9683e6125c8eabccc4bd03cb572d9178b69a9cf7cb4e40f10f1f42cec796ef
    role: context
  - path: pages/traits/genomics/bsta_system.html
    sha256: 0c26a4b83aa826f64411897ecc3d2cb3c9621b29b0e1119b19fbf6af7ae402fd
    role: context
  - path: pages/traits/genomics/bunzi_system.html
    sha256: 7d23d5e85d715a4b6382cfb2e2df3a9a980da2e576997427bbc64c4cfec98a29
    role: context
  - path: pages/traits/genomics/butters_gp30_gp31_system.html
    sha256: e7a2bcb4dc527015346d17f0d63603811eb2b9d70d1783e7d2efaaa8609c3189
    role: context
  - path: pages/traits/genomics/butters_gp57r_system.html
    sha256: b09a5c675dec9379f925d133237c65720df217d15563b428d689c9d455528394
    role: context
  - path: pages/traits/genomics/caprel_system.html
    sha256: ba02927ebeb9fab11625d84ba280d56abe4c802a06b0b74b9508b8a997cf709f
    role: context
  - path: pages/traits/genomics/card_nlr_endonuclease_system.html
    sha256: 14926463ed63b624d8e0624789dd95dd952df034a5396d8b8846c1324f4fa383
    role: context
  - path: pages/traits/genomics/card_nlr_gasdermin_system.html
    sha256: a4250588556fb5463d03525c9aef3882b8c595a3e2db27c84094c00d20e66dde
    role: context
  - path: pages/traits/genomics/card_nlr_like_system.html
    sha256: eea7a50794451a796a04e274646f7bd829a98ae905191286cdade4d1c959ed38
    role: context
  - path: pages/traits/genomics/card_nlr_phospho_system.html
    sha256: a31d53c88e87860d43fd4e679fba36ab8b261155412a5a96c80a0e4ce5135d2d
    role: context
  - path: pages/traits/genomics/card_nlr_subtilase_system.html
    sha256: 77762b435cecf78d0f16e1091d5dd5255666330d2e4399a74dd4b0082f3aa939
    role: context
  - path: pages/traits/genomics/card_nlr_system.html
    sha256: 85536bc9675bd5129a0dd30249d7ad828c9480a52138e370a13c0212ef4d268b
    role: context
  - path: pages/traits/genomics/cbass_system.html
    sha256: 589f5df5b63f9ce15e33fc7212b91f4c8d9d3b55f9a5e0c5f25239afe47df8bf
    role: context
  - path: pages/traits/genomics/ceres_system.html
    sha256: 867e56fa0aa1235cc2804cea9f268bfb0b3dbbad2e042cbf5b62bdc9a6a3517c
    role: context
  - path: pages/traits/genomics/cernunnos_system.html
    sha256: 1e0510308f5736e35b62aae2c968a38421823338c8f7c49c32df52ce5c080460
    role: context
  - path: pages/traits/genomics/charlie_gp32_system.html
    sha256: 1b7c32504495232aec2144b14df2635bf342a8855449086da2cbb9870443b5c3
    role: context
  - path: pages/traits/genomics/clover_system.html
    sha256: 9504be3ebcbcd29e563870433dd26b4cceee1ded9e594362770bf9ff458dfbcd
    role: context
  - path: pages/traits/genomics/cmdtac_system.html
    sha256: e44f716e7ffdf3e93b20be4d14bd2b54bef0758d812e2b9dd7a79d7950d8a4f1
    role: context
  - path: pages/traits/genomics/coconut_system.html
    sha256: 8bd35a87b4728b02a8efc56a84855a903d96bf0470f3a51e693db695338c73e0
    role: context
  - path: pages/traits/genomics/codon_usage_bias.html
    sha256: bb60f1a2795d09dabf923ae85344d59c204f4c1c9c9aebcafafe86b15e710198
    role: context
  - path: pages/traits/genomics/crispr_cas_system.html
    sha256: a5ad3de99888283d49bca17388771ab6f8f78775e2b05c615960afd2d0ca4654
    role: context
  - path: pages/traits/genomics/crouga_system.html
    sha256: d37abcdeb42210ea14a6562f741271330e3271b596771b7718081836a74f85cf
    role: context
  - path: pages/traits/genomics/dag_system.html
    sha256: 7d491ebb1b9dce3c40262e5144e2697ed02850e2ecef5bd5b413bc4ffebe64d6
    role: context
  - path: pages/traits/genomics/damona_system.html
    sha256: e53c2329f5604427f3932e9ffd207ed857b3b61faeed68f728b46dd9c14026dc
    role: context
  - path: pages/traits/genomics/darna_system.html
    sha256: dcacc410edcd06d9fd4b4dd39553a4e281c3410cbe1ce9a50fbab3bada44baf8
    role: context
  - path: pages/traits/genomics/dartg_system.html
    sha256: 66631a3ff025a9b54a78d2db96d8f8ddae16b33305c92cced584c4ad60bc3fb2
    role: context
  - path: pages/traits/genomics/dazbog_system.html
    sha256: 76088a99aacf8a1e355b2fffd5cb2ab26e76112f95da7182612f7600ffc3ad21
    role: context
  - path: pages/traits/genomics/dctpdeaminase_system.html
    sha256: d5d912777846e048ed82539633ebbda6170f0bb3d119fcfbc718055160fa965f
    role: context
  - path: pages/traits/genomics/ddmde_system.html
    sha256: 205b617b450ff947d0d391adfbd1ee61da49b20ef13702d079a1e5b7fa08241a
    role: context
  - path: pages/traits/genomics/detocs_system.html
    sha256: c17f8f925611014c165ed18d752e39756e52dc9a67cbd657b6d7ff2325e41cf4
    role: context
  - path: pages/traits/genomics/dgtpase_system.html
    sha256: 03a280c4053f4bf9dc8936cd0bfd9cf96f0f84a6eceaba0cae5191fa9ae9f521
    role: context
  - path: pages/traits/genomics/dionysus_system.html
    sha256: b636716fcf152c56777794fd0179e3f4f44065489885f125e5f0044306c7fa6b
    role: context
  - path: pages/traits/genomics/disarm1_system.html
    sha256: 18ac3572c609b8184059d7e6c7efbe80d7ea0e3610e38ad9a85ffc932383122e
    role: context
  - path: pages/traits/genomics/disarm2_system.html
    sha256: 3b8c968c922cf79cd18f6eba5fc4a2e698a5db4bd6a5e19c338b6408e91f185b
    role: context
  - path: pages/traits/genomics/disarm_system.html
    sha256: 1700fa5d89ad230a7d48ee5279fa96b667cdb7b9b99a46b45004094706f1ba78
    role: context
  - path: pages/traits/genomics/divona_system.html
    sha256: f8a834fc1cc4304a82ea6192db99226d3bd2610f5f96efd6a9a147cd7c445264
    role: context
  - path: pages/traits/genomics/dnd_system.html
    sha256: e28768b7013bfd4e37d02841bcac8786b49967bcb290831bfa601c80ffb12cab
    role: context
  - path: pages/traits/genomics/dndcdea_pbeabcd_system.html
    sha256: 3b2caadeb13f2b194d42c0c6fd6a67694b248435e120244814907dd0bb1958bf
    role: context
  - path: pages/traits/genomics/dodola_system.html
    sha256: 572c629f66f837ef836f39ec4d2bdecef16d22cb837242ee4c47b48093d8988c
    role: context
  - path: pages/traits/genomics/dpd_system.html
    sha256: f913f4276ee37df3f4a70b425b3a55f49b9d927f8c688f92cabf0f6cf13ff4c2
    role: context
  - path: pages/traits/genomics/drt1_system.html
    sha256: bbca7f1e678cd3e27aef2bddd25470e324730ddb78d7503297e1152a396a3841
    role: context
  - path: pages/traits/genomics/drt2_system.html
    sha256: 0c721288127360e7f1559a712a6812508522586017af5ed988f7c7c93381f67f
    role: context
  - path: pages/traits/genomics/drt3_system.html
    sha256: 86bca32f25dd7aa6a4bcbee6f25fcec88d052a87ae63245d70e436e47988b695
    role: context
  - path: pages/traits/genomics/drt4_system.html
    sha256: ee9cfae0b5361fa49ca54eb1ddff0eeaed0ea3d0a8fc2fe1eb5c15c804cb4c36
    role: context
  - path: pages/traits/genomics/drt5_system.html
    sha256: fa38f141d0e574acb17917843d3268da2f7ccd40704c88ee3a2190c4871192bf
    role: context
  - path: pages/traits/genomics/drt6_system.html
    sha256: f6fdc378dd88503a771775380899384694ed66cd24cb0475e364866b37619d29
    role: context
  - path: pages/traits/genomics/drt7_system.html
    sha256: 73d0c4d115aea7a838490c5ab67362c082633f43c99ab7db23467d0c74ae1860
    role: context
  - path: pages/traits/genomics/drt8_system.html
    sha256: de856a1d16aa29cfefba4694dd30cccb3b17f4f4556ce032155e57f35c8b920e
    role: context
  - path: pages/traits/genomics/drt9_system.html
    sha256: dfc2c7d7ff545a37c75171e09ab6d3da85bd96280c1287b30aa4fd359144ab2c
    role: context
  - path: pages/traits/genomics/drt_system.html
    sha256: 3a904ce3d04b5d1206c426bebc287df5f20ebdf709fa9048e601a41bd5ea3df1
    role: context
  - path: pages/traits/genomics/druantia_iii_system.html
    sha256: 165f580417bcff294f25e7b00fcd105fd676211ff6326c9c146dc544ac6fb299
    role: context
  - path: pages/traits/genomics/druantia_system.html
    sha256: a3da7aa57351deb4df42f50a6ea9f4e6069f9d9c833de473d8d00b9603c1cd0b
    role: context
  - path: pages/traits/genomics/druantia_type_i_system.html
    sha256: 76e54abf794c1c77496a79453cba5fc0b9f57dbe1e114a299c2b78a4a2f669dd
    role: context
  - path: pages/traits/genomics/druantia_type_ii_system.html
    sha256: 879792108d40a373e8c0811f6faa58e0026d99aecb768e75d4fcf5f0dfc14459
    role: context
  - path: pages/traits/genomics/druantia_type_iv_system.html
    sha256: 3751c7fa933715f50d1b8c80b8882a7f4c6163d0283f99535d4d9d534007a4ea
    role: context
  - path: pages/traits/genomics/ds_10_system.html
    sha256: 5aa45bd6d6949f9bcefc40325e61eb3f287cbeefd63478dd5da4dc6eb3938f49
    role: context
  - path: pages/traits/genomics/ds_11_system.html
    sha256: cc179c327ecf12722fc0f31b1f799552362c484637b9a1597ce9ffed69903a7b
    role: context
  - path: pages/traits/genomics/ds_12_system.html
    sha256: adeb13b5a3e4ca2aa9a927bd8f2f855b53c57def5c09ae30a45385d412c86250
    role: context
  - path: pages/traits/genomics/ds_13_system.html
    sha256: eba85cc6bdddf0bae0b8616ef3d4d9537176c935b83cd7d61495aaff0f1fef41
    role: context
  - path: pages/traits/genomics/ds_14_system.html
    sha256: 8292b1b280c84da6047387b2449bc3e4062601e21ee099beab83c6bcbb57f015
    role: context
  - path: pages/traits/genomics/ds_15_system.html
    sha256: 4d644558a164e12c31687af10795d219af8ffe8986189e69e56286d8422c8cf7
    role: context
  - path: pages/traits/genomics/ds_16_system.html
    sha256: e7ade978ef984a02ff7550e50e29f11b44ae1332c6df973114c25498688036de
    role: context
  - path: pages/traits/genomics/ds_17_system.html
    sha256: 5d83833d22dca53575b5a4db21663a1a33e02145885bbbc44ecfa89561abd72e
    role: context
  - path: pages/traits/genomics/ds_18_system.html
    sha256: 1d59c76454ba0538c17fb6855383c35a01db61cc6a9ce528cbd3031265619c76
    role: context
  - path: pages/traits/genomics/ds_19_system.html
    sha256: 7b6f6d3e737ea4351eb2e147af85067f742dd9b3ca72475d9814449c1d7fa78c
    role: context
  - path: pages/traits/genomics/ds_1_system.html
    sha256: a87ac2f6a0b3bcbd737ea79ef39a7f5584ffd58d05c166c73415780ba26fedf0
    role: context
  - path: pages/traits/genomics/ds_20_system.html
    sha256: 20cbbd92d442705ebc96f186cd4d06d59a38e4762d24f1bd19c35c35b415e2d1
    role: context
  - path: pages/traits/genomics/ds_21_system.html
    sha256: e03204d902d0091ea9ff21b073a8c5d99144b8a40eb07eee796edd6ab3d7550a
    role: context
  - path: pages/traits/genomics/ds_22_system.html
    sha256: 2ad9403e028d130573ee4909b8f9df557007703545dbe80fc1cec258dd3301a9
    role: context
  - path: pages/traits/genomics/ds_23_system.html
    sha256: 1e6a2a1aebb285dcc948352dfcc201ff9f0c4b312ef311dfc15568f7aad01dfc
    role: context
  - path: pages/traits/genomics/ds_24_system.html
    sha256: a769811b27eb35303b7df3c40f2e70f4d1b2ffb95437c7b55599781740ccf3b4
    role: context
  - path: pages/traits/genomics/ds_25_system.html
    sha256: cbfcc91c83c918c06baaf403b657a7ffe126b305556696107e3cd713bf603bb2
    role: context
  - path: pages/traits/genomics/ds_26_system.html
    sha256: 629a93c0326c566884f2788b4354f0211e7a2f82e4cb623c84f0a850b58708c5
    role: context
  - path: pages/traits/genomics/ds_27_system.html
    sha256: 009e3d1a7bc4efb7fe34e681f4ecb63d5ff34c01f3425cde1956fdee16974b15
    role: context
  - path: pages/traits/genomics/ds_28_system.html
    sha256: 77679b95058c7485aaa371178fb6f4b15aef96d440c6bb83468eb8860c85b1af
    role: context
  - path: pages/traits/genomics/ds_29_system.html
    sha256: f7020a63fd63cfdb0b8dfa269482a2927f2773e1b9d58fc57d5c5552dcdff8c7
    role: context
  - path: pages/traits/genomics/ds_2_system.html
    sha256: 5f215309e22ddccb1efd593f84c7f8589e0c896974d7307121886a7d74abf3dd
    role: context
  - path: pages/traits/genomics/ds_30_system.html
    sha256: be85f05e06a18c25b99bde6c8d564eda4a41fa673ad52b74194945e9d06b9b16
    role: context
  - path: pages/traits/genomics/ds_31_system.html
    sha256: 8b2aee14a5f7c5d3a9025fc0720b0990a5652286d4b300d134ada5a2e1ed80df
    role: context
  - path: pages/traits/genomics/ds_32_system.html
    sha256: 86dac39c47e49ed7f406c9f98c3dba39f173b0963e5c92589625eb9889662cc7
    role: context
  - path: pages/traits/genomics/ds_33_system.html
    sha256: 337cfd6a47d2c229b5e39c42722209c5560015f42053406899fca9671c5d5ead
    role: context
  - path: pages/traits/genomics/ds_34_system.html
    sha256: fb253aee57050c767e5c97dbebbb5e7b8ac3cea07b4199fce835ea3591c984ab
    role: context
  - path: pages/traits/genomics/ds_35_system.html
    sha256: 5fa2bd0f97fdd7bbb2d94f6ef4a28b812c980d93c24ccc470a696e3397f0ea47
    role: context
  - path: pages/traits/genomics/ds_36_system.html
    sha256: a0ee317a9de555f5622eed3976bee2a1c9e76eaf6cae360dedbd1da1327b347c
    role: context
  - path: pages/traits/genomics/ds_37_system.html
    sha256: dc81df8acb43259822ee0698574110118a764a1d47e0371024429c45a8914f7c
    role: context
  - path: pages/traits/genomics/ds_38_system.html
    sha256: e17933241437f069c86629737f33ac2d3348b05e9fb4b903b0163b3c16a67e2f
    role: context
  - path: pages/traits/genomics/ds_39_system.html
    sha256: 2a3602a40aa77e6c6727985e122bbcc19dd854c165bfb7f032f96aa0f2b15ed9
    role: context
  - path: pages/traits/genomics/ds_3_system.html
    sha256: c669dae96489f838c4654c14b6d4013aa92d209087cf02a9a3e2e299db76229f
    role: context
  - path: pages/traits/genomics/ds_40_system.html
    sha256: 70ed1721f01c56a3bfb40240dde8fc861711cdef2bdbc68493c1d3a191d4d7fb
    role: context
  - path: pages/traits/genomics/ds_41_system.html
    sha256: 25f2c0526b19315545fa434db309c2c9569adb5155e8de7fda69e95d7c347665
    role: context
  - path: pages/traits/genomics/ds_42_system.html
    sha256: 540b4ab2b83599be4c899d93e575af3728114351f524ac113bb39c0d39254328
    role: context
  - path: pages/traits/genomics/ds_43_system.html
    sha256: bef8fc861c50d37f665c3f802105ee77ad26a1f8b88de910ee972299094d45c1
    role: context
  - path: pages/traits/genomics/ds_44_system.html
    sha256: bfc40e0049793c85f5ae0128eafa565b4f027068787399fd6e08c9e9e252b978
    role: context
  - path: pages/traits/genomics/ds_45_system.html
    sha256: e83918a2fd1e0117a4319f51ba7eb6bb523949d1cfaf71cca959bbcbefbbfbe4
    role: context
  - path: pages/traits/genomics/ds_46_system.html
    sha256: 733eab3c2d1dd8a603b2ac1cf43a83135d7f11a0908f53df47e500a406db645d
    role: context
  - path: pages/traits/genomics/ds_4_system.html
    sha256: 4b5500f5483226a005932e16b4d1418ba21c44f525f46f6f8229663cf3c63a85
    role: context
  - path: pages/traits/genomics/ds_5_system.html
    sha256: 1397fcbb9795d0944ab1310566c12d36e4497dc1d16717eebdaad3eb123cdb8c
    role: context
  - path: pages/traits/genomics/ds_6_system.html
    sha256: 6878f90984ace3cee6c9101466a9790a3f582e374a46786cc97caced2c4a2b0d
    role: context
  - path: pages/traits/genomics/ds_7_system.html
    sha256: d198a741868f422ea89eb7a49b2d4472c781a39de3f5bdd64e016b29efce59a1
    role: context
  - path: pages/traits/genomics/ds_8_system.html
    sha256: 672d02f1bff6f6d4985ab2bccc61ef16dd4087260b6555a2efecedbf78d6af75
    role: context
  - path: pages/traits/genomics/ds_9_system.html
    sha256: d1ffcccf8ed7513dcb6c24fe947acdeb1181562220d8001eafee26722376beec
    role: context
  - path: pages/traits/genomics/dsr_system.html
    sha256: 8eb3c629e33deacf821452218198d431ea62b71aba2248a55656ca39aaaa8d98
    role: context
  - path: pages/traits/genomics/duf262_schlafen_system.html
    sha256: 225067f1ac8c0dd8a85e2e6c77578da9f499f06324b826d6ef5048c78e43e1d7
    role: context
  - path: pages/traits/genomics/ecokmcra_system.html
    sha256: ac632348a1358a59c31de08adf6f1f308db0770707291a619c47a4e267688604
    role: context
  - path: pages/traits/genomics/eleos_system.html
    sha256: 4e248e81eff18def33d2694fc39880e007da0a0e452208331836d3af664c5112
    role: context
  - path: pages/traits/genomics/endpacf1_system.html
    sha256: 520ccddeb534bb731ecd015c4f731648dfbccbf5a940c41b399d9724e9a4d402
    role: context
  - path: pages/traits/genomics/epona_system.html
    sha256: 1ba6cd815d654127100fc1b48234ebc7653a787d7d4c2bf5882ca9a9ee7e06f1
    role: context
  - path: pages/traits/genomics/erebus_system.html
    sha256: b0e354e58a79ded6d2ea3f4adfbfcb5cbdb18d1c97b446757d31f123331311ca
    role: context
  - path: pages/traits/genomics/esos_system.html
    sha256: afdf87aed148c62eb57bd92c2d33571887d35703bfa835dbceec29492aae6ebb
    role: context
  - path: pages/traits/genomics/fliodhais_system.html
    sha256: 799b4b6e83f6c609dac3f10f2d2b19a5613aaa79366c6f801b1881868b23c901
    role: context
  - path: pages/traits/genomics/fs_giy_yig_system.html
    sha256: aadb54a970a22efb48592cc87e66c952f6e3658085bd72137d05d1cde98528ad
    role: context
  - path: pages/traits/genomics/fs_hepn_tm_system.html
    sha256: 7af9968ebfb8a7b916a6e20c6bb823cf553a1e0c60ee19c61446cbe291cfcfa2
    role: context
  - path: pages/traits/genomics/fs_hp_sdh_sah_system.html
    sha256: c4c9655409f1e5daf0a3f9fe4ee90f64e805efb255a4cb5d4ae956ae4344fca0
    role: context
  - path: pages/traits/genomics/fs_hp_system.html
    sha256: 7b35c1405a8cbe5022ac735f19decd01dbad162251f831bbb9f894baa385b985
    role: context
  - path: pages/traits/genomics/fs_hsdr_like_system.html
    sha256: 6da457b501911020b4b8328ee2aef40d28ea3a7d61a8b69b86f67ec69d1d771c
    role: context
  - path: pages/traits/genomics/fs_sma_system.html
    sha256: 456bebed70a026c76f678ee29c1fa3b2aaf050829ae42a6a429485ff960b8dc1
    role: context
  - path: pages/traits/genomics/gabija_system.html
    sha256: d91dc39fbd2e73aac930a130f8c2b2ecd5e4bb86ab4415fa23d38ff302b180be
    role: context
  - path: pages/traits/genomics/gao_ape_system.html
    sha256: a1fa9f68b7f6a65e3774339a825f4c6050678dd16fa40ac465f5046432940959
    role: context
  - path: pages/traits/genomics/gao_her_duf_system.html
    sha256: 15528820570b8f221df0bd3e5c21abdd70f11671c9a75ea5bbe08fa00ac6e765
    role: context
  - path: pages/traits/genomics/gao_her_sir_system.html
    sha256: d32890566a4c2690ed3c4b2159a71cac7f271a08f756c5064bf65c5c4fc9b845
    role: context
  - path: pages/traits/genomics/gao_her_system.html
    sha256: c18aa7e750332a03bacf2c8cc05bb81b8acc77071dea5300ddc25a1c7188059c
    role: context
  - path: pages/traits/genomics/gao_hhe_system.html
    sha256: cc3b229dc8e466262a3d109fc47dde1726282f85e8c13b4a463fa4d1ee690c19
    role: context
  - path: pages/traits/genomics/gao_iet_system.html
    sha256: aebb0f5083344c6681778deae4e7e6e72a7b1bd48f5a29c3332e34014f6787fb
    role: context
  - path: pages/traits/genomics/gao_mza_system.html
    sha256: 2dde356a5518896f412a90ce4345e513ecd74dc10a204d49bf63e5e78c216248
    role: context
  - path: pages/traits/genomics/gao_ppl_system.html
    sha256: 3d341b718e0da368f407c636c5d54f14ac4390188945220f38c17449eb87c229
    role: context
  - path: pages/traits/genomics/gao_qat_system.html
    sha256: e272bd437494605b9c1dab06f0a2235dd61be3132a7a5847d50f03051bd0a665
    role: context
  - path: pages/traits/genomics/gao_rl_system.html
    sha256: 021a4fb86b247c054eecffabc7c796247600300910c75ce43adbcbefadf48ff5
    role: context
  - path: pages/traits/genomics/gao_tery_system.html
    sha256: 82748a347e546ac2cff5fc19621b22ec4efd54640daa99cb91a6f1eb8a6e498d
    role: context
  - path: pages/traits/genomics/gao_tmn_system.html
    sha256: 3e3ec64ffc59b18361e06a16009522c6971a6166f5d7260d18832aafb3ab7856
    role: context
  - path: pages/traits/genomics/gao_upx_system.html
    sha256: b98a1ee7f9e1835bd2ebcb1bc95649f8bf12acab0cf1fd3c8a8379e842844e2f
    role: context
  - path: pages/traits/genomics/gaps1_system.html
    sha256: c4709be193d352115f3d84e44353876c947bd248aeda9b5578c6a408caff170b
    role: context
  - path: pages/traits/genomics/gaps2_system.html
    sha256: 5a4c111121a19b1a74b4c6fd70b59c21ccc08b9bf77a9c4592374cf0908f9058
    role: context
  - path: pages/traits/genomics/gaps4_system.html
    sha256: b8b5e625aed3ca54c6a5ff7b7b3df138a2e1c4b5c4ddf6c1b2de5e3d6f9634a9
    role: context
  - path: pages/traits/genomics/gaps6_system.html
    sha256: a22ba80df56b6fbd184c3b37cfcfd1836ade063b2297e5da407545f990bb6889
    role: context
  - path: pages/traits/genomics/gasdermin_system.html
    sha256: c89502f3a8795fbc323d3fd838bef8569581825a9c7f7fc110081a98da2fcaa2
    role: context
  - path: pages/traits/genomics/gc_content.html
    sha256: b84a0a4b6bc8872f68bf7a79b256185a150450aa637b5cfc1d97db61f5fc6851
    role: context
  - path: pages/traits/genomics/gc_high.html
    sha256: 116e14fcf482ced9929b464e02f0d7fad9c64d55b8a4f4783a6d25f161ae5f81
    role: context
  - path: pages/traits/genomics/gc_low.html
    sha256: a1be03a5ba1592f68217f6269a66e680e9586b80e95d4385134dec20eda45b6e
    role: context
  - path: pages/traits/genomics/gc_mid1.html
    sha256: fd78ab8a83ef367db5431a2ba2dd9bc20231670260b3d0e3b40f999dc322351c
    role: context
  - path: pages/traits/genomics/gc_mid2.html
    sha256: fb7ff19b5653dc4eaf7e95b4a8d0c5af5ba9253b015fe51e6ae36a9afc1a183d
    role: context
  - path: pages/traits/genomics/gc_skew.html
    sha256: 90f9ba50e72f4321f85af635600ea933024ec67c5346bd98113eeb7db0b4d4fc
    role: context
  - path: pages/traits/genomics/geb_system.html
    sha256: 9da61f596a020b2312464070caaf82cb80f53ee98fbec04217749b2ce3aca9db
    role: context
  - path: pages/traits/genomics/genome_size.html
    sha256: 487b8f614b98a906c2ca8959c1f335d78973ab95a69f36e9f6394bff772b7af5
    role: context
  - path: pages/traits/genomics/genome_streamlining.html
    sha256: 7dd5f2dbf98fb8db245d77cfe4ecf6495ef34c2cab9e315c0d1f47b8babdeb21
    role: context
  - path: pages/traits/genomics/genomic_island.html
    sha256: 24d0e71aa91d9f40e7964d054c0111668a45f3902241e926731dcd8747778e33
    role: context
  - path: pages/traits/genomics/gmrsd_system.html
    sha256: 2c243c6aab90239c2a3b6ba1215f049dba975fc92f77b67175f2abb0e276e50c
    role: context
  - path: pages/traits/genomics/hachiman_system.html
    sha256: aa951a5391c0f9d59a6332ba4b41e0c0337343dfbfbf7ac8fcc82bdb96afbd08
    role: context
  - path: pages/traits/genomics/hachiman_type_i_system.html
    sha256: f17debdb1aa557112a3ec0f2cc44fe45a726ce9f3c5cc39c050d7191b7102d78
    role: context
  - path: pages/traits/genomics/hachiman_type_ii_system.html
    sha256: 3789dbe8c0ca968c483cf18ffee6589041565d91a0072184171381d7235299aa
    role: context
  - path: pages/traits/genomics/hailong_system.html
    sha256: 9e095eb2c2b301ba757605d804ccb5a89c7d85e8c05f86c9b09b467d97776cca
    role: context
  - path: pages/traits/genomics/hec_02_system.html
    sha256: 2357b99253048267c592acebea3c9e1773af324876bce8056b347ee70e738776
    role: context
  - path: pages/traits/genomics/hec_03_system.html
    sha256: fd4ede20d42ba5772607576c4a28c97a004032219b2807addfc26b85ffc0102d
    role: context
  - path: pages/traits/genomics/hec_04_system.html
    sha256: f54fb910b1e59394b0346f76c51cb18e624808f8677af31932bb5d1620e94372
    role: context
  - path: pages/traits/genomics/hec_05_system.html
    sha256: 77f3ef4a7ec38231f667d46c1c12cf0e512d9c67c96f42b0b349fda3fdc05986
    role: context
  - path: pages/traits/genomics/hec_06_system.html
    sha256: 74e83540094a8cf675564f46c194709ee330c3328149dd8b9aee0ba982bfa164
    role: context
  - path: pages/traits/genomics/hec_07_system.html
    sha256: 461cd9549c75247119a4bc7cf43b021c266281ae2062ba6655dff97e8081e693
    role: context
  - path: pages/traits/genomics/hec_08_system.html
    sha256: 75d1e3401d18d61f30b32b9bf309bb6f436b8546e09359bde993c283388cba16
    role: context
  - path: pages/traits/genomics/hesat_system.html
    sha256: 4f95902d6621902fc8f9be95ca6e645676b21928236c0aae26fdcc7bf03a406f
    role: context
  - path: pages/traits/genomics/heterokaryosis.html
    sha256: 16c22070e7680c6b9e5f6d73d884e5e740a96b88f7b4d8a46841fd3f3c07c0ac
    role: context
  - path: pages/traits/genomics/hma_system.html
    sha256: ff8ecb9411832f7ad3160f9aac67bd6680bb3580398b73d96b0581c2077983d7
    role: context
  - path: pages/traits/genomics/hna_system.html
    sha256: 395ab56bf2c2dff401aa57d2fb485e26354778177f9801e369ad9d9edae724ad
    role: context
  - path: pages/traits/genomics/hypnos_system.html
    sha256: 9c0790b35cc093a847f8785c5cab217059be701f3e58ae829ae95d42b8e0209c
    role: context
  - path: pages/traits/genomics/ig_like_schlafen_system.html
    sha256: 869786b609b1d065ad9e28c94b417a2cf915391a4542afac5fc579344b8ed38d
    role: context
  - path: pages/traits/genomics/integrative_conjugative_element.html
    sha256: d9843ae08568840271932d1e98741e6f8d15d77c6816b984aab13105a50fae05
    role: context
  - path: pages/traits/genomics/jukab_system.html
    sha256: cbac36c966cbb97667131f93effbd22ede29eca019f307e2d2b80500cf0f082c
    role: context
  - path: pages/traits/genomics/kamadhenu_system.html
    sha256: 38d6b869ba63b879d80577d309d9093a69b73ed02233804097c735e71cd6d17b
    role: context
  - path: pages/traits/genomics/kiwa_system.html
    sha256: 15d13671ce3f17d38333807fd3a0751902fa79462fb84ae29c869c4fce853bf8
    role: context
  - path: pages/traits/genomics/kongming_system.html
    sha256: 834b541adcab3f226766ca5fcf735368965fd91423d9e94be70c3f59566b500d
    role: context
  - path: pages/traits/genomics/lamassu_amidase_system.html
    sha256: ffc7038807924d4a77a1e0ae9deff6434c2382d7e45c94d46c65bb21193d1b82
    role: context
  - path: pages/traits/genomics/lamassu_cap4_nuclease_system.html
    sha256: 65b7025d8b77fb4f6f44f9e261351309900b39cc86014a02cf34835a926ea998
    role: context
  - path: pages/traits/genomics/lamassu_fmo_system.html
    sha256: 58a1aecfad448d06efc58dbd965a5acc205a0c6c21970dcc976b2edf6d226afe
    role: context
  - path: pages/traits/genomics/lamassu_hnh_system.html
    sha256: 73149eb9b62823fa692a217ddbc071b2bd5cccc9f3ae82597c5419b0c540e12e
    role: context
  - path: pages/traits/genomics/lamassu_hydrolase_protease_system.html
    sha256: 48e9c3cf61d1bbb25ffc92e36ade2102de756b76606805f03e8a031614ea6c7b
    role: context
  - path: pages/traits/genomics/lamassu_hydrolase_system.html
    sha256: 37d75a8e74639af3bf3f89135a3f34e4327a96bedfe01c0201eeaee4f6180ab2
    role: context
  - path: pages/traits/genomics/lamassu_lipase_system.html
    sha256: 2deb9b9afc8e75927659da74a49bef31557fc710f5a29094de1d08b559c20a48
    role: context
  - path: pages/traits/genomics/lamassu_mrr_system.html
    sha256: 24b49ac309d9c7f18ba9437464c73aa2f4c2cb5908422947fdb88965c6b1a745
    role: context
  - path: pages/traits/genomics/lamassu_pddexk_system.html
    sha256: 8e58b49895a6fec65ad0c6699cd6c1b68f38641caa7a12199eb8acee87f7c742
    role: context
  - path: pages/traits/genomics/lamassu_protease_system.html
    sha256: 42efcf6a7193e0a8ecee89f16d57bb4240358514b6d1e5a05166c9583aacda6a
    role: context
  - path: pages/traits/genomics/lamassu_sir2_system.html
    sha256: e6148652faeddb6a7a4ad2cba23585281e54c2e64988c1d900438f1e2569ad27
    role: context
  - path: pages/traits/genomics/lamassu_smek_system.html
    sha256: 4dc43d1ad5219ffab36646508b7262d480aca879dd61bcbaf9e7a6bdc4dd0b4d
    role: context
  - path: pages/traits/genomics/lamassu_system.html
    sha256: 56f202858863abfd007ffb8110addaa169f11d20524864a826d482827b562ade
    role: context
  - path: pages/traits/genomics/lamassu_type_i_system.html
    sha256: 63e0fd6a14a6f94503b511ed6f55bbbca90da0b88567c1a1d70d834ae2c32652
    role: context
  - path: pages/traits/genomics/lamassu_type_ii_system.html
    sha256: 18167cbe26ab2284aeb9fef4af4190e5937bd505e265cf459a31e1fc9d2fc5b4
    role: context
  - path: pages/traits/genomics/lanthivirin_system.html
    sha256: 077b77d47f587e560ba9b86ae4f3cf581b2bfd5e4cc324fee976288be1263048
    role: context
  - path: pages/traits/genomics/lit_system.html
    sha256: b17742c0eaafa7dc4fa36a1f0df90413a75fe1f9fb82217e6cf4490be0970437
    role: context
  - path: pages/traits/genomics/long_lamassu_system.html
    sha256: de2fff252953d95e69f269bde54f358e59990d6ad5fd811d02a64a0261986b20
    role: context
  - path: pages/traits/genomics/lugos_system.html
    sha256: 91098673e49da12dcb798d515a78d5e4dd19e50ada021dbbf6cdb9496ebbe78b
    role: context
  - path: pages/traits/genomics/mads_system.html
    sha256: 387be8a7da6da440cac3a06a285389bf50459a4bce0b4eca18be418da39b0fbf
    role: context
  - path: pages/traits/genomics/mazef_system.html
    sha256: f2b4c8085862216e5d53d1f98fbd343c5bab03be557bd4a6ce14a948f031ef73
    role: context
  - path: pages/traits/genomics/mcrbc_system.html
    sha256: 4a211872545d8e7fbc2c5b861078e1ce3f353013fba822e981aecf00fceb42c5
    role: context
  - path: pages/traits/genomics/menshen_system.html
    sha256: 364b79edb88fca74b5a86a3a5c0350b2571dc437dd3696e621f4f65ed036077a
    role: context
  - path: pages/traits/genomics/metis_system.html
    sha256: 2ab8aff487e3752d65f1593e529c2678f771c99150c29001aedc63bef14660d4
    role: context
  - path: pages/traits/genomics/mksbefg_system.html
    sha256: f1ce538c4e42edeb81aa806d0f8e6e74e3099b4d9aa6815e41fa54e070a63fb1
    role: context
  - path: pages/traits/genomics/mmb_gp29_gp30_system.html
    sha256: bfc8a9dce5271d236c10d98656b1aa6ef1aae77d670df741d55781ff84092555
    role: context
  - path: pages/traits/genomics/mobile_genetic_element.html
    sha256: 83b21d914001c78b741dc0ae9c8f01900d3d6bc8786b1406d3bf6b61735c0c66
    role: context
  - path: pages/traits/genomics/mok_hok_sok_system.html
    sha256: 9cd2291fbd162eca497fed484ea2b42768e2d65f57d7458e6db511a5b6b7918f
    role: context
  - path: pages/traits/genomics/mokosh_system.html
    sha256: 64379ba5a101bdfb6bac598d22cefba401b466242e930d3613794cce7e1168cf
    role: context
  - path: pages/traits/genomics/mqsrac_system.html
    sha256: 60670b4ca74ec147c483636712b4ebbaf8877e4aab6402cab6e1d7fb6a5dd689
    role: context
  - path: pages/traits/genomics/mspji_system.html
    sha256: 85dce0f76037e8a7e98276c68d7f0655490e788d9e6c8fd1f580cb0fc2acc049
    role: context
  - path: pages/traits/genomics/nantosuelta_system.html
    sha256: 76d2b14a4bb5e3f381204e1a4d8304a7d81961bfbfb1df3c0598195118bd5b2e
    role: context
  - path: pages/traits/genomics/nemetona_system.html
    sha256: 4697d39e2e81b38b986308febeb7099959dd392395d8cc2e4799211253405662
    role: context
  - path: pages/traits/genomics/nhi_system.html
    sha256: 28751928d9082b1d65fcb23ea9e26312cfec3eba09bba780868d196776ee9a43
    role: context
  - path: pages/traits/genomics/nixi_system.html
    sha256: adc1454531b3f348f65867cf6a2c92cbac12e1f4511c79aa18ff031ff2ad4075
    role: context
  - path: pages/traits/genomics/nlr_like_bnacht_system.html
    sha256: 06ed20eeed973859f6db3346dc8cb0fcc37d1b3ebc29aaaf1e7b11aa696b4adc
    role: context
  - path: pages/traits/genomics/ogmios_system.html
    sha256: 6ec5881e8499245c1caa4eb2fd6ced93fdc80bbcfcb234b20ec7c3e08ce3d67d
    role: context
  - path: pages/traits/genomics/old_exonuclease_system.html
    sha256: b7f416d037007de0aeaa9207b974e47149c15d57982250028d53027c9cdb4f9f
    role: context
  - path: pages/traits/genomics/olokun_system.html
    sha256: 4cdae35ede056e698a740a223fcd4c3d5dca16fa448ee33f829daed311824be9
    role: context
  - path: pages/traits/genomics/ophion_system.html
    sha256: e3cb7c94e9334a118faeef4038c6ee2db1fd76fee24cd824fbe4979db983b6c1
    role: context
  - path: pages/traits/genomics/oshun_system.html
    sha256: 41d4b530e21bc830a7fcf20ed71f2286107e55479d5a9c443f8013c47a5dbb29
    role: context
  - path: pages/traits/genomics/pago_system.html
    sha256: 3c7bf3b8c034d143dcdd6fc5536bae0d1ab19467f84766edcabe79257332e08f
    role: context
  - path: pages/traits/genomics/panchino_gp28_system.html
    sha256: bd0288edcec3c0ae2397e8b6f6906a02d5d6902fdb90fb4850bcc55aeca595e1
    role: context
  - path: pages/traits/genomics/pangenome_openness.html
    sha256: 37e05debbc4902b0519f6da8bfa9a6e15ea5014e1931b2241182140cfed39909
    role: context
  - path: pages/traits/genomics/panoptes_system.html
    sha256: 525473d423166bb5be023b63041c39306b565266dfeeaeac2207ab0ad65ce777
    role: context
  - path: pages/traits/genomics/paris_system.html
    sha256: fc17c230fdee5bf71718af8fc51d315cd0eccaeb8590e2f92449adc665fa123b
    role: context
  - path: pages/traits/genomics/pd_lambda_1_system.html
    sha256: 781fcd679fd2ddc9369263b1e2100899f7bcdc80b732302a93891877c4d6702f
    role: context
  - path: pages/traits/genomics/pd_lambda_2_system.html
    sha256: 95df7f7057c209265cf37d31eb2d449c75e3fa42bc816273dc6566b3f8dda0d7
    role: context
  - path: pages/traits/genomics/pd_lambda_3_system.html
    sha256: f33596299d6d12fa547d25261775a76a1efd111af43376e0e94d72e23326aadf
    role: context
  - path: pages/traits/genomics/pd_lambda_4_system.html
    sha256: c275071413781e3ea75a746c5a2474a00686418fa5cf944f3edc7b090591ea7a
    role: context
  - path: pages/traits/genomics/pd_lambda_5_system.html
    sha256: 0add0c074fdd682af9a31b1195da6555ea3587272713320f25b22eed795995d7
    role: context
  - path: pages/traits/genomics/pd_lambda_6_system.html
    sha256: f434d157be5096abe4f0af2b94c1b445990d6dc8a693ef6e0ed6ab4ad3c1164f
    role: context
  - path: pages/traits/genomics/pd_t2_1_system.html
    sha256: e9407a9f89625b5a1648b08fb8ab429342d7a70b554ed458c907647c2b2152e1
    role: context
  - path: pages/traits/genomics/pd_t4_10_system.html
    sha256: 6e2efebae707deec7a64b47971b6b4dc4edf97df534ee8b94db57e8544282d37
    role: context
  - path: pages/traits/genomics/pd_t4_1_system.html
    sha256: 0a62510523e3263956e0fbc05f742474c655f062d79ceb5804692439f603618f
    role: context
  - path: pages/traits/genomics/pd_t4_2_system.html
    sha256: e87c1048dd83c409430e639d51e6e9af8733a262e07cfb0ef87277b4d480c128
    role: context
  - path: pages/traits/genomics/pd_t4_3_system.html
    sha256: d9d9bf238cadc45fb3dbaf6ca887fd349dedb2ea5c53e6c8602c24bc1941f5e0
    role: context
  - path: pages/traits/genomics/pd_t4_4_system.html
    sha256: 10356054c6e92c7759e555537a64ab0b566c0aa54dd15efb7f38cdfbfcc8b8cf
    role: context
  - path: pages/traits/genomics/pd_t4_5_system.html
    sha256: 32f5f56fea4cf55167323aa64da825e3140c702f76f42731f6656af264eb61ed
    role: context
  - path: pages/traits/genomics/pd_t4_6_system.html
    sha256: 0656ab8494239ccda4bce5b7eea2be83652917e08ac8124b05aa1e38b3d3b4b3
    role: context
  - path: pages/traits/genomics/pd_t4_7_system.html
    sha256: 500065927ad560b89a5ea38d00d03c74b389cac2a834766501a2fc3b23a25513
    role: context
  - path: pages/traits/genomics/pd_t4_8_system.html
    sha256: 8ece21c7d66328e38ef91de383efa315327325f8d443bff4f4b82b82fe7cde98
    role: context
  - path: pages/traits/genomics/pd_t7_1_system.html
    sha256: f00ad6c6cbed73fe913b5e4921a2d155dd6f2be524adbdd8b7946c12ae93e257
    role: context
  - path: pages/traits/genomics/pd_t7_2_system.html
    sha256: 6b1ee842c6e5811065250e915a38a736bfbddd38b1277807162639fabe8b8e3d
    role: context
  - path: pages/traits/genomics/pd_t7_3_system.html
    sha256: 130fdfe85ea74b6078ca11b9c248be66d324d2ba31ecae8de4323412e960eec9
    role: context
  - path: pages/traits/genomics/pd_t7_4_system.html
    sha256: 7fc76bdd293b9034aad110916bf56c1eee601af0eca994ce5d8f5e7822fe435d
    role: context
  - path: pages/traits/genomics/pd_t7_5_system.html
    sha256: d38f5de4fbdce41a57f7947daad6ded2bfb2ec24fbb93b52ea220ba18e5c35e6
    role: context
  - path: pages/traits/genomics/pfiat_system.html
    sha256: 7e52d16f68043d773c9ac9f27e4c82d8aa92c8aec834e56ef3c8d61623cf5d67
    role: context
  - path: pages/traits/genomics/phage_defense_system.html
    sha256: 3beb05e73168153545423f23a1a30a16d246ba61d1ce28ca2a9b266607610aca
    role: context
  - path: pages/traits/genomics/phosphorothioate_defense_system.html
    sha256: 82ea7b1085b7fc5756676a16ed31d29a19a759dd2fa47b5faa850b057d200c57
    role: context
  - path: pages/traits/genomics/phrann_gp29_gp30_system.html
    sha256: d544f2fe074bd45aa2d6ca8ee8bc76ee91d8c8b565ee93e43e1c58d153c643c5
    role: context
  - path: pages/traits/genomics/pif_system.html
    sha256: fb893ba15a43ab7402f92d83a84c36c419be1de8786c93772890ba006757ce8f
    role: context
  - path: pages/traits/genomics/plasmid_carriage.html
    sha256: af0cde50650f9cefe2eb2d70c64d49e24b92a1880c84c5394345527d5f062171
    role: context
  - path: pages/traits/genomics/ploidy.html
    sha256: c76cce5e3f8119033e00847a273899451fbab46b915a6a4c70355ce2c302eae2
    role: context
  - path: pages/traits/genomics/prithvi_system.html
    sha256: f4f41446c4d0191f119549a296a539b91bde69593c7bbf502af5d005f932e7b3
    role: context
  - path: pages/traits/genomics/prometheus_system.html
    sha256: fafbb477b504060e735af4417aba06976621cfe6f7e8bfbbea23c029fdaf53e4
    role: context
  - path: pages/traits/genomics/prophage.html
    sha256: 9ba8ba1f996d253ffc57ffb448d0c81918bc31cc70118c55689f291f61cca2bc
    role: context
  - path: pages/traits/genomics/prrc_system.html
    sha256: 355357d91cf7a454b279549cad2bcc639f338a59a1ad34fed58e13269ae61f5c
    role: context
  - path: pages/traits/genomics/psyrta_system.html
    sha256: dc29b1e40dc6eecaeb7dae75ed70d58d3e8e6be8d47c3aff62921f8b0bed915d
    role: context
  - path: pages/traits/genomics/pvurts1i_system.html
    sha256: da4c50a368905142f0b22aafccdb494278fa531d4051c5d859ca2eebb54c1eb7
    role: context
  - path: pages/traits/genomics/pycsar_system.html
    sha256: cfc29c773653ea7cac95e172d3be71e19ccb449d0357211b4293b9ede93516c8
    role: context
  - path: pages/traits/genomics/radar_system.html
    sha256: 14e36b2d82299a7af71913ea2ff88b314a490f6ff0a1f859df4bded2b12cf3d0
    role: context
  - path: pages/traits/genomics/razr_system.html
    sha256: 3227fb070b172571c4a66549c0b06f7b7b7fb520562ce0bd8a47c9c256764f40
    role: context
  - path: pages/traits/genomics/resolvase_duf5677_system.html
    sha256: e92c4cf6c57b1825509a587d4b25fcdc2307d185c285c81adbc1d6c955e1a079
    role: context
  - path: pages/traits/genomics/resolvase_kap_ntpase_system.html
    sha256: f591935e39770700c3006b67c5233a9852c3b07fce48ed7f0149a5bdcddf0a74
    role: context
  - path: pages/traits/genomics/resolvase_schlafen_system.html
    sha256: 9d40a9f3313875edfff8c186cb31bc0c65b372e108c2ed3b199c11c0c1309697
    role: context
  - path: pages/traits/genomics/restriction_modification_system.html
    sha256: 60bf763db1cdd1fe5b6ba7bd09f9645863c0fa8b71e0aada4a014204313bd1aa
    role: context
  - path: pages/traits/genomics/retron_system.html
    sha256: 5fbc63684103d2e78f80a1fee993806a15f680d79da7223740bf2bb1748bdbfd
    role: context
  - path: pages/traits/genomics/reve_system.html
    sha256: 68ef630fb8c4d10e64b9ce19094f800df4ec24fef918a3c3fae76054d3b8e1b6
    role: context
  - path: pages/traits/genomics/rexab_system.html
    sha256: 4d50510c6b7a0b9a2e18fced8c029d9443e7ccbb2c3568b4a5826c4ea12b2eb2
    role: context
  - path: pages/traits/genomics/rhea_system.html
    sha256: 5ed280ee55735c14e41d740896f30650b7d0ccec8a92daf529b1e267ee654098
    role: context
  - path: pages/traits/genomics/rloc_system.html
    sha256: d48e55ee65e847764fb61f637dcedcbe128442abbd3f7e32d5715bc9b23601f3
    role: context
  - path: pages/traits/genomics/rnlab_system.html
    sha256: ea56f4a04caf482d1f38e4643464ee979ef3b204bd91917f335ea3c96ee8c719
    role: context
  - path: pages/traits/genomics/rosmerta_system.html
    sha256: c0804e6dc50f6bcfac8af84dfc46a96807b7b5e4d7e184b3504ca2834bbed539
    role: context
  - path: pages/traits/genomics/rrna_operon_copy_number.html
    sha256: ebc3a31201d8afde85798609ef130b9c28170473798bdd52b9b09a5a78d59b69
    role: context
  - path: pages/traits/genomics/rst_2tm_1tm_tir_system.html
    sha256: 7229f6838b515231fd142245abd114372e6f9a480de10b73f2968c912f4aab30
    role: context
  - path: pages/traits/genomics/rst_3hp_system.html
    sha256: b912e03cfde6e027a014634b50c19174409d407037c02d749938577725470497
    role: context
  - path: pages/traits/genomics/rst_duf4238_system.html
    sha256: 11bf6525f45d0905dfcf4178f927755ee9b01ac7203f7b180da5e51b386e4b42
    role: context
  - path: pages/traits/genomics/rst_gop_beta_cll_system.html
    sha256: 1e449d8f4052e5728372b7af7484a06e2c2032ffb5c2828915389401f69e1000
    role: context
  - path: pages/traits/genomics/rst_helicaseduf2290_system.html
    sha256: 30197a04133fc6aa6cc5cf94db0268d8aaf2cd66b438f389abce9e77a06c47ce
    role: context
  - path: pages/traits/genomics/rst_hydrolase_3tm_system.html
    sha256: 19396725bc66dfc643c105c4243d2d245b3ef587ea02bd6d921a829ce0ebfc4e
    role: context
  - path: pages/traits/genomics/rst_rt_nitrilase_tm_system.html
    sha256: 204e1771199dc7e0f2feb7c350a2a67e8ff3c7791c449ed1c75009d8dc174f03
    role: context
  - path: pages/traits/genomics/rst_tir_nlr_system.html
    sha256: 2c5dc509ee580342bae458b3809f3343a8dcb1e9d7e70f7862ff141aa21bf6e8
    role: context
  - path: pages/traits/genomics/rugutis_system.html
    sha256: a013ff642220d10ac6a1d9473f67ba6bac7d6a89bc8e6c64e2e3d75cf6b6628e
    role: context
  - path: pages/traits/genomics/sanata_system.html
    sha256: c16ba6fef111784e650e2544adf005788cd4cd4892840de54fb9db4aacbd166d
    role: context
  - path: pages/traits/genomics/scomcra_system.html
    sha256: 4e90ed8796613ac7737e413de6404de1414be375b0dc19578fb4a3509bf2eda6
    role: context
  - path: pages/traits/genomics/sdic1_system.html
    sha256: 86f321c0f7693ca3e8e4e548661e45de91e13a85503c00710921014b08733e89
    role: context
  - path: pages/traits/genomics/sdic3_system.html
    sha256: 81add5d14fcf76563c4f4c19b04a239206f7e90c433d5ba50c206b1b6b7eb657
    role: context
  - path: pages/traits/genomics/sdic4_system.html
    sha256: a0da044fc5c35ae954b363abab68889a83b0db2648ae3c83818a082e07785850
    role: context
  - path: pages/traits/genomics/sefir_system.html
    sha256: 076b9e8b78f27e5c0523b2c8b92787bd5ddfa9a6fe70ce58392dc1405bf37655
    role: context
  - path: pages/traits/genomics/septu_system.html
    sha256: abb84cc8f7f6fdd2984241a2bdfc3fc940348b77332eb767d7ca1921a149dc3e
    role: context
  - path: pages/traits/genomics/shango_system.html
    sha256: c10eef8931acf4a74d029cd0597e5fd4ba68b4ae62a730e31dd63f5634e7c0c0
    role: context
  - path: pages/traits/genomics/shedu_system.html
    sha256: 5a6443b8f47a89d1dfffaf1159c68964d08c532b8a87e830c3a5ee9fb3c714d4
    role: context
  - path: pages/traits/genomics/short_lamassu_system.html
    sha256: 3fa9f7b89eb9c2d495ba09b9245ca1c97271c10d689cca463b25b0204097f45e
    role: context
  - path: pages/traits/genomics/shosta_system.html
    sha256: be350c52373db79d74882d2a7ae5b6eeba852d4dfb40b9766d13769f017342ba
    role: context
  - path: pages/traits/genomics/sirona_system.html
    sha256: cf17d40969724dc55dc68fe5efb4133ce1bd4d068f67f7c639fefaa7cf3a0cfc
    role: context
  - path: pages/traits/genomics/six_a_mbl_system.html
    sha256: 72c38cb324a43f8ec98fb397695b5316c72dbaf41fd6c10f7de608071c6c9b07
    role: context
  - path: pages/traits/genomics/snipe_system.html
    sha256: 30ecac77324fcb7edff44ba73d94e275f61db237507d8fbc2103cb9aadfa6170
    role: context
  - path: pages/traits/genomics/sofic_system.html
    sha256: f6b64bcaed35a199e036a94067af14a39a845e9bd5a24199221ec7703654f0a7
    role: context
  - path: pages/traits/genomics/sparta_system.html
    sha256: bf4411be6303170adb8d98353460fade879ebec9519893609154ed7ae1fb3c0d
    role: context
  - path: pages/traits/genomics/spbk_system.html
    sha256: 41f9b0391c44c00a94f4899d5d47822a7dc000894bc078681130f723082940fa
    role: context
  - path: pages/traits/genomics/sspabcd_sspe_system.html
    sha256: c55c07827ad911561daae10c690fe75b00d97b7a4de0f749bb8f6132d5380743
    role: context
  - path: pages/traits/genomics/sspabcd_sspfgh_system.html
    sha256: be352b2dc7cb76f0baa30d2546ad36f704bcd39f2e872fc84511ee089b571a67
    role: context
  - path: pages/traits/genomics/stk2_system.html
    sha256: f1c496a66644e402692d791970100248559b13edddcdc80fd06c2917c386591f
    role: context
  - path: pages/traits/genomics/sucellos_system.html
    sha256: e548bde339dcf66437622c140fb7bac239a2a880be320d26cc6a0a9400fc610f
    role: context
  - path: pages/traits/genomics/tab_system.html
    sha256: 6aa2bb9ed5bf274195fb9a59716cec9af9243e567532558ad087520493a61631
    role: context
  - path: pages/traits/genomics/tagi_system.html
    sha256: d513e30121ea7d4211f054b219cd2f2e92b0bceef50c91ee3c5507c522929ca6
    role: context
  - path: pages/traits/genomics/taranis_system.html
    sha256: 7e394bf4636bf4fcc08a3bd370b13ac693471826b45e6084f4f8806b6b2e2b24
    role: context
  - path: pages/traits/genomics/tgvab_system.html
    sha256: 7ddd5440d8aafc3f71770f36e170e74f8a37a3f5bafb80429bbd45150e08ee18
    role: context
  - path: pages/traits/genomics/tha_system.html
    sha256: e6fd2ff26c136c3f7517a4088390605ecdd27ce5fd7d9ec155f1bee89d9d92e5
    role: context
  - path: pages/traits/genomics/thoeris_system.html
    sha256: 424b02a70f4c5634032c2a80929f177242b6c76112d9b73492ae67f277cdfa89
    role: context
  - path: pages/traits/genomics/tiamat_system.html
    sha256: 69cde3f6b2f260ba93c7c9060c076feaa89f1040bf987bf388016feb902c626d
    role: context
  - path: pages/traits/genomics/tir_i_system.html
    sha256: c2c1e0f8f20999aa5bedaf7d03d977843ece5cacf95db080177b031f71434da2
    role: context
  - path: pages/traits/genomics/tir_iii_system.html
    sha256: afab29d61fed6635e052969e221e791e5030348313e13374a77c1da66afaa7bb
    role: context
  - path: pages/traits/genomics/tir_iv_system.html
    sha256: 3c6323df7104bc1738ded36b7581c082214d8fbb1be0ed172e61441c3cb5e88c
    role: context
  - path: pages/traits/genomics/tir_vii_system.html
    sha256: cc85d3f5760ccb006570f6cbfe08b593829355a8af20a96198639d671eefeb3f
    role: context
  - path: pages/traits/genomics/tir_viii_system.html
    sha256: 860229adf9aad13d9a2cbccb15fa25e6f8dc486000d38939070b98369c968caf
    role: context
  - path: pages/traits/genomics/toga_system.html
    sha256: 783b409182c7636afffa6cf98c029b27f2ec7ecec3382f179e19f83de32662a7
    role: context
  - path: pages/traits/genomics/toutatis_system.html
    sha256: 4d76208122bf749d56444a382f39035a7ce84dcd34f9646cb149e95681334e67
    role: context
  - path: pages/traits/genomics/toxin_system.html
    sha256: ddb0a3eb42b38eacd88b174b60803f7a7c6f772cb848c303d269d72bdaa4766c
    role: context
  - path: pages/traits/genomics/transposable_element.html
    sha256: f4964fc8c984390e9b9864cb89e6815fe70a79a89c6836c69f3e537beb7f0291
    role: context
  - path: pages/traits/genomics/type_i_restriction_modification_system.html
    sha256: f09b4c44b4fffd22008324a558373b817c62869ed9686e5f98fa41b2cf7fdcd8
    role: context
  - path: pages/traits/genomics/type_ii_restriction_modification_system.html
    sha256: 812be3ed7cb09cf8062629ded5ad886f4744d7af18062b20846baf99e6bc1d58
    role: context
  - path: pages/traits/genomics/type_iig_restriction_modification_system.html
    sha256: 598114e3cf38a01beaa8e22ca7be079aa463e99a1d3d4cbb64c6204b30702160
    role: context
  - path: pages/traits/genomics/type_iii_restriction_modification_system.html
    sha256: 779e87c0492d266d32fdf8f95b3990b3043a305fac1323d0bbca54f7ace55c34
    role: context
  - path: pages/traits/genomics/type_iv_modification_dependent_restriction_system.html
    sha256: 381f39c1a24eb0a188d9478129fd3465bb847db25bd5da9f1141b411c0239643
    role: context
  - path: pages/traits/genomics/ukko_system.html
    sha256: 4da19063ece648f155da153c9719ede8ddb86d80a18aff8a717f45e1a8e1f970
    role: context
  - path: pages/traits/genomics/uzume_system.html
    sha256: eaf1df32fefb5c9c867a1585ff7a63b7d7955fc0f49997d60a8ca67441991bdc
    role: context
  - path: pages/traits/genomics/vcam4i_system.html
    sha256: e026b3ba3e0300a883fe53709a23eee694c3acd8da7aeedff9e8b7baa6525bc7
    role: context
  - path: pages/traits/genomics/veles_system.html
    sha256: a825ab64e0540eac0d9029d53a262410bcf73c927e24b11c9de258c9a90c94e9
    role: context
  - path: pages/traits/genomics/viperin_system.html
    sha256: 4279dc4cd4a63f3e33044a96af05e713fb81a0167c01f0f6ea33a5e13a87cf57
    role: context
  - path: pages/traits/genomics/vp1796_system.html
    sha256: 3fd23a24d2b463fbde2ed68474562f38e3be56d6bf0c3a09dc81e3bde9d150a7
    role: context
  - path: pages/traits/genomics/vp1817_system.html
    sha256: 096d0377065297fb32bf8a57ac58ad4c633132d29cc33e24c3ca175ea7ef724e
    role: context
  - path: pages/traits/genomics/vp1823_system.html
    sha256: 8105961db21f595fd12b92b38f62835858e8596d9b0ce37bc89fcf10c5b1cf1e
    role: context
  - path: pages/traits/genomics/vp1826_system.html
    sha256: fbe0cc49521dda77878965f3fcd1fce90e135b1faabbb5eace177b86a547512e
    role: context
  - path: pages/traits/genomics/vp1839_system.html
    sha256: 718e65e60d460efcda0fd338d759808c7153826c8ac6ca907b509708980733d2
    role: context
  - path: pages/traits/genomics/vp1840_system.html
    sha256: 2163d26a384b1bad98902e0e77dfd4341a8cdc542b19def43994202827c446e7
    role: context
  - path: pages/traits/genomics/vp1848_system.html
    sha256: 9aa6c083519cb6aaf644011d8e50480401f34bc8c6579258ae3549aef5af9cf4
    role: context
  - path: pages/traits/genomics/vp1851_system.html
    sha256: c6e891c5a51eec127c640a5c4fd7c4276d9fec6b98dd5866f40586b78ce0c2f9
    role: context
  - path: pages/traits/genomics/vp1853_system.html
    sha256: da89b2d84d0994931a99099af29ec397407f78936519bc6a827713e0702f786e
    role: context
  - path: pages/traits/genomics/wadjet_system.html
    sha256: 42141a400ad88b334df952995b2d38b64dc142d8144a7b8871dc5e2dd5d62e87
    role: context
  - path: pages/traits/genomics/zorya_system.html
    sha256: 3855dfbe829b28cd58e5173d2cc4ead766a8628d8938c034b68c83fc7892966e
    role: context
  - path: pages/traits/genomics/zorya_type_i_system.html
    sha256: 1afce7f11a99aeac3d03f1d1cc3dc3e5848006372840f1b21e0589707e59ed47
    role: context
  - path: pages/traits/genomics/zorya_type_ii_system.html
    sha256: 9a056de9e8ba11c568b1a5f269efc266aabd9b068b039764558dceb37fde52ec
    role: context
  - path: pages/traits/genomics/zorya_type_iii_system.html
    sha256: db3d82cf6d1e51eb20e5e2e3613999a61878ce55df9a8a647f15c871b7887d01
    role: context
  - path: pages/traits/metabolism/accumulates.html
    sha256: fcea87464d6f269fe99a39df6cbf5173d6c41a0b6adf8b0398c2b46ea6321bf8
    role: context
  - path: pages/traits/metabolism/acetoclastic_methanogenesis.html
    sha256: 61459c0fc1eecaa3a0dbfbc29278f7705c08ae72ee6167fb4b82411646ffea9f
    role: context
  - path: pages/traits/metabolism/acetogenesis.html
    sha256: 4c4a46aff1c014816bf1140bff1529e89b5187e547fb8407c47e22a17d7bb3b9
    role: context
  - path: pages/traits/metabolism/acetone_butanol_ethanol_fermentation.html
    sha256: 35e430d20ff7743e48d5720b9de61975f9a2a9d161b734506a92a3c3ade319b1
    role: context
  - path: pages/traits/metabolism/aerobic_respiration.html
    sha256: c5799d000d4a3201674a372f803c2fa36afe811b495efe2a09057509c5b76456
    role: context
  - path: pages/traits/metabolism/anaerobic_ammonium_oxidation.html
    sha256: e7d5cc948427047869424f9b5bba2c8a3ac4ce09751fc6eab0d8ceb3e6a7492b
    role: context
  - path: pages/traits/metabolism/anaerobic_oxidation_of_methane.html
    sha256: 842df02c83772d9464e1cf75e9f9532387646775fccc654daa8c71b7efb12171
    role: context
  - path: pages/traits/metabolism/anaerobic_respiration.html
    sha256: caa1c64f257ae8bdf10d8cb653f338f69e2df43e94bc31ebdd06039ff6246051
    role: context
  - path: pages/traits/metabolism/anoxygenic_photosynthesis.html
    sha256: fb29d89df1125c84170fa05b77154872cf863be5ba68f8c72e653b854a8e602a
    role: context
  - path: pages/traits/metabolism/aromatic_compound_degradation.html
    sha256: 92b5d939a11352d277b71e8f24df54a3c604879f0c1715bc3de4cac632442f97
    role: context
  - path: pages/traits/metabolism/aromatic_hydrocarbon_degradation.html
    sha256: 0425a2b81cbb4af6bd3d1e9b1f920c86d62d72b89682bb0ded976b1eff375bcd
    role: context
  - path: pages/traits/metabolism/arsenate_respiration.html
    sha256: eb6f6e991ccc49737459febafacb736f523896e72a8d1ca5ae923b75fe5155e0
    role: context
  - path: pages/traits/metabolism/arsenite_oxidation.html
    sha256: 776b009e4bc2f241ef0ca1f0201c89f666798e2044b23c861e940dc7ed65cf00
    role: context
  - path: pages/traits/metabolism/assimilates.html
    sha256: f6ff75bad736316a5cad3fab649952c489f2c6ab28c4d84d007a5b31653277ff
    role: context
  - path: pages/traits/metabolism/biopolymer_degradation.html
    sha256: 73c9d8d3c28680f7a240f278d398a4dcab5b38052a29d5ecce991cafb3cc3151
    role: context
  - path: pages/traits/metabolism/builds_acid_from.html
    sha256: a8328ad9001fca6c837c99bb24f2941394033cca80f0ef4e618c2cd439f471d8
    role: context
  - path: pages/traits/metabolism/builds_base_from.html
    sha256: 707b5595fe82478865903be4288ca36a0f3561c81994edf42657e3c0441a7d0a
    role: context
  - path: pages/traits/metabolism/builds_gas_from.html
    sha256: 2cf07008884abf76796fb1f16336ad6f0ff95d36a1d6d250c9cd306489260a2f
    role: context
  - path: pages/traits/metabolism/butanediol_fermentation.html
    sha256: 2c394fed47cbb8daf02d24771f7cb622fdfe510ad006d20f9655d9f16afc5dea
    role: context
  - path: pages/traits/metabolism/butyric_acid_fermentation.html
    sha256: 8232e174e451188c60e9ddebe12e3f2242f880376a34d0d5e9906ffdb4610caf
    role: context
  - path: pages/traits/metabolism/cable_bacteria_metabolism.html
    sha256: 23b82a21e72fe2901550ba9a9d29b5164470566e4a412b2f369ae32ccc5c48e9
    role: context
  - path: pages/traits/metabolism/calvin_benson_bassham_cycle.html
    sha256: 1e60d9005ca040c35c14f568498e24e9602c0729b6bc7b5783a65e73215f632f
    role: context
  - path: pages/traits/metabolism/capable_of.html
    sha256: b1d4d20affeffc8b2b03432c49193260f993a017f0f24192fc4c0a458b3d41cc
    role: context
  - path: pages/traits/metabolism/carbon_fixation.html
    sha256: c1837d0198a88bc08a3471fe7db46b8051c4aa7889631385971e1250e57113c7
    role: context
  - path: pages/traits/metabolism/cellulolysis.html
    sha256: f0992f3132887a6855a8ece272f561424515bbbd56980ccc94f2292b9de58ef9
    role: context
  - path: pages/traits/metabolism/chitinolysis.html
    sha256: aeef4ebb731a992bac7632dcf8c260944b1938a7360a23d95a068caf55e1e821
    role: context
  - path: pages/traits/metabolism/chlorate_respiration.html
    sha256: 06522e0d6526d2eab74179c2c7a603adf5bc9be1393706fba8d93f795f614922
    role: context
  - path: pages/traits/metabolism/citrate_fermentation.html
    sha256: 75ea33ba6143b6b45b4aa88e5583ce8740d65f25cc175d351f036bd97992d408
    role: context
  - path: pages/traits/metabolism/compartmentalizes.html
    sha256: 19357afac4f8d10878ed1879e081eb438c1ce15c033199a0b2698635d19c211f
    role: context
  - path: pages/traits/metabolism/complete_ammonia_oxidation.html
    sha256: 0b7ffb20a329d1cfacf29e064031450ac572abe1e492f8c26b5ef86b0f91acd8
    role: context
  - path: pages/traits/metabolism/dark_hydrogen_oxidation.html
    sha256: 064155144b747f4b0e84413a7e9b0f6c29cb123a7b8b52b80b6b7928100fdbc6
    role: context
  - path: pages/traits/metabolism/dark_oxidation_of_sulfur_compounds.html
    sha256: 4d10aa415561cba41f4aa9d9f33d8c7fccb684585086c6fdae649e895df11b56
    role: context
  - path: pages/traits/metabolism/degrades.html
    sha256: 1286a930d1d08dbfe6b12b4b349845c6b683b63997e90cc816afcbb5aac411fc
    role: context
  - path: pages/traits/metabolism/denitrification.html
    sha256: ecffa6baa8891897a69d271884d0a1251bd8030359970e5c6288095eebb74b69
    role: context
  - path: pages/traits/metabolism/dicarboxylate_four_hydroxybutyrate_cycle.html
    sha256: a32a62fc671a90e4b5a9f8b1e3353784fe18f2f2a98772ed7d37fca3dae36cab
    role: context
  - path: pages/traits/metabolism/dimethyl_sulfoxide_respiration.html
    sha256: daae444cb89aa3bf76b15882d33d04dbfe8b68f767d300bb177a10a36cbc5ad4
    role: context
  - path: pages/traits/metabolism/disproportionates.html
    sha256: 26120128b3792ba29eafe0f9fad454e551f3f27afa79299111f61cb35ac3fe88
    role: context
  - path: pages/traits/metabolism/disproportionation.html
    sha256: 00bfe2d5daa14721456dc0e5d643ba5a3fb65d9d20d1df590bdf524637ddddfa
    role: context
  - path: pages/traits/metabolism/dissimilatory_iron_reduction.html
    sha256: 3eae3dc50ac93a98993fed2c2e3b3cabef2be4eedaf6c5843d7760c3b27e01dd
    role: context
  - path: pages/traits/metabolism/dissimilatory_manganese_reduction.html
    sha256: f8b984de4b2258a430d1550ec1ee769d2257ec854f8a0b29f9eb78df38dc4eb6
    role: context
  - path: pages/traits/metabolism/dissimilatory_metal_reduction.html
    sha256: 601e17ab3569aa387dd3f32c683b4d8b30ae319c43ff04369e0d2fed2d092e27
    role: context
  - path: pages/traits/metabolism/dissimilatory_nitrate_reduction_to_ammonium.html
    sha256: e07b462a60c943158f5b67e447a3b265d651c34a5696625e44385432fcce76d8
    role: context
  - path: pages/traits/metabolism/dissimilatory_sulfate_reduction.html
    sha256: bef94a220e3a9c9e022f4ad0adf08e3236e37fa9a71ab03a0b897c0f0b865fc0
    role: context
  - path: pages/traits/metabolism/does_not_accumulate.html
    sha256: 3ffcb4f4f3f045bab7c2b3214f218e0fb218941e32cafd1722058789593f931c
    role: context
  - path: pages/traits/metabolism/does_not_assimilate.html
    sha256: 72882f02de5f91f4e04940d430bc2d5be421913816e9cad9cc464383609d6be9
    role: context
  - path: pages/traits/metabolism/does_not_build_acid_from.html
    sha256: 80b82fc0fb785ba52e864a0e8d66c01e7a2ba28008abe99f6be2a755d3588cfd
    role: context
  - path: pages/traits/metabolism/does_not_build_base_from.html
    sha256: 258ea6a9c0b3e4e26dcaf3664b2bfd7e2c12130574dbfccccd639257465e67e6
    role: context
  - path: pages/traits/metabolism/does_not_build_gas_from.html
    sha256: 0150ef6552378184892c196c42b67e3bc10b27ecffa97dcad455f73620753b5d
    role: context
  - path: pages/traits/metabolism/does_not_compartmentalize.html
    sha256: 339c746751f9890db445a268c3f7b811a164496e5af0bd825820d1cf65d33c3f
    role: context
  - path: pages/traits/metabolism/does_not_degrade.html
    sha256: ccfe7a876cd6174d3e663eae5ce11580f22300ddc49aeba405a0e44737133879
    role: context
  - path: pages/traits/metabolism/does_not_disproportionate.html
    sha256: 4a425364872e35e697dca0ce56f829c3d41a6fcd923b3569374f82d23d9e5ac4
    role: context
  - path: pages/traits/metabolism/does_not_export.html
    sha256: 5078f8c81ac7b4ffa880c9d06db7408d171ce0328606e6c2f0899f7324079622
    role: context
  - path: pages/traits/metabolism/does_not_ferment.html
    sha256: 83fcb212748851fd358df892f8e6107fafb30854a798c0e47903ffdfb2bb90c6
    role: context
  - path: pages/traits/metabolism/does_not_hydrolyze.html
    sha256: ac35d87bd44508165220c158bb25c8f2a338ef2934b05bbc0d3f69dca7afa1fe
    role: context
  - path: pages/traits/metabolism/does_not_import.html
    sha256: ae4cc9c703da83aa5286edfc3089388cdd3184d3d70d10b71f8677ce62b4acd4
    role: context
  - path: pages/traits/metabolism/does_not_oxidize.html
    sha256: d40ccba2b79fa2f24c9410710c0a8022e0232be5e11a0ca10910d1ea62f4d506
    role: context
  - path: pages/traits/metabolism/does_not_produce.html
    sha256: cf81e1b11e49eb8b1b135f19fa9a33ee6eb2e868a86ff3578cedfb5293f27145
    role: context
  - path: pages/traits/metabolism/does_not_reduce.html
    sha256: 223ee75c026ba062ca3ac7723a544dfb9b8589577cba66a69f8b10e0e1373267
    role: context
  - path: pages/traits/metabolism/does_not_sequester.html
    sha256: b7f822bfa85313eb35b97980508e767621d6d83d383d9341aa371f681e8faccf
    role: context
  - path: pages/traits/metabolism/does_not_show_activity_of.html
    sha256: c021e1bb7285683aafad9fd4b71f7c711545d1e5468038e70b75271a749db7a7
    role: context
  - path: pages/traits/metabolism/does_not_transport.html
    sha256: 07510dcc336f7cb41de55959aea526abc49ac9e7de684d71eee94cc588cb6eef
    role: context
  - path: pages/traits/metabolism/does_not_use_as_carbon_source.html
    sha256: fd0bf98d5943e823d48641e4c618413dcd14d8f35473fff73b97fb2ced7e0c9f
    role: context
  - path: pages/traits/metabolism/does_not_use_as_electron_acceptor.html
    sha256: c7ccc4c988e0d44cf3fb2d94e2c7de81ab7dfa9306855333342812377e6cf5a3
    role: context
  - path: pages/traits/metabolism/does_not_use_as_electron_donor.html
    sha256: d5c95d520cc912885e912bd45e0b37340e5e35213084c2056b327961691ec2c8
    role: context
  - path: pages/traits/metabolism/does_not_use_as_energy_source.html
    sha256: 85b15cf3dbc2e3b7662cee14ef886dae9784f2abf5439598d495c4a042b9c28e
    role: context
  - path: pages/traits/metabolism/does_not_use_as_nitrogen_source.html
    sha256: 52c40186ced82c2106c9585497f1edd80214e5b0e8cfce29f848ca2195c03429
    role: context
  - path: pages/traits/metabolism/does_not_use_as_sulfur_source.html
    sha256: b7e137d3a2e501bf6c25c41c81d740a99739cab000e7aa8e8c31fc11482ee8a6
    role: context
  - path: pages/traits/metabolism/does_not_use_for_aerobic_catabolization.html
    sha256: 22906c27c5f687556a79851765efdbfc37fb8a09868fa331c24c017e69b3ad5f
    role: context
  - path: pages/traits/metabolism/does_not_use_for_aerobic_growth.html
    sha256: 9f37ca12d6b45946aa97b0dc1aa0938c9640f26e716f3775919b7d8e90d8c5b4
    role: context
  - path: pages/traits/metabolism/does_not_use_for_anaerobic_catabolization.html
    sha256: 0960484cad143371bd085cffb1ab8462a4fe2c4fe617706539b271cacd8bec98
    role: context
  - path: pages/traits/metabolism/does_not_use_for_anaerobic_growth.html
    sha256: 13edc0d9b9e7e367314ab16f6a44a23b2b408d27fcddc7c8b4515b7a59370cf0
    role: context
  - path: pages/traits/metabolism/does_not_use_for_anaerobic_growth_in_the_dark.html
    sha256: 6ea671c38f45493b5f7c29728c4631b2129bb1c7bbe442a4bf2aa5dfd14be2fa
    role: context
  - path: pages/traits/metabolism/does_not_use_for_anaerobic_growth_with_light.html
    sha256: 6ce0d7d71b201986ece67fffb3f1435e258cf402e87f1f921184bd7586f95bc7
    role: context
  - path: pages/traits/metabolism/does_not_use_for_growth.html
    sha256: 5578b69e459ac25cef6898c16c4f93fd70198d257b2db854db1492d1713f9058
    role: context
  - path: pages/traits/metabolism/does_not_use_for_respiration.html
    sha256: 9241ee106384b6feae8d27ba5fe360e6ffcb8a09783f4c2ae272c27584773d98
    role: context
  - path: pages/traits/metabolism/does_not_use_in_other_way.html
    sha256: 633a6a0b4fd2cadc98583cc3f979a7f886ebc95da3893c0813a7e1aeedd12fd6
    role: context
  - path: pages/traits/metabolism/electron_transfer.html
    sha256: edbe259f304a949ff22d4fdf0ca8d3c6de82c4bee1230c37bdc830a270289be5
    role: context
  - path: pages/traits/metabolism/enzyme_activity_analyzed.html
    sha256: 13b363d23dcf8423bf90164c962a078e6314e9bf4b5f4a61ea6c35c2736615dd
    role: context
  - path: pages/traits/metabolism/ethanol_fermentation.html
    sha256: a3ff595d443f8a7096a1a780ae13b13d5cc6e1d67307aa9a1f5c6bd8cffb0399
    role: context
  - path: pages/traits/metabolism/exports.html
    sha256: b1012b74ee35ff322d0480e92f0d667b3dd6bba8ec219a2d5f255748aab1b76c
    role: context
  - path: pages/traits/metabolism/fermentation.html
    sha256: 2d5053484a701245c95cd7e01db70ce6cf4548eb8c175258115cc1b68222e0e4
    role: context
  - path: pages/traits/metabolism/fermentative_hydrogen_production.html
    sha256: 6d6225900246d0456c19c1145d3dcef782f5d62568227a68fd26a91c511e6eb4
    role: context
  - path: pages/traits/metabolism/ferments.html
    sha256: 6108c32099c4e19c833b04c25fe5394fa04165aabab7cc791e3d628f91a9b88b
    role: context
  - path: pages/traits/metabolism/fumarate_respiration.html
    sha256: 42fad1c0b382a04526c3918d493926a05d2970845c8223e08c8d8fbc92751240
    role: context
  - path: pages/traits/metabolism/has_growth_nacl_observation.html
    sha256: e594b42727ca8de3793f094272efc679789664e21fa7967e3d6459b6cf76e699
    role: context
  - path: pages/traits/metabolism/has_growth_oxygen_observation.html
    sha256: 24803b13d024d45703ff083fcebebdd376e96de0a117fb4556724e0dffb6c7f5
    role: context
  - path: pages/traits/metabolism/has_growth_ph_observation.html
    sha256: c377bb1952a7c88cc349e15078f34e269fb8fc5c90bac0d85c006a82773d0a36
    role: context
  - path: pages/traits/metabolism/has_growth_temperature_observation.html
    sha256: 5fe6fddc91139ca623dedc14a6e78a12acceb6b7f3b28bd2fdbdeb7c6002a547
    role: context
  - path: pages/traits/metabolism/has_nacl_delta_observation.html
    sha256: 02bcbe2e0c8d2b1b031aac339de3191b1d25c8dbc058f9e7125f3169b1b4ec85
    role: context
  - path: pages/traits/metabolism/has_nacl_observation.html
    sha256: f75ad978197cfccb09af451df687b47b558d1d8a1f0a73899c46aa2670603742
    role: context
  - path: pages/traits/metabolism/has_observation.html
    sha256: 04658be6b30b7f13d0e3275cf354c558c814ba4b0880709bd804368b3c733369
    role: context
  - path: pages/traits/metabolism/has_optimum_nacl_observation.html
    sha256: 6b529754ca5f80d16e5e746fe32ef8ae49690ea2b55d6e217e2d4667117f779b
    role: context
  - path: pages/traits/metabolism/has_optimum_oxygen_observation.html
    sha256: 96f842a396658ab3c37ba3ef22be1fa6adfe29ba46e420ca2c5b1049345f2a25
    role: context
  - path: pages/traits/metabolism/has_optimum_ph_observation.html
    sha256: bc2a977042851577977e868c43577ee9965feddfb98d7f32ede330a32a82f088
    role: context
  - path: pages/traits/metabolism/has_optimum_temperature_observation.html
    sha256: 49ebb889e8eeb449622712662b7b94ae68b8c6e888c23dfd187995edde86e3bd
    role: context
  - path: pages/traits/metabolism/has_oxygen_delta_observation.html
    sha256: 3d5ba7f5923421968321bc16578f58c82a958711083866dde3fc948593e3810f
    role: context
  - path: pages/traits/metabolism/has_oxygen_observation.html
    sha256: 3a5e46398b59ed9e9707e3e342878a1957e068cd108ddaedb34fd7888ee1689f
    role: context
  - path: pages/traits/metabolism/has_ph_delta_observation.html
    sha256: 869d1503ff8cdbc192cc60d7c8726a28efd5d974a129d0583108e4268b16d331
    role: context
  - path: pages/traits/metabolism/has_ph_observation.html
    sha256: 2433aa9eb18c35ed4b7e093c20aaab70ac57fb8d0ed14cb13653a229ca402fe3
    role: context
  - path: pages/traits/metabolism/has_phenotype.html
    sha256: f75b7aed2d5c30772c9ac231dcc982f702d448f072bb32c72203e22886bd778c
    role: context
  - path: pages/traits/metabolism/has_quality.html
    sha256: 4ba6b561455b7d904612f52b944d1952e2cb27d19c7ade54c5ce4170c0176bad
    role: context
  - path: pages/traits/metabolism/has_range_nacl_observation.html
    sha256: 0989c12c91a91050ad47147feff8016d8c5ac81b36023fabf0d83e11b66da02b
    role: context
  - path: pages/traits/metabolism/has_range_oxygen_observation.html
    sha256: 0145454fd92c368d6893efe7cb74157cdc9ef83dba343a069bd3e8ca2078b666
    role: context
  - path: pages/traits/metabolism/has_range_ph_observation.html
    sha256: 39d90584979b0b406741de094fcbf5824276d8a1fc1587ffe070e545e168dd0c
    role: context
  - path: pages/traits/metabolism/has_range_temperature_observation.html
    sha256: 74e3634ed8cc9556d773fa105d994eb7b6d9759760f4db07336aaa6273731ad1
    role: context
  - path: pages/traits/metabolism/has_temperature_delta_observation.html
    sha256: 8bfeb2270dbbb07b535eb16a782073ca4406c1c0616020437e1d5eb5835eb9ca
    role: context
  - path: pages/traits/metabolism/has_temperature_observation.html
    sha256: b03c1e78ef7a9f02e70ee2398f8d3ae39f7bbc3ee73f9d78f9559a294033d3d5
    role: context
  - path: pages/traits/metabolism/homoacetogenesis.html
    sha256: b29cbccae2ab4c0b1b40eb1a9a1371df4deef3ae00fcf897e369efdeb6763cb9
    role: context
  - path: pages/traits/metabolism/hydrocarbon_degradation.html
    sha256: ee89a7c9bf3c7ec0ead89d9a40f4a2d6fd7a110e4fbbcb89c4bb3bea54833c1b
    role: context
  - path: pages/traits/metabolism/hydrogenotrophic_methanogenesis.html
    sha256: ecbc7cf902907d83b83d6bf57e523703c5411fbcecf71b8778bfcf30c3378fc4
    role: context
  - path: pages/traits/metabolism/hydrolyzes.html
    sha256: e3d3f20c883252c464d1bc5ba02f13bf1c7941241e17cb4edb556c1d368e61c1
    role: context
  - path: pages/traits/metabolism/imports.html
    sha256: 515ca106500dc3e68b7e6c8f98638c7945c2afe5a16e514897b3ba9394061ec0
    role: context
  - path: pages/traits/metabolism/iodate_respiration.html
    sha256: 40af4cff9521ccdd5959c79932a7163ecf2cabda0c96e125914dcd7d717c1cad
    role: context
  - path: pages/traits/metabolism/iron_oxidation.html
    sha256: 24e6169ee4d4f10d57c082562683a7643c13972417317fcf1ab0f631b4d79481
    role: context
  - path: pages/traits/metabolism/is_not_required_for_growth.html
    sha256: 79a3b4479a31dc2d5a03d3d783b4222855f60f8b0e87c5a1f58acc3eb1b6da7d
    role: context
  - path: pages/traits/metabolism/lactic_acid_fermentation.html
    sha256: b5637eea912202aa89ba316584483b2316868954aaa2b59260895f7316a1846d
    role: context
  - path: pages/traits/metabolism/lignin_degradation.html
    sha256: cb5d5a91c2c156d85c92d3491fe450efa5e3c851e1181ba0d4bb5a31bbb1fc88
    role: context
  - path: pages/traits/metabolism/lipolysis.html
    sha256: fbaad74cd43f8062f4144f69aaf40f5e482f6a7ff13b543aa8ed54eae7991541
    role: context
  - path: pages/traits/metabolism/manganese_oxidation.html
    sha256: f791a27332dd04b6be4668e0bcd902caba3793199e98ff074ef03c8e9eb509ac
    role: context
  - path: pages/traits/metabolism/metabolism.html
    sha256: ad0a95391e1a2e8ba1ca3246962fd166a022f0558be9ec6121a77d3319f48288
    role: context
  - path: pages/traits/metabolism/methanogenesis.html
    sha256: d82f68356ec001403ee36b243b673ab53507c259cadceb15ec3111e65d933c6b
    role: context
  - path: pages/traits/metabolism/methanol_oxidation.html
    sha256: a31dac31aab14c83994b67337a27b992f18ce781c7aed16ae68ed54fbad97f66
    role: context
  - path: pages/traits/metabolism/methyl_based_methanogenesis.html
    sha256: 0ce32add4c72941ffdd94dfc67292099c423616254ad517d001ae569c53dfbbf
    role: context
  - path: pages/traits/metabolism/mixed_acid_fermentation.html
    sha256: 495f43240820803372ddc217b17a6aae6a985285b6f741ec9b6b1dbd7ce7c741
    role: context
  - path: pages/traits/metabolism/nitrate_reduction.html
    sha256: cbbbf45dea0a13ac259e5b4734d4e5633cc67be6af22b7fba919d92475d4c460
    role: context
  - path: pages/traits/metabolism/nitrate_respiration.html
    sha256: 5e5cda47b7bdc38d3a7b799a41e3343c01930dc29cccea8414a480f2c8a002ae
    role: context
  - path: pages/traits/metabolism/nitrification.html
    sha256: 0e90bf371413a2a4843eea31b016f59d3d9a9632b688f58a69e269a99918a571
    role: context
  - path: pages/traits/metabolism/nitrite_respiration.html
    sha256: a0b3363e39fd1e2a6fb52103a5bd668be17e15fcff86b6fa33fb106897b269a9
    role: context
  - path: pages/traits/metabolism/nitrogen_fixation.html
    sha256: dc7d06f4edd466bb016fcad0c90a1efac0caf97d38290c48d77f81aef9fa764a
    role: context
  - path: pages/traits/metabolism/nitrogen_respiration.html
    sha256: 040d4184573dcf8ab541667816bdbfec11aa68b011aee26130c79172fe08b08e
    role: context
  - path: pages/traits/metabolism/organism_interacts_with_chemical.html
    sha256: 720618c534d1bc03cd786fa82dac00ffd97573d8eb3571885a6f69e91b2ecf00
    role: context
  - path: pages/traits/metabolism/organohalide_respiration.html
    sha256: 7f7996ef19131ddc0be3e9d23840b5505434a2bfe0931e2d46795856e624124c
    role: context
  - path: pages/traits/metabolism/oxidative_phosphorylation.html
    sha256: d5079b4bd4931e3edfa85b9e99cd6c7e9f907cfe7e81aacf9c9819e6becf91c5
    role: context
  - path: pages/traits/metabolism/oxidizes.html
    sha256: 780e81440c125b8a8346106ab040be05d54ef966e5eb8bf05b525f4a9f93fb20
    role: context
  - path: pages/traits/metabolism/oxygenic_photosynthesis.html
    sha256: 9df272bbf328244874ec96214bf6174581735e1fb1c7a8b7499c87999172eba0
    role: context
  - path: pages/traits/metabolism/pectin_degradation.html
    sha256: ea376faef40e1bbd723ecdf000dbce9eb7963793d8f32e3de3ce50fbd9c94955
    role: context
  - path: pages/traits/metabolism/perchlorate_respiration.html
    sha256: 8fe8a31769b666e7aa734fe1b3643156c1300434812d124114c696e51066ebac
    role: context
  - path: pages/traits/metabolism/photoferrotrophy.html
    sha256: 2398ce50881c0638ba435f5c511edc1bc0f99d18c9fdcf20e31b376716a70d4f
    role: context
  - path: pages/traits/metabolism/photosynthesis.html
    sha256: 9aa93b611edd82f9a9742fbb6fc710a82eeb45e2c7e6c56cd5a809d52bec630d
    role: context
  - path: pages/traits/metabolism/phototrophy.html
    sha256: 563f188078412846a92e6b5ad712e9f5641a8eaf0e2c26db5ef288b6e86d76ba
    role: context
  - path: pages/traits/metabolism/produces.html
    sha256: 1e02e1e8849bce0ccf8d53c7f8b32c6ca851136425e676e4cb0839b5278e815b
    role: context
  - path: pages/traits/metabolism/propionic_acid_fermentation.html
    sha256: 203bf8e6fecf487daaec1fcf669974c1023580cd692765ce9f5fa91105ac9a71
    role: context
  - path: pages/traits/metabolism/proteolysis.html
    sha256: 9f594bde0a50936ccd959a3a9654a1361ef29eeaf0fd7d6a9fc7ae8f8ad2bf3e
    role: context
  - path: pages/traits/metabolism/proteorhodopsin_phototrophy.html
    sha256: 871c935f7b26ce12a8a9d37b404d75762c6a9cf76d071b6f8716b59661a3dee8
    role: context
  - path: pages/traits/metabolism/reduces.html
    sha256: 59aa8027641efbed75e1bce2bcef90fd84ab1be03e0f481f45d3801b04d86ff4
    role: context
  - path: pages/traits/metabolism/reductive_tca_cycle.html
    sha256: 6b92ea8cd49977d71407215667f5e8c86544b465a7640aa85d13d8539faefc88
    role: context
  - path: pages/traits/metabolism/requires_for_growth.html
    sha256: 9786c7aea514cd3f32f435bc8db876bd2a6a06b2cbffb01116094d1d934a49e2
    role: context
  - path: pages/traits/metabolism/respiration.html
    sha256: 46eda92bd8af811da88a5a9a51d5e3d81a21c8132bbbb5a95ffe3218aeb8f615
    role: context
  - path: pages/traits/metabolism/respiration_of_sulfur_compounds.html
    sha256: 0547be0d2e077b97dcc16730a76bafc92f6a64795a3a380613154e4358d57f40
    role: context
  - path: pages/traits/metabolism/selenate_respiration.html
    sha256: b19406af6807a0fb9e660b1c60bb88114cd0c9375c468e8ad05c1ff76951d22d
    role: context
  - path: pages/traits/metabolism/sequesters.html
    sha256: db403adb6aa043ed979fa1b293e93ef9313b026db395f2b0e3ae3600f4531748
    role: context
  - path: pages/traits/metabolism/shows_activity_of.html
    sha256: ee7a7d751102cb283f58e8cf3598f6d0a4d5e5de3b82eaefb9fb442dd8184314
    role: context
  - path: pages/traits/metabolism/starch_degradation.html
    sha256: 599d99b16c6063feb409b6065e587abc48967b6645eb5a54c1aa267592f81277
    role: context
  - path: pages/traits/metabolism/substrate_level_phosphorylation.html
    sha256: 6aaa560356e67287eb672fa77d90e70e0889e9b1bf3af7ece131a86f8f9a0a24
    role: context
  - path: pages/traits/metabolism/sulfur_oxidation.html
    sha256: 4c6370864a02a6f9d607f0cf77ce7a1a89d1f73bab45f9a322d62ba3a4452338
    role: context
  - path: pages/traits/metabolism/sulfur_respiration.html
    sha256: 8ab30b47834e9cf8d5895b12dd7518087a708817b20d0358b45f50245b226935
    role: context
  - path: pages/traits/metabolism/syntrophy.html
    sha256: a91d1631e72e9fbc027c1cd6a5d78a0ae1efebb866717d41538a2049381d11a2
    role: context
  - path: pages/traits/metabolism/tetrathionate_respiration.html
    sha256: b3a2b94d3ceb3ec821cf26347635bb8e226ccd0c3a2a39d25f71fa37c002dd95
    role: context
  - path: pages/traits/metabolism/thiosulfate_respiration.html
    sha256: a01ba1eff017e500c0945f692efaca3b62bd5029997ab6f4cb830db9ac5cdb11
    role: context
  - path: pages/traits/metabolism/three_hydroxypropionate_bicycle.html
    sha256: 5630e69fb71809ec524acd975f93220524eb6d63166a555a32b65b94b75d6d66
    role: context
  - path: pages/traits/metabolism/three_hydroxypropionate_four_hydroxybutyrate_cycle.html
    sha256: fea9b741ce61f064f2076d11c890bd7ab65a04a3c0f6b769b349081c9ee8f2f3
    role: context
  - path: pages/traits/metabolism/transports.html
    sha256: addcc55f0cd0c0e897047f7ea532dad4509b7c04b03b38ccbf50df9c2114f42d
    role: context
  - path: pages/traits/metabolism/trimethylamine_n_oxide_respiration.html
    sha256: 52bea7d20fed599993de9de3b7e88f430a3bebb731f52893401355b0376fa945
    role: context
  - path: pages/traits/metabolism/uses_as_carbon_source.html
    sha256: 8d89a5a3150ef8a363c57b66f103b024c5393fdb2088cddaccc4a2124e31ab6b
    role: context
  - path: pages/traits/metabolism/uses_as_electron_acceptor.html
    sha256: 675770212af4af05db4a259c93bacef7cee1cf23ffbc8a7e33c13223897dc9da
    role: context
  - path: pages/traits/metabolism/uses_as_electron_donor.html
    sha256: 6d3346c236e1f693403473eb3793ab5dcac13430dd3e62ee8c718b840c9319b2
    role: context
  - path: pages/traits/metabolism/uses_as_energy_source.html
    sha256: 84789017a4c8252016cf72912ae9f98a73a05b776ce155a18dce3a3fca989c4c
    role: context
  - path: pages/traits/metabolism/uses_as_nitrogen_source.html
    sha256: 58d771fa3909edfd362514d61837fafd8af4ac52cd8ff3bf695795cb86db4574
    role: context
  - path: pages/traits/metabolism/uses_as_sulfur_source.html
    sha256: 9cf76ceb8d89893fd71750776722290b4be46465df589e1fafa555279983aad1
    role: context
  - path: pages/traits/metabolism/uses_for_aerobic_catabolization.html
    sha256: 4c5c88567455de307e38a8ad6b2bed18f59eac4df566b806028c168a0767d793
    role: context
  - path: pages/traits/metabolism/uses_for_aerobic_growth.html
    sha256: 80a27f7392c32e2325e69304797c529a9e4d710c7de2b3fb3246f1e7b0fed64e
    role: context
  - path: pages/traits/metabolism/uses_for_anaerobic_catabolization.html
    sha256: 98b15fa4ff18296ca42dba1e7d0c07c3803a9e3b4b8f38fb334f179c6626510c
    role: context
  - path: pages/traits/metabolism/uses_for_anaerobic_growth.html
    sha256: 225091c32173343be1ebb5b6151ced722f7f5d8feb6a5d0ad80ebae856b56787
    role: context
  - path: pages/traits/metabolism/uses_for_anaerobic_growth_in_the_dark.html
    sha256: fce89b79df12e14a94abf198e1c78ab8802462969cfe30778b27079a6d63b07b
    role: context
  - path: pages/traits/metabolism/uses_for_anaerobic_growth_with_light.html
    sha256: bf3cc700354d431ab16b7f8ed394f9fc77278f528375803e7c00088528e036cb
    role: context
  - path: pages/traits/metabolism/uses_for_growth.html
    sha256: 6d0624f577b77cbb9ad6ab1eafcc219037dc9854e24f5c748a22dde17edc064e
    role: context
  - path: pages/traits/metabolism/uses_for_respiration.html
    sha256: 305f1bfb2f1807189c4b43d3f3f510d6ea68a94dc2bb6365c006307b65930860
    role: context
  - path: pages/traits/metabolism/uses_in_other_way.html
    sha256: 8220ad04eebc34b69e20b3e4319bad8264b50773582e5ebe2ad0daff1208c0e0
    role: context
  - path: pages/traits/metabolism/wood_ljungdahl_pathway.html
    sha256: d78a403e44c4b69d5eec3a00442a3b3756e214a7a2eccda01e855a6999c56a53
    role: context
  - path: pages/traits/metabolism/xylan_degradation.html
    sha256: 4622cf5c62592be4341ff025d8d76759fe8ca5abe130c208ddf46d6280d476de
    role: context
  - path: pages/traits/morphology/akinete.html
    sha256: 9acaecff7e47ddca1e08a2d9e5ccf0d1ae2a6558272801d17ac057617a0f7064
    role: context
  - path: pages/traits/morphology/amphitrichous.html
    sha256: 19f9fb99ad6ad608df7da55211a897a0c2786836410745bc48bb1f2f7f1cb6c4
    role: context
  - path: pages/traits/morphology/axially_filamented.html
    sha256: bcb90212f63053daefb9b3d37fa6b513d47d91572730dff03beedb9b81cea549
    role: context
  - path: pages/traits/morphology/bacillus_shaped.html
    sha256: 45f8809d371b179393d1b048cc8168d9da4ebc1c6ae930feb3b21a7816139918
    role: context
  - path: pages/traits/morphology/baeocyte_formation.html
    sha256: 3ea5c7a9b7bbba34e6847ad1068e3aa21b6cca6348b9c3ce8384b386d837c000
    role: context
  - path: pages/traits/morphology/black_pigmented.html
    sha256: 9d50fcc78d731dd70fbfb783fe72a91a842fe15667956a0a133e53ccf024ff38
    role: context
  - path: pages/traits/morphology/branched_shaped.html
    sha256: fd030f1885b56bc30c1e6c09f9c8176eaaa9e07c45b228bf77931b0763344652
    role: context
  - path: pages/traits/morphology/brown_pigmented.html
    sha256: fbbb243bafffd9560d0526e7289a3b66601fb887161f19853864c3e152ed3327
    role: context
  - path: pages/traits/morphology/capsule.html
    sha256: 81d37a8c0aaa09cb0fbc10bee415c6731ed40da16d65b47fbce7bc18d1de1bcd
    role: context
  - path: pages/traits/morphology/carboxysome.html
    sha256: bbc1894fa96ca8877ea2036dd79860acd2fcde8f9af7a5adb8dd14f3ca863d47
    role: context
  - path: pages/traits/morphology/carotenoid_pigmentation.html
    sha256: a6c9e55bd8da0d6c5d23cfad87719ea5303815c59d60bcff95105237b5c39397
    role: context
  - path: pages/traits/morphology/cell_length.html
    sha256: b9e650563526c6ee7bc81714e4786031c3e692065f462ac1f1e5d2f2d098abd1
    role: context
  - path: pages/traits/morphology/cell_length_large.html
    sha256: 0e8cc2f6c6a27167a433ce29b4212b65c4df18b3b8c717c484457c90e5001baa
    role: context
  - path: pages/traits/morphology/cell_length_medium.html
    sha256: e617ae9ab26d2c4906915f41d49317ed9c35d1d1d0393f2d17996eda2507ba9c
    role: context
  - path: pages/traits/morphology/cell_length_small.html
    sha256: bd16471e19e62300ba1d35d7c59840c7ed184a925c085ac93918fc45c0bde8ad
    role: context
  - path: pages/traits/morphology/cell_length_very_small.html
    sha256: d152471d4abd4c811a74ff6a9b19483fe8df6efae9383578aa7663b4d4de1b4f
    role: context
  - path: pages/traits/morphology/cell_shape.html
    sha256: 9e1f0315e3eee378afd2a876da1a5fac6a088262eeedd613d4678707f9bd07f9
    role: context
  - path: pages/traits/morphology/cell_width.html
    sha256: b7b0a23281d38036ec97f30952038d4628d9ea2a0d36af99446dbcf696ca451e
    role: context
  - path: pages/traits/morphology/cell_width_large.html
    sha256: 087a2ee4e2d444a223393af6feb92412893f1b0e7a5600b9522c6f8182d27d64
    role: context
  - path: pages/traits/morphology/cell_width_medium.html
    sha256: f3cb09dcfec1ddb421cae6e91fecc6d842df293558186c0bba9637fa0df22e31
    role: context
  - path: pages/traits/morphology/cell_width_small.html
    sha256: 230fb759ca6e3e1ed2d59e1d1754027894bf6d736b2333eed80108334299f155
    role: context
  - path: pages/traits/morphology/cell_width_very_small.html
    sha256: 817e6bb0544a64c5f491a7a50454032a5e172b4de332e62023f41564929a4154
    role: context
  - path: pages/traits/morphology/coccobacillus_shaped.html
    sha256: 89aafb1951c83ce3da86f42b9e60c92c518ee63a2a7654ec8bc42b97f127a1ca
    role: context
  - path: pages/traits/morphology/coccus_shaped.html
    sha256: c14e1ca3bdf57dd6accf2302b2776ed8e800d75899166f80b293ed779dba88b2
    role: context
  - path: pages/traits/morphology/coenobium_formation.html
    sha256: e5bef4dda26e9014ac89e073ea76d3e8723449269fe037660c17cedb259c7a77
    role: context
  - path: pages/traits/morphology/cream_pigmented.html
    sha256: 879b086b71119225e06f04cf65c6b4221353f56da1386a8279734269331bc692
    role: context
  - path: pages/traits/morphology/crescent_shaped.html
    sha256: c519971f1e5a07344608cba4a754e147099133b547c6e7530abb6b0041f5f48a
    role: context
  - path: pages/traits/morphology/curved_shaped.html
    sha256: 390ac0aec386149ea9efc67f274cbb2128546c9fe434c662296db3678a7d0408
    role: context
  - path: pages/traits/morphology/cyanobacterial_multiseriate_trichome_formation.html
    sha256: 69ac922b266809d37903f2b0a75cbfffb500438ee6d51fbde70df04235032e72
    role: context
  - path: pages/traits/morphology/cyanophycin_granule.html
    sha256: 48f5bd27b054b28bb401c6e4eed438845e10bb52130a4afffd2d7e7a883f538d
    role: context
  - path: pages/traits/morphology/diplococcus_shaped.html
    sha256: 63f608112ebec0a92ff1db8815ad7f2ce8d99a40bc279a0fad136babfbdecb54
    role: context
  - path: pages/traits/morphology/disc_shaped.html
    sha256: 67f9b529e6ef1bec08cd04fdfbd9ec10e6da7079fc0ee82d0ce1f566c7959603
    role: context
  - path: pages/traits/morphology/dumbbell_shaped.html
    sha256: 1a1aed3eb40b23d8ba59f5be92ca735ff4f55d1cdee8d1a85777178560ce7d4e
    role: context
  - path: pages/traits/morphology/ellipsoidal.html
    sha256: 6d7987810dd3d41ccd8f8c28cb648db4a4b753e0326540bf8ecc87893cd9a4b9
    role: context
  - path: pages/traits/morphology/expansion_driven_sliding_motility.html
    sha256: e676ae0f094a888079faabd30ca16f37f639319dc67b4661d75f85292d63370c
    role: context
  - path: pages/traits/morphology/false_branching.html
    sha256: 58d50e6d5c1722f0d6db6aba69f042032930b13fa7215dd6636f0c31862b80ad
    role: context
  - path: pages/traits/morphology/ferrosome.html
    sha256: 45e6e9f794a8624467ef40285274e34c51d1330a6fd83586835e32f14582af4f
    role: context
  - path: pages/traits/morphology/filament_shaped.html
    sha256: 7a62d6c56f2822219f13f93f8a3cd6d54d0579ae2b5e6f32a3a3a7b58f375cde
    role: context
  - path: pages/traits/morphology/flagellar_arrangement.html
    sha256: 18314c4a9b328000386d4816f6fb735ea18cd74a37cf1f74f26319da922a1284
    role: context
  - path: pages/traits/morphology/flagellated.html
    sha256: fa8136604763290376a4191c14edf66f4b5cfa231347e8bfb7a6257803bce0e9
    role: context
  - path: pages/traits/morphology/flask_shaped.html
    sha256: 3efa927564168303420217586a6b793cf5ef6295beaded48ba79f6b48370bb44
    role: context
  - path: pages/traits/morphology/fungal_adhesive_column_trap_formation.html
    sha256: 672224b1dcfe50602f8613285c651d88bbc5f519d5a826798166ffca06d103a4
    role: context
  - path: pages/traits/morphology/fungal_adhesive_knob_trap_formation.html
    sha256: cee85e3055862ff86c7f0f10e9bc8cee2498591d34af51f6ec11d67b88380445
    role: context
  - path: pages/traits/morphology/fungal_adhesive_net_trap_formation.html
    sha256: 42fa99896ed99dd8a24f6dfdcaa2154d2914f8d32d17f3b0886dbd772d7dec90
    role: context
  - path: pages/traits/morphology/fungal_appressorium_formation.html
    sha256: 5e4f82e71afccecf1af7812c3db2391b8cddb6d54692b085d28cd37991af13ee
    role: context
  - path: pages/traits/morphology/fungal_arbuscule_formation.html
    sha256: ef20cc6578c640eec3353bb376ac22e184aa893490ef7f660dd1bcd7e9947713
    role: context
  - path: pages/traits/morphology/fungal_auxiliary_cell_formation.html
    sha256: 14aca7f3661224df66d05f0b019fe87cd8e99607b37a082392cf8a00dcf58a0e
    role: context
  - path: pages/traits/morphology/fungal_branched_absorbing_structure_formation.html
    sha256: e091e335edb0ed87d916e22a2814adfec8b62ebe48cc6b9398adb80477db7624
    role: context
  - path: pages/traits/morphology/fungal_chlamydospore_formation.html
    sha256: e105e1edc77b0624dc6567f13bcd3dab1d83d3395f407ec1cef9993ae839a56d
    role: context
  - path: pages/traits/morphology/fungal_conidiation.html
    sha256: 6c6b1c945d9d825fce241b22b32b6efb64863e07e7e2ccdd2e1f37a299fa07d5
    role: context
  - path: pages/traits/morphology/fungal_constricting_ring_formation.html
    sha256: 3b5c9dfa3e50140ca9a4bbf87d1976a22add6dde568399e2fc0f78a0b9ea34b6
    role: context
  - path: pages/traits/morphology/fungal_hartig_net_formation.html
    sha256: 5898daa32bf1f32b6ceb53962416d1fc644241d06d2fcb704d0dcb2349a91abf
    role: context
  - path: pages/traits/morphology/fungal_internal_mycorrhizal_vesicle_formation.html
    sha256: 867d2adb691b2629ab8c9867b5adc6243dfa15e071abe4efaf36e5650dee6950
    role: context
  - path: pages/traits/morphology/fungal_mycelial_cord_formation.html
    sha256: efc7fec6fcc5974ca64a9a0beb7edbe247534cbb4b314f0d5975f637ef49066b
    role: context
  - path: pages/traits/morphology/fungal_nematode_trap_formation.html
    sha256: c20a367b33f05ec9b9aa3ced4b62a1118290a086d24449de77adde6060e1f7f8
    role: context
  - path: pages/traits/morphology/fungal_nonconstricting_ring_trap_formation.html
    sha256: 9038a0ce8ee0de23765a4eda3aef00841d3beeda0f299d5eec826410eaf6f057
    role: context
  - path: pages/traits/morphology/fungal_peloton_formation.html
    sha256: ce4a047393ea2153d0852e8c10c3131b982ece308c6ae423ce7d18fec57ce508
    role: context
  - path: pages/traits/morphology/fungal_rhizomorph_formation.html
    sha256: 67f48452232e44807623e8619deea4b4f9d83f3d810403abb03f6237cedef41b
    role: context
  - path: pages/traits/morphology/fungal_root_mantle_formation.html
    sha256: e5fea279d503a68d29d2ba3df2893e9218be290cf02d8f8b536159b5b007ae24
    role: context
  - path: pages/traits/morphology/fungal_sclerotium_formation.html
    sha256: 0209a6eda56459b41152a824460b459554a28fec94c28d439e1eda06b2d7985c
    role: context
  - path: pages/traits/morphology/fusiform_shaped.html
    sha256: 2c2dde74c33f96024258023fa65ffd2a7b656783f46d80d9bcb1dc519770afdc
    role: context
  - path: pages/traits/morphology/gas_vesicle.html
    sha256: c28891149e2c8481c0cd1e714e31266bde12a33136377e75596f5d7751c69dac
    role: context
  - path: pages/traits/morphology/gliding.html
    sha256: d78676105f33790e70770fc03062ccb77ca4434b242965da205e2976c53b4134
    role: context
  - path: pages/traits/morphology/gram_negative.html
    sha256: bbbb909082e6073ad3ed41b704e7ebe8a676f2229b144940f43214018973ac2f
    role: context
  - path: pages/traits/morphology/gram_positive.html
    sha256: 8f9834a3ce6da3ed5fbbb29e4d486837ebfa867ee1024bded972d1a783e05e02
    role: context
  - path: pages/traits/morphology/gram_stain.html
    sha256: 94c88fc15f0dae735c77ec798790437aed9876c75cd003c3b2600bd72f5e67f6
    role: context
  - path: pages/traits/morphology/gram_variable.html
    sha256: 0dd36b2f49628ce89953bdc2c72ffd28e41bcc2f7fe99c48bfaccee9837b8384
    role: context
  - path: pages/traits/morphology/green_pigmented.html
    sha256: 253cebed3a217476eb80a93eed6054775960a1b3837a9e4b7d023c56957218c4
    role: context
  - path: pages/traits/morphology/helical_shaped.html
    sha256: 0fed3de169d57ad092d490722f7d58aac954942c2cf127d5e97f246dfffc5fc3
    role: context
  - path: pages/traits/morphology/heterocyst.html
    sha256: f9e99b1e6567ec8efde05e643c22c41a812ff39c12a594f0f683674b3e863d4d
    role: context
  - path: pages/traits/morphology/holdfast.html
    sha256: 875686b8e7484e3f934793d76a2b0ad38c28369f695759d81167fa05e722bf56
    role: context
  - path: pages/traits/morphology/hormogonium_formation.html
    sha256: 971909100d2d128815b6847d7260d2556261a7a84ea3a53d5ecddc11bca3f935
    role: context
  - path: pages/traits/morphology/intracellular_inclusion.html
    sha256: 653663ced72fca3402125a97bbd0a43a42d92de472ab35567e5fdb4928830c7f
    role: context
  - path: pages/traits/morphology/irregular_shaped.html
    sha256: 17144587916ac3491f3cd3dfd61eff4dfee5c2cbf95701ebb869df5ec52760a4
    role: context
  - path: pages/traits/morphology/lateral_flagellation.html
    sha256: da924d7d2975820adbb87c6833c431bf08db443136475ab9f599502b7a86f88a
    role: context
  - path: pages/traits/morphology/lophotrichous.html
    sha256: ee40b21a33bda05daed8d40e290c496d16e8e211687aa9b705a4ab465b30b9b7
    role: context
  - path: pages/traits/morphology/magnetosome.html
    sha256: 76a0de5a4e48378e5a2713cc944fbf26905f05db94557ffdbdeada5210e2da93
    role: context
  - path: pages/traits/morphology/microbial_haustorium_formation.html
    sha256: 79f33ad9766fabea7c13e92370731fb641fe6deddc0a1f80434a0795a21b9c43
    role: context
  - path: pages/traits/morphology/monotrichous.html
    sha256: b807b5735e5acf8eefa76bf191135d1f4c6d2ac5706cf9181dd824a07bfa1725
    role: context
  - path: pages/traits/morphology/motile.html
    sha256: 09950b333bb0d5754d89a472b66d61335ea36edcf1c08946ecc97480dd4bfda4
    role: context
  - path: pages/traits/morphology/motility.html
    sha256: aa5394ca0c8a868cf1b2be0ea021f52a9838353492db17e1cf2ddfe61c087519
    role: context
  - path: pages/traits/morphology/mycelial_growth.html
    sha256: 29eacaef8258ea8934b6083772247c658d8c4f5403991bc5c82329885474577d
    role: context
  - path: pages/traits/morphology/necridium_formation.html
    sha256: b6d3dca1a99402148a17ae3b03539a05c160b9d1101a676409188051e58abada
    role: context
  - path: pages/traits/morphology/non_motile.html
    sha256: c7658d2a75934b3c4d5d38deee83389903facaccb2978f8c3a7c32964589ff58
    role: context
  - path: pages/traits/morphology/non_spore_forming.html
    sha256: be8459375eb76efb6ce2a0ab226b7281d52843c856a81e5e1a9ef071d05aa3aa
    role: context
  - path: pages/traits/morphology/orange_pigmented.html
    sha256: 4b1c9157dcf88dfd87b3c886adc5b126fcb0114823c0716a2b8185a759d8455d
    role: context
  - path: pages/traits/morphology/oval_shaped.html
    sha256: 001226ffb58fbdec88c340d01aea6bd742d6961ab1b239701c88240e771bde73
    role: context
  - path: pages/traits/morphology/ovoid_shaped.html
    sha256: d0162342698fbd7cb7b95f78ee9ccd92771aa4c547a92d8b9d8c2c749ef808c5
    role: context
  - path: pages/traits/morphology/palmelloid_formation.html
    sha256: 4d890fe949e0c3ed552fd3aac69eb063ab3a2955647bc3942fa548c21c939937
    role: context
  - path: pages/traits/morphology/peritrichous.html
    sha256: 16e6338798c187f92dfad459e7dfa6a28b350957a3e1198dc187f181b1771924
    role: context
  - path: pages/traits/morphology/pigmentation.html
    sha256: 90b867a91852e1c86036ea22f3a0fe9e7b38ed8ca59f1d291fd4a54799bfdcdc
    role: context
  - path: pages/traits/morphology/pink_pigmented.html
    sha256: 3d612ac8c9bd8982810fe947ceab1b9fcb6c9a261e52a5fd1f6fc8495f362b46
    role: context
  - path: pages/traits/morphology/pleomorphic_shaped.html
    sha256: b949955b78bd08952f690bc611de8f049fd56e273d0df26b8f4580ea87f76b13
    role: context
  - path: pages/traits/morphology/polar_flagellation.html
    sha256: 01c52ab6364357b28628621e442e5bb800b05a70d56c5fe9010bfbde01d6fe46
    role: context
  - path: pages/traits/morphology/polyhydroxyalkanoate_granule.html
    sha256: 03905b03802b992a80b5c8415b5a5c1db0a00acdbd0576e1637fd9072e03d400
    role: context
  - path: pages/traits/morphology/polyphosphate_granule.html
    sha256: 354269cd5990802971a3d0f8cdc123beca352e6a29dfe65bec6fbead5fb84fd3
    role: context
  - path: pages/traits/morphology/polytrichous_flagellation.html
    sha256: f91a943c3a4d4d3b22d0d70db6d1048e6987aa005b4011eeca1bbdfc2ad7d8a8
    role: context
  - path: pages/traits/morphology/prosthecate.html
    sha256: 6b986a5f38b838e24726d69a2078f2da5a780ce0d29f62cdde81eddf5628a27f
    role: context
  - path: pages/traits/morphology/pseudohyphal_growth.html
    sha256: 888925c060c59883cf15130972b8acf065593c38742fcf1dd0c160fa70cbccc2
    role: context
  - path: pages/traits/morphology/red_pigmented.html
    sha256: bfa9013ac200231ca334124e6dd43c6e9e00b295345eb56c35efd082d7c8e322
    role: context
  - path: pages/traits/morphology/ring_shaped.html
    sha256: 1ee0c393a1204a3837dd08cc9eab0b80d0cd97964070d6cee154f472ee0b33ee
    role: context
  - path: pages/traits/morphology/rod_shaped.html
    sha256: 65fbae9ef18be5f77bbd430d09244d8f6292b03c704e088268f0b4e94b05393c
    role: context
  - path: pages/traits/morphology/rosette_cell_arrangement.html
    sha256: b04ab440f7e440b511eff3b818993911ae7463f26476ef6dba17ed4c350df788
    role: context
  - path: pages/traits/morphology/s_layer.html
    sha256: 9dcf2b5648affcf5fc8e9407e9e8d68919464b9764c347ed55f63d28ba0a8d6b
    role: context
  - path: pages/traits/morphology/sarcina_arrangement.html
    sha256: d26ee09f7633d7f8128b50352fda14ae564a2097adad8b343b97a5376eb67031
    role: context
  - path: pages/traits/morphology/sphere_shaped.html
    sha256: 7d5db72ebbd41080371a2aab7c69ef9d0c44e72fa13f67ebe734b68ade641699
    role: context
  - path: pages/traits/morphology/spindle_shaped.html
    sha256: 92f14b4e9a6ef037dc5cab9722be8560067ed43e8991373114292f311654c33e
    role: context
  - path: pages/traits/morphology/spiral_shaped.html
    sha256: 5ad1d4660a79798c3c1d72309a268e7e20852126b975892c520fd6771f1ba519
    role: context
  - path: pages/traits/morphology/spirochete_shaped.html
    sha256: 9e515870475019f83f8e44f44bf4bd423b511726960a36342802098e1f2c0b63
    role: context
  - path: pages/traits/morphology/spore_forming.html
    sha256: aeaafc00bfce464e68d205c8e05eab2a13bc42bab6316d66ef1e24561ba0dbcd
    role: context
  - path: pages/traits/morphology/spore_shaped.html
    sha256: ff6f3bbf2dc910b94d14e854375f276f4387c5164e2c00439d62081792ab7618
    role: context
  - path: pages/traits/morphology/sporulation.html
    sha256: be6e7bf18e25b99d218c2781e2dc30790916e20f9e6b059c8cacb6ef2ae64a12
    role: context
  - path: pages/traits/morphology/square_shaped.html
    sha256: fc2f2e0ebdf99122f52e98fdc9b20bc1ed574db756988ec9e55a126011c536ce
    role: context
  - path: pages/traits/morphology/staphylococcus_arrangement.html
    sha256: 6c375f48c9e5632167500a8e5c19e07710cacb2cc45edd8ad8e929760750d63a
    role: context
  - path: pages/traits/morphology/star_shaped.html
    sha256: 0d8491a43271fb65b33b5ac9b4a2bf7c24ebcad2c87e7ae964e8ccaf0240e373
    role: context
  - path: pages/traits/morphology/streptococcus_arrangement.html
    sha256: d91c41ecacc120e4591e620bbe271b8f9ed2a17343e59075599fede1f4d633d0
    role: context
  - path: pages/traits/morphology/subpolar_flagellation.html
    sha256: 33d7e6335909367ba9091914e19b98b6123e2ac1f398c1c616f41b7cc33f2f5d
    role: context
  - path: pages/traits/morphology/sulfur_globule.html
    sha256: e143d8593efa260231badb4712cdec5cda8069628a521b921b00dce78ba44b23
    role: context
  - path: pages/traits/morphology/swarming_motility.html
    sha256: 69eda905bbac6d51a69f936c77fccf7f68613cf98c0c36ee97355ea0bdd3c388
    role: context
  - path: pages/traits/morphology/swimming_motility.html
    sha256: 5e793c7698dd0fbff958b2486d39efd6af996af03b9f305a1546ccd06c1d871b
    role: context
  - path: pages/traits/morphology/synnema_formation.html
    sha256: 48832fa7b41b13644c499b7f9247254b50c978e1ab8fabde6cb02d0ba7a8a23a
    role: context
  - path: pages/traits/morphology/tailed_shaped.html
    sha256: b94cb889dd58e844fc5e8837ae0fbab04255395e421cccbddebafd1497159736
    role: context
  - path: pages/traits/morphology/tetrad_arrangement.html
    sha256: 68b27df63c444fa51309909730607c7e1ced9755c7e3ce05cec0d905155a25b1
    role: context
  - path: pages/traits/morphology/triangular_shaped.html
    sha256: b480ec6644d8c2d77315bc5f84946257e6cf05c153fa6a10f6e3ded4b1c2c6f7
    role: context
  - path: pages/traits/morphology/twitching_motility.html
    sha256: 61531fa28f5d214dced34178ad7625593d5d494eb2034a22ac7bf78e02dfc22b
    role: context
  - path: pages/traits/morphology/type_iv_pilus.html
    sha256: cadd8373603b524febc3f71d6b65fa46433e4f367e1248e9d99909be76513ca6
    role: context
  - path: pages/traits/morphology/vibrio_shaped.html
    sha256: c2a2acbfa89932ddbe8ec1defb000c29a65d7b607b0011b5add40a9b855defeb
    role: context
  - path: pages/traits/morphology/white_pigmented.html
    sha256: 153938e56c56ce1751a34d59a4440c1332465ade48f020d9ff97e04b14362b06
    role: context
  - path: pages/traits/morphology/yellow_pigmented.html
    sha256: 0823c447459d27880e77c0b36061710c526b292d9efd9096da27227ef61d11e8
    role: context
  - path: pages/traits/observation/growth_nacl_observation.html
    sha256: 106c979d00f6d1bf9ca8a9a088b09c4db0cd11be038207e9dcb6b16b097e659e
    role: context
  - path: pages/traits/observation/growth_oxygen_observation.html
    sha256: 75019a3b04ee815bf1ef2bff97f2c59ca12af432645abd194612a58856c85908
    role: context
  - path: pages/traits/observation/growth_ph_observation.html
    sha256: d60944bd3bbc40fd84e0b198b9c0a8543e270b051ae636b794869876582068b7
    role: context
  - path: pages/traits/observation/growth_temperature_observation.html
    sha256: 6df18e28df14c907c9969e6d0c1ca31629f7340a93ee728bf02f47783c486c54
    role: context
  - path: pages/traits/observation/nacl_delta_observation.html
    sha256: 5ec9ddc3a118827fad16541084cf45e35b7e9b5e13ee72649f178b69286de791
    role: context
  - path: pages/traits/observation/nacl_observation.html
    sha256: 3a4669d0c70e27a6e8c0fa391263aedfa96b55971f9153f282ae60fb9615d13e
    role: context
  - path: pages/traits/observation/nacl_range_observation.html
    sha256: 2bfb7a63f68deebeb82ce7e1c59c0e97afd1942f7d6621c5326a5e54c580354a
    role: context
  - path: pages/traits/observation/optimum_nacl_observation.html
    sha256: 194c47febb02d405c7ac2ec9cd96ccff441a107dcd67ba9f4353f0a988169190
    role: context
  - path: pages/traits/observation/optimum_oxygen_observation.html
    sha256: 6b4c8be7d3cb57444d23fa12ace15962cb672010849e473a1c7546d2a087318e
    role: context
  - path: pages/traits/observation/optimum_ph_observation.html
    sha256: 0788cb8459372a2f0efe7cba56c534b03ddc34b5a3a9858567640dd3a8753f7a
    role: context
  - path: pages/traits/observation/optimum_temperature_observation.html
    sha256: 9b184843234b9029c7ef9a8b1664c4cb1b7b13360881cecadd16f9cf8099da56
    role: context
  - path: pages/traits/observation/oxygen_delta_observation.html
    sha256: 12c56e8ca080f16ff971fbd4ca4bfc059b644f4eedc8237a15f0b110db495708
    role: context
  - path: pages/traits/observation/oxygen_observation.html
    sha256: 9af2d94b6477d9671c32b563d13f74f5e56369a320820de770e7d5fae6304dd3
    role: context
  - path: pages/traits/observation/oxygen_range_observation.html
    sha256: 53c3f27970b00ff03678e77d4cd5be3798d11bb4c2502573d8ce492e836c3a78
    role: context
  - path: pages/traits/observation/ph_delta_observation.html
    sha256: 941739340cab18af18ddc86014492eb6e283ad611193a29e825f4d6411f93a04
    role: context
  - path: pages/traits/observation/ph_observation.html
    sha256: c2c3e917eff0416702cd4dd81395aff7c9010e1e80a52e54f0f7370ab810fdb4
    role: context
  - path: pages/traits/observation/ph_range_observation.html
    sha256: c6350f18e5a72d8f566b42240be0ad6668643cc0bd3dd1e2e525f346c543d218
    role: context
  - path: pages/traits/observation/temperature_delta_observation.html
    sha256: 4219bc6775d94268ede12c433efd6dbb9d59210eed29fc03901955fa7400011f
    role: context
  - path: pages/traits/observation/temperature_observation.html
    sha256: 3a81a94b6a3a00fe63274d90a16dadc104b33594dd20fdd9de7fe04ca89b1931
    role: context
  - path: pages/traits/observation/temperature_range_observation.html
    sha256: 3e46b77bd3bd2eb518242c87f08be642e9613e0baa4b90132e0b14134d6474ca
    role: context
  - path: pages/traits/other/catalase_negative.html
    sha256: f63efee5a19af4fa1e8e0f10eee89e28c8bd05ee172a8d2ae97e199021ec4783
    role: context
  - path: pages/traits/other/catalase_test.html
    sha256: 12ae6d908aa9b66e037a6340b6643edba98d3aacdd3da7435c3762c0af0467ae
    role: context
  - path: pages/traits/other/circular_colony.html
    sha256: d7f5c31ac046133871b187944687bc3d8ae3b7680607ee4e3d5eec4f6ba06115
    role: context
  - path: pages/traits/other/coagulase_negative.html
    sha256: 447ecedc760db45f48ad813af15997347083a371536902702341bfc9c3639cb3
    role: context
  - path: pages/traits/other/coagulase_positive.html
    sha256: af2d9b3d8cfa1834d6c37d15585bce2ebc6d7ae4e56ea59051a8a242dc5e8645
    role: context
  - path: pages/traits/other/colony_morphology.html
    sha256: 4c4080f7cbd6461c277a00bcb21cf036b7005018db3a9fc95e4fbd94b550fbf2
    role: context
  - path: pages/traits/other/colony_shape.html
    sha256: 9d0c1145492be53e13dd426f195fe45dd0f9d43b171428c0f12131a5218e8706
    role: context
  - path: pages/traits/other/epibiont_phenotype.html
    sha256: 4570f7e28acc6d8fa79662cdc7a3b25b11f86cf95514ebfcd560a16a8403f12f
    role: context
  - path: pages/traits/other/filamentous_colony.html
    sha256: 0e75b9f8810024452a3469e1782a34cc4e296b4f41a4a1d121d27a226c23440c
    role: context
  - path: pages/traits/other/fried_egg_shaped_colony.html
    sha256: 444e19d6f648839c5934fea8606f46c8fa611c2740ffc014514ba9a81688af23
    role: context
  - path: pages/traits/other/generalist.html
    sha256: a9ebf18e0d7c07f18c390143aff8f117fc022d5a8133baebc2f59047bf01a385
    role: context
  - path: pages/traits/other/hemolysis.html
    sha256: e16a7e4acbccffa34d571d7938b0cf57a5aa8aacd17c57f432cc1990b437352b
    role: context
  - path: pages/traits/other/hemolytic.html
    sha256: d88d6f4f55cf2d039423d0f317006e1f14168974b18bed59798f769ab33c0915
    role: context
  - path: pages/traits/other/indole_test.html
    sha256: de51456670abca9bef57d16a3a9451053f909eefaa39c8e5e7bbb42da303fffb
    role: context
  - path: pages/traits/other/indole_test_negative.html
    sha256: f20afab28fd2c93b1972e8f2fad78fb8fb9de730beee0b7c85b304140805ed83
    role: context
  - path: pages/traits/other/indole_test_positive.html
    sha256: d9a4a8255913dbf93ab9e3c6cce88291509745fed235b2365578f6d2c468ec75
    role: context
  - path: pages/traits/other/irregular_colony.html
    sha256: daa31281e6c5fd347be5e1edbdc5f82871a414bb46487e1784ab3eebc8cbeb72
    role: context
  - path: pages/traits/other/methyl_red_test.html
    sha256: b28acfb65f31244bb2cf117ee0e44e6a1665b6ecda98b3b00db19b397d784f43
    role: context
  - path: pages/traits/other/methyl_red_test_negative.html
    sha256: 6202f1d34c5f0823977230c36661aa91fe0e09569973820b84fd544048721fa2
    role: context
  - path: pages/traits/other/methyl_red_test_positive.html
    sha256: d327988a1da876875d1fce673569cb4b6a65ced5c06183205b7743960c8fda44
    role: context
  - path: pages/traits/other/non_hemolytic.html
    sha256: b507fecfe7beea4eee0d7ffe2dfae10a775730d5808ad5038c0693bc393bbb43
    role: context
  - path: pages/traits/other/osmotic_tolerance.html
    sha256: 9e1b3cd89b784f3153c178bf4e8ba349944d3639d4c9a4e2580b89c925273827
    role: context
  - path: pages/traits/other/oxidase_negative.html
    sha256: 2941edc5f01a62833af80dd2e7bfc111923302adaa7a51914cc9bd82b61056b0
    role: context
  - path: pages/traits/other/oxidase_test.html
    sha256: 5def16be896a0ea7fd4b02db98d2ddd6431e61638fed09f6ccfcbb7d83323ed7
    role: context
  - path: pages/traits/other/punctiform_colony.html
    sha256: a60b05f0cdd06758a96d012e1bff67f8dbddd5d32dbec9f68f50077112e41346
    role: context
  - path: pages/traits/other/rhizoid_colony.html
    sha256: ce1f8b32d7beae44a25d1f79684ecbd5f82fe140e197ec9880c01e53c23e1b71
    role: context
  - path: pages/traits/other/specialist.html
    sha256: 7f33e009e6a7b98c8fc23b2759b2dd21cea57e825a3194c57d02ab165f771694
    role: context
  - path: pages/traits/other/urease_negative.html
    sha256: 2ec16f2478d648a2b7a6e42ac066a9d4da6b3b2d45fc81748fb23eeab2f2c4d8
    role: context
  - path: pages/traits/other/urease_test.html
    sha256: 1332a7cb89e9f8e580ba4f7f671e534f725fae90baeb605cd91131200221a2a5
    role: context
  - path: pages/traits/other/voges_proskauer_test.html
    sha256: 53eb1222cf140ffc7a430b74da1f7a06c982f681c574bb163963a08dfbbbf2d5
    role: context
  - path: pages/traits/other/voges_proskauer_test_negative.html
    sha256: 059156e46e22b1eb10489a88c100280ba87aaf16599fe5f136854d3d832e3637
    role: context
  - path: pages/traits/other/voges_proskauer_test_positive.html
    sha256: 657ab1da0647d6361fed8d60d5b63ede75db5e99b9783f7a85393939222a9d62
    role: context
  - path: pages/traits/physiology/acid_phosphatase_activity.html
    sha256: cb892920f4a969dc2ca9564f8790f74a8ed6790aafeb70cb4e316312da430f17
    role: context
  - path: pages/traits/physiology/acquired_stress_resistance_memory.html
    sha256: ac700801cc59778f1c949a11de5062b4488ca43f7384156722013cdb94e8b4d9
    role: context
  - path: pages/traits/physiology/aerobic_anoxygenic_phototrophy.html
    sha256: 789475bd62f6edcee2bd39163aa58ba5f2ca90d5302d350e877fdc0a73f72c77
    role: context
  - path: pages/traits/physiology/aerobic_overflow_metabolism.html
    sha256: 7c8d7b569e367aaa16d6306dba02abd2d021e5bf43edf102cb9d105e2f0e2986
    role: context
  - path: pages/traits/physiology/aerotaxis.html
    sha256: 87662cf578d05d1b9781a9473b59490636d9054e30c70b4645ede2401eceeb96
    role: context
  - path: pages/traits/physiology/aerotropism.html
    sha256: 3958dce272542f50c5421d16054db87169491ab42ba244378b81f073f8df931c
    role: context
  - path: pages/traits/physiology/aggrephagy.html
    sha256: 3c254e49a0365e5dc12ca7fbdea80e3692c78128fce939016e8b7f71ef658bc6
    role: context
  - path: pages/traits/physiology/alanine_arylamidase_activity.html
    sha256: 3e7af2b8d99e3668b824d0277a247d802208d8a94c66803207ec6694425e3c6a
    role: context
  - path: pages/traits/physiology/alkaline_phosphatase_activity.html
    sha256: 5f29799873857c9b5047c907bd2fa3b62a6db53375a9b0ea4b44ee9a49ec1c4f
    role: context
  - path: pages/traits/physiology/alpha_chymotrypsin_activity.html
    sha256: 3574b6568234426d5351995e65857f5492c4232b841bd99603e75974415fa407
    role: context
  - path: pages/traits/physiology/alpha_fucosidase_activity.html
    sha256: 3325bfa4c33dfa7a3309d480a190ff703e9edfca5d5f69fe333fcb565379c1c5
    role: context
  - path: pages/traits/physiology/alpha_galactosidase_activity.html
    sha256: 9b39ecbeb5105a2b9f3f018798e07749a2f460ef44fb3ae4ee704c90ef49f7db
    role: context
  - path: pages/traits/physiology/alpha_glucosidase_activity.html
    sha256: 8e38870879d42f25a9812625a352cebe8c6568ab1449d4ba6efe24c87084e2cd
    role: context
  - path: pages/traits/physiology/alpha_mannosidase_activity.html
    sha256: c44c2e3a88faa0b930792f6d9301780f59505787161704b0e7392dc350befc2b
    role: context
  - path: pages/traits/physiology/amylase_activity.html
    sha256: 718945fedb757265e3597b174a3ccaf30cadc5b99b118a8ff68c42152cb925ca
    role: context
  - path: pages/traits/physiology/anisogamy.html
    sha256: f9049a87278df9c51690bc820063ce28511f47854a850e3b7c088c0746790fc8
    role: context
  - path: pages/traits/physiology/antibiotic_resistance.html
    sha256: da6ee9ac6454a05d331b1773bbbaf02aa11daf597bec63633113a873ef350846
    role: context
  - path: pages/traits/physiology/arginine_arylamidase_activity.html
    sha256: 80ab1786607f72dc65861736bd0144c46c3141c355ebcb4b5e451e1704eb7fac
    role: context
  - path: pages/traits/physiology/arginine_dihydrolase_activity.html
    sha256: 123fdd2585c996f8c59d96be8d767d169dc3629fd27b2cd68d5ff2e93a9e8ebf
    role: context
  - path: pages/traits/physiology/autogamy.html
    sha256: 1ddddf7e1cc30fccab8b4f24bebbdd9fbad3c7ee52c2d117280b387c815ac09e
    role: context
  - path: pages/traits/physiology/automixis.html
    sha256: c37c46260ee04e25246f5b8b6dfb1420a0b4dbf7daaa65aaa96aef980bafd727
    role: context
  - path: pages/traits/physiology/autophagic_glycogen_degradation.html
    sha256: eeb4ef32a5470f40626444d8cff8812b551af58e6baf3f8e1a98efd38626ad18
    role: context
  - path: pages/traits/physiology/autophagy.html
    sha256: 498b6fd69016a4aa6a6ad8f1b864eb6a574fcdadcc0e503fc1a2f99931675609
    role: context
  - path: pages/traits/physiology/autotrophic.html
    sha256: 572858a2b22304cf9812c0d6aff605f2f0e25af05d546cc2cc0aeb169a1027da
    role: context
  - path: pages/traits/physiology/bacteriocin_production.html
    sha256: 0fbcfb3a6719a32cedf42e5cac3ec10fa1ab665392d26194d18f9f206d10382a
    role: context
  - path: pages/traits/physiology/ballistospore_discharge.html
    sha256: 45704b4ce7bf68e8085b65009c341d3483b88938469fd5023b9c4dfac966ab1b
    role: context
  - path: pages/traits/physiology/behavioral_habituation.html
    sha256: 095b96200744eedfa02adbfbc0deaf286c8e20fa1eedd6be7b454d41ffe93bf9
    role: context
  - path: pages/traits/physiology/beta_galactosidase_activity.html
    sha256: b53acde4d21b86ac609b2559bead0a9fdda8a1dea961df08b264e4886b4c4c46
    role: context
  - path: pages/traits/physiology/beta_glucosidase_activity.html
    sha256: b9d27c4e4afee11ac59d603f4496528ba313a106cd771294e602bf9fb844e024
    role: context
  - path: pages/traits/physiology/beta_glucuronidase_activity.html
    sha256: d3f40cbe83387be1c50e83e8e58212cd0eae7e219d8277afc65170fafb6decf5
    role: context
  - path: pages/traits/physiology/beta_n_acetylhexosaminidase_activity.html
    sha256: 1a39b9eeedcf8f100f62078bc771f89615879ec4dab0e665bb8419d389a45594
    role: context
  - path: pages/traits/physiology/bioluminescence.html
    sha256: 76fcaef6d6f97283a8e62b8bb9baeb4eb9d5060ce1a94c3ae0e3c715b517fb60
    role: context
  - path: pages/traits/physiology/biomineralization.html
    sha256: 62db066c0101b0601f2bd4d567f2d255f41065357938af86e5e5da0229f0da8a
    role: context
  - path: pages/traits/physiology/bipolar_mating_system.html
    sha256: 03795e50dde236359daf0a1d89787de819e7f15d728ad2b2ead0d9fdaaea0d6a
    role: context
  - path: pages/traits/physiology/carbon_source_memory.html
    sha256: d325179a102c5f49f612cbda78f8051afe9ccea42965e80a63a7d7b146e81c95
    role: context
  - path: pages/traits/physiology/carboxydotrophic.html
    sha256: d2ab304c6d8416ecdb7b84717c73a8a30b8dfa13055de58193427eef19b3e275
    role: context
  - path: pages/traits/physiology/carboxylesterase_activity.html
    sha256: 0bb1de3c92f2bca704b1ccd0d4e9e09e64e7f2950f1c0898cf45b82db467b311
    role: context
  - path: pages/traits/physiology/caseinase_activity.html
    sha256: 40e43d90daaa56e0054e33b371cb08880cf61ef98f76df14dfdce88481ff4a7c
    role: context
  - path: pages/traits/physiology/catalase_activity.html
    sha256: d60df0417a14dc873847158e0b677c874d6ecc979f9f1b1bc73f5cbc8db6488e
    role: context
  - path: pages/traits/physiology/cellular_buoyancy.html
    sha256: 4864da2a6d24e702c07a39c379fc03dc2c8914ca270cb002ecd950012ad75c69
    role: context
  - path: pages/traits/physiology/cellular_rejuvenation.html
    sha256: 4042af2c176dbd36518d786af29d778727be5b39f8230319f2744ef81423a5f4
    role: context
  - path: pages/traits/physiology/chemoautolithotrophic.html
    sha256: 88df940f1c53448fe2cc555191a91873978a1ea20b1ebbd2a6742754373c26c4
    role: context
  - path: pages/traits/physiology/chemoautotrophic.html
    sha256: d0522e530dc4e32aa51eb9f1a745a56bf578abcd2d8f949db02a85976317e556
    role: context
  - path: pages/traits/physiology/chemoheterotrophic.html
    sha256: 2a5dbed84b5770426750750ee79fb42dae6dfe1e8db257dcf3793e4d7e64c8ab
    role: context
  - path: pages/traits/physiology/chemokinesis.html
    sha256: 844aa11b6a552c53ed8453faa692f0636875e54088c1b9b855cc0b85ae88c23a
    role: context
  - path: pages/traits/physiology/chemolithoautotrophic.html
    sha256: e69d9908bac2c6f0e343d86215a9d650e0586e923da7c65c8b5f1f824f1a0cbc
    role: context
  - path: pages/traits/physiology/chemolithoheterotrophic.html
    sha256: 4606dfdc17f55456788ec2e40940cbb3f0a4d821b7d667e1a22b4f8469964195
    role: context
  - path: pages/traits/physiology/chemolithotrophic.html
    sha256: 5cc6218819b8e6ba7284cf38dcadfa34bae4e3166ee406e93814dbea47d4be7e
    role: context
  - path: pages/traits/physiology/chemoorganoheterotrophic.html
    sha256: ee7d47fd2ead5705964438b02d262f7b4a81b00bbfaa71951e18ef6240e5017d
    role: context
  - path: pages/traits/physiology/chemoorganotrophic.html
    sha256: 2136772139a095dd53dc6bb1a61bff2f21fc4e11c485f97490427c9c35c8cd88
    role: context
  - path: pages/traits/physiology/chemotaxis.html
    sha256: 0528565519c4f43b96e9872e4fe2f8b91e2e537c37e511eed9b0deb6a5a887a2
    role: context
  - path: pages/traits/physiology/chemotrophic.html
    sha256: f572a46dae1ebfbd304b11d17f2bee27b973a1f05c6774a94fc82e6a7d7f4743
    role: context
  - path: pages/traits/physiology/chemotropism.html
    sha256: 5853edf2f28032257fc3827f25daeac81069712ba8a54561ffce864b8bf54030
    role: context
  - path: pages/traits/physiology/coagulase_activity.html
    sha256: cc5615616e466d265dcee3deb7e3b18df068a0d1ff857e813781860286071523
    role: context
  - path: pages/traits/physiology/coccolith_production.html
    sha256: f093ab253bc4bdd48adb5ebd956ceb6a0a2d6d28b313d2cdfd75eb99751c019e
    role: context
  - path: pages/traits/physiology/cold_shock_response.html
    sha256: 14e9dbcebfa5750f3f3bb7bdfb7842e10ddf2bf13612fdc0687c1eeaa29933d4
    role: context
  - path: pages/traits/physiology/contact_dependent_outer_membrane_exchange.html
    sha256: 95839f273cb9644cdf547456daadeb75eef51f01b4bad83a8aca491a1cdad3a8
    role: context
  - path: pages/traits/physiology/copiotrophic.html
    sha256: c7d73f8534d5a1447e7e37e1499a03ec289390274e83b8405fa2a696ab8a3bd6
    role: context
  - path: pages/traits/physiology/cue_triggered_environmental_anticipation.html
    sha256: 447d5771869fa0501a43dd68368c1c01c560f8a54bed53a0432b9af9fd2fa67e
    role: context
  - path: pages/traits/physiology/cystine_arylamidase_activity.html
    sha256: 40edb56a8815d29c130ae649bdb3ed057634565204a05bbbd6ca7068a2a44daf
    role: context
  - path: pages/traits/physiology/cytogamy.html
    sha256: 4f86cdf0e3ed74a6c2559eff09698dbe7e034c034204a812e846f12dedc558eb
    role: context
  - path: pages/traits/physiology/diatom_frustule_production.html
    sha256: 2d4316a4c978761f64e23c4800a0d7a97ee95c5b66dd863f2d1c295e7bf61191
    role: context
  - path: pages/traits/physiology/diatom_perizonium_production.html
    sha256: 504ee9a5320b0d1d5ebef7afe1d6bf6908e48ea8703b82b31d1872e4affc0040
    role: context
  - path: pages/traits/physiology/diatom_seta_production.html
    sha256: deb152e7a3b141a216791cecaf95323acfa6d862032bd2c61c4e44c267ebbd72
    role: context
  - path: pages/traits/physiology/diauxic_growth.html
    sha256: 494cf9008ae3e24a2a63f0db075262d3274a06fb4e4643d493053059d85a2530
    role: context
  - path: pages/traits/physiology/diversifying_bet_hedging.html
    sha256: f8fb545b34da2e88fd032cd3205ba38576f0aa2128896a59a5a772efdca0f272
    role: context
  - path: pages/traits/physiology/dnase_activity.html
    sha256: 12a0f8086d276c0de741c6a8f73e709686d9b2047ff36ba4e020fbc3079c94e8
    role: context
  - path: pages/traits/physiology/dormancy.html
    sha256: 3d92eebb73aa0e8fb726137a5bb5a3b454d8d767c769c35f4118c1abf07d437c
    role: context
  - path: pages/traits/physiology/durotaxis.html
    sha256: 4e816c65cbdc4b9a95eaefe1f139338fe8785fddfc9543cda5f6082506de4cd9
    role: context
  - path: pages/traits/physiology/endocytosis.html
    sha256: 89e217f4f3ff60a4334ed6ee797426ed560f1f2e351d63302dd3d61b34e41c5d
    role: context
  - path: pages/traits/physiology/energy_taxis.html
    sha256: da8bb2f4da8e3cbda7133dd4c203618e1d158b7f8bbc9626f4f2544a2b1a0cdf
    role: context
  - path: pages/traits/physiology/enhanced_transcriptional_reactivation_memory.html
    sha256: 073b2d8b88e62cb9924b44e9dc84259162f01334b8f2284738e262714fc7bbea
    role: context
  - path: pages/traits/physiology/er_phagy.html
    sha256: 1b122e3f4471f57758ca0695bf4dd417ce08ff483f6b071868fa8973cd75821b
    role: context
  - path: pages/traits/physiology/exocytosis.html
    sha256: 1d01fcde90e6ed9e9585c6dc866a270cacba679e45812cda75ca5c96f8e27a54
    role: context
  - path: pages/traits/physiology/extracellular_membrane_vesicle_production.html
    sha256: 64c415d843187d12b9d6390e92ebe013643b905c3c5c086eec5b6fc513d21c32
    role: context
  - path: pages/traits/physiology/extracellular_trail_based_spatial_memory.html
    sha256: e737dbf678423fee369b0a5a2a13935f1cac132c417f2af48f9b4865c53b02f7
    role: context
  - path: pages/traits/physiology/galvanotaxis.html
    sha256: 75f1e7ebd5451c2d4099c96a0d7daac15e98d3c7f5e88a0619cb2eec59791fcf
    role: context
  - path: pages/traits/physiology/galvanotropism.html
    sha256: e647442c5c72b48565bbcec5ff16ae4fda551fcd6ee2ce28025d6a476f98651e
    role: context
  - path: pages/traits/physiology/gamma_glutamyltransferase_activity.html
    sha256: 977bfefc2ec2ba576f7a95963e61b8771f8da98c6ed8d486288a9e9e32d81cba
    role: context
  - path: pages/traits/physiology/gelatinase_activity.html
    sha256: d65d62c2e77a39dfac7ae3b67d42da9db23457fd776fa3d85d2f55179db7f194
    role: context
  - path: pages/traits/physiology/glutamyl_glutamic_acid_arylamidase_activity.html
    sha256: b4bfd503a37004b41e71248e5353ca1ae66340022660b1dae6cc09fc6eeb6562
    role: context
  - path: pages/traits/physiology/glycine_arylamidase_activity.html
    sha256: 675aad7828f2048f1c429ecadb620fac9ebedc7828135f103e3a415cdfe0b532
    role: context
  - path: pages/traits/physiology/gravikinesis.html
    sha256: 0b330db89597c83a587e521da919880d5d51971c5772599f7b9049f8fea439fe
    role: context
  - path: pages/traits/physiology/gravitaxis.html
    sha256: 3c7d78a13616aa356c93e754f1c5ca72e4a7427dd57c8c84d8a3d6a02fcf04ad
    role: context
  - path: pages/traits/physiology/gravitropism.html
    sha256: fc12cf354be26f95558e9626515e40bc02b39bab2889f0a0f9e84c41127944bb
    role: context
  - path: pages/traits/physiology/gyrotaxis.html
    sha256: 13b0158217eea63e911fb44e00680fbc56587d9f6ffe17f278bdf4fa8bd6d531
    role: context
  - path: pages/traits/physiology/haptocyst_discharge.html
    sha256: 1916d331ef34b9776fc391bc1114ee37640a931e387091d665ed928ac675c4c8
    role: context
  - path: pages/traits/physiology/heat_shock_response.html
    sha256: 384ad2c36caa0cd80cb70978a6938be02f1fdadceb953e3317611f24a8d26870
    role: context
  - path: pages/traits/physiology/heterokaryon_incompatibility.html
    sha256: ce16971c774252707369154767fda5e911c09ebcc36a5561dcbcc1338cc46297
    role: context
  - path: pages/traits/physiology/heterothallism.html
    sha256: 341a87ee4817607562291cf0ff33a83782c538b464dacbc9fffc1bc262af814e
    role: context
  - path: pages/traits/physiology/heterotrophic.html
    sha256: 3d5e73ff6d8cad6f6ea54cc690103410eb41d2b64926b9d87bde5738cd03a6f7
    role: context
  - path: pages/traits/physiology/histidine_arylamidase_activity.html
    sha256: bf8806b36558cd9ebdc8693002af18d04bb37d1c6b56291aa531b86b7e11a5be
    role: context
  - path: pages/traits/physiology/homeoviscous_adaptation.html
    sha256: 57ce08dda105190c95402c2c9303c6afc36453eab080fe3eed012b6a3475c866
    role: context
  - path: pages/traits/physiology/homothallism.html
    sha256: 22e7945233f2cd841875691cc9e9059b5d5f3d6b851f544bb27dc2997191d11c
    role: context
  - path: pages/traits/physiology/hydrogenotrophic.html
    sha256: 1a7dc84ab2f7f9e107eaa670932e91c8f5247e1dce6f10241c85510a983e3cfd
    role: context
  - path: pages/traits/physiology/hyphal_anastomosis.html
    sha256: c5ba89a24e99534aca01e501a0ee787064904cfac9d466b4825079e3c4bf4f0f
    role: context
  - path: pages/traits/physiology/isogamy.html
    sha256: 4ac93fafacfd8b8ee8a42ce2c01c29fc6cbad8c17742b9f388e444e63c3b27a9
    role: context
  - path: pages/traits/physiology/karyoklepty.html
    sha256: 55e68141e730ff355fdd455b28d76be97644b5098e2e2af2ce519433587f738f
    role: context
  - path: pages/traits/physiology/kinetocyst_discharge.html
    sha256: e731abfbc421a72e53c5956bb35980e0ff30512cd1b08c12a446bc3f5c383886
    role: context
  - path: pages/traits/physiology/kleptoplasty.html
    sha256: 2184722f6c27bcd7b07615223e27fee0ae3282c37f0e61fece3b4c665c9be243
    role: context
  - path: pages/traits/physiology/lecithinase_activity.html
    sha256: 10d2d0215cdb77a97f60b44efe7f2d3bdc4dfcc363b6f548b785f53f03b7db5f
    role: context
  - path: pages/traits/physiology/lethal_algicidal_activity.html
    sha256: 16c437fee443b4f950324350e7bced20b8e3804cb0e739f8d181f8d928a0502c
    role: context
  - path: pages/traits/physiology/lethal_nematicidal_activity.html
    sha256: c7e2adee319073d17da1fdfae43765f90d1e94de5fd3699514187e6a109baa01
    role: context
  - path: pages/traits/physiology/leucine_arylamidase_activity.html
    sha256: dbfb36de7bc0691ed8852c3a96147bbc142971d8be987f5089cb8e277491a884
    role: context
  - path: pages/traits/physiology/leucyl_glycine_arylamidase_activity.html
    sha256: bce91079e07d554fdbca3e64ecae465bc1cff2ec28909aad1e41a5d02c2114c8
    role: context
  - path: pages/traits/physiology/lipase_activity.html
    sha256: c93c9d530d8d8bebe3af0cc405f55d469dcd26316d60ae8541ead14e189c283e
    role: context
  - path: pages/traits/physiology/lipophagy.html
    sha256: 0931048d78fd08e9792cbf26b8e332386043b444e53e36fec634e84b9c1cb7df
    role: context
  - path: pages/traits/physiology/lithoautotrophic.html
    sha256: 214c2dc6e17812595a5126fb0b7c8aec8d79dd8771e5871ae501ff76249cd785
    role: context
  - path: pages/traits/physiology/lithoheterotrophic.html
    sha256: 1e60c9a07e0e80faf9f47a4c06af2d687d2ec982b1d092762c4245b4c1f8f1b3
    role: context
  - path: pages/traits/physiology/lithotrophic.html
    sha256: df3796ab327903cb79bbbe9ac3b1653adba4af0d9585bfd76a6fd184f5c80ebe
    role: context
  - path: pages/traits/physiology/lysine_decarboxylase_activity.html
    sha256: 2c29cffa91877376a72a52f9633bccd0228a5c9653a571f718adf8e54c2f74a3
    role: context
  - path: pages/traits/physiology/macropinocytosis.html
    sha256: 5cde806b5fe7ec665bc00e64e0a824816f3d9f5de6558aa889b4c4878c3f6216
    role: context
  - path: pages/traits/physiology/magnetotaxis.html
    sha256: 1c53deccd5be0841c9f6a51e11ac3eda2dc3c0a98034fcde7abe540ff4ce2e7f
    role: context
  - path: pages/traits/physiology/mating_type_switching.html
    sha256: df75dc7ce1d70393e768618f0365f3e05668bbecfc88c652b5cf25d6c369a631
    role: context
  - path: pages/traits/physiology/methanotrophic.html
    sha256: 1d10f7dee7e15b93a34f34594ccfe51e3570ede181d7756a83276fe5bad5cd6b
    role: context
  - path: pages/traits/physiology/methylotrophic.html
    sha256: 3dfa5a367d254d2d60cb138ae88f84638e860b4f0ff97b08cdb2343cf6aaefa3
    role: context
  - path: pages/traits/physiology/mitophagy.html
    sha256: 009d5373d48bc467af676ae10743b74782313f312701945659c5eebe4bc07f62
    role: context
  - path: pages/traits/physiology/mixotrophic.html
    sha256: 50536803c93a9805f24427aa2031a0770d73e5c70875fc3ea4c001ab5c7b6ae0
    role: context
  - path: pages/traits/physiology/mucocyst_discharge.html
    sha256: 7dc8635b7dbba9f3728b13f59bdbde8db76b45075377ea4b42a42f6f5ba1d08b
    role: context
  - path: pages/traits/physiology/myzocytosis.html
    sha256: cfb529eaac41a7027c7f99b936fc04a5729955e76153a87e06a243022ab46035
    role: context
  - path: pages/traits/physiology/nad_dependent_alcohol_dehydrogenase_activity.html
    sha256: 8bc5a917751082db64fe2881d38e060b34e9b5b2f8b11f4f921f93cca2fe435a
    role: context
  - path: pages/traits/physiology/naphthol_as_bi_phosphohydrolase_activity.html
    sha256: ba9393c362923c553699438b5f1c111df0866f9d6925904a67f100f060d9beb0
    role: context
  - path: pages/traits/physiology/natural_competence.html
    sha256: 017edb6891d9115217f3246958940540a7394e1798bc33553df2376f18bde2b0
    role: context
  - path: pages/traits/physiology/negative_autotropism.html
    sha256: e4d4dd87625c6b36c6b06cb97a438aa4d986594ebe04b4f8612a63b069d1ed4b
    role: context
  - path: pages/traits/physiology/nematode_attracting_activity.html
    sha256: 25e0dabfca7cc6678377b978d6107cb5b3ea05764a8e48c811128fa813b520bc
    role: context
  - path: pages/traits/physiology/nematode_egg_hatching_inhibitory_activity.html
    sha256: 3a973c71a44352aaf216408304fffa94ddabdc66f7f1ef134c782653394a417a
    role: context
  - path: pages/traits/physiology/nucleophagy.html
    sha256: b82c304f9cf9ef6d9bac3bb7e4f47be7f6415f52db8228288867e4f4f407513e
    role: context
  - path: pages/traits/physiology/nutrient_adaptation.html
    sha256: 5636dc241a8dea056f5283bf92325d9b46f641654c47161a6e6e22575cf0b3f5
    role: context
  - path: pages/traits/physiology/oligotrophic.html
    sha256: d6a66e2e07b54df888d47c4fd4199b19c42043dff0447e76965a1f9e522490ab
    role: context
  - path: pages/traits/physiology/oogamy.html
    sha256: bc9296222a68cce849504c11829a04c6429a1812d350c39da0e07febdc0f3a38
    role: context
  - path: pages/traits/physiology/organoheterotrophic.html
    sha256: 3740f9f329ea4812cdb157d939da16becb2a535fbe09288e282ae88618bb969d
    role: context
  - path: pages/traits/physiology/organotrophic.html
    sha256: cd71e170530238ad3b239bf9442a9c014607f83e8c67d514924c23c3fe743189
    role: context
  - path: pages/traits/physiology/ornithine_decarboxylase_activity.html
    sha256: 8ce227afef88a580e34c42ede0203d9f3e03df19e6cc339c2225b5c9d417dc08
    role: context
  - path: pages/traits/physiology/osmotaxis.html
    sha256: bb8b3a40120c5a288f924a4026ba89cf814a55d484f917fa41c2d1250fe81e73
    role: context
  - path: pages/traits/physiology/oxidase_activity.html
    sha256: 0d1bd5c9221fed9c51d0a9e119e97906e0ca5ed645908ca8f5b5a95f306301f3
    role: context
  - path: pages/traits/physiology/oxidative_stress_response.html
    sha256: e4f6ebf74f707aa6bfbb367da1e76749e081473ad36a901dc7aac1ded383f6dc
    role: context
  - path: pages/traits/physiology/paedogamy.html
    sha256: 997edb281ac56bbe10bb629b42ca1ddceb381f49d8012ccddf78b824041a5722
    role: context
  - path: pages/traits/physiology/pallium_feeding.html
    sha256: 8c333f7a584746b43989596e9b9f681b7a0a74b0e2c4e46996644968924b1747
    role: context
  - path: pages/traits/physiology/parasexuality.html
    sha256: 0be838adcc1d77022987ac62a7c352696423c578dd8c994ddfe549d38604e966
    role: context
  - path: pages/traits/physiology/persister_cell_formation.html
    sha256: aa58d2cf975a82180d7b5c6af0dc0b59c782e981601b628b4ec60e7690b95914
    role: context
  - path: pages/traits/physiology/pexophagy.html
    sha256: 0b12627ad4941babc73780ab0fc95c95cc0d319da09293bf707ea2cf9fa46b5f
    role: context
  - path: pages/traits/physiology/ph_taxis.html
    sha256: d556fdb09a93075cd3eaf23e986a86e52a757bc2540ab3efedc8f2f217dd91ba
    role: context
  - path: pages/traits/physiology/ph_tropism.html
    sha256: 45e7dbd72ea029b27a62351b988b61cbb7e28c3027126e178f7ab4953f61dca9
    role: context
  - path: pages/traits/physiology/phagocytosis.html
    sha256: 5c26204e76d6f7f01f6628aeb2acf8d2a0edf23fcfe165a884051417c564141d
    role: context
  - path: pages/traits/physiology/phagotrophy.html
    sha256: f0d04177c94b32637e11bcc00c491f3ed0217f6d966ae6d4de37226d35a66efd
    role: context
  - path: pages/traits/physiology/phenylalanine_arylamidase_activity.html
    sha256: 7bdca7a53066a4973944d92aac3e05204c75e9ffc434ffcca291064334ea00ff
    role: context
  - path: pages/traits/physiology/photoautotrophic.html
    sha256: d599b6c8483e08d553d128aaa68ef43039a8b0b68c93d55e710346c54f9b70e6
    role: context
  - path: pages/traits/physiology/photoheterotrophic.html
    sha256: 582338368610e406417d13a3cf9322029f12f9922ca3a2cbb5203fd23902c1dc
    role: context
  - path: pages/traits/physiology/photokinesis.html
    sha256: 261dc885c1402c8c4fac0a3cd1adb8ff5b392119334e5b450138029882ece2bb
    role: context
  - path: pages/traits/physiology/photolithoautotrophic.html
    sha256: a78049bb7f4f3162d84744c274c85c628ab3428072c58f40f5dcb66737636611
    role: context
  - path: pages/traits/physiology/photolithotrophic.html
    sha256: d37082b0e072abac458acdbebc06716ef29c8ce0d56ae9a571c837c191991579
    role: context
  - path: pages/traits/physiology/photoorganoheterotrophic.html
    sha256: 91c51c82ad68bb64e6769564955e0462646d6f943d94d2bc6d391028cb10eba3
    role: context
  - path: pages/traits/physiology/phototaxis.html
    sha256: 85b59e1fefb4756477a09fbc6d8b0099af3ddd10e6c47404b9fc7ccae405bba0
    role: context
  - path: pages/traits/physiology/phototrophic.html
    sha256: 610793f2533a9a272f556b5a07f7c921ba53f3fd21df966b36c52c753e6223d3
    role: context
  - path: pages/traits/physiology/phototropism.html
    sha256: 60b44647ab240a209ecd31efc5cc6ea80a9e03ae6858fd874e04fb0b70d716a2
    role: context
  - path: pages/traits/physiology/pinocytosis.html
    sha256: b7858c02acece79c5ea4a8c1fab3917e416f6a303567c49cd349966d69105ac0
    role: context
  - path: pages/traits/physiology/positive_autotropism.html
    sha256: d38e5a90d8a1c55ce28cd4327d5bc4b5c6d6633218446106e3bab2f4c07875a7
    role: context
  - path: pages/traits/physiology/primary_homothallism.html
    sha256: 1b937194418b8bc129c5d622ddc00d7301ac3b9fa682990126a6f2f7440deaeb
    role: context
  - path: pages/traits/physiology/prolyl_aminopeptidase_activity.html
    sha256: 10761d8a958725748ecebb02da4518df69ab77a404935431f2e8ae37412da830
    role: context
  - path: pages/traits/physiology/proteaphagy.html
    sha256: f15c13f157bed6cb613fa8ac6538935c903581c1b73e877ec7c9710c4606b05f
    role: context
  - path: pages/traits/physiology/pseudobipolar_mating_system.html
    sha256: b2d9a406e2c963c2da120264ea3a1fa2646ef9bf7bb86f6a9ce58fbb80f4d61f
    role: context
  - path: pages/traits/physiology/pseudohomothallism.html
    sha256: f876aabddb87778050ed8934546f8e2f7e8cf0280273e897d4505db98fa905b6
    role: context
  - path: pages/traits/physiology/pyrazinamidase_activity.html
    sha256: c691beeb6898adcf76b79ee13c1d41e1709d25d364258c7e8c87902ab2643e53
    role: context
  - path: pages/traits/physiology/pyrrolidonyl_arylamidase_activity.html
    sha256: 6b8d634bf3804685a79d582bbbfc8ec640c9f7e7e030a2954cbd4fa69d3801fa
    role: context
  - path: pages/traits/physiology/quorum_quenching.html
    sha256: 19933d553ab3f7ae84c99d7fc23fd3dc90fe31784023f609c4caf8a2f34db782
    role: context
  - path: pages/traits/physiology/quorum_sensing.html
    sha256: 1ba38579198273b77562d088ab1a15f418491723a773c2bcb274bf19cc42772e
    role: context
  - path: pages/traits/physiology/rapid_axopodial_contraction.html
    sha256: 875d9b3c6837769663292ff86b25331a58c1bae69ebdefc57ba4361117b8f161
    role: context
  - path: pages/traits/physiology/replicative_aging.html
    sha256: 2e5cd92af562fe1b451a88bfd356cb5331fc4f40bea6da6207240d8490833767
    role: context
  - path: pages/traits/physiology/reversible_nematode_paralyzing_activity.html
    sha256: b3c2a8d17196b386e7014cbd5563ec5d96faf2b47173613ae9d404900015500b
    role: context
  - path: pages/traits/physiology/rheotaxis.html
    sha256: 3ee5a0069e8f99081385c80d4c6e401cb906442445bf8db846b528b022d92c50
    role: context
  - path: pages/traits/physiology/rheotropism.html
    sha256: 4a75e2ece30da1c83b48e15006582a458cf5509a84d0cc65e1636776d6be22bf
    role: context
  - path: pages/traits/physiology/ribophagy.html
    sha256: cc0aa3fbec300e827bea8c93130346f8959bb1d97ec85dd3ee6d5ba531c7cf5c
    role: context
  - path: pages/traits/physiology/serine_arylamidase_activity.html
    sha256: ae23a3d600168870081ab07ddb7ab71425b6d5207fcb49bbcf1d5d91e907ade0
    role: context
  - path: pages/traits/physiology/siderophore_production.html
    sha256: 14485e484fd2592816582ab775598225d0a25fe577fee63c52ac694d6ccc1113
    role: context
  - path: pages/traits/physiology/siliceous_scale_production.html
    sha256: 6125f9ae8c4a9e2cfc6ea3e65a9a2df59655288264c249a5d6beddf1017b9559
    role: context
  - path: pages/traits/physiology/sos_response.html
    sha256: cf358e06045705c86002ee6d9e09d74023332475dbe78807a51409d8dc910b1f
    role: context
  - path: pages/traits/physiology/spore_germination.html
    sha256: e3b28d9d6df24b470ffa8bf6211fa0e8b7f734a6c6c14d184a6767270dd2a4d0
    role: context
  - path: pages/traits/physiology/stress_response.html
    sha256: e4b4a2f5148e3cde8a0a3f3f03cf970709165a5efe5c8742236761787e8eefad
    role: context
  - path: pages/traits/physiology/tetrapolar_mating_system.html
    sha256: 72cfe71566cd0c1e6666acc412611bfd55752f1be82bf42c8973f4a4cb51ac9d
    role: context
  - path: pages/traits/physiology/thermotaxis.html
    sha256: 903ccc61639b88b6337754facfbdf90a7d792d53fd11b7c7dea3c7abb116c4e9
    role: context
  - path: pages/traits/physiology/thigmotropism.html
    sha256: 6e1ebe049488b5afc5c26be02fc7b388bc081bda2415d425ce1097a53d106012
    role: context
  - path: pages/traits/physiology/toxicyst_discharge.html
    sha256: b459208c54f19447705de0053fe86f8ec631ccaff71ffecfa9858f5afa5bf85a
    role: context
  - path: pages/traits/physiology/trichocyst_discharge.html
    sha256: fc674247206bc66d70305f361c552c04193de3dee6e6fecfa5459a79f23fa845
    role: context
  - path: pages/traits/physiology/tripolar_mating_system.html
    sha256: df474d78566c6787a30f9c4a3daefda6bdf56d5d2da47c48f204fd6c911a9438
    role: context
  - path: pages/traits/physiology/trogocytosis.html
    sha256: d483c0cf05c6c90333f5e85cd89bbca11b5ff11474edadf45a000100858ae549
    role: context
  - path: pages/traits/physiology/trophic_type.html
    sha256: 79c57d54741f042817b6a596d35b75b263afaaf68df362d52fc6f8a7d9357ee2
    role: context
  - path: pages/traits/physiology/trypsin_activity.html
    sha256: 9e79288ad37fbad200b6685cfc0948dee3cda817c4ecd210a8d89d39a4e6d3a7
    role: context
  - path: pages/traits/physiology/tyrosine_arylamidase_activity.html
    sha256: 4f2d0fc100117d0c43e75884a5fa3acf6942d9032e3902bd6e0c785af144dab6
    role: context
  - path: pages/traits/physiology/unconventional_protein_secretion.html
    sha256: abb646d96c41a6340cdef69eb79d756f46b7552893dcecf0a75126b379527618
    role: context
  - path: pages/traits/physiology/unequal_protein_aggregate_inheritance.html
    sha256: 26a669de1e8e1d14ec250684e5df90284b6a944c5023aaca11420b8ef6bc2d5a
    role: context
  - path: pages/traits/physiology/unisexual_reproduction.html
    sha256: fbd5161d1560e148184111197d41718dbceb7400676a7c8c1d2377b5d89383f8
    role: context
  - path: pages/traits/physiology/urease_activity.html
    sha256: 3eb9c6cda45210e495f563e694de550abc79142208c28dcac68cd901ea0aa1c0
    role: context
  - path: pages/traits/physiology/valine_arylamidase_activity.html
    sha256: 3adb1d3b0938b8aac81d1c191420520738aa273d6f2f5ae4dcb56b1d2199d62b
    role: context
  - path: pages/traits/physiology/viable_but_nonculturable_state.html
    sha256: 7b9c788ab6dd87ccd735fb6cf629d9b42ec416367664383864e131d8d58f9461
    role: context
  - path: pages/traits/physiology/viscotaxis.html
    sha256: f73ae9e2cab199de5bc9f7af1cd193e52705f0bb89b8ae1d659d837f621ed05d
    role: context
  - path: pages/traits/quantitative_property/has_maximum_observed_value.html
    sha256: 0441ff6c2409fc0d3be20f3503bbf722a8a831496a34ef3cdba5817ffef2e261
    role: context
  - path: pages/traits/quantitative_property/has_minimum_observed_value.html
    sha256: 72e5671147b93703d9c9d5cd0a043c835a217254bf08db59f8da032202d5794a
    role: context
  - path: pages/traits/quantitative_property/has_observed_spot_value.html
    sha256: 7ae539abfc40a56e2492e864b60fc816a5f2b970aec5c3f209225d9514ab5710
    role: context
  - path: pages/traits/quantitative_property/has_value.html
    sha256: bdea063b1c43dd7e3326639d2bb9d789c5d66d76b24c54497ddab0d1f0a03404
    role: context
  - path: pages/traits/quantitative_property/has_value_comments.html
    sha256: 4298296eb09800ff9f83ecca8ec06bf39b8d335b9ece61a6becb5e35a2189301
    role: context
  - path: pages/traits/quantitative_property/is_negative_data.html
    sha256: 4170dca6c2f3fb6ee063de38d979c0f841c4a8e0e34a927d40f51978737cdfd0
    role: context
  - path: pages/traits/quantitative_property/observation_data_property.html
    sha256: 577535759acfd4c82d05e32710dc7177dd31e4b4b773d60294f419e1f837393d
    role: context
  - path: pages/traits/upper/biological_process.html
    sha256: 808e00e9322d8fca8dd397d250a5f0a7d54d371a67127708a02b18472e4b3b8b
    role: context
  - path: pages/traits/upper/chemical_entity.html
    sha256: 4b0a6b63efdf8c8335bbe8e94f2ae991fda9483cb9644289cfaa7f33b384f924
    role: context
  - path: pages/traits/upper/enzyme.html
    sha256: 198ade4e19a2c5cc8feb3a50bfb64e8a7e6bb6a8c236221118e4c3602253c27b
    role: context
  - path: pages/traits/upper/material_entity.html
    sha256: 39e2a52204ba9cbd363658d9ab127ac85f84e4ae453a94474b7f6426fe736a85
    role: context
  - path: pages/traits/upper/microbe.html
    sha256: c6fcda7d7e250d007ea3e061bb35ba77db85f0411fe2bb82467362ffbe48f9fa
    role: context
  - path: pages/traits/upper/observation.html
    sha256: 265ae596b077d6a7ef7bdbd0d1f3394633b6a717ad78137e9f81897dc277d65b
    role: context
  - path: pages/traits/upper/phenotype.html
    sha256: 767202b02cb2f14ee51c798b4536358b97fc7dc6d5a4ed4c0873024c9d9740e5
    role: context
  - path: pages/traits/upper/quality.html
    sha256: 2eddb28ea08a6664454e812f0df1f201a31ab82e5fcb2ea027a3cce05879ae2f
    role: context
  - path: pages/umap.html
    sha256: 70f4e101cc7795efbeca46ab957ca64a3d27de51c75aa06fc059f6e0aea9149a
    role: context
  - path: proposals/metpo_traitmech_v599/metpo_proposal_classes_robot.tsv
    sha256: e68c81d775941891d8c16f895c9ca5798e3daa5128ce13071a98725161768027
    role: context
  - path: proposals/metpo_traitmech_v599/proposal.md
    sha256: fe537b4ed4a242adae69cf9c0e156e6e8e188733f1c9df3a49b5b3433f9a019d
    role: context
  - path: reports/proposal_citation_audit.tsv
    sha256: 6236d2ad13638e1519155f561684b0224f3b36354b9a215d0f00b47d2d9e9504
    role: context
  - path: reports/robot/metpo_traitmech_v599/classes.owl
    sha256: 59b0ef41082cc65b570b605b7198df0083fbf0d6b653fd09bbef82732c856797
    role: context
  - path: reports/robot/metpo_traitmech_v599/merged.owl
    sha256: 1899b0c05a8802aa899d359d6656ee0c379b658396359868a4152bcf756ba4f1
    role: context
  - path: reports/robot/metpo_traitmech_v599/reasoned.owl
    sha256: 987d5fed22ee0c93a81ab9df0bd87c5b98200ff81e5a231f6a3471e155732cc8
    role: context
  - path: research/traits/physiology/nematode_egg_hatching_inhibitory_activity-source-verification.json
    sha256: 7cf05642ba3d01c985cf524cd9c027ece482fc1c5934bcdcf832c678242b6993
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/add_nematode_egg_hatching_inhibitory_activity_trait.py
    sha256: cbd66286213231e7da3ad2b5bc8605f24a6552231c375718c77b0728c4bd333f
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
  - path: tests/test_add_nematode_egg_hatching_inhibitory_activity_trait.py
    sha256: f6f8c0c9baff9314fda4bb169f70e59744de382691d609e0e09bcb23c84e42bf
    role: context
targets:
- target_id: traitmech:000723
  path: data/traits/physiology/nematode_egg_hatching_inhibitory_activity.yaml
  label: nematode egg-hatching inhibitory activity
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/physiology/nematode_egg_hatching_inhibitory_activity.yaml
    role: maintained record
  - repository: CultureBotAI/TraitMech
    path: scripts/add_nematode_egg_hatching_inhibitory_activity_trait.py
    role: guarded curation writer
scope:
  description: One complete new record and its maintained/generated owners, not whole-corpus
    scientific review.
  selection: One exact new trait, without sampling.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - traitmech:000723
  exclusions:
  - target: Other 1117 TraitRecords
    reason: Novelty context, deterministic diagnostics and byte preservation only.
  - target: data/traits/physiology/spore_germination.yaml
    reason: Protected and byte-preserved.
checks:
- check_id: records-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate
    -s src/traitmech/schema/traitmech.yaml --target-class TraitRecord data/traits/physiology/nematode_egg_hatching_inhibitory_activity.yaml
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate
    -s src/traitmech/schema/traitmech.yaml --target-class TraitRecord data/traits/physiology/nematode_egg_hatching_inhibitory_activity.yaml
  status: passed
  required: true
  target_ids:
  - traitmech:000723
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; corpus diagnostics are not whole-corpus
    scientific review.
- check_id: records-1
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_strict.py data/traits/physiology/nematode_egg_hatching_inhibitory_activity.yaml
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_strict.py data/traits/physiology/nematode_egg_hatching_inhibitory_activity.yaml
  status: passed
  required: true
  target_ids:
  - traitmech:000723
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; corpus diagnostics are not whole-corpus
    scientific review.
- check_id: records-2
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_history_links.py history/records/nematode_egg_hatching_inhibitory_activity
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_history_links.py history/records/nematode_egg_hatching_inhibitory_activity
  status: passed
  required: true
  target_ids:
  - traitmech:000723
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; corpus diagnostics are not whole-corpus
    scientific review.
- check_id: records-3
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/verify_snippets.py --record data/traits/physiology/nematode_egg_hatching_inhibitory_activity.yaml
    --out /tmp/traitmech-egg-hatching-checks-20261014/native-record.tsv
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/verify_snippets.py --record data/traits/physiology/nematode_egg_hatching_inhibitory_activity.yaml
    --out /tmp/traitmech-egg-hatching-checks-20261014/native-record.tsv
  status: passed
  required: true
  target_ids:
  - traitmech:000723
  exit_code: 0
  expected_exit_code: 0
  summary: 'Native snippet command exited zero with two rows: UNRESOLVED and NOT_IN_ABSTRACT.
    Neither is native VERIFIED. Direct source inspection is separately recorded.'
- check_id: records-4
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q tests/test_add_nematode_egg_hatching_inhibitory_activity_trait.py
    -k 'not source_receipt'
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q tests/test_add_nematode_egg_hatching_inhibitory_activity_trait.py
    -k 'not source_receipt'
  status: passed
  required: true
  target_ids:
  - traitmech:000723
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; corpus diagnostics are not whole-corpus
    scientific review.
- check_id: focused-after-readme-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q tests/test_add_nematode_egg_hatching_inhibitory_activity_trait.py
    tests/test_readme_artifacts.py tests/test_trait_priority.py tests/test_qc_dashboard_artifacts.py
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q tests/test_add_nematode_egg_hatching_inhibitory_activity_trait.py
    tests/test_readme_artifacts.py tests/test_trait_priority.py tests/test_qc_dashboard_artifacts.py
  status: passed
  required: true
  target_ids:
  - traitmech:000723
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; corpus diagnostics are not whole-corpus
    scientific review.
- check_id: focused-after-readme-1
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/ruff
    check src scripts tests
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/ruff
    check src scripts tests
  status: passed
  required: true
  target_ids:
  - traitmech:000723
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
  - traitmech:000723
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
  - traitmech:000723
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
  - traitmech:000723
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
  - traitmech:000723
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
  - traitmech:000723
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
  - traitmech:000723
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
  - traitmech:000723
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
  - traitmech:000723
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
  - traitmech:000723
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
  - traitmech:000723
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
  - traitmech:000723
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
  - traitmech:000723
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
  - traitmech:000723
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
  - traitmech:000723
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
  - traitmech:000723
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; corpus diagnostics are not whole-corpus
    scientific review.
- check_id: verify-3
  name: just verify-proposal metpo_traitmech_v599
  command: just verify-proposal metpo_traitmech_v599
  status: passed
  required: true
  target_ids:
  - traitmech:000723
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; corpus diagnostics are not whole-corpus
    scientific review.
- check_id: verify-4
  name: just robot-validate-proposal metpo_traitmech_v599
  command: just robot-validate-proposal metpo_traitmech_v599
  status: passed
  required: true
  target_ids:
  - traitmech:000723
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
  - traitmech:000723
  exit_code: 0
  expected_exit_code: 0
  summary: Canonical shape check used --no-resolve, not live taxonomy verification.
    This record has no canonical examples.
- check_id: verify-6
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/run_trait_graph_audit.py --verify
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/run_trait_graph_audit.py --verify
  status: passed
  required: true
  target_ids:
  - traitmech:000723
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; corpus diagnostics are not whole-corpus
    scientific review.
- check_id: verify-7
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/audit_history_records.py --base 4200c75a930654cfec7e635edcbcec896efef919
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/audit_history_records.py --base 4200c75a930654cfec7e635edcbcec896efef919
  status: passed
  required: true
  target_ids:
  - traitmech:000723
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed; corpus diagnostics are not whole-corpus
    scientific review.
- check_id: tests-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q --junitxml=/tmp/traitmech-egg-hatching-checks-20261014/pytest.xml
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q --junitxml=/tmp/traitmech-egg-hatching-checks-20261014/pytest.xml
  status: passed
  required: true
  target_ids:
  - traitmech:000723
  exit_code: 0
  expected_exit_code: 0
  summary: 4607 tests passed without failures, errors or skips.
- check_id: products
  name: products
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    /tmp/traitmech-egg-hatching-products-20261014.py
  status: passed
  required: true
  target_ids:
  - traitmech:000723
  exit_code: 0
  expected_exit_code: 0
  summary: All 1117 prior records, protected spore germination, prior history/reviews/proposals/embeddings/templates/baseline
    are byte-preserved. Old pages differ only in footer counts except the phenotype
    child link. Exact w3id RDF hierarchy and definition citations pass.
- check_id: browser
  name: browser
  command: node /tmp/traitmech-egg-hatching-browser-20261014.cjs
  status: passed
  required: true
  target_ids:
  - traitmech:000723
  exit_code: 0
  expected_exit_code: 0
  summary: '1440/390 px tests pass: two quotes, two discussions, one history, local
    identifier, parent/browse navigation, dashboard count 1118 and loaded coverage
    image. Eight screenshots visually inspected; no horizontal overflow or page errors.'
evidence:
- evidence_id: source-0
  kind: primary_source
  reference: DOI:10.1163/156854104323072883
  locator: Results, printed page 28/PDF page 6, lower left column. All ten article
    pages, Methods, Results, Table 1 and Figure 1 inspected. Quoted page re-inspected
    during curation. No full raw-data reanalysis or canonical taxonomy verification.
  accessed_at: '2026-10-14T03:45:53Z'
  support: supports
  snapshot_sha256: 277daa845dd300ba8b26d6a92e0b95cfcbcc7cbfe7e54ee30c721b49cfc8813d
  summary: Results and Table 1 support reduced SCN/RKN hatch in fungal filtrates.
    Fourteen-day counts include motile and immotile juveniles; initial egg count and
    matched uninoculated PDB denominators are distinct. Seven days is culture age.
    Host assays use different filtrate concentrations. Only 40 of 253 isolates were
    retested. Hatch inhibition does not establish egg death, recovery or a molecule;
    unneutralized pH remains a condition. The separate USDA/paper motility-count discrepancy
    is retained.
- evidence_id: source-1
  kind: primary_source
  reference: DOI:10.1038/s41598-023-33669-z
  locator: Results, egg-hatching paragraph; not a named egg-assay Results subsection.
    Original publisher HTML scientific Abstract, own hatch Results, culture-filtrate
    and hatch Methods, actual Figure 3 inspected. Prior qualified supplement/GenBank
    checks were reread; no full DOCX page render or complete field/raw-data audit.
  accessed_at: '2026-10-14T03:45:53Z'
  support: supports
  snapshot_sha256: 9cd48922e85bd719a9108435fd1c4914f76e2a28bce35ea9ca005bb902243bc1
  summary: The quoted Results describe the study own hatch experiment, not its background
    Meyer summary. Five egg masses, 20/40/60/80% spore-checked filtrates, water/PDB
    controls and alternate-day counts through ten days support the endpoint. Results
    maximum at 120 h conflicts with Figure 3 time labels, so no exact maximum/time
    pair is adopted. Egg deformation and juvenile recovery do not establish egg death
    or recovery. GenBank/supplement strain inconsistencies preclude a canonical taxon.
- evidence_id: content
  kind: record_content
  reference: data/traits/physiology/nematode_egg_hatching_inhibitory_activity.yaml
  locator: Whole record, guarded writer, tests, proposal, sidecar, history and generated
    diff.
  accessed_at: '2026-10-14T03:45:53Z'
  support: supports
  summary: One microbial capability reducing nematode egg hatching over a defined
    observation interval versus comparable unexposed controls. The microorganism is
    the bearer. It is not a susceptibility trait, an assay, a chemical role or a sequence
    feature. No egg death, irreversible arrest, recovery, canonical examples, exact
    synonyms/xrefs, proteins or graph are inferred.
- evidence_id: ontology
  kind: database
  reference: data/raw/metpo.owl
  locator: Three OWL inputs, six upstream TSV owners and current neighboring records.
  accessed_at: '2026-10-14T03:45:53Z'
  support: supports
  summary: Phenotype METPO:1000059 below quality METPO:1000188 is a conservative broader
    parent. Infection, feeding, killing, trapping, attraction and paralysis are not
    required. The only egg lexical lead in active/deprecated/draft annotations was
    fried-egg-shaped colony, not an equivalent. The editor input has 31 metadata triples
    and is not an import closure. Pinned OWL is unchanged.
- evidence_id: novelty
  kind: search
  reference: research/traits/physiology/nematode_egg_hatching_inhibitory_activity-source-verification.json
  locator: Known ignored/hidden current copies, retained regular-file history, changed
    pending blobs and selected upstream owners.
  accessed_at: '2026-10-14T03:45:53Z'
  support: supports
  summary: 182 known locations, 178 available, 139 retained heads, 11 open/draft PRs,
    783 pending nonremoved blobs and 587 selected upstream owners were screened. All
    76 matched paths were adjudicated. Existing hatch mentions are exclusions or literature
    context, not exact synonyms/nodes/parent gaps. CommunityMech TYQ1 is a consortium,
    not this microbial trait. Sequence categories remain leads. Zero exact allocation
    hits and 665 broad editor-envelope intervals did not establish conflict.
  search_scope: Available ignored/hidden files included. No lost historical ignored/untracked
    reconstruction, symlink targets or arbitrary local archive decoding. Pending content
    scope is changed blobs, not entire PR trees. Not atomic allocation.
- evidence_id: provenance
  kind: authority
  reference: research/traits/physiology/nematode_egg_hatching_inhibitory_activity-source-verification.json
  locator: Primary source bytes, typeset/HTML excerpts, native report, metadata and
    notice-check receipts.
  accessed_at: '2026-10-14T03:45:53Z'
  support: supports
  summary: Meyer supplies definition authority; Saharan supplies an independent primary
    hatch assay, not an automatic definition citation. The 22/13-word quotes were
    directly checked. Meyer PDF extraction loses fi, so typeset fidelity is not text-layer
    or native verification. Native outcomes remain UNRESOLVED/NOT_IN_ABSTRACT. Original
    Nature HTML was reread after fresh web access failed; it is not called a fresh
    download. Meyer Crossmark has no data; other bounded checks are not comprehensive
    notice clearance.
- evidence_id: products
  kind: validation
  reference: reports/proposal_citation_audit.tsv
  locator: Actual native checks, parsed RDF, byte preservation and responsive browser
    receipts.
  accessed_at: '2026-10-14T03:45:53Z'
  support: supports
  summary: 'All required local gates pass. RDF triple counts: {''classes'': 15, ''merged'':
    12628, ''reasoned'': 12632}. Only Meyer and the local record annotate the definition.
    All 645 pinned CLAW blobs match. Both configured embedding inputs are absent and
    existing embedding artifacts are retained.'
- evidence_id: history
  kind: record_content
  reference: history/records/nematode_egg_hatching_inhibitory_activity
  locator: Minting and append-only CREATE entries.
  accessed_at: '2026-10-14T03:45:53Z'
  support: supports
  summary: Observed acceptance at 03:09:57Z precedes CREATE at 03:14:30Z. Codex/GPT-5
    and LLM assistance are explicit. Record remains PROPOSED; no human sign-off is
    inferred.
- evidence_id: readme
  kind: validation
  reference: https://github.com/CultureBotAI/TraitMech/issues/1924
  locator: Initial failed focused receipt, corrected README and successful rerun/full
    suite.
  accessed_at: '2026-10-14T03:45:53Z'
  support: supports
  summary: Pre-review validation found stale category/prose counts (59 passed, two
    failed). The maintained README category row, total, prose and layout were corrected
    without changing test assertions. The successful 61-test rerun and full suite
    supersede that failed attempt. Issue 1924 tracks the correction through PR merge;
    it is not a remaining reviewed-tree defect.
- evidence_id: publication
  kind: search
  reference: /tmp/traitmech-egg-hatching-publication-20261014/accepted.json
  locator: Refreshed local ignored/hidden reservation and live remote identity guards.
  accessed_at: '2026-10-14T03:45:53Z'
  support: supports
  snapshot_sha256: 4ebe8dc4641c0b52482373136a50fbeabfc6e25033ed63bf582654608af52e4f
  summary: 183 known locations rechecked. Owned hits separated from competing reservations;
    no conflict identified. Remote and retained-head identities remain as inspected.
  search_scope: Available ignored/hidden files included. No lost historical ignored/untracked
    reconstruction, symlink targets or arbitrary local archive decoding. Pending content
    scope is changed blobs, not entire PR trees. Not atomic allocation.
assessments:
- assessment_id: identity
  area: identity
  topic: Microbial bearer and measured hatch endpoint
  summary: Reduced nematode hatching defines a capability of the microorganism. Egg
    susceptibility and microorganism development are different meanings. Controls
    and observation interval bound the phenotype. No killing/recovery mechanism is
    required.
  target_ids:
  - traitmech:000723
  evidence_ids:
  - content
  - source-0
  - source-1
  outcome: supported
- assessment_id: evidence
  area: evidence
  topic: Primary hatch assays rather than adjacent endpoints
  summary: Both studies report their own hatch experiments. Host-specific concentration,
    denominators, timing and repeat scope remain explicit. Reduced root egg masses,
    juvenile paralysis, recovery or death cannot substitute for this evidence. Conflicting
    source details are retained.
  target_ids:
  - traitmech:000723
  evidence_ids:
  - source-0
  - source-1
  - content
  outcome: supported
- assessment_id: grounding
  area: grounding
  topic: Broader phenotype parent and non-equivalent neighbors
  summary: Phenotype is broader. Existing related traits have distinct endpoints;
    a producer may possess several. Bounded ignored-inclusive and ontology checks
    support local fallback without a global novelty or disjointness claim. No coupled
    repair is indicated.
  target_ids:
  - traitmech:000723
  evidence_ids:
  - ontology
  - novelty
  - publication
  - content
  outcome: supported
- assessment_id: provenance
  area: provenance
  topic: Direct excerpts versus native abstract results
  summary: Actual typeset/HTML source spans support the quotes. Extraction and abstract-index
    limits are not concealed. Only definition authority enters ROBOT annotation. Strain/accession
    ambiguity remains uncorrected rather than being guessed into a canonical example.
  target_ids:
  - traitmech:000723
  evidence_ids:
  - provenance
  - source-0
  - source-1
  - products
  outcome: supported
- assessment_id: products
  area: consistency
  topic: Guarded writer, exact RDF and preserved owners
  summary: Writer dry-run/replay/schema/drift tests, full QC, history, proposal and
    responsive browser checks pass. Existing records and immutable artifacts are preserved.
    README counts agree after the recorded correction.
  target_ids:
  - traitmech:000723
  evidence_ids:
  - products
  - history
  - content
  - readme
  outcome: supported
- assessment_id: limits
  area: completeness
  topic: Unresolved source and mechanism gaps
  summary: No egg-death/recovery inference, universal host or potency cutoff, shared
    active molecule, causal protein, field efficacy or environmental safety is established.
    These limits do not erase the narrower observed capability.
  target_ids:
  - traitmech:000723
  evidence_ids:
  - content
  - source-0
  - source-1
  - provenance
  outcome: unknown
findings: []
actions: []
limitations:
- Author self-review only. Exact-head external review, CI, native queue and landed-tree
  verification remain separate publication gates unfinished at this timestamp.
- Meyer pages were visually inspected during research and the quoted page reread during
  curation/review. Saharan HTML and actual Figure 3 were read. No complete raw-data/statistical
  reanalysis or independent experimental replication was performed.
- Hatch inhibition does not establish death, irreversible arrest, later recovery,
  universal host/stage response, a dose threshold, canonical taxon, field efficacy,
  mechanism or safety.
- Native UNRESOLVED and NOT_IN_ABSTRACT outcomes are retained. Neither quote is native
  VERIFIED. Meyer text extraction loses a ligature. Nature fresh web access and PMC
  browser challenge limited live full-text access; original bytes remained readable.
  Bounded notice checks do not certify comprehensive clearance.
- Canonical-example auditing used --no-resolve for shape only. No canonical example
  is asserted here.
- Known ignored/hidden copies were included. Four unavailable locations, lost historical
  ignored/untracked files, symlink targets, arbitrary archives and unchanged pending-tree
  content were not reconstructed. Discovery is not exhausted and allocation is not
  atomic.
- Configured embedding inputs are absent; existing embeddings are unchanged. Required
  empty ROBOT cells use a path-scoped whitespace exception, not an unqualified clean-whitespace
  claim.
- The initial focused run failed two README assertions and is retained as a failure.
  Corrected counts pass unchanged tests; issue 1924 awaits the reviewed PR merge.
tags:
- add-trait
- nematode-egg-hatching-inhibitory-activity
- self-review
```
