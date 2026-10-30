# Whole-record review of temperature optimum mid2

- Review: 20261022T012848Z-temperature-optimum-mid2
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-22T01:23:17.880044Z
- Finished UTC: 2026-10-22T01:28:48Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Temperature optimum mid2 needs correction of three imported relations, one category/state facet and two evidence-note wording issues. Human acceptance needs attribution. Active bin identity, the reported28°C canonical optimum and all four literal snippets are supported; exact calibration and synonym equivalence remain unresolved.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: Second record in the actual B14 queue; current 245-line target and 98 captured inputs. Local review is independent of remote publication.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 508ee3089c93a36413969cd1ede7f9528a1940a4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| METPO:1000444 | data/traits/environment/temperature_optimum_mid2.yaml | maintained | temperature optimum mid2 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Fresh B14 corpus QC | passed | True | METPO:1000444 | Actual just qc passed: strict validation of 1130 records with 0 errors; graph audit: 74 baselined, 0 new and 0 blocking findings; 135 connected graphs and 1588 wired nodes; protein coverage: 729 graphs (134 pass, 594 NONMECHANISTIC, 0 gaps, 1 protected); snippet audit: 2419 baselined, 0 new and 0 blocking findings; 19 PathwayMech links. These are corpus diagnostics, not scientific validation of this target. |
| Fresh B14 history integrity | passed | True | METPO:1000444 | 1278 HistoryRecord YAMLs validated, 0 invalid; current history snapshot contains 1279 files. Integrity does not establish scientific correctness or human acceptance. |
| Fresh B14 mapping identifier/label validation | passed | True | METPO:1000444 | 361 canonical matches, 2 exact-synonym matches, 1 exception and 123 SKIPPED_NO_ADAPTER pairs. Configured scope is the two grounding mappings, not every target identifier or scientific claim. |
| Focused Stage2 writer tests | passed | False | METPO:1000444 | Five tests passed in the explicitly selected Stage2 test file. This is not a full just test run or biological validation. |
| Focused native validation | passed | True | METPO:1000444 | Native record validation passed; scientific interpretation is assessed separately. |
| Focused strict validation | passed | True | METPO:1000444 | The actual validate-strict command passed. |
| Focused network snippet check | passed | True | METPO:1000444 | All four supplied snippets were VERIFIED by the native abstract check and independently literal in the source audit. Literal occurrence does not establish adjacent numerical or causal claims. |
| One-target native review capture | passed | True | METPO:1000444 | One current target, 98 captured inputs, exact current base and successful native inspect. |
| Protein-instance metadata applicability | not_applicable | False | METPO:1000444 | No protein nodes or instances in this quantitative NONMECHANISTIC graph; no accession or token instance is required. |
| Structured source-organism expression query availability | unavailable | False | METPO:1000444 | Current bounded discovery found the maintained adapter unavailable. Retained species catalog and selected primary fallback establish no exact strain or module membership result. |

## Scientific And Domain Assessments

### Native checklist: active class, aliases and direct parent

identity: supported. Targets: METPO:1000444.

Active METPO:1000444 and parent METPO:1000304 agree with the local quantitative bin. Current mesophilic alias inheritance is documentary; legacy spelling provenance and exact scientific equivalence remain qualified.

### Native checklist: best-growth temperature and numerical calibration

quantity: unknown. Targets: METPO:1000444.

The inclusive 27–30 degree interval is explicit in local identity. Generic membrane adaptation does not establish exact cutoff calibration or sufficient whole-organism optima; a 20–45 growth interval does not prove an optimum outside this bin.

### Native checklist: exact taxon and reported optimum

quantity: supported. Targets: METPO:1000444.

Official Pontibacterium sinense identity and N1Y112 aliases agree. The assigned abstract reports optimum 28 degrees C and growth at 20–35 degrees C; these are distinct strain-specific observations, not an exhaustive response curve.

### Native checklist: five works and all placements

evidence: unknown. Targets: METPO:1000444.

All five identities are verified. Exact-bin calibration and baseline causal sufficiency remain unresolved. The Tolner note needs high-temperature scope qualification, and the written saturated/unsaturated ratio contradicts its stated direction toward UFAs. These are bounded note concerns; no underlying generic physical relation is refuted. Detailed pathogen survival, fitness, ROS-defense, AMR and intervention mechanisms remain UNASSESSED_SCOPE.

### Native checklist: four snippets and evidence-note scope

evidence: supported. Targets: METPO:1000444.

All four snippets are literal and native VERIFIED. Literal occurrence is distinct from adjacent numerical or causal attribution; the high-temperature note remains a separate minor concern.

### Native checklist: all nine current referents

representation: concern. Targets: METPO:1000444.

Node 8 describes an organism category but is typed as molecular/bioenergetic STATE, a bounded facet concern. Material fatty acids and fluidity quality remain meaningful. Temperature decrease denotes an event. Baseline adaptation versus its repertoire result and rigidification versus rigidity quality remain qualified, without forced extra retyping.

{
  "grounding": [
    {
      "index": 0,
      "node_id": "temperature_optimum_mid2_trait",
      "label": "temperature optimum mid2",
      "node_type": "TRAIT",
      "grounding": "METPO:1000444",
      "outcome": "supported",
      "assessment": "Active optimum bin and direct parent; scientific synonym equivalence remains independent."
    },
    {
      "index": 1,
      "node_id": "temperature_optimum",
      "label": "temperature optimum",
      "node_type": "TRAIT",
      "grounding": "METPO:1000304",
      "outcome": "supported",
      "assessment": "Active temperature-optimum measurement phenotype parent."
    },
    {
      "index": 2,
      "node_id": "mesophilic_environment",
      "label": "mesophilic environment",
      "node_type": "ENVIRONMENTAL_FACTOR",
      "grounding": null,
      "outcome": "supported",
      "assessment": "Ambient27–30°C habitat condition, not automatically a process. Its lexical outgoing edge has no imported process domain."
    },
    {
      "index": 3,
      "node_id": "baseline_mesophile_adaptation",
      "label": "baseline mesophile adaptation",
      "node_type": "BIOLOGICAL_PROCESS",
      "grounding": null,
      "outcome": "qualified",
      "assessment": "Adaptation process is intended by type and edges, while membrane/enzyme repertoire wording describes an adapted result. Preserve this bounded ambiguity; no forced separate facet or replacement mechanism."
    },
    {
      "index": 4,
      "node_id": "temperature_decrease",
      "label": "temperature decrease",
      "node_type": "ENVIRONMENTAL_FACTOR",
      "grounding": null,
      "outcome": "supported",
      "assessment": "Explicit drop in ambient temperature denotes an event; ENVIRONMENTAL_FACTOR alone does not invalidate processual interpretation."
    },
    {
      "index": 5,
      "node_id": "membrane_rigidity",
      "label": "membrane rigidification",
      "node_type": "QUALITY",
      "grounding": null,
      "outcome": "qualified",
      "assessment": "Current QUALITY denotes increased bilayer order/thickness. Rigidification/phase-transition words also evoke a process; maintained exact membrane_rigidity decision supports the quality result. No additional forced retype."
    },
    {
      "index": 6,
      "node_id": "unsaturated_fatty_acids",
      "label": "unsaturated fatty acids",
      "node_type": "CHEMICAL",
      "grounding": "CHEBI:27208",
      "outcome": "supported",
      "assessment": "Material unsaturated-fatty-acid class; CHEBI27208 double-bond subset is meaningful."
    },
    {
      "index": 7,
      "node_id": "membrane_fluidity",
      "label": "membrane fluidity",
      "node_type": "QUALITY",
      "grounding": "METPO:1007505",
      "outcome": "supported",
      "assessment": "Explicit membrane-fluidity physical quality, consistent with local v3."
    },
    {
      "index": 8,
      "node_id": "mesophile_category",
      "label": "mesophile category",
      "node_type": "STATE",
      "grounding": null,
      "outcome": "concern",
      "assessment": "Label and description denote an organism category, while schema STATE means a molecular/bioenergetic state of a cell. Bounded facet precision minor: intended category remains legible; no forced replacement enum, CURIE or biological subclass inference."
    }
  ],
  "source": [
    {
      "index": 0,
      "node_id": "temperature_optimum_mid2_trait",
      "field_path": "causal_graphs[0].nodes[0]",
      "label": "temperature optimum mid2",
      "description": "Temperature optimum approximately 27–30 °C.",
      "status": "UNKNOWN",
      "assessment": "Local numerical bin definition; exact source cutoff calibration remains unknown.",
      "primary_locator": "Indexed abstract opening sentence; current publisher abstract line100 corroborates generic direction."
    },
    {
      "index": 1,
      "node_id": "temperature_optimum",
      "field_path": "causal_graphs[0].nodes[1]",
      "label": "temperature optimum",
      "description": "Ambient temperature supporting maximal growth.",
      "status": "SUPPORTED_DEFINITIONAL",
      "assessment": "Parent maximum-growth-temperature meaning is distinct from growth interval; no causal sufficiency inferred.",
      "primary_locator": "Indexed abstract strain/growth/optimum/type clauses; current publisher export lines48 and51."
    },
    {
      "index": 2,
      "node_id": "mesophilic_environment",
      "field_path": "causal_graphs[0].nodes[2]",
      "label": "mesophilic environment",
      "description": "Habitat ambient temperature in the 27–30 °C range.",
      "status": "UNKNOWN",
      "assessment": "Record stipulates habitat27–30; no specific habitat optimum universality established.",
      "primary_locator": "Indexed abstract opening sentence; current publisher abstract line100 corroborates generic direction."
    },
    {
      "index": 3,
      "node_id": "baseline_mesophile_adaptation",
      "field_path": "causal_graphs[0].nodes[3]",
      "label": "baseline mesophile adaptation",
      "description": "Standard mesophile membrane and enzyme repertoire matching a moderate ambient-temperature setpoint.",
      "status": "PARTIAL",
      "assessment": "Generic membrane adaptation is supported; combined standard enzyme/membrane repertoire and a specific setpoint remain broader than inspected source.",
      "primary_locator": "Indexed abstract opening sentence; current publisher abstract line100 corroborates generic direction."
    },
    {
      "index": 4,
      "node_id": "temperature_decrease",
      "field_path": "causal_graphs[0].nodes[4]",
      "label": "temperature decrease",
      "description": "A drop in ambient temperature below the growth setpoint.",
      "status": "SUPPORTED_GENERIC",
      "assessment": "Environmental temperature drop is the physical trigger in the selected introduction.",
      "primary_locator": "spectrum.xml zero-based .//body//p[1], first sentence fluidity definition and fourth/final sentence generic cooling/rigidification/thickening/gel."
    },
    {
      "index": 5,
      "node_id": "membrane_rigidity",
      "field_path": "causal_graphs[0].nodes[5]",
      "label": "membrane rigidification",
      "description": "Increased bilayer order/thickness and liquid-crystalline to gel transition of the cytoplasmic membrane.",
      "status": "SUPPORTED_GENERIC",
      "assessment": "Rigidification/thickening/gel transition is explicit generic physical context.",
      "primary_locator": "spectrum.xml zero-based .//body//p[1], first sentence fluidity definition and fourth/final sentence generic cooling/rigidification/thickening/gel."
    },
    {
      "index": 6,
      "node_id": "unsaturated_fatty_acids",
      "field_path": "causal_graphs[0].nodes[6]",
      "label": "unsaturated fatty acids",
      "description": "Membrane fatty acyl chains bearing one or more double bonds (CHEBI:27208).",
      "status": "SUPPORTED_GENERIC",
      "assessment": "Unsaturation means double bonds in fatty-acyl chains; selected generic composition context supports the referent. CHEBI identity independently audited.",
      "primary_locator": "cold-pmc.html zero-based all-HTML paragraphs: p10 classification clause, p17 generic phase/composition passage."
    },
    {
      "index": 7,
      "node_id": "membrane_fluidity",
      "field_path": "causal_graphs[0].nodes[7]",
      "label": "membrane fluidity",
      "description": "Physical fluidity/disorder state of the cytoplasmic membrane.",
      "status": "SUPPORTED_GENERIC",
      "assessment": "Membrane fluidity is a physical freedom-of-motion state; selected Spectrum first sentence supports this generic referent.",
      "primary_locator": "spectrum.xml zero-based .//body//p[1], first sentence fluidity definition and fourth/final sentence generic cooling/rigidification/thickening/gel."
    },
    {
      "index": 8,
      "node_id": "mesophile_category",
      "field_path": "causal_graphs[0].nodes[8]",
      "label": "mesophile category",
      "description": "Organisms growing between approximately 20 and 45 degrees C ambient temperature.",
      "status": "PARTIAL",
      "assessment": "Ramón classification clause reports mesophile growth around20–45. This is not a complete optimum criterion; organism-category/state representation is grounding scope.",
      "primary_locator": "cold-pmc.html zero-based all-HTML paragraphs: p10 classification clause, p17 generic phase/composition passage."
    }
  ]
}

### Native checklist: all eight current relations

consistency: concern. Targets: METPO:1000444.

RO role concerns are limited to edges 4, 5 and 6. Edge 4 has material/quality endpoints under process/process RO2213; edge 5 has a valid process subject but material object; edge 6 has a quality subject where RO2327 requires material, with a valid process object. Biolink causes has broad endpoints; the temperature-drop event is a positive control. Local confers, grounded hierarchy and two lexical predicates receive no invented constraints.

{
  "grounding": [
    {
      "index": 0,
      "subject": "mesophilic_environment",
      "predicate": "engages",
      "predicate_id": null,
      "object": "baseline_mesophile_adaptation",
      "outcome": "unknown",
      "assessment": "Lexical engages has no imported role constraints; exact optimum causal calibration remains source-scoped."
    },
    {
      "index": 1,
      "subject": "baseline_mesophile_adaptation",
      "predicate": "confers",
      "predicate_id": "METPO:2007700",
      "object": "temperature_optimum_mid2_trait",
      "outcome": "supported",
      "assessment": "Local confers broad causal-node endpoints and trait-object prose fit the declared adaptation/trait roles; exact27–30°C sufficiency remains unverified independently."
    },
    {
      "index": 2,
      "subject": "temperature_optimum_mid2_trait",
      "predicate": "is a",
      "predicate_id": "rdfs:subClassOf",
      "object": "temperature_optimum",
      "outcome": "supported",
      "assessment": "Current active bin has the declared active temperature-optimum parent. Its attached evidence-note attribution is a separate source question."
    },
    {
      "index": 3,
      "subject": "temperature_decrease",
      "predicate": "causes",
      "predicate_id": "biolink:causes",
      "object": "membrane_rigidity",
      "outcome": "supported",
      "assessment": "Actual Biolink causes ancestry has NamedThing endpoints, not inherited RO2326 material/process restrictions. Explicit temperature-drop event and rigidity quality do not establish a formal endpoint failure; transition/result wording stays qualified."
    },
    {
      "index": 4,
      "subject": "unsaturated_fatty_acids",
      "predicate": "increases",
      "predicate_id": "RO:0002213",
      "object": "membrane_fluidity",
      "outcome": "concern",
      "assessment": "RO2213 inherits process/process roles; material fatty acids and fluidity quality both conflict with those roles."
    },
    {
      "index": 5,
      "subject": "baseline_mesophile_adaptation",
      "predicate": "increases",
      "predicate_id": "RO:0002213",
      "object": "unsaturated_fatty_acids",
      "outcome": "concern",
      "assessment": "RO2213 requires a process object. The adaptation process subject can fit, but the explicit fatty-acid material object does not."
    },
    {
      "index": 6,
      "subject": "membrane_fluidity",
      "predicate": "enables",
      "predicate_id": "RO:0002327",
      "object": "baseline_mesophile_adaptation",
      "outcome": "concern",
      "assessment": "RO2327 inherits material-domain/process-range through2215/2216/2500/2595. Current membrane-fluidity quality is not a material executor. Adaptation process object is a positive range control, subject to its wording qualification."
    },
    {
      "index": 7,
      "subject": "temperature_optimum_mid2_trait",
      "predicate": "subclass of",
      "predicate_id": null,
      "object": "mesophile_category",
      "outcome": "qualified",
      "assessment": "Lexical subclass of is not a grounded rdfs assertion. Current organism-category object has a separate bounded STATE facet issue; a reported growth interval alone does not independently establish an optimum equivalence or universal subset. Source scope remains qualified without another imported-role finding."
    }
  ],
  "source": [
    {
      "index": 0,
      "field_path": "causal_graphs[0].edges[0]",
      "subject": "mesophilic_environment",
      "predicate": "engages",
      "object": "baseline_mesophile_adaptation",
      "description": "Mesophilic environments engage baseline mesophile adaptation.",
      "status": "PARTIAL",
      "assessment": "Generic temperature-linked lipid adaptation is supported; the specific27–30 environment and baseline outcome are not established by the inspected abstract.",
      "primary_locator": "Indexed abstract opening sentence; current publisher abstract line100 corroborates generic direction.",
      "formal_role_scope": "Independent grounding audit; no source classification substitutes for endpoint typing."
    },
    {
      "index": 1,
      "field_path": "causal_graphs[0].edges[1]",
      "subject": "baseline_mesophile_adaptation",
      "predicate": "confers",
      "object": "temperature_optimum_mid2_trait",
      "description": "Baseline mesophile adaptation yields a 27–30 °C optimum.",
      "status": "UNKNOWN",
      "assessment": "Generic membrane adaptation does not establish a sufficient whole-organism27–30 optimum. Full article uninspected; no false-paper-absence claim.",
      "primary_locator": "Indexed abstract opening sentence; current publisher abstract line100 corroborates generic direction.",
      "formal_role_scope": "Independent grounding audit; no source classification substitutes for endpoint typing."
    },
    {
      "index": 2,
      "field_path": "causal_graphs[0].edges[2]",
      "subject": "temperature_optimum_mid2_trait",
      "predicate": "is a",
      "object": "temperature_optimum",
      "description": "Temperature optimum mid2 is a quantitative bin of the temperature-optimum phenotype.",
      "status": "CONCERN",
      "assessment": "Literal high-temperature thermophile passage does not supply the adjacent specific27–30 optimum attribution. Local subclass hierarchy is assessed independently.",
      "primary_locator": "Indexed abstract opening two sentences and retained author portal: thermophiles/high temperatures.",
      "formal_role_scope": "Independent grounding audit; no source classification substitutes for endpoint typing."
    },
    {
      "index": 3,
      "field_path": "causal_graphs[0].edges[3]",
      "subject": "temperature_decrease",
      "predicate": "causes",
      "object": "membrane_rigidity",
      "description": "A temperature drop rigidifies and thickens the cytoplasmic membrane.",
      "status": "SUPPORTED_GENERIC",
      "assessment": "Assigned introduction explicitly states generic cooling causes rigidification, thickening and phase change; this does not establish bin-specific physiological efficacy.",
      "primary_locator": "spectrum.xml zero-based .//body//p[1], first sentence fluidity definition and fourth/final sentence generic cooling/rigidification/thickening/gel.",
      "formal_role_scope": "Independent grounding audit; no source classification substitutes for endpoint typing."
    },
    {
      "index": 4,
      "field_path": "causal_graphs[0].edges[4]",
      "subject": "unsaturated_fatty_acids",
      "predicate": "increases",
      "object": "membrane_fluidity",
      "description": "Higher unsaturated fatty acid content fluidizes and thins the bilayer.",
      "status": "SUPPORTED_WITH_NOTE_CONCERN",
      "assessment": "Generic UFA enrichment/fluidity direction is positive. The note reverses the stated ratio: increasing SFA/UFA cannot mean shifting toward UFA. This is a local explanatory-direction defect, independent of imported relation roles.",
      "primary_locator": "cold-pmc.html zero-based all-HTML paragraphs: p10 classification clause, p17 generic phase/composition passage.",
      "formal_role_scope": "Independent grounding audit; no source classification substitutes for endpoint typing."
    },
    {
      "index": 5,
      "field_path": "causal_graphs[0].edges[5]",
      "subject": "baseline_mesophile_adaptation",
      "predicate": "increases",
      "object": "unsaturated_fatty_acids",
      "description": "Homeoviscous mesophile adaptation raises unsaturated fatty acid content to offset cooling.",
      "status": "PARTIAL",
      "assessment": "Generic composition adjustment/increased unsaturation during cooling is supported; not a universal mesophile strategy or exact-bin efficacy claim. Current process-to-material relation is separately grounded.",
      "primary_locator": "cold-pmc.html zero-based all-HTML paragraphs: p10 classification clause, p17 generic phase/composition passage.",
      "formal_role_scope": "Independent grounding audit; no source classification substitutes for endpoint typing."
    },
    {
      "index": 6,
      "field_path": "causal_graphs[0].edges[6]",
      "subject": "membrane_fluidity",
      "predicate": "enables",
      "object": "baseline_mesophile_adaptation",
      "description": "Maintained membrane fluidity supports the baseline mesophile physiological state.",
      "status": "UNASSESSED_SCOPE",
      "assessment": "Generic membrane fluidity is meaningful; detailed sensing/correction and efficacy of the specific desaturation system are outside the declared review scope. The cited paper is B.subtilis-specific and must not imply universal or27–30-bin efficacy.",
      "primary_locator": "spectrum.xml zero-based .//body//p[1], first sentence fluidity definition and fourth/final sentence generic cooling/rigidification/thickening/gel.",
      "formal_role_scope": "Independent grounding audit; no source classification substitutes for endpoint typing."
    },
    {
      "index": 7,
      "field_path": "causal_graphs[0].edges[7]",
      "subject": "temperature_optimum_mid2_trait",
      "predicate": "subclass of",
      "object": "mesophile_category",
      "description": "The 27-30 C optimum falls within the mesophile growth range.",
      "status": "PARTIAL",
      "assessment": "The reported mesophile20–45 growth-range wording and arithmetic containment are positive. Growth interval is distinct from an optimum-based exact synonym or exhaustive organism classification; complete identity inference remains UNKNOWN.",
      "primary_locator": "cold-pmc.html zero-based all-HTML paragraphs: p10 classification clause, p17 generic phase/composition passage.",
      "formal_role_scope": "Independent grounding audit; no source classification substitutes for endpoint typing."
    }
  ]
}

### Native checklist: maintained writers and recurrence

ownership: supported. Targets: METPO:1000444.

Current populated RO assertions are record-owned; wildcard increases/enables mappings can recur only for empty IDs and the shared grounder skips existing IDs. Node 8 facet is record-only. Process-quality migration preserves the current rigidity rationale but its absent maximal-growth edge guard excludes it from current RO repair. Exact canonical backfill has the matching tuple and equality guard; alias and sibling discoveries remain qualified context.

### Native checklist: attributable human acceptance

provenance: concern. Targets: METPO:1000444.

Twelve embedded events comprise eleven AI events and one seed. Ignored- and hidden-inclusive search found 176 matching paths and 67 actual target arrays, none exact. One current whole and seventeen qualified prior whole history readings do not establish attributable human acceptance of current assertions; private or remote acceptance remains unknown.

### Native checklist: catalog coverage and adapter availability

completeness: unknown. Targets: METPO:1000444.

The retained catalog covers B.subtilis and E.coli source species but no exact canonical Pontibacterium entry. No strain or module substitution is made. Appropriate generic queries were not executed because bounded current discovery found the maintained adapter unavailable; selected primary context is fallback.

### Native checklist: graph scope and optional protein instances

completeness: supported. Targets: METPO:1000444.

Two components, nine nodes and eight edges form a quantitative NONMECHANISTIC record. Zero protein nodes or instances do not require fabricated molecular details or graph connectors. Detailed excluded biological efficacy remains unassessed.

### Native checklist: actual native and fresh B14 diagnostics

schema: supported. Targets: METPO:1000444.

Current native capture, focused validation, strict validation and all four snippet fields passed. B14 common checks are actual fresh executions at the advanced base; historical failures, cache provenance, product skips and the omitted full test suite remain explicit. These diagnostics do not certify scientific meaning.

## Findings

### imported-process-roles: Imported process roles

major / open / confirmed; issue key: temperature-optimum-mid2-imported-process-roles.

Three grounded relations conflict with their actual endpoint referents. RO:0002213 inherits process domain and range: edge4 has material fatty acids and a fluidity quality, while edge5 has a material fatty-acid object despite its compatible adaptation-process subject. Edge6 uses RO:0002327 with a fluidity-quality subject instead of a material executor; the adaptation-process object fits the inherited process range subject to its wording qualification. The material domain follows2327→2215→2216→2500→2595. Biolink causes has its own broad NamedThing endpoints, and the explicit temperature drop is an event. Two lexical predicates receive no invented imported constraints.

### organism-category-state-facet: Organism category state facet

minor / open / confirmed; issue key: temperature-optimum-mid2-organism-category-state-facet.

The mesophile-category label and description consistently denote a category of organisms, while schema STATE denotes a bioenergetic or molecular state of a cell. The intended category remains legible, so this is a bounded facet-precision concern. It does not establish scientific synonym equivalence or a universal optimum-based subclass, and the lexical subclass edge7 is not an imported rdfs assertion.

### high-temperature-source-placement: High temperature source placement

minor / open / confirmed; issue key: temperature-optimum-mid2-high-temperature-source-placement.

The literal Tolner passage explicitly concerns thermophiles adapted to high temperatures, while its adjacent note attributes specific27–30°C optimum support to that passage. Qualify the nearest-evidence attribution. The active local subclass hierarchy is independently supported by METPO; no whole-paper absence or false hierarchy is asserted.

### fatty-acid-ratio-direction: Fatty acid ratio direction

minor / open / confirmed; issue key: temperature-optimum-mid2-fatty-acid-ratio-direction.

The note says increasing the saturated/unsaturated ratio moves toward unsaturated fatty acids. Increasing SFA/UFA instead shifts the proportion toward saturated fatty acids, contradicting the stated UFA-rich direction and the edge description. Generic increased-unsaturation/fluidity context is supported; this is a bounded mathematical wording defect, separate from the imported-relation concern and not a proposed intervention.

### human-acceptance-link: Human acceptance link

minor / open / confirmed; issue key: temperature-optimum-mid2-human-acceptance-link.

Current REVIEWED status lacks attributable human acceptance of present assertions in the inspected local evidence. The ignored- and hidden-inclusive search, excluding .git/.venv, found176 matching paths and67 actual review target arrays with no exact target. Twelve embedded events comprise11 AI events and one seed;18 captured infrastructure/sibling histories contain no exact-target acceptance record. One current whole history and17 qualified prior whole readings are explicitly distinguished. Private or remote acceptance remains unknown.

## Recommended Actions And Acceptance Checks

### curate-imported-process-roles

In separately authorized curation, reconcile the three grounded predicates with their actual material, quality and process referents. Preserve valid node identities and avoid inventing a replacement mechanism. Review wildcard increases/enables mapping recurrence together with record assertions; the grounder skips populated IDs, so rerunning it alone does not repair the current graph. The process-quality rigidity rule provides positive context and does not currently rewrite these edges.

- Demonstrate inherited domain/range compatibility with actual referents, retaining the valid process endpoints and broad Biolink/event positive controls.
- Retain NONMECHANISTIC scope, two contextual components and zero proteins unless independent evidence warrants a change; do not fabricate connectors or token instances.
- Run focused strict validation, relevant graph/predicate audits, full QC and required curation history/product gates.

### curate-organism-category-state-facet

Clarify how the existing organism-category concept is represented within the graph or its classification context. Reconcile the STATE field with the schema meaning without automatically substituting an enum or CURIE. Keep the optimum-versus-growth-range and exact-synonym questions explicitly separate.

- The node referent and chosen representation agree with the maintained schema, with any necessary scope decision documented.
- Do not assert an imported rdfs relation or universal organism classification merely from lexical wording or interval containment.
- Validate the focused record, graph/schema checks and curation history after authorized changes.

### curate-high-temperature-source-placement

Qualify the source note to distinguish the literal high-temperature context from the independently supported numeric-bin hierarchy. Attach exact numerical support only where a relevant passage was inspected. Preserve the positive literal snippet and source provenance.

- The nearest-evidence note accurately states the inspected passage and does not imply unestablished27–30°C support.
- Retain independent hierarchy support and explicit full-paper access limits.
- Validate evidence/snippet fields, curation history and strict/QC gates.

### curate-fatty-acid-ratio-direction

Reconcile the written numerator/denominator and direction with the intended UFA-rich meaning. Keep this as a correction to the explanatory note; no biological optimization or new mechanism is required.

- The direction stated for SFA/UFA is mathematically consistent with the intended compositional meaning.
- Preserve the distinction between generic physical source support and unresolved exact-bin or organism-wide efficacy.
- Validate the edited evidence note, history and focused strict/QC gates.

### curate-human-acceptance-link

Link attributable human acceptance of current assertions or reconcile REVIEWED through the native status workflow in separately authorized curation. Preserve existing AI actors and history.

- Accepted assertion scope and human reviewer are attributable, or status reflects the available evidence.
- Per-record and repository history validates and AI assistance remains explicit.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| fresh-common-completion | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/new-base-diagnostic-independent-review-agent/fresh-products-completion.json; Fresh products completion plus prior diagnostic evidence; original execution intervals retained | context_only | Actual B14 checks and current input guards; setup cross-batch comparison remains false. |
| check-new-base-qc | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/new-base-qc.log; Executed 2026-10-21T23:25:15.125723+00:00 through 2026-10-21T23:26:53.864156+00:00; metadata new-base-qc.json | context_only | Actual just qc passed: strict validation of 1130 records with 0 errors; graph audit: 74 baselined, 0 new and 0 blocking findings; 135 connected graphs and 1588 wired nodes; protein coverage: 729 graphs (134 pass, 594 NONMECHANISTIC, 0 gaps, 1 protected); snippet audit: 2419 baselined, 0 new and 0 blocking findings; 19 PathwayMech links. These are corpus diagnostics, not scientific validation of this target. |
| check-new-base-history | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/new-base-history.log; Executed 2026-10-21T23:25:15.125609+00:00 through 2026-10-21T23:25:19.527774+00:00; metadata new-base-history.json | context_only | 1278 HistoryRecord YAMLs validated, 0 invalid; current history snapshot contains 1279 files. Integrity does not establish scientific correctness or human acceptance. |
| check-new-base-products | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/new-base-products.log; Executed 2026-10-21T23:29:02.243310+00:00 through 2026-10-21T23:29:27.250859+00:00; metadata new-base-products.json | context_only | 361 canonical matches, 2 exact-synonym matches, 1 exception and 123 SKIPPED_NO_ADAPTER pairs. Configured scope is the two grounding mappings, not every target identifier or scientific claim. |
| check-new-base-stage2-tests | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/new-base-stage2-tests.log; Executed 2026-10-21T23:25:19.981459+00:00 through 2026-10-21T23:25:21.660071+00:00; metadata new-base-stage2-tests.json | context_only | Five tests passed in the explicitly selected Stage2 test file. This is not a full just test run or biological validation. |
| historical-validate-products | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log; Historical original execution 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z | context_only | Historical products exit 2; preserved provenance only, superseded for B14 by its actual fresh products run. |
| historical-validate-products-retry-local | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log; Historical original execution 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z | context_only | Historical products exit 2; preserved provenance only, superseded for B14 by its actual fresh products run. |
| historical-validate-products-retry-network | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log; Historical original execution 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z | context_only | Historical products exit 0; preserved provenance only, superseded for B14 by its actual fresh products run. |
| check-temperature-optimum-mid2-validate | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-validate.log; Executed 2026-10-22T01:23:37.222495+00:00 through 2026-10-22T01:23:38.051614+00:00; metadata temperature-optimum-mid2-validate.json | context_only | Native record validation passed; scientific interpretation is assessed separately. |
| check-temperature-optimum-mid2-strict | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-strict.log; Executed 2026-10-22T01:23:37.222463+00:00 through 2026-10-22T01:23:38.707395+00:00; metadata temperature-optimum-mid2-strict.json | context_only | The actual validate-strict command passed. |
| check-temperature-optimum-mid2-snippets-network | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-snippets-network.log; Executed 2026-10-22T01:23:47.479566+00:00 through 2026-10-22T01:23:50.948948+00:00; metadata temperature-optimum-mid2-snippets-network.json | context_only | All four supplied snippets were VERIFIED by the native abstract check and independently literal in the source audit. Literal occurrence does not establish adjacent numerical or causal claims. |
| capture | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2.inspect.json; Actual successful native inspect with 98 captured inputs | context_only | All current source hashes and the exact target are bound before serialization. |
| record | data/traits/environment/temperature_optimum_mid2.yaml; Whole current record | supports | Nine nodes, eight edges, twelve embedded events, one canonical example and no protein classes or instances. |
| local-init | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/batch014-local-initialization-receipt.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Actual local initialization and second queue target; publication remains separate. |
| policy | docs/GROUNDING_POLICY.md; Captured maintained authority | supports | Protein family/function grounding and optional protein instances. |
| playbook | docs/CURATION_PLAYBOOK.md; Captured maintained authority | supports | Literal source scope and attributable acceptance. |
| schema | src/traitmech/schema/traitmech.yaml; Captured maintained authority | supports | Current facets and NONMECHANISTIC scope. |
| predicate-mapping | mappings/predicate_grounding.tsv; Captured maintained authority | supports | Wildcard increases mapping can populate empty IDs; current populated assertions are skipped. |
| node-mapping | mappings/node_grounding.tsv; Captured maintained authority | supports | Current label/type keys and qualified mappings. |
| identity | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-ground-agent/identity-assessment.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Active exact bin, direct parent and qualified historical aliases. |
| nodes-edges | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-ground-agent/node-edge-grounding-ledger.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | All nine node and eight edge judgments with positive controls. |
| owners | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-ground-agent/owner-provenance-assessment.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Populated-ID skip guards and exact canonical backfill distinguished from discovery-only leads. |
| owner-primary | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-ground-agent/owner-primary-reading.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Actual maintained writer and migration decision windows. |
| human-search | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-ground-agent/search-and-provenance.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | 176 ignored- and hidden-inclusive matching paths, 67 actual review target arrays, zero exact target. |
| histories | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-ground-agent/history-reading-provenance.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | One current whole history plus seventeen qualified prior whole readings; eighteen current projections. |
| discovery | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-ground-agent/discovery-disposition.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Two uncaptured history leads and three scripts remain matching-line context. |
| alias-discovery | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-ground-agent/alias-writer-discovery-only.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Additional uncaptured alias writer remains discovery-only, not a fully read current owner. |
| expression | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-ground-agent/expression-and-readiness.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Species catalog coverage is separate from exact strain or module support; adapter unavailable. |
| expression-discovery | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-ground-agent/expression-runner-current-discovery.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Fresh bounded PATH/project/install-root discovery, not global absence. |
| local-authority | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-ground-agent/local-authority-reading.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Exact current v3/v8, Biolink causes ancestry, mappings and schema windows. |
| ground-reading | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-ground-agent/reading-scope-receipt.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Actual current and qualified prior reading scopes. |
| ground-manifest | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-ground-agent/evidence-manifest.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | All 31 frozen ground artifacts verified. |
| metpo-primary | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/repo/data/raw/metpo.owl; Selected actual primary statements at the recorded reading time | supports | Active bin and parent, inclusive 27–30 Cel restriction and raw alias provenance. |
| metpo-primary-projection | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-ground-agent/metpo-authority.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Exact primary source hash and selected statement projection. |
| chebi-primary | /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/chebi.db; Selected actual primary statements at the recorded reading time | supports | Fatty-acid classes encompass the current meaningful material referents. |
| chebi-primary-projection | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-ground-agent/selected-chebi-primary-reading.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Exact primary source hash and selected statement projection. |
| ro-primary | /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/ro.db; Selected actual primary statements at the recorded reading time | supports | RO:0002213 inherits process/process roles; RO:0002327 inherits material/process roles through enables and the causal ancestry. |
| ro-primary-projection | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-ground-agent/selected-ro-primary-reading.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Exact primary source hash and selected statement projection. |
| mendoza-metadata | DOI:10.1146/annurev-micro-091313-103612; Indexed identity/status and opening generic abstract sentence | supports | Generic unsaturation and sensing context; exact-bin sufficiency remains unknown. |
| mendoza-publisher | DOI:10.1146/annurev-micro-091313-103612; Retained actual browser abstract export, not raw HTML | supports | Original tool-call interval retained; origin cache-fetch time is unknown. |
| cold-metadata | DOI:10.1007/s42770-023-01057-4; Indexed identity/status and generic abstract | supports | Assigned review identity and generic membrane context. |
| cold-primary | DOI:10.1007/s42770-023-01057-4; Zero-based all-HTML paragraph 10 classification clause and paragraph 17 generic phase/composition passage | supports | Only stated generic classification and physical context adopted; no universal strategy or intervention efficacy. |
| tolner-metadata | DOI:10.1016/s0300-9629(97)00003-0; Indexed title/status and opening two high-temperature abstract sentences | supports | Literal high-temperature context does not establish the adjacent specific 27–30 degree optimum claim. |
| tolner-zero-hit | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016%2Fs0300-9629%2897%2900003-0&amp;format=json&amp;resultType=core; Original successful HTTP response with zero indexed matches | context_only | A retrieval diagnostic superseded for identity by the positive PMID and Crossref responses; not an absent-paper claim. |
| tolner-crossref | DOI:10.1016/s0300-9629(97)00003-0; Crossref identity metadata | supports | Positive identity after the original zero-hit DOI query. |
| tolner-author | DOI:10.1016/s0300-9629(97)00003-0; Retained author portal abstract, opening high-temperature sentences | supports | Independent abstract surface; not a full-paper absence judgment. |
| spectrum-primary | DOI:10.1128/spectrum.03925-23; Zero-based body paragraph 1, first sentence and fourth/final sentence | supports | Generic fluidity definition and cooling/rigidification/thickening/phase context only; detailed regulation, assays, antimicrobial and intervention content unassessed. |
| spectrum-metadata | DOI:10.1128/spectrum.03925-23; Indexed identity/status | supports | Assigned B.subtilis study identity; detailed efficacy is outside scope. |
| canonical-metadata | DOI:10.1099/ijsem.0.006018; Indexed title/status and strain/growth/optimum abstract clauses | supports | N1Y112T reported optimum 28 degrees C, distinct from growth at 20–35 degrees C. |
| current-browser | DOI:10.1099/ijsem.0.006018; Actual root browser export copied by source auditor; canonical publisher abstract lines 48 and 51, Mendoza line 100 | partial | Canonical optimum support and generic unsaturation direction are positive. This is not raw HTML; recorded_at is export time only, with first-call bounds and original cache-fetch times unknown. |
| taxonomy | NCBITaxon:2781979; Whole successful retained official retry response; original acquisition time | supports | Pontibacterium sinense and N1Y112 type aliases are positive independently of phenotype support. |
| taxonomy-prior-failure | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=2781979&amp;retmode=xml; Original DNS-failure bytes; not official taxonomy content | context_only | Historical retrieval failure followed by successful official retry; not a current native validation failure. |
| taxonomy-copy | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-ground-agent/taxonomy-reuse.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Original failed/successful requests and current exact copy times are separate. |
| taxonomy-reading | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-ground-agent/taxonomy-identity.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Current official identity reading; no phenotype inference from taxonomy. |
| sources | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-source-agent/source-assessment.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Five works with overall UNKNOWN source scope and two bounded source-note findings. |
| source-identities | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-source-agent/source-identities-status.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | All assigned identities and bounded metadata notice fields. |
| placements | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-source-agent/source-placement-ledger.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | All eleven external placements and ten grounding fields accounted. |
| snippets | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-source-agent/snippet-ledger.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | All four supplied snippets literal; adjacent inference remains separate. |
| notes | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-source-agent/source-note-ledger.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | All nine evidence notes plus canonical note assessed within explicit scope. |
| source-nodes-edges | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-source-agent/node-edge-source-ledger.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | All nine nodes and eight edges with qualified physical/source attribution. |
| classification | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-source-agent/classification-assessment.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Mesophilic exactness remains unknown; a growth interval is not an outside-bin optimum. |
| canonical | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-source-agent/canonical-assessment.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Reported 28 degree optimum supports the bin, separately from the 20–35 growth interval. |
| source-reading | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-source-agent/primary-reading-scope.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Selected primary passages and explicit excluded detailed mechanism scope. |
| source-access | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-source-agent/source-access-limits.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Body access limits and prior browser observations are not substituted as current body evidence. |
| source-reuse | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-source-agent/source-reuse-receipt.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Original acquisition, current copy and current interpretation clocks are separate. |
| source-native | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-source-agent/native-check-context.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Four native VERIFIED fields and four manual literal matches. |
| source-manifest | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-source-agent/evidence-manifest.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | All 29 frozen source artifacts verified. |
| root-reading | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-source-root/selected-primary-reading.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Independent bounded primary/owner reading; root and ground current/prior whole-history scopes remain separately attributed. |
| adjudication | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-root-adjudication.json; Final root adjudication | supports | Exact finding fields, owner qualifications, actions and unresolved source scopes control serialization. |

## Limits And Additional Notes

- Full just test was NOT_RUN under the selected review-only diagnostic scope; only the five focused Stage2 tests are recorded. Products retains 123 no-adapter skips. Common checks establish bounded software/data integrity, not scientific support.
- Exact27–30 calibration, baseline causal sufficiency and exact mesophilic alias equivalence remain UNKNOWN; no outside-bin optimum inferred from20–45 growth wording.
- Mendoza and Tolner inspected abstracts/portal do not establish every adjacent numerical claim. Full articles not acquired; no paper-wide absence assertion.
- Spectrum actual body was available, but only generic membrane-fluidity and temperature/phase physical statements adopted; antimicrobial, biosensor, des-system efficacy and intervention details remain UNASSESSED_SCOPE.
- Ramón source is a broad review. Generic classification/phase/composition statements adopted; no universal organism strategy or intervention efficacy inferred.
- Canonical optimum28 and growth20–35 are separate reported strain observations; no full body or exhaustive response curve acquired.
- Publication notice checks use retained indexed fields and current official abstract identity only; no exhaustive up-to-the-minute retraction clearance.
- Original requests, present copying, extraction and current interpretation clocks remain separate. Current browser export is not raw HTML; its first-call start/end and origin cache-fetch times are unknown.
- All five abstracts were displayed for identity/context. Detailed transport, regulation, AMR/assay material displayed incidentally in Tolner/Spectrum/Ramón abstracts and the ratio-search hit p20 was not adopted, evaluated or developed.
- Full paragraph10 includes unrelated taxa after the mesophile clause; only the initial classification clause is adopted. No source-species catalog absence inferred.
- Scientific mesophilic exact equivalence is UNKNOWN from inspected growth-range wording alone; legacy Mesophilie provenance is not reconstructed.
- Baseline-adaptation repertoire/process and rigidity-transition/quality wording remain qualified without extra forced findings.
- Lexical edge7 is not imported rdfs; its optimum-versus-growth-range inference is source-scoped.
- Source note polarity/attribution and exact numeric causal bridge are separate from this grounding count.
- Two uncaptured histories/three node-script leads and the alias writer remain matching-line context, not full-body owner claims.
- B14 differs from B13; individual reused histories/authorities carry exact hashes and original reading/access receipts.
- Structured adapter unavailable within declared bounds; species-level source catalog coverage does not establish strain/module efficacy.
- Private/remote human acceptance and detailed dangerous-pathogen mechanisms remain unassessed.
- Root read18 actor/target/event projections and one complete process-quality history;17 prior whole readings are agent-qualified scope.
- Only successful taxonomy retry bytes support identity; original DNS-error text remains a separate diagnostic.
- Detailed pathogen survival, fitness, ROS-defense, AMR and intervention efficacy remain UNASSESSED_SCOPE.
- Historical products failures/retry and original cache provenance remain in /private/tmp/traitmech-record-sweep-014.q8m4v2cs/new-base-diagnostic-independent-review-agent/fresh-products-completion.json. The earlier outstanding-products status is superseded by the actual fresh run; no blanket cross-batch reuse qualification is asserted.
- Final finding fields, severities and actions are supplied only by actual root FINAL. Current scientific uncertainty is not converted into inherited numerical, alias or canonical findings.
- This serializer adopts frozen audits and root adjudication. Original acquisition, present copy/read and extraction scopes remain separate, including browser clock limits and historical taxonomy failure/retry. No scientific record, state, Git or publication change is performed by this serializer.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T012848Z-temperature-optimum-mid2
kind: record
repository: CultureBotAI/TraitMech
title: Whole-record review of temperature optimum mid2
started_at: '2026-10-22T01:23:17.880044Z'
finished_at: '2026-10-22T01:28:48Z'
reviewer:
  identity: codex
  kind: agent
  independence: independent
  independence_basis: Separate source and grounding audits plus root primary reading
    and final adjudication supply the scientific judgments. Serializer preparation
    does not claim an additional whole-paper scientific review.
  model: GPT-6 (Codex)
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Temperature optimum mid2 needs correction of three imported relations, one
  category/state facet and two evidence-note wording issues. Human acceptance needs
  attribution. Active bin identity, the reported28°C canonical optimum and all four
  literal snippets are supported; exact calibration and synonym equivalence remain
  unresolved.
source:
  git_revision: 508ee3089c93a36413969cd1ede7f9528a1940a4
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
  - path: data/traits/environment/temperature_optimum_mid2.yaml
    sha256: f97f6bddb24d09ee6fb58c83b569a84f10da84a59cb983b1c917d5ea68242245
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
  - path: history/records/homeoviscous_adaptation/2026-09-15T072704Z-codex-6cb554.yaml
    sha256: f82d94646e70fd82a5d3f6939339efae8ce0fe5e80fe6f50aab994de6c409fa8
    role: context
  - path: history/records/mesophilic/2026-09-04T004000Z-codex-14a39b.yaml
    sha256: cdf9710543d62277f232e633fca2dd146a1ae45dab75f957a5462929650accf0
    role: context
  - path: history/records/mesophilic/2026-09-04T130000Z-codex-183.yaml
    sha256: 3690075be370a302871b86f5f37fd70776296927d7b98c58d27af10dc2d2cc31
    role: context
  - path: history/records/mesophilic/2026-09-06T133000Z-codex-133a5b.yaml
    sha256: 1ae727f3ba27c1d3d05fdcdd488aa48b9369c3c4a71d3fb38521912a841ef51a
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
    sha256: 96c01dd8457ab2b91a6f90cb199eb99a32c649c9fba1ef0658ab407cfb009496
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
  - path: research/traits/environment/temperature_optimum_mid2-deep-research-falcon.md
    sha256: 566ee887525ddef81dd024e7c3e9684093194c086ebba166a5a5fc16b20cae33
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
  - path: scripts/enrich_lateral_flagellation_trait.py
    sha256: 841e82aad335fcb81d9ba6113b36eed8b35bb9c9f7ae1132effe6e2a1bae5520
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
- target_id: METPO:1000444
  path: data/traits/environment/temperature_optimum_mid2.yaml
  label: temperature optimum mid2
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_optimum_mid2.yaml
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
  selection: Second record in the actual B14 queue; current 245-line target and 98
    captured inputs. Local review is independent of remote publication.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - METPO:1000444
checks:
- check_id: new-base-qc
  name: Fresh B14 corpus QC
  status: passed
  required: true
  target_ids:
  - METPO:1000444
  command: just qc
  exit_code: 0
  expected_exit_code: 0
  summary: 'Actual just qc passed: strict validation of 1130 records with 0 errors;
    graph audit: 74 baselined, 0 new and 0 blocking findings; 135 connected graphs
    and 1588 wired nodes; protein coverage: 729 graphs (134 pass, 594 NONMECHANISTIC,
    0 gaps, 1 protected); snippet audit: 2419 baselined, 0 new and 0 blocking findings;
    19 PathwayMech links. These are corpus diagnostics, not scientific validation
    of this target.'
  evidence_ids:
  - check-new-base-qc
  - fresh-common-completion
  scope_note: Actual B14 execution at base 508ee3089c93a36413969cd1ede7f9528a1940a4.
    QC children share the recorded aggregate interval; no invented child times. Current
    source maps/cache bytes are rechecked; no prior-batch check is relabelled as fresh.
- check_id: new-base-history
  name: Fresh B14 history integrity
  status: passed
  required: true
  target_ids:
  - METPO:1000444
  command: just validate-history
  exit_code: 0
  expected_exit_code: 0
  summary: 1278 HistoryRecord YAMLs validated, 0 invalid; current history snapshot
    contains 1279 files. Integrity does not establish scientific correctness or human
    acceptance.
  evidence_ids:
  - check-new-base-history
  - fresh-common-completion
  scope_note: Actual B14 execution at base 508ee3089c93a36413969cd1ede7f9528a1940a4.
    QC children share the recorded aggregate interval; no invented child times. Current
    source maps/cache bytes are rechecked; no prior-batch check is relabelled as fresh.
- check_id: new-base-products
  name: Fresh B14 mapping identifier/label validation
  status: passed
  required: true
  target_ids:
  - METPO:1000444
  command: env PYSTOW_HOME=/private/tmp/traitmech-record-sweep.FU79Gr/pystow OAKLIB_HOME=/private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib
    SQLITE_TMPDIR=/private/tmp/traitmech-record-sweep.FU79Gr/sqlite-tmp just validate-products
  exit_code: 0
  expected_exit_code: 0
  summary: 361 canonical matches, 2 exact-synonym matches, 1 exception and 123 SKIPPED_NO_ADAPTER
    pairs. Configured scope is the two grounding mappings, not every target identifier
    or scientific claim.
  evidence_ids:
  - check-new-base-products
  - fresh-common-completion
  scope_note: Actual B14 execution at base 508ee3089c93a36413969cd1ede7f9528a1940a4.
    QC children share the recorded aggregate interval; no invented child times. Current
    source maps/cache bytes are rechecked; no prior-batch check is relabelled as fresh.
- check_id: new-base-stage2-tests
  name: Focused Stage2 writer tests
  status: passed
  required: false
  target_ids:
  - METPO:1000444
  command: uv run pytest tests/test_curate_stage2_causal_graphs.py -q
  exit_code: 0
  expected_exit_code: 0
  summary: Five tests passed in the explicitly selected Stage2 test file. This is
    not a full just test run or biological validation.
  evidence_ids:
  - check-new-base-stage2-tests
  - fresh-common-completion
  scope_note: Actual B14 execution at base 508ee3089c93a36413969cd1ede7f9528a1940a4.
    QC children share the recorded aggregate interval; no invented child times. Current
    source maps/cache bytes are rechecked; no prior-batch check is relabelled as fresh.
- check_id: temperature-optimum-mid2-validate
  name: Focused native validation
  status: passed
  required: true
  target_ids:
  - METPO:1000444
  command: just validate data/traits/environment/temperature_optimum_mid2.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Native record validation passed; scientific interpretation is assessed
    separately.
  evidence_ids:
  - check-temperature-optimum-mid2-validate
- check_id: temperature-optimum-mid2-strict
  name: Focused strict validation
  status: passed
  required: true
  target_ids:
  - METPO:1000444
  command: just validate-strict data/traits/environment/temperature_optimum_mid2.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: The actual validate-strict command passed.
  evidence_ids:
  - check-temperature-optimum-mid2-strict
- check_id: temperature-optimum-mid2-snippets-network
  name: Focused network snippet check
  status: passed
  required: true
  target_ids:
  - METPO:1000444
  command: just verify-snippets --record data/traits/environment/temperature_optimum_mid2.yaml
    --out /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-snippets.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: All four supplied snippets were VERIFIED by the native abstract check and
    independently literal in the source audit. Literal occurrence does not establish
    adjacent numerical or causal claims.
  evidence_ids:
  - check-temperature-optimum-mid2-snippets-network
- check_id: native-inspect
  name: One-target native review capture
  status: passed
  required: true
  target_ids:
  - METPO:1000444
  command: uv run python scripts/record_review.py inspect --targets /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2.targets.json
    --input .claude/skills/curate-yaml-record/references/review-checklist.md --input
    .claude/skills/manage-identifiers/SKILL.md --input .claude/skills/review-yaml-record/SKILL.md
    --input CLAUDE.md --input DO_NOT_WORK.md --input conf/evidence_snippet_baseline.tsv
    --input conf/record_review.yaml --input data/raw/biolink-model.yaml --input data/raw/metpo.owl
    --input data/traits/environment/temperature_optimum.yaml --input docs/CURATION_PLAYBOOK.md
    --input docs/GROUNDING_POLICY.md --input docs/PATHWAY_LINKS.md --input docs/record-review-profile.md
    --input docs/record-reviews.md --input history/infrastructure/node-type-consistency/2026-08-15T014631Z-claude-code-9d7f4d.yaml
    --input history/infrastructure/pr664-adversarial-review/2026-09-07T010000Z-codex-60bca2.yaml
    --input history/infrastructure/process-quality-consistency/2026-08-21T073211Z-codex-174227.yaml
    --input history/other/canonical-examples-batch1/2026-08-20T074839Z-claude-code-6fb2f5.yaml
    --input history/other/canonical-examples-six/2026-08-21T065406Z-codex-a1ab82.yaml
    --input history/records/homeoviscous_adaptation/2026-09-15T072704Z-codex-6cb554.yaml
    --input history/records/mesophilic/2026-09-04T004000Z-codex-14a39b.yaml --input
    history/records/mesophilic/2026-09-04T130000Z-codex-183.yaml --input history/records/mesophilic/2026-09-06T133000Z-codex-133a5b.yaml
    --input history/records/temperature_optimum/2026-09-15T070759Z-codex-e0d923.yaml
    --input history/records/temperature_optimum_high/2026-09-04T032000Z-codex-f0b8c3.yaml
    --input history/records/temperature_optimum_high/2026-09-04T200000Z-codex-183.yaml
    --input history/records/temperature_optimum_high/2026-09-08T033000Z-codex-506e08.yaml
    --input history/records/temperature_optimum_mid1/2026-09-15T070759Z-codex-35d0a7.yaml
    --input history/records/temperature_optimum_mid3/2026-09-15T070800Z-codex-44b4c3.yaml
    --input history/records/temperature_optimum_very_low/2026-09-04T034000Z-codex-1f380e.yaml
    --input history/records/temperature_optimum_very_low/2026-09-04T210000Z-codex-183.yaml
    --input history/records/temperature_optimum_very_low/2026-09-08T032500Z-codex-77dafe.yaml
    --input justfile --input mappings/node_grounding.tsv --input mappings/predicate_grounding.tsv
    --input mappings/trait_exact_match_review.tsv --input mappings/uniprot_regrounding_candidates.tsv
    --input proposals/metpo_traitmech_v3/metpo_proposal_classes_robot.tsv --input
    proposals/metpo_traitmech_v3/proposal.md --input proposals/metpo_traitmech_v8/metpo_proposal_properties_robot.tsv
    --input proposals/metpo_traitmech_v8/proposal.md --input proposals/metpo_traitmech_v9/metpo_proposal_properties_robot.tsv
    --input proposals/metpo_traitmech_v9/proposal.md --input reports/metpo_2026_06_12_active_review.tsv
    --input reports/metpo_2026_06_12_release_delta.tsv --input reports/ontology_snapshot_manifest.tsv
    --input research/traits/environment/temperature_optimum_mid2-deep-research-falcon.md
    --input schema/record_review.yaml --input scripts/add_homeoviscous_adaptation_trait.py
    --input scripts/audit_causal_graphs.py --input scripts/audit_graph_protein_taxa.py
    --input scripts/audit_predicate_domains.py --input scripts/audit_unapplied_groundings.py
    --input scripts/audit_uniprot_grounding.py --input scripts/backfill_canonical_examples_444.py
    --input scripts/connect_mesophilic_graph_183.py --input scripts/connect_temperature_delta_high_graph_183.py
    --input scripts/connect_temperature_delta_very_low_graph_183.py --input scripts/connect_temperature_optimum_high_graph_183.py
    --input scripts/connect_temperature_optimum_very_low_graph_183.py --input scripts/connect_temperature_range_mid3_graph_183.py
    --input scripts/connect_temperature_range_mid4_graph_183.py --input scripts/connect_temperature_range_very_low_graph_183.py
    --input scripts/enrich_lateral_flagellation_trait.py --input scripts/finalize_metpo_2026_06_12_review.py
    --input scripts/ground_causal_nodes.py --input scripts/ground_causal_predicates.py
    --input scripts/migrate_disposition_typing.py --input scripts/migrate_enables_range_edges.py
    --input scripts/migrate_enables_trait_edges.py --input scripts/migrate_metpo_2026_06_12.py
    --input scripts/migrate_microbe_domain_edges.py --input scripts/migrate_name_match_groundings.py
    --input scripts/migrate_node_type_consistency.py --input scripts/migrate_pathway_vs_process.py
    --input scripts/migrate_process_quality_consistency.py --input scripts/migrate_protein_vs_activity.py
    --input scripts/migrate_remaining_microbe_domain_edges.py --input scripts/migrate_uniprot_instance_groundings.py
    --input scripts/normalize_homeoviscous_nodes.py --input scripts/record_review.py
    --input scripts/repair_pr664_adversarial_review.py --input scripts/review_mesophilic_graph_183.py
    --input scripts/review_obligately_piezophilic_graph_183.py --input scripts/review_temperature_delta_high_graph_183.py
    --input scripts/review_temperature_delta_very_low_graph_183.py --input scripts/review_temperature_optimum_high_graph_183.py
    --input scripts/review_temperature_optimum_very_low_graph_183.py --input scripts/review_temperature_range_mid3_graph_183.py
    --input scripts/review_temperature_range_mid4_graph_183.py --input scripts/review_temperature_range_very_low_graph_183.py
    --input scripts/seed_from_metpo.py --input scripts/verify_metpo_proposal.py --input
    src/traitmech/schema/mech_shared.yaml --input src/traitmech/schema/traitmech.yaml
    --input src/traitmech/validation/write_validated.py
  exit_code: 0
  expected_exit_code: 0
  summary: One current target, 98 captured inputs, exact current base and successful
    native inspect.
  evidence_ids:
  - capture
- check_id: uniprot-applicability
  name: Protein-instance metadata applicability
  status: not_applicable
  required: false
  target_ids:
  - METPO:1000444
  summary: No protein nodes or instances in this quantitative NONMECHANISTIC graph;
    no accession or token instance is required.
  evidence_ids:
  - record
  - policy
  - expression
- check_id: expression-adapter-availability
  name: Structured source-organism expression query availability
  status: unavailable
  required: false
  target_ids:
  - METPO:1000444
  summary: Current bounded discovery found the maintained adapter unavailable. Retained
    species catalog and selected primary fallback establish no exact strain or module
    membership result.
  evidence_ids:
  - expression
  - expression-discovery
  - cold-primary
evidence:
- evidence_id: fresh-common-completion
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/new-base-diagnostic-independent-review-agent/fresh-products-completion.json
  locator: Fresh products completion plus prior diagnostic evidence; original execution
    intervals retained
  accessed_at: '2026-10-21T23:30:28.240498Z'
  support: context_only
  summary: Actual B14 checks and current input guards; setup cross-batch comparison
    remains false.
  snapshot_sha256: 2898fb8bd1af98aeea3a60a152fac664f547bc081632ba69aeeefe93678b6a84
- evidence_id: check-new-base-qc
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/new-base-qc.log
  locator: Executed 2026-10-21T23:25:15.125723+00:00 through 2026-10-21T23:26:53.864156+00:00;
    metadata new-base-qc.json
  accessed_at: '2026-10-21T23:26:53.864156Z'
  support: context_only
  summary: 'Actual just qc passed: strict validation of 1130 records with 0 errors;
    graph audit: 74 baselined, 0 new and 0 blocking findings; 135 connected graphs
    and 1588 wired nodes; protein coverage: 729 graphs (134 pass, 594 NONMECHANISTIC,
    0 gaps, 1 protected); snippet audit: 2419 baselined, 0 new and 0 blocking findings;
    19 PathwayMech links. These are corpus diagnostics, not scientific validation
    of this target.'
  snapshot_sha256: 586016aa869497e51bc3e5bb431e4e7658cf5b489dc0577b4475cf9cd22c7947
- evidence_id: check-new-base-history
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/new-base-history.log
  locator: Executed 2026-10-21T23:25:15.125609+00:00 through 2026-10-21T23:25:19.527774+00:00;
    metadata new-base-history.json
  accessed_at: '2026-10-21T23:25:19.527774Z'
  support: context_only
  summary: 1278 HistoryRecord YAMLs validated, 0 invalid; current history snapshot
    contains 1279 files. Integrity does not establish scientific correctness or human
    acceptance.
  snapshot_sha256: 82546ec27fb7d9543d08183e9d0086bd9ca32bbd45ecb2d87ef3f5b990af81c3
- evidence_id: check-new-base-products
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/new-base-products.log
  locator: Executed 2026-10-21T23:29:02.243310+00:00 through 2026-10-21T23:29:27.250859+00:00;
    metadata new-base-products.json
  accessed_at: '2026-10-21T23:29:27.250859Z'
  support: context_only
  summary: 361 canonical matches, 2 exact-synonym matches, 1 exception and 123 SKIPPED_NO_ADAPTER
    pairs. Configured scope is the two grounding mappings, not every target identifier
    or scientific claim.
  snapshot_sha256: 060fcb191c9b0fceb7dd8ebf172d1055f794292211401b30fa4e7f4ffa819141
- evidence_id: check-new-base-stage2-tests
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/new-base-stage2-tests.log
  locator: Executed 2026-10-21T23:25:19.981459+00:00 through 2026-10-21T23:25:21.660071+00:00;
    metadata new-base-stage2-tests.json
  accessed_at: '2026-10-21T23:25:21.660071Z'
  support: context_only
  summary: Five tests passed in the explicitly selected Stage2 test file. This is
    not a full just test run or biological validation.
  snapshot_sha256: 547282404c58d0e8a8e243f434252a5fc215fc1abb8c974b39e7ccdfe759398d
- evidence_id: historical-validate-products
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log
  locator: Historical original execution 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z
  accessed_at: '2026-10-19T07:34:01Z'
  support: context_only
  summary: Historical products exit 2; preserved provenance only, superseded for B14
    by its actual fresh products run.
  snapshot_sha256: 697efcbe603c9a5e27f9726e688d1b9d9f621fa548f585d9005b5157d81dadae
- evidence_id: historical-validate-products-retry-local
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log
  locator: Historical original execution 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z
  accessed_at: '2026-10-19T07:35:24Z'
  support: context_only
  summary: Historical products exit 2; preserved provenance only, superseded for B14
    by its actual fresh products run.
  snapshot_sha256: b636ab6978cf8b8d4cc2cc4033f1cdca399cca46dc615a26073cfe680d44ebb5
- evidence_id: historical-validate-products-retry-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log
  locator: Historical original execution 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z
  accessed_at: '2026-10-19T07:36:03Z'
  support: context_only
  summary: Historical products exit 0; preserved provenance only, superseded for B14
    by its actual fresh products run.
  snapshot_sha256: 67e91252adce1d441ad6b37d6904f0cbcea703575aec8011e65e94822fa810ea
- evidence_id: check-temperature-optimum-mid2-validate
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-validate.log
  locator: Executed 2026-10-22T01:23:37.222495+00:00 through 2026-10-22T01:23:38.051614+00:00;
    metadata temperature-optimum-mid2-validate.json
  accessed_at: '2026-10-22T01:23:38.051614Z'
  support: context_only
  summary: Native record validation passed; scientific interpretation is assessed
    separately.
  snapshot_sha256: 6cd9054ae30497e467410c4056cceb9aae6e9d275605a10030f7cbfde501b358
- evidence_id: check-temperature-optimum-mid2-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-strict.log
  locator: Executed 2026-10-22T01:23:37.222463+00:00 through 2026-10-22T01:23:38.707395+00:00;
    metadata temperature-optimum-mid2-strict.json
  accessed_at: '2026-10-22T01:23:38.707395Z'
  support: context_only
  summary: The actual validate-strict command passed.
  snapshot_sha256: a81af15c83622ca0e3934b50f6620078e3832906a906a2efa9aaf50db8c7dba3
- evidence_id: check-temperature-optimum-mid2-snippets-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-snippets-network.log
  locator: Executed 2026-10-22T01:23:47.479566+00:00 through 2026-10-22T01:23:50.948948+00:00;
    metadata temperature-optimum-mid2-snippets-network.json
  accessed_at: '2026-10-22T01:23:50.948948Z'
  support: context_only
  summary: All four supplied snippets were VERIFIED by the native abstract check and
    independently literal in the source audit. Literal occurrence does not establish
    adjacent numerical or causal claims.
  snapshot_sha256: d8a9be2c0750f2a2b3b81cbb28905b67d5fb7928088783475cd041b2114580a1
- evidence_id: capture
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2.inspect.json
  locator: Actual successful native inspect with 98 captured inputs
  accessed_at: '2026-10-22T01:23:18.769863Z'
  support: context_only
  summary: All current source hashes and the exact target are bound before serialization.
  snapshot_sha256: 888b010fc4ff7432879abb8bde1e5f2a24ea620315c7a93921c19ad098460451
- evidence_id: record
  kind: record_content
  reference: data/traits/environment/temperature_optimum_mid2.yaml
  locator: Whole current record
  accessed_at: '2026-10-22T01:23:18.769863Z'
  support: supports
  summary: Nine nodes, eight edges, twelve embedded events, one canonical example
    and no protein classes or instances.
  snapshot_sha256: f97f6bddb24d09ee6fb58c83b569a84f10da84a59cb983b1c917d5ea68242245
- evidence_id: local-init
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/batch014-local-initialization-receipt.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T01:07:39.713898Z'
  support: context_only
  summary: Actual local initialization and second queue target; publication remains
    separate.
  snapshot_sha256: 3dade2205affd0bd7eea4b7d5018e8c97080db55bba3620e89cf4a4da4123fa3
- evidence_id: policy
  kind: authority
  reference: docs/GROUNDING_POLICY.md
  locator: Captured maintained authority
  accessed_at: '2026-10-22T01:25:49.968694Z'
  support: supports
  summary: Protein family/function grounding and optional protein instances.
  snapshot_sha256: 891678c983c2283a47c81c47950b35753981e9339d105f3bbdda92a1f5ab7f42
- evidence_id: playbook
  kind: authority
  reference: docs/CURATION_PLAYBOOK.md
  locator: Captured maintained authority
  accessed_at: '2026-10-22T01:25:49.968694Z'
  support: supports
  summary: Literal source scope and attributable acceptance.
  snapshot_sha256: 735e9b810471da9f7d8364e35ffe1e741edb3421480dac01727db6ea5aa65da9
- evidence_id: schema
  kind: authority
  reference: src/traitmech/schema/traitmech.yaml
  locator: Captured maintained authority
  accessed_at: '2026-10-22T01:25:49.968694Z'
  support: supports
  summary: Current facets and NONMECHANISTIC scope.
  snapshot_sha256: 46c47fc627b80ccbba1e8ab3fb6f2aee93bc2aef7aaf72fe9aadc3257f2c02dd
- evidence_id: predicate-mapping
  kind: authority
  reference: mappings/predicate_grounding.tsv
  locator: Captured maintained authority
  accessed_at: '2026-10-22T01:25:49.968694Z'
  support: supports
  summary: Wildcard increases mapping can populate empty IDs; current populated assertions
    are skipped.
  snapshot_sha256: 8e28c19e93aca3dc164a3befbe2612b289241de457c59f499e65936c03b7ce52
- evidence_id: node-mapping
  kind: authority
  reference: mappings/node_grounding.tsv
  locator: Captured maintained authority
  accessed_at: '2026-10-22T01:25:49.968694Z'
  support: supports
  summary: Current label/type keys and qualified mappings.
  snapshot_sha256: d7de9b3ab04960c4775a5bc295a945bd1a72d81467830459f4793e654f82b3d0
- evidence_id: identity
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-ground-agent/identity-assessment.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T01:25:49.894169Z'
  support: context_only
  summary: Active exact bin, direct parent and qualified historical aliases.
  snapshot_sha256: c8e06c58af4ed86a0678a15bfb8652437fd2ca87bd5f27ea4c9f1f5540f1f459
- evidence_id: nodes-edges
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-ground-agent/node-edge-grounding-ledger.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T01:25:49.956768Z'
  support: context_only
  summary: All nine node and eight edge judgments with positive controls.
  snapshot_sha256: 11b909fff62ecef0eae6b92944e41c6b7f1286cf219cb56256705722fae1e470
- evidence_id: owners
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-ground-agent/owner-provenance-assessment.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T01:25:49.966404Z'
  support: context_only
  summary: Populated-ID skip guards and exact canonical backfill distinguished from
    discovery-only leads.
  snapshot_sha256: 1c579aa2f6ab4561091d3bdfd573cec9c0bfe394490c2d16136b87790debacb4
- evidence_id: owner-primary
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-ground-agent/owner-primary-reading.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T01:25:49.895964Z'
  support: context_only
  summary: Actual maintained writer and migration decision windows.
  snapshot_sha256: 18dd0dbda9d944ce8c7ddf4865978737f3cd64276c9c05eeda4f7f4be1e4d339
- evidence_id: human-search
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-ground-agent/search-and-provenance.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T01:23:50.788053Z'
  support: context_only
  summary: 176 ignored- and hidden-inclusive matching paths, 67 actual review target
    arrays, zero exact target.
  snapshot_sha256: 528ec787779d276855ab0af4c687bc45dd85161943930d4026dee5b88c8236b9
- evidence_id: histories
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-ground-agent/history-reading-provenance.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T01:25:49.965552Z'
  support: context_only
  summary: One current whole history plus seventeen qualified prior whole readings;
    eighteen current projections.
  snapshot_sha256: 9ff2c5995fb59043a3e5f120401175fe504bafce0c2a5f6315e32959d207d51a
- evidence_id: discovery
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-ground-agent/discovery-disposition.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T01:25:49.933384Z'
  support: context_only
  summary: Two uncaptured history leads and three scripts remain matching-line context.
  snapshot_sha256: b2b85c5e652477ddaf6ce55e586c5287beb8147a051d38c359d11dd29ca71bcd
- evidence_id: alias-discovery
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-ground-agent/alias-writer-discovery-only.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T01:25:49.956349Z'
  support: context_only
  summary: Additional uncaptured alias writer remains discovery-only, not a fully
    read current owner.
  snapshot_sha256: b20e7964252d0b07405d5286660e4cdf372e92aa78ed9415c656b982cfa1e5f6
- evidence_id: expression
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-ground-agent/expression-and-readiness.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T01:25:49.967563Z'
  support: context_only
  summary: Species catalog coverage is separate from exact strain or module support;
    adapter unavailable.
  snapshot_sha256: ec2dd9f8900964d292cbf3bd5df21e3db9259f1f77e05da9af356be71b990b82
- evidence_id: expression-discovery
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-ground-agent/expression-runner-current-discovery.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T01:24:55.612612Z'
  support: context_only
  summary: Fresh bounded PATH/project/install-root discovery, not global absence.
  snapshot_sha256: ca6bfab2465dcde61f42339394fce3a37d28fe945d458cdb932aaee41a6efd81
- evidence_id: local-authority
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-ground-agent/local-authority-reading.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T01:25:49.853336Z'
  support: context_only
  summary: Exact current v3/v8, Biolink causes ancestry, mappings and schema windows.
  snapshot_sha256: e5a1434f56bc4386c14802b8e2fcf4b9c77862d2b7d8b7e29d3a85d0474f6da7
- evidence_id: ground-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-ground-agent/reading-scope-receipt.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T01:25:49.969496Z'
  support: context_only
  summary: Actual current and qualified prior reading scopes.
  snapshot_sha256: e29d5c520f99a4d3a843314e8f24716bba584bcd7004c90604ca0b666f72eb07
- evidence_id: ground-manifest
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-ground-agent/evidence-manifest.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T01:25:49.976630Z'
  support: context_only
  summary: All 31 frozen ground artifacts verified.
  snapshot_sha256: e74c8878a433e54f06d47adb6e252a2f44ebfb3c86debfc4501af580e8ebbc85
- evidence_id: metpo-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/repo/data/raw/metpo.owl
  locator: Selected actual primary statements at the recorded reading time
  accessed_at: '2026-10-22T01:23:50.621331Z'
  support: supports
  summary: Active bin and parent, inclusive 27–30 Cel restriction and raw alias provenance.
  snapshot_sha256: 8b6f8fe0510a698579e532658c8ace05da2550093365df9ca83feb0741778415
- evidence_id: metpo-primary-projection
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-ground-agent/metpo-authority.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T01:23:50.621331Z'
  support: context_only
  summary: Exact primary source hash and selected statement projection.
  snapshot_sha256: dd12b331bd68ee55a88b06a86e513f6797441e6c84eee757f3f9c962c6dc5ab6
- evidence_id: chebi-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/chebi.db
  locator: Selected actual primary statements at the recorded reading time
  accessed_at: '2026-10-22T01:23:46.991209Z'
  support: supports
  summary: Fatty-acid classes encompass the current meaningful material referents.
  snapshot_sha256: 26ad4890cdcf6ee357760d815dfee8f5ba81e0873e62cb379369b04205722b0f
- evidence_id: chebi-primary-projection
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-ground-agent/selected-chebi-primary-reading.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T01:23:46.991209Z'
  support: context_only
  summary: Exact primary source hash and selected statement projection.
  snapshot_sha256: 4a14734e214e614f770ca456e5d63ab4ef47d543dfff8d5c3f4a1e72b47ff0e9
- evidence_id: ro-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/ro.db
  locator: Selected actual primary statements at the recorded reading time
  accessed_at: '2026-10-22T01:23:46.984705Z'
  support: supports
  summary: RO:0002213 inherits process/process roles; RO:0002327 inherits material/process
    roles through enables and the causal ancestry.
  snapshot_sha256: 849e616c29fecd0d4a6c6dee0dc0f6f117ace7167dbfa1e0f043dc84868f83cb
- evidence_id: ro-primary-projection
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-ground-agent/selected-ro-primary-reading.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T01:23:46.984705Z'
  support: context_only
  summary: Exact primary source hash and selected statement projection.
  snapshot_sha256: 93d1a0d40c0fc8e2cdea4641698bc1a409ef2f83c770131bf59cfe1558a17135
- evidence_id: mendoza-metadata
  kind: primary_source
  reference: DOI:10.1146/annurev-micro-091313-103612
  locator: Indexed identity/status and opening generic abstract sentence
  accessed_at: '2026-10-21T10:00:02.042457Z'
  support: supports
  summary: Generic unsaturation and sensing context; exact-bin sufficiency remains
    unknown.
  snapshot_sha256: 801da630644a181211f991a6f21c49b178e42a65f615c4eebd8196bc29244588
- evidence_id: mendoza-publisher
  kind: primary_source
  reference: DOI:10.1146/annurev-micro-091313-103612
  locator: Retained actual browser abstract export, not raw HTML
  accessed_at: '2026-10-21T23:38:35Z'
  support: supports
  summary: Original tool-call interval retained; origin cache-fetch time is unknown.
  snapshot_sha256: b8635235ad5e362d0b33ef4834f84eb25fe7ff6b1bd1321affb2b61cecbc66fc
- evidence_id: cold-metadata
  kind: primary_source
  reference: DOI:10.1007/s42770-023-01057-4
  locator: Indexed identity/status and generic abstract
  accessed_at: '2026-10-21T22:07:08.865512Z'
  support: supports
  summary: Assigned review identity and generic membrane context.
  snapshot_sha256: da5cffab81fe0e039c6fcec8f318b2715f5604eaf8722ea6f63f944178ed447b
- evidence_id: cold-primary
  kind: primary_source
  reference: DOI:10.1007/s42770-023-01057-4
  locator: Zero-based all-HTML paragraph 10 classification clause and paragraph 17
    generic phase/composition passage
  accessed_at: '2026-10-21T22:07:50.938485Z'
  support: supports
  summary: Only stated generic classification and physical context adopted; no universal
    strategy or intervention efficacy.
  snapshot_sha256: bb09a59c07f43ff0af177f89b624c8b5d4841e513ed0d478120954a016342889
- evidence_id: tolner-metadata
  kind: primary_source
  reference: DOI:10.1016/s0300-9629(97)00003-0
  locator: Indexed title/status and opening two high-temperature abstract sentences
  accessed_at: '2026-10-21T09:29:01.331044Z'
  support: supports
  summary: Literal high-temperature context does not establish the adjacent specific
    27–30 degree optimum claim.
  snapshot_sha256: 56f69a7ce2e69822ef753fec5c43716583184e45fc1a2c0cae98aa9bdb841265
- evidence_id: tolner-zero-hit
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016%2Fs0300-9629%2897%2900003-0&format=json&resultType=core
  locator: Original successful HTTP response with zero indexed matches
  accessed_at: '2026-10-21T09:25:49.176885Z'
  support: context_only
  summary: A retrieval diagnostic superseded for identity by the positive PMID and
    Crossref responses; not an absent-paper claim.
  snapshot_sha256: 25e3cf6616503721ec087dd147e11ac038f8834891e32d704a1f67074095c9cc
- evidence_id: tolner-crossref
  kind: primary_source
  reference: DOI:10.1016/s0300-9629(97)00003-0
  locator: Crossref identity metadata
  accessed_at: '2026-10-21T09:27:49.120434Z'
  support: supports
  summary: Positive identity after the original zero-hit DOI query.
  snapshot_sha256: 6f0a5c9b3558992f0f75d1861225410727bededc63928e7a72e1762170d34349
- evidence_id: tolner-author
  kind: primary_source
  reference: DOI:10.1016/s0300-9629(97)00003-0
  locator: Retained author portal abstract, opening high-temperature sentences
  accessed_at: '2026-10-21T09:29:00.791083Z'
  support: supports
  summary: Independent abstract surface; not a full-paper absence judgment.
  snapshot_sha256: 3c475aae5c42532ff36e66a262fe2d6a9c6fc8b64aa6576d93efdc96cada4134
- evidence_id: spectrum-primary
  kind: primary_source
  reference: DOI:10.1128/spectrum.03925-23
  locator: Zero-based body paragraph 1, first sentence and fourth/final sentence
  accessed_at: '2026-10-21T22:07:32.905772Z'
  support: supports
  summary: Generic fluidity definition and cooling/rigidification/thickening/phase
    context only; detailed regulation, assays, antimicrobial and intervention content
    unassessed.
  snapshot_sha256: 4e57f358369566231e022520fc5b5adad7b8c182adfa282d9ed404fa3298a561
- evidence_id: spectrum-metadata
  kind: primary_source
  reference: DOI:10.1128/spectrum.03925-23
  locator: Indexed identity/status
  accessed_at: '2026-10-21T22:07:08.906527Z'
  support: supports
  summary: Assigned B.subtilis study identity; detailed efficacy is outside scope.
  snapshot_sha256: 745eedfa2c11814739b07a4d944725bf565eb4e3f9c6b207ba0d31b967563f98
- evidence_id: canonical-metadata
  kind: primary_source
  reference: DOI:10.1099/ijsem.0.006018
  locator: Indexed title/status and strain/growth/optimum abstract clauses
  accessed_at: '2026-10-22T00:01:21.958472Z'
  support: supports
  summary: N1Y112T reported optimum 28 degrees C, distinct from growth at 20–35 degrees
    C.
  snapshot_sha256: bd5137f9ca1f804e99b65dc384a8568883209f76738962070bac05dac78b7573
- evidence_id: current-browser
  kind: primary_source
  reference: DOI:10.1099/ijsem.0.006018
  locator: Actual root browser export copied by source auditor; canonical publisher
    abstract lines 48 and 51, Mendoza line 100
  accessed_at: '2026-10-22T01:24:13Z'
  support: partial
  summary: Canonical optimum support and generic unsaturation direction are positive.
    This is not raw HTML; recorded_at is export time only, with first-call bounds
    and original cache-fetch times unknown.
  snapshot_sha256: 17824ac1f7423f70474f992c46c71da08359a69849a4e125cbe97df88b02d7ca
- evidence_id: taxonomy
  kind: authority
  reference: NCBITaxon:2781979
  locator: Whole successful retained official retry response; original acquisition
    time
  accessed_at: '2026-10-22T00:01:45.678625Z'
  support: supports
  summary: Pontibacterium sinense and N1Y112 type aliases are positive independently
    of phenotype support.
  snapshot_sha256: 9ce6edf003761e8b4b7ce3e178a366b6f25e353090e03b121a9e4c53e2609b6d
- evidence_id: taxonomy-prior-failure
  kind: validation
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=2781979&retmode=xml
  locator: Original DNS-failure bytes; not official taxonomy content
  accessed_at: '2026-10-22T00:01:32.096470Z'
  support: context_only
  summary: Historical retrieval failure followed by successful official retry; not
    a current native validation failure.
  snapshot_sha256: 35281279d8e2164cee8666d6f8aad891326911e887ab1b2ab778c8ac6d09dc6c
- evidence_id: taxonomy-copy
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-ground-agent/taxonomy-reuse.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T01:24:18.928534Z'
  support: context_only
  summary: Original failed/successful requests and current exact copy times are separate.
  snapshot_sha256: 67f73c9b22c8a0df195e45f922163588e410601f7f2cc0c8f8565ead21d320ca
- evidence_id: taxonomy-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-ground-agent/taxonomy-identity.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T01:25:49.893914Z'
  support: context_only
  summary: Current official identity reading; no phenotype inference from taxonomy.
  snapshot_sha256: 6dae1b380b21696d3d44999940bb4a20c0ae85c3f61ae6ed5057ac979f06983f
- evidence_id: sources
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-source-agent/source-assessment.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T01:26:15.820418Z'
  support: context_only
  summary: Five works with overall UNKNOWN source scope and two bounded source-note
    findings.
  snapshot_sha256: 972ce9090ffe00ba5aa87a01b21e0ef63c31096f134c9901636d12aa26b455e1
- evidence_id: source-identities
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-source-agent/source-identities-status.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T01:26:15.820418Z'
  support: context_only
  summary: All assigned identities and bounded metadata notice fields.
  snapshot_sha256: 5dce1fa458ef4ae512867eea61b1988d077059047e6966e893f125d4ee8735da
- evidence_id: placements
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-source-agent/source-placement-ledger.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T01:26:15.820418Z'
  support: context_only
  summary: All eleven external placements and ten grounding fields accounted.
  snapshot_sha256: 5e8792a70b84a2c048ca268a57129f5579365aedfece9626c284e6e822749930
- evidence_id: snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-source-agent/snippet-ledger.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T01:26:15.820418Z'
  support: context_only
  summary: All four supplied snippets literal; adjacent inference remains separate.
  snapshot_sha256: d85e8a719661ea7f6c3bedbe084a2b49414a14e531a19a5e4943db03bffc9f24
- evidence_id: notes
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-source-agent/source-note-ledger.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T01:26:15.820418Z'
  support: context_only
  summary: All nine evidence notes plus canonical note assessed within explicit scope.
  snapshot_sha256: ef3231dc5f29f4ef295348b966463421542fccd920297a2ba73d0d5225a17e9f
- evidence_id: source-nodes-edges
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-source-agent/node-edge-source-ledger.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T01:26:15.820418Z'
  support: context_only
  summary: All nine nodes and eight edges with qualified physical/source attribution.
  snapshot_sha256: b0689afbdf3c3fb3a92c85336d748b8819fea4c374a7ee60173ab6181ffdb999
- evidence_id: classification
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-source-agent/classification-assessment.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T01:26:15.820418Z'
  support: context_only
  summary: Mesophilic exactness remains unknown; a growth interval is not an outside-bin
    optimum.
  snapshot_sha256: 69b6cd2069ba934d9f027fc146a50c43a1824ac308f5a621c37212766fdf4a6f
- evidence_id: canonical
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-source-agent/canonical-assessment.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T01:26:15.820418Z'
  support: context_only
  summary: Reported 28 degree optimum supports the bin, separately from the 20–35
    growth interval.
  snapshot_sha256: 39d73de1adbdefcddacef99e201f13dd1fa60730afb1a854cf355d3928294cdc
- evidence_id: source-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-source-agent/primary-reading-scope.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T01:26:15.820418Z'
  support: context_only
  summary: Selected primary passages and explicit excluded detailed mechanism scope.
  snapshot_sha256: 9dd4163d49d4c061dbe1904a09d64d15b9e97ae1f311bd14fe40272f3b7cf2ba
- evidence_id: source-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-source-agent/source-access-limits.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T01:26:15.820418Z'
  support: context_only
  summary: Body access limits and prior browser observations are not substituted as
    current body evidence.
  snapshot_sha256: 36a0c34368cc3690a63ed8c80184203ee28ef3927b2ff8b1f5713c5755ca1530
- evidence_id: source-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-source-agent/source-reuse-receipt.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T01:26:15.820243Z'
  support: context_only
  summary: Original acquisition, current copy and current interpretation clocks are
    separate.
  snapshot_sha256: a09510a2b768bb64cd288eba1b5501ca3e679e2d2b21c9c14c1a952574ea0cbb
- evidence_id: source-native
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-source-agent/native-check-context.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T01:26:15.820418Z'
  support: context_only
  summary: Four native VERIFIED fields and four manual literal matches.
  snapshot_sha256: d395a64c800322a405d1e01d62324199f597856b478c80d271b26a91647a97f0
- evidence_id: source-manifest
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-source-agent/evidence-manifest.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T01:26:15.835237Z'
  support: context_only
  summary: All 29 frozen source artifacts verified.
  snapshot_sha256: abb12bd9cb731ccaf5b3ebed1e338629e11e8eeff9234a540b6f50fbfee06eaf
- evidence_id: root-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-source-root/selected-primary-reading.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T01:27:09.029939Z'
  support: context_only
  summary: Independent bounded primary/owner reading; root and ground current/prior
    whole-history scopes remain separately attributed.
  snapshot_sha256: 0f1a7a65f49f48a5ed742d04d1e48ffadd14ba9af0a0e7c45bc3b6c1b50f8b67
- evidence_id: adjudication
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-mid2-root-adjudication.json
  locator: Final root adjudication
  accessed_at: '2026-10-22T01:27:09.029939Z'
  support: supports
  summary: Exact finding fields, owner qualifications, actions and unresolved source
    scopes control serialization.
  snapshot_sha256: dd815ee01338360e75b253ef7dfbbcd14fb4fb011f57f3550ac62e5ed9ba7435
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: active class, aliases and direct parent'
  outcome: supported
  target_ids:
  - METPO:1000444
  summary: Active METPO:1000444 and parent METPO:1000304 agree with the local quantitative
    bin. Current mesophilic alias inheritance is documentary; legacy spelling provenance
    and exact scientific equivalence remain qualified.
  evidence_ids:
  - identity
  - metpo-primary
  - classification
  - record
- assessment_id: definition
  area: quantity
  topic: 'Native checklist: best-growth temperature and numerical calibration'
  outcome: unknown
  target_ids:
  - METPO:1000444
  summary: The inclusive 27–30 degree interval is explicit in local identity. Generic
    membrane adaptation does not establish exact cutoff calibration or sufficient
    whole-organism optima; a 20–45 growth interval does not prove an optimum outside
    this bin.
  evidence_ids:
  - sources
  - placements
  - classification
  - metpo-primary
- assessment_id: canonical
  area: quantity
  topic: 'Native checklist: exact taxon and reported optimum'
  outcome: supported
  target_ids:
  - METPO:1000444
  summary: Official Pontibacterium sinense identity and N1Y112 aliases agree. The
    assigned abstract reports optimum 28 degrees C and growth at 20–35 degrees C;
    these are distinct strain-specific observations, not an exhaustive response curve.
  evidence_ids:
  - canonical
  - canonical-metadata
  - current-browser
  - taxonomy
  - taxonomy-reading
- assessment_id: source-support
  area: evidence
  topic: 'Native checklist: five works and all placements'
  outcome: unknown
  target_ids:
  - METPO:1000444
  summary: All five identities are verified. Exact-bin calibration and baseline causal
    sufficiency remain unresolved. The Tolner note needs high-temperature scope qualification,
    and the written saturated/unsaturated ratio contradicts its stated direction toward
    UFAs. These are bounded note concerns; no underlying generic physical relation
    is refuted. Detailed pathogen survival, fitness, ROS-defense, AMR and intervention
    mechanisms remain UNASSESSED_SCOPE.
  evidence_ids:
  - sources
  - source-identities
  - placements
  - notes
  - source-reading
  - source-access
  - tolner-metadata
  - tolner-author
  - cold-primary
- assessment_id: quotations
  area: evidence
  topic: 'Native checklist: four snippets and evidence-note scope'
  outcome: supported
  target_ids:
  - METPO:1000444
  summary: All four snippets are literal and native VERIFIED. Literal occurrence is
    distinct from adjacent numerical or causal attribution; the high-temperature note
    remains a separate minor concern.
  evidence_ids:
  - snippets
  - source-native
  - notes
  - mendoza-metadata
  - tolner-metadata
- assessment_id: nodes
  area: representation
  topic: 'Native checklist: all nine current referents'
  outcome: concern
  target_ids:
  - METPO:1000444
  summary: Node 8 describes an organism category but is typed as molecular/bioenergetic
    STATE, a bounded facet concern. Material fatty acids and fluidity quality remain
    meaningful. Temperature decrease denotes an event. Baseline adaptation versus
    its repertoire result and rigidification versus rigidity quality remain qualified,
    without forced extra retyping.
  evidence_ids:
  - nodes-edges
  - source-nodes-edges
  - chebi-primary
  - local-authority
  - schema
  details: "{\n  \"grounding\": [\n    {\n      \"index\": 0,\n      \"node_id\":\
    \ \"temperature_optimum_mid2_trait\",\n      \"label\": \"temperature optimum\
    \ mid2\",\n      \"node_type\": \"TRAIT\",\n      \"grounding\": \"METPO:1000444\"\
    ,\n      \"outcome\": \"supported\",\n      \"assessment\": \"Active optimum bin\
    \ and direct parent; scientific synonym equivalence remains independent.\"\n \
    \   },\n    {\n      \"index\": 1,\n      \"node_id\": \"temperature_optimum\"\
    ,\n      \"label\": \"temperature optimum\",\n      \"node_type\": \"TRAIT\",\n\
    \      \"grounding\": \"METPO:1000304\",\n      \"outcome\": \"supported\",\n\
    \      \"assessment\": \"Active temperature-optimum measurement phenotype parent.\"\
    \n    },\n    {\n      \"index\": 2,\n      \"node_id\": \"mesophilic_environment\"\
    ,\n      \"label\": \"mesophilic environment\",\n      \"node_type\": \"ENVIRONMENTAL_FACTOR\"\
    ,\n      \"grounding\": null,\n      \"outcome\": \"supported\",\n      \"assessment\"\
    : \"Ambient27–30°C habitat condition, not automatically a process. Its lexical\
    \ outgoing edge has no imported process domain.\"\n    },\n    {\n      \"index\"\
    : 3,\n      \"node_id\": \"baseline_mesophile_adaptation\",\n      \"label\":\
    \ \"baseline mesophile adaptation\",\n      \"node_type\": \"BIOLOGICAL_PROCESS\"\
    ,\n      \"grounding\": null,\n      \"outcome\": \"qualified\",\n      \"assessment\"\
    : \"Adaptation process is intended by type and edges, while membrane/enzyme repertoire\
    \ wording describes an adapted result. Preserve this bounded ambiguity; no forced\
    \ separate facet or replacement mechanism.\"\n    },\n    {\n      \"index\":\
    \ 4,\n      \"node_id\": \"temperature_decrease\",\n      \"label\": \"temperature\
    \ decrease\",\n      \"node_type\": \"ENVIRONMENTAL_FACTOR\",\n      \"grounding\"\
    : null,\n      \"outcome\": \"supported\",\n      \"assessment\": \"Explicit drop\
    \ in ambient temperature denotes an event; ENVIRONMENTAL_FACTOR alone does not\
    \ invalidate processual interpretation.\"\n    },\n    {\n      \"index\": 5,\n\
    \      \"node_id\": \"membrane_rigidity\",\n      \"label\": \"membrane rigidification\"\
    ,\n      \"node_type\": \"QUALITY\",\n      \"grounding\": null,\n      \"outcome\"\
    : \"qualified\",\n      \"assessment\": \"Current QUALITY denotes increased bilayer\
    \ order/thickness. Rigidification/phase-transition words also evoke a process;\
    \ maintained exact membrane_rigidity decision supports the quality result. No\
    \ additional forced retype.\"\n    },\n    {\n      \"index\": 6,\n      \"node_id\"\
    : \"unsaturated_fatty_acids\",\n      \"label\": \"unsaturated fatty acids\",\n\
    \      \"node_type\": \"CHEMICAL\",\n      \"grounding\": \"CHEBI:27208\",\n \
    \     \"outcome\": \"supported\",\n      \"assessment\": \"Material unsaturated-fatty-acid\
    \ class; CHEBI27208 double-bond subset is meaningful.\"\n    },\n    {\n     \
    \ \"index\": 7,\n      \"node_id\": \"membrane_fluidity\",\n      \"label\": \"\
    membrane fluidity\",\n      \"node_type\": \"QUALITY\",\n      \"grounding\":\
    \ \"METPO:1007505\",\n      \"outcome\": \"supported\",\n      \"assessment\"\
    : \"Explicit membrane-fluidity physical quality, consistent with local v3.\"\n\
    \    },\n    {\n      \"index\": 8,\n      \"node_id\": \"mesophile_category\"\
    ,\n      \"label\": \"mesophile category\",\n      \"node_type\": \"STATE\",\n\
    \      \"grounding\": null,\n      \"outcome\": \"concern\",\n      \"assessment\"\
    : \"Label and description denote an organism category, while schema STATE means\
    \ a molecular/bioenergetic state of a cell. Bounded facet precision minor: intended\
    \ category remains legible; no forced replacement enum, CURIE or biological subclass\
    \ inference.\"\n    }\n  ],\n  \"source\": [\n    {\n      \"index\": 0,\n   \
    \   \"node_id\": \"temperature_optimum_mid2_trait\",\n      \"field_path\": \"\
    causal_graphs[0].nodes[0]\",\n      \"label\": \"temperature optimum mid2\",\n\
    \      \"description\": \"Temperature optimum approximately 27–30 °C.\",\n   \
    \   \"status\": \"UNKNOWN\",\n      \"assessment\": \"Local numerical bin definition;\
    \ exact source cutoff calibration remains unknown.\",\n      \"primary_locator\"\
    : \"Indexed abstract opening sentence; current publisher abstract line100 corroborates\
    \ generic direction.\"\n    },\n    {\n      \"index\": 1,\n      \"node_id\"\
    : \"temperature_optimum\",\n      \"field_path\": \"causal_graphs[0].nodes[1]\"\
    ,\n      \"label\": \"temperature optimum\",\n      \"description\": \"Ambient\
    \ temperature supporting maximal growth.\",\n      \"status\": \"SUPPORTED_DEFINITIONAL\"\
    ,\n      \"assessment\": \"Parent maximum-growth-temperature meaning is distinct\
    \ from growth interval; no causal sufficiency inferred.\",\n      \"primary_locator\"\
    : \"Indexed abstract strain/growth/optimum/type clauses; current publisher export\
    \ lines48 and51.\"\n    },\n    {\n      \"index\": 2,\n      \"node_id\": \"\
    mesophilic_environment\",\n      \"field_path\": \"causal_graphs[0].nodes[2]\"\
    ,\n      \"label\": \"mesophilic environment\",\n      \"description\": \"Habitat\
    \ ambient temperature in the 27–30 °C range.\",\n      \"status\": \"UNKNOWN\"\
    ,\n      \"assessment\": \"Record stipulates habitat27–30; no specific habitat\
    \ optimum universality established.\",\n      \"primary_locator\": \"Indexed abstract\
    \ opening sentence; current publisher abstract line100 corroborates generic direction.\"\
    \n    },\n    {\n      \"index\": 3,\n      \"node_id\": \"baseline_mesophile_adaptation\"\
    ,\n      \"field_path\": \"causal_graphs[0].nodes[3]\",\n      \"label\": \"baseline\
    \ mesophile adaptation\",\n      \"description\": \"Standard mesophile membrane\
    \ and enzyme repertoire matching a moderate ambient-temperature setpoint.\",\n\
    \      \"status\": \"PARTIAL\",\n      \"assessment\": \"Generic membrane adaptation\
    \ is supported; combined standard enzyme/membrane repertoire and a specific setpoint\
    \ remain broader than inspected source.\",\n      \"primary_locator\": \"Indexed\
    \ abstract opening sentence; current publisher abstract line100 corroborates generic\
    \ direction.\"\n    },\n    {\n      \"index\": 4,\n      \"node_id\": \"temperature_decrease\"\
    ,\n      \"field_path\": \"causal_graphs[0].nodes[4]\",\n      \"label\": \"temperature\
    \ decrease\",\n      \"description\": \"A drop in ambient temperature below the\
    \ growth setpoint.\",\n      \"status\": \"SUPPORTED_GENERIC\",\n      \"assessment\"\
    : \"Environmental temperature drop is the physical trigger in the selected introduction.\"\
    ,\n      \"primary_locator\": \"spectrum.xml zero-based .//body//p[1], first sentence\
    \ fluidity definition and fourth/final sentence generic cooling/rigidification/thickening/gel.\"\
    \n    },\n    {\n      \"index\": 5,\n      \"node_id\": \"membrane_rigidity\"\
    ,\n      \"field_path\": \"causal_graphs[0].nodes[5]\",\n      \"label\": \"membrane\
    \ rigidification\",\n      \"description\": \"Increased bilayer order/thickness\
    \ and liquid-crystalline to gel transition of the cytoplasmic membrane.\",\n \
    \     \"status\": \"SUPPORTED_GENERIC\",\n      \"assessment\": \"Rigidification/thickening/gel\
    \ transition is explicit generic physical context.\",\n      \"primary_locator\"\
    : \"spectrum.xml zero-based .//body//p[1], first sentence fluidity definition\
    \ and fourth/final sentence generic cooling/rigidification/thickening/gel.\"\n\
    \    },\n    {\n      \"index\": 6,\n      \"node_id\": \"unsaturated_fatty_acids\"\
    ,\n      \"field_path\": \"causal_graphs[0].nodes[6]\",\n      \"label\": \"unsaturated\
    \ fatty acids\",\n      \"description\": \"Membrane fatty acyl chains bearing\
    \ one or more double bonds (CHEBI:27208).\",\n      \"status\": \"SUPPORTED_GENERIC\"\
    ,\n      \"assessment\": \"Unsaturation means double bonds in fatty-acyl chains;\
    \ selected generic composition context supports the referent. CHEBI identity independently\
    \ audited.\",\n      \"primary_locator\": \"cold-pmc.html zero-based all-HTML\
    \ paragraphs: p10 classification clause, p17 generic phase/composition passage.\"\
    \n    },\n    {\n      \"index\": 7,\n      \"node_id\": \"membrane_fluidity\"\
    ,\n      \"field_path\": \"causal_graphs[0].nodes[7]\",\n      \"label\": \"membrane\
    \ fluidity\",\n      \"description\": \"Physical fluidity/disorder state of the\
    \ cytoplasmic membrane.\",\n      \"status\": \"SUPPORTED_GENERIC\",\n      \"\
    assessment\": \"Membrane fluidity is a physical freedom-of-motion state; selected\
    \ Spectrum first sentence supports this generic referent.\",\n      \"primary_locator\"\
    : \"spectrum.xml zero-based .//body//p[1], first sentence fluidity definition\
    \ and fourth/final sentence generic cooling/rigidification/thickening/gel.\"\n\
    \    },\n    {\n      \"index\": 8,\n      \"node_id\": \"mesophile_category\"\
    ,\n      \"field_path\": \"causal_graphs[0].nodes[8]\",\n      \"label\": \"mesophile\
    \ category\",\n      \"description\": \"Organisms growing between approximately\
    \ 20 and 45 degrees C ambient temperature.\",\n      \"status\": \"PARTIAL\",\n\
    \      \"assessment\": \"Ramón classification clause reports mesophile growth\
    \ around20–45. This is not a complete optimum criterion; organism-category/state\
    \ representation is grounding scope.\",\n      \"primary_locator\": \"cold-pmc.html\
    \ zero-based all-HTML paragraphs: p10 classification clause, p17 generic phase/composition\
    \ passage.\"\n    }\n  ]\n}"
- assessment_id: relations
  area: consistency
  topic: 'Native checklist: all eight current relations'
  outcome: concern
  target_ids:
  - METPO:1000444
  summary: RO role concerns are limited to edges 4, 5 and 6. Edge 4 has material/quality
    endpoints under process/process RO2213; edge 5 has a valid process subject but
    material object; edge 6 has a quality subject where RO2327 requires material,
    with a valid process object. Biolink causes has broad endpoints; the temperature-drop
    event is a positive control. Local confers, grounded hierarchy and two lexical
    predicates receive no invented constraints.
  evidence_ids:
  - nodes-edges
  - source-nodes-edges
  - ro-primary
  - local-authority
  - adjudication
  details: "{\n  \"grounding\": [\n    {\n      \"index\": 0,\n      \"subject\":\
    \ \"mesophilic_environment\",\n      \"predicate\": \"engages\",\n      \"predicate_id\"\
    : null,\n      \"object\": \"baseline_mesophile_adaptation\",\n      \"outcome\"\
    : \"unknown\",\n      \"assessment\": \"Lexical engages has no imported role constraints;\
    \ exact optimum causal calibration remains source-scoped.\"\n    },\n    {\n \
    \     \"index\": 1,\n      \"subject\": \"baseline_mesophile_adaptation\",\n \
    \     \"predicate\": \"confers\",\n      \"predicate_id\": \"METPO:2007700\",\n\
    \      \"object\": \"temperature_optimum_mid2_trait\",\n      \"outcome\": \"\
    supported\",\n      \"assessment\": \"Local confers broad causal-node endpoints\
    \ and trait-object prose fit the declared adaptation/trait roles; exact27–30°C\
    \ sufficiency remains unverified independently.\"\n    },\n    {\n      \"index\"\
    : 2,\n      \"subject\": \"temperature_optimum_mid2_trait\",\n      \"predicate\"\
    : \"is a\",\n      \"predicate_id\": \"rdfs:subClassOf\",\n      \"object\": \"\
    temperature_optimum\",\n      \"outcome\": \"supported\",\n      \"assessment\"\
    : \"Current active bin has the declared active temperature-optimum parent. Its\
    \ attached evidence-note attribution is a separate source question.\"\n    },\n\
    \    {\n      \"index\": 3,\n      \"subject\": \"temperature_decrease\",\n  \
    \    \"predicate\": \"causes\",\n      \"predicate_id\": \"biolink:causes\",\n\
    \      \"object\": \"membrane_rigidity\",\n      \"outcome\": \"supported\",\n\
    \      \"assessment\": \"Actual Biolink causes ancestry has NamedThing endpoints,\
    \ not inherited RO2326 material/process restrictions. Explicit temperature-drop\
    \ event and rigidity quality do not establish a formal endpoint failure; transition/result\
    \ wording stays qualified.\"\n    },\n    {\n      \"index\": 4,\n      \"subject\"\
    : \"unsaturated_fatty_acids\",\n      \"predicate\": \"increases\",\n      \"\
    predicate_id\": \"RO:0002213\",\n      \"object\": \"membrane_fluidity\",\n  \
    \    \"outcome\": \"concern\",\n      \"assessment\": \"RO2213 inherits process/process\
    \ roles; material fatty acids and fluidity quality both conflict with those roles.\"\
    \n    },\n    {\n      \"index\": 5,\n      \"subject\": \"baseline_mesophile_adaptation\"\
    ,\n      \"predicate\": \"increases\",\n      \"predicate_id\": \"RO:0002213\"\
    ,\n      \"object\": \"unsaturated_fatty_acids\",\n      \"outcome\": \"concern\"\
    ,\n      \"assessment\": \"RO2213 requires a process object. The adaptation process\
    \ subject can fit, but the explicit fatty-acid material object does not.\"\n \
    \   },\n    {\n      \"index\": 6,\n      \"subject\": \"membrane_fluidity\",\n\
    \      \"predicate\": \"enables\",\n      \"predicate_id\": \"RO:0002327\",\n\
    \      \"object\": \"baseline_mesophile_adaptation\",\n      \"outcome\": \"concern\"\
    ,\n      \"assessment\": \"RO2327 inherits material-domain/process-range through2215/2216/2500/2595.\
    \ Current membrane-fluidity quality is not a material executor. Adaptation process\
    \ object is a positive range control, subject to its wording qualification.\"\n\
    \    },\n    {\n      \"index\": 7,\n      \"subject\": \"temperature_optimum_mid2_trait\"\
    ,\n      \"predicate\": \"subclass of\",\n      \"predicate_id\": null,\n    \
    \  \"object\": \"mesophile_category\",\n      \"outcome\": \"qualified\",\n  \
    \    \"assessment\": \"Lexical subclass of is not a grounded rdfs assertion. Current\
    \ organism-category object has a separate bounded STATE facet issue; a reported\
    \ growth interval alone does not independently establish an optimum equivalence\
    \ or universal subset. Source scope remains qualified without another imported-role\
    \ finding.\"\n    }\n  ],\n  \"source\": [\n    {\n      \"index\": 0,\n     \
    \ \"field_path\": \"causal_graphs[0].edges[0]\",\n      \"subject\": \"mesophilic_environment\"\
    ,\n      \"predicate\": \"engages\",\n      \"object\": \"baseline_mesophile_adaptation\"\
    ,\n      \"description\": \"Mesophilic environments engage baseline mesophile\
    \ adaptation.\",\n      \"status\": \"PARTIAL\",\n      \"assessment\": \"Generic\
    \ temperature-linked lipid adaptation is supported; the specific27–30 environment\
    \ and baseline outcome are not established by the inspected abstract.\",\n   \
    \   \"primary_locator\": \"Indexed abstract opening sentence; current publisher\
    \ abstract line100 corroborates generic direction.\",\n      \"formal_role_scope\"\
    : \"Independent grounding audit; no source classification substitutes for endpoint\
    \ typing.\"\n    },\n    {\n      \"index\": 1,\n      \"field_path\": \"causal_graphs[0].edges[1]\"\
    ,\n      \"subject\": \"baseline_mesophile_adaptation\",\n      \"predicate\"\
    : \"confers\",\n      \"object\": \"temperature_optimum_mid2_trait\",\n      \"\
    description\": \"Baseline mesophile adaptation yields a 27–30 °C optimum.\",\n\
    \      \"status\": \"UNKNOWN\",\n      \"assessment\": \"Generic membrane adaptation\
    \ does not establish a sufficient whole-organism27–30 optimum. Full article uninspected;\
    \ no false-paper-absence claim.\",\n      \"primary_locator\": \"Indexed abstract\
    \ opening sentence; current publisher abstract line100 corroborates generic direction.\"\
    ,\n      \"formal_role_scope\": \"Independent grounding audit; no source classification\
    \ substitutes for endpoint typing.\"\n    },\n    {\n      \"index\": 2,\n   \
    \   \"field_path\": \"causal_graphs[0].edges[2]\",\n      \"subject\": \"temperature_optimum_mid2_trait\"\
    ,\n      \"predicate\": \"is a\",\n      \"object\": \"temperature_optimum\",\n\
    \      \"description\": \"Temperature optimum mid2 is a quantitative bin of the\
    \ temperature-optimum phenotype.\",\n      \"status\": \"CONCERN\",\n      \"\
    assessment\": \"Literal high-temperature thermophile passage does not supply the\
    \ adjacent specific27–30 optimum attribution. Local subclass hierarchy is assessed\
    \ independently.\",\n      \"primary_locator\": \"Indexed abstract opening two\
    \ sentences and retained author portal: thermophiles/high temperatures.\",\n \
    \     \"formal_role_scope\": \"Independent grounding audit; no source classification\
    \ substitutes for endpoint typing.\"\n    },\n    {\n      \"index\": 3,\n   \
    \   \"field_path\": \"causal_graphs[0].edges[3]\",\n      \"subject\": \"temperature_decrease\"\
    ,\n      \"predicate\": \"causes\",\n      \"object\": \"membrane_rigidity\",\n\
    \      \"description\": \"A temperature drop rigidifies and thickens the cytoplasmic\
    \ membrane.\",\n      \"status\": \"SUPPORTED_GENERIC\",\n      \"assessment\"\
    : \"Assigned introduction explicitly states generic cooling causes rigidification,\
    \ thickening and phase change; this does not establish bin-specific physiological\
    \ efficacy.\",\n      \"primary_locator\": \"spectrum.xml zero-based .//body//p[1],\
    \ first sentence fluidity definition and fourth/final sentence generic cooling/rigidification/thickening/gel.\"\
    ,\n      \"formal_role_scope\": \"Independent grounding audit; no source classification\
    \ substitutes for endpoint typing.\"\n    },\n    {\n      \"index\": 4,\n   \
    \   \"field_path\": \"causal_graphs[0].edges[4]\",\n      \"subject\": \"unsaturated_fatty_acids\"\
    ,\n      \"predicate\": \"increases\",\n      \"object\": \"membrane_fluidity\"\
    ,\n      \"description\": \"Higher unsaturated fatty acid content fluidizes and\
    \ thins the bilayer.\",\n      \"status\": \"SUPPORTED_WITH_NOTE_CONCERN\",\n\
    \      \"assessment\": \"Generic UFA enrichment/fluidity direction is positive.\
    \ The note reverses the stated ratio: increasing SFA/UFA cannot mean shifting\
    \ toward UFA. This is a local explanatory-direction defect, independent of imported\
    \ relation roles.\",\n      \"primary_locator\": \"cold-pmc.html zero-based all-HTML\
    \ paragraphs: p10 classification clause, p17 generic phase/composition passage.\"\
    ,\n      \"formal_role_scope\": \"Independent grounding audit; no source classification\
    \ substitutes for endpoint typing.\"\n    },\n    {\n      \"index\": 5,\n   \
    \   \"field_path\": \"causal_graphs[0].edges[5]\",\n      \"subject\": \"baseline_mesophile_adaptation\"\
    ,\n      \"predicate\": \"increases\",\n      \"object\": \"unsaturated_fatty_acids\"\
    ,\n      \"description\": \"Homeoviscous mesophile adaptation raises unsaturated\
    \ fatty acid content to offset cooling.\",\n      \"status\": \"PARTIAL\",\n \
    \     \"assessment\": \"Generic composition adjustment/increased unsaturation\
    \ during cooling is supported; not a universal mesophile strategy or exact-bin\
    \ efficacy claim. Current process-to-material relation is separately grounded.\"\
    ,\n      \"primary_locator\": \"cold-pmc.html zero-based all-HTML paragraphs:\
    \ p10 classification clause, p17 generic phase/composition passage.\",\n     \
    \ \"formal_role_scope\": \"Independent grounding audit; no source classification\
    \ substitutes for endpoint typing.\"\n    },\n    {\n      \"index\": 6,\n   \
    \   \"field_path\": \"causal_graphs[0].edges[6]\",\n      \"subject\": \"membrane_fluidity\"\
    ,\n      \"predicate\": \"enables\",\n      \"object\": \"baseline_mesophile_adaptation\"\
    ,\n      \"description\": \"Maintained membrane fluidity supports the baseline\
    \ mesophile physiological state.\",\n      \"status\": \"UNASSESSED_SCOPE\",\n\
    \      \"assessment\": \"Generic membrane fluidity is meaningful; detailed sensing/correction\
    \ and efficacy of the specific desaturation system are outside the declared review\
    \ scope. The cited paper is B.subtilis-specific and must not imply universal or27–30-bin\
    \ efficacy.\",\n      \"primary_locator\": \"spectrum.xml zero-based .//body//p[1],\
    \ first sentence fluidity definition and fourth/final sentence generic cooling/rigidification/thickening/gel.\"\
    ,\n      \"formal_role_scope\": \"Independent grounding audit; no source classification\
    \ substitutes for endpoint typing.\"\n    },\n    {\n      \"index\": 7,\n   \
    \   \"field_path\": \"causal_graphs[0].edges[7]\",\n      \"subject\": \"temperature_optimum_mid2_trait\"\
    ,\n      \"predicate\": \"subclass of\",\n      \"object\": \"mesophile_category\"\
    ,\n      \"description\": \"The 27-30 C optimum falls within the mesophile growth\
    \ range.\",\n      \"status\": \"PARTIAL\",\n      \"assessment\": \"The reported\
    \ mesophile20–45 growth-range wording and arithmetic containment are positive.\
    \ Growth interval is distinct from an optimum-based exact synonym or exhaustive\
    \ organism classification; complete identity inference remains UNKNOWN.\",\n \
    \     \"primary_locator\": \"cold-pmc.html zero-based all-HTML paragraphs: p10\
    \ classification clause, p17 generic phase/composition passage.\",\n      \"formal_role_scope\"\
    : \"Independent grounding audit; no source classification substitutes for endpoint\
    \ typing.\"\n    }\n  ]\n}"
- assessment_id: owners
  area: ownership
  topic: 'Native checklist: maintained writers and recurrence'
  outcome: supported
  target_ids:
  - METPO:1000444
  summary: Current populated RO assertions are record-owned; wildcard increases/enables
    mappings can recur only for empty IDs and the shared grounder skips existing IDs.
    Node 8 facet is record-only. Process-quality migration preserves the current rigidity
    rationale but its absent maximal-growth edge guard excludes it from current RO
    repair. Exact canonical backfill has the matching tuple and equality guard; alias
    and sibling discoveries remain qualified context.
  evidence_ids:
  - owners
  - owner-primary
  - predicate-mapping
  - node-mapping
  - discovery
  - alias-discovery
- assessment_id: provenance
  area: provenance
  topic: 'Native checklist: attributable human acceptance'
  outcome: concern
  target_ids:
  - METPO:1000444
  summary: Twelve embedded events comprise eleven AI events and one seed. Ignored-
    and hidden-inclusive search found 176 matching paths and 67 actual target arrays,
    none exact. One current whole and seventeen qualified prior whole history readings
    do not establish attributable human acceptance of current assertions; private
    or remote acceptance remains unknown.
  evidence_ids:
  - human-search
  - histories
  - ground-reading
  - root-reading
  - record
- assessment_id: expression
  area: completeness
  topic: 'Native checklist: catalog coverage and adapter availability'
  outcome: unknown
  target_ids:
  - METPO:1000444
  summary: The retained catalog covers B.subtilis and E.coli source species but no
    exact canonical Pontibacterium entry. No strain or module substitution is made.
    Appropriate generic queries were not executed because bounded current discovery
    found the maintained adapter unavailable; selected primary context is fallback.
  evidence_ids:
  - expression
  - expression-discovery
  - spectrum-primary
- assessment_id: readiness
  area: completeness
  topic: 'Native checklist: graph scope and optional protein instances'
  outcome: supported
  target_ids:
  - METPO:1000444
  summary: Two components, nine nodes and eight edges form a quantitative NONMECHANISTIC
    record. Zero protein nodes or instances do not require fabricated molecular details
    or graph connectors. Detailed excluded biological efficacy remains unassessed.
  evidence_ids:
  - record
  - nodes-edges
  - expression
  - policy
- assessment_id: validation
  area: schema
  topic: 'Native checklist: actual native and fresh B14 diagnostics'
  outcome: supported
  target_ids:
  - METPO:1000444
  summary: Current native capture, focused validation, strict validation and all four
    snippet fields passed. B14 common checks are actual fresh executions at the advanced
    base; historical failures, cache provenance, product skips and the omitted full
    test suite remain explicit. These diagnostics do not certify scientific meaning.
  evidence_ids:
  - capture
  - fresh-common-completion
  - check-temperature-optimum-mid2-validate
  - check-temperature-optimum-mid2-strict
  - check-temperature-optimum-mid2-snippets-network
findings:
- finding_id: imported-process-roles
  issue_key: temperature-optimum-mid2-imported-process-roles
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Imported process roles
  description: 'Three grounded relations conflict with their actual endpoint referents.
    RO:0002213 inherits process domain and range: edge4 has material fatty acids and
    a fluidity quality, while edge5 has a material fatty-acid object despite its compatible
    adaptation-process subject. Edge6 uses RO:0002327 with a fluidity-quality subject
    instead of a material executor; the adaptation-process object fits the inherited
    process range subject to its wording qualification. The material domain follows2327→2215→2216→2500→2595.
    Biolink causes has its own broad NamedThing endpoints, and the explicit temperature
    drop is an event. Two lexical predicates receive no invented imported constraints.'
  target_ids:
  - METPO:1000444
  field_paths:
  - causal_graphs[0].edges[4].predicate_id
  - causal_graphs[0].edges[5].predicate_id
  - causal_graphs[0].edges[6].predicate_id
  evidence_ids:
  - nodes-edges
  - ro-primary
  - chebi-primary
  - owners
  - predicate-mapping
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_optimum_mid2.yaml
    role: Current record assertions
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Conditional recurrence mapping; not an automatic current rewrite
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Shared writer skips populated IDs; no ordinary rerun repair
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: organism-category-state-facet
  issue_key: temperature-optimum-mid2-organism-category-state-facet
  category: representation
  severity: minor
  status: open
  certainty: confirmed
  title: Organism category state facet
  description: The mesophile-category label and description consistently denote a
    category of organisms, while schema STATE denotes a bioenergetic or molecular
    state of a cell. The intended category remains legible, so this is a bounded facet-precision
    concern. It does not establish scientific synonym equivalence or a universal optimum-based
    subclass, and the lexical subclass edge7 is not an imported rdfs assertion.
  target_ids:
  - METPO:1000444
  field_paths:
  - causal_graphs[0].nodes[8].node_type
  evidence_ids:
  - nodes-edges
  - schema
  - owners
  - record
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_optimum_mid2.yaml
    role: Current record assertions
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: high-temperature-source-placement
  issue_key: temperature-optimum-mid2-high-temperature-source-placement
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: High temperature source placement
  description: The literal Tolner passage explicitly concerns thermophiles adapted
    to high temperatures, while its adjacent note attributes specific27–30°C optimum
    support to that passage. Qualify the nearest-evidence attribution. The active
    local subclass hierarchy is independently supported by METPO; no whole-paper absence
    or false hierarchy is asserted.
  target_ids:
  - METPO:1000444
  field_paths:
  - causal_graphs[0].edges[2].evidence[0].notes
  evidence_ids:
  - sources
  - placements
  - notes
  - tolner-metadata
  - tolner-author
  - metpo-primary
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_optimum_mid2.yaml
    role: Current record assertions
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: fatty-acid-ratio-direction
  issue_key: temperature-optimum-mid2-fatty-acid-ratio-direction
  category: consistency
  severity: minor
  status: open
  certainty: confirmed
  title: Fatty acid ratio direction
  description: The note says increasing the saturated/unsaturated ratio moves toward
    unsaturated fatty acids. Increasing SFA/UFA instead shifts the proportion toward
    saturated fatty acids, contradicting the stated UFA-rich direction and the edge
    description. Generic increased-unsaturation/fluidity context is supported; this
    is a bounded mathematical wording defect, separate from the imported-relation
    concern and not a proposed intervention.
  target_ids:
  - METPO:1000444
  field_paths:
  - causal_graphs[0].edges[4].evidence[0].notes
  evidence_ids:
  - record
  - notes
  - cold-primary
  - mendoza-metadata
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_optimum_mid2.yaml
    role: Current record assertions
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: human-acceptance-link
  issue_key: temperature-optimum-mid2-human-acceptance-link
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Human acceptance link
  description: Current REVIEWED status lacks attributable human acceptance of present
    assertions in the inspected local evidence. The ignored- and hidden-inclusive
    search, excluding .git/.venv, found176 matching paths and67 actual review target
    arrays with no exact target. Twelve embedded events comprise11 AI events and one
    seed;18 captured infrastructure/sibling histories contain no exact-target acceptance
    record. One current whole history and17 qualified prior whole readings are explicitly
    distinguished. Private or remote acceptance remains unknown.
  target_ids:
  - METPO:1000444
  field_paths:
  - mapping_status
  - curation_history
  evidence_ids:
  - human-search
  - histories
  - ground-reading
  - root-reading
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_optimum_mid2.yaml
    role: Current record assertions
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
actions:
- action_id: curate-imported-process-roles
  description: In separately authorized curation, reconcile the three grounded predicates
    with their actual material, quality and process referents. Preserve valid node
    identities and avoid inventing a replacement mechanism. Review wildcard increases/enables
    mapping recurrence together with record assertions; the grounder skips populated
    IDs, so rerunning it alone does not repair the current graph. The process-quality
    rigidity rule provides positive context and does not currently rewrite these edges.
  finding_ids:
  - imported-process-roles
  target_ids:
  - METPO:1000444
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_optimum_mid2.yaml
    role: Current record assertions
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Conditional recurrence mapping; not an automatic current rewrite
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Shared writer skips populated IDs; no ordinary rerun repair
  acceptance_checks:
  - Demonstrate inherited domain/range compatibility with actual referents, retaining
    the valid process endpoints and broad Biolink/event positive controls.
  - Retain NONMECHANISTIC scope, two contextual components and zero proteins unless
    independent evidence warrants a change; do not fabricate connectors or token instances.
  - Run focused strict validation, relevant graph/predicate audits, full QC and required
    curation history/product gates.
- action_id: curate-organism-category-state-facet
  description: Clarify how the existing organism-category concept is represented within
    the graph or its classification context. Reconcile the STATE field with the schema
    meaning without automatically substituting an enum or CURIE. Keep the optimum-versus-growth-range
    and exact-synonym questions explicitly separate.
  finding_ids:
  - organism-category-state-facet
  target_ids:
  - METPO:1000444
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_optimum_mid2.yaml
    role: Current record assertions
  acceptance_checks:
  - The node referent and chosen representation agree with the maintained schema,
    with any necessary scope decision documented.
  - Do not assert an imported rdfs relation or universal organism classification merely
    from lexical wording or interval containment.
  - Validate the focused record, graph/schema checks and curation history after authorized
    changes.
- action_id: curate-high-temperature-source-placement
  description: Qualify the source note to distinguish the literal high-temperature
    context from the independently supported numeric-bin hierarchy. Attach exact numerical
    support only where a relevant passage was inspected. Preserve the positive literal
    snippet and source provenance.
  finding_ids:
  - high-temperature-source-placement
  target_ids:
  - METPO:1000444
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_optimum_mid2.yaml
    role: Current record assertions
  acceptance_checks:
  - The nearest-evidence note accurately states the inspected passage and does not
    imply unestablished27–30°C support.
  - Retain independent hierarchy support and explicit full-paper access limits.
  - Validate evidence/snippet fields, curation history and strict/QC gates.
- action_id: curate-fatty-acid-ratio-direction
  description: Reconcile the written numerator/denominator and direction with the
    intended UFA-rich meaning. Keep this as a correction to the explanatory note;
    no biological optimization or new mechanism is required.
  finding_ids:
  - fatty-acid-ratio-direction
  target_ids:
  - METPO:1000444
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_optimum_mid2.yaml
    role: Current record assertions
  acceptance_checks:
  - The direction stated for SFA/UFA is mathematically consistent with the intended
    compositional meaning.
  - Preserve the distinction between generic physical source support and unresolved
    exact-bin or organism-wide efficacy.
  - Validate the edited evidence note, history and focused strict/QC gates.
- action_id: curate-human-acceptance-link
  description: Link attributable human acceptance of current assertions or reconcile
    REVIEWED through the native status workflow in separately authorized curation.
    Preserve existing AI actors and history.
  finding_ids:
  - human-acceptance-link
  target_ids:
  - METPO:1000444
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_optimum_mid2.yaml
    role: Current record assertions
  acceptance_checks:
  - Accepted assertion scope and human reviewer are attributable, or status reflects
    the available evidence.
  - Per-record and repository history validates and AI assistance remains explicit.
limitations:
- Full just test was NOT_RUN under the selected review-only diagnostic scope; only
  the five focused Stage2 tests are recorded. Products retains 123 no-adapter skips.
  Common checks establish bounded software/data integrity, not scientific support.
- Exact27–30 calibration, baseline causal sufficiency and exact mesophilic alias equivalence
  remain UNKNOWN; no outside-bin optimum inferred from20–45 growth wording.
- Mendoza and Tolner inspected abstracts/portal do not establish every adjacent numerical
  claim. Full articles not acquired; no paper-wide absence assertion.
- Spectrum actual body was available, but only generic membrane-fluidity and temperature/phase
  physical statements adopted; antimicrobial, biosensor, des-system efficacy and intervention
  details remain UNASSESSED_SCOPE.
- Ramón source is a broad review. Generic classification/phase/composition statements
  adopted; no universal organism strategy or intervention efficacy inferred.
- Canonical optimum28 and growth20–35 are separate reported strain observations; no
  full body or exhaustive response curve acquired.
- Publication notice checks use retained indexed fields and current official abstract
  identity only; no exhaustive up-to-the-minute retraction clearance.
- Original requests, present copying, extraction and current interpretation clocks
  remain separate. Current browser export is not raw HTML; its first-call start/end
  and origin cache-fetch times are unknown.
- All five abstracts were displayed for identity/context. Detailed transport, regulation,
  AMR/assay material displayed incidentally in Tolner/Spectrum/Ramón abstracts and
  the ratio-search hit p20 was not adopted, evaluated or developed.
- Full paragraph10 includes unrelated taxa after the mesophile clause; only the initial
  classification clause is adopted. No source-species catalog absence inferred.
- Scientific mesophilic exact equivalence is UNKNOWN from inspected growth-range wording
  alone; legacy Mesophilie provenance is not reconstructed.
- Baseline-adaptation repertoire/process and rigidity-transition/quality wording remain
  qualified without extra forced findings.
- Lexical edge7 is not imported rdfs; its optimum-versus-growth-range inference is
  source-scoped.
- Source note polarity/attribution and exact numeric causal bridge are separate from
  this grounding count.
- Two uncaptured histories/three node-script leads and the alias writer remain matching-line
  context, not full-body owner claims.
- B14 differs from B13; individual reused histories/authorities carry exact hashes
  and original reading/access receipts.
- Structured adapter unavailable within declared bounds; species-level source catalog
  coverage does not establish strain/module efficacy.
- Private/remote human acceptance and detailed dangerous-pathogen mechanisms remain
  unassessed.
- Root read18 actor/target/event projections and one complete process-quality history;17
  prior whole readings are agent-qualified scope.
- Only successful taxonomy retry bytes support identity; original DNS-error text remains
  a separate diagnostic.
- Detailed pathogen survival, fitness, ROS-defense, AMR and intervention efficacy
  remain UNASSESSED_SCOPE.
notes:
- Historical products failures/retry and original cache provenance remain in /private/tmp/traitmech-record-sweep-014.q8m4v2cs/new-base-diagnostic-independent-review-agent/fresh-products-completion.json.
  The earlier outstanding-products status is superseded by the actual fresh run; no
  blanket cross-batch reuse qualification is asserted.
- Final finding fields, severities and actions are supplied only by actual root FINAL.
  Current scientific uncertainty is not converted into inherited numerical, alias
  or canonical findings.
- This serializer adopts frozen audits and root adjudication. Original acquisition,
  present copy/read and extraction scopes remain separate, including browser clock
  limits and historical taxonomy failure/retry. No scientific record, state, Git or
  publication change is performed by this serializer.
tags:
- record-review
- temperature-optimum-mid2
- environment
- needs-curation
```
