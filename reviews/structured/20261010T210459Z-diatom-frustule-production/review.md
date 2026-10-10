# Adversarial self-review of diatom frustule production

- Review: 20261010T210459Z-diatom-frustule-production
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-10T20:41:26Z
- Finished UTC: 2026-10-10T21:04:59Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The formation phenotype is supported by two primary sources and has the correct broader local parent. No actionable defect found. Source access and mechanistic limits remain explicit; mapping status stays PROPOSED.

## Scope And Provenance

One complete new TraitRecord, with its writer/tests, v567 proposal, provenance and generated surfaces.

Selection: Exact traitmech:000691 on the trait-scoped branch; no sampling.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7f67960eaeb1059552bbf6fe3a7e1ad0e552862e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| traitmech:000691 | data/traits/physiology/diatom_frustule_production.yaml | maintained | diatom frustule production |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| .venv/bin/linkml-validate -s src/traitmech/schema/traitmech.yaml --target-class TraitRecord data/traits/physiology/diatom_frustule_production.yaml | passed | True | traitmech:000691 | Completed successfully at its actual command scope, including corpus-wide audits. Existing baselines were not expanded. |
| .venv/bin/python scripts/validate_strict.py data/traits/physiology/diatom_frustule_production.yaml | passed | True | traitmech:000691 | Completed successfully at its actual command scope, including corpus-wide audits. Existing baselines were not expanded. |
| .venv/bin/python scripts/verify_snippets.py --record data/traits/physiology/diatom_frustule_production.yaml | passed | True | traitmech:000691 | Native snippet verification completed: Bedoshvili VERIFIED; Aram NOT_IN_ABSTRACT. The latter is an Introduction quote, directly checked in official full text, not an abstract-verifier success. |
| just audit-proposals | passed | True | traitmech:000691 | Completed successfully at its actual command scope, including corpus-wide audits. Existing baselines were not expanded. |
| just ground-predicates | passed | True | traitmech:000691 | Completed successfully at its actual command scope, including corpus-wide audits. Existing baselines were not expanded. |
| just ground-nodes | passed | True | traitmech:000691 | Completed successfully at its actual command scope, including corpus-wide audits. Existing baselines were not expanded. |
| just audit-graphs | passed | True | traitmech:000691 | Completed successfully at its actual command scope, including corpus-wide audits. Existing baselines were not expanded. |
| just audit-graph-protein-taxa | passed | True | traitmech:000691 | Completed successfully at its actual command scope, including corpus-wide audits. Existing baselines were not expanded. |
| just audit-predicate-domains | passed | True | traitmech:000691 | Completed successfully at its actual command scope, including corpus-wide audits. Existing baselines were not expanded. |
| just check-biolink-coverage | passed | True | traitmech:000691 | Completed successfully at its actual command scope, including corpus-wide audits. Existing baselines were not expanded. |
| just audit-snippets | passed | True | traitmech:000691 | Completed successfully at its actual command scope, including corpus-wide audits. Existing baselines were not expanded. |
| just gen-discussions-data | passed | True | traitmech:000691 | Completed successfully at its actual command scope, including corpus-wide audits. Existing baselines were not expanded. |
| just gen-qc-dashboard | passed | True | traitmech:000691 | Completed successfully at its actual command scope, including corpus-wide audits. Existing baselines were not expanded. |
| just gen-pages | passed | True | traitmech:000691 | Completed successfully at its actual command scope, including corpus-wide audits. Existing baselines were not expanded. |
| just gen-priority-dashboard | passed | True | traitmech:000691 | Completed successfully at its actual command scope, including corpus-wide audits. Existing baselines were not expanded. |
| just qc | passed | True | traitmech:000691 | Completed successfully at its actual command scope, including corpus-wide audits. Existing baselines were not expanded. |
| just validate-history | passed | True | traitmech:000691 | Completed successfully at its actual command scope, including corpus-wide audits. Existing baselines were not expanded. |
| just validate-products | passed | True | traitmech:000691 | Completed successfully at its actual command scope, including corpus-wide audits. Existing baselines were not expanded. |
| just verify-proposal metpo_traitmech_v567 | passed | True | traitmech:000691 | Completed successfully at its actual command scope, including corpus-wide audits. Existing baselines were not expanded. |
| just robot-validate-proposal metpo_traitmech_v567 | passed | True | traitmech:000691 | Completed successfully at its actual command scope, including corpus-wide audits. Existing baselines were not expanded. |
| .venv/bin/ruff check src scripts tests | passed | True | traitmech:000691 | Completed successfully at its actual command scope, including corpus-wide audits. Existing baselines were not expanded. |
| .venv/bin/python -m pytest -q --junitxml=/tmp/traitmech-frustule-checks-20261010/pytest.xml | passed | True | traitmech:000691 | 3790 tests passed, with no failures, errors or skips. |
| focused | passed | True | traitmech:000691 | 20 focused tests passed: identity and scope, source limits, proposal header/refinement, dry run, exact replay, preserved parent, drift refusal and prevalidation. |
| history-diff | passed | True | traitmech:000691 | One changed trait and one appended repository history; committed-diff provenance gate passed. |
| browser | passed | True | traitmech:000691 | Headless Chrome passed at 1440px and 390px: local identity, two quotes, two OPEN discussions, no invented graph/examples, history link, parent round trip, exact-ID browse, 1086-record dashboard, loaded coverage image, no overflow or page errors. Desktop record and mobile evidence screenshots visually inspected. Initial sandbox Chrome launch failed before page inspection; the authorized unsandboxed rerun passed. |
| artifacts | passed | True | traitmech:000691 | All 1085 existing trait YAMLs byte-preserved, including protected spore germination. Of old pages, 1084 change only footer; biomineralization adds this child. Only existing priority delta is parent child count 2 to 3; phenotype stays 181. Old histories, reviews, proposals, embeddings and discussion templates preserved. Canonical 11-column header and record/TSV agreement pass. |
| rdf | passed | True | traitmech:000691 | Parsed RDF graph cardinalities: {'classes': 15, 'merged': 12628, 'reasoned': 12632}. Correct w3id child 1064400 -&gt; labeled phenotype 1000059 -&gt; quality 1000188; no legacy OBO METPO stubs. Biomineralization 1064300 refinement is explicitly requested in narrative and TSV observations, not emitted by this standalone cohort. |
| sources | passed | True | traitmech:000691 | One exact source-qualified MED match per PMID, matching DOI/title. Bedoshvili quote matches scientific Abstract; Aram quote absent from Abstract and matches Introduction in cached official XML. Access sections and limits are retained. |
| fresh-novelty | passed | True | traitmech:000691 | Refreshed whole-worktree ignored-and-hidden concept/citation/full-block searches. All five pending PR heads and complete paginated file lists unchanged; current main unchanged. New external-to-owned matches were only inspected metadata of this branch. No unowned reservation or unresolved new candidate match. |
| whitespace | passed | True | traitmech:000691 | Ordinary staged check returned 2 only for three required empty trailing ROBOT directive cells. Exact-path exception and separate non-TSV check passed. Both headers are canonical 11 columns; no global whitespace setting changed. |
| Configured embedding source applicability | not_applicable | False | traitmech:000691 | Exact configured default/fallback paths absent in primary and owned layouts, checked independently of gitignore. Existing embedding artifacts preserved. |

## Scientific And Domain Assessments

### Production phenotype, not the material wall

identity: supported. Targets: traitmech:000691.

The definition denotes formation of new siliceous wall elements. It does not equate a cell structure, sequence feature, retained valve or chemical uptake with production.

### Distinct endpoint and allocation

identity: supported. Targets: traitmech:000691.

No exact existing record or conflicting ID found within the explicitly searched scope. Scale production, auxospore coverings and setae alone do not establish the endpoint; none is declared organism-level disjoint.

### Strictly broader biomineralization

grounding: supported. Targets: traitmech:000691.

Formation of the specified mineral elements entails mineral formation. Local parent 000690 is broader; standalone v567 uses released phenotype and explicitly requests the v566 refinement on adoption.

### Exact sources, quote sections and inference limits

evidence: supported. Targets: traitmech:000691.

Both primary studies support production; quotes are short contiguous spans with separate section attribution. Structural association and inferred maturation order are not upgraded to necessary mechanisms or longitudinal observation.

### Guarded writer and append-only history

provenance: supported. Targets: traitmech:000691.

The native curation event and repository CREATE history match the sole new record. Writer guards and focused regression tests cover dry run, refusal, replay and prevalidation; old records and histories remain intact.

### Proposal and generated artifacts

consistency: supported. Targets: traitmech:000691.

Canonical template, parsed w3id hierarchy, corpus counts, parent links and rendered identity agree. Old cohorts and protected records are preserved.

### Taxa, mappings and molecular causality

completeness: unknown. Targets: traitmech:000691.

Canonical taxa and exact mappings await authority review; production-specific molecular evidence and paired accessions are required before graph curation. Two OPEN discussions retain these limits.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| morphogenesis | DOI:10.1007/s00709-017-1199-4; Complete scientific Abstract at https://pubmed.ncbi.nlm.nih.gov/29270874/ and Europe PMC CORE EXT_ID:29270874 AND SRC:MED. Timestamp is the refreshed qualified CORE lookup, not first acquisition. | supports | Defines frustule components as silica valves and girdle bands and observes valve morphogenesis in Encyonema ventricosum. Online 2017-12-21, issue May 2018. Full Methods, actual figures and supplements unread. Cytoskeletal proximity does not establish molecular necessity; the short quote is exact. |
| tomography | DOI:10.1038/s41467-024-52211-x; Scientific Abstract, Introduction, Results, Discussion and Methods in https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11385223/fullTextXML; actual Figure 2 inspected. Timestamp is cached XML reread and exact Introduction-quote check, not a new download. PMID:39251596 independently source-qualified. | supports | CCMP1335 silicon-starvation/resupply and cryoET support valve formation. Figure 2 orders different cells by inferred maturation, not a longitudinal time series. Cell-wall terminology supports definition; Results support production. Contact-site function, transport and actin expansion remain proposed mechanisms. Historical Thalassiosira pseudonana naming is not current taxonomy assignment; other actual figures and supplements unread. |
| novelty | proposals/metpo_traitmech_v567/proposal.md; Allocation and novelty, proposal hierarchy, upstream template contract. Access timestamp is proposal reread, not earlier search execution. | supports | No exact record or conflicting reservation found in the bounded ignored-and-hidden searches. Scale production and biomineralization are distinct/broader. Full block 1064400-1064499 reserved, only 1064400 populated; v566 remains unchanged. |
| record | data/traits/physiology/diatom_frustule_production.yaml; Complete new record and comparator definitions/discussions for biomineralization, scales and coccoliths. | supports | New valve/girdle-element formation is a reusable phenotype under biomineralization, not a material frustule, retained valve or generic silica uptake. Scope does not require both valves formed anew per division or all parts made simultaneously. No synonyms/xrefs, examples, causal graphs or protein accessions asserted. |
| implementation | scripts/add_diatom_frustule_production_trait.py; build_record, proposal_tsv, main; focused test file and new repository history. | supports | Writer defaults to dry run, checks parent identity projection and target/proposal drift, prevalidates before writes and permits exact replay. Controlled fixture tests preserve parent bytes. Native per-record event and CREATE history retain correct agent, actual decision/write distinction and PROPOSED status. |
| products | reports/proposal_citation_audit.tsv; Completed native generation/checks, artifact byte audit, parsed proposal RDF and browser inspection. | supports | 1086 records and consistent native products. Exact pinned CLAW a5d562962c75a2ad9efd8160b548df5944315422 source verified across 152 source blobs and used for shared generators. Embeddings preserved because configured sources are absent. No baseline relaxation or unrelated record edit. |

## Limits And Additional Notes

- Author self-review, not independent review or human scientific signoff.
- Full coverage means this one target, not a scientific review of the entire corpus. Broad input hashes support comparison and deterministic checks only.
- Bedoshvili scientific Abstract read; full Methods, actual figures and supplements unread. Aram main text and actual Figure 2 read; other actual figures and supplements unread.
- Native Aram snippet outcome remains NOT_IN_ABSTRACT; direct Introduction verification is separately documented.
- No canonical taxon, synonym, exact external mapping, protein accession or causal mechanism asserted. Two discussions stay OPEN and the term remains PROPOSED.
- Standalone v567 emits the released phenotype ancestor, not the requested biomineralization refinement; upstream adoption must reconcile v566 and v567.
- Configured embedding sources absent; old embeddings preserved. No paid research performed.
- Curation-decision time, history-write time, source recheck times and review times describe different events. Working-tree input hashes are reviewer attestations, not proof the reviewed bytes were committed.
- No new defect issue warranted by this bounded pass. External review and final CI/reservation outcomes belong in the PR.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261010T210459Z-diatom-frustule-production
kind: record
repository: CultureBotAI/TraitMech
title: Adversarial self-review of diatom frustule production
started_at: '2026-10-10T20:41:26Z'
finished_at: '2026-10-10T21:04:59Z'
reviewer:
  identity: codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: The author performed this falsification-oriented pass. External
    review requests and green checks do not make this assessment independent.
skill: .claude/skills/add-trait/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The formation phenotype is supported by two primary sources and has the correct
  broader local parent. No actionable defect found. Source access and mechanistic
  limits remain explicit; mapping status stays PROPOSED.
source:
  git_revision: 7f67960eaeb1059552bbf6fe3a7e1ad0e552862e
  state: working_tree
  inputs:
  - path: .claude/skills/add-trait/SKILL.md
    sha256: 2869d64c2e438f2bb81e9d834496e2c42d0c1c16a4a7b246f531558096856e97
    role: context
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: da8896328a0fd6cc92f1adf0d8be8980d0ddd41f3172c7936f2c7f119b293ac1
    role: context
  - path: .claude/skills/manage-identifiers/SKILL.md
    sha256: 31a472fe425d6b97986e9694d1dd2c51594243b284c7b13569134f9601a39d7e
    role: context
  - path: .claude/skills/metpo-proposal/SKILL.md
    sha256: d617b5e25518ec0cb26f2eda00364a2c4c8b4e5cb703814256af6d8deae892e9
    role: context
  - path: CLAUDE.md
    sha256: 4d328127022388e1affe9b71be24bc93944a971636d0d0ea902f6511e0b405c5
    role: context
  - path: DO_NOT_WORK.md
    sha256: 9ae0b05cc06f4ce8938801287a568d535e471d06dda5e258fcdbbed222abf712
    role: context
  - path: README.md
    sha256: ace3fb50ebeac9e39ff0bf72ebf4727fde274cb14d4c3a3705db7de8b5d75129
    role: context
  - path: app/dashboard/priority.html
    sha256: 5217d9fe0f3408929c5e6c622b7071af85c2ad791e1da1fae2f46208a46a3de0
    role: context
  - path: app/dashboard/priority.json
    sha256: 0796bc290744f8c8e3e8a929d1c13206260cae94369abef19c6c15e70bdb1226
    role: context
  - path: app/discussions/data.js
    sha256: 01c195e8f7dfc53fb3d0f49bbfe6779dfb9a3bbf4b27c22adb1eaca4eb6ab598
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
  - path: dashboard/index.html
    sha256: 11f0f22cac4b37e68bf41d5fccd3c22104dae258083fafec5db45476228ec9ea
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
  - path: data/traits/ecology/commensalism.yaml
    sha256: 145d5d82edb69ec596fe6b1fd068ee6eb686cfd6da37f0aff22427fa8ce5907d
    role: context
  - path: data/traits/ecology/endophytic.yaml
    sha256: a71d78c4bde350bd7941f5e5e7340207d67ee1d86cfa7ee76bc7236c10221d6a
    role: context
  - path: data/traits/ecology/endosymbiosis.yaml
    sha256: e42e413a5d2a662aabbd7add9be674718bfc392a1bcc16f1d55fdb8d3c37cb91
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
  - path: data/traits/ecology/plant_pathogen.yaml
    sha256: 4c8c4cf20790c060a91495e96a13656c7d7b72ef0856b0fbc2598ff53a99eb00
    role: context
  - path: data/traits/ecology/predatory_bacterium.yaml
    sha256: d69bf9a84c935eb0c3fbd5b31283ab56ec9f06f5e573093d9a145c89205a6287
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
    sha256: 6112ab015ce3f2da3417cc9dca9ad6b6b7267e01ca05c1644c22d62fa2e43196
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
    role: target
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
  - path: docs/record-review-profile.md
    sha256: 37e37e274e9e884245948242a2b18cee202579ca1f740a7e44a72e0b4817012c
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: history/README.md
    sha256: f795a191e17978454a8bb80da91ed6873a9405a240e6e5758837dd9bdc3b5c07
    role: context
  - path: history/records/diatom_frustule_production/2026-10-10T201809Z-codex-7489a5.yaml
    sha256: 9b4ec7230061be500fec41e26bdbd1591f18e3b36406838dc70e47f88817406d
    role: context
  - path: justfile
    sha256: e6047ea612115a6a78d100b281483ba824c860c3def59bcd0d40e7fb56b3526a
    role: context
  - path: pages/browse.html
    sha256: 048f5aeac72b12a554477ab6263ad8d4fe1ff1074476ad9cf0589b3e57813ed2
    role: context
  - path: pages/category/ecology.html
    sha256: d61a6c83a8306f4c7ce809586bd140921b262b582b6743e2d0d236ff337effbc
    role: context
  - path: pages/category/environment.html
    sha256: f7ed21d0baf3289bfefd0b2a351e6b0489963dd3f2861fb8bbbaa9b10020a2b9
    role: context
  - path: pages/category/genomics.html
    sha256: 53f556913ea48603ca289b31ab8b1b0b4b379baa5253f3b416f6276453d145a6
    role: context
  - path: pages/category/metabolism.html
    sha256: e20c1b22963505aa8c6d8e05b5fb0bdbd45a2743eb9215a2750dcf715accb461
    role: context
  - path: pages/category/morphology.html
    sha256: 8d0b9ba7707b74d77acbd71a0e69aed1cbcaa2d106c3a3ca4227dc2b2055bd41
    role: context
  - path: pages/category/observation.html
    sha256: f81cbee12580457c0e18de0b08bfb6716a85937f4a0c9f7896bc9da7fd8e9918
    role: context
  - path: pages/category/other.html
    sha256: 1d59e4a168e0d95054a447de83cf4ebb00125f5bfec96b94832846138ebb7e1b
    role: context
  - path: pages/category/physiology.html
    sha256: 056e8a26581468d4efd060e050c89a79614e5c22eefd9430eead743f93a3eda9
    role: context
  - path: pages/category/quantitative_property.html
    sha256: 7deb3d8b2639c0c36fee4b656dde118bccb671184b815327c6cba0b094c2dfca
    role: context
  - path: pages/category/upper.html
    sha256: 5d2f1699c3ed477d00272eb509a7d71c153239679bab420b4beba5942977032d
    role: context
  - path: pages/graph.html
    sha256: a555cc1b7a3280bf19f5f9c50854f39bd7fb1653811da7ba8d430eb5411d2592
    role: context
  - path: pages/index.html
    sha256: 3ec369a281327aff81f8de3582740a019e6f266fc185b2caf3b7c88dbe61cd0e
    role: context
  - path: pages/traits/ecology/animal_pathogen.html
    sha256: 9256398ca6ce2295308ea59aba9ffa3dff6e29d48a102d31f6d9ffd52a1c7464
    role: context
  - path: pages/traits/ecology/bacterial_cannibalism.html
    sha256: 95317438d176c253c5dcb17ea2cc171413daf4693c41ee09093ef858f28bb67d
    role: context
  - path: pages/traits/ecology/biofilm_formation.html
    sha256: ff639809afe6acad2c72a26cbdf58f0f2deb8c08b8935d98986037cb86933c27
    role: context
  - path: pages/traits/ecology/biosafety_level.html
    sha256: fa4b59e8f4df4f402d8320641840c6758d60356ce8970a2893d9b225355a58fc
    role: context
  - path: pages/traits/ecology/biosafety_level_1.html
    sha256: 37dab6024f4116ef7f614110754450e46a44318a2ea71985ae22f3e7cd02e355
    role: context
  - path: pages/traits/ecology/biosafety_level_2.html
    sha256: 1ec3eb79655d821264669d0063d511b1681f566e131a96fdd8e3964ce97ee99d
    role: context
  - path: pages/traits/ecology/biosafety_level_3.html
    sha256: 74506e8d6ac815640c289a4a8db30b3798e956acc631962a6400f11cf3e53f6a
    role: context
  - path: pages/traits/ecology/biosafety_level_4.html
    sha256: cb8fe30e7ee6b45a60006bb787f04c2c1bec16ee3c6c594412490125ecdfd08e
    role: context
  - path: pages/traits/ecology/biosafety_level_5.html
    sha256: a8cb423cee70bde1174c2430bc46228edacc6bac42c717ec7a86b42bacd568e0
    role: context
  - path: pages/traits/ecology/commensalism.html
    sha256: f4b589475142ee1da92d4d8f3b36ea492b8abf8df577d797391e16b0153f0b9f
    role: context
  - path: pages/traits/ecology/endophytic.html
    sha256: c8cfb2fe61efb7e380a342ff7da8845d6c0c857686526a4c1c1889a6d35ed313
    role: context
  - path: pages/traits/ecology/endosymbiosis.html
    sha256: 06d16243472034c7dd91b0e114661ae2047910d0bfea655426499d663cb3d1a0
    role: context
  - path: pages/traits/ecology/epiphytic.html
    sha256: 4202718d7aa0ca866be05cdade0181ec1a5d5012f22127257dcf8e05033a6834
    role: context
  - path: pages/traits/ecology/free_living.html
    sha256: 6769190abcfe5992ae3d5ac3ccaeb7adcaac282cd6725cc7cd99698598adcad1
    role: context
  - path: pages/traits/ecology/gut_associated.html
    sha256: ceffe8d63da9507f43ae2b31e2239f88bbf24f743516a53192a20d9bc0053526
    role: context
  - path: pages/traits/ecology/habitat_association.html
    sha256: c6463fc01f2dcb9913c5d53619c5b455b815daa92a3e44f730a559c51a59c1ba
    role: context
  - path: pages/traits/ecology/host_associated.html
    sha256: aa80817f6ae3b163b2d42137bb416bbb6854bf6d6f9f62b2395ee8f3b1cc7ee4
    role: context
  - path: pages/traits/ecology/human_pathogen.html
    sha256: 094209da9f750f1b1650d5ec52a74bacf32862ec337d8fb1c480735a78cfd0b6
    role: context
  - path: pages/traits/ecology/mutualism.html
    sha256: 2338339fcbb61bf5905076101a0823f6f44ccb0be9ddcab7d56b75aafb54cdef
    role: context
  - path: pages/traits/ecology/nitrogen_fixing_symbiosis.html
    sha256: c559f6d1ff9819db318f22e6cb611fcdf29b01ada5532c54c2aef4f75c4b49e2
    role: context
  - path: pages/traits/ecology/opportunistic_pathogen.html
    sha256: cc41bf26fac6c24c7d5bc8d08db1c2fb5c46934d3f7fceeb5cca7c9b955667a5
    role: context
  - path: pages/traits/ecology/parasitism.html
    sha256: 442fdb7dc827d4429990939369372889d1baf0a513b9f74e09883fb2e9192668
    role: context
  - path: pages/traits/ecology/pathogenic_to_host.html
    sha256: 8c3d5bd28ee25c3307d1e16839eb52e3140478fa5cd1d12d6def4c6b5370b7a9
    role: context
  - path: pages/traits/ecology/plant_pathogen.html
    sha256: 6fe9e363e91d7fd4aa4b98cd27981412cc2bdce521530f77ecdade49edbe0d68
    role: context
  - path: pages/traits/ecology/predatory_bacterium.html
    sha256: 40131c3f059c18bdf1cf5ae054cff5a1770350e5f748f2945d58783737ac835b
    role: context
  - path: pages/traits/ecology/rhizosphere_association.html
    sha256: 21ef5e166c3d90652af794bff99a1ce3c1500c206ed1f7c091d05e5282b8883a
    role: context
  - path: pages/traits/ecology/saprotrophy.html
    sha256: ad5da48e765c08d95e8f224dc110dc86b9abdc67dfe436fd12f4bf4b37fe24ec
    role: context
  - path: pages/traits/ecology/soil_dwelling.html
    sha256: 60f9665af803d4bd1fa6b9cf0b9984dbf77ed8de559a189b43e13f4f8140e271
    role: context
  - path: pages/traits/ecology/symbiosis.html
    sha256: 4f5ca1f94851cc475d7a7c2817d45e5bc722c60da3097cedb33c3f555b8357b5
    role: context
  - path: pages/traits/environment/acidophilic.html
    sha256: 1d97ed93eb14a2aa6ef2003ce1cd893a4fee59d65112aad2923bd935cf1b7d38
    role: context
  - path: pages/traits/environment/acidotolerant.html
    sha256: 01d1f40660d57150ad0a35fee1a78310a4976e90b16bd7d472c8dec0d35cfce4
    role: context
  - path: pages/traits/environment/aerobic.html
    sha256: 8494c90ed01af988ef1730589905bf334365962d929ba42c9a5eb48a1f97628d
    role: context
  - path: pages/traits/environment/aerotolerant.html
    sha256: 92baf180985b5a2a53db4f24d8c122877a3617cd2d8edef28d0c8f1b654e261f
    role: context
  - path: pages/traits/environment/alkalotolerant.html
    sha256: c253662d43ec9621c917a00b22f713eb25a431ddce60539d18df8e5866d6f8c4
    role: context
  - path: pages/traits/environment/alkaphilic.html
    sha256: 2ed3c50b5e0e70552822682385fa8a10c72362f2e4993b726f8015ff7a60dce4
    role: context
  - path: pages/traits/environment/anaerobic.html
    sha256: 20363002af52c5323769c993f9cda068b391a4385ebb8db593f8a429e626c5ff
    role: context
  - path: pages/traits/environment/arsenic_tolerant.html
    sha256: f60316ec472bbcdd84eb2459d4070d99d5e50b484a47ad8ad25e272d9b03f63b
    role: context
  - path: pages/traits/environment/cadmium_tolerant.html
    sha256: 0f252a10249c807296bea398711b8130095518ef70db20198b118b94bb9a1a5e
    role: context
  - path: pages/traits/environment/capnophilic.html
    sha256: 7e5ef904bdc7d144dfe352eab74994a9a8837fdebbd7e0852fd41003bb49f89e
    role: context
  - path: pages/traits/environment/cobalt_tolerant.html
    sha256: 71b610487ef7ae5c2a0127dbdb2bf987cd726762d51d6ab209f69cea24fc8703
    role: context
  - path: pages/traits/environment/copper_tolerant.html
    sha256: 50d5fb048a7b221e4ef9311df939e0b20be4d2e21ef8f4d9d7bf90837bbdf884
    role: context
  - path: pages/traits/environment/delta_phenotype_with_numerical_limits.html
    sha256: 84d0313025d3c1f89351276616486f444c235ffdab03e0e58082fbd8019e5855
    role: context
  - path: pages/traits/environment/desiccation_tolerant.html
    sha256: f4be3d3a2b9ee44777fe19f37b4d1470f0a30e712fa13264782c559e975d5712
    role: context
  - path: pages/traits/environment/euryhaline.html
    sha256: ef77b7aa8443cafe7f33e03a069ca8d5bf1d0365bd2e7d5a039e2f0212a849a0
    role: context
  - path: pages/traits/environment/extreme_hyperthermophilic.html
    sha256: 9c490a95703d85296599f29e69fed54adeff0c690d0daab7cf406c0b3359fcaf
    role: context
  - path: pages/traits/environment/extremely_halophilic.html
    sha256: 68ed4f6f914747e630f99077fcee3dc73a872d3e0ff2195d504ddd83a9d306c8
    role: context
  - path: pages/traits/environment/facultative_oxygen_preference.html
    sha256: f1e687a2a7e290ccbe012aa9771dc77bc594bb79ac57d43563097c1217c47186
    role: context
  - path: pages/traits/environment/facultative_psychrophilic.html
    sha256: 77a7e37182ccfd642d3da0dcda59bd2c0c9283bd12c90319724701fe40a6fa64
    role: context
  - path: pages/traits/environment/facultatively_acidophilic.html
    sha256: 28ca93a4e7d60eac4e5e4f25569274bb8b35cabd9a4b6734f7b1c714117e9591
    role: context
  - path: pages/traits/environment/facultatively_aerobic.html
    sha256: 1b94eaa92776c6f97fad0dd785c648952e4bcf8a4d5b119f348fafddcc1ee7c4
    role: context
  - path: pages/traits/environment/facultatively_alkaphilic.html
    sha256: f53137a48cc635806834deb10d9f133d56b21800a82ff78b0608d159456e3c36
    role: context
  - path: pages/traits/environment/facultatively_anaerobic.html
    sha256: 1c90a345912d01be158b8857842bea3b7d9323e009271cb179ed8b0f31d46bbd
    role: context
  - path: pages/traits/environment/growth_range_phenotype_with_numerical_limits.html
    sha256: 2ab1f2dd7b536ae3584acddc99c8a34d9c3b4d2cb68725029d45bc16349e5c82
    role: context
  - path: pages/traits/environment/haloalkaliphilic.html
    sha256: d69b707562cb45306db3fc41daf1faea722b053fa5f517b0027f82a02eadb296
    role: context
  - path: pages/traits/environment/halophilic.html
    sha256: 1ce27388e0c3e758ce1bd620076919479a7ed59ad4bcd91cda9ba67bff731d68
    role: context
  - path: pages/traits/environment/halophily_preference.html
    sha256: 70a2fc9bb788c0d7f1279f6700ce184cd9e499fb7f7d418939d8d754fafbd60d
    role: context
  - path: pages/traits/environment/halotolerant.html
    sha256: b855030c171feba64a92b46a8a87e222be10efcdcbd7e2c351aa05e2b23b4b13
    role: context
  - path: pages/traits/environment/hyperthermophilic.html
    sha256: 5a3ffb17bb60bd50908d7fde40be13d187a9157247f9f580e7abfb32e7d12aee
    role: context
  - path: pages/traits/environment/ionizing_radiation_tolerant.html
    sha256: d4c595eddb36de4161f973f9292c8d8d6b83ca4c388daa1b45eb8d57b442032a
    role: context
  - path: pages/traits/environment/mercury_tolerant.html
    sha256: 9116ff5a626b8ce4e572944ead3bad04ab5cd7f3b117f9acade84268e0867d78
    role: context
  - path: pages/traits/environment/mesophilic.html
    sha256: 526f4238e57b78f039874632addd4fc25f2a6da7d971c42e28b4a0cc606f4797
    role: context
  - path: pages/traits/environment/metal_tolerant.html
    sha256: 77a8ad97f3342ddd865af4405c969ea64b0b2227b0c66162fcdf98df1630f10b
    role: context
  - path: pages/traits/environment/microaerophilic.html
    sha256: 5a95b0f4b3cdedd4c74f3bf7fc6e568e37ed2f4a69864e4658dd31a964750297
    role: context
  - path: pages/traits/environment/microaerotolerant.html
    sha256: 5fbf9bfe7222b20f90c36c336c8a82a84bbce7ad3cbe236a41a95683ad570bce
    role: context
  - path: pages/traits/environment/moderately_halophilic.html
    sha256: dca1c3815f79983aa33bf44582cd538a7b7941684e1902e70468aae10699e454
    role: context
  - path: pages/traits/environment/nacl_delta.html
    sha256: 27837cc90de5a9f166e72461c7c91b5f488735901607cc5417f808cb38e370b3
    role: context
  - path: pages/traits/environment/nacl_delta_high.html
    sha256: 6adb4ee57a53ff5da668ffeb2d5ef7f28bd3309d04891c12bc176afcf71724ae
    role: context
  - path: pages/traits/environment/nacl_delta_low.html
    sha256: 1917ea69be481bfe98e0afa4e11f6a4f6625778bf50b8aa4e4af07982f231d3b
    role: context
  - path: pages/traits/environment/nacl_delta_mid1.html
    sha256: a9e1a38b9ae80b230e0d890ba16b21f8b50bd273e4bce0ab1b9086b08b113632
    role: context
  - path: pages/traits/environment/nacl_delta_mid2.html
    sha256: 6c2c433f8203f22b90b34fb869819eca60bc73b09409b063618ff231fc3b38dd
    role: context
  - path: pages/traits/environment/nacl_optimum.html
    sha256: 30011870cb375c1f0e6c1b1cc4b2e571818155dcab63b44159eb5510cfabf032
    role: context
  - path: pages/traits/environment/nacl_optimum_high.html
    sha256: d669c282efa82a568804230158c7764cb4132953d21409417804d84d490fd960
    role: context
  - path: pages/traits/environment/nacl_optimum_low.html
    sha256: 4547d8c2363d76c83cd629955f490f6f589a25b7b6c8984a1ae4be302641c932
    role: context
  - path: pages/traits/environment/nacl_optimum_mid1.html
    sha256: 3206912e0d1b63acf7ef3056916e5972945b88c03737963cc049e77d0a266931
    role: context
  - path: pages/traits/environment/nacl_optimum_mid2.html
    sha256: 2b2814d98adbcdb856be02de1a9258a6e9a4f7c37caf35e2cc0237c9ac9906df
    role: context
  - path: pages/traits/environment/nacl_range.html
    sha256: 5e21b355c321169718f0b8757c6a8b8975ef0198c787c3e71a6fe0676a560d2f
    role: context
  - path: pages/traits/environment/nacl_range_high.html
    sha256: f79db1f695533186b5aa39f558fb4421ba721950135eb8fcef2589bb8becc9ae
    role: context
  - path: pages/traits/environment/nacl_range_low.html
    sha256: e1178c96121fd2a8d5cc61effd19861690be6b6e30622a07675a48f884f61c3d
    role: context
  - path: pages/traits/environment/nacl_range_mid1.html
    sha256: be758d509931c9045aa046fc5e6ae7d3486b82cb3eca3250208fff2b4a5fe24d
    role: context
  - path: pages/traits/environment/nacl_range_mid2.html
    sha256: f5eb78ba587a6fbdb6242194204793465820dd0e255288390b3235fadac2daef
    role: context
  - path: pages/traits/environment/neutrophilic.html
    sha256: 4a4f87891d0d573adf938b9664379de4a80e2823d909e456a24d7ff226d8dcfb
    role: context
  - path: pages/traits/environment/non_halophilic.html
    sha256: 8d386a859d0c9f1f23a4d514f2359b5209594e2a387fa0edfae2e79df383b72a
    role: context
  - path: pages/traits/environment/obligately_acidophilic.html
    sha256: c147f9f5a08100843afabda32b4a7cce7386231f59b1ef6fc35ea299466445ed
    role: context
  - path: pages/traits/environment/obligately_aerobic.html
    sha256: db54257c283826f5650731c88a30e1d60e2833b68dbdec2fcbf3f9223b5c8666
    role: context
  - path: pages/traits/environment/obligately_alkaphilic.html
    sha256: fd29bb09373f035f08d168c01a8d3e5228fc825516a755f76379fa3a20358a44
    role: context
  - path: pages/traits/environment/obligately_anaerobic.html
    sha256: 1430b672b0c48c18bcee6d3f11801d62c89ab4f1c5c547ffcd6a63804f877167
    role: context
  - path: pages/traits/environment/obligately_piezophilic.html
    sha256: f486c9821b9c842dfe0db424bf19a8d1419d819940bdce39c389544bb38de7a7
    role: context
  - path: pages/traits/environment/optimum_phenotype_with_numerical_limits.html
    sha256: 3ac20fb76e0fb165021e8ac4b90dbe7909b04bc3a78b3d8360a455a84de26d78
    role: context
  - path: pages/traits/environment/oxygen_preference.html
    sha256: 98bdf2d6142c104d204f646ce2b07fa707345b2182c8555ef61ce6a59b520593
    role: context
  - path: pages/traits/environment/ph_delta.html
    sha256: 79e8c7d028fce5915f2c1f4df5b0c0974c364efba886ede998b8b3f3a453f626
    role: context
  - path: pages/traits/environment/ph_delta_high.html
    sha256: eb9faf0cb16699a8b0fef8f42dfa45579d2aa45df4d907f4ecb41c58622761e8
    role: context
  - path: pages/traits/environment/ph_delta_low.html
    sha256: 92f351bbb812272ea2837322528d9f2d4048c65f10319b9e42232d45ce9356df
    role: context
  - path: pages/traits/environment/ph_delta_mid1.html
    sha256: 2c2e096d7c9f5b748132f0391404e64e4a1e5f06eb85e04789f6d9570347f4cf
    role: context
  - path: pages/traits/environment/ph_delta_mid2.html
    sha256: 0d85272dea24608896daaf26957e2aeaf895f9ad41a82fa5c0621271850b15d6
    role: context
  - path: pages/traits/environment/ph_delta_mid3.html
    sha256: fe9280a26df95fd02f07b79736de6e7980b2bda5055ad13896c4432046e320ed
    role: context
  - path: pages/traits/environment/ph_delta_very_low.html
    sha256: bcd32c78af17487eb0b5680975bd920461a80e58de15a58308580aac4de8e35f
    role: context
  - path: pages/traits/environment/ph_growth_preference.html
    sha256: 3435427a37f8692086f70c2f9b787daa4012900ae553c662297db6c0da25902d
    role: context
  - path: pages/traits/environment/ph_optimum.html
    sha256: 3104f68920aa36c384a1f39e821e8d435f384ca4d09a95833265dd3bbd840331
    role: context
  - path: pages/traits/environment/ph_optimum_high.html
    sha256: b323cc7fa292e31b5efeff445e2bab928514b9d67ff9a053fa00516f7e7b686d
    role: context
  - path: pages/traits/environment/ph_optimum_low.html
    sha256: 555b45299b88ea356165fcb59f21944c68c67345f7d3adba27c9a68651c7f0a8
    role: context
  - path: pages/traits/environment/ph_optimum_mid1.html
    sha256: 440384678bb86d31f6457ea59fbed66dd5f55788d6ce507cdacd7e51cc0860f2
    role: context
  - path: pages/traits/environment/ph_optimum_mid2.html
    sha256: 93fbc70e85e303a5326271474307b3c59225e4824de67bf1e8208ea1378576a9
    role: context
  - path: pages/traits/environment/ph_phenotype_with_numerical_limits.html
    sha256: ed4d85857aece1e147b66453ea641919bd6c5210696dac8ca43ba9c4639094e7
    role: context
  - path: pages/traits/environment/ph_range.html
    sha256: 0f558030a7b164a3d2ada302d20361da07aafdd0e4114a62506f33450fb8b043
    role: context
  - path: pages/traits/environment/ph_range_high.html
    sha256: 8d25397277912b590e5234726987a51333ee24592cb502b92d24273845f0eba5
    role: context
  - path: pages/traits/environment/ph_range_low.html
    sha256: 3580d6c2672889ffa1bfdf1aa963322d8ba74f4aacd4caaaf27217b85af1a56d
    role: context
  - path: pages/traits/environment/ph_range_mid1.html
    sha256: cfd02eac617a81eeff6ee9d2755e3b9a87dc609b4e87a3eae3a492e57f471999
    role: context
  - path: pages/traits/environment/ph_range_mid2.html
    sha256: b1b797cdcea1c856e3b798301fd34b327b300c6dfd3a7d96d51d5a696966da41
    role: context
  - path: pages/traits/environment/ph_range_mid3.html
    sha256: 04db8862b852c0dd5420a89801d602c3f5846eb3b60cd9ab6e1d4ee937ac410c
    role: context
  - path: pages/traits/environment/ph_range_very_low.html
    sha256: 791ea5574ceab362802b1d8a67790f58d3470f9f205a7068774653efc9287d55
    role: context
  - path: pages/traits/environment/piezophilic.html
    sha256: a2defd5b2e870116ed05762ccfaea08c9859cc9505149424247ee36abc7868da
    role: context
  - path: pages/traits/environment/piezotolerant.html
    sha256: 4922912cd4976a1b39f7dfbcd5b48f7420dfb41e6b6b6f9b852265ae2a1ce279
    role: context
  - path: pages/traits/environment/pressure_delta.html
    sha256: c2f8e2b620284d7e30861b29f180dbf8d69e403e5f0150f6e294af45963da491
    role: context
  - path: pages/traits/environment/pressure_optimum.html
    sha256: ed1ef3b74a2700ed437e4e7610613dc1fd09f09471c0bb25c440edc6b27b53b0
    role: context
  - path: pages/traits/environment/pressure_range.html
    sha256: 4eb3e86693c1ec48998b11185585d27c8ad42ebf8c7a3595229bf4cc349bd435
    role: context
  - path: pages/traits/environment/psychrophilic.html
    sha256: a36a54b4ceb0c0daa3e4ef56ce755b281b670117e4f6a2808aef3280a482df1d
    role: context
  - path: pages/traits/environment/psychrotolerant.html
    sha256: 6a752751d8987f7d58e2a511f1a8fdb2d1b3d5acb96f499314b23170801d79cc
    role: context
  - path: pages/traits/environment/radiotolerant.html
    sha256: 1b3dbaa3b11d9b1fcc1a74c9a7e9ddd49c1beff7052e48069bd51fc4a89a5f4f
    role: context
  - path: pages/traits/environment/salinity_phenotype_with_numerical_limits.html
    sha256: 51a70d70d18b11c8b6f4bb5d4b7f4144d5be3886786ffc27361630b9aabd93e0
    role: context
  - path: pages/traits/environment/slightly_halophilic.html
    sha256: 1b137c880ada612e3f64ce8934241d85f0c3532922c1965c423649260e26accc
    role: context
  - path: pages/traits/environment/stenohaline.html
    sha256: f08801b238cc702b6180b3edc8c570c6bb7c0e0ee5aba291a5ef9993640fe069
    role: context
  - path: pages/traits/environment/strictly_anaerobic.html
    sha256: 28835d24103b8633e27b7259a3f40e1c43a5a12aa8def4ab13dc4ceaae64e856
    role: context
  - path: pages/traits/environment/temperature_delta.html
    sha256: 1c2b3251ca64a904d7801c959a522d10f7fd29e4a95bc1852cdfa03918be4bde
    role: context
  - path: pages/traits/environment/temperature_delta_high.html
    sha256: 233af5faf1f37c7a3029df41dd5776bd4d6df775e5d0fb18a5da205d3d5f3994
    role: context
  - path: pages/traits/environment/temperature_delta_low.html
    sha256: 8a5f22c3e49c327eaefc91e138e71bd355372c0680669da6fcd69f5da63d321a
    role: context
  - path: pages/traits/environment/temperature_delta_mid1.html
    sha256: ec4f8e5eb0d0d69ca7493acb8d8d37ed8297cea620cf48a8f891b7c67a83df4a
    role: context
  - path: pages/traits/environment/temperature_delta_mid2.html
    sha256: 1a340a1d5b4dea151753a960180e0a33859b7674395e76209f0c64beb1ddb97c
    role: context
  - path: pages/traits/environment/temperature_delta_very_low.html
    sha256: dcdcc06ff50ae9115a2414a0cfccf1455a1c0766652b15acc5469060fe10707b
    role: context
  - path: pages/traits/environment/temperature_optimum.html
    sha256: 41c431c89b0a3943b5bbd6f76d650edc65dcb5e36cedd950f049a6d2b364e266
    role: context
  - path: pages/traits/environment/temperature_optimum_high.html
    sha256: 4eef8a719ec33fef9f4161c0d40b929d8ce9ee1cb7897a59fad0c336d32bf62b
    role: context
  - path: pages/traits/environment/temperature_optimum_low.html
    sha256: 1297414451b4488e9731e0d9d87b4e223b0ab9d3d52de917c6456ebea771ffb9
    role: context
  - path: pages/traits/environment/temperature_optimum_mid1.html
    sha256: a8c7233e4952c4dfb05209cd8a7c0f7ae4da03407d8d4b7eff1b7d457f640398
    role: context
  - path: pages/traits/environment/temperature_optimum_mid2.html
    sha256: 71b486cc57075eaebeb963f3ee50bb19a891a856afc28c4d14ae7fd6ada77380
    role: context
  - path: pages/traits/environment/temperature_optimum_mid3.html
    sha256: 2a90ff48d96a263900be45c604e7fd62cdc599d1c893042d04d22fc760b8d19c
    role: context
  - path: pages/traits/environment/temperature_optimum_mid4.html
    sha256: 2e9fc5c86e42c0db9a3c6a59ffbad152c26202aec07d1b1bbfd28b97d742547f
    role: context
  - path: pages/traits/environment/temperature_optimum_very_low.html
    sha256: 277cfe2d57b95aceaa489ce12875f13ba1db831c14f86947a19de9f51cefb9aa
    role: context
  - path: pages/traits/environment/temperature_phenotype_with_numerical_limits.html
    sha256: 6d1fd11bf906183efdca504005c57d40249bbec8d16a349cfeb3478ddf70d487
    role: context
  - path: pages/traits/environment/temperature_preference.html
    sha256: 367ac735a516c43871ea7459178e942131d12134881fbef1ed7afbd93cfec1ad
    role: context
  - path: pages/traits/environment/temperature_range.html
    sha256: 28ffbd0875393679d8034124abc91debd273903cf936446bda5fa35bc98d667b
    role: context
  - path: pages/traits/environment/temperature_range_high.html
    sha256: 1c28f22ae326d48d4c50a60ff4dbde5bc061ee73bb99611d3f1517b0595560c3
    role: context
  - path: pages/traits/environment/temperature_range_low.html
    sha256: 9016ea2bfa86dfa2f2a63bdff868b9aa23094738cc6d022fe83bab0e85a66a2e
    role: context
  - path: pages/traits/environment/temperature_range_mid1.html
    sha256: 86333db75f2533dc28a975c977cc9c5a107fd1a8b095129c0890358f4e54fdf5
    role: context
  - path: pages/traits/environment/temperature_range_mid2.html
    sha256: 7f19245532caef74361c5a1158a6155dfd45390e7349e58397652ad2676ff25a
    role: context
  - path: pages/traits/environment/temperature_range_mid3.html
    sha256: b45330c9e8e8b6a0da4456c9513c46d62eb4e689ee26dbf5439da773202386a0
    role: context
  - path: pages/traits/environment/temperature_range_mid4.html
    sha256: c30c5c50825c98f6ada2b0e5ef293a1e3cb8108e5395bb1fd368b386352e8bcb
    role: context
  - path: pages/traits/environment/temperature_range_very_low.html
    sha256: 99f37470c23a709a14dc301bc4b271d9f98a70e1865109ba4b0c43a50885b6a2
    role: context
  - path: pages/traits/environment/thermophilic.html
    sha256: 3a8bad6538a299eaf3ed2c46e9255c0d3cce215257a95e3befce6a67f4d411f4
    role: context
  - path: pages/traits/environment/thermotolerant.html
    sha256: a5b08054243b0edb6650d84b78a035107f163dd56b4f83dc6f8d31d84837efaa
    role: context
  - path: pages/traits/environment/uv_radiation_tolerant.html
    sha256: b2f30b74a38e3420896809bfc6e349dcd08613bdbb49cd746b6f3d2d94e0bf15
    role: context
  - path: pages/traits/environment/xerophilic.html
    sha256: 44e96e238d0f5311cf71af7b4915bbef7e8a2efb53e381e3bad088138785fec3
    role: context
  - path: pages/traits/environment/zinc_tolerant.html
    sha256: b00f47cdc7216ee64f342d8f9605a806d94c631138e8a33c33aa9a8602d226bc
    role: context
  - path: pages/traits/genomics/abi2_system.html
    sha256: ea669a8405a140614b5444a3d34fbc6d9a68171009c7d79749a4ec806cd26460
    role: context
  - path: pages/traits/genomics/abia_system.html
    sha256: 8e473318e878dd22e6f37f6baea8d7800eb48e74ef2735ef8a4dd3cb04148ef0
    role: context
  - path: pages/traits/genomics/abialpha_system.html
    sha256: 695e5267139d16aef3a4d9c52c5e7effde5caec847390ecd40482e39511f8a50
    role: context
  - path: pages/traits/genomics/abib_system.html
    sha256: 031ec6e0711cf91107ecfe04c32d6118b8b7aef0a656850e4a31a5d38bad875f
    role: context
  - path: pages/traits/genomics/abic_system.html
    sha256: fe17f832c7212695a34ca48b9cdb18cfa67a04e6494b337de08ed98eb26f2c99
    role: context
  - path: pages/traits/genomics/abid_system.html
    sha256: 14aa10e032e599813ae115033cb55a2acf6443ce590d06c080c927b7710574cb
    role: context
  - path: pages/traits/genomics/abie_system.html
    sha256: 9f1dcdf250701321e920fd8329b4973e26af0c7be628017fcb5192f51e21148e
    role: context
  - path: pages/traits/genomics/abif_system.html
    sha256: 2b3d0b1fd4ee2ebdc0b0d32ed55f527fa2650d5cd412bdf8690676e6c377b1c4
    role: context
  - path: pages/traits/genomics/abig_system.html
    sha256: c734c8ee03f677918d65e6c15cddfd6f1efe0958de0d8713c8b0b4bee1da0040
    role: context
  - path: pages/traits/genomics/abih_system.html
    sha256: faecbe270805a108b4e85a50805cf38d1c1d58d07da211676ca818fba7dba06b
    role: context
  - path: pages/traits/genomics/abii_system.html
    sha256: 36bb5b2084ebe04ab4b946f305fb2cce178e99fbca07e18308d29d0e625b168c
    role: context
  - path: pages/traits/genomics/abij_system.html
    sha256: 6e6b76f550941af0670dfd9f0b0517810211ad5d3d167e9e224c34aee19bac3d
    role: context
  - path: pages/traits/genomics/abik_system.html
    sha256: 1951e2e82cf8b88e456a9a82c47ce28c57b3681972045d21a06440f3cbba2b36
    role: context
  - path: pages/traits/genomics/abil_system.html
    sha256: 36e3911edc23bf10b8dfed3849d8f62ff58f29362e0edc3b5b78d7f2c9b6f479
    role: context
  - path: pages/traits/genomics/abin_system.html
    sha256: f92aa80fe6cc07cc1dd81e01092ed1848131fe9da7b47448fe962f57a4849915
    role: context
  - path: pages/traits/genomics/abio_system.html
    sha256: 2cd9fdfdd7f33c39d56d67fe3a2165541ed59047e3374ca976c45d7087828d3b
    role: context
  - path: pages/traits/genomics/abip2_system.html
    sha256: 4263836a987dcbbbda5eb3e7e672127c2cc9964728033212a290446c88c81533
    role: context
  - path: pages/traits/genomics/abiq_system.html
    sha256: e1269ec7d4864bc5ee0c4f4af19aacc8a9ebe9805557d99cad16a02e8b8b9c81
    role: context
  - path: pages/traits/genomics/abir_system.html
    sha256: 1304160b05134209b1bed96dee7974d292480d8013efaf95f6ebc3200319ac16
    role: context
  - path: pages/traits/genomics/abit_system.html
    sha256: 2bd9841c5e7f175923ed9f9811f288f8c24c8c9cb09e43c951ee422e9e575af2
    role: context
  - path: pages/traits/genomics/abiu_system.html
    sha256: 3daf8d92137dbdd5bb21236b3bb4bda298e822c9aec94a459a77db7285902258
    role: context
  - path: pages/traits/genomics/abiv_system.html
    sha256: ad358329577e38570e42695bab2365146e96a041d4a058c485164af1a5b40b6e
    role: context
  - path: pages/traits/genomics/abiz_system.html
    sha256: 5399a4615e6f96f880f26c1c12b595c6332c1f14bcad3393fb1a303b52b1640d
    role: context
  - path: pages/traits/genomics/abortive_infection_system.html
    sha256: 10bcdd6e15c50484344de1e705634b234fbf6707b114d25070bb4c33988c68d6
    role: context
  - path: pages/traits/genomics/aditi_system.html
    sha256: 713950548b035ba77d2ba9e79bdc62b875d9ee0124d6db03264a7ae7edc29a64
    role: context
  - path: pages/traits/genomics/ambrosia_system.html
    sha256: 0e45f270a3b0be2183b417d67ff4af0e4e1a09649a2adeeff65c19e2f155c920
    role: context
  - path: pages/traits/genomics/apsab_system.html
    sha256: a06d71ae0eacbdabf2d87ec8545aab69c602d6d3ebe847965e878ebc7567a11a
    role: context
  - path: pages/traits/genomics/aristaios_system.html
    sha256: 4da3db014f56ba662c2cea5cd85533d4e122d417ecf228dca39c684f57b8097f
    role: context
  - path: pages/traits/genomics/armada_system.html
    sha256: 3de424eff87e65d81045558598549ffb78390d0255b01dd24f54b346048443e5
    role: context
  - path: pages/traits/genomics/audmula_system.html
    sha256: fa8bb1bbe5d83909fc2c072c92c289f837f0aaf1b4bac669d9bba1d4730c3bd6
    role: context
  - path: pages/traits/genomics/avast_system.html
    sha256: 176eb66bf266fc17251698316b7aa70b9426cd298be870cbb6fca7c858b99b4f
    role: context
  - path: pages/traits/genomics/avs_i_system.html
    sha256: 4bff2199226884f1438ccaf4ef1fbd60bb8cbc98ea569e01538a8c747b4e08aa
    role: context
  - path: pages/traits/genomics/avs_ii_system.html
    sha256: 58cc3076418ea10298a39b6807773e02a1a81bf92e6b4cafd45483389d055b31
    role: context
  - path: pages/traits/genomics/avs_iii_system.html
    sha256: 88ad4c20c0a01e9b29b39441db8f823177717f8e7ffa9ae6b697f32ab9bf9a13
    role: context
  - path: pages/traits/genomics/avs_iv_system.html
    sha256: 80944cb7562bd61b84da98943739c198c888bdb7cce8f77a58a4c125037b5f4e
    role: context
  - path: pages/traits/genomics/avs_v_system.html
    sha256: 1ab7dc2d968caade3aea0d559133e727197132c26609ad06e5b3bb9bec469776
    role: context
  - path: pages/traits/genomics/azaca_system.html
    sha256: 1cb9d49a0df0b020a8446da0ab33d145aa1050089272e07cb20550425bf7b82c
    role: context
  - path: pages/traits/genomics/belenos_system.html
    sha256: 3583460ef58d677a897cc1d87969c6e6dfd5c7d62bf3bc743f3c84e03499f6d7
    role: context
  - path: pages/traits/genomics/belisama_system.html
    sha256: d6200b1d60c7e53ddc71a27e0e4439db21714664dee6d6bb6a801da3154e65ce
    role: context
  - path: pages/traits/genomics/bil_system.html
    sha256: 578ead76af1cfc2464124032d793ec2d25b92eac25ec65b90ec5d0361142dbe6
    role: context
  - path: pages/traits/genomics/borvo_system.html
    sha256: 9864f580dfc22735ac903f7ab5fc5a00b5ffc3d6fbfbf6b7be257237e2a8128b
    role: context
  - path: pages/traits/genomics/brc113_system.html
    sha256: 513ee63b8b4f44542038e7830157a2b228c44f61850ec0c99299c16c3f32323f
    role: context
  - path: pages/traits/genomics/brc142_system.html
    sha256: a46540427fd45aa7b1c6ca5718b3ceea07ddaba97b9e885ebe0e552d7560d316
    role: context
  - path: pages/traits/genomics/brc167_system.html
    sha256: e6dd45b1ce5d132439131b399dcaae9a27436c9e53be40dc7bf1bd6f8e6159ca
    role: context
  - path: pages/traits/genomics/brc217_system.html
    sha256: ffcd82ac441a2eaadedf0d67f55cdcca4ed76cd272170bb8d2e4abbafd46b3c1
    role: context
  - path: pages/traits/genomics/brc22_system.html
    sha256: e27aa3f231e465a0ac8f553e1b997f39a73135308ac9a6ce006009f8a8df838c
    role: context
  - path: pages/traits/genomics/brc233_system.html
    sha256: ee583d81ad0c8f45845d42e0ce58549441b1fd3f199c283624ab4d69d656ae2d
    role: context
  - path: pages/traits/genomics/brc23_system.html
    sha256: bf0ea8c3074e48abecbae3c5e62e006a4d1fc54fbbe76c559ac262a1212a3931
    role: context
  - path: pages/traits/genomics/brc24_system.html
    sha256: 0797044992fa855973acbc30ca7a04a41c312e5ccd20649a2690c9550a8af045
    role: context
  - path: pages/traits/genomics/brc59_system.html
    sha256: c8d23110174ca9daf682c38cc22b1035011e9ba150a2b5e4a6828b2121983231
    role: context
  - path: pages/traits/genomics/brc76_system.html
    sha256: 78cf028c56835ef5a6a52c3798ba3f6f55a352971304b445e40ac5d5e87a155f
    role: context
  - path: pages/traits/genomics/brcwgs21_system.html
    sha256: 22a578dffe9766a9c44af83b99559588cac7534fee343d2cf809f5d62a346cb8
    role: context
  - path: pages/traits/genomics/brex_system.html
    sha256: f651edae3b151cb3d6674b2d6acefd08fdf2ff834d6209db885bdbfdd689a5de
    role: context
  - path: pages/traits/genomics/brig1_system.html
    sha256: 462063a7a1cdd42e848ff9a2d9e764dae77ab20ec15ed3dc73743ad0ec4a9033
    role: context
  - path: pages/traits/genomics/brigantia_system.html
    sha256: a8f622e38a21fd5b9d4b03102abc2179e9754dfb0ef5e372d07df3e65b3e5fb5
    role: context
  - path: pages/traits/genomics/bsta_system.html
    sha256: 2399d8500cb7aee26f16a1c1d76585071fd0f5efd7e494420aeebe80753efa28
    role: context
  - path: pages/traits/genomics/bunzi_system.html
    sha256: e0281e37b854fc721f5e356ade25872247b037e291e91cabeb7d0b2c0fad7bdd
    role: context
  - path: pages/traits/genomics/butters_gp30_gp31_system.html
    sha256: 110061a348e7f07e3488b7f412e6e04f43662d4b86346e81252b1f8dd7f1e78b
    role: context
  - path: pages/traits/genomics/butters_gp57r_system.html
    sha256: 80f1b6bbfaa1be1739cecc43be8f3029ec761fef09f14a13e6ff2bc358d9b27c
    role: context
  - path: pages/traits/genomics/caprel_system.html
    sha256: b84ad4022455fb7a6ca10e7721cd5e64a5c62c8156e9725c480427aaceb45e63
    role: context
  - path: pages/traits/genomics/card_nlr_endonuclease_system.html
    sha256: 3c42ff4f4f14f5a1b71b385a5366dbf8c5de406a093aa94bfa97c9e135894be3
    role: context
  - path: pages/traits/genomics/card_nlr_gasdermin_system.html
    sha256: 2e7754aca531fd010097b4c7947a8021c7748f05bfaa3517a3caf7a1b21206c4
    role: context
  - path: pages/traits/genomics/card_nlr_like_system.html
    sha256: d33bb7ae0b168b8ed03e2fb1e864ac66c5e688dfd3bfee3b5de1d133c49246ea
    role: context
  - path: pages/traits/genomics/card_nlr_phospho_system.html
    sha256: f8adb36059db4661eb2caafad53140a48515e3c6b108f6bffb59dcba35d2f322
    role: context
  - path: pages/traits/genomics/card_nlr_subtilase_system.html
    sha256: fe2b91adbca07e658fcdc2facc0da9d54895f0391759402bc4d13c7677635e99
    role: context
  - path: pages/traits/genomics/card_nlr_system.html
    sha256: a6ad42ad478fc974608b97247505f94fb6b45d1d456a8ceabc0b5dc213e257c1
    role: context
  - path: pages/traits/genomics/cbass_system.html
    sha256: 237c6b34c7ef750bee753f15c638423afb69bf1e94d4c812a31184303c74366c
    role: context
  - path: pages/traits/genomics/ceres_system.html
    sha256: fad4bb5e6a9e2b5833390d2c515de0e4724ba72e40b3cc02b8d2eada3651e917
    role: context
  - path: pages/traits/genomics/cernunnos_system.html
    sha256: ce3af2c89e8694c78a64cf70b3804affdb18ab902b0580aa11228e066fbc76d7
    role: context
  - path: pages/traits/genomics/charlie_gp32_system.html
    sha256: 7724aa28dc53a09b9bbd923909d69187bfd565ec306276a27946996b8198218d
    role: context
  - path: pages/traits/genomics/clover_system.html
    sha256: 575be1741aad16f70992761098d980b989bb6b70b143b20f1ad687b6a37a1e7c
    role: context
  - path: pages/traits/genomics/cmdtac_system.html
    sha256: 295c23a8d6dedf4fb8acc0c1ad2179e1eb96dcb519f8606fbbdadd3bb4ccb7c2
    role: context
  - path: pages/traits/genomics/coconut_system.html
    sha256: c1afdc134c0f31d76f040b6286243091b88fa246e5065642585b102f36334e3e
    role: context
  - path: pages/traits/genomics/codon_usage_bias.html
    sha256: 261bfda676b9af38238ca3d030db7325aaa59daed0ef9a989bea7cc681d0a2c7
    role: context
  - path: pages/traits/genomics/crispr_cas_system.html
    sha256: e8650a3b3ae29fe36e754da79df000c4abb1cd8cb64117aa0fb7cf8d9523d11e
    role: context
  - path: pages/traits/genomics/crouga_system.html
    sha256: d9f9bf4e669dd66596254e8f3838e054ac5e0e02881fc930a02ea04faf0d3e0e
    role: context
  - path: pages/traits/genomics/dag_system.html
    sha256: 4675aa242cb5134dcaed88d663000370d1e38149ec3b983f9b0602b697bd9b32
    role: context
  - path: pages/traits/genomics/damona_system.html
    sha256: a02fd5690d80058a04d2380dcaee5357d20ba2cd8c1e89a8106f6ba034e12a7e
    role: context
  - path: pages/traits/genomics/darna_system.html
    sha256: 5637b6c7aa0853b632739b219330a251e2c4ff9c229dfa44e313c2b7677fd0f4
    role: context
  - path: pages/traits/genomics/dartg_system.html
    sha256: 528f117a168f1bfdc3540dbb16778d8d0e978814510d3cf81e1ace8b61102567
    role: context
  - path: pages/traits/genomics/dazbog_system.html
    sha256: 13389aeac4be164baeb56e4e8621f00433470c4aa8b00113c1ef4f704038a480
    role: context
  - path: pages/traits/genomics/dctpdeaminase_system.html
    sha256: d05ae7b721d840f9a2610e05918ecb3186671f705f3c87a2e30c0c3d1791527b
    role: context
  - path: pages/traits/genomics/ddmde_system.html
    sha256: 97266c1ba251505a5ca8c15bb07b34bc6ef57ae1442c2111a12d399e240b1cad
    role: context
  - path: pages/traits/genomics/detocs_system.html
    sha256: 190e0ea0460837885ae680fdc95899f6e67a3ac16bd051e6e3b0706fd2f232de
    role: context
  - path: pages/traits/genomics/dgtpase_system.html
    sha256: 65a62a5b01c0eb623663375e4e4a1bc62a79c4b484d94ee2b494903929b6b709
    role: context
  - path: pages/traits/genomics/dionysus_system.html
    sha256: 5cd2f118d3eb8fed862f1c92b094065a9092e0bf3a79a6a49d5396124ab7cace
    role: context
  - path: pages/traits/genomics/disarm1_system.html
    sha256: 069bdec13cd58475f00aa191b1395ea6bbcd8ebd1d081da931b720d6f485b6f2
    role: context
  - path: pages/traits/genomics/disarm2_system.html
    sha256: a13b36bbf699d5fd58b4070119b49086f79d0401e67f04efe79f822c91fabbc3
    role: context
  - path: pages/traits/genomics/disarm_system.html
    sha256: 553561259b97b383e473a9c7babd3d304b13e0867be0c642a842a45527c6cebd
    role: context
  - path: pages/traits/genomics/divona_system.html
    sha256: 329db93690c20eaa90983b3ad068276c998e327ef0dae3ac0c18396db88ac557
    role: context
  - path: pages/traits/genomics/dnd_system.html
    sha256: a088547db31ca26060fa35de074864a5e817a8bca38386b00fda0c80ca518c91
    role: context
  - path: pages/traits/genomics/dndcdea_pbeabcd_system.html
    sha256: a791534407ff9dcc45ffdef4594935c2cb7b4775b30e2583a0ca681fcec93366
    role: context
  - path: pages/traits/genomics/dodola_system.html
    sha256: 254e3fe9b9e8f6ee521007027e24189390286c1f0b67cb4b23929b4e27f97ac5
    role: context
  - path: pages/traits/genomics/dpd_system.html
    sha256: f14ee0e6b23eddaf7f3b92e7e3d996d9a075d185af010c0ce62a7db0d9b42e0f
    role: context
  - path: pages/traits/genomics/drt1_system.html
    sha256: c91e064ddb5e221242ca8693419c9249b2d3b7b968a0ead2525ef1640d64ebd1
    role: context
  - path: pages/traits/genomics/drt2_system.html
    sha256: 3d14c982add51c76d69766efbe5855dec8fb93f1edb2442c4a1b100dcdab822b
    role: context
  - path: pages/traits/genomics/drt3_system.html
    sha256: a99f1d2dab606a797f504a9215b1c3c773689f8c19422f1ec66157d4f0e543db
    role: context
  - path: pages/traits/genomics/drt4_system.html
    sha256: 4023b930d17ae5dab545217e9808ea02032961c5de479efbc46129f35725e521
    role: context
  - path: pages/traits/genomics/drt5_system.html
    sha256: 8fc03ab4e38ee36398ee2b8f7aa6820e4b6bad551c227c78d18aa16a1fa52448
    role: context
  - path: pages/traits/genomics/drt6_system.html
    sha256: e4451e99e0e652588b6b215efbc5618101ab049c81cf20e2b3067fa7874ed85b
    role: context
  - path: pages/traits/genomics/drt7_system.html
    sha256: e1101c31c15e1e0a24534e45815ec4a1aeeb155541088c4ace3c119a137f9663
    role: context
  - path: pages/traits/genomics/drt8_system.html
    sha256: c34de6f590606886502b59b3d5e20444c4170b8c9e20e83a943058185abaf423
    role: context
  - path: pages/traits/genomics/drt9_system.html
    sha256: 154107565e56ee53041102f477db9efa48ce91311800edd64dadf0b05209c5b4
    role: context
  - path: pages/traits/genomics/drt_system.html
    sha256: 214dc8193faea3b0d43140c4219cf0e0864ee9a7e11b50f384e6398c8cb7d37f
    role: context
  - path: pages/traits/genomics/druantia_iii_system.html
    sha256: 85460064ec16a96a2ec111953857e46a5ec978c4ede9c6c71b69c543aeec3988
    role: context
  - path: pages/traits/genomics/druantia_system.html
    sha256: 114e69035fc862ce6d1a11b527d3297155ea370e2ad08a9f963384df25c3834a
    role: context
  - path: pages/traits/genomics/druantia_type_i_system.html
    sha256: 06ecc2ffeb2b11cdaf965e1831017b7ccfb9ab2cfd33e58b2ea19106ec62e642
    role: context
  - path: pages/traits/genomics/druantia_type_ii_system.html
    sha256: 0905328a2ad9faee9e8e09974ec05ff1c17c269a7ff5f27c409a3ccf61652258
    role: context
  - path: pages/traits/genomics/druantia_type_iv_system.html
    sha256: 50c74d35d0efa8196a516b045b9f6f6c6cfddb26c02dcc6622fca9f76b496725
    role: context
  - path: pages/traits/genomics/ds_10_system.html
    sha256: 159dfdab67e1d1a3a92294ef36515697d93134a07dcaa54054eee36aa21f9282
    role: context
  - path: pages/traits/genomics/ds_11_system.html
    sha256: bb572f6638c6900958aa037f25d07242aa9ee991fab0bffc1bcfc1c775408e19
    role: context
  - path: pages/traits/genomics/ds_12_system.html
    sha256: 557831606fa85ec6d4614af6f2a519413a31c9b24ff08efc1e9ce30983ea30a2
    role: context
  - path: pages/traits/genomics/ds_13_system.html
    sha256: ed9a04ee35cddc2e2e557bc8986ade7e5e5ddac68e8b532bcbd5308833e585f7
    role: context
  - path: pages/traits/genomics/ds_14_system.html
    sha256: 67f9a318388bb88f8caca64a8b1628de223895866f30b9b5be56526c32e24e2b
    role: context
  - path: pages/traits/genomics/ds_15_system.html
    sha256: 007d94b98256758443ceae30197f20a286d73b9371c0b683c28507083a1b1661
    role: context
  - path: pages/traits/genomics/ds_16_system.html
    sha256: c98cfa4c7ee8f4b04cb1dc4333742d36a6ad33ee591191cfea9b3482827a9e8d
    role: context
  - path: pages/traits/genomics/ds_17_system.html
    sha256: 7b26571a8100cf916c7ffb9a52abeed60da489adc874db1df661f2225d6a564c
    role: context
  - path: pages/traits/genomics/ds_18_system.html
    sha256: 16aabb70fdec65559fcbf9806ff5825201157e5d2759ee078635d9616a18f568
    role: context
  - path: pages/traits/genomics/ds_19_system.html
    sha256: edb0352f8878fa17fb591ab5e76cc710caea5d8642d31c478b2931d8322d9059
    role: context
  - path: pages/traits/genomics/ds_1_system.html
    sha256: 896d7a72baa88391cb293d47bdb5579cf2bb06264e78b4b871ccd906ce35595a
    role: context
  - path: pages/traits/genomics/ds_20_system.html
    sha256: 7647d548d052095db65c7fc3432e7e97b41d1a9dcb86a9ecc8d81d8020fd1e41
    role: context
  - path: pages/traits/genomics/ds_21_system.html
    sha256: c2a89dbfb79303fbf311c1556dc4c11360f959c5f0a450cd4bd443e59dabaf16
    role: context
  - path: pages/traits/genomics/ds_22_system.html
    sha256: 7934d2dce68536c26a61bb3a37544521e4170c56fe5196f155d3f7bd5848686e
    role: context
  - path: pages/traits/genomics/ds_23_system.html
    sha256: 77f7cc387460c69759d1a8f62acb3d555705de5d68f301ab391e997dcef38392
    role: context
  - path: pages/traits/genomics/ds_24_system.html
    sha256: 3ceaf0e094d03b1e0d04b14a16849c909a48607f23e9acd360efbc5d592ef1ca
    role: context
  - path: pages/traits/genomics/ds_25_system.html
    sha256: d3c96c33188810905e2db54d8bd0ed466e4db035bca0c1589cf7fdc9f0f9a41a
    role: context
  - path: pages/traits/genomics/ds_26_system.html
    sha256: eee77bd5dcdc38b45fb468c8bc0c8187efa2c163ee515b157e15c185d995695b
    role: context
  - path: pages/traits/genomics/ds_27_system.html
    sha256: b18afaea42674fcb4d2352471c21b767ab2a1602ab562c25a4ae8adbefc048ba
    role: context
  - path: pages/traits/genomics/ds_28_system.html
    sha256: f35b2763f14448a16e498fd48d5621d575c332dfca3c1723cbe1d091ae54e3fe
    role: context
  - path: pages/traits/genomics/ds_29_system.html
    sha256: 89ee24723e1e0a0a93d209f479d3d07d5ea54ca4ef76d4fb6cf331aa0dc2d742
    role: context
  - path: pages/traits/genomics/ds_2_system.html
    sha256: 952f0e64717c5f5bfe2f7b573a7e48d56b2eac658e78168ea17254a2b4c6aafb
    role: context
  - path: pages/traits/genomics/ds_30_system.html
    sha256: 2c17f676a172c4d913be8fc503cc133a800986a1079796aaf763c3fc90fdb3cc
    role: context
  - path: pages/traits/genomics/ds_31_system.html
    sha256: 2453995f8bd6cfc51d120a02f7e673b90680fe339a662b9620e4c5d912138828
    role: context
  - path: pages/traits/genomics/ds_32_system.html
    sha256: 7ccb1ca9af965d8100b561d5eb5220cef4927f47f9573220254210da5a32461c
    role: context
  - path: pages/traits/genomics/ds_33_system.html
    sha256: 6ea9251244b8d655240ffd8a495bf3b4a968eca9e100d9dd424d2a6040d1835e
    role: context
  - path: pages/traits/genomics/ds_34_system.html
    sha256: cc1688916f59a2a44fd122b064216eea651616f8150ea18db9493c5801794c36
    role: context
  - path: pages/traits/genomics/ds_35_system.html
    sha256: a6455c94cda60afc67eefb03b7a4983d945ba935ad825f84aeddcb5491d77e55
    role: context
  - path: pages/traits/genomics/ds_36_system.html
    sha256: fadd3182c664273d52c8467c2c7eafd17b683802fad6b3cff30dae72ebc6f1a1
    role: context
  - path: pages/traits/genomics/ds_37_system.html
    sha256: c05ccd67c2ca945f9ee4609e05bc8bb3c32b51e1ffeb2b3a171ce3888d5161d1
    role: context
  - path: pages/traits/genomics/ds_38_system.html
    sha256: 14542c953382c5cef35a98d55758e936ccd225c0d73ef78755dc8d7dae11c773
    role: context
  - path: pages/traits/genomics/ds_39_system.html
    sha256: b037df3c795f0005272ce92346155561335d7aefeb4c1fdfe97c1277c01faf85
    role: context
  - path: pages/traits/genomics/ds_3_system.html
    sha256: 99033219e0d897d3df201e1ac5a7706c171001fbd2a512d52c6c462019e08547
    role: context
  - path: pages/traits/genomics/ds_40_system.html
    sha256: 1c079946e4cfb5c618b83ec4f729481bc9ebd60b2c3ad09f7baae2a74c8ebd65
    role: context
  - path: pages/traits/genomics/ds_41_system.html
    sha256: e8c2f28b9162dac4b07d2f8e5965460110dea57d30c02f70d9bc88b95f91a74d
    role: context
  - path: pages/traits/genomics/ds_42_system.html
    sha256: 9f4a2fd9ac81865284c396237510bd471cccf4768542c33fda753463fccdfb62
    role: context
  - path: pages/traits/genomics/ds_43_system.html
    sha256: b1a55137fc477da9535b740f1d9504754e11c4ddfe3c87e9e33e4ae6f53d3c23
    role: context
  - path: pages/traits/genomics/ds_44_system.html
    sha256: e17b4553f6da5db85cc0e600b0f3dfb204b9ceda3deaeb97bc4b4d1d93b64e60
    role: context
  - path: pages/traits/genomics/ds_45_system.html
    sha256: 9e02dfa3f279062a5c457462eaa96c41b709b78e58f2a9b3efa97ca7bca9fc1e
    role: context
  - path: pages/traits/genomics/ds_46_system.html
    sha256: 73f5ebf5e32f912a8c93516b619b247258c31c4b33d6f2e9a463b49f0dc4cac3
    role: context
  - path: pages/traits/genomics/ds_4_system.html
    sha256: af8b43e30f7859ce0d3a4cff4bbf6d60ae5d71a034452a1994c85ed34969be14
    role: context
  - path: pages/traits/genomics/ds_5_system.html
    sha256: 63fe2a8469be1c150aec0dc6d5d8956bbd4f2877968feab5ebda71b08aebc7a1
    role: context
  - path: pages/traits/genomics/ds_6_system.html
    sha256: 0ba1194eb9a90393088d57b2dca02b4e2e1617a9ba311fb5b56014442d44d823
    role: context
  - path: pages/traits/genomics/ds_7_system.html
    sha256: 427a3f32815d1e69f41caa6dfe5262a0d28ced2848e58966ccd96e36f7969131
    role: context
  - path: pages/traits/genomics/ds_8_system.html
    sha256: 3d1162c3832d65259d9b16ca4a3b27e1b1bafea55fb5ea932a2d1e7b86aed0a6
    role: context
  - path: pages/traits/genomics/ds_9_system.html
    sha256: 2c19c1ef5baf85547ff418a90f4e0b0a142f56bcc5feba820af13e08b6fd2098
    role: context
  - path: pages/traits/genomics/dsr_system.html
    sha256: 0e24c6827803f2fab40f724315bba0b12eb8e38232a21a3751eafb801e5a287f
    role: context
  - path: pages/traits/genomics/duf262_schlafen_system.html
    sha256: 33082e103b7e899857e960db62665753e546b32f276ac1a4414216423f24ce43
    role: context
  - path: pages/traits/genomics/ecokmcra_system.html
    sha256: 76be9a260c0c949962b8879c5d458d3cfd29eefecc68f2b8ff0f87e47048ad2f
    role: context
  - path: pages/traits/genomics/eleos_system.html
    sha256: 1793783590a2002ce6f2974388c0e20c99e142b7900044714dea78f8a1b34201
    role: context
  - path: pages/traits/genomics/endpacf1_system.html
    sha256: aee2ffc0e986958a1d24b970856b0a5aa68288ccfbed1e2b79f0613cf6089071
    role: context
  - path: pages/traits/genomics/epona_system.html
    sha256: 7813980871dfb8fffe6f509b7a4390c116d483e039e323792ebb0aabdc72683d
    role: context
  - path: pages/traits/genomics/erebus_system.html
    sha256: 1e3ae869885e0134ad5690e02ed763aa8831dfea5e6196246455f62c0924b713
    role: context
  - path: pages/traits/genomics/esos_system.html
    sha256: f0d5c8f6959bff5eb5bb88b8ce9ddff7ffdc422e88299db895e439d931c2030f
    role: context
  - path: pages/traits/genomics/fliodhais_system.html
    sha256: ab79d2e7694b8f54e2fc0b6f5794008057503ebaeb49b49fdfd7d1307a4de374
    role: context
  - path: pages/traits/genomics/fs_giy_yig_system.html
    sha256: d76fd21af68ff1e5e7dc71ffb0f5c01491807a028b7147d981317c9bb5bbbbb4
    role: context
  - path: pages/traits/genomics/fs_hepn_tm_system.html
    sha256: cea0b063847f30cc22e48da0e3f6e5c5c484df4223d8c61d5fd0d94036ab6779
    role: context
  - path: pages/traits/genomics/fs_hp_sdh_sah_system.html
    sha256: 8453ad26c59ec3056d2e9c962dfedc64b22271cad2a21fa0af1df4a421eba5bd
    role: context
  - path: pages/traits/genomics/fs_hp_system.html
    sha256: b5b7e5633b02f38587e08a174dcc4981f707e92873821886e2b6f5ae2083e59d
    role: context
  - path: pages/traits/genomics/fs_hsdr_like_system.html
    sha256: fe5ade7c8b4aea6014306a0db4e26b9e6ad81f4359e1d2b8294fb7f89c47ef66
    role: context
  - path: pages/traits/genomics/fs_sma_system.html
    sha256: d386e56db17c7b8aa2e66bfa593658b058f0e8be2da1b29644808fb9f11a0775
    role: context
  - path: pages/traits/genomics/gabija_system.html
    sha256: 5b71ba6a85573466314b864491810576825e9f49f8e5ff009ecb1bf26506323a
    role: context
  - path: pages/traits/genomics/gao_ape_system.html
    sha256: 59bc25e6c11771809af331c1a5f379ba24452c9ea658a4c40d16a024cdc2bd6a
    role: context
  - path: pages/traits/genomics/gao_her_duf_system.html
    sha256: 481ec777613ec77e645886c11aeb1c08db860f3d685af8cebf66cdc4d1a67afa
    role: context
  - path: pages/traits/genomics/gao_her_sir_system.html
    sha256: 655e032a409b34275c47838a3e5d2cbdf0f0b5750ad7f1d9a32b0fb5accb267f
    role: context
  - path: pages/traits/genomics/gao_her_system.html
    sha256: 6359a920c500715e2ecc39e44a9960c2d038ca5d305617794699a0d4e3e11cff
    role: context
  - path: pages/traits/genomics/gao_hhe_system.html
    sha256: 688a4515cf0cdd9c2781e0b2a41a8631b2e819ac475d92d95ed8bf24ca11655b
    role: context
  - path: pages/traits/genomics/gao_iet_system.html
    sha256: 43f76edc376d1e4f417a2687e4081d1fcc1aded92be53f1e1d556cbe2cad039f
    role: context
  - path: pages/traits/genomics/gao_mza_system.html
    sha256: faf5ef4ef1bc435baf4f7604c006d0c8a7f23a3f8c5230df69e6990f2ce32d9a
    role: context
  - path: pages/traits/genomics/gao_ppl_system.html
    sha256: 482ed4219119fb69a274bc92fa99b2d8378447b8878b2f8d9ff4cc45634a839a
    role: context
  - path: pages/traits/genomics/gao_qat_system.html
    sha256: c060d3563803e5065565edbe78d877148064eb0c039a67c2bc576077770103c2
    role: context
  - path: pages/traits/genomics/gao_rl_system.html
    sha256: c01eb89e898a25c0f0367ce1592de40473cd3ed05fd807d6105146a1e8efcd5d
    role: context
  - path: pages/traits/genomics/gao_tery_system.html
    sha256: 4997a4de8d5cccdd823dd0942985de3dcefdef5ddffb3b02612278f57173b4c0
    role: context
  - path: pages/traits/genomics/gao_tmn_system.html
    sha256: 39069736b221794b6ea8b9f8b43bde6cfc503ebaaaa07bd9dd599aaf88336a82
    role: context
  - path: pages/traits/genomics/gao_upx_system.html
    sha256: da8be1656be284fc22174d2c6cf9fd0607ea567377f6e39d79e092014ef08b6a
    role: context
  - path: pages/traits/genomics/gaps1_system.html
    sha256: d0ae6069bd31b2f77e3bbe60d95f5fda4523e5e6d953fdd09c04de80c4d2053e
    role: context
  - path: pages/traits/genomics/gaps2_system.html
    sha256: c7d4476abe44fe341489daea985bf839c7e53796c5e64877ca63bc0f4379c2b0
    role: context
  - path: pages/traits/genomics/gaps4_system.html
    sha256: 526d13802c2cfdf7fa8addcc7d623d21b2937a029a8303dc03edf113e96128bd
    role: context
  - path: pages/traits/genomics/gaps6_system.html
    sha256: a99cb35729a64d307a4d78b5fd58f2454d9442c7c235bcb29e9923779bb3e85b
    role: context
  - path: pages/traits/genomics/gasdermin_system.html
    sha256: 68adb111d61c5e6e148d7f34984973416eecb0947c80fae01b0971c7454dcd69
    role: context
  - path: pages/traits/genomics/gc_content.html
    sha256: e0ffb2b3ac5f512ca81bd4e9c203989159bc69c6098ce396194bc4175794e6c3
    role: context
  - path: pages/traits/genomics/gc_high.html
    sha256: c01807ae19d1b9828a88697572a0a8844fbaf43f160db11cdfc2d82b04334147
    role: context
  - path: pages/traits/genomics/gc_low.html
    sha256: 980edf1e140471cc0bd3d6cae03f08924f26a4427b107425cba3d690a40c5cf9
    role: context
  - path: pages/traits/genomics/gc_mid1.html
    sha256: eb35b6a7a3eb8d207e66ac2b6e858f1566dc18a758416ab194b9c39474d99678
    role: context
  - path: pages/traits/genomics/gc_mid2.html
    sha256: 03a117055e62a9c609376dde369f383cfa38a2f1bb3be98272c6f1c1b61b1579
    role: context
  - path: pages/traits/genomics/gc_skew.html
    sha256: 2a112792afbcf3fef6177a0fc94b1251983e041226430dbd9046c141a8e81fc5
    role: context
  - path: pages/traits/genomics/geb_system.html
    sha256: ff65389fd8fb71358b8ca4c3c160640c0f8e2d918c95b173ae40cbfbd1891d4a
    role: context
  - path: pages/traits/genomics/genome_size.html
    sha256: 3f5340e1582e8b9e0df70325f02d4b23d64b28abbd806e99b7f0a29bf37f9f09
    role: context
  - path: pages/traits/genomics/genome_streamlining.html
    sha256: e236a4c473bfe381d99d95afe32a462500a22c637a8d096d237b700c9f7314bb
    role: context
  - path: pages/traits/genomics/genomic_island.html
    sha256: 2c7022e048cafe8c9eb1ca45f71f6c098bda3d6e4016227847f2d24b660913e7
    role: context
  - path: pages/traits/genomics/gmrsd_system.html
    sha256: 7d92c684a2088f285a33ed75d0a4702cd3d8607ee559f203c16f8d1844123326
    role: context
  - path: pages/traits/genomics/hachiman_system.html
    sha256: 51da4cc615e6571edda0e6778e4d12f2f3b5fa886fb87afe7d9248cca5d279bc
    role: context
  - path: pages/traits/genomics/hachiman_type_i_system.html
    sha256: 32c9d8288fc09f6e8db75e0c4b0cbf073eb3aa472c7b55dc9504b09288b006eb
    role: context
  - path: pages/traits/genomics/hachiman_type_ii_system.html
    sha256: 5b660a81aae3cbd58950ead1328a44aa770e33a42d3d380e577723a74d80af32
    role: context
  - path: pages/traits/genomics/hailong_system.html
    sha256: a6fda01b2aaf76da71b7635a219eb0c30f9aea07a49236327f70adc02d08d954
    role: context
  - path: pages/traits/genomics/hec_02_system.html
    sha256: 1eb8c4e20032c72fb5d566c6fc2da11c41c654b82b09da2df9df813f3653562a
    role: context
  - path: pages/traits/genomics/hec_03_system.html
    sha256: 63bbf3152d73ae5d7794ae59ef0acf8100414c58c211b3b3fbf81b39d234095d
    role: context
  - path: pages/traits/genomics/hec_04_system.html
    sha256: 90b43c2b901bf2bed95ec3433c5c5c46eeaeac5bb41b85e70ee79dba0ffa3fbe
    role: context
  - path: pages/traits/genomics/hec_05_system.html
    sha256: f681670c8aea3274e74e1aa7b6115bdf986ddc166ca9209c5d9e8372b7cc380a
    role: context
  - path: pages/traits/genomics/hec_06_system.html
    sha256: 55929a86ad82f8f275abe991cbc473ad34b47bd50277b8ceba5ccba7a2571b94
    role: context
  - path: pages/traits/genomics/hec_07_system.html
    sha256: fd2d7d991682e72b713cb59c84ae86af512ef530cc68346e526ddf76c98b185f
    role: context
  - path: pages/traits/genomics/hec_08_system.html
    sha256: 43b316284b347c255bb08b7101a04ac11746672dff489be63723fa04d4106b29
    role: context
  - path: pages/traits/genomics/hesat_system.html
    sha256: 8d178fd4845dbbb86a2e114cfbb5c093c12e93121580094cc10d45805110d25d
    role: context
  - path: pages/traits/genomics/heterokaryosis.html
    sha256: adbe34c7ad519e58ccde8f49986b5d5034077d6de24235937967cb3b4305b47c
    role: context
  - path: pages/traits/genomics/hma_system.html
    sha256: c2e693feca235e919e0f6b15ab6c5f5ec6072c66aedf7002b847c31435554f38
    role: context
  - path: pages/traits/genomics/hna_system.html
    sha256: d4d2c7b647f20689d1436370f4b521cbcf52ce066ade251fcc3008342fb9abfb
    role: context
  - path: pages/traits/genomics/hypnos_system.html
    sha256: 61eea381ba8f8d9c3d5269e4edd2b2db2bacf5b94ba6e5c632797e2733ad8166
    role: context
  - path: pages/traits/genomics/ig_like_schlafen_system.html
    sha256: 5be9dc7e38dd9793d638641fa0e5bf101f8dd57b080c7a4dd0fcb79809000bdd
    role: context
  - path: pages/traits/genomics/integrative_conjugative_element.html
    sha256: 62350f372fb1996a28aff1278bd30aee807fe47977b4b92f1eb9869852ba5173
    role: context
  - path: pages/traits/genomics/jukab_system.html
    sha256: d2c18cb07c75ae9710d4f8c777c5005d38bc66e5d9f07dc3c17576cdf1991713
    role: context
  - path: pages/traits/genomics/kamadhenu_system.html
    sha256: c19e7c3c582802fde9f506627ac47fe79f4722625e0127ef46778ff272475fcb
    role: context
  - path: pages/traits/genomics/kiwa_system.html
    sha256: 05a1e4567c7ffb88f77b92f18a4e4a4b9f9dbee137f99a00cf98a722aa581bed
    role: context
  - path: pages/traits/genomics/kongming_system.html
    sha256: 090a2bd1266cdfcf47fca3c0bc2dc80877c976ebf36c40acb3ae8f3a14b3f4f0
    role: context
  - path: pages/traits/genomics/lamassu_amidase_system.html
    sha256: 9f7757faeb6bbf37325335799f70db6feec05e811f8111a7d1221290be74fda2
    role: context
  - path: pages/traits/genomics/lamassu_cap4_nuclease_system.html
    sha256: c774706f6e4be06a9a5ab93a8a2cc5cec22ac88ba1319c14692e6d18bfd136c9
    role: context
  - path: pages/traits/genomics/lamassu_fmo_system.html
    sha256: dce00f52911712528ed5fe5dafb6fdf17602f4052d2cee3cd563e5a911e367a2
    role: context
  - path: pages/traits/genomics/lamassu_hnh_system.html
    sha256: 4c94753e1af11ad91a31c9d1c5410d506350fd391948d6733456705e3d598278
    role: context
  - path: pages/traits/genomics/lamassu_hydrolase_protease_system.html
    sha256: a36728dd2b825bfd4d33e85fb852c9b9070dcbce0830b869ab9ccb0a0b189335
    role: context
  - path: pages/traits/genomics/lamassu_hydrolase_system.html
    sha256: 0ca9dcbb4952400a05baa277e02a61592cccacfea717cef536a8e6930cbacf74
    role: context
  - path: pages/traits/genomics/lamassu_lipase_system.html
    sha256: 53d462c9097f073f506d301943c6c6964bf6b6ddc62dde2781a44ce999b6a0d3
    role: context
  - path: pages/traits/genomics/lamassu_mrr_system.html
    sha256: d958aa8b98240abe59dc52040437cd7ec08f00539f61cdcf36bf7777f9b81f63
    role: context
  - path: pages/traits/genomics/lamassu_pddexk_system.html
    sha256: 5910ce92ac23ad646ab05b89b63be5bc702e3df0bb6c97c9fa391198633ec210
    role: context
  - path: pages/traits/genomics/lamassu_protease_system.html
    sha256: 6bb021bb539a4f0d25337340fe362a75d6179f192c9d41eb2e7b3ea8fb738018
    role: context
  - path: pages/traits/genomics/lamassu_sir2_system.html
    sha256: 25ac6d1f5f46c8d4a8e22618f5467bf0c1751546aa6fd38de82ff04a26f7332f
    role: context
  - path: pages/traits/genomics/lamassu_smek_system.html
    sha256: 312818bffa4f7e194ba0b46ec0b08616b3841a274291b9309fb3febd8b66ca94
    role: context
  - path: pages/traits/genomics/lamassu_system.html
    sha256: 916166cd9a619b4669c303bdd8e085500af69a8523c78c29ce93749d1d26f022
    role: context
  - path: pages/traits/genomics/lamassu_type_i_system.html
    sha256: fd39ba6e6214b2403d2ec0da6334ccb0d7d84161f6357be383717753b7c79b97
    role: context
  - path: pages/traits/genomics/lamassu_type_ii_system.html
    sha256: d5417b4dc467cedf93d678991745971eaff26ad36cc73a83dadb6f5c00a3d6b4
    role: context
  - path: pages/traits/genomics/lanthivirin_system.html
    sha256: 86d9697cbdf653f7c44bcc56b6fb19dfb9f1397c1331f675c22e1eee7e656392
    role: context
  - path: pages/traits/genomics/lit_system.html
    sha256: e09b0adfb6343a167af017cb1ae773f923bee9710c2922b7cb821c03ea876337
    role: context
  - path: pages/traits/genomics/long_lamassu_system.html
    sha256: acbd4fb387d616a5bbfbb9c2b26ae381e2b49bba5cf4d7885a43b369e829492f
    role: context
  - path: pages/traits/genomics/lugos_system.html
    sha256: 4c1b879d92345e06ba36312ce1f9747c4bb1d5d634af9ead80c5732dea8411cd
    role: context
  - path: pages/traits/genomics/mads_system.html
    sha256: 3e075d06c29b665829e7b26aadc4a4b33755fa9f1f2b9b04d30ce31646d5c2a0
    role: context
  - path: pages/traits/genomics/mazef_system.html
    sha256: 86e12fa7862d507a7f37da0f31a4c179bddbf5a4d73a70ef2f562b3a997dd84f
    role: context
  - path: pages/traits/genomics/mcrbc_system.html
    sha256: 421bb31884ad8e6071feb16687b269c6ddfe640493a8c826846fcbd040636411
    role: context
  - path: pages/traits/genomics/menshen_system.html
    sha256: f690fdd3f3ee869debf8f3ad77778ce942da8128c061469aabd32cd94592c3b5
    role: context
  - path: pages/traits/genomics/metis_system.html
    sha256: fc9727224a3463099663a8cfb6a5dbd5c5c4a6033b8ccc9a37593e05ce74c71c
    role: context
  - path: pages/traits/genomics/mksbefg_system.html
    sha256: baa013d3fad940ca906c0847a414765cc51a1e21eeae01f0b87fcfd9526dee15
    role: context
  - path: pages/traits/genomics/mmb_gp29_gp30_system.html
    sha256: 013b17d69365d1f43849e20ff984338e362eae0e3521115c060a08cdbf15b548
    role: context
  - path: pages/traits/genomics/mobile_genetic_element.html
    sha256: feeb50626e4379eb9586d933648455eec7aa1c7d164db227fb9a83c6fb9716ec
    role: context
  - path: pages/traits/genomics/mok_hok_sok_system.html
    sha256: a3b87acea70d332ddf11c8ba51b97a121a2b225ccc766b5cd36e5a30f2ab780b
    role: context
  - path: pages/traits/genomics/mokosh_system.html
    sha256: 1d20dec531696a5552d3de8e95d4a94972261128d6cf7fa81a6c2495694c8fa2
    role: context
  - path: pages/traits/genomics/mqsrac_system.html
    sha256: 23a4b5c0f39ce17556e1d2b0c25fe69e8891bff437bcfbf85fdd41ef685c82dd
    role: context
  - path: pages/traits/genomics/mspji_system.html
    sha256: e5925cfe91ae997a55f9e0c73ed89c44f37e8bdfed13086b1f5a5175f3ca7fec
    role: context
  - path: pages/traits/genomics/nantosuelta_system.html
    sha256: 6b9b87dbdd77c3967a4caeb7da13593bd6283e8e19ce3134873fbe0ce561071c
    role: context
  - path: pages/traits/genomics/nemetona_system.html
    sha256: 7c244fbca042b78f01e4e64daba18ff5f82990ebcf31caf75e72df60dcedee58
    role: context
  - path: pages/traits/genomics/nhi_system.html
    sha256: 58d88f3ec78a674a61c78a6dd9ed721d3ffcfd9d1adbabcda331c36051159911
    role: context
  - path: pages/traits/genomics/nixi_system.html
    sha256: 1abfc446d73e997676c811896197f4bc2c76fa459b55b8ee4b354ef384dc2e08
    role: context
  - path: pages/traits/genomics/nlr_like_bnacht_system.html
    sha256: d29d8383d83a80ce1ea492fd0a57f03bbeeb9c21505cd36e022424cbf2a6cc94
    role: context
  - path: pages/traits/genomics/ogmios_system.html
    sha256: ef59a08f84c81549d6ff801381ef58baacef7721d2f37089e66f662d02fefacd
    role: context
  - path: pages/traits/genomics/old_exonuclease_system.html
    sha256: 5b4a9201cc4a7088117c5184db11eb4e6ac8987161cc4e509dc92340ed7def7d
    role: context
  - path: pages/traits/genomics/olokun_system.html
    sha256: 7dfef4470ab938d675f6c44334d1dfeb21bdeb32fea714f114712109022c3094
    role: context
  - path: pages/traits/genomics/ophion_system.html
    sha256: 20e0f887bb1c20fd353cb775e73f5796e8ee90804b4fede23c2fde112f75125d
    role: context
  - path: pages/traits/genomics/oshun_system.html
    sha256: 2a48e877432c404f5497f7d6c1118fe5f99219fb1d0d1eb8e305e1aa819bbc93
    role: context
  - path: pages/traits/genomics/pago_system.html
    sha256: c446916c85ff3240ddca7c44c6ba67ae2e4ced32f9c8b8c4d07b608140a7a86b
    role: context
  - path: pages/traits/genomics/panchino_gp28_system.html
    sha256: 08525cf57aca25dc9d0d522a11c03d8b7400c0e33d27e12ffda249c1e0692a9e
    role: context
  - path: pages/traits/genomics/pangenome_openness.html
    sha256: 8bdeebe1f3cad85ea47dfc29ee599b2ea2349280d59be646d3cf73bf7ad886fa
    role: context
  - path: pages/traits/genomics/panoptes_system.html
    sha256: 481c34561371127da4ce687d86cd2310938fcfcc170ff272ac7e4bc31ec20d15
    role: context
  - path: pages/traits/genomics/paris_system.html
    sha256: 7b56d6adfbba6a683e60eba3b8dadfd53b1721bb2cfc75f6da5accd63ea1211a
    role: context
  - path: pages/traits/genomics/pd_lambda_1_system.html
    sha256: b9c2d7c599be377e8af5e4bdb1494d1698388dd7c2205c8414f84937208b67ca
    role: context
  - path: pages/traits/genomics/pd_lambda_2_system.html
    sha256: 912b5deccfb007d6f3e664b09bdf9c197cf718790656b7d21cd5842c4730271e
    role: context
  - path: pages/traits/genomics/pd_lambda_3_system.html
    sha256: b0fc4a9d628229e9fa52cca70ec791298107f2fa391da89f866ae6942b9665b4
    role: context
  - path: pages/traits/genomics/pd_lambda_4_system.html
    sha256: 77d8f285361dfb4097218d7816933062df8502198b09ff5aee6f0253a5333585
    role: context
  - path: pages/traits/genomics/pd_lambda_5_system.html
    sha256: 25e59ca75707aacf9cba589accabb465d4bc01651e100fabfe00d42975049a80
    role: context
  - path: pages/traits/genomics/pd_lambda_6_system.html
    sha256: f80d211e6ae0e2251626d82f6db9d668bcf005b435cf486d3d05463b992f5963
    role: context
  - path: pages/traits/genomics/pd_t2_1_system.html
    sha256: 1367c9d61509ac3cb044f9c29e2aa14095898bcef50cbc69c518523ec8246e21
    role: context
  - path: pages/traits/genomics/pd_t4_10_system.html
    sha256: db1e4c3050eef65530aa5d0829b9582fd957fff77f3a3269102f1d3bfd493b61
    role: context
  - path: pages/traits/genomics/pd_t4_1_system.html
    sha256: f54b77ce2d226a3fb5ab9072d72162a70494da4237f3755316172d979161007e
    role: context
  - path: pages/traits/genomics/pd_t4_2_system.html
    sha256: 8fc36638d34c4f6c5a682155c6e16ad670f6fe0d61bb87fac17e2edd92410dfd
    role: context
  - path: pages/traits/genomics/pd_t4_3_system.html
    sha256: e522656f6a7e6de66bdb2611786f489ae7d675bb22a237f63c29b9e1d90f6145
    role: context
  - path: pages/traits/genomics/pd_t4_4_system.html
    sha256: c2600c5ec0054d592ad854bc82e8e373550aa571751e90530952097a8a9fbfff
    role: context
  - path: pages/traits/genomics/pd_t4_5_system.html
    sha256: fdc7d3e46d844abb3fcae39d0c5452d88829b2da58fb7b44a86581a8ab648d13
    role: context
  - path: pages/traits/genomics/pd_t4_6_system.html
    sha256: ff85b80bf36203ba37efda9aca46b63adadcae2e18c0edf48f3b01573f31c169
    role: context
  - path: pages/traits/genomics/pd_t4_7_system.html
    sha256: aedfc60b6bd361b1ec0bf910e5f51bad2a3753b9b08479494e7db04248af47a3
    role: context
  - path: pages/traits/genomics/pd_t4_8_system.html
    sha256: eda299da5af4bbc0d6945acf3e302b00f46b8685a091297f847c1e0df81460a7
    role: context
  - path: pages/traits/genomics/pd_t7_1_system.html
    sha256: 36cbdf95403a49f56af61ea3c3a108a8cdd7108da48f774bc9f28dbb05fcb228
    role: context
  - path: pages/traits/genomics/pd_t7_2_system.html
    sha256: 735f7c545f4356017af481d202e63434391709d91fd245445bfdef06224d1573
    role: context
  - path: pages/traits/genomics/pd_t7_3_system.html
    sha256: e6d039c36a1b8abdd258260b68a77caf9ffd3162c6823e635f0fae3649a3ce82
    role: context
  - path: pages/traits/genomics/pd_t7_4_system.html
    sha256: cd59d59623a4972308115fb415bb3ae59b57b3ee26747e885dd54eea8e65a3ba
    role: context
  - path: pages/traits/genomics/pd_t7_5_system.html
    sha256: abb9ada72417d43181fc827c1ffd0c827e2925d482e848625eeccd4be79f5c80
    role: context
  - path: pages/traits/genomics/pfiat_system.html
    sha256: e2fd1cde5f2a1535ef1f52d7bbbeeccb3472c60d0a700a746efe38977be9d055
    role: context
  - path: pages/traits/genomics/phage_defense_system.html
    sha256: 4ca7d8ed3bbb153d1aae54d7a679974e6aefc4cadc5470600bdf8d23ec1217af
    role: context
  - path: pages/traits/genomics/phosphorothioate_defense_system.html
    sha256: 400791e7a8d54c170f6a71090518787d6e3f2b9cfd99ec2f442f35793129cbf5
    role: context
  - path: pages/traits/genomics/phrann_gp29_gp30_system.html
    sha256: 9e99e1bf5159c9dd935e7a7516d4432c5380a1c0e96d4427b9fccf351e747588
    role: context
  - path: pages/traits/genomics/pif_system.html
    sha256: bdde040e7d2debb7ef777535d46a8ce382d0ff0867c3bca2d4863f06285c3f1a
    role: context
  - path: pages/traits/genomics/plasmid_carriage.html
    sha256: 5f2666f788e06a665b71d40bcba7fbf5484d1cf6bda075330e635809370ee924
    role: context
  - path: pages/traits/genomics/ploidy.html
    sha256: 521b31ad517d25306b3a91ad7d644d9d7888bbaac0b8508e47b8aa61ed569383
    role: context
  - path: pages/traits/genomics/prithvi_system.html
    sha256: 91d3ed2d6f6601e4ab516537297c713951420de997d8adfe5c269dff6ff95e98
    role: context
  - path: pages/traits/genomics/prometheus_system.html
    sha256: 5c806e05a49e03a2d76ff57d65b3b12a6754efeb1a51efd90c2ab2e223f7c942
    role: context
  - path: pages/traits/genomics/prophage.html
    sha256: 5a86ca5e5dea08755c7040adeeb94bd2b9a612684f32342939ac4479faab8b5c
    role: context
  - path: pages/traits/genomics/prrc_system.html
    sha256: a56aab94d37aee4cf6003c3282b97a68aa9dfffa3f9e9605d56ac56a57912741
    role: context
  - path: pages/traits/genomics/psyrta_system.html
    sha256: afd50cc7ba04ce990145603ced7aadd02f607dea9d437fabe68eb359a21b751f
    role: context
  - path: pages/traits/genomics/pvurts1i_system.html
    sha256: 9d7d1048568f8da97cb80c9d9df0a782d65018eb09d1c73550b541c2d528ef9f
    role: context
  - path: pages/traits/genomics/pycsar_system.html
    sha256: 2f2ea6613e161ae709f8240a9472ddd9a36a55039895dd441171540d1ec0f3de
    role: context
  - path: pages/traits/genomics/radar_system.html
    sha256: 10b477a22b96a01ed2414ef9232467f43a0b4b092ae64613e2f9bf8212a9a944
    role: context
  - path: pages/traits/genomics/razr_system.html
    sha256: 1e4f442266d8c37f8aa92ec75ab1fdbece27a7079d03b0703abf497d3e96dd23
    role: context
  - path: pages/traits/genomics/resolvase_duf5677_system.html
    sha256: 999e77fb5175d0c7d4706be2d47bfe82a1508d42f706d7eb2e9fd2aca8ddf8d5
    role: context
  - path: pages/traits/genomics/resolvase_kap_ntpase_system.html
    sha256: 6ada29f47aa46f81833926d571c96927d7bf1010e2bac407e8ec6980dbcb289b
    role: context
  - path: pages/traits/genomics/resolvase_schlafen_system.html
    sha256: 37d08e00ecba2eefb3f49f6f150b3e9e771c3be6164b4c3fb311f92edfe7d09a
    role: context
  - path: pages/traits/genomics/restriction_modification_system.html
    sha256: b692900aa3385e1c888a3d5c17b047f0dd94f52819cd7ea7c7693cc6a0cde21e
    role: context
  - path: pages/traits/genomics/retron_system.html
    sha256: f44e13fb36c063be1f9f6c6136a5c09c573d4dcebc4e04fb15bc53a1cf223b0a
    role: context
  - path: pages/traits/genomics/reve_system.html
    sha256: 20d6184fd5c1cf906edc22aac457abe36ecd3e38eec1441b3894e463efb48f19
    role: context
  - path: pages/traits/genomics/rexab_system.html
    sha256: 3ab40183c01ebeda71d7ace320664a6f27c092b29a1d84a2921be291d1fc53f5
    role: context
  - path: pages/traits/genomics/rhea_system.html
    sha256: 641ee69037e2889393cf597038d4f8904432137ac152de96a838b83a4c134ca7
    role: context
  - path: pages/traits/genomics/rloc_system.html
    sha256: 48f8e93f59e8bf4bb3168afd4c1f3b8017f6a1b1c1099956f3b39e970fc77f18
    role: context
  - path: pages/traits/genomics/rnlab_system.html
    sha256: e4fabb8219eba55f05b6ad491941d568472869c00776ca5d2ec8f4574d0bc168
    role: context
  - path: pages/traits/genomics/rosmerta_system.html
    sha256: 567ec05a75934dd1d53135dc49afa6656c9e4757491f01b89c6308096a41cf5b
    role: context
  - path: pages/traits/genomics/rrna_operon_copy_number.html
    sha256: 1ce40d9487d4d1f63e312177ea46ef5586a5e8dbed51070b4be05a9a57ef6eea
    role: context
  - path: pages/traits/genomics/rst_2tm_1tm_tir_system.html
    sha256: a76eb111412abd0a05a2bba7da5448ceb23a0836d98bf1b68e05ea76de94d33e
    role: context
  - path: pages/traits/genomics/rst_3hp_system.html
    sha256: d40cb991196561e16895bd6ced1ed9c7eb7f5dd91916583473f6a3f608fb9e18
    role: context
  - path: pages/traits/genomics/rst_duf4238_system.html
    sha256: 6c6b2608f9467ffb98a9c3685fed2280c7da6fede160e2339fa73d7f38babe3d
    role: context
  - path: pages/traits/genomics/rst_gop_beta_cll_system.html
    sha256: d799ba670071d4e0a6afa8b57b8b9b347eb6c3351af915b21ba3a3ac3211811f
    role: context
  - path: pages/traits/genomics/rst_helicaseduf2290_system.html
    sha256: 5ee545510edb16c635774106f638c8299ff40cc45ccac885fd08ea1e77549de3
    role: context
  - path: pages/traits/genomics/rst_hydrolase_3tm_system.html
    sha256: 1395e7cf9cb36010a4b810324b995375c665d956354583981fde74063410007f
    role: context
  - path: pages/traits/genomics/rst_rt_nitrilase_tm_system.html
    sha256: 691ef589b13a62dac3238c9125a69c6535e2d62eb91bd5dc74316e33596dd499
    role: context
  - path: pages/traits/genomics/rst_tir_nlr_system.html
    sha256: 580d6d47665a75af415f7ae6d633214cd10747f2c9b2066600816105a81c3a8f
    role: context
  - path: pages/traits/genomics/rugutis_system.html
    sha256: 14014036c80b6f4675ae29cac8a6a52e984958cfab78d4e98387e914326e518e
    role: context
  - path: pages/traits/genomics/sanata_system.html
    sha256: 9eff2c5f5268db7c80178f9029fd3bdc9ed5f2a5cad3358ca08c16845590e690
    role: context
  - path: pages/traits/genomics/scomcra_system.html
    sha256: a100d22e4e575cb260b7ec1e45005b1b43aa2621bb109a293b14523c9c525832
    role: context
  - path: pages/traits/genomics/sdic1_system.html
    sha256: dfadc1fd96346b9cbfd6af092632c2212e31b3ee496020ea7ad048f27b3dc748
    role: context
  - path: pages/traits/genomics/sdic3_system.html
    sha256: bb9a1d8a1e97a037bae89d1eda8a06b26019327f82fa9985f40712ddcee7b424
    role: context
  - path: pages/traits/genomics/sdic4_system.html
    sha256: f9e875579065d6721edc77e045991f5cfebc8bbf26c0d882d23c55153629be76
    role: context
  - path: pages/traits/genomics/sefir_system.html
    sha256: 7d56c7a867ed868a41c86d985517e6dcbbe783b27590126a2f6910a21ef1bc07
    role: context
  - path: pages/traits/genomics/septu_system.html
    sha256: 775f9b24818a93107b24f85f71f41439e1ed39843e3e66635a9c95c8478e4c1c
    role: context
  - path: pages/traits/genomics/shango_system.html
    sha256: 4edb2b050a0dda9503332309d059d25248ad0ec515cee1ca140c8e01a0c29991
    role: context
  - path: pages/traits/genomics/shedu_system.html
    sha256: 48d49eb4f4cf30f99f2ee221517a4cf5f2194e5b621488e2852611f084ecd48a
    role: context
  - path: pages/traits/genomics/short_lamassu_system.html
    sha256: f16ae68f1dd1ce9869b1553acea9fca9991dfc71cca33d2588c5dd86ca5b4841
    role: context
  - path: pages/traits/genomics/shosta_system.html
    sha256: 7753ccd9fca7c57f9e30a3bd0c3ee6a352483aa35a0bdb074da90937652e254b
    role: context
  - path: pages/traits/genomics/sirona_system.html
    sha256: 541d66a6c51109bd0a248871d28fd003134944fe60deff7aa158bc33c0787ede
    role: context
  - path: pages/traits/genomics/six_a_mbl_system.html
    sha256: fd5b22ef89067e28ebd0e17cac56a2ef253bbc3de7bbb5be15ce0a7bc9803f65
    role: context
  - path: pages/traits/genomics/snipe_system.html
    sha256: dc643743b2e4328db44fba56049dca0850baa5988bbe351e08b33487c1d2d720
    role: context
  - path: pages/traits/genomics/sofic_system.html
    sha256: b95f5f4e42a258effd2ecc918ccbda6563b8874e6ee8e3ca0dc1ee7713faa8f0
    role: context
  - path: pages/traits/genomics/sparta_system.html
    sha256: 58d42d626d82ad5d4cd835762779e6f82a0e99c12edf10423e50be891126173b
    role: context
  - path: pages/traits/genomics/spbk_system.html
    sha256: e08a603b46f4f0f0851f5f1aecafd6eafe517b5b7828c6e5f8dc08b766e1b193
    role: context
  - path: pages/traits/genomics/sspabcd_sspe_system.html
    sha256: 5492874f4ee491aaec1dcab7b0cc77223b8123e4fbc0d2feae140b12be16dca7
    role: context
  - path: pages/traits/genomics/sspabcd_sspfgh_system.html
    sha256: 135293aabea1b56c0097e7692bdbd2bdb00c8defe6a9efb489b8234924eba539
    role: context
  - path: pages/traits/genomics/stk2_system.html
    sha256: d455ffad94fd5b6985f115354f6cfd575f4d9b6b625d1f032862cda24e65e533
    role: context
  - path: pages/traits/genomics/sucellos_system.html
    sha256: 07b35b94e9a7bc5aa4fb6bb651f2770112d0eab10e2ea9ec1946e31073a039d4
    role: context
  - path: pages/traits/genomics/tab_system.html
    sha256: 8f2f217a8a4f78925303814eade7be7b846e41e67d85455c46fe87e4f9d82694
    role: context
  - path: pages/traits/genomics/tagi_system.html
    sha256: bbbdaea23a4b054f04805c49f3cc35629ee61787b448642c24143e117305ebb3
    role: context
  - path: pages/traits/genomics/taranis_system.html
    sha256: 676ae7a1d568748365c9fa586343db99a31735d62f15a7f7d5f8e6bd83b785dc
    role: context
  - path: pages/traits/genomics/tgvab_system.html
    sha256: a3d617eefcd8cbb45b3265f352a3acf9c61103a5daff94a84840b3dd05dcd30b
    role: context
  - path: pages/traits/genomics/tha_system.html
    sha256: 559d1f80683cc87c72aaec9d99ff3ed204d1c91bae140322c71db57503e15d9f
    role: context
  - path: pages/traits/genomics/thoeris_system.html
    sha256: 76909bf92d274f4a8fe7e4604be74cb33c8478e7e930d36a4852c946ed96c2ec
    role: context
  - path: pages/traits/genomics/tiamat_system.html
    sha256: 7eda2f4356d449515b7ae3af3af2f915d847a1f39f046c1691a5830a56711a7d
    role: context
  - path: pages/traits/genomics/tir_i_system.html
    sha256: 252881199cc7715170486d69e86283994b89a929b536709b82650920ab7964a1
    role: context
  - path: pages/traits/genomics/tir_iii_system.html
    sha256: d4aef455d72f224bbcef9a8ce7124eb4b8850c19cb90a7a837178bff028a4008
    role: context
  - path: pages/traits/genomics/tir_iv_system.html
    sha256: 58053f8a97071e3f16dc5fe9f316be93d29c3523d8e46c12d9505b18d7c4ce4a
    role: context
  - path: pages/traits/genomics/tir_vii_system.html
    sha256: 5fef8d52b78ee31ffa596d9626fe24583eba2a05ed191f18a81c0617dfc01b20
    role: context
  - path: pages/traits/genomics/tir_viii_system.html
    sha256: 6ac1d0a11967de923c3809421e9df6c49e6d35f1e96fd0d6ea6e2157e6ec6845
    role: context
  - path: pages/traits/genomics/toga_system.html
    sha256: f5633af7b7677509a134acda9207fa7c9aec519dc7797eb69c609911639c29ce
    role: context
  - path: pages/traits/genomics/toutatis_system.html
    sha256: 24cc2e2d932eae653ec840f19f0789d93107e0f33dad3854b8e5c76bb5204275
    role: context
  - path: pages/traits/genomics/toxin_system.html
    sha256: ffde72db5d3daf293a8acbe5aa5439ae0c2e055b9d1e0aa2167086cae0b9d811
    role: context
  - path: pages/traits/genomics/transposable_element.html
    sha256: c1c928ba2153f0c26c180f155cd97eb270d4a333ebba5186ba113e37bad9fa75
    role: context
  - path: pages/traits/genomics/type_i_restriction_modification_system.html
    sha256: 7f1de700b7eb0b4c945723d6c45325f53318c1d751420335fe630032b7b2c2c3
    role: context
  - path: pages/traits/genomics/type_ii_restriction_modification_system.html
    sha256: 5c18ceb2fcfea99772a116132db7d70ffbb087911e444755bc8edc5a36dcb440
    role: context
  - path: pages/traits/genomics/type_iig_restriction_modification_system.html
    sha256: 1a03cdb7a4328067c4c4037076fe82e6d99b398dd7ab63c3dd85105358860132
    role: context
  - path: pages/traits/genomics/type_iii_restriction_modification_system.html
    sha256: b345f67e34abe8d1d0ebde1b698d81aa10b7114280769a1408e7dc54bf922d5b
    role: context
  - path: pages/traits/genomics/type_iv_modification_dependent_restriction_system.html
    sha256: c39894dd81167ad65d76f6ecabcb5d17d142562fb09e269722fcf9cb0b60522e
    role: context
  - path: pages/traits/genomics/ukko_system.html
    sha256: 457b3e67038847faa29f0f7cf5c43a1dd9da1df3df868c4603ef43cba98cd27d
    role: context
  - path: pages/traits/genomics/uzume_system.html
    sha256: 9d9156cfea0b3629f82d4e9fa7bd426c568782e921023c97db9eb5bf4a816353
    role: context
  - path: pages/traits/genomics/vcam4i_system.html
    sha256: cc4ba8358225ce41c6ff983867f478efcca62fb751befd7cdd8bbd12936f52ab
    role: context
  - path: pages/traits/genomics/veles_system.html
    sha256: bac53c98acd987fb86f3de8d9c9d2f46ac69192a0919bbc18673c24ad8062eb4
    role: context
  - path: pages/traits/genomics/viperin_system.html
    sha256: 61e2f32f90ec2095806163dead8ae5bd10b3cd8961667159910e562d456e5c0d
    role: context
  - path: pages/traits/genomics/vp1796_system.html
    sha256: ea80d40fab23fd2a41ffb4ab3b3f2ac2e6482242f6afd03804a763dec7e3cbec
    role: context
  - path: pages/traits/genomics/vp1817_system.html
    sha256: c1f91f9c6d4f53f58f91979267465a4cdb687100075a368e88a912ebcff19602
    role: context
  - path: pages/traits/genomics/vp1823_system.html
    sha256: f2cb3373e750f247c46dc7d6ece42293713c5b4f82dc71f4a98c929ed5ecc11d
    role: context
  - path: pages/traits/genomics/vp1826_system.html
    sha256: e5ce3f52001555dd23d14a3a09a0da01e3df713da834e59d7fbf10b30cfc7dcd
    role: context
  - path: pages/traits/genomics/vp1839_system.html
    sha256: 8442fc2ee0e27e50ec41367f10a256974867bac7e62b2b9803f5beea89c714f0
    role: context
  - path: pages/traits/genomics/vp1840_system.html
    sha256: 9c7fd1b636362937093a4d17b4237688b0283cc068f2eac6092355945526b4b2
    role: context
  - path: pages/traits/genomics/vp1848_system.html
    sha256: 411157e28d30dcee3033e6f0456bbb3cef3ae12279b1c288e37cb78930ee84f4
    role: context
  - path: pages/traits/genomics/vp1851_system.html
    sha256: c7921c24caa4711dc716e5478091a43580c5701fabf926d6e45b0d62808be292
    role: context
  - path: pages/traits/genomics/vp1853_system.html
    sha256: 996b78779f75bffedfe28eb431d088ecac67c47faaf80b3af0f935ef0c8e5a87
    role: context
  - path: pages/traits/genomics/wadjet_system.html
    sha256: e33fad16df4d2bc9ad26d637f9f7b46f1ac88cb30ceda361c98fd1c44575dbcb
    role: context
  - path: pages/traits/genomics/zorya_system.html
    sha256: 45562d97284c2b8b9d7706b42b0be11c93d7a62321536d20a5561ac0a63b13a5
    role: context
  - path: pages/traits/genomics/zorya_type_i_system.html
    sha256: 2bcee95322e990b4f18338873385588bf63556547970a6438912317a28e11116
    role: context
  - path: pages/traits/genomics/zorya_type_ii_system.html
    sha256: a8aa48601ff007b3e80204920654e884b13c7a2e10997c7ba56e31da219fe935
    role: context
  - path: pages/traits/genomics/zorya_type_iii_system.html
    sha256: fab65bba05546e825ca1b951d432649231ef0bfbd2ff1837880acc9f50481fc3
    role: context
  - path: pages/traits/metabolism/accumulates.html
    sha256: ca47ce39803ca8627c8bb520b7e2bf55929470cd2c3beafcde5b2dfcf268c026
    role: context
  - path: pages/traits/metabolism/acetoclastic_methanogenesis.html
    sha256: 6c35ef8317a66f768608eff7ad05fb8c6a706f8b5f0a6039ab3d728eb18b671a
    role: context
  - path: pages/traits/metabolism/acetogenesis.html
    sha256: 76dfecfe7a8a954a9b62f57e8985c525019b2e0d6545afe783d8c1bff7f5146b
    role: context
  - path: pages/traits/metabolism/acetone_butanol_ethanol_fermentation.html
    sha256: 2ddf507279b58cbbfc956e03309453815710c68e6343b96420a2970e1e5112db
    role: context
  - path: pages/traits/metabolism/aerobic_respiration.html
    sha256: 232f9c43a067a66df15da84549551e0a5d1170e96c84ebceb8d5a4ba4358521d
    role: context
  - path: pages/traits/metabolism/anaerobic_ammonium_oxidation.html
    sha256: bfa452667f28ed9e9df50d8bd013af170e0eb4954a546faf8f1942eb7a4365f4
    role: context
  - path: pages/traits/metabolism/anaerobic_oxidation_of_methane.html
    sha256: 0f62b4ef34012a8ca144c355d48c1fd4f45e85e1cdaee3a7155d49c745a6b652
    role: context
  - path: pages/traits/metabolism/anaerobic_respiration.html
    sha256: 2531568c24ed9ce7dae42f7a18236070b432ac91079b7302b46499bd3c7e1404
    role: context
  - path: pages/traits/metabolism/anoxygenic_photosynthesis.html
    sha256: f0aff96b7c36767e30ad3dc2a0bcdab6168f681e70ab66f3d6b013f65572ff6a
    role: context
  - path: pages/traits/metabolism/aromatic_compound_degradation.html
    sha256: ce0816e9dcb4a17f52a8ef718c62446b05fed2d5daac8c1621ffc3ec897fda15
    role: context
  - path: pages/traits/metabolism/aromatic_hydrocarbon_degradation.html
    sha256: 32f3cd17aa370db85765474baef1587a9248e5862482a98ddc5f9157800ba239
    role: context
  - path: pages/traits/metabolism/arsenate_respiration.html
    sha256: 9d4e85a82a2c880145813ae34b16357bbedfc8721fca577009422ad18abb27df
    role: context
  - path: pages/traits/metabolism/arsenite_oxidation.html
    sha256: 789177b3568e54b2ae372b16a5d911af1cf06007c9b0bba945aea71f56e778ed
    role: context
  - path: pages/traits/metabolism/assimilates.html
    sha256: fd0b5056a59848e26bd681f06210e6de336745d08b76997ebe5d1b92fe1fe47e
    role: context
  - path: pages/traits/metabolism/biopolymer_degradation.html
    sha256: c24dc207ad1f93a68d0f46a3e70aaf45523823c8b97ad2a95dcbdbb6defdba6d
    role: context
  - path: pages/traits/metabolism/builds_acid_from.html
    sha256: 5ef1b87c43041669517f3fbb941763eeebf709654fb5643d463f40a64fb022a7
    role: context
  - path: pages/traits/metabolism/builds_base_from.html
    sha256: c444b1c8f341e2becf3a58977080ee27b312c76320757f9d7c0721546435a97c
    role: context
  - path: pages/traits/metabolism/builds_gas_from.html
    sha256: aaa087aada15246952c974669a22b6cd58d47db5d2b7178f7822477797b36dee
    role: context
  - path: pages/traits/metabolism/butanediol_fermentation.html
    sha256: 7e5b53c4dc29b4880c91d1191eb495701e55dfb067abbbcdfe953686aa81a26f
    role: context
  - path: pages/traits/metabolism/butyric_acid_fermentation.html
    sha256: bcfcb8b5b8821e7eb3ea76908fcc0227969edf0635a17100c7c006324ab389ec
    role: context
  - path: pages/traits/metabolism/cable_bacteria_metabolism.html
    sha256: ff1f5860260d057128a6dca63f38b2216be2186e3ced76545b62cc5b51b9930e
    role: context
  - path: pages/traits/metabolism/calvin_benson_bassham_cycle.html
    sha256: 8246b3cf1b18c820c05466e1de3063c4eac062723e29b8788ad4badb26d4cf72
    role: context
  - path: pages/traits/metabolism/capable_of.html
    sha256: 334f93bf18e071440bcfbfcf1cb0432b2ba41ce8229b8720b3d567174ab0fb64
    role: context
  - path: pages/traits/metabolism/carbon_fixation.html
    sha256: 1b6461c02a29606f36d2bd53ec3ceb95ac3a1543e35a8f76d22ec7c2705f5fe9
    role: context
  - path: pages/traits/metabolism/cellulolysis.html
    sha256: 14e73b85d5a11fd811ce8c41e9edbeb84b71bbb8e37a0056782b6625d8e61da5
    role: context
  - path: pages/traits/metabolism/chitinolysis.html
    sha256: 9b8ea833a15a3a53625dd785c85f127fb5b273083cce3cee843c1ace349cffa0
    role: context
  - path: pages/traits/metabolism/chlorate_respiration.html
    sha256: 0afe7015a4697e002ccf76ab8ba282897e4fcffee97efecf8acdab54b886e69d
    role: context
  - path: pages/traits/metabolism/citrate_fermentation.html
    sha256: c1f7d765eae4e870b9f73b4cd998b15260eac2fb9715187c7f71151a012ea456
    role: context
  - path: pages/traits/metabolism/compartmentalizes.html
    sha256: 20831c5f504e0278771b9f3b926b0a250c0a90e18fb87205db6390ff43a93178
    role: context
  - path: pages/traits/metabolism/complete_ammonia_oxidation.html
    sha256: 6db844cd3c55e7a2bb002c02739448db9901745a42ba9b75b87c48b93e3f4907
    role: context
  - path: pages/traits/metabolism/dark_hydrogen_oxidation.html
    sha256: ee94339b980437f5c852f7f3fc9194a9502402096e7704411810a25540a31509
    role: context
  - path: pages/traits/metabolism/dark_oxidation_of_sulfur_compounds.html
    sha256: bfa1c8dd737205f958e01c5ba101b5d4533c75a93751aec110c8cdb961994a34
    role: context
  - path: pages/traits/metabolism/degrades.html
    sha256: eae09b04866327584c97e89dc6ab9d85aa4f8978f78521b05244940f52700ad5
    role: context
  - path: pages/traits/metabolism/denitrification.html
    sha256: 026e0d2d2a295ce6445e79c0b71e211cd8535e08451d5c4a1f2dce3020274d2c
    role: context
  - path: pages/traits/metabolism/dicarboxylate_four_hydroxybutyrate_cycle.html
    sha256: 51dcbee48c8bfce9e0001c60199a7484c603ae89d63334f35f51c41b5a2f5d43
    role: context
  - path: pages/traits/metabolism/dimethyl_sulfoxide_respiration.html
    sha256: 6c39e2ed506cb92f9109ea981d3b20272c3d870a088e2866a100e5dd3322c03c
    role: context
  - path: pages/traits/metabolism/disproportionates.html
    sha256: edbe203439c31ea355d76b2ed3a87bae7576e00799e2b8552225da726b0e7e3f
    role: context
  - path: pages/traits/metabolism/disproportionation.html
    sha256: 9fe8835198f16b6a11293eca88e5ee71c4bfa6683b6c12a056772bace9242e37
    role: context
  - path: pages/traits/metabolism/dissimilatory_iron_reduction.html
    sha256: 846933ae4d3efa596e3ce2504c6adbef69146045941e0fe8bf1d768495ab60a3
    role: context
  - path: pages/traits/metabolism/dissimilatory_manganese_reduction.html
    sha256: 3c1ddcbbf34eff8f1def02d67a06753da409884379a93986813d798bacb9fff2
    role: context
  - path: pages/traits/metabolism/dissimilatory_metal_reduction.html
    sha256: d0db4ce237661e7f0e1da0643d60bf354d5fef794ab93fe028b8f1dd26d690ea
    role: context
  - path: pages/traits/metabolism/dissimilatory_nitrate_reduction_to_ammonium.html
    sha256: eca07c93a6a2c3d24ee92f7d3347ee6f34c770c98dd2aee2d4d6ac306524b1c9
    role: context
  - path: pages/traits/metabolism/dissimilatory_sulfate_reduction.html
    sha256: a23f731b9194966d27a5c85a4909c9daac1dc03c7b808c47afa583b829fac9fa
    role: context
  - path: pages/traits/metabolism/does_not_accumulate.html
    sha256: f76d36166167547fb5d5e85cb26b96b35169b66a3d141bb7daa404514448c9d2
    role: context
  - path: pages/traits/metabolism/does_not_assimilate.html
    sha256: 29ba083666922c784d147242e371c455725b808738fae5c77dec7de471126c8b
    role: context
  - path: pages/traits/metabolism/does_not_build_acid_from.html
    sha256: c02e49bc125f76b8c2aacaa8b5e7b473f69ad1eecc32aa386a15fa2fa032d95a
    role: context
  - path: pages/traits/metabolism/does_not_build_base_from.html
    sha256: 7809e270d7baab8347c04ead5cbeef85198b7dd67d1805fb49eb9c5cb211f85b
    role: context
  - path: pages/traits/metabolism/does_not_build_gas_from.html
    sha256: db84ca559fa72009a758a5fe399b82ed51b84019f04114b352eada346b119d3d
    role: context
  - path: pages/traits/metabolism/does_not_compartmentalize.html
    sha256: 0680af816551f99cd8de226afb0b240be5a02f00e5218e3be4e9d73823345c74
    role: context
  - path: pages/traits/metabolism/does_not_degrade.html
    sha256: c36e911d3555781ee0aaec42c1801b0d1657718d90d8df53634b89c5f3df1818
    role: context
  - path: pages/traits/metabolism/does_not_disproportionate.html
    sha256: 0e0e7dc25ccf3839cd0b5fdcd4a9aec163e68ed459812b979fb54d5763e8dfa6
    role: context
  - path: pages/traits/metabolism/does_not_export.html
    sha256: c1a6de6c9e4720aec7ea0d9a44dcd4880da2f4a93429e1e5258c3f1dfbd35039
    role: context
  - path: pages/traits/metabolism/does_not_ferment.html
    sha256: a0a9d075ea3978f5f61cf5dd7039293a64862bd72495b3a446567d84ea10ea9e
    role: context
  - path: pages/traits/metabolism/does_not_hydrolyze.html
    sha256: 972b70a098c90cf96623f30179e2b2f64acd556dd6ea965f00b6e57efc6206fa
    role: context
  - path: pages/traits/metabolism/does_not_import.html
    sha256: efac8a3fec206475621fc7d8f37e282c0a9f80ca889dbc665acce78de5f6a68b
    role: context
  - path: pages/traits/metabolism/does_not_oxidize.html
    sha256: 379ecbe4fdf9be2beb911516f4b8e38bcc3feb129dd23ea0e64d9f025454b91e
    role: context
  - path: pages/traits/metabolism/does_not_produce.html
    sha256: 409a5e094a21a3efa1504d10b17adf27cf677161d3607d5c7724f934461c2aa3
    role: context
  - path: pages/traits/metabolism/does_not_reduce.html
    sha256: 6b4a6a9919dd0d41a258419ad64ef301e01912d037f57e440d26c5fdf956c208
    role: context
  - path: pages/traits/metabolism/does_not_sequester.html
    sha256: 0ed815b111239e3d3072f5a568fb440cc34374baadb01bdc3de227e783c34576
    role: context
  - path: pages/traits/metabolism/does_not_show_activity_of.html
    sha256: 1f34ae92307e73158ee248bf8f511a7e6f30ee4c09acb2bf9842fce567a95c1d
    role: context
  - path: pages/traits/metabolism/does_not_transport.html
    sha256: e4bd7f2f19fa072592df2b0642829440023c5a14adff8e9fd6fa9e959a3b05f6
    role: context
  - path: pages/traits/metabolism/does_not_use_as_carbon_source.html
    sha256: 685cb66ba401c335809fabe5853a9077e1e45238c825bf579106653d115d0be7
    role: context
  - path: pages/traits/metabolism/does_not_use_as_electron_acceptor.html
    sha256: 3b2aa97e74023d2b02f980be3315ff4517b7d1c7d5a1d4d0e69d6cb7741b16cc
    role: context
  - path: pages/traits/metabolism/does_not_use_as_electron_donor.html
    sha256: fb35a8199dd0952c7a42349c3e82b120ce342ca64cfa3ac0ba9e62631babcf1b
    role: context
  - path: pages/traits/metabolism/does_not_use_as_energy_source.html
    sha256: 1eafe7941332234816c2d7c6d3dfed6bfe3ff65b41993eea23ee41d07204d0b4
    role: context
  - path: pages/traits/metabolism/does_not_use_as_nitrogen_source.html
    sha256: 34193cfca33cfd17560af02dc956ea9a7015aa6cd2150ef54303d800df52daca
    role: context
  - path: pages/traits/metabolism/does_not_use_as_sulfur_source.html
    sha256: d5df8700fb183b0d0eadee8d8bf04060a46a88bc19098c6272a64c018abdad0a
    role: context
  - path: pages/traits/metabolism/does_not_use_for_aerobic_catabolization.html
    sha256: b722ca11c5f44da41ec02e87d9cf8ece88e9630eea65036431e9179a7972c60f
    role: context
  - path: pages/traits/metabolism/does_not_use_for_aerobic_growth.html
    sha256: d2b30fdd282a1de430760eb216f8c33df8b5e8d9b9243acf45be2665c7d6f01c
    role: context
  - path: pages/traits/metabolism/does_not_use_for_anaerobic_catabolization.html
    sha256: daeeaf488b913b65224a5b3633b8ac7dcf797eb15190913560bfd0c66c7e80ca
    role: context
  - path: pages/traits/metabolism/does_not_use_for_anaerobic_growth.html
    sha256: 585db976966b9d36877d8583c5d4fafc441bf21823cb85b0d2f0a9b13f3765e9
    role: context
  - path: pages/traits/metabolism/does_not_use_for_anaerobic_growth_in_the_dark.html
    sha256: 7463a1bd2009366cfce706f77d57d15cf13b1096c46fda23bde604feabe4c115
    role: context
  - path: pages/traits/metabolism/does_not_use_for_anaerobic_growth_with_light.html
    sha256: f581295d557391cedf8e656fadd44da74ed12bb1f07e3845268012e4e7183ba7
    role: context
  - path: pages/traits/metabolism/does_not_use_for_growth.html
    sha256: b58c3fb32d7fa817adb2350962f1957e11e38c1be7f6fdad44dda97579c1a9cd
    role: context
  - path: pages/traits/metabolism/does_not_use_for_respiration.html
    sha256: 83777d96d7ca05b48829cd6738b036b512816985ae899df9d92bb6af92abd852
    role: context
  - path: pages/traits/metabolism/does_not_use_in_other_way.html
    sha256: 35a060b9b2f825f7fe3591a2f44cea4a43bc3e108a79f8fb8ef472390e5e3120
    role: context
  - path: pages/traits/metabolism/electron_transfer.html
    sha256: 3522d264e61c167d8cc71927157c90ed6c16f84a25a87a0b78c22f13a9034852
    role: context
  - path: pages/traits/metabolism/enzyme_activity_analyzed.html
    sha256: 70d86fee5d35e2f0db2dd797c6fe8224cf19e08908d4f5b6af1c037c865dcf2b
    role: context
  - path: pages/traits/metabolism/ethanol_fermentation.html
    sha256: 6255928076d34fd68e5e23de787020384f272c4bce0f912b0c749a6b75dd45bf
    role: context
  - path: pages/traits/metabolism/exports.html
    sha256: c62a5d87e9b3d82bfa3fa316495f94c2e0159d7f7fd320d1732c28f7c2b49ba1
    role: context
  - path: pages/traits/metabolism/fermentation.html
    sha256: d1199201313f4ad012dbca23198a3cdfe0c1e48b13c9d845cded8406612f6dfe
    role: context
  - path: pages/traits/metabolism/fermentative_hydrogen_production.html
    sha256: 8409be0dc79c13470f29dfb46d3555c195a5858b1e9d46391f9d2e6bf1de86bf
    role: context
  - path: pages/traits/metabolism/ferments.html
    sha256: 7fb2eeddeeec45b398ea725c92fc0d883d9d985f636f3e22102206552ad2640e
    role: context
  - path: pages/traits/metabolism/fumarate_respiration.html
    sha256: 31b7bd663cce7c5da756a7cfbc3497d9b0380cb2a194532c2b67e3546d0348a3
    role: context
  - path: pages/traits/metabolism/has_growth_nacl_observation.html
    sha256: e19740cec875a60492bcfdee3753a9bf7f77af36f79f05eedf1cb38fde74b5b3
    role: context
  - path: pages/traits/metabolism/has_growth_oxygen_observation.html
    sha256: 9c414a5d5a93c80d1a8d92643ce70d7a519277be290a91a921fb1cc0213da9ef
    role: context
  - path: pages/traits/metabolism/has_growth_ph_observation.html
    sha256: 57282fc49da9d5d0cafe474330ab04ea359582eb89d3e3930f5da09c102d21b6
    role: context
  - path: pages/traits/metabolism/has_growth_temperature_observation.html
    sha256: 4800c699d2a9ef717e64e6a3d1b34e4ab28e67727906407196b7c2cba0941b50
    role: context
  - path: pages/traits/metabolism/has_nacl_delta_observation.html
    sha256: 94c18c20b8c023e03b8912f1b4004d791acc70382765ddf2704d6c0c954e07df
    role: context
  - path: pages/traits/metabolism/has_nacl_observation.html
    sha256: f00e9d01fc749d4d181ad325f60111037404f1f6228408bee0c1bb0b55c9209e
    role: context
  - path: pages/traits/metabolism/has_observation.html
    sha256: 2b08aa14451eaecdb5e2a8e7c74133797d8b7988d944aeefc9078e03bf8cda52
    role: context
  - path: pages/traits/metabolism/has_optimum_nacl_observation.html
    sha256: c813a4e68629021371accda7d6dcf37eb3abc66aba7788b162aaf25a67e586ee
    role: context
  - path: pages/traits/metabolism/has_optimum_oxygen_observation.html
    sha256: c00b31b1f3fd0245d81a0b7eeea49cc062fca2ce250ad206c1d20a9de5fb3626
    role: context
  - path: pages/traits/metabolism/has_optimum_ph_observation.html
    sha256: 9b8836c8919e0dcc1a11c80f06d5ec6f0977a92e3ca26bb15c171b56be2c041c
    role: context
  - path: pages/traits/metabolism/has_optimum_temperature_observation.html
    sha256: 7fd30e2039fc6007749148f9d4b746086ed9d5851390bb08a340cff2f149eed7
    role: context
  - path: pages/traits/metabolism/has_oxygen_delta_observation.html
    sha256: a683c8f86fcaa5c2124a604bba22c6d57b84f97e0992eeed3339cbbf698a5e48
    role: context
  - path: pages/traits/metabolism/has_oxygen_observation.html
    sha256: 7c60e74c9d69aee1c28d2316cb2e4dd4277fe7bee62c89ac79cb2d5169f5f2b8
    role: context
  - path: pages/traits/metabolism/has_ph_delta_observation.html
    sha256: aba3c53fe1a4658b21ddd804b43189c579ce059b43ac63ad055052255eee36a9
    role: context
  - path: pages/traits/metabolism/has_ph_observation.html
    sha256: 33564d976efda1abc6a291006cea37d3492b66b7d8d125a753d75b8fa6de748a
    role: context
  - path: pages/traits/metabolism/has_phenotype.html
    sha256: 155dfbc538ba58a470b29bd86515dda18ed277a4a6f0346152c787ecce19c6ad
    role: context
  - path: pages/traits/metabolism/has_quality.html
    sha256: 44224017a9cc1408ac9480b8b7f49695a06af499cfcb1e6c9b2168545e679ec4
    role: context
  - path: pages/traits/metabolism/has_range_nacl_observation.html
    sha256: b110c68f37b9ac2945846d49f0116283d95e41ad906852b7c7fd91395f1366c1
    role: context
  - path: pages/traits/metabolism/has_range_oxygen_observation.html
    sha256: 0602f69888d59699c3c0c22fea15a8d5a26be72b97518ef60f5a6d100c25087d
    role: context
  - path: pages/traits/metabolism/has_range_ph_observation.html
    sha256: bfafa6b3865c210f08eedaf4777fc5e12793582c1c85dd5d18899ab5a8e3598f
    role: context
  - path: pages/traits/metabolism/has_range_temperature_observation.html
    sha256: 64f7f4d43a0ef45f3b7779fa468777788f4641775ce1dc19c80ca33e88029675
    role: context
  - path: pages/traits/metabolism/has_temperature_delta_observation.html
    sha256: 3cd8af516dbe3f59e9977de40b40a619474e8667e0c1d418098b0e90a3364101
    role: context
  - path: pages/traits/metabolism/has_temperature_observation.html
    sha256: fc1f324760b2f1d754cec48bfcc000425ed35e0a8f786e8f8d48e222d48eb7ec
    role: context
  - path: pages/traits/metabolism/homoacetogenesis.html
    sha256: bd109dbc526fa696ee968fb389c4cec3491a4450e8e4064e06ed9a687fa3dbc7
    role: context
  - path: pages/traits/metabolism/hydrocarbon_degradation.html
    sha256: 99e7e0f51f20e696b26a69b90b7f50978399d473c8050320a7d13da4ba60d5aa
    role: context
  - path: pages/traits/metabolism/hydrogenotrophic_methanogenesis.html
    sha256: dd300bd1febed50da74deebffff01f28264cd4081bf29d7d647585501e2eb4e2
    role: context
  - path: pages/traits/metabolism/hydrolyzes.html
    sha256: a0707142fab72baa5c6991d742e09723134c83fffe9a9be83998ab88ac0714ac
    role: context
  - path: pages/traits/metabolism/imports.html
    sha256: 73e658496aaf00c07177ad82405a019afd51af3b9cc94608dcb78b2c74dc6f20
    role: context
  - path: pages/traits/metabolism/iodate_respiration.html
    sha256: 3af57574ab1852393e49f2b761318a0f7cb68609f170e1fb53ed2d4a27b0ce89
    role: context
  - path: pages/traits/metabolism/iron_oxidation.html
    sha256: ab84ddea0bc01d5dc82be68dddafac3150a5dad480df7f86a54f2de4ac1e0920
    role: context
  - path: pages/traits/metabolism/is_not_required_for_growth.html
    sha256: 6aca5065b32dd63371fe2a2471a6293d336d2b86b1c4af4c6a9afe39509adb88
    role: context
  - path: pages/traits/metabolism/lactic_acid_fermentation.html
    sha256: 62ddc87497644b15db5e1c8860292a0fd2822959d21a4a2937f74419594cce95
    role: context
  - path: pages/traits/metabolism/lignin_degradation.html
    sha256: 19de79e1c48f92a5efecf2eeedbb73b15191f0dbf09089d1f8c65d51bf5c3df0
    role: context
  - path: pages/traits/metabolism/lipolysis.html
    sha256: e1b56e63756aaf1bcdcb9a12658a67c442e1032cd754606dc2bb5beb39179114
    role: context
  - path: pages/traits/metabolism/manganese_oxidation.html
    sha256: 0e99d1cfe2a28d396bdbb2d2854a6ee4c48c4b974e04207591e51841fbd6f9bb
    role: context
  - path: pages/traits/metabolism/metabolism.html
    sha256: 4313fdeb93846c5ea2633a5db6e3e87c327052a6fa3949f5fbab80c37a1e83fa
    role: context
  - path: pages/traits/metabolism/methanogenesis.html
    sha256: 3101833a9c1c50e4ba2ec1931bba346f151d88521c7682be41236d16f216dd94
    role: context
  - path: pages/traits/metabolism/methanol_oxidation.html
    sha256: ae491a28e62ad76090759fba51a660e5e9c608b15a03a31fb9acd8aadf08b6be
    role: context
  - path: pages/traits/metabolism/methyl_based_methanogenesis.html
    sha256: efde2e5724d96b32cbb8eef2ce918a95762ba7944b6bb47d3953255eb653e52e
    role: context
  - path: pages/traits/metabolism/mixed_acid_fermentation.html
    sha256: e58fe26c2542ecdc31ad4e49c262eb8a5500d24ec06595a167a4a81271678211
    role: context
  - path: pages/traits/metabolism/nitrate_reduction.html
    sha256: 5bd5661e82971af99e031029097a60ace9335d7be743d432c8bc396ee94a3164
    role: context
  - path: pages/traits/metabolism/nitrate_respiration.html
    sha256: c518f4870463923925cb71286f03a04880ff51288918adb9c50a26bb7e350d39
    role: context
  - path: pages/traits/metabolism/nitrification.html
    sha256: 719b7ec3c915ebbd31b4b3b45578e184fee9a82cda28f1c2887517474c721e6d
    role: context
  - path: pages/traits/metabolism/nitrite_respiration.html
    sha256: a371cb3d479918e66df9852e92bc6e865b8293a90063749043957c52dbe98742
    role: context
  - path: pages/traits/metabolism/nitrogen_fixation.html
    sha256: 212fd137f4d9fdf99ae6685f8488d9dc1fa823e6076802beee98a656f7d579e7
    role: context
  - path: pages/traits/metabolism/nitrogen_respiration.html
    sha256: f3a035b47a34b45460e9bc8a600ae1bf337e85c7ad6d34336405212ea274967a
    role: context
  - path: pages/traits/metabolism/organism_interacts_with_chemical.html
    sha256: e077fb2bf19224c5cce01f114ed9ecd8e0fba4f12bb4bd75e869504081adebfe
    role: context
  - path: pages/traits/metabolism/organohalide_respiration.html
    sha256: e521facfaaff7aae1f44aab6d251d6b0b4c039dc680db5326a8a9e137efa7d70
    role: context
  - path: pages/traits/metabolism/oxidative_phosphorylation.html
    sha256: b2eb14838d782fa6b453e563ab74226fcca319db89abf4fde8eaf5c39b510b77
    role: context
  - path: pages/traits/metabolism/oxidizes.html
    sha256: 1326ebd3530996ec9090e051c14001a005d7b791acc18ed145accfa6a4fc3016
    role: context
  - path: pages/traits/metabolism/oxygenic_photosynthesis.html
    sha256: 7ea5d58b4ddb3fe3db59173d9cda1f5b27b25ec288c8b5c822d6d46abf774f75
    role: context
  - path: pages/traits/metabolism/pectin_degradation.html
    sha256: c300eec2c5f197bb09d99b54f268efc0e2dfc9eabcadd761781ea50eccf08550
    role: context
  - path: pages/traits/metabolism/perchlorate_respiration.html
    sha256: 7f8c7597758773878175cd18e029b627ba4fe3701a7d8e8c50f74147038ec88d
    role: context
  - path: pages/traits/metabolism/photoferrotrophy.html
    sha256: 5d9e2fdf5a1e101d35d0538e3205ddbe7f7a8ef94c560796271d4dcc0a68d3ba
    role: context
  - path: pages/traits/metabolism/photosynthesis.html
    sha256: cbe61df8c118d16a938adc9d8513fb09853f97262e9bdac6382ea27e8155a5bf
    role: context
  - path: pages/traits/metabolism/phototrophy.html
    sha256: fb790d1c95b5dc5a28fcd7926ce9b3e2833b64f3bda98409bd940a279f96856d
    role: context
  - path: pages/traits/metabolism/produces.html
    sha256: 333b7898f0d4b72ebc146b3f84d1cee08ae12b057de5d1d5b9300d18af80d3c4
    role: context
  - path: pages/traits/metabolism/propionic_acid_fermentation.html
    sha256: 2f458ca98910dd49c8fc13e8fc4c108f7829be17ef1ac95df556338442626bfd
    role: context
  - path: pages/traits/metabolism/proteolysis.html
    sha256: 771f385f24c7532d935b1b48c236a1dbda3f06e4c2a42f04131f19169f6cfc7a
    role: context
  - path: pages/traits/metabolism/proteorhodopsin_phototrophy.html
    sha256: ea11cc285788e8f633dd25e639d96be2a0ae3cc7de405ef7adc909bc80141fcc
    role: context
  - path: pages/traits/metabolism/reduces.html
    sha256: e5ba8a142485a64157a3765ab545cb1c20b938baffc39d8de54a0c22aaa8eff1
    role: context
  - path: pages/traits/metabolism/reductive_tca_cycle.html
    sha256: 0431e73dbe2ef64bd85944bd11254ac8933dcb2bafd1b339dea1cc651edac2ec
    role: context
  - path: pages/traits/metabolism/requires_for_growth.html
    sha256: f10dc154848fb17a503bbbb80a2559ff25e71b40c7bbd539ce203dfb2cd40ae5
    role: context
  - path: pages/traits/metabolism/respiration.html
    sha256: 76872d80a6f3ac466855178b5f5eb55b7e49acd75c8d5e92112102915c29d106
    role: context
  - path: pages/traits/metabolism/respiration_of_sulfur_compounds.html
    sha256: 5dd60653da2d667eb5a793ec203d53c8b4d10770425d37939e90f566a07408a8
    role: context
  - path: pages/traits/metabolism/selenate_respiration.html
    sha256: 3b059837da546aa86248ba56453a7c64937731ab47f7eb49adac1812c3868553
    role: context
  - path: pages/traits/metabolism/sequesters.html
    sha256: 8279a15d6813f25b04ef67521d122860954bf61444827851b1960b485e6c9a78
    role: context
  - path: pages/traits/metabolism/shows_activity_of.html
    sha256: 59e8b08814b2d93089f4f6769acec92912ce443f8b91ccaf6b46fa108a08e34b
    role: context
  - path: pages/traits/metabolism/starch_degradation.html
    sha256: 77bd0f76ed32a95538201127284c0887776d9097c12fdb157eb7b6ef8e3c9c5c
    role: context
  - path: pages/traits/metabolism/substrate_level_phosphorylation.html
    sha256: fd4c5186db9c8d1e42ba651cb045ac1816a537e9eefc84fdb567b3b0b7527cd8
    role: context
  - path: pages/traits/metabolism/sulfur_oxidation.html
    sha256: 030a5f0de91058e8afb8026a2ee4d5caad3990208c6749aabd343c9f3d0c94d8
    role: context
  - path: pages/traits/metabolism/sulfur_respiration.html
    sha256: 09f3eda8d9c98cc4a3254a76f6210ed26bd78b48e13068e67673ab6d5af26a28
    role: context
  - path: pages/traits/metabolism/syntrophy.html
    sha256: 9e4ec82dc77ee0f406ba45f25948ddd59ecb972125b9ef3b4bb065ee61d2b947
    role: context
  - path: pages/traits/metabolism/tetrathionate_respiration.html
    sha256: 2acb4f23803439258242b371b296804a40da7e4ba2d4dfa52f54cc060bd18d2c
    role: context
  - path: pages/traits/metabolism/thiosulfate_respiration.html
    sha256: dc1a20a4680c88585cf50c8a8326558020a87ac87bb87da5fb85efcd71499457
    role: context
  - path: pages/traits/metabolism/three_hydroxypropionate_bicycle.html
    sha256: 139a36d16f424e6bcf10623faacecba525048d2ee3d5ca16f42e9c6bb5a094a5
    role: context
  - path: pages/traits/metabolism/three_hydroxypropionate_four_hydroxybutyrate_cycle.html
    sha256: 06f82d9342fd6c11c27e65d6bb513a33f79687058171992b1093bf7e374fcb75
    role: context
  - path: pages/traits/metabolism/transports.html
    sha256: d77e4871a5e24d0da791520815c57cae5c652be1667ba6ebb22c6470e736a0b9
    role: context
  - path: pages/traits/metabolism/trimethylamine_n_oxide_respiration.html
    sha256: 13805b4314a30489352c933fa91eb64aa3e9b72054dffd65d82974ff55ca25d9
    role: context
  - path: pages/traits/metabolism/uses_as_carbon_source.html
    sha256: a168c0499b27eb2ef79657666a93b3ef37624aa28883560317742de1dbbf5f15
    role: context
  - path: pages/traits/metabolism/uses_as_electron_acceptor.html
    sha256: fdbda733c4ef038ef127c073af550e5ee4c09f601ae4e0fcc11a8a8323f78ef6
    role: context
  - path: pages/traits/metabolism/uses_as_electron_donor.html
    sha256: 92240af2b9c92cfec2d744ce0280ad83799bc64b962342ebf9a95780f0ab6e18
    role: context
  - path: pages/traits/metabolism/uses_as_energy_source.html
    sha256: cc9e90c7eedfcbf8176ad78afe38a24484997a602b2a1cebd0073d741c969855
    role: context
  - path: pages/traits/metabolism/uses_as_nitrogen_source.html
    sha256: 73b7f1d8cb7f66ec2f0f74f1b1e7c2b339e43c155df9ef6638be76c71771f0a9
    role: context
  - path: pages/traits/metabolism/uses_as_sulfur_source.html
    sha256: fb2a7c8ce003fe0ef44ed49da8d941c6d188226d0b7fd4a08e5dd83cc0cba5e6
    role: context
  - path: pages/traits/metabolism/uses_for_aerobic_catabolization.html
    sha256: 694ba59383b1bb8fcdfec83af61787d8d132b6869970a6ba96403af88d696b3c
    role: context
  - path: pages/traits/metabolism/uses_for_aerobic_growth.html
    sha256: de169d1ff6f33cbfcde288279c04733c8cbb457d21e884bb3bd133d5e336e58c
    role: context
  - path: pages/traits/metabolism/uses_for_anaerobic_catabolization.html
    sha256: d1489c0d259162fed0cfed363adade1a4d1793ae4d3863988385f3f3e245f591
    role: context
  - path: pages/traits/metabolism/uses_for_anaerobic_growth.html
    sha256: 3cb4dc7d4890a2cf100060f37baf6487dc64686ca1cffc5c28e9929d975b1df2
    role: context
  - path: pages/traits/metabolism/uses_for_anaerobic_growth_in_the_dark.html
    sha256: a8c3016bccd059981fbecbf2a2bc07b61a7c6dcc92123754734b3af0d28db975
    role: context
  - path: pages/traits/metabolism/uses_for_anaerobic_growth_with_light.html
    sha256: 146d8a4668996110141ac30088348e8c4cae919c4898b28667ed9be666a6d1ef
    role: context
  - path: pages/traits/metabolism/uses_for_growth.html
    sha256: 51ecf6a6681537ae4aeaf225cf70ae5df39d060612c492970df4320598e5b5b6
    role: context
  - path: pages/traits/metabolism/uses_for_respiration.html
    sha256: a20fc134f8bb276d8af07535780a628949f751c31b6c81fbb2a671de9d23dc98
    role: context
  - path: pages/traits/metabolism/uses_in_other_way.html
    sha256: 0b58b2f87acc9f31746190ec346fe181712fa1a41975486bbdbcfd1af92d7f7a
    role: context
  - path: pages/traits/metabolism/wood_ljungdahl_pathway.html
    sha256: 084c6f98f9b31dfa1dd1669c499092c3080fbbe68304e7402f548419d3a7ed75
    role: context
  - path: pages/traits/metabolism/xylan_degradation.html
    sha256: f4834c7930f4e1bb38310a02b92ed8e0d6c934a9e9f663ff37775c4ecdc54f19
    role: context
  - path: pages/traits/morphology/akinete.html
    sha256: ca02c4f24476bacf75713465f6abf01a518537c488e3cf179290cbfe71341686
    role: context
  - path: pages/traits/morphology/amphitrichous.html
    sha256: e5985a85d02ecc03dbc7716eabcab31ad71ff87a867290337aaa597d636d136c
    role: context
  - path: pages/traits/morphology/axially_filamented.html
    sha256: c966d97d63ff69143490029b6afe919edfa742e323800cbb0759ebf3ca742ff3
    role: context
  - path: pages/traits/morphology/bacillus_shaped.html
    sha256: 850d2fb000b28dd8f792825b58b0872247272899922e01531f0e4dcdcbb40f90
    role: context
  - path: pages/traits/morphology/baeocyte_formation.html
    sha256: 57a09e04767528af11dc39415109db7590d788be52ed66fd5845d10aff78e35c
    role: context
  - path: pages/traits/morphology/black_pigmented.html
    sha256: 904908575e4e0b4577077521dd4a701466ccda8be1239edb813b2297e8ea5a19
    role: context
  - path: pages/traits/morphology/branched_shaped.html
    sha256: 2120a5b2f390d8d8d27d4b47814eaa4e544c0045ac7362e223d07d42dc8fc481
    role: context
  - path: pages/traits/morphology/brown_pigmented.html
    sha256: aa89b3a0f58559239b6db82eef87f3db1d2a792c248b71ddd25f63f2550398ff
    role: context
  - path: pages/traits/morphology/capsule.html
    sha256: 46e326c30554e23be6325004b5799b560830a5e20d56628e76830511eb934642
    role: context
  - path: pages/traits/morphology/carboxysome.html
    sha256: 7cfde4d6a24f0c85e0b712e0a81ceb0e20f8fda195fe3262f265d8ccfb2bfe9c
    role: context
  - path: pages/traits/morphology/carotenoid_pigmentation.html
    sha256: 1556b47d744c1c02cbe4eb337b4f984b55ecc730ffbff4d5ea4b7c0b431cda98
    role: context
  - path: pages/traits/morphology/cell_length.html
    sha256: 53dfd3d7b642530acf932fe9f62281ba01e7f88edd0ce6495d4da819bb81d0b4
    role: context
  - path: pages/traits/morphology/cell_length_large.html
    sha256: 0fd3ce42014330ec6d4670ae8ed468db62297fbd0807efb16d3de30aa3129dba
    role: context
  - path: pages/traits/morphology/cell_length_medium.html
    sha256: 808f5e9338228a41c2fc83ab6cc3a8bdf4b383b356370f3b6a4946700aab82ea
    role: context
  - path: pages/traits/morphology/cell_length_small.html
    sha256: b3d77d1293d9394061fa48c49416a32f371201065068cebc3186bec8b3832a89
    role: context
  - path: pages/traits/morphology/cell_length_very_small.html
    sha256: 62b40227d1f4b03fffb17df91595ff7c4d9f9357cb574f35548e2e3176725502
    role: context
  - path: pages/traits/morphology/cell_shape.html
    sha256: 30034eb9850ade6075fa7c4f6261a5cf36228bbd49f471fc0e0c3209b0e564ce
    role: context
  - path: pages/traits/morphology/cell_width.html
    sha256: 9c727ce82935780f8b4f89c07f393386e3e3f6d10dc04b63e5869a4b483be318
    role: context
  - path: pages/traits/morphology/cell_width_large.html
    sha256: 7945a62215d9636269a05a3c13a8baa1fb627338060aea0a6aaf9a0181c8f060
    role: context
  - path: pages/traits/morphology/cell_width_medium.html
    sha256: 1525dbef0fefb7717d46af398ac60c10bc716810f1c38e74224dc19e93acdffe
    role: context
  - path: pages/traits/morphology/cell_width_small.html
    sha256: a025953ef157d82388ada1be1fdbcc5a5b47f0e731be58a0c49c18871506be6a
    role: context
  - path: pages/traits/morphology/cell_width_very_small.html
    sha256: 6956789c8f1fed6aa3a3a6e182fbb5d653a36bf8bbdd145ada2f49e8c3e9adab
    role: context
  - path: pages/traits/morphology/coccobacillus_shaped.html
    sha256: 37a5a8dc8933494b935b20b31ec444809ea92365c4aadd3fe59e87d7bc207932
    role: context
  - path: pages/traits/morphology/coccus_shaped.html
    sha256: 1e9e8fdb7823ef9a9a9d55e7e2ae36882de6cd5cac537cde3bdcf7b6ecefa9f2
    role: context
  - path: pages/traits/morphology/coenobium_formation.html
    sha256: 5e88923eda8d7e9661ec6b005a5163af665a3012851c3a404f1083f43f7d15e3
    role: context
  - path: pages/traits/morphology/cream_pigmented.html
    sha256: fa980211c72655d5335b871bf6d20cb3397f44b1b5e0ba1ee7d610fef91dec91
    role: context
  - path: pages/traits/morphology/crescent_shaped.html
    sha256: 9f8a239b227db9ce9ff945a8850dce97c6e9f4bd9614382cf14fc3c453a00c7c
    role: context
  - path: pages/traits/morphology/curved_shaped.html
    sha256: 2ee1d383833131891a00f68faf22d9699e7968643934a6c61d7887456937f48d
    role: context
  - path: pages/traits/morphology/cyanobacterial_multiseriate_trichome_formation.html
    sha256: 4a40ff909ff932e2c2afb6ddf6cfdff8dbdb7da3399dcbaec882a057b05b58dd
    role: context
  - path: pages/traits/morphology/cyanophycin_granule.html
    sha256: eb90cdded84885b4298b08c038ed46348480323a18056a1f94605816c055d32b
    role: context
  - path: pages/traits/morphology/diplococcus_shaped.html
    sha256: f8078d98c8af680aad06c982b70eefdb0c18fb76bd6276bf1ced15f81600652e
    role: context
  - path: pages/traits/morphology/disc_shaped.html
    sha256: 76280ce149a975f1e2ecf7a7c17b5b7619b74a992e496985eaacf7881b308277
    role: context
  - path: pages/traits/morphology/dumbbell_shaped.html
    sha256: a8d7bff82e956e9ea0355c2f66519fe8422b1233bcd33d57564262132a9d9390
    role: context
  - path: pages/traits/morphology/ellipsoidal.html
    sha256: 9ab0b7a70597e2b4ec771ec8a33c16dc7477f45d33c65730e2da44cbf460aa6a
    role: context
  - path: pages/traits/morphology/false_branching.html
    sha256: df242687227dc545c91a0615746b9e544d2e1b182d660512741a3306702c06a8
    role: context
  - path: pages/traits/morphology/ferrosome.html
    sha256: 0966df32d9d69419ac7d73d3dac5ad4a3225b9accda909c385da94bc51b7671c
    role: context
  - path: pages/traits/morphology/filament_shaped.html
    sha256: 495514ca46e60c42c21ca618f20e17497e399d07e917a4e19e6875c4eafc9874
    role: context
  - path: pages/traits/morphology/flagellar_arrangement.html
    sha256: 9446e17c47d9f8e04f2fc21f0f5aae39a787eb8f753aeed7c18143a1ff6f2027
    role: context
  - path: pages/traits/morphology/flagellated.html
    sha256: c6ea15b22fa3fb282066e21cb0f08e9ff5689fa6516eac8a761bc9359c55259c
    role: context
  - path: pages/traits/morphology/flask_shaped.html
    sha256: e258d6351c5fff9c7c2276a6ca6af85ca5635461ed21fd80f9f644787d573e3c
    role: context
  - path: pages/traits/morphology/fungal_adhesive_column_trap_formation.html
    sha256: f53a3f3ea51cc755e76c2c3210750eac0164a0e4c3e7ed3d938b3ed165370425
    role: context
  - path: pages/traits/morphology/fungal_adhesive_knob_trap_formation.html
    sha256: 30e00444a61af2dadd8768bafb59176523e79e3b8e3a55b716667f0afcd73f64
    role: context
  - path: pages/traits/morphology/fungal_adhesive_net_trap_formation.html
    sha256: 45d20e75441ec933e441dc47afb184b5e0a8bc9fca28063e45f4549076ff821f
    role: context
  - path: pages/traits/morphology/fungal_appressorium_formation.html
    sha256: bd6739f4f51704dadee5c006484aea00d671653f129f08d155a678f561145a33
    role: context
  - path: pages/traits/morphology/fungal_arbuscule_formation.html
    sha256: cdc99373886817db55c0a4412bae6ef0f4fe0eec61e3eca48a81f656323ce191
    role: context
  - path: pages/traits/morphology/fungal_auxiliary_cell_formation.html
    sha256: 51b3a7f92e1885eb0e07410f53c972560bc99357dc6402848790f223cf898bb0
    role: context
  - path: pages/traits/morphology/fungal_branched_absorbing_structure_formation.html
    sha256: 6dd6aae94d4ade6b02bc9bee8ea38b6d2acbf10fdc5f5ac493360568934b77d8
    role: context
  - path: pages/traits/morphology/fungal_chlamydospore_formation.html
    sha256: e72b93b5d6d6079f6d52d87a9e651f40815f5d35955046ae5e0fe726a65ef5d1
    role: context
  - path: pages/traits/morphology/fungal_conidiation.html
    sha256: 59ee3d9c7d33620986333f3739163a2f4be3aab70665941f67f38a8883bc5dd5
    role: context
  - path: pages/traits/morphology/fungal_constricting_ring_formation.html
    sha256: f401f4b750d7aba4279a1d86030b7498219af557937e1bf22a7481980fc3b0b4
    role: context
  - path: pages/traits/morphology/fungal_hartig_net_formation.html
    sha256: f3271f1255f82684f828ac9e9d1cd17dd03a979b29d801e64d96c743ca3c7915
    role: context
  - path: pages/traits/morphology/fungal_internal_mycorrhizal_vesicle_formation.html
    sha256: e84391b4a909b3e7f9b10c97c590e5c713fd2a77c00037227307c740417d9ea8
    role: context
  - path: pages/traits/morphology/fungal_mycelial_cord_formation.html
    sha256: c9448d2c8f44117fc3453e78a3a48a58cb74e3df5a6ff4b129b4c162db87e58f
    role: context
  - path: pages/traits/morphology/fungal_nonconstricting_ring_trap_formation.html
    sha256: dc0efa43552b59084eadb828c78b1a56abb73a28a41b74a3936462ea5eae45b7
    role: context
  - path: pages/traits/morphology/fungal_peloton_formation.html
    sha256: 3f7eed4c3e92b7159976e344372c7cf755e96698484c1002e096a53e1b2c2497
    role: context
  - path: pages/traits/morphology/fungal_rhizomorph_formation.html
    sha256: 3caea4f247caca226447ed9e7a6d8981f417b9e3749caf903b933d6a255f0ca5
    role: context
  - path: pages/traits/morphology/fungal_root_mantle_formation.html
    sha256: 95d8fdd133606113165a60486a23943f7857a9bae9b8f0daeb121e4c0cffa8bd
    role: context
  - path: pages/traits/morphology/fungal_sclerotium_formation.html
    sha256: 8dd1c15f0307dbb15e7710fbaca4524c8477f92a709ea3314e712a28dc9bd5a4
    role: context
  - path: pages/traits/morphology/fusiform_shaped.html
    sha256: dad92bba8458dbd8bc1adb1cbb5e5ccc39567f99056d6f503bebfb1c773c7fd0
    role: context
  - path: pages/traits/morphology/gas_vesicle.html
    sha256: 834bbb43e2ae9ddba9f82f98c5fad51abffacf9f23df127830da303fe269f7e2
    role: context
  - path: pages/traits/morphology/gliding.html
    sha256: 8412c21d6972dc8a73937dfd0576eabc435f82a2993683af37bdd0bb2c772321
    role: context
  - path: pages/traits/morphology/gram_negative.html
    sha256: 279c0241b394d66cb3dd8bc7067d728a7ab7a21e0ce04bbc196a54330c0de951
    role: context
  - path: pages/traits/morphology/gram_positive.html
    sha256: e8380ac6c950f7f79c8d94544ee1f07974439758d20b52223beb3900d916fb07
    role: context
  - path: pages/traits/morphology/gram_stain.html
    sha256: f44caaf7fefb9cd988e61c1f16746a5c3b23ce999dde30288ab8186ff1410f06
    role: context
  - path: pages/traits/morphology/gram_variable.html
    sha256: 7cf8a5c4c379d162f6c4eefdb10b03e4a7181c6af9a9d51e46b781f8b8c8b878
    role: context
  - path: pages/traits/morphology/green_pigmented.html
    sha256: 1aa679bc12495a746a188ebf06ee8020db5da80a5d9153a8294bd4b0bb64457d
    role: context
  - path: pages/traits/morphology/helical_shaped.html
    sha256: bb35cab204e80182fd6dc4b70b5d2088435c90ea61861f383d741c578f9f2905
    role: context
  - path: pages/traits/morphology/heterocyst.html
    sha256: a8a8847424db0715c1c03a902cf374506a0d5231a96aba43ab8697eae4ac9249
    role: context
  - path: pages/traits/morphology/holdfast.html
    sha256: e40a39e1e09e4a3f3bf06429312e370c5390b4056b94c444fd79f31b49cc52e4
    role: context
  - path: pages/traits/morphology/hormogonium_formation.html
    sha256: 81dcae062b473e84c0a8dae8b47d0532a18a55678d43eed39592673d26bb2560
    role: context
  - path: pages/traits/morphology/intracellular_inclusion.html
    sha256: 331ad049c02d35f2bc60b317850c4be3c912335a777b7ab925dfbe1b233ed8a5
    role: context
  - path: pages/traits/morphology/irregular_shaped.html
    sha256: 139f30b15d5ba5c68dce40f9efba9b7c1379e01654837290f0cdaa5d60c81bf8
    role: context
  - path: pages/traits/morphology/lateral_flagellation.html
    sha256: f85a9d62b001ada5c955123b42ff2d17a79de384681d8ca11e7af2a8f2c5a165
    role: context
  - path: pages/traits/morphology/lophotrichous.html
    sha256: 1727e278f29afbc795316916eb52f0d17764e9471f64c66eeed1434d84b5196f
    role: context
  - path: pages/traits/morphology/magnetosome.html
    sha256: 9e6cfb2b9a6ba6a812c186376fb57c3efa9588efe13feabc4fe5e952d7fea48c
    role: context
  - path: pages/traits/morphology/microbial_haustorium_formation.html
    sha256: e523aa9d41438ef685479b0bf93c9e01a19c84a5c63b5e019858b702bcd1da93
    role: context
  - path: pages/traits/morphology/monotrichous.html
    sha256: 6b87467adb91af6b7bdf799386b2fb8a9682e07d3e11fc9ba7b25d4d741e4717
    role: context
  - path: pages/traits/morphology/motile.html
    sha256: fccd81034b020591bdba6d5ee32dcffc01be1519912a444dc8c56411a6a6b7c0
    role: context
  - path: pages/traits/morphology/motility.html
    sha256: 6eac3429dea84d95816caf8b8d651488bfded15bae0f9ac4189822d2e9ad361c
    role: context
  - path: pages/traits/morphology/mycelial_growth.html
    sha256: 334ac18bb9f88d87aab7269157583f62afc6b86a71f0028a7bfc1a3ed7b04e73
    role: context
  - path: pages/traits/morphology/necridium_formation.html
    sha256: 861356b4607920cca015fd072b4e77ffc7b8958a3a691287a0b84fbb85409866
    role: context
  - path: pages/traits/morphology/non_motile.html
    sha256: f9a9058a7576c07a5dd3b22240e010f1f5f3dbdbb8dd1bb97e678bf491eb74f3
    role: context
  - path: pages/traits/morphology/non_spore_forming.html
    sha256: 8c4f302ac26d70f1c8bb50352b3e19ca2d4ddf36ace58035f695ba8097f0d5d9
    role: context
  - path: pages/traits/morphology/orange_pigmented.html
    sha256: c98e2fdac49216637673aee18c59d55e7b4e08c125f0f5fe8bc2b5a292bf8771
    role: context
  - path: pages/traits/morphology/oval_shaped.html
    sha256: 92ad91224492f99e3dc2620a23b7dfa5957b83a6443caef2b86420275c85e559
    role: context
  - path: pages/traits/morphology/ovoid_shaped.html
    sha256: 5b874ea40e630e8f1c546ac9f79425399ec8d7effa21c872fdf9f8d8652d6c12
    role: context
  - path: pages/traits/morphology/palmelloid_formation.html
    sha256: 3f265e1c7682c7aefe9b4f7fbb0b200cfb4318559c18dd8dfa9e535e25bcd8e3
    role: context
  - path: pages/traits/morphology/peritrichous.html
    sha256: 8a93f9a0d94490f2f34fb9b21c2e859d12c354b209181720135f8fb2d5afe6f4
    role: context
  - path: pages/traits/morphology/pigmentation.html
    sha256: 3dc1cd4d2de82aaf521c94876d3a5cb490e30a1db8f718e6b30e519e0e3b0faa
    role: context
  - path: pages/traits/morphology/pink_pigmented.html
    sha256: 202671bf4b223013198929951030faf2b818bd61e29421bce380a1422d85f057
    role: context
  - path: pages/traits/morphology/pleomorphic_shaped.html
    sha256: 9790bbe9d9f8656604f03b3f34e6aec95f27f2f432330b4f1aba910c6791fdfd
    role: context
  - path: pages/traits/morphology/polar_flagellation.html
    sha256: 04dc23a14381ea61725e6857f76db00c86b5da75fbd9cf3699c6cc017164d93b
    role: context
  - path: pages/traits/morphology/polyhydroxyalkanoate_granule.html
    sha256: 82cb2ea97e1fd4f9b965c657658c0d394ec0587c3d698beadb805fc52a52ea6c
    role: context
  - path: pages/traits/morphology/polyphosphate_granule.html
    sha256: 82755e2cfea2b64978dae83c8f910f51766a641591b12f9784db33e253f44091
    role: context
  - path: pages/traits/morphology/polytrichous_flagellation.html
    sha256: 68ce6d25c24328250181e90ccc45b6111ba5524919e736b5b13a3d0a89d5d057
    role: context
  - path: pages/traits/morphology/prosthecate.html
    sha256: 3de29cb86b6fceb1a20525b698d7f1eeca073f8ca16e14edd78ba40a5f3072c4
    role: context
  - path: pages/traits/morphology/pseudohyphal_growth.html
    sha256: 29c9d86b837c2ad020ec608d33cfba073af39a74f705c00e59e56aabb2665e96
    role: context
  - path: pages/traits/morphology/red_pigmented.html
    sha256: 6ea480bacdf97f3467a2e5884a69fa40808a9814e6659fad3987d0d972176b3e
    role: context
  - path: pages/traits/morphology/ring_shaped.html
    sha256: 416eea402352c4c7de68b022964d54afc1b1404e46a818bf2d756847740210de
    role: context
  - path: pages/traits/morphology/rod_shaped.html
    sha256: 6e3a78d787b783458c61d966a5fcfc51b74403b86e91420477246fcb6b9fd1a1
    role: context
  - path: pages/traits/morphology/rosette_cell_arrangement.html
    sha256: eac75ebc5cca139a61bfb2179d897d1ec113be2d9337037df3c2e2e51d167a8b
    role: context
  - path: pages/traits/morphology/s_layer.html
    sha256: 70bf2788543c507b10646486cf9a02a0f811802e2dfb7fdaa298babb8727ce19
    role: context
  - path: pages/traits/morphology/sarcina_arrangement.html
    sha256: 23b1b4e0547abb3395759fdb8d3d42686358ab9836232e36fb82992f2370bec1
    role: context
  - path: pages/traits/morphology/sphere_shaped.html
    sha256: 52c4a56494e82f14ae7bf2cf19cabcafe6ff4f34d3797837718cbe128e6b82cd
    role: context
  - path: pages/traits/morphology/spindle_shaped.html
    sha256: de70c8882f9a42ddc1c905bce33477e22172356025e4c4e06d1d894d0c86ddde
    role: context
  - path: pages/traits/morphology/spiral_shaped.html
    sha256: f55c5d00d67c90be7918d89a9f06f158fd51799b0e03292e55bbec2e37517496
    role: context
  - path: pages/traits/morphology/spirochete_shaped.html
    sha256: bd5c76f4efab08675ce704665baf7377ed968fad042d8320c45f6c656132c990
    role: context
  - path: pages/traits/morphology/spore_forming.html
    sha256: 440f5bd081139b2ff86fa809c47377582f4c4917a3ba60bb8a2cb064312c2c1e
    role: context
  - path: pages/traits/morphology/spore_shaped.html
    sha256: 3e6ed62f74c1e56de5aa588c1aaf09c141d638ab5e5dff0b566e1b55dd7e9cd0
    role: context
  - path: pages/traits/morphology/sporulation.html
    sha256: b72a64c24f620f54249afb9af90cfcbdc88e80b119db55d356d77c799739cecf
    role: context
  - path: pages/traits/morphology/square_shaped.html
    sha256: 8084dd978af7d7d59feca7703fd2c9b3e6e5812aa10a18567a645771572c0837
    role: context
  - path: pages/traits/morphology/staphylococcus_arrangement.html
    sha256: 367317630dfb5a65afe72bcab876feb3935e51a706366afce096223e164af382
    role: context
  - path: pages/traits/morphology/star_shaped.html
    sha256: d664eeaad0b9508fa0d6077403c89d25e77206f6bce89fe76a089b644e2fb98b
    role: context
  - path: pages/traits/morphology/streptococcus_arrangement.html
    sha256: 1d93c55a847b95cdc2a7936e41dd7a17f5a5ed44267539d9a13807b5ffb6bc52
    role: context
  - path: pages/traits/morphology/subpolar_flagellation.html
    sha256: 24e3e7bafda5b2489e09d208b28a1c55641038eff2e8d62d27f8d3757ee21fc8
    role: context
  - path: pages/traits/morphology/sulfur_globule.html
    sha256: 5d2a4de05e10b358e6a19d0febecc1979101ce3ae5c8ef3f932a0a45bcca5199
    role: context
  - path: pages/traits/morphology/swarming_motility.html
    sha256: e5edc7c57a3661cc21441eb6a2fbde2e04c6e73cdecc5b298dce703d5af5ada5
    role: context
  - path: pages/traits/morphology/synnema_formation.html
    sha256: 15a17e34a2cc3c5f0b6ec7ded12717bbd47f921237d0eae025d05c6556f1b619
    role: context
  - path: pages/traits/morphology/tailed_shaped.html
    sha256: ae67a5568b6386867a53a4f060376f5f3b362c73e1178e72f8605cd270aff462
    role: context
  - path: pages/traits/morphology/tetrad_arrangement.html
    sha256: b953ad71271ea32d5ac9dc1cb15bce131b1f618b6b4b939bc6cd4302556de7cc
    role: context
  - path: pages/traits/morphology/triangular_shaped.html
    sha256: fb5ce0cdee53cfd3bcf3095a4c73790d5b67b8e2c549c2dd1f971cad018efadd
    role: context
  - path: pages/traits/morphology/twitching_motility.html
    sha256: 618d4d6548ee36b40c9e929994ca5697f82dfad7f4a7864b52fa571f999bd499
    role: context
  - path: pages/traits/morphology/type_iv_pilus.html
    sha256: 7651ba0c84d84105d0d6a64f0c1df3b5dc8902e79352288e5f06d1cf291d31d0
    role: context
  - path: pages/traits/morphology/vibrio_shaped.html
    sha256: 7c978e44837a39fb000712f95d12c552def43c39f9d4683cf3b72e6b56edebd4
    role: context
  - path: pages/traits/morphology/white_pigmented.html
    sha256: be5f7f3edb7d949723e3f2aa637b0a5defd1c1c82072df7ea5441e3afb761836
    role: context
  - path: pages/traits/morphology/yellow_pigmented.html
    sha256: 03b849adc8b0bdf7a896383e6fad8491dd1f946c1a42a3eef2c82897afa396c1
    role: context
  - path: pages/traits/observation/growth_nacl_observation.html
    sha256: 4af5712f372dc25d7dbc63cf0eedee33bee8b2d3ba691829e522b78f7be7fbcc
    role: context
  - path: pages/traits/observation/growth_oxygen_observation.html
    sha256: cffed775469e6fe29baa51fa69aa1195b8eafca8e31ef64720937bd22320a11b
    role: context
  - path: pages/traits/observation/growth_ph_observation.html
    sha256: 02a92dba92644246febfba538f33437f77b41c5e9b0c83b875d8012506b56399
    role: context
  - path: pages/traits/observation/growth_temperature_observation.html
    sha256: 02f7c66d125dd06e7c86783c2eb0dcbba10fa295d73c39a50ae3315f9d39e63b
    role: context
  - path: pages/traits/observation/nacl_delta_observation.html
    sha256: bcb44cf78a83ff76463f83d62aa144b1450dd9d1d6c68b0fe4055e918bdbb1a9
    role: context
  - path: pages/traits/observation/nacl_observation.html
    sha256: 63118d63a4dd45b19801133957a0003e4527fa3bcd3b44a1102ad8e678d3800f
    role: context
  - path: pages/traits/observation/nacl_range_observation.html
    sha256: c124c1da21778d62db4d4f726458f7ae9be7815496f7b9c8d9cad7a735e6532e
    role: context
  - path: pages/traits/observation/optimum_nacl_observation.html
    sha256: 64ecdd89136140c6af2af3957d3798f5cd1b410f4c8619c28dd79ea443d39bae
    role: context
  - path: pages/traits/observation/optimum_oxygen_observation.html
    sha256: 93910d84553a42959f1455aba8e217c399ed9c07cd9c7ab96f8a970289022fb9
    role: context
  - path: pages/traits/observation/optimum_ph_observation.html
    sha256: c286cf0704f81ecc84298fb8fac878b516c40f81345d95840b83ecbbdce8a698
    role: context
  - path: pages/traits/observation/optimum_temperature_observation.html
    sha256: 5f5f8fc79a18f869943d8e61122a38022dfd122f1e064134be1a5058bdc02009
    role: context
  - path: pages/traits/observation/oxygen_delta_observation.html
    sha256: b692a934e1b972c81ddb2793cbad9acc94c74c9d56e5b787034f30759d238055
    role: context
  - path: pages/traits/observation/oxygen_observation.html
    sha256: f6182f77e90828c4698732e588b39526c7fdefc20c167c95cd35e4c478f7fdab
    role: context
  - path: pages/traits/observation/oxygen_range_observation.html
    sha256: bbf5b5a86da417e5b79b01a56a32fdab63ef3d6cd9c71261d19d55cd21b1425d
    role: context
  - path: pages/traits/observation/ph_delta_observation.html
    sha256: 60ebf9d00f5d0d705709d1186f459801e6df9d65acc020a2bed68a4d46c8c8c8
    role: context
  - path: pages/traits/observation/ph_observation.html
    sha256: 6afd282c04541cbc186e61ce86505cc45bc9ecb6ba8f66c68423dc8e5a4467a3
    role: context
  - path: pages/traits/observation/ph_range_observation.html
    sha256: 9f988adbe5267838688edd99b60184e5a44edee2447d8fb671da5115dd8a529d
    role: context
  - path: pages/traits/observation/temperature_delta_observation.html
    sha256: 579d268de02db00daa0a355a9019f2d87a0bb2bf10e317d22333911e49b16d43
    role: context
  - path: pages/traits/observation/temperature_observation.html
    sha256: 638be19a714b87afcc64f8f46a04eb16ebb175d574470581cde90278c8e70675
    role: context
  - path: pages/traits/observation/temperature_range_observation.html
    sha256: 44f059517a0cb523fea3fe99ac80782114d2b2269aa054247c57a2190871d4e6
    role: context
  - path: pages/traits/other/catalase_negative.html
    sha256: b985e65b3de1af9c2f0f4c47c3f02d5110b271c3687083a45cde22cc20412203
    role: context
  - path: pages/traits/other/catalase_test.html
    sha256: ce036cb3de77309418cae201f8dc81f3d0967678c50f641d482be1560f78a469
    role: context
  - path: pages/traits/other/circular_colony.html
    sha256: fdcf1cfa50e895343d1bf011052d0b5ba56b5ed819738c31b639e9da3f89b602
    role: context
  - path: pages/traits/other/coagulase_negative.html
    sha256: 60ac505c5a2585227a13bf7657c689f1a1aaae6c44a3901e7246d174e8919020
    role: context
  - path: pages/traits/other/coagulase_positive.html
    sha256: 40800e241f143d61583674ab481e1eda6acb987b8c1f10ade4eb95dd4ae5f98f
    role: context
  - path: pages/traits/other/colony_morphology.html
    sha256: b3fc218cd7eee5791da1e1d4ab0abcf0ff3d1cb533d54a555e39e82e39027eb4
    role: context
  - path: pages/traits/other/colony_shape.html
    sha256: e9d7c8665efefa9fb195d8449d0f5426832436647c83cec890e14bc0508d0013
    role: context
  - path: pages/traits/other/epibiont_phenotype.html
    sha256: 0b38aeb216756a4732b3da7460f6a0b6810eeb06bb06a5e047712956bedef9e4
    role: context
  - path: pages/traits/other/filamentous_colony.html
    sha256: 2192ac0f072f34a0bbef631cefb3c6136d600349ab69d5f08e24ca2dc1faa4ce
    role: context
  - path: pages/traits/other/fried_egg_shaped_colony.html
    sha256: e1d0919d9023021840cf5047c0bc4907c09a5cd684de02c096d14bfbd427cb42
    role: context
  - path: pages/traits/other/generalist.html
    sha256: 42e10a3eff3eed1919cc2b470c8243b423b854a97c2bf193cde74c495a1dad37
    role: context
  - path: pages/traits/other/hemolysis.html
    sha256: 954081731690ae7aca914a8c97acf12086527fa322c22edc8c8ad91d05beebc9
    role: context
  - path: pages/traits/other/hemolytic.html
    sha256: 4fe2c933c965f702a92d4cfbf02d5934b34dd4533ef01057dfb0f0709a06d620
    role: context
  - path: pages/traits/other/indole_test.html
    sha256: bcd0fa89c39fbd3c465883b3c0b12485204df7b376b80cd2502872a4cf6e6ecc
    role: context
  - path: pages/traits/other/indole_test_negative.html
    sha256: a2e44d0eb4afb2f3e42ba4e31844a2a811f43122da6d3da602b4d4f378c4ae8e
    role: context
  - path: pages/traits/other/indole_test_positive.html
    sha256: 0511315b550d526f8331b7802797d8d10252ab11b9beb38cc8ff4d428757ed2a
    role: context
  - path: pages/traits/other/irregular_colony.html
    sha256: d86ac4912af8745a9f255d9e4b67e9c1302a994ff7f3f017e532782c78ee37ba
    role: context
  - path: pages/traits/other/methyl_red_test.html
    sha256: 79768bf1a70a153cd1e484650a38c36638aeac25bc1fb1938946238f9a989ff7
    role: context
  - path: pages/traits/other/methyl_red_test_negative.html
    sha256: 7501b4ce5730d083c130044c1e68d07f3929a3a92017e7c0e16526cef9b4f18d
    role: context
  - path: pages/traits/other/methyl_red_test_positive.html
    sha256: 038821aab065aae4b8563557fd86f430ae0a971f9031ab5d82c2fae5370e0289
    role: context
  - path: pages/traits/other/non_hemolytic.html
    sha256: 3aa88b54c1787baaabf42c21922a03d942b0a3faf4ca3003f8e144bfddb6f447
    role: context
  - path: pages/traits/other/osmotic_tolerance.html
    sha256: 2c1c73ab6af5c29d138eb23e26b436e9dde92fed090f3c9cf15d3bf804960af7
    role: context
  - path: pages/traits/other/oxidase_negative.html
    sha256: 67ff3c4c97401c0c86a5de6640392023a72bbed4bbe1bd8b78d7f11eb8033f9b
    role: context
  - path: pages/traits/other/oxidase_test.html
    sha256: 0f8265e5a77f428298afe63b173f94b4d074347a002fec39838a3293bbfe0374
    role: context
  - path: pages/traits/other/punctiform_colony.html
    sha256: 68c723ceed082c2f655b317b5974b584ea89e139276dcd9d82494fb119ed5e43
    role: context
  - path: pages/traits/other/rhizoid_colony.html
    sha256: 460ae2ad2587432fd334ee7d570c6c95648e746434a2b66173353b86eeb6992c
    role: context
  - path: pages/traits/other/specialist.html
    sha256: 66875826d4d6769e2e28c11854c86fb170ef39ee9cba134d3918938afd177d87
    role: context
  - path: pages/traits/other/urease_negative.html
    sha256: f8f153a44d9877bba2bbc86aa38d65a929d05310cac6a78c70eb9fc9109da9d8
    role: context
  - path: pages/traits/other/urease_test.html
    sha256: bbfa69691b736e78f496f26147d778ed79883a01622784ba8af9204d67654401
    role: context
  - path: pages/traits/other/voges_proskauer_test.html
    sha256: 5d9107d789996e1e0d57c0705d82e33851cac7a146fc27faace9f5784ff44c0e
    role: context
  - path: pages/traits/other/voges_proskauer_test_negative.html
    sha256: 83d52e3d4d1287db04bf30ec845ebff9227a7d0678a006ad414736db0b057e28
    role: context
  - path: pages/traits/other/voges_proskauer_test_positive.html
    sha256: 478714036dfef1fae7361ccb783ec4a5238ecd89cbd95c19d8d3c72391b5ca88
    role: context
  - path: pages/traits/physiology/acid_phosphatase_activity.html
    sha256: 5e95b7cfd58c04640c7165affbe804bd9349b33aad7d83349813b46c03ff8cb9
    role: context
  - path: pages/traits/physiology/aerobic_anoxygenic_phototrophy.html
    sha256: d965f25b3eebe52ae6518d61c0b47e640b5ca6e2aa8d4f881afc97dc21062464
    role: context
  - path: pages/traits/physiology/aerotaxis.html
    sha256: 76210824f12eca27aa24202a931bfb6fccb773e6562dd9b87451922da5b059b4
    role: context
  - path: pages/traits/physiology/aerotropism.html
    sha256: 143e07df3351e59dabec94a0eaf41b020ee31e1ee5f0d35f784b458498f823d4
    role: context
  - path: pages/traits/physiology/aggrephagy.html
    sha256: 4f06d95e97553ee97badfa48ffee12232da9f119ba20acf684503c28138f9966
    role: context
  - path: pages/traits/physiology/alanine_arylamidase_activity.html
    sha256: 78b34a4b1ecc13d6c5ffbd83d3ccdeba9f9ab845dd473c4f0bb81f1f0642a548
    role: context
  - path: pages/traits/physiology/alkaline_phosphatase_activity.html
    sha256: a3a875d0eebfd72f79a8afc22cf7801d3ef545772e4db42382979b5d500e67a8
    role: context
  - path: pages/traits/physiology/alpha_chymotrypsin_activity.html
    sha256: e23a63068f837ad919babf9451e2fa0517d54b4f750b3656586319fe5d54b415
    role: context
  - path: pages/traits/physiology/alpha_fucosidase_activity.html
    sha256: d8a5f661dc843e0a51665e2de3b9ed8563abc8526accdab234cf0da09181319c
    role: context
  - path: pages/traits/physiology/alpha_galactosidase_activity.html
    sha256: 22887fcdb5ea1291cc9f9be3bfb9605628e9306eee3a0ba67af58c83759262d6
    role: context
  - path: pages/traits/physiology/alpha_glucosidase_activity.html
    sha256: 8fe795598aae1f36e345f617dfe10cd6efce2dfa20ec977c7f7e3beb3c65ce86
    role: context
  - path: pages/traits/physiology/alpha_mannosidase_activity.html
    sha256: 09636dff6d7b76a8976eedfe6e95dbc94942706eeb7e4a3fbfee7bc4c4f63234
    role: context
  - path: pages/traits/physiology/amylase_activity.html
    sha256: 8fd87538fbb52e624c78d3d0314a482ca903271c64d40c51c99495de36130fcf
    role: context
  - path: pages/traits/physiology/anisogamy.html
    sha256: a48fea29db872e7631cac026b443ed75492c32d7da5d5913920ce32848fecd33
    role: context
  - path: pages/traits/physiology/antibiotic_resistance.html
    sha256: 1b8fdcc00e6bc962f87c6c00525187c3aadb5147172b546a45c362d502c8e2c4
    role: context
  - path: pages/traits/physiology/arginine_arylamidase_activity.html
    sha256: cc220af43b0904e44eedd6f297cab4bd086e7b80ebd3c84f766bb79e4a6e3b42
    role: context
  - path: pages/traits/physiology/arginine_dihydrolase_activity.html
    sha256: a03692e59432b7981fcd116003db6a20435725b0dbb0cf7a39d7f5a054485e91
    role: context
  - path: pages/traits/physiology/autogamy.html
    sha256: 330b45717a2b09e6dcd15562f19a6cbf26207b61eeb347108184c4009a5e127d
    role: context
  - path: pages/traits/physiology/automixis.html
    sha256: ab3dc39c2fdeee2c9dd56dbcf72ce61f708116c3f6516a04c8d1e79ea1926089
    role: context
  - path: pages/traits/physiology/autophagic_glycogen_degradation.html
    sha256: 1431ff435a14519905cd16ddadc069c61a19eaa35e42daf3667ebd19c07bc815
    role: context
  - path: pages/traits/physiology/autophagy.html
    sha256: 5d35ef755d3a293d70fdfa79200ea1a8f4ce16a314647b60e80c36c7e7a57d35
    role: context
  - path: pages/traits/physiology/autotrophic.html
    sha256: d1c5941eefa430e118f5395b61d5080399244aeca19ea34c0d6685471b665157
    role: context
  - path: pages/traits/physiology/bacteriocin_production.html
    sha256: 5d53e997126e805deb8747e6e95c07aa542c2af7a5aa16d166a35695ccf97010
    role: context
  - path: pages/traits/physiology/ballistospore_discharge.html
    sha256: d6ab59f99dc30a741e699abe86738a23f5f690d0220fdcfdf69e0593b766682b
    role: context
  - path: pages/traits/physiology/beta_galactosidase_activity.html
    sha256: 2e2e741b2a6b468315d70f4ba59ebeae00a6a668d978dd95ea017c530263a9d3
    role: context
  - path: pages/traits/physiology/beta_glucosidase_activity.html
    sha256: 1b367e93a6d47c1a3fad9818da7a0d5c2a27a96e9db79b576d8027c96d4c54c9
    role: context
  - path: pages/traits/physiology/beta_glucuronidase_activity.html
    sha256: d549089172b3795be651fa7090ac29485042efed0ea320a0bbc67e36201b725b
    role: context
  - path: pages/traits/physiology/beta_n_acetylhexosaminidase_activity.html
    sha256: cab47db49a1312b73881d4858e4bfbc5f273c8eb58b3a237de01927d6a69c21b
    role: context
  - path: pages/traits/physiology/bioluminescence.html
    sha256: 3da3452283e0d36ae2bf6e9926393fd2635f9bba4e609371a62da9cda4447801
    role: context
  - path: pages/traits/physiology/biomineralization.html
    sha256: 5428597335dd439d4d91a760f59afbb508f785e9525265ecdd1a9f6b5f5d5781
    role: context
  - path: pages/traits/physiology/bipolar_mating_system.html
    sha256: de29c388be718f2ddd8959be2bdf37a66c9ab45d7ac99d78163234bf12ac8b77
    role: context
  - path: pages/traits/physiology/carboxydotrophic.html
    sha256: 444ef5e214825817b85a746c6225e441c9e9706648b5b2b639720ef62b9420e1
    role: context
  - path: pages/traits/physiology/carboxylesterase_activity.html
    sha256: 21a910e7b174d8932f14d1d126148371d9422366cc097b31b73d2b40a2a483c3
    role: context
  - path: pages/traits/physiology/caseinase_activity.html
    sha256: 1e6cd95d86935e5976b2938dbabfeb80e85ca6ad0d9d1a1275638a62cdd83223
    role: context
  - path: pages/traits/physiology/catalase_activity.html
    sha256: d747482517f8b91a21dbd3ca6839dfcbd9672bab2e6b219e16dd2c4d91d96228
    role: context
  - path: pages/traits/physiology/cellular_buoyancy.html
    sha256: e7ad4f12a96278cf599ae2dec65a5f078325ff40dd230ffa75d4addd2e428948
    role: context
  - path: pages/traits/physiology/chemoautolithotrophic.html
    sha256: dca0830b83b696c8ddae0a7691b05d4e52cc6444b91d3f3af93bd2fc82cabfe9
    role: context
  - path: pages/traits/physiology/chemoautotrophic.html
    sha256: 8137133c919801a4ce8b426bf0e4c31ee0eb81aaa4f0fc4d00b9a4bc76cde9a9
    role: context
  - path: pages/traits/physiology/chemoheterotrophic.html
    sha256: cd7ff83df27b77669ee30d8456188835c6fffcc363392ffc6fe2a93664270d99
    role: context
  - path: pages/traits/physiology/chemokinesis.html
    sha256: 6ce8474aa02a61ad6d29095f28649074daa7b3c3e9303ec7e0d47fa91652597d
    role: context
  - path: pages/traits/physiology/chemolithoautotrophic.html
    sha256: ab151dde223d3c9c449ae0435c80c73d7110673318fe9d73e84eca6f065f24f5
    role: context
  - path: pages/traits/physiology/chemolithoheterotrophic.html
    sha256: 03b3dd0f265719a6a4d0f993fe32a9b7afe89c6e2455611d3ecd9bd109d85dda
    role: context
  - path: pages/traits/physiology/chemolithotrophic.html
    sha256: eab01be20da1014a6b0e6a3002b038e9db1f1f0538e633d04eb8278402bc7e7f
    role: context
  - path: pages/traits/physiology/chemoorganoheterotrophic.html
    sha256: 673597041f8ae9fcfaa62c932858bd6c5065adb6dc5b5b75fb0b7a0d51639a58
    role: context
  - path: pages/traits/physiology/chemoorganotrophic.html
    sha256: f0c6a34f8edee5d696f45817c355b9a379f364fbab7510d98f5b2ee3d1bffd25
    role: context
  - path: pages/traits/physiology/chemotaxis.html
    sha256: 966937fc8d917f76df25b543751131f5dbba678ad5e59aa707206ea93901fd3e
    role: context
  - path: pages/traits/physiology/chemotrophic.html
    sha256: b7e90af52984d2b9d21084c911202ddf0a779b788aa1241c7f097906bed87b63
    role: context
  - path: pages/traits/physiology/chemotropism.html
    sha256: f0e43e780a6e30bc2a25e5c2ff094740f4b7fb3314a9c76219dfe3e0c7d86d6f
    role: context
  - path: pages/traits/physiology/coagulase_activity.html
    sha256: 566e1febc8dc88dc05214b53647bb346c0d3fb7743f5c4bf3dc2ac7e63502c1d
    role: context
  - path: pages/traits/physiology/coccolith_production.html
    sha256: 5cf18b03511a48d2ffab94754cc9b434919acc11f5e57d3dabbd03d0cdd25098
    role: context
  - path: pages/traits/physiology/cold_shock_response.html
    sha256: 8f135f917c9e4e532bc7e7573584d878a5a7a721c267041875287151713751b3
    role: context
  - path: pages/traits/physiology/contact_dependent_outer_membrane_exchange.html
    sha256: 8906c85d2a25ba9636097ab612ca1e710d1ed86dd6501149df3722be1865a6bc
    role: context
  - path: pages/traits/physiology/copiotrophic.html
    sha256: 18056ba50c9312501b1ab2c669f385dcbe0084e65074aae87e07a5b0a327635c
    role: context
  - path: pages/traits/physiology/cystine_arylamidase_activity.html
    sha256: 9591cedbd6cb4478fe93fe786867a888135c672497428a551999d84c5a16a095
    role: context
  - path: pages/traits/physiology/cytogamy.html
    sha256: 73131c3fb37bda1b3a0505c8226c48ea574b65da8855f2c3b2112be033abf9c8
    role: context
  - path: pages/traits/physiology/diatom_frustule_production.html
    sha256: fbe9602f96eeffd9fac106c3227b08112b9b152d657d0ebc9c5147180832037a
    role: context
  - path: pages/traits/physiology/dnase_activity.html
    sha256: 6d2d2098ad3f9c6c7f7db081974735eab1e044bc285f84cbfa8312c86e559411
    role: context
  - path: pages/traits/physiology/dormancy.html
    sha256: e146f9f24180e3bc972c473d1a57b13a1ba6eee58d64d6b6ef9c325bd1c6b0ef
    role: context
  - path: pages/traits/physiology/durotaxis.html
    sha256: af6cc027b9f3d755583105ca41aee0ba0368ae7e54703d97b4d8412977df8305
    role: context
  - path: pages/traits/physiology/endocytosis.html
    sha256: 89b7a076360e04bb0c815aa611158e2d1d941c2439cd06d593af78571525d1d9
    role: context
  - path: pages/traits/physiology/energy_taxis.html
    sha256: 546ad7ae6b52dd69fa975f6e89cafed92a68a62ec7a89cea50199c1c4df2e180
    role: context
  - path: pages/traits/physiology/er_phagy.html
    sha256: 88c9ed5c37086de048781748b1c7d7a5536fd86c98fcfd99df9cb38b38a5da23
    role: context
  - path: pages/traits/physiology/exocytosis.html
    sha256: 8ffea073895ee99faf6976ac8613a33b015b051bf780f411e7e15c40e5947d18
    role: context
  - path: pages/traits/physiology/extracellular_membrane_vesicle_production.html
    sha256: 2130e3d8931bbc0bb3165147438044665f36482d7eb2e2eb8420e73247ccdc3c
    role: context
  - path: pages/traits/physiology/galvanotaxis.html
    sha256: c08eae6c8fbf4664e7f02c79ab3a28e5a5378583413acd7d1dc2d286c066d6cd
    role: context
  - path: pages/traits/physiology/galvanotropism.html
    sha256: add059ddf02f72741d2a92207a4584605f1332acc033c20f6f9d8a43ea0d643b
    role: context
  - path: pages/traits/physiology/gamma_glutamyltransferase_activity.html
    sha256: 90a3cc060b7588ef3a28ec6904e22ae3d0eb92ef3a610f17431352d2da2846a2
    role: context
  - path: pages/traits/physiology/gelatinase_activity.html
    sha256: 5e1446750cd4e77f452da37e6236d629ba56694a4c0050651c71082ddcb38e9d
    role: context
  - path: pages/traits/physiology/glutamyl_glutamic_acid_arylamidase_activity.html
    sha256: 37b958cbdd21bf08dea8b2382b026329647ee2d3d4ee69fad96906b755791321
    role: context
  - path: pages/traits/physiology/glycine_arylamidase_activity.html
    sha256: 2b7a744c892cf27fa1e279eb0ef9b4d8ca16d95237958639971eee2c9da3385a
    role: context
  - path: pages/traits/physiology/gravikinesis.html
    sha256: 9aedaed76e4e072bda2a18afcd528d1765f76a1b2fa58efe1189285d14644354
    role: context
  - path: pages/traits/physiology/gravitaxis.html
    sha256: 87157df87a48252ddb2db60eeab659b47b19acfc33e6661b845918bf2794063e
    role: context
  - path: pages/traits/physiology/gravitropism.html
    sha256: 284defbc5d09ad379a24adb81abec9b8de51130f865c0e35b3c75f3cea9dc507
    role: context
  - path: pages/traits/physiology/gyrotaxis.html
    sha256: dca13ea8035a94c0a1f16c23e40c3abd3dbdcafec84622f15db5f3dc50948512
    role: context
  - path: pages/traits/physiology/haptocyst_discharge.html
    sha256: df6d7a4d87b9a09d78846206af5aea3133aad91022048101a8c3fb3f76b9cb4a
    role: context
  - path: pages/traits/physiology/heat_shock_response.html
    sha256: 0b963b14f43816af2249757a020b44c94ba4cef0c4f7998778ba26ed5e0f28d2
    role: context
  - path: pages/traits/physiology/heterokaryon_incompatibility.html
    sha256: 6c77317d861103cbeaf130f28eb4423f07c0422314ab11fdd458376db72bc8c2
    role: context
  - path: pages/traits/physiology/heterothallism.html
    sha256: d876ed4ff97a55281b18d2841cb54a0dbfc5632f2b1de3b4779b6be8dc674a48
    role: context
  - path: pages/traits/physiology/heterotrophic.html
    sha256: f4f7fcb5565a65a55a42fd96754b6109b7da1711929c111a2b28afbba6776447
    role: context
  - path: pages/traits/physiology/histidine_arylamidase_activity.html
    sha256: c6eda90d5e09e3ad6593004b7464c80e990661595b20e7f97df616b369de4c58
    role: context
  - path: pages/traits/physiology/homeoviscous_adaptation.html
    sha256: fabbc28d97bdabb2ad400b5f6407f6996f41f27a710f043f36054e6cedc329e9
    role: context
  - path: pages/traits/physiology/homothallism.html
    sha256: f7db723711ab70a22df0ed3c01b28132c9cf3efd0aa808b03ee3b56e123c15f0
    role: context
  - path: pages/traits/physiology/hydrogenotrophic.html
    sha256: da7359ad98e960de7f286c2ea0f702440eba83ac49551959899e143037d11cb2
    role: context
  - path: pages/traits/physiology/hyphal_anastomosis.html
    sha256: 9e26ad26a07ce81e26a0bb41ff851b5a271c9d63572fd9187c51ccae5d1325c1
    role: context
  - path: pages/traits/physiology/isogamy.html
    sha256: 0b41638ec48812416c267e881c0d73c035e083f408cba770b188d1a5bc384ef9
    role: context
  - path: pages/traits/physiology/karyoklepty.html
    sha256: 4a43130e1d842bb4804f2cce79216adc87b7609f964bea8b8f9987dfa39559a8
    role: context
  - path: pages/traits/physiology/kinetocyst_discharge.html
    sha256: c4736d543b692786be81ba7811b179d0015a3d08224463cb0760998dd81370b6
    role: context
  - path: pages/traits/physiology/kleptoplasty.html
    sha256: 6f6aa7e00a7d7c8c05142155441415048dd5bd0dc969cd3802b3ab0378663a44
    role: context
  - path: pages/traits/physiology/lecithinase_activity.html
    sha256: 1415650e3efbddb24406f3532f01db8dc64e273148a381b36928045354351bbb
    role: context
  - path: pages/traits/physiology/leucine_arylamidase_activity.html
    sha256: 6a62fcd966ae9981566560805b6a4415ee4c1b7c9b96041cadfad257acf434db
    role: context
  - path: pages/traits/physiology/leucyl_glycine_arylamidase_activity.html
    sha256: c9cb3ca09dcaedff11fae1dbc8539b16cea4397689be5fdce015a9907cafa3ab
    role: context
  - path: pages/traits/physiology/lipase_activity.html
    sha256: 0269447d1443b7bec7f9c40b0b1cd89d167d27c832606ac6396e7bd7c4c07a00
    role: context
  - path: pages/traits/physiology/lipophagy.html
    sha256: 528ae3f4c8bb6401da3855b7f8768030e603dd850fdcb81801ca6007ddba0ad3
    role: context
  - path: pages/traits/physiology/lithoautotrophic.html
    sha256: 6cfecd80da0de17af1597dd4df1c493db584d92befa0a13c0cb01f795c22ed49
    role: context
  - path: pages/traits/physiology/lithoheterotrophic.html
    sha256: ceeddfd3f104b656c5ddb8ea65b3d95ce4a131ed8114400d150967d29f39bb45
    role: context
  - path: pages/traits/physiology/lithotrophic.html
    sha256: e9df9bd4684bde373ea9e18bcd4b12a32514794310df434d68575acd9e393990
    role: context
  - path: pages/traits/physiology/lysine_decarboxylase_activity.html
    sha256: 148508f7cbb2c5a91cc2fae10531c5ad50972a2f41c98cedcd569f5095b9a0c8
    role: context
  - path: pages/traits/physiology/macropinocytosis.html
    sha256: bbd24a59ec17666869872476181db695e20384a861ebac8b820df79df710e3c6
    role: context
  - path: pages/traits/physiology/magnetotaxis.html
    sha256: 476b082a9dfa0659aee9a8da64fbd2fbc72eaac3f824139c95f35dc82c67e5b5
    role: context
  - path: pages/traits/physiology/mating_type_switching.html
    sha256: c686e993e773259f5e38db5b4531e964fa9195ec65b5f8f8133480f48c99ac39
    role: context
  - path: pages/traits/physiology/methanotrophic.html
    sha256: 73c0db159c794933257c399b99bca3c000a7341ff234cbf1626f9b0d722362e9
    role: context
  - path: pages/traits/physiology/methylotrophic.html
    sha256: cebec7733e44891063041763184c3e912e32800ed9ae8c3c32813f63a4eb3660
    role: context
  - path: pages/traits/physiology/mitophagy.html
    sha256: 58be1003126f52a6c2c025d1537ad76ea5753df5d9aaf6f909eabd31b63f9d5d
    role: context
  - path: pages/traits/physiology/mixotrophic.html
    sha256: b4d00b0f548dc8167ad7cebeac9ef5608790a1de1ad81db34f9e159a04012b80
    role: context
  - path: pages/traits/physiology/mucocyst_discharge.html
    sha256: de764832fddd147e29bde6bd7d1a97ea5554024fcb77418d6ceb0ab845c5876c
    role: context
  - path: pages/traits/physiology/myzocytosis.html
    sha256: 58c2f06c470865bc5fbe523336fdff338bc2adcf999b3e4b641d92b5a144bcd8
    role: context
  - path: pages/traits/physiology/nad_dependent_alcohol_dehydrogenase_activity.html
    sha256: 5acd0286481761d271f7a49446ced7a0b58785a8ab71269c7084b61e5ad97c14
    role: context
  - path: pages/traits/physiology/naphthol_as_bi_phosphohydrolase_activity.html
    sha256: a4f0217881fe453d0f9365cb9743c5b5f0699470d48054c3be4e50c8e0358141
    role: context
  - path: pages/traits/physiology/natural_competence.html
    sha256: e7792073d3c508e28c1f102b08b712735b4ce819a2c6b001340310c14f7207aa
    role: context
  - path: pages/traits/physiology/negative_autotropism.html
    sha256: bf6356acb9114741ae65a621ee583b2651c229014b043a1e33fbdd9d2e17bee4
    role: context
  - path: pages/traits/physiology/nucleophagy.html
    sha256: 72ad4b951bf8bf311a9bf30d45689dd1099d0e7cc2addbe9c152d71cfb753a99
    role: context
  - path: pages/traits/physiology/nutrient_adaptation.html
    sha256: 704b7f297c3cc2ed2f834b57a0fc2bc2e4c9a1ef5919da7f8ce7d3d9c2845040
    role: context
  - path: pages/traits/physiology/oligotrophic.html
    sha256: 7258cf6b518d93ded64545481ee8c1d38cc989f4e4e3524b49dc015bff17a2a7
    role: context
  - path: pages/traits/physiology/oogamy.html
    sha256: d917901e1d3870b9e77f5dec89ef5d75e1035ae09abdb6df00ca8f14ff27e263
    role: context
  - path: pages/traits/physiology/organoheterotrophic.html
    sha256: 83551c554dc4743ed14e8630af1125cc5c78ef8265dc8a2b02e3db1d742a7b9c
    role: context
  - path: pages/traits/physiology/organotrophic.html
    sha256: ef25dbaff97555a474adf252e468cb77f2477a8a01e2b784c2a4b52028f3cf60
    role: context
  - path: pages/traits/physiology/ornithine_decarboxylase_activity.html
    sha256: 445b2b99d2116b9f8d6b9913f87ce01001a77b93338f06a26c03915147ac99fd
    role: context
  - path: pages/traits/physiology/osmotaxis.html
    sha256: cc490175b3207c256362703e09e429b8a1c586193cffa15a39b2ff3c87118601
    role: context
  - path: pages/traits/physiology/oxidase_activity.html
    sha256: b58dc574aa531d47be17571c62ec38938da3268b2c9fcc075858ff4c4fc660c6
    role: context
  - path: pages/traits/physiology/oxidative_stress_response.html
    sha256: abcfa9bad434cccbc2bdcc45d782d182b03cdc00fb27729831193d7da9f1f2c9
    role: context
  - path: pages/traits/physiology/paedogamy.html
    sha256: ce3e7b339163babf6c77ab10021a3e4aff926339e9a0db8bbd4802a3adb7b5b8
    role: context
  - path: pages/traits/physiology/pallium_feeding.html
    sha256: 88f1e1b1975eb8c453d19ef19ff6fd0a28c573a09ae0afd991974e2c26a5e0fb
    role: context
  - path: pages/traits/physiology/parasexuality.html
    sha256: 8cb0fb5074a0fbd42a380ef62259bd865cea71d6b4276dbe7f910d2ac053adbd
    role: context
  - path: pages/traits/physiology/persister_cell_formation.html
    sha256: f0b131b34268127a391370e50a05da8dd109a962c490348294308c8dfc2caad5
    role: context
  - path: pages/traits/physiology/pexophagy.html
    sha256: c62112118c75a2ef217a37a3e28df3f821fa704922604a5f29a8b91ec2ad2433
    role: context
  - path: pages/traits/physiology/ph_taxis.html
    sha256: 6986569142b21e7ad51fe4760c12239f7a836d97cd6a5ce93340a83b86902d81
    role: context
  - path: pages/traits/physiology/ph_tropism.html
    sha256: 6b7decb4dde3eb2703d634342aa0a349275de9ee6c6bb77e5d44d9ea73681be6
    role: context
  - path: pages/traits/physiology/phagocytosis.html
    sha256: 9026fc8a0f6967d72448e198e83801817a3883228eb9c116e3ca725720d9afbe
    role: context
  - path: pages/traits/physiology/phagotrophy.html
    sha256: 2b1049ca33efeff11732cb74781948a570b5efeb176e2e0448f38d3401eda4ec
    role: context
  - path: pages/traits/physiology/phenylalanine_arylamidase_activity.html
    sha256: 908b7eba109d4800df769522d38884e815ee5c73bbbcf9cd2886d91a048e7c6f
    role: context
  - path: pages/traits/physiology/photoautotrophic.html
    sha256: e390fa13c1588a347e12c00f74542219ae78412c843024499eee052b65ac7902
    role: context
  - path: pages/traits/physiology/photoheterotrophic.html
    sha256: c33dca30a01be6b80172e777253f60e7f2fb92b7a04e114b2777d21611c38467
    role: context
  - path: pages/traits/physiology/photokinesis.html
    sha256: 4ce173da0fb2bea53675482eb1e4c15d36d4a5a4c3a5c97c8ce3b41f0dec0f72
    role: context
  - path: pages/traits/physiology/photolithoautotrophic.html
    sha256: d28c41f65b20984f5de85d990225cb9f10b55bf7e262adf13ead82263ef9ab12
    role: context
  - path: pages/traits/physiology/photolithotrophic.html
    sha256: ac75aa8c7c05d23952ee75721fbf06f7d3d2678b75acc18a6a2810ac1efa9736
    role: context
  - path: pages/traits/physiology/photoorganoheterotrophic.html
    sha256: 3f37a09a4901c0cf0d7ccf19c22b6452de02b70aa31b240d71be11a26f837e81
    role: context
  - path: pages/traits/physiology/phototaxis.html
    sha256: be0f585a5df9a817bf115905f35d18605749b35636fad2d90efa436d25b60150
    role: context
  - path: pages/traits/physiology/phototrophic.html
    sha256: be6a6d48a7b94a636fd9ae120685c9a6e7be946dcc7fe33217b882b9493ebae8
    role: context
  - path: pages/traits/physiology/phototropism.html
    sha256: 65a2abd522147106ab66544c92b5dea4660917e9454646d500c1585438228562
    role: context
  - path: pages/traits/physiology/pinocytosis.html
    sha256: 6191b7fd9bd92ff63fdc9b6fbbf8bc5409eb87bb7f3865101382a54ae6fcfcbc
    role: context
  - path: pages/traits/physiology/positive_autotropism.html
    sha256: 1dd989bc46d2325bc4a27c4eb08459192e0fea8fcc41d139b5e3a7f2f03150d7
    role: context
  - path: pages/traits/physiology/primary_homothallism.html
    sha256: dc94e1dd5c891d5c98c8d1d4483812dc6a595ea70cb8b28bb39060a508fd8ca9
    role: context
  - path: pages/traits/physiology/prolyl_aminopeptidase_activity.html
    sha256: 5f2ef075118e7952b39aeb02148a8680e85b17ca6ab5fe35aba8e427b43a8f53
    role: context
  - path: pages/traits/physiology/proteaphagy.html
    sha256: 8205dc539fd9f18ea89d4358130df94711532193c7e81b9c167e496ad84f7637
    role: context
  - path: pages/traits/physiology/pseudobipolar_mating_system.html
    sha256: 0d3d7e9a4152bf10c34ec7e47b287fd86d09f75a6930247dc6fb74d04755e96b
    role: context
  - path: pages/traits/physiology/pseudohomothallism.html
    sha256: 8d317c5e05b966fe86a7b10fae8af4d1cdc9c86046923900e16429704d8a30a4
    role: context
  - path: pages/traits/physiology/pyrazinamidase_activity.html
    sha256: d1453677580211af372b68abdd3bb36552d92c8f618052a94a8c8276fbeeadbe
    role: context
  - path: pages/traits/physiology/pyrrolidonyl_arylamidase_activity.html
    sha256: e37ca9d286d93b8d535c8a65913e6c21ee29d1ade66778b8ecf168acba516809
    role: context
  - path: pages/traits/physiology/quorum_sensing.html
    sha256: 21e6858673ceba08c48387fd42c21810e233b6c78d564ee961404550959bbc15
    role: context
  - path: pages/traits/physiology/rapid_axopodial_contraction.html
    sha256: b881a07aea0a66f6d66ef248f35393f38164dab670e69d9e627f613901515f9e
    role: context
  - path: pages/traits/physiology/rheotaxis.html
    sha256: 0338c2221bdcebf447b2eaf3395da1b3a45e7e35d86f7994dad5eda8b0d18cb7
    role: context
  - path: pages/traits/physiology/rheotropism.html
    sha256: d2202214410ae6119d74503f6ce8be25784f4568ce54c494f039db4e3bc1553d
    role: context
  - path: pages/traits/physiology/ribophagy.html
    sha256: d4a462ef50236a3395e1f2e1774f965f53b0e30803130b3d4d07b75344eff4d2
    role: context
  - path: pages/traits/physiology/serine_arylamidase_activity.html
    sha256: aed9ceb58e48aa01de26a8b8573d0560f05c6a064b9b416047ac8e499c7be750
    role: context
  - path: pages/traits/physiology/siderophore_production.html
    sha256: 947ed403a5f4614be72c5f1b26e3658f01e0fabed3ad273be3628e9ab26f60d9
    role: context
  - path: pages/traits/physiology/siliceous_scale_production.html
    sha256: 2215e24ca06472a8f72f87b9a740cc09fe6ea8cf29668181e568c599b24299be
    role: context
  - path: pages/traits/physiology/sos_response.html
    sha256: 1f9248975aca43aa92a388b74d116906e17a0166866a20c5c841afa14385928e
    role: context
  - path: pages/traits/physiology/spore_germination.html
    sha256: 9c7dae3af5e4e8f9c4798b4c907fd1699b94120d2a4a837aec91109f3955fb48
    role: context
  - path: pages/traits/physiology/stress_response.html
    sha256: 0953a591b8ced23bcfa28f2622151db85de08ac6ee08fc5ab9e059609382191d
    role: context
  - path: pages/traits/physiology/tetrapolar_mating_system.html
    sha256: e2637d7c7f16ced29e65aa80b6d53d5c86944aaf19ff11b6d41aa24a77770a02
    role: context
  - path: pages/traits/physiology/thermotaxis.html
    sha256: d7136864fa92ddb3364811c08ebde0efbbb5e5b75280f441d19e23997f2d04b8
    role: context
  - path: pages/traits/physiology/thigmotropism.html
    sha256: c3538d096ae05e9ab1019a7c7362b8969716db4d03c98df2ce00a7bebda1693b
    role: context
  - path: pages/traits/physiology/toxicyst_discharge.html
    sha256: 049276351f91946c7d2372b1f5830cea11b67c03bfe35efd41d83c69235c14b8
    role: context
  - path: pages/traits/physiology/trichocyst_discharge.html
    sha256: 28a2abd563429de24ecc89a839f5e04099f3c99a8befbca36ea6aeb589c4f217
    role: context
  - path: pages/traits/physiology/tripolar_mating_system.html
    sha256: ef42f385ecaa138386b9d0b29465bce7d526e3f31dab98e4f8eb437cce90f787
    role: context
  - path: pages/traits/physiology/trogocytosis.html
    sha256: dec572719935d7e1310481ab52f69fa544314ef9246ad6958a7a4f30fa13f2ab
    role: context
  - path: pages/traits/physiology/trophic_type.html
    sha256: 0f27f16554f262f2109dc87c1a89392de96829cf6aa78481a36f980702a2e2b7
    role: context
  - path: pages/traits/physiology/trypsin_activity.html
    sha256: fa917f04dcd24f411e8a4d115d1cf2986f87e311f9b189bb501c1b8f5d281aff
    role: context
  - path: pages/traits/physiology/tyrosine_arylamidase_activity.html
    sha256: 08690303d8526ee3a3a8298a5adf32b9cc801a1a17fa070579e34319d55cbfa3
    role: context
  - path: pages/traits/physiology/unconventional_protein_secretion.html
    sha256: a6a2651c6646a2a9ea8e217abb765af5aad7f73ae8141bf8e0d7732951340310
    role: context
  - path: pages/traits/physiology/unisexual_reproduction.html
    sha256: a560c48271208e37f94cf72d42f68298787b240cbead38637ce04f779c607cf0
    role: context
  - path: pages/traits/physiology/urease_activity.html
    sha256: 133a1dcb99cf34db268338c0bfd794fb46dc2e9b4e2bfc68112537032c30e3e6
    role: context
  - path: pages/traits/physiology/valine_arylamidase_activity.html
    sha256: cff308455d23148bfb7dbb2deb910700f6cf241520f4103cd4d2793b14a91f85
    role: context
  - path: pages/traits/physiology/viable_but_nonculturable_state.html
    sha256: 84642403415a9aa81cad1843637bd7b569778acb06d75fa166095aad44a422d5
    role: context
  - path: pages/traits/physiology/viscotaxis.html
    sha256: d91217537a49dc74e2cf9964c836352b2800e147d26a1f3df597be4eac8e8de5
    role: context
  - path: pages/traits/quantitative_property/has_maximum_observed_value.html
    sha256: e7cb26396f327a31d0c3f5e7b8a4a8d53677706db3c1aba6bf470b684678d021
    role: context
  - path: pages/traits/quantitative_property/has_minimum_observed_value.html
    sha256: 131a8a4f15f5497873581584848fbe5f736dfa91e8efbc02ee4367d3213d471b
    role: context
  - path: pages/traits/quantitative_property/has_observed_spot_value.html
    sha256: 979e7c13dab2eb8931f305e6d2c8333950bba0af256ffdbe27f1eb8192a2abbb
    role: context
  - path: pages/traits/quantitative_property/has_value.html
    sha256: 3b38cd32dfd23c0e48aedda1140bdf46b8eb73ea070e14f21b274dc3587929b9
    role: context
  - path: pages/traits/quantitative_property/has_value_comments.html
    sha256: d824f553ab35f8258d0ab1cec10380f84c08b7ff7948147f2ced6990d7154a9b
    role: context
  - path: pages/traits/quantitative_property/is_negative_data.html
    sha256: 6f661323b22ca1f992545c91acab37d52f626e73c76fda30208a46c9543c3a85
    role: context
  - path: pages/traits/quantitative_property/observation_data_property.html
    sha256: 07a40a25c9c7f363d759addb01d4b5efe5e1a31e9103bc93d0b00926de2e1b22
    role: context
  - path: pages/traits/upper/biological_process.html
    sha256: 323b255e7b94444fd188fbc0199cb93f0aedb466f0b9b57ed28f51c9e1a48276
    role: context
  - path: pages/traits/upper/chemical_entity.html
    sha256: c42af95873b91a5fb36d5802113aea4cd0626f5945e0afe3551e8660357b36bc
    role: context
  - path: pages/traits/upper/enzyme.html
    sha256: d0bf74b2185464d786268961bb9259e9d980138dc178d9ae8d6f558f7eb41a65
    role: context
  - path: pages/traits/upper/material_entity.html
    sha256: 4ca027719dde41c88bd4dcf408bdd4679647e3e08fce481ed14bc3712c06cc05
    role: context
  - path: pages/traits/upper/microbe.html
    sha256: cff1d001228c43b4c8991a30f664fe9994603665fbbc0c7eb96ed8d297550934
    role: context
  - path: pages/traits/upper/observation.html
    sha256: 2327b67c795634ceccd4d3a895325f3c6224f4e56572a1ecf1ef3601741ede6a
    role: context
  - path: pages/traits/upper/phenotype.html
    sha256: 15a3dc06c9228b43e89ff6df0a40f1534f30fa36d2948873b201bc17ed12e7fc
    role: context
  - path: pages/traits/upper/quality.html
    sha256: 67255972a39575d87eded485bcf0e52f21821fd70c1664a41053ed533cf16dfb
    role: context
  - path: pages/umap.html
    sha256: 4a9ad24ffe939663df09d00a87f8f203c298430d0a05ab74e69851bcb5a5209e
    role: context
  - path: proposals/metpo_traitmech_v564/proposal.md
    sha256: 9e57693bc431c35ee5703a87334fcfb6e41a22a9d13162df0b4f91de4842d617
    role: context
  - path: proposals/metpo_traitmech_v565/proposal.md
    sha256: 131e22178a9ffffa9922f9386df806329c5d7042651fdf34e588c6b7c629b424
    role: context
  - path: proposals/metpo_traitmech_v566/metpo_proposal_classes_robot.tsv
    sha256: 86db04745500177cb68184b43b8d9e842c318875128a30b4eb0d37fd46cb995e
    role: context
  - path: proposals/metpo_traitmech_v566/proposal.md
    sha256: 9200e3e4a67479d632cfe9fc479eccf1f31ee6aa36631baa45aadac3ce39bf40
    role: context
  - path: proposals/metpo_traitmech_v567/metpo_proposal_classes_robot.tsv
    sha256: 9678756c4d662ba6715fa97eafe039a59305aff82c614d000ece572ee3328baa
    role: context
  - path: proposals/metpo_traitmech_v567/proposal.md
    sha256: 7542dfa8807df4f8b61c16ebdf421c3727470498cb06e5508aa0e0b52be679d5
    role: context
  - path: reports/proposal_citation_audit.tsv
    sha256: 1d738bd0612e0413df74c122c2d6e6af75c6c8b59a6921c2187975583dad7d19
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/.vendored_canon_ref
    sha256: 698af47e96e93fe96e81910bb140593a79c2b92c4688892edeab9b63244ec5bf
    role: context
  - path: scripts/add_diatom_frustule_production_trait.py
    sha256: 90ca57c26bb972a736f9809fe9f90cc81a21ebebf7d58dfb83285ebbc2c28bd7
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
  - path: tests/test_add_diatom_frustule_production_trait.py
    sha256: 19db5dbfd8244e526ef83639fa1a0f1855681acf4f287af59592120e73f7f9b9
    role: context
targets:
- target_id: traitmech:000691
  path: data/traits/physiology/diatom_frustule_production.yaml
  label: diatom frustule production
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/physiology/diatom_frustule_production.yaml
    role: curated record
  - repository: CultureBotAI/TraitMech
    path: scripts/add_diatom_frustule_production_trait.py
    role: guarded writer
scope:
  description: One complete new TraitRecord, with its writer/tests, v567 proposal,
    provenance and generated surfaces.
  selection: Exact traitmech:000691 on the trait-scoped branch; no sampling.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - traitmech:000691
  exclusions:
  - target: Other 1085 TraitRecords
    reason: Comparators and automated corpus checks, not whole-corpus scientific adjudication.
  - target: data/traits/physiology/spore_germination.yaml
    reason: DO_NOT_WORK exclusion; byte-preserved and not curated.
checks:
- check_id: records-0
  name: .venv/bin/linkml-validate -s src/traitmech/schema/traitmech.yaml --target-class
    TraitRecord data/traits/physiology/diatom_frustule_production.yaml
  status: passed
  required: true
  target_ids:
  - traitmech:000691
  command: .venv/bin/linkml-validate -s src/traitmech/schema/traitmech.yaml --target-class
    TraitRecord data/traits/physiology/diatom_frustule_production.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Completed successfully at its actual command scope, including corpus-wide
    audits. Existing baselines were not expanded.
- check_id: records-1
  name: .venv/bin/python scripts/validate_strict.py data/traits/physiology/diatom_frustule_production.yaml
  status: passed
  required: true
  target_ids:
  - traitmech:000691
  command: .venv/bin/python scripts/validate_strict.py data/traits/physiology/diatom_frustule_production.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Completed successfully at its actual command scope, including corpus-wide
    audits. Existing baselines were not expanded.
- check_id: records-2
  name: .venv/bin/python scripts/verify_snippets.py --record data/traits/physiology/diatom_frustule_production.yaml
  status: passed
  required: true
  target_ids:
  - traitmech:000691
  command: .venv/bin/python scripts/verify_snippets.py --record data/traits/physiology/diatom_frustule_production.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: 'Native snippet verification completed: Bedoshvili VERIFIED; Aram NOT_IN_ABSTRACT.
    The latter is an Introduction quote, directly checked in official full text, not
    an abstract-verifier success.'
- check_id: generate-0
  name: just audit-proposals
  status: passed
  required: true
  target_ids:
  - traitmech:000691
  command: just audit-proposals
  exit_code: 0
  expected_exit_code: 0
  summary: Completed successfully at its actual command scope, including corpus-wide
    audits. Existing baselines were not expanded.
- check_id: generate-1
  name: just ground-predicates
  status: passed
  required: true
  target_ids:
  - traitmech:000691
  command: just ground-predicates
  exit_code: 0
  expected_exit_code: 0
  summary: Completed successfully at its actual command scope, including corpus-wide
    audits. Existing baselines were not expanded.
- check_id: generate-2
  name: just ground-nodes
  status: passed
  required: true
  target_ids:
  - traitmech:000691
  command: just ground-nodes
  exit_code: 0
  expected_exit_code: 0
  summary: Completed successfully at its actual command scope, including corpus-wide
    audits. Existing baselines were not expanded.
- check_id: generate-3
  name: just audit-graphs
  status: passed
  required: true
  target_ids:
  - traitmech:000691
  command: just audit-graphs
  exit_code: 0
  expected_exit_code: 0
  summary: Completed successfully at its actual command scope, including corpus-wide
    audits. Existing baselines were not expanded.
- check_id: generate-4
  name: just audit-graph-protein-taxa
  status: passed
  required: true
  target_ids:
  - traitmech:000691
  command: just audit-graph-protein-taxa
  exit_code: 0
  expected_exit_code: 0
  summary: Completed successfully at its actual command scope, including corpus-wide
    audits. Existing baselines were not expanded.
- check_id: generate-5
  name: just audit-predicate-domains
  status: passed
  required: true
  target_ids:
  - traitmech:000691
  command: just audit-predicate-domains
  exit_code: 0
  expected_exit_code: 0
  summary: Completed successfully at its actual command scope, including corpus-wide
    audits. Existing baselines were not expanded.
- check_id: generate-6
  name: just check-biolink-coverage
  status: passed
  required: true
  target_ids:
  - traitmech:000691
  command: just check-biolink-coverage
  exit_code: 0
  expected_exit_code: 0
  summary: Completed successfully at its actual command scope, including corpus-wide
    audits. Existing baselines were not expanded.
- check_id: generate-7
  name: just audit-snippets
  status: passed
  required: true
  target_ids:
  - traitmech:000691
  command: just audit-snippets
  exit_code: 0
  expected_exit_code: 0
  summary: Completed successfully at its actual command scope, including corpus-wide
    audits. Existing baselines were not expanded.
- check_id: generate-8
  name: just gen-discussions-data
  status: passed
  required: true
  target_ids:
  - traitmech:000691
  command: just gen-discussions-data
  exit_code: 0
  expected_exit_code: 0
  summary: Completed successfully at its actual command scope, including corpus-wide
    audits. Existing baselines were not expanded.
- check_id: generate-9
  name: just gen-qc-dashboard
  status: passed
  required: true
  target_ids:
  - traitmech:000691
  command: just gen-qc-dashboard
  exit_code: 0
  expected_exit_code: 0
  summary: Completed successfully at its actual command scope, including corpus-wide
    audits. Existing baselines were not expanded.
- check_id: generate-10
  name: just gen-pages
  status: passed
  required: true
  target_ids:
  - traitmech:000691
  command: just gen-pages
  exit_code: 0
  expected_exit_code: 0
  summary: Completed successfully at its actual command scope, including corpus-wide
    audits. Existing baselines were not expanded.
- check_id: generate-11
  name: just gen-priority-dashboard
  status: passed
  required: true
  target_ids:
  - traitmech:000691
  command: just gen-priority-dashboard
  exit_code: 0
  expected_exit_code: 0
  summary: Completed successfully at its actual command scope, including corpus-wide
    audits. Existing baselines were not expanded.
- check_id: verify-0
  name: just qc
  status: passed
  required: true
  target_ids:
  - traitmech:000691
  command: just qc
  exit_code: 0
  expected_exit_code: 0
  summary: Completed successfully at its actual command scope, including corpus-wide
    audits. Existing baselines were not expanded.
- check_id: verify-1
  name: just validate-history
  status: passed
  required: true
  target_ids:
  - traitmech:000691
  command: just validate-history
  exit_code: 0
  expected_exit_code: 0
  summary: Completed successfully at its actual command scope, including corpus-wide
    audits. Existing baselines were not expanded.
- check_id: verify-2
  name: just validate-products
  status: passed
  required: true
  target_ids:
  - traitmech:000691
  command: just validate-products
  exit_code: 0
  expected_exit_code: 0
  summary: Completed successfully at its actual command scope, including corpus-wide
    audits. Existing baselines were not expanded.
- check_id: verify-3
  name: just verify-proposal metpo_traitmech_v567
  status: passed
  required: true
  target_ids:
  - traitmech:000691
  command: just verify-proposal metpo_traitmech_v567
  exit_code: 0
  expected_exit_code: 0
  summary: Completed successfully at its actual command scope, including corpus-wide
    audits. Existing baselines were not expanded.
- check_id: verify-4
  name: just robot-validate-proposal metpo_traitmech_v567
  status: passed
  required: true
  target_ids:
  - traitmech:000691
  command: just robot-validate-proposal metpo_traitmech_v567
  exit_code: 0
  expected_exit_code: 0
  summary: Completed successfully at its actual command scope, including corpus-wide
    audits. Existing baselines were not expanded.
- check_id: verify-5
  name: .venv/bin/ruff check src scripts tests
  status: passed
  required: true
  target_ids:
  - traitmech:000691
  command: .venv/bin/ruff check src scripts tests
  exit_code: 0
  expected_exit_code: 0
  summary: Completed successfully at its actual command scope, including corpus-wide
    audits. Existing baselines were not expanded.
- check_id: tests-0
  name: .venv/bin/python -m pytest -q --junitxml=/tmp/traitmech-frustule-checks-20261010/pytest.xml
  status: passed
  required: true
  target_ids:
  - traitmech:000691
  command: .venv/bin/python -m pytest -q --junitxml=/tmp/traitmech-frustule-checks-20261010/pytest.xml
  exit_code: 0
  expected_exit_code: 0
  summary: 3790 tests passed, with no failures, errors or skips.
- check_id: focused
  name: focused
  status: passed
  required: true
  summary: '20 focused tests passed: identity and scope, source limits, proposal header/refinement,
    dry run, exact replay, preserved parent, drift refusal and prevalidation.'
  target_ids:
  - traitmech:000691
  command: .venv/bin/python -m pytest tests/test_add_diatom_frustule_production_trait.py
    -q
  exit_code: 0
  expected_exit_code: 0
- check_id: history-diff
  name: history-diff
  status: passed
  required: true
  summary: One changed trait and one appended repository history; committed-diff provenance
    gate passed.
  target_ids:
  - traitmech:000691
  command: .venv/bin/python scripts/audit_history_records.py --base 156c7ea2c30315372d7c5078d0dd578839b12da8
  exit_code: 0
  expected_exit_code: 0
- check_id: browser
  name: browser
  status: passed
  required: true
  summary: 'Headless Chrome passed at 1440px and 390px: local identity, two quotes,
    two OPEN discussions, no invented graph/examples, history link, parent round trip,
    exact-ID browse, 1086-record dashboard, loaded coverage image, no overflow or
    page errors. Desktop record and mobile evidence screenshots visually inspected.
    Initial sandbox Chrome launch failed before page inspection; the authorized unsandboxed
    rerun passed.'
  target_ids:
  - traitmech:000691
  command: node /tmp/traitmech-frustule-browser-qa-20261010.cjs
  exit_code: 0
  expected_exit_code: 0
- check_id: artifacts
  name: artifacts
  status: passed
  required: true
  summary: All 1085 existing trait YAMLs byte-preserved, including protected spore
    germination. Of old pages, 1084 change only footer; biomineralization adds this
    child. Only existing priority delta is parent child count 2 to 3; phenotype stays
    181. Old histories, reviews, proposals, embeddings and discussion templates preserved.
    Canonical 11-column header and record/TSV agreement pass.
  target_ids:
  - traitmech:000691
  command: .venv/bin/python /tmp/traitmech-frustule-artifact-audit-20261010.py
  exit_code: 0
  expected_exit_code: 0
- check_id: rdf
  name: rdf
  status: passed
  required: true
  summary: 'Parsed RDF graph cardinalities: {''classes'': 15, ''merged'': 12628, ''reasoned'':
    12632}. Correct w3id child 1064400 -> labeled phenotype 1000059 -> quality 1000188;
    no legacy OBO METPO stubs. Biomineralization 1064300 refinement is explicitly
    requested in narrative and TSV observations, not emitted by this standalone cohort.'
  target_ids:
  - traitmech:000691
  command: .venv/bin/python /tmp/traitmech-frustule-rdf-check-20261010.py
  exit_code: 0
  expected_exit_code: 0
- check_id: sources
  name: sources
  status: passed
  required: true
  summary: One exact source-qualified MED match per PMID, matching DOI/title. Bedoshvili
    quote matches scientific Abstract; Aram quote absent from Abstract and matches
    Introduction in cached official XML. Access sections and limits are retained.
  target_ids:
  - traitmech:000691
  command: .venv/bin/python /tmp/traitmech-frustule-source-check-20261010.py
  exit_code: 0
  expected_exit_code: 0
- check_id: fresh-novelty
  name: fresh-novelty
  status: passed
  required: true
  summary: Refreshed whole-worktree ignored-and-hidden concept/citation/full-block
    searches. All five pending PR heads and complete paginated file lists unchanged;
    current main unchanged. New external-to-owned matches were only inspected metadata
    of this branch. No unowned reservation or unresolved new candidate match.
  target_ids:
  - traitmech:000691
  command: .venv/bin/python /tmp/traitmech-frustule-prepublish-20261010.py
  exit_code: 0
  expected_exit_code: 0
- check_id: whitespace
  name: whitespace
  status: passed
  required: true
  summary: Ordinary staged check returned 2 only for three required empty trailing
    ROBOT directive cells. Exact-path exception and separate non-TSV check passed.
    Both headers are canonical 11 columns; no global whitespace setting changed.
  target_ids:
  - traitmech:000691
  command: git -c core.whitespace=-blank-at-eol diff --cached --check -- proposals/metpo_traitmech_v567/metpo_proposal_classes_robot.tsv
  exit_code: 0
  expected_exit_code: 0
- check_id: embeddings
  name: Configured embedding source applicability
  status: not_applicable
  required: false
  target_ids:
  - traitmech:000691
  summary: Exact configured default/fallback paths absent in primary and owned layouts,
    checked independently of gitignore. Existing embedding artifacts preserved.
evidence:
- evidence_id: morphogenesis
  kind: primary_source
  reference: DOI:10.1007/s00709-017-1199-4
  locator: Complete scientific Abstract at https://pubmed.ncbi.nlm.nih.gov/29270874/
    and Europe PMC CORE EXT_ID:29270874 AND SRC:MED. Timestamp is the refreshed qualified
    CORE lookup, not first acquisition.
  accessed_at: '2026-10-10T20:20:25.556453Z'
  snapshot_sha256: 5b27a027b0ed358ac41cbfe249a4e277b635f74331724a705db7cda7484d6cc2
  support: supports
  summary: Defines frustule components as silica valves and girdle bands and observes
    valve morphogenesis in Encyonema ventricosum. Online 2017-12-21, issue May 2018.
    Full Methods, actual figures and supplements unread. Cytoskeletal proximity does
    not establish molecular necessity; the short quote is exact.
- evidence_id: tomography
  kind: primary_source
  reference: DOI:10.1038/s41467-024-52211-x
  locator: Scientific Abstract, Introduction, Results, Discussion and Methods in https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11385223/fullTextXML;
    actual Figure 2 inspected. Timestamp is cached XML reread and exact Introduction-quote
    check, not a new download. PMID:39251596 independently source-qualified.
  accessed_at: '2026-10-10T20:20:26.171284Z'
  snapshot_sha256: 7621599f1b24d49735667b034c7009199ba6f818871cee7d87de87544d4ac39d
  support: supports
  summary: CCMP1335 silicon-starvation/resupply and cryoET support valve formation.
    Figure 2 orders different cells by inferred maturation, not a longitudinal time
    series. Cell-wall terminology supports definition; Results support production.
    Contact-site function, transport and actin expansion remain proposed mechanisms.
    Historical Thalassiosira pseudonana naming is not current taxonomy assignment;
    other actual figures and supplements unread.
- evidence_id: novelty
  kind: search
  reference: proposals/metpo_traitmech_v567/proposal.md
  locator: Allocation and novelty, proposal hierarchy, upstream template contract.
    Access timestamp is proposal reread, not earlier search execution.
  accessed_at: '2026-10-10T21:04:59Z'
  support: supports
  summary: No exact record or conflicting reservation found in the bounded ignored-and-hidden
    searches. Scale production and biomineralization are distinct/broader. Full block
    1064400-1064499 reserved, only 1064400 populated; v566 remains unchanged.
  search_scope: All 22 pre-existing worktrees plus this owned branch; entire trees
    including ignored/hidden files. Exact local ID/cohort/full proposed numeric block;
    frustule/diatom/silicification/girdle/valve variants; cited DOI/PMID/PMC strings
    and 2021 research lead. Pinned 12617-triple METPO graph, fresh 399-record seed,
    full release delta and active-review rows checked. All five pending PRs including
    draft 924, paginated files and immutable curation blobs inspected. CommunityMech
    whole-block ignored/hidden search found only two identical decimal-measurement
    hits, directly read. Seed absence does not prove novelty or exhaustion.
- evidence_id: record
  kind: record_content
  reference: data/traits/physiology/diatom_frustule_production.yaml
  locator: Complete new record and comparator definitions/discussions for biomineralization,
    scales and coccoliths.
  accessed_at: '2026-10-10T21:04:59Z'
  support: supports
  summary: New valve/girdle-element formation is a reusable phenotype under biomineralization,
    not a material frustule, retained valve or generic silica uptake. Scope does not
    require both valves formed anew per division or all parts made simultaneously.
    No synonyms/xrefs, examples, causal graphs or protein accessions asserted.
- evidence_id: implementation
  kind: record_content
  reference: scripts/add_diatom_frustule_production_trait.py
  locator: build_record, proposal_tsv, main; focused test file and new repository
    history.
  accessed_at: '2026-10-10T21:04:59Z'
  support: supports
  summary: Writer defaults to dry run, checks parent identity projection and target/proposal
    drift, prevalidates before writes and permits exact replay. Controlled fixture
    tests preserve parent bytes. Native per-record event and CREATE history retain
    correct agent, actual decision/write distinction and PROPOSED status.
- evidence_id: products
  kind: validation
  reference: reports/proposal_citation_audit.tsv
  locator: Completed native generation/checks, artifact byte audit, parsed proposal
    RDF and browser inspection.
  accessed_at: '2026-10-10T21:04:59Z'
  support: supports
  summary: 1086 records and consistent native products. Exact pinned CLAW a5d562962c75a2ad9efd8160b548df5944315422
    source verified across 152 source blobs and used for shared generators. Embeddings
    preserved because configured sources are absent. No baseline relaxation or unrelated
    record edit.
assessments:
- assessment_id: identity
  area: identity
  topic: Production phenotype, not the material wall
  summary: The definition denotes formation of new siliceous wall elements. It does
    not equate a cell structure, sequence feature, retained valve or chemical uptake
    with production.
  target_ids:
  - traitmech:000691
  evidence_ids:
  - morphogenesis
  - tomography
  - record
  outcome: supported
- assessment_id: novelty
  area: identity
  topic: Distinct endpoint and allocation
  summary: No exact existing record or conflicting ID found within the explicitly
    searched scope. Scale production, auxospore coverings and setae alone do not establish
    the endpoint; none is declared organism-level disjoint.
  target_ids:
  - traitmech:000691
  evidence_ids:
  - novelty
  - record
  outcome: supported
- assessment_id: hierarchy
  area: grounding
  topic: Strictly broader biomineralization
  summary: Formation of the specified mineral elements entails mineral formation.
    Local parent 000690 is broader; standalone v567 uses released phenotype and explicitly
    requests the v566 refinement on adoption.
  target_ids:
  - traitmech:000691
  evidence_ids:
  - record
  - novelty
  - products
  outcome: supported
- assessment_id: evidence
  area: evidence
  topic: Exact sources, quote sections and inference limits
  summary: Both primary studies support production; quotes are short contiguous spans
    with separate section attribution. Structural association and inferred maturation
    order are not upgraded to necessary mechanisms or longitudinal observation.
  target_ids:
  - traitmech:000691
  evidence_ids:
  - morphogenesis
  - tomography
  outcome: supported
- assessment_id: provenance
  area: provenance
  topic: Guarded writer and append-only history
  summary: The native curation event and repository CREATE history match the sole
    new record. Writer guards and focused regression tests cover dry run, refusal,
    replay and prevalidation; old records and histories remain intact.
  target_ids:
  - traitmech:000691
  evidence_ids:
  - implementation
  - products
  outcome: supported
- assessment_id: products
  area: consistency
  topic: Proposal and generated artifacts
  summary: Canonical template, parsed w3id hierarchy, corpus counts, parent links
    and rendered identity agree. Old cohorts and protected records are preserved.
  target_ids:
  - traitmech:000691
  evidence_ids:
  - novelty
  - products
  outcome: supported
- assessment_id: gaps
  area: completeness
  topic: Taxa, mappings and molecular causality
  summary: Canonical taxa and exact mappings await authority review; production-specific
    molecular evidence and paired accessions are required before graph curation. Two
    OPEN discussions retain these limits.
  target_ids:
  - traitmech:000691
  evidence_ids:
  - record
  - tomography
  outcome: unknown
findings: []
actions: []
limitations:
- Author self-review, not independent review or human scientific signoff.
- Full coverage means this one target, not a scientific review of the entire corpus.
  Broad input hashes support comparison and deterministic checks only.
- Bedoshvili scientific Abstract read; full Methods, actual figures and supplements
  unread. Aram main text and actual Figure 2 read; other actual figures and supplements
  unread.
- Native Aram snippet outcome remains NOT_IN_ABSTRACT; direct Introduction verification
  is separately documented.
- No canonical taxon, synonym, exact external mapping, protein accession or causal
  mechanism asserted. Two discussions stay OPEN and the term remains PROPOSED.
- Standalone v567 emits the released phenotype ancestor, not the requested biomineralization
  refinement; upstream adoption must reconcile v566 and v567.
- Configured embedding sources absent; old embeddings preserved. No paid research
  performed.
- Curation-decision time, history-write time, source recheck times and review times
  describe different events. Working-tree input hashes are reviewer attestations,
  not proof the reviewed bytes were committed.
notes:
- No new defect issue warranted by this bounded pass. External review and final CI/reservation
  outcomes belong in the PR.
tags:
- add-trait
- diatom-frustule-production
- self-review
```
