# Whole-record review of temperature preference

- Review: 20261022T024853Z-temperature-preference
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-22T02:36:26.647389Z
- Finished UTC: 2026-10-22T02:48:53Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Whole-record review of temperature preference finds one major imported-relation role defect across seven edges and three bounded minor findings: rate/process typing, noncontiguous source snippets and human-acceptance traceability. Active identity, broad definition, parent, family grounding and canonical species identities are positive; detailed efficacy and canonical numerical claims remain unassessed.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: Seventh record in the actual B14 queue; current 339-line target and 86 captured inputs. Local review is independent of remote publication.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 508ee3089c93a36413969cd1ede7f9528a1940a4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| METPO:1000613 | data/traits/environment/temperature_preference.yaml | maintained | temperature preference |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Fresh B14 corpus QC | passed | True | METPO:1000613 | Actual just qc passed: strict validation of 1130 records with 0 errors; graph audit: 74 baselined, 0 new and 0 blocking findings; 135 connected graphs and 1588 wired nodes; protein coverage: 729 graphs (134 pass, 594 NONMECHANISTIC, 0 gaps, 1 protected); snippet audit: 2419 baselined, 0 new and 0 blocking findings; 19 PathwayMech links. These are corpus diagnostics, not scientific validation of this target. |
| Fresh B14 history integrity | passed | True | METPO:1000613 | 1278 HistoryRecord YAMLs validated, 0 invalid; current history snapshot contains 1279 files. Integrity does not establish scientific correctness or human acceptance. |
| Fresh B14 mapping identifier/label validation | passed | True | METPO:1000613 | 361 canonical matches, 2 exact-synonym matches, 1 exception and 123 SKIPPED_NO_ADAPTER pairs. Configured scope is the two grounding mappings, not every target identifier or scientific claim. |
| Focused Stage2 writer tests | passed | False | METPO:1000613 | Five tests passed in the explicitly selected Stage2 test file. This is not a full just test run or biological validation. |
| Focused native validation | passed | True | METPO:1000613 | Native record validation passed; scientific interpretation is assessed separately. |
| Focused strict validation | passed | True | METPO:1000613 | The actual validate-strict command passed. |
| Focused network snippet check | passed | True | METPO:1000613 | Native command completed successfully: seven fields across five references, three VERIFIED, two NOT_IN_ABSTRACT and two UNRESOLVED. Misses remain inconclusive. Manual inspection separately found five literal and two noncontiguous snippets; the baselined Tolner ELLIPTICAL_SNIPPET ERROR remains explicit. |
| One-target native review capture | passed | True | METPO:1000613 | One current target, 86 captured inputs, exact current base and successful native inspect. |
| Protein-instance metadata applicability | not_applicable | False | METPO:1000613 | One InterPro-grounded protein family and no instances; no accession invented. |
| Structured source-organism expression query availability | unavailable | False | METPO:1000613 | Maintained adapter unavailable within bounded discovery; retained catalog and generic primary context do not supply module membership or efficacy results. |

## Scientific And Domain Assessments

### Native checklist: active target, parent and local authorities

identity: supported. Targets: METPO:1000613.

Active METPO:1000613 identity and METPO:1000059 parent are positive. Local challenges and membrane-fluidity terms are positive; redundant related-label wording remains an upstream qualification, not a forced identifier change.

### Native checklist: broad temperature preference classification

quantity: supported. Targets: METPO:1000613.

Dantigny publisher identity and the supplied generic classification phrase support the broad definition. Its successful publisher response is distinct from a zero-hit indexed lookup. No quantitative model, growth parameters or exhaustive phenotype support is adopted.

### Native checklist: species and article identity versus numerical support

quantity: unknown. Targets: METPO:1000613.

Both official species and assigned article identities are positive. Canonical quantities, cultivation, adaptation and optimization support remain UNASSESSED_SCOPE; title-level identity does not verify or refute those notes.

### Native checklist: nine works and sixteen placements

evidence: unknown. Targets: METPO:1000613.

All nine source identities resolve. Generic physical context and supplied literal spans do not establish exact mechanism-to-preference sufficiency. Permeability is distinct from fluidity. Detailed RNA/stress/desaturase regulation, survival, fitness, defense, enzyme/intervention efficacy and canonical numerical/cultivation support remain UNASSESSED_SCOPE.

### Native checklist: seven supplied snippets and original native severity

evidence: concern. Targets: METPO:1000613.

Manual inspection found five literal snippets and two noncontiguous presentations. Tolner joins spans with a marked ellipsis; Mendoza omits intervening words. Preserve Tolner native ELLIPTICAL_SNIPPET ERROR, normalized here to a minor copied-span finding because generic context remains supported. Native three VERIFIED, two NOT_IN_ABSTRACT and two UNRESOLVED remain separate; misses are inconclusive, not biological refutations.

### Native checklist: all thirteen current referents

representation: concern. Targets: METPO:1000613.

The explicit growth-rate attribute is typed as a process: a bounded node 6 precision minor. Protein-stability wording remains qualified, without forced capacity retyping. Downshift may denote an event, cold-shock chaperone activity is a molecular activity, and the protein family has positive InterPro identity.

{
  "grounding": [
    {
      "index": 0,
      "node": {
        "node_id": "temperature_preference_trait",
        "label": "temperature preference",
        "node_type": "TRAIT",
        "grounding": "METPO:1000613",
        "description": "Growth phenotype characterized by preferred environmental temperature."
      },
      "status": "supported",
      "assessment": "Trait class exact active identity; broad preferred-temperature phenotype."
    },
    {
      "index": 1,
      "node": {
        "node_id": "environmental_temperature",
        "label": "environmental temperature",
        "node_type": "ENVIRONMENTAL_FACTOR",
        "description": "Growth temperature experienced by the organism."
      },
      "status": "supported",
      "assessment": "Environmental growth-temperature condition/axis, not explicitly a temperature-change process. ENVIRONMENTAL_FACTOR is appropriate; this condition does not satisfy imported RO process roles merely because it influences growth."
    },
    {
      "index": 2,
      "node": {
        "node_id": "low_temperature",
        "label": "low temperature",
        "node_type": "ENVIRONMENTAL_FACTOR",
        "description": "Cold growth condition that reduces molecular motion and membrane fluidity.",
        "grounding": "PATO:0001306"
      },
      "status": "supported",
      "assessment": "Cold growth condition is compatible with PATO relatively low-temperature quality and exact low-temperature synonym. Reference value unspecified; no forced event interpretation or enum defect."
    },
    {
      "index": 3,
      "node": {
        "node_id": "high_temperature",
        "label": "high temperature",
        "node_type": "ENVIRONMENTAL_FACTOR",
        "description": "Hot growth condition that challenges protein and membrane stability.",
        "grounding": "PATO:0001305"
      },
      "status": "supported",
      "assessment": "Hot growth condition is compatible with PATO relatively high-temperature quality and high-temperature synonym. Relative reference unspecified; no independent grounding/type finding."
    },
    {
      "index": 4,
      "node": {
        "node_id": "membrane_fluidity",
        "label": "membrane fluidity",
        "node_type": "QUALITY",
        "description": "Physical state of the membrane affecting transport and cell function.",
        "grounding": "METPO:1007505"
      },
      "status": "supported",
      "assessment": "Explicit membrane physical attribute and local v3 dynamic mobility term support QUALITY."
    },
    {
      "index": 5,
      "node": {
        "node_id": "protein_stability",
        "label": "protein stability",
        "node_type": "MOLECULAR_FUNCTION",
        "description": "Capacity of proteins to retain folded, functional conformations."
      },
      "status": "qualified",
      "assessment": "Capacity to retain folded functional conformations can describe a stability property/disposition or broad molecular function. Current MOLECULAR_FUNCTION includes function; no forced CAPACITY reservoir enum, no automatic protein/function conflation or separate confirmed finding. Detailed efficacy unassessed."
    },
    {
      "index": 6,
      "node": {
        "node_id": "growth_rate",
        "label": "microbial growth rate",
        "node_type": "BIOLOGICAL_PROCESS",
        "description": "Rate of population growth under a given temperature regime."
      },
      "status": "minor",
      "assessment": "Explicit rate of population growth denotes a measurable attribute, while BIOLOGICAL_PROCESS denotes the growth process. Clear label/description preserve intended quantity, so this is a bounded node-type precision finding, separate from the imported relation-role major. Do not invent a biological mechanism or new grounding."
    },
    {
      "index": 7,
      "node": {
        "node_id": "temperature_downshift",
        "label": "temperature downshift",
        "node_type": "ENVIRONMENTAL_FACTOR",
        "description": "A decrease in environmental growth temperature (cold shift)."
      },
      "status": "supported",
      "assessment": "Actual environmental decrease/cold shift denotes an event. ENVIRONMENTAL_FACTOR is permitted for environmental exposure or condition and is not inherently nonprocess."
    },
    {
      "index": 8,
      "node": {
        "node_id": "fatty_acid_desaturase",
        "label": "fatty acid desaturase",
        "node_type": "GENE_OR_PROTEIN",
        "description": "Desaturase enzyme (e.g., Des) that introduces double bonds into membrane fatty acids.",
        "grounding": "InterPro:IPR012171"
      },
      "status": "supported",
      "assessment": "Explicit desaturase enzyme is a material protein-family referent. Official IPR012171 family label matches; closeMatch is taxon-agnostic. Detailed function and organism-specific efficacy unassessed."
    },
    {
      "index": 9,
      "node": {
        "node_id": "unsaturated_membrane_fatty_acids",
        "label": "unsaturated membrane fatty acids",
        "node_type": "CHEMICAL",
        "description": "Membrane fatty acids bearing double bonds; raise membrane fluidity (homeoviscous adaptation)."
      },
      "status": "supported",
      "assessment": "Membrane fatty-acid molecules are chemical material. Their explanatory physical wording does not turn the node into a process or a measured proportion."
    },
    {
      "index": 10,
      "node": {
        "node_id": "rna_thermometer",
        "label": "RNA thermometer",
        "node_type": "RNA",
        "description": "Temperature-responsive RNA structure (ROSE/FourU) in 5-UTRs that gates translation by melting with temperature."
      },
      "status": "supported",
      "assessment": "Functional RNA structure is compatible with RNA. Detailed thermometer/translation regulation efficacy unassessed."
    },
    {
      "index": 11,
      "node": {
        "node_id": "heat_shock_gene_translation",
        "label": "heat-shock gene translation",
        "node_type": "BIOLOGICAL_PROCESS",
        "description": "Translation of heat-shock response genes permitted upon RNA thermometer melting at elevated temperature."
      },
      "status": "supported",
      "assessment": "Explicit translation denotes a biological process. Detailed heat-response efficacy unassessed."
    },
    {
      "index": 12,
      "node": {
        "node_id": "cold_shock_rna_chaperone_activity",
        "label": "cold-shock RNA chaperone activity",
        "node_type": "MOLECULAR_FUNCTION",
        "description": "CspA-type RNA chaperone activity that maintains single-stranded RNA to support translation at low temperature."
      },
      "status": "supported",
      "assessment": "Explicit RNA chaperone activity is a molecular activity; not a protein merely because a protein family is mentioned. Detailed cold-response efficacy unassessed."
    }
  ],
  "source": [
    {
      "index": 0,
      "field": "causal_graphs[0].nodes[0]",
      "node_id": "temperature_preference_trait",
      "label": "temperature preference",
      "node_type": "TRAIT",
      "source_outcome": "supported",
      "assessment": "Broad temperature-dependent growth phenotype supported by actual definition publisher context.",
      "incident_edges": [
        4,
        5
      ]
    },
    {
      "index": 1,
      "field": "causal_graphs[0].nodes[1]",
      "node_id": "environmental_temperature",
      "label": "environmental temperature",
      "node_type": "ENVIRONMENTAL_FACTOR",
      "source_outcome": "supported",
      "assessment": "Temperature is the study’s environmental axis; no operational growth model adopted.",
      "incident_edges": [
        0
      ]
    },
    {
      "index": 2,
      "field": "causal_graphs[0].nodes[2]",
      "node_id": "low_temperature",
      "label": "low temperature",
      "node_type": "ENVIRONMENTAL_FACTOR",
      "source_outcome": "qualified",
      "assessment": "Generic cold/physical fluidity context supported; detailed transport/survival efficacy not assessed.",
      "incident_edges": [
        1,
        10
      ]
    },
    {
      "index": 3,
      "field": "causal_graphs[0].nodes[3]",
      "node_id": "high_temperature",
      "label": "high temperature",
      "node_type": "ENVIRONMENTAL_FACTOR",
      "source_outcome": "qualified",
      "assessment": "Generic high-temperature material-stability context supported; source constraints and actual formal node sense remain distinct.",
      "incident_edges": [
        2,
        3,
        8
      ]
    },
    {
      "index": 4,
      "field": "causal_graphs[0].nodes[4]",
      "node_id": "membrane_fluidity",
      "label": "membrane fluidity",
      "node_type": "QUALITY",
      "source_outcome": "qualified",
      "assessment": "Generic membrane fluidity physical meaning positive. Permeability is a related but distinct property; no equivalence assumed.",
      "incident_edges": [
        1,
        3,
        4,
        7
      ]
    },
    {
      "index": 5,
      "field": "causal_graphs[0].nodes[5]",
      "node_id": "protein_stability",
      "label": "protein stability",
      "node_type": "MOLECULAR_FUNCTION",
      "source_outcome": "qualified",
      "assessment": "Protein conformational stability is generic source context; detailed mechanism/enhancement efficacy unassessed and formal facet separately audited.",
      "incident_edges": [
        2,
        5
      ]
    },
    {
      "index": 6,
      "field": "causal_graphs[0].nodes[6]",
      "node_id": "growth_rate",
      "label": "microbial growth rate",
      "node_type": "BIOLOGICAL_PROCESS",
      "source_outcome": "supported",
      "assessment": "Definition publisher explicitly refers to microbial growth rate; quantity-versus-process formal representation is separately assessed.",
      "incident_edges": [
        0
      ]
    },
    {
      "index": 7,
      "field": "causal_graphs[0].nodes[7]",
      "node_id": "temperature_downshift",
      "label": "temperature downshift",
      "node_type": "ENVIRONMENTAL_FACTOR",
      "source_outcome": "qualified",
      "assessment": "A temperature downshift is a contextual change; detailed induction efficacy not inferred.",
      "incident_edges": [
        11
      ]
    },
    {
      "index": 8,
      "field": "causal_graphs[0].nodes[8]",
      "node_id": "fatty_acid_desaturase",
      "label": "fatty acid desaturase",
      "node_type": "GENE_OR_PROTEIN",
      "source_outcome": "UNASSESSED_SCOPE",
      "assessment": "Enzyme class identity/formal grounding handled separately; detailed gene regulation and intervention effects unassessed.",
      "incident_edges": [
        6,
        11
      ]
    },
    {
      "index": 9,
      "field": "causal_graphs[0].nodes[9]",
      "node_id": "unsaturated_membrane_fatty_acids",
      "label": "unsaturated membrane fatty acids",
      "node_type": "CHEMICAL",
      "source_outcome": "qualified",
      "assessment": "Generic unsaturated fatty-acid physical context supported without cross-taxon or intervention efficacy inference.",
      "incident_edges": [
        6,
        7
      ]
    },
    {
      "index": 10,
      "field": "causal_graphs[0].nodes[10]",
      "node_id": "rna_thermometer",
      "label": "RNA thermometer",
      "node_type": "RNA",
      "source_outcome": "UNASSESSED_SCOPE",
      "assessment": "RNA naming/formal facet only; detailed thermosensing mechanism unassessed.",
      "incident_edges": [
        8,
        9
      ]
    },
    {
      "index": 11,
      "field": "causal_graphs[0].nodes[11]",
      "node_id": "heat_shock_gene_translation",
      "label": "heat-shock gene translation",
      "node_type": "BIOLOGICAL_PROCESS",
      "source_outcome": "UNASSESSED_SCOPE",
      "assessment": "Detailed heat-shock/stress-regulation efficacy unassessed.",
      "incident_edges": [
        9
      ]
    },
    {
      "index": 12,
      "field": "causal_graphs[0].nodes[12]",
      "node_id": "cold_shock_rna_chaperone_activity",
      "label": "cold-shock RNA chaperone activity",
      "node_type": "MOLECULAR_FUNCTION",
      "source_outcome": "UNASSESSED_SCOPE",
      "assessment": "Detailed cold-survival/RNA-chaperone mechanism and enhancement unassessed.",
      "incident_edges": [
        10
      ]
    }
  ]
}

### Native checklist: all twelve current relations

consistency: concern. Targets: METPO:1000613.

RO2211/2212/2213 edges 0/1/3/4/5/6/7 conflict with inherited process roles for their stated condition, quantity, phenotype or material referents. The edge 5 trait object is independently decisive despite qualified protein-stability wording. Local challenges has broad compatible endpoints. Four lexical-only edges do not inherit RO/Biolink restrictions from their English verbs. Detailed biological efficacy remains unassessed.

{
  "grounding": [
    {
      "index": 0,
      "edge": {
        "subject": "environmental_temperature",
        "predicate": "regulates",
        "object": "growth_rate",
        "description": "Microbial growth rate varies with growth temperature.",
        "evidence": [
          {
            "reference": "DOI:10.1038/sj.jim.2900572",
            "snippet": "growth rate vs temperature",
            "notes": "Study analyzes temperature dependence of microbial growth rates across psychrotrophs, mesophiles, and thermophiles."
          }
        ],
        "predicate_id": "RO:0002211"
      },
      "status": "major",
      "assessment": "RO2211 requires process/process. Current subject is environmental temperature condition/axis and object is an explicit growth-rate attribute despite its process enum. The subject mismatch persists after correcting the object type."
    },
    {
      "index": 1,
      "edge": {
        "subject": "low_temperature",
        "predicate": "decreases",
        "object": "membrane_fluidity",
        "description": "Cold temperature reduces membrane fluidity and transport efficiency.",
        "evidence": [
          {
            "reference": "DOI:10.1038/sj.embor.7400662",
            "snippet": "decreased membrane fluidity",
            "notes": "Review identifies membrane fluidity loss as a core cold challenge."
          }
        ],
        "predicate_id": "RO:0002212"
      },
      "status": "major",
      "assessment": "RO2212 inherits RO2211 process/process; the cold condition and membrane-fluidity quality are not the required processes."
    },
    {
      "index": 2,
      "edge": {
        "subject": "high_temperature",
        "predicate": "challenges",
        "object": "protein_stability",
        "description": "Elevated temperature challenges protein folding and functional stability.",
        "evidence": [
          {
            "reference": "DOI:10.1128/MMBR.65.1.1-43.2001",
            "snippet": "resistant to irreversible inactivation at high temperatures",
            "notes": "Review supports thermostable enzymes as a high-temperature adaptation."
          }
        ],
        "predicate_id": "METPO:2007406"
      },
      "status": "qualified",
      "assessment": "Local v2 challenges has broad scaffold endpoints and compatible stressor-to-stability/function wording. No imported RO restriction inferred. Its detailed biological support is outside this audit."
    },
    {
      "index": 3,
      "edge": {
        "subject": "high_temperature",
        "predicate": "increases",
        "object": "membrane_fluidity",
        "description": "High temperature increases membrane permeability and fluidity, creating a limit on growth.",
        "evidence": [
          {
            "reference": "DOI:10.1016/s0300-9629(97)00003-0",
            "snippet": "proton permeability ... increase with the temperature",
            "notes": "Review links increased membrane permeability to upper temperature growth limits."
          }
        ],
        "predicate_id": "RO:0002213"
      },
      "status": "major",
      "assessment": "RO2213 inherits process/process; current hot condition and membrane-fluidity quality do not satisfy those roles."
    },
    {
      "index": 4,
      "edge": {
        "subject": "membrane_fluidity",
        "predicate": "regulates",
        "object": "temperature_preference_trait",
        "description": "Temperature preference reflects the range in which membrane function remains compatible with growth.",
        "evidence": [
          {
            "reference": "DOI:10.1146/annurev-micro-091313-103612",
            "snippet": "optimizes the performance of cellular physiological processes",
            "notes": "Review supports membrane fluidity adaptation as a temperature-sensing and response mechanism."
          }
        ],
        "predicate_id": "RO:0002211"
      },
      "status": "major",
      "assessment": "RO2211 applied to membrane-fluidity QUALITY and temperature-preference TRAIT; both actual referents differ from processes."
    },
    {
      "index": 5,
      "edge": {
        "subject": "protein_stability",
        "predicate": "regulates",
        "object": "temperature_preference_trait",
        "description": "Growth at preferred temperatures requires proteins to remain active and stable.",
        "evidence": [
          {
            "reference": "DOI:10.1128/MMBR.65.1.1-43.2001",
            "snippet": "molecular mechanisms involved in protein thermostabilization",
            "notes": "Supports protein stability as a determinant of high-temperature growth."
          }
        ],
        "predicate_id": "RO:0002211"
      },
      "status": "major",
      "assessment": "RO2211 has an explicit trait object, independently conflicting with process range. Protein-stability function/quality facet remains qualified; no categorical MF exclusion needed for the finding."
    },
    {
      "index": 6,
      "edge": {
        "subject": "fatty_acid_desaturase",
        "predicate": "increases",
        "object": "unsaturated_membrane_fatty_acids",
        "description": "Desaturase expression increases double bonds in membrane fatty acids (homeoviscous adaptation).",
        "evidence": [
          {
            "reference": "DOI:10.1007/s42770-023-01057-4",
            "notes": "Activation of des (desaturase) transcription increases double bonds in membrane fatty acids; generic UFA-biosynthesis module."
          }
        ],
        "predicate_id": "RO:0002213"
      },
      "status": "major",
      "assessment": "RO2213 applied from explicit material desaturase enzyme to material fatty acids. Description mentions expression but current node identity is the protein family, not an expression process. No mechanistic replacement prescribed."
    },
    {
      "index": 7,
      "edge": {
        "subject": "unsaturated_membrane_fatty_acids",
        "predicate": "increases",
        "object": "membrane_fluidity",
        "description": "Increased unsaturated membrane fatty acids restore/raise membrane fluidity.",
        "evidence": [
          {
            "reference": "DOI:10.1007/s42770-023-01057-4",
            "notes": "Increasing double bonds in membrane fatty acids restores membrane fluidity; core homeoviscous-adaptation edge broadly curatable across microbes."
          }
        ],
        "predicate_id": "RO:0002213"
      },
      "status": "major",
      "assessment": "RO2213 applied from material fatty acids to membrane-fluidity QUALITY; process roles fail independently of efficacy."
    },
    {
      "index": 8,
      "edge": {
        "subject": "high_temperature",
        "predicate": "melts",
        "object": "rna_thermometer",
        "description": "Elevated temperature melts RNA thermometer hairpins, relieving translational repression.",
        "evidence": [
          {
            "reference": "DOI:10.1007/s12275-023-00031-x",
            "notes": "RNA thermometers (ROSE/FourU) control translation by occluding Shine-Dalgarno/start codons and melt with temperature; bacterial heat-sensing mechanism."
          }
        ]
      },
      "status": "lexical_only",
      "assessment": "melts has no predicate_id. No imported RO/Biolink domain or range is inferred from the label. Detailed RNA-thermometer efficacy unassessed."
    },
    {
      "index": 9,
      "edge": {
        "subject": "rna_thermometer",
        "predicate": "permits translation of",
        "object": "heat_shock_gene_translation",
        "description": "RNA thermometer melting permits translation of heat-shock genes.",
        "evidence": [
          {
            "reference": "DOI:10.1007/s12275-023-00031-x",
            "notes": "Post-transcriptional RNA thermometers in 5-UTRs mediate rapid temperature-dependent control of translation; strong generic edge."
          }
        ]
      },
      "status": "lexical_only",
      "assessment": "permits translation of has no predicate_id. RNA-to-translation referents are legible; no automatic RO executor inference or detailed efficacy conclusion."
    },
    {
      "index": 10,
      "edge": {
        "subject": "low_temperature",
        "predicate": "induces",
        "object": "cold_shock_rna_chaperone_activity",
        "description": "Cold shock induces CspA-mediated RNA chaperone activity that maintains translatable RNA.",
        "evidence": [
          {
            "reference": "DOI:10.1007/s12275-023-00031-x",
            "notes": "Cold shock induces cold-shock proteins (CspA) that help maintain single-stranded RNA for translation at low temperature."
          }
        ]
      },
      "status": "lexical_only",
      "assessment": "induces has no predicate_id. Low condition/activity referents are preserved; cold-shock wording versus steady low condition is a source/biological qualification, not a new imported-role finding."
    },
    {
      "index": 11,
      "edge": {
        "subject": "temperature_downshift",
        "predicate": "induces",
        "object": "fatty_acid_desaturase",
        "description": "Cold downshift induces fatty-acid desaturase activity to maintain membrane fluidity.",
        "evidence": [
          {
            "reference": "DOI:10.1038/sj.jim.2900572",
            "notes": "Connecting edge wiring the enrichment node into the graph."
          }
        ]
      },
      "status": "lexical_only",
      "assessment": "induces has no predicate_id. Subject describes an actual downshift event; material protein object is not automatically a formal error absent an imported predicate. Detailed regulation support unassessed."
    }
  ],
  "source": [
    {
      "index": 0,
      "field": "causal_graphs[0].edges[0]",
      "subject": "environmental_temperature",
      "predicate": "regulates",
      "object": "growth_rate",
      "source_outcome": "supported",
      "assessment": "Publisher line183 explicitly compares growth rate versus temperature across psychrotrophs, mesophiles and thermophiles; broad phenotype context positive without adopting model parameters.",
      "references": [
        "DOI:10.1038/sj.jim.2900572"
      ]
    },
    {
      "index": 1,
      "field": "causal_graphs[0].edges[1]",
      "subject": "low_temperature",
      "predicate": "decreases",
      "object": "membrane_fluidity",
      "source_outcome": "qualified",
      "assessment": "D’Amico supplied abstract phrase is literal and supports generic reduced fluidity in cold context; detailed transport/survival efficacy unassessed.",
      "references": [
        "DOI:10.1038/sj.embor.7400662"
      ]
    },
    {
      "index": 2,
      "field": "causal_graphs[0].edges[2]",
      "subject": "high_temperature",
      "predicate": "challenges",
      "object": "protein_stability",
      "source_outcome": "qualified",
      "assessment": "Vieille/Zeikus supplied phrase is literal in its abstract and supplies generic high-temperature stability context, not detailed thermostabilization/enhancement efficacy.",
      "references": [
        "DOI:10.1128/MMBR.65.1.1-43.2001"
      ]
    },
    {
      "index": 3,
      "field": "causal_graphs[0].edges[3]",
      "subject": "high_temperature",
      "predicate": "increases",
      "object": "membrane_fluidity",
      "source_outcome": "concern",
      "assessment": "Explicit ellipsis joins source spans rather than a contiguous snippet. The nearest abstract addresses proton permeability and growth limits; permeability and fluidity are distinct properties, so broader direct fluidity attribution remains qualified/unknown, not refuted.",
      "references": [
        "DOI:10.1016/s0300-9629(97)00003-0"
      ]
    },
    {
      "index": 4,
      "field": "causal_graphs[0].edges[4]",
      "subject": "membrane_fluidity",
      "predicate": "regulates",
      "object": "temperature_preference_trait",
      "source_outcome": "concern",
      "assessment": "Mendoza snippet omits intervening words. Generic bilayer/physiological context is positive; exact causal sufficiency for preference is not established by this short phrase.",
      "references": [
        "DOI:10.1146/annurev-micro-091313-103612"
      ]
    },
    {
      "index": 5,
      "field": "causal_graphs[0].edges[5]",
      "subject": "protein_stability",
      "predicate": "regulates",
      "object": "temperature_preference_trait",
      "source_outcome": "qualified",
      "assessment": "Vieille/Zeikus abstract snippet is literal. Broad protein stability context is positive; exact whole-organism necessity/sufficiency and detailed mechanism unassessed.",
      "references": [
        "DOI:10.1128/MMBR.65.1.1-43.2001"
      ]
    },
    {
      "index": 6,
      "field": "causal_graphs[0].edges[6]",
      "subject": "fatty_acid_desaturase",
      "predicate": "increases",
      "object": "unsaturated_membrane_fatty_acids",
      "source_outcome": "UNASSESSED_SCOPE",
      "assessment": "Ramón identity positive; detailed desaturase transcription/stress regulation and efficacy not assessed.",
      "references": [
        "DOI:10.1007/s42770-023-01057-4"
      ]
    },
    {
      "index": 7,
      "field": "causal_graphs[0].edges[7]",
      "subject": "unsaturated_membrane_fatty_acids",
      "predicate": "increases",
      "object": "membrane_fluidity",
      "source_outcome": "qualified",
      "assessment": "Generic unsaturation/fluidity physical direction is consistent with inspected Mendoza context. Broad cross-organism restorative efficacy and detailed source mechanisms remain unassessed.",
      "references": [
        "DOI:10.1007/s42770-023-01057-4"
      ]
    },
    {
      "index": 8,
      "field": "causal_graphs[0].edges[8]",
      "subject": "high_temperature",
      "predicate": "melts",
      "object": "rna_thermometer",
      "source_outcome": "UNASSESSED_SCOPE",
      "assessment": "Moon identity only; detailed RNA thermometer/heat sensing mechanisms not assessed or repaired.",
      "references": [
        "DOI:10.1007/s12275-023-00031-x"
      ]
    },
    {
      "index": 9,
      "field": "causal_graphs[0].edges[9]",
      "subject": "rna_thermometer",
      "predicate": "permits translation of",
      "object": "heat_shock_gene_translation",
      "source_outcome": "UNASSESSED_SCOPE",
      "assessment": "Moon identity only; detailed heat-shock translational control efficacy unassessed.",
      "references": [
        "DOI:10.1007/s12275-023-00031-x"
      ]
    },
    {
      "index": 10,
      "field": "causal_graphs[0].edges[10]",
      "subject": "low_temperature",
      "predicate": "induces",
      "object": "cold_shock_rna_chaperone_activity",
      "source_outcome": "UNASSESSED_SCOPE",
      "assessment": "Moon identity only; detailed cold-shock/RNA-chaperone induction efficacy unassessed.",
      "references": [
        "DOI:10.1007/s12275-023-00031-x"
      ]
    },
    {
      "index": 11,
      "field": "causal_graphs[0].edges[11]",
      "subject": "temperature_downshift",
      "predicate": "induces",
      "object": "fatty_acid_desaturase",
      "source_outcome": "UNASSESSED_SCOPE",
      "assessment": "Dantigny publisher establishes growth-temperature study identity/classification; its detailed support for a desaturase-induction connector is not inspected. No absence or false-source assertion from the available abstract.",
      "references": [
        "DOI:10.1038/sj.jim.2900572"
      ]
    }
  ]
}

### Native checklist: conditional recurrence and record-only fields

ownership: supported. Targets: METPO:1000613.

Formal relation owners are the record, wildcard regulates/decreases/increases mappings and skip-populated grounder. Ordinary replay does not repair current IDs. No exact faulty target payload or snippet writer was demonstrated. The maximal_growth_rate migration does not select current growth_rate; node type and snippets remain record-owned.

### Native checklist: attributable human acceptance

provenance: concern. Targets: METPO:1000613.

Nineteen embedded events comprise eighteen AI events plus a seed; three captured AI context histories were read whole currently. Ignored- and hidden-inclusive search found 204 matching paths, 67 matching-search arrays and 98 all-local arrays, with zero exact current target in all 98. Initial discovery already retained 98; follow-up suspicion of a parser issue did not establish missing arrays. Private or remote acceptance remains unknown.

### Native checklist: bounded catalog and adapter availability

completeness: unknown. Targets: METPO:1000613.

Retained catalog scope distinguishes canonical-name absence from positive source-organism species coverage. No global organism absence, exact-strain or module result follows. Maintained adapter discovery is unavailable in the bounded current environment; generic primary fallback does not supply a membership or efficacy result.

### Native checklist: NONMECHANISTIC scope and optional instances

completeness: supported. Targets: METPO:1000613.

Two components with thirteen nodes and twelve edges do not require invented connectors. One positively grounded protein family and zero instances do not require an accession or detailed mechanism. Canonical quantities and detailed efficacy remain unassessed.

### Native checklist: native checks, baseline and fresh common diagnostics

schema: supported. Targets: METPO:1000613.

Current inspect, focused validation, strict validation and snippet command completed successfully. Existing Tolner native ELLIPTICAL_SNIPPET ERROR remains explicit and scientifically normalized, not erased. B14 common diagnostics retain actual execution intervals, original historical attempts, product skips and omitted full suite; they do not establish scientific correctness.

## Findings

### imported-process-roles: Imported process roles

major / open / confirmed; issue key: temperature-preference-imported-process-roles.

RO:0002211/RO:0002212/RO:0002213 require process-to-process roles; these seven current assertions instead use explicit temperature conditions, qualities, trait, protein or chemicals. Edge 5 trait range is independently decisive despite qualified protein-stability facet.

### growth-rate-facet: Growth rate facet

minor / open / confirmed; issue key: temperature-preference-growth-rate-facet.

The explicit rate of population growth is typed BIOLOGICAL_PROCESS. Its clear label/description preserve the intended quantity, making this bounded type precision rather than uncertain identity. Independent of the regulation-edge issue.

### nonverbatim-source-snippets: Nonverbatim source snippets

minor / open / confirmed; issue key: temperature-preference-nonverbatim-source-snippets.

Tolner uses a marked ellipsis to join separate abstract spans; Mendoza omits intervening words from its actual abstract sentence. These do not satisfy contiguous copied-span presentation. Preserve generic physical meaning and qualify exact-source/version scope; no biological refutation or fabricated-quotation accusation.

### human-acceptance-link: Human acceptance link

minor / open / confirmed; issue key: temperature-preference-human-acceptance-link.

REVIEWED lacks an attributable human acceptance link in the bounded current record/local review/history scope: eighteen AI events plus seed; three captured AI context histories; zero exact target across all 98 current review arrays. Private or remote acceptance remains unknown.

## Recommended Actions And Acceptance Checks

### curate-imported-process-roles

In separately authorized curation reconcile the seven populated process-restricted relation assertions with their preserved condition, quantity, phenotype and material referents. Check conditional regulates/decreases/increases mapping recurrence; ordinary grounder replay skips populated IDs. No exact target-specific faulty payload writer was demonstrated.

- Demonstrate inherited role compatibility for edges 0/1/3/4/5/6/7 without retyping referents merely to fit a predicate.
- Check wildcard mapping rows 11/61/65 against incompatible endpoints and legitimate process controls; preserve skip-populated behavior explicitly.
- Keep local challenges and four lexical-only edges distinct; no operational biological repair or invented connector.
- Run focused strict, relevant predicate/graph checks, full QC and required history/product gates for any authorized changes.

### curate-growth-rate-facet

Align the node 6 declared type with its stated rate attribute while preserving its label/description and assessing incident relation roles separately. The current maximal_growth_rate migration does not select growth_rate; the current record owns this change.

- Type and explicit rate referent agree without invented accession or growth mechanism.
- The imported-role finding remains independently checked; run required guarded-curation validation.

### curate-nonverbatim-source-snippets

In separately authorized curation make each supplied snippet one exact contiguous source span, or move the paraphrase to notes, retaining DOI and selected-source locator. The current record is the demonstrated owner; no exact recurring snippet writer was established.

- Compare final snippets to their identified inspected primary version with only documented whitespace/HTML normalization.
- Keep native ELLIPTICAL_SNIPPET ERROR separate from its normalized review severity and from inconclusive metadata matching.
- Preserve unknown nearest-claim support, permeability/fluidity distinction and unassessed mechanisms; run native snippet and required curation gates.

### curate-human-acceptance-link

Link actual attributable acceptance of the current assertions if available, or qualify review-status provenance accurately. Do not fabricate retrospective sign-off.

- Acceptance evidence identifies the person, exact assertions and disposition, or the remaining uncertainty is explicit.
- Preserve append-only history and run applicable gates for separately authorized curation.

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
| check-temperature-preference-validate | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-validate.log; Executed 2026-10-22T02:36:46.735624+00:00 through 2026-10-22T02:36:47.751013+00:00; metadata temperature-preference-validate.json | context_only | Native record validation passed; scientific interpretation is assessed separately. |
| check-temperature-preference-strict | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-strict.log; Executed 2026-10-22T02:36:46.739354+00:00 through 2026-10-22T02:36:48.259062+00:00; metadata temperature-preference-strict.json | context_only | The actual validate-strict command passed. |
| check-temperature-preference-snippets-network | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-snippets-network.log; Executed 2026-10-22T02:37:03.250614+00:00 through 2026-10-22T02:37:11.711952+00:00; metadata temperature-preference-snippets-network.json | context_only | Native command completed successfully: seven fields across five references, three VERIFIED, two NOT_IN_ABSTRACT and two UNRESOLVED. Misses remain inconclusive. Manual inspection separately found five literal and two noncontiguous snippets; the baselined Tolner ELLIPTICAL_SNIPPET ERROR remains explicit. |
| capture | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference.inspect.json; Actual successful native inspect with 86 captured inputs | context_only | All current source hashes and the exact target are bound before serialization. |
| record | data/traits/environment/temperature_preference.yaml; Whole current record | supports | Thirteen nodes, twelve edges, nineteen embedded events, two canonical examples, one grounded protein family and no instances. |
| local-init | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/batch014-local-initialization-receipt.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Actual local initialization and seventh queue target; publication remains separate. |
| policy | docs/GROUNDING_POLICY.md; Captured maintained authority | supports | Protein family/function grounding and optional protein instances. |
| playbook | docs/CURATION_PLAYBOOK.md; Captured maintained authority | supports | Contiguous copied spans, exact source scope and attributable acceptance. |
| schema | src/traitmech/schema/traitmech.yaml; Captured maintained authority | supports | Current condition, process, molecular activity, quantity and NONMECHANISTIC facets. |
| predicate-mapping | mappings/predicate_grounding.tsv; Captured maintained authority | supports | Conditional wildcard regulates/decreases/increases mappings can populate empty IDs; current populated assertions are skipped. |
| node-mapping | mappings/node_grounding.tsv; Captured maintained authority | supports | Actual node mappings and current applicability, separate from record-only growth-rate type precision. |
| native-ellipsis | conf/evidence_snippet_baseline.tsv; Exact current target Tolner row: ELLIPTICAL_SNIPPET, native ERROR | context_only | Existing diagnostic is preserved. Root normalizes this bounded presentation defect to minor while retaining generic source context and inconclusive metadata misses. |
| identity | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-grounding-agent/identity-assessment.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Active target and parent, positive PATO/local terms and one protein-family grounding. |
| nodes-edges | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-grounding-agent/node-edge-grounding-ledger.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | All thirteen node and twelve edge judgments; growth-rate type precision and seven imported role conflicts. |
| ground-assessment | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-grounding-agent/documentary-assessment.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Grounding contributes one major and two minors; the source audit separately adds its snippet-presentation minor. |
| owners | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-grounding-agent/owner-provenance-assessment.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Record and conditional predicate recurrence owners; no demonstrated exact faulty target payload or snippet writer. |
| owner-primary | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-grounding-agent/owner-primary-reading.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Actual skip-populated predicates and nonapplicable maximal_growth_rate migration; current growth_rate remains record-owned. |
| human-search | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-grounding-agent/search-and-provenance.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Initial ignored- and hidden-inclusive search already retained 98 all-local arrays; matching-path subset has 67. |
| human-search-followup | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-grounding-agent/search-and-provenance-corrected.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Follow-up initially suspected a parser issue, but no all-local array was lost or added. |
| search-clarification | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-grounding-agent/search-count-clarification.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | 204 matching paths, 67 matching-search arrays and 98 all-local arrays; zero exact current target in all 98. |
| histories | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-grounding-agent/history-reading-ledger.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Three current whole captured AI context histories, separate from nineteen embedded events. |
| discovery | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-grounding-agent/discovery-disposition.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Three uncaptured scripts and one sibling history remain matching-line context only. |
| expression | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-grounding-agent/expression-and-readiness.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Canonical exact keys absent and source-organism species keys positive only within the retained catalog; no module or efficacy inference. |
| expression-discovery | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-grounding-agent/expression-runner-current-discovery.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Bounded PATH/project/install discovery found the maintained adapter unavailable. |
| local-authority | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-grounding-agent/local-authority-reading.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Actual local challenges and membrane-fluidity proposals, schema and maintained mapping scope. |
| ground-reading | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-grounding-agent/reading-scope-receipt.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Actual current whole, selected and matching-line scopes; detailed efficacy remains unassessed. |
| ground-manifest | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-grounding-agent/evidence-manifest.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | All 33 frozen grounding artifacts verified. |
| metpo-primary | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/repo/data/raw/metpo.owl; Selected current target and direct parent elements | supports | Active METPO:1000613 identity and METPO:1000059 parent are positive; redundant related-label wording is an upstream qualification. |
| metpo-projection | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-grounding-agent/metpo-authority.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Exact raw source and selected class elements. |
| ontology-primary | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-source-root/selected-ontology-primary.json; Actual root PATO/RO query response, separately read by the grounding auditor | supports | Temperature-quality referents and inherited RO2211/2212/2213 process roles are interpreted without detailed biological efficacy. |
| ontology-provenance | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-grounding-agent/ontology-primary-provenance.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Actual query and current copy clocks; original selected database hash clocks remain separate. |
| pato-primary | /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/pato.db; Previously qualified database bytes; selected query bound by ontology-primary | supports | Recorded authority provenance adopted without a fresh release or duplicate large-database hash claim. |
| ro-primary | /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/ro.db; Previously qualified database bytes; selected query bound by ontology-primary | supports | Recorded authority provenance adopted without a fresh release or duplicate large-database hash claim. |
| tolner-metadata | DOI:10.1016/s0300-9629(97)00003-0; Indexed identity and generic high-temperature abstract | supports | Marked ellipsis is not one contiguous span; permeability remains distinct from fluidity. |
| tolner-crossref | DOI:10.1016/s0300-9629(97)00003-0; Retained Crossref identity | supports | Positive identity separate from original zero-hit DOI search. |
| tolner-author | DOI:10.1016/s0300-9629(97)00003-0; Retained university abstract, not full article | supports | Generic high-temperature/permeability context only. |
| tolner-zero-hit | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016%2Fs0300-9629%2897%2900003-0&amp;format=json&amp;resultType=core; Original indexed response with zero matches | context_only | Retrieval diagnostic with independently positive identity; not a missing-paper finding. |
| damico-metadata | DOI:10.1038/sj.embor.7400662; Indexed identity and supplied physical-context snippet | supports | Supplied low-temperature membrane-fluidity fragment is literal; detailed physiology is unassessed. |
| mendoza-metadata | DOI:10.1146/annurev-micro-091313-103612; Indexed identity and generic physical abstract | supports | Current snippet omits intervening words; generic physical context remains positive. |
| mendoza-publisher | DOI:10.1146/annurev-micro-091313-103612; Retained actual browser abstract export, not raw HTML | supports | Original tool-call interval retained; source spelling and omitted words checked on this surface, with origin cache-fetch time unknown. |
| cold-metadata | DOI:10.1007/s42770-023-01057-4; Indexed identity and bounded notice fields | supports | Review identity positive; detailed cold-stress enzyme and signaling claims unassessed. |
| canonical-cold | DOI:10.1016/j.bbalip.2013.02.004; Indexed article title and identifiers only | supports | Canonical article identity positive; numerical and cultivation support unassessed. |
| canonical-hot | DOI:10.3389/fmicb.2023.1265216; Indexed article title and identifiers only | supports | Canonical article identity positive; numerical, adaptive and cultivation support unassessed. |
| vieille-metadata | DOI:10.1128/MMBR.65.1.1-43.2001; Indexed identity and two supplied abstract fragments | supports | Both current supplied fragments are literal; generic stability context does not establish mechanism-to-preference sufficiency. |
| moon-metadata | DOI:10.1007/s12275-023-00031-x; Indexed title, identifiers and bounded notice fields | supports | Source identity only; detailed proteostasis, survival and defense efficacy unassessed. |
| damico-extraction | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-source-agent/damico-derivation-receipt.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Historical author-repository PDF extraction and exact text hashes are retained; the current supplied snippet is separately checked on indexed metadata, not claimed as a new PDF reading. |
| definition-zero-hit | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038%2Fsj.jim.2900572&amp;format=json&amp;resultType=core; Actual current indexed response with zero matches | context_only | Dantigny identity is established by the actual publisher response, not this zero-hit diagnostic. |
| definition-indexed-access | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-source-agent/definition-metadata-access.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Actual indexed request interval and response hash. |
| definition-publisher | DOI:10.1038/sj.jim.2900572; Actual OUP tool response: selected identity lines and supplied generic classification phrase | supports | Positive title/identity and broad definition context only; no formulas, culture parameters or quantitative model support adopted. Tool response is not raw HTML, and export is distinct from call interval. |
| vieille-body-failure | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC99017/fullTextXML; Historical HTTP500 error bytes, not article XML | context_only | Retained unavailable-body attempt does not refute source content or relabel current indexed snippets. |
| vieille-failure-access | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-source-agent/original-vieille-fulltext-access.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Original historical failed request interval retained separately from current copied evidence. |
| taxonomy-132926 | NCBITaxon:132926; Exact reused official species identity; original successful request interval | supports | Official species identity only; no canonical quantity or cultivation inference. |
| taxonomy-access-132926 | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-grounding-agent/taxon132926-original-access.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Original successful acquisition, distinct from current exact copy and reading. |
| taxonomy-2325 | NCBITaxon:2325; Exact reused official species identity; original successful request interval | supports | Official species identity only; no canonical quantity or cultivation inference. |
| taxonomy-access-2325 | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-grounding-agent/taxon2325-original-access.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Original successful acquisition, distinct from current exact copy and reading. |
| taxonomy-reuse | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-grounding-agent/taxonomy-reuse.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Both original successful official responses and current copies are explicit. |
| taxonomy-reading | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-grounding-agent/taxonomy-identity.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Species identity interpreted separately from unassessed canonical quantities. |
| interpro-primary | InterPro:IPR012171; Fresh successful family metadata retry, not sequence or efficacy data | supports | Current protein-family grounding is positive; no individual protein instance required. |
| interpro-access | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-grounding-agent/interpro-network-retry-access.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Actual successful retry interval and response hash. |
| interpro-reading | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-grounding-agent/interpro-identity.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Bounded family identity reading. |
| interpro-initial-failure | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR012171/; Initial DNS error bytes, not InterPro metadata | context_only | Original failed access is separate from successful retry and from native validation. |
| interpro-failure-access | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-grounding-agent/interpro-access.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Actual initial failed request and error hash. |
| sources | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-source-agent/source-assessment.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Nine works, one bounded source-snippet minor, overall source scope unknown. |
| source-identities | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-source-agent/source-ledger.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | All nine assigned identities with selected and excluded reading scope. |
| source-status | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-source-agent/source-status-ledger.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Original-time response-scoped notice observations, not an exhaustive current publication-status search. |
| placements | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-source-agent/source-placement-ledger.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | All sixteen external placements; thirteen grounding fields are separately covered by node-edge audits. |
| snippets | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-source-agent/snippet-ledger.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Seven supplied snippets: five literal and two noncontiguous, preserving generic physical meaning. |
| notes | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-source-agent/source-note-ledger.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Fifteen notes including singular canonical notes; detailed efficacy and numerical canonical support unassessed. |
| source-nodes-edges | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-source-agent/node-edge-source-ledger.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | All thirteen nodes and twelve edges, retaining unknown nearest support and unassessed details. |
| canonical | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-source-agent/canonical-assessment.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Both article identities positive; numerical, cultivation and adaptive support unassessed. |
| source-reading | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-source-agent/primary-reading-scope.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Selected identity/classification and literal supplied text; no new detailed mechanism or cultivation review. |
| source-access | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-source-agent/source-access-limits.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Successful, unavailable and uninspected source surfaces remain distinct. |
| source-reuse | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-source-agent/source-reuse-receipt.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Twenty exact copies with original access, historical extraction, current copy and reading clocks. |
| source-native | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-source-agent/native-context.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Native three VERIFIED/two NOT_IN_ABSTRACT/two UNRESOLVED versus manual five literal/two noncontiguous. |
| source-manifest | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-source-agent/evidence-manifest.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | All 38 frozen source artifacts verified. |
| root-reading | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-source-root/selected-primary-reading.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Root selected current source/authority reading and precise exclusions; delegated whole history scope is separate. |
| root-verification | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-source-root/root-current-verification.json; Frozen current audit or exact retained receipt; original reading scope controls interpretation | context_only | Root current inputs, frozen artifacts and all 98 actual local review arrays verified. |
| adjudication | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-root-adjudication.json; Revised final root adjudication with original pre-clarification version preserved | supports | Exact one major and three minors, bounded owners/actions, native ERROR normalization and all unknown scopes retained. |

## Limits And Additional Notes

- Full just test was NOT_RUN under the selected review-only diagnostic scope; only the five focused Stage2 tests are recorded. Products retains 123 no-adapter skips. Common checks establish bounded software/data integrity, not scientific support.
- Exact mechanism-to-preference sufficiency and permeability-versus-fluidity source scope remain qualified/unknown.
- Detailed RNA/stress/desaturase regulation, survival/fitness/defense, enzyme/intervention efficacy remain UNASSESSED_SCOPE.
- Both canonical quantitative/cultivation/adaptation claims remain unassessed; metadata/title identity does not validate them.
- Retained metadata notice observations are original-time bounded, not current publication-status refreshes.
- Detailed stress-defense, survival, fitness, RNA regulation, enzyme efficacy, adaptation/cultivation/numerical canonical support and intervention mechanisms UNASSESSED_SCOPE.
- The grounding audit adds no separate source finding; the independent source audit supplies the adopted snippet-presentation minor.
- Only stated current/whole/selected/matching-line scopes adopted; no exact target payload writer invented.
- Private and remote human acceptance unknown.
- Original taxonomy/catalog access clocks and current InterPro retry clocks are retained. The grounding auditor reused pinned database provenance and did not rerun native checks; root focused checks are recorded separately.
- Native snippet check passed with 3 VERIFIED, 2 NOT_IN_ABSTRACT and 2 UNRESOLVED results. Manual selected primary text yields 5 literal and 2 noncontiguous snippets; native results are not rewritten.
- Dantigny OUP browser response supplies positive identity and broad classification. EPMC zero-hit and root DOI tool failure are retrieval diagnostics. Browser response is not raw HTML or whole article; root failure has only export time and no inferred HTTP status.
- Original acquisition, extraction, copy and current reading clocks remain distinct; old notice fields are not refreshed publication status. Initial InterPro DNS failure is retained separately from the successful public API retry.
- Grounding auditor read 3 captured histories whole; root read their actor/target/event-type projections. Search across 204 paths includes ignored/hidden except .git/.venv; 67 matching-search review arrays differ from 98 all-local arrays, all 98 have zero exact targets. Three uncaptured script leads and one sibling history are matching-line context only.
- The maintained expression adapter is unavailable in bounded current discovery. Retained catalog of 20 organisms and 28 datasets has no exact canonical species key; B.subtilis/E.coli species keys do not establish exact strain/module or efficacy. No stress-term query executed.
- The NONMECHANISTIC graph has 2 components, 1 family-grounded protein class and 0 instances; these do not require invented connectors, proteins or datasets.
- Protein-stability function versus property facet remains qualified. PATO low/high temperature condition shorthand is compatible; actual downshift is an event. No automatic CAPACITY or blanket environmental-type error.
- Permeability is distinct from fluidity. Generic physical context and literal snippets do not establish sufficient, exclusive or universal temperature-preference mechanisms.
- Source overall UNKNOWN is retained; one source minor joins grounding findings of 1 major and 2 minors without upgrading unassessed biological claims.
- Growth-rate type precision is minor because label/description preserve intended quantity; role-major remains independently valid.
- Root primary and current verification receipts distinguish direct reading from delegated selected owner/history review.
- Local challenge and fluidity proposal identities are positive; wildcard mappings are conditional recurrence owners, not proof of exact source-writer authorship.
- Historical products failures/retry and original cache provenance remain in /private/tmp/traitmech-record-sweep-014.q8m4v2cs/new-base-diagnostic-independent-review-agent/fresh-products-completion.json. The earlier outstanding-products status is superseded by the actual fresh run; no blanket cross-batch reuse qualification is asserted.
- Final fields, categories, severities, owners and actions come from revised root FINAL. The source snippet minor joins the grounding audit findings; no unassessed biological claim is upgraded.
- This serializer adopts frozen audits and root adjudication. Original acquisitions/extraction, current copies/readings, browser tool intervals/exports and failed/successful requests remain distinct. Serializer preparation is static; root execution and native output validation are separately recorded. No scientific record, state, Git or publication change is performed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T024853Z-temperature-preference
kind: record
repository: CultureBotAI/TraitMech
title: Whole-record review of temperature preference
started_at: '2026-10-22T02:36:26.647389Z'
finished_at: '2026-10-22T02:48:53Z'
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
summary: 'Whole-record review of temperature preference finds one major imported-relation
  role defect across seven edges and three bounded minor findings: rate/process typing,
  noncontiguous source snippets and human-acceptance traceability. Active identity,
  broad definition, parent, family grounding and canonical species identities are
  positive; detailed efficacy and canonical numerical claims remain unassessed.'
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
  - path: data/traits/environment/temperature_preference.yaml
    sha256: 124373347177201d4a2ed44d2d69d1160636e6a99aacc87b4b0ee71e73f0234f
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
  - path: history/infrastructure/node-type-consistency/2026-08-15T014631Z-claude-code-9d7f4d.yaml
    sha256: 21f19561c0d4769e7acc62e05e41d0d395a0f239938f00829f79f2b9c3ac2510
    role: context
  - path: history/infrastructure/protein-vs-activity/2026-08-15T202806Z-claude-code-ddcd62.yaml
    sha256: 58f55f2617869c39eb6412455c0d838b350433ff0ad979c848be1df9bcb3fd4f
    role: context
  - path: history/records/mesophilic/2026-09-04T130000Z-codex-183.yaml
    sha256: 3690075be370a302871b86f5f37fd70776296927d7b98c58d27af10dc2d2cc31
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
  - path: proposals/metpo_traitmech_v3/metpo_proposal_classes_robot.tsv
    sha256: 1a1cc789782cfae195c1fc81ddaf848d06d162c7434d94cceb66838de98ab6fa
    role: context
  - path: proposals/metpo_traitmech_v3/proposal.md
    sha256: 37be7b2c2efe0d1598d62b8df04f08262ba74b9d8068e010df6ee48069449067
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
  - path: research/traits/environment/temperature_preference-deep-research-falcon.md
    sha256: 2d198f87d2ccb7759ae7b9e0653208d945187eb8bed6e6eb046e5d38ca4f8721
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
  - path: scripts/add_thermotaxis_trait.py
    sha256: 37ed0df3824199c227ed98f79d17dbbcce3aff5ea4aea3103444c9c13a6fcf5a
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
  - path: scripts/connect_nacl_optimum_graph_183.py
    sha256: f1608bd82c1323c7d2306268860502ae3483d40f093e055b9b70cd463a1ecf04
    role: context
  - path: scripts/connect_soil_dwelling_graph_183.py
    sha256: 8859ec1a06573e82995d427fa4127d3da5bec6687ededca3d962db42abb052ef
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
  - path: scripts/review_mesophilic_graph_183.py
    sha256: 46f9548808936268217a5e078fc1fa64d74cc2eeb69863ab6f3bb0da21e2b59c
    role: context
  - path: scripts/review_nacl_optimum_graph_183.py
    sha256: 6d0de1ccb1604fb87294432692cc051e3a8a1d52e082eaff6aa1f8d3cb621ffd
    role: context
  - path: scripts/review_obligately_piezophilic_graph_183.py
    sha256: d8fcbbb725162212cfce96bed9800e2cf08374170b7d929a1928248178111efb
    role: context
  - path: scripts/review_ring_shaped_graph_183.py
    sha256: b2bc333efa2af3d0292f6a13bbe69980f9b1990e43fcb32a3d52ff8708008da2
    role: context
  - path: scripts/review_soil_dwelling_graph_183.py
    sha256: 17bcf631620cb26cb0f99d373541f5775e66b1972ec01c4d8df2b29f88338a32
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
- target_id: METPO:1000613
  path: data/traits/environment/temperature_preference.yaml
  label: temperature preference
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_preference.yaml
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
  selection: Seventh record in the actual B14 queue; current 339-line target and 86
    captured inputs. Local review is independent of remote publication.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - METPO:1000613
checks:
- check_id: new-base-qc
  name: Fresh B14 corpus QC
  status: passed
  required: true
  target_ids:
  - METPO:1000613
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
  - METPO:1000613
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
  - METPO:1000613
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
  - METPO:1000613
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
- check_id: temperature-preference-validate
  name: Focused native validation
  status: passed
  required: true
  target_ids:
  - METPO:1000613
  command: just validate data/traits/environment/temperature_preference.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Native record validation passed; scientific interpretation is assessed
    separately.
  evidence_ids:
  - check-temperature-preference-validate
- check_id: temperature-preference-strict
  name: Focused strict validation
  status: passed
  required: true
  target_ids:
  - METPO:1000613
  command: just validate-strict data/traits/environment/temperature_preference.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: The actual validate-strict command passed.
  evidence_ids:
  - check-temperature-preference-strict
- check_id: temperature-preference-snippets-network
  name: Focused network snippet check
  status: passed
  required: true
  target_ids:
  - METPO:1000613
  command: just verify-snippets --record data/traits/environment/temperature_preference.yaml
    --out /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-snippets.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 'Native command completed successfully: seven fields across five references,
    three VERIFIED, two NOT_IN_ABSTRACT and two UNRESOLVED. Misses remain inconclusive.
    Manual inspection separately found five literal and two noncontiguous snippets;
    the baselined Tolner ELLIPTICAL_SNIPPET ERROR remains explicit.'
  evidence_ids:
  - check-temperature-preference-snippets-network
- check_id: native-inspect
  name: One-target native review capture
  status: passed
  required: true
  target_ids:
  - METPO:1000613
  command: uv run python scripts/record_review.py inspect --targets /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference.targets.json
    --input .claude/skills/curate-yaml-record/references/review-checklist.md --input
    .claude/skills/manage-identifiers/SKILL.md --input .claude/skills/review-yaml-record/SKILL.md
    --input CLAUDE.md --input DO_NOT_WORK.md --input conf/evidence_snippet_baseline.tsv
    --input conf/record_review.yaml --input data/raw/biolink-model.yaml --input data/raw/metpo.owl
    --input data/traits/upper/phenotype.yaml --input docs/CURATION_PLAYBOOK.md --input
    docs/GROUNDING_POLICY.md --input docs/PATHWAY_LINKS.md --input docs/record-review-profile.md
    --input docs/record-reviews.md --input history/infrastructure/node-type-consistency/2026-08-15T014631Z-claude-code-9d7f4d.yaml
    --input history/infrastructure/protein-vs-activity/2026-08-15T202806Z-claude-code-ddcd62.yaml
    --input history/records/mesophilic/2026-09-04T130000Z-codex-183.yaml --input justfile
    --input mappings/node_grounding.tsv --input mappings/predicate_grounding.tsv --input
    mappings/trait_exact_match_review.tsv --input mappings/uniprot_regrounding_candidates.tsv
    --input proposals/metpo_traitmech_v2/metpo_proposal_properties_robot.tsv --input
    proposals/metpo_traitmech_v2/proposal.md --input proposals/metpo_traitmech_v3/metpo_proposal_classes_robot.tsv
    --input proposals/metpo_traitmech_v3/proposal.md --input reports/metpo_2026_06_12_active_review.tsv
    --input reports/metpo_2026_06_12_release_delta.tsv --input reports/ontology_snapshot_manifest.tsv
    --input research/traits/environment/temperature_preference-deep-research-falcon.md
    --input schema/record_review.yaml --input scripts/add_cold_shock_response_trait.py
    --input scripts/add_homeoviscous_adaptation_trait.py --input scripts/add_thermotaxis_trait.py
    --input scripts/audit_causal_graphs.py --input scripts/audit_graph_protein_taxa.py
    --input scripts/audit_predicate_domains.py --input scripts/audit_unapplied_groundings.py
    --input scripts/audit_uniprot_grounding.py --input scripts/backfill_canonical_examples_444.py
    --input scripts/connect_mesophilic_graph_183.py --input scripts/connect_nacl_optimum_graph_183.py
    --input scripts/connect_soil_dwelling_graph_183.py --input scripts/connect_temperature_delta_high_graph_183.py
    --input scripts/connect_temperature_delta_very_low_graph_183.py --input scripts/connect_temperature_optimum_high_graph_183.py
    --input scripts/connect_temperature_optimum_very_low_graph_183.py --input scripts/connect_temperature_range_mid3_graph_183.py
    --input scripts/connect_temperature_range_mid4_graph_183.py --input scripts/connect_temperature_range_very_low_graph_183.py
    --input scripts/finalize_metpo_2026_06_12_review.py --input scripts/ground_causal_nodes.py
    --input scripts/ground_causal_predicates.py --input scripts/migrate_disposition_typing.py
    --input scripts/migrate_enables_range_edges.py --input scripts/migrate_enables_trait_edges.py
    --input scripts/migrate_metpo_2026_06_12.py --input scripts/migrate_microbe_domain_edges.py
    --input scripts/migrate_name_match_groundings.py --input scripts/migrate_node_type_consistency.py
    --input scripts/migrate_pathway_vs_process.py --input scripts/migrate_process_quality_consistency.py
    --input scripts/migrate_protein_vs_activity.py --input scripts/migrate_remaining_microbe_domain_edges.py
    --input scripts/migrate_uniprot_instance_groundings.py --input scripts/normalize_homeoviscous_nodes.py
    --input scripts/record_review.py --input scripts/review_mesophilic_graph_183.py
    --input scripts/review_nacl_optimum_graph_183.py --input scripts/review_obligately_piezophilic_graph_183.py
    --input scripts/review_ring_shaped_graph_183.py --input scripts/review_soil_dwelling_graph_183.py
    --input scripts/review_temperature_delta_high_graph_183.py --input scripts/review_temperature_delta_very_low_graph_183.py
    --input scripts/review_temperature_optimum_high_graph_183.py --input scripts/review_temperature_optimum_very_low_graph_183.py
    --input scripts/review_temperature_range_mid3_graph_183.py --input scripts/review_temperature_range_mid4_graph_183.py
    --input scripts/review_temperature_range_very_low_graph_183.py --input scripts/seed_from_metpo.py
    --input scripts/verify_metpo_proposal.py --input src/traitmech/schema/mech_shared.yaml
    --input src/traitmech/schema/traitmech.yaml --input src/traitmech/validation/write_validated.py
  exit_code: 0
  expected_exit_code: 0
  summary: One current target, 86 captured inputs, exact current base and successful
    native inspect.
  evidence_ids:
  - capture
- check_id: uniprot-applicability
  name: Protein-instance metadata applicability
  status: not_applicable
  required: false
  target_ids:
  - METPO:1000613
  summary: One InterPro-grounded protein family and no instances; no accession invented.
  evidence_ids:
  - record
  - policy
  - interpro-primary
- check_id: expression-adapter-availability
  name: Structured source-organism expression query availability
  status: unavailable
  required: false
  target_ids:
  - METPO:1000613
  summary: Maintained adapter unavailable within bounded discovery; retained catalog
    and generic primary context do not supply module membership or efficacy results.
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
- evidence_id: check-temperature-preference-validate
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-validate.log
  locator: Executed 2026-10-22T02:36:46.735624+00:00 through 2026-10-22T02:36:47.751013+00:00;
    metadata temperature-preference-validate.json
  accessed_at: '2026-10-22T02:36:47.751013Z'
  support: context_only
  summary: Native record validation passed; scientific interpretation is assessed
    separately.
  snapshot_sha256: 27dfbc67d34b9c5d9b8e39ae84fed293bc73d0559ab0ad759306acdb73fb0141
- evidence_id: check-temperature-preference-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-strict.log
  locator: Executed 2026-10-22T02:36:46.739354+00:00 through 2026-10-22T02:36:48.259062+00:00;
    metadata temperature-preference-strict.json
  accessed_at: '2026-10-22T02:36:48.259062Z'
  support: context_only
  summary: The actual validate-strict command passed.
  snapshot_sha256: 15c838e2ed93f1ff3e0f31a57b3e792c3bf735278a4895e10bc2dc438f517854
- evidence_id: check-temperature-preference-snippets-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-snippets-network.log
  locator: Executed 2026-10-22T02:37:03.250614+00:00 through 2026-10-22T02:37:11.711952+00:00;
    metadata temperature-preference-snippets-network.json
  accessed_at: '2026-10-22T02:37:11.711952Z'
  support: context_only
  summary: 'Native command completed successfully: seven fields across five references,
    three VERIFIED, two NOT_IN_ABSTRACT and two UNRESOLVED. Misses remain inconclusive.
    Manual inspection separately found five literal and two noncontiguous snippets;
    the baselined Tolner ELLIPTICAL_SNIPPET ERROR remains explicit.'
  snapshot_sha256: 2d6cfc68ab16b9e39d017605ff2ce3a35dcca56cc50ffbaddd528a9d4256fc77
- evidence_id: capture
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference.inspect.json
  locator: Actual successful native inspect with 86 captured inputs
  accessed_at: '2026-10-22T02:36:27.592587Z'
  support: context_only
  summary: All current source hashes and the exact target are bound before serialization.
  snapshot_sha256: 1c4dd8017e0b67d849b15717d8574ee69acf5f524768c6d7c9be9f532dbe3673
- evidence_id: record
  kind: record_content
  reference: data/traits/environment/temperature_preference.yaml
  locator: Whole current record
  accessed_at: '2026-10-22T02:36:27.592587Z'
  support: supports
  summary: Thirteen nodes, twelve edges, nineteen embedded events, two canonical examples,
    one grounded protein family and no instances.
  snapshot_sha256: 124373347177201d4a2ed44d2d69d1160636e6a99aacc87b4b0ee71e73f0234f
- evidence_id: local-init
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/batch014-local-initialization-receipt.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T01:07:39.713898Z'
  support: context_only
  summary: Actual local initialization and seventh queue target; publication remains
    separate.
  snapshot_sha256: 3dade2205affd0bd7eea4b7d5018e8c97080db55bba3620e89cf4a4da4123fa3
- evidence_id: policy
  kind: authority
  reference: docs/GROUNDING_POLICY.md
  locator: Captured maintained authority
  accessed_at: '2026-10-22T02:41:30.337944Z'
  support: supports
  summary: Protein family/function grounding and optional protein instances.
  snapshot_sha256: 891678c983c2283a47c81c47950b35753981e9339d105f3bbdda92a1f5ab7f42
- evidence_id: playbook
  kind: authority
  reference: docs/CURATION_PLAYBOOK.md
  locator: Captured maintained authority
  accessed_at: '2026-10-22T02:41:30.337944Z'
  support: supports
  summary: Contiguous copied spans, exact source scope and attributable acceptance.
  snapshot_sha256: 735e9b810471da9f7d8364e35ffe1e741edb3421480dac01727db6ea5aa65da9
- evidence_id: schema
  kind: authority
  reference: src/traitmech/schema/traitmech.yaml
  locator: Captured maintained authority
  accessed_at: '2026-10-22T02:41:30.337944Z'
  support: supports
  summary: Current condition, process, molecular activity, quantity and NONMECHANISTIC
    facets.
  snapshot_sha256: 46c47fc627b80ccbba1e8ab3fb6f2aee93bc2aef7aaf72fe9aadc3257f2c02dd
- evidence_id: predicate-mapping
  kind: authority
  reference: mappings/predicate_grounding.tsv
  locator: Captured maintained authority
  accessed_at: '2026-10-22T02:41:30.337944Z'
  support: supports
  summary: Conditional wildcard regulates/decreases/increases mappings can populate
    empty IDs; current populated assertions are skipped.
  snapshot_sha256: 8e28c19e93aca3dc164a3befbe2612b289241de457c59f499e65936c03b7ce52
- evidence_id: node-mapping
  kind: authority
  reference: mappings/node_grounding.tsv
  locator: Captured maintained authority
  accessed_at: '2026-10-22T02:41:30.337944Z'
  support: supports
  summary: Actual node mappings and current applicability, separate from record-only
    growth-rate type precision.
  snapshot_sha256: d7de9b3ab04960c4775a5bc295a945bd1a72d81467830459f4793e654f82b3d0
- evidence_id: native-ellipsis
  kind: validation
  reference: conf/evidence_snippet_baseline.tsv
  locator: 'Exact current target Tolner row: ELLIPTICAL_SNIPPET, native ERROR'
  accessed_at: '2026-10-22T02:36:27.592587Z'
  support: context_only
  summary: Existing diagnostic is preserved. Root normalizes this bounded presentation
    defect to minor while retaining generic source context and inconclusive metadata
    misses.
  snapshot_sha256: cbe5c82379e796446366b292f15194d80625b928119b482a67d857a379ab31a7
- evidence_id: identity
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-grounding-agent/identity-assessment.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:41:30.337944Z'
  support: context_only
  summary: Active target and parent, positive PATO/local terms and one protein-family
    grounding.
  snapshot_sha256: 9861717d251410fa33c937b5c58b42eb3b2441e736ad565014fe9859943e95c2
- evidence_id: nodes-edges
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-grounding-agent/node-edge-grounding-ledger.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:41:30.337944Z'
  support: context_only
  summary: All thirteen node and twelve edge judgments; growth-rate type precision
    and seven imported role conflicts.
  snapshot_sha256: da72c9a21f4c9e8afb3f8e2c57a39b143592bbf99aa7db71edc0896a36021dec
- evidence_id: ground-assessment
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-grounding-agent/documentary-assessment.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:41:30.337944Z'
  support: context_only
  summary: Grounding contributes one major and two minors; the source audit separately
    adds its snippet-presentation minor.
  snapshot_sha256: e6afd03f4ca96bc9c179a015077ac2f22f7e4cba70a7490f0ceb436966b7fcda
- evidence_id: owners
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-grounding-agent/owner-provenance-assessment.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:41:30.337944Z'
  support: context_only
  summary: Record and conditional predicate recurrence owners; no demonstrated exact
    faulty target payload or snippet writer.
  snapshot_sha256: b24dd50c3120a0496e791aade1d78b8a0d865da2afef21c9fd7c45e1763cdf65
- evidence_id: owner-primary
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-grounding-agent/owner-primary-reading.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:40:04.192945Z'
  support: context_only
  summary: Actual skip-populated predicates and nonapplicable maximal_growth_rate
    migration; current growth_rate remains record-owned.
  snapshot_sha256: 67a9ab3f99f7d6c29ba3efa8be7a17605408de807d8dedc37c8086d8b0a618fa
- evidence_id: human-search
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-grounding-agent/search-and-provenance.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:38:23.311445Z'
  support: context_only
  summary: Initial ignored- and hidden-inclusive search already retained 98 all-local
    arrays; matching-path subset has 67.
  snapshot_sha256: 0f146dd435f75d17bcde53126a2ffa261fb74b8ffcacfde632ab4f8e34e3b55b
- evidence_id: human-search-followup
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-grounding-agent/search-and-provenance-corrected.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:38:23.311445Z'
  support: context_only
  summary: Follow-up initially suspected a parser issue, but no all-local array was
    lost or added.
  snapshot_sha256: 5d22ce35c5dc4a67f490836ddd69dd6fa717f58640cdbf39c5f553d19992377f
- evidence_id: search-clarification
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-grounding-agent/search-count-clarification.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:39:25.176720Z'
  support: context_only
  summary: 204 matching paths, 67 matching-search arrays and 98 all-local arrays;
    zero exact current target in all 98.
  snapshot_sha256: 239b58ae12cb3d2b043040a95e5443e6e4a703fd5b637b0112c5995f9c988ea5
- evidence_id: histories
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-grounding-agent/history-reading-ledger.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:41:30.337944Z'
  support: context_only
  summary: Three current whole captured AI context histories, separate from nineteen
    embedded events.
  snapshot_sha256: 2b12a634baafd11aafdb3ab35be066ce6ef22cda6e6c7f1833da2764d578a9fb
- evidence_id: discovery
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-grounding-agent/discovery-disposition.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:41:30.337944Z'
  support: context_only
  summary: Three uncaptured scripts and one sibling history remain matching-line context
    only.
  snapshot_sha256: 3f942d424e9ffe0501a83ceab54d58234b1cf1cbe60f2e4b511d4d8135f93c44
- evidence_id: expression
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-grounding-agent/expression-and-readiness.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:41:30.337944Z'
  support: context_only
  summary: Canonical exact keys absent and source-organism species keys positive only
    within the retained catalog; no module or efficacy inference.
  snapshot_sha256: 549b497081b676daa876e0b817700491bd2f0a15f7c5d06068d3942e44a049a1
- evidence_id: expression-discovery
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-grounding-agent/expression-runner-current-discovery.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:40:04.291890Z'
  support: context_only
  summary: Bounded PATH/project/install discovery found the maintained adapter unavailable.
  snapshot_sha256: 39f6490966e6498bc64840598463565f1c1e8fc7aa7f8b7757d67156db2df552
- evidence_id: local-authority
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-grounding-agent/local-authority-reading.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:40:04.191249Z'
  support: context_only
  summary: Actual local challenges and membrane-fluidity proposals, schema and maintained
    mapping scope.
  snapshot_sha256: 1d64f7c82d6b522e8af88e0d12a1fb095c740b46d3c12c358ad5ba354308e935
- evidence_id: ground-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-grounding-agent/reading-scope-receipt.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:41:30.344164Z'
  support: context_only
  summary: Actual current whole, selected and matching-line scopes; detailed efficacy
    remains unassessed.
  snapshot_sha256: 1a4dda8dd779c33af89e56a1b2a0c464c1879225d73230bc3e098d90e129c506
- evidence_id: ground-manifest
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-grounding-agent/evidence-manifest.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:41:30.347624Z'
  support: context_only
  summary: All 33 frozen grounding artifacts verified.
  snapshot_sha256: 58449eaae054dc2876172ec5e59e6bdd8b52e907bcff1bdb8e25231174e73416
- evidence_id: metpo-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/repo/data/raw/metpo.owl
  locator: Selected current target and direct parent elements
  accessed_at: '2026-10-22T02:37:20.146421Z'
  support: supports
  summary: Active METPO:1000613 identity and METPO:1000059 parent are positive; redundant
    related-label wording is an upstream qualification.
  snapshot_sha256: 8b6f8fe0510a698579e532658c8ace05da2550093365df9ca83feb0741778415
- evidence_id: metpo-projection
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-grounding-agent/metpo-authority.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:37:20.146421Z'
  support: context_only
  summary: Exact raw source and selected class elements.
  snapshot_sha256: 5c40d8ab4dfb422b1b1da5856c794be77145a1f8fd0a94bf0a8a12b5b006aff1
- evidence_id: ontology-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-source-root/selected-ontology-primary.json
  locator: Actual root PATO/RO query response, separately read by the grounding auditor
  accessed_at: '2026-10-22T02:37:17.512564Z'
  support: supports
  summary: Temperature-quality referents and inherited RO2211/2212/2213 process roles
    are interpreted without detailed biological efficacy.
  snapshot_sha256: 074e3e6d2175810c6cb9558bc390c912ba01e56b4a150e66d790a56019e734fe
- evidence_id: ontology-provenance
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-grounding-agent/ontology-primary-provenance.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:40:04.189201Z'
  support: context_only
  summary: Actual query and current copy clocks; original selected database hash clocks
    remain separate.
  snapshot_sha256: e213148fb4b1499cbc5c763818d54b6a635d7d01673635079654b1927b9062d0
- evidence_id: pato-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/pato.db
  locator: Previously qualified database bytes; selected query bound by ontology-primary
  accessed_at: '2026-10-22T02:37:17.512564Z'
  support: supports
  summary: Recorded authority provenance adopted without a fresh release or duplicate
    large-database hash claim.
  snapshot_sha256: 179ab512b5c3a8827c74e2a496da575e2908a84740429deef265d58c9ce61d3b
- evidence_id: ro-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/ro.db
  locator: Previously qualified database bytes; selected query bound by ontology-primary
  accessed_at: '2026-10-22T02:37:17.512564Z'
  support: supports
  summary: Recorded authority provenance adopted without a fresh release or duplicate
    large-database hash claim.
  snapshot_sha256: 849e616c29fecd0d4a6c6dee0dc0f6f117ace7167dbfa1e0f043dc84868f83cb
- evidence_id: tolner-metadata
  kind: primary_source
  reference: DOI:10.1016/s0300-9629(97)00003-0
  locator: Indexed identity and generic high-temperature abstract
  accessed_at: '2026-10-21T09:29:01.331044Z'
  support: supports
  summary: Marked ellipsis is not one contiguous span; permeability remains distinct
    from fluidity.
  snapshot_sha256: 56f69a7ce2e69822ef753fec5c43716583184e45fc1a2c0cae98aa9bdb841265
- evidence_id: tolner-crossref
  kind: primary_source
  reference: DOI:10.1016/s0300-9629(97)00003-0
  locator: Retained Crossref identity
  accessed_at: '2026-10-21T09:27:49.120434Z'
  support: supports
  summary: Positive identity separate from original zero-hit DOI search.
  snapshot_sha256: 6f0a5c9b3558992f0f75d1861225410727bededc63928e7a72e1762170d34349
- evidence_id: tolner-author
  kind: primary_source
  reference: DOI:10.1016/s0300-9629(97)00003-0
  locator: Retained university abstract, not full article
  accessed_at: '2026-10-21T09:29:00.791083Z'
  support: supports
  summary: Generic high-temperature/permeability context only.
  snapshot_sha256: 3c475aae5c42532ff36e66a262fe2d6a9c6fc8b64aa6576d93efdc96cada4134
- evidence_id: tolner-zero-hit
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016%2Fs0300-9629%2897%2900003-0&format=json&resultType=core
  locator: Original indexed response with zero matches
  accessed_at: '2026-10-21T09:25:49.176885Z'
  support: context_only
  summary: Retrieval diagnostic with independently positive identity; not a missing-paper
    finding.
  snapshot_sha256: 25e3cf6616503721ec087dd147e11ac038f8834891e32d704a1f67074095c9cc
- evidence_id: damico-metadata
  kind: primary_source
  reference: DOI:10.1038/sj.embor.7400662
  locator: Indexed identity and supplied physical-context snippet
  accessed_at: '2026-10-21T10:00:01.461116Z'
  support: supports
  summary: Supplied low-temperature membrane-fluidity fragment is literal; detailed
    physiology is unassessed.
  snapshot_sha256: 24d64254a2baba7c573dff7ae523cc0e00d30e297c4f1fd7aa3a23c51a057059
- evidence_id: mendoza-metadata
  kind: primary_source
  reference: DOI:10.1146/annurev-micro-091313-103612
  locator: Indexed identity and generic physical abstract
  accessed_at: '2026-10-21T10:00:02.042457Z'
  support: supports
  summary: Current snippet omits intervening words; generic physical context remains
    positive.
  snapshot_sha256: 801da630644a181211f991a6f21c49b178e42a65f615c4eebd8196bc29244588
- evidence_id: mendoza-publisher
  kind: primary_source
  reference: DOI:10.1146/annurev-micro-091313-103612
  locator: Retained actual browser abstract export, not raw HTML
  accessed_at: '2026-10-21T23:38:35Z'
  support: supports
  summary: Original tool-call interval retained; source spelling and omitted words
    checked on this surface, with origin cache-fetch time unknown.
  snapshot_sha256: b8635235ad5e362d0b33ef4834f84eb25fe7ff6b1bd1321affb2b61cecbc66fc
- evidence_id: cold-metadata
  kind: primary_source
  reference: DOI:10.1007/s42770-023-01057-4
  locator: Indexed identity and bounded notice fields
  accessed_at: '2026-10-21T22:07:08.865512Z'
  support: supports
  summary: Review identity positive; detailed cold-stress enzyme and signaling claims
    unassessed.
  snapshot_sha256: da5cffab81fe0e039c6fcec8f318b2715f5604eaf8722ea6f63f944178ed447b
- evidence_id: canonical-cold
  kind: primary_source
  reference: DOI:10.1016/j.bbalip.2013.02.004
  locator: Indexed article title and identifiers only
  accessed_at: '2026-10-22T02:05:32.923541Z'
  support: supports
  summary: Canonical article identity positive; numerical and cultivation support
    unassessed.
  snapshot_sha256: 9f35081f59b689b6b577f9fa11ff84bac7ba2cc25ba562cddfce84d512203212
- evidence_id: canonical-hot
  kind: primary_source
  reference: DOI:10.3389/fmicb.2023.1265216
  locator: Indexed article title and identifiers only
  accessed_at: '2026-10-22T02:23:07.149167Z'
  support: supports
  summary: Canonical article identity positive; numerical, adaptive and cultivation
    support unassessed.
  snapshot_sha256: 2baef05efc8e4e8841706630e7436ebbf1e5945e6c435e4ca90c8f8385e92313
- evidence_id: vieille-metadata
  kind: primary_source
  reference: DOI:10.1128/MMBR.65.1.1-43.2001
  locator: Indexed identity and two supplied abstract fragments
  accessed_at: '2026-10-21T11:23:22.820553Z'
  support: supports
  summary: Both current supplied fragments are literal; generic stability context
    does not establish mechanism-to-preference sufficiency.
  snapshot_sha256: 7fbda4bf0eea7b0c1641d88dc150329587687249fd800726e14b7f84a9670e0c
- evidence_id: moon-metadata
  kind: primary_source
  reference: DOI:10.1007/s12275-023-00031-x
  locator: Indexed title, identifiers and bounded notice fields
  accessed_at: '2026-10-21T09:25:42.394675Z'
  support: supports
  summary: Source identity only; detailed proteostasis, survival and defense efficacy
    unassessed.
  snapshot_sha256: c4ed17a04c2e85dfe16fee756b0f5347ae4599d17fc03622f63ff7c84a1ff8aa
- evidence_id: damico-extraction
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-source-agent/damico-derivation-receipt.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-21T21:57:11.990598Z'
  support: context_only
  summary: Historical author-repository PDF extraction and exact text hashes are retained;
    the current supplied snippet is separately checked on indexed metadata, not claimed
    as a new PDF reading.
  snapshot_sha256: 4bc68e1e7c942f28f8b2be82ef5b82e45461cdec22ed95828753130bc433d1ac
- evidence_id: definition-zero-hit
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038%2Fsj.jim.2900572&format=json&resultType=core
  locator: Actual current indexed response with zero matches
  accessed_at: '2026-10-22T02:37:13.691553Z'
  support: context_only
  summary: Dantigny identity is established by the actual publisher response, not
    this zero-hit diagnostic.
  snapshot_sha256: c9189314da71deb66d1df57f1f29499b905fe0c16501c46417795672d8df5efa
- evidence_id: definition-indexed-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-source-agent/definition-metadata-access.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:37:13.691553Z'
  support: context_only
  summary: Actual indexed request interval and response hash.
  snapshot_sha256: fe8de0dcd5ccefba5f20baf802995130dbce6b3b02e9e5835f1f5ff084c1a38f
- evidence_id: definition-publisher
  kind: primary_source
  reference: DOI:10.1038/sj.jim.2900572
  locator: 'Actual OUP tool response: selected identity lines and supplied generic
    classification phrase'
  accessed_at: '2026-10-22T02:37:36Z'
  support: supports
  summary: Positive title/identity and broad definition context only; no formulas,
    culture parameters or quantitative model support adopted. Tool response is not
    raw HTML, and export is distinct from call interval.
  snapshot_sha256: b142a9391a8057738c8a2575c92f92b79976563c74df63e4ef3dda8b67332967
- evidence_id: vieille-body-failure
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC99017/fullTextXML
  locator: Historical HTTP500 error bytes, not article XML
  accessed_at: '2026-10-21T23:40:25.832769Z'
  support: context_only
  summary: Retained unavailable-body attempt does not refute source content or relabel
    current indexed snippets.
  snapshot_sha256: e0e941acc188eeea39928336d9947cc59e8719064066ceb596a11ed6a5c76c84
- evidence_id: vieille-failure-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-source-agent/original-vieille-fulltext-access.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-21T23:40:25.832769Z'
  support: context_only
  summary: Original historical failed request interval retained separately from current
    copied evidence.
  snapshot_sha256: 1dd82389bc0ff2304794ed34129e6bdf6b58742659d4a5ba3423bb92f7577eb0
- evidence_id: taxonomy-132926
  kind: authority
  reference: NCBITaxon:132926
  locator: Exact reused official species identity; original successful request interval
  accessed_at: '2026-10-22T02:04:25.623269Z'
  support: supports
  summary: Official species identity only; no canonical quantity or cultivation inference.
  snapshot_sha256: 245bd094ae1de7aaee89438775af8f35f40f78f3e169e0ea6d102f92383f32bf
- evidence_id: taxonomy-access-132926
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-grounding-agent/taxon132926-original-access.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:04:25.623269Z'
  support: context_only
  summary: Original successful acquisition, distinct from current exact copy and reading.
  snapshot_sha256: 5da31b4dccb36881557591a25a60cc44c9b58db2a6408a08b784bbee8c1d371b
- evidence_id: taxonomy-2325
  kind: authority
  reference: NCBITaxon:2325
  locator: Exact reused official species identity; original successful request interval
  accessed_at: '2026-10-22T02:23:33.918490Z'
  support: supports
  summary: Official species identity only; no canonical quantity or cultivation inference.
  snapshot_sha256: 37c6c31fb7118bf97ce378e10ed5be6fdf21ab68f3d00936a190162f581b8d77
- evidence_id: taxonomy-access-2325
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-grounding-agent/taxon2325-original-access.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:23:33.918490Z'
  support: context_only
  summary: Original successful acquisition, distinct from current exact copy and reading.
  snapshot_sha256: 1297076321414c185dd51b65b3daf2022a1f252cf9096e66c21e3e88f5dac994
- evidence_id: taxonomy-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-grounding-agent/taxonomy-reuse.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:38:27.265359Z'
  support: context_only
  summary: Both original successful official responses and current copies are explicit.
  snapshot_sha256: c1b0349d338456e1520ef1250efd184c90a084fc061dc0b23fa9fc423ca7510c
- evidence_id: taxonomy-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-grounding-agent/taxonomy-identity.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:38:27.265460Z'
  support: context_only
  summary: Species identity interpreted separately from unassessed canonical quantities.
  snapshot_sha256: 43e2ad984d5f8748306e7c7b483590cb0f9140f607be388d1637279d85170bd4
- evidence_id: interpro-primary
  kind: authority
  reference: InterPro:IPR012171
  locator: Fresh successful family metadata retry, not sequence or efficacy data
  accessed_at: '2026-10-22T02:37:44.576021Z'
  support: supports
  summary: Current protein-family grounding is positive; no individual protein instance
    required.
  snapshot_sha256: 2b020d14032d9e5d407930c7328235ec9f849a1792d3b3a158f8820369281233
- evidence_id: interpro-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-grounding-agent/interpro-network-retry-access.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:37:44.576021Z'
  support: context_only
  summary: Actual successful retry interval and response hash.
  snapshot_sha256: fdac0ba5dc629b7b208551a758a1788bdbfaa06d19ad408cb2c9ea31a814c5d6
- evidence_id: interpro-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-grounding-agent/interpro-identity.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:41:30.337944Z'
  support: context_only
  summary: Bounded family identity reading.
  snapshot_sha256: 8fa2646bf1c5d11ca96ac37bc7ea490e2c1e55a3327cff92de9c57d59882b899
- evidence_id: interpro-initial-failure
  kind: validation
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR012171/
  locator: Initial DNS error bytes, not InterPro metadata
  accessed_at: '2026-10-22T02:37:20.104259Z'
  support: context_only
  summary: Original failed access is separate from successful retry and from native
    validation.
  snapshot_sha256: 35281279d8e2164cee8666d6f8aad891326911e887ab1b2ab778c8ac6d09dc6c
- evidence_id: interpro-failure-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-grounding-agent/interpro-access.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:37:20.104259Z'
  support: context_only
  summary: Actual initial failed request and error hash.
  snapshot_sha256: a73e9348041903cab1160b3bb4a0175a3ed5a55342170ec1db28eae1750bb974
- evidence_id: sources
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-source-agent/source-assessment.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:39:36.371347Z'
  support: context_only
  summary: Nine works, one bounded source-snippet minor, overall source scope unknown.
  snapshot_sha256: 049f2a43582b2be7d565b47fc52fa0859a0f8bc2ff099c544053e1f5a205ddbb
- evidence_id: source-identities
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-source-agent/source-ledger.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:39:36.367718Z'
  support: context_only
  summary: All nine assigned identities with selected and excluded reading scope.
  snapshot_sha256: 9cb388f11ff3dc28585ea2b9d18d063c681fe7faaef3ea790bf5372c81291322
- evidence_id: source-status
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-source-agent/source-status-ledger.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:39:36.371028Z'
  support: context_only
  summary: Original-time response-scoped notice observations, not an exhaustive current
    publication-status search.
  snapshot_sha256: 25370fbd9b0a488534d4f638ab72a35a385f1e7f761d315f31cf7c1a32431067
- evidence_id: placements
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-source-agent/source-placement-ledger.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:39:36.369265Z'
  support: context_only
  summary: All sixteen external placements; thirteen grounding fields are separately
    covered by node-edge audits.
  snapshot_sha256: 99ceb305eab78153430e8cd34480b22025f1498d78161fc37d5c667caf19c3eb
- evidence_id: snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-source-agent/snippet-ledger.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:39:36.368977Z'
  support: context_only
  summary: 'Seven supplied snippets: five literal and two noncontiguous, preserving
    generic physical meaning.'
  snapshot_sha256: f521885ae38287e1a7a3328035f593ee1c7131885916ab7e780d6320e670c123
- evidence_id: notes
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-source-agent/source-note-ledger.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:39:36.369421Z'
  support: context_only
  summary: Fifteen notes including singular canonical notes; detailed efficacy and
    numerical canonical support unassessed.
  snapshot_sha256: 6ec4dc2ee0da112e1765120441bcd35306879b3ca92c404fd065e2f965e2db55
- evidence_id: source-nodes-edges
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-source-agent/node-edge-source-ledger.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:39:36.369532Z'
  support: context_only
  summary: All thirteen nodes and twelve edges, retaining unknown nearest support
    and unassessed details.
  snapshot_sha256: c6345256a07cddab85cd684ef83f70816b25748fb64bd67e5fd6d3bfac273f23
- evidence_id: canonical
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-source-agent/canonical-assessment.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:39:36.369711Z'
  support: context_only
  summary: Both article identities positive; numerical, cultivation and adaptive support
    unassessed.
  snapshot_sha256: 97444d2b692c69246e717eed9cbfe5c5cd6e2915dc1978bf8ddc25e1c4015dfe
- evidence_id: source-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-source-agent/primary-reading-scope.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:39:36.371209Z'
  support: context_only
  summary: Selected identity/classification and literal supplied text; no new detailed
    mechanism or cultivation review.
  snapshot_sha256: 365fd17679a51c2198688d7add01f44a7473d0082d790b863593996c0471f870
- evidence_id: source-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-source-agent/source-access-limits.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:39:36.371126Z'
  support: context_only
  summary: Successful, unavailable and uninspected source surfaces remain distinct.
  snapshot_sha256: 7ff7a42561dc4edff74776b4861e43844c8622b11eab8eea0da3f5af804199b2
- evidence_id: source-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-source-agent/source-reuse-receipt.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:37:10.377352Z'
  support: context_only
  summary: Twenty exact copies with original access, historical extraction, current
    copy and reading clocks.
  snapshot_sha256: 8d8fb7b6930aa40dfbb54605abdab5eaf50f3c00df23904c80338f8865b0b17e
- evidence_id: source-native
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-source-agent/native-context.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:39:36.370721Z'
  support: context_only
  summary: Native three VERIFIED/two NOT_IN_ABSTRACT/two UNRESOLVED versus manual
    five literal/two noncontiguous.
  snapshot_sha256: 547589ec2c8987631a713ae9f12b5122a388cd871adfe664700f4ec5eb419f81
- evidence_id: source-manifest
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-source-agent/evidence-manifest.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:39:36.371488Z'
  support: context_only
  summary: All 38 frozen source artifacts verified.
  snapshot_sha256: 3a1e4e599c84dc1e91f77a95007816c566552c5ccef795e38a9a6a76805d37c8
- evidence_id: root-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-source-root/selected-primary-reading.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:38:34.088421Z'
  support: context_only
  summary: Root selected current source/authority reading and precise exclusions;
    delegated whole history scope is separate.
  snapshot_sha256: 15806cc07a0ee16322f15f8c3939d4a9b2a32629682a47bd8f8eef9772e0e152
- evidence_id: root-verification
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-source-root/root-current-verification.json
  locator: Frozen current audit or exact retained receipt; original reading scope
    controls interpretation
  accessed_at: '2026-10-22T02:42:36.448294Z'
  support: context_only
  summary: Root current inputs, frozen artifacts and all 98 actual local review arrays
    verified.
  snapshot_sha256: b6e24fb51fe856c13530819f5b170317ca962f636d93bda69279cd2aad6977b9
- evidence_id: adjudication
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-preference-root-adjudication.json
  locator: Revised final root adjudication with original pre-clarification version
    preserved
  accessed_at: '2026-10-22T02:43:28.995689Z'
  support: supports
  summary: Exact one major and three minors, bounded owners/actions, native ERROR
    normalization and all unknown scopes retained.
  snapshot_sha256: 3ded16d17c726968973d115ec55b5ff915e9e9e98139e798bcc342d1c0c22802
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: active target, parent and local authorities'
  outcome: supported
  target_ids:
  - METPO:1000613
  summary: Active METPO:1000613 identity and METPO:1000059 parent are positive. Local
    challenges and membrane-fluidity terms are positive; redundant related-label wording
    remains an upstream qualification, not a forced identifier change.
  evidence_ids:
  - identity
  - metpo-primary
  - metpo-projection
  - local-authority
  - record
- assessment_id: definition
  area: quantity
  topic: 'Native checklist: broad temperature preference classification'
  outcome: supported
  target_ids:
  - METPO:1000613
  summary: Dantigny publisher identity and the supplied generic classification phrase
    support the broad definition. Its successful publisher response is distinct from
    a zero-hit indexed lookup. No quantitative model, growth parameters or exhaustive
    phenotype support is adopted.
  evidence_ids:
  - sources
  - placements
  - source-identities
  - definition-publisher
  - definition-zero-hit
  - metpo-primary
- assessment_id: canonical
  area: quantity
  topic: 'Native checklist: species and article identity versus numerical support'
  outcome: unknown
  target_ids:
  - METPO:1000613
  summary: Both official species and assigned article identities are positive. Canonical
    quantities, cultivation, adaptation and optimization support remain UNASSESSED_SCOPE;
    title-level identity does not verify or refute those notes.
  evidence_ids:
  - canonical
  - canonical-cold
  - canonical-hot
  - taxonomy-132926
  - taxonomy-2325
  - taxonomy-reading
- assessment_id: source-support
  area: evidence
  topic: 'Native checklist: nine works and sixteen placements'
  outcome: unknown
  target_ids:
  - METPO:1000613
  summary: All nine source identities resolve. Generic physical context and supplied
    literal spans do not establish exact mechanism-to-preference sufficiency. Permeability
    is distinct from fluidity. Detailed RNA/stress/desaturase regulation, survival,
    fitness, defense, enzyme/intervention efficacy and canonical numerical/cultivation
    support remain UNASSESSED_SCOPE.
  evidence_ids:
  - sources
  - source-identities
  - source-status
  - placements
  - notes
  - source-reading
  - source-access
  - tolner-metadata
  - mendoza-metadata
  - vieille-metadata
- assessment_id: quotations
  area: evidence
  topic: 'Native checklist: seven supplied snippets and original native severity'
  outcome: concern
  target_ids:
  - METPO:1000613
  summary: Manual inspection found five literal snippets and two noncontiguous presentations.
    Tolner joins spans with a marked ellipsis; Mendoza omits intervening words. Preserve
    Tolner native ELLIPTICAL_SNIPPET ERROR, normalized here to a minor copied-span
    finding because generic context remains supported. Native three VERIFIED, two
    NOT_IN_ABSTRACT and two UNRESOLVED remain separate; misses are inconclusive, not
    biological refutations.
  evidence_ids:
  - snippets
  - source-native
  - native-ellipsis
  - notes
  - tolner-metadata
  - mendoza-metadata
  - mendoza-publisher
  - damico-metadata
  - adjudication
- assessment_id: nodes
  area: representation
  topic: 'Native checklist: all thirteen current referents'
  outcome: concern
  target_ids:
  - METPO:1000613
  summary: 'The explicit growth-rate attribute is typed as a process: a bounded node
    6 precision minor. Protein-stability wording remains qualified, without forced
    capacity retyping. Downshift may denote an event, cold-shock chaperone activity
    is a molecular activity, and the protein family has positive InterPro identity.'
  evidence_ids:
  - nodes-edges
  - source-nodes-edges
  - schema
  - local-authority
  - policy
  - pato-primary
  - interpro-primary
  - adjudication
  details: "{\n  \"grounding\": [\n    {\n      \"index\": 0,\n      \"node\": {\n\
    \        \"node_id\": \"temperature_preference_trait\",\n        \"label\": \"\
    temperature preference\",\n        \"node_type\": \"TRAIT\",\n        \"grounding\"\
    : \"METPO:1000613\",\n        \"description\": \"Growth phenotype characterized\
    \ by preferred environmental temperature.\"\n      },\n      \"status\": \"supported\"\
    ,\n      \"assessment\": \"Trait class exact active identity; broad preferred-temperature\
    \ phenotype.\"\n    },\n    {\n      \"index\": 1,\n      \"node\": {\n      \
    \  \"node_id\": \"environmental_temperature\",\n        \"label\": \"environmental\
    \ temperature\",\n        \"node_type\": \"ENVIRONMENTAL_FACTOR\",\n        \"\
    description\": \"Growth temperature experienced by the organism.\"\n      },\n\
    \      \"status\": \"supported\",\n      \"assessment\": \"Environmental growth-temperature\
    \ condition/axis, not explicitly a temperature-change process. ENVIRONMENTAL_FACTOR\
    \ is appropriate; this condition does not satisfy imported RO process roles merely\
    \ because it influences growth.\"\n    },\n    {\n      \"index\": 2,\n      \"\
    node\": {\n        \"node_id\": \"low_temperature\",\n        \"label\": \"low\
    \ temperature\",\n        \"node_type\": \"ENVIRONMENTAL_FACTOR\",\n        \"\
    description\": \"Cold growth condition that reduces molecular motion and membrane\
    \ fluidity.\",\n        \"grounding\": \"PATO:0001306\"\n      },\n      \"status\"\
    : \"supported\",\n      \"assessment\": \"Cold growth condition is compatible\
    \ with PATO relatively low-temperature quality and exact low-temperature synonym.\
    \ Reference value unspecified; no forced event interpretation or enum defect.\"\
    \n    },\n    {\n      \"index\": 3,\n      \"node\": {\n        \"node_id\":\
    \ \"high_temperature\",\n        \"label\": \"high temperature\",\n        \"\
    node_type\": \"ENVIRONMENTAL_FACTOR\",\n        \"description\": \"Hot growth\
    \ condition that challenges protein and membrane stability.\",\n        \"grounding\"\
    : \"PATO:0001305\"\n      },\n      \"status\": \"supported\",\n      \"assessment\"\
    : \"Hot growth condition is compatible with PATO relatively high-temperature quality\
    \ and high-temperature synonym. Relative reference unspecified; no independent\
    \ grounding/type finding.\"\n    },\n    {\n      \"index\": 4,\n      \"node\"\
    : {\n        \"node_id\": \"membrane_fluidity\",\n        \"label\": \"membrane\
    \ fluidity\",\n        \"node_type\": \"QUALITY\",\n        \"description\": \"\
    Physical state of the membrane affecting transport and cell function.\",\n   \
    \     \"grounding\": \"METPO:1007505\"\n      },\n      \"status\": \"supported\"\
    ,\n      \"assessment\": \"Explicit membrane physical attribute and local v3 dynamic\
    \ mobility term support QUALITY.\"\n    },\n    {\n      \"index\": 5,\n     \
    \ \"node\": {\n        \"node_id\": \"protein_stability\",\n        \"label\"\
    : \"protein stability\",\n        \"node_type\": \"MOLECULAR_FUNCTION\",\n   \
    \     \"description\": \"Capacity of proteins to retain folded, functional conformations.\"\
    \n      },\n      \"status\": \"qualified\",\n      \"assessment\": \"Capacity\
    \ to retain folded functional conformations can describe a stability property/disposition\
    \ or broad molecular function. Current MOLECULAR_FUNCTION includes function; no\
    \ forced CAPACITY reservoir enum, no automatic protein/function conflation or\
    \ separate confirmed finding. Detailed efficacy unassessed.\"\n    },\n    {\n\
    \      \"index\": 6,\n      \"node\": {\n        \"node_id\": \"growth_rate\"\
    ,\n        \"label\": \"microbial growth rate\",\n        \"node_type\": \"BIOLOGICAL_PROCESS\"\
    ,\n        \"description\": \"Rate of population growth under a given temperature\
    \ regime.\"\n      },\n      \"status\": \"minor\",\n      \"assessment\": \"\
    Explicit rate of population growth denotes a measurable attribute, while BIOLOGICAL_PROCESS\
    \ denotes the growth process. Clear label/description preserve intended quantity,\
    \ so this is a bounded node-type precision finding, separate from the imported\
    \ relation-role major. Do not invent a biological mechanism or new grounding.\"\
    \n    },\n    {\n      \"index\": 7,\n      \"node\": {\n        \"node_id\":\
    \ \"temperature_downshift\",\n        \"label\": \"temperature downshift\",\n\
    \        \"node_type\": \"ENVIRONMENTAL_FACTOR\",\n        \"description\": \"\
    A decrease in environmental growth temperature (cold shift).\"\n      },\n   \
    \   \"status\": \"supported\",\n      \"assessment\": \"Actual environmental decrease/cold\
    \ shift denotes an event. ENVIRONMENTAL_FACTOR is permitted for environmental\
    \ exposure or condition and is not inherently nonprocess.\"\n    },\n    {\n \
    \     \"index\": 8,\n      \"node\": {\n        \"node_id\": \"fatty_acid_desaturase\"\
    ,\n        \"label\": \"fatty acid desaturase\",\n        \"node_type\": \"GENE_OR_PROTEIN\"\
    ,\n        \"description\": \"Desaturase enzyme (e.g., Des) that introduces double\
    \ bonds into membrane fatty acids.\",\n        \"grounding\": \"InterPro:IPR012171\"\
    \n      },\n      \"status\": \"supported\",\n      \"assessment\": \"Explicit\
    \ desaturase enzyme is a material protein-family referent. Official IPR012171\
    \ family label matches; closeMatch is taxon-agnostic. Detailed function and organism-specific\
    \ efficacy unassessed.\"\n    },\n    {\n      \"index\": 9,\n      \"node\":\
    \ {\n        \"node_id\": \"unsaturated_membrane_fatty_acids\",\n        \"label\"\
    : \"unsaturated membrane fatty acids\",\n        \"node_type\": \"CHEMICAL\",\n\
    \        \"description\": \"Membrane fatty acids bearing double bonds; raise membrane\
    \ fluidity (homeoviscous adaptation).\"\n      },\n      \"status\": \"supported\"\
    ,\n      \"assessment\": \"Membrane fatty-acid molecules are chemical material.\
    \ Their explanatory physical wording does not turn the node into a process or\
    \ a measured proportion.\"\n    },\n    {\n      \"index\": 10,\n      \"node\"\
    : {\n        \"node_id\": \"rna_thermometer\",\n        \"label\": \"RNA thermometer\"\
    ,\n        \"node_type\": \"RNA\",\n        \"description\": \"Temperature-responsive\
    \ RNA structure (ROSE/FourU) in 5-UTRs that gates translation by melting with\
    \ temperature.\"\n      },\n      \"status\": \"supported\",\n      \"assessment\"\
    : \"Functional RNA structure is compatible with RNA. Detailed thermometer/translation\
    \ regulation efficacy unassessed.\"\n    },\n    {\n      \"index\": 11,\n   \
    \   \"node\": {\n        \"node_id\": \"heat_shock_gene_translation\",\n     \
    \   \"label\": \"heat-shock gene translation\",\n        \"node_type\": \"BIOLOGICAL_PROCESS\"\
    ,\n        \"description\": \"Translation of heat-shock response genes permitted\
    \ upon RNA thermometer melting at elevated temperature.\"\n      },\n      \"\
    status\": \"supported\",\n      \"assessment\": \"Explicit translation denotes\
    \ a biological process. Detailed heat-response efficacy unassessed.\"\n    },\n\
    \    {\n      \"index\": 12,\n      \"node\": {\n        \"node_id\": \"cold_shock_rna_chaperone_activity\"\
    ,\n        \"label\": \"cold-shock RNA chaperone activity\",\n        \"node_type\"\
    : \"MOLECULAR_FUNCTION\",\n        \"description\": \"CspA-type RNA chaperone\
    \ activity that maintains single-stranded RNA to support translation at low temperature.\"\
    \n      },\n      \"status\": \"supported\",\n      \"assessment\": \"Explicit\
    \ RNA chaperone activity is a molecular activity; not a protein merely because\
    \ a protein family is mentioned. Detailed cold-response efficacy unassessed.\"\
    \n    }\n  ],\n  \"source\": [\n    {\n      \"index\": 0,\n      \"field\": \"\
    causal_graphs[0].nodes[0]\",\n      \"node_id\": \"temperature_preference_trait\"\
    ,\n      \"label\": \"temperature preference\",\n      \"node_type\": \"TRAIT\"\
    ,\n      \"source_outcome\": \"supported\",\n      \"assessment\": \"Broad temperature-dependent\
    \ growth phenotype supported by actual definition publisher context.\",\n    \
    \  \"incident_edges\": [\n        4,\n        5\n      ]\n    },\n    {\n    \
    \  \"index\": 1,\n      \"field\": \"causal_graphs[0].nodes[1]\",\n      \"node_id\"\
    : \"environmental_temperature\",\n      \"label\": \"environmental temperature\"\
    ,\n      \"node_type\": \"ENVIRONMENTAL_FACTOR\",\n      \"source_outcome\": \"\
    supported\",\n      \"assessment\": \"Temperature is the study’s environmental\
    \ axis; no operational growth model adopted.\",\n      \"incident_edges\": [\n\
    \        0\n      ]\n    },\n    {\n      \"index\": 2,\n      \"field\": \"causal_graphs[0].nodes[2]\"\
    ,\n      \"node_id\": \"low_temperature\",\n      \"label\": \"low temperature\"\
    ,\n      \"node_type\": \"ENVIRONMENTAL_FACTOR\",\n      \"source_outcome\": \"\
    qualified\",\n      \"assessment\": \"Generic cold/physical fluidity context supported;\
    \ detailed transport/survival efficacy not assessed.\",\n      \"incident_edges\"\
    : [\n        1,\n        10\n      ]\n    },\n    {\n      \"index\": 3,\n   \
    \   \"field\": \"causal_graphs[0].nodes[3]\",\n      \"node_id\": \"high_temperature\"\
    ,\n      \"label\": \"high temperature\",\n      \"node_type\": \"ENVIRONMENTAL_FACTOR\"\
    ,\n      \"source_outcome\": \"qualified\",\n      \"assessment\": \"Generic high-temperature\
    \ material-stability context supported; source constraints and actual formal node\
    \ sense remain distinct.\",\n      \"incident_edges\": [\n        2,\n       \
    \ 3,\n        8\n      ]\n    },\n    {\n      \"index\": 4,\n      \"field\"\
    : \"causal_graphs[0].nodes[4]\",\n      \"node_id\": \"membrane_fluidity\",\n\
    \      \"label\": \"membrane fluidity\",\n      \"node_type\": \"QUALITY\",\n\
    \      \"source_outcome\": \"qualified\",\n      \"assessment\": \"Generic membrane\
    \ fluidity physical meaning positive. Permeability is a related but distinct property;\
    \ no equivalence assumed.\",\n      \"incident_edges\": [\n        1,\n      \
    \  3,\n        4,\n        7\n      ]\n    },\n    {\n      \"index\": 5,\n  \
    \    \"field\": \"causal_graphs[0].nodes[5]\",\n      \"node_id\": \"protein_stability\"\
    ,\n      \"label\": \"protein stability\",\n      \"node_type\": \"MOLECULAR_FUNCTION\"\
    ,\n      \"source_outcome\": \"qualified\",\n      \"assessment\": \"Protein conformational\
    \ stability is generic source context; detailed mechanism/enhancement efficacy\
    \ unassessed and formal facet separately audited.\",\n      \"incident_edges\"\
    : [\n        2,\n        5\n      ]\n    },\n    {\n      \"index\": 6,\n    \
    \  \"field\": \"causal_graphs[0].nodes[6]\",\n      \"node_id\": \"growth_rate\"\
    ,\n      \"label\": \"microbial growth rate\",\n      \"node_type\": \"BIOLOGICAL_PROCESS\"\
    ,\n      \"source_outcome\": \"supported\",\n      \"assessment\": \"Definition\
    \ publisher explicitly refers to microbial growth rate; quantity-versus-process\
    \ formal representation is separately assessed.\",\n      \"incident_edges\":\
    \ [\n        0\n      ]\n    },\n    {\n      \"index\": 7,\n      \"field\":\
    \ \"causal_graphs[0].nodes[7]\",\n      \"node_id\": \"temperature_downshift\"\
    ,\n      \"label\": \"temperature downshift\",\n      \"node_type\": \"ENVIRONMENTAL_FACTOR\"\
    ,\n      \"source_outcome\": \"qualified\",\n      \"assessment\": \"A temperature\
    \ downshift is a contextual change; detailed induction efficacy not inferred.\"\
    ,\n      \"incident_edges\": [\n        11\n      ]\n    },\n    {\n      \"index\"\
    : 8,\n      \"field\": \"causal_graphs[0].nodes[8]\",\n      \"node_id\": \"fatty_acid_desaturase\"\
    ,\n      \"label\": \"fatty acid desaturase\",\n      \"node_type\": \"GENE_OR_PROTEIN\"\
    ,\n      \"source_outcome\": \"UNASSESSED_SCOPE\",\n      \"assessment\": \"Enzyme\
    \ class identity/formal grounding handled separately; detailed gene regulation\
    \ and intervention effects unassessed.\",\n      \"incident_edges\": [\n     \
    \   6,\n        11\n      ]\n    },\n    {\n      \"index\": 9,\n      \"field\"\
    : \"causal_graphs[0].nodes[9]\",\n      \"node_id\": \"unsaturated_membrane_fatty_acids\"\
    ,\n      \"label\": \"unsaturated membrane fatty acids\",\n      \"node_type\"\
    : \"CHEMICAL\",\n      \"source_outcome\": \"qualified\",\n      \"assessment\"\
    : \"Generic unsaturated fatty-acid physical context supported without cross-taxon\
    \ or intervention efficacy inference.\",\n      \"incident_edges\": [\n      \
    \  6,\n        7\n      ]\n    },\n    {\n      \"index\": 10,\n      \"field\"\
    : \"causal_graphs[0].nodes[10]\",\n      \"node_id\": \"rna_thermometer\",\n \
    \     \"label\": \"RNA thermometer\",\n      \"node_type\": \"RNA\",\n      \"\
    source_outcome\": \"UNASSESSED_SCOPE\",\n      \"assessment\": \"RNA naming/formal\
    \ facet only; detailed thermosensing mechanism unassessed.\",\n      \"incident_edges\"\
    : [\n        8,\n        9\n      ]\n    },\n    {\n      \"index\": 11,\n   \
    \   \"field\": \"causal_graphs[0].nodes[11]\",\n      \"node_id\": \"heat_shock_gene_translation\"\
    ,\n      \"label\": \"heat-shock gene translation\",\n      \"node_type\": \"\
    BIOLOGICAL_PROCESS\",\n      \"source_outcome\": \"UNASSESSED_SCOPE\",\n     \
    \ \"assessment\": \"Detailed heat-shock/stress-regulation efficacy unassessed.\"\
    ,\n      \"incident_edges\": [\n        9\n      ]\n    },\n    {\n      \"index\"\
    : 12,\n      \"field\": \"causal_graphs[0].nodes[12]\",\n      \"node_id\": \"\
    cold_shock_rna_chaperone_activity\",\n      \"label\": \"cold-shock RNA chaperone\
    \ activity\",\n      \"node_type\": \"MOLECULAR_FUNCTION\",\n      \"source_outcome\"\
    : \"UNASSESSED_SCOPE\",\n      \"assessment\": \"Detailed cold-survival/RNA-chaperone\
    \ mechanism and enhancement unassessed.\",\n      \"incident_edges\": [\n    \
    \    10\n      ]\n    }\n  ]\n}"
- assessment_id: relations
  area: consistency
  topic: 'Native checklist: all twelve current relations'
  outcome: concern
  target_ids:
  - METPO:1000613
  summary: RO2211/2212/2213 edges 0/1/3/4/5/6/7 conflict with inherited process roles
    for their stated condition, quantity, phenotype or material referents. The edge
    5 trait object is independently decisive despite qualified protein-stability wording.
    Local challenges has broad compatible endpoints. Four lexical-only edges do not
    inherit RO/Biolink restrictions from their English verbs. Detailed biological
    efficacy remains unassessed.
  evidence_ids:
  - nodes-edges
  - source-nodes-edges
  - ro-primary
  - ontology-primary
  - local-authority
  - adjudication
  details: "{\n  \"grounding\": [\n    {\n      \"index\": 0,\n      \"edge\": {\n\
    \        \"subject\": \"environmental_temperature\",\n        \"predicate\": \"\
    regulates\",\n        \"object\": \"growth_rate\",\n        \"description\": \"\
    Microbial growth rate varies with growth temperature.\",\n        \"evidence\"\
    : [\n          {\n            \"reference\": \"DOI:10.1038/sj.jim.2900572\",\n\
    \            \"snippet\": \"growth rate vs temperature\",\n            \"notes\"\
    : \"Study analyzes temperature dependence of microbial growth rates across psychrotrophs,\
    \ mesophiles, and thermophiles.\"\n          }\n        ],\n        \"predicate_id\"\
    : \"RO:0002211\"\n      },\n      \"status\": \"major\",\n      \"assessment\"\
    : \"RO2211 requires process/process. Current subject is environmental temperature\
    \ condition/axis and object is an explicit growth-rate attribute despite its process\
    \ enum. The subject mismatch persists after correcting the object type.\"\n  \
    \  },\n    {\n      \"index\": 1,\n      \"edge\": {\n        \"subject\": \"\
    low_temperature\",\n        \"predicate\": \"decreases\",\n        \"object\"\
    : \"membrane_fluidity\",\n        \"description\": \"Cold temperature reduces\
    \ membrane fluidity and transport efficiency.\",\n        \"evidence\": [\n  \
    \        {\n            \"reference\": \"DOI:10.1038/sj.embor.7400662\",\n   \
    \         \"snippet\": \"decreased membrane fluidity\",\n            \"notes\"\
    : \"Review identifies membrane fluidity loss as a core cold challenge.\"\n   \
    \       }\n        ],\n        \"predicate_id\": \"RO:0002212\"\n      },\n  \
    \    \"status\": \"major\",\n      \"assessment\": \"RO2212 inherits RO2211 process/process;\
    \ the cold condition and membrane-fluidity quality are not the required processes.\"\
    \n    },\n    {\n      \"index\": 2,\n      \"edge\": {\n        \"subject\":\
    \ \"high_temperature\",\n        \"predicate\": \"challenges\",\n        \"object\"\
    : \"protein_stability\",\n        \"description\": \"Elevated temperature challenges\
    \ protein folding and functional stability.\",\n        \"evidence\": [\n    \
    \      {\n            \"reference\": \"DOI:10.1128/MMBR.65.1.1-43.2001\",\n  \
    \          \"snippet\": \"resistant to irreversible inactivation at high temperatures\"\
    ,\n            \"notes\": \"Review supports thermostable enzymes as a high-temperature\
    \ adaptation.\"\n          }\n        ],\n        \"predicate_id\": \"METPO:2007406\"\
    \n      },\n      \"status\": \"qualified\",\n      \"assessment\": \"Local v2\
    \ challenges has broad scaffold endpoints and compatible stressor-to-stability/function\
    \ wording. No imported RO restriction inferred. Its detailed biological support\
    \ is outside this audit.\"\n    },\n    {\n      \"index\": 3,\n      \"edge\"\
    : {\n        \"subject\": \"high_temperature\",\n        \"predicate\": \"increases\"\
    ,\n        \"object\": \"membrane_fluidity\",\n        \"description\": \"High\
    \ temperature increases membrane permeability and fluidity, creating a limit on\
    \ growth.\",\n        \"evidence\": [\n          {\n            \"reference\"\
    : \"DOI:10.1016/s0300-9629(97)00003-0\",\n            \"snippet\": \"proton permeability\
    \ ... increase with the temperature\",\n            \"notes\": \"Review links\
    \ increased membrane permeability to upper temperature growth limits.\"\n    \
    \      }\n        ],\n        \"predicate_id\": \"RO:0002213\"\n      },\n   \
    \   \"status\": \"major\",\n      \"assessment\": \"RO2213 inherits process/process;\
    \ current hot condition and membrane-fluidity quality do not satisfy those roles.\"\
    \n    },\n    {\n      \"index\": 4,\n      \"edge\": {\n        \"subject\":\
    \ \"membrane_fluidity\",\n        \"predicate\": \"regulates\",\n        \"object\"\
    : \"temperature_preference_trait\",\n        \"description\": \"Temperature preference\
    \ reflects the range in which membrane function remains compatible with growth.\"\
    ,\n        \"evidence\": [\n          {\n            \"reference\": \"DOI:10.1146/annurev-micro-091313-103612\"\
    ,\n            \"snippet\": \"optimizes the performance of cellular physiological\
    \ processes\",\n            \"notes\": \"Review supports membrane fluidity adaptation\
    \ as a temperature-sensing and response mechanism.\"\n          }\n        ],\n\
    \        \"predicate_id\": \"RO:0002211\"\n      },\n      \"status\": \"major\"\
    ,\n      \"assessment\": \"RO2211 applied to membrane-fluidity QUALITY and temperature-preference\
    \ TRAIT; both actual referents differ from processes.\"\n    },\n    {\n     \
    \ \"index\": 5,\n      \"edge\": {\n        \"subject\": \"protein_stability\"\
    ,\n        \"predicate\": \"regulates\",\n        \"object\": \"temperature_preference_trait\"\
    ,\n        \"description\": \"Growth at preferred temperatures requires proteins\
    \ to remain active and stable.\",\n        \"evidence\": [\n          {\n    \
    \        \"reference\": \"DOI:10.1128/MMBR.65.1.1-43.2001\",\n            \"snippet\"\
    : \"molecular mechanisms involved in protein thermostabilization\",\n        \
    \    \"notes\": \"Supports protein stability as a determinant of high-temperature\
    \ growth.\"\n          }\n        ],\n        \"predicate_id\": \"RO:0002211\"\
    \n      },\n      \"status\": \"major\",\n      \"assessment\": \"RO2211 has an\
    \ explicit trait object, independently conflicting with process range. Protein-stability\
    \ function/quality facet remains qualified; no categorical MF exclusion needed\
    \ for the finding.\"\n    },\n    {\n      \"index\": 6,\n      \"edge\": {\n\
    \        \"subject\": \"fatty_acid_desaturase\",\n        \"predicate\": \"increases\"\
    ,\n        \"object\": \"unsaturated_membrane_fatty_acids\",\n        \"description\"\
    : \"Desaturase expression increases double bonds in membrane fatty acids (homeoviscous\
    \ adaptation).\",\n        \"evidence\": [\n          {\n            \"reference\"\
    : \"DOI:10.1007/s42770-023-01057-4\",\n            \"notes\": \"Activation of\
    \ des (desaturase) transcription increases double bonds in membrane fatty acids;\
    \ generic UFA-biosynthesis module.\"\n          }\n        ],\n        \"predicate_id\"\
    : \"RO:0002213\"\n      },\n      \"status\": \"major\",\n      \"assessment\"\
    : \"RO2213 applied from explicit material desaturase enzyme to material fatty\
    \ acids. Description mentions expression but current node identity is the protein\
    \ family, not an expression process. No mechanistic replacement prescribed.\"\n\
    \    },\n    {\n      \"index\": 7,\n      \"edge\": {\n        \"subject\": \"\
    unsaturated_membrane_fatty_acids\",\n        \"predicate\": \"increases\",\n \
    \       \"object\": \"membrane_fluidity\",\n        \"description\": \"Increased\
    \ unsaturated membrane fatty acids restore/raise membrane fluidity.\",\n     \
    \   \"evidence\": [\n          {\n            \"reference\": \"DOI:10.1007/s42770-023-01057-4\"\
    ,\n            \"notes\": \"Increasing double bonds in membrane fatty acids restores\
    \ membrane fluidity; core homeoviscous-adaptation edge broadly curatable across\
    \ microbes.\"\n          }\n        ],\n        \"predicate_id\": \"RO:0002213\"\
    \n      },\n      \"status\": \"major\",\n      \"assessment\": \"RO2213 applied\
    \ from material fatty acids to membrane-fluidity QUALITY; process roles fail independently\
    \ of efficacy.\"\n    },\n    {\n      \"index\": 8,\n      \"edge\": {\n    \
    \    \"subject\": \"high_temperature\",\n        \"predicate\": \"melts\",\n \
    \       \"object\": \"rna_thermometer\",\n        \"description\": \"Elevated\
    \ temperature melts RNA thermometer hairpins, relieving translational repression.\"\
    ,\n        \"evidence\": [\n          {\n            \"reference\": \"DOI:10.1007/s12275-023-00031-x\"\
    ,\n            \"notes\": \"RNA thermometers (ROSE/FourU) control translation\
    \ by occluding Shine-Dalgarno/start codons and melt with temperature; bacterial\
    \ heat-sensing mechanism.\"\n          }\n        ]\n      },\n      \"status\"\
    : \"lexical_only\",\n      \"assessment\": \"melts has no predicate_id. No imported\
    \ RO/Biolink domain or range is inferred from the label. Detailed RNA-thermometer\
    \ efficacy unassessed.\"\n    },\n    {\n      \"index\": 9,\n      \"edge\":\
    \ {\n        \"subject\": \"rna_thermometer\",\n        \"predicate\": \"permits\
    \ translation of\",\n        \"object\": \"heat_shock_gene_translation\",\n  \
    \      \"description\": \"RNA thermometer melting permits translation of heat-shock\
    \ genes.\",\n        \"evidence\": [\n          {\n            \"reference\":\
    \ \"DOI:10.1007/s12275-023-00031-x\",\n            \"notes\": \"Post-transcriptional\
    \ RNA thermometers in 5-UTRs mediate rapid temperature-dependent control of translation;\
    \ strong generic edge.\"\n          }\n        ]\n      },\n      \"status\":\
    \ \"lexical_only\",\n      \"assessment\": \"permits translation of has no predicate_id.\
    \ RNA-to-translation referents are legible; no automatic RO executor inference\
    \ or detailed efficacy conclusion.\"\n    },\n    {\n      \"index\": 10,\n  \
    \    \"edge\": {\n        \"subject\": \"low_temperature\",\n        \"predicate\"\
    : \"induces\",\n        \"object\": \"cold_shock_rna_chaperone_activity\",\n \
    \       \"description\": \"Cold shock induces CspA-mediated RNA chaperone activity\
    \ that maintains translatable RNA.\",\n        \"evidence\": [\n          {\n\
    \            \"reference\": \"DOI:10.1007/s12275-023-00031-x\",\n            \"\
    notes\": \"Cold shock induces cold-shock proteins (CspA) that help maintain single-stranded\
    \ RNA for translation at low temperature.\"\n          }\n        ]\n      },\n\
    \      \"status\": \"lexical_only\",\n      \"assessment\": \"induces has no predicate_id.\
    \ Low condition/activity referents are preserved; cold-shock wording versus steady\
    \ low condition is a source/biological qualification, not a new imported-role\
    \ finding.\"\n    },\n    {\n      \"index\": 11,\n      \"edge\": {\n       \
    \ \"subject\": \"temperature_downshift\",\n        \"predicate\": \"induces\"\
    ,\n        \"object\": \"fatty_acid_desaturase\",\n        \"description\": \"\
    Cold downshift induces fatty-acid desaturase activity to maintain membrane fluidity.\"\
    ,\n        \"evidence\": [\n          {\n            \"reference\": \"DOI:10.1038/sj.jim.2900572\"\
    ,\n            \"notes\": \"Connecting edge wiring the enrichment node into the\
    \ graph.\"\n          }\n        ]\n      },\n      \"status\": \"lexical_only\"\
    ,\n      \"assessment\": \"induces has no predicate_id. Subject describes an actual\
    \ downshift event; material protein object is not automatically a formal error\
    \ absent an imported predicate. Detailed regulation support unassessed.\"\n  \
    \  }\n  ],\n  \"source\": [\n    {\n      \"index\": 0,\n      \"field\": \"causal_graphs[0].edges[0]\"\
    ,\n      \"subject\": \"environmental_temperature\",\n      \"predicate\": \"\
    regulates\",\n      \"object\": \"growth_rate\",\n      \"source_outcome\": \"\
    supported\",\n      \"assessment\": \"Publisher line183 explicitly compares growth\
    \ rate versus temperature across psychrotrophs, mesophiles and thermophiles; broad\
    \ phenotype context positive without adopting model parameters.\",\n      \"references\"\
    : [\n        \"DOI:10.1038/sj.jim.2900572\"\n      ]\n    },\n    {\n      \"\
    index\": 1,\n      \"field\": \"causal_graphs[0].edges[1]\",\n      \"subject\"\
    : \"low_temperature\",\n      \"predicate\": \"decreases\",\n      \"object\"\
    : \"membrane_fluidity\",\n      \"source_outcome\": \"qualified\",\n      \"assessment\"\
    : \"D’Amico supplied abstract phrase is literal and supports generic reduced fluidity\
    \ in cold context; detailed transport/survival efficacy unassessed.\",\n     \
    \ \"references\": [\n        \"DOI:10.1038/sj.embor.7400662\"\n      ]\n    },\n\
    \    {\n      \"index\": 2,\n      \"field\": \"causal_graphs[0].edges[2]\",\n\
    \      \"subject\": \"high_temperature\",\n      \"predicate\": \"challenges\"\
    ,\n      \"object\": \"protein_stability\",\n      \"source_outcome\": \"qualified\"\
    ,\n      \"assessment\": \"Vieille/Zeikus supplied phrase is literal in its abstract\
    \ and supplies generic high-temperature stability context, not detailed thermostabilization/enhancement\
    \ efficacy.\",\n      \"references\": [\n        \"DOI:10.1128/MMBR.65.1.1-43.2001\"\
    \n      ]\n    },\n    {\n      \"index\": 3,\n      \"field\": \"causal_graphs[0].edges[3]\"\
    ,\n      \"subject\": \"high_temperature\",\n      \"predicate\": \"increases\"\
    ,\n      \"object\": \"membrane_fluidity\",\n      \"source_outcome\": \"concern\"\
    ,\n      \"assessment\": \"Explicit ellipsis joins source spans rather than a\
    \ contiguous snippet. The nearest abstract addresses proton permeability and growth\
    \ limits; permeability and fluidity are distinct properties, so broader direct\
    \ fluidity attribution remains qualified/unknown, not refuted.\",\n      \"references\"\
    : [\n        \"DOI:10.1016/s0300-9629(97)00003-0\"\n      ]\n    },\n    {\n \
    \     \"index\": 4,\n      \"field\": \"causal_graphs[0].edges[4]\",\n      \"\
    subject\": \"membrane_fluidity\",\n      \"predicate\": \"regulates\",\n     \
    \ \"object\": \"temperature_preference_trait\",\n      \"source_outcome\": \"\
    concern\",\n      \"assessment\": \"Mendoza snippet omits intervening words. Generic\
    \ bilayer/physiological context is positive; exact causal sufficiency for preference\
    \ is not established by this short phrase.\",\n      \"references\": [\n     \
    \   \"DOI:10.1146/annurev-micro-091313-103612\"\n      ]\n    },\n    {\n    \
    \  \"index\": 5,\n      \"field\": \"causal_graphs[0].edges[5]\",\n      \"subject\"\
    : \"protein_stability\",\n      \"predicate\": \"regulates\",\n      \"object\"\
    : \"temperature_preference_trait\",\n      \"source_outcome\": \"qualified\",\n\
    \      \"assessment\": \"Vieille/Zeikus abstract snippet is literal. Broad protein\
    \ stability context is positive; exact whole-organism necessity/sufficiency and\
    \ detailed mechanism unassessed.\",\n      \"references\": [\n        \"DOI:10.1128/MMBR.65.1.1-43.2001\"\
    \n      ]\n    },\n    {\n      \"index\": 6,\n      \"field\": \"causal_graphs[0].edges[6]\"\
    ,\n      \"subject\": \"fatty_acid_desaturase\",\n      \"predicate\": \"increases\"\
    ,\n      \"object\": \"unsaturated_membrane_fatty_acids\",\n      \"source_outcome\"\
    : \"UNASSESSED_SCOPE\",\n      \"assessment\": \"Ramón identity positive; detailed\
    \ desaturase transcription/stress regulation and efficacy not assessed.\",\n \
    \     \"references\": [\n        \"DOI:10.1007/s42770-023-01057-4\"\n      ]\n\
    \    },\n    {\n      \"index\": 7,\n      \"field\": \"causal_graphs[0].edges[7]\"\
    ,\n      \"subject\": \"unsaturated_membrane_fatty_acids\",\n      \"predicate\"\
    : \"increases\",\n      \"object\": \"membrane_fluidity\",\n      \"source_outcome\"\
    : \"qualified\",\n      \"assessment\": \"Generic unsaturation/fluidity physical\
    \ direction is consistent with inspected Mendoza context. Broad cross-organism\
    \ restorative efficacy and detailed source mechanisms remain unassessed.\",\n\
    \      \"references\": [\n        \"DOI:10.1007/s42770-023-01057-4\"\n      ]\n\
    \    },\n    {\n      \"index\": 8,\n      \"field\": \"causal_graphs[0].edges[8]\"\
    ,\n      \"subject\": \"high_temperature\",\n      \"predicate\": \"melts\",\n\
    \      \"object\": \"rna_thermometer\",\n      \"source_outcome\": \"UNASSESSED_SCOPE\"\
    ,\n      \"assessment\": \"Moon identity only; detailed RNA thermometer/heat sensing\
    \ mechanisms not assessed or repaired.\",\n      \"references\": [\n        \"\
    DOI:10.1007/s12275-023-00031-x\"\n      ]\n    },\n    {\n      \"index\": 9,\n\
    \      \"field\": \"causal_graphs[0].edges[9]\",\n      \"subject\": \"rna_thermometer\"\
    ,\n      \"predicate\": \"permits translation of\",\n      \"object\": \"heat_shock_gene_translation\"\
    ,\n      \"source_outcome\": \"UNASSESSED_SCOPE\",\n      \"assessment\": \"Moon\
    \ identity only; detailed heat-shock translational control efficacy unassessed.\"\
    ,\n      \"references\": [\n        \"DOI:10.1007/s12275-023-00031-x\"\n     \
    \ ]\n    },\n    {\n      \"index\": 10,\n      \"field\": \"causal_graphs[0].edges[10]\"\
    ,\n      \"subject\": \"low_temperature\",\n      \"predicate\": \"induces\",\n\
    \      \"object\": \"cold_shock_rna_chaperone_activity\",\n      \"source_outcome\"\
    : \"UNASSESSED_SCOPE\",\n      \"assessment\": \"Moon identity only; detailed\
    \ cold-shock/RNA-chaperone induction efficacy unassessed.\",\n      \"references\"\
    : [\n        \"DOI:10.1007/s12275-023-00031-x\"\n      ]\n    },\n    {\n    \
    \  \"index\": 11,\n      \"field\": \"causal_graphs[0].edges[11]\",\n      \"\
    subject\": \"temperature_downshift\",\n      \"predicate\": \"induces\",\n   \
    \   \"object\": \"fatty_acid_desaturase\",\n      \"source_outcome\": \"UNASSESSED_SCOPE\"\
    ,\n      \"assessment\": \"Dantigny publisher establishes growth-temperature study\
    \ identity/classification; its detailed support for a desaturase-induction connector\
    \ is not inspected. No absence or false-source assertion from the available abstract.\"\
    ,\n      \"references\": [\n        \"DOI:10.1038/sj.jim.2900572\"\n      ]\n\
    \    }\n  ]\n}"
- assessment_id: owners
  area: ownership
  topic: 'Native checklist: conditional recurrence and record-only fields'
  outcome: supported
  target_ids:
  - METPO:1000613
  summary: Formal relation owners are the record, wildcard regulates/decreases/increases
    mappings and skip-populated grounder. Ordinary replay does not repair current
    IDs. No exact faulty target payload or snippet writer was demonstrated. The maximal_growth_rate
    migration does not select current growth_rate; node type and snippets remain record-owned.
  evidence_ids:
  - owners
  - owner-primary
  - predicate-mapping
  - node-mapping
  - discovery
  - adjudication
- assessment_id: provenance
  area: provenance
  topic: 'Native checklist: attributable human acceptance'
  outcome: concern
  target_ids:
  - METPO:1000613
  summary: Nineteen embedded events comprise eighteen AI events plus a seed; three
    captured AI context histories were read whole currently. Ignored- and hidden-inclusive
    search found 204 matching paths, 67 matching-search arrays and 98 all-local arrays,
    with zero exact current target in all 98. Initial discovery already retained 98;
    follow-up suspicion of a parser issue did not establish missing arrays. Private
    or remote acceptance remains unknown.
  evidence_ids:
  - human-search
  - human-search-followup
  - search-clarification
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
  - METPO:1000613
  summary: Retained catalog scope distinguishes canonical-name absence from positive
    source-organism species coverage. No global organism absence, exact-strain or
    module result follows. Maintained adapter discovery is unavailable in the bounded
    current environment; generic primary fallback does not supply a membership or
    efficacy result.
  evidence_ids:
  - expression
  - expression-discovery
  - source-reading
- assessment_id: readiness
  area: completeness
  topic: 'Native checklist: NONMECHANISTIC scope and optional instances'
  outcome: supported
  target_ids:
  - METPO:1000613
  summary: Two components with thirteen nodes and twelve edges do not require invented
    connectors. One positively grounded protein family and zero instances do not require
    an accession or detailed mechanism. Canonical quantities and detailed efficacy
    remain unassessed.
  evidence_ids:
  - record
  - nodes-edges
  - expression
  - policy
  - interpro-primary
- assessment_id: validation
  area: schema
  topic: 'Native checklist: native checks, baseline and fresh common diagnostics'
  outcome: supported
  target_ids:
  - METPO:1000613
  summary: Current inspect, focused validation, strict validation and snippet command
    completed successfully. Existing Tolner native ELLIPTICAL_SNIPPET ERROR remains
    explicit and scientifically normalized, not erased. B14 common diagnostics retain
    actual execution intervals, original historical attempts, product skips and omitted
    full suite; they do not establish scientific correctness.
  evidence_ids:
  - capture
  - fresh-common-completion
  - check-temperature-preference-validate
  - check-temperature-preference-strict
  - check-temperature-preference-snippets-network
  - source-native
  - native-ellipsis
findings:
- finding_id: imported-process-roles
  issue_key: temperature-preference-imported-process-roles
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Imported process roles
  description: RO:0002211/RO:0002212/RO:0002213 require process-to-process roles;
    these seven current assertions instead use explicit temperature conditions, qualities,
    trait, protein or chemicals. Edge 5 trait range is independently decisive despite
    qualified protein-stability facet.
  target_ids:
  - METPO:1000613
  field_paths:
  - causal_graphs[0].edges[0].predicate_id
  - causal_graphs[0].edges[1].predicate_id
  - causal_graphs[0].edges[3].predicate_id
  - causal_graphs[0].edges[4].predicate_id
  - causal_graphs[0].edges[5].predicate_id
  - causal_graphs[0].edges[6].predicate_id
  - causal_graphs[0].edges[7].predicate_id
  evidence_ids:
  - nodes-edges
  - ro-primary
  - ontology-primary
  - owners
  - owner-primary
  - predicate-mapping
  - local-authority
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_preference.yaml
    role: Current record assertions; separate authorized curation required
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Conditional wildcard recurrence for empty predicate IDs, not an automatic
      current rewrite
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Shared predicate writer skips populated IDs; ordinary replay does not repair
      current assertions
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: growth-rate-facet
  issue_key: temperature-preference-growth-rate-facet
  category: representation
  severity: minor
  status: open
  certainty: confirmed
  title: Growth rate facet
  description: The explicit rate of population growth is typed BIOLOGICAL_PROCESS.
    Its clear label/description preserve the intended quantity, making this bounded
    type precision rather than uncertain identity. Independent of the regulation-edge
    issue.
  target_ids:
  - METPO:1000613
  field_paths:
  - causal_graphs[0].nodes[6].node_type
  evidence_ids:
  - record
  - nodes-edges
  - schema
  - owner-primary
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_preference.yaml
    role: Current record assertions; separate authorized curation required
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: nonverbatim-source-snippets
  issue_key: temperature-preference-nonverbatim-source-snippets
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Nonverbatim source snippets
  description: Tolner uses a marked ellipsis to join separate abstract spans; Mendoza
    omits intervening words from its actual abstract sentence. These do not satisfy
    contiguous copied-span presentation. Preserve generic physical meaning and qualify
    exact-source/version scope; no biological refutation or fabricated-quotation accusation.
  target_ids:
  - METPO:1000613
  field_paths:
  - causal_graphs[0].edges[3].evidence[0].snippet
  - causal_graphs[0].edges[4].evidence[0].snippet
  evidence_ids:
  - snippets
  - source-native
  - native-ellipsis
  - tolner-metadata
  - mendoza-metadata
  - mendoza-publisher
  - owners
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_preference.yaml
    role: Current record assertions; separate authorized curation required
  rule_id: ELLIPTICAL_SNIPPET; native verbatim-snippet requirement
  native_severity: ERROR
  normalization_reason: The baselined Tolner ELLIPTICAL_SNIPPET diagnostic is ERROR;
    normalized to a minor scientific-review finding because the bounded defect is
    copied-span presentation with generic context supported. Mendoza independently
    omits words. Native NOT_IN_ABSTRACT remains inconclusive; no biological refutation
    or fabricated-source allegation.
- finding_id: human-acceptance-link
  issue_key: temperature-preference-human-acceptance-link
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Human acceptance link
  description: 'REVIEWED lacks an attributable human acceptance link in the bounded
    current record/local review/history scope: eighteen AI events plus seed; three
    captured AI context histories; zero exact target across all 98 current review
    arrays. Private or remote acceptance remains unknown.'
  target_ids:
  - METPO:1000613
  field_paths:
  - mapping_status
  - curation_history
  evidence_ids:
  - human-search
  - human-search-followup
  - search-clarification
  - histories
  - ground-reading
  - root-reading
  - root-verification
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_preference.yaml
    role: Current record assertions; separate authorized curation required
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
actions:
- action_id: curate-imported-process-roles
  description: In separately authorized curation reconcile the seven populated process-restricted
    relation assertions with their preserved condition, quantity, phenotype and material
    referents. Check conditional regulates/decreases/increases mapping recurrence;
    ordinary grounder replay skips populated IDs. No exact target-specific faulty
    payload writer was demonstrated.
  finding_ids:
  - imported-process-roles
  target_ids:
  - METPO:1000613
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_preference.yaml
    role: Current record assertions; separate authorized curation required
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Conditional wildcard recurrence for empty predicate IDs, not an automatic
      current rewrite
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Shared predicate writer skips populated IDs; ordinary replay does not repair
      current assertions
  acceptance_checks:
  - Demonstrate inherited role compatibility for edges 0/1/3/4/5/6/7 without retyping
    referents merely to fit a predicate.
  - Check wildcard mapping rows 11/61/65 against incompatible endpoints and legitimate
    process controls; preserve skip-populated behavior explicitly.
  - Keep local challenges and four lexical-only edges distinct; no operational biological
    repair or invented connector.
  - Run focused strict, relevant predicate/graph checks, full QC and required history/product
    gates for any authorized changes.
- action_id: curate-growth-rate-facet
  description: Align the node 6 declared type with its stated rate attribute while
    preserving its label/description and assessing incident relation roles separately.
    The current maximal_growth_rate migration does not select growth_rate; the current
    record owns this change.
  finding_ids:
  - growth-rate-facet
  target_ids:
  - METPO:1000613
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_preference.yaml
    role: Current record assertions; separate authorized curation required
  acceptance_checks:
  - Type and explicit rate referent agree without invented accession or growth mechanism.
  - The imported-role finding remains independently checked; run required guarded-curation
    validation.
- action_id: curate-nonverbatim-source-snippets
  description: In separately authorized curation make each supplied snippet one exact
    contiguous source span, or move the paraphrase to notes, retaining DOI and selected-source
    locator. The current record is the demonstrated owner; no exact recurring snippet
    writer was established.
  finding_ids:
  - nonverbatim-source-snippets
  target_ids:
  - METPO:1000613
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_preference.yaml
    role: Current record assertions; separate authorized curation required
  acceptance_checks:
  - Compare final snippets to their identified inspected primary version with only
    documented whitespace/HTML normalization.
  - Keep native ELLIPTICAL_SNIPPET ERROR separate from its normalized review severity
    and from inconclusive metadata matching.
  - Preserve unknown nearest-claim support, permeability/fluidity distinction and
    unassessed mechanisms; run native snippet and required curation gates.
- action_id: curate-human-acceptance-link
  description: Link actual attributable acceptance of the current assertions if available,
    or qualify review-status provenance accurately. Do not fabricate retrospective
    sign-off.
  finding_ids:
  - human-acceptance-link
  target_ids:
  - METPO:1000613
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_preference.yaml
    role: Current record assertions; separate authorized curation required
  acceptance_checks:
  - Acceptance evidence identifies the person, exact assertions and disposition, or
    the remaining uncertainty is explicit.
  - Preserve append-only history and run applicable gates for separately authorized
    curation.
limitations:
- Full just test was NOT_RUN under the selected review-only diagnostic scope; only
  the five focused Stage2 tests are recorded. Products retains 123 no-adapter skips.
  Common checks establish bounded software/data integrity, not scientific support.
- Exact mechanism-to-preference sufficiency and permeability-versus-fluidity source
  scope remain qualified/unknown.
- Detailed RNA/stress/desaturase regulation, survival/fitness/defense, enzyme/intervention
  efficacy remain UNASSESSED_SCOPE.
- Both canonical quantitative/cultivation/adaptation claims remain unassessed; metadata/title
  identity does not validate them.
- Retained metadata notice observations are original-time bounded, not current publication-status
  refreshes.
- Detailed stress-defense, survival, fitness, RNA regulation, enzyme efficacy, adaptation/cultivation/numerical
  canonical support and intervention mechanisms UNASSESSED_SCOPE.
- The grounding audit adds no separate source finding; the independent source audit
  supplies the adopted snippet-presentation minor.
- Only stated current/whole/selected/matching-line scopes adopted; no exact target
  payload writer invented.
- Private and remote human acceptance unknown.
- Original taxonomy/catalog access clocks and current InterPro retry clocks are retained.
  The grounding auditor reused pinned database provenance and did not rerun native
  checks; root focused checks are recorded separately.
- Native snippet check passed with 3 VERIFIED, 2 NOT_IN_ABSTRACT and 2 UNRESOLVED
  results. Manual selected primary text yields 5 literal and 2 noncontiguous snippets;
  native results are not rewritten.
- Dantigny OUP browser response supplies positive identity and broad classification.
  EPMC zero-hit and root DOI tool failure are retrieval diagnostics. Browser response
  is not raw HTML or whole article; root failure has only export time and no inferred
  HTTP status.
- Original acquisition, extraction, copy and current reading clocks remain distinct;
  old notice fields are not refreshed publication status. Initial InterPro DNS failure
  is retained separately from the successful public API retry.
- Grounding auditor read 3 captured histories whole; root read their actor/target/event-type
  projections. Search across 204 paths includes ignored/hidden except .git/.venv;
  67 matching-search review arrays differ from 98 all-local arrays, all 98 have zero
  exact targets. Three uncaptured script leads and one sibling history are matching-line
  context only.
- The maintained expression adapter is unavailable in bounded current discovery. Retained
  catalog of 20 organisms and 28 datasets has no exact canonical species key; B.subtilis/E.coli
  species keys do not establish exact strain/module or efficacy. No stress-term query
  executed.
- The NONMECHANISTIC graph has 2 components, 1 family-grounded protein class and 0
  instances; these do not require invented connectors, proteins or datasets.
- Protein-stability function versus property facet remains qualified. PATO low/high
  temperature condition shorthand is compatible; actual downshift is an event. No
  automatic CAPACITY or blanket environmental-type error.
- Permeability is distinct from fluidity. Generic physical context and literal snippets
  do not establish sufficient, exclusive or universal temperature-preference mechanisms.
- Source overall UNKNOWN is retained; one source minor joins grounding findings of
  1 major and 2 minors without upgrading unassessed biological claims.
- Growth-rate type precision is minor because label/description preserve intended
  quantity; role-major remains independently valid.
- Root primary and current verification receipts distinguish direct reading from delegated
  selected owner/history review.
- Local challenge and fluidity proposal identities are positive; wildcard mappings
  are conditional recurrence owners, not proof of exact source-writer authorship.
notes:
- Historical products failures/retry and original cache provenance remain in /private/tmp/traitmech-record-sweep-014.q8m4v2cs/new-base-diagnostic-independent-review-agent/fresh-products-completion.json.
  The earlier outstanding-products status is superseded by the actual fresh run; no
  blanket cross-batch reuse qualification is asserted.
- Final fields, categories, severities, owners and actions come from revised root
  FINAL. The source snippet minor joins the grounding audit findings; no unassessed
  biological claim is upgraded.
- This serializer adopts frozen audits and root adjudication. Original acquisitions/extraction,
  current copies/readings, browser tool intervals/exports and failed/successful requests
  remain distinct. Serializer preparation is static; root execution and native output
  validation are separately recorded. No scientific record, state, Git or publication
  change is performed.
tags:
- record-review
- temperature-preference
- environment
- needs-curation
```
