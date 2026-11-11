# Whole-record review of temperature range very low

- Review: 20261022T050833Z-temperature-range-very-low
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-22T04:55:02.134554Z
- Finished UTC: 2026-10-22T05:08:33Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Whole-record review identifies incompatible imported process roles at four edges and three bounded minor issues: machinery facet, three source-surface notes and retrievable human acceptance. Current threshold semantics are internally coherent. Active identity, canonical reported -12 to10 degreesC interval, all15 literal quotations and selected formal facets are positive; detailed biological efficacy remains unassessed.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: Fifth record in the actual B15 queue; current 366-line target and 101 captured inputs. Local review is independent of remote publication.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 508ee3089c93a36413969cd1ede7f9528a1940a4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| METPO:1000448 | data/traits/environment/temperature_range_very_low.yaml | maintained | temperature range very low |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Reused B14 corpus QC | passed | True | METPO:1000448 | Actual just qc passed: strict validation of 1130 records with 0 errors; graph audit: 74 baselined, 0 new and 0 blocking findings; 135 connected graphs and 1588 wired nodes; protein coverage: 729 graphs (134 pass, 594 NONMECHANISTIC, 0 gaps, 1 protected); snippet audit: 2419 baselined, 0 new and 0 blocking findings; 19 PathwayMech links. These are corpus diagnostics, not scientific validation of this target. |
| Reused B14 history integrity | passed | True | METPO:1000448 | 1278 HistoryRecord YAMLs validated, 0 invalid; current history snapshot contains 1279 files. Integrity does not establish scientific correctness or human acceptance. |
| Reused B14 mapping identifier/label validation | passed | True | METPO:1000448 | 361 canonical matches, 2 exact-synonym matches, 1 exception and 123 SKIPPED_NO_ADAPTER pairs. Configured scope is the two grounding mappings, not every target identifier or scientific claim. |
| Reused B14 focused Stage2 writer tests | passed | False | METPO:1000448 | Five tests passed in the explicitly selected Stage2 test file. This is not a full just test run or biological validation. |
| Focused native validation | passed | True | METPO:1000448 | Native validation passed; scientific interpretation is assessed separately. |
| Focused strict validation | passed | True | METPO:1000448 | The actual validate-strict command passed. |
| Focused network snippet check | passed | True | METPO:1000448 | Native command succeeded for fifteen snippets: four VERIFIED and eleven NOT_IN_ABSTRACT, the latter inconclusive. Manual matching supports all fifteen literal spans; three notes misidentify their source surface. |
| One-target native review capture | passed | True | METPO:1000448 | One current target, 101 captured inputs, exact current base and successful native inspect. |
| Protein-instance metadata applicability | not_applicable | False | METPO:1000448 | Three contextual protein aggregates are REVIEWED_LABEL_ONLY with rationales and zero instances; no token accession required. |
| Structured source-organism expression query availability | unavailable | False | METPO:1000448 | Bounded maintained-runner discovery found no adapter. Retained catalog and selected source identities provide no module or efficacy result. |

## Scientific And Domain Assessments

### Native checklist: active bin, parent and bounded alias interpretation

identity: supported. Targets: METPO:1000448.

Active METPO:1000448, direct parent METPO:1000306 and the numeric-temperature/growth-range lineage are supported. Raw maximum-inclusive 10 Cel uses generic has-value. Local membrane fluidity is a v3 identity absent from captured upstream raw OWL; broad v8 confers is retained. Exact biological Psychrophile equivalence remains qualified.

### Native checklist: internally coherent ambient threshold

quantity: supported. Targets: METPO:1000448.

Definition, node 0, edge 0, graph description and canonical note use growth reaching an ambient threshold at or below approximately 10 °C. The reported -12 to 10 °C interval supports that use. No interval-width conflict is inherited from siblings. Exact inclusive-boundary calibration and broad alias equivalence remain qualified; generic has-value alone is not a complete measurement protocol.

### Native checklist: existing strain-scoped interval and identity

evidence: supported. Targets: METPO:1000448.

Successful canonical metadata retry supports Psychromonas ingrahamii strain 37T, the existing -12 to 10 °C interval and CCUG51855T/CIP108865T aliases. Official taxonomy supports identity only. No full curve, optimum or other culture/composition/genomic property is adopted. Initial canonical and taxonomy error bytes remain distinct from successful retries.

### Native checklist: five works and seventeen placements

evidence: concern. Targets: METPO:1000448.

Five identities, selected near-freezing classification and generic physical context are supported. Three notes incorrectly attribute body quotations to PubMed abstracts. Detailed signaling, regulation, stress defense, survival, fitness, cryoprotection, cultivation optimization and intervention efficacy remain unassessed. Ramasamy matching establishes six supplied literal spans only; no surrounding numerical-strain comparison or mechanistic efficacy is adopted.

### Native checklist: fifteen literal spans and three body locators

evidence: supported. Targets: METPO:1000448.

All fifteen schema snippets are literal. Native four VERIFIED and eleven NOT_IN_ABSTRACT are distinct, with abstract misses inconclusive for body text. Edges 8/9 use Ramón body paragraphs 17/31; edge 10 uses Phadtare body paragraph 11. Their exact spans are absent from inspected indexed and PMC abstracts. Correcting three note locators does not change literal status or establish detailed efficacy.

### Native checklist: all fifteen current referents

representation: concern. Targets: METPO:1000448.

The machinery node combines a process type with material enzymes/membranes and a functional clause, warranting bounded facet clarification without prescribing a replacement enum. RNA secondary structure and membrane fluidity are qualities; low temperature is an ambient condition with coherent PATO closeMatch; ice growth is processual. Node 6 signaling-system wording remains qualified without an extra type finding. Three label-only aggregates require no accession or instance.

{
  "grounding": [
    {
      "index": 0,
      "field": "causal_graphs[0].nodes[0]",
      "node": {
        "node_id": "temperature_range_very_low_trait",
        "label": "temperature range very low",
        "node_type": "TRAIT",
        "grounding": "METPO:1000448",
        "description": "Temperature growth-supporting range reaching ≤ ~10 °C."
      },
      "outcome": "positive",
      "judgment": "Exact active METPO1000448; current reach-at-or-below-10 wording agrees internally with canonical threshold use. Generic raw numerical property does not independently force width semantics."
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
      "judgment": "Exact active direct temperature-range parent; parent also has numerical-temperature and numerical-growth-range parents."
    },
    {
      "index": 2,
      "field": "causal_graphs[0].nodes[2]",
      "node": {
        "node_id": "psychrophile_machinery",
        "label": "psychrophile cold-adapted machinery",
        "node_type": "BIOLOGICAL_PROCESS",
        "description": "Cold-active enzymes and unsaturated-lipid membranes that sustain function near freezing."
      },
      "outcome": "minor",
      "judgment": "BIOLOGICAL_PROCESS contrasts with a machinery label and description enumerating material enzymes and membranes. The functional sustaining clause permits a process interpretation but does not identify one; bounded referent/facet precision is needed without prescribing a replacement enum or mechanism."
    },
    {
      "index": 3,
      "field": "causal_graphs[0].nodes[3]",
      "node": {
        "node_id": "low_temperature",
        "label": "low temperature",
        "node_type": "ENVIRONMENTAL_FACTOR",
        "description": "Ambient temperature at or below ~10 C imposing cold stress.",
        "grounding": "PATO:0001306"
      },
      "outcome": "qualified",
      "judgment": "Actual ambient low-temperature condition is compatible ENVIRONMENTAL_FACTOR. PATO1306 relatively-low temperature quality is a declared closeMatch condition shorthand, not an event merely because its label says decreased. Its use as an imported process-regulator subject is separately inconsistent."
    },
    {
      "index": 4,
      "field": "causal_graphs[0].nodes[4]",
      "node": {
        "node_id": "membrane_fatty_acid_desaturation",
        "label": "membrane fatty-acid desaturation",
        "node_type": "BIOLOGICAL_PROCESS",
        "description": "Introduction of double bonds into membrane lipids during cold adaptation."
      },
      "outcome": "positive",
      "judgment": "Introduction of double bonds is an explicit process; no enzyme improvement or biological efficacy judgment."
    },
    {
      "index": 5,
      "field": "causal_graphs[0].nodes[5]",
      "node": {
        "node_id": "membrane_fluidity",
        "label": "membrane fluidity",
        "node_type": "QUALITY",
        "description": "Physical fluidity of the membrane bilayer required for function in the cold.",
        "grounding": "METPO:1007505"
      },
      "outcome": "positive",
      "judgment": "Physical bilayer fluidity is QUALITY. Exact local v3 METPO1007505 identity and mapping50 are positive, absent from captured active upstream raw OWL."
    },
    {
      "index": 6,
      "field": "causal_graphs[0].nodes[6]",
      "node": {
        "node_id": "two_component_cold_signaling",
        "label": "two-component cold signaling",
        "node_type": "BIOLOGICAL_PROCESS",
        "description": "Two-component regulatory systems triggered by cold-induced membrane state changes."
      },
      "outcome": "qualified",
      "judgment": "Signaling label/type denotes a process, although description names regulatory systems. Process reading is plausible; detailed regulation/fitness efficacy unassessed, no forced material retype."
    },
    {
      "index": 7,
      "field": "causal_graphs[0].nodes[7]",
      "node": {
        "node_id": "cold_shock_proteins",
        "label": "cold-shock proteins (CspA-family)",
        "node_type": "GENE_OR_PROTEIN",
        "grounding_status": "REVIEWED_LABEL_ONLY",
        "grounding_notes": "Reviewed as a contextual protein or protein-complex label within a quantitative measurement graph; no exact semantic family term was established for this aggregate use.",
        "description": "CspA-family RNA chaperones that bind nucleic acids during cold acclimation."
      },
      "outcome": "positive",
      "judgment": "Explicit protein-family material, reviewed label-only with rationale. No required accession or instance; detailed RNA chaperoning efficacy unassessed."
    },
    {
      "index": 8,
      "field": "causal_graphs[0].nodes[8]",
      "node": {
        "node_id": "cold_stabilized_rna_secondary_structure",
        "label": "cold-stabilized mRNA/RNA secondary structure",
        "node_type": "QUALITY",
        "description": "Cold-stabilized RNA secondary structures impeding translation."
      },
      "outcome": "positive",
      "judgment": "Cold-stabilized RNA secondary structure is a quality of material RNA, not RNA as chemical substance. Current corrective node identity/type and history are coherent."
    },
    {
      "index": 9,
      "field": "causal_graphs[0].nodes[9]",
      "node": {
        "node_id": "molecular_chaperones",
        "label": "molecular chaperones (DnaK/GroEL/GroES/Clp/TF)",
        "node_type": "GENE_OR_PROTEIN",
        "grounding_status": "REVIEWED_LABEL_ONLY",
        "grounding_notes": "Reviewed as a contextual protein or protein-complex label within a quantitative measurement graph; no exact semantic family term was established for this aggregate use.",
        "description": "Chaperone and protease systems maintaining proteostasis under cold."
      },
      "outcome": "positive",
      "judgment": "Explicit material chaperone/protease systems, reviewed label-only; functional description does not itself force a process retype."
    },
    {
      "index": 10,
      "field": "causal_graphs[0].nodes[10]",
      "node": {
        "node_id": "proteostasis_cold",
        "label": "protein folding and proteostasis in the cold",
        "node_type": "BIOLOGICAL_PROCESS",
        "description": "Maintenance of correct protein folding despite cold-slowed folding kinetics."
      },
      "outcome": "positive",
      "judgment": "Folding and maintenance denote processes. Detailed cold proteostasis efficacy is outside review scope."
    },
    {
      "index": 11,
      "field": "causal_graphs[0].nodes[11]",
      "node": {
        "node_id": "compatible_solutes",
        "label": "compatible solutes (glycine betaine/trehalose/glycerol)",
        "node_type": "CHEMICAL",
        "description": "Osmolytes that lower freezing damage and stabilize macromolecules."
      },
      "outcome": "positive",
      "judgment": "Examples identify material compatible-solute chemicals. No populated CHEBI role grounding to misread as exact substance identity."
    },
    {
      "index": 12,
      "field": "causal_graphs[0].nodes[12]",
      "node": {
        "node_id": "protein_membrane_stabilization",
        "label": "protein and membrane stabilization",
        "node_type": "BIOLOGICAL_PROCESS",
        "description": "Stabilization of proteins and membranes against cold/freezing damage."
      },
      "outcome": "positive",
      "judgment": "Stabilization denotes processual activity; detailed cryoprotection or intervention support unassessed."
    },
    {
      "index": 13,
      "field": "causal_graphs[0].nodes[13]",
      "node": {
        "node_id": "ice_binding_proteins",
        "label": "ice-binding/antifreeze proteins",
        "node_type": "GENE_OR_PROTEIN",
        "grounding_status": "REVIEWED_LABEL_ONLY",
        "grounding_notes": "Reviewed as a contextual protein or protein-complex label within a quantitative measurement graph; no exact semantic family term was established for this aggregate use.",
        "description": "AFPs/IBPs that bind ice and inhibit ice-crystal growth."
      },
      "outcome": "positive",
      "judgment": "Explicit material ice-binding protein aggregate, reviewed label-only. No invented accession or efficacy claim."
    },
    {
      "index": 14,
      "field": "causal_graphs[0].nodes[14]",
      "node": {
        "node_id": "ice_crystal_growth",
        "label": "ice-crystal growth/recrystallization",
        "node_type": "BIOLOGICAL_PROCESS",
        "description": "Damaging ice-crystal growth and recrystallization around cells."
      },
      "outcome": "positive",
      "judgment": "Ice growth/recrystallization is a physical process compatible with imported BFO process range. BIOLOGICAL_PROCESS enum context does not independently establish a defect merely because the process is physical."
    }
  ],
  "source": [
    {
      "index": 0,
      "field": "causal_graphs[0].nodes[0]",
      "node": {
        "node_id": "temperature_range_very_low_trait",
        "label": "temperature range very low",
        "node_type": "TRAIT",
        "grounding": "METPO:1000448",
        "description": "Temperature growth-supporting range reaching ≤ ~10 °C."
      },
      "disposition": "PARTIAL",
      "scope": "Threshold interpretation consistent with canonical; boundary authority qualified."
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
      "disposition": "SUPPORTED",
      "scope": "Generic measured growth interval context."
    },
    {
      "index": 2,
      "field": "causal_graphs[0].nodes[2]",
      "node": {
        "node_id": "psychrophile_machinery",
        "label": "psychrophile cold-adapted machinery",
        "node_type": "BIOLOGICAL_PROCESS",
        "description": "Cold-active enzymes and unsaturated-lipid membranes that sustain function near freezing."
      },
      "disposition": "UNASSESSED_SCOPE",
      "scope": "Existing contextual label/description preserved; detailed molecular regulation/protection/fitness/survival efficacy unassessed."
    },
    {
      "index": 3,
      "field": "causal_graphs[0].nodes[3]",
      "node": {
        "node_id": "low_temperature",
        "label": "low temperature",
        "node_type": "ENVIRONMENTAL_FACTOR",
        "description": "Ambient temperature at or below ~10 C imposing cold stress.",
        "grounding": "PATO:0001306"
      },
      "disposition": "PARTIAL",
      "scope": "Generic low-temperature condition; exact10 calibration qualified."
    },
    {
      "index": 4,
      "field": "causal_graphs[0].nodes[4]",
      "node": {
        "node_id": "membrane_fatty_acid_desaturation",
        "label": "membrane fatty-acid desaturation",
        "node_type": "BIOLOGICAL_PROCESS",
        "description": "Introduction of double bonds into membrane lipids during cold adaptation."
      },
      "disposition": "PARTIAL",
      "scope": "Generic composition context only; detailed adaptation efficacy unassessed."
    },
    {
      "index": 5,
      "field": "causal_graphs[0].nodes[5]",
      "node": {
        "node_id": "membrane_fluidity",
        "label": "membrane fluidity",
        "node_type": "QUALITY",
        "description": "Physical fluidity of the membrane bilayer required for function in the cold.",
        "grounding": "METPO:1007505"
      },
      "disposition": "PARTIAL",
      "scope": "Generic membrane phase/fluidity context only; efficacy unassessed."
    },
    {
      "index": 6,
      "field": "causal_graphs[0].nodes[6]",
      "node": {
        "node_id": "two_component_cold_signaling",
        "label": "two-component cold signaling",
        "node_type": "BIOLOGICAL_PROCESS",
        "description": "Two-component regulatory systems triggered by cold-induced membrane state changes."
      },
      "disposition": "UNASSESSED_SCOPE",
      "scope": "Existing contextual label/description preserved; detailed molecular regulation/protection/fitness/survival efficacy unassessed."
    },
    {
      "index": 7,
      "field": "causal_graphs[0].nodes[7]",
      "node": {
        "node_id": "cold_shock_proteins",
        "label": "cold-shock proteins (CspA-family)",
        "node_type": "GENE_OR_PROTEIN",
        "grounding_status": "REVIEWED_LABEL_ONLY",
        "grounding_notes": "Reviewed as a contextual protein or protein-complex label within a quantitative measurement graph; no exact semantic family term was established for this aggregate use.",
        "description": "CspA-family RNA chaperones that bind nucleic acids during cold acclimation."
      },
      "disposition": "UNASSESSED_SCOPE",
      "scope": "Existing contextual label/description preserved; detailed molecular regulation/protection/fitness/survival efficacy unassessed."
    },
    {
      "index": 8,
      "field": "causal_graphs[0].nodes[8]",
      "node": {
        "node_id": "cold_stabilized_rna_secondary_structure",
        "label": "cold-stabilized mRNA/RNA secondary structure",
        "node_type": "QUALITY",
        "description": "Cold-stabilized RNA secondary structures impeding translation."
      },
      "disposition": "UNASSESSED_SCOPE",
      "scope": "Existing contextual label/description preserved; detailed molecular regulation/protection/fitness/survival efficacy unassessed."
    },
    {
      "index": 9,
      "field": "causal_graphs[0].nodes[9]",
      "node": {
        "node_id": "molecular_chaperones",
        "label": "molecular chaperones (DnaK/GroEL/GroES/Clp/TF)",
        "node_type": "GENE_OR_PROTEIN",
        "grounding_status": "REVIEWED_LABEL_ONLY",
        "grounding_notes": "Reviewed as a contextual protein or protein-complex label within a quantitative measurement graph; no exact semantic family term was established for this aggregate use.",
        "description": "Chaperone and protease systems maintaining proteostasis under cold."
      },
      "disposition": "UNASSESSED_SCOPE",
      "scope": "Existing contextual label/description preserved; detailed molecular regulation/protection/fitness/survival efficacy unassessed."
    },
    {
      "index": 10,
      "field": "causal_graphs[0].nodes[10]",
      "node": {
        "node_id": "proteostasis_cold",
        "label": "protein folding and proteostasis in the cold",
        "node_type": "BIOLOGICAL_PROCESS",
        "description": "Maintenance of correct protein folding despite cold-slowed folding kinetics."
      },
      "disposition": "UNASSESSED_SCOPE",
      "scope": "Existing contextual label/description preserved; detailed molecular regulation/protection/fitness/survival efficacy unassessed."
    },
    {
      "index": 11,
      "field": "causal_graphs[0].nodes[11]",
      "node": {
        "node_id": "compatible_solutes",
        "label": "compatible solutes (glycine betaine/trehalose/glycerol)",
        "node_type": "CHEMICAL",
        "description": "Osmolytes that lower freezing damage and stabilize macromolecules."
      },
      "disposition": "UNASSESSED_SCOPE",
      "scope": "Existing contextual label/description preserved; detailed molecular regulation/protection/fitness/survival efficacy unassessed."
    },
    {
      "index": 12,
      "field": "causal_graphs[0].nodes[12]",
      "node": {
        "node_id": "protein_membrane_stabilization",
        "label": "protein and membrane stabilization",
        "node_type": "BIOLOGICAL_PROCESS",
        "description": "Stabilization of proteins and membranes against cold/freezing damage."
      },
      "disposition": "UNASSESSED_SCOPE",
      "scope": "Existing contextual label/description preserved; detailed molecular regulation/protection/fitness/survival efficacy unassessed."
    },
    {
      "index": 13,
      "field": "causal_graphs[0].nodes[13]",
      "node": {
        "node_id": "ice_binding_proteins",
        "label": "ice-binding/antifreeze proteins",
        "node_type": "GENE_OR_PROTEIN",
        "grounding_status": "REVIEWED_LABEL_ONLY",
        "grounding_notes": "Reviewed as a contextual protein or protein-complex label within a quantitative measurement graph; no exact semantic family term was established for this aggregate use.",
        "description": "AFPs/IBPs that bind ice and inhibit ice-crystal growth."
      },
      "disposition": "UNASSESSED_SCOPE",
      "scope": "Existing contextual label/description preserved; detailed molecular regulation/protection/fitness/survival efficacy unassessed."
    },
    {
      "index": 14,
      "field": "causal_graphs[0].nodes[14]",
      "node": {
        "node_id": "ice_crystal_growth",
        "label": "ice-crystal growth/recrystallization",
        "node_type": "BIOLOGICAL_PROCESS",
        "description": "Damaging ice-crystal growth and recrystallization around cells."
      },
      "disposition": "UNASSESSED_SCOPE",
      "scope": "Existing contextual label/description preserved; detailed molecular regulation/protection/fitness/survival efficacy unassessed."
    }
  ]
}

### Native checklist: all fourteen current relations

consistency: concern. Targets: METPO:1000448.

One formal-role major covers edges 2/3/4/7: imported process regulation conflicts with quality, ambient-condition or material-protein endpoints. Edge 7 has a compatible physical process object. RO2326 material-to-process fit at edges 5/6 remains positive without efficacy endorsement. Broad local confers, exact subclass and Biolink association roles remain compatible or qualified; no statistical association or benefit is inferred. No biological replacement or intermediary is prescribed.

{
  "grounding": [
    {
      "index": 0,
      "field": "causal_graphs[0].edges[0]",
      "edge": {
        "subject": "psychrophile_machinery",
        "predicate": "confers",
        "object": "temperature_range_very_low_trait",
        "description": "Psychrophile cold-adapted machinery enables growth at ≤ 10 °C.",
        "evidence": [
          {
            "reference": "DOI:10.1038/sj.embor.7400662",
            "snippet": "decreased membrane fluidity",
            "notes": "Supports cold-adapted membranes and enzymes as enablers of growth at very low temperatures."
          }
        ],
        "predicate_id": "METPO:2007700"
      },
      "outcome": "qualified",
      "judgment": "Local v8 confers accepts broad causal-node endpoints and trait object. Mixed subject facet and detailed causal sufficiency remain qualified; no hard imported endpoint failure."
    },
    {
      "index": 1,
      "field": "causal_graphs[0].edges[1]",
      "edge": {
        "subject": "temperature_range_very_low_trait",
        "predicate": "is a",
        "object": "temperature_range",
        "description": "Temperature range very low is a quantitative bin of the temperature-range phenotype.",
        "evidence": [
          {
            "reference": "DOI:10.1038/sj.embor.7400662",
            "snippet": "growing well at temperatures around the freezing point of water",
            "notes": "Supports a ≤10 °C range as a value within the temperature-range distribution."
          }
        ],
        "predicate_id": "rdfs:subClassOf"
      },
      "outcome": "positive",
      "judgment": "rdfs:subClassOf agrees with current exact active raw child/direct-parent hierarchy."
    },
    {
      "index": 2,
      "field": "causal_graphs[0].edges[2]",
      "edge": {
        "subject": "membrane_fatty_acid_desaturation",
        "predicate": "increases",
        "object": "membrane_fluidity",
        "description": "Homeoviscous adaptation via lipid desaturation maintains membrane fluidity in the cold.",
        "evidence": [
          {
            "reference": "DOI:10.1007/s42770-023-01057-4",
            "snippet": "production of double bonds in lipids",
            "notes": "Verified against the open Ramón et al. PubMed abstract; the multifactorial cold-adaptation model lists membrane composition adaptation by producing lipid double bonds."
          }
        ],
        "predicate_id": "RO:0002213"
      },
      "outcome": "major",
      "judgment": "RO2213 inherits RO2211 process/process. Explicit desaturation process fits subject, but membrane-fluidity QUALITY fails process range."
    },
    {
      "index": 3,
      "field": "causal_graphs[0].edges[3]",
      "edge": {
        "subject": "low_temperature",
        "predicate": "activates",
        "object": "two_component_cold_signaling",
        "description": "Cold-induced membrane state changes activate two-component cold signaling.",
        "evidence": [
          {
            "reference": "DOI:10.1007/s42770-023-01057-4",
            "snippet": "activation of a two-component system",
            "notes": "Verified against the open Ramón et al. PubMed abstract; cold sensing is described as occurring mainly through liquid-crystalline membrane-state changes that activate a two-component signal-transduction system."
          }
        ],
        "predicate_id": "RO:0002213"
      },
      "outcome": "major",
      "judgment": "RO2213 requires process/process. Current subject explicitly denotes an ambient low-temperature condition, not a temperature-drop event; object signaling process is compatible. Finding follows actual referent and PATO quality context, not the ENV enum alone."
    },
    {
      "index": 4,
      "field": "causal_graphs[0].edges[4]",
      "edge": {
        "subject": "cold_shock_proteins",
        "predicate": "regulates",
        "object": "cold_stabilized_rna_secondary_structure",
        "description": "CspA-family RNA chaperones regulate cold-stabilized RNA structures to sustain translation.",
        "evidence": [
          {
            "reference": "DOI:10.4161/rna.7.6.13482",
            "snippet": "through their RNA chaperoning function",
            "notes": "Verified against the open Phadtare and Severinov PubMed abstract; CspA-family cold-shock proteins are described as RNA-modulating proteins affecting low-temperature transcription and possibly translation through RNA chaperoning."
          }
        ],
        "predicate_id": "RO:0002211"
      },
      "outcome": "major",
      "judgment": "RO2211 process/process conflicts with explicit material protein subject and RNA secondary-structure QUALITY object. No biological mechanism repair proposed."
    },
    {
      "index": 5,
      "field": "causal_graphs[0].edges[5]",
      "edge": {
        "subject": "molecular_chaperones",
        "predicate": "contributes to",
        "object": "proteostasis_cold",
        "description": "Chaperone/protease systems contribute to proteostasis by countering cold-slowed folding and misfolding risk.",
        "evidence": [
          {
            "reference": "DOI:10.3389/fmicb.2023.1197797",
            "snippet": "heat shock proteins associated to folding",
            "notes": "Verified against the open Ramasamy et al. PMC text; the Antarctic psychrophile review discusses heat-shock proteins associated with protein folding in 4 °C versus 18 °C Pseudoalteromonas haloplanktis TAC125."
          }
        ],
        "predicate_id": "RO:0002326"
      },
      "outcome": "qualified",
      "judgment": "RO2326 through2216/2500/2595 has material domain/process range. Protein-system material to proteostasis process fits formal endpoints; detailed participation/function and efficacy remain unassessed. GO-specific molecular-function annotation guidance is not imposed as a universal range."
    },
    {
      "index": 6,
      "field": "causal_graphs[0].edges[6]",
      "edge": {
        "subject": "compatible_solutes",
        "predicate": "contributes to",
        "object": "protein_membrane_stabilization",
        "description": "Osmolytes contribute to protein and membrane stabilization while lowering freezing damage.",
        "evidence": [
          {
            "reference": "DOI:10.3389/fmicb.2023.1197797",
            "snippet": "counteracting protein aggregation, improving protein folding",
            "notes": "Verified against the open Ramasamy et al. PMC text; Antarctic compatible osmolytes are described as counteracting protein aggregation and improving protein folding."
          }
        ],
        "predicate_id": "RO:0002326"
      },
      "outcome": "qualified",
      "judgment": "RO2326 material-to-process endpoints fit explicit solute chemicals and stabilization activity. Formal fit is not an efficacy or intervention endorsement."
    },
    {
      "index": 7,
      "field": "causal_graphs[0].edges[7]",
      "edge": {
        "subject": "ice_binding_proteins",
        "predicate": "inhibits",
        "object": "ice_crystal_growth",
        "description": "AFPs/IBPs bind ice and inhibit ice-crystal growth and recrystallization.",
        "evidence": [
          {
            "reference": "DOI:10.3389/fmicb.2023.1197797",
            "snippet": "inhibits the growth of ice crystals",
            "notes": "Verified against the open Ramasamy et al. PMC text; ice binding proteins are described as antifreeze proteins that bind ice, inhibit ice-crystal growth, lower freezing temperature, create a thermal hysteresis gap, and display ice-recrystallization inhibition activity."
          }
        ],
        "predicate_id": "RO:0002212"
      },
      "outcome": "major",
      "judgment": "RO2212 inherits process/process fromRO2211. Ice-binding proteins are material subjects; physical ice growth is process-compatible object. No object fault inferred solely from physical-process context."
    },
    {
      "index": 8,
      "field": "causal_graphs[0].edges[8]",
      "edge": {
        "subject": "membrane_fluidity",
        "predicate": "associated with",
        "object": "psychrophile_machinery",
        "description": "Membrane fatty-acid desaturation is associated with the cold-adapted machinery supporting psychrophile growth ranges.",
        "evidence": [
          {
            "reference": "DOI:10.1007/s42770-023-01057-4",
            "snippet": "maintain the liquid crystalline phase",
            "notes": "Verified against the open Ramón et al. PubMed abstract; this connector keeps membrane desaturation as cold membrane-adaptation context."
          }
        ],
        "predicate_id": "biolink:associated_with"
      },
      "outcome": "qualified",
      "judgment": "Biolink associated_with has broad named-thing endpoints and admits related proxy entities. Current quality source versus desaturation-process description is retained as a scope/precision qualification; no automatic RO domain import or separate forced mechanism finding."
    },
    {
      "index": 9,
      "field": "causal_graphs[0].edges[9]",
      "edge": {
        "subject": "two_component_cold_signaling",
        "predicate": "associated with",
        "object": "psychrophile_machinery",
        "description": "Two-component cold signaling is associated with psychrophile cold-adapted machinery.",
        "evidence": [
          {
            "reference": "DOI:10.1007/s42770-023-01057-4",
            "snippet": "When the temperature drops, DesK/DesR is the two-component system involved in membrane adaptation",
            "notes": "Verified against the open Ramón et al. PubMed abstract; this connector keeps low-temperature membrane sensing as cold-acclimation context."
          }
        ],
        "predicate_id": "biolink:associated_with"
      },
      "outcome": "qualified",
      "judgment": "Broad Biolink association allows signaling-process/context relation; detailed cold-regulation efficacy unassessed."
    },
    {
      "index": 10,
      "field": "causal_graphs[0].edges[10]",
      "edge": {
        "subject": "cold_stabilized_rna_secondary_structure",
        "predicate": "associated with",
        "object": "psychrophile_machinery",
        "description": "CspA-family regulation of cold-stabilized RNA structure is associated with psychrophile cold-adapted machinery.",
        "evidence": [
          {
            "reference": "DOI:10.4161/rna.7.6.13482",
            "snippet": "CspA, the main cold shock protein, and its homologs act as RNA chaperones",
            "notes": "Verified against the open Phadtare and Severinov PubMed abstract; this connector keeps CspA-family RNA chaperones as low-temperature transcript context."
          }
        ],
        "predicate_id": "biolink:associated_with"
      },
      "outcome": "qualified",
      "judgment": "Broad Biolink association permits the structural-quality proxy in contextual relation. Description references the regulating process rather than asserting a new exact material identity; keep scope qualified without imported process-domain claim."
    },
    {
      "index": 11,
      "field": "causal_graphs[0].edges[11]",
      "edge": {
        "subject": "proteostasis_cold",
        "predicate": "associated with",
        "object": "psychrophile_machinery",
        "description": "Cold proteostasis support is associated with the psychrophile machinery context.",
        "evidence": [
          {
            "reference": "DOI:10.3389/fmicb.2023.1197797",
            "snippet": "ice binding, cold shock and heat shock proteins to sustain their physiological state",
            "notes": "Verified against the open Ramasamy et al. PMC text; this connector keeps chaperone/protease systems as protein-folding context."
          }
        ],
        "predicate_id": "biolink:associated_with"
      },
      "outcome": "qualified",
      "judgment": "Broad Biolink association fits process/context endpoints; detailed efficacy and statistical dependence are not newly established."
    },
    {
      "index": 12,
      "field": "causal_graphs[0].edges[12]",
      "edge": {
        "subject": "protein_membrane_stabilization",
        "predicate": "associated with",
        "object": "psychrophile_machinery",
        "description": "Compatible-solute stabilization is associated with psychrophile cold-adapted machinery.",
        "evidence": [
          {
            "reference": "DOI:10.3389/fmicb.2023.1197797",
            "snippet": "scavenging free radicals, counteracting protein aggregation",
            "notes": "Verified against the open Ramasamy et al. PMC text; this connector keeps compatible osmolytes as stabilization context."
          }
        ],
        "predicate_id": "biolink:associated_with"
      },
      "outcome": "qualified",
      "judgment": "Broad Biolink association fits stabilization-process/context endpoints; detailed biological support unassessed."
    },
    {
      "index": 13,
      "field": "causal_graphs[0].edges[13]",
      "edge": {
        "subject": "ice_crystal_growth",
        "predicate": "associated with",
        "object": "psychrophile_machinery",
        "description": "Ice-binding protein inhibition of ice-crystal growth is associated with psychrophile cold-adapted machinery.",
        "evidence": [
          {
            "reference": "DOI:10.3389/fmicb.2023.1197797",
            "snippet": "This ceases ice growth by creating a thermal hysteresis gap",
            "notes": "Verified against the open Ramasamy et al. PMC text; this connector keeps ice-binding proteins as freezing-protection context."
          }
        ],
        "predicate_id": "biolink:associated_with"
      },
      "outcome": "qualified",
      "judgment": "Broad Biolink association admits physical process/context proxies; description attributes protein-mediated context, with no new efficacy endorsement or imported RO exclusion."
    }
  ],
  "source": [
    {
      "index": 0,
      "field": "causal_graphs[0].edges[0]",
      "edge": {
        "subject": "psychrophile_machinery",
        "predicate": "confers",
        "object": "temperature_range_very_low_trait",
        "description": "Psychrophile cold-adapted machinery enables growth at ≤ 10 °C.",
        "evidence": [
          {
            "reference": "DOI:10.1038/sj.embor.7400662",
            "snippet": "decreased membrane fluidity",
            "notes": "Supports cold-adapted membranes and enzymes as enablers of growth at very low temperatures."
          }
        ],
        "predicate_id": "METPO:2007700"
      },
      "disposition": "PARTIAL",
      "scope": "Generic cold membrane-fluidity context positive; whole-machinery efficacy at exact threshold UNASSESSED_SCOPE."
    },
    {
      "index": 1,
      "field": "causal_graphs[0].edges[1]",
      "edge": {
        "subject": "temperature_range_very_low_trait",
        "predicate": "is a",
        "object": "temperature_range",
        "description": "Temperature range very low is a quantitative bin of the temperature-range phenotype.",
        "evidence": [
          {
            "reference": "DOI:10.1038/sj.embor.7400662",
            "snippet": "growing well at temperatures around the freezing point of water",
            "notes": "Supports a ≤10 °C range as a value within the temperature-range distribution."
          }
        ],
        "predicate_id": "rdfs:subClassOf"
      },
      "disposition": "PARTIAL",
      "scope": "Broad near-freezing classification positive; exact10 cutoff not calibrated by selected passage alone."
    },
    {
      "index": 2,
      "field": "causal_graphs[0].edges[2]",
      "edge": {
        "subject": "membrane_fatty_acid_desaturation",
        "predicate": "increases",
        "object": "membrane_fluidity",
        "description": "Homeoviscous adaptation via lipid desaturation maintains membrane fluidity in the cold.",
        "evidence": [
          {
            "reference": "DOI:10.1007/s42770-023-01057-4",
            "snippet": "production of double bonds in lipids",
            "notes": "Verified against the open Ramón et al. PubMed abstract; the multifactorial cold-adaptation model lists membrane composition adaptation by producing lipid double bonds."
          }
        ],
        "predicate_id": "RO:0002213"
      },
      "disposition": "PARTIAL",
      "scope": "Generic lipid composition context and phrase positive; detailed regulation/efficacy unassessed."
    },
    {
      "index": 3,
      "field": "causal_graphs[0].edges[3]",
      "edge": {
        "subject": "low_temperature",
        "predicate": "activates",
        "object": "two_component_cold_signaling",
        "description": "Cold-induced membrane state changes activate two-component cold signaling.",
        "evidence": [
          {
            "reference": "DOI:10.1007/s42770-023-01057-4",
            "snippet": "activation of a two-component system",
            "notes": "Verified against the open Ramón et al. PubMed abstract; cold sensing is described as occurring mainly through liquid-crystalline membrane-state changes that activate a two-component signal-transduction system."
          }
        ],
        "predicate_id": "RO:0002213"
      },
      "disposition": "UNASSESSED_SCOPE",
      "scope": "Literal phrase only; detailed cold-sensing activation unassessed."
    },
    {
      "index": 4,
      "field": "causal_graphs[0].edges[4]",
      "edge": {
        "subject": "cold_shock_proteins",
        "predicate": "regulates",
        "object": "cold_stabilized_rna_secondary_structure",
        "description": "CspA-family RNA chaperones regulate cold-stabilized RNA structures to sustain translation.",
        "evidence": [
          {
            "reference": "DOI:10.4161/rna.7.6.13482",
            "snippet": "through their RNA chaperoning function",
            "notes": "Verified against the open Phadtare and Severinov PubMed abstract; CspA-family cold-shock proteins are described as RNA-modulating proteins affecting low-temperature transcription and possibly translation through RNA chaperoning."
          }
        ],
        "predicate_id": "RO:0002211"
      },
      "disposition": "UNASSESSED_SCOPE",
      "scope": "Literal phrase only; detailed RNA/translation efficacy unassessed."
    },
    {
      "index": 5,
      "field": "causal_graphs[0].edges[5]",
      "edge": {
        "subject": "molecular_chaperones",
        "predicate": "contributes to",
        "object": "proteostasis_cold",
        "description": "Chaperone/protease systems contribute to proteostasis by countering cold-slowed folding and misfolding risk.",
        "evidence": [
          {
            "reference": "DOI:10.3389/fmicb.2023.1197797",
            "snippet": "heat shock proteins associated to folding",
            "notes": "Verified against the open Ramasamy et al. PMC text; the Antarctic psychrophile review discusses heat-shock proteins associated with protein folding in 4 °C versus 18 °C Pseudoalteromonas haloplanktis TAC125."
          }
        ],
        "predicate_id": "RO:0002326"
      },
      "disposition": "UNASSESSED_SCOPE",
      "scope": "Literal phrase only; numerical strain-specific proteostasis comparison unassessed."
    },
    {
      "index": 6,
      "field": "causal_graphs[0].edges[6]",
      "edge": {
        "subject": "compatible_solutes",
        "predicate": "contributes to",
        "object": "protein_membrane_stabilization",
        "description": "Osmolytes contribute to protein and membrane stabilization while lowering freezing damage.",
        "evidence": [
          {
            "reference": "DOI:10.3389/fmicb.2023.1197797",
            "snippet": "counteracting protein aggregation, improving protein folding",
            "notes": "Verified against the open Ramasamy et al. PMC text; Antarctic compatible osmolytes are described as counteracting protein aggregation and improving protein folding."
          }
        ],
        "predicate_id": "RO:0002326"
      },
      "disposition": "UNASSESSED_SCOPE",
      "scope": "Literal phrase only; detailed osmolyte protection/folding efficacy unassessed."
    },
    {
      "index": 7,
      "field": "causal_graphs[0].edges[7]",
      "edge": {
        "subject": "ice_binding_proteins",
        "predicate": "inhibits",
        "object": "ice_crystal_growth",
        "description": "AFPs/IBPs bind ice and inhibit ice-crystal growth and recrystallization.",
        "evidence": [
          {
            "reference": "DOI:10.3389/fmicb.2023.1197797",
            "snippet": "inhibits the growth of ice crystals",
            "notes": "Verified against the open Ramasamy et al. PMC text; ice binding proteins are described as antifreeze proteins that bind ice, inhibit ice-crystal growth, lower freezing temperature, create a thermal hysteresis gap, and display ice-recrystallization inhibition activity."
          }
        ],
        "predicate_id": "RO:0002212"
      },
      "disposition": "UNASSESSED_SCOPE",
      "scope": "Literal phrase only; ice-binding/protection efficacy unassessed."
    },
    {
      "index": 8,
      "field": "causal_graphs[0].edges[8]",
      "edge": {
        "subject": "membrane_fluidity",
        "predicate": "associated with",
        "object": "psychrophile_machinery",
        "description": "Membrane fatty-acid desaturation is associated with the cold-adapted machinery supporting psychrophile growth ranges.",
        "evidence": [
          {
            "reference": "DOI:10.1007/s42770-023-01057-4",
            "snippet": "maintain the liquid crystalline phase",
            "notes": "Verified against the open Ramón et al. PubMed abstract; this connector keeps membrane desaturation as cold membrane-adaptation context."
          }
        ],
        "predicate_id": "biolink:associated_with"
      },
      "disposition": "PARTIAL",
      "scope": "Generic membrane phase context and body phrase positive; note incorrectly says abstract."
    },
    {
      "index": 9,
      "field": "causal_graphs[0].edges[9]",
      "edge": {
        "subject": "two_component_cold_signaling",
        "predicate": "associated with",
        "object": "psychrophile_machinery",
        "description": "Two-component cold signaling is associated with psychrophile cold-adapted machinery.",
        "evidence": [
          {
            "reference": "DOI:10.1007/s42770-023-01057-4",
            "snippet": "When the temperature drops, DesK/DesR is the two-component system involved in membrane adaptation",
            "notes": "Verified against the open Ramón et al. PubMed abstract; this connector keeps low-temperature membrane sensing as cold-acclimation context."
          }
        ],
        "predicate_id": "biolink:associated_with"
      },
      "disposition": "UNASSESSED_SCOPE",
      "scope": "Body phrase positive; note incorrectly says abstract; regulation efficacy unassessed."
    },
    {
      "index": 10,
      "field": "causal_graphs[0].edges[10]",
      "edge": {
        "subject": "cold_stabilized_rna_secondary_structure",
        "predicate": "associated with",
        "object": "psychrophile_machinery",
        "description": "CspA-family regulation of cold-stabilized RNA structure is associated with psychrophile cold-adapted machinery.",
        "evidence": [
          {
            "reference": "DOI:10.4161/rna.7.6.13482",
            "snippet": "CspA, the main cold shock protein, and its homologs act as RNA chaperones",
            "notes": "Verified against the open Phadtare and Severinov PubMed abstract; this connector keeps CspA-family RNA chaperones as low-temperature transcript context."
          }
        ],
        "predicate_id": "biolink:associated_with"
      },
      "disposition": "UNASSESSED_SCOPE",
      "scope": "Body phrase positive; note incorrectly says abstract; RNA efficacy unassessed."
    },
    {
      "index": 11,
      "field": "causal_graphs[0].edges[11]",
      "edge": {
        "subject": "proteostasis_cold",
        "predicate": "associated with",
        "object": "psychrophile_machinery",
        "description": "Cold proteostasis support is associated with the psychrophile machinery context.",
        "evidence": [
          {
            "reference": "DOI:10.3389/fmicb.2023.1197797",
            "snippet": "ice binding, cold shock and heat shock proteins to sustain their physiological state",
            "notes": "Verified against the open Ramasamy et al. PMC text; this connector keeps chaperone/protease systems as protein-folding context."
          }
        ],
        "predicate_id": "biolink:associated_with"
      },
      "disposition": "UNASSESSED_SCOPE",
      "scope": "Literal phrase only; proteostasis/fitness benefit unassessed."
    },
    {
      "index": 12,
      "field": "causal_graphs[0].edges[12]",
      "edge": {
        "subject": "protein_membrane_stabilization",
        "predicate": "associated with",
        "object": "psychrophile_machinery",
        "description": "Compatible-solute stabilization is associated with psychrophile cold-adapted machinery.",
        "evidence": [
          {
            "reference": "DOI:10.3389/fmicb.2023.1197797",
            "snippet": "scavenging free radicals, counteracting protein aggregation",
            "notes": "Verified against the open Ramasamy et al. PMC text; this connector keeps compatible osmolytes as stabilization context."
          }
        ],
        "predicate_id": "biolink:associated_with"
      },
      "disposition": "UNASSESSED_SCOPE",
      "scope": "Literal phrase only; stabilization/ROS-defense efficacy unassessed."
    },
    {
      "index": 13,
      "field": "causal_graphs[0].edges[13]",
      "edge": {
        "subject": "ice_crystal_growth",
        "predicate": "associated with",
        "object": "psychrophile_machinery",
        "description": "Ice-binding protein inhibition of ice-crystal growth is associated with psychrophile cold-adapted machinery.",
        "evidence": [
          {
            "reference": "DOI:10.3389/fmicb.2023.1197797",
            "snippet": "This ceases ice growth by creating a thermal hysteresis gap",
            "notes": "Verified against the open Ramasamy et al. PMC text; this connector keeps ice-binding proteins as freezing-protection context."
          }
        ],
        "predicate_id": "biolink:associated_with"
      },
      "disposition": "UNASSESSED_SCOPE",
      "scope": "Literal phrase only; protection efficacy unassessed."
    }
  ]
}

### Native checklist: exact templates and distinct guarded consumers

ownership: supported. Targets: METPO:1000448.

Six review after-edges and one node match current content. All six connector source guards/additions and AFTER metadata match; ordinary review and connector replay therefore no-op. PR664 consumes review after-payloads and six unfiltered additions and can replace populated matched triples. The exact three locator notes belong to connector ADDED_EDGES, with PR664 as consumer. Generic grounder skips populated IDs; rows 11/58/64/65 are conditional recurrence inputs. Machinery facet is record-only; no faulty producer demonstrated.

### Native checklist: bounded human acceptance link

provenance: concern. Targets: METPO:1000448.

Twelve embedded events comprise eleven AI-assisted entries and a seed. All 22 current captured actor projections are AI; whole readings are exact qualified prior readings with no fresh whole-history claim. Ignored- and hidden-inclusive search excluding .git/.venv internals found 196 matching paths and 71 matching arrays; all 96 actual local top-level target arrays have zero exact match. Private or remote acceptance remains unknown.

### Native checklist: retained catalog and bounded adapter availability

completeness: unknown. Targets: METPO:1000448.

The retained 20-organism/28-dataset catalog has no exact Psychromonas/P. ingrahamii or Pseudoalteromonas/P. haloplanktis entry under the bounded name searches. This is not an exhaustive source-organism inventory or global absence claim. No maintained adapter was found within current project/install/PATH scope, so no module query or efficacy result is asserted.

### Native checklist: NONMECHANISTIC context and optional instances

completeness: supported. Targets: METPO:1000448.

One connected component, fifteen nodes, fourteen edges, three reviewed label-only aggregates and zero instances are permissible current NONMECHANISTIC context. No extra connector, accession or dataset is required to fill optional structure. These positives do not resolve the four formal assertions, machinery facet, source locators or human acceptance link.

### Native checklist: current native checks and qualified B14 diagnostics

schema: supported. Targets: METPO:1000448.

Current inspect, target validation, strict validation and snippet checks are successful B15 executions. Four original B14 common diagnostics are qualified for unchanged B15 inputs, not relabeled fresh B15 executions. Original intervals, historical attempts, product skips and omitted full just test retain their scope. These eight command checks do not establish scientific correctness or human acceptance.

## Findings

### imported-process-roles: Imported process roles

major / open / confirmed; issue key: temperature-range-very-low-imported-process-roles.

RO:0002213 at edge2 has a quality object; at edge3 it has an ambient-condition subject. RO:0002211 at edge4 connects a material protein to an RNA-structure quality. RO:0002212 at edge7 has a material protein subject; its physical ice-growth process object is compatible. These predicates inherit process-to-process requirements. Judgments follow actual referents, not node enums alone. All six review after-edges and one after-node match current content. All six connector source guards and six additions also match; current AFTER metadata and one component make both ordinary writers static no-ops. PR664 consumes review replacements and six unfiltered connector additions and can replace populated matched triples. The generic grounder skips populated IDs; regulates/inhibits/activates/increases mapping rows11/58/64/65 remain conditional recurrence inputs. Coordinate these distinct owners and effective roles without inventing biological steps.

### machinery-facet: Machinery facet

minor / open / confirmed; issue key: temperature-range-very-low-machinery-facet.

The machinery node is typed BIOLOGICAL_PROCESS while its description names material cold-active enzymes and unsaturated-lipid membranes. The functional clause about sustaining function leaves its intended facet unclear. Clarify what this node represents; the evidence does not prescribe a replacement enum or added mechanism. No exact faulty producer of these two fields was established.

### source-surface-location: Source surface location

minor / open / confirmed; issue key: temperature-range-very-low-source-surface-location.

Three notes say the quotations were verified in PubMed abstracts. Each exact span is absent from the retained indexed and PMC abstracts but present in article-body text: Ramon all-HTML paragraph17/Par10/Sec3 for edge8, paragraph31/Par20/Sec7 for edge9, and Phadtare paragraph11/sec2 for edge10. All15 supplied snippets remain literal; this is a source-surface correction, not a false-quotation or efficacy finding. The connector stores the exact three note payloads in ADDED_EDGES; its ordinary replay is a no-op. PR664 is a replacement consumer of that payload, not an independent source authority.

### human-acceptance-link: Human acceptance link

minor / open / confirmed; issue key: temperature-range-very-low-human-acceptance-link.

REVIEWED status has no retrievable exact-target human acceptance in the bounded local evidence. The12 embedded events comprise11 AI-assisted entries and the METPO seed. All22 captured histories have AI actor projections; their whole readings are exact qualified prior readings. Ignored- and hidden-inclusive discovery excluding .git/.venv internals found196 matching paths and71 matching review arrays; all96 actual local top-level target arrays contain zero exact target matches. Private or remote acceptance remains unknown.

## Recommended Actions And Acceptance Checks

### curate-imported-process-roles

Resolve the four imported assertions against declared referents and coordinate exact templates, replacement consumers and conditional mapping recurrence.

- Document each affected endpoint and effective inherited domain/range; preserve material, quality, ambient-condition and process distinctions.
- Coordinate review EDGE_REPLACEMENTS, connector source guards/additions and PR664 matched-triple replacement. Both ordinary writers currently no-op; PR664 has six unfiltered additions, unlike earlier temperature records.
- Address regulates row11, inhibits row58, activates row64 and increases row65 for future empty fields; use explicit guarded curation for populated IDs.
- Use meaningful focused grounding/guard checks, strict validation and applicable QC/products. No operational mechanism repair or efficacy improvement is prescribed.

### curate-machinery-facet

Clarify the machinery node referent and align its type and description in separately authorized curation.

- Distinguish the material apparatus from an actual process without assuming a replacement enum or new intermediary.
- Keep broad confers-role compatibility separate from the unresolved node facet and biological efficacy.
- Use guarded record/history curation and applicable validation/products. No unsupported producer attribution.

### curate-source-surface-location

Correct the three body locators and coordinate the exact connector note payload and its PR664 consumer.

- Use body paragraph/section locators from the retained source surfaces rather than PubMed-abstract attribution.
- Preserve all15 literal quotations and their source identities; distinguish manual literal matching from native four VERIFIED and11 inconclusive NOT_IN_ABSTRACT results.
- Preserve causal uncertainty and validate guarded record/history/template changes without treating occurrence as proof of biological efficacy.

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
| check-temperature-range-very-low-target-validate | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-target-validate.log; Executed 2026-10-22T04:55:26.923104+00:00 through 2026-10-22T04:55:27.702377+00:00; metadata temperature-range-very-low-target-validate.json | context_only | Native validation passed; scientific interpretation is assessed separately. |
| check-temperature-range-very-low-target-strict | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-target-strict.log; Executed 2026-10-22T04:55:26.923143+00:00 through 2026-10-22T04:55:28.104669+00:00; metadata temperature-range-very-low-target-strict.json | context_only | The actual validate-strict command passed. |
| check-temperature-range-very-low-snippets-network | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-snippets-network.log; Executed 2026-10-22T04:55:38.779914+00:00 through 2026-10-22T04:55:45.530740+00:00; metadata temperature-range-very-low-snippets-network.json | context_only | Native command succeeded for fifteen snippets: four VERIFIED and eleven NOT_IN_ABSTRACT, the latter inconclusive. Manual matching supports all fifteen literal spans; three notes misidentify their source surface. |
| capture | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low.inspect.json; Actual successful native inspect with 101 captured inputs | context_only | All current captured source hashes and exact target are bound before serialization. |
| record | data/traits/environment/temperature_range_very_low.yaml; Whole current record | supports | Fifteen nodes, fourteen edges, twelve embedded events, one canonical example, three reviewed label-only protein aggregates and zero instances. |
| local-init | /private/tmp/traitmech-record-sweep-015.67f2ce7a/batch015-local-initialization-receipt.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Actual local initialization and fifth queue target; publication remains separate. |
| policy | docs/GROUNDING_POLICY.md; Captured maintained authority | supports | Protein family/function grounding, reviewed label-only aggregates and optional instances. |
| playbook | docs/CURATION_PLAYBOOK.md; Captured maintained authority | supports | Source attribution and attributable acceptance. |
| schema | src/traitmech/schema/traitmech.yaml; Captured maintained authority | supports | Current material, process, quality, environmental condition and quantitative NONMECHANISTIC facets. |
| predicate-mapping | mappings/predicate_grounding.tsv; Captured maintained authority | supports | Wildcard rows 11/58/64/65 are conditional future empty-field recurrence inputs; generic grounder skips populated identifiers. |
| canonical-writer | scripts/backfill_canonical_examples_444.py; Captured maintained authority | supports | Exact Psychromonas threshold note matches current SOURCES/TRANCHE; equality/no-op, nonempty rejection and global queue guards are positive context, not a faulty quantity producer. |
| identity | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-grounding-agent/identity-and-hierarchy.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Active target/direct parent and inclusive threshold restriction; exact boundary calibration and biological alias equivalence remain qualified. |
| nodes-edges | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-grounding-agent/node-edge-grounding-ledger.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | All fifteen referents and fourteen formal relation dispositions. |
| owners | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-grounding-agent/ownership-assessment.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Exact review, connector and PR664 roles; record-only machinery facet and conditional mapping recurrence. |
| owner-primary | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-grounding-agent/owner-primary-reading.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Selected current owner windows and qualified prior context; no writer execution. |
| local-authority | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-grounding-agent/local-authority-reading.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Actual schema, policy, local proposals and mapping scope. |
| histories | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-grounding-agent/history-reading-provenance.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Twenty-two current actor projections and exact qualified prior whole readings; no fresh whole-history claim. |
| embedded-history | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-grounding-agent/embedded-history-ledger.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Twelve embedded events: eleven AI-assisted events and one seed. |
| human-search | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-grounding-agent/search-and-provenance.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Ignored- and hidden-inclusive search: 196 matching paths, 71 matching arrays and 96 all-local arrays, zero exact target. |
| discovery | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-grounding-agent/discovery-dispositions.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Uncaptured leads remain matching-line context; private or remote acceptance unknown. |
| expression | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-grounding-agent/expression-and-readiness.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | One connected NONMECHANISTIC graph and three label-only aggregates are permissible; retained catalog and bounded runner availability do not establish efficacy. |
| expression-discovery | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-grounding-agent/adapter-discovery.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Bounded current maintained-runner discovery found no available adapter; no module query executed. |
| catalog-reuse | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-grounding-agent/catalog-reuse.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Original catalog acquisition remains distinct from current copying and selected-name reading. |
| ground-reading | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-grounding-agent/reading-scope-receipt.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Actual current reading scopes, qualified prior histories and owner distinctions. |
| ground-assessment | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-grounding-agent/grounding-assessment.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | One imported-role major, machinery-facet minor and bounded human provenance minor. |
| ground-manifest | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-grounding-agent/evidence-manifest.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | All 27 immutable ground artifacts verified. |
| writer-payloads | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-grounding-agent/writer-payload-comparison.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Six review after-edges and one node match; six connector guards/additions and AFTER metadata match. Both ordinary writers no-op; PR664 consumes six unfiltered additions. Static comparison only. |
| verification-support | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-grounding-agent/root-verification-support.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Bounded current verification of actual source/ground shapes, current inputs, original clocks and native receipts; no native or scientific reexecution. |
| ontology-primary | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-source-root/selected-ontology-primary.json; Exact selected response; query 2026-10-22T04:56:09.781703+00:00 through 2026-10-22T04:56:09.787919+00:00 | supports | Current selected RO/BFO/PATO, raw METPO, local proposals and Biolink authority. Query clocks differ from copy/read clocks. Ground auditor did not repeat queries or database hashing; serializer common guard separately verifies qualified inputs. |
| authority-primary | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-source-root/selected-authority-primary.json; Exact selected response; query 2026-10-22T04:56:09.788363+00:00 through 2026-10-22T04:56:10.010739+00:00 | supports | Current selected RO/BFO/PATO, raw METPO, local proposals and Biolink authority. Query clocks differ from copy/read clocks. Ground auditor did not repeat queries or database hashing; serializer common guard separately verifies qualified inputs. |
| authority-provenance | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-grounding-agent/primary-reuse-provenance.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Exact current root query clocks and ground-auditor copies, with separate reading completion. |
| catalog-original | https://imodulondb.org/api/datasets; Original retained 20-organism/28-dataset catalog | context_only | No exact Psychromonas or Pseudoalteromonas entry under the bounded name searches; not an exhaustive source-organism inventory or global absence finding. No module or efficacy result. |
| damico-metadata | DOI:10.1038/sj.embor.7400662; Indexed identity and selected generic classification context | supports | Identity and existing near-freezing classification positive; exact threshold calibration and biological alias equivalence remain qualified. |
| damico-pdf | DOI:10.1038/sj.embor.7400662; Original author-repository PDF; selected generic classification and supplied physical fragment | supports | Original acquisition retained; derived text and extraction time are separate. No whole-paper efficacy review. |
| cold-metadata | DOI:10.1007/s42770-023-01057-4; Indexed identity and supplied-span matching | supports | Identity and literal abstract spans only; detailed signaling, defense, survival and fitness efficacy unassessed. |
| cold-body | DOI:10.1007/s42770-023-01057-4; Zero-based all-HTML paragraphs 17/Par10/Sec3 and 31/Par20/Sec7 | supports | Two supplied connector spans occur in body text, not inspected indexed or PMC abstracts; surrounding regulatory efficacy is unassessed. |
| antarctic-metadata | DOI:10.3389/fmicb.2023.1197797; Indexed identity and historical notice fields | supports | Identity only; no current exhaustive notice or detailed efficacy assessment. |
| antarctic-body | DOI:10.3389/fmicb.2023.1197797; Zero-based body paragraphs 8/9: six supplied-fragment matches only | supports | Existing snippets literal; surrounding numerical-strain comparisons, stress defense, cryoprotection and intervention efficacy unassessed. |
| phadtare-metadata | DOI:10.4161/rna.7.6.13482; Indexed identity, supplied spans and selected physical RNA-structure sentence | supports | Generic physical context and literal occurrence only; no detailed regulatory, translation or efficacy conclusion. |
| phadtare-body | DOI:10.4161/rna.7.6.13482; Zero-based all-HTML paragraph 11/sec2 | supports | Existing connector span occurs in body text, not the two inspected abstract surfaces; surrounding regulatory content unassessed. |
| damico-text | DOI:10.1038/sj.embor.7400662; Historical derived reading-order text: newline 10 and newlines 24–33 | context_only | Generic physical/classification and supplied-literal reading aid. Timestamp is the original extraction completion, not PDF acquisition or current copying. |
| damico-derivation | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-source-agent/damico-derivation-receipt.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Original pdftotext command, source/output hashes and extraction interval; not a new extraction. |
| canonical-initial-failure | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1099%2Fijs.0.64068-0&amp;format=json&amp;resultType=core; Actual request 2026-10-22T04:55:55.923942+00:00 through 2026-10-22T04:55:55.935319+00:00 | context_only | Initial DNS error bytes, not metadata; successful retry is separate. |
| canonical-initial-failure-access | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-source-agent/canonical-metadata-access.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Exact current canonical access receipt and response hash; failure distinct from successful retry and native validation. |
| canonical-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1099%2Fijs.0.64068-0&amp;format=json&amp;resultType=core; Actual request 2026-10-22T04:56:06.236517+00:00 through 2026-10-22T04:56:06.953186+00:00 | supports | Successful primary indexed identity and existing strain 37T growth interval from -12 to 10 °C, with CCUG51855T/CIP108865T aliases. No full curve, optimum, culture optimization or other incidental properties adopted. |
| canonical-metadata-access | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-source-agent/canonical-metadata-network-retry-access.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Exact current canonical access receipt and response hash; failure distinct from successful retry and native validation. |
| taxonomy | NCBITaxon:357794; Fresh successful official species/type-material retry | supports | Psychromonas ingrahamii and strain 37T/CCUG51855T/CIP108865T identities only; no quantitative phenotype inferred. |
| taxonomy-access | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-grounding-agent/taxonomy-retry-access.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Actual successful retry interval after a separate initial DNS failure. |
| taxonomy-reading | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-grounding-agent/taxonomy-identity.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Official species/type-material identity with successful original request and separate failed access. |
| taxonomy-initial-failure | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=357794; Initial DNS error bytes, not taxonomy XML | context_only | Failed access is retained separately from the successful retry and native checks. |
| taxonomy-initial-failure-access | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-grounding-agent/taxonomy-access.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Exact initial taxonomy failure interval and response hash. |
| sources | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-source-agent/source-assessment.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Five works, coherent current threshold use and one bounded three-note source-location minor; detailed efficacy unassessed. |
| source-identities | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-source-agent/source-ledger.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | All five assigned identities and selected scopes; retained metadata and current successful canonical retry keep distinct clocks. |
| source-status | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-source-agent/source-status-ledger.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Actual original notice observations, not an exhaustive fresh status search. |
| placements | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-source-agent/source-placement-ledger.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | All seventeen external placements; eighteen grounding fields are separately covered by node-edge audits. |
| snippets | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-source-agent/snippet-ledger.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | All fifteen supplied snippets are literal; source surface and detailed causal efficacy remain separate questions. |
| notes | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-source-agent/source-note-ledger.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Sixteen notes including the singular canonical note; three abstract-surface attributions need correction. |
| source-nodes-edges | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-source-agent/node-edge-source-ledger.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | All fifteen nodes and fourteen edges with complete raw payloads and bounded source dispositions. |
| canonical | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-source-agent/canonical-assessment.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Existing named strain and reported -12 to 10 °C interval support the current ambient threshold, with source and quantity limits retained. |
| source-reading | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-source-agent/primary-reading-scope.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Selected classification, generic physical text and existing literal spans; no whole-paper or detailed efficacy review. |
| source-access | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-source-agent/source-access-limits.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Ten retained entries, eight original acquisition intervals, historical text derivation and two current canonical attempts; clocks distinct. |
| source-reuse | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-source-agent/source-reuse-receipt.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | All ten exact copies retain prior-receipt pins; only eight have acquisition clocks, two derived entries explicitly null. |
| source-native | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-source-agent/native-context.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Native four VERIFIED/eleven NOT_IN_ABSTRACT inconclusive results remain distinct from manual fifteen literal matches. |
| source-locations | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-source-agent/source-surface-location-check.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Three exact body matches with negative indexed/PMC abstract matches; source-surface correction only. |
| source-owners | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-source-agent/source-owner-reading.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Exact connector ADDED_EDGES note payload and PR664 consumer windows; ordinary no-op distinct from replacement consumption. |
| source-manifest | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-source-agent/evidence-manifest.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | All 29 frozen source artifacts verified. |
| root-reading | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-source-root/selected-primary-reading.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Root selected primary, authority and owner scopes; incidental content not adopted. |
| root-verification | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-source-root/root-current-verification.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Root current input, frozen artifact, qualified history and local review-array verification. |
| adjudication | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-root-adjudication.json; Final root adjudication | supports | Exact one major and three minors, four findings/actions and current owner/field scopes control this combined review. |

## Limits And Additional Notes

- No fresh B15 common diagnostic execution is asserted. Full just test was NOT_RUN; only the five optional focused Stage2 tests are reused. Products retains 123 no-adapter skips and covers two configured mappings. Common checks establish bounded software/data integrity, not scientific support, current-target checks or prior-batch finalization. Serializers must append to these helper notes and limitations.
- Selected classification/generic physical text and supplied literal spans only; no whole-paper efficacy or exhaustive notice review.
- Detailed stress-defense/regulatory/fitness/survival/cryoprotection/cultivation optimization and intervention efficacy remains UNASSESSED_SCOPE.
- Exact inclusive10 boundary and exact Psychrophile synonym equivalence remain qualified; no all-publication absence inference from selected near-freezing passage.
- Canonical primary indexed abstract supports existing named strain/interval; no full body, exhaustive curve or optimization adopted. Other displayed culture/composition/genome material incidental and unadopted.
- Original acquisition, current copy, extraction and reading clocks remain distinct; historical notice fields are not fresh status searches.
- Initial optional-path search corrected with ignored-inclusive source-folder search; no retained canonical DOI metadata found in that bounded search. No broken-DOI inference.
- Initial optional BeautifulSoup import unavailable and initial prewrite matcher incorrectly removed angle-bracket content from already-extracted text; standard-library parser and text-only whitespace matching corrected these local read/check issues before any ledger write. Neither was a native failure.
- Source-supported phenotype and literal placements independently source-audited; no new detailed stress/defense/survival/cryoprotection/fitness/cultivation or enzyme-improvement judgments.
- Node6 signaling-system wording and broad-association proxy descriptions remain qualified, without forced extra type or relation findings.
- Biological alias equivalence is not established solely by faithful upstream copying.
- Private/remote human acceptance unknown; local absence includes ignored/hidden files but excludes .git/.venv internals.
- Ground auditor did not rerun common/native checks or ontology databases.
- Root adopted D’Amico selected generic near-freezing classification and physical challenges, Ramon selected generic physical context, and the Phadtare indexed physical RNA-structure sentence. Detailed signaling/regulation, stress defenses, survival, fitness, cryoprotection, cultivation optimization and intervention efficacy remain unassessed. Ramasamy matching establishes six existing literal spans only.
- The canonical indexed abstract was fully displayed, but adopted scope is the existing strain37T, reported -12 to10 degreesC and CCUG51855T/CIP108865T aliases. Other culture, composition and genomic passages are incidental and unadopted; no full growth curve or optimization was assessed.
- Ten retained source entries comprise eight original acquisition intervals, derived PDF text and its historical extraction receipt. Current copy and reading times are distinct. Initial canonical and taxonomy DNS failures and successful retries retain separate clocks and bytes. Notice observations are historical metadata fields, not an exhaustive current status search.
- Current writer outcomes are static inferences from selected guards and exact payload comparisons. No writer or full PR664 dry run was executed.
- Original B14 common diagnostics are qualified for unchanged B15 inputs, not fresh B15 executions. Current target inspect, validation, strict validation and snippet check are fresh. The serializer common guard separately rechecks current inputs and five database pins.
- Full just test was not run; focused Stage2 tests and product skips retain original scope. Software checks do not establish scientific correctness.
- Active exact METPO:1000448, direct parent1000306 and the numeric-temperature/growth-range lineage1000533/1000535 are supported. Raw maximum-inclusive10 Cel restriction uses generic has-value2000071. Definition, trait node, edge0, graph description and canonical note coherently use an ambient threshold at/below10; no inherited interval-width conflict is present. Exact boundary calibration and biological Psychrophile alias equivalence remain qualified.
- Local membrane-fluidity METPO:1007505 is in v3 and absent from captured upstream raw OWL. Local v8 confers is broad. PATO:0001306 decreased temperature is a relatively low-temperature quality with a coherent declared closeMatch to the environmental condition. The current node denotes ambient condition, not a cooling execution.
- RO:0002211 and its negative/positive subproperties require process endpoints. RO:0002326 has material-to-process roles via2216→2500→2595, without2215; edges5/6 fit those formal roles. This does not establish executor efficacy. Ice-crystal growth is processual; RNA structure is a quality; compatible solutes are material substances.
- Node6 process label versus regulatory-system wording and broad Biolink association proxy descriptions remain qualified without forced extra categorical findings. NamedThing roles do not import RO process requirements or prove statistical association or benefit.
- Canonical primary indexed abstract and official taxonomy support Psychromonas ingrahamii37T, existing -12 to10 degreesC interval and aliases. The arithmetic width is irrelevant to the current coherent endpoint threshold; taxonomy supports identity only.
- One connected component,15 nodes,14 edges, three REVIEWED_LABEL_ONLY protein aggregates and zero instances are permissible NONMECHANISTIC context. No extra connector, accession or dataset is required merely to fill optional structure.
- The retained20-organism/28-dataset catalog contains no exact Psychromonas/P.ingrahamii or Pseudoalteromonas/P.haloplanktis entry under the bounded searches. This is not an exhaustive source-organism inventory or whole-corpus absence. Bounded project/install/PATH discovery found no maintained adapter; no module query was executed.
- Publication is separate from this local review. No scientific record, mapping, ontology, history, generated product or paid-provider run changed.
- Qualified reuse of four original B14 diagnostics is recorded in /private/tmp/traitmech-record-sweep-015.67f2ce7a/common-diagnostic-reuse-qualification.json. Historical products failures/retry and original cache provenance remain in /private/tmp/traitmech-record-sweep-014.q8m4v2cs/new-base-diagnostic-independent-review-agent/fresh-products-completion.json. B14 generated reports are retained output snapshots, not B15 source inputs or synthetic B15 reports. B15-to-B14 byte equality does not change the historical false B14-to-B13 comparison; B14 final gates/commit and continuation pins remain separate.
- Exact findings, actions, fields, severities and owners come only from root FINAL: one imported-role major and three bounded minors. Current threshold use is coherent; no sibling interval-width finding or extra type/association finding is inherited.
- Serializer preparation adopts frozen audits and root adjudication without another whole-paper or whole-history review. Ten copied source entries retain eight original acquisition clocks, derived text and its historical extraction receipt. Current canonical/taxonomy failures and retries, root query/read/copy clocks and source-surface corrections remain distinct. Ground-auditor non-repetition is actor-specific; common guard separately rechecks qualified inputs and database pins. Original B14 diagnostics are not fresh B15 executions.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T050833Z-temperature-range-very-low
kind: record
repository: CultureBotAI/TraitMech
title: Whole-record review of temperature range very low
started_at: '2026-10-22T04:55:02.134554Z'
finished_at: '2026-10-22T05:08:33Z'
reviewer:
  identity: codex
  kind: agent
  independence: independent
  independence_basis: Separate source and grounding audits plus root selected primary
    reading and final adjudication supply scientific judgments. Serializer preparation
    does not claim another whole-paper scientific review.
  model: GPT-6 (Codex)
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'Whole-record review identifies incompatible imported process roles at four
  edges and three bounded minor issues: machinery facet, three source-surface notes
  and retrievable human acceptance. Current threshold semantics are internally coherent.
  Active identity, canonical reported -12 to10 degreesC interval, all15 literal quotations
  and selected formal facets are positive; detailed biological efficacy remains unassessed.'
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
  - path: data/traits/environment/temperature_range_very_low.yaml
    sha256: c7261e615cd23d77d07a8f71d0f11c81a56a0f2011b15676f2d6bce51812eb9d
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
  - path: history/infrastructure/disposition-typing-burndown/2026-08-08T060908Z-claude-code-f802c8.yaml
    sha256: 8ede4f80f46395efb74643e1f4158975a119ffaec78b5b291f0fc3a520a11c59
    role: context
  - path: history/infrastructure/node-type-consistency/2026-08-15T014631Z-claude-code-9d7f4d.yaml
    sha256: 21f19561c0d4769e7acc62e05e41d0d395a0f239938f00829f79f2b9c3ac2510
    role: context
  - path: history/infrastructure/pr664-adversarial-review/2026-09-07T010000Z-codex-60bca2.yaml
    sha256: 44f328d3f4735a641a33e6f5823a043ccc87594971cfdd9b58be134f3ea70106
    role: context
  - path: history/infrastructure/pr664-adversarial-review/2026-09-07T072500Z-codex-693abc.yaml
    sha256: 380e91dcba7a246605454aa4cc65cf7ab3f9236d8c95bb32748dc80fe648e6d9
    role: context
  - path: history/infrastructure/prioritize-graph-research/2026-08-18T073129Z-claude-code-6ffbb9.yaml
    sha256: a1c2c954475853822eec940a2c6ec5fafb357039cddb9211568661ba8b9c739b
    role: context
  - path: history/infrastructure/prioritize-graph-research/2026-08-20T072722Z-claude-code-5774c9.yaml
    sha256: f342f08a52f61fa1fe7350ee9aaba6f265760a90b959e98e979b3811135fbd3f
    role: context
  - path: history/infrastructure/trait-priority/2026-08-19T203529Z-claude-code-fbfb40.yaml
    sha256: 5337f34a01bb7f39da1e604544e839a3e42d558069ff2cf52706fb5b05286766
    role: context
  - path: history/other/canonical-examples-batch1/2026-08-20T074839Z-claude-code-6fb2f5.yaml
    sha256: c938f2928f2eb41505d58c2fb72d8de01d99534d766de9af400010e8778988a4
    role: context
  - path: history/records/temperature_optimum_very_low/2026-09-08T032500Z-codex-77dafe.yaml
    sha256: dfa857844cb78f8fbb905a762242c0671701caf54fe35c81da0c38422142cab3
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
  - path: reports/metpo_2026_06_12_active_review.tsv
    sha256: 45e9c6471475635ba1f2602cd636a119d490f5dbd8dd6ac8af1aab89a321379f
    role: context
  - path: reports/metpo_2026_06_12_release_delta.tsv
    sha256: afe858d2aa0ade08322c7808d5917ff370e069ba02c2642d483342db8e9323ac
    role: context
  - path: reports/ontology_snapshot_manifest.tsv
    sha256: 4a157279a8c4e3fc2afb5382a45c31961991bbd1f330f26d0061b0cfd0b4d213
    role: context
  - path: research/traits/environment/temperature_range_very_low-deep-research-falcon.md
    sha256: ad9558548c977b094ab7df525cf28f8e341ab782994bd026e7b5b4bfe65db47e
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
- target_id: METPO:1000448
  path: data/traits/environment/temperature_range_very_low.yaml
  label: temperature range very low
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_range_very_low.yaml
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
  selection: Fifth record in the actual B15 queue; current 366-line target and 101
    captured inputs. Local review is independent of remote publication.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - METPO:1000448
checks:
- check_id: new-base-qc
  name: Reused B14 corpus QC
  status: passed
  required: true
  target_ids:
  - METPO:1000448
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
  - METPO:1000448
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
  - METPO:1000448
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
  - METPO:1000448
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
- check_id: temperature-range-very-low-target-validate
  name: Focused native validation
  status: passed
  required: true
  target_ids:
  - METPO:1000448
  command: just validate data/traits/environment/temperature_range_very_low.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Native validation passed; scientific interpretation is assessed separately.
  evidence_ids:
  - check-temperature-range-very-low-target-validate
- check_id: temperature-range-very-low-target-strict
  name: Focused strict validation
  status: passed
  required: true
  target_ids:
  - METPO:1000448
  command: just validate-strict data/traits/environment/temperature_range_very_low.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: The actual validate-strict command passed.
  evidence_ids:
  - check-temperature-range-very-low-target-strict
- check_id: temperature-range-very-low-snippets-network
  name: Focused network snippet check
  status: passed
  required: true
  target_ids:
  - METPO:1000448
  command: just verify-snippets --record data/traits/environment/temperature_range_very_low.yaml
    --out /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-snippets.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 'Native command succeeded for fifteen snippets: four VERIFIED and eleven
    NOT_IN_ABSTRACT, the latter inconclusive. Manual matching supports all fifteen
    literal spans; three notes misidentify their source surface.'
  evidence_ids:
  - check-temperature-range-very-low-snippets-network
- check_id: native-inspect
  name: One-target native review capture
  status: passed
  required: true
  target_ids:
  - METPO:1000448
  command: uv run python scripts/record_review.py inspect --targets /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low.targets.json
    --input .claude/skills/curate-yaml-record/references/review-checklist.md --input
    .claude/skills/manage-identifiers/SKILL.md --input .claude/skills/review-yaml-record/SKILL.md
    --input CLAUDE.md --input DO_NOT_WORK.md --input conf/evidence_snippet_baseline.tsv
    --input conf/record_review.yaml --input data/raw/biolink-model.yaml --input data/raw/metpo.owl
    --input data/traits/environment/temperature_range.yaml --input docs/CURATION_PLAYBOOK.md
    --input docs/GROUNDING_POLICY.md --input docs/PATHWAY_LINKS.md --input docs/record-review-profile.md
    --input docs/record-reviews.md --input history/infrastructure/canonical-examples/2026-08-19T183734Z-claude-code-44a170.yaml
    --input history/infrastructure/disposition-typing-burndown/2026-08-08T060908Z-claude-code-f802c8.yaml
    --input history/infrastructure/node-type-consistency/2026-08-15T014631Z-claude-code-9d7f4d.yaml
    --input history/infrastructure/pr664-adversarial-review/2026-09-07T010000Z-codex-60bca2.yaml
    --input history/infrastructure/pr664-adversarial-review/2026-09-07T072500Z-codex-693abc.yaml
    --input history/infrastructure/prioritize-graph-research/2026-08-18T073129Z-claude-code-6ffbb9.yaml
    --input history/infrastructure/prioritize-graph-research/2026-08-20T072722Z-claude-code-5774c9.yaml
    --input history/infrastructure/trait-priority/2026-08-19T203529Z-claude-code-fbfb40.yaml
    --input history/other/canonical-examples-batch1/2026-08-20T074839Z-claude-code-6fb2f5.yaml
    --input history/records/temperature_optimum_very_low/2026-09-08T032500Z-codex-77dafe.yaml
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
    --input proposals/metpo_traitmech_v3/metpo_proposal_classes_robot.tsv --input
    proposals/metpo_traitmech_v3/proposal.md --input proposals/metpo_traitmech_v8/metpo_proposal_properties_robot.tsv
    --input proposals/metpo_traitmech_v8/proposal.md --input reports/metpo_2026_06_12_active_review.tsv
    --input reports/metpo_2026_06_12_release_delta.tsv --input reports/ontology_snapshot_manifest.tsv
    --input research/traits/environment/temperature_range_very_low-deep-research-falcon.md
    --input schema/record_review.yaml --input scripts/add_cold_shock_response_trait.py
    --input scripts/add_homeoviscous_adaptation_trait.py --input scripts/add_palmelloid_formation_trait.py
    --input scripts/audit_causal_graphs.py --input scripts/audit_graph_protein_taxa.py
    --input scripts/audit_predicate_domains.py --input scripts/audit_schema.py --input
    scripts/audit_unapplied_groundings.py --input scripts/audit_uniprot_grounding.py
    --input scripts/backfill_canonical_examples_444.py --input scripts/connect_mesophilic_graph_183.py
    --input scripts/connect_temperature_delta_high_graph_183.py --input scripts/connect_temperature_delta_very_low_graph_183.py
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
    --input scripts/record_review.py --input scripts/repair_pr664_adversarial_review.py
    --input scripts/review_mesophilic_graph_183.py --input scripts/review_obligately_piezophilic_graph_183.py
    --input scripts/review_temperature_delta_high_graph_183.py --input scripts/review_temperature_delta_very_low_graph_183.py
    --input scripts/review_temperature_optimum_very_low_graph_183.py --input scripts/review_temperature_range_mid3_graph_183.py
    --input scripts/review_temperature_range_mid4_graph_183.py --input scripts/review_temperature_range_very_low_graph_183.py
    --input scripts/seed_from_metpo.py --input scripts/trait_priority.py --input scripts/verify_metpo_proposal.py
    --input src/traitmech/schema/mech_shared.yaml --input src/traitmech/schema/traitmech.yaml
    --input src/traitmech/validation/write_validated.py
  exit_code: 0
  expected_exit_code: 0
  summary: One current target, 101 captured inputs, exact current base and successful
    native inspect.
  evidence_ids:
  - capture
- check_id: uniprot-applicability
  name: Protein-instance metadata applicability
  status: not_applicable
  required: false
  target_ids:
  - METPO:1000448
  summary: Three contextual protein aggregates are REVIEWED_LABEL_ONLY with rationales
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
  - METPO:1000448
  summary: Bounded maintained-runner discovery found no adapter. Retained catalog
    and selected source identities provide no module or efficacy result.
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
- evidence_id: check-temperature-range-very-low-target-validate
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-target-validate.log
  locator: Executed 2026-10-22T04:55:26.923104+00:00 through 2026-10-22T04:55:27.702377+00:00;
    metadata temperature-range-very-low-target-validate.json
  accessed_at: '2026-10-22T04:55:27.702377Z'
  support: context_only
  summary: Native validation passed; scientific interpretation is assessed separately.
  snapshot_sha256: cf8c9aecf1991ef9be6567e7478f37742e53edc40aca4c3680e288f93423b3f8
- evidence_id: check-temperature-range-very-low-target-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-target-strict.log
  locator: Executed 2026-10-22T04:55:26.923143+00:00 through 2026-10-22T04:55:28.104669+00:00;
    metadata temperature-range-very-low-target-strict.json
  accessed_at: '2026-10-22T04:55:28.104669Z'
  support: context_only
  summary: The actual validate-strict command passed.
  snapshot_sha256: febfce7a235dfe96e1ff6e13abe93ccb7bab6a4744352facdb2f8665d8fb79ea
- evidence_id: check-temperature-range-very-low-snippets-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-snippets-network.log
  locator: Executed 2026-10-22T04:55:38.779914+00:00 through 2026-10-22T04:55:45.530740+00:00;
    metadata temperature-range-very-low-snippets-network.json
  accessed_at: '2026-10-22T04:55:45.530740Z'
  support: context_only
  summary: 'Native command succeeded for fifteen snippets: four VERIFIED and eleven
    NOT_IN_ABSTRACT, the latter inconclusive. Manual matching supports all fifteen
    literal spans; three notes misidentify their source surface.'
  snapshot_sha256: da94622c77cd6508246c89e1f6b89965931399260cedc2e5c3f33399da5c9a78
- evidence_id: capture
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low.inspect.json
  locator: Actual successful native inspect with 101 captured inputs
  accessed_at: '2026-10-22T04:55:02.870968Z'
  support: context_only
  summary: All current captured source hashes and exact target are bound before serialization.
  snapshot_sha256: 6661822d16047e11c43e652e72cdf23aa4f73fdda1f035093daf3eadc1e379cd
- evidence_id: record
  kind: record_content
  reference: data/traits/environment/temperature_range_very_low.yaml
  locator: Whole current record
  accessed_at: '2026-10-22T04:55:02.870968Z'
  support: supports
  summary: Fifteen nodes, fourteen edges, twelve embedded events, one canonical example,
    three reviewed label-only protein aggregates and zero instances.
  snapshot_sha256: c7261e615cd23d77d07a8f71d0f11c81a56a0f2011b15676f2d6bce51812eb9d
- evidence_id: local-init
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/batch015-local-initialization-receipt.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T03:50:31.750633Z'
  support: context_only
  summary: Actual local initialization and fifth queue target; publication remains
    separate.
  snapshot_sha256: b5fc6d47e2719f9da11bad0719b933f4af76d4ccc30226c15a2a7c51c07e2283
- evidence_id: policy
  kind: authority
  reference: docs/GROUNDING_POLICY.md
  locator: Captured maintained authority
  accessed_at: '2026-10-22T04:59:17.422382Z'
  support: supports
  summary: Protein family/function grounding, reviewed label-only aggregates and optional
    instances.
  snapshot_sha256: 891678c983c2283a47c81c47950b35753981e9339d105f3bbdda92a1f5ab7f42
- evidence_id: playbook
  kind: authority
  reference: docs/CURATION_PLAYBOOK.md
  locator: Captured maintained authority
  accessed_at: '2026-10-22T04:59:17.422382Z'
  support: supports
  summary: Source attribution and attributable acceptance.
  snapshot_sha256: 735e9b810471da9f7d8364e35ffe1e741edb3421480dac01727db6ea5aa65da9
- evidence_id: schema
  kind: authority
  reference: src/traitmech/schema/traitmech.yaml
  locator: Captured maintained authority
  accessed_at: '2026-10-22T04:59:17.422382Z'
  support: supports
  summary: Current material, process, quality, environmental condition and quantitative
    NONMECHANISTIC facets.
  snapshot_sha256: 46c47fc627b80ccbba1e8ab3fb6f2aee93bc2aef7aaf72fe9aadc3257f2c02dd
- evidence_id: predicate-mapping
  kind: authority
  reference: mappings/predicate_grounding.tsv
  locator: Captured maintained authority
  accessed_at: '2026-10-22T04:59:17.422382Z'
  support: supports
  summary: Wildcard rows 11/58/64/65 are conditional future empty-field recurrence
    inputs; generic grounder skips populated identifiers.
  snapshot_sha256: 8e28c19e93aca3dc164a3befbe2612b289241de457c59f499e65936c03b7ce52
- evidence_id: canonical-writer
  kind: authority
  reference: scripts/backfill_canonical_examples_444.py
  locator: Captured maintained authority
  accessed_at: '2026-10-22T04:59:17.422382Z'
  support: supports
  summary: Exact Psychromonas threshold note matches current SOURCES/TRANCHE; equality/no-op,
    nonempty rejection and global queue guards are positive context, not a faulty
    quantity producer.
  snapshot_sha256: 18ca0766789c239d693ef665e8b1d43c1209a0f414a326f1c5d890f88de7b20c
- evidence_id: identity
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-grounding-agent/identity-and-hierarchy.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:59:17.417858Z'
  support: context_only
  summary: Active target/direct parent and inclusive threshold restriction; exact
    boundary calibration and biological alias equivalence remain qualified.
  snapshot_sha256: 4ad1f46ae2ae76559172659eb4a1a629d6b4e5045692dcf68c7c86a50505c109
- evidence_id: nodes-edges
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-grounding-agent/node-edge-grounding-ledger.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:59:17.417408Z'
  support: context_only
  summary: All fifteen referents and fourteen formal relation dispositions.
  snapshot_sha256: 1d9387876c2557d77b30805eb88ab589c25aa88fe40487e5e14846a37a36f58f
- evidence_id: owners
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-grounding-agent/ownership-assessment.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:59:17.421215Z'
  support: context_only
  summary: Exact review, connector and PR664 roles; record-only machinery facet and
    conditional mapping recurrence.
  snapshot_sha256: 893cb8737fbd419eba10db53a2fd59629279590591c946c777de2299999160c4
- evidence_id: owner-primary
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-grounding-agent/owner-primary-reading.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:59:17.415512Z'
  support: context_only
  summary: Selected current owner windows and qualified prior context; no writer execution.
  snapshot_sha256: debf7f91b5394ca3a27e313ca27a108725327f98d68a61e36377234effcdf4d8
- evidence_id: local-authority
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-grounding-agent/local-authority-reading.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:59:17.416826Z'
  support: context_only
  summary: Actual schema, policy, local proposals and mapping scope.
  snapshot_sha256: 7995a801bc8d84d5eba619de64157b0402a6828f080ff74bf67220e1733ece70
- evidence_id: histories
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-grounding-agent/history-reading-provenance.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:59:17.413066Z'
  support: context_only
  summary: Twenty-two current actor projections and exact qualified prior whole readings;
    no fresh whole-history claim.
  snapshot_sha256: 84897cd1e06a06a0135f9a355f04912240b3f9be366a8ac8c5fee984f1833354
- evidence_id: embedded-history
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-grounding-agent/embedded-history-ledger.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:59:17.413513Z'
  support: context_only
  summary: 'Twelve embedded events: eleven AI-assisted events and one seed.'
  snapshot_sha256: 4b8e952e6eff0b8d560dbc5f9bdf600cf1ae75eb6cea28307ed2e0d96a663fd1
- evidence_id: human-search
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-grounding-agent/search-and-provenance.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:55:34.115854Z'
  support: context_only
  summary: 'Ignored- and hidden-inclusive search: 196 matching paths, 71 matching
    arrays and 96 all-local arrays, zero exact target.'
  snapshot_sha256: c8990dfdc68abb8d2ebf4155549b8c593058a07da43e3415969f6038904e12c8
- evidence_id: discovery
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-grounding-agent/discovery-dispositions.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:59:17.421110Z'
  support: context_only
  summary: Uncaptured leads remain matching-line context; private or remote acceptance
    unknown.
  snapshot_sha256: 357ecf58575e75c79d12d4add3e32f113e19c5d4ec1f51a8e4504a2955f7f3da
- evidence_id: expression
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-grounding-agent/expression-and-readiness.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:59:17.421987Z'
  support: context_only
  summary: One connected NONMECHANISTIC graph and three label-only aggregates are
    permissible; retained catalog and bounded runner availability do not establish
    efficacy.
  snapshot_sha256: 07805a1b8e87e30bd05ef1ad62eed506ae4930b872d5901e341db2cd673966b9
- evidence_id: expression-discovery
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-grounding-agent/adapter-discovery.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:55:34.239387Z'
  support: context_only
  summary: Bounded current maintained-runner discovery found no available adapter;
    no module query executed.
  snapshot_sha256: 2b385a21c01ab116bb4b55d9bda107f4735b6b74098a77adf490c3a66625b52e
- evidence_id: catalog-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-grounding-agent/catalog-reuse.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:59:17.421903Z'
  support: context_only
  summary: Original catalog acquisition remains distinct from current copying and
    selected-name reading.
  snapshot_sha256: 1546182d6a45fbfbdb8c33a6d564c8bad9c6fddde38f4a83fa6e5deb8422564c
- evidence_id: ground-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-grounding-agent/reading-scope-receipt.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:59:17.422308Z'
  support: context_only
  summary: Actual current reading scopes, qualified prior histories and owner distinctions.
  snapshot_sha256: 6581b2acade3b099a2d0e53a2e706b1a75fe4ff8e9360132081f816ca603f1e9
- evidence_id: ground-assessment
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-grounding-agent/grounding-assessment.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:59:17.422382Z'
  support: context_only
  summary: One imported-role major, machinery-facet minor and bounded human provenance
    minor.
  snapshot_sha256: fc84f20d7557c5e62184a732196a83e5ccd42e3a28ced54e9f72c6ed5cddbceb
- evidence_id: ground-manifest
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-grounding-agent/evidence-manifest.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:59:17.424025Z'
  support: context_only
  summary: All 27 immutable ground artifacts verified.
  snapshot_sha256: 12c04e296d800b102618969a54b28bcbea83a989b8199ea2592bafa4e77208f9
- evidence_id: writer-payloads
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-grounding-agent/writer-payload-comparison.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:57:12.590329Z'
  support: context_only
  summary: Six review after-edges and one node match; six connector guards/additions
    and AFTER metadata match. Both ordinary writers no-op; PR664 consumes six unfiltered
    additions. Static comparison only.
  snapshot_sha256: 756d0141c7c9f65981dcc258432e7cd03ad1f46794bd291f01e9dafe00870695
- evidence_id: verification-support
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-grounding-agent/root-verification-support.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T05:01:07.084759Z'
  support: context_only
  summary: Bounded current verification of actual source/ground shapes, current inputs,
    original clocks and native receipts; no native or scientific reexecution.
  snapshot_sha256: 1f3aa31ea1bcbc8c0bb49238ed66db7f5df0458da5055a51b41fffd1aef5e13c
- evidence_id: ontology-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-source-root/selected-ontology-primary.json
  locator: Exact selected response; query 2026-10-22T04:56:09.781703+00:00 through
    2026-10-22T04:56:09.787919+00:00
  accessed_at: '2026-10-22T04:56:09.787919Z'
  support: supports
  summary: Current selected RO/BFO/PATO, raw METPO, local proposals and Biolink authority.
    Query clocks differ from copy/read clocks. Ground auditor did not repeat queries
    or database hashing; serializer common guard separately verifies qualified inputs.
  snapshot_sha256: 3e4a1cd8b8eee9335b7f586e05237cc7e4cc17da8f8eaae146227ca153801038
- evidence_id: authority-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-source-root/selected-authority-primary.json
  locator: Exact selected response; query 2026-10-22T04:56:09.788363+00:00 through
    2026-10-22T04:56:10.010739+00:00
  accessed_at: '2026-10-22T04:56:10.010739Z'
  support: supports
  summary: Current selected RO/BFO/PATO, raw METPO, local proposals and Biolink authority.
    Query clocks differ from copy/read clocks. Ground auditor did not repeat queries
    or database hashing; serializer common guard separately verifies qualified inputs.
  snapshot_sha256: 94b12e0e661d68cb545b0c55783fcf126247e64e43ca609caa399aba16157dce
- evidence_id: authority-provenance
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-grounding-agent/primary-reuse-provenance.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:59:17.407412Z'
  support: context_only
  summary: Exact current root query clocks and ground-auditor copies, with separate
    reading completion.
  snapshot_sha256: bc791ffd05db1736dac108f7fd27e3ba4cae1a11596956f505b90074503d511b
- evidence_id: catalog-original
  kind: authority
  reference: https://imodulondb.org/api/datasets
  locator: Original retained 20-organism/28-dataset catalog
  accessed_at: '2026-10-21T07:36:12.858149Z'
  support: context_only
  summary: No exact Psychromonas or Pseudoalteromonas entry under the bounded name
    searches; not an exhaustive source-organism inventory or global absence finding.
    No module or efficacy result.
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: damico-metadata
  kind: primary_source
  reference: DOI:10.1038/sj.embor.7400662
  locator: Indexed identity and selected generic classification context
  accessed_at: '2026-10-21T10:00:01.461116Z'
  support: supports
  summary: Identity and existing near-freezing classification positive; exact threshold
    calibration and biological alias equivalence remain qualified.
  snapshot_sha256: 24d64254a2baba7c573dff7ae523cc0e00d30e297c4f1fd7aa3a23c51a057059
- evidence_id: damico-pdf
  kind: primary_source
  reference: DOI:10.1038/sj.embor.7400662
  locator: Original author-repository PDF; selected generic classification and supplied
    physical fragment
  accessed_at: '2026-10-21T10:03:39.641646Z'
  support: supports
  summary: Original acquisition retained; derived text and extraction time are separate.
    No whole-paper efficacy review.
  snapshot_sha256: 5a7678c6418efbcccf54d91c55eea1c08f2a4ed0ce0e07a6995d5903b9a0eb2e
- evidence_id: cold-metadata
  kind: primary_source
  reference: DOI:10.1007/s42770-023-01057-4
  locator: Indexed identity and supplied-span matching
  accessed_at: '2026-10-21T22:07:08.865512Z'
  support: supports
  summary: Identity and literal abstract spans only; detailed signaling, defense,
    survival and fitness efficacy unassessed.
  snapshot_sha256: da5cffab81fe0e039c6fcec8f318b2715f5604eaf8722ea6f63f944178ed447b
- evidence_id: cold-body
  kind: primary_source
  reference: DOI:10.1007/s42770-023-01057-4
  locator: Zero-based all-HTML paragraphs 17/Par10/Sec3 and 31/Par20/Sec7
  accessed_at: '2026-10-21T22:07:50.938485Z'
  support: supports
  summary: Two supplied connector spans occur in body text, not inspected indexed
    or PMC abstracts; surrounding regulatory efficacy is unassessed.
  snapshot_sha256: bb09a59c07f43ff0af177f89b624c8b5d4841e513ed0d478120954a016342889
- evidence_id: antarctic-metadata
  kind: primary_source
  reference: DOI:10.3389/fmicb.2023.1197797
  locator: Indexed identity and historical notice fields
  accessed_at: '2026-10-21T10:00:02.068795Z'
  support: supports
  summary: Identity only; no current exhaustive notice or detailed efficacy assessment.
  snapshot_sha256: d1315a25547237a1d13ab9a9cb37c9a3cc9bfb2c9c393eb6a45e5ad108d78104
- evidence_id: antarctic-body
  kind: primary_source
  reference: DOI:10.3389/fmicb.2023.1197797
  locator: 'Zero-based body paragraphs 8/9: six supplied-fragment matches only'
  accessed_at: '2026-10-21T10:00:47.316930Z'
  support: supports
  summary: Existing snippets literal; surrounding numerical-strain comparisons, stress
    defense, cryoprotection and intervention efficacy unassessed.
  snapshot_sha256: a5d04369d769d107921d98c6892695ea59f8682f2823bc8e60e198f464666bce
- evidence_id: phadtare-metadata
  kind: primary_source
  reference: DOI:10.4161/rna.7.6.13482
  locator: Indexed identity, supplied spans and selected physical RNA-structure sentence
  accessed_at: '2026-10-21T11:41:58.419539Z'
  support: supports
  summary: Generic physical context and literal occurrence only; no detailed regulatory,
    translation or efficacy conclusion.
  snapshot_sha256: afa3b113a78e9df1f4d51a735b8ba6cdde582d022cc561d1428d4af8e1b523fa
- evidence_id: phadtare-body
  kind: primary_source
  reference: DOI:10.4161/rna.7.6.13482
  locator: Zero-based all-HTML paragraph 11/sec2
  accessed_at: '2026-10-22T02:07:16.769656Z'
  support: supports
  summary: Existing connector span occurs in body text, not the two inspected abstract
    surfaces; surrounding regulatory content unassessed.
  snapshot_sha256: efdca44128e6627ab666aae31634f3365dc11fae398a27b06062bbb4fefc0acf
- evidence_id: damico-text
  kind: validation
  reference: DOI:10.1038/sj.embor.7400662
  locator: 'Historical derived reading-order text: newline 10 and newlines 24–33'
  accessed_at: '2026-10-21T21:57:11.990598Z'
  support: context_only
  summary: Generic physical/classification and supplied-literal reading aid. Timestamp
    is the original extraction completion, not PDF acquisition or current copying.
  snapshot_sha256: 71ef77b88e880420f533454926cac17498cbf8db380465139c888057115143e8
- evidence_id: damico-derivation
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-source-agent/damico-derivation-receipt.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-21T21:57:11.990598Z'
  support: context_only
  summary: Original pdftotext command, source/output hashes and extraction interval;
    not a new extraction.
  snapshot_sha256: 4bc68e1e7c942f28f8b2be82ef5b82e45461cdec22ed95828753130bc433d1ac
- evidence_id: canonical-initial-failure
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1099%2Fijs.0.64068-0&format=json&resultType=core
  locator: Actual request 2026-10-22T04:55:55.923942+00:00 through 2026-10-22T04:55:55.935319+00:00
  accessed_at: '2026-10-22T04:55:55.935319Z'
  support: context_only
  summary: Initial DNS error bytes, not metadata; successful retry is separate.
  snapshot_sha256: 35281279d8e2164cee8666d6f8aad891326911e887ab1b2ab778c8ac6d09dc6c
- evidence_id: canonical-initial-failure-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-source-agent/canonical-metadata-access.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:55:55.935319Z'
  support: context_only
  summary: Exact current canonical access receipt and response hash; failure distinct
    from successful retry and native validation.
  snapshot_sha256: adcc10277f1ae7d1e069d2cdf9970c3947180eadf8b458cc0d24b18260cc6d59
- evidence_id: canonical-metadata
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1099%2Fijs.0.64068-0&format=json&resultType=core
  locator: Actual request 2026-10-22T04:56:06.236517+00:00 through 2026-10-22T04:56:06.953186+00:00
  accessed_at: '2026-10-22T04:56:06.953186Z'
  support: supports
  summary: Successful primary indexed identity and existing strain 37T growth interval
    from -12 to 10 °C, with CCUG51855T/CIP108865T aliases. No full curve, optimum,
    culture optimization or other incidental properties adopted.
  snapshot_sha256: bff9e3609446250f658b4918fb0879c2a9ab72cffed247e788f2489f1048b5d4
- evidence_id: canonical-metadata-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-source-agent/canonical-metadata-network-retry-access.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:56:06.953186Z'
  support: context_only
  summary: Exact current canonical access receipt and response hash; failure distinct
    from successful retry and native validation.
  snapshot_sha256: 2a375d49e2e025135c10ab565aa831a72f9802e9d03528422314b18d8e1f24ec
- evidence_id: taxonomy
  kind: authority
  reference: NCBITaxon:357794
  locator: Fresh successful official species/type-material retry
  accessed_at: '2026-10-22T04:56:01.741531Z'
  support: supports
  summary: Psychromonas ingrahamii and strain 37T/CCUG51855T/CIP108865T identities
    only; no quantitative phenotype inferred.
  snapshot_sha256: 36d10a5ee297409c143dba791b34bc166ad0fca14c07f5d2b522f25830b060e0
- evidence_id: taxonomy-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-grounding-agent/taxonomy-retry-access.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:56:01.741531Z'
  support: context_only
  summary: Actual successful retry interval after a separate initial DNS failure.
  snapshot_sha256: f562343b6cca304bfb5e9f04bd09fe93f92e45e1a530a0a128e489d9cf2003c3
- evidence_id: taxonomy-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-grounding-agent/taxonomy-identity.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:59:17.417279Z'
  support: context_only
  summary: Official species/type-material identity with successful original request
    and separate failed access.
  snapshot_sha256: 82638ea5f5066ae8a9c77620bdefb8ec1e735a48e3af67062ed52ee919aae69c
- evidence_id: taxonomy-initial-failure
  kind: validation
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=357794
  locator: Initial DNS error bytes, not taxonomy XML
  accessed_at: '2026-10-22T04:55:38.397380Z'
  support: context_only
  summary: Failed access is retained separately from the successful retry and native
    checks.
  snapshot_sha256: 35281279d8e2164cee8666d6f8aad891326911e887ab1b2ab778c8ac6d09dc6c
- evidence_id: taxonomy-initial-failure-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-grounding-agent/taxonomy-access.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:55:38.397380Z'
  support: context_only
  summary: Exact initial taxonomy failure interval and response hash.
  snapshot_sha256: 6e89fc3941585ec321d8cc8ec3869a2e16cf07ce67a0a7dfada0e82f1f06bdc4
- evidence_id: sources
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-source-agent/source-assessment.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:59:56.833373Z'
  support: context_only
  summary: Five works, coherent current threshold use and one bounded three-note source-location
    minor; detailed efficacy unassessed.
  snapshot_sha256: 988f4de15ebe18ca6d6dbe88158d26058aebcd7f934d28b212e2b5a2ca31b893
- evidence_id: source-identities
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-source-agent/source-ledger.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:59:56.758614Z'
  support: context_only
  summary: All five assigned identities and selected scopes; retained metadata and
    current successful canonical retry keep distinct clocks.
  snapshot_sha256: 70a0fa9ea64654088723fa62a2f6da3a8a4f3929877055a4c0799d9287859f98
- evidence_id: source-status
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-source-agent/source-status-ledger.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:59:56.758614Z'
  support: context_only
  summary: Actual original notice observations, not an exhaustive fresh status search.
  snapshot_sha256: 2a447865b6b322534a16548fd65810a01bc5d77cbcbc8a86bb3a9def567c745e
- evidence_id: placements
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-source-agent/source-placement-ledger.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:59:56.758614Z'
  support: context_only
  summary: All seventeen external placements; eighteen grounding fields are separately
    covered by node-edge audits.
  snapshot_sha256: ac47b58b11c447758856933abc42a4d9dc779606e0f3cde9875ba411bb28a398
- evidence_id: snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-source-agent/snippet-ledger.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:59:56.758614Z'
  support: context_only
  summary: All fifteen supplied snippets are literal; source surface and detailed
    causal efficacy remain separate questions.
  snapshot_sha256: 1bbc14ee52fe7229fc2299769d3bb53f40ce55c440381dbae87a3c8fe25bcf4e
- evidence_id: notes
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-source-agent/source-note-ledger.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:59:56.758614Z'
  support: context_only
  summary: Sixteen notes including the singular canonical note; three abstract-surface
    attributions need correction.
  snapshot_sha256: 5e335e2530013c82d12a3de302be9d9183b21611d1cdc309c53e9f17ce4fdddf
- evidence_id: source-nodes-edges
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-source-agent/node-edge-source-ledger.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:59:56.758614Z'
  support: context_only
  summary: All fifteen nodes and fourteen edges with complete raw payloads and bounded
    source dispositions.
  snapshot_sha256: 26dd8d56af3b4f106058abc1246934264c0bf579a4c673fbe32faa802e547712
- evidence_id: canonical
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-source-agent/canonical-assessment.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:59:56.758614Z'
  support: context_only
  summary: Existing named strain and reported -12 to 10 °C interval support the current
    ambient threshold, with source and quantity limits retained.
  snapshot_sha256: d996a13f8d3dd0589c975ef0bacb5fe95fd73d0c1bf1afe9f341a54a50dcfd54
- evidence_id: source-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-source-agent/primary-reading-scope.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:59:56.831294Z'
  support: context_only
  summary: Selected classification, generic physical text and existing literal spans;
    no whole-paper or detailed efficacy review.
  snapshot_sha256: 592a619b4f5a1feba4636ea33cb1c47b8d3eaa9212ca6297ee2f6b257508deab
- evidence_id: source-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-source-agent/source-access-limits.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:59:56.758614Z'
  support: context_only
  summary: Ten retained entries, eight original acquisition intervals, historical
    text derivation and two current canonical attempts; clocks distinct.
  snapshot_sha256: 4952f40c476469af4edbf684d41258fd46d52b8558c0f34989d2b98bfa18458f
- evidence_id: source-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-source-agent/source-reuse-receipt.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:56:41.247266Z'
  support: context_only
  summary: All ten exact copies retain prior-receipt pins; only eight have acquisition
    clocks, two derived entries explicitly null.
  snapshot_sha256: aeaf9ab5c6befbe045e067b5c998f0ff663cee9a1ecfa3fb062a8f579939b97c
- evidence_id: source-native
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-source-agent/native-context.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:59:56.833209Z'
  support: context_only
  summary: Native four VERIFIED/eleven NOT_IN_ABSTRACT inconclusive results remain
    distinct from manual fifteen literal matches.
  snapshot_sha256: d13a490ce77db21547f530b51bbd70686da6a05378a33b19159835e268278e14
- evidence_id: source-locations
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-source-agent/source-surface-location-check.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:59:56.758614Z'
  support: context_only
  summary: Three exact body matches with negative indexed/PMC abstract matches; source-surface
    correction only.
  snapshot_sha256: 1371c30e6f739243174a61cc94bfb7e415f7e6eb7170ff2ee511a40f9c6db889
- evidence_id: source-owners
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-source-agent/source-owner-reading.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:59:56.831392Z'
  support: context_only
  summary: Exact connector ADDED_EDGES note payload and PR664 consumer windows; ordinary
    no-op distinct from replacement consumption.
  snapshot_sha256: a96f5de171edbc7f4a0d3be3d7b95341c5729d42557490b5edc8671fc90d7f74
- evidence_id: source-manifest
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-source-agent/evidence-manifest.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:59:56.835635Z'
  support: context_only
  summary: All 29 frozen source artifacts verified.
  snapshot_sha256: 3513571d5e2ab2a9c5d24d0c261c3566e358721e18e49123a8f2f863ea3e949b
- evidence_id: root-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-source-root/selected-primary-reading.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:58:53.062335Z'
  support: context_only
  summary: Root selected primary, authority and owner scopes; incidental content not
    adopted.
  snapshot_sha256: e036c7e94c431036f1ad7e4e183f00af14789f64258bdc4b819c38bb5edce909
- evidence_id: root-verification
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-source-root/root-current-verification.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T05:04:11.982752Z'
  support: context_only
  summary: Root current input, frozen artifact, qualified history and local review-array
    verification.
  snapshot_sha256: da39400bf788e562d29ecc6ac3d33d9d5894f1fcac5a154c8c9275ad8b8765eb
- evidence_id: adjudication
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-very-low-root-adjudication.json
  locator: Final root adjudication
  accessed_at: '2026-10-22T05:04:11.987141Z'
  support: supports
  summary: Exact one major and three minors, four findings/actions and current owner/field
    scopes control this combined review.
  snapshot_sha256: b34d29077c2b117010433a6a2b683f8d859928f343d3657cf4b5b4743ddb1799
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: active bin, parent and bounded alias interpretation'
  outcome: supported
  target_ids:
  - METPO:1000448
  summary: Active METPO:1000448, direct parent METPO:1000306 and the numeric-temperature/growth-range
    lineage are supported. Raw maximum-inclusive 10 Cel uses generic has-value. Local
    membrane fluidity is a v3 identity absent from captured upstream raw OWL; broad
    v8 confers is retained. Exact biological Psychrophile equivalence remains qualified.
  evidence_ids:
  - identity
  - authority-primary
  - source-identities
  - record
- assessment_id: definition
  area: quantity
  topic: 'Native checklist: internally coherent ambient threshold'
  outcome: supported
  target_ids:
  - METPO:1000448
  summary: Definition, node 0, edge 0, graph description and canonical note use growth
    reaching an ambient threshold at or below approximately 10 °C. The reported -12
    to 10 °C interval supports that use. No interval-width conflict is inherited from
    siblings. Exact inclusive-boundary calibration and broad alias equivalence remain
    qualified; generic has-value alone is not a complete measurement protocol.
  evidence_ids:
  - identity
  - authority-primary
  - canonical
  - canonical-metadata
  - canonical-writer
  - adjudication
- assessment_id: canonical
  area: evidence
  topic: 'Native checklist: existing strain-scoped interval and identity'
  outcome: supported
  target_ids:
  - METPO:1000448
  summary: Successful canonical metadata retry supports Psychromonas ingrahamii strain
    37T, the existing -12 to 10 °C interval and CCUG51855T/CIP108865T aliases. Official
    taxonomy supports identity only. No full curve, optimum or other culture/composition/genomic
    property is adopted. Initial canonical and taxonomy error bytes remain distinct
    from successful retries.
  evidence_ids:
  - canonical
  - canonical-metadata
  - canonical-metadata-access
  - canonical-initial-failure
  - taxonomy
  - taxonomy-reading
  - taxonomy-initial-failure
  - adjudication
- assessment_id: source-support
  area: evidence
  topic: 'Native checklist: five works and seventeen placements'
  outcome: concern
  target_ids:
  - METPO:1000448
  summary: Five identities, selected near-freezing classification and generic physical
    context are supported. Three notes incorrectly attribute body quotations to PubMed
    abstracts. Detailed signaling, regulation, stress defense, survival, fitness,
    cryoprotection, cultivation optimization and intervention efficacy remain unassessed.
    Ramasamy matching establishes six supplied literal spans only; no surrounding
    numerical-strain comparison or mechanistic efficacy is adopted.
  evidence_ids:
  - sources
  - source-identities
  - source-status
  - placements
  - notes
  - source-reading
  - source-access
  - source-locations
  - damico-pdf
  - cold-body
  - phadtare-body
  - antarctic-body
  - adjudication
- assessment_id: quotations
  area: evidence
  topic: 'Native checklist: fifteen literal spans and three body locators'
  outcome: supported
  target_ids:
  - METPO:1000448
  summary: All fifteen schema snippets are literal. Native four VERIFIED and eleven
    NOT_IN_ABSTRACT are distinct, with abstract misses inconclusive for body text.
    Edges 8/9 use Ramón body paragraphs 17/31; edge 10 uses Phadtare body paragraph
    11. Their exact spans are absent from inspected indexed and PMC abstracts. Correcting
    three note locators does not change literal status or establish detailed efficacy.
  evidence_ids:
  - snippets
  - source-native
  - source-locations
  - cold-body
  - phadtare-body
  - antarctic-body
  - damico-text
  - notes
- assessment_id: nodes
  area: representation
  topic: 'Native checklist: all fifteen current referents'
  outcome: concern
  target_ids:
  - METPO:1000448
  summary: The machinery node combines a process type with material enzymes/membranes
    and a functional clause, warranting bounded facet clarification without prescribing
    a replacement enum. RNA secondary structure and membrane fluidity are qualities;
    low temperature is an ambient condition with coherent PATO closeMatch; ice growth
    is processual. Node 6 signaling-system wording remains qualified without an extra
    type finding. Three label-only aggregates require no accession or instance.
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
    causal_graphs[0].nodes[0]\",\n      \"node\": {\n        \"node_id\": \"temperature_range_very_low_trait\"\
    ,\n        \"label\": \"temperature range very low\",\n        \"node_type\":\
    \ \"TRAIT\",\n        \"grounding\": \"METPO:1000448\",\n        \"description\"\
    : \"Temperature growth-supporting range reaching ≤ ~10 °C.\"\n      },\n     \
    \ \"outcome\": \"positive\",\n      \"judgment\": \"Exact active METPO1000448;\
    \ current reach-at-or-below-10 wording agrees internally with canonical threshold\
    \ use. Generic raw numerical property does not independently force width semantics.\"\
    \n    },\n    {\n      \"index\": 1,\n      \"field\": \"causal_graphs[0].nodes[1]\"\
    ,\n      \"node\": {\n        \"node_id\": \"temperature_range\",\n        \"\
    label\": \"temperature range\",\n        \"node_type\": \"TRAIT\",\n        \"\
    grounding\": \"METPO:1000306\",\n        \"description\": \"Span of ambient temperatures\
    \ supporting growth.\"\n      },\n      \"outcome\": \"positive\",\n      \"judgment\"\
    : \"Exact active direct temperature-range parent; parent also has numerical-temperature\
    \ and numerical-growth-range parents.\"\n    },\n    {\n      \"index\": 2,\n\
    \      \"field\": \"causal_graphs[0].nodes[2]\",\n      \"node\": {\n        \"\
    node_id\": \"psychrophile_machinery\",\n        \"label\": \"psychrophile cold-adapted\
    \ machinery\",\n        \"node_type\": \"BIOLOGICAL_PROCESS\",\n        \"description\"\
    : \"Cold-active enzymes and unsaturated-lipid membranes that sustain function\
    \ near freezing.\"\n      },\n      \"outcome\": \"minor\",\n      \"judgment\"\
    : \"BIOLOGICAL_PROCESS contrasts with a machinery label and description enumerating\
    \ material enzymes and membranes. The functional sustaining clause permits a process\
    \ interpretation but does not identify one; bounded referent/facet precision is\
    \ needed without prescribing a replacement enum or mechanism.\"\n    },\n    {\n\
    \      \"index\": 3,\n      \"field\": \"causal_graphs[0].nodes[3]\",\n      \"\
    node\": {\n        \"node_id\": \"low_temperature\",\n        \"label\": \"low\
    \ temperature\",\n        \"node_type\": \"ENVIRONMENTAL_FACTOR\",\n        \"\
    description\": \"Ambient temperature at or below ~10 C imposing cold stress.\"\
    ,\n        \"grounding\": \"PATO:0001306\"\n      },\n      \"outcome\": \"qualified\"\
    ,\n      \"judgment\": \"Actual ambient low-temperature condition is compatible\
    \ ENVIRONMENTAL_FACTOR. PATO1306 relatively-low temperature quality is a declared\
    \ closeMatch condition shorthand, not an event merely because its label says decreased.\
    \ Its use as an imported process-regulator subject is separately inconsistent.\"\
    \n    },\n    {\n      \"index\": 4,\n      \"field\": \"causal_graphs[0].nodes[4]\"\
    ,\n      \"node\": {\n        \"node_id\": \"membrane_fatty_acid_desaturation\"\
    ,\n        \"label\": \"membrane fatty-acid desaturation\",\n        \"node_type\"\
    : \"BIOLOGICAL_PROCESS\",\n        \"description\": \"Introduction of double bonds\
    \ into membrane lipids during cold adaptation.\"\n      },\n      \"outcome\"\
    : \"positive\",\n      \"judgment\": \"Introduction of double bonds is an explicit\
    \ process; no enzyme improvement or biological efficacy judgment.\"\n    },\n\
    \    {\n      \"index\": 5,\n      \"field\": \"causal_graphs[0].nodes[5]\",\n\
    \      \"node\": {\n        \"node_id\": \"membrane_fluidity\",\n        \"label\"\
    : \"membrane fluidity\",\n        \"node_type\": \"QUALITY\",\n        \"description\"\
    : \"Physical fluidity of the membrane bilayer required for function in the cold.\"\
    ,\n        \"grounding\": \"METPO:1007505\"\n      },\n      \"outcome\": \"positive\"\
    ,\n      \"judgment\": \"Physical bilayer fluidity is QUALITY. Exact local v3\
    \ METPO1007505 identity and mapping50 are positive, absent from captured active\
    \ upstream raw OWL.\"\n    },\n    {\n      \"index\": 6,\n      \"field\": \"\
    causal_graphs[0].nodes[6]\",\n      \"node\": {\n        \"node_id\": \"two_component_cold_signaling\"\
    ,\n        \"label\": \"two-component cold signaling\",\n        \"node_type\"\
    : \"BIOLOGICAL_PROCESS\",\n        \"description\": \"Two-component regulatory\
    \ systems triggered by cold-induced membrane state changes.\"\n      },\n    \
    \  \"outcome\": \"qualified\",\n      \"judgment\": \"Signaling label/type denotes\
    \ a process, although description names regulatory systems. Process reading is\
    \ plausible; detailed regulation/fitness efficacy unassessed, no forced material\
    \ retype.\"\n    },\n    {\n      \"index\": 7,\n      \"field\": \"causal_graphs[0].nodes[7]\"\
    ,\n      \"node\": {\n        \"node_id\": \"cold_shock_proteins\",\n        \"\
    label\": \"cold-shock proteins (CspA-family)\",\n        \"node_type\": \"GENE_OR_PROTEIN\"\
    ,\n        \"grounding_status\": \"REVIEWED_LABEL_ONLY\",\n        \"grounding_notes\"\
    : \"Reviewed as a contextual protein or protein-complex label within a quantitative\
    \ measurement graph; no exact semantic family term was established for this aggregate\
    \ use.\",\n        \"description\": \"CspA-family RNA chaperones that bind nucleic\
    \ acids during cold acclimation.\"\n      },\n      \"outcome\": \"positive\"\
    ,\n      \"judgment\": \"Explicit protein-family material, reviewed label-only\
    \ with rationale. No required accession or instance; detailed RNA chaperoning\
    \ efficacy unassessed.\"\n    },\n    {\n      \"index\": 8,\n      \"field\"\
    : \"causal_graphs[0].nodes[8]\",\n      \"node\": {\n        \"node_id\": \"cold_stabilized_rna_secondary_structure\"\
    ,\n        \"label\": \"cold-stabilized mRNA/RNA secondary structure\",\n    \
    \    \"node_type\": \"QUALITY\",\n        \"description\": \"Cold-stabilized RNA\
    \ secondary structures impeding translation.\"\n      },\n      \"outcome\": \"\
    positive\",\n      \"judgment\": \"Cold-stabilized RNA secondary structure is\
    \ a quality of material RNA, not RNA as chemical substance. Current corrective\
    \ node identity/type and history are coherent.\"\n    },\n    {\n      \"index\"\
    : 9,\n      \"field\": \"causal_graphs[0].nodes[9]\",\n      \"node\": {\n   \
    \     \"node_id\": \"molecular_chaperones\",\n        \"label\": \"molecular chaperones\
    \ (DnaK/GroEL/GroES/Clp/TF)\",\n        \"node_type\": \"GENE_OR_PROTEIN\",\n\
    \        \"grounding_status\": \"REVIEWED_LABEL_ONLY\",\n        \"grounding_notes\"\
    : \"Reviewed as a contextual protein or protein-complex label within a quantitative\
    \ measurement graph; no exact semantic family term was established for this aggregate\
    \ use.\",\n        \"description\": \"Chaperone and protease systems maintaining\
    \ proteostasis under cold.\"\n      },\n      \"outcome\": \"positive\",\n   \
    \   \"judgment\": \"Explicit material chaperone/protease systems, reviewed label-only;\
    \ functional description does not itself force a process retype.\"\n    },\n \
    \   {\n      \"index\": 10,\n      \"field\": \"causal_graphs[0].nodes[10]\",\n\
    \      \"node\": {\n        \"node_id\": \"proteostasis_cold\",\n        \"label\"\
    : \"protein folding and proteostasis in the cold\",\n        \"node_type\": \"\
    BIOLOGICAL_PROCESS\",\n        \"description\": \"Maintenance of correct protein\
    \ folding despite cold-slowed folding kinetics.\"\n      },\n      \"outcome\"\
    : \"positive\",\n      \"judgment\": \"Folding and maintenance denote processes.\
    \ Detailed cold proteostasis efficacy is outside review scope.\"\n    },\n   \
    \ {\n      \"index\": 11,\n      \"field\": \"causal_graphs[0].nodes[11]\",\n\
    \      \"node\": {\n        \"node_id\": \"compatible_solutes\",\n        \"label\"\
    : \"compatible solutes (glycine betaine/trehalose/glycerol)\",\n        \"node_type\"\
    : \"CHEMICAL\",\n        \"description\": \"Osmolytes that lower freezing damage\
    \ and stabilize macromolecules.\"\n      },\n      \"outcome\": \"positive\",\n\
    \      \"judgment\": \"Examples identify material compatible-solute chemicals.\
    \ No populated CHEBI role grounding to misread as exact substance identity.\"\n\
    \    },\n    {\n      \"index\": 12,\n      \"field\": \"causal_graphs[0].nodes[12]\"\
    ,\n      \"node\": {\n        \"node_id\": \"protein_membrane_stabilization\"\
    ,\n        \"label\": \"protein and membrane stabilization\",\n        \"node_type\"\
    : \"BIOLOGICAL_PROCESS\",\n        \"description\": \"Stabilization of proteins\
    \ and membranes against cold/freezing damage.\"\n      },\n      \"outcome\":\
    \ \"positive\",\n      \"judgment\": \"Stabilization denotes processual activity;\
    \ detailed cryoprotection or intervention support unassessed.\"\n    },\n    {\n\
    \      \"index\": 13,\n      \"field\": \"causal_graphs[0].nodes[13]\",\n    \
    \  \"node\": {\n        \"node_id\": \"ice_binding_proteins\",\n        \"label\"\
    : \"ice-binding/antifreeze proteins\",\n        \"node_type\": \"GENE_OR_PROTEIN\"\
    ,\n        \"grounding_status\": \"REVIEWED_LABEL_ONLY\",\n        \"grounding_notes\"\
    : \"Reviewed as a contextual protein or protein-complex label within a quantitative\
    \ measurement graph; no exact semantic family term was established for this aggregate\
    \ use.\",\n        \"description\": \"AFPs/IBPs that bind ice and inhibit ice-crystal\
    \ growth.\"\n      },\n      \"outcome\": \"positive\",\n      \"judgment\": \"\
    Explicit material ice-binding protein aggregate, reviewed label-only. No invented\
    \ accession or efficacy claim.\"\n    },\n    {\n      \"index\": 14,\n      \"\
    field\": \"causal_graphs[0].nodes[14]\",\n      \"node\": {\n        \"node_id\"\
    : \"ice_crystal_growth\",\n        \"label\": \"ice-crystal growth/recrystallization\"\
    ,\n        \"node_type\": \"BIOLOGICAL_PROCESS\",\n        \"description\": \"\
    Damaging ice-crystal growth and recrystallization around cells.\"\n      },\n\
    \      \"outcome\": \"positive\",\n      \"judgment\": \"Ice growth/recrystallization\
    \ is a physical process compatible with imported BFO process range. BIOLOGICAL_PROCESS\
    \ enum context does not independently establish a defect merely because the process\
    \ is physical.\"\n    }\n  ],\n  \"source\": [\n    {\n      \"index\": 0,\n \
    \     \"field\": \"causal_graphs[0].nodes[0]\",\n      \"node\": {\n        \"\
    node_id\": \"temperature_range_very_low_trait\",\n        \"label\": \"temperature\
    \ range very low\",\n        \"node_type\": \"TRAIT\",\n        \"grounding\"\
    : \"METPO:1000448\",\n        \"description\": \"Temperature growth-supporting\
    \ range reaching ≤ ~10 °C.\"\n      },\n      \"disposition\": \"PARTIAL\",\n\
    \      \"scope\": \"Threshold interpretation consistent with canonical; boundary\
    \ authority qualified.\"\n    },\n    {\n      \"index\": 1,\n      \"field\"\
    : \"causal_graphs[0].nodes[1]\",\n      \"node\": {\n        \"node_id\": \"temperature_range\"\
    ,\n        \"label\": \"temperature range\",\n        \"node_type\": \"TRAIT\"\
    ,\n        \"grounding\": \"METPO:1000306\",\n        \"description\": \"Span\
    \ of ambient temperatures supporting growth.\"\n      },\n      \"disposition\"\
    : \"SUPPORTED\",\n      \"scope\": \"Generic measured growth interval context.\"\
    \n    },\n    {\n      \"index\": 2,\n      \"field\": \"causal_graphs[0].nodes[2]\"\
    ,\n      \"node\": {\n        \"node_id\": \"psychrophile_machinery\",\n     \
    \   \"label\": \"psychrophile cold-adapted machinery\",\n        \"node_type\"\
    : \"BIOLOGICAL_PROCESS\",\n        \"description\": \"Cold-active enzymes and\
    \ unsaturated-lipid membranes that sustain function near freezing.\"\n      },\n\
    \      \"disposition\": \"UNASSESSED_SCOPE\",\n      \"scope\": \"Existing contextual\
    \ label/description preserved; detailed molecular regulation/protection/fitness/survival\
    \ efficacy unassessed.\"\n    },\n    {\n      \"index\": 3,\n      \"field\"\
    : \"causal_graphs[0].nodes[3]\",\n      \"node\": {\n        \"node_id\": \"low_temperature\"\
    ,\n        \"label\": \"low temperature\",\n        \"node_type\": \"ENVIRONMENTAL_FACTOR\"\
    ,\n        \"description\": \"Ambient temperature at or below ~10 C imposing cold\
    \ stress.\",\n        \"grounding\": \"PATO:0001306\"\n      },\n      \"disposition\"\
    : \"PARTIAL\",\n      \"scope\": \"Generic low-temperature condition; exact10\
    \ calibration qualified.\"\n    },\n    {\n      \"index\": 4,\n      \"field\"\
    : \"causal_graphs[0].nodes[4]\",\n      \"node\": {\n        \"node_id\": \"membrane_fatty_acid_desaturation\"\
    ,\n        \"label\": \"membrane fatty-acid desaturation\",\n        \"node_type\"\
    : \"BIOLOGICAL_PROCESS\",\n        \"description\": \"Introduction of double bonds\
    \ into membrane lipids during cold adaptation.\"\n      },\n      \"disposition\"\
    : \"PARTIAL\",\n      \"scope\": \"Generic composition context only; detailed\
    \ adaptation efficacy unassessed.\"\n    },\n    {\n      \"index\": 5,\n    \
    \  \"field\": \"causal_graphs[0].nodes[5]\",\n      \"node\": {\n        \"node_id\"\
    : \"membrane_fluidity\",\n        \"label\": \"membrane fluidity\",\n        \"\
    node_type\": \"QUALITY\",\n        \"description\": \"Physical fluidity of the\
    \ membrane bilayer required for function in the cold.\",\n        \"grounding\"\
    : \"METPO:1007505\"\n      },\n      \"disposition\": \"PARTIAL\",\n      \"scope\"\
    : \"Generic membrane phase/fluidity context only; efficacy unassessed.\"\n   \
    \ },\n    {\n      \"index\": 6,\n      \"field\": \"causal_graphs[0].nodes[6]\"\
    ,\n      \"node\": {\n        \"node_id\": \"two_component_cold_signaling\",\n\
    \        \"label\": \"two-component cold signaling\",\n        \"node_type\":\
    \ \"BIOLOGICAL_PROCESS\",\n        \"description\": \"Two-component regulatory\
    \ systems triggered by cold-induced membrane state changes.\"\n      },\n    \
    \  \"disposition\": \"UNASSESSED_SCOPE\",\n      \"scope\": \"Existing contextual\
    \ label/description preserved; detailed molecular regulation/protection/fitness/survival\
    \ efficacy unassessed.\"\n    },\n    {\n      \"index\": 7,\n      \"field\"\
    : \"causal_graphs[0].nodes[7]\",\n      \"node\": {\n        \"node_id\": \"cold_shock_proteins\"\
    ,\n        \"label\": \"cold-shock proteins (CspA-family)\",\n        \"node_type\"\
    : \"GENE_OR_PROTEIN\",\n        \"grounding_status\": \"REVIEWED_LABEL_ONLY\"\
    ,\n        \"grounding_notes\": \"Reviewed as a contextual protein or protein-complex\
    \ label within a quantitative measurement graph; no exact semantic family term\
    \ was established for this aggregate use.\",\n        \"description\": \"CspA-family\
    \ RNA chaperones that bind nucleic acids during cold acclimation.\"\n      },\n\
    \      \"disposition\": \"UNASSESSED_SCOPE\",\n      \"scope\": \"Existing contextual\
    \ label/description preserved; detailed molecular regulation/protection/fitness/survival\
    \ efficacy unassessed.\"\n    },\n    {\n      \"index\": 8,\n      \"field\"\
    : \"causal_graphs[0].nodes[8]\",\n      \"node\": {\n        \"node_id\": \"cold_stabilized_rna_secondary_structure\"\
    ,\n        \"label\": \"cold-stabilized mRNA/RNA secondary structure\",\n    \
    \    \"node_type\": \"QUALITY\",\n        \"description\": \"Cold-stabilized RNA\
    \ secondary structures impeding translation.\"\n      },\n      \"disposition\"\
    : \"UNASSESSED_SCOPE\",\n      \"scope\": \"Existing contextual label/description\
    \ preserved; detailed molecular regulation/protection/fitness/survival efficacy\
    \ unassessed.\"\n    },\n    {\n      \"index\": 9,\n      \"field\": \"causal_graphs[0].nodes[9]\"\
    ,\n      \"node\": {\n        \"node_id\": \"molecular_chaperones\",\n       \
    \ \"label\": \"molecular chaperones (DnaK/GroEL/GroES/Clp/TF)\",\n        \"node_type\"\
    : \"GENE_OR_PROTEIN\",\n        \"grounding_status\": \"REVIEWED_LABEL_ONLY\"\
    ,\n        \"grounding_notes\": \"Reviewed as a contextual protein or protein-complex\
    \ label within a quantitative measurement graph; no exact semantic family term\
    \ was established for this aggregate use.\",\n        \"description\": \"Chaperone\
    \ and protease systems maintaining proteostasis under cold.\"\n      },\n    \
    \  \"disposition\": \"UNASSESSED_SCOPE\",\n      \"scope\": \"Existing contextual\
    \ label/description preserved; detailed molecular regulation/protection/fitness/survival\
    \ efficacy unassessed.\"\n    },\n    {\n      \"index\": 10,\n      \"field\"\
    : \"causal_graphs[0].nodes[10]\",\n      \"node\": {\n        \"node_id\": \"\
    proteostasis_cold\",\n        \"label\": \"protein folding and proteostasis in\
    \ the cold\",\n        \"node_type\": \"BIOLOGICAL_PROCESS\",\n        \"description\"\
    : \"Maintenance of correct protein folding despite cold-slowed folding kinetics.\"\
    \n      },\n      \"disposition\": \"UNASSESSED_SCOPE\",\n      \"scope\": \"\
    Existing contextual label/description preserved; detailed molecular regulation/protection/fitness/survival\
    \ efficacy unassessed.\"\n    },\n    {\n      \"index\": 11,\n      \"field\"\
    : \"causal_graphs[0].nodes[11]\",\n      \"node\": {\n        \"node_id\": \"\
    compatible_solutes\",\n        \"label\": \"compatible solutes (glycine betaine/trehalose/glycerol)\"\
    ,\n        \"node_type\": \"CHEMICAL\",\n        \"description\": \"Osmolytes\
    \ that lower freezing damage and stabilize macromolecules.\"\n      },\n     \
    \ \"disposition\": \"UNASSESSED_SCOPE\",\n      \"scope\": \"Existing contextual\
    \ label/description preserved; detailed molecular regulation/protection/fitness/survival\
    \ efficacy unassessed.\"\n    },\n    {\n      \"index\": 12,\n      \"field\"\
    : \"causal_graphs[0].nodes[12]\",\n      \"node\": {\n        \"node_id\": \"\
    protein_membrane_stabilization\",\n        \"label\": \"protein and membrane stabilization\"\
    ,\n        \"node_type\": \"BIOLOGICAL_PROCESS\",\n        \"description\": \"\
    Stabilization of proteins and membranes against cold/freezing damage.\"\n    \
    \  },\n      \"disposition\": \"UNASSESSED_SCOPE\",\n      \"scope\": \"Existing\
    \ contextual label/description preserved; detailed molecular regulation/protection/fitness/survival\
    \ efficacy unassessed.\"\n    },\n    {\n      \"index\": 13,\n      \"field\"\
    : \"causal_graphs[0].nodes[13]\",\n      \"node\": {\n        \"node_id\": \"\
    ice_binding_proteins\",\n        \"label\": \"ice-binding/antifreeze proteins\"\
    ,\n        \"node_type\": \"GENE_OR_PROTEIN\",\n        \"grounding_status\":\
    \ \"REVIEWED_LABEL_ONLY\",\n        \"grounding_notes\": \"Reviewed as a contextual\
    \ protein or protein-complex label within a quantitative measurement graph; no\
    \ exact semantic family term was established for this aggregate use.\",\n    \
    \    \"description\": \"AFPs/IBPs that bind ice and inhibit ice-crystal growth.\"\
    \n      },\n      \"disposition\": \"UNASSESSED_SCOPE\",\n      \"scope\": \"\
    Existing contextual label/description preserved; detailed molecular regulation/protection/fitness/survival\
    \ efficacy unassessed.\"\n    },\n    {\n      \"index\": 14,\n      \"field\"\
    : \"causal_graphs[0].nodes[14]\",\n      \"node\": {\n        \"node_id\": \"\
    ice_crystal_growth\",\n        \"label\": \"ice-crystal growth/recrystallization\"\
    ,\n        \"node_type\": \"BIOLOGICAL_PROCESS\",\n        \"description\": \"\
    Damaging ice-crystal growth and recrystallization around cells.\"\n      },\n\
    \      \"disposition\": \"UNASSESSED_SCOPE\",\n      \"scope\": \"Existing contextual\
    \ label/description preserved; detailed molecular regulation/protection/fitness/survival\
    \ efficacy unassessed.\"\n    }\n  ]\n}"
- assessment_id: relations
  area: consistency
  topic: 'Native checklist: all fourteen current relations'
  outcome: concern
  target_ids:
  - METPO:1000448
  summary: 'One formal-role major covers edges 2/3/4/7: imported process regulation
    conflicts with quality, ambient-condition or material-protein endpoints. Edge
    7 has a compatible physical process object. RO2326 material-to-process fit at
    edges 5/6 remains positive without efficacy endorsement. Broad local confers,
    exact subclass and Biolink association roles remain compatible or qualified; no
    statistical association or benefit is inferred. No biological replacement or intermediary
    is prescribed.'
  evidence_ids:
  - nodes-edges
  - source-nodes-edges
  - ontology-primary
  - authority-primary
  - local-authority
  - adjudication
  details: "{\n  \"grounding\": [\n    {\n      \"index\": 0,\n      \"field\": \"\
    causal_graphs[0].edges[0]\",\n      \"edge\": {\n        \"subject\": \"psychrophile_machinery\"\
    ,\n        \"predicate\": \"confers\",\n        \"object\": \"temperature_range_very_low_trait\"\
    ,\n        \"description\": \"Psychrophile cold-adapted machinery enables growth\
    \ at ≤ 10 °C.\",\n        \"evidence\": [\n          {\n            \"reference\"\
    : \"DOI:10.1038/sj.embor.7400662\",\n            \"snippet\": \"decreased membrane\
    \ fluidity\",\n            \"notes\": \"Supports cold-adapted membranes and enzymes\
    \ as enablers of growth at very low temperatures.\"\n          }\n        ],\n\
    \        \"predicate_id\": \"METPO:2007700\"\n      },\n      \"outcome\": \"\
    qualified\",\n      \"judgment\": \"Local v8 confers accepts broad causal-node\
    \ endpoints and trait object. Mixed subject facet and detailed causal sufficiency\
    \ remain qualified; no hard imported endpoint failure.\"\n    },\n    {\n    \
    \  \"index\": 1,\n      \"field\": \"causal_graphs[0].edges[1]\",\n      \"edge\"\
    : {\n        \"subject\": \"temperature_range_very_low_trait\",\n        \"predicate\"\
    : \"is a\",\n        \"object\": \"temperature_range\",\n        \"description\"\
    : \"Temperature range very low is a quantitative bin of the temperature-range\
    \ phenotype.\",\n        \"evidence\": [\n          {\n            \"reference\"\
    : \"DOI:10.1038/sj.embor.7400662\",\n            \"snippet\": \"growing well at\
    \ temperatures around the freezing point of water\",\n            \"notes\": \"\
    Supports a ≤10 °C range as a value within the temperature-range distribution.\"\
    \n          }\n        ],\n        \"predicate_id\": \"rdfs:subClassOf\"\n   \
    \   },\n      \"outcome\": \"positive\",\n      \"judgment\": \"rdfs:subClassOf\
    \ agrees with current exact active raw child/direct-parent hierarchy.\"\n    },\n\
    \    {\n      \"index\": 2,\n      \"field\": \"causal_graphs[0].edges[2]\",\n\
    \      \"edge\": {\n        \"subject\": \"membrane_fatty_acid_desaturation\"\
    ,\n        \"predicate\": \"increases\",\n        \"object\": \"membrane_fluidity\"\
    ,\n        \"description\": \"Homeoviscous adaptation via lipid desaturation maintains\
    \ membrane fluidity in the cold.\",\n        \"evidence\": [\n          {\n  \
    \          \"reference\": \"DOI:10.1007/s42770-023-01057-4\",\n            \"\
    snippet\": \"production of double bonds in lipids\",\n            \"notes\": \"\
    Verified against the open Ramón et al. PubMed abstract; the multifactorial cold-adaptation\
    \ model lists membrane composition adaptation by producing lipid double bonds.\"\
    \n          }\n        ],\n        \"predicate_id\": \"RO:0002213\"\n      },\n\
    \      \"outcome\": \"major\",\n      \"judgment\": \"RO2213 inherits RO2211 process/process.\
    \ Explicit desaturation process fits subject, but membrane-fluidity QUALITY fails\
    \ process range.\"\n    },\n    {\n      \"index\": 3,\n      \"field\": \"causal_graphs[0].edges[3]\"\
    ,\n      \"edge\": {\n        \"subject\": \"low_temperature\",\n        \"predicate\"\
    : \"activates\",\n        \"object\": \"two_component_cold_signaling\",\n    \
    \    \"description\": \"Cold-induced membrane state changes activate two-component\
    \ cold signaling.\",\n        \"evidence\": [\n          {\n            \"reference\"\
    : \"DOI:10.1007/s42770-023-01057-4\",\n            \"snippet\": \"activation of\
    \ a two-component system\",\n            \"notes\": \"Verified against the open\
    \ Ramón et al. PubMed abstract; cold sensing is described as occurring mainly\
    \ through liquid-crystalline membrane-state changes that activate a two-component\
    \ signal-transduction system.\"\n          }\n        ],\n        \"predicate_id\"\
    : \"RO:0002213\"\n      },\n      \"outcome\": \"major\",\n      \"judgment\"\
    : \"RO2213 requires process/process. Current subject explicitly denotes an ambient\
    \ low-temperature condition, not a temperature-drop event; object signaling process\
    \ is compatible. Finding follows actual referent and PATO quality context, not\
    \ the ENV enum alone.\"\n    },\n    {\n      \"index\": 4,\n      \"field\":\
    \ \"causal_graphs[0].edges[4]\",\n      \"edge\": {\n        \"subject\": \"cold_shock_proteins\"\
    ,\n        \"predicate\": \"regulates\",\n        \"object\": \"cold_stabilized_rna_secondary_structure\"\
    ,\n        \"description\": \"CspA-family RNA chaperones regulate cold-stabilized\
    \ RNA structures to sustain translation.\",\n        \"evidence\": [\n       \
    \   {\n            \"reference\": \"DOI:10.4161/rna.7.6.13482\",\n           \
    \ \"snippet\": \"through their RNA chaperoning function\",\n            \"notes\"\
    : \"Verified against the open Phadtare and Severinov PubMed abstract; CspA-family\
    \ cold-shock proteins are described as RNA-modulating proteins affecting low-temperature\
    \ transcription and possibly translation through RNA chaperoning.\"\n        \
    \  }\n        ],\n        \"predicate_id\": \"RO:0002211\"\n      },\n      \"\
    outcome\": \"major\",\n      \"judgment\": \"RO2211 process/process conflicts\
    \ with explicit material protein subject and RNA secondary-structure QUALITY object.\
    \ No biological mechanism repair proposed.\"\n    },\n    {\n      \"index\":\
    \ 5,\n      \"field\": \"causal_graphs[0].edges[5]\",\n      \"edge\": {\n   \
    \     \"subject\": \"molecular_chaperones\",\n        \"predicate\": \"contributes\
    \ to\",\n        \"object\": \"proteostasis_cold\",\n        \"description\":\
    \ \"Chaperone/protease systems contribute to proteostasis by countering cold-slowed\
    \ folding and misfolding risk.\",\n        \"evidence\": [\n          {\n    \
    \        \"reference\": \"DOI:10.3389/fmicb.2023.1197797\",\n            \"snippet\"\
    : \"heat shock proteins associated to folding\",\n            \"notes\": \"Verified\
    \ against the open Ramasamy et al. PMC text; the Antarctic psychrophile review\
    \ discusses heat-shock proteins associated with protein folding in 4 °C versus\
    \ 18 °C Pseudoalteromonas haloplanktis TAC125.\"\n          }\n        ],\n  \
    \      \"predicate_id\": \"RO:0002326\"\n      },\n      \"outcome\": \"qualified\"\
    ,\n      \"judgment\": \"RO2326 through2216/2500/2595 has material domain/process\
    \ range. Protein-system material to proteostasis process fits formal endpoints;\
    \ detailed participation/function and efficacy remain unassessed. GO-specific\
    \ molecular-function annotation guidance is not imposed as a universal range.\"\
    \n    },\n    {\n      \"index\": 6,\n      \"field\": \"causal_graphs[0].edges[6]\"\
    ,\n      \"edge\": {\n        \"subject\": \"compatible_solutes\",\n        \"\
    predicate\": \"contributes to\",\n        \"object\": \"protein_membrane_stabilization\"\
    ,\n        \"description\": \"Osmolytes contribute to protein and membrane stabilization\
    \ while lowering freezing damage.\",\n        \"evidence\": [\n          {\n \
    \           \"reference\": \"DOI:10.3389/fmicb.2023.1197797\",\n            \"\
    snippet\": \"counteracting protein aggregation, improving protein folding\",\n\
    \            \"notes\": \"Verified against the open Ramasamy et al. PMC text;\
    \ Antarctic compatible osmolytes are described as counteracting protein aggregation\
    \ and improving protein folding.\"\n          }\n        ],\n        \"predicate_id\"\
    : \"RO:0002326\"\n      },\n      \"outcome\": \"qualified\",\n      \"judgment\"\
    : \"RO2326 material-to-process endpoints fit explicit solute chemicals and stabilization\
    \ activity. Formal fit is not an efficacy or intervention endorsement.\"\n   \
    \ },\n    {\n      \"index\": 7,\n      \"field\": \"causal_graphs[0].edges[7]\"\
    ,\n      \"edge\": {\n        \"subject\": \"ice_binding_proteins\",\n       \
    \ \"predicate\": \"inhibits\",\n        \"object\": \"ice_crystal_growth\",\n\
    \        \"description\": \"AFPs/IBPs bind ice and inhibit ice-crystal growth\
    \ and recrystallization.\",\n        \"evidence\": [\n          {\n          \
    \  \"reference\": \"DOI:10.3389/fmicb.2023.1197797\",\n            \"snippet\"\
    : \"inhibits the growth of ice crystals\",\n            \"notes\": \"Verified\
    \ against the open Ramasamy et al. PMC text; ice binding proteins are described\
    \ as antifreeze proteins that bind ice, inhibit ice-crystal growth, lower freezing\
    \ temperature, create a thermal hysteresis gap, and display ice-recrystallization\
    \ inhibition activity.\"\n          }\n        ],\n        \"predicate_id\": \"\
    RO:0002212\"\n      },\n      \"outcome\": \"major\",\n      \"judgment\": \"\
    RO2212 inherits process/process fromRO2211. Ice-binding proteins are material\
    \ subjects; physical ice growth is process-compatible object. No object fault\
    \ inferred solely from physical-process context.\"\n    },\n    {\n      \"index\"\
    : 8,\n      \"field\": \"causal_graphs[0].edges[8]\",\n      \"edge\": {\n   \
    \     \"subject\": \"membrane_fluidity\",\n        \"predicate\": \"associated\
    \ with\",\n        \"object\": \"psychrophile_machinery\",\n        \"description\"\
    : \"Membrane fatty-acid desaturation is associated with the cold-adapted machinery\
    \ supporting psychrophile growth ranges.\",\n        \"evidence\": [\n       \
    \   {\n            \"reference\": \"DOI:10.1007/s42770-023-01057-4\",\n      \
    \      \"snippet\": \"maintain the liquid crystalline phase\",\n            \"\
    notes\": \"Verified against the open Ramón et al. PubMed abstract; this connector\
    \ keeps membrane desaturation as cold membrane-adaptation context.\"\n       \
    \   }\n        ],\n        \"predicate_id\": \"biolink:associated_with\"\n   \
    \   },\n      \"outcome\": \"qualified\",\n      \"judgment\": \"Biolink associated_with\
    \ has broad named-thing endpoints and admits related proxy entities. Current quality\
    \ source versus desaturation-process description is retained as a scope/precision\
    \ qualification; no automatic RO domain import or separate forced mechanism finding.\"\
    \n    },\n    {\n      \"index\": 9,\n      \"field\": \"causal_graphs[0].edges[9]\"\
    ,\n      \"edge\": {\n        \"subject\": \"two_component_cold_signaling\",\n\
    \        \"predicate\": \"associated with\",\n        \"object\": \"psychrophile_machinery\"\
    ,\n        \"description\": \"Two-component cold signaling is associated with\
    \ psychrophile cold-adapted machinery.\",\n        \"evidence\": [\n         \
    \ {\n            \"reference\": \"DOI:10.1007/s42770-023-01057-4\",\n        \
    \    \"snippet\": \"When the temperature drops, DesK/DesR is the two-component\
    \ system involved in membrane adaptation\",\n            \"notes\": \"Verified\
    \ against the open Ramón et al. PubMed abstract; this connector keeps low-temperature\
    \ membrane sensing as cold-acclimation context.\"\n          }\n        ],\n \
    \       \"predicate_id\": \"biolink:associated_with\"\n      },\n      \"outcome\"\
    : \"qualified\",\n      \"judgment\": \"Broad Biolink association allows signaling-process/context\
    \ relation; detailed cold-regulation efficacy unassessed.\"\n    },\n    {\n \
    \     \"index\": 10,\n      \"field\": \"causal_graphs[0].edges[10]\",\n     \
    \ \"edge\": {\n        \"subject\": \"cold_stabilized_rna_secondary_structure\"\
    ,\n        \"predicate\": \"associated with\",\n        \"object\": \"psychrophile_machinery\"\
    ,\n        \"description\": \"CspA-family regulation of cold-stabilized RNA structure\
    \ is associated with psychrophile cold-adapted machinery.\",\n        \"evidence\"\
    : [\n          {\n            \"reference\": \"DOI:10.4161/rna.7.6.13482\",\n\
    \            \"snippet\": \"CspA, the main cold shock protein, and its homologs\
    \ act as RNA chaperones\",\n            \"notes\": \"Verified against the open\
    \ Phadtare and Severinov PubMed abstract; this connector keeps CspA-family RNA\
    \ chaperones as low-temperature transcript context.\"\n          }\n        ],\n\
    \        \"predicate_id\": \"biolink:associated_with\"\n      },\n      \"outcome\"\
    : \"qualified\",\n      \"judgment\": \"Broad Biolink association permits the\
    \ structural-quality proxy in contextual relation. Description references the\
    \ regulating process rather than asserting a new exact material identity; keep\
    \ scope qualified without imported process-domain claim.\"\n    },\n    {\n  \
    \    \"index\": 11,\n      \"field\": \"causal_graphs[0].edges[11]\",\n      \"\
    edge\": {\n        \"subject\": \"proteostasis_cold\",\n        \"predicate\"\
    : \"associated with\",\n        \"object\": \"psychrophile_machinery\",\n    \
    \    \"description\": \"Cold proteostasis support is associated with the psychrophile\
    \ machinery context.\",\n        \"evidence\": [\n          {\n            \"\
    reference\": \"DOI:10.3389/fmicb.2023.1197797\",\n            \"snippet\": \"\
    ice binding, cold shock and heat shock proteins to sustain their physiological\
    \ state\",\n            \"notes\": \"Verified against the open Ramasamy et al.\
    \ PMC text; this connector keeps chaperone/protease systems as protein-folding\
    \ context.\"\n          }\n        ],\n        \"predicate_id\": \"biolink:associated_with\"\
    \n      },\n      \"outcome\": \"qualified\",\n      \"judgment\": \"Broad Biolink\
    \ association fits process/context endpoints; detailed efficacy and statistical\
    \ dependence are not newly established.\"\n    },\n    {\n      \"index\": 12,\n\
    \      \"field\": \"causal_graphs[0].edges[12]\",\n      \"edge\": {\n       \
    \ \"subject\": \"protein_membrane_stabilization\",\n        \"predicate\": \"\
    associated with\",\n        \"object\": \"psychrophile_machinery\",\n        \"\
    description\": \"Compatible-solute stabilization is associated with psychrophile\
    \ cold-adapted machinery.\",\n        \"evidence\": [\n          {\n         \
    \   \"reference\": \"DOI:10.3389/fmicb.2023.1197797\",\n            \"snippet\"\
    : \"scavenging free radicals, counteracting protein aggregation\",\n         \
    \   \"notes\": \"Verified against the open Ramasamy et al. PMC text; this connector\
    \ keeps compatible osmolytes as stabilization context.\"\n          }\n      \
    \  ],\n        \"predicate_id\": \"biolink:associated_with\"\n      },\n     \
    \ \"outcome\": \"qualified\",\n      \"judgment\": \"Broad Biolink association\
    \ fits stabilization-process/context endpoints; detailed biological support unassessed.\"\
    \n    },\n    {\n      \"index\": 13,\n      \"field\": \"causal_graphs[0].edges[13]\"\
    ,\n      \"edge\": {\n        \"subject\": \"ice_crystal_growth\",\n        \"\
    predicate\": \"associated with\",\n        \"object\": \"psychrophile_machinery\"\
    ,\n        \"description\": \"Ice-binding protein inhibition of ice-crystal growth\
    \ is associated with psychrophile cold-adapted machinery.\",\n        \"evidence\"\
    : [\n          {\n            \"reference\": \"DOI:10.3389/fmicb.2023.1197797\"\
    ,\n            \"snippet\": \"This ceases ice growth by creating a thermal hysteresis\
    \ gap\",\n            \"notes\": \"Verified against the open Ramasamy et al. PMC\
    \ text; this connector keeps ice-binding proteins as freezing-protection context.\"\
    \n          }\n        ],\n        \"predicate_id\": \"biolink:associated_with\"\
    \n      },\n      \"outcome\": \"qualified\",\n      \"judgment\": \"Broad Biolink\
    \ association admits physical process/context proxies; description attributes\
    \ protein-mediated context, with no new efficacy endorsement or imported RO exclusion.\"\
    \n    }\n  ],\n  \"source\": [\n    {\n      \"index\": 0,\n      \"field\": \"\
    causal_graphs[0].edges[0]\",\n      \"edge\": {\n        \"subject\": \"psychrophile_machinery\"\
    ,\n        \"predicate\": \"confers\",\n        \"object\": \"temperature_range_very_low_trait\"\
    ,\n        \"description\": \"Psychrophile cold-adapted machinery enables growth\
    \ at ≤ 10 °C.\",\n        \"evidence\": [\n          {\n            \"reference\"\
    : \"DOI:10.1038/sj.embor.7400662\",\n            \"snippet\": \"decreased membrane\
    \ fluidity\",\n            \"notes\": \"Supports cold-adapted membranes and enzymes\
    \ as enablers of growth at very low temperatures.\"\n          }\n        ],\n\
    \        \"predicate_id\": \"METPO:2007700\"\n      },\n      \"disposition\"\
    : \"PARTIAL\",\n      \"scope\": \"Generic cold membrane-fluidity context positive;\
    \ whole-machinery efficacy at exact threshold UNASSESSED_SCOPE.\"\n    },\n  \
    \  {\n      \"index\": 1,\n      \"field\": \"causal_graphs[0].edges[1]\",\n \
    \     \"edge\": {\n        \"subject\": \"temperature_range_very_low_trait\",\n\
    \        \"predicate\": \"is a\",\n        \"object\": \"temperature_range\",\n\
    \        \"description\": \"Temperature range very low is a quantitative bin of\
    \ the temperature-range phenotype.\",\n        \"evidence\": [\n          {\n\
    \            \"reference\": \"DOI:10.1038/sj.embor.7400662\",\n            \"\
    snippet\": \"growing well at temperatures around the freezing point of water\"\
    ,\n            \"notes\": \"Supports a ≤10 °C range as a value within the temperature-range\
    \ distribution.\"\n          }\n        ],\n        \"predicate_id\": \"rdfs:subClassOf\"\
    \n      },\n      \"disposition\": \"PARTIAL\",\n      \"scope\": \"Broad near-freezing\
    \ classification positive; exact10 cutoff not calibrated by selected passage alone.\"\
    \n    },\n    {\n      \"index\": 2,\n      \"field\": \"causal_graphs[0].edges[2]\"\
    ,\n      \"edge\": {\n        \"subject\": \"membrane_fatty_acid_desaturation\"\
    ,\n        \"predicate\": \"increases\",\n        \"object\": \"membrane_fluidity\"\
    ,\n        \"description\": \"Homeoviscous adaptation via lipid desaturation maintains\
    \ membrane fluidity in the cold.\",\n        \"evidence\": [\n          {\n  \
    \          \"reference\": \"DOI:10.1007/s42770-023-01057-4\",\n            \"\
    snippet\": \"production of double bonds in lipids\",\n            \"notes\": \"\
    Verified against the open Ramón et al. PubMed abstract; the multifactorial cold-adaptation\
    \ model lists membrane composition adaptation by producing lipid double bonds.\"\
    \n          }\n        ],\n        \"predicate_id\": \"RO:0002213\"\n      },\n\
    \      \"disposition\": \"PARTIAL\",\n      \"scope\": \"Generic lipid composition\
    \ context and phrase positive; detailed regulation/efficacy unassessed.\"\n  \
    \  },\n    {\n      \"index\": 3,\n      \"field\": \"causal_graphs[0].edges[3]\"\
    ,\n      \"edge\": {\n        \"subject\": \"low_temperature\",\n        \"predicate\"\
    : \"activates\",\n        \"object\": \"two_component_cold_signaling\",\n    \
    \    \"description\": \"Cold-induced membrane state changes activate two-component\
    \ cold signaling.\",\n        \"evidence\": [\n          {\n            \"reference\"\
    : \"DOI:10.1007/s42770-023-01057-4\",\n            \"snippet\": \"activation of\
    \ a two-component system\",\n            \"notes\": \"Verified against the open\
    \ Ramón et al. PubMed abstract; cold sensing is described as occurring mainly\
    \ through liquid-crystalline membrane-state changes that activate a two-component\
    \ signal-transduction system.\"\n          }\n        ],\n        \"predicate_id\"\
    : \"RO:0002213\"\n      },\n      \"disposition\": \"UNASSESSED_SCOPE\",\n   \
    \   \"scope\": \"Literal phrase only; detailed cold-sensing activation unassessed.\"\
    \n    },\n    {\n      \"index\": 4,\n      \"field\": \"causal_graphs[0].edges[4]\"\
    ,\n      \"edge\": {\n        \"subject\": \"cold_shock_proteins\",\n        \"\
    predicate\": \"regulates\",\n        \"object\": \"cold_stabilized_rna_secondary_structure\"\
    ,\n        \"description\": \"CspA-family RNA chaperones regulate cold-stabilized\
    \ RNA structures to sustain translation.\",\n        \"evidence\": [\n       \
    \   {\n            \"reference\": \"DOI:10.4161/rna.7.6.13482\",\n           \
    \ \"snippet\": \"through their RNA chaperoning function\",\n            \"notes\"\
    : \"Verified against the open Phadtare and Severinov PubMed abstract; CspA-family\
    \ cold-shock proteins are described as RNA-modulating proteins affecting low-temperature\
    \ transcription and possibly translation through RNA chaperoning.\"\n        \
    \  }\n        ],\n        \"predicate_id\": \"RO:0002211\"\n      },\n      \"\
    disposition\": \"UNASSESSED_SCOPE\",\n      \"scope\": \"Literal phrase only;\
    \ detailed RNA/translation efficacy unassessed.\"\n    },\n    {\n      \"index\"\
    : 5,\n      \"field\": \"causal_graphs[0].edges[5]\",\n      \"edge\": {\n   \
    \     \"subject\": \"molecular_chaperones\",\n        \"predicate\": \"contributes\
    \ to\",\n        \"object\": \"proteostasis_cold\",\n        \"description\":\
    \ \"Chaperone/protease systems contribute to proteostasis by countering cold-slowed\
    \ folding and misfolding risk.\",\n        \"evidence\": [\n          {\n    \
    \        \"reference\": \"DOI:10.3389/fmicb.2023.1197797\",\n            \"snippet\"\
    : \"heat shock proteins associated to folding\",\n            \"notes\": \"Verified\
    \ against the open Ramasamy et al. PMC text; the Antarctic psychrophile review\
    \ discusses heat-shock proteins associated with protein folding in 4 °C versus\
    \ 18 °C Pseudoalteromonas haloplanktis TAC125.\"\n          }\n        ],\n  \
    \      \"predicate_id\": \"RO:0002326\"\n      },\n      \"disposition\": \"UNASSESSED_SCOPE\"\
    ,\n      \"scope\": \"Literal phrase only; numerical strain-specific proteostasis\
    \ comparison unassessed.\"\n    },\n    {\n      \"index\": 6,\n      \"field\"\
    : \"causal_graphs[0].edges[6]\",\n      \"edge\": {\n        \"subject\": \"compatible_solutes\"\
    ,\n        \"predicate\": \"contributes to\",\n        \"object\": \"protein_membrane_stabilization\"\
    ,\n        \"description\": \"Osmolytes contribute to protein and membrane stabilization\
    \ while lowering freezing damage.\",\n        \"evidence\": [\n          {\n \
    \           \"reference\": \"DOI:10.3389/fmicb.2023.1197797\",\n            \"\
    snippet\": \"counteracting protein aggregation, improving protein folding\",\n\
    \            \"notes\": \"Verified against the open Ramasamy et al. PMC text;\
    \ Antarctic compatible osmolytes are described as counteracting protein aggregation\
    \ and improving protein folding.\"\n          }\n        ],\n        \"predicate_id\"\
    : \"RO:0002326\"\n      },\n      \"disposition\": \"UNASSESSED_SCOPE\",\n   \
    \   \"scope\": \"Literal phrase only; detailed osmolyte protection/folding efficacy\
    \ unassessed.\"\n    },\n    {\n      \"index\": 7,\n      \"field\": \"causal_graphs[0].edges[7]\"\
    ,\n      \"edge\": {\n        \"subject\": \"ice_binding_proteins\",\n       \
    \ \"predicate\": \"inhibits\",\n        \"object\": \"ice_crystal_growth\",\n\
    \        \"description\": \"AFPs/IBPs bind ice and inhibit ice-crystal growth\
    \ and recrystallization.\",\n        \"evidence\": [\n          {\n          \
    \  \"reference\": \"DOI:10.3389/fmicb.2023.1197797\",\n            \"snippet\"\
    : \"inhibits the growth of ice crystals\",\n            \"notes\": \"Verified\
    \ against the open Ramasamy et al. PMC text; ice binding proteins are described\
    \ as antifreeze proteins that bind ice, inhibit ice-crystal growth, lower freezing\
    \ temperature, create a thermal hysteresis gap, and display ice-recrystallization\
    \ inhibition activity.\"\n          }\n        ],\n        \"predicate_id\": \"\
    RO:0002212\"\n      },\n      \"disposition\": \"UNASSESSED_SCOPE\",\n      \"\
    scope\": \"Literal phrase only; ice-binding/protection efficacy unassessed.\"\n\
    \    },\n    {\n      \"index\": 8,\n      \"field\": \"causal_graphs[0].edges[8]\"\
    ,\n      \"edge\": {\n        \"subject\": \"membrane_fluidity\",\n        \"\
    predicate\": \"associated with\",\n        \"object\": \"psychrophile_machinery\"\
    ,\n        \"description\": \"Membrane fatty-acid desaturation is associated with\
    \ the cold-adapted machinery supporting psychrophile growth ranges.\",\n     \
    \   \"evidence\": [\n          {\n            \"reference\": \"DOI:10.1007/s42770-023-01057-4\"\
    ,\n            \"snippet\": \"maintain the liquid crystalline phase\",\n     \
    \       \"notes\": \"Verified against the open Ramón et al. PubMed abstract; this\
    \ connector keeps membrane desaturation as cold membrane-adaptation context.\"\
    \n          }\n        ],\n        \"predicate_id\": \"biolink:associated_with\"\
    \n      },\n      \"disposition\": \"PARTIAL\",\n      \"scope\": \"Generic membrane\
    \ phase context and body phrase positive; note incorrectly says abstract.\"\n\
    \    },\n    {\n      \"index\": 9,\n      \"field\": \"causal_graphs[0].edges[9]\"\
    ,\n      \"edge\": {\n        \"subject\": \"two_component_cold_signaling\",\n\
    \        \"predicate\": \"associated with\",\n        \"object\": \"psychrophile_machinery\"\
    ,\n        \"description\": \"Two-component cold signaling is associated with\
    \ psychrophile cold-adapted machinery.\",\n        \"evidence\": [\n         \
    \ {\n            \"reference\": \"DOI:10.1007/s42770-023-01057-4\",\n        \
    \    \"snippet\": \"When the temperature drops, DesK/DesR is the two-component\
    \ system involved in membrane adaptation\",\n            \"notes\": \"Verified\
    \ against the open Ramón et al. PubMed abstract; this connector keeps low-temperature\
    \ membrane sensing as cold-acclimation context.\"\n          }\n        ],\n \
    \       \"predicate_id\": \"biolink:associated_with\"\n      },\n      \"disposition\"\
    : \"UNASSESSED_SCOPE\",\n      \"scope\": \"Body phrase positive; note incorrectly\
    \ says abstract; regulation efficacy unassessed.\"\n    },\n    {\n      \"index\"\
    : 10,\n      \"field\": \"causal_graphs[0].edges[10]\",\n      \"edge\": {\n \
    \       \"subject\": \"cold_stabilized_rna_secondary_structure\",\n        \"\
    predicate\": \"associated with\",\n        \"object\": \"psychrophile_machinery\"\
    ,\n        \"description\": \"CspA-family regulation of cold-stabilized RNA structure\
    \ is associated with psychrophile cold-adapted machinery.\",\n        \"evidence\"\
    : [\n          {\n            \"reference\": \"DOI:10.4161/rna.7.6.13482\",\n\
    \            \"snippet\": \"CspA, the main cold shock protein, and its homologs\
    \ act as RNA chaperones\",\n            \"notes\": \"Verified against the open\
    \ Phadtare and Severinov PubMed abstract; this connector keeps CspA-family RNA\
    \ chaperones as low-temperature transcript context.\"\n          }\n        ],\n\
    \        \"predicate_id\": \"biolink:associated_with\"\n      },\n      \"disposition\"\
    : \"UNASSESSED_SCOPE\",\n      \"scope\": \"Body phrase positive; note incorrectly\
    \ says abstract; RNA efficacy unassessed.\"\n    },\n    {\n      \"index\": 11,\n\
    \      \"field\": \"causal_graphs[0].edges[11]\",\n      \"edge\": {\n       \
    \ \"subject\": \"proteostasis_cold\",\n        \"predicate\": \"associated with\"\
    ,\n        \"object\": \"psychrophile_machinery\",\n        \"description\": \"\
    Cold proteostasis support is associated with the psychrophile machinery context.\"\
    ,\n        \"evidence\": [\n          {\n            \"reference\": \"DOI:10.3389/fmicb.2023.1197797\"\
    ,\n            \"snippet\": \"ice binding, cold shock and heat shock proteins\
    \ to sustain their physiological state\",\n            \"notes\": \"Verified against\
    \ the open Ramasamy et al. PMC text; this connector keeps chaperone/protease systems\
    \ as protein-folding context.\"\n          }\n        ],\n        \"predicate_id\"\
    : \"biolink:associated_with\"\n      },\n      \"disposition\": \"UNASSESSED_SCOPE\"\
    ,\n      \"scope\": \"Literal phrase only; proteostasis/fitness benefit unassessed.\"\
    \n    },\n    {\n      \"index\": 12,\n      \"field\": \"causal_graphs[0].edges[12]\"\
    ,\n      \"edge\": {\n        \"subject\": \"protein_membrane_stabilization\"\
    ,\n        \"predicate\": \"associated with\",\n        \"object\": \"psychrophile_machinery\"\
    ,\n        \"description\": \"Compatible-solute stabilization is associated with\
    \ psychrophile cold-adapted machinery.\",\n        \"evidence\": [\n         \
    \ {\n            \"reference\": \"DOI:10.3389/fmicb.2023.1197797\",\n        \
    \    \"snippet\": \"scavenging free radicals, counteracting protein aggregation\"\
    ,\n            \"notes\": \"Verified against the open Ramasamy et al. PMC text;\
    \ this connector keeps compatible osmolytes as stabilization context.\"\n    \
    \      }\n        ],\n        \"predicate_id\": \"biolink:associated_with\"\n\
    \      },\n      \"disposition\": \"UNASSESSED_SCOPE\",\n      \"scope\": \"Literal\
    \ phrase only; stabilization/ROS-defense efficacy unassessed.\"\n    },\n    {\n\
    \      \"index\": 13,\n      \"field\": \"causal_graphs[0].edges[13]\",\n    \
    \  \"edge\": {\n        \"subject\": \"ice_crystal_growth\",\n        \"predicate\"\
    : \"associated with\",\n        \"object\": \"psychrophile_machinery\",\n    \
    \    \"description\": \"Ice-binding protein inhibition of ice-crystal growth is\
    \ associated with psychrophile cold-adapted machinery.\",\n        \"evidence\"\
    : [\n          {\n            \"reference\": \"DOI:10.3389/fmicb.2023.1197797\"\
    ,\n            \"snippet\": \"This ceases ice growth by creating a thermal hysteresis\
    \ gap\",\n            \"notes\": \"Verified against the open Ramasamy et al. PMC\
    \ text; this connector keeps ice-binding proteins as freezing-protection context.\"\
    \n          }\n        ],\n        \"predicate_id\": \"biolink:associated_with\"\
    \n      },\n      \"disposition\": \"UNASSESSED_SCOPE\",\n      \"scope\": \"\
    Literal phrase only; protection efficacy unassessed.\"\n    }\n  ]\n}"
- assessment_id: owners
  area: ownership
  topic: 'Native checklist: exact templates and distinct guarded consumers'
  outcome: supported
  target_ids:
  - METPO:1000448
  summary: Six review after-edges and one node match current content. All six connector
    source guards/additions and AFTER metadata match; ordinary review and connector
    replay therefore no-op. PR664 consumes review after-payloads and six unfiltered
    additions and can replace populated matched triples. The exact three locator notes
    belong to connector ADDED_EDGES, with PR664 as consumer. Generic grounder skips
    populated IDs; rows 11/58/64/65 are conditional recurrence inputs. Machinery facet
    is record-only; no faulty producer demonstrated.
  evidence_ids:
  - owners
  - owner-primary
  - writer-payloads
  - source-owners
  - canonical-writer
  - predicate-mapping
  - discovery
  - adjudication
- assessment_id: provenance
  area: provenance
  topic: 'Native checklist: bounded human acceptance link'
  outcome: concern
  target_ids:
  - METPO:1000448
  summary: Twelve embedded events comprise eleven AI-assisted entries and a seed.
    All 22 current captured actor projections are AI; whole readings are exact qualified
    prior readings with no fresh whole-history claim. Ignored- and hidden-inclusive
    search excluding .git/.venv internals found 196 matching paths and 71 matching
    arrays; all 96 actual local top-level target arrays have zero exact match. Private
    or remote acceptance remains unknown.
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
  topic: 'Native checklist: retained catalog and bounded adapter availability'
  outcome: unknown
  target_ids:
  - METPO:1000448
  summary: The retained 20-organism/28-dataset catalog has no exact Psychromonas/P.
    ingrahamii or Pseudoalteromonas/P. haloplanktis entry under the bounded name searches.
    This is not an exhaustive source-organism inventory or global absence claim. No
    maintained adapter was found within current project/install/PATH scope, so no
    module query or efficacy result is asserted.
  evidence_ids:
  - expression
  - expression-discovery
  - catalog-original
  - catalog-reuse
  - source-reading
  - adjudication
- assessment_id: readiness
  area: completeness
  topic: 'Native checklist: NONMECHANISTIC context and optional instances'
  outcome: supported
  target_ids:
  - METPO:1000448
  summary: One connected component, fifteen nodes, fourteen edges, three reviewed
    label-only aggregates and zero instances are permissible current NONMECHANISTIC
    context. No extra connector, accession or dataset is required to fill optional
    structure. These positives do not resolve the four formal assertions, machinery
    facet, source locators or human acceptance link.
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
  - METPO:1000448
  summary: Current inspect, target validation, strict validation and snippet checks
    are successful B15 executions. Four original B14 common diagnostics are qualified
    for unchanged B15 inputs, not relabeled fresh B15 executions. Original intervals,
    historical attempts, product skips and omitted full just test retain their scope.
    These eight command checks do not establish scientific correctness or human acceptance.
  evidence_ids:
  - capture
  - common-reuse-qualification
  - original-b14-common-completion
  - check-temperature-range-very-low-target-validate
  - check-temperature-range-very-low-target-strict
  - check-temperature-range-very-low-snippets-network
  - source-native
findings:
- finding_id: imported-process-roles
  issue_key: temperature-range-very-low-imported-process-roles
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Imported process roles
  description: RO:0002213 at edge2 has a quality object; at edge3 it has an ambient-condition
    subject. RO:0002211 at edge4 connects a material protein to an RNA-structure quality.
    RO:0002212 at edge7 has a material protein subject; its physical ice-growth process
    object is compatible. These predicates inherit process-to-process requirements.
    Judgments follow actual referents, not node enums alone. All six review after-edges
    and one after-node match current content. All six connector source guards and
    six additions also match; current AFTER metadata and one component make both ordinary
    writers static no-ops. PR664 consumes review replacements and six unfiltered connector
    additions and can replace populated matched triples. The generic grounder skips
    populated IDs; regulates/inhibits/activates/increases mapping rows11/58/64/65
    remain conditional recurrence inputs. Coordinate these distinct owners and effective
    roles without inventing biological steps.
  target_ids:
  - METPO:1000448
  field_paths:
  - causal_graphs[0].edges[2].predicate_id
  - causal_graphs[0].edges[3].predicate_id
  - causal_graphs[0].edges[4].predicate_id
  - causal_graphs[0].edges[7].predicate_id
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
    path: data/traits/environment/temperature_range_very_low.yaml
    role: Current record assertions; separate authorized curation required
  - repository: CultureBotAI/TraitMech
    path: scripts/review_temperature_range_very_low_graph_183.py
    role: Exact six review after-edges and one after-node match current content; ordinary
      transform no-ops
  - repository: CultureBotAI/TraitMech
    path: scripts/connect_temperature_range_very_low_graph_183.py
    role: Six source guards and additions match current AFTER/one-component state;
      exact three source-location notes are ADDED_EDGES payloads; ordinary replay
      no-ops
  - repository: CultureBotAI/TraitMech
    path: scripts/repair_pr664_adversarial_review.py
    role: Matched-triple consumer of review after-payloads and six unfiltered connector
      additions, including source-location note payloads; not independent source authority
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Wildcard rows 11/58/64/65 are future empty-field recurrence inputs
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Conditional generic consumer skips populated identifiers; ordinary replay
      is not current-field repair
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: machinery-facet
  issue_key: temperature-range-very-low-machinery-facet
  category: consistency
  severity: minor
  status: open
  certainty: confirmed
  title: Machinery facet
  description: The machinery node is typed BIOLOGICAL_PROCESS while its description
    names material cold-active enzymes and unsaturated-lipid membranes. The functional
    clause about sustaining function leaves its intended facet unclear. Clarify what
    this node represents; the evidence does not prescribe a replacement enum or added
    mechanism. No exact faulty producer of these two fields was established.
  target_ids:
  - METPO:1000448
  field_paths:
  - causal_graphs[0].nodes[2].node_type
  - causal_graphs[0].nodes[2].description
  evidence_ids:
  - record
  - nodes-edges
  - schema
  - owners
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_range_very_low.yaml
    role: Current record assertions; separate authorized curation required
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: source-surface-location
  issue_key: temperature-range-very-low-source-surface-location
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Source surface location
  description: 'Three notes say the quotations were verified in PubMed abstracts.
    Each exact span is absent from the retained indexed and PMC abstracts but present
    in article-body text: Ramon all-HTML paragraph17/Par10/Sec3 for edge8, paragraph31/Par20/Sec7
    for edge9, and Phadtare paragraph11/sec2 for edge10. All15 supplied snippets remain
    literal; this is a source-surface correction, not a false-quotation or efficacy
    finding. The connector stores the exact three note payloads in ADDED_EDGES; its
    ordinary replay is a no-op. PR664 is a replacement consumer of that payload, not
    an independent source authority.'
  target_ids:
  - METPO:1000448
  field_paths:
  - causal_graphs[0].edges[8].evidence[0].notes
  - causal_graphs[0].edges[9].evidence[0].notes
  - causal_graphs[0].edges[10].evidence[0].notes
  evidence_ids:
  - sources
  - placements
  - notes
  - snippets
  - source-locations
  - source-owners
  - cold-body
  - phadtare-body
  - writer-payloads
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_range_very_low.yaml
    role: Current record assertions; separate authorized curation required
  - repository: CultureBotAI/TraitMech
    path: scripts/connect_temperature_range_very_low_graph_183.py
    role: Six source guards and additions match current AFTER/one-component state;
      exact three source-location notes are ADDED_EDGES payloads; ordinary replay
      no-ops
  - repository: CultureBotAI/TraitMech
    path: scripts/repair_pr664_adversarial_review.py
    role: Matched-triple consumer of review after-payloads and six unfiltered connector
      additions, including source-location note payloads; not independent source authority
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: human-acceptance-link
  issue_key: temperature-range-very-low-human-acceptance-link
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Human acceptance link
  description: REVIEWED status has no retrievable exact-target human acceptance in
    the bounded local evidence. The12 embedded events comprise11 AI-assisted entries
    and the METPO seed. All22 captured histories have AI actor projections; their
    whole readings are exact qualified prior readings. Ignored- and hidden-inclusive
    discovery excluding .git/.venv internals found196 matching paths and71 matching
    review arrays; all96 actual local top-level target arrays contain zero exact target
    matches. Private or remote acceptance remains unknown.
  target_ids:
  - METPO:1000448
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
    path: data/traits/environment/temperature_range_very_low.yaml
    role: Current record assertions; separate authorized curation required
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
actions:
- action_id: curate-imported-process-roles
  description: Resolve the four imported assertions against declared referents and
    coordinate exact templates, replacement consumers and conditional mapping recurrence.
  finding_ids:
  - imported-process-roles
  target_ids:
  - METPO:1000448
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_range_very_low.yaml
    role: Current record assertions; separate authorized curation required
  - repository: CultureBotAI/TraitMech
    path: scripts/review_temperature_range_very_low_graph_183.py
    role: Exact six review after-edges and one after-node match current content; ordinary
      transform no-ops
  - repository: CultureBotAI/TraitMech
    path: scripts/connect_temperature_range_very_low_graph_183.py
    role: Six source guards and additions match current AFTER/one-component state;
      exact three source-location notes are ADDED_EDGES payloads; ordinary replay
      no-ops
  - repository: CultureBotAI/TraitMech
    path: scripts/repair_pr664_adversarial_review.py
    role: Matched-triple consumer of review after-payloads and six unfiltered connector
      additions, including source-location note payloads; not independent source authority
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Wildcard rows 11/58/64/65 are future empty-field recurrence inputs
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Conditional generic consumer skips populated identifiers; ordinary replay
      is not current-field repair
  acceptance_checks:
  - Document each affected endpoint and effective inherited domain/range; preserve
    material, quality, ambient-condition and process distinctions.
  - Coordinate review EDGE_REPLACEMENTS, connector source guards/additions and PR664
    matched-triple replacement. Both ordinary writers currently no-op; PR664 has six
    unfiltered additions, unlike earlier temperature records.
  - Address regulates row11, inhibits row58, activates row64 and increases row65 for
    future empty fields; use explicit guarded curation for populated IDs.
  - Use meaningful focused grounding/guard checks, strict validation and applicable
    QC/products. No operational mechanism repair or efficacy improvement is prescribed.
- action_id: curate-machinery-facet
  description: Clarify the machinery node referent and align its type and description
    in separately authorized curation.
  finding_ids:
  - machinery-facet
  target_ids:
  - METPO:1000448
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_range_very_low.yaml
    role: Current record assertions; separate authorized curation required
  acceptance_checks:
  - Distinguish the material apparatus from an actual process without assuming a replacement
    enum or new intermediary.
  - Keep broad confers-role compatibility separate from the unresolved node facet
    and biological efficacy.
  - Use guarded record/history curation and applicable validation/products. No unsupported
    producer attribution.
- action_id: curate-source-surface-location
  description: Correct the three body locators and coordinate the exact connector
    note payload and its PR664 consumer.
  finding_ids:
  - source-surface-location
  target_ids:
  - METPO:1000448
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_range_very_low.yaml
    role: Current record assertions; separate authorized curation required
  - repository: CultureBotAI/TraitMech
    path: scripts/connect_temperature_range_very_low_graph_183.py
    role: Six source guards and additions match current AFTER/one-component state;
      exact three source-location notes are ADDED_EDGES payloads; ordinary replay
      no-ops
  - repository: CultureBotAI/TraitMech
    path: scripts/repair_pr664_adversarial_review.py
    role: Matched-triple consumer of review after-payloads and six unfiltered connector
      additions, including source-location note payloads; not independent source authority
  acceptance_checks:
  - Use body paragraph/section locators from the retained source surfaces rather than
    PubMed-abstract attribution.
  - Preserve all15 literal quotations and their source identities; distinguish manual
    literal matching from native four VERIFIED and11 inconclusive NOT_IN_ABSTRACT
    results.
  - Preserve causal uncertainty and validate guarded record/history/template changes
    without treating occurrence as proof of biological efficacy.
- action_id: curate-human-acceptance-link
  description: Link attributable human acceptance for REVIEWED status or accurately
    qualify the review state in separately authorized curation.
  finding_ids:
  - human-acceptance-link
  target_ids:
  - METPO:1000448
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_range_very_low.yaml
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
- Selected classification/generic physical text and supplied literal spans only; no
  whole-paper efficacy or exhaustive notice review.
- Detailed stress-defense/regulatory/fitness/survival/cryoprotection/cultivation optimization
  and intervention efficacy remains UNASSESSED_SCOPE.
- Exact inclusive10 boundary and exact Psychrophile synonym equivalence remain qualified;
  no all-publication absence inference from selected near-freezing passage.
- Canonical primary indexed abstract supports existing named strain/interval; no full
  body, exhaustive curve or optimization adopted. Other displayed culture/composition/genome
  material incidental and unadopted.
- Original acquisition, current copy, extraction and reading clocks remain distinct;
  historical notice fields are not fresh status searches.
- Initial optional-path search corrected with ignored-inclusive source-folder search;
  no retained canonical DOI metadata found in that bounded search. No broken-DOI inference.
- Initial optional BeautifulSoup import unavailable and initial prewrite matcher incorrectly
  removed angle-bracket content from already-extracted text; standard-library parser
  and text-only whitespace matching corrected these local read/check issues before
  any ledger write. Neither was a native failure.
- Source-supported phenotype and literal placements independently source-audited;
  no new detailed stress/defense/survival/cryoprotection/fitness/cultivation or enzyme-improvement
  judgments.
- Node6 signaling-system wording and broad-association proxy descriptions remain qualified,
  without forced extra type or relation findings.
- Biological alias equivalence is not established solely by faithful upstream copying.
- Private/remote human acceptance unknown; local absence includes ignored/hidden files
  but excludes .git/.venv internals.
- Ground auditor did not rerun common/native checks or ontology databases.
- Root adopted D’Amico selected generic near-freezing classification and physical
  challenges, Ramon selected generic physical context, and the Phadtare indexed physical
  RNA-structure sentence. Detailed signaling/regulation, stress defenses, survival,
  fitness, cryoprotection, cultivation optimization and intervention efficacy remain
  unassessed. Ramasamy matching establishes six existing literal spans only.
- The canonical indexed abstract was fully displayed, but adopted scope is the existing
  strain37T, reported -12 to10 degreesC and CCUG51855T/CIP108865T aliases. Other culture,
  composition and genomic passages are incidental and unadopted; no full growth curve
  or optimization was assessed.
- Ten retained source entries comprise eight original acquisition intervals, derived
  PDF text and its historical extraction receipt. Current copy and reading times are
  distinct. Initial canonical and taxonomy DNS failures and successful retries retain
  separate clocks and bytes. Notice observations are historical metadata fields, not
  an exhaustive current status search.
- Current writer outcomes are static inferences from selected guards and exact payload
  comparisons. No writer or full PR664 dry run was executed.
- Original B14 common diagnostics are qualified for unchanged B15 inputs, not fresh
  B15 executions. Current target inspect, validation, strict validation and snippet
  check are fresh. The serializer common guard separately rechecks current inputs
  and five database pins.
- Full just test was not run; focused Stage2 tests and product skips retain original
  scope. Software checks do not establish scientific correctness.
- Active exact METPO:1000448, direct parent1000306 and the numeric-temperature/growth-range
  lineage1000533/1000535 are supported. Raw maximum-inclusive10 Cel restriction uses
  generic has-value2000071. Definition, trait node, edge0, graph description and canonical
  note coherently use an ambient threshold at/below10; no inherited interval-width
  conflict is present. Exact boundary calibration and biological Psychrophile alias
  equivalence remain qualified.
- Local membrane-fluidity METPO:1007505 is in v3 and absent from captured upstream
  raw OWL. Local v8 confers is broad. PATO:0001306 decreased temperature is a relatively
  low-temperature quality with a coherent declared closeMatch to the environmental
  condition. The current node denotes ambient condition, not a cooling execution.
- RO:0002211 and its negative/positive subproperties require process endpoints. RO:0002326
  has material-to-process roles via2216→2500→2595, without2215; edges5/6 fit those
  formal roles. This does not establish executor efficacy. Ice-crystal growth is processual;
  RNA structure is a quality; compatible solutes are material substances.
- Node6 process label versus regulatory-system wording and broad Biolink association
  proxy descriptions remain qualified without forced extra categorical findings. NamedThing
  roles do not import RO process requirements or prove statistical association or
  benefit.
- Canonical primary indexed abstract and official taxonomy support Psychromonas ingrahamii37T,
  existing -12 to10 degreesC interval and aliases. The arithmetic width is irrelevant
  to the current coherent endpoint threshold; taxonomy supports identity only.
- One connected component,15 nodes,14 edges, three REVIEWED_LABEL_ONLY protein aggregates
  and zero instances are permissible NONMECHANISTIC context. No extra connector, accession
  or dataset is required merely to fill optional structure.
- The retained20-organism/28-dataset catalog contains no exact Psychromonas/P.ingrahamii
  or Pseudoalteromonas/P.haloplanktis entry under the bounded searches. This is not
  an exhaustive source-organism inventory or whole-corpus absence. Bounded project/install/PATH
  discovery found no maintained adapter; no module query was executed.
- Publication is separate from this local review. No scientific record, mapping, ontology,
  history, generated product or paid-provider run changed.
notes:
- Qualified reuse of four original B14 diagnostics is recorded in /private/tmp/traitmech-record-sweep-015.67f2ce7a/common-diagnostic-reuse-qualification.json.
  Historical products failures/retry and original cache provenance remain in /private/tmp/traitmech-record-sweep-014.q8m4v2cs/new-base-diagnostic-independent-review-agent/fresh-products-completion.json.
  B14 generated reports are retained output snapshots, not B15 source inputs or synthetic
  B15 reports. B15-to-B14 byte equality does not change the historical false B14-to-B13
  comparison; B14 final gates/commit and continuation pins remain separate.
- 'Exact findings, actions, fields, severities and owners come only from root FINAL:
  one imported-role major and three bounded minors. Current threshold use is coherent;
  no sibling interval-width finding or extra type/association finding is inherited.'
- Serializer preparation adopts frozen audits and root adjudication without another
  whole-paper or whole-history review. Ten copied source entries retain eight original
  acquisition clocks, derived text and its historical extraction receipt. Current
  canonical/taxonomy failures and retries, root query/read/copy clocks and source-surface
  corrections remain distinct. Ground-auditor non-repetition is actor-specific; common
  guard separately rechecks qualified inputs and database pins. Original B14 diagnostics
  are not fresh B15 executions.
tags:
- record-review
- temperature-range-very-low
- environment
- needs-curation
```
