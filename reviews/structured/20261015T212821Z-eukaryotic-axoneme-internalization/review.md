# Eukaryotic flagellar axoneme internalization: complete corrected assessment

- Review: 20261015T212821Z-eukaryotic-axoneme-internalization
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-15T21:15:05Z
- Finished UTC: 2026-10-15T21:28:21Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The bounded own-axoneme internalization phenotype has two supporting primary publications. One minor source-locator finding is resolved. Four discussions remain OPEN; mapping status remains PROPOSED.

## Scope And Provenance

Complete new trait, maintained writer/tests, source evidence, v610 proposal, histories and generated surfaces after locator correction.

Selection: Exact traitmech:000734 and maintained owners; no sampling.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 31c475c24eb1c52aaf10e7ae6262b9895a683ea1.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| traitmech:000734 | data/traits/physiology/eukaryotic_flagellar_axoneme_internalization.yaml | maintained | eukaryotic flagellar axoneme internalization |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/add_eukaryotic_flagellar_axoneme_internalization_trait.py --correct-expansion-locator | passed | True | traitmech:000734 | Executed on the corrected working tree/checkpoint. Corpus validation is not corpus-wide scientific review. Product IDs without authority adapters remain skipped, not verified. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/add_eukaryotic_flagellar_axoneme_internalization_trait.py --correct-expansion-locator --apply | passed | True | traitmech:000734 | Executed on the corrected working tree/checkpoint. Corpus validation is not corpus-wide scientific review. Product IDs without authority adapters remain skipped, not verified. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/add_eukaryotic_flagellar_axoneme_internalization_trait.py --correct-expansion-locator --apply | passed | True | traitmech:000734 | Executed on the corrected working tree/checkpoint. Corpus validation is not corpus-wide scientific review. Product IDs without authority adapters remain skipped, not verified. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/new_history_record.py --kind record --slug eukaryotic_flagellar_axoneme_internalization --target-root data/traits/physiology --event EDIT --outcome changed --sections discussions --summary 'Correct the expansion-factor source locator' --details 'Corrected discussions[0].evidence[0].notes and the guarded writer: the 2025 value 5.5 +/- 0.2 is in Results S6, MTOC remodeling from mitosis to ciliogenesis, first paragraph, citing Supplemental Figure S3A-B, not Methods/S3B. Cached JATS S6 and S15 and actual Figure S3 were reread. Preserved the 4.5 versus 5.5 discrepancy, biological definition, supporting sources, excerpts, native verdicts, proposal and prior research/history/review observations. This supplements history/records/eukaryotic_flagellar_axoneme_internalization/2026-10-15T201607Z-codex-b269cd.yaml. Issue #1950 tracks the locator correction and successor review.' --actor-name codex --model GPT-5 --agent-tool Codex --issue https://github.com/CultureBotAI/TraitMech/issues/1950 | passed | True | traitmech:000734 | Executed on the corrected working tree/checkpoint. Corpus validation is not corpus-wide scientific review. Product IDs without authority adapters remain skipped, not verified. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate -s src/traitmech/schema/traitmech.yaml --target-class TraitRecord data/traits/physiology/eukaryotic_flagellar_axoneme_internalization.yaml | passed | True | traitmech:000734 | Executed on the corrected working tree/checkpoint. Corpus validation is not corpus-wide scientific review. Product IDs without authority adapters remain skipped, not verified. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/validate_strict.py data/traits/physiology/eukaryotic_flagellar_axoneme_internalization.yaml | passed | True | traitmech:000734 | Executed on the corrected working tree/checkpoint. Corpus validation is not corpus-wide scientific review. Product IDs without authority adapters remain skipped, not verified. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/validate_history_links.py history/records/eukaryotic_flagellar_axoneme_internalization | passed | True | traitmech:000734 | Executed on the corrected working tree/checkpoint. Corpus validation is not corpus-wide scientific review. Product IDs without authority adapters remain skipped, not verified. |
| just audit-proposals | passed | True | traitmech:000734 | Executed on the corrected working tree/checkpoint. Corpus validation is not corpus-wide scientific review. Product IDs without authority adapters remain skipped, not verified. |
| just ground-predicates | passed | True | traitmech:000734 | Executed on the corrected working tree/checkpoint. Corpus validation is not corpus-wide scientific review. Product IDs without authority adapters remain skipped, not verified. |
| just ground-nodes | passed | True | traitmech:000734 | Executed on the corrected working tree/checkpoint. Corpus validation is not corpus-wide scientific review. Product IDs without authority adapters remain skipped, not verified. |
| just audit-graphs | passed | True | traitmech:000734 | Executed on the corrected working tree/checkpoint. Corpus validation is not corpus-wide scientific review. Product IDs without authority adapters remain skipped, not verified. |
| just audit-graph-protein-taxa | passed | True | traitmech:000734 | Executed on the corrected working tree/checkpoint. Corpus validation is not corpus-wide scientific review. Product IDs without authority adapters remain skipped, not verified. |
| just audit-predicate-domains | passed | True | traitmech:000734 | Executed on the corrected working tree/checkpoint. Corpus validation is not corpus-wide scientific review. Product IDs without authority adapters remain skipped, not verified. |
| just check-biolink-coverage | passed | True | traitmech:000734 | Executed on the corrected working tree/checkpoint. Corpus validation is not corpus-wide scientific review. Product IDs without authority adapters remain skipped, not verified. |
| just audit-snippets | passed | True | traitmech:000734 | Executed on the corrected working tree/checkpoint. Corpus validation is not corpus-wide scientific review. Product IDs without authority adapters remain skipped, not verified. |
| just gen-discussions-data | passed | True | traitmech:000734 | Executed on the corrected working tree/checkpoint. Corpus validation is not corpus-wide scientific review. Product IDs without authority adapters remain skipped, not verified. |
| just gen-qc-dashboard | passed | True | traitmech:000734 | Executed on the corrected working tree/checkpoint. Corpus validation is not corpus-wide scientific review. Product IDs without authority adapters remain skipped, not verified. |
| just gen-pages | passed | True | traitmech:000734 | Executed on the corrected working tree/checkpoint. Corpus validation is not corpus-wide scientific review. Product IDs without authority adapters remain skipped, not verified. |
| just gen-priority-dashboard | passed | True | traitmech:000734 | Executed on the corrected working tree/checkpoint. Corpus validation is not corpus-wide scientific review. Product IDs without authority adapters remain skipped, not verified. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python -m pytest -q tests/test_add_eukaryotic_flagellar_axoneme_internalization_trait.py tests/test_readme_artifacts.py tests/test_qc_dashboard_artifacts.py | passed | True | traitmech:000734 | Executed on the corrected working tree/checkpoint. Corpus validation is not corpus-wide scientific review. Product IDs without authority adapters remain skipped, not verified. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/ruff check src scripts tests | passed | True | traitmech:000734 | Executed on the corrected working tree/checkpoint. Corpus validation is not corpus-wide scientific review. Product IDs without authority adapters remain skipped, not verified. |
| just qc | passed | True | traitmech:000734 | Executed on the corrected working tree/checkpoint. Corpus validation is not corpus-wide scientific review. Product IDs without authority adapters remain skipped, not verified. |
| just validate-history | passed | True | traitmech:000734 | Executed on the corrected working tree/checkpoint. Corpus validation is not corpus-wide scientific review. Product IDs without authority adapters remain skipped, not verified. |
| just validate-products | passed | True | traitmech:000734 | Executed on the corrected working tree/checkpoint. Corpus validation is not corpus-wide scientific review. Product IDs without authority adapters remain skipped, not verified. |
| just verify-proposal metpo_traitmech_v610 | passed | True | traitmech:000734 | Executed on the corrected working tree/checkpoint. Corpus validation is not corpus-wide scientific review. Product IDs without authority adapters remain skipped, not verified. |
| just robot-validate-proposal metpo_traitmech_v610 | passed | True | traitmech:000734 | Executed on the corrected working tree/checkpoint. Corpus validation is not corpus-wide scientific review. Product IDs without authority adapters remain skipped, not verified. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/audit_history_records.py --base a1db3a44599b96d564d7c3bd5ecc0ace19add76e | passed | True | traitmech:000734 | Executed on the corrected working tree/checkpoint. Corpus validation is not corpus-wide scientific review. Product IDs without authority adapters remain skipped, not verified. |
| prior-suite | passed | False | traitmech:000734 | 4817 tests passed at checkpoint 8886062340d71ebcec623416c3fffe37c8abe292. Full suite was not rerun after locator correction; post-correction focused/native gates and protected exact-head CI are separate. |
| preservation | passed | True | traitmech:000734 | Structured proof restores the original record exactly after reversing only the locator and removing the appended event. All 1128 prior records, protected spore germination, prior histories/reviews, source receipt, allocation, proposal, embeddings and shared templates remain preserved. |
| rdf | passed | True | traitmech:000734 | RDF contains 15/12628/12632 triples. Correct w3id child-parent-quality chain; definition annotation contains only the local record and DOI:10.1002/cm.21637. No legacy OBO parent stub; proposal unchanged by repair. |
| browser | passed | True | traitmech:000734 | Desktop/mobile checks at 1440 and 390 pixels confirm local identifier, two supporting excerpts, one context excerpt, four OPEN discussions, corrected locator in curation history, two history links, browse navigation and 1129-count dashboard image without overflow or page errors. An initial test incorrectly expected structured discussion notes in rendered body text; the unchanged template renders the explanation instead. That failed assumption was corrected and the test rerun, not counted as a pass. Screenshots were inspected separately. |
| whitespace | passed | True | traitmech:000734 | Initial ordinary staged check found only required trailing empty cells on the ROBOT directive row. Exact-template exception and all other paths passed. No global whitespace setting weakened; correction does not change the template. |
| allocation | passed | True | traitmech:000734 | Ignored/hidden-aware current, retained-history, complete-range and open/draft PR checks preceded allocation. Publication reassessment covered 211 known locations and 61263 current proposal-owner contexts; remote freshness remains a pre-push gate. |
| Configured embedding source paths | not_applicable | False | traitmech:000734 | Both exact configured sources absent in main and owned layouts. Existing artifacts retained, not rebuilt. Isolated shared generator matched 645 pinned source blobs. |

## Scientific And Domain Assessments

### Intact own-axoneme internalization

identity: supported. Targets: traitmech:000734.

Reusable physiological phenotype supported by the 2020 ultrastructural observations and distinct 2017 reported withdrawal. No gene/profile feature substitutes for an organism-level phenotype.

### Phenotype parent and apparatus boundaries

grounding: supported. Targets: traitmech:000734.

Definition-based parent is broader without requiring locomotion. Shortening by disassembly differs from intact withdrawal; later degradation can follow withdrawal. Bacterial periplasmic structures and pili are different apparatuses. No disjoint-organism axiom.

### Assay, source-role and media bounds

evidence: supported. Targets: traitmech:000734.

Fixed TEM/U-ExM stages are not same-cell trajectories. Selected completed retractions do not establish all-cell probabilities; sporangia and cultures are not retraction-event counts. Video metadata and caption timing remain separate; no rate inferred.

### No universal mechanism or recycling requirement

evidence: supported. Targets: traitmech:000734.

No universal reeling, lash-around, membrane-loss, actin/dynein/protease, cell-cycle stage, rate, complete degradation or recycling imposed. WASP/SCAR pseudopod perturbations do not establish the internalization mechanism.

### Corrected Results locator

provenance: supported. Targets: traitmech:000734.

Issue #1950 is fixed in both maintained notes with guarded repair and append-only provenance. Existing add-trait instructions already require accurate locators and successor reviews; this application error does not require another skill rule.

### Canonical proposal and rendered output

consistency: supported. Targets: traitmech:000734.

Role-correct definition annotation and w3id parent chain agree with the source-backed record. Local identity, snippets, discussions, histories and corpus totals render coherently.

### Authority, mechanism and upstream scope

completeness: unknown. Targets: traitmech:000734.

Canonical strain authority/natural provenance, protein-resolved mechanism, exact mappings and upstream eukaryotic scope remain open. Access and notice checks are bounded, not comprehensive clearance.

## Findings

### expansion-factor-locator: Context note locates the expansion factor in Methods instead of Results

minor / resolved / confirmed; issue key: axoneme-internalization-expansion-factor-locator.

The value is in Results S6, citing Supplemental Figure S3A-B. Methods/S3B is an inaccurate locator. This is a bounded provenance correction, not an identity or evidence-sufficiency failure.

Disposition: Both maintained notes now locate the value in Results S6 with Supplemental Figure S3A-B. Exact-preimage repair, dry run/apply/replay, refusal tests, appended provenance and relevant native gates pass. Biological claims, proposal and earlier observations are preserved.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| source-0 | DOI:10.1002/cm.21637; Results 2.2, TEM interpretation after Figure 2; https://pmc.ncbi.nlm.nih.gov/articles/PMC7944584/ | supports | Venard et al. 2020, PMID:33103844, PMCID:PMC7944584, Results 2.2, TEM interpretation paragraph following Figure 2. Contiguous span checked in direct PMC HTML; native NOT_IN_ABSTRACT retained. Live phase microscopy, fixed immunofluorescence and TEM concern Rhizoclosmatium globosum JEL800 and Spizellomyces punctatus DAOM BR117. Internalized cross-sections retain 9+2 architecture without a surrounding ciliary membrane; fixed TEM is not continuous same-cell tracking. Figure 1's 23 and 32 cells are selected retraction events, not biological-culture counts. Methods time zero is plating, whereas Figure 2's TEM caption says post-retraction; retain that timing discrepancy. Table 1 labels length/diameter with rate units unlike Table 2; no numerical conversion or rate is asserted here. Main text and all five actual main figures were inspected. The main PDF and actual supplemental PDFs/videos remain unread. Subsequent degradation is a separate phase, not a requirement for this internalization phenotype. Formal review reread actual Figure 2. The earlier direct HTML reading is retained; a later PMC CAPTCHA is not a successful retrieval. No local-HTML byte match or same-cell TEM tracking is claimed. Timestamp records cached-byte recheck, not new acquisition. |
| source-1 | DOI:10.1083/jcb.201701074; Discussion JATS s11, printed 1681/PDF page 9; Results s10 and Methods s20; https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5461030/fullTextXML | supports | Fritz-Laylin et al. 2017, PMID:28473602, PMCID:PMC5461030.1, Discussion JATS s11, printed page 1681, PDF page 9. Direct normalized JATS and typeset passage checked; native NOT_IN_ABSTRACT retained. Bd denotes Batrachochytrium dendrobatidis, source strain JEL423, with synchronized zoospores observed under the described confinement preparation. Results s10, Discussion s11 and Methods s20 were read, along with selected PDF pages. Video 5 was inspected through 16 sampled frames and one enlarged frame, not continuous playback or every-frame analysis. File metadata reports 10.1 seconds at nominal 10 fps, burned-in labels span 0-20 seconds, and the caption states 0.1-second acquisition with 20-fps playback. These are not silently reconciled; no retraction rate or replicate count is inferred. The paper's WASP/SCAR pseudopod experiments do not establish an axoneme-internalization mechanism. Formal review reread the complete s10/s11/s20 sections. Selected PDF pages and sampled video were read during research, not all pages or continuous video. Timestamp records cached-byte recheck, not new acquisition. |
| source-2 | DOI:10.1091/mbc.E24-12-0577; Results S7 and Figure 4C; expansion-factor value in Results S6, first paragraph, citing Supplemental Figure S3A-B; https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12659703/fullTextXML | supports | Long et al. 2025, PMID:40833813, PMCID:PMC12659703.2, Results S7, Centrioles shorten but are not degraded during ciliary disassembly, sentence following the coiled-complex observation; Figure 4C. Direct JATS match; native NOT_IN_ABSTRACT retained. R. globosum JEL800 fixed U-ExM stages are not longitudinal trajectories. Actual Figure 4, all supplement text and visual supplement pages 4, 7 and 8 were inspected. The main-text S2 pointer concerns a transcriptomic figure; the relevant centriole panels are S3F-H. Figure 4's caption gives about 4.5-fold expansion, versus 5.5 +/- 0.2 in Results S6 (Supplemental Figure S3A-B); no absolute-size conversion is inferred. Figure 4F counts 16, 3, 26 and 41 sporangia across categories from three to five independent experiments, not retraction events. The two-hour timeline is attributed to 2020, not a new measurement. Other actual main figures, the main PDF and other supplement pages were not visually inspected. The preprint is another version, not another study. Formal review reread S7, Figure 4 caption and actual image, S15 Methods, the S6 value paragraph and actual supplement page 4. This source supports later-degradation context only, not a third definition citation. Timestamp records cached-byte recheck, not new acquisition. |
| identity | data/traits/physiology/eukaryotic_flagellar_axoneme_internalization.yaml; Complete record and four OPEN discussions | supports | Own intact eukaryotic axoneme withdrawal into the cell body is distinct from static localization, foreign-material uptake, external coiling, shortening by disassembly alone, autotomy, bacterial ejection, periplasmic flagellar possession and pilus retraction. Subsequent degradation is allowed, not required; no organism-level disjointness asserted. |
| implementation | scripts/add_eukaryotic_flagellar_axoneme_internalization_trait.py; Whole writer, focused tests and both histories | supports | Explicit apply, prevalidation, deep copies, hash-guarded proposal header and exact-input repair protect later curation. Repair appends one event and normal first-pass mode refuses the corrected record. Status remains PROPOSED. |
| novelty | proposals/metpo_traitmech_v610/proposal.md; Identity, parent, obsolete identifiers and proposal | supports | Phenotype METPO:1000059 is broader by definition. Flagellar possession/arrangement/locomotion and neighboring resorption/autotomy/ejection records are not exact. Historical identifiers are not revived or used as exact xrefs; ontology pin unchanged. Microbial-eukaryote inclusion and obsolescence reason codes remain upstream questions. |
| provenance | research/traits/physiology/eukaryotic_flagellar_axoneme_internalization-source-verification.json; Source receipt with bounded access, metadata and notice checks | supports | Two distinct supporting publications, not two independently replicated laboratories. All three snippets retain native NOT_IN_ABSTRACT distinct from direct full-text matching and claim support. 2025 and its preprint are the same study; the unread linked 2017 editorial is not evidence. Earlier research receipt remains unchanged; a linked correction receipt supersedes only the erroneous locator. |
| correction | research/traits/physiology/eukaryotic_flagellar_axoneme_internalization-locator-correction.json; Locator correction and preserved predecessor hashes | supports | Issue #1950 corrects Methods/S3B to Results S6 (Supplemental Figure S3A-B). Source values and the 4.5-versus-5.5 discrepancy remain unchanged. Original research/history/reviews are preserved. |
| products | reports/proposal_citation_audit.tsv; Native products, RDF and rendered surfaces | supports | 1129 records. Of prior trait pages, 1127 changed only in corpus footer; phenotype gained one child, 206 to 207. Follow-up changes target locator/history rendering and latest-curation metadata only, not corpus counts or proposal. |

## Limits And Additional Notes

- Author self-review, not human sign-off or independent-laboratory replication.
- 2020 main text and all five actual main figures were read during research; formal review reread Figure 2. Main PDF and actual supplementary PDFs/videos remain unread. Later PMC access returned CAPTCHA; supplement endpoint returned an XML error, not a ZIP.
- 2017 selected PDF pages and 16 sampled video frames plus one enlargement were inspected, not all pages, continuous playback or every-frame analysis. Formal review reread s10/s11/s20. Linked editorial content remains unread.
- 2025 text, actual Figure 4 and selected supplemental pages were inspected; other actual main figures and main PDF remain unread. Fixed stages are not trajectories. Preprint is not an independent study.
- Native NOT_IN_ABSTRACT outcomes are not independent biological verification. Metadata/notice fields do not provide comprehensive correction or retraction clearance.
- Full local suite covers the pre-correction checkpoint. Corrected focused/native gates are separate; protected exact-head CI and external reviews remain merge gates.
- Known-copy searches are bounded, not atomic reservation, global absence or literature exhaustion. Temporary assets may not remain available.
- Configured embedding sources unavailable; previous artifacts retained. No raw-data reanalysis or paid research.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T212821Z-eukaryotic-axoneme-internalization
kind: record
repository: CultureBotAI/TraitMech
title: 'Eukaryotic flagellar axoneme internalization: complete corrected assessment'
started_at: '2026-10-15T21:15:05Z'
finished_at: '2026-10-15T21:28:21Z'
reviewer:
  identity: codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Author falsification-oriented source review, not independent
    or human scientific approval. External review requests and CI do not change attribution.
skill: .claude/skills/add-trait/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The bounded own-axoneme internalization phenotype has two supporting primary
  publications. One minor source-locator finding is resolved. Four discussions remain
  OPEN; mapping status remains PROPOSED.
source:
  git_revision: 31c475c24eb1c52aaf10e7ae6262b9895a683ea1
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
    sha256: 9965185f98842b52951a5cd9c22242954a1ae7375f423f7f78b2db3b286f4692
    role: context
  - path: app/dashboard/priority.json
    sha256: 178a13b659b4d031472ccf72a0c28832088f8e98ce1682077367c23d7059b206
    role: context
  - path: app/discussions/data.js
    sha256: 4417529c8c0a0b9e46ccc1376ef73a3bfc719206e20544bf1aede7025941f64f
    role: context
  - path: conf/evidence_snippet_baseline.tsv
    sha256: cbe5c82379e796446366b292f15194d80625b928119b482a67d857a379ab31a7
    role: context
  - path: dashboard/coverage.png
    sha256: b0eea45176f150fcc695f8d57b1bc9626d6f38201940e83ddb858d7988415502
    role: context
  - path: dashboard/index.html
    sha256: 8d0af01b74176ff50af57419a5b6496847be2cb031ce3192a285d4fdbd5f68d6
    role: context
  - path: data/raw/metpo.owl
    sha256: 8b6f8fe0510a698579e532658c8ace05da2550093365df9ca83feb0741778415
    role: context
  - path: data/traits/morphology/flagellar_arrangement.yaml
    sha256: 1b944448f88de4fa9ff773e155866a2c592f7e843a4c7dc152534676d4e4f329
    role: context
  - path: data/traits/morphology/flagellated.yaml
    sha256: ef50cfb498de5c66a4f2fb904a2038f4c97fa2615e6090a652758051ad25250b
    role: context
  - path: data/traits/morphology/palmelloid_formation.yaml
    sha256: 6fec9c7538d049e5301536724aa6ce611e41ebfcdd8d32a9155eeba384eefe1a
    role: context
  - path: data/traits/physiology/bacterial_polar_flagellar_ejection.yaml
    sha256: 6db8657e3504202ba495f77be2487d63c479c433a032d81f93cbf522d0dcf007
    role: context
  - path: data/traits/physiology/eukaryotic_flagellar_autotomy.yaml
    sha256: e4d4924721768cd6c677b9cdc4781960a0526aa83537b182c7e9df1ba07f3bdc
    role: context
  - path: data/traits/physiology/eukaryotic_flagellar_axoneme_internalization.yaml
    sha256: e16e6a6d660b7d51ab966d9f4e76039d6dbf44e04715f240296e380142bd0158
    role: target
  - path: data/traits/physiology/eukaryotic_flagellar_resorption.yaml
    sha256: 9f87ec0e0e3eee6386f0e4937a9b98bcd5dd91ea713ea90874f4c3c7568f16fc
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
  - path: history/records/eukaryotic_flagellar_axoneme_internalization/2026-10-15T201607Z-codex-b269cd.yaml
    sha256: b487bf5eb69c2e7c3c500b1649b54d120ec83d8ac1b5bf2026e65c83659e7af5
    role: context
  - path: history/records/eukaryotic_flagellar_axoneme_internalization/2026-10-15T210641Z-codex-d719db.yaml
    sha256: c2e4a8ad12fabf9b657bab9a798ee5d750f975426b9e3f5669a02f4dfb15598b
    role: context
  - path: pages/browse.html
    sha256: 3b566bf1fb89c7239e868608c3e616acebcfb3b31ef4e2c7644f419bcf387790
    role: context
  - path: pages/traits/physiology/eukaryotic_flagellar_axoneme_internalization.html
    sha256: 92867dabb8e481eee642fde55d7235f669181dccd6a22880cc5c5969c8cf6f2d
    role: context
  - path: pages/traits/upper/phenotype.html
    sha256: 31eb2afa85fa15c9f8e263d5de56fec7d2bc9240aff524a3023326c612daf56e
    role: context
  - path: proposals/metpo_traitmech_v609/metpo_proposal_classes_robot.tsv
    sha256: ed4a62de23eee33700a4f731cf2068335e715d2c6d5c35d9f63412c20dbe0737
    role: context
  - path: proposals/metpo_traitmech_v610/metpo_proposal_classes_robot.tsv
    sha256: 77d0147f395fe730a2830a0e73a470f7e0cde0d27bc730fa2c7ac5434fc3d7f7
    role: context
  - path: proposals/metpo_traitmech_v610/proposal.md
    sha256: 34cfd5bca4fee5bfe5ca15cdc322fc69dbdc3c73f5fab2998801db90a1740b4c
    role: context
  - path: reports/proposal_citation_audit.tsv
    sha256: 8994c57399ce892f0a20040ff369dbb465d158d9365a547386afe5277e4cd00e
    role: context
  - path: research/traits/physiology/eukaryotic_flagellar_axoneme_internalization-allocation.json
    sha256: 9d41c69fa4c393f99587843b3241166d040b9f3371dfd0ddfd4607c50f597a0d
    role: context
  - path: research/traits/physiology/eukaryotic_flagellar_axoneme_internalization-locator-correction.json
    sha256: dc49007b33b334cbffabd3c95dc5aac3972ab29dc449b251cb6b96cf79e1c428
    role: context
  - path: research/traits/physiology/eukaryotic_flagellar_axoneme_internalization-source-verification.json
    sha256: 36ac8e5dfecfdf07e8090c334334277fe84754e6269008aebe364323e97ad49b
    role: context
  - path: reviews/structured/20261015T204954Z-axoneme-internalization-locator-finding/review.yaml
    sha256: c22ebb2377bd627a738a08ae0addda2a97dfa079ce997a1c0c3bbe45db6ca1fd
    role: context
  - path: scripts/add_eukaryotic_flagellar_axoneme_internalization_trait.py
    sha256: d88115bc3e0083657fde66af2ef3015740fcfe7426ee39327324e6824615198e
    role: context
  - path: src/traitmech/schema/traitmech.yaml
    sha256: 46c47fc627b80ccbba1e8ab3fb6f2aee93bc2aef7aaf72fe9aadc3257f2c02dd
    role: context
  - path: src/traitmech/templates/trait.html
    sha256: 00b07955f2d9bf860ff9ffa9fbffe679e1b7a0d7710e95a88fc02eb5e4a07def
    role: context
  - path: tests/test_add_eukaryotic_flagellar_axoneme_internalization_trait.py
    sha256: 36000d2f7bd120305395f6002c26715a02f5284723427807bdd04f4b5232fda3
    role: context
targets:
- target_id: traitmech:000734
  path: data/traits/physiology/eukaryotic_flagellar_axoneme_internalization.yaml
  label: eukaryotic flagellar axoneme internalization
  kind: maintained
  record_class: TraitRecord
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/physiology/eukaryotic_flagellar_axoneme_internalization.yaml
    role: curated_record
  - repository: CultureBotAI/TraitMech
    path: scripts/add_eukaryotic_flagellar_axoneme_internalization_trait.py
    role: guarded_writer
scope:
  description: Complete new trait, maintained writer/tests, source evidence, v610
    proposal, histories and generated surfaces after locator correction.
  selection: Exact traitmech:000734 and maintained owners; no sampling.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - traitmech:000734
  exclusions:
  - target: Other 1128 records
    reason: Automated corpus validation and byte preservation, not fresh scientific
      review.
  - target: data/traits/physiology/spore_germination.yaml
    reason: Protected by DO_NOT_WORK; unchanged and not curated.
checks:
- check_id: correction-write-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/add_eukaryotic_flagellar_axoneme_internalization_trait.py --correct-expansion-locator
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/add_eukaryotic_flagellar_axoneme_internalization_trait.py --correct-expansion-locator
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000734
  summary: Executed on the corrected working tree/checkpoint. Corpus validation is
    not corpus-wide scientific review. Product IDs without authority adapters remain
    skipped, not verified.
- check_id: correction-write-1
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/add_eukaryotic_flagellar_axoneme_internalization_trait.py --correct-expansion-locator
    --apply
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/add_eukaryotic_flagellar_axoneme_internalization_trait.py --correct-expansion-locator
    --apply
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000734
  summary: Executed on the corrected working tree/checkpoint. Corpus validation is
    not corpus-wide scientific review. Product IDs without authority adapters remain
    skipped, not verified.
- check_id: correction-write-2
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/add_eukaryotic_flagellar_axoneme_internalization_trait.py --correct-expansion-locator
    --apply
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/add_eukaryotic_flagellar_axoneme_internalization_trait.py --correct-expansion-locator
    --apply
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000734
  summary: Executed on the corrected working tree/checkpoint. Corpus validation is
    not corpus-wide scientific review. Product IDs without authority adapters remain
    skipped, not verified.
- check_id: correction-history-0
  name: '/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/new_history_record.py --kind record --slug eukaryotic_flagellar_axoneme_internalization
    --target-root data/traits/physiology --event EDIT --outcome changed --sections
    discussions --summary ''Correct the expansion-factor source locator'' --details
    ''Corrected discussions[0].evidence[0].notes and the guarded writer: the 2025
    value 5.5 +/- 0.2 is in Results S6, MTOC remodeling from mitosis to ciliogenesis,
    first paragraph, citing Supplemental Figure S3A-B, not Methods/S3B. Cached JATS
    S6 and S15 and actual Figure S3 were reread. Preserved the 4.5 versus 5.5 discrepancy,
    biological definition, supporting sources, excerpts, native verdicts, proposal
    and prior research/history/review observations. This supplements history/records/eukaryotic_flagellar_axoneme_internalization/2026-10-15T201607Z-codex-b269cd.yaml.
    Issue #1950 tracks the locator correction and successor review.'' --actor-name
    codex --model GPT-5 --agent-tool Codex --issue https://github.com/CultureBotAI/TraitMech/issues/1950'
  command: '/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/new_history_record.py --kind record --slug eukaryotic_flagellar_axoneme_internalization
    --target-root data/traits/physiology --event EDIT --outcome changed --sections
    discussions --summary ''Correct the expansion-factor source locator'' --details
    ''Corrected discussions[0].evidence[0].notes and the guarded writer: the 2025
    value 5.5 +/- 0.2 is in Results S6, MTOC remodeling from mitosis to ciliogenesis,
    first paragraph, citing Supplemental Figure S3A-B, not Methods/S3B. Cached JATS
    S6 and S15 and actual Figure S3 were reread. Preserved the 4.5 versus 5.5 discrepancy,
    biological definition, supporting sources, excerpts, native verdicts, proposal
    and prior research/history/review observations. This supplements history/records/eukaryotic_flagellar_axoneme_internalization/2026-10-15T201607Z-codex-b269cd.yaml.
    Issue #1950 tracks the locator correction and successor review.'' --actor-name
    codex --model GPT-5 --agent-tool Codex --issue https://github.com/CultureBotAI/TraitMech/issues/1950'
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000734
  summary: Executed on the corrected working tree/checkpoint. Corpus validation is
    not corpus-wide scientific review. Product IDs without authority adapters remain
    skipped, not verified.
- check_id: correction-records-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate
    -s src/traitmech/schema/traitmech.yaml --target-class TraitRecord data/traits/physiology/eukaryotic_flagellar_axoneme_internalization.yaml
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate
    -s src/traitmech/schema/traitmech.yaml --target-class TraitRecord data/traits/physiology/eukaryotic_flagellar_axoneme_internalization.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000734
  summary: Executed on the corrected working tree/checkpoint. Corpus validation is
    not corpus-wide scientific review. Product IDs without authority adapters remain
    skipped, not verified.
- check_id: correction-records-1
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_strict.py data/traits/physiology/eukaryotic_flagellar_axoneme_internalization.yaml
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_strict.py data/traits/physiology/eukaryotic_flagellar_axoneme_internalization.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000734
  summary: Executed on the corrected working tree/checkpoint. Corpus validation is
    not corpus-wide scientific review. Product IDs without authority adapters remain
    skipped, not verified.
- check_id: correction-records-2
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_history_links.py history/records/eukaryotic_flagellar_axoneme_internalization
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_history_links.py history/records/eukaryotic_flagellar_axoneme_internalization
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000734
  summary: Executed on the corrected working tree/checkpoint. Corpus validation is
    not corpus-wide scientific review. Product IDs without authority adapters remain
    skipped, not verified.
- check_id: correction-generate-0
  name: just audit-proposals
  command: just audit-proposals
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000734
  summary: Executed on the corrected working tree/checkpoint. Corpus validation is
    not corpus-wide scientific review. Product IDs without authority adapters remain
    skipped, not verified.
- check_id: correction-generate-1
  name: just ground-predicates
  command: just ground-predicates
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000734
  summary: Executed on the corrected working tree/checkpoint. Corpus validation is
    not corpus-wide scientific review. Product IDs without authority adapters remain
    skipped, not verified.
- check_id: correction-generate-2
  name: just ground-nodes
  command: just ground-nodes
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000734
  summary: Executed on the corrected working tree/checkpoint. Corpus validation is
    not corpus-wide scientific review. Product IDs without authority adapters remain
    skipped, not verified.
- check_id: correction-generate-3
  name: just audit-graphs
  command: just audit-graphs
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000734
  summary: Executed on the corrected working tree/checkpoint. Corpus validation is
    not corpus-wide scientific review. Product IDs without authority adapters remain
    skipped, not verified.
- check_id: correction-generate-4
  name: just audit-graph-protein-taxa
  command: just audit-graph-protein-taxa
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000734
  summary: Executed on the corrected working tree/checkpoint. Corpus validation is
    not corpus-wide scientific review. Product IDs without authority adapters remain
    skipped, not verified.
- check_id: correction-generate-5
  name: just audit-predicate-domains
  command: just audit-predicate-domains
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000734
  summary: Executed on the corrected working tree/checkpoint. Corpus validation is
    not corpus-wide scientific review. Product IDs without authority adapters remain
    skipped, not verified.
- check_id: correction-generate-6
  name: just check-biolink-coverage
  command: just check-biolink-coverage
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000734
  summary: Executed on the corrected working tree/checkpoint. Corpus validation is
    not corpus-wide scientific review. Product IDs without authority adapters remain
    skipped, not verified.
- check_id: correction-generate-7
  name: just audit-snippets
  command: just audit-snippets
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000734
  summary: Executed on the corrected working tree/checkpoint. Corpus validation is
    not corpus-wide scientific review. Product IDs without authority adapters remain
    skipped, not verified.
- check_id: correction-generate-8
  name: just gen-discussions-data
  command: just gen-discussions-data
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000734
  summary: Executed on the corrected working tree/checkpoint. Corpus validation is
    not corpus-wide scientific review. Product IDs without authority adapters remain
    skipped, not verified.
- check_id: correction-generate-9
  name: just gen-qc-dashboard
  command: just gen-qc-dashboard
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000734
  summary: Executed on the corrected working tree/checkpoint. Corpus validation is
    not corpus-wide scientific review. Product IDs without authority adapters remain
    skipped, not verified.
- check_id: correction-generate-10
  name: just gen-pages
  command: just gen-pages
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000734
  summary: Executed on the corrected working tree/checkpoint. Corpus validation is
    not corpus-wide scientific review. Product IDs without authority adapters remain
    skipped, not verified.
- check_id: correction-generate-11
  name: just gen-priority-dashboard
  command: just gen-priority-dashboard
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000734
  summary: Executed on the corrected working tree/checkpoint. Corpus validation is
    not corpus-wide scientific review. Product IDs without authority adapters remain
    skipped, not verified.
- check_id: correction-focused-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q tests/test_add_eukaryotic_flagellar_axoneme_internalization_trait.py
    tests/test_readme_artifacts.py tests/test_qc_dashboard_artifacts.py
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    -m pytest -q tests/test_add_eukaryotic_flagellar_axoneme_internalization_trait.py
    tests/test_readme_artifacts.py tests/test_qc_dashboard_artifacts.py
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000734
  summary: Executed on the corrected working tree/checkpoint. Corpus validation is
    not corpus-wide scientific review. Product IDs without authority adapters remain
    skipped, not verified.
- check_id: correction-focused-1
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/ruff
    check src scripts tests
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/ruff
    check src scripts tests
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000734
  summary: Executed on the corrected working tree/checkpoint. Corpus validation is
    not corpus-wide scientific review. Product IDs without authority adapters remain
    skipped, not verified.
- check_id: correction-verify-0
  name: just qc
  command: just qc
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000734
  summary: Executed on the corrected working tree/checkpoint. Corpus validation is
    not corpus-wide scientific review. Product IDs without authority adapters remain
    skipped, not verified.
- check_id: correction-verify-1
  name: just validate-history
  command: just validate-history
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000734
  summary: Executed on the corrected working tree/checkpoint. Corpus validation is
    not corpus-wide scientific review. Product IDs without authority adapters remain
    skipped, not verified.
- check_id: correction-verify-2
  name: just validate-products
  command: just validate-products
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000734
  summary: Executed on the corrected working tree/checkpoint. Corpus validation is
    not corpus-wide scientific review. Product IDs without authority adapters remain
    skipped, not verified.
- check_id: correction-verify-3
  name: just verify-proposal metpo_traitmech_v610
  command: just verify-proposal metpo_traitmech_v610
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000734
  summary: Executed on the corrected working tree/checkpoint. Corpus validation is
    not corpus-wide scientific review. Product IDs without authority adapters remain
    skipped, not verified.
- check_id: correction-verify-4
  name: just robot-validate-proposal metpo_traitmech_v610
  command: just robot-validate-proposal metpo_traitmech_v610
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000734
  summary: Executed on the corrected working tree/checkpoint. Corpus validation is
    not corpus-wide scientific review. Product IDs without authority adapters remain
    skipped, not verified.
- check_id: correction-verify-5
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/audit_history_records.py --base a1db3a44599b96d564d7c3bd5ecc0ace19add76e
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/audit_history_records.py --base a1db3a44599b96d564d7c3bd5ecc0ace19add76e
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000734
  summary: Executed on the corrected working tree/checkpoint. Corpus validation is
    not corpus-wide scientific review. Product IDs without authority adapters remain
    skipped, not verified.
- check_id: prior-suite
  name: prior-suite
  status: passed
  required: false
  target_ids:
  - traitmech:000734
  summary: 4817 tests passed at checkpoint 8886062340d71ebcec623416c3fffe37c8abe292.
    Full suite was not rerun after locator correction; post-correction focused/native
    gates and protected exact-head CI are separate.
- check_id: preservation
  name: preservation
  status: passed
  required: true
  target_ids:
  - traitmech:000734
  summary: Structured proof restores the original record exactly after reversing only
    the locator and removing the appended event. All 1128 prior records, protected
    spore germination, prior histories/reviews, source receipt, allocation, proposal,
    embeddings and shared templates remain preserved.
- check_id: rdf
  name: rdf
  status: passed
  required: true
  target_ids:
  - traitmech:000734
  summary: RDF contains 15/12628/12632 triples. Correct w3id child-parent-quality
    chain; definition annotation contains only the local record and DOI:10.1002/cm.21637.
    No legacy OBO parent stub; proposal unchanged by repair.
- check_id: browser
  name: browser
  status: passed
  required: true
  target_ids:
  - traitmech:000734
  summary: Desktop/mobile checks at 1440 and 390 pixels confirm local identifier,
    two supporting excerpts, one context excerpt, four OPEN discussions, corrected
    locator in curation history, two history links, browse navigation and 1129-count
    dashboard image without overflow or page errors. An initial test incorrectly expected
    structured discussion notes in rendered body text; the unchanged template renders
    the explanation instead. That failed assumption was corrected and the test rerun,
    not counted as a pass. Screenshots were inspected separately.
- check_id: whitespace
  name: whitespace
  status: passed
  required: true
  target_ids:
  - traitmech:000734
  summary: Initial ordinary staged check found only required trailing empty cells
    on the ROBOT directive row. Exact-template exception and all other paths passed.
    No global whitespace setting weakened; correction does not change the template.
- check_id: allocation
  name: allocation
  status: passed
  required: true
  target_ids:
  - traitmech:000734
  summary: Ignored/hidden-aware current, retained-history, complete-range and open/draft
    PR checks preceded allocation. Publication reassessment covered 211 known locations
    and 61263 current proposal-owner contexts; remote freshness remains a pre-push
    gate.
- check_id: embeddings
  name: Configured embedding source paths
  status: not_applicable
  required: false
  target_ids:
  - traitmech:000734
  summary: Both exact configured sources absent in main and owned layouts. Existing
    artifacts retained, not rebuilt. Isolated shared generator matched 645 pinned
    source blobs.
evidence:
- evidence_id: source-0
  kind: primary_source
  reference: DOI:10.1002/cm.21637
  locator: Results 2.2, TEM interpretation after Figure 2; https://pmc.ncbi.nlm.nih.gov/articles/PMC7944584/
  accessed_at: '2026-10-15T21:28:21Z'
  support: supports
  snapshot_sha256: bb16244226aa809168a65c8a49761deaad035d460e94f23c18fe415755a0834a
  summary: Venard et al. 2020, PMID:33103844, PMCID:PMC7944584, Results 2.2, TEM interpretation
    paragraph following Figure 2. Contiguous span checked in direct PMC HTML; native
    NOT_IN_ABSTRACT retained. Live phase microscopy, fixed immunofluorescence and
    TEM concern Rhizoclosmatium globosum JEL800 and Spizellomyces punctatus DAOM BR117.
    Internalized cross-sections retain 9+2 architecture without a surrounding ciliary
    membrane; fixed TEM is not continuous same-cell tracking. Figure 1's 23 and 32
    cells are selected retraction events, not biological-culture counts. Methods time
    zero is plating, whereas Figure 2's TEM caption says post-retraction; retain that
    timing discrepancy. Table 1 labels length/diameter with rate units unlike Table
    2; no numerical conversion or rate is asserted here. Main text and all five actual
    main figures were inspected. The main PDF and actual supplemental PDFs/videos
    remain unread. Subsequent degradation is a separate phase, not a requirement for
    this internalization phenotype. Formal review reread actual Figure 2. The earlier
    direct HTML reading is retained; a later PMC CAPTCHA is not a successful retrieval.
    No local-HTML byte match or same-cell TEM tracking is claimed. Timestamp records
    cached-byte recheck, not new acquisition.
- evidence_id: source-1
  kind: primary_source
  reference: DOI:10.1083/jcb.201701074
  locator: Discussion JATS s11, printed 1681/PDF page 9; Results s10 and Methods s20;
    https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5461030/fullTextXML
  accessed_at: '2026-10-15T21:28:21Z'
  support: supports
  snapshot_sha256: ccd2a9f8ae1b630f98af3dfcac6fcc6d35aad0dcca027f3db63a8f84aa0319e0
  summary: Fritz-Laylin et al. 2017, PMID:28473602, PMCID:PMC5461030.1, Discussion
    JATS s11, printed page 1681, PDF page 9. Direct normalized JATS and typeset passage
    checked; native NOT_IN_ABSTRACT retained. Bd denotes Batrachochytrium dendrobatidis,
    source strain JEL423, with synchronized zoospores observed under the described
    confinement preparation. Results s10, Discussion s11 and Methods s20 were read,
    along with selected PDF pages. Video 5 was inspected through 16 sampled frames
    and one enlarged frame, not continuous playback or every-frame analysis. File
    metadata reports 10.1 seconds at nominal 10 fps, burned-in labels span 0-20 seconds,
    and the caption states 0.1-second acquisition with 20-fps playback. These are
    not silently reconciled; no retraction rate or replicate count is inferred. The
    paper's WASP/SCAR pseudopod experiments do not establish an axoneme-internalization
    mechanism. Formal review reread the complete s10/s11/s20 sections. Selected PDF
    pages and sampled video were read during research, not all pages or continuous
    video. Timestamp records cached-byte recheck, not new acquisition.
- evidence_id: source-2
  kind: primary_source
  reference: DOI:10.1091/mbc.E24-12-0577
  locator: Results S7 and Figure 4C; expansion-factor value in Results S6, first paragraph,
    citing Supplemental Figure S3A-B; https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12659703/fullTextXML
  accessed_at: '2026-10-15T21:28:21Z'
  support: supports
  snapshot_sha256: 3c45fd8706025eedf7deaf7dde3469b67d0213dc81543072c7b8731129b3b51d
  summary: Long et al. 2025, PMID:40833813, PMCID:PMC12659703.2, Results S7, Centrioles
    shorten but are not degraded during ciliary disassembly, sentence following the
    coiled-complex observation; Figure 4C. Direct JATS match; native NOT_IN_ABSTRACT
    retained. R. globosum JEL800 fixed U-ExM stages are not longitudinal trajectories.
    Actual Figure 4, all supplement text and visual supplement pages 4, 7 and 8 were
    inspected. The main-text S2 pointer concerns a transcriptomic figure; the relevant
    centriole panels are S3F-H. Figure 4's caption gives about 4.5-fold expansion,
    versus 5.5 +/- 0.2 in Results S6 (Supplemental Figure S3A-B); no absolute-size
    conversion is inferred. Figure 4F counts 16, 3, 26 and 41 sporangia across categories
    from three to five independent experiments, not retraction events. The two-hour
    timeline is attributed to 2020, not a new measurement. Other actual main figures,
    the main PDF and other supplement pages were not visually inspected. The preprint
    is another version, not another study. Formal review reread S7, Figure 4 caption
    and actual image, S15 Methods, the S6 value paragraph and actual supplement page
    4. This source supports later-degradation context only, not a third definition
    citation. Timestamp records cached-byte recheck, not new acquisition.
- evidence_id: identity
  kind: record_content
  reference: data/traits/physiology/eukaryotic_flagellar_axoneme_internalization.yaml
  locator: Complete record and four OPEN discussions
  accessed_at: '2026-10-15T21:28:21Z'
  support: supports
  snapshot_sha256: e16e6a6d660b7d51ab966d9f4e76039d6dbf44e04715f240296e380142bd0158
  summary: Own intact eukaryotic axoneme withdrawal into the cell body is distinct
    from static localization, foreign-material uptake, external coiling, shortening
    by disassembly alone, autotomy, bacterial ejection, periplasmic flagellar possession
    and pilus retraction. Subsequent degradation is allowed, not required; no organism-level
    disjointness asserted.
- evidence_id: implementation
  kind: record_content
  reference: scripts/add_eukaryotic_flagellar_axoneme_internalization_trait.py
  locator: Whole writer, focused tests and both histories
  accessed_at: '2026-10-15T21:28:21Z'
  support: supports
  snapshot_sha256: d88115bc3e0083657fde66af2ef3015740fcfe7426ee39327324e6824615198e
  summary: Explicit apply, prevalidation, deep copies, hash-guarded proposal header
    and exact-input repair protect later curation. Repair appends one event and normal
    first-pass mode refuses the corrected record. Status remains PROPOSED.
- evidence_id: novelty
  kind: search
  reference: proposals/metpo_traitmech_v610/proposal.md
  locator: Identity, parent, obsolete identifiers and proposal
  accessed_at: '2026-10-15T21:28:21Z'
  support: supports
  snapshot_sha256: 34cfd5bca4fee5bfe5ca15cdc322fc69dbdc3c73f5fab2998801db90a1740b4c
  summary: Phenotype METPO:1000059 is broader by definition. Flagellar possession/arrangement/locomotion
    and neighboring resorption/autotomy/ejection records are not exact. Historical
    identifiers are not revived or used as exact xrefs; ontology pin unchanged. Microbial-eukaryote
    inclusion and obsolescence reason codes remain upstream questions.
  search_scope: Allocation included ignored/hidden files across 210 known locations,
    306 retained heads, 88636 TraitMech and 9308 CommunityMech unique regular Git
    blobs; eleven unavailable locations explicit. Known-positive regex control passed.
    Seventy-six biological contexts inherited byte-matched prior assessments; 74 local
    allocation contexts were broad editor envelopes. Complete-range scan covered 203913
    owner contexts and 2625 unique contents; all 32 matching contents were assessed.
    Twelve open/draft PRs and 784 changed blobs plus 587 selected upstream blobs were
    inspected. Embedding decimals and GMELIN 1068715 are not METPO reservations. Publication
    refresh covered 211 known locations and 61263 current proposal owners; only two
    owned v610 contents were new. No external exact match in that bounded current
    search. Lost ignored history, arbitrary archives, symlink targets and unchanged
    PR files are not reconstructed. No atomic reservation or literature exhaustion
    implied.
- evidence_id: provenance
  kind: record_content
  reference: research/traits/physiology/eukaryotic_flagellar_axoneme_internalization-source-verification.json
  locator: Source receipt with bounded access, metadata and notice checks
  accessed_at: '2026-10-15T21:28:21Z'
  support: supports
  snapshot_sha256: 36ac8e5dfecfdf07e8090c334334277fe84754e6269008aebe364323e97ad49b
  summary: Two distinct supporting publications, not two independently replicated
    laboratories. All three snippets retain native NOT_IN_ABSTRACT distinct from direct
    full-text matching and claim support. 2025 and its preprint are the same study;
    the unread linked 2017 editorial is not evidence. Earlier research receipt remains
    unchanged; a linked correction receipt supersedes only the erroneous locator.
- evidence_id: correction
  kind: record_content
  reference: research/traits/physiology/eukaryotic_flagellar_axoneme_internalization-locator-correction.json
  locator: Locator correction and preserved predecessor hashes
  accessed_at: '2026-10-15T21:28:21Z'
  support: supports
  snapshot_sha256: dc49007b33b334cbffabd3c95dc5aac3972ab29dc449b251cb6b96cf79e1c428
  summary: 'Issue #1950 corrects Methods/S3B to Results S6 (Supplemental Figure S3A-B).
    Source values and the 4.5-versus-5.5 discrepancy remain unchanged. Original research/history/reviews
    are preserved.'
- evidence_id: products
  kind: validation
  reference: reports/proposal_citation_audit.tsv
  locator: Native products, RDF and rendered surfaces
  accessed_at: '2026-10-15T21:28:21Z'
  support: supports
  snapshot_sha256: 8994c57399ce892f0a20040ff369dbb465d158d9365a547386afe5277e4cd00e
  summary: 1129 records. Of prior trait pages, 1127 changed only in corpus footer;
    phenotype gained one child, 206 to 207. Follow-up changes target locator/history
    rendering and latest-curation metadata only, not corpus counts or proposal.
assessments:
- assessment_id: identity
  area: identity
  topic: Intact own-axoneme internalization
  summary: Reusable physiological phenotype supported by the 2020 ultrastructural
    observations and distinct 2017 reported withdrawal. No gene/profile feature substitutes
    for an organism-level phenotype.
  target_ids:
  - traitmech:000734
  evidence_ids:
  - identity
  - source-0
  - source-1
  outcome: supported
- assessment_id: parent
  area: grounding
  topic: Phenotype parent and apparatus boundaries
  summary: Definition-based parent is broader without requiring locomotion. Shortening
    by disassembly differs from intact withdrawal; later degradation can follow withdrawal.
    Bacterial periplasmic structures and pili are different apparatuses. No disjoint-organism
    axiom.
  target_ids:
  - traitmech:000734
  evidence_ids:
  - identity
  - novelty
  outcome: supported
- assessment_id: evidence
  area: evidence
  topic: Assay, source-role and media bounds
  summary: Fixed TEM/U-ExM stages are not same-cell trajectories. Selected completed
    retractions do not establish all-cell probabilities; sporangia and cultures are
    not retraction-event counts. Video metadata and caption timing remain separate;
    no rate inferred.
  target_ids:
  - traitmech:000734
  evidence_ids:
  - source-0
  - source-1
  - source-2
  - provenance
  outcome: supported
- assessment_id: mechanism
  area: evidence
  topic: No universal mechanism or recycling requirement
  summary: No universal reeling, lash-around, membrane-loss, actin/dynein/protease,
    cell-cycle stage, rate, complete degradation or recycling imposed. WASP/SCAR pseudopod
    perturbations do not establish the internalization mechanism.
  target_ids:
  - traitmech:000734
  evidence_ids:
  - identity
  - source-0
  - source-1
  - source-2
  outcome: supported
- assessment_id: locator-resolution
  area: provenance
  topic: Corrected Results locator
  summary: 'Issue #1950 is fixed in both maintained notes with guarded repair and
    append-only provenance. Existing add-trait instructions already require accurate
    locators and successor reviews; this application error does not require another
    skill rule.'
  target_ids:
  - traitmech:000734
  evidence_ids:
  - source-2
  - implementation
  - correction
  outcome: supported
- assessment_id: products
  area: consistency
  topic: Canonical proposal and rendered output
  summary: Role-correct definition annotation and w3id parent chain agree with the
    source-backed record. Local identity, snippets, discussions, histories and corpus
    totals render coherently.
  target_ids:
  - traitmech:000734
  evidence_ids:
  - novelty
  - products
  - implementation
  outcome: supported
- assessment_id: gaps
  area: completeness
  topic: Authority, mechanism and upstream scope
  summary: Canonical strain authority/natural provenance, protein-resolved mechanism,
    exact mappings and upstream eukaryotic scope remain open. Access and notice checks
    are bounded, not comprehensive clearance.
  target_ids:
  - traitmech:000734
  evidence_ids:
  - identity
  - provenance
  outcome: unknown
findings:
- finding_id: expansion-factor-locator
  issue_key: axoneme-internalization-expansion-factor-locator
  category: provenance
  severity: minor
  status: resolved
  certainty: confirmed
  title: Context note locates the expansion factor in Methods instead of Results
  description: The value is in Results S6, citing Supplemental Figure S3A-B. Methods/S3B
    is an inaccurate locator. This is a bounded provenance correction, not an identity
    or evidence-sufficiency failure.
  target_ids:
  - traitmech:000734
  field_paths:
  - discussions[0].evidence[0].notes
  evidence_ids:
  - source-2
  - implementation
  - correction
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/physiology/eukaryotic_flagellar_axoneme_internalization.yaml
    role: curated_record
  - repository: CultureBotAI/TraitMech
    path: scripts/add_eukaryotic_flagellar_axoneme_internalization_trait.py
    role: guarded_writer
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/1950
  previous_occurrences:
  - repository: CultureBotAI/TraitMech
    review_id: 20261015T204954Z-axoneme-internalization-locator-finding
    finding_id: expansion-factor-locator
  disposition_reason: Both maintained notes now locate the value in Results S6 with
    Supplemental Figure S3A-B. Exact-preimage repair, dry run/apply/replay, refusal
    tests, appended provenance and relevant native gates pass. Biological claims,
    proposal and earlier observations are preserved.
actions: []
related_reviews:
- repository: CultureBotAI/TraitMech
  review_id: 20261015T204954Z-axoneme-internalization-locator-finding
  relationship: Resolves the exact minor expansion-factor-locator finding and adds
    a complete bounded scientific assessment; preserves the initial observation.
limitations:
- Author self-review, not human sign-off or independent-laboratory replication.
- 2020 main text and all five actual main figures were read during research; formal
  review reread Figure 2. Main PDF and actual supplementary PDFs/videos remain unread.
  Later PMC access returned CAPTCHA; supplement endpoint returned an XML error, not
  a ZIP.
- 2017 selected PDF pages and 16 sampled video frames plus one enlargement were inspected,
  not all pages, continuous playback or every-frame analysis. Formal review reread
  s10/s11/s20. Linked editorial content remains unread.
- 2025 text, actual Figure 4 and selected supplemental pages were inspected; other
  actual main figures and main PDF remain unread. Fixed stages are not trajectories.
  Preprint is not an independent study.
- Native NOT_IN_ABSTRACT outcomes are not independent biological verification. Metadata/notice
  fields do not provide comprehensive correction or retraction clearance.
- Full local suite covers the pre-correction checkpoint. Corrected focused/native
  gates are separate; protected exact-head CI and external reviews remain merge gates.
- Known-copy searches are bounded, not atomic reservation, global absence or literature
  exhaustion. Temporary assets may not remain available.
- Configured embedding sources unavailable; previous artifacts retained. No raw-data
  reanalysis or paid research.
links:
- https://github.com/CultureBotAI/TraitMech/issues/1950
- https://doi.org/10.1002/cm.21637
- https://doi.org/10.1083/jcb.201701074
- https://doi.org/10.1091/mbc.E24-12-0577
tags:
- add-trait
- axoneme-internalization
- self-review
```
