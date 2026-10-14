# Adversarial review of reversible nematode-paralyzing activity

- Review: 20261014T013353Z-reversible-nematode-paralyzing-activity
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-14T01:25:46Z
- Finished UTC: 2026-10-14T01:33:53Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Source-based author review supports one microbial reversible-paralyzing capability. No actionable defect identified; two OPEN discussions retain hierarchy, source and mechanism uncertainty. PROPOSED is not human sign-off.

## Scope And Provenance

One complete record addition and its maintained/generated owners, not whole-corpus scientific review.

Selection: One exact new trait, without sampling.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 01efb35f2a040057426762303f208048edb83013.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| traitmech:000722 | data/traits/physiology/reversible_nematode_paralyzing_activity.yaml | maintained | reversible nematode-paralyzing activity |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate -s src/traitmech/schema/traitmech.yaml --target-class TraitRecord data/traits/physiology/reversible_nematode_paralyzing_activity.yaml | passed | True | traitmech:000722 | Actual maintained command passed. Corpus diagnostics are not whole-corpus scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/validate_strict.py data/traits/physiology/reversible_nematode_paralyzing_activity.yaml | passed | True | traitmech:000722 | Actual maintained command passed. Corpus diagnostics are not whole-corpus scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/validate_history_links.py history/records/reversible_nematode_paralyzing_activity | passed | True | traitmech:000722 | Actual maintained command passed. Corpus diagnostics are not whole-corpus scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/verify_snippets.py --record data/traits/physiology/reversible_nematode_paralyzing_activity.yaml --out /tmp/traitmech-paralysis-checks-20261014/native-record.tsv | passed | True | traitmech:000722 | The native verifier exited zero but omitted both URL references and emitted zero result rows. Neither excerpt is native VERIFIED. Direct HTML/PDF and typeset checks are separate evidence. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python -m pytest -q tests/test_add_reversible_nematode_paralyzing_activity_trait.py -k 'not source_receipt' | passed | True | traitmech:000722 | Actual maintained command passed. Corpus diagnostics are not whole-corpus scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python -m pytest -q tests/test_add_reversible_nematode_paralyzing_activity_trait.py tests/test_readme_artifacts.py tests/test_trait_priority.py tests/test_qc_dashboard_artifacts.py | passed | True | traitmech:000722 | Actual maintained command passed. Corpus diagnostics are not whole-corpus scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/ruff check src scripts tests | passed | True | traitmech:000722 | Actual maintained command passed. Corpus diagnostics are not whole-corpus scientific review. |
| just audit-proposals | passed | True | traitmech:000722 | Actual maintained command passed. Corpus diagnostics are not whole-corpus scientific review. |
| just ground-predicates | passed | True | traitmech:000722 | Actual maintained command passed. Corpus diagnostics are not whole-corpus scientific review. |
| just ground-nodes | passed | True | traitmech:000722 | Actual maintained command passed. Corpus diagnostics are not whole-corpus scientific review. |
| just audit-graphs | passed | True | traitmech:000722 | Actual maintained command passed. Corpus diagnostics are not whole-corpus scientific review. |
| just audit-graph-protein-taxa | passed | True | traitmech:000722 | Actual maintained command passed. Corpus diagnostics are not whole-corpus scientific review. |
| just audit-predicate-domains | passed | True | traitmech:000722 | Actual maintained command passed. Corpus diagnostics are not whole-corpus scientific review. |
| just check-biolink-coverage | passed | True | traitmech:000722 | Actual maintained command passed. Corpus diagnostics are not whole-corpus scientific review. |
| just audit-snippets | passed | True | traitmech:000722 | Actual maintained command passed. Corpus diagnostics are not whole-corpus scientific review. |
| just gen-discussions-data | passed | True | traitmech:000722 | Actual maintained command passed. Corpus diagnostics are not whole-corpus scientific review. |
| just gen-qc-dashboard | passed | True | traitmech:000722 | Actual maintained command passed. Corpus diagnostics are not whole-corpus scientific review. |
| just gen-pages | passed | True | traitmech:000722 | Actual maintained command passed. Corpus diagnostics are not whole-corpus scientific review. |
| just gen-priority-dashboard | passed | True | traitmech:000722 | Actual maintained command passed. Corpus diagnostics are not whole-corpus scientific review. |
| just qc | passed | True | traitmech:000722 | Actual maintained command passed. Corpus diagnostics are not whole-corpus scientific review. |
| just validate-history | passed | True | traitmech:000722 | Actual maintained command passed. Corpus diagnostics are not whole-corpus scientific review. |
| just validate-products | passed | True | traitmech:000722 | Actual maintained command passed. Corpus diagnostics are not whole-corpus scientific review. |
| just verify-proposal metpo_traitmech_v598 | passed | True | traitmech:000722 | Actual maintained command passed. Corpus diagnostics are not whole-corpus scientific review. |
| just robot-validate-proposal metpo_traitmech_v598 | passed | True | traitmech:000722 | Actual maintained command passed. Corpus diagnostics are not whole-corpus scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/audit_canonical_examples.py --no-resolve | passed | True | traitmech:000722 | Canonical-example shape audit passed with --no-resolve; live NCBI checks were not run. The new record has no canonical examples. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/run_trait_graph_audit.py --verify | passed | True | traitmech:000722 | Actual maintained command passed. Corpus diagnostics are not whole-corpus scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/audit_history_records.py --base f44af60a9d88dcc604543301a8669e1e2bff428d | passed | True | traitmech:000722 | Actual maintained command passed. Corpus diagnostics are not whole-corpus scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python -m pytest -q --junitxml=/tmp/traitmech-paralysis-checks-20261014/pytest.xml | passed | True | traitmech:000722 | 4592 tests passed without failures, errors or skips. |
| products | passed | True | traitmech:000722 | All 1116 prior records, protected spore germination, prior history/reviews/proposals/embeddings/templates/baseline are byte-preserved. Existing pages are footer-only except the phenotype child link. Exact w3id RDF identity, hierarchy and definition citations pass. |
| browser | passed | True | traitmech:000722 | 1440/390 px checks pass: two quotes, two discussions, one history, local identifier, hierarchy/browse navigation, dashboard 1117 and coverage image. Eight screenshots visually inspected. No horizontal overflow or page errors. |

## Scientific And Domain Assessments

### Microbial bearer and recovery-defined endpoint

identity: supported. Targets: traitmech:000722.

Fungal-filtrate experiments support a reusable microbial capability. The nematode is the affected organism, not the trait bearer. Recovery is mandatory; nonmovement alone does not establish the class.

### Washout recovery versus initial immobility

evidence: supported. Targets: traitmech:000722.

Both primary experiments include post-exposure recovery. Failed or confounded assays and boundary differences remain explicit. No universal recovery interval, dose, host/stage effect or individual-cell trajectory is asserted.

### Conservative parent and non-equivalent neighboring traits

grounding: supported. Targets: traitmech:000722.

Phenotype is a broader class. Lethal activity, trapping, feeding and attraction have distinct endpoints; a single producer may express different endpoints in different conditions. Bounded ignored/hidden and ontology searches support a local fallback without claiming global novelty.

### Citation roles, verbatim fidelity and URL skips

provenance: supported. Targets: traitmech:000722.

The selected spans follow the actual source pages. Typeset all is retained despite text-layer dl. Native omission is not native VERIFIED. Strain/dose discrepancies remain attributed, canonical taxa are omitted, and only definition authority enters the ROBOT definition citation.

### Guarded writes, exact RDF and preserved owners

consistency: supported. Targets: traitmech:000722.

Dry-run/replay/prevalidation/drift tests pass. Full QC, tests, history, proposal and responsive page checks pass. Existing maintained records and immutable artifacts are unchanged. The proposal has the exact w3id hierarchy, not a legacy stub.

### Unresolved mechanism and source discrepancies

completeness: unknown. Targets: traitmech:000722.

No common active molecule, neural target, canonical strain, protein mechanism, field benefit or environmental safety is established. These gaps are retained and do not erase the narrower recovery-supported capability.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| source-0 | https://journals.flvc.org/nematropica/article/view/64427; English Abstract, printed page 215; PDF page 1. All rendered pages were inspected during source research; quoted page re-inspected during curation. No complete raw-data/statistical reanalysis. | supports | The English Abstract explicitly reports fungal-filtrate reversible paralysis. Needle-probed immobility at 2 h precedes rinsing and reassessment labelled 21 h. Results/Table 2, not initial-paralysis Figure 1 alone, support recovery. Bioassay 2 has no recovery test, bioassay 3 has a high-paralysis control, and bioassay 5 is null. Strain labels, dose values and timing wording conflict and remain attributed. Repeated counts are not individual trajectories. |
| source-1 | https://horizon.documentation.ird.fr/exl-doc/pleins_textes/pleins_textes_5/pt5/nemato/27861.pdf; Results, Study of the reversibility of the toxic effect, printed page 335/PDF page 5, upper right column. All rendered pages were inspected during source research; quoted page re-inspected during curation. No complete raw-data/statistical reanalysis. | supports | Brazilian P. lilacinus filtrate and M. arenaria larvae are identified in the surrounding experiment. The Results and actual Figure 3 show recovery after 24 h in fresh water, following variable exposure to undiluted filtrate from 10-day illuminated motionless aerated malt culture. Needle probing and water/pH-matched medium controls are described. Summary less-than-48-h and Results through-48-h wording differ. The 72-h endpoint is not universal reversibility. Typeset all, not extracted dl, is quoted; proposed neurotropic action is not demonstrated. |
| content | data/traits/physiology/reversible_nematode_paralyzing_activity.yaml; Entire record, writer, tests, proposal, sidecar, history and generated diff. | supports | One microbial capability requiring nematode movement loss and recovery after exposure ends. Not microbial nonmotility, nematode susceptibility, an assay or chemical role. Immobility, reduced speed, reduced hatch, suppression, trapping, attraction or killing alone is insufficient. No canonical examples, exact synonyms/xrefs, proteins or causal graph. |
| ontology | data/raw/metpo.owl; Specified pinned/current OWL and TSV inputs and live neighboring records. | supports | Phenotype METPO:1000059 is broader and lies below quality METPO:1000188. Related lethal, feeding, trapping and attracting endpoints are not equivalents or necessary parents. No exact active/deprecated counterpart identified in literal annotations of three OWL inputs and all cells of six TSV owners. Editor metadata is not an inspected import closure. |
| novelty | research/traits/physiology/reversible_nematode_paralyzing_activity-source-verification.json; Known ignored/hidden current files, retained regular-file Git blobs, pending changed blobs and selected upstream owners. | supports | Initial screen: 179 known locations, 176 available, 139 retained heads, 11 open/draft PRs, 783 pending nonremoved blobs and 587 upstream owner files. All 88 matching paths adjudicated. Existing paralysis passages are exclusions/comparators, not exact records or unresolved exact nodes. PGPT sequence categories and cached literature are leads. The 256 numeric hits are decimal measurements/coordinates; 572 intervals are broad editor envelopes. The initial Git regex control failed and was corrected before completed historical checks. |
| provenance | research/traits/physiology/reversible_nematode_paralyzing_activity-source-verification.json; Primary source hashes, direct text/typeset excerpts, metadata and native URL omission receipt. | supports | Kilama is definition authority; Cayrol independently supports recovery, not standalone producer identity. The 19/22-word excerpts are typeset-verified, but both URL references are skipped by the native DOI/PMID verifier, which emits zero rows. Cayrol text extraction is not an exact match. Kilama follow-up web fetch returned 403; original directly acquired bytes were rehashed and reread. IRD PDF access succeeded. Bounded metadata/notice checks do not establish comprehensive clearance or absence of a DOI. |
| products | reports/proposal_citation_audit.tsv; Actual checks, generation receipts, parsed RDF, preservation and responsive browser tests. | supports | Local gates and full tests pass. Parsed RDF cardinalities: {'classes': 15, 'merged': 12628, 'reasoned': 12632}. Only Kilama and the local record annotate the definition. All 645 pinned CLAW generator blobs match. Neither configured embedding input exists; embeddings remain unchanged. |
| history | history/records/reversible_nematode_paralyzing_activity; Per-record minting and append-only CREATE records. | supports | Observed acceptance at 01:02:02Z precedes the later 01:05:22Z CREATE. Identity, evidence and discussion scope match the change. Codex/GPT-5 and LLM assistance are explicit. Status remains PROPOSED. |
| publication | /tmp/traitmech-paralysis-publication-20261014/accepted.json; Refreshed ignored/hidden local reservation and live remote identity checks. | supports | 180 known locations rechecked. Owned additions separated from competing reservations. Pending heads, titles/bodies, upstream heads and retained history identities unchanged; no conflict identified. |

## Limits And Additional Notes

- Author self-review only. Exact-head external review, CI, native queue and landed-tree checks remain separate publication gates unfinished at this timestamp.
- All rendered source pages were inspected during research and recovery/quoted pages re-inspected during curation. No complete raw-data or statistical reanalysis was performed; exact excerpt fidelity does not independently validate the experiments.
- Recovery, initial paralysis and possible killing depend on assay conditions. No universal host/stage response, dose or recovery threshold, causal mechanism, canonical taxon, field efficacy or safety claim is made.
- Both URL references are skipped by the native DOI/PMID verifier; zero output rows is not source verification. Kilama follow-up web access failed with 403, while original direct bytes remained readable. Bounded source/index/notice checks are not comprehensive clearance.
- The corpus canonical-example audit used --no-resolve for shape only. No canonical example is asserted for the new record.
- Ignored/hidden known copies were included. Unavailable historical ignored/untracked files, symlink targets, arbitrary archives and all unchanged pending-tree content were not reconstructed. Discovery is not exhausted and allocation is not atomic.
- Configured embedding inputs are absent, so existing embeddings remain unchanged. Required trailing empty ROBOT cells use a path-scoped whitespace exception, not an unqualified clean-whitespace claim.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T013353Z-reversible-nematode-paralyzing-activity
kind: record
repository: CultureBotAI/TraitMech
title: Adversarial review of reversible nematode-paralyzing activity
started_at: '2026-10-14T01:25:46Z'
finished_at: '2026-10-14T01:33:53Z'
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
summary: Source-based author review supports one microbial reversible-paralyzing capability.
  No actionable defect identified; two OPEN discussions retain hierarchy, source and
  mechanism uncertainty. PROPOSED is not human sign-off.
source:
  git_revision: 01efb35f2a040057426762303f208048edb83013
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
    sha256: c1b15ca628f307ad172b8921b0653c728d65e2fd79142614285dcb2488ace510
    role: context
  - path: app/dashboard/priority.html
    sha256: da7e8c60d68cf18f03f345474d84e82eb0610d051e5a911dc3b387c85a18dd36
    role: context
  - path: app/dashboard/priority.json
    sha256: a0d320abf4aef332863f5670781d64b610d2264f3d1ae595dff4dd1fc70e2ee0
    role: context
  - path: app/discussions/data.js
    sha256: 3de14d3b86d15892c99f9d1faf00beed83ba8dc0882fe1f52557ec44df653c9e
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
    sha256: c6c3c3d3b12d0f49ac03c5ef7c2296ec799ef1c36225e9debda89977b73fd814
    role: context
  - path: dashboard/index.html
    sha256: dfac768a238a85ca39ab8c567ac2982aa33573619b3d855606d9488aaaa768cc
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
  - path: history/records/reversible_nematode_paralyzing_activity/2026-10-14T010522Z-codex-860a55.yaml
    sha256: 0246961184457578292805f765821673a71acb150e1b0a34093ddec857d1ac96
    role: context
  - path: justfile
    sha256: e6047ea612115a6a78d100b281483ba824c860c3def59bcd0d40e7fb56b3526a
    role: context
  - path: pages/browse.html
    sha256: ba625ab00af9ef9fdaccce67ae4f0fa7fd785b07e7560326f7973c936498f3cc
    role: context
  - path: pages/category/ecology.html
    sha256: 04f22c761700fab88cbbbc54c59337a900c91c7901a01d0e031e09ace4fb9834
    role: context
  - path: pages/category/environment.html
    sha256: df8acfb80cc042e8aea88325f6ca6c2413f0bccd7870ccaf268e798723c89c5b
    role: context
  - path: pages/category/genomics.html
    sha256: d152427320df0b37755cabe558e10fd0e6e4adb7eb960fb3217b97340457bde6
    role: context
  - path: pages/category/metabolism.html
    sha256: 7812c8509cad6dad56d0a9335f51f259414a775108e18403804acd92563145ca
    role: context
  - path: pages/category/morphology.html
    sha256: c18fcb086d1482da1b7dfbd8dbabff15bedfd1cc81155c1bebf4561b0caa7cce
    role: context
  - path: pages/category/observation.html
    sha256: 807d7473cfc687c89a0f7c220ac87b3f9f6c6ed2dc2bd889c4681556edb28f09
    role: context
  - path: pages/category/other.html
    sha256: 44db2e751888b6da9678024938b0cee09c0e4b3e7c08b3c94237f82b7f72710c
    role: context
  - path: pages/category/physiology.html
    sha256: 485f8416bac818b214fe28a720dfde1eccd0957ae78a288be5fe1c14cc539c7e
    role: context
  - path: pages/category/quantitative_property.html
    sha256: f95fa9baec530648579d368c141deec21ac476df9a14f9c17b6034158d947626
    role: context
  - path: pages/category/upper.html
    sha256: a87e97119ccc15353e1b57a2573c78b31da52b85c03946e8acc400def481ef3f
    role: context
  - path: pages/graph.html
    sha256: b02b358eff3156e7472764d01b68508d7b65393f4135a267a8c13a3bfdcbe31e
    role: context
  - path: pages/index.html
    sha256: ed1ebc1a7b001f5dbea8e19c7b91c392f35f5d46ce3958b01ec7c71b6a89ec5d
    role: context
  - path: pages/traits/ecology/animal_pathogen.html
    sha256: 8c44862db294c5d30e9ed9321470cf8cfe678da7553e024e5ba51518850bce34
    role: context
  - path: pages/traits/ecology/bacterial_cannibalism.html
    sha256: 74145084e49a474d2fd7eed559e3df02d0e8d23e13c273039f3b43062d41c058
    role: context
  - path: pages/traits/ecology/bacterial_mycophagy.html
    sha256: a45ab967a3e320d96e5f8ab7e86cd0f4b3a81369ea18ef3e1779d848589b2074
    role: context
  - path: pages/traits/ecology/biofilm_formation.html
    sha256: dd754fb906b5ab7506f7bb51a2c948d6d83484491fb517634a3a101275f57903
    role: context
  - path: pages/traits/ecology/biosafety_level.html
    sha256: 58c45b647c7e35197152fbb457346b8c80ed565b73cb6e00dbc20b5b31897aa4
    role: context
  - path: pages/traits/ecology/biosafety_level_1.html
    sha256: 16db200edd0e96899d7e056e0ddb3312ed0be827becbba540f834b68013715b5
    role: context
  - path: pages/traits/ecology/biosafety_level_2.html
    sha256: ebb174eb6f57237d4a5199cf1bba85d68e11ae9ae2037fde1dc700e98d2020ec
    role: context
  - path: pages/traits/ecology/biosafety_level_3.html
    sha256: 264c427e56f3c7a4b6bf066bb56519e7de2a2c313b07f554cce7063842f84d0b
    role: context
  - path: pages/traits/ecology/biosafety_level_4.html
    sha256: c8c6b5a76cd6775b021c9e3ac516553b1359aa03bca95bb06d2ebf42c540a296
    role: context
  - path: pages/traits/ecology/biosafety_level_5.html
    sha256: 380a21bb651230530bb51f83895719d54a284a43eb3c61d03f1d4de61cbe292c
    role: context
  - path: pages/traits/ecology/collective_bacterial_predation.html
    sha256: 0384015e86366c06c84e946c29bfa10f8036187823ad8ca8e96090e946f3b4cf
    role: context
  - path: pages/traits/ecology/commensalism.html
    sha256: 3df54f7913bb8a6a68c7d9079f31c7c66ad553548f0a30c32d1e76ab7c455d1f
    role: context
  - path: pages/traits/ecology/cytoplasmic_bacterial_predation.html
    sha256: 33cae5107787be844176ababeec6f2f3cc6a4b19f33104d034a0cdf073313aff
    role: context
  - path: pages/traits/ecology/endophytic.html
    sha256: 237599d4f3a7e303d60d4492751d7d79da3d09dcde27b931e2022b9c1decc9c0
    role: context
  - path: pages/traits/ecology/endosymbiosis.html
    sha256: d731b029e12f7c17147819bca636a58996c57c1cc0b23fe66e434146c01199b1
    role: context
  - path: pages/traits/ecology/epibiotic_bacterial_predation.html
    sha256: 14b0e9f6b18c4dfe0da29b3ccc45580e7c63a05804b759cd0cbcd514dbab90c4
    role: context
  - path: pages/traits/ecology/epiphytic.html
    sha256: 913d3d4bf1c3d4ba46a0c37e4fe84f0973b73bb790867c43ac9b1c5bf33d8d27
    role: context
  - path: pages/traits/ecology/free_living.html
    sha256: a8e5165034515a638630e865b87773c4dc0f3c02f0859d322a725fe1199798f1
    role: context
  - path: pages/traits/ecology/fungal_nematophagy.html
    sha256: 78f261723546cf2a1c7c6a7d0f87796e37f5403f9ff3df804faf6a30609fac84
    role: context
  - path: pages/traits/ecology/gut_associated.html
    sha256: 1a82ff58ac8898d17322c9027ee89c3edd674b47febf58cbe8752b8b798174a6
    role: context
  - path: pages/traits/ecology/habitat_association.html
    sha256: b05d8c03eddfe64d12c6bd3d6181287acaa4cba7d3b18d93e864b3baa21c71ec
    role: context
  - path: pages/traits/ecology/host_associated.html
    sha256: c96fc6a2f12924753b39190294b62b2b7f8517576c5d543353672296294bc104
    role: context
  - path: pages/traits/ecology/human_pathogen.html
    sha256: 2617c96e4304482100c5bf5e6dd84aea1b112f98e27f3a85c3119d9ac7b65956
    role: context
  - path: pages/traits/ecology/ixotrophy.html
    sha256: 5b8303e5bf1578c15642bc88d18a345501077e44feed5dbfd9d892191b8e021f
    role: context
  - path: pages/traits/ecology/kin_discrimination.html
    sha256: ebe71cbbb8918d08e2e47826514594e8e2a860236a90acbf5cbbbb5e68426bf9
    role: context
  - path: pages/traits/ecology/mutualism.html
    sha256: b53adb404728e91a98d68237a5531078477949257f854a3495237b52a67cebb7
    role: context
  - path: pages/traits/ecology/nitrogen_fixing_symbiosis.html
    sha256: 927fd460aa516aba7afb5ab17c4307e9238390e1a837196b7b6f90f38c48afc2
    role: context
  - path: pages/traits/ecology/nutritional_fungal_mycoparasitism.html
    sha256: 19a3414d262c158f0b258adcc9bf716ce523e50142e0a19633bcb45bd49b99dc
    role: context
  - path: pages/traits/ecology/opportunistic_pathogen.html
    sha256: 7c28d712007c23fb5e82cd74e624937ea7c254daed51e456e9d23608e82462fc
    role: context
  - path: pages/traits/ecology/parasitism.html
    sha256: e05e0071ab3bd165550a2ac7eef124016305c192864e5d2b51824751a3ed6f8e
    role: context
  - path: pages/traits/ecology/pathogenic_to_host.html
    sha256: 994b717e29ad28396aee0865675cf004a7a96608d672eb671e09f543ec6db894
    role: context
  - path: pages/traits/ecology/periplasmic_bacterial_predation.html
    sha256: d3008d1de98eb57cfdec3dde03b02833cbd737c889ddc23f4e713ed00e255a36
    role: context
  - path: pages/traits/ecology/plant_pathogen.html
    sha256: 430f2b8d0d085a76b3ad731df63c39043a16b8554209ce7f3828fbb0663b3c79
    role: context
  - path: pages/traits/ecology/predatory_bacterium.html
    sha256: d80fd270b807e76c42d573c06a8cb4f3185710e42d8aca605a4b6be12e98bc07
    role: context
  - path: pages/traits/ecology/rhizosphere_association.html
    sha256: d5b8b710ba08eb1462253c77e1fa38cfbb4eb178baae329db7f3df1311f07dca
    role: context
  - path: pages/traits/ecology/saprotrophy.html
    sha256: 9c67e9fab0d1db4e470499dbf27aefbe5e26ed24c1ba849a2ebd74a8c888e902
    role: context
  - path: pages/traits/ecology/soil_dwelling.html
    sha256: 74d63405d5f07598347028fde420afcceaa2d15204f2b769f902f50d4b37a108
    role: context
  - path: pages/traits/ecology/symbiosis.html
    sha256: 40816a7972c8e176fa0c05aff7c86e152d8d3594a84b5d93dd523fb444a2288e
    role: context
  - path: pages/traits/environment/acidophilic.html
    sha256: 96e551fe909bf6e811e6a61f1217ce79692d6152487d5aa517db3bd8317c28b0
    role: context
  - path: pages/traits/environment/acidotolerant.html
    sha256: 194d8b31015f070a483c8013347631f3c59d64f958aa4db9fce269d4b87f6dfe
    role: context
  - path: pages/traits/environment/aerobic.html
    sha256: 6343c8af47846ecb80d5a5fd2c0895ace88a222b2cb72bf36ce320bbb5321f86
    role: context
  - path: pages/traits/environment/aerotolerant.html
    sha256: 53accd93bd5ca02e29da7a9ad151b5188de7e3425ac8295ec51d45ef59feebb8
    role: context
  - path: pages/traits/environment/alkalotolerant.html
    sha256: 77394e2976095172a00ba7793cc4c5a24430cadb5035d3eec57f94a8e2b54852
    role: context
  - path: pages/traits/environment/alkaphilic.html
    sha256: 4e750c313e41827073142e8c55f2fcf4da1ec4fdd73d5f9fe4e9a04436b125bc
    role: context
  - path: pages/traits/environment/anaerobic.html
    sha256: 0d2dbbb228269bd983264c889de9ae83bb8284736ab6de256dbd878420ca3153
    role: context
  - path: pages/traits/environment/arsenic_tolerant.html
    sha256: 9bc0e5ac3fe89d7b7404504168dc6e912f7e2316e7a9ae45c399a5175f97b98d
    role: context
  - path: pages/traits/environment/cadmium_tolerant.html
    sha256: 1fd5bf4938e69e37b8aafb0ca183eda589f17b99bd78bab692c000265307962c
    role: context
  - path: pages/traits/environment/capnophilic.html
    sha256: 5bb9fa5b630629de1b5e212abbf53a0041aaae853589fc9b1015c6fd84d30eb7
    role: context
  - path: pages/traits/environment/cobalt_tolerant.html
    sha256: f84f6e6cc585eed3737a697b07806daf7b76e11d4ef95d8b95f547ab8c4e7f3d
    role: context
  - path: pages/traits/environment/copper_tolerant.html
    sha256: bb7b383f9309cd4bb66e958fe0495235f3a81a260ad82de28956478ac191d435
    role: context
  - path: pages/traits/environment/delta_phenotype_with_numerical_limits.html
    sha256: e144e5fa28cf7104b391d508bed543b1569042fa9b6d353e94083d7465d1bd6d
    role: context
  - path: pages/traits/environment/desiccation_tolerant.html
    sha256: 9b78bc89984376f199316e1ca0dc8f8b2ba8677d2f36c078e2d1f08d1fe0614e
    role: context
  - path: pages/traits/environment/euryhaline.html
    sha256: 118fb21948592477acbdfe0f96c9b91aca25ef4f338fb84e2edd5baa9805517f
    role: context
  - path: pages/traits/environment/extreme_hyperthermophilic.html
    sha256: 71c0a5c3a7eeb89f116fca8a5c2d8c09260428002cd8037e4c2ad042ff11a419
    role: context
  - path: pages/traits/environment/extremely_halophilic.html
    sha256: 40aa0836cf733fef3e7513a56b796ad480d9d1ec207f19f401487156409153bb
    role: context
  - path: pages/traits/environment/facultative_oxygen_preference.html
    sha256: 3b161898902be05673a92e5fda386c16b6331829be44e9d6129ef55fda748667
    role: context
  - path: pages/traits/environment/facultative_psychrophilic.html
    sha256: 3a03bba2100870059ea811f95babdba69f6f6f65411e1be7a596b855fa369e10
    role: context
  - path: pages/traits/environment/facultatively_acidophilic.html
    sha256: 39231851c3a4d7f57ce186bdcd8a585e9c36012ec329219dbb9bd5d9223c14e3
    role: context
  - path: pages/traits/environment/facultatively_aerobic.html
    sha256: 9949805348e8b9aa4b44a242ee38fa35849b9e47eb7fd5891a30add9cc705f89
    role: context
  - path: pages/traits/environment/facultatively_alkaphilic.html
    sha256: 0fdd4304d7c5fb483b0fbc539b17ba5707ac76ce619071177f51fa215b18ae6d
    role: context
  - path: pages/traits/environment/facultatively_anaerobic.html
    sha256: 18826006b53286383348306c0b925ef0506fd4abcc24738d975bee858140686e
    role: context
  - path: pages/traits/environment/growth_range_phenotype_with_numerical_limits.html
    sha256: 364bffecb297dd81f422dac937fd15831dd682263e4e6dcd0b677f6477ac88d4
    role: context
  - path: pages/traits/environment/haloalkaliphilic.html
    sha256: 6c58d4e179473e81f56f9ea84f36c33dde3c2a464419581baefd04fa086aa5ba
    role: context
  - path: pages/traits/environment/halophilic.html
    sha256: 31daacd6a9a36084e3d71ac421102a60ff697c9199e34a9a66b7c02b303d89ff
    role: context
  - path: pages/traits/environment/halophily_preference.html
    sha256: 1051dd47e63d09a0ea49ee06ab871cf286b8fcf2177ae0e5f169879f0faccc9d
    role: context
  - path: pages/traits/environment/halotolerant.html
    sha256: 7b62a520b88988639ea714d9f64f850ebc6c27cbade09755d582988e6d2cb073
    role: context
  - path: pages/traits/environment/hyperthermophilic.html
    sha256: ec01d75a38a2f486cb89108105c72d11e3b482b784cbfcaf65e2afa6c4859340
    role: context
  - path: pages/traits/environment/ionizing_radiation_tolerant.html
    sha256: 6eb1b0c3e17748434e17e2261919af0c3d21ce58cc484501fb18b8c3a2a4d2ff
    role: context
  - path: pages/traits/environment/mercury_tolerant.html
    sha256: 2832d3f4e508dad83cb998d762e40e89e46c3bceac03005441b9ecd22ed52ea5
    role: context
  - path: pages/traits/environment/mesophilic.html
    sha256: 931932abc824cbf4cbb3c3bc7fb2fa37ff549ef18b13cb26e11ce82588a67e69
    role: context
  - path: pages/traits/environment/metal_tolerant.html
    sha256: 62eeee326d00deabef041cd9cad50e00ca00303fa32cfab5be689da7d33544cc
    role: context
  - path: pages/traits/environment/microaerophilic.html
    sha256: d1931439154659b16aef098ae7710a69293b81d53625a687590d2eba4f273006
    role: context
  - path: pages/traits/environment/microaerotolerant.html
    sha256: 2a4e2b1346cd4a4bdf0046a9190429df19fe9543adfe4f73b4d258ea567eebc4
    role: context
  - path: pages/traits/environment/moderately_halophilic.html
    sha256: 6b1a04f64bb18ed7cd99d4d95f705f228d6cc3193b9bdf8ecbdc3d102dadb497
    role: context
  - path: pages/traits/environment/nacl_delta.html
    sha256: c81444ebac24fa30f8a805dc63c4dbfe275d278ea6153596aac26e83ab85ebff
    role: context
  - path: pages/traits/environment/nacl_delta_high.html
    sha256: 57825b76343afe4c18462cfc8011a20d8a1341a263481cdca3f7257b53e76312
    role: context
  - path: pages/traits/environment/nacl_delta_low.html
    sha256: 535235f6545c60209b2a17446261bf86a797b6fa9757825d9a6a277ad0e0be23
    role: context
  - path: pages/traits/environment/nacl_delta_mid1.html
    sha256: 05dce716a0b9de1ce517e8f724c96d5ae6f9f7925dd6f8d6f0a06cfadf3978fd
    role: context
  - path: pages/traits/environment/nacl_delta_mid2.html
    sha256: bdf11685890732b94cca5b17f166ebb4535532c0b8407ee7eb63f5d98fbcf176
    role: context
  - path: pages/traits/environment/nacl_optimum.html
    sha256: 25a3cbca4df6cea32874a3ed213b83a47518622dd59fce0ce8daf6daf61f9bc3
    role: context
  - path: pages/traits/environment/nacl_optimum_high.html
    sha256: 9580cb7038fa816f66a6ac50a355795a0659366582a1f741ae571ebccb0d35fc
    role: context
  - path: pages/traits/environment/nacl_optimum_low.html
    sha256: 7b03f0d79ceed1fcb9fe5ba0f20703aa77b06ca9437ee0fe2a42a0a904a2a74f
    role: context
  - path: pages/traits/environment/nacl_optimum_mid1.html
    sha256: d25d15c5d034fe4c14e01e2e680d48a20d99a80c23d838c1f90b9ef0bcbc4889
    role: context
  - path: pages/traits/environment/nacl_optimum_mid2.html
    sha256: 41b7d82be6062c1d05188c2e93385b5edb31fd6a0c0d58a7bac8cb2f2a0e01be
    role: context
  - path: pages/traits/environment/nacl_range.html
    sha256: 4eca8afc6840a0a32754aa1bc53a6b6410306510f4132dc1754b404bace794f1
    role: context
  - path: pages/traits/environment/nacl_range_high.html
    sha256: a4c1ffec72167d34bd2e78d398cfe87d86c337c6cc987a413cac16c0932b92a7
    role: context
  - path: pages/traits/environment/nacl_range_low.html
    sha256: fc27308d10147a336cc48a4c444da1483bdcf3ad374fcb23cf7ab6c7f142beb3
    role: context
  - path: pages/traits/environment/nacl_range_mid1.html
    sha256: 20fc6afd43f94b2a947e6c8c865e5e05ae4bd0758337825a91f68d78ba116d56
    role: context
  - path: pages/traits/environment/nacl_range_mid2.html
    sha256: 3986366e3ee77988b08538f64465cd86a485e38b0d02907e85447283a2114b8d
    role: context
  - path: pages/traits/environment/neutrophilic.html
    sha256: 3708f47d12bc8a7f0d48405dd44ba45dbfbcf093bd571c23ca4bc50801aea170
    role: context
  - path: pages/traits/environment/non_halophilic.html
    sha256: a8c1417951776bc428a067ae78bd5cfa578ab8996bfb743ba8b1b627f4219527
    role: context
  - path: pages/traits/environment/obligately_acidophilic.html
    sha256: 94b699ce512e1e4202cac1ca5a5d4872134c7e423014e9b4072f1c7d4196486f
    role: context
  - path: pages/traits/environment/obligately_aerobic.html
    sha256: 143c99dd60dded14307966f6ead813f9127600ffd45f39d6e4decc2dec2a8249
    role: context
  - path: pages/traits/environment/obligately_alkaphilic.html
    sha256: 1a9f157e5acdf8019f71cda6cca8fe887c2b08ac308dd801fa4cb00819462fcd
    role: context
  - path: pages/traits/environment/obligately_anaerobic.html
    sha256: de7ec3cd381f29fb1ed39ad09d82b6dd9540b3288f6476221ac777f717ccfbc9
    role: context
  - path: pages/traits/environment/obligately_piezophilic.html
    sha256: 0ddf6ac74e79a6670cb39fdb731642d6337e972c9ade8ab396e838945d499f99
    role: context
  - path: pages/traits/environment/optimum_phenotype_with_numerical_limits.html
    sha256: ada203013a9badd94c991922863ac187eeee3cd76c5fc51a04ffa8b5de4f6812
    role: context
  - path: pages/traits/environment/oxygen_preference.html
    sha256: 66df1e6e4b25bd0b8ca0ddc2c56b2c8583b30e322f5c78389d4da2f5e35df5eb
    role: context
  - path: pages/traits/environment/ph_delta.html
    sha256: 489be2c497597516914b3399f4fd6131700a35cbe74fb01ccde9395495683a42
    role: context
  - path: pages/traits/environment/ph_delta_high.html
    sha256: 48049a80cf7499dde93435aa416c6b0025782de0220daad3db66767a845477db
    role: context
  - path: pages/traits/environment/ph_delta_low.html
    sha256: eca82289171033df21d1394f74db9eb7baa4fe5e349abd5cdd141ef2db95b4c1
    role: context
  - path: pages/traits/environment/ph_delta_mid1.html
    sha256: 2731e10f86d368375d4c50cefa3c2b002d320fe1f7c6d9a01294f2680334bece
    role: context
  - path: pages/traits/environment/ph_delta_mid2.html
    sha256: 8073c14b655adcb68a063778506f8384e0c9b0cbafc67332c858bdb0ceab23b7
    role: context
  - path: pages/traits/environment/ph_delta_mid3.html
    sha256: 70c8c537160159fc5fabd93c82ff7447610c645eb09d7edf635d4bf680c7e738
    role: context
  - path: pages/traits/environment/ph_delta_very_low.html
    sha256: 5e0057b6d1f0084c749f88a265be3387d351d27d8f43b6ce93f4f229f2f31f47
    role: context
  - path: pages/traits/environment/ph_growth_preference.html
    sha256: a3efd303c81d8489e403af095b3373cba88c84a4ab49c509b57906269dfc4bf7
    role: context
  - path: pages/traits/environment/ph_optimum.html
    sha256: ee03236efff28456b76646d7fdabb60528f4471f17485605034b9d6545c3e57a
    role: context
  - path: pages/traits/environment/ph_optimum_high.html
    sha256: b95dac61bae8612f5fda432b28bb6fe4538fd73bc22fb7211f7eec2817c0aa14
    role: context
  - path: pages/traits/environment/ph_optimum_low.html
    sha256: c6f43dcc72b2833723ad6d4bdae196502fbf3500037a06dcaf2b49175e7f2c61
    role: context
  - path: pages/traits/environment/ph_optimum_mid1.html
    sha256: 0b7a880bd85ffb00458d2147ff94b2fe5e08809abf3ace58903000e25e772e83
    role: context
  - path: pages/traits/environment/ph_optimum_mid2.html
    sha256: 451959d5d95004a78b4a8d81a8efce6d8c46235e56238f3241a7509583f6d92e
    role: context
  - path: pages/traits/environment/ph_phenotype_with_numerical_limits.html
    sha256: 4609489d4327eca65d5b5a646f200d2742d82766ed3d04f3946a84e4b7af0621
    role: context
  - path: pages/traits/environment/ph_range.html
    sha256: 90e6a0feb4d5babe37a0c417ca15b95793b96fa15ce412919760816ffe918ddb
    role: context
  - path: pages/traits/environment/ph_range_high.html
    sha256: 9e9883f5dd343130d827ef982856b22032b62741b1f3e748b22b587dfb5c794c
    role: context
  - path: pages/traits/environment/ph_range_low.html
    sha256: 81fa98882138c6f2034418fff05b2c3e2c868f13c765a7c4a35548e209e2fce1
    role: context
  - path: pages/traits/environment/ph_range_mid1.html
    sha256: b25a369328f59e0732161e16d2ccd34328f5e372cdf8cda4a719c7a14e47a3cd
    role: context
  - path: pages/traits/environment/ph_range_mid2.html
    sha256: d81ee6306173e2dd9c2f30567bc84d3a5f301a8b152b9a454245aa321dfdc714
    role: context
  - path: pages/traits/environment/ph_range_mid3.html
    sha256: df56fa9e68633e2dba21d8477cf5d89614560d8404dfbe5b9137c46129cefee1
    role: context
  - path: pages/traits/environment/ph_range_very_low.html
    sha256: 9fb847ce9ea799292c4eda47fa28486e07062319a24e926ba370fe8070be1c1c
    role: context
  - path: pages/traits/environment/piezophilic.html
    sha256: 0d5bba8ffe619cc7eb2e210f5d5fd1026b6fc9f6b2288adef359d33085ae94c4
    role: context
  - path: pages/traits/environment/piezotolerant.html
    sha256: a368ee064fc6512f325af07fde9e78d1edfba7ca7e741853ff1782382a620bf0
    role: context
  - path: pages/traits/environment/pressure_delta.html
    sha256: 37529168f05f2cd05a00ebfb17068657b4209c0a287ff47d0ace36c579891edb
    role: context
  - path: pages/traits/environment/pressure_optimum.html
    sha256: 26b7686ba1b691f08c3ccd1fe180d4886036574381311b58cd128cf59e03e23a
    role: context
  - path: pages/traits/environment/pressure_range.html
    sha256: 1dc9300604278abe903920869069260accfdb1a6f2d1be8bdea1fd64008555fc
    role: context
  - path: pages/traits/environment/psychrophilic.html
    sha256: 0c1b329356d67a338e82fc92ee50229a832f5c719f655be729c62a93fefafc9c
    role: context
  - path: pages/traits/environment/psychrotolerant.html
    sha256: dc2d06be436c8e4a0364d6fd7658c7318baf86d2bf556a68ca1f8e3153e492e5
    role: context
  - path: pages/traits/environment/radiotolerant.html
    sha256: d2b360ebf26e2f22884357e74cde30d050fa489deb51298ee05da230ed07fb6f
    role: context
  - path: pages/traits/environment/salinity_phenotype_with_numerical_limits.html
    sha256: 835f393706ec4abef1bff5d29856858639b990fb880e2708a6a4a57a661a6dbe
    role: context
  - path: pages/traits/environment/slightly_halophilic.html
    sha256: 0365444477e847b8480d0e021aae34cba10cc532f2d7fcec59760ec686223811
    role: context
  - path: pages/traits/environment/stenohaline.html
    sha256: ee1129784f138be4f34defa64c756bd9f52b50afa142f74aba440b568268f745
    role: context
  - path: pages/traits/environment/strictly_anaerobic.html
    sha256: 75d7bc56db63a6091457709d3538080e0666e7d145344c1adbe79af3926f7eca
    role: context
  - path: pages/traits/environment/temperature_delta.html
    sha256: 6c85279c0873e2af6c9a97ca4cf5f7f04071178162ee778c7bf18ff586745b8d
    role: context
  - path: pages/traits/environment/temperature_delta_high.html
    sha256: 470908a4c1343b03d0c1c7c5d3f116fb25808faf55afd236766be847d39865d9
    role: context
  - path: pages/traits/environment/temperature_delta_low.html
    sha256: b93a7dfde4d6981238950205b7ff5098966a2d5e2240d3dcc9a6b2bea13983e8
    role: context
  - path: pages/traits/environment/temperature_delta_mid1.html
    sha256: d7e8e73ac18fae688f18d797a986f858aee4c397993e026690307bf467425264
    role: context
  - path: pages/traits/environment/temperature_delta_mid2.html
    sha256: 526cead75d85a4323ff750a631a5d16e00e4d4bc8b5d16e9a475228fa2241d23
    role: context
  - path: pages/traits/environment/temperature_delta_very_low.html
    sha256: a0f43fb9bff84e8149c0f7821e81edab2f5e67be409c634c129411ccd6deb08d
    role: context
  - path: pages/traits/environment/temperature_optimum.html
    sha256: 28a87d41460a9f7045cc08d745fcdf1d1005cf1fbc4b16bef535a5e796f54592
    role: context
  - path: pages/traits/environment/temperature_optimum_high.html
    sha256: d63fda81ec99ee4f965ae0eb8276f2e3dd1df46197566c300993a7e2433d4be2
    role: context
  - path: pages/traits/environment/temperature_optimum_low.html
    sha256: 88bc9cfcc54837fc35edc7f7f40d65669896052c5086baec365a641ca5f7b50e
    role: context
  - path: pages/traits/environment/temperature_optimum_mid1.html
    sha256: c3a3b9b883b0bfa1f5a7bd5547baf0eaf9df21aa16191668649f3ffd558aaf1e
    role: context
  - path: pages/traits/environment/temperature_optimum_mid2.html
    sha256: d42295d6cde311491be38e792ce78b241c54db4a60535f299d7c55ef0c988907
    role: context
  - path: pages/traits/environment/temperature_optimum_mid3.html
    sha256: eced75fd023759d3543d71cc573761c57ab33443d93b697aa8276a49db8f07a8
    role: context
  - path: pages/traits/environment/temperature_optimum_mid4.html
    sha256: c7f69077dadee6f3399fa6e3425fdb700ca458e577c4bff06ddaaeb578565826
    role: context
  - path: pages/traits/environment/temperature_optimum_very_low.html
    sha256: 2f35d2dbb62d08bc296185e380618384c4d3c5a509fe55e699d41951c5ba6186
    role: context
  - path: pages/traits/environment/temperature_phenotype_with_numerical_limits.html
    sha256: 45e2ead27e78d88b3bc07f4a0a677684988f516371c49268f3f69965cf048352
    role: context
  - path: pages/traits/environment/temperature_preference.html
    sha256: dfbb5c87a94ba8ef7f88b4898ea719a7c4793ec72359495fbc1bc1f1637b5e54
    role: context
  - path: pages/traits/environment/temperature_range.html
    sha256: 2267f703cd7b72612564d8e90a9db0dec5e06e2f31e93c3d2bd5c61d5f645365
    role: context
  - path: pages/traits/environment/temperature_range_high.html
    sha256: c52dc6d92d7193f9f69d80eaaefed00c2d260d8e7c3eefdda19d2279aea9c52a
    role: context
  - path: pages/traits/environment/temperature_range_low.html
    sha256: 1c1f8d0f685aca62af6b577a34481d0aca517dd8939fef1709d9f6d4899ad3a0
    role: context
  - path: pages/traits/environment/temperature_range_mid1.html
    sha256: e35648cd617c2130d970e8e539fe2ce6a9fdee648b890bf7649f9365c53f20be
    role: context
  - path: pages/traits/environment/temperature_range_mid2.html
    sha256: 589daba8441ede784d39de185ff57aae8c05e8931ff49126144679883127ef84
    role: context
  - path: pages/traits/environment/temperature_range_mid3.html
    sha256: 3306e1a3c4f87f001ea600193226206cfe6ce17df63ead75b93da0abdd5b6a88
    role: context
  - path: pages/traits/environment/temperature_range_mid4.html
    sha256: c7e1c02c89dd3084f614f7d66f55337faf8b2248dccc1ea89141c8f2d51ef63c
    role: context
  - path: pages/traits/environment/temperature_range_very_low.html
    sha256: 47374a53ae0aefced233536964675a3a35dbd8170a5d7a4db550ecff930d3cfc
    role: context
  - path: pages/traits/environment/thermophilic.html
    sha256: e9d2dcf3d90dee3f633d46068bcf669dee41461ad49c9be6c506de1119c52520
    role: context
  - path: pages/traits/environment/thermotolerant.html
    sha256: a1eff1ea746b167120733c3038b139ce9390c28aae11e7b481b35a2292944b56
    role: context
  - path: pages/traits/environment/uv_radiation_tolerant.html
    sha256: 4381cab2d379c1b9a054c0d4efb3a22539cc7831b437fe2dbfb5ae515a6a8bb9
    role: context
  - path: pages/traits/environment/xerophilic.html
    sha256: 4d6237a373267d7f0f7900dec37d19f7dcaaba70069d800fde828f5ea96ca072
    role: context
  - path: pages/traits/environment/zinc_tolerant.html
    sha256: d4e9d17c78803db262aa58ead0f1464357973d3651183fa36dab4e3c438b95c6
    role: context
  - path: pages/traits/genomics/abi2_system.html
    sha256: e3f52fe5b5faa90eb3a4f51282286be69acfdfb2e4ded710821b0aa413501e9e
    role: context
  - path: pages/traits/genomics/abia_system.html
    sha256: 8f5fa1c958c833894bc401a4a715b824e933f97ca2d74f2f1d7a9e0cb87cafdd
    role: context
  - path: pages/traits/genomics/abialpha_system.html
    sha256: 853c6c5dc70a03bae900aaf53337b5b093e2265208b0a1adffca89a5f08301b8
    role: context
  - path: pages/traits/genomics/abib_system.html
    sha256: d3e355094ed2676f3617d146bf30cdc5a69e8ab112701c327f2940114811ee65
    role: context
  - path: pages/traits/genomics/abic_system.html
    sha256: bed74a84c1e39e9be43f8e1fbcbc4c4f367664718f857331aa923ab53084b754
    role: context
  - path: pages/traits/genomics/abid_system.html
    sha256: 78d316c68747029402bbdbd920072d5f5da62192e211abf16acb193c9f58b175
    role: context
  - path: pages/traits/genomics/abie_system.html
    sha256: bb2365653feb45a0cbaef23e8272241569ad187e5f44d9a71b126fdf6c321ff7
    role: context
  - path: pages/traits/genomics/abif_system.html
    sha256: 94c4fad0b8e54f778e108a3695472da081c34ca01dbbe3aa5054b663bf72a0fe
    role: context
  - path: pages/traits/genomics/abig_system.html
    sha256: e6ccc0a578ac8add258bb6324f0322edd7c8bbaa75012c9ce4e35ae4b9e6b26a
    role: context
  - path: pages/traits/genomics/abih_system.html
    sha256: 4f80b3d8e04a1e684cabc816e1e7d03ff043340ed2fa202a7445976204e1b1fd
    role: context
  - path: pages/traits/genomics/abii_system.html
    sha256: 0f838b6df60391f82245ca9e0fc44f8334cbcd7bf3185aeb8deb58bc368e4f22
    role: context
  - path: pages/traits/genomics/abij_system.html
    sha256: e91e7e111669f321f856d7b5d2cdd887000ada22b570605e243ecaad71cd47f4
    role: context
  - path: pages/traits/genomics/abik_system.html
    sha256: c470e0e0122d325d346a33310ecfe8f8488a7bfb7268415d116d49fd2db4e3ad
    role: context
  - path: pages/traits/genomics/abil_system.html
    sha256: 43324b3208c3777a4bd12820f9fe1cb935ce3700f17d903faf317e47aa6a35d1
    role: context
  - path: pages/traits/genomics/abin_system.html
    sha256: 66bcf78282676d4b05d593029819499ed8834c66a6f8291d902418b572dac953
    role: context
  - path: pages/traits/genomics/abio_system.html
    sha256: 2370bfaa29cd2116bcf3930b479cfdff660dc4dbfeb48a54b2d8ac133d923b2f
    role: context
  - path: pages/traits/genomics/abip2_system.html
    sha256: 0a9edd44bb4b4f66b47759c44f6261ef02da426f4e32cd9826c521bc643ece18
    role: context
  - path: pages/traits/genomics/abiq_system.html
    sha256: 7afeac2a8f89f3eca10cd46791ba194a8934aa2c88808cc16037aac59d4c7315
    role: context
  - path: pages/traits/genomics/abir_system.html
    sha256: 7ca8c0070606f0a6dc7daa55f06acca4ff670c2b3e2ffcfcfa8ac8b2363d28ba
    role: context
  - path: pages/traits/genomics/abit_system.html
    sha256: 4422cbdf5fc2b43ef65bf0e42155b1a4de67e488866f4f9854214340827eb29c
    role: context
  - path: pages/traits/genomics/abiu_system.html
    sha256: 36b7e6048c2ffee5b832537bae758b13a88ad23f101fa3c9a85369d8fb97658f
    role: context
  - path: pages/traits/genomics/abiv_system.html
    sha256: 4fa2327e785ecf6ca04513629f884b78acbcf3cd0aac1a70b72ebe88a5dcb039
    role: context
  - path: pages/traits/genomics/abiz_system.html
    sha256: c613d2e7d415e828d78a92fbb44a10c7afde909d811ef35d24ca808083678c74
    role: context
  - path: pages/traits/genomics/abortive_infection_system.html
    sha256: 7d7d6ad558196be970e40a7f101707d0ecf08a195e0e7733288986765c74aac6
    role: context
  - path: pages/traits/genomics/aditi_system.html
    sha256: 3aad5f3d06bf9b6f8cc12d90342b0e1f2ddb8a0de91d87d59c51d0ca281cb6f4
    role: context
  - path: pages/traits/genomics/ambrosia_system.html
    sha256: d05781a84f3faa8d9ebbd05cfeae272aed0551241e9cb17af174ff420a12483c
    role: context
  - path: pages/traits/genomics/apsab_system.html
    sha256: ecd7655b96984b67032de0d9f9040006bc574d52c1ff05285b1d39d5d466dcc7
    role: context
  - path: pages/traits/genomics/aristaios_system.html
    sha256: 5ac38439eb4e3cf62eedddde796c33343b980dc731fbfb2a24cf64e8f3731f7f
    role: context
  - path: pages/traits/genomics/armada_system.html
    sha256: 4399f6894417bd901a23e9b7cfe0cf12ab17d40e8acf7284b512206177a6ee42
    role: context
  - path: pages/traits/genomics/audmula_system.html
    sha256: 722abf3306375473bec070d80c1c2498500a2b634fd507d43b309c0d41790a9f
    role: context
  - path: pages/traits/genomics/avast_system.html
    sha256: a54a4f4af4ed11b10e6ac2f2440511e4f257719bdbb5d2d4623a5ceeea8162f9
    role: context
  - path: pages/traits/genomics/avs_i_system.html
    sha256: 2fac396243034bf16a99d7bc9aa38b3d5b8acc9cba8ba83c7cea6575bac22027
    role: context
  - path: pages/traits/genomics/avs_ii_system.html
    sha256: 883c5ddc1d78cac7280de1b4b6b6ad948ad87f23fcf2574429f944f33133f73c
    role: context
  - path: pages/traits/genomics/avs_iii_system.html
    sha256: d32a211c0894c31ce4f8764340cd8dddf505b12d5a80a53906dcebd2be4a1f29
    role: context
  - path: pages/traits/genomics/avs_iv_system.html
    sha256: 91a9aa0c3649dd75e8ee5dd43623399dee9f877792331e1048156cede986f4da
    role: context
  - path: pages/traits/genomics/avs_v_system.html
    sha256: d03e90bc5e86eef5ae76340c83137e7cb4c423b0a3cd38cd1919378194156167
    role: context
  - path: pages/traits/genomics/azaca_system.html
    sha256: 874aff7388fbf4efce4f5d96ec367621e86514e3ae32493863b46f8411438d4e
    role: context
  - path: pages/traits/genomics/belenos_system.html
    sha256: b4d3fdea1032f57c310fbc3843411c5889b7e26633f8d29e3c6aceff029e19fc
    role: context
  - path: pages/traits/genomics/belisama_system.html
    sha256: 1ac721cf992eb236b397ed88510e97bc0e6946992287d85bce8e4b35406ffa52
    role: context
  - path: pages/traits/genomics/bil_system.html
    sha256: fac03a0341adf82e4f07d74150aa3c19dbd1dbb0aff085d95e61b7ae96809c2b
    role: context
  - path: pages/traits/genomics/borvo_system.html
    sha256: 6663309cb6237939fa19284421ecb64d4239ff338da43f07b0056748be7e6436
    role: context
  - path: pages/traits/genomics/brc113_system.html
    sha256: 0a3c5fc81b43c4cd719f14daaa27dfa6ba1625af7a4e0b8cc0a928160ff5f80f
    role: context
  - path: pages/traits/genomics/brc142_system.html
    sha256: 9e75cda481454dad6b4c7ac18cf15433c54c8c1f4f3a74963ac19e940fac324d
    role: context
  - path: pages/traits/genomics/brc167_system.html
    sha256: bdb79bb248e0cd8ff641ed012049e12eaa66cc9f7eab80b4ef978d3394d1ecd0
    role: context
  - path: pages/traits/genomics/brc217_system.html
    sha256: bd4157b89d6ca9b478ba695b01b745053f297b9ae35ac2c8635ef7bc708a8dcb
    role: context
  - path: pages/traits/genomics/brc22_system.html
    sha256: 506d233a78bd10a628cf7ac7711b6b0691dc96c75415cc70fd99f42828fd13ea
    role: context
  - path: pages/traits/genomics/brc233_system.html
    sha256: b66560c74b99b7cee5f575c9993e5895465d46e5f14c1ee4c38b49fe8c199cdc
    role: context
  - path: pages/traits/genomics/brc23_system.html
    sha256: 82583a4ab4db767e00d5610a23df69c2533834de9d2a20a303d7a74e4cf81447
    role: context
  - path: pages/traits/genomics/brc24_system.html
    sha256: c494fef0aae396d3ce7b807b430e98dfca3938204bed5e4e02a930d5fda74dec
    role: context
  - path: pages/traits/genomics/brc59_system.html
    sha256: 0e1c942a1bb16c134808a5283782bc16faa3e661f7913695a3603a0fff9d9b4f
    role: context
  - path: pages/traits/genomics/brc76_system.html
    sha256: 7933802cff1c5d97f063c3cb8fdd436b362ae51af12c03d86601d363bd7e14ec
    role: context
  - path: pages/traits/genomics/brcwgs21_system.html
    sha256: 0f36ab3275606f7038e8e2ae637de6a03cb633455e9cd017bd700b8b8f7e990f
    role: context
  - path: pages/traits/genomics/brex_system.html
    sha256: f165ae0d0de442837f21541175f2c5cf8644b60af82e2b7ff36a4657fb8012ac
    role: context
  - path: pages/traits/genomics/brig1_system.html
    sha256: 595026a8566184ffa2adbfe588b4554bef11aaea65a903ce09fb77abc2df7cd5
    role: context
  - path: pages/traits/genomics/brigantia_system.html
    sha256: 8f5da804a7a7ee06243be3237aae902da31fcae5d5c7d67d0e42e030e8c95683
    role: context
  - path: pages/traits/genomics/bsta_system.html
    sha256: ee10a5577db3c4b63e92dd3a11d694fd6e913924ed988444dd85c823fd8e9473
    role: context
  - path: pages/traits/genomics/bunzi_system.html
    sha256: 041d7063da6aec7bacb11ad5238c0dcdb6acae30ca420d4c94159028cefc1d95
    role: context
  - path: pages/traits/genomics/butters_gp30_gp31_system.html
    sha256: 3c7c93c4626f64b44222106377698bf6d76016a5a3bad5191ec75b836406266c
    role: context
  - path: pages/traits/genomics/butters_gp57r_system.html
    sha256: 8007090e603cec534eae52d0ea5086184d7b9f66701ec6546b5b4c2a4d16d147
    role: context
  - path: pages/traits/genomics/caprel_system.html
    sha256: f0fab1e463b617bf5242fed5527e13ee98cd70248d25fbed97d023a1e54f8f46
    role: context
  - path: pages/traits/genomics/card_nlr_endonuclease_system.html
    sha256: 0c85698c054155f3104ad1e13d93fdf9f6e5807888d17bfeadac70102fac8ba1
    role: context
  - path: pages/traits/genomics/card_nlr_gasdermin_system.html
    sha256: e938162cff9afc3c9108fb8d122f821d9d035ed50d0b191fca1628232ba15355
    role: context
  - path: pages/traits/genomics/card_nlr_like_system.html
    sha256: 7f84bd7906d75c79b50ac78e2950f03783b0f7d6796cebcddae1849010a7f17b
    role: context
  - path: pages/traits/genomics/card_nlr_phospho_system.html
    sha256: baed54424d18234f193040777960852d5ef8eef775541fae50493e36317b7858
    role: context
  - path: pages/traits/genomics/card_nlr_subtilase_system.html
    sha256: 343c5bc5eea587034826534b43a20f015e5d7d2dd38f57f7a920d9e50e464f94
    role: context
  - path: pages/traits/genomics/card_nlr_system.html
    sha256: cf6772f692860c6aef5a6609835d44c936148fc2ed658a052e3aa402725671ea
    role: context
  - path: pages/traits/genomics/cbass_system.html
    sha256: 5810d7362cfe8f57bf67a7c5a04f4290a31944c341356fa966736340402de425
    role: context
  - path: pages/traits/genomics/ceres_system.html
    sha256: fa6d49959d496dc6e0d44cbfa2f3b864e1697214f78a09dd0d83e21f52d62095
    role: context
  - path: pages/traits/genomics/cernunnos_system.html
    sha256: 8ca5155a22e4577722b22086004448f3bd231a1ee252b346c9a2b47ffe9102f8
    role: context
  - path: pages/traits/genomics/charlie_gp32_system.html
    sha256: ec9f79489acae5f6652a0e9222db612457a7a13b0ea8b45a5b2cf06ad6bb70e7
    role: context
  - path: pages/traits/genomics/clover_system.html
    sha256: 9977ba7852cc5b95269ad0377d9128ff671bab121433b7e6b35947dfc644fd1d
    role: context
  - path: pages/traits/genomics/cmdtac_system.html
    sha256: a66eeaf4b9ab7c0e2f0da5974b4cfac8f62006115c2f811067598b592c9f1077
    role: context
  - path: pages/traits/genomics/coconut_system.html
    sha256: 9d93a623c2fda952226bd5932d448b462d4854d0f4ceb4b81949435c207a18f0
    role: context
  - path: pages/traits/genomics/codon_usage_bias.html
    sha256: f539d0151f2a21b543bd3c6172883bee3b84c8ea689d383c363ba3599d85fab3
    role: context
  - path: pages/traits/genomics/crispr_cas_system.html
    sha256: 6e177f14ee9e264c316ecb77c0c7fc88755324e05a3b46a3adaf5c88ad86f622
    role: context
  - path: pages/traits/genomics/crouga_system.html
    sha256: 0560fe0acf4a785b96cf91c02c0d0b0e8cead9389e71e9901dc5ca949ec9e3f4
    role: context
  - path: pages/traits/genomics/dag_system.html
    sha256: 726810b01a9c1df3b48fa5619be00c42426be06e6521b082fbba0e67535b7b81
    role: context
  - path: pages/traits/genomics/damona_system.html
    sha256: da4279e83569ab6f5053185d10c1d733c5f96fde4b2cc4e641dbc66f98a77b2f
    role: context
  - path: pages/traits/genomics/darna_system.html
    sha256: 73fe282b3d56c15d31ceeaa155d2450b2cf11aa426eac5c19d267ae5dde4dadb
    role: context
  - path: pages/traits/genomics/dartg_system.html
    sha256: cbefee51b3afe3e02b80d32e8a8328ae802ea7aa864cb7bf19de43493961da5d
    role: context
  - path: pages/traits/genomics/dazbog_system.html
    sha256: 9ca73510de57f9188f95d974eaf3035c0dbf66e51fd181be6da3ab831431a9e5
    role: context
  - path: pages/traits/genomics/dctpdeaminase_system.html
    sha256: 89ef7596210d9c636f1a8a6f91c9a98a9fc5f99f2291b3fc5af2e7b15922ce01
    role: context
  - path: pages/traits/genomics/ddmde_system.html
    sha256: 0c063d2686b49de6dac20c7b8aec1a832a7545c63a12423f40834787dd8ef067
    role: context
  - path: pages/traits/genomics/detocs_system.html
    sha256: a6db755278157ae6b8c4f2b55552877bb79ec3aa0ed9280bb413185ab0c43617
    role: context
  - path: pages/traits/genomics/dgtpase_system.html
    sha256: 5b61bd18e433af146667b0a8c31470d306ae89c316d03c42161f2474c72942de
    role: context
  - path: pages/traits/genomics/dionysus_system.html
    sha256: bdaf5fe5129390bd3f2062c1c01182c92b97bb475034e9c065856f8b922ca208
    role: context
  - path: pages/traits/genomics/disarm1_system.html
    sha256: 85198e5797243b430b2915790eecc2f43eee910c1fd745a0b36bcd598416e6f4
    role: context
  - path: pages/traits/genomics/disarm2_system.html
    sha256: 3b19b5df944a9bafb42005bfb378a4d079f2525be2d7d35a454cf9118d74f493
    role: context
  - path: pages/traits/genomics/disarm_system.html
    sha256: 14825a9605ce2fc72e80a5109238f286f45f1e63be3aded9d6771924b0c41c42
    role: context
  - path: pages/traits/genomics/divona_system.html
    sha256: 4984e55ab937e5bc473079698fe364e6dac89fb258659cb18d58def2d18fdba8
    role: context
  - path: pages/traits/genomics/dnd_system.html
    sha256: 3e989107fb6e589f96d5a11fdc61fada3eb81a7963dac99cfdd8a2a1f7b4e9f1
    role: context
  - path: pages/traits/genomics/dndcdea_pbeabcd_system.html
    sha256: 6418b7d99f85c49617591ffd7afb9d5ff9149ba0251449311b89c49242609a5b
    role: context
  - path: pages/traits/genomics/dodola_system.html
    sha256: e6b2508a0f4be50ab7869319aa0c2fecf014d87156b3b8f7863eb96442655f3e
    role: context
  - path: pages/traits/genomics/dpd_system.html
    sha256: f2feaf005f715633c64175c5c3e305b4e2dd7cd8540feb96e845ab6c63668965
    role: context
  - path: pages/traits/genomics/drt1_system.html
    sha256: 5e5d174ffc88631bd4e555fd1ef8c0f34777b2a80ac9aaf32677b8f16dd5aa82
    role: context
  - path: pages/traits/genomics/drt2_system.html
    sha256: 2e6a863d5d31e110664aa72cd5d9eeeeed4c9fdfd8b322886671ecafe53fb4ad
    role: context
  - path: pages/traits/genomics/drt3_system.html
    sha256: 133a0797492d2d0c2de238ae277dfcfdac87dfd0cecb0b6ea9ee12ea07e02766
    role: context
  - path: pages/traits/genomics/drt4_system.html
    sha256: f688abadefd3d34a472dde82cfe2a422bc798086d18af9ce6c7f07874cdac2b4
    role: context
  - path: pages/traits/genomics/drt5_system.html
    sha256: d7446af3b2ceb5b0c2e6c5c8d7721d8136d24f2488d40cc7fa6eebf9a4923298
    role: context
  - path: pages/traits/genomics/drt6_system.html
    sha256: b2d509096a383cae0cec925b61f35384d08d508e8027a84f454b957b2b5100bc
    role: context
  - path: pages/traits/genomics/drt7_system.html
    sha256: 12b854902e81699028cb5b72de394fa89e7c62c7dd4226bacded88ae3715c763
    role: context
  - path: pages/traits/genomics/drt8_system.html
    sha256: 0c4e79f6f1db4147622441ec5b2e58e279f4a518a7286cf51e67ba034409c218
    role: context
  - path: pages/traits/genomics/drt9_system.html
    sha256: 20010f294e7c4087c8807096f13de37dbe2422612c3bda993ea6e6b9a6c5b769
    role: context
  - path: pages/traits/genomics/drt_system.html
    sha256: 2583bfb10551c160304123848ad895d08e44bac17aa7bedac37f6ab1d10d598c
    role: context
  - path: pages/traits/genomics/druantia_iii_system.html
    sha256: c7d46d179e7bc21e90b77155683ac2037ca7d1275cbe65cc3b8723365cd8b9f2
    role: context
  - path: pages/traits/genomics/druantia_system.html
    sha256: a7a83d95580edb7de736315807b800e51c746d6373e63a7c1023c5138742c75b
    role: context
  - path: pages/traits/genomics/druantia_type_i_system.html
    sha256: 6ab0c41f56485f20250259cf7ba46918dd40df182e61db3b7d75ad6b81833790
    role: context
  - path: pages/traits/genomics/druantia_type_ii_system.html
    sha256: 061ee2d395541ce28d623e19aa73d486385b1a2ab487555dea8090aba016fd8f
    role: context
  - path: pages/traits/genomics/druantia_type_iv_system.html
    sha256: 6a7d2fa16a9e79e87d0c3b33ecfb7dce738bfd303f504bb9d8754164a8008e76
    role: context
  - path: pages/traits/genomics/ds_10_system.html
    sha256: 8222022ddad65412f14b0943aab55886f2227065867ca41681341a9f9c6c9a2e
    role: context
  - path: pages/traits/genomics/ds_11_system.html
    sha256: 85903e0d64fab32039b91051c664a4c2b7df114383e25b9eb41ff927fd42cc14
    role: context
  - path: pages/traits/genomics/ds_12_system.html
    sha256: 1804dbc57da8eb8394130b583fd5d2954ee70b26acbddfc26a802f35a40d8079
    role: context
  - path: pages/traits/genomics/ds_13_system.html
    sha256: df382c9d1954731ace49d98400234e0ad27b56bd9073cbdd8ad093bd38585614
    role: context
  - path: pages/traits/genomics/ds_14_system.html
    sha256: e8d8789fc762603574f89fa55960b638b3e38084468fcac539e827046682f60b
    role: context
  - path: pages/traits/genomics/ds_15_system.html
    sha256: 5b78436232684297af7126097c349b98d058363f8c8d07d80d0adad95a88b2b3
    role: context
  - path: pages/traits/genomics/ds_16_system.html
    sha256: d1d8f18c70af6e05b1288962b9ca2d0a5e4278cd75573694907a6eccfe3dcca7
    role: context
  - path: pages/traits/genomics/ds_17_system.html
    sha256: 4164b40b3693e2c19ecc0af494434629bbee03914aed767107f10c4d304434b5
    role: context
  - path: pages/traits/genomics/ds_18_system.html
    sha256: 52a1a83029140f36a704668f1623bf5edcbb1278f04d16003f434fbeba041164
    role: context
  - path: pages/traits/genomics/ds_19_system.html
    sha256: 0c3d05379cab2bb9631ec12818046e6258ccead7e22e199b2423776ed408a682
    role: context
  - path: pages/traits/genomics/ds_1_system.html
    sha256: 0a66d4fc4934b4d5ffe9bdae5fb6562520c4ce09a87874410f10a47b49214ce7
    role: context
  - path: pages/traits/genomics/ds_20_system.html
    sha256: 4581afdc9a503111cbe69cbfc5764e2b1c3217e0e38543bfa9b2bbe22f571bf9
    role: context
  - path: pages/traits/genomics/ds_21_system.html
    sha256: ae743bd06635affb4c7b32bd8dec47ac64ea85eebb8bfb7eb79d3cf95ace889f
    role: context
  - path: pages/traits/genomics/ds_22_system.html
    sha256: e0603bb3d7055966fb2a55bb48583ebe3075087274cd2a26cbe328d86eee5a67
    role: context
  - path: pages/traits/genomics/ds_23_system.html
    sha256: 71e78cbabe45f79aabab3eee895dcddd6490b92adc3ce5f911fceab00ab064e8
    role: context
  - path: pages/traits/genomics/ds_24_system.html
    sha256: 90444ec44b8c6d40f78cefdb70410abfa53ebc8706f7490eef6c3b49fccd1b38
    role: context
  - path: pages/traits/genomics/ds_25_system.html
    sha256: 3e7cc0f2f655620953ce6e221b22e15b5fbb540a3973862d3c0cf0f35f2b8da7
    role: context
  - path: pages/traits/genomics/ds_26_system.html
    sha256: b4c4c9c4d48e27ec941b62767f712479c7f02bd65cff27fc1968fe3b28696883
    role: context
  - path: pages/traits/genomics/ds_27_system.html
    sha256: 7520740e3a399e98fcee6a5bb685afe5a1734b7356c2657b4f35ae3770f52c5b
    role: context
  - path: pages/traits/genomics/ds_28_system.html
    sha256: 958543ce94fd9fef0d4b326d075b594bb9b51d34b7a1868d9d0d6181ff77bd5b
    role: context
  - path: pages/traits/genomics/ds_29_system.html
    sha256: d4c105292d5ad0b60c398c77637252ab48c7ff9c674996efa9e8014424967dee
    role: context
  - path: pages/traits/genomics/ds_2_system.html
    sha256: 292a7170ee7e74b3db7e627c54a76bf66b8242392d5033decc55b7e34687840b
    role: context
  - path: pages/traits/genomics/ds_30_system.html
    sha256: ee8447762798c3c1b39fa9435c90554126fcd8c309de01ed2c5e6fd917ed2ed7
    role: context
  - path: pages/traits/genomics/ds_31_system.html
    sha256: 6a6f1e2ae1d9a98bb5cd0b6258dfcfff7a189d7c3f54ed63d25d566a28327184
    role: context
  - path: pages/traits/genomics/ds_32_system.html
    sha256: 32fa939fec5dd8f43308e2fe7255170c1a6d145f92a98a3f3b593f6670a76023
    role: context
  - path: pages/traits/genomics/ds_33_system.html
    sha256: 5f055af7830457299282fe3393da13fd3e4deedd78f1cb79f2f04dee884c28a9
    role: context
  - path: pages/traits/genomics/ds_34_system.html
    sha256: baaa52420b4587f5b59abd01e48ef6227a1fe6bb8d358d61797c0e5acbc1402f
    role: context
  - path: pages/traits/genomics/ds_35_system.html
    sha256: f86c30c85c2f6a7ecf61a43ebb2f285dc23a15d541087005d0343a0a8717e357
    role: context
  - path: pages/traits/genomics/ds_36_system.html
    sha256: 1701fefcced797a611ad8b0ba85243beab4d763914060dfe46e3ce9e766ebaac
    role: context
  - path: pages/traits/genomics/ds_37_system.html
    sha256: 19d958d0ec376b5c56831d5dfa4d9098c4005b2f8e312bb5b8abc501e70a8eed
    role: context
  - path: pages/traits/genomics/ds_38_system.html
    sha256: 58da100d89cbd13df480eaf3a28aa8da6dbe4723fc61f80fa79a855de52ba943
    role: context
  - path: pages/traits/genomics/ds_39_system.html
    sha256: 421c6c8d9334c2353ccd92845b5a325b14208a368d338ed3d0581157aed81844
    role: context
  - path: pages/traits/genomics/ds_3_system.html
    sha256: b02c978de2492fb7089f63abf74c3038fca31908a406523171b5c8aa21afd85d
    role: context
  - path: pages/traits/genomics/ds_40_system.html
    sha256: 7b21eb94898a9412dc6e8955b00865080234b32a84ed71c4ab5a50ac459e0121
    role: context
  - path: pages/traits/genomics/ds_41_system.html
    sha256: 3f5298563cd86b512a7cbe7eec8b14618d2ed22fde1d73910884bf2f846a4cee
    role: context
  - path: pages/traits/genomics/ds_42_system.html
    sha256: 53ddbdfd64279e94500204d7f207ae73b30bfc2f691a72cd61f97837a7201f09
    role: context
  - path: pages/traits/genomics/ds_43_system.html
    sha256: 6aa565c29bd1025e91f0f1e0292066e2abd0f27ab5e7a31c5ca609bed30ab2df
    role: context
  - path: pages/traits/genomics/ds_44_system.html
    sha256: a7793a71bf0f431b1ae51697f6281412b842ee5ef17d49716a4f3f544450820f
    role: context
  - path: pages/traits/genomics/ds_45_system.html
    sha256: 0aa8836718f5542d0385fb4cbcbe114c2265b17879c2b1317ea1643a35dbf269
    role: context
  - path: pages/traits/genomics/ds_46_system.html
    sha256: 4383d48a5c764454299c7b02d2e43f79ef3702ec198f1c031e09ac8e076ac949
    role: context
  - path: pages/traits/genomics/ds_4_system.html
    sha256: c72c54f6aa19602d52d40c48b2086b4f1da65b9f103e5dc21d2565efb24a4126
    role: context
  - path: pages/traits/genomics/ds_5_system.html
    sha256: 867a855f371e7661f6fba5d09e9c7489aef96e7d73ec8dac64d0c8e05ed4aa08
    role: context
  - path: pages/traits/genomics/ds_6_system.html
    sha256: 5f8b27d0ad134bed63da16a12892c3e82cbf9615d82ab21d81bbbe71ca664702
    role: context
  - path: pages/traits/genomics/ds_7_system.html
    sha256: d63b45cc3279cb9a6658f25558ce151f844ccbb44d2ac122ff0f7564cf3d0a48
    role: context
  - path: pages/traits/genomics/ds_8_system.html
    sha256: 68146521c9ac1a44b33ef16f47abc712285d110cec57096a35daffdc7bb7b793
    role: context
  - path: pages/traits/genomics/ds_9_system.html
    sha256: a904618bf16109edac068672c41b7de9f718345520908bdd25f979bf436da22c
    role: context
  - path: pages/traits/genomics/dsr_system.html
    sha256: 8244fb1cac1657b2f2e5dbbfd6994f1c7ca95055f596228319c0609aca50469a
    role: context
  - path: pages/traits/genomics/duf262_schlafen_system.html
    sha256: 34e3c0350eabae119ce533c1372cf373a1ec9c19cbf16057600f0824bde0f775
    role: context
  - path: pages/traits/genomics/ecokmcra_system.html
    sha256: 03bda66777990e51a6f065ab883b5363883446bcf4ac43af93e454f805f0a285
    role: context
  - path: pages/traits/genomics/eleos_system.html
    sha256: 80b4f7714d452433f7fbed36d016b0d47980e347749ebd599a9c9dc3ddc9d572
    role: context
  - path: pages/traits/genomics/endpacf1_system.html
    sha256: d158c315b00009632a52e85e457e924944357b00fa37882583d794b8d95c346c
    role: context
  - path: pages/traits/genomics/epona_system.html
    sha256: ff3ab1a4fd1bce953b6b7f843b4669d88d770b621cc3b57446c27f26061287d2
    role: context
  - path: pages/traits/genomics/erebus_system.html
    sha256: 3a179aedb3808eb74c59b0600b790d19913386f05092f2c87b63555bdcfee155
    role: context
  - path: pages/traits/genomics/esos_system.html
    sha256: 3cc65f9d136cf569be346e509babb7c537f802380ecb59fafef543fec72dda85
    role: context
  - path: pages/traits/genomics/fliodhais_system.html
    sha256: 4e811ad6532b8e3fa2dcf8837cdc8b18619ff4c63aa98ae34cc669c0e5d97ee8
    role: context
  - path: pages/traits/genomics/fs_giy_yig_system.html
    sha256: 0df60db10ead0b9289165edb27330bc9d676a411ea32fb053bcabdc88ff85f97
    role: context
  - path: pages/traits/genomics/fs_hepn_tm_system.html
    sha256: 7c231b50a6f1a65de1881b005363b55e3749fb4b9d1642bc642042106204a4f4
    role: context
  - path: pages/traits/genomics/fs_hp_sdh_sah_system.html
    sha256: 6517b44c89c0e0669bf6ce113f4db5d61397e1560d716b9ed2919a79e7459174
    role: context
  - path: pages/traits/genomics/fs_hp_system.html
    sha256: 01ca639308ce59c60959a886dabbf27e100342d98b9fd20e35912ac66050979c
    role: context
  - path: pages/traits/genomics/fs_hsdr_like_system.html
    sha256: ad875746c5b5c4be09ecd578531cbb9596e5b536840015fbcfe3c24796f78d3f
    role: context
  - path: pages/traits/genomics/fs_sma_system.html
    sha256: 222c597a1d2a0cc8bd4ad48298920c4985bba45cb7b93493d270f9c53d340fbf
    role: context
  - path: pages/traits/genomics/gabija_system.html
    sha256: 588f4253d6a044d5ab15d8411d3c145426b90bd7aeb83743903467a3a50105bd
    role: context
  - path: pages/traits/genomics/gao_ape_system.html
    sha256: cff7340fbe35615ad792dca1ae6e65686390d5e5cd6683c9a36ca88840a0807b
    role: context
  - path: pages/traits/genomics/gao_her_duf_system.html
    sha256: 026d98eb8cef106a0556ed6eaae75f705cbe5829f27f9091462744c17e071eaf
    role: context
  - path: pages/traits/genomics/gao_her_sir_system.html
    sha256: c50e711130ead02ee0acd51bcdc03445a3ab405a45f9430a27e27710d1fd602f
    role: context
  - path: pages/traits/genomics/gao_her_system.html
    sha256: 339141e64501d8710f27bfd8ee0b35e5106139132f46c7def6026df61818d17d
    role: context
  - path: pages/traits/genomics/gao_hhe_system.html
    sha256: 1265e8a1ba56a2e39649ed3f3b2788b432ed7bf66343f1dab94ad015e13b920a
    role: context
  - path: pages/traits/genomics/gao_iet_system.html
    sha256: 0f236e07f684f160a68cd9a3c0cee97f619af96201e55f292f9c0d434ed12a24
    role: context
  - path: pages/traits/genomics/gao_mza_system.html
    sha256: 9d4858857ad452c439cae89ac71481888976b8fc6788a6f2ef8f8f5717d8705a
    role: context
  - path: pages/traits/genomics/gao_ppl_system.html
    sha256: d641c00590c266470ba02bd5f7ffb1cced3a1cf0ff89f9ca05be5796d3a416cc
    role: context
  - path: pages/traits/genomics/gao_qat_system.html
    sha256: 9223f90f8a4e5287d2dbe21de1d962434b107e50a84cbc3c7bef6650a2d8116f
    role: context
  - path: pages/traits/genomics/gao_rl_system.html
    sha256: d98eb7b2e7a7b2609bf630d45125785b850e2de30642251fd0daef7b7f5b2f3b
    role: context
  - path: pages/traits/genomics/gao_tery_system.html
    sha256: 4c747b34263792c369bc4c8c10eb9fd607c84023c792eb78475f77312e46e105
    role: context
  - path: pages/traits/genomics/gao_tmn_system.html
    sha256: 9a41b22d442c90a7e40117b0a3884372b9ad52efb221bd5df70a633dfe19f990
    role: context
  - path: pages/traits/genomics/gao_upx_system.html
    sha256: 7893be520bb0d328ae3169672eedccdd3fa6ba4ad51823d7960374de84b7ca24
    role: context
  - path: pages/traits/genomics/gaps1_system.html
    sha256: 852017246d8ad68012c5275623d89ce740fb3e83a956b778a787caa673e7f519
    role: context
  - path: pages/traits/genomics/gaps2_system.html
    sha256: 312d0441c01e1ec9c5be200da24c4df4cf9fc896628f12b39bbfc7ad91ee25f9
    role: context
  - path: pages/traits/genomics/gaps4_system.html
    sha256: 07551364ab6b6f2e9f9ce7ea686861d416d0d22de8f4c565f5f04ea245ae9e84
    role: context
  - path: pages/traits/genomics/gaps6_system.html
    sha256: f1f8b017c4e5b5ee94da0c0d3aeeff4f4a1f5258b3ba6dfb21281a1489b809b7
    role: context
  - path: pages/traits/genomics/gasdermin_system.html
    sha256: 48b72c724189a7846b7aa3b670b1495479944bae44603bfc0c6cb9bedf85cf10
    role: context
  - path: pages/traits/genomics/gc_content.html
    sha256: e688959502070bbd0caac661491667a01d6d11a1ed220538614bc81122846be6
    role: context
  - path: pages/traits/genomics/gc_high.html
    sha256: 0c2207f473d503e0dc660e56dd0ce2938187ff171028cec73e6e8be3648d87a2
    role: context
  - path: pages/traits/genomics/gc_low.html
    sha256: 2a37a47536b4add511170c4d157e5924aa607f818c1f713458ff1456f4531c1c
    role: context
  - path: pages/traits/genomics/gc_mid1.html
    sha256: fb0df3131be43ce6b4f1e8e5dd8053f47edf5b0dbf601e04c5afd99712311442
    role: context
  - path: pages/traits/genomics/gc_mid2.html
    sha256: 509ccfaf43358f54b0680dcb083d6cd134715e5fc53de95d8b64884361943b6a
    role: context
  - path: pages/traits/genomics/gc_skew.html
    sha256: d2903c115316c92d93b47e47315a1f9838663438c1b54928e9ad81dc359be71f
    role: context
  - path: pages/traits/genomics/geb_system.html
    sha256: 13c72735cbe3e44fe742be1b8c351b84c1aacc8b863d476e451960171af7fc43
    role: context
  - path: pages/traits/genomics/genome_size.html
    sha256: bdb2cc25ca42d1e2928831930a4525fdfe11af6524b5d65ab8ec0dd64138556f
    role: context
  - path: pages/traits/genomics/genome_streamlining.html
    sha256: 2cfc76db5d443397d3f3653bf6a97e01e59cee650cfe2c99d142091b86e11848
    role: context
  - path: pages/traits/genomics/genomic_island.html
    sha256: 9e136aec18e53e21c8d73b819c4dad5a764e55f154160bfc9b66e0875b24359a
    role: context
  - path: pages/traits/genomics/gmrsd_system.html
    sha256: cf91813e019b364378cdad3ae30bc9cd15b6d11b34c9d33f94b2c1e15c1bc69d
    role: context
  - path: pages/traits/genomics/hachiman_system.html
    sha256: f2390db9078175c441417f677766405e85c063ba2a894ec8ead9d46e793f129e
    role: context
  - path: pages/traits/genomics/hachiman_type_i_system.html
    sha256: 39637c0bd4b7feb1d88a98431b71009851967acce5157e0699d833345e461849
    role: context
  - path: pages/traits/genomics/hachiman_type_ii_system.html
    sha256: 721896dcb4da654038e85cd323d0563e527048b47d212dc8b1d9504f5745f4ad
    role: context
  - path: pages/traits/genomics/hailong_system.html
    sha256: 8f57be5df30a6d4760153422f5840ddbe9455269a3bb032b7f421a9054bacefd
    role: context
  - path: pages/traits/genomics/hec_02_system.html
    sha256: 1552a53145cadce4d39796c8b5d50cee7866d9f4a3222e76f21870d6bc4d7dfc
    role: context
  - path: pages/traits/genomics/hec_03_system.html
    sha256: 701c79f2613f41ee063b8d368f9255a66c0990b71548b9512377d7e4aaf0dcaf
    role: context
  - path: pages/traits/genomics/hec_04_system.html
    sha256: 0908cb902d0e097aa38af688d2e16e0c75209f78f89a3dd130155585321c1db3
    role: context
  - path: pages/traits/genomics/hec_05_system.html
    sha256: a90c234a76b56ed5ade8804d500d73934368d02a5340cbe9ef940514b5e059a0
    role: context
  - path: pages/traits/genomics/hec_06_system.html
    sha256: 38ea7989590b3d2658fe43a71cc78d98d9b227e9fb41eefc4751f98662bc4ca5
    role: context
  - path: pages/traits/genomics/hec_07_system.html
    sha256: 1b3b3a45df4d23c3ba770bdd589db9167ce968b3726ec95b7b92ab52ab15e4cb
    role: context
  - path: pages/traits/genomics/hec_08_system.html
    sha256: c61d292edbf58a971323a141e39e77b9fe667a299f0735881718826e564a3365
    role: context
  - path: pages/traits/genomics/hesat_system.html
    sha256: 189934029a64269f4af7b97b5f3991707dc7f99096b0d26dda534a50d9ff9886
    role: context
  - path: pages/traits/genomics/heterokaryosis.html
    sha256: b48762abb88e054b588ad3f1b5044e20390781b713588d52c61ff6dd2b1caff4
    role: context
  - path: pages/traits/genomics/hma_system.html
    sha256: dbba75f92f4d649b0f115c57fef2c48b2bccb26e20197675bcba341c492c6e41
    role: context
  - path: pages/traits/genomics/hna_system.html
    sha256: 04bf1a90e466dc217383f914bfe03cc69793e7fbe2228c4a2599f4ef798be5c8
    role: context
  - path: pages/traits/genomics/hypnos_system.html
    sha256: ce50cc79c1b8ae2265b107893e74dbf451241eadfa8f8a50c7c53e975e429781
    role: context
  - path: pages/traits/genomics/ig_like_schlafen_system.html
    sha256: c70a5c1733842359f056006cea7a546a6aa412c65fb8fdcc879e4d66ec42a9f1
    role: context
  - path: pages/traits/genomics/integrative_conjugative_element.html
    sha256: edc17aaa2fcaec7524b94c92cf7dab20a31261de5b03270bbe2823ff0dbcd7b6
    role: context
  - path: pages/traits/genomics/jukab_system.html
    sha256: 2705e0f7378fb494248fdc96168d84f1832d29e20df77fc9c7072fd2a25bc96a
    role: context
  - path: pages/traits/genomics/kamadhenu_system.html
    sha256: d67e673948efb8d6b90f6f18bcf1dd9800c1e973298f288bc8d0589fc2e68ef2
    role: context
  - path: pages/traits/genomics/kiwa_system.html
    sha256: 281f54fd7259d66d2ca4e3619d6a042b0214cfb52ab145b06586264d40d9c9a7
    role: context
  - path: pages/traits/genomics/kongming_system.html
    sha256: bf22f370af63fdbd5aec847fd6016b9e4aa36b4ab3629cc467779bc9fb0ea043
    role: context
  - path: pages/traits/genomics/lamassu_amidase_system.html
    sha256: de71d6af004f09e556649330ad56985ed85c403e802ed8c89e2668a9f771155a
    role: context
  - path: pages/traits/genomics/lamassu_cap4_nuclease_system.html
    sha256: 90d25326da801d694743f2b430549e40e6342fb4db0923b7bfe2c23715a03eca
    role: context
  - path: pages/traits/genomics/lamassu_fmo_system.html
    sha256: f4697236b277d57513b898679ace1fc7f6b79c940d15274fe0c9841f896817b4
    role: context
  - path: pages/traits/genomics/lamassu_hnh_system.html
    sha256: dcaa39431e2936d308f78781b07cb072cc03d31e404463b36efda1f8ef9d3608
    role: context
  - path: pages/traits/genomics/lamassu_hydrolase_protease_system.html
    sha256: 0b4ed0492e0dd17b780c5b1ac8f3d0765df5d066fe3fa4febbf4c8ac75d590da
    role: context
  - path: pages/traits/genomics/lamassu_hydrolase_system.html
    sha256: d06616fa22dcf7a3df4f3bd10c849b1063db49b85eb67e12a55ef2b4faac368e
    role: context
  - path: pages/traits/genomics/lamassu_lipase_system.html
    sha256: 488c14cab1f2a296601bba1466bf5989b74743e7c8d206066111996c950a1660
    role: context
  - path: pages/traits/genomics/lamassu_mrr_system.html
    sha256: dae178df3111df27dc90d9b8398d3498d2a8e2ffba1dfc39e1cf381b144e2d25
    role: context
  - path: pages/traits/genomics/lamassu_pddexk_system.html
    sha256: cbe9976d05e770528c1fd50312e6edbb3a26e781c1c71497bb6aea966b0af3f4
    role: context
  - path: pages/traits/genomics/lamassu_protease_system.html
    sha256: ec8115b43419c29808048b09cdef04653380070caf4e32293bcb9e93caf00404
    role: context
  - path: pages/traits/genomics/lamassu_sir2_system.html
    sha256: df4c0442841ffb12adfe719344f90bcd7f667cadc3e05aca858e43c241c6bf43
    role: context
  - path: pages/traits/genomics/lamassu_smek_system.html
    sha256: 6c90b049aecdf12e8da9e7597ba67bdb4ece3e4df641e11649fef800f25e0859
    role: context
  - path: pages/traits/genomics/lamassu_system.html
    sha256: 801a87cf8914c1eb38dd2d5ba007d358f43845a0525822ca408be911eda346fe
    role: context
  - path: pages/traits/genomics/lamassu_type_i_system.html
    sha256: f20c4d7b0c8589f06690c95d9adb73eadf7f668c8714cc520f444f8df4a21162
    role: context
  - path: pages/traits/genomics/lamassu_type_ii_system.html
    sha256: a2a664179dc68e096e413232ec22b7f2886452e0256346d19e9627e328786f7c
    role: context
  - path: pages/traits/genomics/lanthivirin_system.html
    sha256: 4768a031d146cb3735c0c93548c7cbaf904c0c55804215d05799aef4246301a6
    role: context
  - path: pages/traits/genomics/lit_system.html
    sha256: 18f979497c17af4a6b697b923540d033b75327482fd6278ea49f6162ea9d175a
    role: context
  - path: pages/traits/genomics/long_lamassu_system.html
    sha256: 21c681a3a29e2c9f1d8eb89d41568cc7e4b65beb3e0b9fa4aed513945b0575da
    role: context
  - path: pages/traits/genomics/lugos_system.html
    sha256: 9db71d3b5daf817d5b939ea67a78ee4e38fdb02ab9d562e7d0725a0d98e55008
    role: context
  - path: pages/traits/genomics/mads_system.html
    sha256: 839bdfb0465917b64fc259ddcdab5aca139c45fe51a2757ef4aa3332abe90508
    role: context
  - path: pages/traits/genomics/mazef_system.html
    sha256: 7a9a885985b86c420ab54589605e89b46c1c2e379763a6667e01af529842b155
    role: context
  - path: pages/traits/genomics/mcrbc_system.html
    sha256: 1e9d8e9c4ecf21ab5fde2700791d8ce1c158a9485b0bc1fe5cd9c6b07ce92f8d
    role: context
  - path: pages/traits/genomics/menshen_system.html
    sha256: fa30d02169b04fee4fc2c68f4bca018598152ee19a827bea0d8e574f787f8fcf
    role: context
  - path: pages/traits/genomics/metis_system.html
    sha256: 78a15ca6ce2733497ca79f32750c57870f33de9d4ddc916bf7ab589dd53ababf
    role: context
  - path: pages/traits/genomics/mksbefg_system.html
    sha256: bb3b1f95a061b05a45b270e349a1cc9aaf5fbfad3e2fb3d4a15b448efae114e9
    role: context
  - path: pages/traits/genomics/mmb_gp29_gp30_system.html
    sha256: 4e58f4de1cb49cd55d207cdf4f69483bd4a86d5093f6e0214f624481298203b5
    role: context
  - path: pages/traits/genomics/mobile_genetic_element.html
    sha256: 7f69f847751bb2c180d657b56371982f2957feecc98c502730e8f065111711ae
    role: context
  - path: pages/traits/genomics/mok_hok_sok_system.html
    sha256: 3a0fc5a74ec2404d014136157589aedc107abea90fc0a8646d7eee2a9033353b
    role: context
  - path: pages/traits/genomics/mokosh_system.html
    sha256: 3f2db453c248c685df7d2a31fa91119654b78ea3335956c11203c2d3a8658ebe
    role: context
  - path: pages/traits/genomics/mqsrac_system.html
    sha256: 90c756baf5d5d20a750d39c298d53e936454d62c2dcbb2e3dd340c10b13eb303
    role: context
  - path: pages/traits/genomics/mspji_system.html
    sha256: 2a3af51054fba58eb2931e61416f4c2ffc6453879439bcf578c21b5e9c0afbaa
    role: context
  - path: pages/traits/genomics/nantosuelta_system.html
    sha256: 78508fef97c56eac467697032fcb69141a8cf7760a96f4eb7323f3721c6b8050
    role: context
  - path: pages/traits/genomics/nemetona_system.html
    sha256: 5bd7af30ae28f0e71d4f98ce2626ce25ba0d58ef25b38993f06b37e7fa8ee800
    role: context
  - path: pages/traits/genomics/nhi_system.html
    sha256: b71fd55bb1ae4cab537c0dc8b59ae4a893149b228059a355175783c3f97396d7
    role: context
  - path: pages/traits/genomics/nixi_system.html
    sha256: dd574d392575459884badf7615d3989d56a142e1473a51e7cf8e6ff95e19df15
    role: context
  - path: pages/traits/genomics/nlr_like_bnacht_system.html
    sha256: 9ceabcff360c54612d11f0cd669739969a2fdaa5c589e3f2bf4c41416013589f
    role: context
  - path: pages/traits/genomics/ogmios_system.html
    sha256: 9486ef4ee39a85a45d4035f129db0bb912250086625bd69ab5077f772e1753dd
    role: context
  - path: pages/traits/genomics/old_exonuclease_system.html
    sha256: c666da33330338f622e4f04ba8c35b9a0ded8ec9005cbe08d479afb31791c5dd
    role: context
  - path: pages/traits/genomics/olokun_system.html
    sha256: 2a76497cdf4e9dcbd88b5f0cc8e63564970377b3136b9699ddb20a02490a78b1
    role: context
  - path: pages/traits/genomics/ophion_system.html
    sha256: 09f1db2add0ee3382066dd8cea9f9680a1a9afc6e12f1e1701dee694b3f1d7cc
    role: context
  - path: pages/traits/genomics/oshun_system.html
    sha256: a1c23380fa084e8a506ff8f22f730bf52884eb835cb1f53b339a51939eb7155d
    role: context
  - path: pages/traits/genomics/pago_system.html
    sha256: 6d4fa93e8ddbb8d39a07a39b443155db80c437b5846799b09064e1bb78a7d3d6
    role: context
  - path: pages/traits/genomics/panchino_gp28_system.html
    sha256: 7082dadd192b5fd75ddee897c6db6b5c2344101f8aeca660f959185cfa9fa257
    role: context
  - path: pages/traits/genomics/pangenome_openness.html
    sha256: b5a0c568c9f4ebffbff89bbae98dade20850b8628c4c6460a22bb52719dfddcc
    role: context
  - path: pages/traits/genomics/panoptes_system.html
    sha256: 80ee16f209e97143ad1043b83f6be0a2efc8b19700c8c38e2eaeae915bf02c42
    role: context
  - path: pages/traits/genomics/paris_system.html
    sha256: 860711b516c55c6985a131586542ab3166df673e4309f731f567436f34629f16
    role: context
  - path: pages/traits/genomics/pd_lambda_1_system.html
    sha256: 442246b07bbd22486490428ee062ddb87f58ad10b1967fc0c4d6a7c48dfa8488
    role: context
  - path: pages/traits/genomics/pd_lambda_2_system.html
    sha256: fd3a05a33ff127145fa0ad72f1b5a49bd7f352d6e4b8aad5407b0700aeb9b597
    role: context
  - path: pages/traits/genomics/pd_lambda_3_system.html
    sha256: 286724d43518464535caa5f88352dc55752347b08fa7c5eae09427152a63ab02
    role: context
  - path: pages/traits/genomics/pd_lambda_4_system.html
    sha256: c0afaaf81d234975848c74141aabd99a0934ff116287f9aaea0e4eb1e9fd9c3d
    role: context
  - path: pages/traits/genomics/pd_lambda_5_system.html
    sha256: 5ac5fa8f5dbae3d12e5ca030e3aa7f37c899d6a0338495a8dbc43c48f56f5559
    role: context
  - path: pages/traits/genomics/pd_lambda_6_system.html
    sha256: 54b2e66fe5a9c19cc4d35aceddbf04fd27d8b659c3184958a75712a33aa6e646
    role: context
  - path: pages/traits/genomics/pd_t2_1_system.html
    sha256: 493b70b9c0b8ccc12597f77579b9f4ab644cae99d920109583861e0f4a0a6fda
    role: context
  - path: pages/traits/genomics/pd_t4_10_system.html
    sha256: 562457934c18d01b3007d8e985182a9f4f9fc44b6ca4a1d623f588a2a7a08cea
    role: context
  - path: pages/traits/genomics/pd_t4_1_system.html
    sha256: 1f87319519e1b9306ed4df084047dfaa94a252558c28fd97defe93bcc12d9467
    role: context
  - path: pages/traits/genomics/pd_t4_2_system.html
    sha256: 8fdfaa0ad7fc364f10a9801301a533bae1f3a1374f4ab6b1cd17ab3688dba5f1
    role: context
  - path: pages/traits/genomics/pd_t4_3_system.html
    sha256: f08a2653a049f5a374b5529a3b94336f13228d798b7f112a05bb4db7b9d42bc7
    role: context
  - path: pages/traits/genomics/pd_t4_4_system.html
    sha256: 3a6c7ce867c4a0f79326f80e8c0dc2a61b2ba1028cb2588ddce932b16d4081e2
    role: context
  - path: pages/traits/genomics/pd_t4_5_system.html
    sha256: e06d297f445e8002fa94ad3761d8ccd8f24bd4df44e6b6f9f68381262108119a
    role: context
  - path: pages/traits/genomics/pd_t4_6_system.html
    sha256: f4c71a285a9ab12d7f8386984891026f147be2a97879217bc5b75f3ec9688324
    role: context
  - path: pages/traits/genomics/pd_t4_7_system.html
    sha256: 811caeaad7a1a48d03ab1159104688857d7011ce2e082842b8ad3649da6d90bf
    role: context
  - path: pages/traits/genomics/pd_t4_8_system.html
    sha256: b74aa7555aa17a8d8aafa2dd6077fa9b623f327f97119b8a5d8c30626dcf662e
    role: context
  - path: pages/traits/genomics/pd_t7_1_system.html
    sha256: 85928da18cc99f1231a6e16df2743188415bd0c62326ca6efbe1db9b8261e6d9
    role: context
  - path: pages/traits/genomics/pd_t7_2_system.html
    sha256: 3c36e6abc67a17ecc3b0f20d63b8f6038c983670289c2dbbf92329b54eede341
    role: context
  - path: pages/traits/genomics/pd_t7_3_system.html
    sha256: 1fb2e250f97e1d155b58d3fcdc8cd279b57da0b1fa06bb301a65765090561b14
    role: context
  - path: pages/traits/genomics/pd_t7_4_system.html
    sha256: bf0995e0fda1a928f9f92bf9bff39f389a940cf58c7c7a2b25b30fe9343d21ad
    role: context
  - path: pages/traits/genomics/pd_t7_5_system.html
    sha256: 66c88b170fa8a72e207218e986ee793a1bee4220117e5fb507a2f9c1f1d704a5
    role: context
  - path: pages/traits/genomics/pfiat_system.html
    sha256: 28259541f7b498ab47a336c64966e2eb8d1108df269aa713562124e6b98423a3
    role: context
  - path: pages/traits/genomics/phage_defense_system.html
    sha256: 8775d72096e5c5432293daae43514794027d2bc2e7b4f46f44956c7714c6b2c3
    role: context
  - path: pages/traits/genomics/phosphorothioate_defense_system.html
    sha256: 61c1ca5d682c7f50318d3013ea3fa53b8b9701d07af65126e0ec394c6229fad5
    role: context
  - path: pages/traits/genomics/phrann_gp29_gp30_system.html
    sha256: c730aa8bde64584fb714c50aa81bb082bb5583144f55af17f20cb4e013890d9e
    role: context
  - path: pages/traits/genomics/pif_system.html
    sha256: a064a31dccf4116dbf65464021308c3bb659135adf7e6b00e3a4f6fae08aa1fa
    role: context
  - path: pages/traits/genomics/plasmid_carriage.html
    sha256: a1452654a62562220c2e7ddb0efc34dcf692afc91ec89c6e7c4fc6509e1a3a64
    role: context
  - path: pages/traits/genomics/ploidy.html
    sha256: be3f8a55a53ca54d6f91164a98f5a80240ee81e598aed5abfeccd56e8220291e
    role: context
  - path: pages/traits/genomics/prithvi_system.html
    sha256: b68b325f6c952ef48d99504072bc210f907079517eec940fb0aefef268bb3d13
    role: context
  - path: pages/traits/genomics/prometheus_system.html
    sha256: facbdfe19ddaeab5e68e8f59dfb63667e6642179000993beb02590aa54bedf67
    role: context
  - path: pages/traits/genomics/prophage.html
    sha256: 60f6e1d445550f1686fbb1bd4e9396f0d8c7efd7ba0737ce24af527941eac971
    role: context
  - path: pages/traits/genomics/prrc_system.html
    sha256: b55f484b9a36c8a660b5b1f76845d6e02034dbd3755c51e7ad514bcc55c8bbc9
    role: context
  - path: pages/traits/genomics/psyrta_system.html
    sha256: 9b11bc5670bc6dd7535edd329a5c895c8de0bedea27cb62bb5f67bba0138e25e
    role: context
  - path: pages/traits/genomics/pvurts1i_system.html
    sha256: 2658c5f782a2b1bf45bbeb7dd247e8ed9f9ac55b4cf25b99d48f7b916386aefe
    role: context
  - path: pages/traits/genomics/pycsar_system.html
    sha256: 63640689f5228821ef3ef0bac417d50d89dca94435a64983ebab5430f2f1091f
    role: context
  - path: pages/traits/genomics/radar_system.html
    sha256: bb76348f2dd7d47fc579384f42e0637837fe086c7c1bd4af5bf9ac1e88f975f4
    role: context
  - path: pages/traits/genomics/razr_system.html
    sha256: ed36050150dfd19e59f22c9f8946b7ad411622d7b43fa28a6aa9771db406498c
    role: context
  - path: pages/traits/genomics/resolvase_duf5677_system.html
    sha256: 74c15942d655cb78f95f46d8fd0f461f1c470a461f6b573ef025e2a800a3c29c
    role: context
  - path: pages/traits/genomics/resolvase_kap_ntpase_system.html
    sha256: feed38019e5bed33adbdc3289cd5dbddd79e217e5c7b5afe52f72dad22a22435
    role: context
  - path: pages/traits/genomics/resolvase_schlafen_system.html
    sha256: 0c001b0c68ae4d9cd18d339dab6718c841a49bc88cf635acc4cf07b1b53bbd3a
    role: context
  - path: pages/traits/genomics/restriction_modification_system.html
    sha256: dc2a8045efd32768f38bd17179efbb9c0d41d67746ec21ae994e81e744126816
    role: context
  - path: pages/traits/genomics/retron_system.html
    sha256: 716603214894d426ef391057b06993df2f008097744c8761963dfc9466c1805c
    role: context
  - path: pages/traits/genomics/reve_system.html
    sha256: 3b5c17811e0e13f9c1250d1db800775fb4aabf25060574811327267b2c37f4a7
    role: context
  - path: pages/traits/genomics/rexab_system.html
    sha256: be19777b38812d61595a242b06fc1ade7b1226a2cddddc14f16527ace891dae0
    role: context
  - path: pages/traits/genomics/rhea_system.html
    sha256: 96d84118a9a62c71ffab82efac71d7395ac6066447d22b2e3997e2583e2bcaee
    role: context
  - path: pages/traits/genomics/rloc_system.html
    sha256: 0941000d0d5a3b30faf5da859e41d79cb8c703fc25398e3a6be16ba075ff606d
    role: context
  - path: pages/traits/genomics/rnlab_system.html
    sha256: f49775079c519d274af3f77c56af0064879f046ed1006cada0b790627e7211ef
    role: context
  - path: pages/traits/genomics/rosmerta_system.html
    sha256: 5c5f5bcfeff14d59804b4d0e4240db5be97d672436c63f2680eef4b68eb6b3f4
    role: context
  - path: pages/traits/genomics/rrna_operon_copy_number.html
    sha256: 993b7df00e21923208835fd981e14706e065747784a78d7bc636b4c9389f44b1
    role: context
  - path: pages/traits/genomics/rst_2tm_1tm_tir_system.html
    sha256: 76e3293776849f51f85fe15ad9623752cf0e26f29f6762105a26c252a9721323
    role: context
  - path: pages/traits/genomics/rst_3hp_system.html
    sha256: 5c3290f371c5375dfbf7698bf08cc8ff0bb8298a84d66f3465e2b6f9050c751a
    role: context
  - path: pages/traits/genomics/rst_duf4238_system.html
    sha256: 64f8fafc2c97b92559eb542e7f28429418023ae4e9ebf45798a218bc71ce97ae
    role: context
  - path: pages/traits/genomics/rst_gop_beta_cll_system.html
    sha256: 2d645ef43b5eabdcdc1d2da919ad7f05a475e50b23e1909769780147569ce1f5
    role: context
  - path: pages/traits/genomics/rst_helicaseduf2290_system.html
    sha256: 12eac8aa968051bb57c8068c6f8be7ac732b6307cbbabccc966831282269f745
    role: context
  - path: pages/traits/genomics/rst_hydrolase_3tm_system.html
    sha256: 1fa753b12a539fe061491862703366c831b018c12eef2ea9b2cb475641a99a26
    role: context
  - path: pages/traits/genomics/rst_rt_nitrilase_tm_system.html
    sha256: e64dc8a3cf4edc8bb7969b6f9367bcc0362fa35cad086b5e1ed1e023c9ae6358
    role: context
  - path: pages/traits/genomics/rst_tir_nlr_system.html
    sha256: 9385309d6a12955e53cce7f3d11aa9b1e092e669cd1774e66f475d835f770f1e
    role: context
  - path: pages/traits/genomics/rugutis_system.html
    sha256: 603facc6db8060b3d1fa6a8a98e2489d63e048e442582c2a71ee502e17372661
    role: context
  - path: pages/traits/genomics/sanata_system.html
    sha256: af8a640e32c7236f3be5079ad1c9b71e42dd7bb3b8f4b56d53152419d0c3daba
    role: context
  - path: pages/traits/genomics/scomcra_system.html
    sha256: e6997101a7eed9f340ef34ebd29221946dcfdd66017b0645566a7825fb59d3b6
    role: context
  - path: pages/traits/genomics/sdic1_system.html
    sha256: a7ce0585a61560c7e400afc312c643258100dad5ebe58db82d8c6392c6e5036c
    role: context
  - path: pages/traits/genomics/sdic3_system.html
    sha256: c3b62999ff971f6e89bfacb02fd9d0faa8a63d5462a1f91a6cf1a4e590a22660
    role: context
  - path: pages/traits/genomics/sdic4_system.html
    sha256: 0fd6556cfba01b073e57a46e996a60fbc4ca362b1340568a2298a09e85d8d51d
    role: context
  - path: pages/traits/genomics/sefir_system.html
    sha256: 2fa696be058e4d63592cdeaf60b0601e0a214efb840dbbd176d96cfd740b07d1
    role: context
  - path: pages/traits/genomics/septu_system.html
    sha256: 666af20fd71b7c28ce5e0261249891f4a6f7b849e7b2d02fc7787b362866662d
    role: context
  - path: pages/traits/genomics/shango_system.html
    sha256: 1ce9310a58d94db5dba1a8b1b8e369bc6f63413554e9ef392a0c0c5133523ca2
    role: context
  - path: pages/traits/genomics/shedu_system.html
    sha256: efdc76e4de8469bccd449e082677d98b78b27c1c759a5605757ed2f9d24aa8f6
    role: context
  - path: pages/traits/genomics/short_lamassu_system.html
    sha256: e1cbbd68fbf78adc7dc36ad4ae0ebd55ccee218050e63461d7993d42810d7aad
    role: context
  - path: pages/traits/genomics/shosta_system.html
    sha256: 154eebadad9994bb8a7aaec4a0728be8463eefa7b477f87a334c98c8129db345
    role: context
  - path: pages/traits/genomics/sirona_system.html
    sha256: 2f4b1b3f2e365b8fe5e30a3c3fc9408b6817e178096df99ed62b2159d8c54fb8
    role: context
  - path: pages/traits/genomics/six_a_mbl_system.html
    sha256: 0bf32a0938a8f6efdc9c0d7448f41674407f80cb8598f3c1c35d08b19455ca9e
    role: context
  - path: pages/traits/genomics/snipe_system.html
    sha256: b03d5b4917bfd651a694579789818442b35dec722968d4d2153b6f22546b87e4
    role: context
  - path: pages/traits/genomics/sofic_system.html
    sha256: 75e8716451726ba747e85768415d784f36525f331084353e964e253d14d05087
    role: context
  - path: pages/traits/genomics/sparta_system.html
    sha256: d7bd08c0fba08791086cc3b4ba2bc688aa04d63d5b129ebeb0272d54d56b58c8
    role: context
  - path: pages/traits/genomics/spbk_system.html
    sha256: aa1bf4bf1a07f9f5a36e130056d30d1f5d396bc905cd724c4fc4d35deb6d551c
    role: context
  - path: pages/traits/genomics/sspabcd_sspe_system.html
    sha256: 70018f79efb775fcf7d5c919f2c661bd7ff1377264229f8a3beab41ee214b992
    role: context
  - path: pages/traits/genomics/sspabcd_sspfgh_system.html
    sha256: 47be0cc353f3eac45004319681dcccc471abd385fbc9ba9a09e18b0306f3248e
    role: context
  - path: pages/traits/genomics/stk2_system.html
    sha256: 42079023af62a0aba2512de9cb20c3550858af434a9d22b9afc93393a527663a
    role: context
  - path: pages/traits/genomics/sucellos_system.html
    sha256: dc5c3968bba0442414194047de2fcf4e94d037c5ca964dc9131ecd4e3f6a9a93
    role: context
  - path: pages/traits/genomics/tab_system.html
    sha256: b53955620ada40f90fd9b3f5447426cf7ee596c84b30f515e204b1725d459aa0
    role: context
  - path: pages/traits/genomics/tagi_system.html
    sha256: 9e973100d95e39a959d8eb3f60143d0af455961c913d75f19a150b3436db4500
    role: context
  - path: pages/traits/genomics/taranis_system.html
    sha256: 8e0faa20e773fc82b0df67dc24cab4cf7590e424f747564535e6248dc7e88e3d
    role: context
  - path: pages/traits/genomics/tgvab_system.html
    sha256: 0ab15cd03a85f66248a7c0282409c2bee4e5abe6401cb8e92e72bd5b16791834
    role: context
  - path: pages/traits/genomics/tha_system.html
    sha256: 657b3a5320766844cf6870156661fa8182e0794b637e982ed1476e296ec25eb8
    role: context
  - path: pages/traits/genomics/thoeris_system.html
    sha256: 7ddd8eedfd9fc7adb3c5f159e4719011102098618920c228464835c8f95cd165
    role: context
  - path: pages/traits/genomics/tiamat_system.html
    sha256: 42bcf96b83500fff14ed450f21430542ad89ea30b5a4e672b1d7123097b02bc2
    role: context
  - path: pages/traits/genomics/tir_i_system.html
    sha256: 93a43ada09d079d42c80b7a856fea061cd0a02fa0fd11ee147e6885973d04434
    role: context
  - path: pages/traits/genomics/tir_iii_system.html
    sha256: 29e65c9e9f5a739fb887e5372561474e769b16bda5bc9ecb6e5c17566d96ab0c
    role: context
  - path: pages/traits/genomics/tir_iv_system.html
    sha256: 6e2b6cc959af26f98af7d8383a51022639210bfcee2d2375a17884284179da1e
    role: context
  - path: pages/traits/genomics/tir_vii_system.html
    sha256: 06e30f558091617e78298d7f0afb9495dc9266981249001fae68866920c8b1af
    role: context
  - path: pages/traits/genomics/tir_viii_system.html
    sha256: 938f8344355d347f30aeb2a99051ad5a37874fc99ba4198ce71cd120753763c0
    role: context
  - path: pages/traits/genomics/toga_system.html
    sha256: dd61733188e30a1ba3507740527dfdc4173e14daac382ca6d9363d607d2cbd92
    role: context
  - path: pages/traits/genomics/toutatis_system.html
    sha256: daae3c80b9c17071f46e9aae9a1132a9dd2a0c2689111f72c4b40c5e786f56f7
    role: context
  - path: pages/traits/genomics/toxin_system.html
    sha256: ec66ef63ab91c8b6346e77f092287e1d77d66b17426695420b5487ed0c542564
    role: context
  - path: pages/traits/genomics/transposable_element.html
    sha256: a5a25bed979aee4104350f96248807b094f12ec8213b87cb9ed2bebaef230aec
    role: context
  - path: pages/traits/genomics/type_i_restriction_modification_system.html
    sha256: de385bca1a89d4c03c9f02fe44fdbdb838c4ff5f5f46d5f09cba6bbaa58b9761
    role: context
  - path: pages/traits/genomics/type_ii_restriction_modification_system.html
    sha256: 3892c33d9c774352d0c1ef84adf0f4f4645af19f9af1f5a59568e18e1b7917c6
    role: context
  - path: pages/traits/genomics/type_iig_restriction_modification_system.html
    sha256: aced216844dba0397577037d051ef2173a65aff98f759b30e5acea49f926e99a
    role: context
  - path: pages/traits/genomics/type_iii_restriction_modification_system.html
    sha256: bf41174986ce5cb89eb04e5ca45293190db87b5efd924dfd8516782bb53a9759
    role: context
  - path: pages/traits/genomics/type_iv_modification_dependent_restriction_system.html
    sha256: 7e92dc2216d83b49cc10567b2461385f381effc3c0b51de95edbb167e9988d97
    role: context
  - path: pages/traits/genomics/ukko_system.html
    sha256: 94146f0dd517f6b8ab1c7426d9f2dd32bc77343d7ae9382d82d25008c35928dc
    role: context
  - path: pages/traits/genomics/uzume_system.html
    sha256: 62de5c1cbb0f9a7f16afe2ad88e87cc651ffa6f16a37c6f4e388b2ffb244cfa6
    role: context
  - path: pages/traits/genomics/vcam4i_system.html
    sha256: 9cd002b8b9e44c0a2988a2588a6b60dcc05e9819ef68b3551b9bf0d2c6e5d80f
    role: context
  - path: pages/traits/genomics/veles_system.html
    sha256: 39eedf374c719772e26fbf949e8a00484aedfd7aeb3d37cf704816460877b55f
    role: context
  - path: pages/traits/genomics/viperin_system.html
    sha256: 88adb027bf097f8b296ab0bffbfd569620edd33eff01942a7ff4756f289059d4
    role: context
  - path: pages/traits/genomics/vp1796_system.html
    sha256: 28d38cac332268b3345f9e2a01d041510f754a2c1e21a17d02a62e71d0bdf9b2
    role: context
  - path: pages/traits/genomics/vp1817_system.html
    sha256: 92dd4d2c69dc8ba67b6572862d7fb04323a77cab66bb40d08170f23f58d05490
    role: context
  - path: pages/traits/genomics/vp1823_system.html
    sha256: 516361f176214356df72d19a802113dba0c8a3f322415a924b40a65ea2766ac5
    role: context
  - path: pages/traits/genomics/vp1826_system.html
    sha256: ff30610d4243ec51e6a084a20d49bb3fb0a18321123eb4a062bc328702942bc1
    role: context
  - path: pages/traits/genomics/vp1839_system.html
    sha256: a2ab6c08bddc2616ad88297c505f5ebe9daf7a912ec46da6af56f02852f02f1e
    role: context
  - path: pages/traits/genomics/vp1840_system.html
    sha256: 2044d3cbe1d543f43de348f20d9ff3012bbf857cd964c53eb9cce3d9ad0ab614
    role: context
  - path: pages/traits/genomics/vp1848_system.html
    sha256: 5c301a5197f73e70a0d58ea2546f68839a54bf2d311778601ff78e7a4c90e8d8
    role: context
  - path: pages/traits/genomics/vp1851_system.html
    sha256: ff35f3b56608541c85507ce29e1f26d5ff9e0596baa3c060c167b411cc467aec
    role: context
  - path: pages/traits/genomics/vp1853_system.html
    sha256: c6b84e6078355a03ffb0ae7d8b16e0831b7b8e61422cea64dece97e825002a6d
    role: context
  - path: pages/traits/genomics/wadjet_system.html
    sha256: 3cf93706ca2a011950b0f162ffe326c7aca9febd3494780ec0228a2ec9d2e855
    role: context
  - path: pages/traits/genomics/zorya_system.html
    sha256: f81687daaac1b61d516df88e60038b5921d1f57cc2b9f85074ffe5c6d0755289
    role: context
  - path: pages/traits/genomics/zorya_type_i_system.html
    sha256: b6ccc650eb74eda95cfdb47c28d80a1134bd95b86d24ff96430f477afd7c0586
    role: context
  - path: pages/traits/genomics/zorya_type_ii_system.html
    sha256: 1e07912d97d749b6ed3789d68eec08d6db5a5c2c0b00383abeef9b53554fab85
    role: context
  - path: pages/traits/genomics/zorya_type_iii_system.html
    sha256: 906be1b56c78b59c6aca1e03e30f6887492e97a1ea863cb7e6117475b2f69843
    role: context
  - path: pages/traits/metabolism/accumulates.html
    sha256: 7530122a93c9b431869f356cc6f04a5c45f9e65b0b83ff7cd24c8a95c2a6af99
    role: context
  - path: pages/traits/metabolism/acetoclastic_methanogenesis.html
    sha256: 7890f0b8e206ff70a45df612f3d52c0fd8de47f99aaa7c283d80952b15ac8f59
    role: context
  - path: pages/traits/metabolism/acetogenesis.html
    sha256: 32a4f2321757ce451a5488fedb50f77807f833ae82e0a33f96fbcc75c035646e
    role: context
  - path: pages/traits/metabolism/acetone_butanol_ethanol_fermentation.html
    sha256: 28292db2ded28a935e4da70ac466ccc0f8a67f55401a14a55a1dc040972a8353
    role: context
  - path: pages/traits/metabolism/aerobic_respiration.html
    sha256: 67560086790439f9bb506e78940498266765a328a938ce4eee295a048a1433d5
    role: context
  - path: pages/traits/metabolism/anaerobic_ammonium_oxidation.html
    sha256: e5b1b03f9ced51bfc2c21a72157217226c6222c0fcf225ef06901a0ae7880108
    role: context
  - path: pages/traits/metabolism/anaerobic_oxidation_of_methane.html
    sha256: fd0bfc027ed1d7196f1514281ce7aafca2701b95dfc7802302bf6465024e5779
    role: context
  - path: pages/traits/metabolism/anaerobic_respiration.html
    sha256: 116da268a6ad228d10b7da26e62d76cafa45bd137879b86c2dd46ae5c5e84a5a
    role: context
  - path: pages/traits/metabolism/anoxygenic_photosynthesis.html
    sha256: 71de6f956ecb3a7dbbf1206c0805f17ee9fa7e97541713b9f07b8127062d86a6
    role: context
  - path: pages/traits/metabolism/aromatic_compound_degradation.html
    sha256: 5cd89efd4ad57981b30cb4e4633088892c7a3b5fe9c439229f1977e324350433
    role: context
  - path: pages/traits/metabolism/aromatic_hydrocarbon_degradation.html
    sha256: 9b4fdb51b57987e4798f91f7ab49b2f4d1d32635c6cf1a9f0818cb4aeb55c117
    role: context
  - path: pages/traits/metabolism/arsenate_respiration.html
    sha256: 248426bf30f2ace9837a95ebae4508e82d702bb392267732f13074d948091ef1
    role: context
  - path: pages/traits/metabolism/arsenite_oxidation.html
    sha256: e533fd755be0bec96cf8f84ddc3607ddca02d5e00a67b8e6d04d7dd2d32e623f
    role: context
  - path: pages/traits/metabolism/assimilates.html
    sha256: 2c44f906488ab36bde5aa0bb18bcd90ee405b45c1c55a3b3afdacce1a9d5d85d
    role: context
  - path: pages/traits/metabolism/biopolymer_degradation.html
    sha256: ff16492b22708604c225f86f648367feb3fc295acfc535075f58d0f685fb5a22
    role: context
  - path: pages/traits/metabolism/builds_acid_from.html
    sha256: 1a05a80448aa33618e03cd7555bd36931bf6d41573754f1a5ce4c69fb0c2dba2
    role: context
  - path: pages/traits/metabolism/builds_base_from.html
    sha256: 52a22ba52688912115e6e1407127ef7d54f1396b58a7c81cfcd2a6e9e7584a9a
    role: context
  - path: pages/traits/metabolism/builds_gas_from.html
    sha256: 4541acd50ac101f98ed9fe68e6c06d3e27451db333b269df9e44dee30174ab17
    role: context
  - path: pages/traits/metabolism/butanediol_fermentation.html
    sha256: 45c4cd35c12bbc87e5e52d1dcf6d1a8958c3930a7795a9dc048cafc5125d406c
    role: context
  - path: pages/traits/metabolism/butyric_acid_fermentation.html
    sha256: e98d8ab5855b3be4dd87d1c54e0ba7e44136d0f633104add6d8f8bdc133035a6
    role: context
  - path: pages/traits/metabolism/cable_bacteria_metabolism.html
    sha256: 5ea8632611c089ad6eadcd02dfadfe793378115b6e940a937b62a959f28319c9
    role: context
  - path: pages/traits/metabolism/calvin_benson_bassham_cycle.html
    sha256: a0ca1bb9837ea6163e7cd802f1695023cdd02f838d0274f93c0cae4dcab62bf5
    role: context
  - path: pages/traits/metabolism/capable_of.html
    sha256: 21b0176b35308b7b65616c692dd8d9eaeaf832cdfa6e8340748b828f7e5dfdc1
    role: context
  - path: pages/traits/metabolism/carbon_fixation.html
    sha256: 3baaf15eacfaa8d8710fd515c2131c1396b2f3c2a733c8f4518e7a0310544473
    role: context
  - path: pages/traits/metabolism/cellulolysis.html
    sha256: 377e96c73e8bd77cd147bbfdcb85d0b7be0248e2b75e7e39dd0dc5dc7e7b02c2
    role: context
  - path: pages/traits/metabolism/chitinolysis.html
    sha256: 12fff11228ea424d4f72e2ddfd0133ccd89c0482e0d1bb771c1fc61a058d93bf
    role: context
  - path: pages/traits/metabolism/chlorate_respiration.html
    sha256: 6ecfe0acb6b0e6c97cc7536898b452e9bd619c8e07de6f842f6bd8b48e066533
    role: context
  - path: pages/traits/metabolism/citrate_fermentation.html
    sha256: 05740420f7b61def0c125630553bf9e8c9820212bdf55a05a8fc3391df95a11a
    role: context
  - path: pages/traits/metabolism/compartmentalizes.html
    sha256: a4f961c0934a0779973ed85d3c0912243bd0a8e556e431e36658c94c47f0d1e4
    role: context
  - path: pages/traits/metabolism/complete_ammonia_oxidation.html
    sha256: bb859527301ef2515bdcd363cd10b7200d38e6705b2ee18682c2f2ee2133ea98
    role: context
  - path: pages/traits/metabolism/dark_hydrogen_oxidation.html
    sha256: 4971b950f0c7df3fc70c056b9c97109c32f15b884cac4276501cb3a8da449cd7
    role: context
  - path: pages/traits/metabolism/dark_oxidation_of_sulfur_compounds.html
    sha256: 8e885a331ce60a0809a8bf158e4c42883cf60db05b3ef70ad45163289fcdeddf
    role: context
  - path: pages/traits/metabolism/degrades.html
    sha256: 50c44802cc30c38023f98a8721f92e9db86bfea4174f6cbbcf440d2969811cf4
    role: context
  - path: pages/traits/metabolism/denitrification.html
    sha256: ca1b7d5c464566b56546021c57ccabbba69c2e2553c1101c66d3e37755dc812b
    role: context
  - path: pages/traits/metabolism/dicarboxylate_four_hydroxybutyrate_cycle.html
    sha256: 9f6baa129a624699fdcd3626fbd65746eea44b97055fa0e60db9daf31edca13c
    role: context
  - path: pages/traits/metabolism/dimethyl_sulfoxide_respiration.html
    sha256: 5321e049598b65828f3fafa2c466f9fd4bb02a24306a928d58c6911de5fb1f95
    role: context
  - path: pages/traits/metabolism/disproportionates.html
    sha256: bb8b13e1c846fd24e59673e59366c117bd8b30dc2900eb0e0000a050ad71d25e
    role: context
  - path: pages/traits/metabolism/disproportionation.html
    sha256: e16c4ab53f1f4102eef7048ec87d0ce4799470df5b57d119811088b7f3103e0a
    role: context
  - path: pages/traits/metabolism/dissimilatory_iron_reduction.html
    sha256: b7f5321ba41dc30ac70d73a2ea1b3b020fad93ba2aee216bd3b19764b59cfece
    role: context
  - path: pages/traits/metabolism/dissimilatory_manganese_reduction.html
    sha256: 695818fd4439e53a7048394ac19ef60f6b76217945e42d95a77f603acb2d159c
    role: context
  - path: pages/traits/metabolism/dissimilatory_metal_reduction.html
    sha256: ddcf6086de67cad5e6daf231e7c4911bce0a9e17a4c7b0d755fee542b51efd03
    role: context
  - path: pages/traits/metabolism/dissimilatory_nitrate_reduction_to_ammonium.html
    sha256: 2d0d2445deba951be787ea94314eb6bee4134216cd51418b6d3909eb559c9065
    role: context
  - path: pages/traits/metabolism/dissimilatory_sulfate_reduction.html
    sha256: 21bdd688379ca1cfc7166cd040c8bf8877b6c0692ff70890dbbb653d55c40a26
    role: context
  - path: pages/traits/metabolism/does_not_accumulate.html
    sha256: e6ac964d6ff42a695871af3cf4156381e057610c8e23ad43887af07393dd9831
    role: context
  - path: pages/traits/metabolism/does_not_assimilate.html
    sha256: 5c659ac5490464f824607dedb79b6a8723fb4299ddc8cf6ff16884f0ee30497c
    role: context
  - path: pages/traits/metabolism/does_not_build_acid_from.html
    sha256: 111f783722a9f5e9c5e109d55463ab0e627c3b92ead7e5d9acafbdb57453eb4c
    role: context
  - path: pages/traits/metabolism/does_not_build_base_from.html
    sha256: d167ad8d2ddf09b18717b41b40a2bb00888f69beb491e639f59b4df56aa3d097
    role: context
  - path: pages/traits/metabolism/does_not_build_gas_from.html
    sha256: 9c3e32935574f44a22318461b444575b2585cf69b1d36014332282cb096fe7a9
    role: context
  - path: pages/traits/metabolism/does_not_compartmentalize.html
    sha256: ac214af3ea5edf0c5a8f9f09127e5fb99f6afc85ff3359440d1e516f2df3043a
    role: context
  - path: pages/traits/metabolism/does_not_degrade.html
    sha256: 55cec31379f0c6f26da9348de80a971dff7cdebf86f194e33ae18b3299b75dd3
    role: context
  - path: pages/traits/metabolism/does_not_disproportionate.html
    sha256: cd7884d1f413db6dc598ec47db7ca0bb00fd40004a327b0d112360fa92cf59c0
    role: context
  - path: pages/traits/metabolism/does_not_export.html
    sha256: ed0a16f2220af81c002332e7e68f060d91159e1251f06e93ede7ad8c7737ee24
    role: context
  - path: pages/traits/metabolism/does_not_ferment.html
    sha256: 4e424c4f5f5d18a2a7733bbc9cee9f89529c4a983397876929f8c60f17bb8395
    role: context
  - path: pages/traits/metabolism/does_not_hydrolyze.html
    sha256: f9d36c813652ea33911100a9fed7ac10cafb2054da65474181b959c8e26bfe27
    role: context
  - path: pages/traits/metabolism/does_not_import.html
    sha256: 69fc1bedd79d20f9e1be659719fa0af1d288b938bec7d92ce8acc5c3b1030d6d
    role: context
  - path: pages/traits/metabolism/does_not_oxidize.html
    sha256: a818f3c723e1eef88fc6d76086c046684d1ed5936907dc2c63dada74efa4472b
    role: context
  - path: pages/traits/metabolism/does_not_produce.html
    sha256: 3d43652c680531227dc176d53269f09333a7f8fa5de12318a81da278106ab5b0
    role: context
  - path: pages/traits/metabolism/does_not_reduce.html
    sha256: 52b10b5fbdaf99ffd3f49b44bf9c73728b187ac70171d44260215ead418e5a77
    role: context
  - path: pages/traits/metabolism/does_not_sequester.html
    sha256: 2723b86301ef65a4bfdf26a232c5dc544f31f9e9947afd58688d2103ffbfddab
    role: context
  - path: pages/traits/metabolism/does_not_show_activity_of.html
    sha256: abce157c57d9d34d599c80fc29737a3150a021cae36abb6014408877ba58f245
    role: context
  - path: pages/traits/metabolism/does_not_transport.html
    sha256: e19d8d83c5b804c22e5819313ee4cbedae5d6cc5cdfb427f4b2ff1aa6d3e7896
    role: context
  - path: pages/traits/metabolism/does_not_use_as_carbon_source.html
    sha256: 9683d803df6f89d9e471ac98cf80e4be29129b5c0079a7bb3e89da0b93cd25b7
    role: context
  - path: pages/traits/metabolism/does_not_use_as_electron_acceptor.html
    sha256: 3db4460ce5308473f1697dd6e3bf1cf221cfa2ad3b8ba12083b9d63957b15cc4
    role: context
  - path: pages/traits/metabolism/does_not_use_as_electron_donor.html
    sha256: 14def1d0f2ed9d458b80798673a441f0e616feb630de47967910dfcb2ef33512
    role: context
  - path: pages/traits/metabolism/does_not_use_as_energy_source.html
    sha256: 502fca6682b9cb6a1d03d2efc6eaf4c98373b0e0a2c1f3b4d28b644da44514b4
    role: context
  - path: pages/traits/metabolism/does_not_use_as_nitrogen_source.html
    sha256: 5432e0662bb6ec35bc869cb8422397ae1f4780d936827382c867a911250174c1
    role: context
  - path: pages/traits/metabolism/does_not_use_as_sulfur_source.html
    sha256: c19ce9161013b3f3432673b1ffef2caadd979d677e3d20f8229382424c8ea29b
    role: context
  - path: pages/traits/metabolism/does_not_use_for_aerobic_catabolization.html
    sha256: 556f5a4ae799d833d189b9a570c8b56cf0ffddd40c82226abd829879e843aeaf
    role: context
  - path: pages/traits/metabolism/does_not_use_for_aerobic_growth.html
    sha256: cbc9b4abf45333e0f779520634fdb83593f43d01b9b2ec674007e11120158b26
    role: context
  - path: pages/traits/metabolism/does_not_use_for_anaerobic_catabolization.html
    sha256: 57f8dcb52f4ff8f2225c3d09d481bd1e6dd304935297797a382e5486597a5808
    role: context
  - path: pages/traits/metabolism/does_not_use_for_anaerobic_growth.html
    sha256: d2a0aab938d2e14b301f8dee364f3d708c296a75cae5b3a1b7cdaa2b73011094
    role: context
  - path: pages/traits/metabolism/does_not_use_for_anaerobic_growth_in_the_dark.html
    sha256: 7daa0f011453b6f3c4797adfec22481f7008e029da0290c0b03777863f7bfe83
    role: context
  - path: pages/traits/metabolism/does_not_use_for_anaerobic_growth_with_light.html
    sha256: fbb79c73f3830202e37aff56d55f4b1010f4d6cd62e528498da8bee56d168cb3
    role: context
  - path: pages/traits/metabolism/does_not_use_for_growth.html
    sha256: 9ef5d3e6051b077702eb7c8cd0d1ace36e53fa3c03ba52a7a6ba1a86611023f0
    role: context
  - path: pages/traits/metabolism/does_not_use_for_respiration.html
    sha256: 52c2e46071e2a2da8d63b619a2beef329ef611f9c9f2b70973e4f903642a8456
    role: context
  - path: pages/traits/metabolism/does_not_use_in_other_way.html
    sha256: 2d6a2cdaa66635c4ecf150dec2689d0bb305534653b71bd7a1a40308e34dbb14
    role: context
  - path: pages/traits/metabolism/electron_transfer.html
    sha256: 09abe63ee15c3c60a17c5bee4b714c7508222c9ef0e92a6035a8c085742bb40c
    role: context
  - path: pages/traits/metabolism/enzyme_activity_analyzed.html
    sha256: 33da4e6295f0df6b31d5cb0063969a2f4bdb95fcbc32171eb4ff355de4d3ce16
    role: context
  - path: pages/traits/metabolism/ethanol_fermentation.html
    sha256: 8984c0fab9dcd5dd5deb67eee2bd40d01eb5d32a758193fac7221b97f6366952
    role: context
  - path: pages/traits/metabolism/exports.html
    sha256: 85ba4ebb64eb88740178e6d37e9eb83ca3539ff49a74e0d930e8f60652f7d195
    role: context
  - path: pages/traits/metabolism/fermentation.html
    sha256: 86103971bfab50f2108681ad74f123877bc209705faed811e01d4d540928588a
    role: context
  - path: pages/traits/metabolism/fermentative_hydrogen_production.html
    sha256: 5b18d3956dfe3f6a21e6d688fabf789d2f0dfe3c31757d44c29cd858f018c161
    role: context
  - path: pages/traits/metabolism/ferments.html
    sha256: b9f747a12f2e45e5f5e92b413eec89f6151e0f0bf6f53cb821fec8ad216f2e12
    role: context
  - path: pages/traits/metabolism/fumarate_respiration.html
    sha256: 4f4ee9d6a2903675c7335bbd9eb1b410114bdc051b2592a89973b42686ff6b38
    role: context
  - path: pages/traits/metabolism/has_growth_nacl_observation.html
    sha256: 984d588495a355cd9f65e02d50dcc954976686f4955c5eede9f3530c8348b9f3
    role: context
  - path: pages/traits/metabolism/has_growth_oxygen_observation.html
    sha256: 8a27afeb1f505f342187d18efce7a7b861d8a9f94e6333cfda475e4d0d56e6f1
    role: context
  - path: pages/traits/metabolism/has_growth_ph_observation.html
    sha256: 5e86e7e0fa50d6daacef6b76c07f5e341a6de6a70ec2dc0b004f5c79a222de31
    role: context
  - path: pages/traits/metabolism/has_growth_temperature_observation.html
    sha256: 6bb7dd21f1616780c17264e4e3429dc7802dbfd0abbd00fc9009456078759c58
    role: context
  - path: pages/traits/metabolism/has_nacl_delta_observation.html
    sha256: 191e0f15d28f02adfd6265f7aef3dc538b9ed0830a4f428a752eb75a0b776143
    role: context
  - path: pages/traits/metabolism/has_nacl_observation.html
    sha256: 66642d4636e2c4ee963e2b10c731b12486c5e54d2392d747a1df7881e5f91b87
    role: context
  - path: pages/traits/metabolism/has_observation.html
    sha256: d4ba078b1d61a35b0db69d3e27b61eb185925d22c3f037c662344696b9bc44ec
    role: context
  - path: pages/traits/metabolism/has_optimum_nacl_observation.html
    sha256: 55e09da65a773e0a2c2a9d419efc756929ce1da4e7e8b81408f0b99cd5fac909
    role: context
  - path: pages/traits/metabolism/has_optimum_oxygen_observation.html
    sha256: c4e2421baf54c308fb09570a3bd10cfd9375cbe7374b4641e86577dcb6d95158
    role: context
  - path: pages/traits/metabolism/has_optimum_ph_observation.html
    sha256: d9f489f242473861d236cfd61331b4ceff44479b3744a9b9ed7bd9e73b8218fd
    role: context
  - path: pages/traits/metabolism/has_optimum_temperature_observation.html
    sha256: 1763d0f4ff7009c84c88a3297c9ebdc7e0588646c4083dfcae3b2f9905332095
    role: context
  - path: pages/traits/metabolism/has_oxygen_delta_observation.html
    sha256: 0eca61484a533e420736c8e15e82b90cc402be4ba17a4f5ec5eb28c3ed20da00
    role: context
  - path: pages/traits/metabolism/has_oxygen_observation.html
    sha256: eddd7bbe6298780d1cc2e8724cbba28d94b4c6b6bb8348d1f0bc849baf67c0ca
    role: context
  - path: pages/traits/metabolism/has_ph_delta_observation.html
    sha256: ecd6330c512b2dbff20628af72dc4f9b81398263cbf58ae25a3907ec1822c894
    role: context
  - path: pages/traits/metabolism/has_ph_observation.html
    sha256: 11efd97a762f4e6c3fa9af12df9efd0ae535f01c1a8ed3d48f64b1151495f07d
    role: context
  - path: pages/traits/metabolism/has_phenotype.html
    sha256: b2349dea16a05ca42f94838f4a2a3e98bb178b941246fd9b2cf42df826bca242
    role: context
  - path: pages/traits/metabolism/has_quality.html
    sha256: 61c894a5ed0577b0859adc8cc112ce8a94c37b60315f4d1d69253a74aff1b7c8
    role: context
  - path: pages/traits/metabolism/has_range_nacl_observation.html
    sha256: 6c3780dabb54773acb226560855ad0b48e76241cb5aa160c9e715dfe81f8c12d
    role: context
  - path: pages/traits/metabolism/has_range_oxygen_observation.html
    sha256: 9ff6014fd26863723d7e08ba7e80966fd3273bc75b9709051f06877c86b2d317
    role: context
  - path: pages/traits/metabolism/has_range_ph_observation.html
    sha256: f9fe3cdf429b8ed27f4b1760ef2172d2efee7cf12f0cf54883ff5493b93486c1
    role: context
  - path: pages/traits/metabolism/has_range_temperature_observation.html
    sha256: 8fd067c8295cde48d10b48800cb4467051079ad643911ada635b91346c310d67
    role: context
  - path: pages/traits/metabolism/has_temperature_delta_observation.html
    sha256: dc71f0681888cb6a6c0b9e5de56ee0318401621a01433d1974e92e0109fb802e
    role: context
  - path: pages/traits/metabolism/has_temperature_observation.html
    sha256: 018a13bc30ac2d40d160493426b3b7bd9cac88aa39aef6ea9279566908fa4b93
    role: context
  - path: pages/traits/metabolism/homoacetogenesis.html
    sha256: d57032ceab3f18e3e931b2be6eacd89830f555f8da6058f3e872230b4b243821
    role: context
  - path: pages/traits/metabolism/hydrocarbon_degradation.html
    sha256: 31a689f2e9948ebd04173d39e3f4f14f56be72f8d824e957fe2da75a05e24c6c
    role: context
  - path: pages/traits/metabolism/hydrogenotrophic_methanogenesis.html
    sha256: b6052164997866d9d9a4112b3fd5b1a2c4ca35a435fbb19d923d1637315c4463
    role: context
  - path: pages/traits/metabolism/hydrolyzes.html
    sha256: 60d340abc698d177cc5fbe7db4fb962d9b7c1fb2359e4fbe8c0a1fd16978cfed
    role: context
  - path: pages/traits/metabolism/imports.html
    sha256: d82402a37bfa3d728263bb124fd73995fbef6f9b72c287490f45c7b183e13b00
    role: context
  - path: pages/traits/metabolism/iodate_respiration.html
    sha256: fb092a2f09cd2091f77af2492a118e66e93fb14556574aeef7af7a3b08648a1b
    role: context
  - path: pages/traits/metabolism/iron_oxidation.html
    sha256: 46927697e44cab081d8bc8816c3b57550b257adfdb315cb04ff39db237f1e0d2
    role: context
  - path: pages/traits/metabolism/is_not_required_for_growth.html
    sha256: 51405f684686b0b5f0ce5cfb89949ae915e553de22c6682a21f64383956268cf
    role: context
  - path: pages/traits/metabolism/lactic_acid_fermentation.html
    sha256: 96e1097b1ada9d19d6a573d1e31c049f133774ac0fd5d25811eabf1fd3221cc8
    role: context
  - path: pages/traits/metabolism/lignin_degradation.html
    sha256: f73c93ca8f7aac4146fc71a13b130e345fdb7dfe5d0f3de358ced98f0b5e3e23
    role: context
  - path: pages/traits/metabolism/lipolysis.html
    sha256: 6cbb39a1d1d8b3b80afeaf22d069e396979dd0bb363fd183a5626e96ae14e83d
    role: context
  - path: pages/traits/metabolism/manganese_oxidation.html
    sha256: 6bb78de5644218d60dc410f80f0a18c4d92e18e57b40454863359eaa32edc56e
    role: context
  - path: pages/traits/metabolism/metabolism.html
    sha256: 175164132894017bfeacd610bbd5750eef93b0cbd004dc96d32bbef4e9da6120
    role: context
  - path: pages/traits/metabolism/methanogenesis.html
    sha256: cb1fe70ee2a39150a6de44e5e4c1358200700548f5d07f76ce54332167224449
    role: context
  - path: pages/traits/metabolism/methanol_oxidation.html
    sha256: a7bce3b0c4c9c8ad8b9356120846e575d6809f3d48a5e8daf7cf419772c327ba
    role: context
  - path: pages/traits/metabolism/methyl_based_methanogenesis.html
    sha256: 955b7137143c1d488c3172fecc0800f3332db4ab316515c5ee73cb23007d4f28
    role: context
  - path: pages/traits/metabolism/mixed_acid_fermentation.html
    sha256: a971bca834e81851eac3182dc6225763c3c8ac46e2ed3c84b8611ea21a72d254
    role: context
  - path: pages/traits/metabolism/nitrate_reduction.html
    sha256: 481ad5afb6de1d4f642407fdda02bc805a0b4ad4d25e28af30564f8534e9431a
    role: context
  - path: pages/traits/metabolism/nitrate_respiration.html
    sha256: 5d1a728d896114285be6514d27a2a3a864b65f7ac5db6d70fab383accd6d52ee
    role: context
  - path: pages/traits/metabolism/nitrification.html
    sha256: 4034f7fedbf4cbb9b10f7b1da101006248fcd30b90edca9fdc0c58f503f18abc
    role: context
  - path: pages/traits/metabolism/nitrite_respiration.html
    sha256: 0df3efa693445fada8074eceaea90386991b0735af73a20d27a85797e382b167
    role: context
  - path: pages/traits/metabolism/nitrogen_fixation.html
    sha256: db133f2d78b8d596d2188e54dfdd16b39dd46c36309135582e5cac854ce88928
    role: context
  - path: pages/traits/metabolism/nitrogen_respiration.html
    sha256: 824df9436f595ac315dd943d6808837ac3e41daed712e97fce54dd6f94156a90
    role: context
  - path: pages/traits/metabolism/organism_interacts_with_chemical.html
    sha256: cb76c8b4053e5865c1ba90b54c5a5a39aa9e8c0938429de6c38e058566550763
    role: context
  - path: pages/traits/metabolism/organohalide_respiration.html
    sha256: d01b69a0a41b62ce6bfb1ee86bed9b0d6b502e8aff46e9fc43dfbb69f70f15ad
    role: context
  - path: pages/traits/metabolism/oxidative_phosphorylation.html
    sha256: ed679139b220ebd0005eea821a2de85f0f58e5092aeba80bc4d0e3d146d09b35
    role: context
  - path: pages/traits/metabolism/oxidizes.html
    sha256: cb4108a06c0cc1d920c50e9831c07b5f3b10fdd2e3660fc8ca7bfa1da4a40c1d
    role: context
  - path: pages/traits/metabolism/oxygenic_photosynthesis.html
    sha256: b13656ae4b1e7563b6cfed95db00916060ba98fc18e4746dc09ecf36c6b95f8b
    role: context
  - path: pages/traits/metabolism/pectin_degradation.html
    sha256: 923ff4f87dc3da84ce263ec933b9a35802022690c513894ab9d761e2e5870481
    role: context
  - path: pages/traits/metabolism/perchlorate_respiration.html
    sha256: 50f99df0339c7b721a3cc3a3c4e04ec50003a4d298fa3be98123078acef7f99f
    role: context
  - path: pages/traits/metabolism/photoferrotrophy.html
    sha256: 8cb3f4d092641d8eec546d9f60332321b074941bb76a3f1f000f8ca8478df57f
    role: context
  - path: pages/traits/metabolism/photosynthesis.html
    sha256: 1511ee2614900853e92d252f5619a378886b551b5de5e55323c510f4b6da9569
    role: context
  - path: pages/traits/metabolism/phototrophy.html
    sha256: 84f59ab673ec6b9fb965cb143216adfe907c3b2fd5d1794554ad764c3a86eacb
    role: context
  - path: pages/traits/metabolism/produces.html
    sha256: e9c5c9583158268c1d6a092923aa8754e8d4bd16b0c04dbf8089cb7c83600d37
    role: context
  - path: pages/traits/metabolism/propionic_acid_fermentation.html
    sha256: e669236af9165d35510c3ffa2a9c8ed10912963eaa355c7caa94fd0bf470299b
    role: context
  - path: pages/traits/metabolism/proteolysis.html
    sha256: 3a7cc98024ba8fc02a7e7b575bd02e1050b340ed8a190a9c7c9b4bd9dec552b1
    role: context
  - path: pages/traits/metabolism/proteorhodopsin_phototrophy.html
    sha256: 4c7038a177ce6cf490283f051b7bd25b0b2c127767df5e32c1414e66e2bff014
    role: context
  - path: pages/traits/metabolism/reduces.html
    sha256: 5466b0bc1dfbe3ec21e10c29ade3b46c3ec8b1a8107d248df76f8adbde840e54
    role: context
  - path: pages/traits/metabolism/reductive_tca_cycle.html
    sha256: a7c487046859f3fd12ce3482ea6dd8f9cb33d6e949cd2533dea34b7b6c1466d6
    role: context
  - path: pages/traits/metabolism/requires_for_growth.html
    sha256: 4d3a681191fb4ad8ab6065f34efb6709e32810ec14ddb4477ba1c234fc58f5e9
    role: context
  - path: pages/traits/metabolism/respiration.html
    sha256: 92e1be90678334ba175f4aa30eb9f8ea7e0c86153d21868b6785c62f08811e99
    role: context
  - path: pages/traits/metabolism/respiration_of_sulfur_compounds.html
    sha256: 5ec2bbefec00755eec43a40b45a120d78dee25eec9e00dca4d5be42580a16d85
    role: context
  - path: pages/traits/metabolism/selenate_respiration.html
    sha256: bea37b314e36f5ec3a8462849757ad4b86f181e90d7d43995dded0cf5681dfc9
    role: context
  - path: pages/traits/metabolism/sequesters.html
    sha256: 2694d18d14713864d87159a61b96e76fbf25bf6a01c11f3dc495f009c0c675a7
    role: context
  - path: pages/traits/metabolism/shows_activity_of.html
    sha256: e7e58d683a881531b73a184ecb30bccdc0ff01a0c6feac69d424a478c5bd2785
    role: context
  - path: pages/traits/metabolism/starch_degradation.html
    sha256: 143b2d760242e0b26ae790ff37e418105c6037d13247a559748eadde57fa29b1
    role: context
  - path: pages/traits/metabolism/substrate_level_phosphorylation.html
    sha256: a14d8ca4e40f2c9df1b58f398ba0d237ee4eb259c4d3ff218841855f1bf822c0
    role: context
  - path: pages/traits/metabolism/sulfur_oxidation.html
    sha256: d51db27fffec2499b0eceb77102dd275e4652252b54c08a816f5b0f97b0725c9
    role: context
  - path: pages/traits/metabolism/sulfur_respiration.html
    sha256: 4a3ebea09e0aaa20467ac2a9b1a59acc30ee3ee8152382d6d888eac32d7c67b2
    role: context
  - path: pages/traits/metabolism/syntrophy.html
    sha256: b513800e69c3e22c750bd1cd3551c8b9312dc65f55a3e7885e93e42193529058
    role: context
  - path: pages/traits/metabolism/tetrathionate_respiration.html
    sha256: 3216393d7cf367568ef61a33a2328faaf2e307424bcb389b41635f67d6e32afc
    role: context
  - path: pages/traits/metabolism/thiosulfate_respiration.html
    sha256: bba456cda3dd2c8b5883af73ee8006c8b16aa30b778cc176b264f14a637a3ee1
    role: context
  - path: pages/traits/metabolism/three_hydroxypropionate_bicycle.html
    sha256: 385609651ccc4ddf49f7c5c400e1d5a087ab0910519c34fd943f7c89fe43b4b4
    role: context
  - path: pages/traits/metabolism/three_hydroxypropionate_four_hydroxybutyrate_cycle.html
    sha256: a17b2df63602739f083d3e1e98d22f321bcb6c9243789d543e3a5a7f53606a1d
    role: context
  - path: pages/traits/metabolism/transports.html
    sha256: 3488fab9564598d3e45f4d5b502d8e5244b83d50d867e78be85ae0f66f727500
    role: context
  - path: pages/traits/metabolism/trimethylamine_n_oxide_respiration.html
    sha256: 3a59b5f01ba25acd9247d5f72ee1354c4ca4c0fc04b910d5905eff36e1f8fb1a
    role: context
  - path: pages/traits/metabolism/uses_as_carbon_source.html
    sha256: 41f8f826bc79940e511e4c210dafb4dd04da3d823f6db525db53c47a19e87471
    role: context
  - path: pages/traits/metabolism/uses_as_electron_acceptor.html
    sha256: 2c78d06d628f0baec5af9eaa908b2a380773bc2485e1de28515b7dfabe191a3d
    role: context
  - path: pages/traits/metabolism/uses_as_electron_donor.html
    sha256: b2c08d9d441d14975e14fae26a9be50079dc932a10b81b95e358863576c4805e
    role: context
  - path: pages/traits/metabolism/uses_as_energy_source.html
    sha256: bb479c2c2043418dc546ed9a8612a8537edd52ca6f229b97a9fba833e9db29bb
    role: context
  - path: pages/traits/metabolism/uses_as_nitrogen_source.html
    sha256: 218132ce93d392ea19f90f0a8f7c7a5b2ac158026226500ffe7040966cdf8df5
    role: context
  - path: pages/traits/metabolism/uses_as_sulfur_source.html
    sha256: 722527b64fdb90c6fdc28983be6c77feae30db3f7bceffbb204350dd249b84f2
    role: context
  - path: pages/traits/metabolism/uses_for_aerobic_catabolization.html
    sha256: 9281c66886b719ca5ee0a7fa7822a5b629f9952b6c1ac4a188b2ab724b9da9ab
    role: context
  - path: pages/traits/metabolism/uses_for_aerobic_growth.html
    sha256: f08e41463b3306b3cab27778e3640d7ee0f9e439705e99c453672a1a35512acb
    role: context
  - path: pages/traits/metabolism/uses_for_anaerobic_catabolization.html
    sha256: 1b3e57bd2acfa9c55294b339ba098a2e0b180ac213014f1e24e655720796ef37
    role: context
  - path: pages/traits/metabolism/uses_for_anaerobic_growth.html
    sha256: 2fd6448b9f43dd6bcb1836406790f4e61b57d589b17a2f80db5d026ebadc1559
    role: context
  - path: pages/traits/metabolism/uses_for_anaerobic_growth_in_the_dark.html
    sha256: d96d0346b0ec3ca84c77b09ec43a41e25458d6f83bf01bb2f0a9bee3e3ffdb8b
    role: context
  - path: pages/traits/metabolism/uses_for_anaerobic_growth_with_light.html
    sha256: 3330e8112e84dd1d4c0068b6d06ca6985025b1cc5ab2eee8f2384bebcaff7b4c
    role: context
  - path: pages/traits/metabolism/uses_for_growth.html
    sha256: 4ab618d3ea9ea68b99891a67d2076d717792d95a46d2e3f5e400b11e947bf39b
    role: context
  - path: pages/traits/metabolism/uses_for_respiration.html
    sha256: 1c86b278453be4473285e9cadc54516a5c6040cbb0049831ab9da7adc0aea7d4
    role: context
  - path: pages/traits/metabolism/uses_in_other_way.html
    sha256: bb88a129ee830ff1f43a11b235e949b1e77ccefacd37095f43898793ba57831a
    role: context
  - path: pages/traits/metabolism/wood_ljungdahl_pathway.html
    sha256: 68e687810f99c46a8e780025f06b0e5c8ca18f4a6763dfb2c528a46c4dd197d0
    role: context
  - path: pages/traits/metabolism/xylan_degradation.html
    sha256: 13313209d30ebea2184e48a01e19c751e1f79b9c3d4e1a2290a433d6905218b4
    role: context
  - path: pages/traits/morphology/akinete.html
    sha256: b30621c409fc459673b4c571a32f593c71f6d4e2ef18f8aa3a8c68fb94775997
    role: context
  - path: pages/traits/morphology/amphitrichous.html
    sha256: bed2ea48fbf22a4ff6a1235e85647c53bc86cbcfac94c4b84697a69f2a244447
    role: context
  - path: pages/traits/morphology/axially_filamented.html
    sha256: e43a3f2f76053aaa6c64c1a00241557299808684be5592858917f2d12e04fe9f
    role: context
  - path: pages/traits/morphology/bacillus_shaped.html
    sha256: c2c7c7b52271eda9644d7f6219fbd4cc40f6d0e2e144a0300f2ebed23972e998
    role: context
  - path: pages/traits/morphology/baeocyte_formation.html
    sha256: 66c6ffee6ae11665f923a91205d64a630aa10d53ccb4e62f9dc48739e35589f2
    role: context
  - path: pages/traits/morphology/black_pigmented.html
    sha256: 287294fecfaa16d8883592168ea47b0885031ebf4321f85fbee716046bac5c21
    role: context
  - path: pages/traits/morphology/branched_shaped.html
    sha256: 893a3142756872b086ca91aa0be6b89b9b63001835488828784729d3cfbb090c
    role: context
  - path: pages/traits/morphology/brown_pigmented.html
    sha256: 1e1567700bc744902c096fec1d5396ac6453f9a202a582ebdf184893af1fb1c7
    role: context
  - path: pages/traits/morphology/capsule.html
    sha256: 79ff247d13a1508d207843162d84b0f92a1fa57cfbe8db9c75b13920b46f3d53
    role: context
  - path: pages/traits/morphology/carboxysome.html
    sha256: 423682241aef8fd0067fe6870f3adf04c2acef13dd714b4ce497c221b5faec69
    role: context
  - path: pages/traits/morphology/carotenoid_pigmentation.html
    sha256: a72afeb9327357976adfc5818ca839b999e2a366dc2565c1e1315d9f39c6eb48
    role: context
  - path: pages/traits/morphology/cell_length.html
    sha256: ff685f003fbf3e93dc25175bf7eb9294501efee546931393453660014d139978
    role: context
  - path: pages/traits/morphology/cell_length_large.html
    sha256: 8a6e4a2dd7b6ba1e6e462d981aba91a4bae136dbfeed84ca05f3f8014eefe45f
    role: context
  - path: pages/traits/morphology/cell_length_medium.html
    sha256: af26aa9909a8c15ad9401433800c5d37b086de4c0e96778f7ff490d9f43a0bed
    role: context
  - path: pages/traits/morphology/cell_length_small.html
    sha256: d714a92fcad29175fa7de66910410c1acf6e0de993bcc6442e28c9d9a4470625
    role: context
  - path: pages/traits/morphology/cell_length_very_small.html
    sha256: fc3e40457acebac9a80eb2f66baa966f642262eddd09aca688cb0bc78147c5c9
    role: context
  - path: pages/traits/morphology/cell_shape.html
    sha256: fc58047b1bb31853db14788246f5e6d91127f7ead5d33b21d540bc04327ca8d7
    role: context
  - path: pages/traits/morphology/cell_width.html
    sha256: 7ea7c2b38fef888b71884a81c5c338ec437362bb1877d0eb02a1ab3bbc6f81c4
    role: context
  - path: pages/traits/morphology/cell_width_large.html
    sha256: 9610bbbce082c6c17bf10ffb0eda0a09fecc25e5e39e10437039c09b957d105b
    role: context
  - path: pages/traits/morphology/cell_width_medium.html
    sha256: 7a9e2b20c390b5672c42c183d679cd2a91c6aef3d0a6133e3d4329a3498dc01c
    role: context
  - path: pages/traits/morphology/cell_width_small.html
    sha256: d559e56a35811dbdf5430eb922051e8a8ebbcd2b62e757159c9246bf7c82f531
    role: context
  - path: pages/traits/morphology/cell_width_very_small.html
    sha256: 9cb6aa1eb488ea927e8e5a79ec4ef8ff0a7114749fc25369745b4415484d50a8
    role: context
  - path: pages/traits/morphology/coccobacillus_shaped.html
    sha256: f7643da2a6a6723930d6e2023dca4875350194da5ade8980dc450c6a0df92332
    role: context
  - path: pages/traits/morphology/coccus_shaped.html
    sha256: e743d8cf263330d91bae1a19fe728761400a6947fd6c267af25c12a377b53ebc
    role: context
  - path: pages/traits/morphology/coenobium_formation.html
    sha256: bfe2d5414eab8fe868665178916c8347945af7167b429e69aa2a37de1326085c
    role: context
  - path: pages/traits/morphology/cream_pigmented.html
    sha256: b4804f4a5980c7b4747a4522ac66259c2f1bddaa5ee7d3034b00e1c2802238e4
    role: context
  - path: pages/traits/morphology/crescent_shaped.html
    sha256: 50efc5c0f2827ec25c599dbb0da485c6dde6bcb11e31b67bce97587d2980f050
    role: context
  - path: pages/traits/morphology/curved_shaped.html
    sha256: 269463ce60a51ad73ea797ae94adcfe2b95d6df3ab74c2f1d0ba6ea422f37d7a
    role: context
  - path: pages/traits/morphology/cyanobacterial_multiseriate_trichome_formation.html
    sha256: 220f1356962cfc0d24707e6f3b27b6d2558d5fb621779885209313d3368e7796
    role: context
  - path: pages/traits/morphology/cyanophycin_granule.html
    sha256: 7f4b9e4d5c6deb5fc11165ce23fdc97dc868226141fe4a3b7354002d8aef3ab6
    role: context
  - path: pages/traits/morphology/diplococcus_shaped.html
    sha256: 4b8f0b7207c565c9c50de098d79cef7038fe3de8d37f90dc5e8c651714ba72cf
    role: context
  - path: pages/traits/morphology/disc_shaped.html
    sha256: 4c656c01bc2365416d22d0ea759c32f5bf6674c999e1d83c0c3e5361902b003d
    role: context
  - path: pages/traits/morphology/dumbbell_shaped.html
    sha256: 7b4bc92a8cb48baf5538dbef611f7444b27a5fa3cde06f36de515cd49d110362
    role: context
  - path: pages/traits/morphology/ellipsoidal.html
    sha256: 60cdad4a9f5f22582618ca117fc3a246c38731386454a183cd87aa065ebc5a09
    role: context
  - path: pages/traits/morphology/expansion_driven_sliding_motility.html
    sha256: 7ba8142cddd310c03b17c3bd60dce894b13bc03108cbcac1d0557270a51f3986
    role: context
  - path: pages/traits/morphology/false_branching.html
    sha256: a4d3d4d19513069b1d32abac8fb4437ebd73a0181107f3970cd013b35879ec56
    role: context
  - path: pages/traits/morphology/ferrosome.html
    sha256: a4a3d673cbe9de5733c7dd8cde3476984e5f289c0ba4bb028801cfa4cf426107
    role: context
  - path: pages/traits/morphology/filament_shaped.html
    sha256: 6de55828c1d8b775530408669bf02738ba50c10841930dfd5bbb227847a6d15d
    role: context
  - path: pages/traits/morphology/flagellar_arrangement.html
    sha256: 4bd8f40f9304a840ed26ee6102cd33ee8627e03e2063e2db7a552e020d71e653
    role: context
  - path: pages/traits/morphology/flagellated.html
    sha256: 327db13d5751e855301e21a25de9e014e233fddb28eda667530b88ae02da215c
    role: context
  - path: pages/traits/morphology/flask_shaped.html
    sha256: 402feafc0ed101c9fd5d0c9bd31bcb85c98267598c3702c452ed2b1e0c698090
    role: context
  - path: pages/traits/morphology/fungal_adhesive_column_trap_formation.html
    sha256: 4ff42eb3450b4ba0d6d3111773dd9fdb19d40bf3dd9e15a270cdc66bcc8faae9
    role: context
  - path: pages/traits/morphology/fungal_adhesive_knob_trap_formation.html
    sha256: aaf5e1c37e284cefea38525a0edd4c5b723c55b582c21c5b41de7bd11a737383
    role: context
  - path: pages/traits/morphology/fungal_adhesive_net_trap_formation.html
    sha256: 86295b6e8757f6d978fe08b0ccf56a952b98d061191b4837510e4377d8269e6a
    role: context
  - path: pages/traits/morphology/fungal_appressorium_formation.html
    sha256: c95aa45331bdd07c64e6b5aecf88a14abc634f9a953ada32b6ff9f9f2e432adc
    role: context
  - path: pages/traits/morphology/fungal_arbuscule_formation.html
    sha256: 9242ececd47cc8fcc3cebc92506a7b4ccb43504f60cc18d3cdbaefe642d6b26e
    role: context
  - path: pages/traits/morphology/fungal_auxiliary_cell_formation.html
    sha256: 4c56404c92f051098e5f33ae3a1b58b4a8ec67b5da9ed16737bd6df8d9e27a58
    role: context
  - path: pages/traits/morphology/fungal_branched_absorbing_structure_formation.html
    sha256: 95a6ae487a62f2ffef6575a7ad9c0f62932bc19e773c259b1dda9b42ff5f66af
    role: context
  - path: pages/traits/morphology/fungal_chlamydospore_formation.html
    sha256: 9a08d724c9dbe999edcecf982b14c05f56509a0e9f8422011a2f78a72d296984
    role: context
  - path: pages/traits/morphology/fungal_conidiation.html
    sha256: 02cca64fcd4bbccb7ee4b31638dda41671e6fe3f23f4d08c6b8e337b9cbea8bc
    role: context
  - path: pages/traits/morphology/fungal_constricting_ring_formation.html
    sha256: 6fe879aab0b8d2a520155746973db097fb6368fddccff09fc9ff38cf6dfd20a9
    role: context
  - path: pages/traits/morphology/fungal_hartig_net_formation.html
    sha256: 8ad69c2ab8568d2755258c2b6841fa86929d39fab9b37039343f79034d20211c
    role: context
  - path: pages/traits/morphology/fungal_internal_mycorrhizal_vesicle_formation.html
    sha256: 2a1575cf02d45fef69d5384bc58ce1f41d6995a9aa0c79e41b5387a8d6b18c2b
    role: context
  - path: pages/traits/morphology/fungal_mycelial_cord_formation.html
    sha256: 203e0ed7fdbe4015451f12db877c45d054a4378bbe3d1dbab09d219fba78ad95
    role: context
  - path: pages/traits/morphology/fungal_nematode_trap_formation.html
    sha256: 645ab68fd063721dcae0d83a8b6ab33b65999b1afa2bfdd52ad2bda8217dddfe
    role: context
  - path: pages/traits/morphology/fungal_nonconstricting_ring_trap_formation.html
    sha256: 272e1bf67f2ce5e7176afcd67883d939189bd10bd36de57735d062105140cb1a
    role: context
  - path: pages/traits/morphology/fungal_peloton_formation.html
    sha256: c0024dc29b2fed0e63bf5aaf0805c708af196ed11b6bafca8863cdd9277a70ff
    role: context
  - path: pages/traits/morphology/fungal_rhizomorph_formation.html
    sha256: 9ae83fa2cde2a147c5b92a372e73f1b18a5824f16a573fecc9c3d2f464d35e71
    role: context
  - path: pages/traits/morphology/fungal_root_mantle_formation.html
    sha256: 9348320f8f40a9eba639e52d3e280310488833df470e4e10ec99c85de796998c
    role: context
  - path: pages/traits/morphology/fungal_sclerotium_formation.html
    sha256: 42749cd2875e31d6d57b9f1957ea5ad391e55b5e08d3132e744c97320cbbcdbd
    role: context
  - path: pages/traits/morphology/fusiform_shaped.html
    sha256: c50d7a55bb61024b64297c7aa3f49a81c594d151a354f3dcd0db90f71ff19b27
    role: context
  - path: pages/traits/morphology/gas_vesicle.html
    sha256: 4693591750272b03163f12f23eae3ff5460959b8570e5e54967c542e836b251f
    role: context
  - path: pages/traits/morphology/gliding.html
    sha256: f6b646e235da3090e3df6d5cc8ed81282d1b112f78b0de24ba4dc95df4cf791c
    role: context
  - path: pages/traits/morphology/gram_negative.html
    sha256: 8b40132dae037d5f1bc3c7d0adb3e64843bf29f3c41c66770a292027e5da4fc8
    role: context
  - path: pages/traits/morphology/gram_positive.html
    sha256: bdaa4b0564e51cdf2eed19871ce826af8d73a917dc13d183ae72f492769ddd46
    role: context
  - path: pages/traits/morphology/gram_stain.html
    sha256: 20f9545fbe7d7a3e7c57fe3f30a8bcd82b2e266961db16f211597c6b21fec874
    role: context
  - path: pages/traits/morphology/gram_variable.html
    sha256: ee1ef63a2d87df14da186be608539503266512858d8b779a10bd8c291d9014a5
    role: context
  - path: pages/traits/morphology/green_pigmented.html
    sha256: 123243595ed70dc02b735fd54d95db844bb8245092c39c553530ac2c03a7582f
    role: context
  - path: pages/traits/morphology/helical_shaped.html
    sha256: 2c1fbb397fd2d334aa4a4b28b765d36c39109449e74008784b08c5ceddef29cf
    role: context
  - path: pages/traits/morphology/heterocyst.html
    sha256: b9b1e6b0b07ad35eff2dd838f6fd70db17470b445edcf29ad36a532df38d0cb8
    role: context
  - path: pages/traits/morphology/holdfast.html
    sha256: c40ca1990aca27f8a948f1bb778a28944791e8d98b16985adc81a010958cdedb
    role: context
  - path: pages/traits/morphology/hormogonium_formation.html
    sha256: c6269d9b20896b9e78c2d9fc700200044a4ac0da7e0b53affca2ae916d9aeec3
    role: context
  - path: pages/traits/morphology/intracellular_inclusion.html
    sha256: 2b38ccc790854ae9488adf3c033c392db3500ecd10ec2485b8019daf5e66b62b
    role: context
  - path: pages/traits/morphology/irregular_shaped.html
    sha256: 3516c427a3d271837d3dda6e770db04b773781973c4c0ab873488a9c94b1bc61
    role: context
  - path: pages/traits/morphology/lateral_flagellation.html
    sha256: f1bb29266c25040c179952070a8b60e5ff9250fe7697e85223b75d1a891b7865
    role: context
  - path: pages/traits/morphology/lophotrichous.html
    sha256: e078d362ddc185afca21361822eb4e97e7a4303f9c602fe7bb32356f7953afb2
    role: context
  - path: pages/traits/morphology/magnetosome.html
    sha256: e16c02ee1344f51fe296c2b008da2543865ebc66bd58ef82ec9959f6249b3504
    role: context
  - path: pages/traits/morphology/microbial_haustorium_formation.html
    sha256: bd0536ee82cb1e548bab9ac3ee411eb64ee1853b890a63107d6f4f2fd96fd173
    role: context
  - path: pages/traits/morphology/monotrichous.html
    sha256: 29be9102e04449faa04510de22f67e2f1b12d6275cbb7e385ee2b6efc8b7fc5c
    role: context
  - path: pages/traits/morphology/motile.html
    sha256: 4cca076b5e3e8eda5a723716c3bd01847b1f5cf9d0bc17fe2bc0e89a9030ba67
    role: context
  - path: pages/traits/morphology/motility.html
    sha256: 7eb48b023605873cef55b305e251cc026085a674b9b36fcf02fb218aadb24161
    role: context
  - path: pages/traits/morphology/mycelial_growth.html
    sha256: 5d066d1ae044293dd3486fd15ca858e8bcbe3c92cc430ad6c8cc032295e7e961
    role: context
  - path: pages/traits/morphology/necridium_formation.html
    sha256: a55450bb34cc3ea71cf32beb61fe03077cf8bc76c478b8dcaa7a4142ba5db233
    role: context
  - path: pages/traits/morphology/non_motile.html
    sha256: a897df46655769dff6515bf2c9b39a4ac579247ec8afadb6bd9befecda7af068
    role: context
  - path: pages/traits/morphology/non_spore_forming.html
    sha256: 96044e16f0a54ff1d187ae0cf382c2da368f8149ef62fc0ab6e3d5cdb2797219
    role: context
  - path: pages/traits/morphology/orange_pigmented.html
    sha256: 60a2277ff72ec948ece2c6ce0e4e7383d6ecd222293942ca2fbfc148271f0da9
    role: context
  - path: pages/traits/morphology/oval_shaped.html
    sha256: b142d5e6512a2e28c3e34ad2a2fe2ec7b35e02d244631b26ac6b44cb74ce1b01
    role: context
  - path: pages/traits/morphology/ovoid_shaped.html
    sha256: 0706fceb9904eadc93f0baf53e3fdc08f2823776fe22bf72e02f7df80ee18d65
    role: context
  - path: pages/traits/morphology/palmelloid_formation.html
    sha256: f01194865bbc5e30deed2ad034046d5dc0f76c81876c926ee1b387c3940496a4
    role: context
  - path: pages/traits/morphology/peritrichous.html
    sha256: 7ff4f0f532a8110dec52f1b3678e5f96c3213662191bc17a5c9988d9296d96d7
    role: context
  - path: pages/traits/morphology/pigmentation.html
    sha256: 675c4c160ba51dc0c99b771c4be2d65206d3497b7f981cc1467387ac813bd98a
    role: context
  - path: pages/traits/morphology/pink_pigmented.html
    sha256: 4bb4dc9819cbbdfd9702d9cd8e54dfdc6212fd1d7218462d0552eb5757939009
    role: context
  - path: pages/traits/morphology/pleomorphic_shaped.html
    sha256: a77b5a05686eb2d0d545fd1461f46e4f3a84a86681cdc8b465e2ecb02691f0cc
    role: context
  - path: pages/traits/morphology/polar_flagellation.html
    sha256: 59e695eafd27de897f17bb90b6bc3c800a6de66919f2a06fe019c796094409b6
    role: context
  - path: pages/traits/morphology/polyhydroxyalkanoate_granule.html
    sha256: 8f3da4d92de4295440a12e5e5a9b71009181f708adbb91135595d53f467fe7a0
    role: context
  - path: pages/traits/morphology/polyphosphate_granule.html
    sha256: 6d85975e1a871a194f81c8d90dc58e16c04fc6f6bd08f454caf23dc83d0044a2
    role: context
  - path: pages/traits/morphology/polytrichous_flagellation.html
    sha256: fedfe99d70e7d228425f294343ca890fb5e80f4de06e571b7f755dcea9a3fb25
    role: context
  - path: pages/traits/morphology/prosthecate.html
    sha256: 3eacacee3315ffa4ec3ef138fa06f2bf4a853ab530f7fca7a6233ec983860b49
    role: context
  - path: pages/traits/morphology/pseudohyphal_growth.html
    sha256: efabec52bcdbbd4ac4e850bf674e4196d00c2bbbfc59c510286b5246b4135e80
    role: context
  - path: pages/traits/morphology/red_pigmented.html
    sha256: 4f5ffb036397afa2389559044371514a02617e045979fce603d5e976e0d6413e
    role: context
  - path: pages/traits/morphology/ring_shaped.html
    sha256: 776393d8b1e8521e9db578a4e06434c7f10137e853e82c16ba06e7d377b29272
    role: context
  - path: pages/traits/morphology/rod_shaped.html
    sha256: ec9346932b9319b604d85f565f08a439e9655838011d2f6e0ce5d5508430706e
    role: context
  - path: pages/traits/morphology/rosette_cell_arrangement.html
    sha256: f353927e64b610bf5a89086bf0d331516c7943ebd5d938b3623a2d5d85384522
    role: context
  - path: pages/traits/morphology/s_layer.html
    sha256: 69d60b1475921346658086984b0e678e7c15744d2a2dc1fc3182aa7e5e331356
    role: context
  - path: pages/traits/morphology/sarcina_arrangement.html
    sha256: 13948108de325e2771accad58c3c0cc0d17ec5ba97654afff98a5c238fa66049
    role: context
  - path: pages/traits/morphology/sphere_shaped.html
    sha256: 00f570e8b41d6344dbd873fb03c8bd28cc7a83c098f598eac5799bbe4fa31e5e
    role: context
  - path: pages/traits/morphology/spindle_shaped.html
    sha256: bee630ab86d4018db1c4a54338e4b11793b8ab37791401055426e85c94c26de5
    role: context
  - path: pages/traits/morphology/spiral_shaped.html
    sha256: 80cbeb4d1ec351e61f3340b53aab22b568d2f98f4b1d7f7cf064584587cda97c
    role: context
  - path: pages/traits/morphology/spirochete_shaped.html
    sha256: 250390be2cdcc112156aa9b0122097d8273431abf575b3c097c1eaa65cdca970
    role: context
  - path: pages/traits/morphology/spore_forming.html
    sha256: e358a5ca615ef26cdc654299583c2768c353d5e7cc344768b6c6c4ca072ef7ed
    role: context
  - path: pages/traits/morphology/spore_shaped.html
    sha256: 94d8286842e6b176483114624681e29b8f2cdab6b321114b461f7b7eefc66d7b
    role: context
  - path: pages/traits/morphology/sporulation.html
    sha256: d32b73bac4b12a241777d2ba0846d94c7259f2cdc60452818756989318f8be1c
    role: context
  - path: pages/traits/morphology/square_shaped.html
    sha256: c77eadbfd200f4000efdc72e028ad86f9d26990872be75431d45de7a52f103dc
    role: context
  - path: pages/traits/morphology/staphylococcus_arrangement.html
    sha256: ee49457ab756f99d59ecf19d1bd4871ee257b935f06cef916d0e5475184bec18
    role: context
  - path: pages/traits/morphology/star_shaped.html
    sha256: ae6d8124ad7b2a137b84d7073f021bd5494845aea92883986f1769105e5b9cc5
    role: context
  - path: pages/traits/morphology/streptococcus_arrangement.html
    sha256: 5a3008e9950465bc229f27b1aab02dc872eade56066bc4e50fc5cf3ef91aa67a
    role: context
  - path: pages/traits/morphology/subpolar_flagellation.html
    sha256: 2ede1a85ce8088f8a3791f8e43cc8cd3f4726011f18dd56d9e299d2bbe8990ba
    role: context
  - path: pages/traits/morphology/sulfur_globule.html
    sha256: 3131582f1fdce5f14ec970622ede224e88fe4cf6ad03c915cbe8fd0f8abf8b98
    role: context
  - path: pages/traits/morphology/swarming_motility.html
    sha256: 6a9b78cbec1f20b32fb405187524b9a9fa87b4e74a927745017548e1d64eb20c
    role: context
  - path: pages/traits/morphology/swimming_motility.html
    sha256: e345bde3148ff3243872b8af5f227a0af0b9fad586a2509493884b600930b706
    role: context
  - path: pages/traits/morphology/synnema_formation.html
    sha256: ef6f912c6dcebe341883ec238e3e0b73f785564e4f1f23288e825aa9ed9c3a32
    role: context
  - path: pages/traits/morphology/tailed_shaped.html
    sha256: 47c8a44c7ede138bcff0859c0b09b0c8f95024a994a52d8d1410f838cf80c898
    role: context
  - path: pages/traits/morphology/tetrad_arrangement.html
    sha256: 07131e1bda79b1100e2a515f908cb2e85ac8617e05cbedf834976359b7f8be6c
    role: context
  - path: pages/traits/morphology/triangular_shaped.html
    sha256: 42c05ce6d0b9de7b55e4267f3941698109ad7ba39c4ba7cc77554ec25f9edaf9
    role: context
  - path: pages/traits/morphology/twitching_motility.html
    sha256: d4ca733291577c98488363bf92dd449da08a4e07148e0cef52301c7fffca32c4
    role: context
  - path: pages/traits/morphology/type_iv_pilus.html
    sha256: 7b7ac79a04a4431b7e7327153a10fc9273b8ebebcc255fbaeb58b21a31f60e2f
    role: context
  - path: pages/traits/morphology/vibrio_shaped.html
    sha256: 25b1aa01fa63b05bb3b627b646e99141358a07bd20e31f56bcc5bad4c21fae6c
    role: context
  - path: pages/traits/morphology/white_pigmented.html
    sha256: 2dc3d984dd7a77afd0a18acc644470dbb86c965f6e990bd42b0412eef6c01279
    role: context
  - path: pages/traits/morphology/yellow_pigmented.html
    sha256: d0153c4d321bf48101bdbaee1dfef103734f27e82ee34c810e27be9c69c2f306
    role: context
  - path: pages/traits/observation/growth_nacl_observation.html
    sha256: 3b0dc0b5ffe4e8f47ac416d39216960e84b83ab49c3770af8db1558aee92c353
    role: context
  - path: pages/traits/observation/growth_oxygen_observation.html
    sha256: d18afdc5d12816297e978ec748762150f9a364938e0ff8137cf0191ea6451a1e
    role: context
  - path: pages/traits/observation/growth_ph_observation.html
    sha256: b0fc89cc3d12359d5ae7ab76c886ca6c22543749514d2d86a03d3777af730154
    role: context
  - path: pages/traits/observation/growth_temperature_observation.html
    sha256: a72893db2a136c1cb940d66faf11db1f56fe36400816e2f47f51a6471f69d632
    role: context
  - path: pages/traits/observation/nacl_delta_observation.html
    sha256: 145e737d223fdd23414a876b2058b46ec21835faa9f4489b3acb84a0e0bfa267
    role: context
  - path: pages/traits/observation/nacl_observation.html
    sha256: e8e54f7767a1964dacb5177ee20ffa12c350066d4c480de0c98cb20cf0bf0df3
    role: context
  - path: pages/traits/observation/nacl_range_observation.html
    sha256: 52115b746e30b42b48f90320b3ff735cbf4fca7414821318228959547b57a054
    role: context
  - path: pages/traits/observation/optimum_nacl_observation.html
    sha256: 59503c8e07743c500e06b6e8a124cdd3f9a242d0de9a5197678dd0229d087b5e
    role: context
  - path: pages/traits/observation/optimum_oxygen_observation.html
    sha256: edefd52e59f23d3329940fe1646942b3adea0729bad69e1b549d1821e6501566
    role: context
  - path: pages/traits/observation/optimum_ph_observation.html
    sha256: 35f9bad99e40542a130849386d85d6005d02830a28e618c42a72a84d7cb65d45
    role: context
  - path: pages/traits/observation/optimum_temperature_observation.html
    sha256: 2734c974f149ba932c47aa336fac34c075500d55955df4c0d21e054fc6bc9552
    role: context
  - path: pages/traits/observation/oxygen_delta_observation.html
    sha256: 341d36f1f44dce794592b0fa001653b9134b9b0a01793dbc4bb5f3ce6809ebb2
    role: context
  - path: pages/traits/observation/oxygen_observation.html
    sha256: 153453b3da1ddaafda1582b8aa36efc62efbcd788763f7f84b5ab2798ca35066
    role: context
  - path: pages/traits/observation/oxygen_range_observation.html
    sha256: 242dabeed81edf33315e0d4925377a51e293ab228ad6594e1d28547aabb64dd5
    role: context
  - path: pages/traits/observation/ph_delta_observation.html
    sha256: 77cf44260d2aae671b59cbfb5a04a79f3aa94f6b5da3614c2925d977e50fa345
    role: context
  - path: pages/traits/observation/ph_observation.html
    sha256: 238cbf8fbb56300fe5feb8f079e4f22e4b5c0a9c94aadff3a4276beff5c248f0
    role: context
  - path: pages/traits/observation/ph_range_observation.html
    sha256: 51d0553ce3fb9e64102f2701100cb0827872cd6af0eed0aafab7e5e3edf21e28
    role: context
  - path: pages/traits/observation/temperature_delta_observation.html
    sha256: 6fe1c47d2d28e1a147e4aeb456d3c1e8919cb91d40631d1a8d767b0e2c11b9ba
    role: context
  - path: pages/traits/observation/temperature_observation.html
    sha256: b9dec1b6e5819236d27a09b792feb2238539d0316adcd813c2070af858c79d9e
    role: context
  - path: pages/traits/observation/temperature_range_observation.html
    sha256: a929a15672d86a390a1e500d62adab34becf74e0f68351d7c4d2cd7efed17e7c
    role: context
  - path: pages/traits/other/catalase_negative.html
    sha256: 48e7118e829f97ab37a3aa1266bdc96dcd5736f35a9a7529ad8ec159543b453d
    role: context
  - path: pages/traits/other/catalase_test.html
    sha256: efdf1f606a032cdbe928154d38372b14015790335bd4c6bad8800ff79293ae28
    role: context
  - path: pages/traits/other/circular_colony.html
    sha256: 65a54d8d5902e252d8cb9147707fdc728a66b1b56cbaa6152f645c9c7170d148
    role: context
  - path: pages/traits/other/coagulase_negative.html
    sha256: bee4f8411e456f55c86595caba23cad7b69c95da29ece78235f85c925a6776b6
    role: context
  - path: pages/traits/other/coagulase_positive.html
    sha256: eb6c0f5d8054b9d4e22d4664c069c2cb453987ae2d5ca97133c7b72ef98b141d
    role: context
  - path: pages/traits/other/colony_morphology.html
    sha256: 105e9f99cfd732b24e445ee212839e5a9eb612a0f7e4f186dda9fa8983165b05
    role: context
  - path: pages/traits/other/colony_shape.html
    sha256: 51fc35e1a73e7f1d1d45369a746eafa4df253f762cdcbfa7e40600bf343228b3
    role: context
  - path: pages/traits/other/epibiont_phenotype.html
    sha256: a45f26a9e46132ea16da93c02cb045ff99663d944d63d33d0a8c2bfc0f440a22
    role: context
  - path: pages/traits/other/filamentous_colony.html
    sha256: 8096d944f3e4d81437263599a65b9bad92b8132c18e34415c8647ffe901dfe85
    role: context
  - path: pages/traits/other/fried_egg_shaped_colony.html
    sha256: 322e30dc2b535ff33732d37f12a8196f70ea532ced17954c30f2b29124308728
    role: context
  - path: pages/traits/other/generalist.html
    sha256: 1ec682a7e5f351cdb4b3c57dc46191b203da7ee6ea120762ff8e2bdb5a456f15
    role: context
  - path: pages/traits/other/hemolysis.html
    sha256: 3e55b45ca3ce48d56e00e94caacbbb9c774c19fe9584aadca479c1c7bd8ee7ea
    role: context
  - path: pages/traits/other/hemolytic.html
    sha256: 2b9430fc5e2637a26d16a8b12afd71b7cb942d171d295d40cf2d82f444292986
    role: context
  - path: pages/traits/other/indole_test.html
    sha256: 66c82c4230d3594b3902d1e96aea810f5a703e0bf9157d80cfc21a1c12020aee
    role: context
  - path: pages/traits/other/indole_test_negative.html
    sha256: 041834c18b37883ecd71fbf5f17144f6a99f06b1b90d350a93124699459b1eb7
    role: context
  - path: pages/traits/other/indole_test_positive.html
    sha256: 07fa2cc54ffb8d9102108301f248a6a3a8b3b960e2989575ee7a0a7aefe5de70
    role: context
  - path: pages/traits/other/irregular_colony.html
    sha256: cd7e3a04e26d9950f18ae24d66f1fb2a37ce5b182f41b3558e421db9196707b1
    role: context
  - path: pages/traits/other/methyl_red_test.html
    sha256: 8921b374f7443cfb786832cab05e31d8edfd6fc26d6f885f4c9acd18502012f1
    role: context
  - path: pages/traits/other/methyl_red_test_negative.html
    sha256: 233d0b638239ff612e76b5e3cc8486d8845bb96edbba67566fb42e40ff963959
    role: context
  - path: pages/traits/other/methyl_red_test_positive.html
    sha256: 08c3593aadc49e26974863a6c72d3d7465aa9b785773f97c38fc5c905fbc4781
    role: context
  - path: pages/traits/other/non_hemolytic.html
    sha256: f85850fd4b73f5e27cc22500cc40ee2716aabea74bdcf2994a1bcdf1fde85cda
    role: context
  - path: pages/traits/other/osmotic_tolerance.html
    sha256: c6ded1cf6f3b677c017ff22aa25cf2248d49cf416f2b1592a16405dbbb718950
    role: context
  - path: pages/traits/other/oxidase_negative.html
    sha256: f4bdefe572b8cf289b97d998613f2d5308773171d8b04c482e49559cb15c9078
    role: context
  - path: pages/traits/other/oxidase_test.html
    sha256: d068f265d48faaf5a6bd6039d05ce884e4b0348b80d58a674dda24155d1c37d7
    role: context
  - path: pages/traits/other/punctiform_colony.html
    sha256: 9a93d4078c5605d62737a8ccddfe1b38214946e28d933c0aaaafab4524a09c6a
    role: context
  - path: pages/traits/other/rhizoid_colony.html
    sha256: 2bd0efcfa2db3480d3ff0f9f5355eba50179396700386d2517f04b90c573be4e
    role: context
  - path: pages/traits/other/specialist.html
    sha256: 4ad3abb20f6dd0338bb10e324885379910e876cf7bcbd1b05d7b9942154ba42a
    role: context
  - path: pages/traits/other/urease_negative.html
    sha256: ca13d1f68190b2d5ad27be87175c08d3430bd9620f4555056cfdcf1e43e837a5
    role: context
  - path: pages/traits/other/urease_test.html
    sha256: 30dc7c86fe1d8e565c48bbcdf504c42ced13f5196501d8bbbe40458ea687c643
    role: context
  - path: pages/traits/other/voges_proskauer_test.html
    sha256: 19cd0567c83dc5eb37df3b270c97367b3401832066778c5dadca3c953b508ea6
    role: context
  - path: pages/traits/other/voges_proskauer_test_negative.html
    sha256: bb67cdceecf76ab29edad6211ef917dd2464b151e76d63a09f176a3d7caa7b35
    role: context
  - path: pages/traits/other/voges_proskauer_test_positive.html
    sha256: 2e41046dffa530c79660241f855045a2c691763aa5368a6978185ae89b36785a
    role: context
  - path: pages/traits/physiology/acid_phosphatase_activity.html
    sha256: 99c7dc15a40b809f3e9b51cf0ee3c210024bb7ea27aa1871ed1f2b94d5f7c0d8
    role: context
  - path: pages/traits/physiology/acquired_stress_resistance_memory.html
    sha256: 2593aa1c83253a48fa96042e05e1ac3aadb230c9bc651559adc612a4dfdc36ed
    role: context
  - path: pages/traits/physiology/aerobic_anoxygenic_phototrophy.html
    sha256: dacf5c8af15906c6566bdf33fd85844462ed15f87a48d0dc56abfb344d7d9bd7
    role: context
  - path: pages/traits/physiology/aerobic_overflow_metabolism.html
    sha256: 31ec3e08239b9af090722cafe5b54e70f8803220824048a02b36fd186bb42ac4
    role: context
  - path: pages/traits/physiology/aerotaxis.html
    sha256: 1df2504f5d9f71fd234b31acd23756100d8c95fb7b7ad4fd47b3f896c6f8bdff
    role: context
  - path: pages/traits/physiology/aerotropism.html
    sha256: 8c6755e7cdd4afffc818fb118702fe4dab31f4a06ad0e798f89b6d6e8ead5b82
    role: context
  - path: pages/traits/physiology/aggrephagy.html
    sha256: 5db20feebe13e234bf6ce8a6a08232dd05728b43732c5fd0c3d62b60434b4bac
    role: context
  - path: pages/traits/physiology/alanine_arylamidase_activity.html
    sha256: 9982589b9efcba1643a05f575a04736ec2fba1380faefd2302c997f05451c807
    role: context
  - path: pages/traits/physiology/alkaline_phosphatase_activity.html
    sha256: 8fed0acab94ef241942ee9069fc945143e4779bc8aa93641961b20e922c04dc4
    role: context
  - path: pages/traits/physiology/alpha_chymotrypsin_activity.html
    sha256: f49a633d76160ca2be3c088d81c39efa7bc04b252caac9fa11b9bb15bb3c1192
    role: context
  - path: pages/traits/physiology/alpha_fucosidase_activity.html
    sha256: 936d371d0cd38d50665bb2494d9fce21e48cacd4efbba6d11972a892f74ea688
    role: context
  - path: pages/traits/physiology/alpha_galactosidase_activity.html
    sha256: 3d571d5bd66bf7ac3bf7dcd628578fe6b6f55dbe04c70edc8649fd18df64e73f
    role: context
  - path: pages/traits/physiology/alpha_glucosidase_activity.html
    sha256: 683ac0d8c63b19f051535e3b90108a987b39884c4362706a7fed58b2e5619b99
    role: context
  - path: pages/traits/physiology/alpha_mannosidase_activity.html
    sha256: 9977a3183bc786495b57ee88b2a8ebb29fddc055e3cfdbb1bf43b7ca393e68bb
    role: context
  - path: pages/traits/physiology/amylase_activity.html
    sha256: 0f64dd2ec1a79c209f79405ce6faba67d9e249f03437456db1a310f1b170e8cd
    role: context
  - path: pages/traits/physiology/anisogamy.html
    sha256: b88a68e305875631f5199ee011761111f2ac9fd6bc1bc5e5e293f04fd4da125e
    role: context
  - path: pages/traits/physiology/antibiotic_resistance.html
    sha256: ea9ea46eab83d117facc080a1aa344d3857618280ea5399aa6084d2c002ad6ff
    role: context
  - path: pages/traits/physiology/arginine_arylamidase_activity.html
    sha256: 0a4de8e19b548a9760777f4a49255046519918e87cd6f91a4b6ed3193598f74a
    role: context
  - path: pages/traits/physiology/arginine_dihydrolase_activity.html
    sha256: 118ccc26c284e57fae27bf9ce4c03eb38aa0c78fa18f4f0c062fa36782c08bfc
    role: context
  - path: pages/traits/physiology/autogamy.html
    sha256: c9d6dd7cd163751aa40b9e8b8eb2ab6d2b032bf9c1d2a20e9d94cbd09075f54f
    role: context
  - path: pages/traits/physiology/automixis.html
    sha256: ddf601447ead2c357e654d2d2276ae4a19bc4ea3be4a86749c098f660860d25e
    role: context
  - path: pages/traits/physiology/autophagic_glycogen_degradation.html
    sha256: df345fada56ef03685a32b80872079dc8c41c8c193c42345095f60a6a5a57a34
    role: context
  - path: pages/traits/physiology/autophagy.html
    sha256: 6a646c8a75904df4b38fbd9019ebd9db8894cb872ec9da78b341855b01be3917
    role: context
  - path: pages/traits/physiology/autotrophic.html
    sha256: d577888a28ca791cd616f432307d142f0a128240c0cfe42fa1b106a74bca1b9f
    role: context
  - path: pages/traits/physiology/bacteriocin_production.html
    sha256: 321c342807cfedc415283f17111dbda438433f5735c2c522c5f6300cbd5b0a3c
    role: context
  - path: pages/traits/physiology/ballistospore_discharge.html
    sha256: 6ecbb275d923f8e018ffedc7ad44386e89ba9b981d562189b8b5a299d2f841fe
    role: context
  - path: pages/traits/physiology/behavioral_habituation.html
    sha256: 165cfb765e4278dd64d6dff5e67b9566fceb0986c697f11724dbf0bcdfa20ad3
    role: context
  - path: pages/traits/physiology/beta_galactosidase_activity.html
    sha256: 76fb01e4e1e8bd6515b11097ac626172a727305a167587cb5a0faaa5d143fcdc
    role: context
  - path: pages/traits/physiology/beta_glucosidase_activity.html
    sha256: 6535c95cffe133fd013ac680a5fb3bad5823193fe6ed4d07103b8c820fc433e6
    role: context
  - path: pages/traits/physiology/beta_glucuronidase_activity.html
    sha256: 22ea304451cac682ea2420ae0f7e4dc657ec0e5d2a78d420e7c249451e69755b
    role: context
  - path: pages/traits/physiology/beta_n_acetylhexosaminidase_activity.html
    sha256: e0a24b671dedd98a74205b6a482dfbfd054b781db3d6ed6fe8ec4eabf0cb1fef
    role: context
  - path: pages/traits/physiology/bioluminescence.html
    sha256: 7549d5ab992cac0cb432756e139a7f462b07da7ea40437d779fe63b6befee5ec
    role: context
  - path: pages/traits/physiology/biomineralization.html
    sha256: b06fca6ba62350bbe7ba2660b80f5a7cbdfcf7b4ca23ba4ea3fc9d955338df08
    role: context
  - path: pages/traits/physiology/bipolar_mating_system.html
    sha256: 21a8e267e32839ccea4b1f29e243f1247903a4452b7083e79485d29f41d860e8
    role: context
  - path: pages/traits/physiology/carbon_source_memory.html
    sha256: f2a93b061c3abfb97bee3d25ee7b7ce02a39b93a9b9e63641a686186545dc615
    role: context
  - path: pages/traits/physiology/carboxydotrophic.html
    sha256: d395d046a7e53b1a85bde79f6bfeb9d7fc8b4f1e0d028f832c409843e9469903
    role: context
  - path: pages/traits/physiology/carboxylesterase_activity.html
    sha256: b167a9bf309f0528bac0faadb766d8a16549e62fcc3569706f9d18fe1f2fdb59
    role: context
  - path: pages/traits/physiology/caseinase_activity.html
    sha256: 7f4807cdd69040447b2a58dcde002cc90f38223f650df3e29a6a351184c3e9e4
    role: context
  - path: pages/traits/physiology/catalase_activity.html
    sha256: 4a8655df29122198735902cff65a8877a887b700b565356425b743aa3e491d93
    role: context
  - path: pages/traits/physiology/cellular_buoyancy.html
    sha256: 8c923ab99999cb1b70403af4cbd5a874c137d50748ecd339b2b0a9285723c56d
    role: context
  - path: pages/traits/physiology/cellular_rejuvenation.html
    sha256: 99a81b8e7491028644a3b36e5f184cb9dd0e7f6962cc37d12db07676b8404329
    role: context
  - path: pages/traits/physiology/chemoautolithotrophic.html
    sha256: f259873de1471f6b7da18671bdb84010f2a57d4dde355be5e0e9ccd831ffaddf
    role: context
  - path: pages/traits/physiology/chemoautotrophic.html
    sha256: c4e2102a79e3127d16c204e0565f66040fa6724337fac08ce9bab944fbe65494
    role: context
  - path: pages/traits/physiology/chemoheterotrophic.html
    sha256: 59f120c48c1a5e02b61e472fb629861fcd41005c6e39b3507036bd72a38ec58e
    role: context
  - path: pages/traits/physiology/chemokinesis.html
    sha256: acb64edb1fdccd27b0a244a9b638c116b1bb49d8f20796e8a2c757f7ba0dc11a
    role: context
  - path: pages/traits/physiology/chemolithoautotrophic.html
    sha256: 75837d07e6589e3ade71ceb05c7d91ddcd47a86603c39f6320d4c85d1ad08d18
    role: context
  - path: pages/traits/physiology/chemolithoheterotrophic.html
    sha256: eee07003408a6846d7f1f5c54d27efed2834eeec17532f69255ebcc66c428a60
    role: context
  - path: pages/traits/physiology/chemolithotrophic.html
    sha256: 23f238692c12c0e883304488d9b1cb0e11b5cad9d01ebd288a42ca7b296d33f5
    role: context
  - path: pages/traits/physiology/chemoorganoheterotrophic.html
    sha256: 2cb47793a73e822f9c0a8b49a3ab4b826fb41b35f11002f3bb19041cb61ba20f
    role: context
  - path: pages/traits/physiology/chemoorganotrophic.html
    sha256: fa738fc8aefb5603b85441a47e99ac1dd958eed5bbaf24adaddeded351baf101
    role: context
  - path: pages/traits/physiology/chemotaxis.html
    sha256: 2e861806123e1d4bb1d45a4eff9ab319051d73dfd077e5a845f5c2cc79bd7b2a
    role: context
  - path: pages/traits/physiology/chemotrophic.html
    sha256: 3052487dbdc338434a1d6b768407e2c38a33c08ab4b23224cd815b4531aaa8b3
    role: context
  - path: pages/traits/physiology/chemotropism.html
    sha256: 6b26ad07205d68b3c4f5eaef29f4899e4b484ec9f122a73f920556a974327805
    role: context
  - path: pages/traits/physiology/coagulase_activity.html
    sha256: 71305bda0f1e8be07b83eeffe5468644f49a0a769ae4e77a92d6f230a9ac963e
    role: context
  - path: pages/traits/physiology/coccolith_production.html
    sha256: 9caaf482fdd8c656f92f92e368cea1d3cecb19fea421c25c860255ff21fbf021
    role: context
  - path: pages/traits/physiology/cold_shock_response.html
    sha256: f3ba93ed78c9dbab329864ee9a27592bdcadfdd5ee6f7784117894b24c9cc749
    role: context
  - path: pages/traits/physiology/contact_dependent_outer_membrane_exchange.html
    sha256: d7157293c75a11d7e0600a029f78366f7a018eb0b1d1e0b9a918999803a1b103
    role: context
  - path: pages/traits/physiology/copiotrophic.html
    sha256: 43110f35cf3dbb368affed45f915c08c1213d9cf180218e5cdf5564ce75b1a58
    role: context
  - path: pages/traits/physiology/cue_triggered_environmental_anticipation.html
    sha256: aed6facc0d00c118adb1a314b427d0fe65dcae7004e980dc0a642171ed0616e8
    role: context
  - path: pages/traits/physiology/cystine_arylamidase_activity.html
    sha256: 92e50cbd5bb9a60a49f5d830966b82412bd5eddbb525dd7b223b43fae8219bba
    role: context
  - path: pages/traits/physiology/cytogamy.html
    sha256: cba7acd496c523d4a97c8196da0bd1dd817b61456206797d4a40138fed96eaea
    role: context
  - path: pages/traits/physiology/diatom_frustule_production.html
    sha256: cdda322aeaee03167ba45bd3ba1ab03a12ede715794b0f0d05b7f0e829fb0ff3
    role: context
  - path: pages/traits/physiology/diatom_perizonium_production.html
    sha256: c0dbcbe32c66445bfda5442a6135ebd7aff01cc0226f0ca582f433bfc4e049f8
    role: context
  - path: pages/traits/physiology/diatom_seta_production.html
    sha256: d762a4a63600ad1d3cf1ec503f41887a2e8b668ea57f6d5a9f111bae4fe7d922
    role: context
  - path: pages/traits/physiology/diauxic_growth.html
    sha256: 97b9c20fdbe93fab41da9dd7c6ea2ed6e498098c19f7a0c82c7ef5da762afa8f
    role: context
  - path: pages/traits/physiology/diversifying_bet_hedging.html
    sha256: e2a332f73bc73c0444c1c1fac9080d96f88a28f7248da8c201171e7d3ab4b418
    role: context
  - path: pages/traits/physiology/dnase_activity.html
    sha256: 35e4f7d9f070dee3b60eeb946157da2ade8055327c3db617f83b3b986a40af18
    role: context
  - path: pages/traits/physiology/dormancy.html
    sha256: 902b8ebef5227bba99a55d39b6b1f8bac123a9cb57c54b2a8d31b09a18827e67
    role: context
  - path: pages/traits/physiology/durotaxis.html
    sha256: 37229e0f811356dfd2a7dac81228206efaecc1c4568f022463220147d93fdd30
    role: context
  - path: pages/traits/physiology/endocytosis.html
    sha256: 9a96fdbec25dcbcc7c6b577142f3f85afe6a74f8976d4a505b559373df772c7b
    role: context
  - path: pages/traits/physiology/energy_taxis.html
    sha256: c3ee13506fa30599233ab18921713daa53bae39d2eb37526446de0fc6c2ca90f
    role: context
  - path: pages/traits/physiology/enhanced_transcriptional_reactivation_memory.html
    sha256: 787fc7f562373dabff635392874f2c238755ffd930eebccc555a03821245918f
    role: context
  - path: pages/traits/physiology/er_phagy.html
    sha256: 2789afedbc310b4630d1d3063b5bcf233a2435f21d8aabb05a7d998b0402c1a5
    role: context
  - path: pages/traits/physiology/exocytosis.html
    sha256: 67e2b5f1aee00d3fecc9e57e3fee780a9a5d0bd57f6101589f87fc237c607fac
    role: context
  - path: pages/traits/physiology/extracellular_membrane_vesicle_production.html
    sha256: 5de066c552c84bd7b47c387b86d4e74ddaba81aac6a32e8b35c80f3529c42266
    role: context
  - path: pages/traits/physiology/extracellular_trail_based_spatial_memory.html
    sha256: 691e42ae78fee0eacf889a1121a287af87965aae4a71b83a3aec53b03459b569
    role: context
  - path: pages/traits/physiology/galvanotaxis.html
    sha256: 704181f8286b6df33d336a33bb4052a9bfd7409b27a32e7aa779ae3a43164e7b
    role: context
  - path: pages/traits/physiology/galvanotropism.html
    sha256: f78f7b3430748f5790900d831142e0d1fcdc59d132beb42dc6c565f4023408ab
    role: context
  - path: pages/traits/physiology/gamma_glutamyltransferase_activity.html
    sha256: e04966f8f37619cfc5059d7be7ca1052901e7760bd31515b47abada359a6139c
    role: context
  - path: pages/traits/physiology/gelatinase_activity.html
    sha256: 8e920d30c3e54ff1ea4e1ec9b5e1fb990591cb0d9f503fe3e8b37d9fc94394f5
    role: context
  - path: pages/traits/physiology/glutamyl_glutamic_acid_arylamidase_activity.html
    sha256: e308d4bcaff9f1e8055f0e26d447cf4e58c16b65b8493eac7895d912031febe4
    role: context
  - path: pages/traits/physiology/glycine_arylamidase_activity.html
    sha256: afe8cd7b1f1f53622929eff28ef53478bb598396149ce6b730440cc26498d607
    role: context
  - path: pages/traits/physiology/gravikinesis.html
    sha256: 668061c702e8c18604e7b6e3fa268061ba71c046a3fb5639ebfa6ec271380dbc
    role: context
  - path: pages/traits/physiology/gravitaxis.html
    sha256: e7d6f68754c92e514ee861f117371611e8d9e3b2339d55cc4bbf878c477781b0
    role: context
  - path: pages/traits/physiology/gravitropism.html
    sha256: 1398bb33883366ac5eb816af8e4c85da2d3dc6b63328be2de65098b554a5f3da
    role: context
  - path: pages/traits/physiology/gyrotaxis.html
    sha256: cb4e5c61e9eb2557d8f4f4a1ee0e76abbbc389f7ab2532ebbbbc20cc1c2e2d9c
    role: context
  - path: pages/traits/physiology/haptocyst_discharge.html
    sha256: c43c84625bf9f252cfb77afa7b172666b3ce61bd0225449ef3b5942ac1a1dc8d
    role: context
  - path: pages/traits/physiology/heat_shock_response.html
    sha256: e5281277b73d0f755ec9b92be79493062631fd602ba33e5e35632ddf512f09a3
    role: context
  - path: pages/traits/physiology/heterokaryon_incompatibility.html
    sha256: 00c5e26456d6d16bdbe4f7dd949d62d6c5d9511c142c06856bf38dea1e82bad7
    role: context
  - path: pages/traits/physiology/heterothallism.html
    sha256: 2197cd31dc468aa4eeb36c0de44617c55e60355f84b5fbaf36024da464ca3349
    role: context
  - path: pages/traits/physiology/heterotrophic.html
    sha256: bbbcf0ec22cac4f9690940d1adee131e80d62b3993a93a206c57dede5503aaec
    role: context
  - path: pages/traits/physiology/histidine_arylamidase_activity.html
    sha256: 6e3c6c3757d7d55c1fd2a96b63466ae8693733ec58ec8ea1cd9487741237660f
    role: context
  - path: pages/traits/physiology/homeoviscous_adaptation.html
    sha256: fe80c671a39a800cd86248161372ae292701119aaa05d929ba6b55b075e4ee7d
    role: context
  - path: pages/traits/physiology/homothallism.html
    sha256: 6e37e7df0a4dcde530d4aaa0e9b33aa0914c27f7e42b3c72b22298c1ce518470
    role: context
  - path: pages/traits/physiology/hydrogenotrophic.html
    sha256: d3d3c243757fe16eb8c3d44a63d41c31a3d434780b51c7a7d2ea5c9015ded17b
    role: context
  - path: pages/traits/physiology/hyphal_anastomosis.html
    sha256: bb4f1f1f037c2cb23b9d0154952c44d40720b0f1c520f7b5f90ca055cd765675
    role: context
  - path: pages/traits/physiology/isogamy.html
    sha256: b9bcecdff1948415ffd3a9035c674ed538ac573457183335e14db564f7d65803
    role: context
  - path: pages/traits/physiology/karyoklepty.html
    sha256: d6ef456caee14b29bb3106ca89a171e94f8d15ac5f1cb87874a6f1cc1dd10d2a
    role: context
  - path: pages/traits/physiology/kinetocyst_discharge.html
    sha256: 4288d28dffce5be1a749074150c79f2146a64d4b6fa1e341dc4b7a2ae38eab45
    role: context
  - path: pages/traits/physiology/kleptoplasty.html
    sha256: 187dbbced2d2039d190e9e21759ac54baceab65a93073e2bcdc2be9dea0eb6fd
    role: context
  - path: pages/traits/physiology/lecithinase_activity.html
    sha256: 7868ceb3c4a9a004ecee3e2946db9a1520a6c5b3bb5b676ed84bb1adc34b2bed
    role: context
  - path: pages/traits/physiology/lethal_algicidal_activity.html
    sha256: 9c2faa6871aa2c6a35c585b11d1708e07498d1d442416481ed9a163d0f880a43
    role: context
  - path: pages/traits/physiology/lethal_nematicidal_activity.html
    sha256: 8e8ea804923d3821af41b0b1dd3051c3779275bf36b93c4bcd0d69bca77db90c
    role: context
  - path: pages/traits/physiology/leucine_arylamidase_activity.html
    sha256: 1298cc8077bd18021d8b99c94863ed3ff0c0b8a39959bfdbccb7398e6ed0928a
    role: context
  - path: pages/traits/physiology/leucyl_glycine_arylamidase_activity.html
    sha256: 8cdccb746da7f1065bab4e8c7e70ccb15e26ace2c07173f03066b1782c25c08a
    role: context
  - path: pages/traits/physiology/lipase_activity.html
    sha256: e3e63373c981d82278dee53a4917bd35ed9d5e7b81640559bb502635913fe946
    role: context
  - path: pages/traits/physiology/lipophagy.html
    sha256: 442246d0b90be1fc08e5fd032ca6d478b70dccfbcf47c06e1df262aa4a3d2cf5
    role: context
  - path: pages/traits/physiology/lithoautotrophic.html
    sha256: df8eaca3570e46b6ca4759e66e798fb17463ef55e89bb292cd7cb204ac234c4a
    role: context
  - path: pages/traits/physiology/lithoheterotrophic.html
    sha256: 2c6d8cc6a0ec2d8fc86c94af8be3aae1177e54b5e70ff046df9d9666fa43b8fc
    role: context
  - path: pages/traits/physiology/lithotrophic.html
    sha256: 6aa378161b850ed3901617a811322226adac21503200ffc4b9dd25d936c3458b
    role: context
  - path: pages/traits/physiology/lysine_decarboxylase_activity.html
    sha256: 8cd1ae1a750f642474ca1a65c6d40f6523b78d5350ad0cbec4fd1f9a3aa01d05
    role: context
  - path: pages/traits/physiology/macropinocytosis.html
    sha256: 4c8167ea2a7435634fe2b7fd380f89b4297493cf4534d612ff6566741d218b1f
    role: context
  - path: pages/traits/physiology/magnetotaxis.html
    sha256: b06a45cdd31dcd19f2d1ffab5a78c971a650085826df905c7e0462749bc0cd31
    role: context
  - path: pages/traits/physiology/mating_type_switching.html
    sha256: 7f2e8cd5520f9808035737ff17ffefc1bdae3ca0b75864aaa068b269e06f468a
    role: context
  - path: pages/traits/physiology/methanotrophic.html
    sha256: a8c8d2c495594cac50c477b887053d698513ebf6d06419ad28efbc756a1cd602
    role: context
  - path: pages/traits/physiology/methylotrophic.html
    sha256: 00ea875db266a75274a4b03b491b8f4caf2016260c94ee677bdd9e8ef8fc9079
    role: context
  - path: pages/traits/physiology/mitophagy.html
    sha256: e27573adbe4f49e58e209394f9d922426d3df6e6926bbec1e42a2290af503c3e
    role: context
  - path: pages/traits/physiology/mixotrophic.html
    sha256: ae72972c7ef02ae463c1484a2719faf91339131e8d1db5558040571beedd572d
    role: context
  - path: pages/traits/physiology/mucocyst_discharge.html
    sha256: 3c57699778e9632d81112357d7dae4b63f3690ed0ee739968cc2f278dee70dba
    role: context
  - path: pages/traits/physiology/myzocytosis.html
    sha256: cc0ad7de6be6568699bf4ad24b34d20e480dbf9d2f98f619e1d92b56aa582e2a
    role: context
  - path: pages/traits/physiology/nad_dependent_alcohol_dehydrogenase_activity.html
    sha256: 971b32ee8da461309c74174be24aff4ace2b20635d59ecdb762967ae2034c301
    role: context
  - path: pages/traits/physiology/naphthol_as_bi_phosphohydrolase_activity.html
    sha256: 3064d444790aa3668c5e88d0e72a2b9def4677e73961cccc59a4ce0fb42ef02a
    role: context
  - path: pages/traits/physiology/natural_competence.html
    sha256: 51761dd61b60012744ae6823615eb998f48c46d060c00488e2a0d20eaf4dff8b
    role: context
  - path: pages/traits/physiology/negative_autotropism.html
    sha256: 5caf908e4c8ba632118be6d42aaff3e27a287a5a4bf8f76fad3eec8bf64e0451
    role: context
  - path: pages/traits/physiology/nematode_attracting_activity.html
    sha256: 758daa8afbbd74ef175e1ab8de178888e9e09e46aecd08dcc4f4943813927824
    role: context
  - path: pages/traits/physiology/nucleophagy.html
    sha256: 0cac0b612148008ded1d282413d6f8b473fd04b86800125c084ac1238e783cba
    role: context
  - path: pages/traits/physiology/nutrient_adaptation.html
    sha256: c2ca99475378e958a51d5316018d16915b84913a9e7b099f754f689216107684
    role: context
  - path: pages/traits/physiology/oligotrophic.html
    sha256: 7d7c5caf8f8f7e5f2e4b04b5f352b6364ee11bef8e646370180c46e2be67134b
    role: context
  - path: pages/traits/physiology/oogamy.html
    sha256: 99bbaf82fe3a0bd0e6c52bfa808fe7dcbcaca546530177bf493cb7b23c85175f
    role: context
  - path: pages/traits/physiology/organoheterotrophic.html
    sha256: 8cd4a7e65853fb43bbea23eba6534d39c6c50f9dac78254cffb1945097381b58
    role: context
  - path: pages/traits/physiology/organotrophic.html
    sha256: f8e5c72678cf6594c52644ad0549ccbfc032d91710d9ddc9cd2fcc8ac90ad1b1
    role: context
  - path: pages/traits/physiology/ornithine_decarboxylase_activity.html
    sha256: 8251101a7c1aba3b41aed9d7e302ce428957ade8c07419f242e4d46870aa962b
    role: context
  - path: pages/traits/physiology/osmotaxis.html
    sha256: 528bde21751816809c3f1cf4aabf3a217a170dfcaedd3fa0f5eafa63e3589c7a
    role: context
  - path: pages/traits/physiology/oxidase_activity.html
    sha256: 098eab939cffaefc3d752408888c3b70dfa772d6085fce04cf0fcf5cb9506de1
    role: context
  - path: pages/traits/physiology/oxidative_stress_response.html
    sha256: 33dcaf6fda175efe61eec66a8c0177cef6d30ad0e5797d236cf5c4551a793a07
    role: context
  - path: pages/traits/physiology/paedogamy.html
    sha256: 5b88729288f6524371dcadbce98522eeeb9146605c7e4f2c88b7d742ced7a354
    role: context
  - path: pages/traits/physiology/pallium_feeding.html
    sha256: 0e35e6e4fd6251c3db34cfeabc60e543957abef3ca6afa9cbaed3667bf5718da
    role: context
  - path: pages/traits/physiology/parasexuality.html
    sha256: 11848850cc593f47b94f31640ed7cc0ed1eae591f12a807462fe157d104c9512
    role: context
  - path: pages/traits/physiology/persister_cell_formation.html
    sha256: aafb42ab2c7f578edb779a7b065dd78ecc2c5e2ab92a1cd1b35c78c4e9a48ffe
    role: context
  - path: pages/traits/physiology/pexophagy.html
    sha256: ec54427753a9ea336cab04d51e6f07ba250b90044baeaa1642ba8353caf802dc
    role: context
  - path: pages/traits/physiology/ph_taxis.html
    sha256: 78479b3d4c2ec7d7cd917038de5ad58cbe38af1f9389c5af7f12ef8b15bcaea3
    role: context
  - path: pages/traits/physiology/ph_tropism.html
    sha256: caccda9fd2546c08dcaa4229fb66b2ae924d4aa5555abd702c0bfde241eb7c65
    role: context
  - path: pages/traits/physiology/phagocytosis.html
    sha256: 7370202144393f1fbb2d0822dc810ec2244acfee978abe2dfabeb456cf4aaeee
    role: context
  - path: pages/traits/physiology/phagotrophy.html
    sha256: fa521f542738cb806f34cf5414539c1c564cfc9b036cbdff250cc33c82fed148
    role: context
  - path: pages/traits/physiology/phenylalanine_arylamidase_activity.html
    sha256: 3a8febbc0c798a463d2d370b6154f9d261d5906de451ec7f0ca1be02aa3c4f1b
    role: context
  - path: pages/traits/physiology/photoautotrophic.html
    sha256: 06c4493974fdb8f5b8d4b28396d84e49f8c5c4f6e28f29d2bdf457098361d41a
    role: context
  - path: pages/traits/physiology/photoheterotrophic.html
    sha256: a14f3473de3142e0395113f6898348f82fd67d3478ca35dbc3f6a659aa64fb28
    role: context
  - path: pages/traits/physiology/photokinesis.html
    sha256: f02f8a3a05248c39471f8ab578b5760faddbff2f5a00eb538a2b7cb8fc0effa9
    role: context
  - path: pages/traits/physiology/photolithoautotrophic.html
    sha256: f6025bd3a992b9a41495b5630fc692c5c4d40ae6631f7bb3de83bd1eeb8c8bf9
    role: context
  - path: pages/traits/physiology/photolithotrophic.html
    sha256: 75d790adcfedb2adaff54a2af40e5f64f9002a00543cbb327cd3e965637f1183
    role: context
  - path: pages/traits/physiology/photoorganoheterotrophic.html
    sha256: b051c762147fecac395a9c6183df69646928bdc1cc4d9bcd79838cf5fb7fe018
    role: context
  - path: pages/traits/physiology/phototaxis.html
    sha256: 9c7cde17ada0807739c9d5f7514ec0ce8684805dbd0e1af9036b563ad324be29
    role: context
  - path: pages/traits/physiology/phototrophic.html
    sha256: 9307b849fe0f4dc688f5b8b12e2eface50ed73d9e7cde5db65637c4189334679
    role: context
  - path: pages/traits/physiology/phototropism.html
    sha256: 7ac0683a23df04bbea2a1c0fd902b663e4be3052311c951cf72116b5022c1daa
    role: context
  - path: pages/traits/physiology/pinocytosis.html
    sha256: 317c6000372d266599965b8b3f06e9c2d5301249c147e6db45b4de3c01e964c8
    role: context
  - path: pages/traits/physiology/positive_autotropism.html
    sha256: d8443a0b1b8dda8f0e9118cdc686d38e1ac1df8d36a87ddded52b43176da1af2
    role: context
  - path: pages/traits/physiology/primary_homothallism.html
    sha256: c672ffba2b2492bd09e435f5cf4968a4d01a40749cc4075866857b67804f2aea
    role: context
  - path: pages/traits/physiology/prolyl_aminopeptidase_activity.html
    sha256: 884efe96f5172205f8b721544975561bccd0665ae65ebeec74681b7b09a55f06
    role: context
  - path: pages/traits/physiology/proteaphagy.html
    sha256: 73511ab8035fdae442d6cf0794e71777424639878c1a6a66139879c2a62db604
    role: context
  - path: pages/traits/physiology/pseudobipolar_mating_system.html
    sha256: 3dca427c9faada6bdd0d56dc9e6c70052c2afb438bd0dc1ad9b7309ea02a6bee
    role: context
  - path: pages/traits/physiology/pseudohomothallism.html
    sha256: 299861be45017a2b6b389e54972d93610c6f7e5c7019847d14d3021bc1298409
    role: context
  - path: pages/traits/physiology/pyrazinamidase_activity.html
    sha256: 454656ad948c26d0791b7e3ba37cf05c008bd571c451691a0207cd202715fac1
    role: context
  - path: pages/traits/physiology/pyrrolidonyl_arylamidase_activity.html
    sha256: 2b5104662c480ef7549e90e9fd08e631b10ce9ee16a383e41a1c80fe58b0f59a
    role: context
  - path: pages/traits/physiology/quorum_quenching.html
    sha256: 634df1c5700347f18873125799890576a90df9551cbb87b3ea55ebf511d5124d
    role: context
  - path: pages/traits/physiology/quorum_sensing.html
    sha256: aa457ce068ba4a2968d18c69e9da655582b6ddc03035430d6c4a1f2f31e88f32
    role: context
  - path: pages/traits/physiology/rapid_axopodial_contraction.html
    sha256: 338e38bacabc51d78c43d115a5e426dc9d7a3bc0a6839ff03fdf8170cf07f273
    role: context
  - path: pages/traits/physiology/replicative_aging.html
    sha256: 6231f50f32cab4e4227a79992134e37876e8ab229e8e12dd5b28357b3333f51c
    role: context
  - path: pages/traits/physiology/reversible_nematode_paralyzing_activity.html
    sha256: 068f323962b878a9e15cffc04866b581e378b7dea3c2d9793d176f72f854b8eb
    role: context
  - path: pages/traits/physiology/rheotaxis.html
    sha256: 8a753f12ffd727f3e2d8636c453f88d25332171765f4a85cda602acdd54c8de9
    role: context
  - path: pages/traits/physiology/rheotropism.html
    sha256: 2b4537b5a7eedf0dc4c211a84abf00a2c00d37c1bf0cd6d9b65472051bc62418
    role: context
  - path: pages/traits/physiology/ribophagy.html
    sha256: af57e7152f34b626d24b755243de69c8e252cba05eba2bfa4de371c93d3fa367
    role: context
  - path: pages/traits/physiology/serine_arylamidase_activity.html
    sha256: cbb2b627fcb4f057416e9c3829da2cd73b35e7cc2620f2bfbae0e0e6f63d1f4a
    role: context
  - path: pages/traits/physiology/siderophore_production.html
    sha256: eff94679434d616c1904760bed6a0b2234f6143295440eaf518e315940ed6d18
    role: context
  - path: pages/traits/physiology/siliceous_scale_production.html
    sha256: 33f60c95e1eb0ed8ddb1f13e01056a2aaf96795c5261e15cb89c91a4285ab1cf
    role: context
  - path: pages/traits/physiology/sos_response.html
    sha256: d2bbb5d098add1700f564d90d25408c771afa3ff0fd4bdfe93ba73d1eae264c9
    role: context
  - path: pages/traits/physiology/spore_germination.html
    sha256: 73d23ba5eb18a4726af65ab96cd673d60c46715c2051bd7d9e9816ebe933b89e
    role: context
  - path: pages/traits/physiology/stress_response.html
    sha256: 5bef81be3ffb90eb1c6603a1ece4a892451fd9ba94ade8fa0aa90d1730f42e9d
    role: context
  - path: pages/traits/physiology/tetrapolar_mating_system.html
    sha256: 21942a7029c803a4af25e70f930d9d6e2af519ee41d511ca494fc7ca01934dd3
    role: context
  - path: pages/traits/physiology/thermotaxis.html
    sha256: dfa045d55a051a17cc4985fda1a6df857bc09c16e55a63ddb62e64b942f3e448
    role: context
  - path: pages/traits/physiology/thigmotropism.html
    sha256: e6f9e9fc98c7244d163f379ef00820f90b2fdb6a3d09c8c1e75d02d200bf91bd
    role: context
  - path: pages/traits/physiology/toxicyst_discharge.html
    sha256: 3fe247cf00153c5296fe776ff9b60a49b09d34e043efe3f70ca11ef1a2849010
    role: context
  - path: pages/traits/physiology/trichocyst_discharge.html
    sha256: 72bea2d10e83df3b3c4f42d07fffb6a6f73a27ee2a4c8b421a6a61574bab86bb
    role: context
  - path: pages/traits/physiology/tripolar_mating_system.html
    sha256: 64e714e2d342792f192349975ba1679c97dd78e6f73e4e718b5d9479715aea73
    role: context
  - path: pages/traits/physiology/trogocytosis.html
    sha256: 1bdc64575a86a16c60887c2bdd08efd324d2dfda6b08e28bcde2cec3a7211321
    role: context
  - path: pages/traits/physiology/trophic_type.html
    sha256: 2ed8f158674cf77f7b34e97cb00a18981412d4bca250dac6f12f7cf57fe31212
    role: context
  - path: pages/traits/physiology/trypsin_activity.html
    sha256: 155d006020815c887ebb03c42e05fcd8f290eede5a1ddb27c4d504153b759119
    role: context
  - path: pages/traits/physiology/tyrosine_arylamidase_activity.html
    sha256: eaeeb39a0d3153a3efb86a4cc3ddb420e8fe5bcb446754827b7e4e331b3832c3
    role: context
  - path: pages/traits/physiology/unconventional_protein_secretion.html
    sha256: b1d089f35eb93bd0e72edf798b6d5b0daeabbf8f47e274b3f2aea2cbd91f73fe
    role: context
  - path: pages/traits/physiology/unequal_protein_aggregate_inheritance.html
    sha256: 2755e9557a6dcabefe2647172851bc4f4e67c674065237239b884eefb2ffb302
    role: context
  - path: pages/traits/physiology/unisexual_reproduction.html
    sha256: 1f395b649f298c5c85500578bcf1ba6eda5f2a0e7da12ddaec0cbcbed33a879a
    role: context
  - path: pages/traits/physiology/urease_activity.html
    sha256: c10efa99aa3b554ff0e595bca232a086483d996322726b68a4f2c059d4e51c05
    role: context
  - path: pages/traits/physiology/valine_arylamidase_activity.html
    sha256: 2de336ac4c09cf9e8c353b53cc7e2a3958d6e02f1dec4ac58eb83efc4e931454
    role: context
  - path: pages/traits/physiology/viable_but_nonculturable_state.html
    sha256: 6007124562f0b726333150e405d78c23f862979f41baec155aff27b9ec478201
    role: context
  - path: pages/traits/physiology/viscotaxis.html
    sha256: db11934cc0cf3a8fbd5c4677fa5220f225b5eb1a689035199dbfc7f5a0004d98
    role: context
  - path: pages/traits/quantitative_property/has_maximum_observed_value.html
    sha256: d092b12c866b16abd89fc0cf1441172ccd1926122f191710fcbfaee7be65c0bd
    role: context
  - path: pages/traits/quantitative_property/has_minimum_observed_value.html
    sha256: 86429527d06e39b39b46c2ebfd3ffdc470f9c1de26a4d5ebc43b3634a435a49e
    role: context
  - path: pages/traits/quantitative_property/has_observed_spot_value.html
    sha256: 3350502c5d1046ba3ca50c36b41a49d40a247d7028505fdd955c2c5bfa6c56c2
    role: context
  - path: pages/traits/quantitative_property/has_value.html
    sha256: 63de072a446272498bb289082352fad3019a6e79e2a5a9715ff4cfddfcbfa65b
    role: context
  - path: pages/traits/quantitative_property/has_value_comments.html
    sha256: 4037ae1eb5bb8107a850d48418a6447f84978d3f1f7894b6a9185e2b2ebb5af0
    role: context
  - path: pages/traits/quantitative_property/is_negative_data.html
    sha256: dcf9f15283d7725004a90a7d8e5bdee92dc122d35f17cbb2ebf4028273ef2dad
    role: context
  - path: pages/traits/quantitative_property/observation_data_property.html
    sha256: cfca507320c08e477b0de976e810c944e3821e5bd9b3c2802b364244442e7eb9
    role: context
  - path: pages/traits/upper/biological_process.html
    sha256: 23e29f4baf0cf5f4bc1cc4e56f7cb0ff73eb6def82a40ddccdb6239dac793d51
    role: context
  - path: pages/traits/upper/chemical_entity.html
    sha256: 35b8b21b3dfd761f01b6da081161f1def58bed68b0396441ae0d2bb913b9b0bf
    role: context
  - path: pages/traits/upper/enzyme.html
    sha256: f5d26b44ecf70f13c001e95a84463fee23f6fb8eb7824e6328fefca616c8304f
    role: context
  - path: pages/traits/upper/material_entity.html
    sha256: b1cb889e4fe9ae3e4ac1d7c1deb04fd3a1e3db14ab6455ad9c1026fa139c05db
    role: context
  - path: pages/traits/upper/microbe.html
    sha256: 580ffe6aee9ba56abcf5a9371d59c0f528a6058a1ab6b5e1bcb775c955ad957e
    role: context
  - path: pages/traits/upper/observation.html
    sha256: fda624236c4e3eca54b4ad6d98ae9a68eefc781f877f1c1e8305ac6fd68a7ba4
    role: context
  - path: pages/traits/upper/phenotype.html
    sha256: 9a8f4cf081a2dd1f7a5fffce8f5c44d1077b0ee9e13608698b0c1e0e8d183a4c
    role: context
  - path: pages/traits/upper/quality.html
    sha256: 5b83da619b836ad2688b5dc0ffbf8959a180d99c074ff9c550ab79f2aa4c781c
    role: context
  - path: pages/umap.html
    sha256: 8d76edfd5cb73c4751387fd48c9a7d8f275e8fb16212b6b66403131ba9456085
    role: context
  - path: proposals/metpo_traitmech_v598/metpo_proposal_classes_robot.tsv
    sha256: fddb48be0dc3332068601d1c5354dc117e33bddf33faf6dac766084b50a3f7c5
    role: context
  - path: proposals/metpo_traitmech_v598/proposal.md
    sha256: 19c7473186debec52847a658483efda5870047d3270120fa13aaebfdb7169a75
    role: context
  - path: reports/proposal_citation_audit.tsv
    sha256: fe716ce927bca498caffab6e029ee0f8fbf72977576dd85513bbc517d609a720
    role: context
  - path: reports/robot/metpo_traitmech_v598/classes.owl
    sha256: adf51e80306789cbabe2d287b477cc3b3d91555fabe219e2e1e497f6928f35f6
    role: context
  - path: reports/robot/metpo_traitmech_v598/merged.owl
    sha256: 7fc0548adc677fdd1cb555fdb9aec1f4efc33afefd027d836d31fa270ffe2b94
    role: context
  - path: reports/robot/metpo_traitmech_v598/reasoned.owl
    sha256: 925b7efbe0f50677a2aa6a7f7894d3d48ebafd3d4b3a457c50b0a2650e4e240a
    role: context
  - path: research/traits/physiology/reversible_nematode_paralyzing_activity-source-verification.json
    sha256: de073e94fa60e666a9668732a5da275ae64089f585aacdca7ccb3990c3cf2bd6
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/add_reversible_nematode_paralyzing_activity_trait.py
    sha256: 47e34753322adf36973eca5888dc524fd587b611d55a4d2899f8998a4306fc48
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
  - path: tests/test_add_reversible_nematode_paralyzing_activity_trait.py
    sha256: 267c0df4dc59f140e94f0bdd959f3d91d5de9c266b7eb3417a6f1baccb0bd984
    role: context
targets:
- target_id: traitmech:000722
  path: data/traits/physiology/reversible_nematode_paralyzing_activity.yaml
  label: reversible nematode-paralyzing activity
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/physiology/reversible_nematode_paralyzing_activity.yaml
    role: maintained record
  - repository: CultureBotAI/TraitMech
    path: scripts/add_reversible_nematode_paralyzing_activity_trait.py
    role: guarded curation writer
scope:
  description: One complete record addition and its maintained/generated owners, not
    whole-corpus scientific review.
  selection: One exact new trait, without sampling.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - traitmech:000722
  exclusions:
  - target: Other 1116 TraitRecords
    reason: Novelty context, deterministic diagnostics and byte preservation only.
  - target: data/traits/physiology/spore_germination.yaml
    reason: Protected and byte-preserved.
checks:
- check_id: records-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate
    -s src/traitmech/schema/traitmech.yaml --target-class TraitRecord data/traits/physiology/reversible_nematode_paralyzing_activity.yaml
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate
    -s src/traitmech/schema/traitmech.yaml --target-class TraitRecord data/traits/physiology/reversible_nematode_paralyzing_activity.yaml
  status: passed
  required: true
  target_ids:
  - traitmech:000722
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: records-1
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_strict.py data/traits/physiology/reversible_nematode_paralyzing_activity.yaml
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_strict.py data/traits/physiology/reversible_nematode_paralyzing_activity.yaml
  status: passed
  required: true
  target_ids:
  - traitmech:000722
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: records-2
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_history_links.py history/records/reversible_nematode_paralyzing_activity
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_history_links.py history/records/reversible_nematode_paralyzing_activity
  status: passed
  required: true
  target_ids:
  - traitmech:000722
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: records-3
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/verify_snippets.py --record data/traits/physiology/reversible_nematode_paralyzing_activity.yaml
    --out /tmp/traitmech-paralysis-checks-20261014/native-record.tsv
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/verify_snippets.py --record data/traits/physiology/reversible_nematode_paralyzing_activity.yaml
    --out /tmp/traitmech-paralysis-checks-20261014/native-record.tsv
  status: passed
  required: true
  target_ids:
  - traitmech:000722
  exit_code: 0
  expected_exit_code: 0
  summary: The native verifier exited zero but omitted both URL references and emitted
    zero result rows. Neither excerpt is native VERIFIED. Direct HTML/PDF and typeset
    checks are separate evidence.
- check_id: records-4
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q tests/test_add_reversible_nematode_paralyzing_activity_trait.py -k
    'not source_receipt'
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q tests/test_add_reversible_nematode_paralyzing_activity_trait.py -k
    'not source_receipt'
  status: passed
  required: true
  target_ids:
  - traitmech:000722
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: focused-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q tests/test_add_reversible_nematode_paralyzing_activity_trait.py tests/test_readme_artifacts.py
    tests/test_trait_priority.py tests/test_qc_dashboard_artifacts.py
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q tests/test_add_reversible_nematode_paralyzing_activity_trait.py tests/test_readme_artifacts.py
    tests/test_trait_priority.py tests/test_qc_dashboard_artifacts.py
  status: passed
  required: true
  target_ids:
  - traitmech:000722
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: focused-1
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/ruff
    check src scripts tests
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/ruff
    check src scripts tests
  status: passed
  required: true
  target_ids:
  - traitmech:000722
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: generate-0
  name: just audit-proposals
  command: just audit-proposals
  status: passed
  required: true
  target_ids:
  - traitmech:000722
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: generate-1
  name: just ground-predicates
  command: just ground-predicates
  status: passed
  required: true
  target_ids:
  - traitmech:000722
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: generate-2
  name: just ground-nodes
  command: just ground-nodes
  status: passed
  required: true
  target_ids:
  - traitmech:000722
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: generate-3
  name: just audit-graphs
  command: just audit-graphs
  status: passed
  required: true
  target_ids:
  - traitmech:000722
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: generate-4
  name: just audit-graph-protein-taxa
  command: just audit-graph-protein-taxa
  status: passed
  required: true
  target_ids:
  - traitmech:000722
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: generate-5
  name: just audit-predicate-domains
  command: just audit-predicate-domains
  status: passed
  required: true
  target_ids:
  - traitmech:000722
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: generate-6
  name: just check-biolink-coverage
  command: just check-biolink-coverage
  status: passed
  required: true
  target_ids:
  - traitmech:000722
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: generate-7
  name: just audit-snippets
  command: just audit-snippets
  status: passed
  required: true
  target_ids:
  - traitmech:000722
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: generate-8
  name: just gen-discussions-data
  command: just gen-discussions-data
  status: passed
  required: true
  target_ids:
  - traitmech:000722
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: generate-9
  name: just gen-qc-dashboard
  command: just gen-qc-dashboard
  status: passed
  required: true
  target_ids:
  - traitmech:000722
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: generate-10
  name: just gen-pages
  command: just gen-pages
  status: passed
  required: true
  target_ids:
  - traitmech:000722
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: generate-11
  name: just gen-priority-dashboard
  command: just gen-priority-dashboard
  status: passed
  required: true
  target_ids:
  - traitmech:000722
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: verify-0
  name: just qc
  command: just qc
  status: passed
  required: true
  target_ids:
  - traitmech:000722
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: verify-1
  name: just validate-history
  command: just validate-history
  status: passed
  required: true
  target_ids:
  - traitmech:000722
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: verify-2
  name: just validate-products
  command: just validate-products
  status: passed
  required: true
  target_ids:
  - traitmech:000722
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: verify-3
  name: just verify-proposal metpo_traitmech_v598
  command: just verify-proposal metpo_traitmech_v598
  status: passed
  required: true
  target_ids:
  - traitmech:000722
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: verify-4
  name: just robot-validate-proposal metpo_traitmech_v598
  command: just robot-validate-proposal metpo_traitmech_v598
  status: passed
  required: true
  target_ids:
  - traitmech:000722
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: verify-5
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/audit_canonical_examples.py --no-resolve
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/audit_canonical_examples.py --no-resolve
  status: passed
  required: true
  target_ids:
  - traitmech:000722
  exit_code: 0
  expected_exit_code: 0
  summary: Canonical-example shape audit passed with --no-resolve; live NCBI checks
    were not run. The new record has no canonical examples.
- check_id: verify-6
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/run_trait_graph_audit.py --verify
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/run_trait_graph_audit.py --verify
  status: passed
  required: true
  target_ids:
  - traitmech:000722
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: verify-7
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/audit_history_records.py --base f44af60a9d88dcc604543301a8669e1e2bff428d
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/audit_history_records.py --base f44af60a9d88dcc604543301a8669e1e2bff428d
  status: passed
  required: true
  target_ids:
  - traitmech:000722
  exit_code: 0
  expected_exit_code: 0
  summary: Actual maintained command passed. Corpus diagnostics are not whole-corpus
    scientific review.
- check_id: tests-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q --junitxml=/tmp/traitmech-paralysis-checks-20261014/pytest.xml
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q --junitxml=/tmp/traitmech-paralysis-checks-20261014/pytest.xml
  status: passed
  required: true
  target_ids:
  - traitmech:000722
  exit_code: 0
  expected_exit_code: 0
  summary: 4592 tests passed without failures, errors or skips.
- check_id: products
  name: products
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    /tmp/traitmech-paralysis-products-20261014.py
  status: passed
  required: true
  target_ids:
  - traitmech:000722
  exit_code: 0
  expected_exit_code: 0
  summary: All 1116 prior records, protected spore germination, prior history/reviews/proposals/embeddings/templates/baseline
    are byte-preserved. Existing pages are footer-only except the phenotype child
    link. Exact w3id RDF identity, hierarchy and definition citations pass.
- check_id: browser
  name: browser
  command: node /tmp/traitmech-paralysis-browser-20261014.cjs
  status: passed
  required: true
  target_ids:
  - traitmech:000722
  exit_code: 0
  expected_exit_code: 0
  summary: '1440/390 px checks pass: two quotes, two discussions, one history, local
    identifier, hierarchy/browse navigation, dashboard 1117 and coverage image. Eight
    screenshots visually inspected. No horizontal overflow or page errors.'
evidence:
- evidence_id: source-0
  kind: primary_source
  reference: https://journals.flvc.org/nematropica/article/view/64427
  locator: English Abstract, printed page 215; PDF page 1. All rendered pages were
    inspected during source research; quoted page re-inspected during curation. No
    complete raw-data/statistical reanalysis.
  accessed_at: '2026-10-14T01:33:53Z'
  support: supports
  snapshot_sha256: 8ab77f16cf3bbf3974fef3bf5b83a129937c08b2ed5f4a44766a0fedfe278b2a
  summary: The English Abstract explicitly reports fungal-filtrate reversible paralysis.
    Needle-probed immobility at 2 h precedes rinsing and reassessment labelled 21
    h. Results/Table 2, not initial-paralysis Figure 1 alone, support recovery. Bioassay
    2 has no recovery test, bioassay 3 has a high-paralysis control, and bioassay
    5 is null. Strain labels, dose values and timing wording conflict and remain attributed.
    Repeated counts are not individual trajectories.
- evidence_id: source-1
  kind: primary_source
  reference: https://horizon.documentation.ird.fr/exl-doc/pleins_textes/pleins_textes_5/pt5/nemato/27861.pdf
  locator: Results, Study of the reversibility of the toxic effect, printed page 335/PDF
    page 5, upper right column. All rendered pages were inspected during source research;
    quoted page re-inspected during curation. No complete raw-data/statistical reanalysis.
  accessed_at: '2026-10-14T01:33:53Z'
  support: supports
  snapshot_sha256: 8e1fbd264c076bec956f612897a77da84f6a7116736b0430005713fc9c018eec
  summary: Brazilian P. lilacinus filtrate and M. arenaria larvae are identified in
    the surrounding experiment. The Results and actual Figure 3 show recovery after
    24 h in fresh water, following variable exposure to undiluted filtrate from 10-day
    illuminated motionless aerated malt culture. Needle probing and water/pH-matched
    medium controls are described. Summary less-than-48-h and Results through-48-h
    wording differ. The 72-h endpoint is not universal reversibility. Typeset all,
    not extracted dl, is quoted; proposed neurotropic action is not demonstrated.
- evidence_id: content
  kind: record_content
  reference: data/traits/physiology/reversible_nematode_paralyzing_activity.yaml
  locator: Entire record, writer, tests, proposal, sidecar, history and generated
    diff.
  accessed_at: '2026-10-14T01:33:53Z'
  support: supports
  summary: One microbial capability requiring nematode movement loss and recovery
    after exposure ends. Not microbial nonmotility, nematode susceptibility, an assay
    or chemical role. Immobility, reduced speed, reduced hatch, suppression, trapping,
    attraction or killing alone is insufficient. No canonical examples, exact synonyms/xrefs,
    proteins or causal graph.
- evidence_id: ontology
  kind: database
  reference: data/raw/metpo.owl
  locator: Specified pinned/current OWL and TSV inputs and live neighboring records.
  accessed_at: '2026-10-14T01:33:53Z'
  support: supports
  summary: Phenotype METPO:1000059 is broader and lies below quality METPO:1000188.
    Related lethal, feeding, trapping and attracting endpoints are not equivalents
    or necessary parents. No exact active/deprecated counterpart identified in literal
    annotations of three OWL inputs and all cells of six TSV owners. Editor metadata
    is not an inspected import closure.
- evidence_id: novelty
  kind: search
  reference: research/traits/physiology/reversible_nematode_paralyzing_activity-source-verification.json
  locator: Known ignored/hidden current files, retained regular-file Git blobs, pending
    changed blobs and selected upstream owners.
  accessed_at: '2026-10-14T01:33:53Z'
  support: supports
  summary: 'Initial screen: 179 known locations, 176 available, 139 retained heads,
    11 open/draft PRs, 783 pending nonremoved blobs and 587 upstream owner files.
    All 88 matching paths adjudicated. Existing paralysis passages are exclusions/comparators,
    not exact records or unresolved exact nodes. PGPT sequence categories and cached
    literature are leads. The 256 numeric hits are decimal measurements/coordinates;
    572 intervals are broad editor envelopes. The initial Git regex control failed
    and was corrected before completed historical checks.'
  search_scope: Available ignored/hidden files included. No lost historical ignored/untracked
    reconstruction, symlink targets or arbitrary local archive decoding. Pending content
    scope is changed blobs, not entire PR trees. Not atomic allocation.
- evidence_id: provenance
  kind: authority
  reference: research/traits/physiology/reversible_nematode_paralyzing_activity-source-verification.json
  locator: Primary source hashes, direct text/typeset excerpts, metadata and native
    URL omission receipt.
  accessed_at: '2026-10-14T01:33:53Z'
  support: supports
  summary: Kilama is definition authority; Cayrol independently supports recovery,
    not standalone producer identity. The 19/22-word excerpts are typeset-verified,
    but both URL references are skipped by the native DOI/PMID verifier, which emits
    zero rows. Cayrol text extraction is not an exact match. Kilama follow-up web
    fetch returned 403; original directly acquired bytes were rehashed and reread.
    IRD PDF access succeeded. Bounded metadata/notice checks do not establish comprehensive
    clearance or absence of a DOI.
- evidence_id: products
  kind: validation
  reference: reports/proposal_citation_audit.tsv
  locator: Actual checks, generation receipts, parsed RDF, preservation and responsive
    browser tests.
  accessed_at: '2026-10-14T01:33:53Z'
  support: supports
  summary: 'Local gates and full tests pass. Parsed RDF cardinalities: {''classes'':
    15, ''merged'': 12628, ''reasoned'': 12632}. Only Kilama and the local record
    annotate the definition. All 645 pinned CLAW generator blobs match. Neither configured
    embedding input exists; embeddings remain unchanged.'
- evidence_id: history
  kind: record_content
  reference: history/records/reversible_nematode_paralyzing_activity
  locator: Per-record minting and append-only CREATE records.
  accessed_at: '2026-10-14T01:33:53Z'
  support: supports
  summary: Observed acceptance at 01:02:02Z precedes the later 01:05:22Z CREATE. Identity,
    evidence and discussion scope match the change. Codex/GPT-5 and LLM assistance
    are explicit. Status remains PROPOSED.
- evidence_id: publication
  kind: search
  reference: /tmp/traitmech-paralysis-publication-20261014/accepted.json
  locator: Refreshed ignored/hidden local reservation and live remote identity checks.
  accessed_at: '2026-10-14T01:33:53Z'
  support: supports
  snapshot_sha256: f413895507516b4a4dc0971f79cf16c9ccd87b645351f08fb5e3ce615ea17ea6
  summary: 180 known locations rechecked. Owned additions separated from competing
    reservations. Pending heads, titles/bodies, upstream heads and retained history
    identities unchanged; no conflict identified.
  search_scope: Available ignored/hidden files included. No lost historical ignored/untracked
    reconstruction, symlink targets or arbitrary local archive decoding. Pending content
    scope is changed blobs, not entire PR trees. Not atomic allocation.
assessments:
- assessment_id: identity
  area: identity
  topic: Microbial bearer and recovery-defined endpoint
  summary: Fungal-filtrate experiments support a reusable microbial capability. The
    nematode is the affected organism, not the trait bearer. Recovery is mandatory;
    nonmovement alone does not establish the class.
  target_ids:
  - traitmech:000722
  evidence_ids:
  - content
  - source-0
  - source-1
  outcome: supported
- assessment_id: evidence
  area: evidence
  topic: Washout recovery versus initial immobility
  summary: Both primary experiments include post-exposure recovery. Failed or confounded
    assays and boundary differences remain explicit. No universal recovery interval,
    dose, host/stage effect or individual-cell trajectory is asserted.
  target_ids:
  - traitmech:000722
  evidence_ids:
  - source-0
  - source-1
  - content
  outcome: supported
- assessment_id: grounding
  area: grounding
  topic: Conservative parent and non-equivalent neighboring traits
  summary: Phenotype is a broader class. Lethal activity, trapping, feeding and attraction
    have distinct endpoints; a single producer may express different endpoints in
    different conditions. Bounded ignored/hidden and ontology searches support a local
    fallback without claiming global novelty.
  target_ids:
  - traitmech:000722
  evidence_ids:
  - ontology
  - novelty
  - publication
  - content
  outcome: supported
- assessment_id: provenance
  area: provenance
  topic: Citation roles, verbatim fidelity and URL skips
  summary: The selected spans follow the actual source pages. Typeset all is retained
    despite text-layer dl. Native omission is not native VERIFIED. Strain/dose discrepancies
    remain attributed, canonical taxa are omitted, and only definition authority enters
    the ROBOT definition citation.
  target_ids:
  - traitmech:000722
  evidence_ids:
  - provenance
  - source-0
  - source-1
  - products
  outcome: supported
- assessment_id: products
  area: consistency
  topic: Guarded writes, exact RDF and preserved owners
  summary: Dry-run/replay/prevalidation/drift tests pass. Full QC, tests, history,
    proposal and responsive page checks pass. Existing maintained records and immutable
    artifacts are unchanged. The proposal has the exact w3id hierarchy, not a legacy
    stub.
  target_ids:
  - traitmech:000722
  evidence_ids:
  - products
  - history
  - content
  outcome: supported
- assessment_id: limits
  area: completeness
  topic: Unresolved mechanism and source discrepancies
  summary: No common active molecule, neural target, canonical strain, protein mechanism,
    field benefit or environmental safety is established. These gaps are retained
    and do not erase the narrower recovery-supported capability.
  target_ids:
  - traitmech:000722
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
  checks remain separate publication gates unfinished at this timestamp.
- All rendered source pages were inspected during research and recovery/quoted pages
  re-inspected during curation. No complete raw-data or statistical reanalysis was
  performed; exact excerpt fidelity does not independently validate the experiments.
- Recovery, initial paralysis and possible killing depend on assay conditions. No
  universal host/stage response, dose or recovery threshold, causal mechanism, canonical
  taxon, field efficacy or safety claim is made.
- Both URL references are skipped by the native DOI/PMID verifier; zero output rows
  is not source verification. Kilama follow-up web access failed with 403, while original
  direct bytes remained readable. Bounded source/index/notice checks are not comprehensive
  clearance.
- The corpus canonical-example audit used --no-resolve for shape only. No canonical
  example is asserted for the new record.
- Ignored/hidden known copies were included. Unavailable historical ignored/untracked
  files, symlink targets, arbitrary archives and all unchanged pending-tree content
  were not reconstructed. Discovery is not exhausted and allocation is not atomic.
- Configured embedding inputs are absent, so existing embeddings remain unchanged.
  Required trailing empty ROBOT cells use a path-scoped whitespace exception, not
  an unqualified clean-whitespace claim.
tags:
- add-trait
- reversible-nematode-paralyzing-activity
- self-review
```
