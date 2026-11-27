# Whole-record review of piezophilic

- Review: 20261021T205128Z-piezophilic
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-21T20:41:54.354885Z
- Finished UTC: 2026-10-21T20:51:28Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Final root disposition: one grouped imported-role major and three bounded minors for enabling semantics, literal unit format and human acceptance; source observations and both canonical examples positive.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: Tenth record of the actual batch 011 queue. Whole 246-line target and initial 66 inputs verified before source judgment. Supplemental native capture adds two v5 proposal inputs, retains all 66 bytes and supplies final 68 inputs. Source, grounding, challenge and root readings remain separately attributed.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8eee04a8c65609fbaff6df7c54597dcaf1b9d282.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| traitmech:000001 | data/traits/environment/piezophilic.yaml | maintained | piezophilic |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full-corpus graph audit | passed | True | traitmech:000001 | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| Full-corpus snippet audit | passed | True | traitmech:000001 | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| Full-corpus pathway links | passed | True | traitmech:000001 | 19 links checked against the pinned PathwayMech snapshot. |
| Full-corpus history integrity | passed | True | traitmech:000001 | 1277 history records checked, zero invalid links at the 8eee source base; integrity does not establish science or human acceptance. |
| Initial full-product validation | failed | False | traitmech:000001 | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation with isolated local cache | failed | False | traitmech:000001 | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation after isolated-cache download | passed | True | traitmech:000001 | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| Focused native validation | passed | True | traitmech:000001 | Successful focused schema validation; scientific semantics separately assessed. |
| Focused strict validation | passed | True | traitmech:000001 | Successful focused strict validation; not biological efficacy certification. |
| Initial focused snippet attempt | failed | False | traitmech:000001 | Initial DNS failure, exit 2, retained and superseded by successful network retry; no completed-review failure inferred. |
| Focused snippet network retry | passed | True | traitmech:000001 | Two fields over two references: both NOT_IN_ABSTRACT. Actual body verifies first literally; actual Colwellia abstract supports second after explicit unit transcription. |
| Reused maintained batch-ten QC | passed | True | traitmech:000001 | Actual B10 final QC at original time, qualified against B11 bytes. |
| Protein-instance metadata applicability | not_applicable | False | traitmech:000001 | One reviewed label-only protein module, zero instances; NONMECHANISTIC scope does not require token UniProt examples. |

## Scientific And Domain Assessments

### Native checklist: fallback identity and synonym scope

identity: supported. Targets: traitmech:000001.

Current traitmech preference identity remains distinct from tolerance and broader active pressure terms. V5 proposed 1007600 is captured but not an active release replacement; no new fallback allocation invoked.

### Native checklist: high-pressure preference

evidence: supported. Targets: traitmech:000001.

Actual assigned review body defines high-pressure preference and distinguishes piezotolerance. The generic environmental definition is supported without imposing a single quantitative cutoff for all taxa.

### Native checklist: current parent and local authorities

identity: supported. Targets: traitmech:000001.

Direct phenotype parent and captured v2/v8/v9 terms are assessed on actual maintained scope; broad local endpoints do not erase imported RO roles.

### Native checklist: all source identities and placements

evidence: supported. Targets: traitmech:000001.

Five reference forms resolve to four works because the Colwellia DOI and PMID are aliases. All seventeen placements have source-specific support or explicit uncertainty; source types and indexed abstract versus actual body are distinct.

### Native checklist: literal and unit-format fidelity

evidence: concern. Targets: traitmech:000001.

First snippet is literal in the actual review body. Colwellia interval/optimum/temperature are supported after degrees C to °C normalization, but the supplied snippet is not the exact copied format required by policy. Native two NOT_IN_ABSTRACT outcomes remain unchanged.

### Native checklist: reported canonical observations

evidence: supported. Targets: traitmech:000001.

Assigned abstracts support Colwellia MTCD1T high-pressure preference and P. profundum SS9 model status. The 2017 most-piezophilic wording is historical, not a newly verified ranking. Official taxa positive; full primary bodies were not acquired/inspected.

### Native checklist: all eight represented facets

consistency: supported. Targets: traitmech:000001.

Current Pfa node explicitly denotes a protein module, and both chemical groups and adaptation/stabilization processes retain their represented meanings. One reviewed label-only class is permitted; no copied gene-as-protein or obligatory sequence defect.

[{"index": 0, "field": "causal_graphs[0].nodes[0]", "current": {"node_id": "piezophilic_trait", "label": "piezophilic", "node_type": "TRAIT", "grounding": "traitmech:000001", "description": "Optimal growth at hydrostatic pressures well above atmospheric."}, "status": "SUPPORTED", "assessment": "Current trait node exactly reuses the accepted fallback and explicit optimum-growth concept; broad pressure tolerance is not silently substituted."}, {"index": 1, "field": "causal_graphs[0].nodes[1]", "current": {"node_id": "high_hydrostatic_pressure", "label": "high hydrostatic pressure", "node_type": "ENVIRONMENTAL_FACTOR", "description": "Deep-sea / deep-subsurface hydrostatic pressure (tens to &gt;100 MPa)."}, "status": "SUPPORTED_WITH_LIMITATION", "assessment": "Environmental condition is a legitimate schema facet; event interpretation could be made explicit, but does not cure chemical objects of the imported regulation edges."}, {"index": 2, "field": "causal_graphs[0].nodes[2]", "current": {"node_id": "unsaturated_branched_fa", "label": "unsaturated / branched-chain fatty acids", "node_type": "CHEMICAL", "description": "Membrane lipid species maintaining fluidity under high pressure."}, "status": "SUPPORTED", "assessment": "Material fatty-acid class is coherent; lack of a single exact chemical accession is not itself a finding."}, {"index": 3, "field": "causal_graphs[0].nodes[3]", "current": {"node_id": "membrane_adaptation", "label": "membrane lipid adaptation", "node_type": "BIOLOGICAL_PROCESS", "description": "Lipid composition adjustment maintaining membrane fluidity under HHP."}, "status": "SUPPORTED", "assessment": "Explicit lipid-composition adjustment is a process; maintaining fluidity is its described functional effect."}, {"index": 4, "field": "causal_graphs[0].nodes[4]", "current": {"node_id": "pfa_operon", "grounding_status": "REVIEWED_LABEL_ONLY", "grounding_notes": "Reviewed protein family, complex, or aggregate; no single semantic family identifier exactly captures this node's represented scope.", "label": "Pfa polyunsaturated-fatty-acid enzyme module", "node_type": "GENE_OR_PROTEIN", "description": "Protein module forming an omega-3 polyunsaturated fatty acid synthase.", "gene_symbols": ["pfaA", "pfaB", "pfaC", "pfaD", "pfaE"], "operon": "pfa"}, "status": "SUPPORTED", "assessment": "Actual label/description denotes an enzyme protein module. Gene symbols and operon are metadata. REVIEWED_LABEL_ONLY and NONMECHANISTIC scope permit zero optional protein examples."}, {"index": 5, "field": "causal_graphs[0].nodes[5]", "current": {"node_id": "omega3_pufa", "label": "omega-3 polyunsaturated fatty acids", "node_type": "CHEMICAL", "description": "Omega-3 PUFAs (e.g. EPA C20:5, DHA C22:6) supporting membrane fluidity under HHP."}, "status": "SUPPORTED", "assessment": "PUFA chemical class with examples remains material; the imported regulator edges need appropriate roles independently of this valid node facet."}, {"index": 6, "field": "causal_graphs[0].nodes[6]", "current": {"node_id": "piezolytes", "label": "piezolytes (compatible solutes)", "node_type": "CHEMICAL", "description": "Compatible solutes such as glutamate, betaine, beta-hydroxybutyrate and TMAO that confer pressure tolerance."}, "status": "SUPPORTED", "assessment": "Compatible-solute class is material. No categorical inability of a chemical to stabilize a component is inferred."}, {"index": 7, "field": "causal_graphs[0].nodes[7]", "current": {"node_id": "pressure_tolerance", "label": "pressure tolerance", "node_type": "BIOLOGICAL_PROCESS", "description": "Cellular stabilization against high hydrostatic pressure."}, "status": "SUPPORTED_WITH_LIMITATION", "assessment": "Cellular stabilization is a defensible process reading despite the tolerance label. No automatic CAPACITY/TRAIT retyping is required; its outgoing imported relation is independently inconsistent."}]

### Native checklist: all ten relation roles

consistency: concern. Targets: traitmech:000001.

RO2213 edges 3/5 have explicit chemical objects, which independently conflict with the inherited process range; the condition/event subject reading is qualified. RO2326 edge 9 uses process to trait rather than material-to-process contribution. RO2327 edges 1/6 pass endpoint classes but overstate executor role for structural lipid contribution; edge 8 direct stabilization remains qualified positive.

[{"index": 0, "field": "causal_graphs[0].edges[0]", "current": {"subject": "high_hydrostatic_pressure", "predicate": "selects for", "object": "piezophilic_trait", "description": "HHP habitats favor optimal-at-pressure growth phenotype.", "evidence": [{"reference": "DOI:10.3389/fmolb.2022.1058381", "notes": "HHP-adapted organisms are termed piezophiles for their preference for high pressure."}], "predicate_id": "METPO:2007401"}, "subject_type": "ENVIRONMENTAL_FACTOR", "object_type": "TRAIT", "status": "SUPPORTED_WITH_LIMITATION", "assessment": "Local v2 selects for has environmental-condition to adapted-trait prose and broad node endpoints; current shape is eligible. Evolutionary-selection strength remains a source-scope limitation, not a fabricated formal error."}, {"index": 1, "field": "causal_graphs[0].edges[1]", "current": {"subject": "unsaturated_branched_fa", "predicate": "enables", "object": "membrane_adaptation", "description": "Unsaturated and branched-chain fatty acids maintain membrane fluidity under HHP.", "evidence": [{"reference": "DOI:10.3389/fmolb.2022.1058381", "notes": "Piezophile adaptation involves unsaturated and branched-chain fatty acids."}], "predicate_id": "RO:0002327"}, "subject_type": "CHEMICAL", "object_type": "BIOLOGICAL_PROCESS", "status": "MINOR_PRECISION", "assessment": "RO2327 material-to-process endpoints pass. The subject is a structural lipid constituent maintaining fluidity, while the object explicitly denotes composition adjustment; the stronger acts-to-execute relation needs role precision. No chemical exclusion or replacement mechanism is prescribed."}, {"index": 2, "field": "causal_graphs[0].edges[2]", "current": {"subject": "membrane_adaptation", "predicate": "confers", "object": "piezophilic_trait", "description": "Membrane lipid adaptation enables high-pressure-optimal growth.", "evidence": [{"reference": "DOI:10.1099/ijsem.0.001671", "notes": "Colwellia marinimaniae MTCD1 grows optimally at 120 MPa, supported by HHP-adapted membranes."}], "predicate_id": "METPO:2007700"}, "subject_type": "BIOLOGICAL_PROCESS", "object_type": "TRAIT", "status": "SUPPORTED_WITH_LIMITATION", "assessment": "Local v8 confers explicitly permits this biological-process to trait shape. Generic adaptation context does not alone establish every optimum or universal necessity."}, {"index": 3, "field": "causal_graphs[0].edges[3]", "current": {"subject": "high_hydrostatic_pressure", "predicate": "increases", "object": "unsaturated_branched_fa", "description": "HHP increases abundance of membrane unsaturated and branched-chain fatty acids.", "evidence": [{"reference": "DOI:10.3389/fmolb.2022.1058381", "notes": "The abundance of membrane lipids containing unsaturated and branched-chain fatty acids rises with increasing HHP."}], "predicate_id": "RO:0002213"}, "subject_type": "ENVIRONMENTAL_FACTOR", "object_type": "CHEMICAL", "status": "MAJOR", "assessment": "RO2213 inherits process-to-process endpoints through RO2211. The explicit chemical fatty-acid object is not a process; the pressure-condition subject is additionally qualified by a possible event reading. Increasing abundance is not execution of the chemical entity."}, {"index": 4, "field": "causal_graphs[0].edges[4]", "current": {"subject": "pfa_operon", "predicate": "produces", "object": "omega3_pufa", "description": "The pfa operon encodes an omega-3 polyunsaturated fatty acid synthase enabling PUFA production.", "evidence": [{"reference": "DOI:10.3390/microorganisms11071629", "notes": "The pfa operon encodes an omega-3 polyunsaturated fatty acid synthase."}], "predicate_id": "METPO:2007800"}, "subject_type": "GENE_OR_PROTEIN", "object_type": "CHEMICAL", "status": "SUPPORTED", "assessment": "Current protein-module subject to chemical product fits the local produces definition and maintained gate. The historical pfa identifier is not evidence that this current node denotes naked DNA."}, {"index": 5, "field": "causal_graphs[0].edges[5]", "current": {"subject": "high_hydrostatic_pressure", "predicate": "increases", "object": "omega3_pufa", "description": "HHP increases polyunsaturated fatty acids C20:5 (EPA) and C22:6 (DHA) across multiple piezophilic/piezotolerant taxa.", "evidence": [{"reference": "DOI:10.3389/fmolb.2022.1058381", "notes": "HHP-driven increases in C20:5/C22:6 in Photobacterium profundum SS9, Psychromonas, and Shewanella piezotolerans WP3."}], "predicate_id": "RO:0002213"}, "subject_type": "ENVIRONMENTAL_FACTOR", "object_type": "CHEMICAL", "status": "MAJOR", "assessment": "RO2213 inherits process-to-process endpoints. PUFA molecules are material chemical objects; their increasing abundance does not make them processes. Event-versus-condition interpretation of exposure cannot cure this object mismatch."}, {"index": 6, "field": "causal_graphs[0].edges[6]", "current": {"subject": "omega3_pufa", "predicate": "enables", "object": "membrane_adaptation", "description": "Omega-3 PUFAs maintain membrane fluidity, contributing to lipid adaptation under HHP.", "evidence": [{"reference": "DOI:10.3389/fmolb.2022.1058381", "notes": "Unsaturated/polyunsaturated fatty acids maintain membrane fluidity under high pressure."}], "predicate_id": "RO:0002327"}, "subject_type": "CHEMICAL", "object_type": "BIOLOGICAL_PROCESS", "status": "MINOR_PRECISION", "assessment": "Same bounded executor-versus-structural-contributor precision as edge 1. Material/process endpoints fit, while maintaining fluidity differs from directly executing lipid-composition adjustment."}, {"index": 7, "field": "causal_graphs[0].edges[7]", "current": {"subject": "high_hydrostatic_pressure", "predicate": "induces accumulation of", "object": "piezolytes", "description": "HHP is associated with accumulation of compatible solutes (piezolytes) such as glutamate, betaine and beta-hydroxybutyrate.", "evidence": [{"reference": "DOI:10.3390/microorganisms11071629", "notes": "Compatible solutes (piezolytes) detected include glutamate, betaine, and beta-hydroxybutyrate; TMAO acts as a pressure-tolerance molecule."}]}, "subject_type": "ENVIRONMENTAL_FACTOR", "object_type": "CHEMICAL", "status": "SUPPORTED_WITH_LIMITATION", "assessment": "The free predicate has no asserted imported domain/range. Existing association wording is assessed as contextual; absence of an identifier is not automatically a finding."}, {"index": 8, "field": "causal_graphs[0].edges[8]", "current": {"subject": "piezolytes", "predicate": "enables", "object": "pressure_tolerance", "description": "Piezolytes stabilize cellular components, conferring tolerance to high hydrostatic pressure.", "evidence": [{"reference": "DOI:10.3390/microorganisms11071629", "notes": "TMAO and other compatible solutes are highlighted as pressure-tolerance molecules."}], "predicate_id": "RO:0002327"}, "subject_type": "CHEMICAL", "object_type": "BIOLOGICAL_PROCESS", "status": "SUPPORTED_WITH_LIMITATION", "assessment": "Material solutes to the described stabilization process can satisfy the executor reading. Keep this positive/qualified case separate from edges 1/6; no categorical chemical exclusion."}, {"index": 9, "field": "causal_graphs[0].edges[9]", "current": {"subject": "pressure_tolerance", "predicate": "contributes to", "object": "piezophilic_trait", "description": "Pressure tolerance via piezolytes contributes to optimal growth at high pressure.", "evidence": [{"reference": "DOI:10.3390/microorganisms11071629", "notes": "Piezolytes support growth and survival under high hydrostatic pressure."}], "predicate_id": "RO:0002326"}, "subject_type": "BIOLOGICAL_PROCESS", "object_type": "TRAIT", "status": "MAJOR", "assessment": "RO2326 inherits material-subject/process-object constraints through RO2216/2500/2595. Current cellular-stabilization process subject and phenotype trait object do not meet those roles. This does not require changing the valid process node into an arbitrary material type."}]

### Native checklist: generic environmental scope and limits

evidence: unknown. Targets: traitmech:000001.

Actual reviews support contextual membrane and microbial compatible-solute observations with taxon/temperature/salinity exceptions. No universal necessity or tolerance-preference equivalence is inferred. Nearest Colwellia membrane causality remains unknown on the inspected abstract; detailed intervention/fitness mechanisms are UNASSESSED_SCOPE.

### Native checklist: NONMECHANISTIC applicability

completeness: supported. Targets: traitmech:000001.

One component, a contextual reviewed protein module and two canonical examples are compatible with the stated scope. No mandatory extra pathway, connector, accession or experimental design.

### Native checklist: structured catalog applicability

evidence: not_applicable. Targets: traitmech:000001.

No exact canonical or searched type/model alias in the retained 20-organism/28-dataset catalog. Original acquisition is preserved; no substitute organism or downstream experiment query.

### Native checklist: exact current and historical writers

provenance: supported. Targets: traitmech:000001.

Current record and mapping/shared grounder own imported assertions; nonempty IDs are skipped. Historical enables migrations and sibling review/repair context are not asserted to repair current relations automatically.

### Native checklist: bounded attributable acceptance

provenance: concern. Targets: traitmech:000001.

Seven current events are all AI; three captured sibling AI histories are not direct acceptance of this target. Ignored-inclusive 203 paths/67 parsed arrays/zero exact targets bound the traceability concern; private or remote review is not ruled out.

### Native checklist: actual checks and chronology

consistency: supported. Targets: traitmech:000001.

All final 68 inputs and original66 bytes match. Native/strict and network snippet retry passed; initial snippet DNS failure retained as superseded optional check. Body DNS failure/retry is separate. Qualified common original outcomes and B10 QC retain their times.

## Findings

### imported-relation-roles: Imported process-regulation and contribution roles conflict with current referents

major / open / confirmed; issue key: piezophilic-imported-relation-roles.

RO2213 edges 3/5 inherit a process range but have explicit chemical products as objects, an independently decisive conflict. The high-pressure condition/event subject reading remains qualified; the enum alone is not an automatic prohibition. RO2326 edge 9 inherits material-to-process contribution roles but links the stabilization process to a preference trait. This is one grouped representation concern, not a false-pressure-biology finding.

### enabling-role-precision: Structural lipid contribution is described as direct enabling

minor / open / confirmed; issue key: piezophilic-enabling-role-precision.

RO2327 edges 1/6 satisfy material/process endpoints, but the represented lipids are structural contributors to membrane adaptation rather than clearly identified direct executors of that process. This bounded semantic precision concern does not assert false physiology or extend automatically to edge 8 stabilization.

### literal-unit-format: Snippet changes source unit notation

minor / open / confirmed; issue key: piezophilic-literal-unit-format.

The current Colwellia snippet spells degrees C where the actual source abstract uses °C. Normalization preserves interval, optimum and temperature completely; the finding is only literal copied-span format under maintained policy.

### human-acceptance-link: Current provenance lacks an attributable acceptance link

minor / open / confirmed; issue key: piezophilic-human-acceptance-link.

Seven AI events and three sibling AI histories do not identify linked current human acceptance. Ignored-inclusive 203 paths/67 parsed arrays/zero exact target arrays bound this concern; no claim about private or remote review.

## Recommended Actions And Acceptance Checks

### reconcile-imported-roles

Reconcile imported predicates with the represented condition, chemical, process and trait referents during authorized curation.

- Preserve positive environmental observations and source-specific limits.
- Respect current nonempty-ID guards and exact owner selectors; no automatic sibling rewrite.
- No new mechanism, experiment, optimized condition or mandatory protein instance.

### clarify-enabling-role

Clarify direct executor versus structural lipid contribution at the two bounded edges.

- Retain positive lipid/fluidity evidence and compatible endpoint classes.
- Do not extend the concern to edge 8 without its own evidence.

### restore-literal-unit-format

Use the actual source unit notation for the existing supported snippet.

- Preserve all numeric values, temperature and source identity.
- Keep interpretation and historical superlative scope in notes.

### link-human-acceptance

Link attributable current acceptance if available or clarify status while retaining provenance.

- Preserve all seven AI events and bounded sibling-history/search evidence.
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
| check-piezophilic-native | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-native.log; Executed 2026-10-21T20:42:11.589162+00:00 through 2026-10-21T20:42:12.322722+00:00; metadata piezophilic-native.json | context_only | Successful focused schema validation; scientific semantics separately assessed. |
| check-piezophilic-strict | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-strict.log; Executed 2026-10-21T20:42:11.589166+00:00 through 2026-10-21T20:42:12.700803+00:00; metadata piezophilic-strict.json | context_only | Successful focused strict validation; not biological efficacy certification. |
| check-piezophilic-snippets | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-snippets.log; Executed 2026-10-21T20:42:11.591102+00:00 through 2026-10-21T20:42:25.699030+00:00; metadata piezophilic-snippets.json | context_only | Initial DNS failure, exit 2, retained and superseded by successful network retry; no completed-review failure inferred. |
| check-piezophilic-snippets-retry-network | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-snippets-retry-network.log; Executed 2026-10-21T20:42:59.206277+00:00 through 2026-10-21T20:43:03.368420+00:00; metadata piezophilic-snippets-retry-network.json | context_only | Two fields over two references: both NOT_IN_ABSTRACT. Actual body verifies first literally; actual Colwellia abstract supports second after explicit unit transcription. |
| check-batch010-qc | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/batch010-qc.log; Executed 2026-10-21T19:06:27.731868+00:00 through 2026-10-21T19:08:11.219124+00:00; metadata batch010-qc.json | context_only | Actual B10 final QC at original time, qualified against B11 bytes. |
| record | data/traits/environment/piezophilic.yaml; Entire current 246-line record | supports | Eight nodes, ten edges, two snippets, two canonicals and seven AI record events covered. |
| policy | docs/GROUNDING_POLICY.md; Captured maintained authority | supports | Explicit material/process/condition roles and permitted reviewed protein module. |
| playbook | docs/CURATION_PLAYBOOK.md; Captured maintained authority | supports | Source scope, contiguous literal snippets and attributable acceptance. |
| schema | src/traitmech/schema/traitmech.yaml; Captured maintained authority | supports | Current declared node facets and review contract. |
| checklist | .claude/skills/curate-yaml-record/references/review-checklist.md; Captured maintained authority | supports | Complete identity, source, graph, ownership and readiness checklist. |
| reuse | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-b10-qc-supplement-qualified.json; Actual B10-to-B11 qualification | supports | Original outcomes and current byte comparisons bound. |
| reuse-postcheck | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-output-verification-agent/post-execution-verification.json; Independent qualifier verification | supports | Actual output/hash postcheck; no new QC. |
| capture-initial | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-grounding-agent/capture-verification.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Initial 66 inputs verified before judgment. |
| capture-final | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-grounding-agent/supplemental-capture-verification.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Final 68 inputs retain initial 66 and add v5 proposal before final judgment. |
| identity | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-grounding-agent/identity-assessment.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Retained traitmech fallback, parent and exact active/deprecated/proposal comparisons. |
| node-edges | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-grounding-agent/node-edge-ledger.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | All eight nodes/ten edges; role errors separate from bounded executor semantics. |
| owners | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-grounding-agent/owner-provenance-assessment.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Exact current/shared owners versus guarded historical and sibling context; bounded human search. |
| expression | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-grounding-agent/expression-assessment.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Actual structured catalog applicability for both canonical species, no proxy query. |
| authority-reuse | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-grounding-agent/authority-reuse-receipts.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Original catalog/runner acquisition receipts retained. |
| local-authority | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-grounding-agent/local-authority-excerpts.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Actual v2/v8/v9 proposal and broad maintained mapping/schema excerpts. |
| target-authority | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-grounding-agent/target-authority-supplement.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Exact v5 row and six current mapping rows; source hashes separate from receipt. |
| ground-reading | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-grounding-agent/reading-scope-receipt.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Three whole sibling-history reads belong to grounding; no direct target approval inferred. |
| ground-manifest | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-grounding-agent/evidence-manifest.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Frozen grounding artifacts verified. |
| taxon-reuse | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-grounding-agent/taxonomy1513592-reuse.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Colwellia original successful request and earlier DNS failure retained separately. |
| taxon-fresh | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-grounding-agent/taxonomy74109-access.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Actual fresh Photobacterium official taxonomy identity request. |
| metpo-primary | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/repo/data/raw/metpo.owl; Actual selected METPO XML and retained identity comparisons | supports | Active phenotype parent and broader pressure terms do not replace exact preference. Deprecated exact lexical predecessors lack replacement; the separately cited v5 proposal does not change imported release state. |
| ro-primary | /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/ro.db; Actual RO2213/2211, RO2326/2216/2500/2595 and RO2327 role/definition rows | supports | Imported process regulation and material-to-process contribution roles distinguish current conditions/chemicals/trait. Enables executor meaning is separate from material/process endpoint compatibility. |
| proposal-v5-primary | proposals/metpo_traitmech_v5/metpo_proposal_classes_robot.tsv; Captured TSV row3; exact fallback lift, separately from imported METPO | supports | Proposed 1007600 copies the current preference definition and phenotype parent. It remains a local proposal, not an imported active replacement. |
| taxon-colwellia | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-grounding-agent/taxon1513592.xml; Whole retained official taxonomy response; original acquisition | supports | Official Colwellia species/type identity; phenotype comes from assigned publication, not taxon record. |
| taxon-photobacterium | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-grounding-agent/taxon74109.xml; Whole fresh official taxonomy response | supports | Official Photobacterium species identity; SS9 paper scope retained separately. |
| meta-canonical-colwellia | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-agent/canonical-colwellia-metadata.json; Actual indexed metadata/abstract response; original request time | supports | PMID27902293 is the same species description as DOI001671; historical2017 superlative positive, no independently current ranking. |
| meta-canonical-photobacterium | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-agent/canonical-photobacterium-metadata.json; Actual indexed metadata/abstract response; original request time | supports | Actual primary abstract explicitly names SS9 as a piezophily model; no full-body inspection claimed. |
| meta-colwellia | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-agent/colwellia-metadata.json; Actual indexed metadata/abstract response; original request time | supports | Actual primary abstract supports MTCD1T 80–140 MPa, optimum 120 at 6 °C and fatty-acid identities; no demonstrated membrane causality inferred. |
| meta-membrane | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-agent/membrane-metadata.json; Actual indexed metadata/abstract response; original request time | supports | Actual review abstract explicitly describes a non-universal lipid response and pressure/temperature confounding. |
| meta-piezolytes | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-agent/piezolytes-metadata.json; Actual indexed metadata/abstract response; original request time | supports | Actual review identity/abstract covers environmental high-pressure adaptations; selected body separately bound. |
| body-membrane | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-agent/membrane.xml; Selected JATS body 1 classification and generic lipid paragraphs 3/6/8/9/10/13 | supports | Preference distinct from tolerance; current lipid examples positive with species/temperature exceptions and no universal necessity. |
| body-piezolytes | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-agent/piezolytes.xml; JATS selected generic synthase statement in 18 and compatible-solute paragraphs 26–28 | supports | Existing microbial solute/TMAO and synthase context positive; pressure/cold/salinity attribution qualified. Incidental intervention and respiratory/pathogen details unassessed. |
| sources | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-agent/source-assessment.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Four distinct assigned works/five forms; bounded source finding and limits. |
| source-ledger | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-agent/source-ledger.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | DOI/PMID identity aliases and actual abstract-versus-body scope. |
| placements | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-agent/placement-ledger.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | All seventeen external placements accounted for. |
| snippets | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-agent/snippet-ledger.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | One literal body phrase and one meaning-preserving degrees-C transcription; no unknown numeric claim. |
| node-sources | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-agent/node-source-ledger.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | All eight node-source contexts. |
| edge-sources | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-agent/edge-source-ledger.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | All ten edge-source contexts with nearest-citation limits. |
| source-status | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-agent/publication-status-ledger.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Actual indexed status fields; bounded not exhaustive publisher history. |
| source-reading | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-agent/selected-primary-reading.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Selected actual source reading scopes and incidentally displayed excluded details. |
| source-access | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-agent/access-limitations.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Canonical primary bodies not acquired/inspected; no claim of fresh failed canonical-body request. |
| source-metadata-copy | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-agent/metadata-copy-and-access.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Root original metadata requests separate from source copy/read times. |
| source-body-reuse | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-agent/primary-body-reuse.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Original membrane body acquired 16:07, copied 20:42; exact bytes qualified. |
| source-body-failure | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-agent/piezolytes-primary-access-initial.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Actual sandbox DNS body-acquisition failure, separate from native snippet DNS failure. |
| source-body-retry | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-agent/piezolytes-primary-access-network-retry.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Actual successful public body 20:43:58–59; no fabricated retry outcome. |
| canonical-scope | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-agent/canonical-assessment.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Both assigned canonical observations positive with strain and historical-superlative qualification. |
| native-checks | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-agent/native-check-context.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Actual native/strict pass and optional failed snippet followed by required successful retry. |
| source-capture | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-agent/final-capture-verification.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Final 68 and initial 66 inputs unchanged. |
| source-manifest | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-agent/evidence-manifest.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Twenty-six frozen source artifacts verified. |
| root-reading-74 | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-root/root-ground-final-reading.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Only actual bounded root reading/observation scope; receipt hash is not an article-body hash. |
| root-reading-75 | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-root/root-identity-owner-reading.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Only actual bounded root reading/observation scope; receipt hash is not an article-body hash. |
| root-reading-76 | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-root/root-metadata-reading.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Only actual bounded root reading/observation scope; receipt hash is not an article-body hash. |
| root-reading-77 | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-root/root-primary-reading-initial.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Only actual bounded root reading/observation scope; receipt hash is not an article-body hash. |
| root-reading-78 | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-root/root-primary-reading-second.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Only actual bounded root reading/observation scope; receipt hash is not an article-body hash. |
| root-reading-79 | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-root/root-ro-reading.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Only actual bounded root reading/observation scope; receipt hash is not an article-body hash. |
| root-reading-80 | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-root/root-source-freeze-reading.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Only actual bounded root reading/observation scope; receipt hash is not an article-body hash. |
| root-reading-81 | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-root/whole-target-root-reading.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Only actual bounded root reading/observation scope; receipt hash is not an article-body hash. |
| challenge | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-semantic-challenge-agent/semantic-severity-challenge.json; Final independent challenge | supports | Exact final anchors and evidence bindings verified. |
| adjudication | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-root-adjudication.json; Final root disposition | supports | Final severities, fields and nonfindings control this serialization. |

## Limits And Additional Notes

- Detailed pathogen fitness/defense/AMR, intervention efficacy and experimental or optimized conditions are UNASSESSED_SCOPE. Incidental displayed respiratory/mutant/control/future-method paragraphs are not adopted.
- Actual membrane and piezolyte reviews contain taxon-specific exceptions and pressure/temperature/salinity confounding. Current contextual graph is not read as universal necessity or every-taxon/every-lipid assertion.
- Tolerance differs from preferred-pressure growth. Contributes-to wording is not interpreted as equivalence or sufficient classification; formal imported-role defects are assessed independently.
- Colwellia and Photobacterium primary bodies were not acquired/inspected. Their actual assigned abstracts support current canonical observations, but Colwellia membrane causality remains unknown at its nearest citation. No fresh failed canonical-body request or paper-wide absence is claimed.
- The most-piezophilic superlative is explicitly the 2017 source statement; no independently current global ranking or evidence of surpassing it is asserted.
- Microbial TMAO context is explicit in the assigned review; no eukaryote-to-microbe transfer finding. Pressure-specific solute accumulation differs among taxa.
- Current Pfa protein module is coherent; its pressure versus cold association remains qualified without evaluating intervention efficacy or adding accessions.
- Retained fallback identity is not a fresh mint. Deprecated labels and proposed 1007600 do not establish an active exact imported replacement.
- Initial 66 capture preceded source judgment; final 68 adds v5 authority before final judgment and retains initial bytes. Native snippet DNS failure/retry and separate body DNS failure/retry remain distinct.
- Original membrane 16:07 and Colwellia taxonomy 16:11 acquisitions remain separate from current 20:42metadata,20:43body,20:44taxonomy, copies and readings. Three whole sibling-history readings belong to grounding; root/source scopes are separately attributed.
- Final root adjudication and independent challenge are pinned and verified. Author preparation did not import or execute the serializer; root owns later single execution, native validation and save.
- Coverage: four distinct works/five forms, seventeen external placements, eight nodes/ten edges, two canonicals, two snippets: one literal and one supported unit transcription.
- No scientific record, native inventory, Git or sweep state mutation by serializer preparation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T205128Z-piezophilic
kind: record
repository: CultureBotAI/TraitMech
title: Whole-record review of piezophilic
started_at: '2026-10-21T20:41:54.354885Z'
finished_at: '2026-10-21T20:51:28Z'
reviewer:
  identity: codex
  kind: agent
  independence: independent
  independence_basis: Independent source and grounding audits, separate semantic challenge
    and bounded root primary/owner readings. Existing environmental pressure preference/tolerance,
    canonical observations, source fidelity and formal roles assessed. Detailed pathogen
    fitness/defense/AMR and intervention efficacy are UNASSESSED_SCOPE. No scientific
    record edited.
  model: GPT-6 (Codex)
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'Final root disposition: one grouped imported-role major and three bounded
  minors for enabling semantics, literal unit format and human acceptance; source
  observations and both canonical examples positive.'
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
  - path: data/traits/environment/piezophilic.yaml
    sha256: 484e671b502c1c5ced9ff4d93d2a41f5ea025833dfb59edd784a9ea295503317
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
  - path: history/infrastructure/pr664-adversarial-review/2026-09-06T171200Z-codex-3c8677.yaml
    sha256: 0f9e6e876c4253ad25767d9f195f373a376abd716f364ae0ab8c90362e0fd6cc
    role: context
  - path: history/infrastructure/pr664-adversarial-review/2026-09-07T022200Z-codex-680abc.yaml
    sha256: e14f687969a1b4621f8857ca8b4f714662a454ed149431abcf0eab4cca346591
    role: context
  - path: history/records/obligately_piezophilic/2026-09-04T082000Z-codex-7cf93a.yaml
    sha256: b7e2482c60ae1dd34282660375d05ccf1df9172fc4c28f970fea7656f0abe7a4
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
  - path: proposals/metpo_traitmech_v2/metpo_proposal_properties_robot.tsv
    sha256: 4ab5ca37ff8595210254b1099563b4425ecd737ed375dc5a932b44e2ad5c332e
    role: context
  - path: proposals/metpo_traitmech_v2/proposal.md
    sha256: fe0601356b120ef9babc6f90a417f860bf02aa628c46af661517f168e01bc48f
    role: context
  - path: proposals/metpo_traitmech_v5/metpo_proposal_classes_robot.tsv
    sha256: d4b899de7077b33f4bdc6cb8cdebf28b5a705b7a65ba3620f3113b76d8666910
    role: context
  - path: proposals/metpo_traitmech_v5/proposal.md
    sha256: 5d54623dd00ac80a8d67a0eab7b70385f7f57b36daa205c28aa1f9d6f9be6167
    role: context
  - path: proposals/metpo_traitmech_v8/metpo_proposal_properties_robot.tsv
    sha256: 5445e86e845e0a2638292cff4586bf3858b1341d37fecf2e86cefcdbc9a046cd
    role: context
  - path: proposals/metpo_traitmech_v8/proposal.md
    sha256: 119d51e7b7194890514a9e313505212bab92aeba607f7c1b8f9d9d2edeef67e7
    role: context
  - path: proposals/metpo_traitmech_v9/metpo_proposal_properties_robot.tsv
    sha256: 5ae84dd1351a4bec39adf7bcd5b3a8982af2e95fbccd0b53c0efa3efbfc89b0e
    role: context
  - path: proposals/metpo_traitmech_v9/proposal.md
    sha256: 85fde22f4733863188b437cfcf7552a31fea07ad1d32c0400cf493295c1e1156
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
  - path: research/traits/environment/piezophilic-deep-research-falcon.md
    sha256: a1ed25abd5b0fd2326b46f93d3a46f6c9188367f2e5c98a0a89b990e278c0f99
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/add_ds_16_system_trait.py
    sha256: 56ed632043f60bfec71e167fa9e948f878ca160c2149c3f054e92cca6e85f236
    role: context
  - path: scripts/add_ds_43_system_trait.py
    sha256: 76a68189ec93c8bbf9c06bd632da99c6ae2da4e97312d850017d0a815ed27766
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
  - path: scripts/repair_pr664_adversarial_review.py
    sha256: 5717a89bee383aa0e12aec9bf30434ccff74efcbe64684d13ef9b290b1accf96
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
- target_id: traitmech:000001
  path: data/traits/environment/piezophilic.yaml
  label: piezophilic
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/piezophilic.yaml
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
  selection: Tenth record of the actual batch 011 queue. Whole 246-line target and
    initial 66 inputs verified before source judgment. Supplemental native capture
    adds two v5 proposal inputs, retains all 66 bytes and supplies final 68 inputs.
    Source, grounding, challenge and root readings remain separately attributed.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - traitmech:000001
checks:
- check_id: audit-graphs
  name: Full-corpus graph audit
  status: passed
  required: true
  target_ids:
  - traitmech:000001
  command: just audit-graphs --out /private/tmp/traitmech-record-sweep.FU79Gr/causal_graph_audit.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  evidence_ids:
  - check-audit-graphs
  scope_note: 'Original common diagnostics ran at f25; history validation ran in batch
    003 at 8eee. Actual B10 final QC and the seven-file delta are qualified against
    B11 bytes with an independent postcheck. Original failures/retries/skips and times
    remain explicit; no fresh B11 QC. Qualification: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-b10-qc-supplement-qualified.json'
- check_id: audit-snippets
  name: Full-corpus snippet audit
  status: passed
  required: true
  target_ids:
  - traitmech:000001
  command: just audit-snippets --report /private/tmp/traitmech-record-sweep.FU79Gr/evidence_snippet_audit.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  evidence_ids:
  - check-audit-snippets
  scope_note: 'Original common diagnostics ran at f25; history validation ran in batch
    003 at 8eee. Actual B10 final QC and the seven-file delta are qualified against
    B11 bytes with an independent postcheck. Original failures/retries/skips and times
    remain explicit; no fresh B11 QC. Qualification: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-b10-qc-supplement-qualified.json'
- check_id: check-pathway-links
  name: Full-corpus pathway links
  status: passed
  required: true
  target_ids:
  - traitmech:000001
  command: just check-pathway-links
  exit_code: 0
  expected_exit_code: 0
  summary: 19 links checked against the pinned PathwayMech snapshot.
  evidence_ids:
  - check-check-pathway-links
  scope_note: 'Original common diagnostics ran at f25; history validation ran in batch
    003 at 8eee. Actual B10 final QC and the seven-file delta are qualified against
    B11 bytes with an independent postcheck. Original failures/retries/skips and times
    remain explicit; no fresh B11 QC. Qualification: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-b10-qc-supplement-qualified.json'
- check_id: validate-history
  name: Full-corpus history integrity
  status: passed
  required: true
  target_ids:
  - traitmech:000001
  command: just validate-history
  exit_code: 0
  expected_exit_code: 0
  summary: 1277 history records checked, zero invalid links at the 8eee source base;
    integrity does not establish science or human acceptance.
  evidence_ids:
  - check-validate-history
  scope_note: 'Original common diagnostics ran at f25; history validation ran in batch
    003 at 8eee. Actual B10 final QC and the seven-file delta are qualified against
    B11 bytes with an independent postcheck. Original failures/retries/skips and times
    remain explicit; no fresh B11 QC. Qualification: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-b10-qc-supplement-qualified.json'
- check_id: validate-products
  name: Initial full-product validation
  status: failed
  required: false
  target_ids:
  - traitmech:000001
  command: just validate-products
  exit_code: 2
  expected_exit_code: 0
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  evidence_ids:
  - check-validate-products
  scope_note: 'Original common diagnostics ran at f25; history validation ran in batch
    003 at 8eee. Actual B10 final QC and the seven-file delta are qualified against
    B11 bytes with an independent postcheck. Original failures/retries/skips and times
    remain explicit; no fresh B11 QC. Qualification: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-b10-qc-supplement-qualified.json'
- check_id: validate-products-retry-local
  name: Product validation with isolated local cache
  status: failed
  required: false
  target_ids:
  - traitmech:000001
  command: just validate-products
  exit_code: 2
  expected_exit_code: 0
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  evidence_ids:
  - check-validate-products-retry-local
  scope_note: 'Original common diagnostics ran at f25; history validation ran in batch
    003 at 8eee. Actual B10 final QC and the seven-file delta are qualified against
    B11 bytes with an independent postcheck. Original failures/retries/skips and times
    remain explicit; no fresh B11 QC. Qualification: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-b10-qc-supplement-qualified.json'
- check_id: validate-products-retry-network
  name: Product validation after isolated-cache download
  status: passed
  required: true
  target_ids:
  - traitmech:000001
  command: just validate-products
  exit_code: 0
  expected_exit_code: 0
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  evidence_ids:
  - check-validate-products-retry-network
  scope_note: 'Original common diagnostics ran at f25; history validation ran in batch
    003 at 8eee. Actual B10 final QC and the seven-file delta are qualified against
    B11 bytes with an independent postcheck. Original failures/retries/skips and times
    remain explicit; no fresh B11 QC. Qualification: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-b10-qc-supplement-qualified.json'
- check_id: piezophilic-native
  name: Focused native validation
  status: passed
  required: true
  target_ids:
  - traitmech:000001
  command: just validate data/traits/environment/piezophilic.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Successful focused schema validation; scientific semantics separately assessed.
  evidence_ids:
  - check-piezophilic-native
- check_id: piezophilic-strict
  name: Focused strict validation
  status: passed
  required: true
  target_ids:
  - traitmech:000001
  command: just validate-strict data/traits/environment/piezophilic.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Successful focused strict validation; not biological efficacy certification.
  evidence_ids:
  - check-piezophilic-strict
- check_id: piezophilic-snippets
  name: Initial focused snippet attempt
  status: failed
  required: false
  target_ids:
  - traitmech:000001
  command: just verify-snippets --record data/traits/environment/piezophilic.yaml
    --out /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-snippets.tsv
  exit_code: 2
  expected_exit_code: 0
  summary: Initial DNS failure, exit 2, retained and superseded by successful network
    retry; no completed-review failure inferred.
  evidence_ids:
  - check-piezophilic-snippets
- check_id: piezophilic-snippets-retry-network
  name: Focused snippet network retry
  status: passed
  required: true
  target_ids:
  - traitmech:000001
  command: just verify-snippets --record data/traits/environment/piezophilic.yaml
    --out /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-snippets-retry-network.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 'Two fields over two references: both NOT_IN_ABSTRACT. Actual body verifies
    first literally; actual Colwellia abstract supports second after explicit unit
    transcription.'
  evidence_ids:
  - check-piezophilic-snippets-retry-network
- check_id: batch010-qc
  name: Reused maintained batch-ten QC
  status: passed
  required: true
  target_ids:
  - traitmech:000001
  command: just qc
  exit_code: 0
  expected_exit_code: 0
  summary: Actual B10 final QC at original time, qualified against B11 bytes.
  evidence_ids:
  - check-batch010-qc
- check_id: uniprot-applicability
  name: Protein-instance metadata applicability
  status: not_applicable
  required: false
  target_ids:
  - traitmech:000001
  summary: One reviewed label-only protein module, zero instances; NONMECHANISTIC
    scope does not require token UniProt examples.
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
- evidence_id: check-piezophilic-native
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-native.log
  locator: Executed 2026-10-21T20:42:11.589162+00:00 through 2026-10-21T20:42:12.322722+00:00;
    metadata piezophilic-native.json
  accessed_at: '2026-10-21T20:42:12.322722Z'
  support: context_only
  summary: Successful focused schema validation; scientific semantics separately assessed.
  snapshot_sha256: 8c26bdbb9000f016d3961879d4b5955075ac2896752b3833eeb5506688bc9f89
- evidence_id: check-piezophilic-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-strict.log
  locator: Executed 2026-10-21T20:42:11.589166+00:00 through 2026-10-21T20:42:12.700803+00:00;
    metadata piezophilic-strict.json
  accessed_at: '2026-10-21T20:42:12.700803Z'
  support: context_only
  summary: Successful focused strict validation; not biological efficacy certification.
  snapshot_sha256: 6d03fdce64391f3f51da530b8dff0a29ed91683a02fd5de4d21ba85d32a8d6da
- evidence_id: check-piezophilic-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-snippets.log
  locator: Executed 2026-10-21T20:42:11.591102+00:00 through 2026-10-21T20:42:25.699030+00:00;
    metadata piezophilic-snippets.json
  accessed_at: '2026-10-21T20:42:25.699030Z'
  support: context_only
  summary: Initial DNS failure, exit 2, retained and superseded by successful network
    retry; no completed-review failure inferred.
  snapshot_sha256: 18c930f6623f3805a61278a7c70cf7da36c897b619252ee7582431dce92d2a07
- evidence_id: check-piezophilic-snippets-retry-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-snippets-retry-network.log
  locator: Executed 2026-10-21T20:42:59.206277+00:00 through 2026-10-21T20:43:03.368420+00:00;
    metadata piezophilic-snippets-retry-network.json
  accessed_at: '2026-10-21T20:43:03.368420Z'
  support: context_only
  summary: 'Two fields over two references: both NOT_IN_ABSTRACT. Actual body verifies
    first literally; actual Colwellia abstract supports second after explicit unit
    transcription.'
  snapshot_sha256: cd667c65346c0c43c78997aaa2895749caec2e04d1c86d7e30739f52f27383d6
- evidence_id: check-batch010-qc
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/batch010-qc.log
  locator: Executed 2026-10-21T19:06:27.731868+00:00 through 2026-10-21T19:08:11.219124+00:00;
    metadata batch010-qc.json
  accessed_at: '2026-10-21T19:08:11.219124Z'
  support: context_only
  summary: Actual B10 final QC at original time, qualified against B11 bytes.
  snapshot_sha256: a97d2cc68e7db1ebd1a0edd19a7b0d03a4b1f45b55f8c6e6c2c48252f1705201
- evidence_id: record
  kind: record_content
  reference: data/traits/environment/piezophilic.yaml
  locator: Entire current 246-line record
  accessed_at: '2026-10-21T20:44:14.398910Z'
  support: supports
  summary: Eight nodes, ten edges, two snippets, two canonicals and seven AI record
    events covered.
  snapshot_sha256: 484e671b502c1c5ced9ff4d93d2a41f5ea025833dfb59edd784a9ea295503317
- evidence_id: policy
  kind: authority
  reference: docs/GROUNDING_POLICY.md
  locator: Captured maintained authority
  accessed_at: '2026-10-21T20:48:42.973683Z'
  support: supports
  summary: Explicit material/process/condition roles and permitted reviewed protein
    module.
  snapshot_sha256: 891678c983c2283a47c81c47950b35753981e9339d105f3bbdda92a1f5ab7f42
- evidence_id: playbook
  kind: authority
  reference: docs/CURATION_PLAYBOOK.md
  locator: Captured maintained authority
  accessed_at: '2026-10-21T20:48:42.973683Z'
  support: supports
  summary: Source scope, contiguous literal snippets and attributable acceptance.
  snapshot_sha256: 735e9b810471da9f7d8364e35ffe1e741edb3421480dac01727db6ea5aa65da9
- evidence_id: schema
  kind: authority
  reference: src/traitmech/schema/traitmech.yaml
  locator: Captured maintained authority
  accessed_at: '2026-10-21T20:48:42.973683Z'
  support: supports
  summary: Current declared node facets and review contract.
  snapshot_sha256: 46c47fc627b80ccbba1e8ab3fb6f2aee93bc2aef7aaf72fe9aadc3257f2c02dd
- evidence_id: checklist
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Captured maintained authority
  accessed_at: '2026-10-21T20:48:42.973683Z'
  support: supports
  summary: Complete identity, source, graph, ownership and readiness checklist.
  snapshot_sha256: da8896328a0fd6cc92f1adf0d8be8980d0ddd41f3172c7936f2c7f119b293ac1
- evidence_id: reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-b10-qc-supplement-qualified.json
  locator: Actual B10-to-B11 qualification
  accessed_at: '2026-10-21T19:08:29.388400Z'
  support: supports
  summary: Original outcomes and current byte comparisons bound.
  snapshot_sha256: a728777b9987b1283d7d1382168af40739074fce5c05f9a3bd93d3738f56880f
- evidence_id: reuse-postcheck
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-output-verification-agent/post-execution-verification.json
  locator: Independent qualifier verification
  accessed_at: '2026-10-21T19:08:41.804361Z'
  support: supports
  summary: Actual output/hash postcheck; no new QC.
  snapshot_sha256: a3a6f33363e71b00e8db09cbc318cae0027844aba584f7b4cafb282d11ab027a
- evidence_id: capture-initial
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-grounding-agent/capture-verification.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T20:42:29.019229Z'
  support: supports
  summary: Initial 66 inputs verified before judgment.
  snapshot_sha256: 8e4d4a8978704ad35046a908038edfe50078edfb7234ce5ef978f4992063ce39
- evidence_id: capture-final
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-grounding-agent/supplemental-capture-verification.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T20:44:32.308553Z'
  support: supports
  summary: Final 68 inputs retain initial 66 and add v5 proposal before final judgment.
  snapshot_sha256: fd1c82863daa32d78166527b6f76b1fcdcc2173244863af788d514f90502b130
- evidence_id: identity
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-grounding-agent/identity-assessment.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T20:48:42.972794Z'
  support: supports
  summary: Retained traitmech fallback, parent and exact active/deprecated/proposal
    comparisons.
  snapshot_sha256: 0ad2beaa09ba574a6b8fa2d60132fe45060f396a5eabd37f9715b47f5bd85cf7
- evidence_id: node-edges
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-grounding-agent/node-edge-ledger.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T20:48:42.973010Z'
  support: supports
  summary: All eight nodes/ten edges; role errors separate from bounded executor semantics.
  snapshot_sha256: 04891eab93aefafa24c1b2be35b7f6a505c2543b41849bf8ac0ad075d1c5fc02
- evidence_id: owners
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-grounding-agent/owner-provenance-assessment.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T20:48:42.973208Z'
  support: supports
  summary: Exact current/shared owners versus guarded historical and sibling context;
    bounded human search.
  snapshot_sha256: 16cc61f0fa95d352c187213380a2261fbffbec3eeb7e4ba51227cab235076121
- evidence_id: expression
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-grounding-agent/expression-assessment.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T20:48:42.973530Z'
  support: supports
  summary: Actual structured catalog applicability for both canonical species, no
    proxy query.
  snapshot_sha256: 5a0ea4834f8a7fa64e9fad9e54b4dcf1e260daebbd9c764af3739f7bd22bfaf6
- evidence_id: authority-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-grounding-agent/authority-reuse-receipts.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T20:44:17.614311Z'
  support: supports
  summary: Original catalog/runner acquisition receipts retained.
  snapshot_sha256: df7da3237d32a9f370f53c5e973cb65e6aa16c7b87b03f95abcd17fdf9cd3ef1
- evidence_id: local-authority
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-grounding-agent/local-authority-excerpts.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T20:44:17.599458Z'
  support: supports
  summary: Actual v2/v8/v9 proposal and broad maintained mapping/schema excerpts.
  snapshot_sha256: 5faf580821fc91b09d636bc799010e6742ccacfb88bff367ee4dbeb759f57e63
- evidence_id: target-authority
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-grounding-agent/target-authority-supplement.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T20:48:42.971771Z'
  support: supports
  summary: Exact v5 row and six current mapping rows; source hashes separate from
    receipt.
  snapshot_sha256: e324ed7650764c51d8812a2ebb3b812ffbc27a237de24e3970fd1445448a6b51
- evidence_id: ground-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-grounding-agent/reading-scope-receipt.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T20:48:42.973863Z'
  support: supports
  summary: Three whole sibling-history reads belong to grounding; no direct target
    approval inferred.
  snapshot_sha256: 0e01626937d827f7dc0ddd099f3bb9d3ac300f7bf485dc4be25747d8193126df
- evidence_id: ground-manifest
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-grounding-agent/evidence-manifest.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T20:48:42.975238Z'
  support: supports
  summary: Frozen grounding artifacts verified.
  snapshot_sha256: e38059fb8c547c18c77406e1230cc41bbbd47592663c6b4f81bf3a401700853e
- evidence_id: taxon-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-grounding-agent/taxonomy1513592-reuse.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T20:44:32.309787Z'
  support: supports
  summary: Colwellia original successful request and earlier DNS failure retained
    separately.
  snapshot_sha256: 3a496d133f9bb02d9344e6ea3293049933a6875fac2b55532dd6d9d2b9c767e2
- evidence_id: taxon-fresh
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-grounding-agent/taxonomy74109-access.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T20:44:50.500112Z'
  support: supports
  summary: Actual fresh Photobacterium official taxonomy identity request.
  snapshot_sha256: 08c0782a2d49fdcae32482b6f1ffb2f48a393d197eee10c0468d7f276d3fbe0f
- evidence_id: metpo-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/repo/data/raw/metpo.owl
  locator: Actual selected METPO XML and retained identity comparisons
  accessed_at: '2026-10-21T20:44:17.585329Z'
  support: supports
  summary: Active phenotype parent and broader pressure terms do not replace exact
    preference. Deprecated exact lexical predecessors lack replacement; the separately
    cited v5 proposal does not change imported release state.
  snapshot_sha256: 8b6f8fe0510a698579e532658c8ace05da2550093365df9ca83feb0741778415
- evidence_id: ro-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/ro.db
  locator: Actual RO2213/2211, RO2326/2216/2500/2595 and RO2327 role/definition rows
  accessed_at: '2026-10-21T20:44:17.591477Z'
  support: supports
  summary: Imported process regulation and material-to-process contribution roles
    distinguish current conditions/chemicals/trait. Enables executor meaning is separate
    from material/process endpoint compatibility.
  snapshot_sha256: 849e616c29fecd0d4a6c6dee0dc0f6f117ace7167dbfa1e0f043dc84868f83cb
- evidence_id: proposal-v5-primary
  kind: authority
  reference: proposals/metpo_traitmech_v5/metpo_proposal_classes_robot.tsv
  locator: Captured TSV row3; exact fallback lift, separately from imported METPO
  accessed_at: '2026-10-21T20:48:42.971771Z'
  support: supports
  summary: Proposed 1007600 copies the current preference definition and phenotype
    parent. It remains a local proposal, not an imported active replacement.
  snapshot_sha256: d4b899de7077b33f4bdc6cb8cdebf28b5a705b7a65ba3620f3113b76d8666910
- evidence_id: taxon-colwellia
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-grounding-agent/taxon1513592.xml
  locator: Whole retained official taxonomy response; original acquisition
  accessed_at: '2026-10-21T16:11:20.071001Z'
  support: supports
  summary: Official Colwellia species/type identity; phenotype comes from assigned
    publication, not taxon record.
  snapshot_sha256: 44883620d8bdc159d01e53d74afc493e730bac233c92303887b704c10061050e
- evidence_id: taxon-photobacterium
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-grounding-agent/taxon74109.xml
  locator: Whole fresh official taxonomy response
  accessed_at: '2026-10-21T20:44:50.500112Z'
  support: supports
  summary: Official Photobacterium species identity; SS9 paper scope retained separately.
  snapshot_sha256: b2a5ec08303e8ff4191e01fe10bc78b1202e248c155e14ecb9d34fdf1e39b656
- evidence_id: meta-canonical-colwellia
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-agent/canonical-colwellia-metadata.json
  locator: Actual indexed metadata/abstract response; original request time
  accessed_at: '2026-10-21T20:42:51.676896Z'
  support: supports
  summary: PMID27902293 is the same species description as DOI001671; historical2017
    superlative positive, no independently current ranking.
  snapshot_sha256: 68817d4174b5a03d3787fe01db0e43ec6dfa21500b5f07bf499b1fba718de923
- evidence_id: meta-canonical-photobacterium
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-agent/canonical-photobacterium-metadata.json
  locator: Actual indexed metadata/abstract response; original request time
  accessed_at: '2026-10-21T20:42:51.674562Z'
  support: supports
  summary: Actual primary abstract explicitly names SS9 as a piezophily model; no
    full-body inspection claimed.
  snapshot_sha256: 63ce9a9b5cca0d47aaa57a2e79c12b93a1aeac8baef3daa36dbf958b6cfe9788
- evidence_id: meta-colwellia
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-agent/colwellia-metadata.json
  locator: Actual indexed metadata/abstract response; original request time
  accessed_at: '2026-10-21T20:42:51.694246Z'
  support: supports
  summary: Actual primary abstract supports MTCD1T 80–140 MPa, optimum 120 at 6 °C
    and fatty-acid identities; no demonstrated membrane causality inferred.
  snapshot_sha256: e74a6f54136e6dcd2ab87b38d86de68e793d0dc28218b87b9f2bbd3ccd4103d2
- evidence_id: meta-membrane
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-agent/membrane-metadata.json
  locator: Actual indexed metadata/abstract response; original request time
  accessed_at: '2026-10-21T20:42:51.668312Z'
  support: supports
  summary: Actual review abstract explicitly describes a non-universal lipid response
    and pressure/temperature confounding.
  snapshot_sha256: 60b0dd82b02eddbe01f9944f485da11c5ea9e55ec36f65b501a3a78ba9b1e9b3
- evidence_id: meta-piezolytes
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-agent/piezolytes-metadata.json
  locator: Actual indexed metadata/abstract response; original request time
  accessed_at: '2026-10-21T20:42:51.672336Z'
  support: supports
  summary: Actual review identity/abstract covers environmental high-pressure adaptations;
    selected body separately bound.
  snapshot_sha256: f841a93f68b50bd7d184e38aeaf8ed5ebc840e76fd6864c64cedfb77bff21881
- evidence_id: body-membrane
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-agent/membrane.xml
  locator: Selected JATS body 1 classification and generic lipid paragraphs 3/6/8/9/10/13
  accessed_at: '2026-10-21T16:07:35.045859Z'
  support: supports
  summary: Preference distinct from tolerance; current lipid examples positive with
    species/temperature exceptions and no universal necessity.
  snapshot_sha256: d8320b3073b404cd79da19795d94f02477ce8a34accb22809294e05d1e72c032
- evidence_id: body-piezolytes
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-agent/piezolytes.xml
  locator: JATS selected generic synthase statement in 18 and compatible-solute paragraphs
    26–28
  accessed_at: '2026-10-21T20:43:59.908978Z'
  support: supports
  summary: Existing microbial solute/TMAO and synthase context positive; pressure/cold/salinity
    attribution qualified. Incidental intervention and respiratory/pathogen details
    unassessed.
  snapshot_sha256: b32571a4a2b468a959e4eb6d6b947576faa188eb3100daf47cc7840b23d2724e
- evidence_id: sources
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-agent/source-assessment.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T20:46:11.933199Z'
  support: supports
  summary: Four distinct assigned works/five forms; bounded source finding and limits.
  snapshot_sha256: 031d57b7ea9e777e9987ea42f34e238041c0e76e50ca705ad6093198b9ceaa62
- evidence_id: source-ledger
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-agent/source-ledger.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T20:46:11.930846Z'
  support: supports
  summary: DOI/PMID identity aliases and actual abstract-versus-body scope.
  snapshot_sha256: baefaced35154d72aa14fee1d59dae68b61a95a6358bb7d5215dbaeac4d65bed
- evidence_id: placements
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-agent/placement-ledger.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T20:46:11.931454Z'
  support: supports
  summary: All seventeen external placements accounted for.
  snapshot_sha256: 30d5fbb120775505e327340351287836720c0d2340ad29fab2158a12b77fb311
- evidence_id: snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-agent/snippet-ledger.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T20:46:11.931622Z'
  support: supports
  summary: One literal body phrase and one meaning-preserving degrees-C transcription;
    no unknown numeric claim.
  snapshot_sha256: 8f8ba2068f7a269f005ba0b2a2416f8a810b35e84283e2436c66d32a9f6dbefe
- evidence_id: node-sources
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-agent/node-source-ledger.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T20:46:11.931274Z'
  support: supports
  summary: All eight node-source contexts.
  snapshot_sha256: c96eb8a02db989c5166cdc716861187a1bdf222f5ed28ecf12225080ebdf35b3
- evidence_id: edge-sources
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-agent/edge-source-ledger.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T20:46:11.931113Z'
  support: supports
  summary: All ten edge-source contexts with nearest-citation limits.
  snapshot_sha256: 81dbaa667ec2dacaebdee67c96c4f0956863a2881d906895fa8678698d074e12
- evidence_id: source-status
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-agent/publication-status-ledger.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T20:46:11.931008Z'
  support: supports
  summary: Actual indexed status fields; bounded not exhaustive publisher history.
  snapshot_sha256: ed12b7d8e83912c46b46b08d3bdf10636681b6afcf7578266c34f489d898a810
- evidence_id: source-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-agent/selected-primary-reading.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T20:46:11.932939Z'
  support: supports
  summary: Selected actual source reading scopes and incidentally displayed excluded
    details.
  snapshot_sha256: 3c647448ba3ca87521500261c06071e1675cefeaee1ec91b78df961bf431f2cf
- evidence_id: source-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-agent/access-limitations.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T20:46:11.932415Z'
  support: supports
  summary: Canonical primary bodies not acquired/inspected; no claim of fresh failed
    canonical-body request.
  snapshot_sha256: c4058a26fddf02ee47d26d6649a88941f1ad526c425c72416ab5237056dbc64c
- evidence_id: source-metadata-copy
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-agent/metadata-copy-and-access.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T20:46:11.925709Z'
  support: supports
  summary: Root original metadata requests separate from source copy/read times.
  snapshot_sha256: dd747104ea8edf8b5e6ed75600cf5b1159f29ad2142daea2b1a978bf3f71ef2e
- evidence_id: source-body-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-agent/primary-body-reuse.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T20:42:34.939675Z'
  support: supports
  summary: Original membrane body acquired 16:07, copied 20:42; exact bytes qualified.
  snapshot_sha256: 0d28736227660ed3dd0bd2fe256f62df145bf632897fdf277b59e4833c296a0c
- evidence_id: source-body-failure
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-agent/piezolytes-primary-access-initial.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T20:43:49.065454Z'
  support: supports
  summary: Actual sandbox DNS body-acquisition failure, separate from native snippet
    DNS failure.
  snapshot_sha256: 85956afd7614378165ccc9a1a3c3e4fa2806e77131c29c9f5e989fd6b5c2bf50
- evidence_id: source-body-retry
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-agent/piezolytes-primary-access-network-retry.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T20:43:59.908978Z'
  support: supports
  summary: Actual successful public body 20:43:58–59; no fabricated retry outcome.
  snapshot_sha256: 99353b14bd2d500048cb433e75c4816eab51d923cf624c478e0252ecc1d9dfde
- evidence_id: canonical-scope
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-agent/canonical-assessment.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T20:46:11.931856Z'
  support: supports
  summary: Both assigned canonical observations positive with strain and historical-superlative
    qualification.
  snapshot_sha256: 28947b9f939e89e12a443bd78fb98f8b11b96bc04f72c6bc169bae7a390cac04
- evidence_id: native-checks
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-agent/native-check-context.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T20:46:11.932316Z'
  support: supports
  summary: Actual native/strict pass and optional failed snippet followed by required
    successful retry.
  snapshot_sha256: f3432203bfc626d204b8bfc7d22be5b5a8d8a63c954eb9f398167866edb852ad
- evidence_id: source-capture
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-agent/final-capture-verification.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T20:46:11.933400Z'
  support: supports
  summary: Final 68 and initial 66 inputs unchanged.
  snapshot_sha256: 93ea0f89194a7115ade25f6847dec966d0b796b915d9cd64c0b40b24e783d663
- evidence_id: source-manifest
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-agent/evidence-manifest.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T20:46:11.937723Z'
  support: supports
  summary: Twenty-six frozen source artifacts verified.
  snapshot_sha256: 8e85f2f0712ca2be1d04daeb07116bbf31a84cbb885952b9e392d1b9fe374671
- evidence_id: root-reading-74
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-root/root-ground-final-reading.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T20:49:31.850676Z'
  support: supports
  summary: Only actual bounded root reading/observation scope; receipt hash is not
    an article-body hash.
  snapshot_sha256: 6f3fc70a8f610105a951abd6a595337aae726acfb3af88a9ac33d24f68a539bd
- evidence_id: root-reading-75
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-root/root-identity-owner-reading.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T20:45:55.948965Z'
  support: supports
  summary: Only actual bounded root reading/observation scope; receipt hash is not
    an article-body hash.
  snapshot_sha256: 8fb4ce865ec08718a3182ba22e9cf8680a6596c170e2b82d1701d2c995a10c00
- evidence_id: root-reading-76
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-root/root-metadata-reading.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T20:43:17.367043Z'
  support: supports
  summary: Only actual bounded root reading/observation scope; receipt hash is not
    an article-body hash.
  snapshot_sha256: 87084dfa03fec41dd6ad3bbd965a60474e208c685b5b2cb5883d30e86d5fd9e7
- evidence_id: root-reading-77
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-root/root-primary-reading-initial.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T20:43:33.956998Z'
  support: supports
  summary: Only actual bounded root reading/observation scope; receipt hash is not
    an article-body hash.
  snapshot_sha256: a8cc5d91f4f34fc53b4a652518d7d18f441cc1700920d89d1623a6ebee639f25
- evidence_id: root-reading-78
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-root/root-primary-reading-second.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T20:44:43.825274Z'
  support: supports
  summary: Only actual bounded root reading/observation scope; receipt hash is not
    an article-body hash.
  snapshot_sha256: 4b698ba9189cb35723cdeb63874f931aec3aa3475df74b96a3413d32a2b79028
- evidence_id: root-reading-79
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-root/root-ro-reading.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T20:45:21.304682Z'
  support: supports
  summary: Only actual bounded root reading/observation scope; receipt hash is not
    an article-body hash.
  snapshot_sha256: c8fc1e4b7c9c891d4476bb725c49b97197faae710c6c814a2eeadb8926c9c8e4
- evidence_id: root-reading-80
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-root/root-source-freeze-reading.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T20:48:13.964143Z'
  support: supports
  summary: Only actual bounded root reading/observation scope; receipt hash is not
    an article-body hash.
  snapshot_sha256: 12409c7614e012077350231baf62108a84b171d1ffb7f21e7e8aa1a2a04bc56b
- evidence_id: root-reading-81
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-source-root/whole-target-root-reading.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T20:41:54.354705Z'
  support: supports
  summary: Only actual bounded root reading/observation scope; receipt hash is not
    an article-body hash.
  snapshot_sha256: 14208c1e0d3aaf712ff05331dca8baaa867094d6085c39a8b881226561dd4b4a
- evidence_id: challenge
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-semantic-challenge-agent/semantic-severity-challenge.json
  locator: Final independent challenge
  accessed_at: '2026-10-21T20:49:52.020928Z'
  support: supports
  summary: Exact final anchors and evidence bindings verified.
  snapshot_sha256: 456d38f989499b374e29eccbb6a020631e02592eb8394bf2359e9a61e12de557
- evidence_id: adjudication
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/piezophilic-root-adjudication.json
  locator: Final root disposition
  accessed_at: '2026-10-21T20:50:16.252088Z'
  support: supports
  summary: Final severities, fields and nonfindings control this serialization.
  snapshot_sha256: 0c55d6125f75f915a7f6b5fef9a05671f13ea1e2cd2b3439be3894f871c80693
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: fallback identity and synonym scope'
  outcome: supported
  target_ids:
  - traitmech:000001
  summary: Current traitmech preference identity remains distinct from tolerance and
    broader active pressure terms. V5 proposed 1007600 is captured but not an active
    release replacement; no new fallback allocation invoked.
  evidence_ids:
  - record
  - identity
  - metpo-primary
  - proposal-v5-primary
  - target-authority
  - local-authority
  - body-membrane
- assessment_id: definition
  area: evidence
  topic: 'Native checklist: high-pressure preference'
  outcome: supported
  target_ids:
  - traitmech:000001
  summary: Actual assigned review body defines high-pressure preference and distinguishes
    piezotolerance. The generic environmental definition is supported without imposing
    a single quantitative cutoff for all taxa.
  evidence_ids:
  - record
  - sources
  - body-membrane
  - meta-membrane
- assessment_id: hierarchy
  area: identity
  topic: 'Native checklist: current parent and local authorities'
  outcome: supported
  target_ids:
  - traitmech:000001
  summary: Direct phenotype parent and captured v2/v8/v9 terms are assessed on actual
    maintained scope; broad local endpoints do not erase imported RO roles.
  evidence_ids:
  - identity
  - metpo-primary
  - local-authority
  - node-edges
- assessment_id: sources
  area: evidence
  topic: 'Native checklist: all source identities and placements'
  outcome: supported
  target_ids:
  - traitmech:000001
  summary: Five reference forms resolve to four works because the Colwellia DOI and
    PMID are aliases. All seventeen placements have source-specific support or explicit
    uncertainty; source types and indexed abstract versus actual body are distinct.
  evidence_ids:
  - source-ledger
  - placements
  - source-status
  - source-access
- assessment_id: quotations
  area: evidence
  topic: 'Native checklist: literal and unit-format fidelity'
  outcome: concern
  target_ids:
  - traitmech:000001
  summary: First snippet is literal in the actual review body. Colwellia interval/optimum/temperature
    are supported after degrees C to °C normalization, but the supplied snippet is
    not the exact copied format required by policy. Native two NOT_IN_ABSTRACT outcomes
    remain unchanged.
  evidence_ids:
  - snippets
  - body-membrane
  - meta-colwellia
  - playbook
  - native-checks
- assessment_id: canonical
  area: evidence
  topic: 'Native checklist: reported canonical observations'
  outcome: supported
  target_ids:
  - traitmech:000001
  summary: Assigned abstracts support Colwellia MTCD1T high-pressure preference and
    P. profundum SS9 model status. The 2017 most-piezophilic wording is historical,
    not a newly verified ranking. Official taxa positive; full primary bodies were
    not acquired/inspected.
  evidence_ids:
  - canonical-scope
  - meta-colwellia
  - meta-canonical-photobacterium
  - taxon-colwellia
  - taxon-photobacterium
- assessment_id: nodes
  area: consistency
  topic: 'Native checklist: all eight represented facets'
  outcome: supported
  target_ids:
  - traitmech:000001
  summary: Current Pfa node explicitly denotes a protein module, and both chemical
    groups and adaptation/stabilization processes retain their represented meanings.
    One reviewed label-only class is permitted; no copied gene-as-protein or obligatory
    sequence defect.
  evidence_ids:
  - node-edges
  - node-sources
  - schema
  - policy
  - body-piezolytes
  details: '[{"index": 0, "field": "causal_graphs[0].nodes[0]", "current": {"node_id":
    "piezophilic_trait", "label": "piezophilic", "node_type": "TRAIT", "grounding":
    "traitmech:000001", "description": "Optimal growth at hydrostatic pressures well
    above atmospheric."}, "status": "SUPPORTED", "assessment": "Current trait node
    exactly reuses the accepted fallback and explicit optimum-growth concept; broad
    pressure tolerance is not silently substituted."}, {"index": 1, "field": "causal_graphs[0].nodes[1]",
    "current": {"node_id": "high_hydrostatic_pressure", "label": "high hydrostatic
    pressure", "node_type": "ENVIRONMENTAL_FACTOR", "description": "Deep-sea / deep-subsurface
    hydrostatic pressure (tens to >100 MPa)."}, "status": "SUPPORTED_WITH_LIMITATION",
    "assessment": "Environmental condition is a legitimate schema facet; event interpretation
    could be made explicit, but does not cure chemical objects of the imported regulation
    edges."}, {"index": 2, "field": "causal_graphs[0].nodes[2]", "current": {"node_id":
    "unsaturated_branched_fa", "label": "unsaturated / branched-chain fatty acids",
    "node_type": "CHEMICAL", "description": "Membrane lipid species maintaining fluidity
    under high pressure."}, "status": "SUPPORTED", "assessment": "Material fatty-acid
    class is coherent; lack of a single exact chemical accession is not itself a finding."},
    {"index": 3, "field": "causal_graphs[0].nodes[3]", "current": {"node_id": "membrane_adaptation",
    "label": "membrane lipid adaptation", "node_type": "BIOLOGICAL_PROCESS", "description":
    "Lipid composition adjustment maintaining membrane fluidity under HHP."}, "status":
    "SUPPORTED", "assessment": "Explicit lipid-composition adjustment is a process;
    maintaining fluidity is its described functional effect."}, {"index": 4, "field":
    "causal_graphs[0].nodes[4]", "current": {"node_id": "pfa_operon", "grounding_status":
    "REVIEWED_LABEL_ONLY", "grounding_notes": "Reviewed protein family, complex, or
    aggregate; no single semantic family identifier exactly captures this node''s
    represented scope.", "label": "Pfa polyunsaturated-fatty-acid enzyme module",
    "node_type": "GENE_OR_PROTEIN", "description": "Protein module forming an omega-3
    polyunsaturated fatty acid synthase.", "gene_symbols": ["pfaA", "pfaB", "pfaC",
    "pfaD", "pfaE"], "operon": "pfa"}, "status": "SUPPORTED", "assessment": "Actual
    label/description denotes an enzyme protein module. Gene symbols and operon are
    metadata. REVIEWED_LABEL_ONLY and NONMECHANISTIC scope permit zero optional protein
    examples."}, {"index": 5, "field": "causal_graphs[0].nodes[5]", "current": {"node_id":
    "omega3_pufa", "label": "omega-3 polyunsaturated fatty acids", "node_type": "CHEMICAL",
    "description": "Omega-3 PUFAs (e.g. EPA C20:5, DHA C22:6) supporting membrane
    fluidity under HHP."}, "status": "SUPPORTED", "assessment": "PUFA chemical class
    with examples remains material; the imported regulator edges need appropriate
    roles independently of this valid node facet."}, {"index": 6, "field": "causal_graphs[0].nodes[6]",
    "current": {"node_id": "piezolytes", "label": "piezolytes (compatible solutes)",
    "node_type": "CHEMICAL", "description": "Compatible solutes such as glutamate,
    betaine, beta-hydroxybutyrate and TMAO that confer pressure tolerance."}, "status":
    "SUPPORTED", "assessment": "Compatible-solute class is material. No categorical
    inability of a chemical to stabilize a component is inferred."}, {"index": 7,
    "field": "causal_graphs[0].nodes[7]", "current": {"node_id": "pressure_tolerance",
    "label": "pressure tolerance", "node_type": "BIOLOGICAL_PROCESS", "description":
    "Cellular stabilization against high hydrostatic pressure."}, "status": "SUPPORTED_WITH_LIMITATION",
    "assessment": "Cellular stabilization is a defensible process reading despite
    the tolerance label. No automatic CAPACITY/TRAIT retyping is required; its outgoing
    imported relation is independently inconsistent."}]'
- assessment_id: predicates
  area: consistency
  topic: 'Native checklist: all ten relation roles'
  outcome: concern
  target_ids:
  - traitmech:000001
  summary: RO2213 edges 3/5 have explicit chemical objects, which independently conflict
    with the inherited process range; the condition/event subject reading is qualified.
    RO2326 edge 9 uses process to trait rather than material-to-process contribution.
    RO2327 edges 1/6 pass endpoint classes but overstate executor role for structural
    lipid contribution; edge 8 direct stabilization remains qualified positive.
  evidence_ids:
  - node-edges
  - ro-primary
  - local-authority
  - owners
  - challenge
  - adjudication
  details: '[{"index": 0, "field": "causal_graphs[0].edges[0]", "current": {"subject":
    "high_hydrostatic_pressure", "predicate": "selects for", "object": "piezophilic_trait",
    "description": "HHP habitats favor optimal-at-pressure growth phenotype.", "evidence":
    [{"reference": "DOI:10.3389/fmolb.2022.1058381", "notes": "HHP-adapted organisms
    are termed piezophiles for their preference for high pressure."}], "predicate_id":
    "METPO:2007401"}, "subject_type": "ENVIRONMENTAL_FACTOR", "object_type": "TRAIT",
    "status": "SUPPORTED_WITH_LIMITATION", "assessment": "Local v2 selects for has
    environmental-condition to adapted-trait prose and broad node endpoints; current
    shape is eligible. Evolutionary-selection strength remains a source-scope limitation,
    not a fabricated formal error."}, {"index": 1, "field": "causal_graphs[0].edges[1]",
    "current": {"subject": "unsaturated_branched_fa", "predicate": "enables", "object":
    "membrane_adaptation", "description": "Unsaturated and branched-chain fatty acids
    maintain membrane fluidity under HHP.", "evidence": [{"reference": "DOI:10.3389/fmolb.2022.1058381",
    "notes": "Piezophile adaptation involves unsaturated and branched-chain fatty
    acids."}], "predicate_id": "RO:0002327"}, "subject_type": "CHEMICAL", "object_type":
    "BIOLOGICAL_PROCESS", "status": "MINOR_PRECISION", "assessment": "RO2327 material-to-process
    endpoints pass. The subject is a structural lipid constituent maintaining fluidity,
    while the object explicitly denotes composition adjustment; the stronger acts-to-execute
    relation needs role precision. No chemical exclusion or replacement mechanism
    is prescribed."}, {"index": 2, "field": "causal_graphs[0].edges[2]", "current":
    {"subject": "membrane_adaptation", "predicate": "confers", "object": "piezophilic_trait",
    "description": "Membrane lipid adaptation enables high-pressure-optimal growth.",
    "evidence": [{"reference": "DOI:10.1099/ijsem.0.001671", "notes": "Colwellia marinimaniae
    MTCD1 grows optimally at 120 MPa, supported by HHP-adapted membranes."}], "predicate_id":
    "METPO:2007700"}, "subject_type": "BIOLOGICAL_PROCESS", "object_type": "TRAIT",
    "status": "SUPPORTED_WITH_LIMITATION", "assessment": "Local v8 confers explicitly
    permits this biological-process to trait shape. Generic adaptation context does
    not alone establish every optimum or universal necessity."}, {"index": 3, "field":
    "causal_graphs[0].edges[3]", "current": {"subject": "high_hydrostatic_pressure",
    "predicate": "increases", "object": "unsaturated_branched_fa", "description":
    "HHP increases abundance of membrane unsaturated and branched-chain fatty acids.",
    "evidence": [{"reference": "DOI:10.3389/fmolb.2022.1058381", "notes": "The abundance
    of membrane lipids containing unsaturated and branched-chain fatty acids rises
    with increasing HHP."}], "predicate_id": "RO:0002213"}, "subject_type": "ENVIRONMENTAL_FACTOR",
    "object_type": "CHEMICAL", "status": "MAJOR", "assessment": "RO2213 inherits process-to-process
    endpoints through RO2211. The explicit chemical fatty-acid object is not a process;
    the pressure-condition subject is additionally qualified by a possible event reading.
    Increasing abundance is not execution of the chemical entity."}, {"index": 4,
    "field": "causal_graphs[0].edges[4]", "current": {"subject": "pfa_operon", "predicate":
    "produces", "object": "omega3_pufa", "description": "The pfa operon encodes an
    omega-3 polyunsaturated fatty acid synthase enabling PUFA production.", "evidence":
    [{"reference": "DOI:10.3390/microorganisms11071629", "notes": "The pfa operon
    encodes an omega-3 polyunsaturated fatty acid synthase."}], "predicate_id": "METPO:2007800"},
    "subject_type": "GENE_OR_PROTEIN", "object_type": "CHEMICAL", "status": "SUPPORTED",
    "assessment": "Current protein-module subject to chemical product fits the local
    produces definition and maintained gate. The historical pfa identifier is not
    evidence that this current node denotes naked DNA."}, {"index": 5, "field": "causal_graphs[0].edges[5]",
    "current": {"subject": "high_hydrostatic_pressure", "predicate": "increases",
    "object": "omega3_pufa", "description": "HHP increases polyunsaturated fatty acids
    C20:5 (EPA) and C22:6 (DHA) across multiple piezophilic/piezotolerant taxa.",
    "evidence": [{"reference": "DOI:10.3389/fmolb.2022.1058381", "notes": "HHP-driven
    increases in C20:5/C22:6 in Photobacterium profundum SS9, Psychromonas, and Shewanella
    piezotolerans WP3."}], "predicate_id": "RO:0002213"}, "subject_type": "ENVIRONMENTAL_FACTOR",
    "object_type": "CHEMICAL", "status": "MAJOR", "assessment": "RO2213 inherits process-to-process
    endpoints. PUFA molecules are material chemical objects; their increasing abundance
    does not make them processes. Event-versus-condition interpretation of exposure
    cannot cure this object mismatch."}, {"index": 6, "field": "causal_graphs[0].edges[6]",
    "current": {"subject": "omega3_pufa", "predicate": "enables", "object": "membrane_adaptation",
    "description": "Omega-3 PUFAs maintain membrane fluidity, contributing to lipid
    adaptation under HHP.", "evidence": [{"reference": "DOI:10.3389/fmolb.2022.1058381",
    "notes": "Unsaturated/polyunsaturated fatty acids maintain membrane fluidity under
    high pressure."}], "predicate_id": "RO:0002327"}, "subject_type": "CHEMICAL",
    "object_type": "BIOLOGICAL_PROCESS", "status": "MINOR_PRECISION", "assessment":
    "Same bounded executor-versus-structural-contributor precision as edge 1. Material/process
    endpoints fit, while maintaining fluidity differs from directly executing lipid-composition
    adjustment."}, {"index": 7, "field": "causal_graphs[0].edges[7]", "current": {"subject":
    "high_hydrostatic_pressure", "predicate": "induces accumulation of", "object":
    "piezolytes", "description": "HHP is associated with accumulation of compatible
    solutes (piezolytes) such as glutamate, betaine and beta-hydroxybutyrate.", "evidence":
    [{"reference": "DOI:10.3390/microorganisms11071629", "notes": "Compatible solutes
    (piezolytes) detected include glutamate, betaine, and beta-hydroxybutyrate; TMAO
    acts as a pressure-tolerance molecule."}]}, "subject_type": "ENVIRONMENTAL_FACTOR",
    "object_type": "CHEMICAL", "status": "SUPPORTED_WITH_LIMITATION", "assessment":
    "The free predicate has no asserted imported domain/range. Existing association
    wording is assessed as contextual; absence of an identifier is not automatically
    a finding."}, {"index": 8, "field": "causal_graphs[0].edges[8]", "current": {"subject":
    "piezolytes", "predicate": "enables", "object": "pressure_tolerance", "description":
    "Piezolytes stabilize cellular components, conferring tolerance to high hydrostatic
    pressure.", "evidence": [{"reference": "DOI:10.3390/microorganisms11071629", "notes":
    "TMAO and other compatible solutes are highlighted as pressure-tolerance molecules."}],
    "predicate_id": "RO:0002327"}, "subject_type": "CHEMICAL", "object_type": "BIOLOGICAL_PROCESS",
    "status": "SUPPORTED_WITH_LIMITATION", "assessment": "Material solutes to the
    described stabilization process can satisfy the executor reading. Keep this positive/qualified
    case separate from edges 1/6; no categorical chemical exclusion."}, {"index":
    9, "field": "causal_graphs[0].edges[9]", "current": {"subject": "pressure_tolerance",
    "predicate": "contributes to", "object": "piezophilic_trait", "description": "Pressure
    tolerance via piezolytes contributes to optimal growth at high pressure.", "evidence":
    [{"reference": "DOI:10.3390/microorganisms11071629", "notes": "Piezolytes support
    growth and survival under high hydrostatic pressure."}], "predicate_id": "RO:0002326"},
    "subject_type": "BIOLOGICAL_PROCESS", "object_type": "TRAIT", "status": "MAJOR",
    "assessment": "RO2326 inherits material-subject/process-object constraints through
    RO2216/2500/2595. Current cellular-stabilization process subject and phenotype
    trait object do not meet those roles. This does not require changing the valid
    process node into an arbitrary material type."}]'
- assessment_id: biology
  area: evidence
  topic: 'Native checklist: generic environmental scope and limits'
  outcome: unknown
  target_ids:
  - traitmech:000001
  summary: Actual reviews support contextual membrane and microbial compatible-solute
    observations with taxon/temperature/salinity exceptions. No universal necessity
    or tolerance-preference equivalence is inferred. Nearest Colwellia membrane causality
    remains unknown on the inspected abstract; detailed intervention/fitness mechanisms
    are UNASSESSED_SCOPE.
  evidence_ids:
  - edge-sources
  - source-reading
  - source-access
  - body-membrane
  - body-piezolytes
- assessment_id: completeness
  area: completeness
  topic: 'Native checklist: NONMECHANISTIC applicability'
  outcome: supported
  target_ids:
  - traitmech:000001
  summary: One component, a contextual reviewed protein module and two canonical examples
    are compatible with the stated scope. No mandatory extra pathway, connector, accession
    or experimental design.
  evidence_ids:
  - record
  - node-edges
  - policy
  - ground-reading
- assessment_id: expression
  area: evidence
  topic: 'Native checklist: structured catalog applicability'
  outcome: not_applicable
  target_ids:
  - traitmech:000001
  summary: No exact canonical or searched type/model alias in the retained 20-organism/28-dataset
    catalog. Original acquisition is preserved; no substitute organism or downstream
    experiment query.
  evidence_ids:
  - expression
  - authority-reuse
  - taxon-colwellia
  - taxon-photobacterium
- assessment_id: ownership
  area: provenance
  topic: 'Native checklist: exact current and historical writers'
  outcome: supported
  target_ids:
  - traitmech:000001
  summary: Current record and mapping/shared grounder own imported assertions; nonempty
    IDs are skipped. Historical enables migrations and sibling review/repair context
    are not asserted to repair current relations automatically.
  evidence_ids:
  - owners
  - ground-reading
  - local-authority
- assessment_id: human
  area: provenance
  topic: 'Native checklist: bounded attributable acceptance'
  outcome: concern
  target_ids:
  - traitmech:000001
  summary: Seven current events are all AI; three captured sibling AI histories are
    not direct acceptance of this target. Ignored-inclusive 203 paths/67 parsed arrays/zero
    exact targets bound the traceability concern; private or remote review is not
    ruled out.
  evidence_ids:
  - owners
  - ground-reading
  - playbook
  - challenge
  - adjudication
- assessment_id: readiness
  area: consistency
  topic: 'Native checklist: actual checks and chronology'
  outcome: supported
  target_ids:
  - traitmech:000001
  summary: All final 68 inputs and original66 bytes match. Native/strict and network
    snippet retry passed; initial snippet DNS failure retained as superseded optional
    check. Body DNS failure/retry is separate. Qualified common original outcomes
    and B10 QC retain their times.
  evidence_ids:
  - capture-initial
  - capture-final
  - source-capture
  - reuse
  - reuse-postcheck
  - native-checks
  - source-body-failure
  - source-body-retry
  - check-piezophilic-native
  - check-piezophilic-strict
  - check-piezophilic-snippets-retry-network
findings:
- finding_id: imported-relation-roles
  issue_key: piezophilic-imported-relation-roles
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Imported process-regulation and contribution roles conflict with current
    referents
  description: RO2213 edges 3/5 inherit a process range but have explicit chemical
    products as objects, an independently decisive conflict. The high-pressure condition/event
    subject reading remains qualified; the enum alone is not an automatic prohibition.
    RO2326 edge 9 inherits material-to-process contribution roles but links the stabilization
    process to a preference trait. This is one grouped representation concern, not
    a false-pressure-biology finding.
  target_ids:
  - traitmech:000001
  field_paths:
  - causal_graphs[0].edges[3]
  - causal_graphs[0].edges[5]
  - causal_graphs[0].edges[9]
  evidence_ids:
  - node-edges
  - ro-primary
  - schema
  - owners
  - challenge
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/piezophilic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Current grounded role rows; wildcard assignment does not waive imported
      semantics.
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Nonempty current predicate IDs are skipped; mapping change alone does not
      rewrite them.
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: enabling-role-precision
  issue_key: piezophilic-enabling-role-precision
  category: consistency
  severity: minor
  status: open
  certainty: confirmed
  title: Structural lipid contribution is described as direct enabling
  description: RO2327 edges 1/6 satisfy material/process endpoints, but the represented
    lipids are structural contributors to membrane adaptation rather than clearly
    identified direct executors of that process. This bounded semantic precision concern
    does not assert false physiology or extend automatically to edge 8 stabilization.
  target_ids:
  - traitmech:000001
  field_paths:
  - causal_graphs[0].edges[1]
  - causal_graphs[0].edges[6]
  evidence_ids:
  - node-edges
  - ro-primary
  - edge-sources
  - body-membrane
  - owners
  - challenge
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/piezophilic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Current grounded role rows; wildcard assignment does not waive imported
      semantics.
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Nonempty current predicate IDs are skipped; mapping change alone does not
      rewrite them.
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: literal-unit-format
  issue_key: piezophilic-literal-unit-format
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Snippet changes source unit notation
  description: The current Colwellia snippet spells degrees C where the actual source
    abstract uses °C. Normalization preserves interval, optimum and temperature completely;
    the finding is only literal copied-span format under maintained policy.
  target_ids:
  - traitmech:000001
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
    path: data/traits/environment/piezophilic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: human-acceptance-link
  issue_key: piezophilic-human-acceptance-link
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Current provenance lacks an attributable acceptance link
  description: Seven AI events and three sibling AI histories do not identify linked
    current human acceptance. Ignored-inclusive 203 paths/67 parsed arrays/zero exact
    target arrays bound this concern; no claim about private or remote review.
  target_ids:
  - traitmech:000001
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
    path: data/traits/environment/piezophilic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
actions:
- action_id: reconcile-imported-roles
  description: Reconcile imported predicates with the represented condition, chemical,
    process and trait referents during authorized curation.
  finding_ids:
  - imported-relation-roles
  target_ids:
  - traitmech:000001
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/piezophilic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Current grounded role rows; wildcard assignment does not waive imported
      semantics.
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Nonempty current predicate IDs are skipped; mapping change alone does not
      rewrite them.
  acceptance_checks:
  - Preserve positive environmental observations and source-specific limits.
  - Respect current nonempty-ID guards and exact owner selectors; no automatic sibling
    rewrite.
  - No new mechanism, experiment, optimized condition or mandatory protein instance.
- action_id: clarify-enabling-role
  description: Clarify direct executor versus structural lipid contribution at the
    two bounded edges.
  finding_ids:
  - enabling-role-precision
  target_ids:
  - traitmech:000001
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/piezophilic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Current grounded role rows; wildcard assignment does not waive imported
      semantics.
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Nonempty current predicate IDs are skipped; mapping change alone does not
      rewrite them.
  acceptance_checks:
  - Retain positive lipid/fluidity evidence and compatible endpoint classes.
  - Do not extend the concern to edge 8 without its own evidence.
- action_id: restore-literal-unit-format
  description: Use the actual source unit notation for the existing supported snippet.
  finding_ids:
  - literal-unit-format
  target_ids:
  - traitmech:000001
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/piezophilic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Preserve all numeric values, temperature and source identity.
  - Keep interpretation and historical superlative scope in notes.
- action_id: link-human-acceptance
  description: Link attributable current acceptance if available or clarify status
    while retaining provenance.
  finding_ids:
  - human-acceptance-link
  target_ids:
  - traitmech:000001
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/piezophilic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Preserve all seven AI events and bounded sibling-history/search evidence.
  - No contact or automatic status promotion authorized.
limitations:
- Detailed pathogen fitness/defense/AMR, intervention efficacy and experimental or
  optimized conditions are UNASSESSED_SCOPE. Incidental displayed respiratory/mutant/control/future-method
  paragraphs are not adopted.
- Actual membrane and piezolyte reviews contain taxon-specific exceptions and pressure/temperature/salinity
  confounding. Current contextual graph is not read as universal necessity or every-taxon/every-lipid
  assertion.
- Tolerance differs from preferred-pressure growth. Contributes-to wording is not
  interpreted as equivalence or sufficient classification; formal imported-role defects
  are assessed independently.
- Colwellia and Photobacterium primary bodies were not acquired/inspected. Their actual
  assigned abstracts support current canonical observations, but Colwellia membrane
  causality remains unknown at its nearest citation. No fresh failed canonical-body
  request or paper-wide absence is claimed.
- The most-piezophilic superlative is explicitly the 2017 source statement; no independently
  current global ranking or evidence of surpassing it is asserted.
- Microbial TMAO context is explicit in the assigned review; no eukaryote-to-microbe
  transfer finding. Pressure-specific solute accumulation differs among taxa.
- Current Pfa protein module is coherent; its pressure versus cold association remains
  qualified without evaluating intervention efficacy or adding accessions.
- Retained fallback identity is not a fresh mint. Deprecated labels and proposed 1007600
  do not establish an active exact imported replacement.
- Initial 66 capture preceded source judgment; final 68 adds v5 authority before final
  judgment and retains initial bytes. Native snippet DNS failure/retry and separate
  body DNS failure/retry remain distinct.
- Original membrane 16:07 and Colwellia taxonomy 16:11 acquisitions remain separate
  from current 20:42metadata,20:43body,20:44taxonomy, copies and readings. Three whole
  sibling-history readings belong to grounding; root/source scopes are separately
  attributed.
notes:
- Final root adjudication and independent challenge are pinned and verified. Author
  preparation did not import or execute the serializer; root owns later single execution,
  native validation and save.
- 'Coverage: four distinct works/five forms, seventeen external placements, eight
  nodes/ten edges, two canonicals, two snippets: one literal and one supported unit
  transcription.'
- No scientific record, native inventory, Git or sweep state mutation by serializer
  preparation.
tags:
- record-review
- piezophilic
- environment
- needs-curation
native_verdict: needs_curation
```
