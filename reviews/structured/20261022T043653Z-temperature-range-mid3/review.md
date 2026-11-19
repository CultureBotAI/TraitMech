# Whole-record review of temperature range mid3

- Review: 20261022T043653Z-temperature-range-mid3
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-22T04:24:10.002008Z
- Finished UTC: 2026-10-22T04:36:53Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Whole-record review identifies two major issues: ambient-temperature interval versus interval-width semantics and incompatible imported roles at five edges. Two bounded minors concern exact-bin attribution and a retrievable human-acceptance link. Active identity, canonical reported17–50 °C interval with derived width33, eleven literal snippets and selected formal facets are positive. Detailed microbial efficacy remains unassessed.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: Third record in the actual B15 queue; current 362-line target and 103 captured inputs. Local review is independent of remote publication.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 508ee3089c93a36413969cd1ede7f9528a1940a4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| METPO:1000452 | data/traits/environment/temperature_range_mid3.yaml | maintained | temperature range mid3 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Reused B14 corpus QC | passed | True | METPO:1000452 | Actual just qc passed: strict validation of 1130 records with 0 errors; graph audit: 74 baselined, 0 new and 0 blocking findings; 135 connected graphs and 1588 wired nodes; protein coverage: 729 graphs (134 pass, 594 NONMECHANISTIC, 0 gaps, 1 protected); snippet audit: 2419 baselined, 0 new and 0 blocking findings; 19 PathwayMech links. These are corpus diagnostics, not scientific validation of this target. |
| Reused B14 history integrity | passed | True | METPO:1000452 | 1278 HistoryRecord YAMLs validated, 0 invalid; current history snapshot contains 1279 files. Integrity does not establish scientific correctness or human acceptance. |
| Reused B14 mapping identifier/label validation | passed | True | METPO:1000452 | 361 canonical matches, 2 exact-synonym matches, 1 exception and 123 SKIPPED_NO_ADAPTER pairs. Configured scope is the two grounding mappings, not every target identifier or scientific claim. |
| Reused B14 focused Stage2 writer tests | passed | False | METPO:1000452 | Five tests passed in the explicitly selected Stage2 test file. This is not a full just test run or biological validation. |
| Focused native validation | passed | True | METPO:1000452 | Native record validation passed; scientific interpretation is assessed separately. |
| Focused strict validation | passed | True | METPO:1000452 | The actual validate-strict command passed. |
| Focused network snippet check | passed | True | METPO:1000452 | Native command succeeded for eleven snippets: three VERIFIED and eight NOT_IN_ABSTRACT, the latter inconclusive for body text. Separate manual matching supports all eleven literal spans; no false-quotation or adjacent exact-bin inference. |
| One-target native review capture | passed | True | METPO:1000452 | One current target, 103 captured inputs, exact current base and successful native inspect. |
| Protein-instance metadata applicability | not_applicable | False | METPO:1000452 | Two contextual protein classes are REVIEWED_LABEL_ONLY with explicit rationales and zero instances; no token accession required. |
| Structured source-organism expression query availability | unavailable | False | METPO:1000452 | Bounded maintained-runner discovery found no available adapter. Retained catalog and selected source identities provide no strain/module or efficacy result. |

## Scientific And Domain Assessments

### Native checklist: active bin and direct parent

identity: supported. Targets: METPO:1000452.

Active METPO:1000452 and direct parent METPO:1000306 are positive. Historical Mesophilie retention is documented; exact biological alias equivalence to the unresolved quantity remains unknown. Homeoviscous adaptation METPO:1016200 is local v85 proposal identity, not asserted active in the captured upstream raw OWL.

### Native checklist: four ambient-interval versus width anchors

quantity: concern. Targets: METPO:1000452.

Definition, node 0 and edge 0 describe ambient 30–34 °C, while the canonical note describes a width bin. The reported 17–50 °C interval and derived width 33 are positive. One major reconciles these four fields and exact canonical ledger without inferring quantity semantics from generic has-value alone. The current graph description is generic context and is excluded from the four numeric anchors.

### Native checklist: strain-scoped source measurement and identity

evidence: supported. Targets: METPO:1000452.

The successful canonical metadata retry supports novel strains growing at 17–50 °C and names Bacillus nakamurai NRRL B-41091T (=CCUG 68786T); 50 minus 17 equals the derived width 33. Fresh official taxonomy supports species/type-material identity only. No optimum or additional cultivation condition is adopted. The initial canonical-metadata.json is DNS error content, not primary support.

### Native checklist: five works and thirteen placements

evidence: concern. Targets: METPO:1000452.

All five identities resolve. Mendoza generic physical wording and Tolner high-temperature thermophile text do not establish the exact 30–34-bin notes. Selected Spectrum and Ramón physical/phase context remains positive. Existing supplied regulatory snippets were checked only for literal occurrence; detailed sensing, regulation, stress defense, survival/fitness, cultivation optimization and intervention efficacy remain unassessed. No whole-paper absence or biological refutation is inferred.

### Native checklist: eleven existing literal snippets

evidence: supported. Targets: METPO:1000452.

Manual matching supports all eleven current schema snippets under ordinary whitespace normalization: three abstract and eight body spans. Native three VERIFIED and eight NOT_IN_ABSTRACT are separate outcomes; the latter are inconclusive for body text. Literal occurrence does not establish adjacent numerical-bin support or detailed regulatory/fitness efficacy. No copied-span finding is added.

### Native checklist: all thirteen current referents

representation: concern. Targets: METPO:1000452.

Node 0 participates in quantity scope. Explicit membrane order, conformation and phase states, protein and chemical referents remain distinct from processes. Phosphorylated-state/material-bearer and rigidity/property readings are qualified without extra forced findings. The des_gene identifier does not override its explicit protein description. Two reviewed label-only proteins need no accession or instance; detailed regulatory efficacy remains unassessed.

{
  "grounding": [
    {
      "index": 0,
      "field": "causal_graphs[0].nodes[0]",
      "node": {
        "node_id": "temperature_range_mid3_trait",
        "label": "temperature range mid3",
        "node_type": "TRAIT",
        "grounding": "METPO:1000452",
        "description": "Temperature growth-supporting range approximately 30–34 °C."
      },
      "outcome": "concern",
      "judgment": "Active exact METPO identity; ambient30–34 wording conflicts with canonical width33 interpretation."
    },
    {
      "index": 1,
      "field": "causal_graphs[0].nodes[1]",
      "node": {
        "node_id": "temperature_range",
        "label": "temperature range",
        "node_type": "TRAIT",
        "grounding": "METPO:1000306",
        "description": "Span of ambient temperatures supporting growth."
      },
      "outcome": "positive",
      "judgment": "Exact active direct temperature-range parent; generic span wording does not itself fix the quantitative axis."
    },
    {
      "index": 2,
      "field": "causal_graphs[0].nodes[2]",
      "node": {
        "node_id": "upper_mesophile_adaptation",
        "label": "upper-mesophile adaptation",
        "node_type": "BIOLOGICAL_PROCESS",
        "description": "Mesophile membrane and enzyme tuning for ambient temperatures near common animal host body temperatures."
      },
      "outcome": "qualified",
      "judgment": "Adaptation/tuning is process-compatible documentary context. Detailed host-temperature or enzyme/fitness effects unassessed."
    },
    {
      "index": 3,
      "field": "causal_graphs[0].nodes[3]",
      "node": {
        "node_id": "membrane_order",
        "label": "membrane order / fluidity state",
        "node_type": "QUALITY",
        "description": "Physical order/fluidity state of the membrane bilayer; the proximate signal for thermosensing."
      },
      "outcome": "positive",
      "judgment": "Explicit membrane order/fluidity physical property is QUALITY; not an upstream process for RO regulation."
    },
    {
      "index": 4,
      "field": "causal_graphs[0].nodes[4]",
      "node": {
        "node_id": "desk_kinase_state",
        "label": "DesK kinase-dominant state",
        "node_type": "STATE",
        "description": "Membrane thickness sensor DesK in its autophosphorylating kinase-dominant conformation."
      },
      "outcome": "qualified",
      "judgment": "Explicit kinase-dominant conformation is a molecular STATE. Detailed response efficacy unassessed; not itself a process."
    },
    {
      "index": 5,
      "field": "causal_graphs[0].nodes[5]",
      "node": {
        "node_id": "desk",
        "label": "DesK",
        "node_type": "GENE_OR_PROTEIN",
        "grounding_status": "REVIEWED_LABEL_ONLY",
        "grounding_notes": "Reviewed as a contextual protein or protein-complex label within a quantitative measurement graph; no exact semantic family term was established for this aggregate use.",
        "description": "Membrane-bound histidine kinase that senses membrane order/thickness."
      },
      "outcome": "qualified",
      "judgment": "Named DesK protein with explicit reviewed-label-only status; material referent is clear, no accession/instance required."
    },
    {
      "index": 6,
      "field": "causal_graphs[0].nodes[6]",
      "node": {
        "node_id": "phospho_desr",
        "label": "phosphorylated DesR",
        "node_type": "STATE",
        "description": "Phosphorylated DesR that tetramerizes and binds the des promoter."
      },
      "outcome": "qualified",
      "judgment": "Phosphorylated DesR state and material bearer wording overlap. STATE modification/conformation reading is plausible; no forced additional type finding. Either reading is nonprocess for edge3."
    },
    {
      "index": 7,
      "field": "causal_graphs[0].nodes[7]",
      "node": {
        "node_id": "des_gene",
        "label": "des (acyl-lipid desaturase)",
        "node_type": "GENE_OR_PROTEIN",
        "grounding_status": "REVIEWED_LABEL_ONLY",
        "grounding_notes": "Reviewed as a contextual protein or protein-complex label within a quantitative measurement graph; no exact semantic family term was established for this aggregate use.",
        "description": "Fatty-acid desaturase that introduces double bonds to fluidize the membrane."
      },
      "outcome": "positive",
      "judgment": "Despite des_gene identifier and des label, description explicitly denotes desaturase protein. Current GENE_OR_PROTEIN is permitted; no automatic gene-as-protein finding or accession requirement."
    },
    {
      "index": 8,
      "field": "causal_graphs[0].nodes[8]",
      "node": {
        "node_id": "membrane_fatty_acyl_chains",
        "label": "membrane fatty acyl chains",
        "node_type": "CHEMICAL",
        "description": "Fatty acyl chains of membrane phospholipids whose unsaturation modulates fluidity."
      },
      "outcome": "positive",
      "judgment": "Explicit membrane fatty-acyl chemicals/material referent; not a biological process."
    },
    {
      "index": 9,
      "field": "causal_graphs[0].nodes[9]",
      "node": {
        "node_id": "membrane_rigidity",
        "label": "membrane rigidification and increased thickness",
        "node_type": "QUALITY",
        "description": "Cooling-induced membrane rigidification and bilayer thickening, the general homeoviscous sensing signal."
      },
      "outcome": "qualified",
      "judgment": "Rigidity/thickness physical attribute is a coherent QUALITY reading despite process-shaped label. Exact maintained consistency decision supports result/property facet; no forced extra finding."
    },
    {
      "index": 10,
      "field": "causal_graphs[0].nodes[10]",
      "node": {
        "node_id": "temperature_decrease",
        "label": "temperature decrease",
        "node_type": "ENVIRONMENTAL_FACTOR",
        "description": "Drop in ambient temperature within/near the mesophilic range."
      },
      "outcome": "positive",
      "judgment": "Actual drop in temperature is an event; ENVIRONMENTAL_FACTOR is not automatically excluded by enum."
    },
    {
      "index": 11,
      "field": "causal_graphs[0].nodes[11]",
      "node": {
        "node_id": "homeoviscous_adaptation",
        "label": "homeoviscous adaptation",
        "node_type": "BIOLOGICAL_PROCESS",
        "description": "Adjustment of membrane lipid composition to maintain constant fluidity across temperatures.",
        "grounding": "METPO:1016200"
      },
      "outcome": "positive",
      "judgment": "Explicit lipid-composition adjustment is a process; local v85 METPO1016200 provides exact proposal identity, absent from captured upstream raw OWL."
    },
    {
      "index": 12,
      "field": "causal_graphs[0].nodes[12]",
      "node": {
        "node_id": "liquid_crystalline_membrane",
        "label": "liquid-crystalline membrane state",
        "node_type": "STATE",
        "description": "Functional liquid-crystalline phase of the membrane required for growth."
      },
      "outcome": "positive",
      "judgment": "Liquid-crystalline phase is an explicit molecular membrane STATE, not the process of maintaining it."
    }
  ],
  "source": [
    {
      "index": 0,
      "field": "causal_graphs[0].nodes[0]",
      "node_id": "temperature_range_mid3_trait",
      "node_type": "TRAIT",
      "description": "Temperature growth-supporting range approximately 30–34 °C.",
      "outcome": "concern",
      "assessment": "Explicit ambient30–34 description participates in quantity conflict; ontology identity separate."
    },
    {
      "index": 1,
      "field": "causal_graphs[0].nodes[1]",
      "node_id": "temperature_range",
      "node_type": "TRAIT",
      "description": "Span of ambient temperatures supporting growth.",
      "outcome": "supported_generic",
      "assessment": "Parent ambient-temperature span does not settle child endpoints versus width."
    },
    {
      "index": 2,
      "field": "causal_graphs[0].nodes[2]",
      "node_id": "upper_mesophile_adaptation",
      "node_type": "BIOLOGICAL_PROCESS",
      "description": "Mesophile membrane and enzyme tuning for ambient temperatures near common animal host body temperatures.",
      "outcome": "unknown",
      "assessment": "Upper-mesophile enzyme/membrane tuning and host-body-temperature context not established by adopted generic spans; detailed efficacy unassessed."
    },
    {
      "index": 3,
      "field": "causal_graphs[0].nodes[3]",
      "node_id": "membrane_order",
      "node_type": "QUALITY",
      "description": "Physical order/fluidity state of the membrane bilayer; the proximate signal for thermosensing.",
      "outcome": "partial_generic",
      "assessment": "Generic membrane physical order/fluidity positive; specific sensor signal efficacy unassessed."
    },
    {
      "index": 4,
      "field": "causal_graphs[0].nodes[4]",
      "node_id": "desk_kinase_state",
      "node_type": "STATE",
      "description": "Membrane thickness sensor DesK in its autophosphorylating kinase-dominant conformation.",
      "outcome": "UNASSESSED_SCOPE",
      "assessment": "Existing kinase-state label/source literal context only; detailed regulation unassessed."
    },
    {
      "index": 5,
      "field": "causal_graphs[0].nodes[5]",
      "node_id": "desk",
      "node_type": "GENE_OR_PROTEIN",
      "description": "Membrane-bound histidine kinase that senses membrane order/thickness.",
      "outcome": "UNASSESSED_SCOPE",
      "assessment": "Existing DesK protein identity/literal context only; detailed response efficacy unassessed."
    },
    {
      "index": 6,
      "field": "causal_graphs[0].nodes[6]",
      "node_id": "phospho_desr",
      "node_type": "STATE",
      "description": "Phosphorylated DesR that tetramerizes and binds the des promoter.",
      "outcome": "UNASSESSED_SCOPE",
      "assessment": "Existing phosphorylated regulator label retained; detailed binding/regulatory efficacy unassessed."
    },
    {
      "index": 7,
      "field": "causal_graphs[0].nodes[7]",
      "node_id": "des_gene",
      "node_type": "GENE_OR_PROTEIN",
      "description": "Fatty-acid desaturase that introduces double bonds to fluidize the membrane.",
      "outcome": "UNASSESSED_SCOPE",
      "assessment": "Existing des/desaturase label retained; detailed effector function/fitness unassessed."
    },
    {
      "index": 8,
      "field": "causal_graphs[0].nodes[8]",
      "node_id": "membrane_fatty_acyl_chains",
      "node_type": "CHEMICAL",
      "description": "Fatty acyl chains of membrane phospholipids whose unsaturation modulates fluidity.",
      "outcome": "supported_generic",
      "assessment": "Generic fatty-acyl composition/fluidity physics positive; no Des-specific efficacy adoption."
    },
    {
      "index": 9,
      "field": "causal_graphs[0].nodes[9]",
      "node_id": "membrane_rigidity",
      "node_type": "QUALITY",
      "description": "Cooling-induced membrane rigidification and bilayer thickening, the general homeoviscous sensing signal.",
      "outcome": "supported_generic_physical",
      "assessment": "Generic cooling rigidity/thickness sentence positive; detailed sensing efficacy unassessed."
    },
    {
      "index": 10,
      "field": "causal_graphs[0].nodes[10]",
      "node_id": "temperature_decrease",
      "node_type": "ENVIRONMENTAL_FACTOR",
      "description": "Drop in ambient temperature within/near the mesophilic range.",
      "outcome": "supported_generic",
      "assessment": "Ambient temperature drop is generic environmental context, no exact-bin efficacy."
    },
    {
      "index": 11,
      "field": "causal_graphs[0].nodes[11]",
      "node_id": "homeoviscous_adaptation",
      "node_type": "BIOLOGICAL_PROCESS",
      "description": "Adjustment of membrane lipid composition to maintain constant fluidity across temperatures.",
      "outcome": "partial_generic",
      "assessment": "Generic lipid-composition/phase context positive; detailed regulation/constant-fluidity efficacy unassessed."
    },
    {
      "index": 12,
      "field": "causal_graphs[0].nodes[12]",
      "node_id": "liquid_crystalline_membrane",
      "node_type": "STATE",
      "description": "Functional liquid-crystalline phase of the membrane required for growth.",
      "outcome": "partial_generic",
      "assessment": "Liquid-crystalline phase physical context positive; required-for-growth/survival efficacy unassessed."
    }
  ]
}

### Native checklist: all ten current relations

consistency: concern. Targets: METPO:1000452.

Edges 2/3/4/9 import RO2213 or RO2211 process-to-process roles over explicit quality, state, protein and chemical endpoints. Edge 6 imports RO2326 material-to-process roles for adaptation process to membrane phase state. One formal-role major covers all five fields. Broad local confers, direct subclass and Biolink causes/associated_with endpoint compatibility remain positive or qualified without proving detailed biology or association statistics. No replacement predicate, intermediate or mechanism repair is invented.

{
  "grounding": [
    {
      "index": 0,
      "field": "causal_graphs[0].edges[0]",
      "edge": {
        "subject": "upper_mesophile_adaptation",
        "predicate": "confers",
        "object": "temperature_range_mid3_trait",
        "description": "Upper-mesophile adaptation enables growth across 30–34 °C.",
        "evidence": [
          {
            "reference": "DOI:10.1146/annurev-micro-091313-103612",
            "snippet": "more unsaturated fatty acids",
            "notes": "Supports upper-mesophile homeoviscous adaptation as the range mechanism."
          }
        ],
        "predicate_id": "METPO:2007700"
      },
      "outcome": "qualified",
      "judgment": "Local v8 broad confers permits process/context→trait; exact quantitative interpretation is separately conflicting, detailed efficacy unassessed."
    },
    {
      "index": 1,
      "field": "causal_graphs[0].edges[1]",
      "edge": {
        "subject": "temperature_range_mid3_trait",
        "predicate": "is a",
        "object": "temperature_range",
        "description": "Temperature range mid3 is a quantitative bin of the temperature-range phenotype.",
        "evidence": [
          {
            "reference": "DOI:10.1016/s0300-9629(97)00003-0",
            "snippet": "adapted to environments of high temperature",
            "notes": "Supports the 30–34 °C range as a value within the temperature-range distribution."
          }
        ],
        "predicate_id": "rdfs:subClassOf"
      },
      "outcome": "positive",
      "judgment": "rdfs:subClassOf is supported by exact raw METPO child/parent hierarchy."
    },
    {
      "index": 2,
      "field": "causal_graphs[0].edges[2]",
      "edge": {
        "subject": "membrane_order",
        "predicate": "positively regulates",
        "object": "desk_kinase_state",
        "description": "Increased membrane order (reduced fluidity) promotes the DesK kinase-dominant state; membrane physical state is the proximate signal.",
        "evidence": [
          {
            "reference": "DOI:10.1128/spectrum.03925-23",
            "snippet": "Upon temperature decrease, the membrane rigidifies and increases in thickness, resulting in activation of the kinase-dominant state of DesK",
            "notes": "Verified against the open Sidarta et al. introduction; the current Des model links temperature-decrease-driven membrane rigidification/thickening to the active kinase-dominant state."
          }
        ],
        "predicate_id": "RO:0002213"
      },
      "outcome": "major",
      "judgment": "RO2213 inherits RO2211 process/process; membrane-order QUALITY→kinase conformation STATE violates both imported endpoints."
    },
    {
      "index": 3,
      "field": "causal_graphs[0].edges[3]",
      "edge": {
        "subject": "phospho_desr",
        "predicate": "positively regulates",
        "object": "des_gene",
        "description": "DesR-P tetramerizes, binds the des promoter, and positively regulates des expression for lipid desaturation.",
        "evidence": [
          {
            "reference": "DOI:10.1128/spectrum.03925-23",
            "snippet": "activating expression of the des gene",
            "notes": "Verified against the open Sidarta et al. introduction; phosphorylated DesR tetramers bind Pdes and activate des transcription."
          }
        ],
        "predicate_id": "RO:0002213"
      },
      "outcome": "major",
      "judgment": "RO2213 process/process receives phosphorylated state/material subject and explicitly protein object. Protein object independently violates range; transcription prose does not change literal endpoint."
    },
    {
      "index": 4,
      "field": "causal_graphs[0].edges[4]",
      "edge": {
        "subject": "des_gene",
        "predicate": "regulates",
        "object": "membrane_fatty_acyl_chains",
        "description": "Des-mediated unsaturation regulates membrane fatty acyl chains, fluidizing the membrane and reducing bilayer thickness.",
        "evidence": [
          {
            "reference": "DOI:10.1128/spectrum.03925-23",
            "snippet": "desaturates the fatty acyl chains",
            "notes": "Verified against the open Sidarta et al. introduction; Des desaturates membrane-lipid fatty acyl chains as the effector of the DesK/DesR temperature-sensing system."
          }
        ],
        "predicate_id": "RO:0002211"
      },
      "outcome": "major",
      "judgment": "RO2211 directly requires process/process; desaturase protein→fatty-acyl chemical endpoints are material referents, irrespective of activity described in prose."
    },
    {
      "index": 5,
      "field": "causal_graphs[0].edges[5]",
      "edge": {
        "subject": "temperature_decrease",
        "predicate": "causes",
        "object": "membrane_rigidity",
        "description": "A temperature decrease causes membrane rigidification and increased thickness, a physical trigger for homeoviscous adaptation.",
        "evidence": [
          {
            "reference": "DOI:10.1128/spectrum.03925-23",
            "snippet": "rigidification and concomitant thickening",
            "notes": "Verified against the open Sidarta et al. introduction; temperature decrease is described as causing cell-membrane rigidification and thickening."
          }
        ],
        "predicate_id": "biolink:causes"
      },
      "outcome": "positive",
      "judgment": "Biolink causes has broad named-thing ancestry, not RO process/process. Actual temperature-decrease event→rigidity property is domain/range compatible; detailed causal efficacy unassessed."
    },
    {
      "index": 6,
      "field": "causal_graphs[0].edges[6]",
      "edge": {
        "subject": "homeoviscous_adaptation",
        "predicate": "contributes to",
        "object": "liquid_crystalline_membrane",
        "description": "Homeoviscous adaptation contributes to a functional liquid-crystalline membrane state at low temperature.",
        "evidence": [
          {
            "reference": "DOI:10.1007/s42770-023-01057-4",
            "snippet": "maintain the liquid crystalline phase",
            "notes": "Verified against the open Ramón et al. review; organisms in cold environments are described as adapting their membrane composition to maintain a liquid-crystalline state."
          }
        ],
        "predicate_id": "RO:0002326"
      },
      "outcome": "major",
      "judgment": "RO2326→2216→2500→2595 inherits material-entity domain and process range. Explicit adaptation process→liquid-crystalline STATE violates both roles."
    },
    {
      "index": 7,
      "field": "causal_graphs[0].edges[7]",
      "edge": {
        "subject": "membrane_rigidity",
        "predicate": "associated with",
        "object": "membrane_order",
        "description": "Cooling-induced membrane rigidification is associated with the ordered membrane state sensed by DesK.",
        "evidence": [
          {
            "reference": "DOI:10.1128/spectrum.03925-23",
            "snippet": "membrane rigidifies and increases in thickness",
            "notes": "Verified against the open Sidarta et al. introduction; this connector joins the cooling membrane signal to the DesK kinase-state branch."
          }
        ],
        "predicate_id": "biolink:associated_with"
      },
      "outcome": "qualified",
      "judgment": "Biolink associated_with broad named-thing endpoints permit physical-property association. Detailed source/causal interpretation unassessed; no imported RO constraint."
    },
    {
      "index": 8,
      "field": "causal_graphs[0].edges[8]",
      "edge": {
        "subject": "membrane_fatty_acyl_chains",
        "predicate": "associated with",
        "object": "homeoviscous_adaptation",
        "description": "Des-mediated fatty-acyl-chain unsaturation is associated with homeoviscous membrane adaptation.",
        "evidence": [
          {
            "reference": "DOI:10.1128/spectrum.03925-23",
            "snippet": "resulting in membrane fluidization and concomitant decrease of bilayer thickness",
            "notes": "Verified against the open Sidarta et al. introduction; this connector keeps des expression as membrane-fatty-acyl remodeling context."
          }
        ],
        "predicate_id": "biolink:associated_with"
      },
      "outcome": "qualified",
      "judgment": "Biolink associated_with admits material→process referents. Edge description shifts toward unsaturation activity, retained as a bounded interpretation limitation, not a formal domain failure or efficacy verdict."
    },
    {
      "index": 9,
      "field": "causal_graphs[0].edges[9]",
      "edge": {
        "subject": "desk",
        "predicate": "regulates",
        "object": "phospho_desr",
        "description": "DesK regulates DesR phosphorylation in the core two-component signaling step linking membrane physical state to transcriptional response.",
        "evidence": [
          {
            "reference": "DOI:10.1128/spectrum.03925-23",
            "snippet": "phosphorylating or dephosphorylating DesR",
            "notes": "Verified against the open Sidarta et al. introduction; DesK is described as a membrane-associated histidine kinase that phosphorylates or dephosphorylates DesR in a temperature-dependent manner."
          }
        ],
        "predicate_id": "RO:0002211"
      },
      "outcome": "major",
      "judgment": "RO2211 process/process receives explicit DesK protein→phosphorylated STATE/material bearer. Literal endpoints remain nonprocess despite phosphorylation-action prose."
    }
  ],
  "source": [
    {
      "index": 0,
      "field": "causal_graphs[0].edges[0]",
      "subject": "upper_mesophile_adaptation",
      "predicate": "confers",
      "object": "temperature_range_mid3_trait",
      "description": "Upper-mesophile adaptation enables growth across 30–34 °C.",
      "references": [
        "DOI:10.1146/annurev-micro-091313-103612"
      ],
      "outcome": "unknown_exact_bin",
      "assessment": "Generic physical phrase literal; upper-mesophile mechanism/exact-bin sufficiency unassessed. Description explicitly uses ambient interval."
    },
    {
      "index": 1,
      "field": "causal_graphs[0].edges[1]",
      "subject": "temperature_range_mid3_trait",
      "predicate": "is a",
      "object": "temperature_range",
      "description": "Temperature range mid3 is a quantitative bin of the temperature-range phenotype.",
      "references": [
        "DOI:10.1016/s0300-9629(97)00003-0"
      ],
      "outcome": "attribution_concern",
      "assessment": "Literal phrase explicitly thermophile context; nearest span does not establish exact30–34 note. Formal hierarchy separate."
    },
    {
      "index": 2,
      "field": "causal_graphs[0].edges[2]",
      "subject": "membrane_order",
      "predicate": "positively regulates",
      "object": "desk_kinase_state",
      "description": "Increased membrane order (reduced fluidity) promotes the DesK kinase-dominant state; membrane physical state is the proximate signal.",
      "references": [
        "DOI:10.1128/spectrum.03925-23"
      ],
      "outcome": "UNASSESSED_SCOPE",
      "assessment": "Supplied snippet literal; detailed DesK kinase-state regulation/efficacy unassessed."
    },
    {
      "index": 3,
      "field": "causal_graphs[0].edges[3]",
      "subject": "phospho_desr",
      "predicate": "positively regulates",
      "object": "des_gene",
      "description": "DesR-P tetramerizes, binds the des promoter, and positively regulates des expression for lipid desaturation.",
      "references": [
        "DOI:10.1128/spectrum.03925-23"
      ],
      "outcome": "UNASSESSED_SCOPE",
      "assessment": "Supplied snippet literal; detailed DesR transcriptional regulation/efficacy unassessed."
    },
    {
      "index": 4,
      "field": "causal_graphs[0].edges[4]",
      "subject": "des_gene",
      "predicate": "regulates",
      "object": "membrane_fatty_acyl_chains",
      "description": "Des-mediated unsaturation regulates membrane fatty acyl chains, fluidizing the membrane and reducing bilayer thickness.",
      "references": [
        "DOI:10.1128/spectrum.03925-23"
      ],
      "outcome": "UNASSESSED_SCOPE",
      "assessment": "Supplied snippet literal; detailed Des-mediated effector/regulatory efficacy unassessed."
    },
    {
      "index": 5,
      "field": "causal_graphs[0].edges[5]",
      "subject": "temperature_decrease",
      "predicate": "causes",
      "object": "membrane_rigidity",
      "description": "A temperature decrease causes membrane rigidification and increased thickness, a physical trigger for homeoviscous adaptation.",
      "references": [
        "DOI:10.1128/spectrum.03925-23"
      ],
      "outcome": "supported_generic_physical",
      "assessment": "Selected Spectrum body p1 final sentence supports generic cooling, rigidity and thickness, not detailed adaptation efficacy."
    },
    {
      "index": 6,
      "field": "causal_graphs[0].edges[6]",
      "subject": "homeoviscous_adaptation",
      "predicate": "contributes to",
      "object": "liquid_crystalline_membrane",
      "description": "Homeoviscous adaptation contributes to a functional liquid-crystalline membrane state at low temperature.",
      "references": [
        "DOI:10.1007/s42770-023-01057-4"
      ],
      "outcome": "partial_generic_literal",
      "assessment": "Supplied phase-maintenance phrase literal; generic phase context positive, survival/adaptive efficacy and exact-bin sufficiency unassessed."
    },
    {
      "index": 7,
      "field": "causal_graphs[0].edges[7]",
      "subject": "membrane_rigidity",
      "predicate": "associated with",
      "object": "membrane_order",
      "description": "Cooling-induced membrane rigidification is associated with the ordered membrane state sensed by DesK.",
      "references": [
        "DOI:10.1128/spectrum.03925-23"
      ],
      "outcome": "partial_generic_literal",
      "assessment": "Supplied physical-change phrase literal; generic rigidity/order context positive, specific sensing/regulatory coupling unassessed."
    },
    {
      "index": 8,
      "field": "causal_graphs[0].edges[8]",
      "subject": "membrane_fatty_acyl_chains",
      "predicate": "associated with",
      "object": "homeoviscous_adaptation",
      "description": "Des-mediated fatty-acyl-chain unsaturation is associated with homeoviscous membrane adaptation.",
      "references": [
        "DOI:10.1128/spectrum.03925-23"
      ],
      "outcome": "UNASSESSED_SCOPE",
      "assessment": "Supplied phrase literal; detailed Des remodeling/regulation efficacy unassessed."
    },
    {
      "index": 9,
      "field": "causal_graphs[0].edges[9]",
      "subject": "desk",
      "predicate": "regulates",
      "object": "phospho_desr",
      "description": "DesK regulates DesR phosphorylation in the core two-component signaling step linking membrane physical state to transcriptional response.",
      "references": [
        "DOI:10.1128/spectrum.03925-23"
      ],
      "outcome": "UNASSESSED_SCOPE",
      "assessment": "Supplied phrase literal; detailed DesK/DesR phosphoregulation efficacy unassessed."
    }
  ]
}

### Native checklist: exact templates and distinct guarded consumers

ownership: supported. Targets: METPO:1000452.

Canonical SOURCES/TRANCHE preserves the correct measurement and width; coordinate interpretation with equality/no-op, nonempty rejection and queue guards. The review after-payloads match current edges, implying a current no-op; connector SOURCE_CONNECTOR_EDGES are guards and its metadata preimage currently rejects. PR664 replaces matching triples from templates and differs from the generic predicate grounder, which skips populated IDs. Mapping rows 10/11/99 are conditional recurrence inputs. These are static inferences, not executed writer outcomes.

### Native checklist: bounded human acceptance link

provenance: concern. Targets: METPO:1000452.

Nineteen embedded events comprise eighteen AI-assisted events and a seed. All 26 current actor projections are AI; whole-history scope is 25 exact qualified prior readings plus one fresh infrastructure history. Ignored- and hidden-inclusive search excluding .git/.venv internals found 191 matching paths and 69 matching arrays; all 94 actual local top-level review target arrays have zero exact match. Private/remote acceptance remains unknown.

### Native checklist: retained species catalog and bounded adapter availability

completeness: unknown. Targets: METPO:1000452.

The retained original catalog contains 20 organisms and 28 datasets. B. subtilis adopted title context has species-level coverage only, with no strain/module or efficacy result; no exact B. nakamurai canonical key was found. A maintained runner was unavailable within bounded current discovery, so no module query was executed. This does not establish global organism absence.

### Native checklist: intentional NONMECHANISTIC components and label-only proteins

completeness: supported. Targets: METPO:1000452.

Three components with thirteen nodes and ten edges are explicitly retained by current NONMECHANISTIC corrective history. Two reviewed label-only proteins and zero instances require no invented connector, accession or dataset. Historical protein/component counts are not substituted for current structure. These positives do not resolve quantity, attribution or formal-role findings.

### Native checklist: current native checks and qualified B14 diagnostics

schema: supported. Targets: METPO:1000452.

Current inspect, target validation, strict validation and snippet checks are successful B15 executions. Four original B14 common diagnostics are qualified for unchanged B15 inputs, not relabeled as fresh B15 executions. Original intervals, historical attempts, product skips and omitted full just test remain explicit. These eight command checks do not establish scientific correctness or human acceptance.

## Findings

### quantity-scope: Quantity scope

major / open / confirmed; issue key: temperature-range-mid3-quantity-scope.

The definition, node0 and edge0 use30–34 °C as ambient temperatures; the canonical note treats30–34 degrees as an interval-width bin. Primary PMID27150918 reports novel strains growing at17–50 °C and identifies Bacillus nakamurai NRRL B-41091T, giving derived50−17=33. The measurement and arithmetic are positive. Raw METPO gives a generic existential value in[30,34], which does not select endpoints versus width. Reconcile the operational quantity and canonical membership with the exact maintained ledger. The current graph description contains generic context and is excluded from the four explicit numeric anchors.

### imported-process-roles: Imported process roles

major / open / confirmed; issue key: temperature-range-mid3-imported-process-roles.

Edges2/3 use RO:0002213 and edges4/9 use RO:0002211, requiring process-to-process roles. Their explicit quality, molecular-state, protein and chemical referents are nonprocess endpoints. Edge6 uses RO:0002326, whose2326→2216→2500→2595 ancestry requires material entity→process, for an adaptation process→membrane phase state. Exact review after-payloads match current edges, so the review transform would no-op; the connector holds these as source guards and currently rejects its metadata preimage. The PR664 consumer replaces matched triples from those templates, unlike the generic grounder, which skips populated IDs. Wildcard mapping rows10/11/99 are conditional recurrence inputs. Coordinate these distinct owner roles without inventing biological intermediates or relabeling referents merely to satisfy predicates.

### bin-attribution: Bin attribution

minor / open / confirmed; issue key: temperature-range-mid3-bin-attribution.

The Mendoza note attributes exact30–34 °C upper-mesophile support to a generic membrane-physics phrase. The Tolner note attributes that bin to a supplied phrase explicitly concerning high-temperature thermophiles. Both snippets are literal; the nearest inspected spans do not establish the adjacent exact numerical-bin claims. This bounded attribution concern is separate from quantity semantics and does not assert whole-paper absence, false quotation or biological refutation. The subclass relation has independent raw-ontology support.

### human-acceptance-link: Human acceptance link

minor / open / confirmed; issue key: temperature-range-mid3-human-acceptance-link.

REVIEWED status has no retrievable exact-target human acceptance in the bounded local evidence. The19 embedded events comprise18 AI-assisted entries and the METPO seed. All26 current captured history actor projections are AI;25 whole readings are exact qualified prior readings and one infrastructure history was read whole currently. Ignored- and hidden-inclusive local discovery excluding.git/.venv internals found191 matching paths and69 matching review arrays; all94 actual local top-level target arrays contain zero exact target matches. Private or remote acceptance remains unknown.

## Recommended Actions And Acceptance Checks

### curate-quantity-scope

In separately authorized curation, define the measured quantity and reconcile the four numeric anchors with the canonical ledger.

- Establish source-backed quantity and units without deriving endpoints versus width from generic has-value alone.
- Preserve reported17–50 °C and explicitly derived width33; distinguish these positive observations from bin membership.
- Coordinate SOURCES88–90/TRANCHE607–612 and equality/no-op, nonempty-rejection and global queue guards. The correct measurement is not a false writer payload.
- Use guarded record/history curation, focused strict validation and applicable QC/products; regenerate affected products.

### curate-imported-process-roles

Resolve the five imported relation assertions against the existing declared referents and coordinate exact templates, consumer guards and conditional mapping recurrence.

- Document each edge subject/object referent and effective domain/range; preserve quality, state, material and process distinctions.
- Coordinate review EDGE_REPLACEMENTS, connector SOURCE_CONNECTOR_EDGES guards and PR664 matched-triple replacement/repair addition behavior. The connector surviving additions are two broad associations, not the conflicting RO payload source.
- Address contributes-to row10, regulates row11 and positively-regulates row99 for future empty fields; explicit guarded curation must address current populated IDs.
- Use meaningful focused grounding/guard regression checks, strict validation and applicable QC/products. No pathway addition, operational mechanism repair or efficacy improvement is prescribed.

### curate-bin-attribution

Qualify the two notes to distinguish generic physical or thermophile context from exact numerical-bin authority.

- Describe the nearest inspected spans accurately; exact30–34 calibration needs identified support or remains qualified.
- Preserve all11 literal snippets and distinguish manual body matching from native3 VERIFIED/8 NOT_IN_ABSTRACT inconclusive outcomes.
- Preserve independently supported hierarchy and avoid whole-paper absence or false-quotation claims; validate separately curated changes.

### curate-human-acceptance-link

Link attributable human acceptance for REVIEWED status or accurately qualify the review state in separately authorized curation.

- Provide actor identity, exact scope and retrievable acceptance; AI history and seed import do not establish human signoff.
- Retain bounded local-search scope and private/remote uncertainty.
- Use maintained guarded history and validation for any curation change.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| common-reuse-qualification | /private/tmp/traitmech-record-sweep-015.67f2ce7a/common-diagnostic-reuse-qualification.json; Current B15 source maps, maintained inputs and five cache databases qualified against identified B14 diagnostics | context_only | Reuse qualification only; original B14 times retained, no B15 diagnostic execution or B14 finalization asserted. |
| original-b14-common-completion | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/new-base-diagnostic-independent-review-agent/fresh-products-completion.json; Original B14 products completion and diagnostic evidence | context_only | Original four B14 diagnostics, historical attempts and original cache provenance; B14-to-B13 comparison remains false. |
| check-new-base-qc | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/new-base-qc.log; Executed 2026-10-21T23:25:15.125723+00:00 through 2026-10-21T23:26:53.864156+00:00; metadata new-base-qc.json | context_only | Actual just qc passed: strict validation of 1130 records with 0 errors; graph audit: 74 baselined, 0 new and 0 blocking findings; 135 connected graphs and 1588 wired nodes; protein coverage: 729 graphs (134 pass, 594 NONMECHANISTIC, 0 gaps, 1 protected); snippet audit: 2419 baselined, 0 new and 0 blocking findings; 19 PathwayMech links. These are corpus diagnostics, not scientific validation of this target. |
| check-new-base-history | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/new-base-history.log; Executed 2026-10-21T23:25:15.125609+00:00 through 2026-10-21T23:25:19.527774+00:00; metadata new-base-history.json | context_only | 1278 HistoryRecord YAMLs validated, 0 invalid; current history snapshot contains 1279 files. Integrity does not establish scientific correctness or human acceptance. |
| check-new-base-products | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/new-base-products.log; Executed 2026-10-21T23:29:02.243310+00:00 through 2026-10-21T23:29:27.250859+00:00; metadata new-base-products.json | context_only | 361 canonical matches, 2 exact-synonym matches, 1 exception and 123 SKIPPED_NO_ADAPTER pairs. Configured scope is the two grounding mappings, not every target identifier or scientific claim. |
| check-new-base-stage2-tests | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/new-base-stage2-tests.log; Executed 2026-10-21T23:25:19.981459+00:00 through 2026-10-21T23:25:21.660071+00:00; metadata new-base-stage2-tests.json | context_only | Five tests passed in the explicitly selected Stage2 test file. This is not a full just test run or biological validation. |
| historical-validate-products | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log; Historical original execution 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z | context_only | Historical products exit 2; preserved provenance only, superseded for B14 by its actual fresh products run. |
| historical-validate-products-retry-local | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log; Historical original execution 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z | context_only | Historical products exit 2; preserved provenance only, superseded for B14 by its actual fresh products run. |
| historical-validate-products-retry-network | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log; Historical original execution 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z | context_only | Historical products exit 0; preserved provenance only, superseded for B14 by its actual fresh products run. |
| check-temperature-range-mid3-target-validate | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-target-validate.log; Executed 2026-10-22T04:24:46.825109+00:00 through 2026-10-22T04:24:47.779367+00:00; metadata temperature-range-mid3-target-validate.json | context_only | Native record validation passed; scientific interpretation is assessed separately. |
| check-temperature-range-mid3-target-strict | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-target-strict.log; Executed 2026-10-22T04:24:46.825108+00:00 through 2026-10-22T04:24:48.371122+00:00; metadata temperature-range-mid3-target-strict.json | context_only | The actual validate-strict command passed. |
| check-temperature-range-mid3-snippets-network | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-snippets-network.log; Executed 2026-10-22T04:25:04.430475+00:00 through 2026-10-22T04:25:11.700686+00:00; metadata temperature-range-mid3-snippets-network.json | context_only | Native command succeeded for eleven snippets: three VERIFIED and eight NOT_IN_ABSTRACT, the latter inconclusive for body text. Separate manual matching supports all eleven literal spans; no false-quotation or adjacent exact-bin inference. |
| capture | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3.inspect.json; Actual successful native inspect with 103 captured inputs | context_only | All current captured source hashes and the exact target are bound before serialization. |
| record | data/traits/environment/temperature_range_mid3.yaml; Whole current record | supports | Thirteen nodes, ten edges, nineteen embedded events, one canonical example, two reviewed label-only protein classes and zero instances. |
| local-init | /private/tmp/traitmech-record-sweep-015.67f2ce7a/batch015-local-initialization-receipt.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Actual local initialization and third queue target; publication remains separate. |
| policy | docs/GROUNDING_POLICY.md; Captured maintained authority | supports | Protein family/function grounding, reviewed label-only aggregates and optional instances. |
| playbook | docs/CURATION_PLAYBOOK.md; Captured maintained authority | supports | Source attribution and attributable acceptance. |
| schema | src/traitmech/schema/traitmech.yaml; Captured maintained authority | supports | Current material, molecular-activity, process, quality and quantitative NONMECHANISTIC facets. |
| predicate-mapping | mappings/predicate_grounding.tsv; Captured maintained authority | supports | Wildcard contributes-to row 10, regulates row 11 and positively-regulates row 99 can recreate incompatible imported roles in future empty fields; the generic consumer skips populated IDs. |
| canonical-writer | scripts/backfill_canonical_examples_444.py; Captured maintained authority | supports | Exact Bacillus nakamurai SOURCES/TRANCHE payload and equality, rejection and global queue guards; positive interval and width with coordinated quantity interpretation. |
| identity | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-grounding-agent/identity-and-hierarchy.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Active target and parent; historical Mesophilie retention and unresolved broad qualitative equivalence. Generic numeric existential does not decide endpoints versus width. |
| nodes-edges | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-grounding-agent/node-edge-grounding-ledger.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | All thirteen current node referents and ten formal relation dispositions. |
| owners | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-grounding-agent/ownership-assessment.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Exact canonical, review/connector/PR664 and conditional mapping ownership, with distinct current replay guards. |
| owner-primary | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-grounding-agent/owner-primary-reading.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Selected current owner windows and exact replay guards without writer execution. |
| local-authority | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-grounding-agent/local-authority-reading.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Actual schema, policy, local proposals and mapping reading scope. |
| histories | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-grounding-agent/history-reading-provenance.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Twenty-six current actor/event projections: 25 exact qualified prior whole readings and one fresh whole infrastructure-history reading. |
| embedded-history | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-grounding-agent/embedded-history-ledger.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Nineteen embedded events: eighteen AI-assisted events and one seed. |
| human-search | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-grounding-agent/search-and-provenance.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Ignored- and hidden-inclusive local search: 191 matching paths, 69 matching arrays and 94 all-local review arrays, zero exact target. |
| discovery | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-grounding-agent/discovery-dispositions.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Uncaptured leads remain matching-line context; private or remote acceptance unknown. |
| expression | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-grounding-agent/expression-and-readiness.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Three intentionally retained NONMECHANISTIC components and two reviewed label-only protein classes are allowed; B. subtilis title context has species coverage only, with no canonical key or module result. |
| expression-discovery | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-grounding-agent/adapter-discovery.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Bounded maintained-runner discovery found no available adapter; no query executed. |
| catalog-reuse | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-grounding-agent/catalog-reuse.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Original catalog acquisition preserved separately from current copying and selected-name reading. |
| ground-reading | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-grounding-agent/reading-scope-receipt.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Exact current reading scopes, qualified prior histories and owner qualifications. |
| ground-assessment | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-grounding-agent/grounding-assessment.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Two ground majors include the shared quantity finding counted once; bounded human minor. |
| ground-manifest | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-grounding-agent/evidence-manifest.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | All 27 immutable ground artifacts verified. |
| ontology-primary | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-source-root/selected-ontology-primary.json; Exact selected response; query 2026-10-22T04:25:22.418934+00:00 through 2026-10-22T04:25:22.424008+00:00 | supports | Current RO/BFO, raw METPO, local v8/v85 and Biolink selected authority. Copy/read time is not query time. Ground auditor did not repeat queries or database hashing; the serializer common guard separately verifies qualified inputs. |
| authority-primary | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-source-root/selected-authority-primary.json; Exact selected response; query 2026-10-22T04:25:22.424722+00:00 through 2026-10-22T04:25:22.718499+00:00 | supports | Current RO/BFO, raw METPO, local v8/v85 and Biolink selected authority. Copy/read time is not query time. Ground auditor did not repeat queries or database hashing; the serializer common guard separately verifies qualified inputs. |
| authority-provenance | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-grounding-agent/primary-reuse-provenance.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Actual current root query clocks and exact ground-auditor copies; separate reading completion. |
| catalog-original | https://imodulondb.org/api/datasets; Original retained 20-organism/28-dataset catalog | context_only | No exact Bacillus nakamurai canonical key in this retained catalog. B. subtilis title context has species-level coverage only; no strain/module, phenotype or efficacy inference. |
| mendoza-metadata | DOI:10.1146/annurev-micro-091313-103612; Indexed identity and first abstract sentence | supports | Supplied generic physical fragment is literal; nearest inspected wording does not establish exact 30–34-bin calibration. |
| mendoza-publisher | DOI:10.1146/annurev-micro-091313-103612; Retained publisher browser-tool export; historical call interval, not raw HTML | supports | Selected abstract wording retained. Underlying cache fetch time is unknown; no current fresh publisher acquisition is claimed. |
| cold-metadata | DOI:10.1007/s42770-023-01057-4; Indexed identity and original notice fields | supports | Identity verified; detailed stress-defense and survival efficacy remain unassessed. |
| cold-body | DOI:10.1007/s42770-023-01057-4; Source-auditor zero-based all-HTML paragraph 17 supplied phase fragment; root first four physical sentences separately bounded | supports | Existing fragment literal and generic phase context positive. Surrounding survival/freezing wording and detailed adaptive efficacy remain unassessed; no new body acquisition. |
| tolner-metadata | DOI:10.1016/s0300-9629(97)00003-0; Indexed identity and first two thermophile abstract sentences | supports | Supplied snippet is literal and explicitly concerns high-temperature thermophiles; adjacent exact-bin support is not established. |
| tolner-crossref | DOI:10.1016/s0300-9629(97)00003-0; Original Crossref identifier/title | supports | Source identity positive; no detailed transport or regulatory efficacy assessed. |
| spectrum-body | DOI:10.1128/spectrum.03925-23; Zero-based body paragraph 1 first/final generic physical sentences; paragraphs 3/5 machine matching of supplied short spans only | supports | Current supplied snippets occur literally. Detailed DesK/DesR/des regulation, sensing efficacy, survival/fitness and intervention effects are UNASSESSED_SCOPE; exact-bin sufficiency is not established. |
| spectrum-metadata | DOI:10.1128/spectrum.03925-23; Indexed source identity, title and original notice fields | supports | B. subtilis title context only; no strain/module or detailed efficacy inference. |
| canonical-metadata | DOI:10.1099/ijsem.0.001135; Successful retry primary abstract: existing growth sentence and named type-strain statement | supports | Bacillus nakamurai NRRL B-41091T (=CCUG 68786T), reported 17–50 °C interval and explicitly derived width 33 are positive. Other cultivation, optimum, genomic or chemical details are not adopted. |
| canonical-access | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-source-agent/canonical-metadata-network-retry-access.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Current successful canonical metadata retry interval, separate from initial DNS failure and eight historical source copies. |
| canonical-initial-failure | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1099%2Fijsem.0.001135&amp;format=json&amp;resultType=core; Initial DNS error bytes, not canonical metadata | context_only | Only the separate successful network-retry response supplies canonical evidence. This access failure is not native validation failure. |
| taxonomy | NCBITaxon:1793963; Fresh successful official species/type-material response | supports | Bacillus nakamurai species and NRRL B-41091/CCUG 68786 type-material identities positive; no quantitative phenotype inferred from taxonomy. |
| taxonomy-access | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-grounding-agent/taxonomy-retry-access.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Actual successful retry interval and hash. |
| taxonomy-reading | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-grounding-agent/taxonomy-identity.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Official identity, successful response and separate initial failed access. |
| taxonomy-initial-failure | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1793963&amp;retmode=xml; Initial DNS error bytes, not taxonomy XML | context_only | Access failure is retained separately from successful retry and native validation. |
| sources | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-source-agent/source-assessment.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Five works; shared quantity conflict and bounded nearest-span attribution concern, with detailed efficacy unassessed. |
| source-identities | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-source-agent/source-ledger.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | All five identities and selected scopes; reused metadata notices retain original times, alongside the successful current canonical metadata retry. |
| source-status | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-source-agent/source-status-ledger.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Original-time notice observations, not an exhaustive fresh status search. |
| placements | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-source-agent/source-placement-ledger.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | All thirteen external placements; thirteen grounding fields are separately covered by node-edge audits. |
| snippets | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-source-agent/snippet-ledger.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | All eleven supplied snippets are literal: three in indexed abstracts and eight in retained body text. Detailed biological efficacy remains unassessed. |
| notes | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-source-agent/source-note-ledger.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Twelve notes including the singular canonical note; exact-bin attribution distinct from literal text. |
| source-nodes-edges | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-source-agent/node-edge-source-ledger.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | All thirteen nodes and ten edges with supported, partial, unknown and unassessed dispositions. |
| canonical | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-source-agent/canonical-assessment.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Named source interval and derived width positive, incompatible current quantity interpretations grouped once. |
| source-reading | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-source-agent/primary-reading-scope.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Selected identity, physical/classification text and literal spans; no whole-paper or detailed efficacy review. |
| source-access | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-source-agent/source-access-limits.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Eight retained primary surfaces and one current successful canonical metadata retry after DNS failure; no current body acquisition. |
| source-reuse | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-source-agent/source-reuse-receipt.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Eight exact copies with flat original-access clocks and prior-receipt hashes; current canonical failure/retry are separate. |
| source-native | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-source-agent/native-context.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Native three VERIFIED/eight NOT_IN_ABSTRACT inconclusive results, separate from manual eleven literal matches. |
| source-manifest | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-source-agent/evidence-manifest.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | All 26 frozen source artifacts verified. |
| writer-payloads | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-grounding-agent/writer-payload-comparison.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | AST-only exact current after-payload comparison and guard inference: review no-op, connector preimage rejection and PR664 matched-triple consumer are distinct. No writer imported or executed. |
| root-reading | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-source-root/selected-primary-reading.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Root corrected selected source, authority and owner reading scopes, narrower than some source-auditor windows; incidental content not adopted. |
| root-verification | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-source-root/root-current-verification.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Root exact current input, frozen artifact, qualified history and local review-array verification. |
| adjudication | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-root-adjudication.json; Final root adjudication | supports | Exact two majors and two minors, four findings/actions and owner/field scopes control this combined review. |

## Limits And Additional Notes

- No fresh B15 common diagnostic execution is asserted. Full just test was NOT_RUN; only the five optional focused Stage2 tests are reused. Products retains 123 no-adapter skips and covers two configured mappings. Common checks establish bounded software/data integrity, not scientific support, current-target checks or prior-batch finalization. Serializers must append to these helper notes and limitations.
- Detailed stress-defense/regulatory/survival/fitness/cultivation optimization/intervention efficacy UNASSESSED_SCOPE; no operational repairs.
- Canonical interval17–50 and derivedwidth33 positive; ambient30–34 versus width30–34 counted once.
- All11 snippets literal; native3 VERIFIED/8 NOT_IN_ABSTRACT inconclusive for body text and not false evidence.
- Spectrum bodyp3/p5 machine-searched only for existing supplied short fragments; detailed DesK/DesR/des regulation/efficacy not adjudicated.
- Spectrum bodyp1 first/final sentences adopted for generic physical context only.
- Ramón all-HTMLp17 sentence index5 displayed during matching, including survival/freezing wording; only supplied phase-maintenance fragment and generic phase context adopted, no survival efficacy.
- Tolner second abstract sentence displayed wider transport/enzyme details; only explicit thermophile context and supplied phrase adopted.
- Complete canonical abstract displayed; culture, salt/pH/chemistry and comparative genomic details incidental, not adopted beyond named type strain/aliases and existing growth interval.
- Four metadata status observations and body/browser surfaces are exact historical reuse; null notices do not establish exhaustive current absence.
- Retained publisher tool export is not rawHTML; underlying cache fetch time unknown.
- Initial canonical-metadata.json contains DNS error bytes; only canonical-metadata-network-retry.json is successful primary metadata.
- Exact mesophilic alias biological equivalence and exact-bin calibration unknown; generic physical context does not choose bin semantics.
- Detailed temperature response, regulatory mechanisms, survival/fitness/defense, cultivation and optimization efficacy UNASSESSED_SCOPE.
- Phosphorylated-state/material-bearer and rigidification/property wording qualified, not forced into extra findings.
- Generic numeric existential does not settle interval-versus-width; exact alias equivalence unresolved.
- 25 prior whole readings plus1fresh whole history and26 current projections; no claim all26 readwhole currently.
- Ground auditor did not rerun common/native/DB checks; root owns independent native checks.
- Uncaptured discovery stays matching-line context; private/remote human acceptance unknown.
- Root adopted Spectrum zero-based bodyp1 first/final generic physical sentences and Ramón all-HTMLp17 first four physical sentences. Detailed regulation, survival, fitness, cultivation optimization and intervention efficacy remain unassessed even where snippets are literal.
- Canonical and taxonomy initial DNS failures and successful retries retain separate times/bytes; taxonomy establishes identity, not phenotype.
- Current writer outcomes are static inferences from read guards and exact data comparison; no writer or full PR664 dry run was executed.
- Original B14 common diagnostics are qualified for unchanged B15 inputs, not fresh B15 executions. Current target inspect, target validation, strict validation and snippet check are fresh. The serializer common guard separately rechecks current inputs and five database pins.
- Full just test was not run; focused Stage2 tests and product skips retain their original scope. Software checks do not establish scientific correctness.
- Active exact METPO:1000452 and parent METPO:1000306 are positive. Historical Mesophilie retention is documented in active-review106/release-delta1274 and finalizer; biological exact-alias equivalence to unresolved quantity remains unknown.
- Homeoviscous adaptation METPO:1016200 is local v85 proposal/mapping identity, absent from captured upstream raw OWL. Broad localv8 confers admits current process→trait roles; quantity/efficacy separate.
- Biolink causes and associated_with have broad NamedThing roles, not imported RO regulation constraints. Endpoint compatibility alone does not prove association statistics or detailed biology.
- Des_gene explicitly describes a desaturase protein despite its identifier. DesK conformation and phosphorylated DesR are qualified molecular-state readings; rigidity/thickness has a coherent property reading and explicit corrective history. No additional forced type finding.
- Canonical source and official taxonomy support B.nakamurai NRRL B-41091T (=CCUG68786T), existing17–50 interval and derived width33. No additional cultivation condition or optimum is adopted.
- Three components,13 nodes/10 edges, two REVIEWED_LABEL_ONLY proteins and zero instances are permissible NONMECHANISTIC context. Corrective history intentionally retains three components; no invented connector/accession/dataset.
- The retained20-organism/28-dataset catalog has B.subtilis species-level coverage for the adopted title context, without strain/module/efficacy inference. No exact B.nakamurai canonical entry was found in that catalog. Bounded current adapter discovery found no maintained runner; no module query was executed.
- Publication is separate from this local review. No scientific record, mapping, ontology, history, generated product or paid-provider run changed.
- Qualified reuse of four original B14 diagnostics is recorded in /private/tmp/traitmech-record-sweep-015.67f2ce7a/common-diagnostic-reuse-qualification.json. Historical products failures/retry and original cache provenance remain in /private/tmp/traitmech-record-sweep-014.q8m4v2cs/new-base-diagnostic-independent-review-agent/fresh-products-completion.json. B14 generated reports are retained output snapshots, not B15 source inputs or synthetic B15 reports. B15-to-B14 byte equality does not change the historical false B14-to-B13 comparison; B14 final gates/commit and continuation pins remain separate.
- Exact findings, actions, fields, severities and owners come only from root FINAL. Four explicit quantity anchors form one major; the separate five-edge imported-role group and two bounded minors are retained without extra type or connectivity findings.
- Serializer preparation adopts frozen audits and root adjudication without another whole-paper or whole-history review. Eight historical source access clocks, current canonical/taxonomy failure and retry clocks, root authority-query clocks and subsequent copying/reading remain distinct. Ground-auditor non-repetition is actor-specific; the common guard separately rechecks qualified current inputs and database pins. Original B14 diagnostics are not relabeled fresh B15 executions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T043653Z-temperature-range-mid3
kind: record
repository: CultureBotAI/TraitMech
title: Whole-record review of temperature range mid3
started_at: '2026-10-22T04:24:10.002008Z'
finished_at: '2026-10-22T04:36:53Z'
reviewer:
  identity: codex
  kind: agent
  independence: independent
  independence_basis: Separate source and grounding audits plus root selected primary
    reading and final adjudication supply the scientific judgments. Serializer preparation
    does not claim an additional whole-paper scientific review.
  model: GPT-6 (Codex)
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'Whole-record review identifies two major issues: ambient-temperature interval
  versus interval-width semantics and incompatible imported roles at five edges. Two
  bounded minors concern exact-bin attribution and a retrievable human-acceptance
  link. Active identity, canonical reported17–50 °C interval with derived width33,
  eleven literal snippets and selected formal facets are positive. Detailed microbial
  efficacy remains unassessed.'
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
  - path: data/traits/environment/temperature_range.yaml
    sha256: e3f8f082de570a8fc3de3ef6a1fdf95a60bdf28a6e2f6dcc43d3558df0775818
    role: context
  - path: data/traits/environment/temperature_range_mid3.yaml
    sha256: b0cd559b2373e71d092e1645beef2a9ff17548a43f953fded0eeff3d848cb251
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
  - path: history/infrastructure/pr664-adversarial-review/2026-09-07T072500Z-codex-693abc.yaml
    sha256: 380e91dcba7a246605454aa4cc65cf7ab3f9236d8c95bb32748dc80fe648e6d9
    role: context
  - path: history/infrastructure/pr664-adversarial-review/2026-09-07T200500Z-codex-696abc.yaml
    sha256: edb954fc7a95d2a9e6e7e390221fdd99dd9ea8ab8364d846c67c4a5ca41bc896
    role: context
  - path: history/infrastructure/prioritize-graph-research/2026-08-18T073129Z-claude-code-6ffbb9.yaml
    sha256: a1c2c954475853822eec940a2c6ec5fafb357039cddb9211568661ba8b9c739b
    role: context
  - path: history/infrastructure/prioritize-graph-research/2026-08-20T072722Z-claude-code-5774c9.yaml
    sha256: f342f08a52f61fa1fe7350ee9aaba6f265760a90b959e98e979b3811135fbd3f
    role: context
  - path: history/infrastructure/process-quality-consistency/2026-08-21T073211Z-codex-174227.yaml
    sha256: e35d99e8285d488d98584d046aa001825527609cfd62575b3b839c4a31230642
    role: context
  - path: history/infrastructure/trait-priority/2026-08-19T203529Z-claude-code-fbfb40.yaml
    sha256: 5337f34a01bb7f39da1e604544e839a3e42d558069ff2cf52706fb5b05286766
    role: context
  - path: history/records/homeoviscous_adaptation/2026-09-15T070756Z-codex-24f768.yaml
    sha256: e813ec0f62859a2d04d6964a082ac78eea8966e44b8224a3fe49eff8552bd778
    role: context
  - path: history/records/homeoviscous_adaptation/2026-09-15T071638Z-codex-eab563.yaml
    sha256: a0aaa509360e1b845bc09a6a0c598a4e9f1a1b31c63be1907dda97293cf605cd
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
  - path: history/records/temperature_range_mid2/2026-09-15T070801Z-codex-bd686f.yaml
    sha256: 6379be2191db95549d4360d993f972d804905379ccfe87eeee35d76cbfee8672
    role: context
  - path: history/records/temperature_range_mid3/2026-09-04T040000Z-codex-b4cccd.yaml
    sha256: f9d3bcf029e4ef2cf18d27dd0476e931955f2d428351687a5cad2a84c9a49d95
    role: context
  - path: history/records/temperature_range_mid3/2026-09-04T220000Z-codex-183.yaml
    sha256: e223727244f0ec4f0659e149783d5d2f54ce15f38cce2434c063383b400f1a29
    role: context
  - path: history/records/temperature_range_mid3/2026-09-08T033000Z-codex-92877e.yaml
    sha256: 8136f81a463bfd470c6b851e033de476b70014bc1f9c8330413cc30f54e018e4
    role: context
  - path: history/records/temperature_range_mid3/2026-09-15T070801Z-codex-03a328.yaml
    sha256: 81ae8149bb4c24cfda890a009aaa349fe7fc199f8bee6d1eddc6c5fa2b76358f
    role: context
  - path: history/records/temperature_range_mid4/2026-09-04T042000Z-codex-dc46b8.yaml
    sha256: f8bec40942e0e582c4a9afb3fbf6b5bc6baecfc1c56397815ef868df13797bfd
    role: context
  - path: history/records/temperature_range_mid4/2026-09-04T230000Z-codex-183.yaml
    sha256: 06e8a85e8f9e79e4a9fcfc987d8ac1be8512c954dccfa252a05cc94411470df5
    role: context
  - path: history/records/temperature_range_mid4/2026-09-06T133000Z-codex-51e9d3.yaml
    sha256: e1f27934d4616612490374eb314c22b9b047fa305f2a37735af91809d243361b
    role: context
  - path: history/records/temperature_range_mid4/2026-09-08T033000Z-codex-8e41e3.yaml
    sha256: 843c1f43287234961002be15bccf161e3b07bdbf2f59a9e75c01b196f9a491e4
    role: context
  - path: history/records/temperature_range_mid4/2026-09-15T070802Z-codex-c3d317.yaml
    sha256: 631748fbe499f406bd5fa7bbbf49698a78e7a0a929497e1d12ca9e159230b88c
    role: context
  - path: history/records/temperature_range_very_low/2026-09-04T044000Z-codex-3e9ace.yaml
    sha256: 10fc3e20f788b20d9bc52b9abb3ef21c1e3697ee3baf04ae0d344498b1172f4c
    role: context
  - path: history/records/temperature_range_very_low/2026-09-04T232000Z-codex-183.yaml
    sha256: 997c1186d90e27c098a5e4a3912edb0ec1b7d65a4f90f1ebf21a6bfbbc160954
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
  - path: reports/metpo_2026_06_12_active_review.tsv
    sha256: 45e9c6471475635ba1f2602cd636a119d490f5dbd8dd6ac8af1aab89a321379f
    role: context
  - path: reports/metpo_2026_06_12_release_delta.tsv
    sha256: afe858d2aa0ade08322c7808d5917ff370e069ba02c2642d483342db8e9323ac
    role: context
  - path: reports/ontology_snapshot_manifest.tsv
    sha256: 4a157279a8c4e3fc2afb5382a45c31961991bbd1f330f26d0061b0cfd0b4d213
    role: context
  - path: research/traits/environment/temperature_range_mid3-deep-research-falcon.md
    sha256: 3f963b9266f18d49c219ddc5fca0dbfe9970c724d3c3cadb6c15dbc62202fcd3
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
  - path: scripts/audit_schema.py
    sha256: ea8eb5b6f5355a87f6270ec67793e0a05811b14a67828543dad90f2465c5ddb1
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
  - path: scripts/trait_priority.py
    sha256: 96909390f0f55a76fe7161420813f072774a483797c29f96589be379c07892fb
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
- target_id: METPO:1000452
  path: data/traits/environment/temperature_range_mid3.yaml
  label: temperature range mid3
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_range_mid3.yaml
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
  selection: Third record in the actual B15 queue; current 362-line target and 103
    captured inputs. Local review is independent of remote publication.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - METPO:1000452
checks:
- check_id: new-base-qc
  name: Reused B14 corpus QC
  status: passed
  required: true
  target_ids:
  - METPO:1000452
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
  - common-reuse-qualification
  - original-b14-common-completion
  scope_note: Reused original B14 execution at base 508ee3089c93a36413969cd1ede7f9528a1940a4,
    qualified for unchanged B15 inputs. Exact original times/commands/logs retained;
    QC children share the aggregate interval, without invented child times. Current
    B15 source maps/input bytes and five databases rechecked. No fresh B15 execution
    or B14 final QC/commit claimed.
- check_id: new-base-history
  name: Reused B14 history integrity
  status: passed
  required: true
  target_ids:
  - METPO:1000452
  command: just validate-history
  exit_code: 0
  expected_exit_code: 0
  summary: 1278 HistoryRecord YAMLs validated, 0 invalid; current history snapshot
    contains 1279 files. Integrity does not establish scientific correctness or human
    acceptance.
  evidence_ids:
  - check-new-base-history
  - common-reuse-qualification
  - original-b14-common-completion
  scope_note: Reused original B14 execution at base 508ee3089c93a36413969cd1ede7f9528a1940a4,
    qualified for unchanged B15 inputs. Exact original times/commands/logs retained;
    QC children share the aggregate interval, without invented child times. Current
    B15 source maps/input bytes and five databases rechecked. No fresh B15 execution
    or B14 final QC/commit claimed.
- check_id: new-base-products
  name: Reused B14 mapping identifier/label validation
  status: passed
  required: true
  target_ids:
  - METPO:1000452
  command: env PYSTOW_HOME=/private/tmp/traitmech-record-sweep.FU79Gr/pystow OAKLIB_HOME=/private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib
    SQLITE_TMPDIR=/private/tmp/traitmech-record-sweep.FU79Gr/sqlite-tmp just validate-products
  exit_code: 0
  expected_exit_code: 0
  summary: 361 canonical matches, 2 exact-synonym matches, 1 exception and 123 SKIPPED_NO_ADAPTER
    pairs. Configured scope is the two grounding mappings, not every target identifier
    or scientific claim.
  evidence_ids:
  - check-new-base-products
  - common-reuse-qualification
  - original-b14-common-completion
  scope_note: Reused original B14 execution at base 508ee3089c93a36413969cd1ede7f9528a1940a4,
    qualified for unchanged B15 inputs. Exact original times/commands/logs retained;
    QC children share the aggregate interval, without invented child times. Current
    B15 source maps/input bytes and five databases rechecked. No fresh B15 execution
    or B14 final QC/commit claimed.
- check_id: new-base-stage2-tests
  name: Reused B14 focused Stage2 writer tests
  status: passed
  required: false
  target_ids:
  - METPO:1000452
  command: uv run pytest tests/test_curate_stage2_causal_graphs.py -q
  exit_code: 0
  expected_exit_code: 0
  summary: Five tests passed in the explicitly selected Stage2 test file. This is
    not a full just test run or biological validation.
  evidence_ids:
  - check-new-base-stage2-tests
  - common-reuse-qualification
  - original-b14-common-completion
  scope_note: Reused original B14 execution at base 508ee3089c93a36413969cd1ede7f9528a1940a4,
    qualified for unchanged B15 inputs. Exact original times/commands/logs retained;
    QC children share the aggregate interval, without invented child times. Current
    B15 source maps/input bytes and five databases rechecked. No fresh B15 execution
    or B14 final QC/commit claimed.
- check_id: temperature-range-mid3-target-validate
  name: Focused native validation
  status: passed
  required: true
  target_ids:
  - METPO:1000452
  command: just validate data/traits/environment/temperature_range_mid3.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Native record validation passed; scientific interpretation is assessed
    separately.
  evidence_ids:
  - check-temperature-range-mid3-target-validate
- check_id: temperature-range-mid3-target-strict
  name: Focused strict validation
  status: passed
  required: true
  target_ids:
  - METPO:1000452
  command: just validate-strict data/traits/environment/temperature_range_mid3.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: The actual validate-strict command passed.
  evidence_ids:
  - check-temperature-range-mid3-target-strict
- check_id: temperature-range-mid3-snippets-network
  name: Focused network snippet check
  status: passed
  required: true
  target_ids:
  - METPO:1000452
  command: just verify-snippets --record data/traits/environment/temperature_range_mid3.yaml
    --out /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-snippets.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 'Native command succeeded for eleven snippets: three VERIFIED and eight
    NOT_IN_ABSTRACT, the latter inconclusive for body text. Separate manual matching
    supports all eleven literal spans; no false-quotation or adjacent exact-bin inference.'
  evidence_ids:
  - check-temperature-range-mid3-snippets-network
- check_id: native-inspect
  name: One-target native review capture
  status: passed
  required: true
  target_ids:
  - METPO:1000452
  command: uv run python scripts/record_review.py inspect --targets /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3.targets.json
    --input .claude/skills/curate-yaml-record/references/review-checklist.md --input
    .claude/skills/manage-identifiers/SKILL.md --input .claude/skills/review-yaml-record/SKILL.md
    --input CLAUDE.md --input DO_NOT_WORK.md --input conf/evidence_snippet_baseline.tsv
    --input conf/record_review.yaml --input data/raw/biolink-model.yaml --input data/raw/metpo.owl
    --input data/traits/environment/temperature_range.yaml --input docs/CURATION_PLAYBOOK.md
    --input docs/GROUNDING_POLICY.md --input docs/PATHWAY_LINKS.md --input docs/record-review-profile.md
    --input docs/record-reviews.md --input history/infrastructure/canonical-examples/2026-08-19T183734Z-claude-code-44a170.yaml
    --input history/infrastructure/pr664-adversarial-review/2026-09-07T010000Z-codex-60bca2.yaml
    --input history/infrastructure/pr664-adversarial-review/2026-09-07T072500Z-codex-693abc.yaml
    --input history/infrastructure/pr664-adversarial-review/2026-09-07T200500Z-codex-696abc.yaml
    --input history/infrastructure/prioritize-graph-research/2026-08-18T073129Z-claude-code-6ffbb9.yaml
    --input history/infrastructure/prioritize-graph-research/2026-08-20T072722Z-claude-code-5774c9.yaml
    --input history/infrastructure/process-quality-consistency/2026-08-21T073211Z-codex-174227.yaml
    --input history/infrastructure/trait-priority/2026-08-19T203529Z-claude-code-fbfb40.yaml
    --input history/records/homeoviscous_adaptation/2026-09-15T070756Z-codex-24f768.yaml
    --input history/records/homeoviscous_adaptation/2026-09-15T071638Z-codex-eab563.yaml
    --input history/records/homeoviscous_adaptation/2026-09-15T072704Z-codex-6cb554.yaml
    --input history/records/mesophilic/2026-09-04T004000Z-codex-14a39b.yaml --input
    history/records/mesophilic/2026-09-04T130000Z-codex-183.yaml --input history/records/mesophilic/2026-09-06T133000Z-codex-133a5b.yaml
    --input history/records/temperature_range_mid2/2026-09-15T070801Z-codex-bd686f.yaml
    --input history/records/temperature_range_mid3/2026-09-04T040000Z-codex-b4cccd.yaml
    --input history/records/temperature_range_mid3/2026-09-04T220000Z-codex-183.yaml
    --input history/records/temperature_range_mid3/2026-09-08T033000Z-codex-92877e.yaml
    --input history/records/temperature_range_mid3/2026-09-15T070801Z-codex-03a328.yaml
    --input history/records/temperature_range_mid4/2026-09-04T042000Z-codex-dc46b8.yaml
    --input history/records/temperature_range_mid4/2026-09-04T230000Z-codex-183.yaml
    --input history/records/temperature_range_mid4/2026-09-06T133000Z-codex-51e9d3.yaml
    --input history/records/temperature_range_mid4/2026-09-08T033000Z-codex-8e41e3.yaml
    --input history/records/temperature_range_mid4/2026-09-15T070802Z-codex-c3d317.yaml
    --input history/records/temperature_range_very_low/2026-09-04T044000Z-codex-3e9ace.yaml
    --input history/records/temperature_range_very_low/2026-09-04T232000Z-codex-183.yaml
    --input justfile --input mappings/node_grounding.tsv --input mappings/predicate_grounding.tsv
    --input mappings/trait_exact_match_review.tsv --input mappings/uniprot_regrounding_candidates.tsv
    --input proposals/metpo_traitmech_v8/metpo_proposal_properties_robot.tsv --input
    proposals/metpo_traitmech_v8/proposal.md --input proposals/metpo_traitmech_v85/metpo_proposal_classes_robot.tsv
    --input proposals/metpo_traitmech_v85/proposal.md --input reports/metpo_2026_06_12_active_review.tsv
    --input reports/metpo_2026_06_12_release_delta.tsv --input reports/ontology_snapshot_manifest.tsv
    --input research/traits/environment/temperature_range_mid3-deep-research-falcon.md
    --input schema/record_review.yaml --input scripts/add_homeoviscous_adaptation_trait.py
    --input scripts/audit_causal_graphs.py --input scripts/audit_graph_protein_taxa.py
    --input scripts/audit_predicate_domains.py --input scripts/audit_schema.py --input
    scripts/audit_unapplied_groundings.py --input scripts/audit_uniprot_grounding.py
    --input scripts/backfill_canonical_examples_444.py --input scripts/connect_mesophilic_graph_183.py
    --input scripts/connect_temperature_delta_high_graph_183.py --input scripts/connect_temperature_delta_very_low_graph_183.py
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
    --input scripts/review_temperature_delta_high_graph_183.py --input scripts/review_temperature_delta_very_low_graph_183.py
    --input scripts/review_temperature_optimum_very_low_graph_183.py --input scripts/review_temperature_range_mid3_graph_183.py
    --input scripts/review_temperature_range_mid4_graph_183.py --input scripts/review_temperature_range_very_low_graph_183.py
    --input scripts/seed_from_metpo.py --input scripts/trait_priority.py --input scripts/verify_metpo_proposal.py
    --input src/traitmech/schema/mech_shared.yaml --input src/traitmech/schema/traitmech.yaml
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
  - METPO:1000452
  summary: Two contextual protein classes are REVIEWED_LABEL_ONLY with explicit rationales
    and zero instances; no token accession required.
  evidence_ids:
  - record
  - policy
  - expression
- check_id: expression-adapter-availability
  name: Structured source-organism expression query availability
  status: unavailable
  required: false
  target_ids:
  - METPO:1000452
  summary: Bounded maintained-runner discovery found no available adapter. Retained
    catalog and selected source identities provide no strain/module or efficacy result.
  evidence_ids:
  - expression
  - expression-discovery
  - catalog-original
  - source-reading
evidence:
- evidence_id: common-reuse-qualification
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/common-diagnostic-reuse-qualification.json
  locator: Current B15 source maps, maintained inputs and five cache databases qualified
    against identified B14 diagnostics
  accessed_at: '2026-10-22T00:22:12.767304Z'
  support: context_only
  summary: Reuse qualification only; original B14 times retained, no B15 diagnostic
    execution or B14 finalization asserted.
  snapshot_sha256: 669d35950e6eb98d05d2d33ee1312b10981840ba66f9ddd5031e3b7cdf8d49dc
- evidence_id: original-b14-common-completion
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/new-base-diagnostic-independent-review-agent/fresh-products-completion.json
  locator: Original B14 products completion and diagnostic evidence
  accessed_at: '2026-10-21T23:30:28.240498Z'
  support: context_only
  summary: Original four B14 diagnostics, historical attempts and original cache provenance;
    B14-to-B13 comparison remains false.
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
- evidence_id: check-temperature-range-mid3-target-validate
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-target-validate.log
  locator: Executed 2026-10-22T04:24:46.825109+00:00 through 2026-10-22T04:24:47.779367+00:00;
    metadata temperature-range-mid3-target-validate.json
  accessed_at: '2026-10-22T04:24:47.779367Z'
  support: context_only
  summary: Native record validation passed; scientific interpretation is assessed
    separately.
  snapshot_sha256: c9e84a860d6035e28ab4cd304604508602c5f3e476a1c5b41dba6475779dd3f0
- evidence_id: check-temperature-range-mid3-target-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-target-strict.log
  locator: Executed 2026-10-22T04:24:46.825108+00:00 through 2026-10-22T04:24:48.371122+00:00;
    metadata temperature-range-mid3-target-strict.json
  accessed_at: '2026-10-22T04:24:48.371122Z'
  support: context_only
  summary: The actual validate-strict command passed.
  snapshot_sha256: 4b9b8cde08114093b0fe49efe9b9bb76892d9a453e0f0e0e3d5fbf588402be4c
- evidence_id: check-temperature-range-mid3-snippets-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-snippets-network.log
  locator: Executed 2026-10-22T04:25:04.430475+00:00 through 2026-10-22T04:25:11.700686+00:00;
    metadata temperature-range-mid3-snippets-network.json
  accessed_at: '2026-10-22T04:25:11.700686Z'
  support: context_only
  summary: 'Native command succeeded for eleven snippets: three VERIFIED and eight
    NOT_IN_ABSTRACT, the latter inconclusive for body text. Separate manual matching
    supports all eleven literal spans; no false-quotation or adjacent exact-bin inference.'
  snapshot_sha256: c6e1c41d717ab8186950972080a60f99d38481dfb920c2da5af8c906b61ab12f
- evidence_id: capture
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3.inspect.json
  locator: Actual successful native inspect with 103 captured inputs
  accessed_at: '2026-10-22T04:24:10.850708Z'
  support: context_only
  summary: All current captured source hashes and the exact target are bound before
    serialization.
  snapshot_sha256: 9bb9fa9a8af64a909b17120ecbf183c07f9427a2f1c6187c7f0a08ab1d93a923
- evidence_id: record
  kind: record_content
  reference: data/traits/environment/temperature_range_mid3.yaml
  locator: Whole current record
  accessed_at: '2026-10-22T04:24:10.850708Z'
  support: supports
  summary: Thirteen nodes, ten edges, nineteen embedded events, one canonical example,
    two reviewed label-only protein classes and zero instances.
  snapshot_sha256: b0cd559b2373e71d092e1645beef2a9ff17548a43f953fded0eeff3d848cb251
- evidence_id: local-init
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/batch015-local-initialization-receipt.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T03:50:31.750633Z'
  support: context_only
  summary: Actual local initialization and third queue target; publication remains
    separate.
  snapshot_sha256: b5fc6d47e2719f9da11bad0719b933f4af76d4ccc30226c15a2a7c51c07e2283
- evidence_id: policy
  kind: authority
  reference: docs/GROUNDING_POLICY.md
  locator: Captured maintained authority
  accessed_at: '2026-10-22T04:27:50.709314Z'
  support: supports
  summary: Protein family/function grounding, reviewed label-only aggregates and optional
    instances.
  snapshot_sha256: 891678c983c2283a47c81c47950b35753981e9339d105f3bbdda92a1f5ab7f42
- evidence_id: playbook
  kind: authority
  reference: docs/CURATION_PLAYBOOK.md
  locator: Captured maintained authority
  accessed_at: '2026-10-22T04:27:50.709314Z'
  support: supports
  summary: Source attribution and attributable acceptance.
  snapshot_sha256: 735e9b810471da9f7d8364e35ffe1e741edb3421480dac01727db6ea5aa65da9
- evidence_id: schema
  kind: authority
  reference: src/traitmech/schema/traitmech.yaml
  locator: Captured maintained authority
  accessed_at: '2026-10-22T04:27:50.709314Z'
  support: supports
  summary: Current material, molecular-activity, process, quality and quantitative
    NONMECHANISTIC facets.
  snapshot_sha256: 46c47fc627b80ccbba1e8ab3fb6f2aee93bc2aef7aaf72fe9aadc3257f2c02dd
- evidence_id: predicate-mapping
  kind: authority
  reference: mappings/predicate_grounding.tsv
  locator: Captured maintained authority
  accessed_at: '2026-10-22T04:27:50.709314Z'
  support: supports
  summary: Wildcard contributes-to row 10, regulates row 11 and positively-regulates
    row 99 can recreate incompatible imported roles in future empty fields; the generic
    consumer skips populated IDs.
  snapshot_sha256: 8e28c19e93aca3dc164a3befbe2612b289241de457c59f499e65936c03b7ce52
- evidence_id: canonical-writer
  kind: authority
  reference: scripts/backfill_canonical_examples_444.py
  locator: Captured maintained authority
  accessed_at: '2026-10-22T04:27:50.709314Z'
  support: supports
  summary: Exact Bacillus nakamurai SOURCES/TRANCHE payload and equality, rejection
    and global queue guards; positive interval and width with coordinated quantity
    interpretation.
  snapshot_sha256: 18ca0766789c239d693ef665e8b1d43c1209a0f414a326f1c5d890f88de7b20c
- evidence_id: identity
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-grounding-agent/identity-and-hierarchy.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:27:50.705221Z'
  support: context_only
  summary: Active target and parent; historical Mesophilie retention and unresolved
    broad qualitative equivalence. Generic numeric existential does not decide endpoints
    versus width.
  snapshot_sha256: 3ac29c0f3debe38785d80bc35abcef2f9a4df1d4d8dc73e3235c4678e00a65d7
- evidence_id: nodes-edges
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-grounding-agent/node-edge-grounding-ledger.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:27:50.704936Z'
  support: context_only
  summary: All thirteen current node referents and ten formal relation dispositions.
  snapshot_sha256: 9b23460bf4e72d34c1d42a8a2778dc57ef254485baeb7fe295690016323e66ff
- evidence_id: owners
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-grounding-agent/ownership-assessment.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:27:50.708569Z'
  support: context_only
  summary: Exact canonical, review/connector/PR664 and conditional mapping ownership,
    with distinct current replay guards.
  snapshot_sha256: f784bd8e4cd95fc5a38ae6ba913ff1869aa1743806004c3e49b4f66d48bd4ab4
- evidence_id: owner-primary
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-grounding-agent/owner-primary-reading.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:27:50.701523Z'
  support: context_only
  summary: Selected current owner windows and exact replay guards without writer execution.
  snapshot_sha256: 7f9032efcb718a6de4fcff7088924af9219e7dafdb9383845d5e7acfe0ffbf33
- evidence_id: local-authority
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-grounding-agent/local-authority-reading.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:27:50.704171Z'
  support: context_only
  summary: Actual schema, policy, local proposals and mapping reading scope.
  snapshot_sha256: 05fd1ff42aeb7a130f56c2a769950722d80bcf3d659bca862a3e5f85060a7f76
- evidence_id: histories
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-grounding-agent/history-reading-provenance.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:27:50.697750Z'
  support: context_only
  summary: 'Twenty-six current actor/event projections: 25 exact qualified prior whole
    readings and one fresh whole infrastructure-history reading.'
  snapshot_sha256: 514213a690408f026d21ba5ae20941f475809865c731484e6cf5d6632e7221d7
- evidence_id: embedded-history
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-grounding-agent/embedded-history-ledger.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:27:50.698235Z'
  support: context_only
  summary: 'Nineteen embedded events: eighteen AI-assisted events and one seed.'
  snapshot_sha256: e6222ec4cdbb07f3d1a1e8b3bc5c1aab6a9e98e80f5110bd4e0af256606eb451
- evidence_id: human-search
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-grounding-agent/search-and-provenance.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:24:55.318915Z'
  support: context_only
  summary: 'Ignored- and hidden-inclusive local search: 191 matching paths, 69 matching
    arrays and 94 all-local review arrays, zero exact target.'
  snapshot_sha256: 0be69c4324b1bc3fba05acbe5f9c651de424a4c685b03be63985cf559d73f102
- evidence_id: discovery
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-grounding-agent/discovery-dispositions.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:27:50.708423Z'
  support: context_only
  summary: Uncaptured leads remain matching-line context; private or remote acceptance
    unknown.
  snapshot_sha256: 5052a73e36d0f66b48d672b2617fa4b92cdf7bcde5d977ad10fe7c9b28a0a5b8
- evidence_id: expression
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-grounding-agent/expression-and-readiness.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:27:50.709164Z'
  support: context_only
  summary: Three intentionally retained NONMECHANISTIC components and two reviewed
    label-only protein classes are allowed; B. subtilis title context has species
    coverage only, with no canonical key or module result.
  snapshot_sha256: 1e9d4449e2c5604a21f965c4fa839dc2d5448f1f21355d659fbd445cfd8607d4
- evidence_id: expression-discovery
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-grounding-agent/adapter-discovery.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:24:55.488579Z'
  support: context_only
  summary: Bounded maintained-runner discovery found no available adapter; no query
    executed.
  snapshot_sha256: 65ab9386532aa848c29ab262dc4d165e425f247c86b637e9ad5219e9e5edc41e
- evidence_id: catalog-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-grounding-agent/catalog-reuse.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:27:50.709094Z'
  support: context_only
  summary: Original catalog acquisition preserved separately from current copying
    and selected-name reading.
  snapshot_sha256: 2c58874b21e3f6fb92e035fb847c1a0fc7a818942f07a946ceeeb75d77f1b968
- evidence_id: ground-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-grounding-agent/reading-scope-receipt.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:27:50.709463Z'
  support: context_only
  summary: Exact current reading scopes, qualified prior histories and owner qualifications.
  snapshot_sha256: 3e08d09decdc52bfa57b2d8049d339bb382d8a109eaa9826cc1b61ef86552607
- evidence_id: ground-assessment
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-grounding-agent/grounding-assessment.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:27:50.709314Z'
  support: context_only
  summary: Two ground majors include the shared quantity finding counted once; bounded
    human minor.
  snapshot_sha256: 9d89aa9c97d049cb84876c29f46b477e48e9a40e7aaa978a9ee8d76c77327bf1
- evidence_id: ground-manifest
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-grounding-agent/evidence-manifest.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:27:52.135557Z'
  support: context_only
  summary: All 27 immutable ground artifacts verified.
  snapshot_sha256: 7edbae513397332c6ec86b7c05ade7b0b5a07eea129da70500bb5eef3745d3d7
- evidence_id: ontology-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-source-root/selected-ontology-primary.json
  locator: Exact selected response; query 2026-10-22T04:25:22.418934+00:00 through
    2026-10-22T04:25:22.424008+00:00
  accessed_at: '2026-10-22T04:25:22.424008Z'
  support: supports
  summary: Current RO/BFO, raw METPO, local v8/v85 and Biolink selected authority.
    Copy/read time is not query time. Ground auditor did not repeat queries or database
    hashing; the serializer common guard separately verifies qualified inputs.
  snapshot_sha256: 171c34deb4c0076b9203efdb8fb5515192de42eb3067a3200b904c58a81c12e7
- evidence_id: authority-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-source-root/selected-authority-primary.json
  locator: Exact selected response; query 2026-10-22T04:25:22.424722+00:00 through
    2026-10-22T04:25:22.718499+00:00
  accessed_at: '2026-10-22T04:25:22.718499Z'
  support: supports
  summary: Current RO/BFO, raw METPO, local v8/v85 and Biolink selected authority.
    Copy/read time is not query time. Ground auditor did not repeat queries or database
    hashing; the serializer common guard separately verifies qualified inputs.
  snapshot_sha256: 830d209d0a8c72db274fdce1c918f46a40337311578b4bf6624864fddcfb81db
- evidence_id: authority-provenance
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-grounding-agent/primary-reuse-provenance.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:27:50.691359Z'
  support: context_only
  summary: Actual current root query clocks and exact ground-auditor copies; separate
    reading completion.
  snapshot_sha256: edffdd4a5a7492f204bcbabd67c47bb26dab121801095631796944233ed986d6
- evidence_id: catalog-original
  kind: authority
  reference: https://imodulondb.org/api/datasets
  locator: Original retained 20-organism/28-dataset catalog
  accessed_at: '2026-10-21T07:36:12.858149Z'
  support: context_only
  summary: No exact Bacillus nakamurai canonical key in this retained catalog. B.
    subtilis title context has species-level coverage only; no strain/module, phenotype
    or efficacy inference.
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: mendoza-metadata
  kind: primary_source
  reference: DOI:10.1146/annurev-micro-091313-103612
  locator: Indexed identity and first abstract sentence
  accessed_at: '2026-10-21T10:00:02.042457Z'
  support: supports
  summary: Supplied generic physical fragment is literal; nearest inspected wording
    does not establish exact 30–34-bin calibration.
  snapshot_sha256: 801da630644a181211f991a6f21c49b178e42a65f615c4eebd8196bc29244588
- evidence_id: mendoza-publisher
  kind: primary_source
  reference: DOI:10.1146/annurev-micro-091313-103612
  locator: Retained publisher browser-tool export; historical call interval, not raw
    HTML
  accessed_at: '2026-10-21T23:38:35Z'
  support: supports
  summary: Selected abstract wording retained. Underlying cache fetch time is unknown;
    no current fresh publisher acquisition is claimed.
  snapshot_sha256: b8635235ad5e362d0b33ef4834f84eb25fe7ff6b1bd1321affb2b61cecbc66fc
- evidence_id: cold-metadata
  kind: primary_source
  reference: DOI:10.1007/s42770-023-01057-4
  locator: Indexed identity and original notice fields
  accessed_at: '2026-10-21T22:07:08.865512Z'
  support: supports
  summary: Identity verified; detailed stress-defense and survival efficacy remain
    unassessed.
  snapshot_sha256: da5cffab81fe0e039c6fcec8f318b2715f5604eaf8722ea6f63f944178ed447b
- evidence_id: cold-body
  kind: primary_source
  reference: DOI:10.1007/s42770-023-01057-4
  locator: Source-auditor zero-based all-HTML paragraph 17 supplied phase fragment;
    root first four physical sentences separately bounded
  accessed_at: '2026-10-21T22:07:50.938485Z'
  support: supports
  summary: Existing fragment literal and generic phase context positive. Surrounding
    survival/freezing wording and detailed adaptive efficacy remain unassessed; no
    new body acquisition.
  snapshot_sha256: bb09a59c07f43ff0af177f89b624c8b5d4841e513ed0d478120954a016342889
- evidence_id: tolner-metadata
  kind: primary_source
  reference: DOI:10.1016/s0300-9629(97)00003-0
  locator: Indexed identity and first two thermophile abstract sentences
  accessed_at: '2026-10-21T09:29:01.331044Z'
  support: supports
  summary: Supplied snippet is literal and explicitly concerns high-temperature thermophiles;
    adjacent exact-bin support is not established.
  snapshot_sha256: 56f69a7ce2e69822ef753fec5c43716583184e45fc1a2c0cae98aa9bdb841265
- evidence_id: tolner-crossref
  kind: primary_source
  reference: DOI:10.1016/s0300-9629(97)00003-0
  locator: Original Crossref identifier/title
  accessed_at: '2026-10-21T09:27:49.120434Z'
  support: supports
  summary: Source identity positive; no detailed transport or regulatory efficacy
    assessed.
  snapshot_sha256: 6f0a5c9b3558992f0f75d1861225410727bededc63928e7a72e1762170d34349
- evidence_id: spectrum-body
  kind: primary_source
  reference: DOI:10.1128/spectrum.03925-23
  locator: Zero-based body paragraph 1 first/final generic physical sentences; paragraphs
    3/5 machine matching of supplied short spans only
  accessed_at: '2026-10-21T22:07:32.905772Z'
  support: supports
  summary: Current supplied snippets occur literally. Detailed DesK/DesR/des regulation,
    sensing efficacy, survival/fitness and intervention effects are UNASSESSED_SCOPE;
    exact-bin sufficiency is not established.
  snapshot_sha256: 4e57f358369566231e022520fc5b5adad7b8c182adfa282d9ed404fa3298a561
- evidence_id: spectrum-metadata
  kind: primary_source
  reference: DOI:10.1128/spectrum.03925-23
  locator: Indexed source identity, title and original notice fields
  accessed_at: '2026-10-21T22:07:08.906527Z'
  support: supports
  summary: B. subtilis title context only; no strain/module or detailed efficacy inference.
  snapshot_sha256: 745eedfa2c11814739b07a4d944725bf565eb4e3f9c6b207ba0d31b967563f98
- evidence_id: canonical-metadata
  kind: primary_source
  reference: DOI:10.1099/ijsem.0.001135
  locator: 'Successful retry primary abstract: existing growth sentence and named
    type-strain statement'
  accessed_at: '2026-10-22T04:25:13.413436Z'
  support: supports
  summary: Bacillus nakamurai NRRL B-41091T (=CCUG 68786T), reported 17–50 °C interval
    and explicitly derived width 33 are positive. Other cultivation, optimum, genomic
    or chemical details are not adopted.
  snapshot_sha256: 2f9dfdded745650d7abaf31e8ddf60d09d4d1b9bddc15d044c90750b7c1df06b
- evidence_id: canonical-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-source-agent/canonical-metadata-network-retry-access.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:25:13.413436Z'
  support: context_only
  summary: Current successful canonical metadata retry interval, separate from initial
    DNS failure and eight historical source copies.
  snapshot_sha256: 95c869225ff6cab126a4cdc49d2894d3178fae3753a108a4c1c46c30cc2e9838
- evidence_id: canonical-initial-failure
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1099%2Fijsem.0.001135&format=json&resultType=core
  locator: Initial DNS error bytes, not canonical metadata
  accessed_at: '2026-10-22T04:25:00.061322Z'
  support: context_only
  summary: Only the separate successful network-retry response supplies canonical
    evidence. This access failure is not native validation failure.
  snapshot_sha256: 35281279d8e2164cee8666d6f8aad891326911e887ab1b2ab778c8ac6d09dc6c
- evidence_id: taxonomy
  kind: authority
  reference: NCBITaxon:1793963
  locator: Fresh successful official species/type-material response
  accessed_at: '2026-10-22T04:25:24.409276Z'
  support: supports
  summary: Bacillus nakamurai species and NRRL B-41091/CCUG 68786 type-material identities
    positive; no quantitative phenotype inferred from taxonomy.
  snapshot_sha256: 5df829180b71be8f3e48cca4b2114d8d1b7b03758ff4e6ee74418b5dad1dcb9b
- evidence_id: taxonomy-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-grounding-agent/taxonomy-retry-access.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:25:24.409276Z'
  support: context_only
  summary: Actual successful retry interval and hash.
  snapshot_sha256: eb98c1dda56b07ba5c5007f807f236e189c022d7d6d5a22999bbc03a12b5e33f
- evidence_id: taxonomy-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-grounding-agent/taxonomy-identity.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:27:50.704656Z'
  support: context_only
  summary: Official identity, successful response and separate initial failed access.
  snapshot_sha256: d2e00ab9f84c1385805e43831d4a24362d1f3017405d8b0ffbea600ae6e215d9
- evidence_id: taxonomy-initial-failure
  kind: validation
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1793963&retmode=xml
  locator: Initial DNS error bytes, not taxonomy XML
  accessed_at: '2026-10-22T04:24:55.504467Z'
  support: context_only
  summary: Access failure is retained separately from successful retry and native
    validation.
  snapshot_sha256: 35281279d8e2164cee8666d6f8aad891326911e887ab1b2ab778c8ac6d09dc6c
- evidence_id: sources
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-source-agent/source-assessment.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:28:30.945692Z'
  support: context_only
  summary: Five works; shared quantity conflict and bounded nearest-span attribution
    concern, with detailed efficacy unassessed.
  snapshot_sha256: a8f917db87e7024915678675f53cbc54816c4b4bd906d1b32ef626a2a44ac3b6
- evidence_id: source-identities
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-source-agent/source-ledger.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:28:30.921868Z'
  support: context_only
  summary: All five identities and selected scopes; reused metadata notices retain
    original times, alongside the successful current canonical metadata retry.
  snapshot_sha256: 7a940945d384fb6d582416f68307c0a3904b41730a4aa9224cb7e3c79e8990f5
- evidence_id: source-status
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-source-agent/source-status-ledger.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:28:30.921868Z'
  support: context_only
  summary: Original-time notice observations, not an exhaustive fresh status search.
  snapshot_sha256: 7dca55b39e196b4cf17aac190a89785d5c12456d757143999f2fae108878b89b
- evidence_id: placements
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-source-agent/source-placement-ledger.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:28:30.921868Z'
  support: context_only
  summary: All thirteen external placements; thirteen grounding fields are separately
    covered by node-edge audits.
  snapshot_sha256: c822ef2b5253e04a8b1f60d7cd32a3bf98c0c5ed59234ccae6984c70c485e8b3
- evidence_id: snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-source-agent/snippet-ledger.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:28:30.921868Z'
  support: context_only
  summary: 'All eleven supplied snippets are literal: three in indexed abstracts and
    eight in retained body text. Detailed biological efficacy remains unassessed.'
  snapshot_sha256: 26a25b7eb6cfd1b63b8801d97ec344fa6ea40bb3c018a8e48d3d5c4970dd43c6
- evidence_id: notes
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-source-agent/source-note-ledger.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:28:30.921868Z'
  support: context_only
  summary: Twelve notes including the singular canonical note; exact-bin attribution
    distinct from literal text.
  snapshot_sha256: f0b571683877a125c8805ed76234998f6aa471287bd3d39c3586481bbc30cac3
- evidence_id: source-nodes-edges
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-source-agent/node-edge-source-ledger.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:28:30.921868Z'
  support: context_only
  summary: All thirteen nodes and ten edges with supported, partial, unknown and unassessed
    dispositions.
  snapshot_sha256: 4f59874c1fbffa0414254eb33d72bd822ad9f3d13a230498fd40e01993d93a58
- evidence_id: canonical
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-source-agent/canonical-assessment.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:28:30.921868Z'
  support: context_only
  summary: Named source interval and derived width positive, incompatible current
    quantity interpretations grouped once.
  snapshot_sha256: 7a85462b593f03993d034e0fb6486c7071bddfa145a2bdcddb5b20fec4252979
- evidence_id: source-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-source-agent/primary-reading-scope.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:28:30.943842Z'
  support: context_only
  summary: Selected identity, physical/classification text and literal spans; no whole-paper
    or detailed efficacy review.
  snapshot_sha256: 70d11d346f7fb2b9bdfcd05cbdbcc622f471f1914ce69f19666ca2ea17262c8e
- evidence_id: source-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-source-agent/source-access-limits.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:28:30.921868Z'
  support: context_only
  summary: Eight retained primary surfaces and one current successful canonical metadata
    retry after DNS failure; no current body acquisition.
  snapshot_sha256: de70b33c0f96695b2054cfae51742d56ef085f4d2997eea588548a64ffdec363
- evidence_id: source-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-source-agent/source-reuse-receipt.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:24:59.908804Z'
  support: context_only
  summary: Eight exact copies with flat original-access clocks and prior-receipt hashes;
    current canonical failure/retry are separate.
  snapshot_sha256: f4e979d91ef5331aaebfa150d418ed06025a018a0a1e8e1345b9028e3485af2f
- evidence_id: source-native
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-source-agent/native-context.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:28:30.945523Z'
  support: context_only
  summary: Native three VERIFIED/eight NOT_IN_ABSTRACT inconclusive results, separate
    from manual eleven literal matches.
  snapshot_sha256: 05b630da838cbf10bd00223ce445917c6d006a94d853e50c5cd2104e1dcdfaf7
- evidence_id: source-manifest
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-source-agent/evidence-manifest.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:28:47.376086Z'
  support: context_only
  summary: All 26 frozen source artifacts verified.
  snapshot_sha256: 8fe94876fd8d34aed99882051635682b78fd63258feb25b39deca2cc96f7d935
- evidence_id: writer-payloads
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-grounding-agent/writer-payload-comparison.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:26:05.512863Z'
  support: context_only
  summary: 'AST-only exact current after-payload comparison and guard inference: review
    no-op, connector preimage rejection and PR664 matched-triple consumer are distinct.
    No writer imported or executed.'
  snapshot_sha256: 70e8aa29d1af3c485dc84ce9f9dbed1a1c14955df0acac966c8175211b758db0
- evidence_id: root-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-source-root/selected-primary-reading.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:27:04.349276Z'
  support: context_only
  summary: Root corrected selected source, authority and owner reading scopes, narrower
    than some source-auditor windows; incidental content not adopted.
  snapshot_sha256: 9f77dc553ec7a0714495fbd5793250c8a26483caa1cab768b1b93e7b92fc058e
- evidence_id: root-verification
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-source-root/root-current-verification.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:31:46.559351Z'
  support: context_only
  summary: Root exact current input, frozen artifact, qualified history and local
    review-array verification.
  snapshot_sha256: 01303911e9b0168cf64d37e8b862e159cc6f3bd099572743d3f64e805a17ebc8
- evidence_id: adjudication
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid3-root-adjudication.json
  locator: Final root adjudication
  accessed_at: '2026-10-22T04:31:46.563626Z'
  support: supports
  summary: Exact two majors and two minors, four findings/actions and owner/field
    scopes control this combined review.
  snapshot_sha256: 42759f9b0e6210977c09ce0abfa58366d3eb6703b8f04a07c5ddf54973fd21e5
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: active bin and direct parent'
  outcome: supported
  target_ids:
  - METPO:1000452
  summary: Active METPO:1000452 and direct parent METPO:1000306 are positive. Historical
    Mesophilie retention is documented; exact biological alias equivalence to the
    unresolved quantity remains unknown. Homeoviscous adaptation METPO:1016200 is
    local v85 proposal identity, not asserted active in the captured upstream raw
    OWL.
  evidence_ids:
  - identity
  - authority-primary
  - source-identities
  - record
- assessment_id: definition
  area: quantity
  topic: 'Native checklist: four ambient-interval versus width anchors'
  outcome: concern
  target_ids:
  - METPO:1000452
  summary: Definition, node 0 and edge 0 describe ambient 30–34 °C, while the canonical
    note describes a width bin. The reported 17–50 °C interval and derived width 33
    are positive. One major reconciles these four fields and exact canonical ledger
    without inferring quantity semantics from generic has-value alone. The current
    graph description is generic context and is excluded from the four numeric anchors.
  evidence_ids:
  - identity
  - authority-primary
  - canonical
  - canonical-metadata
  - owners
  - canonical-writer
  - adjudication
- assessment_id: canonical
  area: evidence
  topic: 'Native checklist: strain-scoped source measurement and identity'
  outcome: supported
  target_ids:
  - METPO:1000452
  summary: The successful canonical metadata retry supports novel strains growing
    at 17–50 °C and names Bacillus nakamurai NRRL B-41091T (=CCUG 68786T); 50 minus
    17 equals the derived width 33. Fresh official taxonomy supports species/type-material
    identity only. No optimum or additional cultivation condition is adopted. The
    initial canonical-metadata.json is DNS error content, not primary support.
  evidence_ids:
  - canonical
  - canonical-metadata
  - canonical-access
  - canonical-initial-failure
  - taxonomy
  - taxonomy-reading
  - adjudication
- assessment_id: source-support
  area: evidence
  topic: 'Native checklist: five works and thirteen placements'
  outcome: concern
  target_ids:
  - METPO:1000452
  summary: All five identities resolve. Mendoza generic physical wording and Tolner
    high-temperature thermophile text do not establish the exact 30–34-bin notes.
    Selected Spectrum and Ramón physical/phase context remains positive. Existing
    supplied regulatory snippets were checked only for literal occurrence; detailed
    sensing, regulation, stress defense, survival/fitness, cultivation optimization
    and intervention efficacy remain unassessed. No whole-paper absence or biological
    refutation is inferred.
  evidence_ids:
  - sources
  - source-identities
  - source-status
  - placements
  - notes
  - source-reading
  - source-access
  - mendoza-metadata
  - tolner-metadata
  - cold-body
  - spectrum-body
  - adjudication
- assessment_id: quotations
  area: evidence
  topic: 'Native checklist: eleven existing literal snippets'
  outcome: supported
  target_ids:
  - METPO:1000452
  summary: 'Manual matching supports all eleven current schema snippets under ordinary
    whitespace normalization: three abstract and eight body spans. Native three VERIFIED
    and eight NOT_IN_ABSTRACT are separate outcomes; the latter are inconclusive for
    body text. Literal occurrence does not establish adjacent numerical-bin support
    or detailed regulatory/fitness efficacy. No copied-span finding is added.'
  evidence_ids:
  - snippets
  - source-native
  - mendoza-metadata
  - tolner-metadata
  - cold-body
  - spectrum-body
  - notes
- assessment_id: nodes
  area: representation
  topic: 'Native checklist: all thirteen current referents'
  outcome: concern
  target_ids:
  - METPO:1000452
  summary: Node 0 participates in quantity scope. Explicit membrane order, conformation
    and phase states, protein and chemical referents remain distinct from processes.
    Phosphorylated-state/material-bearer and rigidity/property readings are qualified
    without extra forced findings. The des_gene identifier does not override its explicit
    protein description. Two reviewed label-only proteins need no accession or instance;
    detailed regulatory efficacy remains unassessed.
  evidence_ids:
  - nodes-edges
  - source-nodes-edges
  - schema
  - local-authority
  - ontology-primary
  - authority-primary
  - policy
  - adjudication
  details: "{\n  \"grounding\": [\n    {\n      \"index\": 0,\n      \"field\": \"\
    causal_graphs[0].nodes[0]\",\n      \"node\": {\n        \"node_id\": \"temperature_range_mid3_trait\"\
    ,\n        \"label\": \"temperature range mid3\",\n        \"node_type\": \"TRAIT\"\
    ,\n        \"grounding\": \"METPO:1000452\",\n        \"description\": \"Temperature\
    \ growth-supporting range approximately 30–34 °C.\"\n      },\n      \"outcome\"\
    : \"concern\",\n      \"judgment\": \"Active exact METPO identity; ambient30–34\
    \ wording conflicts with canonical width33 interpretation.\"\n    },\n    {\n\
    \      \"index\": 1,\n      \"field\": \"causal_graphs[0].nodes[1]\",\n      \"\
    node\": {\n        \"node_id\": \"temperature_range\",\n        \"label\": \"\
    temperature range\",\n        \"node_type\": \"TRAIT\",\n        \"grounding\"\
    : \"METPO:1000306\",\n        \"description\": \"Span of ambient temperatures\
    \ supporting growth.\"\n      },\n      \"outcome\": \"positive\",\n      \"judgment\"\
    : \"Exact active direct temperature-range parent; generic span wording does not\
    \ itself fix the quantitative axis.\"\n    },\n    {\n      \"index\": 2,\n  \
    \    \"field\": \"causal_graphs[0].nodes[2]\",\n      \"node\": {\n        \"\
    node_id\": \"upper_mesophile_adaptation\",\n        \"label\": \"upper-mesophile\
    \ adaptation\",\n        \"node_type\": \"BIOLOGICAL_PROCESS\",\n        \"description\"\
    : \"Mesophile membrane and enzyme tuning for ambient temperatures near common\
    \ animal host body temperatures.\"\n      },\n      \"outcome\": \"qualified\"\
    ,\n      \"judgment\": \"Adaptation/tuning is process-compatible documentary context.\
    \ Detailed host-temperature or enzyme/fitness effects unassessed.\"\n    },\n\
    \    {\n      \"index\": 3,\n      \"field\": \"causal_graphs[0].nodes[3]\",\n\
    \      \"node\": {\n        \"node_id\": \"membrane_order\",\n        \"label\"\
    : \"membrane order / fluidity state\",\n        \"node_type\": \"QUALITY\",\n\
    \        \"description\": \"Physical order/fluidity state of the membrane bilayer;\
    \ the proximate signal for thermosensing.\"\n      },\n      \"outcome\": \"positive\"\
    ,\n      \"judgment\": \"Explicit membrane order/fluidity physical property is\
    \ QUALITY; not an upstream process for RO regulation.\"\n    },\n    {\n     \
    \ \"index\": 4,\n      \"field\": \"causal_graphs[0].nodes[4]\",\n      \"node\"\
    : {\n        \"node_id\": \"desk_kinase_state\",\n        \"label\": \"DesK kinase-dominant\
    \ state\",\n        \"node_type\": \"STATE\",\n        \"description\": \"Membrane\
    \ thickness sensor DesK in its autophosphorylating kinase-dominant conformation.\"\
    \n      },\n      \"outcome\": \"qualified\",\n      \"judgment\": \"Explicit\
    \ kinase-dominant conformation is a molecular STATE. Detailed response efficacy\
    \ unassessed; not itself a process.\"\n    },\n    {\n      \"index\": 5,\n  \
    \    \"field\": \"causal_graphs[0].nodes[5]\",\n      \"node\": {\n        \"\
    node_id\": \"desk\",\n        \"label\": \"DesK\",\n        \"node_type\": \"\
    GENE_OR_PROTEIN\",\n        \"grounding_status\": \"REVIEWED_LABEL_ONLY\",\n \
    \       \"grounding_notes\": \"Reviewed as a contextual protein or protein-complex\
    \ label within a quantitative measurement graph; no exact semantic family term\
    \ was established for this aggregate use.\",\n        \"description\": \"Membrane-bound\
    \ histidine kinase that senses membrane order/thickness.\"\n      },\n      \"\
    outcome\": \"qualified\",\n      \"judgment\": \"Named DesK protein with explicit\
    \ reviewed-label-only status; material referent is clear, no accession/instance\
    \ required.\"\n    },\n    {\n      \"index\": 6,\n      \"field\": \"causal_graphs[0].nodes[6]\"\
    ,\n      \"node\": {\n        \"node_id\": \"phospho_desr\",\n        \"label\"\
    : \"phosphorylated DesR\",\n        \"node_type\": \"STATE\",\n        \"description\"\
    : \"Phosphorylated DesR that tetramerizes and binds the des promoter.\"\n    \
    \  },\n      \"outcome\": \"qualified\",\n      \"judgment\": \"Phosphorylated\
    \ DesR state and material bearer wording overlap. STATE modification/conformation\
    \ reading is plausible; no forced additional type finding. Either reading is nonprocess\
    \ for edge3.\"\n    },\n    {\n      \"index\": 7,\n      \"field\": \"causal_graphs[0].nodes[7]\"\
    ,\n      \"node\": {\n        \"node_id\": \"des_gene\",\n        \"label\": \"\
    des (acyl-lipid desaturase)\",\n        \"node_type\": \"GENE_OR_PROTEIN\",\n\
    \        \"grounding_status\": \"REVIEWED_LABEL_ONLY\",\n        \"grounding_notes\"\
    : \"Reviewed as a contextual protein or protein-complex label within a quantitative\
    \ measurement graph; no exact semantic family term was established for this aggregate\
    \ use.\",\n        \"description\": \"Fatty-acid desaturase that introduces double\
    \ bonds to fluidize the membrane.\"\n      },\n      \"outcome\": \"positive\"\
    ,\n      \"judgment\": \"Despite des_gene identifier and des label, description\
    \ explicitly denotes desaturase protein. Current GENE_OR_PROTEIN is permitted;\
    \ no automatic gene-as-protein finding or accession requirement.\"\n    },\n \
    \   {\n      \"index\": 8,\n      \"field\": \"causal_graphs[0].nodes[8]\",\n\
    \      \"node\": {\n        \"node_id\": \"membrane_fatty_acyl_chains\",\n   \
    \     \"label\": \"membrane fatty acyl chains\",\n        \"node_type\": \"CHEMICAL\"\
    ,\n        \"description\": \"Fatty acyl chains of membrane phospholipids whose\
    \ unsaturation modulates fluidity.\"\n      },\n      \"outcome\": \"positive\"\
    ,\n      \"judgment\": \"Explicit membrane fatty-acyl chemicals/material referent;\
    \ not a biological process.\"\n    },\n    {\n      \"index\": 9,\n      \"field\"\
    : \"causal_graphs[0].nodes[9]\",\n      \"node\": {\n        \"node_id\": \"membrane_rigidity\"\
    ,\n        \"label\": \"membrane rigidification and increased thickness\",\n \
    \       \"node_type\": \"QUALITY\",\n        \"description\": \"Cooling-induced\
    \ membrane rigidification and bilayer thickening, the general homeoviscous sensing\
    \ signal.\"\n      },\n      \"outcome\": \"qualified\",\n      \"judgment\":\
    \ \"Rigidity/thickness physical attribute is a coherent QUALITY reading despite\
    \ process-shaped label. Exact maintained consistency decision supports result/property\
    \ facet; no forced extra finding.\"\n    },\n    {\n      \"index\": 10,\n   \
    \   \"field\": \"causal_graphs[0].nodes[10]\",\n      \"node\": {\n        \"\
    node_id\": \"temperature_decrease\",\n        \"label\": \"temperature decrease\"\
    ,\n        \"node_type\": \"ENVIRONMENTAL_FACTOR\",\n        \"description\":\
    \ \"Drop in ambient temperature within/near the mesophilic range.\"\n      },\n\
    \      \"outcome\": \"positive\",\n      \"judgment\": \"Actual drop in temperature\
    \ is an event; ENVIRONMENTAL_FACTOR is not automatically excluded by enum.\"\n\
    \    },\n    {\n      \"index\": 11,\n      \"field\": \"causal_graphs[0].nodes[11]\"\
    ,\n      \"node\": {\n        \"node_id\": \"homeoviscous_adaptation\",\n    \
    \    \"label\": \"homeoviscous adaptation\",\n        \"node_type\": \"BIOLOGICAL_PROCESS\"\
    ,\n        \"description\": \"Adjustment of membrane lipid composition to maintain\
    \ constant fluidity across temperatures.\",\n        \"grounding\": \"METPO:1016200\"\
    \n      },\n      \"outcome\": \"positive\",\n      \"judgment\": \"Explicit lipid-composition\
    \ adjustment is a process; local v85 METPO1016200 provides exact proposal identity,\
    \ absent from captured upstream raw OWL.\"\n    },\n    {\n      \"index\": 12,\n\
    \      \"field\": \"causal_graphs[0].nodes[12]\",\n      \"node\": {\n       \
    \ \"node_id\": \"liquid_crystalline_membrane\",\n        \"label\": \"liquid-crystalline\
    \ membrane state\",\n        \"node_type\": \"STATE\",\n        \"description\"\
    : \"Functional liquid-crystalline phase of the membrane required for growth.\"\
    \n      },\n      \"outcome\": \"positive\",\n      \"judgment\": \"Liquid-crystalline\
    \ phase is an explicit molecular membrane STATE, not the process of maintaining\
    \ it.\"\n    }\n  ],\n  \"source\": [\n    {\n      \"index\": 0,\n      \"field\"\
    : \"causal_graphs[0].nodes[0]\",\n      \"node_id\": \"temperature_range_mid3_trait\"\
    ,\n      \"node_type\": \"TRAIT\",\n      \"description\": \"Temperature growth-supporting\
    \ range approximately 30–34 °C.\",\n      \"outcome\": \"concern\",\n      \"\
    assessment\": \"Explicit ambient30–34 description participates in quantity conflict;\
    \ ontology identity separate.\"\n    },\n    {\n      \"index\": 1,\n      \"\
    field\": \"causal_graphs[0].nodes[1]\",\n      \"node_id\": \"temperature_range\"\
    ,\n      \"node_type\": \"TRAIT\",\n      \"description\": \"Span of ambient temperatures\
    \ supporting growth.\",\n      \"outcome\": \"supported_generic\",\n      \"assessment\"\
    : \"Parent ambient-temperature span does not settle child endpoints versus width.\"\
    \n    },\n    {\n      \"index\": 2,\n      \"field\": \"causal_graphs[0].nodes[2]\"\
    ,\n      \"node_id\": \"upper_mesophile_adaptation\",\n      \"node_type\": \"\
    BIOLOGICAL_PROCESS\",\n      \"description\": \"Mesophile membrane and enzyme\
    \ tuning for ambient temperatures near common animal host body temperatures.\"\
    ,\n      \"outcome\": \"unknown\",\n      \"assessment\": \"Upper-mesophile enzyme/membrane\
    \ tuning and host-body-temperature context not established by adopted generic\
    \ spans; detailed efficacy unassessed.\"\n    },\n    {\n      \"index\": 3,\n\
    \      \"field\": \"causal_graphs[0].nodes[3]\",\n      \"node_id\": \"membrane_order\"\
    ,\n      \"node_type\": \"QUALITY\",\n      \"description\": \"Physical order/fluidity\
    \ state of the membrane bilayer; the proximate signal for thermosensing.\",\n\
    \      \"outcome\": \"partial_generic\",\n      \"assessment\": \"Generic membrane\
    \ physical order/fluidity positive; specific sensor signal efficacy unassessed.\"\
    \n    },\n    {\n      \"index\": 4,\n      \"field\": \"causal_graphs[0].nodes[4]\"\
    ,\n      \"node_id\": \"desk_kinase_state\",\n      \"node_type\": \"STATE\",\n\
    \      \"description\": \"Membrane thickness sensor DesK in its autophosphorylating\
    \ kinase-dominant conformation.\",\n      \"outcome\": \"UNASSESSED_SCOPE\",\n\
    \      \"assessment\": \"Existing kinase-state label/source literal context only;\
    \ detailed regulation unassessed.\"\n    },\n    {\n      \"index\": 5,\n    \
    \  \"field\": \"causal_graphs[0].nodes[5]\",\n      \"node_id\": \"desk\",\n \
    \     \"node_type\": \"GENE_OR_PROTEIN\",\n      \"description\": \"Membrane-bound\
    \ histidine kinase that senses membrane order/thickness.\",\n      \"outcome\"\
    : \"UNASSESSED_SCOPE\",\n      \"assessment\": \"Existing DesK protein identity/literal\
    \ context only; detailed response efficacy unassessed.\"\n    },\n    {\n    \
    \  \"index\": 6,\n      \"field\": \"causal_graphs[0].nodes[6]\",\n      \"node_id\"\
    : \"phospho_desr\",\n      \"node_type\": \"STATE\",\n      \"description\": \"\
    Phosphorylated DesR that tetramerizes and binds the des promoter.\",\n      \"\
    outcome\": \"UNASSESSED_SCOPE\",\n      \"assessment\": \"Existing phosphorylated\
    \ regulator label retained; detailed binding/regulatory efficacy unassessed.\"\
    \n    },\n    {\n      \"index\": 7,\n      \"field\": \"causal_graphs[0].nodes[7]\"\
    ,\n      \"node_id\": \"des_gene\",\n      \"node_type\": \"GENE_OR_PROTEIN\"\
    ,\n      \"description\": \"Fatty-acid desaturase that introduces double bonds\
    \ to fluidize the membrane.\",\n      \"outcome\": \"UNASSESSED_SCOPE\",\n   \
    \   \"assessment\": \"Existing des/desaturase label retained; detailed effector\
    \ function/fitness unassessed.\"\n    },\n    {\n      \"index\": 8,\n      \"\
    field\": \"causal_graphs[0].nodes[8]\",\n      \"node_id\": \"membrane_fatty_acyl_chains\"\
    ,\n      \"node_type\": \"CHEMICAL\",\n      \"description\": \"Fatty acyl chains\
    \ of membrane phospholipids whose unsaturation modulates fluidity.\",\n      \"\
    outcome\": \"supported_generic\",\n      \"assessment\": \"Generic fatty-acyl\
    \ composition/fluidity physics positive; no Des-specific efficacy adoption.\"\n\
    \    },\n    {\n      \"index\": 9,\n      \"field\": \"causal_graphs[0].nodes[9]\"\
    ,\n      \"node_id\": \"membrane_rigidity\",\n      \"node_type\": \"QUALITY\"\
    ,\n      \"description\": \"Cooling-induced membrane rigidification and bilayer\
    \ thickening, the general homeoviscous sensing signal.\",\n      \"outcome\":\
    \ \"supported_generic_physical\",\n      \"assessment\": \"Generic cooling rigidity/thickness\
    \ sentence positive; detailed sensing efficacy unassessed.\"\n    },\n    {\n\
    \      \"index\": 10,\n      \"field\": \"causal_graphs[0].nodes[10]\",\n    \
    \  \"node_id\": \"temperature_decrease\",\n      \"node_type\": \"ENVIRONMENTAL_FACTOR\"\
    ,\n      \"description\": \"Drop in ambient temperature within/near the mesophilic\
    \ range.\",\n      \"outcome\": \"supported_generic\",\n      \"assessment\":\
    \ \"Ambient temperature drop is generic environmental context, no exact-bin efficacy.\"\
    \n    },\n    {\n      \"index\": 11,\n      \"field\": \"causal_graphs[0].nodes[11]\"\
    ,\n      \"node_id\": \"homeoviscous_adaptation\",\n      \"node_type\": \"BIOLOGICAL_PROCESS\"\
    ,\n      \"description\": \"Adjustment of membrane lipid composition to maintain\
    \ constant fluidity across temperatures.\",\n      \"outcome\": \"partial_generic\"\
    ,\n      \"assessment\": \"Generic lipid-composition/phase context positive; detailed\
    \ regulation/constant-fluidity efficacy unassessed.\"\n    },\n    {\n      \"\
    index\": 12,\n      \"field\": \"causal_graphs[0].nodes[12]\",\n      \"node_id\"\
    : \"liquid_crystalline_membrane\",\n      \"node_type\": \"STATE\",\n      \"\
    description\": \"Functional liquid-crystalline phase of the membrane required\
    \ for growth.\",\n      \"outcome\": \"partial_generic\",\n      \"assessment\"\
    : \"Liquid-crystalline phase physical context positive; required-for-growth/survival\
    \ efficacy unassessed.\"\n    }\n  ]\n}"
- assessment_id: relations
  area: consistency
  topic: 'Native checklist: all ten current relations'
  outcome: concern
  target_ids:
  - METPO:1000452
  summary: Edges 2/3/4/9 import RO2213 or RO2211 process-to-process roles over explicit
    quality, state, protein and chemical endpoints. Edge 6 imports RO2326 material-to-process
    roles for adaptation process to membrane phase state. One formal-role major covers
    all five fields. Broad local confers, direct subclass and Biolink causes/associated_with
    endpoint compatibility remain positive or qualified without proving detailed biology
    or association statistics. No replacement predicate, intermediate or mechanism
    repair is invented.
  evidence_ids:
  - nodes-edges
  - source-nodes-edges
  - ontology-primary
  - authority-primary
  - local-authority
  - adjudication
  details: "{\n  \"grounding\": [\n    {\n      \"index\": 0,\n      \"field\": \"\
    causal_graphs[0].edges[0]\",\n      \"edge\": {\n        \"subject\": \"upper_mesophile_adaptation\"\
    ,\n        \"predicate\": \"confers\",\n        \"object\": \"temperature_range_mid3_trait\"\
    ,\n        \"description\": \"Upper-mesophile adaptation enables growth across\
    \ 30–34 °C.\",\n        \"evidence\": [\n          {\n            \"reference\"\
    : \"DOI:10.1146/annurev-micro-091313-103612\",\n            \"snippet\": \"more\
    \ unsaturated fatty acids\",\n            \"notes\": \"Supports upper-mesophile\
    \ homeoviscous adaptation as the range mechanism.\"\n          }\n        ],\n\
    \        \"predicate_id\": \"METPO:2007700\"\n      },\n      \"outcome\": \"\
    qualified\",\n      \"judgment\": \"Local v8 broad confers permits process/context→trait;\
    \ exact quantitative interpretation is separately conflicting, detailed efficacy\
    \ unassessed.\"\n    },\n    {\n      \"index\": 1,\n      \"field\": \"causal_graphs[0].edges[1]\"\
    ,\n      \"edge\": {\n        \"subject\": \"temperature_range_mid3_trait\",\n\
    \        \"predicate\": \"is a\",\n        \"object\": \"temperature_range\",\n\
    \        \"description\": \"Temperature range mid3 is a quantitative bin of the\
    \ temperature-range phenotype.\",\n        \"evidence\": [\n          {\n    \
    \        \"reference\": \"DOI:10.1016/s0300-9629(97)00003-0\",\n            \"\
    snippet\": \"adapted to environments of high temperature\",\n            \"notes\"\
    : \"Supports the 30–34 °C range as a value within the temperature-range distribution.\"\
    \n          }\n        ],\n        \"predicate_id\": \"rdfs:subClassOf\"\n   \
    \   },\n      \"outcome\": \"positive\",\n      \"judgment\": \"rdfs:subClassOf\
    \ is supported by exact raw METPO child/parent hierarchy.\"\n    },\n    {\n \
    \     \"index\": 2,\n      \"field\": \"causal_graphs[0].edges[2]\",\n      \"\
    edge\": {\n        \"subject\": \"membrane_order\",\n        \"predicate\": \"\
    positively regulates\",\n        \"object\": \"desk_kinase_state\",\n        \"\
    description\": \"Increased membrane order (reduced fluidity) promotes the DesK\
    \ kinase-dominant state; membrane physical state is the proximate signal.\",\n\
    \        \"evidence\": [\n          {\n            \"reference\": \"DOI:10.1128/spectrum.03925-23\"\
    ,\n            \"snippet\": \"Upon temperature decrease, the membrane rigidifies\
    \ and increases in thickness, resulting in activation of the kinase-dominant state\
    \ of DesK\",\n            \"notes\": \"Verified against the open Sidarta et al.\
    \ introduction; the current Des model links temperature-decrease-driven membrane\
    \ rigidification/thickening to the active kinase-dominant state.\"\n         \
    \ }\n        ],\n        \"predicate_id\": \"RO:0002213\"\n      },\n      \"\
    outcome\": \"major\",\n      \"judgment\": \"RO2213 inherits RO2211 process/process;\
    \ membrane-order QUALITY→kinase conformation STATE violates both imported endpoints.\"\
    \n    },\n    {\n      \"index\": 3,\n      \"field\": \"causal_graphs[0].edges[3]\"\
    ,\n      \"edge\": {\n        \"subject\": \"phospho_desr\",\n        \"predicate\"\
    : \"positively regulates\",\n        \"object\": \"des_gene\",\n        \"description\"\
    : \"DesR-P tetramerizes, binds the des promoter, and positively regulates des\
    \ expression for lipid desaturation.\",\n        \"evidence\": [\n          {\n\
    \            \"reference\": \"DOI:10.1128/spectrum.03925-23\",\n            \"\
    snippet\": \"activating expression of the des gene\",\n            \"notes\":\
    \ \"Verified against the open Sidarta et al. introduction; phosphorylated DesR\
    \ tetramers bind Pdes and activate des transcription.\"\n          }\n       \
    \ ],\n        \"predicate_id\": \"RO:0002213\"\n      },\n      \"outcome\": \"\
    major\",\n      \"judgment\": \"RO2213 process/process receives phosphorylated\
    \ state/material subject and explicitly protein object. Protein object independently\
    \ violates range; transcription prose does not change literal endpoint.\"\n  \
    \  },\n    {\n      \"index\": 4,\n      \"field\": \"causal_graphs[0].edges[4]\"\
    ,\n      \"edge\": {\n        \"subject\": \"des_gene\",\n        \"predicate\"\
    : \"regulates\",\n        \"object\": \"membrane_fatty_acyl_chains\",\n      \
    \  \"description\": \"Des-mediated unsaturation regulates membrane fatty acyl\
    \ chains, fluidizing the membrane and reducing bilayer thickness.\",\n       \
    \ \"evidence\": [\n          {\n            \"reference\": \"DOI:10.1128/spectrum.03925-23\"\
    ,\n            \"snippet\": \"desaturates the fatty acyl chains\",\n         \
    \   \"notes\": \"Verified against the open Sidarta et al. introduction; Des desaturates\
    \ membrane-lipid fatty acyl chains as the effector of the DesK/DesR temperature-sensing\
    \ system.\"\n          }\n        ],\n        \"predicate_id\": \"RO:0002211\"\
    \n      },\n      \"outcome\": \"major\",\n      \"judgment\": \"RO2211 directly\
    \ requires process/process; desaturase protein→fatty-acyl chemical endpoints are\
    \ material referents, irrespective of activity described in prose.\"\n    },\n\
    \    {\n      \"index\": 5,\n      \"field\": \"causal_graphs[0].edges[5]\",\n\
    \      \"edge\": {\n        \"subject\": \"temperature_decrease\",\n        \"\
    predicate\": \"causes\",\n        \"object\": \"membrane_rigidity\",\n       \
    \ \"description\": \"A temperature decrease causes membrane rigidification and\
    \ increased thickness, a physical trigger for homeoviscous adaptation.\",\n  \
    \      \"evidence\": [\n          {\n            \"reference\": \"DOI:10.1128/spectrum.03925-23\"\
    ,\n            \"snippet\": \"rigidification and concomitant thickening\",\n \
    \           \"notes\": \"Verified against the open Sidarta et al. introduction;\
    \ temperature decrease is described as causing cell-membrane rigidification and\
    \ thickening.\"\n          }\n        ],\n        \"predicate_id\": \"biolink:causes\"\
    \n      },\n      \"outcome\": \"positive\",\n      \"judgment\": \"Biolink causes\
    \ has broad named-thing ancestry, not RO process/process. Actual temperature-decrease\
    \ event→rigidity property is domain/range compatible; detailed causal efficacy\
    \ unassessed.\"\n    },\n    {\n      \"index\": 6,\n      \"field\": \"causal_graphs[0].edges[6]\"\
    ,\n      \"edge\": {\n        \"subject\": \"homeoviscous_adaptation\",\n    \
    \    \"predicate\": \"contributes to\",\n        \"object\": \"liquid_crystalline_membrane\"\
    ,\n        \"description\": \"Homeoviscous adaptation contributes to a functional\
    \ liquid-crystalline membrane state at low temperature.\",\n        \"evidence\"\
    : [\n          {\n            \"reference\": \"DOI:10.1007/s42770-023-01057-4\"\
    ,\n            \"snippet\": \"maintain the liquid crystalline phase\",\n     \
    \       \"notes\": \"Verified against the open Ramón et al. review; organisms\
    \ in cold environments are described as adapting their membrane composition to\
    \ maintain a liquid-crystalline state.\"\n          }\n        ],\n        \"\
    predicate_id\": \"RO:0002326\"\n      },\n      \"outcome\": \"major\",\n    \
    \  \"judgment\": \"RO2326→2216→2500→2595 inherits material-entity domain and process\
    \ range. Explicit adaptation process→liquid-crystalline STATE violates both roles.\"\
    \n    },\n    {\n      \"index\": 7,\n      \"field\": \"causal_graphs[0].edges[7]\"\
    ,\n      \"edge\": {\n        \"subject\": \"membrane_rigidity\",\n        \"\
    predicate\": \"associated with\",\n        \"object\": \"membrane_order\",\n \
    \       \"description\": \"Cooling-induced membrane rigidification is associated\
    \ with the ordered membrane state sensed by DesK.\",\n        \"evidence\": [\n\
    \          {\n            \"reference\": \"DOI:10.1128/spectrum.03925-23\",\n\
    \            \"snippet\": \"membrane rigidifies and increases in thickness\",\n\
    \            \"notes\": \"Verified against the open Sidarta et al. introduction;\
    \ this connector joins the cooling membrane signal to the DesK kinase-state branch.\"\
    \n          }\n        ],\n        \"predicate_id\": \"biolink:associated_with\"\
    \n      },\n      \"outcome\": \"qualified\",\n      \"judgment\": \"Biolink associated_with\
    \ broad named-thing endpoints permit physical-property association. Detailed source/causal\
    \ interpretation unassessed; no imported RO constraint.\"\n    },\n    {\n   \
    \   \"index\": 8,\n      \"field\": \"causal_graphs[0].edges[8]\",\n      \"edge\"\
    : {\n        \"subject\": \"membrane_fatty_acyl_chains\",\n        \"predicate\"\
    : \"associated with\",\n        \"object\": \"homeoviscous_adaptation\",\n   \
    \     \"description\": \"Des-mediated fatty-acyl-chain unsaturation is associated\
    \ with homeoviscous membrane adaptation.\",\n        \"evidence\": [\n       \
    \   {\n            \"reference\": \"DOI:10.1128/spectrum.03925-23\",\n       \
    \     \"snippet\": \"resulting in membrane fluidization and concomitant decrease\
    \ of bilayer thickness\",\n            \"notes\": \"Verified against the open\
    \ Sidarta et al. introduction; this connector keeps des expression as membrane-fatty-acyl\
    \ remodeling context.\"\n          }\n        ],\n        \"predicate_id\": \"\
    biolink:associated_with\"\n      },\n      \"outcome\": \"qualified\",\n     \
    \ \"judgment\": \"Biolink associated_with admits material→process referents. Edge\
    \ description shifts toward unsaturation activity, retained as a bounded interpretation\
    \ limitation, not a formal domain failure or efficacy verdict.\"\n    },\n   \
    \ {\n      \"index\": 9,\n      \"field\": \"causal_graphs[0].edges[9]\",\n  \
    \    \"edge\": {\n        \"subject\": \"desk\",\n        \"predicate\": \"regulates\"\
    ,\n        \"object\": \"phospho_desr\",\n        \"description\": \"DesK regulates\
    \ DesR phosphorylation in the core two-component signaling step linking membrane\
    \ physical state to transcriptional response.\",\n        \"evidence\": [\n  \
    \        {\n            \"reference\": \"DOI:10.1128/spectrum.03925-23\",\n  \
    \          \"snippet\": \"phosphorylating or dephosphorylating DesR\",\n     \
    \       \"notes\": \"Verified against the open Sidarta et al. introduction; DesK\
    \ is described as a membrane-associated histidine kinase that phosphorylates or\
    \ dephosphorylates DesR in a temperature-dependent manner.\"\n          }\n  \
    \      ],\n        \"predicate_id\": \"RO:0002211\"\n      },\n      \"outcome\"\
    : \"major\",\n      \"judgment\": \"RO2211 process/process receives explicit DesK\
    \ protein→phosphorylated STATE/material bearer. Literal endpoints remain nonprocess\
    \ despite phosphorylation-action prose.\"\n    }\n  ],\n  \"source\": [\n    {\n\
    \      \"index\": 0,\n      \"field\": \"causal_graphs[0].edges[0]\",\n      \"\
    subject\": \"upper_mesophile_adaptation\",\n      \"predicate\": \"confers\",\n\
    \      \"object\": \"temperature_range_mid3_trait\",\n      \"description\": \"\
    Upper-mesophile adaptation enables growth across 30–34 °C.\",\n      \"references\"\
    : [\n        \"DOI:10.1146/annurev-micro-091313-103612\"\n      ],\n      \"outcome\"\
    : \"unknown_exact_bin\",\n      \"assessment\": \"Generic physical phrase literal;\
    \ upper-mesophile mechanism/exact-bin sufficiency unassessed. Description explicitly\
    \ uses ambient interval.\"\n    },\n    {\n      \"index\": 1,\n      \"field\"\
    : \"causal_graphs[0].edges[1]\",\n      \"subject\": \"temperature_range_mid3_trait\"\
    ,\n      \"predicate\": \"is a\",\n      \"object\": \"temperature_range\",\n\
    \      \"description\": \"Temperature range mid3 is a quantitative bin of the\
    \ temperature-range phenotype.\",\n      \"references\": [\n        \"DOI:10.1016/s0300-9629(97)00003-0\"\
    \n      ],\n      \"outcome\": \"attribution_concern\",\n      \"assessment\"\
    : \"Literal phrase explicitly thermophile context; nearest span does not establish\
    \ exact30–34 note. Formal hierarchy separate.\"\n    },\n    {\n      \"index\"\
    : 2,\n      \"field\": \"causal_graphs[0].edges[2]\",\n      \"subject\": \"membrane_order\"\
    ,\n      \"predicate\": \"positively regulates\",\n      \"object\": \"desk_kinase_state\"\
    ,\n      \"description\": \"Increased membrane order (reduced fluidity) promotes\
    \ the DesK kinase-dominant state; membrane physical state is the proximate signal.\"\
    ,\n      \"references\": [\n        \"DOI:10.1128/spectrum.03925-23\"\n      ],\n\
    \      \"outcome\": \"UNASSESSED_SCOPE\",\n      \"assessment\": \"Supplied snippet\
    \ literal; detailed DesK kinase-state regulation/efficacy unassessed.\"\n    },\n\
    \    {\n      \"index\": 3,\n      \"field\": \"causal_graphs[0].edges[3]\",\n\
    \      \"subject\": \"phospho_desr\",\n      \"predicate\": \"positively regulates\"\
    ,\n      \"object\": \"des_gene\",\n      \"description\": \"DesR-P tetramerizes,\
    \ binds the des promoter, and positively regulates des expression for lipid desaturation.\"\
    ,\n      \"references\": [\n        \"DOI:10.1128/spectrum.03925-23\"\n      ],\n\
    \      \"outcome\": \"UNASSESSED_SCOPE\",\n      \"assessment\": \"Supplied snippet\
    \ literal; detailed DesR transcriptional regulation/efficacy unassessed.\"\n \
    \   },\n    {\n      \"index\": 4,\n      \"field\": \"causal_graphs[0].edges[4]\"\
    ,\n      \"subject\": \"des_gene\",\n      \"predicate\": \"regulates\",\n   \
    \   \"object\": \"membrane_fatty_acyl_chains\",\n      \"description\": \"Des-mediated\
    \ unsaturation regulates membrane fatty acyl chains, fluidizing the membrane and\
    \ reducing bilayer thickness.\",\n      \"references\": [\n        \"DOI:10.1128/spectrum.03925-23\"\
    \n      ],\n      \"outcome\": \"UNASSESSED_SCOPE\",\n      \"assessment\": \"\
    Supplied snippet literal; detailed Des-mediated effector/regulatory efficacy unassessed.\"\
    \n    },\n    {\n      \"index\": 5,\n      \"field\": \"causal_graphs[0].edges[5]\"\
    ,\n      \"subject\": \"temperature_decrease\",\n      \"predicate\": \"causes\"\
    ,\n      \"object\": \"membrane_rigidity\",\n      \"description\": \"A temperature\
    \ decrease causes membrane rigidification and increased thickness, a physical\
    \ trigger for homeoviscous adaptation.\",\n      \"references\": [\n        \"\
    DOI:10.1128/spectrum.03925-23\"\n      ],\n      \"outcome\": \"supported_generic_physical\"\
    ,\n      \"assessment\": \"Selected Spectrum body p1 final sentence supports generic\
    \ cooling, rigidity and thickness, not detailed adaptation efficacy.\"\n    },\n\
    \    {\n      \"index\": 6,\n      \"field\": \"causal_graphs[0].edges[6]\",\n\
    \      \"subject\": \"homeoviscous_adaptation\",\n      \"predicate\": \"contributes\
    \ to\",\n      \"object\": \"liquid_crystalline_membrane\",\n      \"description\"\
    : \"Homeoviscous adaptation contributes to a functional liquid-crystalline membrane\
    \ state at low temperature.\",\n      \"references\": [\n        \"DOI:10.1007/s42770-023-01057-4\"\
    \n      ],\n      \"outcome\": \"partial_generic_literal\",\n      \"assessment\"\
    : \"Supplied phase-maintenance phrase literal; generic phase context positive,\
    \ survival/adaptive efficacy and exact-bin sufficiency unassessed.\"\n    },\n\
    \    {\n      \"index\": 7,\n      \"field\": \"causal_graphs[0].edges[7]\",\n\
    \      \"subject\": \"membrane_rigidity\",\n      \"predicate\": \"associated\
    \ with\",\n      \"object\": \"membrane_order\",\n      \"description\": \"Cooling-induced\
    \ membrane rigidification is associated with the ordered membrane state sensed\
    \ by DesK.\",\n      \"references\": [\n        \"DOI:10.1128/spectrum.03925-23\"\
    \n      ],\n      \"outcome\": \"partial_generic_literal\",\n      \"assessment\"\
    : \"Supplied physical-change phrase literal; generic rigidity/order context positive,\
    \ specific sensing/regulatory coupling unassessed.\"\n    },\n    {\n      \"\
    index\": 8,\n      \"field\": \"causal_graphs[0].edges[8]\",\n      \"subject\"\
    : \"membrane_fatty_acyl_chains\",\n      \"predicate\": \"associated with\",\n\
    \      \"object\": \"homeoviscous_adaptation\",\n      \"description\": \"Des-mediated\
    \ fatty-acyl-chain unsaturation is associated with homeoviscous membrane adaptation.\"\
    ,\n      \"references\": [\n        \"DOI:10.1128/spectrum.03925-23\"\n      ],\n\
    \      \"outcome\": \"UNASSESSED_SCOPE\",\n      \"assessment\": \"Supplied phrase\
    \ literal; detailed Des remodeling/regulation efficacy unassessed.\"\n    },\n\
    \    {\n      \"index\": 9,\n      \"field\": \"causal_graphs[0].edges[9]\",\n\
    \      \"subject\": \"desk\",\n      \"predicate\": \"regulates\",\n      \"object\"\
    : \"phospho_desr\",\n      \"description\": \"DesK regulates DesR phosphorylation\
    \ in the core two-component signaling step linking membrane physical state to\
    \ transcriptional response.\",\n      \"references\": [\n        \"DOI:10.1128/spectrum.03925-23\"\
    \n      ],\n      \"outcome\": \"UNASSESSED_SCOPE\",\n      \"assessment\": \"\
    Supplied phrase literal; detailed DesK/DesR phosphoregulation efficacy unassessed.\"\
    \n    }\n  ]\n}"
- assessment_id: owners
  area: ownership
  topic: 'Native checklist: exact templates and distinct guarded consumers'
  outcome: supported
  target_ids:
  - METPO:1000452
  summary: Canonical SOURCES/TRANCHE preserves the correct measurement and width;
    coordinate interpretation with equality/no-op, nonempty rejection and queue guards.
    The review after-payloads match current edges, implying a current no-op; connector
    SOURCE_CONNECTOR_EDGES are guards and its metadata preimage currently rejects.
    PR664 replaces matching triples from templates and differs from the generic predicate
    grounder, which skips populated IDs. Mapping rows 10/11/99 are conditional recurrence
    inputs. These are static inferences, not executed writer outcomes.
  evidence_ids:
  - owners
  - owner-primary
  - writer-payloads
  - canonical-writer
  - predicate-mapping
  - discovery
  - adjudication
- assessment_id: provenance
  area: provenance
  topic: 'Native checklist: bounded human acceptance link'
  outcome: concern
  target_ids:
  - METPO:1000452
  summary: Nineteen embedded events comprise eighteen AI-assisted events and a seed.
    All 26 current actor projections are AI; whole-history scope is 25 exact qualified
    prior readings plus one fresh infrastructure history. Ignored- and hidden-inclusive
    search excluding .git/.venv internals found 191 matching paths and 69 matching
    arrays; all 94 actual local top-level review target arrays have zero exact match.
    Private/remote acceptance remains unknown.
  evidence_ids:
  - human-search
  - histories
  - embedded-history
  - discovery
  - ground-reading
  - root-reading
  - root-verification
  - record
- assessment_id: expression
  area: completeness
  topic: 'Native checklist: retained species catalog and bounded adapter availability'
  outcome: unknown
  target_ids:
  - METPO:1000452
  summary: The retained original catalog contains 20 organisms and 28 datasets. B.
    subtilis adopted title context has species-level coverage only, with no strain/module
    or efficacy result; no exact B. nakamurai canonical key was found. A maintained
    runner was unavailable within bounded current discovery, so no module query was
    executed. This does not establish global organism absence.
  evidence_ids:
  - expression
  - expression-discovery
  - catalog-original
  - catalog-reuse
  - source-reading
  - adjudication
- assessment_id: readiness
  area: completeness
  topic: 'Native checklist: intentional NONMECHANISTIC components and label-only proteins'
  outcome: supported
  target_ids:
  - METPO:1000452
  summary: Three components with thirteen nodes and ten edges are explicitly retained
    by current NONMECHANISTIC corrective history. Two reviewed label-only proteins
    and zero instances require no invented connector, accession or dataset. Historical
    protein/component counts are not substituted for current structure. These positives
    do not resolve quantity, attribution or formal-role findings.
  evidence_ids:
  - record
  - nodes-edges
  - expression
  - histories
  - policy
- assessment_id: validation
  area: schema
  topic: 'Native checklist: current native checks and qualified B14 diagnostics'
  outcome: supported
  target_ids:
  - METPO:1000452
  summary: Current inspect, target validation, strict validation and snippet checks
    are successful B15 executions. Four original B14 common diagnostics are qualified
    for unchanged B15 inputs, not relabeled as fresh B15 executions. Original intervals,
    historical attempts, product skips and omitted full just test remain explicit.
    These eight command checks do not establish scientific correctness or human acceptance.
  evidence_ids:
  - capture
  - common-reuse-qualification
  - original-b14-common-completion
  - check-temperature-range-mid3-target-validate
  - check-temperature-range-mid3-target-strict
  - check-temperature-range-mid3-snippets-network
  - source-native
findings:
- finding_id: quantity-scope
  issue_key: temperature-range-mid3-quantity-scope
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Quantity scope
  description: The definition, node0 and edge0 use30–34 °C as ambient temperatures;
    the canonical note treats30–34 degrees as an interval-width bin. Primary PMID27150918
    reports novel strains growing at17–50 °C and identifies Bacillus nakamurai NRRL
    B-41091T, giving derived50−17=33. The measurement and arithmetic are positive.
    Raw METPO gives a generic existential value in[30,34], which does not select endpoints
    versus width. Reconcile the operational quantity and canonical membership with
    the exact maintained ledger. The current graph description contains generic context
    and is excluded from the four explicit numeric anchors.
  target_ids:
  - METPO:1000452
  field_paths:
  - definition
  - canonical_examples[0].note
  - causal_graphs[0].nodes[0].description
  - causal_graphs[0].edges[0].description
  evidence_ids:
  - record
  - identity
  - authority-primary
  - canonical
  - canonical-metadata
  - owners
  - canonical-writer
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_range_mid3.yaml
    role: Current record assertions; separate authorized curation required
  - repository: CultureBotAI/TraitMech
    path: scripts/backfill_canonical_examples_444.py
    role: Exact source/TRANCHE with positive measurement and derived width; coordinate
      interpretation while preserving equality/rejection/global queue guards
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: imported-process-roles
  issue_key: temperature-range-mid3-imported-process-roles
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Imported process roles
  description: Edges2/3 use RO:0002213 and edges4/9 use RO:0002211, requiring process-to-process
    roles. Their explicit quality, molecular-state, protein and chemical referents
    are nonprocess endpoints. Edge6 uses RO:0002326, whose2326→2216→2500→2595 ancestry
    requires material entity→process, for an adaptation process→membrane phase state.
    Exact review after-payloads match current edges, so the review transform would
    no-op; the connector holds these as source guards and currently rejects its metadata
    preimage. The PR664 consumer replaces matched triples from those templates, unlike
    the generic grounder, which skips populated IDs. Wildcard mapping rows10/11/99
    are conditional recurrence inputs. Coordinate these distinct owner roles without
    inventing biological intermediates or relabeling referents merely to satisfy predicates.
  target_ids:
  - METPO:1000452
  field_paths:
  - causal_graphs[0].edges[2].predicate_id
  - causal_graphs[0].edges[3].predicate_id
  - causal_graphs[0].edges[4].predicate_id
  - causal_graphs[0].edges[6].predicate_id
  - causal_graphs[0].edges[9].predicate_id
  evidence_ids:
  - nodes-edges
  - ontology-primary
  - schema
  - predicate-mapping
  - owners
  - owner-primary
  - writer-payloads
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_range_mid3.yaml
    role: Current record assertions; separate authorized curation required
  - repository: CultureBotAI/TraitMech
    path: scripts/review_temperature_range_mid3_graph_183.py
    role: Exact after-edge payload owner; all six after dictionaries match current
      edges, implying guarded no-op
  - repository: CultureBotAI/TraitMech
    path: scripts/connect_temperature_range_mid3_graph_183.py
    role: SOURCE_CONNECTOR_EDGES holds review payloads as source guards; current metadata
      preimage rejects; surviving association additions are not the conflicting RO
      source
  - repository: CultureBotAI/TraitMech
    path: scripts/repair_pr664_adversarial_review.py
    role: Matched-triple template consumer and repair additions; unlike generic grounder,
      replaces populated predicates while enforcing expected-key guards
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Wildcard contributes-to row 10, regulates row 11 and positively-regulates
      row 99 are future empty-field recurrence inputs
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Conditional generic consumer skips populated identifiers; ordinary replay
      is not current-field repair
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: bin-attribution
  issue_key: temperature-range-mid3-bin-attribution
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Bin attribution
  description: The Mendoza note attributes exact30–34 °C upper-mesophile support to
    a generic membrane-physics phrase. The Tolner note attributes that bin to a supplied
    phrase explicitly concerning high-temperature thermophiles. Both snippets are
    literal; the nearest inspected spans do not establish the adjacent exact numerical-bin
    claims. This bounded attribution concern is separate from quantity semantics and
    does not assert whole-paper absence, false quotation or biological refutation.
    The subclass relation has independent raw-ontology support.
  target_ids:
  - METPO:1000452
  field_paths:
  - evidence[0].notes
  - causal_graphs[0].edges[1].evidence[0].notes
  evidence_ids:
  - sources
  - placements
  - notes
  - mendoza-metadata
  - tolner-metadata
  - source-reading
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_range_mid3.yaml
    role: Current record assertions; separate authorized curation required
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: human-acceptance-link
  issue_key: temperature-range-mid3-human-acceptance-link
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Human acceptance link
  description: REVIEWED status has no retrievable exact-target human acceptance in
    the bounded local evidence. The19 embedded events comprise18 AI-assisted entries
    and the METPO seed. All26 current captured history actor projections are AI;25
    whole readings are exact qualified prior readings and one infrastructure history
    was read whole currently. Ignored- and hidden-inclusive local discovery excluding.git/.venv
    internals found191 matching paths and69 matching review arrays; all94 actual local
    top-level target arrays contain zero exact target matches. Private or remote acceptance
    remains unknown.
  target_ids:
  - METPO:1000452
  field_paths:
  - mapping_status
  - curation_history
  evidence_ids:
  - human-search
  - histories
  - embedded-history
  - discovery
  - ground-reading
  - root-reading
  - root-verification
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_range_mid3.yaml
    role: Current record assertions; separate authorized curation required
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
actions:
- action_id: curate-quantity-scope
  description: In separately authorized curation, define the measured quantity and
    reconcile the four numeric anchors with the canonical ledger.
  finding_ids:
  - quantity-scope
  target_ids:
  - METPO:1000452
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_range_mid3.yaml
    role: Current record assertions; separate authorized curation required
  - repository: CultureBotAI/TraitMech
    path: scripts/backfill_canonical_examples_444.py
    role: Exact source/TRANCHE with positive measurement and derived width; coordinate
      interpretation while preserving equality/rejection/global queue guards
  acceptance_checks:
  - Establish source-backed quantity and units without deriving endpoints versus width
    from generic has-value alone.
  - Preserve reported17–50 °C and explicitly derived width33; distinguish these positive
    observations from bin membership.
  - Coordinate SOURCES88–90/TRANCHE607–612 and equality/no-op, nonempty-rejection
    and global queue guards. The correct measurement is not a false writer payload.
  - Use guarded record/history curation, focused strict validation and applicable
    QC/products; regenerate affected products.
- action_id: curate-imported-process-roles
  description: Resolve the five imported relation assertions against the existing
    declared referents and coordinate exact templates, consumer guards and conditional
    mapping recurrence.
  finding_ids:
  - imported-process-roles
  target_ids:
  - METPO:1000452
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_range_mid3.yaml
    role: Current record assertions; separate authorized curation required
  - repository: CultureBotAI/TraitMech
    path: scripts/review_temperature_range_mid3_graph_183.py
    role: Exact after-edge payload owner; all six after dictionaries match current
      edges, implying guarded no-op
  - repository: CultureBotAI/TraitMech
    path: scripts/connect_temperature_range_mid3_graph_183.py
    role: SOURCE_CONNECTOR_EDGES holds review payloads as source guards; current metadata
      preimage rejects; surviving association additions are not the conflicting RO
      source
  - repository: CultureBotAI/TraitMech
    path: scripts/repair_pr664_adversarial_review.py
    role: Matched-triple template consumer and repair additions; unlike generic grounder,
      replaces populated predicates while enforcing expected-key guards
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Wildcard contributes-to row 10, regulates row 11 and positively-regulates
      row 99 are future empty-field recurrence inputs
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Conditional generic consumer skips populated identifiers; ordinary replay
      is not current-field repair
  acceptance_checks:
  - Document each edge subject/object referent and effective domain/range; preserve
    quality, state, material and process distinctions.
  - Coordinate review EDGE_REPLACEMENTS, connector SOURCE_CONNECTOR_EDGES guards and
    PR664 matched-triple replacement/repair addition behavior. The connector surviving
    additions are two broad associations, not the conflicting RO payload source.
  - Address contributes-to row10, regulates row11 and positively-regulates row99 for
    future empty fields; explicit guarded curation must address current populated
    IDs.
  - Use meaningful focused grounding/guard regression checks, strict validation and
    applicable QC/products. No pathway addition, operational mechanism repair or efficacy
    improvement is prescribed.
- action_id: curate-bin-attribution
  description: Qualify the two notes to distinguish generic physical or thermophile
    context from exact numerical-bin authority.
  finding_ids:
  - bin-attribution
  target_ids:
  - METPO:1000452
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_range_mid3.yaml
    role: Current record assertions; separate authorized curation required
  acceptance_checks:
  - Describe the nearest inspected spans accurately; exact30–34 calibration needs
    identified support or remains qualified.
  - Preserve all11 literal snippets and distinguish manual body matching from native3
    VERIFIED/8 NOT_IN_ABSTRACT inconclusive outcomes.
  - Preserve independently supported hierarchy and avoid whole-paper absence or false-quotation
    claims; validate separately curated changes.
- action_id: curate-human-acceptance-link
  description: Link attributable human acceptance for REVIEWED status or accurately
    qualify the review state in separately authorized curation.
  finding_ids:
  - human-acceptance-link
  target_ids:
  - METPO:1000452
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_range_mid3.yaml
    role: Current record assertions; separate authorized curation required
  acceptance_checks:
  - Provide actor identity, exact scope and retrievable acceptance; AI history and
    seed import do not establish human signoff.
  - Retain bounded local-search scope and private/remote uncertainty.
  - Use maintained guarded history and validation for any curation change.
limitations:
- No fresh B15 common diagnostic execution is asserted. Full just test was NOT_RUN;
  only the five optional focused Stage2 tests are reused. Products retains 123 no-adapter
  skips and covers two configured mappings. Common checks establish bounded software/data
  integrity, not scientific support, current-target checks or prior-batch finalization.
  Serializers must append to these helper notes and limitations.
- Detailed stress-defense/regulatory/survival/fitness/cultivation optimization/intervention
  efficacy UNASSESSED_SCOPE; no operational repairs.
- Canonical interval17–50 and derivedwidth33 positive; ambient30–34 versus width30–34
  counted once.
- All11 snippets literal; native3 VERIFIED/8 NOT_IN_ABSTRACT inconclusive for body
  text and not false evidence.
- Spectrum bodyp3/p5 machine-searched only for existing supplied short fragments;
  detailed DesK/DesR/des regulation/efficacy not adjudicated.
- Spectrum bodyp1 first/final sentences adopted for generic physical context only.
- Ramón all-HTMLp17 sentence index5 displayed during matching, including survival/freezing
  wording; only supplied phase-maintenance fragment and generic phase context adopted,
  no survival efficacy.
- Tolner second abstract sentence displayed wider transport/enzyme details; only explicit
  thermophile context and supplied phrase adopted.
- Complete canonical abstract displayed; culture, salt/pH/chemistry and comparative
  genomic details incidental, not adopted beyond named type strain/aliases and existing
  growth interval.
- Four metadata status observations and body/browser surfaces are exact historical
  reuse; null notices do not establish exhaustive current absence.
- Retained publisher tool export is not rawHTML; underlying cache fetch time unknown.
- Initial canonical-metadata.json contains DNS error bytes; only canonical-metadata-network-retry.json
  is successful primary metadata.
- Exact mesophilic alias biological equivalence and exact-bin calibration unknown;
  generic physical context does not choose bin semantics.
- Detailed temperature response, regulatory mechanisms, survival/fitness/defense,
  cultivation and optimization efficacy UNASSESSED_SCOPE.
- Phosphorylated-state/material-bearer and rigidification/property wording qualified,
  not forced into extra findings.
- Generic numeric existential does not settle interval-versus-width; exact alias equivalence
  unresolved.
- 25 prior whole readings plus1fresh whole history and26 current projections; no claim
  all26 readwhole currently.
- Ground auditor did not rerun common/native/DB checks; root owns independent native
  checks.
- Uncaptured discovery stays matching-line context; private/remote human acceptance
  unknown.
- Root adopted Spectrum zero-based bodyp1 first/final generic physical sentences and
  Ramón all-HTMLp17 first four physical sentences. Detailed regulation, survival,
  fitness, cultivation optimization and intervention efficacy remain unassessed even
  where snippets are literal.
- Canonical and taxonomy initial DNS failures and successful retries retain separate
  times/bytes; taxonomy establishes identity, not phenotype.
- Current writer outcomes are static inferences from read guards and exact data comparison;
  no writer or full PR664 dry run was executed.
- Original B14 common diagnostics are qualified for unchanged B15 inputs, not fresh
  B15 executions. Current target inspect, target validation, strict validation and
  snippet check are fresh. The serializer common guard separately rechecks current
  inputs and five database pins.
- Full just test was not run; focused Stage2 tests and product skips retain their
  original scope. Software checks do not establish scientific correctness.
- Active exact METPO:1000452 and parent METPO:1000306 are positive. Historical Mesophilie
  retention is documented in active-review106/release-delta1274 and finalizer; biological
  exact-alias equivalence to unresolved quantity remains unknown.
- Homeoviscous adaptation METPO:1016200 is local v85 proposal/mapping identity, absent
  from captured upstream raw OWL. Broad localv8 confers admits current process→trait
  roles; quantity/efficacy separate.
- Biolink causes and associated_with have broad NamedThing roles, not imported RO
  regulation constraints. Endpoint compatibility alone does not prove association
  statistics or detailed biology.
- Des_gene explicitly describes a desaturase protein despite its identifier. DesK
  conformation and phosphorylated DesR are qualified molecular-state readings; rigidity/thickness
  has a coherent property reading and explicit corrective history. No additional forced
  type finding.
- Canonical source and official taxonomy support B.nakamurai NRRL B-41091T (=CCUG68786T),
  existing17–50 interval and derived width33. No additional cultivation condition
  or optimum is adopted.
- Three components,13 nodes/10 edges, two REVIEWED_LABEL_ONLY proteins and zero instances
  are permissible NONMECHANISTIC context. Corrective history intentionally retains
  three components; no invented connector/accession/dataset.
- The retained20-organism/28-dataset catalog has B.subtilis species-level coverage
  for the adopted title context, without strain/module/efficacy inference. No exact
  B.nakamurai canonical entry was found in that catalog. Bounded current adapter discovery
  found no maintained runner; no module query was executed.
- Publication is separate from this local review. No scientific record, mapping, ontology,
  history, generated product or paid-provider run changed.
notes:
- Qualified reuse of four original B14 diagnostics is recorded in /private/tmp/traitmech-record-sweep-015.67f2ce7a/common-diagnostic-reuse-qualification.json.
  Historical products failures/retry and original cache provenance remain in /private/tmp/traitmech-record-sweep-014.q8m4v2cs/new-base-diagnostic-independent-review-agent/fresh-products-completion.json.
  B14 generated reports are retained output snapshots, not B15 source inputs or synthetic
  B15 reports. B15-to-B14 byte equality does not change the historical false B14-to-B13
  comparison; B14 final gates/commit and continuation pins remain separate.
- Exact findings, actions, fields, severities and owners come only from root FINAL.
  Four explicit quantity anchors form one major; the separate five-edge imported-role
  group and two bounded minors are retained without extra type or connectivity findings.
- Serializer preparation adopts frozen audits and root adjudication without another
  whole-paper or whole-history review. Eight historical source access clocks, current
  canonical/taxonomy failure and retry clocks, root authority-query clocks and subsequent
  copying/reading remain distinct. Ground-auditor non-repetition is actor-specific;
  the common guard separately rechecks qualified current inputs and database pins.
  Original B14 diagnostics are not relabeled fresh B15 executions.
tags:
- record-review
- temperature-range-mid3
- environment
- needs-curation
```
