# Whole-record review of temperature optimum very low

- Review: 20261022T021905Z-temperature-optimum-very-low
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-22T02:03:16.983698Z
- Finished UTC: 2026-10-22T02:19:05Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Whole-record review of temperature optimum very low finds one major imported-relation role defect across three edges and four minor issues: machinery referent precision, growth-to-optimum attribution, three nonverbatim source spans, and human acceptance traceability. Current METPO identity, numerical bin and direct parent are positive. All sixteen nodes and fifteen edges have separate formal and source dispositions; sources remain partly unknown and detailed efficacy/canonical numerical claims unassessed.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: Fifth record in the actual B14 queue; current 420-line target and 103 captured inputs. Local review is independent of remote publication.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 508ee3089c93a36413969cd1ede7f9528a1940a4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| METPO:1000441 | data/traits/environment/temperature_optimum_very_low.yaml | maintained | temperature optimum very low |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Fresh B14 corpus QC | passed | True | METPO:1000441 | Actual just qc passed: strict validation of 1130 records with 0 errors; graph audit: 74 baselined, 0 new and 0 blocking findings; 135 connected graphs and 1588 wired nodes; protein coverage: 729 graphs (134 pass, 594 NONMECHANISTIC, 0 gaps, 1 protected); snippet audit: 2419 baselined, 0 new and 0 blocking findings; 19 PathwayMech links. These are corpus diagnostics, not scientific validation of this target. |
| Fresh B14 history integrity | passed | True | METPO:1000441 | 1278 HistoryRecord YAMLs validated, 0 invalid; current history snapshot contains 1279 files. Integrity does not establish scientific correctness or human acceptance. |
| Fresh B14 mapping identifier/label validation | passed | True | METPO:1000441 | 361 canonical matches, 2 exact-synonym matches, 1 exception and 123 SKIPPED_NO_ADAPTER pairs. Configured scope is the two grounding mappings, not every target identifier or scientific claim. |
| Focused Stage2 writer tests | passed | False | METPO:1000441 | Five tests passed in the explicitly selected Stage2 test file. This is not a full just test run or biological validation. |
| Focused native validation | passed | True | METPO:1000441 | Native record validation passed; scientific interpretation is assessed separately. |
| Focused strict validation | passed | True | METPO:1000441 | The actual validate-strict command passed. |
| Focused network snippet check | passed | True | METPO:1000441 | The native command completed successfully: 17 fields across six references, 2 VERIFIED, 6 NOT_IN_ABSTRACT and 9 UNRESOLVED. Misses and unresolved responses remain inconclusive. The separate manual audit found 14 literal spans and three bounded nonverbatim spans; it does not relabel the native results. |
| One-target native review capture | passed | True | METPO:1000441 | One current target, 103 captured inputs, exact current base and successful native inspect. |
| Protein-instance metadata applicability | not_applicable | False | METPO:1000441 | Two reviewed label-only protein classes and no instances; no fabricated accession required. |
| Structured source-organism expression query availability | unavailable | False | METPO:1000441 | The maintained adapter is unavailable within current bounded discovery. Retained catalog checks and primary identity/literal context provide no module or efficacy result. |

## Scientific And Domain Assessments

### Native checklist: active bin, aliases and direct parent

identity: supported. Targets: METPO:1000441.

Active METPO:1000441, quantitative bin and direct parent are positive. Broader source terminology remains distinguished from the exact optimum bin; no additional alias finding is inferred.

### Native checklist: growth versus optimum attribution

quantity: concern. Targets: METPO:1000441.

The selected D’Amico passage uses psychrophiles broadly for microorganisms growing near freezing, including psychrotolerant usage. Two notes convert growth into optimum or at-most-10-degree support. Preserve the literal span and independently supported ontology bin; exact calibration and whole-organism sufficiency remain unknown.

### Native checklist: canonical identity and unassessed numerical support

quantity: unknown. Targets: METPO:1000441.

Official Clostridium psychrophilum species and assigned article title/identity are positive. Numerical phenotype, cultivation parameters, adaptation and optimization support remain UNASSESSED_SCOPE; no canonical paper body or temperature-response table is claimed. The actual field is canonical_examples[0].note; the frozen source-note ledger plural is only a locator typo.

### Native checklist: seven works and nineteen placements

evidence: unknown. Targets: METPO:1000441.

All seven assigned identities are positive within their retained responses. Selected generic physical and literal support is distinct from exact-bin sufficiency. Detailed stress-defense, survival/fitness, cryoprotection, protein/RNA/enzyme enhancement, cultivation and intervention efficacy remain UNASSESSED_SCOPE. Access failures do not refute uninspected source content.

### Native checklist: seventeen snippets and adjacent notes

evidence: concern. Targets: METPO:1000441.

Manual audit found fourteen literal spans and three Hamdan spans absent from retained HTML/PDF-derived text under the recorded normalizations. This is a bounded copied-span issue, not biological refutation or a claim about every publication version. Native results remain 2 VERIFIED, 6 NOT_IN_ABSTRACT and 9 UNRESOLVED; body-supported manual checks do not relabel them.

### Native checklist: all sixteen current referents

representation: concern. Targets: METPO:1000441.

Node 3 names an enzyme/lipid ensemble while typed process; sustaining-function wording leaves an activity reading plausible, so clarify the referent without prescribing an enum. Environmental and chemical identities are positive, explicit molecular activity remains valid, and node 13 lowering can denote a process. Detailed biological efficacy is unassessed.

{
  "grounding": [
    {
      "index": 0,
      "node": {
        "node_id": "temperature_optimum_very_low_trait",
        "label": "temperature optimum very low",
        "node_type": "TRAIT",
        "grounding": "METPO:1000441",
        "description": "Temperature optimum at or below ~10 °C."
      },
      "status": "supported",
      "assessment": "Active exact METPO bin with maxInclusive10 Cel and direct parent1000304; biological calibration and alias equivalence separate."
    },
    {
      "index": 1,
      "node": {
        "node_id": "temperature_optimum",
        "label": "temperature optimum",
        "node_type": "TRAIT",
        "grounding": "METPO:1000304",
        "description": "Ambient temperature supporting maximal growth."
      },
      "status": "supported",
      "assessment": "Active parent describes best-growth ambient conditions, distinct from growth breadth."
    },
    {
      "index": 2,
      "node": {
        "node_id": "cold_environment",
        "label": "cold environment",
        "node_type": "ENVIRONMENTAL_FACTOR",
        "description": "Habitat ambient temperature near the freezing point of water.",
        "grounding": "ENVO:01000309"
      },
      "status": "supported",
      "assessment": "Actual ENVO01000309 is cold environment, lower than a local/global average; near-freezing description is a contextual subset, not an exact universal definition."
    },
    {
      "index": 3,
      "node": {
        "node_id": "psychrophile_machinery",
        "label": "psychrophile cold-adapted machinery",
        "node_type": "BIOLOGICAL_PROCESS",
        "description": "Cold-active enzymes and unsaturated-lipid membranes sustaining function at very low temperature."
      },
      "status": "concern",
      "assessment": "Label and description name an ensemble of enzymes and lipid membranes, whereas BIOLOGICAL_PROCESS indicates an activity. The sustaining-function wording leaves the intended process reading plausible; bounded facet precision minor, no forced replacement enum."
    },
    {
      "index": 4,
      "node": {
        "node_id": "unsaturated_fatty_acids",
        "label": "unsaturated fatty acids",
        "node_type": "CHEMICAL",
        "description": "Unsaturated acyl chains that lower membrane melting point.",
        "grounding": "CHEBI:27208"
      },
      "status": "supported",
      "assessment": "Actual CHEBI27208 names unsaturated fatty acid including at least one C=C or C≡C bond; plural material class is compatible."
    },
    {
      "index": 5,
      "node": {
        "node_id": "membrane_fluidity",
        "label": "membrane fluidity at low temperature",
        "node_type": "QUALITY",
        "description": "Maintained membrane fluidity sustaining transport and function in the cold."
      },
      "status": "supported",
      "assessment": "Membrane fluidity denotes a measurable physical quality; maintained status does not turn the quality into its maintenance process."
    },
    {
      "index": 6,
      "node": {
        "node_id": "fatty_acid_desaturase_activity",
        "label": "fatty acid desaturase activity",
        "node_type": "MOLECULAR_FUNCTION",
        "description": "Desaturase activity introducing double bonds into fatty acyl chains."
      },
      "status": "supported",
      "assessment": "Explicit desaturase activity is MOLECULAR_FUNCTION; do not equate with its material enzyme."
    },
    {
      "index": 7,
      "node": {
        "node_id": "cold_shock_proteins",
        "label": "cold shock proteins / RNA chaperones",
        "node_type": "GENE_OR_PROTEIN",
        "grounding_status": "REVIEWED_LABEL_ONLY",
        "grounding_notes": "Reviewed as a contextual protein or protein-complex label within a quantitative measurement graph; no exact semantic family term was established for this aggregate use.",
        "description": "RNA chaperones that resolve nucleic-acid secondary structure stabilized in the cold."
      },
      "status": "supported_with_scope_limit",
      "assessment": "Reviewed label-only protein/RNA-chaperone aggregate, not RNA material or an asserted protein instance; detailed efficacy unassessed."
    },
    {
      "index": 8,
      "node": {
        "node_id": "translation_low_temperature",
        "label": "translation at low temperature",
        "node_type": "BIOLOGICAL_PROCESS",
        "description": "Maintenance of transcription and translation under low-temperature conditions."
      },
      "status": "supported_with_scope_limit",
      "assessment": "Explicit transcription/translation-maintenance activity is processual; exact biological support unassessed."
    },
    {
      "index": 9,
      "node": {
        "node_id": "protein_membrane_stabilization",
        "label": "protein and membrane stabilization under cold stress",
        "node_type": "BIOLOGICAL_PROCESS",
        "description": "Prevention of protein aggregation and stabilization of membranes during cold stress."
      },
      "status": "supported_with_scope_limit",
      "assessment": "Prevention/stabilization is processual wording; detailed cold-protection efficacy unassessed."
    },
    {
      "index": 10,
      "node": {
        "node_id": "trehalose",
        "label": "trehalose",
        "node_type": "CHEMICAL",
        "description": "Disaccharide compatible solute acting as a cryoprotectant."
      },
      "status": "supported_with_scope_limit",
      "assessment": "Trehalose is used as a chemical referent without populated identifier; no fabricated grounding or efficacy inference."
    },
    {
      "index": 11,
      "node": {
        "node_id": "cryoprotection",
        "label": "cryoprotection",
        "node_type": "BIOLOGICAL_PROCESS",
        "description": "Protection of cellular structures against freezing and freeze-thaw damage."
      },
      "status": "supported_with_scope_limit",
      "assessment": "Protection against freezing damage is explicit process wording; detailed survival/cryoprotection efficacy unassessed."
    },
    {
      "index": 12,
      "node": {
        "node_id": "antifreeze_proteins",
        "label": "antifreeze / ice-binding proteins",
        "node_type": "GENE_OR_PROTEIN",
        "grounding_status": "REVIEWED_LABEL_ONLY",
        "grounding_notes": "Reviewed as a contextual protein or protein-complex label within a quantitative measurement graph; no exact semantic family term was established for this aggregate use.",
        "description": "Ice-binding proteins that depress freezing point via thermal hysteresis."
      },
      "status": "supported_with_scope_limit",
      "assessment": "Reviewed label-only protein aggregate; no instance required by quantitative NONMECHANISTIC scope."
    },
    {
      "index": 13,
      "node": {
        "node_id": "thermal_hysteresis",
        "label": "thermal hysteresis / lowered freezing point",
        "node_type": "BIOLOGICAL_PROCESS",
        "description": "Lowering of the freezing point separating melting and freezing temperatures."
      },
      "status": "qualified",
      "assessment": "Label names a physical separation/hysteresis effect, but description explicitly describes lowering freezing point. Process reading is plausible; no categorical retype or extra defect inferred from label alone."
    },
    {
      "index": 14,
      "node": {
        "node_id": "enzyme_structural_flexibility",
        "label": "increased enzyme structural flexibility",
        "node_type": "QUALITY",
        "description": "Greater conformational flexibility of cold-adapted enzymes."
      },
      "status": "supported",
      "assessment": "Explicit structural/conformational flexibility is a quality, distinct from the process exhibiting it."
    },
    {
      "index": 15,
      "node": {
        "node_id": "catalytic_activity_low_temperature",
        "label": "catalytic activity at low temperature",
        "node_type": "MOLECULAR_FUNCTION",
        "description": "Retention of catalytic efficiency at low temperature."
      },
      "status": "supported_with_scope_limit",
      "assessment": "Explicit catalytic activity is a molecular activity; efficiency wording is a quantitative qualification, not automatic material-enzyme interpretation."
    }
  ],
  "source": [
    {
      "index": 0,
      "field": "causal_graphs[0].nodes[0]",
      "node_id": "temperature_optimum_very_low_trait",
      "label": "temperature optimum very low",
      "node_type": "TRAIT",
      "source_outcome": "unknown",
      "assessment": "Exact ≤10 optimum calibration and biological equivalence of the exact Psychrophile alias are not established by the selected generic passage; maintained bin identity is reviewed separately.",
      "incident_edges": [
        1,
        2
      ]
    },
    {
      "index": 1,
      "field": "causal_graphs[0].nodes[1]",
      "node_id": "temperature_optimum",
      "label": "temperature optimum",
      "node_type": "TRAIT",
      "source_outcome": "qualified",
      "assessment": "A temperature optimum is distinct from growth range or viability; no new source-only objection to the quantitative parent.",
      "incident_edges": [
        2
      ]
    },
    {
      "index": 2,
      "field": "causal_graphs[0].nodes[2]",
      "node_id": "cold_environment",
      "label": "cold environment",
      "node_type": "ENVIRONMENTAL_FACTOR",
      "source_outcome": "supported",
      "assessment": "The selected D’Amico introduction describes near-freezing environments and growth; it is broad context.",
      "incident_edges": [
        0
      ]
    },
    {
      "index": 3,
      "field": "causal_graphs[0].nodes[3]",
      "node_id": "psychrophile_machinery",
      "label": "psychrophile cold-adapted machinery",
      "node_type": "BIOLOGICAL_PROCESS",
      "source_outcome": "unknown",
      "assessment": "Aggregate physiological machinery description does not itself establish an exclusive or sufficient quantitative optimum; detailed mechanisms not assessed.",
      "incident_edges": [
        0,
        1,
        9,
        10,
        13,
        14
      ]
    },
    {
      "index": 4,
      "field": "causal_graphs[0].nodes[4]",
      "node_id": "unsaturated_fatty_acids",
      "label": "unsaturated fatty acids",
      "node_type": "CHEMICAL",
      "source_outcome": "qualified",
      "assessment": "Existing unsaturated-fatty-acid terminology and generic physical membrane context are supported; no bin-specific efficacy inference.",
      "incident_edges": [
        3,
        4
      ]
    },
    {
      "index": 5,
      "field": "causal_graphs[0].nodes[5]",
      "node_id": "membrane_fluidity",
      "label": "membrane fluidity at low temperature",
      "node_type": "QUALITY",
      "source_outcome": "qualified",
      "assessment": "Generic membrane-fluidity physical context is supported without quantitative optimum inference.",
      "incident_edges": [
        4,
        14
      ]
    },
    {
      "index": 6,
      "field": "causal_graphs[0].nodes[6]",
      "node_id": "fatty_acid_desaturase_activity",
      "label": "fatty acid desaturase activity",
      "node_type": "MOLECULAR_FUNCTION",
      "source_outcome": "UNASSESSED_SCOPE",
      "assessment": "Detailed cold-responsive enzyme regulation/efficacy not assessed.",
      "incident_edges": [
        3
      ]
    },
    {
      "index": 7,
      "field": "causal_graphs[0].nodes[7]",
      "node_id": "cold_shock_proteins",
      "label": "cold shock proteins / RNA chaperones",
      "node_type": "GENE_OR_PROTEIN",
      "source_outcome": "UNASSESSED_SCOPE",
      "assessment": "Protein-class naming/literal evidence only; detailed cold-survival mechanism unassessed.",
      "incident_edges": [
        5
      ]
    },
    {
      "index": 8,
      "field": "causal_graphs[0].nodes[8]",
      "node_id": "translation_low_temperature",
      "label": "translation at low temperature",
      "node_type": "BIOLOGICAL_PROCESS",
      "source_outcome": "UNASSESSED_SCOPE",
      "assessment": "Existing short literal support only; detailed translation/cold-survival physiology unassessed.",
      "incident_edges": [
        5,
        9
      ]
    },
    {
      "index": 9,
      "field": "causal_graphs[0].nodes[9]",
      "node_id": "protein_membrane_stabilization",
      "label": "protein and membrane stabilization under cold stress",
      "node_type": "BIOLOGICAL_PROCESS",
      "source_outcome": "UNASSESSED_SCOPE",
      "assessment": "Stabilization efficacy unassessed; related copied-span discrepancy separately identified.",
      "incident_edges": [
        10,
        11
      ]
    },
    {
      "index": 10,
      "field": "causal_graphs[0].nodes[10]",
      "node_id": "trehalose",
      "label": "trehalose",
      "node_type": "CHEMICAL",
      "source_outcome": "UNASSESSED_SCOPE",
      "assessment": "Existing chemical naming/literal statement only; detailed protective efficacy unassessed.",
      "incident_edges": [
        6
      ]
    },
    {
      "index": 11,
      "field": "causal_graphs[0].nodes[11]",
      "node_id": "cryoprotection",
      "label": "cryoprotection",
      "node_type": "BIOLOGICAL_PROCESS",
      "source_outcome": "UNASSESSED_SCOPE",
      "assessment": "Cryoprotective efficacy not assessed or repaired.",
      "incident_edges": [
        6,
        11,
        12
      ]
    },
    {
      "index": 12,
      "field": "causal_graphs[0].nodes[12]",
      "node_id": "antifreeze_proteins",
      "label": "antifreeze / ice-binding proteins",
      "node_type": "GENE_OR_PROTEIN",
      "source_outcome": "UNASSESSED_SCOPE",
      "assessment": "Protein-class naming/literal evidence only; no mechanism or enhancement assessment.",
      "incident_edges": [
        7
      ]
    },
    {
      "index": 13,
      "field": "causal_graphs[0].nodes[13]",
      "node_id": "thermal_hysteresis",
      "label": "thermal hysteresis / lowered freezing point",
      "node_type": "BIOLOGICAL_PROCESS",
      "source_outcome": "UNASSESSED_SCOPE",
      "assessment": "Existing Ramón quotation literal; biological efficacy not adjudicated.",
      "incident_edges": [
        7,
        12
      ]
    },
    {
      "index": 14,
      "field": "causal_graphs[0].nodes[14]",
      "node_id": "enzyme_structural_flexibility",
      "label": "increased enzyme structural flexibility",
      "node_type": "QUALITY",
      "source_outcome": "UNASSESSED_SCOPE",
      "assessment": "No enzyme engineering/flexibility enhancement assessment.",
      "incident_edges": [
        8
      ]
    },
    {
      "index": 15,
      "field": "causal_graphs[0].nodes[15]",
      "node_id": "catalytic_activity_low_temperature",
      "label": "catalytic activity at low temperature",
      "node_type": "MOLECULAR_FUNCTION",
      "source_outcome": "UNASSESSED_SCOPE",
      "assessment": "No catalytic enhancement assessment; current copied-span issue is documentary only.",
      "incident_edges": [
        8,
        13
      ]
    }
  ]
}

### Native checklist: all fifteen current relations

consistency: concern. Targets: METPO:1000441.

RO2213 edge 3 targets chemical material and edge 8 starts from a structural-flexibility quality, contrary to process roles. RO2326 edge 4 targets fluidity quality rather than process. Explicit molecular activities are not rejected by type alone. Edges 5/6 have compatible material/process endpoints; local and Biolink broad roles and subclass support remain positive without certifying efficacy.

{
  "grounding": [
    {
      "index": 0,
      "edge": {
        "subject": "cold_environment",
        "predicate": "selects for",
        "object": "psychrophile_machinery",
        "description": "Cold environments select for cold-adapted enzymes and lipids.",
        "evidence": [
          {
            "reference": "DOI:10.1038/sj.embor.7400662",
            "snippet": "growing well at temperatures around the freezing point of water",
            "notes": "Supports cold habitats as the context for psychrophile machinery."
          }
        ],
        "predicate_id": "METPO:2007401"
      },
      "status": "qualified",
      "assessment": "Local v2 selects-for has broad scaffold endpoints, with environmental-condition/adapted-trait prose. Cold environment is compatible; machinery facet and exact biological selection/bin inference remain qualified, not an invented hard domain violation."
    },
    {
      "index": 1,
      "edge": {
        "subject": "psychrophile_machinery",
        "predicate": "confers",
        "object": "temperature_optimum_very_low_trait",
        "description": "Psychrophile cold-adapted machinery yields a very-low temperature optimum.",
        "evidence": [
          {
            "reference": "DOI:10.1146/annurev-micro-091313-103612",
            "snippet": "more unsaturated fatty acids",
            "notes": "Supports homoviscous adaptation as the mechanism setting the psychrophile optimum."
          }
        ],
        "predicate_id": "METPO:2007700"
      },
      "status": "qualified",
      "assessment": "Local v8 confers permits broad subject classes and TRAIT object. Formal endpoints fit; machinery precision and exact whole-organism setpoint causal bridge remain separate/unknown."
    },
    {
      "index": 2,
      "edge": {
        "subject": "temperature_optimum_very_low_trait",
        "predicate": "is a",
        "object": "temperature_optimum",
        "description": "Temperature optimum very low is a quantitative bin of the temperature-optimum phenotype.",
        "evidence": [
          {
            "reference": "DOI:10.1038/sj.embor.7400662",
            "snippet": "growing well at temperatures around the freezing point of water",
            "notes": "Supports a ≤10 °C optimum as a value within the temperature-optimum distribution."
          }
        ],
        "predicate_id": "rdfs:subClassOf"
      },
      "status": "supported",
      "assessment": "Current bin-to-parent rdfs:subClassOf agrees with raw active METPO hierarchy."
    },
    {
      "index": 3,
      "edge": {
        "subject": "fatty_acid_desaturase_activity",
        "predicate": "increases",
        "object": "unsaturated_fatty_acids",
        "description": "Fatty acid desaturase activity increases unsaturated acyl chains.",
        "evidence": [
          {
            "reference": "DOI:10.17159/sajs.2018/20170254",
            "snippet": "increase in the proportion of unsaturated acyl chains",
            "notes": "Verified against the open Hamdan review; lower growth temperatures are described as activating desaturases that convert saturated acyl fatty acids to unsaturated ones."
          }
        ],
        "predicate_id": "RO:0002213"
      },
      "status": "concern",
      "assessment": "RO2213 inherits RO2211 process/process roles. Explicit activity subject can be processual, but material unsaturated-fatty-acid object is not an execution/process. Firm imported-role defect."
    },
    {
      "index": 4,
      "edge": {
        "subject": "unsaturated_fatty_acids",
        "predicate": "contributes to",
        "object": "membrane_fluidity",
        "description": "Increased unsaturated fatty acids contribute to membrane fluidity at low temperature.",
        "evidence": [
          {
            "reference": "DOI:10.1128/AEM.01928-22",
            "snippet": "proportion of unsaturated fatty acids was higher",
            "notes": "Verified against the open Yang et al. abstract; Bacillus simplex H-b cultured at low temperature carried a higher unsaturated-fatty-acid proportion."
          },
          {
            "reference": "DOI:10.17159/sajs.2018/20170254",
            "snippet": "maintain optimum membrane fluidity",
            "notes": "Verified against the open Hamdan review; fatty-acyl-chain modifications are described as preserving membrane fluidity in freezing environments."
          }
        ],
        "predicate_id": "RO:0002326"
      },
      "status": "concern",
      "assessment": "RO2326 inherits material/process roles via2216→2500→2595. Material fatty acids fit the subject; explicit membrane-fluidity QUALITY fails the process range."
    },
    {
      "index": 5,
      "edge": {
        "subject": "cold_shock_proteins",
        "predicate": "contributes to",
        "object": "translation_low_temperature",
        "description": "Cold shock proteins / RNA chaperones contribute to transcription and translation in the cold.",
        "evidence": [
          {
            "reference": "DOI:10.17159/sajs.2018/20170254",
            "snippet": "regulation of cellular protein synthesis",
            "notes": "Verified against the open Hamdan review; cold-shock proteins are linked to cellular protein-synthesis regulation, including transcription and translation initiation."
          }
        ],
        "predicate_id": "RO:0002326"
      },
      "status": "supported_with_scope_limit",
      "assessment": "Material protein aggregate to explicit translation process fits RO2326 endpoints. Actual contributing execution/efficacy is not validated here."
    },
    {
      "index": 6,
      "edge": {
        "subject": "trehalose",
        "predicate": "contributes to",
        "object": "cryoprotection",
        "description": "Trehalose contributes to cryoprotection.",
        "evidence": [
          {
            "reference": "DOI:10.17159/sajs.2018/20170254",
            "snippet": "preventing protein denaturation and aggregation",
            "notes": "Verified against the open Hamdan review; trehalose is reported as preventing protein denaturation and aggregation in psychrophilic bacteria."
          }
        ],
        "predicate_id": "RO:0002326"
      },
      "status": "supported_with_scope_limit",
      "assessment": "Chemical material to explicit protection process fits RO2326 endpoints. No blanket protein-only constraint; detailed role/cryoprotection efficacy unassessed."
    },
    {
      "index": 7,
      "edge": {
        "subject": "antifreeze_proteins",
        "predicate": "causes",
        "object": "thermal_hysteresis",
        "description": "Antifreeze proteins lower the freezing point via thermal hysteresis.",
        "evidence": [
          {
            "reference": "DOI:10.1007/s42770-023-01057-4",
            "snippet": "lower the water freezing point",
            "notes": "Verified against the open Ramón et al. abstract and review text; anti-freeze proteins are described as lowering the water freezing point via thermal hysteresis or ice-recrystallization inhibition."
          }
        ],
        "predicate_id": "biolink:causes"
      },
      "status": "qualified",
      "assessment": "Actual Biolink causes inherits broad NamedThing endpoints; material protein to described lowering process is not an imported RO failure. Thermal-hysteresis facet and detailed efficacy remain qualified."
    },
    {
      "index": 8,
      "edge": {
        "subject": "enzyme_structural_flexibility",
        "predicate": "increases",
        "object": "catalytic_activity_low_temperature",
        "description": "Increased enzyme structural flexibility increases catalytic activity at low temperature.",
        "evidence": [
          {
            "reference": "DOI:10.17159/sajs.2018/20170254",
            "snippet": "up to 10-fold higher specific activity",
            "notes": "Verified against the open Hamdan review; psychrophiles are described as producing structurally flexible enzymes with higher low-temperature specific activity than mesophilic homologues."
          }
        ],
        "predicate_id": "RO:0002213"
      },
      "status": "concern",
      "assessment": "RO2213 process-domain conflicts with explicit structural flexibility QUALITY. Catalytic activity can be processual; no automatic MF-object rejection."
    },
    {
      "index": 9,
      "edge": {
        "subject": "translation_low_temperature",
        "predicate": "associated with",
        "object": "psychrophile_machinery",
        "description": "Cold-shock protein support for translation is associated with psychrophile cold-adapted machinery.",
        "evidence": [
          {
            "reference": "DOI:10.4161/rna.7.6.13482",
            "snippet": "facilitating transcription and translation at low temperature",
            "notes": "Verified against the open Phadtare and Severinov PubMed abstract; this connector keeps cold-shock RNA chaperones as protein-synthesis context for psychrophile physiology."
          }
        ],
        "predicate_id": "biolink:associated_with"
      },
      "status": "qualified",
      "assessment": "Biolink associated_with has broad named-thing endpoints; process-to-machinery association formally admitted. Machinery facet and efficacy remain separate."
    },
    {
      "index": 10,
      "edge": {
        "subject": "protein_membrane_stabilization",
        "predicate": "associated with",
        "object": "psychrophile_machinery",
        "description": "Compatible-solute protein and membrane stabilization is associated with psychrophile cold-adapted machinery.",
        "evidence": [
          {
            "reference": "DOI:10.17159/sajs.2018/20170254",
            "snippet": "compatible solutes such as trehalose and glycine-betaine",
            "notes": "Verified against the open Hamdan review; this connector keeps glycine-betaine compatible-solute effects as broad cold-stress context."
          }
        ],
        "predicate_id": "biolink:associated_with"
      },
      "status": "qualified",
      "assessment": "Biolink associated_with broadly admits current process and machinery referents; no imported process-only constraint."
    },
    {
      "index": 11,
      "edge": {
        "subject": "cryoprotection",
        "predicate": "associated with",
        "object": "protein_membrane_stabilization",
        "description": "Trehalose-linked cryoprotection is associated with protein and membrane stabilization during cold stress.",
        "evidence": [
          {
            "reference": "DOI:10.17159/sajs.2018/20170254",
            "snippet": "counteracting protein aggregation, improving protein folding and stabilizing membranes and proteins at chilling temperatures",
            "notes": "Verified against the open Hamdan review; this connector keeps trehalose as a compatible-solute cryoprotection branch."
          }
        ],
        "predicate_id": "biolink:associated_with"
      },
      "status": "supported_with_scope_limit",
      "assessment": "Process/process association is formally compatible; detailed protection biology not assessed."
    },
    {
      "index": 12,
      "edge": {
        "subject": "thermal_hysteresis",
        "predicate": "associated with",
        "object": "cryoprotection",
        "description": "Antifreeze-protein thermal hysteresis is associated with cryoprotection near freezing.",
        "evidence": [
          {
            "reference": "DOI:10.1007/s42770-023-01057-4",
            "snippet": "AFPs lower the water freezing point, avoiding frostbite due to their thermal hysteresis",
            "notes": "Verified against the open Ramón et al. abstract and review text; this connector keeps antifreeze proteins as ice-binding cryoprotection context."
          }
        ],
        "predicate_id": "biolink:associated_with"
      },
      "status": "qualified",
      "assessment": "Broad association admits the lowering/hysteresis facet; no extra forced process/quality finding."
    },
    {
      "index": 13,
      "edge": {
        "subject": "catalytic_activity_low_temperature",
        "predicate": "associated with",
        "object": "psychrophile_machinery",
        "description": "Flexible-enzyme catalytic activity is associated with psychrophile cold-adapted machinery.",
        "evidence": [
          {
            "reference": "DOI:10.17159/sajs.2018/20170254",
            "snippet": "adapted to function at low temperatures, with high catalytic constants",
            "notes": "Verified against the open Hamdan review; this connector keeps low-temperature enzyme flexibility as contextual psychrophile machinery."
          }
        ],
        "predicate_id": "biolink:associated_with"
      },
      "status": "qualified",
      "assessment": "Activity-to-machinery association formally compatible under broad Biolink endpoints; no pathway completeness inference."
    },
    {
      "index": 14,
      "edge": {
        "subject": "membrane_fluidity",
        "predicate": "associated with",
        "object": "psychrophile_machinery",
        "description": "Membrane-fluidity regulation is associated with psychrophile cold-adapted machinery.",
        "evidence": [
          {
            "reference": "DOI:10.17159/sajs.2018/20170254",
            "snippet": "regulate or modulate the fluidity of the membrane in freezing environments",
            "notes": "Verified against the open Hamdan review; the membrane-fluidity section names membrane-fluidity modulation in freezing environments as a frequent psychrophile cold-adaptation strategy."
          }
        ],
        "predicate_id": "biolink:associated_with"
      },
      "status": "qualified",
      "assessment": "Quality-to-machinery association formally allowed; not RO2326 and not process-only by inherited mapping."
    }
  ],
  "source": [
    {
      "index": 0,
      "field": "causal_graphs[0].edges[0]",
      "subject": "cold_environment",
      "predicate": "selects for",
      "object": "psychrophile_machinery",
      "source_outcome": "qualified",
      "assessment": "Near-freezing environmental context is supported. Selection and sufficiency are not independently tested by the short quotation.",
      "references": [
        "DOI:10.1038/sj.embor.7400662"
      ]
    },
    {
      "index": 1,
      "field": "causal_graphs[0].edges[1]",
      "subject": "psychrophile_machinery",
      "predicate": "confers",
      "object": "temperature_optimum_very_low_trait",
      "source_outcome": "unknown",
      "assessment": "Generic unsaturation/temperature context is positive; it does not by itself establish a ≤10 optimum or a sufficient machinery-to-bin causal claim.",
      "references": [
        "DOI:10.1146/annurev-micro-091313-103612"
      ]
    },
    {
      "index": 2,
      "field": "causal_graphs[0].edges[2]",
      "subject": "temperature_optimum_very_low_trait",
      "predicate": "is a",
      "object": "temperature_optimum",
      "source_outcome": "concern",
      "assessment": "The quoted D’Amico passage is about broad near-freezing growth; the adjacent note specifically overstates it as ≤10 optimum support. Formal quantitative parentage is separately grounded.",
      "references": [
        "DOI:10.1038/sj.embor.7400662"
      ]
    },
    {
      "index": 3,
      "field": "causal_graphs[0].edges[3]",
      "subject": "fatty_acid_desaturase_activity",
      "predicate": "increases",
      "object": "unsaturated_fatty_acids",
      "source_outcome": "UNASSESSED_SCOPE",
      "assessment": "Existing short Hamdan phrase is literal; detailed desaturase regulation/cold-adaptation efficacy is outside the declared scope.",
      "references": [
        "DOI:10.17159/sajs.2018/20170254"
      ]
    },
    {
      "index": 4,
      "field": "causal_graphs[0].edges[4]",
      "subject": "unsaturated_fatty_acids",
      "predicate": "contributes to",
      "object": "membrane_fluidity",
      "source_outcome": "qualified",
      "assessment": "Both supplied spans are literal. The Yang attribution remains its reported B. simplex H-b context; generic unsaturation/fluidity context does not establish a universal optimum bin or an intervention effect.",
      "references": [
        "DOI:10.1128/AEM.01928-22",
        "DOI:10.17159/sajs.2018/20170254"
      ]
    },
    {
      "index": 5,
      "field": "causal_graphs[0].edges[5]",
      "subject": "cold_shock_proteins",
      "predicate": "contributes to",
      "object": "translation_low_temperature",
      "source_outcome": "UNASSESSED_SCOPE",
      "assessment": "Literal Hamdan phrase verified only; detailed protein-synthesis/cold-survival role not adjudicated.",
      "references": [
        "DOI:10.17159/sajs.2018/20170254"
      ]
    },
    {
      "index": 6,
      "field": "causal_graphs[0].edges[6]",
      "subject": "trehalose",
      "predicate": "contributes to",
      "object": "cryoprotection",
      "source_outcome": "UNASSESSED_SCOPE",
      "assessment": "Existing Hamdan span is literal. Mixed/pathogen context occurs nearby; detailed trehalose survival/defense efficacy not assessed.",
      "references": [
        "DOI:10.17159/sajs.2018/20170254"
      ]
    },
    {
      "index": 7,
      "field": "causal_graphs[0].edges[7]",
      "subject": "antifreeze_proteins",
      "predicate": "causes",
      "object": "thermal_hysteresis",
      "source_outcome": "UNASSESSED_SCOPE",
      "assessment": "Existing Ramón phrase is literal in the retained HTML; antifreeze efficacy/mechanisms not assessed.",
      "references": [
        "DOI:10.1007/s42770-023-01057-4"
      ]
    },
    {
      "index": 8,
      "field": "causal_graphs[0].edges[8]",
      "subject": "enzyme_structural_flexibility",
      "predicate": "increases",
      "object": "catalytic_activity_low_temperature",
      "source_outcome": "UNASSESSED_SCOPE",
      "assessment": "Existing enzyme-activity comparison phrase is literal; no enhancement, engineering or low-temperature efficacy assessment.",
      "references": [
        "DOI:10.17159/sajs.2018/20170254"
      ]
    },
    {
      "index": 9,
      "field": "causal_graphs[0].edges[9]",
      "subject": "translation_low_temperature",
      "predicate": "associated with",
      "object": "psychrophile_machinery",
      "source_outcome": "UNASSESSED_SCOPE",
      "assessment": "Supplied Phadtare phrase is literal in current PMC HTML despite indexed-abstract miss; detailed RNA/protein-synthesis mechanism not assessed.",
      "references": [
        "DOI:10.4161/rna.7.6.13482"
      ]
    },
    {
      "index": 10,
      "field": "causal_graphs[0].edges[10]",
      "subject": "protein_membrane_stabilization",
      "predicate": "associated with",
      "object": "psychrophile_machinery",
      "source_outcome": "concern",
      "assessment": "Supplied Hamdan snippet is not literal on either inspected primary surface; the stabilization connector’s biological efficacy remains unassessed.",
      "references": [
        "DOI:10.17159/sajs.2018/20170254"
      ]
    },
    {
      "index": 11,
      "field": "causal_graphs[0].edges[11]",
      "subject": "cryoprotection",
      "predicate": "associated with",
      "object": "protein_membrane_stabilization",
      "source_outcome": "concern",
      "assessment": "Supplied Hamdan snippet is not literal on either inspected primary surface; no biological refutation or detailed cryoprotection assessment.",
      "references": [
        "DOI:10.17159/sajs.2018/20170254"
      ]
    },
    {
      "index": 12,
      "field": "causal_graphs[0].edges[12]",
      "subject": "thermal_hysteresis",
      "predicate": "associated with",
      "object": "cryoprotection",
      "source_outcome": "UNASSESSED_SCOPE",
      "assessment": "Existing Ramón phrase is literal; no cryoprotection intervention/efficacy adjudication.",
      "references": [
        "DOI:10.1007/s42770-023-01057-4"
      ]
    },
    {
      "index": 13,
      "field": "causal_graphs[0].edges[13]",
      "subject": "catalytic_activity_low_temperature",
      "predicate": "associated with",
      "object": "psychrophile_machinery",
      "source_outcome": "concern",
      "assessment": "Supplied Hamdan snippet is not literal on either inspected primary surface; enzyme enhancement/catalytic efficacy remains unassessed.",
      "references": [
        "DOI:10.17159/sajs.2018/20170254"
      ]
    },
    {
      "index": 14,
      "field": "causal_graphs[0].edges[14]",
      "subject": "membrane_fluidity",
      "predicate": "associated with",
      "object": "psychrophile_machinery",
      "source_outcome": "qualified",
      "assessment": "Existing Hamdan fluidity phrase is literal; basic membrane physical context retained without asserting quantitative optimum or machinery sufficiency.",
      "references": [
        "DOI:10.17159/sajs.2018/20170254"
      ]
    }
  ]
}

### Native checklist: maintained payloads, guards and consumers

ownership: supported. Targets: METPO:1000441.

Formal edges recur in the exact review-writer payload and connector SOURCE_CONNECTOR_EDGES preimage assumptions, with conditional wildcard mappings. Current review replay rejects the pruned partial state; connector no-ops and grounder skips populated IDs. Quotation spans are in connector ADDED_EDGES, consumed by PR664; that consumer is not the original formal-edge writer. Machinery facet and attribution notes are record-only. No ordinary rerun is a repair.

### Native checklist: attributable human acceptance

provenance: concern. Targets: METPO:1000441.

Seventeen embedded events comprise sixteen AI events and one seed. Ignored- and hidden-inclusive discovery found 185 matching paths and 71 actual top-level target arrays, none exact. Seventeen history projections, seven current whole histories and ten qualified prior whole readings establish no attributable local human acceptance. Root selected/projection reading is separately attributed; private or remote acceptance remains unknown.

### Native checklist: bounded catalog and adapter availability

completeness: unknown. Targets: METPO:1000441.

Retained catalog checks cover selected canonical/source-organism names only; they do not establish global expression absence or exhaustive coverage of all incidental source taxa. Current bounded discovery found the maintained adapter unavailable. Primary fallback is limited to identity and supplied generic/literal context; no module membership or efficacy result is reported.

### Native checklist: scope and optional protein instances

completeness: supported. Targets: METPO:1000441.

One component, sixteen nodes and fifteen edges form a quantitative NONMECHANISTIC record. Two reviewed label-only protein classes and no instances do not require fabricated accessions or additional connectors. Completeness of the review does not certify detailed biological mechanisms.

### Native checklist: actual native and fresh B14 diagnostics

schema: supported. Targets: METPO:1000441.

Current inspect, focused validation, strict validation and snippet command completed successfully. Snippet misses/unresolved responses remain inconclusive. B14 common checks are actual fresh executions at the advanced base, with original failures, cache provenance, product skips and omitted full suite retained. Software integrity does not establish scientific meaning.

## Findings

### imported-process-roles: Imported process roles

major / open / confirmed; issue key: temperature-optimum-very-low-imported-process-roles.

Edges 3 and 8 use RO:0002213, whose inherited domain and range require processes: edge 3 targets explicit material fatty acids and edge 8 starts from explicit structural flexibility QUALITY. Edge 4 uses RO:0002326, whose material-to-process roles conflict with its membrane-fluidity QUALITY object. The explicit activity endpoints are not rejected merely for MOLECULAR_FUNCTION type. These are formal representation defects, independent of detailed biological efficacy.

### machinery-facet: Machinery facet

minor / open / confirmed; issue key: temperature-optimum-very-low-machinery-facet.

Node 3 is typed BIOLOGICAL_PROCESS while its label and description name an ensemble of enzymes and lipid membranes. The sustaining-function wording leaves an activity interpretation plausible. Clarify the intended referent; this bounded precision issue does not establish a required replacement enum or refute biological relevance.

### growth-versus-optimum-attribution: Growth versus optimum attribution

minor / open / confirmed; issue key: temperature-optimum-very-low-growth-versus-optimum-attribution.

The D’Amico passage explicitly uses psychrophiles broadly for microorganisms growing near freezing, including psychrotolerant/psychrotroph usage. Two attached notes convert that growth statement into optimum or at-most-10-degree support. Qualify these local attributions while preserving the literal snippet and independently supported METPO bin and parent. No assertion is made that the uninspected remainder lacks all numerical context.

### nonverbatim-source-snippets: Nonverbatim source snippets

minor / open / confirmed; issue key: temperature-optimum-very-low-nonverbatim-source-snippets.

Three supplied Hamdan snippets have no literal match in the retained SciELO HTML or publisher PDF-derived text, including whitespace normalization, case folding and line-end dehyphenation. Their exact strings are also in the current connector ADDED_EDGES payload. Treat this as a bounded copied-span presentation issue; the biological propositions and other publication versions are not refuted.

### human-acceptance-link: Human acceptance link

minor / open / confirmed; issue key: temperature-optimum-very-low-human-acceptance-link.

The REVIEWED status has no attributable human acceptance in the inspected local scope. Seventeen embedded events contain sixteen AI events and one seed. Ignored- and hidden-inclusive discovery found 185 matching paths and 71 actual top-level review target arrays, with no exact current target. Seventeen captured histories have AI actor projections, with seven current whole and ten byte-qualified prior whole readings. Private or remote acceptance remains unknown.

## Recommended Actions And Acceptance Checks

### curate-imported-process-roles

In separately authorized curation, reconcile the three imported relations with their explicit material, quality and activity referents. Coordinate the exact review-writer payload, connector source-preimage guards, and wildcard increases/contributes-to mappings. Current review replay rejects its pruned partial state, the current connector no-ops, and the grounder skips populated IDs; an ordinary rerun is not a repair. No replacement biological mechanism or intervention is proposed.

- Show inherited domain/range compatibility for edges 3, 4 and 8 while preserving the intended referents.
- Keep the target writer payload and connector SOURCE_CONNECTOR_EDGES assumptions consistent under explicit replay/drift checks; PR664 ADDED_EDGES is not the replacement source for these formal edges.
- Preserve RO:0002326 endpoint controls at edges 5 and 6, broad local/Biolink roles and direct subclass support; endpoint compatibility does not certify efficacy.
- Run focused strict and relevant predicate/graph checks, full QC and required history/product gates.

### curate-machinery-facet

Clarify whether node 3 denotes the material ensemble or its activity, and make its label, description and type consistently denote that intended referent. Do not prescribe an unsupported exact ontology term or add a detailed mechanism.

- The retained node has one explicit referent consistent with the schema facet.
- Preserve uncertainty about exact quantitative calibration and causal sufficiency; run focused strict and applicable curation gates.

### curate-growth-versus-optimum-attribution

Qualify the two evidence notes to the inspected broad growth context, distinguishing it from the ontology-supported numerical bin and direct parent relation. Preserve the literal source span.

- Each note describes only what its nearest inspected passage supports.
- Retain the positive ontology hierarchy and rerun focused strict/snippet checks and applicable curation gates.

### curate-nonverbatim-source-snippets

Resolve the three literal-span discrepancies in the current record and exact connector quotation payload. Use only independently verified source text in snippet fields; keep interpretation clearly separate and leave unsupported attribution explicit. Preserve the current guard behavior and validate the PR664 consumer of ADDED_EDGES. No new mechanistic or intervention claim is proposed.

- Each retained snippet has an exact auditable location on its cited inspected source surface; do not silently present a paraphrase as a quotation.
- Current connector payload and record agree, with current no-op/drift guards and PR664 consumer behavior checked before any authorized replay.
- Rerun focused strict and snippet checks, full QC and required history/product gates; literal correctness is not biological validation.

### curate-human-acceptance-link

Link actual attributable human acceptance of these current assertions, if available, or qualify the review-status provenance under repository policy. Do not fabricate retrospective sign-off.

- Acceptance evidence identifies a person, exact assertions and disposition, or remaining uncertainty is explicit.
- Preserve append-only history and run applicable maintained gates for any separately authorized curation change.

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
| check-temperature-optimum-very-low-validate | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-validate.log; Executed 2026-10-22T02:03:36.851813+00:00 through 2026-10-22T02:03:37.774545+00:00; metadata temperature-optimum-very-low-validate.json | context_only | Native record validation passed; scientific interpretation is assessed separately. |
| check-temperature-optimum-very-low-strict | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-strict.log; Executed 2026-10-22T02:03:36.851958+00:00 through 2026-10-22T02:03:38.297943+00:00; metadata temperature-optimum-very-low-strict.json | context_only | The actual validate-strict command passed. |
| check-temperature-optimum-very-low-snippets-network | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-snippets-network.log; Executed 2026-10-22T02:03:46.986231+00:00 through 2026-10-22T02:04:00.891440+00:00; metadata temperature-optimum-very-low-snippets-network.json | context_only | The native command completed successfully: 17 fields across six references, 2 VERIFIED, 6 NOT_IN_ABSTRACT and 9 UNRESOLVED. Misses and unresolved responses remain inconclusive. The separate manual audit found 14 literal spans and three bounded nonverbatim spans; it does not relabel the native results. |
| capture | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low.inspect.json; Actual successful native inspect with 103 captured inputs | context_only | All current source hashes and the exact target are bound before serialization. |
| record | data/traits/environment/temperature_optimum_very_low.yaml; Whole current record | supports | Sixteen nodes, fifteen edges, seventeen embedded events, one canonical example, two reviewed label-only protein classes and no instances. |
| local-init | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/batch014-local-initialization-receipt.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Actual local initialization and fifth queue target; publication remains separate. |
| policy | docs/GROUNDING_POLICY.md; Captured maintained authority | supports | Protein family/function grounding and optional protein instances. |
| playbook | docs/CURATION_PLAYBOOK.md; Captured maintained authority | supports | Literal source scope and attributable acceptance. |
| schema | src/traitmech/schema/traitmech.yaml; Captured maintained authority | supports | Current facets, material referents and NONMECHANISTIC scope. |
| predicate-mapping | mappings/predicate_grounding.tsv; Captured maintained authority | supports | Conditional increases/contributes-to mappings populate empty IDs; current populated assertions are skipped. |
| identity | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-ground-agent/identity-assessment.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Active exact bin, direct parent, environmental/chemical identities and official species identity; no numerical phenotype inference. |
| nodes-edges | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-ground-agent/node-edge-grounding-ledger.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | All sixteen node and fifteen edge judgments with endpoint-positive controls. |
| ground-assessment | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-ground-agent/documentary-assessment.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | One grouped imported-role major and two bounded facet/provenance minors, without detailed efficacy assessment. |
| owners | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-ground-agent/owner-provenance-assessment.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Exact review payload, connector source-preimage guard and current ADDED_EDGES consumer distinguished. |
| owner-primary | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-ground-agent/owner-primary-reading.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Actual maintained writer/migration windows and replay/no-op/skip qualifications. |
| human-search | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-ground-agent/search-and-provenance.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | 185 ignored- and hidden-inclusive matching paths, 71 actual review target arrays, zero exact target. |
| histories | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-ground-agent/history-reading-provenance.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Seven current whole histories plus ten qualified prior whole readings; seventeen current actor/target/event projections. |
| discovery | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-ground-agent/discovery-disposition.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Twenty-nine script leads; the uncaptured thermotaxis script is matching-line context, not a fully read current owner. |
| expression | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-ground-agent/expression-and-readiness.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Bounded retained catalog and selected organism checks; no global expression absence or module result. |
| expression-discovery | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-ground-agent/expression-runner-current-discovery.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Fresh bounded PATH/project/install-root adapter discovery, not a global absence claim. |
| local-authority | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-ground-agent/local-authority-reading.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Actual local confers/selects-for, mappings, Biolink and schema windows. |
| ground-reading | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-ground-agent/reading-scope-receipt.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Actual current and qualified prior reading scopes; documentary history does not adopt historical efficacy claims. |
| ground-manifest | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-ground-agent/evidence-manifest.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | All 31 frozen ground artifacts verified. |
| metpo-primary | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/repo/data/raw/metpo.owl; Selected current raw class and direct parent at the recorded reading time | supports | Active very-low optimum bin and direct parent are positive; exact biological calibration and sufficiency remain qualified. |
| metpo-projection | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-ground-agent/metpo-authority.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Exact raw source hash and current selected class elements. |
| ro-primary | /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/ro.db; Exact adopted response with original query time and recorded database hash | supports | RO2213 requires process endpoints; RO2326 inherits material-to-process roles through 2216, 2500 and 2595. Explicit molecular activity endpoints remain process-compatible. |
| ro-projection | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-ground-agent/selected-ro-primary-reading.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Exact retained response at its original query clock; root separately queried current authority. |
| primary-reuse | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-ground-agent/primary-reuse-receipt.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Original RO query clock and current copying remain distinct. |
| envo-primary | /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/envo.db; Current selected read-only query against the previously hash-qualified cache | supports | Cold-environment identity is positive; no phenotype or tolerance transfer. |
| envo-projection | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-ground-agent/envo-primary-reading.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Cold-environment identity is positive; no phenotype or tolerance transfer. |
| chebi-primary | /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/chebi.db; Current selected read-only query against the previously hash-qualified cache | supports | Unsaturated fatty acid and lipid material referents are distinguished from quality and activity. |
| chebi-projection | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-ground-agent/chebi-primary-reading.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Unsaturated fatty acid and lipid material referents are distinguished from quality and activity. |
| ontology-cache | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-ground-agent/ontology-cache-provenance.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Original selected database hash clocks and current selected query provenance; no fresh release or duplicate large-database hashing claim. |
| definition-metadata | DOI:10.1038/sj.embor.7400662; Retained indexed identity and bounded status fields | supports | Positive identity; source classification interpretation is separately bound to the author-repository PDF. |
| definition-pdf | DOI:10.1038/sj.embor.7400662; Retained author-repository PDF, selected classification lines via separately derived raw text | supports | Broad near-freezing growth includes psychrotolerant usage; it is not automatically an optimum or at-most-10-degree statement. |
| mendoza-metadata | DOI:10.1146/annurev-micro-091313-103612; Indexed identity and supplied generic physical abstract spans | supports | Generic membrane physical context only; detailed efficacy and exact-bin sufficiency unassessed. |
| mendoza-publisher | DOI:10.1146/annurev-micro-091313-103612; Retained actual browser abstract export, not raw HTML | supports | Original tool-call interval retained; origin cache-fetch time is unknown. |
| cold-metadata | DOI:10.1007/s42770-023-01057-4; Retained indexed identity/status | supports | Positive article identity, not detailed cold-defense efficacy. |
| cold-body | DOI:10.1007/s42770-023-01057-4; Retained HTML all-p paragraph 78, existing supplied literal spans only | supports | Literal occurrence positive; detailed antifreeze/cryoprotection efficacy remains UNASSESSED_SCOPE. |
| phadtare-metadata | DOI:10.4161/rna.7.6.13482; Retained indexed identity/status | supports | Article identity positive; an abstract miss does not refute a supplied body span. |
| definition-extraction-text | DOI:10.1038/sj.embor.7400662; Raw text lines 24–33 using newline splitting | partial | Selected broad classification interpretation; original PDF acquisition, prior extraction and current copy clocks are separate. |
| definition-extraction | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/definition-derivation-receipt.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Actual extraction command and source/output hashes; extraction time is not original source acquisition. |
| hamdan-extraction-text | DOI:10.17159/sajs.2018/20170254; Publisher PDF-derived text, mechanical search of supplied strings | partial | Three nonmatches after whitespace/casefold/dehyphenation checks; this is not whole-paper biological interpretation. |
| hamdan-extraction | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/hamdan-derivation-receipt.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Actual extraction command and source/output hashes; extraction time is not original source acquisition. |
| hamdan-crossref | DOI:10.17159/sajs.2018/20170254; Fresh Crossref identity/status fields | supports | Positive identity after zero indexed hits; bounded notice fields only. |
| hamdan-crossref-access | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/hamdan-crossref.json.access.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Actual current request interval and response hash; interpretation restricted to the declared reading scope. |
| hamdan-html | DOI:10.17159/sajs.2018/20170254; Retained HTML selected paragraphs 33/34/40/42/44 and supplied-string matching | partial | Three supplied spans are nonverbatim on this surface; incidental pathogen and detailed adaptation efficacy unassessed. |
| hamdan-html-access | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/hamdan.html.access.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Actual current request interval and response hash; interpretation restricted to the declared reading scope. |
| hamdan-pdf | DOI:10.17159/sajs.2018/20170254; Publisher PDF input to separately recorded extraction | partial | Additional surface for bounded literal checks only; no full-paper efficacy assessment. |
| hamdan-pdf-access | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/hamdan.pdf.access.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Actual current request interval and response hash; interpretation restricted to the declared reading scope. |
| phadtare-html | DOI:10.4161/rna.7.6.13482; Current retained HTML all-p paragraphs 11 and 23 | supports | Existing supplied span literal in body; detailed RNA/chaperone efficacy remains unassessed. |
| phadtare-html-access | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/phadtare.html.access.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Actual current request interval and response hash; interpretation restricted to the declared reading scope. |
| yang-metadata | DOI:10.1128/AEM.01928-22; Fresh indexed identity and supplied existing literal abstract span | supports | Bacillus simplex H-b source context and literal occurrence only; no detailed intervention or efficacy assessment. |
| yang-metadata-access | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/yang-metadata-access.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Actual current request interval and response hash; interpretation restricted to the declared reading scope. |
| canonical-metadata | DOI:10.1016/j.bbalip.2013.02.004; Fresh indexed title/identity and bounded notice fields only | supports | Canonical article identity positive; numerical optimum, culture parameters and adaptation/optimization claims are UNASSESSED_SCOPE. |
| canonical-metadata-access | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/canonical-metadata-access.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Actual current request interval and response hash; interpretation restricted to the declared reading scope. |
| hamdan-index-access | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/hamdan-metadata-access.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Successful request with zero indexed hits; Crossref/publisher identity is positive, so no missing-source finding. |
| yang-body-failure | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/yang.xml.access.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Actual HTTP 500 request, no acquired XML body; indexed snippet occurrence remains positive and body absence is not inferred. |
| current-browser | DOI:10.1038/sj.embor.7400662; DOI:10.1146/annurev-micro-091313-103612; Actual browser call 2026-10-22 02:03:52 UTC through 2026-10-22 02:03:53 UTC; export 2026-10-22 02:03:57 UTC | partial | EMBO access failure and Mendoza publisher generic context only. This is a tool response, not raw HTML; origin/cache-fetch clock unknown. |
| browser-failure-copy | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/root-browser-failure-copy.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Retained earlier Hamdan browser failure, separate from successful current source-agent HTML/PDF access; no invented HTTP status. |
| phadtare-prior-limits | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/phadtare-prior-access-limits.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Prior failed attempts remain historical; current successful HTML supports the bounded literal check. |
| taxonomy | NCBITaxon:132926; Fresh successful official taxonomy retry, scientific name and rank only | supports | Clostridium psychrophilum species identity positive; no numerical phenotype or cultivation transfer. |
| taxonomy-access | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-ground-agent/taxonomy-network-retry-access.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Actual successful request and response hash. |
| taxonomy-reading | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-ground-agent/taxonomy-identity.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Species identity interpreted separately from canonical phenotype support. |
| taxonomy-initial-failure | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=132926; Initial DNS-error bytes, not taxonomy XML | context_only | Retrieval failure followed by successful official retry; no native validation failure. |
| taxonomy-failure-access | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-ground-agent/taxonomy-access.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Initial failed request interval and error hash retained separately. |
| sources | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/source-assessment.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Seven works; overall source scope remains unknown with two bounded source minor findings. |
| source-identities | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/source-ledger.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | All seven assigned identities and actual classification/source scopes; bounded original notice observations. |
| source-status | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/source-status-ledger.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Response-scoped publication/notice observations, not an exhaustive current notice search. |
| placements | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/source-placement-ledger.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | All nineteen external placements; nineteen grounding fields are separately accounted in source and ground node-edge ledgers. |
| snippets | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/snippet-ledger.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Seventeen schema snippets: fourteen literal and three bounded nonverbatim spans; no separate adopted quoted-note spans. |
| literal-check | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/literal-match-completion.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Mechanical occurrence checks across declared retained surfaces, without whole-paper efficacy claims. |
| notes | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/source-note-ledger.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Eighteen notes including canonical note; canonical locator uses plural notes in this ledger but actual field is singular note, as clarified by root. |
| source-nodes-edges | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/node-edge-source-ledger.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | All sixteen nodes and fifteen edges with selected physical/literal support distinguished from excluded efficacy. |
| canonical | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/canonical-assessment.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Article identity positive; canonical numerical phenotype, cultivation and optimization support unassessed. |
| source-reading | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/primary-reading-scope.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Selected classification/physical/literal passages only; canonical title/identity and explicit mechanism exclusions. |
| source-access | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/source-access-limits.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Actual successful/failed/unacquired surfaces, no inference that inaccessible bodies lack a claim. |
| source-reuse | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/source-reuse-receipt.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Twelve exact copies; nested original acquisition, current copy and separate extraction/read clocks retained. |
| source-native | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/native-context.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Native 2 VERIFIED/6 NOT_IN_ABSTRACT/9 UNRESOLVED versus separate manual 14 literal/3 nonverbatim results. |
| source-manifest | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/evidence-manifest.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | All 52 frozen source artifacts verified. |
| root-reading | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-root/selected-primary-reading.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Root selected primary and authority reading; whole-target reading is not a whole-paper mechanism review. |
| root-verification | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-root/root-current-verification.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Root current inputs/artifacts/71 target arrays verified; exact connector quote payload, consumer and singular canonical note clarified. |
| adjudication | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-root-adjudication.json; Final root adjudication | supports | Exact one major and four minors, qualified owners and documentary actions; all unknown and unassessed scopes retained. |

## Limits And Additional Notes

- Full just test was NOT_RUN under the selected review-only diagnostic scope; only the five focused Stage2 tests are recorded. Products retains 123 no-adapter skips. Common checks establish bounded software/data integrity, not scientific support.
- Detailed stress-defense, survival, fitness, cryoprotection, enzyme/RNA/protein enhancement, cultivation optimization and intervention efficacy remain UNASSESSED_SCOPE; no operational repair proposed.
- Canonical DOI/title and official species identity are positive; canonical numerical optimum, culture conditions and phenotype claims were not assessed, and no canonical article body/table was acquired.
- The METPO class establishes the current at-most-10 Cel bin and direct parent; its existential restriction is not a universal growth curve or independent biological calibration. Exact biological equivalence of the inherited Psychrophile alias remains unresolved.
- Generic membrane physical context and source presence do not establish a sufficient or exclusive mechanism for the quantitative optimum.
- Hamdan three-span absence is bounded to retained primary HTML/PDF extracted surfaces and normalization used; it is not biological refutation or an all-publication-version search.
- D’Amico selected generic introduction and supplied literal phrase only; Mendoza publisher abstract only. Whole-body mechanistic reading is not claimed.
- Original source acquisition, derived-text extraction, current copies, browser calls/exports and current readings retain distinct times. Reused metadata notice fields are not current publication-status refreshes.
- Hamdan EuropePMC zero hit and root DOI browser failure are diagnostics, superseded for identity by actual Crossref/HTML/PDF evidence. Yang XML HTTP500 yielded no body; its supplied phrase is literal in the indexed abstract. Phadtare prior failed body attempts are separate from its current successful HTML literal check.
- Taxonomy initial DNS failure is preserved separately from the successful official retry. Identity does not prove phenotype or strain-to-species transfer.
- Seventeen history actor/target/event projections were inspected, with seven current whole and ten individually byte-qualified prior whole readings; seed and AI actors do not establish human acceptance. Private and remote acceptance remains unknown.
- Expression adapter unavailable in fresh bounded PATH/project/install discovery; retained catalog has20organisms28datasets with original access time. No exact canonical/Bacillus simplex or incidental Listeria key is present in that catalog, not a global absence across all source organisms. No detailed module queries or causal claims made.
- NONMECHANISTIC measurement scope, one connected component, two reviewed label-only protein classes and zero instances do not require invented proteins, connectors or mechanisms.
- All sources, formal roles, quotation checks, record status and software checks retain their distinct evidential scopes; schema/QC success is not scientific validation.
- Root final combines the independently frozen grounding assessment (one major/two minors) and source assessment (two minors); it does not promote source UNKNOWN or UNASSESSED_SCOPE claims to supported.
- Formal owner roles differ: review script owns exact after-payload; connector SOURCE_CONNECTOR_EDGES is a source-preimage guard. For the quotation finding, connector ADDED_EDGES is the actual payload; PR664 is its consumer requiring validation, not the origin of the snippet template.
- Frozen source-note-ledger labels the canonical field canonical_examples[0].notes; the actual current field is singular canonical_examples[0].note. This is a locator clarification only, and no finding is attached to that canonical claim.
- Root primary reading is bounded by selected-primary-reading.json and root-current-verification.json. Detailed source literal checks and broader owner/history reads are attributed to the independent peers; no claim that root reread every full paper, script or prior whole history.
- RO:0002326 roles follow 2216 to 2500 to 2595; GO-specific usage commentary does not impose an invented universal protein-only domain. Compatible edge5/6 endpoints do not establish contributing execution or biological efficacy.
- Node13 explicitly describes lowering of freezing point; its process reading remains plausible despite the hysteresis label. No extra forced type finding.
- The current native snippet command passed with 2 VERIFIED, 6 NOT_IN_ABSTRACT and 9 UNRESOLVED. Separate primary checks found 14 of17 supplied spans literal and three nonverbatim on inspected surfaces; the native result is not rewritten.
- Ground search uses the exact current label/ID/slug, includes hidden/ignored entries except .git/.venv, and reads actual top-level targets arrays. One extra uncaptured thermotaxis-script matching line is generic context only, not a fully audited current owner.
- Historical products failures/retry and original cache provenance remain in /private/tmp/traitmech-record-sweep-014.q8m4v2cs/new-base-diagnostic-independent-review-agent/fresh-products-completion.json. The earlier outstanding-products status is superseded by the actual fresh run; no blanket cross-batch reuse qualification is asserted.
- Final fields, severities, owners and actions come only from actual root FINAL. Frozen source and formal ledgers retain unknown and unassessed scope; no inherited finding or biological repair is added.
- The serializer adopts frozen audits and root adjudication. Original acquisition, historical extraction, current copying/reading, actual browser call/export and failed/successful request clocks remain distinct. It makes no scientific record, state, Git or publication changes.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T021905Z-temperature-optimum-very-low
kind: record
repository: CultureBotAI/TraitMech
title: Whole-record review of temperature optimum very low
started_at: '2026-10-22T02:03:16.983698Z'
finished_at: '2026-10-22T02:19:05Z'
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
summary: 'Whole-record review of temperature optimum very low finds one major imported-relation
  role defect across three edges and four minor issues: machinery referent precision,
  growth-to-optimum attribution, three nonverbatim source spans, and human acceptance
  traceability. Current METPO identity, numerical bin and direct parent are positive.
  All sixteen nodes and fifteen edges have separate formal and source dispositions;
  sources remain partly unknown and detailed efficacy/canonical numerical claims unassessed.'
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
  - path: data/traits/environment/temperature_optimum_very_low.yaml
    sha256: 1248a6be1eec6a1c5b4fcaec1102617f04fdf4db70d017bd2f35daeaadc515fa
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
  - path: history/infrastructure/curate-knowledge-gaps/2026-08-17T214933Z-claude-code-9c4af0.yaml
    sha256: a58b53be777e58ac29eb1c1571feb2593633c83d158aff4b6c96b8a1b9214c0f
    role: context
  - path: history/infrastructure/node-type-consistency/2026-08-15T014631Z-claude-code-9d7f4d.yaml
    sha256: 21f19561c0d4769e7acc62e05e41d0d395a0f239938f00829f79f2b9c3ac2510
    role: context
  - path: history/infrastructure/pr664-adversarial-review/2026-09-07T010000Z-codex-60bca2.yaml
    sha256: 44f328d3f4735a641a33e6f5823a043ccc87594971cfdd9b58be134f3ea70106
    role: context
  - path: history/infrastructure/protein-vs-activity/2026-08-15T202806Z-claude-code-ddcd62.yaml
    sha256: 58f55f2617869c39eb6412455c0d838b350433ff0ad979c848be1df9bcb3fd4f
    role: context
  - path: history/other/canonical-examples-batch1/2026-08-20T074839Z-claude-code-6fb2f5.yaml
    sha256: c938f2928f2eb41505d58c2fb72d8de01d99534d766de9af400010e8778988a4
    role: context
  - path: history/other/canonical-examples-six/2026-08-21T065406Z-codex-a1ab82.yaml
    sha256: 23be5f6ab519511e3e23feffa85813eec4fa3c7e6b900e77fd4a3adc0c26da0e
    role: context
  - path: history/other/free-living-trehalose-external-research/2026-08-31T203047Z-claude-code-47e2e8.yaml
    sha256: e250d11c361b6dcb5184d42a754b855ab8dc30028832a27ae914fee6c331a70f
    role: context
  - path: history/records/free_living/2026-08-31T204506Z-claude-code-ca81b1.yaml
    sha256: 0c2d8296d829bf97b806e44163c6138eac07431dbedc34e99a70bcbb191c7fe4
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
  - path: research/traits/environment/temperature_optimum_very_low-deep-research-falcon.md
    sha256: 850f8d349943de070832602fdf2fd348eeee1c4140a52ec2c27d34356cabc56b
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
  - path: scripts/repair_pr664_adversarial_review.py
    sha256: 5717a89bee383aa0e12aec9bf30434ccff74efcbe64684d13ef9b290b1accf96
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
- target_id: METPO:1000441
  path: data/traits/environment/temperature_optimum_very_low.yaml
  label: temperature optimum very low
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_optimum_very_low.yaml
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
  selection: Fifth record in the actual B14 queue; current 420-line target and 103
    captured inputs. Local review is independent of remote publication.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - METPO:1000441
checks:
- check_id: new-base-qc
  name: Fresh B14 corpus QC
  status: passed
  required: true
  target_ids:
  - METPO:1000441
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
  - METPO:1000441
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
  - METPO:1000441
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
  - METPO:1000441
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
- check_id: temperature-optimum-very-low-validate
  name: Focused native validation
  status: passed
  required: true
  target_ids:
  - METPO:1000441
  command: just validate data/traits/environment/temperature_optimum_very_low.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Native record validation passed; scientific interpretation is assessed
    separately.
  evidence_ids:
  - check-temperature-optimum-very-low-validate
- check_id: temperature-optimum-very-low-strict
  name: Focused strict validation
  status: passed
  required: true
  target_ids:
  - METPO:1000441
  command: just validate-strict data/traits/environment/temperature_optimum_very_low.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: The actual validate-strict command passed.
  evidence_ids:
  - check-temperature-optimum-very-low-strict
- check_id: temperature-optimum-very-low-snippets-network
  name: Focused network snippet check
  status: passed
  required: true
  target_ids:
  - METPO:1000441
  command: just verify-snippets --record data/traits/environment/temperature_optimum_very_low.yaml
    --out /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-snippets.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 'The native command completed successfully: 17 fields across six references,
    2 VERIFIED, 6 NOT_IN_ABSTRACT and 9 UNRESOLVED. Misses and unresolved responses
    remain inconclusive. The separate manual audit found 14 literal spans and three
    bounded nonverbatim spans; it does not relabel the native results.'
  evidence_ids:
  - check-temperature-optimum-very-low-snippets-network
- check_id: native-inspect
  name: One-target native review capture
  status: passed
  required: true
  target_ids:
  - METPO:1000441
  command: uv run python scripts/record_review.py inspect --targets /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low.targets.json
    --input .claude/skills/curate-yaml-record/references/review-checklist.md --input
    .claude/skills/manage-identifiers/SKILL.md --input .claude/skills/review-yaml-record/SKILL.md
    --input CLAUDE.md --input DO_NOT_WORK.md --input conf/evidence_snippet_baseline.tsv
    --input conf/record_review.yaml --input data/raw/biolink-model.yaml --input data/raw/metpo.owl
    --input data/traits/environment/temperature_optimum.yaml --input docs/CURATION_PLAYBOOK.md
    --input docs/GROUNDING_POLICY.md --input docs/PATHWAY_LINKS.md --input docs/record-review-profile.md
    --input docs/record-reviews.md --input history/infrastructure/curate-knowledge-gaps/2026-08-17T214933Z-claude-code-9c4af0.yaml
    --input history/infrastructure/node-type-consistency/2026-08-15T014631Z-claude-code-9d7f4d.yaml
    --input history/infrastructure/pr664-adversarial-review/2026-09-07T010000Z-codex-60bca2.yaml
    --input history/infrastructure/protein-vs-activity/2026-08-15T202806Z-claude-code-ddcd62.yaml
    --input history/other/canonical-examples-batch1/2026-08-20T074839Z-claude-code-6fb2f5.yaml
    --input history/other/canonical-examples-six/2026-08-21T065406Z-codex-a1ab82.yaml
    --input history/other/free-living-trehalose-external-research/2026-08-31T203047Z-claude-code-47e2e8.yaml
    --input history/records/free_living/2026-08-31T204506Z-claude-code-ca81b1.yaml
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
    --input proposals/metpo_traitmech_v2/metpo_proposal_properties_robot.tsv --input
    proposals/metpo_traitmech_v2/proposal.md --input proposals/metpo_traitmech_v4/metpo_proposal_properties_robot.tsv
    --input proposals/metpo_traitmech_v4/proposal.md --input proposals/metpo_traitmech_v8/metpo_proposal_properties_robot.tsv
    --input proposals/metpo_traitmech_v8/proposal.md --input proposals/metpo_traitmech_v9/metpo_proposal_properties_robot.tsv
    --input proposals/metpo_traitmech_v9/proposal.md --input reports/metpo_2026_06_12_active_review.tsv
    --input reports/metpo_2026_06_12_release_delta.tsv --input reports/ontology_snapshot_manifest.tsv
    --input research/traits/environment/temperature_optimum_very_low-deep-research-falcon.md
    --input schema/record_review.yaml --input scripts/add_cold_shock_response_trait.py
    --input scripts/add_homeoviscous_adaptation_trait.py --input scripts/add_palmelloid_formation_trait.py
    --input scripts/audit_causal_graphs.py --input scripts/audit_graph_protein_taxa.py
    --input scripts/audit_predicate_domains.py --input scripts/audit_unapplied_groundings.py
    --input scripts/audit_uniprot_grounding.py --input scripts/backfill_canonical_examples_444.py
    --input scripts/connect_free_living_trehalose_osmotic.py --input scripts/connect_mesophilic_graph_183.py
    --input scripts/connect_temperature_delta_high_graph_183.py --input scripts/connect_temperature_delta_very_low_graph_183.py
    --input scripts/connect_temperature_optimum_high_graph_183.py --input scripts/connect_temperature_optimum_very_low_graph_183.py
    --input scripts/connect_temperature_range_mid3_graph_183.py --input scripts/connect_temperature_range_mid4_graph_183.py
    --input scripts/connect_temperature_range_very_low_graph_183.py --input scripts/curate_knowledge_gaps.py
    --input scripts/finalize_metpo_2026_06_12_review.py --input scripts/ground_causal_nodes.py
    --input scripts/ground_causal_predicates.py --input scripts/migrate_disposition_typing.py
    --input scripts/migrate_enables_range_edges.py --input scripts/migrate_enables_trait_edges.py
    --input scripts/migrate_metpo_2026_06_12.py --input scripts/migrate_microbe_domain_edges.py
    --input scripts/migrate_name_match_groundings.py --input scripts/migrate_node_type_consistency.py
    --input scripts/migrate_pathway_vs_process.py --input scripts/migrate_process_quality_consistency.py
    --input scripts/migrate_protein_vs_activity.py --input scripts/migrate_remaining_microbe_domain_edges.py
    --input scripts/migrate_uniprot_instance_groundings.py --input scripts/normalize_homeoviscous_nodes.py
    --input scripts/record_review.py --input scripts/repair_pr664_adversarial_review.py
    --input scripts/review_mesophilic_graph_183.py --input scripts/review_nacl_delta_graph_183.py
    --input scripts/review_obligately_piezophilic_graph_183.py --input scripts/review_temperature_delta_high_graph_183.py
    --input scripts/review_temperature_delta_very_low_graph_183.py --input scripts/review_temperature_optimum_high_graph_183.py
    --input scripts/review_temperature_optimum_very_low_graph_183.py --input scripts/review_temperature_range_mid3_graph_183.py
    --input scripts/review_temperature_range_mid4_graph_183.py --input scripts/review_temperature_range_very_low_graph_183.py
    --input scripts/seed_from_metpo.py --input scripts/verify_metpo_proposal.py --input
    src/traitmech/schema/mech_shared.yaml --input src/traitmech/schema/traitmech.yaml
    --input src/traitmech/validation/write_validated.py
  exit_code: 0
  expected_exit_code: 0
  summary: One current target, 103 captured inputs, exact current base and successful
    native inspect.
  evidence_ids:
  - capture
- check_id: uniprot-applicability
  name: Protein-instance metadata applicability
  status: not_applicable
  required: false
  target_ids:
  - METPO:1000441
  summary: Two reviewed label-only protein classes and no instances; no fabricated
    accession required.
  evidence_ids:
  - record
  - policy
  - expression
- check_id: expression-adapter-availability
  name: Structured source-organism expression query availability
  status: unavailable
  required: false
  target_ids:
  - METPO:1000441
  summary: The maintained adapter is unavailable within current bounded discovery.
    Retained catalog checks and primary identity/literal context provide no module
    or efficacy result.
  evidence_ids:
  - expression
  - expression-discovery
  - source-reading
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
- evidence_id: check-temperature-optimum-very-low-validate
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-validate.log
  locator: Executed 2026-10-22T02:03:36.851813+00:00 through 2026-10-22T02:03:37.774545+00:00;
    metadata temperature-optimum-very-low-validate.json
  accessed_at: '2026-10-22T02:03:37.774545Z'
  support: context_only
  summary: Native record validation passed; scientific interpretation is assessed
    separately.
  snapshot_sha256: 3a02993513d77aea4b54832b92e5098be157556497c42c16ea96502923cf2d14
- evidence_id: check-temperature-optimum-very-low-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-strict.log
  locator: Executed 2026-10-22T02:03:36.851958+00:00 through 2026-10-22T02:03:38.297943+00:00;
    metadata temperature-optimum-very-low-strict.json
  accessed_at: '2026-10-22T02:03:38.297943Z'
  support: context_only
  summary: The actual validate-strict command passed.
  snapshot_sha256: 7388c36d35b268c6c114ab59e7139a318befc2e91d7ac0923de875fc847cdedf
- evidence_id: check-temperature-optimum-very-low-snippets-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-snippets-network.log
  locator: Executed 2026-10-22T02:03:46.986231+00:00 through 2026-10-22T02:04:00.891440+00:00;
    metadata temperature-optimum-very-low-snippets-network.json
  accessed_at: '2026-10-22T02:04:00.891440Z'
  support: context_only
  summary: 'The native command completed successfully: 17 fields across six references,
    2 VERIFIED, 6 NOT_IN_ABSTRACT and 9 UNRESOLVED. Misses and unresolved responses
    remain inconclusive. The separate manual audit found 14 literal spans and three
    bounded nonverbatim spans; it does not relabel the native results.'
  snapshot_sha256: ec7faac40519b929e96d9d0dc90f049d8bff364352e6855e025567967d17aeff
- evidence_id: capture
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low.inspect.json
  locator: Actual successful native inspect with 103 captured inputs
  accessed_at: '2026-10-22T02:03:17.914605Z'
  support: context_only
  summary: All current source hashes and the exact target are bound before serialization.
  snapshot_sha256: 2a70e7fb92c874cc27b71e008a31121530524a9c604bc7a0ce4459cec5d08a61
- evidence_id: record
  kind: record_content
  reference: data/traits/environment/temperature_optimum_very_low.yaml
  locator: Whole current record
  accessed_at: '2026-10-22T02:03:17.914605Z'
  support: supports
  summary: Sixteen nodes, fifteen edges, seventeen embedded events, one canonical
    example, two reviewed label-only protein classes and no instances.
  snapshot_sha256: 1248a6be1eec6a1c5b4fcaec1102617f04fdf4db70d017bd2f35daeaadc515fa
- evidence_id: local-init
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/batch014-local-initialization-receipt.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T01:07:39.713898Z'
  support: context_only
  summary: Actual local initialization and fifth queue target; publication remains
    separate.
  snapshot_sha256: 3dade2205affd0bd7eea4b7d5018e8c97080db55bba3620e89cf4a4da4123fa3
- evidence_id: policy
  kind: authority
  reference: docs/GROUNDING_POLICY.md
  locator: Captured maintained authority
  accessed_at: '2026-10-22T02:08:16.465783Z'
  support: supports
  summary: Protein family/function grounding and optional protein instances.
  snapshot_sha256: 891678c983c2283a47c81c47950b35753981e9339d105f3bbdda92a1f5ab7f42
- evidence_id: playbook
  kind: authority
  reference: docs/CURATION_PLAYBOOK.md
  locator: Captured maintained authority
  accessed_at: '2026-10-22T02:08:16.465783Z'
  support: supports
  summary: Literal source scope and attributable acceptance.
  snapshot_sha256: 735e9b810471da9f7d8364e35ffe1e741edb3421480dac01727db6ea5aa65da9
- evidence_id: schema
  kind: authority
  reference: src/traitmech/schema/traitmech.yaml
  locator: Captured maintained authority
  accessed_at: '2026-10-22T02:08:16.465783Z'
  support: supports
  summary: Current facets, material referents and NONMECHANISTIC scope.
  snapshot_sha256: 46c47fc627b80ccbba1e8ab3fb6f2aee93bc2aef7aaf72fe9aadc3257f2c02dd
- evidence_id: predicate-mapping
  kind: authority
  reference: mappings/predicate_grounding.tsv
  locator: Captured maintained authority
  accessed_at: '2026-10-22T02:08:16.465783Z'
  support: supports
  summary: Conditional increases/contributes-to mappings populate empty IDs; current
    populated assertions are skipped.
  snapshot_sha256: 8e28c19e93aca3dc164a3befbe2612b289241de457c59f499e65936c03b7ce52
- evidence_id: identity
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-ground-agent/identity-assessment.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:07:24.120691Z'
  support: context_only
  summary: Active exact bin, direct parent, environmental/chemical identities and
    official species identity; no numerical phenotype inference.
  snapshot_sha256: d4be3d1c5bfb188db93c326c1ba845d583f3cdeb3d40adfdd3450671b20f4760
- evidence_id: nodes-edges
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-ground-agent/node-edge-grounding-ledger.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:07:24.120140Z'
  support: context_only
  summary: All sixteen node and fifteen edge judgments with endpoint-positive controls.
  snapshot_sha256: 492ecafdc288e73bf7aec2139da6db8e2590721691a16858e2ce4ada1467180a
- evidence_id: ground-assessment
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-ground-agent/documentary-assessment.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:08:16.465783Z'
  support: context_only
  summary: One grouped imported-role major and two bounded facet/provenance minors,
    without detailed efficacy assessment.
  snapshot_sha256: 0b712e67f1ba15ab926bbaacb774e8f1d32bbb8dfe9fc242bf24ed700e77327f
- evidence_id: owners
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-ground-agent/owner-provenance-assessment.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:07:24.121056Z'
  support: context_only
  summary: Exact review payload, connector source-preimage guard and current ADDED_EDGES
    consumer distinguished.
  snapshot_sha256: 90188c2edcf38275b6c6e6b87b2fff973bcddd34e01c80f8b2d9e3a4f3627bc1
- evidence_id: owner-primary
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-ground-agent/owner-primary-reading.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:06:16.913471Z'
  support: context_only
  summary: Actual maintained writer/migration windows and replay/no-op/skip qualifications.
  snapshot_sha256: b3c6a28080d3196023a9b0ea20dcc639b8f7f620582431e2a724ecb260a781f7
- evidence_id: human-search
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-ground-agent/search-and-provenance.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:03:47.054628Z'
  support: context_only
  summary: 185 ignored- and hidden-inclusive matching paths, 71 actual review target
    arrays, zero exact target.
  snapshot_sha256: 29ad2a7ddb2a67253480b5b23cbf9f35a64e0545debdc0e2f5186e0d589da2e9
- evidence_id: histories
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-ground-agent/history-reading-provenance.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:06:17.511751Z'
  support: context_only
  summary: Seven current whole histories plus ten qualified prior whole readings;
    seventeen current actor/target/event projections.
  snapshot_sha256: 67b17d0e2345ed9ad834d526cafb7f49a8b48003e34e062d2aed97212acf708d
- evidence_id: discovery
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-ground-agent/discovery-disposition.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:07:24.121786Z'
  support: context_only
  summary: Twenty-nine script leads; the uncaptured thermotaxis script is matching-line
    context, not a fully read current owner.
  snapshot_sha256: 5fe3cb080a165815695dfbda54a5eadbb7c12ef86900ac07c533cef740a69189
- evidence_id: expression
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-ground-agent/expression-and-readiness.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:08:16.465195Z'
  support: context_only
  summary: Bounded retained catalog and selected organism checks; no global expression
    absence or module result.
  snapshot_sha256: 3f10bc703595024c3984d2e94192bef54fa6860e356bece502ff7d4e61ef88e7
- evidence_id: expression-discovery
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-ground-agent/expression-runner-current-discovery.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:06:17.628178Z'
  support: context_only
  summary: Fresh bounded PATH/project/install-root adapter discovery, not a global
    absence claim.
  snapshot_sha256: 049b03ece2e9df05ae48845260a26872c0deb3c29394e8975fc3d93efe0cf197
- evidence_id: local-authority
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-ground-agent/local-authority-reading.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:06:17.505444Z'
  support: context_only
  summary: Actual local confers/selects-for, mappings, Biolink and schema windows.
  snapshot_sha256: cc0f7ebf160f20b8c31be018e50cb7a4efc8cfa79f0b16f5045b30c3d0acbff2
- evidence_id: ground-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-ground-agent/reading-scope-receipt.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:08:16.466028Z'
  support: context_only
  summary: Actual current and qualified prior reading scopes; documentary history
    does not adopt historical efficacy claims.
  snapshot_sha256: a5c9682c8368a0f82e96c4ba61bfc2c6bcc968620ec8169a6c096789b56d72f4
- evidence_id: ground-manifest
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-ground-agent/evidence-manifest.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:08:16.488140Z'
  support: context_only
  summary: All 31 frozen ground artifacts verified.
  snapshot_sha256: eb5be5f8691008974c0ec83854dbf30d1d76e2a04fb336c63e2d47872c237559
- evidence_id: metpo-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/repo/data/raw/metpo.owl
  locator: Selected current raw class and direct parent at the recorded reading time
  accessed_at: '2026-10-22T02:03:46.889890Z'
  support: supports
  summary: Active very-low optimum bin and direct parent are positive; exact biological
    calibration and sufficiency remain qualified.
  snapshot_sha256: 8b6f8fe0510a698579e532658c8ace05da2550093365df9ca83feb0741778415
- evidence_id: metpo-projection
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-ground-agent/metpo-authority.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:03:46.889890Z'
  support: context_only
  summary: Exact raw source hash and current selected class elements.
  snapshot_sha256: d3a4d4048a0cd914b559a03cb245be750ff02ae1620226bd89f41ba6c3ee78a6
- evidence_id: ro-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/ro.db
  locator: Exact adopted response with original query time and recorded database hash
  accessed_at: '2026-10-22T01:23:46.984705Z'
  support: supports
  summary: RO2213 requires process endpoints; RO2326 inherits material-to-process
    roles through 2216, 2500 and 2595. Explicit molecular activity endpoints remain
    process-compatible.
  snapshot_sha256: 849e616c29fecd0d4a6c6dee0dc0f6f117ace7167dbfa1e0f043dc84868f83cb
- evidence_id: ro-projection
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-ground-agent/selected-ro-primary-reading.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T01:23:46.984705Z'
  support: context_only
  summary: Exact retained response at its original query clock; root separately queried
    current authority.
  snapshot_sha256: 93d1a0d40c0fc8e2cdea4641698bc1a409ef2f83c770131bf59cfe1558a17135
- evidence_id: primary-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-ground-agent/primary-reuse-receipt.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:03:46.843869Z'
  support: context_only
  summary: Original RO query clock and current copying remain distinct.
  snapshot_sha256: bcb4d5e95ba92e2fc3dcec343254a122a7cb2aed5148300bd16a4bd33bb1697c
- evidence_id: envo-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/envo.db
  locator: Current selected read-only query against the previously hash-qualified
    cache
  accessed_at: '2026-10-22T02:04:06.961596Z'
  support: supports
  summary: Cold-environment identity is positive; no phenotype or tolerance transfer.
  snapshot_sha256: 858814472871c9167a687fedbff2c27d74b35dea6b6b6df0a96e01f08dc4c0f5
- evidence_id: envo-projection
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-ground-agent/envo-primary-reading.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:04:06.961596Z'
  support: context_only
  summary: Cold-environment identity is positive; no phenotype or tolerance transfer.
  snapshot_sha256: 83af8d78497e66acb4af5b2c0165fedde88a81060f965466ac438e5e4c5d4539
- evidence_id: chebi-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/chebi.db
  locator: Current selected read-only query against the previously hash-qualified
    cache
  accessed_at: '2026-10-22T02:04:06.964171Z'
  support: supports
  summary: Unsaturated fatty acid and lipid material referents are distinguished from
    quality and activity.
  snapshot_sha256: 26ad4890cdcf6ee357760d815dfee8f5ba81e0873e62cb379369b04205722b0f
- evidence_id: chebi-projection
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-ground-agent/chebi-primary-reading.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:04:06.964171Z'
  support: context_only
  summary: Unsaturated fatty acid and lipid material referents are distinguished from
    quality and activity.
  snapshot_sha256: c9865e1b17cf390468e51e8086302d327a97e6fa8f44a58cbaad68083a6c90da
- evidence_id: ontology-cache
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-ground-agent/ontology-cache-provenance.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:06:17.507703Z'
  support: context_only
  summary: Original selected database hash clocks and current selected query provenance;
    no fresh release or duplicate large-database hashing claim.
  snapshot_sha256: 16ce1ae0bd73971101974b920991a6de8d7aebae80699f8ffbcf5737856fc468
- evidence_id: definition-metadata
  kind: primary_source
  reference: DOI:10.1038/sj.embor.7400662
  locator: Retained indexed identity and bounded status fields
  accessed_at: '2026-10-21T10:00:01.461116Z'
  support: supports
  summary: Positive identity; source classification interpretation is separately bound
    to the author-repository PDF.
  snapshot_sha256: 24d64254a2baba7c573dff7ae523cc0e00d30e297c4f1fd7aa3a23c51a057059
- evidence_id: definition-pdf
  kind: primary_source
  reference: DOI:10.1038/sj.embor.7400662
  locator: Retained author-repository PDF, selected classification lines via separately
    derived raw text
  accessed_at: '2026-10-21T10:03:39.641646Z'
  support: supports
  summary: Broad near-freezing growth includes psychrotolerant usage; it is not automatically
    an optimum or at-most-10-degree statement.
  snapshot_sha256: 5a7678c6418efbcccf54d91c55eea1c08f2a4ed0ce0e07a6995d5903b9a0eb2e
- evidence_id: mendoza-metadata
  kind: primary_source
  reference: DOI:10.1146/annurev-micro-091313-103612
  locator: Indexed identity and supplied generic physical abstract spans
  accessed_at: '2026-10-21T10:00:02.042457Z'
  support: supports
  summary: Generic membrane physical context only; detailed efficacy and exact-bin
    sufficiency unassessed.
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
  locator: Retained indexed identity/status
  accessed_at: '2026-10-21T22:07:08.865512Z'
  support: supports
  summary: Positive article identity, not detailed cold-defense efficacy.
  snapshot_sha256: da5cffab81fe0e039c6fcec8f318b2715f5604eaf8722ea6f63f944178ed447b
- evidence_id: cold-body
  kind: primary_source
  reference: DOI:10.1007/s42770-023-01057-4
  locator: Retained HTML all-p paragraph 78, existing supplied literal spans only
  accessed_at: '2026-10-21T22:07:50.938485Z'
  support: supports
  summary: Literal occurrence positive; detailed antifreeze/cryoprotection efficacy
    remains UNASSESSED_SCOPE.
  snapshot_sha256: bb09a59c07f43ff0af177f89b624c8b5d4841e513ed0d478120954a016342889
- evidence_id: phadtare-metadata
  kind: primary_source
  reference: DOI:10.4161/rna.7.6.13482
  locator: Retained indexed identity/status
  accessed_at: '2026-10-21T11:41:58.419539Z'
  support: supports
  summary: Article identity positive; an abstract miss does not refute a supplied
    body span.
  snapshot_sha256: afa3b113a78e9df1f4d51a735b8ba6cdde582d022cc561d1428d4af8e1b523fa
- evidence_id: definition-extraction-text
  kind: primary_source
  reference: DOI:10.1038/sj.embor.7400662
  locator: Raw text lines 24–33 using newline splitting
  accessed_at: '2026-10-21T21:57:11.990598Z'
  support: partial
  summary: Selected broad classification interpretation; original PDF acquisition,
    prior extraction and current copy clocks are separate.
  snapshot_sha256: 71ef77b88e880420f533454926cac17498cbf8db380465139c888057115143e8
- evidence_id: definition-extraction
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/definition-derivation-receipt.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-21T21:57:11.990598Z'
  support: context_only
  summary: Actual extraction command and source/output hashes; extraction time is
    not original source acquisition.
  snapshot_sha256: 4bc68e1e7c942f28f8b2be82ef5b82e45461cdec22ed95828753130bc433d1ac
- evidence_id: hamdan-extraction-text
  kind: primary_source
  reference: DOI:10.17159/sajs.2018/20170254
  locator: Publisher PDF-derived text, mechanical search of supplied strings
  accessed_at: '2026-10-22T02:07:42.696017Z'
  support: partial
  summary: Three nonmatches after whitespace/casefold/dehyphenation checks; this is
    not whole-paper biological interpretation.
  snapshot_sha256: 8fc1b9412cfc25e4755c6fe06049d2b4f53ec07188aa9e55f0f3d86f4f896c63
- evidence_id: hamdan-extraction
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/hamdan-derivation-receipt.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:07:42.696017Z'
  support: context_only
  summary: Actual extraction command and source/output hashes; extraction time is
    not original source acquisition.
  snapshot_sha256: e07754668094a4941444a7a551fd1673890268ee70f77b5f2202a74f3fe430e6
- evidence_id: hamdan-crossref
  kind: primary_source
  reference: DOI:10.17159/sajs.2018/20170254
  locator: Fresh Crossref identity/status fields
  accessed_at: '2026-10-22T02:06:02.094568Z'
  support: supports
  summary: Positive identity after zero indexed hits; bounded notice fields only.
  snapshot_sha256: b4298c38e24faeeed6ae38a1ff3a67d03ef7edf62e322c57b0fdfd91d645c506
- evidence_id: hamdan-crossref-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/hamdan-crossref.json.access.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:06:02.094568Z'
  support: context_only
  summary: Actual current request interval and response hash; interpretation restricted
    to the declared reading scope.
  snapshot_sha256: 410fc97129477abfbb2c518703d711795ef7b0c43912d1696b928728d1d3f61e
- evidence_id: hamdan-html
  kind: primary_source
  reference: DOI:10.17159/sajs.2018/20170254
  locator: Retained HTML selected paragraphs 33/34/40/42/44 and supplied-string matching
  accessed_at: '2026-10-22T02:06:05.768928Z'
  support: partial
  summary: Three supplied spans are nonverbatim on this surface; incidental pathogen
    and detailed adaptation efficacy unassessed.
  snapshot_sha256: be49e23c3fc5800a4d66f659c99f281d4e53643c7ff5298b8bf43ce4e79949f3
- evidence_id: hamdan-html-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/hamdan.html.access.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:06:05.768928Z'
  support: context_only
  summary: Actual current request interval and response hash; interpretation restricted
    to the declared reading scope.
  snapshot_sha256: 40bfbac86b4b6e838acb16bc4fb3f9bae3ebe3d937899c382c54ff1c520cf37e
- evidence_id: hamdan-pdf
  kind: primary_source
  reference: DOI:10.17159/sajs.2018/20170254
  locator: Publisher PDF input to separately recorded extraction
  accessed_at: '2026-10-22T02:07:20.873516Z'
  support: partial
  summary: Additional surface for bounded literal checks only; no full-paper efficacy
    assessment.
  snapshot_sha256: c9b85343e2a730929469816b08cf087ae22f47b5e9fedde0a30d6e2afd83ea87
- evidence_id: hamdan-pdf-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/hamdan.pdf.access.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:07:20.873516Z'
  support: context_only
  summary: Actual current request interval and response hash; interpretation restricted
    to the declared reading scope.
  snapshot_sha256: e44de0894f34a19e911095a5f3247b17db0f072ac153fd4a984d46a93c53612c
- evidence_id: phadtare-html
  kind: primary_source
  reference: DOI:10.4161/rna.7.6.13482
  locator: Current retained HTML all-p paragraphs 11 and 23
  accessed_at: '2026-10-22T02:07:16.769656Z'
  support: supports
  summary: Existing supplied span literal in body; detailed RNA/chaperone efficacy
    remains unassessed.
  snapshot_sha256: efdca44128e6627ab666aae31634f3365dc11fae398a27b06062bbb4fefc0acf
- evidence_id: phadtare-html-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/phadtare.html.access.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:07:16.769656Z'
  support: context_only
  summary: Actual current request interval and response hash; interpretation restricted
    to the declared reading scope.
  snapshot_sha256: 2884fe778f57140783257b42ca59f241373a0dc968ac5b5c64040d6e95f662e9
- evidence_id: yang-metadata
  kind: primary_source
  reference: DOI:10.1128/AEM.01928-22
  locator: Fresh indexed identity and supplied existing literal abstract span
  accessed_at: '2026-10-22T02:05:33.257647Z'
  support: supports
  summary: Bacillus simplex H-b source context and literal occurrence only; no detailed
    intervention or efficacy assessment.
  snapshot_sha256: 1d858d0cfbe3cd7842374a0b6d7453e4fad6959494b59b775880f473ca5c2195
- evidence_id: yang-metadata-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/yang-metadata-access.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:05:33.257647Z'
  support: context_only
  summary: Actual current request interval and response hash; interpretation restricted
    to the declared reading scope.
  snapshot_sha256: 2ad4982f92c5d1986908d303a6faf48499af92fe8e3ae21a5924b35737afca8d
- evidence_id: canonical-metadata
  kind: primary_source
  reference: DOI:10.1016/j.bbalip.2013.02.004
  locator: Fresh indexed title/identity and bounded notice fields only
  accessed_at: '2026-10-22T02:05:32.923541Z'
  support: supports
  summary: Canonical article identity positive; numerical optimum, culture parameters
    and adaptation/optimization claims are UNASSESSED_SCOPE.
  snapshot_sha256: 9f35081f59b689b6b577f9fa11ff84bac7ba2cc25ba562cddfce84d512203212
- evidence_id: canonical-metadata-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/canonical-metadata-access.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:05:32.923541Z'
  support: context_only
  summary: Actual current request interval and response hash; interpretation restricted
    to the declared reading scope.
  snapshot_sha256: dacf919d924a63f159225e6999703ffe83b672a1933a3f6ace5d4422116ab17d
- evidence_id: hamdan-index-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/hamdan-metadata-access.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:05:32.903861Z'
  support: context_only
  summary: Successful request with zero indexed hits; Crossref/publisher identity
    is positive, so no missing-source finding.
  snapshot_sha256: 04cf34db7a7de7273d7d7865f083d35368ffa728eeac0e82f97c28f768e3f3db
- evidence_id: yang-body-failure
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/yang.xml.access.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:06:02.620486Z'
  support: context_only
  summary: Actual HTTP 500 request, no acquired XML body; indexed snippet occurrence
    remains positive and body absence is not inferred.
  snapshot_sha256: 55f61be6fa4dfd221261c92b264129d281f2eb7f8b120c466fca1245e79e81cd
- evidence_id: current-browser
  kind: primary_source
  reference: DOI:10.1038/sj.embor.7400662; DOI:10.1146/annurev-micro-091313-103612
  locator: Actual browser call 2026-10-22 02:03:52 UTC through 2026-10-22 02:03:53
    UTC; export 2026-10-22 02:03:57 UTC
  accessed_at: '2026-10-22T02:03:53Z'
  support: partial
  summary: EMBO access failure and Mendoza publisher generic context only. This is
    a tool response, not raw HTML; origin/cache-fetch clock unknown.
  snapshot_sha256: ef908819b2fdf38e2b2a72979336147780b6ca826610bc02125e958e5e48fb48
- evidence_id: browser-failure-copy
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/root-browser-failure-copy.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:09:24.733476Z'
  support: context_only
  summary: Retained earlier Hamdan browser failure, separate from successful current
    source-agent HTML/PDF access; no invented HTTP status.
  snapshot_sha256: 95148762a9e8b3a0ad292bd365378563b3656fbbaf4c99dc72d0f369ea6cc88a
- evidence_id: phadtare-prior-limits
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/phadtare-prior-access-limits.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:09:24.733112Z'
  support: context_only
  summary: Prior failed attempts remain historical; current successful HTML supports
    the bounded literal check.
  snapshot_sha256: 5396260adff79d008866d096045446a72fae096b32666128c54bc2f640c114af
- evidence_id: taxonomy
  kind: authority
  reference: NCBITaxon:132926
  locator: Fresh successful official taxonomy retry, scientific name and rank only
  accessed_at: '2026-10-22T02:04:25.623269Z'
  support: supports
  summary: Clostridium psychrophilum species identity positive; no numerical phenotype
    or cultivation transfer.
  snapshot_sha256: 245bd094ae1de7aaee89438775af8f35f40f78f3e169e0ea6d102f92383f32bf
- evidence_id: taxonomy-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-ground-agent/taxonomy-network-retry-access.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:04:25.623269Z'
  support: context_only
  summary: Actual successful request and response hash.
  snapshot_sha256: 5da31b4dccb36881557591a25a60cc44c9b58db2a6408a08b784bbee8c1d371b
- evidence_id: taxonomy-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-ground-agent/taxonomy-identity.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:06:17.508437Z'
  support: context_only
  summary: Species identity interpreted separately from canonical phenotype support.
  snapshot_sha256: e83a44d595820197a31d80921cdd2198404b90f27af9568751c97aab6794ce31
- evidence_id: taxonomy-initial-failure
  kind: validation
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=132926
  locator: Initial DNS-error bytes, not taxonomy XML
  accessed_at: '2026-10-22T02:04:06.969827Z'
  support: context_only
  summary: Retrieval failure followed by successful official retry; no native validation
    failure.
  snapshot_sha256: f125edb3a860dc3c8eea9876c66df767ebcbb44706ab0c1c508f7d8a4154de6d
- evidence_id: taxonomy-failure-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-ground-agent/taxonomy-access.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:04:06.969827Z'
  support: context_only
  summary: Initial failed request interval and error hash retained separately.
  snapshot_sha256: 6d134053a86e2e4c36b9e1d83db3b4990fee76f1f13a205df0ee1fe51c09bcb2
- evidence_id: sources
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/source-assessment.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:09:24.740638Z'
  support: context_only
  summary: Seven works; overall source scope remains unknown with two bounded source
    minor findings.
  snapshot_sha256: b938772377e4f8659a382e311e93130fc5ca4f7fecd7cd0c127a2bdec22d9e23
- evidence_id: source-identities
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/source-ledger.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:09:24.735317Z'
  support: context_only
  summary: All seven assigned identities and actual classification/source scopes;
    bounded original notice observations.
  snapshot_sha256: ebe0dc1c765af92cbe21d5485c6f861927b74c8be3bb4a31f84c596835b71b44
- evidence_id: source-status
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/source-status-ledger.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:09:24.740410Z'
  support: context_only
  summary: Response-scoped publication/notice observations, not an exhaustive current
    notice search.
  snapshot_sha256: dda194811445f3874a774f373cee362baa1afd5e1fa5f03da65330203b2fc0af
- evidence_id: placements
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/source-placement-ledger.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:09:24.738754Z'
  support: context_only
  summary: All nineteen external placements; nineteen grounding fields are separately
    accounted in source and ground node-edge ledgers.
  snapshot_sha256: 91ccf8e9dbe7afcce366c2549a47202fab8958875c359f80624e79e0d8943409
- evidence_id: snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/snippet-ledger.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:09:24.738497Z'
  support: context_only
  summary: 'Seventeen schema snippets: fourteen literal and three bounded nonverbatim
    spans; no separate adopted quoted-note spans.'
  snapshot_sha256: f45f6ba83541a951bd9e2d2f9efa9deb4af483163629c2f3c92098b9503d062a
- evidence_id: literal-check
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/literal-match-completion.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:07:42.710180Z'
  support: context_only
  summary: Mechanical occurrence checks across declared retained surfaces, without
    whole-paper efficacy claims.
  snapshot_sha256: abcc91a4338b8c4aee0eae87a44991eb61ca7ba8bd006d68888f94cd89b5455c
- evidence_id: notes
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/source-note-ledger.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:09:24.738867Z'
  support: context_only
  summary: Eighteen notes including canonical note; canonical locator uses plural
    notes in this ledger but actual field is singular note, as clarified by root.
  snapshot_sha256: 79a06d4882abc5425d5c49c93172670b0b5cecd4c09476c44c5f3b3f956465df
- evidence_id: source-nodes-edges
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/node-edge-source-ledger.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:09:24.739000Z'
  support: context_only
  summary: All sixteen nodes and fifteen edges with selected physical/literal support
    distinguished from excluded efficacy.
  snapshot_sha256: 1759e6fb7883cc2f34844d00864d7f8fd4a00fa01bef15c735fcc23170e63ea6
- evidence_id: canonical
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/canonical-assessment.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:09:24.739122Z'
  support: context_only
  summary: Article identity positive; canonical numerical phenotype, cultivation and
    optimization support unassessed.
  snapshot_sha256: 90f82db3e214978f638ca23d2010c1fd7207715d3df2ad34e4fdbc5b4e25d080
- evidence_id: source-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/primary-reading-scope.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:09:24.740501Z'
  support: context_only
  summary: Selected classification/physical/literal passages only; canonical title/identity
    and explicit mechanism exclusions.
  snapshot_sha256: 5591da2192360f6bba75fce1aae095a4781cb07319634d7651bb48d495a6fc76
- evidence_id: source-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/source-access-limits.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:09:24.740322Z'
  support: context_only
  summary: Actual successful/failed/unacquired surfaces, no inference that inaccessible
    bodies lack a claim.
  snapshot_sha256: 97f85fd1cf121b6f5a986f26fc23b329016cf6fda6494f2c4eff006755e47acf
- evidence_id: source-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/source-reuse-receipt.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:05:20.760564Z'
  support: context_only
  summary: Twelve exact copies; nested original acquisition, current copy and separate
    extraction/read clocks retained.
  snapshot_sha256: dde9e3594d39e405b44287466d15b3b0edce0e5abda40a49963e296c30128d5a
- evidence_id: source-native
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/native-context.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:09:24.740062Z'
  support: context_only
  summary: Native 2 VERIFIED/6 NOT_IN_ABSTRACT/9 UNRESOLVED versus separate manual
    14 literal/3 nonverbatim results.
  snapshot_sha256: e7292dec965f4e8cb40e115adc2c416bee782eca604269904fa03d151edd7b5f
- evidence_id: source-manifest
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-agent/evidence-manifest.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:09:24.740783Z'
  support: context_only
  summary: All 52 frozen source artifacts verified.
  snapshot_sha256: 61cfe7d9f985fec9d5854158ba6671ecde8f430a06f4dd60bafaf49db13e305a
- evidence_id: root-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-root/selected-primary-reading.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:07:09.947928Z'
  support: context_only
  summary: Root selected primary and authority reading; whole-target reading is not
    a whole-paper mechanism review.
  snapshot_sha256: 9f05b50288ad02e64e822c99f1b55d04a2c1af8888f6b336e09266d22d106fd1
- evidence_id: root-verification
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-source-root/root-current-verification.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:10:43.758934Z'
  support: context_only
  summary: Root current inputs/artifacts/71 target arrays verified; exact connector
    quote payload, consumer and singular canonical note clarified.
  snapshot_sha256: f85216205ed9012f0f3e06a49c5fd50ae21ba80aee43b8c1ef203aaaf7903b73
- evidence_id: adjudication
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-optimum-very-low-root-adjudication.json
  locator: Final root adjudication
  accessed_at: '2026-10-22T02:11:32.168132Z'
  support: supports
  summary: Exact one major and four minors, qualified owners and documentary actions;
    all unknown and unassessed scopes retained.
  snapshot_sha256: c00c752d0fe6985de4b74892c2d5e70167bd67338ca59b426448a5ad5aa86b3e
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: active bin, aliases and direct parent'
  outcome: supported
  target_ids:
  - METPO:1000441
  summary: Active METPO:1000441, quantitative bin and direct parent are positive.
    Broader source terminology remains distinguished from the exact optimum bin; no
    additional alias finding is inferred.
  evidence_ids:
  - identity
  - metpo-primary
  - source-identities
  - record
- assessment_id: definition
  area: quantity
  topic: 'Native checklist: growth versus optimum attribution'
  outcome: concern
  target_ids:
  - METPO:1000441
  summary: The selected D’Amico passage uses psychrophiles broadly for microorganisms
    growing near freezing, including psychrotolerant usage. Two notes convert growth
    into optimum or at-most-10-degree support. Preserve the literal span and independently
    supported ontology bin; exact calibration and whole-organism sufficiency remain
    unknown.
  evidence_ids:
  - sources
  - placements
  - notes
  - definition-pdf
  - definition-extraction-text
  - metpo-primary
- assessment_id: canonical
  area: quantity
  topic: 'Native checklist: canonical identity and unassessed numerical support'
  outcome: unknown
  target_ids:
  - METPO:1000441
  summary: Official Clostridium psychrophilum species and assigned article title/identity
    are positive. Numerical phenotype, cultivation parameters, adaptation and optimization
    support remain UNASSESSED_SCOPE; no canonical paper body or temperature-response
    table is claimed. The actual field is canonical_examples[0].note; the frozen source-note
    ledger plural is only a locator typo.
  evidence_ids:
  - canonical
  - canonical-metadata
  - taxonomy
  - taxonomy-reading
  - root-verification
- assessment_id: source-support
  area: evidence
  topic: 'Native checklist: seven works and nineteen placements'
  outcome: unknown
  target_ids:
  - METPO:1000441
  summary: All seven assigned identities are positive within their retained responses.
    Selected generic physical and literal support is distinct from exact-bin sufficiency.
    Detailed stress-defense, survival/fitness, cryoprotection, protein/RNA/enzyme
    enhancement, cultivation and intervention efficacy remain UNASSESSED_SCOPE. Access
    failures do not refute uninspected source content.
  evidence_ids:
  - sources
  - source-identities
  - source-status
  - placements
  - notes
  - source-reading
  - source-access
  - mendoza-metadata
  - yang-metadata
- assessment_id: quotations
  area: evidence
  topic: 'Native checklist: seventeen snippets and adjacent notes'
  outcome: concern
  target_ids:
  - METPO:1000441
  summary: Manual audit found fourteen literal spans and three Hamdan spans absent
    from retained HTML/PDF-derived text under the recorded normalizations. This is
    a bounded copied-span issue, not biological refutation or a claim about every
    publication version. Native results remain 2 VERIFIED, 6 NOT_IN_ABSTRACT and 9
    UNRESOLVED; body-supported manual checks do not relabel them.
  evidence_ids:
  - snippets
  - literal-check
  - source-native
  - hamdan-html
  - hamdan-pdf
  - hamdan-extraction-text
  - phadtare-html
  - root-verification
- assessment_id: nodes
  area: representation
  topic: 'Native checklist: all sixteen current referents'
  outcome: concern
  target_ids:
  - METPO:1000441
  summary: Node 3 names an enzyme/lipid ensemble while typed process; sustaining-function
    wording leaves an activity reading plausible, so clarify the referent without
    prescribing an enum. Environmental and chemical identities are positive, explicit
    molecular activity remains valid, and node 13 lowering can denote a process. Detailed
    biological efficacy is unassessed.
  evidence_ids:
  - nodes-edges
  - source-nodes-edges
  - envo-primary
  - chebi-primary
  - schema
  - adjudication
  details: "{\n  \"grounding\": [\n    {\n      \"index\": 0,\n      \"node\": {\n\
    \        \"node_id\": \"temperature_optimum_very_low_trait\",\n        \"label\"\
    : \"temperature optimum very low\",\n        \"node_type\": \"TRAIT\",\n     \
    \   \"grounding\": \"METPO:1000441\",\n        \"description\": \"Temperature\
    \ optimum at or below ~10 °C.\"\n      },\n      \"status\": \"supported\",\n\
    \      \"assessment\": \"Active exact METPO bin with maxInclusive10 Cel and direct\
    \ parent1000304; biological calibration and alias equivalence separate.\"\n  \
    \  },\n    {\n      \"index\": 1,\n      \"node\": {\n        \"node_id\": \"\
    temperature_optimum\",\n        \"label\": \"temperature optimum\",\n        \"\
    node_type\": \"TRAIT\",\n        \"grounding\": \"METPO:1000304\",\n        \"\
    description\": \"Ambient temperature supporting maximal growth.\"\n      },\n\
    \      \"status\": \"supported\",\n      \"assessment\": \"Active parent describes\
    \ best-growth ambient conditions, distinct from growth breadth.\"\n    },\n  \
    \  {\n      \"index\": 2,\n      \"node\": {\n        \"node_id\": \"cold_environment\"\
    ,\n        \"label\": \"cold environment\",\n        \"node_type\": \"ENVIRONMENTAL_FACTOR\"\
    ,\n        \"description\": \"Habitat ambient temperature near the freezing point\
    \ of water.\",\n        \"grounding\": \"ENVO:01000309\"\n      },\n      \"status\"\
    : \"supported\",\n      \"assessment\": \"Actual ENVO01000309 is cold environment,\
    \ lower than a local/global average; near-freezing description is a contextual\
    \ subset, not an exact universal definition.\"\n    },\n    {\n      \"index\"\
    : 3,\n      \"node\": {\n        \"node_id\": \"psychrophile_machinery\",\n  \
    \      \"label\": \"psychrophile cold-adapted machinery\",\n        \"node_type\"\
    : \"BIOLOGICAL_PROCESS\",\n        \"description\": \"Cold-active enzymes and\
    \ unsaturated-lipid membranes sustaining function at very low temperature.\"\n\
    \      },\n      \"status\": \"concern\",\n      \"assessment\": \"Label and description\
    \ name an ensemble of enzymes and lipid membranes, whereas BIOLOGICAL_PROCESS\
    \ indicates an activity. The sustaining-function wording leaves the intended process\
    \ reading plausible; bounded facet precision minor, no forced replacement enum.\"\
    \n    },\n    {\n      \"index\": 4,\n      \"node\": {\n        \"node_id\":\
    \ \"unsaturated_fatty_acids\",\n        \"label\": \"unsaturated fatty acids\"\
    ,\n        \"node_type\": \"CHEMICAL\",\n        \"description\": \"Unsaturated\
    \ acyl chains that lower membrane melting point.\",\n        \"grounding\": \"\
    CHEBI:27208\"\n      },\n      \"status\": \"supported\",\n      \"assessment\"\
    : \"Actual CHEBI27208 names unsaturated fatty acid including at least one C=C\
    \ or C≡C bond; plural material class is compatible.\"\n    },\n    {\n      \"\
    index\": 5,\n      \"node\": {\n        \"node_id\": \"membrane_fluidity\",\n\
    \        \"label\": \"membrane fluidity at low temperature\",\n        \"node_type\"\
    : \"QUALITY\",\n        \"description\": \"Maintained membrane fluidity sustaining\
    \ transport and function in the cold.\"\n      },\n      \"status\": \"supported\"\
    ,\n      \"assessment\": \"Membrane fluidity denotes a measurable physical quality;\
    \ maintained status does not turn the quality into its maintenance process.\"\n\
    \    },\n    {\n      \"index\": 6,\n      \"node\": {\n        \"node_id\": \"\
    fatty_acid_desaturase_activity\",\n        \"label\": \"fatty acid desaturase\
    \ activity\",\n        \"node_type\": \"MOLECULAR_FUNCTION\",\n        \"description\"\
    : \"Desaturase activity introducing double bonds into fatty acyl chains.\"\n \
    \     },\n      \"status\": \"supported\",\n      \"assessment\": \"Explicit desaturase\
    \ activity is MOLECULAR_FUNCTION; do not equate with its material enzyme.\"\n\
    \    },\n    {\n      \"index\": 7,\n      \"node\": {\n        \"node_id\": \"\
    cold_shock_proteins\",\n        \"label\": \"cold shock proteins / RNA chaperones\"\
    ,\n        \"node_type\": \"GENE_OR_PROTEIN\",\n        \"grounding_status\":\
    \ \"REVIEWED_LABEL_ONLY\",\n        \"grounding_notes\": \"Reviewed as a contextual\
    \ protein or protein-complex label within a quantitative measurement graph; no\
    \ exact semantic family term was established for this aggregate use.\",\n    \
    \    \"description\": \"RNA chaperones that resolve nucleic-acid secondary structure\
    \ stabilized in the cold.\"\n      },\n      \"status\": \"supported_with_scope_limit\"\
    ,\n      \"assessment\": \"Reviewed label-only protein/RNA-chaperone aggregate,\
    \ not RNA material or an asserted protein instance; detailed efficacy unassessed.\"\
    \n    },\n    {\n      \"index\": 8,\n      \"node\": {\n        \"node_id\":\
    \ \"translation_low_temperature\",\n        \"label\": \"translation at low temperature\"\
    ,\n        \"node_type\": \"BIOLOGICAL_PROCESS\",\n        \"description\": \"\
    Maintenance of transcription and translation under low-temperature conditions.\"\
    \n      },\n      \"status\": \"supported_with_scope_limit\",\n      \"assessment\"\
    : \"Explicit transcription/translation-maintenance activity is processual; exact\
    \ biological support unassessed.\"\n    },\n    {\n      \"index\": 9,\n     \
    \ \"node\": {\n        \"node_id\": \"protein_membrane_stabilization\",\n    \
    \    \"label\": \"protein and membrane stabilization under cold stress\",\n  \
    \      \"node_type\": \"BIOLOGICAL_PROCESS\",\n        \"description\": \"Prevention\
    \ of protein aggregation and stabilization of membranes during cold stress.\"\n\
    \      },\n      \"status\": \"supported_with_scope_limit\",\n      \"assessment\"\
    : \"Prevention/stabilization is processual wording; detailed cold-protection efficacy\
    \ unassessed.\"\n    },\n    {\n      \"index\": 10,\n      \"node\": {\n    \
    \    \"node_id\": \"trehalose\",\n        \"label\": \"trehalose\",\n        \"\
    node_type\": \"CHEMICAL\",\n        \"description\": \"Disaccharide compatible\
    \ solute acting as a cryoprotectant.\"\n      },\n      \"status\": \"supported_with_scope_limit\"\
    ,\n      \"assessment\": \"Trehalose is used as a chemical referent without populated\
    \ identifier; no fabricated grounding or efficacy inference.\"\n    },\n    {\n\
    \      \"index\": 11,\n      \"node\": {\n        \"node_id\": \"cryoprotection\"\
    ,\n        \"label\": \"cryoprotection\",\n        \"node_type\": \"BIOLOGICAL_PROCESS\"\
    ,\n        \"description\": \"Protection of cellular structures against freezing\
    \ and freeze-thaw damage.\"\n      },\n      \"status\": \"supported_with_scope_limit\"\
    ,\n      \"assessment\": \"Protection against freezing damage is explicit process\
    \ wording; detailed survival/cryoprotection efficacy unassessed.\"\n    },\n \
    \   {\n      \"index\": 12,\n      \"node\": {\n        \"node_id\": \"antifreeze_proteins\"\
    ,\n        \"label\": \"antifreeze / ice-binding proteins\",\n        \"node_type\"\
    : \"GENE_OR_PROTEIN\",\n        \"grounding_status\": \"REVIEWED_LABEL_ONLY\"\
    ,\n        \"grounding_notes\": \"Reviewed as a contextual protein or protein-complex\
    \ label within a quantitative measurement graph; no exact semantic family term\
    \ was established for this aggregate use.\",\n        \"description\": \"Ice-binding\
    \ proteins that depress freezing point via thermal hysteresis.\"\n      },\n \
    \     \"status\": \"supported_with_scope_limit\",\n      \"assessment\": \"Reviewed\
    \ label-only protein aggregate; no instance required by quantitative NONMECHANISTIC\
    \ scope.\"\n    },\n    {\n      \"index\": 13,\n      \"node\": {\n        \"\
    node_id\": \"thermal_hysteresis\",\n        \"label\": \"thermal hysteresis /\
    \ lowered freezing point\",\n        \"node_type\": \"BIOLOGICAL_PROCESS\",\n\
    \        \"description\": \"Lowering of the freezing point separating melting\
    \ and freezing temperatures.\"\n      },\n      \"status\": \"qualified\",\n \
    \     \"assessment\": \"Label names a physical separation/hysteresis effect, but\
    \ description explicitly describes lowering freezing point. Process reading is\
    \ plausible; no categorical retype or extra defect inferred from label alone.\"\
    \n    },\n    {\n      \"index\": 14,\n      \"node\": {\n        \"node_id\"\
    : \"enzyme_structural_flexibility\",\n        \"label\": \"increased enzyme structural\
    \ flexibility\",\n        \"node_type\": \"QUALITY\",\n        \"description\"\
    : \"Greater conformational flexibility of cold-adapted enzymes.\"\n      },\n\
    \      \"status\": \"supported\",\n      \"assessment\": \"Explicit structural/conformational\
    \ flexibility is a quality, distinct from the process exhibiting it.\"\n    },\n\
    \    {\n      \"index\": 15,\n      \"node\": {\n        \"node_id\": \"catalytic_activity_low_temperature\"\
    ,\n        \"label\": \"catalytic activity at low temperature\",\n        \"node_type\"\
    : \"MOLECULAR_FUNCTION\",\n        \"description\": \"Retention of catalytic efficiency\
    \ at low temperature.\"\n      },\n      \"status\": \"supported_with_scope_limit\"\
    ,\n      \"assessment\": \"Explicit catalytic activity is a molecular activity;\
    \ efficiency wording is a quantitative qualification, not automatic material-enzyme\
    \ interpretation.\"\n    }\n  ],\n  \"source\": [\n    {\n      \"index\": 0,\n\
    \      \"field\": \"causal_graphs[0].nodes[0]\",\n      \"node_id\": \"temperature_optimum_very_low_trait\"\
    ,\n      \"label\": \"temperature optimum very low\",\n      \"node_type\": \"\
    TRAIT\",\n      \"source_outcome\": \"unknown\",\n      \"assessment\": \"Exact\
    \ ≤10 optimum calibration and biological equivalence of the exact Psychrophile\
    \ alias are not established by the selected generic passage; maintained bin identity\
    \ is reviewed separately.\",\n      \"incident_edges\": [\n        1,\n      \
    \  2\n      ]\n    },\n    {\n      \"index\": 1,\n      \"field\": \"causal_graphs[0].nodes[1]\"\
    ,\n      \"node_id\": \"temperature_optimum\",\n      \"label\": \"temperature\
    \ optimum\",\n      \"node_type\": \"TRAIT\",\n      \"source_outcome\": \"qualified\"\
    ,\n      \"assessment\": \"A temperature optimum is distinct from growth range\
    \ or viability; no new source-only objection to the quantitative parent.\",\n\
    \      \"incident_edges\": [\n        2\n      ]\n    },\n    {\n      \"index\"\
    : 2,\n      \"field\": \"causal_graphs[0].nodes[2]\",\n      \"node_id\": \"cold_environment\"\
    ,\n      \"label\": \"cold environment\",\n      \"node_type\": \"ENVIRONMENTAL_FACTOR\"\
    ,\n      \"source_outcome\": \"supported\",\n      \"assessment\": \"The selected\
    \ D’Amico introduction describes near-freezing environments and growth; it is\
    \ broad context.\",\n      \"incident_edges\": [\n        0\n      ]\n    },\n\
    \    {\n      \"index\": 3,\n      \"field\": \"causal_graphs[0].nodes[3]\",\n\
    \      \"node_id\": \"psychrophile_machinery\",\n      \"label\": \"psychrophile\
    \ cold-adapted machinery\",\n      \"node_type\": \"BIOLOGICAL_PROCESS\",\n  \
    \    \"source_outcome\": \"unknown\",\n      \"assessment\": \"Aggregate physiological\
    \ machinery description does not itself establish an exclusive or sufficient quantitative\
    \ optimum; detailed mechanisms not assessed.\",\n      \"incident_edges\": [\n\
    \        0,\n        1,\n        9,\n        10,\n        13,\n        14\n  \
    \    ]\n    },\n    {\n      \"index\": 4,\n      \"field\": \"causal_graphs[0].nodes[4]\"\
    ,\n      \"node_id\": \"unsaturated_fatty_acids\",\n      \"label\": \"unsaturated\
    \ fatty acids\",\n      \"node_type\": \"CHEMICAL\",\n      \"source_outcome\"\
    : \"qualified\",\n      \"assessment\": \"Existing unsaturated-fatty-acid terminology\
    \ and generic physical membrane context are supported; no bin-specific efficacy\
    \ inference.\",\n      \"incident_edges\": [\n        3,\n        4\n      ]\n\
    \    },\n    {\n      \"index\": 5,\n      \"field\": \"causal_graphs[0].nodes[5]\"\
    ,\n      \"node_id\": \"membrane_fluidity\",\n      \"label\": \"membrane fluidity\
    \ at low temperature\",\n      \"node_type\": \"QUALITY\",\n      \"source_outcome\"\
    : \"qualified\",\n      \"assessment\": \"Generic membrane-fluidity physical context\
    \ is supported without quantitative optimum inference.\",\n      \"incident_edges\"\
    : [\n        4,\n        14\n      ]\n    },\n    {\n      \"index\": 6,\n   \
    \   \"field\": \"causal_graphs[0].nodes[6]\",\n      \"node_id\": \"fatty_acid_desaturase_activity\"\
    ,\n      \"label\": \"fatty acid desaturase activity\",\n      \"node_type\":\
    \ \"MOLECULAR_FUNCTION\",\n      \"source_outcome\": \"UNASSESSED_SCOPE\",\n \
    \     \"assessment\": \"Detailed cold-responsive enzyme regulation/efficacy not\
    \ assessed.\",\n      \"incident_edges\": [\n        3\n      ]\n    },\n    {\n\
    \      \"index\": 7,\n      \"field\": \"causal_graphs[0].nodes[7]\",\n      \"\
    node_id\": \"cold_shock_proteins\",\n      \"label\": \"cold shock proteins /\
    \ RNA chaperones\",\n      \"node_type\": \"GENE_OR_PROTEIN\",\n      \"source_outcome\"\
    : \"UNASSESSED_SCOPE\",\n      \"assessment\": \"Protein-class naming/literal\
    \ evidence only; detailed cold-survival mechanism unassessed.\",\n      \"incident_edges\"\
    : [\n        5\n      ]\n    },\n    {\n      \"index\": 8,\n      \"field\":\
    \ \"causal_graphs[0].nodes[8]\",\n      \"node_id\": \"translation_low_temperature\"\
    ,\n      \"label\": \"translation at low temperature\",\n      \"node_type\":\
    \ \"BIOLOGICAL_PROCESS\",\n      \"source_outcome\": \"UNASSESSED_SCOPE\",\n \
    \     \"assessment\": \"Existing short literal support only; detailed translation/cold-survival\
    \ physiology unassessed.\",\n      \"incident_edges\": [\n        5,\n       \
    \ 9\n      ]\n    },\n    {\n      \"index\": 9,\n      \"field\": \"causal_graphs[0].nodes[9]\"\
    ,\n      \"node_id\": \"protein_membrane_stabilization\",\n      \"label\": \"\
    protein and membrane stabilization under cold stress\",\n      \"node_type\":\
    \ \"BIOLOGICAL_PROCESS\",\n      \"source_outcome\": \"UNASSESSED_SCOPE\",\n \
    \     \"assessment\": \"Stabilization efficacy unassessed; related copied-span\
    \ discrepancy separately identified.\",\n      \"incident_edges\": [\n       \
    \ 10,\n        11\n      ]\n    },\n    {\n      \"index\": 10,\n      \"field\"\
    : \"causal_graphs[0].nodes[10]\",\n      \"node_id\": \"trehalose\",\n      \"\
    label\": \"trehalose\",\n      \"node_type\": \"CHEMICAL\",\n      \"source_outcome\"\
    : \"UNASSESSED_SCOPE\",\n      \"assessment\": \"Existing chemical naming/literal\
    \ statement only; detailed protective efficacy unassessed.\",\n      \"incident_edges\"\
    : [\n        6\n      ]\n    },\n    {\n      \"index\": 11,\n      \"field\"\
    : \"causal_graphs[0].nodes[11]\",\n      \"node_id\": \"cryoprotection\",\n  \
    \    \"label\": \"cryoprotection\",\n      \"node_type\": \"BIOLOGICAL_PROCESS\"\
    ,\n      \"source_outcome\": \"UNASSESSED_SCOPE\",\n      \"assessment\": \"Cryoprotective\
    \ efficacy not assessed or repaired.\",\n      \"incident_edges\": [\n       \
    \ 6,\n        11,\n        12\n      ]\n    },\n    {\n      \"index\": 12,\n\
    \      \"field\": \"causal_graphs[0].nodes[12]\",\n      \"node_id\": \"antifreeze_proteins\"\
    ,\n      \"label\": \"antifreeze / ice-binding proteins\",\n      \"node_type\"\
    : \"GENE_OR_PROTEIN\",\n      \"source_outcome\": \"UNASSESSED_SCOPE\",\n    \
    \  \"assessment\": \"Protein-class naming/literal evidence only; no mechanism\
    \ or enhancement assessment.\",\n      \"incident_edges\": [\n        7\n    \
    \  ]\n    },\n    {\n      \"index\": 13,\n      \"field\": \"causal_graphs[0].nodes[13]\"\
    ,\n      \"node_id\": \"thermal_hysteresis\",\n      \"label\": \"thermal hysteresis\
    \ / lowered freezing point\",\n      \"node_type\": \"BIOLOGICAL_PROCESS\",\n\
    \      \"source_outcome\": \"UNASSESSED_SCOPE\",\n      \"assessment\": \"Existing\
    \ Ramón quotation literal; biological efficacy not adjudicated.\",\n      \"incident_edges\"\
    : [\n        7,\n        12\n      ]\n    },\n    {\n      \"index\": 14,\n  \
    \    \"field\": \"causal_graphs[0].nodes[14]\",\n      \"node_id\": \"enzyme_structural_flexibility\"\
    ,\n      \"label\": \"increased enzyme structural flexibility\",\n      \"node_type\"\
    : \"QUALITY\",\n      \"source_outcome\": \"UNASSESSED_SCOPE\",\n      \"assessment\"\
    : \"No enzyme engineering/flexibility enhancement assessment.\",\n      \"incident_edges\"\
    : [\n        8\n      ]\n    },\n    {\n      \"index\": 15,\n      \"field\"\
    : \"causal_graphs[0].nodes[15]\",\n      \"node_id\": \"catalytic_activity_low_temperature\"\
    ,\n      \"label\": \"catalytic activity at low temperature\",\n      \"node_type\"\
    : \"MOLECULAR_FUNCTION\",\n      \"source_outcome\": \"UNASSESSED_SCOPE\",\n \
    \     \"assessment\": \"No catalytic enhancement assessment; current copied-span\
    \ issue is documentary only.\",\n      \"incident_edges\": [\n        8,\n   \
    \     13\n      ]\n    }\n  ]\n}"
- assessment_id: relations
  area: consistency
  topic: 'Native checklist: all fifteen current relations'
  outcome: concern
  target_ids:
  - METPO:1000441
  summary: RO2213 edge 3 targets chemical material and edge 8 starts from a structural-flexibility
    quality, contrary to process roles. RO2326 edge 4 targets fluidity quality rather
    than process. Explicit molecular activities are not rejected by type alone. Edges
    5/6 have compatible material/process endpoints; local and Biolink broad roles
    and subclass support remain positive without certifying efficacy.
  evidence_ids:
  - nodes-edges
  - source-nodes-edges
  - ro-primary
  - local-authority
  - adjudication
  details: "{\n  \"grounding\": [\n    {\n      \"index\": 0,\n      \"edge\": {\n\
    \        \"subject\": \"cold_environment\",\n        \"predicate\": \"selects\
    \ for\",\n        \"object\": \"psychrophile_machinery\",\n        \"description\"\
    : \"Cold environments select for cold-adapted enzymes and lipids.\",\n       \
    \ \"evidence\": [\n          {\n            \"reference\": \"DOI:10.1038/sj.embor.7400662\"\
    ,\n            \"snippet\": \"growing well at temperatures around the freezing\
    \ point of water\",\n            \"notes\": \"Supports cold habitats as the context\
    \ for psychrophile machinery.\"\n          }\n        ],\n        \"predicate_id\"\
    : \"METPO:2007401\"\n      },\n      \"status\": \"qualified\",\n      \"assessment\"\
    : \"Local v2 selects-for has broad scaffold endpoints, with environmental-condition/adapted-trait\
    \ prose. Cold environment is compatible; machinery facet and exact biological\
    \ selection/bin inference remain qualified, not an invented hard domain violation.\"\
    \n    },\n    {\n      \"index\": 1,\n      \"edge\": {\n        \"subject\":\
    \ \"psychrophile_machinery\",\n        \"predicate\": \"confers\",\n        \"\
    object\": \"temperature_optimum_very_low_trait\",\n        \"description\": \"\
    Psychrophile cold-adapted machinery yields a very-low temperature optimum.\",\n\
    \        \"evidence\": [\n          {\n            \"reference\": \"DOI:10.1146/annurev-micro-091313-103612\"\
    ,\n            \"snippet\": \"more unsaturated fatty acids\",\n            \"\
    notes\": \"Supports homoviscous adaptation as the mechanism setting the psychrophile\
    \ optimum.\"\n          }\n        ],\n        \"predicate_id\": \"METPO:2007700\"\
    \n      },\n      \"status\": \"qualified\",\n      \"assessment\": \"Local v8\
    \ confers permits broad subject classes and TRAIT object. Formal endpoints fit;\
    \ machinery precision and exact whole-organism setpoint causal bridge remain separate/unknown.\"\
    \n    },\n    {\n      \"index\": 2,\n      \"edge\": {\n        \"subject\":\
    \ \"temperature_optimum_very_low_trait\",\n        \"predicate\": \"is a\",\n\
    \        \"object\": \"temperature_optimum\",\n        \"description\": \"Temperature\
    \ optimum very low is a quantitative bin of the temperature-optimum phenotype.\"\
    ,\n        \"evidence\": [\n          {\n            \"reference\": \"DOI:10.1038/sj.embor.7400662\"\
    ,\n            \"snippet\": \"growing well at temperatures around the freezing\
    \ point of water\",\n            \"notes\": \"Supports a ≤10 °C optimum as a value\
    \ within the temperature-optimum distribution.\"\n          }\n        ],\n  \
    \      \"predicate_id\": \"rdfs:subClassOf\"\n      },\n      \"status\": \"supported\"\
    ,\n      \"assessment\": \"Current bin-to-parent rdfs:subClassOf agrees with raw\
    \ active METPO hierarchy.\"\n    },\n    {\n      \"index\": 3,\n      \"edge\"\
    : {\n        \"subject\": \"fatty_acid_desaturase_activity\",\n        \"predicate\"\
    : \"increases\",\n        \"object\": \"unsaturated_fatty_acids\",\n        \"\
    description\": \"Fatty acid desaturase activity increases unsaturated acyl chains.\"\
    ,\n        \"evidence\": [\n          {\n            \"reference\": \"DOI:10.17159/sajs.2018/20170254\"\
    ,\n            \"snippet\": \"increase in the proportion of unsaturated acyl chains\"\
    ,\n            \"notes\": \"Verified against the open Hamdan review; lower growth\
    \ temperatures are described as activating desaturases that convert saturated\
    \ acyl fatty acids to unsaturated ones.\"\n          }\n        ],\n        \"\
    predicate_id\": \"RO:0002213\"\n      },\n      \"status\": \"concern\",\n   \
    \   \"assessment\": \"RO2213 inherits RO2211 process/process roles. Explicit activity\
    \ subject can be processual, but material unsaturated-fatty-acid object is not\
    \ an execution/process. Firm imported-role defect.\"\n    },\n    {\n      \"\
    index\": 4,\n      \"edge\": {\n        \"subject\": \"unsaturated_fatty_acids\"\
    ,\n        \"predicate\": \"contributes to\",\n        \"object\": \"membrane_fluidity\"\
    ,\n        \"description\": \"Increased unsaturated fatty acids contribute to\
    \ membrane fluidity at low temperature.\",\n        \"evidence\": [\n        \
    \  {\n            \"reference\": \"DOI:10.1128/AEM.01928-22\",\n            \"\
    snippet\": \"proportion of unsaturated fatty acids was higher\",\n           \
    \ \"notes\": \"Verified against the open Yang et al. abstract; Bacillus simplex\
    \ H-b cultured at low temperature carried a higher unsaturated-fatty-acid proportion.\"\
    \n          },\n          {\n            \"reference\": \"DOI:10.17159/sajs.2018/20170254\"\
    ,\n            \"snippet\": \"maintain optimum membrane fluidity\",\n        \
    \    \"notes\": \"Verified against the open Hamdan review; fatty-acyl-chain modifications\
    \ are described as preserving membrane fluidity in freezing environments.\"\n\
    \          }\n        ],\n        \"predicate_id\": \"RO:0002326\"\n      },\n\
    \      \"status\": \"concern\",\n      \"assessment\": \"RO2326 inherits material/process\
    \ roles via2216→2500→2595. Material fatty acids fit the subject; explicit membrane-fluidity\
    \ QUALITY fails the process range.\"\n    },\n    {\n      \"index\": 5,\n   \
    \   \"edge\": {\n        \"subject\": \"cold_shock_proteins\",\n        \"predicate\"\
    : \"contributes to\",\n        \"object\": \"translation_low_temperature\",\n\
    \        \"description\": \"Cold shock proteins / RNA chaperones contribute to\
    \ transcription and translation in the cold.\",\n        \"evidence\": [\n   \
    \       {\n            \"reference\": \"DOI:10.17159/sajs.2018/20170254\",\n \
    \           \"snippet\": \"regulation of cellular protein synthesis\",\n     \
    \       \"notes\": \"Verified against the open Hamdan review; cold-shock proteins\
    \ are linked to cellular protein-synthesis regulation, including transcription\
    \ and translation initiation.\"\n          }\n        ],\n        \"predicate_id\"\
    : \"RO:0002326\"\n      },\n      \"status\": \"supported_with_scope_limit\",\n\
    \      \"assessment\": \"Material protein aggregate to explicit translation process\
    \ fits RO2326 endpoints. Actual contributing execution/efficacy is not validated\
    \ here.\"\n    },\n    {\n      \"index\": 6,\n      \"edge\": {\n        \"subject\"\
    : \"trehalose\",\n        \"predicate\": \"contributes to\",\n        \"object\"\
    : \"cryoprotection\",\n        \"description\": \"Trehalose contributes to cryoprotection.\"\
    ,\n        \"evidence\": [\n          {\n            \"reference\": \"DOI:10.17159/sajs.2018/20170254\"\
    ,\n            \"snippet\": \"preventing protein denaturation and aggregation\"\
    ,\n            \"notes\": \"Verified against the open Hamdan review; trehalose\
    \ is reported as preventing protein denaturation and aggregation in psychrophilic\
    \ bacteria.\"\n          }\n        ],\n        \"predicate_id\": \"RO:0002326\"\
    \n      },\n      \"status\": \"supported_with_scope_limit\",\n      \"assessment\"\
    : \"Chemical material to explicit protection process fits RO2326 endpoints. No\
    \ blanket protein-only constraint; detailed role/cryoprotection efficacy unassessed.\"\
    \n    },\n    {\n      \"index\": 7,\n      \"edge\": {\n        \"subject\":\
    \ \"antifreeze_proteins\",\n        \"predicate\": \"causes\",\n        \"object\"\
    : \"thermal_hysteresis\",\n        \"description\": \"Antifreeze proteins lower\
    \ the freezing point via thermal hysteresis.\",\n        \"evidence\": [\n   \
    \       {\n            \"reference\": \"DOI:10.1007/s42770-023-01057-4\",\n  \
    \          \"snippet\": \"lower the water freezing point\",\n            \"notes\"\
    : \"Verified against the open Ramón et al. abstract and review text; anti-freeze\
    \ proteins are described as lowering the water freezing point via thermal hysteresis\
    \ or ice-recrystallization inhibition.\"\n          }\n        ],\n        \"\
    predicate_id\": \"biolink:causes\"\n      },\n      \"status\": \"qualified\"\
    ,\n      \"assessment\": \"Actual Biolink causes inherits broad NamedThing endpoints;\
    \ material protein to described lowering process is not an imported RO failure.\
    \ Thermal-hysteresis facet and detailed efficacy remain qualified.\"\n    },\n\
    \    {\n      \"index\": 8,\n      \"edge\": {\n        \"subject\": \"enzyme_structural_flexibility\"\
    ,\n        \"predicate\": \"increases\",\n        \"object\": \"catalytic_activity_low_temperature\"\
    ,\n        \"description\": \"Increased enzyme structural flexibility increases\
    \ catalytic activity at low temperature.\",\n        \"evidence\": [\n       \
    \   {\n            \"reference\": \"DOI:10.17159/sajs.2018/20170254\",\n     \
    \       \"snippet\": \"up to 10-fold higher specific activity\",\n           \
    \ \"notes\": \"Verified against the open Hamdan review; psychrophiles are described\
    \ as producing structurally flexible enzymes with higher low-temperature specific\
    \ activity than mesophilic homologues.\"\n          }\n        ],\n        \"\
    predicate_id\": \"RO:0002213\"\n      },\n      \"status\": \"concern\",\n   \
    \   \"assessment\": \"RO2213 process-domain conflicts with explicit structural\
    \ flexibility QUALITY. Catalytic activity can be processual; no automatic MF-object\
    \ rejection.\"\n    },\n    {\n      \"index\": 9,\n      \"edge\": {\n      \
    \  \"subject\": \"translation_low_temperature\",\n        \"predicate\": \"associated\
    \ with\",\n        \"object\": \"psychrophile_machinery\",\n        \"description\"\
    : \"Cold-shock protein support for translation is associated with psychrophile\
    \ cold-adapted machinery.\",\n        \"evidence\": [\n          {\n         \
    \   \"reference\": \"DOI:10.4161/rna.7.6.13482\",\n            \"snippet\": \"\
    facilitating transcription and translation at low temperature\",\n           \
    \ \"notes\": \"Verified against the open Phadtare and Severinov PubMed abstract;\
    \ this connector keeps cold-shock RNA chaperones as protein-synthesis context\
    \ for psychrophile physiology.\"\n          }\n        ],\n        \"predicate_id\"\
    : \"biolink:associated_with\"\n      },\n      \"status\": \"qualified\",\n  \
    \    \"assessment\": \"Biolink associated_with has broad named-thing endpoints;\
    \ process-to-machinery association formally admitted. Machinery facet and efficacy\
    \ remain separate.\"\n    },\n    {\n      \"index\": 10,\n      \"edge\": {\n\
    \        \"subject\": \"protein_membrane_stabilization\",\n        \"predicate\"\
    : \"associated with\",\n        \"object\": \"psychrophile_machinery\",\n    \
    \    \"description\": \"Compatible-solute protein and membrane stabilization is\
    \ associated with psychrophile cold-adapted machinery.\",\n        \"evidence\"\
    : [\n          {\n            \"reference\": \"DOI:10.17159/sajs.2018/20170254\"\
    ,\n            \"snippet\": \"compatible solutes such as trehalose and glycine-betaine\"\
    ,\n            \"notes\": \"Verified against the open Hamdan review; this connector\
    \ keeps glycine-betaine compatible-solute effects as broad cold-stress context.\"\
    \n          }\n        ],\n        \"predicate_id\": \"biolink:associated_with\"\
    \n      },\n      \"status\": \"qualified\",\n      \"assessment\": \"Biolink\
    \ associated_with broadly admits current process and machinery referents; no imported\
    \ process-only constraint.\"\n    },\n    {\n      \"index\": 11,\n      \"edge\"\
    : {\n        \"subject\": \"cryoprotection\",\n        \"predicate\": \"associated\
    \ with\",\n        \"object\": \"protein_membrane_stabilization\",\n        \"\
    description\": \"Trehalose-linked cryoprotection is associated with protein and\
    \ membrane stabilization during cold stress.\",\n        \"evidence\": [\n   \
    \       {\n            \"reference\": \"DOI:10.17159/sajs.2018/20170254\",\n \
    \           \"snippet\": \"counteracting protein aggregation, improving protein\
    \ folding and stabilizing membranes and proteins at chilling temperatures\",\n\
    \            \"notes\": \"Verified against the open Hamdan review; this connector\
    \ keeps trehalose as a compatible-solute cryoprotection branch.\"\n          }\n\
    \        ],\n        \"predicate_id\": \"biolink:associated_with\"\n      },\n\
    \      \"status\": \"supported_with_scope_limit\",\n      \"assessment\": \"Process/process\
    \ association is formally compatible; detailed protection biology not assessed.\"\
    \n    },\n    {\n      \"index\": 12,\n      \"edge\": {\n        \"subject\"\
    : \"thermal_hysteresis\",\n        \"predicate\": \"associated with\",\n     \
    \   \"object\": \"cryoprotection\",\n        \"description\": \"Antifreeze-protein\
    \ thermal hysteresis is associated with cryoprotection near freezing.\",\n   \
    \     \"evidence\": [\n          {\n            \"reference\": \"DOI:10.1007/s42770-023-01057-4\"\
    ,\n            \"snippet\": \"AFPs lower the water freezing point, avoiding frostbite\
    \ due to their thermal hysteresis\",\n            \"notes\": \"Verified against\
    \ the open Ramón et al. abstract and review text; this connector keeps antifreeze\
    \ proteins as ice-binding cryoprotection context.\"\n          }\n        ],\n\
    \        \"predicate_id\": \"biolink:associated_with\"\n      },\n      \"status\"\
    : \"qualified\",\n      \"assessment\": \"Broad association admits the lowering/hysteresis\
    \ facet; no extra forced process/quality finding.\"\n    },\n    {\n      \"index\"\
    : 13,\n      \"edge\": {\n        \"subject\": \"catalytic_activity_low_temperature\"\
    ,\n        \"predicate\": \"associated with\",\n        \"object\": \"psychrophile_machinery\"\
    ,\n        \"description\": \"Flexible-enzyme catalytic activity is associated\
    \ with psychrophile cold-adapted machinery.\",\n        \"evidence\": [\n    \
    \      {\n            \"reference\": \"DOI:10.17159/sajs.2018/20170254\",\n  \
    \          \"snippet\": \"adapted to function at low temperatures, with high catalytic\
    \ constants\",\n            \"notes\": \"Verified against the open Hamdan review;\
    \ this connector keeps low-temperature enzyme flexibility as contextual psychrophile\
    \ machinery.\"\n          }\n        ],\n        \"predicate_id\": \"biolink:associated_with\"\
    \n      },\n      \"status\": \"qualified\",\n      \"assessment\": \"Activity-to-machinery\
    \ association formally compatible under broad Biolink endpoints; no pathway completeness\
    \ inference.\"\n    },\n    {\n      \"index\": 14,\n      \"edge\": {\n     \
    \   \"subject\": \"membrane_fluidity\",\n        \"predicate\": \"associated with\"\
    ,\n        \"object\": \"psychrophile_machinery\",\n        \"description\": \"\
    Membrane-fluidity regulation is associated with psychrophile cold-adapted machinery.\"\
    ,\n        \"evidence\": [\n          {\n            \"reference\": \"DOI:10.17159/sajs.2018/20170254\"\
    ,\n            \"snippet\": \"regulate or modulate the fluidity of the membrane\
    \ in freezing environments\",\n            \"notes\": \"Verified against the open\
    \ Hamdan review; the membrane-fluidity section names membrane-fluidity modulation\
    \ in freezing environments as a frequent psychrophile cold-adaptation strategy.\"\
    \n          }\n        ],\n        \"predicate_id\": \"biolink:associated_with\"\
    \n      },\n      \"status\": \"qualified\",\n      \"assessment\": \"Quality-to-machinery\
    \ association formally allowed; not RO2326 and not process-only by inherited mapping.\"\
    \n    }\n  ],\n  \"source\": [\n    {\n      \"index\": 0,\n      \"field\": \"\
    causal_graphs[0].edges[0]\",\n      \"subject\": \"cold_environment\",\n     \
    \ \"predicate\": \"selects for\",\n      \"object\": \"psychrophile_machinery\"\
    ,\n      \"source_outcome\": \"qualified\",\n      \"assessment\": \"Near-freezing\
    \ environmental context is supported. Selection and sufficiency are not independently\
    \ tested by the short quotation.\",\n      \"references\": [\n        \"DOI:10.1038/sj.embor.7400662\"\
    \n      ]\n    },\n    {\n      \"index\": 1,\n      \"field\": \"causal_graphs[0].edges[1]\"\
    ,\n      \"subject\": \"psychrophile_machinery\",\n      \"predicate\": \"confers\"\
    ,\n      \"object\": \"temperature_optimum_very_low_trait\",\n      \"source_outcome\"\
    : \"unknown\",\n      \"assessment\": \"Generic unsaturation/temperature context\
    \ is positive; it does not by itself establish a ≤10 optimum or a sufficient machinery-to-bin\
    \ causal claim.\",\n      \"references\": [\n        \"DOI:10.1146/annurev-micro-091313-103612\"\
    \n      ]\n    },\n    {\n      \"index\": 2,\n      \"field\": \"causal_graphs[0].edges[2]\"\
    ,\n      \"subject\": \"temperature_optimum_very_low_trait\",\n      \"predicate\"\
    : \"is a\",\n      \"object\": \"temperature_optimum\",\n      \"source_outcome\"\
    : \"concern\",\n      \"assessment\": \"The quoted D’Amico passage is about broad\
    \ near-freezing growth; the adjacent note specifically overstates it as ≤10 optimum\
    \ support. Formal quantitative parentage is separately grounded.\",\n      \"\
    references\": [\n        \"DOI:10.1038/sj.embor.7400662\"\n      ]\n    },\n \
    \   {\n      \"index\": 3,\n      \"field\": \"causal_graphs[0].edges[3]\",\n\
    \      \"subject\": \"fatty_acid_desaturase_activity\",\n      \"predicate\":\
    \ \"increases\",\n      \"object\": \"unsaturated_fatty_acids\",\n      \"source_outcome\"\
    : \"UNASSESSED_SCOPE\",\n      \"assessment\": \"Existing short Hamdan phrase\
    \ is literal; detailed desaturase regulation/cold-adaptation efficacy is outside\
    \ the declared scope.\",\n      \"references\": [\n        \"DOI:10.17159/sajs.2018/20170254\"\
    \n      ]\n    },\n    {\n      \"index\": 4,\n      \"field\": \"causal_graphs[0].edges[4]\"\
    ,\n      \"subject\": \"unsaturated_fatty_acids\",\n      \"predicate\": \"contributes\
    \ to\",\n      \"object\": \"membrane_fluidity\",\n      \"source_outcome\": \"\
    qualified\",\n      \"assessment\": \"Both supplied spans are literal. The Yang\
    \ attribution remains its reported B. simplex H-b context; generic unsaturation/fluidity\
    \ context does not establish a universal optimum bin or an intervention effect.\"\
    ,\n      \"references\": [\n        \"DOI:10.1128/AEM.01928-22\",\n        \"\
    DOI:10.17159/sajs.2018/20170254\"\n      ]\n    },\n    {\n      \"index\": 5,\n\
    \      \"field\": \"causal_graphs[0].edges[5]\",\n      \"subject\": \"cold_shock_proteins\"\
    ,\n      \"predicate\": \"contributes to\",\n      \"object\": \"translation_low_temperature\"\
    ,\n      \"source_outcome\": \"UNASSESSED_SCOPE\",\n      \"assessment\": \"Literal\
    \ Hamdan phrase verified only; detailed protein-synthesis/cold-survival role not\
    \ adjudicated.\",\n      \"references\": [\n        \"DOI:10.17159/sajs.2018/20170254\"\
    \n      ]\n    },\n    {\n      \"index\": 6,\n      \"field\": \"causal_graphs[0].edges[6]\"\
    ,\n      \"subject\": \"trehalose\",\n      \"predicate\": \"contributes to\"\
    ,\n      \"object\": \"cryoprotection\",\n      \"source_outcome\": \"UNASSESSED_SCOPE\"\
    ,\n      \"assessment\": \"Existing Hamdan span is literal. Mixed/pathogen context\
    \ occurs nearby; detailed trehalose survival/defense efficacy not assessed.\"\
    ,\n      \"references\": [\n        \"DOI:10.17159/sajs.2018/20170254\"\n    \
    \  ]\n    },\n    {\n      \"index\": 7,\n      \"field\": \"causal_graphs[0].edges[7]\"\
    ,\n      \"subject\": \"antifreeze_proteins\",\n      \"predicate\": \"causes\"\
    ,\n      \"object\": \"thermal_hysteresis\",\n      \"source_outcome\": \"UNASSESSED_SCOPE\"\
    ,\n      \"assessment\": \"Existing Ramón phrase is literal in the retained HTML;\
    \ antifreeze efficacy/mechanisms not assessed.\",\n      \"references\": [\n \
    \       \"DOI:10.1007/s42770-023-01057-4\"\n      ]\n    },\n    {\n      \"index\"\
    : 8,\n      \"field\": \"causal_graphs[0].edges[8]\",\n      \"subject\": \"enzyme_structural_flexibility\"\
    ,\n      \"predicate\": \"increases\",\n      \"object\": \"catalytic_activity_low_temperature\"\
    ,\n      \"source_outcome\": \"UNASSESSED_SCOPE\",\n      \"assessment\": \"Existing\
    \ enzyme-activity comparison phrase is literal; no enhancement, engineering or\
    \ low-temperature efficacy assessment.\",\n      \"references\": [\n        \"\
    DOI:10.17159/sajs.2018/20170254\"\n      ]\n    },\n    {\n      \"index\": 9,\n\
    \      \"field\": \"causal_graphs[0].edges[9]\",\n      \"subject\": \"translation_low_temperature\"\
    ,\n      \"predicate\": \"associated with\",\n      \"object\": \"psychrophile_machinery\"\
    ,\n      \"source_outcome\": \"UNASSESSED_SCOPE\",\n      \"assessment\": \"Supplied\
    \ Phadtare phrase is literal in current PMC HTML despite indexed-abstract miss;\
    \ detailed RNA/protein-synthesis mechanism not assessed.\",\n      \"references\"\
    : [\n        \"DOI:10.4161/rna.7.6.13482\"\n      ]\n    },\n    {\n      \"index\"\
    : 10,\n      \"field\": \"causal_graphs[0].edges[10]\",\n      \"subject\": \"\
    protein_membrane_stabilization\",\n      \"predicate\": \"associated with\",\n\
    \      \"object\": \"psychrophile_machinery\",\n      \"source_outcome\": \"concern\"\
    ,\n      \"assessment\": \"Supplied Hamdan snippet is not literal on either inspected\
    \ primary surface; the stabilization connector’s biological efficacy remains unassessed.\"\
    ,\n      \"references\": [\n        \"DOI:10.17159/sajs.2018/20170254\"\n    \
    \  ]\n    },\n    {\n      \"index\": 11,\n      \"field\": \"causal_graphs[0].edges[11]\"\
    ,\n      \"subject\": \"cryoprotection\",\n      \"predicate\": \"associated with\"\
    ,\n      \"object\": \"protein_membrane_stabilization\",\n      \"source_outcome\"\
    : \"concern\",\n      \"assessment\": \"Supplied Hamdan snippet is not literal\
    \ on either inspected primary surface; no biological refutation or detailed cryoprotection\
    \ assessment.\",\n      \"references\": [\n        \"DOI:10.17159/sajs.2018/20170254\"\
    \n      ]\n    },\n    {\n      \"index\": 12,\n      \"field\": \"causal_graphs[0].edges[12]\"\
    ,\n      \"subject\": \"thermal_hysteresis\",\n      \"predicate\": \"associated\
    \ with\",\n      \"object\": \"cryoprotection\",\n      \"source_outcome\": \"\
    UNASSESSED_SCOPE\",\n      \"assessment\": \"Existing Ramón phrase is literal;\
    \ no cryoprotection intervention/efficacy adjudication.\",\n      \"references\"\
    : [\n        \"DOI:10.1007/s42770-023-01057-4\"\n      ]\n    },\n    {\n    \
    \  \"index\": 13,\n      \"field\": \"causal_graphs[0].edges[13]\",\n      \"\
    subject\": \"catalytic_activity_low_temperature\",\n      \"predicate\": \"associated\
    \ with\",\n      \"object\": \"psychrophile_machinery\",\n      \"source_outcome\"\
    : \"concern\",\n      \"assessment\": \"Supplied Hamdan snippet is not literal\
    \ on either inspected primary surface; enzyme enhancement/catalytic efficacy remains\
    \ unassessed.\",\n      \"references\": [\n        \"DOI:10.17159/sajs.2018/20170254\"\
    \n      ]\n    },\n    {\n      \"index\": 14,\n      \"field\": \"causal_graphs[0].edges[14]\"\
    ,\n      \"subject\": \"membrane_fluidity\",\n      \"predicate\": \"associated\
    \ with\",\n      \"object\": \"psychrophile_machinery\",\n      \"source_outcome\"\
    : \"qualified\",\n      \"assessment\": \"Existing Hamdan fluidity phrase is literal;\
    \ basic membrane physical context retained without asserting quantitative optimum\
    \ or machinery sufficiency.\",\n      \"references\": [\n        \"DOI:10.17159/sajs.2018/20170254\"\
    \n      ]\n    }\n  ]\n}"
- assessment_id: owners
  area: ownership
  topic: 'Native checklist: maintained payloads, guards and consumers'
  outcome: supported
  target_ids:
  - METPO:1000441
  summary: Formal edges recur in the exact review-writer payload and connector SOURCE_CONNECTOR_EDGES
    preimage assumptions, with conditional wildcard mappings. Current review replay
    rejects the pruned partial state; connector no-ops and grounder skips populated
    IDs. Quotation spans are in connector ADDED_EDGES, consumed by PR664; that consumer
    is not the original formal-edge writer. Machinery facet and attribution notes
    are record-only. No ordinary rerun is a repair.
  evidence_ids:
  - owners
  - owner-primary
  - predicate-mapping
  - discovery
  - root-verification
  - adjudication
- assessment_id: provenance
  area: provenance
  topic: 'Native checklist: attributable human acceptance'
  outcome: concern
  target_ids:
  - METPO:1000441
  summary: Seventeen embedded events comprise sixteen AI events and one seed. Ignored-
    and hidden-inclusive discovery found 185 matching paths and 71 actual top-level
    target arrays, none exact. Seventeen history projections, seven current whole
    histories and ten qualified prior whole readings establish no attributable local
    human acceptance. Root selected/projection reading is separately attributed; private
    or remote acceptance remains unknown.
  evidence_ids:
  - human-search
  - histories
  - ground-reading
  - root-reading
  - root-verification
  - record
- assessment_id: expression
  area: completeness
  topic: 'Native checklist: bounded catalog and adapter availability'
  outcome: unknown
  target_ids:
  - METPO:1000441
  summary: Retained catalog checks cover selected canonical/source-organism names
    only; they do not establish global expression absence or exhaustive coverage of
    all incidental source taxa. Current bounded discovery found the maintained adapter
    unavailable. Primary fallback is limited to identity and supplied generic/literal
    context; no module membership or efficacy result is reported.
  evidence_ids:
  - expression
  - expression-discovery
  - source-reading
- assessment_id: readiness
  area: completeness
  topic: 'Native checklist: scope and optional protein instances'
  outcome: supported
  target_ids:
  - METPO:1000441
  summary: One component, sixteen nodes and fifteen edges form a quantitative NONMECHANISTIC
    record. Two reviewed label-only protein classes and no instances do not require
    fabricated accessions or additional connectors. Completeness of the review does
    not certify detailed biological mechanisms.
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
  - METPO:1000441
  summary: Current inspect, focused validation, strict validation and snippet command
    completed successfully. Snippet misses/unresolved responses remain inconclusive.
    B14 common checks are actual fresh executions at the advanced base, with original
    failures, cache provenance, product skips and omitted full suite retained. Software
    integrity does not establish scientific meaning.
  evidence_ids:
  - capture
  - fresh-common-completion
  - check-temperature-optimum-very-low-validate
  - check-temperature-optimum-very-low-strict
  - check-temperature-optimum-very-low-snippets-network
  - source-native
findings:
- finding_id: imported-process-roles
  issue_key: temperature-optimum-very-low-imported-process-roles
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Imported process roles
  description: 'Edges 3 and 8 use RO:0002213, whose inherited domain and range require
    processes: edge 3 targets explicit material fatty acids and edge 8 starts from
    explicit structural flexibility QUALITY. Edge 4 uses RO:0002326, whose material-to-process
    roles conflict with its membrane-fluidity QUALITY object. The explicit activity
    endpoints are not rejected merely for MOLECULAR_FUNCTION type. These are formal
    representation defects, independent of detailed biological efficacy.'
  target_ids:
  - METPO:1000441
  field_paths:
  - causal_graphs[0].edges[3].predicate_id
  - causal_graphs[0].edges[4].predicate_id
  - causal_graphs[0].edges[8].predicate_id
  evidence_ids:
  - nodes-edges
  - ro-primary
  - owners
  - owner-primary
  - predicate-mapping
  - root-verification
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_optimum_very_low.yaml
    role: Current record assertions; separate authorized curation required
  - repository: CultureBotAI/TraitMech
    path: scripts/review_temperature_optimum_very_low_graph_183.py
    role: Exact historical formal-edge after-payload; current pruned partial replay
      is rejected
  - repository: CultureBotAI/TraitMech
    path: scripts/connect_temperature_optimum_very_low_graph_183.py
    role: SOURCE_CONNECTOR_EDGES preimage assumptions, not ordinary formal-edge replacement
      payload; current connector no-ops
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Conditional wildcard recurrence for empty predicate IDs, not an automatic
      current rewrite
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Shared predicate writer skips populated IDs; ordinary rerun does not repair
      current assertions
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: machinery-facet
  issue_key: temperature-optimum-very-low-machinery-facet
  category: representation
  severity: minor
  status: open
  certainty: confirmed
  title: Machinery facet
  description: Node 3 is typed BIOLOGICAL_PROCESS while its label and description
    name an ensemble of enzymes and lipid membranes. The sustaining-function wording
    leaves an activity interpretation plausible. Clarify the intended referent; this
    bounded precision issue does not establish a required replacement enum or refute
    biological relevance.
  target_ids:
  - METPO:1000441
  field_paths:
  - causal_graphs[0].nodes[3].node_type
  - causal_graphs[0].nodes[3].description
  evidence_ids:
  - record
  - nodes-edges
  - schema
  - owners
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_optimum_very_low.yaml
    role: Current record assertions; separate authorized curation required
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: growth-versus-optimum-attribution
  issue_key: temperature-optimum-very-low-growth-versus-optimum-attribution
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Growth versus optimum attribution
  description: The D’Amico passage explicitly uses psychrophiles broadly for microorganisms
    growing near freezing, including psychrotolerant/psychrotroph usage. Two attached
    notes convert that growth statement into optimum or at-most-10-degree support.
    Qualify these local attributions while preserving the literal snippet and independently
    supported METPO bin and parent. No assertion is made that the uninspected remainder
    lacks all numerical context.
  target_ids:
  - METPO:1000441
  field_paths:
  - evidence[0].notes
  - causal_graphs[0].edges[2].evidence[0].notes
  evidence_ids:
  - sources
  - placements
  - notes
  - definition-pdf
  - definition-extraction-text
  - metpo-primary
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_optimum_very_low.yaml
    role: Current record assertions; separate authorized curation required
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: nonverbatim-source-snippets
  issue_key: temperature-optimum-very-low-nonverbatim-source-snippets
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Nonverbatim source snippets
  description: Three supplied Hamdan snippets have no literal match in the retained
    SciELO HTML or publisher PDF-derived text, including whitespace normalization,
    case folding and line-end dehyphenation. Their exact strings are also in the current
    connector ADDED_EDGES payload. Treat this as a bounded copied-span presentation
    issue; the biological propositions and other publication versions are not refuted.
  target_ids:
  - METPO:1000441
  field_paths:
  - causal_graphs[0].edges[10].evidence[0].snippet
  - causal_graphs[0].edges[11].evidence[0].snippet
  - causal_graphs[0].edges[13].evidence[0].snippet
  evidence_ids:
  - snippets
  - literal-check
  - hamdan-html
  - hamdan-pdf
  - hamdan-extraction-text
  - root-verification
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_optimum_very_low.yaml
    role: Current record assertions; separate authorized curation required
  - repository: CultureBotAI/TraitMech
    path: scripts/connect_temperature_optimum_very_low_graph_183.py
    role: Exact ADDED_EDGES quotation payload; preserve no-op/drift guards and validate
      PR664 consumer
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: human-acceptance-link
  issue_key: temperature-optimum-very-low-human-acceptance-link
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Human acceptance link
  description: The REVIEWED status has no attributable human acceptance in the inspected
    local scope. Seventeen embedded events contain sixteen AI events and one seed.
    Ignored- and hidden-inclusive discovery found 185 matching paths and 71 actual
    top-level review target arrays, with no exact current target. Seventeen captured
    histories have AI actor projections, with seven current whole and ten byte-qualified
    prior whole readings. Private or remote acceptance remains unknown.
  target_ids:
  - METPO:1000441
  field_paths:
  - mapping_status
  - curation_history
  evidence_ids:
  - human-search
  - histories
  - ground-reading
  - root-reading
  - root-verification
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_optimum_very_low.yaml
    role: Current record assertions; separate authorized curation required
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
actions:
- action_id: curate-imported-process-roles
  description: In separately authorized curation, reconcile the three imported relations
    with their explicit material, quality and activity referents. Coordinate the exact
    review-writer payload, connector source-preimage guards, and wildcard increases/contributes-to
    mappings. Current review replay rejects its pruned partial state, the current
    connector no-ops, and the grounder skips populated IDs; an ordinary rerun is not
    a repair. No replacement biological mechanism or intervention is proposed.
  finding_ids:
  - imported-process-roles
  target_ids:
  - METPO:1000441
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_optimum_very_low.yaml
    role: Current record assertions; separate authorized curation required
  - repository: CultureBotAI/TraitMech
    path: scripts/review_temperature_optimum_very_low_graph_183.py
    role: Exact historical formal-edge after-payload; current pruned partial replay
      is rejected
  - repository: CultureBotAI/TraitMech
    path: scripts/connect_temperature_optimum_very_low_graph_183.py
    role: SOURCE_CONNECTOR_EDGES preimage assumptions, not ordinary formal-edge replacement
      payload; current connector no-ops
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Conditional wildcard recurrence for empty predicate IDs, not an automatic
      current rewrite
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Shared predicate writer skips populated IDs; ordinary rerun does not repair
      current assertions
  acceptance_checks:
  - Show inherited domain/range compatibility for edges 3, 4 and 8 while preserving
    the intended referents.
  - Keep the target writer payload and connector SOURCE_CONNECTOR_EDGES assumptions
    consistent under explicit replay/drift checks; PR664 ADDED_EDGES is not the replacement
    source for these formal edges.
  - Preserve RO:0002326 endpoint controls at edges 5 and 6, broad local/Biolink roles
    and direct subclass support; endpoint compatibility does not certify efficacy.
  - Run focused strict and relevant predicate/graph checks, full QC and required history/product
    gates.
- action_id: curate-machinery-facet
  description: Clarify whether node 3 denotes the material ensemble or its activity,
    and make its label, description and type consistently denote that intended referent.
    Do not prescribe an unsupported exact ontology term or add a detailed mechanism.
  finding_ids:
  - machinery-facet
  target_ids:
  - METPO:1000441
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_optimum_very_low.yaml
    role: Current record assertions; separate authorized curation required
  acceptance_checks:
  - The retained node has one explicit referent consistent with the schema facet.
  - Preserve uncertainty about exact quantitative calibration and causal sufficiency;
    run focused strict and applicable curation gates.
- action_id: curate-growth-versus-optimum-attribution
  description: Qualify the two evidence notes to the inspected broad growth context,
    distinguishing it from the ontology-supported numerical bin and direct parent
    relation. Preserve the literal source span.
  finding_ids:
  - growth-versus-optimum-attribution
  target_ids:
  - METPO:1000441
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_optimum_very_low.yaml
    role: Current record assertions; separate authorized curation required
  acceptance_checks:
  - Each note describes only what its nearest inspected passage supports.
  - Retain the positive ontology hierarchy and rerun focused strict/snippet checks
    and applicable curation gates.
- action_id: curate-nonverbatim-source-snippets
  description: Resolve the three literal-span discrepancies in the current record
    and exact connector quotation payload. Use only independently verified source
    text in snippet fields; keep interpretation clearly separate and leave unsupported
    attribution explicit. Preserve the current guard behavior and validate the PR664
    consumer of ADDED_EDGES. No new mechanistic or intervention claim is proposed.
  finding_ids:
  - nonverbatim-source-snippets
  target_ids:
  - METPO:1000441
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_optimum_very_low.yaml
    role: Current record assertions; separate authorized curation required
  - repository: CultureBotAI/TraitMech
    path: scripts/connect_temperature_optimum_very_low_graph_183.py
    role: Exact ADDED_EDGES quotation payload; preserve no-op/drift guards and validate
      PR664 consumer
  acceptance_checks:
  - Each retained snippet has an exact auditable location on its cited inspected source
    surface; do not silently present a paraphrase as a quotation.
  - Current connector payload and record agree, with current no-op/drift guards and
    PR664 consumer behavior checked before any authorized replay.
  - Rerun focused strict and snippet checks, full QC and required history/product
    gates; literal correctness is not biological validation.
- action_id: curate-human-acceptance-link
  description: Link actual attributable human acceptance of these current assertions,
    if available, or qualify the review-status provenance under repository policy.
    Do not fabricate retrospective sign-off.
  finding_ids:
  - human-acceptance-link
  target_ids:
  - METPO:1000441
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_optimum_very_low.yaml
    role: Current record assertions; separate authorized curation required
  acceptance_checks:
  - Acceptance evidence identifies a person, exact assertions and disposition, or
    remaining uncertainty is explicit.
  - Preserve append-only history and run applicable maintained gates for any separately
    authorized curation change.
limitations:
- Full just test was NOT_RUN under the selected review-only diagnostic scope; only
  the five focused Stage2 tests are recorded. Products retains 123 no-adapter skips.
  Common checks establish bounded software/data integrity, not scientific support.
- Detailed stress-defense, survival, fitness, cryoprotection, enzyme/RNA/protein enhancement,
  cultivation optimization and intervention efficacy remain UNASSESSED_SCOPE; no operational
  repair proposed.
- Canonical DOI/title and official species identity are positive; canonical numerical
  optimum, culture conditions and phenotype claims were not assessed, and no canonical
  article body/table was acquired.
- The METPO class establishes the current at-most-10 Cel bin and direct parent; its
  existential restriction is not a universal growth curve or independent biological
  calibration. Exact biological equivalence of the inherited Psychrophile alias remains
  unresolved.
- Generic membrane physical context and source presence do not establish a sufficient
  or exclusive mechanism for the quantitative optimum.
- Hamdan three-span absence is bounded to retained primary HTML/PDF extracted surfaces
  and normalization used; it is not biological refutation or an all-publication-version
  search.
- D’Amico selected generic introduction and supplied literal phrase only; Mendoza
  publisher abstract only. Whole-body mechanistic reading is not claimed.
- Original source acquisition, derived-text extraction, current copies, browser calls/exports
  and current readings retain distinct times. Reused metadata notice fields are not
  current publication-status refreshes.
- Hamdan EuropePMC zero hit and root DOI browser failure are diagnostics, superseded
  for identity by actual Crossref/HTML/PDF evidence. Yang XML HTTP500 yielded no body;
  its supplied phrase is literal in the indexed abstract. Phadtare prior failed body
  attempts are separate from its current successful HTML literal check.
- Taxonomy initial DNS failure is preserved separately from the successful official
  retry. Identity does not prove phenotype or strain-to-species transfer.
- Seventeen history actor/target/event projections were inspected, with seven current
  whole and ten individually byte-qualified prior whole readings; seed and AI actors
  do not establish human acceptance. Private and remote acceptance remains unknown.
- Expression adapter unavailable in fresh bounded PATH/project/install discovery;
  retained catalog has20organisms28datasets with original access time. No exact canonical/Bacillus
  simplex or incidental Listeria key is present in that catalog, not a global absence
  across all source organisms. No detailed module queries or causal claims made.
- NONMECHANISTIC measurement scope, one connected component, two reviewed label-only
  protein classes and zero instances do not require invented proteins, connectors
  or mechanisms.
- All sources, formal roles, quotation checks, record status and software checks retain
  their distinct evidential scopes; schema/QC success is not scientific validation.
- Root final combines the independently frozen grounding assessment (one major/two
  minors) and source assessment (two minors); it does not promote source UNKNOWN or
  UNASSESSED_SCOPE claims to supported.
- 'Formal owner roles differ: review script owns exact after-payload; connector SOURCE_CONNECTOR_EDGES
  is a source-preimage guard. For the quotation finding, connector ADDED_EDGES is
  the actual payload; PR664 is its consumer requiring validation, not the origin of
  the snippet template.'
- Frozen source-note-ledger labels the canonical field canonical_examples[0].notes;
  the actual current field is singular canonical_examples[0].note. This is a locator
  clarification only, and no finding is attached to that canonical claim.
- Root primary reading is bounded by selected-primary-reading.json and root-current-verification.json.
  Detailed source literal checks and broader owner/history reads are attributed to
  the independent peers; no claim that root reread every full paper, script or prior
  whole history.
- RO:0002326 roles follow 2216 to 2500 to 2595; GO-specific usage commentary does
  not impose an invented universal protein-only domain. Compatible edge5/6 endpoints
  do not establish contributing execution or biological efficacy.
- Node13 explicitly describes lowering of freezing point; its process reading remains
  plausible despite the hysteresis label. No extra forced type finding.
- The current native snippet command passed with 2 VERIFIED, 6 NOT_IN_ABSTRACT and
  9 UNRESOLVED. Separate primary checks found 14 of17 supplied spans literal and three
  nonverbatim on inspected surfaces; the native result is not rewritten.
- Ground search uses the exact current label/ID/slug, includes hidden/ignored entries
  except .git/.venv, and reads actual top-level targets arrays. One extra uncaptured
  thermotaxis-script matching line is generic context only, not a fully audited current
  owner.
notes:
- Historical products failures/retry and original cache provenance remain in /private/tmp/traitmech-record-sweep-014.q8m4v2cs/new-base-diagnostic-independent-review-agent/fresh-products-completion.json.
  The earlier outstanding-products status is superseded by the actual fresh run; no
  blanket cross-batch reuse qualification is asserted.
- Final fields, severities, owners and actions come only from actual root FINAL. Frozen
  source and formal ledgers retain unknown and unassessed scope; no inherited finding
  or biological repair is added.
- The serializer adopts frozen audits and root adjudication. Original acquisition,
  historical extraction, current copying/reading, actual browser call/export and failed/successful
  request clocks remain distinct. It makes no scientific record, state, Git or publication
  changes.
tags:
- record-review
- temperature-optimum-very-low
- environment
- needs-curation
```
