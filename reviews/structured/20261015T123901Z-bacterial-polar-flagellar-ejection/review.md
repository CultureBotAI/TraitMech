# Bacterial polar flagellar ejection

- Review: 20261015T123901Z-bacterial-polar-flagellar-ejection
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-15T11:59:43Z
- Finished UTC: 2026-10-15T12:39:01Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The bounded bacterial basal-release phenotype is supported by three primary papers. No actionable defect found in this one-record scope; four scope, ontology, mechanism and provenance discussions remain OPEN and status remains PROPOSED.

## Scope And Provenance

Complete new trait, source evidence, guarded writer/tests, v608 proposal, histories and generated surfaces.

Selection: Exact traitmech:000732 and maintained owners; no sampling.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base d7c11c8a6a66cba9ce10828051e78894d2fa81da.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| traitmech:000732 | data/traits/physiology/bacterial_polar_flagellar_ejection.yaml | maintained | bacterial polar flagellar ejection |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate -s src/traitmech/schema/traitmech.yaml --target-class TraitRecord data/traits/physiology/bacterial_polar_flagellar_ejection.yaml | passed | True | traitmech:000732 | Native command completed. Corpus-wide validation is not corpus-wide scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/validate_strict.py data/traits/physiology/bacterial_polar_flagellar_ejection.yaml | passed | True | traitmech:000732 | Native command completed. Corpus-wide validation is not corpus-wide scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/validate_history_links.py history/records/bacterial_polar_flagellar_ejection | passed | True | traitmech:000732 | Native command completed. Corpus-wide validation is not corpus-wide scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/verify_snippets.py --record data/traits/physiology/bacterial_polar_flagellar_ejection.yaml --out /tmp/traitmech-bacterial-ejection-checks-20261015/native.tsv | passed | True | traitmech:000732 | Native command completed. Corpus-wide validation is not corpus-wide scientific review. Actual native outcomes are NOT_IN_ABSTRACT, VERIFIED and NOT_IN_ABSTRACT; direct full-text matches are separate evidence. |
| just verify-proposal metpo_traitmech_v608 | passed | True | traitmech:000732 | Native command completed. Corpus-wide validation is not corpus-wide scientific review. |
| just robot-validate-proposal metpo_traitmech_v608 | passed | True | traitmech:000732 | Native command completed. Corpus-wide validation is not corpus-wide scientific review. |
| just audit-proposals | passed | True | traitmech:000732 | Native command completed. Corpus-wide validation is not corpus-wide scientific review. |
| just ground-predicates | passed | True | traitmech:000732 | Native command completed. Corpus-wide validation is not corpus-wide scientific review. |
| just ground-nodes | passed | True | traitmech:000732 | Native command completed. Corpus-wide validation is not corpus-wide scientific review. |
| just audit-graphs | passed | True | traitmech:000732 | Native command completed. Corpus-wide validation is not corpus-wide scientific review. |
| just audit-graph-protein-taxa | passed | True | traitmech:000732 | Native command completed. Corpus-wide validation is not corpus-wide scientific review. |
| just audit-predicate-domains | passed | True | traitmech:000732 | Native command completed. Corpus-wide validation is not corpus-wide scientific review. |
| just check-biolink-coverage | passed | True | traitmech:000732 | Native command completed. Corpus-wide validation is not corpus-wide scientific review. |
| just audit-snippets | passed | True | traitmech:000732 | Native command completed. Corpus-wide validation is not corpus-wide scientific review. |
| just gen-discussions-data | passed | True | traitmech:000732 | Native command completed. Corpus-wide validation is not corpus-wide scientific review. |
| just gen-qc-dashboard | passed | True | traitmech:000732 | Native command completed. Corpus-wide validation is not corpus-wide scientific review. |
| just gen-pages | passed | True | traitmech:000732 | Native command completed. Corpus-wide validation is not corpus-wide scientific review. |
| just gen-priority-dashboard | passed | True | traitmech:000732 | Native command completed. Corpus-wide validation is not corpus-wide scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python -m pytest -q tests/test_add_bacterial_polar_flagellar_ejection_trait.py tests/test_readme_artifacts.py tests/test_trait_priority.py tests/test_qc_dashboard_artifacts.py | passed | True | traitmech:000732 | Native command completed. Corpus-wide validation is not corpus-wide scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/ruff check src scripts tests | passed | True | traitmech:000732 | Native command completed. Corpus-wide validation is not corpus-wide scientific review. |
| just fetch-record-review-bases --apply | passed | True | traitmech:000732 | Native command completed. Corpus-wide validation is not corpus-wide scientific review. |
| just qc | passed | True | traitmech:000732 | Native command completed. Corpus-wide validation is not corpus-wide scientific review. |
| just validate-history | passed | True | traitmech:000732 | Native command completed. Corpus-wide validation is not corpus-wide scientific review. |
| just validate-products | passed | True | traitmech:000732 | Native command completed. Corpus-wide validation is not corpus-wide scientific review. Product identifiers without an adapter remain SKIPPED_NO_ADAPTER, not authority-verified. |
| just verify-proposal metpo_traitmech_v608 | passed | True | traitmech:000732 | Native command completed. Corpus-wide validation is not corpus-wide scientific review. |
| just robot-validate-proposal metpo_traitmech_v608 | passed | True | traitmech:000732 | Native command completed. Corpus-wide validation is not corpus-wide scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/audit_canonical_examples.py --no-resolve | passed | True | traitmech:000732 | Native command completed. Corpus-wide validation is not corpus-wide scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/run_trait_graph_audit.py --verify | passed | True | traitmech:000732 | Native command completed. Corpus-wide validation is not corpus-wide scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/audit_history_records.py --base 616a97577299f7a33d9b6c98ab29c28b30c64758 | passed | True | traitmech:000732 | Native command completed. Corpus-wide validation is not corpus-wide scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python -m pytest -q --junitxml=/tmp/traitmech-bacterial-ejection-checks-20261015/pytest.xml | passed | True | traitmech:000732 | Native command completed. Corpus-wide validation is not corpus-wide scientific review. |
| Full checkpoint suite count | passed | True | traitmech:000732 | 4777 tests passed; zero failures, errors or skips. |
| products | passed | True | traitmech:000732 | 1127 records, with all 1126 prior records byte-preserved. Prior histories, reviews, proposals, embeddings, shared browser templates and snippet baseline preserved. 1125 prior pages changed only in footer; phenotype also gains one child link/count. Only existing priority-row delta is phenotype children 204 to 205. |
| rdf | passed | True | traitmech:000732 | Parsed graphs contain 15/12628/12632 triples. The actual w3id child-parent-quality hierarchy and IAO definition-source annotation match the canonical proposal. Only the local record and definition-authority DOI annotate the definition. |
| browser | passed | True | traitmech:000732 | Chrome at 1440 and 390 pixels passed identity, three quotes, four OPEN discussions, history, browse navigation, dashboard counts/image, overflow and page-error checks. Six screenshots visually inspected before checkpoint; inspected inputs remain unchanged. |
| Scoped ROBOT whitespace exception | passed | True | traitmech:000732 | Ordinary staged diff check flags the required trailing empty directive cells on template line 2. Both canonical headers and the row have 11 columns. Non-template staged check and exact-template blank-at-eol exception passed; no global whitespace setting changed. |
| Configured embedding sources | not_applicable | False | traitmech:000732 | Both exact configured source paths absent in main and owned layouts. Existing artifacts retained, not regenerated. The isolated shared generator has 645 files checked against its pinned Git tree. Coverage PNG was regenerated and is byte-identical; dashboard counts changed. |
| Fresh local and remote reservation reassessment | passed | True | traitmech:000732 | Changed CommunityMech participant-census follow-up introduces no competing candidate or reservation. Earlier acceptance receipts are preserved; publication checks supplement rather than rewrite that history. |

## Scientific And Domain Assessments

### Active basal release phenotype

identity: supported. Targets: traitmech:000732.

Reusable organismal phenotype, not a sequence feature or a motility/assembly defect. Basal release is supported without imposing the same released components, exact molecular cut, stimulus or nonmotility on every instance.

### Phenotype and deprecated identifiers

grounding: supported. Targets: traitmech:000732.

Phenotype is strictly broader by definition. Possession or arrangement is not ejection; deprecated terms and replacements are not exact xrefs. The pin remains unchanged.

### Distinct experimental endpoints

evidence: supported. Targets: traitmech:000732.

Recovered hook-bearing structures, stationary-culture imaging and the nutrient-associated relic comparison support the bounded trait. Population proxies, cell/tomogram counts, biological replicates and trajectories remain distinct. Native full-text misses are not mislabeled VERIFIED.

### No universal added-plug or rod-cut claim

evidence: supported. Targets: traitmech:000732.

The newer FlgI closure interpretation prevents imposing an unidentified added plug. Neither gate-deletion assembly defects nor gene/domain possession establishes ejection failure or organismal phenotype. Cryo-ET states are not a longitudinal trajectory.

### Guarded writer and source receipt

provenance: supported. Targets: traitmech:000732.

Mutation/history safeguards and compact provenance preserve existing records. No new skill rule is warranted: current source, sequence-boundary and review instructions cover the candidate.

### Proposal and rendered artifacts

consistency: supported. Targets: traitmech:000732.

One canonical class row emits the correct w3id parent chain and role-correct definition annotation. Counts, links and dashboards match 1127 records; prior scientific bytes are preserved.

### Authority and mechanism gaps

completeness: unknown. Targets: traitmech:000732.

Canonical strain/taxon provenance, protein-resolved causal graph and exact external mappings remain deferred. Unread figures/supplements and unavailable pages limit the evidence assessment without negating the bounded phenotype.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| source-0 | DOI:10.1371/journal.pbio.3000165; Results, Shed hook-filament structures accumulate in P. shigelloides supernatant, third paragraph; Figure 1G; https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3000165 | supports | Ferreira et al. 2019, PMID:30889173, PMC6424402. Results, Shed hook-filament structures accumulate in P. shigelloides supernatant, third paragraph; Figure 1G. Direct publisher full-text match; native NOT_IN_ABSTRACT. Hook-bearing released structures, population counts and relic/assembly comparisons support ejection rather than daughter-cell dilution or passive midfilament breakage. Nutrient-depletion conditions vary among assays; minimal medium containing glucose is not complete carbon starvation. All 25 main PDF pages and six figures were inspected, not raw supplementary data. Energy conservation and leakage prevention are interpretations. The archived publisher Results paragraph and its biochemical comparison were reread during formal review; all main PDF pages/figures had been read during research, not reread in full here. Timestamp records cached-source hash recheck, not original acquisition. |
| source-1 | DOI:10.1111/mmi.14511; Scientific abstract; sentence beginning Interestingly, we observed; https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:32259388%20AND%20SRC:MED&amp;format=json&amp;resultType=core | supports | Zhuang et al. 2020, PMID:32259388, scientific abstract, sentence beginning Interestingly. Direct MED/publisher match and native VERIFIED. Main publisher text and six figure captions were subsequently read, not the actual figures or supplement. Sections 2.4-2.7 separate daughter-cell dilution from stationary-phase shedding. OD times flagellated fraction is a population proxy, not a direct cell count. VIO5 and engineered EGFP-FliG strain NMB344 are distinct; red/green panels in Figure 3 are not the same cells. Two-color experiments in Figures 5-6 support basal release, but rod breakage is inferred, not a directly imaged cut. Surface immobilization and medium exchanges constrain the assay. Publisher abstract, Results 2.7 and Methods 4.5-4.6 were reaccessed during formal review. Actual figures, PDF and supplement remain unread. Rod severing is inferred, and 69/72 shedding cases are not biological replicates. Timestamp records cached-source hash recheck, not original acquisition. |
| source-2 | DOI:10.1038/s41467-026-75593-6; Results, Two distinct in situ architectures of the flagellar motor in V. cholerae; Supplementary Figure 4 and Table 4; https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13521929/fullTextXML | supports | Guo et al. 2026, PMID:42660870, PMC13521929.1, Results, Two distinct in situ architectures of the flagellar motor in V. cholerae, and Supplementary Figure 4. Direct JATS match; native NOT_IN_ABSTRACT. FOMC denotes the flagellar outer membrane complex. The quoted experiment uses wild-type V. cholerae; delta-flhG structural samples are distinct. All 12 main PDF pages and six main figures were inspected, plus the actual supplementary Figure 4 and supplementary tables. Its 81/273 observations are cells in the figure caption and tomograms in Methods/Table 4, not biological replicates or ejection rates. The main-text Table 3 pointer instead corresponds to Table 4. Other supplements remain incompletely read. The direct JATS Results paragraph was reread during formal review. Earlier reading covered all main PDF pages/figures and the specified supplementary figure/tables, not all supplementary assets. Timestamp records cached-source hash recheck, not original acquisition. |
| identity | data/traits/physiology/bacterial_polar_flagellar_ejection.yaml; Complete record and four OPEN discussions | supports | Active basal release of assembled polar flagellar structures is distinct from possession, arrangement, failed assembly, motor arrest, reduced motility, daughter-cell dilution, passive breakage, periplasmic resorption and eukaryotic axonemal autotomy. No exact synonym, xref, canonical taxon or universal molecular mechanism is asserted. |
| implementation | scripts/add_bacterial_polar_flagellar_ejection_trait.py; Whole writer, paired tests and histories | supports | Explicit apply, deep-copy construction, source-template hash guard, prevalidation, conflicting-output refusal and idempotent replay protect this first-pass writer. Later curation is refused, not overwritten. Histories name the actual actor, and scientific status remains PROPOSED. |
| novelty | proposals/metpo_traitmech_v608/proposal.md; Scope, retired identifiers and allocation assessment | supports | Deprecated flagellar identifiers are not revived. Active locomotory possession and polar arrangement do not denote ejection. Exact candidate tokens and narrow competing ranges were not identified within the recorded bounded search. The emitted canonical class is below phenotype; upstream acceptance remains open. |
| provenance | research/traits/physiology/bacterial_polar_flagellar_ejection-source-verification.json; Complete compact source receipt | supports | Three primary publications support the bounded phenotype, not independent replication. The 16906-byte receipt distinguishes native abstract comparisons from direct source matches and retains failed parsing/access, unread assets and notice limits. Full owner inventory remains a hash-linked local audit instead of a large committed array. |
| products | reports/proposal_citation_audit.tsv; Generated products and separate preservation/RDF/browser checks | supports | One new record changes corpus totals to 1127 and adds one phenotype child. No existing scientific record or historical artifact changed; generated footer churn is scoped and verified. |

## Limits And Additional Notes

- Author self-review; no human scientific sign-off or independent replication implied.
- All Ferreira and Guo main PDF pages/figures were read during research; formal review reread relevant source passages, not all pages. Raw data and some supplemental assets remain unread.
- Wiley full main text/captions were read, and selected passages reaccessed during review; actual figures, PDF and supplement remain unread after access failures.
- Bounded publisher/MED notice checks do not establish comprehensive correction/retraction clearance. Native NOT_IN_ABSTRACT is not full-text verification.
- No canonical strain/taxon, universal trigger, protein mechanism, same-cell cryo-ET trajectory or exact external equivalence is inferred.
- Known-copy searches are bounded; temporary local audit files are not guaranteed permanent availability. No literature exhaustion or atomic reservation claimed.
- Configured embedding sources unavailable; prior artifacts retained. No paid research used.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T123901Z-bacterial-polar-flagellar-ejection
kind: record
repository: CultureBotAI/TraitMech
title: Bacterial polar flagellar ejection
started_at: '2026-10-15T11:59:43Z'
finished_at: '2026-10-15T12:39:01Z'
reviewer:
  identity: codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Author falsification-oriented source review, not independent
    or human scientific approval. External review requests and CI do not change this
    attribution.
skill: .claude/skills/add-trait/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The bounded bacterial basal-release phenotype is supported by three primary
  papers. No actionable defect found in this one-record scope; four scope, ontology,
  mechanism and provenance discussions remain OPEN and status remains PROPOSED.
source:
  git_revision: d7c11c8a6a66cba9ce10828051e78894d2fa81da
  state: working_tree
  inputs:
  - path: .claude/skills/add-trait/SKILL.md
    sha256: a9cb4e5e6180e0cd7c62943174af5eb70d558eaa76901b004ac29ca9389f0d90
    role: context
  - path: .claude/skills/manage-identifiers/SKILL.md
    sha256: a5c5aaa10943ee6d15423a5878ed2189e4e0b28a5c6e09fda80ba299ab779ebb
    role: context
  - path: .claude/skills/metpo-proposal/SKILL.md
    sha256: 03f008c011e6f0d45cafb7516a01a3383c0a7e8d11bfc5c9cb31efaeca51275f
    role: context
  - path: DO_NOT_WORK.md
    sha256: 9ae0b05cc06f4ce8938801287a568d535e471d06dda5e258fcdbbed222abf712
    role: context
  - path: README.md
    sha256: fd60e21d42b2fb83aed34746be1512d5d2daaa8943249978cbf5d939131fa798
    role: context
  - path: app/dashboard/priority.json
    sha256: aeca45d21b1437d03e49580520a63a444f58ec0ea3a120134aa454ee770477ca
    role: context
  - path: app/discussions/data.js
    sha256: e578d9a683fd5632006c2bcfde2cbd85917cd474ccf58b3ade8860416fed2765
    role: context
  - path: conf/evidence_snippet_baseline.tsv
    sha256: cbe5c82379e796446366b292f15194d80625b928119b482a67d857a379ab31a7
    role: context
  - path: dashboard/coverage.png
    sha256: 3e23fc5cae5d8b5e75fa071d79216037e6b253c3d0eb8b5a537a390fc223f59d
    role: context
  - path: dashboard/index.html
    sha256: 859269ac3b038ace7b1a0dda29b48ee84899789a50cd0e85b40c63bb79996549
    role: context
  - path: data/raw/metpo.owl
    sha256: 8b6f8fe0510a698579e532658c8ace05da2550093365df9ca83feb0741778415
    role: context
  - path: data/traits/physiology/bacterial_polar_flagellar_ejection.yaml
    sha256: ec434e45b6a24f45ddea632ebb7ba7b05b6a0fff2bd8a0b5852f2e21d40d4a20
    role: target
  - path: data/traits/upper/phenotype.yaml
    sha256: 502760fa1b7179bf4e25ab56ecb91d0b25d5f50ed5cfe44133c63a9b821cc4a4
    role: context
  - path: docs/CURATION_PLAYBOOK.md
    sha256: 735e9b810471da9f7d8364e35ffe1e741edb3421480dac01727db6ea5aa65da9
    role: context
  - path: docs/GROUNDING_POLICY.md
    sha256: 891678c983c2283a47c81c47950b35753981e9339d105f3bbdda92a1f5ab7f42
    role: context
  - path: history/records/bacterial_polar_flagellar_ejection/2026-10-15T114344Z-codex-e46fbc.yaml
    sha256: 6ad09d60b79e4b1543dff6e76991415cfeba29a4293d96e0c63c403c74a5fbde
    role: context
  - path: pages/browse.html
    sha256: 23582db766ac45edcdbaea4b424cf231573e04511cd512350a60aaf289646685
    role: context
  - path: pages/traits/physiology/bacterial_polar_flagellar_ejection.html
    sha256: 1a099ed8a5f161c944a894a5cb0acf4b5ef9ab83e75422ec0ccbd5dcb4208a7e
    role: context
  - path: pages/traits/upper/phenotype.html
    sha256: d745090aca4aaff49a8d78bc9342416ef850df700f07d1973621e9f29ad6c69a
    role: context
  - path: proposals/metpo_traitmech_v607/metpo_proposal_classes_robot.tsv
    sha256: 72af61de0c6d741f00271b48d1656ee47c313fbde38ce953b6cfb81c7a76aae3
    role: context
  - path: proposals/metpo_traitmech_v608/metpo_proposal_classes_robot.tsv
    sha256: 24a186fd10b1bd4c4729e86197cc7b5ab4824df57422912fce0bb8e55ca1f529
    role: context
  - path: proposals/metpo_traitmech_v608/proposal.md
    sha256: 8aa59bda73af3c43851d60ddc4df38d249dcbddfde6e4befe2691c989a234e22
    role: context
  - path: reports/proposal_citation_audit.tsv
    sha256: 93e0296300fc8e261d328361b0475ed36fd2fb6fdba9f368b23f143d8fd6b4d9
    role: context
  - path: research/traits/physiology/bacterial_polar_flagellar_ejection-source-verification.json
    sha256: 31af39e246daa316f57051b4c526a703d79f3b8d492a5853f0fa4ad72be1f331
    role: context
  - path: scripts/add_bacterial_polar_flagellar_ejection_trait.py
    sha256: 2ec2141a827cb62dfa27b8ace73ece4c224bd8836675a7483ceaecbc505adfac
    role: context
  - path: src/traitmech/schema/traitmech.yaml
    sha256: 46c47fc627b80ccbba1e8ab3fb6f2aee93bc2aef7aaf72fe9aadc3257f2c02dd
    role: context
  - path: tests/test_add_bacterial_polar_flagellar_ejection_trait.py
    sha256: fc23ca4e7f51805254b6604798af2c94cb87adf517e71f624abf0f9be9650e37
    role: context
targets:
- target_id: traitmech:000732
  path: data/traits/physiology/bacterial_polar_flagellar_ejection.yaml
  label: bacterial polar flagellar ejection
  kind: maintained
  record_class: TraitRecord
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/physiology/bacterial_polar_flagellar_ejection.yaml
    role: curated_record
  - repository: CultureBotAI/TraitMech
    path: scripts/add_bacterial_polar_flagellar_ejection_trait.py
    role: guarded_writer
scope:
  description: Complete new trait, source evidence, guarded writer/tests, v608 proposal,
    histories and generated surfaces.
  selection: Exact traitmech:000732 and maintained owners; no sampling.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - traitmech:000732
  exclusions:
  - target: Other 1126 records
    reason: Automated corpus validation and byte preservation, not fresh scientific
      review.
  - target: data/traits/physiology/spore_germination.yaml
    reason: Protected by DO_NOT_WORK; unchanged and not curated.
checks:
- check_id: records-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate
    -s src/traitmech/schema/traitmech.yaml --target-class TraitRecord data/traits/physiology/bacterial_polar_flagellar_ejection.yaml
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate
    -s src/traitmech/schema/traitmech.yaml --target-class TraitRecord data/traits/physiology/bacterial_polar_flagellar_ejection.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000732
  summary: Native command completed. Corpus-wide validation is not corpus-wide scientific
    review.
- check_id: records-1
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_strict.py data/traits/physiology/bacterial_polar_flagellar_ejection.yaml
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_strict.py data/traits/physiology/bacterial_polar_flagellar_ejection.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000732
  summary: Native command completed. Corpus-wide validation is not corpus-wide scientific
    review.
- check_id: records-2
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_history_links.py history/records/bacterial_polar_flagellar_ejection
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_history_links.py history/records/bacterial_polar_flagellar_ejection
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000732
  summary: Native command completed. Corpus-wide validation is not corpus-wide scientific
    review.
- check_id: records-3
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/verify_snippets.py --record data/traits/physiology/bacterial_polar_flagellar_ejection.yaml
    --out /tmp/traitmech-bacterial-ejection-checks-20261015/native.tsv
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/verify_snippets.py --record data/traits/physiology/bacterial_polar_flagellar_ejection.yaml
    --out /tmp/traitmech-bacterial-ejection-checks-20261015/native.tsv
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000732
  summary: Native command completed. Corpus-wide validation is not corpus-wide scientific
    review. Actual native outcomes are NOT_IN_ABSTRACT, VERIFIED and NOT_IN_ABSTRACT;
    direct full-text matches are separate evidence.
- check_id: proposal-0
  name: just verify-proposal metpo_traitmech_v608
  command: just verify-proposal metpo_traitmech_v608
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000732
  summary: Native command completed. Corpus-wide validation is not corpus-wide scientific
    review.
- check_id: proposal-1
  name: just robot-validate-proposal metpo_traitmech_v608
  command: just robot-validate-proposal metpo_traitmech_v608
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000732
  summary: Native command completed. Corpus-wide validation is not corpus-wide scientific
    review.
- check_id: generate-0
  name: just audit-proposals
  command: just audit-proposals
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000732
  summary: Native command completed. Corpus-wide validation is not corpus-wide scientific
    review.
- check_id: generate-1
  name: just ground-predicates
  command: just ground-predicates
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000732
  summary: Native command completed. Corpus-wide validation is not corpus-wide scientific
    review.
- check_id: generate-2
  name: just ground-nodes
  command: just ground-nodes
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000732
  summary: Native command completed. Corpus-wide validation is not corpus-wide scientific
    review.
- check_id: generate-3
  name: just audit-graphs
  command: just audit-graphs
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000732
  summary: Native command completed. Corpus-wide validation is not corpus-wide scientific
    review.
- check_id: generate-4
  name: just audit-graph-protein-taxa
  command: just audit-graph-protein-taxa
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000732
  summary: Native command completed. Corpus-wide validation is not corpus-wide scientific
    review.
- check_id: generate-5
  name: just audit-predicate-domains
  command: just audit-predicate-domains
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000732
  summary: Native command completed. Corpus-wide validation is not corpus-wide scientific
    review.
- check_id: generate-6
  name: just check-biolink-coverage
  command: just check-biolink-coverage
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000732
  summary: Native command completed. Corpus-wide validation is not corpus-wide scientific
    review.
- check_id: generate-7
  name: just audit-snippets
  command: just audit-snippets
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000732
  summary: Native command completed. Corpus-wide validation is not corpus-wide scientific
    review.
- check_id: generate-8
  name: just gen-discussions-data
  command: just gen-discussions-data
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000732
  summary: Native command completed. Corpus-wide validation is not corpus-wide scientific
    review.
- check_id: generate-9
  name: just gen-qc-dashboard
  command: just gen-qc-dashboard
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000732
  summary: Native command completed. Corpus-wide validation is not corpus-wide scientific
    review.
- check_id: generate-10
  name: just gen-pages
  command: just gen-pages
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000732
  summary: Native command completed. Corpus-wide validation is not corpus-wide scientific
    review.
- check_id: generate-11
  name: just gen-priority-dashboard
  command: just gen-priority-dashboard
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000732
  summary: Native command completed. Corpus-wide validation is not corpus-wide scientific
    review.
- check_id: focused-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q tests/test_add_bacterial_polar_flagellar_ejection_trait.py tests/test_readme_artifacts.py
    tests/test_trait_priority.py tests/test_qc_dashboard_artifacts.py
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q tests/test_add_bacterial_polar_flagellar_ejection_trait.py tests/test_readme_artifacts.py
    tests/test_trait_priority.py tests/test_qc_dashboard_artifacts.py
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000732
  summary: Native command completed. Corpus-wide validation is not corpus-wide scientific
    review.
- check_id: focused-1
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/ruff
    check src scripts tests
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/ruff
    check src scripts tests
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000732
  summary: Native command completed. Corpus-wide validation is not corpus-wide scientific
    review.
- check_id: prepare-0
  name: just fetch-record-review-bases --apply
  command: just fetch-record-review-bases --apply
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000732
  summary: Native command completed. Corpus-wide validation is not corpus-wide scientific
    review.
- check_id: verify-0
  name: just qc
  command: just qc
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000732
  summary: Native command completed. Corpus-wide validation is not corpus-wide scientific
    review.
- check_id: verify-1
  name: just validate-history
  command: just validate-history
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000732
  summary: Native command completed. Corpus-wide validation is not corpus-wide scientific
    review.
- check_id: verify-2
  name: just validate-products
  command: just validate-products
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000732
  summary: Native command completed. Corpus-wide validation is not corpus-wide scientific
    review. Product identifiers without an adapter remain SKIPPED_NO_ADAPTER, not
    authority-verified.
- check_id: verify-3
  name: just verify-proposal metpo_traitmech_v608
  command: just verify-proposal metpo_traitmech_v608
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000732
  summary: Native command completed. Corpus-wide validation is not corpus-wide scientific
    review.
- check_id: verify-4
  name: just robot-validate-proposal metpo_traitmech_v608
  command: just robot-validate-proposal metpo_traitmech_v608
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000732
  summary: Native command completed. Corpus-wide validation is not corpus-wide scientific
    review.
- check_id: verify-5
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/audit_canonical_examples.py --no-resolve
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/audit_canonical_examples.py --no-resolve
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000732
  summary: Native command completed. Corpus-wide validation is not corpus-wide scientific
    review.
- check_id: verify-6
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/run_trait_graph_audit.py --verify
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/run_trait_graph_audit.py --verify
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000732
  summary: Native command completed. Corpus-wide validation is not corpus-wide scientific
    review.
- check_id: verify-7
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/audit_history_records.py --base 616a97577299f7a33d9b6c98ab29c28b30c64758
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/audit_history_records.py --base 616a97577299f7a33d9b6c98ab29c28b30c64758
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000732
  summary: Native command completed. Corpus-wide validation is not corpus-wide scientific
    review.
- check_id: tests-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q --junitxml=/tmp/traitmech-bacterial-ejection-checks-20261015/pytest.xml
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q --junitxml=/tmp/traitmech-bacterial-ejection-checks-20261015/pytest.xml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000732
  summary: Native command completed. Corpus-wide validation is not corpus-wide scientific
    review.
- check_id: suite-count
  name: Full checkpoint suite count
  status: passed
  required: true
  target_ids:
  - traitmech:000732
  summary: 4777 tests passed; zero failures, errors or skips.
- check_id: products
  name: products
  command: /tmp/traitmech-bacterial-ejection-products-20261015.py
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000732
  summary: 1127 records, with all 1126 prior records byte-preserved. Prior histories,
    reviews, proposals, embeddings, shared browser templates and snippet baseline
    preserved. 1125 prior pages changed only in footer; phenotype also gains one child
    link/count. Only existing priority-row delta is phenotype children 204 to 205.
- check_id: rdf
  name: rdf
  command: /tmp/traitmech-bacterial-ejection-rdf-20261015.py
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000732
  summary: Parsed graphs contain 15/12628/12632 triples. The actual w3id child-parent-quality
    hierarchy and IAO definition-source annotation match the canonical proposal. Only
    the local record and definition-authority DOI annotate the definition.
- check_id: browser
  name: browser
  command: node /tmp/traitmech-bacterial-ejection-browser-20261015.cjs
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000732
  summary: Chrome at 1440 and 390 pixels passed identity, three quotes, four OPEN
    discussions, history, browse navigation, dashboard counts/image, overflow and
    page-error checks. Six screenshots visually inspected before checkpoint; inspected
    inputs remain unchanged.
- check_id: whitespace
  name: Scoped ROBOT whitespace exception
  status: passed
  required: true
  target_ids:
  - traitmech:000732
  summary: Ordinary staged diff check flags the required trailing empty directive
    cells on template line 2. Both canonical headers and the row have 11 columns.
    Non-template staged check and exact-template blank-at-eol exception passed; no
    global whitespace setting changed.
- check_id: embeddings
  name: Configured embedding sources
  status: not_applicable
  required: false
  target_ids:
  - traitmech:000732
  summary: Both exact configured source paths absent in main and owned layouts. Existing
    artifacts retained, not regenerated. The isolated shared generator has 645 files
    checked against its pinned Git tree. Coverage PNG was regenerated and is byte-identical;
    dashboard counts changed.
- check_id: publication-drift
  name: Fresh local and remote reservation reassessment
  command: /tmp/traitmech-bacterial-ejection-publication-reconcile-20261015.py
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000732
  summary: Changed CommunityMech participant-census follow-up introduces no competing
    candidate or reservation. Earlier acceptance receipts are preserved; publication
    checks supplement rather than rewrite that history.
evidence:
- evidence_id: source-0
  kind: primary_source
  reference: DOI:10.1371/journal.pbio.3000165
  locator: Results, Shed hook-filament structures accumulate in P. shigelloides supernatant,
    third paragraph; Figure 1G; https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3000165
  accessed_at: '2026-10-15T12:39:01Z'
  support: supports
  snapshot_sha256: ae764839eb4744db1307bd422cc836504005ab51e24908150e1d5ca17071a7ba
  summary: Ferreira et al. 2019, PMID:30889173, PMC6424402. Results, Shed hook-filament
    structures accumulate in P. shigelloides supernatant, third paragraph; Figure
    1G. Direct publisher full-text match; native NOT_IN_ABSTRACT. Hook-bearing released
    structures, population counts and relic/assembly comparisons support ejection
    rather than daughter-cell dilution or passive midfilament breakage. Nutrient-depletion
    conditions vary among assays; minimal medium containing glucose is not complete
    carbon starvation. All 25 main PDF pages and six figures were inspected, not raw
    supplementary data. Energy conservation and leakage prevention are interpretations.
    The archived publisher Results paragraph and its biochemical comparison were reread
    during formal review; all main PDF pages/figures had been read during research,
    not reread in full here. Timestamp records cached-source hash recheck, not original
    acquisition.
- evidence_id: source-1
  kind: primary_source
  reference: DOI:10.1111/mmi.14511
  locator: Scientific abstract; sentence beginning Interestingly, we observed; https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:32259388%20AND%20SRC:MED&format=json&resultType=core
  accessed_at: '2026-10-15T12:39:01Z'
  support: supports
  snapshot_sha256: 02f8c92aa90d05daa118f1cf2cfdd5735caeafeb695f2f733278c53680d31240
  summary: Zhuang et al. 2020, PMID:32259388, scientific abstract, sentence beginning
    Interestingly. Direct MED/publisher match and native VERIFIED. Main publisher
    text and six figure captions were subsequently read, not the actual figures or
    supplement. Sections 2.4-2.7 separate daughter-cell dilution from stationary-phase
    shedding. OD times flagellated fraction is a population proxy, not a direct cell
    count. VIO5 and engineered EGFP-FliG strain NMB344 are distinct; red/green panels
    in Figure 3 are not the same cells. Two-color experiments in Figures 5-6 support
    basal release, but rod breakage is inferred, not a directly imaged cut. Surface
    immobilization and medium exchanges constrain the assay. Publisher abstract, Results
    2.7 and Methods 4.5-4.6 were reaccessed during formal review. Actual figures,
    PDF and supplement remain unread. Rod severing is inferred, and 69/72 shedding
    cases are not biological replicates. Timestamp records cached-source hash recheck,
    not original acquisition.
- evidence_id: source-2
  kind: primary_source
  reference: DOI:10.1038/s41467-026-75593-6
  locator: Results, Two distinct in situ architectures of the flagellar motor in V.
    cholerae; Supplementary Figure 4 and Table 4; https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13521929/fullTextXML
  accessed_at: '2026-10-15T12:39:01Z'
  support: supports
  snapshot_sha256: 0f4ef185dfeca2420817818579dfcfac5f78d637b16735ae136747c30352f81e
  summary: Guo et al. 2026, PMID:42660870, PMC13521929.1, Results, Two distinct in
    situ architectures of the flagellar motor in V. cholerae, and Supplementary Figure
    4. Direct JATS match; native NOT_IN_ABSTRACT. FOMC denotes the flagellar outer
    membrane complex. The quoted experiment uses wild-type V. cholerae; delta-flhG
    structural samples are distinct. All 12 main PDF pages and six main figures were
    inspected, plus the actual supplementary Figure 4 and supplementary tables. Its
    81/273 observations are cells in the figure caption and tomograms in Methods/Table
    4, not biological replicates or ejection rates. The main-text Table 3 pointer
    instead corresponds to Table 4. Other supplements remain incompletely read. The
    direct JATS Results paragraph was reread during formal review. Earlier reading
    covered all main PDF pages/figures and the specified supplementary figure/tables,
    not all supplementary assets. Timestamp records cached-source hash recheck, not
    original acquisition.
- evidence_id: identity
  kind: record_content
  reference: data/traits/physiology/bacterial_polar_flagellar_ejection.yaml
  locator: Complete record and four OPEN discussions
  accessed_at: '2026-10-15T12:39:01Z'
  support: supports
  snapshot_sha256: ec434e45b6a24f45ddea632ebb7ba7b05b6a0fff2bd8a0b5852f2e21d40d4a20
  summary: Active basal release of assembled polar flagellar structures is distinct
    from possession, arrangement, failed assembly, motor arrest, reduced motility,
    daughter-cell dilution, passive breakage, periplasmic resorption and eukaryotic
    axonemal autotomy. No exact synonym, xref, canonical taxon or universal molecular
    mechanism is asserted.
- evidence_id: implementation
  kind: record_content
  reference: scripts/add_bacterial_polar_flagellar_ejection_trait.py
  locator: Whole writer, paired tests and histories
  accessed_at: '2026-10-15T12:39:01Z'
  support: supports
  snapshot_sha256: 2ec2141a827cb62dfa27b8ace73ece4c224bd8836675a7483ceaecbc505adfac
  summary: Explicit apply, deep-copy construction, source-template hash guard, prevalidation,
    conflicting-output refusal and idempotent replay protect this first-pass writer.
    Later curation is refused, not overwritten. Histories name the actual actor, and
    scientific status remains PROPOSED.
- evidence_id: novelty
  kind: search
  reference: proposals/metpo_traitmech_v608/proposal.md
  locator: Scope, retired identifiers and allocation assessment
  accessed_at: '2026-10-15T12:39:01Z'
  support: supports
  snapshot_sha256: 8aa59bda73af3c43851d60ddc4df38d249dcbddfde6e4befe2691c989a234e22
  summary: Deprecated flagellar identifiers are not revived. Active locomotory possession
    and polar arrangement do not denote ejection. Exact candidate tokens and narrow
    competing ranges were not identified within the recorded bounded search. The emitted
    canonical class is below phenotype; upstream acceptance remains open.
  search_scope: 'Ignored/hidden current files in 204 known locations; 295 retained
    heads, 86276 TraitMech and 9268 CommunityMech unique regular blobs. Nine unavailable
    locations explicit. All 458 biological and 66 allocation windows assessed. Full
    ranges: 189221 owner contexts, 2636 unique contents, 27 general-envelope overlaps.
    Refreshed 13 open/draft PRs, 812 nonremoved changed blobs and 587 upstream owners.
    CommunityMech PR2018 and its changed local worktree were rechecked; the 11:39:13
    UTC guard was unchanged. Lost ignored/untracked history, arbitrary archives, symlink
    targets and unchanged PR files were not reconstructed. Not global exhaustion or
    an atomic reservation. Publication refresh additionally checked 205 current locations
    including ignored/hidden files; exact tokens occur only in the owned worktree.
    Current remote snapshot has 823 changed blobs. CommunityMech PR2018 advanced to
    be3299e47d79a51f90a28e008409c793fb939eeb: its revised description, 11 changed/additional
    full contents and stable local current files were reassessed. No new candidate
    or wrapped-range matches; 37 local contexts are unchanged from the prior assessed
    set.'
- evidence_id: provenance
  kind: record_content
  reference: research/traits/physiology/bacterial_polar_flagellar_ejection-source-verification.json
  locator: Complete compact source receipt
  accessed_at: '2026-10-15T12:39:01Z'
  support: supports
  snapshot_sha256: 31af39e246daa316f57051b4c526a703d79f3b8d492a5853f0fa4ad72be1f331
  summary: Three primary publications support the bounded phenotype, not independent
    replication. The 16906-byte receipt distinguishes native abstract comparisons
    from direct source matches and retains failed parsing/access, unread assets and
    notice limits. Full owner inventory remains a hash-linked local audit instead
    of a large committed array.
- evidence_id: products
  kind: validation
  reference: reports/proposal_citation_audit.tsv
  locator: Generated products and separate preservation/RDF/browser checks
  accessed_at: '2026-10-15T12:39:01Z'
  support: supports
  snapshot_sha256: 93e0296300fc8e261d328361b0475ed36fd2fb6fdba9f368b23f143d8fd6b4d9
  summary: One new record changes corpus totals to 1127 and adds one phenotype child.
    No existing scientific record or historical artifact changed; generated footer
    churn is scoped and verified.
assessments:
- assessment_id: identity
  area: identity
  topic: Active basal release phenotype
  summary: Reusable organismal phenotype, not a sequence feature or a motility/assembly
    defect. Basal release is supported without imposing the same released components,
    exact molecular cut, stimulus or nonmotility on every instance.
  target_ids:
  - traitmech:000732
  evidence_ids:
  - identity
  - source-0
  - source-1
  - source-2
  outcome: supported
- assessment_id: parent
  area: grounding
  topic: Phenotype and deprecated identifiers
  summary: Phenotype is strictly broader by definition. Possession or arrangement
    is not ejection; deprecated terms and replacements are not exact xrefs. The pin
    remains unchanged.
  target_ids:
  - traitmech:000732
  evidence_ids:
  - identity
  - novelty
  outcome: supported
- assessment_id: evidence
  area: evidence
  topic: Distinct experimental endpoints
  summary: Recovered hook-bearing structures, stationary-culture imaging and the nutrient-associated
    relic comparison support the bounded trait. Population proxies, cell/tomogram
    counts, biological replicates and trajectories remain distinct. Native full-text
    misses are not mislabeled VERIFIED.
  target_ids:
  - traitmech:000732
  evidence_ids:
  - source-0
  - source-1
  - source-2
  - provenance
  outcome: supported
- assessment_id: mechanism
  area: evidence
  topic: No universal added-plug or rod-cut claim
  summary: The newer FlgI closure interpretation prevents imposing an unidentified
    added plug. Neither gate-deletion assembly defects nor gene/domain possession
    establishes ejection failure or organismal phenotype. Cryo-ET states are not a
    longitudinal trajectory.
  target_ids:
  - traitmech:000732
  evidence_ids:
  - identity
  - source-0
  - source-1
  - source-2
  outcome: supported
- assessment_id: mutation
  area: provenance
  topic: Guarded writer and source receipt
  summary: 'Mutation/history safeguards and compact provenance preserve existing records.
    No new skill rule is warranted: current source, sequence-boundary and review instructions
    cover the candidate.'
  target_ids:
  - traitmech:000732
  evidence_ids:
  - implementation
  - provenance
  outcome: supported
- assessment_id: products
  area: consistency
  topic: Proposal and rendered artifacts
  summary: One canonical class row emits the correct w3id parent chain and role-correct
    definition annotation. Counts, links and dashboards match 1127 records; prior
    scientific bytes are preserved.
  target_ids:
  - traitmech:000732
  evidence_ids:
  - novelty
  - products
  outcome: supported
- assessment_id: limits
  area: completeness
  topic: Authority and mechanism gaps
  summary: Canonical strain/taxon provenance, protein-resolved causal graph and exact
    external mappings remain deferred. Unread figures/supplements and unavailable
    pages limit the evidence assessment without negating the bounded phenotype.
  target_ids:
  - traitmech:000732
  evidence_ids:
  - identity
  - provenance
  outcome: unknown
findings: []
actions: []
limitations:
- Author self-review; no human scientific sign-off or independent replication implied.
- All Ferreira and Guo main PDF pages/figures were read during research; formal review
  reread relevant source passages, not all pages. Raw data and some supplemental assets
  remain unread.
- Wiley full main text/captions were read, and selected passages reaccessed during
  review; actual figures, PDF and supplement remain unread after access failures.
- Bounded publisher/MED notice checks do not establish comprehensive correction/retraction
  clearance. Native NOT_IN_ABSTRACT is not full-text verification.
- No canonical strain/taxon, universal trigger, protein mechanism, same-cell cryo-ET
  trajectory or exact external equivalence is inferred.
- Known-copy searches are bounded; temporary local audit files are not guaranteed
  permanent availability. No literature exhaustion or atomic reservation claimed.
- Configured embedding sources unavailable; prior artifacts retained. No paid research
  used.
links:
- https://doi.org/10.1371/journal.pbio.3000165
- https://doi.org/10.1111/mmi.14511
- https://doi.org/10.1038/s41467-026-75593-6
tags:
- add-trait
- flagellar-ejection
- self-review
```
