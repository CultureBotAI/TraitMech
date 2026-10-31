# Whole-record review of pressure range

- Review: 20261021T215151Z-pressure-range
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-21T21:42:04.170213Z
- Finished UTC: 2026-10-21T21:51:51Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Needs curation: one grouped imported-role major and four bounded minors for historical GO mapping precision, hydration explanation, snippet format and human-acceptance traceability; canonical pressure interval remains directly supported.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: Fourth record of the actual locally initialized batch 012 queue. Whole 218-line target and all 68 captured inputs verified before assessment; interval, optimum and derived breadth remain distinct. Local initialization at 21:02:18.445284 UTC does not assert publication of batch 011.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8eee04a8c65609fbaff6df7c54597dcaf1b9d282.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| traitmech:000005 | data/traits/environment/pressure_range.yaml | maintained | pressure range |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full-corpus graph audit | passed | True | traitmech:000005 | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| Full-corpus snippet audit | passed | True | traitmech:000005 | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| Full-corpus pathway links | passed | True | traitmech:000005 | 19 links checked against the pinned PathwayMech snapshot. |
| Full-corpus history integrity | passed | True | traitmech:000005 | 1277 history records checked, zero invalid links at the 8eee source base; integrity does not establish science or human acceptance. |
| Initial full-product validation | failed | False | traitmech:000005 | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation with isolated local cache | failed | False | traitmech:000005 | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation after isolated-cache download | passed | True | traitmech:000005 | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| Focused native validation | passed | True | traitmech:000005 | Successful schema validation; source and semantics separately assessed. |
| Focused strict validation | passed | True | traitmech:000005 | Successful strict validation; no biological efficacy certification. |
| Focused network snippet check | passed | True | traitmech:000005 | Direct authorized network invocation passed with two NOT_IN_ABSTRACT results. No target-specific initial failed attempt. Actual primary review establishes one literal and one supported unit transcription. |
| Reused maintained batch-eleven QC | passed | True | traitmech:000005 | Actual B11 final QC at its original time, qualified against B12 bytes; independent of pending publication. |
| Protein-instance metadata applicability | not_applicable | False | traitmech:000005 | Zero protein classes and instances in the contextual interval graph; no forced accession or detailed pressure-response query. |

## Scientific And Domain Assessments

### Native checklist: range identity and broader-family grounding

identity: concern. Targets: traitmech:000005.

The retained min/max pressure-range fallback, exact proposed 1007604 and active phenotype parent are coherent. GO0006636 is a meaningful broader unsaturated-fatty-acid process family for PUFA synthesis; only the maintained historical exactMatch claim is a bounded precision concern. Preserve the current PATHWAY and qualified CURIE.

### Native checklist: growth-supporting pressure interval

evidence: supported. Targets: traitmech:000005.

The assigned primary abstract directly reports MTCD1 growth from 80 to 140 MPa at 6 °C. Minimum/maximum bounds differ from the optimum coordinate of 120 MPa and the derived interval breadth of 60 MPa. Generic review classification supports context without requiring the source to coin the local trait label.

### Native checklist: parent and local predicate authorities

identity: supported. Targets: traitmech:000005.

Active phenotype parent is appropriate. Exact local defines admits an axis parameterizing a numerical trait and Biolink association has broad named-thing endpoints. Neither imports a process-only restriction. Three lexical expands/stabilizes edges do not silently inherit RO constraints.

### Native checklist: all assigned citations and placements

evidence: unknown. Targets: traitmech:000005.

Four works and eleven external placements are accounted for. Generic membrane and solute context is attributable with exceptions. Expansion of the full minimum/maximum interval at edge 4 remains UNKNOWN from the inspected nearest source, not refuted. Colwellia abstract, actual review bodies and derived HAL text are distinguished.

### Native checklist: literal unit-format fidelity

evidence: concern. Targets: traitmech:000005.

First snippet supports all interval, optimum and temperature values after degrees C to °C normalization; only literal format differs. Second snippet is literal in the assigned membrane body. Native NOT_IN_ABSTRACT results remain unchanged.

### Native checklist: strain and temperature-specific range

evidence: supported. Targets: traitmech:000005.

Colwellia marinimaniae MTCD1 range 80–140 MPa at 6 °C is explicitly reported by the assigned abstract. The source optimum 120 MPa and derived breadth 60 MPa are separate quantities. Official species/type aliases verify identity without supplying the phenotype.

### Native checklist: all nine current referents

consistency: concern. Targets: traitmech:000005.

Pressure condition, interval/fluidity QUALITY, biosynthetic PATHWAY, chemical constituents and explicit accumulation/stabilization processes fit their current descriptions. GO broad-family grounding remains qualified positive; root counts only the historical exactMatch precision as minor while retaining grounding-auditor dissent. No forced replacement, retype, protein or numeric-value finding.

[{"index": 0, "node": {"node_id": "pressure_range_trait", "label": "pressure range", "node_type": "TRAIT", "grounding": "traitmech:000005", "description": "Bounded min-to-max hydrostatic pressure supporting growth."}, "assessment": "supported", "reason": "Self-grounded min/max growth interval agrees with definition."}, {"index": 1, "node": {"node_id": "hydrostatic_pressure", "label": "hydrostatic pressure", "node_type": "ENVIRONMENTAL_FACTOR", "description": "Ambient hydrostatic pressure imposed on the cell.", "grounding": "PATO:0001025"}, "assessment": "supported", "reason": "Ambient pressure condition close-matches the primary pressure quality."}, {"index": 2, "node": {"node_id": "bounded_growth_span", "label": "growth-permissive pressure span", "node_type": "QUALITY", "description": "Continuous interval of hydrostatic pressures supporting growth."}, "assessment": "supported", "reason": "Continuous permissible interval is a measured QUALITY, not a growth-maintenance process or scalar delta."}, {"index": 3, "node": {"node_id": "pufa_biosynthesis", "label": "polyunsaturated fatty acid biosynthesis", "node_type": "PATHWAY", "description": "Synthesis of polyunsaturated fatty acids incorporated into membrane lipids.", "grounding": "GO:0006636"}, "assessment": "qualified_positive", "reason": "GO:0006636 is the active unsaturated fatty acid biosynthetic process, defined by one or more double bonds; polyunsaturated fatty acid biosynthesis is explicitly a narrow synonym. This provides a meaningful broader process-family grounding for current PUFA synthesis, not an exact label-equivalent term. Historical mapping row 192 labels it exactMatch under BIOLOGICAL_PROCESS, which overstates the primary synonym scope. Current node is PATHWAY and already grounded; the mapper type key and nonempty guard prevent straightforward replay. No wrong-material-ID claim or forced PATHWAY retype follows."}, {"index": 4, "node": {"node_id": "membrane_fluidity_hhp", "label": "membrane fluidity under high hydrostatic pressure", "node_type": "QUALITY", "description": "Degree of membrane lipid disorder/fluidity maintained against pressure-induced ordering."}, "assessment": "supported", "reason": "Membrane lipid disorder/fluidity explicitly denotes a measurable quality, not the process maintaining it."}, {"index": 5, "node": {"node_id": "unsaturated_membrane_lipids", "label": "unsaturated membrane lipids", "node_type": "CHEMICAL", "description": "Unsaturated fatty acids in membrane phospholipids that counter pressure-induced ordering."}, "assessment": "supported", "reason": "Fatty acids in membrane phospholipids are chemical constituents; detailed effects belong to the bounded source audit."}, {"index": 6, "node": {"node_id": "tmao", "label": "trimethylamine N-oxide (TMAO)", "node_type": "CHEMICAL", "description": "Compatible solute / piezolyte excluded from the protein hydration layer."}, "assessment": "supported", "reason": "Named TMAO is a chemical referent; absent chemical CURIE alone does not create a mandatory grounding or instance gap."}, {"index": 7, "node": {"node_id": "protein_stabilization", "label": "protein stabilization via preferential hydration", "node_type": "BIOLOGICAL_PROCESS", "description": "Stabilization of native protein structure by preferential exclusion of cosolutes."}, "assessment": "supported", "reason": "Stabilization is explicitly a biological process; detailed physical efficacy is unassessed."}, {"index": 8, "node": {"node_id": "compatible_solute_accumulation", "label": "compatible solute accumulation", "node_type": "BIOLOGICAL_PROCESS", "description": "Accumulation of compatible solutes (betaine, glutamate, beta-hydroxybutyrate) acting as piezolytes."}, "assessment": "supported", "reason": "Accumulation is explicitly a biological process, not a protein or a material solute pool."}]

### Native checklist: all seven relation roles

consistency: concern. Targets: traitmech:000005.

RO2213 at edges 2/3 inherits process/process requirements. Edge 2 has a valid processual biosynthetic subject but explicit fluidity QUALITY object; edge 3 links CHEMICAL constituents to a TRAIT. Group these roles once. Broad local/Biolink relations and lexical edges have no invented imported exclusion.

[{"index": 0, "edge": {"subject": "hydrostatic_pressure", "predicate": "defines", "object": "pressure_range_trait", "description": "The hydrostatic-pressure axis defines the min/max bounds bracketed by the pressure range.", "evidence": [{"reference": "DOI:10.3389/fmolb.2022.1058381", "notes": "Pressure-adaptation review frames the bounded span of growth-permissive pressure as a defining quantitative descriptor."}], "predicate_id": "METPO:2007500"}, "assessment": "supported", "reason": "Exact local v4 defines supports a pressure measurement axis parameterizing interval bounds."}, {"index": 1, "edge": {"subject": "pressure_range_trait", "predicate": "associated with", "object": "bounded_growth_span", "description": "The pressure range records the bounded interval of permissive hydrostatic pressures.", "evidence": [{"reference": "DOI:10.1099/ijsem.0.001671", "notes": "Colwellia marinimaniae MTCD1 illustrates a bounded growth-supporting pressure span (80-140 MPa)."}], "predicate_id": "biolink:associated_with"}, "assessment": "qualified_positive", "reason": "Biolink associated-with has broad named-thing endpoints; current correspondence records the measurement interval and is not an independent causal-effect claim."}, {"index": 2, "edge": {"subject": "pufa_biosynthesis", "predicate": "increases", "object": "membrane_fluidity_hhp", "description": "PUFA biosynthesis increases membrane fluidity to counter pressure-induced membrane ordering.", "evidence": [{"reference": "DOI:10.3389/fmolb.2022.1058381", "notes": "PUFAs (C20:5, C22:6) associated with adaptation to high hydrostatic pressure; broad mechanism across taxa."}], "predicate_id": "RO:0002213"}, "assessment": "major", "reason": "RO2213 inherits process/process roles. The named biosynthetic PATHWAY subject is processual, but its object is explicitly membrane fluidity QUALITY, not a fluidity-maintenance process. The object mismatch is independently sufficient."}, {"index": 3, "edge": {"subject": "unsaturated_membrane_lipids", "predicate": "positively regulates", "object": "pressure_range_trait", "description": "Unsaturated membrane lipids support growth across high hydrostatic pressures.", "evidence": [{"reference": "DOI:10.3389/fmolb.2022.1058381", "notes": "Mutants with reduced C18:1 could not withstand high pressure; unsaturation counters pressure ordering."}], "predicate_id": "RO:0002213"}, "assessment": "major", "reason": "RO2213 process/process relation connects explicit chemical constituents to a TRAIT class; current support-for-growth prose does not turn those endpoints into processes. Group with edge2 as one imported-role issue."}, {"index": 4, "edge": {"subject": "membrane_fluidity_hhp", "predicate": "expands", "object": "pressure_range_trait", "description": "Maintaining membrane fluidity under pressure expands the growth-supporting pressure range.", "evidence": [{"reference": "DOI:10.3390/microorganisms11071629", "notes": "Pressure compacts membranes; organisms restore membrane disorder/function via unsaturation to sustain growth."}]}, "assessment": "lexical_qualified", "reason": "Ungrounded expands has no imported RO constraint. Current quality-to-range language is intelligible, but exact empirical expansion and generality are source-scope questions, not an inferred formal-domain error."}, {"index": 5, "edge": {"subject": "tmao", "predicate": "stabilizes", "object": "protein_stabilization", "description": "TMAO stabilizes proteins via preferential hydration (preferential exclusion from hydration layer).", "evidence": [{"reference": "DOI:10.1021/acs.chemrev.3c00432", "notes": "TMAO preferentially excluded from protein hydration layer causing preferential hydration; biophysical mechanism, not microbe-specific."}]}, "assessment": "lexical_qualified", "reason": "Ungrounded stabilizes does not inherit RO enables or regulates roles. Chemical-to-stabilization context can be described without inventing an imported material-executor restriction; source-specific physical wording is separately audited."}, {"index": 6, "edge": {"subject": "compatible_solute_accumulation", "predicate": "stabilizes", "object": "protein_stabilization", "description": "Compatible solutes stabilize proteins via preferential hydration.", "evidence": [{"reference": "DOI:10.3390/microorganisms11071629", "notes": "Compatible solutes (glutamate, betaine, beta-hydroxybutyrate) act by preferential hydration, displacing protein-bound water."}]}, "assessment": "lexical_qualified", "reason": "Ungrounded stabilizes links accumulation to stabilization processes without an imported relation ID. Formal annotation gap alone is not a mandatory defect; detailed hydration wording and efficacy are separately source-scoped."}]

### Native checklist: generic physical attribution and hydration wording

evidence: concern. Targets: traitmech:000005.

Piezolytes paragraph 26 faithfully supplies the water-displacement note, while assigned ChemRev explains cosolute exclusion with preferential protein hydration, agreeing with current nodes 6/7 and edge 5. Preserve that explanatory inconsistency as a bounded note concern, not a fabricated citation. Lipid and solute effects vary with taxa/conditions. Detailed pathogen pressure-defense, fitness, AMR, intervention efficacy and methods remain UNASSESSED_SCOPE.

### Native checklist: NONMECHANISTIC applicability

completeness: supported. Targets: traitmech:000005.

Two disclosed components, zero protein classes and zero instances are proportionate to the contextual interval graph. No mandatory connector, molecular instance, extra canonical or experiment is prescribed; ungrounded lexical relations are not automatically defects.

### Native checklist: catalog applicability and bounded query scope

evidence: unknown. Targets: traitmech:000005.

Canonical Colwellia/MTCD1 aliases do not match the retained 20-organism / 28-dataset catalog. Other source-organism coverage is not globally denied. No strain-resolved locus or detailed pressure-response query was run.

### Native checklist: current assertions and conditional mappings

provenance: supported. Targets: traitmech:000005.

Record owns current assertions. Wildcard predicate mapping and shared grounder recur only on empty IDs and skip current nonempty values. Historical PUFA exactMatch row is keyed BIOLOGICAL_PROCESS rather than current PATHWAY, also preventing simple replay. Exact PATHWAY normalization and canonical backfill are positive context; sibling writers are not asserted current repair owners.

### Native checklist: bounded acceptance trace

provenance: concern. Targets: traitmech:000005.

Ten current events are all AI. Ignored-inclusive discovery found zero repository history leads; 217 matching paths and 69 structured review arrays contain zero exact current-target arrays. This bounds the missing acceptance link without excluding remote or private review.

### Native checklist: actual checks and local preparation

consistency: supported. Targets: traitmech:000005.

All 68 inputs match. Current native, strict and direct network snippet commands pass, without an invented initial target-specific failure. Historical common failures/retries remain preserved. Actual B11 QC/B12 qualification/postcheck and local initialization are distinct from pending publication. The wrapper diagnostic after completed capture is not a native-review failure.

## Findings

### process-regulation-roles: Process regulation is assigned to quality and trait endpoints

major / open / confirmed; issue key: pressure-range-process-regulation-roles.

RO2213 inherits process domain and range. Edge 2 has a meaningful biosynthetic PATHWAY subject but a membrane-fluidity QUALITY object; edge 3 connects CHEMICAL constituents to the pressure-range TRAIT. Growth-support prose does not change those referents. Group both mismatches, preserving current node facets and contextual source evidence without prescribing detailed mechanism repair.

### go-mapping-precision: Historical mapping overstates a broader-family match as exact

minor / open / confirmed; issue key: pressure-range-go-mapping-precision.

GO0006636 covers unsaturated-fatty-acid biosynthesis with one or more double bonds and marks PUFA biosynthesis as a narrow synonym. The current CURIE remains a meaningful broader family; maintained historical mapping row 192 labels the narrower phrase exactMatch. Qualify that provenance, without asserting a wrong current CURIE or forced PATHWAY retype. Current type and nonempty guards prevent automatic replay. Ground auditor preferred a limitation; root/challenger calibrated this narrow mapping precision as minor.

### hydration-explanation-precision: Assigned hydration explanations conflict

minor / open / confirmed; issue key: pressure-range-hydration-explanation-precision.

The edge 6 note faithfully follows the piezolyte review in describing displacement of protein-bound water. Assigned ChemRev describes cosolute exclusion with preferential protein hydration, agreeing with current nodes 6/7 and edge 5. Preserve the source disagreement and qualify this explanatory note; do not call the attribution fabricated or infer a universal solute mechanism.

### literal-unit-format: Snippet changes the supported temperature-unit notation

minor / open / confirmed; issue key: pressure-range-literal-unit-format.

The record writes degrees C where the actual primary abstract uses °C. Interval, optimum and temperature remain supported after normalization; only literal copied-span fidelity is implicated. The canonical 80–140 MPa range at 6 °C remains positive.

### human-acceptance-link: Reviewed status lacks a locally attributable acceptance link

minor / open / confirmed; issue key: pressure-range-human-acceptance-link.

Ten AI events, zero matching repository history leads and ignored-inclusive 217 matching paths/69 parsed review arrays/zero exact targets do not identify current-target human acceptance. This bounded traceability gap does not rule out private or remote review.

## Recommended Actions And Acceptance Checks

### reconcile-imported-roles

Reconcile edges 2/3 imported process-regulation roles with their actual referents during authorized curation.

- Preserve valid processual pathway and measured-quality facets and contextual source evidence.
- Respect nonempty-ID guards; mapping changes alone do not repair current assertions.
- No detailed mechanism reconstruction or intervention prescription.

### qualify-go-mapping

Qualify historical mapping exactness and the retained broader-family grounding.

- Preserve current meaningful GO family and PATHWAY type unless separate evidence warrants change.
- Do not require an invented replacement CURIE or claim unconditional replay.
- Retain the independent grounding severity qualification.

### clarify-hydration-note

Clarify the conflicting hydration explanation while preserving accurate source attribution.

- Identify the source disagreement explicitly; do not silently report the note as a fabricated quote.
- Retain non-microbial-specific physical context and taxon/condition limitations.
- No experimental efficacy or intervention prescription.

### restore-literal-format

Use the actual source unit notation for the supported snippet.

- Preserve all numerical values and source identity.

### link-human-acceptance

Link attributable acceptance if available or clarify status while preserving provenance.

- Retain all ten AI events and bounded ignored-inclusive search evidence.
- No contact or automatic status promotion authorized.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| check-audit-graphs | /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; metadata audit-graphs.json | context_only | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| check-audit-snippets | /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; metadata audit-snippets.json | context_only | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| check-check-pathway-links | /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; metadata check-pathway-links.json | context_only | 19 links checked against the pinned PathwayMech snapshot. |
| check-validate-history | /private/tmp/traitmech-record-sweep-003.4opxlhgf/validate-history.log; Executed 2026-10-21T07:03:25Z through 2026-10-21T07:03:30Z; metadata validate-history.json | context_only | 1277 history records checked, zero invalid links at the 8eee source base; integrity does not establish science or human acceptance. |
| check-validate-products | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; metadata validate-products.json | context_only | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| check-validate-products-retry-local | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log; Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; metadata validate-products-retry-local.json | context_only | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| check-validate-products-retry-network | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log; Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; metadata validate-products-retry-network.json | context_only | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| check-pressure-range-native | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-native.log; Executed 2026-10-21T21:42:33.387389+00:00 through 2026-10-21T21:42:34.912640+00:00; metadata pressure-range-native.json | context_only | Successful schema validation; source and semantics separately assessed. |
| check-pressure-range-strict | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-strict.log; Executed 2026-10-21T21:42:33.387367+00:00 through 2026-10-21T21:42:37.203254+00:00; metadata pressure-range-strict.json | context_only | Successful strict validation; no biological efficacy certification. |
| check-pressure-range-snippets-network | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-snippets-network.log; Executed 2026-10-21T21:42:42.769089+00:00 through 2026-10-21T21:42:46.388498+00:00; metadata pressure-range-snippets-network.json | context_only | Direct authorized network invocation passed with two NOT_IN_ABSTRACT results. No target-specific initial failed attempt. Actual primary review establishes one literal and one supported unit transcription. |
| check-batch011-qc | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/batch011-qc.log; Executed 2026-10-21T20:52:41.208560+00:00 through 2026-10-21T20:54:10.001030+00:00; metadata batch011-qc.json | context_only | Actual B11 final QC at its original time, qualified against B12 bytes; independent of pending publication. |
| record | data/traits/environment/pressure_range.yaml; Entire current 218-line record | supports | Nine nodes, seven edges, two snippets, one canonical and ten AI events covered. |
| policy | docs/GROUNDING_POLICY.md; Captured maintained authority | supports | Referent-based identity, broader-family qualifications and imported formal roles. |
| playbook | docs/CURATION_PLAYBOOK.md; Captured maintained authority | supports | Source scope, literal copied snippets and attributable acceptance. |
| schema | src/traitmech/schema/traitmech.yaml; Captured maintained authority | supports | Current node facets and review contract. |
| checklist | .claude/skills/curate-yaml-record/references/review-checklist.md; Captured maintained authority | supports | Whole-record identity, evidence, graph, provenance and readiness checks. |
| node-mapping-primary | mappings/node_grounding.tsv; Captured maintained authority | supports | Historical row 192 exactMatch is narrower than the primary GO family; current type and nonempty guards limit replay. |
| reuse | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/common-reuse-b11-qc-supplement-qualified.json; Actual B11-to-B12 qualification | supports | Original outcomes and all current byte comparisons bound. |
| reuse-postcheck | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/common-reuse-output-verification-agent/post-execution-verification.json; Independent actual-output verification | supports | Actual output/hash postcheck; no new QC. |
| local-init | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/batch012-local-initialization-receipt.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Local-only initialization on verified prior local commit; publication status remains separately documented. |
| capture | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-grounding-agent/capture-verification.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | All 68 inputs verified before grounding assessment. |
| identity | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-grounding-agent/identity-assessment.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Retained range fallback, active parent and meaningful broader GO family. |
| node-edges | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-grounding-agent/node-edge-ledger.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | All nine nodes/seven edges and two components; imported roles separate from biology. |
| owners | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-grounding-agent/owner-provenance-assessment.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Current record, conditional RO mapping and historically narrower GO row with replay limits. |
| expression | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-grounding-agent/expression-and-readiness-assessment.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Canonical catalog applicability and zero-protein contextual graph. |
| catalog-reuse | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-grounding-agent/catalog-reuse-receipt.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Original catalog/runner receipts separate from current copies. |
| local-authority | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-grounding-agent/local-authority-excerpts.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Exact v5/v4 proposals, maintained mappings, schema and Biolink. |
| ground-reading | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-grounding-agent/reading-scope-receipt.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Actual selected primary/owner readings; zero matching repository histories and ten current AI events. |
| ground-manifest | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-grounding-agent/evidence-manifest.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Frozen 30 grounding artifacts verified. |
| go-dissent | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-grounding-agent/go-grounding-severity-qualification.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Ground auditor preferred a limitation; root/challenger count only historical exactMatch precision as a minor. Current broader CURIE remains meaningful. |
| taxon-reuse | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-grounding-agent/taxonomy-reuse-receipt.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Original Colwellia request and retained initial DNS failure separate from current copies. |
| metpo-primary | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/repo/data/raw/metpo.owl; Actual selected METPO XML | supports | Broader pressure tolerance is not an exact numerical-interval replacement; v5 separately sourced. |
| ro-primary | /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/ro.db; Actual RO2213 and RO2211 rows | supports | Positive regulation inherits process subject and object requirements. |
| pato-primary | /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/pato.db; Actual PATO0001025 rows | supports | Pressure physical quality supports the ambient condition identity. |
| go-primary | /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/go.db; Actual GO0006636 rows | supports | Active unsaturated-fatty-acid biosynthesis includes one or more double bonds; PUFA biosynthesis is explicitly a narrow synonym. |
| proposal-v5-primary | proposals/metpo_traitmech_v5/metpo_proposal_classes_robot.tsv; Captured TSV row 7 | supports | Proposed 1007604 preserves the exact min/max growth interval, not an installed active replacement. |
| proposal-v4-primary | proposals/metpo_traitmech_v4/metpo_proposal_properties_robot.tsv; Captured TSV row 3 | supports | Defines permits a measurement axis or feature to parameterize a numerical trait. |
| taxon-colwellia | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-grounding-agent/taxon1513592.xml; Whole official taxonomy response; original successful request time | supports | Official species and MTCD1 aliases positive; interval separately sourced. |
| meta-membrane | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-agent/membrane-metadata.json; Actual retained indexed metadata/abstract; original request time | supports | Actual review abstract describes non-universal lipid responses and pressure/temperature context; body separately bound. |
| meta-colwellia | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-agent/colwellia-metadata.json; Actual retained indexed metadata/abstract; original request time | supports | Actual primary abstract reports MTCD1 growth range 80–140 MPa at 6 °C, distinct from optimum 120 MPa. |
| meta-piezolytes | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-agent/piezolytes-metadata.json; Actual retained indexed metadata/abstract; original request time | supports | Actual review identity and abstract; selected membrane, hydration and solute observations separately bound to body. |
| body-membrane | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-agent/membrane.xml; Actual retained primary body; selected passages only | supports | Actual body paragraphs 1/9/10/12/13 provide the literal classification phrase and generic lipid context with taxon/temperature exceptions. |
| body-piezolytes | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-agent/piezolytes.xml; Actual retained primary body; selected passages only | supports | Actual body paragraphs 17/18/20/26/27 provide membrane and hydration wording with source-specific solute/condition contrasts. |
| meta-chemrev | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-agent/chemrev-metadata.json; Actual retained indexed metadata/abstract; original request time | supports | Actual review identity and abstract concerning physical crowding/cosolute effects; author-deposited body separately bound. |
| body-chemrev | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-agent/chemrev.pdf; Actual retained primary body; selected passages only | supports | Actual HAL author-deposited manuscript, cover identity/DOI verified; selected exclusion/hydration discussion and Figure 29. Derived newline extraction is separately bound. |
| chemrev-text | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-agent/chemrev.txt; Derived PDF text; newline-only 2164–2167 and Figure 29 caption 2189–2192 | context_only | Text extraction is not a fresh primary acquisition or publisher HTML; actual author PDF is separately bound. |
| sources | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-agent/source-assessment.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Final four-work audit; unit-format and hydration-explanation minors with exact interval expansion unknown. |
| source-ledger | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-agent/source-ledger.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | All four identities and distinct abstract/body reading scopes. |
| placements | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-agent/placement-ledger.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | All eleven external placements and seven grounding fields accounted for. |
| snippets | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-agent/snippet-ledger.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | One supported unit transcription and one literal phrase; numbers preserved. |
| node-sources | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-agent/node-source-ledger.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | All nine source node contexts. |
| edge-sources | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-agent/edge-source-ledger.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | All seven source edge contexts; nearest-source expansion attribution remains unknown. |
| source-status | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-agent/publication-status-ledger.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Actual returned publication-status fields; bounded history checks. |
| source-reading | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-agent/selected-primary-reading.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Actual selected readings; incidental excluded content not adopted. |
| source-access | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-agent/access-limitations.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Colwellia body not acquired/inspected; three retained actual bodies and original request limits. |
| source-reuse | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-agent/source-reuse-receipt.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Original acquisitions separate from current copies at 21:42:39 UTC. |
| canonical-scope | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-agent/canonical-assessment.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Positive strain/temperature-specific range 80–140 MPa at 6 °C. |
| hydration-scope | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-agent/hydration-wording-assessment.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Faithful piezolyte attribution conflicts with assigned exclusion/hydration explanation and current graph wording. |
| native-checks | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-agent/native-check-context.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Three focused commands pass, including direct network snippets; no current initial failed attempt. |
| source-capture | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-agent/final-capture-verification.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | All 68 captured inputs unchanged. |
| source-manifest | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-agent/evidence-manifest.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Twenty-nine frozen source artifacts verified. |
| root-reading-75 | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-root/frozen-audits-reading.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Only actual bounded root reading/observation scope; receipt hash is not an article-body hash. |
| root-reading-76 | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-root/identity-primary-reading.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Only actual bounded root reading/observation scope; receipt hash is not an article-body hash. |
| root-reading-77 | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-root/literature-primary-reading.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Only actual bounded root reading/observation scope; receipt hash is not an article-body hash. |
| root-reading-78 | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-root/ontology-primary-reading.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Only actual bounded root reading/observation scope; receipt hash is not an article-body hash. |
| root-reading-79 | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-root/owner-and-context-reading.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Only actual bounded root reading/observation scope; receipt hash is not an article-body hash. |
| root-reading-80 | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-root/root-reading-attestation.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Only actual bounded root reading/observation scope; receipt hash is not an article-body hash. |
| root-reading-81 | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-root/taxonomy-catalog-reading.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Only actual bounded root reading/observation scope; receipt hash is not an article-body hash. |
| challenge | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-semantic-challenge-agent/semantic-severity-challenge.json; Final independent challenge | supports | Exact fields, disposition and bindings verified. |
| adjudication | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-root-adjudication.json; Final root disposition | supports | Final findings and nonfindings control serialization; grounding dissent remains explicit. |

## Limits And Additional Notes

- Detailed pathogen pressure-defense, fitness, AMR, intervention efficacy and methods are UNASSESSED_SCOPE; incidental displayed source content is not adopted.
- Canonical MTCD1 interval 80–140 MPa at 6 °C is explicit, distinct from optimum 120 MPa and derived breadth 60 MPa. Colwellia primary body was not acquired/inspected; no failed new request or paper-wide absence is implied.
- Exact widening of minimum/maximum growth endpoints at edge 4 remains UNKNOWN from inspected nearest-source context. Generic lipid support and source exceptions do not prove a universal mechanism or false claim.
- Piezolyte displacement wording is faithfully cited but conflicts with the assigned cosolute-exclusion/protein-hydration explanation; source disagreement is preserved, not silently resolved as false attribution.
- GO0006636 is a meaningful broader process-family grounding. Only the historical exactMatch precision is counted; the grounding auditor preferred a limitation, and current PATHWAY/nonempty guards limit replay.
- Original metadata/body acquisitions, current copies at 21:42:39 UTC and later selected readings are separately bound. ChemRev is a HAL author-deposited manuscript with derived text, not publisher HTML or a new acquisition. Official taxonomy retains original 16:11:19–20 success and prior DNS failure.
- Fallback/proposed 1007604 is not an installed active exact replacement. Zero proteins/instances and two contextual components do not require speculative connectors or additional assays.
- Canonical catalog absence and local human-traceability search are bounded; no global source-organism absence or private-review absence is asserted.
- Actual prior QC, qualification and local initialization do not assert B11 remote publication; publication remains separately documented.
- Final root adjudication and independent challenge are pinned; no builder/helper import or execution during preparation.
- Coverage: four works/four forms, eleven external placements, seven grounding fields, nine nodes/seven edges, one canonical and two snippets: one literal and one supported unit transcription.
- No scientific record, native inventory, Git or sweep-state mutation by serializer preparation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T215151Z-pressure-range
kind: record
repository: CultureBotAI/TraitMech
title: Whole-record review of pressure range
started_at: '2026-10-21T21:42:04.170213Z'
finished_at: '2026-10-21T21:51:51Z'
reviewer:
  identity: codex
  kind: agent
  independence: independent
  independence_basis: Independent source and grounding audits, separate semantic challenge
    and bounded root primary/owner readings. Generic environmental pressure physiology,
    measurement distinctions, literal text and formal roles assessed. Detailed pathogen
    pressure-defense, fitness, AMR and intervention efficacy/methods are UNASSESSED_SCOPE.
    No scientific record edited.
  model: GPT-6 (Codex)
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'Needs curation: one grouped imported-role major and four bounded minors
  for historical GO mapping precision, hydration explanation, snippet format and human-acceptance
  traceability; canonical pressure interval remains directly supported.'
source:
  git_revision: 8eee04a8c65609fbaff6df7c54597dcaf1b9d282
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: da8896328a0fd6cc92f1adf0d8be8980d0ddd41f3172c7936f2c7f119b293ac1
    role: context
  - path: .claude/skills/manage-identifiers/SKILL.md
    sha256: a5c5aaa10943ee6d15423a5878ed2189e4e0b28a5c6e09fda80ba299ab779ebb
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: bb03efa3bbd3748ee1dccf57612a6ce8fcc861f20eb57c33eb16e3ac1dd728bd
    role: context
  - path: CLAUDE.md
    sha256: 4d328127022388e1affe9b71be24bc93944a971636d0d0ea902f6511e0b405c5
    role: context
  - path: DO_NOT_WORK.md
    sha256: 9ae0b05cc06f4ce8938801287a568d535e471d06dda5e258fcdbbed222abf712
    role: context
  - path: conf/evidence_snippet_baseline.tsv
    sha256: cbe5c82379e796446366b292f15194d80625b928119b482a67d857a379ab31a7
    role: context
  - path: conf/record_review.yaml
    sha256: 5adc6244761fb2baf8a059d81f23b0c9b32a33f9426ab84094234c3ec417269d
    role: context
  - path: data/raw/biolink-model.yaml
    sha256: 4955709e1cac1d26fd657f7a0c29d6c8390f42e41f9ebfab859c82b102f2bebb
    role: context
  - path: data/raw/metpo.owl
    sha256: 8b6f8fe0510a698579e532658c8ace05da2550093365df9ca83feb0741778415
    role: context
  - path: data/traits/environment/pressure_range.yaml
    sha256: 660d7961eb1c41bf856e45872894bc198e82563b035ed19592d20558b07bbe24
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
  - path: docs/PATHWAY_LINKS.md
    sha256: 800492750fb3c025dfdf7164813e7a00b3bd72dc8cc6f8e754e2aed5d7bbf414
    role: context
  - path: docs/record-review-profile.md
    sha256: cac714488cad03263ca3847737d5f70d174d40b5be677a09e0c1d9c814d9bc6a
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: justfile
    sha256: 008643042a721e84f647be6beda104ae02fe616361ff9b34fc608643a7526ee2
    role: context
  - path: mappings/node_grounding.tsv
    sha256: d7de9b3ab04960c4775a5bc295a945bd1a72d81467830459f4793e654f82b3d0
    role: context
  - path: mappings/predicate_grounding.tsv
    sha256: 8e28c19e93aca3dc164a3befbe2612b289241de457c59f499e65936c03b7ce52
    role: context
  - path: mappings/trait_exact_match_review.tsv
    sha256: 7728593d526d9a723716e5daad64beb7e1ab5c2e4221ae8d43dd9480cd02f62b
    role: context
  - path: mappings/uniprot_regrounding_candidates.tsv
    sha256: c36d8e038886d137d5a1ae609240e59ce74b6aeee17ae24f21b6c4a0d7407391
    role: context
  - path: proposals/metpo_traitmech_v4/metpo_proposal_properties_robot.tsv
    sha256: 55a96748c50b60ba0622170ef0eb09833f6d1e59431a4ab32b6fcb079103c0b7
    role: context
  - path: proposals/metpo_traitmech_v4/proposal.md
    sha256: c35d12fec87a3efdcfa320125446320315fca17bdb9228dd2b98ed00fe991bd8
    role: context
  - path: proposals/metpo_traitmech_v5/metpo_proposal_classes_robot.tsv
    sha256: d4b899de7077b33f4bdc6cb8cdebf28b5a705b7a65ba3620f3113b76d8666910
    role: context
  - path: proposals/metpo_traitmech_v5/proposal.md
    sha256: 5d54623dd00ac80a8d67a0eab7b70385f7f57b36daa205c28aa1f9d6f9be6167
    role: context
  - path: reports/metpo_2026_06_12_active_review.tsv
    sha256: 45e9c6471475635ba1f2602cd636a119d490f5dbd8dd6ac8af1aab89a321379f
    role: context
  - path: reports/metpo_2026_06_12_release_delta.tsv
    sha256: afe858d2aa0ade08322c7808d5917ff370e069ba02c2642d483342db8e9323ac
    role: context
  - path: reports/ontology_snapshot_manifest.tsv
    sha256: 4a157279a8c4e3fc2afb5382a45c31961991bbd1f330f26d0061b0cfd0b4d213
    role: context
  - path: research/traits/environment/pressure_range-deep-research-falcon.md
    sha256: 576cf6186ce796fee7d0b91187549b77f133c3de12d9fa13f449066e936fef9a
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/add_behavioral_habituation_trait.py
    sha256: d10694ecc93aa91cf26c8e082573e67b28d0d8cb111b0deae762684da8d4b43a
    role: context
  - path: scripts/add_ds_34_system_trait.py
    sha256: e76291f61764660ae4896a6c00d808776e86b9a75a9b4ce201c0b90ab84d1503
    role: context
  - path: scripts/add_ds_3_system_trait.py
    sha256: 4dc9c5a77d40b841c0b41233a885e09594cde1d9036e26a50f442c58ceacea87
    role: context
  - path: scripts/add_fungal_nematophagy_trait.py
    sha256: 25d795459263fc08b7e8dcc2169056c7af0c5d86dc530638f9d7b69676608711
    role: context
  - path: scripts/add_trimethylamine_n_oxide_respiration_trait.py
    sha256: 92ef1bc42f26b9df73d94939a7823a655a2c0dd72cbb25087d31e93a6c5921b7
    role: context
  - path: scripts/audit_causal_graphs.py
    sha256: e0c26506c9de712700317284f142097e7bf69334806b8010db5d6517e905e834
    role: context
  - path: scripts/audit_graph_protein_taxa.py
    sha256: d3375861829c612483b3545dd0f5e2b79872a4576b626edc08714a09fbd9a24d
    role: context
  - path: scripts/audit_predicate_domains.py
    sha256: 35be8589638b8b21379f2dfd7fa7fb7d4eb422ccf71063e1e21a6bc19b767bcf
    role: context
  - path: scripts/audit_unapplied_groundings.py
    sha256: 5afa6a602f0d7d5107adebf8b067d61bde9ea9adb267f9dfaed8a0b7cc0cc76b
    role: context
  - path: scripts/audit_uniprot_grounding.py
    sha256: 91eb2165c69b3a4fcb53154dc8c835ac1070577f88065a43dfc881284d3d1052
    role: context
  - path: scripts/backfill_canonical_examples_444.py
    sha256: 18ca0766789c239d693ef665e8b1d43c1209a0f414a326f1c5d890f88de7b20c
    role: context
  - path: scripts/connect_nacl_optimum_graph_183.py
    sha256: f1608bd82c1323c7d2306268860502ae3483d40f093e055b9b70cd463a1ecf04
    role: context
  - path: scripts/finalize_metpo_2026_06_12_review.py
    sha256: b850b386183b2d86647dada43f7f157059017dbb881f7e1fb2e220ae697d3bea
    role: context
  - path: scripts/ground_causal_nodes.py
    sha256: 204ce4162544154b1752b65da2136538847ea25ced26a52f5708eadff08f5d42
    role: context
  - path: scripts/ground_causal_predicates.py
    sha256: 5a788eeaabf3a56b0d82c469a3e3fe28f1d51707d9382313b9a94289be7d1381
    role: context
  - path: scripts/migrate_disposition_typing.py
    sha256: ebafdd145fc0729d32f3b8a45f570d97a8e001838afadd698e2b246cb8950714
    role: context
  - path: scripts/migrate_enables_range_edges.py
    sha256: 3d0d1bddcaa76baef5833973e2e979e4fee1f834c67d1abcc69a8d866ecb8f32
    role: context
  - path: scripts/migrate_enables_trait_edges.py
    sha256: a5e7965ee4f6b6ba5bae3a06bced2a83cbf755f3b9b150ce6acc0cd808cb1d88
    role: context
  - path: scripts/migrate_metpo_2026_06_12.py
    sha256: 0f3945e7b8e6ddccdc9eaeed32737a2a1cf0832748af2b72a6a0195ba661188f
    role: context
  - path: scripts/migrate_microbe_domain_edges.py
    sha256: 5187ccfb2897d415b243792a27afd6002c0eea4b167068639ff5be73ed583bb6
    role: context
  - path: scripts/migrate_name_match_groundings.py
    sha256: 9b3ea1153839b9b260638cef95eba2d1ccc6d7b3825e7352c33cceb21bfe4dd4
    role: context
  - path: scripts/migrate_node_type_consistency.py
    sha256: a3e7bc170e60f406a73e06c893d74f5253671028d3d40cc15ecf882b6684a69e
    role: context
  - path: scripts/migrate_pathway_vs_process.py
    sha256: f236de7183048732e9001b7fac4367affff58d8b7a7d5c63286e6b058a4b38c2
    role: context
  - path: scripts/migrate_process_quality_consistency.py
    sha256: 1a83ad3dba79ed0c958b875a6fcc4b9e562259af26da2f248d32d5cf7784f80a
    role: context
  - path: scripts/migrate_protein_vs_activity.py
    sha256: 0b183248ff22d3d8aa66b35aece40c53b516684ca499cf73b7714206031dad49
    role: context
  - path: scripts/migrate_remaining_microbe_domain_edges.py
    sha256: 110542d49e25007122c7c254966ad87dc3f7f054358766e933aff89e8ef0a994
    role: context
  - path: scripts/migrate_uniprot_instance_groundings.py
    sha256: 07d2a5405cff5857239757e0a3791f411b1d25709a5760c1e49553eed066993d
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/review_nacl_delta_graph_183.py
    sha256: 91b85da640baff48e0d317c206aaa24c1216b3725d9c9814c6fb9d4d975e192c
    role: context
  - path: scripts/review_nacl_delta_mid2_graph_183.py
    sha256: 7d628bb0265a6f689dbeb47509be8c6528c0c64e6b3d59d84e5a8a0b9cb5e1a5
    role: context
  - path: scripts/review_nacl_optimum_graph_183.py
    sha256: 6d0de1ccb1604fb87294432692cc051e3a8a1d52e082eaff6aa1f8d3cb621ffd
    role: context
  - path: scripts/review_nacl_range_low_graph_183.py
    sha256: d7e6669f6d2aa295487a34cba7fe14666a979404614bdbdd3be529194649accf
    role: context
  - path: scripts/review_obligately_piezophilic_graph_183.py
    sha256: d8fcbbb725162212cfce96bed9800e2cf08374170b7d929a1928248178111efb
    role: context
  - path: scripts/seed_from_metpo.py
    sha256: 0fb9c9f7ea6a8f137eecd5c319775b511c398dba6158c81b1fbfb94210f7d851
    role: context
  - path: scripts/verify_metpo_proposal.py
    sha256: f58355151f7d6a807bb50dc8b732184994b0d6145d3c57f54e29fd0bb76268b6
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
targets:
- target_id: traitmech:000005
  path: data/traits/environment/pressure_range.yaml
  label: pressure range
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/pressure_range.yaml
    role: Maintained target; read-only review.
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Maintained predicate context; recurrence assessed only after capture.
  - repository: CultureBotAI/TraitMech
    path: mappings/node_grounding.tsv
    role: Maintained grounding context; recurrence assessed only after capture.
  record_class: TraitRecord
scope:
  description: One entire maintained TraitRecord. Contextual ontology, source, parent,
    writer and history inputs are not additional review targets.
  selection: Fourth record of the actual locally initialized batch 012 queue. Whole
    218-line target and all 68 captured inputs verified before assessment; interval,
    optimum and derived breadth remain distinct. Local initialization at 21:02:18.445284
    UTC does not assert publication of batch 011.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - traitmech:000005
checks:
- check_id: audit-graphs
  name: Full-corpus graph audit
  status: passed
  required: true
  target_ids:
  - traitmech:000005
  command: just audit-graphs --out /private/tmp/traitmech-record-sweep.FU79Gr/causal_graph_audit.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  evidence_ids:
  - check-audit-graphs
  scope_note: 'Original common diagnostics ran at f25; history validation ran in batch
    003 at 8eee. Actual B11 final QC ran 20:52:41.208560–20:54:10.001030 UTC; B12
    byte qualification completed 20:56:21.138176 and independent postcheck 20:58:20.194890.
    Original failures/retries/skips and seven-file delta remain explicit; no fresh
    B12 QC or B11 publication is claimed. Qualification: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/common-reuse-b11-qc-supplement-qualified.json'
- check_id: audit-snippets
  name: Full-corpus snippet audit
  status: passed
  required: true
  target_ids:
  - traitmech:000005
  command: just audit-snippets --report /private/tmp/traitmech-record-sweep.FU79Gr/evidence_snippet_audit.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  evidence_ids:
  - check-audit-snippets
  scope_note: 'Original common diagnostics ran at f25; history validation ran in batch
    003 at 8eee. Actual B11 final QC ran 20:52:41.208560–20:54:10.001030 UTC; B12
    byte qualification completed 20:56:21.138176 and independent postcheck 20:58:20.194890.
    Original failures/retries/skips and seven-file delta remain explicit; no fresh
    B12 QC or B11 publication is claimed. Qualification: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/common-reuse-b11-qc-supplement-qualified.json'
- check_id: check-pathway-links
  name: Full-corpus pathway links
  status: passed
  required: true
  target_ids:
  - traitmech:000005
  command: just check-pathway-links
  exit_code: 0
  expected_exit_code: 0
  summary: 19 links checked against the pinned PathwayMech snapshot.
  evidence_ids:
  - check-check-pathway-links
  scope_note: 'Original common diagnostics ran at f25; history validation ran in batch
    003 at 8eee. Actual B11 final QC ran 20:52:41.208560–20:54:10.001030 UTC; B12
    byte qualification completed 20:56:21.138176 and independent postcheck 20:58:20.194890.
    Original failures/retries/skips and seven-file delta remain explicit; no fresh
    B12 QC or B11 publication is claimed. Qualification: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/common-reuse-b11-qc-supplement-qualified.json'
- check_id: validate-history
  name: Full-corpus history integrity
  status: passed
  required: true
  target_ids:
  - traitmech:000005
  command: just validate-history
  exit_code: 0
  expected_exit_code: 0
  summary: 1277 history records checked, zero invalid links at the 8eee source base;
    integrity does not establish science or human acceptance.
  evidence_ids:
  - check-validate-history
  scope_note: 'Original common diagnostics ran at f25; history validation ran in batch
    003 at 8eee. Actual B11 final QC ran 20:52:41.208560–20:54:10.001030 UTC; B12
    byte qualification completed 20:56:21.138176 and independent postcheck 20:58:20.194890.
    Original failures/retries/skips and seven-file delta remain explicit; no fresh
    B12 QC or B11 publication is claimed. Qualification: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/common-reuse-b11-qc-supplement-qualified.json'
- check_id: validate-products
  name: Initial full-product validation
  status: failed
  required: false
  target_ids:
  - traitmech:000005
  command: just validate-products
  exit_code: 2
  expected_exit_code: 0
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  evidence_ids:
  - check-validate-products
  scope_note: 'Original common diagnostics ran at f25; history validation ran in batch
    003 at 8eee. Actual B11 final QC ran 20:52:41.208560–20:54:10.001030 UTC; B12
    byte qualification completed 20:56:21.138176 and independent postcheck 20:58:20.194890.
    Original failures/retries/skips and seven-file delta remain explicit; no fresh
    B12 QC or B11 publication is claimed. Qualification: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/common-reuse-b11-qc-supplement-qualified.json'
- check_id: validate-products-retry-local
  name: Product validation with isolated local cache
  status: failed
  required: false
  target_ids:
  - traitmech:000005
  command: just validate-products
  exit_code: 2
  expected_exit_code: 0
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  evidence_ids:
  - check-validate-products-retry-local
  scope_note: 'Original common diagnostics ran at f25; history validation ran in batch
    003 at 8eee. Actual B11 final QC ran 20:52:41.208560–20:54:10.001030 UTC; B12
    byte qualification completed 20:56:21.138176 and independent postcheck 20:58:20.194890.
    Original failures/retries/skips and seven-file delta remain explicit; no fresh
    B12 QC or B11 publication is claimed. Qualification: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/common-reuse-b11-qc-supplement-qualified.json'
- check_id: validate-products-retry-network
  name: Product validation after isolated-cache download
  status: passed
  required: true
  target_ids:
  - traitmech:000005
  command: just validate-products
  exit_code: 0
  expected_exit_code: 0
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  evidence_ids:
  - check-validate-products-retry-network
  scope_note: 'Original common diagnostics ran at f25; history validation ran in batch
    003 at 8eee. Actual B11 final QC ran 20:52:41.208560–20:54:10.001030 UTC; B12
    byte qualification completed 20:56:21.138176 and independent postcheck 20:58:20.194890.
    Original failures/retries/skips and seven-file delta remain explicit; no fresh
    B12 QC or B11 publication is claimed. Qualification: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/common-reuse-b11-qc-supplement-qualified.json'
- check_id: pressure-range-native
  name: Focused native validation
  status: passed
  required: true
  target_ids:
  - traitmech:000005
  command: just validate data/traits/environment/pressure_range.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Successful schema validation; source and semantics separately assessed.
  evidence_ids:
  - check-pressure-range-native
- check_id: pressure-range-strict
  name: Focused strict validation
  status: passed
  required: true
  target_ids:
  - traitmech:000005
  command: just validate-strict data/traits/environment/pressure_range.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Successful strict validation; no biological efficacy certification.
  evidence_ids:
  - check-pressure-range-strict
- check_id: pressure-range-snippets-network
  name: Focused network snippet check
  status: passed
  required: true
  target_ids:
  - traitmech:000005
  command: just verify-snippets --record data/traits/environment/pressure_range.yaml
    --out /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-snippets-network.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: Direct authorized network invocation passed with two NOT_IN_ABSTRACT results.
    No target-specific initial failed attempt. Actual primary review establishes one
    literal and one supported unit transcription.
  evidence_ids:
  - check-pressure-range-snippets-network
- check_id: batch011-qc
  name: Reused maintained batch-eleven QC
  status: passed
  required: true
  target_ids:
  - traitmech:000005
  command: just qc
  exit_code: 0
  expected_exit_code: 0
  summary: Actual B11 final QC at its original time, qualified against B12 bytes;
    independent of pending publication.
  evidence_ids:
  - check-batch011-qc
- check_id: uniprot-applicability
  name: Protein-instance metadata applicability
  status: not_applicable
  required: false
  target_ids:
  - traitmech:000005
  summary: Zero protein classes and instances in the contextual interval graph; no
    forced accession or detailed pressure-response query.
  evidence_ids:
  - record
  - policy
  - node-edges
evidence:
- evidence_id: check-audit-graphs
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; metadata audit-graphs.json
  accessed_at: '2026-10-19T07:33:29Z'
  support: context_only
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  snapshot_sha256: ecce27e6a8f8b8b1fc54a9a0564a27626ee33774da508665859c6d1429337f4d
- evidence_id: check-audit-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; metadata audit-snippets.json
  accessed_at: '2026-10-19T07:33:33Z'
  support: context_only
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  snapshot_sha256: beafaa5c82645f5cf216142b6e0369d556202bcc72fdabbf35825fce955fd59f
- evidence_id: check-check-pathway-links
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; metadata check-pathway-links.json
  accessed_at: '2026-10-19T07:33:28Z'
  support: context_only
  summary: 19 links checked against the pinned PathwayMech snapshot.
  snapshot_sha256: e77729b8afd6ae02cd834e516c48dd5c72d10498802e7a1b0004eebb4831f6a0
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-003.4opxlhgf/validate-history.log
  locator: Executed 2026-10-21T07:03:25Z through 2026-10-21T07:03:30Z; metadata validate-history.json
  accessed_at: '2026-10-21T07:03:30Z'
  support: context_only
  summary: 1277 history records checked, zero invalid links at the 8eee source base;
    integrity does not establish science or human acceptance.
  snapshot_sha256: 02f94872992b2fbc3cc455c552d56a338dd449a315e02b1bf0226b68a8d2cfe3
- evidence_id: check-validate-products
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; metadata validate-products.json
  accessed_at: '2026-10-19T07:34:01Z'
  support: context_only
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  snapshot_sha256: 697efcbe603c9a5e27f9726e688d1b9d9f621fa548f585d9005b5157d81dadae
- evidence_id: check-validate-products-retry-local
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log
  locator: Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; metadata validate-products-retry-local.json
  accessed_at: '2026-10-19T07:35:24Z'
  support: context_only
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  snapshot_sha256: b636ab6978cf8b8d4cc2cc4033f1cdca399cca46dc615a26073cfe680d44ebb5
- evidence_id: check-validate-products-retry-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log
  locator: Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; metadata validate-products-retry-network.json
  accessed_at: '2026-10-19T07:36:03Z'
  support: context_only
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  snapshot_sha256: 67e91252adce1d441ad6b37d6904f0cbcea703575aec8011e65e94822fa810ea
- evidence_id: check-pressure-range-native
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-native.log
  locator: Executed 2026-10-21T21:42:33.387389+00:00 through 2026-10-21T21:42:34.912640+00:00;
    metadata pressure-range-native.json
  accessed_at: '2026-10-21T21:42:34.912640Z'
  support: context_only
  summary: Successful schema validation; source and semantics separately assessed.
  snapshot_sha256: 503cc5264bdc4fe63376af0e6752957147122d20eaad5c036c8e8815a0a5cec6
- evidence_id: check-pressure-range-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-strict.log
  locator: Executed 2026-10-21T21:42:33.387367+00:00 through 2026-10-21T21:42:37.203254+00:00;
    metadata pressure-range-strict.json
  accessed_at: '2026-10-21T21:42:37.203254Z'
  support: context_only
  summary: Successful strict validation; no biological efficacy certification.
  snapshot_sha256: 441a89687330ff546b537db7d1f4206fd845ebd63f35dee9b59fae1d1dfee1b8
- evidence_id: check-pressure-range-snippets-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-snippets-network.log
  locator: Executed 2026-10-21T21:42:42.769089+00:00 through 2026-10-21T21:42:46.388498+00:00;
    metadata pressure-range-snippets-network.json
  accessed_at: '2026-10-21T21:42:46.388498Z'
  support: context_only
  summary: Direct authorized network invocation passed with two NOT_IN_ABSTRACT results.
    No target-specific initial failed attempt. Actual primary review establishes one
    literal and one supported unit transcription.
  snapshot_sha256: 27191d89642cac515a54d811e547546aecb0e1bea2f344a1808ea25c861a43d8
- evidence_id: check-batch011-qc
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/batch011-qc.log
  locator: Executed 2026-10-21T20:52:41.208560+00:00 through 2026-10-21T20:54:10.001030+00:00;
    metadata batch011-qc.json
  accessed_at: '2026-10-21T20:54:10.001030Z'
  support: context_only
  summary: Actual B11 final QC at its original time, qualified against B12 bytes;
    independent of pending publication.
  snapshot_sha256: e9c9063f603119bbd8b98e5ba52a6eb85dbad77b92405eefc249af01216f248f
- evidence_id: record
  kind: record_content
  reference: data/traits/environment/pressure_range.yaml
  locator: Entire current 218-line record
  accessed_at: '2026-10-21T21:42:05.402589Z'
  support: supports
  summary: Nine nodes, seven edges, two snippets, one canonical and ten AI events
    covered.
  snapshot_sha256: 660d7961eb1c41bf856e45872894bc198e82563b035ed19592d20558b07bbe24
- evidence_id: policy
  kind: authority
  reference: docs/GROUNDING_POLICY.md
  locator: Captured maintained authority
  accessed_at: '2026-10-21T21:45:16.018657Z'
  support: supports
  summary: Referent-based identity, broader-family qualifications and imported formal
    roles.
  snapshot_sha256: 891678c983c2283a47c81c47950b35753981e9339d105f3bbdda92a1f5ab7f42
- evidence_id: playbook
  kind: authority
  reference: docs/CURATION_PLAYBOOK.md
  locator: Captured maintained authority
  accessed_at: '2026-10-21T21:45:16.018657Z'
  support: supports
  summary: Source scope, literal copied snippets and attributable acceptance.
  snapshot_sha256: 735e9b810471da9f7d8364e35ffe1e741edb3421480dac01727db6ea5aa65da9
- evidence_id: schema
  kind: authority
  reference: src/traitmech/schema/traitmech.yaml
  locator: Captured maintained authority
  accessed_at: '2026-10-21T21:45:16.018657Z'
  support: supports
  summary: Current node facets and review contract.
  snapshot_sha256: 46c47fc627b80ccbba1e8ab3fb6f2aee93bc2aef7aaf72fe9aadc3257f2c02dd
- evidence_id: checklist
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Captured maintained authority
  accessed_at: '2026-10-21T21:45:16.018657Z'
  support: supports
  summary: Whole-record identity, evidence, graph, provenance and readiness checks.
  snapshot_sha256: da8896328a0fd6cc92f1adf0d8be8980d0ddd41f3172c7936f2c7f119b293ac1
- evidence_id: node-mapping-primary
  kind: authority
  reference: mappings/node_grounding.tsv
  locator: Captured maintained authority
  accessed_at: '2026-10-21T21:45:16.018657Z'
  support: supports
  summary: Historical row 192 exactMatch is narrower than the primary GO family; current
    type and nonempty guards limit replay.
  snapshot_sha256: d7de9b3ab04960c4775a5bc295a945bd1a72d81467830459f4793e654f82b3d0
- evidence_id: reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/common-reuse-b11-qc-supplement-qualified.json
  locator: Actual B11-to-B12 qualification
  accessed_at: '2026-10-21T20:56:21.138176Z'
  support: supports
  summary: Original outcomes and all current byte comparisons bound.
  snapshot_sha256: 237e3fe64b4790f2caa121b17e2a9d6857dd4cfbf74d824d29d986d6c8ff1602
- evidence_id: reuse-postcheck
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/common-reuse-output-verification-agent/post-execution-verification.json
  locator: Independent actual-output verification
  accessed_at: '2026-10-21T20:58:20.194890Z'
  support: supports
  summary: Actual output/hash postcheck; no new QC.
  snapshot_sha256: 59659bb5400fdae759f8a705c18869cfc9192db0234b2a4d763b882f5e67e1c4
- evidence_id: local-init
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/batch012-local-initialization-receipt.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:02:18.445284Z'
  support: supports
  summary: Local-only initialization on verified prior local commit; publication status
    remains separately documented.
  snapshot_sha256: 542fa42507cccb7806576817933aa17f8f43f309702934d265a0c2debccb7cef
- evidence_id: capture
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-grounding-agent/capture-verification.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:42:48.259244Z'
  support: supports
  summary: All 68 inputs verified before grounding assessment.
  snapshot_sha256: 182814f72e0f7413fa250e48bc3afc558190659c8536f5ba5333286d45ffbd95
- evidence_id: identity
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-grounding-agent/identity-assessment.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:45:16.017051Z'
  support: supports
  summary: Retained range fallback, active parent and meaningful broader GO family.
  snapshot_sha256: 32efdc4e33c6c8c0b39fb237f9b3b0526618248d05d410eacdc92bb99f8084e4
- evidence_id: node-edges
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-grounding-agent/node-edge-ledger.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:45:16.017441Z'
  support: supports
  summary: All nine nodes/seven edges and two components; imported roles separate
    from biology.
  snapshot_sha256: 161dddf24bf160018b7df429dd5449fe0439a730b914def5ac0ee99102137644
- evidence_id: owners
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-grounding-agent/owner-provenance-assessment.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:45:16.017821Z'
  support: supports
  summary: Current record, conditional RO mapping and historically narrower GO row
    with replay limits.
  snapshot_sha256: 43efc811f0adddf2cb6e451a73c635cf4db1ad4bcdabe76d4b9a8f40a2f07bfa
- evidence_id: expression
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-grounding-agent/expression-and-readiness-assessment.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:45:16.018154Z'
  support: supports
  summary: Canonical catalog applicability and zero-protein contextual graph.
  snapshot_sha256: 8f63f451d5372310f78721a3102e634d1260ccd39ebb9b57e704bf3a57bf7727
- evidence_id: catalog-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-grounding-agent/catalog-reuse-receipt.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:43:08.102140Z'
  support: supports
  summary: Original catalog/runner receipts separate from current copies.
  snapshot_sha256: e2f9d29889ce96e7160a90e91ea80f9f3418c42a56dfa40517ce737267e16e9f
- evidence_id: local-authority
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-grounding-agent/local-authority-excerpts.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:45:16.013117Z'
  support: supports
  summary: Exact v5/v4 proposals, maintained mappings, schema and Biolink.
  snapshot_sha256: f337f50d76da725c191c2f8e99f701ba2d276d2d90cbd6c87f2af700410345a4
- evidence_id: ground-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-grounding-agent/reading-scope-receipt.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:45:16.019157Z'
  support: supports
  summary: Actual selected primary/owner readings; zero matching repository histories
    and ten current AI events.
  snapshot_sha256: b75c5c1cbbbcf71c4ab3eb3104473aa5ba754f1f80205ebfa0491940ec021685
- evidence_id: ground-manifest
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-grounding-agent/evidence-manifest.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:45:27.677995Z'
  support: supports
  summary: Frozen 30 grounding artifacts verified.
  snapshot_sha256: dce1737d4b8ecdd760beabdc432c3a724b1994ef38ba308c48504775fcb3c735
- evidence_id: go-dissent
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-grounding-agent/go-grounding-severity-qualification.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:45:16.018358Z'
  support: supports
  summary: Ground auditor preferred a limitation; root/challenger count only historical
    exactMatch precision as a minor. Current broader CURIE remains meaningful.
  snapshot_sha256: 659782a8634a8a4b0f48462bf95a5968365e11c0a0763dfbea1fe18779aa52a2
- evidence_id: taxon-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-grounding-agent/taxonomy-reuse-receipt.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:43:08.098402Z'
  support: supports
  summary: Original Colwellia request and retained initial DNS failure separate from
    current copies.
  snapshot_sha256: 23d71c7e63cb819c1042ba53b0918743e53cb557307d644492734a75eccf49db
- evidence_id: metpo-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/repo/data/raw/metpo.owl
  locator: Actual selected METPO XML
  accessed_at: '2026-10-21T21:42:49.515584Z'
  support: supports
  summary: Broader pressure tolerance is not an exact numerical-interval replacement;
    v5 separately sourced.
  snapshot_sha256: 8b6f8fe0510a698579e532658c8ace05da2550093365df9ca83feb0741778415
- evidence_id: ro-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/ro.db
  locator: Actual RO2213 and RO2211 rows
  accessed_at: '2026-10-21T21:42:48.264451Z'
  support: supports
  summary: Positive regulation inherits process subject and object requirements.
  snapshot_sha256: 849e616c29fecd0d4a6c6dee0dc0f6f117ace7167dbfa1e0f043dc84868f83cb
- evidence_id: pato-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/pato.db
  locator: Actual PATO0001025 rows
  accessed_at: '2026-10-21T21:42:48.270050Z'
  support: supports
  summary: Pressure physical quality supports the ambient condition identity.
  snapshot_sha256: 179ab512b5c3a8827c74e2a496da575e2908a84740429deef265d58c9ce61d3b
- evidence_id: go-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/go.db
  locator: Actual GO0006636 rows
  accessed_at: '2026-10-21T21:42:48.352303Z'
  support: supports
  summary: Active unsaturated-fatty-acid biosynthesis includes one or more double
    bonds; PUFA biosynthesis is explicitly a narrow synonym.
  snapshot_sha256: 018a7ef0a5bd1c0767abc3d71b413264a25be7579533daf5349f739cd9a122cd
- evidence_id: proposal-v5-primary
  kind: authority
  reference: proposals/metpo_traitmech_v5/metpo_proposal_classes_robot.tsv
  locator: Captured TSV row 7
  accessed_at: '2026-10-21T21:45:16.013117Z'
  support: supports
  summary: Proposed 1007604 preserves the exact min/max growth interval, not an installed
    active replacement.
  snapshot_sha256: d4b899de7077b33f4bdc6cb8cdebf28b5a705b7a65ba3620f3113b76d8666910
- evidence_id: proposal-v4-primary
  kind: authority
  reference: proposals/metpo_traitmech_v4/metpo_proposal_properties_robot.tsv
  locator: Captured TSV row 3
  accessed_at: '2026-10-21T21:45:16.013117Z'
  support: supports
  summary: Defines permits a measurement axis or feature to parameterize a numerical
    trait.
  snapshot_sha256: 55a96748c50b60ba0622170ef0eb09833f6d1e59431a4ab32b6fcb079103c0b7
- evidence_id: taxon-colwellia
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-grounding-agent/taxon1513592.xml
  locator: Whole official taxonomy response; original successful request time
  accessed_at: '2026-10-21T16:11:20.071001Z'
  support: supports
  summary: Official species and MTCD1 aliases positive; interval separately sourced.
  snapshot_sha256: 44883620d8bdc159d01e53d74afc493e730bac233c92303887b704c10061050e
- evidence_id: meta-membrane
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-agent/membrane-metadata.json
  locator: Actual retained indexed metadata/abstract; original request time
  accessed_at: '2026-10-21T20:42:51.668312Z'
  support: supports
  summary: Actual review abstract describes non-universal lipid responses and pressure/temperature
    context; body separately bound.
  snapshot_sha256: 60b0dd82b02eddbe01f9944f485da11c5ea9e55ec36f65b501a3a78ba9b1e9b3
- evidence_id: meta-colwellia
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-agent/colwellia-metadata.json
  locator: Actual retained indexed metadata/abstract; original request time
  accessed_at: '2026-10-21T20:42:51.694246Z'
  support: supports
  summary: Actual primary abstract reports MTCD1 growth range 80–140 MPa at 6 °C,
    distinct from optimum 120 MPa.
  snapshot_sha256: e74a6f54136e6dcd2ab87b38d86de68e793d0dc28218b87b9f2bbd3ccd4103d2
- evidence_id: meta-piezolytes
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-agent/piezolytes-metadata.json
  locator: Actual retained indexed metadata/abstract; original request time
  accessed_at: '2026-10-21T20:42:51.672336Z'
  support: supports
  summary: Actual review identity and abstract; selected membrane, hydration and solute
    observations separately bound to body.
  snapshot_sha256: f841a93f68b50bd7d184e38aeaf8ed5ebc840e76fd6864c64cedfb77bff21881
- evidence_id: body-membrane
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-agent/membrane.xml
  locator: Actual retained primary body; selected passages only
  accessed_at: '2026-10-21T16:07:35.045859Z'
  support: supports
  summary: Actual body paragraphs 1/9/10/12/13 provide the literal classification
    phrase and generic lipid context with taxon/temperature exceptions.
  snapshot_sha256: d8320b3073b404cd79da19795d94f02477ce8a34accb22809294e05d1e72c032
- evidence_id: body-piezolytes
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-agent/piezolytes.xml
  locator: Actual retained primary body; selected passages only
  accessed_at: '2026-10-21T20:43:59.908978Z'
  support: supports
  summary: Actual body paragraphs 17/18/20/26/27 provide membrane and hydration wording
    with source-specific solute/condition contrasts.
  snapshot_sha256: b32571a4a2b468a959e4eb6d6b947576faa188eb3100daf47cc7840b23d2724e
- evidence_id: meta-chemrev
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-agent/chemrev-metadata.json
  locator: Actual retained indexed metadata/abstract; original request time
  accessed_at: '2026-10-21T21:17:31.023274Z'
  support: supports
  summary: Actual review identity and abstract concerning physical crowding/cosolute
    effects; author-deposited body separately bound.
  snapshot_sha256: bd1f7380dbde15a025a6d0a85b194f7d430791fdbe0458577fc858dc06de6111
- evidence_id: body-chemrev
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-agent/chemrev.pdf
  locator: Actual retained primary body; selected passages only
  accessed_at: '2026-10-21T21:17:59.961010Z'
  support: supports
  summary: Actual HAL author-deposited manuscript, cover identity/DOI verified; selected
    exclusion/hydration discussion and Figure 29. Derived newline extraction is separately
    bound.
  snapshot_sha256: cbdde27b2d4a5f88f8cec3378c6f86f6438088e8e1d5a72d6e0bbdd8b3099590
- evidence_id: chemrev-text
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-agent/chemrev.txt
  locator: Derived PDF text; newline-only 2164–2167 and Figure 29 caption 2189–2192
  accessed_at: '2026-10-21T21:44:13.433026Z'
  support: context_only
  summary: Text extraction is not a fresh primary acquisition or publisher HTML; actual
    author PDF is separately bound.
  snapshot_sha256: e3e7bdc27d15d7540781b3e419676580f53aa7bce21cdd091d47dee86449328e
- evidence_id: sources
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-agent/source-assessment.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:44:13.444391Z'
  support: supports
  summary: Final four-work audit; unit-format and hydration-explanation minors with
    exact interval expansion unknown.
  snapshot_sha256: 4869b51ae47e1c7f94509eff03aca83ca25e2468ed4ce12cc800262db6baa9f8
- evidence_id: source-ledger
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-agent/source-ledger.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:44:13.433026Z'
  support: supports
  summary: All four identities and distinct abstract/body reading scopes.
  snapshot_sha256: 05f951c9462405bdccef38d1460dc4cf7598177f0ffbc090c4ab56449076e7b5
- evidence_id: placements
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-agent/placement-ledger.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:44:13.433026Z'
  support: supports
  summary: All eleven external placements and seven grounding fields accounted for.
  snapshot_sha256: 1c37e3a3d099f697d1dc26b40fc0ac4bf124fa23a4976b41425a7fa9e62236ff
- evidence_id: snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-agent/snippet-ledger.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:44:13.433026Z'
  support: supports
  summary: One supported unit transcription and one literal phrase; numbers preserved.
  snapshot_sha256: d8fa5dc5a4f9c7c0404f994bd144c96ecf02104a2c2c97a9cbdda1097c8ed1e6
- evidence_id: node-sources
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-agent/node-source-ledger.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:44:13.433026Z'
  support: supports
  summary: All nine source node contexts.
  snapshot_sha256: 2b4bfe2d5b839a5ca5538ee45277e30e904e502a931ad291bcaacf4b398b8b3b
- evidence_id: edge-sources
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-agent/edge-source-ledger.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:44:13.433026Z'
  support: supports
  summary: All seven source edge contexts; nearest-source expansion attribution remains
    unknown.
  snapshot_sha256: 62881b5645641d1637fd37869c739687a70bc65503f0cc86fccace25a1cd145a
- evidence_id: source-status
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-agent/publication-status-ledger.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:44:13.433026Z'
  support: supports
  summary: Actual returned publication-status fields; bounded history checks.
  snapshot_sha256: 2fc61b3b741f2c7546762e09489dc79c4803a4c2ca12732b1e1dab57f198a68a
- evidence_id: source-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-agent/selected-primary-reading.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:44:13.433026Z'
  support: supports
  summary: Actual selected readings; incidental excluded content not adopted.
  snapshot_sha256: 336a072f37b0c73c6723027dcc374818096a6d391db4e44a9e07e0901a1ee04d
- evidence_id: source-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-agent/access-limitations.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:44:13.433026Z'
  support: supports
  summary: Colwellia body not acquired/inspected; three retained actual bodies and
    original request limits.
  snapshot_sha256: 5cfd52f8010e04034690562ad060e1677bff1b70001ef7ee4c5e1533329ee647
- evidence_id: source-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-agent/source-reuse-receipt.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:42:39.277430Z'
  support: supports
  summary: Original acquisitions separate from current copies at 21:42:39 UTC.
  snapshot_sha256: 99ae5c13ce0b8844ee5feed5b5d08ce653ffedb594375e6d80fe56627d8bab78
- evidence_id: canonical-scope
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-agent/canonical-assessment.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:44:13.433026Z'
  support: supports
  summary: Positive strain/temperature-specific range 80–140 MPa at 6 °C.
  snapshot_sha256: c60892d38a63b02b8fd603bd914a748d464eb2e1c7af582b3bdb0b7f9096a830
- evidence_id: hydration-scope
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-agent/hydration-wording-assessment.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:44:13.433026Z'
  support: supports
  summary: Faithful piezolyte attribution conflicts with assigned exclusion/hydration
    explanation and current graph wording.
  snapshot_sha256: 4fa77e36d210e95db04227d8abab785fea153ef0312879f405c8ce6dfcbeff3b
- evidence_id: native-checks
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-agent/native-check-context.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:44:13.444115Z'
  support: supports
  summary: Three focused commands pass, including direct network snippets; no current
    initial failed attempt.
  snapshot_sha256: a67a9909ff66ff5630d72e40227a544d767666269eda4e71d8cbb020f5d41344
- evidence_id: source-capture
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-agent/final-capture-verification.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:44:13.444528Z'
  support: supports
  summary: All 68 captured inputs unchanged.
  snapshot_sha256: 9ad77aeb143303baf366675d20011ab18c0aab3c65def1d898031daec24e53f3
- evidence_id: source-manifest
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-agent/evidence-manifest.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:44:13.447213Z'
  support: supports
  summary: Twenty-nine frozen source artifacts verified.
  snapshot_sha256: d4bd0ca9c68c05888d442c7728ba50501f7f55e8cd4eb5d0fca990d1c0b3f96b
- evidence_id: root-reading-75
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-root/frozen-audits-reading.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:46:00.709767Z'
  support: supports
  summary: Only actual bounded root reading/observation scope; receipt hash is not
    an article-body hash.
  snapshot_sha256: d4008efe625d175d413106121fb223e85d71bb19886515711b6b5884772489b7
- evidence_id: root-reading-76
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-root/identity-primary-reading.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:43:30.880804Z'
  support: supports
  summary: Only actual bounded root reading/observation scope; receipt hash is not
    an article-body hash.
  snapshot_sha256: 00c1423297e5f367c8cf564f1aabab93d7e0e27b2019ac01e3f3bf6b2eeb6be9
- evidence_id: root-reading-77
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-root/literature-primary-reading.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:43:49.653176Z'
  support: supports
  summary: Only actual bounded root reading/observation scope; receipt hash is not
    an article-body hash.
  snapshot_sha256: a20bc3a0bf4bcff9ea51bf1f2482632ae4df0782855d35604a06dece8c7cf609
- evidence_id: root-reading-78
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-root/ontology-primary-reading.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:42:55.381597Z'
  support: supports
  summary: Only actual bounded root reading/observation scope; receipt hash is not
    an article-body hash.
  snapshot_sha256: f3a0c10be5a7bb4b28458a4f9d8f4ef94350a04a57e2bf49154d716a58606b0e
- evidence_id: root-reading-79
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-root/owner-and-context-reading.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:44:49.835566Z'
  support: supports
  summary: Only actual bounded root reading/observation scope; receipt hash is not
    an article-body hash.
  snapshot_sha256: 753067d679be26e714b51a5dada05a86b4a69115ad489673a46eed2baa470030
- evidence_id: root-reading-80
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-root/root-reading-attestation.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:43:49.655981Z'
  support: supports
  summary: Only actual bounded root reading/observation scope; receipt hash is not
    an article-body hash.
  snapshot_sha256: 710f5fda3d7a0ad7c9dcb76e418ad07796e2b14bdd4fdeb6110bc144293be42e
- evidence_id: root-reading-81
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-source-root/taxonomy-catalog-reading.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:45:34.389157Z'
  support: supports
  summary: Only actual bounded root reading/observation scope; receipt hash is not
    an article-body hash.
  snapshot_sha256: a2253e98ec2e05a0420f1c4562bff98a148d4f5f945f491e9ce39316bf363edb
- evidence_id: challenge
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-semantic-challenge-agent/semantic-severity-challenge.json
  locator: Final independent challenge
  accessed_at: '2026-10-21T21:48:22.393148Z'
  support: supports
  summary: Exact fields, disposition and bindings verified.
  snapshot_sha256: f99c7e2ac01b2d7d80f07de390afbb6f06ef98182ccdff06f5f8517b0e26fd02
- evidence_id: adjudication
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-range-root-adjudication.json
  locator: Final root disposition
  accessed_at: '2026-10-21T21:48:33.309274Z'
  support: supports
  summary: Final findings and nonfindings control serialization; grounding dissent
    remains explicit.
  snapshot_sha256: e83c5268e0fcfca1446ec2e8c544bbea3716aeba902459d41989da0da8d1d276
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: range identity and broader-family grounding'
  outcome: concern
  target_ids:
  - traitmech:000005
  summary: The retained min/max pressure-range fallback, exact proposed 1007604 and
    active phenotype parent are coherent. GO0006636 is a meaningful broader unsaturated-fatty-acid
    process family for PUFA synthesis; only the maintained historical exactMatch claim
    is a bounded precision concern. Preserve the current PATHWAY and qualified CURIE.
  evidence_ids:
  - record
  - identity
  - metpo-primary
  - proposal-v5-primary
  - go-primary
  - node-mapping-primary
  - go-dissent
  - adjudication
- assessment_id: definition
  area: evidence
  topic: 'Native checklist: growth-supporting pressure interval'
  outcome: supported
  target_ids:
  - traitmech:000005
  summary: The assigned primary abstract directly reports MTCD1 growth from 80 to
    140 MPa at 6 °C. Minimum/maximum bounds differ from the optimum coordinate of
    120 MPa and the derived interval breadth of 60 MPa. Generic review classification
    supports context without requiring the source to coin the local trait label.
  evidence_ids:
  - record
  - sources
  - meta-colwellia
  - canonical-scope
  - body-membrane
- assessment_id: hierarchy
  area: identity
  topic: 'Native checklist: parent and local predicate authorities'
  outcome: supported
  target_ids:
  - traitmech:000005
  summary: Active phenotype parent is appropriate. Exact local defines admits an axis
    parameterizing a numerical trait and Biolink association has broad named-thing
    endpoints. Neither imports a process-only restriction. Three lexical expands/stabilizes
    edges do not silently inherit RO constraints.
  evidence_ids:
  - identity
  - metpo-primary
  - proposal-v4-primary
  - local-authority
  - node-edges
- assessment_id: sources
  area: evidence
  topic: 'Native checklist: all assigned citations and placements'
  outcome: unknown
  target_ids:
  - traitmech:000005
  summary: Four works and eleven external placements are accounted for. Generic membrane
    and solute context is attributable with exceptions. Expansion of the full minimum/maximum
    interval at edge 4 remains UNKNOWN from the inspected nearest source, not refuted.
    Colwellia abstract, actual review bodies and derived HAL text are distinguished.
  evidence_ids:
  - source-ledger
  - placements
  - source-status
  - source-access
  - source-reuse
  - edge-sources
  - body-membrane
  - body-piezolytes
  - body-chemrev
- assessment_id: quotations
  area: evidence
  topic: 'Native checklist: literal unit-format fidelity'
  outcome: concern
  target_ids:
  - traitmech:000005
  summary: First snippet supports all interval, optimum and temperature values after
    degrees C to °C normalization; only literal format differs. Second snippet is
    literal in the assigned membrane body. Native NOT_IN_ABSTRACT results remain unchanged.
  evidence_ids:
  - snippets
  - body-membrane
  - meta-colwellia
  - playbook
  - native-checks
- assessment_id: canonical
  area: evidence
  topic: 'Native checklist: strain and temperature-specific range'
  outcome: supported
  target_ids:
  - traitmech:000005
  summary: Colwellia marinimaniae MTCD1 range 80–140 MPa at 6 °C is explicitly reported
    by the assigned abstract. The source optimum 120 MPa and derived breadth 60 MPa
    are separate quantities. Official species/type aliases verify identity without
    supplying the phenotype.
  evidence_ids:
  - canonical-scope
  - meta-colwellia
  - taxon-colwellia
- assessment_id: nodes
  area: consistency
  topic: 'Native checklist: all nine current referents'
  outcome: concern
  target_ids:
  - traitmech:000005
  summary: Pressure condition, interval/fluidity QUALITY, biosynthetic PATHWAY, chemical
    constituents and explicit accumulation/stabilization processes fit their current
    descriptions. GO broad-family grounding remains qualified positive; root counts
    only the historical exactMatch precision as minor while retaining grounding-auditor
    dissent. No forced replacement, retype, protein or numeric-value finding.
  evidence_ids:
  - node-edges
  - node-sources
  - schema
  - policy
  - pato-primary
  - go-primary
  - go-dissent
  - adjudication
  details: '[{"index": 0, "node": {"node_id": "pressure_range_trait", "label": "pressure
    range", "node_type": "TRAIT", "grounding": "traitmech:000005", "description":
    "Bounded min-to-max hydrostatic pressure supporting growth."}, "assessment": "supported",
    "reason": "Self-grounded min/max growth interval agrees with definition."}, {"index":
    1, "node": {"node_id": "hydrostatic_pressure", "label": "hydrostatic pressure",
    "node_type": "ENVIRONMENTAL_FACTOR", "description": "Ambient hydrostatic pressure
    imposed on the cell.", "grounding": "PATO:0001025"}, "assessment": "supported",
    "reason": "Ambient pressure condition close-matches the primary pressure quality."},
    {"index": 2, "node": {"node_id": "bounded_growth_span", "label": "growth-permissive
    pressure span", "node_type": "QUALITY", "description": "Continuous interval of
    hydrostatic pressures supporting growth."}, "assessment": "supported", "reason":
    "Continuous permissible interval is a measured QUALITY, not a growth-maintenance
    process or scalar delta."}, {"index": 3, "node": {"node_id": "pufa_biosynthesis",
    "label": "polyunsaturated fatty acid biosynthesis", "node_type": "PATHWAY", "description":
    "Synthesis of polyunsaturated fatty acids incorporated into membrane lipids.",
    "grounding": "GO:0006636"}, "assessment": "qualified_positive", "reason": "GO:0006636
    is the active unsaturated fatty acid biosynthetic process, defined by one or more
    double bonds; polyunsaturated fatty acid biosynthesis is explicitly a narrow synonym.
    This provides a meaningful broader process-family grounding for current PUFA synthesis,
    not an exact label-equivalent term. Historical mapping row 192 labels it exactMatch
    under BIOLOGICAL_PROCESS, which overstates the primary synonym scope. Current
    node is PATHWAY and already grounded; the mapper type key and nonempty guard prevent
    straightforward replay. No wrong-material-ID claim or forced PATHWAY retype follows."},
    {"index": 4, "node": {"node_id": "membrane_fluidity_hhp", "label": "membrane fluidity
    under high hydrostatic pressure", "node_type": "QUALITY", "description": "Degree
    of membrane lipid disorder/fluidity maintained against pressure-induced ordering."},
    "assessment": "supported", "reason": "Membrane lipid disorder/fluidity explicitly
    denotes a measurable quality, not the process maintaining it."}, {"index": 5,
    "node": {"node_id": "unsaturated_membrane_lipids", "label": "unsaturated membrane
    lipids", "node_type": "CHEMICAL", "description": "Unsaturated fatty acids in membrane
    phospholipids that counter pressure-induced ordering."}, "assessment": "supported",
    "reason": "Fatty acids in membrane phospholipids are chemical constituents; detailed
    effects belong to the bounded source audit."}, {"index": 6, "node": {"node_id":
    "tmao", "label": "trimethylamine N-oxide (TMAO)", "node_type": "CHEMICAL", "description":
    "Compatible solute / piezolyte excluded from the protein hydration layer."}, "assessment":
    "supported", "reason": "Named TMAO is a chemical referent; absent chemical CURIE
    alone does not create a mandatory grounding or instance gap."}, {"index": 7, "node":
    {"node_id": "protein_stabilization", "label": "protein stabilization via preferential
    hydration", "node_type": "BIOLOGICAL_PROCESS", "description": "Stabilization of
    native protein structure by preferential exclusion of cosolutes."}, "assessment":
    "supported", "reason": "Stabilization is explicitly a biological process; detailed
    physical efficacy is unassessed."}, {"index": 8, "node": {"node_id": "compatible_solute_accumulation",
    "label": "compatible solute accumulation", "node_type": "BIOLOGICAL_PROCESS",
    "description": "Accumulation of compatible solutes (betaine, glutamate, beta-hydroxybutyrate)
    acting as piezolytes."}, "assessment": "supported", "reason": "Accumulation is
    explicitly a biological process, not a protein or a material solute pool."}]'
- assessment_id: predicates
  area: consistency
  topic: 'Native checklist: all seven relation roles'
  outcome: concern
  target_ids:
  - traitmech:000005
  summary: RO2213 at edges 2/3 inherits process/process requirements. Edge 2 has a
    valid processual biosynthetic subject but explicit fluidity QUALITY object; edge
    3 links CHEMICAL constituents to a TRAIT. Group these roles once. Broad local/Biolink
    relations and lexical edges have no invented imported exclusion.
  evidence_ids:
  - node-edges
  - ro-primary
  - local-authority
  - owners
  - challenge
  - adjudication
  details: '[{"index": 0, "edge": {"subject": "hydrostatic_pressure", "predicate":
    "defines", "object": "pressure_range_trait", "description": "The hydrostatic-pressure
    axis defines the min/max bounds bracketed by the pressure range.", "evidence":
    [{"reference": "DOI:10.3389/fmolb.2022.1058381", "notes": "Pressure-adaptation
    review frames the bounded span of growth-permissive pressure as a defining quantitative
    descriptor."}], "predicate_id": "METPO:2007500"}, "assessment": "supported", "reason":
    "Exact local v4 defines supports a pressure measurement axis parameterizing interval
    bounds."}, {"index": 1, "edge": {"subject": "pressure_range_trait", "predicate":
    "associated with", "object": "bounded_growth_span", "description": "The pressure
    range records the bounded interval of permissive hydrostatic pressures.", "evidence":
    [{"reference": "DOI:10.1099/ijsem.0.001671", "notes": "Colwellia marinimaniae
    MTCD1 illustrates a bounded growth-supporting pressure span (80-140 MPa)."}],
    "predicate_id": "biolink:associated_with"}, "assessment": "qualified_positive",
    "reason": "Biolink associated-with has broad named-thing endpoints; current correspondence
    records the measurement interval and is not an independent causal-effect claim."},
    {"index": 2, "edge": {"subject": "pufa_biosynthesis", "predicate": "increases",
    "object": "membrane_fluidity_hhp", "description": "PUFA biosynthesis increases
    membrane fluidity to counter pressure-induced membrane ordering.", "evidence":
    [{"reference": "DOI:10.3389/fmolb.2022.1058381", "notes": "PUFAs (C20:5, C22:6)
    associated with adaptation to high hydrostatic pressure; broad mechanism across
    taxa."}], "predicate_id": "RO:0002213"}, "assessment": "major", "reason": "RO2213
    inherits process/process roles. The named biosynthetic PATHWAY subject is processual,
    but its object is explicitly membrane fluidity QUALITY, not a fluidity-maintenance
    process. The object mismatch is independently sufficient."}, {"index": 3, "edge":
    {"subject": "unsaturated_membrane_lipids", "predicate": "positively regulates",
    "object": "pressure_range_trait", "description": "Unsaturated membrane lipids
    support growth across high hydrostatic pressures.", "evidence": [{"reference":
    "DOI:10.3389/fmolb.2022.1058381", "notes": "Mutants with reduced C18:1 could not
    withstand high pressure; unsaturation counters pressure ordering."}], "predicate_id":
    "RO:0002213"}, "assessment": "major", "reason": "RO2213 process/process relation
    connects explicit chemical constituents to a TRAIT class; current support-for-growth
    prose does not turn those endpoints into processes. Group with edge2 as one imported-role
    issue."}, {"index": 4, "edge": {"subject": "membrane_fluidity_hhp", "predicate":
    "expands", "object": "pressure_range_trait", "description": "Maintaining membrane
    fluidity under pressure expands the growth-supporting pressure range.", "evidence":
    [{"reference": "DOI:10.3390/microorganisms11071629", "notes": "Pressure compacts
    membranes; organisms restore membrane disorder/function via unsaturation to sustain
    growth."}]}, "assessment": "lexical_qualified", "reason": "Ungrounded expands
    has no imported RO constraint. Current quality-to-range language is intelligible,
    but exact empirical expansion and generality are source-scope questions, not an
    inferred formal-domain error."}, {"index": 5, "edge": {"subject": "tmao", "predicate":
    "stabilizes", "object": "protein_stabilization", "description": "TMAO stabilizes
    proteins via preferential hydration (preferential exclusion from hydration layer).",
    "evidence": [{"reference": "DOI:10.1021/acs.chemrev.3c00432", "notes": "TMAO preferentially
    excluded from protein hydration layer causing preferential hydration; biophysical
    mechanism, not microbe-specific."}]}, "assessment": "lexical_qualified", "reason":
    "Ungrounded stabilizes does not inherit RO enables or regulates roles. Chemical-to-stabilization
    context can be described without inventing an imported material-executor restriction;
    source-specific physical wording is separately audited."}, {"index": 6, "edge":
    {"subject": "compatible_solute_accumulation", "predicate": "stabilizes", "object":
    "protein_stabilization", "description": "Compatible solutes stabilize proteins
    via preferential hydration.", "evidence": [{"reference": "DOI:10.3390/microorganisms11071629",
    "notes": "Compatible solutes (glutamate, betaine, beta-hydroxybutyrate) act by
    preferential hydration, displacing protein-bound water."}]}, "assessment": "lexical_qualified",
    "reason": "Ungrounded stabilizes links accumulation to stabilization processes
    without an imported relation ID. Formal annotation gap alone is not a mandatory
    defect; detailed hydration wording and efficacy are separately source-scoped."}]'
- assessment_id: biology
  area: evidence
  topic: 'Native checklist: generic physical attribution and hydration wording'
  outcome: concern
  target_ids:
  - traitmech:000005
  summary: Piezolytes paragraph 26 faithfully supplies the water-displacement note,
    while assigned ChemRev explains cosolute exclusion with preferential protein hydration,
    agreeing with current nodes 6/7 and edge 5. Preserve that explanatory inconsistency
    as a bounded note concern, not a fabricated citation. Lipid and solute effects
    vary with taxa/conditions. Detailed pathogen pressure-defense, fitness, AMR, intervention
    efficacy and methods remain UNASSESSED_SCOPE.
  evidence_ids:
  - edge-sources
  - source-reading
  - source-access
  - hydration-scope
  - body-membrane
  - body-piezolytes
  - body-chemrev
  - chemrev-text
- assessment_id: completeness
  area: completeness
  topic: 'Native checklist: NONMECHANISTIC applicability'
  outcome: supported
  target_ids:
  - traitmech:000005
  summary: Two disclosed components, zero protein classes and zero instances are proportionate
    to the contextual interval graph. No mandatory connector, molecular instance,
    extra canonical or experiment is prescribed; ungrounded lexical relations are
    not automatically defects.
  evidence_ids:
  - record
  - node-edges
  - policy
  - ground-reading
- assessment_id: expression
  area: evidence
  topic: 'Native checklist: catalog applicability and bounded query scope'
  outcome: unknown
  target_ids:
  - traitmech:000005
  summary: Canonical Colwellia/MTCD1 aliases do not match the retained 20-organism
    / 28-dataset catalog. Other source-organism coverage is not globally denied. No
    strain-resolved locus or detailed pressure-response query was run.
  evidence_ids:
  - expression
  - catalog-reuse
  - taxon-colwellia
- assessment_id: ownership
  area: provenance
  topic: 'Native checklist: current assertions and conditional mappings'
  outcome: supported
  target_ids:
  - traitmech:000005
  summary: Record owns current assertions. Wildcard predicate mapping and shared grounder
    recur only on empty IDs and skip current nonempty values. Historical PUFA exactMatch
    row is keyed BIOLOGICAL_PROCESS rather than current PATHWAY, also preventing simple
    replay. Exact PATHWAY normalization and canonical backfill are positive context;
    sibling writers are not asserted current repair owners.
  evidence_ids:
  - owners
  - ground-reading
  - local-authority
  - node-mapping-primary
- assessment_id: human
  area: provenance
  topic: 'Native checklist: bounded acceptance trace'
  outcome: concern
  target_ids:
  - traitmech:000005
  summary: Ten current events are all AI. Ignored-inclusive discovery found zero repository
    history leads; 217 matching paths and 69 structured review arrays contain zero
    exact current-target arrays. This bounds the missing acceptance link without excluding
    remote or private review.
  evidence_ids:
  - owners
  - ground-reading
  - playbook
  - challenge
  - adjudication
- assessment_id: readiness
  area: consistency
  topic: 'Native checklist: actual checks and local preparation'
  outcome: supported
  target_ids:
  - traitmech:000005
  summary: All 68 inputs match. Current native, strict and direct network snippet
    commands pass, without an invented initial target-specific failure. Historical
    common failures/retries remain preserved. Actual B11 QC/B12 qualification/postcheck
    and local initialization are distinct from pending publication. The wrapper diagnostic
    after completed capture is not a native-review failure.
  evidence_ids:
  - capture
  - source-capture
  - reuse
  - reuse-postcheck
  - local-init
  - native-checks
  - check-pressure-range-native
  - check-pressure-range-strict
  - check-pressure-range-snippets-network
findings:
- finding_id: process-regulation-roles
  issue_key: pressure-range-process-regulation-roles
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Process regulation is assigned to quality and trait endpoints
  description: RO2213 inherits process domain and range. Edge 2 has a meaningful biosynthetic
    PATHWAY subject but a membrane-fluidity QUALITY object; edge 3 connects CHEMICAL
    constituents to the pressure-range TRAIT. Growth-support prose does not change
    those referents. Group both mismatches, preserving current node facets and contextual
    source evidence without prescribing detailed mechanism repair.
  target_ids:
  - traitmech:000005
  field_paths:
  - causal_graphs[0].edges[2]
  - causal_graphs[0].edges[3]
  evidence_ids:
  - node-edges
  - ro-primary
  - schema
  - owners
  - body-membrane
  - challenge
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/pressure_range.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Wildcard increases/positively-regulates rows may recur only on empty predicate
      fields.
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Existing nonempty IDs are skipped; mapping edits alone do not repair current
      assertions.
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: go-mapping-precision
  issue_key: pressure-range-go-mapping-precision
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Historical mapping overstates a broader-family match as exact
  description: GO0006636 covers unsaturated-fatty-acid biosynthesis with one or more
    double bonds and marks PUFA biosynthesis as a narrow synonym. The current CURIE
    remains a meaningful broader family; maintained historical mapping row 192 labels
    the narrower phrase exactMatch. Qualify that provenance, without asserting a wrong
    current CURIE or forced PATHWAY retype. Current type and nonempty guards prevent
    automatic replay. Ground auditor preferred a limitation; root/challenger calibrated
    this narrow mapping precision as minor.
  target_ids:
  - traitmech:000005
  field_paths:
  - causal_graphs[0].nodes[3].grounding
  evidence_ids:
  - identity
  - go-primary
  - node-mapping-primary
  - go-dissent
  - owners
  - challenge
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/pressure_range.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: mappings/node_grounding.tsv
    role: Historical row 192 exactMatch overstates the narrower PUFA scope; current
      PATHWAY key and nonempty guards prevent simple replay.
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: hydration-explanation-precision
  issue_key: pressure-range-hydration-explanation-precision
  category: consistency
  severity: minor
  status: open
  certainty: confirmed
  title: Assigned hydration explanations conflict
  description: The edge 6 note faithfully follows the piezolyte review in describing
    displacement of protein-bound water. Assigned ChemRev describes cosolute exclusion
    with preferential protein hydration, agreeing with current nodes 6/7 and edge
    5. Preserve the source disagreement and qualify this explanatory note; do not
    call the attribution fabricated or infer a universal solute mechanism.
  target_ids:
  - traitmech:000005
  field_paths:
  - causal_graphs[0].edges[6].evidence[0].notes
  evidence_ids:
  - hydration-scope
  - node-sources
  - edge-sources
  - body-piezolytes
  - body-chemrev
  - chemrev-text
  - challenge
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/pressure_range.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: literal-unit-format
  issue_key: pressure-range-literal-unit-format
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Snippet changes the supported temperature-unit notation
  description: The record writes degrees C where the actual primary abstract uses
    °C. Interval, optimum and temperature remain supported after normalization; only
    literal copied-span fidelity is implicated. The canonical 80–140 MPa range at
    6 °C remains positive.
  target_ids:
  - traitmech:000005
  field_paths:
  - evidence[0].snippet
  evidence_ids:
  - snippets
  - meta-colwellia
  - playbook
  - challenge
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/pressure_range.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: human-acceptance-link
  issue_key: pressure-range-human-acceptance-link
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Reviewed status lacks a locally attributable acceptance link
  description: Ten AI events, zero matching repository history leads and ignored-inclusive
    217 matching paths/69 parsed review arrays/zero exact targets do not identify
    current-target human acceptance. This bounded traceability gap does not rule out
    private or remote review.
  target_ids:
  - traitmech:000005
  field_paths:
  - mapping_status
  - curation_history
  evidence_ids:
  - owners
  - ground-reading
  - playbook
  - challenge
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/pressure_range.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
actions:
- action_id: reconcile-imported-roles
  description: Reconcile edges 2/3 imported process-regulation roles with their actual
    referents during authorized curation.
  finding_ids:
  - process-regulation-roles
  target_ids:
  - traitmech:000005
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/pressure_range.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Wildcard increases/positively-regulates rows may recur only on empty predicate
      fields.
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Existing nonempty IDs are skipped; mapping edits alone do not repair current
      assertions.
  acceptance_checks:
  - Preserve valid processual pathway and measured-quality facets and contextual source
    evidence.
  - Respect nonempty-ID guards; mapping changes alone do not repair current assertions.
  - No detailed mechanism reconstruction or intervention prescription.
- action_id: qualify-go-mapping
  description: Qualify historical mapping exactness and the retained broader-family
    grounding.
  finding_ids:
  - go-mapping-precision
  target_ids:
  - traitmech:000005
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/pressure_range.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: mappings/node_grounding.tsv
    role: Historical row 192 exactMatch overstates the narrower PUFA scope; current
      PATHWAY key and nonempty guards prevent simple replay.
  acceptance_checks:
  - Preserve current meaningful GO family and PATHWAY type unless separate evidence
    warrants change.
  - Do not require an invented replacement CURIE or claim unconditional replay.
  - Retain the independent grounding severity qualification.
- action_id: clarify-hydration-note
  description: Clarify the conflicting hydration explanation while preserving accurate
    source attribution.
  finding_ids:
  - hydration-explanation-precision
  target_ids:
  - traitmech:000005
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/pressure_range.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Identify the source disagreement explicitly; do not silently report the note as
    a fabricated quote.
  - Retain non-microbial-specific physical context and taxon/condition limitations.
  - No experimental efficacy or intervention prescription.
- action_id: restore-literal-format
  description: Use the actual source unit notation for the supported snippet.
  finding_ids:
  - literal-unit-format
  target_ids:
  - traitmech:000005
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/pressure_range.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Preserve all numerical values and source identity.
- action_id: link-human-acceptance
  description: Link attributable acceptance if available or clarify status while preserving
    provenance.
  finding_ids:
  - human-acceptance-link
  target_ids:
  - traitmech:000005
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/pressure_range.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Retain all ten AI events and bounded ignored-inclusive search evidence.
  - No contact or automatic status promotion authorized.
limitations:
- Detailed pathogen pressure-defense, fitness, AMR, intervention efficacy and methods
  are UNASSESSED_SCOPE; incidental displayed source content is not adopted.
- Canonical MTCD1 interval 80–140 MPa at 6 °C is explicit, distinct from optimum 120
  MPa and derived breadth 60 MPa. Colwellia primary body was not acquired/inspected;
  no failed new request or paper-wide absence is implied.
- Exact widening of minimum/maximum growth endpoints at edge 4 remains UNKNOWN from
  inspected nearest-source context. Generic lipid support and source exceptions do
  not prove a universal mechanism or false claim.
- Piezolyte displacement wording is faithfully cited but conflicts with the assigned
  cosolute-exclusion/protein-hydration explanation; source disagreement is preserved,
  not silently resolved as false attribution.
- GO0006636 is a meaningful broader process-family grounding. Only the historical
  exactMatch precision is counted; the grounding auditor preferred a limitation, and
  current PATHWAY/nonempty guards limit replay.
- Original metadata/body acquisitions, current copies at 21:42:39 UTC and later selected
  readings are separately bound. ChemRev is a HAL author-deposited manuscript with
  derived text, not publisher HTML or a new acquisition. Official taxonomy retains
  original 16:11:19–20 success and prior DNS failure.
- Fallback/proposed 1007604 is not an installed active exact replacement. Zero proteins/instances
  and two contextual components do not require speculative connectors or additional
  assays.
- Canonical catalog absence and local human-traceability search are bounded; no global
  source-organism absence or private-review absence is asserted.
- Actual prior QC, qualification and local initialization do not assert B11 remote
  publication; publication remains separately documented.
notes:
- Final root adjudication and independent challenge are pinned; no builder/helper
  import or execution during preparation.
- 'Coverage: four works/four forms, eleven external placements, seven grounding fields,
  nine nodes/seven edges, one canonical and two snippets: one literal and one supported
  unit transcription.'
- No scientific record, native inventory, Git or sweep-state mutation by serializer
  preparation.
tags:
- record-review
- pressure-range
- environment
- needs-curation
native_verdict: needs_curation
```
