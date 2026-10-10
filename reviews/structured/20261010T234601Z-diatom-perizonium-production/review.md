# Adversarial self-review of diatom perizonium production

- Review: 20261010T234601Z-diatom-perizonium-production
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-10T23:28:09Z
- Finished UTC: 2026-10-10T23:46:01Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Three primary studies support the bounded production phenotype. No actionable defect remains in the reviewed target; access, mapping, exemplar and mechanism limits are explicit. Status remains PROPOSED.

## Scope And Provenance

One complete new TraitRecord with writer/tests, v569 proposal, history and generated surfaces.

Selection: Exact traitmech:000693; no sampling.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base b4d7f0ea857bc488e93e6fe7eb15e6f786736805.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| traitmech:000693 | data/traits/physiology/diatom_perizonium_production.yaml | maintained | diatom perizonium production |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| .venv/bin/linkml-validate -s src/traitmech/schema/traitmech.yaml --target-class TraitRecord data/traits/physiology/diatom_perizonium_production.yaml | passed | True | traitmech:000693 | Passed at actual native command scope, including corpus-wide gates; no baseline relaxation. |
| .venv/bin/python scripts/validate_strict.py data/traits/physiology/diatom_perizonium_production.yaml | passed | True | traitmech:000693 | Passed at actual native command scope, including corpus-wide gates; no baseline relaxation. |
| .venv/bin/python scripts/verify_snippets.py --record data/traits/physiology/diatom_perizonium_production.yaml | passed | True | traitmech:000693 | 2022 NOT_IN_ABSTRACT; 2017 and 2013 VERIFIED. The 2022 Results quote was separately checked in official full text, not relabeled as abstract-verified. |
| just audit-proposals | passed | True | traitmech:000693 | Passed at actual native command scope, including corpus-wide gates; no baseline relaxation. |
| just ground-predicates | passed | True | traitmech:000693 | Passed at actual native command scope, including corpus-wide gates; no baseline relaxation. |
| just ground-nodes | passed | True | traitmech:000693 | Passed at actual native command scope, including corpus-wide gates; no baseline relaxation. |
| just audit-graphs | passed | True | traitmech:000693 | Passed at actual native command scope, including corpus-wide gates; no baseline relaxation. |
| just audit-graph-protein-taxa | passed | True | traitmech:000693 | Passed at actual native command scope, including corpus-wide gates; no baseline relaxation. |
| just audit-predicate-domains | passed | True | traitmech:000693 | Passed at actual native command scope, including corpus-wide gates; no baseline relaxation. |
| just check-biolink-coverage | passed | True | traitmech:000693 | Passed at actual native command scope, including corpus-wide gates; no baseline relaxation. |
| just audit-snippets | passed | True | traitmech:000693 | Passed at actual native command scope, including corpus-wide gates; no baseline relaxation. |
| just gen-discussions-data | passed | True | traitmech:000693 | Passed at actual native command scope, including corpus-wide gates; no baseline relaxation. |
| just gen-qc-dashboard | passed | True | traitmech:000693 | Passed at actual native command scope, including corpus-wide gates; no baseline relaxation. |
| just gen-pages | passed | True | traitmech:000693 | Passed at actual native command scope, including corpus-wide gates; no baseline relaxation. |
| just gen-priority-dashboard | passed | True | traitmech:000693 | Passed at actual native command scope, including corpus-wide gates; no baseline relaxation. |
| just qc | passed | True | traitmech:000693 | Passed at actual native command scope, including corpus-wide gates; no baseline relaxation. |
| just validate-history | passed | True | traitmech:000693 | Passed at actual native command scope, including corpus-wide gates; no baseline relaxation. |
| just validate-products | passed | True | traitmech:000693 | Passed at actual native command scope, including corpus-wide gates; no baseline relaxation. |
| just verify-proposal metpo_traitmech_v569 | passed | True | traitmech:000693 | Passed at actual native command scope, including corpus-wide gates; no baseline relaxation. |
| just robot-validate-proposal metpo_traitmech_v569 | passed | True | traitmech:000693 | Passed at actual native command scope, including corpus-wide gates; no baseline relaxation. |
| .venv/bin/ruff check src scripts tests | passed | True | traitmech:000693 | Passed at actual native command scope, including corpus-wide gates; no baseline relaxation. |
| .venv/bin/python -m pytest -q --junitxml=/tmp/traitmech-perizonium-checks-20261010/pytest.xml | passed | True | traitmech:000693 | 3830 passed; no failures, errors or skips. |
| focused | passed | True | traitmech:000693 | 20 passed: identity, source limits, hierarchy, canonical header, dry run/replay, controlled preimages, drift refusal and prevalidation. An initial fixture-renaming typo was corrected before the passing rerun. |
| history | passed | True | traitmech:000693 | One changed record with one CREATE history; actual codex actor, model and agent tool inspected. |
| browser | passed | True | traitmech:000693 | Desktop 1440px and mobile 390px: three quotes, two OPEN discussions, one history link, parent with five children, browse navigation, 1088-record dashboard and loaded coverage image; no overflow or page errors. Screenshots visually inspected. |
| artifacts | passed | True | traitmech:000693 | 1087 old trait YAMLs preserved byte-for-byte; 1086 prior pages change only footer, parent adds child. Sole old priority change: parent children 4 to 5. Prior history, reviews, proposals, embeddings and browser templates preserved; protected spore germination unchanged. |
| rdf | passed | True | traitmech:000693 | Parsed RDF cardinalities {'classes': 15, 'merged': 12628, 'reasoned': 12632}; w3id 1064600 -&gt; phenotype 1000059 -&gt; quality 1000188. No OBO METPO stubs. Proposed 1064300 refinement requested but not emitted standalone. |
| sources | passed | True | traitmech:000693 | Three exact source-qualified MED/PMID/title/DOI results; contiguous quotes checked in scientific sections; cached actual figures retain recorded SHA-256 identities. |
| reservations | passed | True | traitmech:000693 | Current main, five pending PR heads and full paginated file lists unchanged; ignored/hidden worktree searches found no unowned reservation or unresolved new match. |
| contracts | passed | True | traitmech:000693 | 152 shared-source blobs verified against pinned CLAW; canonical class/property headers rehashed against pinned upstream Git blobs; exact configured embedding sources absent in primary and owned layouts. |
| whitespace | passed | True | traitmech:000693 | Ordinary check identifies only required trailing ROBOT cells. Exact-path exception and separate non-TSV check pass; no global configuration changed. |
| Embedding applicability | not_applicable | False | traitmech:000693 | Exact configured sources absent independently of gitignore; previous embedding artifacts preserved. |

## Scientific And Domain Assessments

### Production of a specific mineralized wall system

identity: supported. Targets: traitmech:000693.

The definition denotes a reusable production phenotype, not a material object or auxosporulation generally.

### Distinct endpoint and reservation

identity: supported. Targets: traitmech:000693.

No exact record or ontology class was found in bounded ignored/hidden searches. Prior broad endpoint notes require no exact-node repair.

### Strictly broader biomineralization

grounding: supported. Targets: traitmech:000693.

Mineralized-band production entails biomineralization. Released-ancestor TSV and explicit v566 refinement are consistent.

### Primary observations and varied band systems

evidence: supported. Targets: traitmech:000693.

Exact source snippets support formation without universal orientation, sequence or expansion timing. Static morphology and chemical labeling do not establish protein-level necessity.

### Guarded curation and actual attribution

provenance: supported. Targets: traitmech:000693.

Controlled preimage tests, native curation event and explicit codex CREATE history agree with the change.

### Proposal and rendered products

consistency: supported. Targets: traitmech:000693.

Canonical template, RDF hierarchy, counts, source text and navigation agree. Historical artifacts are preserved.

### Mapping, exemplar and mechanism follow-up

completeness: unknown. Targets: traitmech:000693.

No authority-verified exact mapping or canonical clone assigned. Functional evidence and paired accessions are required for protein edges; discussions retain these gaps.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| biddulphia | DOI:10.1371/journal.pone.0272778; Scientific Abstract, Introduction, Methods, early Results, Epizonium and perizonium, Discussion: Auxospore structure and development; actual Figure 11. Official XML https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9447881/fullTextXML reread; other actual figures and S1 Appendix unread. https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A36067191+AND+SRC%3AMED&amp;format=json&amp;resultType=core | supports | Formation of siliceous TP/LP bands in an auxospore wall supports the definition. Fixed stages are not live kinetics. Some layer boundaries remain uncertain; atypical cultured clone is not assigned as canonical. |
| plagiogrammaceans | DOI:10.1371/journal.pone.0181413; Scientific Abstract, Methods prose, Auxospore wall fine structure, relevant Discussion paragraphs, actual Figure 5; Table 1/2 headers/footnotes and StA:7/8, Van5:5/6 rows. Official XML https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5558960/fullTextXML reread; remaining rows not fully interpreted, other figures/supplements unread. https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A28813426+AND+SRC%3AMED&amp;format=json&amp;resultType=core | supports | TP production with inferred near-simultaneous deposition argues against universal one-at-a-time secretion. Initial epivalves are not LP by default. The 2013 Tabularia study is retained as reference 100; reinterpretation concerns other sources. Aged cultures are not archetypes. |
| tabularia | DOI:10.1016/j.ejop.2013.06.002; Complete scientific Abstract in source-qualified Europe PMC CORE, online 2013-08-22 / 2014 issue. Full Methods, figures and supplements unread; publisher full text unavailable. https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A23972513+AND+SRC%3AMED&amp;format=json&amp;resultType=core | supports | LP deposition without TP near maximal auxospore length supports the boundary. EDS nondetection is not absolute absence. These distinct primary studies share authors and do not establish independent-laboratory replication. |
| record | data/traits/physiology/diatom_perizonium_production.yaml; Whole record, comparator definitions and discussions. | supports | Production phenotype with strictly broader biomineralization parent; no inherited-possession, organism-level disjointness, universal sexual origin or protein-mechanism claim. Two actionable OPEN discussions; PROPOSED status retained. |
| novelty | proposals/metpo_traitmech_v569/proposal.md; Complete allocation, hierarchy, boundaries and upstream round trip. | supports | No exact term or conflicting reservation found in recorded search scope. Whole 1064600-1064699 block reserved, only 1064600 populated; distinct anisogamy use of 2017 citation does not establish a duplicate. |
| implementation | scripts/add_diatom_perizonium_production_trait.py; Whole writer, focused tests and CREATE history. | supports | Native validated mutation and curation event with dry-run/replay and preimage guards. History attribution correct; no scientific status promotion. Existing add-trait guidance covers the encountered source and sequence-feature interpretation limits. |
| products | reports/proposal_citation_audit.tsv; Native checks, generated pages, dashboards, corpus counts and ROBOT RDF. | supports | 1088 unique records and 573 proposed records pass citation gate. Rendered identity, hierarchy, snippets and history agree with source. No prior source record, protected record, embedding or immutable review changed. |

## Limits And Additional Notes

- Author self-review, not independent review or human scientific signoff; full coverage means one target.
- Only stated source sections, table rows and two actual figures inspected. 2013 source limited to scientific Abstract; unread supplements and figures are not evidence.
- The 2022 quote remains native NOT_IN_ABSTRACT despite direct Results verification. Shared authorship is not independent-laboratory replication.
- No canonical taxon, exact synonym/xref, protein or graph asserted. Two OPEN discussions; record PROPOSED.
- Standalone proposal uses released phenotype; adoption must reconcile v566 biomineralization refinement.
- Configured embedding sources absent; old artifacts preserved. No paid research performed.
- Decision, history, source-recheck and review timestamps denote different events. Working-tree hashes attest inspected bytes, not proof of committed input bytes.
- Issue 1856 tracks a README prose-count mismatch in the initial local draft, corrected before the scientific checkpoint and this review. Current main was not defective. Existing prose-count tests cover the correction; there are no outstanding findings in this final assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261010T234601Z-diatom-perizonium-production
kind: record
repository: CultureBotAI/TraitMech
title: Adversarial self-review of diatom perizonium production
started_at: '2026-10-10T23:28:09Z'
finished_at: '2026-10-10T23:46:01Z'
reviewer:
  identity: codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Author performed this falsification-oriented pass; external
    requests and green CI do not make it independent.
skill: .claude/skills/add-trait/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Three primary studies support the bounded production phenotype. No actionable
  defect remains in the reviewed target; access, mapping, exemplar and mechanism limits
  are explicit. Status remains PROPOSED.
source:
  git_revision: b4d7f0ea857bc488e93e6fe7eb15e6f786736805
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
    sha256: 44e025e8aea453a5ddaee3782037286c44f94cbe4e3de2430242472bd18b8674
    role: context
  - path: app/dashboard/priority.html
    sha256: edcef77cf7309f9bb8228a8f009ec9ecf8b913d41835d4947c4c8f972e25d753
    role: context
  - path: app/dashboard/priority.json
    sha256: 2e4d29541b85ad4c363019d5b4b36cdf18cd3d8f272ef742611a4d2f43966550
    role: context
  - path: app/discussions/data.js
    sha256: 4ed879290f26c2a18be4fea4aed1a77e9d565f177b56caa7213cd72f59a735b4
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
  - path: dashboard/coverage.png
    sha256: 8771265615d9b8cca619766e8d4a32a8a202e4d7d876e6714a7ad0e31ec5eb8b
    role: context
  - path: dashboard/index.html
    sha256: 76336eff0a3bb271632159363d498e59c7225ba64c5c8c8b37f1ea3539b6e8d0
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
    role: context
  - path: data/traits/physiology/diatom_perizonium_production.yaml
    sha256: 25b6c9a02d399e1013aec179770deec4b6791a84748c2d40f6f9ce5537c37473
    role: target
  - path: data/traits/physiology/diatom_seta_production.yaml
    sha256: 69cf1e78c9b4d58f972b2e85fac8433b804bbcd69163f4b90cbdf2961f7ba8f6
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
  - path: history/records/diatom_perizonium_production/2026-10-10T231912Z-codex-d4b43a.yaml
    sha256: ff8108982b48c2a699fdeeb5ac27714ab8808f405b3b304c53961555b1ffba08
    role: context
  - path: justfile
    sha256: e6047ea612115a6a78d100b281483ba824c860c3def59bcd0d40e7fb56b3526a
    role: context
  - path: pages/browse.html
    sha256: 56cb7d2def39c83690d4a08e9eba51cd3962ac33831f2fb6838ddf26332c204d
    role: context
  - path: pages/category/ecology.html
    sha256: 9701513555c5be2ac260ab5865f433d0e083a1858911fb8326c0019600bae258
    role: context
  - path: pages/category/environment.html
    sha256: a64d876d0d0899c3b569325c662d2da46fb0abad4cfabb2f8c8ad3d61e5f480c
    role: context
  - path: pages/category/genomics.html
    sha256: 39ce71b22d6bc9f94e841faf5bf9724abda4b8aa5c956a9c4f4712c72992d159
    role: context
  - path: pages/category/metabolism.html
    sha256: 7de2901a6aad61e37557b3efa951db70946ae05448b8203e041698ed6fc93dae
    role: context
  - path: pages/category/morphology.html
    sha256: 26bd1f4512f3a2acf0d9c6abd8a49fc1c0d4c063a92888f65c6199865917c8ba
    role: context
  - path: pages/category/observation.html
    sha256: cda7fb475694170aecc17e4a63b86cbd17b8bb0288bdcd440ed0d8333565c428
    role: context
  - path: pages/category/other.html
    sha256: ff3f0b24f92033a2bb441aef8a37e6123137841c6fe732cb3a6c6d11f4579e83
    role: context
  - path: pages/category/physiology.html
    sha256: 232af98c0f8e8d94bb8b2c6025b4442b061b432be9f1af4e60e310a2f27bf945
    role: context
  - path: pages/category/quantitative_property.html
    sha256: ba36d50e7057be93a25534dd36ceddf600dea1798415c4d73cd3e095a2a66501
    role: context
  - path: pages/category/upper.html
    sha256: 9803112c67383c91d050616b3d61cb1aeaac1b76015d57475d0c1c229d7c5fab
    role: context
  - path: pages/graph.html
    sha256: d6988008e30710f864a0f25429f4ac3f84d6cfc5c86d4a67216144af8415b200
    role: context
  - path: pages/index.html
    sha256: 9cd14057046eb5d2512c2f0a7a56afe74d5ca03043720664c4fc1aa53dce9776
    role: context
  - path: pages/traits/ecology/animal_pathogen.html
    sha256: fa4c796fcc580d1cc13da13148f59fd1e4eab148012e6ac683a04b8e432de906
    role: context
  - path: pages/traits/ecology/bacterial_cannibalism.html
    sha256: a04fa0076e8a64c57ed9457691d3bb6b064df3f473ca31ee8c8ecd3ea311bbf4
    role: context
  - path: pages/traits/ecology/biofilm_formation.html
    sha256: 4f0538823f0f03547166defc29f0b98e58818c1306667620b87270a3b967c6e0
    role: context
  - path: pages/traits/ecology/biosafety_level.html
    sha256: e3403870bd16d1535eeab6bbe41b2d7b8cc4e0c75d94d29cdd55cbf24d874805
    role: context
  - path: pages/traits/ecology/biosafety_level_1.html
    sha256: 4620a1d4d441e1e055a9792a208a99f28b2bdf6fb9ce993e5606f0424c3fa8d6
    role: context
  - path: pages/traits/ecology/biosafety_level_2.html
    sha256: 1b596b8877e39f6c394e01ce2767b774bc33ccb3177443eb12469bdfbe5f05a1
    role: context
  - path: pages/traits/ecology/biosafety_level_3.html
    sha256: 028e531650e6e60a5eb22de0cb6d39628f9dfb080052ce75c5c236242ae64aeb
    role: context
  - path: pages/traits/ecology/biosafety_level_4.html
    sha256: 4b94c5404dcbd85fe39b86b0fc9280cefa84836cf29b52f8e6bf806a1fedcb81
    role: context
  - path: pages/traits/ecology/biosafety_level_5.html
    sha256: 3c71bac40cfd0582e5cb22089ff901f0060a6803d3554b4daf27c37d162ae3c5
    role: context
  - path: pages/traits/ecology/commensalism.html
    sha256: a3864af050ec5d786695311dd388e0a15118f81b53f839e5bcfb82d2fbfa4b0e
    role: context
  - path: pages/traits/ecology/endophytic.html
    sha256: a54f9a6afa980e2ed0735a0a1dc73c0fd77f9feb19663a56ebb73d6853702bcd
    role: context
  - path: pages/traits/ecology/endosymbiosis.html
    sha256: 6120bc706c6053a11196fcf3a5fd2b7af7751c1512a4bbc1acee014b3cc5dabf
    role: context
  - path: pages/traits/ecology/epiphytic.html
    sha256: b2345c7b34bb1453cd4110755192001d17da17ff39056365263af6f12fa17389
    role: context
  - path: pages/traits/ecology/free_living.html
    sha256: 67d3ab077078840af3325e7fdd87d137537e0a81caa068cca5524f9b84cbccd1
    role: context
  - path: pages/traits/ecology/gut_associated.html
    sha256: 658547b03f2e9cbb361b04547775e164b0df854fc4f11543f4c612daee08ae2d
    role: context
  - path: pages/traits/ecology/habitat_association.html
    sha256: dbb54c321d543f65dd144aaf1491151cdd5ca816c61166ccdf1cee0cb9672390
    role: context
  - path: pages/traits/ecology/host_associated.html
    sha256: d22b19b3342cf5544edbba21de049bcb2849748d5b179cf9632472a82906198b
    role: context
  - path: pages/traits/ecology/human_pathogen.html
    sha256: 94c4a75f4dc4f0fe617dd9d3379170710f00a9eedc296116c530796e279a1b8b
    role: context
  - path: pages/traits/ecology/mutualism.html
    sha256: 0d527d9e79955a44dcef2c664b6e76b93a4dfaac0badf3dd9c8fddee8c1402e4
    role: context
  - path: pages/traits/ecology/nitrogen_fixing_symbiosis.html
    sha256: 562066b6719d4b38c6e93ec2daae70523d445bccef1d4fb1c22a80468e91a07c
    role: context
  - path: pages/traits/ecology/opportunistic_pathogen.html
    sha256: cf4375d52cdcd32d4b98af15eab799f7cedcfbc3376dd1ed54bccc7088563a1d
    role: context
  - path: pages/traits/ecology/parasitism.html
    sha256: 4d6e32f3e722ac9bd23e276e85ec35c54b845e6bc2b8e255a4b6edc2c6df37e6
    role: context
  - path: pages/traits/ecology/pathogenic_to_host.html
    sha256: 369a5ada984c4260a4afa7dc577c1d5d5a3dfaa975bb05606a3497791515badf
    role: context
  - path: pages/traits/ecology/plant_pathogen.html
    sha256: 87427157fe8ebcae3852192327872f7924bda7e31452c0917e32f645aa7451c9
    role: context
  - path: pages/traits/ecology/predatory_bacterium.html
    sha256: 77f033a73c5b82a330b9beee8612f8e928403cdd010289d78be9e6b39ad781ab
    role: context
  - path: pages/traits/ecology/rhizosphere_association.html
    sha256: 0a11a54e708abc1da0b7c511baf1233c54e9470848a3a6ca150141a9235a2ba7
    role: context
  - path: pages/traits/ecology/saprotrophy.html
    sha256: 5a3c40a8927aeea299bd4bce1e13a67b3a62655dd7ebff0f9acecb5111b2202c
    role: context
  - path: pages/traits/ecology/soil_dwelling.html
    sha256: 9346bdcc8081caf77bd4bd674de3e33b0c594f8702f170481050ca5ba16fb3e0
    role: context
  - path: pages/traits/ecology/symbiosis.html
    sha256: d306c52a66b1e2b7ee6a9f4db334b3633e90459a3141cbb0c8f3ec1853eec31e
    role: context
  - path: pages/traits/environment/acidophilic.html
    sha256: c2fd7c94615dc51b8256fe4a0a4ded993a4e4288c9bc5550f3554d5370a40dfb
    role: context
  - path: pages/traits/environment/acidotolerant.html
    sha256: 868e87afe4eac5487923248f49dc0833d6e6e5fa2eab919d0b31f1512e4ca37b
    role: context
  - path: pages/traits/environment/aerobic.html
    sha256: dc77962c49744df87d8e1a6ddceab414ac3c07bab6cb7c536eddcd14b771f7c6
    role: context
  - path: pages/traits/environment/aerotolerant.html
    sha256: 88539f3f5a5dee3da4feee03cc253522b48ab9c519aefd5ef28a7039b13470dc
    role: context
  - path: pages/traits/environment/alkalotolerant.html
    sha256: a94839de086222bdb8378fa279ddf9aba972d9888814e68eafc514d99ab8d96d
    role: context
  - path: pages/traits/environment/alkaphilic.html
    sha256: b43c3480b6b0766f4075ae6303e070bffa20a890a4717a9b8af3fff1b7989fad
    role: context
  - path: pages/traits/environment/anaerobic.html
    sha256: f03912c9f40544bf74b930c74d09ef370534758bad4225738bb8e168be530587
    role: context
  - path: pages/traits/environment/arsenic_tolerant.html
    sha256: f08a54d287239dd4e7797750c972bee47b32155d7292d56ac4212261b28c7ee8
    role: context
  - path: pages/traits/environment/cadmium_tolerant.html
    sha256: bb3d111ca4a180671a54d2198127db03018afb3c68bf69c52ed4c3759fd381c3
    role: context
  - path: pages/traits/environment/capnophilic.html
    sha256: dd1f9326420d470828a8f4bcb57c3f0feb46ff2e1f87d850ab33d9ac2b98530c
    role: context
  - path: pages/traits/environment/cobalt_tolerant.html
    sha256: beb53041f26b3a02c3fd7322654c1bb88e75a00901601c9691fe33252425891b
    role: context
  - path: pages/traits/environment/copper_tolerant.html
    sha256: e18ec7ca2b0c8c6489c790ce136c40f95f21e860c49e0329420988032e48ec16
    role: context
  - path: pages/traits/environment/delta_phenotype_with_numerical_limits.html
    sha256: bad8f68a3a3a1494b8c17bbe82302b37cae010a8e64e13160c466b3bad43b1e6
    role: context
  - path: pages/traits/environment/desiccation_tolerant.html
    sha256: 88bd9f86581dd26d73f39ea48fa864c9c96fc7c392d66c175027cf1db5086c96
    role: context
  - path: pages/traits/environment/euryhaline.html
    sha256: fec6aa9cded912e7fa144fb23230babdda9a4ba85f40fd473101f72789a2d40a
    role: context
  - path: pages/traits/environment/extreme_hyperthermophilic.html
    sha256: d23b8f0d15315410029fafbf4f6f9f29230391db2f89681d3489cceeaa64731b
    role: context
  - path: pages/traits/environment/extremely_halophilic.html
    sha256: 5830067afb4e80d5ab92f4f61e413ca8f0a0a6412f6f9d007fcd8358f4b4684c
    role: context
  - path: pages/traits/environment/facultative_oxygen_preference.html
    sha256: b51e09c8a6d730e6ce338aee0bd2f1ca0d370bc4a6b7cebc43285989525e5870
    role: context
  - path: pages/traits/environment/facultative_psychrophilic.html
    sha256: 77c315b74712613bcd533cfa59112c9de75889e6cfd7a95c2d93bbc08d3481bf
    role: context
  - path: pages/traits/environment/facultatively_acidophilic.html
    sha256: d50ccdde95f4566208184c44b13355e167f369daa9b1a58a531eb62c32ddccc8
    role: context
  - path: pages/traits/environment/facultatively_aerobic.html
    sha256: 214dae0393c8e3649240915c957c199ffb23c2e6b370e94799e27312569bb5b9
    role: context
  - path: pages/traits/environment/facultatively_alkaphilic.html
    sha256: ac33708dbcc2b7c19e3b85bf8bfadcfc68ff5ccab8976eab96a4f11973301c60
    role: context
  - path: pages/traits/environment/facultatively_anaerobic.html
    sha256: 5bfef503abaa14d863407419629afe13e791f55c8cb759fc78e06e9d65ddfe6c
    role: context
  - path: pages/traits/environment/growth_range_phenotype_with_numerical_limits.html
    sha256: 33e8d9e1c5ea9084c2e493c238278cef68a1c6dee4f4dced8d2cb4cd75dda21d
    role: context
  - path: pages/traits/environment/haloalkaliphilic.html
    sha256: e92ffdddf8db27b6dc382190990390745f455484b501160c2816f87717a9a40a
    role: context
  - path: pages/traits/environment/halophilic.html
    sha256: 7b0f6ac7a137face460cf243c1e381a5d169f94e6d765c4466032a470c95efea
    role: context
  - path: pages/traits/environment/halophily_preference.html
    sha256: fb6c3c107ea472f3555d2204d9011be9b88af5e496e594de661b56407133c2d1
    role: context
  - path: pages/traits/environment/halotolerant.html
    sha256: 22faaafcd4cc3419ebecbefcbad38c6d097279e28c69d99c5506719b571d3411
    role: context
  - path: pages/traits/environment/hyperthermophilic.html
    sha256: a2d7f06d8340e169ee2fc690399be49e58549b13eb9274c6558ebf7edcb266ea
    role: context
  - path: pages/traits/environment/ionizing_radiation_tolerant.html
    sha256: b1889b14dc3a1f12cc092c76a33a0f156933f8d9c30c2d81f20c5b397a4586b0
    role: context
  - path: pages/traits/environment/mercury_tolerant.html
    sha256: 338d9680311bb941153eb51bd00957b8ca41d2ee67d5c0dc9d11d19b67839911
    role: context
  - path: pages/traits/environment/mesophilic.html
    sha256: 8da9b902ee04c5a84edc241558afb8bbf08c3f6feba4efa9d6ee0fdac7940f82
    role: context
  - path: pages/traits/environment/metal_tolerant.html
    sha256: e8b78b130f7ff9dad735c5d204175d002a0d02954b31a351a94ac8cf338baf7f
    role: context
  - path: pages/traits/environment/microaerophilic.html
    sha256: c036d2e90585d40c5a9a41bff735aeb7ecb16c2a275bb5f416921dbec4804172
    role: context
  - path: pages/traits/environment/microaerotolerant.html
    sha256: 09a750fea56589a4e1c3bd0771fb321528610a427c3d352c3582d6f46477672a
    role: context
  - path: pages/traits/environment/moderately_halophilic.html
    sha256: 4676805631d5daf78878dd9bbbd705ae6f4287be9afb814370c88163bbfaba09
    role: context
  - path: pages/traits/environment/nacl_delta.html
    sha256: 11ba29dc86a205233664be4ea78a274cac947e26364e71c15b9b6913c0133ea7
    role: context
  - path: pages/traits/environment/nacl_delta_high.html
    sha256: 841f2ad5e831746cbb760b4d2d64e455814067af8b2868a47184bfe1e342de0e
    role: context
  - path: pages/traits/environment/nacl_delta_low.html
    sha256: 33d5aefcb6073c349b8da338d63ec1e22feea3fdf24e1248639cd24d8ba907ef
    role: context
  - path: pages/traits/environment/nacl_delta_mid1.html
    sha256: e24247c8acc17f981678da0f8b3d54a347b1da614b2682cd3a9e004e5aa04326
    role: context
  - path: pages/traits/environment/nacl_delta_mid2.html
    sha256: 0e09b6dacdcb9c0849b9202d7193fce37f5ff8099b7c9ed25b917508f2e17fd7
    role: context
  - path: pages/traits/environment/nacl_optimum.html
    sha256: 274f9022bc8c1030913d7cc28e29354806cc6587c9ecbe22ca94f585797b48aa
    role: context
  - path: pages/traits/environment/nacl_optimum_high.html
    sha256: d68d5f34261e64bcced205ccc9f9f03e97721ec4e74331f43ec59fe99a219ea4
    role: context
  - path: pages/traits/environment/nacl_optimum_low.html
    sha256: 5c7807879917913d0b3ca18e199f5afd33ef8b64db8b4b5346264d294326f465
    role: context
  - path: pages/traits/environment/nacl_optimum_mid1.html
    sha256: 5c9c4896cadc7d935b9e865941a762e64c566ec1f2a9879a0e98a92c73e327c9
    role: context
  - path: pages/traits/environment/nacl_optimum_mid2.html
    sha256: 8a404c70f597805e4c8d42dcb28c8bbd6f22948bc3c1c6e8e55ca0248c03edb9
    role: context
  - path: pages/traits/environment/nacl_range.html
    sha256: 71900921c93d570728e747c40fd4a8585c01fecdd8d23fe2f81985948271c119
    role: context
  - path: pages/traits/environment/nacl_range_high.html
    sha256: cc19d4abb1efaaccb75a3dd9675b6332b62821801699bd3cbeb0feb70167957f
    role: context
  - path: pages/traits/environment/nacl_range_low.html
    sha256: aa260380893954605f9b14d878798d5c7f974d264bccbf84f96a56c0e17f39cf
    role: context
  - path: pages/traits/environment/nacl_range_mid1.html
    sha256: 22842241d17f78e5e1fbc954b110d915199262ab27938a79ce10706a699fca47
    role: context
  - path: pages/traits/environment/nacl_range_mid2.html
    sha256: 7178be401819e6371ba8bc49df266becb894313a991b9d60d542570a7dc0c828
    role: context
  - path: pages/traits/environment/neutrophilic.html
    sha256: 407fbe1c6a0e702b5190f184c973f25b2b47d0ea58ffcde41811b12a2acdb1f2
    role: context
  - path: pages/traits/environment/non_halophilic.html
    sha256: aff4e39feeb287c4db62cd228ef1b6a2e10d2cc87d10bd9ad412af3050330ba4
    role: context
  - path: pages/traits/environment/obligately_acidophilic.html
    sha256: 1b7e1979ffd6c8b654868b74621cd9474d5ea4606867dfae0549ef0ad7e6cb76
    role: context
  - path: pages/traits/environment/obligately_aerobic.html
    sha256: 00490ec2c8cb73d9ecaa38947ed96a79dcadc277f644155e09320e0834fae0b8
    role: context
  - path: pages/traits/environment/obligately_alkaphilic.html
    sha256: 05ca4500fcd9fb3295c9458bce1751a01eb8e6fd5c87eb4e7fec6c32cb8464bd
    role: context
  - path: pages/traits/environment/obligately_anaerobic.html
    sha256: 56553028da4443c79740fd2b4fe805e1fc8a7fe95fbf62ea76687783e63c80f2
    role: context
  - path: pages/traits/environment/obligately_piezophilic.html
    sha256: f641cc2136d95aa614055831f874f8d691b2f1a245934115dd557761bc89255b
    role: context
  - path: pages/traits/environment/optimum_phenotype_with_numerical_limits.html
    sha256: 0561ad5fe9a76f7920baed3eded40688b43085a7f8517b6b6a4dc36875336145
    role: context
  - path: pages/traits/environment/oxygen_preference.html
    sha256: 17d744083948b22f7a9dd55717d2cb3a0e99b67bac354b6e0d16abbea5ed1499
    role: context
  - path: pages/traits/environment/ph_delta.html
    sha256: 4d3783e31c93a45a99171fac2aef3093ebdd2a763f77873d0750337538d3648f
    role: context
  - path: pages/traits/environment/ph_delta_high.html
    sha256: ade1ed9323b6292ab5d566a06b3db9af883895aaed7db41485a6513644074dc3
    role: context
  - path: pages/traits/environment/ph_delta_low.html
    sha256: adf4ce264efa8efa1220cfd4c6363b75b24a5f6defdd192114ccd7e987ee2b0e
    role: context
  - path: pages/traits/environment/ph_delta_mid1.html
    sha256: 52ac368aee50558643714e5635a9bf9812504d1f25aeab1a88c40e846b679c68
    role: context
  - path: pages/traits/environment/ph_delta_mid2.html
    sha256: f56ba7ee838f01e848091325da29f4bc3159780e167e309ff9908cebdea01a55
    role: context
  - path: pages/traits/environment/ph_delta_mid3.html
    sha256: 5829b6d10acadc555fd0a497c2e7e0f835735e0b4e2bf7bf61196c0ac881bb0d
    role: context
  - path: pages/traits/environment/ph_delta_very_low.html
    sha256: 5fabd2292796ea88ded6af8350989ceffeed4b8b23b01dfc4deca5890851e348
    role: context
  - path: pages/traits/environment/ph_growth_preference.html
    sha256: c2afed0368e4040589a3388f542cd694effaef56a5480854e8ae720317276fa2
    role: context
  - path: pages/traits/environment/ph_optimum.html
    sha256: 49dc6b24370bc0469081df639ba7e528823b645741b353e48acd56f9b1331125
    role: context
  - path: pages/traits/environment/ph_optimum_high.html
    sha256: 2e6fc7e7a6c01144ceef2024e52ef3458eca5c4c68348e0fc40e8a18eae4c4af
    role: context
  - path: pages/traits/environment/ph_optimum_low.html
    sha256: 3a0e0918878f30e1677b16ccb9d883e74d012046f2fdd068058f456c0d7e6751
    role: context
  - path: pages/traits/environment/ph_optimum_mid1.html
    sha256: 197594b82182bfec93459a20211ebdf27c6c21290b71b5967738312b770b5182
    role: context
  - path: pages/traits/environment/ph_optimum_mid2.html
    sha256: f024162926a3f850253804bc39780ae9ae778fea11f774c301d0a7e57c7b466b
    role: context
  - path: pages/traits/environment/ph_phenotype_with_numerical_limits.html
    sha256: 023751a9f07e950345a7c4096035564979feacf832ff483379e93aba6f62777a
    role: context
  - path: pages/traits/environment/ph_range.html
    sha256: 44887d4d93879019d4f0925d2ab5f312785e9da4fa2ad8247be14c48c105ae1c
    role: context
  - path: pages/traits/environment/ph_range_high.html
    sha256: 2da4674ec55b8aa9bd85cd62f683e8e0d69d343235a66062e20a21dff4fe7c50
    role: context
  - path: pages/traits/environment/ph_range_low.html
    sha256: 600e851eef5f30ade17cdf32174d756a4536556777840607fb2310085ec1a67d
    role: context
  - path: pages/traits/environment/ph_range_mid1.html
    sha256: 4e10226350387ca7cca7a6dbb70dd016abcda293e6f9f8f7895d5b92d3f6709d
    role: context
  - path: pages/traits/environment/ph_range_mid2.html
    sha256: 8797bdca07aec985ca2533f5f22497bf623354a8b23892b224bf5c9393770fa7
    role: context
  - path: pages/traits/environment/ph_range_mid3.html
    sha256: be23c1b1053905887412c887f56dcdee4701a6b6815a106d3071d87fb7669c2d
    role: context
  - path: pages/traits/environment/ph_range_very_low.html
    sha256: a90adaf86c2e841fb107b2d008a4b95bf6decd0db88f1e1ab4b03cfc465ed329
    role: context
  - path: pages/traits/environment/piezophilic.html
    sha256: 02df419a3faee1d3253dc6b2a47ea42900a29cbf19b9c0950f59075b5d79047b
    role: context
  - path: pages/traits/environment/piezotolerant.html
    sha256: 00499a9f9fe1537791c616b5c6724cbfd8b749bfb5cd06db2e26fb0c9537588b
    role: context
  - path: pages/traits/environment/pressure_delta.html
    sha256: 8f934a010e6baf0629b05da1e5b41e3b7353b59c10316a737ec1920b267bf026
    role: context
  - path: pages/traits/environment/pressure_optimum.html
    sha256: 253195e5d12ede75d8be6d47886042874e282ee68432689ff32f781914108c65
    role: context
  - path: pages/traits/environment/pressure_range.html
    sha256: 1996ecb8b4b2a28ce66ed4f678c8bc0b12e98cdc60b7dc1d5931fc948b82c684
    role: context
  - path: pages/traits/environment/psychrophilic.html
    sha256: 34132a065299d891801b2b5a342947b713f599266345c6dca513b0bd094fc17d
    role: context
  - path: pages/traits/environment/psychrotolerant.html
    sha256: ceb98b341defc82f64eff0f3c3e97e1664187dcac1a202833f29cce4bce7de60
    role: context
  - path: pages/traits/environment/radiotolerant.html
    sha256: 0220149bf1c21e73e0fc6e18838c263471ae3e837ea30fb2099a22040247d47c
    role: context
  - path: pages/traits/environment/salinity_phenotype_with_numerical_limits.html
    sha256: d8707d55732bb92dad494d10f9946cfe21aac73ee46911a21542f8f2e7e6cfb0
    role: context
  - path: pages/traits/environment/slightly_halophilic.html
    sha256: 6b8ab7e541ac088381aa6adcc5ba4fdac66ddb33c91efb0d90c72c2bf1457932
    role: context
  - path: pages/traits/environment/stenohaline.html
    sha256: c534ee3c4cb970afb163faf4b3ee4575b96c65542421731d80feb7bec3c6be74
    role: context
  - path: pages/traits/environment/strictly_anaerobic.html
    sha256: 43762de207410632e25a02c0a5ecc7712b1dd58f139dbe2e76d5e1d8da55aea7
    role: context
  - path: pages/traits/environment/temperature_delta.html
    sha256: 1e0d449c5de2e1ddf99ff63cd97b2727fdbbbf31d6737ead801dda9b4d688203
    role: context
  - path: pages/traits/environment/temperature_delta_high.html
    sha256: 1f82cee0a8174ddaaac595ee53395497fbf99f1e3bcbeb4828082084fb7420e7
    role: context
  - path: pages/traits/environment/temperature_delta_low.html
    sha256: d9d5baf067bf9d01c57b086394e21e49d2d5d5bb2fab8badb366ad00b2d37dda
    role: context
  - path: pages/traits/environment/temperature_delta_mid1.html
    sha256: 5e883ff79234a1ee8c6534ddf33b34e93c19d6a004f9817c267006ec0bdf941b
    role: context
  - path: pages/traits/environment/temperature_delta_mid2.html
    sha256: f191910134e13c5cf45df3eb0654811fdaa0a2c64a138d8e4b8abfec1c676b6f
    role: context
  - path: pages/traits/environment/temperature_delta_very_low.html
    sha256: 642a575b18299ebdcf0c2c373f2d01f6913d7293ee1b0db8e3bb7213b6f8743e
    role: context
  - path: pages/traits/environment/temperature_optimum.html
    sha256: cbe87fabcc57d3bbbb03de3acf32ae0d53aaa735ac20c05d8624e802dddf4c37
    role: context
  - path: pages/traits/environment/temperature_optimum_high.html
    sha256: a5497eca3f74b7868d6941e5a714cd7009a3331060872e01267121d4016f3ced
    role: context
  - path: pages/traits/environment/temperature_optimum_low.html
    sha256: 1c539ce1d468a5b08a338be5e146ce08edb52581ce5485fe0235a06fb44948ee
    role: context
  - path: pages/traits/environment/temperature_optimum_mid1.html
    sha256: c711ea7d182d61b407df975fe656b72662f9ea2e5878ded0641df4e9176ea465
    role: context
  - path: pages/traits/environment/temperature_optimum_mid2.html
    sha256: bc5d62e5e2f59f30aa6063b6f65e2a49d5eeafa0eefc72a695118f1c6239da23
    role: context
  - path: pages/traits/environment/temperature_optimum_mid3.html
    sha256: 637a8ff4d008517e1a222154d812acb101015c011cc4952a90ab0e7cbb4fc1aa
    role: context
  - path: pages/traits/environment/temperature_optimum_mid4.html
    sha256: 7531ba0ccb8b92acafb265ec3603efcac2f893a170cdd0833117ad19023010b5
    role: context
  - path: pages/traits/environment/temperature_optimum_very_low.html
    sha256: 0509ccdcfbb01ced714aa70b8cdf41c0b784958ce7ff59ba15930e684ba544ec
    role: context
  - path: pages/traits/environment/temperature_phenotype_with_numerical_limits.html
    sha256: 6659cc91a9dcac09813d4cac5ce92249906175091301d7bece207fd0559141e9
    role: context
  - path: pages/traits/environment/temperature_preference.html
    sha256: e5340617a8cfeb3dbde08c619e4e5028c04b79758ba2a93f1fbf8aee0064fc93
    role: context
  - path: pages/traits/environment/temperature_range.html
    sha256: 00377d6ef885af2f15f8f018978a1544304a5b66f07607fe5b5c8ca2a0b7a95a
    role: context
  - path: pages/traits/environment/temperature_range_high.html
    sha256: 42beefc287f5469e49ecb22db68a6dd651d810513615be4fc6d608ac665fe41e
    role: context
  - path: pages/traits/environment/temperature_range_low.html
    sha256: 95250ce3c4bd8c893847a54a92ff108777a6e6b438936230d780455769feafb4
    role: context
  - path: pages/traits/environment/temperature_range_mid1.html
    sha256: 0a98b1ceb2541dc3d8e2d7d690fe4bea7df7f728380c5e3d1a2b798736c331bd
    role: context
  - path: pages/traits/environment/temperature_range_mid2.html
    sha256: 61fde9e8ccf62e2aab27dd22a8f070f2d4c9ae5aa5f852bb4c64e2ea1d762cd2
    role: context
  - path: pages/traits/environment/temperature_range_mid3.html
    sha256: 9ab9307ebf4cf23f32f7aea48ed510cce826040c80a76a5199a8d04650b1be90
    role: context
  - path: pages/traits/environment/temperature_range_mid4.html
    sha256: 4038987144bec2ca59ab59f3ac9178ebe4e5517b3ba44473b766a6cef0df32eb
    role: context
  - path: pages/traits/environment/temperature_range_very_low.html
    sha256: 64b8b0066bff145a2ded1902cfb749fa198143eeb2ed2a8a95526b0fa7ddec53
    role: context
  - path: pages/traits/environment/thermophilic.html
    sha256: 2ac9fc448851b7cd07aba26dbb2a99870f793bac33f484df3992d08b65ea7a61
    role: context
  - path: pages/traits/environment/thermotolerant.html
    sha256: d108e3b4ec75a37833501a69fa934619a4058579764c335598267cbc1ad54e24
    role: context
  - path: pages/traits/environment/uv_radiation_tolerant.html
    sha256: 829462840cdeb61fddd25b5608a2c255c159abfa124507f091de913632774377
    role: context
  - path: pages/traits/environment/xerophilic.html
    sha256: 818a8f93220e7b22498aa13cc43b4f5407acafc0cf36b7944b4f2371a4da8cb8
    role: context
  - path: pages/traits/environment/zinc_tolerant.html
    sha256: 851528a8980c3684d9e5f74d18f4551955b7a33f109db534424c7cbc55d4caba
    role: context
  - path: pages/traits/genomics/abi2_system.html
    sha256: b8a44a8ab49dd2a4938eee115b270be430d7c9b529f2dd51fca08e0f5e4688d6
    role: context
  - path: pages/traits/genomics/abia_system.html
    sha256: 890f5863eef19c462e7d25a75c814fdb93bad65a7198618d3c42117245f7210c
    role: context
  - path: pages/traits/genomics/abialpha_system.html
    sha256: 188e88b1402a7b2ffde34f4ef89bb9af1fdb7cc3d465cb483308d133aae91870
    role: context
  - path: pages/traits/genomics/abib_system.html
    sha256: bd7899ce8da03fb7b07da6493363bd72497e83a83fe44cbc782bb5cb7400e7d9
    role: context
  - path: pages/traits/genomics/abic_system.html
    sha256: ebd54f287949530dbed003662094645188893d9b763cd678b0275f1f88cad576
    role: context
  - path: pages/traits/genomics/abid_system.html
    sha256: 787a010df7a5f9651fae05d5c132b83fd89dcd46864b9e53208604e6252c41ab
    role: context
  - path: pages/traits/genomics/abie_system.html
    sha256: 1bc3449c800ce72e40bba2386d6394acb31941791448840b056ef9b45c61c14d
    role: context
  - path: pages/traits/genomics/abif_system.html
    sha256: 64b38803daf220450d99f255f05fe98ed94062440d6da8ca8b0e895f1da7093f
    role: context
  - path: pages/traits/genomics/abig_system.html
    sha256: d57b29cf15584cf4a02629a23afaeb8f8aa6376a72a829e904fd6b0ecd461e99
    role: context
  - path: pages/traits/genomics/abih_system.html
    sha256: e820debb6105d38b0c9bdc5e6147cf7218b13e35a14fc36239440149b9d9bf8d
    role: context
  - path: pages/traits/genomics/abii_system.html
    sha256: 4af36a07f1344c80a55de6c862e6ea7e2eaddbbd70240143efd5c48bafe3b6f7
    role: context
  - path: pages/traits/genomics/abij_system.html
    sha256: 78d5948f8e6f0d7642dc2093486f4cababe87541799e7ca872525e153db4454e
    role: context
  - path: pages/traits/genomics/abik_system.html
    sha256: 656dac370ba3d03b5fb9f3164dce6d9be9cd4d2062b2aba9c57c1c34a2ebbb7a
    role: context
  - path: pages/traits/genomics/abil_system.html
    sha256: 0740c544809c82d1d06a631d40b08e21a907acd4494648cb58f71cb57de77dcd
    role: context
  - path: pages/traits/genomics/abin_system.html
    sha256: 1e911141212ba42af8fb8488e8c67a68e3fa54b1a106b48725c8a94ddfe53c36
    role: context
  - path: pages/traits/genomics/abio_system.html
    sha256: b659aebf1112452f7c86edb6c5a6c9415388a9608758dad6edb597bbfd435bac
    role: context
  - path: pages/traits/genomics/abip2_system.html
    sha256: a6160f1facb78c6eb45be204f9fe022a21c83159ba21121802a1fd9411f042ba
    role: context
  - path: pages/traits/genomics/abiq_system.html
    sha256: 59f6dbd85bd0ce2adf79c9cf8accac87974a573c6a77eda756bd45f3d712ff10
    role: context
  - path: pages/traits/genomics/abir_system.html
    sha256: 6ceb8d876e0b9b968f750918e14a6263d9ea926dc01216da7028a72180dcb9ea
    role: context
  - path: pages/traits/genomics/abit_system.html
    sha256: 811ef4acba498b921447276d2e4506f2e5d3a573b8c978e7513021adbde3b73d
    role: context
  - path: pages/traits/genomics/abiu_system.html
    sha256: 9f4fd452018c52948edd6497abcecd48474a150aef46fe7a4024a867ce237b76
    role: context
  - path: pages/traits/genomics/abiv_system.html
    sha256: 413e8dbb8e61b20887b639da2dd9a552251f45ec2a63d27e6bd9e9733345d87e
    role: context
  - path: pages/traits/genomics/abiz_system.html
    sha256: 669061afb002f9581cb1dfbdb62197685059122e8799b18d80fce61bf6674d84
    role: context
  - path: pages/traits/genomics/abortive_infection_system.html
    sha256: 6ab8c923dce626b9b8bc0736ec674b29801b8ad6cf5ff57a73d07ffaf3b096b5
    role: context
  - path: pages/traits/genomics/aditi_system.html
    sha256: 51409022f9f5bd59d6d2a024bcde92cacce1d34346b07708aea6421255968d85
    role: context
  - path: pages/traits/genomics/ambrosia_system.html
    sha256: 53b51c47209ab6175b25dd7015032963b30d3a7786e0e18b14f11681954636a4
    role: context
  - path: pages/traits/genomics/apsab_system.html
    sha256: 2950e322f7af18e12a5982c354de830e67538141f57b0f87d49af4ecc4e7e8b6
    role: context
  - path: pages/traits/genomics/aristaios_system.html
    sha256: 6743371c37e18daa32b6b28166ccada73084d9473540e42705de78f3745cc52e
    role: context
  - path: pages/traits/genomics/armada_system.html
    sha256: b37c45ac04f67f7ac55fc4ef86e9a40e759172ff4a7c0eedee11b1e67fcfd10c
    role: context
  - path: pages/traits/genomics/audmula_system.html
    sha256: 36ae02007b8b60818cd90a590e739e196ec8a4342c91cf93b4620cdc700e6314
    role: context
  - path: pages/traits/genomics/avast_system.html
    sha256: 9287da6d90636d9652e9cde978a4f869394536b20e152bba4f3072c2c83445de
    role: context
  - path: pages/traits/genomics/avs_i_system.html
    sha256: 3fae8d8798300ba2f58488f714b43b7e7654654e997f27ddabf093bb09ca0886
    role: context
  - path: pages/traits/genomics/avs_ii_system.html
    sha256: 85434dbd9f940534dc3dd13a2582de2ab8ae2ce2359ade4996e325d941f4a878
    role: context
  - path: pages/traits/genomics/avs_iii_system.html
    sha256: a9668e7249c57c45c4e49296986402ca7c2f4a4b223e6173b96314779f4b0558
    role: context
  - path: pages/traits/genomics/avs_iv_system.html
    sha256: 6820260746671c0c20594b8d22298da525c27336da82240ba72ba345ba925d9b
    role: context
  - path: pages/traits/genomics/avs_v_system.html
    sha256: 075cd2139627b8dd43b736a41c5f3d603afd788c3e39a4089cb4f21b83d40448
    role: context
  - path: pages/traits/genomics/azaca_system.html
    sha256: 99f9bf539f839c16ea2c6d2d313a40744dea7fef4e9e2497b00bf7b8465e54b0
    role: context
  - path: pages/traits/genomics/belenos_system.html
    sha256: 9b9319fc6fbed8369d321769bf518881eb4a754dc72f672434139064b4213800
    role: context
  - path: pages/traits/genomics/belisama_system.html
    sha256: 7a1bb4411bff74071676de97fcdecec403f42a2a56a924f6e3ce2238454c271d
    role: context
  - path: pages/traits/genomics/bil_system.html
    sha256: a5badd71f804037179865218e8215792f755a131d7ac239d13963d1241f3e1d2
    role: context
  - path: pages/traits/genomics/borvo_system.html
    sha256: 8ead5b39fd718e7fb2521b1e7f8a414f4493d859a955cc8fc7faaa5d891d5e4e
    role: context
  - path: pages/traits/genomics/brc113_system.html
    sha256: 466c579e06b93d903f9f9c50a7ff876813307569bf6097691fe411c22d45d3f3
    role: context
  - path: pages/traits/genomics/brc142_system.html
    sha256: dbdf0e9d6296f341bbbb912794931110da15a7765868a1617ab1fa1ae63f5e5a
    role: context
  - path: pages/traits/genomics/brc167_system.html
    sha256: 95bb9eb6c02b05f3b4d919dba33e224555a2f981721cb7d8bce61ba239a3668b
    role: context
  - path: pages/traits/genomics/brc217_system.html
    sha256: 4d13b5f24189c71898c9ced06ebdcac7f6a7d6faa717e12825c5f21f4089c50d
    role: context
  - path: pages/traits/genomics/brc22_system.html
    sha256: 4411741452bf843ba66aef383257b4bfff8cdcf80d5628196ad496624b509591
    role: context
  - path: pages/traits/genomics/brc233_system.html
    sha256: 7f967cbfb199c284ea79b9b38f18d5c4e78557e4e2cda3a2f7def0b31a9aa2a2
    role: context
  - path: pages/traits/genomics/brc23_system.html
    sha256: 52afc535839cc7bdcfead2161ceae018674ef91d94bbcee86f45fd1e86e182d8
    role: context
  - path: pages/traits/genomics/brc24_system.html
    sha256: 679df4c8b1b13360cd9c850ed7f35bbcf16598aa6112b77c277312599ab92fb4
    role: context
  - path: pages/traits/genomics/brc59_system.html
    sha256: 5014f67cc42975e38447b0d52155c60f32ed59b734903aadd543ff798aa4dc3e
    role: context
  - path: pages/traits/genomics/brc76_system.html
    sha256: 2a6ea2b68fdb8ee58bca9fb8daddaebeb6eb3413339d4f4dd9eb10e5ab16cdfa
    role: context
  - path: pages/traits/genomics/brcwgs21_system.html
    sha256: 47055512892f468a74e06f82f8b7c45ee99945bae0b87bd8eeea548d2e396857
    role: context
  - path: pages/traits/genomics/brex_system.html
    sha256: 78c79f3d06bb0e168b16d1379935d783be00c3abdea9d2f4f0ea3fac27412f11
    role: context
  - path: pages/traits/genomics/brig1_system.html
    sha256: bb565b8277ef38b82cef5a3512b4af8f9cc988428427df4907b8dbdce8785eee
    role: context
  - path: pages/traits/genomics/brigantia_system.html
    sha256: df55b932920c84c22f79b5ad4655766ef063a6c9f2484c2e4bd3afdc46e11744
    role: context
  - path: pages/traits/genomics/bsta_system.html
    sha256: 1e5a3c43fd9b1dc17e621a1e531cffa31e985ccc031786a8205873e10f2d1d1c
    role: context
  - path: pages/traits/genomics/bunzi_system.html
    sha256: 3c2563048bf6b778579b2a51e30d881a5fc3d4b32800af7ef671508a28b2ed77
    role: context
  - path: pages/traits/genomics/butters_gp30_gp31_system.html
    sha256: cd938a3cb9ee1da05eb5b1bb50b19abd48d163dc0fe425e720d9476e96c8205f
    role: context
  - path: pages/traits/genomics/butters_gp57r_system.html
    sha256: 9e755daecbf5c9fc9d7e57eab6b9123554291f22fe464f33093e025fb823ae19
    role: context
  - path: pages/traits/genomics/caprel_system.html
    sha256: fed60d1a82641da4e4ef5d8ccdd412c87cf1585a20c726199c0e5ce8beb1290e
    role: context
  - path: pages/traits/genomics/card_nlr_endonuclease_system.html
    sha256: 2c011f937ef551acd52630214692ea0bec1185aedde2c6a13d286fa887397574
    role: context
  - path: pages/traits/genomics/card_nlr_gasdermin_system.html
    sha256: 5684c8ca7599db1be2f4ef9a8899983e3e487ebd67829035029596479aa504f4
    role: context
  - path: pages/traits/genomics/card_nlr_like_system.html
    sha256: 2fe7641f66c366051b6a73cb87100e6a7911cf1e1aa3ba37176fae3608e87fa5
    role: context
  - path: pages/traits/genomics/card_nlr_phospho_system.html
    sha256: 000ef29acb52cd8a56f764f4e51ea59eab0e89d87f1a20f9eeae132bbbc6623b
    role: context
  - path: pages/traits/genomics/card_nlr_subtilase_system.html
    sha256: 5f1a8f405c2f7087b4f7d85b2a268622c2ffb33c389928531ee35675f07a201e
    role: context
  - path: pages/traits/genomics/card_nlr_system.html
    sha256: 8343d5bc365d13c5e8b51a878aebc8dbc6cee77f91186238bda9fb8d3f7a044e
    role: context
  - path: pages/traits/genomics/cbass_system.html
    sha256: 7a715c5d3e14c4ccaf76cf80b98ccb3f2f2497bf310a51ac079ce16e63010834
    role: context
  - path: pages/traits/genomics/ceres_system.html
    sha256: 47c228b82e3f0da8af59a7c10cc745e6900a8072c3c2d21ee56cfddcc77f769b
    role: context
  - path: pages/traits/genomics/cernunnos_system.html
    sha256: 9ff8ffea128ebcd08e101cf78050f7bcb33c9747e423c974a3c21ca136ac324d
    role: context
  - path: pages/traits/genomics/charlie_gp32_system.html
    sha256: 3cd6334538ca1d972907b260c3f56c20c6e06e95f1dca693dcda82f60ce26d23
    role: context
  - path: pages/traits/genomics/clover_system.html
    sha256: 52393bd8af512e17e73cdf54a38d8100a21df7f8303503c675a876ce3673f489
    role: context
  - path: pages/traits/genomics/cmdtac_system.html
    sha256: 4b496027d1e2a1e76d691d6da14fc136cacbecc14a7967c00b2b625a00136204
    role: context
  - path: pages/traits/genomics/coconut_system.html
    sha256: 21c9a5e3315c84d0c2ee3d158e3583f8fc7027c85f7daa0c7471f973bb3ea3fb
    role: context
  - path: pages/traits/genomics/codon_usage_bias.html
    sha256: 1339c82a641c53cbc61cbd6462019a873bc1a6f95e160ecc1f172724b8d7d02a
    role: context
  - path: pages/traits/genomics/crispr_cas_system.html
    sha256: 4d0329a6bf7a36a13e98e1f908ffa3838c2fc69e9c276feb4cdd6d6b13e2c3b8
    role: context
  - path: pages/traits/genomics/crouga_system.html
    sha256: 2e2e73f3a8975d03f57eb3692a7e5db487c8c6fe539a5088a7dbb5525d7bc673
    role: context
  - path: pages/traits/genomics/dag_system.html
    sha256: c3e2f416aa880ab5535b9629aec2b2c66fa73e1730436028794f1cf6a8e2bc3c
    role: context
  - path: pages/traits/genomics/damona_system.html
    sha256: 386c0aee1cb0e5e89b9e416998fb35095b3a5251e1b81dd8ba153e7634cba3f5
    role: context
  - path: pages/traits/genomics/darna_system.html
    sha256: 3e5f9974606e3a7fcc722d0195c24f8d56baccdf3b2c09acd97597d3bb615132
    role: context
  - path: pages/traits/genomics/dartg_system.html
    sha256: 0b35238c7e9b29174cc941d46ec87794303df97aa20c0a78861d5455b1472091
    role: context
  - path: pages/traits/genomics/dazbog_system.html
    sha256: e4bfbfdf89c21732b7fbb207e7d53b2f25f8f19e68339f346ee059b69be93cc5
    role: context
  - path: pages/traits/genomics/dctpdeaminase_system.html
    sha256: ad74c8bfc5a7460be1c505ce2479e2318cec03833e17eaaa2863c2b888774370
    role: context
  - path: pages/traits/genomics/ddmde_system.html
    sha256: 1ca845a4bf1718116a8867f0e7cde44148f9da5fd497e6e09c78a9c1739a8467
    role: context
  - path: pages/traits/genomics/detocs_system.html
    sha256: ca15fe16c653c1657c503c48b51d0cebb7462fad7d98f378d9597b8eaa50050d
    role: context
  - path: pages/traits/genomics/dgtpase_system.html
    sha256: 2718c0df32f5b53e79d72254ad961447f97984279e91d25d93c78eadb1ca096e
    role: context
  - path: pages/traits/genomics/dionysus_system.html
    sha256: ab57a5526c93e6e14510f1ee0a248ffa1d50baafd4129c093f6e2ed3b89a1339
    role: context
  - path: pages/traits/genomics/disarm1_system.html
    sha256: add1063efea8e308c23327c313998851d19e60b176af6bae0e850cb7b1a20677
    role: context
  - path: pages/traits/genomics/disarm2_system.html
    sha256: ce7a5a33d346dec76ab79e2c698bbdc53b6d2cb38837c6beec27f927adfb1b65
    role: context
  - path: pages/traits/genomics/disarm_system.html
    sha256: 57c67b0106cb02101f2a902defa9412c762ba56ca754c07e63ef4ec654d8b916
    role: context
  - path: pages/traits/genomics/divona_system.html
    sha256: 67fbe16783419593ae014f5eefcb66bf2bde08047ab41c9753990c3972b093be
    role: context
  - path: pages/traits/genomics/dnd_system.html
    sha256: 4aab0998658078168bf2c7920ec1e739dc8d1c9b5874edb4b4033412347003f1
    role: context
  - path: pages/traits/genomics/dndcdea_pbeabcd_system.html
    sha256: 18deb0b8ecca95f03a9c19a6e235f5cb2106900db4aa848e89486f1992149a8b
    role: context
  - path: pages/traits/genomics/dodola_system.html
    sha256: 1a18e19de032eeaea6e0c8c4a03a7beb8ec32f5f756eac6787b7b2b0e3793fa2
    role: context
  - path: pages/traits/genomics/dpd_system.html
    sha256: ea026db9d7a0aa6fbd4a098927d467ee13e30966bf42378b05f8afa58098e4a3
    role: context
  - path: pages/traits/genomics/drt1_system.html
    sha256: fd45fc7b7180ea6b9ff70897c68a1eb505c91334eb90f0096fb26b624f5f11a3
    role: context
  - path: pages/traits/genomics/drt2_system.html
    sha256: 91c8c8943a4729e96b943807cdb7230b9ad7f15d0f83d62aeb61b421dc8f0c2d
    role: context
  - path: pages/traits/genomics/drt3_system.html
    sha256: 1e986749e085185f9d2250b521909934f7583f54bf64e8444f2efaa379e22164
    role: context
  - path: pages/traits/genomics/drt4_system.html
    sha256: 59e6fe1538fc9774adac0ae257d3474557c368a7db8689fbfafb4d00b096fbd4
    role: context
  - path: pages/traits/genomics/drt5_system.html
    sha256: 6d6e2a4651e911f13cc7b665e00f69758baa9aaeb95721f40e4351559a6d4d16
    role: context
  - path: pages/traits/genomics/drt6_system.html
    sha256: cf04e085261080e86fb08cc21a8ddf4234811ecb3ee489217b8bbb43e7e0a2ff
    role: context
  - path: pages/traits/genomics/drt7_system.html
    sha256: 4a55ab2b6106a8697273d14e5dddcc95ce4922af823ffeb1119cf5e8118dbb3e
    role: context
  - path: pages/traits/genomics/drt8_system.html
    sha256: ba268856b1d0951c86e1f1ca89bf92e4dd72aa1c703e707fd3bef3c201d8db74
    role: context
  - path: pages/traits/genomics/drt9_system.html
    sha256: 805e710be69ee05022b8ab07942c62e72b198e34b66b9b2b31db76780a96d09e
    role: context
  - path: pages/traits/genomics/drt_system.html
    sha256: eecee0f0689c2ea8fd398a2c8e057aff61de8c806870e1f00011be0bae42e905
    role: context
  - path: pages/traits/genomics/druantia_iii_system.html
    sha256: 9ad0b1e34ca1da2da586a6f5cab6593f90ba4f7e75645efb83e525c3b1db315d
    role: context
  - path: pages/traits/genomics/druantia_system.html
    sha256: c9a7b2b2567b38c7b7288e64872362f048eb8171447b6a93d649e868ce3b870f
    role: context
  - path: pages/traits/genomics/druantia_type_i_system.html
    sha256: 2583fee03be36300c3545764aa44803d008e7593f1bf2f5bc5e553fbf37704e8
    role: context
  - path: pages/traits/genomics/druantia_type_ii_system.html
    sha256: 859673fbb100973c9faf81784f47502cb95cdf9b7828247d3ccf2033ab460e2a
    role: context
  - path: pages/traits/genomics/druantia_type_iv_system.html
    sha256: a94b004dd48c51475c5b48ecb946bb9e032a07ff891dc151ca6e597ba4ca4d1d
    role: context
  - path: pages/traits/genomics/ds_10_system.html
    sha256: 8327b194d8304a137532db6c34eef52361b085c8053f712e399c23d6f72b4942
    role: context
  - path: pages/traits/genomics/ds_11_system.html
    sha256: 6ff4e558007d66fae239774ca7b8b6547210e2c1736ed830d60637e027ae0843
    role: context
  - path: pages/traits/genomics/ds_12_system.html
    sha256: 6c43fe2f7728ea7cf577267599e1be02f64ba6427e8ead139f11f7f4cc84d517
    role: context
  - path: pages/traits/genomics/ds_13_system.html
    sha256: e057a54319ff7edd68ddfdfdb9bc625829bce52078cb5947d7b0f88c9c5690bb
    role: context
  - path: pages/traits/genomics/ds_14_system.html
    sha256: 56bea9fed3e750edc7b7164c2491e1ca8c5b43f1d985b042132f8ef25a15f7cc
    role: context
  - path: pages/traits/genomics/ds_15_system.html
    sha256: 761e30aaf0ab5521ccf2a820e3473481a5e3441f86e8228a448621caefee518c
    role: context
  - path: pages/traits/genomics/ds_16_system.html
    sha256: d6d888f14ff8359dd421d1cb2666cda29a48d49e5e5fd3d5afa2f3835fbb4650
    role: context
  - path: pages/traits/genomics/ds_17_system.html
    sha256: 151bf959e05682b58e0f29c5e03bd2cffeb10fb79893b9c3af26ecdc2deae672
    role: context
  - path: pages/traits/genomics/ds_18_system.html
    sha256: d11e832ad512da621861d6b0b4ef747f2ff10195f1e6aaf19a0dabc40e61ef4c
    role: context
  - path: pages/traits/genomics/ds_19_system.html
    sha256: 884bf2599915ab705fa1e13a7ad8716376fc14a105e634ed019feaf63fc9faf7
    role: context
  - path: pages/traits/genomics/ds_1_system.html
    sha256: 50eeec9920db83c556fa7d30aa0e2e70c4458ecf24a343a6489891f1258f9010
    role: context
  - path: pages/traits/genomics/ds_20_system.html
    sha256: 4b3c01bd1896b14714d1c59d3cbc8442c269d94e1b51c1c5e59297c026ee1064
    role: context
  - path: pages/traits/genomics/ds_21_system.html
    sha256: 20cc72d3745223e8b3eb36822511dd63227cf93ef978e3dc3567cf4940e6b673
    role: context
  - path: pages/traits/genomics/ds_22_system.html
    sha256: d0e5c2aad6190ee2854903fea9a21f8846ebd8b536934a9835125dbb88dfd145
    role: context
  - path: pages/traits/genomics/ds_23_system.html
    sha256: c7e88afe9997d58a3c10327ed3e4c4efda11650891c018ebfa2545b49ad6fa2f
    role: context
  - path: pages/traits/genomics/ds_24_system.html
    sha256: f3f11c2386049f997b6a9af87253ed080a5b1e5a4320d40cc4ea5aceb024e656
    role: context
  - path: pages/traits/genomics/ds_25_system.html
    sha256: 4f96cc9dfeb04f55903748c52799c8797258358d6f6fd3594619d891eb6056f9
    role: context
  - path: pages/traits/genomics/ds_26_system.html
    sha256: bfc13f4ed6cec654138eb9c6ddb64f8a3e6c98dd9d34df65501a1f1dd1700265
    role: context
  - path: pages/traits/genomics/ds_27_system.html
    sha256: d9084920262b0c1b9ba279434e0ba0235b9f5527503b4a0cc4c482cfe3cc5788
    role: context
  - path: pages/traits/genomics/ds_28_system.html
    sha256: a7467da317846598346e1166d02b5528af6b59c7764a36682c558095f0c75b77
    role: context
  - path: pages/traits/genomics/ds_29_system.html
    sha256: b6e16ba653f69d0059cae11338dcbdfe97f1256df084cb2c92c524311d0cfe23
    role: context
  - path: pages/traits/genomics/ds_2_system.html
    sha256: 5ab64afa7afd28f88804ca8d36e6ecf4bf1a8d688cea7c991070302b78f8325f
    role: context
  - path: pages/traits/genomics/ds_30_system.html
    sha256: db64b363c69807951f5a7809f196a1a50cf40352d267f45f7e5febb9993b7b92
    role: context
  - path: pages/traits/genomics/ds_31_system.html
    sha256: 8aa96afacd9baa95c7cea087e188b111231100927862cc96df8a841ac6325f72
    role: context
  - path: pages/traits/genomics/ds_32_system.html
    sha256: 5f623b1408a2ad296f501948d9cff200bbe7da758acaecd328f5ee92d743aa7f
    role: context
  - path: pages/traits/genomics/ds_33_system.html
    sha256: 2c26076813e07dd87c2a2ae0ce4f713161ffb5f49299af7b26412ca79adc3615
    role: context
  - path: pages/traits/genomics/ds_34_system.html
    sha256: 26bab4f037d20546f700e862282223cf15f5d9d504acf061c136b5f9b7f20bc1
    role: context
  - path: pages/traits/genomics/ds_35_system.html
    sha256: 5338b8f98e6ce45c578ab5ac646371b0edcba633834927a2a3a976a8555ffb31
    role: context
  - path: pages/traits/genomics/ds_36_system.html
    sha256: 382968e03a44dc0cbd6cae5c30cc744659d7c685f2a29b2e4110256127326fc1
    role: context
  - path: pages/traits/genomics/ds_37_system.html
    sha256: 02b87b25278d0a8748bd36945ee9e4d9573e36f8fcc48383d4c9e103f112998d
    role: context
  - path: pages/traits/genomics/ds_38_system.html
    sha256: 3f68c5bfb032fe6994824ec00c64d4883d321d9fdb55bc59c46907330de20498
    role: context
  - path: pages/traits/genomics/ds_39_system.html
    sha256: 376cc9b82caf66e043b0fac0e5eace9e22d399d3ed21c227f3e2f51d69300595
    role: context
  - path: pages/traits/genomics/ds_3_system.html
    sha256: 0e3b755acf593723995d3adfab9a9590ceb589d54435a6bb5da97d112e8d2fdb
    role: context
  - path: pages/traits/genomics/ds_40_system.html
    sha256: a518df634c2b6ab8ce684b90b428a020334a65bc604a39c32a383543c25b7efc
    role: context
  - path: pages/traits/genomics/ds_41_system.html
    sha256: b36b518a27bd474fc916662fc031c67817c304fef892e24360e793f486f7b6a4
    role: context
  - path: pages/traits/genomics/ds_42_system.html
    sha256: 4a6167cacb61a49524b818a4f0d939004165dbcd1a5b5e198345b3c24d9be1a4
    role: context
  - path: pages/traits/genomics/ds_43_system.html
    sha256: d0f72e931a29e60398a635414e4e6d1d6348e5a37bc83c7ca2af920afca3cf90
    role: context
  - path: pages/traits/genomics/ds_44_system.html
    sha256: 53b3c2be44b9753c0d1dd908a685e0b78ebba1095f0910583ce44812b2ab24d6
    role: context
  - path: pages/traits/genomics/ds_45_system.html
    sha256: d2cd15b230608223aa0342417834abaa395cfac3bd362ee2bde93ecbcff18b57
    role: context
  - path: pages/traits/genomics/ds_46_system.html
    sha256: 93f6128677feba48b13ae8e46e17b63e3a2e8d0b5beced5df5db9e33e68fe32e
    role: context
  - path: pages/traits/genomics/ds_4_system.html
    sha256: 478c01d1561bef14dcfd3760d19cc16269d6be85e05a41108a97ea7fb3ae0f79
    role: context
  - path: pages/traits/genomics/ds_5_system.html
    sha256: 0925c6012f22a8d3b7032fe867455589ade5cbf1a49ea7065b9fd6db8c34bbc3
    role: context
  - path: pages/traits/genomics/ds_6_system.html
    sha256: cc30e04d9cafe28f64ede286373662d418d2fb6b33ec927fc67a651b3f792b57
    role: context
  - path: pages/traits/genomics/ds_7_system.html
    sha256: b393dfc1ed300f528f1c6ffda033571508403d43c86b8ad1cf0d4e89f51c8571
    role: context
  - path: pages/traits/genomics/ds_8_system.html
    sha256: 300757cc8c9158520506dc76a32b590ce3f36ae4ea53c1f8fa90c9a0ebb921cf
    role: context
  - path: pages/traits/genomics/ds_9_system.html
    sha256: b7e7eae7b21efd24f695947458b48e0fad442c1879f2acc069a6d0c431811e1e
    role: context
  - path: pages/traits/genomics/dsr_system.html
    sha256: c03ce15fca06d04945eee05ee22a8e6c89d4350f0cdb10c70ad75fee1cb875b5
    role: context
  - path: pages/traits/genomics/duf262_schlafen_system.html
    sha256: 57ea0dcd30b6e4dee05b7c41665c8080826309fabc4f49814a5e678f20eee264
    role: context
  - path: pages/traits/genomics/ecokmcra_system.html
    sha256: 9b541ad1f282e2b25aaf2648f5f490cdf82d7705e35a70f5ad4fd473dc197bee
    role: context
  - path: pages/traits/genomics/eleos_system.html
    sha256: dd6ee6f0aec80e432dfaa376be7c3a39e484b60c0a62ecb45ca7cae68cb67628
    role: context
  - path: pages/traits/genomics/endpacf1_system.html
    sha256: 6a990aa1657e8eb7ceba078e523709451292d1db08e7507490907052bb7218ca
    role: context
  - path: pages/traits/genomics/epona_system.html
    sha256: df69f6592743f8cc18f4382337ec0102fdf636083c4e3e64623734bb697181c2
    role: context
  - path: pages/traits/genomics/erebus_system.html
    sha256: ba2a1586aeaedc9ad13b65d8e1b699865ff08223179d9f4f0430719f47b3370f
    role: context
  - path: pages/traits/genomics/esos_system.html
    sha256: aa1048a162e116721a7c4d27a614fad1c23c56ab49d01fe933fd9aca9f3bb78e
    role: context
  - path: pages/traits/genomics/fliodhais_system.html
    sha256: fe1bc723afcfce51e08ba0f9a73dda7c84d659bec78e86fd05fb2bed1b37129b
    role: context
  - path: pages/traits/genomics/fs_giy_yig_system.html
    sha256: 2235d9fb1a61c3a0fa45764fe3d27ef9f64389b34f2c8f7b385ac2b9e35000e0
    role: context
  - path: pages/traits/genomics/fs_hepn_tm_system.html
    sha256: da174e8a83ce90bd18cd062f32d32779cb04fe87bf50ee6161c78feecf898c18
    role: context
  - path: pages/traits/genomics/fs_hp_sdh_sah_system.html
    sha256: e4efc4a91fe0166b024e3cf20165f71693b0149ccfdc418edb96a51f43fd6c56
    role: context
  - path: pages/traits/genomics/fs_hp_system.html
    sha256: d402e66c244ace19250373cf748cda1471a10efc87498ffe833eea3d0ab7a18d
    role: context
  - path: pages/traits/genomics/fs_hsdr_like_system.html
    sha256: 5ac2e549e13b7f00309f93072672483b37a757aa951aa6d48ac18fcedd5d742f
    role: context
  - path: pages/traits/genomics/fs_sma_system.html
    sha256: b34944679fc83113cd9a3e2061f5bf63d64678a394dc14e58db3e81a21df7cfa
    role: context
  - path: pages/traits/genomics/gabija_system.html
    sha256: 2db598537fb1a1577701175aa0171817b51ff6f13811c40b26e353230a978ff5
    role: context
  - path: pages/traits/genomics/gao_ape_system.html
    sha256: 633a62ea67f35a156c1bef704b8f72259efd481ab0bac812de1a3bfeeff28cf0
    role: context
  - path: pages/traits/genomics/gao_her_duf_system.html
    sha256: 785b6854d759324fdd4da91ca7649f33bab7c27d7b0569cccfd94cdb6d33d940
    role: context
  - path: pages/traits/genomics/gao_her_sir_system.html
    sha256: fb4ef4a61647bdaa98617a5a21545fcc775f6eba53a6dea7c20af48fd0161cda
    role: context
  - path: pages/traits/genomics/gao_her_system.html
    sha256: 36b327ec1d91a4a34ba3beafb693f30f09b863c9f13a9b911c2b134612d29226
    role: context
  - path: pages/traits/genomics/gao_hhe_system.html
    sha256: c2c2997acabf00b19aedf0d8e0c0d3d1a14ed6069acda654e6f0e668d266c506
    role: context
  - path: pages/traits/genomics/gao_iet_system.html
    sha256: 4edde5e72fd775a45f3e29592c60d9f3bd70d5c29847b39a56ae5a7c8075ddd7
    role: context
  - path: pages/traits/genomics/gao_mza_system.html
    sha256: 68b536d738ef983f3ab950c325a3b4cc00b5ceebf9cad4725d0bc826f4856530
    role: context
  - path: pages/traits/genomics/gao_ppl_system.html
    sha256: fcb9ae225f04e6ffe5ec1f972cbea60d40a335e667937c4774fe0911bee1f098
    role: context
  - path: pages/traits/genomics/gao_qat_system.html
    sha256: 546e2d62f6eee38df1c841347a8fa6ed83c501ec67f38990287b89e70db5788b
    role: context
  - path: pages/traits/genomics/gao_rl_system.html
    sha256: 663f45c83d84791ea103acc94acaf4ad3d5468e3f43b0f5dd6823b2cef4c01c1
    role: context
  - path: pages/traits/genomics/gao_tery_system.html
    sha256: 36b090f01c89df33fc5d0d82fd223dbc4d2574e4c0a0466eab7d47436a98c2e0
    role: context
  - path: pages/traits/genomics/gao_tmn_system.html
    sha256: 243505ea2e079f4ea17324cb54057d1745b695be48af8a39c65ef70827c2134e
    role: context
  - path: pages/traits/genomics/gao_upx_system.html
    sha256: fe4210a8efb1b9ecda957e5be9dff10da8877d0dd137d9a93806d285f5c19cf5
    role: context
  - path: pages/traits/genomics/gaps1_system.html
    sha256: 5d4eefd69a1de95d1dffc06aa9ffbf952e518ecb747f8fecc64ceac8a2f6a396
    role: context
  - path: pages/traits/genomics/gaps2_system.html
    sha256: 2402a86d31bd7a0d7818f1279c50e581c3b05ad94e947182c5e99ee46dd16648
    role: context
  - path: pages/traits/genomics/gaps4_system.html
    sha256: ffeaefaa171851e00773ce063c26cd660ab2c6575709112c77148fc98c119047
    role: context
  - path: pages/traits/genomics/gaps6_system.html
    sha256: 2865cf8ad8c0e29e607864f5cdced1eebc2092868ab7c339c740e93fc543c954
    role: context
  - path: pages/traits/genomics/gasdermin_system.html
    sha256: 404186e5af5e73b2bfa5e51854d3b9fbc3c707233813c2ca67c6bf3b6207d459
    role: context
  - path: pages/traits/genomics/gc_content.html
    sha256: 61107f325b811b62e36c4107d157eddab3ae4bb393728660a95f2fd4f78851f7
    role: context
  - path: pages/traits/genomics/gc_high.html
    sha256: 929ff16244f45623c60655cb20dce65c47c7b77826ddd4efb6ee6483dc4564cd
    role: context
  - path: pages/traits/genomics/gc_low.html
    sha256: b7371bb1b82fb409de7430d935b44a197ca2e973e0479b1e35fd820900476b4f
    role: context
  - path: pages/traits/genomics/gc_mid1.html
    sha256: 61968c6d32406bc88bbedd902bdb0ec63f99411a9783a2401278f6aca2286d9a
    role: context
  - path: pages/traits/genomics/gc_mid2.html
    sha256: 1b3f9c9a1b0f13460740b1ab00f8327b8a2f1e9e955dc9dfbea3d6725a23a05d
    role: context
  - path: pages/traits/genomics/gc_skew.html
    sha256: a825aa689b63a4105b1dd6b9409107ca4fe2c4c0c07c83c3eb703cd28261e6a6
    role: context
  - path: pages/traits/genomics/geb_system.html
    sha256: 8b3d5d5b9ac6e8ac6bacdd34391a4a4cac186fe220da37d2a2f9438c5ed5469c
    role: context
  - path: pages/traits/genomics/genome_size.html
    sha256: 57e3df6cfc8e5b0ef4e85345ef7dc951137e87604b10b09a14639a8df67d157f
    role: context
  - path: pages/traits/genomics/genome_streamlining.html
    sha256: fd2415f0dfe9e48c903dfc25b65cf6f3d20687da94db18f40f2460409f1a391e
    role: context
  - path: pages/traits/genomics/genomic_island.html
    sha256: d586e21e326f5c81a5f1e23cfb5b3fdc62b9158bacb701b2ff68dff76719c92a
    role: context
  - path: pages/traits/genomics/gmrsd_system.html
    sha256: 576541578d68d104417dcdb157b317be03a0a22ed49fddd9f906dd109ce34e65
    role: context
  - path: pages/traits/genomics/hachiman_system.html
    sha256: 4dab6e98f5318ae4c9b5cb158d7a7814584ebadf5ecd59f20b6f10689be9c4f7
    role: context
  - path: pages/traits/genomics/hachiman_type_i_system.html
    sha256: f498cf77a53b899dd8638cc4651ceffcf237f68132e733a0e08faa415b2424df
    role: context
  - path: pages/traits/genomics/hachiman_type_ii_system.html
    sha256: cc10b28e362f357aaaf644590cded8174e82f0492a81772a6400dbb8e779ed04
    role: context
  - path: pages/traits/genomics/hailong_system.html
    sha256: 82a1e200f2236e912d68822774772c07a405b5dced73d1a0ba07423f4b9ef0f2
    role: context
  - path: pages/traits/genomics/hec_02_system.html
    sha256: 6a0bd07ff9fd53465e3c99e8019123e39dec37c9202fb611efb005fc4411330b
    role: context
  - path: pages/traits/genomics/hec_03_system.html
    sha256: 049efc88692db5b5ec1398c45b6f125931ba8ae7d7f48786e532ffc983982952
    role: context
  - path: pages/traits/genomics/hec_04_system.html
    sha256: 848e6c16b7e2ab267cb2237f0a2ad0e0f4b0bb157c4f6df6f0f62483eb8d4cf0
    role: context
  - path: pages/traits/genomics/hec_05_system.html
    sha256: 061ecd2b907e5071db9001c631b12c7025fb17d80c2fa807624a7611c8f77aad
    role: context
  - path: pages/traits/genomics/hec_06_system.html
    sha256: 40ff6a354d6a9fdce8e21ff532daa4ff95fbfcbcf1b6b46902a440cb5ce0188c
    role: context
  - path: pages/traits/genomics/hec_07_system.html
    sha256: 06aa71de19bd37e16ac04a45e3a9fa6dac9bd7c13906c43d770baacba5765c38
    role: context
  - path: pages/traits/genomics/hec_08_system.html
    sha256: 1f69a07acdfda7cd454c5f3f6594e5b86e8c15c2884f9e93edc83ae178b4b11a
    role: context
  - path: pages/traits/genomics/hesat_system.html
    sha256: 88104a2253dadb1c25a69ecdbced4838096714f5d136a2e414ff00f06b95a78d
    role: context
  - path: pages/traits/genomics/heterokaryosis.html
    sha256: dd840741bafa8e107ce3df5aaee1006ef1ae3f685cc14483615945bf0fb9975c
    role: context
  - path: pages/traits/genomics/hma_system.html
    sha256: 9eb35cb7b392b1cd5eee038e7bddb1a0d9d2dd1dab3cc8c36e9cc03d9810698c
    role: context
  - path: pages/traits/genomics/hna_system.html
    sha256: 1a420d329165e75ac3f6f3c94ae9e8f2c2e8b6690987fb2b00da20b9941db3a5
    role: context
  - path: pages/traits/genomics/hypnos_system.html
    sha256: c22189935eecf3c5e2c3380ef197efdcb61aee124e80c652f8aa5a693317172b
    role: context
  - path: pages/traits/genomics/ig_like_schlafen_system.html
    sha256: 9566c19d086cca87e27134939b1ee95faed6185752cbbd1ef4cecd68c7221ba0
    role: context
  - path: pages/traits/genomics/integrative_conjugative_element.html
    sha256: 645b6b2484859a0219aca26f7d6fdadec1a984944418070dfff9021fb3edd03e
    role: context
  - path: pages/traits/genomics/jukab_system.html
    sha256: 42c08c67c37f3ca71f00ef8b9fc62f654ba42b951473f688cce5a2201d469884
    role: context
  - path: pages/traits/genomics/kamadhenu_system.html
    sha256: c8b63b886afcf0c3702218732a19c91da2825fb12b2ff758e8a6964d77fe0a78
    role: context
  - path: pages/traits/genomics/kiwa_system.html
    sha256: 8f4e9ba558ad37c14c05e7d144091d3a047673e09ecbb06121d9f8dae264ef32
    role: context
  - path: pages/traits/genomics/kongming_system.html
    sha256: b7ea6f989949b204a0d3fb909bf14d930937ed5c3156e1e667a03b54188f1578
    role: context
  - path: pages/traits/genomics/lamassu_amidase_system.html
    sha256: cc65d8ef2175b03dc85f5dea667c843d9b96f252d30e53eb7238ebb5d9eb336c
    role: context
  - path: pages/traits/genomics/lamassu_cap4_nuclease_system.html
    sha256: f46987d9c2dbddfc286c6ed438f7f90a4fe8c948c7a8582731619ca009624474
    role: context
  - path: pages/traits/genomics/lamassu_fmo_system.html
    sha256: e7dad56b7f268096fc8b4ddadf36bb0dc7805fb722a8cd36b8df37cfd6e346e9
    role: context
  - path: pages/traits/genomics/lamassu_hnh_system.html
    sha256: d1c8fe0d4fc8195504370fa8fd4e3ab096b1f5b491d8017c839e952301f31653
    role: context
  - path: pages/traits/genomics/lamassu_hydrolase_protease_system.html
    sha256: 8e3a76dae07edb2b02857deba3c78e29e2dc18aacb18220e64d0df2d4afeceeb
    role: context
  - path: pages/traits/genomics/lamassu_hydrolase_system.html
    sha256: e35a5c8a61cdeadd2ffffa4ed40bdfce89ca1542844e97728cd256f6dc9233eb
    role: context
  - path: pages/traits/genomics/lamassu_lipase_system.html
    sha256: 4d299799118fd740f47d22294637e932aa023f616dc56f75d3a3f0b277e57bf9
    role: context
  - path: pages/traits/genomics/lamassu_mrr_system.html
    sha256: 01f1eb4111aeee6c65ae233c6bbff8b7a52b75b0ed49b4ac546de74b290970ef
    role: context
  - path: pages/traits/genomics/lamassu_pddexk_system.html
    sha256: 674991331480a1040f29304ae3d3c866c5ce8dd5755572d45163522de63c0d11
    role: context
  - path: pages/traits/genomics/lamassu_protease_system.html
    sha256: 73f57f33a3aa2f88340ce357dcf9532dcc95b42dc771518388909ca3e0f562be
    role: context
  - path: pages/traits/genomics/lamassu_sir2_system.html
    sha256: 11d99692d5b5ee0703f56690c031a8d08c63ebb0c321ccd53178de2175907aa6
    role: context
  - path: pages/traits/genomics/lamassu_smek_system.html
    sha256: a498810a3d67ef5a3656e476ba3836bfb4230774696c6bc20591f082eb4d97d4
    role: context
  - path: pages/traits/genomics/lamassu_system.html
    sha256: b1f98476e5d51ec5dc73c2d83c29971eec3410dfaadaad380aaa55181b9f282d
    role: context
  - path: pages/traits/genomics/lamassu_type_i_system.html
    sha256: d02e7611e20da26d2a9464989827c608a78b61311c4d4f999e886ff6df9fd275
    role: context
  - path: pages/traits/genomics/lamassu_type_ii_system.html
    sha256: 7b2c1f1738ad0c8e11abc800d77af2fc0bd517d3bbc392bdcdea5c732579d784
    role: context
  - path: pages/traits/genomics/lanthivirin_system.html
    sha256: 64ecc6f0406f020f2fc455af92bd717ee2ddd782f48bad095b3b233786a7895b
    role: context
  - path: pages/traits/genomics/lit_system.html
    sha256: 519e94e78930e2a66638a3f7e18e6e17d3772ec3547bdee5bd301140985737cf
    role: context
  - path: pages/traits/genomics/long_lamassu_system.html
    sha256: 95bc74d2f422924967529f9243dd686ae026eb4145ec1d4e67ad6a3f7d7fc048
    role: context
  - path: pages/traits/genomics/lugos_system.html
    sha256: 26eb909df31c0319a54ff641f424d61bcb9787f6d346ecdecf2ba35e8bdd16f5
    role: context
  - path: pages/traits/genomics/mads_system.html
    sha256: e0ed10c47f5b49a30ef8ed0f24517c1b90c8fbf17f1c28c1f4690176774c6d3c
    role: context
  - path: pages/traits/genomics/mazef_system.html
    sha256: 42246c8c6242aad50f42731915e6eddeaf5a48e9c0127b5bb2b33120b4c1463d
    role: context
  - path: pages/traits/genomics/mcrbc_system.html
    sha256: 3b8b667900eccc26614aa6f52d53994ec5d3e927d222d78ec5122eef56fcf53b
    role: context
  - path: pages/traits/genomics/menshen_system.html
    sha256: 32a8a3b93ecfb7633879d2aa6fecd246543bacf07c30d7a5c329ce4be6a68dad
    role: context
  - path: pages/traits/genomics/metis_system.html
    sha256: 55900956160ddbe61ae37c7d707e6b8affdf0173b4aadaa5e4b3e40137654bf6
    role: context
  - path: pages/traits/genomics/mksbefg_system.html
    sha256: 313d0f5e4d8d842aa6d232eb6d85da7d7f46368684e19ce9c149737244362434
    role: context
  - path: pages/traits/genomics/mmb_gp29_gp30_system.html
    sha256: 6f923d167f7a08e1552da204e3a49cc53a71bac7395e0c6b3d44224a19459bf3
    role: context
  - path: pages/traits/genomics/mobile_genetic_element.html
    sha256: 647494725cefb6db4ef6da8235c82dfbb7bee9506bb6019834068d175432baac
    role: context
  - path: pages/traits/genomics/mok_hok_sok_system.html
    sha256: 9dff401d8535f464567d1a22cabae29278f011d1184af2788d30d10063f05093
    role: context
  - path: pages/traits/genomics/mokosh_system.html
    sha256: c4dfbcfdb87be5c820d5a034c633794057bc3d705d77ae6e13588283f4b9f130
    role: context
  - path: pages/traits/genomics/mqsrac_system.html
    sha256: 1207364fc6a28c318530b56187dc97b734a238e7141175f1721f83766f24877a
    role: context
  - path: pages/traits/genomics/mspji_system.html
    sha256: 835f482495e05b1d4a2bd391ed7f86254283b73bcb2ac7bd80e7d5a26cd3e07e
    role: context
  - path: pages/traits/genomics/nantosuelta_system.html
    sha256: 94415e0852f2a399ee3e9972c07424b87b65924f3eaa8fb1b08b02249bc277a5
    role: context
  - path: pages/traits/genomics/nemetona_system.html
    sha256: 2dfd1c793fb0798992e7de16e117b2908850f65132ce6a2d673fa50ebf6637ed
    role: context
  - path: pages/traits/genomics/nhi_system.html
    sha256: 83bceaba6b6a9d3bbdcd9376d473b23021cc1b0ca56c2eb40b96cd5565fc5aa3
    role: context
  - path: pages/traits/genomics/nixi_system.html
    sha256: e55096b9df3ba7d879820f035a1c7d78f4dc0fdb4e91ec6ef34aa0215eb719ff
    role: context
  - path: pages/traits/genomics/nlr_like_bnacht_system.html
    sha256: a63792c0e2ca2f9fda4dd6762ae6452b181f8d99d43e91da8c2fdcee6d6e81ed
    role: context
  - path: pages/traits/genomics/ogmios_system.html
    sha256: dc16f82c27f3f72a000cc2671e0f247b100b77c7ee60bba3d35341f51c5650d5
    role: context
  - path: pages/traits/genomics/old_exonuclease_system.html
    sha256: 2c22741a18e7ce7fbcbe9b06bb0d1e75b609190230cc0d07410ae0fc4465b109
    role: context
  - path: pages/traits/genomics/olokun_system.html
    sha256: 9630cde971b6ed29f33f4bf3ae21548c96f77e3b88e35e0934a835d1cc8ea706
    role: context
  - path: pages/traits/genomics/ophion_system.html
    sha256: 7bc1421f45de6c16f7ebd8acf26adef5308655da85dc54ddfce5645601e53b03
    role: context
  - path: pages/traits/genomics/oshun_system.html
    sha256: 22b250f1e689f12dee0bca684ad5ffc9f8e01ccbb2fefd4e10922b14e2be88bd
    role: context
  - path: pages/traits/genomics/pago_system.html
    sha256: 56d713e4cbabb2c48342e46d53030070815c6d3ca60774c0a35b87605a56bfa0
    role: context
  - path: pages/traits/genomics/panchino_gp28_system.html
    sha256: 026f509b8014a3ebf3abde51d9b595a74d12dae47135bb2546b8ec73bebde2fe
    role: context
  - path: pages/traits/genomics/pangenome_openness.html
    sha256: 2c797f791d8df4aed0bae0e2076264664a07f3b613cb5e784d84cfa6e92890db
    role: context
  - path: pages/traits/genomics/panoptes_system.html
    sha256: 0873042156e18a81ba8623bc694aa7afd4cabd4937c4aa192fff28871f869d69
    role: context
  - path: pages/traits/genomics/paris_system.html
    sha256: 790b7ea358e3322784e8ed2f721739e29aeece537bdfe14f126f4cbd67ce0281
    role: context
  - path: pages/traits/genomics/pd_lambda_1_system.html
    sha256: b710e1d8c696d491d854642b4dcb68c6208fd2fca41e3c989fff394dcf1a3101
    role: context
  - path: pages/traits/genomics/pd_lambda_2_system.html
    sha256: 1dd71e96465bd97936f5f9ac65b3c38c0f42310582d6708b45d89a9e413a1ac6
    role: context
  - path: pages/traits/genomics/pd_lambda_3_system.html
    sha256: f1e0ddd42770e07b14a09517777431f1b5419afe4b97e79fd13988a32e9e6290
    role: context
  - path: pages/traits/genomics/pd_lambda_4_system.html
    sha256: a795b6c2beef2f4ea77726b3be0321268bcdb5ad830d5151089720fc165a0a85
    role: context
  - path: pages/traits/genomics/pd_lambda_5_system.html
    sha256: f2faa7880d360010b45fcdca0a70fa22af3c4b7a9db245f4b3cd83098d42d815
    role: context
  - path: pages/traits/genomics/pd_lambda_6_system.html
    sha256: c6a91206106badd4a0057c5cfdcdec0d9a833cbe5dd02934b92695245cecd137
    role: context
  - path: pages/traits/genomics/pd_t2_1_system.html
    sha256: f47ee439b26a94b39514257ff1b04de1072d8db47f6a0ee541a19269764785c0
    role: context
  - path: pages/traits/genomics/pd_t4_10_system.html
    sha256: b705518d2ebc7ae21fef52d6795c88f1f19cfc664f9306aa3c9cc571460845eb
    role: context
  - path: pages/traits/genomics/pd_t4_1_system.html
    sha256: 8cbfda87ea2eda160a45e8ffbaec1e28892f4693d4918ee4527f607cd83bd0ec
    role: context
  - path: pages/traits/genomics/pd_t4_2_system.html
    sha256: e72058a47614dfc06b092b12e8f92c319fc894fca69bcdb5c7fc1acc39728ab3
    role: context
  - path: pages/traits/genomics/pd_t4_3_system.html
    sha256: 545a58e947b4e3b963ccf815ce6577f71700250607386bb60d4b6b2063ab0b1d
    role: context
  - path: pages/traits/genomics/pd_t4_4_system.html
    sha256: 429c094ea308cef318bca409aba00eb4534ae58c1e3112668384bb1aa40c8aa4
    role: context
  - path: pages/traits/genomics/pd_t4_5_system.html
    sha256: bc4da4541691ad0324a9d5946a2f70bc2f06a27e7a37e04247cbeed042a2dc5b
    role: context
  - path: pages/traits/genomics/pd_t4_6_system.html
    sha256: 5d0f2497f81cf8ec590cc372789a071e706151f7065bdf6a60b65d087e4fea53
    role: context
  - path: pages/traits/genomics/pd_t4_7_system.html
    sha256: 3f7cd9bdf7d845a201115a979a519ddf674165df1286c9277c6dab8fb7e7e734
    role: context
  - path: pages/traits/genomics/pd_t4_8_system.html
    sha256: d94ac5db00d5c054f26c31495cd0162db682e4c68e3ab07880ea0c5b29b32b86
    role: context
  - path: pages/traits/genomics/pd_t7_1_system.html
    sha256: a74f754571cef26816ed0d5eaa5ac537fae16526c59190786386bc7f9dab58dd
    role: context
  - path: pages/traits/genomics/pd_t7_2_system.html
    sha256: 2015b577fbadceb48487e5c4697b6f61f8aece47556f249c597a6f810dee8a30
    role: context
  - path: pages/traits/genomics/pd_t7_3_system.html
    sha256: 9a12950373842b98411d662655313fda56062f30da04695ac3a2e9938c4eb71c
    role: context
  - path: pages/traits/genomics/pd_t7_4_system.html
    sha256: 1920d464e75e2955336905b73f2a7b068bbbfcb8f0a8effa9ae355a642d153b4
    role: context
  - path: pages/traits/genomics/pd_t7_5_system.html
    sha256: 225405c51a8beeba1604301afc26430aa4ec3aa3144130c31bb8a924e68b2bda
    role: context
  - path: pages/traits/genomics/pfiat_system.html
    sha256: 767265028873d009f84529f4e4b5321f5deaf5b8fca7361488425dd6242e63fd
    role: context
  - path: pages/traits/genomics/phage_defense_system.html
    sha256: 10a09d2ca32d39022a9c83e05b1cea1e61c1b085d1d47e2cd6f08ed46d9e4e4b
    role: context
  - path: pages/traits/genomics/phosphorothioate_defense_system.html
    sha256: c203c033f1bb4ee3275feb6f7f02ebf1a9378b271f1f3bc392215e7a2ef21b85
    role: context
  - path: pages/traits/genomics/phrann_gp29_gp30_system.html
    sha256: d48b4c3ea6c087f890cf15d1f1846ea9cbee7999a96e4b5d825abfeca7170397
    role: context
  - path: pages/traits/genomics/pif_system.html
    sha256: d5a019907055ed608071a3f73915da06c0ad5954903542eb5a58f164b67822b9
    role: context
  - path: pages/traits/genomics/plasmid_carriage.html
    sha256: f7da050e3438d62bd0161fbde52aa333607d6d20b6e14f74e9387f48836b3d82
    role: context
  - path: pages/traits/genomics/ploidy.html
    sha256: 3ef4f18d99077fc01f4286c39fb330f1814a3cd2d54f0eb2bbf8b76ae84b6f94
    role: context
  - path: pages/traits/genomics/prithvi_system.html
    sha256: a4e9dc4c28768cc52d387778bc30b2ee49ed5ef3da59c293aa0a910c014da822
    role: context
  - path: pages/traits/genomics/prometheus_system.html
    sha256: 0dab93bf330138a889df6526942975a8f4e4f7b5b27b37cddd0ee3db82298884
    role: context
  - path: pages/traits/genomics/prophage.html
    sha256: a0073280ee48e9d755473f0aa1e5845e08c955ae613a45e9676e97f622c1afad
    role: context
  - path: pages/traits/genomics/prrc_system.html
    sha256: c87c4c1901a6e75e06fdab17953e105dee139de2fc49ababcdb7e7ff8639f211
    role: context
  - path: pages/traits/genomics/psyrta_system.html
    sha256: 102f4f215ec949f4b91bc8b651b08d6a6cfa2bf5f58e3ea0433835c47202c668
    role: context
  - path: pages/traits/genomics/pvurts1i_system.html
    sha256: 6cf7c32972bf7e190be49116d34dd053618a16bfcc16adb69d73b2257ccee4ab
    role: context
  - path: pages/traits/genomics/pycsar_system.html
    sha256: a176cf1f0348bf9195eb9e2a979ff7ebced72f0858bdce880e52f7246f836757
    role: context
  - path: pages/traits/genomics/radar_system.html
    sha256: 67468644ea66136ddda29fc96c2847932c788051491fd7e7f9afbc1dd7f93f96
    role: context
  - path: pages/traits/genomics/razr_system.html
    sha256: e3f99b1d74875084cb7098a7d38ba684f9eb13bb8fa1b8957443d4da207ab1c7
    role: context
  - path: pages/traits/genomics/resolvase_duf5677_system.html
    sha256: db996b74ec2892df6f8266ba62c8c5041c2e79877926fd68a6ad5e3022cd5115
    role: context
  - path: pages/traits/genomics/resolvase_kap_ntpase_system.html
    sha256: 0e53b3797e2ca3fe729556c7d55f748d7196f6bf066d858b3bc87d0932d21968
    role: context
  - path: pages/traits/genomics/resolvase_schlafen_system.html
    sha256: d752805fcbc552f0a85efa06855a1d3602e6abf6b7e6136d1524ca53804c5d57
    role: context
  - path: pages/traits/genomics/restriction_modification_system.html
    sha256: 29c4fa3f2938ffcae7c5d9af20a903206bc13a6e51c155873d3a501153a38219
    role: context
  - path: pages/traits/genomics/retron_system.html
    sha256: 623f36c691bd3d1ac4390f814846b7c14957972ee74601febb253281aea1356b
    role: context
  - path: pages/traits/genomics/reve_system.html
    sha256: 7f3ddd71df5d25d4a2d6d403924ba96acb1cb6593f0110c31750fec7fcea2a84
    role: context
  - path: pages/traits/genomics/rexab_system.html
    sha256: 1b33a06a449cc14b9c63075ca9c6d1e1b92ba570927445371a35ece7f2fb05c0
    role: context
  - path: pages/traits/genomics/rhea_system.html
    sha256: 112572885d83d316b92cc62a148c465dea45c0b8304104b1fdc69a56b0c05334
    role: context
  - path: pages/traits/genomics/rloc_system.html
    sha256: 3c2da19b5658765ce114cbeac0bcb79e143f9ee9e5d4f9b129cee28d0d44497b
    role: context
  - path: pages/traits/genomics/rnlab_system.html
    sha256: 3d574c82a2f11565c021f3ec7c93eab77b0cc333fdbd94b6f2084d3d20a1c532
    role: context
  - path: pages/traits/genomics/rosmerta_system.html
    sha256: c2bd955a671f095214fe6881e59484860710b632f2a8077f8b146f3be892271d
    role: context
  - path: pages/traits/genomics/rrna_operon_copy_number.html
    sha256: b72d58212a83dbb21b2bad2b86fa1020e0d9e1acae7ada1a3fcf456de3711e08
    role: context
  - path: pages/traits/genomics/rst_2tm_1tm_tir_system.html
    sha256: 87405ed81b2a9dd3aa8e43515804291a3e0897aaaba45039f6e8be473d64b210
    role: context
  - path: pages/traits/genomics/rst_3hp_system.html
    sha256: d07c05558d5fc21e52aac17faed1d03ad6e85d60b5add415aebb1e2e60acafa6
    role: context
  - path: pages/traits/genomics/rst_duf4238_system.html
    sha256: 9f405cb3fa23ba16d31e06215ed087aa63f3651ad9b4b67400b9ebd2c39f06a0
    role: context
  - path: pages/traits/genomics/rst_gop_beta_cll_system.html
    sha256: ca3e5abc2a5fe80328389d96a10db522c68576831b995a1098ccb0e520dcfbea
    role: context
  - path: pages/traits/genomics/rst_helicaseduf2290_system.html
    sha256: 05558ef02bfe964b7438eac8b2bff50b3bd4a0bc6e1a38de22411827ceaa9c08
    role: context
  - path: pages/traits/genomics/rst_hydrolase_3tm_system.html
    sha256: 1f2f45679f9a8de8c049b2a854b4f53806248d7119826323cc552cfe7ecc2527
    role: context
  - path: pages/traits/genomics/rst_rt_nitrilase_tm_system.html
    sha256: dc3c0c6f188e21daf2ed546ffa7448d5dcdc33cd3fc96b6577d0c29eb263ff97
    role: context
  - path: pages/traits/genomics/rst_tir_nlr_system.html
    sha256: 852ae994d1d36f808d5cbce8df0b80fbf3ae29d3a246e3e57ecd8eda38edc419
    role: context
  - path: pages/traits/genomics/rugutis_system.html
    sha256: b37fc2f63418a4e653fc78f6dc50dbe07c4649900aa33916a0293b385b27857e
    role: context
  - path: pages/traits/genomics/sanata_system.html
    sha256: dbe3d996ea40f0e1c308d4e65cb1ac16b37036affc1c547665d211a1c2461223
    role: context
  - path: pages/traits/genomics/scomcra_system.html
    sha256: dfb127299556d04464f07a31c9b4c1dcf967e7e96fb873f537afd72a7b72a30e
    role: context
  - path: pages/traits/genomics/sdic1_system.html
    sha256: 2c01be4e4c97b760caca3233ef1383226b7d3bef60be197d093a4b3a4e3e7509
    role: context
  - path: pages/traits/genomics/sdic3_system.html
    sha256: b38eec00b49b1aba6309e2cc52046c17ba23dc7b88adaf6419e00b5de36b4c82
    role: context
  - path: pages/traits/genomics/sdic4_system.html
    sha256: 0461843ea986efb83326fbc38896a02be1a3f8af95390ce09e1794757861d915
    role: context
  - path: pages/traits/genomics/sefir_system.html
    sha256: 2d333948aa111e5e8996c0f51d79078c919eede8d11726ea8d33ff6a6dc84437
    role: context
  - path: pages/traits/genomics/septu_system.html
    sha256: 8ce3e84b01ec504105ccf033c81e01ead440223e56d018940b7d5810696f4e2f
    role: context
  - path: pages/traits/genomics/shango_system.html
    sha256: 56b08527766301fd3b69457037fc9583be62ba883d822aebfa58c3c4c22f3f84
    role: context
  - path: pages/traits/genomics/shedu_system.html
    sha256: 24bf7fc5dbc383215621582a2340d38fa3d18a60118d3686eafdac83fdb6e9d5
    role: context
  - path: pages/traits/genomics/short_lamassu_system.html
    sha256: 7c73c3df32ecfb10106a2e4fc5d1ab1ee22677b0339f2e9e8c91f6e003e409d3
    role: context
  - path: pages/traits/genomics/shosta_system.html
    sha256: 0af34f7b45169502dce8ffa570ed5a094789f3db9b2521d7d2911411086013a8
    role: context
  - path: pages/traits/genomics/sirona_system.html
    sha256: 53a4acfbdc02ac03ee5652d37a18b00b7ad035954e8115d12cb1fc2893b9f582
    role: context
  - path: pages/traits/genomics/six_a_mbl_system.html
    sha256: ca38516e922852dc8f312fe184ceff6d244f09bd7a20010402133727f25c4b8b
    role: context
  - path: pages/traits/genomics/snipe_system.html
    sha256: 8fdfdef3b150252f149f923a0a3cf49a9ddc3ca79b2f5b2eb9edb955db353588
    role: context
  - path: pages/traits/genomics/sofic_system.html
    sha256: 566c7eb7c48572ae25579e89ac9f3a0d6bc9ed2a6eb8c08781212026d3eccef1
    role: context
  - path: pages/traits/genomics/sparta_system.html
    sha256: eec83a512328e839bad6a36414cf077baa2414f8c4bb6c047c0b2bb527e29b06
    role: context
  - path: pages/traits/genomics/spbk_system.html
    sha256: 0ad0b949e7b7da3f75bd0a0c3219bf2df868bee37882cd2438d1deff7716e745
    role: context
  - path: pages/traits/genomics/sspabcd_sspe_system.html
    sha256: f600735a9d3d256b1e975bc4337c854d67191a66f3c9250302af03fe8cb2f3ea
    role: context
  - path: pages/traits/genomics/sspabcd_sspfgh_system.html
    sha256: 12f7863e240ff9c89a08c7c1d12bedd06ef7f31edfe5cd848afe998a44b09640
    role: context
  - path: pages/traits/genomics/stk2_system.html
    sha256: 8395cefe84c0721a637b0193a010d7504618d359722a64d4e71c0a012b170736
    role: context
  - path: pages/traits/genomics/sucellos_system.html
    sha256: 65a50890572a39f16974fad465cda7a4412cb731cb57acdefa4c919c440efa74
    role: context
  - path: pages/traits/genomics/tab_system.html
    sha256: af8b0d3604c89f6dca9ab9ba3e9ad852c4a21b49b59cb4ea59ba1d2a4930fe82
    role: context
  - path: pages/traits/genomics/tagi_system.html
    sha256: 393692b2f84d5d06d3c3eb8982efb2b7faf375d7cbcdf21aa4c8a01c2fd2d574
    role: context
  - path: pages/traits/genomics/taranis_system.html
    sha256: d99cb58b4d6e3bd2c6dcdddf406acab16b62bd115e2a5e771874ae650afe2d6f
    role: context
  - path: pages/traits/genomics/tgvab_system.html
    sha256: 4ae791a5fb08f49163756287f9a2b313c71f5cc2cb533686deae8bee87c52df5
    role: context
  - path: pages/traits/genomics/tha_system.html
    sha256: fafd89ae01614b441ae527dba62ac634d146da0438f3cc31146acb01fb96e425
    role: context
  - path: pages/traits/genomics/thoeris_system.html
    sha256: c0833470350ec103f0c1897f53fd402ba3cc41c702fe1848f0a69198a2a9788b
    role: context
  - path: pages/traits/genomics/tiamat_system.html
    sha256: 87622349f8298973d8d120fcc6ee6ecff4240831a7a1c751547551f29d294027
    role: context
  - path: pages/traits/genomics/tir_i_system.html
    sha256: cfe3506431cdddc151bded73e0737dca2e87fc725729ec198f81eff222a99560
    role: context
  - path: pages/traits/genomics/tir_iii_system.html
    sha256: 0511ce627dd8aa071c3a5dc3ac3c7683f6134f5a69ee346c7b9e19a039da6208
    role: context
  - path: pages/traits/genomics/tir_iv_system.html
    sha256: 218e94dd935448416a028ed7026c686b32350f3d6c77f10c5384a03ca6b943a9
    role: context
  - path: pages/traits/genomics/tir_vii_system.html
    sha256: 4417b9cf54e41658425520cee5bf85727ea346b235cd25f859280dfce2e4aac8
    role: context
  - path: pages/traits/genomics/tir_viii_system.html
    sha256: 5df81fbb75cdc54c5324b3cfd826aeee536a7900b977026c78c154a089106325
    role: context
  - path: pages/traits/genomics/toga_system.html
    sha256: 7526a4240216b93f124c0fc632f0ba31055c9b37262a324ede7bbffe434d6622
    role: context
  - path: pages/traits/genomics/toutatis_system.html
    sha256: c28f0acff128e2b480f0a8859c49d42d8ea36b46c09f20111d1bc9976fe46d7c
    role: context
  - path: pages/traits/genomics/toxin_system.html
    sha256: ca559e0b8fec8cb1e66762985451c777712d36d5b7480887687fe1eb6e00ca3d
    role: context
  - path: pages/traits/genomics/transposable_element.html
    sha256: f0549a357534820c01f381012736c10b6f72153c2dd8075d1c2748bdeff97b4a
    role: context
  - path: pages/traits/genomics/type_i_restriction_modification_system.html
    sha256: 98f7055c90a4d14ad26f888b2d23541c4b3c09069b9a14d267707c974725068b
    role: context
  - path: pages/traits/genomics/type_ii_restriction_modification_system.html
    sha256: 921ab34d7c8100a00524f9dcfc4e3dfb38723aba94b3bf85f0674d0456c60c58
    role: context
  - path: pages/traits/genomics/type_iig_restriction_modification_system.html
    sha256: 63b71dbab5be4c3ba9365089547f1eb229642794e99d73705a3a0d1a82e27d42
    role: context
  - path: pages/traits/genomics/type_iii_restriction_modification_system.html
    sha256: ab512dbb48e33d55d146837397c8db08ae3a2261ae6630ef28280bfe0b1b3f4a
    role: context
  - path: pages/traits/genomics/type_iv_modification_dependent_restriction_system.html
    sha256: c78adf5008f6a28df18b80799c89c4251b6422e64fe941cfbebca315b23b9dbd
    role: context
  - path: pages/traits/genomics/ukko_system.html
    sha256: 04736c50fb4e4acc8ec76465b333890fd056e49fdc058d839ec3d6d2daa08232
    role: context
  - path: pages/traits/genomics/uzume_system.html
    sha256: ea213e2296fea0ec1fcb43dd3c5dda59841a6dc36fb9fde3170ccf817c6c70b5
    role: context
  - path: pages/traits/genomics/vcam4i_system.html
    sha256: 00ea4c729e6016175a91e213a89c32b70fc41251165d01a9335d19cc686b2e92
    role: context
  - path: pages/traits/genomics/veles_system.html
    sha256: 9947ad21113ba9f8c0c332202027b87fd1fb5d5df75df4c4c71d5ed362d24b80
    role: context
  - path: pages/traits/genomics/viperin_system.html
    sha256: 60781a2afff14745100f31450aa76eac12e3b88d3c682d7a07f4cd905bed25a8
    role: context
  - path: pages/traits/genomics/vp1796_system.html
    sha256: 3ee2f3129abf653ba092a2f150498b344c6cc639c6eb795a6491cea6d5c04249
    role: context
  - path: pages/traits/genomics/vp1817_system.html
    sha256: 276d19e85e105594257a2bdf08311b882e5109f1761e2dd6290d8d811211d9fa
    role: context
  - path: pages/traits/genomics/vp1823_system.html
    sha256: 6c61f54d054f867084cfcf9c55bda912207ead2fb862c7531adbf7af528b6761
    role: context
  - path: pages/traits/genomics/vp1826_system.html
    sha256: d6fb977370fba211898dafd98307ddb3d56b9982456fdefa0c402ddaeedda643
    role: context
  - path: pages/traits/genomics/vp1839_system.html
    sha256: 263a49d8589b30e4f798d8b003fe2269445ece12c9bb8f4ae9b35942d74d9959
    role: context
  - path: pages/traits/genomics/vp1840_system.html
    sha256: 3434510328724fc86d12b9eab4fe65a35a8db416950fb4585ee8d993d0996027
    role: context
  - path: pages/traits/genomics/vp1848_system.html
    sha256: 1bada2ddb00c69439fcaab68b8ac2534e3b454a7b2d025680c0078318020d837
    role: context
  - path: pages/traits/genomics/vp1851_system.html
    sha256: 360dbc63210d984ffd70d1f68c1ce00d6a358da5d66edab68ce5f5f693b16eda
    role: context
  - path: pages/traits/genomics/vp1853_system.html
    sha256: af10db7278f864c439cfa84ff56c88bde97a8f65f4b8e4737ad1782ffb865199
    role: context
  - path: pages/traits/genomics/wadjet_system.html
    sha256: b92697fda72a98341adfa9f30798d3a98506f99c837cc03c6ada4e7502c60f1c
    role: context
  - path: pages/traits/genomics/zorya_system.html
    sha256: 795ed7a5cc6af44e128848d3567ffcf8386c5a4a5fcc95346c21b894f324c1bc
    role: context
  - path: pages/traits/genomics/zorya_type_i_system.html
    sha256: 5a282811b6ddbf0dddb3c88f22266ddeb803fe7e288b6a75518ca8d94e1faa59
    role: context
  - path: pages/traits/genomics/zorya_type_ii_system.html
    sha256: 48fbd027e941a94e3e30337f1f57bd40256aad2e3db4be5991c7643902854650
    role: context
  - path: pages/traits/genomics/zorya_type_iii_system.html
    sha256: 3974e98a8ab7e8f370c25e875b4ccb3fd40966027164ead3e7a86c0e6f496cb2
    role: context
  - path: pages/traits/metabolism/accumulates.html
    sha256: f80710360144dc49c43050e6324b59acb4cfd02ddfad3e43f7d9a599bc2a3446
    role: context
  - path: pages/traits/metabolism/acetoclastic_methanogenesis.html
    sha256: 5ffc816827f71bdb27beabfefba1ead49d92aa95f2ed8461dc214a40116f8991
    role: context
  - path: pages/traits/metabolism/acetogenesis.html
    sha256: e1ce3e8b975090a79d6af4e388f7e16cae6aa7451181700b98b657160dafad4a
    role: context
  - path: pages/traits/metabolism/acetone_butanol_ethanol_fermentation.html
    sha256: 61fdb457953df3ff25dadf6e82fc4973bbc629235e370f75efee836cee43635a
    role: context
  - path: pages/traits/metabolism/aerobic_respiration.html
    sha256: dc2257f7beab66a82b6d3fd54fbeff65288febf5db6bd8201dd44802b505ec38
    role: context
  - path: pages/traits/metabolism/anaerobic_ammonium_oxidation.html
    sha256: d01b72d073aa50ac9605f12e0da32778759b139c6dd1d9711d247a751f39cb4b
    role: context
  - path: pages/traits/metabolism/anaerobic_oxidation_of_methane.html
    sha256: 0eb3de914aeb0bd2796fafe902101c38afd6130284ebf09e86535a3712cd2009
    role: context
  - path: pages/traits/metabolism/anaerobic_respiration.html
    sha256: cdf7d291b13c2e7adda5251c32cf241f7c90823997be6eab0e056bc8ca3e892d
    role: context
  - path: pages/traits/metabolism/anoxygenic_photosynthesis.html
    sha256: f4d716e501d0d434879009a5dfbb758ac89c14e28a9d7e71eb9c7ee367be685d
    role: context
  - path: pages/traits/metabolism/aromatic_compound_degradation.html
    sha256: 4560727c6d97e97db4da55cefd86e8ee21db6b7a9788b30a5553ce59a25602b5
    role: context
  - path: pages/traits/metabolism/aromatic_hydrocarbon_degradation.html
    sha256: 3be6d807f14667d3d48b773e5f33aa2ad257af0c2fb60ca5489fd05afac17e29
    role: context
  - path: pages/traits/metabolism/arsenate_respiration.html
    sha256: 63675cf147ba0a15c8e10e284b05cbd1469e186e99ef939c1ccb341edf199f16
    role: context
  - path: pages/traits/metabolism/arsenite_oxidation.html
    sha256: f676213149ecad843810247d438221fe5b633cd060a2500b563a86ec3b9b3b24
    role: context
  - path: pages/traits/metabolism/assimilates.html
    sha256: 28eef0e745219d8bb2e5bdd68969f51b3c93fe16954a3615e37fb14bbbc3cfde
    role: context
  - path: pages/traits/metabolism/biopolymer_degradation.html
    sha256: ccb688405bf3b8184231adbf4335256eb032957f58472d99499288b047f9c66a
    role: context
  - path: pages/traits/metabolism/builds_acid_from.html
    sha256: 262d00fa1311ec673c6518ac577688bf477f418e0ea05c2dc709e779365cae85
    role: context
  - path: pages/traits/metabolism/builds_base_from.html
    sha256: 45d4b6bc9828d5b767966f7a3ab3adc486d83c34f299f9b57b8c769b53f54101
    role: context
  - path: pages/traits/metabolism/builds_gas_from.html
    sha256: c61fe2ae015559ab147f65b2d85b5f7b27d0f3365dbf72af1522f9fd8766ee1c
    role: context
  - path: pages/traits/metabolism/butanediol_fermentation.html
    sha256: bf3ad636717876d1ed2766fcb08a64e1560cf5cd85c0f73ecae64ec8f8cffa26
    role: context
  - path: pages/traits/metabolism/butyric_acid_fermentation.html
    sha256: ca6073049d2903f88b063d43eec86d9aff869012b8a44f5d6506a53f81dc19f1
    role: context
  - path: pages/traits/metabolism/cable_bacteria_metabolism.html
    sha256: 06e20b488b76c2c183fcc79e2e6d0ecbcdba14ee698a440b25f5595ff970b143
    role: context
  - path: pages/traits/metabolism/calvin_benson_bassham_cycle.html
    sha256: c4c94abbb8905353db6f540323046cf2c386e32dedc63e3fe0d025ff3a5c04e4
    role: context
  - path: pages/traits/metabolism/capable_of.html
    sha256: 726f16bbde6ee87498d3ef2f9063c0f756a907c8685338899a890b6491a43fb8
    role: context
  - path: pages/traits/metabolism/carbon_fixation.html
    sha256: d23f67ef81a28ee05a6d841f71e3dde6d7e6eb86f9698ca62cfda2ee1636479d
    role: context
  - path: pages/traits/metabolism/cellulolysis.html
    sha256: 51335337aff8799f0ce71faafca4a861eaa886dddc72c86ed8898e045fe450f7
    role: context
  - path: pages/traits/metabolism/chitinolysis.html
    sha256: 2622166588039e93d1f6d85657453ec14b84b85b6feebdfcbaad77296a9352d5
    role: context
  - path: pages/traits/metabolism/chlorate_respiration.html
    sha256: d4f8d2af99bc80a065dc011cfd84d0d6f4a3333cb2bc7e59d47a349cc9af9ca6
    role: context
  - path: pages/traits/metabolism/citrate_fermentation.html
    sha256: fafbfc9a3afb8ad6139cc34d5b1fb31de929ef263af01504ec705c01e0cdb355
    role: context
  - path: pages/traits/metabolism/compartmentalizes.html
    sha256: eb703d58a7e7cdd961a07dabda4ab3a8bcc10220ab61fea483ceedbc4c2add2a
    role: context
  - path: pages/traits/metabolism/complete_ammonia_oxidation.html
    sha256: f9b712fdc0d2b7c4364e02e105193d278aa55a9f6f79e39c2ddf2ba3e4998936
    role: context
  - path: pages/traits/metabolism/dark_hydrogen_oxidation.html
    sha256: b8a394f89493e2c38e92b4e7e8108234ddac65387669c91a49bcbfffb852243c
    role: context
  - path: pages/traits/metabolism/dark_oxidation_of_sulfur_compounds.html
    sha256: 87c3053ce0c8dd322cb387f289f4ea04e30e882cf2f2d16e9006a89f11979c68
    role: context
  - path: pages/traits/metabolism/degrades.html
    sha256: 6b3482bc179bc23f34318eb8ca1461445d05486acdf6ad5c63d11d781f9ba644
    role: context
  - path: pages/traits/metabolism/denitrification.html
    sha256: f9d067a6dd9b342bdbbeecc6f136cc11a9d135ec785c583e71f6ecad416791ac
    role: context
  - path: pages/traits/metabolism/dicarboxylate_four_hydroxybutyrate_cycle.html
    sha256: 3291c5b9cb4cdc5f703122b6e3f11927049e4759cf0e048ec2a284f74c8b6f30
    role: context
  - path: pages/traits/metabolism/dimethyl_sulfoxide_respiration.html
    sha256: ee867b02fc15beead3cc0bc9cf55a11701e321941c7796906a34e164d1c7adbd
    role: context
  - path: pages/traits/metabolism/disproportionates.html
    sha256: 45772d09eb78ba9b9499b7e51a4896e309030b6b46acbd639a258b6d203c245a
    role: context
  - path: pages/traits/metabolism/disproportionation.html
    sha256: 4658b3029e0e64f55999499cdc247a997962745b2ab3979fb3be443595840550
    role: context
  - path: pages/traits/metabolism/dissimilatory_iron_reduction.html
    sha256: 1283d48386903c95b8d9b4a26d8ca1bf7b4abdd2fef44d4a61a1349ae307454f
    role: context
  - path: pages/traits/metabolism/dissimilatory_manganese_reduction.html
    sha256: 7c1be5f85b6ae82b4f4ad3749c1e16ba02727a58104e062c1f97a22260366054
    role: context
  - path: pages/traits/metabolism/dissimilatory_metal_reduction.html
    sha256: 6f5abb42faf57597f08c86b82301d177eeb496f041c244019d17308b0dfe0414
    role: context
  - path: pages/traits/metabolism/dissimilatory_nitrate_reduction_to_ammonium.html
    sha256: fd7aeff11ad447ff0e2f81e8c030f28a3a7eb6bf4913b6f779f159ade8326065
    role: context
  - path: pages/traits/metabolism/dissimilatory_sulfate_reduction.html
    sha256: a84389a10a3f41961017b9c4659001ee6d2f85b8455e1deb16affac926fd32a3
    role: context
  - path: pages/traits/metabolism/does_not_accumulate.html
    sha256: 60a16135682340134f4d5ac2188586f4426a9c1c2527d79533a3e1956ef50f12
    role: context
  - path: pages/traits/metabolism/does_not_assimilate.html
    sha256: e2e1b7fbe551f77303f8d6bc34d47e4042dcb8bcee52b08c25a8dc94a2c6c1d8
    role: context
  - path: pages/traits/metabolism/does_not_build_acid_from.html
    sha256: 4a88c94e1b844b252066c4a8c6327ceb1f858a9c4b3a38a428dfa3e7371cb655
    role: context
  - path: pages/traits/metabolism/does_not_build_base_from.html
    sha256: d7d3daa04045ae095c908229ba1aa04372db956ee59c4d9d22b790e1de003b6a
    role: context
  - path: pages/traits/metabolism/does_not_build_gas_from.html
    sha256: 0869171e8225271238b2afd96296a12389344986613fd28f9135f762ffe1ac9f
    role: context
  - path: pages/traits/metabolism/does_not_compartmentalize.html
    sha256: 1a4ac9f49dec1320a33acc0930714071ad1a878fb160b8ef1ecdf673683f3eae
    role: context
  - path: pages/traits/metabolism/does_not_degrade.html
    sha256: 750e0754267abdd25b4f34091a6f45c5611e48b08854dbf5ab2f6231223364e9
    role: context
  - path: pages/traits/metabolism/does_not_disproportionate.html
    sha256: 7b62fec9489089cbe46b8bb8a71a7c880ae6d73aa3127e0259b5c7dd58f1ea4c
    role: context
  - path: pages/traits/metabolism/does_not_export.html
    sha256: b4eb1942b1721e8f384390fafd609480a10cae5e3aebe5cde789dc782f1a7e7a
    role: context
  - path: pages/traits/metabolism/does_not_ferment.html
    sha256: ca1bf3216fe1f1846a19475e4da7309fb0fef1bd06f8627cbb13c3c646fa0348
    role: context
  - path: pages/traits/metabolism/does_not_hydrolyze.html
    sha256: 029b7c4ec37b7922bcedb7a451f7884b7fee6ce77cfc73e91c2eca4154c3ad8c
    role: context
  - path: pages/traits/metabolism/does_not_import.html
    sha256: c8649aeb509392f5e291a6cfd1547cc325b792f9965bebb2dc8523e68cca63c8
    role: context
  - path: pages/traits/metabolism/does_not_oxidize.html
    sha256: 8c45689c236f3e184e8b14501b377ebf0a874c697850f101e8547b2648b858c7
    role: context
  - path: pages/traits/metabolism/does_not_produce.html
    sha256: eb00dd7995b2c625cbf9f036671dab8af13fe16208247234fc6ec1181d4f0b2f
    role: context
  - path: pages/traits/metabolism/does_not_reduce.html
    sha256: 5aba0d0b4ef39525baa3c3dc665372c88832c73a13607fecc4c5b84760170c89
    role: context
  - path: pages/traits/metabolism/does_not_sequester.html
    sha256: 62b015dc90ba4e9153f6cdca1782398f14ad165b3a21eae1cb5ce777f5ba4920
    role: context
  - path: pages/traits/metabolism/does_not_show_activity_of.html
    sha256: cbb14a4b5f519a51638d5edd51058a63c48b70aa116f2008313f5bceb714cf97
    role: context
  - path: pages/traits/metabolism/does_not_transport.html
    sha256: 297423c00a178da6062e67a12905bf6714d4501d3dc6aa96524ebfc0180a045d
    role: context
  - path: pages/traits/metabolism/does_not_use_as_carbon_source.html
    sha256: 079c6f10ea1b9dbc0a02d0ae0ae0062dca6bd0dbae4130a748d4af96d3b98b5f
    role: context
  - path: pages/traits/metabolism/does_not_use_as_electron_acceptor.html
    sha256: f2deaa033ca123b573bfe7ffd9a902c5df02cc81145241ed0406496a6150156e
    role: context
  - path: pages/traits/metabolism/does_not_use_as_electron_donor.html
    sha256: 4e812cd6be965bf92e2c16556e18c7b253ea1a1a2d8978ced4c29b2dae82de74
    role: context
  - path: pages/traits/metabolism/does_not_use_as_energy_source.html
    sha256: 818a3401194bef66b73a76c3e62afb936b17ead58884b227487d3d1c8d5e1600
    role: context
  - path: pages/traits/metabolism/does_not_use_as_nitrogen_source.html
    sha256: 1cde7508e24ec5e7624d579100e3bee1004178e505a0c28655b54d45b7fffa9f
    role: context
  - path: pages/traits/metabolism/does_not_use_as_sulfur_source.html
    sha256: 5803c1c6ab0366d63b9566e9c8a48058615545433346b252c8bd4191f2dd3401
    role: context
  - path: pages/traits/metabolism/does_not_use_for_aerobic_catabolization.html
    sha256: 2e1a2a05258a30999ac72a92bb8ae824445da82870b9054b24f028417728d626
    role: context
  - path: pages/traits/metabolism/does_not_use_for_aerobic_growth.html
    sha256: 1ee3257c1ff6ee837892537cbac9f5a3e6b96ba795464dc0c5d059e78e031345
    role: context
  - path: pages/traits/metabolism/does_not_use_for_anaerobic_catabolization.html
    sha256: a274eb8bcb190759c2c04bb85ab5676cd13f4c912ccd92fd83ba5d517e937e34
    role: context
  - path: pages/traits/metabolism/does_not_use_for_anaerobic_growth.html
    sha256: 3220a05e40195f2311c12d70ace65d50b20fb9d0b6569c577bb74a690e815785
    role: context
  - path: pages/traits/metabolism/does_not_use_for_anaerobic_growth_in_the_dark.html
    sha256: cdc8eac9d7caa1b260d495e166076588601041dba545306f45660bd9a588d496
    role: context
  - path: pages/traits/metabolism/does_not_use_for_anaerobic_growth_with_light.html
    sha256: 2548b0013d34e49effe1f13da467d042bd3838f644269365f105719e54d6c8af
    role: context
  - path: pages/traits/metabolism/does_not_use_for_growth.html
    sha256: 8eebc42e376cefd44041aeb1b10f71d45bb3c293dc9bcef1a54d01df835361aa
    role: context
  - path: pages/traits/metabolism/does_not_use_for_respiration.html
    sha256: b0626f83469a0b98a51bcf59f78e01179d40f88738d51d3f0dc9036c4e8f4a9d
    role: context
  - path: pages/traits/metabolism/does_not_use_in_other_way.html
    sha256: 383feebb8acdfb222ce73b6cfb85357be286a1f2b2a589a6c12e8604e4088225
    role: context
  - path: pages/traits/metabolism/electron_transfer.html
    sha256: dc42092dd4f2f38cc8ee8a3af66dbf652d61e2ddce53963d166cb5efdce6a56d
    role: context
  - path: pages/traits/metabolism/enzyme_activity_analyzed.html
    sha256: 06d4fec7b2c9e4e26f669ce1020f3a55bb4185a288f61285b50f3aa50818f312
    role: context
  - path: pages/traits/metabolism/ethanol_fermentation.html
    sha256: 5191ca3fd2d1b2709dad75578054b4d64a57d92457c53557d98267b60a214b49
    role: context
  - path: pages/traits/metabolism/exports.html
    sha256: f7ad3143cbff178eccf08987447a97528d6f4d494fef81f928cd34917ad75374
    role: context
  - path: pages/traits/metabolism/fermentation.html
    sha256: a0c73e2c10ebe9df085d0b5aaa47b347827abb0a759e147e66919e4832b90e10
    role: context
  - path: pages/traits/metabolism/fermentative_hydrogen_production.html
    sha256: c4d1e5589cd8b4b795819f175ba41390c46e7f0270bd9a9e138afc2f07de6ba0
    role: context
  - path: pages/traits/metabolism/ferments.html
    sha256: 15957fbc4b39bcf04ce19eee3bfff33b41b2577861a22eea5555a253dbc8519f
    role: context
  - path: pages/traits/metabolism/fumarate_respiration.html
    sha256: 1aa5d6f37498ff3443e025312f9883390fa3ae1c1c3247ecc80724c367b35df3
    role: context
  - path: pages/traits/metabolism/has_growth_nacl_observation.html
    sha256: 90573a6268fb38595cb66c2099a59e6fd067ebcb0772b595dfbc2d0a6c8d8a98
    role: context
  - path: pages/traits/metabolism/has_growth_oxygen_observation.html
    sha256: 0d800a99cef5013fdefd997d3fb6b96c7c9542e331742f44d5fcf88c42b119a9
    role: context
  - path: pages/traits/metabolism/has_growth_ph_observation.html
    sha256: ad21f086403fc1b020f8bfacf1922af900e8831d4a32ea14cc0ff61932a6b429
    role: context
  - path: pages/traits/metabolism/has_growth_temperature_observation.html
    sha256: 77842f99b77b2463f282549cf646ff5e238d3900d4339ee05aee6c21ca4bb013
    role: context
  - path: pages/traits/metabolism/has_nacl_delta_observation.html
    sha256: f22600032624acbc03952825bc1151d78b59f8b658f17b9ca7d81e841fa545de
    role: context
  - path: pages/traits/metabolism/has_nacl_observation.html
    sha256: 5170088d4663367f137fc792c756b85357dc709bc91ae8c0c7efcf4cb328d304
    role: context
  - path: pages/traits/metabolism/has_observation.html
    sha256: 8f57a33e01a1e96327a035fa870871308f0244eee0e28aaa6f1485e5f7f6f955
    role: context
  - path: pages/traits/metabolism/has_optimum_nacl_observation.html
    sha256: 8c919658bdbc3a705b8e122f5b689ab7a28fd93e00aef97bd5408c73e86f588c
    role: context
  - path: pages/traits/metabolism/has_optimum_oxygen_observation.html
    sha256: 9cdbbb92a4177fe5e50a9a8bab4aabef0b52b4a6044c1a3d139d3b669c543bb5
    role: context
  - path: pages/traits/metabolism/has_optimum_ph_observation.html
    sha256: e18ab82579c3aefce607aa0f6c6639abe55f1181a1bb7ac64d21b6de272583d5
    role: context
  - path: pages/traits/metabolism/has_optimum_temperature_observation.html
    sha256: d52724e59a10c3364e4dbe3729a0ab6da4867520c725723d1319d598670fbf4f
    role: context
  - path: pages/traits/metabolism/has_oxygen_delta_observation.html
    sha256: f609a2fee50bdfa76a6d2bb2f7ae4c759e1d7ab58dffb234a5576b45bfbfe596
    role: context
  - path: pages/traits/metabolism/has_oxygen_observation.html
    sha256: 7f20e382bb4f931831771b88aea6d98a8b1be77c7ef362e1fc2c386962cfdb3b
    role: context
  - path: pages/traits/metabolism/has_ph_delta_observation.html
    sha256: a809275da7606fe4d93613f530f69f4e3161e020385d8b763841acb0151a15a4
    role: context
  - path: pages/traits/metabolism/has_ph_observation.html
    sha256: bb05475cf63649ff65433252f8dc7c8a43cd9c2f62e358860b95856473a71195
    role: context
  - path: pages/traits/metabolism/has_phenotype.html
    sha256: 45ffeb963f7dd6b2389e927707503afac25bbd2e1126aca3261c69c757ee4ddd
    role: context
  - path: pages/traits/metabolism/has_quality.html
    sha256: acc63fb1d5ad2a028ece774b854bc28349656234a951ec1010a37565f77995b3
    role: context
  - path: pages/traits/metabolism/has_range_nacl_observation.html
    sha256: 56ca65c6ea5211a55ca7aeb3dbbde8e90c6f1d4ce2bd18c0b3ea88ec11d6ddaa
    role: context
  - path: pages/traits/metabolism/has_range_oxygen_observation.html
    sha256: 9449866f5a41d25999d7d17b898fec31ac3f67eabbc2dccd8ecc6ab8f12cc4a3
    role: context
  - path: pages/traits/metabolism/has_range_ph_observation.html
    sha256: 5353971e438d66a61c2da291de941e027245cb019c1d86a8e433be27fcbab954
    role: context
  - path: pages/traits/metabolism/has_range_temperature_observation.html
    sha256: a282112d202e6206bb1d4789ce1628c2fbc9fe5b7eb97b63b5a6bfcbf5ed2424
    role: context
  - path: pages/traits/metabolism/has_temperature_delta_observation.html
    sha256: 24d42664652e5470353a6074f8ea98c723e58f153db80a9b8f256a11acb7692e
    role: context
  - path: pages/traits/metabolism/has_temperature_observation.html
    sha256: d8d0fb8d9920b04dba908809724eac5eb826f2c81740802bffa611d15f4a4a36
    role: context
  - path: pages/traits/metabolism/homoacetogenesis.html
    sha256: ec61806fdc16c914b45b7c34cfb6fd9f1175e32e809172b7852a1b503ad54642
    role: context
  - path: pages/traits/metabolism/hydrocarbon_degradation.html
    sha256: eef47ffdeab9ee3c8c5fd31c2e5795088c63a44dd5a6543f357bffe343659375
    role: context
  - path: pages/traits/metabolism/hydrogenotrophic_methanogenesis.html
    sha256: 9c0bb0209aefd0f0564175dafc48de82e0bf395de05fc5ccc9bc8aab5e3095eb
    role: context
  - path: pages/traits/metabolism/hydrolyzes.html
    sha256: 9ecaacd43cb3d564ebb68f9edef7dea03ea3bf49a2716c773c35334c882b09d3
    role: context
  - path: pages/traits/metabolism/imports.html
    sha256: ea0d9918e88380aa07f32612ee7b51745f2dee73ad4eeadc6e501993f6cbd35c
    role: context
  - path: pages/traits/metabolism/iodate_respiration.html
    sha256: c4c693f52b9013c105f5f6a0a2055d4e2fcc26fc78ab540499ef84af78d047b8
    role: context
  - path: pages/traits/metabolism/iron_oxidation.html
    sha256: 0009422214d40e32e48229fcb2f32e7e85ada74b3d10ae21e2269cde0301b87f
    role: context
  - path: pages/traits/metabolism/is_not_required_for_growth.html
    sha256: 51fda59acbe47bc80052243ffa9d3dc6ca87f060bc6baa107bc3252a51993207
    role: context
  - path: pages/traits/metabolism/lactic_acid_fermentation.html
    sha256: 79031f9034a90b9a1023aba6c7f6d8096c160940cf8cae638e2782e9bb362ff9
    role: context
  - path: pages/traits/metabolism/lignin_degradation.html
    sha256: b5317999be780a6d8ceb841b377b611dcb708bc9ec0f29cea598b79b2949bfa7
    role: context
  - path: pages/traits/metabolism/lipolysis.html
    sha256: 7d1bfa78ea8e2e050547b272724964ebf80926572c241d6b7d2d7f83a04888c9
    role: context
  - path: pages/traits/metabolism/manganese_oxidation.html
    sha256: a6fd1c5a7aa4d3caf64ecabdec1d238afbaf2b1e0518df40ed68d0d9ff77edb4
    role: context
  - path: pages/traits/metabolism/metabolism.html
    sha256: 9b6002845930e7837afea255c4727e65a96ecacf539b9d086c646cdfd4eb8ca3
    role: context
  - path: pages/traits/metabolism/methanogenesis.html
    sha256: 64c2c1cc6bba1b8953c0881b4e3e3e99ad811edc1dd4f6ede6dce3f812089b9e
    role: context
  - path: pages/traits/metabolism/methanol_oxidation.html
    sha256: 82096de574dd3659728ab57c44cc4142c0eb7807506951fd9249dba8fef7777c
    role: context
  - path: pages/traits/metabolism/methyl_based_methanogenesis.html
    sha256: a5abe0553c55fc52907fd97a746e73308a657b8ea9afcc129fa0ab127bb19b47
    role: context
  - path: pages/traits/metabolism/mixed_acid_fermentation.html
    sha256: 10ba363e624e8fa799874dba02c9cba3f1d40a6db257f144d2a8b0ab3cc63837
    role: context
  - path: pages/traits/metabolism/nitrate_reduction.html
    sha256: a0436d18cab1fd60bd5eb51e091776f832e74b4d998c212803c6806366b7d34f
    role: context
  - path: pages/traits/metabolism/nitrate_respiration.html
    sha256: 44b311102b73226e468ebed7907a421b7d0f2628ed33d806f0fc2e99efdd9e20
    role: context
  - path: pages/traits/metabolism/nitrification.html
    sha256: bbb4f13c5c5c5f7eeb5d347374235c555499daff80efa0f199e090e74abbdbaf
    role: context
  - path: pages/traits/metabolism/nitrite_respiration.html
    sha256: cb1dde4a8d70e226e76a75d53c32d22d9a96fc4bef370b9afb48e5ee8d36b728
    role: context
  - path: pages/traits/metabolism/nitrogen_fixation.html
    sha256: 23c53b6fab25d8abb2c7f639020a44010d0b4d656bd0c233886ba40cbdb5f397
    role: context
  - path: pages/traits/metabolism/nitrogen_respiration.html
    sha256: 47404942745e94e8a11b05a864a81fa9f7be1f7f01f674b09ca113ec844079e8
    role: context
  - path: pages/traits/metabolism/organism_interacts_with_chemical.html
    sha256: a335bfe2c1281866c2d31d3d2ba14ce93ce29d3ea6561293b5b4747eb5485fe6
    role: context
  - path: pages/traits/metabolism/organohalide_respiration.html
    sha256: 4d28755ceb1679d18d0a98afd9caf150eb3736b5615f3c45c37a644fb0225a0b
    role: context
  - path: pages/traits/metabolism/oxidative_phosphorylation.html
    sha256: 1ba84e0241e6e94a42d3c9c41a20ef013a479f4e9f2003d814c706ad8e07c474
    role: context
  - path: pages/traits/metabolism/oxidizes.html
    sha256: f42de9e1130e4085eb3957cf56094ddd656bcff6ad979ea3d3c99909b31e117b
    role: context
  - path: pages/traits/metabolism/oxygenic_photosynthesis.html
    sha256: 2523f6bd514d4ff4d4f3895a26af073248774d5058e752e50bab8bf6e16ff2b2
    role: context
  - path: pages/traits/metabolism/pectin_degradation.html
    sha256: f603043dae97403fc3f4b37a1e15698e4614cee009573257edfc241238ffa2f7
    role: context
  - path: pages/traits/metabolism/perchlorate_respiration.html
    sha256: d01fabe5ec6c20583c836fa330e0f0c1371ad10b612e02cc0ba394ac510afe0a
    role: context
  - path: pages/traits/metabolism/photoferrotrophy.html
    sha256: 230245c6b6b6a0f100e515d22d3ed16d71e1b002d3a01b6d0bc8d1bd01c66079
    role: context
  - path: pages/traits/metabolism/photosynthesis.html
    sha256: 82e13ed5764c8d1ae12fa853a0052989999f13f9b99f823c73810802dceb7abb
    role: context
  - path: pages/traits/metabolism/phototrophy.html
    sha256: 993750baf7273488e5e7268c42843a04191be915ca66f8f03c46ecf3e655b0e5
    role: context
  - path: pages/traits/metabolism/produces.html
    sha256: 6c2e36710bca1360e30a8c71f2cba9a6c46a7fedf71c121b78ec11de25d8a1e5
    role: context
  - path: pages/traits/metabolism/propionic_acid_fermentation.html
    sha256: cb937ff45aba9ad3bf3472b1dcbb6ade4f6dddc47c85c0ff8bbf1066298d8b94
    role: context
  - path: pages/traits/metabolism/proteolysis.html
    sha256: 5e55eb7133a48b7110ea3872f088c882f48399e132d877b8d02e0af8945a1d52
    role: context
  - path: pages/traits/metabolism/proteorhodopsin_phototrophy.html
    sha256: 36888502699b4319a9a7620e5361322e0fdd7a996bdde026d779fa9a9cb269f1
    role: context
  - path: pages/traits/metabolism/reduces.html
    sha256: a21b14650c9e424732ebd3184359dcc36977936ab81f6fb93bacc4449792e12f
    role: context
  - path: pages/traits/metabolism/reductive_tca_cycle.html
    sha256: 7fd0b54480e7a3715fbedfd6efcd5c99c5096a9e41d62eb957dd01ce18c755f5
    role: context
  - path: pages/traits/metabolism/requires_for_growth.html
    sha256: 3d98541a247a8c769719cff09dba7311138c0c8575ba1ee7d5cd2837c3350ee6
    role: context
  - path: pages/traits/metabolism/respiration.html
    sha256: a966ebf829d3c8878f2380ca225131c86f5dd936e027d3a0b38be25757ff9edc
    role: context
  - path: pages/traits/metabolism/respiration_of_sulfur_compounds.html
    sha256: 3074e66770d5b100069f8350ce07942ab21e6ad5710db1311fd51d558f7249de
    role: context
  - path: pages/traits/metabolism/selenate_respiration.html
    sha256: 6879fe067201a46920858b95902ce43031cfe348c106e0ed15071796f4da93a9
    role: context
  - path: pages/traits/metabolism/sequesters.html
    sha256: 3c64b4175b4b72369e7b208fd7c7638af8593d294b0aa8a0664cc7cd97195083
    role: context
  - path: pages/traits/metabolism/shows_activity_of.html
    sha256: 025af69916ff6f70c184e4e3759f7f933e2efbee1dda3ec52674e7eb6cd5c1b3
    role: context
  - path: pages/traits/metabolism/starch_degradation.html
    sha256: 67297d42909dc9a17db472ee841cb131b81221a1faaa365870031941d40628f6
    role: context
  - path: pages/traits/metabolism/substrate_level_phosphorylation.html
    sha256: f4d2a6cce9c699f15be6f74724aa3af8d82a74efdb250756ad8a04c90a8b3d48
    role: context
  - path: pages/traits/metabolism/sulfur_oxidation.html
    sha256: dacaab7ba71e8b40e291e2b0898fb6110bb37f84f97fee128480a9d8819eed2b
    role: context
  - path: pages/traits/metabolism/sulfur_respiration.html
    sha256: 133e01f4105e385fa122585a0fd0e961ffcf237ace45c6bd2eae517047b1661b
    role: context
  - path: pages/traits/metabolism/syntrophy.html
    sha256: 6cc7603630a3ab57ab495cbed7d5beb4213e19e614081b1bdd780e6d337a0a22
    role: context
  - path: pages/traits/metabolism/tetrathionate_respiration.html
    sha256: 9d88796a908c48e0835fdea492d6d193481dfe7502fac28317fc7035496c3fd8
    role: context
  - path: pages/traits/metabolism/thiosulfate_respiration.html
    sha256: d3dfac2e0ebbb24db7cc27a446b412bd05551ad52bb9a816930dab7a8b6085c2
    role: context
  - path: pages/traits/metabolism/three_hydroxypropionate_bicycle.html
    sha256: cebfe892e3770fd147b7675dd08ee0994a4188a605c7a0a213ca7ab104546fd3
    role: context
  - path: pages/traits/metabolism/three_hydroxypropionate_four_hydroxybutyrate_cycle.html
    sha256: 0db0c627cd3740781a7160dcce5b7566b634cd149d2523120ab7d23e1f314f61
    role: context
  - path: pages/traits/metabolism/transports.html
    sha256: 68d1cadeaaaa194a80ac145a4b4fbce40151577ef750881884c18d6f144ea171
    role: context
  - path: pages/traits/metabolism/trimethylamine_n_oxide_respiration.html
    sha256: da8f2e0d0fee0992aa8a8fec2a4272190dcd5a115ad4310545d27ad13b3bce29
    role: context
  - path: pages/traits/metabolism/uses_as_carbon_source.html
    sha256: aaf2e263fd1a9d20bf28e77be95d08e5a828332d92586625b069eb760e34fdaf
    role: context
  - path: pages/traits/metabolism/uses_as_electron_acceptor.html
    sha256: 49461fec87fd391b4c663a74d77708dae73d3780e0b558d7f80e86ed9d640a15
    role: context
  - path: pages/traits/metabolism/uses_as_electron_donor.html
    sha256: 83df12c6889fa93695d769ece8bbb404eba6acc5621672405983f7b7095086bc
    role: context
  - path: pages/traits/metabolism/uses_as_energy_source.html
    sha256: 127f087bfe3c9ca9f213f644dde9410270946065cb91016a8c5af8699ea2f774
    role: context
  - path: pages/traits/metabolism/uses_as_nitrogen_source.html
    sha256: 28f9bb4e799f610cba631dd17fecebd0ac4c952f04615e69586ea59a8d4b3d06
    role: context
  - path: pages/traits/metabolism/uses_as_sulfur_source.html
    sha256: 3b96c69814776f56dc322886523160bbccf2b5ce425889da6bac4c0772891a0d
    role: context
  - path: pages/traits/metabolism/uses_for_aerobic_catabolization.html
    sha256: 17d5c92f1797b749c6cda27221148ccc23d073aca0dca111883d473063d980ff
    role: context
  - path: pages/traits/metabolism/uses_for_aerobic_growth.html
    sha256: 584e8d67036913ec84e60b05bb7e902f63dfb1fc6ecae8096e82b88a2a2b53c1
    role: context
  - path: pages/traits/metabolism/uses_for_anaerobic_catabolization.html
    sha256: 9782570d781b5a42579edf0cc89a08a664eb5a5001f0b566f42dd73ce6fce4dd
    role: context
  - path: pages/traits/metabolism/uses_for_anaerobic_growth.html
    sha256: b14c529f49bf6b9d38ee179fc2a6bf18e8582025214d2d818623e310257668fd
    role: context
  - path: pages/traits/metabolism/uses_for_anaerobic_growth_in_the_dark.html
    sha256: 174bddf060f44b2ea21608f1b1ce81fc7be6a77b42ee5f2b2f22cc5059648fd7
    role: context
  - path: pages/traits/metabolism/uses_for_anaerobic_growth_with_light.html
    sha256: 241d5bc48e9c4f4eb4912d610e82d64f5c72a6788efb2f77c7098bd8be12026c
    role: context
  - path: pages/traits/metabolism/uses_for_growth.html
    sha256: 73780be9df340161285ce5f46e00958241b76e79fccfcb7a250fa64d5c0612ca
    role: context
  - path: pages/traits/metabolism/uses_for_respiration.html
    sha256: fcfa6ca6b267bf5a852f6f6629b1f70911a687273308454ed673fbccf58a22b8
    role: context
  - path: pages/traits/metabolism/uses_in_other_way.html
    sha256: 500dc2d12d664fa15b75af9bd6ed216711c90167928a39fc2085ca2abe7a45dd
    role: context
  - path: pages/traits/metabolism/wood_ljungdahl_pathway.html
    sha256: ac4b2234a1b81cf335dfeaab2cf203547994ec3c0a8a16f156f2fe9421bc4dd7
    role: context
  - path: pages/traits/metabolism/xylan_degradation.html
    sha256: 725fa37cd80414740e0d6c181223831bcaa5562170013e2f8f7fca1e01beef3b
    role: context
  - path: pages/traits/morphology/akinete.html
    sha256: 78d81f6fe93d0fd20350b44b66d8920cebdcbca1a5a503cb719d81d64fc91b13
    role: context
  - path: pages/traits/morphology/amphitrichous.html
    sha256: 95b01fbe0768223296f0e5afef9bb30f6ff55efe7545ea01fb724db639840aa0
    role: context
  - path: pages/traits/morphology/axially_filamented.html
    sha256: b6eebbe9d86cc340b2a43a6e883cb6a60ce5dfc913f0a18646a2b7807d73e90e
    role: context
  - path: pages/traits/morphology/bacillus_shaped.html
    sha256: 629c755ac5634c4c32f8b9ad8fa3aa47dbc37e6a7772fbd5953924af0ca1ec1d
    role: context
  - path: pages/traits/morphology/baeocyte_formation.html
    sha256: 28a274232fdeff0dd7c3864a90b76e2230c97008668588de6693f8c4642b4509
    role: context
  - path: pages/traits/morphology/black_pigmented.html
    sha256: 6f7c881ed6b2a3fbf64f5205d1e4ef81d28736e4260d18585b9a5d74ff0c16e5
    role: context
  - path: pages/traits/morphology/branched_shaped.html
    sha256: cdf9b7611de9e2d09ae93b00a5271b8a982cbf35b9d587b90a33103b51fcd971
    role: context
  - path: pages/traits/morphology/brown_pigmented.html
    sha256: ff2701b2c0999e539e308cd54747e293af653696b6d09c79386dc7dd4cbe336a
    role: context
  - path: pages/traits/morphology/capsule.html
    sha256: 8b5a4a89a340ffd9168c38386dec4d8043f3cffdb1e21ba152f747aad3cbd451
    role: context
  - path: pages/traits/morphology/carboxysome.html
    sha256: 8ccde0ffe284bddecbd419201f81ee6684f24fc6cd41a562da09cf7dbd725526
    role: context
  - path: pages/traits/morphology/carotenoid_pigmentation.html
    sha256: 03e7fd311d5d230777ef03816e744f2870fc0fed6ffac25599f78fbce922ea3d
    role: context
  - path: pages/traits/morphology/cell_length.html
    sha256: 8ac1f3855b26fd547a1be0d075ed9bae07e052ddbb359a0268a76450ceae0436
    role: context
  - path: pages/traits/morphology/cell_length_large.html
    sha256: ceee9803722e4424989257069e52efaedb15c357fd60daba7880cc85b2a0f389
    role: context
  - path: pages/traits/morphology/cell_length_medium.html
    sha256: 6d8b06bb306fa766d0209e188a422cd61096242e5c7067d85cd67270f030c5e0
    role: context
  - path: pages/traits/morphology/cell_length_small.html
    sha256: 6b682bae6efb50a72bc51e656059ba6fca887f6c75b3cd8ded0861e562ffa431
    role: context
  - path: pages/traits/morphology/cell_length_very_small.html
    sha256: 7a0422407bb8baa51e509986cba5ac673b57b7c88a83a5ea8253173945aa3265
    role: context
  - path: pages/traits/morphology/cell_shape.html
    sha256: 295a0703f7163435fcafe5c1660652e539f168bf92d9f36141702af5614cb25e
    role: context
  - path: pages/traits/morphology/cell_width.html
    sha256: 3ef7a496750c646b0ef6e97d992473cb71def78f7c809ef04f67063c3c2690dd
    role: context
  - path: pages/traits/morphology/cell_width_large.html
    sha256: 1ee12cbfb37b3ad384b36ef21841ffad520852887456e28c8952e8fb466b1da1
    role: context
  - path: pages/traits/morphology/cell_width_medium.html
    sha256: c86501e315625ff1e09e3c628261b703d2498acb5e2329001ebc40f53f20aa47
    role: context
  - path: pages/traits/morphology/cell_width_small.html
    sha256: 3a5c2d8a0be6c6b1c88a323903380619608743bff9bae37916108b897922f2fb
    role: context
  - path: pages/traits/morphology/cell_width_very_small.html
    sha256: 45ef7d5c3a5ebfcf856c8b6cc71fbb53b2895466be1c1a0e068835cc132f8b4f
    role: context
  - path: pages/traits/morphology/coccobacillus_shaped.html
    sha256: baed2ab98be85d33efaaf43b1e01dbfa2ad69aeebbc6f38359db46e173898ae0
    role: context
  - path: pages/traits/morphology/coccus_shaped.html
    sha256: 4f339bf3bd79f8d39bba5722ef433f5e135b88ea14837007a5de885848606367
    role: context
  - path: pages/traits/morphology/coenobium_formation.html
    sha256: 5ad4ad89bcf87b3e7893603ce1b39c49c351d721526531c6370a241083550442
    role: context
  - path: pages/traits/morphology/cream_pigmented.html
    sha256: 62e9d1f9fc355a9b106c6428767cceb6bd0e4a85c039ccf9ecffa130f83138eb
    role: context
  - path: pages/traits/morphology/crescent_shaped.html
    sha256: 6c1e829acc0997ef1444cde9974d4ba332bd0b70cb6cfe4f6c037acdb9fa73e7
    role: context
  - path: pages/traits/morphology/curved_shaped.html
    sha256: 80b4116a60fe7735bd43d588cc1aedfb812b37062a8dd97f00b348baf9ed3f3a
    role: context
  - path: pages/traits/morphology/cyanobacterial_multiseriate_trichome_formation.html
    sha256: aa89ba4871b6555a330311c81d53b883b65f062bf8af788e7efffdf8930c86af
    role: context
  - path: pages/traits/morphology/cyanophycin_granule.html
    sha256: 4dd6bc51728594029818a2e77e7951a35005c3b72c7159b6d1fa33f6a2724f81
    role: context
  - path: pages/traits/morphology/diplococcus_shaped.html
    sha256: b1c62350e23ac4455a3cac2f39b42b12303fe669a572a225550116370287dbf5
    role: context
  - path: pages/traits/morphology/disc_shaped.html
    sha256: 151e2e8d6a4ce32e74e9817377716d9f21a9b45bb69d99ef17ab2f1f919c3d91
    role: context
  - path: pages/traits/morphology/dumbbell_shaped.html
    sha256: d1d10364c08504271be6be2135daf9dc1c31341ae563801aef0f238e89237624
    role: context
  - path: pages/traits/morphology/ellipsoidal.html
    sha256: 7b170ffe6aa90341a57e3cbd5baae83bf8436b84a34b45fee2c54498a227884c
    role: context
  - path: pages/traits/morphology/false_branching.html
    sha256: 6e060c754f65203e407206c8d07d188f5c993c7d890c1d589b8ff37d3bb58910
    role: context
  - path: pages/traits/morphology/ferrosome.html
    sha256: 844324c586e856998910e3ba360b37b25dc64138958212ef1b69d4ae3c2ce809
    role: context
  - path: pages/traits/morphology/filament_shaped.html
    sha256: 094eea66a1449a7d25c8f85f7446979e1de21aacd8326e2221e87230c701252b
    role: context
  - path: pages/traits/morphology/flagellar_arrangement.html
    sha256: 3989752dce0dc158d46caa6f067b70d89db5d7cfe1b97120551f8ef3b2c848d9
    role: context
  - path: pages/traits/morphology/flagellated.html
    sha256: e17a71c4f69880e146213c7c11aa85f233f2f0d04453c2fe5af14b939b222895
    role: context
  - path: pages/traits/morphology/flask_shaped.html
    sha256: 523fcd5cfdf53730f3fe078a5939ba362fec47418629f29602b6109056a33099
    role: context
  - path: pages/traits/morphology/fungal_adhesive_column_trap_formation.html
    sha256: 6e8824832e881096709a71ed8c27f9cfa78bc32edaf9c788e528f8fe420902c1
    role: context
  - path: pages/traits/morphology/fungal_adhesive_knob_trap_formation.html
    sha256: a7aff27f87f18204de7ca9128a1a534b441d022548bfa8b8a07376debd980802
    role: context
  - path: pages/traits/morphology/fungal_adhesive_net_trap_formation.html
    sha256: cdb90a4ce4033d985818cf8031f944e825f095677df117e67883ee693b7e5ed1
    role: context
  - path: pages/traits/morphology/fungal_appressorium_formation.html
    sha256: 4b980b71c327601177c1099c4d9236d63ac0b6ce7f14f93cc25c860bc9baa14b
    role: context
  - path: pages/traits/morphology/fungal_arbuscule_formation.html
    sha256: 82544dd7656ffeaa0272946a5624db754f8d8ca4491fb8e08010c64737f1ea3d
    role: context
  - path: pages/traits/morphology/fungal_auxiliary_cell_formation.html
    sha256: 2f3d7fb8c841d16d9a14847e9972cac81e2062e98d64d4105c936de2d279eb5c
    role: context
  - path: pages/traits/morphology/fungal_branched_absorbing_structure_formation.html
    sha256: 3136307b6bbd0b10e2b8ac7ab3061acf2e2684b5f81da78a2b399c0f32e653f4
    role: context
  - path: pages/traits/morphology/fungal_chlamydospore_formation.html
    sha256: 27de1bbc4809af0a92e755a6d0c2b77272bbd2327d13e0325753f35b2a4ba1b1
    role: context
  - path: pages/traits/morphology/fungal_conidiation.html
    sha256: 8a1cf6ed862082166ac6bd822a53ba7d0e9a4530fa4241f68756fd9278717669
    role: context
  - path: pages/traits/morphology/fungal_constricting_ring_formation.html
    sha256: c9aa9a644cb3f27f382b3b68df28873f46a1442d3b709a779c35488aa43e360f
    role: context
  - path: pages/traits/morphology/fungal_hartig_net_formation.html
    sha256: 4694ef2ce9bd1e78c2e8805d9a11da974382b91807a247c10ff7f65ebb655b03
    role: context
  - path: pages/traits/morphology/fungal_internal_mycorrhizal_vesicle_formation.html
    sha256: ffbd6644b6017dad80008a2393fa8917104939b22810c79654ee607e9b0f37c3
    role: context
  - path: pages/traits/morphology/fungal_mycelial_cord_formation.html
    sha256: 3ab2c9bc045edbda6976d6b4791ed45e6e40d55d3bebb81d9fe8d7b08914f789
    role: context
  - path: pages/traits/morphology/fungal_nonconstricting_ring_trap_formation.html
    sha256: 853d632f358ba3d55e9be03a8bed4b0e0f50dd04b69fe915638d2691db897042
    role: context
  - path: pages/traits/morphology/fungal_peloton_formation.html
    sha256: 981ed93d58cf290874a9ed8edef2ceb60ab25c9e77694b2c7b29b32d9860eb0d
    role: context
  - path: pages/traits/morphology/fungal_rhizomorph_formation.html
    sha256: 53d72a80d33bd3a7fbafb48b87d45c3d4d5af40287aad8303c394513f8fa2635
    role: context
  - path: pages/traits/morphology/fungal_root_mantle_formation.html
    sha256: 30382cc5f25804b45439d473464f26ce2f3d9d2d2c7f5dfd7d9bbc0631bd7083
    role: context
  - path: pages/traits/morphology/fungal_sclerotium_formation.html
    sha256: 607e02f356aadcc639fddcdef23a4408f279b72ce9c1824ffb12e2091dc246b1
    role: context
  - path: pages/traits/morphology/fusiform_shaped.html
    sha256: 20a78434dcc14ecf63300cdafa4281de5cf69d9791bdb174cf941d6592762ecc
    role: context
  - path: pages/traits/morphology/gas_vesicle.html
    sha256: bed734273c2a14f701cbe18ab11760f41d4429c83d728ff17e28cd8ab94f5ab4
    role: context
  - path: pages/traits/morphology/gliding.html
    sha256: be5e6a465c7aa0fa387bef1d9417e12033fbe337de246c9adcf58ed50fd44cd3
    role: context
  - path: pages/traits/morphology/gram_negative.html
    sha256: 9559c47dd89477dd4d6b0ffc022a4a2d5778df8bd57379bce16ba5ccbdf564ef
    role: context
  - path: pages/traits/morphology/gram_positive.html
    sha256: bf1ce71e59c9044607d0e0e93429ab65953bff7590dd976fcc1999929eaac3f2
    role: context
  - path: pages/traits/morphology/gram_stain.html
    sha256: 4d0efb3c67e3a3cea95f0abb38df255147d2435e528826c28a2eb314360b3132
    role: context
  - path: pages/traits/morphology/gram_variable.html
    sha256: 46834d2b8bb3ef8cf782c74f9346ef5080faedfb9ce0f5b64f2bcd59845aded1
    role: context
  - path: pages/traits/morphology/green_pigmented.html
    sha256: e32221dd0988c693e361c4caba67294a61678f8741fbaf3928aa39caf1b5215e
    role: context
  - path: pages/traits/morphology/helical_shaped.html
    sha256: aec470f9c942514528591895eef4e2e51b87866e1c964f36e40475e363cad104
    role: context
  - path: pages/traits/morphology/heterocyst.html
    sha256: e5901e69314a49f9e24f2ba91181bfd6a27d30c81a1476d29785f22d3624a8a6
    role: context
  - path: pages/traits/morphology/holdfast.html
    sha256: a71034a3ee3558c21251e0cf0a6116802f8ba9cf0bfcc26b078d6a4cef8361e3
    role: context
  - path: pages/traits/morphology/hormogonium_formation.html
    sha256: 95f443b098ff7748cd06bebcd1dcf4b581c151238f8af00813e07c0a596bb613
    role: context
  - path: pages/traits/morphology/intracellular_inclusion.html
    sha256: 09fa55097f4249a69e3aeffe52eb391fbac173722936f7852a9e4eba08294674
    role: context
  - path: pages/traits/morphology/irregular_shaped.html
    sha256: c032873fb16f05b507523ad8343de7bf2dca55887cda752db837855aae738114
    role: context
  - path: pages/traits/morphology/lateral_flagellation.html
    sha256: 4769784a3b0a1eb43e7c44393f6f8bf3e2db2ff22b5ad6741de3212e62c7a6ab
    role: context
  - path: pages/traits/morphology/lophotrichous.html
    sha256: 5ed85dc89e82e14c6c3386d761fda9e73252e3dc133931d0a8b03f4207efbba0
    role: context
  - path: pages/traits/morphology/magnetosome.html
    sha256: 2b2b92b3b42ced44c04bf4e6ad2f0b4965a7de34aadafac485bfa6569bebed17
    role: context
  - path: pages/traits/morphology/microbial_haustorium_formation.html
    sha256: 68fbd62c15125fa772383712854c886c4c8400f79801f002cac1285ddc1eee70
    role: context
  - path: pages/traits/morphology/monotrichous.html
    sha256: b71b11d9eea3056ee173e451f2553c0bcbead1d4df8bacdf9731c134812b65a0
    role: context
  - path: pages/traits/morphology/motile.html
    sha256: ca9f717d26a30ae7044ec5c3e1c586c30d34cfc7f254a5b4cd6338a70c52b7fb
    role: context
  - path: pages/traits/morphology/motility.html
    sha256: 0445bf7827e9b4d9721c5fc4bd1e6077d83828db5cc049cc8034a2c3b7a7aa74
    role: context
  - path: pages/traits/morphology/mycelial_growth.html
    sha256: 1bcadb167f669b1793c69a88e51190cbd63df286a8fd91cb1c868e624d98b079
    role: context
  - path: pages/traits/morphology/necridium_formation.html
    sha256: 922722eaa2ddad295102321b592eb77f96cf144130f0eb11a55e9f89a55df6b7
    role: context
  - path: pages/traits/morphology/non_motile.html
    sha256: db0ce3122001e6bb9f03e7e9c2eade310e3199363ab105c982a58f20a4ff5613
    role: context
  - path: pages/traits/morphology/non_spore_forming.html
    sha256: 14ea9690676bdd6e3cf9180c54cefe6de10138109194a74dc82dc0deca6953a2
    role: context
  - path: pages/traits/morphology/orange_pigmented.html
    sha256: 9e0c24042ecc70edeb1d3d313348751b8e7054853abece74662570c1a4b6a40a
    role: context
  - path: pages/traits/morphology/oval_shaped.html
    sha256: 1c9e0f3cfc8876a93087088af0ab5114c04d0f3a5c7510f0202a4edb348a6436
    role: context
  - path: pages/traits/morphology/ovoid_shaped.html
    sha256: 7bef5ee89eae47aeea3222db716a8152b014b19eac8c2aaa442d2cd2826ad340
    role: context
  - path: pages/traits/morphology/palmelloid_formation.html
    sha256: 86db155d4f0ef471905aca77b238196d8929ad8c47bedd2e048cb707bf4073c8
    role: context
  - path: pages/traits/morphology/peritrichous.html
    sha256: 4d7af6c2a877c8fe0d1a45c0215080095e6a30ca70e4caf90699524d532a71ab
    role: context
  - path: pages/traits/morphology/pigmentation.html
    sha256: 5f9301109862ba747ec3500467cb692b38c16116f695b04ba711d9fc02758a80
    role: context
  - path: pages/traits/morphology/pink_pigmented.html
    sha256: ad851d7f7e1ab64c4b2560c881eec7cce3f2fb3c64a0a7970fae73a2b36dabb0
    role: context
  - path: pages/traits/morphology/pleomorphic_shaped.html
    sha256: 5ca67ce7c5f4dc4e3ed3c7517d42d727338abd78537892727bd344ec78eff835
    role: context
  - path: pages/traits/morphology/polar_flagellation.html
    sha256: f7ba9a0e2e9a33925226500b6369140a6c00c36f7586aff4470867104e0174f7
    role: context
  - path: pages/traits/morphology/polyhydroxyalkanoate_granule.html
    sha256: 3c3ffc659284784752997f9a7acdad615dbb813d2512ad9bf2f5b680b1c15b72
    role: context
  - path: pages/traits/morphology/polyphosphate_granule.html
    sha256: 2c14c8360ec5a51cb7f825a0e8a393e27c8383831081b8be5e8bd7eafc9eee45
    role: context
  - path: pages/traits/morphology/polytrichous_flagellation.html
    sha256: 8bbf96f85e05e159ebabe813b1d5729710c27c24674bd0865a278937514d5fef
    role: context
  - path: pages/traits/morphology/prosthecate.html
    sha256: 8627db0d972d3b487ce8df4ec89bd16fe0817bb38d279a3e9c2bc06b6fd0e7c9
    role: context
  - path: pages/traits/morphology/pseudohyphal_growth.html
    sha256: 351324f73ad139ffe40300d67a215b9ba635b93b2c6cf2f0e9fcfce43921ad42
    role: context
  - path: pages/traits/morphology/red_pigmented.html
    sha256: dd8d8abd0dbb5974c5183c921408225445c0235458e8656b901343f969319855
    role: context
  - path: pages/traits/morphology/ring_shaped.html
    sha256: 30608a56634571dace168342ac10502ae193e1270291055a144df9cc765d06a9
    role: context
  - path: pages/traits/morphology/rod_shaped.html
    sha256: f649c36a1e3456a0a969cf148d205da12b8fea1b74ccd4797f31a74e5786dbf3
    role: context
  - path: pages/traits/morphology/rosette_cell_arrangement.html
    sha256: 9c545b978db95a8b935f6852bdabcb6f0d7c976e84afefa6cf9abb40e1cb05f1
    role: context
  - path: pages/traits/morphology/s_layer.html
    sha256: 90c58c1c3f2ce7cf8dacb3493b7cda880c7a700c3f8521654fd91bb11679a6cd
    role: context
  - path: pages/traits/morphology/sarcina_arrangement.html
    sha256: 75fcdd3049d4949c5bf0e0a345198226c9f4d8d095d8f0c4365f27b76c19a8b4
    role: context
  - path: pages/traits/morphology/sphere_shaped.html
    sha256: d61a712e2f27af707a7a0a9d015e385b754d2f7b3007bd03ef85b6288d2e4b9a
    role: context
  - path: pages/traits/morphology/spindle_shaped.html
    sha256: ba63785875010d226acad55bd69c1dbb3dd892d9ed8596140e64a457a478df80
    role: context
  - path: pages/traits/morphology/spiral_shaped.html
    sha256: c9624aa61aa2c1ea01ae0ceaeac3e729cb5d8a5393ec68ab94dc28f1d8a7bba4
    role: context
  - path: pages/traits/morphology/spirochete_shaped.html
    sha256: 3cc89b1e385fddd35b848645cd89cac9f905922746c3ba9e708723a5d4f37470
    role: context
  - path: pages/traits/morphology/spore_forming.html
    sha256: 5075d7a2a532bcbcbe9303d46e91e599f939b2f1c48e654814e0d1996aaee47e
    role: context
  - path: pages/traits/morphology/spore_shaped.html
    sha256: 04022e5fcbb2d317b1942c5ca0e1f0a709292469f51213f0e9aefec3fb204462
    role: context
  - path: pages/traits/morphology/sporulation.html
    sha256: 9fa680c3fb26edbaaa28370867918dc366ebc6abce8feb5188a9c6bcf9a39628
    role: context
  - path: pages/traits/morphology/square_shaped.html
    sha256: 1fe278cca188bc55600aacb687df808fba81c8b1db60455822a9b4274e54f992
    role: context
  - path: pages/traits/morphology/staphylococcus_arrangement.html
    sha256: 6661c7c490fe7786415c2bd10a78ee54629abb15448a20439af662112ae98b2e
    role: context
  - path: pages/traits/morphology/star_shaped.html
    sha256: cf3a9cf8e043e5962f5c183306028469e22b2f95fdd3c5715d7053a2c649f69f
    role: context
  - path: pages/traits/morphology/streptococcus_arrangement.html
    sha256: 4ea70f498ec24d0bb95b9cf3f554b3e6fc539c224cc1818bf39ec0cf3d4085a5
    role: context
  - path: pages/traits/morphology/subpolar_flagellation.html
    sha256: fb05ce9fa7d842c5b51b1f4b6fc9c51d4f5fba221e9541f7afd200e29818e078
    role: context
  - path: pages/traits/morphology/sulfur_globule.html
    sha256: ca806c1215347afdb80ddb5e946d33511fd4537a28319e27555315c3343f13e0
    role: context
  - path: pages/traits/morphology/swarming_motility.html
    sha256: 71677a4ea29703be440732d231a542b42622c263c6f0297d27133af971ecbbaf
    role: context
  - path: pages/traits/morphology/synnema_formation.html
    sha256: af0768a6bc6b0b9e0eea13213576053f8d9398b633fe5afe5c6547160d42933d
    role: context
  - path: pages/traits/morphology/tailed_shaped.html
    sha256: 8b0347e003bc0c41edc36ca39b5bbc928b6d88d12c2eae7eda628a3054437701
    role: context
  - path: pages/traits/morphology/tetrad_arrangement.html
    sha256: 270bc36c744467979017ab784f2f33c7d44a7edf5a20c54da3b0662d628e40b7
    role: context
  - path: pages/traits/morphology/triangular_shaped.html
    sha256: 854420bd74211986ee517e3e94177c2f0c19f7919f5ff927f3f079a91081e031
    role: context
  - path: pages/traits/morphology/twitching_motility.html
    sha256: 31d0966cbd2cdd3467ce77cda8bf3879784f339d11b06cb915f1d29a8fb8481e
    role: context
  - path: pages/traits/morphology/type_iv_pilus.html
    sha256: c4defce9ca830d1e34037754610d7e0c45deffb3a807015a11aaf4df855d8494
    role: context
  - path: pages/traits/morphology/vibrio_shaped.html
    sha256: 878b864de6f19853e6fd627065a979d02f3bfd53a3bd80017187adef6428020e
    role: context
  - path: pages/traits/morphology/white_pigmented.html
    sha256: 5679bc5591e34a4b697635b3f682f03fd395b340b886a19841dddad98aca2af2
    role: context
  - path: pages/traits/morphology/yellow_pigmented.html
    sha256: 375c0c7ce98edb4d7bcaaa016aa3243b71c778cb2e69027ee21ccf2234f34202
    role: context
  - path: pages/traits/observation/growth_nacl_observation.html
    sha256: cdc4a1ac79b7ce8e16013ece62ef9ca4341b4831f0acf7bddcb3d362b46b8122
    role: context
  - path: pages/traits/observation/growth_oxygen_observation.html
    sha256: 3d6b135638fb7088ed1bffd133a70291c4e94768e9ce3673ac10c480b4421ffb
    role: context
  - path: pages/traits/observation/growth_ph_observation.html
    sha256: ce9bdf591283cba5ce34d148e4b7ea7b3fcc0190039aaff1e2f66f758f8b9168
    role: context
  - path: pages/traits/observation/growth_temperature_observation.html
    sha256: 45390af9c740095c2870be465ddd87d1dbb5ac0a632c8e99e898ba6860eda142
    role: context
  - path: pages/traits/observation/nacl_delta_observation.html
    sha256: 4e57e96b9441c76b1e1920296f441b3187e0d5cdefd282b5d4475cf01a405801
    role: context
  - path: pages/traits/observation/nacl_observation.html
    sha256: 00578d2b09c4d015167ea95361d12113061fabde02de40cc70a30690f25ab103
    role: context
  - path: pages/traits/observation/nacl_range_observation.html
    sha256: 7c1c9e9f706f875e44f49a3553b547c69ec9549d5d5dca4960098047d09519f9
    role: context
  - path: pages/traits/observation/optimum_nacl_observation.html
    sha256: d5da62e76421b7aab9223b1d3d0eb41863a2b1863d0210621d652d86139f009a
    role: context
  - path: pages/traits/observation/optimum_oxygen_observation.html
    sha256: db2bb71ed48b7a1119941e8d6b0215db9e4634a581449d0afbdecc52df5cfda2
    role: context
  - path: pages/traits/observation/optimum_ph_observation.html
    sha256: c3cc195fc4c3f865828d8ec09b183cefe2ecd7fd08a3051cb037fa1c6a046e2d
    role: context
  - path: pages/traits/observation/optimum_temperature_observation.html
    sha256: 3a0a9d3ae979457141b1afa9b5c205c5171216efc92b059934090703ac59262f
    role: context
  - path: pages/traits/observation/oxygen_delta_observation.html
    sha256: 3bd1d38b3f4379df2efa220df19c1ae4a01462ee568bd0e407ef7fa06974db9d
    role: context
  - path: pages/traits/observation/oxygen_observation.html
    sha256: 9a1b0863d23d2f88f6d18c92b58073956402c5cbb8fd130f2bb93cfb734e31af
    role: context
  - path: pages/traits/observation/oxygen_range_observation.html
    sha256: 26c490eb3dd9d27db9105dd04f84656b1d5b38f3b5d3b96f49859b2ffd8e8fab
    role: context
  - path: pages/traits/observation/ph_delta_observation.html
    sha256: 27c5c98d3c491b4240248276af334f0c22552e1b2db75db4b83cb5aedd09f60e
    role: context
  - path: pages/traits/observation/ph_observation.html
    sha256: 317a5d386f2e894a328fee8fc97ec37611b5821d8dbb11fb08347807742576b6
    role: context
  - path: pages/traits/observation/ph_range_observation.html
    sha256: 9be6dcaa80ba28be343efb9e0847dc84dde854186893f3e7d6886a074c342260
    role: context
  - path: pages/traits/observation/temperature_delta_observation.html
    sha256: 4de08aad2ce02d58de1adcdf05b73efca7989b1aeff3e7623847afc9c3d0854a
    role: context
  - path: pages/traits/observation/temperature_observation.html
    sha256: 8b2a51990d69574f5b2c861b6cb90295b1eaedc1c42ef47700136cc171267416
    role: context
  - path: pages/traits/observation/temperature_range_observation.html
    sha256: 565b91f9a330f00ffcc822ef57e274c700c3d3af5ce2614ad5f06f09fe4da3ef
    role: context
  - path: pages/traits/other/catalase_negative.html
    sha256: 22a5292775b12ce36e2d1fc96673f5c8e03da3a394e5d2337bd0d83f6e96a7ea
    role: context
  - path: pages/traits/other/catalase_test.html
    sha256: 2152ed321d9fd94bfca495990184315d792afdf6565347459f00b9051db5fbcc
    role: context
  - path: pages/traits/other/circular_colony.html
    sha256: 3c70123ac61c5cc7420a6a2597ff0f63679fa84112edebfa3497edfff0121fb6
    role: context
  - path: pages/traits/other/coagulase_negative.html
    sha256: 4f3d7bcb6d41029fce0eadf032a03afcdfaeee91115bc33bf1d52c450f34baa8
    role: context
  - path: pages/traits/other/coagulase_positive.html
    sha256: 285a2e5a560e587fbbe4fd426d6cbd95a6f0fd63a3aafba8ff55bbcbb0629268
    role: context
  - path: pages/traits/other/colony_morphology.html
    sha256: c71447a3c22eff6f1350d809186c9a3b5e538d111130b34132347f5ff64e9e4d
    role: context
  - path: pages/traits/other/colony_shape.html
    sha256: 58b5b3cbf907cd4b642d5709a4759e32982cb3812fb67770dc2b13e5608146e8
    role: context
  - path: pages/traits/other/epibiont_phenotype.html
    sha256: 9b0f1e03817c4de81998071005ef326f475f008bdff98c65b609a615658f5f76
    role: context
  - path: pages/traits/other/filamentous_colony.html
    sha256: ba1fbdcb52eb610088baa58f130c72fa96a459b7ece071f20108a197cccc7ac4
    role: context
  - path: pages/traits/other/fried_egg_shaped_colony.html
    sha256: d6b09da6f1212b2cd5acf79a0efefcf8528adf21502540be1922127a5f5da9b4
    role: context
  - path: pages/traits/other/generalist.html
    sha256: 7e370b26cb289fd2ac39f7cfd5e29224d998cc9d0f824fade7c28803ca1c6b8a
    role: context
  - path: pages/traits/other/hemolysis.html
    sha256: 76f10d42594efb4255cab39c4c50cedf6ffca4801da78e695b26439a0758a8f7
    role: context
  - path: pages/traits/other/hemolytic.html
    sha256: 05c35664c1331ff4431b4c4363044aa1ce4a137ec6131f53d0e6025099a8f040
    role: context
  - path: pages/traits/other/indole_test.html
    sha256: 4df9473f63d24750d6a29025d6b397b532089096516f7370ab8561a1b603284e
    role: context
  - path: pages/traits/other/indole_test_negative.html
    sha256: d0275b3bf3cab20724fa248f91e14f57cb39f28697283ffe0181a4ae603a2702
    role: context
  - path: pages/traits/other/indole_test_positive.html
    sha256: 9c06c479b1a16f4ddbccab2d4014700dd169c80ef316ef1a113ef4015d950892
    role: context
  - path: pages/traits/other/irregular_colony.html
    sha256: 8e93556d84589b2d1da8672437de7624d4cc52fc27cd06542b3d00f15308f790
    role: context
  - path: pages/traits/other/methyl_red_test.html
    sha256: 7522a548396d106265483a9e5a49e43ef196d37eee97a2304f06325fe2b762b7
    role: context
  - path: pages/traits/other/methyl_red_test_negative.html
    sha256: 49e2aeb0fc165c476b7ae41b73cc377554aaa129941ba2280a6dab0721787e53
    role: context
  - path: pages/traits/other/methyl_red_test_positive.html
    sha256: 3bd5068a93faf4a2c3a09011dac48babc81ff8e2dccaffcf1ff217522d08aa60
    role: context
  - path: pages/traits/other/non_hemolytic.html
    sha256: 4e7b55a1daf7ea81b209e4f6fadaf3eaa85dd686956aeabf74eee1449e826875
    role: context
  - path: pages/traits/other/osmotic_tolerance.html
    sha256: 98e24dab7bbad82bc10d70223c6c77ce2c9c0c86aab3a1cb5cfdb3c7ab4a8f80
    role: context
  - path: pages/traits/other/oxidase_negative.html
    sha256: 3b1c7ea8095d8febee2e6f100c0b614459c9264744a230049c7f534ed172c5d1
    role: context
  - path: pages/traits/other/oxidase_test.html
    sha256: 1077a9ca2b9f968dcb6347a0da1a4432423f9b69381685050de8eecc86d92980
    role: context
  - path: pages/traits/other/punctiform_colony.html
    sha256: 0e7b07bca53b1ad91c01799506e3bc21ba2f9393507ca9f60e4cf2ad6b394749
    role: context
  - path: pages/traits/other/rhizoid_colony.html
    sha256: 0507ffc8767a50406bf0388da25b31ea2b49a2002b8ca6d3608f773c3bc4817d
    role: context
  - path: pages/traits/other/specialist.html
    sha256: 1d8fbd30a576269e166e46b5d8ad1d21c82fd0c73d5309ea3318fccbe4ab246b
    role: context
  - path: pages/traits/other/urease_negative.html
    sha256: 6caa8b4dd26c86c3358957c3586e8441c8d90b9323cedce77e1046e2d90320db
    role: context
  - path: pages/traits/other/urease_test.html
    sha256: a8eec0a947f0a573a13d94cc7e18648956c06f25821d3f6c32b1534e4cc27d72
    role: context
  - path: pages/traits/other/voges_proskauer_test.html
    sha256: 204c505911ba1cfc136bd5e0ec0bf09fac7519ae6679f5888dfcc8ae86229a60
    role: context
  - path: pages/traits/other/voges_proskauer_test_negative.html
    sha256: 8ee65c107a78d0d4822376f23ececc360350918625a2469511272517d0df7ad9
    role: context
  - path: pages/traits/other/voges_proskauer_test_positive.html
    sha256: 7eee8709396656a933613c55888a3496b42e898cac020e61f3ee03b104d574cd
    role: context
  - path: pages/traits/physiology/acid_phosphatase_activity.html
    sha256: b4a7bd6aa29f4551a840379f0fc7c5e731a2847e8a28af543abe1394908f4e71
    role: context
  - path: pages/traits/physiology/aerobic_anoxygenic_phototrophy.html
    sha256: b7bd91dca32897fd8d8fdfa8785928f29a0305d1e8a6bd3e4dd232a5a9a52935
    role: context
  - path: pages/traits/physiology/aerotaxis.html
    sha256: 766a823beba4111aee3f2893ed210e4e40f6b7df4c5146e44ca2b1c55f8671e6
    role: context
  - path: pages/traits/physiology/aerotropism.html
    sha256: 7a5ce0263c1f8d299f7033cbd35404513bdb907e168c81bf6df60dc6828f6ae4
    role: context
  - path: pages/traits/physiology/aggrephagy.html
    sha256: fadc245795f7856643df9c3e7492c04ceb26a2b2900c16e21e61dc440814a456
    role: context
  - path: pages/traits/physiology/alanine_arylamidase_activity.html
    sha256: 74c5f709013589facf32847bde207a3e6b6a4ed58b351386413a4153ac8056a3
    role: context
  - path: pages/traits/physiology/alkaline_phosphatase_activity.html
    sha256: 966c887a63f1e6574f45f599e5346c79f0968e660640462ae32c34eeca360516
    role: context
  - path: pages/traits/physiology/alpha_chymotrypsin_activity.html
    sha256: 642a4be287bc7241bb498543433d35a801fe28ccf78ef9ff9db4617c56c21294
    role: context
  - path: pages/traits/physiology/alpha_fucosidase_activity.html
    sha256: a1c6bbbee876f9e142cc457b354af231658cdfff1cebfcbfa4a0e2dea516bfd8
    role: context
  - path: pages/traits/physiology/alpha_galactosidase_activity.html
    sha256: 3645085ea5b681ead6a0b0317a8a5e0e82f59babda6cb7f9465be9d1b9d6ba05
    role: context
  - path: pages/traits/physiology/alpha_glucosidase_activity.html
    sha256: 2ed113d0d1c840afa80b5b58a035ec44baa2da071574c9e9e1b6f9152e9ff9c1
    role: context
  - path: pages/traits/physiology/alpha_mannosidase_activity.html
    sha256: ee63ccc4b559ad72c6a1599996848c2777d26db2fa445df3b19c1b19f106a847
    role: context
  - path: pages/traits/physiology/amylase_activity.html
    sha256: 9ea4a7202b81bb2f3a411a45304439dd79023158c14888d32c14b348774765b1
    role: context
  - path: pages/traits/physiology/anisogamy.html
    sha256: 5dce6b55a08c898610f9f1b10f3b190a1b116bd064e1dd3e4b046ffc3daab945
    role: context
  - path: pages/traits/physiology/antibiotic_resistance.html
    sha256: ee47e858f2103db5f68e4f5badef8dabf5e64d3ad2d3170e40928a2d35498d72
    role: context
  - path: pages/traits/physiology/arginine_arylamidase_activity.html
    sha256: fa19bf1cb51462941fd5f11c0c4aa8434e46fc640ce588546d434984b269f7b3
    role: context
  - path: pages/traits/physiology/arginine_dihydrolase_activity.html
    sha256: 352e54b4b415cbc97f7f039f168b14d5ae36d29f470137c18046b52ed69cfee0
    role: context
  - path: pages/traits/physiology/autogamy.html
    sha256: f800898b1af05bc0ea6db224127ba701beabbede21bfdd3a34401736b4bcd10a
    role: context
  - path: pages/traits/physiology/automixis.html
    sha256: 77089a066c172921f524b89f64e3b5d182b221ee60c861f4950f5be50f98be15
    role: context
  - path: pages/traits/physiology/autophagic_glycogen_degradation.html
    sha256: a2cea1864463c25428df62e8d330aab48614ff8eb62fc0444e0ece1e6fc50f36
    role: context
  - path: pages/traits/physiology/autophagy.html
    sha256: e112eeabb2b562e523516bacca966efdd066dfdd4409b901d5d2dbf9130bed40
    role: context
  - path: pages/traits/physiology/autotrophic.html
    sha256: ea27a770adba2498d882618b3cf5a13bebd9fac182c567b414c9bd703363f365
    role: context
  - path: pages/traits/physiology/bacteriocin_production.html
    sha256: 2e5d031de3467d79cc98fb9550261f69969c0ff538805a25ad9f483c58638caa
    role: context
  - path: pages/traits/physiology/ballistospore_discharge.html
    sha256: 72e3d99f0e9844635f87fa27b09b08919662702fab3f1225531a3986bb679e8f
    role: context
  - path: pages/traits/physiology/beta_galactosidase_activity.html
    sha256: c7b6c055d5592f885f70e63fe03a9cd6e8c043871ed4b58973e513534e5f4e42
    role: context
  - path: pages/traits/physiology/beta_glucosidase_activity.html
    sha256: e27a7045de2a68b9f74c0efc90b3c14a148b2ef20837c0c63e3eff6d3dcb2d54
    role: context
  - path: pages/traits/physiology/beta_glucuronidase_activity.html
    sha256: 41e70ed3c39120cc065bc7f16c07920d83242158ec552810518e7581c3fbfb90
    role: context
  - path: pages/traits/physiology/beta_n_acetylhexosaminidase_activity.html
    sha256: a657a8c6195377879f17205a11e7b81dbe9bfd2f3ec4830f53b5c200cfe9f318
    role: context
  - path: pages/traits/physiology/bioluminescence.html
    sha256: 92668c94f9f4fb40bc288a321c70d8f999a496250d880a501cb3004ad7fa62f1
    role: context
  - path: pages/traits/physiology/biomineralization.html
    sha256: f4e23fd6a21a5a67dfc8c85550a0b53d7c8ac6616957b70e6fc76bb86ed76e34
    role: context
  - path: pages/traits/physiology/bipolar_mating_system.html
    sha256: 4c33bfd5609ab5e864f66ceafc38cde3656dde9618c19837b9ad08578d99269c
    role: context
  - path: pages/traits/physiology/carboxydotrophic.html
    sha256: 0c362729f7707cc4e402b235414d9d0bb29ec045515807c9f8fcf4d076d9a4d0
    role: context
  - path: pages/traits/physiology/carboxylesterase_activity.html
    sha256: 9b76611f88808b65877b014cecbeba509c4a8859340ed67bb5b589c6d338a313
    role: context
  - path: pages/traits/physiology/caseinase_activity.html
    sha256: 28520b28f3bf1e24ac4c282a7ba1610b6d6a041e3d48bcc78e70169564e0d294
    role: context
  - path: pages/traits/physiology/catalase_activity.html
    sha256: dae33edd04d98361e1f94dd8638a1b1efd39da86e92b554cc72f548eb7db32f8
    role: context
  - path: pages/traits/physiology/cellular_buoyancy.html
    sha256: 5089d1bcc3188584103d02c10120659b05945fa02902a7db004a2750d6cc043a
    role: context
  - path: pages/traits/physiology/chemoautolithotrophic.html
    sha256: 879d9055bfd050f6d50aef24863665b3cb21e1033e0f4e84ca2d91f2fb755e90
    role: context
  - path: pages/traits/physiology/chemoautotrophic.html
    sha256: bf3f9f67536e96dac127c8b5892efbe72a627cc805a2aa35d55cd00f2ab7df58
    role: context
  - path: pages/traits/physiology/chemoheterotrophic.html
    sha256: c80b524998758cbfc962d3b7da80df436ad691209116fa2818663ee6be1fd6d5
    role: context
  - path: pages/traits/physiology/chemokinesis.html
    sha256: ceda19a6dc01995d705e40425ad5f671c6b449543d7c75fadd00117ddc737c64
    role: context
  - path: pages/traits/physiology/chemolithoautotrophic.html
    sha256: 69088309d91c1c365d98fd137e2847fbc086abef52b5edebd21684f414043001
    role: context
  - path: pages/traits/physiology/chemolithoheterotrophic.html
    sha256: 1b54a72d39a106a39bddcb75fbd1df5a71cf5347a0db17991aec6da4d6b55c40
    role: context
  - path: pages/traits/physiology/chemolithotrophic.html
    sha256: 27c25040d26d9259375b18d84656e90c6b37bdf3dffe0073d53aea8d80ba19b8
    role: context
  - path: pages/traits/physiology/chemoorganoheterotrophic.html
    sha256: f0b9b62725c40f73597dd69960537d1ad377ae16cca12e90d63b560ba4886525
    role: context
  - path: pages/traits/physiology/chemoorganotrophic.html
    sha256: adbaf60c8932ac9d15e1c30fb8d1b2c68949cc8f5e7f3b952db55e8a7f4aa722
    role: context
  - path: pages/traits/physiology/chemotaxis.html
    sha256: e58c30bf996e6cc3a4c4971073374e2013b6f0f111b948998ef38ae641b17652
    role: context
  - path: pages/traits/physiology/chemotrophic.html
    sha256: bc934db8965c3338efbfb3ed8b7f3a70afa4a24ae20bf4fb2482205c7cd71542
    role: context
  - path: pages/traits/physiology/chemotropism.html
    sha256: f4245dd71858cac893bcac8cc019d0770c460c63bc91ccfbbb054ec5a39d3816
    role: context
  - path: pages/traits/physiology/coagulase_activity.html
    sha256: 17c845505673dea1ce0bf8ea645e9ac261d9a6b246b60acb70567bea99fcf233
    role: context
  - path: pages/traits/physiology/coccolith_production.html
    sha256: 150de0cd622909d5e6751649c88d2fcbb853c1d2ab25c59db681b15db8fbe830
    role: context
  - path: pages/traits/physiology/cold_shock_response.html
    sha256: 2d0cee8e37ed949f463e465acbfd66e935055fb4af5bdc93e0e1b1f406086de9
    role: context
  - path: pages/traits/physiology/contact_dependent_outer_membrane_exchange.html
    sha256: 9a6ab1e1a866b1b350badaba4440603f94e81b25877bc9c9bf8fbc58ca854571
    role: context
  - path: pages/traits/physiology/copiotrophic.html
    sha256: 054a29ecf955bda00e5fa8e0d9650f8a84d0879b655fa90663000faac93a71d4
    role: context
  - path: pages/traits/physiology/cystine_arylamidase_activity.html
    sha256: 3709923b84417266643c52551caab4dde0222396be949f28039d1d4fe96f93b1
    role: context
  - path: pages/traits/physiology/cytogamy.html
    sha256: d3c9b612bab91b71a6786afc41316d11de06ccedf8faae18c13750ebd439c7ea
    role: context
  - path: pages/traits/physiology/diatom_frustule_production.html
    sha256: 2ab065f4a8f9bd7829bbf4be8a0f98d2feef66d8ae2268bfa018d6cbbf99f9a0
    role: context
  - path: pages/traits/physiology/diatom_perizonium_production.html
    sha256: f0347e5efd1c632bf2eb75aa07ec8ca378ed44edc3d9944188c6e8db77440b2e
    role: context
  - path: pages/traits/physiology/diatom_seta_production.html
    sha256: 9807b81cb6d70eb5ebc09d8e311954b102378ac237f09c39593d40ce78d2c81a
    role: context
  - path: pages/traits/physiology/dnase_activity.html
    sha256: 5f0c2fa1ae362231883af79419d88fe727ecbbdb01e0a9478ce006dff47fe764
    role: context
  - path: pages/traits/physiology/dormancy.html
    sha256: e8e1529bb672c5548c99aa70dd7c461b2770a235dfdf91ba485b1b5fc71ee0ef
    role: context
  - path: pages/traits/physiology/durotaxis.html
    sha256: 37f6ed6994f62f69e7eb3947d7160bbcbec9a0872b7dd0e5dde5e2c5a05acc02
    role: context
  - path: pages/traits/physiology/endocytosis.html
    sha256: 6a84131ab458892d6aa654010eb6f4804ecae299fb8a9c4de49c9c899522e285
    role: context
  - path: pages/traits/physiology/energy_taxis.html
    sha256: b60b4e935173fb5f669d61fc9a2ba327aa5a31080de79261f2b3c74909d41d1a
    role: context
  - path: pages/traits/physiology/er_phagy.html
    sha256: 449bddb9ab40a043c6b4c4a38987ce44b97b9c3563091b479877196bb6525ec3
    role: context
  - path: pages/traits/physiology/exocytosis.html
    sha256: 6f0b97fd2246a2fe747997ecc885606a42da0873aa2ee2b3bce1a754e2091d54
    role: context
  - path: pages/traits/physiology/extracellular_membrane_vesicle_production.html
    sha256: 05021d25258708bb6bef87ee3ea06909cd7ecb4599e6b34f5af19197b9055916
    role: context
  - path: pages/traits/physiology/galvanotaxis.html
    sha256: f8fc0d35a4b5cf22c266b9a3aa81d12b86717b4466d9bebff865eafd46f079b5
    role: context
  - path: pages/traits/physiology/galvanotropism.html
    sha256: 8f460198002c2f2bdf2982597a5426ca62e6dcc39c38368e091bf748222edbf7
    role: context
  - path: pages/traits/physiology/gamma_glutamyltransferase_activity.html
    sha256: e69c62caf3526f20cb5ccbd99e3a910cd9b29bc46473d89664d5e451260654dd
    role: context
  - path: pages/traits/physiology/gelatinase_activity.html
    sha256: 32e04622f3a0c5e86ce19a32dcd45a0ee7d80a7ffa40c639a40807d8bc1fe23c
    role: context
  - path: pages/traits/physiology/glutamyl_glutamic_acid_arylamidase_activity.html
    sha256: 4a29781ffd68292c2b26e5980ca7cb45996b0c57647edb63d4772c7b34fb8d50
    role: context
  - path: pages/traits/physiology/glycine_arylamidase_activity.html
    sha256: 764c5b7c68dc4514f4b443422831b1443c41ccc7a37e47415695586df52542e9
    role: context
  - path: pages/traits/physiology/gravikinesis.html
    sha256: 69845c1ddaea170881da9150ac1b6436793a1c8e9a92b5f7fdd2a9b78c5dacb0
    role: context
  - path: pages/traits/physiology/gravitaxis.html
    sha256: bbe2b7bd886544795d5d666024ffa95f3a01c8340c007e28ccac0ded0e6d66cc
    role: context
  - path: pages/traits/physiology/gravitropism.html
    sha256: e6d430028e81a1842af1076178faaceb4a3686ac3c2ed014e0ee27fde2291731
    role: context
  - path: pages/traits/physiology/gyrotaxis.html
    sha256: a16df9c510a6bead8d21537ef9c9e44d44d82d6d1f701b769946c00ba282308e
    role: context
  - path: pages/traits/physiology/haptocyst_discharge.html
    sha256: 2457c38a7d91220a6e8833758eb3c09187ba26f2713ec235df006e3dad8bc2e7
    role: context
  - path: pages/traits/physiology/heat_shock_response.html
    sha256: 508cce12e672baf7db707a263b6c92265b3ae7e260449a450b1a0e2d33d18b79
    role: context
  - path: pages/traits/physiology/heterokaryon_incompatibility.html
    sha256: f36d7e63161e9916856ff8139c0012705e8de06086fe2efe5fe3acb086fe0d71
    role: context
  - path: pages/traits/physiology/heterothallism.html
    sha256: 8199eb6e00e4926438b14ec59363630ed2777f21ed2b10f171d8913cf66e62aa
    role: context
  - path: pages/traits/physiology/heterotrophic.html
    sha256: 43c47727c73bacd81dd744de68a6edae8f9805f3965355b7c9631dd727236ffe
    role: context
  - path: pages/traits/physiology/histidine_arylamidase_activity.html
    sha256: e8bb492b9fb133215bb67a480769ce535ecb700bc34b8a3d51c2f8f47db3e947
    role: context
  - path: pages/traits/physiology/homeoviscous_adaptation.html
    sha256: a1caca8e3351dd04fcd2c1947b0602c8e75b03ddfe3112304befd1adadec7646
    role: context
  - path: pages/traits/physiology/homothallism.html
    sha256: ca02490667d2afb76e5a0828a03201aec63f6ca2446db263db51d902cfd067e6
    role: context
  - path: pages/traits/physiology/hydrogenotrophic.html
    sha256: c5293576b4b0e42d97455ef6ee37a0c1a2ed4c47c8bf556510793fe0be35163f
    role: context
  - path: pages/traits/physiology/hyphal_anastomosis.html
    sha256: 7c1b92d619940616c3a4e769d0cff021e9b93b6b2b599b2970db4fb97942362f
    role: context
  - path: pages/traits/physiology/isogamy.html
    sha256: 5df26c034241ee7e7c8074fa9328a14517ab1910524665d617c23f994d461ace
    role: context
  - path: pages/traits/physiology/karyoklepty.html
    sha256: 88d2aac4160466906df51f0211efce242ee2ba994b1d42b63c35040fc011b908
    role: context
  - path: pages/traits/physiology/kinetocyst_discharge.html
    sha256: b4ced2cbabb26db56d2c8adb478b56c45dc16a1fa3661d2129eb3fe54525a2ef
    role: context
  - path: pages/traits/physiology/kleptoplasty.html
    sha256: d9567abe3b4e07f4b5ee0376bd43df8741f1cecea9ffa0ac60ae968f8dfbaf35
    role: context
  - path: pages/traits/physiology/lecithinase_activity.html
    sha256: 7c2f5afb1c45920a44710b389c1a131b3dc6f74b530290271b8c219da66589c6
    role: context
  - path: pages/traits/physiology/leucine_arylamidase_activity.html
    sha256: aef05d7ba27cf977160c7201a23f07eea3e1bd95124ddfd538feb9093846980c
    role: context
  - path: pages/traits/physiology/leucyl_glycine_arylamidase_activity.html
    sha256: 36a3f7d5034b0cf1fe541693b4db0f36813e7f75c52e6760346be7bc3143b9fb
    role: context
  - path: pages/traits/physiology/lipase_activity.html
    sha256: d4da5595f884662def6961278787cb422ec85337bb580f3bdd398ceaf0cf652b
    role: context
  - path: pages/traits/physiology/lipophagy.html
    sha256: 646c6ef16b90ceaa48ecd7413aa2ff2fa59bd2672fa5fc215ee5f741dacfa685
    role: context
  - path: pages/traits/physiology/lithoautotrophic.html
    sha256: 1e2edacc46b8d6fd1fc218caea9ffe9659dfd5b8766fe9e3956549b18f4ddc9b
    role: context
  - path: pages/traits/physiology/lithoheterotrophic.html
    sha256: 69cfb8c1c0c6fa7a134dc6a0978c46af7fff74f6f698a58133dc6d921aaf4564
    role: context
  - path: pages/traits/physiology/lithotrophic.html
    sha256: 23fdba0e79f8d9ff3af51378cf3e07220283af8c9b71f76b77cbd2a1d20644a7
    role: context
  - path: pages/traits/physiology/lysine_decarboxylase_activity.html
    sha256: 7b80ad61ecaae04f564d0d56bc6e10d81d012b4284f523ae29cce4dd984558b4
    role: context
  - path: pages/traits/physiology/macropinocytosis.html
    sha256: 71b844d99899fdb0f1d208c63cc0ea829db08f9c510edc6182973698da7c069d
    role: context
  - path: pages/traits/physiology/magnetotaxis.html
    sha256: d50b3ce7f4ac2677d89feec19cf9a87a030893872a95c149372a30b6e671fa36
    role: context
  - path: pages/traits/physiology/mating_type_switching.html
    sha256: bca19614cf511b5ccfacab6164738f03b69f77dff0d0be0bf647d9f6b77addd4
    role: context
  - path: pages/traits/physiology/methanotrophic.html
    sha256: 77ae9285cd49565938cc718db1190ce96b6bdb6638fae1787abe40310f4ee4ba
    role: context
  - path: pages/traits/physiology/methylotrophic.html
    sha256: 3d8dafe1ed8f98e339a560d519a91a8d1aba209d4673210fdacab80eca88d5f0
    role: context
  - path: pages/traits/physiology/mitophagy.html
    sha256: 3b107ad94b6da41163fa902bfd94140cc102f5c73280d15960970d8b9da17b33
    role: context
  - path: pages/traits/physiology/mixotrophic.html
    sha256: 4c65053af92f3ca3812222bcb63693e3bba3d654a11dec324e7637a4501fd96b
    role: context
  - path: pages/traits/physiology/mucocyst_discharge.html
    sha256: 7bf4cb1fbc99038b6589b0b65dff26191e6601a7294eb3122c4322f85d35ab15
    role: context
  - path: pages/traits/physiology/myzocytosis.html
    sha256: d3007c613045c3a7d1d74c49edac624b4ffa765b119efa7daadbc568c347b771
    role: context
  - path: pages/traits/physiology/nad_dependent_alcohol_dehydrogenase_activity.html
    sha256: 7ee3db0de7a340a0f47d5391bf49107f77f538665155e108bbcd3a6732de355d
    role: context
  - path: pages/traits/physiology/naphthol_as_bi_phosphohydrolase_activity.html
    sha256: ce4125115717e955b9c4b79b3cfad184c4e14ce9de8db1948b0ebc677a2df111
    role: context
  - path: pages/traits/physiology/natural_competence.html
    sha256: eeed45cc1412947f87ef66471170e6fe9be401a96dc65dafe61eebe68900decc
    role: context
  - path: pages/traits/physiology/negative_autotropism.html
    sha256: baaf19b574cf8154d84901c7da75a85a7141b2d72ce52ad0f66ab61d089d4b31
    role: context
  - path: pages/traits/physiology/nucleophagy.html
    sha256: 98d0ddfedf54f51451af334417ec5a26e759b37c157b3d5f151899234ae18c0d
    role: context
  - path: pages/traits/physiology/nutrient_adaptation.html
    sha256: d1e5998ae996561cef42d50356379fa64f82db8c7ff08fb7de2e10b9622276ee
    role: context
  - path: pages/traits/physiology/oligotrophic.html
    sha256: 3aba6726a93f983b558b8757087cd498545e4a5e0d9fc6c1bc3b17cf6af7f83a
    role: context
  - path: pages/traits/physiology/oogamy.html
    sha256: bfb4b25b476ddb75c285a3dc9a79d0f0cf4e85a0454bf69df1a6d3289c447711
    role: context
  - path: pages/traits/physiology/organoheterotrophic.html
    sha256: d45c98d938c8634545454713d0855d4590491447f944c5c42f1330ac78981e3a
    role: context
  - path: pages/traits/physiology/organotrophic.html
    sha256: 695dea9b084c8b0fb034aead865e523d274984991ee62a0eda5c5e215fae156c
    role: context
  - path: pages/traits/physiology/ornithine_decarboxylase_activity.html
    sha256: bfd788f54e3b96a0075c30a71fd30a657c30e30954f062922e25000604c3d9bb
    role: context
  - path: pages/traits/physiology/osmotaxis.html
    sha256: e062533bb7a115a05087b88b6be4aecb4929f707a31e99d82934d1ba38f3c152
    role: context
  - path: pages/traits/physiology/oxidase_activity.html
    sha256: 503ce3dc954c305172e71ea027c5b32a1e7f3f7b55edcd1262bbec3e7e3f65f4
    role: context
  - path: pages/traits/physiology/oxidative_stress_response.html
    sha256: bc203138a76df21698dc0d93469286dbbdf30b72c35b8371076ced372eee7a03
    role: context
  - path: pages/traits/physiology/paedogamy.html
    sha256: b409e44cce6f8df711a4f2f8e549dae027c9e5bdac0edf83a4ebf619726e94c5
    role: context
  - path: pages/traits/physiology/pallium_feeding.html
    sha256: 5f3efcbe20073da863d2e310d3d351033cb4b99a06dd872117e8de58dabce13b
    role: context
  - path: pages/traits/physiology/parasexuality.html
    sha256: 7fedcb75d499cee91133b4ee35a2e6d67ebb86df8edf1835d267bc1f926e545b
    role: context
  - path: pages/traits/physiology/persister_cell_formation.html
    sha256: 120d0580b0812afd24fdd7f9c05dfb6ad81d8cad651a594fd5f31e0ee548529a
    role: context
  - path: pages/traits/physiology/pexophagy.html
    sha256: cd6855ebe67f0a08b25b06561c708b85ec4f82a40221131d4c687a98c0d0f5f3
    role: context
  - path: pages/traits/physiology/ph_taxis.html
    sha256: 001713f5c3bf78b690883ff70c3eb9ab30576e509d78ba1dd0cd8bcd28e6a588
    role: context
  - path: pages/traits/physiology/ph_tropism.html
    sha256: 2e553a668260fca84545e2ce46804e05d537de77ce02e7178951be7e832d0dfe
    role: context
  - path: pages/traits/physiology/phagocytosis.html
    sha256: b8958d9fb637e0c75c150654ad1c14b6f34fc0733c8ba30935903f62c415f7c3
    role: context
  - path: pages/traits/physiology/phagotrophy.html
    sha256: 94c1de95d0c428fe420ce12226e0a486d667c75019c6e79e014dc072e1604e5c
    role: context
  - path: pages/traits/physiology/phenylalanine_arylamidase_activity.html
    sha256: c36f035a171f4cdea41b0ca93cbe9cb8bab4aef300a4f2f7167781c4a2fa6d8c
    role: context
  - path: pages/traits/physiology/photoautotrophic.html
    sha256: 0bbf0ce4a1750464c0a675f96a7068b2d3d0e8a08c26c1cd264c608c47a2ad6f
    role: context
  - path: pages/traits/physiology/photoheterotrophic.html
    sha256: 79f244634e3c6c88a37f7ac812d716673cd0b9b9dfeac01529bac0c1228f38d9
    role: context
  - path: pages/traits/physiology/photokinesis.html
    sha256: 56c5b6605940e35d11b99c46c1427e9ba1881e5527547dea1a2f79f52a223f37
    role: context
  - path: pages/traits/physiology/photolithoautotrophic.html
    sha256: a6f688974f6d053f4f5b6d99cb2bd174a41fd85a2a629a5c40081c30424da46f
    role: context
  - path: pages/traits/physiology/photolithotrophic.html
    sha256: ca2181bab4ff37a978e6479af899e28e7e3f28525c23ec825da994f1b9034aa9
    role: context
  - path: pages/traits/physiology/photoorganoheterotrophic.html
    sha256: 114e1962a7a187f2027c8f8d5e933bd56b0db8f00534f3b03cafc424688cd021
    role: context
  - path: pages/traits/physiology/phototaxis.html
    sha256: ef099c847a0201f35fa7263c47924a5bcf0a6d31e12c9a75a6c980e617fc6bdb
    role: context
  - path: pages/traits/physiology/phototrophic.html
    sha256: 581e4245cc1cc5f93bbd78be4426eae9ff9e40c63a8feeea3c444a17d98b87c9
    role: context
  - path: pages/traits/physiology/phototropism.html
    sha256: 28a1a0c91434400e2200fdb9af1e2cbff52b59bb6dce0759c9691c8c718d499e
    role: context
  - path: pages/traits/physiology/pinocytosis.html
    sha256: 29c7eef67e7bb5f70143f145b5ce75e8789362dcb6b4f38d271d70c19d8758b3
    role: context
  - path: pages/traits/physiology/positive_autotropism.html
    sha256: 1b609995ea56dd2b927aed1b99aae8364ebefdbd279eddcaa25129e4bec1bd22
    role: context
  - path: pages/traits/physiology/primary_homothallism.html
    sha256: d5b23450d9cb353b8142e9525375a167139601975b38354884dd75e8d7b14800
    role: context
  - path: pages/traits/physiology/prolyl_aminopeptidase_activity.html
    sha256: 285c45aabe70f0eee8f79d9222c26360dfcb51a5a5ca17c9f891d387c06af3fb
    role: context
  - path: pages/traits/physiology/proteaphagy.html
    sha256: 8a2f920eb56f3b53a12a69b9a795b2a5cd8d74268d6b0efc3fe9b2c8d1d9d724
    role: context
  - path: pages/traits/physiology/pseudobipolar_mating_system.html
    sha256: 70111367409e84fbb10509c61b7b893831077f3667542fd3467ceca46d955408
    role: context
  - path: pages/traits/physiology/pseudohomothallism.html
    sha256: afadb0a84f9106254b4b50d5114c05d0f91dfdbc963e76c564866eedd2963b8e
    role: context
  - path: pages/traits/physiology/pyrazinamidase_activity.html
    sha256: 141f4e72bc4fc9ef472e841ae87bf9cb88a3c007e9660ab2ffa281e82570b7f5
    role: context
  - path: pages/traits/physiology/pyrrolidonyl_arylamidase_activity.html
    sha256: 2efb7966b5344a927e47668cf15811e401d7617b35c38aed1713677d48b14227
    role: context
  - path: pages/traits/physiology/quorum_sensing.html
    sha256: 05e6e3d197de48239f7acbda35f7f6ac6f99c3e8735b991e0e807e94b4cecbab
    role: context
  - path: pages/traits/physiology/rapid_axopodial_contraction.html
    sha256: ae07e7647bea5cab4b3aad749548e8bbff61bfee366de211cbaf9cb02c374885
    role: context
  - path: pages/traits/physiology/rheotaxis.html
    sha256: 5c4630eaca9610f245b6e4f6beb8f356447e2119d832462108decbd5d861b8b8
    role: context
  - path: pages/traits/physiology/rheotropism.html
    sha256: b000f522fb3931a664baf49cba834d5bea04f7e3cb1c5b76e3ff05d27c63f100
    role: context
  - path: pages/traits/physiology/ribophagy.html
    sha256: ca862d645ae2b31c6ec3f8c230e57befc03fc8a8265676203820561680258a31
    role: context
  - path: pages/traits/physiology/serine_arylamidase_activity.html
    sha256: 7fee98e7e1f3c4eb1cec8302ad0865b30eb25a172a965e3102f8c34a636b2b10
    role: context
  - path: pages/traits/physiology/siderophore_production.html
    sha256: e170797707c29b41ab12b1fccaf7a675d767533a941af2e2edad4b7fb3f4c4f9
    role: context
  - path: pages/traits/physiology/siliceous_scale_production.html
    sha256: fb40723f6bf31be49f6c511978558ec5d0c96eebc3bd90a4f19f9a3c995c2ba3
    role: context
  - path: pages/traits/physiology/sos_response.html
    sha256: 9f79588bddab21919c2dcdf0b84e79650af30b64eedcca3efa17487893d745e4
    role: context
  - path: pages/traits/physiology/spore_germination.html
    sha256: 96aa60bdcbd239b1b96ebe9cf450960e56668e0564fe2e12e8150383206c6070
    role: context
  - path: pages/traits/physiology/stress_response.html
    sha256: bf863bd955609aaf6f1ed4307a469eece01b858ab1bc109be6f7d6dcb2009ca3
    role: context
  - path: pages/traits/physiology/tetrapolar_mating_system.html
    sha256: 0360508f348632adff4e06a8f4527e7e7ae3c0787f3e9f77a9d8427f4e0de38e
    role: context
  - path: pages/traits/physiology/thermotaxis.html
    sha256: 378fede8c34b69ae9f9045a0c0f66e7de6d488d6873a1d57da9c0087a2876b92
    role: context
  - path: pages/traits/physiology/thigmotropism.html
    sha256: c732248e199324e9ad6685887e38abb5fc7353352929bd34200dac7bb21bb6a1
    role: context
  - path: pages/traits/physiology/toxicyst_discharge.html
    sha256: b5b8edea8d2b29aaf82e6ecdb1dc28816c8389acfefcad593cb92e21a2184c87
    role: context
  - path: pages/traits/physiology/trichocyst_discharge.html
    sha256: c450182575b9a63f4bef1b8df8386c53579c251dd2322c56d22c219c5b0239f2
    role: context
  - path: pages/traits/physiology/tripolar_mating_system.html
    sha256: 4edcb29d258d244d01ce811a3eb5c34860f750602dec14c0c3bcb3b062eb3eb8
    role: context
  - path: pages/traits/physiology/trogocytosis.html
    sha256: 83f9d5eae2d1207f7737c45ba807c5d1b97525e6f9484a5890413f847790481f
    role: context
  - path: pages/traits/physiology/trophic_type.html
    sha256: 05aa985ce96670b8b2e400c5b9dc03fd3b08b27687f08fdf618831331525621c
    role: context
  - path: pages/traits/physiology/trypsin_activity.html
    sha256: 5eb2bcc3e2d727f0d1b9c5068f60793a63697504091759f4e54b6b43e7e58268
    role: context
  - path: pages/traits/physiology/tyrosine_arylamidase_activity.html
    sha256: 7b1d6941b7fa4742054c753d462d373f6c95212679d3a08c23a0e958b22d027a
    role: context
  - path: pages/traits/physiology/unconventional_protein_secretion.html
    sha256: 169f640561e33ab4242057377d8cdc33f8b495af321c898d826487ab7445cd57
    role: context
  - path: pages/traits/physiology/unisexual_reproduction.html
    sha256: 184c10b60258398d9ab6ca02b1d1ef9472038a321a23c4e6f519b18fd26c60fe
    role: context
  - path: pages/traits/physiology/urease_activity.html
    sha256: d65effcf76bf411a85e51c4124b549f5a55c6b034ff1edd6cad7890474988b74
    role: context
  - path: pages/traits/physiology/valine_arylamidase_activity.html
    sha256: 410c8f556f3e3b95a65a11c6745ef9f84e473056ac5044bb2fcc9083ea3894ac
    role: context
  - path: pages/traits/physiology/viable_but_nonculturable_state.html
    sha256: c7d9f4867321e616247aebf32cae961c2964ff3ad6d38a4e0eb2d1aacbc61d91
    role: context
  - path: pages/traits/physiology/viscotaxis.html
    sha256: f2c5e6aec5ec6e5ce029a3e0d82ce75aa20708701e8decb4d033c92d5126f4b6
    role: context
  - path: pages/traits/quantitative_property/has_maximum_observed_value.html
    sha256: b9127520ef262f0cdb9e0df7095b841609e27cfdc0749d19739fdcabb6b9e1f6
    role: context
  - path: pages/traits/quantitative_property/has_minimum_observed_value.html
    sha256: 49d322bd8d8a9cb4e4f5eb8b63cb70ac6340af8a890996de95261654ecf8fd98
    role: context
  - path: pages/traits/quantitative_property/has_observed_spot_value.html
    sha256: 4d4869e19cbe658811aec7f27896841791e1fbe52343365b8de66a7f758d2474
    role: context
  - path: pages/traits/quantitative_property/has_value.html
    sha256: cd17c446cdc3ae2cfdb011d12ed3e87022e3a4f9a0de99746d0e3529dc488e90
    role: context
  - path: pages/traits/quantitative_property/has_value_comments.html
    sha256: ec8dd0be415c838dbf256c86087d448a252f9902107be8e2199bf2623555c4ca
    role: context
  - path: pages/traits/quantitative_property/is_negative_data.html
    sha256: c839c6cfe12fe63a676e9696f079af025183401157f2c6b6cff657ee4d47c89c
    role: context
  - path: pages/traits/quantitative_property/observation_data_property.html
    sha256: 84dc87aef2e3f9cb72a1f4b2afdf56b83fc464eb034c8985e01610ea1bc75216
    role: context
  - path: pages/traits/upper/biological_process.html
    sha256: 7cdfc4bd8f55cf894b97c5f23b69de1ec858c3e6bec69966dd9ee2a93e5a4fdf
    role: context
  - path: pages/traits/upper/chemical_entity.html
    sha256: 7942f035a0567034e5421af1d9bae723644db6ecc38c571437872d16a6d7a9a3
    role: context
  - path: pages/traits/upper/enzyme.html
    sha256: 0e8b36c66f7ba26ec3dae2daf7b55ca584a9567f1e9e7aaf6053480478762965
    role: context
  - path: pages/traits/upper/material_entity.html
    sha256: 9f5a0db1f3b330157cbe4e8fd890f76bf4cbb620dd2762d14a851dce0a285983
    role: context
  - path: pages/traits/upper/microbe.html
    sha256: 16014b9f27fdc86cffb2b9f4e6dbb81566bdaaf2eaa196828d2927512316b34e
    role: context
  - path: pages/traits/upper/observation.html
    sha256: 156fd11ca212978b67fd96ffb0ade09650a1aaa37a8e609db6b62fd5876ab2b9
    role: context
  - path: pages/traits/upper/phenotype.html
    sha256: fbd27d735d4ade663f812639bc1859893d9abd8e5967240eb86523480835d144
    role: context
  - path: pages/traits/upper/quality.html
    sha256: 90f2ae5264f7d0f9f695fc60e35f463c9a043fee9f61fb868722a1b3df3f6485
    role: context
  - path: pages/umap.html
    sha256: e5736f5ad1275449dac9a41ddd64acfe3261571528d960ee240d9a51f8ace3e6
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
  - path: proposals/metpo_traitmech_v569/metpo_proposal_classes_robot.tsv
    sha256: 01e596d43828e0da4924f77ccbfca5b51e9daeeef82b5725101aaeadf965346e
    role: context
  - path: proposals/metpo_traitmech_v569/proposal.md
    sha256: e21ebb3c998537fb164884627686de95c330c9a30f4ae3a5874aa37995782e4e
    role: context
  - path: reports/proposal_citation_audit.tsv
    sha256: 05e0237aa85753c005120732d2d67634836ea35e0ffd5ff835ce55339a06ddb3
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/.vendored_canon_ref
    sha256: 698af47e96e93fe96e81910bb140593a79c2b92c4688892edeab9b63244ec5bf
    role: context
  - path: scripts/add_diatom_perizonium_production_trait.py
    sha256: 1b4cc6636b2db9f1d8be823c359765eb23b378c3e2277d9a05a6afd106204cfd
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
  - path: tests/test_add_diatom_perizonium_production_trait.py
    sha256: 33543a6c688c3b0634bb49a90adbcc3695082231c78e2efb93514fb13edf7914
    role: context
targets:
- target_id: traitmech:000693
  path: data/traits/physiology/diatom_perizonium_production.yaml
  label: diatom perizonium production
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/physiology/diatom_perizonium_production.yaml
    role: curated record
  - repository: CultureBotAI/TraitMech
    path: scripts/add_diatom_perizonium_production_trait.py
    role: guarded writer
scope:
  description: One complete new TraitRecord with writer/tests, v569 proposal, history
    and generated surfaces.
  selection: Exact traitmech:000693; no sampling.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - traitmech:000693
  exclusions:
  - target: Other 1087 TraitRecords
    reason: Comparators and automated checks, not corpus-wide scientific adjudication.
  - target: data/traits/physiology/spore_germination.yaml
    reason: DO_NOT_WORK protected; byte-preserved.
checks:
- check_id: records-0
  name: .venv/bin/linkml-validate -s src/traitmech/schema/traitmech.yaml --target-class
    TraitRecord data/traits/physiology/diatom_perizonium_production.yaml
  command: .venv/bin/linkml-validate -s src/traitmech/schema/traitmech.yaml --target-class
    TraitRecord data/traits/physiology/diatom_perizonium_production.yaml
  status: passed
  required: true
  target_ids:
  - traitmech:000693
  exit_code: 0
  expected_exit_code: 0
  summary: Passed at actual native command scope, including corpus-wide gates; no
    baseline relaxation.
- check_id: records-1
  name: .venv/bin/python scripts/validate_strict.py data/traits/physiology/diatom_perizonium_production.yaml
  command: .venv/bin/python scripts/validate_strict.py data/traits/physiology/diatom_perizonium_production.yaml
  status: passed
  required: true
  target_ids:
  - traitmech:000693
  exit_code: 0
  expected_exit_code: 0
  summary: Passed at actual native command scope, including corpus-wide gates; no
    baseline relaxation.
- check_id: records-2
  name: .venv/bin/python scripts/verify_snippets.py --record data/traits/physiology/diatom_perizonium_production.yaml
  command: .venv/bin/python scripts/verify_snippets.py --record data/traits/physiology/diatom_perizonium_production.yaml
  status: passed
  required: true
  target_ids:
  - traitmech:000693
  exit_code: 0
  expected_exit_code: 0
  summary: 2022 NOT_IN_ABSTRACT; 2017 and 2013 VERIFIED. The 2022 Results quote was
    separately checked in official full text, not relabeled as abstract-verified.
- check_id: generate-0
  name: just audit-proposals
  command: just audit-proposals
  status: passed
  required: true
  target_ids:
  - traitmech:000693
  exit_code: 0
  expected_exit_code: 0
  summary: Passed at actual native command scope, including corpus-wide gates; no
    baseline relaxation.
- check_id: generate-1
  name: just ground-predicates
  command: just ground-predicates
  status: passed
  required: true
  target_ids:
  - traitmech:000693
  exit_code: 0
  expected_exit_code: 0
  summary: Passed at actual native command scope, including corpus-wide gates; no
    baseline relaxation.
- check_id: generate-2
  name: just ground-nodes
  command: just ground-nodes
  status: passed
  required: true
  target_ids:
  - traitmech:000693
  exit_code: 0
  expected_exit_code: 0
  summary: Passed at actual native command scope, including corpus-wide gates; no
    baseline relaxation.
- check_id: generate-3
  name: just audit-graphs
  command: just audit-graphs
  status: passed
  required: true
  target_ids:
  - traitmech:000693
  exit_code: 0
  expected_exit_code: 0
  summary: Passed at actual native command scope, including corpus-wide gates; no
    baseline relaxation.
- check_id: generate-4
  name: just audit-graph-protein-taxa
  command: just audit-graph-protein-taxa
  status: passed
  required: true
  target_ids:
  - traitmech:000693
  exit_code: 0
  expected_exit_code: 0
  summary: Passed at actual native command scope, including corpus-wide gates; no
    baseline relaxation.
- check_id: generate-5
  name: just audit-predicate-domains
  command: just audit-predicate-domains
  status: passed
  required: true
  target_ids:
  - traitmech:000693
  exit_code: 0
  expected_exit_code: 0
  summary: Passed at actual native command scope, including corpus-wide gates; no
    baseline relaxation.
- check_id: generate-6
  name: just check-biolink-coverage
  command: just check-biolink-coverage
  status: passed
  required: true
  target_ids:
  - traitmech:000693
  exit_code: 0
  expected_exit_code: 0
  summary: Passed at actual native command scope, including corpus-wide gates; no
    baseline relaxation.
- check_id: generate-7
  name: just audit-snippets
  command: just audit-snippets
  status: passed
  required: true
  target_ids:
  - traitmech:000693
  exit_code: 0
  expected_exit_code: 0
  summary: Passed at actual native command scope, including corpus-wide gates; no
    baseline relaxation.
- check_id: generate-8
  name: just gen-discussions-data
  command: just gen-discussions-data
  status: passed
  required: true
  target_ids:
  - traitmech:000693
  exit_code: 0
  expected_exit_code: 0
  summary: Passed at actual native command scope, including corpus-wide gates; no
    baseline relaxation.
- check_id: generate-9
  name: just gen-qc-dashboard
  command: just gen-qc-dashboard
  status: passed
  required: true
  target_ids:
  - traitmech:000693
  exit_code: 0
  expected_exit_code: 0
  summary: Passed at actual native command scope, including corpus-wide gates; no
    baseline relaxation.
- check_id: generate-10
  name: just gen-pages
  command: just gen-pages
  status: passed
  required: true
  target_ids:
  - traitmech:000693
  exit_code: 0
  expected_exit_code: 0
  summary: Passed at actual native command scope, including corpus-wide gates; no
    baseline relaxation.
- check_id: generate-11
  name: just gen-priority-dashboard
  command: just gen-priority-dashboard
  status: passed
  required: true
  target_ids:
  - traitmech:000693
  exit_code: 0
  expected_exit_code: 0
  summary: Passed at actual native command scope, including corpus-wide gates; no
    baseline relaxation.
- check_id: verify-0
  name: just qc
  command: just qc
  status: passed
  required: true
  target_ids:
  - traitmech:000693
  exit_code: 0
  expected_exit_code: 0
  summary: Passed at actual native command scope, including corpus-wide gates; no
    baseline relaxation.
- check_id: verify-1
  name: just validate-history
  command: just validate-history
  status: passed
  required: true
  target_ids:
  - traitmech:000693
  exit_code: 0
  expected_exit_code: 0
  summary: Passed at actual native command scope, including corpus-wide gates; no
    baseline relaxation.
- check_id: verify-2
  name: just validate-products
  command: just validate-products
  status: passed
  required: true
  target_ids:
  - traitmech:000693
  exit_code: 0
  expected_exit_code: 0
  summary: Passed at actual native command scope, including corpus-wide gates; no
    baseline relaxation.
- check_id: verify-3
  name: just verify-proposal metpo_traitmech_v569
  command: just verify-proposal metpo_traitmech_v569
  status: passed
  required: true
  target_ids:
  - traitmech:000693
  exit_code: 0
  expected_exit_code: 0
  summary: Passed at actual native command scope, including corpus-wide gates; no
    baseline relaxation.
- check_id: verify-4
  name: just robot-validate-proposal metpo_traitmech_v569
  command: just robot-validate-proposal metpo_traitmech_v569
  status: passed
  required: true
  target_ids:
  - traitmech:000693
  exit_code: 0
  expected_exit_code: 0
  summary: Passed at actual native command scope, including corpus-wide gates; no
    baseline relaxation.
- check_id: verify-5
  name: .venv/bin/ruff check src scripts tests
  command: .venv/bin/ruff check src scripts tests
  status: passed
  required: true
  target_ids:
  - traitmech:000693
  exit_code: 0
  expected_exit_code: 0
  summary: Passed at actual native command scope, including corpus-wide gates; no
    baseline relaxation.
- check_id: tests-0
  name: .venv/bin/python -m pytest -q --junitxml=/tmp/traitmech-perizonium-checks-20261010/pytest.xml
  command: .venv/bin/python -m pytest -q --junitxml=/tmp/traitmech-perizonium-checks-20261010/pytest.xml
  status: passed
  required: true
  target_ids:
  - traitmech:000693
  exit_code: 0
  expected_exit_code: 0
  summary: 3830 passed; no failures, errors or skips.
- check_id: focused
  name: focused
  command: .venv/bin/python -m pytest tests/test_add_diatom_perizonium_production_trait.py
    -q
  status: passed
  required: true
  target_ids:
  - traitmech:000693
  exit_code: 0
  expected_exit_code: 0
  summary: '20 passed: identity, source limits, hierarchy, canonical header, dry run/replay,
    controlled preimages, drift refusal and prevalidation. An initial fixture-renaming
    typo was corrected before the passing rerun.'
- check_id: history
  name: history
  command: .venv/bin/python scripts/audit_history_records.py --base 33f6efa71a829eac1b54763336057410970c61ff
  status: passed
  required: true
  target_ids:
  - traitmech:000693
  exit_code: 0
  expected_exit_code: 0
  summary: One changed record with one CREATE history; actual codex actor, model and
    agent tool inspected.
- check_id: browser
  name: browser
  command: node /tmp/traitmech-perizonium-browser-qa-20261010.cjs
  status: passed
  required: true
  target_ids:
  - traitmech:000693
  exit_code: 0
  expected_exit_code: 0
  summary: 'Desktop 1440px and mobile 390px: three quotes, two OPEN discussions, one
    history link, parent with five children, browse navigation, 1088-record dashboard
    and loaded coverage image; no overflow or page errors. Screenshots visually inspected.'
- check_id: artifacts
  name: artifacts
  command: .venv/bin/python /tmp/traitmech-perizonium-artifact-audit-20261010.py
  status: passed
  required: true
  target_ids:
  - traitmech:000693
  exit_code: 0
  expected_exit_code: 0
  summary: '1087 old trait YAMLs preserved byte-for-byte; 1086 prior pages change
    only footer, parent adds child. Sole old priority change: parent children 4 to
    5. Prior history, reviews, proposals, embeddings and browser templates preserved;
    protected spore germination unchanged.'
- check_id: rdf
  name: rdf
  command: .venv/bin/python /tmp/traitmech-perizonium-rdf-check-20261010.py
  status: passed
  required: true
  target_ids:
  - traitmech:000693
  exit_code: 0
  expected_exit_code: 0
  summary: 'Parsed RDF cardinalities {''classes'': 15, ''merged'': 12628, ''reasoned'':
    12632}; w3id 1064600 -> phenotype 1000059 -> quality 1000188. No OBO METPO stubs.
    Proposed 1064300 refinement requested but not emitted standalone.'
- check_id: sources
  name: sources
  command: .venv/bin/python /tmp/traitmech-perizonium-source-check-20261010.py
  status: passed
  required: true
  target_ids:
  - traitmech:000693
  exit_code: 0
  expected_exit_code: 0
  summary: Three exact source-qualified MED/PMID/title/DOI results; contiguous quotes
    checked in scientific sections; cached actual figures retain recorded SHA-256
    identities.
- check_id: reservations
  name: reservations
  command: .venv/bin/python /tmp/traitmech-perizonium-prepublish-20261010.py
  status: passed
  required: true
  target_ids:
  - traitmech:000693
  exit_code: 0
  expected_exit_code: 0
  summary: Current main, five pending PR heads and full paginated file lists unchanged;
    ignored/hidden worktree searches found no unowned reservation or unresolved new
    match.
- check_id: contracts
  name: contracts
  command: .venv/bin/python /tmp/traitmech-perizonium-prepare-20261010.py
  status: passed
  required: true
  target_ids:
  - traitmech:000693
  exit_code: 0
  expected_exit_code: 0
  summary: 152 shared-source blobs verified against pinned CLAW; canonical class/property
    headers rehashed against pinned upstream Git blobs; exact configured embedding
    sources absent in primary and owned layouts.
- check_id: whitespace
  name: whitespace
  command: git -c core.whitespace=-blank-at-eol diff --cached --check -- proposals/metpo_traitmech_v569/metpo_proposal_classes_robot.tsv
  status: passed
  required: true
  target_ids:
  - traitmech:000693
  exit_code: 0
  expected_exit_code: 0
  summary: Ordinary check identifies only required trailing ROBOT cells. Exact-path
    exception and separate non-TSV check pass; no global configuration changed.
- check_id: embeddings
  name: Embedding applicability
  status: not_applicable
  required: false
  target_ids:
  - traitmech:000693
  summary: Exact configured sources absent independently of gitignore; previous embedding
    artifacts preserved.
evidence:
- evidence_id: biddulphia
  kind: primary_source
  reference: DOI:10.1371/journal.pone.0272778
  locator: 'Scientific Abstract, Introduction, Methods, early Results, Epizonium and
    perizonium, Discussion: Auxospore structure and development; actual Figure 11.
    Official XML https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9447881/fullTextXML
    reread; other actual figures and S1 Appendix unread. https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A36067191+AND+SRC%3AMED&format=json&resultType=core'
  accessed_at: '2026-10-10T23:18:44.351905Z'
  snapshot_sha256: e32ce810dc161ca8faf90cffa34a62b169eb1cbb129922ab1267017282154338
  support: supports
  summary: Formation of siliceous TP/LP bands in an auxospore wall supports the definition.
    Fixed stages are not live kinetics. Some layer boundaries remain uncertain; atypical
    cultured clone is not assigned as canonical.
- evidence_id: plagiogrammaceans
  kind: primary_source
  reference: DOI:10.1371/journal.pone.0181413
  locator: Scientific Abstract, Methods prose, Auxospore wall fine structure, relevant
    Discussion paragraphs, actual Figure 5; Table 1/2 headers/footnotes and StA:7/8,
    Van5:5/6 rows. Official XML https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5558960/fullTextXML
    reread; remaining rows not fully interpreted, other figures/supplements unread.
    https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A28813426+AND+SRC%3AMED&format=json&resultType=core
  accessed_at: '2026-10-10T23:18:45.092565Z'
  snapshot_sha256: 399998f5a66536b299e2622e0177ad3a1fc945c234d02cda097603b5df6f292d
  support: supports
  summary: TP production with inferred near-simultaneous deposition argues against
    universal one-at-a-time secretion. Initial epivalves are not LP by default. The
    2013 Tabularia study is retained as reference 100; reinterpretation concerns other
    sources. Aged cultures are not archetypes.
- evidence_id: tabularia
  kind: primary_source
  reference: DOI:10.1016/j.ejop.2013.06.002
  locator: Complete scientific Abstract in source-qualified Europe PMC CORE, online
    2013-08-22 / 2014 issue. Full Methods, figures and supplements unread; publisher
    full text unavailable. https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A23972513+AND+SRC%3AMED&format=json&resultType=core
  accessed_at: '2026-10-10T23:18:46.312804Z'
  snapshot_sha256: 6ddea50ebfc5f9ce1f60b22c4af1d86e812dddcdb82c2f630644eb4ca86550ef
  support: supports
  summary: LP deposition without TP near maximal auxospore length supports the boundary.
    EDS nondetection is not absolute absence. These distinct primary studies share
    authors and do not establish independent-laboratory replication.
- evidence_id: record
  kind: record_content
  reference: data/traits/physiology/diatom_perizonium_production.yaml
  locator: Whole record, comparator definitions and discussions.
  accessed_at: '2026-10-10T23:46:01Z'
  support: supports
  summary: Production phenotype with strictly broader biomineralization parent; no
    inherited-possession, organism-level disjointness, universal sexual origin or
    protein-mechanism claim. Two actionable OPEN discussions; PROPOSED status retained.
- evidence_id: novelty
  kind: search
  reference: proposals/metpo_traitmech_v569/proposal.md
  locator: Complete allocation, hierarchy, boundaries and upstream round trip.
  accessed_at: '2026-10-10T23:46:01Z'
  support: supports
  summary: No exact term or conflicting reservation found in recorded search scope.
    Whole 1064600-1064699 block reserved, only 1064600 populated; distinct anisogamy
    use of 2017 citation does not establish a duplicate.
  search_scope: 'Whole main and all 22 pre-existing worktrees plus owned branch, ignored/hidden
    included: perizoni/perizonal/properizoni, auxospore bands/walls/silica, source
    species and three DOI/PMID plus both PMC identities; broader mineral/diatom/frustule/scales/reproductive
    context. Full 12617-triple pinned ontology, 399 fresh seeds, 1546-row release
    delta and 153-row active review/policy; five open PRs including draft 924 with
    complete paginated files and immutable curation blobs. CommunityMech whole-block
    search zero hits. No global exhaustion claim.'
- evidence_id: implementation
  kind: record_content
  reference: scripts/add_diatom_perizonium_production_trait.py
  locator: Whole writer, focused tests and CREATE history.
  accessed_at: '2026-10-10T23:46:01Z'
  support: supports
  summary: Native validated mutation and curation event with dry-run/replay and preimage
    guards. History attribution correct; no scientific status promotion. Existing
    add-trait guidance covers the encountered source and sequence-feature interpretation
    limits.
- evidence_id: products
  kind: validation
  reference: reports/proposal_citation_audit.tsv
  locator: Native checks, generated pages, dashboards, corpus counts and ROBOT RDF.
  accessed_at: '2026-10-10T23:46:01Z'
  support: supports
  summary: 1088 unique records and 573 proposed records pass citation gate. Rendered
    identity, hierarchy, snippets and history agree with source. No prior source record,
    protected record, embedding or immutable review changed.
assessments:
- assessment_id: identity
  area: identity
  topic: Production of a specific mineralized wall system
  summary: The definition denotes a reusable production phenotype, not a material
    object or auxosporulation generally.
  target_ids:
  - traitmech:000693
  evidence_ids:
  - record
  - biddulphia
  - plagiogrammaceans
  - tabularia
  outcome: supported
- assessment_id: novelty
  area: identity
  topic: Distinct endpoint and reservation
  summary: No exact record or ontology class was found in bounded ignored/hidden searches.
    Prior broad endpoint notes require no exact-node repair.
  target_ids:
  - traitmech:000693
  evidence_ids:
  - novelty
  - record
  outcome: supported
- assessment_id: hierarchy
  area: grounding
  topic: Strictly broader biomineralization
  summary: Mineralized-band production entails biomineralization. Released-ancestor
    TSV and explicit v566 refinement are consistent.
  target_ids:
  - traitmech:000693
  evidence_ids:
  - record
  - novelty
  - products
  outcome: supported
- assessment_id: evidence
  area: evidence
  topic: Primary observations and varied band systems
  summary: Exact source snippets support formation without universal orientation,
    sequence or expansion timing. Static morphology and chemical labeling do not establish
    protein-level necessity.
  target_ids:
  - traitmech:000693
  evidence_ids:
  - biddulphia
  - plagiogrammaceans
  - tabularia
  outcome: supported
- assessment_id: provenance
  area: provenance
  topic: Guarded curation and actual attribution
  summary: Controlled preimage tests, native curation event and explicit codex CREATE
    history agree with the change.
  target_ids:
  - traitmech:000693
  evidence_ids:
  - implementation
  - products
  outcome: supported
- assessment_id: consistency
  area: consistency
  topic: Proposal and rendered products
  summary: Canonical template, RDF hierarchy, counts, source text and navigation agree.
    Historical artifacts are preserved.
  target_ids:
  - traitmech:000693
  evidence_ids:
  - products
  - novelty
  outcome: supported
- assessment_id: gaps
  area: completeness
  topic: Mapping, exemplar and mechanism follow-up
  summary: No authority-verified exact mapping or canonical clone assigned. Functional
    evidence and paired accessions are required for protein edges; discussions retain
    these gaps.
  target_ids:
  - traitmech:000693
  evidence_ids:
  - record
  - biddulphia
  - plagiogrammaceans
  - tabularia
  outcome: unknown
findings: []
actions: []
limitations:
- Author self-review, not independent review or human scientific signoff; full coverage
  means one target.
- Only stated source sections, table rows and two actual figures inspected. 2013 source
  limited to scientific Abstract; unread supplements and figures are not evidence.
- The 2022 quote remains native NOT_IN_ABSTRACT despite direct Results verification.
  Shared authorship is not independent-laboratory replication.
- No canonical taxon, exact synonym/xref, protein or graph asserted. Two OPEN discussions;
  record PROPOSED.
- Standalone proposal uses released phenotype; adoption must reconcile v566 biomineralization
  refinement.
- Configured embedding sources absent; old artifacts preserved. No paid research performed.
- Decision, history, source-recheck and review timestamps denote different events.
  Working-tree hashes attest inspected bytes, not proof of committed input bytes.
notes:
- Issue 1856 tracks a README prose-count mismatch in the initial local draft, corrected
  before the scientific checkpoint and this review. Current main was not defective.
  Existing prose-count tests cover the correction; there are no outstanding findings
  in this final assessment.
tags:
- add-trait
- diatom-perizonium-production
- self-review
```
