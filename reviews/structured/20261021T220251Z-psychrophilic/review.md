# Whole-record review of psychrophilic

- Review: 20261021T220251Z-psychrophilic
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-21T21:53:42.109453Z
- Finished UTC: 2026-10-21T22:02:51Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Needs curation: two major representation issues for imported process roles and reversed stability polarity, plus a bounded human-acceptance traceability minor.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: Fifth record of the actual locally initialized batch 012 queue. Whole 330-line target and all 86 captured inputs verified before assessment. Local initialization at 21:02:18.445284 UTC does not assert publication of batch 011.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8eee04a8c65609fbaff6df7c54597dcaf1b9d282.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| METPO:1000614 | data/traits/environment/psychrophilic.yaml | maintained | psychrophilic |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full-corpus graph audit | passed | True | METPO:1000614 | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| Full-corpus snippet audit | passed | True | METPO:1000614 | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| Full-corpus pathway links | passed | True | METPO:1000614 | 19 links checked against the pinned PathwayMech snapshot. |
| Full-corpus history integrity | passed | True | METPO:1000614 | 1277 history records checked, zero invalid links at the 8eee source base; integrity does not establish science or human acceptance. |
| Initial full-product validation | failed | False | METPO:1000614 | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation with isolated local cache | failed | False | METPO:1000614 | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation after isolated-cache download | passed | True | METPO:1000614 | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| Focused native validation | passed | True | METPO:1000614 | Successful schema validation; source and semantics separately assessed. |
| Focused strict validation | passed | True | METPO:1000614 | Successful strict validation; no biological efficacy certification. |
| Focused network snippet check | passed | True | METPO:1000614 | Direct network invocation passed: eight fields over four references, four VERIFIED and four NOT_IN_ABSTRACT. Manual audit found seven literal spans and one PDF typography normalization; no current initial failed snippet attempt. |
| Reused maintained batch-eleven QC | passed | True | METPO:1000614 | Actual B11 final QC at its original time, qualified against B12 bytes; independent of pending publication. |
| Protein-instance metadata applicability | not_applicable | False | METPO:1000614 | Three reviewed label-only protein classes and zero instances in a NONMECHANISTIC graph; no forced accession or detailed cold-response query. |

## Scientific And Domain Assessments

### Native checklist: active preference identity and groundings

identity: supported. Targets: METPO:1000614.

Active METPO1000614 and direct parent1000613 match the current qualified low-temperature preference. Deprecated predecessors and neighboring numeric bins are distinguished; no exact-alias conflation is asserted. PATO cold condition, local membrane quality and CHEBI solute/ROS identities are meaningful.

### Native checklist: generic low-temperature preference

evidence: supported. Targets: METPO:1000614.

Current definition is a qualified preference, not a universal numerical cutoff. The author review uses a broad near-freezing classification; the approximate 15 °C criterion is not directly calibrated by that passage. Ontology wording is positive without upgrading source scope to a precise threshold or efficacy claim.

### Native checklist: direct parent and local relation semantics

identity: supported. Targets: METPO:1000614.

Active temperature-preference parent is appropriate. Exact local selects-for and confers are compatible with current condition-to-trait and protein-class-to-trait uses. They do not silently inherit imported RO process requirements.

### Native checklist: all assigned citations and placements

evidence: unknown. Targets: METPO:1000614.

Assigned bibliographic identities, generic classification and selected literal passages are assessed within the frozen source ledger. Inaccessible bodies and excluded detailed efficacy are not interpreted as false claims or absent statements.

{"completed_at": "2026-10-21T21:59:18.963759+00:00", "nodes": [{"index": 0, "node_id": "psychrophilic_trait", "label": "psychrophilic", "node_type": "TRAIT", "grounding": "METPO:1000614", "assessment": "Broad environmental classification, supported by assigned author definition; exact 15 °C approximation qualified."}, {"index": 1, "node_id": "low_temperature", "label": "low temperature", "node_type": "ENVIRONMENTAL_FACTOR", "grounding": "PATO:0001306", "assessment": "Generic environmental cold condition; physical context supported without operational interpretation."}, {"index": 2, "node_id": "membrane_fluidity", "label": "membrane fluidity", "node_type": "QUALITY", "grounding": "METPO:1007505", "assessment": "Generic membrane physical state; detailed causal efficacy excluded and ontology role audit separate."}, {"index": 3, "node_id": "unsaturated_fatty_acids", "label": "unsaturated and branched-chain fatty acids", "node_type": "CHEMICAL", "grounding": null, "assessment": "Generic lipid context supported by assigned annual abstract and author review; no universal structural requirement inferred."}, {"index": 4, "node_id": "cold_adapted_enzymes", "label": "cold-adapted enzymes", "node_type": "GENE_OR_PROTEIN", "grounding": null, "assessment": "Cold-active enzyme category and omics literal context only; detailed efficacy unassessed."}, {"index": 5, "node_id": "cold_shock_proteins", "label": "cold-shock proteins", "node_type": "GENE_OR_PROTEIN", "grounding": null, "assessment": "Cold-shock class literal source mention positive; detailed cold-defense efficacy unassessed."}, {"index": 6, "node_id": "antifreeze_proteins", "label": "antifreeze and ice-binding proteins", "node_type": "GENE_OR_PROTEIN", "grounding": null, "assessment": "AFP/ice-binding category literal source association positive; detailed defense efficacy unassessed."}, {"index": 7, "node_id": "transcription_translation", "label": "transcription and translation", "node_type": "BIOLOGICAL_PROCESS", "grounding": null, "assessment": "Process names explicit in current record; detailed mechanism unassessed."}, {"index": 8, "node_id": "compatible_solutes", "label": "compatible solutes", "node_type": "CHEMICAL", "grounding": "CHEBI:25728", "assessment": "Generic solute category citation identity positive; exact cross-taxon list/efficacy not established by inspected nearest text."}, {"index": 9, "node_id": "trehalose", "label": "trehalose", "node_type": "CHEMICAL", "grounding": null, "assessment": "Existing trehalose source note literal verified only; no efficacy endorsement."}, {"index": 10, "node_id": "protein_membrane_stability", "label": "protein and membrane stability", "node_type": "QUALITY", "grounding": null, "assessment": "Current stability referent is explicit; incoming prevents edge reverses its positive state wording."}, {"index": 11, "node_id": "ice_crystals", "label": "ice crystals", "node_type": "CHEMICAL", "grounding": null, "assessment": "Ice material referent explicit; literal source association only."}, {"index": 12, "node_id": "reactive_oxygen_species", "label": "reactive oxygen species", "node_type": "CHEMICAL", "grounding": "CHEBI:26523", "assessment": "Detailed ROS concentration/generation biology unassessed; formal node/edge roles separate."}], "edges": [{"index": 0, "subject": "low_temperature", "predicate": "selects for", "object": "psychrophilic_trait", "reference": "DOI:10.1038/sj.embor.7400662", "outcome": "qualified_support", "assessment": "Generic low-temperature classification is supported by the assigned definition passage; selection is broad contextual language, not an exclusive mechanism."}, {"index": 1, "subject": "low_temperature", "predicate": "decreases", "object": "membrane_fluidity", "reference": "DOI:10.1038/sj.embor.7400662", "outcome": "supported_generic_context", "assessment": "Assigned abstract and generic membrane passage describe decreased membrane fluidity as a cold physical challenge; formal relation roles are separate."}, {"index": 2, "subject": "unsaturated_fatty_acids", "predicate": "regulates", "object": "membrane_fluidity", "reference": "DOI:10.1146/annurev-micro-091313-103612", "outcome": "qualified_support", "assessment": "Nearest annual-review abstract supports more unsaturated fatty acids and homeoviscous context. Detailed cross-taxon efficacy and every branched-chain component are not separately validated; no universal assertion inferred."}, {"index": 3, "subject": "cold_adapted_enzymes", "predicate": "confers", "object": "psychrophilic_trait", "reference": "DOI:10.1016/j.tim.2010.05.002", "outcome": "UNASSESSED_SCOPE", "assessment": "Exact omics phrase is verified in the abstract. Detailed enzyme mechanism/sufficiency is outside scope; generic association does not establish universal necessity."}, {"index": 4, "subject": "cold_shock_proteins", "predicate": "contributes to", "object": "psychrophilic_trait", "reference": "DOI:10.1038/sj.embor.7400662", "outcome": "UNASSESSED_SCOPE", "assessment": "Exact Cold-shock proteins sentence verified after PDF line-break dehyphenation; detailed fitness/acclimation efficacy unassessed."}, {"index": 5, "subject": "antifreeze_proteins", "predicate": "protects against", "object": "low_temperature", "reference": "DOI:10.1038/sj.embor.7400662", "outcome": "UNASSESSED_SCOPE", "assessment": "Exact intracellular ice formation phrase in source abstract; literal AFP/ice association is present in author review, detailed defense efficacy unassessed."}, {"index": 6, "subject": "cold_shock_proteins", "predicate": "regulates", "object": "transcription_translation", "reference": "DOI:10.1002/embr.201338170", "outcome": "UNASSESSED_SCOPE", "assessment": "Citation identity positive; assigned detailed transcription/translation note not independently body-verified. Initial source routes returned error/help/metadata-only/preview, not a demonstrated false claim."}, {"index": 7, "subject": "trehalose", "predicate": "prevents", "object": "protein_membrane_stability", "reference": "DOI:10.1038/sj.embor.7400662", "outcome": "internal_polarity_conflict", "assessment": "Current predicate/object prevents stability reverses current description and source-attributed note about preventing denaturation/aggregation. This documentary sign conflict is independent of detailed efficacy and independent of formal RO endpoints."}, {"index": 8, "subject": "compatible_solutes", "predicate": "maintains", "object": "protein_membrane_stability", "reference": "DOI:10.37256/amtt.5220244537", "outcome": "unknown", "assessment": "Crossref identity/abstract supports general review context; exact ellipsis-bearing note and nearest-source specificity unverified because no inspected full body. Detailed cryoprotection efficacy unassessed."}, {"index": 9, "subject": "antifreeze_proteins", "predicate": "binds to", "object": "ice_crystals", "reference": "DOI:10.1038/sj.embor.7400662", "outcome": "literal_attribution_supported_scope_limited", "assessment": "Author PDF selected AFP paragraph contains the literal bind-to-ice statement; no further mechanism or effectiveness claim assessed."}, {"index": 10, "subject": "low_temperature", "predicate": "increases", "object": "reactive_oxygen_species", "reference": "DOI:10.1002/embr.201338170", "outcome": "UNASSESSED_SCOPE", "assessment": "Assigned review identity is positive; actual detailed ROS-generation/defense note unassessed and not independently body-verified. No inferred paper-wide absence or efficacy conclusion."}], "scope": "Source identity, literal attribution, generic environmental classification and non-operational physical context only. Detailed pathogen cold-survival/fitness, ROS-defense, AMR, vector manipulation, interventions and mechanistic efficacy are UNASSESSED_SCOPE. Incidental displayed text is not adopted as a mechanism assessment."}

### Native checklist: native and manual copied-span coverage

evidence: supported. Targets: METPO:1000614.

Eight snippets have seven literal matches and one PDF line-break typography normalization, without omitted words or a meaning change. Native results remain four VERIFIED and four NOT_IN_ABSTRACT; body review supplies additional attribution without rewriting those results.

### Native checklist: Colwellia strain and named Psychrobacter exemplar

evidence: supported. Targets: METPO:1000614.

Taxon 167879 identifies Colwellia psychrerythraea 34H at strain rank. Actual assigned primary Introduction supports active growth at and below zero, beyond survival alone; extrapolated minimum and motility are not growth measurements. Named Psychrobacter sp. DAB_AL43B remains a different organism context. The taxonomy category misspelling is not copied as a strain alias.

### Native checklist: all thirteen current referents

consistency: supported. Targets: METPO:1000614.

The cold condition, membrane/stability qualities, chemical classes, protein aggregates and transcription/translation process retain their stated facets. Activity wording does not turn enzyme or cold-shock protein classes into processes. No forced protein instance, connector, retype or new identifier is required.

[{"index": 0, "node": {"node_id": "psychrophilic_trait", "label": "psychrophilic", "node_type": "TRAIT", "grounding": "METPO:1000614", "description": "Growth is favored at low temperatures."}, "assessment": "supported", "reason": "Active self-grounded low-temperature growth preference."}, {"index": 1, "node": {"node_id": "low_temperature", "label": "low temperature", "node_type": "ENVIRONMENTAL_FACTOR", "description": "Cold environment near the freezing point of water.", "grounding": "PATO:0001306"}, "assessment": "supported", "reason": "Low-temperature environment is a condition close-matching the PATO temperature quality, not an explicit cooling/exposure process."}, {"index": 2, "node": {"node_id": "membrane_fluidity", "label": "membrane fluidity", "node_type": "QUALITY", "description": "Physical state of the membrane needed for transport and growth.", "grounding": "METPO:1007505"}, "assessment": "supported", "reason": "Physical membrane fluidity is a QUALITY; local v3 definition and maintained schema agree. Its maintenance is a distinct process."}, {"index": 3, "node": {"node_id": "unsaturated_fatty_acids", "label": "unsaturated and branched-chain fatty acids", "node_type": "CHEMICAL", "description": "Membrane lipid features that reduce packing order and maintain fluidity at low temperature."}, "assessment": "supported", "reason": "Unsaturated/branched-chain fatty acids are material lipid constituents; label aggregates features without asserting a single molecular species."}, {"index": 4, "node": {"node_id": "cold_adapted_enzymes", "grounding_status": "REVIEWED_LABEL_ONLY", "grounding_notes": "Reviewed protein family, complex, or aggregate; no single semantic family identifier exactly captures this node's represented scope.", "label": "cold-adapted enzymes", "node_type": "GENE_OR_PROTEIN", "description": "Enzymes with activity at low temperature, often associated with increased structural flexibility."}, "assessment": "supported", "reason": "Cold-adapted enzymes are a taxon-agnostic protein aggregate, explicitly REVIEWED_LABEL_ONLY with rationale. No gene-as-protein or mandatory single accession issue."}, {"index": 5, "node": {"node_id": "cold_shock_proteins", "grounding_status": "REVIEWED_LABEL_ONLY", "grounding_notes": "Reviewed protein family, complex, or aggregate; no single semantic family identifier exactly captures this node's represented scope.", "label": "cold-shock proteins", "node_type": "GENE_OR_PROTEIN", "description": "Proteins induced during cold shock or cold acclimation."}, "assessment": "supported", "reason": "Cold-shock proteins are a material protein class, not the regulatory activity they may perform. Label-only rationale is explicit."}, {"index": 6, "node": {"node_id": "antifreeze_proteins", "grounding_status": "REVIEWED_LABEL_ONLY", "grounding_notes": "Reviewed protein family, complex, or aggregate; no single semantic family identifier exactly captures this node's represented scope.", "label": "antifreeze and ice-binding proteins", "node_type": "GENE_OR_PROTEIN", "description": "Proteins that mitigate ice formation or recrystallization damage."}, "assessment": "supported", "reason": "Antifreeze/ice-binding proteins are a protein aggregate, explicitly reviewed label-only; no forced accession or efficacy conclusion."}, {"index": 7, "node": {"node_id": "transcription_translation", "label": "transcription and translation", "node_type": "BIOLOGICAL_PROCESS", "description": "Macromolecular synthesis processes impaired by cold-induced nucleic-acid secondary structure."}, "assessment": "supported", "reason": "Transcription and translation are explicitly macromolecular synthesis processes; no molecular-activity versus material ambiguity required."}, {"index": 8, "node": {"node_id": "compatible_solutes", "label": "compatible solutes", "node_type": "CHEMICAL", "description": "Low-molecular-weight osmolytes (e.g. trehalose, glycine betaine, glycerol) accumulated for cryoprotection.", "grounding": "CHEBI:25728"}, "assessment": "qualified_positive", "reason": "Compatible solutes are named chemical solutes with CHEBI osmolyte closeMatch; no single molecule identity is asserted and detailed cryoprotection is unassessed."}, {"index": 9, "node": {"node_id": "trehalose", "label": "trehalose", "node_type": "CHEMICAL", "description": "Disaccharide cryoprotectant with colligative and protein-stabilizing effects."}, "assessment": "supported", "reason": "Trehalose is a chemical referent; lack of a CURIE alone is not a mandatory defect."}, {"index": 10, "node": {"node_id": "protein_membrane_stability", "label": "protein and membrane stability", "node_type": "QUALITY", "description": "Structural integrity of proteins and membranes maintained against cold denaturation."}, "assessment": "supported", "reason": "Structural integrity/stability is a positive measurable QUALITY, not denaturation or aggregation."}, {"index": 11, "node": {"node_id": "ice_crystals", "label": "ice crystals", "node_type": "CHEMICAL", "description": "Intracellular/extracellular ice whose growth and recrystallization damage cells."}, "assessment": "supported", "reason": "Ice crystals are a material chemical water phase; no forced ontology grounding or detailed ice-damage assessment."}, {"index": 12, "node": {"node_id": "reactive_oxygen_species", "label": "reactive oxygen species", "node_type": "CHEMICAL", "description": "ROS whose concentration rises at low temperature due to increased gas solubility.", "grounding": "CHEBI:26523"}, "assessment": "supported", "reason": "Named ROS chemical class matches CHEBI26523; concentration/biological effects are not evaluated in this grounding audit."}]

### Native checklist: all eleven relation roles and signed meaning

consistency: concern. Targets: METPO:1000614.

Group RO role conflicts at edges 1/2/4/6/7/10. Regulation has explicit process endpoints; contributes-to permits its protein subject but not the trait object. Edge 7 also independently negates positive structural integrity while its prose concerns preventing damage. Root/challenge count that sign reversal as a separate major; the grounding auditor favored a minor. Three lexical edges and compatible local relations remain qualified positives.

[{"index": 0, "edge": {"subject": "low_temperature", "predicate": "selects for", "object": "psychrophilic_trait", "description": "Permanently cold environments select for microorganisms able to grow near freezing.", "evidence": [{"reference": "DOI:10.1038/sj.embor.7400662", "snippet": "growing well at temperatures around the freezing point", "notes": "Review supports psychrophile growth in near-freezing environments."}], "predicate_id": "METPO:2007401"}, "assessment": "supported", "reason": "Exact local selects-for relates environmental condition to adapted trait; no imported RO process-domain restriction and no assertion of detailed selection efficacy."}, {"index": 1, "edge": {"subject": "low_temperature", "predicate": "decreases", "object": "membrane_fluidity", "description": "Cold reduces membrane fluidity, altering transport and waste exchange.", "evidence": [{"reference": "DOI:10.1038/sj.embor.7400662", "snippet": "decreased membrane fluidity", "notes": "Supports membrane rigidification as a low-temperature challenge."}], "predicate_id": "RO:0002212"}, "assessment": "major", "reason": "RO2212 inherits RO2211 process/process constraints. Explicit low-temperature condition/PATO quality to membrane-fluidity QUALITY does not denote two processes. The fluidity object independently suffices; no blanket ENVIRONMENTAL_FACTOR prohibition."}, {"index": 2, "edge": {"subject": "unsaturated_fatty_acids", "predicate": "regulates", "object": "membrane_fluidity", "description": "Unsaturated and branched-chain fatty acids maintain membrane fluidity during cold growth.", "evidence": [{"reference": "DOI:10.1146/annurev-micro-091313-103612", "snippet": "more unsaturated fatty acids", "notes": "Review supports homoviscous membrane adaptation as temperature decreases."}], "predicate_id": "RO:0002211"}, "assessment": "major", "reason": "RO2211 regulates connects material fatty-acid constituents to fluidity QUALITY, not process to process."}, {"index": 3, "edge": {"subject": "cold_adapted_enzymes", "predicate": "confers", "object": "psychrophilic_trait", "description": "Cold-active enzymes support catalysis at low temperature.", "evidence": [{"reference": "DOI:10.1016/j.tim.2010.05.002", "snippet": "genes involved in cold adaptation", "notes": "Review connects psychrophile omics signatures with cold-adaptation mechanisms."}], "predicate_id": "METPO:2007700"}, "assessment": "supported", "reason": "Local v8 confers and maintained mapping102 admit a protein class as subject and TRAIT as object. Formal compatibility does not validate detailed enzyme efficacy."}, {"index": 4, "edge": {"subject": "cold_shock_proteins", "predicate": "contributes to", "object": "psychrophilic_trait", "description": "Cold-shock proteins support cellular acclimation to low temperature.", "evidence": [{"reference": "DOI:10.1038/sj.embor.7400662", "snippet": "Cold-shock proteins have also been described", "notes": "Supports cold-shock proteins as psychrophile-associated adaptations."}], "predicate_id": "RO:0002326"}, "assessment": "major", "reason": "RO2326 inherits material/process roles through2216/2500/2595. Protein subject is material and fits; psychrophilic TRAIT object is not the required process. Do not falsely reject its protein subject."}, {"index": 5, "edge": {"subject": "antifreeze_proteins", "predicate": "protects against", "object": "low_temperature", "description": "Antifreeze and ice-binding proteins mitigate ice-associated stress in cold habitats.", "evidence": [{"reference": "DOI:10.1038/sj.embor.7400662", "snippet": "intracellular ice formation", "notes": "Review identifies ice formation as a cold challenge and cites bacterial antifreeze protein activity."}]}, "assessment": "lexical_qualified", "reason": "Ungrounded protects-against carries no imported RO endpoint constraint. Generic wording spans ice-associated stress rather than temperature itself; detailed protection efficacy remains unassessed, no separate mandatory grounding finding."}, {"index": 6, "edge": {"subject": "cold_shock_proteins", "predicate": "regulates", "object": "transcription_translation", "description": "Cold-shock proteins regulate transcription and translation during cold acclimation.", "evidence": [{"reference": "DOI:10.1002/embr.201338170", "notes": "cold-shock proteins (CSPs) regulate a variety of cellular processes, including transcription, translation."}], "predicate_id": "RO:0002211"}, "assessment": "major", "reason": "RO2211 process/process regulation has material cold-shock protein class subject, while transcription/translation object is valid process. Protein activity cannot silently replace the represented protein referent."}, {"index": 7, "edge": {"subject": "trehalose", "predicate": "prevents", "object": "protein_membrane_stability", "description": "Trehalose helps prevent protein denaturation and aggregation, acting as a cryoprotectant.", "evidence": [{"reference": "DOI:10.1038/sj.embor.7400662", "notes": "Trehalose is thought to have a colligative effect, but probably also helps in preventing protein denaturation and aggregation."}], "predicate_id": "RO:0002212"}, "assessment": "major_plus_minor_polarity", "reason": "RO2212 process/process relation connects trehalose CHEMICAL to positive stability QUALITY, contributing to the grouped formal issue. Independently, literal prevents points to stability whereas description/notes concern preventing denaturation/aggregation; bounded predicate/object polarity inconsistency. Intended supportive effect is explicit, so independently calibrated minor rather than a second formal major."}, {"index": 8, "edge": {"subject": "compatible_solutes", "predicate": "maintains", "object": "protein_membrane_stability", "description": "Compatible solutes depress the freezing point and stabilize proteins and membranes.", "evidence": [{"reference": "DOI:10.37256/amtt.5220244537", "notes": "Compatible solutes depress the freezing point... stabilize proteins and membranes."}]}, "assessment": "lexical_qualified", "reason": "Ungrounded maintains links compatible-solute chemicals with positive stability quality; no imported RO constraint. Detailed stabilization or fitness efficacy unassessed."}, {"index": 9, "edge": {"subject": "antifreeze_proteins", "predicate": "binds to", "object": "ice_crystals", "description": "Antifreeze/ice-binding proteins bind ice crystals to control ice growth and recrystallization.", "evidence": [{"reference": "DOI:10.1038/sj.embor.7400662", "notes": "Antifreeze proteins (AFPs) have the ability to bind to ice crystals."}]}, "assessment": "lexical_qualified", "reason": "Ungrounded binds-to has protein and ice material referents. Formal molecular binding wording is intelligible; no new interaction mechanism or efficacy reconstruction."}, {"index": 10, "edge": {"subject": "low_temperature", "predicate": "increases", "object": "reactive_oxygen_species", "description": "Increased gas solubility at low temperature raises reactive oxygen species concentrations.", "evidence": [{"reference": "DOI:10.1002/embr.201338170", "notes": "The solubility of gases increases at lower temperatures, resulting in increased concentrations of reactive oxygen species."}], "predicate_id": "RO:0002213"}, "assessment": "major", "reason": "RO2213 inherits process/process roles; explicit low-temperature condition/PATO quality to ROS CHEMICAL object is not process to process. The chemical object is independently decisive; no inference about physiological ROS concentration correctness."}]

### Native checklist: generic context and excluded detailed efficacy

scope: unknown. Targets: METPO:1000614.

Formal types and the internal direction of an assertion can be reviewed while detailed cold-survival, fitness, ROS-defense, AMR and intervention mechanisms remain UNASSESSED_SCOPE. Source-specific generic context remains separate from such efficacy claims; no repaired mechanism or experiment is prescribed.

### Native checklist: NONMECHANISTIC applicability

completeness: supported. Targets: METPO:1000614.

Two disclosed components, three reviewed label-only protein classes and zero instances are proportionate to this contextual graph. No mandatory connector, molecular instance, additional canonical organism or experiment is prescribed.

### Native checklist: catalog applicability and bounded query scope

evidence: unknown. Targets: METPO:1000614.

Exact Colwellia 34H and named Psychrobacter exemplar aliases do not match the retained 20-organism / 28-dataset catalog. Other source organisms can be covered; no global absence is asserted. No strain-resolved locus or detailed stress-response gene/module query was run.

### Native checklist: current assertions and conditional writers

provenance: supported. Targets: METPO:1000614.

Record owns current assertions and polarity. Shared predicate mappings fill empty IDs and preserve current nonempty values. The fluidity normalizer already agrees with current QUALITY; the trait-enables migration selects RO2327, not current RO2326. Sibling temperature/free-living histories and writers do not own this record. No exact current canonical-backfill entry was established.

### Native checklist: bounded acceptance trace

provenance: concern. Targets: METPO:1000614.

Nineteen embedded events include eighteen AI events and an automated seed. All six complete repository histories are contextual AI records; ignored-inclusive 216 matching paths and 67 structured review target arrays contain zero exact current targets. This bounds the missing acceptance link without ruling out private or remote review.

### Native checklist: actual checks and local preparation

consistency: supported. Targets: METPO:1000614.

All 86 captured inputs match. Native, strict and direct network snippet commands pass; initial taxonomy DNS failure is separately retained from its successful retry. Historical common failures/retries remain explicit. Actual prior QC, byte qualification and local initialization do not assert B11 remote publication.

## Findings

### imported-process-roles: Imported process relations conflict with current endpoint referents

major / open / confirmed; issue key: psychrophilic-imported-process-roles.

RO2211/2212/2213 require process endpoints. Current edges 1/2/6/7/10 instead include explicitly grounded cold condition, physical qualities or chemical/protein materials. RO2326 at edge 4 permits the material protein subject but inherits a process object, unlike the current trait. Group these six role conflicts, preserving valid node facets and generic context; do not infer a categorical ban on environmental nodes.

### stability-polarity: Negative relation targets the positive stability outcome

major / open / confirmed; issue key: psychrophilic-stability-polarity.

Edge 7 points a negative predicate at protein/membrane stability, explicitly defined as positive structural integrity, while its description and note concern preventing denaturation and aggregation. This reverses the machine-readable signed assertion independently of the imported endpoint problem. Root/challenger calibrate it as major; the ground auditor favored a bounded minor because the intended meaning is explicit. No biological intervention or replacement mechanism is prescribed.

### human-acceptance-link: Reviewed status lacks a locally attributable acceptance link

minor / open / confirmed; issue key: psychrophilic-human-acceptance-link.

Eighteen AI events and an automated seed, six contextual AI histories, and ignored-inclusive 216 paths/67 parsed target arrays/zero exact targets do not identify current-target human acceptance. This bounded traceability gap does not exclude private or remote review.

## Recommended Actions And Acceptance Checks

### reconcile-imported-roles

Reconcile the six imported relation-role mismatches during authorized curation.

- Preserve valid current node facets and compatible local/lexical relation semantics.
- Respect nonempty-ID guards; mapping changes alone do not repair current assertions.
- No detailed mechanism reconstruction or intervention prescription.

### reconcile-stability-sign

Reconcile the edge-7 signed assertion with its explicit intended stability meaning.

- Address signed predicate/object meaning separately from imported endpoint roles.
- Preserve the independent severity calibration and source attribution.
- No new efficacy claim, assay or operational mechanism repair.

### link-human-acceptance

Link attributable acceptance if available or clarify status while preserving provenance.

- Retain all nineteen events and bounded ignored-inclusive search evidence.
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
| check-psychrophilic-native | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-native.log; Executed 2026-10-21T21:54:04.428656+00:00 through 2026-10-21T21:54:04.975912+00:00; metadata psychrophilic-native.json | context_only | Successful schema validation; source and semantics separately assessed. |
| check-psychrophilic-strict | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-strict.log; Executed 2026-10-21T21:54:04.428657+00:00 through 2026-10-21T21:54:05.367790+00:00; metadata psychrophilic-strict.json | context_only | Successful strict validation; no biological efficacy certification. |
| check-psychrophilic-snippets-network | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-snippets-network.log; Executed 2026-10-21T21:54:10.985673+00:00 through 2026-10-21T21:54:17.669898+00:00; metadata psychrophilic-snippets-network.json | context_only | Direct network invocation passed: eight fields over four references, four VERIFIED and four NOT_IN_ABSTRACT. Manual audit found seven literal spans and one PDF typography normalization; no current initial failed snippet attempt. |
| check-batch011-qc | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/batch011-qc.log; Executed 2026-10-21T20:52:41.208560+00:00 through 2026-10-21T20:54:10.001030+00:00; metadata batch011-qc.json | context_only | Actual B11 final QC at its original time, qualified against B12 bytes; independent of pending publication. |
| record | data/traits/environment/psychrophilic.yaml; Entire current 330-line record | supports | Thirteen nodes, eleven edges, eight snippets including two top-level snippets, one canonical and nineteen events covered. |
| policy | docs/GROUNDING_POLICY.md; Captured maintained authority | supports | Referent-based identity, functional facets and aggregate protein classes. |
| playbook | docs/CURATION_PLAYBOOK.md; Captured maintained authority | supports | Source scope, literal copied snippets and attributable acceptance. |
| schema | src/traitmech/schema/traitmech.yaml; Captured maintained authority | supports | Current node facets and review contract. |
| checklist | .claude/skills/curate-yaml-record/references/review-checklist.md; Captured maintained authority | supports | Whole-record identity, evidence, graph, provenance and readiness checks. |
| predicate-mapping-primary | mappings/predicate_grounding.tsv; Captured maintained authority | supports | Conditional RO wildcard rows and compatible local selects-for/confers gates. |
| reuse | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/common-reuse-b11-qc-supplement-qualified.json; Actual B11-to-B12 qualification | supports | Original outcomes and all current byte comparisons bound. |
| reuse-postcheck | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/common-reuse-output-verification-agent/post-execution-verification.json; Independent actual-output verification | supports | Actual output/hash postcheck; no new QC. |
| local-init | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/batch012-local-initialization-receipt.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Local-only initialization on verified prior local commit; publication status remains separately documented. |
| capture | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-grounding-agent/capture-verification.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | All 86 inputs verified before grounding assessment. |
| identity | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-grounding-agent/identity-assessment.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Active exact identity and direct parent; taxonomy names qualified by the separate projection addendum. |
| node-edges | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-grounding-agent/node-edge-ledger.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | All thirteen nodes, eleven edges and two components; formal roles separate from biology. |
| owners | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-grounding-agent/owner-provenance-assessment.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Current record and conditional mappings; shared and sibling writer boundaries. |
| expression | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-grounding-agent/expression-and-readiness-assessment.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Exact canonical/exemplar catalog applicability; three label-only aggregate classes, zero instances. |
| catalog-reuse | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-grounding-agent/catalog-reuse-receipt.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Original catalog/runner receipts separate from current copies. |
| local-authority | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-grounding-agent/local-and-owner-primary-excerpts.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Exact v2/v3/v8 rows, schema/policy and bounded writer windows actually read. |
| ground-reading | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-grounding-agent/reading-scope-receipt.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Six complete contextual histories and nineteen embedded events read; conservative inputs do not imply whole-source scientific assessment. |
| ground-manifest | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-grounding-agent/evidence-manifest.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Frozen 29 grounding artifacts verified. |
| ground-disposition | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-grounding-agent/documentary-assessment.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Ground auditor favored a separate polarity minor; final root/challenge calibration controls severity without overwriting this dissent. |
| taxonomy-addendum | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-grounding-agent/taxonomy-name-projection-addendum.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | XML ClassCDE misspelling is a category, not a name; direct names and nested DispName remain separate. |
| taxonomy-failure | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-grounding-agent/taxonomy-access.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Retained initial DNS failure, not an identity response or native-review validation failure. |
| metpo-primary | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/repo/data/raw/metpo.owl; All seventeen selected METPO XML elements | supports | Active exact psychrophilic and direct temperature-preference parent; deprecated replacements and neighboring numeric bins distinguished. |
| ro-primary | /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/ro.db; Actual RO2211/2212/2213 and inherited RO2326 chain | supports | Regulation requires process endpoints; contributes-to inherits a material subject and process object. |
| pato-primary | /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/pato.db; Actual PATO0001306 rows | supports | Decreased temperature denotes the physical condition/quality, supporting close grounding without making it a process. |
| chebi-primary | /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/chebi.db; Actual CHEBI25728 and CHEBI26523 rows | supports | Osmolyte and ROS chemical identities are meaningful; physiological efficacy is outside scope. |
| selects-for-primary | proposals/metpo_traitmech_v2/metpo_proposal_properties_robot.tsv; Captured TSV row 4 | supports | Environmental condition can favor an adapted trait under this local scaffold. |
| fluidity-primary | proposals/metpo_traitmech_v3/metpo_proposal_classes_robot.tsv; Captured TSV row 8 | supports | Membrane fluidity is a physical quality; the placeholder is separate from active upstream identity. |
| confers-primary | proposals/metpo_traitmech_v8/metpo_proposal_properties_robot.tsv; Captured TSV row 3 | supports | Presence/activity/state of a causal subject can confer a trait; broad formal endpoints retained. |
| taxon-colwellia | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-grounding-agent/taxon167879-network-retry.xml; Whole successful official taxonomy response; separate initial failure retained | supports | Taxon 167879 is the exact Colwellia psychrerythraea 34H strain; identity does not establish cold-growth phenotype. |
| meta-definition | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/definition-metadata.json; Actual retained indexed metadata/abstract; original request time | supports | Indexed review identity and abstract; selected author-PDF definition and notes are separately bound. |
| meta-annual | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/annual-metadata.json; Actual retained indexed metadata/abstract; original request time | supports | Indexed review identity, literal lipid phrase and generic membrane physical context only. |
| meta-solutes | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/solutes-metadata.json; Actual retained indexed metadata/abstract; original request time | context_only | Zero-hit Europe PMC lookup is a retrieval diagnostic, not an absent-DOI or absent-body claim. |
| meta-solutes-crossref | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/solutes-crossref.json; Positive Crossref identity and returned abstract; original request time | supports | AMTT review identity is positive despite Europe PMC zero hits; uninspected ellipsis-bearing note remains unknown. |
| body-definition | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/definition-author.pdf; Institutional author PDF p385 generic classification; p386 existing note and binding phrases only | supports | Broad near-freezing classification and existing note attribution supported. Prevention concerns damage rather than the positive stability outcome; detailed efficacy remains unassessed. |
| meta-canonical | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/canonical-metadata.json; Actual indexed metadata/abstract at its request time | supports | Actual article identity and indexed classification; later primary Introduction growth observation separately bound. |
| meta-psychrobacter | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/psychrobacter-metadata.json; Actual indexed metadata/abstract at its request time | supports | Actual title/abstract classification of named DAB_AL43B only; vector/AMR details are unassessed. |
| meta-omics | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/omics-metadata.json; Actual indexed metadata/abstract at its request time | supports | Actual review identity and literal abstract phrase; detailed enzyme or pathway efficacy unassessed. |
| meta-embr2013 | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/embr2013-metadata.json; Actual indexed metadata/abstract at its request time | supports | Actual review identity and abstract only; detailed notes not independently body-verified. |
| body-canonical | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/canonical-pmc.html; Official PMC HTML Introduction paragraphs 11/12; named strain classification/growth only | supports | Primary text supports active growth at and below zero for Colwellia 34H. Extrapolated minimum and motility are not substituted for measured growth. |
| definition-text | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/definition-author-raw.txt; Derived PDF reading-order text; p385/p386 selected literal spans | context_only | Current raw-text extraction is distinct from original PDF acquisition and retained earlier layout text. |
| sources | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/source-assessment.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Seven-work audit; source outcome remains unknown for detailed notes and unavailable nearest body text. |
| source-ledger | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/source-ledger.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | All seven bibliographic identities and actual abstract/body scopes. |
| placements | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/placement-ledger.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Fifteen external placements accounted for; grounding-field coverage is separately bound to the capture and grounding ledgers. |
| snippets | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/snippet-ledger.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Eight snippets: seven literal and one PDF line-break typography normalization; no unknown snippet or unsupported meaning. |
| node-sources | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/node-edge-source-ledger.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | All thirteen source node assessments and eleven source edge assessments, with detailed efficacy excluded. |
| edge-sources | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/node-edge-source-ledger.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Complete edge source ledger; unavailable notes and documentary polarity distinguished. |
| source-notes | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/note-attribution-ledger.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Existing stability and binding note attribution supported; other detailed/ellipsis notes remain limited. |
| source-status | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/publication-status-audit.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Actual returned notice fields; bounded publication-status checks. |
| source-reading | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/primary-reading-scope.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Actual selective primary reading and scope; incidental excluded content not adopted. |
| source-access | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/access-limits.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | API errors/help HTML/front-only metadata and successful later canonical HTML are distinguished. |
| source-reuse | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/source-reuse-receipt.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Original acquisitions separate from current copies at 21:54:49 UTC. |
| canonical-scope | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/canonical-assessment.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Exact 34H primary growth support; identity and measured/extrapolated quantities kept separate. |
| native-checks | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/native-check-context.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Current native/strict/direct network snippet commands passed; eight fields with four VERIFIED and four NOT_IN_ABSTRACT. |
| source-capture | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/initial-capture-verification.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | All 86 captured inputs checked before source assessment. |
| source-manifest | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/evidence-manifest.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Frozen fifty-three source artifacts verified. |
| root-reading-101 | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-root/canonical-primary-html-reading.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Only actual bounded root reading/observation scope; receipt hash is not an article-body hash. |
| root-reading-102 | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-root/grounding-frozen-reading.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Only actual bounded root reading/observation scope; receipt hash is not an article-body hash. |
| root-reading-103 | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-root/history-and-canonical-reading.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Only actual bounded root reading/observation scope; receipt hash is not an article-body hash. |
| root-reading-104 | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-root/identity-primary-reading.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Only actual bounded root reading/observation scope; receipt hash is not an article-body hash. |
| root-reading-105 | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-root/ontology-primary-reading.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Only actual bounded root reading/observation scope; receipt hash is not an article-body hash. |
| root-reading-106 | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-root/owner-and-taxonomy-reading.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Only actual bounded root reading/observation scope; receipt hash is not an article-body hash. |
| root-reading-107 | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-root/placement-reading.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Only actual bounded root reading/observation scope; receipt hash is not an article-body hash. |
| root-reading-109 | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-root/root-reading-attestation.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Only actual bounded root reading/observation scope; receipt hash is not an article-body hash. |
| root-reading-110 | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-root/selected-writer-primary-reading.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Only actual bounded root reading/observation scope; receipt hash is not an article-body hash. |
| root-reading-111 | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-root/source-frozen-reading.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Only actual bounded root reading/observation scope; receipt hash is not an article-body hash. |
| root-reading-112 | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-root/source-metadata-and-definition-reading.json; Derived audit or bounded reading/access receipt; primary bytes separately identified | supports | Only actual bounded root reading/observation scope; receipt hash is not an article-body hash. |
| challenge | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-semantic-challenge-agent/semantic-severity-challenge.json; Final independent challenge | supports | Exact fields, disposition and bindings verified. |
| adjudication | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-root-adjudication.json; Final root disposition | supports | Final findings control serialization; grounding polarity-severity dissent remains explicit. |

## Limits And Additional Notes

- Detailed cold-survival, fitness, ROS-defense, AMR and intervention efficacy/methods remain UNASSESSED_SCOPE; incidental displayed source material is not adopted.
- Frozen grounding recommends a minor for the separate stability-polarity inconsistency; root and independent challenge final calibration controls the serialized severity while preserving that dissent.
- Taxonomy supplies exact strain identity, not phenotype. Initial DNS bytes are not primary XML; successful retry and the category-versus-name projection correction are separately bound.
- Current Falcon frontmatter postdates the embedded June enrichment; it is a research lead, not proof of original source-acquisition chronology.
- Six whole repository histories are contextual; no exact current-target human acceptance was found locally. Private or off-repository acceptance remains unexcluded.
- Three label-only classes, zero instances and two NONMECHANISTIC components do not require speculative proteins, connectors, detailed module queries or experiments.
- Original metadata/body acquisitions, copies at 21:54:49 UTC, raw text derivation at 21:57:11 and successful canonical HTML acquisition at 21:57:26 remain distinct. API error/help/front-only responses are not body evidence. Detailed EMBR2013 notes and the AMTT ellipsis-bearing note remain unknown or unassessed, not false or paper-wide absent.
- Actual prior QC, qualification and local initialization do not assert B11 remote publication; publication remains separately documented.
- Final source, root adjudication and independent challenge are pinned; no builder/helper import or execution occurred during preparation.
- Coverage: seven works/seven forms, fifteen external placements, thirteen grounding fields, thirteen nodes/eleven edges, eight snippets (seven literal, one typographic), one canonical, three lexical edges, two components and nineteen embedded events.
- No scientific record, native inventory, Git or sweep-state mutation by serializer preparation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T220251Z-psychrophilic
kind: record
repository: CultureBotAI/TraitMech
title: Whole-record review of psychrophilic
started_at: '2026-10-21T21:53:42.109453Z'
finished_at: '2026-10-21T22:02:51Z'
reviewer:
  identity: codex
  kind: agent
  independence: independent
  independence_basis: Independent source and grounding audits, separate semantic challenge
    and bounded root primary/owner readings. Generic classification, identity, formal
    relation roles and the internal sign of an assertion assessed. Detailed cold-survival,
    fitness, ROS-defense, AMR and intervention efficacy/methods remain UNASSESSED_SCOPE.
    No scientific record edited.
  model: GPT-6 (Codex)
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'Needs curation: two major representation issues for imported process roles
  and reversed stability polarity, plus a bounded human-acceptance traceability minor.'
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
  - path: data/traits/environment/psychrophilic.yaml
    sha256: 1efc37ea89af76558af8c0ddbba1d67e9c4e6ddb9876d1faf6b884309a274457
    role: target
  - path: data/traits/environment/temperature_preference.yaml
    sha256: 124373347177201d4a2ed44d2d69d1160636e6a99aacc87b4b0ee71e73f0234f
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
  - path: history/infrastructure/curate-knowledge-gaps/2026-08-17T214933Z-claude-code-9c4af0.yaml
    sha256: a58b53be777e58ac29eb1c1571feb2593633c83d158aff4b6c96b8a1b9214c0f
    role: context
  - path: history/infrastructure/disposition-typing-burndown/2026-08-08T060908Z-claude-code-f802c8.yaml
    sha256: 8ede4f80f46395efb74643e1f4158975a119ffaec78b5b291f0fc3a520a11c59
    role: context
  - path: history/infrastructure/node-type-consistency/2026-08-15T014631Z-claude-code-9d7f4d.yaml
    sha256: 21f19561c0d4769e7acc62e05e41d0d395a0f239938f00829f79f2b9c3ac2510
    role: context
  - path: history/other/free-living-trehalose-external-research/2026-08-31T203047Z-claude-code-47e2e8.yaml
    sha256: e250d11c361b6dcb5184d42a754b855ab8dc30028832a27ae914fee6c331a70f
    role: context
  - path: history/records/free_living/2026-08-31T204506Z-claude-code-ca81b1.yaml
    sha256: 0c2d8296d829bf97b806e44163c6138eac07431dbedc34e99a70bcbb191c7fe4
    role: context
  - path: history/records/temperature_optimum_very_low/2026-09-04T034000Z-codex-1f380e.yaml
    sha256: 86baac0f11d45ba1989ba43c4c8a43294c652ebd6298f98cccdbb3cd9b32b198
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
  - path: proposals/metpo_traitmech_v3/metpo_proposal_classes_robot.tsv
    sha256: 1a1cc789782cfae195c1fc81ddaf848d06d162c7434d94cceb66838de98ab6fa
    role: context
  - path: proposals/metpo_traitmech_v3/proposal.md
    sha256: 37be7b2c2efe0d1598d62b8df04f08262ba74b9d8068e010df6ee48069449067
    role: context
  - path: proposals/metpo_traitmech_v4/metpo_proposal_properties_robot.tsv
    sha256: 55a96748c50b60ba0622170ef0eb09833f6d1e59431a4ab32b6fcb079103c0b7
    role: context
  - path: proposals/metpo_traitmech_v4/proposal.md
    sha256: c35d12fec87a3efdcfa320125446320315fca17bdb9228dd2b98ed00fe991bd8
    role: context
  - path: proposals/metpo_traitmech_v8/metpo_proposal_properties_robot.tsv
    sha256: 5445e86e845e0a2638292cff4586bf3858b1341d37fecf2e86cefcdbc9a046cd
    role: context
  - path: proposals/metpo_traitmech_v8/proposal.md
    sha256: 119d51e7b7194890514a9e313505212bab92aeba607f7c1b8f9d9d2edeef67e7
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
  - path: research/traits/environment/psychrophilic-deep-research-falcon.md
    sha256: 5561249c368f27cb8eb7c15dc94519d64b5de6844324fb86faf0258e49bbbe96
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/add_cold_shock_response_trait.py
    sha256: d90be1ba41afbc2c8194466485291a02c7f46c078cf4356c2635c169add6f521
    role: context
  - path: scripts/add_homeoviscous_adaptation_trait.py
    sha256: 1c757fd67bda18d2f4afb2fbf63d899844d416d084e2b9d53e298182ae2e4d09
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
  - path: scripts/connect_free_living_trehalose_osmotic.py
    sha256: 7b39fbf6fdae76a319dd88115888ac66137c1cbc5e798d1aaaaa35692df26252
    role: context
  - path: scripts/connect_mesophilic_graph_183.py
    sha256: 3f1fa78321d7aa98dc2fedde9784e71ed60624a94f825bf3af1674753af56f85
    role: context
  - path: scripts/connect_temperature_delta_high_graph_183.py
    sha256: ccbb1e6bb0e050d2975425914d6412fb3eb5812720407e1d143fbaae5a548bb7
    role: context
  - path: scripts/connect_temperature_delta_very_low_graph_183.py
    sha256: 19eb2722de2fae0c76bf4c83b5f5b13f09841b17def22cdccb86d373711bf879
    role: context
  - path: scripts/connect_temperature_optimum_very_low_graph_183.py
    sha256: 4749be5b5aacc87817ea013e587c41096e8a213c93dde74546f4906a0a08dc7e
    role: context
  - path: scripts/connect_temperature_range_mid4_graph_183.py
    sha256: dd4b85888e88346adb515170c8fa37d542c7c7d9307d8a9fc63b22bdd6fb8b70
    role: context
  - path: scripts/connect_temperature_range_very_low_graph_183.py
    sha256: 71755acb7ce3311fd473c8bef9a71dfed5fc6b8089b79cf33ea95cd5d1dad0a1
    role: context
  - path: scripts/curate_knowledge_gaps.py
    sha256: 9e0fb7e01a901d84189a28f1912a2552f28d2da8733c113589e4947359d48c73
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
  - path: scripts/normalize_homeoviscous_nodes.py
    sha256: 9b219161570aff3ca48bf79d7fac0fe0da0a629a32ce6ca60bee9b4b9d0f4bc9
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/review_mesophilic_graph_183.py
    sha256: 46f9548808936268217a5e078fc1fa64d74cc2eeb69863ab6f3bb0da21e2b59c
    role: context
  - path: scripts/review_nacl_delta_graph_183.py
    sha256: 91b85da640baff48e0d317c206aaa24c1216b3725d9c9814c6fb9d4d975e192c
    role: context
  - path: scripts/review_obligately_piezophilic_graph_183.py
    sha256: d8fcbbb725162212cfce96bed9800e2cf08374170b7d929a1928248178111efb
    role: context
  - path: scripts/review_temperature_delta_high_graph_183.py
    sha256: dcade5d2fdf07c76e06cd5d8abca898af95a8faabf70e45a62bebf951f2ae31b
    role: context
  - path: scripts/review_temperature_delta_very_low_graph_183.py
    sha256: 1ac23973b6cf54861f6ae79afefe93e39cc9382a93c73c36a8daa37b376334d0
    role: context
  - path: scripts/review_temperature_optimum_very_low_graph_183.py
    sha256: 17e41b0426e6c41a43e7624799cf35db9737ef372d3aeb3ea40ac0a2dce20869
    role: context
  - path: scripts/review_temperature_range_mid4_graph_183.py
    sha256: 51611a8200146f1887831e5b2a49800151dc0b112d177853c3055dd442852a5a
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
- target_id: METPO:1000614
  path: data/traits/environment/psychrophilic.yaml
  label: psychrophilic
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/psychrophilic.yaml
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
  selection: Fifth record of the actual locally initialized batch 012 queue. Whole
    330-line target and all 86 captured inputs verified before assessment. Local initialization
    at 21:02:18.445284 UTC does not assert publication of batch 011.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - METPO:1000614
checks:
- check_id: audit-graphs
  name: Full-corpus graph audit
  status: passed
  required: true
  target_ids:
  - METPO:1000614
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
  - METPO:1000614
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
  - METPO:1000614
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
  - METPO:1000614
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
  - METPO:1000614
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
  - METPO:1000614
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
  - METPO:1000614
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
- check_id: psychrophilic-native
  name: Focused native validation
  status: passed
  required: true
  target_ids:
  - METPO:1000614
  command: just validate data/traits/environment/psychrophilic.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Successful schema validation; source and semantics separately assessed.
  evidence_ids:
  - check-psychrophilic-native
- check_id: psychrophilic-strict
  name: Focused strict validation
  status: passed
  required: true
  target_ids:
  - METPO:1000614
  command: just validate-strict data/traits/environment/psychrophilic.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Successful strict validation; no biological efficacy certification.
  evidence_ids:
  - check-psychrophilic-strict
- check_id: psychrophilic-snippets-network
  name: Focused network snippet check
  status: passed
  required: true
  target_ids:
  - METPO:1000614
  command: just verify-snippets --record data/traits/environment/psychrophilic.yaml
    --out /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-snippets-network.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 'Direct network invocation passed: eight fields over four references, four
    VERIFIED and four NOT_IN_ABSTRACT. Manual audit found seven literal spans and
    one PDF typography normalization; no current initial failed snippet attempt.'
  evidence_ids:
  - check-psychrophilic-snippets-network
- check_id: batch011-qc
  name: Reused maintained batch-eleven QC
  status: passed
  required: true
  target_ids:
  - METPO:1000614
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
  - METPO:1000614
  summary: Three reviewed label-only protein classes and zero instances in a NONMECHANISTIC
    graph; no forced accession or detailed cold-response query.
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
- evidence_id: check-psychrophilic-native
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-native.log
  locator: Executed 2026-10-21T21:54:04.428656+00:00 through 2026-10-21T21:54:04.975912+00:00;
    metadata psychrophilic-native.json
  accessed_at: '2026-10-21T21:54:04.975912Z'
  support: context_only
  summary: Successful schema validation; source and semantics separately assessed.
  snapshot_sha256: 95d2e9ac05e5af6a6b3e3fe35bea838a882f242b15a8869ae88fa3ae1cb00cde
- evidence_id: check-psychrophilic-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-strict.log
  locator: Executed 2026-10-21T21:54:04.428657+00:00 through 2026-10-21T21:54:05.367790+00:00;
    metadata psychrophilic-strict.json
  accessed_at: '2026-10-21T21:54:05.367790Z'
  support: context_only
  summary: Successful strict validation; no biological efficacy certification.
  snapshot_sha256: 3dcabd7c045827a92d8fbb13d299b4d3ad4f7fdc1eff677db28918f1dc085ee0
- evidence_id: check-psychrophilic-snippets-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-snippets-network.log
  locator: Executed 2026-10-21T21:54:10.985673+00:00 through 2026-10-21T21:54:17.669898+00:00;
    metadata psychrophilic-snippets-network.json
  accessed_at: '2026-10-21T21:54:17.669898Z'
  support: context_only
  summary: 'Direct network invocation passed: eight fields over four references, four
    VERIFIED and four NOT_IN_ABSTRACT. Manual audit found seven literal spans and
    one PDF typography normalization; no current initial failed snippet attempt.'
  snapshot_sha256: 6f6312b67efa8ebda5a2612dff6296dbd6261f0aa5f67fe8914ec3b118469661
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
  reference: data/traits/environment/psychrophilic.yaml
  locator: Entire current 330-line record
  accessed_at: '2026-10-21T21:53:42.619508Z'
  support: supports
  summary: Thirteen nodes, eleven edges, eight snippets including two top-level snippets,
    one canonical and nineteen events covered.
  snapshot_sha256: 1efc37ea89af76558af8c0ddbba1d67e9c4e6ddb9876d1faf6b884309a274457
- evidence_id: policy
  kind: authority
  reference: docs/GROUNDING_POLICY.md
  locator: Captured maintained authority
  accessed_at: '2026-10-21T21:57:15.395674Z'
  support: supports
  summary: Referent-based identity, functional facets and aggregate protein classes.
  snapshot_sha256: 891678c983c2283a47c81c47950b35753981e9339d105f3bbdda92a1f5ab7f42
- evidence_id: playbook
  kind: authority
  reference: docs/CURATION_PLAYBOOK.md
  locator: Captured maintained authority
  accessed_at: '2026-10-21T21:57:15.395674Z'
  support: supports
  summary: Source scope, literal copied snippets and attributable acceptance.
  snapshot_sha256: 735e9b810471da9f7d8364e35ffe1e741edb3421480dac01727db6ea5aa65da9
- evidence_id: schema
  kind: authority
  reference: src/traitmech/schema/traitmech.yaml
  locator: Captured maintained authority
  accessed_at: '2026-10-21T21:57:15.395674Z'
  support: supports
  summary: Current node facets and review contract.
  snapshot_sha256: 46c47fc627b80ccbba1e8ab3fb6f2aee93bc2aef7aaf72fe9aadc3257f2c02dd
- evidence_id: checklist
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Captured maintained authority
  accessed_at: '2026-10-21T21:57:15.395674Z'
  support: supports
  summary: Whole-record identity, evidence, graph, provenance and readiness checks.
  snapshot_sha256: da8896328a0fd6cc92f1adf0d8be8980d0ddd41f3172c7936f2c7f119b293ac1
- evidence_id: predicate-mapping-primary
  kind: authority
  reference: mappings/predicate_grounding.tsv
  locator: Captured maintained authority
  accessed_at: '2026-10-21T21:57:15.395674Z'
  support: supports
  summary: Conditional RO wildcard rows and compatible local selects-for/confers gates.
  snapshot_sha256: 8e28c19e93aca3dc164a3befbe2612b289241de457c59f499e65936c03b7ce52
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
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-grounding-agent/capture-verification.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:54:24.850107Z'
  support: supports
  summary: All 86 inputs verified before grounding assessment.
  snapshot_sha256: 9e1e761d425a9c2af7cdd64c07c85ffaab69c00d30d07a5ce183072ac056be6a
- evidence_id: identity
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-grounding-agent/identity-assessment.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:57:15.389205Z'
  support: supports
  summary: Active exact identity and direct parent; taxonomy names qualified by the
    separate projection addendum.
  snapshot_sha256: e8eccf904472bf22adb877dd9a4fe3f5de1d0a32f285cc0620b08c5192f283c8
- evidence_id: node-edges
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-grounding-agent/node-edge-ledger.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:57:15.390691Z'
  support: supports
  summary: All thirteen nodes, eleven edges and two components; formal roles separate
    from biology.
  snapshot_sha256: 4773aa10ded15100f8419650e681a5ada5e0eff8d0b4e9443032e0852ee4143b
- evidence_id: owners
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-grounding-agent/owner-provenance-assessment.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:57:15.393515Z'
  support: supports
  summary: Current record and conditional mappings; shared and sibling writer boundaries.
  snapshot_sha256: a074b98de14267edf2b04780386752cbd80d6ebde50828ca01f09f979c98649e
- evidence_id: expression
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-grounding-agent/expression-and-readiness-assessment.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:57:15.394884Z'
  support: supports
  summary: Exact canonical/exemplar catalog applicability; three label-only aggregate
    classes, zero instances.
  snapshot_sha256: 7edffdf1eb3304f3203bcf5f0c0890af3a8d245f7c67e5a9b007d5dd12937057
- evidence_id: catalog-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-grounding-agent/catalog-reuse-receipt.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:54:38.761967Z'
  support: supports
  summary: Original catalog/runner receipts separate from current copies.
  snapshot_sha256: 8a3d230d3874021e09058ac69955913353a4a4c396e56326c964a3019c1f1a48
- evidence_id: local-authority
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-grounding-agent/local-and-owner-primary-excerpts.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:55:17.668436Z'
  support: supports
  summary: Exact v2/v3/v8 rows, schema/policy and bounded writer windows actually
    read.
  snapshot_sha256: 1f49731ff3520c4c6101f6a9e843a2b1400295216a67135a63c63b5efe8eb84c
- evidence_id: ground-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-grounding-agent/reading-scope-receipt.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:57:15.397787Z'
  support: supports
  summary: Six complete contextual histories and nineteen embedded events read; conservative
    inputs do not imply whole-source scientific assessment.
  snapshot_sha256: 69d17792168419461244ce140d0beb7f1674ba602c3f5b33498c0410d1322202
- evidence_id: ground-manifest
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-grounding-agent/evidence-manifest.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:57:29.201973Z'
  support: supports
  summary: Frozen 29 grounding artifacts verified.
  snapshot_sha256: 96dc4df3420f73bef2aee3b6f52055a00988f353755fe25f54d771203417a9e5
- evidence_id: ground-disposition
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-grounding-agent/documentary-assessment.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:57:15.395674Z'
  support: supports
  summary: Ground auditor favored a separate polarity minor; final root/challenge
    calibration controls severity without overwriting this dissent.
  snapshot_sha256: 662426a4f4b0eb045f55348c333df1fa37fd45b8d674ec7e1de28cd6e65c30eb
- evidence_id: taxonomy-addendum
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-grounding-agent/taxonomy-name-projection-addendum.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:58:53.125753Z'
  support: supports
  summary: XML ClassCDE misspelling is a category, not a name; direct names and nested
    DispName remain separate.
  snapshot_sha256: 002d53847f363db67dc49d47ff9b3e5fbb374cb991e8c94848f2664ea0a67cd3
- evidence_id: taxonomy-failure
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-grounding-agent/taxonomy-access.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:54:43.936485Z'
  support: supports
  summary: Retained initial DNS failure, not an identity response or native-review
    validation failure.
  snapshot_sha256: 4ed26ebb1499da849d9af2a56bc8902967629ef1729b0d56b65aa472d0ad0676
- evidence_id: metpo-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/repo/data/raw/metpo.owl
  locator: All seventeen selected METPO XML elements
  accessed_at: '2026-10-21T21:54:27.615657Z'
  support: supports
  summary: Active exact psychrophilic and direct temperature-preference parent; deprecated
    replacements and neighboring numeric bins distinguished.
  snapshot_sha256: 8b6f8fe0510a698579e532658c8ace05da2550093365df9ca83feb0741778415
- evidence_id: ro-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/ro.db
  locator: Actual RO2211/2212/2213 and inherited RO2326 chain
  accessed_at: '2026-10-21T21:54:24.853549Z'
  support: supports
  summary: Regulation requires process endpoints; contributes-to inherits a material
    subject and process object.
  snapshot_sha256: 849e616c29fecd0d4a6c6dee0dc0f6f117ace7167dbfa1e0f043dc84868f83cb
- evidence_id: pato-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/pato.db
  locator: Actual PATO0001306 rows
  accessed_at: '2026-10-21T21:54:24.857167Z'
  support: supports
  summary: Decreased temperature denotes the physical condition/quality, supporting
    close grounding without making it a process.
  snapshot_sha256: 179ab512b5c3a8827c74e2a496da575e2908a84740429deef265d58c9ce61d3b
- evidence_id: chebi-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/chebi.db
  locator: Actual CHEBI25728 and CHEBI26523 rows
  accessed_at: '2026-10-21T21:54:24.921806Z'
  support: supports
  summary: Osmolyte and ROS chemical identities are meaningful; physiological efficacy
    is outside scope.
  snapshot_sha256: 26ad4890cdcf6ee357760d815dfee8f5ba81e0873e62cb379369b04205722b0f
- evidence_id: selects-for-primary
  kind: authority
  reference: proposals/metpo_traitmech_v2/metpo_proposal_properties_robot.tsv
  locator: Captured TSV row 4
  accessed_at: '2026-10-21T21:55:17.668436Z'
  support: supports
  summary: Environmental condition can favor an adapted trait under this local scaffold.
  snapshot_sha256: 4ab5ca37ff8595210254b1099563b4425ecd737ed375dc5a932b44e2ad5c332e
- evidence_id: fluidity-primary
  kind: authority
  reference: proposals/metpo_traitmech_v3/metpo_proposal_classes_robot.tsv
  locator: Captured TSV row 8
  accessed_at: '2026-10-21T21:55:17.668436Z'
  support: supports
  summary: Membrane fluidity is a physical quality; the placeholder is separate from
    active upstream identity.
  snapshot_sha256: 1a1cc789782cfae195c1fc81ddaf848d06d162c7434d94cceb66838de98ab6fa
- evidence_id: confers-primary
  kind: authority
  reference: proposals/metpo_traitmech_v8/metpo_proposal_properties_robot.tsv
  locator: Captured TSV row 3
  accessed_at: '2026-10-21T21:55:17.668436Z'
  support: supports
  summary: Presence/activity/state of a causal subject can confer a trait; broad formal
    endpoints retained.
  snapshot_sha256: 5445e86e845e0a2638292cff4586bf3858b1341d37fecf2e86cefcdbc9a046cd
- evidence_id: taxon-colwellia
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-grounding-agent/taxon167879-network-retry.xml
  locator: Whole successful official taxonomy response; separate initial failure retained
  accessed_at: '2026-10-21T21:54:54.539996Z'
  support: supports
  summary: Taxon 167879 is the exact Colwellia psychrerythraea 34H strain; identity
    does not establish cold-growth phenotype.
  snapshot_sha256: 761bc61e5323d2879e6826374dcd3577cf00273761599555e444d58bf3db5e77
- evidence_id: meta-definition
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/definition-metadata.json
  locator: Actual retained indexed metadata/abstract; original request time
  accessed_at: '2026-10-21T10:00:01.461116Z'
  support: supports
  summary: Indexed review identity and abstract; selected author-PDF definition and
    notes are separately bound.
  snapshot_sha256: 24d64254a2baba7c573dff7ae523cc0e00d30e297c4f1fd7aa3a23c51a057059
- evidence_id: meta-annual
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/annual-metadata.json
  locator: Actual retained indexed metadata/abstract; original request time
  accessed_at: '2026-10-21T10:00:02.042457Z'
  support: supports
  summary: Indexed review identity, literal lipid phrase and generic membrane physical
    context only.
  snapshot_sha256: 801da630644a181211f991a6f21c49b178e42a65f615c4eebd8196bc29244588
- evidence_id: meta-solutes
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/solutes-metadata.json
  locator: Actual retained indexed metadata/abstract; original request time
  accessed_at: '2026-10-21T10:00:02.275195Z'
  support: context_only
  summary: Zero-hit Europe PMC lookup is a retrieval diagnostic, not an absent-DOI
    or absent-body claim.
  snapshot_sha256: d0eef7c61f38fab3f0b2a3d73127915d63da077e0617bff6ac487ec290045df3
- evidence_id: meta-solutes-crossref
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/solutes-crossref.json
  locator: Positive Crossref identity and returned abstract; original request time
  accessed_at: '2026-10-21T10:00:29.852181Z'
  support: supports
  summary: AMTT review identity is positive despite Europe PMC zero hits; uninspected
    ellipsis-bearing note remains unknown.
  snapshot_sha256: 9f5ed8f0f9d07aface3f482bc888a6c47a4d9683abf51f76b16bf56412857cf7
- evidence_id: body-definition
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/definition-author.pdf
  locator: Institutional author PDF p385 generic classification; p386 existing note
    and binding phrases only
  accessed_at: '2026-10-21T10:03:39.641646Z'
  support: supports
  summary: Broad near-freezing classification and existing note attribution supported.
    Prevention concerns damage rather than the positive stability outcome; detailed
    efficacy remains unassessed.
  snapshot_sha256: 5a7678c6418efbcccf54d91c55eea1c08f2a4ed0ce0e07a6995d5903b9a0eb2e
- evidence_id: meta-canonical
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/canonical-metadata.json
  locator: Actual indexed metadata/abstract at its request time
  accessed_at: '2026-10-21T21:54:41.569243Z'
  support: supports
  summary: Actual article identity and indexed classification; later primary Introduction
    growth observation separately bound.
  snapshot_sha256: 7eaded5876b1514eaf5900f1616e89bd6b4666a2848a0288d3ab26063a535554
- evidence_id: meta-psychrobacter
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/psychrobacter-metadata.json
  locator: Actual indexed metadata/abstract at its request time
  accessed_at: '2026-10-21T21:54:41.557337Z'
  support: supports
  summary: Actual title/abstract classification of named DAB_AL43B only; vector/AMR
    details are unassessed.
  snapshot_sha256: 1659f008dd06c225a074f55d68f82b88af8ccf03269b0ec7a9af916bca7d2081
- evidence_id: meta-omics
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/omics-metadata.json
  locator: Actual indexed metadata/abstract at its request time
  accessed_at: '2026-10-21T21:54:41.553260Z'
  support: supports
  summary: Actual review identity and literal abstract phrase; detailed enzyme or
    pathway efficacy unassessed.
  snapshot_sha256: 444b5453b6d5a72f0851ab5c2f0f8f2219fca893742bdc9c1c2d63217ce8231e
- evidence_id: meta-embr2013
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/embr2013-metadata.json
  locator: Actual indexed metadata/abstract at its request time
  accessed_at: '2026-10-21T21:54:41.526902Z'
  support: supports
  summary: Actual review identity and abstract only; detailed notes not independently
    body-verified.
  snapshot_sha256: c883ee5de4369a67ce5b910f6caaa6f09fc96eb2f22ca09f7366d6dc4ec8d256
- evidence_id: body-canonical
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/canonical-pmc.html
  locator: Official PMC HTML Introduction paragraphs 11/12; named strain classification/growth
    only
  accessed_at: '2026-10-21T21:57:26.518407Z'
  support: supports
  summary: Primary text supports active growth at and below zero for Colwellia 34H.
    Extrapolated minimum and motility are not substituted for measured growth.
  snapshot_sha256: 0cee8ce3d45adc0014856d101f76ff05553dc35df57e4f14bf74e21da315e990
- evidence_id: definition-text
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/definition-author-raw.txt
  locator: Derived PDF reading-order text; p385/p386 selected literal spans
  accessed_at: '2026-10-21T21:57:11.990598Z'
  support: context_only
  summary: Current raw-text extraction is distinct from original PDF acquisition and
    retained earlier layout text.
  snapshot_sha256: 71ef77b88e880420f533454926cac17498cbf8db380465139c888057115143e8
- evidence_id: sources
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/source-assessment.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:59:18.977372Z'
  support: supports
  summary: Seven-work audit; source outcome remains unknown for detailed notes and
    unavailable nearest body text.
  snapshot_sha256: c4777a054fc2a2f6a743928ada6a2270c0292855330c3a0da75002a35331952f
- evidence_id: source-ledger
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/source-ledger.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:59:18.947729Z'
  support: supports
  summary: All seven bibliographic identities and actual abstract/body scopes.
  snapshot_sha256: cd9b14928ea9aaba19fe2231a24aefef3913fd1135e22be0d6a5e5b0d6d83897
- evidence_id: placements
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/placement-ledger.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:59:18.963310Z'
  support: supports
  summary: Fifteen external placements accounted for; grounding-field coverage is
    separately bound to the capture and grounding ledgers.
  snapshot_sha256: 7d8a71122b62083c9e1cc6b7766ead0b38f212d2b2ed4128dba27ea8935b08ff
- evidence_id: snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/snippet-ledger.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:59:18.966023Z'
  support: supports
  summary: 'Eight snippets: seven literal and one PDF line-break typography normalization;
    no unknown snippet or unsupported meaning.'
  snapshot_sha256: 24c30d0c9eae9329818f5be289d06ccd590ab20d2c2162bd013e8cca0fad7071
- evidence_id: node-sources
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/node-edge-source-ledger.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:59:18.963759Z'
  support: supports
  summary: All thirteen source node assessments and eleven source edge assessments,
    with detailed efficacy excluded.
  snapshot_sha256: 48e5c08c3ab47bcba17f1e82b85ec99fb2d91aece06374933f37de731042aa5a
- evidence_id: edge-sources
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/node-edge-source-ledger.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:59:18.963759Z'
  support: supports
  summary: Complete edge source ledger; unavailable notes and documentary polarity
    distinguished.
  snapshot_sha256: 48e5c08c3ab47bcba17f1e82b85ec99fb2d91aece06374933f37de731042aa5a
- evidence_id: source-notes
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/note-attribution-ledger.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:59:18.966452Z'
  support: supports
  summary: Existing stability and binding note attribution supported; other detailed/ellipsis
    notes remain limited.
  snapshot_sha256: 9562a1ac4c67006e7f99208709d7b2c210bc9314658afbfd58b3f3a249a55ce5
- evidence_id: source-status
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/publication-status-audit.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:59:18.969365Z'
  support: supports
  summary: Actual returned notice fields; bounded publication-status checks.
  snapshot_sha256: f4d6868f4acb571b20a0a0db3f6d38262558bf9fd0738efb71b703784198bf51
- evidence_id: source-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/primary-reading-scope.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:59:18.974218Z'
  support: supports
  summary: Actual selective primary reading and scope; incidental excluded content
    not adopted.
  snapshot_sha256: 54bdabd4070e6bc900f18486411eb398ace98d54ccca5036183d68d469e23974
- evidence_id: source-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/access-limits.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:59:18.973049Z'
  support: supports
  summary: API errors/help HTML/front-only metadata and successful later canonical
    HTML are distinguished.
  snapshot_sha256: 0b80b230a07af6a8c3fc4847d7bb3442209084f2e0f3f3b50a132ab73046e453
- evidence_id: source-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/source-reuse-receipt.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:54:49.028177Z'
  support: supports
  summary: Original acquisitions separate from current copies at 21:54:49 UTC.
  snapshot_sha256: b17f25da2449e5731b02982b42d6b7dca6096d9730547133c2341c81043b37e8
- evidence_id: canonical-scope
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/canonical-assessment.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:59:18.961892Z'
  support: supports
  summary: Exact 34H primary growth support; identity and measured/extrapolated quantities
    kept separate.
  snapshot_sha256: 4dc0be1db5b23ee240198263566bc18099c43235bbdb829d567bccd5f711e6cb
- evidence_id: native-checks
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/native-check-context.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:59:18.968977Z'
  support: supports
  summary: Current native/strict/direct network snippet commands passed; eight fields
    with four VERIFIED and four NOT_IN_ABSTRACT.
  snapshot_sha256: 0e1bc8665f789b5b12a69acc5db820094cc980ab4c5277797d5e458ad2badebf
- evidence_id: source-capture
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/initial-capture-verification.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:54:12.546016Z'
  support: supports
  summary: All 86 captured inputs checked before source assessment.
  snapshot_sha256: f8bcc5c6d5ebe6a2139bf848669e01c554ce8873fce2fef64abaf227c672c914
- evidence_id: source-manifest
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-agent/evidence-manifest.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:59:18.993583Z'
  support: supports
  summary: Frozen fifty-three source artifacts verified.
  snapshot_sha256: 4612f29a42750e8204d8503cd68207854db3921e3dbd1c92043205f406b7cfc3
- evidence_id: root-reading-101
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-root/canonical-primary-html-reading.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:57:52.628913Z'
  support: supports
  summary: Only actual bounded root reading/observation scope; receipt hash is not
    an article-body hash.
  snapshot_sha256: fa578b2ca7c38d7b4897b0f4be994247e327a5a18799b3f3aa99a4c0f42a9ffa
- evidence_id: root-reading-102
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-root/grounding-frozen-reading.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:58:33.847706Z'
  support: supports
  summary: Only actual bounded root reading/observation scope; receipt hash is not
    an article-body hash.
  snapshot_sha256: db95e5006133006ac183ba20ed754c78796249830f7c01bceb697ca1cf26cc34
- evidence_id: root-reading-103
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-root/history-and-canonical-reading.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:57:31.440717Z'
  support: supports
  summary: Only actual bounded root reading/observation scope; receipt hash is not
    an article-body hash.
  snapshot_sha256: 3feaa84185fe9a10f08250c5a7d19e857c5ca473682c2a4a1d9415034fa0a4e8
- evidence_id: root-reading-104
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-root/identity-primary-reading.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:56:59.060193Z'
  support: supports
  summary: Only actual bounded root reading/observation scope; receipt hash is not
    an article-body hash.
  snapshot_sha256: e59a832bb77ee3185fc87f19471a816f02bd4d4712057c419bcbde1d49bb975e
- evidence_id: root-reading-105
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-root/ontology-primary-reading.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:56:49.266096Z'
  support: supports
  summary: Only actual bounded root reading/observation scope; receipt hash is not
    an article-body hash.
  snapshot_sha256: e075122d11aec9b0f11de20f6ca2e6c34a17b76e81e3eda03d155b68df3d0b21
- evidence_id: root-reading-106
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-root/owner-and-taxonomy-reading.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:57:18.723921Z'
  support: supports
  summary: Only actual bounded root reading/observation scope; receipt hash is not
    an article-body hash.
  snapshot_sha256: d576285062b53edcaaf374b62d8ac361b65db7e4a42233cb69d9b58f96adbb21
- evidence_id: root-reading-107
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-root/placement-reading.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T22:00:29.589050Z'
  support: supports
  summary: Only actual bounded root reading/observation scope; receipt hash is not
    an article-body hash.
  snapshot_sha256: 33127989453c9afb6d9de6b1460867956e68b0d3bfeec7f99cb07a4c6182299a
- evidence_id: root-reading-109
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-root/root-reading-attestation.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:57:41.888237Z'
  support: supports
  summary: Only actual bounded root reading/observation scope; receipt hash is not
    an article-body hash.
  snapshot_sha256: 63a447d76d6a28e7e4cca7edc70ddc6e9815941ebd14df3a4a0e789eb86cb3d1
- evidence_id: root-reading-110
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-root/selected-writer-primary-reading.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:58:13.914832Z'
  support: supports
  summary: Only actual bounded root reading/observation scope; receipt hash is not
    an article-body hash.
  snapshot_sha256: 59d23216c8243ba4ed2b43b5f2581ad1f419241aa9b5e5ca9113112bbd977993
- evidence_id: root-reading-111
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-root/source-frozen-reading.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:59:44.092001Z'
  support: supports
  summary: Only actual bounded root reading/observation scope; receipt hash is not
    an article-body hash.
  snapshot_sha256: 3846bd395736270800f9d673afe4fa1fc49790a3515fb932d1e8e86a751eff98
- evidence_id: root-reading-112
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-source-root/source-metadata-and-definition-reading.json
  locator: Derived audit or bounded reading/access receipt; primary bytes separately
    identified
  accessed_at: '2026-10-21T21:57:04.719079Z'
  support: supports
  summary: Only actual bounded root reading/observation scope; receipt hash is not
    an article-body hash.
  snapshot_sha256: 61a97516f4722837cb78797837e8331bd802b388a5f97676e1ead1245e8b25d3
- evidence_id: challenge
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-semantic-challenge-agent/semantic-severity-challenge.json
  locator: Final independent challenge
  accessed_at: '2026-10-21T22:01:40.754673Z'
  support: supports
  summary: Exact fields, disposition and bindings verified.
  snapshot_sha256: 1e6565f44fdb0d7090354ca0a4b7986ba3e86225a2a9902982701ef79d42f47d
- evidence_id: adjudication
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/psychrophilic-root-adjudication.json
  locator: Final root disposition
  accessed_at: '2026-10-21T22:01:47.978897Z'
  support: supports
  summary: Final findings control serialization; grounding polarity-severity dissent
    remains explicit.
  snapshot_sha256: 50a8f2939b3c8e99ec31161b3ad1efad3075f00c476862eebf33121154b7e765
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: active preference identity and groundings'
  outcome: supported
  target_ids:
  - METPO:1000614
  summary: Active METPO1000614 and direct parent1000613 match the current qualified
    low-temperature preference. Deprecated predecessors and neighboring numeric bins
    are distinguished; no exact-alias conflation is asserted. PATO cold condition,
    local membrane quality and CHEBI solute/ROS identities are meaningful.
  evidence_ids:
  - record
  - identity
  - metpo-primary
  - pato-primary
  - chebi-primary
  - fluidity-primary
  - taxonomy-addendum
- assessment_id: definition
  area: evidence
  topic: 'Native checklist: generic low-temperature preference'
  outcome: supported
  target_ids:
  - METPO:1000614
  summary: Current definition is a qualified preference, not a universal numerical
    cutoff. The author review uses a broad near-freezing classification; the approximate
    15 °C criterion is not directly calibrated by that passage. Ontology wording is
    positive without upgrading source scope to a precise threshold or efficacy claim.
  evidence_ids:
  - record
  - sources
  - identity
  - metpo-primary
  - source-reading
- assessment_id: hierarchy
  area: identity
  topic: 'Native checklist: direct parent and local relation semantics'
  outcome: supported
  target_ids:
  - METPO:1000614
  summary: Active temperature-preference parent is appropriate. Exact local selects-for
    and confers are compatible with current condition-to-trait and protein-class-to-trait
    uses. They do not silently inherit imported RO process requirements.
  evidence_ids:
  - identity
  - metpo-primary
  - selects-for-primary
  - confers-primary
  - local-authority
  - node-edges
- assessment_id: sources
  area: evidence
  topic: 'Native checklist: all assigned citations and placements'
  outcome: unknown
  target_ids:
  - METPO:1000614
  summary: Assigned bibliographic identities, generic classification and selected
    literal passages are assessed within the frozen source ledger. Inaccessible bodies
    and excluded detailed efficacy are not interpreted as false claims or absent statements.
  evidence_ids:
  - sources
  - source-ledger
  - placements
  - source-status
  - source-access
  - source-reuse
  - node-sources
  - edge-sources
  details: '{"completed_at": "2026-10-21T21:59:18.963759+00:00", "nodes": [{"index":
    0, "node_id": "psychrophilic_trait", "label": "psychrophilic", "node_type": "TRAIT",
    "grounding": "METPO:1000614", "assessment": "Broad environmental classification,
    supported by assigned author definition; exact 15 °C approximation qualified."},
    {"index": 1, "node_id": "low_temperature", "label": "low temperature", "node_type":
    "ENVIRONMENTAL_FACTOR", "grounding": "PATO:0001306", "assessment": "Generic environmental
    cold condition; physical context supported without operational interpretation."},
    {"index": 2, "node_id": "membrane_fluidity", "label": "membrane fluidity", "node_type":
    "QUALITY", "grounding": "METPO:1007505", "assessment": "Generic membrane physical
    state; detailed causal efficacy excluded and ontology role audit separate."},
    {"index": 3, "node_id": "unsaturated_fatty_acids", "label": "unsaturated and branched-chain
    fatty acids", "node_type": "CHEMICAL", "grounding": null, "assessment": "Generic
    lipid context supported by assigned annual abstract and author review; no universal
    structural requirement inferred."}, {"index": 4, "node_id": "cold_adapted_enzymes",
    "label": "cold-adapted enzymes", "node_type": "GENE_OR_PROTEIN", "grounding":
    null, "assessment": "Cold-active enzyme category and omics literal context only;
    detailed efficacy unassessed."}, {"index": 5, "node_id": "cold_shock_proteins",
    "label": "cold-shock proteins", "node_type": "GENE_OR_PROTEIN", "grounding": null,
    "assessment": "Cold-shock class literal source mention positive; detailed cold-defense
    efficacy unassessed."}, {"index": 6, "node_id": "antifreeze_proteins", "label":
    "antifreeze and ice-binding proteins", "node_type": "GENE_OR_PROTEIN", "grounding":
    null, "assessment": "AFP/ice-binding category literal source association positive;
    detailed defense efficacy unassessed."}, {"index": 7, "node_id": "transcription_translation",
    "label": "transcription and translation", "node_type": "BIOLOGICAL_PROCESS", "grounding":
    null, "assessment": "Process names explicit in current record; detailed mechanism
    unassessed."}, {"index": 8, "node_id": "compatible_solutes", "label": "compatible
    solutes", "node_type": "CHEMICAL", "grounding": "CHEBI:25728", "assessment": "Generic
    solute category citation identity positive; exact cross-taxon list/efficacy not
    established by inspected nearest text."}, {"index": 9, "node_id": "trehalose",
    "label": "trehalose", "node_type": "CHEMICAL", "grounding": null, "assessment":
    "Existing trehalose source note literal verified only; no efficacy endorsement."},
    {"index": 10, "node_id": "protein_membrane_stability", "label": "protein and membrane
    stability", "node_type": "QUALITY", "grounding": null, "assessment": "Current
    stability referent is explicit; incoming prevents edge reverses its positive state
    wording."}, {"index": 11, "node_id": "ice_crystals", "label": "ice crystals",
    "node_type": "CHEMICAL", "grounding": null, "assessment": "Ice material referent
    explicit; literal source association only."}, {"index": 12, "node_id": "reactive_oxygen_species",
    "label": "reactive oxygen species", "node_type": "CHEMICAL", "grounding": "CHEBI:26523",
    "assessment": "Detailed ROS concentration/generation biology unassessed; formal
    node/edge roles separate."}], "edges": [{"index": 0, "subject": "low_temperature",
    "predicate": "selects for", "object": "psychrophilic_trait", "reference": "DOI:10.1038/sj.embor.7400662",
    "outcome": "qualified_support", "assessment": "Generic low-temperature classification
    is supported by the assigned definition passage; selection is broad contextual
    language, not an exclusive mechanism."}, {"index": 1, "subject": "low_temperature",
    "predicate": "decreases", "object": "membrane_fluidity", "reference": "DOI:10.1038/sj.embor.7400662",
    "outcome": "supported_generic_context", "assessment": "Assigned abstract and generic
    membrane passage describe decreased membrane fluidity as a cold physical challenge;
    formal relation roles are separate."}, {"index": 2, "subject": "unsaturated_fatty_acids",
    "predicate": "regulates", "object": "membrane_fluidity", "reference": "DOI:10.1146/annurev-micro-091313-103612",
    "outcome": "qualified_support", "assessment": "Nearest annual-review abstract
    supports more unsaturated fatty acids and homeoviscous context. Detailed cross-taxon
    efficacy and every branched-chain component are not separately validated; no universal
    assertion inferred."}, {"index": 3, "subject": "cold_adapted_enzymes", "predicate":
    "confers", "object": "psychrophilic_trait", "reference": "DOI:10.1016/j.tim.2010.05.002",
    "outcome": "UNASSESSED_SCOPE", "assessment": "Exact omics phrase is verified in
    the abstract. Detailed enzyme mechanism/sufficiency is outside scope; generic
    association does not establish universal necessity."}, {"index": 4, "subject":
    "cold_shock_proteins", "predicate": "contributes to", "object": "psychrophilic_trait",
    "reference": "DOI:10.1038/sj.embor.7400662", "outcome": "UNASSESSED_SCOPE", "assessment":
    "Exact Cold-shock proteins sentence verified after PDF line-break dehyphenation;
    detailed fitness/acclimation efficacy unassessed."}, {"index": 5, "subject": "antifreeze_proteins",
    "predicate": "protects against", "object": "low_temperature", "reference": "DOI:10.1038/sj.embor.7400662",
    "outcome": "UNASSESSED_SCOPE", "assessment": "Exact intracellular ice formation
    phrase in source abstract; literal AFP/ice association is present in author review,
    detailed defense efficacy unassessed."}, {"index": 6, "subject": "cold_shock_proteins",
    "predicate": "regulates", "object": "transcription_translation", "reference":
    "DOI:10.1002/embr.201338170", "outcome": "UNASSESSED_SCOPE", "assessment": "Citation
    identity positive; assigned detailed transcription/translation note not independently
    body-verified. Initial source routes returned error/help/metadata-only/preview,
    not a demonstrated false claim."}, {"index": 7, "subject": "trehalose", "predicate":
    "prevents", "object": "protein_membrane_stability", "reference": "DOI:10.1038/sj.embor.7400662",
    "outcome": "internal_polarity_conflict", "assessment": "Current predicate/object
    prevents stability reverses current description and source-attributed note about
    preventing denaturation/aggregation. This documentary sign conflict is independent
    of detailed efficacy and independent of formal RO endpoints."}, {"index": 8, "subject":
    "compatible_solutes", "predicate": "maintains", "object": "protein_membrane_stability",
    "reference": "DOI:10.37256/amtt.5220244537", "outcome": "unknown", "assessment":
    "Crossref identity/abstract supports general review context; exact ellipsis-bearing
    note and nearest-source specificity unverified because no inspected full body.
    Detailed cryoprotection efficacy unassessed."}, {"index": 9, "subject": "antifreeze_proteins",
    "predicate": "binds to", "object": "ice_crystals", "reference": "DOI:10.1038/sj.embor.7400662",
    "outcome": "literal_attribution_supported_scope_limited", "assessment": "Author
    PDF selected AFP paragraph contains the literal bind-to-ice statement; no further
    mechanism or effectiveness claim assessed."}, {"index": 10, "subject": "low_temperature",
    "predicate": "increases", "object": "reactive_oxygen_species", "reference": "DOI:10.1002/embr.201338170",
    "outcome": "UNASSESSED_SCOPE", "assessment": "Assigned review identity is positive;
    actual detailed ROS-generation/defense note unassessed and not independently body-verified.
    No inferred paper-wide absence or efficacy conclusion."}], "scope": "Source identity,
    literal attribution, generic environmental classification and non-operational
    physical context only. Detailed pathogen cold-survival/fitness, ROS-defense, AMR,
    vector manipulation, interventions and mechanistic efficacy are UNASSESSED_SCOPE.
    Incidental displayed text is not adopted as a mechanism assessment."}'
- assessment_id: quotations
  area: evidence
  topic: 'Native checklist: native and manual copied-span coverage'
  outcome: supported
  target_ids:
  - METPO:1000614
  summary: Eight snippets have seven literal matches and one PDF line-break typography
    normalization, without omitted words or a meaning change. Native results remain
    four VERIFIED and four NOT_IN_ABSTRACT; body review supplies additional attribution
    without rewriting those results.
  evidence_ids:
  - snippets
  - source-reading
  - playbook
  - native-checks
- assessment_id: canonical
  area: evidence
  topic: 'Native checklist: Colwellia strain and named Psychrobacter exemplar'
  outcome: supported
  target_ids:
  - METPO:1000614
  summary: Taxon 167879 identifies Colwellia psychrerythraea 34H at strain rank. Actual
    assigned primary Introduction supports active growth at and below zero, beyond
    survival alone; extrapolated minimum and motility are not growth measurements.
    Named Psychrobacter sp. DAB_AL43B remains a different organism context. The taxonomy
    category misspelling is not copied as a strain alias.
  evidence_ids:
  - canonical-scope
  - sources
  - body-canonical
  - taxon-colwellia
  - taxonomy-addendum
- assessment_id: nodes
  area: consistency
  topic: 'Native checklist: all thirteen current referents'
  outcome: supported
  target_ids:
  - METPO:1000614
  summary: The cold condition, membrane/stability qualities, chemical classes, protein
    aggregates and transcription/translation process retain their stated facets. Activity
    wording does not turn enzyme or cold-shock protein classes into processes. No
    forced protein instance, connector, retype or new identifier is required.
  evidence_ids:
  - node-edges
  - node-sources
  - schema
  - policy
  - pato-primary
  - chebi-primary
  - fluidity-primary
  details: '[{"index": 0, "node": {"node_id": "psychrophilic_trait", "label": "psychrophilic",
    "node_type": "TRAIT", "grounding": "METPO:1000614", "description": "Growth is
    favored at low temperatures."}, "assessment": "supported", "reason": "Active self-grounded
    low-temperature growth preference."}, {"index": 1, "node": {"node_id": "low_temperature",
    "label": "low temperature", "node_type": "ENVIRONMENTAL_FACTOR", "description":
    "Cold environment near the freezing point of water.", "grounding": "PATO:0001306"},
    "assessment": "supported", "reason": "Low-temperature environment is a condition
    close-matching the PATO temperature quality, not an explicit cooling/exposure
    process."}, {"index": 2, "node": {"node_id": "membrane_fluidity", "label": "membrane
    fluidity", "node_type": "QUALITY", "description": "Physical state of the membrane
    needed for transport and growth.", "grounding": "METPO:1007505"}, "assessment":
    "supported", "reason": "Physical membrane fluidity is a QUALITY; local v3 definition
    and maintained schema agree. Its maintenance is a distinct process."}, {"index":
    3, "node": {"node_id": "unsaturated_fatty_acids", "label": "unsaturated and branched-chain
    fatty acids", "node_type": "CHEMICAL", "description": "Membrane lipid features
    that reduce packing order and maintain fluidity at low temperature."}, "assessment":
    "supported", "reason": "Unsaturated/branched-chain fatty acids are material lipid
    constituents; label aggregates features without asserting a single molecular species."},
    {"index": 4, "node": {"node_id": "cold_adapted_enzymes", "grounding_status": "REVIEWED_LABEL_ONLY",
    "grounding_notes": "Reviewed protein family, complex, or aggregate; no single
    semantic family identifier exactly captures this node''s represented scope.",
    "label": "cold-adapted enzymes", "node_type": "GENE_OR_PROTEIN", "description":
    "Enzymes with activity at low temperature, often associated with increased structural
    flexibility."}, "assessment": "supported", "reason": "Cold-adapted enzymes are
    a taxon-agnostic protein aggregate, explicitly REVIEWED_LABEL_ONLY with rationale.
    No gene-as-protein or mandatory single accession issue."}, {"index": 5, "node":
    {"node_id": "cold_shock_proteins", "grounding_status": "REVIEWED_LABEL_ONLY",
    "grounding_notes": "Reviewed protein family, complex, or aggregate; no single
    semantic family identifier exactly captures this node''s represented scope.",
    "label": "cold-shock proteins", "node_type": "GENE_OR_PROTEIN", "description":
    "Proteins induced during cold shock or cold acclimation."}, "assessment": "supported",
    "reason": "Cold-shock proteins are a material protein class, not the regulatory
    activity they may perform. Label-only rationale is explicit."}, {"index": 6, "node":
    {"node_id": "antifreeze_proteins", "grounding_status": "REVIEWED_LABEL_ONLY",
    "grounding_notes": "Reviewed protein family, complex, or aggregate; no single
    semantic family identifier exactly captures this node''s represented scope.",
    "label": "antifreeze and ice-binding proteins", "node_type": "GENE_OR_PROTEIN",
    "description": "Proteins that mitigate ice formation or recrystallization damage."},
    "assessment": "supported", "reason": "Antifreeze/ice-binding proteins are a protein
    aggregate, explicitly reviewed label-only; no forced accession or efficacy conclusion."},
    {"index": 7, "node": {"node_id": "transcription_translation", "label": "transcription
    and translation", "node_type": "BIOLOGICAL_PROCESS", "description": "Macromolecular
    synthesis processes impaired by cold-induced nucleic-acid secondary structure."},
    "assessment": "supported", "reason": "Transcription and translation are explicitly
    macromolecular synthesis processes; no molecular-activity versus material ambiguity
    required."}, {"index": 8, "node": {"node_id": "compatible_solutes", "label": "compatible
    solutes", "node_type": "CHEMICAL", "description": "Low-molecular-weight osmolytes
    (e.g. trehalose, glycine betaine, glycerol) accumulated for cryoprotection.",
    "grounding": "CHEBI:25728"}, "assessment": "qualified_positive", "reason": "Compatible
    solutes are named chemical solutes with CHEBI osmolyte closeMatch; no single molecule
    identity is asserted and detailed cryoprotection is unassessed."}, {"index": 9,
    "node": {"node_id": "trehalose", "label": "trehalose", "node_type": "CHEMICAL",
    "description": "Disaccharide cryoprotectant with colligative and protein-stabilizing
    effects."}, "assessment": "supported", "reason": "Trehalose is a chemical referent;
    lack of a CURIE alone is not a mandatory defect."}, {"index": 10, "node": {"node_id":
    "protein_membrane_stability", "label": "protein and membrane stability", "node_type":
    "QUALITY", "description": "Structural integrity of proteins and membranes maintained
    against cold denaturation."}, "assessment": "supported", "reason": "Structural
    integrity/stability is a positive measurable QUALITY, not denaturation or aggregation."},
    {"index": 11, "node": {"node_id": "ice_crystals", "label": "ice crystals", "node_type":
    "CHEMICAL", "description": "Intracellular/extracellular ice whose growth and recrystallization
    damage cells."}, "assessment": "supported", "reason": "Ice crystals are a material
    chemical water phase; no forced ontology grounding or detailed ice-damage assessment."},
    {"index": 12, "node": {"node_id": "reactive_oxygen_species", "label": "reactive
    oxygen species", "node_type": "CHEMICAL", "description": "ROS whose concentration
    rises at low temperature due to increased gas solubility.", "grounding": "CHEBI:26523"},
    "assessment": "supported", "reason": "Named ROS chemical class matches CHEBI26523;
    concentration/biological effects are not evaluated in this grounding audit."}]'
- assessment_id: predicates
  area: consistency
  topic: 'Native checklist: all eleven relation roles and signed meaning'
  outcome: concern
  target_ids:
  - METPO:1000614
  summary: Group RO role conflicts at edges 1/2/4/6/7/10. Regulation has explicit
    process endpoints; contributes-to permits its protein subject but not the trait
    object. Edge 7 also independently negates positive structural integrity while
    its prose concerns preventing damage. Root/challenge count that sign reversal
    as a separate major; the grounding auditor favored a minor. Three lexical edges
    and compatible local relations remain qualified positives.
  evidence_ids:
  - node-edges
  - ro-primary
  - local-authority
  - owners
  - ground-disposition
  - challenge
  - adjudication
  details: '[{"index": 0, "edge": {"subject": "low_temperature", "predicate": "selects
    for", "object": "psychrophilic_trait", "description": "Permanently cold environments
    select for microorganisms able to grow near freezing.", "evidence": [{"reference":
    "DOI:10.1038/sj.embor.7400662", "snippet": "growing well at temperatures around
    the freezing point", "notes": "Review supports psychrophile growth in near-freezing
    environments."}], "predicate_id": "METPO:2007401"}, "assessment": "supported",
    "reason": "Exact local selects-for relates environmental condition to adapted
    trait; no imported RO process-domain restriction and no assertion of detailed
    selection efficacy."}, {"index": 1, "edge": {"subject": "low_temperature", "predicate":
    "decreases", "object": "membrane_fluidity", "description": "Cold reduces membrane
    fluidity, altering transport and waste exchange.", "evidence": [{"reference":
    "DOI:10.1038/sj.embor.7400662", "snippet": "decreased membrane fluidity", "notes":
    "Supports membrane rigidification as a low-temperature challenge."}], "predicate_id":
    "RO:0002212"}, "assessment": "major", "reason": "RO2212 inherits RO2211 process/process
    constraints. Explicit low-temperature condition/PATO quality to membrane-fluidity
    QUALITY does not denote two processes. The fluidity object independently suffices;
    no blanket ENVIRONMENTAL_FACTOR prohibition."}, {"index": 2, "edge": {"subject":
    "unsaturated_fatty_acids", "predicate": "regulates", "object": "membrane_fluidity",
    "description": "Unsaturated and branched-chain fatty acids maintain membrane fluidity
    during cold growth.", "evidence": [{"reference": "DOI:10.1146/annurev-micro-091313-103612",
    "snippet": "more unsaturated fatty acids", "notes": "Review supports homoviscous
    membrane adaptation as temperature decreases."}], "predicate_id": "RO:0002211"},
    "assessment": "major", "reason": "RO2211 regulates connects material fatty-acid
    constituents to fluidity QUALITY, not process to process."}, {"index": 3, "edge":
    {"subject": "cold_adapted_enzymes", "predicate": "confers", "object": "psychrophilic_trait",
    "description": "Cold-active enzymes support catalysis at low temperature.", "evidence":
    [{"reference": "DOI:10.1016/j.tim.2010.05.002", "snippet": "genes involved in
    cold adaptation", "notes": "Review connects psychrophile omics signatures with
    cold-adaptation mechanisms."}], "predicate_id": "METPO:2007700"}, "assessment":
    "supported", "reason": "Local v8 confers and maintained mapping102 admit a protein
    class as subject and TRAIT as object. Formal compatibility does not validate detailed
    enzyme efficacy."}, {"index": 4, "edge": {"subject": "cold_shock_proteins", "predicate":
    "contributes to", "object": "psychrophilic_trait", "description": "Cold-shock
    proteins support cellular acclimation to low temperature.", "evidence": [{"reference":
    "DOI:10.1038/sj.embor.7400662", "snippet": "Cold-shock proteins have also been
    described", "notes": "Supports cold-shock proteins as psychrophile-associated
    adaptations."}], "predicate_id": "RO:0002326"}, "assessment": "major", "reason":
    "RO2326 inherits material/process roles through2216/2500/2595. Protein subject
    is material and fits; psychrophilic TRAIT object is not the required process.
    Do not falsely reject its protein subject."}, {"index": 5, "edge": {"subject":
    "antifreeze_proteins", "predicate": "protects against", "object": "low_temperature",
    "description": "Antifreeze and ice-binding proteins mitigate ice-associated stress
    in cold habitats.", "evidence": [{"reference": "DOI:10.1038/sj.embor.7400662",
    "snippet": "intracellular ice formation", "notes": "Review identifies ice formation
    as a cold challenge and cites bacterial antifreeze protein activity."}]}, "assessment":
    "lexical_qualified", "reason": "Ungrounded protects-against carries no imported
    RO endpoint constraint. Generic wording spans ice-associated stress rather than
    temperature itself; detailed protection efficacy remains unassessed, no separate
    mandatory grounding finding."}, {"index": 6, "edge": {"subject": "cold_shock_proteins",
    "predicate": "regulates", "object": "transcription_translation", "description":
    "Cold-shock proteins regulate transcription and translation during cold acclimation.",
    "evidence": [{"reference": "DOI:10.1002/embr.201338170", "notes": "cold-shock
    proteins (CSPs) regulate a variety of cellular processes, including transcription,
    translation."}], "predicate_id": "RO:0002211"}, "assessment": "major", "reason":
    "RO2211 process/process regulation has material cold-shock protein class subject,
    while transcription/translation object is valid process. Protein activity cannot
    silently replace the represented protein referent."}, {"index": 7, "edge": {"subject":
    "trehalose", "predicate": "prevents", "object": "protein_membrane_stability",
    "description": "Trehalose helps prevent protein denaturation and aggregation,
    acting as a cryoprotectant.", "evidence": [{"reference": "DOI:10.1038/sj.embor.7400662",
    "notes": "Trehalose is thought to have a colligative effect, but probably also
    helps in preventing protein denaturation and aggregation."}], "predicate_id":
    "RO:0002212"}, "assessment": "major_plus_minor_polarity", "reason": "RO2212 process/process
    relation connects trehalose CHEMICAL to positive stability QUALITY, contributing
    to the grouped formal issue. Independently, literal prevents points to stability
    whereas description/notes concern preventing denaturation/aggregation; bounded
    predicate/object polarity inconsistency. Intended supportive effect is explicit,
    so independently calibrated minor rather than a second formal major."}, {"index":
    8, "edge": {"subject": "compatible_solutes", "predicate": "maintains", "object":
    "protein_membrane_stability", "description": "Compatible solutes depress the freezing
    point and stabilize proteins and membranes.", "evidence": [{"reference": "DOI:10.37256/amtt.5220244537",
    "notes": "Compatible solutes depress the freezing point... stabilize proteins
    and membranes."}]}, "assessment": "lexical_qualified", "reason": "Ungrounded maintains
    links compatible-solute chemicals with positive stability quality; no imported
    RO constraint. Detailed stabilization or fitness efficacy unassessed."}, {"index":
    9, "edge": {"subject": "antifreeze_proteins", "predicate": "binds to", "object":
    "ice_crystals", "description": "Antifreeze/ice-binding proteins bind ice crystals
    to control ice growth and recrystallization.", "evidence": [{"reference": "DOI:10.1038/sj.embor.7400662",
    "notes": "Antifreeze proteins (AFPs) have the ability to bind to ice crystals."}]},
    "assessment": "lexical_qualified", "reason": "Ungrounded binds-to has protein
    and ice material referents. Formal molecular binding wording is intelligible;
    no new interaction mechanism or efficacy reconstruction."}, {"index": 10, "edge":
    {"subject": "low_temperature", "predicate": "increases", "object": "reactive_oxygen_species",
    "description": "Increased gas solubility at low temperature raises reactive oxygen
    species concentrations.", "evidence": [{"reference": "DOI:10.1002/embr.201338170",
    "notes": "The solubility of gases increases at lower temperatures, resulting in
    increased concentrations of reactive oxygen species."}], "predicate_id": "RO:0002213"},
    "assessment": "major", "reason": "RO2213 inherits process/process roles; explicit
    low-temperature condition/PATO quality to ROS CHEMICAL object is not process to
    process. The chemical object is independently decisive; no inference about physiological
    ROS concentration correctness."}]'
- assessment_id: biology
  area: scope
  topic: 'Native checklist: generic context and excluded detailed efficacy'
  outcome: unknown
  target_ids:
  - METPO:1000614
  summary: Formal types and the internal direction of an assertion can be reviewed
    while detailed cold-survival, fitness, ROS-defense, AMR and intervention mechanisms
    remain UNASSESSED_SCOPE. Source-specific generic context remains separate from
    such efficacy claims; no repaired mechanism or experiment is prescribed.
  evidence_ids:
  - edge-sources
  - source-reading
  - source-access
  - ground-reading
- assessment_id: completeness
  area: completeness
  topic: 'Native checklist: NONMECHANISTIC applicability'
  outcome: supported
  target_ids:
  - METPO:1000614
  summary: Two disclosed components, three reviewed label-only protein classes and
    zero instances are proportionate to this contextual graph. No mandatory connector,
    molecular instance, additional canonical organism or experiment is prescribed.
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
  - METPO:1000614
  summary: Exact Colwellia 34H and named Psychrobacter exemplar aliases do not match
    the retained 20-organism / 28-dataset catalog. Other source organisms can be covered;
    no global absence is asserted. No strain-resolved locus or detailed stress-response
    gene/module query was run.
  evidence_ids:
  - expression
  - catalog-reuse
  - taxon-colwellia
- assessment_id: ownership
  area: provenance
  topic: 'Native checklist: current assertions and conditional writers'
  outcome: supported
  target_ids:
  - METPO:1000614
  summary: Record owns current assertions and polarity. Shared predicate mappings
    fill empty IDs and preserve current nonempty values. The fluidity normalizer already
    agrees with current QUALITY; the trait-enables migration selects RO2327, not current
    RO2326. Sibling temperature/free-living histories and writers do not own this
    record. No exact current canonical-backfill entry was established.
  evidence_ids:
  - owners
  - ground-reading
  - local-authority
  - predicate-mapping-primary
- assessment_id: human
  area: provenance
  topic: 'Native checklist: bounded acceptance trace'
  outcome: concern
  target_ids:
  - METPO:1000614
  summary: Nineteen embedded events include eighteen AI events and an automated seed.
    All six complete repository histories are contextual AI records; ignored-inclusive
    216 matching paths and 67 structured review target arrays contain zero exact current
    targets. This bounds the missing acceptance link without ruling out private or
    remote review.
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
  - METPO:1000614
  summary: All 86 captured inputs match. Native, strict and direct network snippet
    commands pass; initial taxonomy DNS failure is separately retained from its successful
    retry. Historical common failures/retries remain explicit. Actual prior QC, byte
    qualification and local initialization do not assert B11 remote publication.
  evidence_ids:
  - capture
  - source-capture
  - reuse
  - reuse-postcheck
  - local-init
  - native-checks
  - taxonomy-failure
  - taxon-colwellia
  - check-psychrophilic-native
  - check-psychrophilic-strict
  - check-psychrophilic-snippets-network
findings:
- finding_id: imported-process-roles
  issue_key: psychrophilic-imported-process-roles
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Imported process relations conflict with current endpoint referents
  description: RO2211/2212/2213 require process endpoints. Current edges 1/2/6/7/10
    instead include explicitly grounded cold condition, physical qualities or chemical/protein
    materials. RO2326 at edge 4 permits the material protein subject but inherits
    a process object, unlike the current trait. Group these six role conflicts, preserving
    valid node facets and generic context; do not infer a categorical ban on environmental
    nodes.
  target_ids:
  - METPO:1000614
  field_paths:
  - causal_graphs[0].edges[1]
  - causal_graphs[0].edges[2]
  - causal_graphs[0].edges[4]
  - causal_graphs[0].edges[6]
  - causal_graphs[0].edges[7]
  - causal_graphs[0].edges[10]
  evidence_ids:
  - node-edges
  - ro-primary
  - pato-primary
  - schema
  - owners
  - challenge
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/psychrophilic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: RO wildcard mappings recur only for empty predicate fields; compatible local
      gates remain separate.
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Existing nonempty IDs are skipped; mapping edits alone do not repair current
      assertions.
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: stability-polarity
  issue_key: psychrophilic-stability-polarity
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Negative relation targets the positive stability outcome
  description: Edge 7 points a negative predicate at protein/membrane stability, explicitly
    defined as positive structural integrity, while its description and note concern
    preventing denaturation and aggregation. This reverses the machine-readable signed
    assertion independently of the imported endpoint problem. Root/challenger calibrate
    it as major; the ground auditor favored a bounded minor because the intended meaning
    is explicit. No biological intervention or replacement mechanism is prescribed.
  target_ids:
  - METPO:1000614
  field_paths:
  - causal_graphs[0].edges[7].predicate
  - causal_graphs[0].edges[7].object
  evidence_ids:
  - record
  - node-edges
  - ground-disposition
  - edge-sources
  - source-notes
  - body-definition
  - definition-text
  - challenge
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/psychrophilic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: human-acceptance-link
  issue_key: psychrophilic-human-acceptance-link
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Reviewed status lacks a locally attributable acceptance link
  description: Eighteen AI events and an automated seed, six contextual AI histories,
    and ignored-inclusive 216 paths/67 parsed target arrays/zero exact targets do
    not identify current-target human acceptance. This bounded traceability gap does
    not exclude private or remote review.
  target_ids:
  - METPO:1000614
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
    path: data/traits/environment/psychrophilic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
actions:
- action_id: reconcile-imported-roles
  description: Reconcile the six imported relation-role mismatches during authorized
    curation.
  finding_ids:
  - imported-process-roles
  target_ids:
  - METPO:1000614
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/psychrophilic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: RO wildcard mappings recur only for empty predicate fields; compatible local
      gates remain separate.
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Existing nonempty IDs are skipped; mapping edits alone do not repair current
      assertions.
  acceptance_checks:
  - Preserve valid current node facets and compatible local/lexical relation semantics.
  - Respect nonempty-ID guards; mapping changes alone do not repair current assertions.
  - No detailed mechanism reconstruction or intervention prescription.
- action_id: reconcile-stability-sign
  description: Reconcile the edge-7 signed assertion with its explicit intended stability
    meaning.
  finding_ids:
  - stability-polarity
  target_ids:
  - METPO:1000614
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/psychrophilic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Address signed predicate/object meaning separately from imported endpoint roles.
  - Preserve the independent severity calibration and source attribution.
  - No new efficacy claim, assay or operational mechanism repair.
- action_id: link-human-acceptance
  description: Link attributable acceptance if available or clarify status while preserving
    provenance.
  finding_ids:
  - human-acceptance-link
  target_ids:
  - METPO:1000614
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/psychrophilic.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Retain all nineteen events and bounded ignored-inclusive search evidence.
  - No contact or automatic status promotion authorized.
limitations:
- Detailed cold-survival, fitness, ROS-defense, AMR and intervention efficacy/methods
  remain UNASSESSED_SCOPE; incidental displayed source material is not adopted.
- Frozen grounding recommends a minor for the separate stability-polarity inconsistency;
  root and independent challenge final calibration controls the serialized severity
  while preserving that dissent.
- Taxonomy supplies exact strain identity, not phenotype. Initial DNS bytes are not
  primary XML; successful retry and the category-versus-name projection correction
  are separately bound.
- Current Falcon frontmatter postdates the embedded June enrichment; it is a research
  lead, not proof of original source-acquisition chronology.
- Six whole repository histories are contextual; no exact current-target human acceptance
  was found locally. Private or off-repository acceptance remains unexcluded.
- Three label-only classes, zero instances and two NONMECHANISTIC components do not
  require speculative proteins, connectors, detailed module queries or experiments.
- Original metadata/body acquisitions, copies at 21:54:49 UTC, raw text derivation
  at 21:57:11 and successful canonical HTML acquisition at 21:57:26 remain distinct.
  API error/help/front-only responses are not body evidence. Detailed EMBR2013 notes
  and the AMTT ellipsis-bearing note remain unknown or unassessed, not false or paper-wide
  absent.
- Actual prior QC, qualification and local initialization do not assert B11 remote
  publication; publication remains separately documented.
notes:
- Final source, root adjudication and independent challenge are pinned; no builder/helper
  import or execution occurred during preparation.
- 'Coverage: seven works/seven forms, fifteen external placements, thirteen grounding
  fields, thirteen nodes/eleven edges, eight snippets (seven literal, one typographic),
  one canonical, three lexical edges, two components and nineteen embedded events.'
- No scientific record, native inventory, Git or sweep-state mutation by serializer
  preparation.
tags:
- record-review
- psychrophilic
- environment
- needs-curation
native_verdict: needs_curation
```
