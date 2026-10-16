# Bacterial flagellar filament internalization: bounded adversarial assessment

- Review: 20261016T025010Z-bacterial-flagellar-filament-internalization
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-16T02:13:30Z
- Finished UTC: 2026-10-16T02:50:10Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Own-filament withdrawal into bacterial cell-body periplasm is supported by one primary experiment and a distinct author perspective. No actionable curation defect found in this scope. 4837 full-suite tests passed; four discussions remain OPEN and status stays PROPOSED.

## Scope And Provenance

Complete new record, guarded writer/tests, evidence receipt, proposal v611, history and generated surfaces.

Selection: Exact traitmech:000735 and its maintained owners; no sampling.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 55dd57432329dc99afb0ba152b391e4f7e17f4e7.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| traitmech:000735 | data/traits/physiology/bacterial_flagellar_filament_internalization.yaml | maintained | bacterial flagellar filament internalization |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/add_bacterial_flagellar_filament_internalization_trait.py | passed | True | traitmech:000735 | Executed on the captured content. Corpus checks are not a corpus-wide scientific review. Authority identifiers without adapters remain skipped, not verified. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/add_bacterial_flagellar_filament_internalization_trait.py --apply | passed | True | traitmech:000735 | Executed on the captured content. Corpus checks are not a corpus-wide scientific review. Authority identifiers without adapters remain skipped, not verified. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/add_bacterial_flagellar_filament_internalization_trait.py --apply | passed | True | traitmech:000735 | Executed on the captured content. Corpus checks are not a corpus-wide scientific review. Authority identifiers without adapters remain skipped, not verified. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python -m pytest -q tests/test_add_bacterial_flagellar_filament_internalization_trait.py | passed | True | traitmech:000735 | Executed on the captured content. Corpus checks are not a corpus-wide scientific review. Authority identifiers without adapters remain skipped, not verified. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/new_history_record.py --kind record --slug bacterial_flagellar_filament_internalization --target-root data/traits/physiology --event CREATE --outcome changed --sections identity,evidence,discussions --summary 'Add bacterial flagellar filament internalization' --details 'Added one PROPOSED own-flagellar-filament withdrawal phenotype with primary DOI:10.1038/s41564-023-01401-2 and author-perspective DOI:10.1063/pt.nkma.bqid. Checked 11/13-word full-text excerpts; the perspective describes the same experiment, not independent replication. Kept DOI:10.1111/j.1365-2958.2006.05081.x and its 14-word excerpt as comparison context with NO_EVIDENCE, not a definition citation. Preserved native NOT_IN_ABSTRACT/UNRESOLVED/NOT_IN_ABSTRACT. Reserved traitmech:000735, v611 and full block 1068800-1068899 after ignored/hidden current-file, retained-history, complete-range and open/draft PR checks plus fresh state guard. Preserved partial-withdrawal, frozen-stage, scale-bar and preparation limits. No canonical taxon, exact synonym/xref or universal molecular graph is asserted. Per-record timestamp is the observed allocation decision, not source acquisition.' --actor-name codex --model GPT-5 --agent-tool Codex | passed | True | traitmech:000735 | Executed on the captured content. Corpus checks are not a corpus-wide scientific review. Authority identifiers without adapters remain skipped, not verified. |
| just fetch-record-review-bases --apply | passed | True | traitmech:000735 | Executed on the captured content. Corpus checks are not a corpus-wide scientific review. Authority identifiers without adapters remain skipped, not verified. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/verify_snippets.py --record data/traits/physiology/bacterial_flagellar_filament_internalization.yaml --out /tmp/traitmech-bacterial-internalization-checks-20261016/native-network.tsv | passed | True | traitmech:000735 | Executed on the captured content. Corpus checks are not a corpus-wide scientific review. Authority identifiers without adapters remain skipped, not verified. |
| just verify-proposal metpo_traitmech_v611 | passed | True | traitmech:000735 | Executed on the captured content. Corpus checks are not a corpus-wide scientific review. Authority identifiers without adapters remain skipped, not verified. |
| just robot-validate-proposal metpo_traitmech_v611 | passed | True | traitmech:000735 | Executed on the captured content. Corpus checks are not a corpus-wide scientific review. Authority identifiers without adapters remain skipped, not verified. |
| just audit-proposals | passed | True | traitmech:000735 | Executed on the captured content. Corpus checks are not a corpus-wide scientific review. Authority identifiers without adapters remain skipped, not verified. |
| just ground-predicates | passed | True | traitmech:000735 | Executed on the captured content. Corpus checks are not a corpus-wide scientific review. Authority identifiers without adapters remain skipped, not verified. |
| just ground-nodes | passed | True | traitmech:000735 | Executed on the captured content. Corpus checks are not a corpus-wide scientific review. Authority identifiers without adapters remain skipped, not verified. |
| just audit-graphs | passed | True | traitmech:000735 | Executed on the captured content. Corpus checks are not a corpus-wide scientific review. Authority identifiers without adapters remain skipped, not verified. |
| just audit-graph-protein-taxa | passed | True | traitmech:000735 | Executed on the captured content. Corpus checks are not a corpus-wide scientific review. Authority identifiers without adapters remain skipped, not verified. |
| just audit-predicate-domains | passed | True | traitmech:000735 | Executed on the captured content. Corpus checks are not a corpus-wide scientific review. Authority identifiers without adapters remain skipped, not verified. |
| just check-biolink-coverage | passed | True | traitmech:000735 | Executed on the captured content. Corpus checks are not a corpus-wide scientific review. Authority identifiers without adapters remain skipped, not verified. |
| just audit-snippets | passed | True | traitmech:000735 | Executed on the captured content. Corpus checks are not a corpus-wide scientific review. Authority identifiers without adapters remain skipped, not verified. |
| just gen-discussions-data | passed | True | traitmech:000735 | Executed on the captured content. Corpus checks are not a corpus-wide scientific review. Authority identifiers without adapters remain skipped, not verified. |
| just gen-qc-dashboard | passed | True | traitmech:000735 | Executed on the captured content. Corpus checks are not a corpus-wide scientific review. Authority identifiers without adapters remain skipped, not verified. |
| just gen-pages | passed | True | traitmech:000735 | Executed on the captured content. Corpus checks are not a corpus-wide scientific review. Authority identifiers without adapters remain skipped, not verified. |
| just gen-priority-dashboard | passed | True | traitmech:000735 | Executed on the captured content. Corpus checks are not a corpus-wide scientific review. Authority identifiers without adapters remain skipped, not verified. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python -m pytest -q tests/test_add_bacterial_flagellar_filament_internalization_trait.py tests/test_readme_artifacts.py tests/test_trait_priority.py tests/test_qc_dashboard_artifacts.py | passed | True | traitmech:000735 | Executed on the captured content. Corpus checks are not a corpus-wide scientific review. Authority identifiers without adapters remain skipped, not verified. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/ruff check src scripts tests | passed | True | traitmech:000735 | Executed on the captured content. Corpus checks are not a corpus-wide scientific review. Authority identifiers without adapters remain skipped, not verified. |
| just qc | passed | True | traitmech:000735 | Executed on the captured content. Corpus checks are not a corpus-wide scientific review. Authority identifiers without adapters remain skipped, not verified. |
| just validate-history | passed | True | traitmech:000735 | Executed on the captured content. Corpus checks are not a corpus-wide scientific review. Authority identifiers without adapters remain skipped, not verified. |
| just validate-products | passed | True | traitmech:000735 | Executed on the captured content. Corpus checks are not a corpus-wide scientific review. Authority identifiers without adapters remain skipped, not verified. |
| just verify-proposal metpo_traitmech_v611 | passed | True | traitmech:000735 | Executed on the captured content. Corpus checks are not a corpus-wide scientific review. Authority identifiers without adapters remain skipped, not verified. |
| just robot-validate-proposal metpo_traitmech_v611 | passed | True | traitmech:000735 | Executed on the captured content. Corpus checks are not a corpus-wide scientific review. Authority identifiers without adapters remain skipped, not verified. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/audit_canonical_examples.py --no-resolve | passed | True | traitmech:000735 | Executed on the captured content. Corpus checks are not a corpus-wide scientific review. Authority identifiers without adapters remain skipped, not verified. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/run_trait_graph_audit.py --verify | passed | True | traitmech:000735 | Executed on the captured content. Corpus checks are not a corpus-wide scientific review. Authority identifiers without adapters remain skipped, not verified. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/audit_history_records.py --base aa5f955e20f904859dfd7016a1ffb7fce039c0c7 | passed | True | traitmech:000735 | Executed on the captured content. Corpus checks are not a corpus-wide scientific review. Authority identifiers without adapters remain skipped, not verified. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python -m pytest -q --junitxml=/tmp/traitmech-bacterial-internalization-checks-20261016/pytest.xml | passed | True | traitmech:000735 | Executed on the captured content. Corpus checks are not a corpus-wide scientific review. Authority identifiers without adapters remain skipped, not verified. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate -s src/traitmech/schema/traitmech.yaml --target-class TraitRecord data/traits/physiology/bacterial_flagellar_filament_internalization.yaml | passed | True | traitmech:000735 | Native record/history validation passed. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/validate_strict.py data/traits/physiology/bacterial_flagellar_filament_internalization.yaml | passed | True | traitmech:000735 | Native record/history validation passed. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/validate_history_links.py history/records/bacterial_flagellar_filament_internalization | passed | True | traitmech:000735 | Native record/history validation passed. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/verify_snippets.py --record data/traits/physiology/bacterial_flagellar_filament_internalization.yaml --out /tmp/traitmech-bacterial-internalization-checks-20261016/native.tsv | failed | False | traitmech:000735 | Initial live citation attempt failed sandbox DNS for all three references and proved nothing. This failed attempt is retained; the required network-enabled snippet-retry-0 succeeded with NOT_IN_ABSTRACT/UNRESOLVED/NOT_IN_ABSTRACT. No unavailable final requirement is waived. |
| committed-inputs | passed | True | traitmech:000735 | All captured input hashes also match the exact committed checkpoint. Inspection retains its native working_tree attestation; this additional byte comparison is explicit. |
| preservation | passed | True | traitmech:000735 | All 1129 prior records, protected spore germination, prior histories/reviews/proposals, embeddings, shared templates and snippet baseline remain byte-identical. Existing trait pages change only in corpus footer except the phenotype child link/count, 207 to 208. |
| rdf | passed | True | traitmech:000735 | Actual RDF contains 15/12628/12632 triples. Correct w3id child-parent-quality chain; the definition annotation contains only the local record and DOI:10.1038/s41564-023-01401-2, not the context citation. No legacy OBO METPO parent stub. |
| browser | passed | True | traitmech:000735 | 1440- and 390-pixel browser checks confirm the local identifier, two supporting excerpts, one context excerpt, four OPEN discussions, history, browse search/navigation and 1130-record dashboard image without horizontal overflow or page errors. Actual desktop/mobile screenshots and dashboard images were inspected. |
| whitespace | passed | True | traitmech:000735 | Ordinary staged diff check reported only required trailing empty ROBOT directive cells. Verified 11-column layout, exact-template exception and ordinary checks for every other path passed; no global whitespace setting weakened. |
| Configured embedding source paths | not_applicable | False | traitmech:000735 | Neither exact configured source exists in main or owned layout. Existing artifacts retained, not rebuilt. Generator source matched 645 pinned blobs. |
| Structured expression-module evidence | not_applicable | False | traitmech:000735 | No gene, locus, protein, regulator or expression-module assertion is curated. Expression membership would not establish this structural withdrawal phenotype; no adapter call or negative dataset result is claimed. |

## Scientific And Domain Assessments

### Own assembled filament withdrawal

identity: supported. Targets: traitmech:000735.

The primary microscopy interpretation and author perspective directly support movement into the predator cell-body periplasm. Partial withdrawal is included; static endoflagella and an external sheath lumen do not establish this transition.

### Phenotype parent and apparatus boundaries

grounding: supported. Targets: traitmech:000735.

The broader phenotype parent imposes no locomotion requirement. External ejection, eukaryotic axoneme withdrawal and static flagellar arrangement are not exact equivalents. No disjoint-organism, exact synonym or external-equivalence assertion is added.

### Source roles, strains and observation units

evidence: supported. Targets: traitmech:000735.

The 2024 author perspective cites the same 2023 experiment; it is not independent replication. HD100 minicell-enriched stages are not pooled with 109J retained-filament observations. Feature counts and selected bdelloplast proportions are not culture replicates or internalization frequencies.

### No universal dynamics or degradation model

scope: supported. Targets: traitmech:000735.

Frozen tomograms provide no same-cell timing. Motor displacement, ring separation, sheath zippering, lipid effects, digestion and vesicle origin are not universal defining requirements. No force, rate, protease or recycling inference is made from sequence or a segmented image.

### Earlier retained flagella constrain universal timing

consistency: supported. Targets: traitmech:000735.

External retention in early 109J bdelloplasts does not measure own-periplasmic internalization or rule out later/partial withdrawal. The source is correctly stored as NO_EVIDENCE comparison context with an explanation, not definition support.

### Guarded first-pass curation and products

representation: supported. Targets: traitmech:000735.

Writer guards, native history, canonical proposal headers, role-correct definition annotation, generated products and corpus preservation checks agree. Existing add-trait guidance covers the interpretation and evidence-role risks; no skill update is warranted by this unit.

### Mechanism, taxon authority and upstream review

completeness: unknown. Targets: traitmech:000735.

Canonical strain provenance/representative state, protein-resolved mechanism and ontology equivalence remain open. Linked post-publication review and other media remain unread. No human sign-off or comprehensive notice clearance is implied.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| source-0 | DOI:10.1038/s41564-023-01401-2; PMC11061892.1 Results S3, Attachment of B. bacteriovorus to prey; Figure 3; Discussion S6 and Methods S8-S9 | supports | Kaplan et al. 2023, PMID:37349588, PMC11061892.1, Results S3, Attachment of B. bacteriovorus to prey, paragraph beginning In cells with larger portions. Direct manuscript JATS match; native NOT_IN_ABSTRACT retained. Source strain HD100 and frozen cryo-ET stages support partial through nearly complete withdrawal into the predator's own periplasm, not the prey's. Methods S8-S12 qualify minicell enrichment and possible physiology effects; the images contain no same-cell temporal information. Main Figure 3 and supplement PDF pages 1, 22-35, 66-67 were visually inspected. S20-S21 distinguish external and internal filament portions; S22 is a schematic, not a tracked trajectory. Table S2's 8/4/30 early/intermediate/late absorbed-flagellum observations are not culture replicates or a prevalence denominator. Publisher Figure 3's main scale bar is 100 nm, versus 50 nm in the manuscript caption; no dimension or rate is inferred. Main PDF, other actual main figures, unselected supplemental images and movies remain unread. Later breakage or degradation is not required by the definition. Formal review reread complete S3/S6/S8/S9 and Figure 3 caption plus actual publisher Figure 3. Earlier Methods S10-S12, S17 and selected supplement readings remain bounded research observations, not a claim to have read every asset. Timestamp records cached-byte recheck, not new acquisition. |
| source-1 | DOI:10.1063/pt.nkma.bqid; Direct publisher HTML, Disassembly processes, Figure 5 caption and reference 16 | supports | Kaplan 2024, Physics Today, Figure 5 caption; contiguous span checked in directly retrieved publisher HTML. Disassembly processes and reference 16 were read, and actual Figure 5 was inspected. This is a distinct author-perspective publication describing the same 2023 experiment, not independent experimental replication. The colored segmentation is not another experiment. Native UNRESOLVED means no usable abstract was returned, not that the DOI is invalid; Crossref identity and direct publisher wording were checked separately. Presumed digestion and the hypothesized evolutionary connection to spirochaete endoflagella are not defining requirements or established consequences. Formal review reread that section and reference 16 and inspected actual Figure 5. Classified as author-perspective authority, not another primary experiment. Timestamp records cached-byte recheck, not new acquisition. |
| source-2 | DOI:10.1111/j.1365-2958.2006.05081.x; PMC1453311.1 Results, Flagella are not always shed upon prey entry; Table 1 and actual Figure 1 | context_only | Lambert et al. 2006, PMID:16573680, PMC1453311.1, Results, Flagella are not always shed upon prey entry. Direct JATS match; native NOT_IN_ABSTRACT retained. 109J predators were examined with flagella-minus E. coli DFB225 prey. The approximately 80% of more than 100 assessable early bdelloplasts excludes aggregates and may overestimate the whole-population proportion; its complement is not an internalization frequency. Actual Figure 1 was viewed at 456 by 390 pixels. Its 20-minute time is after mixing, not an invasion or withdrawal duration; 1% PTA staining differs from the 2023 cryo-ET preparation. Other actual figures, supplementary figures and main PDF remain unread. Formal review reread the complete Results subsection with Table 1 and viewed actual Figure 1. Context only, not support for own-periplasmic withdrawal or a third definition citation. Timestamp records cached-byte recheck, not new acquisition. |
| identity | data/traits/physiology/bacterial_flagellar_filament_internalization.yaml; Complete record, four OPEN discussions and curation history | supports | A reusable own-assembled-filament withdrawal phenotype, not a static structure, sequence feature or predator invasion into another cell. Partial withdrawal counts; complete withdrawal, permanent intactness and disjoint organisms are not asserted. |
| implementation | scripts/add_bacterial_flagellar_filament_internalization_trait.py; Whole writer, focused tests and CREATE history | supports | Explicit apply, prevalidation, deep copies, hash-guarded canonical proposal headers and exact-content refusal protect later curation. Dry run/apply/replay and refusal tests passed; no protected record or prior history was changed. |
| novelty | proposals/metpo_traitmech_v611/proposal.md; Hierarchy, deprecated identifiers, evidence roles and reservation | supports | Phenotype METPO:1000059 is broader by definition. Active flagellated and axially filamented denote possession/location under motility, not withdrawal. Neighboring ejection and eukaryotic intact-axoneme internalization have different endpoints/apparatus. Deprecated flagellation identifiers are not revived or used as exact xrefs; ontology pin is unchanged. |
| provenance | research/traits/physiology/bacterial_flagellar_filament_internalization-source-verification.json; Source identities, hashes, access limits and metadata checks | supports | Two distinct supporting citations, one primary experiment. All three native outcomes remain distinct from direct full-text matching and claim support. Frozen stages, preparation differences, scale-bar discrepancy and selected-asset coverage remain explicit. Qualified MED and Crossref notice fields are not comprehensive clearance. |
| allocation | research/traits/physiology/bacterial_flagellar_filament_internalization-allocation.json; Accepted allocation and final state guard | supports | Reserved 000735, v611 and full block 1068800-1068899 after biological acceptance and ignored/hidden, retained-history, complete-range and open/draft PR assessments. Numeric embedding cells and broad editor envelopes were excluded with explicit dispositions. The timestamp records the allocation action, not source acquisition. |
| products | reports/proposal_citation_audit.tsv; Native generated outputs, RDF and browser checks | supports | 1130 records; exactly two supporting citations counted for this addition. Definition authority and comparison-only source remain separate. Generated local identity, discussion evidence, history and counts are consistent with the maintained record. |

## Limits And Additional Notes

- Author self-review of one record, not independent experimental replication, human approval or corpus-wide scientific review.
- 2023 main Figure 3 and 17 selected supplement pages were inspected during research; formal review reread S3/S6/S8/S9 and the caption and actual Figure 3. Main PDF, other actual main figures, unselected supplement images, movies, peer responses and raw data remain unread.
- 2024 is an author perspective about the same experiment. Actual Figure 5 is a segmentation, not an independent experiment; presumed digestion and proposed evolutionary significance are not established consequences.
- 2006 Results/Table 1 and actual Figure 1 were reread. Other actual figures, supplements and main PDF remain unread. Retention is context, not a negative internalization assay.
- Native NOT_IN_ABSTRACT/UNRESOLVED outcomes are not biological verification. Initial sandbox DNS failure is retained separately from the successful network retry. Metadata and returned notice fields are bounded; linked post-publication review remains unread.
- Known-copy novelty/reservation checks are bounded, non-atomic and not literature exhaustion. A separate external-wrapping research lead is not part of this record or its evidence.
- Configured embedding sources unavailable; existing artifacts retained. Authority IDs without adapters remain skipped. Temporary cached sources may not remain available.
- Required external PR reviews, exact-head CI, native queue checks and saved-review check/test after saving are separate publication gates. No paid research or raw-data reanalysis.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261016T025010Z-bacterial-flagellar-filament-internalization
kind: record
repository: CultureBotAI/TraitMech
title: 'Bacterial flagellar filament internalization: bounded adversarial assessment'
started_at: '2026-10-16T02:13:30Z'
finished_at: '2026-10-16T02:50:10Z'
reviewer:
  identity: codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Author falsification-oriented source review. Not independent
    review or human scientific approval; external review requests and CI do not change
    attribution.
skill: .claude/skills/add-trait/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Own-filament withdrawal into bacterial cell-body periplasm is supported by
  one primary experiment and a distinct author perspective. No actionable curation
  defect found in this scope. 4837 full-suite tests passed; four discussions remain
  OPEN and status stays PROPOSED.
source:
  git_revision: 55dd57432329dc99afb0ba152b391e4f7e17f4e7
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
    sha256: 79a3456ae9da9f025a8bfc47df64c57c1bdcc94eb54a4f4d7b7724bf98d6bd01
    role: context
  - path: app/dashboard/priority.json
    sha256: 2f4368fad8e763fbc8e1ca46452aa1ea24cd1992cd886989645dc7efb879acfb
    role: context
  - path: app/discussions/data.js
    sha256: 60b479daf40f83d1339ac167e069c3c514b6264834079514f4edc572b994d6f7
    role: context
  - path: conf/evidence_snippet_baseline.tsv
    sha256: cbe5c82379e796446366b292f15194d80625b928119b482a67d857a379ab31a7
    role: context
  - path: dashboard/coverage.png
    sha256: 4ce2697dc100f5bf8ce4c5691390a39f12ef36dcc42770985aed93fe16caa53b
    role: context
  - path: dashboard/index.html
    sha256: 7da516655f5c1313b9af936d22e7e7277896f7f678152fcb08fd6156123764f9
    role: context
  - path: data/raw/metpo.owl
    sha256: 8b6f8fe0510a698579e532658c8ace05da2550093365df9ca83feb0741778415
    role: context
  - path: data/traits/morphology/axially_filamented.yaml
    sha256: bbfff2a29558906f76ad4f5573eb070fb7e8134f9ec6e0bdba95b788699d434f
    role: context
  - path: data/traits/morphology/flagellated.yaml
    sha256: ef50cfb498de5c66a4f2fb904a2038f4c97fa2615e6090a652758051ad25250b
    role: context
  - path: data/traits/physiology/bacterial_flagellar_filament_internalization.yaml
    sha256: 486a69330a59f4ead6378103fe2f796a98a314ac5c1fbbed2f528ccb040fa31d
    role: target
  - path: data/traits/physiology/bacterial_polar_flagellar_ejection.yaml
    sha256: 6db8657e3504202ba495f77be2487d63c479c433a032d81f93cbf522d0dcf007
    role: context
  - path: data/traits/physiology/eukaryotic_flagellar_axoneme_internalization.yaml
    sha256: e16e6a6d660b7d51ab966d9f4e76039d6dbf44e04715f240296e380142bd0158
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
  - path: history/records/bacterial_flagellar_filament_internalization/2026-10-16T014354Z-codex-c19380.yaml
    sha256: e356af0edc7c46cddc64ff508d3c70e6fe943be3de55744ade4aa95f64fd6dc3
    role: context
  - path: pages/browse.html
    sha256: ccfc9f63153ae28a8dd04779566c77f98f7981d310a2de8a9c5faf4db6d0f8af
    role: context
  - path: pages/traits/physiology/bacterial_flagellar_filament_internalization.html
    sha256: 2a004d47103a2d415419ac68ffa007caa4f01e91fd0cff376fa09b3b2ba6ceb6
    role: context
  - path: pages/traits/upper/phenotype.html
    sha256: 9ac777366a80cce9bae102715b0bbbad5380d1efaad8f44e28d1661ae766162a
    role: context
  - path: proposals/metpo_traitmech_v610/metpo_proposal_classes_robot.tsv
    sha256: 77d0147f395fe730a2830a0e73a470f7e0cde0d27bc730fa2c7ac5434fc3d7f7
    role: context
  - path: proposals/metpo_traitmech_v611/metpo_proposal_classes_robot.tsv
    sha256: bcb05dca3c188e249909b1cd902ea07a64047c4dae4d03d3c904e0c6aaafb0c2
    role: context
  - path: proposals/metpo_traitmech_v611/proposal.md
    sha256: fd89ac9e07bfdca345b3250099b052ad047e4758e8b36ae3aff8005343ab9aca
    role: context
  - path: reports/proposal_citation_audit.tsv
    sha256: 30ac102ff44feb4267256f92d1b8a5628b7556d67c0a2d6099a52b61869d4ee8
    role: context
  - path: research/traits/physiology/bacterial_flagellar_filament_internalization-allocation.json
    sha256: a23cee3e54a2075352cdbf4032a972803044d664889cbcd62689d55762103a02
    role: context
  - path: research/traits/physiology/bacterial_flagellar_filament_internalization-source-verification.json
    sha256: 5ad954ddec31293e3c45a6d12eb8cdde21dae56d0351ccb36b2a17bb29665c8d
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/add_bacterial_flagellar_filament_internalization_trait.py
    sha256: 078e7adc11022800e35901390d73e45b42e425504bf6ce2bade5365eb72e0e58
    role: context
  - path: src/traitmech/schema/traitmech.yaml
    sha256: 46c47fc627b80ccbba1e8ab3fb6f2aee93bc2aef7aaf72fe9aadc3257f2c02dd
    role: context
  - path: src/traitmech/templates/trait.html
    sha256: 00b07955f2d9bf860ff9ffa9fbffe679e1b7a0d7710e95a88fc02eb5e4a07def
    role: context
  - path: tests/test_add_bacterial_flagellar_filament_internalization_trait.py
    sha256: 8ff5514920f3b7b7f8b2bdc570de16cc31b9000133489ea37b226d8d7c7d9180
    role: context
targets:
- target_id: traitmech:000735
  path: data/traits/physiology/bacterial_flagellar_filament_internalization.yaml
  label: bacterial flagellar filament internalization
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: scripts/add_bacterial_flagellar_filament_internalization_trait.py
    role: Guarded writer of the maintained trait and proposal
scope:
  description: Complete new record, guarded writer/tests, evidence receipt, proposal
    v611, history and generated surfaces.
  selection: Exact traitmech:000735 and its maintained owners; no sampling.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - traitmech:000735
  exclusions:
  - target: Other 1129 records
    reason: Automated corpus checks and byte preservation, not a fresh scientific
      review.
  - target: data/traits/physiology/spore_germination.yaml
    reason: Protected by DO_NOT_WORK; unchanged and not curated.
checks:
- check_id: write-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/add_bacterial_flagellar_filament_internalization_trait.py
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/add_bacterial_flagellar_filament_internalization_trait.py
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000735
  summary: Executed on the captured content. Corpus checks are not a corpus-wide scientific
    review. Authority identifiers without adapters remain skipped, not verified.
- check_id: write-1
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/add_bacterial_flagellar_filament_internalization_trait.py --apply
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/add_bacterial_flagellar_filament_internalization_trait.py --apply
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000735
  summary: Executed on the captured content. Corpus checks are not a corpus-wide scientific
    review. Authority identifiers without adapters remain skipped, not verified.
- check_id: write-2
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/add_bacterial_flagellar_filament_internalization_trait.py --apply
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/add_bacterial_flagellar_filament_internalization_trait.py --apply
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000735
  summary: Executed on the captured content. Corpus checks are not a corpus-wide scientific
    review. Authority identifiers without adapters remain skipped, not verified.
- check_id: writer-tests-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q tests/test_add_bacterial_flagellar_filament_internalization_trait.py
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q tests/test_add_bacterial_flagellar_filament_internalization_trait.py
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000735
  summary: Executed on the captured content. Corpus checks are not a corpus-wide scientific
    review. Authority identifiers without adapters remain skipped, not verified.
- check_id: history-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/new_history_record.py --kind record --slug bacterial_flagellar_filament_internalization
    --target-root data/traits/physiology --event CREATE --outcome changed --sections
    identity,evidence,discussions --summary 'Add bacterial flagellar filament internalization'
    --details 'Added one PROPOSED own-flagellar-filament withdrawal phenotype with
    primary DOI:10.1038/s41564-023-01401-2 and author-perspective DOI:10.1063/pt.nkma.bqid.
    Checked 11/13-word full-text excerpts; the perspective describes the same experiment,
    not independent replication. Kept DOI:10.1111/j.1365-2958.2006.05081.x and its
    14-word excerpt as comparison context with NO_EVIDENCE, not a definition citation.
    Preserved native NOT_IN_ABSTRACT/UNRESOLVED/NOT_IN_ABSTRACT. Reserved traitmech:000735,
    v611 and full block 1068800-1068899 after ignored/hidden current-file, retained-history,
    complete-range and open/draft PR checks plus fresh state guard. Preserved partial-withdrawal,
    frozen-stage, scale-bar and preparation limits. No canonical taxon, exact synonym/xref
    or universal molecular graph is asserted. Per-record timestamp is the observed
    allocation decision, not source acquisition.' --actor-name codex --model GPT-5
    --agent-tool Codex
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/new_history_record.py --kind record --slug bacterial_flagellar_filament_internalization
    --target-root data/traits/physiology --event CREATE --outcome changed --sections
    identity,evidence,discussions --summary 'Add bacterial flagellar filament internalization'
    --details 'Added one PROPOSED own-flagellar-filament withdrawal phenotype with
    primary DOI:10.1038/s41564-023-01401-2 and author-perspective DOI:10.1063/pt.nkma.bqid.
    Checked 11/13-word full-text excerpts; the perspective describes the same experiment,
    not independent replication. Kept DOI:10.1111/j.1365-2958.2006.05081.x and its
    14-word excerpt as comparison context with NO_EVIDENCE, not a definition citation.
    Preserved native NOT_IN_ABSTRACT/UNRESOLVED/NOT_IN_ABSTRACT. Reserved traitmech:000735,
    v611 and full block 1068800-1068899 after ignored/hidden current-file, retained-history,
    complete-range and open/draft PR checks plus fresh state guard. Preserved partial-withdrawal,
    frozen-stage, scale-bar and preparation limits. No canonical taxon, exact synonym/xref
    or universal molecular graph is asserted. Per-record timestamp is the observed
    allocation decision, not source acquisition.' --actor-name codex --model GPT-5
    --agent-tool Codex
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000735
  summary: Executed on the captured content. Corpus checks are not a corpus-wide scientific
    review. Authority identifiers without adapters remain skipped, not verified.
- check_id: prepare-0
  name: just fetch-record-review-bases --apply
  command: just fetch-record-review-bases --apply
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000735
  summary: Executed on the captured content. Corpus checks are not a corpus-wide scientific
    review. Authority identifiers without adapters remain skipped, not verified.
- check_id: snippet-retry-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/verify_snippets.py --record data/traits/physiology/bacterial_flagellar_filament_internalization.yaml
    --out /tmp/traitmech-bacterial-internalization-checks-20261016/native-network.tsv
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/verify_snippets.py --record data/traits/physiology/bacterial_flagellar_filament_internalization.yaml
    --out /tmp/traitmech-bacterial-internalization-checks-20261016/native-network.tsv
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000735
  summary: Executed on the captured content. Corpus checks are not a corpus-wide scientific
    review. Authority identifiers without adapters remain skipped, not verified.
- check_id: proposal-0
  name: just verify-proposal metpo_traitmech_v611
  command: just verify-proposal metpo_traitmech_v611
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000735
  summary: Executed on the captured content. Corpus checks are not a corpus-wide scientific
    review. Authority identifiers without adapters remain skipped, not verified.
- check_id: proposal-1
  name: just robot-validate-proposal metpo_traitmech_v611
  command: just robot-validate-proposal metpo_traitmech_v611
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000735
  summary: Executed on the captured content. Corpus checks are not a corpus-wide scientific
    review. Authority identifiers without adapters remain skipped, not verified.
- check_id: generate-0
  name: just audit-proposals
  command: just audit-proposals
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000735
  summary: Executed on the captured content. Corpus checks are not a corpus-wide scientific
    review. Authority identifiers without adapters remain skipped, not verified.
- check_id: generate-1
  name: just ground-predicates
  command: just ground-predicates
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000735
  summary: Executed on the captured content. Corpus checks are not a corpus-wide scientific
    review. Authority identifiers without adapters remain skipped, not verified.
- check_id: generate-2
  name: just ground-nodes
  command: just ground-nodes
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000735
  summary: Executed on the captured content. Corpus checks are not a corpus-wide scientific
    review. Authority identifiers without adapters remain skipped, not verified.
- check_id: generate-3
  name: just audit-graphs
  command: just audit-graphs
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000735
  summary: Executed on the captured content. Corpus checks are not a corpus-wide scientific
    review. Authority identifiers without adapters remain skipped, not verified.
- check_id: generate-4
  name: just audit-graph-protein-taxa
  command: just audit-graph-protein-taxa
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000735
  summary: Executed on the captured content. Corpus checks are not a corpus-wide scientific
    review. Authority identifiers without adapters remain skipped, not verified.
- check_id: generate-5
  name: just audit-predicate-domains
  command: just audit-predicate-domains
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000735
  summary: Executed on the captured content. Corpus checks are not a corpus-wide scientific
    review. Authority identifiers without adapters remain skipped, not verified.
- check_id: generate-6
  name: just check-biolink-coverage
  command: just check-biolink-coverage
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000735
  summary: Executed on the captured content. Corpus checks are not a corpus-wide scientific
    review. Authority identifiers without adapters remain skipped, not verified.
- check_id: generate-7
  name: just audit-snippets
  command: just audit-snippets
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000735
  summary: Executed on the captured content. Corpus checks are not a corpus-wide scientific
    review. Authority identifiers without adapters remain skipped, not verified.
- check_id: generate-8
  name: just gen-discussions-data
  command: just gen-discussions-data
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000735
  summary: Executed on the captured content. Corpus checks are not a corpus-wide scientific
    review. Authority identifiers without adapters remain skipped, not verified.
- check_id: generate-9
  name: just gen-qc-dashboard
  command: just gen-qc-dashboard
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000735
  summary: Executed on the captured content. Corpus checks are not a corpus-wide scientific
    review. Authority identifiers without adapters remain skipped, not verified.
- check_id: generate-10
  name: just gen-pages
  command: just gen-pages
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000735
  summary: Executed on the captured content. Corpus checks are not a corpus-wide scientific
    review. Authority identifiers without adapters remain skipped, not verified.
- check_id: generate-11
  name: just gen-priority-dashboard
  command: just gen-priority-dashboard
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000735
  summary: Executed on the captured content. Corpus checks are not a corpus-wide scientific
    review. Authority identifiers without adapters remain skipped, not verified.
- check_id: focused-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q tests/test_add_bacterial_flagellar_filament_internalization_trait.py
    tests/test_readme_artifacts.py tests/test_trait_priority.py tests/test_qc_dashboard_artifacts.py
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q tests/test_add_bacterial_flagellar_filament_internalization_trait.py
    tests/test_readme_artifacts.py tests/test_trait_priority.py tests/test_qc_dashboard_artifacts.py
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000735
  summary: Executed on the captured content. Corpus checks are not a corpus-wide scientific
    review. Authority identifiers without adapters remain skipped, not verified.
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
  - traitmech:000735
  summary: Executed on the captured content. Corpus checks are not a corpus-wide scientific
    review. Authority identifiers without adapters remain skipped, not verified.
- check_id: verify-0
  name: just qc
  command: just qc
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000735
  summary: Executed on the captured content. Corpus checks are not a corpus-wide scientific
    review. Authority identifiers without adapters remain skipped, not verified.
- check_id: verify-1
  name: just validate-history
  command: just validate-history
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000735
  summary: Executed on the captured content. Corpus checks are not a corpus-wide scientific
    review. Authority identifiers without adapters remain skipped, not verified.
- check_id: verify-2
  name: just validate-products
  command: just validate-products
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000735
  summary: Executed on the captured content. Corpus checks are not a corpus-wide scientific
    review. Authority identifiers without adapters remain skipped, not verified.
- check_id: verify-3
  name: just verify-proposal metpo_traitmech_v611
  command: just verify-proposal metpo_traitmech_v611
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000735
  summary: Executed on the captured content. Corpus checks are not a corpus-wide scientific
    review. Authority identifiers without adapters remain skipped, not verified.
- check_id: verify-4
  name: just robot-validate-proposal metpo_traitmech_v611
  command: just robot-validate-proposal metpo_traitmech_v611
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000735
  summary: Executed on the captured content. Corpus checks are not a corpus-wide scientific
    review. Authority identifiers without adapters remain skipped, not verified.
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
  - traitmech:000735
  summary: Executed on the captured content. Corpus checks are not a corpus-wide scientific
    review. Authority identifiers without adapters remain skipped, not verified.
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
  - traitmech:000735
  summary: Executed on the captured content. Corpus checks are not a corpus-wide scientific
    review. Authority identifiers without adapters remain skipped, not verified.
- check_id: verify-7
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/audit_history_records.py --base aa5f955e20f904859dfd7016a1ffb7fce039c0c7
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/audit_history_records.py --base aa5f955e20f904859dfd7016a1ffb7fce039c0c7
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000735
  summary: Executed on the captured content. Corpus checks are not a corpus-wide scientific
    review. Authority identifiers without adapters remain skipped, not verified.
- check_id: tests-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q --junitxml=/tmp/traitmech-bacterial-internalization-checks-20261016/pytest.xml
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q --junitxml=/tmp/traitmech-bacterial-internalization-checks-20261016/pytest.xml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000735
  summary: Executed on the captured content. Corpus checks are not a corpus-wide scientific
    review. Authority identifiers without adapters remain skipped, not verified.
- check_id: records-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate
    -s src/traitmech/schema/traitmech.yaml --target-class TraitRecord data/traits/physiology/bacterial_flagellar_filament_internalization.yaml
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate
    -s src/traitmech/schema/traitmech.yaml --target-class TraitRecord data/traits/physiology/bacterial_flagellar_filament_internalization.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000735
  summary: Native record/history validation passed.
- check_id: records-1
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_strict.py data/traits/physiology/bacterial_flagellar_filament_internalization.yaml
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_strict.py data/traits/physiology/bacterial_flagellar_filament_internalization.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000735
  summary: Native record/history validation passed.
- check_id: records-2
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_history_links.py history/records/bacterial_flagellar_filament_internalization
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_history_links.py history/records/bacterial_flagellar_filament_internalization
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000735
  summary: Native record/history validation passed.
- check_id: records-3
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/verify_snippets.py --record data/traits/physiology/bacterial_flagellar_filament_internalization.yaml
    --out /tmp/traitmech-bacterial-internalization-checks-20261016/native.tsv
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/verify_snippets.py --record data/traits/physiology/bacterial_flagellar_filament_internalization.yaml
    --out /tmp/traitmech-bacterial-internalization-checks-20261016/native.tsv
  status: failed
  required: false
  exit_code: 2
  expected_exit_code: 0
  target_ids:
  - traitmech:000735
  summary: Initial live citation attempt failed sandbox DNS for all three references
    and proved nothing. This failed attempt is retained; the required network-enabled
    snippet-retry-0 succeeded with NOT_IN_ABSTRACT/UNRESOLVED/NOT_IN_ABSTRACT. No
    unavailable final requirement is waived.
- check_id: committed-inputs
  name: committed-inputs
  status: passed
  required: true
  target_ids:
  - traitmech:000735
  summary: All captured input hashes also match the exact committed checkpoint. Inspection
    retains its native working_tree attestation; this additional byte comparison is
    explicit.
- check_id: preservation
  name: preservation
  status: passed
  required: true
  target_ids:
  - traitmech:000735
  summary: All 1129 prior records, protected spore germination, prior histories/reviews/proposals,
    embeddings, shared templates and snippet baseline remain byte-identical. Existing
    trait pages change only in corpus footer except the phenotype child link/count,
    207 to 208.
- check_id: rdf
  name: rdf
  status: passed
  required: true
  target_ids:
  - traitmech:000735
  summary: Actual RDF contains 15/12628/12632 triples. Correct w3id child-parent-quality
    chain; the definition annotation contains only the local record and DOI:10.1038/s41564-023-01401-2,
    not the context citation. No legacy OBO METPO parent stub.
- check_id: browser
  name: browser
  status: passed
  required: true
  target_ids:
  - traitmech:000735
  summary: 1440- and 390-pixel browser checks confirm the local identifier, two supporting
    excerpts, one context excerpt, four OPEN discussions, history, browse search/navigation
    and 1130-record dashboard image without horizontal overflow or page errors. Actual
    desktop/mobile screenshots and dashboard images were inspected.
- check_id: whitespace
  name: whitespace
  status: passed
  required: true
  target_ids:
  - traitmech:000735
  summary: Ordinary staged diff check reported only required trailing empty ROBOT
    directive cells. Verified 11-column layout, exact-template exception and ordinary
    checks for every other path passed; no global whitespace setting weakened.
- check_id: embedding-inputs
  name: Configured embedding source paths
  status: not_applicable
  required: false
  target_ids:
  - traitmech:000735
  summary: Neither exact configured source exists in main or owned layout. Existing
    artifacts retained, not rebuilt. Generator source matched 645 pinned blobs.
- check_id: imodulondb
  name: Structured expression-module evidence
  status: not_applicable
  required: false
  target_ids:
  - traitmech:000735
  summary: No gene, locus, protein, regulator or expression-module assertion is curated.
    Expression membership would not establish this structural withdrawal phenotype;
    no adapter call or negative dataset result is claimed.
evidence:
- evidence_id: source-0
  kind: primary_source
  reference: DOI:10.1038/s41564-023-01401-2
  locator: PMC11061892.1 Results S3, Attachment of B. bacteriovorus to prey; Figure
    3; Discussion S6 and Methods S8-S9
  accessed_at: '2026-10-16T02:50:10Z'
  support: supports
  snapshot_sha256: 6288c2a9aa29a833565e2c0561f3ef2237856971d8da54e5a2c12947649eaee4
  summary: Kaplan et al. 2023, PMID:37349588, PMC11061892.1, Results S3, Attachment
    of B. bacteriovorus to prey, paragraph beginning In cells with larger portions.
    Direct manuscript JATS match; native NOT_IN_ABSTRACT retained. Source strain HD100
    and frozen cryo-ET stages support partial through nearly complete withdrawal into
    the predator's own periplasm, not the prey's. Methods S8-S12 qualify minicell
    enrichment and possible physiology effects; the images contain no same-cell temporal
    information. Main Figure 3 and supplement PDF pages 1, 22-35, 66-67 were visually
    inspected. S20-S21 distinguish external and internal filament portions; S22 is
    a schematic, not a tracked trajectory. Table S2's 8/4/30 early/intermediate/late
    absorbed-flagellum observations are not culture replicates or a prevalence denominator.
    Publisher Figure 3's main scale bar is 100 nm, versus 50 nm in the manuscript
    caption; no dimension or rate is inferred. Main PDF, other actual main figures,
    unselected supplemental images and movies remain unread. Later breakage or degradation
    is not required by the definition. Formal review reread complete S3/S6/S8/S9 and
    Figure 3 caption plus actual publisher Figure 3. Earlier Methods S10-S12, S17
    and selected supplement readings remain bounded research observations, not a claim
    to have read every asset. Timestamp records cached-byte recheck, not new acquisition.
- evidence_id: source-1
  kind: authority
  reference: DOI:10.1063/pt.nkma.bqid
  locator: Direct publisher HTML, Disassembly processes, Figure 5 caption and reference
    16
  accessed_at: '2026-10-16T02:50:10Z'
  support: supports
  snapshot_sha256: c80795701cc34a52d70dcbe7aeb52653c8d1ace7b8b19a0c1ee380e7de6a1755
  summary: Kaplan 2024, Physics Today, Figure 5 caption; contiguous span checked in
    directly retrieved publisher HTML. Disassembly processes and reference 16 were
    read, and actual Figure 5 was inspected. This is a distinct author-perspective
    publication describing the same 2023 experiment, not independent experimental
    replication. The colored segmentation is not another experiment. Native UNRESOLVED
    means no usable abstract was returned, not that the DOI is invalid; Crossref identity
    and direct publisher wording were checked separately. Presumed digestion and the
    hypothesized evolutionary connection to spirochaete endoflagella are not defining
    requirements or established consequences. Formal review reread that section and
    reference 16 and inspected actual Figure 5. Classified as author-perspective authority,
    not another primary experiment. Timestamp records cached-byte recheck, not new
    acquisition.
- evidence_id: source-2
  kind: primary_source
  reference: DOI:10.1111/j.1365-2958.2006.05081.x
  locator: PMC1453311.1 Results, Flagella are not always shed upon prey entry; Table
    1 and actual Figure 1
  accessed_at: '2026-10-16T02:50:10Z'
  support: context_only
  snapshot_sha256: 13b4024c10eed886fa3e86480d109d0adf532259d258feb9a018a7e2f0026ebc
  summary: Lambert et al. 2006, PMID:16573680, PMC1453311.1, Results, Flagella are
    not always shed upon prey entry. Direct JATS match; native NOT_IN_ABSTRACT retained.
    109J predators were examined with flagella-minus E. coli DFB225 prey. The approximately
    80% of more than 100 assessable early bdelloplasts excludes aggregates and may
    overestimate the whole-population proportion; its complement is not an internalization
    frequency. Actual Figure 1 was viewed at 456 by 390 pixels. Its 20-minute time
    is after mixing, not an invasion or withdrawal duration; 1% PTA staining differs
    from the 2023 cryo-ET preparation. Other actual figures, supplementary figures
    and main PDF remain unread. Formal review reread the complete Results subsection
    with Table 1 and viewed actual Figure 1. Context only, not support for own-periplasmic
    withdrawal or a third definition citation. Timestamp records cached-byte recheck,
    not new acquisition.
- evidence_id: identity
  kind: record_content
  reference: data/traits/physiology/bacterial_flagellar_filament_internalization.yaml
  locator: Complete record, four OPEN discussions and curation history
  accessed_at: '2026-10-16T02:50:10Z'
  support: supports
  snapshot_sha256: 486a69330a59f4ead6378103fe2f796a98a314ac5c1fbbed2f528ccb040fa31d
  summary: A reusable own-assembled-filament withdrawal phenotype, not a static structure,
    sequence feature or predator invasion into another cell. Partial withdrawal counts;
    complete withdrawal, permanent intactness and disjoint organisms are not asserted.
- evidence_id: implementation
  kind: record_content
  reference: scripts/add_bacterial_flagellar_filament_internalization_trait.py
  locator: Whole writer, focused tests and CREATE history
  accessed_at: '2026-10-16T02:50:10Z'
  support: supports
  snapshot_sha256: 078e7adc11022800e35901390d73e45b42e425504bf6ce2bade5365eb72e0e58
  summary: Explicit apply, prevalidation, deep copies, hash-guarded canonical proposal
    headers and exact-content refusal protect later curation. Dry run/apply/replay
    and refusal tests passed; no protected record or prior history was changed.
- evidence_id: novelty
  kind: search
  reference: proposals/metpo_traitmech_v611/proposal.md
  locator: Hierarchy, deprecated identifiers, evidence roles and reservation
  accessed_at: '2026-10-16T02:50:10Z'
  support: supports
  snapshot_sha256: fd89ac9e07bfdca345b3250099b052ad047e4758e8b36ae3aff8005343ab9aca
  summary: Phenotype METPO:1000059 is broader by definition. Active flagellated and
    axially filamented denote possession/location under motility, not withdrawal.
    Neighboring ejection and eukaryotic intact-axoneme internalization have different
    endpoints/apparatus. Deprecated flagellation identifiers are not revived or used
    as exact xrefs; ontology pin is unchanged.
  search_scope: Allocation included ignored/hidden files across 213 known locations,
    310 retained heads, 89818 TraitMech and 9308 CommunityMech unique regular Git
    blobs. Twelve copies were unavailable, including the deliberately removed prior-unit
    worktree; both independent recovery clones were included. Of 324 biological contexts,
    307 inherited byte-matched assessments and all 17 new contexts were read. All
    76 local allocation contexts were broad editor envelopes. Complete ranges covered
    211271 owner contexts and 2627 unique contents; all 32 matching contents were
    assessed. Twelve open/draft PRs, 784 nonremoved changed blobs and 587 selected
    upstream blobs were checked. Eight prior matching pages were byte-identical; two
    new matching owners concern nutrient uptake and flagellin-associated EET. Three
    exact numeric matches were parsed as decimal embedding cells. Worktree/source/upstream/PR
    state was stable at allocation. Publication refresh remains a separate pre-push
    gate. Lost ignored history, symlink targets, arbitrary archives and unchanged
    PR files are not reconstructed; no global absence or literature exhaustion is
    claimed.
- evidence_id: provenance
  kind: record_content
  reference: research/traits/physiology/bacterial_flagellar_filament_internalization-source-verification.json
  locator: Source identities, hashes, access limits and metadata checks
  accessed_at: '2026-10-16T02:50:10Z'
  support: supports
  snapshot_sha256: 5ad954ddec31293e3c45a6d12eb8cdde21dae56d0351ccb36b2a17bb29665c8d
  summary: Two distinct supporting citations, one primary experiment. All three native
    outcomes remain distinct from direct full-text matching and claim support. Frozen
    stages, preparation differences, scale-bar discrepancy and selected-asset coverage
    remain explicit. Qualified MED and Crossref notice fields are not comprehensive
    clearance.
- evidence_id: allocation
  kind: record_content
  reference: research/traits/physiology/bacterial_flagellar_filament_internalization-allocation.json
  locator: Accepted allocation and final state guard
  accessed_at: '2026-10-16T02:50:10Z'
  support: supports
  snapshot_sha256: a23cee3e54a2075352cdbf4032a972803044d664889cbcd62689d55762103a02
  summary: Reserved 000735, v611 and full block 1068800-1068899 after biological acceptance
    and ignored/hidden, retained-history, complete-range and open/draft PR assessments.
    Numeric embedding cells and broad editor envelopes were excluded with explicit
    dispositions. The timestamp records the allocation action, not source acquisition.
- evidence_id: products
  kind: validation
  reference: reports/proposal_citation_audit.tsv
  locator: Native generated outputs, RDF and browser checks
  accessed_at: '2026-10-16T02:50:10Z'
  support: supports
  snapshot_sha256: 30ac102ff44feb4267256f92d1b8a5628b7556d67c0a2d6099a52b61869d4ee8
  summary: 1130 records; exactly two supporting citations counted for this addition.
    Definition authority and comparison-only source remain separate. Generated local
    identity, discussion evidence, history and counts are consistent with the maintained
    record.
assessments:
- assessment_id: identity
  area: identity
  topic: Own assembled filament withdrawal
  summary: The primary microscopy interpretation and author perspective directly support
    movement into the predator cell-body periplasm. Partial withdrawal is included;
    static endoflagella and an external sheath lumen do not establish this transition.
  target_ids:
  - traitmech:000735
  evidence_ids:
  - identity
  - source-0
  - source-1
  outcome: supported
- assessment_id: parent
  area: grounding
  topic: Phenotype parent and apparatus boundaries
  summary: The broader phenotype parent imposes no locomotion requirement. External
    ejection, eukaryotic axoneme withdrawal and static flagellar arrangement are not
    exact equivalents. No disjoint-organism, exact synonym or external-equivalence
    assertion is added.
  target_ids:
  - traitmech:000735
  evidence_ids:
  - identity
  - novelty
  - allocation
  outcome: supported
- assessment_id: evidence
  area: evidence
  topic: Source roles, strains and observation units
  summary: The 2024 author perspective cites the same 2023 experiment; it is not independent
    replication. HD100 minicell-enriched stages are not pooled with 109J retained-filament
    observations. Feature counts and selected bdelloplast proportions are not culture
    replicates or internalization frequencies.
  target_ids:
  - traitmech:000735
  evidence_ids:
  - source-0
  - source-1
  - source-2
  - provenance
  outcome: supported
- assessment_id: mechanism
  area: scope
  topic: No universal dynamics or degradation model
  summary: Frozen tomograms provide no same-cell timing. Motor displacement, ring
    separation, sheath zippering, lipid effects, digestion and vesicle origin are
    not universal defining requirements. No force, rate, protease or recycling inference
    is made from sequence or a segmented image.
  target_ids:
  - traitmech:000735
  evidence_ids:
  - identity
  - source-0
  - source-1
  outcome: supported
- assessment_id: context
  area: consistency
  topic: Earlier retained flagella constrain universal timing
  summary: External retention in early 109J bdelloplasts does not measure own-periplasmic
    internalization or rule out later/partial withdrawal. The source is correctly
    stored as NO_EVIDENCE comparison context with an explanation, not definition support.
  target_ids:
  - traitmech:000735
  evidence_ids:
  - source-2
  - identity
  - products
  outcome: supported
- assessment_id: implementation
  area: representation
  topic: Guarded first-pass curation and products
  summary: Writer guards, native history, canonical proposal headers, role-correct
    definition annotation, generated products and corpus preservation checks agree.
    Existing add-trait guidance covers the interpretation and evidence-role risks;
    no skill update is warranted by this unit.
  target_ids:
  - traitmech:000735
  evidence_ids:
  - implementation
  - products
  - allocation
  outcome: supported
- assessment_id: gaps
  area: completeness
  topic: Mechanism, taxon authority and upstream review
  summary: Canonical strain provenance/representative state, protein-resolved mechanism
    and ontology equivalence remain open. Linked post-publication review and other
    media remain unread. No human sign-off or comprehensive notice clearance is implied.
  target_ids:
  - traitmech:000735
  evidence_ids:
  - provenance
  - identity
  outcome: unknown
findings: []
actions: []
limitations:
- Author self-review of one record, not independent experimental replication, human
  approval or corpus-wide scientific review.
- 2023 main Figure 3 and 17 selected supplement pages were inspected during research;
  formal review reread S3/S6/S8/S9 and the caption and actual Figure 3. Main PDF,
  other actual main figures, unselected supplement images, movies, peer responses
  and raw data remain unread.
- 2024 is an author perspective about the same experiment. Actual Figure 5 is a segmentation,
  not an independent experiment; presumed digestion and proposed evolutionary significance
  are not established consequences.
- 2006 Results/Table 1 and actual Figure 1 were reread. Other actual figures, supplements
  and main PDF remain unread. Retention is context, not a negative internalization
  assay.
- Native NOT_IN_ABSTRACT/UNRESOLVED outcomes are not biological verification. Initial
  sandbox DNS failure is retained separately from the successful network retry. Metadata
  and returned notice fields are bounded; linked post-publication review remains unread.
- Known-copy novelty/reservation checks are bounded, non-atomic and not literature
  exhaustion. A separate external-wrapping research lead is not part of this record
  or its evidence.
- Configured embedding sources unavailable; existing artifacts retained. Authority
  IDs without adapters remain skipped. Temporary cached sources may not remain available.
- Required external PR reviews, exact-head CI, native queue checks and saved-review
  check/test after saving are separate publication gates. No paid research or raw-data
  reanalysis.
links:
- https://doi.org/10.1038/s41564-023-01401-2
- https://doi.org/10.1063/pt.nkma.bqid
- https://doi.org/10.1111/j.1365-2958.2006.05081.x
tags:
- add-trait
- flagellar-internalization
- self-review
```
