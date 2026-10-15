# Eukaryotic flagellar autotomy and receipt remediation

- Review: 20261015T090714Z-eukaryotic-flagellar-autotomy
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-15T08:22:19Z
- Finished UTC: 2026-10-15T09:07:14Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The bounded microbial-eukaryotic shedding phenotype is supported. The one provenance-artifact finding is resolved with evidence-preserving compaction and regression coverage; four scope/mechanism/provenance discussions remain OPEN and status remains PROPOSED.

## Scope And Provenance

Complete new trait, source evidence, guarded writer/tests, v607 proposal, histories and generated surfaces.

Selection: Exact traitmech:000731 and maintained owners; no sampling.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 41b162d8361240d25182e7d3f0d63e69e56544a4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| traitmech:000731 | data/traits/physiology/eukaryotic_flagellar_autotomy.yaml | maintained | eukaryotic flagellar autotomy |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate -s src/traitmech/schema/traitmech.yaml --target-class TraitRecord data/traits/physiology/eukaryotic_flagellar_autotomy.yaml | passed | True | traitmech:000731 | Native command completed. Scope follows its arguments; corpus-wide gates are not corpus-wide scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/validate_strict.py data/traits/physiology/eukaryotic_flagellar_autotomy.yaml | passed | True | traitmech:000731 | Native command completed. Scope follows its arguments; corpus-wide gates are not corpus-wide scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/validate_history_links.py history/records/eukaryotic_flagellar_autotomy | passed | True | traitmech:000731 | Native command completed. Scope follows its arguments; corpus-wide gates are not corpus-wide scientific review. |
| Initial snippet lookup without network access | failed | False | traitmech:000731 | DNS failure for all three references proves nothing. Superseded by the successful snippets-network check; failure retained, not presented as verification. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/verify_snippets.py --record data/traits/physiology/eukaryotic_flagellar_autotomy.yaml --out /tmp/traitmech-flagellar-autotomy-checks-20261015/native-network.tsv | passed | True | traitmech:000731 | Native command completed. Scope follows its arguments; corpus-wide gates are not corpus-wide scientific review. |
| just verify-proposal metpo_traitmech_v607 | passed | True | traitmech:000731 | Native command completed. Scope follows its arguments; corpus-wide gates are not corpus-wide scientific review. |
| just robot-validate-proposal metpo_traitmech_v607 | passed | True | traitmech:000731 | Native command completed. Scope follows its arguments; corpus-wide gates are not corpus-wide scientific review. |
| just audit-proposals | passed | True | traitmech:000731 | Native command completed. Scope follows its arguments; corpus-wide gates are not corpus-wide scientific review. |
| just ground-predicates | passed | True | traitmech:000731 | Native command completed. Scope follows its arguments; corpus-wide gates are not corpus-wide scientific review. |
| just ground-nodes | passed | True | traitmech:000731 | Native command completed. Scope follows its arguments; corpus-wide gates are not corpus-wide scientific review. |
| just audit-graphs | passed | True | traitmech:000731 | Native command completed. Scope follows its arguments; corpus-wide gates are not corpus-wide scientific review. |
| just audit-graph-protein-taxa | passed | True | traitmech:000731 | Native command completed. Scope follows its arguments; corpus-wide gates are not corpus-wide scientific review. |
| just audit-predicate-domains | passed | True | traitmech:000731 | Native command completed. Scope follows its arguments; corpus-wide gates are not corpus-wide scientific review. |
| just check-biolink-coverage | passed | True | traitmech:000731 | Native command completed. Scope follows its arguments; corpus-wide gates are not corpus-wide scientific review. |
| just audit-snippets | passed | True | traitmech:000731 | Native command completed. Scope follows its arguments; corpus-wide gates are not corpus-wide scientific review. |
| just gen-discussions-data | passed | True | traitmech:000731 | Native command completed. Scope follows its arguments; corpus-wide gates are not corpus-wide scientific review. |
| just gen-qc-dashboard | passed | True | traitmech:000731 | Native command completed. Scope follows its arguments; corpus-wide gates are not corpus-wide scientific review. |
| just gen-pages | passed | True | traitmech:000731 | Native command completed. Scope follows its arguments; corpus-wide gates are not corpus-wide scientific review. |
| just gen-priority-dashboard | passed | True | traitmech:000731 | Native command completed. Scope follows its arguments; corpus-wide gates are not corpus-wide scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python -m pytest -q tests/test_add_eukaryotic_flagellar_autotomy_trait.py tests/test_readme_artifacts.py tests/test_trait_priority.py tests/test_qc_dashboard_artifacts.py | passed | True | traitmech:000731 | Native command completed. Scope follows its arguments; corpus-wide gates are not corpus-wide scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/ruff check src scripts tests | passed | True | traitmech:000731 | Native command completed. Scope follows its arguments; corpus-wide gates are not corpus-wide scientific review. |
| just fetch-record-review-bases --apply | passed | True | traitmech:000731 | Native command completed. Scope follows its arguments; corpus-wide gates are not corpus-wide scientific review. |
| just qc | passed | True | traitmech:000731 | Native command completed. Scope follows its arguments; corpus-wide gates are not corpus-wide scientific review. |
| just validate-history | passed | True | traitmech:000731 | Native command completed. Scope follows its arguments; corpus-wide gates are not corpus-wide scientific review. |
| just validate-products | passed | True | traitmech:000731 | Native command completed. Scope follows its arguments; corpus-wide gates are not corpus-wide scientific review. Product identifiers with no adapter remain SKIPPED_NO_ADAPTER, not authority-verified. |
| just verify-proposal metpo_traitmech_v607 | passed | True | traitmech:000731 | Native command completed. Scope follows its arguments; corpus-wide gates are not corpus-wide scientific review. |
| just robot-validate-proposal metpo_traitmech_v607 | passed | True | traitmech:000731 | Native command completed. Scope follows its arguments; corpus-wide gates are not corpus-wide scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/audit_canonical_examples.py --no-resolve | passed | True | traitmech:000731 | Native command completed. Scope follows its arguments; corpus-wide gates are not corpus-wide scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/run_trait_graph_audit.py --verify | passed | True | traitmech:000731 | Native command completed. Scope follows its arguments; corpus-wide gates are not corpus-wide scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/audit_history_records.py --base 982e7239752041073343fad00e24fbd9474e4776 | passed | True | traitmech:000731 | Native command completed. Scope follows its arguments; corpus-wide gates are not corpus-wide scientific review. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python -m pytest -q --junitxml=/tmp/traitmech-flagellar-autotomy-checks-20261015/pytest.xml | passed | True | traitmech:000731 | Native command completed. Scope follows its arguments; corpus-wide gates are not corpus-wide scientific review. |
| Full checkpoint suite count | passed | True | traitmech:000731 | 4765 tests passed; zero failures, errors or skips. |
| products | passed | True | traitmech:000731 | 1126 records, with all 1125 prior records byte-preserved. Old histories, reviews, proposals, embeddings, shared browser templates and snippet baseline preserved. 1124 old pages changed only in footer; phenotype page also gains the one child link/count. Priority phenotype children change 203 to 204 only. |
| rdf | passed | True | traitmech:000731 | Parsed graphs contain 15/12628/12632 RDF triples. Actual w3id child-parent-quality hierarchy and IAO definition-source annotation checked. Typed xsd:string labels and pipe-joined IAO_0000119 citation follow the canonical template; initial temporary probe used incorrect literal/property assumptions and was corrected after reading actual RDF. |
| browser | passed | True | traitmech:000731 | Chrome 1440/390-pixel checks passed identity, evidence, four OPEN discussions, history, browse navigation, dashboard count/image, overflow and page errors. Six screenshots visually inspected. |
| receipt-regression | passed | True | traitmech:000731 | The new regression rejects the 74366222-byte pre-fix staged receipt and accepts the 13023-byte correction. Structured roundtrip confirmed all fields except owner-array replacement and new audit reference unchanged. Twelve updated writer tests also passed in 7.25 seconds; full suite includes the added guard. |
| Scoped ROBOT whitespace exception | passed | True | traitmech:000731 | Writer extra EOF blank line corrected before checkpoint. Non-template staged diff check passed; exact template path passed with blank-at-eol disabled. Ordinary header still flags three required empty trailing cells; canonical 11-column format preserved. |
| Configured embedding sources | not_applicable | False | traitmech:000731 | Both exact configured source paths absent in main and owned layouts. Existing artifacts retained, not regenerated. All 645 pinned shared-generator source files were verified after restoring an isolated clone. |

## Scientific And Domain Assessments

### Near-basal axonemal shedding

identity: supported. Targets: traitmech:000731.

Reusable organismal phenotype rather than a sequence feature or assembly/motility defect. Definition matches the basal severing distinction; assay details do not become universal thresholds.

### Phenotype parent and ontology scope

grounding: supported. Targets: traitmech:000731.

Phenotype is strictly broader by definition. Motility is not required. Deprecated morphology and active flagellar-possession terms are not exact xrefs. Upstream eukaryotic scope remains a maintainer question.

### Source roles and experimental endpoints

evidence: supported. Targets: traitmech:000731.

2003 mutant shedding and 2016 normalized biflagellate-cell loss support the trait within stated media/temperature limits. Neither source yields universal protein dependence; two papers are not independent-laboratory replication.

### Bounded p60 limitation

evidence: supported. Targets: traitmech:000731.

The discussion supports a restriction on a universal severing mechanism, not dispensability of every katanin function. Purified protein, transcript knockdown, tested mutants and cell shedding are distinct evidence levels.

### Guarded curation and repaired source receipt

provenance: supported. Targets: traitmech:000731.

Writer/history safeguards preserve prior records; #1944 is resolved by measured and regression-tested receipt compaction, not by dropping scientific evidence.

### Proposal RDF and generated artifacts

consistency: supported. Targets: traitmech:000731.

One canonical class row, correct w3id parent chain and role-correct definition annotation; pages/dashboard match 1126 records with prior scientific bytes preserved.

### Authority, mechanisms and source access

completeness: unknown. Targets: traitmech:000731.

Canonical taxa, molecular graph, exact mappings and broader comparative mechanism remain unresolved. Unread supplements and source-access failures remain explicit rather than claimed absence.

## Findings

### receipt-inventory: Complete temporary search inventory embedded in tracked summary

minor / resolved / confirmed; issue key: flagellar-autotomy-receipt-inventory.

74,366,222 bytes and 184,357 owner objects exceed the intended compact provenance summary. No change to biological claims is required. GitHub issue #1944 tracks this prepublication defect.

Disposition: Count 184357 and complete local audit SHA-256 replace the embedded array. Receipt reduced from 74366222 to 13023 bytes; structured comparison preserves all other content. Regression rejects original bytes and accepts the correction; full native gates pass.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| source-0 | DOI:10.1186/1471-2121-4-11; Direct Europe PMC MED scientific abstract, Results, second sentence; https://link.springer.com/content/pdf/10.1186/1471-2121-4-11.pdf | supports | Parker and Quarmby 2003, PMID:12930563, PMCID:PMC194436, scientific abstract Results, second sentence. Direct MED text match; native VERIFIED applies to that text, not the PDF degree-symbol typography. Background distinguishes basal axonemal severing from resorption. The quoted response concerns source-named Chlamydomonas fla10 in calcium-containing medium, not reference strain WTB214. Released flagella were counted per 100 cells, with the initial count subtracted; lengths are a separate endpoint. Low calcium is not calcium-free, and buffer exchange is a confound. All twelve main PDF pages and eight figures were inspected. No universal IFT or calcium requirement follows. Access time here is the cached-source hash recheck, not original acquisition. Quoted typeset pages and relevant main-text passages were reread during formal assessment. |
| source-1 | DOI:10.1534/g3.116.034264; Results and Discussion, ADF2 and ADF4 remain unassigned, first paragraph; printed p. 3416, Figure 4A context; https://pmc-oa-opendata.s3.amazonaws.com/PMC5068960.1/PMC5068960.1.pdf?md5=d2b988425cbe2af96f1645d3c70ffebc | supports | Hilton et al. 2016, PMID:27520959, PMCID:PMC5068960.1, page 3416, Results and Discussion subsection ADF2 and ADF4 remain unassigned, first paragraph and Figure 4A. Contiguous JATS and typeset match; native NOT_IN_ABSTRACT retained. The comparison is 21 versus 33 degrees C after six hours, not every temperature. The assay scores the control-normalized decrease in biflagellate cells per 100 cells, not a direct count of released flagella or proof that every responding cell loses both. Figure 4A reports three independent experiments with SD. All ten main pages, four figures and three tables were inspected; supplements remain unread. Phototaxis screening alone is not the shedding endpoint. Access time here is the cached-source hash recheck, not original acquisition. Quoted typeset pages and relevant main-text passages were reread during formal assessment. |
| mechanism | DOI:10.1242/jcs.096941; Discussion, Is katanin required for flagellar excision in Chlamydomonas?; Figure 5A; https://pmc.ncbi.nlm.nih.gov/articles/PMC3516377/ | supports | Dymek and Smith 2012, PMID:22467860, PMCID:PMC3516377, Discussion subsection Is katanin required for flagellar excision in Chlamydomonas? Direct HTML match; native NOT_IN_ABSTRACT retained. Main text and all six figures were inspected; supplements were not. Figure 5A assays cellular shedding; Figure 2 assays purified protein. Transcript knockdown is not verified protein depletion. The reference A54-e18 carries listed mutations, and the tested mutants are not nulls. Earlier successful primary HTML reading supports the quote. Formal-review reaccess returned a challenge page, not a new full-text verification. The retained Figure 5 was visually reread; no fresh PDF or supplement access is claimed. |
| identity | data/traits/physiology/eukaryotic_flagellar_autotomy.yaml; Complete new record and four OPEN discussions | supports | Regulated near-basal axonemal shedding is distinct from possession, arrangement, failed assembly, resorption, passive breakage, distal vesicles and premitotic basal-body release alone. Microbial-eukaryote scope excludes bacterial apparatus ejection; no exact synonym, xref, canonical taxon or universal protein mechanism. |
| implementation | scripts/add_eukaryotic_flagellar_autotomy_trait.py; Whole writer, paired regression tests and native curation/repository history | supports | Dry-run default, explicit apply, source-template hash guard, conflicting-output refusal, idempotent replay and prevalidation protect the one-record addition. Histories identify the actual agent and remain PROPOSED. |
| novelty | proposals/metpo_traitmech_v607/proposal.md; Scope, identity/reservation and current changed-PR reassessment | supports | Deprecated morphology terms are not revived. Locomotory flagellar possession is not autotomy. All overlapping reservation ranges are general editor envelopes. Canonical class template emits one proposed class below phenotype; upstream microbial-eukaryote adoption remains unresolved. |
| provenance | research/traits/physiology/eukaryotic_flagellar_autotomy-source-verification.json; All source roles, native outcomes, hashes, access limits and compact range-audit summary | supports | Two distinct experimental papers are not independent-laboratory replication. Mechanism-limitation evidence is not counted definition support. Native results are VERIFIED/NOT_IN_ABSTRACT/NOT_IN_ABSTRACT, with failed DNS retry and unavailable source access retained honestly. Owner inventory now summarized by count and a hash-linked local audit. |
| products | reports/proposal_citation_audit.tsv; Generated pages/reports and independent product/RDF checks | supports | Products reflect one new record, corpus totals and the phenotype child navigation/count. Source records and historical artifacts remain unchanged. |

## Limits And Additional Notes

- Author self-review; no human scientific sign-off or independent-laboratory replication implied.
- Main 2003 and 2016 papers were read during research; relevant quoted pages and methodological text were reread. 2016 supplements remain unread and supplementary index MD5 differs; nine substantive assets matched.
- 2012 main HTML and six figures were read earlier. Fresh formal-review HTML access returned a challenge page; retained Figure 5 was reread. No full PDF, supplements or new successful full-text acquisition claimed.
- Bounded notice checks do not establish comprehensive correction/retraction clearance. Native NOT_IN_ABSTRACT does not independently verify a full-text quote.
- No raw-data reanalysis, canonical strain/taxon, universal p60/FA/TRP15/IFT/calcium mechanism or exact external equivalence is inferred.
- Known-copy searches and local audit hashes are bounded and temporary files are not guaranteed permanent availability. No claim of literature exhaustion or atomic reservation.
- Configured embeddings unavailable; existing artifacts retained. No paid research used.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T090714Z-eukaryotic-flagellar-autotomy
kind: record
repository: CultureBotAI/TraitMech
title: Eukaryotic flagellar autotomy and receipt remediation
started_at: '2026-10-15T08:22:19Z'
finished_at: '2026-10-15T09:07:14Z'
reviewer:
  identity: codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Author falsification-oriented source review, not independent
    or human scientific approval. External requests and CI do not change this attribution.
skill: .claude/skills/add-trait/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The bounded microbial-eukaryotic shedding phenotype is supported. The one
  provenance-artifact finding is resolved with evidence-preserving compaction and
  regression coverage; four scope/mechanism/provenance discussions remain OPEN and
  status remains PROPOSED.
source:
  git_revision: 41b162d8361240d25182e7d3f0d63e69e56544a4
  state: working_tree
  inputs:
  - path: .claude/skills/add-trait/SKILL.md
    sha256: a9cb4e5e6180e0cd7c62943174af5eb70d558eaa76901b004ac29ca9389f0d90
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
    sha256: ad5edd82e7b3a0f52e76b6b6e31fb5ea97e0bf0503ad2936ae72572d1820beaf
    role: context
  - path: app/dashboard/priority.html
    sha256: ee56ea18f57639736c167fb6caee91308959124642c138ad0e5e3d2a0e133dc9
    role: context
  - path: app/dashboard/priority.json
    sha256: b9aa41fc676be48e11050005f44dc4241a105132407db9cf1e44a19fd374be0e
    role: context
  - path: app/discussions/data.js
    sha256: b9ad8687d3ab1e87d4a3861a005de24c94de4bf99cb1b99010f4e7baaf97cade
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
    sha256: 3e23fc5cae5d8b5e75fa071d79216037e6b253c3d0eb8b5a537a390fc223f59d
    role: context
  - path: dashboard/index.html
    sha256: 9b5cabae780d32de2e0da3839fac279ddc900b61e75951945cb9ce1b8613d06f
    role: context
  - path: data/raw/metpo.owl
    sha256: 8b6f8fe0510a698579e532658c8ace05da2550093365df9ca83feb0741778415
    role: context
  - path: data/traits/physiology/eukaryotic_flagellar_autotomy.yaml
    sha256: e4d4924721768cd6c677b9cdc4781960a0526aa83537b182c7e9df1ba07f3bdc
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
  - path: docs/MERGE_QUEUE.md
    sha256: d3d88b6cb78d755f92e0f72898e75b70ac076cad110f729693fcb9661d27473e
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
  - path: history/records/eukaryotic_flagellar_autotomy/2026-10-15T080109Z-codex-566021.yaml
    sha256: 0424adcc0f610f47cad9a38d4c5fab405aff579128cdefcaaade57251c547fa5
    role: context
  - path: justfile
    sha256: e6047ea612115a6a78d100b281483ba824c860c3def59bcd0d40e7fb56b3526a
    role: context
  - path: pages/browse.html
    sha256: b2ebd44cd55f74b8a3f0d3bed2112ef34dcfc04622d1a0134b8c04ce161d13e0
    role: context
  - path: pages/traits/physiology/eukaryotic_flagellar_autotomy.html
    sha256: d513461af2068cf5f784b79953ff94d7a6de1cbcc93dcdfcb9ec80b8bab58804
    role: context
  - path: pages/traits/upper/phenotype.html
    sha256: 3fd9e9ea9d0aeaf750dcac81c76b96bbefccee246115a570250224ab63c8285b
    role: context
  - path: proposals/metpo_traitmech_v606/metpo_proposal_classes_robot.tsv
    sha256: 8ed5281bf51e818afa9a78b24582122b1b67cf85e26cc9e95ab5a6e3ea044609
    role: context
  - path: proposals/metpo_traitmech_v607/metpo_proposal_classes_robot.tsv
    sha256: 72af61de0c6d741f00271b48d1656ee47c313fbde38ce953b6cfb81c7a76aae3
    role: context
  - path: proposals/metpo_traitmech_v607/proposal.md
    sha256: 161e52bf8f19987ff2af6e0340e8c303c49816be10adac942e1cbb2525624436
    role: context
  - path: reports/proposal_citation_audit.tsv
    sha256: 59166077243db5e7b686a61842df9613c66771a3f8eda81d9bc713a95e6c8864
    role: context
  - path: research/traits/physiology/eukaryotic_flagellar_autotomy-source-verification.json
    sha256: fa3ac61aee0bf9afcb56ea34ed685eb0f5d79b5e90ddec82c36a9dc8b4cb22a5
    role: context
  - path: scripts/add_eukaryotic_flagellar_autotomy_trait.py
    sha256: 9fdb337d58a05bc540b59f3a2b3a70df9a857f58dfe8b879155d35b189da58ae
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
  - path: tests/test_add_eukaryotic_flagellar_autotomy_trait.py
    sha256: 88ce56498fbb4008185107e3f247e982d89e95371e485e85809c45c4e713a0f2
    role: context
targets:
- target_id: traitmech:000731
  path: data/traits/physiology/eukaryotic_flagellar_autotomy.yaml
  label: eukaryotic flagellar autotomy
  kind: maintained
  record_class: TraitRecord
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/physiology/eukaryotic_flagellar_autotomy.yaml
    role: curated_record
  - repository: CultureBotAI/TraitMech
    path: scripts/add_eukaryotic_flagellar_autotomy_trait.py
    role: guarded_writer
scope:
  description: Complete new trait, source evidence, guarded writer/tests, v607 proposal,
    histories and generated surfaces.
  selection: Exact traitmech:000731 and maintained owners; no sampling.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - traitmech:000731
  exclusions:
  - target: Other 1125 records
    reason: Automated corpus validation and byte preservation, not fresh scientific
      review.
  - target: data/traits/physiology/spore_germination.yaml
    reason: Protected by DO_NOT_WORK; unchanged and not curated.
checks:
- check_id: records-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate
    -s src/traitmech/schema/traitmech.yaml --target-class TraitRecord data/traits/physiology/eukaryotic_flagellar_autotomy.yaml
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate
    -s src/traitmech/schema/traitmech.yaml --target-class TraitRecord data/traits/physiology/eukaryotic_flagellar_autotomy.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000731
  summary: Native command completed. Scope follows its arguments; corpus-wide gates
    are not corpus-wide scientific review.
- check_id: records-1
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_strict.py data/traits/physiology/eukaryotic_flagellar_autotomy.yaml
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_strict.py data/traits/physiology/eukaryotic_flagellar_autotomy.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000731
  summary: Native command completed. Scope follows its arguments; corpus-wide gates
    are not corpus-wide scientific review.
- check_id: records-2
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_history_links.py history/records/eukaryotic_flagellar_autotomy
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_history_links.py history/records/eukaryotic_flagellar_autotomy
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000731
  summary: Native command completed. Scope follows its arguments; corpus-wide gates
    are not corpus-wide scientific review.
- check_id: initial-network-failure
  name: Initial snippet lookup without network access
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/verify_snippets.py --record data/traits/physiology/eukaryotic_flagellar_autotomy.yaml
    --out /tmp/traitmech-flagellar-autotomy-checks-20261015/eukaryotic_flagellar_autotomy-native.tsv
  status: failed
  required: false
  exit_code: 2
  target_ids:
  - traitmech:000731
  summary: DNS failure for all three references proves nothing. Superseded by the
    successful snippets-network check; failure retained, not presented as verification.
- check_id: snippets-network-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/verify_snippets.py --record data/traits/physiology/eukaryotic_flagellar_autotomy.yaml
    --out /tmp/traitmech-flagellar-autotomy-checks-20261015/native-network.tsv
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/verify_snippets.py --record data/traits/physiology/eukaryotic_flagellar_autotomy.yaml
    --out /tmp/traitmech-flagellar-autotomy-checks-20261015/native-network.tsv
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000731
  summary: Native command completed. Scope follows its arguments; corpus-wide gates
    are not corpus-wide scientific review.
- check_id: proposal-0
  name: just verify-proposal metpo_traitmech_v607
  command: just verify-proposal metpo_traitmech_v607
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000731
  summary: Native command completed. Scope follows its arguments; corpus-wide gates
    are not corpus-wide scientific review.
- check_id: proposal-1
  name: just robot-validate-proposal metpo_traitmech_v607
  command: just robot-validate-proposal metpo_traitmech_v607
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000731
  summary: Native command completed. Scope follows its arguments; corpus-wide gates
    are not corpus-wide scientific review.
- check_id: generate-0
  name: just audit-proposals
  command: just audit-proposals
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000731
  summary: Native command completed. Scope follows its arguments; corpus-wide gates
    are not corpus-wide scientific review.
- check_id: generate-1
  name: just ground-predicates
  command: just ground-predicates
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000731
  summary: Native command completed. Scope follows its arguments; corpus-wide gates
    are not corpus-wide scientific review.
- check_id: generate-2
  name: just ground-nodes
  command: just ground-nodes
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000731
  summary: Native command completed. Scope follows its arguments; corpus-wide gates
    are not corpus-wide scientific review.
- check_id: generate-3
  name: just audit-graphs
  command: just audit-graphs
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000731
  summary: Native command completed. Scope follows its arguments; corpus-wide gates
    are not corpus-wide scientific review.
- check_id: generate-4
  name: just audit-graph-protein-taxa
  command: just audit-graph-protein-taxa
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000731
  summary: Native command completed. Scope follows its arguments; corpus-wide gates
    are not corpus-wide scientific review.
- check_id: generate-5
  name: just audit-predicate-domains
  command: just audit-predicate-domains
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000731
  summary: Native command completed. Scope follows its arguments; corpus-wide gates
    are not corpus-wide scientific review.
- check_id: generate-6
  name: just check-biolink-coverage
  command: just check-biolink-coverage
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000731
  summary: Native command completed. Scope follows its arguments; corpus-wide gates
    are not corpus-wide scientific review.
- check_id: generate-7
  name: just audit-snippets
  command: just audit-snippets
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000731
  summary: Native command completed. Scope follows its arguments; corpus-wide gates
    are not corpus-wide scientific review.
- check_id: generate-8
  name: just gen-discussions-data
  command: just gen-discussions-data
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000731
  summary: Native command completed. Scope follows its arguments; corpus-wide gates
    are not corpus-wide scientific review.
- check_id: generate-9
  name: just gen-qc-dashboard
  command: just gen-qc-dashboard
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000731
  summary: Native command completed. Scope follows its arguments; corpus-wide gates
    are not corpus-wide scientific review.
- check_id: generate-10
  name: just gen-pages
  command: just gen-pages
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000731
  summary: Native command completed. Scope follows its arguments; corpus-wide gates
    are not corpus-wide scientific review.
- check_id: generate-11
  name: just gen-priority-dashboard
  command: just gen-priority-dashboard
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000731
  summary: Native command completed. Scope follows its arguments; corpus-wide gates
    are not corpus-wide scientific review.
- check_id: focused-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q tests/test_add_eukaryotic_flagellar_autotomy_trait.py tests/test_readme_artifacts.py
    tests/test_trait_priority.py tests/test_qc_dashboard_artifacts.py
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q tests/test_add_eukaryotic_flagellar_autotomy_trait.py tests/test_readme_artifacts.py
    tests/test_trait_priority.py tests/test_qc_dashboard_artifacts.py
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000731
  summary: Native command completed. Scope follows its arguments; corpus-wide gates
    are not corpus-wide scientific review.
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
  - traitmech:000731
  summary: Native command completed. Scope follows its arguments; corpus-wide gates
    are not corpus-wide scientific review.
- check_id: prepare-0
  name: just fetch-record-review-bases --apply
  command: just fetch-record-review-bases --apply
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000731
  summary: Native command completed. Scope follows its arguments; corpus-wide gates
    are not corpus-wide scientific review.
- check_id: verify-0
  name: just qc
  command: just qc
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000731
  summary: Native command completed. Scope follows its arguments; corpus-wide gates
    are not corpus-wide scientific review.
- check_id: verify-1
  name: just validate-history
  command: just validate-history
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000731
  summary: Native command completed. Scope follows its arguments; corpus-wide gates
    are not corpus-wide scientific review.
- check_id: verify-2
  name: just validate-products
  command: just validate-products
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000731
  summary: Native command completed. Scope follows its arguments; corpus-wide gates
    are not corpus-wide scientific review. Product identifiers with no adapter remain
    SKIPPED_NO_ADAPTER, not authority-verified.
- check_id: verify-3
  name: just verify-proposal metpo_traitmech_v607
  command: just verify-proposal metpo_traitmech_v607
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000731
  summary: Native command completed. Scope follows its arguments; corpus-wide gates
    are not corpus-wide scientific review.
- check_id: verify-4
  name: just robot-validate-proposal metpo_traitmech_v607
  command: just robot-validate-proposal metpo_traitmech_v607
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000731
  summary: Native command completed. Scope follows its arguments; corpus-wide gates
    are not corpus-wide scientific review.
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
  - traitmech:000731
  summary: Native command completed. Scope follows its arguments; corpus-wide gates
    are not corpus-wide scientific review.
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
  - traitmech:000731
  summary: Native command completed. Scope follows its arguments; corpus-wide gates
    are not corpus-wide scientific review.
- check_id: verify-7
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/audit_history_records.py --base 982e7239752041073343fad00e24fbd9474e4776
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/audit_history_records.py --base 982e7239752041073343fad00e24fbd9474e4776
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000731
  summary: Native command completed. Scope follows its arguments; corpus-wide gates
    are not corpus-wide scientific review.
- check_id: tests-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q --junitxml=/tmp/traitmech-flagellar-autotomy-checks-20261015/pytest.xml
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q --junitxml=/tmp/traitmech-flagellar-autotomy-checks-20261015/pytest.xml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000731
  summary: Native command completed. Scope follows its arguments; corpus-wide gates
    are not corpus-wide scientific review.
- check_id: suite-count
  name: Full checkpoint suite count
  status: passed
  required: true
  target_ids:
  - traitmech:000731
  summary: 4765 tests passed; zero failures, errors or skips.
- check_id: products
  name: products
  command: /tmp/traitmech-flagellar-autotomy-products-20261015.py
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000731
  summary: 1126 records, with all 1125 prior records byte-preserved. Old histories,
    reviews, proposals, embeddings, shared browser templates and snippet baseline
    preserved. 1124 old pages changed only in footer; phenotype page also gains the
    one child link/count. Priority phenotype children change 203 to 204 only.
- check_id: rdf
  name: rdf
  command: /tmp/traitmech-flagellar-autotomy-rdf-20261015.py
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000731
  summary: Parsed graphs contain 15/12628/12632 RDF triples. Actual w3id child-parent-quality
    hierarchy and IAO definition-source annotation checked. Typed xsd:string labels
    and pipe-joined IAO_0000119 citation follow the canonical template; initial temporary
    probe used incorrect literal/property assumptions and was corrected after reading
    actual RDF.
- check_id: browser
  name: browser
  command: node /tmp/traitmech-flagellar-autotomy-browser-20261015.cjs
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000731
  summary: Chrome 1440/390-pixel checks passed identity, evidence, four OPEN discussions,
    history, browse navigation, dashboard count/image, overflow and page errors. Six
    screenshots visually inspected.
- check_id: receipt-regression
  name: receipt-regression
  command: /tmp/traitmech-flagellar-autotomy-receipt-regression-20261015.py
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000731
  summary: The new regression rejects the 74366222-byte pre-fix staged receipt and
    accepts the 13023-byte correction. Structured roundtrip confirmed all fields except
    owner-array replacement and new audit reference unchanged. Twelve updated writer
    tests also passed in 7.25 seconds; full suite includes the added guard.
- check_id: whitespace
  name: Scoped ROBOT whitespace exception
  status: passed
  required: true
  target_ids:
  - traitmech:000731
  summary: Writer extra EOF blank line corrected before checkpoint. Non-template staged
    diff check passed; exact template path passed with blank-at-eol disabled. Ordinary
    header still flags three required empty trailing cells; canonical 11-column format
    preserved.
- check_id: embeddings
  name: Configured embedding sources
  status: not_applicable
  required: false
  target_ids:
  - traitmech:000731
  summary: Both exact configured source paths absent in main and owned layouts. Existing
    artifacts retained, not regenerated. All 645 pinned shared-generator source files
    were verified after restoring an isolated clone.
evidence:
- evidence_id: source-0
  kind: primary_source
  reference: DOI:10.1186/1471-2121-4-11
  locator: Direct Europe PMC MED scientific abstract, Results, second sentence; https://link.springer.com/content/pdf/10.1186/1471-2121-4-11.pdf
  accessed_at: '2026-10-15T09:07:14Z'
  support: supports
  snapshot_sha256: 7ff9d25f30d82e320b27a51137931864a43b83113a41e08b14bcf3ba0553a36c
  summary: Parker and Quarmby 2003, PMID:12930563, PMCID:PMC194436, scientific abstract
    Results, second sentence. Direct MED text match; native VERIFIED applies to that
    text, not the PDF degree-symbol typography. Background distinguishes basal axonemal
    severing from resorption. The quoted response concerns source-named Chlamydomonas
    fla10 in calcium-containing medium, not reference strain WTB214. Released flagella
    were counted per 100 cells, with the initial count subtracted; lengths are a separate
    endpoint. Low calcium is not calcium-free, and buffer exchange is a confound.
    All twelve main PDF pages and eight figures were inspected. No universal IFT or
    calcium requirement follows. Access time here is the cached-source hash recheck,
    not original acquisition. Quoted typeset pages and relevant main-text passages
    were reread during formal assessment.
- evidence_id: source-1
  kind: primary_source
  reference: DOI:10.1534/g3.116.034264
  locator: Results and Discussion, ADF2 and ADF4 remain unassigned, first paragraph;
    printed p. 3416, Figure 4A context; https://pmc-oa-opendata.s3.amazonaws.com/PMC5068960.1/PMC5068960.1.pdf?md5=d2b988425cbe2af96f1645d3c70ffebc
  accessed_at: '2026-10-15T09:07:14Z'
  support: supports
  snapshot_sha256: 82ffecba6256551e65400492d97cea7d954b7cd31cbfb97f94104928966dbaf7
  summary: Hilton et al. 2016, PMID:27520959, PMCID:PMC5068960.1, page 3416, Results
    and Discussion subsection ADF2 and ADF4 remain unassigned, first paragraph and
    Figure 4A. Contiguous JATS and typeset match; native NOT_IN_ABSTRACT retained.
    The comparison is 21 versus 33 degrees C after six hours, not every temperature.
    The assay scores the control-normalized decrease in biflagellate cells per 100
    cells, not a direct count of released flagella or proof that every responding
    cell loses both. Figure 4A reports three independent experiments with SD. All
    ten main pages, four figures and three tables were inspected; supplements remain
    unread. Phototaxis screening alone is not the shedding endpoint. Access time here
    is the cached-source hash recheck, not original acquisition. Quoted typeset pages
    and relevant main-text passages were reread during formal assessment.
- evidence_id: mechanism
  kind: primary_source
  reference: DOI:10.1242/jcs.096941
  locator: Discussion, Is katanin required for flagellar excision in Chlamydomonas?;
    Figure 5A; https://pmc.ncbi.nlm.nih.gov/articles/PMC3516377/
  accessed_at: '2026-10-15T09:07:14Z'
  support: supports
  summary: Dymek and Smith 2012, PMID:22467860, PMCID:PMC3516377, Discussion subsection
    Is katanin required for flagellar excision in Chlamydomonas? Direct HTML match;
    native NOT_IN_ABSTRACT retained. Main text and all six figures were inspected;
    supplements were not. Figure 5A assays cellular shedding; Figure 2 assays purified
    protein. Transcript knockdown is not verified protein depletion. The reference
    A54-e18 carries listed mutations, and the tested mutants are not nulls. Earlier
    successful primary HTML reading supports the quote. Formal-review reaccess returned
    a challenge page, not a new full-text verification. The retained Figure 5 was
    visually reread; no fresh PDF or supplement access is claimed.
- evidence_id: identity
  kind: record_content
  reference: data/traits/physiology/eukaryotic_flagellar_autotomy.yaml
  locator: Complete new record and four OPEN discussions
  accessed_at: '2026-10-15T09:07:14Z'
  support: supports
  snapshot_sha256: e4d4924721768cd6c677b9cdc4781960a0526aa83537b182c7e9df1ba07f3bdc
  summary: Regulated near-basal axonemal shedding is distinct from possession, arrangement,
    failed assembly, resorption, passive breakage, distal vesicles and premitotic
    basal-body release alone. Microbial-eukaryote scope excludes bacterial apparatus
    ejection; no exact synonym, xref, canonical taxon or universal protein mechanism.
- evidence_id: implementation
  kind: record_content
  reference: scripts/add_eukaryotic_flagellar_autotomy_trait.py
  locator: Whole writer, paired regression tests and native curation/repository history
  accessed_at: '2026-10-15T09:07:14Z'
  support: supports
  snapshot_sha256: 9fdb337d58a05bc540b59f3a2b3a70df9a857f58dfe8b879155d35b189da58ae
  summary: Dry-run default, explicit apply, source-template hash guard, conflicting-output
    refusal, idempotent replay and prevalidation protect the one-record addition.
    Histories identify the actual agent and remain PROPOSED.
- evidence_id: novelty
  kind: search
  reference: proposals/metpo_traitmech_v607/proposal.md
  locator: Scope, identity/reservation and current changed-PR reassessment
  accessed_at: '2026-10-15T09:07:14Z'
  support: supports
  snapshot_sha256: 161e52bf8f19987ff2af6e0340e8c303c49816be10adac942e1cbb2525624436
  summary: Deprecated morphology terms are not revived. Locomotory flagellar possession
    is not autotomy. All overlapping reservation ranges are general editor envelopes.
    Canonical class template emits one proposed class below phenotype; upstream microbial-eukaryote
    adoption remains unresolved.
  search_scope: 'Ignored/hidden current files in 202 known locations; 291 retained
    heads, 85118 TraitMech and 9178 CommunityMech unique regular blobs. Nine unavailable
    locations explicit. All 154 original and 64 supplementary windows assessed; changed
    CommunityMech locations reconciled. 13 open/draft PRs, 840 original nonremoved
    blobs and 587 selected upstream owners. Subsequent changed PR2013 has 88 files
    rechecked at a1c66812a65bf25bd694d0b8c07bc49303c47da1, no hits or binary limits.
    Full-range check: 184357 owners, 2662 unique contents, 26 general-envelope overlaps.
    No lost ignored/untracked history, arbitrary archives, symlink targets or unchanged
    PR files reconstructed; not global exhaustion or atomic reservation.'
- evidence_id: provenance
  kind: record_content
  reference: research/traits/physiology/eukaryotic_flagellar_autotomy-source-verification.json
  locator: All source roles, native outcomes, hashes, access limits and compact range-audit
    summary
  accessed_at: '2026-10-15T09:07:14Z'
  support: supports
  snapshot_sha256: fa3ac61aee0bf9afcb56ea34ed685eb0f5d79b5e90ddec82c36a9dc8b4cb22a5
  summary: Two distinct experimental papers are not independent-laboratory replication.
    Mechanism-limitation evidence is not counted definition support. Native results
    are VERIFIED/NOT_IN_ABSTRACT/NOT_IN_ABSTRACT, with failed DNS retry and unavailable
    source access retained honestly. Owner inventory now summarized by count and a
    hash-linked local audit.
- evidence_id: products
  kind: validation
  reference: reports/proposal_citation_audit.tsv
  locator: Generated pages/reports and independent product/RDF checks
  accessed_at: '2026-10-15T09:07:14Z'
  support: supports
  snapshot_sha256: 59166077243db5e7b686a61842df9613c66771a3f8eda81d9bc713a95e6c8864
  summary: Products reflect one new record, corpus totals and the phenotype child
    navigation/count. Source records and historical artifacts remain unchanged.
assessments:
- assessment_id: identity
  area: identity
  topic: Near-basal axonemal shedding
  summary: Reusable organismal phenotype rather than a sequence feature or assembly/motility
    defect. Definition matches the basal severing distinction; assay details do not
    become universal thresholds.
  target_ids:
  - traitmech:000731
  evidence_ids:
  - identity
  - source-0
  - source-1
  outcome: supported
- assessment_id: parent
  area: grounding
  topic: Phenotype parent and ontology scope
  summary: Phenotype is strictly broader by definition. Motility is not required.
    Deprecated morphology and active flagellar-possession terms are not exact xrefs.
    Upstream eukaryotic scope remains a maintainer question.
  target_ids:
  - traitmech:000731
  evidence_ids:
  - identity
  - novelty
  outcome: supported
- assessment_id: evidence
  area: evidence
  topic: Source roles and experimental endpoints
  summary: 2003 mutant shedding and 2016 normalized biflagellate-cell loss support
    the trait within stated media/temperature limits. Neither source yields universal
    protein dependence; two papers are not independent-laboratory replication.
  target_ids:
  - traitmech:000731
  evidence_ids:
  - source-0
  - source-1
  - provenance
  outcome: supported
- assessment_id: mechanism
  area: evidence
  topic: Bounded p60 limitation
  summary: The discussion supports a restriction on a universal severing mechanism,
    not dispensability of every katanin function. Purified protein, transcript knockdown,
    tested mutants and cell shedding are distinct evidence levels.
  target_ids:
  - traitmech:000731
  evidence_ids:
  - mechanism
  - identity
  outcome: supported
- assessment_id: mutation
  area: provenance
  topic: Guarded curation and repaired source receipt
  summary: 'Writer/history safeguards preserve prior records; #1944 is resolved by
    measured and regression-tested receipt compaction, not by dropping scientific
    evidence.'
  target_ids:
  - traitmech:000731
  evidence_ids:
  - implementation
  - provenance
  outcome: supported
- assessment_id: products
  area: consistency
  topic: Proposal RDF and generated artifacts
  summary: One canonical class row, correct w3id parent chain and role-correct definition
    annotation; pages/dashboard match 1126 records with prior scientific bytes preserved.
  target_ids:
  - traitmech:000731
  evidence_ids:
  - novelty
  - products
  outcome: supported
- assessment_id: limits
  area: completeness
  topic: Authority, mechanisms and source access
  summary: Canonical taxa, molecular graph, exact mappings and broader comparative
    mechanism remain unresolved. Unread supplements and source-access failures remain
    explicit rather than claimed absence.
  target_ids:
  - traitmech:000731
  evidence_ids:
  - identity
  - provenance
  - mechanism
  outcome: unknown
findings:
- finding_id: receipt-inventory
  issue_key: flagellar-autotomy-receipt-inventory
  category: provenance
  severity: minor
  status: resolved
  certainty: confirmed
  target_ids:
  - traitmech:000731
  field_paths:
  - allocation.full_range_check.owners
  evidence_ids:
  - provenance
  - implementation
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: research/traits/physiology/eukaryotic_flagellar_autotomy-source-verification.json
    role: maintained_source_receipt
  title: Complete temporary search inventory embedded in tracked summary
  description: '74,366,222 bytes and 184,357 owner objects exceed the intended compact
    provenance summary. No change to biological claims is required. GitHub issue #1944
    tracks this prepublication defect.'
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261015T081900Z-flagellar-autotomy-receipt
    finding_id: receipt-inventory
  disposition_reason: Count 184357 and complete local audit SHA-256 replace the embedded
    array. Receipt reduced from 74366222 to 13023 bytes; structured comparison preserves
    all other content. Regression rejects original bytes and accepts the correction;
    full native gates pass.
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/1944
actions: []
related_reviews:
- repository: CultureBotAI/TraitMech
  review_id: 20261015T081900Z-flagellar-autotomy-receipt
  relationship: Resolves the same receipt-inventory finding and adds the complete
    bounded scientific assessment.
limitations:
- Author self-review; no human scientific sign-off or independent-laboratory replication
  implied.
- Main 2003 and 2016 papers were read during research; relevant quoted pages and methodological
  text were reread. 2016 supplements remain unread and supplementary index MD5 differs;
  nine substantive assets matched.
- 2012 main HTML and six figures were read earlier. Fresh formal-review HTML access
  returned a challenge page; retained Figure 5 was reread. No full PDF, supplements
  or new successful full-text acquisition claimed.
- Bounded notice checks do not establish comprehensive correction/retraction clearance.
  Native NOT_IN_ABSTRACT does not independently verify a full-text quote.
- No raw-data reanalysis, canonical strain/taxon, universal p60/FA/TRP15/IFT/calcium
  mechanism or exact external equivalence is inferred.
- Known-copy searches and local audit hashes are bounded and temporary files are not
  guaranteed permanent availability. No claim of literature exhaustion or atomic reservation.
- Configured embeddings unavailable; existing artifacts retained. No paid research
  used.
links:
- https://github.com/CultureBotAI/TraitMech/issues/1944
tags:
- add-trait
- flagellar-autotomy
- self-review
```
