# Successor adversarial self-review of decline-qualified replicative aging

- Review: 20261012T110106Z-replicative-aging
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-12T10:43:24Z
- Finished UTC: 2026-10-12T11:01:06Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

One evidence-backed decline-qualified phenotype, four primary DOIs with snippets. One minor label finding resolved; zero open actionable findings in this scope. Mechanism/taxon/upstream terminology remain limited and status stays PROPOSED.

## Scope And Provenance

Complete corrected record, maintained writers/tests, proposal, history, related skill/README changes and derived artifacts.

Selection: One exact new trait; no sampling.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 36874da012f28aa92453c64aebae8a4390f4f37d.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| traitmech:000709 | data/traits/physiology/replicative_aging.yaml | maintained | replicative aging with functional decline |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| .venv/bin/linkml-validate -s src/traitmech/schema/traitmech.yaml --target-class TraitRecord data/traits/physiology/replicative_aging.yaml | passed | True | traitmech:000709 | Actual native check passed on corrected content; corpus validation is not whole-corpus scientific review. |
| .venv/bin/python scripts/validate_strict.py data/traits/physiology/replicative_aging.yaml | passed | True | traitmech:000709 | Actual native check passed on corrected content; corpus validation is not whole-corpus scientific review. |
| .venv/bin/python scripts/verify_snippets.py --record data/traits/physiology/replicative_aging.yaml --out /tmp/traitmech-aging-final-checks-20261012/snippet-results.tsv | passed | True | traitmech:000709 | Two VERIFIED scientific-abstract snippets and two NOT_IN_ABSTRACT full-text snippets. Direct XML section checks support all four; full-text matches were not relabeled as abstract matches. |
| .venv/bin/python -m pytest -q tests/test_add_replicative_aging_trait.py tests/test_qualify_replicative_aging_label.py | passed | True | traitmech:000709 | 31 focused writer tests passed: dry-run default, exact preimage refusal, prevalidation, no partial writes on rejected inputs, copy isolation and idempotent replay. |
| just audit-proposals | passed | True | traitmech:000709 | Actual native check passed on corrected content; corpus validation is not whole-corpus scientific review. |
| just ground-predicates | passed | True | traitmech:000709 | Actual native check passed on corrected content; corpus validation is not whole-corpus scientific review. |
| just ground-nodes | passed | True | traitmech:000709 | Actual native check passed on corrected content; corpus validation is not whole-corpus scientific review. |
| just audit-graphs | passed | True | traitmech:000709 | Actual native check passed on corrected content; corpus validation is not whole-corpus scientific review. |
| just audit-graph-protein-taxa | passed | True | traitmech:000709 | Actual native check passed on corrected content; corpus validation is not whole-corpus scientific review. |
| just audit-predicate-domains | passed | True | traitmech:000709 | Actual native check passed on corrected content; corpus validation is not whole-corpus scientific review. |
| just check-biolink-coverage | passed | True | traitmech:000709 | Actual native check passed on corrected content; corpus validation is not whole-corpus scientific review. |
| just audit-snippets | passed | True | traitmech:000709 | Actual native check passed on corrected content; corpus validation is not whole-corpus scientific review. |
| just gen-discussions-data | passed | True | traitmech:000709 | Actual native check passed on corrected content; corpus validation is not whole-corpus scientific review. |
| just gen-qc-dashboard | passed | True | traitmech:000709 | Actual native check passed on corrected content; corpus validation is not whole-corpus scientific review. |
| just gen-pages | passed | True | traitmech:000709 | Actual native check passed on corrected content; corpus validation is not whole-corpus scientific review. |
| just gen-priority-dashboard | passed | True | traitmech:000709 | Actual native check passed on corrected content; corpus validation is not whole-corpus scientific review. |
| just qc | passed | True | traitmech:000709 | Actual native check passed on corrected content; corpus validation is not whole-corpus scientific review. |
| just validate-history | passed | True | traitmech:000709 | Actual native check passed on corrected content; corpus validation is not whole-corpus scientific review. |
| just validate-products | passed | True | traitmech:000709 | Actual native check passed on corrected content; corpus validation is not whole-corpus scientific review. |
| just verify-proposal metpo_traitmech_v585 | passed | True | traitmech:000709 | Actual native check passed on corrected content; corpus validation is not whole-corpus scientific review. |
| just robot-validate-proposal metpo_traitmech_v585 | passed | True | traitmech:000709 | Actual native check passed on corrected content; corpus validation is not whole-corpus scientific review. |
| .venv/bin/ruff check src scripts tests | passed | True | traitmech:000709 | Actual native check passed on corrected content; corpus validation is not whole-corpus scientific review. |
| .venv/bin/python -m pytest -q --junitxml=/tmp/traitmech-aging-stable-tests-20261012/pytest.xml | passed | True | traitmech:000709 | 4212 tests passed with no failures, errors or skips in the stable-tree rerun. Earlier overlapping-generation run had one stale discussions-data failure; its receipt is retained, not counted as a pass. |
| .venv/bin/python scripts/validate_history_links.py history/records/replicative_aging | passed | True | traitmech:000709 | Actual native check passed on corrected content; corpus validation is not whole-corpus scientific review. |
| .venv/bin/linkml-validate --schema src/traitmech/schema/history.yaml --target-class HistoryRecord history/records/replicative_aging/2026-10-12T101846Z-codex-957baa.yaml | passed | True | traitmech:000709 | Actual native check passed on corrected content; corpus validation is not whole-corpus scientific review. |
| .venv/bin/linkml-validate --schema src/traitmech/schema/history.yaml --target-class HistoryRecord history/records/replicative_aging/2026-10-12T103127Z-codex-884508.yaml | passed | True | traitmech:000709 | Actual native check passed on corrected content; corpus validation is not whole-corpus scientific review. |
| .venv/bin/python scripts/audit_canonical_examples.py --no-resolve | passed | True | traitmech:000709 | Actual native check passed on corrected content; corpus validation is not whole-corpus scientific review. |
| .venv/bin/python scripts/run_trait_graph_audit.py --verify | passed | True | traitmech:000709 | Actual native check passed on corrected content; corpus validation is not whole-corpus scientific review. |
| .venv/bin/python scripts/audit_history_records.py --base 53188095ebb645d2e21bf2d5dbe6548046190279 | passed | True | traitmech:000709 | Actual native check passed on corrected content; corpus validation is not whole-corpus scientific review. |
| git diff --check 53188095ebb645d2e21bf2d5dbe6548046190279 HEAD -- . ':(exclude)proposals/metpo_traitmech_v585/metpo_proposal_classes_robot.tsv' | passed | True | traitmech:000709 | Actual native check passed on corrected content; corpus validation is not whole-corpus scientific review. |
| git -c core.whitespace=-blank-at-eol diff --check 53188095ebb645d2e21bf2d5dbe6548046190279 HEAD -- proposals/metpo_traitmech_v585/metpo_proposal_classes_robot.tsv | passed | True | traitmech:000709 | Actual native check passed on corrected content; corpus validation is not whole-corpus scientific review. |
| Superseded full suite overlapping regeneration | failed | False | traitmech:000709 | Historical run:4211 passed and one discussions searchData freshness failure while generation was unfinished. Preserved as a failed execution, superseded by the required stable-tree rerun; not counted as a passing acceptance check. |
| Isolated discussions freshness recheck | passed | True | traitmech:000709 | The previously failing test passed on the generated and committed tree before the full stable rerun. |
| Desktop/mobile generated-page inspection | passed | True | traitmech:000709 | 1440/390 px assertions and eight visually inspected screenshots: qualified label, local identifier provenance, four quotes, two discussions, two history links, hierarchy/browse navigation and dashboard image/counts, no horizontal overflow or JavaScript errors. |
| Embedding applicability | not_applicable | False | traitmech:000709 | Neither exact configured source exists in primary or owned layouts. Existing embedding artifacts retained, not regenerated. |

## Scientific And Domain Assessments

### Decline-qualified cellular phenotype

identity: supported. Targets: traitmech:000709.

Operational age-associated decline is supported, explicitly qualified, and not equated with finite lifespan or culture age.

### Terminology and conditions

scope: supported. Targets: traitmech:000709.

Broader healthy-aging usage, age axis, plateau, engineered strains and measurement limitations remain explicit.

### Phenotype parent and absent equivalence claims

grounding: supported. Targets: traitmech:000709.

Active w3id phenotype-to-quality hierarchy is broader; no shifted xrefs or forced sibling/node grounding added.

### Four primary citations and exact snippets

evidence: supported. Targets: traitmech:000709.

Positive bacterial evidence and boundary yeast evidence are distinguished; no metadata-only source or preprint counted as replication.

### Bounded novelty and full-block allocation

identity: supported. Targets: traitmech:000709.

Ignored/hidden searches, controlled historical regex and fresh pending-reservation checks support one new inspected trait.

### Guarded correction and immutable lineage

provenance: supported. Targets: traitmech:000709.

Issue1891 is resolved without rewriting initial history/review; human sign-off is not implied.

### Native gates and regenerated products

consistency: supported. Targets: traitmech:000709.

Qualified identity, counts, proposal RDF and navigation agree; prior records and protected file remain unchanged.

### Unasserted mechanisms and natural exemplars

completeness: unknown. Targets: traitmech:000709.

Canonical taxa, strain discrepancy and protein-resolved mechanisms remain deferred, not inferred from markers or lifespan.

## Findings

### label-qualifier: Unqualified aging label hides the functional-decline restriction

minor / resolved / confirmed; issue key: replicative-aging-functional-decline-label.

The source also uses replicative aging for healthy age progression. The record admits that broader meaning but leaves the label and proposal unqualified, so label-only consumers cannot distinguish the narrower phenotype.

Disposition: Record, proposal and rendered labels now expose the functional-decline qualifier. Guarded correction, tests and source-based reassessment pass with original provenance preserved.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| bacterial | DOI:10.1098/rstb.2018.0442; Primary JATS XML: Introduction, Methods, Results(a,b), selected Discussion; Figure 2 caption and actual author-PDF figure. | supports | Age-indexed division-time increase supports a decline phenotype, with later plateau and initial-condition limitations. Brightfield measurements are distinct from fluorescent assays. Methods BW25113 versus Introduction BW21113 remains unresolved, not assigned a canonical taxon. |
| caulobacter | DOI:10.1186/1471-2148-7-126; Scientific abstract Background; directly retrieved primary XML and publisher Background, Results, Discussion, Methods and captions. | supports | Declining reproductive function supports bacterial aging. The cohort endpoint combines survival/reproduction, evolved clones differ in aging direction, and pilA-deletion UJ590 is not an unmodified natural exemplar. Elapsed-time assay complements division-indexed evidence. |
| fission-boundary | DOI:10.7554/eLife.20340; Scientific abstract, not eLife digest, and Discussion in directly retrieved primary XML; source-qualified MED PMID28139976. | supports | Finite replicative lifespan and lifespan extension without classic deterioration are boundary evidence, not a positive exemplar. Constant hazard is not increasing mortality risk, and cumulative survival loss alone is insufficient. |
| yeast-boundary | DOI:10.1371/journal.pbio.3002245; Scientific Abstract, first Results section, Discussion, strain Methods and captions; directly reopened PLOS and primary XML. | supports | Diet-dependent maintenance of performance without longer lifespan separates functional decline from lifespan. Engineered MEP system and broader healthy-ageing terminology are explicit. Qualifying the label avoids equating the narrower operational phenotype with every use of replicative aging. |
| snippets | research/traits/physiology/replicative_aging-source-verification.json; Exact DOI/source-qualified MED/Crossref identity checks, hashed JATS bytes, exact XPath/snippet checks; native final resolver TSV. | supports | Four exact contiguous snippets of 11/12/21/22 words. Two are scientific abstracts, two are full-text caption/Results. Linked preprints, peer evaluations and sequence links are contextual metadata, not independent experiments. Notice checks are bounded, not exhaustive. |
| content | data/traits/physiology/replicative_aging.yaml; Complete final YAML, two writers/tests, two append-only history entries, v585 proposal, skill update, README and rendered page. | supports | One PHYSIOLOGY CLASS under phenotype; age-specific performance decline or increasing risk, not a lifespan field, sequence feature, culture age, old-pole identity or universal mechanism. No synonyms, xrefs, examples or causal graph asserted. |
| novelty | proposals/metpo_traitmech_v585/proposal.md; Full surviving roots with ignored/hidden files; corrected historical PCRE searches with known-positive control; seed/release/RDF/upstream/pending-PR reconciliation and fresh reservation refresh. | supports | No exact competing record or reserved ID/block in inspected scope. Reserve 000709, v585 and 1066200-1066299, populate only 1066200. Culture-aging stationary-phase node and host senescence mentions are not exact. No global exhaustion claim. |
| reservation | /tmp/traitmech-aging-publication-20261012/result.json; Fresh full-block scan across current registered roots and registered historical trees, paginated pending files, immutable upstream bytes. | supports | Refresh at 2026-10-12T10:38:01.349308+00:00 finds no competing reservation. Candidate-owned hits are explicitly distinguished; no external worktree was changed. |
| resolution | https://github.com/CultureBotAI/TraitMech/issues/1891; qualify_replicative_aging_label.py, regression tests, label and discussion, v585 label/narrative, add-trait skill and appended event/history. | supports | Label now explicitly says replicative aging with functional decline. Definition, evidence, identifier and original provenance are preserved; bare aging is not an exact synonym. Remaining upstream terminology is a disclosed curation question. |
| products | reports/proposal_citation_audit.tsv; Final native gates, full/focused tests, parsed RDF, byte-preservation receipts, browser assertions and screenshots. | supports | 1104 records; all 1103 prior YAMLs and prior history/reviews/proposals/embeddings/templates preserved.1102 old pages are footer-only; phenotype gains one child. RDF cardinalities {'classes': 15, 'merged': 12628, 'reasoned': 12632}, w3id parent hierarchy and qualified label agree. No baseline weakened; required TSV directive tabs receive only an exact-path whitespace exception. |
| prior | reviews/structured/20261012T102912Z-aging-label-scope/review.yaml; Initial partial self-review at c53a5fb357b620dc9cbc73aa3403ffacd108898f; finding label-qualifier. | context_only | Original open finding remains immutable; this successor reassesses the correction and records explicit resolution lineage. |

## Limits And Additional Notes

- Self-review, not independent or human sign-off; hashed corpus context is not whole-corpus scientific reassessment.
- Evidence access times include reinspection of directly retrieved snapshots, not necessarily fresh downloads. PLOS reopened directly; PMC2019 reopening returned CAPTCHA.
- Only 2019 Figure 2 visually assessed for primary-source graphics. Other figures, supplements and raw data not independently reanalysed; no molecular mechanism or natural canonical taxon asserted.
- Source-qualified MED/Crossref notice fields and available publisher pages bound the notice check; no exhaustive absence claim.
- Existing adapter-skipped product rows and source-license warnings are retained as limitations, not authority resolutions or newly fixed defects.
- Embedding sources unavailable; existing embeddings retained. Required ROBOT header tabs retain a narrow inspected whitespace exception.
- Historical tracked trees cannot reconstruct unavailable current ignored/untracked files. No archive, symlink-directory, unregistered/private search or global exhaustion claim.
- Native working_tree input capture attests inspected bytes at its recorded Git base; recovery of that base does not prove every ignored RDF input was committed.
- An earlier full suite overlapped artifact regeneration and reported one stale discussions-data failure. The failed 846-second run remains in /tmp/traitmech-aging-final-checks-20261012/tests.json; only the subsequent stable-tree rerun is the passing full-suite gate.
- External review requests, final CI and merge-queue checks follow publication and are not claimed complete here.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T110106Z-replicative-aging
kind: record
repository: CultureBotAI/TraitMech
title: Successor adversarial self-review of decline-qualified replicative aging
started_at: '2026-10-12T10:43:24Z'
finished_at: '2026-10-12T11:01:06Z'
reviewer:
  identity: codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Author source-based adversarial review, not independent review
    or human scientific sign-off.
skill: .claude/skills/add-trait/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: One evidence-backed decline-qualified phenotype, four primary DOIs with snippets.
  One minor label finding resolved; zero open actionable findings in this scope. Mechanism/taxon/upstream
  terminology remain limited and status stays PROPOSED.
source:
  git_revision: 36874da012f28aa92453c64aebae8a4390f4f37d
  state: working_tree
  inputs:
  - path: .claude/skills/add-trait/SKILL.md
    sha256: eb6de9d02b724c174f119f5c53bfc5cea231ac4061aebe4e3530b6f1e647439c
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
    sha256: ae42d87aa68d1a0be0bfb1ee95559cfff187a9911bb071faa28103bd145888dd
    role: context
  - path: app/dashboard/priority.html
    sha256: a5b36d701fb041abae63fddaceddebec8ddbae0708a01b3032f04fbb19c1ffe1
    role: context
  - path: app/dashboard/priority.json
    sha256: 1b508d230a3c61f6f497fa923982d87d07bab4ba7854d7417cb52553dc04237f
    role: context
  - path: app/discussions/data.js
    sha256: 3bffeadb4da9931d0a2a113c26e8e5bf7f3e68713dc0371800b678f0360f1060
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
    sha256: d70b350e34ef0bab215681015ebcf8fc7dcf246ce40225a266d656e0034fbf26
    role: context
  - path: dashboard/index.html
    sha256: f755d5020f878dc94bc3e257b6e0254f69d4aa4eda93b651dde14b8f8391464f
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
    role: target
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
  - path: history/records/replicative_aging/2026-10-12T101846Z-codex-957baa.yaml
    sha256: 5ee9f6453c8356220d05be04e335e85bf01efec15cab8cb02af025a1d603be1f
    role: context
  - path: history/records/replicative_aging/2026-10-12T103127Z-codex-884508.yaml
    sha256: 23bd02d7246fdd9c6155c8e065876c20ee504e7c05057b76a6c05dc71255c967
    role: context
  - path: justfile
    sha256: e6047ea612115a6a78d100b281483ba824c860c3def59bcd0d40e7fb56b3526a
    role: context
  - path: pages/browse.html
    sha256: e92128a4752e61b9330e33d5e9b8c256436c88a3bf8a72d8a6b614f948210d00
    role: context
  - path: pages/category/ecology.html
    sha256: 567d93227de697b0004e90885bba60f05835f7e332a0dc1d8ae88de317675f35
    role: context
  - path: pages/category/environment.html
    sha256: 8f61ab83cb51c0746e5bdd6ec8b28f4bbf450a0fd919c0f6ea12d55863522116
    role: context
  - path: pages/category/genomics.html
    sha256: 80d32b70f338e7e05cc3da63a8147777f76df20921a3ca2c01a4a549e9cd0abd
    role: context
  - path: pages/category/metabolism.html
    sha256: c9dd5a6a656ee1b96d0c77a6b7d59c7e1da1008f54462d48edcc596f7a63b396
    role: context
  - path: pages/category/morphology.html
    sha256: 69db83d2473ac6a570c6c27a26d7e796966ea510a57b137b51ba96c6d948eb0c
    role: context
  - path: pages/category/observation.html
    sha256: 0945b9fb0d1402cb8f08b22e6aa38f6d5fb80924119a922590ffc6f9e5e3ac6b
    role: context
  - path: pages/category/other.html
    sha256: ae4156239ec4d3b028508c4426b8a5dc644a406ba966146d778ce42f7178b13e
    role: context
  - path: pages/category/physiology.html
    sha256: 91e31c1c3dde38fd889b9f2b8179965c692920926a7d9efa61d332a38d378e66
    role: context
  - path: pages/category/quantitative_property.html
    sha256: 2369627617f2646f62aa2a22d1e2e267a26c24fbff002a6d0a2bf3c349822d3e
    role: context
  - path: pages/category/upper.html
    sha256: e40f1fc3ce189fbe1d39039b033b891e58206c82010ca03ab00a7386eff77092
    role: context
  - path: pages/graph.html
    sha256: 06cb47cc0d78505230e14db177885bd6321cfeee62dd36f388ece678865e57b6
    role: context
  - path: pages/index.html
    sha256: 0b20b5358dc66710877c152c07b8f614eaf709a6dce46c09e64f77f96634c513
    role: context
  - path: pages/traits/ecology/animal_pathogen.html
    sha256: 17353a983318fd738d0a670bca54c8a725b578d91678a65231dff2035a868f1b
    role: context
  - path: pages/traits/ecology/bacterial_cannibalism.html
    sha256: 059388f4f88491239ee2e4ab7542c37e6d4ee22bb210b18d435439028f110bee
    role: context
  - path: pages/traits/ecology/bacterial_mycophagy.html
    sha256: 7630355fc644a34b6afe832eafba670b80efa34d9cb73ef24f38c40a298ea974
    role: context
  - path: pages/traits/ecology/biofilm_formation.html
    sha256: 6e80795dbc04ddbe24bd7e06a41f3a90d781a0ce3b4ffca81ba74a76593b0c2d
    role: context
  - path: pages/traits/ecology/biosafety_level.html
    sha256: 7a692d086440c05893169200d8bba5b326a1e2bbf065924737ef39a64180be18
    role: context
  - path: pages/traits/ecology/biosafety_level_1.html
    sha256: 81016febf211aebac7e9d29738569d92d2a46208dfac283393c30424bab02748
    role: context
  - path: pages/traits/ecology/biosafety_level_2.html
    sha256: ec80de5083beffcaac9b938766eeb121ac97f43b21fd7e9a35a5dca2a36a2958
    role: context
  - path: pages/traits/ecology/biosafety_level_3.html
    sha256: 66564093edc0b4b3cad2c31d7d361145fadceee66b16c5bcb381418ba8c72645
    role: context
  - path: pages/traits/ecology/biosafety_level_4.html
    sha256: f28fff23414af92a45345e401d51ce6b278ddd3e7f68c49f969b1b6531357c72
    role: context
  - path: pages/traits/ecology/biosafety_level_5.html
    sha256: 67a0106e988accd5f06353f6940454ec29874fc38815f3cc7a75abc94820bb7b
    role: context
  - path: pages/traits/ecology/collective_bacterial_predation.html
    sha256: 5621d9f1239bdf00225e65a416fb44fbfe27befea268cac1cc76d65cebaca730
    role: context
  - path: pages/traits/ecology/commensalism.html
    sha256: b560b1f504c3ca6a85462e9e07924b07537608c8053021d61ca0779efa789ca9
    role: context
  - path: pages/traits/ecology/cytoplasmic_bacterial_predation.html
    sha256: eaa44544d837bdc5f5af6043a74e1be2d511ac4d91244ef54847fe25bea37303
    role: context
  - path: pages/traits/ecology/endophytic.html
    sha256: 5961683b8581e018acb38f456a5930579d8a43673a2f03e05324e9fc0de927d8
    role: context
  - path: pages/traits/ecology/endosymbiosis.html
    sha256: 60db445dbea91d2e598f7988e1a5cdf3131b428cdc9ec0206719225eb78904c7
    role: context
  - path: pages/traits/ecology/epibiotic_bacterial_predation.html
    sha256: a6bbebcf8428e9f561e946055d1e30237ea5e902a0e4727f0ca0ce77e2408d16
    role: context
  - path: pages/traits/ecology/epiphytic.html
    sha256: 23dc769d32f4543ccbb2ea89208b7e9de86a7acc99b3d9e64c2b711f97de244c
    role: context
  - path: pages/traits/ecology/free_living.html
    sha256: 3870da014e082b8fe1f079a82d602139fd3d5e8b1b70b720628273e02b67d016
    role: context
  - path: pages/traits/ecology/gut_associated.html
    sha256: f71647d2487c757bec4485dc5585ff47adad9c84790f0836a800c31c0892a94d
    role: context
  - path: pages/traits/ecology/habitat_association.html
    sha256: 0f0a4dd94760a25cf139be1b9832bf5e167f60cc4c9a6a05868a7b038aed7dae
    role: context
  - path: pages/traits/ecology/host_associated.html
    sha256: c1cec48be323485bbf2011331cac7d4b5a2b146c5dadd7a3c0f20d2e014401e6
    role: context
  - path: pages/traits/ecology/human_pathogen.html
    sha256: 829ac22e8c7718c0904af06505086ab56c87159a80fe71311b9e266f10ec3149
    role: context
  - path: pages/traits/ecology/ixotrophy.html
    sha256: 261228557af2db7aeccce39a2adace52d04de0f710d9591d29344832d32b690c
    role: context
  - path: pages/traits/ecology/mutualism.html
    sha256: 6199d9992ac3b3146493a8e0d38561a0e3299cbb18fadb1ce46447bc0cdcea25
    role: context
  - path: pages/traits/ecology/nitrogen_fixing_symbiosis.html
    sha256: e1e10940893f18e6c4f68ebd5db09baaf792e6a602b093eee4b5da621cea2f3c
    role: context
  - path: pages/traits/ecology/opportunistic_pathogen.html
    sha256: df767fd2384a4914ed4063a313188a1bec1fdc0891c2d8bd9b4766ac2916decc
    role: context
  - path: pages/traits/ecology/parasitism.html
    sha256: 03e596b0061980a66dfffe152f09ca7f6b2f8a112e894d961aa6c37599e3496c
    role: context
  - path: pages/traits/ecology/pathogenic_to_host.html
    sha256: 49a467212324b08a0ffbcdac85f6876cce1ebafdeff64b6f352ba3b0056e801c
    role: context
  - path: pages/traits/ecology/periplasmic_bacterial_predation.html
    sha256: 38ffac8f9c4b9fbf06a78c19a79feb7283c250a1eb62e8d417f2fe6893373618
    role: context
  - path: pages/traits/ecology/plant_pathogen.html
    sha256: bcd30e60142c6639d204624f36977561acef2a0d5a011a60d535d93e94c13eb1
    role: context
  - path: pages/traits/ecology/predatory_bacterium.html
    sha256: 14ebdbba04276bda90089e96a998fe9ab0615a7ada913576078beee6d876144f
    role: context
  - path: pages/traits/ecology/rhizosphere_association.html
    sha256: 7ac64a6426f29b81b7d9f3b6dbd7244791abcc212af64f429a8657c1ded96b8a
    role: context
  - path: pages/traits/ecology/saprotrophy.html
    sha256: 7edf663838ec40822289d827fc73f2310c96eab540bac4be479e8dfdca5b2bc2
    role: context
  - path: pages/traits/ecology/soil_dwelling.html
    sha256: 4fea97d4e496646f8194ace9d23cbc9c028d9b52ddfb4485f10ad17acc1d3395
    role: context
  - path: pages/traits/ecology/symbiosis.html
    sha256: 77037f83241c7b96f010c5644e372473d9a57e7c885747ab0aed83629bf053af
    role: context
  - path: pages/traits/environment/acidophilic.html
    sha256: 6f0f5bc97faf1968a9932071c43ff5bbd39e30a6ef0d1b2bd4bdd3368256e137
    role: context
  - path: pages/traits/environment/acidotolerant.html
    sha256: 5206184ca51507c59558f06551ec67c24304f4092f864788164343c2242ce981
    role: context
  - path: pages/traits/environment/aerobic.html
    sha256: cd1b99331947ed917693148365ca4e26e6f04920752cb24404c865b6884db655
    role: context
  - path: pages/traits/environment/aerotolerant.html
    sha256: f1dc90e13cb909e6f2c83b10ab5e29b911defaee5aa28fb06dc691bd51c16398
    role: context
  - path: pages/traits/environment/alkalotolerant.html
    sha256: 0f509894b3945e3a0c45fbcc970c5a9a9f7c61f41f5ab4724e2071c9bac3cca2
    role: context
  - path: pages/traits/environment/alkaphilic.html
    sha256: d4e89ba67dd49ba5476e00523df09cfdd7bf0737d8d6766f6dde0befe8520b13
    role: context
  - path: pages/traits/environment/anaerobic.html
    sha256: c551666a908572622f5c3cb11c82e144f7200e0f541c5990ba18ffef4e77043b
    role: context
  - path: pages/traits/environment/arsenic_tolerant.html
    sha256: a5ca96655df081180ab56d0976dc5cc2ececcfa7d8de0ed507bf6f6852464e7c
    role: context
  - path: pages/traits/environment/cadmium_tolerant.html
    sha256: 9cb7075b9fc96eb103bf916854cb8f36aa4b4524bec0956e6f38fb28909c9459
    role: context
  - path: pages/traits/environment/capnophilic.html
    sha256: 04244266b7a90278537acfa291c62e6d93ea69f71db391ffe8a50707bf7c58f7
    role: context
  - path: pages/traits/environment/cobalt_tolerant.html
    sha256: 0a1fd080728c472c5de115c2f43de0ec27e9469c876bedc9a9f79648e1eabd47
    role: context
  - path: pages/traits/environment/copper_tolerant.html
    sha256: 06ad52eea9abc17592e8e6cbbf6d821d90adfee31b15b70976002814754d93a7
    role: context
  - path: pages/traits/environment/delta_phenotype_with_numerical_limits.html
    sha256: cd5100d5ae1b670d877c172dd19424998ef1135f30f35a1e19266d43da0cb390
    role: context
  - path: pages/traits/environment/desiccation_tolerant.html
    sha256: ccbbc1cd531b801afc333f29ba3ad06397b731910b059302912910d64b718b1b
    role: context
  - path: pages/traits/environment/euryhaline.html
    sha256: 0573359e9637b30030bec86f48e1e32f3556b9f346c83781dba45205eaef124b
    role: context
  - path: pages/traits/environment/extreme_hyperthermophilic.html
    sha256: ac4f7461c4d170c2539b9849e9027370e2c3d072701237374b07de1967a00ff0
    role: context
  - path: pages/traits/environment/extremely_halophilic.html
    sha256: ac391ad87687e6f1c3852ac5155d9d6b6ccfdeb6014bb3c00fc463e2424962bb
    role: context
  - path: pages/traits/environment/facultative_oxygen_preference.html
    sha256: 157cdd570ec4f016a529b789d754a143d030df9458605bf3b1d4ded6cd9fc688
    role: context
  - path: pages/traits/environment/facultative_psychrophilic.html
    sha256: e494bf43716ca544fc4f2e872ea544e297dc2c6fca27231a6940619d9ca2ea4b
    role: context
  - path: pages/traits/environment/facultatively_acidophilic.html
    sha256: 92886b1676d32a7faa15382cd1664eadd1ce310501a5d34820ed73a7831a4d5a
    role: context
  - path: pages/traits/environment/facultatively_aerobic.html
    sha256: 8a2bac16e72c1e40064a48a69e1e8abe93209d4acbf6d069ac26d12a5cd5babb
    role: context
  - path: pages/traits/environment/facultatively_alkaphilic.html
    sha256: 00897ad39a8e90efa9f339a1f2b7c72a6f9ce57ab27be8e8c61873586ef5f16b
    role: context
  - path: pages/traits/environment/facultatively_anaerobic.html
    sha256: c621b5cdf6fa19faaafbe508eb4cb8cb9c08ebfca1e7427abdde9953af0d4f74
    role: context
  - path: pages/traits/environment/growth_range_phenotype_with_numerical_limits.html
    sha256: f0d4998b2a9ac3e0fc5948fe4ee5c9032ac442a9cd2ba6f585779619b7372859
    role: context
  - path: pages/traits/environment/haloalkaliphilic.html
    sha256: a8eaf8ee005cad366a56c457021dbe6be1edc57c2891d289ec9d8c618cfcc799
    role: context
  - path: pages/traits/environment/halophilic.html
    sha256: cd82dba07b0ebbd7f6eaee2e862e5b463f5744f305732d243497effa3a453656
    role: context
  - path: pages/traits/environment/halophily_preference.html
    sha256: feeab9b6d367d17041ce512d976e34bdbc1a610e869397a8c25b2048f3985eda
    role: context
  - path: pages/traits/environment/halotolerant.html
    sha256: 4fd63b3910092c693c2fb1dfcd39f5e743f31b8d9231edfb8ca9ea6364821597
    role: context
  - path: pages/traits/environment/hyperthermophilic.html
    sha256: 2c3989c34855df6298d4332235bdc42ec9ebffcd29be930d0fc66196c913f1f3
    role: context
  - path: pages/traits/environment/ionizing_radiation_tolerant.html
    sha256: 742872944811cb9806824a0ca78114a11a4de7ece8575cb027b3ce5363596ee5
    role: context
  - path: pages/traits/environment/mercury_tolerant.html
    sha256: e834b935e52c49ff15376e1542733342d294dab285eba9a3a3aa231e78debd92
    role: context
  - path: pages/traits/environment/mesophilic.html
    sha256: 4b521afb5268bc0ca169008f763157bef5d884a81523e27b4dc6f118b21e232d
    role: context
  - path: pages/traits/environment/metal_tolerant.html
    sha256: ce96b0447e8012ea6bbf620e0ae030af59f94b528853f65ec0b60a6bfab97ea5
    role: context
  - path: pages/traits/environment/microaerophilic.html
    sha256: 5d0de28320c6e1dad2130a0d75a4e2adeb5cc2536e98cbe7e968f010922eca19
    role: context
  - path: pages/traits/environment/microaerotolerant.html
    sha256: f8e2dcfbfa84989b72cf8efd4bd1e6ba985a7161edd40bdbde93530c55c4b9f1
    role: context
  - path: pages/traits/environment/moderately_halophilic.html
    sha256: a8b242aaa88cb97418884839a47c81a9f9e81578bea5bd8390622a918e9db5db
    role: context
  - path: pages/traits/environment/nacl_delta.html
    sha256: 8231cef6977387677f59eec6682e4c60af251672d2f5c6551572f0ef1f1a648a
    role: context
  - path: pages/traits/environment/nacl_delta_high.html
    sha256: 8115662f8bc2e1fdfbaa5bd377c2c2dc4bc1cccec62869100a1f99f1f6889878
    role: context
  - path: pages/traits/environment/nacl_delta_low.html
    sha256: f3bfec6e9dba8813e98944283568dc73bb80d77aa7e8d2ed70de230bcd208d4a
    role: context
  - path: pages/traits/environment/nacl_delta_mid1.html
    sha256: 48dbea528763a463ece2628ec8590bcf2a408dd86837a690ea942bf9217e0f30
    role: context
  - path: pages/traits/environment/nacl_delta_mid2.html
    sha256: 73a7ef2554ecfc983601cfad80142006e27fa796a9445cea543c79ea2d5c63dc
    role: context
  - path: pages/traits/environment/nacl_optimum.html
    sha256: 1f3642371b2f458a1cf168bead2a59dd09c3aafc7fa2d93a14e8a799de87ef45
    role: context
  - path: pages/traits/environment/nacl_optimum_high.html
    sha256: 706d5b312188939f00df6ac57278ffd5e897e98ca294d383dfa836763f09b1ae
    role: context
  - path: pages/traits/environment/nacl_optimum_low.html
    sha256: 331145c3f1e3ba0f7f54241a3b8d44cda8882e0cc8ba0f476253ed6cea309051
    role: context
  - path: pages/traits/environment/nacl_optimum_mid1.html
    sha256: 92b3295c5ad5449daa565ee2e4d9351fb1d3a24643fc68165d7405c369db7563
    role: context
  - path: pages/traits/environment/nacl_optimum_mid2.html
    sha256: ab3b7002c63d328b586d41e4d11b95b2f205e1f437d0109eee30b0802e644c3f
    role: context
  - path: pages/traits/environment/nacl_range.html
    sha256: 692effd198969eeaf6bc476171a55f5e152a7e35dfce38f3e3770a63fdca4613
    role: context
  - path: pages/traits/environment/nacl_range_high.html
    sha256: 9b1c1625edea2bed03ba77a324165d11530613faa12881ea8bba827c66129041
    role: context
  - path: pages/traits/environment/nacl_range_low.html
    sha256: 60f845746734be25dae8d68da3d1951060979df31a191c34fa78373125b80f74
    role: context
  - path: pages/traits/environment/nacl_range_mid1.html
    sha256: d6ca571e679f74312feca1c6c47ebf4c74f1a3ca5266eb949a67718cfe825b03
    role: context
  - path: pages/traits/environment/nacl_range_mid2.html
    sha256: 43917efe4371b8c4662044b46b82dbd5204bd66e9c8957b49749cdfe7cc926a0
    role: context
  - path: pages/traits/environment/neutrophilic.html
    sha256: 4b33d2d4523b0a1f191bc1a5aa3dd61ea6024a666034a3e30a3b28a3bacd9d09
    role: context
  - path: pages/traits/environment/non_halophilic.html
    sha256: 2c90454cee8923074a9d13a17f7ff192be71d4b1489d3427d1562cc69bd3a4f2
    role: context
  - path: pages/traits/environment/obligately_acidophilic.html
    sha256: 84a97e382626762068916a763d667eca430f09b10d850258cb58339d869fd89a
    role: context
  - path: pages/traits/environment/obligately_aerobic.html
    sha256: 59d9018e44a3960bd197c7de02a1dff509dbd4463d78dbaf6d74856c4fde3eca
    role: context
  - path: pages/traits/environment/obligately_alkaphilic.html
    sha256: 66b6d8576e9fa62477b6b4c214f832c783f721111e0b0bb0d77bd1ac08510599
    role: context
  - path: pages/traits/environment/obligately_anaerobic.html
    sha256: 37c1ac1886326c437da1b107d7df06d9985898c638f8b8545791a819e642cdcd
    role: context
  - path: pages/traits/environment/obligately_piezophilic.html
    sha256: ea13864edc04e44abbca9b5fe4693caa5fa9373dfc3f0dc204c4537213a0e39a
    role: context
  - path: pages/traits/environment/optimum_phenotype_with_numerical_limits.html
    sha256: 5754030a22edaaa3345127147f3f2cd52375cb475c9469a159826b86f39f1d45
    role: context
  - path: pages/traits/environment/oxygen_preference.html
    sha256: af649ae0432371c7e361b0817958e039d4678c9f4b5aaa3eb43c7c048c034327
    role: context
  - path: pages/traits/environment/ph_delta.html
    sha256: 4944c043be171c6029e98c0d7febfa160365d925dea7893ada9a37f366fbda84
    role: context
  - path: pages/traits/environment/ph_delta_high.html
    sha256: 3bf5e9ea898dde202ab59ddd82cf7c226fbd5a022bf273c0c6342aa2c9848372
    role: context
  - path: pages/traits/environment/ph_delta_low.html
    sha256: c1841418993c6e117801f87e55a6297f586f397262d2df7c8fa3f1c04d9fefa3
    role: context
  - path: pages/traits/environment/ph_delta_mid1.html
    sha256: ce9a0dd03830975f2af90d28e9de9b6bd4a650c25a2c0329a814eec73a611c2d
    role: context
  - path: pages/traits/environment/ph_delta_mid2.html
    sha256: 876db9415d411da0f0e271ed9f6b05cb25455cbc080a146d9970eb8911469520
    role: context
  - path: pages/traits/environment/ph_delta_mid3.html
    sha256: c2f7079b3038e6f82105d253a6b36c40af2e40008b9c2cf597dc91cc02286c61
    role: context
  - path: pages/traits/environment/ph_delta_very_low.html
    sha256: 8d593ed979ca48ce0b6818212fa12d16e49e0a6f9bc7c051075bf5a1283f8250
    role: context
  - path: pages/traits/environment/ph_growth_preference.html
    sha256: 71a0883cc8160b7e4f8bde444c8e50e77928df501b48c6e553e78a63399921d8
    role: context
  - path: pages/traits/environment/ph_optimum.html
    sha256: f784e8423ff47851064e411d40d4f7a87bd9ebeb75b43eba12f207f03cc05d03
    role: context
  - path: pages/traits/environment/ph_optimum_high.html
    sha256: 07cc7ae0932e576d7fa910795a1e120b9b171fd6aeb6751f125ec05fc275196d
    role: context
  - path: pages/traits/environment/ph_optimum_low.html
    sha256: 984a8e3fddda99f64cb33ecf20707db3a992ca7b44f4b180400530b21ca68e80
    role: context
  - path: pages/traits/environment/ph_optimum_mid1.html
    sha256: 30a70e8d427d44876a3666c77b5a9faefe1ead8819689d5c10f64922d1612ff7
    role: context
  - path: pages/traits/environment/ph_optimum_mid2.html
    sha256: 82270c761c46c2162e88418c30beea494c160bffe3aaf6d22a83808e1ad1f67f
    role: context
  - path: pages/traits/environment/ph_phenotype_with_numerical_limits.html
    sha256: 5b09c267693102bcdf55fa3aa3cc512d7815845aa3df9fec1722178711d5d3f0
    role: context
  - path: pages/traits/environment/ph_range.html
    sha256: 2f6e96fa724a61ca1b736f9c9ff30774285c4be0d41509a2672cb9005ef4c51d
    role: context
  - path: pages/traits/environment/ph_range_high.html
    sha256: dc1e3b1f592d59b106da43daeb00119f83ac2884afb3e441f893a630cd7e7804
    role: context
  - path: pages/traits/environment/ph_range_low.html
    sha256: b3f3cc6ffa9063f5f25861bdff73eac75ba08f0ecc5735fa26bf3f8c4e9ad438
    role: context
  - path: pages/traits/environment/ph_range_mid1.html
    sha256: 35f2b4b7313b033c58385674bf053a43ab9acfabaecdefe05fe2e76b4e8e6d2d
    role: context
  - path: pages/traits/environment/ph_range_mid2.html
    sha256: ef1f2938c180116e6b996ca57f5181743cbc659adbcfd60dc9acb484ff8095f9
    role: context
  - path: pages/traits/environment/ph_range_mid3.html
    sha256: 38ed63a866d865590ec0c51ea767bf763ff0feba5ef303e6991e1e6cf1b2b303
    role: context
  - path: pages/traits/environment/ph_range_very_low.html
    sha256: 6537bb141362fc68dc0732d511dbb040e85ae546e63de609ce77653fc716c19c
    role: context
  - path: pages/traits/environment/piezophilic.html
    sha256: 860619042d87bd0538f7981d74c96c136aa4a1f273eec6dc0e5b8d2bca07ac8c
    role: context
  - path: pages/traits/environment/piezotolerant.html
    sha256: 72f2432bf93ab5b0db5e43c989fe87b6bb32530c3c9cfd14033d542e07a82b73
    role: context
  - path: pages/traits/environment/pressure_delta.html
    sha256: e2658dee7417cdb104f128cd994fa811f7c5cbfa7978a398c31f6abc0b7b6651
    role: context
  - path: pages/traits/environment/pressure_optimum.html
    sha256: db39256fd949c3ef87a4bd086b962ec0716d543178340a38e178090836f4e3e9
    role: context
  - path: pages/traits/environment/pressure_range.html
    sha256: 3050188b8698ef2eb24a9f0ace930d25b8f434ff79cee0d0179e044937143512
    role: context
  - path: pages/traits/environment/psychrophilic.html
    sha256: 85820ba1c1a7e7eb63d11be51a082737b172e7ea1d4ece373d865da76080220c
    role: context
  - path: pages/traits/environment/psychrotolerant.html
    sha256: fe4fc84321663f002b3a129ce8209356abf6535c348570e9c4bc1504fe187d48
    role: context
  - path: pages/traits/environment/radiotolerant.html
    sha256: b98a5e1aa9fbec7bae737abc7855016bee64c2174e520f0ed6f1df8c942247c2
    role: context
  - path: pages/traits/environment/salinity_phenotype_with_numerical_limits.html
    sha256: 4e2058ae51e14bac6346f9708a3076581b9694381dc671339fde96c3d446cd39
    role: context
  - path: pages/traits/environment/slightly_halophilic.html
    sha256: 581dab1555a1396172648c7a44c1d0f45dcb3200942e8df4107f66c680ef7cb4
    role: context
  - path: pages/traits/environment/stenohaline.html
    sha256: c1720b7295daac98037c45f71646c3c90824909873b5e4c78415b7a35863a422
    role: context
  - path: pages/traits/environment/strictly_anaerobic.html
    sha256: 0aa95a8e1e4425f537c3a0b1e9792144428167b4af5877bd8fa1f838fdccf9de
    role: context
  - path: pages/traits/environment/temperature_delta.html
    sha256: 53e42087006de8cc5cae92c6e6ed46e18d835382ee817ed1205d93a15977a00d
    role: context
  - path: pages/traits/environment/temperature_delta_high.html
    sha256: 89944c2c0ad465e1bb06bec93a6f2060bb29574197c68ab925dcc201c17f9e1b
    role: context
  - path: pages/traits/environment/temperature_delta_low.html
    sha256: c99d428d445dcdf0a23a7c55b15753d0def570b4a72f1cd94d1a7fea56e17482
    role: context
  - path: pages/traits/environment/temperature_delta_mid1.html
    sha256: 48e6c4c12c56c3352506facc6f43bc1fc9b4b97d6cf957b0c43d7a01d05fb64a
    role: context
  - path: pages/traits/environment/temperature_delta_mid2.html
    sha256: 118ae6b95875c70c976ebd2d3b3f35309d16063cc6c57df502918020571a3ec5
    role: context
  - path: pages/traits/environment/temperature_delta_very_low.html
    sha256: ced6b5b4fca52a02e95dd2cbabd6086525b8f6dd4ec87ff5a45b439834df7bcb
    role: context
  - path: pages/traits/environment/temperature_optimum.html
    sha256: 93a988d7fd1a464c1b8fc6b1167db99e495ac1a52f32f14c7169262feb5d90d8
    role: context
  - path: pages/traits/environment/temperature_optimum_high.html
    sha256: 626884cb122919851adee0839129b5fa5b40b3adcd6dc875eaeaf4c41a974782
    role: context
  - path: pages/traits/environment/temperature_optimum_low.html
    sha256: a4227c18450f6e6f21af08baf57199e023860bcbe720125440f60cc4c081d14f
    role: context
  - path: pages/traits/environment/temperature_optimum_mid1.html
    sha256: 2107892647a40462f4558d22f4134edf7023947f943e6f49b577c2c727e35af0
    role: context
  - path: pages/traits/environment/temperature_optimum_mid2.html
    sha256: 4bccc2239934c488ca76e85062f18ad4f32aeda20f1d631b58749d7ad34078ec
    role: context
  - path: pages/traits/environment/temperature_optimum_mid3.html
    sha256: 01487187458313fa95b1d9cd26ad5ffb25f146836b7d4494da5bd3ec9df95f70
    role: context
  - path: pages/traits/environment/temperature_optimum_mid4.html
    sha256: 171c2434227da82b367ad0191d03cdd04774a53c4be148780913f391007d0f72
    role: context
  - path: pages/traits/environment/temperature_optimum_very_low.html
    sha256: 5c0fa2c1f8a89bb6c39c784e7facfc2e195f5d4af003cd9f00a2f3a481a24bd7
    role: context
  - path: pages/traits/environment/temperature_phenotype_with_numerical_limits.html
    sha256: 6bfccf293173d7e77738c743aa48452af4d49162594bb9fdd4e97eee455f4dce
    role: context
  - path: pages/traits/environment/temperature_preference.html
    sha256: 9a6161e6b67f894457695b0e29b2a22e0fba9490fa6bf58df8eb3cd5fd404c44
    role: context
  - path: pages/traits/environment/temperature_range.html
    sha256: 722d0512331666c32bb573e21d3e11b91b01441182e295cf49e1df8b14e49b52
    role: context
  - path: pages/traits/environment/temperature_range_high.html
    sha256: f913b72aaff41620b65508f944a1927e8c2b48e5ff38faef1a669ce82a1d24a2
    role: context
  - path: pages/traits/environment/temperature_range_low.html
    sha256: c8fd03c2823b94dad3347ef2e5f6c6ae8b06c5e26e47823d221232a19414c1b1
    role: context
  - path: pages/traits/environment/temperature_range_mid1.html
    sha256: 0ea7c5df6ee0e5b6151d520852bdd9ac7729f4a5f1c45d3218e6fe6bdfcf13f0
    role: context
  - path: pages/traits/environment/temperature_range_mid2.html
    sha256: dc209b71e65498fc948a480187702160014f688306aa2e1ab885fe69ddb86907
    role: context
  - path: pages/traits/environment/temperature_range_mid3.html
    sha256: 0c0804d17a8dbae3e3b79164ec6d563c75ce561500cc1fc99463936c5d24369b
    role: context
  - path: pages/traits/environment/temperature_range_mid4.html
    sha256: e9e052d6cb8e23eb17e77157c781eb1cb143538fc71e8f6df46b85cd48e47583
    role: context
  - path: pages/traits/environment/temperature_range_very_low.html
    sha256: 06495072bf25fb6319d65ea2478418a1c5e2c6e3b3dcc24dca74c2e561840128
    role: context
  - path: pages/traits/environment/thermophilic.html
    sha256: e6121e29e89b99d600a5ab5ec96b4cf988eccb67ef7b6d3e52d02c200d9b15f4
    role: context
  - path: pages/traits/environment/thermotolerant.html
    sha256: 754d66be486b0a62ead95e44cacaa6cbc6480895aa8cdc6aca5347ca1d3a4ba5
    role: context
  - path: pages/traits/environment/uv_radiation_tolerant.html
    sha256: e7e41c0ff03feae0f228e263413eee1dcdd536036a7d24d65a7915e2cca645e8
    role: context
  - path: pages/traits/environment/xerophilic.html
    sha256: 551bb86c35adec069e9a3c494212a478ba583f5c996aee975dc1969015db63d2
    role: context
  - path: pages/traits/environment/zinc_tolerant.html
    sha256: 6b50adde5d793c751949dbd64462eb477faee1f43aaa7cb1a57e17b6551cf986
    role: context
  - path: pages/traits/genomics/abi2_system.html
    sha256: b540fc7eb3cf1f0b5da5c17dbfa3db5988ef6dda209fd78e2fdb8dab3b80e820
    role: context
  - path: pages/traits/genomics/abia_system.html
    sha256: 19661c3161319340644c7ee971d89f6c8d97a11875d3a6f646aef9e18b986891
    role: context
  - path: pages/traits/genomics/abialpha_system.html
    sha256: bda9e5880b4e7c6111de299cbb2a8c1a8a35b92fa9d1f92f18ca195846cf4648
    role: context
  - path: pages/traits/genomics/abib_system.html
    sha256: a6d93479bca7a2293a342006fb5ff29e9e997d75bb7c95a3035e1859ff82c46e
    role: context
  - path: pages/traits/genomics/abic_system.html
    sha256: 914557dba1c36a2d7f492aa8579c862f786c00cd3e696593bc4d1ce61510a7cc
    role: context
  - path: pages/traits/genomics/abid_system.html
    sha256: 8ec9e0acdd044893a07990b6e52458303d19b15561926b044a3e30c014320a3d
    role: context
  - path: pages/traits/genomics/abie_system.html
    sha256: cdb9bf99547e2beacec9ad6b00e6d7ef01bf8329eae5fb441cd01bb993fce072
    role: context
  - path: pages/traits/genomics/abif_system.html
    sha256: fa66eef70a74b6e9bb4ee170a7eb9a4745954ff50e68dda5a38a88d637148a8d
    role: context
  - path: pages/traits/genomics/abig_system.html
    sha256: a6b674cca55c193c005141b768c814ae38037dc99a3a745e347eb6deab6a92ac
    role: context
  - path: pages/traits/genomics/abih_system.html
    sha256: fc3e263e72574ceade4cd64c64931925da8d55bdf785cad9dcb8b155b193e6a3
    role: context
  - path: pages/traits/genomics/abii_system.html
    sha256: 3e1ce2811d237e31bb58d6459fe480d6914d4b32e8c5b688716f96920e00e1b8
    role: context
  - path: pages/traits/genomics/abij_system.html
    sha256: 2b96f86cfa72c4bec3b3a23d5850093ebac112bf2deb2c464a3c1830aa8293d9
    role: context
  - path: pages/traits/genomics/abik_system.html
    sha256: 1f70a71577ad4bc1268254bb976cb960adc865f1468bff99b2e01f3422d2b8c3
    role: context
  - path: pages/traits/genomics/abil_system.html
    sha256: 5c5a69477606dba489c4d6066e5448f741b3cfbdcd362ded33e0a97c7175d1a9
    role: context
  - path: pages/traits/genomics/abin_system.html
    sha256: 0bc0ee1344298905b301d992cc4b62eb53fce71f54be71c0b7eb1cc9a6122583
    role: context
  - path: pages/traits/genomics/abio_system.html
    sha256: 6abaab64382521afecc1d44df79641c7ce94604c06033f14d24109b650535e2a
    role: context
  - path: pages/traits/genomics/abip2_system.html
    sha256: 91c32d769b80e0a2ff3e1e9212ae44c416f8a8407a7ee2f1abd3e8aa2329b6ef
    role: context
  - path: pages/traits/genomics/abiq_system.html
    sha256: 3062e4b7e45ce25e2d50296058a8a0fd8f4f062783c3670f6dbbb6b40e5c539e
    role: context
  - path: pages/traits/genomics/abir_system.html
    sha256: 53ed988b1e14634d3f6ed8746f818ea487aa6f4f22e620e8a9972bb78472ca12
    role: context
  - path: pages/traits/genomics/abit_system.html
    sha256: f345c4f1fe9851905218166158e63139358fa61d36ef68b0005423a38f07a684
    role: context
  - path: pages/traits/genomics/abiu_system.html
    sha256: 8860cf94398669d69012443e3a7d2549e2eec78ae4df608db738589e427487c2
    role: context
  - path: pages/traits/genomics/abiv_system.html
    sha256: cbd45de434d696cc05f23542d7b32317ad7e4fd2f00fa5c381b38989f1088d82
    role: context
  - path: pages/traits/genomics/abiz_system.html
    sha256: 672ac06222714effbd1b45afbefce4cb42d218eb3440a4d4623043e97fcd4e6a
    role: context
  - path: pages/traits/genomics/abortive_infection_system.html
    sha256: 962a11cade4f23b60e2d1511fbafdfbce82a00439f85c0f32e45acaf96e6d673
    role: context
  - path: pages/traits/genomics/aditi_system.html
    sha256: 8ab68753e0629ef8e846909013121f5bc1a163f1317e135797e75974be1c8790
    role: context
  - path: pages/traits/genomics/ambrosia_system.html
    sha256: a61d9f75701408916a088e5ef4f02c56604e15ef0aaca194dbf3bc1feace40f2
    role: context
  - path: pages/traits/genomics/apsab_system.html
    sha256: fd1da897c319826d42203aab9236f612575862ac36e36aceee9257b1be6f5c3e
    role: context
  - path: pages/traits/genomics/aristaios_system.html
    sha256: eaa5de3a44033fc94d2774418c18242e403b60e9d3d623d941c48c3f503b64b1
    role: context
  - path: pages/traits/genomics/armada_system.html
    sha256: 88d0342444e10651b16d560874d98a560046fe17d32128045a9943a91ba8e64d
    role: context
  - path: pages/traits/genomics/audmula_system.html
    sha256: cfe202d0a3f3adfa8a2c630a05d4745436c789f7e2cdb7578a7c653f1ff449a8
    role: context
  - path: pages/traits/genomics/avast_system.html
    sha256: 363d8343fdb349706206edea7830d101c5bd580ef9cefd6df9005e1c87cf6a73
    role: context
  - path: pages/traits/genomics/avs_i_system.html
    sha256: b0cd2c1f227bdd7efca2eef7c9353dee8123cedf865b68e2b8c408afd6cbdc38
    role: context
  - path: pages/traits/genomics/avs_ii_system.html
    sha256: a698a67cd887844acc0bf57a326fbc30d6240c222ccf1295d4e5a4aa90a8bd93
    role: context
  - path: pages/traits/genomics/avs_iii_system.html
    sha256: c252b509e0704a1b540125b0d92ccfd86bff202311dc03a11209f1b88105889d
    role: context
  - path: pages/traits/genomics/avs_iv_system.html
    sha256: efc5caaed6415922dcdce05aaaaea74970fcb345327077045459da9b9d11ed3d
    role: context
  - path: pages/traits/genomics/avs_v_system.html
    sha256: 14777f04f431e3abb4cde0614dc61a92f983f12deb1d9d7bb9d0cc17b223befa
    role: context
  - path: pages/traits/genomics/azaca_system.html
    sha256: a025caac558baa10ac9c6ebb96b18f844e6fbeb5a76f5cdf9f7e1c8e7fb5e155
    role: context
  - path: pages/traits/genomics/belenos_system.html
    sha256: 3fc64e8a497e19af64c9391453932aa3687d4aa4feb5ac6b84cee9cbace09faa
    role: context
  - path: pages/traits/genomics/belisama_system.html
    sha256: 3d70531400f88df108747a18645b912f0dd5b68de32cb762919e45ea252c50fa
    role: context
  - path: pages/traits/genomics/bil_system.html
    sha256: b1ae02624ace61cf9e8aff04a8e6875d18beadb5e2606b77c0c12002d37720c4
    role: context
  - path: pages/traits/genomics/borvo_system.html
    sha256: 8de1b9d3afb1639d4268fb7353aa5ceabbbe3d6f406a360666dd7cb55b639a27
    role: context
  - path: pages/traits/genomics/brc113_system.html
    sha256: 663f21b2379ab91e4454aeb430e1256282678150998facc5dd5f94d5ec92f3a6
    role: context
  - path: pages/traits/genomics/brc142_system.html
    sha256: 5ebae3a1f00dbd4a2611433b96d361ced783f44a06acab59f681d8e14cdf78f2
    role: context
  - path: pages/traits/genomics/brc167_system.html
    sha256: 1bc0eeedec6d148edd1784cfe3eab4da2559964cfcb6ba1bb3cc6d3b627e61d1
    role: context
  - path: pages/traits/genomics/brc217_system.html
    sha256: 75d14a440eb8dfad215618729da7c61113c7a9b391531d18676af468ccc92b8c
    role: context
  - path: pages/traits/genomics/brc22_system.html
    sha256: 538f7ae4dbc3952371802110bb2fd2a42617ed6f934b8527f4500bb592a5061d
    role: context
  - path: pages/traits/genomics/brc233_system.html
    sha256: b2a62ae7f3a1ec72f0db2f52117e8f1feb9ef731355278c35e59812d9f767981
    role: context
  - path: pages/traits/genomics/brc23_system.html
    sha256: 27a61b349771c93d84ebae187e019209e53a6198a80c32df3e32ca4d0f163913
    role: context
  - path: pages/traits/genomics/brc24_system.html
    sha256: 4f240b9849dbde5a99b294c94a27674987a00837e90b005255678494598b81aa
    role: context
  - path: pages/traits/genomics/brc59_system.html
    sha256: 6b3e05368379066bcf3e5a2adf76437fc31755ac12efb2dc349261c9ca387618
    role: context
  - path: pages/traits/genomics/brc76_system.html
    sha256: e168979d83f652358cd6bdb70228e81a3d422a106feff1deea2c4d1e944c2211
    role: context
  - path: pages/traits/genomics/brcwgs21_system.html
    sha256: 2a27d98d902b74bbd6f62f1311d215fb7a1a57175a746073634651145ba20758
    role: context
  - path: pages/traits/genomics/brex_system.html
    sha256: dc3165413a7f0d7e8de986da26df89bcdc46a20fe414761b9c83c8ef7c02b854
    role: context
  - path: pages/traits/genomics/brig1_system.html
    sha256: ee3be0c4461bdd779035e4e8b51e6fa610a80066fbf1571d8e0605b87b6905bc
    role: context
  - path: pages/traits/genomics/brigantia_system.html
    sha256: 62cfd2e311ce15677b039ae0c1d44784fceb018b3d1a12423d86d5ddb7863289
    role: context
  - path: pages/traits/genomics/bsta_system.html
    sha256: a3a742464e013d371b87fdc7a9b58b5d7d62d4886e5c0bc127b8b4cd05ccdefa
    role: context
  - path: pages/traits/genomics/bunzi_system.html
    sha256: 226dc99bee9bcddd179c83c778cb38b51a75a0c462d534c08a42e3c807ae384b
    role: context
  - path: pages/traits/genomics/butters_gp30_gp31_system.html
    sha256: 961d0336a3276c8ad936da61afd0b3865e7551e09e98f4db187b0c495414a766
    role: context
  - path: pages/traits/genomics/butters_gp57r_system.html
    sha256: 381188382cf78c83733d76d503d55a8651a5a4e53fbbe16c907583c235650ef8
    role: context
  - path: pages/traits/genomics/caprel_system.html
    sha256: 64a58c151b1c60fe9641c2c61eb79d4136d25f133f80a819e6788d9db4c64e72
    role: context
  - path: pages/traits/genomics/card_nlr_endonuclease_system.html
    sha256: 321e30174d6fc7557063572ee9342a1ea939bf48cc5f21ec8c928737d59831c7
    role: context
  - path: pages/traits/genomics/card_nlr_gasdermin_system.html
    sha256: 384a9191a0e3eca7e0791d50f2740112f69c09017b5f9b2d7f541fc174365ce9
    role: context
  - path: pages/traits/genomics/card_nlr_like_system.html
    sha256: 7b2e80a3bd4279d3a5037d88b35b0ca938279b107310d40b8d4d8605fa7c83fe
    role: context
  - path: pages/traits/genomics/card_nlr_phospho_system.html
    sha256: f8fdd788ff8aeead2634c2aef897ab7edd9e9296d61401dbcfe4d9be2a52f12c
    role: context
  - path: pages/traits/genomics/card_nlr_subtilase_system.html
    sha256: cdbd690b5d56bc62e3ca1f356f2a07910d2deb92667380934bd85302c1379151
    role: context
  - path: pages/traits/genomics/card_nlr_system.html
    sha256: a62216468df6c6ae62bb64999465b979cf5782d7759bf923ca740e0d15194828
    role: context
  - path: pages/traits/genomics/cbass_system.html
    sha256: 007c0ad807c05913007c8414fa95703fbabd654bbfde0ce47c41c44bf572e140
    role: context
  - path: pages/traits/genomics/ceres_system.html
    sha256: 75b1645eeb17089726dcede1037c0e696e9cb3e7a8726580c937cd1f170f08a5
    role: context
  - path: pages/traits/genomics/cernunnos_system.html
    sha256: 740855d1ec4859e15ac5111508328dd0004d77de99ea8a280f1641e8666e9365
    role: context
  - path: pages/traits/genomics/charlie_gp32_system.html
    sha256: be06544bb04c03813d76256fc862ecae8f3e879817afcaced6bd357d56c02266
    role: context
  - path: pages/traits/genomics/clover_system.html
    sha256: ee4e0357b96296f35c8cc52d01150bda3dc8fb20487958a4dcb1b13f82b1d065
    role: context
  - path: pages/traits/genomics/cmdtac_system.html
    sha256: 8dc41d0813fd34831e4baef47001224ade878207779ad3c97e20cbaeb38a37d1
    role: context
  - path: pages/traits/genomics/coconut_system.html
    sha256: 1ea9f4fdaf27f87306fbfafc1ea18742fa1e9962bbc76db3b7371a9c16311765
    role: context
  - path: pages/traits/genomics/codon_usage_bias.html
    sha256: de1ec38c2c5ffd0fba1832e2340b4641477f17a7876770e8986114ef3165f2e8
    role: context
  - path: pages/traits/genomics/crispr_cas_system.html
    sha256: f7d53fd7b089623c8ea9d5d78de8b9922b0a47657ab4da8ecbd594edff1a5d0c
    role: context
  - path: pages/traits/genomics/crouga_system.html
    sha256: 6b93d137aeee8f8b8776961726939fd26553ba1e060149f627217e7843e06e7a
    role: context
  - path: pages/traits/genomics/dag_system.html
    sha256: 69d285dbe555186ed8bb8d1e4c4dc0483954d853154738867e57bbd5f20f18a4
    role: context
  - path: pages/traits/genomics/damona_system.html
    sha256: 2712e7b143cab3ca596fe3262c00d0a1418cb745335fe674e73a217d25ee7b53
    role: context
  - path: pages/traits/genomics/darna_system.html
    sha256: 7aa0b32b25991d763ffbda9c1f8e4a5e4873ae3931df04d9d4ae4793b6c04f71
    role: context
  - path: pages/traits/genomics/dartg_system.html
    sha256: 665545d08385273b7fdd228b74b8bce56e85e4461c7c8f50fddd9fd420396b79
    role: context
  - path: pages/traits/genomics/dazbog_system.html
    sha256: 5b52d3de37608e3e9071292fc2eda10b4b01ba2ebda7b1a2c471fb1e20a092e3
    role: context
  - path: pages/traits/genomics/dctpdeaminase_system.html
    sha256: ed66e98d0b0e9d69c35df485ebee588085bb6c832cd5660d8fb70dd8ac428e05
    role: context
  - path: pages/traits/genomics/ddmde_system.html
    sha256: b54fbf960f4cbe66d938372dc0252a96fd91722e841ab18a9b0872355f75839a
    role: context
  - path: pages/traits/genomics/detocs_system.html
    sha256: 7003aaa10fcda96f554113a80d96e45357c53a10fb79a1fb9b0ccc6f637af643
    role: context
  - path: pages/traits/genomics/dgtpase_system.html
    sha256: 804b6a37bba075349216d60904809683d7fb47971762426f65b6d7d3ccc561c3
    role: context
  - path: pages/traits/genomics/dionysus_system.html
    sha256: 681028ee0475848137eb0fbadb3ae727c4de0fbb686ce7473aa027f25a93427b
    role: context
  - path: pages/traits/genomics/disarm1_system.html
    sha256: 0b8d0187b6f09ec2ab5f5cb32c4bc4240b3bc2013aed2a986f877bf903d02370
    role: context
  - path: pages/traits/genomics/disarm2_system.html
    sha256: 642a9d8dde3323040aed290dcc60bdf48dee0e93dcb03db908565b69199c0087
    role: context
  - path: pages/traits/genomics/disarm_system.html
    sha256: ed9a57d650cc01825dad130ffe5c7aa83be76646a20bdc86e4adaa2b0a78b8ab
    role: context
  - path: pages/traits/genomics/divona_system.html
    sha256: 49d83dc2e94b19034f0c4b0e9421079d859fab86e7b2a5621dbec9806fad560d
    role: context
  - path: pages/traits/genomics/dnd_system.html
    sha256: 49403e9937b4d70a61006536fa91c8357deff35cae71eab9c1273c55c048bc3c
    role: context
  - path: pages/traits/genomics/dndcdea_pbeabcd_system.html
    sha256: d02765e254fdb597235ec6e80c001d8d1d724582e814c0a2dbc849d561bc4058
    role: context
  - path: pages/traits/genomics/dodola_system.html
    sha256: 44415e2ff13886f8bd323c1d51118935c374b78aac4517f58e06866992e253f4
    role: context
  - path: pages/traits/genomics/dpd_system.html
    sha256: beb05c28bbfeb09c102dfdf3f21f313bcc8de5192f85512603d13fba119eeed0
    role: context
  - path: pages/traits/genomics/drt1_system.html
    sha256: 867217a2595513fa0137b51a542c39d86dcc7ce912951c385018309a67605bff
    role: context
  - path: pages/traits/genomics/drt2_system.html
    sha256: 4878b0e881c70df08c3589fb24467a9f62c2cd5bdf244a9cc2deebe0400f7fed
    role: context
  - path: pages/traits/genomics/drt3_system.html
    sha256: b2413dcaf22419cafac8653e26cba1f625ca4c3644039ad3723f9f56ca513bc1
    role: context
  - path: pages/traits/genomics/drt4_system.html
    sha256: 4bcda327eec8479560cc536512115278e3ed992bd7d97b158c6f86551d56aeb4
    role: context
  - path: pages/traits/genomics/drt5_system.html
    sha256: 6427d8d591330a0f95388b9291ffab7f03b8ec345bd5aec12a7d1d58721c8848
    role: context
  - path: pages/traits/genomics/drt6_system.html
    sha256: 9373c693a5d0f63f161ca0142e39a99f673e5bd0bde1d1d8503851904dee012d
    role: context
  - path: pages/traits/genomics/drt7_system.html
    sha256: ce4b244bd9c1d640650278e855acfda7990ff100d5e7ceb917f4161d019640a5
    role: context
  - path: pages/traits/genomics/drt8_system.html
    sha256: 00849f92e72eb67d13ff3d347b2f3742a0dd927e05c3990955bdc7b93e5fad43
    role: context
  - path: pages/traits/genomics/drt9_system.html
    sha256: fdec469107e9aa38afcb01b3949df1247e19bdb563f9472d57f33c3d315442b5
    role: context
  - path: pages/traits/genomics/drt_system.html
    sha256: 22db2da42e3a4b8cb639b6d33539a23c71620957e0f6294deab1240b0b3dca18
    role: context
  - path: pages/traits/genomics/druantia_iii_system.html
    sha256: d4067276c40f950d256935451e96c16a225cb0d668519ee41c4d792058efb8da
    role: context
  - path: pages/traits/genomics/druantia_system.html
    sha256: 1f0d28cce57918bf034b46396a745e202b727e3e06275fe6ab4eedb499bf7e31
    role: context
  - path: pages/traits/genomics/druantia_type_i_system.html
    sha256: 3db6605e0c1d165cad2d72db977cf2291a699fb3353179e4c43526a1b7a54dc5
    role: context
  - path: pages/traits/genomics/druantia_type_ii_system.html
    sha256: ddf5a1ebd3604e8e1cc945be1e3f497fa9011740455caac6164bbd97077f8f15
    role: context
  - path: pages/traits/genomics/druantia_type_iv_system.html
    sha256: 8ecc90fff6f240cd6d0ed0577679ee13ec7d797a2a104316560e13410c55e098
    role: context
  - path: pages/traits/genomics/ds_10_system.html
    sha256: b75b44946520170e7d95859e1f4f997b2acf0398a9eefa3bdd98d991c9b37244
    role: context
  - path: pages/traits/genomics/ds_11_system.html
    sha256: d009a668b5222bd1bb41b05b77a1c09816fb35764aca9b0bebf40dfb3aa272fb
    role: context
  - path: pages/traits/genomics/ds_12_system.html
    sha256: 18a0e5a5b88dbf201f7bb1732ecd0d76c9956f3a6950925b07351c8e9db1812f
    role: context
  - path: pages/traits/genomics/ds_13_system.html
    sha256: 7a29626f444877cce27ad90e3f71505ccedd1f5400a2873dee06f30fb10e7674
    role: context
  - path: pages/traits/genomics/ds_14_system.html
    sha256: 781cb46a5be0184a07a91972b375becea052b2acc3ac430a136a2cf6704cd6f5
    role: context
  - path: pages/traits/genomics/ds_15_system.html
    sha256: 618dc4a6e93b1d42211b2622f4509cacc0df88e27795bb0c1f89003f28ae91b0
    role: context
  - path: pages/traits/genomics/ds_16_system.html
    sha256: d85e25d725373c3fb553cf91b180575296fcc825d134fae5df27b5d99cb442d6
    role: context
  - path: pages/traits/genomics/ds_17_system.html
    sha256: 7606cc72fe150a1d2b8273d9b8c31742b15c9b62a88253a3d2cd9d432dd91296
    role: context
  - path: pages/traits/genomics/ds_18_system.html
    sha256: b68d198358c3c9fc986890771146079eed28a3ce9de06013122f28d5116b0c7c
    role: context
  - path: pages/traits/genomics/ds_19_system.html
    sha256: 738aa5510c9c26d9fd43d6af7cde97bc1b528d772e13662aea0c98550fb07b60
    role: context
  - path: pages/traits/genomics/ds_1_system.html
    sha256: 32bec2d40d5f8b6b4766102aaefdee15ee30ecadeab769ebf550c3d68f6f271a
    role: context
  - path: pages/traits/genomics/ds_20_system.html
    sha256: cbdfa32174be476bca657b71f25edde8090181618bf1d9a6b65359aa8bc4013a
    role: context
  - path: pages/traits/genomics/ds_21_system.html
    sha256: d313392d20750d3e554f19a3a7c47b4150663512b5e1f6306998475bb90b1331
    role: context
  - path: pages/traits/genomics/ds_22_system.html
    sha256: 05fa0256493e995c0008f5c3557654b5acaee2a29af09ff19f8c93307c72f8f4
    role: context
  - path: pages/traits/genomics/ds_23_system.html
    sha256: 72cbf7abcebd8864ecfa0a4f24e7fa9df3ddb953827aac43dcc39128bbf068a1
    role: context
  - path: pages/traits/genomics/ds_24_system.html
    sha256: 60a8fb715944bb0f5a1e695ead7fb113e1b5db7e2e747cbe79e52543cb220f5a
    role: context
  - path: pages/traits/genomics/ds_25_system.html
    sha256: 7c34a810f22209e501971d6b8bc901c615636a346767d42a69f138491deb8e6f
    role: context
  - path: pages/traits/genomics/ds_26_system.html
    sha256: 38ea633b506b1f6f539727845ad94255a2e1b399e5541b7f07643752290d4122
    role: context
  - path: pages/traits/genomics/ds_27_system.html
    sha256: da48d23f9e4d687b68a307f950ba8e615dd63a644381a95a89aad8b6caf8101a
    role: context
  - path: pages/traits/genomics/ds_28_system.html
    sha256: acf5c1021ad5bc574d89ac4d7cb180f19806684e9c1cefc26b8487b498f8adf0
    role: context
  - path: pages/traits/genomics/ds_29_system.html
    sha256: bad3ddc0c21b75da0ffb188119e3650c0d0c2e3b45dca7bc7d9a928f5ff0bfdb
    role: context
  - path: pages/traits/genomics/ds_2_system.html
    sha256: 443fbc7c0c3bb1e0570392384997f42bd60253296269fbd1eba489c79ab439de
    role: context
  - path: pages/traits/genomics/ds_30_system.html
    sha256: 73c976b7bf015b06108ac50d076e6afb87d3b76e6245ca0f7ab0df529e4ae2e8
    role: context
  - path: pages/traits/genomics/ds_31_system.html
    sha256: 9af145296a8a7abc421c1b36abab363316fae7b22fc47e1da6643bbf62d6c8e4
    role: context
  - path: pages/traits/genomics/ds_32_system.html
    sha256: 96148c786c5c3e11a928699d3f80ddc6f6ae8da9f514ff066f233159ac9c1ef5
    role: context
  - path: pages/traits/genomics/ds_33_system.html
    sha256: 4a23186a907c7cb8c0a90d99b8ef7c006a1992500f4a3600a4ac8b0514392b93
    role: context
  - path: pages/traits/genomics/ds_34_system.html
    sha256: 93faaa6f47a8e297d5c45341f110fc0ec508eaf2b37a4bd40fa5608e4def6867
    role: context
  - path: pages/traits/genomics/ds_35_system.html
    sha256: 85059c78bba247fedf2d72e351eebac02e287c0e166efc55604e895ca7d79203
    role: context
  - path: pages/traits/genomics/ds_36_system.html
    sha256: 07adaaa9cfafd2324b9e92a2df10014f439914019f3318e6dc618ba2bcdbbbaa
    role: context
  - path: pages/traits/genomics/ds_37_system.html
    sha256: c8bbb14c97d990ed075acd93be12e583f546e841b9f2e69ac015cdf022e83029
    role: context
  - path: pages/traits/genomics/ds_38_system.html
    sha256: 553e9c6d75c5287f7b910b7fdd4bb7586bcb3fb576cad0b245ed29539b14e1ba
    role: context
  - path: pages/traits/genomics/ds_39_system.html
    sha256: 35bdba8e175a537bdbe3891b3b62ad1ea26f7b67ba36eb573b196787c2397ef7
    role: context
  - path: pages/traits/genomics/ds_3_system.html
    sha256: cd2b5cba7bbaf0a33b258c70fb1bb46217cf8270838b8017aff47befbf0a23d8
    role: context
  - path: pages/traits/genomics/ds_40_system.html
    sha256: ad5749a1d5c4225256813a791f08e3abfa776fe11601d04a26253f18f950fd0f
    role: context
  - path: pages/traits/genomics/ds_41_system.html
    sha256: b46a057fdfb175f86216f103947117606495f722238b4557b792b1a1b9d38bc1
    role: context
  - path: pages/traits/genomics/ds_42_system.html
    sha256: 71ba995d16a370f3a6aa8058c0374ddbeb745ba9cd01a2c0976c518b62dfde7b
    role: context
  - path: pages/traits/genomics/ds_43_system.html
    sha256: 53c1d6c2db29c5bd60132c3a68644b5c88ea54e39b0682d81c7109eb65f8bcfa
    role: context
  - path: pages/traits/genomics/ds_44_system.html
    sha256: a199a86f2469186f8355431bf32431d4934d54272fb7cc1bad2501f5e9a36b15
    role: context
  - path: pages/traits/genomics/ds_45_system.html
    sha256: 76b398e4010961865e9482ec52cce06e66de0297beca8cdbadbfd4c98720a512
    role: context
  - path: pages/traits/genomics/ds_46_system.html
    sha256: 38877a54468c63aae3a0b752b2c0b32371dbd8fef0fcb4c4fdd5eb6beaa2b44f
    role: context
  - path: pages/traits/genomics/ds_4_system.html
    sha256: eed6f5f184ecedbe9c6df1510b2e327e76e2e9c51a06c09231be467192fa706c
    role: context
  - path: pages/traits/genomics/ds_5_system.html
    sha256: 4ad405b6c592c31350fb47efbaa230e8aaf641d402b039848ffa20f45aba889b
    role: context
  - path: pages/traits/genomics/ds_6_system.html
    sha256: 784a3261a1a3bfbe708a5da4d5db93a01c034e66257b3655d941f5ca17ac91dd
    role: context
  - path: pages/traits/genomics/ds_7_system.html
    sha256: 468b338442fef9b09c7191c2c570b1ae92313bf7290e084cb1047026f79558f4
    role: context
  - path: pages/traits/genomics/ds_8_system.html
    sha256: a4c45316da0ec6c52810e331c37dea346814b2167ecc2a340748777a79a7e0fc
    role: context
  - path: pages/traits/genomics/ds_9_system.html
    sha256: e2e2bd48d1e3f3083004b55677f81815cfd3ef94876dd6e5590b479c526ffc28
    role: context
  - path: pages/traits/genomics/dsr_system.html
    sha256: 6ad581cd8e8af20debd3164e0a27320d60a6a6962c00ac51b167c8d9d9d6ea74
    role: context
  - path: pages/traits/genomics/duf262_schlafen_system.html
    sha256: ed085c360bd1f207982cafeb10461fe959d0f25ce2629d46a3a04d2eb6a7e02a
    role: context
  - path: pages/traits/genomics/ecokmcra_system.html
    sha256: 8a3c8a105061c245a854636f3489b56e0636d8f5ca0d64aee4e90b1f38218d6c
    role: context
  - path: pages/traits/genomics/eleos_system.html
    sha256: 11fb4742d00cfbc09cb6f64b0d6651d027f5278fbe56e98ca9ab238cdd861676
    role: context
  - path: pages/traits/genomics/endpacf1_system.html
    sha256: d612f33c6f5613e48e84ff41e7794491d00d564afca1e5daada1a1d00e2f9511
    role: context
  - path: pages/traits/genomics/epona_system.html
    sha256: a22b1210817fdc6d1cd8b0d8d936a906ab8c891aa2fb2670ec968f9ae0aa317e
    role: context
  - path: pages/traits/genomics/erebus_system.html
    sha256: d6d1d8e8f159e60033b09f6152f95e592f293b9652cb4dca12760b420c23061d
    role: context
  - path: pages/traits/genomics/esos_system.html
    sha256: f0a7545d9096be952e96ae99ca34d958c652681ffafbde9603d7ee9e6b8cdbd4
    role: context
  - path: pages/traits/genomics/fliodhais_system.html
    sha256: c4c487b8aad6b2d30c7d68efcafaf7d8816c0209029080ee7af9d20f9398172f
    role: context
  - path: pages/traits/genomics/fs_giy_yig_system.html
    sha256: a4fcc93ac7bdf91dcb78c38e465a2cecb22d79212eaf9716953125e7f68f87a2
    role: context
  - path: pages/traits/genomics/fs_hepn_tm_system.html
    sha256: 7d27ef4da9a3042b47a9b78c3bd8a3e3fe2130b5c042c4789b6889351181cba2
    role: context
  - path: pages/traits/genomics/fs_hp_sdh_sah_system.html
    sha256: 30ad834abeb65fe8e4d44b6d843b4c25a701b1b5a9aa4d1e96524abe4990eede
    role: context
  - path: pages/traits/genomics/fs_hp_system.html
    sha256: 2ed743e29eb7b25e8a57db8b72c890cb5894c4da8ed5bc71e7ae0a15894a07d9
    role: context
  - path: pages/traits/genomics/fs_hsdr_like_system.html
    sha256: b59d806702b0f957e8d0eea21b71f7ca567f04b832ab38f301fd8b79fc930fd9
    role: context
  - path: pages/traits/genomics/fs_sma_system.html
    sha256: e7381365f1ddabcd036de3c150f71306325d31c7a80e2f362149d5c89ce0dc6a
    role: context
  - path: pages/traits/genomics/gabija_system.html
    sha256: b06c5fc52d057bc73c7be6ef74af8f7465ec6baae877913d76b6cd942c6b7351
    role: context
  - path: pages/traits/genomics/gao_ape_system.html
    sha256: f3694fe417af1fea3d929558909da036e35ade467889115224796301e5474b85
    role: context
  - path: pages/traits/genomics/gao_her_duf_system.html
    sha256: c4663332701b8a4b77c323d2a057c18cba3b5fbd9a9f65327f70ea270b066edd
    role: context
  - path: pages/traits/genomics/gao_her_sir_system.html
    sha256: 1e34511427d1483da4ffb596c696e081d2751163a13ab45b9b2b85838b27c4a5
    role: context
  - path: pages/traits/genomics/gao_her_system.html
    sha256: 32abbf41357a2a5883b03f13ddff89298c37cb77da479dc4363d5af1a8845d05
    role: context
  - path: pages/traits/genomics/gao_hhe_system.html
    sha256: 56a77792b057660225740ded71d2dc7fdb371b7c1e8e74ed466809afc0030a5c
    role: context
  - path: pages/traits/genomics/gao_iet_system.html
    sha256: b473efc769e319fd08fbf1d718232cd8d0f734042860ae76e273ef4703d37f43
    role: context
  - path: pages/traits/genomics/gao_mza_system.html
    sha256: 17d88704b02e33346d67dc1a64b87a8befa92aa645135cf3ec56a51beaea48f5
    role: context
  - path: pages/traits/genomics/gao_ppl_system.html
    sha256: 91510bc6b9f180c620c8fb3c4e40aa0b0de9b4d2e35160344902e5ff28914a7b
    role: context
  - path: pages/traits/genomics/gao_qat_system.html
    sha256: f46a9e078231259a2e899ceaf56daf0c28bff27a365ee7d67ef9df9c6b613333
    role: context
  - path: pages/traits/genomics/gao_rl_system.html
    sha256: 4e6ef8e873641f66b64d523bbe87bcfdc913d24be1230abab8345649e44f9478
    role: context
  - path: pages/traits/genomics/gao_tery_system.html
    sha256: 49daf7f55879f8ab880b439e8ba1ecd33a5d35402aaeff1e683d7572355b47e5
    role: context
  - path: pages/traits/genomics/gao_tmn_system.html
    sha256: a0032fc1f67ea3768d478c25c438019395305ce1c79a467eaa3aa702133753e3
    role: context
  - path: pages/traits/genomics/gao_upx_system.html
    sha256: 2dbb3700d4c4481d71fbb7943ed254539dcfe269cc049c2acb573f029113f566
    role: context
  - path: pages/traits/genomics/gaps1_system.html
    sha256: a8273168a1e19f8e26b175c02e5c4f58f1bf520ca843d5c2a2f34efaaed2b5dc
    role: context
  - path: pages/traits/genomics/gaps2_system.html
    sha256: 3fb95129a1383c5b256611159e9fe2cb052dda615eaae4b2e3edc149c60e0e2a
    role: context
  - path: pages/traits/genomics/gaps4_system.html
    sha256: f572b49186fd098dbaa88eafbfd9f080634022b878aa6f153d071dba1b7da332
    role: context
  - path: pages/traits/genomics/gaps6_system.html
    sha256: b799f3d3fe7e2679b28e25643c2b27f5e1ea9985d26835c4c909e46a9e0247cd
    role: context
  - path: pages/traits/genomics/gasdermin_system.html
    sha256: c6661c246e8167a6e2cac2aa991083c415ac6be54b6e446654dbfe7334c3b7f9
    role: context
  - path: pages/traits/genomics/gc_content.html
    sha256: d88997950a2c4eba5e0d9b6a3a3fd4c57c48ac4089521caac423b520a9462d1c
    role: context
  - path: pages/traits/genomics/gc_high.html
    sha256: dba4c7de29302436b03d68c35d489ea83ad57917a438bb5a8b5a6a25ea9eae08
    role: context
  - path: pages/traits/genomics/gc_low.html
    sha256: 9656f80c70dfeeb26b9df5338bd8ae4e2deb2e4c18674b524a62d5a578dc5d37
    role: context
  - path: pages/traits/genomics/gc_mid1.html
    sha256: d7a80f3a3724e221e47e3a07ac6c427415e9a91ca897175743607f3c1337a862
    role: context
  - path: pages/traits/genomics/gc_mid2.html
    sha256: 2c12ef654c722fb2910a0386123db078430af4a02e888ce5e849e8d5afefeeae
    role: context
  - path: pages/traits/genomics/gc_skew.html
    sha256: 982edb922c1f534918147487ecbbe72626b1a7ae900b4bc8b36fef78e91f0a89
    role: context
  - path: pages/traits/genomics/geb_system.html
    sha256: cf065398fe56eb3bde2c8a4c8f3121d996a0d776be610b1a2fef54463bbd4a25
    role: context
  - path: pages/traits/genomics/genome_size.html
    sha256: 534c869cdc12f913fe22b45dee27a9c1578d9db5b71e83dff64451a72b4fddc6
    role: context
  - path: pages/traits/genomics/genome_streamlining.html
    sha256: 30add2872d0fabdcf8efb6da899a80829e80a8ad8fc8ba9ff6e196baf784b11b
    role: context
  - path: pages/traits/genomics/genomic_island.html
    sha256: f44b61eef90f7941ea3ee746b3de7928f72b932850a66ef64b7f8b6ec9bc08e4
    role: context
  - path: pages/traits/genomics/gmrsd_system.html
    sha256: 0673b6bc203cf9c44420639f4e5f646e854eab20668b35c962b14219fb9b18f7
    role: context
  - path: pages/traits/genomics/hachiman_system.html
    sha256: dfc1d444408a51c4e91de6eb7e98f642ac610c51fb8dff4290a5686cadaadc04
    role: context
  - path: pages/traits/genomics/hachiman_type_i_system.html
    sha256: 773595480af63a948ac55c70355cfc8e0b5b05056dff37eb15b462a997b1f8d2
    role: context
  - path: pages/traits/genomics/hachiman_type_ii_system.html
    sha256: 592b0443b8152165c36a45f8044ea62b1531ff03cf217ae9909d027d4cd51551
    role: context
  - path: pages/traits/genomics/hailong_system.html
    sha256: 6e2e63fe786bb5c8c460268be50d46d4aab4ab31dc9b7184829737fa54cefc7f
    role: context
  - path: pages/traits/genomics/hec_02_system.html
    sha256: 84f82c715e9b0bb8a6c4c7b63ce57bb3910d7c9616b8eaf199b61a75e30c617d
    role: context
  - path: pages/traits/genomics/hec_03_system.html
    sha256: d78d8712ddd5544c01106a2d432e2ac0708e3f5057cfdb026cf043d1965087f1
    role: context
  - path: pages/traits/genomics/hec_04_system.html
    sha256: f738f8b3afe3a37913bb93aebfcd12bc23f1a1548cd7536127d8cdacd965b165
    role: context
  - path: pages/traits/genomics/hec_05_system.html
    sha256: 50f1c42abd2080b28b706dc5750a43652c79809fc8a12899b7d51f700e45f368
    role: context
  - path: pages/traits/genomics/hec_06_system.html
    sha256: d39d19079e7353d044c3cde94edef0df2ff7c7004cb0ee6466eba2f20e556438
    role: context
  - path: pages/traits/genomics/hec_07_system.html
    sha256: c8c872c6257d59163bcfaa6cd2f5c273922e34e7bffee1f628c4bbac8c5469a1
    role: context
  - path: pages/traits/genomics/hec_08_system.html
    sha256: ee12f17ba8dbf57d3280e302f7f0007b654e49f9c44ce551c8db27cccc9e1299
    role: context
  - path: pages/traits/genomics/hesat_system.html
    sha256: 27249af85a6d269b6d952741b040180abe53bf4c41bd0a5b7d9e403756aba820
    role: context
  - path: pages/traits/genomics/heterokaryosis.html
    sha256: ae4d21e371d4e856e4531ee348b2bec1833bb2c02e246c52abb65e754a10b984
    role: context
  - path: pages/traits/genomics/hma_system.html
    sha256: a23e47579b9695cc03001e751980e11e8c6088ba17a686af7e9259e965563a95
    role: context
  - path: pages/traits/genomics/hna_system.html
    sha256: 2b8e32799b915844a00a1f37dc9b9a2b5f9c269af05d460be3353438fd60bbe7
    role: context
  - path: pages/traits/genomics/hypnos_system.html
    sha256: e1bfe9804339adea61c2bd3ebb9aa0c2bf71b90618b0de14bc94ca29f34891c3
    role: context
  - path: pages/traits/genomics/ig_like_schlafen_system.html
    sha256: af01a095bac4df3da20ac328e2fe89751822ee9ba1f0ab8382f1badea5b9d20e
    role: context
  - path: pages/traits/genomics/integrative_conjugative_element.html
    sha256: fa343f47beed822a83025a1b6f07ed81f3cb42771c774ed898eb0eb74d97c183
    role: context
  - path: pages/traits/genomics/jukab_system.html
    sha256: 5c85eb33a050f75b3093a664fe3a6865f34401f5e86213384c9b60d5584eaae2
    role: context
  - path: pages/traits/genomics/kamadhenu_system.html
    sha256: 02177fa6494694ce686e433a69e4c4770ad9b88a1376c7b2b15f1224b8e9c549
    role: context
  - path: pages/traits/genomics/kiwa_system.html
    sha256: 68fa8120a26652e8c1135025d8c36e92ec8fe9962ee7da1d3d94380cbf7440c7
    role: context
  - path: pages/traits/genomics/kongming_system.html
    sha256: 04e033e393354e7f707a9b55b2230671965dc3f78f1a56bb77c54f433d435135
    role: context
  - path: pages/traits/genomics/lamassu_amidase_system.html
    sha256: 69a3ae9af66284d13eab09c82c5337155eb393df1d80307ccaeb9ff314c95af0
    role: context
  - path: pages/traits/genomics/lamassu_cap4_nuclease_system.html
    sha256: fca1546612c6d88588a4e4d899d081ba89d2811cd23cdb1b728f529d9b77206e
    role: context
  - path: pages/traits/genomics/lamassu_fmo_system.html
    sha256: d51859f8f49b499fb4852feadaabb291884897444f75ee2ecdf128c44ea761cb
    role: context
  - path: pages/traits/genomics/lamassu_hnh_system.html
    sha256: cbd3fb68c1e25b71ca3bb5191038ae735029a16380a321c9c7cadc569ed72bc8
    role: context
  - path: pages/traits/genomics/lamassu_hydrolase_protease_system.html
    sha256: f1f3f04ea1ff7ff3684109faedcfed152dbaf8363b1455ed558a13e6ccbfa209
    role: context
  - path: pages/traits/genomics/lamassu_hydrolase_system.html
    sha256: 8eee003e93a359807a038e3dae837ececefb189529906118d65035f28329c3b9
    role: context
  - path: pages/traits/genomics/lamassu_lipase_system.html
    sha256: b3631822b8fd8a235cc0e46649bcc28af3cf4a1ccb12b59a670559c64b0d41ec
    role: context
  - path: pages/traits/genomics/lamassu_mrr_system.html
    sha256: 468a9267f6f93983778a4efc29d06686811fd1aea582b8f2640168398e918fd8
    role: context
  - path: pages/traits/genomics/lamassu_pddexk_system.html
    sha256: 864320cef551676d73427eb5efa51b18698fd59c2cd6aa3f49748138665923fd
    role: context
  - path: pages/traits/genomics/lamassu_protease_system.html
    sha256: f579666800a1e8ce4cf80ff76b675a328022b4814ddeb1465a65e77bf6a4db96
    role: context
  - path: pages/traits/genomics/lamassu_sir2_system.html
    sha256: c9846efa4fe3e1952cfae960e14fdee8c48bea8a584711c80bf3e56806be6b5d
    role: context
  - path: pages/traits/genomics/lamassu_smek_system.html
    sha256: dfd0a839e0ba3171b7643e45dd76e86867d0d0769a75fd470d2b429c0ed159d0
    role: context
  - path: pages/traits/genomics/lamassu_system.html
    sha256: 942af2a14959bc0934950a61dfd434a860862b3c9efb01e71517a34e1d1e7b91
    role: context
  - path: pages/traits/genomics/lamassu_type_i_system.html
    sha256: 367a9c3ac44388dd8e6eadb10f20fe22f5a7a5d06c86055395eacfb99828f893
    role: context
  - path: pages/traits/genomics/lamassu_type_ii_system.html
    sha256: da49254a1bf4f579124e08f12e20ac7c17cc8ef7b827073ab7b29597045482fa
    role: context
  - path: pages/traits/genomics/lanthivirin_system.html
    sha256: 2002fe95a0609d074c39fc789953533b61c8a2293d5534a043128ee6cf3a05c9
    role: context
  - path: pages/traits/genomics/lit_system.html
    sha256: 6385a2f185109ec7f717d21f19fb0a8a48e60b56c17fe5bd6c7199632fe5bfea
    role: context
  - path: pages/traits/genomics/long_lamassu_system.html
    sha256: 2e00caadddf1cf9fce6755279eeb599c59cc63b9025d259db9eb9105b4a5ba82
    role: context
  - path: pages/traits/genomics/lugos_system.html
    sha256: c4141ac9dae63c85a6c9c7e678d02f6f03e8789c97cf50613e6e401c1900beb6
    role: context
  - path: pages/traits/genomics/mads_system.html
    sha256: 451e6647d69301d9d25f51cd900d94534248e85a93fc83958d84ceb3da037d07
    role: context
  - path: pages/traits/genomics/mazef_system.html
    sha256: 97934615d0d82b55b4ab062d958c9601ed4a4f22bd4eebb31d3b98601285373d
    role: context
  - path: pages/traits/genomics/mcrbc_system.html
    sha256: b2d36e2dc5e95a932389daf9415b4bcd7de84d64abab8b5b4f06280025be1061
    role: context
  - path: pages/traits/genomics/menshen_system.html
    sha256: fbd112356fa7e4b9f94742d37276dcd23bdd028dd8c0afacff1ff9a6b53560d9
    role: context
  - path: pages/traits/genomics/metis_system.html
    sha256: 7c2314e99925f1699ad2000e0cf0400cfa67beab32eac28f099158737e2edf71
    role: context
  - path: pages/traits/genomics/mksbefg_system.html
    sha256: 4108da78403341c867b45316c0ebc736069e2c5decb67c28b20c4f424f42b9fc
    role: context
  - path: pages/traits/genomics/mmb_gp29_gp30_system.html
    sha256: a7dbd27861fe502358531a15029abd5225f96752a83af2cf87930d04af4a7239
    role: context
  - path: pages/traits/genomics/mobile_genetic_element.html
    sha256: c0b8668b2a9c39ad412a6f06d9ef1c11eae99e1a1ccd28204e2fe103b2a39a47
    role: context
  - path: pages/traits/genomics/mok_hok_sok_system.html
    sha256: 2b3b9e641e3c2c785a87368237afdbef5b1b9cb4d8d5477e96f14da94379ec04
    role: context
  - path: pages/traits/genomics/mokosh_system.html
    sha256: 890645c5eec2c22a383afbb84a2d0b5c7abe1222228ae9a0eb7dfe1b11c68687
    role: context
  - path: pages/traits/genomics/mqsrac_system.html
    sha256: b165b8379effb3a885e8da7676a74c049561427db5732dd37cc5c264b10a0dee
    role: context
  - path: pages/traits/genomics/mspji_system.html
    sha256: 0babc0e27d9a52abfc7503f06e4c0e89416b8534a634bb024b65e13b7ebd0670
    role: context
  - path: pages/traits/genomics/nantosuelta_system.html
    sha256: c2514e38e8af0c84b365b41dcfc4b7adadc9cb06ba50d6f148297fb925042aa8
    role: context
  - path: pages/traits/genomics/nemetona_system.html
    sha256: e213188d9f6f442616bb85c5b6bb84047a7df0f8c2f212c7759d398efcef7336
    role: context
  - path: pages/traits/genomics/nhi_system.html
    sha256: c8b0270b06289653512173c3c86c3d13ffe131a2ebea05a6c0de34a0816663ae
    role: context
  - path: pages/traits/genomics/nixi_system.html
    sha256: fd08a3d71cbaaec6cd54de9400abeff17dab6c22ecbcb64ea886582d26aaa8ee
    role: context
  - path: pages/traits/genomics/nlr_like_bnacht_system.html
    sha256: d0211a2899667a4f42d612276d4efb8cc8a731aa97e4edfeedb2237320fbb305
    role: context
  - path: pages/traits/genomics/ogmios_system.html
    sha256: 6f2a9c9e2dd96698d4c137380dd099f36a4e4c1f8bac0fdb6b20c6100a07edce
    role: context
  - path: pages/traits/genomics/old_exonuclease_system.html
    sha256: 55c81622959bae90476a9c626c4c94221636121550b246414f03d55c134caf44
    role: context
  - path: pages/traits/genomics/olokun_system.html
    sha256: 53dd5d4e90ba145b72941524a610f07d3c31dfd8985ad5cff928c3ab48f79e9c
    role: context
  - path: pages/traits/genomics/ophion_system.html
    sha256: 0367f76d51b113af7fead49990ad6022dcae063c97e0242fbef29f258865c0e0
    role: context
  - path: pages/traits/genomics/oshun_system.html
    sha256: d2b7a7c4028a24f718b493e0aa25420bb962d45bbf7328251e284fb40e3fc346
    role: context
  - path: pages/traits/genomics/pago_system.html
    sha256: 36998445f161827c89a83c77f2371b52c3dc6829ec03e1183c957bcde54eb975
    role: context
  - path: pages/traits/genomics/panchino_gp28_system.html
    sha256: c9046d6ac5a0362e4a68fbfcbab01385df989b711371eee210a7fe9e451d95a7
    role: context
  - path: pages/traits/genomics/pangenome_openness.html
    sha256: e8b57007c8648c653838a6bb1f7e21ad06e82f05258467de8d768c74d7ac0e0c
    role: context
  - path: pages/traits/genomics/panoptes_system.html
    sha256: 5f4b269e220bff75cddf2ae7d412671dd0ebb000b5d0cd984c1c8c2a4091d5e1
    role: context
  - path: pages/traits/genomics/paris_system.html
    sha256: f52401538426498ffaac45714a7d1354ba4e3e8fb9fdb5d16eeb267b1ffc701f
    role: context
  - path: pages/traits/genomics/pd_lambda_1_system.html
    sha256: a416d14582332638c1840cf2fe46e4df863e1b9014058746bb5be19436e38b0a
    role: context
  - path: pages/traits/genomics/pd_lambda_2_system.html
    sha256: 5494e1e2781099f806d0fcf6492f9de1a815b2ff225dcf1ae879e15f93fe2b82
    role: context
  - path: pages/traits/genomics/pd_lambda_3_system.html
    sha256: aaaa832e90b9b54eb5776ec3b199a9ef1190493a7b40574747dd70688c081067
    role: context
  - path: pages/traits/genomics/pd_lambda_4_system.html
    sha256: c291de6d7b856ddd1298f598cfd2f6890e1cbce38d52d68a11c816e0999b42ca
    role: context
  - path: pages/traits/genomics/pd_lambda_5_system.html
    sha256: b780e876f34acd56d29997e4ce7374211e16519b854b247aef90bd3743ae94f6
    role: context
  - path: pages/traits/genomics/pd_lambda_6_system.html
    sha256: efef391a0004b8cc73483372274c2450ebe2a8d3c8c62f0290362d27846cf83c
    role: context
  - path: pages/traits/genomics/pd_t2_1_system.html
    sha256: 5abab8c23e5dbeedd3845cdb3a12afe957a5e2ac0fb22e0e4a8722eea589b2c4
    role: context
  - path: pages/traits/genomics/pd_t4_10_system.html
    sha256: 40cfb573b26f2cd5c54f2b2b985066f2d516a6d385458c160d1b2e5b9008e51f
    role: context
  - path: pages/traits/genomics/pd_t4_1_system.html
    sha256: 9142722e590001ccd697ecf65b2b22eea03fdd7bbd7edf5aa30b4309ae5d85cb
    role: context
  - path: pages/traits/genomics/pd_t4_2_system.html
    sha256: fa873e6706de16153e95c425f99b7bb32dd8939a2e7a05b544eb795a155d6a2f
    role: context
  - path: pages/traits/genomics/pd_t4_3_system.html
    sha256: d20743ba5571b45bcc61308560cc73f5c90abb32f6e5ccd8c9295758e590996a
    role: context
  - path: pages/traits/genomics/pd_t4_4_system.html
    sha256: 84055804b431fef57eaefcbb94cac1d4bd2fd32f3d40724c75cf7788f7eaef3e
    role: context
  - path: pages/traits/genomics/pd_t4_5_system.html
    sha256: 8cc74395e71682dc53de1405d37a62d943744381174f1a1f520ffcb5af4616fe
    role: context
  - path: pages/traits/genomics/pd_t4_6_system.html
    sha256: e3d153772a2afdd97212fc4b15b6d6ef9e16bac85f167dbb7a59747e3f7222c5
    role: context
  - path: pages/traits/genomics/pd_t4_7_system.html
    sha256: 5b4d85da9c628b8cbc58ecad3a017142751b783e0d18a3e720814d9babb34031
    role: context
  - path: pages/traits/genomics/pd_t4_8_system.html
    sha256: 1ea146d86b17962298cf091b8ee39394a4fc357073df74aa83d552b221d79183
    role: context
  - path: pages/traits/genomics/pd_t7_1_system.html
    sha256: f682dcfce4ca53fa52faae77ed6bced6a40dc7190787fadd631359fa40fdbde4
    role: context
  - path: pages/traits/genomics/pd_t7_2_system.html
    sha256: 09d888da60b1c572132d776d508be45daab61bde57e08b28ea032f99a145e33d
    role: context
  - path: pages/traits/genomics/pd_t7_3_system.html
    sha256: b86e4c43b95d0173cbc2c2b40ac74289b9d3ab2dcd745efff9b317e5962309c3
    role: context
  - path: pages/traits/genomics/pd_t7_4_system.html
    sha256: 600d220a2dd4a6b5f014f132e62f2e37a87e2166fe36d7f1a419a0645f0b5f98
    role: context
  - path: pages/traits/genomics/pd_t7_5_system.html
    sha256: 65738512ef4f19812afeee222322b60013e61e3777ddf9354c7842dcc4cc0bf6
    role: context
  - path: pages/traits/genomics/pfiat_system.html
    sha256: da4d01526c76225d1e6ca1aafb3211e9e8a460b74f0eacc0b6162e2a82ac36db
    role: context
  - path: pages/traits/genomics/phage_defense_system.html
    sha256: 3c38f0c706cb489c303d638fa15ebcc6c68a8066e4a0c03c3c3b81abf0797117
    role: context
  - path: pages/traits/genomics/phosphorothioate_defense_system.html
    sha256: 1e49344bbd9539b50490446010b6ad2e9e94e8ec01b3d08d6d6a6dab4c191e5e
    role: context
  - path: pages/traits/genomics/phrann_gp29_gp30_system.html
    sha256: 0a5b04c46068b5ccf4c75692b956f6345b219b2d7e80306b92aa508f2ca74395
    role: context
  - path: pages/traits/genomics/pif_system.html
    sha256: 6c033a2d55085574edf70161aaeec92926f864bee25f229fddbf27cb573286de
    role: context
  - path: pages/traits/genomics/plasmid_carriage.html
    sha256: ba3c130f444b1e9571ff5fac92a1215c38f6a95f852e1939751edf90a15125aa
    role: context
  - path: pages/traits/genomics/ploidy.html
    sha256: ca6189fb9fbdbb2046cfad0bf971432d089b1e91195348f59fd386de55ddb83a
    role: context
  - path: pages/traits/genomics/prithvi_system.html
    sha256: 51bd76d3dbf40f47e3f9c1adcd80d6e2793e34757cba8bca4985210a62611c66
    role: context
  - path: pages/traits/genomics/prometheus_system.html
    sha256: d690c2206531b8f0fba1a71d7e16e9a68be7671df721c442ab65a5c300df5888
    role: context
  - path: pages/traits/genomics/prophage.html
    sha256: 66604f1a1004fb17b9b4a53b684604068a816e528d1922889b08fd7bacd8fe84
    role: context
  - path: pages/traits/genomics/prrc_system.html
    sha256: 87ca6d61c8983d2b32df4758cdc44965db31e71c205dd7ee88dee5b983e2cb07
    role: context
  - path: pages/traits/genomics/psyrta_system.html
    sha256: 0bd726316f9cd72a973a47444c23d4420d2b7bf33d5b15dede26b1525288eb09
    role: context
  - path: pages/traits/genomics/pvurts1i_system.html
    sha256: 66981619f8a8deb163dd8ca6becd6a8b6435f081ccfeb5755722a902e7aa889a
    role: context
  - path: pages/traits/genomics/pycsar_system.html
    sha256: eb50395478e859a7a5985613b460938c864985a10581ed07417a98fb8d69be8a
    role: context
  - path: pages/traits/genomics/radar_system.html
    sha256: 3d72541d80f5e82bf91da74cabdb7a71bb58d81a467741b8afa283ebe428b8af
    role: context
  - path: pages/traits/genomics/razr_system.html
    sha256: 20adb4e11e56d7ae655247a1ded09ef6b7b332d7e539854182a02096367f7190
    role: context
  - path: pages/traits/genomics/resolvase_duf5677_system.html
    sha256: 09ea6e1ab41ef1b31df5d798a2f6343c4c922df64797e56741963ba94b1400f9
    role: context
  - path: pages/traits/genomics/resolvase_kap_ntpase_system.html
    sha256: 144497a8ed03cfb0549a5a152ac7b2b3ddb75b9e2784907aa1930d8092eed382
    role: context
  - path: pages/traits/genomics/resolvase_schlafen_system.html
    sha256: 0c9d665a6ecb5c1377b7b8eb2e041c48f93b5782fb063324d4899b279b0e9dff
    role: context
  - path: pages/traits/genomics/restriction_modification_system.html
    sha256: 84a3a07cea2cf6defe8869019a03c79f3d774151de2d07d51109d90e35d8ea62
    role: context
  - path: pages/traits/genomics/retron_system.html
    sha256: 1956df6dbc7307e79b42989ee19d99ecaf8ee3b233d781e73e25ea4de6ea0dc5
    role: context
  - path: pages/traits/genomics/reve_system.html
    sha256: 6b5d94741135d9934ce3864ad65487487b5f69c11940407598f829a9d222c991
    role: context
  - path: pages/traits/genomics/rexab_system.html
    sha256: 33c848a528ffc41ec063b098c5cead09b454d0e5e65994d56692b999d589b87c
    role: context
  - path: pages/traits/genomics/rhea_system.html
    sha256: a9800a0c75717ae52fa457e68e7da582ccc47df7511b9823b6b187e4682734a4
    role: context
  - path: pages/traits/genomics/rloc_system.html
    sha256: 5890725787e063a987853f4436fecb6e494664fcedf1b1dd5a77fb1b154d50d7
    role: context
  - path: pages/traits/genomics/rnlab_system.html
    sha256: d27c11ec55632c30db782b7e06fcb398ea4f013be4e09db81c1deb8c131b616d
    role: context
  - path: pages/traits/genomics/rosmerta_system.html
    sha256: ad7a92fbb91f06ee0f2dd9a01b44942cdaaedcef9312dac7354675d0ec8755de
    role: context
  - path: pages/traits/genomics/rrna_operon_copy_number.html
    sha256: 26ee46b098de4d14727e9c9334df95fb0a0ad283223d8e7d1fdc4a30f3e0c5ae
    role: context
  - path: pages/traits/genomics/rst_2tm_1tm_tir_system.html
    sha256: 8c4c2cf48d08baf2f85a5218da1dc3b08055d998cacea2d8a6353964e5760953
    role: context
  - path: pages/traits/genomics/rst_3hp_system.html
    sha256: ec53f5f11994c8ef9199b7793b307bf90480733b38819653b027bbbc695f5732
    role: context
  - path: pages/traits/genomics/rst_duf4238_system.html
    sha256: 8186426ffd3a9d3be84af22b42c8f15dc984eb78cb026fc5cddafb0fe72eb86c
    role: context
  - path: pages/traits/genomics/rst_gop_beta_cll_system.html
    sha256: 718a92723c227388496a92c246030d68bb76f79c36250316ff15ce2c77a4366f
    role: context
  - path: pages/traits/genomics/rst_helicaseduf2290_system.html
    sha256: cb12b71baef8f4bc8bc41c3eebecc3ff621eda9bb8a8a49c419dbe81970bf6a1
    role: context
  - path: pages/traits/genomics/rst_hydrolase_3tm_system.html
    sha256: 1d04a874f521de5ff5d717397bcbcc3b380b123d47c5c6e31e81bc5b970cc5d5
    role: context
  - path: pages/traits/genomics/rst_rt_nitrilase_tm_system.html
    sha256: 785addfef5d54f5408c6ff802757d69a7c3822616d9f662c78b45d1c191ae66c
    role: context
  - path: pages/traits/genomics/rst_tir_nlr_system.html
    sha256: 088efc2ce6197d7716efcd6f622c893baf6efe0741c4f4416bfd44b4ca89b70b
    role: context
  - path: pages/traits/genomics/rugutis_system.html
    sha256: 8ffd503f74d81433b70c9184570165ff6a8d094e7d06eb26aa1219b08f701ce9
    role: context
  - path: pages/traits/genomics/sanata_system.html
    sha256: 7124201855cd7b373b7b1b1b152733705a1e359218fdfefd95d180245d3ab30a
    role: context
  - path: pages/traits/genomics/scomcra_system.html
    sha256: cb86298066e12848879659ec43f1b6ff0cf9ef12a43420261522d8de4ff8c6a9
    role: context
  - path: pages/traits/genomics/sdic1_system.html
    sha256: ede11e3966cd7bd0db815c6f5f629e1c236bd4673d4db89309be60d93a298196
    role: context
  - path: pages/traits/genomics/sdic3_system.html
    sha256: f6fd39edec82c892d01e06fbb6e3e8a9886da1cda43d26b3cb5f655f50de75e8
    role: context
  - path: pages/traits/genomics/sdic4_system.html
    sha256: 4dbeb09adfd241b9f6495a57e9dd12f41f972bbc82aa5eb5985bc1040593efb9
    role: context
  - path: pages/traits/genomics/sefir_system.html
    sha256: 98e0c75baf35f85e740478f5796957ba2b99b26fe4f0adcb24568c2f507afc21
    role: context
  - path: pages/traits/genomics/septu_system.html
    sha256: 42d1b6a392ab6cba367f2f38b4be765aa77d17a78bd12271c9f7c39340ee246a
    role: context
  - path: pages/traits/genomics/shango_system.html
    sha256: cd14cb8a809281fc97ec3b440f352db5544a4082ecf516ff41c0c77216f73172
    role: context
  - path: pages/traits/genomics/shedu_system.html
    sha256: 0c382aa1bc0cd02807971c70e39ff938bcc8ef326b18f72eef9c133ded384a72
    role: context
  - path: pages/traits/genomics/short_lamassu_system.html
    sha256: 6a1f4eb98f4e65792549af1370dc5840e5a1941598f26229235d697d423c0308
    role: context
  - path: pages/traits/genomics/shosta_system.html
    sha256: 33ac477093d25e2cf3892422a5285f6b852f477a0c46578d8383d0c5e34070c1
    role: context
  - path: pages/traits/genomics/sirona_system.html
    sha256: 9c4da0c697cfd91bb94ff309aa2eba3f3f2580064266293e200b86c8667b9b57
    role: context
  - path: pages/traits/genomics/six_a_mbl_system.html
    sha256: dee63d5fdb5de493670b3185278cc3381f18d71ae52c888d15e00227e521f885
    role: context
  - path: pages/traits/genomics/snipe_system.html
    sha256: d963ad2bc2e88c0d74f00ddcc59e299e8bdc9e25e132b354a807319d50773bd4
    role: context
  - path: pages/traits/genomics/sofic_system.html
    sha256: fe5441abad9d44673f16f37c87f511b808c5793f44cac2e7ffd77e57b4d29a1e
    role: context
  - path: pages/traits/genomics/sparta_system.html
    sha256: d27b80f6b1e8b37d912281a9aed62170e5937894e48ca033589fe73e3cdc496f
    role: context
  - path: pages/traits/genomics/spbk_system.html
    sha256: c97941129222d32c05654e6abda484a22c17c9a174b8dbbeddacba2e3234d259
    role: context
  - path: pages/traits/genomics/sspabcd_sspe_system.html
    sha256: d72ebd77566163f9da1d12bd788c2bf4da677738dc1258d6f912249ae688ea5c
    role: context
  - path: pages/traits/genomics/sspabcd_sspfgh_system.html
    sha256: 85794ed6d50cc2f030348f62db2d5a0938d61f3bce66ee49970ebbac3b862c84
    role: context
  - path: pages/traits/genomics/stk2_system.html
    sha256: 6fab380ec0c3b66dfa6500bd4d0b8bd32bbc9b47d722a95a1a30cacd881afe38
    role: context
  - path: pages/traits/genomics/sucellos_system.html
    sha256: ff5a90f93a251d5e6ec41998c66b8c71d8eb1b8bf44a34fa242b8232c19656cc
    role: context
  - path: pages/traits/genomics/tab_system.html
    sha256: e49f28bfcf98bc81af1b5690aebee2ac762f939bc3b78644a75da2d7534136bb
    role: context
  - path: pages/traits/genomics/tagi_system.html
    sha256: 3999b9b5c66178d32be588ef39da7d9d8d4e18f57aaeb8867e2459cd79e298df
    role: context
  - path: pages/traits/genomics/taranis_system.html
    sha256: 23622d883070c6ba68ee9e42a25c473887e7682fcaed7ab9ead1ed0e401f8b27
    role: context
  - path: pages/traits/genomics/tgvab_system.html
    sha256: 8779eb33193874730a7955dd94862cb6c8b38fce7905f59e435242ffdc2a500a
    role: context
  - path: pages/traits/genomics/tha_system.html
    sha256: 974ca5d4d3d575bb194efb3d15bd3c5ad9ed4531953ebb3bee226ba0f6908e28
    role: context
  - path: pages/traits/genomics/thoeris_system.html
    sha256: b057ed845bc329fe7afef152b6c3c47c8d8ce712011eefa4665ec400e0e3717b
    role: context
  - path: pages/traits/genomics/tiamat_system.html
    sha256: da5d5cf4a2ef47b9e9d1955a7ff182fd3d0d6f6977cf4c703d2dcf065e27f4bf
    role: context
  - path: pages/traits/genomics/tir_i_system.html
    sha256: 3115a5e357db531dc086ad7f15592a5de27f6cc2593b94799ef598eaa632c687
    role: context
  - path: pages/traits/genomics/tir_iii_system.html
    sha256: 301d6ea6285e860be7679c123037cd1ebf1668fd62e26dd9e220673870ed48ee
    role: context
  - path: pages/traits/genomics/tir_iv_system.html
    sha256: 0a53172dcff92b2827d29a95c2cb4c77a6772a1426c1a5117989c00e84c36e52
    role: context
  - path: pages/traits/genomics/tir_vii_system.html
    sha256: 48d1d8509cd1b4956a39df4b13f1e3c3df283bcd83e40863fe233fec4875e217
    role: context
  - path: pages/traits/genomics/tir_viii_system.html
    sha256: 1e265d33217f17fd241452783bf9d7f635a3b1b70d1d24087aa110f396cabab8
    role: context
  - path: pages/traits/genomics/toga_system.html
    sha256: 19043000483c01dc383a26ea89ff121e8523b484df2696524b802a47ba1b573b
    role: context
  - path: pages/traits/genomics/toutatis_system.html
    sha256: d33ee254ca9d28570c2812693d5d3a165ab8efd1611d2d460bad4de1b36bdf4a
    role: context
  - path: pages/traits/genomics/toxin_system.html
    sha256: 3dc2023efb51b0fff0341cdc3ace94c087e63e5ddd640bfc6c4b1b5657d01170
    role: context
  - path: pages/traits/genomics/transposable_element.html
    sha256: 8785b7d337810aa5ceaf47026f8ac50ed499de001317dbd161be98058374132f
    role: context
  - path: pages/traits/genomics/type_i_restriction_modification_system.html
    sha256: 4dc73d7611cadf0eaadc9c43c8ae57b6246ceb36cdda0b90bbf483960911eeb5
    role: context
  - path: pages/traits/genomics/type_ii_restriction_modification_system.html
    sha256: a97c1e5e8bda69f867066122bb3704084a8c9b15724bead757f2caf0c156509d
    role: context
  - path: pages/traits/genomics/type_iig_restriction_modification_system.html
    sha256: bf6cd0a04a71274dccba6ca3f9c962b40cbd883d8f4553a97a2f17de70ce261e
    role: context
  - path: pages/traits/genomics/type_iii_restriction_modification_system.html
    sha256: da239345856c6265a3a55bc88f48db0b7203c83b0101fe7526d12ff792c6f22d
    role: context
  - path: pages/traits/genomics/type_iv_modification_dependent_restriction_system.html
    sha256: 3e6ef4b94cd2c2d14824aefe6b6000d4dda9c9bb603b3f7ba07598b767e8d084
    role: context
  - path: pages/traits/genomics/ukko_system.html
    sha256: 3a45949fc11a26fb907eed1d13d88b345490ee9a384ef46f666f3fd484c5c74b
    role: context
  - path: pages/traits/genomics/uzume_system.html
    sha256: ebab68f9560d7a99442b15b04f4d7941632582b3001fd14d0409c991323f81a1
    role: context
  - path: pages/traits/genomics/vcam4i_system.html
    sha256: 6fc53fc970145008a1c6413fd2d47b71c9a9cb99b6b4eb23f92ab8b8f2cb2254
    role: context
  - path: pages/traits/genomics/veles_system.html
    sha256: 8a2fc0a592befe098e2564ea35755b4747eac60a8f6283a9262f5a338e835ffe
    role: context
  - path: pages/traits/genomics/viperin_system.html
    sha256: f69aa86de6ae20cdd822f8e04be4cd45f1df19d1f0804f1de29c067add5f3f39
    role: context
  - path: pages/traits/genomics/vp1796_system.html
    sha256: fdfdebd512d9dec4579da503e3c20705ef5a2495d0c3e3594fbb114d03be3998
    role: context
  - path: pages/traits/genomics/vp1817_system.html
    sha256: 214db047916f5a140d3f6d9b5c7b4845523a0498a47ff97409b33843cbff2699
    role: context
  - path: pages/traits/genomics/vp1823_system.html
    sha256: 6406a48c6a17228998170cb108ca747981dd77e484b5edd30df72b5ce1da3c78
    role: context
  - path: pages/traits/genomics/vp1826_system.html
    sha256: 33043d38b95f487e1bd3864180602b394dbe3afdcd102bd6ff17014957dc9f98
    role: context
  - path: pages/traits/genomics/vp1839_system.html
    sha256: 026a31620bc52dd2b309f9687e9b8a186edb6397619dc7a00bca15d621dec730
    role: context
  - path: pages/traits/genomics/vp1840_system.html
    sha256: 32560ca7254de9d0f3645656408523344ca958e6701c14a7df68fab9daf73f8d
    role: context
  - path: pages/traits/genomics/vp1848_system.html
    sha256: b732999e13461a08e71a3fd487250c1f5dff5723633629db9c557e867a3836f8
    role: context
  - path: pages/traits/genomics/vp1851_system.html
    sha256: a5c2f94127bc2b36e064c452ce0958bb2838f838386e777677663575d4c2ad27
    role: context
  - path: pages/traits/genomics/vp1853_system.html
    sha256: 8e930b94a160b1c35a9d64c33676f1f561adfca43431286bbccca1139a350115
    role: context
  - path: pages/traits/genomics/wadjet_system.html
    sha256: 4524c2690664d2e19b7c22cc4a67ce811913b1076871d174fc19ab5612defdcb
    role: context
  - path: pages/traits/genomics/zorya_system.html
    sha256: 6e5eb149d37dc45eebb38e85ffeb5d236a20d8b41b7d6deea4fcb6e95f2524ed
    role: context
  - path: pages/traits/genomics/zorya_type_i_system.html
    sha256: 424782973718ed4fa08afc726d92e2c3e7de4f486fb3d56ae5cffbe637145e88
    role: context
  - path: pages/traits/genomics/zorya_type_ii_system.html
    sha256: 3e5dbbdb1f01fb741f399d2ff4d944e966615cc2ca382012e99fa10cb02924cf
    role: context
  - path: pages/traits/genomics/zorya_type_iii_system.html
    sha256: 46bf84639a77413cbaa50bae713a0623956c3ec2e2e823117579dc926ba71fce
    role: context
  - path: pages/traits/metabolism/accumulates.html
    sha256: ce2a0ab114885c2d37fa37a54af11f4d90aa8876085e4ec140c6814272a0c4af
    role: context
  - path: pages/traits/metabolism/acetoclastic_methanogenesis.html
    sha256: e66ccb82d156849ef96c0cf5fe8e95a987eae33a04a438b71fa2a65fd3f50624
    role: context
  - path: pages/traits/metabolism/acetogenesis.html
    sha256: 440cfec8758d60ed5e48e66afe17168837e23587ee65f845c778cdc7169f2ed0
    role: context
  - path: pages/traits/metabolism/acetone_butanol_ethanol_fermentation.html
    sha256: 8a3610e6c46c09eb7e94d548b05f0d38d3c5376c8228ab673f476e2f44ac3b5c
    role: context
  - path: pages/traits/metabolism/aerobic_respiration.html
    sha256: feb2e6751343ac24c7ab6e22ba1e44e49507fcf5bbba1433c16cf5af401fdb3f
    role: context
  - path: pages/traits/metabolism/anaerobic_ammonium_oxidation.html
    sha256: e7f5b273353a606cd275c7a621e3a3f8f3626bb716374335c2b625dd014e6aac
    role: context
  - path: pages/traits/metabolism/anaerobic_oxidation_of_methane.html
    sha256: 41432cb186046be819be0e13ca1ba97753df1229f7fc1ea66b3d56657c6caa9a
    role: context
  - path: pages/traits/metabolism/anaerobic_respiration.html
    sha256: 7c3f8afcdfbbb9abe0dffc48a3760e704b68f2cb16d9c66ef8fa89016aafe2d4
    role: context
  - path: pages/traits/metabolism/anoxygenic_photosynthesis.html
    sha256: 366960d34299ff521df945aa62eff2fc1f4eaca5d6a716d4a1420210cd4e678e
    role: context
  - path: pages/traits/metabolism/aromatic_compound_degradation.html
    sha256: be16f1816324fbe219a42f204274295863ac609e2e4cd86bd9b34ee9c913118d
    role: context
  - path: pages/traits/metabolism/aromatic_hydrocarbon_degradation.html
    sha256: 301961f264bc420cabf5959ae5083a744bfc6d61d8de8533783d3fe4892a57a4
    role: context
  - path: pages/traits/metabolism/arsenate_respiration.html
    sha256: ce82017770846ae8ad427fefdbfef033cc3f94dbf740a680fcaa6aa9f0700fad
    role: context
  - path: pages/traits/metabolism/arsenite_oxidation.html
    sha256: a1a0e602110c0c3f4248acb4c0453c876a76b8cd4e0de16cdc75edc7162900f9
    role: context
  - path: pages/traits/metabolism/assimilates.html
    sha256: df3fe134f56528bf6eda0548b2c6422d5523d883ef3847f90ccdf319b29aff7a
    role: context
  - path: pages/traits/metabolism/biopolymer_degradation.html
    sha256: 51ade9f06d384eca02bda0027174334287ce5a228a21fbffe80305a78ae305ef
    role: context
  - path: pages/traits/metabolism/builds_acid_from.html
    sha256: c097212831d1a9f0f290d808c822b54cdaf4ccb774fa06b7d9818a25bfdae9d8
    role: context
  - path: pages/traits/metabolism/builds_base_from.html
    sha256: e47019f19e82ff8a0ace94313bca4a2925fd4a1f6d90d5c78ff3ddff97115140
    role: context
  - path: pages/traits/metabolism/builds_gas_from.html
    sha256: 0d31dca8d9eda29a85baf0a6e086a627f041a75edc947903954b3683cf1ac4a8
    role: context
  - path: pages/traits/metabolism/butanediol_fermentation.html
    sha256: 644a562aa9fdbf1fa0aca36c375cd93b7d06b2aa2f5b085de8ab9199bcd41bfd
    role: context
  - path: pages/traits/metabolism/butyric_acid_fermentation.html
    sha256: 30abc497a53d4063cd7f793ccc1b4375bece8da854d6fd7691668c276402aaeb
    role: context
  - path: pages/traits/metabolism/cable_bacteria_metabolism.html
    sha256: 8789e8a0a9600dc07ffcae079b38ef12e0be9d3ef576860f72237a7b903bb14f
    role: context
  - path: pages/traits/metabolism/calvin_benson_bassham_cycle.html
    sha256: 027e78324444ffc2c0f7e9e94c99809e13ab4040f1236bf48c18a4681b39c9ed
    role: context
  - path: pages/traits/metabolism/capable_of.html
    sha256: 508592b5ef8e3048d9e754443bb949c849b9d7c5c2f2fa5274b8e3434b44b05a
    role: context
  - path: pages/traits/metabolism/carbon_fixation.html
    sha256: 4309d05e20c27c37a0ad1822c366c64e3166806534f0e73cc78148bd857bf523
    role: context
  - path: pages/traits/metabolism/cellulolysis.html
    sha256: 8aec0acee676e6eca5eef382a1ea79b6e8239a78d476bf5ec6359194ddbcbd27
    role: context
  - path: pages/traits/metabolism/chitinolysis.html
    sha256: 2f6eee74af124c1f4a89e91ad9a599249f49db6fed292982ca268bc5751c9dee
    role: context
  - path: pages/traits/metabolism/chlorate_respiration.html
    sha256: a729e7828bc4e232238efb64bf1680b20d2fab34ad56cb3959da4260d6dfea77
    role: context
  - path: pages/traits/metabolism/citrate_fermentation.html
    sha256: 55e88878f67a12a58a82a9d963e8c8ff45d9558ae4288452ac105802976b3eb1
    role: context
  - path: pages/traits/metabolism/compartmentalizes.html
    sha256: caf00bf4afdd7ff47e4532f8b3dafb330160e0d7b6ae4c5f65d0388d31654aee
    role: context
  - path: pages/traits/metabolism/complete_ammonia_oxidation.html
    sha256: 7e708e8ae6e255152a63dbae2b03d51531aaa442add575604249319e87905405
    role: context
  - path: pages/traits/metabolism/dark_hydrogen_oxidation.html
    sha256: 3ac3383daccae3ba9d64845f47df8280b4cb533d77eaa79494bf9f9500b3735c
    role: context
  - path: pages/traits/metabolism/dark_oxidation_of_sulfur_compounds.html
    sha256: 24b04b60b24d9fc8fbab448ddc69a33fcd95a9f3996c984d6d53be6d17a1f0a1
    role: context
  - path: pages/traits/metabolism/degrades.html
    sha256: a7fefa347e8b341ca1ba3b49ded967e63fd779caefee12ab934edd8df999360b
    role: context
  - path: pages/traits/metabolism/denitrification.html
    sha256: 794adaf33e1c7258e13bf6ad2d8aaa63c95b68b3588bb8cb53e34ae196204fe4
    role: context
  - path: pages/traits/metabolism/dicarboxylate_four_hydroxybutyrate_cycle.html
    sha256: e4d77bcda24b183b16100221a99340ff7849913ff8e300ad9fcce7825bc6df9b
    role: context
  - path: pages/traits/metabolism/dimethyl_sulfoxide_respiration.html
    sha256: 746ad74976e1e9ba0ed15c26dee41e1448392e910d1500a8b452711cd0961b88
    role: context
  - path: pages/traits/metabolism/disproportionates.html
    sha256: bb59b1c887aef4aded4cb2027fcdced0ab5c98f15e07e5429bb28d4621b71d3c
    role: context
  - path: pages/traits/metabolism/disproportionation.html
    sha256: e464e198edb71e48eeb95bcfadb5555e294b07e9571dd5d346509f9e91eb943d
    role: context
  - path: pages/traits/metabolism/dissimilatory_iron_reduction.html
    sha256: cfc1707baa8874b998e553bdcf131fb7847ac51b1a50c647640c0b5b61dc6ee6
    role: context
  - path: pages/traits/metabolism/dissimilatory_manganese_reduction.html
    sha256: a576ac2cc96c71ca03e1bd879442e1de1fead6cfdae4c393378da22323eda5c4
    role: context
  - path: pages/traits/metabolism/dissimilatory_metal_reduction.html
    sha256: c5bd14feb35e69e9928de87c945e5fe7e58742bfa900a2faacacfea032a6d118
    role: context
  - path: pages/traits/metabolism/dissimilatory_nitrate_reduction_to_ammonium.html
    sha256: 8368955e0a12d3641fd3380dda4a8343ab7b34a1161389ac56c1f13e983e3479
    role: context
  - path: pages/traits/metabolism/dissimilatory_sulfate_reduction.html
    sha256: 11d3d4f6f2fa60c4f46dd22ceeb72a2806e890c238b5bf8f96c9f7716607877a
    role: context
  - path: pages/traits/metabolism/does_not_accumulate.html
    sha256: dd1a2af3983a94fc4dcd9faa59043c22d73c8839ed70cce9d272ee5c006d702d
    role: context
  - path: pages/traits/metabolism/does_not_assimilate.html
    sha256: 243585179337b8ffd1720d866d57aa5303225b1765326c98a52eda5e9fb98ca1
    role: context
  - path: pages/traits/metabolism/does_not_build_acid_from.html
    sha256: 49b33e5b59612ede7e1042c059c074a1bd6c6cb4e45023faea5ea05e47377751
    role: context
  - path: pages/traits/metabolism/does_not_build_base_from.html
    sha256: 645e24ce82614797930790b6130eaa6adbe651d40881947bd3a6cc62554c798d
    role: context
  - path: pages/traits/metabolism/does_not_build_gas_from.html
    sha256: ccb9de6986b9d4b69d862802b7c63677eff71436616ff1b0d7e2760a8017e792
    role: context
  - path: pages/traits/metabolism/does_not_compartmentalize.html
    sha256: ce6d7acbc0f82cb5fa5e792b8cfaa1cd7fbab502383ed22bb7b128d01013e3d5
    role: context
  - path: pages/traits/metabolism/does_not_degrade.html
    sha256: dfa6fb27c3bba1ddbc37664b6730dfef6c5024ef4518d88037efb1cad67902ed
    role: context
  - path: pages/traits/metabolism/does_not_disproportionate.html
    sha256: 13f608c7ed0e47957673f0346abe1fb9bed54f0367a1c61ba7d48526491dd6dc
    role: context
  - path: pages/traits/metabolism/does_not_export.html
    sha256: 1b95510de8b624b9c56e44020645abc598df9083e4410ee57dd14309e41cc329
    role: context
  - path: pages/traits/metabolism/does_not_ferment.html
    sha256: cf913840b892cb3443b84fc3b286cce94dd5ffddef86b9cc21822e4081c92ff3
    role: context
  - path: pages/traits/metabolism/does_not_hydrolyze.html
    sha256: 155a496a563970fec70ff2c7dbeef5a9ba1577bded86ec16472b9cf77cac8251
    role: context
  - path: pages/traits/metabolism/does_not_import.html
    sha256: 4a548cf81d66952e71e320ddf9c7a946e21f444c324838f36bf14c82c82ad00f
    role: context
  - path: pages/traits/metabolism/does_not_oxidize.html
    sha256: 2c6542f5c59c3423f6823512bacf6d3aa6c6ebaf94dc1275790dd8af2e6d1fc0
    role: context
  - path: pages/traits/metabolism/does_not_produce.html
    sha256: 99d54ff42734f242af23346304322cd59435772453289f49a7713a079d13636f
    role: context
  - path: pages/traits/metabolism/does_not_reduce.html
    sha256: 1192c3e93f667e5f9727e6eb5079f0e7383aff3ac3cc53c8284d6a2ad66304e8
    role: context
  - path: pages/traits/metabolism/does_not_sequester.html
    sha256: f0af19d8db33021351b04142ae2f2e5094c28f089cdec10c06bd58ba296b7aa0
    role: context
  - path: pages/traits/metabolism/does_not_show_activity_of.html
    sha256: 352a0a56177227cd5f1b4a9a6a1ccc0ace747adcf4cb6369be43b958a0dbb64a
    role: context
  - path: pages/traits/metabolism/does_not_transport.html
    sha256: 2c0134d26e8a5948c1be82a05170d6bfe845dc1d688434888ad5557250f518c1
    role: context
  - path: pages/traits/metabolism/does_not_use_as_carbon_source.html
    sha256: e0f2d4e2368b9c90bc8c7715cde13dd89c5f8259923bf1204db9aae4a7c1a4c3
    role: context
  - path: pages/traits/metabolism/does_not_use_as_electron_acceptor.html
    sha256: a9f5be9cfe441b19e1990fd5e4d3a52d52bb28d1e311c7887298623e1768e051
    role: context
  - path: pages/traits/metabolism/does_not_use_as_electron_donor.html
    sha256: bf6e7c25b00578a7a131c3af7180b35d712f33e5ebc30ca15e50722aded52460
    role: context
  - path: pages/traits/metabolism/does_not_use_as_energy_source.html
    sha256: 8d0b38ab5b3d628cfa4010fc4df61ed5c7d09e75e1a03a916563523ff4d19a57
    role: context
  - path: pages/traits/metabolism/does_not_use_as_nitrogen_source.html
    sha256: 860e1debdc1cc97e22d87deaa21e19deea5a0b87ab203f00fef03b0e516a2991
    role: context
  - path: pages/traits/metabolism/does_not_use_as_sulfur_source.html
    sha256: 490ce2f8c3d3f98613de1dbf417e0f0e624cfeb66861fe483580ba6a2250a506
    role: context
  - path: pages/traits/metabolism/does_not_use_for_aerobic_catabolization.html
    sha256: 24ef4458a2434d367804f9c20b1c2ebcafd8ed3d459b8077052e8a5c1227e7b0
    role: context
  - path: pages/traits/metabolism/does_not_use_for_aerobic_growth.html
    sha256: 829efca81c474db467f39529f593e9d0a5895171d915c36e52cead7d146ac308
    role: context
  - path: pages/traits/metabolism/does_not_use_for_anaerobic_catabolization.html
    sha256: 3f9e54d87f430f89a3a67147a3de7c1f32bdefc5709e7387f7b9d2799fbdac52
    role: context
  - path: pages/traits/metabolism/does_not_use_for_anaerobic_growth.html
    sha256: 87114441431e470d7a8125e26e1bfee5243cbdf0e77ed1beb1231c0a6ef07d17
    role: context
  - path: pages/traits/metabolism/does_not_use_for_anaerobic_growth_in_the_dark.html
    sha256: a8a5ed7ade9f72dedf5e712656869ef2445bb75bb4489cfac9e81717a4d60aaf
    role: context
  - path: pages/traits/metabolism/does_not_use_for_anaerobic_growth_with_light.html
    sha256: 9f761ca0a771cf9837a74d9ea4714bea4e134aef062141148e5045a749146b2f
    role: context
  - path: pages/traits/metabolism/does_not_use_for_growth.html
    sha256: de86d335d9d7f04b40df0fe94065cd1d71afaa092e1a662eeafe299c649aacd5
    role: context
  - path: pages/traits/metabolism/does_not_use_for_respiration.html
    sha256: dd9688ff37552d6ef8f2258be3409bf9181547a524e5fe9226adeca6a7bf8608
    role: context
  - path: pages/traits/metabolism/does_not_use_in_other_way.html
    sha256: 5fc27d7a2c266307669e2676107d540d9d2bfaf281a410cb2f21cb0b90c844d9
    role: context
  - path: pages/traits/metabolism/electron_transfer.html
    sha256: b8b74a02592fa3a7097bfc2a9ff904aeeec4b2053dec67e7bac2598a612049af
    role: context
  - path: pages/traits/metabolism/enzyme_activity_analyzed.html
    sha256: 4cb44fde08f1524bd82df36a1e4fc5d16f7132657ce361b4bbb329d1650e4f27
    role: context
  - path: pages/traits/metabolism/ethanol_fermentation.html
    sha256: f827d31e11b67a19a6509b04115a27660a44ebc499a520c3b53f8d30c636291e
    role: context
  - path: pages/traits/metabolism/exports.html
    sha256: c24adb83618a63bd63780495558e905d91c2dc410e664c4fe7aa941ffc8648b2
    role: context
  - path: pages/traits/metabolism/fermentation.html
    sha256: 5b1e67b864b872de3408ba46894da5b7e318c7e47e6a98f95a0a475849f424d8
    role: context
  - path: pages/traits/metabolism/fermentative_hydrogen_production.html
    sha256: a6b277591e22d2a792c1419c6bbc458810c5fe1aa277b1b4ab249ccb76dc98f8
    role: context
  - path: pages/traits/metabolism/ferments.html
    sha256: 0c3f1265bb233daaba2b317aa59988a64756eb2f1e58ef3d044eb641625f769a
    role: context
  - path: pages/traits/metabolism/fumarate_respiration.html
    sha256: 78433363e0ac3884b6023b1a7321a578beb98d8f24f648f1da954ca00d57c569
    role: context
  - path: pages/traits/metabolism/has_growth_nacl_observation.html
    sha256: af3152d35866d8712c7fd0cdab49d444acecdc075d3b6a71319411a04ac9ec23
    role: context
  - path: pages/traits/metabolism/has_growth_oxygen_observation.html
    sha256: d92e7cfa9d241d62c9f4106592ea474dece63d45387b01adc206d40e79ad709c
    role: context
  - path: pages/traits/metabolism/has_growth_ph_observation.html
    sha256: 30ce62617b8c2e7406a3b7dd7e9ea33c6a5f801ec0d136586d69f0d62181dcfe
    role: context
  - path: pages/traits/metabolism/has_growth_temperature_observation.html
    sha256: 1ae6a3fef2caedbdce78ba90810144af888779bfcecda0ceaabecc2b9c97e0d6
    role: context
  - path: pages/traits/metabolism/has_nacl_delta_observation.html
    sha256: b732b0f93eb4a5550570570fdd4ea37413cfd61a0650cfd5ffd349e42b931fd4
    role: context
  - path: pages/traits/metabolism/has_nacl_observation.html
    sha256: 98b4972041a99ce7ce628e68eba0e1570596c2d0e37e8dde209b908a8228d2d0
    role: context
  - path: pages/traits/metabolism/has_observation.html
    sha256: 8ca4fe5da3da45b66ae05c00de072d700204ac8a1c773747c2b218e283b17a2c
    role: context
  - path: pages/traits/metabolism/has_optimum_nacl_observation.html
    sha256: 51d2fefff4fa8a599c297100f1d1b9619d8f46d05b69d3313bc15bb750d4352a
    role: context
  - path: pages/traits/metabolism/has_optimum_oxygen_observation.html
    sha256: 63acf221bf1ac6ff1142e38ac68b09000aa3b331efa7010fab3df0ab1a310398
    role: context
  - path: pages/traits/metabolism/has_optimum_ph_observation.html
    sha256: 6614236cc9a5f74bb14a1acc2e956cf6d7875314f1632be6f086428210755071
    role: context
  - path: pages/traits/metabolism/has_optimum_temperature_observation.html
    sha256: 3acb4466784d37b5ceeba190772d3b5fc1cb14a954e0ce8dfe42346106c60052
    role: context
  - path: pages/traits/metabolism/has_oxygen_delta_observation.html
    sha256: 089e6e994fe8e5625e377257173f1e4d75e157de2d4f03d9794e6ab5a7e5dbec
    role: context
  - path: pages/traits/metabolism/has_oxygen_observation.html
    sha256: acdb0c50cb7c81ad0346d793bfd9eed29ac0a9f3e5abf37ef134a7af6802c6bc
    role: context
  - path: pages/traits/metabolism/has_ph_delta_observation.html
    sha256: d31d3cef7812592fed5344ff9ad7fafa4952e971b249220eeb222e7ee0f916cd
    role: context
  - path: pages/traits/metabolism/has_ph_observation.html
    sha256: c8d9818b1f9dd341291b946917b58c76732eb38b55e0e52e6cc2e57cd72c74dd
    role: context
  - path: pages/traits/metabolism/has_phenotype.html
    sha256: 2bd4b1f3d311de2377dc6f96709a7e36994348fb80cee9d41aa1af508f971c7f
    role: context
  - path: pages/traits/metabolism/has_quality.html
    sha256: f42e8e75ab56e52fb0c89d7b6985d4e1cde45b2d0bfb55edcc45a0e518db4bd0
    role: context
  - path: pages/traits/metabolism/has_range_nacl_observation.html
    sha256: c830726c97522741408a022d0dbbb01d89e7e2c731cfb2004034656af7da72c3
    role: context
  - path: pages/traits/metabolism/has_range_oxygen_observation.html
    sha256: 1ab71731319e8895b9c393670e874c8b0aeb6711339d074807e8687ba92126ff
    role: context
  - path: pages/traits/metabolism/has_range_ph_observation.html
    sha256: 28a3e00708b0fa9fb8a09799df04df64627763915b179d5f8d631fcbbd26b8ba
    role: context
  - path: pages/traits/metabolism/has_range_temperature_observation.html
    sha256: c26006612b68943ae7bd43a835145162a631361b5ae3ee846c4114d3d76e99b3
    role: context
  - path: pages/traits/metabolism/has_temperature_delta_observation.html
    sha256: c183e7307c7d7d82d324f5e812dba5784c1d52a7143c98d7aafabee80353310e
    role: context
  - path: pages/traits/metabolism/has_temperature_observation.html
    sha256: f3b4d44ccf94635d94b0f85752ba72896db6d7399491832c56be228cd37def50
    role: context
  - path: pages/traits/metabolism/homoacetogenesis.html
    sha256: 0ba88e4bce0df65f4df614509994d6dd611843cf9401b9be83d053bffab9d679
    role: context
  - path: pages/traits/metabolism/hydrocarbon_degradation.html
    sha256: c68eed538fbe79348a39f643e5fce68f39c8adc03326e3c697d40d9787cc167a
    role: context
  - path: pages/traits/metabolism/hydrogenotrophic_methanogenesis.html
    sha256: 864bed6225c12cac5c3bee3d145be1fdede8a9a87cfdca2d4af0caebc0787233
    role: context
  - path: pages/traits/metabolism/hydrolyzes.html
    sha256: 8e04ec403ba3db07af8a3d0ee380df0744e75d311c796b46e4e166940d07a8b7
    role: context
  - path: pages/traits/metabolism/imports.html
    sha256: 2f86220bda987863c76db587749009a1ebe893bee23bcd47264558ddde0981eb
    role: context
  - path: pages/traits/metabolism/iodate_respiration.html
    sha256: 00f573bd9a739d2245c45cd6fe3eea1a504f2a93ee4ceea381bc34ed6764b36f
    role: context
  - path: pages/traits/metabolism/iron_oxidation.html
    sha256: 9979050c5379ac6782e4632441f2352ed6b87336d87a130169058fe0263d1c18
    role: context
  - path: pages/traits/metabolism/is_not_required_for_growth.html
    sha256: c0e8d94e8e7fc40b6e7630c9b401573171d5e1eaa889266ae6ddd24ea005a1c7
    role: context
  - path: pages/traits/metabolism/lactic_acid_fermentation.html
    sha256: 9ca5f38be059e6a614fd60c38b3ec8351ddb2c24e5f82c0b0dbd4a2faea08804
    role: context
  - path: pages/traits/metabolism/lignin_degradation.html
    sha256: b137fb3e45371de71d71afc0f6ad1c57541e7c6ddc3f9a7f91ec6a9d2cb2fbe8
    role: context
  - path: pages/traits/metabolism/lipolysis.html
    sha256: 7b9e73d10c621d537b162d3aa79f3f46f208b9503204d02324788e6afd16c3b9
    role: context
  - path: pages/traits/metabolism/manganese_oxidation.html
    sha256: b0270ced60c19ddb5707dce4f26429dfdf8b5cc596751820768a8b1178c1dd9c
    role: context
  - path: pages/traits/metabolism/metabolism.html
    sha256: da5da71ed4395bdd86636de67298437c80cb86118bbd9643d38047755f726ae0
    role: context
  - path: pages/traits/metabolism/methanogenesis.html
    sha256: 22f54bcb754838baf78d720bf3b590585c79acabf3da7b46fd03076d3bdc0dc9
    role: context
  - path: pages/traits/metabolism/methanol_oxidation.html
    sha256: bacdb72f19a4231eb72d1fb887b5dcab52e33f6ed92e2b5b8099f2eedf763117
    role: context
  - path: pages/traits/metabolism/methyl_based_methanogenesis.html
    sha256: 4eeb1b79703f9e9dd8a2587ed425a56b36de8adfa98731412b252137c7ca59d8
    role: context
  - path: pages/traits/metabolism/mixed_acid_fermentation.html
    sha256: b1d3186b2c5664723bf0ec7cd4265fbe91d09e4a8371568911de3db6d8633576
    role: context
  - path: pages/traits/metabolism/nitrate_reduction.html
    sha256: 6dd6dea79bfda73938b1a19b20d3282daf867e93cd3ae4a06961188fbfdbdc13
    role: context
  - path: pages/traits/metabolism/nitrate_respiration.html
    sha256: 517f316bc802ed1801148a3c50b4d2d8cd6ec3fb97ce2f7c5bfd9b27843760d0
    role: context
  - path: pages/traits/metabolism/nitrification.html
    sha256: 9f7c904e55268fcbacca02b98b60e11057745ea2030d2032e3daec3c25d7300c
    role: context
  - path: pages/traits/metabolism/nitrite_respiration.html
    sha256: 6c0f042580c7f307ae528f8d397be6d6d3c1dd8e9fec3844bc6e8d40c6ef512b
    role: context
  - path: pages/traits/metabolism/nitrogen_fixation.html
    sha256: c5609369640e71798d8b25ee501f9e9636efb8b85363c529a471013b9cc4db2d
    role: context
  - path: pages/traits/metabolism/nitrogen_respiration.html
    sha256: 0660cb913aa5d9cf315ebde1a6931b6efc88c03a5164ef01d094314f9fdfd4ec
    role: context
  - path: pages/traits/metabolism/organism_interacts_with_chemical.html
    sha256: aab052f5f18a0a5f7880cbbb61cb94ea8815092dd102c9bf469483fde4b8455b
    role: context
  - path: pages/traits/metabolism/organohalide_respiration.html
    sha256: 550b9296cccfd5804e2c282841d03fba47a37f5b0ca90bd2f2a77c1846e59868
    role: context
  - path: pages/traits/metabolism/oxidative_phosphorylation.html
    sha256: 8e34138cdaee7bb9f1f643c5e7fd15dcf1aeb5250fc71a30bfd234ce42266d9a
    role: context
  - path: pages/traits/metabolism/oxidizes.html
    sha256: 161bf743e8e63b16ddd4ec73868244cceeec8702b2efd01fd340f87fc7f886ea
    role: context
  - path: pages/traits/metabolism/oxygenic_photosynthesis.html
    sha256: 27870b7b7c17ca62ce6cb03958d1982376db56686300022e85e7a8f095f9bc15
    role: context
  - path: pages/traits/metabolism/pectin_degradation.html
    sha256: caca4f4de0d7cd5efbba1bd4e40f8115e2d02694a3bab472af9bdb9735ce7b21
    role: context
  - path: pages/traits/metabolism/perchlorate_respiration.html
    sha256: 4b2d91b83f99fc783a1100f909cfa0591845268d59dedd6b5bc375e1699c56d5
    role: context
  - path: pages/traits/metabolism/photoferrotrophy.html
    sha256: 174100dcd1c2de4d97a4c04dd71575b130a5006f7b1faa31cac6d6938f73e050
    role: context
  - path: pages/traits/metabolism/photosynthesis.html
    sha256: 7690f4e536e79cf25af313842b33227f69133f4633bf28a61adf5536356a578d
    role: context
  - path: pages/traits/metabolism/phototrophy.html
    sha256: 15936da79f01870f1eaceff4d787aa3bec8a00c7541b80cfbfaec80cba88e832
    role: context
  - path: pages/traits/metabolism/produces.html
    sha256: aeff0715f16aada4df6d2c95e9bf8005b77e289acc0fb2c3b6f2612c672c794c
    role: context
  - path: pages/traits/metabolism/propionic_acid_fermentation.html
    sha256: 7f45f5233d272cc45b2df3680b15bf333452bcd5d51e8737cb330584d834627f
    role: context
  - path: pages/traits/metabolism/proteolysis.html
    sha256: 3c71ff895fcbb1295442f6eec62d3cf6c2b05417a2e8bbb4c206c57324794c6b
    role: context
  - path: pages/traits/metabolism/proteorhodopsin_phototrophy.html
    sha256: 98fe162d980b5667dafc5337f86d5f19c5320a43aa09ce01cbf65bbcb0c02a11
    role: context
  - path: pages/traits/metabolism/reduces.html
    sha256: efa82871dc00bbd03fd6aa7063555ae249a0f848f852165096211172cf1f36fc
    role: context
  - path: pages/traits/metabolism/reductive_tca_cycle.html
    sha256: c0323428f4dfcb2e708d449e432b9a8d109d820acb02837f8735cc25be0cf135
    role: context
  - path: pages/traits/metabolism/requires_for_growth.html
    sha256: 8fedc27dc5a1ae5ac01a402a959fb0187c3c6a18049765331d041adf6cfd478b
    role: context
  - path: pages/traits/metabolism/respiration.html
    sha256: 8d131d5fa1e669ecf708cc203520006899a7f963df2af8bd30dde48cbd915deb
    role: context
  - path: pages/traits/metabolism/respiration_of_sulfur_compounds.html
    sha256: a0efcb853b1eba222e81c817132826cad155d45c76dd9463a80f5f90e9f083d9
    role: context
  - path: pages/traits/metabolism/selenate_respiration.html
    sha256: e3959ee6c7b97b7eb5579bdf8756f3e89b7c386ee2d361ba4e7038ed385b63c5
    role: context
  - path: pages/traits/metabolism/sequesters.html
    sha256: c5e9da31d5506e3a227741d1065dd2bc31c6b6b0fcad0f1f7940cc6d531ad047
    role: context
  - path: pages/traits/metabolism/shows_activity_of.html
    sha256: c1f885fe659f6084cd88766cac174877f5724d555272a6fc9dd1aefb1bfa3784
    role: context
  - path: pages/traits/metabolism/starch_degradation.html
    sha256: 4b7f1ce943647ec67931e336c9d0fb8e9a4318c8a18432549b53b3e5e8eb560e
    role: context
  - path: pages/traits/metabolism/substrate_level_phosphorylation.html
    sha256: 62728d93c293991c0713c8d9dfe3a3490c328625ab092901cac3001f1b983457
    role: context
  - path: pages/traits/metabolism/sulfur_oxidation.html
    sha256: cfc33b18586e271d521797c7f0c900c85afea4431d5c3a49316aa04b7abf6c04
    role: context
  - path: pages/traits/metabolism/sulfur_respiration.html
    sha256: 724b2bc9ec9e1d0bc7f390e49a00518f438e197b705151b4ba8913254a367235
    role: context
  - path: pages/traits/metabolism/syntrophy.html
    sha256: acc131b8cf52b54e819fad45edeb421cdf910215f6809e9f927e7779117d2a38
    role: context
  - path: pages/traits/metabolism/tetrathionate_respiration.html
    sha256: 4b05aabfd2caaa65f78cb4d493f389a3eb5d8b6f639bcdeeb8bd090b23aada6d
    role: context
  - path: pages/traits/metabolism/thiosulfate_respiration.html
    sha256: edf110dcaa4c9a96d2a089ef90735de315ce313bad9b8aafcc10640928d42c1d
    role: context
  - path: pages/traits/metabolism/three_hydroxypropionate_bicycle.html
    sha256: f98498c1806687f5f9ce61e95a18114d82b99c93a475b0de04e195ddf94bf07d
    role: context
  - path: pages/traits/metabolism/three_hydroxypropionate_four_hydroxybutyrate_cycle.html
    sha256: 4ae7a797f86449ded7c645560115371ba57477a7caf92c3c9214e27c3b9e77f6
    role: context
  - path: pages/traits/metabolism/transports.html
    sha256: e7677d5153f9aac478c4d5dfc479f511982edae7cdb997be98e6c3f342ea93eb
    role: context
  - path: pages/traits/metabolism/trimethylamine_n_oxide_respiration.html
    sha256: 53a598c3744ec50390c2e728fc6efadb71c6ad97607f106cb875673b3dd3378b
    role: context
  - path: pages/traits/metabolism/uses_as_carbon_source.html
    sha256: 4afe5b556484fae45cecc0045deab4f7a9aa7f9b5d0cfb2bf03f8bead696ab20
    role: context
  - path: pages/traits/metabolism/uses_as_electron_acceptor.html
    sha256: 494dd15d6ef45ccc4482113643a084b74e311531800b5c50940d4a59925b7a71
    role: context
  - path: pages/traits/metabolism/uses_as_electron_donor.html
    sha256: b34677a5bf54249dbc8e0716130d07c470861f2997c5653b339346fac63cb88a
    role: context
  - path: pages/traits/metabolism/uses_as_energy_source.html
    sha256: 84cb8ed721bdb761168d64363fe2cc48aeca451920f0ca9df4b92d0dbe84f382
    role: context
  - path: pages/traits/metabolism/uses_as_nitrogen_source.html
    sha256: ff5865baba3d241cd6ca52f4c5f5ef7a4928e9b5dc1523da47067ffe895f7d5a
    role: context
  - path: pages/traits/metabolism/uses_as_sulfur_source.html
    sha256: 3fdc490171bbb6651e50458fe57fa668cb25449cde4a83c7c8c9568e263c6e68
    role: context
  - path: pages/traits/metabolism/uses_for_aerobic_catabolization.html
    sha256: 9f76ea77f1381efcb3d8d7348c28dc4b8f938d5e4ef595ddce579b57be892067
    role: context
  - path: pages/traits/metabolism/uses_for_aerobic_growth.html
    sha256: 7a9118ce275cfc51b8c6bf37e8c22030660c7a01097afd928aa67f192c3c67e2
    role: context
  - path: pages/traits/metabolism/uses_for_anaerobic_catabolization.html
    sha256: 17c20b320ffea23525a1ca567970f5cc93cc2d5471a0be144cfc22b01fd09750
    role: context
  - path: pages/traits/metabolism/uses_for_anaerobic_growth.html
    sha256: c486ac7dc07970dd28700c7917e1eb10d3fc56a8e197e294b1a787369df0ab0e
    role: context
  - path: pages/traits/metabolism/uses_for_anaerobic_growth_in_the_dark.html
    sha256: f2f4160cc80b19249d2daf70c014a44cdeeb6104ed77f54712acc935169f247f
    role: context
  - path: pages/traits/metabolism/uses_for_anaerobic_growth_with_light.html
    sha256: 48bf02fbbaee87d2d63ff8ceaf12fa0aea1b228d4a7f440c3d41ceab88b0860e
    role: context
  - path: pages/traits/metabolism/uses_for_growth.html
    sha256: 81a7f0e97dc33463d0c2177714be94a323aa1aadba110e7bc5289220581634e1
    role: context
  - path: pages/traits/metabolism/uses_for_respiration.html
    sha256: baa3c14c40540b869b2d7bc813b8f2971435aec4538785cb9054e674fdb0d097
    role: context
  - path: pages/traits/metabolism/uses_in_other_way.html
    sha256: c35cba6f16861693563325cce2e5df56124c81dec72764e0ed9356cb850dab57
    role: context
  - path: pages/traits/metabolism/wood_ljungdahl_pathway.html
    sha256: f2ea33d28e7a2a42f5c17f34ee0e94ed8482985f18023fadb51c11302c653f78
    role: context
  - path: pages/traits/metabolism/xylan_degradation.html
    sha256: 73d8396051dd4d17f9be9f9053919ed9e78d909c7f501e63e6dddb353861477d
    role: context
  - path: pages/traits/morphology/akinete.html
    sha256: 2eff19147a9d6e8840fc6a28eda04a19ff0cdf01f43a694984bcc8165cdb0f90
    role: context
  - path: pages/traits/morphology/amphitrichous.html
    sha256: 0626a1de4d8cc3dc7deda0b9a38e2a9cb8b31e1ee6a8eac9ca20723bba6384c2
    role: context
  - path: pages/traits/morphology/axially_filamented.html
    sha256: 2287954cc62fb3278b6cc6a465c763c2c3b939e259da97f8e2768366e3b92d5b
    role: context
  - path: pages/traits/morphology/bacillus_shaped.html
    sha256: 164dc89103262de6f51f20945a1fcf40553a419663e07ffcfe50881be5ae6f9c
    role: context
  - path: pages/traits/morphology/baeocyte_formation.html
    sha256: bbb9eb99992150adf2573e439298340b59be38308c285311ad6726580931bef9
    role: context
  - path: pages/traits/morphology/black_pigmented.html
    sha256: b8d47e9405b7b8ce9457f2c58790214b0485bf20f1ed3eb388e3731ed6ac6848
    role: context
  - path: pages/traits/morphology/branched_shaped.html
    sha256: 867b334644530eebdfa91f8084f0d20a5c76cebf6b9c6fefc7e52e6680ee45f9
    role: context
  - path: pages/traits/morphology/brown_pigmented.html
    sha256: aa5fc4f5d1b46efb07451d4408394bc22a05e55ffd7fca9098484657d6312170
    role: context
  - path: pages/traits/morphology/capsule.html
    sha256: 152ecb1ee36954fd054ba77eb9a2352eca020e0fc3eefc3184abebc4edd248e1
    role: context
  - path: pages/traits/morphology/carboxysome.html
    sha256: 9aaf47e7c751b4fa92c2d079c3772166b9867499cbb53b3ebe406c45031d4694
    role: context
  - path: pages/traits/morphology/carotenoid_pigmentation.html
    sha256: 0de4eae0e47260f3400ba5ee624227f8d11aca54dd5c4c167216f153c6c77382
    role: context
  - path: pages/traits/morphology/cell_length.html
    sha256: d34b847507110b9ae074b078b0fe455ae175d23520eee33169b56b309f7a1416
    role: context
  - path: pages/traits/morphology/cell_length_large.html
    sha256: 14b7e91ed8ac5a6a7655eef08d491bbf2cdf405f89fad522a9408a60c4a55f53
    role: context
  - path: pages/traits/morphology/cell_length_medium.html
    sha256: cc27ec879e9dba69fcf76266cc89f45492c4b56c870e0b6f85e57e91eda5550e
    role: context
  - path: pages/traits/morphology/cell_length_small.html
    sha256: 0bc8b64af8c41ea8c36f559b8e2cd3e9f33fa52605b7b0cdc449514bd38fb586
    role: context
  - path: pages/traits/morphology/cell_length_very_small.html
    sha256: 6b87a1835538144198c95f01c51aedc350c02b212039ed269ae794df2db69ead
    role: context
  - path: pages/traits/morphology/cell_shape.html
    sha256: 98eaa0137e7dc40a989b932fc4a3f71aaa0e1b1615ed133204ae1b729af8496b
    role: context
  - path: pages/traits/morphology/cell_width.html
    sha256: 0fe773359764b18cbeb12897706da203358247d048ed0bfa9959bc9efed187ed
    role: context
  - path: pages/traits/morphology/cell_width_large.html
    sha256: 0e0e36890171afae4db5c5d5977724fa4edbc6d5a67b46efd93f5aa13ea2baf8
    role: context
  - path: pages/traits/morphology/cell_width_medium.html
    sha256: 72d31ebeaa18a7635db4726ed05df4e4c8bbc15e9e8ef2bbb031dcaf44068ef9
    role: context
  - path: pages/traits/morphology/cell_width_small.html
    sha256: 71572066a44dc0ec463a36d9bbcdb28e9c3a3526b42be46a3d20ee732a265ffa
    role: context
  - path: pages/traits/morphology/cell_width_very_small.html
    sha256: 0057d3de357ba0eab0c455d92f96ecf09a5cfab2b95eb3ae41575544758bfd2a
    role: context
  - path: pages/traits/morphology/coccobacillus_shaped.html
    sha256: 783233e532c8fc5653ca059cd4388b2ed9f301f9175ee2a15ac730dbd47b9b10
    role: context
  - path: pages/traits/morphology/coccus_shaped.html
    sha256: 41684cd7a5d22116ce5446d1cffb3a0dc035f65e0085fd9b57a0e152dae97529
    role: context
  - path: pages/traits/morphology/coenobium_formation.html
    sha256: 950fb1ac817a8fcf81168d5b5c0630e3c041e177d14a55fe3002c7c6d67938fb
    role: context
  - path: pages/traits/morphology/cream_pigmented.html
    sha256: 8325ad7d56f47bd7807b643205f63ebb0a8b47129d415c7576e22713d6193dc2
    role: context
  - path: pages/traits/morphology/crescent_shaped.html
    sha256: 5d04048f4297f87a26615658c30f3afaa73635339216a24fd536fef715c30d72
    role: context
  - path: pages/traits/morphology/curved_shaped.html
    sha256: 2869458a9547a7d0ec8a1f64a5e46fde275515fc4164a6f3a9a0b8038bcb30fb
    role: context
  - path: pages/traits/morphology/cyanobacterial_multiseriate_trichome_formation.html
    sha256: 6f9af8b1e786bff15ec21bab1382692cab64e10f825c6e3cf37812b740c65314
    role: context
  - path: pages/traits/morphology/cyanophycin_granule.html
    sha256: 2108588483b302b4eb60c28b05d46252ef504091eeba9f39d340cce1f69b170e
    role: context
  - path: pages/traits/morphology/diplococcus_shaped.html
    sha256: 4b8aeaa1e83790a35f3fe56e614b8a2e7570d165cad4a4089483eb78ac80e72b
    role: context
  - path: pages/traits/morphology/disc_shaped.html
    sha256: 838491c40f895e7cc1106384bf99858bb3a963e48c0d348f26eab4f4e1c6cacc
    role: context
  - path: pages/traits/morphology/dumbbell_shaped.html
    sha256: e357d8053c009bd660eacf18da7da23b470d7137c185ce4765cf45777817a2a5
    role: context
  - path: pages/traits/morphology/ellipsoidal.html
    sha256: 3609d53b7581765b44c57e30ad1d43686f98adf3f74a66fdd8053d2fc6b8502b
    role: context
  - path: pages/traits/morphology/expansion_driven_sliding_motility.html
    sha256: fe53940a74e1bf22b3d7a77086041e4fb62a9866d1744f170aa4aa930c76f692
    role: context
  - path: pages/traits/morphology/false_branching.html
    sha256: 71d2597d68ff12ffe9e960d25b45d5f8bcee484074c5808f2e7cbbf73e1b3df2
    role: context
  - path: pages/traits/morphology/ferrosome.html
    sha256: f84251b7f6f479fc167675709045eeeba2011c47c298d8b7cc5aa20fd269b4fa
    role: context
  - path: pages/traits/morphology/filament_shaped.html
    sha256: 78d76800b47bf4df5d5f5d3327fbb61b709049e11b7ac24db9350d4af6bb38a4
    role: context
  - path: pages/traits/morphology/flagellar_arrangement.html
    sha256: f443e19435a17886ada5f1bef422c4e8f196ffb53800e228d2b8c6cb3ab922c3
    role: context
  - path: pages/traits/morphology/flagellated.html
    sha256: dba1b230a2bd0ac76a810f1ac84fc95e8e61c286a701888ec8fdc0a9482234ef
    role: context
  - path: pages/traits/morphology/flask_shaped.html
    sha256: ed7333dc8a4bfcb8bf9207ec96661f1c13ca09a87d22b0be0657563dbde0356d
    role: context
  - path: pages/traits/morphology/fungal_adhesive_column_trap_formation.html
    sha256: 86f4da333c8881aa15d725190d86e9bf254a33566f14e2d3ad6ceedd48ffbb44
    role: context
  - path: pages/traits/morphology/fungal_adhesive_knob_trap_formation.html
    sha256: 8bf15782f5ad19737021ec00a0294d1d70149da898162e9cfc0d116c4686eead
    role: context
  - path: pages/traits/morphology/fungal_adhesive_net_trap_formation.html
    sha256: 02de2e6f1c12b7baa9e5e1adf2fc4a9bb8bdf9955e91bd97d841c6d914982ed8
    role: context
  - path: pages/traits/morphology/fungal_appressorium_formation.html
    sha256: 28e87d55e2ce848b86bdca0e1062c1622bd4f84b6169dc5c891d9db235e31a11
    role: context
  - path: pages/traits/morphology/fungal_arbuscule_formation.html
    sha256: 92cd596e3c2291ee75c1bf75b645d2486bcc3463791c4bdda3f17a27e132374e
    role: context
  - path: pages/traits/morphology/fungal_auxiliary_cell_formation.html
    sha256: f05c5209d44818c46377163a81ac1c7831bc03d2ee1a073574bf7250997612ea
    role: context
  - path: pages/traits/morphology/fungal_branched_absorbing_structure_formation.html
    sha256: 21388a79fc52731eece7842b11add80b0b705113bb61c9a44b093982887e4319
    role: context
  - path: pages/traits/morphology/fungal_chlamydospore_formation.html
    sha256: 9c140153ca39dac5321d4d657ade1793d425f0743b306a8adad613205887029e
    role: context
  - path: pages/traits/morphology/fungal_conidiation.html
    sha256: 7c0eb7c18b438254de4cde761e47b865d64d02c802abe8326680812d17b436fb
    role: context
  - path: pages/traits/morphology/fungal_constricting_ring_formation.html
    sha256: 4f62e41e24f0751180569afadbd724011d8a821bc3e3ef81a3adc7b499cf9109
    role: context
  - path: pages/traits/morphology/fungal_hartig_net_formation.html
    sha256: dba51c16019380749447a4fb9ad353d27a85655f845dfb0ab59e9bacb83d304e
    role: context
  - path: pages/traits/morphology/fungal_internal_mycorrhizal_vesicle_formation.html
    sha256: a845357a469f0cde806795365e318dedc6aac5625e0a0ca41b6fbc613c71ed70
    role: context
  - path: pages/traits/morphology/fungal_mycelial_cord_formation.html
    sha256: 8cb34572dc93436f3b3a6fb5354df310a6d4186d9ed5c84f0e6fb6717ce294c8
    role: context
  - path: pages/traits/morphology/fungal_nonconstricting_ring_trap_formation.html
    sha256: 9a440365f23c25e39c0fa847bdd329f9da1ce966d36e4a2eed601a1d36eee9bd
    role: context
  - path: pages/traits/morphology/fungal_peloton_formation.html
    sha256: 2f2484e775525d8c4c548f600c272816b3aeb464771eee329e2ca651c831e0e9
    role: context
  - path: pages/traits/morphology/fungal_rhizomorph_formation.html
    sha256: d20727e92f2db0d41e161af7212dca64fd8afd6943cb260a417cbadd5e9fbbdc
    role: context
  - path: pages/traits/morphology/fungal_root_mantle_formation.html
    sha256: 1620552732aa3073229f5366dfba9531b3dd25dc905daaea91b6edb34e876c40
    role: context
  - path: pages/traits/morphology/fungal_sclerotium_formation.html
    sha256: 97c7431a5e9c7e9fb14a6e7fff9b664ee652aa02b0b13c769cad44a150cfbfb5
    role: context
  - path: pages/traits/morphology/fusiform_shaped.html
    sha256: 1b3233e89549f9c1da4d0f8351ea55b5513a458709edc4b73eb97b5d005b056c
    role: context
  - path: pages/traits/morphology/gas_vesicle.html
    sha256: 56dee7dae0ba82abe276cd6def1d0814c2885de5e46a7e00ca345ad9202ac371
    role: context
  - path: pages/traits/morphology/gliding.html
    sha256: ee2e2564a3ad63fd00eaf31d2b697f9494fbe62eabb949e6bc5c17031d3104cb
    role: context
  - path: pages/traits/morphology/gram_negative.html
    sha256: 86a372893b3ead26b7f829399a52dcb76de260ee6c43401030a575d40fdc9323
    role: context
  - path: pages/traits/morphology/gram_positive.html
    sha256: 670c38e0565f099a477104e0242b5f183fc2ab9906c5999f361b45ecd9b2bd50
    role: context
  - path: pages/traits/morphology/gram_stain.html
    sha256: 57ac79653c8411b63da244a8894797372b669e3aceb91f88fd45b149ed9196b4
    role: context
  - path: pages/traits/morphology/gram_variable.html
    sha256: 6cccc5f19aa6f982de68a9a697210db4dc0160f94fb3d8652091fa9bf08bfa1c
    role: context
  - path: pages/traits/morphology/green_pigmented.html
    sha256: 3f09c8ffa00e059ef973182d87c18c1f3541d107f5150d85e50e0680f18fa64b
    role: context
  - path: pages/traits/morphology/helical_shaped.html
    sha256: 9dabd868eed043a5a43be737c7959416f97ee5c4e192ff8ee313cdb8af559051
    role: context
  - path: pages/traits/morphology/heterocyst.html
    sha256: 06ca6e30953c494b00e1f89c8c2422aad3b7aa7dc4a7dd2b223fe09177e03df4
    role: context
  - path: pages/traits/morphology/holdfast.html
    sha256: f30491c90f35d962d682e4fbd8657a9aa198323968a8741906acd130d1ca72f9
    role: context
  - path: pages/traits/morphology/hormogonium_formation.html
    sha256: 36a63dadba3a3c55e2256b2573bee38335de0ebb42d80c39370e8790998c340c
    role: context
  - path: pages/traits/morphology/intracellular_inclusion.html
    sha256: 392ef6d122e4a93058681e8ce210c131fddf78242e4841109a5c367a4df8fe1f
    role: context
  - path: pages/traits/morphology/irregular_shaped.html
    sha256: 073037118ba3496003a098faa34449678fde0b591c025c81cebd0a9ab3244274
    role: context
  - path: pages/traits/morphology/lateral_flagellation.html
    sha256: 49f11e142a637cc29bd45a2a2864e157db6332edc637274d298a0e0b31c9dbd1
    role: context
  - path: pages/traits/morphology/lophotrichous.html
    sha256: 69abc887c72ef94ca14f8b737724d8d1c4519f956e5f6d887c0a849525869037
    role: context
  - path: pages/traits/morphology/magnetosome.html
    sha256: b0b3d5be425435d381728bbf506d5d3e43c322ef4c4ce3e25050888eea933fec
    role: context
  - path: pages/traits/morphology/microbial_haustorium_formation.html
    sha256: d0f39db525e5093f6680e8abc31cb6fc71784c19c853218fcd3f61fb07e1064a
    role: context
  - path: pages/traits/morphology/monotrichous.html
    sha256: 37103a4f94f61f4e08c9c835dcdec3444b239bf20d9715b0773f53e848146240
    role: context
  - path: pages/traits/morphology/motile.html
    sha256: b81e356c392e6a615ddd2bea61ed6436800f4fa96528554042294afffdeb36df
    role: context
  - path: pages/traits/morphology/motility.html
    sha256: 66a3137f9302f433a59db9b90b4da7b8267b5c0486d2b4d5d681606c8a5de685
    role: context
  - path: pages/traits/morphology/mycelial_growth.html
    sha256: 76aaa3780141877605ca6a108e7c12ef8669629e2219406f152588371f629d86
    role: context
  - path: pages/traits/morphology/necridium_formation.html
    sha256: e45434a6357569a3c8465f9126c15504bc8f5ead1d57b9cf8413c61cb76b9582
    role: context
  - path: pages/traits/morphology/non_motile.html
    sha256: d501210c51e8d6604ad7d454866774d77be098d7ab45ecd80a6ff30628117468
    role: context
  - path: pages/traits/morphology/non_spore_forming.html
    sha256: 7e75515010a00f3fb7249a84fb8003f98f4de333b882420efcd9469d87fe0b54
    role: context
  - path: pages/traits/morphology/orange_pigmented.html
    sha256: d09dca0aa563dd1365a29cdfecd788d4e50aca3a986a518ef36b36dd5ca04cab
    role: context
  - path: pages/traits/morphology/oval_shaped.html
    sha256: 1fa348632d5bf38e5e7e9f2b2d15bf7b1d2fa4b7999aa84b320f7847175daf96
    role: context
  - path: pages/traits/morphology/ovoid_shaped.html
    sha256: e7a74f02d944f3f9802f1a9e01e3de1279b91bcb8e505d0f7b7954050a17622c
    role: context
  - path: pages/traits/morphology/palmelloid_formation.html
    sha256: e78be4e4b703652719b963bd3352aa2ac5a253471a78825e66eb734453fdda8a
    role: context
  - path: pages/traits/morphology/peritrichous.html
    sha256: 6db94a674c264ad6b5ca6d923c1018cd75e9ffa0ac4e6f0103cbaac7d7ac77e7
    role: context
  - path: pages/traits/morphology/pigmentation.html
    sha256: 7d76a63be852b2a7bfaf13693a2c88206ad5d60b83937de042d720393e427533
    role: context
  - path: pages/traits/morphology/pink_pigmented.html
    sha256: ee98b11a655062dd1d438e7c85107e5c9bc10cc3d91bfb21654f5a29744524f0
    role: context
  - path: pages/traits/morphology/pleomorphic_shaped.html
    sha256: 8bcb11e456e0875267245897eea5cf4d087759037d9985e251ea44a92ddcbbfb
    role: context
  - path: pages/traits/morphology/polar_flagellation.html
    sha256: a12317a51e2911bd4526f5569fc943da789c059a14545bdc702a18fc6d8f7948
    role: context
  - path: pages/traits/morphology/polyhydroxyalkanoate_granule.html
    sha256: de07b97cac3f45c6c44b0ab60be6eaa20626c5cecb1d1b8577220e67dfa2210c
    role: context
  - path: pages/traits/morphology/polyphosphate_granule.html
    sha256: 547127885bf1135260e25b355f1bd1b4b60d6a1c0e8786df3a7d9bc7a3e6b899
    role: context
  - path: pages/traits/morphology/polytrichous_flagellation.html
    sha256: a39e0077610c828ef3d201792da49b101b87cf86b71766cd9816dd6ccff5e487
    role: context
  - path: pages/traits/morphology/prosthecate.html
    sha256: e06d0a24d4444e30b0bd86f0796585b57f8d92d0b2587aa5dd29aaa4fe7d4765
    role: context
  - path: pages/traits/morphology/pseudohyphal_growth.html
    sha256: fa9f4c1a3faead421be809cf7159491442ef93bd6402f7d0dc39a6a07cf20ae4
    role: context
  - path: pages/traits/morphology/red_pigmented.html
    sha256: 7a43f50a36b457f1f4d4757b1de236ec1be3c7cc3a0c6a1501e6501fff70901d
    role: context
  - path: pages/traits/morphology/ring_shaped.html
    sha256: 697f915d02d17830d3a4fc8727a40751fc84f4540546772929e0bf3cdd1c9d6b
    role: context
  - path: pages/traits/morphology/rod_shaped.html
    sha256: d4699add5d1d110a8fd89568646350d44b8841e24236089bdca26bced11c9516
    role: context
  - path: pages/traits/morphology/rosette_cell_arrangement.html
    sha256: b30fd9dfb39379b385378523fdec688f0b7e6b6a50b3a227c8c6ddc307802656
    role: context
  - path: pages/traits/morphology/s_layer.html
    sha256: 04dcc01c4294c7e4af44cce7b9f8f738b7c70a83eb7c0003c97f06cb560efc6f
    role: context
  - path: pages/traits/morphology/sarcina_arrangement.html
    sha256: c00f997b8e8910b142c0491e7cf94804c7dee1bc96b997c57260f404bbdfe178
    role: context
  - path: pages/traits/morphology/sphere_shaped.html
    sha256: 721984165481288d4411a3ce9dc1712bb3cb279aeea141182f1301d4c71e6777
    role: context
  - path: pages/traits/morphology/spindle_shaped.html
    sha256: d5813623e07329ba09315899fe42e7f17acaae8ceb5996e3ef0cb5e2b75f670a
    role: context
  - path: pages/traits/morphology/spiral_shaped.html
    sha256: d598c4a256e89fb1e3e2f3aa03a5db4c5cabd85ebea0c6e1b2f13f3f36c97537
    role: context
  - path: pages/traits/morphology/spirochete_shaped.html
    sha256: 662d5635607b92ac80f910397c22f58346730bd0876779613d8cc37c692d9d96
    role: context
  - path: pages/traits/morphology/spore_forming.html
    sha256: 1667c619e45656ea19e20255799cd7b0777a88e67e43cae23fa185b44edeaa4e
    role: context
  - path: pages/traits/morphology/spore_shaped.html
    sha256: 3fb085de1f6ab5dfacaa02013f2f3c26a5b815576d2a372fe7d5103fd35a0f8b
    role: context
  - path: pages/traits/morphology/sporulation.html
    sha256: c80819243a964438b9df7fd5ccabec41a0541edb1874765c5ba5b002f3ebc431
    role: context
  - path: pages/traits/morphology/square_shaped.html
    sha256: 88a444bd8df8aad6dc2acc7b4e3f09cb12d6824ec9034e89ae5b1df084bc63ed
    role: context
  - path: pages/traits/morphology/staphylococcus_arrangement.html
    sha256: 8353f0e67cc0784d6d7c7174ce34b2b723437f3226d4ab83dff24df059e38ac2
    role: context
  - path: pages/traits/morphology/star_shaped.html
    sha256: 4f8307494c027d230ed2356926319d69d7264a36dec4d65db69e6b92692162ca
    role: context
  - path: pages/traits/morphology/streptococcus_arrangement.html
    sha256: c717a5a45361132dc69a19283377d8daf880f42edfee4df5befb3f307483139c
    role: context
  - path: pages/traits/morphology/subpolar_flagellation.html
    sha256: ba053cfde76ba756f5ead3d0d3e581135c217ff2ebe0cfdc789cfc6b0fefc6f2
    role: context
  - path: pages/traits/morphology/sulfur_globule.html
    sha256: 06670c6278d1c78bf2d9ecd6296b0f113ba0d4e2b27ee447f865399c69647493
    role: context
  - path: pages/traits/morphology/swarming_motility.html
    sha256: 7705d99376a188613d8a05b9415b4db42a322f9018d523fb631104d14bf3c9e5
    role: context
  - path: pages/traits/morphology/swimming_motility.html
    sha256: a776af9c08a051855265e49ae64cbfd062c6885b706ea28b63e1eaa363c875f5
    role: context
  - path: pages/traits/morphology/synnema_formation.html
    sha256: 415ff9927276f4cee2e48f7afbf686e6e040ae4c00f8270d111f1423d49baf74
    role: context
  - path: pages/traits/morphology/tailed_shaped.html
    sha256: 370a1cffc8bef9eb62eeb07c8a6fe89ec68c9d1c3490da214c4431919c9961c7
    role: context
  - path: pages/traits/morphology/tetrad_arrangement.html
    sha256: c0d91b9dc54e3c9031714d8f0a186e603ac6bcfd3a023eca2fefa17d4659f344
    role: context
  - path: pages/traits/morphology/triangular_shaped.html
    sha256: 66edc82c9c7559d4e72d2814b08791fcbf6df80a4d67ffaa3780973977f415fe
    role: context
  - path: pages/traits/morphology/twitching_motility.html
    sha256: 874e17229653775f581524706f37f07f11854c1a01c477ffeab6c269a16349fc
    role: context
  - path: pages/traits/morphology/type_iv_pilus.html
    sha256: c3a565420bc4c8ed1e87ac10f1fc44ca8269a674a097eac20b85f8000d4b9eaa
    role: context
  - path: pages/traits/morphology/vibrio_shaped.html
    sha256: e23338dd38fec12efd2ba778317a5e5766c5d39c4a6f71de2f52afe979d4fc1e
    role: context
  - path: pages/traits/morphology/white_pigmented.html
    sha256: 78e0b9e36e04c91e8a6da39cc4d9864710a88159c186c608ad22ad622c79ad28
    role: context
  - path: pages/traits/morphology/yellow_pigmented.html
    sha256: 040f3930ca59a0abf669a6ceb701863fb91890d4fc8df873865a4df3434c93a0
    role: context
  - path: pages/traits/observation/growth_nacl_observation.html
    sha256: 1cfcfe0a208e5451026b271c49e1bb36b9f738e30a29759d026b4a573a894ac6
    role: context
  - path: pages/traits/observation/growth_oxygen_observation.html
    sha256: 386b90898ed0e4da5bd02d19e42e75e840599ed8c08373dfa966468a9a6e257b
    role: context
  - path: pages/traits/observation/growth_ph_observation.html
    sha256: 426fd987fec5d047237a124264ef6d58018b82d921c9fa293547b438331ea828
    role: context
  - path: pages/traits/observation/growth_temperature_observation.html
    sha256: 8e1870d40677572e4d0aa4d173b39a77fbcf127d613895fa43daa7aced04e382
    role: context
  - path: pages/traits/observation/nacl_delta_observation.html
    sha256: 2a76cc08ea8406cbbbfe72fad4d6f6c66d80f4ac7217c2a0bd7718dfefcd10c9
    role: context
  - path: pages/traits/observation/nacl_observation.html
    sha256: 40072b85853e704112ad2924cb1182b779126eaa0043fbfb49e589ff1f00d932
    role: context
  - path: pages/traits/observation/nacl_range_observation.html
    sha256: a09741b42d5284c5f1a451131542e07f090a8d1baa7373b8d66d89b3b6dcbe3a
    role: context
  - path: pages/traits/observation/optimum_nacl_observation.html
    sha256: b0310224fa91cf26510ba7f7eca3d08de0bfafab0e5c5c2c0c6e34662c180a6d
    role: context
  - path: pages/traits/observation/optimum_oxygen_observation.html
    sha256: 5830a35be9ce365704c61e1fe1787f4d547d5e0f76c2fcbcd148f5e137f29d3b
    role: context
  - path: pages/traits/observation/optimum_ph_observation.html
    sha256: a8aec68b43ee052a3fa7dcc8c18494fe3a0e861bc7422c6cbdaf770cf77a3e43
    role: context
  - path: pages/traits/observation/optimum_temperature_observation.html
    sha256: 42e601f1ca07111652c155e1fc6bc252f24ee91e7ff3e7bfa1408edbb973da83
    role: context
  - path: pages/traits/observation/oxygen_delta_observation.html
    sha256: c9f2c29de95000b2eb3a8170c0d2d8a53fbb5e9ec554a72e42cc48a1a57e0279
    role: context
  - path: pages/traits/observation/oxygen_observation.html
    sha256: c5303035d7e7cfdb298a63f71526a08ccd256dc917dd3a73d2136ffdbdf20d23
    role: context
  - path: pages/traits/observation/oxygen_range_observation.html
    sha256: 4f5a3b13ac1be51f3c9f8d70442cf1f650f4c79540e0e4bf8072f9523d654aee
    role: context
  - path: pages/traits/observation/ph_delta_observation.html
    sha256: 18c0b31ad0f4276255f95e7018f3b6758ecae1078243ff0a6864f5e02b9da452
    role: context
  - path: pages/traits/observation/ph_observation.html
    sha256: 8ffc362bfe00fa1b751f61299b802e6eca578f3df32247b968392cb788ce8463
    role: context
  - path: pages/traits/observation/ph_range_observation.html
    sha256: 322f7c13720f3c7a3987ac75696002203fbdb41c9d009aa1cb8d08be1aa4bc4f
    role: context
  - path: pages/traits/observation/temperature_delta_observation.html
    sha256: 330254255214d4a52f2839e367f825736f24d4e61f5581bc77f02a0c4e983408
    role: context
  - path: pages/traits/observation/temperature_observation.html
    sha256: 43bf88151f38378da7b235c586ab536e70733a52e0a3ba227011f7bef23285c9
    role: context
  - path: pages/traits/observation/temperature_range_observation.html
    sha256: 832bfb5caba52958912dd537074fbab5f3af9da0f23cef3d6184554d1500b4fd
    role: context
  - path: pages/traits/other/catalase_negative.html
    sha256: 02a9f9ce349aa973d0eb5e37bacb71c254f66bbe2dbe6c1d57530867770efadf
    role: context
  - path: pages/traits/other/catalase_test.html
    sha256: 696fc57af73393686eeed17bd74912c2afede23dd140003ad93a5f18e6f4d927
    role: context
  - path: pages/traits/other/circular_colony.html
    sha256: c18dd37e5fa447022a45d65df69907ca4626519331afcf2b73d9853ce6246a3e
    role: context
  - path: pages/traits/other/coagulase_negative.html
    sha256: 214fe83dfd6aabc8f11749af848d962c23875f604b356ed395cd1b69685126eb
    role: context
  - path: pages/traits/other/coagulase_positive.html
    sha256: 45cde966ecbc915ae205137a5a0a0116075d6a01adc82810fc9e4543b0188ef6
    role: context
  - path: pages/traits/other/colony_morphology.html
    sha256: 4afcb98192e761319ae7656bd5ee49ff8ea9631081ba8fb3c33ff56330667ead
    role: context
  - path: pages/traits/other/colony_shape.html
    sha256: 36eadc0f520049fac586f7e70ff04d47c7fa45ed639c3d261818736406e3286a
    role: context
  - path: pages/traits/other/epibiont_phenotype.html
    sha256: ce509dca33e976f9b714b5ca2e7498e4a20513000895d8c1979c04930d560eb6
    role: context
  - path: pages/traits/other/filamentous_colony.html
    sha256: 49149bc9454dfaacdda51747729290d7793b047c8f7bb2c1f9146c8b1f54676c
    role: context
  - path: pages/traits/other/fried_egg_shaped_colony.html
    sha256: 80fefd262b81fc1606276e703556ac3781182582c768b9f254f1f0ee50009bf7
    role: context
  - path: pages/traits/other/generalist.html
    sha256: 24ed998b9ea3a019aee1f613a14cdafdfbbfa3c8b6eb490a25f145dd3e0ac6ac
    role: context
  - path: pages/traits/other/hemolysis.html
    sha256: e7575c7f27ab55913feab1ceb9fa8ba4e2e59e0fdc1f448b014e0de880b27f6c
    role: context
  - path: pages/traits/other/hemolytic.html
    sha256: ce32cc9f623cc18720c026e29830b79cc258dc5e2ad3962d1aecc45f6e7d76ad
    role: context
  - path: pages/traits/other/indole_test.html
    sha256: fb9f7fd10fceff138a2a64db8baabeee80843b50c2c8ea1431d9c96404ca36bb
    role: context
  - path: pages/traits/other/indole_test_negative.html
    sha256: 23831434a814e00fcbe67e77128b709beee4833e628a1f0eeaff9a3fcb36c201
    role: context
  - path: pages/traits/other/indole_test_positive.html
    sha256: 3327676b361993ce22650584a72751dc176362a030a86681edf64cc47fa2d0a9
    role: context
  - path: pages/traits/other/irregular_colony.html
    sha256: b231f3a9846e318c855453c33bad335428c222d12c6ec3d097104caafddf6498
    role: context
  - path: pages/traits/other/methyl_red_test.html
    sha256: c7edbbbe07c6cabbc2f028aaf8c5426ab7273fa8c624fcfce978b0567c98cc33
    role: context
  - path: pages/traits/other/methyl_red_test_negative.html
    sha256: 457bf759dfc0b7b6afe1d5527235c9aaff742c8d7d955fe320dfbb8b28861a7b
    role: context
  - path: pages/traits/other/methyl_red_test_positive.html
    sha256: 5d165ccac6d8ee2b58b03c7fa700a5743507ad3a1dff0a12c6b963e21ea977e9
    role: context
  - path: pages/traits/other/non_hemolytic.html
    sha256: b3dd8bbc8ac75c61c02f451d779f1e4ddeb0ce0d246ab7238b1660290989334a
    role: context
  - path: pages/traits/other/osmotic_tolerance.html
    sha256: 0b714a21692d6595b736a85bd7907a6e5a70e7261322d351244d46ab56d0ff89
    role: context
  - path: pages/traits/other/oxidase_negative.html
    sha256: e9420c24da92d77aa250712011cd99682983330fd22921493783e656e24bffc6
    role: context
  - path: pages/traits/other/oxidase_test.html
    sha256: bcdf89523a98208f9a4d0570dec7a8a01c72db02d2d4b7268bc58a2284448fe2
    role: context
  - path: pages/traits/other/punctiform_colony.html
    sha256: eec524354a6f5816448222ca8c69fa4cddd192531f9c685a2e1e75996b76f375
    role: context
  - path: pages/traits/other/rhizoid_colony.html
    sha256: d0624a4a35e19363705a84eeeb6fefc4f8e32409f5837c858270699aec842eae
    role: context
  - path: pages/traits/other/specialist.html
    sha256: 99419da3acd9c7bf6c8e7e7f287559d04113040588a66da6e0956ba924a230b9
    role: context
  - path: pages/traits/other/urease_negative.html
    sha256: fa723412fe8daa724ba01bcb53cbfef61d0cb3a3d9852117f151fe495eb8c9ce
    role: context
  - path: pages/traits/other/urease_test.html
    sha256: e0d961e1a688311246d3b77fcc7c88d355bb9019785cf102d5f5c0d55f34e4a3
    role: context
  - path: pages/traits/other/voges_proskauer_test.html
    sha256: fe375614447414a61a62102e3264ea7ad67dd14444576eec35dfe056807f9f68
    role: context
  - path: pages/traits/other/voges_proskauer_test_negative.html
    sha256: fff9983c4d8500ca5b3e03a4f84e344f71a05d2b046ab96c896de9f41a2868be
    role: context
  - path: pages/traits/other/voges_proskauer_test_positive.html
    sha256: b2aca4d0f6add606d3e0f4342f3e2f71feb10a7a6f988894759f49932ee0751f
    role: context
  - path: pages/traits/physiology/acid_phosphatase_activity.html
    sha256: 2c1ffceaacc1f4149f57159a3f7adecfa354d8964916a2b6b5de06da7641a1ac
    role: context
  - path: pages/traits/physiology/aerobic_anoxygenic_phototrophy.html
    sha256: 6d17d61e1e1ac3650aeabba8c98a959ea7d1120ec21ec05fb8cba5c88a788d5f
    role: context
  - path: pages/traits/physiology/aerobic_overflow_metabolism.html
    sha256: 74fef0aba8aca19b7613cb6384894cc382aa038797c485624a193a26384bb233
    role: context
  - path: pages/traits/physiology/aerotaxis.html
    sha256: e5a420d22281572097cc291fbbe0b76487badfc43b556df0b647f2b22baa1dfb
    role: context
  - path: pages/traits/physiology/aerotropism.html
    sha256: 12cd8fc4626bdbbfac1fcf823f25fa3d720ea69108f3c5cb611ee2f87f130aed
    role: context
  - path: pages/traits/physiology/aggrephagy.html
    sha256: 8b8698fade4603964dac08783ea1cdf0f391cf499153682c36effcc7c02477cf
    role: context
  - path: pages/traits/physiology/alanine_arylamidase_activity.html
    sha256: dd2374e04762c1fba9923f93081c785bb7b9d85763d08618ada14a4171f51d5b
    role: context
  - path: pages/traits/physiology/alkaline_phosphatase_activity.html
    sha256: 81cd954999b980d432ad82a34f997119404c7739586d07cc01299017ee547c87
    role: context
  - path: pages/traits/physiology/alpha_chymotrypsin_activity.html
    sha256: ce82d40c2882115c5c6e16cecc144c5b3f11205a36f3ca1a07432bbac1cbd9b8
    role: context
  - path: pages/traits/physiology/alpha_fucosidase_activity.html
    sha256: 70ce0a60837b8d9b1ad799f2387697dce1c1ac7692675129cc5ce973aef064f3
    role: context
  - path: pages/traits/physiology/alpha_galactosidase_activity.html
    sha256: cfa6e1e63745cfa6f8819e3798e385cf6e657b8c156d5adf9b82d3ad1a98140b
    role: context
  - path: pages/traits/physiology/alpha_glucosidase_activity.html
    sha256: 8138f9b25bc1a558cf4b24ac2169b294c9095df10a5568c838dff66c3cf925ac
    role: context
  - path: pages/traits/physiology/alpha_mannosidase_activity.html
    sha256: 938fc0ae0919be64b58a6175b3233ff003eaec80fbd9f00c1d4a27c0dd952c9b
    role: context
  - path: pages/traits/physiology/amylase_activity.html
    sha256: 14a275867da2ca707a56f33309628bda966ca6c76dee01f024bc020c0c75af9f
    role: context
  - path: pages/traits/physiology/anisogamy.html
    sha256: 143ef718acd8c368844ff16090a2e8e8894aebb492e749fd3d98ef9c84030bf0
    role: context
  - path: pages/traits/physiology/antibiotic_resistance.html
    sha256: 370885b4e12ad49337a54e6343174d46b581536d6f0b9d9d646c35e876a9fcf6
    role: context
  - path: pages/traits/physiology/arginine_arylamidase_activity.html
    sha256: 695ddbf5ac23790895eaf58e150d166aa2c845b6b1be3c844281ec22419bdb09
    role: context
  - path: pages/traits/physiology/arginine_dihydrolase_activity.html
    sha256: 1bbaa3001f59d72923249ccf9671cf2b49aa987d7a3981f78d09f8124b10774c
    role: context
  - path: pages/traits/physiology/autogamy.html
    sha256: d63d9c47e77167cad7c06e5420f030fe52723f35fab0c72ac4a56b82ab28f0f9
    role: context
  - path: pages/traits/physiology/automixis.html
    sha256: 5a133419ac3e6fcf4340cdca66246e8a55db110034619c691caef4b803558455
    role: context
  - path: pages/traits/physiology/autophagic_glycogen_degradation.html
    sha256: 5ecf85ac41d8e97c6a6da8d8fe92fb0638776781496d4a3686299ae0ee376031
    role: context
  - path: pages/traits/physiology/autophagy.html
    sha256: 165bacfb033622b8d8f3fc4349d9d1b04ef7aab32d7a1d89960cce481a154d1e
    role: context
  - path: pages/traits/physiology/autotrophic.html
    sha256: 5f739b6795ebae645c0f32570a8900dbdc9d010ed977749b75011b7c27ea789c
    role: context
  - path: pages/traits/physiology/bacteriocin_production.html
    sha256: 8ef86cd6b3300b74da4ccf4d06cd7b4e94063ae1c5197a156059b37233ef0bd7
    role: context
  - path: pages/traits/physiology/ballistospore_discharge.html
    sha256: 37513ea239424e2a7827a8c81dc69051cdee5ebe94b2df839b15c5be46e07118
    role: context
  - path: pages/traits/physiology/beta_galactosidase_activity.html
    sha256: 8923dea1c9341e019411603d30c2f3e9f8fe4b24e5903223dc0de77e4dafcf6a
    role: context
  - path: pages/traits/physiology/beta_glucosidase_activity.html
    sha256: 49db06b6554f5fa27eca2a24e21c1e4cd823063eea9fb0f8c0a2c36bb59d09a8
    role: context
  - path: pages/traits/physiology/beta_glucuronidase_activity.html
    sha256: 9936b1ce91c2e4ff28c5f4becc58eb54a9d69dd263b7b4d2d11cecbe25c20c02
    role: context
  - path: pages/traits/physiology/beta_n_acetylhexosaminidase_activity.html
    sha256: a20c7c9788a947b98b78e6779293acbca1578a20dc8bdb8dcdc7a2a25bf4a4b6
    role: context
  - path: pages/traits/physiology/bioluminescence.html
    sha256: 4a706b555d722cdafe36452c87bfc6980e50a8f41dee1b52d226abb28c21dd60
    role: context
  - path: pages/traits/physiology/biomineralization.html
    sha256: 2db91a342ddf2e9888a45ca940d2b1ea8d39c47c0974f164fbe8d3030d8f63c9
    role: context
  - path: pages/traits/physiology/bipolar_mating_system.html
    sha256: 96b9ed453c6d35a46cf9446a5bfa3553c4c6876ef92a3e8152f2eb27a43ae908
    role: context
  - path: pages/traits/physiology/carbon_source_memory.html
    sha256: 4773093d39c05334131bbedd9b489d3bc6c2c6f88197d1c78c40b3f88b70085e
    role: context
  - path: pages/traits/physiology/carboxydotrophic.html
    sha256: 8bf812250a0cfc418437827c67641ff9b3329bcc5fd40ddda0fc4d6642de2294
    role: context
  - path: pages/traits/physiology/carboxylesterase_activity.html
    sha256: 107eefe739c1f1a2e989524f3aa2fcce44a94d94bb4e9d679c5dff5948f79c23
    role: context
  - path: pages/traits/physiology/caseinase_activity.html
    sha256: 8298d9072d1f58deabd357c87a1796c5b4c0a7035c28ae186b859fc4b4cd985e
    role: context
  - path: pages/traits/physiology/catalase_activity.html
    sha256: 856ab30bb90d691f138322b1f40b145cbc19a0a0b7eda11012f75fb646e4cc44
    role: context
  - path: pages/traits/physiology/cellular_buoyancy.html
    sha256: 59acd2005473943dfdd763eae08dba6df93b2cac810edaea4bbd192b089e48a1
    role: context
  - path: pages/traits/physiology/chemoautolithotrophic.html
    sha256: a40b65f4fa351f0506cad246dd4b1a90b7501943e54a578f804112669529ae9b
    role: context
  - path: pages/traits/physiology/chemoautotrophic.html
    sha256: 56b9eceadc192e597a0553a56c7dc8d50640adcd737582d510cb95a10284f268
    role: context
  - path: pages/traits/physiology/chemoheterotrophic.html
    sha256: 735657b3bda0e4912cc5c56cdc0bd6a916b8bed0f239fd39a31e430f8245e943
    role: context
  - path: pages/traits/physiology/chemokinesis.html
    sha256: a8620f0204181c0bb30bc902d717f9fe10130bc8c0315a68cf900439e2f05049
    role: context
  - path: pages/traits/physiology/chemolithoautotrophic.html
    sha256: a13a22ba1b3236300f92e9c23d52d86562d0f480a273a4867019264aca1c96ee
    role: context
  - path: pages/traits/physiology/chemolithoheterotrophic.html
    sha256: 41fcd58f8b95ce2fb69423a47e579e318eea662949f5469f7149e181928c6777
    role: context
  - path: pages/traits/physiology/chemolithotrophic.html
    sha256: 029cfb1a46e7502eb034bd11b7d2be23b4c723e14b83f5dbf97f54ef3b011c7e
    role: context
  - path: pages/traits/physiology/chemoorganoheterotrophic.html
    sha256: 1436441507e76399720650086801d15f44d856ad6ca5de0e483e771784efb0f8
    role: context
  - path: pages/traits/physiology/chemoorganotrophic.html
    sha256: bbb76dbcf9fea9befe5676c83c615c592c6d5a46d3b20895f88d1324f74a6764
    role: context
  - path: pages/traits/physiology/chemotaxis.html
    sha256: d936b416c27630232de59fa191a64341c271238cc14c07905eb427a9a641ea81
    role: context
  - path: pages/traits/physiology/chemotrophic.html
    sha256: 1fd3c5c100bdba4d5c108637b4487d07aad2e33d7255fc67b0e0846c8929bbec
    role: context
  - path: pages/traits/physiology/chemotropism.html
    sha256: c749d77623e1fe27d52268449afe5d3feefc4ef922895736edf5409434e8ad18
    role: context
  - path: pages/traits/physiology/coagulase_activity.html
    sha256: f3228aa9c7dd05c95d87d4a755742d979c1c2423c70cc88bf703f213d7341f17
    role: context
  - path: pages/traits/physiology/coccolith_production.html
    sha256: 3dab49cd5eebf232290f8cca32d73220510594d2a60e469bf54d2e6867586540
    role: context
  - path: pages/traits/physiology/cold_shock_response.html
    sha256: a1e33de51fbb0b5dfa0f370d9a437bb20eb5af7f60ea643bfa787940ff60c3e8
    role: context
  - path: pages/traits/physiology/contact_dependent_outer_membrane_exchange.html
    sha256: 96cfd403471aefa500183c0f67b22feb4785cd0fd4a8ef08c41c54030b00b45c
    role: context
  - path: pages/traits/physiology/copiotrophic.html
    sha256: 1216925011acb77ba80251b35e8821f6732635a64fd724a9971098ea37386de5
    role: context
  - path: pages/traits/physiology/cue_triggered_environmental_anticipation.html
    sha256: 78e823498f881fe84c40d3b09dc33ff3031579457058407e9d5d878fd3ae080b
    role: context
  - path: pages/traits/physiology/cystine_arylamidase_activity.html
    sha256: 05e92c5886193615335c283d61c46cea28466830d1de389a030dbaf434314125
    role: context
  - path: pages/traits/physiology/cytogamy.html
    sha256: 93942b0782a9ea3432d2f5203bc40ad4171e3e509a284b1fbefb7ffe9e4ddbf5
    role: context
  - path: pages/traits/physiology/diatom_frustule_production.html
    sha256: 6e2f016f7c2ad3342e75d9db82e7eaf17aceca3a0cc884485076a7f64f8f331c
    role: context
  - path: pages/traits/physiology/diatom_perizonium_production.html
    sha256: 37121753514b81c5305346ac76a148e999548d312ca33acf9d59af4e02578ee5
    role: context
  - path: pages/traits/physiology/diatom_seta_production.html
    sha256: f91c0df2fc8ea9707d6d2f39b9b0d0abcccb7904d7be3981e24d8ecbf35e95d8
    role: context
  - path: pages/traits/physiology/diauxic_growth.html
    sha256: 23d7c6815f7bd06c801cc239c977d1828081651a73adb4dcf49dbbd37dc3d157
    role: context
  - path: pages/traits/physiology/diversifying_bet_hedging.html
    sha256: ef93b6aa10315ffe38991c1bd856b09ff56797b7ace56bad8ca212613c246ee9
    role: context
  - path: pages/traits/physiology/dnase_activity.html
    sha256: 643b773076dc52bd80217b610a585288e77cfd6cce0908546aae1f819aa9185a
    role: context
  - path: pages/traits/physiology/dormancy.html
    sha256: bc2c4c65425c8ae66f940d28f66ab38b256f39b70de72c7d0880187cb4d71027
    role: context
  - path: pages/traits/physiology/durotaxis.html
    sha256: cceaa98f7c49a9beca25d424a9bc7bc765bfe75d70a481839edc36f4a19d91b7
    role: context
  - path: pages/traits/physiology/endocytosis.html
    sha256: ea1ca5434ba5c47402a8a438b70f3b43531d7d0f7fb1538b04cb104d1ad12314
    role: context
  - path: pages/traits/physiology/energy_taxis.html
    sha256: 8c584806842e89b51ea3ff8bce6af9fe05f9dc85ade771acb2dcf20759b357ef
    role: context
  - path: pages/traits/physiology/er_phagy.html
    sha256: 43d62aac207b6ff2f1ae9b6d2d9cbbeecbe6ed30e17ca41f6c22a8ebf6737418
    role: context
  - path: pages/traits/physiology/exocytosis.html
    sha256: c253651026fb201374e89fda712d4adcf7ef0a9fb54b17412bc92803acf1f6ce
    role: context
  - path: pages/traits/physiology/extracellular_membrane_vesicle_production.html
    sha256: 3657ff7bc09b16a8eb24163fed501d3e433da8a3461b033957147b12ed27668e
    role: context
  - path: pages/traits/physiology/galvanotaxis.html
    sha256: 419954db6260407e11224b28d9e920d8efc0440284341061cd8cfd9f2fb1cf45
    role: context
  - path: pages/traits/physiology/galvanotropism.html
    sha256: 07ae4e4fb807a3e19570201717d1fd85e0a616a1eccb69ed6a74ed1465963ddc
    role: context
  - path: pages/traits/physiology/gamma_glutamyltransferase_activity.html
    sha256: e1f8818233c829abb8af224bcd00a89bcf22c9091433d50765e3bf01192b0f4a
    role: context
  - path: pages/traits/physiology/gelatinase_activity.html
    sha256: 8ae479a4bc7fa5025bc742ed13d42046ee8bdd173e2f37fc977e3135f8f56b14
    role: context
  - path: pages/traits/physiology/glutamyl_glutamic_acid_arylamidase_activity.html
    sha256: db25c9487662c9bda471f700824fa29083d1c73431d29bd623c56e507986ecc3
    role: context
  - path: pages/traits/physiology/glycine_arylamidase_activity.html
    sha256: 5e4d1aca1ceb0d287dfe098b65be31273e644a10e580c52a6365a900c11bce3e
    role: context
  - path: pages/traits/physiology/gravikinesis.html
    sha256: 91870a87c3d6ef2bbc9710120e2b642e061b163945cc6798944c4d6fcdda1209
    role: context
  - path: pages/traits/physiology/gravitaxis.html
    sha256: 1b2e614c67f3fcdceee1546c066e301de2fa258fca4fefb8ee768b560471a6f8
    role: context
  - path: pages/traits/physiology/gravitropism.html
    sha256: e64daa01bd1b1feb5c9f1009f174979d102fff4144d057f54d2a6ff535e32dc6
    role: context
  - path: pages/traits/physiology/gyrotaxis.html
    sha256: 182bb164715725d7a5a29ba58f91d641ac928ef09ac5c689e52e979c739fedc1
    role: context
  - path: pages/traits/physiology/haptocyst_discharge.html
    sha256: 98660fc2e2bcc0b667a0d7227690e56c17a1ef09408da10bf87068b60fe7d989
    role: context
  - path: pages/traits/physiology/heat_shock_response.html
    sha256: 2720ecf3c4dd1b034fb3b2137e9b2b608f06a4665e50e5ed435a8d72025738cf
    role: context
  - path: pages/traits/physiology/heterokaryon_incompatibility.html
    sha256: dbfd2c32ae1b831644d7d2c15e88d26a490010a9657be145935716d87e74510a
    role: context
  - path: pages/traits/physiology/heterothallism.html
    sha256: 92ba512f159366d89a815100d8441e62037f30d2a7a5f4b5ab6b7607ce7f00f0
    role: context
  - path: pages/traits/physiology/heterotrophic.html
    sha256: 5870b29acad155e56da05d5b86a58dbe27ef1d82ba1777dd9a72e51318dc50ac
    role: context
  - path: pages/traits/physiology/histidine_arylamidase_activity.html
    sha256: 14a02d9db8c196a3de2588fb0f7629a6de0fb5d60bbb9ce05cb6d9eafb2e0286
    role: context
  - path: pages/traits/physiology/homeoviscous_adaptation.html
    sha256: f48b7f72b0d414e70703240eb8283182562311b57d2d630bbe3be72c117244f8
    role: context
  - path: pages/traits/physiology/homothallism.html
    sha256: d632f28f86b661871828e87b23f2f76f51a6959abec560e00d7d990b52e9f47e
    role: context
  - path: pages/traits/physiology/hydrogenotrophic.html
    sha256: 4ce119f4871b979096761ce6776c549a6a0cd5ff9681edb59e25601a7bd34a62
    role: context
  - path: pages/traits/physiology/hyphal_anastomosis.html
    sha256: ce57822acde01fb1e52757595304828331b0421edeb875d843a17a463305d09d
    role: context
  - path: pages/traits/physiology/isogamy.html
    sha256: 01bbc9f652b3fa80fb3f47e257349e717c5cb6338ff593c90ebb4c215637bdbc
    role: context
  - path: pages/traits/physiology/karyoklepty.html
    sha256: ccb5ea7d5692a059a7cddfbe2f4822f777b14e6cbf07d0f9ccdf773072c7ed39
    role: context
  - path: pages/traits/physiology/kinetocyst_discharge.html
    sha256: 40b64cf57e2958816d58eeb7a694f94a233616fe21185088aea127a754659d8b
    role: context
  - path: pages/traits/physiology/kleptoplasty.html
    sha256: 26848ad6f575890c19a1449d47985ce108576193f77c2aa2d5f4be0afe9f5b22
    role: context
  - path: pages/traits/physiology/lecithinase_activity.html
    sha256: 13a2c27cd96bef4246da9c3b2e2971cd7615c5fe811f04e796f6fdcfac8fb0c4
    role: context
  - path: pages/traits/physiology/lethal_algicidal_activity.html
    sha256: 68367f087999bcb318c13c9eed38cd06e7be2607e244d9bfea8c1c89de23be77
    role: context
  - path: pages/traits/physiology/leucine_arylamidase_activity.html
    sha256: 57a0b457201369adcb09fd20fe5f5873f1751a6bcaa6834acba3ceaca000d58d
    role: context
  - path: pages/traits/physiology/leucyl_glycine_arylamidase_activity.html
    sha256: ddd47c7471f837170e28c29058631630870469fccd467da2adeed4515a5174d3
    role: context
  - path: pages/traits/physiology/lipase_activity.html
    sha256: f0731ee609b567902cf6ffc5d7ac8e39ae236aca5c662f4b88bf7352141be0a0
    role: context
  - path: pages/traits/physiology/lipophagy.html
    sha256: 9a553663c0d4956ea8d000879dfc915250bde597a09611248291817a2efe7a3d
    role: context
  - path: pages/traits/physiology/lithoautotrophic.html
    sha256: 71740ebc3067f25be3281b85fb8bc2ee3d89f9bc8bc810662f11069ab594d157
    role: context
  - path: pages/traits/physiology/lithoheterotrophic.html
    sha256: c92f1fb7683a66bae187f33d4663b24255d6dbd5beefc5d3aa16df3f3b9b3423
    role: context
  - path: pages/traits/physiology/lithotrophic.html
    sha256: c851d6e7bc601b7c61135f9a858c43545ea6264ff9dbb85c3ab86187ef5bd91e
    role: context
  - path: pages/traits/physiology/lysine_decarboxylase_activity.html
    sha256: fc6a2e42f10f6763af1af5e0852418f57aaf0cfeee27f5cac8f73b73186e3986
    role: context
  - path: pages/traits/physiology/macropinocytosis.html
    sha256: 13b3a3442397266e08b9aab225c53c510e18bf2769ddd2b0193a74a01fdb702a
    role: context
  - path: pages/traits/physiology/magnetotaxis.html
    sha256: 8f35f2ef3ba1adac392d94b9aeb02005ed94e4e18caa621078ec520aa87dff35
    role: context
  - path: pages/traits/physiology/mating_type_switching.html
    sha256: a2fc894197029e57aead96d65cb7853e25c9f9d6721a8446e99658abdc1e073f
    role: context
  - path: pages/traits/physiology/methanotrophic.html
    sha256: 7e4dcb6ccb02e58f4ea7af59a1f26e4874357b36860a408fc8197218b4c54deb
    role: context
  - path: pages/traits/physiology/methylotrophic.html
    sha256: feb48d5f505e9584e774d87857f94ccf0864349459f6bfb3c48652b76e718326
    role: context
  - path: pages/traits/physiology/mitophagy.html
    sha256: bfe85e5ad283ec9d424115dccc88580fc5bb5e387cf7905b911f409714d2a895
    role: context
  - path: pages/traits/physiology/mixotrophic.html
    sha256: 01d964ed30849537a4610332018298e0ae5b9e08ea7c4c9957106b5ab28b4a4d
    role: context
  - path: pages/traits/physiology/mucocyst_discharge.html
    sha256: ef2e18b7279a6a8640ee5e824caf94f27524e3d2ff2fc1baf0761d0d467a646b
    role: context
  - path: pages/traits/physiology/myzocytosis.html
    sha256: 5c9c880d5fd43bb39da30da877d2791e0f54af33033c4af14382c223d60cd39c
    role: context
  - path: pages/traits/physiology/nad_dependent_alcohol_dehydrogenase_activity.html
    sha256: 1e1e01bc08322bb17bbce63936c5a884b6c128e65f61de438376afff8618dbdd
    role: context
  - path: pages/traits/physiology/naphthol_as_bi_phosphohydrolase_activity.html
    sha256: 0c09ba8b4727a741d1a2bbc0f6c7785514211d4dc660ba7c8abdb113c9330993
    role: context
  - path: pages/traits/physiology/natural_competence.html
    sha256: afda30129530949f7b0c08718db2b3bb71f88dbdf3dbc9740b7c6a8cdb86b0f2
    role: context
  - path: pages/traits/physiology/negative_autotropism.html
    sha256: 1e71410171b634f1b8883f9d7c4271eb7131c8f1fd883ce25814a97f315c61e6
    role: context
  - path: pages/traits/physiology/nucleophagy.html
    sha256: 0c79fc105830b657c1c296a3cbbfd646128d48ec6b357951f327c2e1b2347237
    role: context
  - path: pages/traits/physiology/nutrient_adaptation.html
    sha256: 891af51c3719fc41f7c4f794b4f8d1fbcdb460407d27aab0471825526bd28434
    role: context
  - path: pages/traits/physiology/oligotrophic.html
    sha256: c93d635ee5afb28bcc66be2fce8d9caff3ecf1506b709f0b3f231c2611210a68
    role: context
  - path: pages/traits/physiology/oogamy.html
    sha256: 6c7b961130a38f1d7d71f157492f32cdf477f50f9250ac3c5cdb0548c3ca16e3
    role: context
  - path: pages/traits/physiology/organoheterotrophic.html
    sha256: 811c9ad35cc52bc37aaef7e030da2fd536e7f535f00972f35f457907543d635c
    role: context
  - path: pages/traits/physiology/organotrophic.html
    sha256: aac6589ef3fc4c84355787ccd9462d1b1f905ac4a24e2d5ebc5f72eef535df61
    role: context
  - path: pages/traits/physiology/ornithine_decarboxylase_activity.html
    sha256: 08423cf070986cf54eaa850ad05942dcae261313c6315d0e36bbcfc63aaecb7c
    role: context
  - path: pages/traits/physiology/osmotaxis.html
    sha256: def2cb72e690154242109793508f4904ea24ef5cf538966356729a677bee531e
    role: context
  - path: pages/traits/physiology/oxidase_activity.html
    sha256: ea69a433ef5a75df0462e91f310216a1b6bd388c5dde26851a6dbf0535819644
    role: context
  - path: pages/traits/physiology/oxidative_stress_response.html
    sha256: 857e51d5a40528d654145fbe320a5e47c96c74084883cfe54e1c1720ba0e78c3
    role: context
  - path: pages/traits/physiology/paedogamy.html
    sha256: 2126501f18128078830e8bef183828cfd71fa245e3644582a5f95f2737893230
    role: context
  - path: pages/traits/physiology/pallium_feeding.html
    sha256: c44252c93f677f3e620b6606928365a7e6dd2ac7f3c9aeac2d03adc1f0e3f74e
    role: context
  - path: pages/traits/physiology/parasexuality.html
    sha256: 4191fbbc034430c5f418af0b605c67db4092a5b0d882ca3f9e746ce37d1b3f2a
    role: context
  - path: pages/traits/physiology/persister_cell_formation.html
    sha256: 05f9b2933bf4a072ab3d110d1fcf62d4eea08aecc1f509064d3417c571b20fe7
    role: context
  - path: pages/traits/physiology/pexophagy.html
    sha256: 3da1521c8d2eae6fb70b800a4f83cb8cb2feff2bbe63df68b4be844c5e63eb91
    role: context
  - path: pages/traits/physiology/ph_taxis.html
    sha256: d2b7621b944d27f87160162c01a9103a5f0effe0278a17e05e928ed3c90581a2
    role: context
  - path: pages/traits/physiology/ph_tropism.html
    sha256: 90e7297fa7dd59007b7007baa6385d247003dfaa9de4c373931c9551e4605c94
    role: context
  - path: pages/traits/physiology/phagocytosis.html
    sha256: 80803963eb9d419b10b59c787394a7af78eb5d46d6e906546c5817899ba051b7
    role: context
  - path: pages/traits/physiology/phagotrophy.html
    sha256: d79b4df5303f77ec9875b435315bd039825a67545cb1841c9320e4260e5a6791
    role: context
  - path: pages/traits/physiology/phenylalanine_arylamidase_activity.html
    sha256: b8112a4b249e8b3f75fc014f1a2a32191da9f2b8d0b2d6ec1eb418e4dd5eba7b
    role: context
  - path: pages/traits/physiology/photoautotrophic.html
    sha256: 07ac89740c0f298c07c537d4c01b756b06e3e4e37a0fe1b2944ca02435b1ab80
    role: context
  - path: pages/traits/physiology/photoheterotrophic.html
    sha256: b07374399a6ce947f3ac0d53fcaae343a597e7b7713829faf8431b4164dd1aef
    role: context
  - path: pages/traits/physiology/photokinesis.html
    sha256: e7201480738281d1bcf6f3e4552936bee4d716c738a47062624e89a4ac7ebac5
    role: context
  - path: pages/traits/physiology/photolithoautotrophic.html
    sha256: b9e06b5d355849380d3000d2b790ddf0d926c8b53ad21a7b6ac0dde6770dba4c
    role: context
  - path: pages/traits/physiology/photolithotrophic.html
    sha256: 170d80a797f8a883412c2d6c62167d14da6fa7249145eae3d7d44da3365613ff
    role: context
  - path: pages/traits/physiology/photoorganoheterotrophic.html
    sha256: 7466847c3ee555499a4167cfcde81c1fbdf3d24f38f59069f072ceb1b25011f9
    role: context
  - path: pages/traits/physiology/phototaxis.html
    sha256: eb915691b8058eeabda1189328022bc94f36509dcc38c087cf74b762ea395598
    role: context
  - path: pages/traits/physiology/phototrophic.html
    sha256: 2a958856c38c48f4d0342739b725ffc7117e4cb21c3a01f8704dad33b2084b66
    role: context
  - path: pages/traits/physiology/phototropism.html
    sha256: 989e6098c939f5375291aecfaea59e6f88392613df66ffe2f0822b311167ed5d
    role: context
  - path: pages/traits/physiology/pinocytosis.html
    sha256: 05cdd69bb7af7279c0b61c2e853b4bad5c2687094118d71d4ad3a11f549f1415
    role: context
  - path: pages/traits/physiology/positive_autotropism.html
    sha256: cc0716c9bbbddd57139bc7076ea4e6ca29f56297acf1a1b7e626c31d7484927b
    role: context
  - path: pages/traits/physiology/primary_homothallism.html
    sha256: b2a63e611eff133430247e50be63219f251872afe0443f3dbb5259e0beb5e7af
    role: context
  - path: pages/traits/physiology/prolyl_aminopeptidase_activity.html
    sha256: 4122861eacb5be5dbe4a8865e9c1b2a9cef6e05242becf322b2ee767324122c8
    role: context
  - path: pages/traits/physiology/proteaphagy.html
    sha256: 8393f465908e6635a03897b1430e5fbd02acebf6b13b2bc2f76f3905b2a67a03
    role: context
  - path: pages/traits/physiology/pseudobipolar_mating_system.html
    sha256: 1b0c842493c5928bbfcd520c50fcab9602bce57fe6176b8be6d25ecb0e637f99
    role: context
  - path: pages/traits/physiology/pseudohomothallism.html
    sha256: 45347d64a626a9d8e29fcd0de51e76776cf48de01592c2507279061a6b9390e9
    role: context
  - path: pages/traits/physiology/pyrazinamidase_activity.html
    sha256: b84806ea0bdef9669932c198fb6506fa4ac680dc92a24bbf0f63b81506a442ef
    role: context
  - path: pages/traits/physiology/pyrrolidonyl_arylamidase_activity.html
    sha256: 73a202d214dca01925e79c17e2ef44f3bb5e233cbf4fb81730a75850306c5e6d
    role: context
  - path: pages/traits/physiology/quorum_quenching.html
    sha256: 00bfb33b3f66fde5aa94dd5ae3ef939758ac46fdb57d0fb1daa92e548a4386d4
    role: context
  - path: pages/traits/physiology/quorum_sensing.html
    sha256: 55a6899a3f15fe6d49cf96aa76f58e7a0c6e19f1b93435c544d1a1b1295bdc6e
    role: context
  - path: pages/traits/physiology/rapid_axopodial_contraction.html
    sha256: 50da1629e023cf20c0a59eaf56fe23f72d0313de3449e73f3a6837d0becf573b
    role: context
  - path: pages/traits/physiology/replicative_aging.html
    sha256: be1642e8130c6a2a1cbd06d28c70f73f06fb24441fc04867b9c8248466201d19
    role: context
  - path: pages/traits/physiology/rheotaxis.html
    sha256: 8999ee990c57109f8f7b63fd2467b000ce6c85f758d1f43fb83e9f26c3b1ae6d
    role: context
  - path: pages/traits/physiology/rheotropism.html
    sha256: 409ecc4c65b6dc1837afd05b4b9257378ad09d0b6d4bed7e81ce64e8311f7bd7
    role: context
  - path: pages/traits/physiology/ribophagy.html
    sha256: abb9b213391888fb60e33047ca29be0a98cc1ab0b09e2cc4d9b5b842850a7b88
    role: context
  - path: pages/traits/physiology/serine_arylamidase_activity.html
    sha256: e63f865b994e0996fce4a3a80316cd92f87cf19165fea2b197d1f83054ced7b0
    role: context
  - path: pages/traits/physiology/siderophore_production.html
    sha256: 13f6c6ceeb069a469583fca1e7959fddb94af0d8d3e3855a98a7f7fa18a974d8
    role: context
  - path: pages/traits/physiology/siliceous_scale_production.html
    sha256: 72aa0263682245f0aa794a82c6c35a0569a65e1e40756d8c54d4309f9a0f9468
    role: context
  - path: pages/traits/physiology/sos_response.html
    sha256: a8dcee814bb2e7a6595d9d2bc0431ffc9c228d5e42608673793ff96fa314ec33
    role: context
  - path: pages/traits/physiology/spore_germination.html
    sha256: 2b1ab8b1b6916aa9a86e9355cbbeec29d1b3b9f6cd7942709ff668ec051949bc
    role: context
  - path: pages/traits/physiology/stress_response.html
    sha256: 68613e2bfb2efc2df48d86cd2228055960ff92035569d74598a99d252a6fd348
    role: context
  - path: pages/traits/physiology/tetrapolar_mating_system.html
    sha256: 82fc14c4c878fe5d9d9591b045fa20811b55aca734d5cca99500ef49ddbd70c7
    role: context
  - path: pages/traits/physiology/thermotaxis.html
    sha256: 109941ac501d8fe76eda1803a930655cc933110e8b119367de360fb08d65ac4a
    role: context
  - path: pages/traits/physiology/thigmotropism.html
    sha256: 8fafc61f606c25c1ab7841f569ab025f1ab740c3c84ca985aec9531454c416b5
    role: context
  - path: pages/traits/physiology/toxicyst_discharge.html
    sha256: 4851c560a259bc54b2d1f777488960bb3a704d717e3526fbe57ee46f1be888cf
    role: context
  - path: pages/traits/physiology/trichocyst_discharge.html
    sha256: e2bad91ddcd641ab7f7d4ad3533f9d6076303ce6f8ad85405ee8bf5bdb850efa
    role: context
  - path: pages/traits/physiology/tripolar_mating_system.html
    sha256: 1de4c891bfb791545f8d499231d68414c3eb53b848edaea155463a6250348f7d
    role: context
  - path: pages/traits/physiology/trogocytosis.html
    sha256: dfce8aab7504901a9f7a55936cecf5c0f33dcf5ca098b807feffad7eff50f41c
    role: context
  - path: pages/traits/physiology/trophic_type.html
    sha256: 8305c8c681967560a835d3260f8a287e14358eb810570112e5b71c60e3d10708
    role: context
  - path: pages/traits/physiology/trypsin_activity.html
    sha256: 91b7aec9ed6221f82bdb3c0b63a7aa07622a619c693ae7b337d8a1262b6460f0
    role: context
  - path: pages/traits/physiology/tyrosine_arylamidase_activity.html
    sha256: ff868db3d1435d29947a6e827f923ca5fce02e2d48f6032b81d21cc34ab5114f
    role: context
  - path: pages/traits/physiology/unconventional_protein_secretion.html
    sha256: 262296028c4fee5329c4140f8df51ffed4e22f1df161ad9f2c5c9d6e1921d405
    role: context
  - path: pages/traits/physiology/unisexual_reproduction.html
    sha256: 1d870d5e14330d089ffc36e4ec62da00b6e0883deea21f6fb87b1e9b60a93bbf
    role: context
  - path: pages/traits/physiology/urease_activity.html
    sha256: 1a5c1f28cf2eba187f94de2a7cd14f5d5f3afced587c6d7a273c197e75037fd6
    role: context
  - path: pages/traits/physiology/valine_arylamidase_activity.html
    sha256: 8c3ddc85d8632794996a5ffa79fcaa38ee7d9f7a4bc2934f142b9d363722a902
    role: context
  - path: pages/traits/physiology/viable_but_nonculturable_state.html
    sha256: de13a2dd478b880264c16dbafa6d88427418a2dd3d219cbb8a42debd2de7f738
    role: context
  - path: pages/traits/physiology/viscotaxis.html
    sha256: 2e950f0a3bb57b005b7fcfbad2ba0a510d7e22cec3cd0a68215fe40eba3c1034
    role: context
  - path: pages/traits/quantitative_property/has_maximum_observed_value.html
    sha256: 9357b4caf46d1ea0ffe75ad72d2593e875a573139421c1fbebfed7ffd0f453fe
    role: context
  - path: pages/traits/quantitative_property/has_minimum_observed_value.html
    sha256: 0b9bab31627fa4d2ba4cdcb11c3dffe6815d5c26d3fb21d9018be0d9e86df139
    role: context
  - path: pages/traits/quantitative_property/has_observed_spot_value.html
    sha256: 7671624cbf6ff968ebcaecc52680511b80dfbca6c3cc1809a3c3c61343b4380d
    role: context
  - path: pages/traits/quantitative_property/has_value.html
    sha256: a6125479c57d0a65441e22c34809e0a23de2048370b89dd7b26a66f5a39e85b9
    role: context
  - path: pages/traits/quantitative_property/has_value_comments.html
    sha256: ca6ace6ea64e09571262bc33c715bb51a726db7e1d8bca39eddf4c5b1245f226
    role: context
  - path: pages/traits/quantitative_property/is_negative_data.html
    sha256: 7bf44763ac633834bdd5a2384aeb59144a03739d8730d70e2b906bb932eb375e
    role: context
  - path: pages/traits/quantitative_property/observation_data_property.html
    sha256: 5874e6b1a6996a922834050fd3d538d8be54240754e51d945a5387502b1b392b
    role: context
  - path: pages/traits/upper/biological_process.html
    sha256: 2f675f487b3e6f805409c7e7a9343b3dd3c4fef17b0995c73f3b97ea7d4b2a5b
    role: context
  - path: pages/traits/upper/chemical_entity.html
    sha256: 0f3799b7eceb25d7e43dec1e135d5d6c0f71017da342114c2ff69f3487d198df
    role: context
  - path: pages/traits/upper/enzyme.html
    sha256: 8ed0a94c9b83c459888053504accf6d521e6db9226a1ac61fd73e920cda6b63d
    role: context
  - path: pages/traits/upper/material_entity.html
    sha256: e441486bdc9ee5f3d0d4e1ff9b48865af055a96fe4a252eb266a2d8dea12e657
    role: context
  - path: pages/traits/upper/microbe.html
    sha256: 29acd7bb56e2a1d7c3f57c4f9f5595d0b0a4a7e365483ff55363c11e1b1af9bc
    role: context
  - path: pages/traits/upper/observation.html
    sha256: 45a3a45e66891ed24c44d6e0c4e07bbd41c672916e56547719b27f2ac6f9cdae
    role: context
  - path: pages/traits/upper/phenotype.html
    sha256: b41b48cb896b04c6b5ac43557de043348edcd249154e45e221c84cfd90c5fe1e
    role: context
  - path: pages/traits/upper/quality.html
    sha256: 8447a27bb8e8879bcfd0d8f81cc5795e7326cf57544cdd68c6659caf07236556
    role: context
  - path: pages/umap.html
    sha256: c7c4220699618e34758479d0b3d450e4e3627242c9a28757da5841628e23e1fe
    role: context
  - path: proposals/metpo_traitmech_v585/metpo_proposal_classes_robot.tsv
    sha256: 2bb77eb078ff1a538f2b83f86180015885e24374c16245af503dc3c72c3d5933
    role: context
  - path: proposals/metpo_traitmech_v585/proposal.md
    sha256: fb6e2f007255a138ab1a820ab79f14fd099aca4f0059ce97c999aa36c10e3796
    role: context
  - path: reports/metpo_2026_06_12_active_review.tsv
    sha256: 45e9c6471475635ba1f2602cd636a119d490f5dbd8dd6ac8af1aab89a321379f
    role: context
  - path: reports/metpo_2026_06_12_release_delta.tsv
    sha256: afe858d2aa0ade08322c7808d5917ff370e069ba02c2642d483342db8e9323ac
    role: context
  - path: reports/proposal_citation_audit.tsv
    sha256: 5cc34df4b60b02f901a87b982478f073debc7146316b6731380f80cef9e177a0
    role: context
  - path: reports/robot/metpo_traitmech_v585/classes.owl
    sha256: a5830165be11aaf04fd36fc8ec2a189e1bfde2a5e82645151eb91d961b20c11f
    role: context
  - path: reports/robot/metpo_traitmech_v585/merged.owl
    sha256: 657996017ccac0a1d290d80e92a4605f4a9d8c50390104c3f585d819327c7898
    role: context
  - path: reports/robot/metpo_traitmech_v585/reasoned.owl
    sha256: 1de5502ebabd3d326622745dade6df8cd402d7d2c8d0d56a7133e785838b2af2
    role: context
  - path: research/traits/physiology/replicative_aging-source-verification.json
    sha256: c350362e884bfac1b8172d861d0b3b61cb0108639d77546f57198ac44e6516f7
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
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/.vendored_canon_ref
    sha256: 698af47e96e93fe96e81910bb140593a79c2b92c4688892edeab9b63244ec5bf
    role: context
  - path: scripts/add_replicative_aging_trait.py
    sha256: 9e1f9095ed68aa2d12c799334a8c5c6f7d6758de8b0d78bd85d64ffd7743b743
    role: context
  - path: scripts/audit_canonical_examples.py
    sha256: 367b9a1759b81e545b06c8dc0c22419ae8d478e3fcd8de6d0bc0cacbb9eacf54
    role: context
  - path: scripts/qualify_replicative_aging_label.py
    sha256: f3b44728454be4ba21038991726a964855954052bbfb0486383664a1e9a4be44
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
  - path: tests/test_add_replicative_aging_trait.py
    sha256: 1e055331b30d15b6f50f99df9c5ed1706983e5a24f1429204dce9a257ae59a29
    role: context
  - path: tests/test_qualify_replicative_aging_label.py
    sha256: a64534e83906f9790fdc8a5fb285c1e7870efecc441428df31b689ee4cd87f52
    role: context
targets:
- target_id: traitmech:000709
  path: data/traits/physiology/replicative_aging.yaml
  label: replicative aging with functional decline
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: scripts/qualify_replicative_aging_label.py
    role: guarded label correction writer
  - repository: CultureBotAI/TraitMech
    path: scripts/add_replicative_aging_trait.py
    role: guarded curation writer
  - repository: CultureBotAI/TraitMech
    path: data/traits/physiology/replicative_aging.yaml
    role: maintained trait record
  - repository: CultureBotAI/TraitMech
    path: proposals/metpo_traitmech_v585/metpo_proposal_classes_robot.tsv
    role: companion METPO proposal
scope:
  description: Complete corrected record, maintained writers/tests, proposal, history,
    related skill/README changes and derived artifacts.
  selection: One exact new trait; no sampling.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - traitmech:000709
  exclusions:
  - target: Other 1103 TraitRecords
    reason: Novelty/preservation and deterministic checks only, not scientific reassessment.
  - target: data/traits/physiology/spore_germination.yaml
    reason: Protected and byte-preserved.
checks:
- check_id: records-0
  name: .venv/bin/linkml-validate -s src/traitmech/schema/traitmech.yaml --target-class
    TraitRecord data/traits/physiology/replicative_aging.yaml
  command: .venv/bin/linkml-validate -s src/traitmech/schema/traitmech.yaml --target-class
    TraitRecord data/traits/physiology/replicative_aging.yaml
  status: passed
  required: true
  target_ids:
  - traitmech:000709
  exit_code: 0
  expected_exit_code: 0
  summary: Actual native check passed on corrected content; corpus validation is not
    whole-corpus scientific review.
- check_id: records-1
  name: .venv/bin/python scripts/validate_strict.py data/traits/physiology/replicative_aging.yaml
  command: .venv/bin/python scripts/validate_strict.py data/traits/physiology/replicative_aging.yaml
  status: passed
  required: true
  target_ids:
  - traitmech:000709
  exit_code: 0
  expected_exit_code: 0
  summary: Actual native check passed on corrected content; corpus validation is not
    whole-corpus scientific review.
- check_id: records-2
  name: .venv/bin/python scripts/verify_snippets.py --record data/traits/physiology/replicative_aging.yaml
    --out /tmp/traitmech-aging-final-checks-20261012/snippet-results.tsv
  command: .venv/bin/python scripts/verify_snippets.py --record data/traits/physiology/replicative_aging.yaml
    --out /tmp/traitmech-aging-final-checks-20261012/snippet-results.tsv
  status: passed
  required: true
  target_ids:
  - traitmech:000709
  exit_code: 0
  expected_exit_code: 0
  summary: Two VERIFIED scientific-abstract snippets and two NOT_IN_ABSTRACT full-text
    snippets. Direct XML section checks support all four; full-text matches were not
    relabeled as abstract matches.
- check_id: writer-0
  name: .venv/bin/python -m pytest -q tests/test_add_replicative_aging_trait.py tests/test_qualify_replicative_aging_label.py
  command: .venv/bin/python -m pytest -q tests/test_add_replicative_aging_trait.py
    tests/test_qualify_replicative_aging_label.py
  status: passed
  required: true
  target_ids:
  - traitmech:000709
  exit_code: 0
  expected_exit_code: 0
  summary: '31 focused writer tests passed: dry-run default, exact preimage refusal,
    prevalidation, no partial writes on rejected inputs, copy isolation and idempotent
    replay.'
- check_id: generate-0
  name: just audit-proposals
  command: just audit-proposals
  status: passed
  required: true
  target_ids:
  - traitmech:000709
  exit_code: 0
  expected_exit_code: 0
  summary: Actual native check passed on corrected content; corpus validation is not
    whole-corpus scientific review.
- check_id: generate-1
  name: just ground-predicates
  command: just ground-predicates
  status: passed
  required: true
  target_ids:
  - traitmech:000709
  exit_code: 0
  expected_exit_code: 0
  summary: Actual native check passed on corrected content; corpus validation is not
    whole-corpus scientific review.
- check_id: generate-2
  name: just ground-nodes
  command: just ground-nodes
  status: passed
  required: true
  target_ids:
  - traitmech:000709
  exit_code: 0
  expected_exit_code: 0
  summary: Actual native check passed on corrected content; corpus validation is not
    whole-corpus scientific review.
- check_id: generate-3
  name: just audit-graphs
  command: just audit-graphs
  status: passed
  required: true
  target_ids:
  - traitmech:000709
  exit_code: 0
  expected_exit_code: 0
  summary: Actual native check passed on corrected content; corpus validation is not
    whole-corpus scientific review.
- check_id: generate-4
  name: just audit-graph-protein-taxa
  command: just audit-graph-protein-taxa
  status: passed
  required: true
  target_ids:
  - traitmech:000709
  exit_code: 0
  expected_exit_code: 0
  summary: Actual native check passed on corrected content; corpus validation is not
    whole-corpus scientific review.
- check_id: generate-5
  name: just audit-predicate-domains
  command: just audit-predicate-domains
  status: passed
  required: true
  target_ids:
  - traitmech:000709
  exit_code: 0
  expected_exit_code: 0
  summary: Actual native check passed on corrected content; corpus validation is not
    whole-corpus scientific review.
- check_id: generate-6
  name: just check-biolink-coverage
  command: just check-biolink-coverage
  status: passed
  required: true
  target_ids:
  - traitmech:000709
  exit_code: 0
  expected_exit_code: 0
  summary: Actual native check passed on corrected content; corpus validation is not
    whole-corpus scientific review.
- check_id: generate-7
  name: just audit-snippets
  command: just audit-snippets
  status: passed
  required: true
  target_ids:
  - traitmech:000709
  exit_code: 0
  expected_exit_code: 0
  summary: Actual native check passed on corrected content; corpus validation is not
    whole-corpus scientific review.
- check_id: generate-8
  name: just gen-discussions-data
  command: just gen-discussions-data
  status: passed
  required: true
  target_ids:
  - traitmech:000709
  exit_code: 0
  expected_exit_code: 0
  summary: Actual native check passed on corrected content; corpus validation is not
    whole-corpus scientific review.
- check_id: generate-9
  name: just gen-qc-dashboard
  command: just gen-qc-dashboard
  status: passed
  required: true
  target_ids:
  - traitmech:000709
  exit_code: 0
  expected_exit_code: 0
  summary: Actual native check passed on corrected content; corpus validation is not
    whole-corpus scientific review.
- check_id: generate-10
  name: just gen-pages
  command: just gen-pages
  status: passed
  required: true
  target_ids:
  - traitmech:000709
  exit_code: 0
  expected_exit_code: 0
  summary: Actual native check passed on corrected content; corpus validation is not
    whole-corpus scientific review.
- check_id: generate-11
  name: just gen-priority-dashboard
  command: just gen-priority-dashboard
  status: passed
  required: true
  target_ids:
  - traitmech:000709
  exit_code: 0
  expected_exit_code: 0
  summary: Actual native check passed on corrected content; corpus validation is not
    whole-corpus scientific review.
- check_id: verify-0
  name: just qc
  command: just qc
  status: passed
  required: true
  target_ids:
  - traitmech:000709
  exit_code: 0
  expected_exit_code: 0
  summary: Actual native check passed on corrected content; corpus validation is not
    whole-corpus scientific review.
- check_id: verify-1
  name: just validate-history
  command: just validate-history
  status: passed
  required: true
  target_ids:
  - traitmech:000709
  exit_code: 0
  expected_exit_code: 0
  summary: Actual native check passed on corrected content; corpus validation is not
    whole-corpus scientific review.
- check_id: verify-2
  name: just validate-products
  command: just validate-products
  status: passed
  required: true
  target_ids:
  - traitmech:000709
  exit_code: 0
  expected_exit_code: 0
  summary: Actual native check passed on corrected content; corpus validation is not
    whole-corpus scientific review.
- check_id: verify-3
  name: just verify-proposal metpo_traitmech_v585
  command: just verify-proposal metpo_traitmech_v585
  status: passed
  required: true
  target_ids:
  - traitmech:000709
  exit_code: 0
  expected_exit_code: 0
  summary: Actual native check passed on corrected content; corpus validation is not
    whole-corpus scientific review.
- check_id: verify-4
  name: just robot-validate-proposal metpo_traitmech_v585
  command: just robot-validate-proposal metpo_traitmech_v585
  status: passed
  required: true
  target_ids:
  - traitmech:000709
  exit_code: 0
  expected_exit_code: 0
  summary: Actual native check passed on corrected content; corpus validation is not
    whole-corpus scientific review.
- check_id: verify-5
  name: .venv/bin/ruff check src scripts tests
  command: .venv/bin/ruff check src scripts tests
  status: passed
  required: true
  target_ids:
  - traitmech:000709
  exit_code: 0
  expected_exit_code: 0
  summary: Actual native check passed on corrected content; corpus validation is not
    whole-corpus scientific review.
- check_id: tests-0
  name: .venv/bin/python -m pytest -q --junitxml=/tmp/traitmech-aging-stable-tests-20261012/pytest.xml
  command: .venv/bin/python -m pytest -q --junitxml=/tmp/traitmech-aging-stable-tests-20261012/pytest.xml
  status: passed
  required: true
  target_ids:
  - traitmech:000709
  exit_code: 0
  expected_exit_code: 0
  summary: 4212 tests passed with no failures, errors or skips in the stable-tree
    rerun. Earlier overlapping-generation run had one stale discussions-data failure;
    its receipt is retained, not counted as a pass.
- check_id: supplemental-0
  name: .venv/bin/python scripts/validate_history_links.py history/records/replicative_aging
  command: .venv/bin/python scripts/validate_history_links.py history/records/replicative_aging
  status: passed
  required: true
  target_ids:
  - traitmech:000709
  exit_code: 0
  expected_exit_code: 0
  summary: Actual native check passed on corrected content; corpus validation is not
    whole-corpus scientific review.
- check_id: supplemental-1
  name: .venv/bin/linkml-validate --schema src/traitmech/schema/history.yaml --target-class
    HistoryRecord history/records/replicative_aging/2026-10-12T101846Z-codex-957baa.yaml
  command: .venv/bin/linkml-validate --schema src/traitmech/schema/history.yaml --target-class
    HistoryRecord history/records/replicative_aging/2026-10-12T101846Z-codex-957baa.yaml
  status: passed
  required: true
  target_ids:
  - traitmech:000709
  exit_code: 0
  expected_exit_code: 0
  summary: Actual native check passed on corrected content; corpus validation is not
    whole-corpus scientific review.
- check_id: supplemental-2
  name: .venv/bin/linkml-validate --schema src/traitmech/schema/history.yaml --target-class
    HistoryRecord history/records/replicative_aging/2026-10-12T103127Z-codex-884508.yaml
  command: .venv/bin/linkml-validate --schema src/traitmech/schema/history.yaml --target-class
    HistoryRecord history/records/replicative_aging/2026-10-12T103127Z-codex-884508.yaml
  status: passed
  required: true
  target_ids:
  - traitmech:000709
  exit_code: 0
  expected_exit_code: 0
  summary: Actual native check passed on corrected content; corpus validation is not
    whole-corpus scientific review.
- check_id: supplemental-3
  name: .venv/bin/python scripts/audit_canonical_examples.py --no-resolve
  command: .venv/bin/python scripts/audit_canonical_examples.py --no-resolve
  status: passed
  required: true
  target_ids:
  - traitmech:000709
  exit_code: 0
  expected_exit_code: 0
  summary: Actual native check passed on corrected content; corpus validation is not
    whole-corpus scientific review.
- check_id: supplemental-4
  name: .venv/bin/python scripts/run_trait_graph_audit.py --verify
  command: .venv/bin/python scripts/run_trait_graph_audit.py --verify
  status: passed
  required: true
  target_ids:
  - traitmech:000709
  exit_code: 0
  expected_exit_code: 0
  summary: Actual native check passed on corrected content; corpus validation is not
    whole-corpus scientific review.
- check_id: supplemental-5
  name: .venv/bin/python scripts/audit_history_records.py --base 53188095ebb645d2e21bf2d5dbe6548046190279
  command: .venv/bin/python scripts/audit_history_records.py --base 53188095ebb645d2e21bf2d5dbe6548046190279
  status: passed
  required: true
  target_ids:
  - traitmech:000709
  exit_code: 0
  expected_exit_code: 0
  summary: Actual native check passed on corrected content; corpus validation is not
    whole-corpus scientific review.
- check_id: supplemental-6
  name: git diff --check 53188095ebb645d2e21bf2d5dbe6548046190279 HEAD -- . ':(exclude)proposals/metpo_traitmech_v585/metpo_proposal_classes_robot.tsv'
  command: git diff --check 53188095ebb645d2e21bf2d5dbe6548046190279 HEAD -- . ':(exclude)proposals/metpo_traitmech_v585/metpo_proposal_classes_robot.tsv'
  status: passed
  required: true
  target_ids:
  - traitmech:000709
  exit_code: 0
  expected_exit_code: 0
  summary: Actual native check passed on corrected content; corpus validation is not
    whole-corpus scientific review.
- check_id: supplemental-7
  name: git -c core.whitespace=-blank-at-eol diff --check 53188095ebb645d2e21bf2d5dbe6548046190279
    HEAD -- proposals/metpo_traitmech_v585/metpo_proposal_classes_robot.tsv
  command: git -c core.whitespace=-blank-at-eol diff --check 53188095ebb645d2e21bf2d5dbe6548046190279
    HEAD -- proposals/metpo_traitmech_v585/metpo_proposal_classes_robot.tsv
  status: passed
  required: true
  target_ids:
  - traitmech:000709
  exit_code: 0
  expected_exit_code: 0
  summary: Actual native check passed on corrected content; corpus validation is not
    whole-corpus scientific review.
- check_id: superseded-tests
  name: Superseded full suite overlapping regeneration
  command: .venv/bin/python -m pytest -q --junitxml=/tmp/traitmech-aging-final-checks-20261012/pytest.xml
  status: failed
  required: false
  target_ids:
  - traitmech:000709
  exit_code: 1
  expected_exit_code: 0
  summary: Historical run:4211 passed and one discussions searchData freshness failure
    while generation was unfinished. Preserved as a failed execution, superseded by
    the required stable-tree rerun; not counted as a passing acceptance check.
- check_id: freshness-recheck
  name: Isolated discussions freshness recheck
  command: env UV_NO_SYNC=1 PYTHONPATH=src .venv/bin/python -m pytest -q tests/test_audit_discussions_data.py::test_repository_artifact_is_current
  status: passed
  required: true
  target_ids:
  - traitmech:000709
  exit_code: 0
  expected_exit_code: 0
  summary: The previously failing test passed on the generated and committed tree
    before the full stable rerun.
- check_id: browser
  name: Desktop/mobile generated-page inspection
  command: node /tmp/traitmech-aging-browser-20261012.cjs
  status: passed
  required: true
  target_ids:
  - traitmech:000709
  exit_code: 0
  expected_exit_code: 0
  summary: '1440/390 px assertions and eight visually inspected screenshots: qualified
    label, local identifier provenance, four quotes, two discussions, two history
    links, hierarchy/browse navigation and dashboard image/counts, no horizontal overflow
    or JavaScript errors.'
- check_id: embeddings
  name: Embedding applicability
  status: not_applicable
  required: false
  target_ids:
  - traitmech:000709
  summary: Neither exact configured source exists in primary or owned layouts. Existing
    embedding artifacts retained, not regenerated.
evidence:
- evidence_id: bacterial
  kind: primary_source
  reference: DOI:10.1098/rstb.2018.0442
  locator: 'Primary JATS XML: Introduction, Methods, Results(a,b), selected Discussion;
    Figure 2 caption and actual author-PDF figure.'
  accessed_at: '2026-10-12T11:01:06Z'
  support: supports
  summary: Age-indexed division-time increase supports a decline phenotype, with later
    plateau and initial-condition limitations. Brightfield measurements are distinct
    from fluorescent assays. Methods BW25113 versus Introduction BW21113 remains unresolved,
    not assigned a canonical taxon.
  snapshot_sha256: 31bf56ae9f3d4035f97ad975bf18078a26b960a5606c3a91a417f238a08c20eb
- evidence_id: caulobacter
  kind: primary_source
  reference: DOI:10.1186/1471-2148-7-126
  locator: Scientific abstract Background; directly retrieved primary XML and publisher
    Background, Results, Discussion, Methods and captions.
  accessed_at: '2026-10-12T11:01:06Z'
  support: supports
  summary: Declining reproductive function supports bacterial aging. The cohort endpoint
    combines survival/reproduction, evolved clones differ in aging direction, and
    pilA-deletion UJ590 is not an unmodified natural exemplar. Elapsed-time assay
    complements division-indexed evidence.
  snapshot_sha256: 7d6e7d54ea9c0aa558d892e7a9690ab18c0a3b5ad1e531d195f1054bfc19eff6
- evidence_id: fission-boundary
  kind: primary_source
  reference: DOI:10.7554/eLife.20340
  locator: Scientific abstract, not eLife digest, and Discussion in directly retrieved
    primary XML; source-qualified MED PMID28139976.
  accessed_at: '2026-10-12T11:01:06Z'
  support: supports
  summary: Finite replicative lifespan and lifespan extension without classic deterioration
    are boundary evidence, not a positive exemplar. Constant hazard is not increasing
    mortality risk, and cumulative survival loss alone is insufficient.
  snapshot_sha256: 2e75310f8805c186d9755697731b1f07ce848195f5c35bb8e996436c8d72b32c
- evidence_id: yeast-boundary
  kind: primary_source
  reference: DOI:10.1371/journal.pbio.3002245
  locator: Scientific Abstract, first Results section, Discussion, strain Methods
    and captions; directly reopened PLOS and primary XML.
  accessed_at: '2026-10-12T11:01:06Z'
  support: supports
  summary: Diet-dependent maintenance of performance without longer lifespan separates
    functional decline from lifespan. Engineered MEP system and broader healthy-ageing
    terminology are explicit. Qualifying the label avoids equating the narrower operational
    phenotype with every use of replicative aging.
  snapshot_sha256: 9a5d4eb9234be837681761e43e2295246872425bf1138195e8372b1c7e54fc5f
- evidence_id: snippets
  kind: validation
  reference: research/traits/physiology/replicative_aging-source-verification.json
  locator: Exact DOI/source-qualified MED/Crossref identity checks, hashed JATS bytes,
    exact XPath/snippet checks; native final resolver TSV.
  accessed_at: '2026-10-12T11:01:06Z'
  support: supports
  summary: Four exact contiguous snippets of 11/12/21/22 words. Two are scientific
    abstracts, two are full-text caption/Results. Linked preprints, peer evaluations
    and sequence links are contextual metadata, not independent experiments. Notice
    checks are bounded, not exhaustive.
- evidence_id: content
  kind: record_content
  reference: data/traits/physiology/replicative_aging.yaml
  locator: Complete final YAML, two writers/tests, two append-only history entries,
    v585 proposal, skill update, README and rendered page.
  accessed_at: '2026-10-12T11:01:06Z'
  support: supports
  summary: One PHYSIOLOGY CLASS under phenotype; age-specific performance decline
    or increasing risk, not a lifespan field, sequence feature, culture age, old-pole
    identity or universal mechanism. No synonyms, xrefs, examples or causal graph
    asserted.
- evidence_id: novelty
  kind: search
  reference: proposals/metpo_traitmech_v585/proposal.md
  locator: Full surviving roots with ignored/hidden files; corrected historical PCRE
    searches with known-positive control; seed/release/RDF/upstream/pending-PR reconciliation
    and fresh reservation refresh.
  accessed_at: '2026-10-12T11:01:06Z'
  support: supports
  summary: No exact competing record or reserved ID/block in inspected scope. Reserve
    000709, v585 and 1066200-1066299, populate only 1066200. Culture-aging stationary-phase
    node and host senescence mentions are not exact. No global exhaustion claim.
  search_scope: 22 baseline registered TraitMech roots plus owned addition;18 lack
    Git metadata but surviving files and historical tracked trees inspected. Baseline1103
    records;399 seed IDs,344 overlap and55 absent leads; frozen1546/153-row inventories.127
    CommunityMech roots and surviving/historical proposals,644 METPO issue/PR bodies,654
    comments; complete paginated pending PR files including drafts and changed ontology/template
    blobs. Fresh open heads and proposal reservations unchanged. Ignored/hidden included;
    unavailable current ignored/untracked bytes cannot be reconstructed; normal binary
    handling, no archive unpacking, symlink-directory traversal or unregistered/private
    coverage.
- evidence_id: reservation
  kind: search
  reference: /tmp/traitmech-aging-publication-20261012/result.json
  locator: Fresh full-block scan across current registered roots and registered historical
    trees, paginated pending files, immutable upstream bytes.
  accessed_at: '2026-10-12T11:01:06Z'
  support: supports
  summary: Refresh at 2026-10-12T10:38:01.349308+00:00 finds no competing reservation.
    Candidate-owned hits are explicitly distinguished; no external worktree was changed.
  snapshot_sha256: e849b7faa0c446cd58633209b4e2ad7d0a2cec9dcec7a4c7c930b889d10e18a0
  search_scope: All 23 registered TraitMech roots, surviving current files with ignored
    and hidden files included, and available registered historical tracked trees;
    all 127 CommunityMech registrations and their proposal bytes; unchanged open and
    draft PR heads with full paginated changed-file lists and complete inspected upstream
    ontology and template blobs. The full 1066200-1066299 block, cohort and local
    ID were checked. Own-branch hits are expected, not competing reservations. Unavailable
    current ignored or untracked bytes, archives, symlink directories and unregistered
    or private work are outside the conclusion.
- evidence_id: resolution
  kind: record_content
  reference: https://github.com/CultureBotAI/TraitMech/issues/1891
  locator: qualify_replicative_aging_label.py, regression tests, label and discussion,
    v585 label/narrative, add-trait skill and appended event/history.
  accessed_at: '2026-10-12T11:01:06Z'
  support: supports
  summary: Label now explicitly says replicative aging with functional decline. Definition,
    evidence, identifier and original provenance are preserved; bare aging is not
    an exact synonym. Remaining upstream terminology is a disclosed curation question.
- evidence_id: products
  kind: validation
  reference: reports/proposal_citation_audit.tsv
  locator: Final native gates, full/focused tests, parsed RDF, byte-preservation receipts,
    browser assertions and screenshots.
  accessed_at: '2026-10-12T11:01:06Z'
  support: supports
  summary: '1104 records; all 1103 prior YAMLs and prior history/reviews/proposals/embeddings/templates
    preserved.1102 old pages are footer-only; phenotype gains one child. RDF cardinalities
    {''classes'': 15, ''merged'': 12628, ''reasoned'': 12632}, w3id parent hierarchy
    and qualified label agree. No baseline weakened; required TSV directive tabs receive
    only an exact-path whitespace exception.'
- evidence_id: prior
  kind: prior_review
  reference: reviews/structured/20261012T102912Z-aging-label-scope/review.yaml
  locator: Initial partial self-review at c53a5fb357b620dc9cbc73aa3403ffacd108898f;
    finding label-qualifier.
  accessed_at: '2026-10-12T11:01:06Z'
  support: context_only
  summary: Original open finding remains immutable; this successor reassesses the
    correction and records explicit resolution lineage.
assessments:
- assessment_id: identity
  area: identity
  topic: Decline-qualified cellular phenotype
  summary: Operational age-associated decline is supported, explicitly qualified,
    and not equated with finite lifespan or culture age.
  target_ids:
  - traitmech:000709
  evidence_ids:
  - bacterial
  - caulobacter
  - fission-boundary
  - yeast-boundary
  - content
  outcome: supported
- assessment_id: scope
  area: scope
  topic: Terminology and conditions
  summary: Broader healthy-aging usage, age axis, plateau, engineered strains and
    measurement limitations remain explicit.
  target_ids:
  - traitmech:000709
  evidence_ids:
  - bacterial
  - caulobacter
  - fission-boundary
  - yeast-boundary
  - resolution
  outcome: supported
- assessment_id: hierarchy
  area: grounding
  topic: Phenotype parent and absent equivalence claims
  summary: Active w3id phenotype-to-quality hierarchy is broader; no shifted xrefs
    or forced sibling/node grounding added.
  target_ids:
  - traitmech:000709
  evidence_ids:
  - content
  - novelty
  - products
  outcome: supported
- assessment_id: evidence
  area: evidence
  topic: Four primary citations and exact snippets
  summary: Positive bacterial evidence and boundary yeast evidence are distinguished;
    no metadata-only source or preprint counted as replication.
  target_ids:
  - traitmech:000709
  evidence_ids:
  - bacterial
  - caulobacter
  - fission-boundary
  - yeast-boundary
  - snippets
  outcome: supported
- assessment_id: novelty
  area: identity
  topic: Bounded novelty and full-block allocation
  summary: Ignored/hidden searches, controlled historical regex and fresh pending-reservation
    checks support one new inspected trait.
  target_ids:
  - traitmech:000709
  evidence_ids:
  - novelty
  - reservation
  outcome: supported
- assessment_id: provenance
  area: provenance
  topic: Guarded correction and immutable lineage
  summary: Issue1891 is resolved without rewriting initial history/review; human sign-off
    is not implied.
  target_ids:
  - traitmech:000709
  evidence_ids:
  - content
  - resolution
  - prior
  - products
  outcome: supported
- assessment_id: outputs
  area: consistency
  topic: Native gates and regenerated products
  summary: Qualified identity, counts, proposal RDF and navigation agree; prior records
    and protected file remain unchanged.
  target_ids:
  - traitmech:000709
  evidence_ids:
  - products
  - resolution
  outcome: supported
- assessment_id: gaps
  area: completeness
  topic: Unasserted mechanisms and natural exemplars
  summary: Canonical taxa, strain discrepancy and protein-resolved mechanisms remain
    deferred, not inferred from markers or lifespan.
  target_ids:
  - traitmech:000709
  evidence_ids:
  - content
  - bacterial
  - caulobacter
  - yeast-boundary
  outcome: unknown
findings:
- finding_id: label-qualifier
  issue_key: replicative-aging-functional-decline-label
  category: scope
  severity: minor
  status: resolved
  certainty: confirmed
  title: Unqualified aging label hides the functional-decline restriction
  description: The source also uses replicative aging for healthy age progression.
    The record admits that broader meaning but leaves the label and proposal unqualified,
    so label-only consumers cannot distinguish the narrower phenotype.
  target_ids:
  - traitmech:000709
  field_paths:
  - label
  - discussions[0]
  evidence_ids:
  - yeast-boundary
  - resolution
  - products
  - prior
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: scripts/qualify_replicative_aging_label.py
    role: guarded label correction writer
  - repository: CultureBotAI/TraitMech
    path: scripts/add_replicative_aging_trait.py
    role: guarded curation writer
  - repository: CultureBotAI/TraitMech
    path: data/traits/physiology/replicative_aging.yaml
    role: maintained trait record
  - repository: CultureBotAI/TraitMech
    path: proposals/metpo_traitmech_v585/metpo_proposal_classes_robot.tsv
    role: companion METPO proposal
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/1891
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261012T102912Z-aging-label-scope
    finding_id: label-qualifier
  disposition_reason: Record, proposal and rendered labels now expose the functional-decline
    qualifier. Guarded correction, tests and source-based reassessment pass with original
    provenance preserved.
actions: []
related_reviews:
- repository: CultureBotAI/TraitMech
  review_id: 20261012T102912Z-aging-label-scope
  relationship: Successor resolving the same minor label-scope finding.
limitations:
- Self-review, not independent or human sign-off; hashed corpus context is not whole-corpus
  scientific reassessment.
- Evidence access times include reinspection of directly retrieved snapshots, not
  necessarily fresh downloads. PLOS reopened directly; PMC2019 reopening returned
  CAPTCHA.
- Only 2019 Figure 2 visually assessed for primary-source graphics. Other figures,
  supplements and raw data not independently reanalysed; no molecular mechanism or
  natural canonical taxon asserted.
- Source-qualified MED/Crossref notice fields and available publisher pages bound
  the notice check; no exhaustive absence claim.
- Existing adapter-skipped product rows and source-license warnings are retained as
  limitations, not authority resolutions or newly fixed defects.
- Embedding sources unavailable; existing embeddings retained. Required ROBOT header
  tabs retain a narrow inspected whitespace exception.
- Historical tracked trees cannot reconstruct unavailable current ignored/untracked
  files. No archive, symlink-directory, unregistered/private search or global exhaustion
  claim.
- Native working_tree input capture attests inspected bytes at its recorded Git base;
  recovery of that base does not prove every ignored RDF input was committed.
- An earlier full suite overlapped artifact regeneration and reported one stale discussions-data
  failure. The failed 846-second run remains in /tmp/traitmech-aging-final-checks-20261012/tests.json;
  only the subsequent stable-tree rerun is the passing full-suite gate.
- External review requests, final CI and merge-queue checks follow publication and
  are not claimed complete here.
tags:
- add-trait
- replicative-aging
- self-review
- issue-1891
```
