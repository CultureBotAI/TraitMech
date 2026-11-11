# Whole-record review of temperature optimum high

- Review: 20261022T004826Z-temperature-optimum-high
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-22T00:38:05.328146Z
- Finished UTC: 2026-10-22T00:48:26Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Temperature optimum high needs one grouped representation repair for five imported-role edges and the coupled thermostability facet, plus a link to attributable human acceptance. Active identity, canonical reported optimum and all sixteen literal snippets are supported; exact category calibration and sufficient organism-optimum claims remain unknown.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: Ninth record of the actual local batch 013 queue. Whole 457-line target and 85 captured inputs verified; local review does not assert remote publication.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8eee04a8c65609fbaff6df7c54597dcaf1b9d282.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| METPO:1000447 | data/traits/environment/temperature_optimum_high.yaml | maintained | temperature optimum high |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full-corpus graph audit | passed | True | METPO:1000447 | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| Full-corpus snippet audit | passed | True | METPO:1000447 | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| Full-corpus pathway links | passed | True | METPO:1000447 | 19 links checked against the pinned PathwayMech snapshot. |
| Full-corpus history integrity | passed | True | METPO:1000447 | 1277 history records checked, zero invalid links at the 8eee source base; integrity does not establish science or human acceptance. |
| Initial full-product validation | failed | False | METPO:1000447 | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation with isolated local cache | failed | False | METPO:1000447 | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation after isolated-cache download | passed | True | METPO:1000447 | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| Focused native validation | passed | True | METPO:1000447 | Native record validation passed; scientific interpretation is assessed separately. |
| Focused strict validation | passed | True | METPO:1000447 | Actual validate-strict command passed. |
| Focused network snippet check | passed | True | METPO:1000447 | Six of sixteen schema snippets were VERIFIED; ten were NOT_IN_ABSTRACT in the native abstract check. Separate manual inspection verifies all sixteen literal spans. Native inconclusive results are not body-absence evidence. |
| Qualified batch-twelve QC | passed | True | METPO:1000447 | Actual prior QC qualified against B13 bytes; this is not a new B13 QC execution or publication. |
| Protein-instance metadata applicability | not_applicable | False | METPO:1000447 | Four contextual protein classes, three reviewed label-only classes and zero instances. Legacy GO molecular-function grounding is permitted; no mandatory accession or instance follows from this quantitative NONMECHANISTIC overview. |
| Structured source-organism expression query availability | unavailable | False | METPO:1000447 | Generic queries for covered benign S.acidocaldarius were appropriate but not executed because current bounded discovery found the adapter unavailable. Retained catalog and selected assigned primary context are fallback; no module membership result or canonical species transfer. |

## Scientific And Domain Assessments

### Native checklist: active identity and hierarchy

identity: supported. Targets: METPO:1000447.

Active METPO1000447 and direct parent1000304 match the high optimum concept. Raw inclusive40 restriction and approximate above40/related synonym are an explicit endpoint qualification, not a second confirmed defect.

### Native checklist: threshold and sufficient optimum claims

quantity: unknown. Targets: METPO:1000447.

Inspected Tolner/Vieille abstracts support generic adaptation and enzyme thermostability. Exact approximate40 calibration, exact Thermophile equivalence and sufficient thermostability-to-organism-optimum claims remain unknown; inaccessible body content is not refuted.

### Native checklist: reported optimum

quantity: supported. Targets: METPO:1000447.

S.islandicus REY15A is explicitly reported at an optimal-control temperature of76 degrees C, separate from the66-degree comparator. This supports the current bin under stated study conditions without asserting a complete response curve. Official species identity is checked separately.

### Native checklist: six works and eighteen placements

evidence: unknown. Targets: METPO:1000447.

Generic environmental archaeal attribution and all source identities are positive. Physiological debate, in-vitro DNA observations and correlations remain qualified; heat-shock response context and hyperthermophile introductions do not establish every organism optimum. Detailed dangerous-pathogen mechanisms and intervention efficacy remain UNASSESSED_SCOPE.

### Native checklist: all snippets and notes

evidence: supported. Targets: METPO:1000447.

All sixteen schema snippets are literal. The native abstract check verified six and left ten inconclusive; selected body inspection resolves literal occurrence without validating every note or causal interpretation. No inherited quoted-note finding is added.

### Native checklist: all sixteen referents

representation: concern. Targets: METPO:1000447.

Node3 thermostability/material-property wording conflicts with its process facet, grouped with edge9. Reverse gyrase has allowed GO molecular-function grounding. Node5 process/state, node14 quality/stabilization and node15 enrichment nuances remain qualifications; no forced additional retype.

{
  "grounding": [
    {
      "index": 0,
      "node_id": "temperature_optimum_high_trait",
      "label": "temperature optimum high",
      "node_type": "TRAIT",
      "grounding": "METPO:1000447",
      "outcome": "supported",
      "assessment": "Active high-bin identity; exact inclusive40 versus approximate above40 is a bounded endpoint qualification."
    },
    {
      "index": 1,
      "node_id": "temperature_optimum",
      "label": "temperature optimum",
      "node_type": "TRAIT",
      "grounding": "METPO:1000304",
      "outcome": "supported",
      "assessment": "Active parent temperature-optimum trait."
    },
    {
      "index": 2,
      "node_id": "hot_environment",
      "label": "hot environment",
      "node_type": "ENVIRONMENTAL_FACTOR",
      "grounding": null,
      "outcome": "supported",
      "assessment": "Ambient hot habitat condition; not assumed to be a process or change event solely from ENVIRONMENTAL_FACTOR."
    },
    {
      "index": 3,
      "node_id": "thermophile_thermostability",
      "label": "thermophile protein thermostability",
      "node_type": "BIOLOGICAL_PROCESS",
      "grounding": null,
      "outcome": "concern",
      "assessment": "Label denotes protein thermostability and description denotes heat-stable lipids/proteins, not an activity. BIOLOGICAL_PROCESS facet conflicts with actual referent; coupled to edge9 role group, no separately counted facet finding or automatic replacement type."
    },
    {
      "index": 4,
      "node_id": "reverse_gyrase",
      "label": "reverse gyrase",
      "node_type": "GENE_OR_PROTEIN",
      "grounding": "GO:0160097",
      "outcome": "supported",
      "assessment": "Protein-class referent grounded through allowed GO molecular-function facet. GO0160097 is reverse gyrase activity, not BP."
    },
    {
      "index": 5,
      "node_id": "dna_positive_supercoiling",
      "label": "DNA positive supercoiling",
      "node_type": "BIOLOGICAL_PROCESS",
      "grounding": null,
      "outcome": "unknown",
      "assessment": "Label and process-quality writer intend introduction of positive supercoils; description calls it a topological state. Process-versus-state wording remains qualified, without forced extra finding."
    },
    {
      "index": 6,
      "node_id": "dna_melting_high_temperature",
      "label": "DNA melting at high temperature",
      "node_type": "BIOLOGICAL_PROCESS",
      "grounding": null,
      "outcome": "supported",
      "assessment": "Explicit DNA strand-separation/denaturation process."
    },
    {
      "index": 7,
      "node_id": "nucleoid_associated_proteins",
      "label": "nucleoid-associated proteins",
      "node_type": "GENE_OR_PROTEIN",
      "grounding": null,
      "outcome": "supported",
      "assessment": "Explicit material protein group; REVIEWED_LABEL_ONLY is allowed for this aggregate."
    },
    {
      "index": 8,
      "node_id": "genome_thermostability",
      "label": "genome thermostability",
      "node_type": "QUALITY",
      "grounding": null,
      "outcome": "supported",
      "assessment": "Explicit resistance-to-denaturation quality."
    },
    {
      "index": 9,
      "node_id": "small_heat_shock_proteins",
      "label": "small heat shock proteins",
      "node_type": "GENE_OR_PROTEIN",
      "grounding": null,
      "outcome": "supported",
      "assessment": "Explicit material chaperone group; reviewed label-only is not an automatic coverage defect."
    },
    {
      "index": 10,
      "node_id": "protein_aggregation_heat",
      "label": "heat-induced protein aggregation",
      "node_type": "BIOLOGICAL_PROCESS",
      "grounding": null,
      "outcome": "supported",
      "assessment": "Explicit aggregation process."
    },
    {
      "index": 11,
      "node_id": "thermosome",
      "label": "thermosome (group II chaperonin)",
      "node_type": "GENE_OR_PROTEIN",
      "grounding": null,
      "outcome": "supported",
      "assessment": "Material group-II complex; aggregate label-only is bounded and material executor is meaningful."
    },
    {
      "index": 12,
      "node_id": "denatured_protein_refolding",
      "label": "refolding of denatured proteins",
      "node_type": "BIOLOGICAL_PROCESS",
      "grounding": null,
      "outcome": "supported",
      "assessment": "Explicit refolding process."
    },
    {
      "index": 13,
      "node_id": "membrane_lipid_composition",
      "label": "altered membrane lipid composition",
      "node_type": "BIOLOGICAL_PROCESS",
      "grounding": null,
      "outcome": "supported",
      "assessment": "Despite composition label, description explicitly denotes lipid-remodeling process; do not force a material type from label alone."
    },
    {
      "index": 14,
      "node_id": "membrane_thermostability",
      "label": "cytoplasmic membrane thermostability",
      "node_type": "QUALITY",
      "grounding": null,
      "outcome": "unknown",
      "assessment": "Label/type denote membrane thermostability quality while description uses stabilization language. Retain nuance; edge8 process subject independently conflicts with material domain."
    },
    {
      "index": 15,
      "node_id": "aa_composition_thermostability",
      "label": "hydrophobic and charged amino acid enrichment",
      "node_type": "BIOLOGICAL_PROCESS",
      "grounding": null,
      "outcome": "unknown",
      "assessment": "Enrichment can mean compositional change or resulting composition; no forced extra facet finding. Edge9 property object is independently decisive."
    }
  ],
  "source": [
    {
      "index": 0,
      "node_id": "temperature_optimum_high_trait",
      "node_type": "TRAIT",
      "outcome": "UNKNOWN_NUMERIC_CALIBRATION",
      "assessment": "Current &gt;~40°C bin is explicit local scope; exact literature threshold/qualitative Thermophile equivalence is unverified from selected Tolner abstract."
    },
    {
      "index": 1,
      "node_id": "temperature_optimum",
      "node_type": "TRAIT",
      "outcome": "SUPPORTED_MEASUREMENT_CONCEPT",
      "assessment": "Optimum is a growth-temperature measurement; do not substitute stress exposure, range, survival or enzyme activity optimum."
    },
    {
      "index": 2,
      "node_id": "hot_environment",
      "node_type": "ENVIRONMENTAL_FACTOR",
      "outcome": "SUPPORTED_GENERIC_CONTEXT",
      "assessment": "High-temperature environments are generic context; exposure above40°C does not alone prove an optimum above40°C."
    },
    {
      "index": 3,
      "node_id": "thermophile_thermostability",
      "node_type": "BIOLOGICAL_PROCESS",
      "outcome": "SUPPORTED_CONTEXT_FACET_QUALIFIED",
      "assessment": "Sources support stability of proteins/lipids. Description mixes material capacity/property with declared process facet; formal review owns that distinction."
    },
    {
      "index": 4,
      "node_id": "reverse_gyrase",
      "node_type": "GENE_OR_PROTEIN",
      "outcome": "SUPPORTED_SOURCE_ATTRIBUTION",
      "assessment": "Reverse gyrase and its supplied topological activity description are source-backed; no new protein instance or universal optimum inference."
    },
    {
      "index": 5,
      "node_id": "dna_positive_supercoiling",
      "node_type": "BIOLOGICAL_PROCESS",
      "outcome": "SUPPORTED_ACTIVITY_CONTEXT",
      "assessment": "Positive-supercoiling activity is discussed; topological state and physiological effect remain distinct and source-qualified."
    },
    {
      "index": 6,
      "node_id": "dna_melting_high_temperature",
      "node_type": "BIOLOGICAL_PROCESS",
      "outcome": "SUPPORTED_PHYSICAL_CONTEXT",
      "assessment": "Thermal DNA strand separation is generic physical context; no intervention protocol reconstructed."
    },
    {
      "index": 7,
      "node_id": "nucleoid_associated_proteins",
      "node_type": "GENE_OR_PROTEIN",
      "outcome": "SUPPORTED_WITH_ASSAY_QUALIFICATION",
      "assessment": "Aggregate NAP source context is in-vitro stabilization plus archaeal correlation, not an exact component or universal causal optimum claim."
    },
    {
      "index": 8,
      "node_id": "genome_thermostability",
      "node_type": "QUALITY",
      "outcome": "SUPPORTED_PHYSICAL_CONTEXT",
      "assessment": "DNA thermostability as resistance to thermal denaturation is relevant; source does not measure a unique genome-wide optimum."
    },
    {
      "index": 9,
      "node_id": "small_heat_shock_proteins",
      "node_type": "GENE_OR_PROTEIN",
      "outcome": "SUPPORTED_ARCHAEAL_CONTEXT",
      "assessment": "Baes introductory small-HSP protein-quality attribution is positive within Sulfolobales context."
    },
    {
      "index": 10,
      "node_id": "protein_aggregation_heat",
      "node_type": "BIOLOGICAL_PROCESS",
      "outcome": "SUPPORTED_ARCHAEAL_CONTEXT",
      "assessment": "Aggregation prevention is part of the supplied introductory context, without operational efficacy assessment."
    },
    {
      "index": 11,
      "node_id": "thermosome",
      "node_type": "GENE_OR_PROTEIN",
      "outcome": "SUPPORTED_ARCHAEAL_CONTEXT",
      "assessment": "Thermosome is described as a group-II chaperonin complex; no forced component-level example."
    },
    {
      "index": 12,
      "node_id": "denatured_protein_refolding",
      "node_type": "BIOLOGICAL_PROCESS",
      "outcome": "SUPPORTED_ARCHAEAL_CONTEXT",
      "assessment": "ATP-dependent refolding attribution is explicit in selected introduction."
    },
    {
      "index": 13,
      "node_id": "membrane_lipid_composition",
      "node_type": "BIOLOGICAL_PROCESS",
      "outcome": "SUPPORTED_RESPONSE_CONTEXT",
      "assessment": "Current description names remodeling process; the selected source describes altered composition in heat-shock response rather than a universal optimum determinant."
    },
    {
      "index": 14,
      "node_id": "membrane_thermostability",
      "node_type": "QUALITY",
      "outcome": "SUPPORTED_CONTEXT_WITH_LIMITS",
      "assessment": "Membrane stabilization is a contextual interpretation of the selected response branch; exact physiological efficacy is not established here."
    },
    {
      "index": 15,
      "node_id": "aa_composition_thermostability",
      "node_type": "BIOLOGICAL_PROCESS",
      "outcome": "SUPPORTED_GENERIC_CONTEXT",
      "assessment": "Enrichment is listed in hyperthermophile introduction; no designed sequence change or improvement is proposed."
    }
  ]
}

### Native checklist: all fourteen relations

consistency: concern. Targets: METPO:1000447.

One imported-role group covers edges3/5/6/8/9 with the coupled node3 facet. Thermosome material executor to refolding process is a positive control. Edge4 process interpretation remains qualified; broad local and Biolink associations receive no invented narrow RO constraints.

{
  "grounding": [
    {
      "index": 0,
      "subject": "hot_environment",
      "predicate": "selects for",
      "predicate_id": "METPO:2007401",
      "object": "thermophile_thermostability",
      "outcome": "unknown",
      "assessment": "Local selects-for broad formal causal-node endpoints do not impose RO process constraints. Environmental condition fits selection context; node3 adapted-material/property shorthand is qualified."
    },
    {
      "index": 1,
      "subject": "thermophile_thermostability",
      "predicate": "confers",
      "predicate_id": "METPO:2007700",
      "object": "temperature_optimum_high_trait",
      "outcome": "supported",
      "assessment": "Local confers broad endpoints admit current generic subject and trait object; no invented imported role."
    },
    {
      "index": 2,
      "subject": "temperature_optimum_high_trait",
      "predicate": "is a",
      "predicate_id": "rdfs:subClassOf",
      "object": "temperature_optimum",
      "outcome": "supported",
      "assessment": "Actual high trait is a subclass of captured temperature-optimum parent."
    },
    {
      "index": 3,
      "subject": "reverse_gyrase",
      "predicate": "positively regulates",
      "predicate_id": "RO:0002213",
      "object": "dna_positive_supercoiling",
      "outcome": "concern",
      "assessment": "RO2213 inherits process domain/range. Current subject is a topoisomerase protein class; legacy MF grounding does not silently retype it into the process needed by this regulatory relation."
    },
    {
      "index": 4,
      "subject": "dna_positive_supercoiling",
      "predicate": "decreases",
      "predicate_id": "RO:0002212",
      "object": "dna_melting_high_temperature",
      "outcome": "unknown",
      "assessment": "Process-intended supercoiling and DNA-denaturation object are formally compatible; topological-state wording remains qualified. Ontology does not establish in-vivo efficacy."
    },
    {
      "index": 5,
      "subject": "nucleoid_associated_proteins",
      "predicate": "increases",
      "predicate_id": "RO:0002213",
      "object": "genome_thermostability",
      "outcome": "concern",
      "assessment": "RO2213 process domain/range conflict with explicit material protein subject and genome-resistance QUALITY object."
    },
    {
      "index": 6,
      "subject": "small_heat_shock_proteins",
      "predicate": "prevents",
      "predicate_id": "RO:0002212",
      "object": "protein_aggregation_heat",
      "outcome": "concern",
      "assessment": "RO2212 inherits process domain; explicit small-HSP protein subject is material. Aggregation object is a process, a positive range control."
    },
    {
      "index": 7,
      "subject": "thermosome",
      "predicate": "enables",
      "predicate_id": "RO:0002327",
      "object": "denatured_protein_refolding",
      "outcome": "supported",
      "assessment": "RO2327 material executor to process fits thermosome/refolding current referents."
    },
    {
      "index": 8,
      "subject": "membrane_lipid_composition",
      "predicate": "contributes to",
      "predicate_id": "RO:0002326",
      "object": "membrane_thermostability",
      "outcome": "concern",
      "assessment": "RO2326 material-to-process inherited roles conflict with explicit lipid-remodeling process subject; membrane-quality object also needs precise referent. Subject mismatch independently decisive."
    },
    {
      "index": 9,
      "subject": "aa_composition_thermostability",
      "predicate": "increases",
      "predicate_id": "RO:0002213",
      "object": "thermophile_thermostability",
      "outcome": "concern",
      "assessment": "RO2213 process range conflicts with explicit protein-thermostability/material-stability object. Node3 process label does not repair its property/material referent. Enrichment process/result ambiguity does not remove object issue."
    },
    {
      "index": 10,
      "subject": "dna_positive_supercoiling",
      "predicate": "associated with",
      "predicate_id": "biolink:associated_with",
      "object": "genome_thermostability",
      "outcome": "supported",
      "assessment": "Biolink associated-with has broad NamedThing roles; no process/material exclusion inferred."
    },
    {
      "index": 11,
      "subject": "genome_thermostability",
      "predicate": "associated with",
      "predicate_id": "biolink:associated_with",
      "object": "thermophile_thermostability",
      "outcome": "supported",
      "assessment": "Broad Biolink association endpoints fit; biological strength remains source-dependent."
    },
    {
      "index": 12,
      "subject": "protein_aggregation_heat",
      "predicate": "associated with",
      "predicate_id": "biolink:associated_with",
      "object": "denatured_protein_refolding",
      "outcome": "supported",
      "assessment": "Broad association between aggregation and refolding processes is not a role defect."
    },
    {
      "index": 13,
      "subject": "denatured_protein_refolding",
      "predicate": "associated with",
      "predicate_id": "biolink:associated_with",
      "object": "thermophile_thermostability",
      "outcome": "supported",
      "assessment": "Broad association to thermostability context is not assigned narrow RO constraints."
    }
  ],
  "source": [
    {
      "index": 0,
      "subject": "hot_environment",
      "predicate": "selects for",
      "object": "thermophile_thermostability",
      "outcome": "SUPPORTED_GENERIC_CONTEXT",
      "assessment": "Tolner supports high-temperature environmental adaptation context. The approximate40°C optimum threshold and an evolutionary selection claim are not directly calibrated in the inspected abstract.",
      "locator": "tolner-metadata.json; opening adaptation context"
    },
    {
      "index": 1,
      "subject": "thermophile_thermostability",
      "predicate": "confers",
      "object": "temperature_optimum_high_trait",
      "outcome": "UNKNOWN_EXACT_CAUSAL_SCOPE",
      "assessment": "Vieille/Zeikus describes enzyme thermostability in hyperthermophiles, not a sufficient rule that thermostability yields every &gt;40°C growth optimum. Exact causal/bin calibration remains unknown because the primary body is unavailable here.",
      "locator": "vieille-metadata.json; abstract first sentence and enzyme-versus-organism scope"
    },
    {
      "index": 2,
      "subject": "temperature_optimum_high_trait",
      "predicate": "is a",
      "object": "temperature_optimum",
      "outcome": "UNKNOWN_NUMERIC_CALIBRATION",
      "assessment": "The local high-optimum-to-optimum hierarchy is coherent but the cited abstract does not itself define the approximate40°C threshold or its complete distribution. No unavailable-body absence claim.",
      "locator": "tolner-metadata.json; generic thermophile scope"
    },
    {
      "index": 3,
      "subject": "reverse_gyrase",
      "predicate": "positively regulates",
      "object": "dna_positive_supercoiling",
      "outcome": "SUPPORTED_SOURCE_ATTRIBUTION",
      "assessment": "Takemata abstract explicitly describes reverse gyrase introducing positive supercoils. Source context is particularly thermophiles above65°C; this is not a universal defining mechanism for all &gt;40°C optima. Formal protein/process relation roles are separately reviewed.",
      "locator": "takemata.xml; abstract and bodyp2"
    },
    {
      "index": 4,
      "subject": "dna_positive_supercoiling",
      "predicate": "decreases",
      "object": "dna_melting_high_temperature",
      "outcome": "SUPPORTED_WITH_PHYSIOLOGICAL_QUALIFICATION",
      "assessment": "The exact thermal-denaturation phrase is attributed to a widely accepted idea in paragraph4. Paragraph6 explicitly debates the physiological importance of positive supercoiling, with cross-species variation. Preserve the accepted biophysical explanation separately from established universal in-vivo necessity or sufficiency.",
      "locator": "takemata.xml; bodyp4 and p6"
    },
    {
      "index": 5,
      "subject": "nucleoid_associated_proteins",
      "predicate": "increases",
      "object": "genome_thermostability",
      "outcome": "SUPPORTED_WITH_ASSAY_QUALIFICATION",
      "assessment": "The record note correctly identifies in-vitro DNA melting-temperature observations and a correlation with archaeal growth temperature. These are not proof that every NAP determines an organism optimum.",
      "locator": "takemata.xml; bodyp10"
    },
    {
      "index": 6,
      "subject": "small_heat_shock_proteins",
      "predicate": "prevents",
      "object": "protein_aggregation_heat",
      "outcome": "SUPPORTED_ARCHAEAL_CONTEXT",
      "assessment": "The supplied protection phrase and note match the Sulfolobales introductory description. No new detailed intervention efficacy or universal temperature-bin inference is established.",
      "locator": "baes.xml; bodyp1"
    },
    {
      "index": 7,
      "subject": "thermosome",
      "predicate": "enables",
      "object": "denatured_protein_refolding",
      "outcome": "SUPPORTED_ARCHAEAL_CONTEXT",
      "assessment": "The introductory description explicitly attributes ATP-dependent refolding to the thermosome. This supports the existing environmental archaeal protein context, not a specified organism-wide optimum.",
      "locator": "baes.xml; bodyp1"
    },
    {
      "index": 8,
      "subject": "membrane_lipid_composition",
      "predicate": "contributes to",
      "object": "membrane_thermostability",
      "outcome": "SUPPORTED_RESPONSE_CONTEXT",
      "assessment": "The source reports altered membrane lipid composition during Sulfolobales heat shock. The current note already frames this as a response branch rather than a single thermophily determinant; specific causal contribution to stability remains contextual.",
      "locator": "baes.xml; bodyp1 opening sentence"
    },
    {
      "index": 9,
      "subject": "aa_composition_thermostability",
      "predicate": "increases",
      "object": "thermophile_thermostability",
      "outcome": "SUPPORTED_GENERIC_CONTEXT",
      "assessment": "The hyperthermophile introduction lists amino-acid enrichment among adaptation mechanisms. This is generic context, not a direct measurement that enrichment sets the &gt;40°C bin for all organisms.",
      "locator": "grunberger.xml; bodyp1"
    },
    {
      "index": 10,
      "subject": "dna_positive_supercoiling",
      "predicate": "associated with",
      "object": "genome_thermostability",
      "outcome": "SUPPORTED_QUALIFIED_ASSOCIATION",
      "assessment": "Takemata presents reverse gyrase as considered to protect thermophile genomes, with particular &gt;65°C context; retain paragraph6 physiological qualification. Association is not demonstrated whole-bin causality.",
      "locator": "takemata.xml; bodyp2 and p6"
    },
    {
      "index": 11,
      "subject": "genome_thermostability",
      "predicate": "associated with",
      "object": "thermophile_thermostability",
      "outcome": "SUPPORTED_QUALIFIED_ASSOCIATION",
      "assessment": "Takemata links NAPs and other factors to DNA thermostability. The modest association wording is contextual; in-vitro/correlation limits are retained.",
      "locator": "takemata.xml; bodyp2 and p10"
    },
    {
      "index": 12,
      "subject": "protein_aggregation_heat",
      "predicate": "associated with",
      "object": "denatured_protein_refolding",
      "outcome": "SUPPORTED_QUALIFIED_ASSOCIATION",
      "assessment": "Baes introduction places small-HSP/prefoldin protection and thermosome refolding in a shared protein-quality description. No new mechanistic intervention or direct optimum effect is asserted here.",
      "locator": "baes.xml; bodyp1"
    },
    {
      "index": 13,
      "subject": "denatured_protein_refolding",
      "predicate": "associated with",
      "object": "thermophile_thermostability",
      "outcome": "SUPPORTED_QUALIFIED_ASSOCIATION",
      "assessment": "Thermosome composition/substrate specificity is described in the selected introduction. The connector remains protein-quality context, not proof of a quantitative optimal temperature.",
      "locator": "baes.xml; bodyp1"
    }
  ]
}

### Native checklist: quantitative overview and optional proteins

scope: supported. Targets: METPO:1000447.

Two components are explicitly retained after corrective pruning. Four protein classes and three reviewed label-only classes with zero instances are permitted in this NONMECHANISTIC quantitative overview; no token protein or forced connector is requested.

### Native checklist: bounded catalog and unavailable adapter

evidence: unknown. Targets: METPO:1000447.

The retained catalog has source S.acidocaldarius/modulome coverage, but no exact canonical S.islandicus/REY15A match. Fresh bounded discovery establishes adapter unavailability for the appropriate generic source queries. Catalog/primary fallback supports context only; no unexecuted query result, membership or cross-species transfer is claimed.

### Native checklist: exact owners and replay boundaries

consistency: supported. Targets: METPO:1000447.

The current reviewer exact-after guard is a no-op; its source constants own current assertions. The connector retains disputed source preimages but current replay rejects after corrective pruning. Repair uses filtered ADDED_EDGES, not current RO-role payloads. Shared grounders skip populated IDs; node3 facet has record-only ownership.

### Native checklist: attributable current acceptance

provenance: concern. Targets: METPO:1000447.

Twenty embedded AI events plus a seed and the ignored-inclusive182-path/68-array search do not establish current human acceptance. Four whole history files were read now and ten prior whole readings qualified by identical bytes; private or remote acceptance remains unknown.

### Native checklist: checks, snapshots and chronology

consistency: supported. Targets: METPO:1000447.

All85 inputs and36/29 frozen audit artifacts match, with the expression supplement and original line-count correction bound separately. Focused native checks passed; common B13 reuse retains original diagnostics, optional failures/retries and skips. Acquisition, copy and reading times remain distinct.

## Findings

### imported-process-roles: Imported relation roles conflict with current material and property referents

major / open / confirmed; issue key: temperature-optimum-high-imported-process-roles.

One connected representation issue affects five edges and the coupled thermostability facet. RO:0002211 requires process subjects and objects; RO:0002212 and RO:0002213 inherit those roles. Edge3 explicitly names a reverse-gyrase protein class, edge5 a NAP material subject and genome-resistance quality object, edge6 a small-HSP material subject, and edge9 a thermostability/property object despite node3 being declared BIOLOGICAL_PROCESS. Edge8 uses RO:0002326, whose material-to-process roles are inherited through RO:0002216, RO:0002500 and RO:0002595; its explicit lipid-remodeling process subject independently conflicts. The allowed GO molecular-function grounding does not silently retype the named protein. Node3 label/description names thermostability and heat-stable material rather than an activity; that facet is counted once with edge9. Enrichment process/result and stabilization/property ambiguities remain qualified. These are formal referent/role findings, separate from physiological efficacy.

### human-acceptance-link: Reviewed status lacks locally attributable acceptance

minor / open / confirmed; issue key: temperature-optimum-high-human-acceptance-link.

Current REVIEWED status lacks attributable human acceptance of present assertions in inspected local evidence. The ignored- and hidden-inclusive search, excluding .git and .venv, found182 matching paths and68 actual review target arrays with no exact target. Twenty-one embedded events comprise twenty AI events and one seed; the three exact-target repository histories have AI actors. Private or remote acceptance remains unknown.

## Recommended Actions And Acceptance Checks

### resolve-imported-process-roles

In separately authorized curation, reconcile actual material, process and quality referents with inherited predicate roles, including node3 thermostability. Update reviewer source assertions and connector preimage expectations together while preserving exact guards and corrective pruning. Current reviewer exact-after checks no-op; connector replay rejects its pruned current shape before mutation. Its SOURCE_CONNECTOR_EDGES are guarded historical preimages, not an unconditional overwrite. Repair_pr664 uses filtered ADDED_EDGES and does not own the disputed current RO-role payloads. Shared grounding skips populated IDs, so rerunning it alone is not a fix; node3 facet has record-only ownership within this group.

- Show compatible actual referents and inherited predicate roles without inventing process identities, numerical calibration or mechanisms.
- Preserve legacy allowed GO molecular-function grounding, NONMECHANISTIC scope, two components and three reviewed label-only classes; no required protein instance or forced connector.
- Retain all sixteen literal-source positives, canonical reported optimum and source uncertainty. Validate strict record/schema, relevant graph/predicate audits, QC and required history/product gates.

### resolve-human-acceptance-link

Link attributable human acceptance of current assertions or reconcile REVIEWED through the native status workflow in separately authorized curation. Preserve existing AI actors and history.

- Human reviewer and accepted assertion scope are attributable, or status accurately reflects available evidence.
- Per-record and repository history validates and AI assistance remains explicit.

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
| check-temperature-optimum-high-validate | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-validate.log; Executed 2026-10-22T00:38:24.641489+00:00 through 2026-10-22T00:38:25.358642+00:00; metadata temperature-optimum-high-validate.json | context_only | Native record validation passed; scientific interpretation is assessed separately. |
| check-temperature-optimum-high-strict | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-strict.log; Executed 2026-10-22T00:38:24.641612+00:00 through 2026-10-22T00:38:25.727995+00:00; metadata temperature-optimum-high-strict.json | context_only | Actual validate-strict command passed. |
| check-temperature-optimum-high-snippets-network | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-snippets-network.log; Executed 2026-10-22T00:38:41.864632+00:00 through 2026-10-22T00:38:50.166278+00:00; metadata temperature-optimum-high-snippets-network.json | context_only | Six of sixteen schema snippets were VERIFIED; ten were NOT_IN_ABSTRACT in the native abstract check. Separate manual inspection verifies all sixteen literal spans. Native inconclusive results are not body-absence evidence. |
| check-batch012-qc | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/batch012-qc.log; Executed 2026-10-21T23:02:31.440808+00:00 through 2026-10-21T23:04:01.628423+00:00; metadata batch012-qc.json | context_only | Actual prior QC qualified against B13 bytes; this is not a new B13 QC execution or publication. |
| record | data/traits/environment/temperature_optimum_high.yaml; Whole 457-line current record | supports | Sixteen nodes, fourteen edges, twenty-one embedded events, one canonical example, four protein classes and zero instances. |
| inspect-reading-correction | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high.inspect-reading-correction.json; Derived audit or reading receipt; primary bytes and original acquisitions bound separately | supports | Original inspect receipt misstated 442 lines; append-only correction records the actual complete 457-line reading without altering original command, capture or target bytes. |
| reuse | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-b12-qc-supplement-qualified.json; Actual B12-to-B13 qualification | supports | Original diagnostic times, failures, retries and skips remain explicit. |
| reuse-postcheck | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-output-verification-agent/post-execution-verification.json; Independent actual-output verification | supports | Qualification verification, not new QC. |
| local-init | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/batch013-local-initialization-receipt.json; Derived audit or reading receipt; primary bytes and original acquisitions bound separately | supports | Actual local initialization; publication remains separate. |
| policy | docs/GROUNDING_POLICY.md; Captured maintained authority | supports | Actual referents, allowed legacy molecular-function grounding and optional protein instances. |
| playbook | docs/CURATION_PLAYBOOK.md; Captured maintained authority | supports | Source scope and attributable current acceptance. |
| schema | src/traitmech/schema/traitmech.yaml; Captured maintained authority | supports | Current facets and NONMECHANISTIC scope. |
| predicate-mapping | mappings/predicate_grounding.tsv; Captured maintained authority | supports | Shared future-empty-field mapping; populated predicate IDs are skipped. |
| node-mapping | mappings/node_grounding.tsv; Captured maintained authority | supports | Reverse-gyrase functional grounding, distinct from a protein instance. |
| local-v2 | proposals/metpo_traitmech_v2/metpo_proposal_properties_robot.tsv; Captured maintained authority | supports | Local selects-for broad endpoints, separate from imported RO roles. |
| local-v8 | proposals/metpo_traitmech_v8/metpo_proposal_properties_robot.tsv; Captured maintained authority | supports | Local confers broad endpoints and trait range. |
| identity | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-ground-agent/identity-assessment.json; Derived audit or reading receipt; primary bytes and original acquisitions bound separately | supports | Active high-bin identity and direct parent; inclusive endpoint qualification. |
| nodes-edges | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-ground-agent/node-edge-grounding-ledger.json; Derived audit or reading receipt; primary bytes and original acquisitions bound separately | supports | All sixteen node and fourteen relation judgments, including contrary controls. |
| owners | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-ground-agent/owner-provenance-assessment.json; Derived audit or reading receipt; primary bytes and original acquisitions bound separately | supports | Exact current, conditional and sibling owner distinctions. |
| owner-primary | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-ground-agent/owner-primary-reading.json; Derived audit or reading receipt; primary bytes and original acquisitions bound separately | supports | Whole reviewer/connector and selected repair/shared-grounder guards. |
| writer-shape | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-ground-agent/writer-current-shape-check.json; Derived audit or reading receipt; primary bytes and original acquisitions bound separately | supports | Reviewer exact-after no-op and connector rejection after pruning; repair does not supply current RO roles. |
| human-search | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-ground-agent/search-and-provenance.json; Derived audit or reading receipt; primary bytes and original acquisitions bound separately | supports | 182 ignored-inclusive matching paths, 68 actual target arrays, zero exact current target. |
| histories | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-ground-agent/history-reading-provenance.json; Derived audit or reading receipt; primary bytes and original acquisitions bound separately | supports | Four current whole history reads plus ten unchanged qualified prior reads; fourteen current projections. |
| discovery | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-ground-agent/discovery-disposition.json; Derived audit or reading receipt; primary bytes and original acquisitions bound separately | supports | All history leads captured; one uncaptured thermotaxis script is matching-line-only context. |
| expression-original | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-ground-agent/expression-and-readiness.json; Derived audit or reading receipt; primary bytes and original acquisitions bound separately | supports | Retained original catalog/coverage receipt; scope-only query omission rationale is superseded by the separate supplement. |
| expression-supplement | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-ground-agent/expression-supplement.json; Derived audit or reading receipt; primary bytes and original acquisitions bound separately | supports | Covered benign source query is appropriate; current bounded adapter unavailability prevents execution, with catalog/source fallback and no membership result. |
| expression-discovery | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-ground-agent/expression-runner-current-discovery.json; Derived audit or reading receipt; primary bytes and original acquisitions bound separately | supports | Actual current PATH/project/install search, bounded unavailable adapter result. |
| local-authority | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-ground-agent/local-authority-reading.json; Derived audit or reading receipt; primary bytes and original acquisitions bound separately | supports | Exact local proposal, mapping, Biolink and schema/policy windows. |
| ground-reading | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-ground-agent/reading-scope-receipt.json; Derived audit or reading receipt; primary bytes and original acquisitions bound separately | supports | Actual agent readings and honest prior-read reuse scope. |
| ground-manifest | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-ground-agent/evidence-manifest.json; Derived audit or reading receipt; primary bytes and original acquisitions bound separately | supports | Twenty-nine unchanged frozen artifacts plus separately bound expression supplement. |
| metpo-primary | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/repo/data/raw/metpo.owl; Selected primary authority statements, read at the recorded time | supports | Active high class and direct parent; existential inclusive40 Cel versus approximate prose is qualified. |
| metpo-primary-projection | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-ground-agent/metpo-authority.json; Derived audit or reading receipt; primary bytes and original acquisitions bound separately | supports | Exact source bytes and selected statement projection. |
| go-primary | /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/go.db; Selected primary authority statements, read at the recorded time | supports | GO0160097 is reverse gyrase molecular function, not a biological process. |
| go-primary-projection | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-ground-agent/selected-go-primary-reading.json; Derived audit or reading receipt; primary bytes and original acquisitions bound separately | supports | Exact source bytes and selected statement projection. |
| ro-primary | /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/ro.db; Selected primary authority statements, read at the recorded time | supports | Actual inherited regulation process roles and material-to-process capable-of chain. |
| ro-primary-projection | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-ground-agent/selected-ro-primary-reading.json; Derived audit or reading receipt; primary bytes and original acquisitions bound separately | supports | Exact source bytes and selected statement projection. |
| tolner-metadata | DOI:10.1016/s0300-9629(97)00003-0; Indexed abstract and identifier/status fields | supports | Generic adaptation and literal spans; exact threshold and sufficiency remain unknown. |
| vieille-metadata | DOI:10.1128/MMBR.65.1.1-43.2001; Indexed abstract and identifier/status fields | supports | Enzyme thermostability context and literal phrase; no full-body interpretation. |
| vieille-error | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC99017/fullTextXML; Original failed body request and retained error bytes; not XML article content | context_only | Historical access limit, not current native-check failure or full-paper absence. |
| grunberger-metadata | DOI:10.1128/mbio.02174-23; Indexed identity/status and broad organism context | supports | Preprint link is not a retraction or correction. |
| grunberger-primary | DOI:10.1128/mbio.02174-23; Zero-based body paragraph1, existing introductory phrase only | supports | Hyperthermophile context does not set a universal quantitative optimum. |
| takemata-metadata | DOI:10.1264/jsme2.me23087; Indexed identity/status and abstract | supports | Identity and supplied activity wording; physiological conclusions remain source-qualified. |
| baes-metadata | DOI:10.1128/mbio.03593-22; Indexed identity/status | supports | Sulfolobales source identity; Preprint-in link is not correction/retraction. |
| canonical-metadata | DOI:10.3389/fmicb.2023.1219779; Indexed identity/status and organism context | supports | Study identity; exact reported optimum is supported by the selected body separately. |
| takemata-primary | DOI:10.1264/jsme2.me23087; Abstract and zero-based body paragraphs2/4/6/10 | supports | Supplied spans and generic attribution retain physiological debate, in-vitro observations and correlations; no universal-bin necessity or sufficiency. |
| baes-primary | DOI:10.1128/mbio.03593-22; Zero-based body paragraph1, selected introductory phrases | supports | Existing Sulfolobales context and literal snippets; no methods/results or intervention-efficacy audit. |
| canonical-primary | DOI:10.3389/fmicb.2023.1219779; Section2.1, zero-based body paragraph3, first two sentences | supports | REY15A reported optimum-control76 degrees C is distinct from the66-degree comparison; no complete response curve claimed. |
| taxonomy | NCBITaxon:43080; Whole successful official species response | supports | Saccharolobus islandicus and former Sulfolobus islandicus name are positive. Species identity is distinct from the source strain and phenotype. |
| taxonomy-reading | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-ground-agent/taxonomy-identity.json; Derived audit or reading receipt; primary bytes and original acquisitions bound separately | supports | Successful primary XML and initial DNS-error bytes are kept separate. |
| sources | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-source-agent/source-assessment.json; Derived audit or reading receipt; primary bytes and original acquisitions bound separately | supports | Six works, no source finding, overall UNKNOWN for exact threshold/sufficient optimum claims. |
| source-identities | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-source-agent/source-identities-status.json; Derived audit or reading receipt; primary bytes and original acquisitions bound separately | supports | All six assigned identities and bounded publication-notice fields. |
| placements | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-source-agent/source-placement-ledger.json; Derived audit or reading receipt; primary bytes and original acquisitions bound separately | supports | All eighteen external placements and seventeen grounding fields accounted. |
| snippets | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-source-agent/snippet-ledger.json; Derived audit or reading receipt; primary bytes and original acquisitions bound separately | supports | All sixteen short supplied schema snippets literal on inspected primary surfaces. |
| notes | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-source-agent/source-note-ledger.json; Derived audit or reading receipt; primary bytes and original acquisitions bound separately | supports | All sixteen evidence notes with explicit physiological/assay scope. |
| source-nodes-edges | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-source-agent/node-edge-source-ledger.json; Derived audit or reading receipt; primary bytes and original acquisitions bound separately | supports | All sixteen nodes and fourteen edges; generic attribution distinct from causal sufficiency. |
| source-reading | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-source-agent/primary-reading-scope.json; Derived audit or reading receipt; primary bytes and original acquisitions bound separately | supports | Selected generic primary passages; no full-article scientific or excluded mechanism assessment. |
| source-access | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-source-agent/source-access-limits.json; Derived audit or reading receipt; primary bytes and original acquisitions bound separately | supports | Abstract-only sources and historical body failure remain unknown, not refuted. |
| source-reuse | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-source-agent/source-reuse-receipt.json; Derived audit or reading receipt; primary bytes and original acquisitions bound separately | supports | Original request clocks, current copy clocks and current interpretation remain distinct. |
| canonical | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-source-agent/canonical-assessment.json; Derived audit or reading receipt; primary bytes and original acquisitions bound separately | supports | Reported76-degree optimum-control is positive within stated source conditions; no exhaustive curve. |
| source-native | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-source-agent/native-check-context.json; Derived audit or reading receipt; primary bytes and original acquisitions bound separately | supports | Native six VERIFIED/ten inconclusive differs from sixteen manual literal confirmations. |
| source-manifest | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-source-agent/evidence-manifest.json; Derived audit or reading receipt; primary bytes and original acquisitions bound separately | supports | Thirty-six frozen source artifacts verified. |
| root-reading | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-source-root/selected-primary-reading.json; Derived audit or reading receipt; primary bytes and original acquisitions bound separately | supports | Independent selected primary/authority/owner readings; three whole exact-target histories and fourteen projections, not fourteen root whole-body readings. |
| adjudication | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-root-adjudication.json; Final root adjudication | supports | Exact final findings, field anchors, owner qualifications and actions control serialization. |

## Limits And Additional Notes

- Overall sources UNKNOWN for exact approximately40°C category calibration, exact Thermophile synonym equivalence, and sufficient thermostability-to-whole-organism-optimum claims. Missing body is not evidence of falsehood.
- Tolner and Vieille/Zeikus support inspected abstract context only; Vieille retained fullTextXML attempt is HTTP500 error bytes, not primary body. No duplicate attempt or full-paper absence claim.
- Takemata accepted thermal-denaturation idea is distinguished from the same review’s debate over in-vivo physiological importance; greater-than65°C specificity is context, not a universal40°C definition.
- NAP melting-temperature evidence is in vitro and archaeal abundance association is correlational. Do not convert either to universal necessity/sufficiency for the bin.
- Baes context is Sulfolobales heat-shock response; Grünberger introductory statement concerns hyperthermophilic archaea. These generic statements do not establish every organism-specific optimal temperature.
- Canonical is REY15A reported optimal-control76°C at pH3.4 versus66°C comparator, not a complete response curve. Incidental displayed methods, dataset-access text and other conditions were not adopted or used.
- Detailed dangerous-pathogen stress/fitness/defense/ROS/AMR/intervention mechanisms and efficacy remain UNASSESSED_SCOPE. No source follow-up proposes physiological enhancement.
- Metadata notice fields show two Preprint-in links, not retractions/corrections. Publication status is bounded to inspected primary metadata and selected body frontmatter.
- Source-organism catalog relevance is bounded to actually named contexts: canonical S.islandicus REY15A, Baes S.acidocaldarius/Sulfolobales, Grünberger P.furiosus, generic Takemata Bacteria/Archaea. No exact strain/module/efficacy inference from species-level coverage.
- Inclusive40 numeric restriction differs from approximate above40/related &gt;40 wording; bounded upstream endpoint nuance, no independent finding.
- Node5 process/state wording and edge4 causal interpretation remain qualified; wrong process wording in historical GO rationale does not invalidate actual MF protein grounding.
- Node14 stabilization/quality and node15 enrichment process/result ambiguity are qualified; firm role findings have independent endpoints.
- Detailed dangerous-pathogen mechanisms UNASSESSED_SCOPE; generic source physiological sufficiency and exact bin causal calibration require separate source review.
- One uncaptured thermotaxis script is matching-line context only; no unbounded owner absence claim.
- Catalog source-organism coverage does not establish exact canonical dataset or intervention/module evidence.
- Private/remote human acceptance remains unknown.
- The current expression supplement supersedes the earlier scope-only omission rationale: an appropriate generic query for catalog-covered benign S.acidocaldarius was not executed because the adapter was unavailable within the fresh bounded search. Catalog and selected primary fallback do not establish module membership or canonical strain coverage.
- Official JStage releaseJune6,2024 and February8,2025 license-display PDF correction were inspected. Indexed first-publicationJanuary1,2024 is an index field, not asserted as exact release. The license correction is not a biological correction; publication-notice inspection is not exhaustive.
- Root read three exact-target histories whole and fourteen compact actor/target/read-mode projections; agent read four current whole histories and qualified ten unchanged prior whole readings.
- Original acquisitions, current copies and current readings are distinct. Browser tool-call bounds do not establish cache origin-fetch times.
- Native snippets six VERIFIED and ten NOT_IN_ABSTRACT are distinct from all sixteen manually located literal spans. Literal occurrence does not establish the adjacent exact-bin causal interpretation.
- Current adapter-unavailable expression supplement supersedes only the earlier scope-based omission rationale; frozen ground manifest remains unchanged.
- Original source acquisitions, current copies and selected readings remain distinct; sixteen literal matches do not establish universal optimum causation.
- Qualified B12/common diagnostics are not fresh B13 QC or publication; retained optional failures/retries and123 no-adapter skips remain explicit.
- Whole457-line target and85 captured inputs; six sources/eighteen placements/seventeen grounding fields/sixteen literal snippets and sixteen evidence notes.
- Ground history scope is four current whole bodies plus ten qualified prior whole readings; root read three exact-target histories whole and fourteen projections.
- Original inspect receipt442-line typo remains immutable and is corrected by the bound457-line addendum.
- Root owns any eventual one-time serialization, actual-output review, native validation and save; this preparation did not execute or import the serializer.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T004826Z-temperature-optimum-high
kind: record
repository: CultureBotAI/TraitMech
title: Whole-record review of temperature optimum high
started_at: '2026-10-22T00:38:05.328146Z'
finished_at: '2026-10-22T00:48:26Z'
reviewer:
  identity: codex
  kind: agent
  independence: independent
  independence_basis: Separate source and grounding audits plus independent root primary,
    owner, source and final-adjudication readings. This serializer adopts those bounded
    judgments without claiming another independent biological review.
  model: GPT-6 (Codex)
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Temperature optimum high needs one grouped representation repair for five
  imported-role edges and the coupled thermostability facet, plus a link to attributable
  human acceptance. Active identity, canonical reported optimum and all sixteen literal
  snippets are supported; exact category calibration and sufficient organism-optimum
  claims remain unknown.
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
  - path: data/traits/environment/temperature_optimum.yaml
    sha256: e419e363fd4b2e26f2ce3f092b117fba3103e5155e6dafb95bb5ce5c76644a0d
    role: context
  - path: data/traits/environment/temperature_optimum_high.yaml
    sha256: 55c6a5d2c2b644a373eb0a21b5d4b7fa32fde87fb625017ae9cc98bf61977280
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
  - path: history/infrastructure/canonical-examples/2026-08-19T183734Z-claude-code-44a170.yaml
    sha256: b6155e63f3c4719b794f7d71c65f9ccaa3e01030b0d5b676b33e4dd5a542cc62
    role: context
  - path: history/infrastructure/pr664-adversarial-review/2026-09-07T010000Z-codex-60bca2.yaml
    sha256: 44f328d3f4735a641a33e6f5823a043ccc87594971cfdd9b58be134f3ea70106
    role: context
  - path: history/infrastructure/process-quality-consistency/2026-08-21T073211Z-codex-174227.yaml
    sha256: e35d99e8285d488d98584d046aa001825527609cfd62575b3b839c4a31230642
    role: context
  - path: history/other/canonical-examples-batch1/2026-08-20T074839Z-claude-code-6fb2f5.yaml
    sha256: c938f2928f2eb41505d58c2fb72d8de01d99534d766de9af400010e8778988a4
    role: context
  - path: history/other/canonical-examples-six/2026-08-21T065406Z-codex-a1ab82.yaml
    sha256: 23be5f6ab519511e3e23feffa85813eec4fa3c7e6b900e77fd4a3adc0c26da0e
    role: context
  - path: history/records/temperature_optimum/2026-09-15T070759Z-codex-e0d923.yaml
    sha256: 05e6ac08e579e45031473bc1b2ebd8089d18d639534ac5db409d705943882b86
    role: context
  - path: history/records/temperature_optimum_high/2026-09-04T032000Z-codex-f0b8c3.yaml
    sha256: fea3d657cff8ef0b7a7fe783991943f1248f163f2a8ca59ddb218a4183649772
    role: context
  - path: history/records/temperature_optimum_high/2026-09-04T200000Z-codex-183.yaml
    sha256: 10cd203cb37e56abd0f36721b0cdb857bd1f0c769d200d4df963028bb1ab0761
    role: context
  - path: history/records/temperature_optimum_high/2026-09-08T033000Z-codex-506e08.yaml
    sha256: d7aa33a420444c86380ce26aa63c3a77950a19306f3b9bd3692bf2f5be0be999
    role: context
  - path: history/records/temperature_optimum_mid1/2026-09-15T070759Z-codex-35d0a7.yaml
    sha256: c10f51ae7c1806d27cf51df19d9b2e8a601cbdae078a9cf1de8ffab49f339a53
    role: context
  - path: history/records/temperature_optimum_mid3/2026-09-15T070800Z-codex-44b4c3.yaml
    sha256: 410c667e0f7988e3f8df1319c4e42326130b5ee46b34854009b8a744b67ab5e7
    role: context
  - path: history/records/temperature_optimum_very_low/2026-09-04T034000Z-codex-1f380e.yaml
    sha256: 86baac0f11d45ba1989ba43c4c8a43294c652ebd6298f98cccdbb3cd9b32b198
    role: context
  - path: history/records/temperature_optimum_very_low/2026-09-04T210000Z-codex-183.yaml
    sha256: d2dff988a235fc27369f305585f4e865266f3dabf23fa06670a6e30a415f2f6e
    role: context
  - path: history/records/temperature_optimum_very_low/2026-09-08T032500Z-codex-77dafe.yaml
    sha256: dfa857844cb78f8fbb905a762242c0671701caf54fe35c81da0c38422142cab3
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
  - path: research/traits/environment/temperature_optimum_high-deep-research-falcon.md
    sha256: bdcb409d66de87d71e6dd844f794cedcd82e46833d9d2bd8aaf3bf73c599bf1c
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
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
  - path: scripts/connect_temperature_optimum_high_graph_183.py
    sha256: 7d2c6bee0f2af46cec82afe93b93b5a993ffb6042f953e7793b2bbc6ea713504
    role: context
  - path: scripts/connect_temperature_optimum_very_low_graph_183.py
    sha256: 4749be5b5aacc87817ea013e587c41096e8a213c93dde74546f4906a0a08dc7e
    role: context
  - path: scripts/connect_temperature_range_mid4_graph_183.py
    sha256: dd4b85888e88346adb515170c8fa37d542c7c7d9307d8a9fc63b22bdd6fb8b70
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
  - path: scripts/review_temperature_delta_high_graph_183.py
    sha256: dcade5d2fdf07c76e06cd5d8abca898af95a8faabf70e45a62bebf951f2ae31b
    role: context
  - path: scripts/review_temperature_optimum_high_graph_183.py
    sha256: ed7b046129400db1fa4352250d27569e0844ef837000577f1448e565a0e60576
    role: context
  - path: scripts/review_temperature_optimum_very_low_graph_183.py
    sha256: 17e41b0426e6c41a43e7624799cf35db9737ef372d3aeb3ea40ac0a2dce20869
    role: context
  - path: scripts/review_temperature_range_mid4_graph_183.py
    sha256: 51611a8200146f1887831e5b2a49800151dc0b112d177853c3055dd442852a5a
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
- target_id: METPO:1000447
  path: data/traits/environment/temperature_optimum_high.yaml
  label: temperature optimum high
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_optimum_high.yaml
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
  selection: Ninth record of the actual local batch 013 queue. Whole 457-line target
    and 85 captured inputs verified; local review does not assert remote publication.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - METPO:1000447
checks:
- check_id: audit-graphs
  name: Full-corpus graph audit
  status: passed
  required: true
  target_ids:
  - METPO:1000447
  command: just audit-graphs --out /private/tmp/traitmech-record-sweep.FU79Gr/causal_graph_audit.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  evidence_ids:
  - check-audit-graphs
  scope_note: 'History validation ran in batch 003 at the 8eee source base. Original
    common diagnostics ran at f25, with the documented seven-file workflow/skill/infrastructure-history
    delta to 8eee. B13 reuse is permitted only after the separate B12-final qualification
    receipt passes the runtime guard. Original timestamps, failures, retries and skips
    remain explicit. B12 final QC is separate evidence and is not automatically added
    as a new B13 execution. Qualification: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-b12-qc-supplement-qualified.json'
- check_id: audit-snippets
  name: Full-corpus snippet audit
  status: passed
  required: true
  target_ids:
  - METPO:1000447
  command: just audit-snippets --report /private/tmp/traitmech-record-sweep.FU79Gr/evidence_snippet_audit.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  evidence_ids:
  - check-audit-snippets
  scope_note: 'History validation ran in batch 003 at the 8eee source base. Original
    common diagnostics ran at f25, with the documented seven-file workflow/skill/infrastructure-history
    delta to 8eee. B13 reuse is permitted only after the separate B12-final qualification
    receipt passes the runtime guard. Original timestamps, failures, retries and skips
    remain explicit. B12 final QC is separate evidence and is not automatically added
    as a new B13 execution. Qualification: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-b12-qc-supplement-qualified.json'
- check_id: check-pathway-links
  name: Full-corpus pathway links
  status: passed
  required: true
  target_ids:
  - METPO:1000447
  command: just check-pathway-links
  exit_code: 0
  expected_exit_code: 0
  summary: 19 links checked against the pinned PathwayMech snapshot.
  evidence_ids:
  - check-check-pathway-links
  scope_note: 'History validation ran in batch 003 at the 8eee source base. Original
    common diagnostics ran at f25, with the documented seven-file workflow/skill/infrastructure-history
    delta to 8eee. B13 reuse is permitted only after the separate B12-final qualification
    receipt passes the runtime guard. Original timestamps, failures, retries and skips
    remain explicit. B12 final QC is separate evidence and is not automatically added
    as a new B13 execution. Qualification: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-b12-qc-supplement-qualified.json'
- check_id: validate-history
  name: Full-corpus history integrity
  status: passed
  required: true
  target_ids:
  - METPO:1000447
  command: just validate-history
  exit_code: 0
  expected_exit_code: 0
  summary: 1277 history records checked, zero invalid links at the 8eee source base;
    integrity does not establish science or human acceptance.
  evidence_ids:
  - check-validate-history
  scope_note: 'History validation ran in batch 003 at the 8eee source base. Original
    common diagnostics ran at f25, with the documented seven-file workflow/skill/infrastructure-history
    delta to 8eee. B13 reuse is permitted only after the separate B12-final qualification
    receipt passes the runtime guard. Original timestamps, failures, retries and skips
    remain explicit. B12 final QC is separate evidence and is not automatically added
    as a new B13 execution. Qualification: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-b12-qc-supplement-qualified.json'
- check_id: validate-products
  name: Initial full-product validation
  status: failed
  required: false
  target_ids:
  - METPO:1000447
  command: just validate-products
  exit_code: 2
  expected_exit_code: 0
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  evidence_ids:
  - check-validate-products
  scope_note: 'History validation ran in batch 003 at the 8eee source base. Original
    common diagnostics ran at f25, with the documented seven-file workflow/skill/infrastructure-history
    delta to 8eee. B13 reuse is permitted only after the separate B12-final qualification
    receipt passes the runtime guard. Original timestamps, failures, retries and skips
    remain explicit. B12 final QC is separate evidence and is not automatically added
    as a new B13 execution. Qualification: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-b12-qc-supplement-qualified.json'
- check_id: validate-products-retry-local
  name: Product validation with isolated local cache
  status: failed
  required: false
  target_ids:
  - METPO:1000447
  command: just validate-products
  exit_code: 2
  expected_exit_code: 0
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  evidence_ids:
  - check-validate-products-retry-local
  scope_note: 'History validation ran in batch 003 at the 8eee source base. Original
    common diagnostics ran at f25, with the documented seven-file workflow/skill/infrastructure-history
    delta to 8eee. B13 reuse is permitted only after the separate B12-final qualification
    receipt passes the runtime guard. Original timestamps, failures, retries and skips
    remain explicit. B12 final QC is separate evidence and is not automatically added
    as a new B13 execution. Qualification: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-b12-qc-supplement-qualified.json'
- check_id: validate-products-retry-network
  name: Product validation after isolated-cache download
  status: passed
  required: true
  target_ids:
  - METPO:1000447
  command: just validate-products
  exit_code: 0
  expected_exit_code: 0
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  evidence_ids:
  - check-validate-products-retry-network
  scope_note: 'History validation ran in batch 003 at the 8eee source base. Original
    common diagnostics ran at f25, with the documented seven-file workflow/skill/infrastructure-history
    delta to 8eee. B13 reuse is permitted only after the separate B12-final qualification
    receipt passes the runtime guard. Original timestamps, failures, retries and skips
    remain explicit. B12 final QC is separate evidence and is not automatically added
    as a new B13 execution. Qualification: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-b12-qc-supplement-qualified.json'
- check_id: temperature-optimum-high-validate
  name: Focused native validation
  status: passed
  required: true
  target_ids:
  - METPO:1000447
  command: just validate data/traits/environment/temperature_optimum_high.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Native record validation passed; scientific interpretation is assessed
    separately.
  evidence_ids:
  - check-temperature-optimum-high-validate
- check_id: temperature-optimum-high-strict
  name: Focused strict validation
  status: passed
  required: true
  target_ids:
  - METPO:1000447
  command: just validate-strict data/traits/environment/temperature_optimum_high.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual validate-strict command passed.
  evidence_ids:
  - check-temperature-optimum-high-strict
- check_id: temperature-optimum-high-snippets-network
  name: Focused network snippet check
  status: passed
  required: true
  target_ids:
  - METPO:1000447
  command: just verify-snippets --record data/traits/environment/temperature_optimum_high.yaml
    --out /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-snippets.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: Six of sixteen schema snippets were VERIFIED; ten were NOT_IN_ABSTRACT
    in the native abstract check. Separate manual inspection verifies all sixteen
    literal spans. Native inconclusive results are not body-absence evidence.
  evidence_ids:
  - check-temperature-optimum-high-snippets-network
- check_id: batch012-qc
  name: Qualified batch-twelve QC
  status: passed
  required: true
  target_ids:
  - METPO:1000447
  command: just qc
  exit_code: 0
  expected_exit_code: 0
  summary: Actual prior QC qualified against B13 bytes; this is not a new B13 QC execution
    or publication.
  evidence_ids:
  - check-batch012-qc
- check_id: uniprot-applicability
  name: Protein-instance metadata applicability
  status: not_applicable
  required: false
  target_ids:
  - METPO:1000447
  summary: Four contextual protein classes, three reviewed label-only classes and
    zero instances. Legacy GO molecular-function grounding is permitted; no mandatory
    accession or instance follows from this quantitative NONMECHANISTIC overview.
  evidence_ids:
  - record
  - policy
  - go-primary
  - expression-supplement
- check_id: expression-adapter-availability
  name: Structured source-organism expression query availability
  status: unavailable
  required: false
  target_ids:
  - METPO:1000447
  summary: Generic queries for covered benign S.acidocaldarius were appropriate but
    not executed because current bounded discovery found the adapter unavailable.
    Retained catalog and selected assigned primary context are fallback; no module
    membership result or canonical species transfer.
  evidence_ids:
  - expression-supplement
  - expression-discovery
  - baes-primary
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
- evidence_id: check-temperature-optimum-high-validate
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-validate.log
  locator: Executed 2026-10-22T00:38:24.641489+00:00 through 2026-10-22T00:38:25.358642+00:00;
    metadata temperature-optimum-high-validate.json
  accessed_at: '2026-10-22T00:38:25.358642Z'
  support: context_only
  summary: Native record validation passed; scientific interpretation is assessed
    separately.
  snapshot_sha256: 71eb93d980451caa9889660f422b54e4485818bff0cfaf90bd4d9dc9f4959116
- evidence_id: check-temperature-optimum-high-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-strict.log
  locator: Executed 2026-10-22T00:38:24.641612+00:00 through 2026-10-22T00:38:25.727995+00:00;
    metadata temperature-optimum-high-strict.json
  accessed_at: '2026-10-22T00:38:25.727995Z'
  support: context_only
  summary: Actual validate-strict command passed.
  snapshot_sha256: d1220adaa1c24734197348cf2746ede7baed3ebc64faed9fac9bcb4b1088900c
- evidence_id: check-temperature-optimum-high-snippets-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-snippets-network.log
  locator: Executed 2026-10-22T00:38:41.864632+00:00 through 2026-10-22T00:38:50.166278+00:00;
    metadata temperature-optimum-high-snippets-network.json
  accessed_at: '2026-10-22T00:38:50.166278Z'
  support: context_only
  summary: Six of sixteen schema snippets were VERIFIED; ten were NOT_IN_ABSTRACT
    in the native abstract check. Separate manual inspection verifies all sixteen
    literal spans. Native inconclusive results are not body-absence evidence.
  snapshot_sha256: 0e359aa3ad9cf488c5c49c97dca462cfc47aaa78a1d80a6501e82cfefb1eaea2
- evidence_id: check-batch012-qc
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/batch012-qc.log
  locator: Executed 2026-10-21T23:02:31.440808+00:00 through 2026-10-21T23:04:01.628423+00:00;
    metadata batch012-qc.json
  accessed_at: '2026-10-21T23:04:01.628423Z'
  support: context_only
  summary: Actual prior QC qualified against B13 bytes; this is not a new B13 QC execution
    or publication.
  snapshot_sha256: 8ab67b821055863ce13616ed79a0acacaf61b632dcb80f6aa63fd45f0485c52b
- evidence_id: record
  kind: record_content
  reference: data/traits/environment/temperature_optimum_high.yaml
  locator: Whole 457-line current record
  accessed_at: '2026-10-22T00:38:05.818147Z'
  support: supports
  summary: Sixteen nodes, fourteen edges, twenty-one embedded events, one canonical
    example, four protein classes and zero instances.
  snapshot_sha256: 55c6a5d2c2b644a373eb0a21b5d4b7fa32fde87fb625017ae9cc98bf61977280
- evidence_id: inspect-reading-correction
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high.inspect-reading-correction.json
  locator: Derived audit or reading receipt; primary bytes and original acquisitions
    bound separately
  accessed_at: '2026-10-22T00:38:30.468985Z'
  support: supports
  summary: Original inspect receipt misstated 442 lines; append-only correction records
    the actual complete 457-line reading without altering original command, capture
    or target bytes.
  snapshot_sha256: 8fbb34a8f37a5fc77b2228bc774960e0fbb74ff244e3ee23cff29d97afb810fa
- evidence_id: reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-b12-qc-supplement-qualified.json
  locator: Actual B12-to-B13 qualification
  accessed_at: '2026-10-21T23:05:39.165510Z'
  support: supports
  summary: Original diagnostic times, failures, retries and skips remain explicit.
  snapshot_sha256: e1fa58cb626ef76e2b2066404078b9893b069a5b53a0cffbc3a184e68f0cd9f1
- evidence_id: reuse-postcheck
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-output-verification-agent/post-execution-verification.json
  locator: Independent actual-output verification
  accessed_at: '2026-10-21T23:07:53.187524Z'
  support: supports
  summary: Qualification verification, not new QC.
  snapshot_sha256: 42a5580991e7251963a9b83d0817facda019de29d9e13208e870c27e1c62ad7d
- evidence_id: local-init
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/batch013-local-initialization-receipt.json
  locator: Derived audit or reading receipt; primary bytes and original acquisitions
    bound separately
  accessed_at: '2026-10-21T23:09:00.804479Z'
  support: supports
  summary: Actual local initialization; publication remains separate.
  snapshot_sha256: cda5c0d3753e7a2a3ceb9ba723261fa79d4f760aad1713ff2d33b08def3577f7
- evidence_id: policy
  kind: authority
  reference: docs/GROUNDING_POLICY.md
  locator: Captured maintained authority
  accessed_at: '2026-10-22T00:41:42.229851Z'
  support: supports
  summary: Actual referents, allowed legacy molecular-function grounding and optional
    protein instances.
  snapshot_sha256: 891678c983c2283a47c81c47950b35753981e9339d105f3bbdda92a1f5ab7f42
- evidence_id: playbook
  kind: authority
  reference: docs/CURATION_PLAYBOOK.md
  locator: Captured maintained authority
  accessed_at: '2026-10-22T00:41:42.229851Z'
  support: supports
  summary: Source scope and attributable current acceptance.
  snapshot_sha256: 735e9b810471da9f7d8364e35ffe1e741edb3421480dac01727db6ea5aa65da9
- evidence_id: schema
  kind: authority
  reference: src/traitmech/schema/traitmech.yaml
  locator: Captured maintained authority
  accessed_at: '2026-10-22T00:41:42.229851Z'
  support: supports
  summary: Current facets and NONMECHANISTIC scope.
  snapshot_sha256: 46c47fc627b80ccbba1e8ab3fb6f2aee93bc2aef7aaf72fe9aadc3257f2c02dd
- evidence_id: predicate-mapping
  kind: authority
  reference: mappings/predicate_grounding.tsv
  locator: Captured maintained authority
  accessed_at: '2026-10-22T00:41:42.229851Z'
  support: supports
  summary: Shared future-empty-field mapping; populated predicate IDs are skipped.
  snapshot_sha256: 8e28c19e93aca3dc164a3befbe2612b289241de457c59f499e65936c03b7ce52
- evidence_id: node-mapping
  kind: authority
  reference: mappings/node_grounding.tsv
  locator: Captured maintained authority
  accessed_at: '2026-10-22T00:41:42.229851Z'
  support: supports
  summary: Reverse-gyrase functional grounding, distinct from a protein instance.
  snapshot_sha256: d7de9b3ab04960c4775a5bc295a945bd1a72d81467830459f4793e654f82b3d0
- evidence_id: local-v2
  kind: authority
  reference: proposals/metpo_traitmech_v2/metpo_proposal_properties_robot.tsv
  locator: Captured maintained authority
  accessed_at: '2026-10-22T00:41:42.229851Z'
  support: supports
  summary: Local selects-for broad endpoints, separate from imported RO roles.
  snapshot_sha256: 4ab5ca37ff8595210254b1099563b4425ecd737ed375dc5a932b44e2ad5c332e
- evidence_id: local-v8
  kind: authority
  reference: proposals/metpo_traitmech_v8/metpo_proposal_properties_robot.tsv
  locator: Captured maintained authority
  accessed_at: '2026-10-22T00:41:42.229851Z'
  support: supports
  summary: Local confers broad endpoints and trait range.
  snapshot_sha256: 5445e86e845e0a2638292cff4586bf3858b1341d37fecf2e86cefcdbc9a046cd
- evidence_id: identity
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-ground-agent/identity-assessment.json
  locator: Derived audit or reading receipt; primary bytes and original acquisitions
    bound separately
  accessed_at: '2026-10-22T00:41:42.165402Z'
  support: supports
  summary: Active high-bin identity and direct parent; inclusive endpoint qualification.
  snapshot_sha256: bccd6a5e0c380ee39c24e52fb062788d37a613f27d311e7254dcf714eba6f014
- evidence_id: nodes-edges
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-ground-agent/node-edge-grounding-ledger.json
  locator: Derived audit or reading receipt; primary bytes and original acquisitions
    bound separately
  accessed_at: '2026-10-22T00:41:42.225367Z'
  support: supports
  summary: All sixteen node and fourteen relation judgments, including contrary controls.
  snapshot_sha256: 7b6364e0e1c58b14a36315e076671e68cdf91aa0bd28845e9d45ef6da6a6e89b
- evidence_id: owners
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-ground-agent/owner-provenance-assessment.json
  locator: Derived audit or reading receipt; primary bytes and original acquisitions
    bound separately
  accessed_at: '2026-10-22T00:41:42.228904Z'
  support: supports
  summary: Exact current, conditional and sibling owner distinctions.
  snapshot_sha256: 03c96d42e94ecc6f8897a46ff4aefacee4bdde7e0375c568243180fa50aaa5e8
- evidence_id: owner-primary
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-ground-agent/owner-primary-reading.json
  locator: Derived audit or reading receipt; primary bytes and original acquisitions
    bound separately
  accessed_at: '2026-10-22T00:41:42.165785Z'
  support: supports
  summary: Whole reviewer/connector and selected repair/shared-grounder guards.
  snapshot_sha256: 86b6db901d53d5d865a5f898b3ba9aec5ce54af02ee22e263bc03de91cc07892
- evidence_id: writer-shape
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-ground-agent/writer-current-shape-check.json
  locator: Derived audit or reading receipt; primary bytes and original acquisitions
    bound separately
  accessed_at: '2026-10-22T00:41:42.169083Z'
  support: supports
  summary: Reviewer exact-after no-op and connector rejection after pruning; repair
    does not supply current RO roles.
  snapshot_sha256: d0028492e103edda36b2ead7a20ddcabf8597f86c7b93eba31689f6428c24ae3
- evidence_id: human-search
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-ground-agent/search-and-provenance.json
  locator: Derived audit or reading receipt; primary bytes and original acquisitions
    bound separately
  accessed_at: '2026-10-22T00:39:43.830390Z'
  support: supports
  summary: 182 ignored-inclusive matching paths, 68 actual target arrays, zero exact
    current target.
  snapshot_sha256: 721a264779c2de87b2687c0329df01d5ca2d36d0fb1dd75d7c2ca4c8e0d35e21
- evidence_id: histories
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-ground-agent/history-reading-provenance.json
  locator: Derived audit or reading receipt; primary bytes and original acquisitions
    bound separately
  accessed_at: '2026-10-22T00:41:42.228613Z'
  support: supports
  summary: Four current whole history reads plus ten unchanged qualified prior reads;
    fourteen current projections.
  snapshot_sha256: 264cce1b133163e70a5b8bf609b1c3ee935d3b3b8cb2177869c0a96f4e05c0dc
- evidence_id: discovery
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-ground-agent/discovery-disposition.json
  locator: Derived audit or reading receipt; primary bytes and original acquisitions
    bound separately
  accessed_at: '2026-10-22T00:41:42.225145Z'
  support: supports
  summary: All history leads captured; one uncaptured thermotaxis script is matching-line-only
    context.
  snapshot_sha256: a6940578959a0c87ee0789b6773cd66055c3a995ce2e7b3970fc68e3e999355c
- evidence_id: expression-original
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-ground-agent/expression-and-readiness.json
  locator: Derived audit or reading receipt; primary bytes and original acquisitions
    bound separately
  accessed_at: '2026-10-22T00:41:42.229503Z'
  support: supports
  summary: Retained original catalog/coverage receipt; scope-only query omission rationale
    is superseded by the separate supplement.
  snapshot_sha256: 273b86a5289465420633b8145f6f760061f1d925f435dbd353703a2c82edd2ff
- evidence_id: expression-supplement
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-ground-agent/expression-supplement.json
  locator: Derived audit or reading receipt; primary bytes and original acquisitions
    bound separately
  accessed_at: '2026-10-22T00:42:53.142774Z'
  support: supports
  summary: Covered benign source query is appropriate; current bounded adapter unavailability
    prevents execution, with catalog/source fallback and no membership result.
  snapshot_sha256: 182846e9b84cd2bd35a6057ebfc7f8a71f58778576a9cc90153d4169263b0b04
- evidence_id: expression-discovery
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-ground-agent/expression-runner-current-discovery.json
  locator: Derived audit or reading receipt; primary bytes and original acquisitions
    bound separately
  accessed_at: '2026-10-22T00:42:35.640883Z'
  support: supports
  summary: Actual current PATH/project/install search, bounded unavailable adapter
    result.
  snapshot_sha256: 1422318bbbd8c59f6dd807ab282ef1791c548be61b283d48a1e4572533b896e5
- evidence_id: local-authority
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-ground-agent/local-authority-reading.json
  locator: Derived audit or reading receipt; primary bytes and original acquisitions
    bound separately
  accessed_at: '2026-10-22T00:41:42.130347Z'
  support: supports
  summary: Exact local proposal, mapping, Biolink and schema/policy windows.
  snapshot_sha256: 2712482fc66760dda7d8ed1ed23708df7b85aab6cb4e277d4f4239b2d398cccc
- evidence_id: ground-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-ground-agent/reading-scope-receipt.json
  locator: Derived audit or reading receipt; primary bytes and original acquisitions
    bound separately
  accessed_at: '2026-10-22T00:41:42.230166Z'
  support: supports
  summary: Actual agent readings and honest prior-read reuse scope.
  snapshot_sha256: 76b09dcbd711ad62c08ef37b33f73f1afcd1db6876ee0efc1838e7578434f107
- evidence_id: ground-manifest
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-ground-agent/evidence-manifest.json
  locator: Derived audit or reading receipt; primary bytes and original acquisitions
    bound separately
  accessed_at: '2026-10-22T00:41:42.233211Z'
  support: supports
  summary: Twenty-nine unchanged frozen artifacts plus separately bound expression
    supplement.
  snapshot_sha256: ad1609da3d1a097b197f177d7785dd198c09fd1e324b8cb2d33a94e0314bff1c
- evidence_id: metpo-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/repo/data/raw/metpo.owl
  locator: Selected primary authority statements, read at the recorded time
  accessed_at: '2026-10-22T00:39:43.696678Z'
  support: supports
  summary: Active high class and direct parent; existential inclusive40 Cel versus
    approximate prose is qualified.
  snapshot_sha256: 8b6f8fe0510a698579e532658c8ace05da2550093365df9ca83feb0741778415
- evidence_id: metpo-primary-projection
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-ground-agent/metpo-authority.json
  locator: Derived audit or reading receipt; primary bytes and original acquisitions
    bound separately
  accessed_at: '2026-10-22T00:39:43.696678Z'
  support: supports
  summary: Exact source bytes and selected statement projection.
  snapshot_sha256: 4b7ecbb0104e07d78a0568ae2eb960d9a4ed660a4dbfa9f01ecbfb36323bb6eb
- evidence_id: go-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/go.db
  locator: Selected primary authority statements, read at the recorded time
  accessed_at: '2026-10-22T00:39:42.991895Z'
  support: supports
  summary: GO0160097 is reverse gyrase molecular function, not a biological process.
  snapshot_sha256: 018a7ef0a5bd1c0767abc3d71b413264a25be7579533daf5349f739cd9a122cd
- evidence_id: go-primary-projection
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-ground-agent/selected-go-primary-reading.json
  locator: Derived audit or reading receipt; primary bytes and original acquisitions
    bound separately
  accessed_at: '2026-10-22T00:39:42.991895Z'
  support: supports
  summary: Exact source bytes and selected statement projection.
  snapshot_sha256: 4e62068c5ad8fc4117c5b9e534403bf13f781ee6e0575a5574969cfaad3d276a
- evidence_id: ro-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/ro.db
  locator: Selected primary authority statements, read at the recorded time
  accessed_at: '2026-10-22T00:39:42.988471Z'
  support: supports
  summary: Actual inherited regulation process roles and material-to-process capable-of
    chain.
  snapshot_sha256: 849e616c29fecd0d4a6c6dee0dc0f6f117ace7167dbfa1e0f043dc84868f83cb
- evidence_id: ro-primary-projection
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-ground-agent/selected-ro-primary-reading.json
  locator: Derived audit or reading receipt; primary bytes and original acquisitions
    bound separately
  accessed_at: '2026-10-22T00:39:42.988471Z'
  support: supports
  summary: Exact source bytes and selected statement projection.
  snapshot_sha256: e2e54656f0ce0d2fe9a06683f0f6aa0a50ca8b2f58618f76240afe95ff299e00
- evidence_id: tolner-metadata
  kind: primary_source
  reference: DOI:10.1016/s0300-9629(97)00003-0
  locator: Indexed abstract and identifier/status fields
  accessed_at: '2026-10-21T09:29:01.331044Z'
  support: supports
  summary: Generic adaptation and literal spans; exact threshold and sufficiency remain
    unknown.
  snapshot_sha256: 56f69a7ce2e69822ef753fec5c43716583184e45fc1a2c0cae98aa9bdb841265
- evidence_id: vieille-metadata
  kind: primary_source
  reference: DOI:10.1128/MMBR.65.1.1-43.2001
  locator: Indexed abstract and identifier/status fields
  accessed_at: '2026-10-21T11:23:22.820553Z'
  support: supports
  summary: Enzyme thermostability context and literal phrase; no full-body interpretation.
  snapshot_sha256: 7fbda4bf0eea7b0c1641d88dc150329587687249fd800726e14b7f84a9670e0c
- evidence_id: vieille-error
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC99017/fullTextXML
  locator: Original failed body request and retained error bytes; not XML article
    content
  accessed_at: '2026-10-21T23:40:25.832769Z'
  support: context_only
  summary: Historical access limit, not current native-check failure or full-paper
    absence.
  snapshot_sha256: e0e941acc188eeea39928336d9947cc59e8719064066ceb596a11ed6a5c76c84
- evidence_id: grunberger-metadata
  kind: primary_source
  reference: DOI:10.1128/mbio.02174-23
  locator: Indexed identity/status and broad organism context
  accessed_at: '2026-10-21T11:41:58.823005Z'
  support: supports
  summary: Preprint link is not a retraction or correction.
  snapshot_sha256: b820f0062019e2484afc9c6a79c23c83924aefb9d301e9eae2ece60a66ed9674
- evidence_id: grunberger-primary
  kind: primary_source
  reference: DOI:10.1128/mbio.02174-23
  locator: Zero-based body paragraph1, existing introductory phrase only
  accessed_at: '2026-10-21T11:42:31.334593Z'
  support: supports
  summary: Hyperthermophile context does not set a universal quantitative optimum.
  snapshot_sha256: ae33c2f1c09cbe76d982f51f63a3a8d25fcb8774c177364e472df395561335fc
- evidence_id: takemata-metadata
  kind: primary_source
  reference: DOI:10.1264/jsme2.me23087
  locator: Indexed identity/status and abstract
  accessed_at: '2026-10-22T00:38:59.670863Z'
  support: supports
  summary: Identity and supplied activity wording; physiological conclusions remain
    source-qualified.
  snapshot_sha256: cb82777c9d646903003cb00cf17529b364de2d37957f374d81bf2e572f537b74
- evidence_id: baes-metadata
  kind: primary_source
  reference: DOI:10.1128/mbio.03593-22
  locator: Indexed identity/status
  accessed_at: '2026-10-22T00:38:59.695227Z'
  support: supports
  summary: Sulfolobales source identity; Preprint-in link is not correction/retraction.
  snapshot_sha256: 5b742bdec8fbe4a692d6dab3e3a417a15215793e7f497e57cd2b685d197db9b2
- evidence_id: canonical-metadata
  kind: primary_source
  reference: DOI:10.3389/fmicb.2023.1219779
  locator: Indexed identity/status and organism context
  accessed_at: '2026-10-22T00:38:59.802908Z'
  support: supports
  summary: Study identity; exact reported optimum is supported by the selected body
    separately.
  snapshot_sha256: d505a07f4ab49b59cc5bd5c06862102fa159751835969304a4c6fd08b81a2d95
- evidence_id: takemata-primary
  kind: primary_source
  reference: DOI:10.1264/jsme2.me23087
  locator: Abstract and zero-based body paragraphs2/4/6/10
  accessed_at: '2026-10-22T00:39:00.890308Z'
  support: supports
  summary: Supplied spans and generic attribution retain physiological debate, in-vitro
    observations and correlations; no universal-bin necessity or sufficiency.
  snapshot_sha256: 341f7792b825942ef02b465f443214dcbcc3843203ebb4fa11885f43bec422e2
- evidence_id: baes-primary
  kind: primary_source
  reference: DOI:10.1128/mbio.03593-22
  locator: Zero-based body paragraph1, selected introductory phrases
  accessed_at: '2026-10-22T00:39:01.720198Z'
  support: supports
  summary: Existing Sulfolobales context and literal snippets; no methods/results
    or intervention-efficacy audit.
  snapshot_sha256: 6caf9f39a39f589a840c350bd9f84a307656ace6b97d605ca7791ef06d588c9d
- evidence_id: canonical-primary
  kind: primary_source
  reference: DOI:10.3389/fmicb.2023.1219779
  locator: Section2.1, zero-based body paragraph3, first two sentences
  accessed_at: '2026-10-22T00:39:01.243225Z'
  support: supports
  summary: REY15A reported optimum-control76 degrees C is distinct from the66-degree
    comparison; no complete response curve claimed.
  snapshot_sha256: ff608de9d057699933e5c2c6263d113e4a275697caa75e0d04ad6b2923c46fb4
- evidence_id: taxonomy
  kind: authority
  reference: NCBITaxon:43080
  locator: Whole successful official species response
  accessed_at: '2026-10-22T00:40:16.469891Z'
  support: supports
  summary: Saccharolobus islandicus and former Sulfolobus islandicus name are positive.
    Species identity is distinct from the source strain and phenotype.
  snapshot_sha256: dcfce9197b2a21f404791d38e78ae1a4a3dc25f05cd6540ab3f30f4638bc1826
- evidence_id: taxonomy-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-ground-agent/taxonomy-identity.json
  locator: Derived audit or reading receipt; primary bytes and original acquisitions
    bound separately
  accessed_at: '2026-10-22T00:41:42.164999Z'
  support: supports
  summary: Successful primary XML and initial DNS-error bytes are kept separate.
  snapshot_sha256: f4c2c30860dd053c2d08c6aa0336324637f4c2aa206df852ff2f5f53950fd1ed
- evidence_id: sources
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-source-agent/source-assessment.json
  locator: Derived audit or reading receipt; primary bytes and original acquisitions
    bound separately
  accessed_at: '2026-10-22T00:42:13.711363Z'
  support: supports
  summary: Six works, no source finding, overall UNKNOWN for exact threshold/sufficient
    optimum claims.
  snapshot_sha256: d07c35389cc13ff20ddf5d789e9dc5358464fadbd1805f9518b87f27b0bfbd03
- evidence_id: source-identities
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-source-agent/source-identities-status.json
  locator: Derived audit or reading receipt; primary bytes and original acquisitions
    bound separately
  accessed_at: '2026-10-22T00:42:13.711363Z'
  support: supports
  summary: All six assigned identities and bounded publication-notice fields.
  snapshot_sha256: f78e07de2c4fcd578ad0a2df5cd6e0f9e05373fd68f34d142e8d74175c49bd14
- evidence_id: placements
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-source-agent/source-placement-ledger.json
  locator: Derived audit or reading receipt; primary bytes and original acquisitions
    bound separately
  accessed_at: '2026-10-22T00:42:13.711363Z'
  support: supports
  summary: All eighteen external placements and seventeen grounding fields accounted.
  snapshot_sha256: a098dff3e4d6b896859a9f4308075cba5dde8e117633b30cd699674539c7ceac
- evidence_id: snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-source-agent/snippet-ledger.json
  locator: Derived audit or reading receipt; primary bytes and original acquisitions
    bound separately
  accessed_at: '2026-10-22T00:42:13.711363Z'
  support: supports
  summary: All sixteen short supplied schema snippets literal on inspected primary
    surfaces.
  snapshot_sha256: 6e238e2101e3869223354f414e1ecdddc3a005a4645d0cfc9009b22cef6af58a
- evidence_id: notes
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-source-agent/source-note-ledger.json
  locator: Derived audit or reading receipt; primary bytes and original acquisitions
    bound separately
  accessed_at: '2026-10-22T00:42:13.711363Z'
  support: supports
  summary: All sixteen evidence notes with explicit physiological/assay scope.
  snapshot_sha256: 703325991986d81ef351fd0225520ff9e86344e71fe09d81ded18956e21561e0
- evidence_id: source-nodes-edges
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-source-agent/node-edge-source-ledger.json
  locator: Derived audit or reading receipt; primary bytes and original acquisitions
    bound separately
  accessed_at: '2026-10-22T00:42:13.711363Z'
  support: supports
  summary: All sixteen nodes and fourteen edges; generic attribution distinct from
    causal sufficiency.
  snapshot_sha256: a4959ea3c8f5009bfbda2f1d6f388f35bee6f6188fa6c105cb90009e01be725b
- evidence_id: source-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-source-agent/primary-reading-scope.json
  locator: Derived audit or reading receipt; primary bytes and original acquisitions
    bound separately
  accessed_at: '2026-10-22T00:42:13.711363Z'
  support: supports
  summary: Selected generic primary passages; no full-article scientific or excluded
    mechanism assessment.
  snapshot_sha256: 7c6b893407023f057bb600649410bccc378641e735ca083f60525c67c2665e76
- evidence_id: source-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-source-agent/source-access-limits.json
  locator: Derived audit or reading receipt; primary bytes and original acquisitions
    bound separately
  accessed_at: '2026-10-22T00:42:13.711363Z'
  support: supports
  summary: Abstract-only sources and historical body failure remain unknown, not refuted.
  snapshot_sha256: 9df175aec2a387193dc65583fa9b11251a75a8435af90fa0ad0b088da56735b7
- evidence_id: source-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-source-agent/source-reuse-receipt.json
  locator: Derived audit or reading receipt; primary bytes and original acquisitions
    bound separately
  accessed_at: '2026-10-22T00:39:11.114523Z'
  support: supports
  summary: Original request clocks, current copy clocks and current interpretation
    remain distinct.
  snapshot_sha256: aedadf01f320f0dbe8666bc926c862e17ee9fadb953ef1ca7bd5df91828e7815
- evidence_id: canonical
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-source-agent/canonical-assessment.json
  locator: Derived audit or reading receipt; primary bytes and original acquisitions
    bound separately
  accessed_at: '2026-10-22T00:42:13.711363Z'
  support: supports
  summary: Reported76-degree optimum-control is positive within stated source conditions;
    no exhaustive curve.
  snapshot_sha256: eff01a022a2a9df23e58101e8fc3e4f8140447b7237fe9c569b0228faa416d9f
- evidence_id: source-native
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-source-agent/native-check-context.json
  locator: Derived audit or reading receipt; primary bytes and original acquisitions
    bound separately
  accessed_at: '2026-10-22T00:42:13.711363Z'
  support: supports
  summary: Native six VERIFIED/ten inconclusive differs from sixteen manual literal
    confirmations.
  snapshot_sha256: 112893814de2da9229a2ec501c7c9aa870bea954910d928e93be85dbcee4f676
- evidence_id: source-manifest
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-source-agent/evidence-manifest.json
  locator: Derived audit or reading receipt; primary bytes and original acquisitions
    bound separately
  accessed_at: '2026-10-22T00:42:13.755892Z'
  support: supports
  summary: Thirty-six frozen source artifacts verified.
  snapshot_sha256: ea00f02dfebab39bb017cff4e27a4832754f5f97274c62fccb7077ed849f1230
- evidence_id: root-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-source-root/selected-primary-reading.json
  locator: Derived audit or reading receipt; primary bytes and original acquisitions
    bound separately
  accessed_at: '2026-10-22T00:41:08.068154Z'
  support: supports
  summary: Independent selected primary/authority/owner readings; three whole exact-target
    histories and fourteen projections, not fourteen root whole-body readings.
  snapshot_sha256: 11bc1fa4fe7ed2b091c4831bf38ac5e116341f077135931048bec00af540a152
- evidence_id: adjudication
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-high-root-adjudication.json
  locator: Final root adjudication
  accessed_at: '2026-10-22T00:46:29.117023Z'
  support: supports
  summary: Exact final findings, field anchors, owner qualifications and actions control
    serialization.
  snapshot_sha256: 60098061932168e706f05059ba9b57dfe52d6ccb45047387a192f00569373dce
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: active identity and hierarchy'
  outcome: supported
  target_ids:
  - METPO:1000447
  summary: Active METPO1000447 and direct parent1000304 match the high optimum concept.
    Raw inclusive40 restriction and approximate above40/related synonym are an explicit
    endpoint qualification, not a second confirmed defect.
  evidence_ids:
  - identity
  - metpo-primary
  - local-authority
  - record
- assessment_id: definition
  area: quantity
  topic: 'Native checklist: threshold and sufficient optimum claims'
  outcome: unknown
  target_ids:
  - METPO:1000447
  summary: Inspected Tolner/Vieille abstracts support generic adaptation and enzyme
    thermostability. Exact approximate40 calibration, exact Thermophile equivalence
    and sufficient thermostability-to-organism-optimum claims remain unknown; inaccessible
    body content is not refuted.
  evidence_ids:
  - sources
  - placements
  - notes
  - tolner-metadata
  - vieille-metadata
  - source-access
- assessment_id: canonical-example
  area: quantity
  topic: 'Native checklist: reported optimum'
  outcome: supported
  target_ids:
  - METPO:1000447
  summary: S.islandicus REY15A is explicitly reported at an optimal-control temperature
    of76 degrees C, separate from the66-degree comparator. This supports the current
    bin under stated study conditions without asserting a complete response curve.
    Official species identity is checked separately.
  evidence_ids:
  - canonical
  - canonical-primary
  - taxonomy
  - taxonomy-reading
  - root-reading
- assessment_id: source-support
  area: evidence
  topic: 'Native checklist: six works and eighteen placements'
  outcome: unknown
  target_ids:
  - METPO:1000447
  summary: Generic environmental archaeal attribution and all source identities are
    positive. Physiological debate, in-vitro DNA observations and correlations remain
    qualified; heat-shock response context and hyperthermophile introductions do not
    establish every organism optimum. Detailed dangerous-pathogen mechanisms and intervention
    efficacy remain UNASSESSED_SCOPE.
  evidence_ids:
  - sources
  - source-identities
  - placements
  - notes
  - source-reading
  - takemata-primary
  - baes-primary
  - grunberger-primary
- assessment_id: quotations
  area: evidence
  topic: 'Native checklist: all snippets and notes'
  outcome: supported
  target_ids:
  - METPO:1000447
  summary: All sixteen schema snippets are literal. The native abstract check verified
    six and left ten inconclusive; selected body inspection resolves literal occurrence
    without validating every note or causal interpretation. No inherited quoted-note
    finding is added.
  evidence_ids:
  - snippets
  - notes
  - source-native
  - source-reading
- assessment_id: nodes
  area: representation
  topic: 'Native checklist: all sixteen referents'
  outcome: concern
  target_ids:
  - METPO:1000447
  summary: Node3 thermostability/material-property wording conflicts with its process
    facet, grouped with edge9. Reverse gyrase has allowed GO molecular-function grounding.
    Node5 process/state, node14 quality/stabilization and node15 enrichment nuances
    remain qualifications; no forced additional retype.
  evidence_ids:
  - nodes-edges
  - source-nodes-edges
  - schema
  - go-primary
  - adjudication
  details: "{\n  \"grounding\": [\n    {\n      \"index\": 0,\n      \"node_id\":\
    \ \"temperature_optimum_high_trait\",\n      \"label\": \"temperature optimum\
    \ high\",\n      \"node_type\": \"TRAIT\",\n      \"grounding\": \"METPO:1000447\"\
    ,\n      \"outcome\": \"supported\",\n      \"assessment\": \"Active high-bin\
    \ identity; exact inclusive40 versus approximate above40 is a bounded endpoint\
    \ qualification.\"\n    },\n    {\n      \"index\": 1,\n      \"node_id\": \"\
    temperature_optimum\",\n      \"label\": \"temperature optimum\",\n      \"node_type\"\
    : \"TRAIT\",\n      \"grounding\": \"METPO:1000304\",\n      \"outcome\": \"supported\"\
    ,\n      \"assessment\": \"Active parent temperature-optimum trait.\"\n    },\n\
    \    {\n      \"index\": 2,\n      \"node_id\": \"hot_environment\",\n      \"\
    label\": \"hot environment\",\n      \"node_type\": \"ENVIRONMENTAL_FACTOR\",\n\
    \      \"grounding\": null,\n      \"outcome\": \"supported\",\n      \"assessment\"\
    : \"Ambient hot habitat condition; not assumed to be a process or change event\
    \ solely from ENVIRONMENTAL_FACTOR.\"\n    },\n    {\n      \"index\": 3,\n  \
    \    \"node_id\": \"thermophile_thermostability\",\n      \"label\": \"thermophile\
    \ protein thermostability\",\n      \"node_type\": \"BIOLOGICAL_PROCESS\",\n \
    \     \"grounding\": null,\n      \"outcome\": \"concern\",\n      \"assessment\"\
    : \"Label denotes protein thermostability and description denotes heat-stable\
    \ lipids/proteins, not an activity. BIOLOGICAL_PROCESS facet conflicts with actual\
    \ referent; coupled to edge9 role group, no separately counted facet finding or\
    \ automatic replacement type.\"\n    },\n    {\n      \"index\": 4,\n      \"\
    node_id\": \"reverse_gyrase\",\n      \"label\": \"reverse gyrase\",\n      \"\
    node_type\": \"GENE_OR_PROTEIN\",\n      \"grounding\": \"GO:0160097\",\n    \
    \  \"outcome\": \"supported\",\n      \"assessment\": \"Protein-class referent\
    \ grounded through allowed GO molecular-function facet. GO0160097 is reverse gyrase\
    \ activity, not BP.\"\n    },\n    {\n      \"index\": 5,\n      \"node_id\":\
    \ \"dna_positive_supercoiling\",\n      \"label\": \"DNA positive supercoiling\"\
    ,\n      \"node_type\": \"BIOLOGICAL_PROCESS\",\n      \"grounding\": null,\n\
    \      \"outcome\": \"unknown\",\n      \"assessment\": \"Label and process-quality\
    \ writer intend introduction of positive supercoils; description calls it a topological\
    \ state. Process-versus-state wording remains qualified, without forced extra\
    \ finding.\"\n    },\n    {\n      \"index\": 6,\n      \"node_id\": \"dna_melting_high_temperature\"\
    ,\n      \"label\": \"DNA melting at high temperature\",\n      \"node_type\"\
    : \"BIOLOGICAL_PROCESS\",\n      \"grounding\": null,\n      \"outcome\": \"supported\"\
    ,\n      \"assessment\": \"Explicit DNA strand-separation/denaturation process.\"\
    \n    },\n    {\n      \"index\": 7,\n      \"node_id\": \"nucleoid_associated_proteins\"\
    ,\n      \"label\": \"nucleoid-associated proteins\",\n      \"node_type\": \"\
    GENE_OR_PROTEIN\",\n      \"grounding\": null,\n      \"outcome\": \"supported\"\
    ,\n      \"assessment\": \"Explicit material protein group; REVIEWED_LABEL_ONLY\
    \ is allowed for this aggregate.\"\n    },\n    {\n      \"index\": 8,\n     \
    \ \"node_id\": \"genome_thermostability\",\n      \"label\": \"genome thermostability\"\
    ,\n      \"node_type\": \"QUALITY\",\n      \"grounding\": null,\n      \"outcome\"\
    : \"supported\",\n      \"assessment\": \"Explicit resistance-to-denaturation\
    \ quality.\"\n    },\n    {\n      \"index\": 9,\n      \"node_id\": \"small_heat_shock_proteins\"\
    ,\n      \"label\": \"small heat shock proteins\",\n      \"node_type\": \"GENE_OR_PROTEIN\"\
    ,\n      \"grounding\": null,\n      \"outcome\": \"supported\",\n      \"assessment\"\
    : \"Explicit material chaperone group; reviewed label-only is not an automatic\
    \ coverage defect.\"\n    },\n    {\n      \"index\": 10,\n      \"node_id\":\
    \ \"protein_aggregation_heat\",\n      \"label\": \"heat-induced protein aggregation\"\
    ,\n      \"node_type\": \"BIOLOGICAL_PROCESS\",\n      \"grounding\": null,\n\
    \      \"outcome\": \"supported\",\n      \"assessment\": \"Explicit aggregation\
    \ process.\"\n    },\n    {\n      \"index\": 11,\n      \"node_id\": \"thermosome\"\
    ,\n      \"label\": \"thermosome (group II chaperonin)\",\n      \"node_type\"\
    : \"GENE_OR_PROTEIN\",\n      \"grounding\": null,\n      \"outcome\": \"supported\"\
    ,\n      \"assessment\": \"Material group-II complex; aggregate label-only is\
    \ bounded and material executor is meaningful.\"\n    },\n    {\n      \"index\"\
    : 12,\n      \"node_id\": \"denatured_protein_refolding\",\n      \"label\": \"\
    refolding of denatured proteins\",\n      \"node_type\": \"BIOLOGICAL_PROCESS\"\
    ,\n      \"grounding\": null,\n      \"outcome\": \"supported\",\n      \"assessment\"\
    : \"Explicit refolding process.\"\n    },\n    {\n      \"index\": 13,\n     \
    \ \"node_id\": \"membrane_lipid_composition\",\n      \"label\": \"altered membrane\
    \ lipid composition\",\n      \"node_type\": \"BIOLOGICAL_PROCESS\",\n      \"\
    grounding\": null,\n      \"outcome\": \"supported\",\n      \"assessment\": \"\
    Despite composition label, description explicitly denotes lipid-remodeling process;\
    \ do not force a material type from label alone.\"\n    },\n    {\n      \"index\"\
    : 14,\n      \"node_id\": \"membrane_thermostability\",\n      \"label\": \"cytoplasmic\
    \ membrane thermostability\",\n      \"node_type\": \"QUALITY\",\n      \"grounding\"\
    : null,\n      \"outcome\": \"unknown\",\n      \"assessment\": \"Label/type denote\
    \ membrane thermostability quality while description uses stabilization language.\
    \ Retain nuance; edge8 process subject independently conflicts with material domain.\"\
    \n    },\n    {\n      \"index\": 15,\n      \"node_id\": \"aa_composition_thermostability\"\
    ,\n      \"label\": \"hydrophobic and charged amino acid enrichment\",\n     \
    \ \"node_type\": \"BIOLOGICAL_PROCESS\",\n      \"grounding\": null,\n      \"\
    outcome\": \"unknown\",\n      \"assessment\": \"Enrichment can mean compositional\
    \ change or resulting composition; no forced extra facet finding. Edge9 property\
    \ object is independently decisive.\"\n    }\n  ],\n  \"source\": [\n    {\n \
    \     \"index\": 0,\n      \"node_id\": \"temperature_optimum_high_trait\",\n\
    \      \"node_type\": \"TRAIT\",\n      \"outcome\": \"UNKNOWN_NUMERIC_CALIBRATION\"\
    ,\n      \"assessment\": \"Current >~40°C bin is explicit local scope; exact literature\
    \ threshold/qualitative Thermophile equivalence is unverified from selected Tolner\
    \ abstract.\"\n    },\n    {\n      \"index\": 1,\n      \"node_id\": \"temperature_optimum\"\
    ,\n      \"node_type\": \"TRAIT\",\n      \"outcome\": \"SUPPORTED_MEASUREMENT_CONCEPT\"\
    ,\n      \"assessment\": \"Optimum is a growth-temperature measurement; do not\
    \ substitute stress exposure, range, survival or enzyme activity optimum.\"\n\
    \    },\n    {\n      \"index\": 2,\n      \"node_id\": \"hot_environment\",\n\
    \      \"node_type\": \"ENVIRONMENTAL_FACTOR\",\n      \"outcome\": \"SUPPORTED_GENERIC_CONTEXT\"\
    ,\n      \"assessment\": \"High-temperature environments are generic context;\
    \ exposure above40°C does not alone prove an optimum above40°C.\"\n    },\n  \
    \  {\n      \"index\": 3,\n      \"node_id\": \"thermophile_thermostability\"\
    ,\n      \"node_type\": \"BIOLOGICAL_PROCESS\",\n      \"outcome\": \"SUPPORTED_CONTEXT_FACET_QUALIFIED\"\
    ,\n      \"assessment\": \"Sources support stability of proteins/lipids. Description\
    \ mixes material capacity/property with declared process facet; formal review\
    \ owns that distinction.\"\n    },\n    {\n      \"index\": 4,\n      \"node_id\"\
    : \"reverse_gyrase\",\n      \"node_type\": \"GENE_OR_PROTEIN\",\n      \"outcome\"\
    : \"SUPPORTED_SOURCE_ATTRIBUTION\",\n      \"assessment\": \"Reverse gyrase and\
    \ its supplied topological activity description are source-backed; no new protein\
    \ instance or universal optimum inference.\"\n    },\n    {\n      \"index\":\
    \ 5,\n      \"node_id\": \"dna_positive_supercoiling\",\n      \"node_type\":\
    \ \"BIOLOGICAL_PROCESS\",\n      \"outcome\": \"SUPPORTED_ACTIVITY_CONTEXT\",\n\
    \      \"assessment\": \"Positive-supercoiling activity is discussed; topological\
    \ state and physiological effect remain distinct and source-qualified.\"\n   \
    \ },\n    {\n      \"index\": 6,\n      \"node_id\": \"dna_melting_high_temperature\"\
    ,\n      \"node_type\": \"BIOLOGICAL_PROCESS\",\n      \"outcome\": \"SUPPORTED_PHYSICAL_CONTEXT\"\
    ,\n      \"assessment\": \"Thermal DNA strand separation is generic physical context;\
    \ no intervention protocol reconstructed.\"\n    },\n    {\n      \"index\": 7,\n\
    \      \"node_id\": \"nucleoid_associated_proteins\",\n      \"node_type\": \"\
    GENE_OR_PROTEIN\",\n      \"outcome\": \"SUPPORTED_WITH_ASSAY_QUALIFICATION\"\
    ,\n      \"assessment\": \"Aggregate NAP source context is in-vitro stabilization\
    \ plus archaeal correlation, not an exact component or universal causal optimum\
    \ claim.\"\n    },\n    {\n      \"index\": 8,\n      \"node_id\": \"genome_thermostability\"\
    ,\n      \"node_type\": \"QUALITY\",\n      \"outcome\": \"SUPPORTED_PHYSICAL_CONTEXT\"\
    ,\n      \"assessment\": \"DNA thermostability as resistance to thermal denaturation\
    \ is relevant; source does not measure a unique genome-wide optimum.\"\n    },\n\
    \    {\n      \"index\": 9,\n      \"node_id\": \"small_heat_shock_proteins\"\
    ,\n      \"node_type\": \"GENE_OR_PROTEIN\",\n      \"outcome\": \"SUPPORTED_ARCHAEAL_CONTEXT\"\
    ,\n      \"assessment\": \"Baes introductory small-HSP protein-quality attribution\
    \ is positive within Sulfolobales context.\"\n    },\n    {\n      \"index\":\
    \ 10,\n      \"node_id\": \"protein_aggregation_heat\",\n      \"node_type\":\
    \ \"BIOLOGICAL_PROCESS\",\n      \"outcome\": \"SUPPORTED_ARCHAEAL_CONTEXT\",\n\
    \      \"assessment\": \"Aggregation prevention is part of the supplied introductory\
    \ context, without operational efficacy assessment.\"\n    },\n    {\n      \"\
    index\": 11,\n      \"node_id\": \"thermosome\",\n      \"node_type\": \"GENE_OR_PROTEIN\"\
    ,\n      \"outcome\": \"SUPPORTED_ARCHAEAL_CONTEXT\",\n      \"assessment\": \"\
    Thermosome is described as a group-II chaperonin complex; no forced component-level\
    \ example.\"\n    },\n    {\n      \"index\": 12,\n      \"node_id\": \"denatured_protein_refolding\"\
    ,\n      \"node_type\": \"BIOLOGICAL_PROCESS\",\n      \"outcome\": \"SUPPORTED_ARCHAEAL_CONTEXT\"\
    ,\n      \"assessment\": \"ATP-dependent refolding attribution is explicit in\
    \ selected introduction.\"\n    },\n    {\n      \"index\": 13,\n      \"node_id\"\
    : \"membrane_lipid_composition\",\n      \"node_type\": \"BIOLOGICAL_PROCESS\"\
    ,\n      \"outcome\": \"SUPPORTED_RESPONSE_CONTEXT\",\n      \"assessment\": \"\
    Current description names remodeling process; the selected source describes altered\
    \ composition in heat-shock response rather than a universal optimum determinant.\"\
    \n    },\n    {\n      \"index\": 14,\n      \"node_id\": \"membrane_thermostability\"\
    ,\n      \"node_type\": \"QUALITY\",\n      \"outcome\": \"SUPPORTED_CONTEXT_WITH_LIMITS\"\
    ,\n      \"assessment\": \"Membrane stabilization is a contextual interpretation\
    \ of the selected response branch; exact physiological efficacy is not established\
    \ here.\"\n    },\n    {\n      \"index\": 15,\n      \"node_id\": \"aa_composition_thermostability\"\
    ,\n      \"node_type\": \"BIOLOGICAL_PROCESS\",\n      \"outcome\": \"SUPPORTED_GENERIC_CONTEXT\"\
    ,\n      \"assessment\": \"Enrichment is listed in hyperthermophile introduction;\
    \ no designed sequence change or improvement is proposed.\"\n    }\n  ]\n}"
- assessment_id: relations
  area: consistency
  topic: 'Native checklist: all fourteen relations'
  outcome: concern
  target_ids:
  - METPO:1000447
  summary: One imported-role group covers edges3/5/6/8/9 with the coupled node3 facet.
    Thermosome material executor to refolding process is a positive control. Edge4
    process interpretation remains qualified; broad local and Biolink associations
    receive no invented narrow RO constraints.
  evidence_ids:
  - nodes-edges
  - source-nodes-edges
  - ro-primary
  - go-primary
  - local-authority
  - adjudication
  details: "{\n  \"grounding\": [\n    {\n      \"index\": 0,\n      \"subject\":\
    \ \"hot_environment\",\n      \"predicate\": \"selects for\",\n      \"predicate_id\"\
    : \"METPO:2007401\",\n      \"object\": \"thermophile_thermostability\",\n   \
    \   \"outcome\": \"unknown\",\n      \"assessment\": \"Local selects-for broad\
    \ formal causal-node endpoints do not impose RO process constraints. Environmental\
    \ condition fits selection context; node3 adapted-material/property shorthand\
    \ is qualified.\"\n    },\n    {\n      \"index\": 1,\n      \"subject\": \"thermophile_thermostability\"\
    ,\n      \"predicate\": \"confers\",\n      \"predicate_id\": \"METPO:2007700\"\
    ,\n      \"object\": \"temperature_optimum_high_trait\",\n      \"outcome\": \"\
    supported\",\n      \"assessment\": \"Local confers broad endpoints admit current\
    \ generic subject and trait object; no invented imported role.\"\n    },\n   \
    \ {\n      \"index\": 2,\n      \"subject\": \"temperature_optimum_high_trait\"\
    ,\n      \"predicate\": \"is a\",\n      \"predicate_id\": \"rdfs:subClassOf\"\
    ,\n      \"object\": \"temperature_optimum\",\n      \"outcome\": \"supported\"\
    ,\n      \"assessment\": \"Actual high trait is a subclass of captured temperature-optimum\
    \ parent.\"\n    },\n    {\n      \"index\": 3,\n      \"subject\": \"reverse_gyrase\"\
    ,\n      \"predicate\": \"positively regulates\",\n      \"predicate_id\": \"\
    RO:0002213\",\n      \"object\": \"dna_positive_supercoiling\",\n      \"outcome\"\
    : \"concern\",\n      \"assessment\": \"RO2213 inherits process domain/range.\
    \ Current subject is a topoisomerase protein class; legacy MF grounding does not\
    \ silently retype it into the process needed by this regulatory relation.\"\n\
    \    },\n    {\n      \"index\": 4,\n      \"subject\": \"dna_positive_supercoiling\"\
    ,\n      \"predicate\": \"decreases\",\n      \"predicate_id\": \"RO:0002212\"\
    ,\n      \"object\": \"dna_melting_high_temperature\",\n      \"outcome\": \"\
    unknown\",\n      \"assessment\": \"Process-intended supercoiling and DNA-denaturation\
    \ object are formally compatible; topological-state wording remains qualified.\
    \ Ontology does not establish in-vivo efficacy.\"\n    },\n    {\n      \"index\"\
    : 5,\n      \"subject\": \"nucleoid_associated_proteins\",\n      \"predicate\"\
    : \"increases\",\n      \"predicate_id\": \"RO:0002213\",\n      \"object\": \"\
    genome_thermostability\",\n      \"outcome\": \"concern\",\n      \"assessment\"\
    : \"RO2213 process domain/range conflict with explicit material protein subject\
    \ and genome-resistance QUALITY object.\"\n    },\n    {\n      \"index\": 6,\n\
    \      \"subject\": \"small_heat_shock_proteins\",\n      \"predicate\": \"prevents\"\
    ,\n      \"predicate_id\": \"RO:0002212\",\n      \"object\": \"protein_aggregation_heat\"\
    ,\n      \"outcome\": \"concern\",\n      \"assessment\": \"RO2212 inherits process\
    \ domain; explicit small-HSP protein subject is material. Aggregation object is\
    \ a process, a positive range control.\"\n    },\n    {\n      \"index\": 7,\n\
    \      \"subject\": \"thermosome\",\n      \"predicate\": \"enables\",\n     \
    \ \"predicate_id\": \"RO:0002327\",\n      \"object\": \"denatured_protein_refolding\"\
    ,\n      \"outcome\": \"supported\",\n      \"assessment\": \"RO2327 material\
    \ executor to process fits thermosome/refolding current referents.\"\n    },\n\
    \    {\n      \"index\": 8,\n      \"subject\": \"membrane_lipid_composition\"\
    ,\n      \"predicate\": \"contributes to\",\n      \"predicate_id\": \"RO:0002326\"\
    ,\n      \"object\": \"membrane_thermostability\",\n      \"outcome\": \"concern\"\
    ,\n      \"assessment\": \"RO2326 material-to-process inherited roles conflict\
    \ with explicit lipid-remodeling process subject; membrane-quality object also\
    \ needs precise referent. Subject mismatch independently decisive.\"\n    },\n\
    \    {\n      \"index\": 9,\n      \"subject\": \"aa_composition_thermostability\"\
    ,\n      \"predicate\": \"increases\",\n      \"predicate_id\": \"RO:0002213\"\
    ,\n      \"object\": \"thermophile_thermostability\",\n      \"outcome\": \"concern\"\
    ,\n      \"assessment\": \"RO2213 process range conflicts with explicit protein-thermostability/material-stability\
    \ object. Node3 process label does not repair its property/material referent.\
    \ Enrichment process/result ambiguity does not remove object issue.\"\n    },\n\
    \    {\n      \"index\": 10,\n      \"subject\": \"dna_positive_supercoiling\"\
    ,\n      \"predicate\": \"associated with\",\n      \"predicate_id\": \"biolink:associated_with\"\
    ,\n      \"object\": \"genome_thermostability\",\n      \"outcome\": \"supported\"\
    ,\n      \"assessment\": \"Biolink associated-with has broad NamedThing roles;\
    \ no process/material exclusion inferred.\"\n    },\n    {\n      \"index\": 11,\n\
    \      \"subject\": \"genome_thermostability\",\n      \"predicate\": \"associated\
    \ with\",\n      \"predicate_id\": \"biolink:associated_with\",\n      \"object\"\
    : \"thermophile_thermostability\",\n      \"outcome\": \"supported\",\n      \"\
    assessment\": \"Broad Biolink association endpoints fit; biological strength remains\
    \ source-dependent.\"\n    },\n    {\n      \"index\": 12,\n      \"subject\"\
    : \"protein_aggregation_heat\",\n      \"predicate\": \"associated with\",\n \
    \     \"predicate_id\": \"biolink:associated_with\",\n      \"object\": \"denatured_protein_refolding\"\
    ,\n      \"outcome\": \"supported\",\n      \"assessment\": \"Broad association\
    \ between aggregation and refolding processes is not a role defect.\"\n    },\n\
    \    {\n      \"index\": 13,\n      \"subject\": \"denatured_protein_refolding\"\
    ,\n      \"predicate\": \"associated with\",\n      \"predicate_id\": \"biolink:associated_with\"\
    ,\n      \"object\": \"thermophile_thermostability\",\n      \"outcome\": \"supported\"\
    ,\n      \"assessment\": \"Broad association to thermostability context is not\
    \ assigned narrow RO constraints.\"\n    }\n  ],\n  \"source\": [\n    {\n   \
    \   \"index\": 0,\n      \"subject\": \"hot_environment\",\n      \"predicate\"\
    : \"selects for\",\n      \"object\": \"thermophile_thermostability\",\n     \
    \ \"outcome\": \"SUPPORTED_GENERIC_CONTEXT\",\n      \"assessment\": \"Tolner\
    \ supports high-temperature environmental adaptation context. The approximate40°C\
    \ optimum threshold and an evolutionary selection claim are not directly calibrated\
    \ in the inspected abstract.\",\n      \"locator\": \"tolner-metadata.json; opening\
    \ adaptation context\"\n    },\n    {\n      \"index\": 1,\n      \"subject\"\
    : \"thermophile_thermostability\",\n      \"predicate\": \"confers\",\n      \"\
    object\": \"temperature_optimum_high_trait\",\n      \"outcome\": \"UNKNOWN_EXACT_CAUSAL_SCOPE\"\
    ,\n      \"assessment\": \"Vieille/Zeikus describes enzyme thermostability in\
    \ hyperthermophiles, not a sufficient rule that thermostability yields every >40°C\
    \ growth optimum. Exact causal/bin calibration remains unknown because the primary\
    \ body is unavailable here.\",\n      \"locator\": \"vieille-metadata.json; abstract\
    \ first sentence and enzyme-versus-organism scope\"\n    },\n    {\n      \"index\"\
    : 2,\n      \"subject\": \"temperature_optimum_high_trait\",\n      \"predicate\"\
    : \"is a\",\n      \"object\": \"temperature_optimum\",\n      \"outcome\": \"\
    UNKNOWN_NUMERIC_CALIBRATION\",\n      \"assessment\": \"The local high-optimum-to-optimum\
    \ hierarchy is coherent but the cited abstract does not itself define the approximate40°C\
    \ threshold or its complete distribution. No unavailable-body absence claim.\"\
    ,\n      \"locator\": \"tolner-metadata.json; generic thermophile scope\"\n  \
    \  },\n    {\n      \"index\": 3,\n      \"subject\": \"reverse_gyrase\",\n  \
    \    \"predicate\": \"positively regulates\",\n      \"object\": \"dna_positive_supercoiling\"\
    ,\n      \"outcome\": \"SUPPORTED_SOURCE_ATTRIBUTION\",\n      \"assessment\"\
    : \"Takemata abstract explicitly describes reverse gyrase introducing positive\
    \ supercoils. Source context is particularly thermophiles above65°C; this is not\
    \ a universal defining mechanism for all >40°C optima. Formal protein/process\
    \ relation roles are separately reviewed.\",\n      \"locator\": \"takemata.xml;\
    \ abstract and bodyp2\"\n    },\n    {\n      \"index\": 4,\n      \"subject\"\
    : \"dna_positive_supercoiling\",\n      \"predicate\": \"decreases\",\n      \"\
    object\": \"dna_melting_high_temperature\",\n      \"outcome\": \"SUPPORTED_WITH_PHYSIOLOGICAL_QUALIFICATION\"\
    ,\n      \"assessment\": \"The exact thermal-denaturation phrase is attributed\
    \ to a widely accepted idea in paragraph4. Paragraph6 explicitly debates the physiological\
    \ importance of positive supercoiling, with cross-species variation. Preserve\
    \ the accepted biophysical explanation separately from established universal in-vivo\
    \ necessity or sufficiency.\",\n      \"locator\": \"takemata.xml; bodyp4 and\
    \ p6\"\n    },\n    {\n      \"index\": 5,\n      \"subject\": \"nucleoid_associated_proteins\"\
    ,\n      \"predicate\": \"increases\",\n      \"object\": \"genome_thermostability\"\
    ,\n      \"outcome\": \"SUPPORTED_WITH_ASSAY_QUALIFICATION\",\n      \"assessment\"\
    : \"The record note correctly identifies in-vitro DNA melting-temperature observations\
    \ and a correlation with archaeal growth temperature. These are not proof that\
    \ every NAP determines an organism optimum.\",\n      \"locator\": \"takemata.xml;\
    \ bodyp10\"\n    },\n    {\n      \"index\": 6,\n      \"subject\": \"small_heat_shock_proteins\"\
    ,\n      \"predicate\": \"prevents\",\n      \"object\": \"protein_aggregation_heat\"\
    ,\n      \"outcome\": \"SUPPORTED_ARCHAEAL_CONTEXT\",\n      \"assessment\": \"\
    The supplied protection phrase and note match the Sulfolobales introductory description.\
    \ No new detailed intervention efficacy or universal temperature-bin inference\
    \ is established.\",\n      \"locator\": \"baes.xml; bodyp1\"\n    },\n    {\n\
    \      \"index\": 7,\n      \"subject\": \"thermosome\",\n      \"predicate\"\
    : \"enables\",\n      \"object\": \"denatured_protein_refolding\",\n      \"outcome\"\
    : \"SUPPORTED_ARCHAEAL_CONTEXT\",\n      \"assessment\": \"The introductory description\
    \ explicitly attributes ATP-dependent refolding to the thermosome. This supports\
    \ the existing environmental archaeal protein context, not a specified organism-wide\
    \ optimum.\",\n      \"locator\": \"baes.xml; bodyp1\"\n    },\n    {\n      \"\
    index\": 8,\n      \"subject\": \"membrane_lipid_composition\",\n      \"predicate\"\
    : \"contributes to\",\n      \"object\": \"membrane_thermostability\",\n     \
    \ \"outcome\": \"SUPPORTED_RESPONSE_CONTEXT\",\n      \"assessment\": \"The source\
    \ reports altered membrane lipid composition during Sulfolobales heat shock. The\
    \ current note already frames this as a response branch rather than a single thermophily\
    \ determinant; specific causal contribution to stability remains contextual.\"\
    ,\n      \"locator\": \"baes.xml; bodyp1 opening sentence\"\n    },\n    {\n \
    \     \"index\": 9,\n      \"subject\": \"aa_composition_thermostability\",\n\
    \      \"predicate\": \"increases\",\n      \"object\": \"thermophile_thermostability\"\
    ,\n      \"outcome\": \"SUPPORTED_GENERIC_CONTEXT\",\n      \"assessment\": \"\
    The hyperthermophile introduction lists amino-acid enrichment among adaptation\
    \ mechanisms. This is generic context, not a direct measurement that enrichment\
    \ sets the >40°C bin for all organisms.\",\n      \"locator\": \"grunberger.xml;\
    \ bodyp1\"\n    },\n    {\n      \"index\": 10,\n      \"subject\": \"dna_positive_supercoiling\"\
    ,\n      \"predicate\": \"associated with\",\n      \"object\": \"genome_thermostability\"\
    ,\n      \"outcome\": \"SUPPORTED_QUALIFIED_ASSOCIATION\",\n      \"assessment\"\
    : \"Takemata presents reverse gyrase as considered to protect thermophile genomes,\
    \ with particular >65°C context; retain paragraph6 physiological qualification.\
    \ Association is not demonstrated whole-bin causality.\",\n      \"locator\":\
    \ \"takemata.xml; bodyp2 and p6\"\n    },\n    {\n      \"index\": 11,\n     \
    \ \"subject\": \"genome_thermostability\",\n      \"predicate\": \"associated\
    \ with\",\n      \"object\": \"thermophile_thermostability\",\n      \"outcome\"\
    : \"SUPPORTED_QUALIFIED_ASSOCIATION\",\n      \"assessment\": \"Takemata links\
    \ NAPs and other factors to DNA thermostability. The modest association wording\
    \ is contextual; in-vitro/correlation limits are retained.\",\n      \"locator\"\
    : \"takemata.xml; bodyp2 and p10\"\n    },\n    {\n      \"index\": 12,\n    \
    \  \"subject\": \"protein_aggregation_heat\",\n      \"predicate\": \"associated\
    \ with\",\n      \"object\": \"denatured_protein_refolding\",\n      \"outcome\"\
    : \"SUPPORTED_QUALIFIED_ASSOCIATION\",\n      \"assessment\": \"Baes introduction\
    \ places small-HSP/prefoldin protection and thermosome refolding in a shared protein-quality\
    \ description. No new mechanistic intervention or direct optimum effect is asserted\
    \ here.\",\n      \"locator\": \"baes.xml; bodyp1\"\n    },\n    {\n      \"index\"\
    : 13,\n      \"subject\": \"denatured_protein_refolding\",\n      \"predicate\"\
    : \"associated with\",\n      \"object\": \"thermophile_thermostability\",\n \
    \     \"outcome\": \"SUPPORTED_QUALIFIED_ASSOCIATION\",\n      \"assessment\"\
    : \"Thermosome composition/substrate specificity is described in the selected\
    \ introduction. The connector remains protein-quality context, not proof of a\
    \ quantitative optimal temperature.\",\n      \"locator\": \"baes.xml; bodyp1\"\
    \n    }\n  ]\n}"
- assessment_id: scope-completeness
  area: scope
  topic: 'Native checklist: quantitative overview and optional proteins'
  outcome: supported
  target_ids:
  - METPO:1000447
  summary: Two components are explicitly retained after corrective pruning. Four protein
    classes and three reviewed label-only classes with zero instances are permitted
    in this NONMECHANISTIC quantitative overview; no token protein or forced connector
    is requested.
  evidence_ids:
  - record
  - policy
  - histories
  - writer-shape
  - expression-supplement
- assessment_id: expression
  area: evidence
  topic: 'Native checklist: bounded catalog and unavailable adapter'
  outcome: unknown
  target_ids:
  - METPO:1000447
  summary: The retained catalog has source S.acidocaldarius/modulome coverage, but
    no exact canonical S.islandicus/REY15A match. Fresh bounded discovery establishes
    adapter unavailability for the appropriate generic source queries. Catalog/primary
    fallback supports context only; no unexecuted query result, membership or cross-species
    transfer is claimed.
  evidence_ids:
  - expression-original
  - expression-supplement
  - expression-discovery
  - baes-primary
  - source-reading
- assessment_id: recurrence
  area: consistency
  topic: 'Native checklist: exact owners and replay boundaries'
  outcome: supported
  target_ids:
  - METPO:1000447
  summary: The current reviewer exact-after guard is a no-op; its source constants
    own current assertions. The connector retains disputed source preimages but current
    replay rejects after corrective pruning. Repair uses filtered ADDED_EDGES, not
    current RO-role payloads. Shared grounders skip populated IDs; node3 facet has
    record-only ownership.
  evidence_ids:
  - owners
  - owner-primary
  - writer-shape
  - predicate-mapping
  - discovery
  - root-reading
- assessment_id: human
  area: provenance
  topic: 'Native checklist: attributable current acceptance'
  outcome: concern
  target_ids:
  - METPO:1000447
  summary: Twenty embedded AI events plus a seed and the ignored-inclusive182-path/68-array
    search do not establish current human acceptance. Four whole history files were
    read now and ten prior whole readings qualified by identical bytes; private or
    remote acceptance remains unknown.
  evidence_ids:
  - human-search
  - histories
  - owners
  - playbook
  - root-reading
- assessment_id: readiness
  area: consistency
  topic: 'Native checklist: checks, snapshots and chronology'
  outcome: supported
  target_ids:
  - METPO:1000447
  summary: All85 inputs and36/29 frozen audit artifacts match, with the expression
    supplement and original line-count correction bound separately. Focused native
    checks passed; common B13 reuse retains original diagnostics, optional failures/retries
    and skips. Acquisition, copy and reading times remain distinct.
  evidence_ids:
  - record
  - reuse
  - reuse-postcheck
  - local-init
  - source-reuse
  - source-native
  - ground-manifest
  - source-manifest
  - inspect-reading-correction
  - expression-supplement
findings:
- finding_id: imported-process-roles
  issue_key: temperature-optimum-high-imported-process-roles
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Imported relation roles conflict with current material and property referents
  description: One connected representation issue affects five edges and the coupled
    thermostability facet. RO:0002211 requires process subjects and objects; RO:0002212
    and RO:0002213 inherit those roles. Edge3 explicitly names a reverse-gyrase protein
    class, edge5 a NAP material subject and genome-resistance quality object, edge6
    a small-HSP material subject, and edge9 a thermostability/property object despite
    node3 being declared BIOLOGICAL_PROCESS. Edge8 uses RO:0002326, whose material-to-process
    roles are inherited through RO:0002216, RO:0002500 and RO:0002595; its explicit
    lipid-remodeling process subject independently conflicts. The allowed GO molecular-function
    grounding does not silently retype the named protein. Node3 label/description
    names thermostability and heat-stable material rather than an activity; that facet
    is counted once with edge9. Enrichment process/result and stabilization/property
    ambiguities remain qualified. These are formal referent/role findings, separate
    from physiological efficacy.
  target_ids:
  - METPO:1000447
  field_paths:
  - causal_graphs[0].nodes[3].node_type
  - causal_graphs[0].edges[3].predicate_id
  - causal_graphs[0].edges[5].predicate_id
  - causal_graphs[0].edges[6].predicate_id
  - causal_graphs[0].edges[8].predicate_id
  - causal_graphs[0].edges[9].predicate_id
  evidence_ids:
  - nodes-edges
  - ro-primary
  - go-primary
  - owners
  - writer-shape
  - schema
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_optimum_high.yaml
    role: Exact current assertion or qualified conditional recurrence; preserve replay
      guards and corrective pruning.
  - repository: CultureBotAI/TraitMech
    path: scripts/review_temperature_optimum_high_graph_183.py
    role: Exact current assertion or qualified conditional recurrence; preserve replay
      guards and corrective pruning.
  - repository: CultureBotAI/TraitMech
    path: scripts/connect_temperature_optimum_high_graph_183.py
    role: Exact current assertion or qualified conditional recurrence; preserve replay
      guards and corrective pruning.
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Exact current assertion or qualified conditional recurrence; preserve replay
      guards and corrective pruning.
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Exact current assertion or qualified conditional recurrence; preserve replay
      guards and corrective pruning.
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: human-acceptance-link
  issue_key: temperature-optimum-high-human-acceptance-link
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Reviewed status lacks locally attributable acceptance
  description: Current REVIEWED status lacks attributable human acceptance of present
    assertions in inspected local evidence. The ignored- and hidden-inclusive search,
    excluding .git and .venv, found182 matching paths and68 actual review target arrays
    with no exact target. Twenty-one embedded events comprise twenty AI events and
    one seed; the three exact-target repository histories have AI actors. Private
    or remote acceptance remains unknown.
  target_ids:
  - METPO:1000447
  field_paths:
  - mapping_status
  - curation_history
  evidence_ids:
  - human-search
  - histories
  - owners
  - playbook
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_optimum_high.yaml
    role: Exact current assertion or qualified conditional recurrence; preserve replay
      guards and corrective pruning.
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
actions:
- action_id: resolve-imported-process-roles
  description: In separately authorized curation, reconcile actual material, process
    and quality referents with inherited predicate roles, including node3 thermostability.
    Update reviewer source assertions and connector preimage expectations together
    while preserving exact guards and corrective pruning. Current reviewer exact-after
    checks no-op; connector replay rejects its pruned current shape before mutation.
    Its SOURCE_CONNECTOR_EDGES are guarded historical preimages, not an unconditional
    overwrite. Repair_pr664 uses filtered ADDED_EDGES and does not own the disputed
    current RO-role payloads. Shared grounding skips populated IDs, so rerunning it
    alone is not a fix; node3 facet has record-only ownership within this group.
  finding_ids:
  - imported-process-roles
  target_ids:
  - METPO:1000447
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_optimum_high.yaml
    role: Exact current assertion or qualified conditional recurrence; preserve replay
      guards and corrective pruning.
  - repository: CultureBotAI/TraitMech
    path: scripts/review_temperature_optimum_high_graph_183.py
    role: Exact current assertion or qualified conditional recurrence; preserve replay
      guards and corrective pruning.
  - repository: CultureBotAI/TraitMech
    path: scripts/connect_temperature_optimum_high_graph_183.py
    role: Exact current assertion or qualified conditional recurrence; preserve replay
      guards and corrective pruning.
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Exact current assertion or qualified conditional recurrence; preserve replay
      guards and corrective pruning.
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Exact current assertion or qualified conditional recurrence; preserve replay
      guards and corrective pruning.
  acceptance_checks:
  - Show compatible actual referents and inherited predicate roles without inventing
    process identities, numerical calibration or mechanisms.
  - Preserve legacy allowed GO molecular-function grounding, NONMECHANISTIC scope,
    two components and three reviewed label-only classes; no required protein instance
    or forced connector.
  - Retain all sixteen literal-source positives, canonical reported optimum and source
    uncertainty. Validate strict record/schema, relevant graph/predicate audits, QC
    and required history/product gates.
- action_id: resolve-human-acceptance-link
  description: Link attributable human acceptance of current assertions or reconcile
    REVIEWED through the native status workflow in separately authorized curation.
    Preserve existing AI actors and history.
  finding_ids:
  - human-acceptance-link
  target_ids:
  - METPO:1000447
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_optimum_high.yaml
    role: Exact current assertion or qualified conditional recurrence; preserve replay
      guards and corrective pruning.
  acceptance_checks:
  - Human reviewer and accepted assertion scope are attributable, or status accurately
    reflects available evidence.
  - Per-record and repository history validates and AI assistance remains explicit.
limitations:
- Overall sources UNKNOWN for exact approximately40°C category calibration, exact
  Thermophile synonym equivalence, and sufficient thermostability-to-whole-organism-optimum
  claims. Missing body is not evidence of falsehood.
- Tolner and Vieille/Zeikus support inspected abstract context only; Vieille retained
  fullTextXML attempt is HTTP500 error bytes, not primary body. No duplicate attempt
  or full-paper absence claim.
- Takemata accepted thermal-denaturation idea is distinguished from the same review’s
  debate over in-vivo physiological importance; greater-than65°C specificity is context,
  not a universal40°C definition.
- NAP melting-temperature evidence is in vitro and archaeal abundance association
  is correlational. Do not convert either to universal necessity/sufficiency for the
  bin.
- Baes context is Sulfolobales heat-shock response; Grünberger introductory statement
  concerns hyperthermophilic archaea. These generic statements do not establish every
  organism-specific optimal temperature.
- Canonical is REY15A reported optimal-control76°C at pH3.4 versus66°C comparator,
  not a complete response curve. Incidental displayed methods, dataset-access text
  and other conditions were not adopted or used.
- Detailed dangerous-pathogen stress/fitness/defense/ROS/AMR/intervention mechanisms
  and efficacy remain UNASSESSED_SCOPE. No source follow-up proposes physiological
  enhancement.
- Metadata notice fields show two Preprint-in links, not retractions/corrections.
  Publication status is bounded to inspected primary metadata and selected body frontmatter.
- 'Source-organism catalog relevance is bounded to actually named contexts: canonical
  S.islandicus REY15A, Baes S.acidocaldarius/Sulfolobales, Grünberger P.furiosus,
  generic Takemata Bacteria/Archaea. No exact strain/module/efficacy inference from
  species-level coverage.'
- Inclusive40 numeric restriction differs from approximate above40/related >40 wording;
  bounded upstream endpoint nuance, no independent finding.
- Node5 process/state wording and edge4 causal interpretation remain qualified; wrong
  process wording in historical GO rationale does not invalidate actual MF protein
  grounding.
- Node14 stabilization/quality and node15 enrichment process/result ambiguity are
  qualified; firm role findings have independent endpoints.
- Detailed dangerous-pathogen mechanisms UNASSESSED_SCOPE; generic source physiological
  sufficiency and exact bin causal calibration require separate source review.
- One uncaptured thermotaxis script is matching-line context only; no unbounded owner
  absence claim.
- Catalog source-organism coverage does not establish exact canonical dataset or intervention/module
  evidence.
- Private/remote human acceptance remains unknown.
- 'The current expression supplement supersedes the earlier scope-only omission rationale:
  an appropriate generic query for catalog-covered benign S.acidocaldarius was not
  executed because the adapter was unavailable within the fresh bounded search. Catalog
  and selected primary fallback do not establish module membership or canonical strain
  coverage.'
- Official JStage releaseJune6,2024 and February8,2025 license-display PDF correction
  were inspected. Indexed first-publicationJanuary1,2024 is an index field, not asserted
  as exact release. The license correction is not a biological correction; publication-notice
  inspection is not exhaustive.
- Root read three exact-target histories whole and fourteen compact actor/target/read-mode
  projections; agent read four current whole histories and qualified ten unchanged
  prior whole readings.
- Original acquisitions, current copies and current readings are distinct. Browser
  tool-call bounds do not establish cache origin-fetch times.
- Native snippets six VERIFIED and ten NOT_IN_ABSTRACT are distinct from all sixteen
  manually located literal spans. Literal occurrence does not establish the adjacent
  exact-bin causal interpretation.
- Current adapter-unavailable expression supplement supersedes only the earlier scope-based
  omission rationale; frozen ground manifest remains unchanged.
- Original source acquisitions, current copies and selected readings remain distinct;
  sixteen literal matches do not establish universal optimum causation.
- Qualified B12/common diagnostics are not fresh B13 QC or publication; retained optional
  failures/retries and123 no-adapter skips remain explicit.
notes:
- Whole457-line target and85 captured inputs; six sources/eighteen placements/seventeen
  grounding fields/sixteen literal snippets and sixteen evidence notes.
- Ground history scope is four current whole bodies plus ten qualified prior whole
  readings; root read three exact-target histories whole and fourteen projections.
- Original inspect receipt442-line typo remains immutable and is corrected by the
  bound457-line addendum.
- Root owns any eventual one-time serialization, actual-output review, native validation
  and save; this preparation did not execute or import the serializer.
tags:
- record-review
- temperature-optimum-high
- environment
- needs-curation
```
