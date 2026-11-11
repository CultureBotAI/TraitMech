# Whole-record review of pressure delta

- Review: 20261021T212815Z-pressure-delta
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-21T21:16:57.952674Z
- Finished UTC: 2026-10-21T21:28:15Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Final root disposition: one formal-role major and four bounded description, attribution, literal-format and human-acceptance minors.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: Second record of the actual locally initialized batch 012 queue. Whole 247-line target and all 64 captured inputs verified before assessment. Local initialization at 21:02:18.445284 UTC does not assert publication of batch 011.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8eee04a8c65609fbaff6df7c54597dcaf1b9d282.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| traitmech:000006 | data/traits/environment/pressure_delta.yaml | maintained | pressure delta |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full-corpus graph audit | passed | True | traitmech:000006 | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| Full-corpus snippet audit | passed | True | traitmech:000006 | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| Full-corpus pathway links | passed | True | traitmech:000006 | 19 links checked against the pinned PathwayMech snapshot. |
| Full-corpus history integrity | passed | True | traitmech:000006 | 1277 history records checked, zero invalid links at the 8eee source base; integrity does not establish science or human acceptance. |
| Initial full-product validation | failed | False | traitmech:000006 | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation with isolated local cache | failed | False | traitmech:000006 | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation after isolated-cache download | passed | True | traitmech:000006 | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| Focused native validation | passed | True | traitmech:000006 | Successful schema validation; source and semantics separately assessed. |
| Focused strict validation | passed | True | traitmech:000006 | Successful strict validation; no biological efficacy certification. |
| Initial focused snippet attempt | failed | False | traitmech:000006 | DNS failure, exit 2, retained separately from successful network retry; no completed-review failure inferred. |
| Focused snippet network retry | passed | True | traitmech:000006 | Two fields over two references: both NOT_IN_ABSTRACT. Actual membrane body verifies first literally; Colwellia abstract supports second after explicit unit transcription. |
| Reused maintained batch-eleven QC | passed | True | traitmech:000006 | Actual B11 final QC at its original time, qualified against B12 bytes; independent of pending publication. |
| Protein-instance metadata applicability | not_applicable | False | traitmech:000006 | One reviewed label-only Complex I aggregate, zero instances; no forced UniProt accession or detailed pressure-response query. |

## Scientific And Domain Assessments

### Native checklist: derived pressure breadth

identity: supported. Targets: traitmech:000006.

Retained traitmech:000006 denotes max minus min of a growth-supporting pressure interval, distinct from broader pressure tolerance/preference. Proposed 1007605 is an exact local lift, not an installed active replacement.

### Native checklist: measurement definition and source context

evidence: supported. Targets: traitmech:000006.

The operational breadth definition is coherent and illustrated by an explicitly reported interval. The membrane review supplies pressure-adaptation context; this audit does not claim that it coins the term pressure delta or establishes every generic mechanism as an exclusive breadth determinant.

### Native checklist: parent and local defines authority

identity: supported. Targets: traitmech:000006.

Active phenotype parent is appropriate. Local v4 defines admits an axis or growth-bound feature parameterizing a quantitative trait; broad local endpoints do not waive imported RO requirements.

### Native checklist: all assigned citations and placements

evidence: concern. Targets: traitmech:000006.

Six works and fifteen external placements accounted for. The comparative Colwellia desaturase statement is broadened in one note to all piezophiles; other contextual source inferences and unavailable bodies remain qualified limitations. Metadata, actual article files, author manuscript and derived browser receipt have separate provenance.

### Native checklist: literal unit-format fidelity

evidence: concern. Targets: traitmech:000006.

First snippet is literal in the assigned membrane body. Second supports all interval, optimum and temperature values after degrees C to °C normalization; only literal copied-span format differs. Native NOT_IN_ABSTRACT results remain unchanged.

### Native checklist: measured interval and derived arithmetic

evidence: supported. Targets: traitmech:000006.

Colwellia marinimaniae MTCD1 grew over 80–140 MPa at 6 °C, giving 140 minus 80 = 60 MPa. The optimum 120 MPa is a separate value. Assigned abstract and comparative article support this strain/temperature-specific observation; official species/type aliases are independently verified.

### Native checklist: all twelve current referents

consistency: concern. Targets: traitmech:000006.

Pressure condition, breadth/bounds qualities and explicitly named production, loss and maintenance processes are coherent. Node 9 label and reviewed aggregate denote protein Complex I, while its description calls it an operon; this is a bounded description precision issue, not a protein identity major or mandatory accession.

[{"index": 0, "node": {"node_id": "pressure_delta_trait", "label": "pressure delta", "node_type": "TRAIT", "grounding": "traitmech:000006", "description": "Breadth (max − min) of the growth-supporting hydrostatic-pressure range."}, "assessment": "supported", "reason": "Self-grounded derived measurement trait, same max-minus-min identity as definition."}, {"index": 1, "node": {"node_id": "hydrostatic_pressure", "label": "hydrostatic pressure", "node_type": "ENVIRONMENTAL_FACTOR", "description": "Ambient hydrostatic pressure imposed on the cell.", "grounding": "PATO:0001025"}, "assessment": "supported", "reason": "Ambient pressure condition has an explicit PATO physical-quality close match; current type permits environmental conditions."}, {"index": 2, "node": {"node_id": "pressure_tolerance_breadth", "label": "pressure-tolerance breadth", "node_type": "QUALITY", "description": "Width of the hydrostatic-pressure interval over which growth is sustained."}, "assessment": "supported", "reason": "Width of a growth-supporting interval is a measurable quality, not an asserted process."}, {"index": 3, "node": {"node_id": "membrane_fluidity_maintenance", "label": "membrane fluidity maintenance under high pressure", "node_type": "BIOLOGICAL_PROCESS", "description": "Maintenance of adequate membrane fluidity against pressure-induced lipid compression."}, "assessment": "supported", "reason": "Maintenance is explicitly a biological process; no capacity/state retyping follows from its noun phrase."}, {"index": 4, "node": {"node_id": "membrane_fluidity_loss", "label": "loss of membrane fluidity at high pressure", "node_type": "BIOLOGICAL_PROCESS", "description": "Pressure-induced reduction of membrane fluidity that impairs membrane function."}, "assessment": "supported", "reason": "Loss/reduction denotes change, compatible with process representation; detailed biological efficacy unassessed."}, {"index": 5, "node": {"node_id": "unsaturated_fatty_acid_production", "label": "unsaturated fatty acid production", "node_type": "BIOLOGICAL_PROCESS", "description": "Biosynthesis/desaturation generating unsaturated acyl chains that counter pressure-induced membrane ordering."}, "assessment": "supported", "reason": "Biosynthesis/desaturation explicitly denotes a process. This supplies the subject-role conflict at edge 2, not a defect in this node type."}, {"index": 6, "node": {"node_id": "ribosome_dissociation", "label": "pressure-induced ribosome dissociation", "node_type": "BIOLOGICAL_PROCESS", "description": "High-pressure dissociation of ribosomes suppressing translation and growth."}, "assessment": "supported", "reason": "Dissociation explicitly denotes a process; detailed pressure effects remain outside this formal audit."}, {"index": 7, "node": {"node_id": "compatible_solutes", "label": "intracellular osmolytes / compatible solutes", "node_type": "CHEMICAL", "description": "Cosolutes/osmolytes that stabilize protein structure under high hydrostatic pressure."}, "assessment": "supported", "reason": "Cosolutes are material chemical entities; no mandatory exact chemical accession is inferred for the broad collective label."}, {"index": 8, "node": {"node_id": "protein_stabilization_under_pressure", "label": "protein stabilization under pressure", "node_type": "BIOLOGICAL_PROCESS", "description": "Reinforcement of protein structure against pressure-induced perturbation."}, "assessment": "supported_with_qualification", "reason": "Stabilization is a process; direct chemical stabilization can fit executor semantics, with detailed efficacy unassessed."}, {"index": 9, "node": {"node_id": "nuo_complex_i", "label": "nuo NADH dehydrogenase I complex", "node_type": "GENE_OR_PROTEIN", "grounding_status": "REVIEWED_LABEL_ONLY", "grounding_notes": "Reviewed as a contextual protein or protein-complex label within a quantitative measurement graph; no exact semantic family term was established for this aggregate use.", "description": "Proton-translocating NADH dehydrogenase I (Complex I) operon enriched in piezophiles."}, "assessment": "minor_precision", "reason": "Label, reviewed-label-only rationale and edge 8 identify a protein complex, but description explicitly calls that same referent an operon. Clarify the protein-complex description and keep operon information as metadata; not a gene-as-protein identity major or mandatory accession finding."}, {"index": 10, "node": {"node_id": "high_pressure_energy_conservation", "label": "high-pressure respiratory energy conservation", "node_type": "BIOLOGICAL_PROCESS", "description": "Respiratory-chain energy conservation supporting growth under high hydrostatic pressure."}, "assessment": "supported", "reason": "Energy conservation is explicitly a process; detailed fitness effects unassessed."}, {"index": 11, "node": {"node_id": "min_max_growth_pressure_bounds", "label": "minimum and maximum growth pressure bounds", "node_type": "QUALITY", "description": "Lower and upper hydrostatic-pressure limits of growth whose difference defines the delta."}, "assessment": "supported", "reason": "Minimum and maximum growth bounds are measurable attributes defining a derived difference."}]

### Native checklist: all ten relation roles

consistency: concern. Targets: traitmech:000006.

RO2327 enables inherits material executor to process through 2327→2215→2216→2500→2595. Edge 2 instead has an explicit production-process subject. Edge 7 chemical-to-stabilization process has compatible roles and qualified direct stabilization meaning. Biolink broad endpoints, local defines and lexical restricts/supports are not assigned invented RO restrictions.

[{"index": 0, "edge": {"subject": "hydrostatic_pressure", "predicate": "defines", "object": "pressure_delta_trait", "description": "The hydrostatic-pressure axis defines the values whose max minus min yields the delta.", "evidence": [{"reference": "DOI:10.3389/fmolb.2022.1058381", "notes": "Pressure-adaptation review frames the breadth of the pressure-tolerance span as a derived descriptor of pressure-adaptation flexibility."}], "predicate_id": "METPO:2007500"}, "assessment": "supported", "reason": "Local v4 defines explicitly admits a measurement axis parameterizing a numerical phenotype; no process-domain requirement."}, {"index": 1, "edge": {"subject": "pressure_delta_trait", "predicate": "associated with", "object": "pressure_tolerance_breadth", "description": "The delta encodes the breadth of pressure-tolerance flexibility.", "evidence": [{"reference": "DOI:10.1099/ijsem.0.001671", "notes": "The 80-140 MPa span of Colwellia marinimaniae MTCD1 (delta = 60 MPa) illustrates the breadth this phenotype records."}], "predicate_id": "biolink:associated_with"}, "assessment": "supported_with_qualification", "reason": "Biolink association uses broad named-thing endpoints. The edge is definitional correspondence between the delta and its breadth facet, not a demonstrated causal execution relation; no new statistical mechanism claim is inferred."}, {"index": 2, "edge": {"subject": "unsaturated_fatty_acid_production", "predicate": "enables", "object": "membrane_fluidity_maintenance", "description": "Unsaturated acyl-chain production/desaturation sustains membrane fluidity under high hydrostatic pressure.", "evidence": [{"reference": "DOI:10.1186/s12864-020-07102-y", "notes": "All piezophiles encode a delta-9 acyl-phospholipid desaturase; unsaturated chains allow better adaptation to higher pressures (general HHP mechanism)."}, {"reference": "DOI:10.1021/acs.chemrev.3c00432", "notes": "Membrane fluidity adjustment is a core pressure-adaptation node."}], "predicate_id": "RO:0002327"}, "assessment": "major", "reason": "RO2327 enables requires an executor capable of and executing a process. The full ancestor chain gives material entity to process. Subject node 5 is expressly a biosynthetic/desaturation process, while object maintenance is a process. The production-process subject is the confirmed mismatch."}, {"index": 3, "edge": {"subject": "hydrostatic_pressure", "predicate": "causes", "object": "membrane_fluidity_loss", "description": "High hydrostatic pressure compresses membranes and reduces fluidity.", "evidence": [{"reference": "DOI:10.3389/fmicb.2024.1293928", "notes": "High pressure causes loss of membrane fluidity (cross-taxa physiological mechanism)."}], "predicate_id": "biolink:causes"}, "assessment": "supported_formal_scope", "reason": "Current Biolink causes has broad named-thing ancestry and no inherited RO process-only endpoint restriction. A pressure quality subject is not automatically a role failure; source causality is assessed separately."}, {"index": 4, "edge": {"subject": "membrane_fluidity_loss", "predicate": "restricts", "object": "pressure_tolerance_breadth", "description": "Loss of membrane fluidity limits growth at the upper pressure bound, narrowing the supported range.", "evidence": [{"reference": "DOI:10.1038/s43247-023-01045-4", "notes": "Reduced membrane fluidity under HHP coincides with cessation of respiration/degradation, restricting the upper growth bound."}]}, "assessment": "lexical_only", "reason": "Ungrounded restricts asserts a qualitative limitation; no imported RO domain/range is imposed and no quantitative breadth effect is certified."}, {"index": 5, "edge": {"subject": "hydrostatic_pressure", "predicate": "causes", "object": "ribosome_dissociation", "description": "High pressure induces ribosome dissociation, suppressing translation and growth.", "evidence": [{"reference": "DOI:10.1038/s43247-023-01045-4", "notes": "High pressure causes ribosome dissociation; translation/replication become dysfunctional, preventing growth and division."}], "predicate_id": "biolink:causes"}, "assessment": "supported_formal_scope", "reason": "Current Biolink causes broad endpoints do not automatically exclude ambient pressure. Detailed pressure-induced ribosome biology remains unassessed."}, {"index": 6, "edge": {"subject": "ribosome_dissociation", "predicate": "restricts", "object": "pressure_tolerance_breadth", "description": "Translation failure from ribosome dissociation limits the growth-supporting pressure range.", "evidence": [{"reference": "DOI:10.1038/s43247-023-01045-4", "notes": "Ribosome dissociation preventing growth and division narrows the pressure range over which growth is sustained."}]}, "assessment": "lexical_only", "reason": "Ungrounded restricts has no imported process/material endpoint requirement; detailed biological effect remains unassessed."}, {"index": 7, "edge": {"subject": "compatible_solutes", "predicate": "enables", "object": "protein_stabilization_under_pressure", "description": "Intracellular osmolytes/cosolutes reinforce protein structure under high hydrostatic pressure.", "evidence": [{"reference": "DOI:10.1021/acs.chemrev.3c00432", "notes": "Osmolytes reinforce the structure of proteins; cosolutes modulate biomolecular function under HHP (general mechanism)."}], "predicate_id": "RO:0002327"}, "assessment": "qualified_positive", "reason": "Chemical cosolutes to stabilization process meet RO material/process endpoints. Direct stabilization wording can support execution; no categorical chemical prohibition or additional precision finding is inferred."}, {"index": 8, "edge": {"subject": "nuo_complex_i", "predicate": "supports", "object": "high_pressure_energy_conservation", "description": "The nuo NADH dehydrogenase I complex supports respiratory energy conservation enabling growth under high pressure.", "evidence": [{"reference": "DOI:10.1186/s12864-020-07102-y", "notes": "nuo dehydrogenase operons present in piezophiles; respiratory-chain composition modulates pressure tolerance, a candidate contributor to wider high-pressure growth support."}]}, "assessment": "lexical_only", "reason": "Ungrounded supports links a contextual protein-complex aggregate to a process; the operon wording issue belongs to node 9 only. Detailed efficacy is unassessed."}, {"index": 9, "edge": {"subject": "min_max_growth_pressure_bounds", "predicate": "defines", "object": "pressure_delta_trait", "description": "The minimum and maximum growth-pressure limits define the breadth (max minus min) recorded by the delta.", "evidence": [{"reference": "DOI:10.1186/s12864-020-07102-y", "notes": "Range-bound examples (e.g., MTCD1 80-140 MPa =&gt; delta = 60 MPa) show min/max bounds defining the pressure-delta breadth descriptor."}], "predicate_id": "METPO:2007500"}, "assessment": "supported", "reason": "The pair of growth pressure bounds operationally defines their difference; v4 defines feature-to-trait meaning fits."}]

### Native checklist: generic environmental context and limitations

evidence: unknown. Targets: traitmech:000006.

Selected membrane, physical chemistry and comparative environmental observations support contextual pressure/fluidity, solute and growth-bound associations. Community respiration versus species growth and the conditional nuo contribution remain qualifications. Detailed pressure-defense, fitness, AMR, survival training, intervention efficacy and methods are UNASSESSED_SCOPE.

### Native checklist: NONMECHANISTIC applicability

completeness: supported. Targets: traitmech:000006.

Four disclosed components, one reviewed label-only aggregate and zero instances are compatible with the contextual quantitative graph. No mandatory connector, pathway, protein instance, additional canonical or experiment is prescribed.

### Native checklist: catalog applicability and bounded query scope

evidence: unknown. Targets: traitmech:000006.

Canonical Colwellia/MTCD1 aliases do not match the retained 20-organism / 28-dataset catalog. No strain-resolved locus or detailed pressure-response module query was run. This does not assert global dataset absence.

### Native checklist: current and conditional writers

provenance: supported. Targets: traitmech:000006.

Record owns node 9 wording and source notes. Predicate mapping/shared grounder conditionally recur on empty IDs; nonempty IDs are skipped. Exact canonical backfill is positive and guarded. Sibling reviewers and trait-object migrations do not repair current process-object edge 2.

### Native checklist: bounded acceptance trace

provenance: concern. Targets: traitmech:000006.

Seven current events are all AI. One whole contextual repository history does not identify current-target acceptance. Ignored-inclusive 239 matching paths/67 structured arrays/zero exact target arrays bound this gap; remote or private review is not ruled out.

### Native checklist: actual checks and local preparation

consistency: supported. Targets: traitmech:000006.

All 64 inputs match. Native/strict and snippet retry pass; initial DNS failure is retained as optional. Actual B11 QC/B12 qualification/postcheck and local initialization are distinct from pending B11 publication.

## Findings

### process-as-executor: Imported enables uses a production process as its material executor

major / open / confirmed; issue key: pressure-delta-process-as-executor.

RO2327 inherits a material-entity executor domain and process range. Current edge 2 subject explicitly denotes unsaturated fatty acid production/desaturation, a process, while its object is a maintenance process. Preserve the source-backed generic observation while reconciling the formal assertion; this is not a defect in the correctly typed production node.

### complex-operon-wording: Protein-complex description calls its referent an operon

minor / open / confirmed; issue key: pressure-delta-complex-operon-wording.

Node 9 label, reviewed aggregate rationale and outgoing relation identify Complex I, while its description uses operon. Clarify this local description without inferring a gene-as-protein identity major, forced accession or detailed respiratory mechanism repair.

### desaturase-cohort-scope: Comparative Colwellia statement is broadened to all piezophiles

minor / open / confirmed; issue key: pressure-delta-desaturase-cohort-scope.

The assigned genomic comparison scopes the desaturase observation to its piezophilic Colwellia cohort; the current note broadens this to all piezophiles. Generic unsaturated-lipid context remains supported, including source exceptions. This is a bounded attribution correction, not proof of a universal biological absence or false entire paper.

### literal-unit-format: Snippet changes the source unit notation

minor / open / confirmed; issue key: pressure-delta-literal-unit-format.

The record writes degrees C where the source abstract uses °C. All interval, optimum and temperature values are supported after normalization; only the maintained literal copied-span rule is implicated.

### human-acceptance-link: Current reviewed status lacks a locally attributable acceptance link

minor / open / confirmed; issue key: pressure-delta-human-acceptance-link.

Seven AI events and one contextual history do not identify current-target human acceptance. Ignored-inclusive 239 matching paths/67 parsed arrays/zero exact targets bound this traceability concern; no private or remote review absence is claimed.

## Recommended Actions And Acceptance Checks

### reconcile-imported-role

Reconcile the imported enables assertion with the actual process referents during authorized curation.

- Preserve supported generic environmental observations and correct production node type.
- Respect nonempty-ID guards; mapping edits do not automatically replace current assertions.
- No detailed mechanism or intervention reconstruction.

### clarify-complex-description

Clarify node 9 description so it denotes the existing protein-complex aggregate.

- Retain operon information only as appropriately separated metadata.
- No mandatory protein instance, locus or mechanistic repair.

### restore-cohort-scope

Scope the desaturase attribution to the actual comparative source cohort.

- Preserve supported generic membrane context and source-specific exceptions.
- Do not replace a bounded comparison with a universal biological claim.

### restore-literal-format

Use the actual source unit notation for the supported snippet.

- Preserve all numerical values and source identity.

### link-human-acceptance

Link attributable acceptance if available or clarify status while preserving provenance.

- Retain all seven AI events and bounded contextual history/search evidence.
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
| check-pressure-delta-native | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-native.log; Executed 2026-10-21T21:17:20.030558+00:00 through 2026-10-21T21:17:20.546728+00:00; metadata pressure-delta-native.json | context_only | Successful schema validation; source and semantics separately assessed. |
| check-pressure-delta-strict | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-strict.log; Executed 2026-10-21T21:17:20.030424+00:00 through 2026-10-21T21:17:20.899084+00:00; metadata pressure-delta-strict.json | context_only | Successful strict validation; no biological efficacy certification. |
| check-pressure-delta-snippets | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-snippets.log; Executed 2026-10-21T21:17:20.031650+00:00 through 2026-10-21T21:17:34.152174+00:00; metadata pressure-delta-snippets.json | context_only | DNS failure, exit 2, retained separately from successful network retry; no completed-review failure inferred. |
| check-pressure-delta-snippets-retry-network | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-snippets-retry-network.log; Executed 2026-10-21T21:17:46.041110+00:00 through 2026-10-21T21:17:49.454967+00:00; metadata pressure-delta-snippets-retry-network.json | context_only | Two fields over two references: both NOT_IN_ABSTRACT. Actual membrane body verifies first literally; Colwellia abstract supports second after explicit unit transcription. |
| check-batch011-qc | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/batch011-qc.log; Executed 2026-10-21T20:52:41.208560+00:00 through 2026-10-21T20:54:10.001030+00:00; metadata batch011-qc.json | context_only | Actual B11 final QC at its original time, qualified against B12 bytes; independent of pending publication. |
| record | data/traits/environment/pressure_delta.yaml; Entire current 247-line record | supports | Twelve nodes, ten edges, two snippets, one canonical and seven AI events covered. |
| policy | docs/GROUNDING_POLICY.md; Captured maintained authority | supports | Referent-based formal roles and permitted reviewed protein aggregate. |
| playbook | docs/CURATION_PLAYBOOK.md; Captured maintained authority | supports | Source scope, literal copied snippets and attributable acceptance. |
| schema | src/traitmech/schema/traitmech.yaml; Captured maintained authority | supports | Current node facets and review contract. |
| checklist | .claude/skills/curate-yaml-record/references/review-checklist.md; Captured maintained authority | supports | Whole-record identity, evidence, graph, provenance and readiness checks. |
| reuse | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/common-reuse-b11-qc-supplement-qualified.json; Actual B11-to-B12 qualification | supports | Original outcomes and all current byte comparisons bound. |
| reuse-postcheck | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/common-reuse-output-verification-agent/post-execution-verification.json; Independent actual-output verification | supports | Actual output/hash postcheck; no new QC. |
| local-init | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/batch012-local-initialization-receipt.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Local-only initialization on verified prior local commit; publication status remains separately documented. |
| capture | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-grounding-agent/capture-verification.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | All 64 inputs verified before grounding assessment. |
| identity | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-grounding-agent/identity-assessment.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Retained fallback denotes a derived breadth, distinct from tolerance and preference. |
| node-edges | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-grounding-agent/node-edge-ledger.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | All twelve nodes/ten edges and four components; imported roles separate from biological efficacy. |
| owners | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-grounding-agent/owner-provenance-assessment.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Current/shared owners and guarded historical context; bounded human search. |
| expression | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-grounding-agent/expression-and-readiness-assessment.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Canonical catalog applicability and contextual protein disposition. |
| catalog-reuse | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-grounding-agent/catalog-reuse-receipt.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Original catalog and runner receipts separate from current copies. |
| local-authority | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-grounding-agent/local-authority-excerpts.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Exact v5/v4 proposals, maintained mappings, schema and Biolink. |
| ground-reading | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-grounding-agent/reading-scope-receipt.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Actual selected primary/owner readings and one whole context history, not direct target approval. |
| ground-manifest | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-grounding-agent/evidence-manifest.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Frozen 28 grounding artifacts verified. |
| taxon-reuse | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-grounding-agent/taxonomy-reuse-receipt.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Original Colwellia request and retained initial DNS failure separate from current copies. |
| ro-intermediate | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-grounding-agent/ro-intermediate-ancestor.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Selected actual RO2216 rows complete the inherited role chain. |
| metpo-primary | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/repo/data/raw/metpo.owl; Actual selected METPO XML | supports | Active broader pressure terms and obsolete replacements do not establish an exact current breadth replacement; local v5 separately sourced. |
| ro-primary | /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/ro.db; Actual RO2327,2215,2500,2595 rows; intermediate2216 separately bound | supports | RO2327 inherits material executor to process roles through 2215,2216,2500,2595. |
| pato-primary | /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/pato.db; Actual PATO0001025 rows | supports | Pressure physical quality supports the declared ambient condition identity; no process event inferred. |
| proposal-v5-primary | proposals/metpo_traitmech_v5/metpo_proposal_classes_robot.tsv; Captured TSV row 8 | supports | Proposed 1007605 lifts the fallback breadth concept; not an active imported replacement. |
| proposal-v4-primary | proposals/metpo_traitmech_v4/metpo_proposal_properties_robot.tsv; Captured TSV row 3 | supports | Defines permits a measurement axis or feature to parameterize a numerical trait, with broad formal endpoints. |
| taxon-colwellia | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-grounding-agent/taxon1513592.xml; Whole official taxonomy response; original successful request time | supports | Official Colwellia marinimaniae species and MTCD1 aliases positive; phenotype separately sourced. |
| meta-membrane | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/membrane-metadata.json; Actual retained indexed metadata/abstract; original request time | supports | Actual review abstract describes non-universal lipid responses and pressure/temperature context; selected body separately bound. |
| meta-colwellia | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/colwellia-metadata.json; Actual retained indexed metadata/abstract; original request time | supports | Actual primary abstract supports MTCD1 80–140 MPa range and optimum 120 MPa at 6 °C; derived breadth is 60 MPa. |
| body-membrane | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/membrane.xml; Selected actual JATS paragraphs; definition at zero-based paragraph 1 | supports | Literal pressure-adaptation phrase and generic lipid context; preference/tolerance and taxon exceptions retained. |
| meta-genomes | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/genomes-metadata.json; Actual fresh indexed response; bounded metadata scope | supports | Actual comparative Colwellia study abstract and source identity; Preprint in is a preprint link, not a correction/retraction finding. |
| meta-chemrev | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/chemrev-metadata.json; Actual fresh indexed response; bounded metadata scope | supports | Actual review identity/abstract; author-deposited manuscript text is separately bound. |
| meta-physiology | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/physiology-metadata.json; Actual fresh indexed response; bounded metadata scope | supports | Actual source identity/status only; detailed pressure-training, survival, defense, transcriptomic effects and methods are UNASSESSED_SCOPE. |
| meta-bounds | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/bounds-metadata.json; Actual fresh indexed response; bounded metadata scope | context_only | Successful indexed request returned zero hits; identity resolved separately by actual Crossref response. |
| bounds-crossref | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/bounds-crossref.json; Actual successful Crossref identity/status response | supports | Assigned Nature work identity resolved; no full-text support inferred from metadata. |
| body-genomes | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/genomes.xml; Actual JATS zero-based paragraphs 2,15,16,26 and first three sentences of 27 | supports | Canonical interval positive; desaturase statement is scoped to comparative Colwellia cohort; nuo hypothesis remains explicitly conditional. |
| body-physiology | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/physiology.xml; Actual Introduction zero-based paragraph 3, first two generic physical sentences only | supports | Generic pressure/fluidity background supports contextual wording; detailed biological efficacy/methods excluded. |
| body-chemrev | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/chemrev.pdf; HAL author-deposited manuscript; cover DOI/title and selected generic membrane/osmolyte passages | supports | Generic physical context positive. Author-deposited version, not asserted to be the publisher-formatted final body. |
| chemrev-text | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/chemrev.txt; Derived PDF text; newline-only lines 288–308,400–419,945–999; Python splitlines differs because of formfeed | supports | Text extraction of the bound author manuscript; locator convention explicit, not an independent primary acquisition. |
| sources | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/source-assessment.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Final six-work source audit; bounded attribution and snippet-format minors only. |
| source-ledger | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/source-ledger.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | All six identities and distinct abstract/body reading scopes. |
| placements | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/placement-ledger.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | All fifteen external placements and nine grounding fields accounted for. |
| snippets | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/snippet-ledger.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | One literal phrase and one supported unit transcription; numbers preserved. |
| node-sources | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/node-source-ledger.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | All twelve source node contexts. |
| edge-sources | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/edge-source-ledger.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | All ten source edge contexts, scope exclusions and qualified inferences. |
| source-status | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/publication-status-ledger.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Actual returned publication-status fields; bounded history checks. |
| source-reading | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/selected-primary-reading.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Actual selected reading scopes; incidental excluded content not adopted. |
| source-access | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/access-limitations.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Colwellia body not acquired/inspected; Nature later HTTP500 and PDF403 failures retained. |
| source-reuse | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/source-reuse-receipt.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Original metadata/body acquisitions and current 21:19:31 copies remain distinct. |
| canonical-scope | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/canonical-assessment.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Positive strain/temperature-specific 80–140 interval gives derived breadth 60 MPa. |
| native-checks | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/native-check-context.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Native/strict pass and initial snippet DNS failure followed by successful retry. |
| source-capture | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/final-capture-verification.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | All 64 captured inputs unchanged. |
| source-manifest | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/evidence-manifest.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Forty-three frozen source artifacts verified. |
| bounds-observation | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/bounds-selected-browser-observation.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Derived transcription of original successful selected publisher text; exact first access time uninstrumented. Receipt hash is not raw HTML/body hash; later failed access is separate. |
| bounds-later-failure | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/bounds-browser-response.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Retained later failed browser reread/export, not the positive original source observation. |
| root-reading-83 | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-root/additional-primary-reading.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Only actual bounded root reading/observation scope; receipt hash is not an article-body hash. |
| root-reading-84 | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-root/biolink-primary-reading.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Only actual bounded root reading/observation scope; receipt hash is not an article-body hash. |
| root-reading-85 | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-root/bounds-root-web-access-failure.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Only actual bounded root reading/observation scope; receipt hash is not an article-body hash. |
| root-reading-86 | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-root/chemrev-primary-reading-corrected.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Only actual bounded root reading/observation scope; receipt hash is not an article-body hash. |
| root-reading-87 | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-root/definition-canonical-primary-reading.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Only actual bounded root reading/observation scope; receipt hash is not an article-body hash. |
| root-reading-88 | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-root/final-evidence-reading-attestation.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Only actual bounded root reading/observation scope; receipt hash is not an article-body hash. |
| root-reading-89 | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-root/frozen-audits-verification.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Only actual bounded root reading/observation scope; receipt hash is not an article-body hash. |
| root-reading-90 | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-root/graph-structure-reading.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Only actual bounded root reading/observation scope; receipt hash is not an article-body hash. |
| root-reading-91 | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-root/identity-primary-reading.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Only actual bounded root reading/observation scope; receipt hash is not an article-body hash. |
| root-reading-92 | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-root/metpo-primary-reading-corrected.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Only actual bounded root reading/observation scope; receipt hash is not an article-body hash. |
| root-reading-93 | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-root/physiology-and-bounds-reading.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Only actual bounded root reading/observation scope; receipt hash is not an article-body hash. |
| root-reading-94 | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-root/ro-primary-reading.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Only actual bounded root reading/observation scope; receipt hash is not an article-body hash. |
| root-reading-95 | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-root/root-reading-attestation.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Only actual bounded root reading/observation scope; receipt hash is not an article-body hash. |
| root-reading-96 | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-root/taxonomy-primary-reading.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Only actual bounded root reading/observation scope; receipt hash is not an article-body hash. |
| challenge | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-semantic-challenge-agent/semantic-severity-challenge.json; Final independent challenge | supports | Exact fields, disposition and bindings verified. |
| adjudication | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-root-adjudication.json; Final root disposition | supports | Final findings and nonfindings control serialization. |

## Limits And Additional Notes

- Detailed pathogen pressure-defense, fitness, AMR, survival training, intervention efficacy and methods are UNASSESSED_SCOPE; incidental displayed content is not adopted.
- The canonical 60 MPa is derived arithmetic from an explicitly reported 80–140 MPa interval at 6 °C; source need not coin pressure delta, and optimum 120 MPa is distinct.
- Colwellia primary body was not acquired/inspected; its indexed abstract directly supports the canonical observation. No fresh failed primary-body request or paper-wide absence is claimed.
- Nature selected text is represented by a derived transcription receipt, not retained raw HTML. The original successful browser access time was not instrumented; later failed HTTP500 reread and PDF403 attempts remain explicit. Root read the receipt, not raw publisher HTML.
- ChemRev is an author-deposited manuscript with verified title/DOI; selected generic physical context and derived PDF text are distinguished from a publisher-formatted final body. Newline locators differ from Python splitlines because of PDF formfeeds.
- Community respiration observations do not independently calibrate every species growth bound. Conditional nuo energy contribution and generic source inference remain limitations rather than added findings.
- Retained metadata acquisition was 20:42:51 and membrane body acquisition 16:07:33–35; copies at 21:19:31 are distinct from fresh metadata 21:17:30–31 and body requests starting 21:17:49. Official taxonomy retains original successful 16:11:19–20 acquisition and prior DNS failure.
- Fallback/proposed 1007605 is not an imported active replacement. Four contextual components and a reviewed label-only protein aggregate do not require speculative connectors or instances.
- Actual prior QC, current qualification and local initialization do not assert B11 remote publication; publication remains separately documented.
- Final root adjudication and independent challenge are pinned and verified; preparation does not import or execute the serializer. Root owns subsequent execution, validation and save.
- Coverage: six works/six forms, fifteen external placements, nine grounding fields, twelve nodes/ten edges, one canonical, two snippets: one literal and one supported unit transcription.
- No scientific record, native inventory, Git or sweep-state mutation by serializer preparation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T212815Z-pressure-delta
kind: record
repository: CultureBotAI/TraitMech
title: Whole-record review of pressure delta
started_at: '2026-10-21T21:16:57.952674Z'
finished_at: '2026-10-21T21:28:15Z'
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
summary: 'Final root disposition: one formal-role major and four bounded description,
  attribution, literal-format and human-acceptance minors.'
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
  - path: data/traits/environment/pressure_delta.yaml
    sha256: 6fd90cd9c1f1e1404a2fbf6cb0a0462582c0075ee255cb27b4d5d26320077f52
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
  - path: history/infrastructure/disposition-typing-burndown/2026-08-08T060908Z-claude-code-f802c8.yaml
    sha256: 8ede4f80f46395efb74643e1f4158975a119ffaec78b5b291f0fc3a520a11c59
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
  - path: research/traits/environment/pressure_delta-deep-research-falcon.md
    sha256: 85a621a42f5ffe966fbcf65a53d2008502bf92e931970e0e5240d478e0be3cab
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/add_cell_body_contraction_trait.py
    sha256: 9b3d4fa868124764410a5d47145a2398ed0e1fa2c61ca5463f1695839e0b7c8f
    role: context
  - path: scripts/add_cellular_contraction_trait.py
    sha256: e924e40ae9145b59f7e6ec4a43c337ff64cf118c0b6f621abb83c4ceb98be5ee
    role: context
  - path: scripts/add_ds_26_system_trait.py
    sha256: 05f2d677ef69e8648d125fc03f0fab9f126d38e23b13db35df47060bc3c45d69
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
  - path: scripts/connect_temperature_range_very_low_graph_183.py
    sha256: 71755acb7ce3311fd473c8bef9a71dfed5fc6b8089b79cf33ea95cd5d1dad0a1
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
  - path: scripts/review_obligately_piezophilic_graph_183.py
    sha256: d8fcbbb725162212cfce96bed9800e2cf08374170b7d929a1928248178111efb
    role: context
  - path: scripts/review_temperature_range_very_low_graph_183.py
    sha256: 4a48e54f1e448c2a4f67088cce8ecfe248f81034faf7271ab272e45e9e2541d4
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
- target_id: traitmech:000006
  path: data/traits/environment/pressure_delta.yaml
  label: pressure delta
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/pressure_delta.yaml
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
  selection: Second record of the actual locally initialized batch 012 queue. Whole
    247-line target and all 64 captured inputs verified before assessment. Local initialization
    at 21:02:18.445284 UTC does not assert publication of batch 011.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - traitmech:000006
checks:
- check_id: audit-graphs
  name: Full-corpus graph audit
  status: passed
  required: true
  target_ids:
  - traitmech:000006
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
  - traitmech:000006
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
  - traitmech:000006
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
  - traitmech:000006
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
  - traitmech:000006
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
  - traitmech:000006
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
  - traitmech:000006
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
- check_id: pressure-delta-native
  name: Focused native validation
  status: passed
  required: true
  target_ids:
  - traitmech:000006
  command: just validate data/traits/environment/pressure_delta.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Successful schema validation; source and semantics separately assessed.
  evidence_ids:
  - check-pressure-delta-native
- check_id: pressure-delta-strict
  name: Focused strict validation
  status: passed
  required: true
  target_ids:
  - traitmech:000006
  command: just validate-strict data/traits/environment/pressure_delta.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Successful strict validation; no biological efficacy certification.
  evidence_ids:
  - check-pressure-delta-strict
- check_id: pressure-delta-snippets
  name: Initial focused snippet attempt
  status: failed
  required: false
  target_ids:
  - traitmech:000006
  command: just verify-snippets --record data/traits/environment/pressure_delta.yaml
    --out /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-snippets.tsv
  exit_code: 2
  expected_exit_code: 0
  summary: DNS failure, exit 2, retained separately from successful network retry;
    no completed-review failure inferred.
  evidence_ids:
  - check-pressure-delta-snippets
- check_id: pressure-delta-snippets-retry-network
  name: Focused snippet network retry
  status: passed
  required: true
  target_ids:
  - traitmech:000006
  command: just verify-snippets --record data/traits/environment/pressure_delta.yaml
    --out /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-snippets-retry-network.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 'Two fields over two references: both NOT_IN_ABSTRACT. Actual membrane
    body verifies first literally; Colwellia abstract supports second after explicit
    unit transcription.'
  evidence_ids:
  - check-pressure-delta-snippets-retry-network
- check_id: batch011-qc
  name: Reused maintained batch-eleven QC
  status: passed
  required: true
  target_ids:
  - traitmech:000006
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
  - traitmech:000006
  summary: One reviewed label-only Complex I aggregate, zero instances; no forced
    UniProt accession or detailed pressure-response query.
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
- evidence_id: check-pressure-delta-native
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-native.log
  locator: Executed 2026-10-21T21:17:20.030558+00:00 through 2026-10-21T21:17:20.546728+00:00;
    metadata pressure-delta-native.json
  accessed_at: '2026-10-21T21:17:20.546728Z'
  support: context_only
  summary: Successful schema validation; source and semantics separately assessed.
  snapshot_sha256: c4f2302651a626c4e5bfce8d079feff92d0ed12a4d230eea6f742b662c990226
- evidence_id: check-pressure-delta-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-strict.log
  locator: Executed 2026-10-21T21:17:20.030424+00:00 through 2026-10-21T21:17:20.899084+00:00;
    metadata pressure-delta-strict.json
  accessed_at: '2026-10-21T21:17:20.899084Z'
  support: context_only
  summary: Successful strict validation; no biological efficacy certification.
  snapshot_sha256: 1ef6b62183fd717465cf6c892527b7624cff4c5e41dd17e1942764525824a99c
- evidence_id: check-pressure-delta-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-snippets.log
  locator: Executed 2026-10-21T21:17:20.031650+00:00 through 2026-10-21T21:17:34.152174+00:00;
    metadata pressure-delta-snippets.json
  accessed_at: '2026-10-21T21:17:34.152174Z'
  support: context_only
  summary: DNS failure, exit 2, retained separately from successful network retry;
    no completed-review failure inferred.
  snapshot_sha256: 95a03ece51ece658470431bbd497336ffa8ead1e86a0fcde572dde551ff2f784
- evidence_id: check-pressure-delta-snippets-retry-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-snippets-retry-network.log
  locator: Executed 2026-10-21T21:17:46.041110+00:00 through 2026-10-21T21:17:49.454967+00:00;
    metadata pressure-delta-snippets-retry-network.json
  accessed_at: '2026-10-21T21:17:49.454967Z'
  support: context_only
  summary: 'Two fields over two references: both NOT_IN_ABSTRACT. Actual membrane
    body verifies first literally; Colwellia abstract supports second after explicit
    unit transcription.'
  snapshot_sha256: 0b5c3f67d458cb5c70d546b5a5c8f5d2f4c6410855a0ac0d40f338f4c10f81b5
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
  reference: data/traits/environment/pressure_delta.yaml
  locator: Entire current 247-line record
  accessed_at: '2026-10-21T21:16:58.524937Z'
  support: supports
  summary: Twelve nodes, ten edges, two snippets, one canonical and seven AI events
    covered.
  snapshot_sha256: 6fd90cd9c1f1e1404a2fbf6cb0a0462582c0075ee255cb27b4d5d26320077f52
- evidence_id: policy
  kind: authority
  reference: docs/GROUNDING_POLICY.md
  locator: Captured maintained authority
  accessed_at: '2026-10-21T21:21:11.697900Z'
  support: supports
  summary: Referent-based formal roles and permitted reviewed protein aggregate.
  snapshot_sha256: 891678c983c2283a47c81c47950b35753981e9339d105f3bbdda92a1f5ab7f42
- evidence_id: playbook
  kind: authority
  reference: docs/CURATION_PLAYBOOK.md
  locator: Captured maintained authority
  accessed_at: '2026-10-21T21:21:11.697900Z'
  support: supports
  summary: Source scope, literal copied snippets and attributable acceptance.
  snapshot_sha256: 735e9b810471da9f7d8364e35ffe1e741edb3421480dac01727db6ea5aa65da9
- evidence_id: schema
  kind: authority
  reference: src/traitmech/schema/traitmech.yaml
  locator: Captured maintained authority
  accessed_at: '2026-10-21T21:21:11.697900Z'
  support: supports
  summary: Current node facets and review contract.
  snapshot_sha256: 46c47fc627b80ccbba1e8ab3fb6f2aee93bc2aef7aaf72fe9aadc3257f2c02dd
- evidence_id: checklist
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Captured maintained authority
  accessed_at: '2026-10-21T21:21:11.697900Z'
  support: supports
  summary: Whole-record identity, evidence, graph, provenance and readiness checks.
  snapshot_sha256: da8896328a0fd6cc92f1adf0d8be8980d0ddd41f3172c7936f2c7f119b293ac1
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
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-grounding-agent/capture-verification.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:18:56.963407Z'
  support: supports
  summary: All 64 inputs verified before grounding assessment.
  snapshot_sha256: a762b6ce7a3bafd1cf7e7a777d81cc4433e702ff76204129e1448a23ecb48c85
- evidence_id: identity
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-grounding-agent/identity-assessment.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:21:11.696382Z'
  support: supports
  summary: Retained fallback denotes a derived breadth, distinct from tolerance and
    preference.
  snapshot_sha256: df9e6a9695acf62be9c9a3e32f3b268c5e7739850c2ec0b932ca4234b0050317
- evidence_id: node-edges
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-grounding-agent/node-edge-ledger.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:21:11.696728Z'
  support: supports
  summary: All twelve nodes/ten edges and four components; imported roles separate
    from biological efficacy.
  snapshot_sha256: 50d1be73418868eaa470e623c69dacd661453ec41207f4c1967439a3977c8c93
- evidence_id: owners
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-grounding-agent/owner-provenance-assessment.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:21:11.697219Z'
  support: supports
  summary: Current/shared owners and guarded historical context; bounded human search.
  snapshot_sha256: 54972e297b060bd73582531f6b1caf05550f1a8fddd5ecb1f825af5c38bc0203
- evidence_id: expression
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-grounding-agent/expression-and-readiness-assessment.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:21:11.697617Z'
  support: supports
  summary: Canonical catalog applicability and contextual protein disposition.
  snapshot_sha256: e799f194fb02501d4b228e3c6caa1dce32b9184dd08bd6f2cdff6911c252b25a
- evidence_id: catalog-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-grounding-agent/catalog-reuse-receipt.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:19:07.900651Z'
  support: supports
  summary: Original catalog and runner receipts separate from current copies.
  snapshot_sha256: 698a695cf50ac6147722123c8b04ea748d1cf0dd0a5b6e7dde504cddb5d43649
- evidence_id: local-authority
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-grounding-agent/local-authority-excerpts.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:21:11.691929Z'
  support: supports
  summary: Exact v5/v4 proposals, maintained mappings, schema and Biolink.
  snapshot_sha256: a4c769ed9b719810dde0f84db9910a121d6c6af804b316ff0cda6235fefe0880
- evidence_id: ground-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-grounding-agent/reading-scope-receipt.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:21:11.698036Z'
  support: supports
  summary: Actual selected primary/owner readings and one whole context history, not
    direct target approval.
  snapshot_sha256: 71f2dc1f63fe80b44d8bf008fbe51fe9f0f715c372d6ea6305ab2cfeacc18881
- evidence_id: ground-manifest
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-grounding-agent/evidence-manifest.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:21:33.233158Z'
  support: supports
  summary: Frozen 28 grounding artifacts verified.
  snapshot_sha256: fba15484307e9c396e9969a756cbe6b16902989888f22046a0af88eb14b84ca8
- evidence_id: taxon-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-grounding-agent/taxonomy-reuse-receipt.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:19:07.899496Z'
  support: supports
  summary: Original Colwellia request and retained initial DNS failure separate from
    current copies.
  snapshot_sha256: 890b1533b43a130ed5366c708a3ef85bf6ae839c5fdccccbde543f1bb07a4dfc
- evidence_id: ro-intermediate
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-grounding-agent/ro-intermediate-ancestor.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:21:11.460026Z'
  support: supports
  summary: Selected actual RO2216 rows complete the inherited role chain.
  snapshot_sha256: 96e3f0d57702c37944d0d9f00ecc1bf2d7893840483675893c37b82178899e2c
- evidence_id: metpo-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/repo/data/raw/metpo.owl
  locator: Actual selected METPO XML
  accessed_at: '2026-10-21T21:18:57.082162Z'
  support: supports
  summary: Active broader pressure terms and obsolete replacements do not establish
    an exact current breadth replacement; local v5 separately sourced.
  snapshot_sha256: 8b6f8fe0510a698579e532658c8ace05da2550093365df9ca83feb0741778415
- evidence_id: ro-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/ro.db
  locator: Actual RO2327,2215,2500,2595 rows; intermediate2216 separately bound
  accessed_at: '2026-10-21T21:18:56.966097Z'
  support: supports
  summary: RO2327 inherits material executor to process roles through 2215,2216,2500,2595.
  snapshot_sha256: 849e616c29fecd0d4a6c6dee0dc0f6f117ace7167dbfa1e0f043dc84868f83cb
- evidence_id: pato-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/pato.db
  locator: Actual PATO0001025 rows
  accessed_at: '2026-10-21T21:18:56.969564Z'
  support: supports
  summary: Pressure physical quality supports the declared ambient condition identity;
    no process event inferred.
  snapshot_sha256: 179ab512b5c3a8827c74e2a496da575e2908a84740429deef265d58c9ce61d3b
- evidence_id: proposal-v5-primary
  kind: authority
  reference: proposals/metpo_traitmech_v5/metpo_proposal_classes_robot.tsv
  locator: Captured TSV row 8
  accessed_at: '2026-10-21T21:21:11.691929Z'
  support: supports
  summary: Proposed 1007605 lifts the fallback breadth concept; not an active imported
    replacement.
  snapshot_sha256: d4b899de7077b33f4bdc6cb8cdebf28b5a705b7a65ba3620f3113b76d8666910
- evidence_id: proposal-v4-primary
  kind: authority
  reference: proposals/metpo_traitmech_v4/metpo_proposal_properties_robot.tsv
  locator: Captured TSV row 3
  accessed_at: '2026-10-21T21:21:11.691929Z'
  support: supports
  summary: Defines permits a measurement axis or feature to parameterize a numerical
    trait, with broad formal endpoints.
  snapshot_sha256: 55a96748c50b60ba0622170ef0eb09833f6d1e59431a4ab32b6fcb079103c0b7
- evidence_id: taxon-colwellia
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-grounding-agent/taxon1513592.xml
  locator: Whole official taxonomy response; original successful request time
  accessed_at: '2026-10-21T16:11:20.071001Z'
  support: supports
  summary: Official Colwellia marinimaniae species and MTCD1 aliases positive; phenotype
    separately sourced.
  snapshot_sha256: 44883620d8bdc159d01e53d74afc493e730bac233c92303887b704c10061050e
- evidence_id: meta-membrane
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/membrane-metadata.json
  locator: Actual retained indexed metadata/abstract; original request time
  accessed_at: '2026-10-21T20:42:51.668312Z'
  support: supports
  summary: Actual review abstract describes non-universal lipid responses and pressure/temperature
    context; selected body separately bound.
  snapshot_sha256: 60b0dd82b02eddbe01f9944f485da11c5ea9e55ec36f65b501a3a78ba9b1e9b3
- evidence_id: meta-colwellia
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/colwellia-metadata.json
  locator: Actual retained indexed metadata/abstract; original request time
  accessed_at: '2026-10-21T20:42:51.694246Z'
  support: supports
  summary: Actual primary abstract supports MTCD1 80–140 MPa range and optimum 120
    MPa at 6 °C; derived breadth is 60 MPa.
  snapshot_sha256: e74a6f54136e6dcd2ab87b38d86de68e793d0dc28218b87b9f2bbd3ccd4103d2
- evidence_id: body-membrane
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/membrane.xml
  locator: Selected actual JATS paragraphs; definition at zero-based paragraph 1
  accessed_at: '2026-10-21T16:07:35.045859Z'
  support: supports
  summary: Literal pressure-adaptation phrase and generic lipid context; preference/tolerance
    and taxon exceptions retained.
  snapshot_sha256: d8320b3073b404cd79da19795d94f02477ce8a34accb22809294e05d1e72c032
- evidence_id: meta-genomes
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/genomes-metadata.json
  locator: Actual fresh indexed response; bounded metadata scope
  accessed_at: '2026-10-21T21:17:31.045859Z'
  support: supports
  summary: Actual comparative Colwellia study abstract and source identity; Preprint
    in is a preprint link, not a correction/retraction finding.
  snapshot_sha256: 24367006816b135c1f174cbb038e4653b50caa31cd32b44709765d7698e86438
- evidence_id: meta-chemrev
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/chemrev-metadata.json
  locator: Actual fresh indexed response; bounded metadata scope
  accessed_at: '2026-10-21T21:17:31.023274Z'
  support: supports
  summary: Actual review identity/abstract; author-deposited manuscript text is separately
    bound.
  snapshot_sha256: bd1f7380dbde15a025a6d0a85b194f7d430791fdbe0458577fc858dc06de6111
- evidence_id: meta-physiology
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/physiology-metadata.json
  locator: Actual fresh indexed response; bounded metadata scope
  accessed_at: '2026-10-21T21:17:31.029739Z'
  support: supports
  summary: Actual source identity/status only; detailed pressure-training, survival,
    defense, transcriptomic effects and methods are UNASSESSED_SCOPE.
  snapshot_sha256: 766c4057a9a9414c99da4829c4c8ea37a6299d0111020df215974235315ab957
- evidence_id: meta-bounds
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/bounds-metadata.json
  locator: Actual fresh indexed response; bounded metadata scope
  accessed_at: '2026-10-21T21:17:31.005205Z'
  support: context_only
  summary: Successful indexed request returned zero hits; identity resolved separately
    by actual Crossref response.
  snapshot_sha256: f266ad94f98c3c69a9126c9ca91dd7ee3bb0d5537b46001fbf6747da3cbbe277
- evidence_id: bounds-crossref
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/bounds-crossref.json
  locator: Actual successful Crossref identity/status response
  accessed_at: '2026-10-21T21:17:49.600955Z'
  support: supports
  summary: Assigned Nature work identity resolved; no full-text support inferred from
    metadata.
  snapshot_sha256: ff2c29277843971342c6b5ccaf11396e88e403b50051eec78777b339eec9ee94
- evidence_id: body-genomes
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/genomes.xml
  locator: Actual JATS zero-based paragraphs 2,15,16,26 and first three sentences
    of 27
  accessed_at: '2026-10-21T21:17:50.586975Z'
  support: supports
  summary: Canonical interval positive; desaturase statement is scoped to comparative
    Colwellia cohort; nuo hypothesis remains explicitly conditional.
  snapshot_sha256: 825e85cb67ca727a14e9efc327571859646ed867e22c494eafaef0ce2d8e66d3
- evidence_id: body-physiology
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/physiology.xml
  locator: Actual Introduction zero-based paragraph 3, first two generic physical
    sentences only
  accessed_at: '2026-10-21T21:17:50.453112Z'
  support: supports
  summary: Generic pressure/fluidity background supports contextual wording; detailed
    biological efficacy/methods excluded.
  snapshot_sha256: f66a71424aab1edf641bd20a6bad748dff74976247a37043d12ebd447193290a
- evidence_id: body-chemrev
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/chemrev.pdf
  locator: HAL author-deposited manuscript; cover DOI/title and selected generic membrane/osmolyte
    passages
  accessed_at: '2026-10-21T21:17:59.961010Z'
  support: supports
  summary: Generic physical context positive. Author-deposited version, not asserted
    to be the publisher-formatted final body.
  snapshot_sha256: cbdde27b2d4a5f88f8cec3378c6f86f6438088e8e1d5a72d6e0bbdd8b3099590
- evidence_id: chemrev-text
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/chemrev.txt
  locator: Derived PDF text; newline-only lines 288–308,400–419,945–999; Python splitlines
    differs because of formfeed
  accessed_at: '2026-10-21T21:21:25.542113Z'
  support: supports
  summary: Text extraction of the bound author manuscript; locator convention explicit,
    not an independent primary acquisition.
  snapshot_sha256: e3e7bdc27d15d7540781b3e419676580f53aa7bce21cdd091d47dee86449328e
- evidence_id: sources
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/source-assessment.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:21:25.547573Z'
  support: supports
  summary: Final six-work source audit; bounded attribution and snippet-format minors
    only.
  snapshot_sha256: 8a24c0e2a6dec03656fc96234851617d7076240930101fa555b7c83243cc8eff
- evidence_id: source-ledger
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/source-ledger.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:21:25.537841Z'
  support: supports
  summary: All six identities and distinct abstract/body reading scopes.
  snapshot_sha256: 900daff599e1df747e8621cf5ebaf121f25326b73fd61e1d8e61d31e60f449d2
- evidence_id: placements
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/placement-ledger.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:21:25.538217Z'
  support: supports
  summary: All fifteen external placements and nine grounding fields accounted for.
  snapshot_sha256: 245a71201812cc7f569b07a6c986630d1964a831f6543abf55cda04657d42096
- evidence_id: snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/snippet-ledger.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:21:25.540342Z'
  support: supports
  summary: One literal phrase and one supported unit transcription; numbers preserved.
  snapshot_sha256: ecf690b3665f50a688f6e1ff59aa3d4d7e00b2073ed78f3e2a52585dae28f78a
- evidence_id: node-sources
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/node-source-ledger.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:21:25.538437Z'
  support: supports
  summary: All twelve source node contexts.
  snapshot_sha256: 7c59fc018ac3e3425ff40a29852450e1a3edd0245bf257f589113db5dbf1ffaa
- evidence_id: edge-sources
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/edge-source-ledger.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:21:25.538320Z'
  support: supports
  summary: All ten source edge contexts, scope exclusions and qualified inferences.
  snapshot_sha256: 6e16ec734c967bab1b1896d125dedb80353d6f27599d90be70bf00b0a7f4b710
- evidence_id: source-status
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/publication-status-ledger.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:21:25.538102Z'
  support: supports
  summary: Actual returned publication-status fields; bounded history checks.
  snapshot_sha256: 3902d168a700b503176c4e89c2ab29f4d6a1d47c5f36f471d380e1744ec12432
- evidence_id: source-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/selected-primary-reading.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:21:25.542113Z'
  support: supports
  summary: Actual selected reading scopes; incidental excluded content not adopted.
  snapshot_sha256: 82a320b93f6f65ccc329bcc292ee004eadf8c587c89d927135464e54f60476c9
- evidence_id: source-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/access-limitations.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:21:25.545895Z'
  support: supports
  summary: Colwellia body not acquired/inspected; Nature later HTTP500 and PDF403
    failures retained.
  snapshot_sha256: d7b1f3aa440e5eefa9ea280d5cb65cb9b571bae8bc0d36fab96abddcf3cf6b12
- evidence_id: source-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/source-reuse-receipt.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:19:31.529368Z'
  support: supports
  summary: Original metadata/body acquisitions and current 21:19:31 copies remain
    distinct.
  snapshot_sha256: 05dc59909bee0a08bb3b243d1b4f0e6bffe0e971771486a061572915bf07df7d
- evidence_id: canonical-scope
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/canonical-assessment.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:21:25.540493Z'
  support: supports
  summary: Positive strain/temperature-specific 80–140 interval gives derived breadth
    60 MPa.
  snapshot_sha256: dfa75586545fde1d663f15e6a67d5755e094744ec131a40dc62cc2079ac2edf8
- evidence_id: native-checks
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/native-check-context.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:21:25.545791Z'
  support: supports
  summary: Native/strict pass and initial snippet DNS failure followed by successful
    retry.
  snapshot_sha256: e8f4561177e77abfdf08c5eaafe6dad0b3d6c7db75da753289aaf9775806eeeb
- evidence_id: source-capture
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/final-capture-verification.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:21:25.547716Z'
  support: supports
  summary: All 64 captured inputs unchanged.
  snapshot_sha256: 7b60b727537938f5a9273c5729f213ad61646cb6cfc9a7a988bb68dea601d4ff
- evidence_id: source-manifest
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/evidence-manifest.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:21:25.554747Z'
  support: supports
  summary: Forty-three frozen source artifacts verified.
  snapshot_sha256: 4bde73b97f20f825a78b15f17ff2fc822a09a999717a83a1c79dd3f88088f970
- evidence_id: bounds-observation
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/bounds-selected-browser-observation.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:20:10.204586Z'
  support: supports
  summary: Derived transcription of original successful selected publisher text; exact
    first access time uninstrumented. Receipt hash is not raw HTML/body hash; later
    failed access is separate.
  snapshot_sha256: 9a20d1e8ac7341b8484ba731a62fe2e89d811eeb80368d87d5f039a5a6bcaf5c
- evidence_id: bounds-later-failure
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-agent/bounds-browser-response.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:19:49Z'
  support: supports
  summary: Retained later failed browser reread/export, not the positive original
    source observation.
  snapshot_sha256: 51a97313468cb87005f081b33dc13adc3cfbb0025ef8e2e6d95c0d8365972c75
- evidence_id: root-reading-83
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-root/additional-primary-reading.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:18:59.279675Z'
  support: supports
  summary: Only actual bounded root reading/observation scope; receipt hash is not
    an article-body hash.
  snapshot_sha256: e9646f2c1b0b73575fd1feb2f330643815b1ca471d018d62e696ebf677f49ac9
- evidence_id: root-reading-84
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-root/biolink-primary-reading.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:17:30.339336Z'
  support: supports
  summary: Only actual bounded root reading/observation scope; receipt hash is not
    an article-body hash.
  snapshot_sha256: baae39b77ff4be2e9c0bed648c0f9d283818cd79cd4c11d415abbe636c0440d5
- evidence_id: root-reading-85
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-root/bounds-root-web-access-failure.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:19:35.301628Z'
  support: supports
  summary: Only actual bounded root reading/observation scope; receipt hash is not
    an article-body hash.
  snapshot_sha256: 213141bcb22ed92b14e891433e4ea33960868f5a291b4b3e0a117d6fc61576ba
- evidence_id: root-reading-86
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-root/chemrev-primary-reading-corrected.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:19:35.301247Z'
  support: supports
  summary: Only actual bounded root reading/observation scope; receipt hash is not
    an article-body hash.
  snapshot_sha256: fe6a07fded1dffc8253292cdc4d876f0bcb001e37e7bb36a3a23fbc865ea102d
- evidence_id: root-reading-87
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-root/definition-canonical-primary-reading.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:17:37.852487Z'
  support: supports
  summary: Only actual bounded root reading/observation scope; receipt hash is not
    an article-body hash.
  snapshot_sha256: 8e8f8dbd674250a2724e3890268c72637d60df9f54ac7e8e61beb546decfccd4
- evidence_id: root-reading-88
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-root/final-evidence-reading-attestation.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:22:28.650555Z'
  support: supports
  summary: Only actual bounded root reading/observation scope; receipt hash is not
    an article-body hash.
  snapshot_sha256: 32f773bb9807152aaf6dd2af6498e6ba1a92459288c3bb1b769bb3e9ccdbdb63
- evidence_id: root-reading-89
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-root/frozen-audits-verification.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:22:07.670033Z'
  support: supports
  summary: Only actual bounded root reading/observation scope; receipt hash is not
    an article-body hash.
  snapshot_sha256: d4a44a7dd6438cf73848b61d1f6271fba4981a45259588bbf15abf1fdbb79908
- evidence_id: root-reading-90
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-root/graph-structure-reading.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:20:50.014593Z'
  support: supports
  summary: Only actual bounded root reading/observation scope; receipt hash is not
    an article-body hash.
  snapshot_sha256: 4d2fe29de947b9253ce164ac7bf1a90e245d6dc8aaa2441a6b7b504e6f5d9914
- evidence_id: root-reading-91
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-root/identity-primary-reading.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:18:15.316389Z'
  support: supports
  summary: Only actual bounded root reading/observation scope; receipt hash is not
    an article-body hash.
  snapshot_sha256: d149faa8bca4113390fbbd1e8a7b1a649cc93d1b95e6f21c6603b88c54c5f2fa
- evidence_id: root-reading-92
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-root/metpo-primary-reading-corrected.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:18:24.609800Z'
  support: supports
  summary: Only actual bounded root reading/observation scope; receipt hash is not
    an article-body hash.
  snapshot_sha256: 170cdf8468d4a7165171df0d0f07c3e4b5a4594cb575a627d2672ab96511b341
- evidence_id: root-reading-93
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-root/physiology-and-bounds-reading.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:20:50.017336Z'
  support: supports
  summary: Only actual bounded root reading/observation scope; receipt hash is not
    an article-body hash.
  snapshot_sha256: 037cf4983f1652f60d9f558a638d12be45874116eef0718baa207e05b17f3ee1
- evidence_id: root-reading-94
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-root/ro-primary-reading.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:17:30.141705Z'
  support: supports
  summary: Only actual bounded root reading/observation scope; receipt hash is not
    an article-body hash.
  snapshot_sha256: d8c532164f7f1f12e55cc0fb24b4137c9e68fe8e784d3eb7f65009eacc855261
- evidence_id: root-reading-95
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-root/root-reading-attestation.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:18:36.859167Z'
  support: supports
  summary: Only actual bounded root reading/observation scope; receipt hash is not
    an article-body hash.
  snapshot_sha256: 8a1d8f943d67d098dcad54601f9e2dbd98c28d460fd12f46e921100966320598
- evidence_id: root-reading-96
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-source-root/taxonomy-primary-reading.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:21:08.021765Z'
  support: supports
  summary: Only actual bounded root reading/observation scope; receipt hash is not
    an article-body hash.
  snapshot_sha256: 0b1e691906ca08bac0d1813e893e73b1f1abeb6f8b4a20481a251f1d10d2e35b
- evidence_id: challenge
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-semantic-challenge-agent/semantic-severity-challenge.json
  locator: Final independent challenge
  accessed_at: '2026-10-21T21:24:13.907934Z'
  support: supports
  summary: Exact fields, disposition and bindings verified.
  snapshot_sha256: e5ceed0ae35e8edb83dd8c8790502adfbc83c2e55f8549f3eda801df95242c75
- evidence_id: adjudication
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/pressure-delta-root-adjudication.json
  locator: Final root disposition
  accessed_at: '2026-10-21T21:24:50.096003Z'
  support: supports
  summary: Final findings and nonfindings control serialization.
  snapshot_sha256: 1ed0beda282189a5ab8ed4e409b907c90fe4c25164f1588da51b467e12870b20
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: derived pressure breadth'
  outcome: supported
  target_ids:
  - traitmech:000006
  summary: Retained traitmech:000006 denotes max minus min of a growth-supporting
    pressure interval, distinct from broader pressure tolerance/preference. Proposed
    1007605 is an exact local lift, not an installed active replacement.
  evidence_ids:
  - record
  - identity
  - metpo-primary
  - proposal-v5-primary
- assessment_id: definition
  area: evidence
  topic: 'Native checklist: measurement definition and source context'
  outcome: supported
  target_ids:
  - traitmech:000006
  summary: The operational breadth definition is coherent and illustrated by an explicitly
    reported interval. The membrane review supplies pressure-adaptation context; this
    audit does not claim that it coins the term pressure delta or establishes every
    generic mechanism as an exclusive breadth determinant.
  evidence_ids:
  - record
  - sources
  - body-membrane
  - meta-colwellia
  - canonical-scope
- assessment_id: hierarchy
  area: identity
  topic: 'Native checklist: parent and local defines authority'
  outcome: supported
  target_ids:
  - traitmech:000006
  summary: Active phenotype parent is appropriate. Local v4 defines admits an axis
    or growth-bound feature parameterizing a quantitative trait; broad local endpoints
    do not waive imported RO requirements.
  evidence_ids:
  - identity
  - metpo-primary
  - proposal-v4-primary
  - local-authority
- assessment_id: sources
  area: evidence
  topic: 'Native checklist: all assigned citations and placements'
  outcome: concern
  target_ids:
  - traitmech:000006
  summary: Six works and fifteen external placements accounted for. The comparative
    Colwellia desaturase statement is broadened in one note to all piezophiles; other
    contextual source inferences and unavailable bodies remain qualified limitations.
    Metadata, actual article files, author manuscript and derived browser receipt
    have separate provenance.
  evidence_ids:
  - source-ledger
  - placements
  - source-status
  - source-access
  - source-reuse
  - edge-sources
  - body-genomes
  - bounds-observation
- assessment_id: quotations
  area: evidence
  topic: 'Native checklist: literal unit-format fidelity'
  outcome: concern
  target_ids:
  - traitmech:000006
  summary: First snippet is literal in the assigned membrane body. Second supports
    all interval, optimum and temperature values after degrees C to °C normalization;
    only literal copied-span format differs. Native NOT_IN_ABSTRACT results remain
    unchanged.
  evidence_ids:
  - snippets
  - body-membrane
  - meta-colwellia
  - playbook
  - native-checks
- assessment_id: canonical
  area: evidence
  topic: 'Native checklist: measured interval and derived arithmetic'
  outcome: supported
  target_ids:
  - traitmech:000006
  summary: Colwellia marinimaniae MTCD1 grew over 80–140 MPa at 6 °C, giving 140 minus
    80 = 60 MPa. The optimum 120 MPa is a separate value. Assigned abstract and comparative
    article support this strain/temperature-specific observation; official species/type
    aliases are independently verified.
  evidence_ids:
  - canonical-scope
  - meta-colwellia
  - body-genomes
  - taxon-colwellia
- assessment_id: nodes
  area: consistency
  topic: 'Native checklist: all twelve current referents'
  outcome: concern
  target_ids:
  - traitmech:000006
  summary: Pressure condition, breadth/bounds qualities and explicitly named production,
    loss and maintenance processes are coherent. Node 9 label and reviewed aggregate
    denote protein Complex I, while its description calls it an operon; this is a
    bounded description precision issue, not a protein identity major or mandatory
    accession.
  evidence_ids:
  - node-edges
  - node-sources
  - schema
  - policy
  - pato-primary
  details: '[{"index": 0, "node": {"node_id": "pressure_delta_trait", "label": "pressure
    delta", "node_type": "TRAIT", "grounding": "traitmech:000006", "description":
    "Breadth (max − min) of the growth-supporting hydrostatic-pressure range."}, "assessment":
    "supported", "reason": "Self-grounded derived measurement trait, same max-minus-min
    identity as definition."}, {"index": 1, "node": {"node_id": "hydrostatic_pressure",
    "label": "hydrostatic pressure", "node_type": "ENVIRONMENTAL_FACTOR", "description":
    "Ambient hydrostatic pressure imposed on the cell.", "grounding": "PATO:0001025"},
    "assessment": "supported", "reason": "Ambient pressure condition has an explicit
    PATO physical-quality close match; current type permits environmental conditions."},
    {"index": 2, "node": {"node_id": "pressure_tolerance_breadth", "label": "pressure-tolerance
    breadth", "node_type": "QUALITY", "description": "Width of the hydrostatic-pressure
    interval over which growth is sustained."}, "assessment": "supported", "reason":
    "Width of a growth-supporting interval is a measurable quality, not an asserted
    process."}, {"index": 3, "node": {"node_id": "membrane_fluidity_maintenance",
    "label": "membrane fluidity maintenance under high pressure", "node_type": "BIOLOGICAL_PROCESS",
    "description": "Maintenance of adequate membrane fluidity against pressure-induced
    lipid compression."}, "assessment": "supported", "reason": "Maintenance is explicitly
    a biological process; no capacity/state retyping follows from its noun phrase."},
    {"index": 4, "node": {"node_id": "membrane_fluidity_loss", "label": "loss of membrane
    fluidity at high pressure", "node_type": "BIOLOGICAL_PROCESS", "description":
    "Pressure-induced reduction of membrane fluidity that impairs membrane function."},
    "assessment": "supported", "reason": "Loss/reduction denotes change, compatible
    with process representation; detailed biological efficacy unassessed."}, {"index":
    5, "node": {"node_id": "unsaturated_fatty_acid_production", "label": "unsaturated
    fatty acid production", "node_type": "BIOLOGICAL_PROCESS", "description": "Biosynthesis/desaturation
    generating unsaturated acyl chains that counter pressure-induced membrane ordering."},
    "assessment": "supported", "reason": "Biosynthesis/desaturation explicitly denotes
    a process. This supplies the subject-role conflict at edge 2, not a defect in
    this node type."}, {"index": 6, "node": {"node_id": "ribosome_dissociation", "label":
    "pressure-induced ribosome dissociation", "node_type": "BIOLOGICAL_PROCESS", "description":
    "High-pressure dissociation of ribosomes suppressing translation and growth."},
    "assessment": "supported", "reason": "Dissociation explicitly denotes a process;
    detailed pressure effects remain outside this formal audit."}, {"index": 7, "node":
    {"node_id": "compatible_solutes", "label": "intracellular osmolytes / compatible
    solutes", "node_type": "CHEMICAL", "description": "Cosolutes/osmolytes that stabilize
    protein structure under high hydrostatic pressure."}, "assessment": "supported",
    "reason": "Cosolutes are material chemical entities; no mandatory exact chemical
    accession is inferred for the broad collective label."}, {"index": 8, "node":
    {"node_id": "protein_stabilization_under_pressure", "label": "protein stabilization
    under pressure", "node_type": "BIOLOGICAL_PROCESS", "description": "Reinforcement
    of protein structure against pressure-induced perturbation."}, "assessment": "supported_with_qualification",
    "reason": "Stabilization is a process; direct chemical stabilization can fit executor
    semantics, with detailed efficacy unassessed."}, {"index": 9, "node": {"node_id":
    "nuo_complex_i", "label": "nuo NADH dehydrogenase I complex", "node_type": "GENE_OR_PROTEIN",
    "grounding_status": "REVIEWED_LABEL_ONLY", "grounding_notes": "Reviewed as a contextual
    protein or protein-complex label within a quantitative measurement graph; no exact
    semantic family term was established for this aggregate use.", "description":
    "Proton-translocating NADH dehydrogenase I (Complex I) operon enriched in piezophiles."},
    "assessment": "minor_precision", "reason": "Label, reviewed-label-only rationale
    and edge 8 identify a protein complex, but description explicitly calls that same
    referent an operon. Clarify the protein-complex description and keep operon information
    as metadata; not a gene-as-protein identity major or mandatory accession finding."},
    {"index": 10, "node": {"node_id": "high_pressure_energy_conservation", "label":
    "high-pressure respiratory energy conservation", "node_type": "BIOLOGICAL_PROCESS",
    "description": "Respiratory-chain energy conservation supporting growth under
    high hydrostatic pressure."}, "assessment": "supported", "reason": "Energy conservation
    is explicitly a process; detailed fitness effects unassessed."}, {"index": 11,
    "node": {"node_id": "min_max_growth_pressure_bounds", "label": "minimum and maximum
    growth pressure bounds", "node_type": "QUALITY", "description": "Lower and upper
    hydrostatic-pressure limits of growth whose difference defines the delta."}, "assessment":
    "supported", "reason": "Minimum and maximum growth bounds are measurable attributes
    defining a derived difference."}]'
- assessment_id: predicates
  area: consistency
  topic: 'Native checklist: all ten relation roles'
  outcome: concern
  target_ids:
  - traitmech:000006
  summary: RO2327 enables inherits material executor to process through 2327→2215→2216→2500→2595.
    Edge 2 instead has an explicit production-process subject. Edge 7 chemical-to-stabilization
    process has compatible roles and qualified direct stabilization meaning. Biolink
    broad endpoints, local defines and lexical restricts/supports are not assigned
    invented RO restrictions.
  evidence_ids:
  - node-edges
  - ro-primary
  - ro-intermediate
  - local-authority
  - owners
  - challenge
  - adjudication
  details: '[{"index": 0, "edge": {"subject": "hydrostatic_pressure", "predicate":
    "defines", "object": "pressure_delta_trait", "description": "The hydrostatic-pressure
    axis defines the values whose max minus min yields the delta.", "evidence": [{"reference":
    "DOI:10.3389/fmolb.2022.1058381", "notes": "Pressure-adaptation review frames
    the breadth of the pressure-tolerance span as a derived descriptor of pressure-adaptation
    flexibility."}], "predicate_id": "METPO:2007500"}, "assessment": "supported",
    "reason": "Local v4 defines explicitly admits a measurement axis parameterizing
    a numerical phenotype; no process-domain requirement."}, {"index": 1, "edge":
    {"subject": "pressure_delta_trait", "predicate": "associated with", "object":
    "pressure_tolerance_breadth", "description": "The delta encodes the breadth of
    pressure-tolerance flexibility.", "evidence": [{"reference": "DOI:10.1099/ijsem.0.001671",
    "notes": "The 80-140 MPa span of Colwellia marinimaniae MTCD1 (delta = 60 MPa)
    illustrates the breadth this phenotype records."}], "predicate_id": "biolink:associated_with"},
    "assessment": "supported_with_qualification", "reason": "Biolink association uses
    broad named-thing endpoints. The edge is definitional correspondence between the
    delta and its breadth facet, not a demonstrated causal execution relation; no
    new statistical mechanism claim is inferred."}, {"index": 2, "edge": {"subject":
    "unsaturated_fatty_acid_production", "predicate": "enables", "object": "membrane_fluidity_maintenance",
    "description": "Unsaturated acyl-chain production/desaturation sustains membrane
    fluidity under high hydrostatic pressure.", "evidence": [{"reference": "DOI:10.1186/s12864-020-07102-y",
    "notes": "All piezophiles encode a delta-9 acyl-phospholipid desaturase; unsaturated
    chains allow better adaptation to higher pressures (general HHP mechanism)."},
    {"reference": "DOI:10.1021/acs.chemrev.3c00432", "notes": "Membrane fluidity adjustment
    is a core pressure-adaptation node."}], "predicate_id": "RO:0002327"}, "assessment":
    "major", "reason": "RO2327 enables requires an executor capable of and executing
    a process. The full ancestor chain gives material entity to process. Subject node
    5 is expressly a biosynthetic/desaturation process, while object maintenance is
    a process. The production-process subject is the confirmed mismatch."}, {"index":
    3, "edge": {"subject": "hydrostatic_pressure", "predicate": "causes", "object":
    "membrane_fluidity_loss", "description": "High hydrostatic pressure compresses
    membranes and reduces fluidity.", "evidence": [{"reference": "DOI:10.3389/fmicb.2024.1293928",
    "notes": "High pressure causes loss of membrane fluidity (cross-taxa physiological
    mechanism)."}], "predicate_id": "biolink:causes"}, "assessment": "supported_formal_scope",
    "reason": "Current Biolink causes has broad named-thing ancestry and no inherited
    RO process-only endpoint restriction. A pressure quality subject is not automatically
    a role failure; source causality is assessed separately."}, {"index": 4, "edge":
    {"subject": "membrane_fluidity_loss", "predicate": "restricts", "object": "pressure_tolerance_breadth",
    "description": "Loss of membrane fluidity limits growth at the upper pressure
    bound, narrowing the supported range.", "evidence": [{"reference": "DOI:10.1038/s43247-023-01045-4",
    "notes": "Reduced membrane fluidity under HHP coincides with cessation of respiration/degradation,
    restricting the upper growth bound."}]}, "assessment": "lexical_only", "reason":
    "Ungrounded restricts asserts a qualitative limitation; no imported RO domain/range
    is imposed and no quantitative breadth effect is certified."}, {"index": 5, "edge":
    {"subject": "hydrostatic_pressure", "predicate": "causes", "object": "ribosome_dissociation",
    "description": "High pressure induces ribosome dissociation, suppressing translation
    and growth.", "evidence": [{"reference": "DOI:10.1038/s43247-023-01045-4", "notes":
    "High pressure causes ribosome dissociation; translation/replication become dysfunctional,
    preventing growth and division."}], "predicate_id": "biolink:causes"}, "assessment":
    "supported_formal_scope", "reason": "Current Biolink causes broad endpoints do
    not automatically exclude ambient pressure. Detailed pressure-induced ribosome
    biology remains unassessed."}, {"index": 6, "edge": {"subject": "ribosome_dissociation",
    "predicate": "restricts", "object": "pressure_tolerance_breadth", "description":
    "Translation failure from ribosome dissociation limits the growth-supporting pressure
    range.", "evidence": [{"reference": "DOI:10.1038/s43247-023-01045-4", "notes":
    "Ribosome dissociation preventing growth and division narrows the pressure range
    over which growth is sustained."}]}, "assessment": "lexical_only", "reason": "Ungrounded
    restricts has no imported process/material endpoint requirement; detailed biological
    effect remains unassessed."}, {"index": 7, "edge": {"subject": "compatible_solutes",
    "predicate": "enables", "object": "protein_stabilization_under_pressure", "description":
    "Intracellular osmolytes/cosolutes reinforce protein structure under high hydrostatic
    pressure.", "evidence": [{"reference": "DOI:10.1021/acs.chemrev.3c00432", "notes":
    "Osmolytes reinforce the structure of proteins; cosolutes modulate biomolecular
    function under HHP (general mechanism)."}], "predicate_id": "RO:0002327"}, "assessment":
    "qualified_positive", "reason": "Chemical cosolutes to stabilization process meet
    RO material/process endpoints. Direct stabilization wording can support execution;
    no categorical chemical prohibition or additional precision finding is inferred."},
    {"index": 8, "edge": {"subject": "nuo_complex_i", "predicate": "supports", "object":
    "high_pressure_energy_conservation", "description": "The nuo NADH dehydrogenase
    I complex supports respiratory energy conservation enabling growth under high
    pressure.", "evidence": [{"reference": "DOI:10.1186/s12864-020-07102-y", "notes":
    "nuo dehydrogenase operons present in piezophiles; respiratory-chain composition
    modulates pressure tolerance, a candidate contributor to wider high-pressure growth
    support."}]}, "assessment": "lexical_only", "reason": "Ungrounded supports links
    a contextual protein-complex aggregate to a process; the operon wording issue
    belongs to node 9 only. Detailed efficacy is unassessed."}, {"index": 9, "edge":
    {"subject": "min_max_growth_pressure_bounds", "predicate": "defines", "object":
    "pressure_delta_trait", "description": "The minimum and maximum growth-pressure
    limits define the breadth (max minus min) recorded by the delta.", "evidence":
    [{"reference": "DOI:10.1186/s12864-020-07102-y", "notes": "Range-bound examples
    (e.g., MTCD1 80-140 MPa => delta = 60 MPa) show min/max bounds defining the pressure-delta
    breadth descriptor."}], "predicate_id": "METPO:2007500"}, "assessment": "supported",
    "reason": "The pair of growth pressure bounds operationally defines their difference;
    v4 defines feature-to-trait meaning fits."}]'
- assessment_id: biology
  area: evidence
  topic: 'Native checklist: generic environmental context and limitations'
  outcome: unknown
  target_ids:
  - traitmech:000006
  summary: Selected membrane, physical chemistry and comparative environmental observations
    support contextual pressure/fluidity, solute and growth-bound associations. Community
    respiration versus species growth and the conditional nuo contribution remain
    qualifications. Detailed pressure-defense, fitness, AMR, survival training, intervention
    efficacy and methods are UNASSESSED_SCOPE.
  evidence_ids:
  - edge-sources
  - source-reading
  - source-access
  - body-membrane
  - body-chemrev
  - body-physiology
  - body-genomes
  - bounds-observation
- assessment_id: completeness
  area: completeness
  topic: 'Native checklist: NONMECHANISTIC applicability'
  outcome: supported
  target_ids:
  - traitmech:000006
  summary: Four disclosed components, one reviewed label-only aggregate and zero instances
    are compatible with the contextual quantitative graph. No mandatory connector,
    pathway, protein instance, additional canonical or experiment is prescribed.
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
  - traitmech:000006
  summary: Canonical Colwellia/MTCD1 aliases do not match the retained 20-organism
    / 28-dataset catalog. No strain-resolved locus or detailed pressure-response module
    query was run. This does not assert global dataset absence.
  evidence_ids:
  - expression
  - catalog-reuse
  - taxon-colwellia
- assessment_id: ownership
  area: provenance
  topic: 'Native checklist: current and conditional writers'
  outcome: supported
  target_ids:
  - traitmech:000006
  summary: Record owns node 9 wording and source notes. Predicate mapping/shared grounder
    conditionally recur on empty IDs; nonempty IDs are skipped. Exact canonical backfill
    is positive and guarded. Sibling reviewers and trait-object migrations do not
    repair current process-object edge 2.
  evidence_ids:
  - owners
  - ground-reading
  - local-authority
- assessment_id: human
  area: provenance
  topic: 'Native checklist: bounded acceptance trace'
  outcome: concern
  target_ids:
  - traitmech:000006
  summary: Seven current events are all AI. One whole contextual repository history
    does not identify current-target acceptance. Ignored-inclusive 239 matching paths/67
    structured arrays/zero exact target arrays bound this gap; remote or private review
    is not ruled out.
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
  - traitmech:000006
  summary: All 64 inputs match. Native/strict and snippet retry pass; initial DNS
    failure is retained as optional. Actual B11 QC/B12 qualification/postcheck and
    local initialization are distinct from pending B11 publication.
  evidence_ids:
  - capture
  - source-capture
  - reuse
  - reuse-postcheck
  - local-init
  - native-checks
  - check-pressure-delta-native
  - check-pressure-delta-strict
  - check-pressure-delta-snippets-retry-network
findings:
- finding_id: process-as-executor
  issue_key: pressure-delta-process-as-executor
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Imported enables uses a production process as its material executor
  description: RO2327 inherits a material-entity executor domain and process range.
    Current edge 2 subject explicitly denotes unsaturated fatty acid production/desaturation,
    a process, while its object is a maintenance process. Preserve the source-backed
    generic observation while reconciling the formal assertion; this is not a defect
    in the correctly typed production node.
  target_ids:
  - traitmech:000006
  field_paths:
  - causal_graphs[0].edges[2]
  evidence_ids:
  - node-edges
  - ro-primary
  - ro-intermediate
  - schema
  - owners
  - challenge
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/pressure_delta.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Wildcard enables row may recur on empty predicate fields.
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Existing nonempty IDs are skipped; mapping edits alone do not repair the
      current assertion.
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: complex-operon-wording
  issue_key: pressure-delta-complex-operon-wording
  category: consistency
  severity: minor
  status: open
  certainty: confirmed
  title: Protein-complex description calls its referent an operon
  description: Node 9 label, reviewed aggregate rationale and outgoing relation identify
    Complex I, while its description uses operon. Clarify this local description without
    inferring a gene-as-protein identity major, forced accession or detailed respiratory
    mechanism repair.
  target_ids:
  - traitmech:000006
  field_paths:
  - causal_graphs[0].nodes[9].description
  evidence_ids:
  - node-edges
  - node-sources
  - policy
  - owners
  - challenge
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/pressure_delta.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: desaturase-cohort-scope
  issue_key: pressure-delta-desaturase-cohort-scope
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Comparative Colwellia statement is broadened to all piezophiles
  description: The assigned genomic comparison scopes the desaturase observation to
    its piezophilic Colwellia cohort; the current note broadens this to all piezophiles.
    Generic unsaturated-lipid context remains supported, including source exceptions.
    This is a bounded attribution correction, not proof of a universal biological
    absence or false entire paper.
  target_ids:
  - traitmech:000006
  field_paths:
  - causal_graphs[0].edges[2].evidence[0].notes
  evidence_ids:
  - edge-sources
  - body-genomes
  - body-membrane
  - body-chemrev
  - challenge
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/pressure_delta.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: literal-unit-format
  issue_key: pressure-delta-literal-unit-format
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Snippet changes the source unit notation
  description: The record writes degrees C where the source abstract uses °C. All
    interval, optimum and temperature values are supported after normalization; only
    the maintained literal copied-span rule is implicated.
  target_ids:
  - traitmech:000006
  field_paths:
  - evidence[1].snippet
  evidence_ids:
  - snippets
  - meta-colwellia
  - playbook
  - challenge
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/pressure_delta.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: human-acceptance-link
  issue_key: pressure-delta-human-acceptance-link
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Current reviewed status lacks a locally attributable acceptance link
  description: Seven AI events and one contextual history do not identify current-target
    human acceptance. Ignored-inclusive 239 matching paths/67 parsed arrays/zero exact
    targets bound this traceability concern; no private or remote review absence is
    claimed.
  target_ids:
  - traitmech:000006
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
    path: data/traits/environment/pressure_delta.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
actions:
- action_id: reconcile-imported-role
  description: Reconcile the imported enables assertion with the actual process referents
    during authorized curation.
  finding_ids:
  - process-as-executor
  target_ids:
  - traitmech:000006
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/pressure_delta.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Wildcard enables row may recur on empty predicate fields.
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Existing nonempty IDs are skipped; mapping edits alone do not repair the
      current assertion.
  acceptance_checks:
  - Preserve supported generic environmental observations and correct production node
    type.
  - Respect nonempty-ID guards; mapping edits do not automatically replace current
    assertions.
  - No detailed mechanism or intervention reconstruction.
- action_id: clarify-complex-description
  description: Clarify node 9 description so it denotes the existing protein-complex
    aggregate.
  finding_ids:
  - complex-operon-wording
  target_ids:
  - traitmech:000006
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/pressure_delta.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Retain operon information only as appropriately separated metadata.
  - No mandatory protein instance, locus or mechanistic repair.
- action_id: restore-cohort-scope
  description: Scope the desaturase attribution to the actual comparative source cohort.
  finding_ids:
  - desaturase-cohort-scope
  target_ids:
  - traitmech:000006
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/pressure_delta.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Preserve supported generic membrane context and source-specific exceptions.
  - Do not replace a bounded comparison with a universal biological claim.
- action_id: restore-literal-format
  description: Use the actual source unit notation for the supported snippet.
  finding_ids:
  - literal-unit-format
  target_ids:
  - traitmech:000006
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/pressure_delta.yaml
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
  - traitmech:000006
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/pressure_delta.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Retain all seven AI events and bounded contextual history/search evidence.
  - No contact or automatic status promotion authorized.
limitations:
- Detailed pathogen pressure-defense, fitness, AMR, survival training, intervention
  efficacy and methods are UNASSESSED_SCOPE; incidental displayed content is not adopted.
- The canonical 60 MPa is derived arithmetic from an explicitly reported 80–140 MPa
  interval at 6 °C; source need not coin pressure delta, and optimum 120 MPa is distinct.
- Colwellia primary body was not acquired/inspected; its indexed abstract directly
  supports the canonical observation. No fresh failed primary-body request or paper-wide
  absence is claimed.
- Nature selected text is represented by a derived transcription receipt, not retained
  raw HTML. The original successful browser access time was not instrumented; later
  failed HTTP500 reread and PDF403 attempts remain explicit. Root read the receipt,
  not raw publisher HTML.
- ChemRev is an author-deposited manuscript with verified title/DOI; selected generic
  physical context and derived PDF text are distinguished from a publisher-formatted
  final body. Newline locators differ from Python splitlines because of PDF formfeeds.
- Community respiration observations do not independently calibrate every species
  growth bound. Conditional nuo energy contribution and generic source inference remain
  limitations rather than added findings.
- Retained metadata acquisition was 20:42:51 and membrane body acquisition 16:07:33–35;
  copies at 21:19:31 are distinct from fresh metadata 21:17:30–31 and body requests
  starting 21:17:49. Official taxonomy retains original successful 16:11:19–20 acquisition
  and prior DNS failure.
- Fallback/proposed 1007605 is not an imported active replacement. Four contextual
  components and a reviewed label-only protein aggregate do not require speculative
  connectors or instances.
- Actual prior QC, current qualification and local initialization do not assert B11
  remote publication; publication remains separately documented.
notes:
- Final root adjudication and independent challenge are pinned and verified; preparation
  does not import or execute the serializer. Root owns subsequent execution, validation
  and save.
- 'Coverage: six works/six forms, fifteen external placements, nine grounding fields,
  twelve nodes/ten edges, one canonical, two snippets: one literal and one supported
  unit transcription.'
- No scientific record, native inventory, Git or sweep-state mutation by serializer
  preparation.
tags:
- record-review
- pressure-delta
- environment
- needs-curation
native_verdict: needs_curation
```
