# Cellular contraction and two hierarchy repairs: initial

- Review: 20261014T230107Z-cellular-contraction-initial
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-14T23:00:46Z
- Finished UTC: 2026-10-14T23:01:07Z
- Reviewer: codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The new shortening phenotype and definition-based child refinements are supported within scope. One minor sidecar provenance inconsistency needs correction; full final validation is still running.

## Scope And Provenance

Complete new parent and bounded hierarchy/discussion/source-URL/history changes to two children, including evidence sidecar, guarded writer/tests, skill, proposal and generated surfaces.

Selection: Exact three trait IDs on the cellular-contraction branch; no sampling.
Coverage: partial; 3 reviewed / 3 in the declared population.
Source: working_tree at Git base b27e7a8e1c0e3c29bd34dd6cfcbee4ddb449b9fd.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| traitmech:000729 | data/traits/physiology/cellular_contraction.yaml | maintained | cellular contraction (body or cytoplasmic projection shortening) |
| traitmech:000728 | data/traits/physiology/cell_body_contraction.yaml | maintained | cell-body contraction |
| traitmech:000682 | data/traits/physiology/rapid_axopodial_contraction.yaml | maintained | rapid axopodial contraction |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate -s src/traitmech/schema/traitmech.yaml --target-class TraitRecord data/traits/physiology/cellular_contraction.yaml | passed | True | traitmech:000729, traitmech:000728, traitmech:000682 | Completed native command. Scope is its arguments, including corpus-wide generation and audits; no baseline was weakened. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/validate_strict.py data/traits/physiology/cellular_contraction.yaml | passed | True | traitmech:000729, traitmech:000728, traitmech:000682 | Completed native command. Scope is its arguments, including corpus-wide generation and audits; no baseline was weakened. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/validate_history_links.py history/records/cellular_contraction | passed | True | traitmech:000729, traitmech:000728, traitmech:000682 | Completed native command. Scope is its arguments, including corpus-wide generation and audits; no baseline was weakened. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/verify_snippets.py --record data/traits/physiology/cellular_contraction.yaml --out /tmp/traitmech-cellular-contraction-checks-20261014/cellular_contraction-native.tsv | passed | True | traitmech:000729, traitmech:000728, traitmech:000682 | Completed native command. Scope is its arguments, including corpus-wide generation and audits; no baseline was weakened. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate -s src/traitmech/schema/traitmech.yaml --target-class TraitRecord data/traits/physiology/cell_body_contraction.yaml | passed | True | traitmech:000729, traitmech:000728, traitmech:000682 | Completed native command. Scope is its arguments, including corpus-wide generation and audits; no baseline was weakened. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/validate_strict.py data/traits/physiology/cell_body_contraction.yaml | passed | True | traitmech:000729, traitmech:000728, traitmech:000682 | Completed native command. Scope is its arguments, including corpus-wide generation and audits; no baseline was weakened. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/validate_history_links.py history/records/cell_body_contraction | passed | True | traitmech:000729, traitmech:000728, traitmech:000682 | Completed native command. Scope is its arguments, including corpus-wide generation and audits; no baseline was weakened. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/verify_snippets.py --record data/traits/physiology/cell_body_contraction.yaml --out /tmp/traitmech-cellular-contraction-checks-20261014/cell_body_contraction-native.tsv | passed | True | traitmech:000729, traitmech:000728, traitmech:000682 | Completed native command. Scope is its arguments, including corpus-wide generation and audits; no baseline was weakened. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate -s src/traitmech/schema/traitmech.yaml --target-class TraitRecord data/traits/physiology/rapid_axopodial_contraction.yaml | passed | True | traitmech:000729, traitmech:000728, traitmech:000682 | Completed native command. Scope is its arguments, including corpus-wide generation and audits; no baseline was weakened. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/validate_strict.py data/traits/physiology/rapid_axopodial_contraction.yaml | passed | True | traitmech:000729, traitmech:000728, traitmech:000682 | Completed native command. Scope is its arguments, including corpus-wide generation and audits; no baseline was weakened. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/validate_history_links.py history/records/rapid_axopodial_contraction | passed | True | traitmech:000729, traitmech:000728, traitmech:000682 | Completed native command. Scope is its arguments, including corpus-wide generation and audits; no baseline was weakened. |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python scripts/verify_snippets.py --record data/traits/physiology/rapid_axopodial_contraction.yaml --out /tmp/traitmech-cellular-contraction-checks-20261014/rapid_axopodial_contraction-native.tsv | passed | True | traitmech:000729, traitmech:000728, traitmech:000682 | Completed native command. Scope is its arguments, including corpus-wide generation and audits; no baseline was weakened. |
| just verify-proposal metpo_traitmech_v605 | passed | True | traitmech:000729, traitmech:000728, traitmech:000682 | Completed native command. Scope is its arguments, including corpus-wide generation and audits; no baseline was weakened. |
| just robot-validate-proposal metpo_traitmech_v605 | passed | True | traitmech:000729, traitmech:000728, traitmech:000682 | Completed native command. Scope is its arguments, including corpus-wide generation and audits; no baseline was weakened. |
| just audit-proposals | passed | True | traitmech:000729, traitmech:000728, traitmech:000682 | Completed native command. Scope is its arguments, including corpus-wide generation and audits; no baseline was weakened. |
| just ground-predicates | passed | True | traitmech:000729, traitmech:000728, traitmech:000682 | Completed native command. Scope is its arguments, including corpus-wide generation and audits; no baseline was weakened. |
| just ground-nodes | passed | True | traitmech:000729, traitmech:000728, traitmech:000682 | Completed native command. Scope is its arguments, including corpus-wide generation and audits; no baseline was weakened. |
| just audit-graphs | passed | True | traitmech:000729, traitmech:000728, traitmech:000682 | Completed native command. Scope is its arguments, including corpus-wide generation and audits; no baseline was weakened. |
| just audit-graph-protein-taxa | passed | True | traitmech:000729, traitmech:000728, traitmech:000682 | Completed native command. Scope is its arguments, including corpus-wide generation and audits; no baseline was weakened. |
| just audit-predicate-domains | passed | True | traitmech:000729, traitmech:000728, traitmech:000682 | Completed native command. Scope is its arguments, including corpus-wide generation and audits; no baseline was weakened. |
| just check-biolink-coverage | passed | True | traitmech:000729, traitmech:000728, traitmech:000682 | Completed native command. Scope is its arguments, including corpus-wide generation and audits; no baseline was weakened. |
| just audit-snippets | passed | True | traitmech:000729, traitmech:000728, traitmech:000682 | Completed native command. Scope is its arguments, including corpus-wide generation and audits; no baseline was weakened. |
| just gen-discussions-data | passed | True | traitmech:000729, traitmech:000728, traitmech:000682 | Completed native command. Scope is its arguments, including corpus-wide generation and audits; no baseline was weakened. |
| just gen-qc-dashboard | passed | True | traitmech:000729, traitmech:000728, traitmech:000682 | Completed native command. Scope is its arguments, including corpus-wide generation and audits; no baseline was weakened. |
| just gen-pages | passed | True | traitmech:000729, traitmech:000728, traitmech:000682 | Completed native command. Scope is its arguments, including corpus-wide generation and audits; no baseline was weakened. |
| just gen-priority-dashboard | passed | True | traitmech:000729, traitmech:000728, traitmech:000682 | Completed native command. Scope is its arguments, including corpus-wide generation and audits; no baseline was weakened. |
| Final focused gates | unavailable | True | traitmech:000729, traitmech:000728, traitmech:000682 | Still running when this original finding was saved; no final success claimed. Required before publication. |
| Final verify gates | unavailable | True | traitmech:000729, traitmech:000728, traitmech:000682 | Still running when this original finding was saved; no final success claimed. Required before publication. |
| Final tests gates | unavailable | True | traitmech:000729, traitmech:000728, traitmech:000682 | Still running when this original finding was saved; no final success claimed. Required before publication. |
| products | passed | True | traitmech:000729, traitmech:000728, traitmech:000682 | Integrity assertions passed: 1124 records, 1121 untouched old YAMLs, both child definitions/snippets/prior history preserved, protected record unchanged; old proposals, histories, reviews, embeddings and templates preserved. 1120 old pages are footer-only. Only phenotype child count changes in existing priority rows, 204 to 203. RDF contains 15/12628/12632 triples in classes/merged/reasoned graphs, real w3id phenotype/quality hierarchy and only Katoh/local-record definition annotation; historical child axioms are requested in narrative, not emitted. |
| browser | passed | True | traitmech:000729, traitmech:000728, traitmech:000682 | Chrome 1440/390 checks passed source/identity, three quotes, three parent discussions, two child links, open assay question, history, browse navigation, dashboard count/image and overflow/errors. All eight screenshots visually inspected. |
| Configured embedding source applicability | not_applicable | False | traitmech:000729, traitmech:000728, traitmech:000682 | Both exact configured source paths absent in owned and main layouts; existing artifacts retained, not regenerated. |
| Scoped ROBOT header whitespace | passed | True | traitmech:000729, traitmech:000728, traitmech:000682 | Ordinary staged diff check returned 2 solely for the three required empty trailing TSV directive cells. Inspected canonical 11-column headers; separate non-TSV and exact-path blank-at-eol exception checks returned 0. No global exemption. |

## Scientific And Domain Assessments

### Observable shortening phenotype

identity: supported. Targets: traitmech:000729.

The qualified label and endpoint distinguish active body/projection shortening from generic contractility, locomotion, molecular machines and static morphology.

### Strictly broader parent

grounding: supported. Targets: traitmech:000729, traitmech:000728, traitmech:000682.

Both child definitions entail the new parent. Phenotype remains their ancestor; no disjoint taxa, process equivalence or common molecular mechanism follows.

### Primary-result scope and source fidelity

evidence: supported. Targets: traitmech:000729.

Three concise primary-result excerpts support shortening. Living cells and extracted preparations, body and head-to-stalk length, natural and slowed responses, and native abstract versus direct PDF verdicts remain distinct. The percentage and calcium observations are not universal.

### Child scope and independent questions

consistency: supported. Targets: traitmech:000728, traitmech:000682.

Only the hierarchy question is resolved; prior rationales, definitions, excerpts and histories remain, and the axopodial assay question is explicitly OPEN.

### Guarded curation and histories

provenance: supported. Targets: traitmech:000729, traitmech:000728, traitmech:000682.

Exact preimages, replay refusal, prevalidation, agent-attributed events and native histories protect the scoped changes.

### Temporal parent state

provenance: concern. Targets: traitmech:000729, traitmech:000728, traitmech:000682.

The post-curation sidecar carries child_repair.current_parent=METPO:1000059 from the research plan. The written children instead have direct parent traitmech:000729; phenotype remains an ancestor. Separate historical and applied state so provenance readers do not receive conflicting direct-parent assertions.

### Proposal and rendered products

consistency: supported. Targets: traitmech:000729, traitmech:000728, traitmech:000682.

Standalone proposal emits one correctly rooted class; child axioms remain explicit upstream requests. Generated pages, discussions and counts reflect the coupled repair.

### Taxonomic and molecular gaps

completeness: unknown. Targets: traitmech:000729, traitmech:000728, traitmech:000682.

No canonical taxa or proteins are asserted. Isolate identities, mechanisms, exact mappings and comparative assays remain open, not falsely completed by sequence evidence or hierarchy repair.

## Findings

### sidecar-parent-state: Source sidecar presents the pre-change direct parent as current

minor / open / confirmed; issue key: cellular-contraction-sidecar-parent-state.

The post-curation sidecar carries child_repair.current_parent=METPO:1000059 from the research plan. The written children instead have direct parent traitmech:000729; phenotype remains an ancestor. Separate historical and applied state so provenance readers do not receive conflicting direct-parent assertions.

## Recommended Actions And Acceptance Checks

### clarify-parent-state

Label the pre-change direct parent and record the accepted post-change direct parent; test both against the coupled YAML state without changing scientific evidence or histories.

- Explicit pre_change_parent=METPO:1000059 and post_change_parent=traitmech:000729.
- Regression test agrees with both child parent_traits.
- Prior source receipts and histories byte-preserved; linked successor review saved.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| source-0 | DOI:10.1242/jeb.189.1.163; Scientific abstract, numbered item 3, first clause; https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9317557+AND+SRC%3AMED&amp;resultType=core&amp;format=json. Access time records cached-source reread and hash verification, not first acquisition. | supports | Katoh and Naitoh 1994, PMID:9317557, scientific Abstract item 3, first clause. Direct namespace-qualified Europe PMC MED match; native VERIFIED. The same sentence contrasts graded cell-body shrinkage with all-or-nothing stalk coiling. This supports the curator-synthesized body/projection-shortening parent, not a universal calcium threshold. Other abstract items use Triton-extracted preparations, not the living-cell injection assay. Calcium-induced calcium release is an assumption, not direct molecular proof. Publisher requests returned 403; full Methods, figures and strain provenance were not accessed. |
| source-1 | DOI:10.2108/zsj.20.1367; Scientific abstract, opening sentence; https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14624035+AND+SRC%3AMED&amp;resultType=core&amp;format=json. Access time records cached-source reread and hash verification, not first acquisition. | supports | Khan et al. 2003, PMID:14624035, scientific Abstract opening sentence. Direct namespace-qualified Europe PMC MED match; native VERIFIED. This supports stimulated shortening of a cytoplasmic projection rather than whole-cell locomotion. Reported calcium dependence and speed apply to this assay, not every member of the parent class. Non-detection of other filaments after fixation is not proof of their absence. Full Methods and figures were not accessed; the publisher's HTTP 200 response was an access challenge, not readable article content. Current taxonomic and culture identities remain unresolved. |
| source-2 | DOI:10.1083/jcb.118.3.585; Results, Kinetics of the Contraction, printed page 588, right column; https://pdfs.semanticscholar.org/20fc/996490bf001a841702e28a552eee5f6e50e7.pdf. Access time records cached-source reread and hash verification, not first acquisition. | supports | Febvre-Chevalier and Febvre 1992, PMID:1639845, PMCID:PMC2289557, Results, Kinetics of the Contraction, printed page 588, right column. Direct extracted-PDF match with the typeset passage visually checked; native NOT_IN_ABSTRACT retained. The primary PDF was retrieved from its Semantic Scholar mirror after official PDF attempts failed. Selected Methods/Results and actual Figures 1 and 3-6 were inspected. Length was measured from head top to stalk base, not isolated cell-body length; graph axes use stalk length. The percentage is study-specific. Natural-seawater responses differ from artificially slowed responses. The specimens were collected near Villefranche and cultured at 14-18 C; current taxonomic identity is not verified. The n=20 initial-length sample is not asserted as independent contraction replication. Microtubule disassembly accompanies shortening, but this study expressly does not establish force production. Its disassembly half-time is not automatically contraction duration. The accessible JATS contains an abstract and PDF pointer, not the complete experimental text. |
| hierarchy | data/traits/physiology/cellular_contraction.yaml; Complete new record and both child definitions, parent_traits, discussions and histories. | supports | A shortening-defined physiological phenotype, not force production in general, locomotion, a protein sequence, an organelle or assay row. Both child definitions entail this broader endpoint. Their prior rationales/evidence/history remain intact; only the parent component is resolved and axopodial assay comparability remains OPEN. |
| implementation | scripts/add_cellular_contraction_trait.py; Complete writer, controlled-fixture tests, three append-only histories and skill clarification. | supports | Dry-run default; exact structured preimage hashes and whole-result replay checks; all three records prevalidated before production writes. Source URL qualification preserves scientific excerpts. Every changed trait has a per-record event and native history. No human review promotion; all remain PROPOSED. |
| novelty | proposals/metpo_traitmech_v605/proposal.md; Identity/allocation section and captured source-sidecar receipts. | supports | Accepted bounded search distinguishes two narrower children from unrelated contraction endpoints and numeric lookalikes. No additional exact parent, synonym or graph-node migration was accepted. Pinned/current/editor ontology assessment distinguishes related deprecated locomotion IDs and active phenotype hierarchy. v605 reserves the full block but emits one class; old cohorts remain unchanged. |
| products | reports/proposal_citation_audit.tsv; Native generated products plus independent preservation, parsed-RDF and browser checks. | supports | Maintained generation agrees with the new parent and two child repairs; only intended scientific owners change. Unrelated page churn is corpus-footer counts, not curation. |
| sidecar | research/traits/physiology/cellular_contraction-source-verification.json; child_repair.current_parent and source-sidecar top-level written-curation status; compare both child parent_traits. | supports | The original sidecar copied pre-curation proposed_repair.current_parent=METPO:1000059 without identifying it as pre-change. Written child YAMLs instead have direct parent traitmech:000729. The ontology and evidence remain correct; the sidecar is temporally ambiguous. |

## Limits And Additional Notes

- Self-review and PROPOSED curation, not independent review or human sign-off.
- Complete parent assessment; children only for the coupled changes and preservation, not their entire literature.
- Katoh and Khan scientific abstracts accessible; full Methods/figures unavailable. Publisher 200 for Khan was an access challenge. Febvre selected printed pages 585/586/588 and actual Figures 1/3-6 inspected; other rendered pages were not treated as viewed. Reread printed 588 during formal review.
- Febvre native NOT_IN_ABSTRACT remains unchanged despite a verified primary-PDF match. Its total-length endpoint is not isolated body length; microtubule breakdown is not demonstrated force production.
- Correction/retraction checks cover specific MED/Crossref fields and available sources, not comprehensive clearance.
- No universal trigger, speed, shortening fraction, calcium threshold, ATP mechanism, ecological role, exact synonym or external equivalence inferred. Protein sequence features alone do not establish the phenotype.
- Source acquisition and reservation receipts are retained with stable URLs/hashes; temporary raw files are not guaranteed long-term availability. Known-copy searches do not establish exhaustive global discovery.
- Embedding inputs unavailable; existing embeddings preserved. No paid research used.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T230107Z-cellular-contraction-initial
kind: batch
repository: CultureBotAI/TraitMech
title: 'Cellular contraction and two hierarchy repairs: initial'
started_at: '2026-10-14T23:00:46Z'
finished_at: '2026-10-14T23:01:07Z'
reviewer:
  identity: codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Author falsification-oriented pass, not independent or human
    scientific sign-off. External requests and CI do not change this attribution.
skill: .claude/skills/add-trait/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: The new shortening phenotype and definition-based child refinements are supported
  within scope. One minor sidecar provenance inconsistency needs correction; full
  final validation is still running.
source:
  git_revision: b27e7a8e1c0e3c29bd34dd6cfcbee4ddb449b9fd
  state: working_tree
  inputs:
  - path: .claude/skills/add-trait/SKILL.md
    sha256: b36001591513b57b34392862ef36294eb6458427173b1f575a5bd71376069a92
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
    sha256: 84a47d0765c124cbe62105fb2dc4e3d87b32f13948f3b0d60f103e458af24ba2
    role: context
  - path: app/dashboard/priority.html
    sha256: 4a6b6e1e92bacaebb091bcef05fa9462ae0bdc5392bab8f5394e68a350a220c3
    role: context
  - path: app/dashboard/priority.json
    sha256: 76e7f7fe731e4fe6ed0c04beb614f1bdbf247f6a7c6920a3d61f73d843e3317a
    role: context
  - path: app/discussions/data.js
    sha256: 673e122002fd349663c1aea51713a5416d6341c67925e84120db3264b1b48b18
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
    sha256: 14cb7b04eb072ca6ee0445b3ed971eb41cb149f109e2497f70491072b817bc6a
    role: context
  - path: dashboard/index.html
    sha256: 0028f8928935985628de7558aa6a6a06d4f33fa0398281849a4ea0ce9658d846
    role: context
  - path: data/raw/metpo.owl
    sha256: 8b6f8fe0510a698579e532658c8ace05da2550093365df9ca83feb0741778415
    role: context
  - path: data/traits/physiology/cell_body_contraction.yaml
    sha256: 74efcfa3e5e6312569c3f18f667912492bad7c492fb07341914e12fc67275ed9
    role: target
  - path: data/traits/physiology/cellular_contraction.yaml
    sha256: 74ac2ccac8a856faff4095d47c20580f1b781a841caeb3b06a69280dc13125f0
    role: target
  - path: data/traits/physiology/rapid_axopodial_contraction.yaml
    sha256: 83a7e6a81235b86017f9f1325e404fe976d4e85538ddae125d63905e737f9ebb
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
  - path: history/records/cell_body_contraction/2026-10-14T173532Z-codex-c9af70.yaml
    sha256: defd3d917ca15678d1f8a62ebcdd1355b385607ad595729bcf0e9f071eb30038
    role: context
  - path: history/records/cell_body_contraction/2026-10-14T175927Z-codex-09ab48.yaml
    sha256: c7bf5a1d09f3e269900fe4776134b4ecaec9c9fdf078b1479cc11b6c67de24d6
    role: context
  - path: history/records/cell_body_contraction/2026-10-14T185654Z-codex-d5ad35.yaml
    sha256: f8a41772bbf07d728e6b99c075741522a069e897a4403d49cb12d3b76ffb44f5
    role: context
  - path: history/records/cell_body_contraction/2026-10-14T190521Z-codex-9d794a.yaml
    sha256: eb998e1af17a67d234ddcab7d8acfdc82472691a44d7c5a52ecaebd102fa08ac
    role: context
  - path: history/records/cell_body_contraction/2026-10-14T223940Z-codex-c0f579.yaml
    sha256: 5de1b4c2948160eb6cc77a2af4fae3a2454807ea0084dabb78c7cd731461c7f1
    role: context
  - path: history/records/cellular_contraction/2026-10-14T223936Z-codex-5fdb55.yaml
    sha256: c27d8cca7a482933849be9451b8be9407cebfca08ea5e0822254d2b0c3f76ea2
    role: context
  - path: history/records/rapid_axopodial_contraction/2026-10-08T145708Z-codex-2f9679.yaml
    sha256: 3888a98801b3ad44dc19ef29445f8d433af27a82fcf16d1e7470f19d131c031d
    role: context
  - path: history/records/rapid_axopodial_contraction/2026-10-14T223943Z-codex-966313.yaml
    sha256: 410b41709cf405543a4acd60c075e0c4e5ad9c51546474f50bead509a6de01f6
    role: context
  - path: justfile
    sha256: e6047ea612115a6a78d100b281483ba824c860c3def59bcd0d40e7fb56b3526a
    role: context
  - path: pages/browse.html
    sha256: 482b2dac11b74adcc292c2deffc76593b4ab920e2f6786750bed76cbb407c477
    role: context
  - path: pages/traits/physiology/cell_body_contraction.html
    sha256: 4189ac8747c852e6384d8e2a5fdf5191b0ada729f218c20a6d2ffe5de509ef1c
    role: context
  - path: pages/traits/physiology/cellular_contraction.html
    sha256: 6feeabe823f0c574002c9f7a2a6291b83d3c7fd519a3157f6e42e8501527cfe2
    role: context
  - path: pages/traits/physiology/rapid_axopodial_contraction.html
    sha256: 935a392915f167b4a4049f618bf5528aebdb51daa4c84245ce8d058805ba111d
    role: context
  - path: pages/traits/upper/phenotype.html
    sha256: 829f523034e2f2fd48d64d54a2858368e6bf43009c1f7827cd59829f14e07dbf
    role: context
  - path: proposals/metpo_traitmech_v558/metpo_proposal_classes_robot.tsv
    sha256: dad8ccb2031b4e7f518efa57ee3094a1137ff60af3fe5de783b0a6d8cd8d5655
    role: context
  - path: proposals/metpo_traitmech_v558/proposal.md
    sha256: 12c05618afe97eb140bf296e529151f37a08a4b727fdfe13b309d141ed01e5de
    role: context
  - path: proposals/metpo_traitmech_v604/metpo_proposal_classes_robot.tsv
    sha256: d6ff228db4e4814e7f789aff4b5958c0681514792e1f14e8c2cf48c5af293d13
    role: context
  - path: proposals/metpo_traitmech_v604/proposal.md
    sha256: b5e96c8ab282fa1d31a87bf7b273a9442c1e7e11636fa6b519aae53332e01e1c
    role: context
  - path: proposals/metpo_traitmech_v605/metpo_proposal_classes_robot.tsv
    sha256: f854f0e18fcfad87293154aa5ce63376872a080b2d48bcb058e681fdfef6429a
    role: context
  - path: proposals/metpo_traitmech_v605/proposal.md
    sha256: b329dc54a85fdf1a4afb8a9fcabfb71cf769e4de2308d35c6e06e203503f908b
    role: context
  - path: reports/proposal_citation_audit.tsv
    sha256: 98275d4165e89a998586c413c87259ef5361398b0f7598a07f0de5e55b7b0707
    role: context
  - path: research/traits/physiology/cellular_contraction-source-verification.json
    sha256: 3188d8c1e78d4375bae4b3d6e5d2f2b9e06bb6ebd4d5432dcaafe11dda156c8c
    role: context
  - path: scripts/add_cellular_contraction_trait.py
    sha256: e924e40ae9145b59f7e6ec4a43c337ff64cf118c0b6f621abb83c4ceb98be5ee
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
  - path: src/traitmech/schema/traitmech.yaml
    sha256: 46c47fc627b80ccbba1e8ab3fb6f2aee93bc2aef7aaf72fe9aadc3257f2c02dd
    role: context
  - path: src/traitmech/validation/write_validated.py
    sha256: 68cfeb876a60d67fd72d5a2800cd29e41b5cf563be5a27b698398a5bb3e67231
    role: context
  - path: tests/test_add_axopodial_contraction_trait.py
    sha256: a5fabdbd5b528f183a9cd3c2532e6f9c70d75937f1baeb0899bdaa9c797b29ae
    role: context
  - path: tests/test_add_cell_body_contraction_trait.py
    sha256: 6bc91e9fdb3db3d758ef7095a8e666d78c3d8157a0ba3dadac0cc2ec7539466b
    role: context
  - path: tests/test_add_cellular_contraction_trait.py
    sha256: 3a68aaa92206e4fd1d53680ad32aca618e87ca4cb26f7df6148310e74d2240ad
    role: context
targets:
- target_id: traitmech:000729
  path: data/traits/physiology/cellular_contraction.yaml
  label: cellular contraction (body or cytoplasmic projection shortening)
  kind: maintained
  record_class: TraitRecord
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/physiology/cellular_contraction.yaml
    role: curated_record
  - repository: CultureBotAI/TraitMech
    path: scripts/add_cellular_contraction_trait.py
    role: guarded_writer
- target_id: traitmech:000728
  path: data/traits/physiology/cell_body_contraction.yaml
  label: cell-body contraction
  kind: maintained
  record_class: TraitRecord
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/physiology/cell_body_contraction.yaml
    role: curated_record
  - repository: CultureBotAI/TraitMech
    path: scripts/add_cellular_contraction_trait.py
    role: guarded_writer
- target_id: traitmech:000682
  path: data/traits/physiology/rapid_axopodial_contraction.yaml
  label: rapid axopodial contraction
  kind: maintained
  record_class: TraitRecord
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/physiology/rapid_axopodial_contraction.yaml
    role: curated_record
  - repository: CultureBotAI/TraitMech
    path: scripts/add_cellular_contraction_trait.py
    role: guarded_writer
scope:
  description: Complete new parent and bounded hierarchy/discussion/source-URL/history
    changes to two children, including evidence sidecar, guarded writer/tests, skill,
    proposal and generated surfaces.
  selection: Exact three trait IDs on the cellular-contraction branch; no sampling.
  coverage: partial
  population_size: 3
  reviewed_target_ids:
  - traitmech:000729
  - traitmech:000728
  - traitmech:000682
  exclusions:
  - target: Unchanged child scientific claims
    reason: Read for hierarchy and preservation; not a fresh complete source/figure
      audit of both children.
  - target: Other 1121 TraitRecords
    reason: Automated checks and preservation comparisons, not scientific adjudication.
  - target: data/traits/physiology/spore_germination.yaml
    reason: Protected by DO_NOT_WORK; byte-preserved and not curated.
checks:
- check_id: records-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate
    -s src/traitmech/schema/traitmech.yaml --target-class TraitRecord data/traits/physiology/cellular_contraction.yaml
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate
    -s src/traitmech/schema/traitmech.yaml --target-class TraitRecord data/traits/physiology/cellular_contraction.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000729
  - traitmech:000728
  - traitmech:000682
  summary: Completed native command. Scope is its arguments, including corpus-wide
    generation and audits; no baseline was weakened.
- check_id: records-1
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_strict.py data/traits/physiology/cellular_contraction.yaml
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_strict.py data/traits/physiology/cellular_contraction.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000729
  - traitmech:000728
  - traitmech:000682
  summary: Completed native command. Scope is its arguments, including corpus-wide
    generation and audits; no baseline was weakened.
- check_id: records-2
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_history_links.py history/records/cellular_contraction
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_history_links.py history/records/cellular_contraction
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000729
  - traitmech:000728
  - traitmech:000682
  summary: Completed native command. Scope is its arguments, including corpus-wide
    generation and audits; no baseline was weakened.
- check_id: records-3
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/verify_snippets.py --record data/traits/physiology/cellular_contraction.yaml
    --out /tmp/traitmech-cellular-contraction-checks-20261014/cellular_contraction-native.tsv
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/verify_snippets.py --record data/traits/physiology/cellular_contraction.yaml
    --out /tmp/traitmech-cellular-contraction-checks-20261014/cellular_contraction-native.tsv
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000729
  - traitmech:000728
  - traitmech:000682
  summary: Completed native command. Scope is its arguments, including corpus-wide
    generation and audits; no baseline was weakened.
- check_id: records-4
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate
    -s src/traitmech/schema/traitmech.yaml --target-class TraitRecord data/traits/physiology/cell_body_contraction.yaml
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate
    -s src/traitmech/schema/traitmech.yaml --target-class TraitRecord data/traits/physiology/cell_body_contraction.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000729
  - traitmech:000728
  - traitmech:000682
  summary: Completed native command. Scope is its arguments, including corpus-wide
    generation and audits; no baseline was weakened.
- check_id: records-5
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_strict.py data/traits/physiology/cell_body_contraction.yaml
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_strict.py data/traits/physiology/cell_body_contraction.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000729
  - traitmech:000728
  - traitmech:000682
  summary: Completed native command. Scope is its arguments, including corpus-wide
    generation and audits; no baseline was weakened.
- check_id: records-6
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_history_links.py history/records/cell_body_contraction
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_history_links.py history/records/cell_body_contraction
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000729
  - traitmech:000728
  - traitmech:000682
  summary: Completed native command. Scope is its arguments, including corpus-wide
    generation and audits; no baseline was weakened.
- check_id: records-7
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/verify_snippets.py --record data/traits/physiology/cell_body_contraction.yaml
    --out /tmp/traitmech-cellular-contraction-checks-20261014/cell_body_contraction-native.tsv
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/verify_snippets.py --record data/traits/physiology/cell_body_contraction.yaml
    --out /tmp/traitmech-cellular-contraction-checks-20261014/cell_body_contraction-native.tsv
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000729
  - traitmech:000728
  - traitmech:000682
  summary: Completed native command. Scope is its arguments, including corpus-wide
    generation and audits; no baseline was weakened.
- check_id: records-8
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate
    -s src/traitmech/schema/traitmech.yaml --target-class TraitRecord data/traits/physiology/rapid_axopodial_contraction.yaml
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/linkml-validate
    -s src/traitmech/schema/traitmech.yaml --target-class TraitRecord data/traits/physiology/rapid_axopodial_contraction.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000729
  - traitmech:000728
  - traitmech:000682
  summary: Completed native command. Scope is its arguments, including corpus-wide
    generation and audits; no baseline was weakened.
- check_id: records-9
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_strict.py data/traits/physiology/rapid_axopodial_contraction.yaml
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_strict.py data/traits/physiology/rapid_axopodial_contraction.yaml
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000729
  - traitmech:000728
  - traitmech:000682
  summary: Completed native command. Scope is its arguments, including corpus-wide
    generation and audits; no baseline was weakened.
- check_id: records-10
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_history_links.py history/records/rapid_axopodial_contraction
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/validate_history_links.py history/records/rapid_axopodial_contraction
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000729
  - traitmech:000728
  - traitmech:000682
  summary: Completed native command. Scope is its arguments, including corpus-wide
    generation and audits; no baseline was weakened.
- check_id: records-11
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/verify_snippets.py --record data/traits/physiology/rapid_axopodial_contraction.yaml
    --out /tmp/traitmech-cellular-contraction-checks-20261014/rapid_axopodial_contraction-native.tsv
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/TraitMech/.venv/bin/python
    scripts/verify_snippets.py --record data/traits/physiology/rapid_axopodial_contraction.yaml
    --out /tmp/traitmech-cellular-contraction-checks-20261014/rapid_axopodial_contraction-native.tsv
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000729
  - traitmech:000728
  - traitmech:000682
  summary: Completed native command. Scope is its arguments, including corpus-wide
    generation and audits; no baseline was weakened.
- check_id: proposal-0
  name: just verify-proposal metpo_traitmech_v605
  command: just verify-proposal metpo_traitmech_v605
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000729
  - traitmech:000728
  - traitmech:000682
  summary: Completed native command. Scope is its arguments, including corpus-wide
    generation and audits; no baseline was weakened.
- check_id: proposal-1
  name: just robot-validate-proposal metpo_traitmech_v605
  command: just robot-validate-proposal metpo_traitmech_v605
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000729
  - traitmech:000728
  - traitmech:000682
  summary: Completed native command. Scope is its arguments, including corpus-wide
    generation and audits; no baseline was weakened.
- check_id: generate-0
  name: just audit-proposals
  command: just audit-proposals
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000729
  - traitmech:000728
  - traitmech:000682
  summary: Completed native command. Scope is its arguments, including corpus-wide
    generation and audits; no baseline was weakened.
- check_id: generate-1
  name: just ground-predicates
  command: just ground-predicates
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000729
  - traitmech:000728
  - traitmech:000682
  summary: Completed native command. Scope is its arguments, including corpus-wide
    generation and audits; no baseline was weakened.
- check_id: generate-2
  name: just ground-nodes
  command: just ground-nodes
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000729
  - traitmech:000728
  - traitmech:000682
  summary: Completed native command. Scope is its arguments, including corpus-wide
    generation and audits; no baseline was weakened.
- check_id: generate-3
  name: just audit-graphs
  command: just audit-graphs
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000729
  - traitmech:000728
  - traitmech:000682
  summary: Completed native command. Scope is its arguments, including corpus-wide
    generation and audits; no baseline was weakened.
- check_id: generate-4
  name: just audit-graph-protein-taxa
  command: just audit-graph-protein-taxa
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000729
  - traitmech:000728
  - traitmech:000682
  summary: Completed native command. Scope is its arguments, including corpus-wide
    generation and audits; no baseline was weakened.
- check_id: generate-5
  name: just audit-predicate-domains
  command: just audit-predicate-domains
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000729
  - traitmech:000728
  - traitmech:000682
  summary: Completed native command. Scope is its arguments, including corpus-wide
    generation and audits; no baseline was weakened.
- check_id: generate-6
  name: just check-biolink-coverage
  command: just check-biolink-coverage
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000729
  - traitmech:000728
  - traitmech:000682
  summary: Completed native command. Scope is its arguments, including corpus-wide
    generation and audits; no baseline was weakened.
- check_id: generate-7
  name: just audit-snippets
  command: just audit-snippets
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000729
  - traitmech:000728
  - traitmech:000682
  summary: Completed native command. Scope is its arguments, including corpus-wide
    generation and audits; no baseline was weakened.
- check_id: generate-8
  name: just gen-discussions-data
  command: just gen-discussions-data
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000729
  - traitmech:000728
  - traitmech:000682
  summary: Completed native command. Scope is its arguments, including corpus-wide
    generation and audits; no baseline was weakened.
- check_id: generate-9
  name: just gen-qc-dashboard
  command: just gen-qc-dashboard
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000729
  - traitmech:000728
  - traitmech:000682
  summary: Completed native command. Scope is its arguments, including corpus-wide
    generation and audits; no baseline was weakened.
- check_id: generate-10
  name: just gen-pages
  command: just gen-pages
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000729
  - traitmech:000728
  - traitmech:000682
  summary: Completed native command. Scope is its arguments, including corpus-wide
    generation and audits; no baseline was weakened.
- check_id: generate-11
  name: just gen-priority-dashboard
  command: just gen-priority-dashboard
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000729
  - traitmech:000728
  - traitmech:000682
  summary: Completed native command. Scope is its arguments, including corpus-wide
    generation and audits; no baseline was weakened.
- check_id: focused-pending
  name: Final focused gates
  status: unavailable
  required: true
  target_ids:
  - traitmech:000729
  - traitmech:000728
  - traitmech:000682
  summary: Still running when this original finding was saved; no final success claimed.
    Required before publication.
- check_id: verify-pending
  name: Final verify gates
  status: unavailable
  required: true
  target_ids:
  - traitmech:000729
  - traitmech:000728
  - traitmech:000682
  summary: Still running when this original finding was saved; no final success claimed.
    Required before publication.
- check_id: tests-pending
  name: Final tests gates
  status: unavailable
  required: true
  target_ids:
  - traitmech:000729
  - traitmech:000728
  - traitmech:000682
  summary: Still running when this original finding was saved; no final success claimed.
    Required before publication.
- check_id: products
  name: products
  command: /tmp/traitmech-cellular-contraction-products-20261014.py
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000729
  - traitmech:000728
  - traitmech:000682
  summary: 'Integrity assertions passed: 1124 records, 1121 untouched old YAMLs, both
    child definitions/snippets/prior history preserved, protected record unchanged;
    old proposals, histories, reviews, embeddings and templates preserved. 1120 old
    pages are footer-only. Only phenotype child count changes in existing priority
    rows, 204 to 203. RDF contains 15/12628/12632 triples in classes/merged/reasoned
    graphs, real w3id phenotype/quality hierarchy and only Katoh/local-record definition
    annotation; historical child axioms are requested in narrative, not emitted.'
- check_id: browser
  name: browser
  command: node /tmp/traitmech-cellular-contraction-browser-20261014.cjs
  status: passed
  required: true
  exit_code: 0
  expected_exit_code: 0
  target_ids:
  - traitmech:000729
  - traitmech:000728
  - traitmech:000682
  summary: Chrome 1440/390 checks passed source/identity, three quotes, three parent
    discussions, two child links, open assay question, history, browse navigation,
    dashboard count/image and overflow/errors. All eight screenshots visually inspected.
- check_id: embeddings
  name: Configured embedding source applicability
  status: not_applicable
  required: false
  target_ids:
  - traitmech:000729
  - traitmech:000728
  - traitmech:000682
  summary: Both exact configured source paths absent in owned and main layouts; existing
    artifacts retained, not regenerated.
- check_id: whitespace
  name: Scoped ROBOT header whitespace
  status: passed
  required: true
  target_ids:
  - traitmech:000729
  - traitmech:000728
  - traitmech:000682
  summary: Ordinary staged diff check returned 2 solely for the three required empty
    trailing TSV directive cells. Inspected canonical 11-column headers; separate
    non-TSV and exact-path blank-at-eol exception checks returned 0. No global exemption.
evidence:
- evidence_id: source-0
  kind: primary_source
  reference: DOI:10.1242/jeb.189.1.163
  locator: Scientific abstract, numbered item 3, first clause; https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9317557+AND+SRC%3AMED&resultType=core&format=json.
    Access time records cached-source reread and hash verification, not first acquisition.
  accessed_at: '2026-10-14T23:01:07Z'
  support: supports
  snapshot_sha256: e0ca327e3218fec881bbed883eea7c892e2858131c01382e12f7f936e0d445b4
  summary: Katoh and Naitoh 1994, PMID:9317557, scientific Abstract item 3, first
    clause. Direct namespace-qualified Europe PMC MED match; native VERIFIED. The
    same sentence contrasts graded cell-body shrinkage with all-or-nothing stalk coiling.
    This supports the curator-synthesized body/projection-shortening parent, not a
    universal calcium threshold. Other abstract items use Triton-extracted preparations,
    not the living-cell injection assay. Calcium-induced calcium release is an assumption,
    not direct molecular proof. Publisher requests returned 403; full Methods, figures
    and strain provenance were not accessed.
- evidence_id: source-1
  kind: primary_source
  reference: DOI:10.2108/zsj.20.1367
  locator: Scientific abstract, opening sentence; https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14624035+AND+SRC%3AMED&resultType=core&format=json.
    Access time records cached-source reread and hash verification, not first acquisition.
  accessed_at: '2026-10-14T23:01:07Z'
  support: supports
  snapshot_sha256: ceac41c64cf671b769bc3d43666fbae0c2057ba177efbf899a2622c1c2bd1e90
  summary: Khan et al. 2003, PMID:14624035, scientific Abstract opening sentence.
    Direct namespace-qualified Europe PMC MED match; native VERIFIED. This supports
    stimulated shortening of a cytoplasmic projection rather than whole-cell locomotion.
    Reported calcium dependence and speed apply to this assay, not every member of
    the parent class. Non-detection of other filaments after fixation is not proof
    of their absence. Full Methods and figures were not accessed; the publisher's
    HTTP 200 response was an access challenge, not readable article content. Current
    taxonomic and culture identities remain unresolved.
- evidence_id: source-2
  kind: primary_source
  reference: DOI:10.1083/jcb.118.3.585
  locator: Results, Kinetics of the Contraction, printed page 588, right column; https://pdfs.semanticscholar.org/20fc/996490bf001a841702e28a552eee5f6e50e7.pdf.
    Access time records cached-source reread and hash verification, not first acquisition.
  accessed_at: '2026-10-14T23:01:07Z'
  support: supports
  snapshot_sha256: 40e9c083574fa7f845ac304286c40116e135881485508d70214ed5b28746fda1
  summary: Febvre-Chevalier and Febvre 1992, PMID:1639845, PMCID:PMC2289557, Results,
    Kinetics of the Contraction, printed page 588, right column. Direct extracted-PDF
    match with the typeset passage visually checked; native NOT_IN_ABSTRACT retained.
    The primary PDF was retrieved from its Semantic Scholar mirror after official
    PDF attempts failed. Selected Methods/Results and actual Figures 1 and 3-6 were
    inspected. Length was measured from head top to stalk base, not isolated cell-body
    length; graph axes use stalk length. The percentage is study-specific. Natural-seawater
    responses differ from artificially slowed responses. The specimens were collected
    near Villefranche and cultured at 14-18 C; current taxonomic identity is not verified.
    The n=20 initial-length sample is not asserted as independent contraction replication.
    Microtubule disassembly accompanies shortening, but this study expressly does
    not establish force production. Its disassembly half-time is not automatically
    contraction duration. The accessible JATS contains an abstract and PDF pointer,
    not the complete experimental text.
- evidence_id: hierarchy
  kind: record_content
  reference: data/traits/physiology/cellular_contraction.yaml
  locator: Complete new record and both child definitions, parent_traits, discussions
    and histories.
  accessed_at: '2026-10-14T23:01:07Z'
  support: supports
  snapshot_sha256: 74ac2ccac8a856faff4095d47c20580f1b781a841caeb3b06a69280dc13125f0
  summary: A shortening-defined physiological phenotype, not force production in general,
    locomotion, a protein sequence, an organelle or assay row. Both child definitions
    entail this broader endpoint. Their prior rationales/evidence/history remain intact;
    only the parent component is resolved and axopodial assay comparability remains
    OPEN.
- evidence_id: implementation
  kind: record_content
  reference: scripts/add_cellular_contraction_trait.py
  locator: Complete writer, controlled-fixture tests, three append-only histories
    and skill clarification.
  accessed_at: '2026-10-14T23:01:07Z'
  support: supports
  snapshot_sha256: e924e40ae9145b59f7e6ec4a43c337ff64cf118c0b6f621abb83c4ceb98be5ee
  summary: Dry-run default; exact structured preimage hashes and whole-result replay
    checks; all three records prevalidated before production writes. Source URL qualification
    preserves scientific excerpts. Every changed trait has a per-record event and
    native history. No human review promotion; all remain PROPOSED.
- evidence_id: novelty
  kind: search
  reference: proposals/metpo_traitmech_v605/proposal.md
  locator: Identity/allocation section and captured source-sidecar receipts.
  accessed_at: '2026-10-14T23:01:07Z'
  support: supports
  snapshot_sha256: b329dc54a85fdf1a4afb8a9fcabfb71cf769e4de2308d35c6e06e203503f908b
  summary: Accepted bounded search distinguishes two narrower children from unrelated
    contraction endpoints and numeric lookalikes. No additional exact parent, synonym
    or graph-node migration was accepted. Pinned/current/editor ontology assessment
    distinguishes related deprecated locomotion IDs and active phenotype hierarchy.
    v605 reserves the full block but emits one class; old cohorts remain unchanged.
  search_scope: Ignored/hidden current files in 199 known locations; 149 retained
    heads; all changed nonremoved blobs in 13 open/draft PRs plus 587 selected upstream
    owners. Original 1722 lexical variants assessed at maintained-owner level; added
    bare-contraction matches checked. Full-content ranges include 52939 owner contexts
    and 2637 unique contents. Not a whole-host crawl, archive/symlink reconstruction,
    unchanged-PR-tree audit or literature exhaustion. Earlier catalogue guard failure
    remains documented and was superseded by a fresh stable acceptance scan.
- evidence_id: products
  kind: validation
  reference: reports/proposal_citation_audit.tsv
  locator: Native generated products plus independent preservation, parsed-RDF and
    browser checks.
  accessed_at: '2026-10-14T23:01:07Z'
  support: supports
  snapshot_sha256: 98275d4165e89a998586c413c87259ef5361398b0f7598a07f0de5e55b7b0707
  summary: Maintained generation agrees with the new parent and two child repairs;
    only intended scientific owners change. Unrelated page churn is corpus-footer
    counts, not curation.
- evidence_id: sidecar
  kind: record_content
  reference: research/traits/physiology/cellular_contraction-source-verification.json
  locator: child_repair.current_parent and source-sidecar top-level written-curation
    status; compare both child parent_traits.
  accessed_at: '2026-10-14T23:01:07Z'
  support: supports
  snapshot_sha256: 3188d8c1e78d4375bae4b3d6e5d2f2b9e06bb6ebd4d5432dcaafe11dda156c8c
  summary: The original sidecar copied pre-curation proposed_repair.current_parent=METPO:1000059
    without identifying it as pre-change. Written child YAMLs instead have direct
    parent traitmech:000729. The ontology and evidence remain correct; the sidecar
    is temporally ambiguous.
assessments:
- assessment_id: identity
  area: identity
  topic: Observable shortening phenotype
  summary: The qualified label and endpoint distinguish active body/projection shortening
    from generic contractility, locomotion, molecular machines and static morphology.
  target_ids:
  - traitmech:000729
  evidence_ids:
  - hierarchy
  - source-0
  - source-1
  - novelty
  outcome: supported
- assessment_id: hierarchy
  area: grounding
  topic: Strictly broader parent
  summary: Both child definitions entail the new parent. Phenotype remains their ancestor;
    no disjoint taxa, process equivalence or common molecular mechanism follows.
  target_ids:
  - traitmech:000729
  - traitmech:000728
  - traitmech:000682
  evidence_ids:
  - hierarchy
  - source-0
  - source-1
  outcome: supported
- assessment_id: sources
  area: evidence
  topic: Primary-result scope and source fidelity
  summary: Three concise primary-result excerpts support shortening. Living cells
    and extracted preparations, body and head-to-stalk length, natural and slowed
    responses, and native abstract versus direct PDF verdicts remain distinct. The
    percentage and calcium observations are not universal.
  target_ids:
  - traitmech:000729
  evidence_ids:
  - source-0
  - source-1
  - source-2
  outcome: supported
- assessment_id: preservation
  area: consistency
  topic: Child scope and independent questions
  summary: Only the hierarchy question is resolved; prior rationales, definitions,
    excerpts and histories remain, and the axopodial assay question is explicitly
    OPEN.
  target_ids:
  - traitmech:000728
  - traitmech:000682
  evidence_ids:
  - hierarchy
  - products
  outcome: supported
- assessment_id: mutation
  area: provenance
  topic: Guarded curation and histories
  summary: Exact preimages, replay refusal, prevalidation, agent-attributed events
    and native histories protect the scoped changes.
  target_ids:
  - traitmech:000729
  - traitmech:000728
  - traitmech:000682
  evidence_ids:
  - implementation
  outcome: supported
- assessment_id: sidecar
  area: provenance
  topic: Temporal parent state
  summary: The post-curation sidecar carries child_repair.current_parent=METPO:1000059
    from the research plan. The written children instead have direct parent traitmech:000729;
    phenotype remains an ancestor. Separate historical and applied state so provenance
    readers do not receive conflicting direct-parent assertions.
  target_ids:
  - traitmech:000729
  - traitmech:000728
  - traitmech:000682
  evidence_ids:
  - sidecar
  - hierarchy
  outcome: concern
- assessment_id: products
  area: consistency
  topic: Proposal and rendered products
  summary: Standalone proposal emits one correctly rooted class; child axioms remain
    explicit upstream requests. Generated pages, discussions and counts reflect the
    coupled repair.
  target_ids:
  - traitmech:000729
  - traitmech:000728
  - traitmech:000682
  evidence_ids:
  - products
  - novelty
  outcome: supported
- assessment_id: limits
  area: completeness
  topic: Taxonomic and molecular gaps
  summary: No canonical taxa or proteins are asserted. Isolate identities, mechanisms,
    exact mappings and comparative assays remain open, not falsely completed by sequence
    evidence or hierarchy repair.
  target_ids:
  - traitmech:000729
  - traitmech:000728
  - traitmech:000682
  evidence_ids:
  - hierarchy
  - source-0
  - source-1
  - source-2
  outcome: unknown
findings:
- finding_id: sidecar-parent-state
  issue_key: cellular-contraction-sidecar-parent-state
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Source sidecar presents the pre-change direct parent as current
  description: The post-curation sidecar carries child_repair.current_parent=METPO:1000059
    from the research plan. The written children instead have direct parent traitmech:000729;
    phenotype remains an ancestor. Separate historical and applied state so provenance
    readers do not receive conflicting direct-parent assertions.
  target_ids:
  - traitmech:000729
  - traitmech:000728
  - traitmech:000682
  field_paths:
  - child_repair.current_parent
  evidence_ids:
  - sidecar
  - hierarchy
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: research/traits/physiology/cellular_contraction-source-verification.json
    role: maintained evidence provenance
  - repository: CultureBotAI/TraitMech
    path: tests/test_add_cellular_contraction_trait.py
    role: regression assertions
  external_issues:
  - https://github.com/CultureBotAI/TraitMech/issues/1939
actions:
- action_id: clarify-parent-state
  description: Label the pre-change direct parent and record the accepted post-change
    direct parent; test both against the coupled YAML state without changing scientific
    evidence or histories.
  finding_ids:
  - sidecar-parent-state
  target_ids:
  - traitmech:000729
  - traitmech:000728
  - traitmech:000682
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: research/traits/physiology/cellular_contraction-source-verification.json
    role: maintained evidence provenance
  - repository: CultureBotAI/TraitMech
    path: tests/test_add_cellular_contraction_trait.py
    role: regression assertions
  acceptance_checks:
  - Explicit pre_change_parent=METPO:1000059 and post_change_parent=traitmech:000729.
  - Regression test agrees with both child parent_traits.
  - Prior source receipts and histories byte-preserved; linked successor review saved.
related_reviews: []
limitations:
- Self-review and PROPOSED curation, not independent review or human sign-off.
- Complete parent assessment; children only for the coupled changes and preservation,
  not their entire literature.
- Katoh and Khan scientific abstracts accessible; full Methods/figures unavailable.
  Publisher 200 for Khan was an access challenge. Febvre selected printed pages 585/586/588
  and actual Figures 1/3-6 inspected; other rendered pages were not treated as viewed.
  Reread printed 588 during formal review.
- Febvre native NOT_IN_ABSTRACT remains unchanged despite a verified primary-PDF match.
  Its total-length endpoint is not isolated body length; microtubule breakdown is
  not demonstrated force production.
- Correction/retraction checks cover specific MED/Crossref fields and available sources,
  not comprehensive clearance.
- No universal trigger, speed, shortening fraction, calcium threshold, ATP mechanism,
  ecological role, exact synonym or external equivalence inferred. Protein sequence
  features alone do not establish the phenotype.
- Source acquisition and reservation receipts are retained with stable URLs/hashes;
  temporary raw files are not guaranteed long-term availability. Known-copy searches
  do not establish exhaustive global discovery.
- Embedding inputs unavailable; existing embeddings preserved. No paid research used.
links:
- https://github.com/CultureBotAI/TraitMech/issues/1939
tags:
- add-trait
- cellular-contraction
- self-review
```
