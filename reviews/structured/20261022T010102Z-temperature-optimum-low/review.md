# Whole-record review of temperature optimum low

- Review: 20261022T010102Z-temperature-optimum-low
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-22T00:49:43.981927Z
- Finished UTC: 2026-10-22T01:01:02Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Temperature optimum low needs three substantive corrections: imported process-role predicates, the inherited exact Psychrophile synonym scope, and one canonical citation. Human acceptance also needs attribution. Active bin identity and all four literal snippets are supported; the other canonical example and exact physiological calibration remain unknown.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: Tenth record in the initialized local batch 013 queue. Whole 283-line target and 100 captured inputs verified; local review does not assert remote publication.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8eee04a8c65609fbaff6df7c54597dcaf1b9d282.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| METPO:1000442 | data/traits/environment/temperature_optimum_low.yaml | maintained | temperature optimum low |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full-corpus graph audit | passed | True | METPO:1000442 | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| Full-corpus snippet audit | passed | True | METPO:1000442 | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| Full-corpus pathway links | passed | True | METPO:1000442 | 19 links checked against the pinned PathwayMech snapshot. |
| Full-corpus history integrity | passed | True | METPO:1000442 | 1277 history records checked, zero invalid links at the 8eee source base; integrity does not establish science or human acceptance. |
| Initial full-product validation | failed | False | METPO:1000442 | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation with isolated local cache | failed | False | METPO:1000442 | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation after isolated-cache download | passed | True | METPO:1000442 | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| Focused native validation | passed | True | METPO:1000442 | Native record validation passed; scientific interpretation is assessed separately. |
| Focused strict validation | passed | True | METPO:1000442 | The actual validate-strict command passed. |
| Focused network snippet check | passed | True | METPO:1000442 | Two of four snippets were VERIFIED and two were NOT_IN_ABSTRACT in the native abstract check. Manual primary inspection finds all four literal; native inconclusive results are not body-absence evidence. |
| Qualified batch-twelve QC | passed | True | METPO:1000442 | Actual prior QC qualified against B13 bytes; this is not a fresh B13 QC execution or publication. |
| Protein-instance metadata applicability | not_applicable | False | METPO:1000442 | Two reviewed label-only protein classes and no instances in a quantitative NONMECHANISTIC graph; no compulsory accession or token instance. |
| Structured source-organism expression query availability | unavailable | False | METPO:1000442 | An appropriate generic B.subtilis source query was not executed because fresh bounded discovery found the maintained adapter unavailable. Catalog and selected primary fallback do not supply membership results. |

## Scientific And Domain Assessments

### Native checklist: active class and direct parent

identity: supported. Targets: METPO:1000442.

Active METPO:1000442 and parent METPO:1000304 agree with the numeric low-bin identity. Raw exact aliases are faithfully inherited documentary facts; scientific equivalence is assessed separately.

### Native checklist: qualitative alias and numerical bin

scope: concern. Targets: METPO:1000442.

The assigned review includes a Psychrophile with a reported optimum of 2 degrees C, outside 10–22 degrees C. This supports the index 0 exactness concern without invalidating active identity. Psychrotolerant equivalence and exact cutoff calibration remain unknown.

### Native checklist: measurement and exact threshold

quantity: unknown. Targets: METPO:1000442.

Best-growth ambient temperature is distinct from exposure, survival or low-temperature growth. The 10–22 interval is explicit in the local identity, but inspected generic adaptation sources do not calibrate that precise bin or establish sufficient whole-organism optima.

### Native checklist: two exact taxon/source/optimum claims

quantity: concern. Targets: METPO:1000442.

Both species identities are positive. P.fragi remains unknown because the assigned AMTT body is unavailable. The assigned complete Ramon article does not identify P.sivasensis or W-6; the current low-temperature-growth note does not supply the required best-growth temperature. This is a citation-support gap, not biological impossibility.

### Native checklist: six works and all placements

evidence: unknown. Targets: METPO:1000442.

All assigned identities are verified. Selected membrane physics and yeast PUFA context do not establish every taxon or exact optimum. AMTT body-dependent statements remain unknown; detailed pathogen cold-survival, fitness, ROS-defense, AMR and intervention efficacy remain UNASSESSED_SCOPE.

### Native checklist: four schema snippets and evidence notes

evidence: supported. Targets: METPO:1000442.

All four snippets are literal. Native abstract checks verify two and leave two inconclusive; retained author-repository PDF-derived text supplies the remaining literal matches. Literal occurrence does not validate adjacent causal or numerical claims.

### Native checklist: all fourteen current referents

representation: supported. Targets: METPO:1000442.

Current temperature and fluidity referents are qualities or conditions, while adaptation and named PUFA biosynthesis retain process/pathway meanings. Osmolyte role versus material bearer is a qualified close mapping. ROS-level wording remains qualified; no extra facet or wrong-CURIE finding is inferred.

{
  "grounding": [
    {
      "index": 0,
      "node_id": "temperature_optimum_low_trait",
      "label": "temperature optimum low",
      "node_type": "TRAIT",
      "grounding": "METPO:1000442",
      "outcome": "supported",
      "assessment": "Active exact temperature-optimum-low bin; raw synonyms do not themselves prove scientific equivalence."
    },
    {
      "index": 1,
      "node_id": "temperature_optimum",
      "label": "temperature optimum",
      "node_type": "TRAIT",
      "grounding": "METPO:1000304",
      "outcome": "supported",
      "assessment": "Active direct temperature-optimum parent."
    },
    {
      "index": 2,
      "node_id": "cool_environment",
      "label": "cool environment",
      "node_type": "ENVIRONMENTAL_FACTOR",
      "grounding": null,
      "outcome": "supported",
      "assessment": "Ambient cool condition, not automatically a process/event from enum."
    },
    {
      "index": 3,
      "node_id": "psychrotolerant_adaptation",
      "label": "psychrotolerant adaptation",
      "node_type": "BIOLOGICAL_PROCESS",
      "grounding": null,
      "outcome": "supported",
      "assessment": "Description denotes a generic adaptation process; exact physiological and numeric-bin sufficiency remains source-dependent."
    },
    {
      "index": 4,
      "node_id": "low_temperature",
      "label": "low temperature",
      "node_type": "ENVIRONMENTAL_FACTOR",
      "grounding": "PATO:0001306",
      "outcome": "supported",
      "assessment": "Relative low-temperature quality/condition under close PATO mapping. Its current description does not denote a temperature-decrease event; no independent enum/facet finding."
    },
    {
      "index": 5,
      "node_id": "membrane_fluidity",
      "label": "membrane fluidity",
      "node_type": "QUALITY",
      "grounding": "METPO:1007505",
      "outcome": "supported",
      "assessment": "Explicit membrane-fluidity physical quality; local v3 and current QUALITY mapping agree."
    },
    {
      "index": 6,
      "node_id": "membrane_unsaturation",
      "label": "fatty-acyl unsaturation",
      "node_type": "QUALITY",
      "grounding": null,
      "outcome": "supported",
      "assessment": "Degree of fatty-acyl unsaturation is explicitly a quality, not biosynthesis activity."
    },
    {
      "index": 7,
      "node_id": "cold_shock_proteins",
      "label": "cold shock proteins",
      "node_type": "GENE_OR_PROTEIN",
      "grounding": null,
      "outcome": "supported",
      "assessment": "Material cold-shock protein family. Reviewed label-only class is permitted; no fabricated instance or accession required."
    },
    {
      "index": 8,
      "node_id": "compatible_solutes",
      "label": "compatible solutes",
      "node_type": "CHEMICAL",
      "grounding": "CHEBI:25728",
      "outcome": "qualified",
      "assessment": "CHEBI25728 is an osmolyte biological role, while current node denotes solute bearers. Maintained closeMatch supports a functional grouping with explicit role/bearer qualification; not exact material identity and no separately confirmed replacement finding."
    },
    {
      "index": 9,
      "node_id": "protein_membrane_stabilization",
      "label": "protein and membrane stabilization",
      "node_type": "BIOLOGICAL_PROCESS",
      "grounding": null,
      "outcome": "supported",
      "assessment": "Stabilization and freezing-point-depression description denotes processes; detailed efficacy unassessed."
    },
    {
      "index": 10,
      "node_id": "ice_binding_proteins",
      "label": "ice-binding/antifreeze proteins",
      "node_type": "GENE_OR_PROTEIN",
      "grounding": null,
      "outcome": "supported",
      "assessment": "Material ice-binding protein class; reviewed label-only is not an automatic completeness defect."
    },
    {
      "index": 11,
      "node_id": "ice_crystal_growth",
      "label": "ice crystal growth",
      "node_type": "BIOLOGICAL_PROCESS",
      "grounding": null,
      "outcome": "supported",
      "assessment": "Ice-crystal growth/recrystallization process is explicit."
    },
    {
      "index": 12,
      "node_id": "oxidative_stress",
      "label": "oxidative stress",
      "node_type": "BIOLOGICAL_PROCESS",
      "grounding": null,
      "outcome": "qualified",
      "assessment": "Label/type indicate oxidative-stress process while description emphasizes elevated ROS. Process versus resulting ROS-level wording remains bounded; the low-temperature quality subject independently establishes edge8 role mismatch. Detailed ROS biology UNASSESSED_SCOPE."
    },
    {
      "index": 13,
      "node_id": "pufa_biosynthesis",
      "label": "PUFA biosynthesis",
      "node_type": "PATHWAY",
      "grounding": null,
      "outcome": "supported",
      "assessment": "Named polyunsaturated-fatty-acid biosynthetic route is compatible with maintained pathway-like mechanism policy and exact shared node-ID migration decision."
    }
  ],
  "source": [
    {
      "index": 0,
      "node_id": "temperature_optimum_low_trait",
      "node_type": "TRAIT",
      "outcome": "UNKNOWN_NUMERIC_CALIBRATION",
      "assessment": "Current10–22 optimum is an explicit local bin; sources do not supply exact calibration."
    },
    {
      "index": 1,
      "node_id": "temperature_optimum",
      "node_type": "TRAIT",
      "outcome": "SUPPORTED_MEASUREMENT_CONCEPT",
      "assessment": "Growth optimum is distinct from temperature range, exposure or survival."
    },
    {
      "index": 2,
      "node_id": "cool_environment",
      "node_type": "ENVIRONMENTAL_FACTOR",
      "outcome": "SUPPORTED_GENERIC_CONTEXT",
      "assessment": "Habitat temperature is environmental context, not measured organism optimum."
    },
    {
      "index": 3,
      "node_id": "psychrotolerant_adaptation",
      "node_type": "BIOLOGICAL_PROCESS",
      "outcome": "UNKNOWN_CAUSAL_SCOPE",
      "assessment": "Generic membrane/protein adaptation is source context, not sufficient proof of a precise optimum."
    },
    {
      "index": 4,
      "node_id": "low_temperature",
      "node_type": "ENVIRONMENTAL_FACTOR",
      "outcome": "SUPPORTED_GENERIC_PHYSICAL_CONTEXT",
      "assessment": "Cool ambient temperature is contextual; formal PATO referent assessed separately."
    },
    {
      "index": 5,
      "node_id": "membrane_fluidity",
      "node_type": "QUALITY",
      "outcome": "SUPPORTED_GENERIC_PHYSICAL_CONTEXT",
      "assessment": "Membrane-fluidity physical quality is supported by selected Spectrum introduction."
    },
    {
      "index": 6,
      "node_id": "membrane_unsaturation",
      "node_type": "QUALITY",
      "outcome": "SUPPORTED_GENERIC_PHYSICAL_CONTEXT",
      "assessment": "Degree of unsaturation is composition/property context; process roles separately assessed."
    },
    {
      "index": 7,
      "node_id": "cold_shock_proteins",
      "node_type": "GENE_OR_PROTEIN",
      "outcome": "UNASSESSED_SCOPE",
      "assessment": "AMTT identity positive, body inaccessible; detailed cold-response/fitness assessment excluded."
    },
    {
      "index": 8,
      "node_id": "compatible_solutes",
      "node_type": "CHEMICAL",
      "outcome": "UNKNOWN_NEAREST_SOURCE",
      "assessment": "Existing solute list not verified from assigned accessible abstract; no body-absence inference."
    },
    {
      "index": 9,
      "node_id": "protein_membrane_stabilization",
      "node_type": "BIOLOGICAL_PROCESS",
      "outcome": "UNKNOWN_NEAREST_SOURCE",
      "assessment": "Existing stabilization/freezing-point explanation not verified against assigned body."
    },
    {
      "index": 10,
      "node_id": "ice_binding_proteins",
      "node_type": "GENE_OR_PROTEIN",
      "outcome": "UNKNOWN_NEAREST_SOURCE",
      "assessment": "Existing ice-binding protein attribution not verified against assigned body; no compulsory example."
    },
    {
      "index": 11,
      "node_id": "ice_crystal_growth",
      "node_type": "BIOLOGICAL_PROCESS",
      "outcome": "SUPPORTED_GENERIC_PHYSICAL_CONTEXT",
      "assessment": "Ice growth is physical context; source-specific inhibition remains unknown."
    },
    {
      "index": 12,
      "node_id": "oxidative_stress",
      "node_type": "BIOLOGICAL_PROCESS",
      "outcome": "UNASSESSED_SCOPE",
      "assessment": "Detailed oxidative-stress/ROS-defense branch is not scientifically adjudicated."
    },
    {
      "index": 13,
      "node_id": "pufa_biosynthesis",
      "node_type": "PATHWAY",
      "outcome": "SUPPORTED_GENERIC_CONTEXT",
      "assessment": "Named PUFA pathway has generic yeast membrane context; no new intervention or universal optimum claim."
    }
  ]
}

### Native checklist: all ten current relations

consistency: concern. Targets: METPO:1000442.

The RO group is limited to edges 3, 7 and 8: explicit quality or material subjects conflict with inherited process roles, with quality objects additionally relevant at edge 3. Local confers, subclass and five lexical relations receive no invented imported constraints. Source efficacy remains separate.

{
  "grounding": [
    {
      "index": 0,
      "subject": "cool_environment",
      "predicate": "engages",
      "predicate_id": null,
      "object": "psychrotolerant_adaptation",
      "outcome": "unknown",
      "assessment": "Ungrounded lexical engages has no imported domain/range. Generic environmental-to-adaptation assertion requires source support."
    },
    {
      "index": 1,
      "subject": "psychrotolerant_adaptation",
      "predicate": "confers",
      "predicate_id": "METPO:2007700",
      "object": "temperature_optimum_low_trait",
      "outcome": "supported",
      "assessment": "Local confers broad causal-node endpoints and trait-object prose fit current adaptation process/trait; exact-bin causal calibration remains separate."
    },
    {
      "index": 2,
      "subject": "temperature_optimum_low_trait",
      "predicate": "is a",
      "predicate_id": "rdfs:subClassOf",
      "object": "temperature_optimum",
      "outcome": "supported",
      "assessment": "Current bin is a subclass of its explicit active temperature-optimum parent."
    },
    {
      "index": 3,
      "subject": "membrane_unsaturation",
      "predicate": "increases",
      "predicate_id": "RO:0002213",
      "object": "membrane_fluidity",
      "outcome": "concern",
      "assessment": "RO2213 inherits RO2211 process domain/range. Both current unsaturation and membrane-fluidity referents are explicit qualities, so the grounded assertion conflicts with inherited roles."
    },
    {
      "index": 4,
      "subject": "low_temperature",
      "predicate": "induces",
      "predicate_id": null,
      "object": "cold_shock_proteins",
      "outcome": "unknown",
      "assessment": "Lexical induces has no imported RO domain/range; no enum-only or invented predicate constraint. Biological efficacy unassessed."
    },
    {
      "index": 5,
      "subject": "low_temperature",
      "predicate": "promotes accumulation of",
      "predicate_id": null,
      "object": "compatible_solutes",
      "outcome": "unknown",
      "assessment": "Lexical promotes accumulation of has no imported RO constraints. Detailed accumulation/fitness efficacy is unassessed."
    },
    {
      "index": 6,
      "subject": "compatible_solutes",
      "predicate": "stabilizes",
      "predicate_id": null,
      "object": "protein_membrane_stabilization",
      "outcome": "unknown",
      "assessment": "Lexical stabilizes is not RO2326. Material-to-process wording is not assigned imported contributes-to constraints; detailed biology unassessed."
    },
    {
      "index": 7,
      "subject": "ice_binding_proteins",
      "predicate": "inhibits",
      "predicate_id": "RO:0002212",
      "object": "ice_crystal_growth",
      "outcome": "concern",
      "assessment": "RO2212 inherits process domain. Current ice-binding protein subject is material; ice-crystal-growth process object is a positive range control."
    },
    {
      "index": 8,
      "subject": "low_temperature",
      "predicate": "increases",
      "predicate_id": "RO:0002213",
      "object": "oxidative_stress",
      "outcome": "concern",
      "assessment": "RO2213 inherits process domain; current PATO-grounded low-temperature condition is a quality, not a decrease event. ROS object wording remains qualified and is not needed to establish the subject mismatch."
    },
    {
      "index": 9,
      "subject": "pufa_biosynthesis",
      "predicate": "maintains",
      "predicate_id": null,
      "object": "membrane_fluidity",
      "outcome": "unknown",
      "assessment": "Lexical maintains has no imported process-range constraint. Named biosynthetic pathway and fluidity-quality referents are not automatically inconsistent without a grounded predicate."
    }
  ],
  "source": [
    {
      "index": 0,
      "subject": "cool_environment",
      "predicate": "engages",
      "object": "psychrotolerant_adaptation",
      "outcome": "SUPPORTED_GENERIC_CONTEXT_UNKNOWN_BIN",
      "assessment": "D’Amico supplied decreased-fluidity phrase supports a generic cold physical challenge. It does not itself establish a10–22°C optimum or all adaptation programs.",
      "locator": "definition-metadata.json abstract; definition-author-raw.txt introduction"
    },
    {
      "index": 1,
      "subject": "psychrotolerant_adaptation",
      "predicate": "confers",
      "object": "temperature_optimum_low_trait",
      "outcome": "UNKNOWN_NUMERIC_CAUSAL_SCOPE",
      "assessment": "Mendoza explicitly supports greater unsaturation as temperature decreases. The claim that adaptation yields a10–22°C organism optimum is not established by the inspected abstract.",
      "locator": "mendoza-metadata.json abstract and retained publisher abstract export"
    },
    {
      "index": 2,
      "subject": "temperature_optimum_low_trait",
      "predicate": "is a",
      "object": "temperature_optimum",
      "outcome": "UNKNOWN_NUMERIC_CALIBRATION",
      "assessment": "Parent-child measurement hierarchy is documentary; freezing-point growth language does not calibrate an optimum10–22°C interval. Growth, optimum and tolerance remain distinct.",
      "locator": "definition-author-raw.txt introduction"
    },
    {
      "index": 3,
      "subject": "membrane_unsaturation",
      "predicate": "increases",
      "object": "membrane_fluidity",
      "outcome": "SUPPORTED_GENERIC_PHYSICAL_CONTEXT",
      "assessment": "Selected Spectrum introduction describes temperature/composition dependence of membrane fluidity and B.subtilis adaptation context. Broad transfer to every taxon and exact optimum is not established; no intervention efficacy is audited.",
      "locator": "spectrum.xml zero-based bodyp1 and firsttwo sentences bodyp2"
    },
    {
      "index": 4,
      "subject": "low_temperature",
      "predicate": "induces",
      "object": "cold_shock_proteins",
      "outcome": "UNASSESSED_SCOPE",
      "assessment": "AMTT identity is verified but body unavailable. Existing CSP induction/threshold note is not verified from accessible metadata; detailed cold-survival/fitness mechanism assessment is excluded.",
      "locator": "arrhenius-crossref.json identity/abstract; historical403 responses"
    },
    {
      "index": 5,
      "subject": "low_temperature",
      "predicate": "promotes accumulation of",
      "object": "compatible_solutes",
      "outcome": "UNKNOWN_NEAREST_SOURCE",
      "assessment": "AMTT abstract lacks the specified compatible-solute list and accumulation attribution; body unavailable. No falsity or paperwide absence inferred.",
      "locator": "arrhenius-crossref.json abstract"
    },
    {
      "index": 6,
      "subject": "compatible_solutes",
      "predicate": "stabilizes",
      "object": "protein_membrane_stabilization",
      "outcome": "UNKNOWN_NEAREST_SOURCE",
      "assessment": "Generic physical stabilization/freezing-point attribution cannot be verified against unavailable assigned AMTT body. No enhanced survival or intervention inference.",
      "locator": "arrhenius-crossref.json abstract"
    },
    {
      "index": 7,
      "subject": "ice_binding_proteins",
      "predicate": "inhibits",
      "object": "ice_crystal_growth",
      "outcome": "UNKNOWN_NEAREST_SOURCE",
      "assessment": "Assigned AMTT body unavailable; exact existing ice-binding explanation remains unverified. Formal protein/process roles are separately reviewed.",
      "locator": "arrhenius-crossref.json abstract"
    },
    {
      "index": 8,
      "subject": "low_temperature",
      "predicate": "increases",
      "object": "oxidative_stress",
      "outcome": "UNASSESSED_SCOPE",
      "assessment": "Assigned source identity verified; detailed oxidative-stress/ROS-defense/fitness branch is not adjudicated, and body is unavailable.",
      "locator": "arrhenius-crossref.json identity"
    },
    {
      "index": 9,
      "subject": "pufa_biosynthesis",
      "predicate": "maintains",
      "object": "membrane_fluidity",
      "outcome": "SUPPORTED_GENERIC_CONTEXT",
      "assessment": "Genes selected paragraph14 firstthree sentences directly describes PUFA-content changes and membrane fluidity at low temperature. Study cohort is psychrophilic yeasts; no universal bacterial or exact10–22 optimum transfer, and detailed gene/fitness comparisons are not adopted.",
      "locator": "genes.xml zero-based .//body//p[14], firstthree sentences"
    }
  ]
}

### Native checklist: quantitative graph and optional protein instances

scope: supported. Targets: METPO:1000442.

Four components and two reviewed label-only protein classes with no instances are permitted in this NONMECHANISTIC quantitative overview. No forced connector, protein example or mechanism completion is requested.

### Native checklist: bounded catalog and unavailable query adapter

evidence: unknown. Targets: METPO:1000442.

Neither canonical species has an exact retained catalog match; other Pseudomonas datasets are not substitutes. B.subtilis source coverage is positive, but the appropriate generic query was not executed because the runner is unavailable within the searched roots. Primary fallback gives context only.

### Native checklist: current owners and conditional writers

consistency: supported. Targets: METPO:1000442.

Populated RO IDs belong to the current record; shared mappings can recur on empty fields while grounders skip current IDs. Seeder normally skips existing records, the release migration excludes this target, and the release finalizer writes reports only. Canonical backfill lacks a current exact plan entry. Sibling scripts and matching-line leads are qualified context.

### Native checklist: attributable current acceptance

provenance: concern. Targets: METPO:1000442.

Nine embedded AI events plus a seed and the ignored-inclusive search of 169 matching paths and 67 review target arrays do not establish current human acceptance. Four histories were read whole now and 14 prior whole readings were qualified by unchanged bytes; private or remote acceptance remains unknown.

### Native checklist: native checks, snapshots and chronology

consistency: supported. Targets: METPO:1000442.

All 100 captured inputs and 41 source plus 31 ground artifacts match. Focused native checks passed; qualified common diagnostics retain original executions, optional failures, retries and skips. Acquisition, extraction, copy and reading times remain separate.

## Findings

### imported-process-roles: Imported regulation predicates conflict with current material and quality referents

major / open / confirmed; issue key: temperature-optimum-low-imported-process-roles.

Three edges conflict with inherited RO process roles. RO:0002212 and RO:0002213 inherit RO:0002211 process domain and range. Edge 3 relates explicit unsaturation and membrane-fluidity qualities; edge 7 has a material ice-binding protein subject, although its ice-growth process object is compatible; edge 8 has an explicitly low-temperature condition/quality subject, not a temperature-change event. The ENVIRONMENTAL_FACTOR enum alone is not the reason for that finding. ROS process-versus-level wording remains qualified and is not needed to establish the subject mismatch. Five lexical predicates have no imported formal roles and are not included.

### psychrophile-exact-synonym-scope: Exact Psychrophile alias exceeds the numerical optimum bin

major / open / confirmed; issue key: temperature-optimum-low-psychrophile-exact-synonym-scope.

Psychrophile is declared an exact synonym of the 10–22 °C optimum bin. The assigned D’Amico review explicitly uses psychrophiles broadly and immediately includes Moritella profunda with maximal growth at 2 °C, outside that bin. This concrete source usage contradicts exact equivalence. The active METPO identifier, numeric restriction and faithful import of the upstream exact alias remain positive; the issue is inherited synonym scope, not a wrong identifier. Psychrotolerant exactness remains unresolved and is not counted as another finding.

### canonical-source-attribution: Assigned source does not establish the second canonical optimum claim

major / open / confirmed; issue key: temperature-optimum-low-canonical-source-attribution.

The assigned Ramón review does not identify Pseudomonas sivasensis, sivasen variants or W-6/W6 in the retained complete parsed text. The current note also describes low-temperature growth without a reported 10–22 °C optimum. That citation does not establish the current exemplar-to-bin assertion. Official species identity is positive and is preserved; this is a bounded citation/measurement-support defect, not evidence that the organism lacks the phenotype. The inaccessible AMTT body for P. fragi remains UNKNOWN and does not receive this finding.

### human-acceptance-link: Reviewed status lacks locally attributable acceptance

minor / open / confirmed; issue key: temperature-optimum-low-human-acceptance-link.

Current REVIEWED status lacks attributable human acceptance of present assertions in the inspected local evidence. The ignored- and hidden-inclusive search, excluding .git and .venv, found 169 matching paths and 67 actual review target arrays with no exact target. Ten embedded events comprise nine AI events and one seed; the 18 captured history projections contain no exact-target history establishing acceptance. Private or remote acceptance remains unknown.

## Recommended Actions And Acceptance Checks

### resolve-imported-process-roles

In separately authorized curation, reconcile the three grounded predicates with their actual material, condition and quality referents. Retain correctly described fluidity and unsaturation qualities. Review wildcard increases/inhibits mapping recurrence together with record assertions; the shared grounder skips current populated IDs, so rerunning it alone is not a fix. Sibling graph writers and process-quality/homeoviscous normalizers are not current sources of these assertions.

- Demonstrate compatible inherited domain/range with actual referents without inventing mechanisms or assigning RO rules to lexical predicates.
- Retain NONMECHANISTIC scope, four components and two reviewed label-only protein classes; do not require token protein instances or connectors.
- Run focused strict validation, relevant graph/predicate audits, full QC and required curation history/product gates.

### resolve-psychrophile-exact-synonym-scope

Reconcile the inherited Psychrophile synonym scope with the upstream METPO term and document the local curation decision through the maintained ontology-source workflow. Preserve the active identifier, numeric-bin identity and upstream provenance. The vendored OWL path is evidence of upstream ownership, not an instruction to silently edit the locked snapshot. Fresh seeding copies exact scope but skips existing files unless forced; do not use forced reseeding as a repair. The three-alkaline-trait release migration excludes this target and the release finalizer writes review TSVs only.

- The synonym relationship reflects the broader source usage, or a documented narrower sense is independently supported.
- Track the upstream disposition and any curated local exception so future imports preserve the accepted scope; keep Psychrotolerant uncertainty separate.
- Verify identifier/snapshot integrity and native strict, history and QC gates after separately authorized curation.

### resolve-canonical-source-attribution

Resolve the exact primary citation and strain/organism attribution for the existing P. sivasensis example, and require a reported optimum within the bin rather than cold growth alone. If adequate evidence cannot be established, record an explicit evidence-gap disposition instead of retaining an unsupported canonical assertion. Keep source taxonomy and existing provenance; do not infer phenotype absence or automatically substitute another organism.

- The cited primary text identifies the example and supports its best-growth temperature in the defined bin, with any strain/assay limits explicit.
- Preserve the separate UNKNOWN disposition for P. fragi until its own assigned source can be adequately inspected.
- Validate canonical-reference fields, curation history and native strict/QC gates.

### resolve-human-acceptance-link

Link attributable human acceptance of current assertions or reconcile REVIEWED through the native status workflow in separately authorized curation. Preserve existing AI actors and history.

- Accepted assertion scope and human reviewer are attributable, or status reflects the available evidence.
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
| check-temperature-optimum-low-validate | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-validate.log; Executed 2026-10-22T00:50:07.333126+00:00 through 2026-10-22T00:50:07.952678+00:00; metadata temperature-optimum-low-validate.json | context_only | Native record validation passed; scientific interpretation is assessed separately. |
| check-temperature-optimum-low-strict | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-strict.log; Executed 2026-10-22T00:50:07.333891+00:00 through 2026-10-22T00:50:08.347569+00:00; metadata temperature-optimum-low-strict.json | context_only | The actual validate-strict command passed. |
| check-temperature-optimum-low-snippets-network | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-snippets-network.log; Executed 2026-10-22T00:50:12.466666+00:00 through 2026-10-22T00:50:15.779381+00:00; metadata temperature-optimum-low-snippets-network.json | context_only | Two of four snippets were VERIFIED and two were NOT_IN_ABSTRACT in the native abstract check. Manual primary inspection finds all four literal; native inconclusive results are not body-absence evidence. |
| check-batch012-qc | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/batch012-qc.log; Executed 2026-10-21T23:02:31.440808+00:00 through 2026-10-21T23:04:01.628423+00:00; metadata batch012-qc.json | context_only | Actual prior QC qualified against B13 bytes; this is not a fresh B13 QC execution or publication. |
| record | data/traits/environment/temperature_optimum_low.yaml; Whole current record | supports | Fourteen nodes, ten edges, ten embedded events, two canonical examples, two reviewed label-only protein classes and zero instances. |
| reuse | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-b12-qc-supplement-qualified.json; Actual B12-to-B13 diagnostic qualification | supports | Original diagnostic times, failures, retries and skips remain explicit. |
| reuse-postcheck | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-output-verification-agent/post-execution-verification.json; Derived audit or reading receipt; original primary bytes and acquisition clocks bound separately | supports | Independent qualification output verification, not new QC. |
| local-init | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/batch013-local-initialization-receipt.json; Derived audit or reading receipt; original primary bytes and acquisition clocks bound separately | supports | Actual local initialization; publication remains separate. |
| policy | docs/GROUNDING_POLICY.md; Captured maintained authority | supports | Protein family/function grounding and optional protein instances. |
| playbook | docs/CURATION_PLAYBOOK.md; Captured maintained authority | supports | Source scope and attributable acceptance. |
| schema | src/traitmech/schema/traitmech.yaml; Captured maintained authority | supports | Current facets and NONMECHANISTIC scope. |
| predicate-mapping | mappings/predicate_grounding.tsv; Captured maintained authority | supports | Mappings can populate empty IDs; populated assertions are skipped. |
| node-mapping | mappings/node_grounding.tsv; Captured maintained authority | supports | Current label/type keys and qualified functional mappings. |
| local-v3 | proposals/metpo_traitmech_v3/metpo_proposal_classes_robot.tsv; Captured maintained authority | supports | Local membrane-fluidity quality. |
| local-v8 | proposals/metpo_traitmech_v8/metpo_proposal_properties_robot.tsv; Captured maintained authority | supports | Local confers broad endpoints and trait range. |
| identity | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-ground-agent/identity-assessment.json; Derived audit or reading receipt; original primary bytes and acquisition clocks bound separately | supports | Active bin and direct parent; documentary synonym provenance is distinct from scientific equivalence. |
| nodes-edges | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-ground-agent/node-edge-grounding-ledger.json; Derived audit or reading receipt; original primary bytes and acquisition clocks bound separately | supports | All 14 node and 10 relation judgments, including contrary controls. |
| owners | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-ground-agent/owner-provenance-assessment.json; Derived audit or reading receipt; original primary bytes and acquisition clocks bound separately | supports | Current record, conditional shared writers and sibling contexts distinguished. |
| owner-primary | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-ground-agent/owner-primary-reading.json; Derived audit or reading receipt; original primary bytes and acquisition clocks bound separately | supports | Actual maintained writer and migration decision windows. |
| alias-owner | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-ground-agent/alias-source-and-owner-qualification.json; Derived audit or reading receipt; original primary bytes and acquisition clocks bound separately | supports | Seeder copies upstream aliases for new records but normally skips existing ones; release migration excludes this target and finalizer writes reports only. |
| human-search | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-ground-agent/search-and-provenance.json; Derived audit or reading receipt; original primary bytes and acquisition clocks bound separately | supports | 169 ignored-inclusive matching paths, 67 actual review target arrays, zero exact current target. |
| histories | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-ground-agent/history-reading-provenance.json; Derived audit or reading receipt; original primary bytes and acquisition clocks bound separately | supports | Four current whole history reads plus 14 unchanged qualified prior whole reads; 18 current projections. |
| discovery | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-ground-agent/discovery-disposition.json; Derived audit or reading receipt; original primary bytes and acquisition clocks bound separately | supports | Eight uncaptured script leads and one sibling history remain matching-line context only. |
| expression | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-ground-agent/expression-and-readiness.json; Derived audit or reading receipt; original primary bytes and acquisition clocks bound separately | supports | Covered benign source context has an unavailable adapter; catalog and primary fallback do not establish module membership. |
| expression-discovery | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-ground-agent/expression-runner-current-discovery.json; Derived audit or reading receipt; original primary bytes and acquisition clocks bound separately | supports | Fresh bounded PATH/project/install-root discovery; no global absence claim. |
| local-authority | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-ground-agent/local-authority-reading.json; Derived audit or reading receipt; original primary bytes and acquisition clocks bound separately | supports | Exact current proposal, mapping and schema windows. |
| chebi-role | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-ground-agent/chebi-role-supplement.json; Derived audit or reading receipt; original primary bytes and acquisition clocks bound separately | supports | Osmolyte role and material bearer distinguished without a forced replacement. |
| ground-reading | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-ground-agent/reading-scope-receipt.json; Derived audit or reading receipt; original primary bytes and acquisition clocks bound separately | supports | Actual current readings and honest prior-read reuse scope. |
| ground-manifest | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-ground-agent/evidence-manifest.json; Derived audit or reading receipt; original primary bytes and acquisition clocks bound separately | supports | All 31 frozen ground artifacts verified. |
| metpo-primary | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/repo/data/raw/metpo.owl; Selected primary statements at the recorded reading time | supports | Active exact class and parent, inclusive 10–22 Cel restriction and upstream alias scope. |
| metpo-primary-projection | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-ground-agent/metpo-authority.json; Derived audit or reading receipt; original primary bytes and acquisition clocks bound separately | supports | Exact primary bytes and selected statement projection. |
| pato-primary | /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/pato.db; Selected primary statements at the recorded reading time | supports | Low temperature denotes a quality or condition, not a temperature-decrease event. |
| pato-primary-projection | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-ground-agent/selected-pato-primary-reading.json; Derived audit or reading receipt; original primary bytes and acquisition clocks bound separately | supports | Exact primary bytes and selected statement projection. |
| chebi-primary | /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/chebi.db; Selected primary statements at the recorded reading time | supports | Osmolyte role definition used under a qualified close functional mapping. |
| chebi-primary-projection | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-ground-agent/selected-chebi-primary-reading.json; Derived audit or reading receipt; original primary bytes and acquisition clocks bound separately | supports | Exact primary bytes and selected statement projection. |
| ro-primary | /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/ro.db; Selected primary statements at the recorded reading time | supports | Regulation predicates inherit process subject and object roles. |
| ro-primary-projection | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-ground-agent/selected-ro-primary-reading.json; Derived audit or reading receipt; original primary bytes and acquisition clocks bound separately | supports | Exact primary bytes and selected statement projection. |
| definition-metadata | DOI:10.1038/sj.embor.7400662; Indexed identity/status and generic abstract | supports | Generic cold classification and supplied decreased-fluidity phrase. |
| definition-primary | DOI:10.1038/sj.embor.7400662; Author-repository PDF introduction; derived newline-based lines 23–42 | supports | Broad Psychrophile category includes a reported optimum of 2 degrees C outside this bin; no organism substitution or intervention proposed. |
| mendoza-metadata | DOI:10.1146/annurev-micro-091313-103612; Indexed identity/status and abstract | supports | Literal unsaturation phrase and generic attribution; exact optimum sufficiency remains unknown. |
| mendoza-publisher | DOI:10.1146/annurev-micro-091313-103612; Retained actual browser abstract export, not raw HTML | supports | Original tool-call bounds are preserved; origin cache-fetch time remains unknown. |
| cold-metadata | DOI:10.1007/s42770-023-01057-4; Indexed identity/status and abstract | supports | Assigned review identity is separate from exact species and optimum support. |
| cold-primary | DOI:10.1007/s42770-023-01057-4; Selected paragraph 10 classification plus mechanical whole-text canonical-name search | supports | No P.sivasensis or W-6 identification found in the retained text; not a species phenotype impossibility claim. |
| spectrum-metadata | DOI:10.1128/spectrum.03925-23; Indexed identity/status | supports | Benign source identity; detailed experiments are unassessed. |
| spectrum-primary | DOI:10.1128/spectrum.03925-23; Zero-based body paragraph 1 and first two sentences of paragraph 2 | supports | Selected generic physical membrane context and B.subtilis attribution only. |
| amtt-metadata | DOI:10.37256/amtt.5220244537; Crossref title/publication fields and generic abstract | supports | Legacy filename identifies this exact assigned AMTT work; body-dependent statements remain unknown. |
| access-arrhenius-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.37256/amtt.5220244537&amp;format=json&amp;resultType=core; Original zero-hit or failed body access, not article content | context_only | Historical AMTT access limit; no body-absence or fresh native-failure claim. |
| access-arrhenius-publisher | https://wiserpub.com/uploads/1/20241105/29fd7fa9dab36af843bb14d851dbb31c.pdf; Original zero-hit or failed body access, not article content | context_only | Historical AMTT access limit; no body-absence or fresh native-failure claim. |
| access-arrhenius-vor | https://ojs.wiserpub.com/index.php/AMTT/article/download/4537/2677; Original zero-hit or failed body access, not article content | context_only | Historical AMTT access limit; no body-absence or fresh native-failure claim. |
| definition-text | DOI:10.1038/sj.embor.7400662; Derived reading-order text, newline-based introduction lines 23–42 and exact supplied spans | supports | PDF acquisition, text extraction and present copy clocks are separately bound. |
| text-derivation | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-source-agent/definition-derivation-receipt.json; Derived audit or reading receipt; original primary bytes and acquisition clocks bound separately | supports | Actual prior PDF-to-text command and source/output hashes. |
| text-copy | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-source-agent/raw-text-reuse-receipt.json; Derived audit or reading receipt; original primary bytes and acquisition clocks bound separately | supports | Exact prior derived bytes copied now; no new primary acquisition. |
| genes-metadata | DOI:10.3390/genes14010158; Indexed identity/status | supports | Assigned yeast study identity, not universal optimum evidence. |
| genes-primary | DOI:10.3390/genes14010158; Zero-based body paragraph 14, first three sentences | supports | Selected generic yeast PUFA and fluidity context; detailed gene/fitness or pathogenic comparisons are not adopted. |
| taxonomy-296 | NCBITaxon:296; Whole successful official species response | supports | Species identity is positive and does not establish the source strain or best-growth temperature. |
| taxonomy-1880678 | NCBITaxon:1880678; Whole successful official species response | supports | Species identity is positive and does not establish the source strain or best-growth temperature. |
| taxonomy-reading | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-ground-agent/taxonomy-identity.json; Derived audit or reading receipt; original primary bytes and acquisition clocks bound separately | supports | Both official species identities, kept separate from source-specific phenotype support. |
| sources | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-source-agent/source-assessment.json; Derived audit or reading receipt; original primary bytes and acquisition clocks bound separately | supports | Six works and overall UNKNOWN source scope; two bounded source concerns remain separate from formal roles. |
| source-identities | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-source-agent/source-identities-status.json; Derived audit or reading receipt; original primary bytes and acquisition clocks bound separately | supports | All six assigned identities and bounded notice fields; AMTT legacy filename qualification explicit. |
| placements | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-source-agent/source-placement-ledger.json; Derived audit or reading receipt; original primary bytes and acquisition clocks bound separately | supports | All 14 external placements and 10 grounding fields accounted. |
| snippets | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-source-agent/snippet-ledger.json; Derived audit or reading receipt; original primary bytes and acquisition clocks bound separately | supports | All four supplied snippets literal on inspected primary surfaces. |
| notes | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-source-agent/source-note-ledger.json; Derived audit or reading receipt; original primary bytes and acquisition clocks bound separately | supports | All 11 evidence notes and both canonical notes retain explicit scope. |
| source-nodes-edges | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-source-agent/node-edge-source-ledger.json; Derived audit or reading receipt; original primary bytes and acquisition clocks bound separately | supports | All 14 nodes and 10 edges; generic attribution distinguished from numerical or causal sufficiency. |
| classification | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-source-agent/classification-assessment.json; Derived audit or reading receipt; original primary bytes and acquisition clocks bound separately | supports | Assigned classification counterexample narrows the exact Psychrophile alias concern to index 0. |
| canonical | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-source-agent/canonical-assessment.json; Derived audit or reading receipt; original primary bytes and acquisition clocks bound separately | supports | P.fragi remains unknown with inaccessible body; P.sivasensis has a bounded assigned-source attribution gap. |
| canonical-name-search | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-source-agent/canonical-source-name-search.json; Derived audit or reading receipt; original primary bytes and acquisition clocks bound separately | supports | Mechanical whole retained article search with explicit name variants and no phenotype-impossibility inference. |
| source-reading | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-source-agent/primary-reading-scope.json; Derived audit or reading receipt; original primary bytes and acquisition clocks bound separately | supports | Selected generic primary passages; no full-paper scientific or excluded mechanism audit. |
| source-access | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-source-agent/source-access-limits.json; Derived audit or reading receipt; original primary bytes and acquisition clocks bound separately | supports | Unavailable bodies and unverified exact optimum claims remain unknown, not refuted. |
| source-reuse | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-source-agent/source-reuse-receipt.json; Derived audit or reading receipt; original primary bytes and acquisition clocks bound separately | supports | Original acquisition, current copy and current interpretation clocks remain distinct. |
| source-native | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-source-agent/native-check-context.json; Derived audit or reading receipt; original primary bytes and acquisition clocks bound separately | supports | Native two VERIFIED and two inconclusive results are separate from four manual literal confirmations. |
| source-manifest | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-source-agent/evidence-manifest.json; Derived audit or reading receipt; original primary bytes and acquisition clocks bound separately | supports | All 41 frozen source artifacts verified. |
| root-reading | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-source-root/selected-primary-reading.json; Derived audit or reading receipt; original primary bytes and acquisition clocks bound separately | supports | Independent selected primary and owner reading; root read all 18 history projections, not 18 whole history bodies. |
| adjudication | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-root-adjudication.json; Final root adjudication | supports | Exact final finding fields, owner qualifications, actions and source limits control serialization. |

## Limits And Additional Notes

- Exact10–22 optimum calibration and Psychrotolerant exact equivalence remain UNKNOWN. The separate Psychrophile exact-alias concern rests on the assigned D’Amico2°C optimum counterexample; active METPO identity and faithful inherited alias import remain positive. Ramón paragraph10 above20 wording alone does not prove an outside22 optimum.
- AMTT identity is positive via Crossref; current inherited arrhenius-* filenames are aliases for DOI10.37256/amtt.5220244537. EPMC zero-hit and historical403 PDF responses are diagnostic, not article bodies. P.fragi and detailed notes remain unknown/unassessed, not false.
- Canonical P.sivasensis assigned-source concern is limited to actual retained article/name-variant search and absent exact optimum attribution; no species-level biological impossibility or automatic replacement.
- Mendoza inspected abstract supports generic adaptation and literal unsaturation phrase, not a sufficient10–22 organism optimum.
- Spectrum scope is selected B.subtilis introductory physical context; Genes scope is selected generic yeast PUFA/fluidity context. Detailed gene contrasts, pathogenic cold-survival/fitness/ROS/AMR/defense/intervention efficacy remain UNASSESSED_SCOPE.
- No complete temperature-response curves acquired for either canonical example; low-temperature growth alone cannot substitute for best-growth temperature.
- Metadata notice fields contain no correction/retraction indication in inspected fields; not exhaustive publication-status clearance.
- Source catalog context includes benign B.subtilis and generic yeast cohort; no exact canonical, strain/module membership or biological effect inferred from catalog presence.
- Original access, extraction, prior copies and present copy/read clocks remain distinct. Whole text mechanical phrase/name searches do not claim whole-paper scientific reading.
- Raw exact synonyms are documentary identity facts, not independent proof of scientific synonym equivalence.
- Compatible-solute role grounding is qualified closeMatch, not exact material identity; no separate confirmed defect or replacement asserted.
- ROS process versus elevated-level wording and detailed biological efficacy remain unassessed/qualified; edge8 quality subject independently decides the role finding.
- Exact numeric-bin causal bridge, canonical citation/optimum support and source literal attribution are separate source judgments.
- Eight uncaptured script leads and one uncaptured sibling history remain matching-line context, not complete-body scientific authority.
- Covered source B.subtilis has no currently available maintained structured runner within declared roots; primary fallback and catalog scope do not imply absence of modules.
- Private/remote human acceptance remains unknown.
- Root read all 18 history actor/target/event/read-mode projections; four current whole and fourteen qualified prior whole readings are agent scope, not new root whole-body readings.
- The exact Psychrophile alias concern is supported by a reported optimum outside the bin; it does not invalidate the active METPO class or justify a silent locked-OWL edit.
- Original source requests, PDF extraction, copy and reading times remain distinct. Browser failures are not article content and browser cache origin-fetch times remain unknown.
- Four literal snippet matches do not validate the adjacent numerical or sufficient-causal interpretation. Native abstract verification returned two VERIFIED and two inconclusive results.
- Whole 283-line current target and 100 captured inputs; six works, 14 external placements, 10 grounding fields, four literal snippets and 11 evidence notes.
- Original primary acquisitions, extraction and later copies are distinct. Legacy arrhenius filenames identify the assigned AMTT work, not an extra source.
- Grounding history scope is four current whole files plus 14 qualified prior whole readings; uncaptured leads remain matching-line context only.
- Root owns eventual single serialization, actual-output review, native validation and save. This preparation did not execute or import the serializer.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T010102Z-temperature-optimum-low
kind: record
repository: CultureBotAI/TraitMech
title: Whole-record review of temperature optimum low
started_at: '2026-10-22T00:49:43.981927Z'
finished_at: '2026-10-22T01:01:02Z'
reviewer:
  identity: codex
  kind: agent
  independence: independent
  independence_basis: Separate source and grounding audits plus independent root primary,
    owner and final-adjudication readings. Serialization adopts those bounded judgments
    without claiming another independent biological audit.
  model: GPT-6 (Codex)
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'Temperature optimum low needs three substantive corrections: imported process-role
  predicates, the inherited exact Psychrophile synonym scope, and one canonical citation.
  Human acceptance also needs attribution. Active bin identity and all four literal
  snippets are supported; the other canonical example and exact physiological calibration
  remain unknown.'
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
  - path: data/traits/environment/temperature_optimum_low.yaml
    sha256: 77a124a8c80516c4e9e9035da3ed24ab9ffd69ca55e7a87a179b06ef8ae66976
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
  - path: history/infrastructure/disposition-typing-burndown/2026-08-08T060908Z-claude-code-f802c8.yaml
    sha256: 8ede4f80f46395efb74643e1f4158975a119ffaec78b5b291f0fc3a520a11c59
    role: context
  - path: history/infrastructure/node-type-consistency/2026-08-15T014631Z-claude-code-9d7f4d.yaml
    sha256: 21f19561c0d4769e7acc62e05e41d0d395a0f239938f00829f79f2b9c3ac2510
    role: context
  - path: history/infrastructure/pr664-adversarial-review/2026-09-07T010000Z-codex-60bca2.yaml
    sha256: 44f328d3f4735a641a33e6f5823a043ccc87594971cfdd9b58be134f3ea70106
    role: context
  - path: history/infrastructure/pr664-adversarial-review/2026-09-07T022200Z-codex-680abc.yaml
    sha256: e14f687969a1b4621f8857ca8b4f714662a454ed149431abcf0eab4cca346591
    role: context
  - path: history/infrastructure/pr664-adversarial-review/2026-09-07T022300Z-codex-681abc.yaml
    sha256: 614d735ae87694a6591db42fe38bee3f6b4fd12cb3218fea26ee5b515d492dca
    role: context
  - path: history/infrastructure/pr664-adversarial-review/2026-09-07T022400Z-codex-682abc.yaml
    sha256: 557647c63e08f644fcedcb016d618d48c4d7b0085790a07c8d44bfefcf3ef4e5
    role: context
  - path: history/other/canonical-examples-batch1/2026-08-20T074839Z-claude-code-6fb2f5.yaml
    sha256: c938f2928f2eb41505d58c2fb72d8de01d99534d766de9af400010e8778988a4
    role: context
  - path: history/other/canonical-examples-six/2026-08-21T065406Z-codex-a1ab82.yaml
    sha256: 23be5f6ab519511e3e23feffa85813eec4fa3c7e6b900e77fd4a3adc0c26da0e
    role: context
  - path: history/records/oxidative_stress_response/2026-09-04T064000Z-codex-dcb23b.yaml
    sha256: 16c312454060c316af7213b4aab048c319488bf2990f2f7ff5f5a0ca3a9bf98a
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
  - path: research/traits/environment/temperature_optimum_low-deep-research-falcon.md
    sha256: 0d7c573d452588671497887775f6a85a24d7b2a98c3b708f5dfc3924018a751c
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
  - path: scripts/add_palmelloid_formation_trait.py
    sha256: 451f36e0648aa1f7d0a82010cba249b17479c370ad51d0f64f3da8d60b54b6bf
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
  - path: scripts/connect_temperature_optimum_high_graph_183.py
    sha256: 7d2c6bee0f2af46cec82afe93b93b5a993ffb6042f953e7793b2bbc6ea713504
    role: context
  - path: scripts/connect_temperature_optimum_very_low_graph_183.py
    sha256: 4749be5b5aacc87817ea013e587c41096e8a213c93dde74546f4906a0a08dc7e
    role: context
  - path: scripts/connect_temperature_range_mid3_graph_183.py
    sha256: 0b72a42532f79c8efef52aaec4e60e0b58a7c8b9bc7ec288b9fa21a4c0e25656
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
  - path: scripts/review_oxidative_stress_response_graph_183.py
    sha256: 1b4f7e4494b777859a4f209ec765864b644f5df5a3e93f016679f4d3d490d417
    role: context
  - path: scripts/review_temperature_delta_high_graph_183.py
    sha256: dcade5d2fdf07c76e06cd5d8abca898af95a8faabf70e45a62bebf951f2ae31b
    role: context
  - path: scripts/review_temperature_delta_very_low_graph_183.py
    sha256: 1ac23973b6cf54861f6ae79afefe93e39cc9382a93c73c36a8daa37b376334d0
    role: context
  - path: scripts/review_temperature_optimum_high_graph_183.py
    sha256: ed7b046129400db1fa4352250d27569e0844ef837000577f1448e565a0e60576
    role: context
  - path: scripts/review_temperature_optimum_very_low_graph_183.py
    sha256: 17e41b0426e6c41a43e7624799cf35db9737ef372d3aeb3ea40ac0a2dce20869
    role: context
  - path: scripts/review_temperature_range_mid3_graph_183.py
    sha256: 623668a7f0f2cd487c096c2b786471fe986f64cfd5c34edad30422299f03794a
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
- target_id: METPO:1000442
  path: data/traits/environment/temperature_optimum_low.yaml
  label: temperature optimum low
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_optimum_low.yaml
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
  selection: Tenth record in the initialized local batch 013 queue. Whole 283-line
    target and 100 captured inputs verified; local review does not assert remote publication.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - METPO:1000442
checks:
- check_id: audit-graphs
  name: Full-corpus graph audit
  status: passed
  required: true
  target_ids:
  - METPO:1000442
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
  - METPO:1000442
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
  - METPO:1000442
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
  - METPO:1000442
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
  - METPO:1000442
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
  - METPO:1000442
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
  - METPO:1000442
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
- check_id: temperature-optimum-low-validate
  name: Focused native validation
  status: passed
  required: true
  target_ids:
  - METPO:1000442
  command: just validate data/traits/environment/temperature_optimum_low.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Native record validation passed; scientific interpretation is assessed
    separately.
  evidence_ids:
  - check-temperature-optimum-low-validate
- check_id: temperature-optimum-low-strict
  name: Focused strict validation
  status: passed
  required: true
  target_ids:
  - METPO:1000442
  command: just validate-strict data/traits/environment/temperature_optimum_low.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: The actual validate-strict command passed.
  evidence_ids:
  - check-temperature-optimum-low-strict
- check_id: temperature-optimum-low-snippets-network
  name: Focused network snippet check
  status: passed
  required: true
  target_ids:
  - METPO:1000442
  command: just verify-snippets --record data/traits/environment/temperature_optimum_low.yaml
    --out /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-snippets.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: Two of four snippets were VERIFIED and two were NOT_IN_ABSTRACT in the
    native abstract check. Manual primary inspection finds all four literal; native
    inconclusive results are not body-absence evidence.
  evidence_ids:
  - check-temperature-optimum-low-snippets-network
- check_id: batch012-qc
  name: Qualified batch-twelve QC
  status: passed
  required: true
  target_ids:
  - METPO:1000442
  command: just qc
  exit_code: 0
  expected_exit_code: 0
  summary: Actual prior QC qualified against B13 bytes; this is not a fresh B13 QC
    execution or publication.
  evidence_ids:
  - check-batch012-qc
- check_id: uniprot-applicability
  name: Protein-instance metadata applicability
  status: not_applicable
  required: false
  target_ids:
  - METPO:1000442
  summary: Two reviewed label-only protein classes and no instances in a quantitative
    NONMECHANISTIC graph; no compulsory accession or token instance.
  evidence_ids:
  - record
  - policy
  - expression
- check_id: expression-adapter-availability
  name: Structured source-organism expression query availability
  status: unavailable
  required: false
  target_ids:
  - METPO:1000442
  summary: An appropriate generic B.subtilis source query was not executed because
    fresh bounded discovery found the maintained adapter unavailable. Catalog and
    selected primary fallback do not supply membership results.
  evidence_ids:
  - expression
  - expression-discovery
  - spectrum-primary
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
- evidence_id: check-temperature-optimum-low-validate
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-validate.log
  locator: Executed 2026-10-22T00:50:07.333126+00:00 through 2026-10-22T00:50:07.952678+00:00;
    metadata temperature-optimum-low-validate.json
  accessed_at: '2026-10-22T00:50:07.952678Z'
  support: context_only
  summary: Native record validation passed; scientific interpretation is assessed
    separately.
  snapshot_sha256: dfae4a76159e60e70e34cbb2a2e5112506482b6e5a34e9cc6936b7ee51377f31
- evidence_id: check-temperature-optimum-low-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-strict.log
  locator: Executed 2026-10-22T00:50:07.333891+00:00 through 2026-10-22T00:50:08.347569+00:00;
    metadata temperature-optimum-low-strict.json
  accessed_at: '2026-10-22T00:50:08.347569Z'
  support: context_only
  summary: The actual validate-strict command passed.
  snapshot_sha256: 5e132bf4fae5126e640569ba1ac895e07ac137471ad212c72ce4ce0493b4ac4e
- evidence_id: check-temperature-optimum-low-snippets-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-snippets-network.log
  locator: Executed 2026-10-22T00:50:12.466666+00:00 through 2026-10-22T00:50:15.779381+00:00;
    metadata temperature-optimum-low-snippets-network.json
  accessed_at: '2026-10-22T00:50:15.779381Z'
  support: context_only
  summary: Two of four snippets were VERIFIED and two were NOT_IN_ABSTRACT in the
    native abstract check. Manual primary inspection finds all four literal; native
    inconclusive results are not body-absence evidence.
  snapshot_sha256: 5bf67bbc3b343cdbf59ee033905197e4110b0c6711f74143528e70f82c70fdac
- evidence_id: check-batch012-qc
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-012.j4n7q2vc/batch012-qc.log
  locator: Executed 2026-10-21T23:02:31.440808+00:00 through 2026-10-21T23:04:01.628423+00:00;
    metadata batch012-qc.json
  accessed_at: '2026-10-21T23:04:01.628423Z'
  support: context_only
  summary: Actual prior QC qualified against B13 bytes; this is not a fresh B13 QC
    execution or publication.
  snapshot_sha256: 8ab67b821055863ce13616ed79a0acacaf61b632dcb80f6aa63fd45f0485c52b
- evidence_id: record
  kind: record_content
  reference: data/traits/environment/temperature_optimum_low.yaml
  locator: Whole current record
  accessed_at: '2026-10-22T00:49:44.567378Z'
  support: supports
  summary: Fourteen nodes, ten edges, ten embedded events, two canonical examples,
    two reviewed label-only protein classes and zero instances.
  snapshot_sha256: 77a124a8c80516c4e9e9035da3ed24ab9ffd69ca55e7a87a179b06ef8ae66976
- evidence_id: reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-b12-qc-supplement-qualified.json
  locator: Actual B12-to-B13 diagnostic qualification
  accessed_at: '2026-10-21T23:05:39.165510Z'
  support: supports
  summary: Original diagnostic times, failures, retries and skips remain explicit.
  snapshot_sha256: e1fa58cb626ef76e2b2066404078b9893b069a5b53a0cffbc3a184e68f0cd9f1
- evidence_id: reuse-postcheck
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-output-verification-agent/post-execution-verification.json
  locator: Derived audit or reading receipt; original primary bytes and acquisition
    clocks bound separately
  accessed_at: '2026-10-21T23:07:53.187524Z'
  support: supports
  summary: Independent qualification output verification, not new QC.
  snapshot_sha256: 42a5580991e7251963a9b83d0817facda019de29d9e13208e870c27e1c62ad7d
- evidence_id: local-init
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/batch013-local-initialization-receipt.json
  locator: Derived audit or reading receipt; original primary bytes and acquisition
    clocks bound separately
  accessed_at: '2026-10-21T23:09:00.804479Z'
  support: supports
  summary: Actual local initialization; publication remains separate.
  snapshot_sha256: cda5c0d3753e7a2a3ceb9ba723261fa79d4f760aad1713ff2d33b08def3577f7
- evidence_id: policy
  kind: authority
  reference: docs/GROUNDING_POLICY.md
  locator: Captured maintained authority
  accessed_at: '2026-10-22T00:54:34.604185Z'
  support: supports
  summary: Protein family/function grounding and optional protein instances.
  snapshot_sha256: 891678c983c2283a47c81c47950b35753981e9339d105f3bbdda92a1f5ab7f42
- evidence_id: playbook
  kind: authority
  reference: docs/CURATION_PLAYBOOK.md
  locator: Captured maintained authority
  accessed_at: '2026-10-22T00:54:34.604185Z'
  support: supports
  summary: Source scope and attributable acceptance.
  snapshot_sha256: 735e9b810471da9f7d8364e35ffe1e741edb3421480dac01727db6ea5aa65da9
- evidence_id: schema
  kind: authority
  reference: src/traitmech/schema/traitmech.yaml
  locator: Captured maintained authority
  accessed_at: '2026-10-22T00:54:34.604185Z'
  support: supports
  summary: Current facets and NONMECHANISTIC scope.
  snapshot_sha256: 46c47fc627b80ccbba1e8ab3fb6f2aee93bc2aef7aaf72fe9aadc3257f2c02dd
- evidence_id: predicate-mapping
  kind: authority
  reference: mappings/predicate_grounding.tsv
  locator: Captured maintained authority
  accessed_at: '2026-10-22T00:54:34.604185Z'
  support: supports
  summary: Mappings can populate empty IDs; populated assertions are skipped.
  snapshot_sha256: 8e28c19e93aca3dc164a3befbe2612b289241de457c59f499e65936c03b7ce52
- evidence_id: node-mapping
  kind: authority
  reference: mappings/node_grounding.tsv
  locator: Captured maintained authority
  accessed_at: '2026-10-22T00:54:34.604185Z'
  support: supports
  summary: Current label/type keys and qualified functional mappings.
  snapshot_sha256: d7de9b3ab04960c4775a5bc295a945bd1a72d81467830459f4793e654f82b3d0
- evidence_id: local-v3
  kind: authority
  reference: proposals/metpo_traitmech_v3/metpo_proposal_classes_robot.tsv
  locator: Captured maintained authority
  accessed_at: '2026-10-22T00:54:34.604185Z'
  support: supports
  summary: Local membrane-fluidity quality.
  snapshot_sha256: 1a1cc789782cfae195c1fc81ddaf848d06d162c7434d94cceb66838de98ab6fa
- evidence_id: local-v8
  kind: authority
  reference: proposals/metpo_traitmech_v8/metpo_proposal_properties_robot.tsv
  locator: Captured maintained authority
  accessed_at: '2026-10-22T00:54:34.604185Z'
  support: supports
  summary: Local confers broad endpoints and trait range.
  snapshot_sha256: 5445e86e845e0a2638292cff4586bf3858b1341d37fecf2e86cefcdbc9a046cd
- evidence_id: identity
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-ground-agent/identity-assessment.json
  locator: Derived audit or reading receipt; original primary bytes and acquisition
    clocks bound separately
  accessed_at: '2026-10-22T00:54:34.564164Z'
  support: supports
  summary: Active bin and direct parent; documentary synonym provenance is distinct
    from scientific equivalence.
  snapshot_sha256: 61b81151a5255302eb5b9efbd45794fecb31bc708bc38c1e1827660c53874d7b
- evidence_id: nodes-edges
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-ground-agent/node-edge-grounding-ledger.json
  locator: Derived audit or reading receipt; original primary bytes and acquisition
    clocks bound separately
  accessed_at: '2026-10-22T00:54:34.596195Z'
  support: supports
  summary: All 14 node and 10 relation judgments, including contrary controls.
  snapshot_sha256: 8508c0556635b6164c7ba995ed4f18e782a7fca04471424684485c0f1edc7310
- evidence_id: owners
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-ground-agent/owner-provenance-assessment.json
  locator: Derived audit or reading receipt; original primary bytes and acquisition
    clocks bound separately
  accessed_at: '2026-10-22T00:54:34.603172Z'
  support: supports
  summary: Current record, conditional shared writers and sibling contexts distinguished.
  snapshot_sha256: f8ad8a155e80efc7186f97a5b5c5731f338ee464f83f706aa7fe5e902e8e8603
- evidence_id: owner-primary
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-ground-agent/owner-primary-reading.json
  locator: Derived audit or reading receipt; original primary bytes and acquisition
    clocks bound separately
  accessed_at: '2026-10-22T00:54:34.565778Z'
  support: supports
  summary: Actual maintained writer and migration decision windows.
  snapshot_sha256: 3d0a351d47223f406e02ebd5421d284618c59d0dbf07ee20de3c24d4c5905070
- evidence_id: alias-owner
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-ground-agent/alias-source-and-owner-qualification.json
  locator: Derived audit or reading receipt; original primary bytes and acquisition
    clocks bound separately
  accessed_at: '2026-10-22T00:54:34.564915Z'
  support: supports
  summary: Seeder copies upstream aliases for new records but normally skips existing
    ones; release migration excludes this target and finalizer writes reports only.
  snapshot_sha256: 195a04eb27b22874a509773dc152dfd78b6b47cc7358ad35ac0f7b306713d856
- evidence_id: human-search
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-ground-agent/search-and-provenance.json
  locator: Derived audit or reading receipt; original primary bytes and acquisition
    clocks bound separately
  accessed_at: '2026-10-22T00:50:16.214958Z'
  support: supports
  summary: 169 ignored-inclusive matching paths, 67 actual review target arrays, zero
    exact current target.
  snapshot_sha256: 8bcb12453f4eb96b01ca0042f60bc4b24d97a4dbc2f309b42b46b8e1bedb795f
- evidence_id: histories
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-ground-agent/history-reading-provenance.json
  locator: Derived audit or reading receipt; original primary bytes and acquisition
    clocks bound separately
  accessed_at: '2026-10-22T00:54:34.602745Z'
  support: supports
  summary: Four current whole history reads plus 14 unchanged qualified prior whole
    reads; 18 current projections.
  snapshot_sha256: f4c8987d7b7d4fe7c5dbeaefbda98d75aaa52b89588187da634bcb232b8d7630
- evidence_id: discovery
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-ground-agent/discovery-disposition.json
  locator: Derived audit or reading receipt; original primary bytes and acquisition
    clocks bound separately
  accessed_at: '2026-10-22T00:54:34.595897Z'
  support: supports
  summary: Eight uncaptured script leads and one sibling history remain matching-line
    context only.
  snapshot_sha256: a378d794403bfbd8268bf154cf6ebfb7a78bcd8822b5f5e5dae12ed5ef3d6266
- evidence_id: expression
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-ground-agent/expression-and-readiness.json
  locator: Derived audit or reading receipt; original primary bytes and acquisition
    clocks bound separately
  accessed_at: '2026-10-22T00:54:34.603668Z'
  support: supports
  summary: Covered benign source context has an unavailable adapter; catalog and primary
    fallback do not establish module membership.
  snapshot_sha256: b1953e594ca29566dfb8171bf9e0a38c3defba1f96df68d5acb2a6834d84c3df
- evidence_id: expression-discovery
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-ground-agent/expression-runner-current-discovery.json
  locator: Derived audit or reading receipt; original primary bytes and acquisition
    clocks bound separately
  accessed_at: '2026-10-22T00:51:18.468365Z'
  support: supports
  summary: Fresh bounded PATH/project/install-root discovery; no global absence claim.
  snapshot_sha256: 09a582c9d1a147cb218ce55296cb2888fdccc3a47fabf0d48422104b90e27c63
- evidence_id: local-authority
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-ground-agent/local-authority-reading.json
  locator: Derived audit or reading receipt; original primary bytes and acquisition
    clocks bound separately
  accessed_at: '2026-10-22T00:54:34.526653Z'
  support: supports
  summary: Exact current proposal, mapping and schema windows.
  snapshot_sha256: ad418318bd4e6697a61a8b2d476bc8a0dea9c6f6b01fe43d70a7d7bced209a6a
- evidence_id: chebi-role
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-ground-agent/chebi-role-supplement.json
  locator: Derived audit or reading receipt; original primary bytes and acquisition
    clocks bound separately
  accessed_at: '2026-10-22T00:53:05.332032Z'
  support: supports
  summary: Osmolyte role and material bearer distinguished without a forced replacement.
  snapshot_sha256: 52646e7b9e9052e0aafaeac3155ad8c5f37e6713a88169ee580114e12b72c183
- evidence_id: ground-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-ground-agent/reading-scope-receipt.json
  locator: Derived audit or reading receipt; original primary bytes and acquisition
    clocks bound separately
  accessed_at: '2026-10-22T00:54:34.604354Z'
  support: supports
  summary: Actual current readings and honest prior-read reuse scope.
  snapshot_sha256: 3d3c31055bf6b00111fe521d1ab3cd15427833ddc7e0ca574a555b0ad0c4d594
- evidence_id: ground-manifest
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-ground-agent/evidence-manifest.json
  locator: Derived audit or reading receipt; original primary bytes and acquisition
    clocks bound separately
  accessed_at: '2026-10-22T00:54:34.608036Z'
  support: supports
  summary: All 31 frozen ground artifacts verified.
  snapshot_sha256: a09c1f7678f89fa6a30236aa65abef269bf7188d36afe10e3e3b1c46a58e3114
- evidence_id: metpo-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/repo/data/raw/metpo.owl
  locator: Selected primary statements at the recorded reading time
  accessed_at: '2026-10-22T00:50:16.095264Z'
  support: supports
  summary: Active exact class and parent, inclusive 10–22 Cel restriction and upstream
    alias scope.
  snapshot_sha256: 8b6f8fe0510a698579e532658c8ace05da2550093365df9ca83feb0741778415
- evidence_id: metpo-primary-projection
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-ground-agent/metpo-authority.json
  locator: Derived audit or reading receipt; original primary bytes and acquisition
    clocks bound separately
  accessed_at: '2026-10-22T00:50:16.095264Z'
  support: supports
  summary: Exact primary bytes and selected statement projection.
  snapshot_sha256: 712e8d2942df6d2c0db066ecccfd13745224019edafbf1882344df1547c0c9ba
- evidence_id: pato-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/pato.db
  locator: Selected primary statements at the recorded reading time
  accessed_at: '2026-10-22T00:50:14.194559Z'
  support: supports
  summary: Low temperature denotes a quality or condition, not a temperature-decrease
    event.
  snapshot_sha256: 179ab512b5c3a8827c74e2a496da575e2908a84740429deef265d58c9ce61d3b
- evidence_id: pato-primary-projection
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-ground-agent/selected-pato-primary-reading.json
  locator: Derived audit or reading receipt; original primary bytes and acquisition
    clocks bound separately
  accessed_at: '2026-10-22T00:50:14.194559Z'
  support: supports
  summary: Exact primary bytes and selected statement projection.
  snapshot_sha256: 56088117956e2300d0b06d29533804b8a27e0f36afb1669025bd3f47897f8bcc
- evidence_id: chebi-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/chebi.db
  locator: Selected primary statements at the recorded reading time
  accessed_at: '2026-10-22T00:50:14.254867Z'
  support: supports
  summary: Osmolyte role definition used under a qualified close functional mapping.
  snapshot_sha256: 26ad4890cdcf6ee357760d815dfee8f5ba81e0873e62cb379369b04205722b0f
- evidence_id: chebi-primary-projection
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-ground-agent/selected-chebi-primary-reading.json
  locator: Derived audit or reading receipt; original primary bytes and acquisition
    clocks bound separately
  accessed_at: '2026-10-22T00:50:14.254867Z'
  support: supports
  summary: Exact primary bytes and selected statement projection.
  snapshot_sha256: 48370b3abd6ba0a7117e542bfd71e4566dcc104b7ff2fa433c5e5b531db23fb8
- evidence_id: ro-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/ro.db
  locator: Selected primary statements at the recorded reading time
  accessed_at: '2026-10-22T00:50:14.190515Z'
  support: supports
  summary: Regulation predicates inherit process subject and object roles.
  snapshot_sha256: 849e616c29fecd0d4a6c6dee0dc0f6f117ace7167dbfa1e0f043dc84868f83cb
- evidence_id: ro-primary-projection
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-ground-agent/selected-ro-primary-reading.json
  locator: Derived audit or reading receipt; original primary bytes and acquisition
    clocks bound separately
  accessed_at: '2026-10-22T00:50:14.190515Z'
  support: supports
  summary: Exact primary bytes and selected statement projection.
  snapshot_sha256: bd681d8d59839c9ed4e43487a589be0edc0c55899c9a4aa2337a4eeebe8a87bc
- evidence_id: definition-metadata
  kind: primary_source
  reference: DOI:10.1038/sj.embor.7400662
  locator: Indexed identity/status and generic abstract
  accessed_at: '2026-10-21T10:00:01.461116Z'
  support: supports
  summary: Generic cold classification and supplied decreased-fluidity phrase.
  snapshot_sha256: 24d64254a2baba7c573dff7ae523cc0e00d30e297c4f1fd7aa3a23c51a057059
- evidence_id: definition-primary
  kind: primary_source
  reference: DOI:10.1038/sj.embor.7400662
  locator: Author-repository PDF introduction; derived newline-based lines 23–42
  accessed_at: '2026-10-21T10:03:39.641646Z'
  support: supports
  summary: Broad Psychrophile category includes a reported optimum of 2 degrees C
    outside this bin; no organism substitution or intervention proposed.
  snapshot_sha256: 5a7678c6418efbcccf54d91c55eea1c08f2a4ed0ce0e07a6995d5903b9a0eb2e
- evidence_id: mendoza-metadata
  kind: primary_source
  reference: DOI:10.1146/annurev-micro-091313-103612
  locator: Indexed identity/status and abstract
  accessed_at: '2026-10-21T10:00:02.042457Z'
  support: supports
  summary: Literal unsaturation phrase and generic attribution; exact optimum sufficiency
    remains unknown.
  snapshot_sha256: 801da630644a181211f991a6f21c49b178e42a65f615c4eebd8196bc29244588
- evidence_id: mendoza-publisher
  kind: primary_source
  reference: DOI:10.1146/annurev-micro-091313-103612
  locator: Retained actual browser abstract export, not raw HTML
  accessed_at: '2026-10-21T23:38:35Z'
  support: supports
  summary: Original tool-call bounds are preserved; origin cache-fetch time remains
    unknown.
  snapshot_sha256: b8635235ad5e362d0b33ef4834f84eb25fe7ff6b1bd1321affb2b61cecbc66fc
- evidence_id: cold-metadata
  kind: primary_source
  reference: DOI:10.1007/s42770-023-01057-4
  locator: Indexed identity/status and abstract
  accessed_at: '2026-10-21T22:07:08.865512Z'
  support: supports
  summary: Assigned review identity is separate from exact species and optimum support.
  snapshot_sha256: da5cffab81fe0e039c6fcec8f318b2715f5604eaf8722ea6f63f944178ed447b
- evidence_id: cold-primary
  kind: primary_source
  reference: DOI:10.1007/s42770-023-01057-4
  locator: Selected paragraph 10 classification plus mechanical whole-text canonical-name
    search
  accessed_at: '2026-10-21T22:07:50.938485Z'
  support: supports
  summary: No P.sivasensis or W-6 identification found in the retained text; not a
    species phenotype impossibility claim.
  snapshot_sha256: bb09a59c07f43ff0af177f89b624c8b5d4841e513ed0d478120954a016342889
- evidence_id: spectrum-metadata
  kind: primary_source
  reference: DOI:10.1128/spectrum.03925-23
  locator: Indexed identity/status
  accessed_at: '2026-10-21T22:07:08.906527Z'
  support: supports
  summary: Benign source identity; detailed experiments are unassessed.
  snapshot_sha256: 745eedfa2c11814739b07a4d944725bf565eb4e3f9c6b207ba0d31b967563f98
- evidence_id: spectrum-primary
  kind: primary_source
  reference: DOI:10.1128/spectrum.03925-23
  locator: Zero-based body paragraph 1 and first two sentences of paragraph 2
  accessed_at: '2026-10-21T22:07:32.905772Z'
  support: supports
  summary: Selected generic physical membrane context and B.subtilis attribution only.
  snapshot_sha256: 4e57f358369566231e022520fc5b5adad7b8c182adfa282d9ed404fa3298a561
- evidence_id: amtt-metadata
  kind: primary_source
  reference: DOI:10.37256/amtt.5220244537
  locator: Crossref title/publication fields and generic abstract
  accessed_at: '2026-10-22T00:29:26.281512Z'
  support: supports
  summary: Legacy filename identifies this exact assigned AMTT work; body-dependent
    statements remain unknown.
  snapshot_sha256: 9f5ed8f0f9d07aface3f482bc888a6c47a4d9683abf51f76b16bf56412857cf7
- evidence_id: access-arrhenius-metadata
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.37256/amtt.5220244537&format=json&resultType=core
  locator: Original zero-hit or failed body access, not article content
  accessed_at: '2026-10-22T00:29:26.622156Z'
  support: context_only
  summary: Historical AMTT access limit; no body-absence or fresh native-failure claim.
  snapshot_sha256: d0eef7c61f38fab3f0b2a3d73127915d63da077e0617bff6ac487ec290045df3
- evidence_id: access-arrhenius-publisher
  kind: validation
  reference: https://wiserpub.com/uploads/1/20241105/29fd7fa9dab36af843bb14d851dbb31c.pdf
  locator: Original zero-hit or failed body access, not article content
  accessed_at: '2026-10-22T00:29:26.719413Z'
  support: context_only
  summary: Historical AMTT access limit; no body-absence or fresh native-failure claim.
  snapshot_sha256: f358c15edde3a09413815f1b01c69bfb0e5e58e96629819638fefa8806de521a
- evidence_id: access-arrhenius-vor
  kind: validation
  reference: https://ojs.wiserpub.com/index.php/AMTT/article/download/4537/2677
  locator: Original zero-hit or failed body access, not article content
  accessed_at: '2026-10-22T00:30:07.641227Z'
  support: context_only
  summary: Historical AMTT access limit; no body-absence or fresh native-failure claim.
  snapshot_sha256: c56ebc2fa81c11f95e4c9ded4da58937f68f3f57d372fc7dff2181a3de31e605
- evidence_id: definition-text
  kind: primary_source
  reference: DOI:10.1038/sj.embor.7400662
  locator: Derived reading-order text, newline-based introduction lines 23–42 and
    exact supplied spans
  accessed_at: '2026-10-21T21:57:11.990598Z'
  support: supports
  summary: PDF acquisition, text extraction and present copy clocks are separately
    bound.
  snapshot_sha256: 71ef77b88e880420f533454926cac17498cbf8db380465139c888057115143e8
- evidence_id: text-derivation
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-source-agent/definition-derivation-receipt.json
  locator: Derived audit or reading receipt; original primary bytes and acquisition
    clocks bound separately
  accessed_at: '2026-10-21T21:57:11.990598Z'
  support: supports
  summary: Actual prior PDF-to-text command and source/output hashes.
  snapshot_sha256: 4bc68e1e7c942f28f8b2be82ef5b82e45461cdec22ed95828753130bc433d1ac
- evidence_id: text-copy
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-source-agent/raw-text-reuse-receipt.json
  locator: Derived audit or reading receipt; original primary bytes and acquisition
    clocks bound separately
  accessed_at: '2026-10-22T00:52:12.514086Z'
  support: supports
  summary: Exact prior derived bytes copied now; no new primary acquisition.
  snapshot_sha256: 5abcb1bfe626b7fa67056dda76997d02e34fb3801486993464fbba42d8854a56
- evidence_id: genes-metadata
  kind: primary_source
  reference: DOI:10.3390/genes14010158
  locator: Indexed identity/status
  accessed_at: '2026-10-22T00:51:27.318435Z'
  support: supports
  summary: Assigned yeast study identity, not universal optimum evidence.
  snapshot_sha256: 6fd73475ff7e75c556ae91cce6a28b347adf2f81acc0f922f8fc8efb910de6b7
- evidence_id: genes-primary
  kind: primary_source
  reference: DOI:10.3390/genes14010158
  locator: Zero-based body paragraph 14, first three sentences
  accessed_at: '2026-10-22T00:51:27.763667Z'
  support: supports
  summary: Selected generic yeast PUFA and fluidity context; detailed gene/fitness
    or pathogenic comparisons are not adopted.
  snapshot_sha256: c0d1c36b7cd10e8ca3e392c75a53ad6190a718aaf768764b3455f89479217e6e
- evidence_id: taxonomy-296
  kind: authority
  reference: NCBITaxon:296
  locator: Whole successful official species response
  accessed_at: '2026-10-22T00:50:44.495340Z'
  support: supports
  summary: Species identity is positive and does not establish the source strain or
    best-growth temperature.
  snapshot_sha256: 13da301e2587429c884ae3baaee2237bda29d76d509db3f1b04211fa4bc7cd13
- evidence_id: taxonomy-1880678
  kind: authority
  reference: NCBITaxon:1880678
  locator: Whole successful official species response
  accessed_at: '2026-10-22T00:50:44.888737Z'
  support: supports
  summary: Species identity is positive and does not establish the source strain or
    best-growth temperature.
  snapshot_sha256: 8db86914625d96e8f03a342e74913e73fd2a32b2eeda2d96b9b644771da5c142
- evidence_id: taxonomy-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-ground-agent/taxonomy-identity.json
  locator: Derived audit or reading receipt; original primary bytes and acquisition
    clocks bound separately
  accessed_at: '2026-10-22T00:54:34.563824Z'
  support: supports
  summary: Both official species identities, kept separate from source-specific phenotype
    support.
  snapshot_sha256: 94e3a202bcfa889b7a8109e1f5afa8e05f32ea12c0ff50b990dbeb30b90e435e
- evidence_id: sources
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-source-agent/source-assessment.json
  locator: Derived audit or reading receipt; original primary bytes and acquisition
    clocks bound separately
  accessed_at: '2026-10-22T00:54:14.858511Z'
  support: supports
  summary: Six works and overall UNKNOWN source scope; two bounded source concerns
    remain separate from formal roles.
  snapshot_sha256: f120156e56d796f9969890a9a8e199e846c40f9cac3a44269a6882b4331d2128
- evidence_id: source-identities
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-source-agent/source-identities-status.json
  locator: Derived audit or reading receipt; original primary bytes and acquisition
    clocks bound separately
  accessed_at: '2026-10-22T00:54:14.858511Z'
  support: supports
  summary: All six assigned identities and bounded notice fields; AMTT legacy filename
    qualification explicit.
  snapshot_sha256: 37ae54db171579352e9538c45d443699a337a695c4aebc78b00b18512a568d94
- evidence_id: placements
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-source-agent/source-placement-ledger.json
  locator: Derived audit or reading receipt; original primary bytes and acquisition
    clocks bound separately
  accessed_at: '2026-10-22T00:54:14.858511Z'
  support: supports
  summary: All 14 external placements and 10 grounding fields accounted.
  snapshot_sha256: 1926bf921e132d14c4ee1977133873779b6c1bc90cddeeec6c226d829379a065
- evidence_id: snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-source-agent/snippet-ledger.json
  locator: Derived audit or reading receipt; original primary bytes and acquisition
    clocks bound separately
  accessed_at: '2026-10-22T00:54:14.858511Z'
  support: supports
  summary: All four supplied snippets literal on inspected primary surfaces.
  snapshot_sha256: dff162ff81bc8758547aaac728efcf6bc2d61dae9523c2bc578c04b2cf739d3c
- evidence_id: notes
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-source-agent/source-note-ledger.json
  locator: Derived audit or reading receipt; original primary bytes and acquisition
    clocks bound separately
  accessed_at: '2026-10-22T00:54:14.858511Z'
  support: supports
  summary: All 11 evidence notes and both canonical notes retain explicit scope.
  snapshot_sha256: 42615146ae8c6b6bb2253027de6251fc4deb4b08da2fb3043f392de020c8e1d6
- evidence_id: source-nodes-edges
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-source-agent/node-edge-source-ledger.json
  locator: Derived audit or reading receipt; original primary bytes and acquisition
    clocks bound separately
  accessed_at: '2026-10-22T00:54:14.858511Z'
  support: supports
  summary: All 14 nodes and 10 edges; generic attribution distinguished from numerical
    or causal sufficiency.
  snapshot_sha256: be405e767967970ffe789d68f44dcd62044a3e0cc6d055c136bfe0bf3e4ffccc
- evidence_id: classification
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-source-agent/classification-assessment.json
  locator: Derived audit or reading receipt; original primary bytes and acquisition
    clocks bound separately
  accessed_at: '2026-10-22T00:54:14.858511Z'
  support: supports
  summary: Assigned classification counterexample narrows the exact Psychrophile alias
    concern to index 0.
  snapshot_sha256: 16c4b7f13a65200ef9bd1ff1ad88bb1c6dfa96fe3fa6099281638f4da2b4e367
- evidence_id: canonical
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-source-agent/canonical-assessment.json
  locator: Derived audit or reading receipt; original primary bytes and acquisition
    clocks bound separately
  accessed_at: '2026-10-22T00:54:14.858511Z'
  support: supports
  summary: P.fragi remains unknown with inaccessible body; P.sivasensis has a bounded
    assigned-source attribution gap.
  snapshot_sha256: 27774c3be71e8b11a27ad29460e03c31e6e9a3846faf37c5ac53852130bbe6dd
- evidence_id: canonical-name-search
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-source-agent/canonical-source-name-search.json
  locator: Derived audit or reading receipt; original primary bytes and acquisition
    clocks bound separately
  accessed_at: '2026-10-22T00:54:14.858511Z'
  support: supports
  summary: Mechanical whole retained article search with explicit name variants and
    no phenotype-impossibility inference.
  snapshot_sha256: 699b8517bcecb2160649e75f15d8d14fea9c1fc938dbbf80d983e3498a3d7b50
- evidence_id: source-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-source-agent/primary-reading-scope.json
  locator: Derived audit or reading receipt; original primary bytes and acquisition
    clocks bound separately
  accessed_at: '2026-10-22T00:54:14.858511Z'
  support: supports
  summary: Selected generic primary passages; no full-paper scientific or excluded
    mechanism audit.
  snapshot_sha256: 4923aedc7268c58213349a16afa304c1bf98e48465ed8ed713146dd613613bb8
- evidence_id: source-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-source-agent/source-access-limits.json
  locator: Derived audit or reading receipt; original primary bytes and acquisition
    clocks bound separately
  accessed_at: '2026-10-22T00:54:14.858511Z'
  support: supports
  summary: Unavailable bodies and unverified exact optimum claims remain unknown,
    not refuted.
  snapshot_sha256: f0988c65014f2b43cadbab2f85fe981ccb27deeba3ddc952d674622293a1a87f
- evidence_id: source-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-source-agent/source-reuse-receipt.json
  locator: Derived audit or reading receipt; original primary bytes and acquisition
    clocks bound separately
  accessed_at: '2026-10-22T00:51:22.157170Z'
  support: supports
  summary: Original acquisition, current copy and current interpretation clocks remain
    distinct.
  snapshot_sha256: 2952db9955893dfa379e7c68e13ec4b9be75a361b82c5e1caec0f0dcb28d45d6
- evidence_id: source-native
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-source-agent/native-check-context.json
  locator: Derived audit or reading receipt; original primary bytes and acquisition
    clocks bound separately
  accessed_at: '2026-10-22T00:54:14.858511Z'
  support: supports
  summary: Native two VERIFIED and two inconclusive results are separate from four
    manual literal confirmations.
  snapshot_sha256: f6a26f827942f45b6d55c6b2e600fe8de92905f2c5b14e34fd561bb87fe07714
- evidence_id: source-manifest
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-source-agent/evidence-manifest.json
  locator: Derived audit or reading receipt; original primary bytes and acquisition
    clocks bound separately
  accessed_at: '2026-10-22T00:54:14.907912Z'
  support: supports
  summary: All 41 frozen source artifacts verified.
  snapshot_sha256: 3c16e0d429689df8d521bd9dcbecc7143596dc355b52c46cddafd8218639461d
- evidence_id: root-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-source-root/selected-primary-reading.json
  locator: Derived audit or reading receipt; original primary bytes and acquisition
    clocks bound separately
  accessed_at: '2026-10-22T00:56:16.467641Z'
  support: supports
  summary: Independent selected primary and owner reading; root read all 18 history
    projections, not 18 whole history bodies.
  snapshot_sha256: 7b2fda984af98c8ad50ce109eabdeae50d71de9bb4c63d4629403438f4b7583d
- evidence_id: adjudication
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-optimum-low-root-adjudication.json
  locator: Final root adjudication
  accessed_at: '2026-10-22T00:56:16.468441Z'
  support: supports
  summary: Exact final finding fields, owner qualifications, actions and source limits
    control serialization.
  snapshot_sha256: 63809669db5dc4023bdb4e8016f0e5fd59463a0ac93451daa62a6cdb89ed3729
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: active class and direct parent'
  outcome: supported
  target_ids:
  - METPO:1000442
  summary: Active METPO:1000442 and parent METPO:1000304 agree with the numeric low-bin
    identity. Raw exact aliases are faithfully inherited documentary facts; scientific
    equivalence is assessed separately.
  evidence_ids:
  - identity
  - metpo-primary
  - alias-owner
  - record
- assessment_id: synonym-scope
  area: scope
  topic: 'Native checklist: qualitative alias and numerical bin'
  outcome: concern
  target_ids:
  - METPO:1000442
  summary: The assigned review includes a Psychrophile with a reported optimum of
    2 degrees C, outside 10–22 degrees C. This supports the index 0 exactness concern
    without invalidating active identity. Psychrotolerant equivalence and exact cutoff
    calibration remain unknown.
  evidence_ids:
  - classification
  - definition-primary
  - definition-text
  - alias-owner
  - identity
- assessment_id: definition
  area: quantity
  topic: 'Native checklist: measurement and exact threshold'
  outcome: unknown
  target_ids:
  - METPO:1000442
  summary: Best-growth ambient temperature is distinct from exposure, survival or
    low-temperature growth. The 10–22 interval is explicit in the local identity,
    but inspected generic adaptation sources do not calibrate that precise bin or
    establish sufficient whole-organism optima.
  evidence_ids:
  - sources
  - placements
  - source-reading
  - metpo-primary
- assessment_id: canonical-examples
  area: quantity
  topic: 'Native checklist: two exact taxon/source/optimum claims'
  outcome: concern
  target_ids:
  - METPO:1000442
  summary: Both species identities are positive. P.fragi remains unknown because the
    assigned AMTT body is unavailable. The assigned complete Ramon article does not
    identify P.sivasensis or W-6; the current low-temperature-growth note does not
    supply the required best-growth temperature. This is a citation-support gap, not
    biological impossibility.
  evidence_ids:
  - canonical
  - canonical-name-search
  - cold-primary
  - amtt-metadata
  - taxonomy-296
  - taxonomy-1880678
- assessment_id: source-support
  area: evidence
  topic: 'Native checklist: six works and all placements'
  outcome: unknown
  target_ids:
  - METPO:1000442
  summary: All assigned identities are verified. Selected membrane physics and yeast
    PUFA context do not establish every taxon or exact optimum. AMTT body-dependent
    statements remain unknown; detailed pathogen cold-survival, fitness, ROS-defense,
    AMR and intervention efficacy remain UNASSESSED_SCOPE.
  evidence_ids:
  - sources
  - source-identities
  - placements
  - notes
  - source-reading
  - source-access
- assessment_id: quotations
  area: evidence
  topic: 'Native checklist: four schema snippets and evidence notes'
  outcome: supported
  target_ids:
  - METPO:1000442
  summary: All four snippets are literal. Native abstract checks verify two and leave
    two inconclusive; retained author-repository PDF-derived text supplies the remaining
    literal matches. Literal occurrence does not validate adjacent causal or numerical
    claims.
  evidence_ids:
  - snippets
  - source-native
  - definition-primary
  - definition-text
  - mendoza-metadata
  - notes
- assessment_id: nodes
  area: representation
  topic: 'Native checklist: all fourteen current referents'
  outcome: supported
  target_ids:
  - METPO:1000442
  summary: Current temperature and fluidity referents are qualities or conditions,
    while adaptation and named PUFA biosynthesis retain process/pathway meanings.
    Osmolyte role versus material bearer is a qualified close mapping. ROS-level wording
    remains qualified; no extra facet or wrong-CURIE finding is inferred.
  evidence_ids:
  - nodes-edges
  - source-nodes-edges
  - pato-primary
  - chebi-primary
  - chebi-role
  - schema
  details: "{\n  \"grounding\": [\n    {\n      \"index\": 0,\n      \"node_id\":\
    \ \"temperature_optimum_low_trait\",\n      \"label\": \"temperature optimum low\"\
    ,\n      \"node_type\": \"TRAIT\",\n      \"grounding\": \"METPO:1000442\",\n\
    \      \"outcome\": \"supported\",\n      \"assessment\": \"Active exact temperature-optimum-low\
    \ bin; raw synonyms do not themselves prove scientific equivalence.\"\n    },\n\
    \    {\n      \"index\": 1,\n      \"node_id\": \"temperature_optimum\",\n   \
    \   \"label\": \"temperature optimum\",\n      \"node_type\": \"TRAIT\",\n   \
    \   \"grounding\": \"METPO:1000304\",\n      \"outcome\": \"supported\",\n   \
    \   \"assessment\": \"Active direct temperature-optimum parent.\"\n    },\n  \
    \  {\n      \"index\": 2,\n      \"node_id\": \"cool_environment\",\n      \"\
    label\": \"cool environment\",\n      \"node_type\": \"ENVIRONMENTAL_FACTOR\"\
    ,\n      \"grounding\": null,\n      \"outcome\": \"supported\",\n      \"assessment\"\
    : \"Ambient cool condition, not automatically a process/event from enum.\"\n \
    \   },\n    {\n      \"index\": 3,\n      \"node_id\": \"psychrotolerant_adaptation\"\
    ,\n      \"label\": \"psychrotolerant adaptation\",\n      \"node_type\": \"BIOLOGICAL_PROCESS\"\
    ,\n      \"grounding\": null,\n      \"outcome\": \"supported\",\n      \"assessment\"\
    : \"Description denotes a generic adaptation process; exact physiological and\
    \ numeric-bin sufficiency remains source-dependent.\"\n    },\n    {\n      \"\
    index\": 4,\n      \"node_id\": \"low_temperature\",\n      \"label\": \"low temperature\"\
    ,\n      \"node_type\": \"ENVIRONMENTAL_FACTOR\",\n      \"grounding\": \"PATO:0001306\"\
    ,\n      \"outcome\": \"supported\",\n      \"assessment\": \"Relative low-temperature\
    \ quality/condition under close PATO mapping. Its current description does not\
    \ denote a temperature-decrease event; no independent enum/facet finding.\"\n\
    \    },\n    {\n      \"index\": 5,\n      \"node_id\": \"membrane_fluidity\"\
    ,\n      \"label\": \"membrane fluidity\",\n      \"node_type\": \"QUALITY\",\n\
    \      \"grounding\": \"METPO:1007505\",\n      \"outcome\": \"supported\",\n\
    \      \"assessment\": \"Explicit membrane-fluidity physical quality; local v3\
    \ and current QUALITY mapping agree.\"\n    },\n    {\n      \"index\": 6,\n \
    \     \"node_id\": \"membrane_unsaturation\",\n      \"label\": \"fatty-acyl unsaturation\"\
    ,\n      \"node_type\": \"QUALITY\",\n      \"grounding\": null,\n      \"outcome\"\
    : \"supported\",\n      \"assessment\": \"Degree of fatty-acyl unsaturation is\
    \ explicitly a quality, not biosynthesis activity.\"\n    },\n    {\n      \"\
    index\": 7,\n      \"node_id\": \"cold_shock_proteins\",\n      \"label\": \"\
    cold shock proteins\",\n      \"node_type\": \"GENE_OR_PROTEIN\",\n      \"grounding\"\
    : null,\n      \"outcome\": \"supported\",\n      \"assessment\": \"Material cold-shock\
    \ protein family. Reviewed label-only class is permitted; no fabricated instance\
    \ or accession required.\"\n    },\n    {\n      \"index\": 8,\n      \"node_id\"\
    : \"compatible_solutes\",\n      \"label\": \"compatible solutes\",\n      \"\
    node_type\": \"CHEMICAL\",\n      \"grounding\": \"CHEBI:25728\",\n      \"outcome\"\
    : \"qualified\",\n      \"assessment\": \"CHEBI25728 is an osmolyte biological\
    \ role, while current node denotes solute bearers. Maintained closeMatch supports\
    \ a functional grouping with explicit role/bearer qualification; not exact material\
    \ identity and no separately confirmed replacement finding.\"\n    },\n    {\n\
    \      \"index\": 9,\n      \"node_id\": \"protein_membrane_stabilization\",\n\
    \      \"label\": \"protein and membrane stabilization\",\n      \"node_type\"\
    : \"BIOLOGICAL_PROCESS\",\n      \"grounding\": null,\n      \"outcome\": \"supported\"\
    ,\n      \"assessment\": \"Stabilization and freezing-point-depression description\
    \ denotes processes; detailed efficacy unassessed.\"\n    },\n    {\n      \"\
    index\": 10,\n      \"node_id\": \"ice_binding_proteins\",\n      \"label\": \"\
    ice-binding/antifreeze proteins\",\n      \"node_type\": \"GENE_OR_PROTEIN\",\n\
    \      \"grounding\": null,\n      \"outcome\": \"supported\",\n      \"assessment\"\
    : \"Material ice-binding protein class; reviewed label-only is not an automatic\
    \ completeness defect.\"\n    },\n    {\n      \"index\": 11,\n      \"node_id\"\
    : \"ice_crystal_growth\",\n      \"label\": \"ice crystal growth\",\n      \"\
    node_type\": \"BIOLOGICAL_PROCESS\",\n      \"grounding\": null,\n      \"outcome\"\
    : \"supported\",\n      \"assessment\": \"Ice-crystal growth/recrystallization\
    \ process is explicit.\"\n    },\n    {\n      \"index\": 12,\n      \"node_id\"\
    : \"oxidative_stress\",\n      \"label\": \"oxidative stress\",\n      \"node_type\"\
    : \"BIOLOGICAL_PROCESS\",\n      \"grounding\": null,\n      \"outcome\": \"qualified\"\
    ,\n      \"assessment\": \"Label/type indicate oxidative-stress process while\
    \ description emphasizes elevated ROS. Process versus resulting ROS-level wording\
    \ remains bounded; the low-temperature quality subject independently establishes\
    \ edge8 role mismatch. Detailed ROS biology UNASSESSED_SCOPE.\"\n    },\n    {\n\
    \      \"index\": 13,\n      \"node_id\": \"pufa_biosynthesis\",\n      \"label\"\
    : \"PUFA biosynthesis\",\n      \"node_type\": \"PATHWAY\",\n      \"grounding\"\
    : null,\n      \"outcome\": \"supported\",\n      \"assessment\": \"Named polyunsaturated-fatty-acid\
    \ biosynthetic route is compatible with maintained pathway-like mechanism policy\
    \ and exact shared node-ID migration decision.\"\n    }\n  ],\n  \"source\": [\n\
    \    {\n      \"index\": 0,\n      \"node_id\": \"temperature_optimum_low_trait\"\
    ,\n      \"node_type\": \"TRAIT\",\n      \"outcome\": \"UNKNOWN_NUMERIC_CALIBRATION\"\
    ,\n      \"assessment\": \"Current10–22 optimum is an explicit local bin; sources\
    \ do not supply exact calibration.\"\n    },\n    {\n      \"index\": 1,\n   \
    \   \"node_id\": \"temperature_optimum\",\n      \"node_type\": \"TRAIT\",\n \
    \     \"outcome\": \"SUPPORTED_MEASUREMENT_CONCEPT\",\n      \"assessment\": \"\
    Growth optimum is distinct from temperature range, exposure or survival.\"\n \
    \   },\n    {\n      \"index\": 2,\n      \"node_id\": \"cool_environment\",\n\
    \      \"node_type\": \"ENVIRONMENTAL_FACTOR\",\n      \"outcome\": \"SUPPORTED_GENERIC_CONTEXT\"\
    ,\n      \"assessment\": \"Habitat temperature is environmental context, not measured\
    \ organism optimum.\"\n    },\n    {\n      \"index\": 3,\n      \"node_id\":\
    \ \"psychrotolerant_adaptation\",\n      \"node_type\": \"BIOLOGICAL_PROCESS\"\
    ,\n      \"outcome\": \"UNKNOWN_CAUSAL_SCOPE\",\n      \"assessment\": \"Generic\
    \ membrane/protein adaptation is source context, not sufficient proof of a precise\
    \ optimum.\"\n    },\n    {\n      \"index\": 4,\n      \"node_id\": \"low_temperature\"\
    ,\n      \"node_type\": \"ENVIRONMENTAL_FACTOR\",\n      \"outcome\": \"SUPPORTED_GENERIC_PHYSICAL_CONTEXT\"\
    ,\n      \"assessment\": \"Cool ambient temperature is contextual; formal PATO\
    \ referent assessed separately.\"\n    },\n    {\n      \"index\": 5,\n      \"\
    node_id\": \"membrane_fluidity\",\n      \"node_type\": \"QUALITY\",\n      \"\
    outcome\": \"SUPPORTED_GENERIC_PHYSICAL_CONTEXT\",\n      \"assessment\": \"Membrane-fluidity\
    \ physical quality is supported by selected Spectrum introduction.\"\n    },\n\
    \    {\n      \"index\": 6,\n      \"node_id\": \"membrane_unsaturation\",\n \
    \     \"node_type\": \"QUALITY\",\n      \"outcome\": \"SUPPORTED_GENERIC_PHYSICAL_CONTEXT\"\
    ,\n      \"assessment\": \"Degree of unsaturation is composition/property context;\
    \ process roles separately assessed.\"\n    },\n    {\n      \"index\": 7,\n \
    \     \"node_id\": \"cold_shock_proteins\",\n      \"node_type\": \"GENE_OR_PROTEIN\"\
    ,\n      \"outcome\": \"UNASSESSED_SCOPE\",\n      \"assessment\": \"AMTT identity\
    \ positive, body inaccessible; detailed cold-response/fitness assessment excluded.\"\
    \n    },\n    {\n      \"index\": 8,\n      \"node_id\": \"compatible_solutes\"\
    ,\n      \"node_type\": \"CHEMICAL\",\n      \"outcome\": \"UNKNOWN_NEAREST_SOURCE\"\
    ,\n      \"assessment\": \"Existing solute list not verified from assigned accessible\
    \ abstract; no body-absence inference.\"\n    },\n    {\n      \"index\": 9,\n\
    \      \"node_id\": \"protein_membrane_stabilization\",\n      \"node_type\":\
    \ \"BIOLOGICAL_PROCESS\",\n      \"outcome\": \"UNKNOWN_NEAREST_SOURCE\",\n  \
    \    \"assessment\": \"Existing stabilization/freezing-point explanation not verified\
    \ against assigned body.\"\n    },\n    {\n      \"index\": 10,\n      \"node_id\"\
    : \"ice_binding_proteins\",\n      \"node_type\": \"GENE_OR_PROTEIN\",\n     \
    \ \"outcome\": \"UNKNOWN_NEAREST_SOURCE\",\n      \"assessment\": \"Existing ice-binding\
    \ protein attribution not verified against assigned body; no compulsory example.\"\
    \n    },\n    {\n      \"index\": 11,\n      \"node_id\": \"ice_crystal_growth\"\
    ,\n      \"node_type\": \"BIOLOGICAL_PROCESS\",\n      \"outcome\": \"SUPPORTED_GENERIC_PHYSICAL_CONTEXT\"\
    ,\n      \"assessment\": \"Ice growth is physical context; source-specific inhibition\
    \ remains unknown.\"\n    },\n    {\n      \"index\": 12,\n      \"node_id\":\
    \ \"oxidative_stress\",\n      \"node_type\": \"BIOLOGICAL_PROCESS\",\n      \"\
    outcome\": \"UNASSESSED_SCOPE\",\n      \"assessment\": \"Detailed oxidative-stress/ROS-defense\
    \ branch is not scientifically adjudicated.\"\n    },\n    {\n      \"index\"\
    : 13,\n      \"node_id\": \"pufa_biosynthesis\",\n      \"node_type\": \"PATHWAY\"\
    ,\n      \"outcome\": \"SUPPORTED_GENERIC_CONTEXT\",\n      \"assessment\": \"\
    Named PUFA pathway has generic yeast membrane context; no new intervention or\
    \ universal optimum claim.\"\n    }\n  ]\n}"
- assessment_id: relations
  area: consistency
  topic: 'Native checklist: all ten current relations'
  outcome: concern
  target_ids:
  - METPO:1000442
  summary: 'The RO group is limited to edges 3, 7 and 8: explicit quality or material
    subjects conflict with inherited process roles, with quality objects additionally
    relevant at edge 3. Local confers, subclass and five lexical relations receive
    no invented imported constraints. Source efficacy remains separate.'
  evidence_ids:
  - nodes-edges
  - source-nodes-edges
  - ro-primary
  - pato-primary
  - local-authority
  - adjudication
  details: "{\n  \"grounding\": [\n    {\n      \"index\": 0,\n      \"subject\":\
    \ \"cool_environment\",\n      \"predicate\": \"engages\",\n      \"predicate_id\"\
    : null,\n      \"object\": \"psychrotolerant_adaptation\",\n      \"outcome\"\
    : \"unknown\",\n      \"assessment\": \"Ungrounded lexical engages has no imported\
    \ domain/range. Generic environmental-to-adaptation assertion requires source\
    \ support.\"\n    },\n    {\n      \"index\": 1,\n      \"subject\": \"psychrotolerant_adaptation\"\
    ,\n      \"predicate\": \"confers\",\n      \"predicate_id\": \"METPO:2007700\"\
    ,\n      \"object\": \"temperature_optimum_low_trait\",\n      \"outcome\": \"\
    supported\",\n      \"assessment\": \"Local confers broad causal-node endpoints\
    \ and trait-object prose fit current adaptation process/trait; exact-bin causal\
    \ calibration remains separate.\"\n    },\n    {\n      \"index\": 2,\n      \"\
    subject\": \"temperature_optimum_low_trait\",\n      \"predicate\": \"is a\",\n\
    \      \"predicate_id\": \"rdfs:subClassOf\",\n      \"object\": \"temperature_optimum\"\
    ,\n      \"outcome\": \"supported\",\n      \"assessment\": \"Current bin is a\
    \ subclass of its explicit active temperature-optimum parent.\"\n    },\n    {\n\
    \      \"index\": 3,\n      \"subject\": \"membrane_unsaturation\",\n      \"\
    predicate\": \"increases\",\n      \"predicate_id\": \"RO:0002213\",\n      \"\
    object\": \"membrane_fluidity\",\n      \"outcome\": \"concern\",\n      \"assessment\"\
    : \"RO2213 inherits RO2211 process domain/range. Both current unsaturation and\
    \ membrane-fluidity referents are explicit qualities, so the grounded assertion\
    \ conflicts with inherited roles.\"\n    },\n    {\n      \"index\": 4,\n    \
    \  \"subject\": \"low_temperature\",\n      \"predicate\": \"induces\",\n    \
    \  \"predicate_id\": null,\n      \"object\": \"cold_shock_proteins\",\n     \
    \ \"outcome\": \"unknown\",\n      \"assessment\": \"Lexical induces has no imported\
    \ RO domain/range; no enum-only or invented predicate constraint. Biological efficacy\
    \ unassessed.\"\n    },\n    {\n      \"index\": 5,\n      \"subject\": \"low_temperature\"\
    ,\n      \"predicate\": \"promotes accumulation of\",\n      \"predicate_id\"\
    : null,\n      \"object\": \"compatible_solutes\",\n      \"outcome\": \"unknown\"\
    ,\n      \"assessment\": \"Lexical promotes accumulation of has no imported RO\
    \ constraints. Detailed accumulation/fitness efficacy is unassessed.\"\n    },\n\
    \    {\n      \"index\": 6,\n      \"subject\": \"compatible_solutes\",\n    \
    \  \"predicate\": \"stabilizes\",\n      \"predicate_id\": null,\n      \"object\"\
    : \"protein_membrane_stabilization\",\n      \"outcome\": \"unknown\",\n     \
    \ \"assessment\": \"Lexical stabilizes is not RO2326. Material-to-process wording\
    \ is not assigned imported contributes-to constraints; detailed biology unassessed.\"\
    \n    },\n    {\n      \"index\": 7,\n      \"subject\": \"ice_binding_proteins\"\
    ,\n      \"predicate\": \"inhibits\",\n      \"predicate_id\": \"RO:0002212\"\
    ,\n      \"object\": \"ice_crystal_growth\",\n      \"outcome\": \"concern\",\n\
    \      \"assessment\": \"RO2212 inherits process domain. Current ice-binding protein\
    \ subject is material; ice-crystal-growth process object is a positive range control.\"\
    \n    },\n    {\n      \"index\": 8,\n      \"subject\": \"low_temperature\",\n\
    \      \"predicate\": \"increases\",\n      \"predicate_id\": \"RO:0002213\",\n\
    \      \"object\": \"oxidative_stress\",\n      \"outcome\": \"concern\",\n  \
    \    \"assessment\": \"RO2213 inherits process domain; current PATO-grounded low-temperature\
    \ condition is a quality, not a decrease event. ROS object wording remains qualified\
    \ and is not needed to establish the subject mismatch.\"\n    },\n    {\n    \
    \  \"index\": 9,\n      \"subject\": \"pufa_biosynthesis\",\n      \"predicate\"\
    : \"maintains\",\n      \"predicate_id\": null,\n      \"object\": \"membrane_fluidity\"\
    ,\n      \"outcome\": \"unknown\",\n      \"assessment\": \"Lexical maintains\
    \ has no imported process-range constraint. Named biosynthetic pathway and fluidity-quality\
    \ referents are not automatically inconsistent without a grounded predicate.\"\
    \n    }\n  ],\n  \"source\": [\n    {\n      \"index\": 0,\n      \"subject\"\
    : \"cool_environment\",\n      \"predicate\": \"engages\",\n      \"object\":\
    \ \"psychrotolerant_adaptation\",\n      \"outcome\": \"SUPPORTED_GENERIC_CONTEXT_UNKNOWN_BIN\"\
    ,\n      \"assessment\": \"D’Amico supplied decreased-fluidity phrase supports\
    \ a generic cold physical challenge. It does not itself establish a10–22°C optimum\
    \ or all adaptation programs.\",\n      \"locator\": \"definition-metadata.json\
    \ abstract; definition-author-raw.txt introduction\"\n    },\n    {\n      \"\
    index\": 1,\n      \"subject\": \"psychrotolerant_adaptation\",\n      \"predicate\"\
    : \"confers\",\n      \"object\": \"temperature_optimum_low_trait\",\n      \"\
    outcome\": \"UNKNOWN_NUMERIC_CAUSAL_SCOPE\",\n      \"assessment\": \"Mendoza\
    \ explicitly supports greater unsaturation as temperature decreases. The claim\
    \ that adaptation yields a10–22°C organism optimum is not established by the inspected\
    \ abstract.\",\n      \"locator\": \"mendoza-metadata.json abstract and retained\
    \ publisher abstract export\"\n    },\n    {\n      \"index\": 2,\n      \"subject\"\
    : \"temperature_optimum_low_trait\",\n      \"predicate\": \"is a\",\n      \"\
    object\": \"temperature_optimum\",\n      \"outcome\": \"UNKNOWN_NUMERIC_CALIBRATION\"\
    ,\n      \"assessment\": \"Parent-child measurement hierarchy is documentary;\
    \ freezing-point growth language does not calibrate an optimum10–22°C interval.\
    \ Growth, optimum and tolerance remain distinct.\",\n      \"locator\": \"definition-author-raw.txt\
    \ introduction\"\n    },\n    {\n      \"index\": 3,\n      \"subject\": \"membrane_unsaturation\"\
    ,\n      \"predicate\": \"increases\",\n      \"object\": \"membrane_fluidity\"\
    ,\n      \"outcome\": \"SUPPORTED_GENERIC_PHYSICAL_CONTEXT\",\n      \"assessment\"\
    : \"Selected Spectrum introduction describes temperature/composition dependence\
    \ of membrane fluidity and B.subtilis adaptation context. Broad transfer to every\
    \ taxon and exact optimum is not established; no intervention efficacy is audited.\"\
    ,\n      \"locator\": \"spectrum.xml zero-based bodyp1 and firsttwo sentences\
    \ bodyp2\"\n    },\n    {\n      \"index\": 4,\n      \"subject\": \"low_temperature\"\
    ,\n      \"predicate\": \"induces\",\n      \"object\": \"cold_shock_proteins\"\
    ,\n      \"outcome\": \"UNASSESSED_SCOPE\",\n      \"assessment\": \"AMTT identity\
    \ is verified but body unavailable. Existing CSP induction/threshold note is not\
    \ verified from accessible metadata; detailed cold-survival/fitness mechanism\
    \ assessment is excluded.\",\n      \"locator\": \"arrhenius-crossref.json identity/abstract;\
    \ historical403 responses\"\n    },\n    {\n      \"index\": 5,\n      \"subject\"\
    : \"low_temperature\",\n      \"predicate\": \"promotes accumulation of\",\n \
    \     \"object\": \"compatible_solutes\",\n      \"outcome\": \"UNKNOWN_NEAREST_SOURCE\"\
    ,\n      \"assessment\": \"AMTT abstract lacks the specified compatible-solute\
    \ list and accumulation attribution; body unavailable. No falsity or paperwide\
    \ absence inferred.\",\n      \"locator\": \"arrhenius-crossref.json abstract\"\
    \n    },\n    {\n      \"index\": 6,\n      \"subject\": \"compatible_solutes\"\
    ,\n      \"predicate\": \"stabilizes\",\n      \"object\": \"protein_membrane_stabilization\"\
    ,\n      \"outcome\": \"UNKNOWN_NEAREST_SOURCE\",\n      \"assessment\": \"Generic\
    \ physical stabilization/freezing-point attribution cannot be verified against\
    \ unavailable assigned AMTT body. No enhanced survival or intervention inference.\"\
    ,\n      \"locator\": \"arrhenius-crossref.json abstract\"\n    },\n    {\n  \
    \    \"index\": 7,\n      \"subject\": \"ice_binding_proteins\",\n      \"predicate\"\
    : \"inhibits\",\n      \"object\": \"ice_crystal_growth\",\n      \"outcome\"\
    : \"UNKNOWN_NEAREST_SOURCE\",\n      \"assessment\": \"Assigned AMTT body unavailable;\
    \ exact existing ice-binding explanation remains unverified. Formal protein/process\
    \ roles are separately reviewed.\",\n      \"locator\": \"arrhenius-crossref.json\
    \ abstract\"\n    },\n    {\n      \"index\": 8,\n      \"subject\": \"low_temperature\"\
    ,\n      \"predicate\": \"increases\",\n      \"object\": \"oxidative_stress\"\
    ,\n      \"outcome\": \"UNASSESSED_SCOPE\",\n      \"assessment\": \"Assigned\
    \ source identity verified; detailed oxidative-stress/ROS-defense/fitness branch\
    \ is not adjudicated, and body is unavailable.\",\n      \"locator\": \"arrhenius-crossref.json\
    \ identity\"\n    },\n    {\n      \"index\": 9,\n      \"subject\": \"pufa_biosynthesis\"\
    ,\n      \"predicate\": \"maintains\",\n      \"object\": \"membrane_fluidity\"\
    ,\n      \"outcome\": \"SUPPORTED_GENERIC_CONTEXT\",\n      \"assessment\": \"\
    Genes selected paragraph14 firstthree sentences directly describes PUFA-content\
    \ changes and membrane fluidity at low temperature. Study cohort is psychrophilic\
    \ yeasts; no universal bacterial or exact10–22 optimum transfer, and detailed\
    \ gene/fitness comparisons are not adopted.\",\n      \"locator\": \"genes.xml\
    \ zero-based .//body//p[14], firstthree sentences\"\n    }\n  ]\n}"
- assessment_id: completeness
  area: scope
  topic: 'Native checklist: quantitative graph and optional protein instances'
  outcome: supported
  target_ids:
  - METPO:1000442
  summary: Four components and two reviewed label-only protein classes with no instances
    are permitted in this NONMECHANISTIC quantitative overview. No forced connector,
    protein example or mechanism completion is requested.
  evidence_ids:
  - record
  - policy
  - schema
  - expression
- assessment_id: expression
  area: evidence
  topic: 'Native checklist: bounded catalog and unavailable query adapter'
  outcome: unknown
  target_ids:
  - METPO:1000442
  summary: Neither canonical species has an exact retained catalog match; other Pseudomonas
    datasets are not substitutes. B.subtilis source coverage is positive, but the
    appropriate generic query was not executed because the runner is unavailable within
    the searched roots. Primary fallback gives context only.
  evidence_ids:
  - expression
  - expression-discovery
  - source-reading
  - spectrum-primary
  - genes-primary
- assessment_id: recurrence
  area: consistency
  topic: 'Native checklist: current owners and conditional writers'
  outcome: supported
  target_ids:
  - METPO:1000442
  summary: Populated RO IDs belong to the current record; shared mappings can recur
    on empty fields while grounders skip current IDs. Seeder normally skips existing
    records, the release migration excludes this target, and the release finalizer
    writes reports only. Canonical backfill lacks a current exact plan entry. Sibling
    scripts and matching-line leads are qualified context.
  evidence_ids:
  - owners
  - owner-primary
  - alias-owner
  - discovery
  - predicate-mapping
  - node-mapping
- assessment_id: human
  area: provenance
  topic: 'Native checklist: attributable current acceptance'
  outcome: concern
  target_ids:
  - METPO:1000442
  summary: Nine embedded AI events plus a seed and the ignored-inclusive search of
    169 matching paths and 67 review target arrays do not establish current human
    acceptance. Four histories were read whole now and 14 prior whole readings were
    qualified by unchanged bytes; private or remote acceptance remains unknown.
  evidence_ids:
  - human-search
  - histories
  - owners
  - playbook
- assessment_id: readiness
  area: consistency
  topic: 'Native checklist: native checks, snapshots and chronology'
  outcome: supported
  target_ids:
  - METPO:1000442
  summary: All 100 captured inputs and 41 source plus 31 ground artifacts match. Focused
    native checks passed; qualified common diagnostics retain original executions,
    optional failures, retries and skips. Acquisition, extraction, copy and reading
    times remain separate.
  evidence_ids:
  - record
  - reuse
  - reuse-postcheck
  - local-init
  - source-native
  - source-reuse
  - ground-manifest
  - source-manifest
  - text-derivation
  - text-copy
findings:
- finding_id: imported-process-roles
  issue_key: temperature-optimum-low-imported-process-roles
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Imported regulation predicates conflict with current material and quality
    referents
  description: Three edges conflict with inherited RO process roles. RO:0002212 and
    RO:0002213 inherit RO:0002211 process domain and range. Edge 3 relates explicit
    unsaturation and membrane-fluidity qualities; edge 7 has a material ice-binding
    protein subject, although its ice-growth process object is compatible; edge 8
    has an explicitly low-temperature condition/quality subject, not a temperature-change
    event. The ENVIRONMENTAL_FACTOR enum alone is not the reason for that finding.
    ROS process-versus-level wording remains qualified and is not needed to establish
    the subject mismatch. Five lexical predicates have no imported formal roles and
    are not included.
  target_ids:
  - METPO:1000442
  field_paths:
  - causal_graphs[0].edges[3].predicate_id
  - causal_graphs[0].edges[7].predicate_id
  - causal_graphs[0].edges[8].predicate_id
  evidence_ids:
  - nodes-edges
  - ro-primary
  - pato-primary
  - owners
  - schema
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_optimum_low.yaml
    role: Current assertion or qualified conditional owner; preserve source provenance
      and existing writer guards.
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Current assertion or qualified conditional owner; preserve source provenance
      and existing writer guards.
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Current assertion or qualified conditional owner; preserve source provenance
      and existing writer guards.
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: psychrophile-exact-synonym-scope
  issue_key: temperature-optimum-low-psychrophile-exact-synonym-scope
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Exact Psychrophile alias exceeds the numerical optimum bin
  description: Psychrophile is declared an exact synonym of the 10–22 °C optimum bin.
    The assigned D’Amico review explicitly uses psychrophiles broadly and immediately
    includes Moritella profunda with maximal growth at 2 °C, outside that bin. This
    concrete source usage contradicts exact equivalence. The active METPO identifier,
    numeric restriction and faithful import of the upstream exact alias remain positive;
    the issue is inherited synonym scope, not a wrong identifier. Psychrotolerant
    exactness remains unresolved and is not counted as another finding.
  target_ids:
  - METPO:1000442
  field_paths:
  - synonyms[0].synonym_type
  evidence_ids:
  - classification
  - definition-primary
  - definition-text
  - identity
  - alias-owner
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_optimum_low.yaml
    role: Current assertion or qualified conditional owner; preserve source provenance
      and existing writer guards.
  - repository: CultureBotAI/TraitMech
    path: data/raw/metpo.owl
    role: Locked upstream source evidence; coordinate the accepted synonym scope without
      silently editing the vendored snapshot.
  - repository: CultureBotAI/TraitMech
    path: scripts/seed_from_metpo.py
    role: Current assertion or qualified conditional owner; preserve source provenance
      and existing writer guards.
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: canonical-source-attribution
  issue_key: temperature-optimum-low-canonical-source-attribution
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Assigned source does not establish the second canonical optimum claim
  description: The assigned Ramón review does not identify Pseudomonas sivasensis,
    sivasen variants or W-6/W6 in the retained complete parsed text. The current note
    also describes low-temperature growth without a reported 10–22 °C optimum. That
    citation does not establish the current exemplar-to-bin assertion. Official species
    identity is positive and is preserved; this is a bounded citation/measurement-support
    defect, not evidence that the organism lacks the phenotype. The inaccessible AMTT
    body for P. fragi remains UNKNOWN and does not receive this finding.
  target_ids:
  - METPO:1000442
  field_paths:
  - canonical_examples[1].reference
  - canonical_examples[1].note
  evidence_ids:
  - canonical
  - canonical-name-search
  - cold-primary
  - source-identities
  - owners
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_optimum_low.yaml
    role: Current assertion or qualified conditional owner; preserve source provenance
      and existing writer guards.
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: human-acceptance-link
  issue_key: temperature-optimum-low-human-acceptance-link
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Reviewed status lacks locally attributable acceptance
  description: Current REVIEWED status lacks attributable human acceptance of present
    assertions in the inspected local evidence. The ignored- and hidden-inclusive
    search, excluding .git and .venv, found 169 matching paths and 67 actual review
    target arrays with no exact target. Ten embedded events comprise nine AI events
    and one seed; the 18 captured history projections contain no exact-target history
    establishing acceptance. Private or remote acceptance remains unknown.
  target_ids:
  - METPO:1000442
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
    path: data/traits/environment/temperature_optimum_low.yaml
    role: Current assertion or qualified conditional owner; preserve source provenance
      and existing writer guards.
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
actions:
- action_id: resolve-imported-process-roles
  description: In separately authorized curation, reconcile the three grounded predicates
    with their actual material, condition and quality referents. Retain correctly
    described fluidity and unsaturation qualities. Review wildcard increases/inhibits
    mapping recurrence together with record assertions; the shared grounder skips
    current populated IDs, so rerunning it alone is not a fix. Sibling graph writers
    and process-quality/homeoviscous normalizers are not current sources of these
    assertions.
  finding_ids:
  - imported-process-roles
  target_ids:
  - METPO:1000442
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_optimum_low.yaml
    role: Current assertion or qualified conditional owner; preserve source provenance
      and existing writer guards.
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Current assertion or qualified conditional owner; preserve source provenance
      and existing writer guards.
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Current assertion or qualified conditional owner; preserve source provenance
      and existing writer guards.
  acceptance_checks:
  - Demonstrate compatible inherited domain/range with actual referents without inventing
    mechanisms or assigning RO rules to lexical predicates.
  - Retain NONMECHANISTIC scope, four components and two reviewed label-only protein
    classes; do not require token protein instances or connectors.
  - Run focused strict validation, relevant graph/predicate audits, full QC and required
    curation history/product gates.
- action_id: resolve-psychrophile-exact-synonym-scope
  description: Reconcile the inherited Psychrophile synonym scope with the upstream
    METPO term and document the local curation decision through the maintained ontology-source
    workflow. Preserve the active identifier, numeric-bin identity and upstream provenance.
    The vendored OWL path is evidence of upstream ownership, not an instruction to
    silently edit the locked snapshot. Fresh seeding copies exact scope but skips
    existing files unless forced; do not use forced reseeding as a repair. The three-alkaline-trait
    release migration excludes this target and the release finalizer writes review
    TSVs only.
  finding_ids:
  - psychrophile-exact-synonym-scope
  target_ids:
  - METPO:1000442
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_optimum_low.yaml
    role: Current assertion or qualified conditional owner; preserve source provenance
      and existing writer guards.
  - repository: CultureBotAI/TraitMech
    path: data/raw/metpo.owl
    role: Locked upstream source evidence; coordinate the accepted synonym scope without
      silently editing the vendored snapshot.
  - repository: CultureBotAI/TraitMech
    path: scripts/seed_from_metpo.py
    role: Current assertion or qualified conditional owner; preserve source provenance
      and existing writer guards.
  acceptance_checks:
  - The synonym relationship reflects the broader source usage, or a documented narrower
    sense is independently supported.
  - Track the upstream disposition and any curated local exception so future imports
    preserve the accepted scope; keep Psychrotolerant uncertainty separate.
  - Verify identifier/snapshot integrity and native strict, history and QC gates after
    separately authorized curation.
- action_id: resolve-canonical-source-attribution
  description: Resolve the exact primary citation and strain/organism attribution
    for the existing P. sivasensis example, and require a reported optimum within
    the bin rather than cold growth alone. If adequate evidence cannot be established,
    record an explicit evidence-gap disposition instead of retaining an unsupported
    canonical assertion. Keep source taxonomy and existing provenance; do not infer
    phenotype absence or automatically substitute another organism.
  finding_ids:
  - canonical-source-attribution
  target_ids:
  - METPO:1000442
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_optimum_low.yaml
    role: Current assertion or qualified conditional owner; preserve source provenance
      and existing writer guards.
  acceptance_checks:
  - The cited primary text identifies the example and supports its best-growth temperature
    in the defined bin, with any strain/assay limits explicit.
  - Preserve the separate UNKNOWN disposition for P. fragi until its own assigned
    source can be adequately inspected.
  - Validate canonical-reference fields, curation history and native strict/QC gates.
- action_id: resolve-human-acceptance-link
  description: Link attributable human acceptance of current assertions or reconcile
    REVIEWED through the native status workflow in separately authorized curation.
    Preserve existing AI actors and history.
  finding_ids:
  - human-acceptance-link
  target_ids:
  - METPO:1000442
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_optimum_low.yaml
    role: Current assertion or qualified conditional owner; preserve source provenance
      and existing writer guards.
  acceptance_checks:
  - Accepted assertion scope and human reviewer are attributable, or status reflects
    the available evidence.
  - Per-record and repository history validates and AI assistance remains explicit.
limitations:
- Exact10–22 optimum calibration and Psychrotolerant exact equivalence remain UNKNOWN.
  The separate Psychrophile exact-alias concern rests on the assigned D’Amico2°C optimum
  counterexample; active METPO identity and faithful inherited alias import remain
  positive. Ramón paragraph10 above20 wording alone does not prove an outside22 optimum.
- AMTT identity is positive via Crossref; current inherited arrhenius-* filenames
  are aliases for DOI10.37256/amtt.5220244537. EPMC zero-hit and historical403 PDF
  responses are diagnostic, not article bodies. P.fragi and detailed notes remain
  unknown/unassessed, not false.
- Canonical P.sivasensis assigned-source concern is limited to actual retained article/name-variant
  search and absent exact optimum attribution; no species-level biological impossibility
  or automatic replacement.
- Mendoza inspected abstract supports generic adaptation and literal unsaturation
  phrase, not a sufficient10–22 organism optimum.
- Spectrum scope is selected B.subtilis introductory physical context; Genes scope
  is selected generic yeast PUFA/fluidity context. Detailed gene contrasts, pathogenic
  cold-survival/fitness/ROS/AMR/defense/intervention efficacy remain UNASSESSED_SCOPE.
- No complete temperature-response curves acquired for either canonical example; low-temperature
  growth alone cannot substitute for best-growth temperature.
- Metadata notice fields contain no correction/retraction indication in inspected
  fields; not exhaustive publication-status clearance.
- Source catalog context includes benign B.subtilis and generic yeast cohort; no exact
  canonical, strain/module membership or biological effect inferred from catalog presence.
- Original access, extraction, prior copies and present copy/read clocks remain distinct.
  Whole text mechanical phrase/name searches do not claim whole-paper scientific reading.
- Raw exact synonyms are documentary identity facts, not independent proof of scientific
  synonym equivalence.
- Compatible-solute role grounding is qualified closeMatch, not exact material identity;
  no separate confirmed defect or replacement asserted.
- ROS process versus elevated-level wording and detailed biological efficacy remain
  unassessed/qualified; edge8 quality subject independently decides the role finding.
- Exact numeric-bin causal bridge, canonical citation/optimum support and source literal
  attribution are separate source judgments.
- Eight uncaptured script leads and one uncaptured sibling history remain matching-line
  context, not complete-body scientific authority.
- Covered source B.subtilis has no currently available maintained structured runner
  within declared roots; primary fallback and catalog scope do not imply absence of
  modules.
- Private/remote human acceptance remains unknown.
- Root read all 18 history actor/target/event/read-mode projections; four current
  whole and fourteen qualified prior whole readings are agent scope, not new root
  whole-body readings.
- The exact Psychrophile alias concern is supported by a reported optimum outside
  the bin; it does not invalidate the active METPO class or justify a silent locked-OWL
  edit.
- Original source requests, PDF extraction, copy and reading times remain distinct.
  Browser failures are not article content and browser cache origin-fetch times remain
  unknown.
- Four literal snippet matches do not validate the adjacent numerical or sufficient-causal
  interpretation. Native abstract verification returned two VERIFIED and two inconclusive
  results.
notes:
- Whole 283-line current target and 100 captured inputs; six works, 14 external placements,
  10 grounding fields, four literal snippets and 11 evidence notes.
- Original primary acquisitions, extraction and later copies are distinct. Legacy
  arrhenius filenames identify the assigned AMTT work, not an extra source.
- Grounding history scope is four current whole files plus 14 qualified prior whole
  readings; uncaptured leads remain matching-line context only.
- Root owns eventual single serialization, actual-output review, native validation
  and save. This preparation did not execute or import the serializer.
tags:
- record-review
- temperature-optimum-low
- environment
- needs-curation
```
