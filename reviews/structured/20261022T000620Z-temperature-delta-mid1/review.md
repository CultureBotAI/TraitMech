# Whole-record review of temperature delta mid1

- Review: 20261022T000620Z-temperature-delta-mid1
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-22T00:00:45.403117Z
- Finished UTC: 2026-10-22T00:06:20Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Whole-record review finds one grouped formal relation-role major and one human-acceptance minor. The canonical 15 °C growth breadth and three literal snippets are positive; exact numerical causal attribution and Noll body wording remain unknown.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: Fifth record of the actual local batch 013 queue. Whole 250-line target and 91 captured inputs verified before judgment; local review does not assert remote publication.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8eee04a8c65609fbaff6df7c54597dcaf1b9d282.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| METPO:1000485 | data/traits/environment/temperature_delta_mid1.yaml | maintained | temperature delta mid1 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full-corpus graph audit | passed | True | METPO:1000485 | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| Full-corpus snippet audit | passed | True | METPO:1000485 | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| Full-corpus pathway links | passed | True | METPO:1000485 | 19 links checked against the pinned PathwayMech snapshot. |
| Full-corpus history integrity | passed | True | METPO:1000485 | 1277 history records checked, zero invalid links at the 8eee source base; integrity does not establish science or human acceptance. |
| Initial full-product validation | failed | False | METPO:1000485 | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation with isolated local cache | failed | False | METPO:1000485 | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation after isolated-cache download | passed | True | METPO:1000485 | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| Focused native validation | passed | True | METPO:1000485 | Native record validation passed; scientific interpretation is assessed separately. |
| Focused strict validation | passed | True | METPO:1000485 | The actual validate-strict command passed. |
| Focused network snippet check | passed | True | METPO:1000485 | Three snippets over two references were VERIFIED; independent manual checks also support all three literal fragments. |
| Qualified batch-twelve QC | passed | True | METPO:1000485 | Actual prior QC qualified against B13 bytes; this is not a new B13 QC execution or publication. |
| Protein-instance metadata applicability | not_applicable | False | METPO:1000485 | Zero protein classes or instances in this quantitative NONMECHANISTIC overview; no token protein requirement. |

## Scientific And Domain Assessments

### Native checklist: active identity and hierarchy

identity: supported. Targets: METPO:1000485.

Active METPO:1000485, parent 1000303 and related Td_10_20 align with the inclusive 10–20 Cel existential restriction. Local v3/v4/v8 identifiers retain proposal status.

### Native checklist: numerical source calibration

quantity: unknown. Targets: METPO:1000485.

Inspected generic membrane and high-temperature sources do not establish the exact 10–20 °C class calibration or moderate-flexibility causal bridge. The OWL class restriction is not experimental validation.

### Native checklist: reported growth breadth

quantity: supported. Targets: METPO:1000485.

The actual indexed abstract reports Pontibacterium sinense N1Y112T growth from 20 to 35 °C, giving a 15 °C breadth inside this bin. Official taxonomy supports identity separately; no optimum-only or survival inference, and no full-paper reading claim.

### Native checklist: six works and twelve placements

evidence: unknown. Targets: METPO:1000485.

Source identities and selected generic physical attribution are positive. Noll body-level wording and exact quantitative sufficiency remain unknown; failed retrievals and an empty indexed search do not refute the source.

### Native checklist: three supplied fragments

evidence: supported. Targets: METPO:1000485.

All three supplied snippets are literal in inspected abstracts and passed native verification. Their adjacent numerical or causal interpretations are assessed separately.

### Native checklist: all eleven current referents

representation: unknown. Targets: METPO:1000485.

Current traits, membrane-fluidity quality and explicit process facets are supported. Moderate-capacity wording at node 2 and property/class interpretation at node 9 remain qualified; no forced reservoir CAPACITY retype.

{
  "grounding": [
    {
      "index": 0,
      "node_id": "temperature_delta_mid1_trait",
      "label": "temperature delta mid1",
      "node_type": "TRAIT",
      "grounding": "METPO:1000485",
      "outcome": "supported",
      "assessment": "Active exact 10–20 inclusive temperature-breadth bin."
    },
    {
      "index": 1,
      "node_id": "temperature_delta",
      "label": "temperature delta",
      "node_type": "TRAIT",
      "grounding": "METPO:1000303",
      "outcome": "supported",
      "assessment": "Active parent temperature-delta class 1000303."
    },
    {
      "index": 2,
      "node_id": "moderate_thermal_adaptation",
      "label": "moderate thermal-adaptation flexibility",
      "node_type": "BIOLOGICAL_PROCESS",
      "grounding": null,
      "outcome": "unknown",
      "assessment": "Mid-range remodeling capacity may be a disposition or process shorthand. Do not force reservoir CAPACITY enum or count a separate finding without disambiguation."
    },
    {
      "index": 3,
      "node_id": "temperature_decrease",
      "label": "decrease in ambient temperature",
      "node_type": "ENVIRONMENTAL_FACTOR",
      "grounding": null,
      "outcome": "supported",
      "assessment": "Current description denotes a drop in ambient growth temperature, so an event/process reading is available; environmental enum alone is not exclusionary."
    },
    {
      "index": 4,
      "node_id": "membrane_unsaturated_fatty_acids",
      "label": "membrane unsaturated fatty acids",
      "node_type": "CHEMICAL",
      "grounding": null,
      "outcome": "supported",
      "assessment": "Cis-unsaturated membrane acyl chains are material chemicals. Current description and type agree; no unsupported GO/CHEBI grounding is invented."
    },
    {
      "index": 5,
      "node_id": "membrane_fluidity",
      "label": "membrane fluidity",
      "node_type": "QUALITY",
      "grounding": "METPO:1007505",
      "outcome": "supported",
      "assessment": "Explicit physical bilayer fluidity is a QUALITY; exact v3 row and current node mapping support identity, distinct from the maintenance process."
    },
    {
      "index": 6,
      "node_id": "ufa_biosynthesis",
      "label": "cis-unsaturated fatty acid biosynthesis",
      "node_type": "BIOLOGICAL_PROCESS",
      "grounding": null,
      "outcome": "supported",
      "assessment": "Synthesis is an explicit biological process; no protein-instance requirement."
    },
    {
      "index": 7,
      "node_id": "membrane_physical_state_change",
      "label": "membrane physical-state change",
      "node_type": "BIOLOGICAL_PROCESS",
      "grounding": null,
      "outcome": "supported",
      "assessment": "Change of physical state is described as a process/event, distinct from the static quality."
    },
    {
      "index": 8,
      "node_id": "two_component_cold_signaling",
      "label": "two-component cold signaling",
      "node_type": "BIOLOGICAL_PROCESS",
      "grounding": null,
      "outcome": "supported",
      "assessment": "Signaling activity is an explicit process; no material-protein interpretation is imposed."
    },
    {
      "index": 9,
      "node_id": "thermal_niche_breadth",
      "label": "thermal niche / temperature breadth",
      "node_type": "QUALITY",
      "grounding": null,
      "outcome": "unknown",
      "assessment": "Thermal niche/breadth is a measured property bounded by growth conditions. Quantity versus interval wording and its class-level relation to the phenotype remain qualifications; QUALITY alone does not prove a wrong class assertion."
    },
    {
      "index": 10,
      "node_id": "tmin_tmax",
      "label": "Tmin and Tmax growth boundaries",
      "node_type": "QUALITY",
      "grounding": null,
      "outcome": "supported",
      "assessment": "Cardinal minimum/maximum growth temperatures are defining measurement boundaries; no process or material identity is implied."
    }
  ],
  "source": [
    {
      "index": 0,
      "field": "causal_graphs[0].nodes[0]",
      "node_id": "temperature_delta_mid1_trait",
      "outcome": "unknown",
      "assessment": "Explicit10–20 bin; exact assigned-source calibration remains unresolved."
    },
    {
      "index": 1,
      "field": "causal_graphs[0].nodes[1]",
      "node_id": "temperature_delta",
      "outcome": "supported_at_definition_scope",
      "assessment": "Growth breadth is distinct from optimum or survival; canonical arithmetic is positive."
    },
    {
      "index": 2,
      "field": "causal_graphs[0].nodes[2]",
      "node_id": "moderate_thermal_adaptation",
      "outcome": "unknown",
      "assessment": "Mid-range membrane/enzyme capacity is a record synthesis not directly established as10–20 sufficiency by inspected sources."
    },
    {
      "index": 3,
      "field": "causal_graphs[0].nodes[3]",
      "node_id": "temperature_decrease",
      "outcome": "supported_at_generic_scope",
      "assessment": "Cooling is the physical context of the assigned abstracts and selected introductory text."
    },
    {
      "index": 4,
      "field": "causal_graphs[0].nodes[4]",
      "node_id": "membrane_unsaturated_fatty_acids",
      "outcome": "qualified_generic_support",
      "assessment": "Cis-unsaturated lipid composition context is supported, without a universal response or detailed taxon efficacy inference."
    },
    {
      "index": 5,
      "field": "causal_graphs[0].nodes[5]",
      "node_id": "membrane_fluidity",
      "outcome": "supported_at_generic_scope",
      "assessment": "Membrane fluidity is the physical property discussed; formal facet roles are separately audited."
    },
    {
      "index": 6,
      "field": "causal_graphs[0].nodes[6]",
      "node_id": "ufa_biosynthesis",
      "outcome": "qualified_generic_support",
      "assessment": "Generic unsaturated synthesis/composition attribution is present; detailed pathway output/efficacy unassessed."
    },
    {
      "index": 7,
      "field": "causal_graphs[0].nodes[7]",
      "node_id": "membrane_physical_state_change",
      "outcome": "supported_at_attribution_scope",
      "assessment": "Cold-review abstract names liquid-crystalline state change as sensing context; no detailed sensor efficacy judgment."
    },
    {
      "index": 8,
      "field": "causal_graphs[0].nodes[8]",
      "node_id": "two_component_cold_signaling",
      "outcome": "supported_at_attribution_scope",
      "assessment": "Two-component activation is explicitly attributed in the review abstract; detailed signaling mechanisms/fitness are outside scope."
    },
    {
      "index": 9,
      "field": "causal_graphs[0].nodes[9]",
      "node_id": "thermal_niche_breadth",
      "outcome": "unknown",
      "assessment": "Thermal niche as a bounded growth quantity is readable in record; nearest Noll body attribution is not verified."
    },
    {
      "index": 10,
      "field": "causal_graphs[0].nodes[10]",
      "node_id": "tmin_tmax",
      "outcome": "unknown",
      "assessment": "Minimum/maximum growth boundaries are explicit record referents; nearest assigned Noll body wording remains unavailable."
    }
  ]
}

### Native checklist: all nine current relations

consistency: concern. Targets: METPO:1000485.

Edges 3/4/6 form one imported-role group: RO2213 conflicts with chemical/quality endpoints, and RO2327 conflicts with a quality subject. Edge 2 can denote a temperature-decrease event; edge 5 has process endpoints. Local defines and RDFS subclass modeling at 7/8 remain qualifications, not automatic enum failures.

{
  "grounding": [
    {
      "index": 0,
      "subject": "moderate_thermal_adaptation",
      "predicate": "confers",
      "predicate_id": "METPO:2007700",
      "object": "temperature_delta_mid1_trait",
      "outcome": "supported",
      "assessment": "Local v8 broad formal causal-node roles and trait object fit. The exact quantitative causal bridge remains independently source-assessed, not proven by formal fit."
    },
    {
      "index": 1,
      "subject": "temperature_delta_mid1_trait",
      "predicate": "is a",
      "predicate_id": "rdfs:subClassOf",
      "object": "temperature_delta",
      "outcome": "supported",
      "assessment": "Exact imported 1000485 subclass 1000303 is positive."
    },
    {
      "index": 2,
      "subject": "temperature_decrease",
      "predicate": "increases",
      "predicate_id": "RO:0002213",
      "object": "ufa_biosynthesis",
      "outcome": "unknown",
      "assessment": "RO2213 inherits process/process roles. A temperature-decrease event can satisfy the subject interpretation, and the object is an explicit biosynthetic process; no enum-only categorical error. Biological efficacy/universality unassessed."
    },
    {
      "index": 3,
      "subject": "ufa_biosynthesis",
      "predicate": "increases",
      "predicate_id": "RO:0002213",
      "object": "membrane_unsaturated_fatty_acids",
      "outcome": "concern",
      "assessment": "RO2213 inherits process range via RO2211, but the object is material unsaturated acyl chains rather than a process. The explicit biosynthetic subject is compatible."
    },
    {
      "index": 4,
      "subject": "membrane_unsaturated_fatty_acids",
      "predicate": "increases",
      "predicate_id": "RO:0002213",
      "object": "membrane_fluidity",
      "outcome": "concern",
      "assessment": "RO2213 process/process roles conflict with a material-chemical subject and physical-quality object. This is formal representation, not a claim that the biological direction is false."
    },
    {
      "index": 5,
      "subject": "membrane_physical_state_change",
      "predicate": "activates",
      "predicate_id": "RO:0002213",
      "object": "two_component_cold_signaling",
      "outcome": "supported",
      "assessment": "Physical-state change and signaling are explicitly processual, so imported process endpoints fit. Detailed cold-response efficacy is unassessed."
    },
    {
      "index": 6,
      "subject": "membrane_fluidity",
      "predicate": "enables",
      "predicate_id": "RO:0002327",
      "object": "moderate_thermal_adaptation",
      "outcome": "concern",
      "assessment": "RO2327 inherits material-entity subject via RO2215/2216/2500/2595. Membrane fluidity is an explicit QUALITY, not its material bearer. Moderate-process/capacity wording of the object is separately qualified; the subject mismatch is independently firm."
    },
    {
      "index": 7,
      "subject": "tmin_tmax",
      "predicate": "defines",
      "predicate_id": "METPO:2007500",
      "object": "thermal_niche_breadth",
      "outcome": "unknown",
      "assessment": "Local v4 defines has broad formal causal-node endpoints. Cardinal boundaries operationally identify thermal breadth; object QUALITY versus trait-class prose and interval/width distinction remain bounded modeling qualifications, not an invented hard domain failure."
    },
    {
      "index": 8,
      "subject": "thermal_niche_breadth",
      "predicate": "is a",
      "predicate_id": "rdfs:subClassOf",
      "object": "temperature_delta",
      "outcome": "unknown",
      "assessment": "RDFS subclass is class-level; both graph concepts may be class representations. Current measured thermal-breadth property and temperature-delta phenotype are closely scoped, but the property/class interpretation is not fully explicit. No automatic quality-to-trait error or source measurement claim is imposed."
    }
  ],
  "source": [
    {
      "index": 0,
      "field": "causal_graphs[0].edges[0]",
      "subject": "moderate_thermal_adaptation",
      "object": "temperature_delta_mid1_trait",
      "outcome": "unknown",
      "assessment": "UNKNOWN: inspected generic membrane or high-temperature context does not establish the exact 10–20 °C class calibration or moderate-flexibility causal bridge. Unavailable bodies are not paper-wide absence or biological refutation.",
      "formal_role_scope": "Separate grounding audit; literal or generic source support does not validate imported predicate roles."
    },
    {
      "index": 1,
      "field": "causal_graphs[0].edges[1]",
      "subject": "temperature_delta_mid1_trait",
      "object": "temperature_delta",
      "outcome": "unknown",
      "assessment": "UNKNOWN: inspected generic membrane or high-temperature context does not establish the exact 10–20 °C class calibration or moderate-flexibility causal bridge. Unavailable bodies are not paper-wide absence or biological refutation.",
      "formal_role_scope": "Separate grounding audit; literal or generic source support does not validate imported predicate roles."
    },
    {
      "index": 2,
      "field": "causal_graphs[0].edges[2]",
      "subject": "temperature_decrease",
      "object": "ufa_biosynthesis",
      "outcome": "qualified_generic_support",
      "assessment": "Cold-review abstract clause(ii) and actual HTML p20 first sentence support unsaturation/cis-MUFA context. This is generic attribution; taxon-specific regulation, universal efficacy or a measured10–20 breadth are not established.",
      "formal_role_scope": "Separate grounding audit; literal or generic source support does not validate imported predicate roles."
    },
    {
      "index": 3,
      "field": "causal_graphs[0].edges[3]",
      "subject": "ufa_biosynthesis",
      "object": "membrane_unsaturated_fatty_acids",
      "outcome": "qualified_generic_support",
      "assessment": "Cold-review abstract clause(ii) and actual HTML p20 first sentence support unsaturation/cis-MUFA context. This is generic attribution; taxon-specific regulation, universal efficacy or a measured10–20 breadth are not established.",
      "formal_role_scope": "Separate grounding audit; literal or generic source support does not validate imported predicate roles."
    },
    {
      "index": 4,
      "field": "causal_graphs[0].edges[4]",
      "subject": "membrane_unsaturated_fatty_acids",
      "object": "membrane_fluidity",
      "outcome": "qualified_generic_support",
      "assessment": "Spectrum introduction names homeoviscous adaptation and existing B.subtilis membrane-composition context. Generic physical attribution is retained; the note generalizable does not authorize a universal or detailed antimicrobial/strain efficacy assessment.",
      "formal_role_scope": "Separate grounding audit; literal or generic source support does not validate imported predicate roles."
    },
    {
      "index": 5,
      "field": "causal_graphs[0].edges[5]",
      "subject": "membrane_physical_state_change",
      "object": "two_component_cold_signaling",
      "outcome": "supported_at_attribution_scope",
      "assessment": "Cold-review abstract clause(i) explicitly places membrane liquid-crystalline-state change upstream of two-component activation. This verifies existing generic source attribution only; detailed sensing, pathway efficacy, pathogen fitness and intervention mechanisms are UNASSESSED_SCOPE.",
      "formal_role_scope": "Separate grounding audit; literal or generic source support does not validate imported predicate roles."
    },
    {
      "index": 6,
      "field": "causal_graphs[0].edges[6]",
      "subject": "membrane_fluidity",
      "object": "moderate_thermal_adaptation",
      "outcome": "unknown",
      "assessment": "UNKNOWN: inspected generic membrane or high-temperature context does not establish the exact 10–20 °C class calibration or moderate-flexibility causal bridge. Unavailable bodies are not paper-wide absence or biological refutation.",
      "formal_role_scope": "Separate grounding audit; literal or generic source support does not validate imported predicate roles."
    },
    {
      "index": 7,
      "field": "causal_graphs[0].edges[7]",
      "subject": "tmin_tmax",
      "object": "thermal_niche_breadth",
      "outcome": "unknown",
      "assessment": "Noll identity and generic temperature-modeling scope are verified. Exact body-level Tmin/Tmax flank/niche attribution is unresolved because inspected Crossref abstract does not supply that wording and public body routes failed. No paper-wide absence, false-citation finding, or mechanistic repair inferred.",
      "formal_role_scope": "Separate grounding audit; literal or generic source support does not validate imported predicate roles."
    },
    {
      "index": 8,
      "field": "causal_graphs[0].edges[8]",
      "subject": "thermal_niche_breadth",
      "object": "temperature_delta",
      "outcome": "unknown",
      "assessment": "Noll identity and generic temperature-modeling scope are verified. Exact body-level Tmin/Tmax flank/niche attribution is unresolved because inspected Crossref abstract does not supply that wording and public body routes failed. No paper-wide absence, false-citation finding, or mechanistic repair inferred.",
      "formal_role_scope": "Separate grounding audit; literal or generic source support does not validate imported predicate roles."
    }
  ]
}

### Native checklist: quantitative graph and biological limits

scope: unknown. Targets: METPO:1000485.

Two components and no protein classes or instances are proportionate to this NONMECHANISTIC overview. Generic classification, attribution and formal representation were reviewed; detailed pathogen survival, fitness, ROS/AMR, sensing or intervention efficacy remains UNASSESSED_SCOPE.

### Native checklist: bounded catalog applicability

evidence: unknown. Targets: METPO:1000485.

The retained 20-organism / 28-dataset catalog has no exact Pontibacterium taxon or strain-alias match. B. subtilis source-context coverage is separately positive. No universal source-species absence, strain transfer or detailed module query is claimed.

### Native checklist: conditional current writers

ownership: supported. Targets: METPO:1000485.

Shared grounding skips populated IDs. The membrane-fluidity migration already agrees with QUALITY. Exact canonical backfill is a no-op for matching existing examples and rejects unexpected populated values under its live-queue guard. Sibling and uncaptured matching-line leads are not current recurrence owners.

### Native checklist: attributable current acceptance

provenance: concern. Targets: METPO:1000485.

Eight AI events plus a seed and the ignored-inclusive 164-path / 67-array search do not establish current human acceptance. Twelve current history projections reuse twelve prior complete readings by exact hashes; no new whole-history reading is claimed. Private or remote acceptance remains unknown.

### Native checklist: checks and evidence chronology

consistency: supported. Targets: METPO:1000485.

All 91 inputs and frozen audits match. Focused native, strict and snippet checks passed. Qualified common diagnostics retain historical optional failures and 123 no-adapter skips. Original acquisitions, intervening copies and current readings remain distinct; no new B13 QC or publication is asserted.

## Findings

### imported-process-roles: Imported relation roles conflict with current referents

major / open / confirmed; issue key: temperature-delta-mid1-imported-process-roles.

RO:0002213 inherits process domain and range from RO:0002211. Edge3 has material acyl chains as its object, and edge4 relates those chemicals to a physical fluidity quality. Edge6 uses RO:0002327 with that explicit quality as subject despite its inherited material-entity domain through RO:0002215, RO:0002216, RO:0002500 and RO:0002595. These are formal representation conflicts, independent of biological efficacy. Edge2 can describe a temperature-decrease event, and edge5 has explicit process endpoints; neither is included.

### human-acceptance-link: Reviewed status lacks locally attributable acceptance

minor / open / confirmed; issue key: temperature-delta-mid1-human-acceptance-link.

Current REVIEWED status has no attributable human acceptance link in the inspected local evidence. The ignored- and hidden-inclusive search, excluding .git and .venv, found164 matching paths and67 actual review target arrays with no exact target. Nine embedded events comprise eight AI events and one seed event. This is a bounded non-blocking provenance gap; private or remote acceptance remains unknown.

## Recommended Actions And Acceptance Checks

### resolve-imported-process-roles

In separately authorized curation, align the selected relationship groundings with their actual process, material and quality referents. Review the shared mapping for future empty fields while preserving compatible event/process cases. The grounder skips populated IDs, so a mapping rerun alone cannot repair these current fields. Keep exact numerical source attribution unresolved until directly supported.

- Document compatible ontology roles for each current referent without asserting unreviewed biological efficacy.
- Preserve already-correct membrane-fluidity QUALITY and compatible process/event cases; do not assign sibling scripts as current owners.
- Run focused strict validation, relevant graph and predicate audits, full QC and required history/product gates after authorized curation.

### resolve-human-acceptance-link

Link attributable human acceptance of the current assertions, or reconcile REVIEWED through the native status workflow in separately authorized curation. Preserve existing actor attribution.

- The human reviewer and current accepted scope are attributable, or the status accurately reflects available evidence.
- Required per-record and repository history validates and AI assistance remains explicit.

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
| check-temperature-delta-mid1-validate | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-validate.log; Executed 2026-10-22T00:01:00.700665+00:00 through 2026-10-22T00:01:01.335375+00:00; metadata temperature-delta-mid1-validate.json | context_only | Native record validation passed; scientific interpretation is assessed separately. |
| check-temperature-delta-mid1-strict | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-strict.log; Executed 2026-10-22T00:01:00.700664+00:00 through 2026-10-22T00:01:01.799759+00:00; metadata temperature-delta-mid1-strict.json | context_only | The actual validate-strict command passed. |
| check-temperature-delta-mid1-snippets-network | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-snippets-network.log; Executed 2026-10-22T00:01:04.274210+00:00 through 2026-10-22T00:01:07.664523+00:00; metadata temperature-delta-mid1-snippets-network.json | context_only | Three snippets over two references were VERIFIED; independent manual checks also support all three literal fragments. |
| check-batch012-qc | /private/tmp/traitmech-record-sweep-012.j4n7q2vc/batch012-qc.log; Executed 2026-10-21T23:02:31.440808+00:00 through 2026-10-21T23:04:01.628423+00:00; metadata batch012-qc.json | context_only | Actual prior QC qualified against B13 bytes; this is not a new B13 QC execution or publication. |
| record | data/traits/environment/temperature_delta_mid1.yaml; Whole 250-line current record | supports | Eleven nodes, nine edges and nine embedded events; one canonical example and no protein examples. |
| reuse | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-b12-qc-supplement-qualified.json; Actual B12-to-B13 qualification | supports | Current byte comparisons retain original diagnostic failures, retries and skips. |
| reuse-postcheck | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-output-verification-agent/post-execution-verification.json; Independent actual-output verification | supports | Qualification verification, not new QC. |
| local-init | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/batch013-local-initialization-receipt.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Actual local initialization; publication remains a separate action. |
| policy | docs/GROUNDING_POLICY.md; Captured maintained authority | supports | Actual referents and optional protein applicability. |
| playbook | docs/CURATION_PLAYBOOK.md; Captured maintained authority | supports | Source scope and attributable acceptance. |
| schema | src/traitmech/schema/traitmech.yaml; Captured maintained authority | supports | Current facets and NONMECHANISTIC scope. |
| predicate-mapping | mappings/predicate_grounding.tsv; Captured maintained authority | supports | Shared mapping for future empty fields; populated IDs are skipped. |
| local-v8 | proposals/metpo_traitmech_v8/metpo_proposal_properties_robot.tsv; Captured maintained authority | supports | Confers has broad formal endpoints and trait-object context. |
| local-v3 | proposals/metpo_traitmech_v3/metpo_proposal_classes_robot.tsv; Captured maintained authority | supports | Exact local membrane-fluidity quality. |
| local-v4 | proposals/metpo_traitmech_v4/metpo_proposal_properties_robot.tsv; Captured maintained authority | supports | Operational defines relation has broad formal causal-node endpoints. |
| capture | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-ground-agent/capture-verification.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | All 91 inputs and whole target verified. |
| identity | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-ground-agent/identity-assessment.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Active identity, parent and inclusive numerical restriction. |
| nodes-edges | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-ground-agent/node-edge-grounding-ledger.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Every current node and edge, including formal positives and limitations. |
| owners | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-ground-agent/owner-provenance-assessment.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Exact current owners and conditional recurrence. |
| owner-primary | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-ground-agent/owner-primary-reading.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Actual shared grounder, current facet migration and canonical-entry guards. |
| human-search | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-ground-agent/search-and-provenance.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | 164 ignored-inclusive matching paths; 67 actual target arrays, zero exact target. |
| histories | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-ground-agent/history-reading-provenance.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Twelve current projections; all twelve prior complete readings qualified by identical current hashes. |
| discovery | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-ground-agent/discovery-disposition.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | One uncaptured history and one script lead remain matching-line-only context. |
| expression | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-ground-agent/expression-and-readiness.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Canonical Pontibacterium aliases lack exact retained catalog coverage; source B. subtilis coverage is separately positive. |
| local-authority | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-ground-agent/local-authority-reading.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Actual mapping/proposal rows and facet policies; no Biolink predicate occurs in the current graph. |
| ground-manifest | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-ground-agent/evidence-manifest.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Frozen grounding artifacts, all hashes verified. |
| metpo-primary | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/repo/data/raw/metpo.owl; Retained primary authority, locally read at the recorded time | supports | Active 1000485, parent 1000303 and inclusive 10–20 Cel existential restriction. |
| metpo-primary-projection | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-ground-agent/metpo-authority.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Selected statements with exact primary-byte provenance. |
| ro-primary | /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/ro.db; Retained primary authority, locally read at the recorded time | supports | Actual inherited material/process and process/process roles. |
| ro-primary-projection | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-ground-agent/selected-ro-primary-reading.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Selected statements with exact primary-byte provenance. |
| spectrum-metadata | DOI:10.1128/spectrum.03925-23; Indexed metadata | supports | Source identity and bounded notice fields. |
| cold-metadata | DOI:10.1007/s42770-023-01057-4; Indexed metadata | supports | Assigned general cold-review identity and bounded notice fields. |
| spectrum-body | DOI:10.1128/spectrum.03925-23; JATS body paragraph 0 named adaptation sentence and paragraph 2 introductory composition sentence, zero based | supports | Existing generic physical attribution only; detailed sensor, assay and antimicrobial efficacy unassessed. |
| cold-body | DOI:10.1007/s42770-023-01057-4; All HTML p elements, paragraph 20 first sentence; abstract clauses (i)/(ii) separately read | supports | Generic cis-unsaturation and source-attributed state-change context only; no detailed pathway or universal numerical-bin inference. |
| mendoza | DOI:10.1146/annurev-micro-091313-103612; Indexed abstract | supports | Generic membrane context and two supplied literal fragments; exact bin calibration unknown. |
| tolner | DOI:10.1016/s0300-9629(97)00003-0; Indexed abstract | supports | Generic high-temperature context and supplied fragment; no exact breadth calibration. |
| tolner-author | DOI:10.1016/s0300-9629(97)00003-0; Author institutional abstract page | supports | Generic opening and existing fragment only; not full article. |
| mendoza-browser | DOI:10.1146/annurev-micro-091313-103612; Actual browser export of publisher abstract; origin/cache-fetch time unknown | supports | Generic abstract support; retained tool output is not raw HTML or a full body. |
| canonical-primary | DOI:10.1099/ijsem.0.006018; Actual structured metadata/abstract response | supports | Current abstract explicitly reports N1Y112T growth 20–35 °C, supporting 15 °C breadth; full paper not inspected. |
| noll-primary | DOI:10.3390/pr8010121; Actual structured metadata/abstract response | supports | Official publication identity and abstract context only; exact Tmin/Tmax body wording is unknown. |
| noll-index-search | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.3390/pr8010121&amp;format=json&amp;resultType=core; Zero-hit indexed search; not a missing DOI or source refutation | context_only | Crossref independently verifies this DOI; no full body was acquired by this search. |
| taxonomy | NCBITaxon:2781979; Whole successful official taxonomy XML | supports | Pontibacterium sinense with N1Y112 type aliases; taxonomy establishes identity, not temperature phenotype. |
| taxonomy-access | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-ground-agent/taxonomy-network-retry-access.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Actual successful request after a retained DNS failure. |
| taxonomy-initial | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-ground-agent/taxonomy-access.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Initial failed request is diagnostic text, not primary XML. |
| sources | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-source-agent/source-assessment.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Six works; overall UNKNOWN and no source-only finding. |
| source-identities | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-source-agent/source-identities-status.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Exact source identities and bounded publication-status observations. |
| placements | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-source-agent/source-placement-ledger.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Twelve external placements and adjacent notes accounted for. |
| snippets | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-source-agent/snippet-ledger.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Three supplied snippets are literal; Noll body-level notes remain separately unknown. |
| source-nodes-edges | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-source-agent/node-edge-source-ledger.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Source judgments for every node and edge. |
| source-reading | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-source-agent/primary-reading-scope.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Selected abstracts and generic body sentences only; no whole-article claim. |
| source-access | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-source-agent/source-access-limits.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Unavailable bodies and retained retrieval diagnostics are not refutations. |
| source-reuse | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-source-agent/source-reuse-receipt.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Original acquisitions, current copies and current reads have distinct timestamps. |
| canonical | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-source-agent/canonical-assessment.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Reported 20–35 °C growth gives 15 °C breadth within this bin. |
| source-manifest | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-source-agent/evidence-manifest.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Frozen source artifacts, all hashes verified. |
| root-reading | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-source-root/root-reading.json; Derived audit or reading receipt; underlying primary bytes identified separately | supports | Root independent selected primary, full assessment and bounded history-projection readings. |
| root-browser-failure | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-source-root/noll-later-positioned-access.json; Later positioned browser attempt; actual tool clock bounds, no primary-body claim | context_only | The later Noll attempt returned 429; exact body attribution remains unknown. |
| adjudication | /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-root-adjudication.json; Final root adjudication | supports | One major and one minor; exact findings, owners and actions control serialization. |

## Limits And Additional Notes

- UNKNOWN: inspected generic membrane or high-temperature context does not establish the exact 10–20 °C class calibration or moderate-flexibility causal bridge. Unavailable bodies are not paper-wide absence or biological refutation.
- Noll exact body attribution remains unknown; publication identity is positive and missing body is not negative source evidence.
- Generic compositional and signaling attribution does not establish universal taxon efficacy, exact bin membership or a causal mechanism for breadth.
- Detailed pathogen fitness/AMR/ROS/defense and intervention mechanisms are UNASSESSED_SCOPE.
- Canonical statement is strain/source scoped; no phenotype transfer from taxonomy alone.
- Node2 moderate capacity/process wording remains qualified; no forced reservoir CAPACITY retyping.
- Edges7/8 operational quantity/class modeling remains qualified; no automatic QUALITY-to-TRAIT or invented local hard-domain violation.
- Existential OWL restriction is not a complete measured-range or causal verification.
- Exact quantitative/source efficacy is audited separately; detailed pathogen survival/fitness/ROS/AMR/intervention biology UNASSESSED_SCOPE.
- One uncaptured history and one script lead are matching-line-only context, not whole-body authority.
- Initial official taxonomy DNS failure is preserved separately from successful primary XML.
- Retained catalog absence is canonical-only; source species coverage can be positive and detailed module queries were not executed.
- Private/remote human acceptance remains unknown.
- Browser evidence is actual retained tool output, not raw article text; uninstrumented first-call and origin/cache-fetch times are not invented. Original acquisitions differ from copy/read times.
- Historical common failures, retries and no-adapter skips remain explicit; qualified B12 QC is not a new B13 execution or remote publication.
- Whole 250-line target, 91 captured inputs, six works, twelve external placements, twelve grounding fields, eleven nodes and nine edges reviewed.
- Twelve current history projections reuse twelve unchanged prior whole-file readings. One uncaptured history and one script were matching-line context only.
- The bounded scratch serializer runs once after root FINAL. Root independently inspects the actual YAML and runs native output validation before any save.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T000620Z-temperature-delta-mid1
kind: record
repository: CultureBotAI/TraitMech
title: Whole-record review of temperature delta mid1
started_at: '2026-10-22T00:00:45.403117Z'
finished_at: '2026-10-22T00:06:20Z'
reviewer:
  identity: codex
  kind: agent
  independence: independent
  independence_basis: Separate source and grounding audits plus independent root primary,
    owner and final adjudication readings; no additional semantic challenge was required.
    Generic classification, attribution and formal representation only; detailed survival
    or intervention mechanisms remain UNASSESSED_SCOPE.
  model: GPT-6 (Codex)
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Whole-record review finds one grouped formal relation-role major and one
  human-acceptance minor. The canonical 15 °C growth breadth and three literal snippets
  are positive; exact numerical causal attribution and Noll body wording remain unknown.
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
  - path: data/traits/environment/temperature_delta_mid1.yaml
    sha256: 3f43e2bb4daf2c44cb8b899c2ea09963e96ed83f5a5c0ab3348628955155e9dc
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
  - path: research/traits/environment/temperature_delta_mid1-deep-research-falcon.md
    sha256: e19710d9db2b50edab83b2de2d27ee2245b3fc9e938a63d2f68c08b12d910075
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
  - path: scripts/review_temperature_delta_high_graph_183.py
    sha256: dcade5d2fdf07c76e06cd5d8abca898af95a8faabf70e45a62bebf951f2ae31b
    role: context
  - path: scripts/review_temperature_delta_very_low_graph_183.py
    sha256: 1ac23973b6cf54861f6ae79afefe93e39cc9382a93c73c36a8daa37b376334d0
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
- target_id: METPO:1000485
  path: data/traits/environment/temperature_delta_mid1.yaml
  label: temperature delta mid1
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_delta_mid1.yaml
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
  selection: Fifth record of the actual local batch 013 queue. Whole 250-line target
    and 91 captured inputs verified before judgment; local review does not assert
    remote publication.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - METPO:1000485
checks:
- check_id: audit-graphs
  name: Full-corpus graph audit
  status: passed
  required: true
  target_ids:
  - METPO:1000485
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
  - METPO:1000485
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
  - METPO:1000485
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
  - METPO:1000485
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
  - METPO:1000485
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
  - METPO:1000485
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
  - METPO:1000485
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
- check_id: temperature-delta-mid1-validate
  name: Focused native validation
  status: passed
  required: true
  target_ids:
  - METPO:1000485
  command: just validate data/traits/environment/temperature_delta_mid1.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Native record validation passed; scientific interpretation is assessed
    separately.
  evidence_ids:
  - check-temperature-delta-mid1-validate
- check_id: temperature-delta-mid1-strict
  name: Focused strict validation
  status: passed
  required: true
  target_ids:
  - METPO:1000485
  command: just validate-strict data/traits/environment/temperature_delta_mid1.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: The actual validate-strict command passed.
  evidence_ids:
  - check-temperature-delta-mid1-strict
- check_id: temperature-delta-mid1-snippets-network
  name: Focused network snippet check
  status: passed
  required: true
  target_ids:
  - METPO:1000485
  command: just verify-snippets --record data/traits/environment/temperature_delta_mid1.yaml
    --out /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-snippets.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: Three snippets over two references were VERIFIED; independent manual checks
    also support all three literal fragments.
  evidence_ids:
  - check-temperature-delta-mid1-snippets-network
- check_id: batch012-qc
  name: Qualified batch-twelve QC
  status: passed
  required: true
  target_ids:
  - METPO:1000485
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
  - METPO:1000485
  summary: Zero protein classes or instances in this quantitative NONMECHANISTIC overview;
    no token protein requirement.
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
- evidence_id: check-temperature-delta-mid1-validate
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-validate.log
  locator: Executed 2026-10-22T00:01:00.700665+00:00 through 2026-10-22T00:01:01.335375+00:00;
    metadata temperature-delta-mid1-validate.json
  accessed_at: '2026-10-22T00:01:01.335375Z'
  support: context_only
  summary: Native record validation passed; scientific interpretation is assessed
    separately.
  snapshot_sha256: 2ffcefdfc9351d493d4cfcc56e952029671231f8abc7ab7b593a64b81e27ffaa
- evidence_id: check-temperature-delta-mid1-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-strict.log
  locator: Executed 2026-10-22T00:01:00.700664+00:00 through 2026-10-22T00:01:01.799759+00:00;
    metadata temperature-delta-mid1-strict.json
  accessed_at: '2026-10-22T00:01:01.799759Z'
  support: context_only
  summary: The actual validate-strict command passed.
  snapshot_sha256: 1d851d87f46e9dc433cb768958367f1c9a070f7d8848cb09e64074b9830eb3af
- evidence_id: check-temperature-delta-mid1-snippets-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-snippets-network.log
  locator: Executed 2026-10-22T00:01:04.274210+00:00 through 2026-10-22T00:01:07.664523+00:00;
    metadata temperature-delta-mid1-snippets-network.json
  accessed_at: '2026-10-22T00:01:07.664523Z'
  support: context_only
  summary: Three snippets over two references were VERIFIED; independent manual checks
    also support all three literal fragments.
  snapshot_sha256: d4e43c53014da51bb3d7f7e218496356fd02a6eece28d754002bd5b44677b9c8
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
  reference: data/traits/environment/temperature_delta_mid1.yaml
  locator: Whole 250-line current record
  accessed_at: '2026-10-22T00:00:45.937465Z'
  support: supports
  summary: Eleven nodes, nine edges and nine embedded events; one canonical example
    and no protein examples.
  snapshot_sha256: 3f43e2bb4daf2c44cb8b899c2ea09963e96ed83f5a5c0ab3348628955155e9dc
- evidence_id: reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/common-reuse-b12-qc-supplement-qualified.json
  locator: Actual B12-to-B13 qualification
  accessed_at: '2026-10-21T23:05:39.165510Z'
  support: supports
  summary: Current byte comparisons retain original diagnostic failures, retries and
    skips.
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
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-21T23:09:00.804479Z'
  support: supports
  summary: Actual local initialization; publication remains a separate action.
  snapshot_sha256: cda5c0d3753e7a2a3ceb9ba723261fa79d4f760aad1713ff2d33b08def3577f7
- evidence_id: policy
  kind: authority
  reference: docs/GROUNDING_POLICY.md
  locator: Captured maintained authority
  accessed_at: '2026-10-22T00:03:25.818844Z'
  support: supports
  summary: Actual referents and optional protein applicability.
  snapshot_sha256: 891678c983c2283a47c81c47950b35753981e9339d105f3bbdda92a1f5ab7f42
- evidence_id: playbook
  kind: authority
  reference: docs/CURATION_PLAYBOOK.md
  locator: Captured maintained authority
  accessed_at: '2026-10-22T00:03:25.818844Z'
  support: supports
  summary: Source scope and attributable acceptance.
  snapshot_sha256: 735e9b810471da9f7d8364e35ffe1e741edb3421480dac01727db6ea5aa65da9
- evidence_id: schema
  kind: authority
  reference: src/traitmech/schema/traitmech.yaml
  locator: Captured maintained authority
  accessed_at: '2026-10-22T00:03:25.818844Z'
  support: supports
  summary: Current facets and NONMECHANISTIC scope.
  snapshot_sha256: 46c47fc627b80ccbba1e8ab3fb6f2aee93bc2aef7aaf72fe9aadc3257f2c02dd
- evidence_id: predicate-mapping
  kind: authority
  reference: mappings/predicate_grounding.tsv
  locator: Captured maintained authority
  accessed_at: '2026-10-22T00:03:25.818844Z'
  support: supports
  summary: Shared mapping for future empty fields; populated IDs are skipped.
  snapshot_sha256: 8e28c19e93aca3dc164a3befbe2612b289241de457c59f499e65936c03b7ce52
- evidence_id: local-v8
  kind: authority
  reference: proposals/metpo_traitmech_v8/metpo_proposal_properties_robot.tsv
  locator: Captured maintained authority
  accessed_at: '2026-10-22T00:03:25.818844Z'
  support: supports
  summary: Confers has broad formal endpoints and trait-object context.
  snapshot_sha256: 5445e86e845e0a2638292cff4586bf3858b1341d37fecf2e86cefcdbc9a046cd
- evidence_id: local-v3
  kind: authority
  reference: proposals/metpo_traitmech_v3/metpo_proposal_classes_robot.tsv
  locator: Captured maintained authority
  accessed_at: '2026-10-22T00:03:25.818844Z'
  support: supports
  summary: Exact local membrane-fluidity quality.
  snapshot_sha256: 1a1cc789782cfae195c1fc81ddaf848d06d162c7434d94cceb66838de98ab6fa
- evidence_id: local-v4
  kind: authority
  reference: proposals/metpo_traitmech_v4/metpo_proposal_properties_robot.tsv
  locator: Captured maintained authority
  accessed_at: '2026-10-22T00:03:25.818844Z'
  support: supports
  summary: Operational defines relation has broad formal causal-node endpoints.
  snapshot_sha256: 55a96748c50b60ba0622170ef0eb09833f6d1e59431a4ab32b6fcb079103c0b7
- evidence_id: capture
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-ground-agent/capture-verification.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:01:12.414699Z'
  support: supports
  summary: All 91 inputs and whole target verified.
  snapshot_sha256: 20ba221fc153a0c7abee8edd9eaf33210e72d6a31775e51360d509b836fcf0a0
- evidence_id: identity
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-ground-agent/identity-assessment.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:03:25.816745Z'
  support: supports
  summary: Active identity, parent and inclusive numerical restriction.
  snapshot_sha256: 6994d9d78741ea8f58eec058856877f2de36cc0bf40bc58b21928bc152a727f8
- evidence_id: nodes-edges
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-ground-agent/node-edge-grounding-ledger.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:03:25.817217Z'
  support: supports
  summary: Every current node and edge, including formal positives and limitations.
  snapshot_sha256: 78a17b1b1ca366fe1bd30f5e63f1e0dfba091689661bc5ece1a2643a2751dfff
- evidence_id: owners
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-ground-agent/owner-provenance-assessment.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:03:25.818207Z'
  support: supports
  summary: Exact current owners and conditional recurrence.
  snapshot_sha256: 6b1fc2787d4613421d4615fce17498afecfeb723f65c28ec45e1b8d4f766549e
- evidence_id: owner-primary
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-ground-agent/owner-primary-reading.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:03:25.734412Z'
  support: supports
  summary: Actual shared grounder, current facet migration and canonical-entry guards.
  snapshot_sha256: 434070f2e7b09b438fc948e0c01318f4fcb8b9e64b7adb81191437ec79316e98
- evidence_id: human-search
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-ground-agent/search-and-provenance.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:01:22.111247Z'
  support: supports
  summary: 164 ignored-inclusive matching paths; 67 actual target arrays, zero exact
    target.
  snapshot_sha256: aaaa3cb4fc4a0cb56408c9807215ab882bee1119111886f31cbfbce1b109f065
- evidence_id: histories
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-ground-agent/history-reading-provenance.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:03:25.817808Z'
  support: supports
  summary: Twelve current projections; all twelve prior complete readings qualified
    by identical current hashes.
  snapshot_sha256: 55e3ef085f5ca2f1ffb136f04a8392df6ad9d3867347fe69f37f2f8e63046ed9
- evidence_id: discovery
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-ground-agent/discovery-disposition.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:03:25.781757Z'
  support: supports
  summary: One uncaptured history and one script lead remain matching-line-only context.
  snapshot_sha256: db09d4000e4961e7d144c3a50bc4df2d3819a4a00efc0c4f5a70176dca4df920
- evidence_id: expression
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-ground-agent/expression-and-readiness.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:03:25.818560Z'
  support: supports
  summary: Canonical Pontibacterium aliases lack exact retained catalog coverage;
    source B. subtilis coverage is separately positive.
  snapshot_sha256: 533981a06f508ce1b76210f2d1cc696824df1f240d86844062f800b0692dc0af
- evidence_id: local-authority
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-ground-agent/local-authority-reading.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:03:25.734005Z'
  support: supports
  summary: Actual mapping/proposal rows and facet policies; no Biolink predicate occurs
    in the current graph.
  snapshot_sha256: 4bcf8aa72f77a70924d3b71f8a90d66100a522a5b9d45c982ef60b97bdfbfd27
- evidence_id: ground-manifest
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-ground-agent/evidence-manifest.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:03:25.822299Z'
  support: supports
  summary: Frozen grounding artifacts, all hashes verified.
  snapshot_sha256: 545155b02fc641d9dc9e0ee03014a60e3c1166c63eed8622fb151cd0c0fcb652
- evidence_id: metpo-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/repo/data/raw/metpo.owl
  locator: Retained primary authority, locally read at the recorded time
  accessed_at: '2026-10-22T00:01:21.989135Z'
  support: supports
  summary: Active 1000485, parent 1000303 and inclusive 10–20 Cel existential restriction.
  snapshot_sha256: 8b6f8fe0510a698579e532658c8ace05da2550093365df9ca83feb0741778415
- evidence_id: metpo-primary-projection
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-ground-agent/metpo-authority.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:01:21.989135Z'
  support: supports
  summary: Selected statements with exact primary-byte provenance.
  snapshot_sha256: 6428268745b5fe65c8ccc9478550920067cfab3e52cabe67b9f55c84db1b901b
- evidence_id: ro-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/ro.db
  locator: Retained primary authority, locally read at the recorded time
  accessed_at: '2026-10-22T00:01:21.953455Z'
  support: supports
  summary: Actual inherited material/process and process/process roles.
  snapshot_sha256: 849e616c29fecd0d4a6c6dee0dc0f6f117ace7167dbfa1e0f043dc84868f83cb
- evidence_id: ro-primary-projection
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-ground-agent/selected-ro-primary-reading.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:01:21.953455Z'
  support: supports
  summary: Selected statements with exact primary-byte provenance.
  snapshot_sha256: b5dd9970ac9d6af315b1f23e5438dfab1dcb4d9647e3db8ed564cf6139fd23fd
- evidence_id: spectrum-metadata
  kind: primary_source
  reference: DOI:10.1128/spectrum.03925-23
  locator: Indexed metadata
  accessed_at: '2026-10-21T22:07:08.906527Z'
  support: supports
  summary: Source identity and bounded notice fields.
  snapshot_sha256: 745eedfa2c11814739b07a4d944725bf565eb4e3f9c6b207ba0d31b967563f98
- evidence_id: cold-metadata
  kind: primary_source
  reference: DOI:10.1007/s42770-023-01057-4
  locator: Indexed metadata
  accessed_at: '2026-10-21T22:07:08.865512Z'
  support: supports
  summary: Assigned general cold-review identity and bounded notice fields.
  snapshot_sha256: da5cffab81fe0e039c6fcec8f318b2715f5604eaf8722ea6f63f944178ed447b
- evidence_id: spectrum-body
  kind: primary_source
  reference: DOI:10.1128/spectrum.03925-23
  locator: JATS body paragraph 0 named adaptation sentence and paragraph 2 introductory
    composition sentence, zero based
  accessed_at: '2026-10-21T22:07:32.905772Z'
  support: supports
  summary: Existing generic physical attribution only; detailed sensor, assay and
    antimicrobial efficacy unassessed.
  snapshot_sha256: 4e57f358369566231e022520fc5b5adad7b8c182adfa282d9ed404fa3298a561
- evidence_id: cold-body
  kind: primary_source
  reference: DOI:10.1007/s42770-023-01057-4
  locator: All HTML p elements, paragraph 20 first sentence; abstract clauses (i)/(ii)
    separately read
  accessed_at: '2026-10-21T22:07:50.938485Z'
  support: supports
  summary: Generic cis-unsaturation and source-attributed state-change context only;
    no detailed pathway or universal numerical-bin inference.
  snapshot_sha256: bb09a59c07f43ff0af177f89b624c8b5d4841e513ed0d478120954a016342889
- evidence_id: mendoza
  kind: primary_source
  reference: DOI:10.1146/annurev-micro-091313-103612
  locator: Indexed abstract
  accessed_at: '2026-10-21T10:00:02.042457Z'
  support: supports
  summary: Generic membrane context and two supplied literal fragments; exact bin
    calibration unknown.
  snapshot_sha256: 801da630644a181211f991a6f21c49b178e42a65f615c4eebd8196bc29244588
- evidence_id: tolner
  kind: primary_source
  reference: DOI:10.1016/s0300-9629(97)00003-0
  locator: Indexed abstract
  accessed_at: '2026-10-21T09:29:01.331044Z'
  support: supports
  summary: Generic high-temperature context and supplied fragment; no exact breadth
    calibration.
  snapshot_sha256: 56f69a7ce2e69822ef753fec5c43716583184e45fc1a2c0cae98aa9bdb841265
- evidence_id: tolner-author
  kind: primary_source
  reference: DOI:10.1016/s0300-9629(97)00003-0
  locator: Author institutional abstract page
  accessed_at: '2026-10-21T09:29:00.791083Z'
  support: supports
  summary: Generic opening and existing fragment only; not full article.
  snapshot_sha256: 3c475aae5c42532ff36e66a262fe2d6a9c6fc8b64aa6576d93efdc96cada4134
- evidence_id: mendoza-browser
  kind: primary_source
  reference: DOI:10.1146/annurev-micro-091313-103612
  locator: Actual browser export of publisher abstract; origin/cache-fetch time unknown
  accessed_at: '2026-10-21T23:38:35Z'
  support: supports
  summary: Generic abstract support; retained tool output is not raw HTML or a full
    body.
  snapshot_sha256: b8635235ad5e362d0b33ef4834f84eb25fe7ff6b1bd1321affb2b61cecbc66fc
- evidence_id: canonical-primary
  kind: primary_source
  reference: DOI:10.1099/ijsem.0.006018
  locator: Actual structured metadata/abstract response
  accessed_at: '2026-10-22T00:01:21.958472Z'
  support: supports
  summary: Current abstract explicitly reports N1Y112T growth 20–35 °C, supporting
    15 °C breadth; full paper not inspected.
  snapshot_sha256: bd5137f9ca1f804e99b65dc384a8568883209f76738962070bac05dac78b7573
- evidence_id: noll-primary
  kind: primary_source
  reference: DOI:10.3390/pr8010121
  locator: Actual structured metadata/abstract response
  accessed_at: '2026-10-22T00:01:40.203632Z'
  support: supports
  summary: Official publication identity and abstract context only; exact Tmin/Tmax
    body wording is unknown.
  snapshot_sha256: 97f9d4d96b3531f6be368d1f9fa4eeae8bf0ddb7a92b52c14d40836228493110
- evidence_id: noll-index-search
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.3390/pr8010121&format=json&resultType=core
  locator: Zero-hit indexed search; not a missing DOI or source refutation
  accessed_at: '2026-10-22T00:01:21.938449Z'
  support: context_only
  summary: Crossref independently verifies this DOI; no full body was acquired by
    this search.
  snapshot_sha256: ff2a2a379b0388eb4e5464245931338d053be12faf692ecaa6b4efd98fc492e9
- evidence_id: taxonomy
  kind: authority
  reference: NCBITaxon:2781979
  locator: Whole successful official taxonomy XML
  accessed_at: '2026-10-22T00:01:45.678625Z'
  support: supports
  summary: Pontibacterium sinense with N1Y112 type aliases; taxonomy establishes identity,
    not temperature phenotype.
  snapshot_sha256: 9ce6edf003761e8b4b7ce3e178a366b6f25e353090e03b121a9e4c53e2609b6d
- evidence_id: taxonomy-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-ground-agent/taxonomy-network-retry-access.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:01:45.678625Z'
  support: supports
  summary: Actual successful request after a retained DNS failure.
  snapshot_sha256: f167e8597d4d206957d03eeea976f756626e4059cccfed46a9296340def2a297
- evidence_id: taxonomy-initial
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-ground-agent/taxonomy-access.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:01:32.096470Z'
  support: supports
  summary: Initial failed request is diagnostic text, not primary XML.
  snapshot_sha256: bdb5be5eb25b165c1b4e220cfba16a58c699af776df923e7cb5286c5aff1fa73
- evidence_id: sources
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-source-agent/source-assessment.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:03:51.753283Z'
  support: supports
  summary: Six works; overall UNKNOWN and no source-only finding.
  snapshot_sha256: 2246148ce9e7340f113719ea7eb38655c6dfb66cfbe868538b761af882a80ebd
- evidence_id: source-identities
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-source-agent/source-identities-status.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:03:51.751653Z'
  support: supports
  summary: Exact source identities and bounded publication-status observations.
  snapshot_sha256: 197209d6efa148302b4d010a14df714d62ac73204a8c20e641ebd8b5ba41ed77
- evidence_id: placements
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-source-agent/source-placement-ledger.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:03:51.751903Z'
  support: supports
  summary: Twelve external placements and adjacent notes accounted for.
  snapshot_sha256: 13fb2b3b9f3ebffd920cd77e3d78e92edd955d748afe014e9902bce1405f1537
- evidence_id: snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-source-agent/snippet-ledger.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:03:51.752122Z'
  support: supports
  summary: Three supplied snippets are literal; Noll body-level notes remain separately
    unknown.
  snapshot_sha256: df10d3ac1c4d3b54838e317566f48d8a45b0bb450819a8c38f670600617782ca
- evidence_id: source-nodes-edges
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-source-agent/node-edge-source-ledger.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:03:51.752216Z'
  support: supports
  summary: Source judgments for every node and edge.
  snapshot_sha256: aae463338fa312c0bc8a66402486c28be0d1f3891b1cc69ffe386858813413e7
- evidence_id: source-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-source-agent/primary-reading-scope.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:03:51.753220Z'
  support: supports
  summary: Selected abstracts and generic body sentences only; no whole-article claim.
  snapshot_sha256: f3d62c5eed4803ec3b738ed301009daaec0cf1168b964eef5f6b6968d738c663
- evidence_id: source-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-source-agent/source-access-limits.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:03:51.752443Z'
  support: supports
  summary: Unavailable bodies and retained retrieval diagnostics are not refutations.
  snapshot_sha256: cf86cbb86331cb62fcdf0d6093c0f39b85b5e48ec1f4e138faf8b74d9986b7df
- evidence_id: source-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-source-agent/source-reuse-receipt.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:02:34.264346Z'
  support: supports
  summary: Original acquisitions, current copies and current reads have distinct timestamps.
  snapshot_sha256: fe0f8e06b9d9f508474eddf9b2619effd6240e63517f43d22b1bb05c3ac73b63
- evidence_id: canonical
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-source-agent/canonical-assessment.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:03:51.752348Z'
  support: supports
  summary: Reported 20–35 °C growth gives 15 °C breadth within this bin.
  snapshot_sha256: d1ef58332317c81244accfec8daff83b359f8d169b80b753efa0549d781ca9e4
- evidence_id: source-manifest
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-source-agent/evidence-manifest.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:03:51.761250Z'
  support: supports
  summary: Frozen source artifacts, all hashes verified.
  snapshot_sha256: aa309617de8ee09b54a1a3d85d8e7c30920a244ea1dc8733e2ba8e4a122b5fc8
- evidence_id: root-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-source-root/root-reading.json
  locator: Derived audit or reading receipt; underlying primary bytes identified separately
  accessed_at: '2026-10-22T00:05:04.683833Z'
  support: supports
  summary: Root independent selected primary, full assessment and bounded history-projection
    readings.
  snapshot_sha256: 4f15143dfe7c2c398021be81dcf4f125a784d0f0775c70db9573012a3a55bb3d
- evidence_id: root-browser-failure
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-source-root/noll-later-positioned-access.json
  locator: Later positioned browser attempt; actual tool clock bounds, no primary-body
    claim
  accessed_at: '2026-10-22T00:04:15Z'
  support: context_only
  summary: The later Noll attempt returned 429; exact body attribution remains unknown.
  snapshot_sha256: 10cc61dec6cea8fe16a93d2b83bce91722cc3aecc1d00032287f96abbeba2a04
- evidence_id: adjudication
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-013.p7v3m9qa/temperature-delta-mid1-root-adjudication.json
  locator: Final root adjudication
  accessed_at: '2026-10-22T00:05:04.685347Z'
  support: supports
  summary: One major and one minor; exact findings, owners and actions control serialization.
  snapshot_sha256: 30c43e8e035fc015b5061d54c25462545d64b232b7fde9aa09215edce2173b8d
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: active identity and hierarchy'
  outcome: supported
  target_ids:
  - METPO:1000485
  summary: Active METPO:1000485, parent 1000303 and related Td_10_20 align with the
    inclusive 10–20 Cel existential restriction. Local v3/v4/v8 identifiers retain
    proposal status.
  evidence_ids:
  - identity
  - metpo-primary
  - local-v3
  - local-v4
  - local-v8
- assessment_id: definition
  area: quantity
  topic: 'Native checklist: numerical source calibration'
  outcome: unknown
  target_ids:
  - METPO:1000485
  summary: Inspected generic membrane and high-temperature sources do not establish
    the exact 10–20 °C class calibration or moderate-flexibility causal bridge. The
    OWL class restriction is not experimental validation.
  evidence_ids:
  - sources
  - placements
  - mendoza
  - tolner
  - identity
- assessment_id: canonical-example
  area: quantity
  topic: 'Native checklist: reported growth breadth'
  outcome: supported
  target_ids:
  - METPO:1000485
  summary: The actual indexed abstract reports Pontibacterium sinense N1Y112T growth
    from 20 to 35 °C, giving a 15 °C breadth inside this bin. Official taxonomy supports
    identity separately; no optimum-only or survival inference, and no full-paper
    reading claim.
  evidence_ids:
  - canonical
  - canonical-primary
  - taxonomy
- assessment_id: source-support
  area: evidence
  topic: 'Native checklist: six works and twelve placements'
  outcome: unknown
  target_ids:
  - METPO:1000485
  summary: Source identities and selected generic physical attribution are positive.
    Noll body-level wording and exact quantitative sufficiency remain unknown; failed
    retrievals and an empty indexed search do not refute the source.
  evidence_ids:
  - sources
  - source-identities
  - placements
  - source-access
  - source-reading
  - noll-primary
  - root-browser-failure
- assessment_id: quotations
  area: evidence
  topic: 'Native checklist: three supplied fragments'
  outcome: supported
  target_ids:
  - METPO:1000485
  summary: All three supplied snippets are literal in inspected abstracts and passed
    native verification. Their adjacent numerical or causal interpretations are assessed
    separately.
  evidence_ids:
  - snippets
  - mendoza
  - tolner
- assessment_id: nodes
  area: representation
  topic: 'Native checklist: all eleven current referents'
  outcome: unknown
  target_ids:
  - METPO:1000485
  summary: Current traits, membrane-fluidity quality and explicit process facets are
    supported. Moderate-capacity wording at node 2 and property/class interpretation
    at node 9 remain qualified; no forced reservoir CAPACITY retype.
  evidence_ids:
  - nodes-edges
  - source-nodes-edges
  - schema
  - local-authority
  details: "{\n  \"grounding\": [\n    {\n      \"index\": 0,\n      \"node_id\":\
    \ \"temperature_delta_mid1_trait\",\n      \"label\": \"temperature delta mid1\"\
    ,\n      \"node_type\": \"TRAIT\",\n      \"grounding\": \"METPO:1000485\",\n\
    \      \"outcome\": \"supported\",\n      \"assessment\": \"Active exact 10–20\
    \ inclusive temperature-breadth bin.\"\n    },\n    {\n      \"index\": 1,\n \
    \     \"node_id\": \"temperature_delta\",\n      \"label\": \"temperature delta\"\
    ,\n      \"node_type\": \"TRAIT\",\n      \"grounding\": \"METPO:1000303\",\n\
    \      \"outcome\": \"supported\",\n      \"assessment\": \"Active parent temperature-delta\
    \ class 1000303.\"\n    },\n    {\n      \"index\": 2,\n      \"node_id\": \"\
    moderate_thermal_adaptation\",\n      \"label\": \"moderate thermal-adaptation\
    \ flexibility\",\n      \"node_type\": \"BIOLOGICAL_PROCESS\",\n      \"grounding\"\
    : null,\n      \"outcome\": \"unknown\",\n      \"assessment\": \"Mid-range remodeling\
    \ capacity may be a disposition or process shorthand. Do not force reservoir CAPACITY\
    \ enum or count a separate finding without disambiguation.\"\n    },\n    {\n\
    \      \"index\": 3,\n      \"node_id\": \"temperature_decrease\",\n      \"label\"\
    : \"decrease in ambient temperature\",\n      \"node_type\": \"ENVIRONMENTAL_FACTOR\"\
    ,\n      \"grounding\": null,\n      \"outcome\": \"supported\",\n      \"assessment\"\
    : \"Current description denotes a drop in ambient growth temperature, so an event/process\
    \ reading is available; environmental enum alone is not exclusionary.\"\n    },\n\
    \    {\n      \"index\": 4,\n      \"node_id\": \"membrane_unsaturated_fatty_acids\"\
    ,\n      \"label\": \"membrane unsaturated fatty acids\",\n      \"node_type\"\
    : \"CHEMICAL\",\n      \"grounding\": null,\n      \"outcome\": \"supported\"\
    ,\n      \"assessment\": \"Cis-unsaturated membrane acyl chains are material chemicals.\
    \ Current description and type agree; no unsupported GO/CHEBI grounding is invented.\"\
    \n    },\n    {\n      \"index\": 5,\n      \"node_id\": \"membrane_fluidity\"\
    ,\n      \"label\": \"membrane fluidity\",\n      \"node_type\": \"QUALITY\",\n\
    \      \"grounding\": \"METPO:1007505\",\n      \"outcome\": \"supported\",\n\
    \      \"assessment\": \"Explicit physical bilayer fluidity is a QUALITY; exact\
    \ v3 row and current node mapping support identity, distinct from the maintenance\
    \ process.\"\n    },\n    {\n      \"index\": 6,\n      \"node_id\": \"ufa_biosynthesis\"\
    ,\n      \"label\": \"cis-unsaturated fatty acid biosynthesis\",\n      \"node_type\"\
    : \"BIOLOGICAL_PROCESS\",\n      \"grounding\": null,\n      \"outcome\": \"supported\"\
    ,\n      \"assessment\": \"Synthesis is an explicit biological process; no protein-instance\
    \ requirement.\"\n    },\n    {\n      \"index\": 7,\n      \"node_id\": \"membrane_physical_state_change\"\
    ,\n      \"label\": \"membrane physical-state change\",\n      \"node_type\":\
    \ \"BIOLOGICAL_PROCESS\",\n      \"grounding\": null,\n      \"outcome\": \"supported\"\
    ,\n      \"assessment\": \"Change of physical state is described as a process/event,\
    \ distinct from the static quality.\"\n    },\n    {\n      \"index\": 8,\n  \
    \    \"node_id\": \"two_component_cold_signaling\",\n      \"label\": \"two-component\
    \ cold signaling\",\n      \"node_type\": \"BIOLOGICAL_PROCESS\",\n      \"grounding\"\
    : null,\n      \"outcome\": \"supported\",\n      \"assessment\": \"Signaling\
    \ activity is an explicit process; no material-protein interpretation is imposed.\"\
    \n    },\n    {\n      \"index\": 9,\n      \"node_id\": \"thermal_niche_breadth\"\
    ,\n      \"label\": \"thermal niche / temperature breadth\",\n      \"node_type\"\
    : \"QUALITY\",\n      \"grounding\": null,\n      \"outcome\": \"unknown\",\n\
    \      \"assessment\": \"Thermal niche/breadth is a measured property bounded\
    \ by growth conditions. Quantity versus interval wording and its class-level relation\
    \ to the phenotype remain qualifications; QUALITY alone does not prove a wrong\
    \ class assertion.\"\n    },\n    {\n      \"index\": 10,\n      \"node_id\":\
    \ \"tmin_tmax\",\n      \"label\": \"Tmin and Tmax growth boundaries\",\n    \
    \  \"node_type\": \"QUALITY\",\n      \"grounding\": null,\n      \"outcome\"\
    : \"supported\",\n      \"assessment\": \"Cardinal minimum/maximum growth temperatures\
    \ are defining measurement boundaries; no process or material identity is implied.\"\
    \n    }\n  ],\n  \"source\": [\n    {\n      \"index\": 0,\n      \"field\": \"\
    causal_graphs[0].nodes[0]\",\n      \"node_id\": \"temperature_delta_mid1_trait\"\
    ,\n      \"outcome\": \"unknown\",\n      \"assessment\": \"Explicit10–20 bin;\
    \ exact assigned-source calibration remains unresolved.\"\n    },\n    {\n   \
    \   \"index\": 1,\n      \"field\": \"causal_graphs[0].nodes[1]\",\n      \"node_id\"\
    : \"temperature_delta\",\n      \"outcome\": \"supported_at_definition_scope\"\
    ,\n      \"assessment\": \"Growth breadth is distinct from optimum or survival;\
    \ canonical arithmetic is positive.\"\n    },\n    {\n      \"index\": 2,\n  \
    \    \"field\": \"causal_graphs[0].nodes[2]\",\n      \"node_id\": \"moderate_thermal_adaptation\"\
    ,\n      \"outcome\": \"unknown\",\n      \"assessment\": \"Mid-range membrane/enzyme\
    \ capacity is a record synthesis not directly established as10–20 sufficiency\
    \ by inspected sources.\"\n    },\n    {\n      \"index\": 3,\n      \"field\"\
    : \"causal_graphs[0].nodes[3]\",\n      \"node_id\": \"temperature_decrease\"\
    ,\n      \"outcome\": \"supported_at_generic_scope\",\n      \"assessment\": \"\
    Cooling is the physical context of the assigned abstracts and selected introductory\
    \ text.\"\n    },\n    {\n      \"index\": 4,\n      \"field\": \"causal_graphs[0].nodes[4]\"\
    ,\n      \"node_id\": \"membrane_unsaturated_fatty_acids\",\n      \"outcome\"\
    : \"qualified_generic_support\",\n      \"assessment\": \"Cis-unsaturated lipid\
    \ composition context is supported, without a universal response or detailed taxon\
    \ efficacy inference.\"\n    },\n    {\n      \"index\": 5,\n      \"field\":\
    \ \"causal_graphs[0].nodes[5]\",\n      \"node_id\": \"membrane_fluidity\",\n\
    \      \"outcome\": \"supported_at_generic_scope\",\n      \"assessment\": \"\
    Membrane fluidity is the physical property discussed; formal facet roles are separately\
    \ audited.\"\n    },\n    {\n      \"index\": 6,\n      \"field\": \"causal_graphs[0].nodes[6]\"\
    ,\n      \"node_id\": \"ufa_biosynthesis\",\n      \"outcome\": \"qualified_generic_support\"\
    ,\n      \"assessment\": \"Generic unsaturated synthesis/composition attribution\
    \ is present; detailed pathway output/efficacy unassessed.\"\n    },\n    {\n\
    \      \"index\": 7,\n      \"field\": \"causal_graphs[0].nodes[7]\",\n      \"\
    node_id\": \"membrane_physical_state_change\",\n      \"outcome\": \"supported_at_attribution_scope\"\
    ,\n      \"assessment\": \"Cold-review abstract names liquid-crystalline state\
    \ change as sensing context; no detailed sensor efficacy judgment.\"\n    },\n\
    \    {\n      \"index\": 8,\n      \"field\": \"causal_graphs[0].nodes[8]\",\n\
    \      \"node_id\": \"two_component_cold_signaling\",\n      \"outcome\": \"supported_at_attribution_scope\"\
    ,\n      \"assessment\": \"Two-component activation is explicitly attributed in\
    \ the review abstract; detailed signaling mechanisms/fitness are outside scope.\"\
    \n    },\n    {\n      \"index\": 9,\n      \"field\": \"causal_graphs[0].nodes[9]\"\
    ,\n      \"node_id\": \"thermal_niche_breadth\",\n      \"outcome\": \"unknown\"\
    ,\n      \"assessment\": \"Thermal niche as a bounded growth quantity is readable\
    \ in record; nearest Noll body attribution is not verified.\"\n    },\n    {\n\
    \      \"index\": 10,\n      \"field\": \"causal_graphs[0].nodes[10]\",\n    \
    \  \"node_id\": \"tmin_tmax\",\n      \"outcome\": \"unknown\",\n      \"assessment\"\
    : \"Minimum/maximum growth boundaries are explicit record referents; nearest assigned\
    \ Noll body wording remains unavailable.\"\n    }\n  ]\n}"
- assessment_id: relations
  area: consistency
  topic: 'Native checklist: all nine current relations'
  outcome: concern
  target_ids:
  - METPO:1000485
  summary: 'Edges 3/4/6 form one imported-role group: RO2213 conflicts with chemical/quality
    endpoints, and RO2327 conflicts with a quality subject. Edge 2 can denote a temperature-decrease
    event; edge 5 has process endpoints. Local defines and RDFS subclass modeling
    at 7/8 remain qualifications, not automatic enum failures.'
  evidence_ids:
  - nodes-edges
  - source-nodes-edges
  - ro-primary
  - local-authority
  - adjudication
  details: "{\n  \"grounding\": [\n    {\n      \"index\": 0,\n      \"subject\":\
    \ \"moderate_thermal_adaptation\",\n      \"predicate\": \"confers\",\n      \"\
    predicate_id\": \"METPO:2007700\",\n      \"object\": \"temperature_delta_mid1_trait\"\
    ,\n      \"outcome\": \"supported\",\n      \"assessment\": \"Local v8 broad formal\
    \ causal-node roles and trait object fit. The exact quantitative causal bridge\
    \ remains independently source-assessed, not proven by formal fit.\"\n    },\n\
    \    {\n      \"index\": 1,\n      \"subject\": \"temperature_delta_mid1_trait\"\
    ,\n      \"predicate\": \"is a\",\n      \"predicate_id\": \"rdfs:subClassOf\"\
    ,\n      \"object\": \"temperature_delta\",\n      \"outcome\": \"supported\"\
    ,\n      \"assessment\": \"Exact imported 1000485 subclass 1000303 is positive.\"\
    \n    },\n    {\n      \"index\": 2,\n      \"subject\": \"temperature_decrease\"\
    ,\n      \"predicate\": \"increases\",\n      \"predicate_id\": \"RO:0002213\"\
    ,\n      \"object\": \"ufa_biosynthesis\",\n      \"outcome\": \"unknown\",\n\
    \      \"assessment\": \"RO2213 inherits process/process roles. A temperature-decrease\
    \ event can satisfy the subject interpretation, and the object is an explicit\
    \ biosynthetic process; no enum-only categorical error. Biological efficacy/universality\
    \ unassessed.\"\n    },\n    {\n      \"index\": 3,\n      \"subject\": \"ufa_biosynthesis\"\
    ,\n      \"predicate\": \"increases\",\n      \"predicate_id\": \"RO:0002213\"\
    ,\n      \"object\": \"membrane_unsaturated_fatty_acids\",\n      \"outcome\"\
    : \"concern\",\n      \"assessment\": \"RO2213 inherits process range via RO2211,\
    \ but the object is material unsaturated acyl chains rather than a process. The\
    \ explicit biosynthetic subject is compatible.\"\n    },\n    {\n      \"index\"\
    : 4,\n      \"subject\": \"membrane_unsaturated_fatty_acids\",\n      \"predicate\"\
    : \"increases\",\n      \"predicate_id\": \"RO:0002213\",\n      \"object\": \"\
    membrane_fluidity\",\n      \"outcome\": \"concern\",\n      \"assessment\": \"\
    RO2213 process/process roles conflict with a material-chemical subject and physical-quality\
    \ object. This is formal representation, not a claim that the biological direction\
    \ is false.\"\n    },\n    {\n      \"index\": 5,\n      \"subject\": \"membrane_physical_state_change\"\
    ,\n      \"predicate\": \"activates\",\n      \"predicate_id\": \"RO:0002213\"\
    ,\n      \"object\": \"two_component_cold_signaling\",\n      \"outcome\": \"\
    supported\",\n      \"assessment\": \"Physical-state change and signaling are\
    \ explicitly processual, so imported process endpoints fit. Detailed cold-response\
    \ efficacy is unassessed.\"\n    },\n    {\n      \"index\": 6,\n      \"subject\"\
    : \"membrane_fluidity\",\n      \"predicate\": \"enables\",\n      \"predicate_id\"\
    : \"RO:0002327\",\n      \"object\": \"moderate_thermal_adaptation\",\n      \"\
    outcome\": \"concern\",\n      \"assessment\": \"RO2327 inherits material-entity\
    \ subject via RO2215/2216/2500/2595. Membrane fluidity is an explicit QUALITY,\
    \ not its material bearer. Moderate-process/capacity wording of the object is\
    \ separately qualified; the subject mismatch is independently firm.\"\n    },\n\
    \    {\n      \"index\": 7,\n      \"subject\": \"tmin_tmax\",\n      \"predicate\"\
    : \"defines\",\n      \"predicate_id\": \"METPO:2007500\",\n      \"object\":\
    \ \"thermal_niche_breadth\",\n      \"outcome\": \"unknown\",\n      \"assessment\"\
    : \"Local v4 defines has broad formal causal-node endpoints. Cardinal boundaries\
    \ operationally identify thermal breadth; object QUALITY versus trait-class prose\
    \ and interval/width distinction remain bounded modeling qualifications, not an\
    \ invented hard domain failure.\"\n    },\n    {\n      \"index\": 8,\n      \"\
    subject\": \"thermal_niche_breadth\",\n      \"predicate\": \"is a\",\n      \"\
    predicate_id\": \"rdfs:subClassOf\",\n      \"object\": \"temperature_delta\"\
    ,\n      \"outcome\": \"unknown\",\n      \"assessment\": \"RDFS subclass is class-level;\
    \ both graph concepts may be class representations. Current measured thermal-breadth\
    \ property and temperature-delta phenotype are closely scoped, but the property/class\
    \ interpretation is not fully explicit. No automatic quality-to-trait error or\
    \ source measurement claim is imposed.\"\n    }\n  ],\n  \"source\": [\n    {\n\
    \      \"index\": 0,\n      \"field\": \"causal_graphs[0].edges[0]\",\n      \"\
    subject\": \"moderate_thermal_adaptation\",\n      \"object\": \"temperature_delta_mid1_trait\"\
    ,\n      \"outcome\": \"unknown\",\n      \"assessment\": \"UNKNOWN: inspected\
    \ generic membrane or high-temperature context does not establish the exact 10–20\
    \ °C class calibration or moderate-flexibility causal bridge. Unavailable bodies\
    \ are not paper-wide absence or biological refutation.\",\n      \"formal_role_scope\"\
    : \"Separate grounding audit; literal or generic source support does not validate\
    \ imported predicate roles.\"\n    },\n    {\n      \"index\": 1,\n      \"field\"\
    : \"causal_graphs[0].edges[1]\",\n      \"subject\": \"temperature_delta_mid1_trait\"\
    ,\n      \"object\": \"temperature_delta\",\n      \"outcome\": \"unknown\",\n\
    \      \"assessment\": \"UNKNOWN: inspected generic membrane or high-temperature\
    \ context does not establish the exact 10–20 °C class calibration or moderate-flexibility\
    \ causal bridge. Unavailable bodies are not paper-wide absence or biological refutation.\"\
    ,\n      \"formal_role_scope\": \"Separate grounding audit; literal or generic\
    \ source support does not validate imported predicate roles.\"\n    },\n    {\n\
    \      \"index\": 2,\n      \"field\": \"causal_graphs[0].edges[2]\",\n      \"\
    subject\": \"temperature_decrease\",\n      \"object\": \"ufa_biosynthesis\",\n\
    \      \"outcome\": \"qualified_generic_support\",\n      \"assessment\": \"Cold-review\
    \ abstract clause(ii) and actual HTML p20 first sentence support unsaturation/cis-MUFA\
    \ context. This is generic attribution; taxon-specific regulation, universal efficacy\
    \ or a measured10–20 breadth are not established.\",\n      \"formal_role_scope\"\
    : \"Separate grounding audit; literal or generic source support does not validate\
    \ imported predicate roles.\"\n    },\n    {\n      \"index\": 3,\n      \"field\"\
    : \"causal_graphs[0].edges[3]\",\n      \"subject\": \"ufa_biosynthesis\",\n \
    \     \"object\": \"membrane_unsaturated_fatty_acids\",\n      \"outcome\": \"\
    qualified_generic_support\",\n      \"assessment\": \"Cold-review abstract clause(ii)\
    \ and actual HTML p20 first sentence support unsaturation/cis-MUFA context. This\
    \ is generic attribution; taxon-specific regulation, universal efficacy or a measured10–20\
    \ breadth are not established.\",\n      \"formal_role_scope\": \"Separate grounding\
    \ audit; literal or generic source support does not validate imported predicate\
    \ roles.\"\n    },\n    {\n      \"index\": 4,\n      \"field\": \"causal_graphs[0].edges[4]\"\
    ,\n      \"subject\": \"membrane_unsaturated_fatty_acids\",\n      \"object\"\
    : \"membrane_fluidity\",\n      \"outcome\": \"qualified_generic_support\",\n\
    \      \"assessment\": \"Spectrum introduction names homeoviscous adaptation and\
    \ existing B.subtilis membrane-composition context. Generic physical attribution\
    \ is retained; the note generalizable does not authorize a universal or detailed\
    \ antimicrobial/strain efficacy assessment.\",\n      \"formal_role_scope\": \"\
    Separate grounding audit; literal or generic source support does not validate\
    \ imported predicate roles.\"\n    },\n    {\n      \"index\": 5,\n      \"field\"\
    : \"causal_graphs[0].edges[5]\",\n      \"subject\": \"membrane_physical_state_change\"\
    ,\n      \"object\": \"two_component_cold_signaling\",\n      \"outcome\": \"\
    supported_at_attribution_scope\",\n      \"assessment\": \"Cold-review abstract\
    \ clause(i) explicitly places membrane liquid-crystalline-state change upstream\
    \ of two-component activation. This verifies existing generic source attribution\
    \ only; detailed sensing, pathway efficacy, pathogen fitness and intervention\
    \ mechanisms are UNASSESSED_SCOPE.\",\n      \"formal_role_scope\": \"Separate\
    \ grounding audit; literal or generic source support does not validate imported\
    \ predicate roles.\"\n    },\n    {\n      \"index\": 6,\n      \"field\": \"\
    causal_graphs[0].edges[6]\",\n      \"subject\": \"membrane_fluidity\",\n    \
    \  \"object\": \"moderate_thermal_adaptation\",\n      \"outcome\": \"unknown\"\
    ,\n      \"assessment\": \"UNKNOWN: inspected generic membrane or high-temperature\
    \ context does not establish the exact 10–20 °C class calibration or moderate-flexibility\
    \ causal bridge. Unavailable bodies are not paper-wide absence or biological refutation.\"\
    ,\n      \"formal_role_scope\": \"Separate grounding audit; literal or generic\
    \ source support does not validate imported predicate roles.\"\n    },\n    {\n\
    \      \"index\": 7,\n      \"field\": \"causal_graphs[0].edges[7]\",\n      \"\
    subject\": \"tmin_tmax\",\n      \"object\": \"thermal_niche_breadth\",\n    \
    \  \"outcome\": \"unknown\",\n      \"assessment\": \"Noll identity and generic\
    \ temperature-modeling scope are verified. Exact body-level Tmin/Tmax flank/niche\
    \ attribution is unresolved because inspected Crossref abstract does not supply\
    \ that wording and public body routes failed. No paper-wide absence, false-citation\
    \ finding, or mechanistic repair inferred.\",\n      \"formal_role_scope\": \"\
    Separate grounding audit; literal or generic source support does not validate\
    \ imported predicate roles.\"\n    },\n    {\n      \"index\": 8,\n      \"field\"\
    : \"causal_graphs[0].edges[8]\",\n      \"subject\": \"thermal_niche_breadth\"\
    ,\n      \"object\": \"temperature_delta\",\n      \"outcome\": \"unknown\",\n\
    \      \"assessment\": \"Noll identity and generic temperature-modeling scope\
    \ are verified. Exact body-level Tmin/Tmax flank/niche attribution is unresolved\
    \ because inspected Crossref abstract does not supply that wording and public\
    \ body routes failed. No paper-wide absence, false-citation finding, or mechanistic\
    \ repair inferred.\",\n      \"formal_role_scope\": \"Separate grounding audit;\
    \ literal or generic source support does not validate imported predicate roles.\"\
    \n    }\n  ]\n}"
- assessment_id: scope-completeness
  area: scope
  topic: 'Native checklist: quantitative graph and biological limits'
  outcome: unknown
  target_ids:
  - METPO:1000485
  summary: Two components and no protein classes or instances are proportionate to
    this NONMECHANISTIC overview. Generic classification, attribution and formal representation
    were reviewed; detailed pathogen survival, fitness, ROS/AMR, sensing or intervention
    efficacy remains UNASSESSED_SCOPE.
  evidence_ids:
  - record
  - policy
  - source-reading
  - expression
- assessment_id: expression
  area: evidence
  topic: 'Native checklist: bounded catalog applicability'
  outcome: unknown
  target_ids:
  - METPO:1000485
  summary: The retained 20-organism / 28-dataset catalog has no exact Pontibacterium
    taxon or strain-alias match. B. subtilis source-context coverage is separately
    positive. No universal source-species absence, strain transfer or detailed module
    query is claimed.
  evidence_ids:
  - expression
  - taxonomy
  - source-identities
- assessment_id: ownership
  area: ownership
  topic: 'Native checklist: conditional current writers'
  outcome: supported
  target_ids:
  - METPO:1000485
  summary: Shared grounding skips populated IDs. The membrane-fluidity migration already
    agrees with QUALITY. Exact canonical backfill is a no-op for matching existing
    examples and rejects unexpected populated values under its live-queue guard. Sibling
    and uncaptured matching-line leads are not current recurrence owners.
  evidence_ids:
  - owners
  - owner-primary
  - predicate-mapping
  - discovery
- assessment_id: human
  area: provenance
  topic: 'Native checklist: attributable current acceptance'
  outcome: concern
  target_ids:
  - METPO:1000485
  summary: Eight AI events plus a seed and the ignored-inclusive 164-path / 67-array
    search do not establish current human acceptance. Twelve current history projections
    reuse twelve prior complete readings by exact hashes; no new whole-history reading
    is claimed. Private or remote acceptance remains unknown.
  evidence_ids:
  - human-search
  - histories
  - owners
  - playbook
  - root-reading
- assessment_id: readiness
  area: consistency
  topic: 'Native checklist: checks and evidence chronology'
  outcome: supported
  target_ids:
  - METPO:1000485
  summary: All 91 inputs and frozen audits match. Focused native, strict and snippet
    checks passed. Qualified common diagnostics retain historical optional failures
    and 123 no-adapter skips. Original acquisitions, intervening copies and current
    readings remain distinct; no new B13 QC or publication is asserted.
  evidence_ids:
  - capture
  - reuse
  - reuse-postcheck
  - local-init
  - source-reuse
  - root-reading
findings:
- finding_id: imported-process-roles
  issue_key: temperature-delta-mid1-imported-process-roles
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Imported relation roles conflict with current referents
  description: RO:0002213 inherits process domain and range from RO:0002211. Edge3
    has material acyl chains as its object, and edge4 relates those chemicals to a
    physical fluidity quality. Edge6 uses RO:0002327 with that explicit quality as
    subject despite its inherited material-entity domain through RO:0002215, RO:0002216,
    RO:0002500 and RO:0002595. These are formal representation conflicts, independent
    of biological efficacy. Edge2 can describe a temperature-decrease event, and edge5
    has explicit process endpoints; neither is included.
  target_ids:
  - METPO:1000485
  field_paths:
  - causal_graphs[0].edges[3].predicate_id
  - causal_graphs[0].edges[4].predicate_id
  - causal_graphs[0].edges[6].predicate_id
  evidence_ids:
  - nodes-edges
  - ro-primary
  - owners
  - predicate-mapping
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_delta_mid1.yaml
    role: Current assertion or documented conditional recurrence; preserve the recorded
      replay guards.
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Current assertion or documented conditional recurrence; preserve the recorded
      replay guards.
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Current assertion or documented conditional recurrence; preserve the recorded
      replay guards.
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: human-acceptance-link
  issue_key: temperature-delta-mid1-human-acceptance-link
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Reviewed status lacks locally attributable acceptance
  description: Current REVIEWED status has no attributable human acceptance link in
    the inspected local evidence. The ignored- and hidden-inclusive search, excluding
    .git and .venv, found164 matching paths and67 actual review target arrays with
    no exact target. Nine embedded events comprise eight AI events and one seed event.
    This is a bounded non-blocking provenance gap; private or remote acceptance remains
    unknown.
  target_ids:
  - METPO:1000485
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
    path: data/traits/environment/temperature_delta_mid1.yaml
    role: Current assertion or documented conditional recurrence; preserve the recorded
      replay guards.
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
actions:
- action_id: resolve-imported-process-roles
  description: In separately authorized curation, align the selected relationship
    groundings with their actual process, material and quality referents. Review the
    shared mapping for future empty fields while preserving compatible event/process
    cases. The grounder skips populated IDs, so a mapping rerun alone cannot repair
    these current fields. Keep exact numerical source attribution unresolved until
    directly supported.
  finding_ids:
  - imported-process-roles
  target_ids:
  - METPO:1000485
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_delta_mid1.yaml
    role: Current assertion or documented conditional recurrence; preserve the recorded
      replay guards.
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Current assertion or documented conditional recurrence; preserve the recorded
      replay guards.
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Current assertion or documented conditional recurrence; preserve the recorded
      replay guards.
  acceptance_checks:
  - Document compatible ontology roles for each current referent without asserting
    unreviewed biological efficacy.
  - Preserve already-correct membrane-fluidity QUALITY and compatible process/event
    cases; do not assign sibling scripts as current owners.
  - Run focused strict validation, relevant graph and predicate audits, full QC and
    required history/product gates after authorized curation.
- action_id: resolve-human-acceptance-link
  description: Link attributable human acceptance of the current assertions, or reconcile
    REVIEWED through the native status workflow in separately authorized curation.
    Preserve existing actor attribution.
  finding_ids:
  - human-acceptance-link
  target_ids:
  - METPO:1000485
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_delta_mid1.yaml
    role: Current assertion or documented conditional recurrence; preserve the recorded
      replay guards.
  acceptance_checks:
  - The human reviewer and current accepted scope are attributable, or the status
    accurately reflects available evidence.
  - Required per-record and repository history validates and AI assistance remains
    explicit.
limitations:
- 'UNKNOWN: inspected generic membrane or high-temperature context does not establish
  the exact 10–20 °C class calibration or moderate-flexibility causal bridge. Unavailable
  bodies are not paper-wide absence or biological refutation.'
- Noll exact body attribution remains unknown; publication identity is positive and
  missing body is not negative source evidence.
- Generic compositional and signaling attribution does not establish universal taxon
  efficacy, exact bin membership or a causal mechanism for breadth.
- Detailed pathogen fitness/AMR/ROS/defense and intervention mechanisms are UNASSESSED_SCOPE.
- Canonical statement is strain/source scoped; no phenotype transfer from taxonomy
  alone.
- Node2 moderate capacity/process wording remains qualified; no forced reservoir CAPACITY
  retyping.
- Edges7/8 operational quantity/class modeling remains qualified; no automatic QUALITY-to-TRAIT
  or invented local hard-domain violation.
- Existential OWL restriction is not a complete measured-range or causal verification.
- Exact quantitative/source efficacy is audited separately; detailed pathogen survival/fitness/ROS/AMR/intervention
  biology UNASSESSED_SCOPE.
- One uncaptured history and one script lead are matching-line-only context, not whole-body
  authority.
- Initial official taxonomy DNS failure is preserved separately from successful primary
  XML.
- Retained catalog absence is canonical-only; source species coverage can be positive
  and detailed module queries were not executed.
- Private/remote human acceptance remains unknown.
- Browser evidence is actual retained tool output, not raw article text; uninstrumented
  first-call and origin/cache-fetch times are not invented. Original acquisitions
  differ from copy/read times.
- Historical common failures, retries and no-adapter skips remain explicit; qualified
  B12 QC is not a new B13 execution or remote publication.
notes:
- Whole 250-line target, 91 captured inputs, six works, twelve external placements,
  twelve grounding fields, eleven nodes and nine edges reviewed.
- Twelve current history projections reuse twelve unchanged prior whole-file readings.
  One uncaptured history and one script were matching-line context only.
- The bounded scratch serializer runs once after root FINAL. Root independently inspects
  the actual YAML and runs native output validation before any save.
tags:
- record-review
- temperature-delta-mid1
- environment
- needs-curation
```
