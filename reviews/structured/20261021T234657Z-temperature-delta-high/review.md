# Whole-record review of temperature delta high

- Review: 20261021T234657Z-temperature-delta-high
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-21T23:37:09.389373Z
- Finished UTC: 2026-10-21T23:46:57Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Whole-record review identifies one grouped imported-role major and two minors for copied spelling and human acceptance. Canonical 46 °C growth breadth and 14 literal fragments are positive; broader mechanism attribution remains unknown.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: Third record of the actual local batch 013 queue. Whole 394-line target and 90 inputs verified before judgment; local review does not assert remote publication.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8eee04a8c65609fbaff6df7c54597dcaf1b9d282.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| METPO:1000487 | data/traits/environment/temperature_delta_high.yaml | maintained | temperature delta high |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full-corpus graph audit | passed | True | METPO:1000487 | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| Full-corpus snippet audit | passed | True | METPO:1000487 | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| Full-corpus pathway links | passed | True | METPO:1000487 | 19 links checked against the pinned PathwayMech snapshot. |
| Full-corpus history integrity | passed | True | METPO:1000487 | 1277 history records checked, zero invalid links at the 8eee source base; integrity does not establish science or human acceptance. |
| Initial full-product validation | failed | False | METPO:1000487 | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation with isolated local cache | failed | False | METPO:1000487 | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation after isolated-cache download | passed | True | METPO:1000487 | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| Focused native validation | passed | True | METPO:1000487 | Successful native record validation; semantics assessed separately. |
| Initial strict recipe invocation | failed | False | METPO:1000487 | Nonexistent validate-record-strict recipe failed before strict validation. Optional superseded invocation, not completed-review validation failure. |
| Corrected focused strict validation | passed | True | METPO:1000487 | Actual validate-strict recipe passed after naming correction. |
| Focused network snippet check | passed | True | METPO:1000487 | 15 snippets:10 VERIFIED and5 NOT_IN_ABSTRACT; manual source review gives14 literal and1 spelling discrepancy. No initial target-specific network failure is invented. |
| Qualified batch-twelve QC | passed | True | METPO:1000487 | Actual prior QC qualified against B13 bytes; local continuation is independent of publication. |
| Protein-instance metadata applicability | not_applicable | False | METPO:1000487 | Zero protein classes or instances. Desaturase activity and thermostability quality are not protein instances; no token protein requirement. |

## Scientific And Domain Assessments

### Native checklist: active identity and hierarchy

identity: supported. Targets: METPO:1000487.

Active1000487 and parent1000303 align. Local1016200/1007505 placeholders and GO0006636 are positive; official1385984 and RW-2 type material match.

### Native checklist: numeric boundary and source calibration

quantity: unknown. Targets: METPO:1000487.

Raw METPO minInclusive30 and relatedTd_&gt;30 differ at exact30; current approximate-above30 prose is qualified, not a separate wrong-ID finding. Exact source calibration beyond inspected generic abstracts remains unknown.

### Native checklist: measured growth breadth

quantity: supported. Targets: METPO:1000487.

RW2 reported4–50 °C growth gives46 °C breadth under attached source conditions. Historical broadest-in-genus language is not independently current; no experiment or intervention proposed.

### Native checklist: four works and 17 placements

evidence: unknown. Targets: METPO:1000487.

Source identities and generic physical context are positive. Full Mendoza/Vieille bodies unavailable; joint adaptation and extreme-breadth causal calibration remain unknown, not disproved.

### Native checklist: all 15 supplied fragments

evidence: concern. Targets: METPO:1000487.

Manual14 literal matches and one copied-span discrepancy. Edge8 record homeoviscous differs from inspected publisher/indexed homoviscous despite abstract-verification note; scientific meaning is unchanged. Native 10 VERIFIED / 5 NOT_IN_ABSTRACT is not manual15-way adjudication.

### Native checklist: all 14 current referents

representation: unknown. Targets: METPO:1000487.

Identity/facets mostly align. Node2 capacity/process and node11 chemical/composition-shift wording remain qualified. Molecular activity need not be a material protein; thermostability is a quality.

{
  "grounding": [
    {
      "index": 0,
      "node_id": "temperature_delta_high_trait",
      "label": "temperature delta high",
      "node_type": "TRAIT",
      "grounding": "METPO:1000487",
      "outcome": "supported",
      "assessment": "Active exact numeric target; exact30 precision retained as limitation.",
      "biological_support": "UNASSESSED_SCOPE for detailed survival/fitness or intervention mechanisms"
    },
    {
      "index": 1,
      "node_id": "temperature_delta",
      "label": "temperature delta",
      "node_type": "TRAIT",
      "grounding": "METPO:1000303",
      "outcome": "supported",
      "assessment": "Active exact broader temperature-breadth parent.",
      "biological_support": "UNASSESSED_SCOPE for detailed survival/fitness or intervention mechanisms"
    },
    {
      "index": 2,
      "node_id": "maximal_thermal_adaptation",
      "label": "maximal thermal-adaptation flexibility",
      "node_type": "BIOLOGICAL_PROCESS",
      "grounding": null,
      "outcome": "unknown",
      "assessment": "Combined adaptation capacity wording can be disposition or process shorthand. Do not force reservoir CAPACITY enum; local confers allows broad mechanisms and no separate type finding is established.",
      "biological_support": "UNASSESSED_SCOPE for detailed survival/fitness or intervention mechanisms"
    },
    {
      "index": 3,
      "node_id": "decreased_growth_temperature",
      "label": "decreased growth temperature",
      "node_type": "ENVIRONMENTAL_FACTOR",
      "grounding": null,
      "outcome": "supported",
      "assessment": "Description denotes a decrease in ambient temperature, an event. ENVIRONMENTAL_FACTOR includes exposure/condition and does not categorically exclude event/process interpretation.",
      "biological_support": "UNASSESSED_SCOPE for detailed survival/fitness or intervention mechanisms"
    },
    {
      "index": 4,
      "node_id": "unsaturated_fatty_acid_biosynthesis",
      "label": "unsaturated fatty acid biosynthesis",
      "node_type": "BIOLOGICAL_PROCESS",
      "grounding": "GO:0006636",
      "outcome": "supported",
      "assessment": "GO0006636 label/definition directly identifies unsaturated-fatty-acid biosynthetic process, aligned with current node; no PUFA-specific mapping issue copied from other records.",
      "biological_support": "UNASSESSED_SCOPE for detailed survival/fitness or intervention mechanisms"
    },
    {
      "index": 5,
      "node_id": "homoviscous_adaptation",
      "label": "homoviscous adaptation",
      "node_type": "BIOLOGICAL_PROCESS",
      "grounding": "METPO:1016200",
      "outcome": "supported",
      "assessment": "Exact spelling variant is provided by local v85 proposal and mapping row133; current process sense distinguished from physical fluidity quality.",
      "biological_support": "UNASSESSED_SCOPE for detailed survival/fitness or intervention mechanisms"
    },
    {
      "index": 6,
      "node_id": "membrane_fluidity_homeostasis",
      "label": "membrane fluidity homeostasis",
      "node_type": "BIOLOGICAL_PROCESS",
      "grounding": null,
      "outcome": "supported",
      "assessment": "Maintenance of fluidity/permeability is explicitly a process; exact node-type consistency writer agrees.",
      "biological_support": "UNASSESSED_SCOPE for detailed survival/fitness or intervention mechanisms"
    },
    {
      "index": 7,
      "node_id": "decreased_membrane_fluidity",
      "label": "decreased membrane fluidity",
      "node_type": "STATE",
      "grounding": null,
      "outcome": "supported",
      "assessment": "Reduced membrane-fluidity state, not the sensing or establishment process. This referent drives edge4 concern.",
      "biological_support": "UNASSESSED_SCOPE for detailed survival/fitness or intervention mechanisms"
    },
    {
      "index": 8,
      "node_id": "lipid_desaturase_activity",
      "label": "lipid desaturase activity",
      "node_type": "MOLECULAR_FUNCTION",
      "grounding": null,
      "outcome": "supported",
      "assessment": "Molecular activity of lipid desaturation can be processual. It is not automatically a material protein; edge5 fails independently at quality object.",
      "biological_support": "UNASSESSED_SCOPE for detailed survival/fitness or intervention mechanisms"
    },
    {
      "index": 9,
      "node_id": "membrane_fluidity",
      "label": "membrane fluidity",
      "node_type": "QUALITY",
      "grounding": "METPO:1007505",
      "outcome": "supported",
      "assessment": "Physical membrane-fluidity quality, supported by exact v3 proposal and current mapping50.",
      "biological_support": "UNASSESSED_SCOPE for detailed survival/fitness or intervention mechanisms"
    },
    {
      "index": 10,
      "node_id": "membrane_viscosity_high_temperature",
      "label": "membrane viscosity at higher temperature",
      "node_type": "QUALITY",
      "grounding": null,
      "outcome": "supported",
      "assessment": "Membrane-viscosity quality retained as such; no requirement for universal grounding.",
      "biological_support": "UNASSESSED_SCOPE for detailed survival/fitness or intervention mechanisms"
    },
    {
      "index": 11,
      "node_id": "increased_fatty_acid_diversity",
      "label": "increased short-/branched-/unsaturated fatty acids",
      "node_type": "CHEMICAL",
      "grounding": null,
      "outcome": "unknown",
      "assessment": "Chemical enum and shift-of-composition description leave entity-versus-change precision qualified. Edge6 quality object independently conflicts with RO process range; no separate forced retype or new finding.",
      "biological_support": "UNASSESSED_SCOPE for detailed survival/fitness or intervention mechanisms"
    },
    {
      "index": 12,
      "node_id": "thermostable_enzyme",
      "label": "hyperthermophilic enzyme thermostability",
      "node_type": "QUALITY",
      "grounding": null,
      "outcome": "supported",
      "assessment": "Actual label/description denotes enzyme thermostability QUALITY, despite node_id shorthand. Not a protein class or instance. Its quality subject conflicts with edge7 process domain.",
      "biological_support": "UNASSESSED_SCOPE for detailed survival/fitness or intervention mechanisms"
    },
    {
      "index": 13,
      "node_id": "irreversible_protein_inactivation",
      "label": "irreversible inactivation at high temperatures",
      "node_type": "BIOLOGICAL_PROCESS",
      "grounding": null,
      "outcome": "supported",
      "assessment": "Irreversible protein-inactivation process; negative polarity refers to damage/inactivation and is not reversed positive-integrity polarity.",
      "biological_support": "UNASSESSED_SCOPE for detailed survival/fitness or intervention mechanisms"
    }
  ],
  "source": [
    {
      "index": 0,
      "field": "causal_graphs[0].nodes[0]",
      "node_id": "temperature_delta_high_trait",
      "outcome": "unknown",
      "assessment": "Current &gt;30 °C bin is explicit in the record; exact source threshold calibration is unresolved from inspected Mendoza abstract."
    },
    {
      "index": 1,
      "field": "causal_graphs[0].nodes[1]",
      "node_id": "temperature_delta",
      "outcome": "supported_at_definition_scope",
      "assessment": "Growth-supporting breadth is distinguished from optimum and survival; canonical arithmetic is independently positive."
    },
    {
      "index": 2,
      "field": "causal_graphs[0].nodes[2]",
      "node_id": "maximal_thermal_adaptation",
      "outcome": "unknown",
      "assessment": "Combined maximal adaptation capacity is an explicit synthesis; inspected generic sources do not measure this construct or establish exclusive &gt;30 °C sufficiency."
    },
    {
      "index": 3,
      "field": "causal_graphs[0].nodes[3]",
      "node_id": "decreased_growth_temperature",
      "outcome": "supported_at_generic_scope",
      "assessment": "Temperature decrease is the generic environmental context explicitly present in Mendoza abstract."
    },
    {
      "index": 4,
      "field": "causal_graphs[0].nodes[4]",
      "node_id": "unsaturated_fatty_acid_biosynthesis",
      "outcome": "supported_at_generic_scope",
      "assessment": "Existing UFA biosynthesis wording is covered by supplied Mendoza abstract spans; no detailed gene/pathway or intervention assessment."
    },
    {
      "index": 5,
      "field": "causal_graphs[0].nodes[5]",
      "node_id": "homoviscous_adaptation",
      "outcome": "supported_at_generic_scope",
      "assessment": "Named adaptation process is explicit in the current publisher abstract; exact copied-spelling issue is isolated at edge8."
    },
    {
      "index": 6,
      "field": "causal_graphs[0].nodes[6]",
      "node_id": "membrane_fluidity_homeostasis",
      "outcome": "supported_at_generic_scope",
      "assessment": "Generic membrane fluidity maintenance context is supported; all-condition or all-taxon performance is not established."
    },
    {
      "index": 7,
      "field": "causal_graphs[0].nodes[7]",
      "node_id": "decreased_membrane_fluidity",
      "outcome": "supported_at_generic_scope",
      "assessment": "Mendoza abstract explicitly discusses sensing decreased fluidity; no detailed sensing efficacy is assessed."
    },
    {
      "index": 8,
      "field": "causal_graphs[0].nodes[8]",
      "node_id": "lipid_desaturase_activity",
      "outcome": "supported_at_literal_physical_scope",
      "assessment": "Wu body p4 supports existing cis-bond/packing physical wording, not a detailed pathogen enzyme intervention."
    },
    {
      "index": 9,
      "field": "causal_graphs[0].nodes[9]",
      "node_id": "membrane_fluidity",
      "outcome": "supported_at_generic_scope",
      "assessment": "Fluidity is the physical referent in the selected abstract/body spans; formal typing assessed separately."
    },
    {
      "index": 10,
      "field": "causal_graphs[0].nodes[10]",
      "node_id": "membrane_viscosity_high_temperature",
      "outcome": "supported_at_literal_physical_scope",
      "assessment": "Wu p6 contains the existing trans-UFA/viscosity span; no universal warming response asserted by this audit."
    },
    {
      "index": 11,
      "field": "causal_graphs[0].nodes[11]",
      "node_id": "increased_fatty_acid_diversity",
      "outcome": "qualified",
      "assessment": "Wu p5 supports context-dependent acyl composition changes; no universal rule that every branching/chain change increases fluidity is inferred."
    },
    {
      "index": 12,
      "field": "causal_graphs[0].nodes[12]",
      "node_id": "thermostable_enzyme",
      "outcome": "supported_at_generic_scope",
      "assessment": "Vieille abstract explicitly supplies hyperthermophilic enzyme thermostability context."
    },
    {
      "index": 13,
      "field": "causal_graphs[0].nodes[13]",
      "node_id": "irreversible_protein_inactivation",
      "outcome": "supported_at_generic_scope",
      "assessment": "Irreversible inactivation is the outcome named in the source abstract; prevention efficacy is not expanded."
    }
  ]
}

### Native checklist: all 13 current relations

consistency: concern. Targets: METPO:1000487.

Edges3/4/5/6/7/8 form one imported-role group. Edge2 may denote a temperature-decrease event; Biolink associations retain broad endpoints. Edge7 negatively targets inactivation, so no reversed-positive-integrity finding.

{
  "grounding": [
    {
      "index": 0,
      "subject": "maximal_thermal_adaptation",
      "predicate": "confers",
      "predicate_id": "METPO:2007700",
      "object": "temperature_delta_high_trait",
      "outcome": "supported",
      "assessment": "Local v8 confers broad causal-node roles and maintained trait-object gate fit; capacity/process nuance does not establish formal violation.",
      "biological_support": "UNASSESSED_SCOPE for detailed survival/fitness or intervention mechanisms"
    },
    {
      "index": 1,
      "subject": "temperature_delta_high_trait",
      "predicate": "is a",
      "predicate_id": "rdfs:subClassOf",
      "object": "temperature_delta",
      "outcome": "supported",
      "assessment": "rdfs subclass edge agrees with exact imported1000487→1000303 hierarchy.",
      "biological_support": "UNASSESSED_SCOPE for detailed survival/fitness or intervention mechanisms"
    },
    {
      "index": 2,
      "subject": "decreased_growth_temperature",
      "predicate": "increases",
      "predicate_id": "RO:0002213",
      "object": "unsaturated_fatty_acid_biosynthesis",
      "outcome": "supported",
      "assessment": "Temperature-decrease event to biosynthetic process is a defensible processual reading. No enum-only ENVIRONMENTAL_FACTOR exclusion. Detailed causal biology is unassessed.",
      "biological_support": "UNASSESSED_SCOPE for detailed survival/fitness or intervention mechanisms"
    },
    {
      "index": 3,
      "subject": "homoviscous_adaptation",
      "predicate": "contributes to",
      "predicate_id": "RO:0002326",
      "object": "membrane_fluidity_homeostasis",
      "outcome": "concern",
      "assessment": "RO2326 inherits material→process via2216/2500/2595; explicit homoviscous process subject is nonmaterial, object process valid.",
      "biological_support": "UNASSESSED_SCOPE for detailed survival/fitness or intervention mechanisms"
    },
    {
      "index": 4,
      "subject": "decreased_membrane_fluidity",
      "predicate": "positively regulates",
      "predicate_id": "RO:0002213",
      "object": "unsaturated_fatty_acid_biosynthesis",
      "outcome": "concern",
      "assessment": "RO2213 inherits process→process via2211; actual low-fluidity STATE is not a process, despite nearby sensing prose.",
      "biological_support": "UNASSESSED_SCOPE for detailed survival/fitness or intervention mechanisms"
    },
    {
      "index": 5,
      "subject": "lipid_desaturase_activity",
      "predicate": "increases",
      "predicate_id": "RO:0002213",
      "object": "membrane_fluidity",
      "outcome": "concern",
      "assessment": "RO2213 process range conflicts with fluidity QUALITY object. Molecular-function activity subject is not independently excluded.",
      "biological_support": "UNASSESSED_SCOPE for detailed survival/fitness or intervention mechanisms"
    },
    {
      "index": 6,
      "subject": "increased_fatty_acid_diversity",
      "predicate": "increases",
      "predicate_id": "RO:0002213",
      "object": "membrane_fluidity",
      "outcome": "concern",
      "assessment": "RO2213 process endpoints conflict with current CHEMICAL subject and QUALITY object; even an event reading of composition shift leaves quality object conflict.",
      "biological_support": "UNASSESSED_SCOPE for detailed survival/fitness or intervention mechanisms"
    },
    {
      "index": 7,
      "subject": "thermostable_enzyme",
      "predicate": "prevents",
      "predicate_id": "RO:0002212",
      "object": "irreversible_protein_inactivation",
      "outcome": "concern",
      "assessment": "RO2212 inherits process→process; actual thermostability QUALITY subject is not a process. Object inactivation is process; negative polarity is coherent and not separately reversed.",
      "biological_support": "UNASSESSED_SCOPE for detailed survival/fitness or intervention mechanisms"
    },
    {
      "index": 8,
      "subject": "unsaturated_fatty_acid_biosynthesis",
      "predicate": "contributes to",
      "predicate_id": "RO:0002326",
      "object": "homoviscous_adaptation",
      "outcome": "concern",
      "assessment": "RO2326 material domain conflicts with explicit biosynthetic PROCESS subject; object homoviscous process is compatible.",
      "biological_support": "UNASSESSED_SCOPE for detailed survival/fitness or intervention mechanisms"
    },
    {
      "index": 9,
      "subject": "membrane_fluidity",
      "predicate": "associated with",
      "predicate_id": "biolink:associated_with",
      "object": "membrane_fluidity_homeostasis",
      "outcome": "supported",
      "assessment": "Biolink associated-with broad named-thing endpoints admit quality/process. Evidence scope remains separate.",
      "biological_support": "UNASSESSED_SCOPE for detailed survival/fitness or intervention mechanisms"
    },
    {
      "index": 10,
      "subject": "membrane_viscosity_high_temperature",
      "predicate": "associated with",
      "predicate_id": "biolink:associated_with",
      "object": "membrane_fluidity_homeostasis",
      "outcome": "supported",
      "assessment": "Biolink associated-with broad named-thing endpoints admit quality/process; no imported RO constraint inferred.",
      "biological_support": "UNASSESSED_SCOPE for detailed survival/fitness or intervention mechanisms"
    },
    {
      "index": 11,
      "subject": "membrane_fluidity_homeostasis",
      "predicate": "associated with",
      "predicate_id": "biolink:associated_with",
      "object": "maximal_thermal_adaptation",
      "outcome": "supported",
      "assessment": "Biolink associated-with broad named-thing endpoints admit process/process or capacity shorthand; no formal mismatch.",
      "biological_support": "UNASSESSED_SCOPE for detailed survival/fitness or intervention mechanisms"
    },
    {
      "index": 12,
      "subject": "thermostable_enzyme",
      "predicate": "associated with",
      "predicate_id": "biolink:associated_with",
      "object": "maximal_thermal_adaptation",
      "outcome": "supported",
      "assessment": "Biolink associated-with broad named-thing endpoints admit quality/process or capacity shorthand; no formal mismatch.",
      "biological_support": "UNASSESSED_SCOPE for detailed survival/fitness or intervention mechanisms"
    }
  ],
  "source": [
    {
      "index": 0,
      "field": "causal_graphs[0].edges[0]",
      "subject": "maximal_thermal_adaptation",
      "object": "temperature_delta_high_trait",
      "outcome": "unknown",
      "assessment": "UNKNOWN: inspected source supports generic membrane or protein context, but the exact &gt;30 °C growth-breadth calibration or joint adaptation bridge is not established by that inspected text. Full Mendoza/Vieille bodies were unavailable in this audit; this is not a paper-wide absence or biological refutation.",
      "source_placement": "causal_graphs[0].edges[0].evidence[0]",
      "predicate_formal_role": "Separate grounding audit; source match does not validate imported relation domain/range."
    },
    {
      "index": 1,
      "field": "causal_graphs[0].edges[1]",
      "subject": "temperature_delta_high_trait",
      "object": "temperature_delta",
      "outcome": "unknown",
      "assessment": "UNKNOWN: inspected source supports generic membrane or protein context, but the exact &gt;30 °C growth-breadth calibration or joint adaptation bridge is not established by that inspected text. Full Mendoza/Vieille bodies were unavailable in this audit; this is not a paper-wide absence or biological refutation.",
      "source_placement": "causal_graphs[0].edges[1].evidence[0]",
      "predicate_formal_role": "Separate grounding audit; source match does not validate imported relation domain/range."
    },
    {
      "index": 2,
      "field": "causal_graphs[0].edges[2]",
      "subject": "decreased_growth_temperature",
      "object": "unsaturated_fatty_acid_biosynthesis",
      "outcome": "supported_at_bounded_scope",
      "assessment": "Supplied span and generic physical/classification context supported. Detailed taxon-specific signaling, fitness, defense, AMR and intervention efficacy are UNASSESSED_SCOPE; a literal match is not complete mechanism validation.",
      "source_placement": "causal_graphs[0].edges[2].evidence[0]",
      "predicate_formal_role": "Separate grounding audit; source match does not validate imported relation domain/range."
    },
    {
      "index": 3,
      "field": "causal_graphs[0].edges[3]",
      "subject": "homoviscous_adaptation",
      "object": "membrane_fluidity_homeostasis",
      "outcome": "supported_at_bounded_scope",
      "assessment": "Supplied span and generic physical/classification context supported. Detailed taxon-specific signaling, fitness, defense, AMR and intervention efficacy are UNASSESSED_SCOPE; a literal match is not complete mechanism validation.",
      "source_placement": "causal_graphs[0].edges[3].evidence[0]",
      "predicate_formal_role": "Separate grounding audit; source match does not validate imported relation domain/range."
    },
    {
      "index": 4,
      "field": "causal_graphs[0].edges[4]",
      "subject": "decreased_membrane_fluidity",
      "object": "unsaturated_fatty_acid_biosynthesis",
      "outcome": "supported_at_bounded_scope",
      "assessment": "Supplied span and generic physical/classification context supported. Detailed taxon-specific signaling, fitness, defense, AMR and intervention efficacy are UNASSESSED_SCOPE; a literal match is not complete mechanism validation.",
      "source_placement": "causal_graphs[0].edges[4].evidence[0]",
      "predicate_formal_role": "Separate grounding audit; source match does not validate imported relation domain/range."
    },
    {
      "index": 5,
      "field": "causal_graphs[0].edges[5]",
      "subject": "lipid_desaturase_activity",
      "object": "membrane_fluidity",
      "outcome": "supported_at_bounded_scope",
      "assessment": "Supplied span and generic physical/classification context supported. Detailed taxon-specific signaling, fitness, defense, AMR and intervention efficacy are UNASSESSED_SCOPE; a literal match is not complete mechanism validation.",
      "source_placement": "causal_graphs[0].edges[5].evidence[0]",
      "predicate_formal_role": "Separate grounding audit; source match does not validate imported relation domain/range."
    },
    {
      "index": 6,
      "field": "causal_graphs[0].edges[6]",
      "subject": "increased_fatty_acid_diversity",
      "object": "membrane_fluidity",
      "outcome": "supported_at_bounded_scope",
      "assessment": "Supplied span and generic physical/classification context supported. Detailed taxon-specific signaling, fitness, defense, AMR and intervention efficacy are UNASSESSED_SCOPE; a literal match is not complete mechanism validation.",
      "source_placement": "causal_graphs[0].edges[6].evidence[0]",
      "predicate_formal_role": "Separate grounding audit; source match does not validate imported relation domain/range."
    },
    {
      "index": 7,
      "field": "causal_graphs[0].edges[7]",
      "subject": "thermostable_enzyme",
      "object": "irreversible_protein_inactivation",
      "outcome": "qualified",
      "assessment": "Enzyme thermostability and literal resistance-to-inactivation phrase are supported; extending whole-organism upper growth limits is an inference, not directly measured by this inspected abstract. No new finding solely from the inaccessible body.",
      "source_placement": "causal_graphs[0].edges[7].evidence[0]",
      "predicate_formal_role": "Separate grounding audit; source match does not validate imported relation domain/range."
    },
    {
      "index": 8,
      "field": "causal_graphs[0].edges[8]",
      "subject": "unsaturated_fatty_acid_biosynthesis",
      "object": "homoviscous_adaptation",
      "outcome": "concern",
      "assessment": "Generic adaptation component is supported; supplied homeoviscous phrase is not verbatim in the specifically claimed abstract, which spells homoviscous in both original indexed bytes and current publisher export. No biological falsehood or unseen-body claim.",
      "source_placement": "causal_graphs[0].edges[8].evidence[0]",
      "predicate_formal_role": "Separate grounding audit; source match does not validate imported relation domain/range."
    },
    {
      "index": 9,
      "field": "causal_graphs[0].edges[9]",
      "subject": "membrane_fluidity",
      "object": "membrane_fluidity_homeostasis",
      "outcome": "supported_at_bounded_scope",
      "assessment": "Supplied span and generic physical/classification context supported. Detailed taxon-specific signaling, fitness, defense, AMR and intervention efficacy are UNASSESSED_SCOPE; a literal match is not complete mechanism validation.",
      "source_placement": "causal_graphs[0].edges[9].evidence[0]",
      "predicate_formal_role": "Separate grounding audit; source match does not validate imported relation domain/range."
    },
    {
      "index": 10,
      "field": "causal_graphs[0].edges[10]",
      "subject": "membrane_viscosity_high_temperature",
      "object": "membrane_fluidity_homeostasis",
      "outcome": "supported_at_bounded_scope",
      "assessment": "Supplied span and generic physical/classification context supported. Detailed taxon-specific signaling, fitness, defense, AMR and intervention efficacy are UNASSESSED_SCOPE; a literal match is not complete mechanism validation.",
      "source_placement": "causal_graphs[0].edges[10].evidence[0]",
      "predicate_formal_role": "Separate grounding audit; source match does not validate imported relation domain/range."
    },
    {
      "index": 11,
      "field": "causal_graphs[0].edges[11]",
      "subject": "membrane_fluidity_homeostasis",
      "object": "maximal_thermal_adaptation",
      "outcome": "supported_at_bounded_scope",
      "assessment": "Supplied span and generic physical/classification context supported. Detailed taxon-specific signaling, fitness, defense, AMR and intervention efficacy are UNASSESSED_SCOPE; a literal match is not complete mechanism validation.",
      "source_placement": "causal_graphs[0].edges[11].evidence[0]",
      "predicate_formal_role": "Separate grounding audit; source match does not validate imported relation domain/range."
    },
    {
      "index": 12,
      "field": "causal_graphs[0].edges[12]",
      "subject": "thermostable_enzyme",
      "object": "maximal_thermal_adaptation",
      "outcome": "supported_at_bounded_scope",
      "assessment": "Supplied span and generic physical/classification context supported. Detailed taxon-specific signaling, fitness, defense, AMR and intervention efficacy are UNASSESSED_SCOPE; a literal match is not complete mechanism validation.",
      "source_placement": "causal_graphs[0].edges[12].evidence[0]",
      "predicate_formal_role": "Separate grounding audit; source match does not validate imported relation domain/range."
    }
  ]
}

### Native checklist: quantitative NONMECHANISTIC graph

scope: supported. Targets: METPO:1000487.

One component and zero protein classes/instances are appropriate to a numerical-bin overview; no fabricated connector or protein requirement.

### Native checklist: bounded biological reading

scope: unknown. Targets: METPO:1000487.

Generic environmental classification, supplied quotation and formal representations only. Detailed pathogen survival/fitness/ROS/AMR/intervention efficacy remains UNASSESSED_SCOPE; literal matches do not verify every causal bridge.

### Native checklist: canonical and source catalog applicability

evidence: unknown. Targets: METPO:1000487.

Retained 20-organism / 28-dataset catalog lacks exact canonical coverage. B. subtilis, E. coli and P. putida source/context species have coverage, but no strain-level or module-to46 °C phenotype inference or detailed module query was made.

### Native checklist: current writer recurrence

ownership: supported. Targets: METPO:1000487.

Generic grounder skips populated IDs. Dedicated review/connector have exact-state guards; repair dispatcher replaces selected existing keys using connector constants subject to complete-key prerequisites. Sibling label normalizers are context; no current canonical writer claim.

### Native checklist: actual whole reads and reuse

provenance: supported. Targets: METPO:1000487.

Thirteen current actor/target/event projections: four current whole-file reads and nine prior complete reads qualified by unchanged hashes. Three exact-target histories are AI edits; source-specific historical wording is not primary scientific authority.

### Native checklist: attributable current acceptance

provenance: concern. Targets: METPO:1000487.

16 AI events plus seed,179 ignored-inclusive paths and 68 actual target arrays with zero exact record do not establish attributable current human acceptance. Private/remote evidence remains unknown.

### Native checklist: checks and evidence chronology

consistency: supported. Targets: METPO:1000487.

All 90 inputs and frozen audits match. Native and corrected strict passed; wrong-recipe failure is optional/superseded. Common failures/skips, original acquisitions, copied/read times and local initialization remain explicit; no fresh B13 QC/publication claimed.

## Findings

### imported-process-roles: Imported roles conflict with current node referents

major / open / confirmed; issue key: temperature-delta-high-imported-process-roles.

Six imported relations conflict with the represented node referents. RO:0002326 inherits a material-entity subject, whereas edges 3 and 8 have explicit biological-process subjects. RO:0002213 inherits process-to-process roles: edge 4 starts from a reduced-fluidity state and edges 5 and 6 point to a fluidity quality. RO:0002212 also inherits process-to-process roles; edge 7 starts from thermostability quality. This is one grouped representation defect, not a biological refutation. Edge 2 denotes a temperature-decrease event and is not rejected merely because it uses the environmental-factor enum.

### quoted-spelling-drift: Copied abstract spelling and verification note disagree

minor / open / confirmed; issue key: temperature-delta-high-quoted-spelling-drift.

The supplied edge8 snippet says termed homeoviscous adaptation, while the currently inspected publisher and indexed abstracts say termed homoviscous adaptation. These spellings denote the same concept here, but the exact-quotation and abstract-verification claims need correction or an exact source-version locator. Historical requotation prose is not primary evidence of the supplied spelling.

### human-acceptance-link: Reviewed status lacks locally attributable acceptance

minor / open / confirmed; issue key: temperature-delta-high-human-acceptance-link.

The current REVIEWED status is not linked to attributable human acceptance of the present assertions in the inspected local evidence. The bounded search included ignored and hidden files, excluding .git and .venv: 179 matching paths, 68 actual review target arrays with zero exact current-target arrays, 17 embedded events (16 AI plus a seed), and 13 histories with explicit reading provenance. Private or remote acceptance remains unknown.

## Recommended Actions And Acceptance Checks

### resolve-imported-process-roles

Curate the six existing relation assertions against their actual node referents, retaining supported biological context. Review direct writer/connector constants and conditional mapping recurrence together; do not infer that rerunning a table grounder changes populated IDs or resurrect previously removed cis-trans assertions.

- Each affected triple fits the selected relation definition and inherited roles with an inspected source at the narrow claim.
- Preserve the current nonmechanistic scope, endpoint identity, prior removal and replay guards.
- Guarded curation/history plus strict, grounding, snippet, graph and maintained QC gates pass.

### resolve-quoted-spelling-drift

Align edge8 quoted text and its abstract-verification note with the exact inspected source version, or provide a verifiable version/locator containing the current wording; reconcile connector constants through guarded curation and append new history rather than rewriting old history.

- Literal snippet matches the identified primary source version.
- Verification note names the actual source scope; historical events remain immutable.
- Snippet check and strict validation pass, with full-text limitations stated.

### resolve-human-acceptance-link

Locate and attach an attributable human acceptance of the current assertions, or use the established curation process to resolve the status provenance; preserve prior actors and history.

- Acceptance identifies the reviewed assertions/version, responsible curator and accessible decision evidence.
- Status is not promoted solely because this AI review or deterministic checks passed.

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
| check-temperature-delta-high-validate | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-validate.log; Executed 2026-10-21T23:37:24.189596+00:00 through 2026-10-21T23:37:24.940228+00:00; metadata temperature-delta-high-validate.json | context_only | Successful native record validation; semantics assessed separately. |
| check-temperature-delta-high-strict | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-strict.log; Executed 2026-10-21T23:37:24.189547+00:00 through 2026-10-21T23:37:24.195545+00:00; metadata temperature-delta-high-strict.json | context_only | Nonexistent validate-record-strict recipe failed before strict validation. Optional superseded invocation, not completed-review validation failure. |
| check-temperature-delta-high-strict-corrected | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-strict-corrected.log; Executed 2026-10-21T23:37:29.736875+00:00 through 2026-10-21T23:37:31.372700+00:00; metadata temperature-delta-high-strict-corrected.json | context_only | Actual validate-strict recipe passed after naming correction. |
| check-temperature-delta-high-snippets-network | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-snippets-network.log; Executed 2026-10-21T23:37:34.939425+00:00 through 2026-10-21T23:37:40.009911+00:00; metadata temperature-delta-high-snippets-network.json | context_only | 15 snippets:10 VERIFIED and5 NOT_IN_ABSTRACT; manual source review gives14 literal and1 spelling discrepancy. No initial target-specific network failure is invented. |
| check-batch012-qc | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/batch012-qc.log; Executed 2026-10-21T23:02:31.440808+00:00 through 2026-10-21T23:04:01.628423+00:00; metadata batch012-qc.json | context_only | Actual prior QC qualified against B13 bytes; local continuation is independent of publication. |
| record | data/traits/environment/temperature_delta_high.yaml; Whole current394-line record | supports | All 14 nodes and 13 edges,17 events and one canonical example. |
| reuse | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-b12-qc-supplement-qualified.json; Actual B12-to-B13 qualification | supports | Original outcomes and current byte comparisons. |
| reuse-postcheck | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-output-verification-agent/post-execution-verification.json; Independent actual-output verification | supports | Actual qualification/hash postcheck, not new QC. |
| local-init | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/batch013-local-initialization-receipt.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Actual local initialization; publication status is separate. |
| policy | docs/GROUNDING_POLICY.md; Captured maintained authority | supports | Actual node referents and optional protein applicability. |
| playbook | docs/CURATION_PLAYBOOK.md; Captured maintained authority | supports | Verbatim source scope and attributable acceptance. |
| schema | src/traitmech/schema/traitmech.yaml; Captured maintained authority | supports | Current node facets and graph scope. |
| checklist | .claude/skills/curate-yaml-record/references/review-checklist.md; Captured maintained authority | supports | Whole-record review coverage. |
| predicate-mapping | mappings/predicate_grounding.tsv; Captured maintained authority | supports | Future-empty predicate mapping, with current skip-existing guard. |
| local-v3 | proposals/metpo_traitmech_v3/metpo_proposal_classes_robot.tsv; Captured maintained authority | supports | 1007505 fluidity quality. |
| local-v8 | proposals/metpo_traitmech_v8/metpo_proposal_properties_robot.tsv; Captured maintained authority | supports | 2007700 confers broad formal roles and trait object. |
| local-v85 | proposals/metpo_traitmech_v85/metpo_proposal_classes_robot.tsv; Captured maintained authority | supports | 1016200 named homeoviscous process, including homoviscous spelling. |
| capture | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-ground-agent/capture-verification.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | All 90 inputs and whole current target verified. |
| identity | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-ground-agent/identity-assessment.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Active target/parent, local placeholders and exact30 qualification. |
| nodes-edges | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-ground-agent/node-edge-grounding-ledger.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | All 14 nodes and 13 edges; formal positives and six grouped conflicts. |
| owners | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-ground-agent/owner-provenance-assessment.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Exact current direct writers and recurrence guards. |
| owner-primary | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-ground-agent/owner-primary-reading.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Actual direct reviewer, connector, repair and shared-grounder windows. |
| writer-state | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-ground-agent/writer-current-state-comparison.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | AST literal comparisons only; no maintained writer execution. |
| human-search | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-ground-agent/search-and-provenance.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | 179 ignored-inclusive matching paths, 68 actual arrays, zero exact target. |
| histories | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-ground-agent/history-reading-provenance.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | All 13 current projections; four current whole reads and nine prior whole reads reused by exact hash. |
| ground-reading | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-ground-agent/reading-scope-receipt.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Precise primary/history and excluded-science reading scopes. |
| expression | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-ground-agent/expression-and-readiness.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Canonical absent from retained catalog; source species coverage separately positive. |
| catalog-reuse | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-ground-agent/catalog-reuse-receipt.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Original 20-organism, 28-dataset provenance. |
| local-authority | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-ground-agent/local-authority-reading.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Local v3/v8/v85 and actual broad Biolink chain. |
| replacements | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-ground-agent/metpo-replacement-and-local-status.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Exact imported replacement/local-status search. |
| ground-manifest | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-ground-agent/evidence-manifest.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Frozen 30 artifacts, all hashes checked. |
| ground-disposition | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-ground-agent/documentary-assessment.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | One formal major and bounded human minor. |
| metpo-primary | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/repo/data/raw/metpo.owl; Actual retained primary authority; selected projection separately bound | supports | Active1000487 numeric minInclusive30/Cel, parent1000303 and relatedTd_&gt;30. |
| metpo-primary-projection | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-ground-agent/metpo-authority.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Selected current primary statements, not a replacement for raw authority. |
| ro-primary | /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/ro.db; Actual retained primary authority; selected projection separately bound | supports | Actual material/process and process/process inherited roles. |
| ro-primary-projection | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-ground-agent/selected-ro-primary-reading.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Selected current primary statements, not a replacement for raw authority. |
| go-primary | /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/go.db; Actual retained primary authority; selected projection separately bound | supports | GO0006636 exact unsaturated-fatty-acid biosynthetic-process identity. |
| go-primary-projection | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-ground-agent/selected-go-primary-reading.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Selected current primary statements, not a replacement for raw authority. |
| taxonomy | NCBITaxon:1385984; Whole successful official XML, current network retry | supports | Exiguobacterium chiriqhucha and RW-2 type material; taxonomy does not establish phenotype. |
| taxonomy-access | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-ground-agent/taxonomy-network-retry-access.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Actual successful taxonomy access, distinct from initial DNS failure. |
| taxonomy-initial | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-ground-agent/taxonomy-access.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Retained initial DNS failure, not a primary XML or identity contradiction. |
| mendoza | DOI:10.1146/annurev-micro-091313-103612; Retained indexed metadata/abstract; not full body | supports | Generic membrane context and supplied abstract spelling; exact breadth calibration unknown. |
| vieille | DOI:10.1128/MMBR.65.1.1-43.2001; Retained indexed metadata/abstract; not full body | supports | Generic thermostability context and supplied abstract span; exact breadth bridge unknown. |
| wu-metadata | DOI:10.3390/cells12101353; Indexed metadata/abstract | supports | Source identity and notice fields only. |
| canonical-metadata | DOI:10.3389/fmicb.2018.03189; Indexed metadata/abstract | supports | Canonical source identity and existing growth classification. |
| wu-primary | DOI:10.3390/cells12101353; JATS body paragraphs2/4/5/6,zero based | supports | Supplied fragments and generic physical context; no detailed intervention/efficacy inference. |
| canonical-primary | DOI:10.3389/fmicb.2018.03189; JATS abstract and first sentences of body44/68,zero based; existing condition cross-check13 | supports | RW2 reported growth4–50 °C supports46 °C breadth; historical ranking is not a current universal claim. |
| mendoza-browser | https://www.annualreviews.org/doi/10.1146/annurev-micro-091313-103612; Retained browser tool response, publisher abstract; not raw HTML or independently known origin/cache-fetch time | refutes | Current publisher abstract agrees with indexed homoviscous spelling; only the narrow copied-span claim is challenged. |
| sources | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-source-agent/source-assessment.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Four works, overall UNKNOWN, one bounded copied-span minor. |
| source-identities | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-source-agent/source-identities.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Actual identities and assigned-work scope. |
| placements | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-source-agent/source-placement-ledger.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | All 17 external placements and structured grounding accounting. |
| snippets | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-source-agent/snippet-ledger.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | 15 supplied snippets:14 literal,one spelling discrepancy. |
| copy-discrepancy | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-source-agent/copied-span-assessment.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Homeoviscous/homoviscous exact quotation difference preserves concept meaning. |
| source-nodes-edges | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-source-agent/node-edge-source-ledger.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | All14node/13edge source judgments. |
| source-status | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-source-agent/source-status-ledger.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Bounded notice checks, not exhaustive current publication search. |
| source-reading | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-source-agent/primary-reading-scope.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Selected abstracts/body paragraphs; no whole-article reading claim. |
| source-access | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-source-agent/source-access-limits.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | HTTP403/500 and unavailable full bodies remain access limits, not refutations. |
| source-reuse | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-source-agent/source-reuse-receipt.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Original 10:00/11:23 metadata acquisition differs from current copy/read times. |
| canonical | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-source-agent/canonical-assessment.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Source-specific growth interval and46 °C arithmetic positive. |
| source-checks | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-source-agent/native-check-context.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Actual failed wrong recipe and corrected strict plus10/5native snippet outcomes. |
| source-manifest | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-source-agent/evidence-manifest.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Frozen 35 artifacts, all hashes checked. |
| root-reading | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-source-root/root-primary-reading.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Actual root primary authority and source reading, bounded to recorded scopes. |
| root-ledgers | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-source-root/root-ledger-reading.json; Derived audit, reading or access receipt; primary bytes separately identified | supports | Actual source/ground/owner ledgers and history projection scope. |
| challenge | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-semantic-challenge-agent/semantic-severity-challenge.json; Final independent semantic challenge | supports | Actual frozen grouping/severity and all bound evidence verified. |
| adjudication | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-root-adjudication.json; Final root adjudication | supports | One major and two minors; exact field/action parity controls serialization. |

## Limits And Additional Notes

- Raw METPO existential minInclusive30 and related synonym Td_&gt;30 conflict at exact30. Approximate record prose is retained as a boundary qualification, not a separate wrong-identity finding.
- Node2 capacity wording and node11 compositional-shift wording warrant referent precision; no unsupported standalone node defect or forced CAPACITY reservoir claim.
- The direct &gt;30 calibration and extreme-breadth causal attribution remain UNKNOWN beyond inspected generic abstracts; inaccessible bodies are not negative evidence.
- Detailed pathogen defense/fitness/intervention mechanisms are outside this generic physiological review.
- Literal matches alone do not verify adjacent scope or causal inference.
- UNKNOWN: inspected source supports generic membrane or protein context, but the exact &gt;30 °C growth-breadth calibration or joint adaptation bridge is not established by that inspected text. Full Mendoza/Vieille bodies were unavailable in this audit; this is not a paper-wide absence or biological refutation.
- Edge0/edge1 direct breadth attribution is stronger than inspected generic abstract support; retain unknown rather than claiming unseen full-source absence or inventing another finding.
- Node/edge physical context and supplied spans are assessed at generic non-operational scope; detailed mechanism sufficiency and efficacy remain unassessed.
- Canonical historical superlative is not an independently current ranking.
- Formal role and node-typing findings are owned by the separate grounding audit.
- Full source acquisition is distinct from selected reading; current browser export is not raw publisher HTML.
- Original Mendoza and Vieille metadata acquisition times, current copy times, publisher HTTP403 and Vieille HTTP500 are preserved.
- Grounding history coverage comprises four current whole rereads and nine qualified unchanged prior whole reads; root independently read three exact-target histories and all thirteen projections.
- Canonical catalog absence does not imply source-organism absence: retained catalog covers contextual B. subtilis, E. coli and P. putida at species level; no exact strain/module breadth support is claimed.
- The initial wrong strict recipe failed before validation; corrected maintained validate-strict passed. This was not a completed review validation failure.
- Qualified historical common diagnostics preserve original failures/retries/skips; no fresh B13 corpus QC or remote publication is claimed.
- Publisher browser evidence is retained tool output; actual origin/cache-fetch time is not independently known. HTTP403/500 bytes and initial taxonomy DNS error are access diagnostics, not primary bodies.
- Original metadata acquisitions, current copies and current selected readings have separate timestamps. Qualified common diagnostics retain original failures/skips; no fresh B13 QC or remote publication is asserted.
- Whole 394-line target,90 captured inputs, four works / 17 placements / 18 grounding fields, 14 nodes and 13 edges, 15 snippets and one canonical example reviewed.
- History coverage is four current whole reads plus nine prior unchanged whole reads; all 13 projections are current. The graph has 17 events (16 AI plus a seed), one component and zero protein classes or instances.
- Preparation imports/executes no serializer/helper and changes no scientific record, Git or state. Root owns eventual single serialization.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T234657Z-temperature-delta-high
kind: record
repository: CultureBotAI/TraitMech
title: Whole-record review of temperature delta high
started_at: '2026-10-21T23:37:09.389373Z'
finished_at: '2026-10-21T23:46:57Z'
reviewer:
  identity: codex
  kind: agent
  independence: independent
  independence_basis: Separate source and grounding audits, independent semantic challenge
    and root primary/owner readings. Generic environmental classification, source
    attribution and formal representation only; detailed pathogen survival and intervention
    mechanisms remain UNASSESSED_SCOPE.
  model: GPT-6 (Codex)
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Whole-record review identifies one grouped imported-role major and two minors
  for copied spelling and human acceptance. Canonical 46 °C growth breadth and 14
  literal fragments are positive; broader mechanism attribution remains unknown.
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
  - path: data/traits/environment/temperature_delta.yaml
    sha256: 38d2a033d5966f366b6db1a671d9fc2fc1ae09f6f4297cef9894e5eeae23840a
    role: context
  - path: data/traits/environment/temperature_delta_high.yaml
    sha256: 5a14c751b66b3593df2f558e50cedd4983484d782915e1b167e1404eebf12418
    role: target
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
  - path: history/infrastructure/node-type-consistency/2026-08-15T014631Z-claude-code-9d7f4d.yaml
    sha256: 21f19561c0d4769e7acc62e05e41d0d395a0f239938f00829f79f2b9c3ac2510
    role: context
  - path: history/infrastructure/pr664-adversarial-review/2026-09-07T010200Z-codex-8e1e0f.yaml
    sha256: 274926690fd3c48c8344b70c1b9c826a673d63e000960282ee270d0083152641
    role: context
  - path: history/infrastructure/pr664-adversarial-review/2026-09-07T022000Z-codex-678abc.yaml
    sha256: 22312f00ff8b72ef65f94fe63009df22d611de0e8f41616dfbfd392cf7869942
    role: context
  - path: history/infrastructure/pr664-adversarial-review/2026-09-07T022300Z-codex-681abc.yaml
    sha256: 614d735ae87694a6591db42fe38bee3f6b4fd12cb3218fea26ee5b515d492dca
    role: context
  - path: history/other/canonical-examples-batch1/2026-08-20T074839Z-claude-code-6fb2f5.yaml
    sha256: c938f2928f2eb41505d58c2fb72d8de01d99534d766de9af400010e8778988a4
    role: context
  - path: history/records/mesophilic/2026-09-04T004000Z-codex-14a39b.yaml
    sha256: cdf9710543d62277f232e633fca2dd146a1ae45dab75f957a5462929650accf0
    role: context
  - path: history/records/temperature_delta_high/2026-09-04T030000Z-codex-ac3022.yaml
    sha256: 5f6af59766c35dfbb6ffa33f91863f2779f96a4057b50d13e39cbca318cc6ca2
    role: context
  - path: history/records/temperature_delta_high/2026-09-04T190000Z-codex-183.yaml
    sha256: 22684cc1063398106292e5b1b1a209cba9b61aa15c25a79164cdb5e7530d04fd
    role: context
  - path: history/records/temperature_delta_high/2026-09-15T070757Z-codex-cfe242.yaml
    sha256: 9919c243dab7f253ab0af9ffb0cec69244976119a9d448671a41197a0f7c9554
    role: context
  - path: history/records/temperature_delta_low/2026-09-15T070758Z-codex-4f2793.yaml
    sha256: 99ee1d757aeabef188fe06ed276db702248fef41d12e2a472dac8daaa07b6b4c
    role: context
  - path: history/records/temperature_delta_mid2/2026-09-15T070758Z-codex-ad0c3d.yaml
    sha256: c1052664e16050c3173a359351a8a147a3e77750bfe98642b34b3c00893402d0
    role: context
  - path: history/records/temperature_delta_very_low/2026-09-04T090000Z-codex-fa3b24.yaml
    sha256: 8559b5b393e455e4b349d5c916f729c66435e071e32f1ef739964538f00fc5af
    role: context
  - path: history/records/temperature_delta_very_low/2026-09-04T110000Z-codex-183.yaml
    sha256: f1c20403c8ac77f63e7b27fb531020f851f4d35a3e36054c7c271b98a22bbc81
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
  - path: proposals/metpo_traitmech_v3/metpo_proposal_classes_robot.tsv
    sha256: 1a1cc789782cfae195c1fc81ddaf848d06d162c7434d94cceb66838de98ab6fa
    role: context
  - path: proposals/metpo_traitmech_v3/proposal.md
    sha256: 37be7b2c2efe0d1598d62b8df04f08262ba74b9d8068e010df6ee48069449067
    role: context
  - path: proposals/metpo_traitmech_v8/metpo_proposal_properties_robot.tsv
    sha256: 5445e86e845e0a2638292cff4586bf3858b1341d37fecf2e86cefcdbc9a046cd
    role: context
  - path: proposals/metpo_traitmech_v8/proposal.md
    sha256: 119d51e7b7194890514a9e313505212bab92aeba607f7c1b8f9d9d2edeef67e7
    role: context
  - path: proposals/metpo_traitmech_v85/metpo_proposal_classes_robot.tsv
    sha256: 6f32bf183eda67697a4d4c9920416473b0d09b78fab4f1d8d67140db68fb8550
    role: context
  - path: proposals/metpo_traitmech_v85/proposal.md
    sha256: b41cf306750f63743bf9d7c465f3e9ad8b4ec75f19a383d64e2187331d721f05
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
  - path: research/traits/environment/temperature_delta_high-deep-research-falcon.md
    sha256: 47ca735bc337b91cbc2f794e30905ecd991b5f592073658cca827d830f2fc9d8
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
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
  - path: scripts/repair_pr664_adversarial_review.py
    sha256: 5717a89bee383aa0e12aec9bf30434ccff74efcbe64684d13ef9b290b1accf96
    role: context
  - path: scripts/review_mesophilic_graph_183.py
    sha256: 46f9548808936268217a5e078fc1fa64d74cc2eeb69863ab6f3bb0da21e2b59c
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
- target_id: METPO:1000487
  path: data/traits/environment/temperature_delta_high.yaml
  label: temperature delta high
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_delta_high.yaml
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
  selection: Third record of the actual local batch 013 queue. Whole 394-line target
    and 90 inputs verified before judgment; local review does not assert remote publication.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - METPO:1000487
checks:
- check_id: audit-graphs
  name: Full-corpus graph audit
  status: passed
  required: true
  target_ids:
  - METPO:1000487
  command: just audit-graphs --out /private/tmp/traitmech-record-sweep.FU79Gr/causal_graph_audit.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  evidence_ids:
  - check-audit-graphs
  scope_note: 'Original common diagnostics ran at f25; history validation ran in batch003
    at8eee. Actual B12 final QC23:02:31.440808–23:04:01.628423UTC; B13 qualification23:05:39.165510
    and independent postcheck23:07:53.187524. Original failures/retries/skips and
    seven-file delta remain explicit; no fresh B13 QC or publication claimed. Qualification:
    /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-b12-qc-supplement-qualified.json'
- check_id: audit-snippets
  name: Full-corpus snippet audit
  status: passed
  required: true
  target_ids:
  - METPO:1000487
  command: just audit-snippets --report /private/tmp/traitmech-record-sweep.FU79Gr/evidence_snippet_audit.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  evidence_ids:
  - check-audit-snippets
  scope_note: 'Original common diagnostics ran at f25; history validation ran in batch003
    at8eee. Actual B12 final QC23:02:31.440808–23:04:01.628423UTC; B13 qualification23:05:39.165510
    and independent postcheck23:07:53.187524. Original failures/retries/skips and
    seven-file delta remain explicit; no fresh B13 QC or publication claimed. Qualification:
    /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-b12-qc-supplement-qualified.json'
- check_id: check-pathway-links
  name: Full-corpus pathway links
  status: passed
  required: true
  target_ids:
  - METPO:1000487
  command: just check-pathway-links
  exit_code: 0
  expected_exit_code: 0
  summary: 19 links checked against the pinned PathwayMech snapshot.
  evidence_ids:
  - check-check-pathway-links
  scope_note: 'Original common diagnostics ran at f25; history validation ran in batch003
    at8eee. Actual B12 final QC23:02:31.440808–23:04:01.628423UTC; B13 qualification23:05:39.165510
    and independent postcheck23:07:53.187524. Original failures/retries/skips and
    seven-file delta remain explicit; no fresh B13 QC or publication claimed. Qualification:
    /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-b12-qc-supplement-qualified.json'
- check_id: validate-history
  name: Full-corpus history integrity
  status: passed
  required: true
  target_ids:
  - METPO:1000487
  command: just validate-history
  exit_code: 0
  expected_exit_code: 0
  summary: 1277 history records checked, zero invalid links at the 8eee source base;
    integrity does not establish science or human acceptance.
  evidence_ids:
  - check-validate-history
  scope_note: 'Original common diagnostics ran at f25; history validation ran in batch003
    at8eee. Actual B12 final QC23:02:31.440808–23:04:01.628423UTC; B13 qualification23:05:39.165510
    and independent postcheck23:07:53.187524. Original failures/retries/skips and
    seven-file delta remain explicit; no fresh B13 QC or publication claimed. Qualification:
    /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-b12-qc-supplement-qualified.json'
- check_id: validate-products
  name: Initial full-product validation
  status: failed
  required: false
  target_ids:
  - METPO:1000487
  command: just validate-products
  exit_code: 2
  expected_exit_code: 0
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  evidence_ids:
  - check-validate-products
  scope_note: 'Original common diagnostics ran at f25; history validation ran in batch003
    at8eee. Actual B12 final QC23:02:31.440808–23:04:01.628423UTC; B13 qualification23:05:39.165510
    and independent postcheck23:07:53.187524. Original failures/retries/skips and
    seven-file delta remain explicit; no fresh B13 QC or publication claimed. Qualification:
    /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-b12-qc-supplement-qualified.json'
- check_id: validate-products-retry-local
  name: Product validation with isolated local cache
  status: failed
  required: false
  target_ids:
  - METPO:1000487
  command: just validate-products
  exit_code: 2
  expected_exit_code: 0
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  evidence_ids:
  - check-validate-products-retry-local
  scope_note: 'Original common diagnostics ran at f25; history validation ran in batch003
    at8eee. Actual B12 final QC23:02:31.440808–23:04:01.628423UTC; B13 qualification23:05:39.165510
    and independent postcheck23:07:53.187524. Original failures/retries/skips and
    seven-file delta remain explicit; no fresh B13 QC or publication claimed. Qualification:
    /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-b12-qc-supplement-qualified.json'
- check_id: validate-products-retry-network
  name: Product validation after isolated-cache download
  status: passed
  required: true
  target_ids:
  - METPO:1000487
  command: just validate-products
  exit_code: 0
  expected_exit_code: 0
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  evidence_ids:
  - check-validate-products-retry-network
  scope_note: 'Original common diagnostics ran at f25; history validation ran in batch003
    at8eee. Actual B12 final QC23:02:31.440808–23:04:01.628423UTC; B13 qualification23:05:39.165510
    and independent postcheck23:07:53.187524. Original failures/retries/skips and
    seven-file delta remain explicit; no fresh B13 QC or publication claimed. Qualification:
    /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-b12-qc-supplement-qualified.json'
- check_id: temperature-delta-high-validate
  name: Focused native validation
  status: passed
  required: true
  target_ids:
  - METPO:1000487
  command: just validate data/traits/environment/temperature_delta_high.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Successful native record validation; semantics assessed separately.
  evidence_ids:
  - check-temperature-delta-high-validate
- check_id: temperature-delta-high-strict
  name: Initial strict recipe invocation
  status: failed
  required: false
  target_ids:
  - METPO:1000487
  command: just validate-record-strict data/traits/environment/temperature_delta_high.yaml
  exit_code: 1
  expected_exit_code: 0
  summary: Nonexistent validate-record-strict recipe failed before strict validation.
    Optional superseded invocation, not completed-review validation failure.
  evidence_ids:
  - check-temperature-delta-high-strict
- check_id: temperature-delta-high-strict-corrected
  name: Corrected focused strict validation
  status: passed
  required: true
  target_ids:
  - METPO:1000487
  command: just validate-strict data/traits/environment/temperature_delta_high.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual validate-strict recipe passed after naming correction.
  evidence_ids:
  - check-temperature-delta-high-strict-corrected
- check_id: temperature-delta-high-snippets-network
  name: Focused network snippet check
  status: passed
  required: true
  target_ids:
  - METPO:1000487
  command: just verify-snippets --record data/traits/environment/temperature_delta_high.yaml
    --out /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-snippets.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 15 snippets:10 VERIFIED and5 NOT_IN_ABSTRACT; manual source review gives14
    literal and1 spelling discrepancy. No initial target-specific network failure
    is invented.
  evidence_ids:
  - check-temperature-delta-high-snippets-network
- check_id: batch012-qc
  name: Qualified batch-twelve QC
  status: passed
  required: true
  target_ids:
  - METPO:1000487
  command: just qc
  exit_code: 0
  expected_exit_code: 0
  summary: Actual prior QC qualified against B13 bytes; local continuation is independent
    of publication.
  evidence_ids:
  - check-batch012-qc
- check_id: uniprot-applicability
  name: Protein-instance metadata applicability
  status: not_applicable
  required: false
  target_ids:
  - METPO:1000487
  summary: Zero protein classes or instances. Desaturase activity and thermostability
    quality are not protein instances; no token protein requirement.
  evidence_ids:
  - record
  - policy
  - expression
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
- evidence_id: check-temperature-delta-high-validate
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-validate.log
  locator: Executed 2026-10-21T23:37:24.189596+00:00 through 2026-10-21T23:37:24.940228+00:00;
    metadata temperature-delta-high-validate.json
  accessed_at: '2026-10-21T23:37:24.940228Z'
  support: context_only
  summary: Successful native record validation; semantics assessed separately.
  snapshot_sha256: afece28d2cc5448aff7c7881d81f9042a59245c77f69bfb8da7b9e983a4c7c12
- evidence_id: check-temperature-delta-high-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-strict.log
  locator: Executed 2026-10-21T23:37:24.189547+00:00 through 2026-10-21T23:37:24.195545+00:00;
    metadata temperature-delta-high-strict.json
  accessed_at: '2026-10-21T23:37:24.195545Z'
  support: context_only
  summary: Nonexistent validate-record-strict recipe failed before strict validation.
    Optional superseded invocation, not completed-review validation failure.
  snapshot_sha256: bdaf4381c2fed5914ec46e1073c5cdc42a75539c0b63e7fbd99a3abec59942ff
- evidence_id: check-temperature-delta-high-strict-corrected
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-strict-corrected.log
  locator: Executed 2026-10-21T23:37:29.736875+00:00 through 2026-10-21T23:37:31.372700+00:00;
    metadata temperature-delta-high-strict-corrected.json
  accessed_at: '2026-10-21T23:37:31.372700Z'
  support: context_only
  summary: Actual validate-strict recipe passed after naming correction.
  snapshot_sha256: 4605a37f1e37d0694195718af3b14a0728c4827de7aa0a333dbfe42a112161ac
- evidence_id: check-temperature-delta-high-snippets-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-snippets-network.log
  locator: Executed 2026-10-21T23:37:34.939425+00:00 through 2026-10-21T23:37:40.009911+00:00;
    metadata temperature-delta-high-snippets-network.json
  accessed_at: '2026-10-21T23:37:40.009911Z'
  support: context_only
  summary: 15 snippets:10 VERIFIED and5 NOT_IN_ABSTRACT; manual source review gives14
    literal and1 spelling discrepancy. No initial target-specific network failure
    is invented.
  snapshot_sha256: 6774cf10324acb2b5cd1b0500be24171b7d56764cf87b589b6a4de9cb73dc730
- evidence_id: check-batch012-qc
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/batch012-qc.log
  locator: Executed 2026-10-21T23:02:31.440808+00:00 through 2026-10-21T23:04:01.628423+00:00;
    metadata batch012-qc.json
  accessed_at: '2026-10-21T23:04:01.628423Z'
  support: context_only
  summary: Actual prior QC qualified against B13 bytes; local continuation is independent
    of publication.
  snapshot_sha256: 8ab67b821055863ce13616ed79a0acacaf61b632dcb80f6aa63fd45f0485c52b
- evidence_id: record
  kind: record_content
  reference: data/traits/environment/temperature_delta_high.yaml
  locator: Whole current394-line record
  accessed_at: '2026-10-21T23:37:10.153046Z'
  support: supports
  summary: All 14 nodes and 13 edges,17 events and one canonical example.
  snapshot_sha256: 5a14c751b66b3593df2f558e50cedd4983484d782915e1b167e1404eebf12418
- evidence_id: reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-b12-qc-supplement-qualified.json
  locator: Actual B12-to-B13 qualification
  accessed_at: '2026-10-21T23:05:39.165510Z'
  support: supports
  summary: Original outcomes and current byte comparisons.
  snapshot_sha256: e1fa58cb626ef76e2b2066404078b9893b069a5b53a0cffbc3a184e68f0cd9f1
- evidence_id: reuse-postcheck
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-output-verification-agent/post-execution-verification.json
  locator: Independent actual-output verification
  accessed_at: '2026-10-21T23:07:53.187524Z'
  support: supports
  summary: Actual qualification/hash postcheck, not new QC.
  snapshot_sha256: 42a5580991e7251963a9b83d0817facda019de29d9e13208e870c27e1c62ad7d
- evidence_id: local-init
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/batch013-local-initialization-receipt.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:09:00.804479Z'
  support: supports
  summary: Actual local initialization; publication status is separate.
  snapshot_sha256: cda5c0d3753e7a2a3ceb9ba723261fa79d4f760aad1713ff2d33b08def3577f7
- evidence_id: policy
  kind: authority
  reference: docs/GROUNDING_POLICY.md
  locator: Captured maintained authority
  accessed_at: '2026-10-21T23:41:45.008944Z'
  support: supports
  summary: Actual node referents and optional protein applicability.
  snapshot_sha256: 891678c983c2283a47c81c47950b35753981e9339d105f3bbdda92a1f5ab7f42
- evidence_id: playbook
  kind: authority
  reference: docs/CURATION_PLAYBOOK.md
  locator: Captured maintained authority
  accessed_at: '2026-10-21T23:41:45.008944Z'
  support: supports
  summary: Verbatim source scope and attributable acceptance.
  snapshot_sha256: 735e9b810471da9f7d8364e35ffe1e741edb3421480dac01727db6ea5aa65da9
- evidence_id: schema
  kind: authority
  reference: src/traitmech/schema/traitmech.yaml
  locator: Captured maintained authority
  accessed_at: '2026-10-21T23:41:45.008944Z'
  support: supports
  summary: Current node facets and graph scope.
  snapshot_sha256: 46c47fc627b80ccbba1e8ab3fb6f2aee93bc2aef7aaf72fe9aadc3257f2c02dd
- evidence_id: checklist
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Captured maintained authority
  accessed_at: '2026-10-21T23:41:45.008944Z'
  support: supports
  summary: Whole-record review coverage.
  snapshot_sha256: da8896328a0fd6cc92f1adf0d8be8980d0ddd41f3172c7936f2c7f119b293ac1
- evidence_id: predicate-mapping
  kind: authority
  reference: mappings/predicate_grounding.tsv
  locator: Captured maintained authority
  accessed_at: '2026-10-21T23:41:45.008944Z'
  support: supports
  summary: Future-empty predicate mapping, with current skip-existing guard.
  snapshot_sha256: 8e28c19e93aca3dc164a3befbe2612b289241de457c59f499e65936c03b7ce52
- evidence_id: local-v3
  kind: authority
  reference: proposals/metpo_traitmech_v3/metpo_proposal_classes_robot.tsv
  locator: Captured maintained authority
  accessed_at: '2026-10-21T23:41:45.008944Z'
  support: supports
  summary: 1007505 fluidity quality.
  snapshot_sha256: 1a1cc789782cfae195c1fc81ddaf848d06d162c7434d94cceb66838de98ab6fa
- evidence_id: local-v8
  kind: authority
  reference: proposals/metpo_traitmech_v8/metpo_proposal_properties_robot.tsv
  locator: Captured maintained authority
  accessed_at: '2026-10-21T23:41:45.008944Z'
  support: supports
  summary: 2007700 confers broad formal roles and trait object.
  snapshot_sha256: 5445e86e845e0a2638292cff4586bf3858b1341d37fecf2e86cefcdbc9a046cd
- evidence_id: local-v85
  kind: authority
  reference: proposals/metpo_traitmech_v85/metpo_proposal_classes_robot.tsv
  locator: Captured maintained authority
  accessed_at: '2026-10-21T23:41:45.008944Z'
  support: supports
  summary: 1016200 named homeoviscous process, including homoviscous spelling.
  snapshot_sha256: 6f32bf183eda67697a4d4c9920416473b0d09b78fab4f1d8d67140db68fb8550
- evidence_id: capture
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-ground-agent/capture-verification.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:39:37.811192Z'
  support: supports
  summary: All 90 inputs and whole current target verified.
  snapshot_sha256: 10db6dae1b04767ed1d6caca9244622e51ed85072c49f04044b6472e07e8846f
- evidence_id: identity
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-ground-agent/identity-assessment.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:41:45.004808Z'
  support: supports
  summary: Active target/parent, local placeholders and exact30 qualification.
  snapshot_sha256: 43924c6000b74c021eb888142ad7067ea69ad783c3b147e2e0846fb709f62267
- evidence_id: nodes-edges
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-ground-agent/node-edge-grounding-ledger.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:41:45.005425Z'
  support: supports
  summary: All 14 nodes and 13 edges; formal positives and six grouped conflicts.
  snapshot_sha256: 512a971b570237702ebbaed701f9cb422c65163c56767de5a5884b02922d1e40
- evidence_id: owners
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-ground-agent/owner-provenance-assessment.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:41:45.007690Z'
  support: supports
  summary: Exact current direct writers and recurrence guards.
  snapshot_sha256: 5a7206218f03c4fe0cbc0fc911999831c46e8b82568ef837a496170960e11509
- evidence_id: owner-primary
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-ground-agent/owner-primary-reading.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:41:44.904155Z'
  support: supports
  summary: Actual direct reviewer, connector, repair and shared-grounder windows.
  snapshot_sha256: d0b969ac2f1c0469fd46b250bbb8a3e96ddfe0b06aa088961c70b5743c370528
- evidence_id: writer-state
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-ground-agent/writer-current-state-comparison.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:41:44.946681Z'
  support: supports
  summary: AST literal comparisons only; no maintained writer execution.
  snapshot_sha256: 6afe8059e7b4daa13c097c74491c5c49edc4df648a9075ab9dcc8bccfe68967d
- evidence_id: human-search
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-ground-agent/search-and-provenance.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:38:55.932795Z'
  support: supports
  summary: 179 ignored-inclusive matching paths, 68 actual arrays, zero exact target.
  snapshot_sha256: e0a5e3e0d4fa14e02d8f8859d265e94a1cd8b2e8ee7aff49c5f3c29eb4b5e646
- evidence_id: histories
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-ground-agent/history-reading-provenance.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:41:45.006773Z'
  support: supports
  summary: All 13 current projections; four current whole reads and nine prior whole
    reads reused by exact hash.
  snapshot_sha256: e17bf7077bf751a0d10bc1f1b7b51841f68319d266efe87a52b76caff4245c0a
- evidence_id: ground-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-ground-agent/reading-scope-receipt.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:41:45.009456Z'
  support: supports
  summary: Precise primary/history and excluded-science reading scopes.
  snapshot_sha256: 2cd00ef51f975ac94e3a876d6769cd057d21a0dea591a45a45b9b621aaaf4e64
- evidence_id: expression
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-ground-agent/expression-and-readiness.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:41:45.008316Z'
  support: supports
  summary: Canonical absent from retained catalog; source species coverage separately
    positive.
  snapshot_sha256: 3410db437ca2d978611ad1c13146689d4e6f206e4a55bd9f4a5d967d8074c380
- evidence_id: catalog-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-ground-agent/catalog-reuse-receipt.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:39:08.555197Z'
  support: supports
  summary: Original 20-organism, 28-dataset provenance.
  snapshot_sha256: 2dbf712c62e450fc2a2d65a7dad584146d895bb98f1f88d502b9a5db671e0f5c
- evidence_id: local-authority
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-ground-agent/local-authority-reading.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:41:44.899128Z'
  support: supports
  summary: Local v3/v8/v85 and actual broad Biolink chain.
  snapshot_sha256: 09e486f4690c6d40e27b6f2fa13d0844fb87a15f8353b2fb76b72cc4e4a78634
- evidence_id: replacements
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-ground-agent/metpo-replacement-and-local-status.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:41:45.002791Z'
  support: supports
  summary: Exact imported replacement/local-status search.
  snapshot_sha256: c9c63b80d7ea6c35df07e5aa3bb9f6655c09c4903c83edb43920f8d12dda0fb3
- evidence_id: ground-manifest
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-ground-agent/evidence-manifest.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:41:45.025888Z'
  support: supports
  summary: Frozen 30 artifacts, all hashes checked.
  snapshot_sha256: 193e4cafcb0e7c394448890e4956ce228d74ae38213cb787677da00ead6c8b18
- evidence_id: ground-disposition
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-ground-agent/documentary-assessment.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:41:45.008944Z'
  support: supports
  summary: One formal major and bounded human minor.
  snapshot_sha256: db37d67a753b681cd844420a109f54ac55bae8421e9996508a03d4435536d8f3
- evidence_id: metpo-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/repo/data/raw/metpo.owl
  locator: Actual retained primary authority; selected projection separately bound
  accessed_at: '2026-10-21T23:38:55.797847Z'
  support: supports
  summary: Active1000487 numeric minInclusive30/Cel, parent1000303 and relatedTd_>30.
  snapshot_sha256: 8b6f8fe0510a698579e532658c8ace05da2550093365df9ca83feb0741778415
- evidence_id: metpo-primary-projection
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-ground-agent/metpo-authority.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:38:55.797847Z'
  support: supports
  summary: Selected current primary statements, not a replacement for raw authority.
  snapshot_sha256: 8a8a802da1e90b2632361c5bddd3f90a06064eb5fdfcb93a446324636ef4c559
- evidence_id: ro-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/ro.db
  locator: Actual retained primary authority; selected projection separately bound
  accessed_at: '2026-10-21T23:38:55.074908Z'
  support: supports
  summary: Actual material/process and process/process inherited roles.
  snapshot_sha256: 849e616c29fecd0d4a6c6dee0dc0f6f117ace7167dbfa1e0f043dc84868f83cb
- evidence_id: ro-primary-projection
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-ground-agent/selected-ro-primary-reading.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:38:55.074908Z'
  support: supports
  summary: Selected current primary statements, not a replacement for raw authority.
  snapshot_sha256: 8f8d843432d58421f0c7c689850a18140ef7faa2d8b5fc9e3891a37c25e15a7f
- evidence_id: go-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/go.db
  locator: Actual retained primary authority; selected projection separately bound
  accessed_at: '2026-10-21T23:38:55.079307Z'
  support: supports
  summary: GO0006636 exact unsaturated-fatty-acid biosynthetic-process identity.
  snapshot_sha256: 018a7ef0a5bd1c0767abc3d71b413264a25be7579533daf5349f739cd9a122cd
- evidence_id: go-primary-projection
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-ground-agent/selected-go-primary-reading.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:38:55.079307Z'
  support: supports
  summary: Selected current primary statements, not a replacement for raw authority.
  snapshot_sha256: bfe8479154424cec4c7e328e0737dcbd1754f11867151bbf098913e62cdf7242
- evidence_id: taxonomy
  kind: authority
  reference: NCBITaxon:1385984
  locator: Whole successful official XML, current network retry
  accessed_at: '2026-10-21T23:40:02.749930Z'
  support: supports
  summary: Exiguobacterium chiriqhucha and RW-2 type material; taxonomy does not establish
    phenotype.
  snapshot_sha256: 1d5df4a9a97eeb88cd852f5833e11d2b9ab21cf7e5d76c4d6e8be6a2c4ed1289
- evidence_id: taxonomy-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-ground-agent/taxonomy-network-retry-access.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:40:02.749930Z'
  support: supports
  summary: Actual successful taxonomy access, distinct from initial DNS failure.
  snapshot_sha256: 091b18221637288bc4a472a0045b2258835646053ee9574472da2d8377094fed
- evidence_id: taxonomy-initial
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-ground-agent/taxonomy-access.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:39:52.073168Z'
  support: supports
  summary: Retained initial DNS failure, not a primary XML or identity contradiction.
  snapshot_sha256: 1d20324503e9bac985d4d8a26e2d9de9cdd2663ca7ac6560a1df86857d5ec3d6
- evidence_id: mendoza
  kind: primary_source
  reference: DOI:10.1146/annurev-micro-091313-103612
  locator: Retained indexed metadata/abstract; not full body
  accessed_at: '2026-10-21T10:00:02.042457Z'
  support: supports
  summary: Generic membrane context and supplied abstract spelling; exact breadth
    calibration unknown.
  snapshot_sha256: 801da630644a181211f991a6f21c49b178e42a65f615c4eebd8196bc29244588
- evidence_id: vieille
  kind: primary_source
  reference: DOI:10.1128/MMBR.65.1.1-43.2001
  locator: Retained indexed metadata/abstract; not full body
  accessed_at: '2026-10-21T11:23:22.820553Z'
  support: supports
  summary: Generic thermostability context and supplied abstract span; exact breadth
    bridge unknown.
  snapshot_sha256: 7fbda4bf0eea7b0c1641d88dc150329587687249fd800726e14b7f84a9670e0c
- evidence_id: wu-metadata
  kind: primary_source
  reference: DOI:10.3390/cells12101353
  locator: Indexed metadata/abstract
  accessed_at: '2026-10-21T23:37:50.878181Z'
  support: supports
  summary: Source identity and notice fields only.
  snapshot_sha256: b62f7028eb519d5ca43eccb5d7d7815ef5b00e3337567a26a7522c1bc20586db
- evidence_id: canonical-metadata
  kind: primary_source
  reference: DOI:10.3389/fmicb.2018.03189
  locator: Indexed metadata/abstract
  accessed_at: '2026-10-21T23:37:50.892115Z'
  support: supports
  summary: Canonical source identity and existing growth classification.
  snapshot_sha256: 1403fd32eb73364c347fb95451f2c8cba9df7419382e6f6d9ea11f263fd4db12
- evidence_id: wu-primary
  kind: primary_source
  reference: DOI:10.3390/cells12101353
  locator: JATS body paragraphs2/4/5/6,zero based
  accessed_at: '2026-10-21T23:38:05.360966Z'
  support: supports
  summary: Supplied fragments and generic physical context; no detailed intervention/efficacy
    inference.
  snapshot_sha256: a531fd8e0c7db35efe00239339ef6adfda3a40c0ed7ecaad21a0a5d44ad3eb0f
- evidence_id: canonical-primary
  kind: primary_source
  reference: DOI:10.3389/fmicb.2018.03189
  locator: JATS abstract and first sentences of body44/68,zero based; existing condition
    cross-check13
  accessed_at: '2026-10-21T23:38:05.505767Z'
  support: supports
  summary: RW2 reported growth4–50 °C supports46 °C breadth; historical ranking is
    not a current universal claim.
  snapshot_sha256: 7fd7b4cb84d4395e7d2a780cc9b20c5e3e170e00c18e790225af0a0be1515bc3
- evidence_id: mendoza-browser
  kind: primary_source
  reference: https://www.annualreviews.org/doi/10.1146/annurev-micro-091313-103612
  locator: Retained browser tool response, publisher abstract; not raw HTML or independently
    known origin/cache-fetch time
  accessed_at: '2026-10-21T23:38:35Z'
  support: refutes
  summary: Current publisher abstract agrees with indexed homoviscous spelling; only
    the narrow copied-span claim is challenged.
  snapshot_sha256: b8635235ad5e362d0b33ef4834f84eb25fe7ff6b1bd1321affb2b61cecbc66fc
- evidence_id: sources
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-source-agent/source-assessment.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:41:51.206924Z'
  support: supports
  summary: Four works, overall UNKNOWN, one bounded copied-span minor.
  snapshot_sha256: c5f89c0794e5a6be52be649e401b698d4ffcabf51c6d95f3689b6940ad690aa6
- evidence_id: source-identities
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-source-agent/source-identities.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:40:45.051272Z'
  support: supports
  summary: Actual identities and assigned-work scope.
  snapshot_sha256: 2e6ae518a7dbd9a01d4418e7292be3e8ff221c3ae57764a769653de6f686a9cc
- evidence_id: placements
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-source-agent/source-placement-ledger.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:41:51.202791Z'
  support: supports
  summary: All 17 external placements and structured grounding accounting.
  snapshot_sha256: 62118544f3dd4c274e5925eeb07a86c91024d18be3ced4a5a84bf0f584336cfa
- evidence_id: snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-source-agent/snippet-ledger.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:40:45.051443Z'
  support: supports
  summary: 15 supplied snippets:14 literal,one spelling discrepancy.
  snapshot_sha256: dcf682e9192df5116e6f3143d7f55d3c19797e4bf6b920ca7f8d788e63579b2b
- evidence_id: copy-discrepancy
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-source-agent/copied-span-assessment.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:41:51.204177Z'
  support: supports
  summary: Homeoviscous/homoviscous exact quotation difference preserves concept meaning.
  snapshot_sha256: 77dfeded6f141488597c1266d58f505f089080c6be9f0d35467ca4a41d53f5cc
- evidence_id: source-nodes-edges
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-source-agent/node-edge-source-ledger.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:41:51.203118Z'
  support: supports
  summary: All14node/13edge source judgments.
  snapshot_sha256: c6874fb57bcc0e377dbc001a1c58c1470b5aa2510d4970fc347acf18c33ebcfd
- evidence_id: source-status
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-source-agent/source-status-ledger.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:41:51.204871Z'
  support: supports
  summary: Bounded notice checks, not exhaustive current publication search.
  snapshot_sha256: eccc3033d4180342e7ffcf13982730326ef6bb88db63698898306c27999b7ef6
- evidence_id: source-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-source-agent/primary-reading-scope.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:41:51.206703Z'
  support: supports
  summary: Selected abstracts/body paragraphs; no whole-article reading claim.
  snapshot_sha256: 5876574d9dbfc9e7950b5b1c101f32a5980798dc437c032867acaf68d7553900
- evidence_id: source-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-source-agent/source-access-limits.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:41:51.204949Z'
  support: supports
  summary: HTTP403/500 and unavailable full bodies remain access limits, not refutations.
  snapshot_sha256: 009ac21c02ca3cabee1501474122e270c2383d59f1d4e6a52dc5531ad9511903
- evidence_id: source-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-source-agent/source-reuse-receipt.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:40:45.032604Z'
  support: supports
  summary: Original 10:00/11:23 metadata acquisition differs from current copy/read
    times.
  snapshot_sha256: 4b1b9af4d6d741a99ed91ee86f3ede58f19d225723eb3f8d90461632991c9923
- evidence_id: canonical
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-source-agent/canonical-assessment.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:41:51.203292Z'
  support: supports
  summary: Source-specific growth interval and46 °C arithmetic positive.
  snapshot_sha256: 22ae57b9b8170c80617f7408c549948504e2be2a3ce0f4baf461e0dbac2e824b
- evidence_id: source-checks
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-source-agent/native-check-context.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:41:51.206584Z'
  support: supports
  summary: Actual failed wrong recipe and corrected strict plus10/5native snippet
    outcomes.
  snapshot_sha256: 0542402a9ec0e8f494953fd4e9ebe532c222ca49589f407cd94e79fb15d00781
- evidence_id: source-manifest
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-source-agent/evidence-manifest.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:41:51.221471Z'
  support: supports
  summary: Frozen 35 artifacts, all hashes checked.
  snapshot_sha256: 62bd3436be6fd7df94fecaa346c8a0db142a20f54431f7bb2ed5a6951aca36cc
- evidence_id: root-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-source-root/root-primary-reading.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:39:15.461220Z'
  support: supports
  summary: Actual root primary authority and source reading, bounded to recorded scopes.
  snapshot_sha256: 05c0dae1c6d227894273d8969c37d346719ffada4bbdf86ff72418810980b95b
- evidence_id: root-ledgers
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-source-root/root-ledger-reading.json
  locator: Derived audit, reading or access receipt; primary bytes separately identified
  accessed_at: '2026-10-21T23:42:53.528700Z'
  support: supports
  summary: Actual source/ground/owner ledgers and history projection scope.
  snapshot_sha256: 244e3666361e30a56ee756e21002ab9b547744711a429c06b0c285369e9f7e0f
- evidence_id: challenge
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-semantic-challenge-agent/semantic-severity-challenge.json
  locator: Final independent semantic challenge
  accessed_at: '2026-10-21T23:43:36.946093Z'
  support: supports
  summary: Actual frozen grouping/severity and all bound evidence verified.
  snapshot_sha256: 196239fe545efae78a0d30a454b6ee7dc4157b60c780be8898f2806e8c21c872
- evidence_id: adjudication
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-high-root-adjudication.json
  locator: Final root adjudication
  accessed_at: '2026-10-21T23:44:08.372469Z'
  support: supports
  summary: One major and two minors; exact field/action parity controls serialization.
  snapshot_sha256: 190a60505c63ed9638a892beea18c4122a26fdfe3cd01e04268ebace8d62772f
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: active identity and hierarchy'
  outcome: supported
  target_ids:
  - METPO:1000487
  summary: Active1000487 and parent1000303 align. Local1016200/1007505 placeholders
    and GO0006636 are positive; official1385984 and RW-2 type material match.
  evidence_ids:
  - identity
  - metpo-primary
  - local-v3
  - local-v85
  - go-primary
  - taxonomy
- assessment_id: definition
  area: quantity
  topic: 'Native checklist: numeric boundary and source calibration'
  outcome: unknown
  target_ids:
  - METPO:1000487
  summary: Raw METPO minInclusive30 and relatedTd_>30 differ at exact30; current approximate-above30
    prose is qualified, not a separate wrong-ID finding. Exact source calibration
    beyond inspected generic abstracts remains unknown.
  evidence_ids:
  - identity
  - metpo-primary
  - sources
  - placements
- assessment_id: canonical-example
  area: quantity
  topic: 'Native checklist: measured growth breadth'
  outcome: supported
  target_ids:
  - METPO:1000487
  summary: RW2 reported4–50 °C growth gives46 °C breadth under attached source conditions.
    Historical broadest-in-genus language is not independently current; no experiment
    or intervention proposed.
  evidence_ids:
  - canonical
  - canonical-primary
  - taxonomy
- assessment_id: source-support
  area: evidence
  topic: 'Native checklist: four works and 17 placements'
  outcome: unknown
  target_ids:
  - METPO:1000487
  summary: Source identities and generic physical context are positive. Full Mendoza/Vieille
    bodies unavailable; joint adaptation and extreme-breadth causal calibration remain
    unknown, not disproved.
  evidence_ids:
  - sources
  - source-identities
  - placements
  - source-access
  - source-status
- assessment_id: quotations
  area: evidence
  topic: 'Native checklist: all 15 supplied fragments'
  outcome: concern
  target_ids:
  - METPO:1000487
  summary: Manual14 literal matches and one copied-span discrepancy. Edge8 record
    homeoviscous differs from inspected publisher/indexed homoviscous despite abstract-verification
    note; scientific meaning is unchanged. Native 10 VERIFIED / 5 NOT_IN_ABSTRACT
    is not manual15-way adjudication.
  evidence_ids:
  - snippets
  - copy-discrepancy
  - mendoza
  - mendoza-browser
  - source-checks
- assessment_id: nodes
  area: representation
  topic: 'Native checklist: all 14 current referents'
  outcome: unknown
  target_ids:
  - METPO:1000487
  summary: Identity/facets mostly align. Node2 capacity/process and node11 chemical/composition-shift
    wording remain qualified. Molecular activity need not be a material protein; thermostability
    is a quality.
  evidence_ids:
  - nodes-edges
  - schema
  - local-authority
  details: "{\n  \"grounding\": [\n    {\n      \"index\": 0,\n      \"node_id\":\
    \ \"temperature_delta_high_trait\",\n      \"label\": \"temperature delta high\"\
    ,\n      \"node_type\": \"TRAIT\",\n      \"grounding\": \"METPO:1000487\",\n\
    \      \"outcome\": \"supported\",\n      \"assessment\": \"Active exact numeric\
    \ target; exact30 precision retained as limitation.\",\n      \"biological_support\"\
    : \"UNASSESSED_SCOPE for detailed survival/fitness or intervention mechanisms\"\
    \n    },\n    {\n      \"index\": 1,\n      \"node_id\": \"temperature_delta\"\
    ,\n      \"label\": \"temperature delta\",\n      \"node_type\": \"TRAIT\",\n\
    \      \"grounding\": \"METPO:1000303\",\n      \"outcome\": \"supported\",\n\
    \      \"assessment\": \"Active exact broader temperature-breadth parent.\",\n\
    \      \"biological_support\": \"UNASSESSED_SCOPE for detailed survival/fitness\
    \ or intervention mechanisms\"\n    },\n    {\n      \"index\": 2,\n      \"node_id\"\
    : \"maximal_thermal_adaptation\",\n      \"label\": \"maximal thermal-adaptation\
    \ flexibility\",\n      \"node_type\": \"BIOLOGICAL_PROCESS\",\n      \"grounding\"\
    : null,\n      \"outcome\": \"unknown\",\n      \"assessment\": \"Combined adaptation\
    \ capacity wording can be disposition or process shorthand. Do not force reservoir\
    \ CAPACITY enum; local confers allows broad mechanisms and no separate type finding\
    \ is established.\",\n      \"biological_support\": \"UNASSESSED_SCOPE for detailed\
    \ survival/fitness or intervention mechanisms\"\n    },\n    {\n      \"index\"\
    : 3,\n      \"node_id\": \"decreased_growth_temperature\",\n      \"label\": \"\
    decreased growth temperature\",\n      \"node_type\": \"ENVIRONMENTAL_FACTOR\"\
    ,\n      \"grounding\": null,\n      \"outcome\": \"supported\",\n      \"assessment\"\
    : \"Description denotes a decrease in ambient temperature, an event. ENVIRONMENTAL_FACTOR\
    \ includes exposure/condition and does not categorically exclude event/process\
    \ interpretation.\",\n      \"biological_support\": \"UNASSESSED_SCOPE for detailed\
    \ survival/fitness or intervention mechanisms\"\n    },\n    {\n      \"index\"\
    : 4,\n      \"node_id\": \"unsaturated_fatty_acid_biosynthesis\",\n      \"label\"\
    : \"unsaturated fatty acid biosynthesis\",\n      \"node_type\": \"BIOLOGICAL_PROCESS\"\
    ,\n      \"grounding\": \"GO:0006636\",\n      \"outcome\": \"supported\",\n \
    \     \"assessment\": \"GO0006636 label/definition directly identifies unsaturated-fatty-acid\
    \ biosynthetic process, aligned with current node; no PUFA-specific mapping issue\
    \ copied from other records.\",\n      \"biological_support\": \"UNASSESSED_SCOPE\
    \ for detailed survival/fitness or intervention mechanisms\"\n    },\n    {\n\
    \      \"index\": 5,\n      \"node_id\": \"homoviscous_adaptation\",\n      \"\
    label\": \"homoviscous adaptation\",\n      \"node_type\": \"BIOLOGICAL_PROCESS\"\
    ,\n      \"grounding\": \"METPO:1016200\",\n      \"outcome\": \"supported\",\n\
    \      \"assessment\": \"Exact spelling variant is provided by local v85 proposal\
    \ and mapping row133; current process sense distinguished from physical fluidity\
    \ quality.\",\n      \"biological_support\": \"UNASSESSED_SCOPE for detailed survival/fitness\
    \ or intervention mechanisms\"\n    },\n    {\n      \"index\": 6,\n      \"node_id\"\
    : \"membrane_fluidity_homeostasis\",\n      \"label\": \"membrane fluidity homeostasis\"\
    ,\n      \"node_type\": \"BIOLOGICAL_PROCESS\",\n      \"grounding\": null,\n\
    \      \"outcome\": \"supported\",\n      \"assessment\": \"Maintenance of fluidity/permeability\
    \ is explicitly a process; exact node-type consistency writer agrees.\",\n   \
    \   \"biological_support\": \"UNASSESSED_SCOPE for detailed survival/fitness or\
    \ intervention mechanisms\"\n    },\n    {\n      \"index\": 7,\n      \"node_id\"\
    : \"decreased_membrane_fluidity\",\n      \"label\": \"decreased membrane fluidity\"\
    ,\n      \"node_type\": \"STATE\",\n      \"grounding\": null,\n      \"outcome\"\
    : \"supported\",\n      \"assessment\": \"Reduced membrane-fluidity state, not\
    \ the sensing or establishment process. This referent drives edge4 concern.\"\
    ,\n      \"biological_support\": \"UNASSESSED_SCOPE for detailed survival/fitness\
    \ or intervention mechanisms\"\n    },\n    {\n      \"index\": 8,\n      \"node_id\"\
    : \"lipid_desaturase_activity\",\n      \"label\": \"lipid desaturase activity\"\
    ,\n      \"node_type\": \"MOLECULAR_FUNCTION\",\n      \"grounding\": null,\n\
    \      \"outcome\": \"supported\",\n      \"assessment\": \"Molecular activity\
    \ of lipid desaturation can be processual. It is not automatically a material\
    \ protein; edge5 fails independently at quality object.\",\n      \"biological_support\"\
    : \"UNASSESSED_SCOPE for detailed survival/fitness or intervention mechanisms\"\
    \n    },\n    {\n      \"index\": 9,\n      \"node_id\": \"membrane_fluidity\"\
    ,\n      \"label\": \"membrane fluidity\",\n      \"node_type\": \"QUALITY\",\n\
    \      \"grounding\": \"METPO:1007505\",\n      \"outcome\": \"supported\",\n\
    \      \"assessment\": \"Physical membrane-fluidity quality, supported by exact\
    \ v3 proposal and current mapping50.\",\n      \"biological_support\": \"UNASSESSED_SCOPE\
    \ for detailed survival/fitness or intervention mechanisms\"\n    },\n    {\n\
    \      \"index\": 10,\n      \"node_id\": \"membrane_viscosity_high_temperature\"\
    ,\n      \"label\": \"membrane viscosity at higher temperature\",\n      \"node_type\"\
    : \"QUALITY\",\n      \"grounding\": null,\n      \"outcome\": \"supported\",\n\
    \      \"assessment\": \"Membrane-viscosity quality retained as such; no requirement\
    \ for universal grounding.\",\n      \"biological_support\": \"UNASSESSED_SCOPE\
    \ for detailed survival/fitness or intervention mechanisms\"\n    },\n    {\n\
    \      \"index\": 11,\n      \"node_id\": \"increased_fatty_acid_diversity\",\n\
    \      \"label\": \"increased short-/branched-/unsaturated fatty acids\",\n  \
    \    \"node_type\": \"CHEMICAL\",\n      \"grounding\": null,\n      \"outcome\"\
    : \"unknown\",\n      \"assessment\": \"Chemical enum and shift-of-composition\
    \ description leave entity-versus-change precision qualified. Edge6 quality object\
    \ independently conflicts with RO process range; no separate forced retype or\
    \ new finding.\",\n      \"biological_support\": \"UNASSESSED_SCOPE for detailed\
    \ survival/fitness or intervention mechanisms\"\n    },\n    {\n      \"index\"\
    : 12,\n      \"node_id\": \"thermostable_enzyme\",\n      \"label\": \"hyperthermophilic\
    \ enzyme thermostability\",\n      \"node_type\": \"QUALITY\",\n      \"grounding\"\
    : null,\n      \"outcome\": \"supported\",\n      \"assessment\": \"Actual label/description\
    \ denotes enzyme thermostability QUALITY, despite node_id shorthand. Not a protein\
    \ class or instance. Its quality subject conflicts with edge7 process domain.\"\
    ,\n      \"biological_support\": \"UNASSESSED_SCOPE for detailed survival/fitness\
    \ or intervention mechanisms\"\n    },\n    {\n      \"index\": 13,\n      \"\
    node_id\": \"irreversible_protein_inactivation\",\n      \"label\": \"irreversible\
    \ inactivation at high temperatures\",\n      \"node_type\": \"BIOLOGICAL_PROCESS\"\
    ,\n      \"grounding\": null,\n      \"outcome\": \"supported\",\n      \"assessment\"\
    : \"Irreversible protein-inactivation process; negative polarity refers to damage/inactivation\
    \ and is not reversed positive-integrity polarity.\",\n      \"biological_support\"\
    : \"UNASSESSED_SCOPE for detailed survival/fitness or intervention mechanisms\"\
    \n    }\n  ],\n  \"source\": [\n    {\n      \"index\": 0,\n      \"field\": \"\
    causal_graphs[0].nodes[0]\",\n      \"node_id\": \"temperature_delta_high_trait\"\
    ,\n      \"outcome\": \"unknown\",\n      \"assessment\": \"Current >30 °C bin\
    \ is explicit in the record; exact source threshold calibration is unresolved\
    \ from inspected Mendoza abstract.\"\n    },\n    {\n      \"index\": 1,\n   \
    \   \"field\": \"causal_graphs[0].nodes[1]\",\n      \"node_id\": \"temperature_delta\"\
    ,\n      \"outcome\": \"supported_at_definition_scope\",\n      \"assessment\"\
    : \"Growth-supporting breadth is distinguished from optimum and survival; canonical\
    \ arithmetic is independently positive.\"\n    },\n    {\n      \"index\": 2,\n\
    \      \"field\": \"causal_graphs[0].nodes[2]\",\n      \"node_id\": \"maximal_thermal_adaptation\"\
    ,\n      \"outcome\": \"unknown\",\n      \"assessment\": \"Combined maximal adaptation\
    \ capacity is an explicit synthesis; inspected generic sources do not measure\
    \ this construct or establish exclusive >30 °C sufficiency.\"\n    },\n    {\n\
    \      \"index\": 3,\n      \"field\": \"causal_graphs[0].nodes[3]\",\n      \"\
    node_id\": \"decreased_growth_temperature\",\n      \"outcome\": \"supported_at_generic_scope\"\
    ,\n      \"assessment\": \"Temperature decrease is the generic environmental context\
    \ explicitly present in Mendoza abstract.\"\n    },\n    {\n      \"index\": 4,\n\
    \      \"field\": \"causal_graphs[0].nodes[4]\",\n      \"node_id\": \"unsaturated_fatty_acid_biosynthesis\"\
    ,\n      \"outcome\": \"supported_at_generic_scope\",\n      \"assessment\": \"\
    Existing UFA biosynthesis wording is covered by supplied Mendoza abstract spans;\
    \ no detailed gene/pathway or intervention assessment.\"\n    },\n    {\n    \
    \  \"index\": 5,\n      \"field\": \"causal_graphs[0].nodes[5]\",\n      \"node_id\"\
    : \"homoviscous_adaptation\",\n      \"outcome\": \"supported_at_generic_scope\"\
    ,\n      \"assessment\": \"Named adaptation process is explicit in the current\
    \ publisher abstract; exact copied-spelling issue is isolated at edge8.\"\n  \
    \  },\n    {\n      \"index\": 6,\n      \"field\": \"causal_graphs[0].nodes[6]\"\
    ,\n      \"node_id\": \"membrane_fluidity_homeostasis\",\n      \"outcome\": \"\
    supported_at_generic_scope\",\n      \"assessment\": \"Generic membrane fluidity\
    \ maintenance context is supported; all-condition or all-taxon performance is\
    \ not established.\"\n    },\n    {\n      \"index\": 7,\n      \"field\": \"\
    causal_graphs[0].nodes[7]\",\n      \"node_id\": \"decreased_membrane_fluidity\"\
    ,\n      \"outcome\": \"supported_at_generic_scope\",\n      \"assessment\": \"\
    Mendoza abstract explicitly discusses sensing decreased fluidity; no detailed\
    \ sensing efficacy is assessed.\"\n    },\n    {\n      \"index\": 8,\n      \"\
    field\": \"causal_graphs[0].nodes[8]\",\n      \"node_id\": \"lipid_desaturase_activity\"\
    ,\n      \"outcome\": \"supported_at_literal_physical_scope\",\n      \"assessment\"\
    : \"Wu body p4 supports existing cis-bond/packing physical wording, not a detailed\
    \ pathogen enzyme intervention.\"\n    },\n    {\n      \"index\": 9,\n      \"\
    field\": \"causal_graphs[0].nodes[9]\",\n      \"node_id\": \"membrane_fluidity\"\
    ,\n      \"outcome\": \"supported_at_generic_scope\",\n      \"assessment\": \"\
    Fluidity is the physical referent in the selected abstract/body spans; formal\
    \ typing assessed separately.\"\n    },\n    {\n      \"index\": 10,\n      \"\
    field\": \"causal_graphs[0].nodes[10]\",\n      \"node_id\": \"membrane_viscosity_high_temperature\"\
    ,\n      \"outcome\": \"supported_at_literal_physical_scope\",\n      \"assessment\"\
    : \"Wu p6 contains the existing trans-UFA/viscosity span; no universal warming\
    \ response asserted by this audit.\"\n    },\n    {\n      \"index\": 11,\n  \
    \    \"field\": \"causal_graphs[0].nodes[11]\",\n      \"node_id\": \"increased_fatty_acid_diversity\"\
    ,\n      \"outcome\": \"qualified\",\n      \"assessment\": \"Wu p5 supports context-dependent\
    \ acyl composition changes; no universal rule that every branching/chain change\
    \ increases fluidity is inferred.\"\n    },\n    {\n      \"index\": 12,\n   \
    \   \"field\": \"causal_graphs[0].nodes[12]\",\n      \"node_id\": \"thermostable_enzyme\"\
    ,\n      \"outcome\": \"supported_at_generic_scope\",\n      \"assessment\": \"\
    Vieille abstract explicitly supplies hyperthermophilic enzyme thermostability\
    \ context.\"\n    },\n    {\n      \"index\": 13,\n      \"field\": \"causal_graphs[0].nodes[13]\"\
    ,\n      \"node_id\": \"irreversible_protein_inactivation\",\n      \"outcome\"\
    : \"supported_at_generic_scope\",\n      \"assessment\": \"Irreversible inactivation\
    \ is the outcome named in the source abstract; prevention efficacy is not expanded.\"\
    \n    }\n  ]\n}"
- assessment_id: relations
  area: consistency
  topic: 'Native checklist: all 13 current relations'
  outcome: concern
  target_ids:
  - METPO:1000487
  summary: Edges3/4/5/6/7/8 form one imported-role group. Edge2 may denote a temperature-decrease
    event; Biolink associations retain broad endpoints. Edge7 negatively targets inactivation,
    so no reversed-positive-integrity finding.
  evidence_ids:
  - nodes-edges
  - ro-primary
  - local-authority
  - adjudication
  details: "{\n  \"grounding\": [\n    {\n      \"index\": 0,\n      \"subject\":\
    \ \"maximal_thermal_adaptation\",\n      \"predicate\": \"confers\",\n      \"\
    predicate_id\": \"METPO:2007700\",\n      \"object\": \"temperature_delta_high_trait\"\
    ,\n      \"outcome\": \"supported\",\n      \"assessment\": \"Local v8 confers\
    \ broad causal-node roles and maintained trait-object gate fit; capacity/process\
    \ nuance does not establish formal violation.\",\n      \"biological_support\"\
    : \"UNASSESSED_SCOPE for detailed survival/fitness or intervention mechanisms\"\
    \n    },\n    {\n      \"index\": 1,\n      \"subject\": \"temperature_delta_high_trait\"\
    ,\n      \"predicate\": \"is a\",\n      \"predicate_id\": \"rdfs:subClassOf\"\
    ,\n      \"object\": \"temperature_delta\",\n      \"outcome\": \"supported\"\
    ,\n      \"assessment\": \"rdfs subclass edge agrees with exact imported1000487→1000303\
    \ hierarchy.\",\n      \"biological_support\": \"UNASSESSED_SCOPE for detailed\
    \ survival/fitness or intervention mechanisms\"\n    },\n    {\n      \"index\"\
    : 2,\n      \"subject\": \"decreased_growth_temperature\",\n      \"predicate\"\
    : \"increases\",\n      \"predicate_id\": \"RO:0002213\",\n      \"object\": \"\
    unsaturated_fatty_acid_biosynthesis\",\n      \"outcome\": \"supported\",\n  \
    \    \"assessment\": \"Temperature-decrease event to biosynthetic process is a\
    \ defensible processual reading. No enum-only ENVIRONMENTAL_FACTOR exclusion.\
    \ Detailed causal biology is unassessed.\",\n      \"biological_support\": \"\
    UNASSESSED_SCOPE for detailed survival/fitness or intervention mechanisms\"\n\
    \    },\n    {\n      \"index\": 3,\n      \"subject\": \"homoviscous_adaptation\"\
    ,\n      \"predicate\": \"contributes to\",\n      \"predicate_id\": \"RO:0002326\"\
    ,\n      \"object\": \"membrane_fluidity_homeostasis\",\n      \"outcome\": \"\
    concern\",\n      \"assessment\": \"RO2326 inherits material→process via2216/2500/2595;\
    \ explicit homoviscous process subject is nonmaterial, object process valid.\"\
    ,\n      \"biological_support\": \"UNASSESSED_SCOPE for detailed survival/fitness\
    \ or intervention mechanisms\"\n    },\n    {\n      \"index\": 4,\n      \"subject\"\
    : \"decreased_membrane_fluidity\",\n      \"predicate\": \"positively regulates\"\
    ,\n      \"predicate_id\": \"RO:0002213\",\n      \"object\": \"unsaturated_fatty_acid_biosynthesis\"\
    ,\n      \"outcome\": \"concern\",\n      \"assessment\": \"RO2213 inherits process→process\
    \ via2211; actual low-fluidity STATE is not a process, despite nearby sensing\
    \ prose.\",\n      \"biological_support\": \"UNASSESSED_SCOPE for detailed survival/fitness\
    \ or intervention mechanisms\"\n    },\n    {\n      \"index\": 5,\n      \"subject\"\
    : \"lipid_desaturase_activity\",\n      \"predicate\": \"increases\",\n      \"\
    predicate_id\": \"RO:0002213\",\n      \"object\": \"membrane_fluidity\",\n  \
    \    \"outcome\": \"concern\",\n      \"assessment\": \"RO2213 process range conflicts\
    \ with fluidity QUALITY object. Molecular-function activity subject is not independently\
    \ excluded.\",\n      \"biological_support\": \"UNASSESSED_SCOPE for detailed\
    \ survival/fitness or intervention mechanisms\"\n    },\n    {\n      \"index\"\
    : 6,\n      \"subject\": \"increased_fatty_acid_diversity\",\n      \"predicate\"\
    : \"increases\",\n      \"predicate_id\": \"RO:0002213\",\n      \"object\": \"\
    membrane_fluidity\",\n      \"outcome\": \"concern\",\n      \"assessment\": \"\
    RO2213 process endpoints conflict with current CHEMICAL subject and QUALITY object;\
    \ even an event reading of composition shift leaves quality object conflict.\"\
    ,\n      \"biological_support\": \"UNASSESSED_SCOPE for detailed survival/fitness\
    \ or intervention mechanisms\"\n    },\n    {\n      \"index\": 7,\n      \"subject\"\
    : \"thermostable_enzyme\",\n      \"predicate\": \"prevents\",\n      \"predicate_id\"\
    : \"RO:0002212\",\n      \"object\": \"irreversible_protein_inactivation\",\n\
    \      \"outcome\": \"concern\",\n      \"assessment\": \"RO2212 inherits process→process;\
    \ actual thermostability QUALITY subject is not a process. Object inactivation\
    \ is process; negative polarity is coherent and not separately reversed.\",\n\
    \      \"biological_support\": \"UNASSESSED_SCOPE for detailed survival/fitness\
    \ or intervention mechanisms\"\n    },\n    {\n      \"index\": 8,\n      \"subject\"\
    : \"unsaturated_fatty_acid_biosynthesis\",\n      \"predicate\": \"contributes\
    \ to\",\n      \"predicate_id\": \"RO:0002326\",\n      \"object\": \"homoviscous_adaptation\"\
    ,\n      \"outcome\": \"concern\",\n      \"assessment\": \"RO2326 material domain\
    \ conflicts with explicit biosynthetic PROCESS subject; object homoviscous process\
    \ is compatible.\",\n      \"biological_support\": \"UNASSESSED_SCOPE for detailed\
    \ survival/fitness or intervention mechanisms\"\n    },\n    {\n      \"index\"\
    : 9,\n      \"subject\": \"membrane_fluidity\",\n      \"predicate\": \"associated\
    \ with\",\n      \"predicate_id\": \"biolink:associated_with\",\n      \"object\"\
    : \"membrane_fluidity_homeostasis\",\n      \"outcome\": \"supported\",\n    \
    \  \"assessment\": \"Biolink associated-with broad named-thing endpoints admit\
    \ quality/process. Evidence scope remains separate.\",\n      \"biological_support\"\
    : \"UNASSESSED_SCOPE for detailed survival/fitness or intervention mechanisms\"\
    \n    },\n    {\n      \"index\": 10,\n      \"subject\": \"membrane_viscosity_high_temperature\"\
    ,\n      \"predicate\": \"associated with\",\n      \"predicate_id\": \"biolink:associated_with\"\
    ,\n      \"object\": \"membrane_fluidity_homeostasis\",\n      \"outcome\": \"\
    supported\",\n      \"assessment\": \"Biolink associated-with broad named-thing\
    \ endpoints admit quality/process; no imported RO constraint inferred.\",\n  \
    \    \"biological_support\": \"UNASSESSED_SCOPE for detailed survival/fitness\
    \ or intervention mechanisms\"\n    },\n    {\n      \"index\": 11,\n      \"\
    subject\": \"membrane_fluidity_homeostasis\",\n      \"predicate\": \"associated\
    \ with\",\n      \"predicate_id\": \"biolink:associated_with\",\n      \"object\"\
    : \"maximal_thermal_adaptation\",\n      \"outcome\": \"supported\",\n      \"\
    assessment\": \"Biolink associated-with broad named-thing endpoints admit process/process\
    \ or capacity shorthand; no formal mismatch.\",\n      \"biological_support\"\
    : \"UNASSESSED_SCOPE for detailed survival/fitness or intervention mechanisms\"\
    \n    },\n    {\n      \"index\": 12,\n      \"subject\": \"thermostable_enzyme\"\
    ,\n      \"predicate\": \"associated with\",\n      \"predicate_id\": \"biolink:associated_with\"\
    ,\n      \"object\": \"maximal_thermal_adaptation\",\n      \"outcome\": \"supported\"\
    ,\n      \"assessment\": \"Biolink associated-with broad named-thing endpoints\
    \ admit quality/process or capacity shorthand; no formal mismatch.\",\n      \"\
    biological_support\": \"UNASSESSED_SCOPE for detailed survival/fitness or intervention\
    \ mechanisms\"\n    }\n  ],\n  \"source\": [\n    {\n      \"index\": 0,\n   \
    \   \"field\": \"causal_graphs[0].edges[0]\",\n      \"subject\": \"maximal_thermal_adaptation\"\
    ,\n      \"object\": \"temperature_delta_high_trait\",\n      \"outcome\": \"\
    unknown\",\n      \"assessment\": \"UNKNOWN: inspected source supports generic\
    \ membrane or protein context, but the exact >30 °C growth-breadth calibration\
    \ or joint adaptation bridge is not established by that inspected text. Full Mendoza/Vieille\
    \ bodies were unavailable in this audit; this is not a paper-wide absence or biological\
    \ refutation.\",\n      \"source_placement\": \"causal_graphs[0].edges[0].evidence[0]\"\
    ,\n      \"predicate_formal_role\": \"Separate grounding audit; source match does\
    \ not validate imported relation domain/range.\"\n    },\n    {\n      \"index\"\
    : 1,\n      \"field\": \"causal_graphs[0].edges[1]\",\n      \"subject\": \"temperature_delta_high_trait\"\
    ,\n      \"object\": \"temperature_delta\",\n      \"outcome\": \"unknown\",\n\
    \      \"assessment\": \"UNKNOWN: inspected source supports generic membrane or\
    \ protein context, but the exact >30 °C growth-breadth calibration or joint adaptation\
    \ bridge is not established by that inspected text. Full Mendoza/Vieille bodies\
    \ were unavailable in this audit; this is not a paper-wide absence or biological\
    \ refutation.\",\n      \"source_placement\": \"causal_graphs[0].edges[1].evidence[0]\"\
    ,\n      \"predicate_formal_role\": \"Separate grounding audit; source match does\
    \ not validate imported relation domain/range.\"\n    },\n    {\n      \"index\"\
    : 2,\n      \"field\": \"causal_graphs[0].edges[2]\",\n      \"subject\": \"decreased_growth_temperature\"\
    ,\n      \"object\": \"unsaturated_fatty_acid_biosynthesis\",\n      \"outcome\"\
    : \"supported_at_bounded_scope\",\n      \"assessment\": \"Supplied span and generic\
    \ physical/classification context supported. Detailed taxon-specific signaling,\
    \ fitness, defense, AMR and intervention efficacy are UNASSESSED_SCOPE; a literal\
    \ match is not complete mechanism validation.\",\n      \"source_placement\":\
    \ \"causal_graphs[0].edges[2].evidence[0]\",\n      \"predicate_formal_role\"\
    : \"Separate grounding audit; source match does not validate imported relation\
    \ domain/range.\"\n    },\n    {\n      \"index\": 3,\n      \"field\": \"causal_graphs[0].edges[3]\"\
    ,\n      \"subject\": \"homoviscous_adaptation\",\n      \"object\": \"membrane_fluidity_homeostasis\"\
    ,\n      \"outcome\": \"supported_at_bounded_scope\",\n      \"assessment\": \"\
    Supplied span and generic physical/classification context supported. Detailed\
    \ taxon-specific signaling, fitness, defense, AMR and intervention efficacy are\
    \ UNASSESSED_SCOPE; a literal match is not complete mechanism validation.\",\n\
    \      \"source_placement\": \"causal_graphs[0].edges[3].evidence[0]\",\n    \
    \  \"predicate_formal_role\": \"Separate grounding audit; source match does not\
    \ validate imported relation domain/range.\"\n    },\n    {\n      \"index\":\
    \ 4,\n      \"field\": \"causal_graphs[0].edges[4]\",\n      \"subject\": \"decreased_membrane_fluidity\"\
    ,\n      \"object\": \"unsaturated_fatty_acid_biosynthesis\",\n      \"outcome\"\
    : \"supported_at_bounded_scope\",\n      \"assessment\": \"Supplied span and generic\
    \ physical/classification context supported. Detailed taxon-specific signaling,\
    \ fitness, defense, AMR and intervention efficacy are UNASSESSED_SCOPE; a literal\
    \ match is not complete mechanism validation.\",\n      \"source_placement\":\
    \ \"causal_graphs[0].edges[4].evidence[0]\",\n      \"predicate_formal_role\"\
    : \"Separate grounding audit; source match does not validate imported relation\
    \ domain/range.\"\n    },\n    {\n      \"index\": 5,\n      \"field\": \"causal_graphs[0].edges[5]\"\
    ,\n      \"subject\": \"lipid_desaturase_activity\",\n      \"object\": \"membrane_fluidity\"\
    ,\n      \"outcome\": \"supported_at_bounded_scope\",\n      \"assessment\": \"\
    Supplied span and generic physical/classification context supported. Detailed\
    \ taxon-specific signaling, fitness, defense, AMR and intervention efficacy are\
    \ UNASSESSED_SCOPE; a literal match is not complete mechanism validation.\",\n\
    \      \"source_placement\": \"causal_graphs[0].edges[5].evidence[0]\",\n    \
    \  \"predicate_formal_role\": \"Separate grounding audit; source match does not\
    \ validate imported relation domain/range.\"\n    },\n    {\n      \"index\":\
    \ 6,\n      \"field\": \"causal_graphs[0].edges[6]\",\n      \"subject\": \"increased_fatty_acid_diversity\"\
    ,\n      \"object\": \"membrane_fluidity\",\n      \"outcome\": \"supported_at_bounded_scope\"\
    ,\n      \"assessment\": \"Supplied span and generic physical/classification context\
    \ supported. Detailed taxon-specific signaling, fitness, defense, AMR and intervention\
    \ efficacy are UNASSESSED_SCOPE; a literal match is not complete mechanism validation.\"\
    ,\n      \"source_placement\": \"causal_graphs[0].edges[6].evidence[0]\",\n  \
    \    \"predicate_formal_role\": \"Separate grounding audit; source match does\
    \ not validate imported relation domain/range.\"\n    },\n    {\n      \"index\"\
    : 7,\n      \"field\": \"causal_graphs[0].edges[7]\",\n      \"subject\": \"thermostable_enzyme\"\
    ,\n      \"object\": \"irreversible_protein_inactivation\",\n      \"outcome\"\
    : \"qualified\",\n      \"assessment\": \"Enzyme thermostability and literal resistance-to-inactivation\
    \ phrase are supported; extending whole-organism upper growth limits is an inference,\
    \ not directly measured by this inspected abstract. No new finding solely from\
    \ the inaccessible body.\",\n      \"source_placement\": \"causal_graphs[0].edges[7].evidence[0]\"\
    ,\n      \"predicate_formal_role\": \"Separate grounding audit; source match does\
    \ not validate imported relation domain/range.\"\n    },\n    {\n      \"index\"\
    : 8,\n      \"field\": \"causal_graphs[0].edges[8]\",\n      \"subject\": \"unsaturated_fatty_acid_biosynthesis\"\
    ,\n      \"object\": \"homoviscous_adaptation\",\n      \"outcome\": \"concern\"\
    ,\n      \"assessment\": \"Generic adaptation component is supported; supplied\
    \ homeoviscous phrase is not verbatim in the specifically claimed abstract, which\
    \ spells homoviscous in both original indexed bytes and current publisher export.\
    \ No biological falsehood or unseen-body claim.\",\n      \"source_placement\"\
    : \"causal_graphs[0].edges[8].evidence[0]\",\n      \"predicate_formal_role\"\
    : \"Separate grounding audit; source match does not validate imported relation\
    \ domain/range.\"\n    },\n    {\n      \"index\": 9,\n      \"field\": \"causal_graphs[0].edges[9]\"\
    ,\n      \"subject\": \"membrane_fluidity\",\n      \"object\": \"membrane_fluidity_homeostasis\"\
    ,\n      \"outcome\": \"supported_at_bounded_scope\",\n      \"assessment\": \"\
    Supplied span and generic physical/classification context supported. Detailed\
    \ taxon-specific signaling, fitness, defense, AMR and intervention efficacy are\
    \ UNASSESSED_SCOPE; a literal match is not complete mechanism validation.\",\n\
    \      \"source_placement\": \"causal_graphs[0].edges[9].evidence[0]\",\n    \
    \  \"predicate_formal_role\": \"Separate grounding audit; source match does not\
    \ validate imported relation domain/range.\"\n    },\n    {\n      \"index\":\
    \ 10,\n      \"field\": \"causal_graphs[0].edges[10]\",\n      \"subject\": \"\
    membrane_viscosity_high_temperature\",\n      \"object\": \"membrane_fluidity_homeostasis\"\
    ,\n      \"outcome\": \"supported_at_bounded_scope\",\n      \"assessment\": \"\
    Supplied span and generic physical/classification context supported. Detailed\
    \ taxon-specific signaling, fitness, defense, AMR and intervention efficacy are\
    \ UNASSESSED_SCOPE; a literal match is not complete mechanism validation.\",\n\
    \      \"source_placement\": \"causal_graphs[0].edges[10].evidence[0]\",\n   \
    \   \"predicate_formal_role\": \"Separate grounding audit; source match does not\
    \ validate imported relation domain/range.\"\n    },\n    {\n      \"index\":\
    \ 11,\n      \"field\": \"causal_graphs[0].edges[11]\",\n      \"subject\": \"\
    membrane_fluidity_homeostasis\",\n      \"object\": \"maximal_thermal_adaptation\"\
    ,\n      \"outcome\": \"supported_at_bounded_scope\",\n      \"assessment\": \"\
    Supplied span and generic physical/classification context supported. Detailed\
    \ taxon-specific signaling, fitness, defense, AMR and intervention efficacy are\
    \ UNASSESSED_SCOPE; a literal match is not complete mechanism validation.\",\n\
    \      \"source_placement\": \"causal_graphs[0].edges[11].evidence[0]\",\n   \
    \   \"predicate_formal_role\": \"Separate grounding audit; source match does not\
    \ validate imported relation domain/range.\"\n    },\n    {\n      \"index\":\
    \ 12,\n      \"field\": \"causal_graphs[0].edges[12]\",\n      \"subject\": \"\
    thermostable_enzyme\",\n      \"object\": \"maximal_thermal_adaptation\",\n  \
    \    \"outcome\": \"supported_at_bounded_scope\",\n      \"assessment\": \"Supplied\
    \ span and generic physical/classification context supported. Detailed taxon-specific\
    \ signaling, fitness, defense, AMR and intervention efficacy are UNASSESSED_SCOPE;\
    \ a literal match is not complete mechanism validation.\",\n      \"source_placement\"\
    : \"causal_graphs[0].edges[12].evidence[0]\",\n      \"predicate_formal_role\"\
    : \"Separate grounding audit; source match does not validate imported relation\
    \ domain/range.\"\n    }\n  ]\n}"
- assessment_id: scope-completeness
  area: scope
  topic: 'Native checklist: quantitative NONMECHANISTIC graph'
  outcome: supported
  target_ids:
  - METPO:1000487
  summary: One component and zero protein classes/instances are appropriate to a numerical-bin
    overview; no fabricated connector or protein requirement.
  evidence_ids:
  - record
  - policy
  - expression
- assessment_id: biology-limits
  area: scope
  topic: 'Native checklist: bounded biological reading'
  outcome: unknown
  target_ids:
  - METPO:1000487
  summary: Generic environmental classification, supplied quotation and formal representations
    only. Detailed pathogen survival/fitness/ROS/AMR/intervention efficacy remains
    UNASSESSED_SCOPE; literal matches do not verify every causal bridge.
  evidence_ids:
  - source-reading
  - source-nodes-edges
  - ground-reading
- assessment_id: expression
  area: evidence
  topic: 'Native checklist: canonical and source catalog applicability'
  outcome: unknown
  target_ids:
  - METPO:1000487
  summary: Retained 20-organism / 28-dataset catalog lacks exact canonical coverage.
    B. subtilis, E. coli and P. putida source/context species have coverage, but no
    strain-level or module-to46 °C phenotype inference or detailed module query was
    made.
  evidence_ids:
  - expression
  - catalog-reuse
  - taxonomy
- assessment_id: ownership
  area: ownership
  topic: 'Native checklist: current writer recurrence'
  outcome: supported
  target_ids:
  - METPO:1000487
  summary: Generic grounder skips populated IDs. Dedicated review/connector have exact-state
    guards; repair dispatcher replaces selected existing keys using connector constants
    subject to complete-key prerequisites. Sibling label normalizers are context;
    no current canonical writer claim.
  evidence_ids:
  - owners
  - owner-primary
  - writer-state
  - predicate-mapping
- assessment_id: history-scope
  area: provenance
  topic: 'Native checklist: actual whole reads and reuse'
  outcome: supported
  target_ids:
  - METPO:1000487
  summary: 'Thirteen current actor/target/event projections: four current whole-file
    reads and nine prior complete reads qualified by unchanged hashes. Three exact-target
    histories are AI edits; source-specific historical wording is not primary scientific
    authority.'
  evidence_ids:
  - histories
  - ground-reading
  - owners
- assessment_id: human
  area: provenance
  topic: 'Native checklist: attributable current acceptance'
  outcome: concern
  target_ids:
  - METPO:1000487
  summary: 16 AI events plus seed,179 ignored-inclusive paths and 68 actual target
    arrays with zero exact record do not establish attributable current human acceptance.
    Private/remote evidence remains unknown.
  evidence_ids:
  - owners
  - human-search
  - histories
  - playbook
  - challenge
- assessment_id: readiness
  area: consistency
  topic: 'Native checklist: checks and evidence chronology'
  outcome: supported
  target_ids:
  - METPO:1000487
  summary: All 90 inputs and frozen audits match. Native and corrected strict passed;
    wrong-recipe failure is optional/superseded. Common failures/skips, original acquisitions,
    copied/read times and local initialization remain explicit; no fresh B13 QC/publication
    claimed.
  evidence_ids:
  - capture
  - source-checks
  - reuse
  - reuse-postcheck
  - local-init
findings:
- finding_id: imported-process-roles
  issue_key: temperature-delta-high-imported-process-roles
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Imported roles conflict with current node referents
  description: 'Six imported relations conflict with the represented node referents.
    RO:0002326 inherits a material-entity subject, whereas edges 3 and 8 have explicit
    biological-process subjects. RO:0002213 inherits process-to-process roles: edge
    4 starts from a reduced-fluidity state and edges 5 and 6 point to a fluidity quality.
    RO:0002212 also inherits process-to-process roles; edge 7 starts from thermostability
    quality. This is one grouped representation defect, not a biological refutation.
    Edge 2 denotes a temperature-decrease event and is not rejected merely because
    it uses the environmental-factor enum.'
  target_ids:
  - METPO:1000487
  field_paths:
  - causal_graphs[0].edges[3].predicate_id
  - causal_graphs[0].edges[4].predicate_id
  - causal_graphs[0].edges[5].predicate_id
  - causal_graphs[0].edges[6].predicate_id
  - causal_graphs[0].edges[7].predicate_id
  - causal_graphs[0].edges[8].predicate_id
  evidence_ids:
  - nodes-edges
  - ro-primary
  - owners
  - owner-primary
  - challenge
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_delta_high.yaml
    role: Current assertion or documented conditional recurrence; exact replay guards
      remain applicable.
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Current assertion or documented conditional recurrence; exact replay guards
      remain applicable.
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Current assertion or documented conditional recurrence; exact replay guards
      remain applicable.
  - repository: CultureBotAI/TraitMech
    path: scripts/review_temperature_delta_high_graph_183.py
    role: Current assertion or documented conditional recurrence; exact replay guards
      remain applicable.
  - repository: CultureBotAI/TraitMech
    path: scripts/connect_temperature_delta_high_graph_183.py
    role: Current assertion or documented conditional recurrence; exact replay guards
      remain applicable.
  - repository: CultureBotAI/TraitMech
    path: scripts/repair_pr664_adversarial_review.py
    role: Current assertion or documented conditional recurrence; exact replay guards
      remain applicable.
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: quoted-spelling-drift
  issue_key: temperature-delta-high-quoted-spelling-drift
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Copied abstract spelling and verification note disagree
  description: The supplied edge8 snippet says termed homeoviscous adaptation, while
    the currently inspected publisher and indexed abstracts say termed homoviscous
    adaptation. These spellings denote the same concept here, but the exact-quotation
    and abstract-verification claims need correction or an exact source-version locator.
    Historical requotation prose is not primary evidence of the supplied spelling.
  target_ids:
  - METPO:1000487
  field_paths:
  - causal_graphs[0].edges[8].evidence[0].snippet
  - causal_graphs[0].edges[8].evidence[0].notes
  evidence_ids:
  - copy-discrepancy
  - mendoza
  - mendoza-browser
  - writer-state
  - challenge
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_delta_high.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: scripts/connect_temperature_delta_high_graph_183.py
    role: Current edge8 constant and exact-state connector guard.
  - repository: CultureBotAI/TraitMech
    path: scripts/repair_pr664_adversarial_review.py
    role: Loads connector constants and replaces selected matching keys; preserve
      full dispatcher prerequisites.
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: human-acceptance-link
  issue_key: temperature-delta-high-human-acceptance-link
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Reviewed status lacks locally attributable acceptance
  description: 'The current REVIEWED status is not linked to attributable human acceptance
    of the present assertions in the inspected local evidence. The bounded search
    included ignored and hidden files, excluding .git and .venv: 179 matching paths,
    68 actual review target arrays with zero exact current-target arrays, 17 embedded
    events (16 AI plus a seed), and 13 histories with explicit reading provenance.
    Private or remote acceptance remains unknown.'
  target_ids:
  - METPO:1000487
  field_paths:
  - mapping_status
  - curation_history
  evidence_ids:
  - human-search
  - histories
  - owners
  - playbook
  - challenge
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_delta_high.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
actions:
- action_id: resolve-imported-process-roles
  description: Curate the six existing relation assertions against their actual node
    referents, retaining supported biological context. Review direct writer/connector
    constants and conditional mapping recurrence together; do not infer that rerunning
    a table grounder changes populated IDs or resurrect previously removed cis-trans
    assertions.
  finding_ids:
  - imported-process-roles
  target_ids:
  - METPO:1000487
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_delta_high.yaml
    role: Current assertion or documented conditional recurrence; exact replay guards
      remain applicable.
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Current assertion or documented conditional recurrence; exact replay guards
      remain applicable.
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Current assertion or documented conditional recurrence; exact replay guards
      remain applicable.
  - repository: CultureBotAI/TraitMech
    path: scripts/review_temperature_delta_high_graph_183.py
    role: Current assertion or documented conditional recurrence; exact replay guards
      remain applicable.
  - repository: CultureBotAI/TraitMech
    path: scripts/connect_temperature_delta_high_graph_183.py
    role: Current assertion or documented conditional recurrence; exact replay guards
      remain applicable.
  - repository: CultureBotAI/TraitMech
    path: scripts/repair_pr664_adversarial_review.py
    role: Current assertion or documented conditional recurrence; exact replay guards
      remain applicable.
  acceptance_checks:
  - Each affected triple fits the selected relation definition and inherited roles
    with an inspected source at the narrow claim.
  - Preserve the current nonmechanistic scope, endpoint identity, prior removal and
    replay guards.
  - Guarded curation/history plus strict, grounding, snippet, graph and maintained
    QC gates pass.
- action_id: resolve-quoted-spelling-drift
  description: Align edge8 quoted text and its abstract-verification note with the
    exact inspected source version, or provide a verifiable version/locator containing
    the current wording; reconcile connector constants through guarded curation and
    append new history rather than rewriting old history.
  finding_ids:
  - quoted-spelling-drift
  target_ids:
  - METPO:1000487
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_delta_high.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: scripts/connect_temperature_delta_high_graph_183.py
    role: Current edge8 constant and exact-state connector guard.
  - repository: CultureBotAI/TraitMech
    path: scripts/repair_pr664_adversarial_review.py
    role: Loads connector constants and replaces selected matching keys; preserve
      full dispatcher prerequisites.
  acceptance_checks:
  - Literal snippet matches the identified primary source version.
  - Verification note names the actual source scope; historical events remain immutable.
  - Snippet check and strict validation pass, with full-text limitations stated.
- action_id: resolve-human-acceptance-link
  description: Locate and attach an attributable human acceptance of the current assertions,
    or use the established curation process to resolve the status provenance; preserve
    prior actors and history.
  finding_ids:
  - human-acceptance-link
  target_ids:
  - METPO:1000487
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_delta_high.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Acceptance identifies the reviewed assertions/version, responsible curator and
    accessible decision evidence.
  - Status is not promoted solely because this AI review or deterministic checks passed.
limitations:
- Raw METPO existential minInclusive30 and related synonym Td_>30 conflict at exact30.
  Approximate record prose is retained as a boundary qualification, not a separate
  wrong-identity finding.
- Node2 capacity wording and node11 compositional-shift wording warrant referent precision;
  no unsupported standalone node defect or forced CAPACITY reservoir claim.
- The direct >30 calibration and extreme-breadth causal attribution remain UNKNOWN
  beyond inspected generic abstracts; inaccessible bodies are not negative evidence.
- Detailed pathogen defense/fitness/intervention mechanisms are outside this generic
  physiological review.
- Literal matches alone do not verify adjacent scope or causal inference.
- 'UNKNOWN: inspected source supports generic membrane or protein context, but the
  exact >30 °C growth-breadth calibration or joint adaptation bridge is not established
  by that inspected text. Full Mendoza/Vieille bodies were unavailable in this audit;
  this is not a paper-wide absence or biological refutation.'
- Edge0/edge1 direct breadth attribution is stronger than inspected generic abstract
  support; retain unknown rather than claiming unseen full-source absence or inventing
  another finding.
- Node/edge physical context and supplied spans are assessed at generic non-operational
  scope; detailed mechanism sufficiency and efficacy remain unassessed.
- Canonical historical superlative is not an independently current ranking.
- Formal role and node-typing findings are owned by the separate grounding audit.
- Full source acquisition is distinct from selected reading; current browser export
  is not raw publisher HTML.
- Original Mendoza and Vieille metadata acquisition times, current copy times, publisher
  HTTP403 and Vieille HTTP500 are preserved.
- Grounding history coverage comprises four current whole rereads and nine qualified
  unchanged prior whole reads; root independently read three exact-target histories
  and all thirteen projections.
- 'Canonical catalog absence does not imply source-organism absence: retained catalog
  covers contextual B. subtilis, E. coli and P. putida at species level; no exact
  strain/module breadth support is claimed.'
- The initial wrong strict recipe failed before validation; corrected maintained validate-strict
  passed. This was not a completed review validation failure.
- Qualified historical common diagnostics preserve original failures/retries/skips;
  no fresh B13 corpus QC or remote publication is claimed.
- Publisher browser evidence is retained tool output; actual origin/cache-fetch time
  is not independently known. HTTP403/500 bytes and initial taxonomy DNS error are
  access diagnostics, not primary bodies.
- Original metadata acquisitions, current copies and current selected readings have
  separate timestamps. Qualified common diagnostics retain original failures/skips;
  no fresh B13 QC or remote publication is asserted.
notes:
- Whole 394-line target,90 captured inputs, four works / 17 placements / 18 grounding
  fields, 14 nodes and 13 edges, 15 snippets and one canonical example reviewed.
- History coverage is four current whole reads plus nine prior unchanged whole reads;
  all 13 projections are current. The graph has 17 events (16 AI plus a seed), one
  component and zero protein classes or instances.
- Preparation imports/executes no serializer/helper and changes no scientific record,
  Git or state. Root owns eventual single serialization.
tags:
- record-review
- temperature-delta-high
- environment
- needs-curation
```
