# Full successor review of corrected functional cellular rejuvenation

- Review: 20261012T130746Z-rejuvenation-figure-resolution
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-12T12:55:27Z
- Finished UTC: 2026-10-12T13:07:46Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Full corrected-record self-review: one resolved minor finding (issue1893), zero open curation findings. Five primary-source evidence entries retain endpoint and access limits. Corrected native gates, browser checks and restored local/remote publication assessment pass. External PR review and queue remain subsequent gates.

## Scope And Provenance

Complete corrected trait, maintained owners, evidence, identity and proposal, history, directly related skill guidance, tests and generated changes.

Selection: Same exact affected trait as the predecessor; no sampling.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 1ee4d0ac5fb63a9d2c03c0aedea2e985d9422f8c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| traitmech:000710 | data/traits/physiology/cellular_rejuvenation.yaml | maintained | functional cellular rejuvenation |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| .venv/bin/linkml-validate -s src/traitmech/schema/traitmech.yaml --target-class TraitRecord data/traits/physiology/cellular_rejuvenation.yaml | passed | True | traitmech:000710 | Corrected-content native check passed; corpus checks do not constitute whole-corpus scientific review. |
| .venv/bin/python scripts/validate_strict.py data/traits/physiology/cellular_rejuvenation.yaml | passed | True | traitmech:000710 | Corrected-content native check passed; corpus checks do not constitute whole-corpus scientific review. |
| .venv/bin/python scripts/verify_snippets.py --record data/traits/physiology/cellular_rejuvenation.yaml --out /tmp/traitmech-rejuvenation-corrected-checks-20261012/snippet-results.tsv | passed | True | traitmech:000710 | Four VERIFIED abstract spans and one NOT_IN_ABSTRACT Results span. The latter remains directly verified in primary XML; no change to any quote or DOI. |
| .venv/bin/python -m pytest -q tests/test_add_cellular_rejuvenation_trait.py tests/test_correct_cellular_rejuvenation_figures.py | passed | True | traitmech:000710 | 30 focused tests passed, including exact correction preimages, preserved original event/source assessment, no writes on rejected input, idempotency and endpoint-specific attribution. |
| just audit-proposals | passed | True | traitmech:000710 | Corrected-content native check passed; corpus checks do not constitute whole-corpus scientific review. |
| just ground-predicates | passed | True | traitmech:000710 | Corrected-content native check passed; corpus checks do not constitute whole-corpus scientific review. |
| just ground-nodes | passed | True | traitmech:000710 | Corrected-content native check passed; corpus checks do not constitute whole-corpus scientific review. |
| just audit-graphs | passed | True | traitmech:000710 | Corrected-content native check passed; corpus checks do not constitute whole-corpus scientific review. |
| just audit-graph-protein-taxa | passed | True | traitmech:000710 | Corrected-content native check passed; corpus checks do not constitute whole-corpus scientific review. |
| just audit-predicate-domains | passed | True | traitmech:000710 | Corrected-content native check passed; corpus checks do not constitute whole-corpus scientific review. |
| just check-biolink-coverage | passed | True | traitmech:000710 | Corrected-content native check passed; corpus checks do not constitute whole-corpus scientific review. |
| just audit-snippets | passed | True | traitmech:000710 | Corrected-content native check passed; corpus checks do not constitute whole-corpus scientific review. |
| just gen-discussions-data | passed | True | traitmech:000710 | Corrected-content native check passed; corpus checks do not constitute whole-corpus scientific review. |
| just gen-qc-dashboard | passed | True | traitmech:000710 | Corrected-content native check passed; corpus checks do not constitute whole-corpus scientific review. |
| just gen-pages | passed | True | traitmech:000710 | Corrected-content native check passed; corpus checks do not constitute whole-corpus scientific review. |
| just gen-priority-dashboard | passed | True | traitmech:000710 | Corrected-content native check passed; corpus checks do not constitute whole-corpus scientific review. |
| just qc | passed | True | traitmech:000710 | Corrected-content native check passed; corpus checks do not constitute whole-corpus scientific review. |
| just validate-history | passed | True | traitmech:000710 | Corrected-content native check passed; corpus checks do not constitute whole-corpus scientific review. |
| just validate-products | passed | True | traitmech:000710 | Corrected-content native check passed; corpus checks do not constitute whole-corpus scientific review. |
| just verify-proposal metpo_traitmech_v586 | passed | True | traitmech:000710 | Corrected-content native check passed; corpus checks do not constitute whole-corpus scientific review. |
| just robot-validate-proposal metpo_traitmech_v586 | passed | True | traitmech:000710 | Corrected-content native check passed; corpus checks do not constitute whole-corpus scientific review. |
| .venv/bin/ruff check src scripts tests | passed | True | traitmech:000710 | Corrected-content native check passed; corpus checks do not constitute whole-corpus scientific review. |
| .venv/bin/python -m pytest -q --junitxml=/tmp/traitmech-rejuvenation-corrected-checks-20261012/pytest.xml | passed | True | traitmech:000710 | 4242 tests passed on the stable corrected checkpoint, after regeneration. |
| .venv/bin/python scripts/validate_history_links.py history/records/cellular_rejuvenation | passed | True | traitmech:000710 | Corrected-content native check passed; corpus checks do not constitute whole-corpus scientific review. |
| .venv/bin/linkml-validate --schema src/traitmech/schema/history.yaml --target-class HistoryRecord history/records/cellular_rejuvenation/2026-10-12T121656Z-codex-a49ab2.yaml | passed | True | traitmech:000710 | Corrected-content native check passed; corpus checks do not constitute whole-corpus scientific review. |
| .venv/bin/linkml-validate --schema src/traitmech/schema/history.yaml --target-class HistoryRecord history/records/cellular_rejuvenation/2026-10-12T124939Z-codex-e5fcad.yaml | passed | True | traitmech:000710 | Corrected-content native check passed; corpus checks do not constitute whole-corpus scientific review. |
| .venv/bin/python scripts/audit_canonical_examples.py --no-resolve | passed | True | traitmech:000710 | Corrected-content native check passed; corpus checks do not constitute whole-corpus scientific review. |
| .venv/bin/python scripts/run_trait_graph_audit.py --verify | passed | True | traitmech:000710 | Corrected-content native check passed; corpus checks do not constitute whole-corpus scientific review. |
| .venv/bin/python scripts/audit_history_records.py --base d5ade193d52ce90dfd8cd46adb6b28aa0871eb06 | passed | True | traitmech:000710 | Corrected-content native check passed; corpus checks do not constitute whole-corpus scientific review. |
| git diff --check d5ade193d52ce90dfd8cd46adb6b28aa0871eb06 HEAD -- . ':(exclude)proposals/metpo_traitmech_v586/metpo_proposal_classes_robot.tsv' | passed | True | traitmech:000710 | Corrected-content native check passed; corpus checks do not constitute whole-corpus scientific review. |
| git -c core.whitespace=-blank-at-eol diff --check d5ade193d52ce90dfd8cd46adb6b28aa0871eb06 HEAD -- proposals/metpo_traitmech_v586/metpo_proposal_classes_robot.tsv | passed | True | traitmech:000710 | Corrected-content native check passed; corpus checks do not constitute whole-corpus scientific review. |
| Desktop/mobile generated products | passed | True | traitmech:000710 | Desktop1440/mobile390 assertions and eight visually inspected corrected screenshots: Figure4 endpoint qualified, two history links, five snippets, two discussions, correct local identifier, working navigation/count/image, no overflow or page errors. |
| Embedding applicability | not_applicable | False | traitmech:000710 | Neither exact configured embedding source exists in the inspected primary/owned layouts. Existing artifacts retained, not regenerated. |
| Restored local and remote publication assessment | passed | True | traitmech:000710 | Fresh 23 registered TraitMech roots, 127 CommunityMech roots, historical tracked reservations, complete open/draft PR files and upstream heads checked. Original owned copy matches initial committed checkpoint; independent corrected publishing clone separately scanned, not falsely equated to registered HEAD. No conflicting reservation. |

## Scientific And Domain Assessments

### Functional cellular phenotype

identity: supported. Targets: traitmech:000710.

Same-cell performance recovery and descendant replicative-potential reset support a reusable endpoint-qualified trait.

### Recovery unit, endpoints and boundaries

scope: supported. Targets: traitmech:000710.

Recovery can be partial/transient; marker changes, mature-state reset, preserved function and generic dormancy exit alone are insufficient.

### Strictly broader active phenotype parent

grounding: supported. Targets: traitmech:000710.

No claim that autogamy, gametogenesis, aging or dormancy is an exact or narrower parent. Actual RDF uses the w3id phenotype-to-quality hierarchy.

### Primary-source identity and short verbatim spans

evidence: supported. Targets: traitmech:000710.

All evidence identities and source sections verified; positive and boundary roles distinguished with access and checksum limitations.

### Do not group unlike figure endpoints

evidence: supported. Targets: traitmech:000710.

Corrected note and explicit sidecar successor distinguish Figure1 gamete reset from Figure4 vegetative extension; abstract evidence is unchanged.

### Guarded writes, history and derived outputs

consistency: supported. Targets: traitmech:000710.

Tests and byte-preservation checks support the narrow change set; no source status promotion or forced molecular mechanism.

### Bounded novelty and restored current reservation state

identity: supported. Targets: traitmech:000710.

Initial identity searches included ignored and hidden files; fresh restored worktree and complete pending-PR assessments find no collision. Independent publishing copy is separately assessed as an owned correction of the preserved initial checkpoint.

### Mechanistic and taxonomic limits

completeness: unknown. Targets: traitmech:000710.

Natural exemplars, exact gene/protein identities and shared chemistry remain deferred; no evidence is invented to fill optional fields.

### Endpoint-specific figure attribution

evidence: supported. Targets: traitmech:000710.

Gamete reset and vegetative extension have separate, source-faithful locators; preserved abstract quote still supports gamete replicative-potential reset.

### Guarded correction with retained predecessor

provenance: supported. Targets: traitmech:000710.

Original event, source assessment and saved review remain intact; successor explicitly resolves only the supported curation defect without promoting status or waiving publication gates.

## Findings

### yeast-figure-attribution: Figure4 is vegetative extension evidence, not gamete-reset evidence

minor / resolved / confirmed; issue key: cellular-rejuvenation-yeast-figure-attribution.

The yeast note groups Figures1 and4 as support for gamete replicative-potential reset. Figure4 instead measures lifespan extension in vegetatively growing aged cells. The following sentence distinguishes that result but does not correct the preceding locator attribution; the sidecar repeats it.

Disposition: The corrected note explicitly assigns Figure1 to gamete reset and Figure4 to vegetative extension. Guarded correction, preserved original event and source assessment, appended history, tests and rendered evidence agree. The separate earlier publication hold is reassessed by the now-passing restored local and remote checks.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| source-0 | DOI:10.1242/jcs.86.1.263; MED scientific abstract, contiguous span after HTML inline markup removal | supports | Haga and Karino 1986, PMID:3654779; scientific abstract, directly read in the MED record. Young-cell cytoplasm restored sexual activity in senescent cells (about 700 fissions); recovery persisted for up to 20 fissions. Division rate and fertility after self-conjugation did not improve. This supports endpoint-specific recovery in treated old cells, not whole-cell or permanent rejuvenation. Full methods and figures were unavailable. |
| source-1 | DOI:10.1038/s41467-018-06154-9; /article/body/sec[2]/sec[4]/p[3] | supports | Proenca et al. 2018, PMID:30213942, PMC6137065; Results, Stable equilibria are connected by aging and rejuvenation (Sec6), directly checked in primary XML. Actual Figure 4d was visually inspected: new-daughter lineages from the old-cell equilibrium converge toward faster growth over successive generations. These doubling times are derived from elongation rates, not direct interdivision intervals. Recovery is in descendants, not the same old mother. The tested MG1655 conditions do not establish all-environment recovery or a universal damage mechanism. |
| source-2 | DOI:10.1126/science.1204349; MED scientific abstract, contiguous span after HTML inline markup removal | supports | Unal et al. 2011, PMID:21700873, PMC3923466; scientific abstract, directly checked in MED and an MIT-hosted author manuscript. Main text and Figure 1 support gamete replicative-potential reset. Figure 4 concerns the separate vegetative lifespan-extension experiment. Transient NDT80-dependent vegetative lifespan extension is a separate result and does not establish reversal of every aged-cell defect. Supplements and strain tables were not assessed. The retrieved PDF identifies the article but differs in size and checksum from MIT bitstream metadata; original deposited-byte identity remains unresolved. |
| source-3 | DOI:10.3390/microorganisms11010082; /article/front/article-meta/abstract/p | supports | Haga 2023, PMID:36677375, PMC9865852; scientific abstract, directly checked in primary XML and PMC text. Results 3.1 uses rejuvenation for suppression of mating in mature cells: that maturation-state reset alone is outside this functional trait. Results 3.2 reports recovery of old-cell mating activity after transformation. Figure 6C measures total cell counts over four days, not direct division times, and lacks a young-cell growth comparator. Engineered treatment is not a natural canonical taxon example; inferred chemistry is not a proven mechanism. |
| source-4 | DOI:10.1016/j.isci.2022.103765; /article/front/article-meta/abstract[1]/p | context_only | Cesar et al. 2022, PMID:35243217, PMC8858994; scientific abstract, directly checked against MED and primary XML. Boundary evidence: culture duration during stationary phase is not individual replicative age. Immediate regrowth can reflect preserved function, not recovery from a demonstrated deficit. Regrowth classes use area-derived growth rates; nongrowth during the observation window is not proof of irreversible death. Results 2.1 and 2.3, Discussion, limitations and classification methods were read; figures and raw data were not independently assessed. |
| content | data/traits/physiology/cellular_rejuvenation.yaml; Complete YAML, writer/tests, proposal v586, history, source-verification JSON, skill guidance, README and generated page. | supports | One PHYSIOLOGY CLASS under phenotype; functional qualifier excludes marker-only or maturation-only reset. Same-cell and descendant recovery distinguished. No exact synonym, xref, canonical taxon or molecular graph asserted; status remains PROPOSED. |
| snippets | research/traits/physiology/cellular_rejuvenation-source-verification.json; DOI-qualified MED/Crossref identity, exact paragraph/abstract matching, notice fields and actual-byte hashes. | supports | All five contiguous spans match; 20/12/17/15/20 words. Linked comment and peer evaluations are not corrections or independent experiments. MIT article identity is verified but the delivered PDF does not match catalog bytes. |
| novelty | proposals/metpo_traitmech_v586/proposal.md; Pre-allocation novelty assessment plus restored 13:01 UTC publication recheck and independent publishing-copy inventory. | supports | No exact prior trait or reservation conflict in the bounded inspected scope. Fresh restored local/remote checks preserve other reservations and heads; two owned copies are explicitly distinguished and their provenance verified. |
| products | reports/proposal_citation_audit.tsv; Native gates, byte preservation, parsed ROBOT RDF, browser assertions/screenshots and independent-clone recovery receipt. | supports | All1104 prior YAMLs and previous history/reviews/proposals/embeddings preserved;1103 old pages change only footers, phenotype gains one child. RDF triples {'classes': 15, 'merged': 12628, 'reasoned': 12632}; w3id parent-to-quality hierarchy verified. Recovery copied1133 owned changed files byte-for-byte without metadata repair. |
| access | /tmp/traitmech-rejuvenation-publication-20261012/result.json; Fresh local/remote assessment and /tmp/traitmech-rejuvenation-owned-copies-20261012.json. | supports | Earlier OS access failures remain in the predecessor. Access is now restored: registered worktrees are freshly assessed, all initial owned blobs match the retained checkpoint, and the corrected independent clone passes its own reservation scan. Cleanup still requires a fresh ownership check after merge. |
| figure-attribution | DOI:10.1126/science.1204349; MIT-delivered author manuscript, PDF pages7/10: actual Figures1/4 and captions; corresponding main-text experiments. | supports | Figure1 tests gamete RLS reset. Figure4 tests transient NDT80-dependent lifespan extension in vegetatively growing aged cells. Grouping both as direct support for gamete reset misattributes Figure4, despite the following sentence distinguishing that endpoint. |
| correction | data/traits/physiology/cellular_rejuvenation.yaml; evidence[2].notes, second curation event, guarded correction writer/tests, second history entry, sidecar assessment_corrections, proposal clarification and rendered page. | supports | Figure endpoints now distinguished. Definition, DOI, snippet, status and checksum limitation preserved. Original event/source interpretation retained with explicit successors. Corrected native gates and browser checks pass; no optional molecular/taxon claims added. |
| prior | reviews/structured/20261012T124741Z-cellular-rejuvenation/review.yaml; Open finding yeast-figure-attribution; separate failed local-publication-refresh check. | context_only | Initial needs_curation review remains immutable. This successor reassesses the whole corrected addition, resolves its figure finding, and records the successful restored publication check without rewriting the earlier failed observation. |

## Limits And Additional Notes

- Author self-review, not independent or human scientific sign-off. Full scope for this one addition, not whole-corpus scientific review or completion of the external PR lifecycle.
- Earlier OS access failures are preserved in the predecessor; fresh restored checks now pass. The original registered branch remains at the baseline with preserved uncommitted pre-correction bytes; publication uses the independently corrected clone. Cleanup requires a new ownership check.
- Earlier full review and source-access limitations remain: MIT delivered-byte/catalog mismatch, incomplete publisher/notice access, no full supplement/raw-data reanalysis or natural canonical/protein mechanism claim.
- The original focused test execution failed on inaccessible Git metadata. Its isolated rerun and the independent-clone full suite passed; no test was weakened.
- Source access timestamps include reinspection of retained primary snapshots. Only the previously documented figures were visually inspected, not all experiments.
- Existing product adapter skips and source-license warnings remain baseline limits; embeddings retained. Required TSV header tabs retain the narrow inspected exception.
- External review, PR CI, native queue and landed-tree/independent recovery checks are not completed by this bundle.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T130746Z-rejuvenation-figure-resolution
kind: record
repository: CultureBotAI/TraitMech
title: Full successor review of corrected functional cellular rejuvenation
started_at: '2026-10-12T12:55:27Z'
finished_at: '2026-10-12T13:07:46Z'
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
summary: 'Full corrected-record self-review: one resolved minor finding (issue1893),
  zero open curation findings. Five primary-source evidence entries retain endpoint
  and access limits. Corrected native gates, browser checks and restored local/remote
  publication assessment pass. External PR review and queue remain subsequent gates.'
source:
  git_revision: 1ee4d0ac5fb63a9d2c03c0aedea2e985d9422f8c
  state: working_tree
  inputs:
  - path: .claude/skills/add-trait/SKILL.md
    sha256: a19ce8b29dfdc02df1d9066ed9b26e9e30643c69733ff6f3a3ff05218aebaace
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
    sha256: 72ba95afe1e1865b4359873a5493c641f329f43109609d438def56128750256a
    role: context
  - path: app/dashboard/priority.html
    sha256: 39048248fe3e56b810039997b1f9196360f14174c51f62acf0a0b7311bf5d8ca
    role: context
  - path: app/dashboard/priority.json
    sha256: 12ae38f1f667ffd505415ef92a2ec6e942d8276762b3df4e69bcce0aff31df3a
    role: context
  - path: app/discussions/data.js
    sha256: ffbae285078e5ded5b80dca966b5e7960355c6122f5a7e0f492c343649b49b9a
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
    sha256: 08ca33dd7e50c1a402645fd0c59bb59846c02d71dfde82319260a995d4bd9762
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
    role: target
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
  - path: history/records/cellular_rejuvenation/2026-10-12T121656Z-codex-a49ab2.yaml
    sha256: 8e540d6cee78457667bdb5bfe04f93bd6c7c7298ab8d1abd3497ee5c8b80a6a8
    role: context
  - path: history/records/cellular_rejuvenation/2026-10-12T124939Z-codex-e5fcad.yaml
    sha256: 47ca9b7f85f148220d03e03fb5448f338d2dbd57bff91b6ea7068b773b3f419b
    role: context
  - path: justfile
    sha256: e6047ea612115a6a78d100b281483ba824c860c3def59bcd0d40e7fb56b3526a
    role: context
  - path: pages/browse.html
    sha256: 0312a8570a3c816c11cf59b3ba11bce83623ead340661f8f6fa392a094412ce1
    role: context
  - path: pages/category/ecology.html
    sha256: 7ea104f645e764eb619301209f6c742a71497b1a6843f7a35603cf14b2b739c7
    role: context
  - path: pages/category/environment.html
    sha256: 2eb35114b602332e8d070f5240990ce03cd318117f0932fee2765947d1e59359
    role: context
  - path: pages/category/genomics.html
    sha256: 771a0ee6250be72c3dfab8d275918c7e45dc5ec6e7982190bcab64e723e5d217
    role: context
  - path: pages/category/metabolism.html
    sha256: bbea3b0acbaa2c8387be5246eb7fdfd536104d24f0611ec1b1cf577d596f8e3b
    role: context
  - path: pages/category/morphology.html
    sha256: 8547a02c444b29c211965fccf66cd9f71d2c5abf8d289834a94b2a4b1f44f39f
    role: context
  - path: pages/category/observation.html
    sha256: 694074a346f079313b8cd23d7748def50b8ca9ff011c15592f4235d49a955c48
    role: context
  - path: pages/category/other.html
    sha256: 3cf7c7f5193b551f30aa5b1b0fd570e9b24f293323eb8b5e93bcf7363e227bf8
    role: context
  - path: pages/category/physiology.html
    sha256: c6b6a4ab0e923999e3e9b439c7b66053995adfeff8001f6bf9bcf3f152fdc212
    role: context
  - path: pages/category/quantitative_property.html
    sha256: fee63caba5f651c618197d971dbd59d973583e9a8a7305065af5d06013f9b9cb
    role: context
  - path: pages/category/upper.html
    sha256: 2a0dd01749d7b043de32ee90f4442933618879be93ab8a2fda86404725b98d5b
    role: context
  - path: pages/graph.html
    sha256: a53807839f50b947ba9db6e908bf6e630240ef56173eeab5e6cd9face9d06da4
    role: context
  - path: pages/index.html
    sha256: be290f759162c1dfac4a6ab3181bef07a265fb83e338c3ca7883d562993093cd
    role: context
  - path: pages/traits/ecology/animal_pathogen.html
    sha256: ce122b49e186b5a3f062f068fea2f7fe1b018f02d2e94fc00220e0872c440313
    role: context
  - path: pages/traits/ecology/bacterial_cannibalism.html
    sha256: 76a0059bf4a9bf85076f32b08e37a01179be2eaec185af4db15abdf0ad69b4ed
    role: context
  - path: pages/traits/ecology/bacterial_mycophagy.html
    sha256: 5ccbbfb501d528e43cb0f329f59f61ba104721da9e7244d46ff0c9c49e41a58e
    role: context
  - path: pages/traits/ecology/biofilm_formation.html
    sha256: 697b645dbbec95bd78938f5d2838114c8c1202235f0db588d799188c80d13eb7
    role: context
  - path: pages/traits/ecology/biosafety_level.html
    sha256: b529df77437db50d3463861db604d2b16f56718d5b96f0a9a6249579a69f41d1
    role: context
  - path: pages/traits/ecology/biosafety_level_1.html
    sha256: c180ab25993e0602e1441af416d10ef80425f2d965658504067dbc1f9e97bdb8
    role: context
  - path: pages/traits/ecology/biosafety_level_2.html
    sha256: e9d47c8060f20ac3cd4608f2b5675dc2dbb1e90da9efa0025738d1b5c3aeae1f
    role: context
  - path: pages/traits/ecology/biosafety_level_3.html
    sha256: cce3bcb70884f40080c722c8e1064f227a98ee43cbf3ba15f298b4b843485fea
    role: context
  - path: pages/traits/ecology/biosafety_level_4.html
    sha256: 054b074e65ce04e19b87d4c6cd18c74aab5419c58600ea2286af23ecb5ad9737
    role: context
  - path: pages/traits/ecology/biosafety_level_5.html
    sha256: 1c9904fa131b2bfa15b2586442c17ec66ff7fdf290d3a2f77820e974a74b01d5
    role: context
  - path: pages/traits/ecology/collective_bacterial_predation.html
    sha256: b5eb0a0a870374a91d1b8b63b8fa3d5441d69081de7da8698023e4c308ea035a
    role: context
  - path: pages/traits/ecology/commensalism.html
    sha256: b24a8e8b55e488f42182816eaad77016dd1e2fae84b0d4f672c1a77947ab1848
    role: context
  - path: pages/traits/ecology/cytoplasmic_bacterial_predation.html
    sha256: 873e68890f4f607c98055fbd5b904119d46ab3299e4d382c6af56251b2726a35
    role: context
  - path: pages/traits/ecology/endophytic.html
    sha256: a0783ec7f9fde95b85297eccc6682740d60d5e66969674fd6df0ec61709b0dc3
    role: context
  - path: pages/traits/ecology/endosymbiosis.html
    sha256: 2580cc050a220f8797494eddd7e623557923ba6ecebd2906fa105d02aba476a0
    role: context
  - path: pages/traits/ecology/epibiotic_bacterial_predation.html
    sha256: d8ee2a2e52b5bf7ee0186d911d78b75fc3a453b6a72416e0afcb72b0cbffb99a
    role: context
  - path: pages/traits/ecology/epiphytic.html
    sha256: f723b709c692edc943929c846c1bc525325fb696dc16ae561e8895b69914fceb
    role: context
  - path: pages/traits/ecology/free_living.html
    sha256: e4d7eb04571504979eb9859b1db944983caeb638954c1fc337e674f0f29e312d
    role: context
  - path: pages/traits/ecology/gut_associated.html
    sha256: 288e6b23120882cfd59426a8c8566966cc8562025f1b854da7703c7c32fef0e1
    role: context
  - path: pages/traits/ecology/habitat_association.html
    sha256: 6eb8bddbc8586f4f71ccebfea22ca8ab8e73de99253d3402210c896fd81b05f4
    role: context
  - path: pages/traits/ecology/host_associated.html
    sha256: cbb595bba3763e2c392abe3d4196bb2963f752b58cabe7fe863fe941ffa50f53
    role: context
  - path: pages/traits/ecology/human_pathogen.html
    sha256: 61799b21c40d57a5ee52fd77bb9c6fce3d0ef12f6364d33170c30100c2407e9b
    role: context
  - path: pages/traits/ecology/ixotrophy.html
    sha256: 9a182a1bac0fbb32dc95cfa137f9b2110f85e64cc420eaac79911cfe55692806
    role: context
  - path: pages/traits/ecology/mutualism.html
    sha256: 689acff715ef6f27d1b438e6c563eaca45abf3998e42e23e0be43bdbe0273297
    role: context
  - path: pages/traits/ecology/nitrogen_fixing_symbiosis.html
    sha256: 9fd57e51fac0bf1ab8bb68e1fa78f3477a05fa8878d90506678e8cecc155ec74
    role: context
  - path: pages/traits/ecology/opportunistic_pathogen.html
    sha256: 5576ea35eddb6b75ce863f6ce7e04ae51d1b592565a341a54b5d63378b131616
    role: context
  - path: pages/traits/ecology/parasitism.html
    sha256: 82758885dc5870945f83984e463c8bd8ec938b8acc4b27f5a0d848c641eb1c5c
    role: context
  - path: pages/traits/ecology/pathogenic_to_host.html
    sha256: d2c06cf5f852d348b70c36596117632ec291792ce93e6e9b5fda8ec801698032
    role: context
  - path: pages/traits/ecology/periplasmic_bacterial_predation.html
    sha256: 621bfb49628ff3302c85df36cf98eca92b962dcc0bdb9da97914f8deec18ffbb
    role: context
  - path: pages/traits/ecology/plant_pathogen.html
    sha256: 729ae579704d11b2262819d408f9efaa3de2522fcb0c1ae0055c49f685957e6e
    role: context
  - path: pages/traits/ecology/predatory_bacterium.html
    sha256: fe499e51034821c1d5250ba249aa0bd73df11817687418c76cda01aab1367e14
    role: context
  - path: pages/traits/ecology/rhizosphere_association.html
    sha256: e240c5fc4d58afddcaecf353c088488f6f29001a8d587e878fda218e83debbb6
    role: context
  - path: pages/traits/ecology/saprotrophy.html
    sha256: 100a92d59d659c64b4245f25a66dc2818aa32530ba404b3f769de5aed5cfaec5
    role: context
  - path: pages/traits/ecology/soil_dwelling.html
    sha256: 9220318b4f325f490414bc26c30b27cf950a2e87737bf2f1bc8636f00c9ae7d9
    role: context
  - path: pages/traits/ecology/symbiosis.html
    sha256: 629faeac1136f7bd0f28d09a9d026f7e263292c1a48be3473d9d2e2afdac4964
    role: context
  - path: pages/traits/environment/acidophilic.html
    sha256: fcb2fb11f6390583a968507bc8f6d375cb12d75f8b6faa16c86b454030ce9b77
    role: context
  - path: pages/traits/environment/acidotolerant.html
    sha256: a36da08b0c3a0093309253bc55d4e7a4169bb01effe33a0873d6fa639c28975a
    role: context
  - path: pages/traits/environment/aerobic.html
    sha256: 38c83db2743be2195a16a1c3ec5108016ee1cc907ba14d0eaa6cf32a6acb3a1f
    role: context
  - path: pages/traits/environment/aerotolerant.html
    sha256: 227df08870b86f74c818dc791741c8aa7698f5e5a3b466d88b7d5fb98e748105
    role: context
  - path: pages/traits/environment/alkalotolerant.html
    sha256: 866fe0d193e88cd6c180a53b8b55dad2e8b39545bf95e4852b0a053063cb318e
    role: context
  - path: pages/traits/environment/alkaphilic.html
    sha256: addb618e721f502fc44a9002f79d2a2444f1dbe32f2cd3aafc7fba719c1035b4
    role: context
  - path: pages/traits/environment/anaerobic.html
    sha256: 1ea91c5bde4f0f7f7f942a617a06dbe9f3685af47c468e49b99460d0bf7d5199
    role: context
  - path: pages/traits/environment/arsenic_tolerant.html
    sha256: 76f938ea405a6e7fc43b2c58cd377b2edc8c978e3ce81dcb3ea2fe1ac4a5d6fa
    role: context
  - path: pages/traits/environment/cadmium_tolerant.html
    sha256: 2b4561770a4f7c55989e9d618a190829986282c7230e88d99768979520f12db8
    role: context
  - path: pages/traits/environment/capnophilic.html
    sha256: 2449d29205195a68a036deb24a3b25dd7bf65e823ed29651946b3695d122dd95
    role: context
  - path: pages/traits/environment/cobalt_tolerant.html
    sha256: 18cad1fce5d9ddfe462741318bf1796e0deba8265cf2e0e12c5a202f46d67045
    role: context
  - path: pages/traits/environment/copper_tolerant.html
    sha256: 0565e8b5b81fe0338a1945b7fe1daf56f674bb197fbbd81c01d1cb7f64cf1444
    role: context
  - path: pages/traits/environment/delta_phenotype_with_numerical_limits.html
    sha256: f5d4b249e7378d9499d84552e21ba867931c5eae5dd64140216e771b1f57537c
    role: context
  - path: pages/traits/environment/desiccation_tolerant.html
    sha256: 005c12c2567e264590a1f83cb9d77063a92bc9a78a980ea63cc624db9f585535
    role: context
  - path: pages/traits/environment/euryhaline.html
    sha256: fc36f575c3c60f4c0cd5d099ab1c15b2881e9601a72caca6e171b964c3972018
    role: context
  - path: pages/traits/environment/extreme_hyperthermophilic.html
    sha256: 513cb68d969ec2533ab80f7512e2033feebc2bf99dfe455974f0b8086db70eba
    role: context
  - path: pages/traits/environment/extremely_halophilic.html
    sha256: afeee6e2e2798c26c3541259ae10705256a6298234c16bdcea9a7849c51712fd
    role: context
  - path: pages/traits/environment/facultative_oxygen_preference.html
    sha256: 16f5d7a9b83e93db8f6218652e6c77f0ceeac19a9ef6f71a4caf6e5054bf2f88
    role: context
  - path: pages/traits/environment/facultative_psychrophilic.html
    sha256: 148b06ce7ce8de5d77c55f52d77b2477ae3a0e1b1dab529b250f324fbb21406d
    role: context
  - path: pages/traits/environment/facultatively_acidophilic.html
    sha256: 7060b8d1ecd49a2f8e9c53e819fcd2f2cc86f29b32a80ae6b238c70a27300f97
    role: context
  - path: pages/traits/environment/facultatively_aerobic.html
    sha256: fc455d5de48dca6d8fc0d1f43ebfefbad34ea3a05184138ff79cb9600d6aa4d5
    role: context
  - path: pages/traits/environment/facultatively_alkaphilic.html
    sha256: f82e5696e0cebcc341c98c5d5b250d80870d996e4a96e06012404eb8f6265259
    role: context
  - path: pages/traits/environment/facultatively_anaerobic.html
    sha256: 40c864877037fa732d0a0723c12c0eb806f85a80a65526467f499e34da0d8a81
    role: context
  - path: pages/traits/environment/growth_range_phenotype_with_numerical_limits.html
    sha256: de45caec2945ed6635053017e520915522c9e4d58099d7583a48a64bf498eb17
    role: context
  - path: pages/traits/environment/haloalkaliphilic.html
    sha256: 8846311909807d1d6257cfb0f6d9c3bb9632e9d0b68936270da330b90339b145
    role: context
  - path: pages/traits/environment/halophilic.html
    sha256: 678238709d58fa9956c61f632c28a71d0c977f3fc6ae1f886fc30e557e1b4b86
    role: context
  - path: pages/traits/environment/halophily_preference.html
    sha256: 16ac169c25970236964acdaae1e73e94614055f826ddf37c34427b16128b7052
    role: context
  - path: pages/traits/environment/halotolerant.html
    sha256: fb796f11f724c176610d80d3f4a59fdcb557bc00cd493f909d1b20cd9dbb2e58
    role: context
  - path: pages/traits/environment/hyperthermophilic.html
    sha256: fedc4e345d4dc72d3c6003436a7326e17c6fdfe67e724eec4ef6a4753848e69b
    role: context
  - path: pages/traits/environment/ionizing_radiation_tolerant.html
    sha256: d28400bbd839247d0525910821ad6411837e9490b585e3f22bc7d2fc71b234f8
    role: context
  - path: pages/traits/environment/mercury_tolerant.html
    sha256: e7ca69df2dab1a271c3e0f2cbee17d244c1bcd756dabd8a6327678dc066c6015
    role: context
  - path: pages/traits/environment/mesophilic.html
    sha256: e7a62c561e97156a8491d0470dc315a676dab8e25281d4a9bdacea76a1da7c83
    role: context
  - path: pages/traits/environment/metal_tolerant.html
    sha256: d3454434165d9e8c175ed510323866b92c7a4f6066d881737798c353d003b269
    role: context
  - path: pages/traits/environment/microaerophilic.html
    sha256: 3cd176a57a29c9dad0caef28d62c7d2feddd535b85d5f7ceb8aa3ac0acd84faf
    role: context
  - path: pages/traits/environment/microaerotolerant.html
    sha256: ebfac15166c6b8ae83a1a8650863540dbd73cd0f5f473488aca5e44cdf7e180e
    role: context
  - path: pages/traits/environment/moderately_halophilic.html
    sha256: fc9c62d7816dc224f39f7b9377fd852c5027a12d79686165f99bfa5bb785272a
    role: context
  - path: pages/traits/environment/nacl_delta.html
    sha256: 1e73a343bc4a4439409a0ce21961538c90a2134b8206868c643a178e938cad68
    role: context
  - path: pages/traits/environment/nacl_delta_high.html
    sha256: 296d9690f233197306335917420cb65520b0f7dd4d9c5fe6f80b3be08f6d1eb7
    role: context
  - path: pages/traits/environment/nacl_delta_low.html
    sha256: 55718a93666de05714919d91d796c16e1a589a2e29423ec798faa8dede833936
    role: context
  - path: pages/traits/environment/nacl_delta_mid1.html
    sha256: 487113202716676abd217308a293a2e8bd722f79fd10b1f40d3906d1e6317c6e
    role: context
  - path: pages/traits/environment/nacl_delta_mid2.html
    sha256: aa0e06107e9fca918119f98f0bd958dc98c3dfe3829c09b0c62c5cf3f5fbb368
    role: context
  - path: pages/traits/environment/nacl_optimum.html
    sha256: c9fe9916dfb70e55ee53b58b6ccb7eefbe9755863f774627df61b943cf378053
    role: context
  - path: pages/traits/environment/nacl_optimum_high.html
    sha256: 346e6727744c43380d55f33268f7a113ab2e973d7f47909c36066ab9ebd01650
    role: context
  - path: pages/traits/environment/nacl_optimum_low.html
    sha256: 10039b1f5246de784dddd699f011187ebdb459863057e2c4be3ce97447bf2119
    role: context
  - path: pages/traits/environment/nacl_optimum_mid1.html
    sha256: 0b6fbe5d3217452a60f59b1d7fb244712ee8cc2c10e222e0dfc97dc0e5fd412b
    role: context
  - path: pages/traits/environment/nacl_optimum_mid2.html
    sha256: 2add53315179b3d0208a69828eb9f7cf1e8da26ef4d63f0d4e523e43db755448
    role: context
  - path: pages/traits/environment/nacl_range.html
    sha256: a43e13ee29df673c01089e70de345050860db096c26ddb25e6e3438dd27ef338
    role: context
  - path: pages/traits/environment/nacl_range_high.html
    sha256: 00fdbc2278b24df1dc2f58c3cd91d5b531e302f4de2752b27f3f99683f105cc2
    role: context
  - path: pages/traits/environment/nacl_range_low.html
    sha256: e6f4285e88b9dfe2232b9c943afa4b609cb21ad6e59b744adc5aece804ea198d
    role: context
  - path: pages/traits/environment/nacl_range_mid1.html
    sha256: 26355d70b09b170b2e9f690bfeb8f750d34e3610662b8ff9db591baa1c0897fe
    role: context
  - path: pages/traits/environment/nacl_range_mid2.html
    sha256: db214d0ce6ec2aeb5f086dee2586f39b860479f976e96f263bebbf5f02984312
    role: context
  - path: pages/traits/environment/neutrophilic.html
    sha256: e51187d17a44b6bc87557942d9f69d46f92eba4d9bb95c0f72c8fdc428b30692
    role: context
  - path: pages/traits/environment/non_halophilic.html
    sha256: 198bf63c776a93de4aad974fe9a76bbef964fe1b27356c531f4c003e14c9f080
    role: context
  - path: pages/traits/environment/obligately_acidophilic.html
    sha256: 79dac5e2861ca874d05e470da5f05d107e0b10099f4af0d0cc5341ab9bd3f33a
    role: context
  - path: pages/traits/environment/obligately_aerobic.html
    sha256: bbf3cec068ab859033302395c5eaf6c9bb0b242196b1f8b425b798b265deb757
    role: context
  - path: pages/traits/environment/obligately_alkaphilic.html
    sha256: c7f976e10bb9d75672f0571eea1a6c69b8b2e5a8fb8fb72cf52f1af367eda9f4
    role: context
  - path: pages/traits/environment/obligately_anaerobic.html
    sha256: f92356ad87828880e928bd641c590610a11495456c35a2d7b40cb7ab6e4a40c2
    role: context
  - path: pages/traits/environment/obligately_piezophilic.html
    sha256: b34b5e1884daf1c4e7f02aa223f37bf2f3eb5446b9388c25418f942e1a38fb65
    role: context
  - path: pages/traits/environment/optimum_phenotype_with_numerical_limits.html
    sha256: 1431939f070811d65668298355b2bffec96b801d686231e6d7288e66aeb12e3c
    role: context
  - path: pages/traits/environment/oxygen_preference.html
    sha256: 3794d2a72049ebe03f86148e0462fe6c8a572b130439086608d69d142855e26e
    role: context
  - path: pages/traits/environment/ph_delta.html
    sha256: 306195bdece85a9379e25d6e107a7cd9d8ad28c14865c59729e821167d7cfccb
    role: context
  - path: pages/traits/environment/ph_delta_high.html
    sha256: 1fc7080b1de3d5f57bdcdc69d0db5d547395598b0f917b9463cc0ec206bdfccf
    role: context
  - path: pages/traits/environment/ph_delta_low.html
    sha256: eba097c2da60e78f448a381600251e803f9df6aba974ca5c83dd5da0934a4e57
    role: context
  - path: pages/traits/environment/ph_delta_mid1.html
    sha256: e7811c5e55444d2e800e82ba1f7db86b9d228e8d1795aa4e7b2c3d89e0cf6d37
    role: context
  - path: pages/traits/environment/ph_delta_mid2.html
    sha256: f26d6ff81ac7bb572540ec8f68afd54c6f1d81daf0c9f8b0f28a248046409f7c
    role: context
  - path: pages/traits/environment/ph_delta_mid3.html
    sha256: fcc6be010915e9b6750e0a1754e0846c579b6a59e348398d7df1344a19503092
    role: context
  - path: pages/traits/environment/ph_delta_very_low.html
    sha256: c747d76978c9c4a17815a4b6e4fc042b6a82e3296b0fba88ab1d570b9a308acc
    role: context
  - path: pages/traits/environment/ph_growth_preference.html
    sha256: f86f5596b62bca92d64cbb84cf848c4d8dd7967ab6fb88a6f0a9b37c9c5a74ac
    role: context
  - path: pages/traits/environment/ph_optimum.html
    sha256: 8883027f0ad3683caff50117d2ab8fc7c5ab1098871c99599dd1810f8c79564a
    role: context
  - path: pages/traits/environment/ph_optimum_high.html
    sha256: bede55cfd7bd5565668d185d4778bf71f476c6502febca52e093b314055c3f4a
    role: context
  - path: pages/traits/environment/ph_optimum_low.html
    sha256: 5a37509d3228f96f47478e1afdd58900dde6693d506f0ca6578e84d5cfff6a48
    role: context
  - path: pages/traits/environment/ph_optimum_mid1.html
    sha256: e3cc48ec3861034d4d68f5af1e1eb13bb08b4a6dcc19587675744a5894c0e15b
    role: context
  - path: pages/traits/environment/ph_optimum_mid2.html
    sha256: 2170738da6095ff7d1a3fda99374dd7e06038092add5d38477941258954e485f
    role: context
  - path: pages/traits/environment/ph_phenotype_with_numerical_limits.html
    sha256: 987c9f70dea796141d35c61c54034f22d0abeadb962eb18b8d3d9b8c5fbfcad0
    role: context
  - path: pages/traits/environment/ph_range.html
    sha256: 54637c97f2fb713c88f58ae65b6aa057924d06e5a1f6bac8d2e8e0cdfa87f620
    role: context
  - path: pages/traits/environment/ph_range_high.html
    sha256: 562d05a9a7795b66db2f5dd49c09f51982de39faf151710b159c0e275484cb27
    role: context
  - path: pages/traits/environment/ph_range_low.html
    sha256: fe026e2f2286f48bb8ea1279dfa10d1a43b4ff18cdb3c79358cb9c9c1668d5d5
    role: context
  - path: pages/traits/environment/ph_range_mid1.html
    sha256: bd38dd6bc2099fa50aeef38c958c94b7e9853419436ff648f77cfe5b5c220387
    role: context
  - path: pages/traits/environment/ph_range_mid2.html
    sha256: 77e279c877a9ffbd27307946f73e143aa046b308981c0f0590ca8db8a3076721
    role: context
  - path: pages/traits/environment/ph_range_mid3.html
    sha256: baedf757dde873cc4e20b030268f32ac7e93ffc119cfec61caf8ede56fc6d435
    role: context
  - path: pages/traits/environment/ph_range_very_low.html
    sha256: 4f9df13400780a6b6de1423ee455549231a9651b7a0c3cd401f1271ffd933472
    role: context
  - path: pages/traits/environment/piezophilic.html
    sha256: 27b0c2ac7d40e3f841a0a0cb95a4e523671dedab91ce2eddae482189c4caaa6c
    role: context
  - path: pages/traits/environment/piezotolerant.html
    sha256: 846743634deec3e8ca3aa63fe59ace5a0a322ec76725bd89029fcac2fb56d306
    role: context
  - path: pages/traits/environment/pressure_delta.html
    sha256: 9c5b11703a414a222a01b29d7be8600a1f466a9dc09442cae32b23ae12c62340
    role: context
  - path: pages/traits/environment/pressure_optimum.html
    sha256: 432d8f93da23e183a4509d2749c39e33e35071f03ea8325e9fbb4dd899aeda53
    role: context
  - path: pages/traits/environment/pressure_range.html
    sha256: 8877267a0e51aa52ee57048d883c53bd28f083920ddf54ea79f4dfc5b2821e81
    role: context
  - path: pages/traits/environment/psychrophilic.html
    sha256: ddc5205522f47a76aed6f40672fad2859f51af58670a132ddafcb3b719c9b576
    role: context
  - path: pages/traits/environment/psychrotolerant.html
    sha256: 9ff9eb0ff48eb48bdd004d502766105f15b307463bc6ba826da8aee03ab24cfe
    role: context
  - path: pages/traits/environment/radiotolerant.html
    sha256: 64f5cd25bfcfbe56b1864f0f5029ac74b7ece6b7d8c1717e77249b3dce984b12
    role: context
  - path: pages/traits/environment/salinity_phenotype_with_numerical_limits.html
    sha256: e39149001cca085811a7cc8b4a30c248569745362923bb7a10cb868d1a376705
    role: context
  - path: pages/traits/environment/slightly_halophilic.html
    sha256: 34becb5b4c55ca01be472cafd0ac9c16275d2c493bf04c8180ef8f6839749316
    role: context
  - path: pages/traits/environment/stenohaline.html
    sha256: 1203e00a27df14bcc00c43253d0033a52aa886a213822e73627e168a36d60db1
    role: context
  - path: pages/traits/environment/strictly_anaerobic.html
    sha256: 853f6749147ff3f9c586f258dcb070398fa21fa3c4fe72c6ca636fca21392f9d
    role: context
  - path: pages/traits/environment/temperature_delta.html
    sha256: e6c191b29b2ac053498668b59767c2e2226b945521770dc33e529b9b784d50a2
    role: context
  - path: pages/traits/environment/temperature_delta_high.html
    sha256: 4322825fa089c637ca1b84e2f6e028900b834261c6e0be2a2975f2201691024c
    role: context
  - path: pages/traits/environment/temperature_delta_low.html
    sha256: 98f69adabbc791f9aba64a4b3240f6a90c0599cb1432206100dc9d27dd31084b
    role: context
  - path: pages/traits/environment/temperature_delta_mid1.html
    sha256: 2c0f7e569ad82a8ad982d71fc8bca3da50c24ead7ae1731d92e0534677270744
    role: context
  - path: pages/traits/environment/temperature_delta_mid2.html
    sha256: 211c16896abba43638d45f48d892ad93fc041da72f837f4119a1498a24694a78
    role: context
  - path: pages/traits/environment/temperature_delta_very_low.html
    sha256: 8fa71f0dd2d3b81420b3ca41c4244490f27890f8dd897694238c4b313778ada7
    role: context
  - path: pages/traits/environment/temperature_optimum.html
    sha256: 57af8ddcbd47d76150563cfc19a1982fe5a46bb374c58833c7b9eebe0e995537
    role: context
  - path: pages/traits/environment/temperature_optimum_high.html
    sha256: b750c403f99cfd36ae8b398bce5c3d8208c4c8aea9500824ddb0b153f8bbe5f6
    role: context
  - path: pages/traits/environment/temperature_optimum_low.html
    sha256: 680a079136b10890c5e9d7bf8b401b89eb37b8c57f3f05c59c1d685811458732
    role: context
  - path: pages/traits/environment/temperature_optimum_mid1.html
    sha256: fa1794d269ce2d53920575bbaa3769f654dcacc39b2679d299191265e4af16eb
    role: context
  - path: pages/traits/environment/temperature_optimum_mid2.html
    sha256: 53deff558c91a39b8a5e33e28a88716a1c1280a6b42a3868d377702cef7e0e76
    role: context
  - path: pages/traits/environment/temperature_optimum_mid3.html
    sha256: 8b4d75ad2151aa35fa318de146041a9809dd92fb96a1f641ab8be14b3f0704c4
    role: context
  - path: pages/traits/environment/temperature_optimum_mid4.html
    sha256: be68439960b3460e39ffae3cd2f16e3bd60abb823d53aa9bc3728838af32d531
    role: context
  - path: pages/traits/environment/temperature_optimum_very_low.html
    sha256: ade37fade8829dd9f5b2453948fb5ebb368557da1746f3da84b9e82afe4f37aa
    role: context
  - path: pages/traits/environment/temperature_phenotype_with_numerical_limits.html
    sha256: 954946a30049fc6a77f5752917016733113e2c72ac50a5fe2f018bb8b3d9305e
    role: context
  - path: pages/traits/environment/temperature_preference.html
    sha256: 48e1dc1cbdf577eacdd3f7a6c354ea6d883d3860bc5535ae5ef8499b15ffce54
    role: context
  - path: pages/traits/environment/temperature_range.html
    sha256: c0042c585ecc5832501ab0c53d57c47646d46c4f6140a54b45837df8f3db6b0d
    role: context
  - path: pages/traits/environment/temperature_range_high.html
    sha256: 3f11366f0b58555346219d6b779b64f4dfdc8bed02444baf7cc2df5649158f54
    role: context
  - path: pages/traits/environment/temperature_range_low.html
    sha256: 41cc1e8cd92d7f224a2a572ec3e6a7fad638db44e6529a0ab902275eb55bd062
    role: context
  - path: pages/traits/environment/temperature_range_mid1.html
    sha256: 29080beeca7a2ba28b021d5d8fd890e869f4d1468be0429d77e03ae10c4ae05d
    role: context
  - path: pages/traits/environment/temperature_range_mid2.html
    sha256: fc1f243c69ea2074c75cfb75d40905c139f551db9c60e51b105a610ebae38657
    role: context
  - path: pages/traits/environment/temperature_range_mid3.html
    sha256: 53d7d11b4100038308e8552e7cf8325aa4173415487fb5b1c5e5a5ccc574819b
    role: context
  - path: pages/traits/environment/temperature_range_mid4.html
    sha256: ac77a0f0cdd9f18907eba15e96501945113af0aff9a9bae91a28b9a86dde3d31
    role: context
  - path: pages/traits/environment/temperature_range_very_low.html
    sha256: bacd78573b74048c8c6e29574b414627f2ea0dd8f7919252602fc3131e2585ca
    role: context
  - path: pages/traits/environment/thermophilic.html
    sha256: c47d038ae6fb4441de54c29322f6c7d2fe105154e73b4d71fb083c137cfbdd89
    role: context
  - path: pages/traits/environment/thermotolerant.html
    sha256: 628be0499ef71938ac972fe1c2489c4d11b076c2fdf36df38d7fe1a0b1716adf
    role: context
  - path: pages/traits/environment/uv_radiation_tolerant.html
    sha256: 3161c5fa379ad12048f557a3ba7967a6c13b46c4547284b9953f82b0390afd8c
    role: context
  - path: pages/traits/environment/xerophilic.html
    sha256: dbc6125dc80e7f0f5aea421437ba4352c1c535c5dde3f99c954def678048bce6
    role: context
  - path: pages/traits/environment/zinc_tolerant.html
    sha256: c49833ce27df1bd5eef355faba6681951b1bb33902e4c2780a9d67c751cca0df
    role: context
  - path: pages/traits/genomics/abi2_system.html
    sha256: 54d2c412eb330381a49bfdf5f751a4ca90dbe526ec3fcd93ae9893a35b813925
    role: context
  - path: pages/traits/genomics/abia_system.html
    sha256: 4145a17e422bf91bfd71b3d90154089411618824fa691917445ea3215f30ea0e
    role: context
  - path: pages/traits/genomics/abialpha_system.html
    sha256: f0139e3d3fc3e2f159e39f3a3609cf649ad85b3c948cbdb03ecba1c164866df0
    role: context
  - path: pages/traits/genomics/abib_system.html
    sha256: 5bd19772e27fa1d6268b40bb66229e5284e718ec3a9e5a77c8581f788ba18b68
    role: context
  - path: pages/traits/genomics/abic_system.html
    sha256: c23728aa0a38644d779d52655e8d6026e2e2ed4f57049419df2c032b862a0e8e
    role: context
  - path: pages/traits/genomics/abid_system.html
    sha256: a0a14ca37bbb2aacb6e348c54a0e4e19dc9c7427eac785c94e1ec5c32abc1754
    role: context
  - path: pages/traits/genomics/abie_system.html
    sha256: 10fa6052b2cb9b40134eb79639f514b064c2a1caa581e3663cc99e42b7d43116
    role: context
  - path: pages/traits/genomics/abif_system.html
    sha256: ae4a01b563b9fe947ac1134253468dff6f1842dc66a2ef7c53767a88205745a0
    role: context
  - path: pages/traits/genomics/abig_system.html
    sha256: 06cfd797dceaaa2d90a96226052f49208c575e5b758c3c986d3b85a5b2f9ff08
    role: context
  - path: pages/traits/genomics/abih_system.html
    sha256: fe155d30e2c00a63563119f7bbfae27933eb385032a5fd87baf6b51859814572
    role: context
  - path: pages/traits/genomics/abii_system.html
    sha256: 990b69c29bb9979982d9075b8e092d88c108e5c566d20254b3bf924f2a0c36dc
    role: context
  - path: pages/traits/genomics/abij_system.html
    sha256: b1bc1819c95d02461af2618c4174380169a9c3df1b7fbd2c0cf7a40ef02910f2
    role: context
  - path: pages/traits/genomics/abik_system.html
    sha256: 074d0f3ed09ef890c6248e9f4e003b584c1b54e2e3e8cc41b8cd74ecab0f1c5c
    role: context
  - path: pages/traits/genomics/abil_system.html
    sha256: 6a787b0192e4f8175b7fcb09f8f814b856bc7148c9cce9730793f4357c7e5cba
    role: context
  - path: pages/traits/genomics/abin_system.html
    sha256: 950b5c87dbe103ded501953f3a6496ba2d34ca77e58ccc5d921878752c198373
    role: context
  - path: pages/traits/genomics/abio_system.html
    sha256: dc060c56b35dec343f17f5986b78bff45c037466e085fd9534d3e3036f0caa58
    role: context
  - path: pages/traits/genomics/abip2_system.html
    sha256: 281e08bf6099943740efd5a7deb903f6dabac58b73f77b5d1fcfaeeb0b44f42e
    role: context
  - path: pages/traits/genomics/abiq_system.html
    sha256: 007c7f0a77990a689417869117a55df3bc11ea3486425245af76309094176b3f
    role: context
  - path: pages/traits/genomics/abir_system.html
    sha256: f1921303fb036b3cc377be725c3313b22ad8ae76a56c3d9f6ca35fd849e0c58a
    role: context
  - path: pages/traits/genomics/abit_system.html
    sha256: 46cabb96c1ae47ce27437e68f957013a8a6858b0d192e459247b7b6c527d493d
    role: context
  - path: pages/traits/genomics/abiu_system.html
    sha256: ad18e431b863c4adbd6e9aa2ab17cff3bc20c179c24a3e9411314bb29ea1606c
    role: context
  - path: pages/traits/genomics/abiv_system.html
    sha256: f26e1e02a634ffcd449f6f7a3903a987c4b65c0d13789dc670d7dec2a3b6f7e2
    role: context
  - path: pages/traits/genomics/abiz_system.html
    sha256: b199a377555298df910af280ac8b41c7b9c66a70e3daa20449134331c0edc493
    role: context
  - path: pages/traits/genomics/abortive_infection_system.html
    sha256: 9227e363e745ad2ab31d6dc8115e1ed7a8318b332a0a63b5d122301ebf325db5
    role: context
  - path: pages/traits/genomics/aditi_system.html
    sha256: 59957206e2c238dc2e7831fc5a17e107f36e6c31222e738704449f34c70a0927
    role: context
  - path: pages/traits/genomics/ambrosia_system.html
    sha256: d3a83836268e41843b084b1f268c91a9d373dc4aaa17f8f44db3d972bc45f11c
    role: context
  - path: pages/traits/genomics/apsab_system.html
    sha256: 2331fc1f557e59463b65af1219ebdc669de222eabd697e849593f5c3cfa88be9
    role: context
  - path: pages/traits/genomics/aristaios_system.html
    sha256: 33432065d35ba4a25d5062e6d26fd2406fff0aff56d20df99a6a66bf30c20395
    role: context
  - path: pages/traits/genomics/armada_system.html
    sha256: 81e56033e648219682f1c9236f46555734e9ca710cf463759789315659d2333a
    role: context
  - path: pages/traits/genomics/audmula_system.html
    sha256: 62e93e25ee07ecb284551ca55d327873cead9ea2151a91129049bed8abca9917
    role: context
  - path: pages/traits/genomics/avast_system.html
    sha256: c02a07ffec5b203977171986f6a494e124cb409012933685020cc03f969010cb
    role: context
  - path: pages/traits/genomics/avs_i_system.html
    sha256: c3e44194c9325a0549794cb0ae478aed573d4aab3a26774b972cb8c6fa8be692
    role: context
  - path: pages/traits/genomics/avs_ii_system.html
    sha256: d9312b41aef1035c2553373a5fdb982bbf3cf8d39b5bf7b4174af1ae9694215f
    role: context
  - path: pages/traits/genomics/avs_iii_system.html
    sha256: 9e4a7946ed3517744f5bf44d170f39290299e7e57dc7a08dba9d7860f3c44592
    role: context
  - path: pages/traits/genomics/avs_iv_system.html
    sha256: e0c371302a601c256fa0e775a7b9295e5f7ed09827841f577db736984de6eb5b
    role: context
  - path: pages/traits/genomics/avs_v_system.html
    sha256: 803f54278bead115abd73c4ea4234290aefa809e1e31a828f0f092c0225b5277
    role: context
  - path: pages/traits/genomics/azaca_system.html
    sha256: 793b7a356b00af972d03894d902e381fff7650510b080c2d91a12a64ea702104
    role: context
  - path: pages/traits/genomics/belenos_system.html
    sha256: 407bed17c64952748df0607f2755b461426002106e299d27d1b4de4fa315cab9
    role: context
  - path: pages/traits/genomics/belisama_system.html
    sha256: d985f833b3428b1bae6237920904633a10fb1c555446d08924052a1e79ab7504
    role: context
  - path: pages/traits/genomics/bil_system.html
    sha256: e043718fc6ac39c2b7bddbe505deb32efeee0a1e64834195f34bf1406244ac7f
    role: context
  - path: pages/traits/genomics/borvo_system.html
    sha256: 1dd7bce008a8a9a77219ae63b69fb30d89b2f0c5581a5bc1202100375f0b23b3
    role: context
  - path: pages/traits/genomics/brc113_system.html
    sha256: e4ac6e0a2060615520d4be143336fb2f941ce6ce1011a43ce95e6fe4aa6851d9
    role: context
  - path: pages/traits/genomics/brc142_system.html
    sha256: 24625cad160ff98ee55ef0e4ed8cd11dd3a9f6ef4eb9ac349864697620e558c3
    role: context
  - path: pages/traits/genomics/brc167_system.html
    sha256: e5e55b94a8700b6cb1b51bf09cc1d5aac6e221ee402a2f5ebd479b168691a2be
    role: context
  - path: pages/traits/genomics/brc217_system.html
    sha256: 65526f81b0b2572c7afc0d1e8e329a4c1d770aecf1e02c0fca055e52f8a7add0
    role: context
  - path: pages/traits/genomics/brc22_system.html
    sha256: 0e397444beb4d87e961c53c3585f20affd54f1ddf02128f2d7040dfcc7fd8309
    role: context
  - path: pages/traits/genomics/brc233_system.html
    sha256: 4977acf34bcc947c89c70f96edfd08a722ebf2c16077c8937019c593a42c9bd6
    role: context
  - path: pages/traits/genomics/brc23_system.html
    sha256: e18c6e0541fd2894d038b2661621863f84ffa8d3078e10ee57de870a909722e6
    role: context
  - path: pages/traits/genomics/brc24_system.html
    sha256: 2aca1b1d864d2b8e07ca0ab9e6ef3eca8d0fd4df79a6bf57d896fd863bd65f08
    role: context
  - path: pages/traits/genomics/brc59_system.html
    sha256: 4a521ef9ef6b60c182566d881e7bcaaa5694968c1f7ab9e684eb3febf066e36c
    role: context
  - path: pages/traits/genomics/brc76_system.html
    sha256: 8b890cb4571475abaf9aca74f175761443d9f8e91372062d808c1c9614ba196a
    role: context
  - path: pages/traits/genomics/brcwgs21_system.html
    sha256: 4c46e95e7ee502149767338aa4c8bbffa0da913c0d9abccce29e8787f8db766a
    role: context
  - path: pages/traits/genomics/brex_system.html
    sha256: aecea235db6285d915c834fdef12825860cad115b0c2109bfb241553abb4140f
    role: context
  - path: pages/traits/genomics/brig1_system.html
    sha256: 738cf9544af3d21da5f9ff50b78c994b6c01669e1cbd5b741f234048e35cf701
    role: context
  - path: pages/traits/genomics/brigantia_system.html
    sha256: 21a7e1bb29480d8824192b5a8a057f44547f313f8fc0555154ec2dc3931c62d9
    role: context
  - path: pages/traits/genomics/bsta_system.html
    sha256: 018edd147615e1993968f987ef960f0f382fa275d8d00e448f9530c3bfb74b86
    role: context
  - path: pages/traits/genomics/bunzi_system.html
    sha256: c0d7fa3afe65b5913d1636a19d729d8d3bac85e56b6cd320227c130478a4dc73
    role: context
  - path: pages/traits/genomics/butters_gp30_gp31_system.html
    sha256: 7d6d51ebc4b7056bfd0131ab6c449d5a2ce78c2689daddea1b940501f18d40b7
    role: context
  - path: pages/traits/genomics/butters_gp57r_system.html
    sha256: 072fc92eb4245341a4dfb43c2ce5fd4dae0e5c68eefbca6edce131aec7db2af9
    role: context
  - path: pages/traits/genomics/caprel_system.html
    sha256: f4793fbf19ae730a0d2d07ae02235cd2f88fef237b29a509a0e7eccd4ae7c8b9
    role: context
  - path: pages/traits/genomics/card_nlr_endonuclease_system.html
    sha256: 77bfbd84f9447d14f7eda8ea902962cc72ec6e8cb405615fee62a599de5b279f
    role: context
  - path: pages/traits/genomics/card_nlr_gasdermin_system.html
    sha256: a0943ec8a5be5e44d469ace0258e1d18cb0e9a730f7921c70718d92806d20a14
    role: context
  - path: pages/traits/genomics/card_nlr_like_system.html
    sha256: eda65df5eff095aba90c999cf56eeb568d10625e3d3fa67c25ab32dfcea3ae35
    role: context
  - path: pages/traits/genomics/card_nlr_phospho_system.html
    sha256: 54adccfc0839638138e8120e29905448f28d1ab5af1d0f8fab144cdb45f157ff
    role: context
  - path: pages/traits/genomics/card_nlr_subtilase_system.html
    sha256: 790d5dbf1a6e77beef9fed0bd0379bb07afebd45f6bbddd1e382fece8d4c20d0
    role: context
  - path: pages/traits/genomics/card_nlr_system.html
    sha256: 718e938c456c2fbedc47541267a2dccd2824e3dabc0a63c1b58d7b99ea534c11
    role: context
  - path: pages/traits/genomics/cbass_system.html
    sha256: fa661d061151671336b0c8c142d9dc22326d00ecb276a8377c4bf469aebc3c08
    role: context
  - path: pages/traits/genomics/ceres_system.html
    sha256: f850ea1dd855dbe45b9b9b7efe391bc342c4cd937b1e4e941bd970ceb17d2a36
    role: context
  - path: pages/traits/genomics/cernunnos_system.html
    sha256: 61af1912e0d3259bc506d2e2a457e53a8951a917de9f7e49e663cf4c8985fac3
    role: context
  - path: pages/traits/genomics/charlie_gp32_system.html
    sha256: d0783e9fa03bcb8f7d802d4b933d1e12e33b1f23cfec96212627b228f559f1fb
    role: context
  - path: pages/traits/genomics/clover_system.html
    sha256: 0a26f673fc40a837622dba6e80316c2afd6e8e899f4d629950a2a040aa5117ca
    role: context
  - path: pages/traits/genomics/cmdtac_system.html
    sha256: d22996c6e253e00ba26c798d1ee961bb63889f8efe0e5536a074a61bc179b368
    role: context
  - path: pages/traits/genomics/coconut_system.html
    sha256: 4884a1063a5fb3d5e154509e06f25c7db9c70519555d51dcf2d8f65ec127a3e4
    role: context
  - path: pages/traits/genomics/codon_usage_bias.html
    sha256: 5fc670683c5787e6430d1e2315fa5e92df85628000ecd19bc9e12c8757d880d9
    role: context
  - path: pages/traits/genomics/crispr_cas_system.html
    sha256: 9a2473a1f5904753352f4586caba8feebbacc401656ebbbf86de3e8e4b4e70ec
    role: context
  - path: pages/traits/genomics/crouga_system.html
    sha256: 5ad21730ac4ebf5aeec3daf7110c1b4224665562eb45b4110fbe313ea34c87be
    role: context
  - path: pages/traits/genomics/dag_system.html
    sha256: 12c826787e3dc8f70931626651fa6ca2f400d4aa75634549b0c6c802ad02d363
    role: context
  - path: pages/traits/genomics/damona_system.html
    sha256: ecbbf19e6a57dd14b840d7ecbeb390cf3f614c4d82e3cbd52b35034f58c01a0b
    role: context
  - path: pages/traits/genomics/darna_system.html
    sha256: 79c1c70981f1d048e71d6d93255818dec715ffad31b94a7879a645650e1f3daa
    role: context
  - path: pages/traits/genomics/dartg_system.html
    sha256: c6acaac73dfb5919802b801c26fe048f1d4ceaa32ac2802412c489385d39a8d6
    role: context
  - path: pages/traits/genomics/dazbog_system.html
    sha256: a44f8c99a5a48254231b28a1fb2287ed8879a14cbf5f2860d13663a98e487bb1
    role: context
  - path: pages/traits/genomics/dctpdeaminase_system.html
    sha256: 1a43058256f1286e46d485d3ed96bbcb6555951a0869e0aa96d84de72331f419
    role: context
  - path: pages/traits/genomics/ddmde_system.html
    sha256: 418ab3457ada126d2c42cea7aeb662d078b2f88422ec8bd3e247523f64b22481
    role: context
  - path: pages/traits/genomics/detocs_system.html
    sha256: 578d08363d66fe6c3bdd44c023b70a2f78e0cb6ab24fe0262b0b93a19cee4fc0
    role: context
  - path: pages/traits/genomics/dgtpase_system.html
    sha256: 84cd5b18a4c5fba14411a6555c2f9211753079824d82280f85f4b2b9d41d6b53
    role: context
  - path: pages/traits/genomics/dionysus_system.html
    sha256: 07da37bd1062a70e9fc5860d211512c9c3eb0bdc01bc9e16330b96559c20cff8
    role: context
  - path: pages/traits/genomics/disarm1_system.html
    sha256: ae924d11751bb43bb9af225ec14456889bdda9ebab6f7df60565c16c107c6baf
    role: context
  - path: pages/traits/genomics/disarm2_system.html
    sha256: 74066c707bc5781ab65ff45da714488d466d2b6a1359b0120809634b377835f4
    role: context
  - path: pages/traits/genomics/disarm_system.html
    sha256: 2e720f57e023de62a40f262fe543eb9f4ed00cd92827fe51af9d162d44a16e84
    role: context
  - path: pages/traits/genomics/divona_system.html
    sha256: dc6308adad6278c6f79fd21d8593a9705ccd5583defdbbaef0d317741ce094a6
    role: context
  - path: pages/traits/genomics/dnd_system.html
    sha256: fa9af2ebdd9d7540c0950671e9a204e4497401eacfbe6b3b1c61203ff65c758f
    role: context
  - path: pages/traits/genomics/dndcdea_pbeabcd_system.html
    sha256: 99f680ae067d51416e897765afc311ba3a5664cac9310f8fd6a3e0e869fef938
    role: context
  - path: pages/traits/genomics/dodola_system.html
    sha256: c146c4adb26a8e94fa8c4b4dadbcbd462d17d98c07305ac7f398c4a2f9e5e0c6
    role: context
  - path: pages/traits/genomics/dpd_system.html
    sha256: 2a79ad7a520529dcac7ff6cc91f9d5b18f370f148c6de7b0e25533a20caf42b8
    role: context
  - path: pages/traits/genomics/drt1_system.html
    sha256: 8a0de5a0bd2a596bc4c1a472e36e3275449e6d1fe2ecedf62a9eeff51f8482e2
    role: context
  - path: pages/traits/genomics/drt2_system.html
    sha256: e1480d9a2a479162a26f7ba910c1d3f73f5452c80da1ab8af956eeb80e78abc3
    role: context
  - path: pages/traits/genomics/drt3_system.html
    sha256: 8af5fe90499fce959b1c9358f68f02a3850e24ca618337ecfc28f53c7182348a
    role: context
  - path: pages/traits/genomics/drt4_system.html
    sha256: 03452b7d1b9fcd4c45dacf885e1fc582807c88ed703b6d59160837b90bc5b38d
    role: context
  - path: pages/traits/genomics/drt5_system.html
    sha256: a479b8c88607e3cf44ddeba748cb7478f5465acbc9a8272747e946b928bde7e4
    role: context
  - path: pages/traits/genomics/drt6_system.html
    sha256: d5c4a44f992329a8baad312932a945a215fc6e0ff3ba4319422c10a990dbb3a3
    role: context
  - path: pages/traits/genomics/drt7_system.html
    sha256: 88f2411ce0e372f9563913d338ab3ca756292e54d7caa4c0760b6c2bcf89886a
    role: context
  - path: pages/traits/genomics/drt8_system.html
    sha256: 5cca87768dc986842febc05688620217b3057fd8cfc68bf21befc41291173453
    role: context
  - path: pages/traits/genomics/drt9_system.html
    sha256: 5e5de232d9942e5ce401da0a7b54b6724076fba18e387b81f42710dfe5c6834d
    role: context
  - path: pages/traits/genomics/drt_system.html
    sha256: fee56a7a9612710c15ce323c755aece42ba818e32ee69125bb314e3a03a06e74
    role: context
  - path: pages/traits/genomics/druantia_iii_system.html
    sha256: f8c7a6e146a2049aa66f09631f0f630bc016fb60659eb837261ae641ca77020c
    role: context
  - path: pages/traits/genomics/druantia_system.html
    sha256: 22b2b398d39373cc4985ccfd5200d5d1a93be96f851ab332ea3d9c9ced3a19b0
    role: context
  - path: pages/traits/genomics/druantia_type_i_system.html
    sha256: 6a5ec186f26a2bcdce660070642c6d87e03c754aad4d90dfd1d4d4f43e832ee1
    role: context
  - path: pages/traits/genomics/druantia_type_ii_system.html
    sha256: 5c3e5e4e87fb528be1a695e97d2210935b937365c22f00c68bf197df3fbaa9e7
    role: context
  - path: pages/traits/genomics/druantia_type_iv_system.html
    sha256: fed7e0567421153216c315a8f0e2a666e22e84a8e7487ddbe2758fb6bd212ef9
    role: context
  - path: pages/traits/genomics/ds_10_system.html
    sha256: 34b2932f8bbdc5b7e2f74f8bbdbf08abae78d5261681cea25f1c560de6943d42
    role: context
  - path: pages/traits/genomics/ds_11_system.html
    sha256: 245825bf8a3e49cf13018767235fc6c73cc5050870ad3b89f0b8b44aff80dc0d
    role: context
  - path: pages/traits/genomics/ds_12_system.html
    sha256: 0455e047b067809e698ae8ae09cd42231f9ac18c2c2273faec5640bc8fbd63cf
    role: context
  - path: pages/traits/genomics/ds_13_system.html
    sha256: c90e118bb60b98575365b00c7237e03e3b69c0b39c22a0d74ec12e807ef9a5b7
    role: context
  - path: pages/traits/genomics/ds_14_system.html
    sha256: 4676c5dc5e6357d7db1188586b149d660026ab98eaf8e7b04693655f924b8494
    role: context
  - path: pages/traits/genomics/ds_15_system.html
    sha256: b59b1610dd512196251295bc0d49a235c59fc49a17c3d213ddbcd0d897c564b1
    role: context
  - path: pages/traits/genomics/ds_16_system.html
    sha256: 6592eff2a9f8b0a0cb76891ef8636c84edb34e3a7615abdc846a62969cc888a6
    role: context
  - path: pages/traits/genomics/ds_17_system.html
    sha256: 9b105acf80e3d8ab2121a1aced41d982453a06bf41cf06de7ec6b6e663613a6b
    role: context
  - path: pages/traits/genomics/ds_18_system.html
    sha256: e1adeba788da7813ee7db1a991b693fe5a34f0e60773ffdb7d9ed38fc34de5f2
    role: context
  - path: pages/traits/genomics/ds_19_system.html
    sha256: 1ebc78798d277cff2eba6cb0cc026b511b6c45918293d756581a5e857dfa3b9d
    role: context
  - path: pages/traits/genomics/ds_1_system.html
    sha256: 68241b8fe16ad8e3d1aedcfe784eb366434fea0f7ac9b5832db545d8ecc47ca8
    role: context
  - path: pages/traits/genomics/ds_20_system.html
    sha256: 794c161ca94a9036f747b8c66c01b7c6a394e9579cd0c4e33521f44b147b2786
    role: context
  - path: pages/traits/genomics/ds_21_system.html
    sha256: 7e677e3fa9b1bfc21fef1f02c3e816702e992c82dde780ddd08f005c85f037b5
    role: context
  - path: pages/traits/genomics/ds_22_system.html
    sha256: 251e50200838037da64318faab98cc5918d1765208b65a4f9bf453fcbc8e6518
    role: context
  - path: pages/traits/genomics/ds_23_system.html
    sha256: 5b8373c0794481dd49fe9f1a03921c2c90c535aa11474147c2e60ab1f8b9a227
    role: context
  - path: pages/traits/genomics/ds_24_system.html
    sha256: f7651ebeaf2cf3b77ae75986878ebf04d66c52ae0ea8df9be6ec45b612d04be1
    role: context
  - path: pages/traits/genomics/ds_25_system.html
    sha256: acd99a8c7563df95009de48c7996eb372d28e890726bcba462005dd27f8b8fa0
    role: context
  - path: pages/traits/genomics/ds_26_system.html
    sha256: 013372852aa519032c1c535fc84a9363da6228d435b6b380ed88a739eaeb3309
    role: context
  - path: pages/traits/genomics/ds_27_system.html
    sha256: d86418a7ebaf49badb7b007357c1f0604b0f90805701262892ba039d5edcf6d8
    role: context
  - path: pages/traits/genomics/ds_28_system.html
    sha256: 786bca3d1a2cefc5ec984b0f67f02cc3c944c802658c90b3e52381de8548ec0e
    role: context
  - path: pages/traits/genomics/ds_29_system.html
    sha256: 3a8dd770a0ec752a7aadd731ad13efef27faf23473cd0cc411ae57673116444f
    role: context
  - path: pages/traits/genomics/ds_2_system.html
    sha256: fbc5297c035537e15792296c3c59cca8a9b9b5fbee0ac482f852b01c7c5d33f4
    role: context
  - path: pages/traits/genomics/ds_30_system.html
    sha256: ba71e13f8ea4059d949a655637a66d3d766e6373902879241883de1d4c35a2c4
    role: context
  - path: pages/traits/genomics/ds_31_system.html
    sha256: 4fecaef7eab44fdc86bff100b3beb6da557aa2b6a5968de2eff811af90e3b27a
    role: context
  - path: pages/traits/genomics/ds_32_system.html
    sha256: c72f37bac43700a01ceec324fc87c38717a7f02b8612633d695d1d4e6f3e8968
    role: context
  - path: pages/traits/genomics/ds_33_system.html
    sha256: 981f095ba5739ff2ddc910aa9ab8485a1fcf01c0854378b230031cc05a3e4944
    role: context
  - path: pages/traits/genomics/ds_34_system.html
    sha256: f55fd3e6121421c81502ba50a51bfd160cbd3c3c2a1fefb9e108eda2dda23dab
    role: context
  - path: pages/traits/genomics/ds_35_system.html
    sha256: 5cc33ed4fa57a8d57a1d4914a0b6b9407bdfe9e41e71d8447a5d5ecf80a5c77d
    role: context
  - path: pages/traits/genomics/ds_36_system.html
    sha256: a35b39b044f8126a454acbe46e5af8f1e64072a21d4004dfc2c8419fcc63f18d
    role: context
  - path: pages/traits/genomics/ds_37_system.html
    sha256: a498f68fd4c0cabc6bfa2eed2a2e5ea1f9b48ad418d27bbd646599e1998b2a67
    role: context
  - path: pages/traits/genomics/ds_38_system.html
    sha256: a6e7f162068c0d61d52ad00022ee5f2cc71312e6a0df75b7ecc3943bf6694d00
    role: context
  - path: pages/traits/genomics/ds_39_system.html
    sha256: 1704e4fdbad2fd3dfe69c9f636d87183f9ffbca91ebb1791571614b4dbd3b705
    role: context
  - path: pages/traits/genomics/ds_3_system.html
    sha256: b3c498b88a2c6d91d80ecdfab32c907183ca640817f489b3bbb090ddcbcfcb82
    role: context
  - path: pages/traits/genomics/ds_40_system.html
    sha256: df766c05a5deeadcb68bf745107f45c1ba9b3eafb41ac36ffd203f0217f7b045
    role: context
  - path: pages/traits/genomics/ds_41_system.html
    sha256: 6f647e7955c680ef2a2ba8cab4c8370425363ef2172c049581afdcacf7c0fc37
    role: context
  - path: pages/traits/genomics/ds_42_system.html
    sha256: 90ef62f782b76641dfc71bcf4b6f2092a581342d4a41bcdab2948935b4099461
    role: context
  - path: pages/traits/genomics/ds_43_system.html
    sha256: 2de93a0c48600d0d1e33a23edb8a3534c1f5030d5b42355a1976b931ff5d8219
    role: context
  - path: pages/traits/genomics/ds_44_system.html
    sha256: 70d8c4b7755a8d55aafa61a4bce66d2eb02f79a3942b53b30ef1ba3bdd5543c8
    role: context
  - path: pages/traits/genomics/ds_45_system.html
    sha256: 7f1739299df3de6aea2b14319a5991094911b2f16e79e8265aeb673762687856
    role: context
  - path: pages/traits/genomics/ds_46_system.html
    sha256: 3bc66619c72ce6ab81ad90af6754d1c23a36abb15b16701d308167bdebfcf9aa
    role: context
  - path: pages/traits/genomics/ds_4_system.html
    sha256: 2a82c24f7ab119b457b6cb3478db8acd3cb756734b441d3583c1a11bc34dc8f3
    role: context
  - path: pages/traits/genomics/ds_5_system.html
    sha256: 7129e62c9313f8917716fa06881a175afea501e4298192e89e1ad5719451f14b
    role: context
  - path: pages/traits/genomics/ds_6_system.html
    sha256: e552358ac13af5337614f0bd70ec38cf050b3bff30650ed7af7edc72d152c38e
    role: context
  - path: pages/traits/genomics/ds_7_system.html
    sha256: bcf5bdd3d026faed941141b11aaf01e3bf6d2eadf3b738afef32803f5ed795e3
    role: context
  - path: pages/traits/genomics/ds_8_system.html
    sha256: 6af4ad163100307f8f15c057c8967fb0370ed6525c2946cdc876381be77df107
    role: context
  - path: pages/traits/genomics/ds_9_system.html
    sha256: 6fc9416bf0d5b59f60f294f35c2eb27ec28bea9c3698e1988045c27d61f82ea5
    role: context
  - path: pages/traits/genomics/dsr_system.html
    sha256: 7b7284d0c87c5d5bafd0c7c862cdc31815486be7bcf06e4b53de0eee8c035a46
    role: context
  - path: pages/traits/genomics/duf262_schlafen_system.html
    sha256: 3154e6247468b94bcf913927f1b89590042b75d6a2d36fd6d3e333c4c4361b3a
    role: context
  - path: pages/traits/genomics/ecokmcra_system.html
    sha256: e9f79bf272a2d4dfe8e18a63822aef13a16414e2ed4b19e14bde431a47551eb3
    role: context
  - path: pages/traits/genomics/eleos_system.html
    sha256: cad195c5b699c3787bc43f75260e54e96e84bfbdcadf7a173532e271f580c569
    role: context
  - path: pages/traits/genomics/endpacf1_system.html
    sha256: 5aa6647641e1b86b16166aa5ced32250c089bf537d2b419eb25f164c19fc586a
    role: context
  - path: pages/traits/genomics/epona_system.html
    sha256: e8d83b7db24092ae66a3d402c1a65ee69c1fc036c2a62d49bfbb9b1d5a5b6908
    role: context
  - path: pages/traits/genomics/erebus_system.html
    sha256: 94f621ca0048871de529d207eaa9bea0a6d8d5ec2ca0d9c6019ed8ccc7db74cb
    role: context
  - path: pages/traits/genomics/esos_system.html
    sha256: 8e8aaa1c4862471647d15294a34e415ca052d7210bffb4834abfdbeb4ec194fc
    role: context
  - path: pages/traits/genomics/fliodhais_system.html
    sha256: 9e5e4e9a5d60bae94bd65c1ff08e1325352596979ab2923f2d4a9d8c2bbc4965
    role: context
  - path: pages/traits/genomics/fs_giy_yig_system.html
    sha256: 948b97ac638304093fd9c6cad451360a7a2673c0699eb88913bbef1a4a9c8ce7
    role: context
  - path: pages/traits/genomics/fs_hepn_tm_system.html
    sha256: 70a400e8f0354f522f6b0c9af3f873ac7b9a90def1b5a3a31cf0659146df7905
    role: context
  - path: pages/traits/genomics/fs_hp_sdh_sah_system.html
    sha256: c7a8afb75908990e79b0f6d934be7db8bcccb4467fe6e42317c5be7a944b0c9b
    role: context
  - path: pages/traits/genomics/fs_hp_system.html
    sha256: e4863c6f16d0e541dc2302bcec2fd3b7168e0c25bba4919b5a89d63b294bc9c2
    role: context
  - path: pages/traits/genomics/fs_hsdr_like_system.html
    sha256: 354f965d800968c9fa1a17891f640b89a8cad1d62bb876a32698fafb3c76b839
    role: context
  - path: pages/traits/genomics/fs_sma_system.html
    sha256: c1644524cd50db170c7afccf81bfa27d00aceba4f4e564c1eaec0621ee32f3dc
    role: context
  - path: pages/traits/genomics/gabija_system.html
    sha256: 7f0195975ac41b752f06febf01d991c9852bd0d55662828522cf6bcb36005b0a
    role: context
  - path: pages/traits/genomics/gao_ape_system.html
    sha256: ee18d96bb52c200fa57f84cafbf861c0602a4f560f32ffc4117c3a39292c778e
    role: context
  - path: pages/traits/genomics/gao_her_duf_system.html
    sha256: 2040cf01106dd47c143cdf7f9d767739094091232039ff52e7c54224255bd066
    role: context
  - path: pages/traits/genomics/gao_her_sir_system.html
    sha256: 0564c95a43ea6454dd090aafc6e53872fe0926053948510c57d4ae2e6ec48c50
    role: context
  - path: pages/traits/genomics/gao_her_system.html
    sha256: 9899c956fd477df4b353b8b22d112983f5334c564df037c301d177ad685fbe29
    role: context
  - path: pages/traits/genomics/gao_hhe_system.html
    sha256: 52943aa0d2f8b45be027bd6e0b4e14a26a31d2d40e1286dabc9f131e3734574b
    role: context
  - path: pages/traits/genomics/gao_iet_system.html
    sha256: dff4d02ccfa569a1af80ed1ed98636a2de4c0f8fcc76312aceb9ac0541ba20c3
    role: context
  - path: pages/traits/genomics/gao_mza_system.html
    sha256: 848948ad1766ae66c31dc5dffe850d78f63dbb0876b69e7e2206f4d7842daeef
    role: context
  - path: pages/traits/genomics/gao_ppl_system.html
    sha256: bd7fb6911c5e0bcdc0591f0b7807396d4365ecb3f0fd97911cb686aaa1a5e000
    role: context
  - path: pages/traits/genomics/gao_qat_system.html
    sha256: 82502df5c5b4d7fa7c36ce3e0233c76df22aba09e0b44fe0b88e332f00f18bb8
    role: context
  - path: pages/traits/genomics/gao_rl_system.html
    sha256: f4fa81a01c171dbc324d4a078c71a6210ab5cc1d4ce63832432cfb5a464212be
    role: context
  - path: pages/traits/genomics/gao_tery_system.html
    sha256: 65e1e7950d4e152b62887144f96059cd7a294d0aaf0cbb36e85c663867d30339
    role: context
  - path: pages/traits/genomics/gao_tmn_system.html
    sha256: a02b1311930252a07c77082915a5305e0d5c3f3f082415d01ec6cc0131968e11
    role: context
  - path: pages/traits/genomics/gao_upx_system.html
    sha256: 380164964378f24ccc0d4425361d4e359390bdcf44fd79c2de87f5ae3453f3a5
    role: context
  - path: pages/traits/genomics/gaps1_system.html
    sha256: 888937da20ea43361d027d883300112f20ebaaa4d7171bacfbbbcbb5fe95b346
    role: context
  - path: pages/traits/genomics/gaps2_system.html
    sha256: fe9d6952a1a160bd864da1e7d20f6360dc1dd6b205a4d62a24bc8b2dbeafde83
    role: context
  - path: pages/traits/genomics/gaps4_system.html
    sha256: 1bc87ab56f01ca290a2811596c98a48c83d99b7602e62b20a32378974095aca0
    role: context
  - path: pages/traits/genomics/gaps6_system.html
    sha256: a2e0b24ff32cc81fb6ad4f46e067c79812c57f27d067ca2da53ba5eeaff9d628
    role: context
  - path: pages/traits/genomics/gasdermin_system.html
    sha256: fb94a7ed2d9cb5d79f5f5232d3f9dd35edf4f971138554447b6e8765572c905a
    role: context
  - path: pages/traits/genomics/gc_content.html
    sha256: b62c86442faa5847a7c708ef57710ebf9bb005523dcfc4b63bee4f3fcade2acf
    role: context
  - path: pages/traits/genomics/gc_high.html
    sha256: fd9e8e79ce8a8e21ed86569756f1f5883d62fec6d8f08952dc1f2028bb6c29f9
    role: context
  - path: pages/traits/genomics/gc_low.html
    sha256: ee803ee866a7c02cbff19b41960e7b1ced14abecaea4dcbdcdcecd7ea369ac24
    role: context
  - path: pages/traits/genomics/gc_mid1.html
    sha256: 3746edd3143facfbafe1c84c1bb61ab5a8ce91021952f262e1ab8c9a744990f4
    role: context
  - path: pages/traits/genomics/gc_mid2.html
    sha256: 67feb6ebd415a0e8a15091bc767fe78010c5ce9601bffa5191251eb3aab33423
    role: context
  - path: pages/traits/genomics/gc_skew.html
    sha256: ee5a98acc8a27932eff23fb09fd81f2b12e634fa43d575734d93b0a141bb053f
    role: context
  - path: pages/traits/genomics/geb_system.html
    sha256: 2ad11d4a9842b56490e48739df954b4f11f4f8b1bd57d93f413e3edb202d9e74
    role: context
  - path: pages/traits/genomics/genome_size.html
    sha256: c5ea593a930cd25cb15fe42ec36caaf806383ef71c1858c5fe9c4bfad3ac3305
    role: context
  - path: pages/traits/genomics/genome_streamlining.html
    sha256: c6dcefc7795fc075f795ade7b4c5c540ca81056ddaf0055ea3907b955ecc277a
    role: context
  - path: pages/traits/genomics/genomic_island.html
    sha256: ada0ad14f5cb4b88bc5c4f8817d21f29ec45c7a9f35e2a7bd08ad5385c28bd5b
    role: context
  - path: pages/traits/genomics/gmrsd_system.html
    sha256: 7c5f3b93d35a0d9b06429f1db69744a770d98a2fec300c058871dddbd79447bd
    role: context
  - path: pages/traits/genomics/hachiman_system.html
    sha256: 92c50704435fd87452611f0e02083944c9655c0d6f29766f978df2994a0a1598
    role: context
  - path: pages/traits/genomics/hachiman_type_i_system.html
    sha256: d9c23c8bd13c81120b7880b2b29e3e4bc0993fd0bb2939de92388ba630bcd650
    role: context
  - path: pages/traits/genomics/hachiman_type_ii_system.html
    sha256: 824848b15870a7e850078fea5e71bfc0c61c30ee4f7cdfbac1da5153918d4f81
    role: context
  - path: pages/traits/genomics/hailong_system.html
    sha256: 1022d0e28adb0bd5e35840a6a99628ee5b97bafbdcb75205ce3dd8ec452eca1f
    role: context
  - path: pages/traits/genomics/hec_02_system.html
    sha256: a446e5f8d405913a93d5f46daf5afd281eb256061a2d5c598add91aeb8425700
    role: context
  - path: pages/traits/genomics/hec_03_system.html
    sha256: f22ad326f79b0d81ddfd11dca6001140158b55fb1d2ce0049f677b8053e88e57
    role: context
  - path: pages/traits/genomics/hec_04_system.html
    sha256: de1d32500c1143f82426bcee536df84d6f43dbdd63e327888990e7c990fd070a
    role: context
  - path: pages/traits/genomics/hec_05_system.html
    sha256: 6ae3a779c0cbd30ad9748fcfc93cb2edd4ac9589da9f0a0197f92ae5d23bf6af
    role: context
  - path: pages/traits/genomics/hec_06_system.html
    sha256: 95a16392309004a9ed40346ba97205f5d5cf1e3e34388e10420d3822d54bd16e
    role: context
  - path: pages/traits/genomics/hec_07_system.html
    sha256: fcd8a84103cefd004ad4e191137436df840b1596ec71e3394b07c913c11d2aa0
    role: context
  - path: pages/traits/genomics/hec_08_system.html
    sha256: 88f4ce1d883be3f7f46e6a59ad07b2f703bc6d90f7dae94b29dda462f988e664
    role: context
  - path: pages/traits/genomics/hesat_system.html
    sha256: 9907454fab5ae3460d104c8d07de75255fcc70d0e79443cc34457ed76fb41f4a
    role: context
  - path: pages/traits/genomics/heterokaryosis.html
    sha256: 1066d7fe0c81e47cb6f8b43217b2a807fb42cac72bc1e34e34c95ae07822633d
    role: context
  - path: pages/traits/genomics/hma_system.html
    sha256: 8919a68e193d5daa319cdafa0a10a2cebb6ba6812e0b080cd496106183613ed2
    role: context
  - path: pages/traits/genomics/hna_system.html
    sha256: f8eae98d4c4fb4feebe0dcdcf3a86c9c1a0b9be75eecf22901fbba4c16b8f0b2
    role: context
  - path: pages/traits/genomics/hypnos_system.html
    sha256: c7f4c0e7e9890c31374b9a5ebd4e3dd5bdfc6ec7be98a01aa93a482cd161067c
    role: context
  - path: pages/traits/genomics/ig_like_schlafen_system.html
    sha256: 85c649a18e2ae4745d175ca6f40e538b60c1c64faeea29eaecbbc67bb1409082
    role: context
  - path: pages/traits/genomics/integrative_conjugative_element.html
    sha256: 526febb56a115f60708bca8efa9818c34add5cf41fcfae86b46d3d7ba5c5b815
    role: context
  - path: pages/traits/genomics/jukab_system.html
    sha256: b60aa4f4a6d8c48bd2a78436727680eb2b2dc0adba5bb25880ffa7726f9bb64b
    role: context
  - path: pages/traits/genomics/kamadhenu_system.html
    sha256: 0c86483f06f9471dcb0415d5d46c403b6b035ae4f369243206d0f59b88e74912
    role: context
  - path: pages/traits/genomics/kiwa_system.html
    sha256: a85e2aa7b08c288a41962633693aa5367051ed52830be0e1bfe057e6124b4427
    role: context
  - path: pages/traits/genomics/kongming_system.html
    sha256: 4ed47a7c2f4a26f5032e90cd7d7ee32539a27050fddb6292ba167a47c4f415c4
    role: context
  - path: pages/traits/genomics/lamassu_amidase_system.html
    sha256: 1d0911fde6686fd17fe81b4493a513ad3c488d861a44958bcfff0cb1d764484f
    role: context
  - path: pages/traits/genomics/lamassu_cap4_nuclease_system.html
    sha256: 75c179c97a062347a545862959a3911d2022289682907570b2f8c6f6c4834909
    role: context
  - path: pages/traits/genomics/lamassu_fmo_system.html
    sha256: b03c2e59ab6a0c4b0f440af671a380da3a581a9ca5c2fe1ff73d1af9b023dedc
    role: context
  - path: pages/traits/genomics/lamassu_hnh_system.html
    sha256: 6d0f363b40a14fc66881cc069f0f792106bfd28d201ecc1b86c89aacd558aef6
    role: context
  - path: pages/traits/genomics/lamassu_hydrolase_protease_system.html
    sha256: 5afc5f8313d022f2fa6e1dd67055714f64ba3c31d0468e6b84b174ba8813ddc0
    role: context
  - path: pages/traits/genomics/lamassu_hydrolase_system.html
    sha256: dd0280974ba18290781ebc1a8347d9b8dfacb0ff7ab117d6c897b74b544402c9
    role: context
  - path: pages/traits/genomics/lamassu_lipase_system.html
    sha256: 337492ff0ef4a03fe0dd7733f9c9cc4978bcd6a883a0fdf5cc5a066869726ed2
    role: context
  - path: pages/traits/genomics/lamassu_mrr_system.html
    sha256: 611d4c93b70cb2baf90de20b45cf078af4fddb364dee9dfef82d47a08ff4754b
    role: context
  - path: pages/traits/genomics/lamassu_pddexk_system.html
    sha256: 127658cb680ad682aea28b110d167572706ddeece49ec1633cf7d3dcb5595255
    role: context
  - path: pages/traits/genomics/lamassu_protease_system.html
    sha256: 2f82a4b57a439840c3424d71c4da206f5bb060b1a56be0ecff5cba8797279a19
    role: context
  - path: pages/traits/genomics/lamassu_sir2_system.html
    sha256: d7fc4237a38959afa83c6f2140fefe9eda10c1117b4f05453791fea4e5b16d71
    role: context
  - path: pages/traits/genomics/lamassu_smek_system.html
    sha256: 8692ac5877dbbd990a286118c1d573e71a4f3b0243f4da1d17ce7884d098a334
    role: context
  - path: pages/traits/genomics/lamassu_system.html
    sha256: 60186223d55489f3baa33d2bd9d98639f22f0a0f82d46b3d0160dee95c641ca8
    role: context
  - path: pages/traits/genomics/lamassu_type_i_system.html
    sha256: ac5ab22a76232b7360e06b244d73bfc713299bfa88820925c1c3b6824ab0d8c7
    role: context
  - path: pages/traits/genomics/lamassu_type_ii_system.html
    sha256: 4331aa111ddb5edd994aa02e578b4cd03fd8fbce76810a4d41a7d70751eb453c
    role: context
  - path: pages/traits/genomics/lanthivirin_system.html
    sha256: fda494856fdaaa3f650702156ce73a581eeaa6a1722ccf19040e12e332375bc9
    role: context
  - path: pages/traits/genomics/lit_system.html
    sha256: 190d4df0200f7c0d24ef4ee314fae907b03d0fe9d7a108b525b83cb3eca68b6a
    role: context
  - path: pages/traits/genomics/long_lamassu_system.html
    sha256: 8eef5a1afd295bbbddcdc19fd7f30c412eab0ba9a5310b10a77d29ada8393b43
    role: context
  - path: pages/traits/genomics/lugos_system.html
    sha256: 409f08fb889b37c3e5648b1c7508015943a21143f8fe7a44d82d63fb8ced9bf7
    role: context
  - path: pages/traits/genomics/mads_system.html
    sha256: f8c2aade63da60e3c9ddcb52d9fd2af73093c9fcb554f7fd9915ca9a98818d30
    role: context
  - path: pages/traits/genomics/mazef_system.html
    sha256: bf6199762602cf79425916da25aa5f239e485c2652c5f2c3677529b5fbbe9bdb
    role: context
  - path: pages/traits/genomics/mcrbc_system.html
    sha256: bdc7b74f5573411ff6623566b16e2d2f607bfcfb1acdc2268997f5e07d59f312
    role: context
  - path: pages/traits/genomics/menshen_system.html
    sha256: 796e23f4bfeefe8194dba353e2af456fe9364b517b1c5a8d3f2e25961865410c
    role: context
  - path: pages/traits/genomics/metis_system.html
    sha256: 29654aae0d791a328e03ae8310703ceeb2cc90464a30fb8591d2bf405e8e333b
    role: context
  - path: pages/traits/genomics/mksbefg_system.html
    sha256: e60b521779611d7dd259c486c43c02f4e2e684e62fab4b7c794e18d6587a7980
    role: context
  - path: pages/traits/genomics/mmb_gp29_gp30_system.html
    sha256: 478fb697e4254536458bda19c613424366f16b5f8ecba21da905c9754a353ca9
    role: context
  - path: pages/traits/genomics/mobile_genetic_element.html
    sha256: b5876b6b4dedeec79c30b128ee259de43b2e6d8383a8c9f35b6befa347852686
    role: context
  - path: pages/traits/genomics/mok_hok_sok_system.html
    sha256: b64c624ef5b7eb6a348c114773a292e5b2ce6ab7b30e8a8f8e74bf5e74d8ac02
    role: context
  - path: pages/traits/genomics/mokosh_system.html
    sha256: 68e4e65a252d6e0dd62dae054f06611a88bf551f9750f027e66f506a88ae8a1f
    role: context
  - path: pages/traits/genomics/mqsrac_system.html
    sha256: fc61df1297b6cd07c6f9beae1863f2af27b18e7e4ffa97432f90d60e5b20a5aa
    role: context
  - path: pages/traits/genomics/mspji_system.html
    sha256: 8b4fa35197dcab35659a4b7767653f4881a4dd4466bff72412a1efd63eb31a6a
    role: context
  - path: pages/traits/genomics/nantosuelta_system.html
    sha256: fef125bc33b47057d457fbabc3d0d28ca53dd6d9b85e70ce4f6629ff56253b52
    role: context
  - path: pages/traits/genomics/nemetona_system.html
    sha256: dc1e84dc1d23fb2bbc9e1be57539885245f9cf581ff6327a749df84a74e56322
    role: context
  - path: pages/traits/genomics/nhi_system.html
    sha256: 1818edbd3ca8d1687326c87e3798acd7a030e8549ac1d48f1eaacf70bf8212e7
    role: context
  - path: pages/traits/genomics/nixi_system.html
    sha256: 43b4867fd73418f09eb043f8b7fef6d01321176b4e3f014ddea5f3362caf2db3
    role: context
  - path: pages/traits/genomics/nlr_like_bnacht_system.html
    sha256: 18aca46c77b3b011d95d95c51d0356916df9ac6bac7d4ace4a243795a505a2d3
    role: context
  - path: pages/traits/genomics/ogmios_system.html
    sha256: a200843564b9b66c67ee0403d5d17040b311238d8e0713b0f91140fdc6732a4e
    role: context
  - path: pages/traits/genomics/old_exonuclease_system.html
    sha256: 414d2eaeaf86aaa8aa881c3a95d8c05f6741b590749515e19f1f1da5a82fb203
    role: context
  - path: pages/traits/genomics/olokun_system.html
    sha256: 649495ecf319604bb399e1112d03362289f453cfae23fb00fee9d77026c50e36
    role: context
  - path: pages/traits/genomics/ophion_system.html
    sha256: 186958df31d13bc314706d0b916cd374d5a1965ecf4ddda1129a2bb987d0000d
    role: context
  - path: pages/traits/genomics/oshun_system.html
    sha256: 3242536dd36bbe1567e9ca7845533ce060452f68a07a7247179c06a8af16683a
    role: context
  - path: pages/traits/genomics/pago_system.html
    sha256: e1d9b9575d1db96921b8c7f2fee92dbe31c9dc2bd15ff8e5c7f75742d5f5a161
    role: context
  - path: pages/traits/genomics/panchino_gp28_system.html
    sha256: a6f824db0e906883393e90837442618797d84a27b2f0438730e896129232badd
    role: context
  - path: pages/traits/genomics/pangenome_openness.html
    sha256: e43f95790b12e5c7aa2d5955d50a57207c7b78763ad7b12cd3e5555a6a5692e4
    role: context
  - path: pages/traits/genomics/panoptes_system.html
    sha256: a134f9b230e067cc290a7fb59949a0a7cbabadd1cc2683e2b65abbf38942035b
    role: context
  - path: pages/traits/genomics/paris_system.html
    sha256: 42d915ceb04050b755ecc730e8e3f98641294881defc0e844e03e92d42866386
    role: context
  - path: pages/traits/genomics/pd_lambda_1_system.html
    sha256: 53cd49c2be229929ea2a5f7bd53dd18933ee2a7bdde985c028bfdf30244c2567
    role: context
  - path: pages/traits/genomics/pd_lambda_2_system.html
    sha256: 2599ca04e47fde8160fead4e1a50366d08bcf115a32dc4abed19e19a6a257338
    role: context
  - path: pages/traits/genomics/pd_lambda_3_system.html
    sha256: 31dbd05f83e0eec99d73f66b4a4d4eeb7e5b4ea3eb7b671af1d798001b0ed43b
    role: context
  - path: pages/traits/genomics/pd_lambda_4_system.html
    sha256: e0c4401a7ce8556339c5a85e513347cea74419d37f97f2f255e919fbb329780e
    role: context
  - path: pages/traits/genomics/pd_lambda_5_system.html
    sha256: 8b6a5d8bb96a09e482ca4d43a6de0af162e6916ca3a3e826589a1f00eed39bef
    role: context
  - path: pages/traits/genomics/pd_lambda_6_system.html
    sha256: e96083f94798615588bac4e8516d87068da771115ef0817e641b5c09b7786ed9
    role: context
  - path: pages/traits/genomics/pd_t2_1_system.html
    sha256: e12b1a1678ce6c90b93278a3f9c296fe5ffdf7e5475ae3d05f55afd324a48d37
    role: context
  - path: pages/traits/genomics/pd_t4_10_system.html
    sha256: 439a7b5ea50f05c303aec34846507eca9ef3bf4f4125815c422cdc07e363f33e
    role: context
  - path: pages/traits/genomics/pd_t4_1_system.html
    sha256: d6bbe8f5ec6627a9e79a4fc3480260ef7b149cd512644450bf7bb9944ce1033a
    role: context
  - path: pages/traits/genomics/pd_t4_2_system.html
    sha256: 906eb885291f685c91d49bf345be494f553355601033a6d7f0c365f1b594562e
    role: context
  - path: pages/traits/genomics/pd_t4_3_system.html
    sha256: 94a2037e3e4da9d6e0e5b79749eca5f92cf537ae6d3f8ecc5f53dd56ffa4abc0
    role: context
  - path: pages/traits/genomics/pd_t4_4_system.html
    sha256: d09acd4859a637617fc35e50400088e99787dd1adb191b30d235efbbaba1177f
    role: context
  - path: pages/traits/genomics/pd_t4_5_system.html
    sha256: 5abaeace8c7b6ef38cb1b8dda3a9d205852aaee21fd5ad4caa7ab3909f15876b
    role: context
  - path: pages/traits/genomics/pd_t4_6_system.html
    sha256: 6a933b2c0fa1fb6fe352ceb9bec3b867fb806ab887f1a2d645bed9875cadfffa
    role: context
  - path: pages/traits/genomics/pd_t4_7_system.html
    sha256: 2faa84edafcb10e8c9c96d8dc44d87087b5fd8900cc2e77a469138b76b870028
    role: context
  - path: pages/traits/genomics/pd_t4_8_system.html
    sha256: 6ccc6770e3dd6375e6f40ec938439fe7f0d3e779f4e3e9d209ab2d74588d6e0f
    role: context
  - path: pages/traits/genomics/pd_t7_1_system.html
    sha256: 219f8e0b9fa6bce9818ce772765a8b719d3521a4bfb68f6022032d015e3d42d5
    role: context
  - path: pages/traits/genomics/pd_t7_2_system.html
    sha256: 9ad11014465c1274ec66632f0b6d405755f6fc726e41af6c983bcdde6f658a2c
    role: context
  - path: pages/traits/genomics/pd_t7_3_system.html
    sha256: 2a121aee7508da6391394e82083c77db1a492707be567ecb6394f50d6e971690
    role: context
  - path: pages/traits/genomics/pd_t7_4_system.html
    sha256: 66e04a6c1370b3a136cc4cfd7b8c2f8ce2c5f9a354ebb625d1beb29b1854f8ca
    role: context
  - path: pages/traits/genomics/pd_t7_5_system.html
    sha256: 597686d358fd6040a59001e17affcbbdfa963d273f123080255f151462e59384
    role: context
  - path: pages/traits/genomics/pfiat_system.html
    sha256: 338c6dc6cc34106ccbd4dd426c74a18818ed571eb10e38c208184ec6f38b57e0
    role: context
  - path: pages/traits/genomics/phage_defense_system.html
    sha256: 19bf01c1684ad012977a8f5848e92450de3cc9e669cf401ba60e6b5d56dc991b
    role: context
  - path: pages/traits/genomics/phosphorothioate_defense_system.html
    sha256: 0e4b92792bed0c0b93f2104cf6f355a17c69cae424361fb6ed2317defbc95f51
    role: context
  - path: pages/traits/genomics/phrann_gp29_gp30_system.html
    sha256: 07bf6e877c40ef6bc07b9e78200b06e448ecbfb5aaba2bca178b670a0eaedeba
    role: context
  - path: pages/traits/genomics/pif_system.html
    sha256: 3388b059b5060398272b148c56678127e4332a01b6b2c87643352fada23c5398
    role: context
  - path: pages/traits/genomics/plasmid_carriage.html
    sha256: fe03157b182bd74f3079a8ac84a3dc9f400ea9f4500c78c430eb3853e4235a8c
    role: context
  - path: pages/traits/genomics/ploidy.html
    sha256: 0476851b57d97c338d450afd3da85d1f8e1fe83b1081e46b109deb2ded7e0106
    role: context
  - path: pages/traits/genomics/prithvi_system.html
    sha256: e7b3592a0f9af3a84c83c5319b8f1f524fdc77a993a7553d87c85d2466ad89c9
    role: context
  - path: pages/traits/genomics/prometheus_system.html
    sha256: 5fe85c9d8b4134f1589ede139992c56fd3685f8f06b2b7479ef2a96b47bd1a18
    role: context
  - path: pages/traits/genomics/prophage.html
    sha256: 0c8a66812e7427438fd0eff20ccdd1fc86d910e450e5f3abce3c2872115f2bfb
    role: context
  - path: pages/traits/genomics/prrc_system.html
    sha256: add01120091ba3e9fb0427559fdf086afa71b23681c925ecca67af3d19517b21
    role: context
  - path: pages/traits/genomics/psyrta_system.html
    sha256: 76e425acdf8ab3890ff6f793b14148f59b968708edc5d128773d768ac048292f
    role: context
  - path: pages/traits/genomics/pvurts1i_system.html
    sha256: e5331fc967ec72384e6c3c2b6662206e072f90fbd42fc2c504943ff04879f952
    role: context
  - path: pages/traits/genomics/pycsar_system.html
    sha256: e0a6b39a5781dc48e0411c98f8e507e21a57ed1d82a059531954ea4bfb247f03
    role: context
  - path: pages/traits/genomics/radar_system.html
    sha256: fff7e01669165cad9c799387e68241d4b320feb2239da6a3bffe0ba47532e931
    role: context
  - path: pages/traits/genomics/razr_system.html
    sha256: 105867c18b1f28dde56799abb6e90c52b3d3ff89e13cfa84e9344ed4016b04aa
    role: context
  - path: pages/traits/genomics/resolvase_duf5677_system.html
    sha256: c0731804882f260866e5038184cc3224a282c2560212089b3057b08e12a52fba
    role: context
  - path: pages/traits/genomics/resolvase_kap_ntpase_system.html
    sha256: 16a21fbf1f47d812f0e311e3a2b883e953e9b75b75301c67342d1d7361df13ae
    role: context
  - path: pages/traits/genomics/resolvase_schlafen_system.html
    sha256: d7982027cdaa90b2ce7a79898715d3b0e29b814960a956273feaec74250c696e
    role: context
  - path: pages/traits/genomics/restriction_modification_system.html
    sha256: d4345c15b22793ff8664ab6861afc95716d7b25a24db6dc89538c5d86f30991f
    role: context
  - path: pages/traits/genomics/retron_system.html
    sha256: 75a50ed733a3b4ba93aee46eafdda0ec836420d4e4da810b56d0145d6fa2df84
    role: context
  - path: pages/traits/genomics/reve_system.html
    sha256: 77c6d8b5712cb08a0f6fcef2f3bda882479b6a9f44d92af50f0f11b4d39fbca1
    role: context
  - path: pages/traits/genomics/rexab_system.html
    sha256: f888e9c3d42a03ba7f4cc3f9dd7e4f86a84941559ae9b75a5e4e4e4b719a9c03
    role: context
  - path: pages/traits/genomics/rhea_system.html
    sha256: 76739af21810512edb5965819a04a26c90db60c78c102efe4c23a8d720aceb17
    role: context
  - path: pages/traits/genomics/rloc_system.html
    sha256: 62a0c4f544b41738e7db9cc37085c7976022237707a84358e82e4009bdc749ac
    role: context
  - path: pages/traits/genomics/rnlab_system.html
    sha256: be631db908655e64f5585dc00a9f633ee13a9b3780163961443695635b08093c
    role: context
  - path: pages/traits/genomics/rosmerta_system.html
    sha256: 21a9dba43d4d9a179f9f64680a6ef43c4da07099ed4651f0518cd0b111b8a955
    role: context
  - path: pages/traits/genomics/rrna_operon_copy_number.html
    sha256: 5e278ea66ab192464f900422f72851919a3e5809054ac97dc7acfd4f27fa774c
    role: context
  - path: pages/traits/genomics/rst_2tm_1tm_tir_system.html
    sha256: 03bf1269be223b824a94616b829b2e22aabb04cc47252d46af423163966f2dc2
    role: context
  - path: pages/traits/genomics/rst_3hp_system.html
    sha256: 1dfb698cd689de9a1350af25b6686b130d1f9a29bd032ce854207f31b2084280
    role: context
  - path: pages/traits/genomics/rst_duf4238_system.html
    sha256: 2ea83e5c90588e8425a9a2f736e9253357867c0c620ea15195dc9d4c955e5f04
    role: context
  - path: pages/traits/genomics/rst_gop_beta_cll_system.html
    sha256: 5d5c85bf573475f263a1eae99f0ef753f344c9eca6ceb3e5b0c586410e1db82e
    role: context
  - path: pages/traits/genomics/rst_helicaseduf2290_system.html
    sha256: fa4e86bfd72573e1966c503c1f78eb0799fd72ece37a4f07f243556cc9374d2a
    role: context
  - path: pages/traits/genomics/rst_hydrolase_3tm_system.html
    sha256: 8b98401948dc15afc43abe11871b2dc36668c7da7fda8c7067c6316a1c96d075
    role: context
  - path: pages/traits/genomics/rst_rt_nitrilase_tm_system.html
    sha256: c42c4f00ac39ea6100bca99c422d6c9ec151df89a68978aec3c4f6b11f98099d
    role: context
  - path: pages/traits/genomics/rst_tir_nlr_system.html
    sha256: 750bba2f80576776698c6c97c8907b9fdfd7ddd1e8b3d64b7952c0737192b5f7
    role: context
  - path: pages/traits/genomics/rugutis_system.html
    sha256: 6c16411a9594ef0e1af211dae6b56e5b6000f38a987650c7d299a8a485e8d49b
    role: context
  - path: pages/traits/genomics/sanata_system.html
    sha256: c89a0f312db51e0a9fe36bba4d53767e3da36b10d9d797422c2c3eedabcc190a
    role: context
  - path: pages/traits/genomics/scomcra_system.html
    sha256: 7e91b2b82aa833649ed930d5f8fc72e4da4de2ea822f62345a0178f1e8bb69ee
    role: context
  - path: pages/traits/genomics/sdic1_system.html
    sha256: 1745111517fb9bd19ea128275730399bbe7321f8c7b874f1eaf745f853c0286b
    role: context
  - path: pages/traits/genomics/sdic3_system.html
    sha256: 3eb91f7ae21ebef965479014175f4a683ab464e3b9bdd1f765dd1bb07cab9863
    role: context
  - path: pages/traits/genomics/sdic4_system.html
    sha256: aadd393eed0256355245b320084c70f2b6322b67b1ee87cb0dd3bf98f8ffed2b
    role: context
  - path: pages/traits/genomics/sefir_system.html
    sha256: fed2db55a495ab2529a08ab538a1b6eeb15613980f8ba87187a2eb05c5ab610e
    role: context
  - path: pages/traits/genomics/septu_system.html
    sha256: 10168a24035c51c78685cc13ba4ec5bc01809768e6eaa9e780de4ecf8f11a628
    role: context
  - path: pages/traits/genomics/shango_system.html
    sha256: 230ffcea7eefa79819334cba0097a5b6c15cc7d010ceca7c448aa98b48817427
    role: context
  - path: pages/traits/genomics/shedu_system.html
    sha256: 774a8c11cbc008940f6d75800f949d86c3cebc20b8ad6aa4ad84e5d6e173efaf
    role: context
  - path: pages/traits/genomics/short_lamassu_system.html
    sha256: c433464643eace896fd309a4694cd2b5eefdee974683dfc76f3a16df0fe0e5d7
    role: context
  - path: pages/traits/genomics/shosta_system.html
    sha256: e23653f30497d7bf65555cb90e067015ce29aa3e12a9a65321acfec675901ab4
    role: context
  - path: pages/traits/genomics/sirona_system.html
    sha256: 9591f2a773130b8dbac4f2735fcb1ea7e74352828af94d30476bb97588694ece
    role: context
  - path: pages/traits/genomics/six_a_mbl_system.html
    sha256: 4daffa6c2420a50de5319c3a751306e1d2884346a8a17fe6544b927cb60d0d69
    role: context
  - path: pages/traits/genomics/snipe_system.html
    sha256: 300039eaecbf57fe81db2a182479c8555982877ac89f306bde0af2d208f56c88
    role: context
  - path: pages/traits/genomics/sofic_system.html
    sha256: ff2467e125e31f811bb574195d6d1eee416fd83c95d507a74eab23f92f996129
    role: context
  - path: pages/traits/genomics/sparta_system.html
    sha256: 89e2f416d96ed694b067b0f06d97c42f7788c25f495c209f729fa3b35af86e28
    role: context
  - path: pages/traits/genomics/spbk_system.html
    sha256: 7d8eb93ca417a5ed15e5a5092ce20e4379e8e60ba71e1660745eb7a07b600128
    role: context
  - path: pages/traits/genomics/sspabcd_sspe_system.html
    sha256: 7242f950931eb1cfde4ca907609b49172a0fffafe3d993884f05a7b83ce7b50d
    role: context
  - path: pages/traits/genomics/sspabcd_sspfgh_system.html
    sha256: e18c83d4b35caa18f81b472c13fe5263b5159328c57bf64c3ce4eba0cabdc1e7
    role: context
  - path: pages/traits/genomics/stk2_system.html
    sha256: 09bf86d2c0cd1c1cf49b3b4a16a1786d893457d9901a31bf9c330c181c8377ae
    role: context
  - path: pages/traits/genomics/sucellos_system.html
    sha256: 3a934f113c137769b2aac7301ffab8a5d7d3204a500a59cbd981cd26837df08b
    role: context
  - path: pages/traits/genomics/tab_system.html
    sha256: 8bdc63c335fe996b2e5bb890d805f635003a07b41f2dee1c45ebf468103ed51f
    role: context
  - path: pages/traits/genomics/tagi_system.html
    sha256: 3c4260d046f327c5745c992a7e1410b961a1a55553105f5296e511ad63485186
    role: context
  - path: pages/traits/genomics/taranis_system.html
    sha256: 669e2474c95e519c358ee1c67cfe20327c514379cd55dd3ba46f3f35d621624f
    role: context
  - path: pages/traits/genomics/tgvab_system.html
    sha256: 6168b0ad4c99547137dec34ca01ca4d72d90f94d8e42ee4efaef112d697afaea
    role: context
  - path: pages/traits/genomics/tha_system.html
    sha256: 21cdf6be6adabe71175492862b33b5a3668e20f26f8461c80f858547530f555f
    role: context
  - path: pages/traits/genomics/thoeris_system.html
    sha256: d17599761e6e03842fdfbd725bf95147ff9a8d2d1d153027f1404dea97ce9085
    role: context
  - path: pages/traits/genomics/tiamat_system.html
    sha256: 68ee1003461da4ddd072c9d3e9bae584632cb6256e5497548e5cf1838ebd50db
    role: context
  - path: pages/traits/genomics/tir_i_system.html
    sha256: 76054a429210cc02bc9f1c27c85873a7ddb163e769e7471f9047ec978cd6b634
    role: context
  - path: pages/traits/genomics/tir_iii_system.html
    sha256: ad53f9cde34410ed7bbb3f9f4fd2a7ffb65ad02ed88f5b38d165752e6c01b21e
    role: context
  - path: pages/traits/genomics/tir_iv_system.html
    sha256: 06a2f848086983384028f5c10b86e154028636476a0eaa40063b91d713a40349
    role: context
  - path: pages/traits/genomics/tir_vii_system.html
    sha256: 4ece02bdc6189f54e071dab5d798ceb6898adf343c833c4399d0141c9e4d0b3c
    role: context
  - path: pages/traits/genomics/tir_viii_system.html
    sha256: 6d393928561da9eadcf6ee6eb54f2e3273c53b1cf1741b11977714f496b42cb2
    role: context
  - path: pages/traits/genomics/toga_system.html
    sha256: f8c54f43a0cbea5b32f33262c92591e0403415068cb6ed4a5c861a31530c422c
    role: context
  - path: pages/traits/genomics/toutatis_system.html
    sha256: c8a7b28e8961d4e278cb102dd6c990e60b83d7b6c104e91153084f1a28b4594d
    role: context
  - path: pages/traits/genomics/toxin_system.html
    sha256: cf5209210a4b8dbe9152e496d048602e00be25053b4891be711788465ce647ce
    role: context
  - path: pages/traits/genomics/transposable_element.html
    sha256: 9029b225779f976db676871bd2b1c39be2b8e4da1c268fbe837b826f0b2844b7
    role: context
  - path: pages/traits/genomics/type_i_restriction_modification_system.html
    sha256: 4d485c3da0bca3324cfe5929af9e6502ffe59199df172020827c4938a1b4d895
    role: context
  - path: pages/traits/genomics/type_ii_restriction_modification_system.html
    sha256: 9d1ad18cef8378544e6298615cd4b8fc6aa01a9cb262d538d5662a2fc0eb0bff
    role: context
  - path: pages/traits/genomics/type_iig_restriction_modification_system.html
    sha256: 5a1d923eaa27063f0deb797ac66534b57bd92b754485c7452c73c4aa14a5fafb
    role: context
  - path: pages/traits/genomics/type_iii_restriction_modification_system.html
    sha256: a818b636e337852a0e7aa89dd87bb5494ae71c60792026b9869bb6109324039d
    role: context
  - path: pages/traits/genomics/type_iv_modification_dependent_restriction_system.html
    sha256: d376b5af10a96cc1dfa76e01255be58f85e981a1c6793edb2302a2d2eefe4719
    role: context
  - path: pages/traits/genomics/ukko_system.html
    sha256: 3cc733999c788c00d9114457afa103a5eb76c28607cfc1a2fbe1fb534e3a4926
    role: context
  - path: pages/traits/genomics/uzume_system.html
    sha256: e9af06b9236c2af69d7790c31848f9d9bef7c230984cfec2a2fcf28f0340ea2e
    role: context
  - path: pages/traits/genomics/vcam4i_system.html
    sha256: 1ff9e4ba1132f47f8506d0264f133f9f557f026983958ad8e70184cc54e24cda
    role: context
  - path: pages/traits/genomics/veles_system.html
    sha256: e1deb17b0a83a2f09188c736f74e0513ea574176ae2b012ac5978d9b30266c45
    role: context
  - path: pages/traits/genomics/viperin_system.html
    sha256: 1d88535b975a99f1c69c48953cb19bfc8df141c8d0446b37f4d88761fc4b11a0
    role: context
  - path: pages/traits/genomics/vp1796_system.html
    sha256: 0e990d84a06da227854707c53fdfccdffa0734d801b2d4874896ccba21693a1d
    role: context
  - path: pages/traits/genomics/vp1817_system.html
    sha256: 331ba12be5de6734472cc4fec079593c3698075b0dfe62c35962afc4c5db4003
    role: context
  - path: pages/traits/genomics/vp1823_system.html
    sha256: 0a738f8e7915913dc966d3fd504c95a67344f63ace9899009ff17bb8f43e8054
    role: context
  - path: pages/traits/genomics/vp1826_system.html
    sha256: 9d942366889ed1e8a408fb9522c881bc9561cf65d234e68172c2b0ce5f6f934d
    role: context
  - path: pages/traits/genomics/vp1839_system.html
    sha256: 0508d47d77fe1452f81af01d736f6fcfbaa9be32fec7125d94572859d3fd843a
    role: context
  - path: pages/traits/genomics/vp1840_system.html
    sha256: 3d0695f01349f9e153f10f16143b7727766fb5763980664068e56ebf6ac73960
    role: context
  - path: pages/traits/genomics/vp1848_system.html
    sha256: e4d5c3c40d6058e32da476bc0d461835d2f67ffa233bad8e741260580e21fcfc
    role: context
  - path: pages/traits/genomics/vp1851_system.html
    sha256: 230b0ef22ee420f7e75588d73d0de6f6c85bead9da17a88643425f08855186ee
    role: context
  - path: pages/traits/genomics/vp1853_system.html
    sha256: e9801e2025776ca5884a7b71a6bb96a05b36cd7ffdcb4317ff72e0a66bab4e2b
    role: context
  - path: pages/traits/genomics/wadjet_system.html
    sha256: a29f3c17d1c34211d6738c04e4d046aa5d57e7d92df0f097784a5476045871c2
    role: context
  - path: pages/traits/genomics/zorya_system.html
    sha256: 60092f5703f3264a1dc56dea606fdeb0519359c41f1a238bf2d996f5826a09e9
    role: context
  - path: pages/traits/genomics/zorya_type_i_system.html
    sha256: cc9e32eee3be832ad4f168a3c1232ee351b15a6e2dd3916e6e935c5452632cfd
    role: context
  - path: pages/traits/genomics/zorya_type_ii_system.html
    sha256: 6e882eb2f0625820c976805686e8ba3ae76e954a7ea4222e7e4e6576315d8a13
    role: context
  - path: pages/traits/genomics/zorya_type_iii_system.html
    sha256: 200919732186de722a28d9297936252ee2a382a222843ff779226e65756f4ecd
    role: context
  - path: pages/traits/metabolism/accumulates.html
    sha256: fb3e95a2ebc08d300264f062a8396e5b39357ba853634bec0589cc5715f81b85
    role: context
  - path: pages/traits/metabolism/acetoclastic_methanogenesis.html
    sha256: f5bdc1480fd5005f483c42ac80059920f982138da22ded4501d8c411b1a59c00
    role: context
  - path: pages/traits/metabolism/acetogenesis.html
    sha256: fde9d37391314251c2da7f5b28a77f7393d0ef122c87b0ca3b1b8662d3b5db94
    role: context
  - path: pages/traits/metabolism/acetone_butanol_ethanol_fermentation.html
    sha256: 6b82c7d96f89dfd6b4cb3c37597e755401a7aecb1bf0b16417021a5c44a718b0
    role: context
  - path: pages/traits/metabolism/aerobic_respiration.html
    sha256: 7492a643624d5956e3a626b3dde052a88daa898278c0e119f586b2055278a23f
    role: context
  - path: pages/traits/metabolism/anaerobic_ammonium_oxidation.html
    sha256: 44ea89cb5b4a4a42a44c7793b30e3b2383c19b3774f13e8f711169ae83819a16
    role: context
  - path: pages/traits/metabolism/anaerobic_oxidation_of_methane.html
    sha256: 1b57ee7c6fd939004b00abd99bfdc9a054ccf19e24c10b8da50c18d3cc1cc796
    role: context
  - path: pages/traits/metabolism/anaerobic_respiration.html
    sha256: cc773ce55c6bb44f5ad055216242d0f8bf032747d74670419123beedd56b2a4f
    role: context
  - path: pages/traits/metabolism/anoxygenic_photosynthesis.html
    sha256: 1c498d5eef3d92f511b5fd22eda79b6d770a7706bb26ce43d8a7b5f1a312b722
    role: context
  - path: pages/traits/metabolism/aromatic_compound_degradation.html
    sha256: 5c447ed9cd6988a0242115b326ed33146808bc032dbcc265c8182d90a06c04c5
    role: context
  - path: pages/traits/metabolism/aromatic_hydrocarbon_degradation.html
    sha256: 07e30f093e323635a72e237370deeb9f7bbc4f08b6c635d0226e5cf13761f153
    role: context
  - path: pages/traits/metabolism/arsenate_respiration.html
    sha256: 46796285b83d92806e4e9b4a683fb0883c0e5bfcac03003259f48c97039cbb10
    role: context
  - path: pages/traits/metabolism/arsenite_oxidation.html
    sha256: e9bf95ee9f0cf1e74eb8d657ae5e6c3731a537dfebcf7aa2181df70a53f60a40
    role: context
  - path: pages/traits/metabolism/assimilates.html
    sha256: b9ea59981e409a26a0138b9c17963b55576a308b1bb6367b353f4192eb35e151
    role: context
  - path: pages/traits/metabolism/biopolymer_degradation.html
    sha256: 358836596ce16622be96caea9ab04b3652b72e4d882e11f93e5cdad5142cbd22
    role: context
  - path: pages/traits/metabolism/builds_acid_from.html
    sha256: e179e2462493f90cc49577929874c7c7377821b8192057cbb35abf3ad4602807
    role: context
  - path: pages/traits/metabolism/builds_base_from.html
    sha256: b0a0ac7fec7972829a506f4c8a1eda552e323740e0751721f4485201ccc47b4c
    role: context
  - path: pages/traits/metabolism/builds_gas_from.html
    sha256: 24106a663f1a761be8b5713596bf65a66d7e2b974d134bf396d863db920a6185
    role: context
  - path: pages/traits/metabolism/butanediol_fermentation.html
    sha256: 7897066ab80292e491cf37ddf8e813d14c7ab9464c3f4d397a42d955176afc6e
    role: context
  - path: pages/traits/metabolism/butyric_acid_fermentation.html
    sha256: d5df864aad936dc133ac125b8875a353771b0e2acd18cfd1dd7c4f208839a724
    role: context
  - path: pages/traits/metabolism/cable_bacteria_metabolism.html
    sha256: 09e4a93b7d65cf41367d15a6f980a557b4aacf48f502c7d3b53332da03e2032b
    role: context
  - path: pages/traits/metabolism/calvin_benson_bassham_cycle.html
    sha256: 4c2d4396858ec0e1a0b66e0e6f0c9f46ce09d8c73f4818a256c966cc7f76c81e
    role: context
  - path: pages/traits/metabolism/capable_of.html
    sha256: f670f2bd2d289bc6f01cdddf3b8dfb61d1580ec680a46c6098892ee6a77d230a
    role: context
  - path: pages/traits/metabolism/carbon_fixation.html
    sha256: f7e9f42518b6e7371eec421e73ad6d70016a1f1851147ffe9c57e91edc486ee7
    role: context
  - path: pages/traits/metabolism/cellulolysis.html
    sha256: b3c3be3fddd3e36e36f94918531b2cea140bef9715c554c71c7b3520431148e2
    role: context
  - path: pages/traits/metabolism/chitinolysis.html
    sha256: 7df60217ea0b20942e57971fbf5587e67e0c6e6937924b0b54b09d6082161d7f
    role: context
  - path: pages/traits/metabolism/chlorate_respiration.html
    sha256: c3f1f28030b3269ee2458fab259c8b9df9673a282ce4d6f6b29fe4a9a1b9b0a8
    role: context
  - path: pages/traits/metabolism/citrate_fermentation.html
    sha256: 2ac84928cf76a918f3e112d41c7910217cd58acc2d06c88464eb34ad1b0e0464
    role: context
  - path: pages/traits/metabolism/compartmentalizes.html
    sha256: c8afd4811c84ec33f3d6b3b76100d3d30ff782564ed8f540bd68132a716ab305
    role: context
  - path: pages/traits/metabolism/complete_ammonia_oxidation.html
    sha256: ba2ec29bfd5516a9f799719787b00c902572cc7759a837182b1b1587d769ea5d
    role: context
  - path: pages/traits/metabolism/dark_hydrogen_oxidation.html
    sha256: da52db13bd674550efa258aa58cc709941afd2f671d2b299dadbb21923803c10
    role: context
  - path: pages/traits/metabolism/dark_oxidation_of_sulfur_compounds.html
    sha256: 9fd2381e47640bd799f8ee066cb4ff85a48670d86fc89be048b3ef5b6f4e4996
    role: context
  - path: pages/traits/metabolism/degrades.html
    sha256: b13c9b708b4557519bfdb663e13e3fdcfd322d528c7311534cec83dab32b1750
    role: context
  - path: pages/traits/metabolism/denitrification.html
    sha256: 33c51f155637652a16c35d50334a8374fa9ed9a6755018719c77d2948ed3eed7
    role: context
  - path: pages/traits/metabolism/dicarboxylate_four_hydroxybutyrate_cycle.html
    sha256: f25931d958305758ea8da37b80748894724683a6a873d1c88a8538fab3b2b42b
    role: context
  - path: pages/traits/metabolism/dimethyl_sulfoxide_respiration.html
    sha256: 8b621ab874f22960d37951e651408c277a6102c1850e62603c42848dbbe43837
    role: context
  - path: pages/traits/metabolism/disproportionates.html
    sha256: 79f46a7c799b7210e50e33721423db232ee0e479464984446e03ecabe9ff21f1
    role: context
  - path: pages/traits/metabolism/disproportionation.html
    sha256: 84278310973d41dcd92c856c23f626c16deb9087438c9272d2b83a1b8a816645
    role: context
  - path: pages/traits/metabolism/dissimilatory_iron_reduction.html
    sha256: de763b87baccedb52794aa12f0ac499e93ea486439491b44be1013aebd0c56c4
    role: context
  - path: pages/traits/metabolism/dissimilatory_manganese_reduction.html
    sha256: cb475d45bf116a8ffa51068411e6bc14edbcb874dd7868cf8ae04530074a32eb
    role: context
  - path: pages/traits/metabolism/dissimilatory_metal_reduction.html
    sha256: 9f4a8b9d7ccc956aecbecd5a60679bf3b39670713dbcb9e9e3129a82c7835924
    role: context
  - path: pages/traits/metabolism/dissimilatory_nitrate_reduction_to_ammonium.html
    sha256: f4d0ae2aed78eb7d4315f7b15d69c6804acd9bb5ac2adb7d0773bd14209f163a
    role: context
  - path: pages/traits/metabolism/dissimilatory_sulfate_reduction.html
    sha256: bf4f6261ea70cabb769027aa1fdb1427c72960e5732ec7ceb99f9c726987a1de
    role: context
  - path: pages/traits/metabolism/does_not_accumulate.html
    sha256: 18de3778d73e5a5b63438fc1a6af5a7b92e574d355dfdc6aec1505ba5ab78770
    role: context
  - path: pages/traits/metabolism/does_not_assimilate.html
    sha256: c2a6b952ac2823d9e741504c591cc61e3ebcd2324b462bca2e113e91f5b764b0
    role: context
  - path: pages/traits/metabolism/does_not_build_acid_from.html
    sha256: 9aac5770129ee3a41225fe1226ccf07dca338ae60d492d4720ea66f84c14a119
    role: context
  - path: pages/traits/metabolism/does_not_build_base_from.html
    sha256: 74fed3b899025e50bbb404bd9c964c52020cf3c168dae885ef017386bafa53a9
    role: context
  - path: pages/traits/metabolism/does_not_build_gas_from.html
    sha256: 512257cbe64a70155004b562abc68639ea07a5e164afb73ea8110a32ecb18e6e
    role: context
  - path: pages/traits/metabolism/does_not_compartmentalize.html
    sha256: fd7f36e2929a2b25ce82ba658c9881bf98dd65b06fba4201b7a1331473879d97
    role: context
  - path: pages/traits/metabolism/does_not_degrade.html
    sha256: 8ea0dc581983b8f2db1ff5c9bd1ea3f24011b15df99775a253f205bb846c75dd
    role: context
  - path: pages/traits/metabolism/does_not_disproportionate.html
    sha256: 0b7c27f81bb88a90d7aa78c60278a688e40e7652a8be6eada03ae7e01feb4fbf
    role: context
  - path: pages/traits/metabolism/does_not_export.html
    sha256: 2f8fb28ca64d3dd9a1ea0563402bb39f962f9317c3b3ea625f9efbb4420dcff9
    role: context
  - path: pages/traits/metabolism/does_not_ferment.html
    sha256: 9f312e6dc132d91d8d5ea07f5a2512bd9f51c7e9352c508198bee843308279a2
    role: context
  - path: pages/traits/metabolism/does_not_hydrolyze.html
    sha256: a1048c99413e3cb1861ae50c880e28ac0c8d5e921be97cd56c9d73aab1574200
    role: context
  - path: pages/traits/metabolism/does_not_import.html
    sha256: 47e8e129a74f9520ae8ee04cb92999986376e23fa25d3d78bcc3951e9425ae94
    role: context
  - path: pages/traits/metabolism/does_not_oxidize.html
    sha256: 4217a180dd6516e9f85d23c6f07caabfd127fb91e390db9730182958dbfdb5d8
    role: context
  - path: pages/traits/metabolism/does_not_produce.html
    sha256: 24b7a71f2fcfb2b987358f84bd73d8dce88add2f8987e4c4f99f40729ac9763b
    role: context
  - path: pages/traits/metabolism/does_not_reduce.html
    sha256: d8d799649a5ff391cf1b94fd478e9ad843f4bdca7b072af79c9492cff6a43f4e
    role: context
  - path: pages/traits/metabolism/does_not_sequester.html
    sha256: 84bf6c4ad07ee5c980db6db76471965ffdf166171e78d799e2420aee8ca90525
    role: context
  - path: pages/traits/metabolism/does_not_show_activity_of.html
    sha256: 7fc1fb6c73bfbbefd2f5b933ef086fabf17e9226b1709f771984ed8cf52b8ab4
    role: context
  - path: pages/traits/metabolism/does_not_transport.html
    sha256: dd67cd81692624937a66ec8bc8128684494cedb7c3515dee9ea070df2b500b21
    role: context
  - path: pages/traits/metabolism/does_not_use_as_carbon_source.html
    sha256: b3ce9054fde2d3a7db303fc8527a25c2b6c9ef78d3c0c3983a55aef0214f37d3
    role: context
  - path: pages/traits/metabolism/does_not_use_as_electron_acceptor.html
    sha256: df8f5c8b7e9a6d3f5ba302836ac09539d6cb1395daadcf04b3cd9d2af6908ec9
    role: context
  - path: pages/traits/metabolism/does_not_use_as_electron_donor.html
    sha256: a2093d3c104bdcba8c7040280d36c891861851f3a5f46cef558ec22b99666377
    role: context
  - path: pages/traits/metabolism/does_not_use_as_energy_source.html
    sha256: 105ad2da79cddd4d619f25d7969928e0f6424142ed89945830e35e30e2427d1c
    role: context
  - path: pages/traits/metabolism/does_not_use_as_nitrogen_source.html
    sha256: 5f9c0b201924aea660d7895210259450a5c4b97c3c4fff11612eb208fc951f50
    role: context
  - path: pages/traits/metabolism/does_not_use_as_sulfur_source.html
    sha256: 1eedfb73f1d26567d72fc364623270c9cfb9565e6256e1bca77f692f2ec41432
    role: context
  - path: pages/traits/metabolism/does_not_use_for_aerobic_catabolization.html
    sha256: 5ab939b23c2d0d4f5451095b72c88f33a07205aa522541a273249d3b372fb749
    role: context
  - path: pages/traits/metabolism/does_not_use_for_aerobic_growth.html
    sha256: 55507d35bd7c077f18304799eabb60964d0a01dee4f34dded68e2499e22b961d
    role: context
  - path: pages/traits/metabolism/does_not_use_for_anaerobic_catabolization.html
    sha256: 8d541aec0e84d4cf1fa4d34a55098a4556390c5ca02e42ee399c8652a2d5e7d5
    role: context
  - path: pages/traits/metabolism/does_not_use_for_anaerobic_growth.html
    sha256: c2c5c8a7380524e767aa0cbe78df08ff2db58d58ad5a9d3665cc995410ed4855
    role: context
  - path: pages/traits/metabolism/does_not_use_for_anaerobic_growth_in_the_dark.html
    sha256: 1f6c1f57afd26b771115d20506bc516e6d07f0e52e6ef1e1a35a1192234cdb5e
    role: context
  - path: pages/traits/metabolism/does_not_use_for_anaerobic_growth_with_light.html
    sha256: 10756597daa8c94e64a1c6eb8bfe3fc4628e506d833c41c56741692d483849c1
    role: context
  - path: pages/traits/metabolism/does_not_use_for_growth.html
    sha256: ae1f242e7de01e09d8a8aa80f108485e77dc4925a859c74e2f33048c970b8f7c
    role: context
  - path: pages/traits/metabolism/does_not_use_for_respiration.html
    sha256: 061f160e1d31d68f592295a3cf94aaa92c15966fec697d8020c16eb89786dfdc
    role: context
  - path: pages/traits/metabolism/does_not_use_in_other_way.html
    sha256: 39cf470fcaadb7b7a20ea73965e0d06b07507ee1dc3e1840ab90bf91e6a6b5b4
    role: context
  - path: pages/traits/metabolism/electron_transfer.html
    sha256: 8c294f2ac39d168bf1bc648a659a3d82e09a19040dc054dfee05bc3998b9b3b3
    role: context
  - path: pages/traits/metabolism/enzyme_activity_analyzed.html
    sha256: 2f7ad4adf364fdbc6f2fc510061d93abf21d8ded2d2fa8168a3a07724c6881ad
    role: context
  - path: pages/traits/metabolism/ethanol_fermentation.html
    sha256: c910b20ab6cc905e2a8f849057db7306ca42f062b33116cb86829b6c4f7b554d
    role: context
  - path: pages/traits/metabolism/exports.html
    sha256: 2abc8750553456c15b7015ac4a04b89c2ffab3b03da296a46a3da92fccea837f
    role: context
  - path: pages/traits/metabolism/fermentation.html
    sha256: 13778b5b767465c6ea724fa1343c5bb828d8b95f333c9315194ad3e2efcf1c8b
    role: context
  - path: pages/traits/metabolism/fermentative_hydrogen_production.html
    sha256: 326eadea1d8f5b88c2bfc5290662fe5054638e500019d41567db09473482e47e
    role: context
  - path: pages/traits/metabolism/ferments.html
    sha256: ee4f0ebcf54295658a9ff34a108ab03885a7ab5b3a230a1a44386b2d2addb6bc
    role: context
  - path: pages/traits/metabolism/fumarate_respiration.html
    sha256: 8bdc7d96295e6a0efccd6946e28b8a4c2f57aba8dfd8bf693bebcaa365600798
    role: context
  - path: pages/traits/metabolism/has_growth_nacl_observation.html
    sha256: 91340a8c9e54125918b705440ccc45592657c49d03175b0996cff1d8a9bf7fa7
    role: context
  - path: pages/traits/metabolism/has_growth_oxygen_observation.html
    sha256: c8c152b7ad6eb1ca43acb0bae385a0b341f6c3a46134f92b81d99b78862ac34a
    role: context
  - path: pages/traits/metabolism/has_growth_ph_observation.html
    sha256: 4c29f59a53edc22d0f1daa54a5b0acd864a1567233cedee174f09aea5f7ffdfd
    role: context
  - path: pages/traits/metabolism/has_growth_temperature_observation.html
    sha256: 628edd9740448e9a98513745c4148c6af00cdd540f5d18f92a5279ff9821adc5
    role: context
  - path: pages/traits/metabolism/has_nacl_delta_observation.html
    sha256: e2634f2a9eeb3a13b61c014d50fd5f9bd076c8f56d6ffb70c11fec6454111778
    role: context
  - path: pages/traits/metabolism/has_nacl_observation.html
    sha256: 60dc2f91d980113bf20502cd51dc3b342d3f09dc3f1da5edfe2101db44487e0e
    role: context
  - path: pages/traits/metabolism/has_observation.html
    sha256: 6eddae398927b15b98970672e1074a9debd7204cc61a971c24cb866dd2ac20d0
    role: context
  - path: pages/traits/metabolism/has_optimum_nacl_observation.html
    sha256: 86749d5b612732348e196b1e3958b413c6b0c7a2f251db444a28022aa74391a7
    role: context
  - path: pages/traits/metabolism/has_optimum_oxygen_observation.html
    sha256: 99cb6d976cc0d9319db585dcb54b34df9113350694528f05ae5fde60873286f7
    role: context
  - path: pages/traits/metabolism/has_optimum_ph_observation.html
    sha256: cf0bb890799f18daf838f94bc9c62394eebfbb281f4a25996da75a4fcf34bab0
    role: context
  - path: pages/traits/metabolism/has_optimum_temperature_observation.html
    sha256: 7a17851a86a4c7e31f89d6f9dec942d83a99aebda83336cc4146f4a9c65ba675
    role: context
  - path: pages/traits/metabolism/has_oxygen_delta_observation.html
    sha256: 5a86fab72c95c8f1f5258696eac8fe9381a50555b86faec35486bf271849936c
    role: context
  - path: pages/traits/metabolism/has_oxygen_observation.html
    sha256: 771385a8bee2585be9156046971929853ccd8074ace0bcbcbdda4b4e6481cbd4
    role: context
  - path: pages/traits/metabolism/has_ph_delta_observation.html
    sha256: 9ada4a3e86ca8695cfb6f215d0395c05fdc7430c1bd0e5876b650e5b57b54097
    role: context
  - path: pages/traits/metabolism/has_ph_observation.html
    sha256: f311918d5b6d966e7a6a70367b33d3f5a2273f38ee3a19ee2948a6a4217364a8
    role: context
  - path: pages/traits/metabolism/has_phenotype.html
    sha256: 59802ba8f61469525b82f60da111b0da72c91406399766fffd13c1db5af7698a
    role: context
  - path: pages/traits/metabolism/has_quality.html
    sha256: 2e2f5909919eadfbfefbddbebd47438b0fc01d4f7146ff8f7f2b1d2941e87d73
    role: context
  - path: pages/traits/metabolism/has_range_nacl_observation.html
    sha256: b82118681a4ece48bc5c38f8b8a2c9db88821b2897eec98605d5b04f7d489ac7
    role: context
  - path: pages/traits/metabolism/has_range_oxygen_observation.html
    sha256: 0536f0a8729d79a955089d1f767dfd751ed35fcab66f4c90e7b1355e5407fe3b
    role: context
  - path: pages/traits/metabolism/has_range_ph_observation.html
    sha256: c0b3e4000959adab816a0c2925634a8e5155f40c2b56eec2300ce2507156807e
    role: context
  - path: pages/traits/metabolism/has_range_temperature_observation.html
    sha256: 407accb15033bdd4c5adee4e1480b7162732f130ca6cf8ad19a5b273f43be917
    role: context
  - path: pages/traits/metabolism/has_temperature_delta_observation.html
    sha256: d9b13523cc9812ede05335df4003c7fcde484566e79285042b71401a45334fed
    role: context
  - path: pages/traits/metabolism/has_temperature_observation.html
    sha256: c9f3e0d6e538e4fb6a4d091f4001a2c6283309d7e3f328aee47bca1b8cbbf414
    role: context
  - path: pages/traits/metabolism/homoacetogenesis.html
    sha256: 90a3c0960fb50ab9633003b21716bfa4c31301eb2944b4451c4e904acd47e7fd
    role: context
  - path: pages/traits/metabolism/hydrocarbon_degradation.html
    sha256: f9c2ec3e311a2d8b9937aba26113254104dc1d0483c0234d710dcf2fe5138bab
    role: context
  - path: pages/traits/metabolism/hydrogenotrophic_methanogenesis.html
    sha256: 49f8c1ef68dd4087a4f2be82a4cde2bc06f0248a8b5704668d38f1652f513f7f
    role: context
  - path: pages/traits/metabolism/hydrolyzes.html
    sha256: 887026d43a0b7deaac9bf2b5dc6969b94bfca3a4504bfd4a9c8db01cdc31bfc4
    role: context
  - path: pages/traits/metabolism/imports.html
    sha256: 6d0d81419738211406293d199749db2254cb7a24b120a669a42f240112fd9e83
    role: context
  - path: pages/traits/metabolism/iodate_respiration.html
    sha256: 0aeba273b6892df61a9fee27019f6e2b9f5791e0254009f5f4cdd84c9a7f4390
    role: context
  - path: pages/traits/metabolism/iron_oxidation.html
    sha256: f30bf2d7681296d47eec25c500c228d785152045be61c068156014e88bb36234
    role: context
  - path: pages/traits/metabolism/is_not_required_for_growth.html
    sha256: 995e0155c6664a5667dce2e5caadbbe6d4d5d7691443d23cc075abb3370eff9c
    role: context
  - path: pages/traits/metabolism/lactic_acid_fermentation.html
    sha256: 8b61734d4e0c8801b5973966d1a806d570375b980b691d60c509f1ff8bb49178
    role: context
  - path: pages/traits/metabolism/lignin_degradation.html
    sha256: c7ce973247c0333e32924a5cb82a793ba563f5d75f3755e2b2b37ac6e619d0fc
    role: context
  - path: pages/traits/metabolism/lipolysis.html
    sha256: 6d49db221087b55dd7f8c092431ec5ff5cc461152afaa106cc49fa7431e27229
    role: context
  - path: pages/traits/metabolism/manganese_oxidation.html
    sha256: c7fd997ba8540bdd33917149a625d3e9af05e4feb2eb74ae20927e3f6a31cb90
    role: context
  - path: pages/traits/metabolism/metabolism.html
    sha256: 68ee038651491f382f2fffb3d2f8ff9e9ecdad0354f9d82006b1947e375da2ab
    role: context
  - path: pages/traits/metabolism/methanogenesis.html
    sha256: 9537d9351362fc6b5b17849ab4e4ce728fc3232a47d34317b80e5f2f01bc4826
    role: context
  - path: pages/traits/metabolism/methanol_oxidation.html
    sha256: 187a6f77c1d117b564df58b67eccffb18a288282197d95559df88f1c0a6cde70
    role: context
  - path: pages/traits/metabolism/methyl_based_methanogenesis.html
    sha256: 41d911aa5752742fefdc3ea864cefd6e3640743d880b1a5525fa37a70b96d6ef
    role: context
  - path: pages/traits/metabolism/mixed_acid_fermentation.html
    sha256: c6fd5679d6332636ee4c5d0f089f844e7020b7a0826ae43e1e51f917bf5d2c63
    role: context
  - path: pages/traits/metabolism/nitrate_reduction.html
    sha256: 534bedc9bb29e0b23ed9aafdf07495bb0f9ab5bba86db44aac1a1a8ae96ef538
    role: context
  - path: pages/traits/metabolism/nitrate_respiration.html
    sha256: 615dc2bc84f1574cc945cded845bf1bae9887b86038f141c260d29e8c939ba73
    role: context
  - path: pages/traits/metabolism/nitrification.html
    sha256: 5e85216fa00a58ed31f2693a4df56ec2ef6be79035edac5a1f041a2fec4c4afe
    role: context
  - path: pages/traits/metabolism/nitrite_respiration.html
    sha256: 6e5bf20066105e5ff5077ccd5010bc06852eb26037bf3d2688922cb50f5967c5
    role: context
  - path: pages/traits/metabolism/nitrogen_fixation.html
    sha256: 8bc257824b0964e8a996cfd862792e08e9c5f4c53e8b3201ee9c5819005ee910
    role: context
  - path: pages/traits/metabolism/nitrogen_respiration.html
    sha256: f5f7d5b35a7945e5422d0323660fcc4349995bf325e94269466c3f6e5f0f57c2
    role: context
  - path: pages/traits/metabolism/organism_interacts_with_chemical.html
    sha256: 21649b3ae1116bc1670bdc4c73fa7f7a25ebfb2c5a5cec1b0ce44bea6a28c150
    role: context
  - path: pages/traits/metabolism/organohalide_respiration.html
    sha256: 5922a99dc6faeb88f23a3886b1050fbcdce975e1d137bbea205607e97eb179ae
    role: context
  - path: pages/traits/metabolism/oxidative_phosphorylation.html
    sha256: 6a3afa4b1aeec598bc23ffd3340369e3f6605b9bbd7421394a8471fd93d39559
    role: context
  - path: pages/traits/metabolism/oxidizes.html
    sha256: 5f7fbcb21dea1509a744957e8266e4fda8bb5d2a3a7ac4e6dbdbb5c57a8b73b7
    role: context
  - path: pages/traits/metabolism/oxygenic_photosynthesis.html
    sha256: bd139ff015e7384babd65394d14bfef04472db3a205de48f4c2636d96eee7e0a
    role: context
  - path: pages/traits/metabolism/pectin_degradation.html
    sha256: 5b4350f34eb37cad8d41a829b8667d7cb46b4647e9c3857ad0670efeb7183998
    role: context
  - path: pages/traits/metabolism/perchlorate_respiration.html
    sha256: b578b7267b7f41d58a8b7af470818d4585261cedae11eb13c3551a065845030b
    role: context
  - path: pages/traits/metabolism/photoferrotrophy.html
    sha256: 8001420657d2688f23649e348d615a3e5902c86fe44c74f62f46e4632a6cb887
    role: context
  - path: pages/traits/metabolism/photosynthesis.html
    sha256: 1b26d4a2ebf02c4f6427b77847c5c525754f2317e89e3dbe4090a3b620cc3ee8
    role: context
  - path: pages/traits/metabolism/phototrophy.html
    sha256: 59bb53aa79f715a3550e77db8bafd1c04b61c1b4df9d4792a636b71861fd2b0b
    role: context
  - path: pages/traits/metabolism/produces.html
    sha256: 19509da6f1596fd26ab3721f65f34a877ded4e909a3582a6f297b125fc0ffa12
    role: context
  - path: pages/traits/metabolism/propionic_acid_fermentation.html
    sha256: 1cbd68c44e0613f9be7b30ef5b07b7071aaf6b81da012ad4c0e79bd7dbf800ce
    role: context
  - path: pages/traits/metabolism/proteolysis.html
    sha256: edc539ed019d56c6b6851d121babee0f101631404c8928435b5224f24c17db57
    role: context
  - path: pages/traits/metabolism/proteorhodopsin_phototrophy.html
    sha256: 27d271ef6b76c037b9199dbbb6ff8d86b132d826b78c56f8d565dc0cf776257d
    role: context
  - path: pages/traits/metabolism/reduces.html
    sha256: d23cb35d77fa59c636b72d960f0a6d619e285b4a744f353a972c343bbf04e42f
    role: context
  - path: pages/traits/metabolism/reductive_tca_cycle.html
    sha256: c0b70c7c7cf6067f4217c3141d40d3bb52e24c6c768dbcb359f741da42f1be0c
    role: context
  - path: pages/traits/metabolism/requires_for_growth.html
    sha256: 997c35d76b2c16ae224090f7b70444bdbb85e79e442739a00ec140c96ed99e2a
    role: context
  - path: pages/traits/metabolism/respiration.html
    sha256: e8dc10dadf918d153a6fe7e76cad882c8ae8cd965af16c49be1de9b87d429288
    role: context
  - path: pages/traits/metabolism/respiration_of_sulfur_compounds.html
    sha256: e06ffcc64d80e5795783861d1514986911102d4cc6746d0ce8167488a2850da5
    role: context
  - path: pages/traits/metabolism/selenate_respiration.html
    sha256: 3772b196fe5cddedbc6bf891f12dafb70ce81fbc58ab2f45e9be148ac9cc3559
    role: context
  - path: pages/traits/metabolism/sequesters.html
    sha256: 26b526530bcd0561d9f3fa0fa9d91ba5f2dadb99ab99ba653e2e2bcebdd3b748
    role: context
  - path: pages/traits/metabolism/shows_activity_of.html
    sha256: ce55726ca12f6082ac0b679ed0e0d98245a16402dc6fbe57d385122b986e57f1
    role: context
  - path: pages/traits/metabolism/starch_degradation.html
    sha256: 0a5e2e8878b93394f1299222291a3e83054a46b21fd33381164409df353eecca
    role: context
  - path: pages/traits/metabolism/substrate_level_phosphorylation.html
    sha256: de7ad7fc5fdfccef1902173135831690dd8b78ad8ee6de604898680e57af9f00
    role: context
  - path: pages/traits/metabolism/sulfur_oxidation.html
    sha256: 0daeb3e23994c38bef1942fd8ae75805f68f44739a7cdbbeb09744ecd38ac140
    role: context
  - path: pages/traits/metabolism/sulfur_respiration.html
    sha256: 8cd39763d84a28c1d34c7182601952ee55acad0a675d3fc99968bd175d4f3531
    role: context
  - path: pages/traits/metabolism/syntrophy.html
    sha256: ecd88387adb486c88e509726d57d9d3b362f406824eea1406a4591130242c1ad
    role: context
  - path: pages/traits/metabolism/tetrathionate_respiration.html
    sha256: 54a864a650beccc2b5e0902d2f2237f2596fc91372981a51f04e13aa79bc175e
    role: context
  - path: pages/traits/metabolism/thiosulfate_respiration.html
    sha256: 121f2413296a01cefe4ef1948a504f1fd3e991c9e4960a968cb2e7b74000f2a1
    role: context
  - path: pages/traits/metabolism/three_hydroxypropionate_bicycle.html
    sha256: 04ecc690be98b12d16f898215bd4bd6b326cf05a4d9f73d118282d928f9a885a
    role: context
  - path: pages/traits/metabolism/three_hydroxypropionate_four_hydroxybutyrate_cycle.html
    sha256: de4ab67b50e650cf1c1355f0d868696a00e36a52f88a1161cc874410f82db333
    role: context
  - path: pages/traits/metabolism/transports.html
    sha256: b13283094dce94027b6f027589a33914b2cb100dd3dd6428b7c62e44bb640189
    role: context
  - path: pages/traits/metabolism/trimethylamine_n_oxide_respiration.html
    sha256: a891a2dd9701040beff3b0eea30b6375c098210a1141857b8b06e3d74b5cfb36
    role: context
  - path: pages/traits/metabolism/uses_as_carbon_source.html
    sha256: 322042e4700cc281ea406d237d6bda8d2d1103f924407780e32889fec0d94d0d
    role: context
  - path: pages/traits/metabolism/uses_as_electron_acceptor.html
    sha256: 8d7bcf462879558be0db3ab65bc05b6204091efb7082ce77273ad01a1f6e286a
    role: context
  - path: pages/traits/metabolism/uses_as_electron_donor.html
    sha256: 8ff4e21b095bf9d37d48386f6c6976d6dcaa00eee88e1f079973dad47bd9b5f7
    role: context
  - path: pages/traits/metabolism/uses_as_energy_source.html
    sha256: c00e522c4b54fc312fc7854cf99fcf31683d65707eed447a9c7911e7f910e4cb
    role: context
  - path: pages/traits/metabolism/uses_as_nitrogen_source.html
    sha256: d41634a24634f8fb89ff3b99bcdd6ef9d421dd61d6ceb5dbc00eac5f7d28e5f7
    role: context
  - path: pages/traits/metabolism/uses_as_sulfur_source.html
    sha256: a011b87e909940b36c6bd1dec9ce2506042a2df63412eb01cc8aef0e267ae7ab
    role: context
  - path: pages/traits/metabolism/uses_for_aerobic_catabolization.html
    sha256: ff846770742c397ff6314ca6207630f03f52b339e478cd663da7b63b6b4c67e4
    role: context
  - path: pages/traits/metabolism/uses_for_aerobic_growth.html
    sha256: 8e1c2118e8fa11c6400816ee749421c5654b7aa0bb6dd2520a0e0c7d76e6315e
    role: context
  - path: pages/traits/metabolism/uses_for_anaerobic_catabolization.html
    sha256: 389835928e2f7c155c9e8d98d22a0e587e83541c40d8a1f49a35e7a1ebfeee9d
    role: context
  - path: pages/traits/metabolism/uses_for_anaerobic_growth.html
    sha256: 8b02d595f3101c76d910aa22a1e62b224f0e81560012d4603e89307a3d2f3db1
    role: context
  - path: pages/traits/metabolism/uses_for_anaerobic_growth_in_the_dark.html
    sha256: f7f7b7fb4c1a2cea30012a275c6ed1b85f0ac78b3f4f7f1750e16d90689cfff7
    role: context
  - path: pages/traits/metabolism/uses_for_anaerobic_growth_with_light.html
    sha256: f78b0337db70f3b4e531563417919c348afb91a14615304e05100cb615edcae3
    role: context
  - path: pages/traits/metabolism/uses_for_growth.html
    sha256: bb58feba832158ddbacf40e3c3ac4fd129677e31489b7b353f8d2b81b4082415
    role: context
  - path: pages/traits/metabolism/uses_for_respiration.html
    sha256: 2e42cda64245ade336d956cc2b3392d0ad9391331642006c0dbdff8e41d0ad39
    role: context
  - path: pages/traits/metabolism/uses_in_other_way.html
    sha256: 31adc7951a0e071efb5d1c3f06d9b94e5b136942571ff40da38f98b43867028a
    role: context
  - path: pages/traits/metabolism/wood_ljungdahl_pathway.html
    sha256: 56765c649943b8efaba30e6de8efba50aec278ffe0e157a2fdd8968bedcbfa50
    role: context
  - path: pages/traits/metabolism/xylan_degradation.html
    sha256: acac206fb901e7b347b04cd94be08eb9f53af3f51119004fb6ec93269b611a2d
    role: context
  - path: pages/traits/morphology/akinete.html
    sha256: 15dff4093b4382f9b908a3a7da97b07edb48caee0e45d4148298acc6fd93f2c3
    role: context
  - path: pages/traits/morphology/amphitrichous.html
    sha256: c90cea21dc50f3bd383128bf3486fddcc57870bc8a47d1cd1e60afe021ac9313
    role: context
  - path: pages/traits/morphology/axially_filamented.html
    sha256: c3576dc81dbbff470a56f11c9fd35abe581d8ff46169ab710bfab46625a8d3e4
    role: context
  - path: pages/traits/morphology/bacillus_shaped.html
    sha256: 134af472e531700c9614168ceefa1036ad57e935d06cd51caac2299290f2bdc2
    role: context
  - path: pages/traits/morphology/baeocyte_formation.html
    sha256: 0cafae4219ad5d18e946dfe57e4dbd4c8090b0f902d5fbdf85145b86be944246
    role: context
  - path: pages/traits/morphology/black_pigmented.html
    sha256: 5a00645f4570cb352de7884d9beff1e7d946904a2ee68d48ae4a2216f7726b77
    role: context
  - path: pages/traits/morphology/branched_shaped.html
    sha256: 2aeb5d21dadc56ce909ed447780a8e842d427ac048a897d44de65aadbc5c3d16
    role: context
  - path: pages/traits/morphology/brown_pigmented.html
    sha256: 26250625e1601b2c0d2df898804cf49ed4d1346a4f3ee6c90cd5b79bd5c88235
    role: context
  - path: pages/traits/morphology/capsule.html
    sha256: 413b39b92a733cd9847b13db346cffbd8713f4056e05aa51fd28fb7ff7db0065
    role: context
  - path: pages/traits/morphology/carboxysome.html
    sha256: 4a48364877787741c79a8341a1a0561afc3b3646debd9a42cc2175e4c11842d9
    role: context
  - path: pages/traits/morphology/carotenoid_pigmentation.html
    sha256: 3bbf8619ea0329e216690e6786c0cbe304666d8e32ff55a68b7a13424f33702e
    role: context
  - path: pages/traits/morphology/cell_length.html
    sha256: 82248a964d541a94ed925e9ce49cf113cd6e5e32cb36850f6fd025c0151265b3
    role: context
  - path: pages/traits/morphology/cell_length_large.html
    sha256: 32bcdcddccd4ac287e0f1bee590eb0b6d3cb083b2c99a42d26e6d027f0cdb8c4
    role: context
  - path: pages/traits/morphology/cell_length_medium.html
    sha256: c39ff1db7a5e32fc33832d35026e031c67f556b79c63b36414a474223311d10a
    role: context
  - path: pages/traits/morphology/cell_length_small.html
    sha256: e7df78c8e471419aa9d1aaad519ebe0f1da7cadd935aff76c9e6b239593cf4aa
    role: context
  - path: pages/traits/morphology/cell_length_very_small.html
    sha256: 7caf16fc07a6f8e9f49e3c71c865be5e6f6d589b265e06a39b7748939bdcb075
    role: context
  - path: pages/traits/morphology/cell_shape.html
    sha256: 4b2181e9b8c623854322864975439dac5267438d7a3705d9c76ff42717aeb748
    role: context
  - path: pages/traits/morphology/cell_width.html
    sha256: 6feb24fac2202b5f81352e8ebf56bf88cd5224fd1d54c4e3ed9921f288e7adca
    role: context
  - path: pages/traits/morphology/cell_width_large.html
    sha256: daf3075d62e2ad29635938b4b5c4524246656ae0f2e946b47e1368cdf1aeb338
    role: context
  - path: pages/traits/morphology/cell_width_medium.html
    sha256: a5033d64114d527f74080214da359881cc7f0e0d59382b640ba9070f6b07f2d7
    role: context
  - path: pages/traits/morphology/cell_width_small.html
    sha256: 97a0754c8bed677a00930d826a9d9d28b07a6f6b2f368153c3eb83a8a46048c9
    role: context
  - path: pages/traits/morphology/cell_width_very_small.html
    sha256: 4bc3354888b8ed5b18341534af2588c76ab7e71915d51f0bd397726ef62f9891
    role: context
  - path: pages/traits/morphology/coccobacillus_shaped.html
    sha256: 9c219211880ecd7b37a752c95a4b9220ee339d6cc05ab12809897aa6d4360956
    role: context
  - path: pages/traits/morphology/coccus_shaped.html
    sha256: aefc349388ee8227312fccf01355ccce042230d557727d05fe69ff8815b95054
    role: context
  - path: pages/traits/morphology/coenobium_formation.html
    sha256: 72a4528352536bd442811985efd0c82857adba18a0719cdcbd0204b29b07d287
    role: context
  - path: pages/traits/morphology/cream_pigmented.html
    sha256: 7b47de62452d08765e742aca3b847910e80a3f0df9574cee835f53c5d7c0415f
    role: context
  - path: pages/traits/morphology/crescent_shaped.html
    sha256: 1911714bfe592176bea473943ddee7eb1308333ff2ced2ee58b387af4e34a621
    role: context
  - path: pages/traits/morphology/curved_shaped.html
    sha256: eeb8dd500cff950d27f31008aca5e1b14ade2a766d7e1f2aff970889013edba6
    role: context
  - path: pages/traits/morphology/cyanobacterial_multiseriate_trichome_formation.html
    sha256: dbfe4ed5b0c935b0dc51f4b91ba2cd4524215ab03b61444dff6226aa813fc35f
    role: context
  - path: pages/traits/morphology/cyanophycin_granule.html
    sha256: 9c039f0ddeafe7fc072f599ce5925477a2c049b33938d250f3978abd4a4813ad
    role: context
  - path: pages/traits/morphology/diplococcus_shaped.html
    sha256: e3898a97e56feaeba0192bfafb4c68002306c4ccaeffc050e3c1f25aeebe14d6
    role: context
  - path: pages/traits/morphology/disc_shaped.html
    sha256: f983184c374288247a3ec917753a90bf56f3af30107aff38554e1e05a0b798d9
    role: context
  - path: pages/traits/morphology/dumbbell_shaped.html
    sha256: a1699c569d10b7bad9369454135f4b3d8d9fa970d39a891231a596dfdb98d8d3
    role: context
  - path: pages/traits/morphology/ellipsoidal.html
    sha256: abb882655c2fe35869171a34e449a74f325b77a8f6b41f9ab752a8fe5de634bd
    role: context
  - path: pages/traits/morphology/expansion_driven_sliding_motility.html
    sha256: 2a28cab4e19be77bf88fb5088756771455dcd1e82c726100518a0edd76ba82f6
    role: context
  - path: pages/traits/morphology/false_branching.html
    sha256: 75848bc8103125404b44530ab2b39b38a2f592dffb3fd3cafeeacc99076ae0dd
    role: context
  - path: pages/traits/morphology/ferrosome.html
    sha256: 47187f703881fdc2fbee23cbd194f8661894339ec2a6485c82a1320992485955
    role: context
  - path: pages/traits/morphology/filament_shaped.html
    sha256: 3a89efb9ef053b499a52e8e7c8a1605dc1a005c5cb46668718cc47fe4ebfc9d3
    role: context
  - path: pages/traits/morphology/flagellar_arrangement.html
    sha256: 4d06e6d5a5f291aa0c5cbf0f235aef2c6fc10f55f0f0f05aa5037f327a0380bc
    role: context
  - path: pages/traits/morphology/flagellated.html
    sha256: 5baf7e8197fc39012261e98815e88de6639d7a2953b402756357959f3a5d8223
    role: context
  - path: pages/traits/morphology/flask_shaped.html
    sha256: 35bef1e8ddca532e1507e228a3c0693729bd1321d709abeaede4dda9d656e8e0
    role: context
  - path: pages/traits/morphology/fungal_adhesive_column_trap_formation.html
    sha256: 13806e32415c607ea197d414b7d363a26009585c6f53446c5903d20d5c0c4e5b
    role: context
  - path: pages/traits/morphology/fungal_adhesive_knob_trap_formation.html
    sha256: 842de2877cb0263d7544e4cbedefb1471250a6aacc4bebeb317d4222b0956f97
    role: context
  - path: pages/traits/morphology/fungal_adhesive_net_trap_formation.html
    sha256: 6ef349fa1acec249c450c42dd218db8d8a8b7963abacd96ae771550cfb41b18e
    role: context
  - path: pages/traits/morphology/fungal_appressorium_formation.html
    sha256: ad42b51dc061e99d9611557fa86106a274fb6339f6dc66cab55d1fb87b0a0136
    role: context
  - path: pages/traits/morphology/fungal_arbuscule_formation.html
    sha256: 7c99fa2541f70d622ed51f688f823ca2aaef4b2284769bccde324ff57e86589c
    role: context
  - path: pages/traits/morphology/fungal_auxiliary_cell_formation.html
    sha256: 7512fa401549d0aad99909d54107de552a2bce34730c430f942e80a8cb2fc9fc
    role: context
  - path: pages/traits/morphology/fungal_branched_absorbing_structure_formation.html
    sha256: 48ee1dc59be180a7af486a7f663d05a47e9b94bd4ab68bbfbe56f6b9b4ff0e5a
    role: context
  - path: pages/traits/morphology/fungal_chlamydospore_formation.html
    sha256: 92f2eda9d1c189fb7219c0c748b6f7e94a0d1b25ea9fc0e8ebabfb3c0f754689
    role: context
  - path: pages/traits/morphology/fungal_conidiation.html
    sha256: fc45d8a5e6aae60f02d84d61aae4cfb06a040887f6382a5ad0fa669b03287337
    role: context
  - path: pages/traits/morphology/fungal_constricting_ring_formation.html
    sha256: bb76e289a54811529c7961c07688e458cbf7512cbc900f7a7e56f56efe537ba3
    role: context
  - path: pages/traits/morphology/fungal_hartig_net_formation.html
    sha256: a0ab2148fc7b48425c1d2dd90823e9e73f4d0761d6586f24b4efa83d8bd99488
    role: context
  - path: pages/traits/morphology/fungal_internal_mycorrhizal_vesicle_formation.html
    sha256: 190558192b06e8bdaca393348439eede4a1961edaafe77b0055ff615de84a81e
    role: context
  - path: pages/traits/morphology/fungal_mycelial_cord_formation.html
    sha256: 764f2c5044d6f7ad35695c564a86628b38c02e827095984335b8dce08ba025c2
    role: context
  - path: pages/traits/morphology/fungal_nonconstricting_ring_trap_formation.html
    sha256: 1d894cc5d8484532dd698510d944039cf6ff22c37c91a7c16e69cd2031cd12da
    role: context
  - path: pages/traits/morphology/fungal_peloton_formation.html
    sha256: 127c4e2285916fcf5756139821234eb370ea448677ad50f298a6ab36dea57441
    role: context
  - path: pages/traits/morphology/fungal_rhizomorph_formation.html
    sha256: a83f55c2bbb9f5810f5ab7ac3e832136032b448ad50402e5c9b7e82baf7b4a35
    role: context
  - path: pages/traits/morphology/fungal_root_mantle_formation.html
    sha256: 0be9155f1210686faf95eb41cd8118862b5682b21555a832952c0a7f37c347d4
    role: context
  - path: pages/traits/morphology/fungal_sclerotium_formation.html
    sha256: 42b9f810c283588e51c9e4213ea3a6d2e5ef274be839dc048790efe775ef8114
    role: context
  - path: pages/traits/morphology/fusiform_shaped.html
    sha256: e987c85919c18b9bd76744c8b307b1aeef1d5f307d5c6be43c9be3718dd06c92
    role: context
  - path: pages/traits/morphology/gas_vesicle.html
    sha256: 213cbab7918af0512056602855bf010b1e06fb789230b387511e36dd3edbfa5d
    role: context
  - path: pages/traits/morphology/gliding.html
    sha256: 6da5295d8ec790b53a4e0338bd4c25795c208d131eb34446309e13fad542dff0
    role: context
  - path: pages/traits/morphology/gram_negative.html
    sha256: ca92cece258dc15cb032800b2a97c883a1f915dcea125e623b13d289d6238172
    role: context
  - path: pages/traits/morphology/gram_positive.html
    sha256: 25bff39ba033bedf8c189ad3b2a2590fb3eb1496fe5b3d93860c9d46ac284794
    role: context
  - path: pages/traits/morphology/gram_stain.html
    sha256: 2bd5f486dbeeab76b5a10da5e2070b6bb0cb3ffd7c372ab718f01e6f1673ad84
    role: context
  - path: pages/traits/morphology/gram_variable.html
    sha256: 8d4aee0a94fb9579e705e6643a894f49a5d4703130f10af6709d7fae2aa4ac81
    role: context
  - path: pages/traits/morphology/green_pigmented.html
    sha256: ccda5408d8d3053abca6d0eeca3b285c725814ed383d9155bca742b1aa01a3c8
    role: context
  - path: pages/traits/morphology/helical_shaped.html
    sha256: a5444398470c6fda3aae37562f7d87e6d7a1c417908e3b3b23e2b060f375232f
    role: context
  - path: pages/traits/morphology/heterocyst.html
    sha256: c5f4f8d08b4c41c344f8773f5109fc037275533cee27832f2079a869b1f9dcd7
    role: context
  - path: pages/traits/morphology/holdfast.html
    sha256: 7f0ef11e7944604d36bfd4273fa4966b5886b7b79be49543102cb8f2f5837495
    role: context
  - path: pages/traits/morphology/hormogonium_formation.html
    sha256: 887d5fa228a7bba9f2f881cfc9149f428605417e6b5c6636c274dce57656de12
    role: context
  - path: pages/traits/morphology/intracellular_inclusion.html
    sha256: bc86cbf75c5a86a2fa103d0a20e630d498bb62a055246251ea51dd29d2ffdc44
    role: context
  - path: pages/traits/morphology/irregular_shaped.html
    sha256: 07af918e2c00aab97e2583a6482d3736c527b96173290c93282fdcc0381b9e7f
    role: context
  - path: pages/traits/morphology/lateral_flagellation.html
    sha256: 1c56c858b418ec45cdc42d6d7dbd79477b0308435fa015334cbc0684a9df4273
    role: context
  - path: pages/traits/morphology/lophotrichous.html
    sha256: 0f54a7a7710743020c0ea39dea6cbff657f6b10e9937638da73b980575a96ddb
    role: context
  - path: pages/traits/morphology/magnetosome.html
    sha256: ece8f4f673574b9b71ba15df329ed5e5dbbd8a3481cb35686e0d9ab8d38ddba4
    role: context
  - path: pages/traits/morphology/microbial_haustorium_formation.html
    sha256: 35e535d9d6ec7a2de42dea139d61d2630872eda864c51dc21b3c4f22198fb657
    role: context
  - path: pages/traits/morphology/monotrichous.html
    sha256: 68421fe5205c61054bb0ac85295a19cb5d455b0b8ad28b03741002959a6d4263
    role: context
  - path: pages/traits/morphology/motile.html
    sha256: 0451da601b3ad1c0939b0a23aeecaeb6f31b7836f02aa2df3490d7c98bd71734
    role: context
  - path: pages/traits/morphology/motility.html
    sha256: 196a3c31ea6dbf3f0cdb720e32ec1cb2a34f952a449e4168bb6411cf5b0644a9
    role: context
  - path: pages/traits/morphology/mycelial_growth.html
    sha256: bf49a494b72801be6a644723b9e2bec09c2021a692b08d53fe793ca449a5c88b
    role: context
  - path: pages/traits/morphology/necridium_formation.html
    sha256: ce6e90c7fd6de9760c710222cb85076a5fed50f96f0e7c6a037a34feb0da67f4
    role: context
  - path: pages/traits/morphology/non_motile.html
    sha256: 303006225db6379c1dafe2a6dcefc4bd6fd5e957bc78111d1f71981c37301364
    role: context
  - path: pages/traits/morphology/non_spore_forming.html
    sha256: 01c9f77b09c3e1345a1b1fbb7bd4e429cea7d0b56e1f0605aba21023fe905c19
    role: context
  - path: pages/traits/morphology/orange_pigmented.html
    sha256: 37a65fdbba4353d38a1ae689ee0e9374f1b9d22a7d59946ddd7cb8372b63bd71
    role: context
  - path: pages/traits/morphology/oval_shaped.html
    sha256: 94af8b2e863d155a29b81d330dfdd2aa2ed2afb904fe1110bb70bc1f2cd7010d
    role: context
  - path: pages/traits/morphology/ovoid_shaped.html
    sha256: 891dc508998a4947bc65eb383ef9958d1895716193e1c8c57020608481e2c48f
    role: context
  - path: pages/traits/morphology/palmelloid_formation.html
    sha256: 34f8697ad364264dfc0607fe915aff4d5510092521e12f5932d10380270d8f2d
    role: context
  - path: pages/traits/morphology/peritrichous.html
    sha256: d451582c28798ddee6ee946cf1f1c80b849ccb3862e5b3cd2c986c093bf8107a
    role: context
  - path: pages/traits/morphology/pigmentation.html
    sha256: 2fcf96725fae331995e1c1671467ab820760c83df376ef84f38e18d89a03ac69
    role: context
  - path: pages/traits/morphology/pink_pigmented.html
    sha256: 8dbdc9f9ea34dc7bcdb9ae891e61803d18ebe2c7babce126a81da109464b08e2
    role: context
  - path: pages/traits/morphology/pleomorphic_shaped.html
    sha256: 7a0f256bc9392750ce125ab1fe019431347f7f82aac40d6e7005a53489d1b5d6
    role: context
  - path: pages/traits/morphology/polar_flagellation.html
    sha256: 1da494909074838d7388b27cbd14f62c4272721f707807dc030d1893f47dd017
    role: context
  - path: pages/traits/morphology/polyhydroxyalkanoate_granule.html
    sha256: 5160d5fdbcad9040275154e839423dff567ab0ba7e5e68727e740e528ceb68f3
    role: context
  - path: pages/traits/morphology/polyphosphate_granule.html
    sha256: 67064fbb4b9ff7a7b3553414e6964cd1a6364c2355ee75f8efbe3903c2731c35
    role: context
  - path: pages/traits/morphology/polytrichous_flagellation.html
    sha256: a771886c150359d1fdcbe1650a4f7e8874cbfe72d391eff89c9f9ad8edb8775f
    role: context
  - path: pages/traits/morphology/prosthecate.html
    sha256: 3c91fcd96c11932b189209825f4001aedbfb531cc009e6b0ad3cb39963c481cf
    role: context
  - path: pages/traits/morphology/pseudohyphal_growth.html
    sha256: 83e9471a1b675e4aaf4470720d28027d2198c424cfff87ac189cb525cb1012c5
    role: context
  - path: pages/traits/morphology/red_pigmented.html
    sha256: 5b4632561d9a04c2dbc8adcd978eb79becc25d51085df91595c15c9d4f7f416e
    role: context
  - path: pages/traits/morphology/ring_shaped.html
    sha256: 342aeb5f9177a472c0590f18840abb7191c28a4648fe780bf93acbf729dac471
    role: context
  - path: pages/traits/morphology/rod_shaped.html
    sha256: fd9571060848035090ce315cc0a0193a81fe0cda0a511064b9b7a32fc7505e87
    role: context
  - path: pages/traits/morphology/rosette_cell_arrangement.html
    sha256: 288e5594f9272a5330594a8f2f89531a90a08ade5ce2dd8283a7455ea19d3fb2
    role: context
  - path: pages/traits/morphology/s_layer.html
    sha256: 990badaf97457411a06a24d7bf77be9fa6aaf076b0aacd876aff7a5e76d74afc
    role: context
  - path: pages/traits/morphology/sarcina_arrangement.html
    sha256: 832e2a7fbb2f3d60348760277fe8e9e5f3c9edd7b5b09cb1f7cfa79ecff8c945
    role: context
  - path: pages/traits/morphology/sphere_shaped.html
    sha256: 9be594bc9b65d92c8a4aaed21c339f33066ab59f99a391dd182f917451ac6256
    role: context
  - path: pages/traits/morphology/spindle_shaped.html
    sha256: 70add8fd356c2c8110993624f8c516e8197a47e2c56939d3cd5bf1a911bb7397
    role: context
  - path: pages/traits/morphology/spiral_shaped.html
    sha256: 053dac6dc695a519b09f682daa2db74d600f825e66aa2f276376376550fd2982
    role: context
  - path: pages/traits/morphology/spirochete_shaped.html
    sha256: 827e187d738d0545399ebb6853c03db681cb7f49c73cde3f5b0abb6dab4510b7
    role: context
  - path: pages/traits/morphology/spore_forming.html
    sha256: 93dab5c25d4a3b4fbdd79ca7b6ee589246eaf1e8f7fc8c899a1b34ed4ade31f2
    role: context
  - path: pages/traits/morphology/spore_shaped.html
    sha256: 57fa6d5bd241b12ea3106910b0a940e4c99bd93a905dacce586e0922acc1fcbb
    role: context
  - path: pages/traits/morphology/sporulation.html
    sha256: 1ca3ac199b00b1f5d8ec66c2a22b4e3e8932314f207fd95493c2e7e1ac7c57df
    role: context
  - path: pages/traits/morphology/square_shaped.html
    sha256: 5f96216857a9affae44e390f910a868cf2b7d0c786f01da1003a5db00ecd893a
    role: context
  - path: pages/traits/morphology/staphylococcus_arrangement.html
    sha256: e89644302f0672ea179d439a0c6e705f5ba8537874c83f7769cebc6e89466b59
    role: context
  - path: pages/traits/morphology/star_shaped.html
    sha256: 359467ea8a4b3d7e423058c44adbb0f1299c0428373efdf5f60ef3008f5d6b85
    role: context
  - path: pages/traits/morphology/streptococcus_arrangement.html
    sha256: c845d1ec72e453fd17060a3b2755912e359006a50bd9c1465e9f4d4217a1f8d2
    role: context
  - path: pages/traits/morphology/subpolar_flagellation.html
    sha256: f0669f306cab5d2054f2a7306c39c0279d547498ff79fa750409d8a22c1050ee
    role: context
  - path: pages/traits/morphology/sulfur_globule.html
    sha256: add8c2d8a62981b54d16628ae74452a295c57272ebc7349a2acd6a0e27210956
    role: context
  - path: pages/traits/morphology/swarming_motility.html
    sha256: 6772a7053d078cc034057f01c94751d7a7b36547aeebf2092cb52bbb9e3d6914
    role: context
  - path: pages/traits/morphology/swimming_motility.html
    sha256: 339acbe71cf6800249876046e311dd08c0822e4b7a2fcde4b06a6f61c2dbfaf9
    role: context
  - path: pages/traits/morphology/synnema_formation.html
    sha256: bbaf4ba738751d1042f9ee457c6bc754eab233281cc7266e099cb30be3441c4a
    role: context
  - path: pages/traits/morphology/tailed_shaped.html
    sha256: 6448e85c4a8a34384a568a8d64d5bff72d21944cbb4f947996ef86d18fecb027
    role: context
  - path: pages/traits/morphology/tetrad_arrangement.html
    sha256: 63e6aa4127c301650b7087559de3dcec2e4c11900bf774b93da9c16acb028ebc
    role: context
  - path: pages/traits/morphology/triangular_shaped.html
    sha256: 2315350478cc2838af55dbba424177451a9ca544e45a66296d92aa061b8f8fe2
    role: context
  - path: pages/traits/morphology/twitching_motility.html
    sha256: 0155ec2412b775782164c25c52a9aea0bf91e38c5a4185ad4d9115b97b161a42
    role: context
  - path: pages/traits/morphology/type_iv_pilus.html
    sha256: 1eba3b5bf1eb1f89eed87db106efa77e0c17ea075914d00389b887902b67f250
    role: context
  - path: pages/traits/morphology/vibrio_shaped.html
    sha256: 06bf1733e214e2bf326ba8a6a0287306eebf77432e17785a1d93b95694733e96
    role: context
  - path: pages/traits/morphology/white_pigmented.html
    sha256: 221a59d3f7d3b7df9f162525d51e0584d2c7eb771413149d7751e9263d1d1322
    role: context
  - path: pages/traits/morphology/yellow_pigmented.html
    sha256: a19435eba8f41b54363db128cc05dd72e43acad019f6995b7940ebf03f2f6498
    role: context
  - path: pages/traits/observation/growth_nacl_observation.html
    sha256: b5521af8ea052762aac497c871466f48b09221acda9c3bb4136ee5a4caaa68b1
    role: context
  - path: pages/traits/observation/growth_oxygen_observation.html
    sha256: edc589ba42cf510ed16d95175dcf2766d8d4617f5c06901d54e35014d5bc1b71
    role: context
  - path: pages/traits/observation/growth_ph_observation.html
    sha256: b4f000d539b2c14e12c8b4e158cba99c5712e17c64e10e53b8fa47a52307af74
    role: context
  - path: pages/traits/observation/growth_temperature_observation.html
    sha256: 1dee0e77fa756f8b37e29aa34bf2ae705ffb60b3a236470db72c7a95643d14de
    role: context
  - path: pages/traits/observation/nacl_delta_observation.html
    sha256: ea7642d38c29589f4ef429f68f14022598092f4d486323611e9a11a2fd197159
    role: context
  - path: pages/traits/observation/nacl_observation.html
    sha256: dcf1d18a1457a496336c52512cc82ffc55f4f6a0b0547bec6bac22cac740a5b7
    role: context
  - path: pages/traits/observation/nacl_range_observation.html
    sha256: 0415750c0573d9b963bb2d60683b1d5dcd43ab577e7df9d830360752f9a508d8
    role: context
  - path: pages/traits/observation/optimum_nacl_observation.html
    sha256: bb6c6740436df8238012bfea9c15b1a6d7d882e860869b747e558cb4c2611300
    role: context
  - path: pages/traits/observation/optimum_oxygen_observation.html
    sha256: 17de6b24ad26c7f39da76e561e1a75597a465375d533a01ebb682eb2416ef12b
    role: context
  - path: pages/traits/observation/optimum_ph_observation.html
    sha256: 7319b2a46842142a0f3674e11dc0a89749aaec14cd0d4711ff853a7cc99e5581
    role: context
  - path: pages/traits/observation/optimum_temperature_observation.html
    sha256: 33c7cee4b90e567000035f63e3f259ddc4f6c7e9e8acd632ec6e5bbd34b1e0c8
    role: context
  - path: pages/traits/observation/oxygen_delta_observation.html
    sha256: ea1cc7fff1b813de2fbd8ded1a6d2c7549dc2850be42d99ef86b85afc94b4f4d
    role: context
  - path: pages/traits/observation/oxygen_observation.html
    sha256: 596b24790885de7fcfe206652ff4ef928b1e2a091faf5f3735fe5865d815ff7f
    role: context
  - path: pages/traits/observation/oxygen_range_observation.html
    sha256: 317ae67e4336bd2473dcb4ce763ec1ec09e5fdbe603496a3b303adfd7d7a4d9c
    role: context
  - path: pages/traits/observation/ph_delta_observation.html
    sha256: cb42aaa63f254c4f4af87dec11bc82c229a01d4fc795c9335959df53a613823a
    role: context
  - path: pages/traits/observation/ph_observation.html
    sha256: 977486732f61c2875ecd1c50b4b46384eb5645b80e16a140d6384abd1fe5e1a7
    role: context
  - path: pages/traits/observation/ph_range_observation.html
    sha256: dce3abef48f8444e9074b86fe3155356cf19121f257530b58b5438f6551edc2c
    role: context
  - path: pages/traits/observation/temperature_delta_observation.html
    sha256: a3a4004cb9ab8583f2a35dc7d54a105efb31f8fb1578577bcb36fa99c12b409c
    role: context
  - path: pages/traits/observation/temperature_observation.html
    sha256: f412fd86f315cfe25011e20ffe1bc5afca8ab648e939b866beaf850a4cc4c265
    role: context
  - path: pages/traits/observation/temperature_range_observation.html
    sha256: e4f4c0fdf261deac68df9856b0527c5b61ca679ddfcc506e333f45c6786124a0
    role: context
  - path: pages/traits/other/catalase_negative.html
    sha256: 3a439dce82427092cd105779c67763bbb7d4732b706ea6626d3cfea929019ace
    role: context
  - path: pages/traits/other/catalase_test.html
    sha256: c816c94c93cffc4864c4977420ef926ab527a542ddba28ca5cd955064ba973de
    role: context
  - path: pages/traits/other/circular_colony.html
    sha256: d087c83968dd13e84808cc0708a82d752d2d6c5e7a0e6a1fd2b1db341f25977e
    role: context
  - path: pages/traits/other/coagulase_negative.html
    sha256: bc16b7b108da3ff3389c38c676d3ca54149aa477bbab4dee6a558cf2dcb39050
    role: context
  - path: pages/traits/other/coagulase_positive.html
    sha256: b03b557cd2cc5105f0917e0fef845165fe5c3b6720b91e5574c2ebdccef42431
    role: context
  - path: pages/traits/other/colony_morphology.html
    sha256: a9137d854e894cd6a8b2cd559ff5d8f9e8ec7b2ae7c739128ac774afa2dc85db
    role: context
  - path: pages/traits/other/colony_shape.html
    sha256: c173fe1ede0abc7d7f53fa56a9fec530f259fd25ca34b0b3a6f01e5a07e4a73c
    role: context
  - path: pages/traits/other/epibiont_phenotype.html
    sha256: 4cba1da90af67d5f22bb57183e2c87b30b623b98218a0f6a9b8e4455991f542d
    role: context
  - path: pages/traits/other/filamentous_colony.html
    sha256: 8bafa57c08526e05ce831c77becaea99c2ae6e5d42d28e07db5ae09c7628c585
    role: context
  - path: pages/traits/other/fried_egg_shaped_colony.html
    sha256: 1dd04c75e88e3954edc0de81ac41a645a7a9e919273126b806fb224f238c0088
    role: context
  - path: pages/traits/other/generalist.html
    sha256: faf36bbf6441e7caaf80f93381aec8db91644f9bc156f0d86488b6a6dc4692eb
    role: context
  - path: pages/traits/other/hemolysis.html
    sha256: b74c20d26827eda1c4edbf0d28fee6452cf97fb447a26ceab7f89c5083e4d22b
    role: context
  - path: pages/traits/other/hemolytic.html
    sha256: c9d7b54d84efb48c0dbf6be076909ad6442977f93539822b95e02e9fdb2fb840
    role: context
  - path: pages/traits/other/indole_test.html
    sha256: 7b514a979e8d47a7763094ddc50e8c32ba6acd67b6418fa6fb73973ee5bd63c2
    role: context
  - path: pages/traits/other/indole_test_negative.html
    sha256: e03f3765dbd884291aa05309a10e2d709b3894fbb04cfd7f82f4de109130b5c0
    role: context
  - path: pages/traits/other/indole_test_positive.html
    sha256: 83d54fe97e3f26345ef80f7685a4cbc4a8ffc6ebe560b61a5894dde9e8fac105
    role: context
  - path: pages/traits/other/irregular_colony.html
    sha256: e7d5b68900d0ccaf557a06b68de7624eed0bb17120e1c1b04bc224a90b40a6b1
    role: context
  - path: pages/traits/other/methyl_red_test.html
    sha256: 93e2b63e1118e0b5ce47edc80ef5bf5fad4bbb38a2bf6ddd1f9c7b384847a2fc
    role: context
  - path: pages/traits/other/methyl_red_test_negative.html
    sha256: 842d8323a8cc9e895ed356c87965eaf7064318286970def62f92f47faddc5d0f
    role: context
  - path: pages/traits/other/methyl_red_test_positive.html
    sha256: 9112d33a4b0269a4db90879e4c2a460b79f7ea0956ee7f9818b40eb8a473924b
    role: context
  - path: pages/traits/other/non_hemolytic.html
    sha256: b3eca199dacdd81054bd809375153d3cfa1c1bff1b940a614043c8e423c59b42
    role: context
  - path: pages/traits/other/osmotic_tolerance.html
    sha256: 8a49be78879f920f9c5b19c6a79f06ee80c5b9b3185f1f89eaf584c0629eec81
    role: context
  - path: pages/traits/other/oxidase_negative.html
    sha256: 6e3db76d892bb5469d70de5a5854265ae134fffdb8a9631e34fd995c58d257fe
    role: context
  - path: pages/traits/other/oxidase_test.html
    sha256: 3ec006f10bdcb35b5b0362908fcdd3f5e3eff9e4d0b3bd01bd746800d8e8f86c
    role: context
  - path: pages/traits/other/punctiform_colony.html
    sha256: 3d88542455ff3d882bf9e53e4beec6d588831e79d882f77fb6a15b4d9b9c432a
    role: context
  - path: pages/traits/other/rhizoid_colony.html
    sha256: 2015a2ff7211cf670eb316a6207a2280ad332628e540ce29549a0b9e0da3041b
    role: context
  - path: pages/traits/other/specialist.html
    sha256: dbeac88113caf0e92f4933adb0bb048804547fe8d533f8989766833da6741ee2
    role: context
  - path: pages/traits/other/urease_negative.html
    sha256: 28eff020d306dd34e12a4646f7f7a7d73a4d68ca0d1b164fa90b0866655e08a4
    role: context
  - path: pages/traits/other/urease_test.html
    sha256: 7bbc2944e85f55df6459c55309279d4c81a8f7e90e43a2dae4dbabce534c6379
    role: context
  - path: pages/traits/other/voges_proskauer_test.html
    sha256: eb2cf953a8cdda9d29eee7e3909b84b498ed610487abeca2e0482c08e0fff65b
    role: context
  - path: pages/traits/other/voges_proskauer_test_negative.html
    sha256: 6904b8a3e968a7879efc6209a2e566fd98e0cff13789f0100f7e9fa4b3b0291d
    role: context
  - path: pages/traits/other/voges_proskauer_test_positive.html
    sha256: 0bc67e0cb6b96f4c3fc451d05ace3a8ae0bb0404ffe81664bf851da58cdd13cf
    role: context
  - path: pages/traits/physiology/acid_phosphatase_activity.html
    sha256: be3b035475af06d634615da417ca0f855d437d0470a1203635413fdb719560e9
    role: context
  - path: pages/traits/physiology/aerobic_anoxygenic_phototrophy.html
    sha256: 291059fb074ec236a596adb58503f24a5b5616549618c8968044588ec728a9c4
    role: context
  - path: pages/traits/physiology/aerobic_overflow_metabolism.html
    sha256: 8e79efc8c7d4200882382b57a57ffbd5d67845a19edb44c0edebcee1f5908d66
    role: context
  - path: pages/traits/physiology/aerotaxis.html
    sha256: fe7f82cafdb1954d14bf5b2c229d863304fda7fe16c779cdab8181ea3cd346c6
    role: context
  - path: pages/traits/physiology/aerotropism.html
    sha256: 1e4dcec621cc5d73a31b8b21f4f82094fb87222c1ace6a1ca9c25673e702e2fa
    role: context
  - path: pages/traits/physiology/aggrephagy.html
    sha256: 91bdb3773103d7f59dd17f4a9e820ebc4a662350aea5c3682d829cb4e5e5aaf0
    role: context
  - path: pages/traits/physiology/alanine_arylamidase_activity.html
    sha256: 8164770a712217d01f245f8f7160be74d828b4357dd690fa0e9c9084a84d0fcc
    role: context
  - path: pages/traits/physiology/alkaline_phosphatase_activity.html
    sha256: 4f1260d688527c33a7441ded7753b88db2f9343c990b415e4e326c4853bc1987
    role: context
  - path: pages/traits/physiology/alpha_chymotrypsin_activity.html
    sha256: 0e49a524f97377195f8144d15eb915da0298ed10fea8c5a41f72418c3c8e894c
    role: context
  - path: pages/traits/physiology/alpha_fucosidase_activity.html
    sha256: ac08eb9735a6d1a8c47c008efe9a2ff0d3dc4e51a01fdc3c941f23e4fb3e5878
    role: context
  - path: pages/traits/physiology/alpha_galactosidase_activity.html
    sha256: bd0d0f6b736f7df642b919e18833b64d66c4b5d4167cc3972c332358943de5b1
    role: context
  - path: pages/traits/physiology/alpha_glucosidase_activity.html
    sha256: 71a3572a8b8cc0eeff1046f89e7de0a95fbb3f9ce0157b9f41394c14d9699745
    role: context
  - path: pages/traits/physiology/alpha_mannosidase_activity.html
    sha256: b65efc5896243a4e08323b21ffcd7b0f79ada5f08c8c628d817a8c7cf274a2a5
    role: context
  - path: pages/traits/physiology/amylase_activity.html
    sha256: 14b779ac41ad2315dfef888d950a2bee7a0da77059c18de7fd6e4d2c376b7249
    role: context
  - path: pages/traits/physiology/anisogamy.html
    sha256: 365ebe7fbf8b1070c72c182df756c43be6eccf8122324e42b575cdfcf8dd116a
    role: context
  - path: pages/traits/physiology/antibiotic_resistance.html
    sha256: a0d3108005c7add850c02051a5ce5eecff9ee77a681498eb73ea01400ced0abc
    role: context
  - path: pages/traits/physiology/arginine_arylamidase_activity.html
    sha256: 3a9d0357445d00ce61befb130912c3b70fbb1628678802435022bb1d3a6c9f31
    role: context
  - path: pages/traits/physiology/arginine_dihydrolase_activity.html
    sha256: 6d1a6af1fd7d0a475be216ee0d9091a130cbd77a2fa6ea2246aa22f0ee11413d
    role: context
  - path: pages/traits/physiology/autogamy.html
    sha256: ef32164c63bc302a7add1416df373837a5e870daf92cc97f0952dbc70b512c8b
    role: context
  - path: pages/traits/physiology/automixis.html
    sha256: 0ec4078513e2580e4576298e0ab99703a0b3fb9184b091ac4fa584693cfc0eea
    role: context
  - path: pages/traits/physiology/autophagic_glycogen_degradation.html
    sha256: f8fb8ba5e8099aa1c9b3f5992f0bf362fce89023a57a212849e6c5d372d8eb97
    role: context
  - path: pages/traits/physiology/autophagy.html
    sha256: d3ded067c60879d7e860e7bb1aa1dd1c25deafc9ce1fa1d33aba686719153432
    role: context
  - path: pages/traits/physiology/autotrophic.html
    sha256: e5f2225f77c727c2809d859461a82c13d8f7ae1a8db805a6f0e8524356311e32
    role: context
  - path: pages/traits/physiology/bacteriocin_production.html
    sha256: 23229eb9b9c492e3678f863077b843af8fd1ff167393ae6389466e53036d059e
    role: context
  - path: pages/traits/physiology/ballistospore_discharge.html
    sha256: f479f06ee9d3b8ab9b4d654a01c1f31923870b414e7fcc7e594185827ce5a189
    role: context
  - path: pages/traits/physiology/beta_galactosidase_activity.html
    sha256: 25163c9203b716c891e00d7848d1f5214dd6824e6b60781a94944aa7cc0f811b
    role: context
  - path: pages/traits/physiology/beta_glucosidase_activity.html
    sha256: b25042c19fd4634154a79bca0bb733d1dd657b655350e83defae98ed1120c9b4
    role: context
  - path: pages/traits/physiology/beta_glucuronidase_activity.html
    sha256: 1dfd8953aeaa6593446d97a198682ec13e3f74ad81ef2f0f29ad5b7d5cd4a835
    role: context
  - path: pages/traits/physiology/beta_n_acetylhexosaminidase_activity.html
    sha256: 3ebdabbaa922bd12b76aa4ef66d6d826a5e2a4606ef54a125181b90b9fc1e53e
    role: context
  - path: pages/traits/physiology/bioluminescence.html
    sha256: 296c3979a72e64e0dae386e7c7c70c2fff984e07711b5d44089845cdda995a06
    role: context
  - path: pages/traits/physiology/biomineralization.html
    sha256: ca7663a1a97e2cc0fcc5638ce3b105624d9eb9efc4e4734ae0e638961dd22a77
    role: context
  - path: pages/traits/physiology/bipolar_mating_system.html
    sha256: ab428bbc2765db4c725a63d09ee63ac550abecee5b38e87e253983f92409c8a6
    role: context
  - path: pages/traits/physiology/carbon_source_memory.html
    sha256: 8e6f068af29f9efa86bb3c0b9d837dec4a99712055a8245784081123957399a1
    role: context
  - path: pages/traits/physiology/carboxydotrophic.html
    sha256: d44ec7bbd2f4085866949caf43f5bac000e97b3deeca5e387e11a1979ef3488e
    role: context
  - path: pages/traits/physiology/carboxylesterase_activity.html
    sha256: b120d83eac9ede32625d7a03900f7b3f0e98c71b00b7ab18033b0bae845d144a
    role: context
  - path: pages/traits/physiology/caseinase_activity.html
    sha256: 88836460d170f00f42dd090ea97d9b6e256c366c4e567cfebca08c24cdc09fb3
    role: context
  - path: pages/traits/physiology/catalase_activity.html
    sha256: 6f54b53f72cbee8f2643e9e46a33995e7aa1f066676a1f1f6e401c48f974ef7e
    role: context
  - path: pages/traits/physiology/cellular_buoyancy.html
    sha256: 0b6a06d532e19b10bb6fd9d9c8b0014a193751fe83ca944ce95ba4bc37fd1f49
    role: context
  - path: pages/traits/physiology/cellular_rejuvenation.html
    sha256: 197a4620c142d4a00690ad30c07b074f23a056a4d383be245fd27e58e28c8499
    role: context
  - path: pages/traits/physiology/chemoautolithotrophic.html
    sha256: 8f2249bc843e2a9566eaa44abed8c0b76ec43ae38676d06cc410882839e9cbba
    role: context
  - path: pages/traits/physiology/chemoautotrophic.html
    sha256: a439b37e3a8f8cf77ade526e97f1236f23caa00891021e11edb8e3d99cd75be6
    role: context
  - path: pages/traits/physiology/chemoheterotrophic.html
    sha256: 87b67f7b8a8ed43515b53a902b9579dc09f648a6d6b06845b5d0672df051fbe7
    role: context
  - path: pages/traits/physiology/chemokinesis.html
    sha256: ff2a9f597be0ee7435ce635b50f91be50b5475a43e549c7d8640098eccb7ab82
    role: context
  - path: pages/traits/physiology/chemolithoautotrophic.html
    sha256: 6a688dff7f7a37991f2dc6f47cce8a95b0da41093c518399a9846fc351b9f933
    role: context
  - path: pages/traits/physiology/chemolithoheterotrophic.html
    sha256: 98de1f5248fe4bae20e284929dc05eea78b02490bd89714592e6aa35be6868df
    role: context
  - path: pages/traits/physiology/chemolithotrophic.html
    sha256: ca957ba594ef66b2fdee1eec5d8cac4b8cf6b277ddd881962ef9ed9ac5558e27
    role: context
  - path: pages/traits/physiology/chemoorganoheterotrophic.html
    sha256: 9c2e936357273f9d224840e69f29fad65254cadce9f887f57e54d7c184e7732d
    role: context
  - path: pages/traits/physiology/chemoorganotrophic.html
    sha256: d40c673797a85f9a4a2d075f61942ba5ea21d64334c4f66f6ba95ac4bb1a4a47
    role: context
  - path: pages/traits/physiology/chemotaxis.html
    sha256: c4bd59de3c1690d98bb0ca99654ce786e8b10429af669cff08ee0019cceb7a33
    role: context
  - path: pages/traits/physiology/chemotrophic.html
    sha256: eb924cfc326aede1d1de79e4a6cff6d4858ced6d603041757d0b975c3899e5ae
    role: context
  - path: pages/traits/physiology/chemotropism.html
    sha256: 88b8ee59e277fc185377fa403d7aed01ed4e1d06fbd7b211538a5d99f09efb54
    role: context
  - path: pages/traits/physiology/coagulase_activity.html
    sha256: b0512d0a624ba7c290ad9a1f085f0e8dc3d9b8f2e164ee281964ed8925115816
    role: context
  - path: pages/traits/physiology/coccolith_production.html
    sha256: 4b389096d10545116b80c35130f229efc880310da298dbd53f103e9174137d63
    role: context
  - path: pages/traits/physiology/cold_shock_response.html
    sha256: 35986f5272e257aa66cd0fd9b0e29576d4e31cc3bcb2c86d504ea60a406a7e51
    role: context
  - path: pages/traits/physiology/contact_dependent_outer_membrane_exchange.html
    sha256: c17b0002b31a7903eaca8a35b2adbefa0c4fd73d56fd270955866f661dd1b979
    role: context
  - path: pages/traits/physiology/copiotrophic.html
    sha256: 4bd2a5406f6db7fd41692f7f756adbfc8fbde69fbaae78ecf6beda68a99545ee
    role: context
  - path: pages/traits/physiology/cue_triggered_environmental_anticipation.html
    sha256: a33b0d0b0028b092dcebd44339853ed1a28715d18e819b1ee2da8914b22b388a
    role: context
  - path: pages/traits/physiology/cystine_arylamidase_activity.html
    sha256: 1a3390638b5de012804a8ed25c4d4791cc62ea17ee6581e3aebde96357b0c061
    role: context
  - path: pages/traits/physiology/cytogamy.html
    sha256: 720c2e38603de2bf62002ad910a8e19341a3872e3418c0f941f636bcab2d0572
    role: context
  - path: pages/traits/physiology/diatom_frustule_production.html
    sha256: cd0e75916954bf3cece303eed5634ecb753e0c86e62e0b9d8a889fd96d85d8a7
    role: context
  - path: pages/traits/physiology/diatom_perizonium_production.html
    sha256: 33ca38a165202fa09b610f4b31ac59ae336194af763b218b7a4a53cb54c630f9
    role: context
  - path: pages/traits/physiology/diatom_seta_production.html
    sha256: 65c934fc143db90ce2fe81ccc9fd58786da70f555da8bbeac6badd9e12028998
    role: context
  - path: pages/traits/physiology/diauxic_growth.html
    sha256: 3b50fdd20928c710f390b91a977d0805979b31971345b9a17c0b8948e0b6f052
    role: context
  - path: pages/traits/physiology/diversifying_bet_hedging.html
    sha256: 576739093e321bbd49751398424d759df73d0435a41bf6bd6ffa07ddec676e56
    role: context
  - path: pages/traits/physiology/dnase_activity.html
    sha256: 8a3b140f8b1dbb38a18a76fae6ff1666a1891fb21a7209d19f8e5e20cb4801c1
    role: context
  - path: pages/traits/physiology/dormancy.html
    sha256: a25563c4ae34a9f9e5c1a040a0f53fc45f06ee6eb587d3f190dce6364c89925d
    role: context
  - path: pages/traits/physiology/durotaxis.html
    sha256: 088593905e40ad793f6274f9739fbafa9e4a03bda6227806d41ee508ca543ecd
    role: context
  - path: pages/traits/physiology/endocytosis.html
    sha256: cb93a90b73aee704ef882b0e501b5c6bf180c38af80c1b091c45c9ce0862e72c
    role: context
  - path: pages/traits/physiology/energy_taxis.html
    sha256: 9cb1c00c26b40c88d4ade85f6fc3fb6bea78c4993790ec281c185b434038adf6
    role: context
  - path: pages/traits/physiology/er_phagy.html
    sha256: e9bfd998eb59ae1f8a932f1c13ba9b3443f2095daf04bf6623e8e4e8616df9f7
    role: context
  - path: pages/traits/physiology/exocytosis.html
    sha256: f0e08c113496e9c2486e4b631e53f0c23a467e77af73e698ee7e1a07c0cfc566
    role: context
  - path: pages/traits/physiology/extracellular_membrane_vesicle_production.html
    sha256: 9ef95a5cd079f1b3a966bb848bdfbc63ac4b7d824d8972227e5949577d52fb4b
    role: context
  - path: pages/traits/physiology/galvanotaxis.html
    sha256: 46606982b3584f3bbc21c4106941ee10e1db0832ac04ddf3b7db0d1dc1164f91
    role: context
  - path: pages/traits/physiology/galvanotropism.html
    sha256: effa75cf587f9d57999f0eb5f37f7e811e1a8cad299af5193ebcc0e7969e3fa3
    role: context
  - path: pages/traits/physiology/gamma_glutamyltransferase_activity.html
    sha256: c53348e253dd2ec837c15211bcb7b6a2a780267d9dbb2da0d735ef866173bec5
    role: context
  - path: pages/traits/physiology/gelatinase_activity.html
    sha256: c25fdfd8444a9cfda966ce85ec9e2b54d12de6b5b7755960f89a33b2e7434d3b
    role: context
  - path: pages/traits/physiology/glutamyl_glutamic_acid_arylamidase_activity.html
    sha256: 2836c22223cfe9a5bf0ade74ac368d737fe79b82e5d19b24f3c1a2c520e99dd6
    role: context
  - path: pages/traits/physiology/glycine_arylamidase_activity.html
    sha256: a460263d39f5537d60ecc798328fb8fd8566bc572532d91b5175c2db6754bd5b
    role: context
  - path: pages/traits/physiology/gravikinesis.html
    sha256: 4325f02ab79e662ade7c6667df29d0d26afe65152f4c8df42a73a2e917c9d7a3
    role: context
  - path: pages/traits/physiology/gravitaxis.html
    sha256: 2fb30087fe42c93f53c07e69e5456805dfbd1e54f8c0bc589c2c7170cbd67c1e
    role: context
  - path: pages/traits/physiology/gravitropism.html
    sha256: e6b9e0257658714b41f8045402a72af4660fac4263ec4d6c3b09cada858cec78
    role: context
  - path: pages/traits/physiology/gyrotaxis.html
    sha256: 668d7740b36484d75dffbf98d3c10f31bb73422f90b84bcbb3e00219b692a31b
    role: context
  - path: pages/traits/physiology/haptocyst_discharge.html
    sha256: 17dea579983ed505e6c08d1c929616848c6f273c8843b3840fc711b8e055d71b
    role: context
  - path: pages/traits/physiology/heat_shock_response.html
    sha256: 08bd703022d627cee7ca335ac3f77df018bb04b2a442b5e2ab17eb1d940690fa
    role: context
  - path: pages/traits/physiology/heterokaryon_incompatibility.html
    sha256: 7c674ea69c00f1d508835d95d98d10f6e858e5d69717db49ee0fa21d5ab1de3e
    role: context
  - path: pages/traits/physiology/heterothallism.html
    sha256: 6cddb9a4c0df745623ada659375af74e62757b13b596d82fcd4e93f174f94c5b
    role: context
  - path: pages/traits/physiology/heterotrophic.html
    sha256: 4b61e3509d3d5e5d790878a8daafe7b4cb46fd78813ce08f3b5877005d3d53f8
    role: context
  - path: pages/traits/physiology/histidine_arylamidase_activity.html
    sha256: 16214db542f6e204bb1ce40805447046c2edafdb1b736dbad6eb0425fbf203b5
    role: context
  - path: pages/traits/physiology/homeoviscous_adaptation.html
    sha256: 75195a6d0c1116c0e6e0cf9955bd0d384f46605dd9f97acc2469b90b2c6f0c33
    role: context
  - path: pages/traits/physiology/homothallism.html
    sha256: e7ec8d33640e33f083c65428234a4c4c3e8815a8d5ff71ee8a6b4e553b0b7b2c
    role: context
  - path: pages/traits/physiology/hydrogenotrophic.html
    sha256: 06097cc5b811e184644c849393e889866dca6438fff70670de66ebe076287483
    role: context
  - path: pages/traits/physiology/hyphal_anastomosis.html
    sha256: e2ad41798819ef208c9e9426dac64b8a745f11a54c5aa67aae056692605860b5
    role: context
  - path: pages/traits/physiology/isogamy.html
    sha256: 4256744537d49a2cd9a41ea7badfe3139e6d26ed131df85a23cc69153257da39
    role: context
  - path: pages/traits/physiology/karyoklepty.html
    sha256: f1d6bf04835cbd0eac605b949a9996df6d24bbc0b39a34bd4c98d00487e9e15b
    role: context
  - path: pages/traits/physiology/kinetocyst_discharge.html
    sha256: de12d117c2b5e181fe62fb2ffe776969f8acf739bd1e359c27127c62b5d5301e
    role: context
  - path: pages/traits/physiology/kleptoplasty.html
    sha256: e1607474c1d3bc060eb07ed5f1d00b40cb7002eace8ae6acc65bea7aed9bdfb2
    role: context
  - path: pages/traits/physiology/lecithinase_activity.html
    sha256: 7993c8222a2ff10604502d8f0bae0d987c8393946326b295ae381944bc4e7f30
    role: context
  - path: pages/traits/physiology/lethal_algicidal_activity.html
    sha256: 5e4b5ec043fd53aac52350bc7097064ec8dd3b73bca5e266450afbad641be267
    role: context
  - path: pages/traits/physiology/leucine_arylamidase_activity.html
    sha256: 953176e6e9a29591e12f57af27bc900f6fccc00a7bb1a1861ec38f390ab8e448
    role: context
  - path: pages/traits/physiology/leucyl_glycine_arylamidase_activity.html
    sha256: e42bb7c28e235c8cfb9375c0d302e55206e62238b7eb2be8e2e854c8a5b0258c
    role: context
  - path: pages/traits/physiology/lipase_activity.html
    sha256: fd56d5fb89b28fdc8f7eaf9f93533491eabe8447101cd74c46a396b820f41fd1
    role: context
  - path: pages/traits/physiology/lipophagy.html
    sha256: fea72bc8a6c1bf8c68bfdb79ea964a2b6b53756bfda2229ad69c19795437537e
    role: context
  - path: pages/traits/physiology/lithoautotrophic.html
    sha256: e56aa4bf046e70a2f96253511d680882b2497c6d689bb2941bb135d913782c51
    role: context
  - path: pages/traits/physiology/lithoheterotrophic.html
    sha256: 8bd765d2fbf2d52194bc0015606c65a3515088d3c8a274ecebe0af01c0f758e1
    role: context
  - path: pages/traits/physiology/lithotrophic.html
    sha256: 5da09716d5b817eb2bb9731565afa54f52e9025fcfc0ed9981ee05d7fe0e3161
    role: context
  - path: pages/traits/physiology/lysine_decarboxylase_activity.html
    sha256: 97663a7544a52efbbf0685061377dae05c35991845f53d24e2fed2ed15808ba6
    role: context
  - path: pages/traits/physiology/macropinocytosis.html
    sha256: 45903b87c99edcc8ee06d808031bc065e5da9f2b7b693005683243d0d7fc013b
    role: context
  - path: pages/traits/physiology/magnetotaxis.html
    sha256: c8ab3e6e8679f5f6cb51581a8bfbed3c011b541bc375fedbd139ed512f894a47
    role: context
  - path: pages/traits/physiology/mating_type_switching.html
    sha256: 6399a23a120bfdbcbb03377b3955aa834763319dfd6ea77ccc212c2f638db204
    role: context
  - path: pages/traits/physiology/methanotrophic.html
    sha256: a7bb2c02e04535662ac5e8fea9fcdd60adc4d468e5afe8e56216952fc41dc541
    role: context
  - path: pages/traits/physiology/methylotrophic.html
    sha256: 360fe112314e6cee984a7810f594c2c0324e377e2d1e562aba9cbb22a5cd2619
    role: context
  - path: pages/traits/physiology/mitophagy.html
    sha256: af286acce5378abb5c8d56496d9dd2c768be129fcaa4cd18c06b89fcd782ad3e
    role: context
  - path: pages/traits/physiology/mixotrophic.html
    sha256: 4e96431f0c72fdabcbd121e27ccdc7bf0c4d14ae68aaebe543a2a1a458cd4180
    role: context
  - path: pages/traits/physiology/mucocyst_discharge.html
    sha256: 2eed284f619037f39ece3306a8a0cf28f5abed135987945d18406d61ebc5bca6
    role: context
  - path: pages/traits/physiology/myzocytosis.html
    sha256: f13b841827a688d2297e7b767ce5bd4306aeb1f01128ce7a7da7a3092a8d0e14
    role: context
  - path: pages/traits/physiology/nad_dependent_alcohol_dehydrogenase_activity.html
    sha256: c18a47b5973d9d1e62c942a4a4116e164d2cc81e503d64d003edc8d0a5758eed
    role: context
  - path: pages/traits/physiology/naphthol_as_bi_phosphohydrolase_activity.html
    sha256: 24af291879f7c12f89bc484021d22ca4e39fb1c78d4f085f87c935569af3a046
    role: context
  - path: pages/traits/physiology/natural_competence.html
    sha256: 8852abc717b20fa34ae17b11bcf3f040782ab35e4ed2323cb47fb55a6444233a
    role: context
  - path: pages/traits/physiology/negative_autotropism.html
    sha256: 50dfc71f11908df972ede9142b5278189608b60f73b3935578e7ab9543760744
    role: context
  - path: pages/traits/physiology/nucleophagy.html
    sha256: 6a4cd64e437f8b0b0a01cf96ee907158011bd757c1b547f225e37afb9e008194
    role: context
  - path: pages/traits/physiology/nutrient_adaptation.html
    sha256: de1ed41cecf95788189e0673e1f6874896165e5eebb79798b344fb68b8cacc27
    role: context
  - path: pages/traits/physiology/oligotrophic.html
    sha256: a864965584f40a1f7e8085923b6903be1213a25f5641577c9678face6fdd6b23
    role: context
  - path: pages/traits/physiology/oogamy.html
    sha256: cd90491a758ab06b31e52af2b35950e4f74a6d18b1ffc22c40f5c51bc4a88d60
    role: context
  - path: pages/traits/physiology/organoheterotrophic.html
    sha256: 54957c8689d551cfaaf537fea0f9055d51ccabce7cd8fdaaa57e5ac2e1cc0340
    role: context
  - path: pages/traits/physiology/organotrophic.html
    sha256: ba0def29afc3ac069b8f34d87d07e982834d82033d6bce293da62ae6be40ef71
    role: context
  - path: pages/traits/physiology/ornithine_decarboxylase_activity.html
    sha256: a6bbbd65e796b1070f86b1d68e3baf5ef961753bbeab85a09d8f5736f81316dc
    role: context
  - path: pages/traits/physiology/osmotaxis.html
    sha256: 3355b4b310b70d0adf27156d3acc367b095449e60c7db911f9e60843e6159e1c
    role: context
  - path: pages/traits/physiology/oxidase_activity.html
    sha256: f243159f56616244ff34ba6646f3964b7482f7d4a0e57aab14c43b7be48e8f34
    role: context
  - path: pages/traits/physiology/oxidative_stress_response.html
    sha256: bf0cdb0741f78243c75340f28b83921085e800314026fe5c05b0351f5a1edcb3
    role: context
  - path: pages/traits/physiology/paedogamy.html
    sha256: c0e1fd1ba086ce1b2ba85a4167ad2a11f7182a9fe10470fd5eb32f649a00e66d
    role: context
  - path: pages/traits/physiology/pallium_feeding.html
    sha256: 6ce5c79bb42a69b27d66fdd6fa6ba36927bb82f0092ac1d3c6202e0725900c92
    role: context
  - path: pages/traits/physiology/parasexuality.html
    sha256: 9b1bc1e1574f5119938f94856ab8ac10b5c2dda024266e4ae935d761a9424f0c
    role: context
  - path: pages/traits/physiology/persister_cell_formation.html
    sha256: 2a5a852dd59ae66997bdb5638eff8a4d98e1ee6f948c9c4540416b821b4ab6ac
    role: context
  - path: pages/traits/physiology/pexophagy.html
    sha256: 89807be7ae9d1446e43da846c019ec52b6270b40e413d3347068d050b0e1a9e3
    role: context
  - path: pages/traits/physiology/ph_taxis.html
    sha256: 7488c19a3a88193632fe571b355de13850cb6fb4be15140faba1d302dad7a376
    role: context
  - path: pages/traits/physiology/ph_tropism.html
    sha256: e1836a409770bc71a4d287dea981d63b9dbca4053ef838c9d2171019cfa66410
    role: context
  - path: pages/traits/physiology/phagocytosis.html
    sha256: 6fe8d632fcea41a21b5dc9c326b27d2575800857219bfce23f452d6f6dbef938
    role: context
  - path: pages/traits/physiology/phagotrophy.html
    sha256: ae739c926292f06edbb5327b02ff07ecc25a3628adbd152f23e316d9383f1207
    role: context
  - path: pages/traits/physiology/phenylalanine_arylamidase_activity.html
    sha256: 9899ba57cac83d179358430f51b79619b3d02c51b353d565afe55387d44740d9
    role: context
  - path: pages/traits/physiology/photoautotrophic.html
    sha256: 4874f35b6c930530573830a3859de19689cef9ee96edf5c81f86c889f08880ac
    role: context
  - path: pages/traits/physiology/photoheterotrophic.html
    sha256: 01e63fc738afdfbe35a7ab588b9781e06e0777ffe52d5e0cf0867431e090e967
    role: context
  - path: pages/traits/physiology/photokinesis.html
    sha256: abb4adeb7634cca934b1ce7b038ccaf1083a75ced1d0894e21bbafbb995f673f
    role: context
  - path: pages/traits/physiology/photolithoautotrophic.html
    sha256: 9c5d41861f3f4740238137b3ff500b132fe406caef80981baa39fcb934fffa33
    role: context
  - path: pages/traits/physiology/photolithotrophic.html
    sha256: ae1c55ec0acd4fa035b767be676bda1319c36eaed6b9efd9a9edf3201a84baf5
    role: context
  - path: pages/traits/physiology/photoorganoheterotrophic.html
    sha256: b1a43ffc569df8907e836cb4389d44f074eedf4e069cfdc2cecbf4807051f8b4
    role: context
  - path: pages/traits/physiology/phototaxis.html
    sha256: 3d53371c3a27ce8caa6406bf82c41b2a7c00e6e9797ae79bde791c77ab09274a
    role: context
  - path: pages/traits/physiology/phototrophic.html
    sha256: 72fc8239c938d3014b3acc497a901ad022fd48cd8e9787205cf72077c2140a2c
    role: context
  - path: pages/traits/physiology/phototropism.html
    sha256: 8cce501453acb90a041388d44a31c32b058de86efbf7e94e8f8743e69588ac0c
    role: context
  - path: pages/traits/physiology/pinocytosis.html
    sha256: 42f8f2426e26a639af0b92cc09c35ff78f378be4d5acc177dbcfc5f7b5893785
    role: context
  - path: pages/traits/physiology/positive_autotropism.html
    sha256: 79bdbd7421260440c8cf368fe8a9366730a569ec2a79bcbc54b45fd7b5e40814
    role: context
  - path: pages/traits/physiology/primary_homothallism.html
    sha256: d81b2b7b06c73c2bb4ba95a901e62443fde402008fdd8e7f5c2a5b7ee6d662f5
    role: context
  - path: pages/traits/physiology/prolyl_aminopeptidase_activity.html
    sha256: a1c20e20899f8f4542aad64248a218fa9bb8259cf6be4ab2aa9bc8e581e469dc
    role: context
  - path: pages/traits/physiology/proteaphagy.html
    sha256: ab0e8d545aee0dc06addd2c1b6046067c320e430b57a9153ea4f7a4580a98f5b
    role: context
  - path: pages/traits/physiology/pseudobipolar_mating_system.html
    sha256: 5fe99f0df6ed22d5eb90ec6435748748fad0eebb2b724847a33c12e398b0d913
    role: context
  - path: pages/traits/physiology/pseudohomothallism.html
    sha256: 5acf1e98b7f29ca8355ce65bd334915982e51e8ee2caef6cb52b3673bf089f7b
    role: context
  - path: pages/traits/physiology/pyrazinamidase_activity.html
    sha256: 05ccb2aeb37aee1560d6d758939e8cc67d5dd22f77e3f4138d38c7e8536cf45a
    role: context
  - path: pages/traits/physiology/pyrrolidonyl_arylamidase_activity.html
    sha256: aa5e590e970bfa3898fb3fabca2ee4b524d4d42d426e59622cdf1435bdc2d178
    role: context
  - path: pages/traits/physiology/quorum_quenching.html
    sha256: 1c86224111b10eed77cca82b6e5f5ee73c2a3716aa3df26bf0134a198f253565
    role: context
  - path: pages/traits/physiology/quorum_sensing.html
    sha256: 3a73f163b72c5295d29c9f395e0dbc3008e1e9af9e7ddb97a459c0b8d24addc6
    role: context
  - path: pages/traits/physiology/rapid_axopodial_contraction.html
    sha256: 845b48e03cfb72188d496215178796209194f2ec340f48d5e9074fb62d86a8d6
    role: context
  - path: pages/traits/physiology/replicative_aging.html
    sha256: 4a9ad08c30dea142f58a0aaa64b34f42a9a8a58f322fe0436a15b66235043090
    role: context
  - path: pages/traits/physiology/rheotaxis.html
    sha256: 4b025fc06b825b7ab64e615ac2d122f91e79ac1f61551421bc01c490bca78a6b
    role: context
  - path: pages/traits/physiology/rheotropism.html
    sha256: 17abe11973dbded23a95aa5f37c23e05ef6037fd21c1165539e393117aa45e59
    role: context
  - path: pages/traits/physiology/ribophagy.html
    sha256: d46f35a9ea142b45f67d2492eb4579e0ee0f92a1a74ca02ed8356dccd9c690bc
    role: context
  - path: pages/traits/physiology/serine_arylamidase_activity.html
    sha256: 1ef881d8367cd444515f5220c1839bb928267e6f9c799c20bc8dc8a1d8929b2e
    role: context
  - path: pages/traits/physiology/siderophore_production.html
    sha256: 63719d1b64153e45e1c85fdfda65c9a3ae43751c1cf1d2f922139e7aecd1c320
    role: context
  - path: pages/traits/physiology/siliceous_scale_production.html
    sha256: 782ab658fc0a2abda57b37ff496e8e5002896dd5a8c4f52f263cd5cdf5c07d07
    role: context
  - path: pages/traits/physiology/sos_response.html
    sha256: 5479f1313a5e4db0efa50526ac2358ad3ff8a07f3467ab5b75a1f03f6fb896c7
    role: context
  - path: pages/traits/physiology/spore_germination.html
    sha256: 2d617b6a4d1939d27688d066fffc648dc5ab81f7f2bf8a306a4f06dd9b0b6c66
    role: context
  - path: pages/traits/physiology/stress_response.html
    sha256: 66b4bf3ec7eff017dcab922fc8f9b3b196c50fb515ac4b071605684f264a56f0
    role: context
  - path: pages/traits/physiology/tetrapolar_mating_system.html
    sha256: f8d6fe67ab4514da97d8e8e76d1b13af37590f56d0dfd7a192a0cb73f0baf158
    role: context
  - path: pages/traits/physiology/thermotaxis.html
    sha256: d6a1d464ac46ece96c8d4ddee164660ebb604b259da3cb11ff490f1c294e3ad0
    role: context
  - path: pages/traits/physiology/thigmotropism.html
    sha256: 09fae10d94c4df87782c5b680b9fecb7161c251cc04260f56c194352dd86f500
    role: context
  - path: pages/traits/physiology/toxicyst_discharge.html
    sha256: adac64ca82ff133a20d5b555c431a1d4b3d6a3a6a44dabd37faae1ce83e9c6f2
    role: context
  - path: pages/traits/physiology/trichocyst_discharge.html
    sha256: 408a8e39bbb96d24d5e13516d6fd9c3473a24bb86d570c8c5f38918286cb915a
    role: context
  - path: pages/traits/physiology/tripolar_mating_system.html
    sha256: fdfc2ededa4ea369a599c769a377ce073a6dadd774c6a2e1ebabe446d22b094f
    role: context
  - path: pages/traits/physiology/trogocytosis.html
    sha256: 09d93a92ad9e41383d77a53e6f8bb759e79ed67226de901e0de4cfad43048f91
    role: context
  - path: pages/traits/physiology/trophic_type.html
    sha256: 4a2317b0e64f5fe0a656eecae175af727ed40d8acb0531c90ce72b7f7e901674
    role: context
  - path: pages/traits/physiology/trypsin_activity.html
    sha256: f70c1e85cd8cc0af9a5835be4b2457ec542ba73e607e6c763e1f2f8188064a26
    role: context
  - path: pages/traits/physiology/tyrosine_arylamidase_activity.html
    sha256: 9cbef83d43a9f6992997b7478d5274a43146753278d352de1032991ace231c8b
    role: context
  - path: pages/traits/physiology/unconventional_protein_secretion.html
    sha256: db749311f473712791a9ad6726ced005578a2c2e79c06dfe9c85d4f237f56045
    role: context
  - path: pages/traits/physiology/unisexual_reproduction.html
    sha256: 49b655cfa7d679f5a565de9d31c8bdc5ea87e9af88f8e727b0b307391a1cfe30
    role: context
  - path: pages/traits/physiology/urease_activity.html
    sha256: e3c065e17a1184457e8f74979ebf679c8062a2cee3abc917fdb3a436f8d88bba
    role: context
  - path: pages/traits/physiology/valine_arylamidase_activity.html
    sha256: 2e2692e58be60d8f760c9e6cdcc8a9eaac92c9e61dce7cf2af19be434ed59b9e
    role: context
  - path: pages/traits/physiology/viable_but_nonculturable_state.html
    sha256: 846bbb17c24c47083be51b8cc2e20bc8dafb7b83e60af86a2ba8a00537dc4459
    role: context
  - path: pages/traits/physiology/viscotaxis.html
    sha256: ecb1ed8024658ccab6d05c6b2276d56f9c70374a801c3da965f2fffdf24207d1
    role: context
  - path: pages/traits/quantitative_property/has_maximum_observed_value.html
    sha256: dc30a03617c91602012d9f53951f7fa887d40ee67596e66e6101b9b48f247caa
    role: context
  - path: pages/traits/quantitative_property/has_minimum_observed_value.html
    sha256: 68a04a169a148cc4bcffedb2b94a2a6c7a4b5ae5c131bef6bd262379328f47e3
    role: context
  - path: pages/traits/quantitative_property/has_observed_spot_value.html
    sha256: 022f787fd0ea2cf89af4c1c56e00bf07f596238f2771752e7ca8684440a96db9
    role: context
  - path: pages/traits/quantitative_property/has_value.html
    sha256: 6d5effc34005b8b6e9b5e31ea7120f22d9a0944c1d279ed8406afb9f06f76dfe
    role: context
  - path: pages/traits/quantitative_property/has_value_comments.html
    sha256: 97a9b25711035c43822e1d49a2968d71d6866726baf709aefe834994fcd8ed5d
    role: context
  - path: pages/traits/quantitative_property/is_negative_data.html
    sha256: 94c0376eec48d74111c83d2d0cb209f03275623cfe3bb7b26c15d5a21a246083
    role: context
  - path: pages/traits/quantitative_property/observation_data_property.html
    sha256: 49b3cf5c35dc11bf12c6326b83293c19b6f6a0f289b366cc0d85081f128564b4
    role: context
  - path: pages/traits/upper/biological_process.html
    sha256: 1386638f0f60b9189c8047a1b1f0f544d4d47e6aab6ecb4442d51ed126f49fa5
    role: context
  - path: pages/traits/upper/chemical_entity.html
    sha256: d66342746d3a71342388346bdc2c86fc335fa14b92f3d7bae29dcb3dbc8cbfd5
    role: context
  - path: pages/traits/upper/enzyme.html
    sha256: 6708ba1ff38d7db5e1107b8c10275c062e49667bcb571e267e52161b7d85b20d
    role: context
  - path: pages/traits/upper/material_entity.html
    sha256: 7f8ba23cd6bc3f7b6b2e9ea05d5f17dc343196bf7602439710fae9e3a44ab953
    role: context
  - path: pages/traits/upper/microbe.html
    sha256: c886809f933efd07278fa59c9d7daef24ec97003981ab3c60acdf6cd2e14ca66
    role: context
  - path: pages/traits/upper/observation.html
    sha256: c3942f93b1a908c82edd94b2382b1ce5abcc449622395126642793c1bea22711
    role: context
  - path: pages/traits/upper/phenotype.html
    sha256: 20b8dc611b6c6c568358c82118490464f94e64d65300512145c7ed3e7a7c3ab8
    role: context
  - path: pages/traits/upper/quality.html
    sha256: 85da312a958d3f38bf6c2905625676be5661cf960b43679ee9e41d573da401df
    role: context
  - path: pages/umap.html
    sha256: d56aa5652be577e013867c4ae74fe1dea2ccc1ecf03ff34977b34133ec3963bf
    role: context
  - path: proposals/metpo_traitmech_v586/metpo_proposal_classes_robot.tsv
    sha256: 818aaf5a28c59c602d0b7ad9d3728b89da1f017e983a8760d9463eccc8b7f851
    role: context
  - path: proposals/metpo_traitmech_v586/proposal.md
    sha256: f9c74f6b69a0210cac6c23bcb78fdf8e4b73f584f21ad52c649c10c01f96cbaa
    role: context
  - path: reports/metpo_2026_06_12_active_review.tsv
    sha256: 45e9c6471475635ba1f2602cd636a119d490f5dbd8dd6ac8af1aab89a321379f
    role: context
  - path: reports/metpo_2026_06_12_release_delta.tsv
    sha256: afe858d2aa0ade08322c7808d5917ff370e069ba02c2642d483342db8e9323ac
    role: context
  - path: reports/proposal_citation_audit.tsv
    sha256: c901e62828efb80dea9332ffaf4a5c2c2b8ba42d7d5664c76ab65e606e5408bd
    role: context
  - path: reports/robot/metpo_traitmech_v586/classes.owl
    sha256: 6441fe6a90760a48fced8fa3169caf0ae03ebab1b0cec21ea59c0c95a0900f51
    role: context
  - path: reports/robot/metpo_traitmech_v586/merged.owl
    sha256: b7ae62416c74c80e5e3af0be207813978eb6904b8e17792f71fbab2de1793084
    role: context
  - path: reports/robot/metpo_traitmech_v586/reasoned.owl
    sha256: 56091be7bc4e05397258b312699051269dc42232088f9715b4c5f18dffd83cad
    role: context
  - path: research/traits/physiology/cellular_rejuvenation-source-verification.json
    sha256: 182bd4cf3cc91cc193c79b344968f36d6d070e0054fc19b7231a6809026f9820
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
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/.vendored_canon_ref
    sha256: 698af47e96e93fe96e81910bb140593a79c2b92c4688892edeab9b63244ec5bf
    role: context
  - path: scripts/add_cellular_rejuvenation_trait.py
    sha256: 2155ebb0bc3a76b86cdf525ce97657bcbc4e3ee8e4424c25b32b28eac4bd89a5
    role: context
  - path: scripts/audit_canonical_examples.py
    sha256: 367b9a1759b81e545b06c8dc0c22419ae8d478e3fcd8de6d0bc0cacbb9eacf54
    role: context
  - path: scripts/correct_cellular_rejuvenation_figures.py
    sha256: ecd42e67620fcdc6b538fd69a1c312325eb605d94770a779b922af5594cd6bcf
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
  - path: tests/test_add_cellular_rejuvenation_trait.py
    sha256: 221b541ab8264163faf7daefc71f9cb702dd9c2613e9512c693dfdd5d12261f9
    role: context
  - path: tests/test_correct_cellular_rejuvenation_figures.py
    sha256: b461db61807d37ce50e547d0d8f4fbf7633cf2ba5b80e01f44efedab771d0845
    role: context
targets:
- target_id: traitmech:000710
  path: data/traits/physiology/cellular_rejuvenation.yaml
  label: functional cellular rejuvenation
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: scripts/correct_cellular_rejuvenation_figures.py
    role: guarded figure-attribution correction
  - repository: CultureBotAI/TraitMech
    path: scripts/add_cellular_rejuvenation_trait.py
    role: guarded curation writer
  - repository: CultureBotAI/TraitMech
    path: data/traits/physiology/cellular_rejuvenation.yaml
    role: maintained trait record
  - repository: CultureBotAI/TraitMech
    path: proposals/metpo_traitmech_v586/metpo_proposal_classes_robot.tsv
    role: companion METPO proposal
  - repository: CultureBotAI/TraitMech
    path: research/traits/physiology/cellular_rejuvenation-source-verification.json
    role: historical source assessment with explicit successor correction
scope:
  description: Complete corrected trait, maintained owners, evidence, identity and
    proposal, history, directly related skill guidance, tests and generated changes.
  selection: Same exact affected trait as the predecessor; no sampling.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - traitmech:000710
  exclusions:
  - target: Other1104 TraitRecords
    reason: Byte preservation and deterministic gates only, not scientific reassessment.
  - target: data/traits/physiology/spore_germination.yaml
    reason: Protected; unchanged.
checks:
- check_id: records-0
  name: .venv/bin/linkml-validate -s src/traitmech/schema/traitmech.yaml --target-class
    TraitRecord data/traits/physiology/cellular_rejuvenation.yaml
  command: .venv/bin/linkml-validate -s src/traitmech/schema/traitmech.yaml --target-class
    TraitRecord data/traits/physiology/cellular_rejuvenation.yaml
  status: passed
  required: true
  target_ids:
  - traitmech:000710
  exit_code: 0
  expected_exit_code: 0
  summary: Corrected-content native check passed; corpus checks do not constitute
    whole-corpus scientific review.
- check_id: records-1
  name: .venv/bin/python scripts/validate_strict.py data/traits/physiology/cellular_rejuvenation.yaml
  command: .venv/bin/python scripts/validate_strict.py data/traits/physiology/cellular_rejuvenation.yaml
  status: passed
  required: true
  target_ids:
  - traitmech:000710
  exit_code: 0
  expected_exit_code: 0
  summary: Corrected-content native check passed; corpus checks do not constitute
    whole-corpus scientific review.
- check_id: records-2
  name: .venv/bin/python scripts/verify_snippets.py --record data/traits/physiology/cellular_rejuvenation.yaml
    --out /tmp/traitmech-rejuvenation-corrected-checks-20261012/snippet-results.tsv
  command: .venv/bin/python scripts/verify_snippets.py --record data/traits/physiology/cellular_rejuvenation.yaml
    --out /tmp/traitmech-rejuvenation-corrected-checks-20261012/snippet-results.tsv
  status: passed
  required: true
  target_ids:
  - traitmech:000710
  exit_code: 0
  expected_exit_code: 0
  summary: Four VERIFIED abstract spans and one NOT_IN_ABSTRACT Results span. The
    latter remains directly verified in primary XML; no change to any quote or DOI.
- check_id: writer-0
  name: .venv/bin/python -m pytest -q tests/test_add_cellular_rejuvenation_trait.py
    tests/test_correct_cellular_rejuvenation_figures.py
  command: .venv/bin/python -m pytest -q tests/test_add_cellular_rejuvenation_trait.py
    tests/test_correct_cellular_rejuvenation_figures.py
  status: passed
  required: true
  target_ids:
  - traitmech:000710
  exit_code: 0
  expected_exit_code: 0
  summary: 30 focused tests passed, including exact correction preimages, preserved
    original event/source assessment, no writes on rejected input, idempotency and
    endpoint-specific attribution.
- check_id: generate-0
  name: just audit-proposals
  command: just audit-proposals
  status: passed
  required: true
  target_ids:
  - traitmech:000710
  exit_code: 0
  expected_exit_code: 0
  summary: Corrected-content native check passed; corpus checks do not constitute
    whole-corpus scientific review.
- check_id: generate-1
  name: just ground-predicates
  command: just ground-predicates
  status: passed
  required: true
  target_ids:
  - traitmech:000710
  exit_code: 0
  expected_exit_code: 0
  summary: Corrected-content native check passed; corpus checks do not constitute
    whole-corpus scientific review.
- check_id: generate-2
  name: just ground-nodes
  command: just ground-nodes
  status: passed
  required: true
  target_ids:
  - traitmech:000710
  exit_code: 0
  expected_exit_code: 0
  summary: Corrected-content native check passed; corpus checks do not constitute
    whole-corpus scientific review.
- check_id: generate-3
  name: just audit-graphs
  command: just audit-graphs
  status: passed
  required: true
  target_ids:
  - traitmech:000710
  exit_code: 0
  expected_exit_code: 0
  summary: Corrected-content native check passed; corpus checks do not constitute
    whole-corpus scientific review.
- check_id: generate-4
  name: just audit-graph-protein-taxa
  command: just audit-graph-protein-taxa
  status: passed
  required: true
  target_ids:
  - traitmech:000710
  exit_code: 0
  expected_exit_code: 0
  summary: Corrected-content native check passed; corpus checks do not constitute
    whole-corpus scientific review.
- check_id: generate-5
  name: just audit-predicate-domains
  command: just audit-predicate-domains
  status: passed
  required: true
  target_ids:
  - traitmech:000710
  exit_code: 0
  expected_exit_code: 0
  summary: Corrected-content native check passed; corpus checks do not constitute
    whole-corpus scientific review.
- check_id: generate-6
  name: just check-biolink-coverage
  command: just check-biolink-coverage
  status: passed
  required: true
  target_ids:
  - traitmech:000710
  exit_code: 0
  expected_exit_code: 0
  summary: Corrected-content native check passed; corpus checks do not constitute
    whole-corpus scientific review.
- check_id: generate-7
  name: just audit-snippets
  command: just audit-snippets
  status: passed
  required: true
  target_ids:
  - traitmech:000710
  exit_code: 0
  expected_exit_code: 0
  summary: Corrected-content native check passed; corpus checks do not constitute
    whole-corpus scientific review.
- check_id: generate-8
  name: just gen-discussions-data
  command: just gen-discussions-data
  status: passed
  required: true
  target_ids:
  - traitmech:000710
  exit_code: 0
  expected_exit_code: 0
  summary: Corrected-content native check passed; corpus checks do not constitute
    whole-corpus scientific review.
- check_id: generate-9
  name: just gen-qc-dashboard
  command: just gen-qc-dashboard
  status: passed
  required: true
  target_ids:
  - traitmech:000710
  exit_code: 0
  expected_exit_code: 0
  summary: Corrected-content native check passed; corpus checks do not constitute
    whole-corpus scientific review.
- check_id: generate-10
  name: just gen-pages
  command: just gen-pages
  status: passed
  required: true
  target_ids:
  - traitmech:000710
  exit_code: 0
  expected_exit_code: 0
  summary: Corrected-content native check passed; corpus checks do not constitute
    whole-corpus scientific review.
- check_id: generate-11
  name: just gen-priority-dashboard
  command: just gen-priority-dashboard
  status: passed
  required: true
  target_ids:
  - traitmech:000710
  exit_code: 0
  expected_exit_code: 0
  summary: Corrected-content native check passed; corpus checks do not constitute
    whole-corpus scientific review.
- check_id: verify-0
  name: just qc
  command: just qc
  status: passed
  required: true
  target_ids:
  - traitmech:000710
  exit_code: 0
  expected_exit_code: 0
  summary: Corrected-content native check passed; corpus checks do not constitute
    whole-corpus scientific review.
- check_id: verify-1
  name: just validate-history
  command: just validate-history
  status: passed
  required: true
  target_ids:
  - traitmech:000710
  exit_code: 0
  expected_exit_code: 0
  summary: Corrected-content native check passed; corpus checks do not constitute
    whole-corpus scientific review.
- check_id: verify-2
  name: just validate-products
  command: just validate-products
  status: passed
  required: true
  target_ids:
  - traitmech:000710
  exit_code: 0
  expected_exit_code: 0
  summary: Corrected-content native check passed; corpus checks do not constitute
    whole-corpus scientific review.
- check_id: verify-3
  name: just verify-proposal metpo_traitmech_v586
  command: just verify-proposal metpo_traitmech_v586
  status: passed
  required: true
  target_ids:
  - traitmech:000710
  exit_code: 0
  expected_exit_code: 0
  summary: Corrected-content native check passed; corpus checks do not constitute
    whole-corpus scientific review.
- check_id: verify-4
  name: just robot-validate-proposal metpo_traitmech_v586
  command: just robot-validate-proposal metpo_traitmech_v586
  status: passed
  required: true
  target_ids:
  - traitmech:000710
  exit_code: 0
  expected_exit_code: 0
  summary: Corrected-content native check passed; corpus checks do not constitute
    whole-corpus scientific review.
- check_id: verify-5
  name: .venv/bin/ruff check src scripts tests
  command: .venv/bin/ruff check src scripts tests
  status: passed
  required: true
  target_ids:
  - traitmech:000710
  exit_code: 0
  expected_exit_code: 0
  summary: Corrected-content native check passed; corpus checks do not constitute
    whole-corpus scientific review.
- check_id: tests-0
  name: .venv/bin/python -m pytest -q --junitxml=/tmp/traitmech-rejuvenation-corrected-checks-20261012/pytest.xml
  command: .venv/bin/python -m pytest -q --junitxml=/tmp/traitmech-rejuvenation-corrected-checks-20261012/pytest.xml
  status: passed
  required: true
  target_ids:
  - traitmech:000710
  exit_code: 0
  expected_exit_code: 0
  summary: 4242 tests passed on the stable corrected checkpoint, after regeneration.
- check_id: supplemental-0
  name: .venv/bin/python scripts/validate_history_links.py history/records/cellular_rejuvenation
  command: .venv/bin/python scripts/validate_history_links.py history/records/cellular_rejuvenation
  status: passed
  required: true
  target_ids:
  - traitmech:000710
  exit_code: 0
  expected_exit_code: 0
  summary: Corrected-content native check passed; corpus checks do not constitute
    whole-corpus scientific review.
- check_id: supplemental-1
  name: .venv/bin/linkml-validate --schema src/traitmech/schema/history.yaml --target-class
    HistoryRecord history/records/cellular_rejuvenation/2026-10-12T121656Z-codex-a49ab2.yaml
  command: .venv/bin/linkml-validate --schema src/traitmech/schema/history.yaml --target-class
    HistoryRecord history/records/cellular_rejuvenation/2026-10-12T121656Z-codex-a49ab2.yaml
  status: passed
  required: true
  target_ids:
  - traitmech:000710
  exit_code: 0
  expected_exit_code: 0
  summary: Corrected-content native check passed; corpus checks do not constitute
    whole-corpus scientific review.
- check_id: supplemental-2
  name: .venv/bin/linkml-validate --schema src/traitmech/schema/history.yaml --target-class
    HistoryRecord history/records/cellular_rejuvenation/2026-10-12T124939Z-codex-e5fcad.yaml
  command: .venv/bin/linkml-validate --schema src/traitmech/schema/history.yaml --target-class
    HistoryRecord history/records/cellular_rejuvenation/2026-10-12T124939Z-codex-e5fcad.yaml
  status: passed
  required: true
  target_ids:
  - traitmech:000710
  exit_code: 0
  expected_exit_code: 0
  summary: Corrected-content native check passed; corpus checks do not constitute
    whole-corpus scientific review.
- check_id: supplemental-3
  name: .venv/bin/python scripts/audit_canonical_examples.py --no-resolve
  command: .venv/bin/python scripts/audit_canonical_examples.py --no-resolve
  status: passed
  required: true
  target_ids:
  - traitmech:000710
  exit_code: 0
  expected_exit_code: 0
  summary: Corrected-content native check passed; corpus checks do not constitute
    whole-corpus scientific review.
- check_id: supplemental-4
  name: .venv/bin/python scripts/run_trait_graph_audit.py --verify
  command: .venv/bin/python scripts/run_trait_graph_audit.py --verify
  status: passed
  required: true
  target_ids:
  - traitmech:000710
  exit_code: 0
  expected_exit_code: 0
  summary: Corrected-content native check passed; corpus checks do not constitute
    whole-corpus scientific review.
- check_id: supplemental-5
  name: .venv/bin/python scripts/audit_history_records.py --base d5ade193d52ce90dfd8cd46adb6b28aa0871eb06
  command: .venv/bin/python scripts/audit_history_records.py --base d5ade193d52ce90dfd8cd46adb6b28aa0871eb06
  status: passed
  required: true
  target_ids:
  - traitmech:000710
  exit_code: 0
  expected_exit_code: 0
  summary: Corrected-content native check passed; corpus checks do not constitute
    whole-corpus scientific review.
- check_id: supplemental-6
  name: git diff --check d5ade193d52ce90dfd8cd46adb6b28aa0871eb06 HEAD -- . ':(exclude)proposals/metpo_traitmech_v586/metpo_proposal_classes_robot.tsv'
  command: git diff --check d5ade193d52ce90dfd8cd46adb6b28aa0871eb06 HEAD -- . ':(exclude)proposals/metpo_traitmech_v586/metpo_proposal_classes_robot.tsv'
  status: passed
  required: true
  target_ids:
  - traitmech:000710
  exit_code: 0
  expected_exit_code: 0
  summary: Corrected-content native check passed; corpus checks do not constitute
    whole-corpus scientific review.
- check_id: supplemental-7
  name: git -c core.whitespace=-blank-at-eol diff --check d5ade193d52ce90dfd8cd46adb6b28aa0871eb06
    HEAD -- proposals/metpo_traitmech_v586/metpo_proposal_classes_robot.tsv
  command: git -c core.whitespace=-blank-at-eol diff --check d5ade193d52ce90dfd8cd46adb6b28aa0871eb06
    HEAD -- proposals/metpo_traitmech_v586/metpo_proposal_classes_robot.tsv
  status: passed
  required: true
  target_ids:
  - traitmech:000710
  exit_code: 0
  expected_exit_code: 0
  summary: Corrected-content native check passed; corpus checks do not constitute
    whole-corpus scientific review.
- check_id: browser
  name: Desktop/mobile generated products
  command: node /tmp/traitmech-rejuvenation-corrected-browser-20261012.cjs
  status: passed
  required: true
  target_ids:
  - traitmech:000710
  exit_code: 0
  expected_exit_code: 0
  summary: 'Desktop1440/mobile390 assertions and eight visually inspected corrected
    screenshots: Figure4 endpoint qualified, two history links, five snippets, two
    discussions, correct local identifier, working navigation/count/image, no overflow
    or page errors.'
- check_id: embeddings
  name: Embedding applicability
  status: not_applicable
  required: false
  target_ids:
  - traitmech:000710
  summary: Neither exact configured embedding source exists in the inspected primary/owned
    layouts. Existing artifacts retained, not regenerated.
- check_id: local-publication-refresh
  name: Restored local and remote publication assessment
  command: PYTHONPATH=src .venv/bin/python /tmp/traitmech-rejuvenation-check-helpers-20261012.py
    prepublish; .venv/bin/python /tmp/traitmech-rejuvenation-owned-copies-20261012.py
  status: passed
  required: true
  target_ids:
  - traitmech:000710
  exit_code: 0
  expected_exit_code: 0
  summary: Fresh 23 registered TraitMech roots, 127 CommunityMech roots, historical
    tracked reservations, complete open/draft PR files and upstream heads checked.
    Original owned copy matches initial committed checkpoint; independent corrected
    publishing clone separately scanned, not falsely equated to registered HEAD. No
    conflicting reservation.
evidence:
- evidence_id: source-0
  kind: primary_source
  reference: DOI:10.1242/jcs.86.1.263
  locator: MED scientific abstract, contiguous span after HTML inline markup removal
  accessed_at: '2026-10-12T13:07:46Z'
  support: supports
  summary: Haga and Karino 1986, PMID:3654779; scientific abstract, directly read
    in the MED record. Young-cell cytoplasm restored sexual activity in senescent
    cells (about 700 fissions); recovery persisted for up to 20 fissions. Division
    rate and fertility after self-conjugation did not improve. This supports endpoint-specific
    recovery in treated old cells, not whole-cell or permanent rejuvenation. Full
    methods and figures were unavailable.
  snapshot_sha256: 42a36cfef3992bcd38635ac206475303831a4cbeee350e9ea87bd6b4b59a19bc
- evidence_id: source-1
  kind: primary_source
  reference: DOI:10.1038/s41467-018-06154-9
  locator: /article/body/sec[2]/sec[4]/p[3]
  accessed_at: '2026-10-12T13:07:46Z'
  support: supports
  summary: 'Proenca et al. 2018, PMID:30213942, PMC6137065; Results, Stable equilibria
    are connected by aging and rejuvenation (Sec6), directly checked in primary XML.
    Actual Figure 4d was visually inspected: new-daughter lineages from the old-cell
    equilibrium converge toward faster growth over successive generations. These doubling
    times are derived from elongation rates, not direct interdivision intervals. Recovery
    is in descendants, not the same old mother. The tested MG1655 conditions do not
    establish all-environment recovery or a universal damage mechanism.'
  snapshot_sha256: a63ca9af79785836d84b4e5e9902a56320c0fb4bf5cf65b1eb3d8d3f83288f58
- evidence_id: source-2
  kind: primary_source
  reference: DOI:10.1126/science.1204349
  locator: MED scientific abstract, contiguous span after HTML inline markup removal
  accessed_at: '2026-10-12T13:07:46Z'
  support: supports
  summary: Unal et al. 2011, PMID:21700873, PMC3923466; scientific abstract, directly
    checked in MED and an MIT-hosted author manuscript. Main text and Figure 1 support
    gamete replicative-potential reset. Figure 4 concerns the separate vegetative
    lifespan-extension experiment. Transient NDT80-dependent vegetative lifespan extension
    is a separate result and does not establish reversal of every aged-cell defect.
    Supplements and strain tables were not assessed. The retrieved PDF identifies
    the article but differs in size and checksum from MIT bitstream metadata; original
    deposited-byte identity remains unresolved.
  snapshot_sha256: b6bc3e93735e7b231243280fef3a4f17590a79fde4d2a3f877fe5e35236ea898
- evidence_id: source-3
  kind: primary_source
  reference: DOI:10.3390/microorganisms11010082
  locator: /article/front/article-meta/abstract/p
  accessed_at: '2026-10-12T13:07:46Z'
  support: supports
  summary: 'Haga 2023, PMID:36677375, PMC9865852; scientific abstract, directly checked
    in primary XML and PMC text. Results 3.1 uses rejuvenation for suppression of
    mating in mature cells: that maturation-state reset alone is outside this functional
    trait. Results 3.2 reports recovery of old-cell mating activity after transformation.
    Figure 6C measures total cell counts over four days, not direct division times,
    and lacks a young-cell growth comparator. Engineered treatment is not a natural
    canonical taxon example; inferred chemistry is not a proven mechanism.'
  snapshot_sha256: 22f0a9578b988c8555a87ec03351db9fa15fa01ec5986025f1571ca9713ce754
- evidence_id: source-4
  kind: primary_source
  reference: DOI:10.1016/j.isci.2022.103765
  locator: /article/front/article-meta/abstract[1]/p
  accessed_at: '2026-10-12T13:07:46Z'
  support: context_only
  summary: 'Cesar et al. 2022, PMID:35243217, PMC8858994; scientific abstract, directly
    checked against MED and primary XML. Boundary evidence: culture duration during
    stationary phase is not individual replicative age. Immediate regrowth can reflect
    preserved function, not recovery from a demonstrated deficit. Regrowth classes
    use area-derived growth rates; nongrowth during the observation window is not
    proof of irreversible death. Results 2.1 and 2.3, Discussion, limitations and
    classification methods were read; figures and raw data were not independently
    assessed.'
  snapshot_sha256: 40bee57760b257d9b94eedcb21606ee956557342cf8a87a43b15adfdf7c006cd
- evidence_id: content
  kind: record_content
  reference: data/traits/physiology/cellular_rejuvenation.yaml
  locator: Complete YAML, writer/tests, proposal v586, history, source-verification
    JSON, skill guidance, README and generated page.
  accessed_at: '2026-10-12T13:07:46Z'
  support: supports
  summary: One PHYSIOLOGY CLASS under phenotype; functional qualifier excludes marker-only
    or maturation-only reset. Same-cell and descendant recovery distinguished. No
    exact synonym, xref, canonical taxon or molecular graph asserted; status remains
    PROPOSED.
- evidence_id: snippets
  kind: validation
  reference: research/traits/physiology/cellular_rejuvenation-source-verification.json
  locator: DOI-qualified MED/Crossref identity, exact paragraph/abstract matching,
    notice fields and actual-byte hashes.
  accessed_at: '2026-10-12T13:07:46Z'
  support: supports
  summary: All five contiguous spans match; 20/12/17/15/20 words. Linked comment and
    peer evaluations are not corrections or independent experiments. MIT article identity
    is verified but the delivered PDF does not match catalog bytes.
- evidence_id: novelty
  kind: search
  reference: proposals/metpo_traitmech_v586/proposal.md
  locator: Pre-allocation novelty assessment plus restored 13:01 UTC publication recheck
    and independent publishing-copy inventory.
  accessed_at: '2026-10-12T13:07:46Z'
  support: supports
  summary: No exact prior trait or reservation conflict in the bounded inspected scope.
    Fresh restored local/remote checks preserve other reservations and heads; two
    owned copies are explicitly distinguished and their provenance verified.
  search_scope: Ignored/hidden included across 22 baseline TraitMech roots, 18 historical
    tracked trees, 585 cohorts and 6296 interval occurrences; 127 CommunityMech registrations
    and proposal bytes. Frozen 1546/153-row decisions,399 seed IDs with344 live overlap
    and55 absent leads,1106 distinct available YAML versions. Pinned/current released
    RDF and complete paginated pending PR files, including drafts and changed ontology/template
    blobs. Historical trees cannot reconstruct unavailable current ignored/untracked
    bytes; no archive unpacking, symlink-directory traversal, unregistered/private
    coverage or discovery exhaustion claim.
- evidence_id: products
  kind: validation
  reference: reports/proposal_citation_audit.tsv
  locator: Native gates, byte preservation, parsed ROBOT RDF, browser assertions/screenshots
    and independent-clone recovery receipt.
  accessed_at: '2026-10-12T13:07:46Z'
  support: supports
  summary: 'All1104 prior YAMLs and previous history/reviews/proposals/embeddings
    preserved;1103 old pages change only footers, phenotype gains one child. RDF triples
    {''classes'': 15, ''merged'': 12628, ''reasoned'': 12632}; w3id parent-to-quality
    hierarchy verified. Recovery copied1133 owned changed files byte-for-byte without
    metadata repair.'
- evidence_id: access
  kind: validation
  reference: /tmp/traitmech-rejuvenation-publication-20261012/result.json
  locator: Fresh local/remote assessment and /tmp/traitmech-rejuvenation-owned-copies-20261012.json.
  accessed_at: '2026-10-12T13:07:46Z'
  support: supports
  summary: 'Earlier OS access failures remain in the predecessor. Access is now restored:
    registered worktrees are freshly assessed, all initial owned blobs match the retained
    checkpoint, and the corrected independent clone passes its own reservation scan.
    Cleanup still requires a fresh ownership check after merge.'
- evidence_id: figure-attribution
  kind: primary_source
  reference: DOI:10.1126/science.1204349
  locator: 'MIT-delivered author manuscript, PDF pages7/10: actual Figures1/4 and
    captions; corresponding main-text experiments.'
  accessed_at: '2026-10-12T13:07:46Z'
  support: supports
  summary: Figure1 tests gamete RLS reset. Figure4 tests transient NDT80-dependent
    lifespan extension in vegetatively growing aged cells. Grouping both as direct
    support for gamete reset misattributes Figure4, despite the following sentence
    distinguishing that endpoint.
  snapshot_sha256: 59b8752682806a55e155502090992dc7de3e01201615192c86a11726d330a7c4
- evidence_id: correction
  kind: record_content
  reference: data/traits/physiology/cellular_rejuvenation.yaml
  locator: evidence[2].notes, second curation event, guarded correction writer/tests,
    second history entry, sidecar assessment_corrections, proposal clarification and
    rendered page.
  accessed_at: '2026-10-12T13:07:46Z'
  support: supports
  summary: Figure endpoints now distinguished. Definition, DOI, snippet, status and
    checksum limitation preserved. Original event/source interpretation retained with
    explicit successors. Corrected native gates and browser checks pass; no optional
    molecular/taxon claims added.
- evidence_id: prior
  kind: prior_review
  reference: reviews/structured/20261012T124741Z-cellular-rejuvenation/review.yaml
  locator: Open finding yeast-figure-attribution; separate failed local-publication-refresh
    check.
  accessed_at: '2026-10-12T13:07:46Z'
  support: context_only
  summary: Initial needs_curation review remains immutable. This successor reassesses
    the whole corrected addition, resolves its figure finding, and records the successful
    restored publication check without rewriting the earlier failed observation.
assessments:
- assessment_id: identity
  area: identity
  topic: Functional cellular phenotype
  summary: Same-cell performance recovery and descendant replicative-potential reset
    support a reusable endpoint-qualified trait.
  target_ids:
  - traitmech:000710
  evidence_ids:
  - source-0
  - source-1
  - source-2
  - content
  outcome: supported
- assessment_id: scope
  area: scope
  topic: Recovery unit, endpoints and boundaries
  summary: Recovery can be partial/transient; marker changes, mature-state reset,
    preserved function and generic dormancy exit alone are insufficient.
  target_ids:
  - traitmech:000710
  evidence_ids:
  - source-0
  - source-1
  - source-2
  - source-3
  - source-4
  - content
  outcome: supported
- assessment_id: grounding
  area: grounding
  topic: Strictly broader active phenotype parent
  summary: No claim that autogamy, gametogenesis, aging or dormancy is an exact or
    narrower parent. Actual RDF uses the w3id phenotype-to-quality hierarchy.
  target_ids:
  - traitmech:000710
  evidence_ids:
  - content
  - novelty
  - products
  outcome: supported
- assessment_id: evidence
  area: evidence
  topic: Primary-source identity and short verbatim spans
  summary: All evidence identities and source sections verified; positive and boundary
    roles distinguished with access and checksum limitations.
  target_ids:
  - traitmech:000710
  evidence_ids:
  - source-0
  - source-1
  - source-2
  - source-3
  - source-4
  - snippets
  outcome: supported
- assessment_id: figure-attribution
  area: evidence
  topic: Do not group unlike figure endpoints
  summary: Corrected note and explicit sidecar successor distinguish Figure1 gamete
    reset from Figure4 vegetative extension; abstract evidence is unchanged.
  target_ids:
  - traitmech:000710
  evidence_ids:
  - content
  - figure-attribution
  - correction
  outcome: supported
- assessment_id: products
  area: consistency
  topic: Guarded writes, history and derived outputs
  summary: Tests and byte-preservation checks support the narrow change set; no source
    status promotion or forced molecular mechanism.
  target_ids:
  - traitmech:000710
  evidence_ids:
  - content
  - products
  outcome: supported
- assessment_id: novelty
  area: identity
  topic: Bounded novelty and restored current reservation state
  summary: Initial identity searches included ignored and hidden files; fresh restored
    worktree and complete pending-PR assessments find no collision. Independent publishing
    copy is separately assessed as an owned correction of the preserved initial checkpoint.
  target_ids:
  - traitmech:000710
  evidence_ids:
  - novelty
  - access
  outcome: supported
- assessment_id: gaps
  area: completeness
  topic: Mechanistic and taxonomic limits
  summary: Natural exemplars, exact gene/protein identities and shared chemistry remain
    deferred; no evidence is invented to fill optional fields.
  target_ids:
  - traitmech:000710
  evidence_ids:
  - content
  - source-1
  - source-2
  - source-3
  outcome: unknown
- assessment_id: figure-correction
  area: evidence
  topic: Endpoint-specific figure attribution
  outcome: supported
  target_ids:
  - traitmech:000710
  evidence_ids:
  - figure-attribution
  - correction
  - snippets
  summary: Gamete reset and vegetative extension have separate, source-faithful locators;
    preserved abstract quote still supports gamete replicative-potential reset.
- assessment_id: provenance
  area: provenance
  topic: Guarded correction with retained predecessor
  outcome: supported
  target_ids:
  - traitmech:000710
  evidence_ids:
  - correction
  - prior
  summary: Original event, source assessment and saved review remain intact; successor
    explicitly resolves only the supported curation defect without promoting status
    or waiving publication gates.
findings:
- finding_id: yeast-figure-attribution
  issue_key: cellular-rejuvenation-yeast-figure-attribution
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: Figure4 is vegetative extension evidence, not gamete-reset evidence
  description: The yeast note groups Figures1 and4 as support for gamete replicative-potential
    reset. Figure4 instead measures lifespan extension in vegetatively growing aged
    cells. The following sentence distinguishes that result but does not correct the
    preceding locator attribution; the sidecar repeats it.
  target_ids:
  - traitmech:000710
  field_paths:
  - evidence[2].notes
  evidence_ids:
  - figure-attribution
  - correction
  - prior
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: scripts/correct_cellular_rejuvenation_figures.py
    role: guarded figure-attribution correction
  - repository: CultureBotAI/TraitMech
    path: scripts/add_cellular_rejuvenation_trait.py
    role: guarded curation writer
  - repository: CultureBotAI/TraitMech
    path: data/traits/physiology/cellular_rejuvenation.yaml
    role: maintained trait record
  - repository: CultureBotAI/TraitMech
    path: proposals/metpo_traitmech_v586/metpo_proposal_classes_robot.tsv
    role: companion METPO proposal
  - repository: CultureBotAI/TraitMech
    path: research/traits/physiology/cellular_rejuvenation-source-verification.json
    role: historical source assessment with explicit successor correction
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/1893
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261012T124741Z-cellular-rejuvenation
    finding_id: yeast-figure-attribution
  disposition_reason: The corrected note explicitly assigns Figure1 to gamete reset
    and Figure4 to vegetative extension. Guarded correction, preserved original event
    and source assessment, appended history, tests and rendered evidence agree. The
    separate earlier publication hold is reassessed by the now-passing restored local
    and remote checks.
actions: []
limitations:
- Author self-review, not independent or human scientific sign-off. Full scope for
  this one addition, not whole-corpus scientific review or completion of the external
  PR lifecycle.
- Earlier OS access failures are preserved in the predecessor; fresh restored checks
  now pass. The original registered branch remains at the baseline with preserved
  uncommitted pre-correction bytes; publication uses the independently corrected clone.
  Cleanup requires a new ownership check.
- 'Earlier full review and source-access limitations remain: MIT delivered-byte/catalog
  mismatch, incomplete publisher/notice access, no full supplement/raw-data reanalysis
  or natural canonical/protein mechanism claim.'
- The original focused test execution failed on inaccessible Git metadata. Its isolated
  rerun and the independent-clone full suite passed; no test was weakened.
- Source access timestamps include reinspection of retained primary snapshots. Only
  the previously documented figures were visually inspected, not all experiments.
- Existing product adapter skips and source-license warnings remain baseline limits;
  embeddings retained. Required TSV header tabs retain the narrow inspected exception.
- External review, PR CI, native queue and landed-tree/independent recovery checks
  are not completed by this bundle.
tags:
- add-trait
- cellular-rejuvenation
- self-review
- issue-1893
- full-successor
related_reviews:
- repository: CultureBotAI/TraitMech
  review_id: 20261012T124741Z-cellular-rejuvenation
  relationship: Full successor on corrected inputs; resolves the figure finding and
    reassesses the formerly unavailable publication check after access restoration.
```
