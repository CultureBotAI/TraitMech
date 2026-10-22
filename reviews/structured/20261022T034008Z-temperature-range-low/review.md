# Whole-record review of temperature range low

- Review: 20261022T034008Z-temperature-range-low
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-22T03:27:28.607294Z
- Finished UTC: 2026-10-22T03:40:08Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Whole-record review identifies two major issues: conflicting ambient-interval versus range-width semantics, and incompatible imported process roles at four edges. Two bounded minors concern nearest-source exact-bin attribution and a retrievable human-acceptance link. Active identity, source-resolved canonical22–36interval/14width, three literal snippets and several formal endpoint facets are positive; detailed microbial efficacy remains unassessed.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: Tenth record in the actual B14 queue; current 253-line target and 103 captured inputs. Local review is independent of remote publication.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 508ee3089c93a36413969cd1ede7f9528a1940a4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| METPO:1000449 | data/traits/environment/temperature_range_low.yaml | maintained | temperature range low |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Fresh B14 corpus QC | passed | True | METPO:1000449 | Actual just qc passed: strict validation of 1130 records with 0 errors; graph audit: 74 baselined, 0 new and 0 blocking findings; 135 connected graphs and 1588 wired nodes; protein coverage: 729 graphs (134 pass, 594 NONMECHANISTIC, 0 gaps, 1 protected); snippet audit: 2419 baselined, 0 new and 0 blocking findings; 19 PathwayMech links. These are corpus diagnostics, not scientific validation of this target. |
| Fresh B14 history integrity | passed | True | METPO:1000449 | 1278 HistoryRecord YAMLs validated, 0 invalid; current history snapshot contains 1279 files. Integrity does not establish scientific correctness or human acceptance. |
| Fresh B14 mapping identifier/label validation | passed | True | METPO:1000449 | 361 canonical matches, 2 exact-synonym matches, 1 exception and 123 SKIPPED_NO_ADAPTER pairs. Configured scope is the two grounding mappings, not every target identifier or scientific claim. |
| Focused Stage2 writer tests | passed | False | METPO:1000449 | Five tests passed in the explicitly selected Stage2 test file. This is not a full just test run or biological validation. |
| Focused native validation | passed | True | METPO:1000449 | Native record validation passed; scientific interpretation is assessed separately. |
| Focused strict validation | passed | True | METPO:1000449 | The actual validate-strict command passed. |
| Focused network snippet check | passed | True | METPO:1000449 | Native command completed successfully: one VERIFIED and two NOT_IN_ABSTRACT, the latter inconclusive. Manual retained primary text supports all three supplied snippets, one with ordinary PDF line-break dehyphenation. Literal support does not establish adjacent exact-bin claims. |
| One-target native review capture | passed | True | METPO:1000449 | One current target, 103 captured inputs, exact current base and successful native inspect. |
| Protein-instance metadata applicability | not_applicable | False | METPO:1000449 | Two contextual protein aggregates have explicit label-only rationales and zero instances; no token accession required. |
| Structured source-organism expression query availability | unavailable | False | METPO:1000449 | Bounded maintained-runner discovery found no available adapter. Retained catalog and selected source identities provide no exact species/strain/module or efficacy result. |

## Scientific And Domain Assessments

### Native checklist: active bin and direct parent

identity: supported. Targets: METPO:1000449.

Active METPO:1000449 and direct parent METPO:1000306 are positive. Copied upstream qualitative synonyms are faithful; exact biological equivalence remains unresolved, not a separate forced synonym defect. Generic raw numeric restrictions do not decide the operational quantity.

### Native checklist: ambient interval versus range width

quantity: concern. Targets: METPO:1000449.

Definition and graph use 10–22 °C as an ambient growth interval, while the canonical note interprets the same numerical bin as a width. The source interval 22–36 °C and arithmetic 36 minus 22 equals 14 are correct. One grouped major reconciles quantity meaning without rejecting the supported measurement or inferring endpoint/width semantics solely from generic existential has-value.

### Native checklist: strain-scoped source measurement and identity

evidence: supported. Targets: METPO:1000449.

The assigned primary abstract supports Aestuariibius violaceus strain 2305UL40-4T, its reported 22–36 °C growth interval and derived width 14. Official species/type-material identity is positive. The source optimum is separate. Membership interpretation participates in the quantity finding; no false measurement, wrong organism or cultivation optimization is asserted.

### Native checklist: six works and eleven placements

evidence: concern. Targets: METPO:1000449.

All six identities resolve. Two D’Amico notes overstate nearest broad cold/near-freezing spans as exact 10–22 support, a bounded minor distinct from the quantity major. Selected Ramón physical context and Yang Bacillus simplex H-b UFA observation are qualified positives. Exact-bin mechanism sufficiency and detailed defense, survival, fitness, regulation, enhancement, cryoprotection and intervention efficacy remain unassessed; inaccessible AMTT body is not refuted.

### Native checklist: three supplied literal snippets

evidence: supported. Targets: METPO:1000449.

All three current schema snippets are supported by retained author-repository PDF text; one needs ordinary pro-/teins line-break dehyphenation. Native one VERIFIED and two NOT_IN_ABSTRACT remain separate from manual primary matching. There is no copied-span finding, and literal phrases do not establish exact numerical-bin support in adjacent notes.

### Native checklist: all thirteen current referents

representation: concern. Targets: METPO:1000449.

The child and ambient-condition descriptions participate in the grouped quantity conflict. PATO relatively-low condition, membrane-fluidity/proportion QUALITY and molecular-activity facets are otherwise positive. CHEBI osmolyte role versus material bearer is a maintained closeMatch qualification, not forced wrong identity. Two protein aggregates have explicit label-only rationales; detailed function and efficacy are unassessed.

{
  "grounding": [
    {
      "index": 0,
      "field": "causal_graphs[0].nodes[0]",
      "node": {
        "node_id": "temperature_range_low_trait",
        "label": "temperature range low",
        "node_type": "TRAIT",
        "grounding": "METPO:1000449",
        "description": "Temperature growth-supporting range approximately 10–22 °C."
      },
      "outcome": "concern",
      "judgment": "Active exact trait identity and direct parent are positive; explicit ambient 10–22 °C wording conflicts with canonical range-width interpretation (one grouped quantity finding)."
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
      "judgment": "Active parent temperature range identity; retained raw class has both numerical-temperature and numerical-growth-range parents."
    },
    {
      "index": 2,
      "field": "causal_graphs[0].nodes[2]",
      "node": {
        "node_id": "psychrotolerant_adaptation",
        "label": "psychrotolerant adaptation",
        "node_type": "BIOLOGICAL_PROCESS",
        "description": "Mild cold-adaptation of membrane and enzyme function sustaining growth at cool temperatures."
      },
      "outcome": "qualified",
      "judgment": "Explicit adaptation process is process-compatible; exact numerical calibration and biological efficacy unassessed."
    },
    {
      "index": 3,
      "field": "causal_graphs[0].nodes[3]",
      "node": {
        "node_id": "low_temperature",
        "label": "low temperature",
        "node_type": "ENVIRONMENTAL_FACTOR",
        "description": "Cool ambient temperature in the approximately 10-22 C range.",
        "grounding": "PATO:0001306"
      },
      "outcome": "qualified",
      "judgment": "PATO relatively-low-temperature condition fits environmental exposure shorthand; not a decrease event. Absolute 10–22 wording participates in the quantity-scope conflict, not a separate PATO defect."
    },
    {
      "index": 4,
      "field": "causal_graphs[0].nodes[4]",
      "node": {
        "node_id": "membrane_fluidity",
        "label": "membrane fluidity",
        "node_type": "QUALITY",
        "description": "Physical fluidity state of the cytoplasmic membrane lipid bilayer.",
        "grounding": "METPO:1007505"
      },
      "outcome": "positive",
      "judgment": "Physical membrane-fluidity quality matches v3 METPO1007505; not a process."
    },
    {
      "index": 5,
      "field": "causal_graphs[0].nodes[5]",
      "node": {
        "node_id": "fatty_acid_desaturase_activity",
        "label": "fatty acid desaturase activity",
        "node_type": "MOLECULAR_FUNCTION",
        "description": "Enzymatic introduction of double bonds into fatty acyl chains (fatty acid desaturases, EC 1.14.19.-)."
      },
      "outcome": "positive",
      "judgment": "Enzymatic activity is process-compatible MOLECULAR_FUNCTION, not automatically a material protein."
    },
    {
      "index": 6,
      "field": "causal_graphs[0].nodes[6]",
      "node": {
        "node_id": "unsaturated_fatty_acid_proportion",
        "label": "unsaturated fatty acid proportion",
        "node_type": "QUALITY",
        "description": "Relative abundance of unsaturated fatty acids in membrane lipids."
      },
      "outcome": "positive",
      "judgment": "Relative abundance/proportion is explicitly a QUALITY; the node already preserves the correct quantity facet."
    },
    {
      "index": 7,
      "field": "causal_graphs[0].nodes[7]",
      "node": {
        "node_id": "cold_shock_proteins",
        "label": "cold-shock proteins",
        "node_type": "GENE_OR_PROTEIN",
        "grounding_status": "REVIEWED_LABEL_ONLY",
        "grounding_notes": "Reviewed as a contextual protein or protein-complex label within a quantitative measurement graph; no exact semantic family term was established for this aggregate use.",
        "description": "CspA/CspC family cold-shock proteins acting as RNA chaperones."
      },
      "outcome": "qualified",
      "judgment": "Protein-family material referent with explicit REVIEWED_LABEL_ONLY disposition; no exact accession or instance required."
    },
    {
      "index": 8,
      "field": "causal_graphs[0].nodes[8]",
      "node": {
        "node_id": "rna_chaperone_activity",
        "label": "RNA chaperone activity",
        "node_type": "MOLECULAR_FUNCTION",
        "description": "Resolution of inhibitory RNA secondary structures supporting translation at low temperature."
      },
      "outcome": "positive",
      "judgment": "RNA secondary-structure resolution is a molecular activity/process referent; no molecular efficacy assessed."
    },
    {
      "index": 9,
      "field": "causal_graphs[0].nodes[9]",
      "node": {
        "node_id": "compatible_solutes",
        "label": "compatible solutes",
        "node_type": "CHEMICAL",
        "description": "Glycine betaine, trehalose and glycerol accumulated as cryoprotectants.",
        "grounding": "CHEBI:25728"
      },
      "outcome": "qualified",
      "judgment": "Material solutes are clear in prose; CHEBI25728 has role ancestry. Maintained closeMatch is looser than identity, so qualify role-versus-bearer grounding rather than declare a wrong identifier."
    },
    {
      "index": 10,
      "field": "causal_graphs[0].nodes[10]",
      "node": {
        "node_id": "cryoprotection",
        "label": "cryoprotection",
        "node_type": "BIOLOGICAL_PROCESS",
        "description": "Stabilization of proteins and membranes and protection against cold/freezing damage."
      },
      "outcome": "qualified",
      "judgment": "Stabilization/protection is a processual referent; detailed cryoprotection efficacy unassessed."
    },
    {
      "index": 11,
      "field": "causal_graphs[0].nodes[11]",
      "node": {
        "node_id": "molecular_chaperones",
        "label": "GroEL/DnaK molecular chaperones",
        "node_type": "GENE_OR_PROTEIN",
        "grounding_status": "REVIEWED_LABEL_ONLY",
        "grounding_notes": "Reviewed as a contextual protein or protein-complex label within a quantitative measurement graph; no exact semantic family term was established for this aggregate use.",
        "description": "GroEL and DnaK chaperones assisting protein folding under temperature stress."
      },
      "outcome": "qualified",
      "judgment": "Chaperone protein-family material referent with explicit REVIEWED_LABEL_ONLY disposition; no mandatory exemplar."
    },
    {
      "index": 12,
      "field": "causal_graphs[0].nodes[12]",
      "node": {
        "node_id": "protein_misfolding",
        "label": "protein misfolding",
        "node_type": "BIOLOGICAL_PROCESS",
        "description": "Cold-denaturation and misfolding of proteins at low temperature."
      },
      "outcome": "positive",
      "judgment": "Misfolding is a biological process; negative direction targets the damaging process, so no independent polarity inconsistency."
    }
  ],
  "source": [
    {
      "index": 0,
      "field": "causal_graphs[0].nodes[0]",
      "node_id": "temperature_range_low_trait",
      "label": "temperature range low",
      "description": "Temperature growth-supporting range approximately 10–22 °C.",
      "outcome": "CONCERN",
      "scope": "Current10–22 ambient interval conflicts with explicit canonical width interpretation; no source-derived replacement chosen."
    },
    {
      "index": 1,
      "field": "causal_graphs[0].nodes[1]",
      "node_id": "temperature_range",
      "label": "temperature range",
      "description": "Span of ambient temperatures supporting growth.",
      "outcome": "SUPPORTED_WITH_QUALIFICATION",
      "scope": "Generic span of growth-supporting ambient temperatures is coherent; endpoints versus scalar width must be distinguished in the child."
    },
    {
      "index": 2,
      "field": "causal_graphs[0].nodes[2]",
      "node_id": "psychrotolerant_adaptation",
      "label": "psychrotolerant adaptation",
      "description": "Mild cold-adaptation of membrane and enzyme function sustaining growth at cool temperatures.",
      "outcome": "UNASSESSED_SCOPE",
      "scope": "Broad cold-adaptation identity only; membrane/enzyme efficacy for exact bin not assessed."
    },
    {
      "index": 3,
      "field": "causal_graphs[0].nodes[3]",
      "node_id": "low_temperature",
      "label": "low temperature",
      "description": "Cool ambient temperature in the approximately 10-22 C range.",
      "outcome": "PARTIAL",
      "scope": "Cold ambient physical context is supported generically;10–22 calibration and quantity interpretation unresolved."
    },
    {
      "index": 4,
      "field": "causal_graphs[0].nodes[4]",
      "node_id": "membrane_fluidity",
      "label": "membrane fluidity",
      "description": "Physical fluidity state of the cytoplasmic membrane lipid bilayer.",
      "outcome": "SUPPORTED",
      "scope": "Generic physical membrane-fluidity referent supported by selected D’Amico and Ramón text."
    },
    {
      "index": 5,
      "field": "causal_graphs[0].nodes[5]",
      "node_id": "fatty_acid_desaturase_activity",
      "label": "fatty acid desaturase activity",
      "description": "Enzymatic introduction of double bonds into fatty acyl chains (fatty acid desaturases, EC 1.14.19.-).",
      "outcome": "UNASSESSED_SCOPE",
      "scope": "Existing desaturase activity name retained; detailed intervention/fitness efficacy not evaluated."
    },
    {
      "index": 6,
      "field": "causal_graphs[0].nodes[6]",
      "node_id": "unsaturated_fatty_acid_proportion",
      "label": "unsaturated fatty acid proportion",
      "description": "Relative abundance of unsaturated fatty acids in membrane lipids.",
      "outcome": "PARTIAL",
      "scope": "Generic composition property and reported UFA cohort observation positive; no universal or exact-bin inference."
    },
    {
      "index": 7,
      "field": "causal_graphs[0].nodes[7]",
      "node_id": "cold_shock_proteins",
      "label": "cold-shock proteins",
      "description": "CspA/CspC family cold-shock proteins acting as RNA chaperones.",
      "outcome": "UNASSESSED_SCOPE",
      "scope": "Contextual CspA/CspC label retained; detailed family function and cold-survival intervention efficacy unassessed."
    },
    {
      "index": 8,
      "field": "causal_graphs[0].nodes[8]",
      "node_id": "rna_chaperone_activity",
      "label": "RNA chaperone activity",
      "description": "Resolution of inhibitory RNA secondary structures supporting translation at low temperature.",
      "outcome": "UNASSESSED_SCOPE",
      "scope": "Existing RNA-chaperone name retained; detailed efficacy unassessed."
    },
    {
      "index": 9,
      "field": "causal_graphs[0].nodes[9]",
      "node_id": "compatible_solutes",
      "label": "compatible solutes",
      "description": "Glycine betaine, trehalose and glycerol accumulated as cryoprotectants.",
      "outcome": "UNASSESSED_SCOPE",
      "scope": "Existing compatible-solute names retained; detailed cryoprotective/defense claims unassessed."
    },
    {
      "index": 10,
      "field": "causal_graphs[0].nodes[10]",
      "node_id": "cryoprotection",
      "label": "cryoprotection",
      "description": "Stabilization of proteins and membranes and protection against cold/freezing damage.",
      "outcome": "UNASSESSED_SCOPE",
      "scope": "Existing cryoprotection process label retained; detailed biological efficacy unassessed."
    },
    {
      "index": 11,
      "field": "causal_graphs[0].nodes[11]",
      "node_id": "molecular_chaperones",
      "label": "GroEL/DnaK molecular chaperones",
      "description": "GroEL and DnaK chaperones assisting protein folding under temperature stress.",
      "outcome": "UNASSESSED_SCOPE",
      "scope": "Existing GroEL/DnaK aggregate retained; detailed proteostasis intervention efficacy unassessed."
    },
    {
      "index": 12,
      "field": "causal_graphs[0].nodes[12]",
      "node_id": "protein_misfolding",
      "label": "protein misfolding",
      "description": "Cold-denaturation and misfolding of proteins at low temperature.",
      "outcome": "UNASSESSED_SCOPE",
      "scope": "Existing cold-denaturation/misfolding process label retained; detailed stress mechanism unassessed."
    }
  ]
}

### Native checklist: all eight current relations

consistency: concern. Targets: METPO:1000449.

RO2212/RO2213 process-to-process constraints conflict with explicit quality objects at edges 2/3/4 and material protein subject at edge 7. Correct activity/process facets are preserved; no biological intermediate or predicate replacement is invented. Edge 5 material-to-activity endpoint fit is positive without executor-efficacy validation. Broad v8 confers, exact subclass relation and lexical provides retain their separate scopes. Misfolding is a damaging process, so no extra polarity finding.

{
  "grounding": [
    {
      "index": 0,
      "field": "causal_graphs[0].edges[0]",
      "edge": {
        "subject": "psychrotolerant_adaptation",
        "predicate": "confers",
        "object": "temperature_range_low_trait",
        "description": "Psychrotolerant adaptation enables growth across 10–22 °C.",
        "evidence": [
          {
            "reference": "DOI:10.1038/sj.embor.7400662",
            "snippet": "Cold-shock proteins have also been described",
            "notes": "Supports cold-shock and acclimation responses as the cool-range mechanism."
          }
        ],
        "predicate_id": "METPO:2007700"
      },
      "outcome": "qualified",
      "judgment": "Local v8 confers admits broad causal-node-to-trait endpoints; adaptation process to trait fits. Numeric object scope needs the grouped quantity reconciliation; detailed efficacy unassessed."
    },
    {
      "index": 1,
      "field": "causal_graphs[0].edges[1]",
      "edge": {
        "subject": "temperature_range_low_trait",
        "predicate": "is a",
        "object": "temperature_range",
        "description": "Temperature range low is a quantitative bin of the temperature-range phenotype.",
        "evidence": [
          {
            "reference": "DOI:10.1038/sj.embor.7400662",
            "snippet": "growing well at temperatures around the freezing point of water",
            "notes": "Supports the 10–22 °C range as a value within the temperature-range distribution."
          }
        ],
        "predicate_id": "rdfs:subClassOf"
      },
      "outcome": "positive",
      "judgment": "Actual rdfs:subClassOf is present, and the exact child/parent relation is asserted in raw METPO; inheritance is a valid positive control."
    },
    {
      "index": 2,
      "field": "causal_graphs[0].edges[2]",
      "edge": {
        "subject": "low_temperature",
        "predicate": "decreases",
        "object": "membrane_fluidity",
        "description": "Low temperature reduces membrane fluidity, triggering compensatory lipid remodeling.",
        "evidence": [
          {
            "reference": "DOI:10.1007/s42770-023-01057-4",
            "notes": "Cold reduces membrane fluidity; changes in membrane physical state mediate cold sensing."
          }
        ],
        "predicate_id": "RO:0002212"
      },
      "outcome": "major",
      "judgment": "RO2212 inherits process/process. The current subject is a cool condition and object an explicit fluidity QUALITY; quality object independently violates range."
    },
    {
      "index": 3,
      "field": "causal_graphs[0].edges[3]",
      "edge": {
        "subject": "fatty_acid_desaturase_activity",
        "predicate": "increases",
        "object": "membrane_fluidity",
        "description": "Fatty acid desaturase activity raises unsaturation to restore membrane fluidity at low temperature.",
        "evidence": [
          {
            "reference": "DOI:10.37256/amtt.5220244537",
            "notes": "Genes for desaturation are upregulated; desaturases enhance membrane fluidity via unsaturated/PUFA synthesis."
          }
        ],
        "predicate_id": "RO:0002213"
      },
      "outcome": "major",
      "judgment": "RO2213 inherits process/process. Activity subject is compatible; fluidity QUALITY object independently violates range."
    },
    {
      "index": 4,
      "field": "causal_graphs[0].edges[4]",
      "edge": {
        "subject": "low_temperature",
        "predicate": "increases",
        "object": "unsaturated_fatty_acid_proportion",
        "description": "Growth at low temperature increases the proportion of unsaturated fatty acids in membrane lipids.",
        "evidence": [
          {
            "reference": "DOI:10.1128/aem.01928-22",
            "notes": "Proportion of unsaturated fatty acids was higher in strains cultured at low temperatures while long-chain SFAs decreased."
          }
        ],
        "predicate_id": "RO:0002213"
      },
      "outcome": "major",
      "judgment": "RO2213 inherits process/process. Current cool-condition subject and relative-abundance QUALITY object are not processes; quality object independently decides failure."
    },
    {
      "index": 5,
      "field": "causal_graphs[0].edges[5]",
      "edge": {
        "subject": "cold_shock_proteins",
        "predicate": "enables",
        "object": "rna_chaperone_activity",
        "description": "Cold-shock proteins act as RNA chaperones supporting translation at low temperature.",
        "evidence": [
          {
            "reference": "DOI:10.3389/fmicb.2023.1197797",
            "notes": "Cold shock proteins (Csps) can function as RNA chaperones, supporting translation in the cold."
          }
        ],
        "predicate_id": "RO:0002327"
      },
      "outcome": "positive",
      "judgment": "RO2327 inherited material/process endpoints fit protein-family subject and molecular-activity object. This is domain/range compatibility only, not biological executor/efficacy validation."
    },
    {
      "index": 6,
      "field": "causal_graphs[0].edges[6]",
      "edge": {
        "subject": "compatible_solutes",
        "predicate": "provides",
        "object": "cryoprotection",
        "description": "Compatible solutes provide cryoprotection by stabilizing membranes and proteins and lowering freezing point.",
        "evidence": [
          {
            "reference": "DOI:10.3389/fmicb.2023.1197797",
            "notes": "Compatible osmolytes prevent cell shrinkage, lower freezing point, scavenge radicals, and stabilize membranes/proteins."
          }
        ]
      },
      "outcome": "qualified",
      "judgment": "Lexical provides has no predicate_id; do not invent imported RO constraints. Material-solute/process relation is not formally rejected; detailed efficacy unassessed."
    },
    {
      "index": 7,
      "field": "causal_graphs[0].edges[7]",
      "edge": {
        "subject": "molecular_chaperones",
        "predicate": "prevents",
        "object": "protein_misfolding",
        "description": "GroEL/DnaK chaperones prevent cold-denaturation and protein misfolding at low temperature.",
        "evidence": [
          {
            "reference": "DOI:10.37256/amtt.5220244537",
            "notes": "Chaperones are upregulated at low temperatures to prevent cold-denaturation and misfolding."
          }
        ],
        "predicate_id": "RO:0002212"
      },
      "outcome": "major",
      "judgment": "RO2212 requires process/process; current molecular-chaperone subject is a material protein family. Process object is compatible, negative direction is internally coherent."
    }
  ],
  "source": [
    {
      "index": 0,
      "field": "causal_graphs[0].edges[0]",
      "subject": "psychrotolerant_adaptation",
      "predicate": "confers",
      "object": "temperature_range_low_trait",
      "description": "Psychrotolerant adaptation enables growth across 10–22 °C.",
      "source_reference": "DOI:10.1038/sj.embor.7400662",
      "outcome": "UNASSESSED_SCOPE",
      "scope": "Supplied cold-shock phrase literal after PDF line-break dehyphenation; detailed acclimation efficacy unassessed."
    },
    {
      "index": 1,
      "field": "causal_graphs[0].edges[1]",
      "subject": "temperature_range_low_trait",
      "predicate": "is a",
      "object": "temperature_range",
      "description": "Temperature range low is a quantitative bin of the temperature-range phenotype.",
      "source_reference": "DOI:10.1038/sj.embor.7400662",
      "outcome": "PARTIAL",
      "scope": "Near-freezing phrase literal; note overstates its exact10–22 interval support."
    },
    {
      "index": 2,
      "field": "causal_graphs[0].edges[2]",
      "subject": "low_temperature",
      "predicate": "decreases",
      "object": "membrane_fluidity",
      "description": "Low temperature reduces membrane fluidity, triggering compensatory lipid remodeling.",
      "source_reference": "DOI:10.1007/s42770-023-01057-4",
      "outcome": "PARTIAL",
      "scope": "Generic cooling/phase packing context positive; sensing/regulatory efficacy unassessed."
    },
    {
      "index": 3,
      "field": "causal_graphs[0].edges[3]",
      "subject": "fatty_acid_desaturase_activity",
      "predicate": "increases",
      "object": "membrane_fluidity",
      "description": "Fatty acid desaturase activity raises unsaturation to restore membrane fluidity at low temperature.",
      "source_reference": "DOI:10.37256/amtt.5220244537",
      "outcome": "UNASSESSED_SCOPE",
      "scope": "AMTT identity positive; detailed desaturase upregulation/efficacy unassessed and body text unavailable in retained access."
    },
    {
      "index": 4,
      "field": "causal_graphs[0].edges[4]",
      "subject": "low_temperature",
      "predicate": "increases",
      "object": "unsaturated_fatty_acid_proportion",
      "description": "Growth at low temperature increases the proportion of unsaturated fatty acids in membrane lipids.",
      "source_reference": "DOI:10.1128/aem.01928-22",
      "outcome": "PARTIAL",
      "scope": "Studied B.simplex H-b abstract supports higher UFA proportion; long-chain SFA clause and generalization remain unverified by inspected text."
    },
    {
      "index": 5,
      "field": "causal_graphs[0].edges[5]",
      "subject": "cold_shock_proteins",
      "predicate": "enables",
      "object": "rna_chaperone_activity",
      "description": "Cold-shock proteins act as RNA chaperones supporting translation at low temperature.",
      "source_reference": "DOI:10.3389/fmicb.2023.1197797",
      "outcome": "UNASSESSED_SCOPE",
      "scope": "Antarctic review identity positive; detailed RNA-chaperone efficacy UNASSESSED_SCOPE."
    },
    {
      "index": 6,
      "field": "causal_graphs[0].edges[6]",
      "subject": "compatible_solutes",
      "predicate": "provides",
      "object": "cryoprotection",
      "description": "Compatible solutes provide cryoprotection by stabilizing membranes and proteins and lowering freezing point.",
      "source_reference": "DOI:10.3389/fmicb.2023.1197797",
      "outcome": "UNASSESSED_SCOPE",
      "scope": "Antarctic review identity positive; detailed osmolyte/cryoprotection/radical-defense efficacy UNASSESSED_SCOPE."
    },
    {
      "index": 7,
      "field": "causal_graphs[0].edges[7]",
      "subject": "molecular_chaperones",
      "predicate": "prevents",
      "object": "protein_misfolding",
      "description": "GroEL/DnaK chaperones prevent cold-denaturation and protein misfolding at low temperature.",
      "source_reference": "DOI:10.37256/amtt.5220244537",
      "outcome": "UNASSESSED_SCOPE",
      "scope": "AMTT identity positive; detailed chaperone regulation/efficacy UNASSESSED_SCOPE and body text unavailable."
    }
  ]
}

### Native checklist: exact canonical ledger and conditional predicate grounder

ownership: supported. Targets: METPO:1000449.

The exact SOURCES/TRANCHE canonical payload preserves a supported interval and width; coordinate its quantity interpretation with current record fields while retaining equality/no-op and nonempty-difference rejection guards. Predicate wildcard rows 60/61/65 can recreate incompatible roles in empty fields; the consumer skips current populated IDs, so ordinary replay is not a repair. Sibling node-type/review/connector hits are not promoted to current faulty owners.

### Native checklist: bounded human acceptance link

provenance: concern. Targets: METPO:1000449.

Nine embedded events comprise eight AI-assisted events and a seed. All 24 current history projections are AI and rely on exact qualified prior whole-body readings; zero new whole-history reads are claimed. Ignored- and hidden-inclusive search has 206 matching paths, 67 matching review arrays and 101 all-local arrays with zero exact target. Uncaptured leads remain matching-line context; private or remote acceptance is unknown.

### Native checklist: retained species catalog and bounded adapter availability

completeness: unknown. Targets: METPO:1000449.

The original catalog contains 20 organisms and 28 datasets; current selected-name comparison has no exact Aestuariibius violaceus or Bacillus simplex key. This does not establish global absence or permit B. subtilis/E. coli source-organism substitution. No module query was executed because the maintained runner is unavailable within bounded discovery. No strain/module/efficacy result is inferred.

### Native checklist: NONMECHANISTIC context and optional instances

completeness: supported. Targets: METPO:1000449.

Five disconnected components with thirteen nodes and eight edges are permissible contextual NONMECHANISTIC structure. Two protein classes are explicitly label-only and have zero instances; no connector, token accession or dataset is mandatory. This structural disposition does not resolve the quantity, source-attribution or formal-role findings.

### Native checklist: actual native and fresh B14 diagnostics

schema: supported. Targets: METPO:1000449.

Current inspect, focused target validation, strict validation and snippet command completed successfully. B14 common diagnostics retain original execution intervals, historical attempts, product skips and omitted full suite. These bounded software checks do not establish scientific correctness, source efficacy or human acceptance.

## Findings

### quantity-scope: Quantity scope

major / open / confirmed; issue key: temperature-range-low-quantity-scope.

The definition and graph use 10–22 °C as an absolute ambient growth interval, while canonical_examples[0].note explicitly treats 10–22 degrees as a range-width bin. The assigned primary abstract supports growth22–36 °C for the named strain, and36−22=14 is correct; it is a different quantity from ambient interval10–22. Raw METPO supplies an existential generic numeric value in[10,22] but does not specify endpoint versus width operationalization. Reconcile the quantity throughout this record and its exact maintained canonical ledger without rejecting the supported source measurement, choosing an unsupported ontology interpretation, or asserting a wrong organism.

### imported-process-roles: Imported process roles

major / open / confirmed; issue key: temperature-range-low-imported-process-roles.

RO:0002212 and RO:0002213 inherit process-to-process roles from RO:0002211. Current edges2/3/4 target explicitly stated fluidity or relative-abundance qualities; edges2/4 also use a cool ambient condition. Edge7 uses a material chaperone-protein subject with a process object. These existing referents conflict with the imported roles. Edge5 protein-to-molecular-activity endpoint fit is positive; direction and biological efficacy remain separate. Wildcard mapping rows60/61/65 can recreate these assignments in empty fields, while the grounder skips current populated IDs, so ordinary replay will not repair them.

### cold-bin-attribution: Cold bin attribution

minor / open / confirmed; issue key: temperature-range-low-cold-bin-attribution.

These notes attribute exact 10–22 °C range support to broad cold/near-freezing passages. The supplied D’Amico phrases are literal, but the inspected introduction explicitly describes a continuum with wide or narrow ranges and uses psychrophiles broadly for near-freezing growth. This supports a bounded nearest-span attribution correction, not a claim that every part of the paper lacks calibration or that its biology is false.

### human-acceptance-link: Human acceptance link

minor / open / confirmed; issue key: temperature-range-low-human-acceptance-link.

The record is REVIEWED, but its nine embedded events comprise eight AI-assisted events plus the METPO seed. All24 captured current actor projections are AI; their whole bodies are exact qualified prior readings, not new whole reads. The ignored- and hidden-inclusive bounded local search finds206matching paths,67matching review arrays and101all-local arrays with zero exact target. This local evidence does not provide an attributable human acceptance link. Private or remote acceptance remains unknown.

## Recommended Actions And Acceptance Checks

### curate-quantity-scope

In separately authorized curation, establish and document the measured-quantity contract, then reconcile definition, graph and canonical membership interpretation with the exact backfill ledger. Preserve the verified strain interval and distinguish derived width from absolute temperatures.

- Document source-backed intended quantity and unit semantics without deriving an endpoint/width contract solely from generic has-value.
- Keep the22–36source interval and36−22=14arithmetic accurate and explicitly strain-scoped; make all affected fields use one consistent contract.
- Coordinate SOURCES/TRANCHE and the existing equality/rejection guards; current correct source payload is not itself a false-measurement finding.
- Use guarded curation/history and run focused strict validation plus applicable QC/products and regenerate affected products.

### curate-imported-process-roles

Resolve the four relation identifiers against the actual existing referents; coordinate narrowly scoped mapping/consumer behavior to avoid recreating incompatible imported roles.

- For each edge2/3/4/7, document the retained subject/object referents and formal domain/range support of the chosen representation.
- Preserve correct quality and molecular-activity facets; do not relabel them merely to pass a relation check or invent biological intermediates.
- Demonstrate future empty-field grounding respects the revised semantic decision and explicitly repair current populated IDs through guarded curation; ordinary grounder replay skips them.
- Retain positive edge5 endpoint fit and lexical-edge6 scope; run focused strict validation, applicable graph/QC/products checks and meaningful grounding regression checks.

### curate-cold-bin-attribution

Revise the two evidence notes to distinguish the inspected generic cold/near-freezing support from any exact numerical-bin authority.

- Each note accurately describes its nearest inspected source span; exact10–22 calibration requires an explicitly identified supporting source or remains qualified.
- Retain all three literal snippets, including ordinary PDF line-break normalization, and preserve native1VERIFIED/2NOT_IN_ABSTRACT separately from manual full-text findings.
- Do not infer whole-paper absence or biological falsity from the bounded passages; validate the separately curated record.

### curate-human-acceptance-link

Link attributable human acceptance for the REVIEWED status or accurately qualify the review state in separately authorized curation.

- Retain actor identity, scope and retrievable acceptance reference rather than treating AI review or seed import as human signoff.
- Preserve the bounded local-search limitation and private/remote uncertainty.
- Use maintained guarded history/validation procedures if status or evidence changes.

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
| check-temperature-range-low-target-validate | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-target-validate.log; Executed 2026-10-22T03:27:58.482137+00:00 through 2026-10-22T03:27:59.076290+00:00; metadata temperature-range-low-target-validate.json | context_only | Native record validation passed; scientific interpretation is assessed separately. |
| check-temperature-range-low-target-strict | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-target-strict.log; Executed 2026-10-22T03:27:58.482225+00:00 through 2026-10-22T03:27:59.469198+00:00; metadata temperature-range-low-target-strict.json | context_only | The actual validate-strict command passed. |
| check-temperature-range-low-snippets-network | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-snippets-network.log; Executed 2026-10-22T03:28:25.354650+00:00 through 2026-10-22T03:28:27.225976+00:00; metadata temperature-range-low-snippets-network.json | context_only | Native command completed successfully: one VERIFIED and two NOT_IN_ABSTRACT, the latter inconclusive. Manual retained primary text supports all three supplied snippets, one with ordinary PDF line-break dehyphenation. Literal support does not establish adjacent exact-bin claims. |
| capture | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low.inspect.json; Actual successful native inspect with 103 captured inputs | context_only | All current source hashes and the exact target are bound before serialization. |
| record | data/traits/environment/temperature_range_low.yaml; Whole current record | supports | Thirteen nodes, eight edges, nine embedded events, one canonical example, two label-only protein classes and zero instances. |
| local-init | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/batch014-local-initialization-receipt.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Actual local initialization and tenth queue target; publication remains separate. |
| policy | docs/GROUNDING_POLICY.md; Captured maintained authority | supports | Protein family/function grounding, label-only rationale and optional instances. |
| playbook | docs/CURATION_PLAYBOOK.md; Captured maintained authority | supports | Source attribution and attributable acceptance. |
| schema | src/traitmech/schema/traitmech.yaml; Captured maintained authority | supports | Current material, molecular-activity, process, quality and quantitative NONMECHANISTIC facets. |
| predicate-mapping | mappings/predicate_grounding.tsv; Captured maintained authority | supports | Wildcard closeMatch rows 60/61/65 and conditional future empty-field predicate grounding; current populated IDs are skipped. |
| node-mapping | mappings/node_grounding.tsv; Captured maintained authority | supports | Environmental-condition and osmolyte role/bearer closeMatch qualifications; not automatic exact identity. |
| canonical-writer | scripts/backfill_canonical_examples_444.py; Captured maintained authority | supports | Exact SOURCES/TRANCHE payload and equality/rejection guards; positive measurement with coordinated quantity interpretation. |
| identity | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-grounding-agent/identity-and-hierarchy.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Active target and parent; raw generic numeric existential does not decide interval versus width. |
| nodes-edges | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-grounding-agent/node-edge-grounding-ledger.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | All thirteen current node referents and eight formal relation dispositions. |
| owners | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-grounding-agent/ownership-assessment.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Exact canonical ledger and conditional mapping/consumer applicability; no sibling writer promoted without evidence. |
| owner-primary | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-grounding-agent/owner-primary-reading.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Selected current owner windows and exact replay guards, without executing writers. |
| local-authority | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-grounding-agent/local-authority-reading.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Actual schema, policy, local proposals and mapping reading scope. |
| histories | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-grounding-agent/history-reading-provenance.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Twenty-four current actor/event projections with exact qualified prior whole readings; zero new whole-history reads. |
| embedded-history | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-grounding-agent/embedded-history-ledger.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Nine embedded events: eight AI-assisted events and one seed. |
| human-search | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-grounding-agent/search-and-provenance.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Ignored- and hidden-inclusive local search: 206 matching paths, 67 matching arrays, 101 all-local review arrays, zero exact target. |
| discovery | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-grounding-agent/discovery-dispositions.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Uncaptured leads remain matching-line context; private or remote acceptance unknown. |
| expression | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-grounding-agent/expression-and-readiness.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Two label-only protein classes and five components allowed; no exact selected catalog species key or module result. |
| expression-discovery | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-grounding-agent/adapter-discovery.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Bounded maintained-runner discovery found no available adapter; no query executed. |
| catalog-reuse | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-grounding-agent/catalog-reuse.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Original catalog acquisition preserved separately from current exact copying. |
| catalog-reading | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-grounding-agent/catalog-reading-confirmation.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Post-freeze actual whole catalog reading confirms selected-name scope; separately root-FINAL-bound, frozen manifest unchanged. |
| ground-reading | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-grounding-agent/reading-scope-receipt.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Exact current reading scopes, qualified prior histories and retained scratch-preparation corrections. |
| ground-assessment | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-grounding-agent/grounding-assessment.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Two ground majors include the shared quantity finding counted once; bounded human minor. |
| ground-manifest | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-grounding-agent/evidence-manifest.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | All 27 immutable ground artifacts verified. |
| ontology-primary | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-source-root/selected-ontology-primary.json; Exact selected response; original query 2026-10-22T03:28:27.266410+00:00 through 2026-10-22T03:28:27.273083+00:00 | supports | Current RO/PATO/CHEBI or raw METPO/local-proposal authority; retained earlier CHEBI ancestry only, not prior-record judgments. Copy time is not query time. |
| authority-primary | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-source-root/selected-authority-primary.json; Exact selected response; original query 2026-10-22T03:28:27.273503+00:00 through 2026-10-22T03:28:27.291580+00:00 | supports | Current RO/PATO/CHEBI or raw METPO/local-proposal authority; retained earlier CHEBI ancestry only, not prior-record judgments. Copy time is not query time. |
| chebi-ancestry | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-source-root/selected-authority-primary.json; Exact selected response; original query 2026-10-22T02:55:21.732289+00:00 through 2026-10-22T02:55:21.754582+00:00 | supports | Current RO/PATO/CHEBI or raw METPO/local-proposal authority; retained earlier CHEBI ancestry only, not prior-record judgments. Copy time is not query time. |
| authority-provenance | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-grounding-agent/primary-reuse-provenance.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Corrected original query clocks and exact current copies; no new database rehash. |
| catalog-original | https://imodulondb.org/api/datasets; Original retained 20-organism/28-dataset catalog | context_only | No exact selected Aestuariibius violaceus or Bacillus simplex name key within this retained catalog. No global absence, current B. subtilis/E. coli source substitution or strain/module inference. |
| damico-metadata | DOI:10.1038/sj.embor.7400662; Indexed identity and generic physical fragment | supports | Broad cold classification does not calibrate the exact current numerical bin. |
| damico-pdf | DOI:10.1038/sj.embor.7400662; Retained author-repository PDF; selected introduction and supplied snippet spans | supports | Broad near-freezing classification and variable ranges are positive; three existing snippets supported, one with ordinary line-break dehyphenation. |
| cold-metadata | DOI:10.1007/s42770-023-01057-4; Indexed identity only | supports | Detailed stress-defense and regulatory efficacy remain unassessed. |
| cold-body | DOI:10.1007/s42770-023-01057-4; All-HTML paragraph 17 sentences 1–2, physical phase/packing context; paragraph 10 first classification sentence only | supports | Generic physical context is positive. Incidentally displayed paragraph 17 sentence 5 is not adopted as detailed efficacy. |
| amtt-zero-hit | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.37256/amtt.5220244537&amp;format=json&amp;resultType=core; Original successful indexed response with zero matches | context_only | Retrieval diagnostic with positive Crossref identity; not a missing-paper finding. |
| amtt-crossref | DOI:10.37256/amtt.5220244537; Original Crossref title/identifier/date | supports | Source identity positive despite indexed zero-hit; detailed desaturase/chaperone claims unassessed and retained body access unavailable. |
| yang-metadata | DOI:10.1128/aem.01928-22; Identity and the supplied single abstract UFA observation | supports | Bacillus simplex H-b cohort context only; no universal, exact-bin or long-chain-SFA inference. |
| antarctic-metadata | DOI:10.3389/fmicb.2023.1197797; Indexed identity/title only | supports | Detailed RNA/chaperone/cryoprotection efficacy remains UNASSESSED_SCOPE. |
| antarctic-body | DOI:10.3389/fmicb.2023.1197797; Article-title only; body count machine-enumerated without body reading | supports | Retained XML availability does not imply current whole-article scientific reading or detailed efficacy assessment. |
| damico-derived | DOI:10.1038/sj.embor.7400662; Retained derived PDF reading text: newline 24–33 classification; 10, 56–57 and 32–33 supplied snippets | supports | Timestamp is original text extraction completion, not PDF acquisition. No current extraction or whole-paper review is claimed. |
| damico-extraction | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-source-agent/damico-derivation-receipt.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Original PDF/text bindings and extraction interval separate from original retrieval and current copying. |
| canonical-metadata | DOI:10.1099/ijsem.0.006834; Current indexed primary abstract: named strain/type identities and reported growth interval only | supports | Reported 22–36 °C interval and derived width 14 are positive at the cited strain scope. They do not settle whether this record denotes ambient endpoints or a width bin. |
| canonical-access | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-source-agent/canonical-metadata-access.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Actual current metadata request interval; no new body or cultivation optimization assessment. |
| yang-body-failure | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-source-agent/yang-original-body-access.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Original HTTP500 body-access receipt; no body available through that attempt and no content-refutation inference. |
| amtt-prior-access | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-source-agent/amtt-prior-access-observation.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Derived historical browser/PDF failure observation; its recorded_at is an observation-write clock, not an acquisition. Original call interval uninstrumented. |
| taxonomy | NCBITaxon:3234132; Fresh successful official species/type-material response | supports | Aestuariibius violaceus species and named type-material identities positive; no quantitative phenotype inferred from taxonomy. |
| taxonomy-access | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-grounding-agent/taxonomy-retry-access.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Actual successful retry interval and hash. |
| taxonomy-reading | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-grounding-agent/taxonomy-identity.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Official identity, original successful response and initial failed-access distinction. |
| taxonomy-initial-failure | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=3234132&amp;retmode=xml; Initial DNS error bytes, not taxonomy XML | context_only | Access failure is retained separately from successful retry and native validation. |
| sources | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-source-agent/source-assessment.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Six works; quantity conflict and bounded nearest-span attribution concern, with detailed efficacy unassessed. |
| source-identities | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-source-agent/source-ledger.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | All six identities and selected scopes; AMTT Crossref positive, original metadata notices not refreshed. |
| source-status | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-source-agent/source-status-ledger.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Original-time notice observations, not an exhaustive fresh status search. |
| placements | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-source-agent/source-placement-ledger.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | All eleven external placements; twelve grounding fields are separately covered by node-edge audits. |
| snippets | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-source-agent/snippet-ledger.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | All three supplied snippets literal after ordinary PDF typography handling in one span. |
| notes | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-source-agent/source-note-ledger.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Ten notes including the singular canonical note; exact-bin attribution distinct from literal text. |
| source-nodes-edges | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-source-agent/node-edge-source-ledger.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | All thirteen nodes and eight edges with exact supported, partial and unassessed dispositions. |
| canonical | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-source-agent/canonical-assessment.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Named source interval and derived width positive, with incompatible current quantity interpretations grouped once. |
| source-reading | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-source-agent/primary-reading-scope.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Selected identity, physical/classification text and existing literal spans; no whole-paper or detailed efficacy review. |
| source-access | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-source-agent/source-access-limits.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Retained actual primary surfaces, historical access limits and one new canonical metadata request. |
| source-reuse | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-source-agent/source-reuse-receipt.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Fourteen exact copies with flat original-access clocks and retained prior-receipt hashes. |
| source-native | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-source-agent/native-context.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Native one VERIFIED/two NOT_IN_ABSTRACT and separate manual three literal results. |
| source-manifest | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-source-agent/evidence-manifest.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | All thirty frozen source artifacts verified. |
| root-reading | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-source-root/selected-primary-reading.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Root selected source/authority/owner readings; primary measurement and bounded cold-bin attribution distinguished. |
| root-verification | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-source-root/root-current-verification.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Root 103 inputs, 57 frozen artifacts, 24 qualified prior-history bindings and all 101 current review arrays verified. |
| adjudication | /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-root-adjudication.json; Final root adjudication | supports | Exact two majors and two minors, four findings/actions and exact owner/field scopes control this combined review. |

## Limits And Additional Notes

- Full just test was NOT_RUN under the selected review-only diagnostic scope; only the five focused Stage2 tests are recorded. Products retains 123 no-adapter skips. Common checks establish bounded software/data integrity, not scientific support.
- Detailed microbial heat/cold defense, survival/fitness, cultivation optimization, regulation, molecular enhancement and intervention efficacy remain UNASSESSED_SCOPE. No operational repair is proposed.
- Current quantity prose mixes absolute temperature interval and interval width; primary canonical measurement/arithmetic are positive but do not settle which quantity the record should encode.
- D’Amico selected introduction supports broad near-freezing classification with variable ranges, not the exact10–22 attribution made by current notes. No whole-paper absence assertion.
- All three snippets supported by retained author-repository PDF text; one requires ordinary linebreak dehyphenation. Native1VERIFIED2NOT_IN_ABSTRACT remains separate.
- Only selected primary text adopted. Full metadata abstract display included incidental canonical chemistry/taxonomic details; not adopted beyond identity/temperature/type strain.
- Ramón paragraph17 sentence5 was incidentally displayed while filtering; only sentences1–2 physical phase/packing context adopted.
- Yang study is Bacillus simplex H-b; its selected abstract UFA observation is not general proof of all strains, long-chain-SFA clause, exact bin, or detailed adaptation efficacy. Historical body request failed.
- Frontiers1197797 retained XML is available but inspected current identity/title only; detailed RNA/cryoprotection passages deliberately unassessed.
- AMTT indexed zero-hit does not mean DOI missing: Crossref identity positive. Actual historical publisher/PDF access failure leaves body claims unresolved; no fresh body acquisition.
- Metadata/publication notice observations remain tied to original request times; current copy/read times are not acquisitions.
- No exact-source species/catalog inference from uninspected body passages; source identity alone does not establish strain/module/phenotype coverage.
- Detailed biological efficacy, stress-defense, cold survival, cryoprotection, regulatory and cultivation optimization are UNASSESSED_SCOPE.
- CHEBI role/bearer closeMatch is qualified, not forced wrong-identifier finding.
- Raw numeric existential restriction does not specify interval versus width operationalization.
- All 24 history bodies are exact prior whole-reading qualifications, with current actor/event projections; no fresh whole-history claim.
- Uncaptured discovery leads remain matching-line context only; private/remote human review unknown.
- No common-corpus or database rehash repeated. Source findings are independently owned by source auditor.
- Active target/parent and copied upstream synonyms are positive; exact biological equivalence of broad aliases remains unresolved, not a separate forced synonym finding.
- Five disconnected components are permitted contextual NONMECHANISTIC structure; no forced connector, token protein instance or dataset.
- PATO relatively-low condition and v3fluidity quality are positive; CHEBI osmolyte role/bearer closeMatch is qualified rather than declared exact identity.
- Broad local v8confers does not inherit ROexecutor restrictions from its cross-reference. Edge5 formal endpoint fit does not verify physiological executor efficacy.
- Current canonical taxonomy is official species/type-material identity only. Retained20-organism28-dataset catalog has no exact selected canonical/B.simplex name; no B.subtilis/E.coli source-organism substitution or global absence inference.
- Publication remains separate from this local scientific review; no record, ontology, history, mapping, generated product or provider run is changed.
- Historical products failures/retry and original cache provenance remain in /private/tmp/traitmech-record-sweep-014.q8m4v2cs/new-base-diagnostic-independent-review-agent/fresh-products-completion.json. The earlier outstanding-products status is superseded by the actual fresh run; no blanket cross-batch reuse qualification is asserted.
- Final fields, categories, severities, owners and actions come only from actual root FINAL. The shared source/ground quantity conflict is counted once, alongside one formal-role major and two bounded minors.
- This serializer adopts frozen audits and root adjudication. Original source/catalog acquisitions, PDF extraction, current metadata request, exact copies/readings and failed/successful taxonomy requests retain separate clocks. Static serializer preparation does not claim another whole-paper review or fresh whole-history readings. Root execution and native output validation are separate; no scientific record, state, Git or publication change is performed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T034008Z-temperature-range-low
kind: record
repository: CultureBotAI/TraitMech
title: Whole-record review of temperature range low
started_at: '2026-10-22T03:27:28.607294Z'
finished_at: '2026-10-22T03:40:08Z'
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
summary: 'Whole-record review identifies two major issues: conflicting ambient-interval
  versus range-width semantics, and incompatible imported process roles at four edges.
  Two bounded minors concern nearest-source exact-bin attribution and a retrievable
  human-acceptance link. Active identity, source-resolved canonical22–36interval/14width,
  three literal snippets and several formal endpoint facets are positive; detailed
  microbial efficacy remains unassessed.'
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
  - path: data/traits/environment/temperature_range_low.yaml
    sha256: 88f9b9beb20b6a02eb878596af1e2fefc2de88c9f79eabd8cf4a5ed07510a3c8
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
  - path: history/infrastructure/protein-vs-activity/2026-08-15T202806Z-claude-code-ddcd62.yaml
    sha256: 58f55f2617869c39eb6412455c0d838b350433ff0ad979c848be1df9bcb3fd4f
    role: context
  - path: history/infrastructure/trait-priority/2026-08-19T203529Z-claude-code-fbfb40.yaml
    sha256: 5337f34a01bb7f39da1e604544e839a3e42d558069ff2cf52706fb5b05286766
    role: context
  - path: history/other/canonical-examples-batch1/2026-08-20T074839Z-claude-code-6fb2f5.yaml
    sha256: c938f2928f2eb41505d58c2fb72d8de01d99534d766de9af400010e8778988a4
    role: context
  - path: history/records/temperature_optimum_very_low/2026-09-04T210000Z-codex-183.yaml
    sha256: d2dff988a235fc27369f305585f4e865266f3dabf23fa06670a6e30a415f2f6e
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
  - path: research/traits/environment/temperature_range_low-deep-research-falcon.md
    sha256: 65b1e96996c48f0a6d8b7f9ff26d8f97cfddd09095dbea481400b51cdeef7073
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
- target_id: METPO:1000449
  path: data/traits/environment/temperature_range_low.yaml
  label: temperature range low
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_range_low.yaml
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
  selection: Tenth record in the actual B14 queue; current 253-line target and 103
    captured inputs. Local review is independent of remote publication.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - METPO:1000449
checks:
- check_id: new-base-qc
  name: Fresh B14 corpus QC
  status: passed
  required: true
  target_ids:
  - METPO:1000449
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
  - METPO:1000449
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
  - METPO:1000449
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
  - METPO:1000449
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
- check_id: temperature-range-low-target-validate
  name: Focused native validation
  status: passed
  required: true
  target_ids:
  - METPO:1000449
  command: just validate data/traits/environment/temperature_range_low.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Native record validation passed; scientific interpretation is assessed
    separately.
  evidence_ids:
  - check-temperature-range-low-target-validate
- check_id: temperature-range-low-target-strict
  name: Focused strict validation
  status: passed
  required: true
  target_ids:
  - METPO:1000449
  command: just validate-strict data/traits/environment/temperature_range_low.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: The actual validate-strict command passed.
  evidence_ids:
  - check-temperature-range-low-target-strict
- check_id: temperature-range-low-snippets-network
  name: Focused network snippet check
  status: passed
  required: true
  target_ids:
  - METPO:1000449
  command: just verify-snippets --record data/traits/environment/temperature_range_low.yaml
    --out /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-snippets.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 'Native command completed successfully: one VERIFIED and two NOT_IN_ABSTRACT,
    the latter inconclusive. Manual retained primary text supports all three supplied
    snippets, one with ordinary PDF line-break dehyphenation. Literal support does
    not establish adjacent exact-bin claims.'
  evidence_ids:
  - check-temperature-range-low-snippets-network
- check_id: native-inspect
  name: One-target native review capture
  status: passed
  required: true
  target_ids:
  - METPO:1000449
  command: uv run python scripts/record_review.py inspect --targets /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low.targets.json
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
    --input history/infrastructure/protein-vs-activity/2026-08-15T202806Z-claude-code-ddcd62.yaml
    --input history/infrastructure/trait-priority/2026-08-19T203529Z-claude-code-fbfb40.yaml
    --input history/other/canonical-examples-batch1/2026-08-20T074839Z-claude-code-6fb2f5.yaml
    --input history/records/temperature_optimum_very_low/2026-09-04T210000Z-codex-183.yaml
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
    --input research/traits/environment/temperature_range_low-deep-research-falcon.md
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
  summary: One current target, 103 captured inputs, exact current base and successful
    native inspect.
  evidence_ids:
  - capture
- check_id: uniprot-applicability
  name: Protein-instance metadata applicability
  status: not_applicable
  required: false
  target_ids:
  - METPO:1000449
  summary: Two contextual protein aggregates have explicit label-only rationales and
    zero instances; no token accession required.
  evidence_ids:
  - record
  - policy
  - expression
- check_id: expression-adapter-availability
  name: Structured source-organism expression query availability
  status: unavailable
  required: false
  target_ids:
  - METPO:1000449
  summary: Bounded maintained-runner discovery found no available adapter. Retained
    catalog and selected source identities provide no exact species/strain/module
    or efficacy result.
  evidence_ids:
  - expression
  - expression-discovery
  - catalog-reading
  - catalog-original
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
- evidence_id: check-temperature-range-low-target-validate
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-target-validate.log
  locator: Executed 2026-10-22T03:27:58.482137+00:00 through 2026-10-22T03:27:59.076290+00:00;
    metadata temperature-range-low-target-validate.json
  accessed_at: '2026-10-22T03:27:59.076290Z'
  support: context_only
  summary: Native record validation passed; scientific interpretation is assessed
    separately.
  snapshot_sha256: 6a1aefdef1b7ff0ef92edef18c534c9cb16f75f252af380bbc6b99a308955d7e
- evidence_id: check-temperature-range-low-target-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-target-strict.log
  locator: Executed 2026-10-22T03:27:58.482225+00:00 through 2026-10-22T03:27:59.469198+00:00;
    metadata temperature-range-low-target-strict.json
  accessed_at: '2026-10-22T03:27:59.469198Z'
  support: context_only
  summary: The actual validate-strict command passed.
  snapshot_sha256: e3456b4c79bc37267e5475591150bec0accb8c23c35a0404cfbc3404f87372d4
- evidence_id: check-temperature-range-low-snippets-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-snippets-network.log
  locator: Executed 2026-10-22T03:28:25.354650+00:00 through 2026-10-22T03:28:27.225976+00:00;
    metadata temperature-range-low-snippets-network.json
  accessed_at: '2026-10-22T03:28:27.225976Z'
  support: context_only
  summary: 'Native command completed successfully: one VERIFIED and two NOT_IN_ABSTRACT,
    the latter inconclusive. Manual retained primary text supports all three supplied
    snippets, one with ordinary PDF line-break dehyphenation. Literal support does
    not establish adjacent exact-bin claims.'
  snapshot_sha256: edf5f225a46b222ea6bbb37f1826aaeb1b8ac4d185999833fd2e3cc43ba49477
- evidence_id: capture
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low.inspect.json
  locator: Actual successful native inspect with 103 captured inputs
  accessed_at: '2026-10-22T03:27:29.278910Z'
  support: context_only
  summary: All current source hashes and the exact target are bound before serialization.
  snapshot_sha256: 317e022916ae0fe1105b0510ea980667ea443d8e5c98f51d3e7faa3e407d151d
- evidence_id: record
  kind: record_content
  reference: data/traits/environment/temperature_range_low.yaml
  locator: Whole current record
  accessed_at: '2026-10-22T03:27:29.278910Z'
  support: supports
  summary: Thirteen nodes, eight edges, nine embedded events, one canonical example,
    two label-only protein classes and zero instances.
  snapshot_sha256: 88f9b9beb20b6a02eb878596af1e2fefc2de88c9f79eabd8cf4a5ed07510a3c8
- evidence_id: local-init
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/batch014-local-initialization-receipt.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T01:07:39.713898Z'
  support: context_only
  summary: Actual local initialization and tenth queue target; publication remains
    separate.
  snapshot_sha256: 3dade2205affd0bd7eea4b7d5018e8c97080db55bba3620e89cf4a4da4123fa3
- evidence_id: policy
  kind: authority
  reference: docs/GROUNDING_POLICY.md
  locator: Captured maintained authority
  accessed_at: '2026-10-22T03:32:07.542076Z'
  support: supports
  summary: Protein family/function grounding, label-only rationale and optional instances.
  snapshot_sha256: 891678c983c2283a47c81c47950b35753981e9339d105f3bbdda92a1f5ab7f42
- evidence_id: playbook
  kind: authority
  reference: docs/CURATION_PLAYBOOK.md
  locator: Captured maintained authority
  accessed_at: '2026-10-22T03:32:07.542076Z'
  support: supports
  summary: Source attribution and attributable acceptance.
  snapshot_sha256: 735e9b810471da9f7d8364e35ffe1e741edb3421480dac01727db6ea5aa65da9
- evidence_id: schema
  kind: authority
  reference: src/traitmech/schema/traitmech.yaml
  locator: Captured maintained authority
  accessed_at: '2026-10-22T03:32:07.542076Z'
  support: supports
  summary: Current material, molecular-activity, process, quality and quantitative
    NONMECHANISTIC facets.
  snapshot_sha256: 46c47fc627b80ccbba1e8ab3fb6f2aee93bc2aef7aaf72fe9aadc3257f2c02dd
- evidence_id: predicate-mapping
  kind: authority
  reference: mappings/predicate_grounding.tsv
  locator: Captured maintained authority
  accessed_at: '2026-10-22T03:32:07.542076Z'
  support: supports
  summary: Wildcard closeMatch rows 60/61/65 and conditional future empty-field predicate
    grounding; current populated IDs are skipped.
  snapshot_sha256: 8e28c19e93aca3dc164a3befbe2612b289241de457c59f499e65936c03b7ce52
- evidence_id: node-mapping
  kind: authority
  reference: mappings/node_grounding.tsv
  locator: Captured maintained authority
  accessed_at: '2026-10-22T03:32:07.542076Z'
  support: supports
  summary: Environmental-condition and osmolyte role/bearer closeMatch qualifications;
    not automatic exact identity.
  snapshot_sha256: d7de9b3ab04960c4775a5bc295a945bd1a72d81467830459f4793e654f82b3d0
- evidence_id: canonical-writer
  kind: authority
  reference: scripts/backfill_canonical_examples_444.py
  locator: Captured maintained authority
  accessed_at: '2026-10-22T03:32:07.542076Z'
  support: supports
  summary: Exact SOURCES/TRANCHE payload and equality/rejection guards; positive measurement
    with coordinated quantity interpretation.
  snapshot_sha256: 18ca0766789c239d693ef665e8b1d43c1209a0f414a326f1c5d890f88de7b20c
- evidence_id: identity
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-grounding-agent/identity-and-hierarchy.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T03:32:07.537713Z'
  support: context_only
  summary: Active target and parent; raw generic numeric existential does not decide
    interval versus width.
  snapshot_sha256: a648ca88422eb1b99046c7a57d8d97bea86d4f3c6fee0566b88f449afcff3d06
- evidence_id: nodes-edges
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-grounding-agent/node-edge-grounding-ledger.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T03:32:07.537584Z'
  support: context_only
  summary: All thirteen current node referents and eight formal relation dispositions.
  snapshot_sha256: 38c98297ee3cd159eb0b0a5465735f219d86ca1b73a53a35153277e7c74260bd
- evidence_id: owners
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-grounding-agent/ownership-assessment.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T03:32:07.541226Z'
  support: context_only
  summary: Exact canonical ledger and conditional mapping/consumer applicability;
    no sibling writer promoted without evidence.
  snapshot_sha256: 8040182e2d7a8b54223df5109d1bac775599ce0a3edd70fa3b00a03edd8ee8e3
- evidence_id: owner-primary
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-grounding-agent/owner-primary-reading.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T03:32:07.534717Z'
  support: context_only
  summary: Selected current owner windows and exact replay guards, without executing
    writers.
  snapshot_sha256: 2b40329d491db58f878f34f71b0b2b234c033df49b80b93a010b678b0456b9ee
- evidence_id: local-authority
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-grounding-agent/local-authority-reading.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T03:32:07.536793Z'
  support: context_only
  summary: Actual schema, policy, local proposals and mapping reading scope.
  snapshot_sha256: 2bcd9b016ad3a49b441fcf70af2a64026f42dddba84b1105eee04e41092f1863
- evidence_id: histories
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-grounding-agent/history-reading-provenance.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T03:32:07.531604Z'
  support: context_only
  summary: Twenty-four current actor/event projections with exact qualified prior
    whole readings; zero new whole-history reads.
  snapshot_sha256: cf1f6a61b0d34e9e0b10ee4380d52e07bd72f4c2b0ee6054f3c6349f34cec2d6
- evidence_id: embedded-history
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-grounding-agent/embedded-history-ledger.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T03:32:07.531852Z'
  support: context_only
  summary: 'Nine embedded events: eight AI-assisted events and one seed.'
  snapshot_sha256: 99cebc4cab705274ebc2c50f2c41af04dc883c5352609bacb2a0248bb6e0c1bc
- evidence_id: human-search
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-grounding-agent/search-and-provenance.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T03:30:03.162299Z'
  support: context_only
  summary: 'Ignored- and hidden-inclusive local search: 206 matching paths, 67 matching
    arrays, 101 all-local review arrays, zero exact target.'
  snapshot_sha256: 6271991ae397cf7e781d3f351476ad81761b20c78f705cce3e62f4217bfcdf0c
- evidence_id: discovery
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-grounding-agent/discovery-dispositions.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T03:32:07.541094Z'
  support: context_only
  summary: Uncaptured leads remain matching-line context; private or remote acceptance
    unknown.
  snapshot_sha256: af282a42d92a460a5d4ef163c98070038838b8813cc940be9a87cd44cb202c6c
- evidence_id: expression
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-grounding-agent/expression-and-readiness.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T03:32:07.541919Z'
  support: context_only
  summary: Two label-only protein classes and five components allowed; no exact selected
    catalog species key or module result.
  snapshot_sha256: 40b130f471586bab65e4e7d7100ff98be5f4fcf125d28a86f2af5c47826cff79
- evidence_id: expression-discovery
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-grounding-agent/adapter-discovery.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T03:30:03.292701Z'
  support: context_only
  summary: Bounded maintained-runner discovery found no available adapter; no query
    executed.
  snapshot_sha256: 8cb5ee9c4ec5b7fdbe713c7ae650c698eb19295c8410ffdf91617ba6ec0d2c55
- evidence_id: catalog-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-grounding-agent/catalog-reuse.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T03:32:07.541835Z'
  support: context_only
  summary: Original catalog acquisition preserved separately from current exact copying.
  snapshot_sha256: bac583d133f63f2711f921a3b99b6fbd586f09ee0aac9f14d7162c942304b757
- evidence_id: catalog-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-grounding-agent/catalog-reading-confirmation.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T03:32:26.830335Z'
  support: context_only
  summary: Post-freeze actual whole catalog reading confirms selected-name scope;
    separately root-FINAL-bound, frozen manifest unchanged.
  snapshot_sha256: c84ee56f07ce20380ed73657f152d9713ce1cebb7b8013f6566d44d035ba0b90
- evidence_id: ground-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-grounding-agent/reading-scope-receipt.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T03:32:07.542241Z'
  support: context_only
  summary: Exact current reading scopes, qualified prior histories and retained scratch-preparation
    corrections.
  snapshot_sha256: 5c2335e0ca2b656b478a87764344601f7333c28d5af69d918beab3bb7ceac88d
- evidence_id: ground-assessment
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-grounding-agent/grounding-assessment.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T03:32:07.542076Z'
  support: context_only
  summary: Two ground majors include the shared quantity finding counted once; bounded
    human minor.
  snapshot_sha256: e8c47e45459c03cf556d1b3fa5f3550e75f2af0fecf2e87e7cc728e321186c2f
- evidence_id: ground-manifest
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-grounding-agent/evidence-manifest.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T03:32:07.558525Z'
  support: context_only
  summary: All 27 immutable ground artifacts verified.
  snapshot_sha256: 03599d084d14bc1aebd3d9429094105e8d49f6d5076461c98b33e9dfc139eecd
- evidence_id: ontology-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-source-root/selected-ontology-primary.json
  locator: Exact selected response; original query 2026-10-22T03:28:27.266410+00:00
    through 2026-10-22T03:28:27.273083+00:00
  accessed_at: '2026-10-22T03:28:27.273083Z'
  support: supports
  summary: Current RO/PATO/CHEBI or raw METPO/local-proposal authority; retained earlier
    CHEBI ancestry only, not prior-record judgments. Copy time is not query time.
  snapshot_sha256: 67182239e2535f4e19a89f116e235fda4ceb456e557b82f915f13272596b4186
- evidence_id: authority-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-source-root/selected-authority-primary.json
  locator: Exact selected response; original query 2026-10-22T03:28:27.273503+00:00
    through 2026-10-22T03:28:27.291580+00:00
  accessed_at: '2026-10-22T03:28:27.291580Z'
  support: supports
  summary: Current RO/PATO/CHEBI or raw METPO/local-proposal authority; retained earlier
    CHEBI ancestry only, not prior-record judgments. Copy time is not query time.
  snapshot_sha256: 6e40130f6aa3c9693f06e6125cc9553925ddae3d923826d2abc9542f94873904
- evidence_id: chebi-ancestry
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-source-root/selected-authority-primary.json
  locator: Exact selected response; original query 2026-10-22T02:55:21.732289+00:00
    through 2026-10-22T02:55:21.754582+00:00
  accessed_at: '2026-10-22T02:55:21.754582Z'
  support: supports
  summary: Current RO/PATO/CHEBI or raw METPO/local-proposal authority; retained earlier
    CHEBI ancestry only, not prior-record judgments. Copy time is not query time.
  snapshot_sha256: 85ebea792fb0323ceb45b60496657e2a7280c9123d625d050fedd208cf7f0646
- evidence_id: authority-provenance
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-grounding-agent/primary-reuse-provenance.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T03:32:07.523633Z'
  support: context_only
  summary: Corrected original query clocks and exact current copies; no new database
    rehash.
  snapshot_sha256: 05285c46a64b4fb602e7a4be76d3f70e1d41468021bf7280572aa6b75531a76c
- evidence_id: catalog-original
  kind: authority
  reference: https://imodulondb.org/api/datasets
  locator: Original retained 20-organism/28-dataset catalog
  accessed_at: '2026-10-21T07:36:12.858149Z'
  support: context_only
  summary: No exact selected Aestuariibius violaceus or Bacillus simplex name key
    within this retained catalog. No global absence, current B. subtilis/E. coli source
    substitution or strain/module inference.
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: damico-metadata
  kind: primary_source
  reference: DOI:10.1038/sj.embor.7400662
  locator: Indexed identity and generic physical fragment
  accessed_at: '2026-10-21T10:00:01.461116Z'
  support: supports
  summary: Broad cold classification does not calibrate the exact current numerical
    bin.
  snapshot_sha256: 24d64254a2baba7c573dff7ae523cc0e00d30e297c4f1fd7aa3a23c51a057059
- evidence_id: damico-pdf
  kind: primary_source
  reference: DOI:10.1038/sj.embor.7400662
  locator: Retained author-repository PDF; selected introduction and supplied snippet
    spans
  accessed_at: '2026-10-21T10:03:39.641646Z'
  support: supports
  summary: Broad near-freezing classification and variable ranges are positive; three
    existing snippets supported, one with ordinary line-break dehyphenation.
  snapshot_sha256: 5a7678c6418efbcccf54d91c55eea1c08f2a4ed0ce0e07a6995d5903b9a0eb2e
- evidence_id: cold-metadata
  kind: primary_source
  reference: DOI:10.1007/s42770-023-01057-4
  locator: Indexed identity only
  accessed_at: '2026-10-21T22:07:08.865512Z'
  support: supports
  summary: Detailed stress-defense and regulatory efficacy remain unassessed.
  snapshot_sha256: da5cffab81fe0e039c6fcec8f318b2715f5604eaf8722ea6f63f944178ed447b
- evidence_id: cold-body
  kind: primary_source
  reference: DOI:10.1007/s42770-023-01057-4
  locator: All-HTML paragraph 17 sentences 1–2, physical phase/packing context; paragraph
    10 first classification sentence only
  accessed_at: '2026-10-21T22:07:50.938485Z'
  support: supports
  summary: Generic physical context is positive. Incidentally displayed paragraph
    17 sentence 5 is not adopted as detailed efficacy.
  snapshot_sha256: bb09a59c07f43ff0af177f89b624c8b5d4841e513ed0d478120954a016342889
- evidence_id: amtt-zero-hit
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.37256/amtt.5220244537&format=json&resultType=core
  locator: Original successful indexed response with zero matches
  accessed_at: '2026-10-22T00:29:26.622156Z'
  support: context_only
  summary: Retrieval diagnostic with positive Crossref identity; not a missing-paper
    finding.
  snapshot_sha256: d0eef7c61f38fab3f0b2a3d73127915d63da077e0617bff6ac487ec290045df3
- evidence_id: amtt-crossref
  kind: primary_source
  reference: DOI:10.37256/amtt.5220244537
  locator: Original Crossref title/identifier/date
  accessed_at: '2026-10-22T00:29:26.281512Z'
  support: supports
  summary: Source identity positive despite indexed zero-hit; detailed desaturase/chaperone
    claims unassessed and retained body access unavailable.
  snapshot_sha256: 9f5ed8f0f9d07aface3f482bc888a6c47a4d9683abf51f76b16bf56412857cf7
- evidence_id: yang-metadata
  kind: primary_source
  reference: DOI:10.1128/aem.01928-22
  locator: Identity and the supplied single abstract UFA observation
  accessed_at: '2026-10-22T02:05:33.257647Z'
  support: supports
  summary: Bacillus simplex H-b cohort context only; no universal, exact-bin or long-chain-SFA
    inference.
  snapshot_sha256: 1d858d0cfbe3cd7842374a0b6d7453e4fad6959494b59b775880f473ca5c2195
- evidence_id: antarctic-metadata
  kind: primary_source
  reference: DOI:10.3389/fmicb.2023.1197797
  locator: Indexed identity/title only
  accessed_at: '2026-10-21T10:00:02.068795Z'
  support: supports
  summary: Detailed RNA/chaperone/cryoprotection efficacy remains UNASSESSED_SCOPE.
  snapshot_sha256: d1315a25547237a1d13ab9a9cb37c9a3cc9bfb2c9c393eb6a45e5ad108d78104
- evidence_id: antarctic-body
  kind: primary_source
  reference: DOI:10.3389/fmicb.2023.1197797
  locator: Article-title only; body count machine-enumerated without body reading
  accessed_at: '2026-10-21T10:00:47.316930Z'
  support: supports
  summary: Retained XML availability does not imply current whole-article scientific
    reading or detailed efficacy assessment.
  snapshot_sha256: a5d04369d769d107921d98c6892695ea59f8682f2823bc8e60e198f464666bce
- evidence_id: damico-derived
  kind: primary_source
  reference: DOI:10.1038/sj.embor.7400662
  locator: 'Retained derived PDF reading text: newline 24–33 classification; 10, 56–57
    and 32–33 supplied snippets'
  accessed_at: '2026-10-21T21:57:11.990598Z'
  support: supports
  summary: Timestamp is original text extraction completion, not PDF acquisition.
    No current extraction or whole-paper review is claimed.
  snapshot_sha256: 71ef77b88e880420f533454926cac17498cbf8db380465139c888057115143e8
- evidence_id: damico-extraction
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-source-agent/damico-derivation-receipt.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-21T21:57:11.990598Z'
  support: context_only
  summary: Original PDF/text bindings and extraction interval separate from original
    retrieval and current copying.
  snapshot_sha256: 4bc68e1e7c942f28f8b2be82ef5b82e45461cdec22ed95828753130bc433d1ac
- evidence_id: canonical-metadata
  kind: primary_source
  reference: DOI:10.1099/ijsem.0.006834
  locator: 'Current indexed primary abstract: named strain/type identities and reported
    growth interval only'
  accessed_at: '2026-10-22T03:28:55.673544Z'
  support: supports
  summary: Reported 22–36 °C interval and derived width 14 are positive at the cited
    strain scope. They do not settle whether this record denotes ambient endpoints
    or a width bin.
  snapshot_sha256: 8ddd3b939b3102cd35d5ce0297d6f46d553a95ca3258ed7f20d8df96cb388e65
- evidence_id: canonical-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-source-agent/canonical-metadata-access.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T03:28:55.673544Z'
  support: context_only
  summary: Actual current metadata request interval; no new body or cultivation optimization
    assessment.
  snapshot_sha256: 3ce98a37000798b4e1252ae3996509b676c1ca41f3a2ae542d5a7afe3a2a91ed
- evidence_id: yang-body-failure
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-source-agent/yang-original-body-access.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T02:06:02.620486Z'
  support: context_only
  summary: Original HTTP500 body-access receipt; no body available through that attempt
    and no content-refutation inference.
  snapshot_sha256: 55f61be6fa4dfd221261c92b264129d281f2eb7f8b120c466fca1245e79e81cd
- evidence_id: amtt-prior-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-source-agent/amtt-prior-access-observation.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T03:31:45.742491Z'
  support: context_only
  summary: Derived historical browser/PDF failure observation; its recorded_at is
    an observation-write clock, not an acquisition. Original call interval uninstrumented.
  snapshot_sha256: 256b97600bdeb4f786d141306201028634b29cdcbd009b726127599944350bdb
- evidence_id: taxonomy
  kind: authority
  reference: NCBITaxon:3234132
  locator: Fresh successful official species/type-material response
  accessed_at: '2026-10-22T03:30:19.493936Z'
  support: supports
  summary: Aestuariibius violaceus species and named type-material identities positive;
    no quantitative phenotype inferred from taxonomy.
  snapshot_sha256: 17510e6ef00d0a40cdddbd89412287c28ef7969ef05231e79700057db67ee7ef
- evidence_id: taxonomy-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-grounding-agent/taxonomy-retry-access.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T03:30:19.493936Z'
  support: context_only
  summary: Actual successful retry interval and hash.
  snapshot_sha256: 8c1bd1d0695a277d98abfdd7cb363d1b54736bfee4ae9528a00d0b19f11ba837
- evidence_id: taxonomy-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-grounding-agent/taxonomy-identity.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T03:32:07.537301Z'
  support: context_only
  summary: Official identity, original successful response and initial failed-access
    distinction.
  snapshot_sha256: 629a6e500c6c2523a3d66d576ab2cdd7dc32b1e04b7bc4dcbda0a1ffe0b69049
- evidence_id: taxonomy-initial-failure
  kind: validation
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=3234132&retmode=xml
  locator: Initial DNS error bytes, not taxonomy XML
  accessed_at: '2026-10-22T03:30:07.997625Z'
  support: context_only
  summary: Access failure is retained separately from successful retry and native
    validation.
  snapshot_sha256: 35281279d8e2164cee8666d6f8aad891326911e887ab1b2ab778c8ac6d09dc6c
- evidence_id: sources
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-source-agent/source-assessment.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T03:31:45.745415Z'
  support: context_only
  summary: Six works; quantity conflict and bounded nearest-span attribution concern,
    with detailed efficacy unassessed.
  snapshot_sha256: b4e7dab28ae927bae22dfa2ad109832e609f5452b17c3783410713b86fe46da9
- evidence_id: source-identities
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-source-agent/source-ledger.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T03:31:45.736803Z'
  support: context_only
  summary: All six identities and selected scopes; AMTT Crossref positive, original
    metadata notices not refreshed.
  snapshot_sha256: 9502291edf37e26c4c3e89d79610123af5ac27f115c512e5108ab2cf8c1da951
- evidence_id: source-status
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-source-agent/source-status-ledger.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T03:31:45.736803Z'
  support: context_only
  summary: Original-time notice observations, not an exhaustive fresh status search.
  snapshot_sha256: 07751f369bc44ae739bc7e398230a34b098d75220bc0997e884205fb014eb57e
- evidence_id: placements
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-source-agent/source-placement-ledger.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T03:31:45.736803Z'
  support: context_only
  summary: All eleven external placements; twelve grounding fields are separately
    covered by node-edge audits.
  snapshot_sha256: 364e5df8ce879bcd9365ed70ab355ab42708a242c93822c42e137bb8d1a827ff
- evidence_id: snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-source-agent/snippet-ledger.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T03:31:45.736803Z'
  support: context_only
  summary: All three supplied snippets literal after ordinary PDF typography handling
    in one span.
  snapshot_sha256: fc46b035734242623c2541fe120ba6336f8c4657f8745323e3925d3e8559774e
- evidence_id: notes
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-source-agent/source-note-ledger.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T03:31:45.736803Z'
  support: context_only
  summary: Ten notes including the singular canonical note; exact-bin attribution
    distinct from literal text.
  snapshot_sha256: 36b7af70bcfa7bb4b5c40d6452eb4296eafaeeb70e61d11c06dfe86edcf645f6
- evidence_id: source-nodes-edges
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-source-agent/node-edge-source-ledger.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T03:31:45.736803Z'
  support: context_only
  summary: All thirteen nodes and eight edges with exact supported, partial and unassessed
    dispositions.
  snapshot_sha256: f76b92d402da04511c3534f3e038fdfaebbacf1ebc0555e4ea898043d19fa3f3
- evidence_id: canonical
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-source-agent/canonical-assessment.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T03:31:45.736803Z'
  support: context_only
  summary: Named source interval and derived width positive, with incompatible current
    quantity interpretations grouped once.
  snapshot_sha256: 07de19eaaeb1dc3ed120377740e53d65fe14e3a2a964c463a6baaac091277a89
- evidence_id: source-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-source-agent/primary-reading-scope.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T03:31:45.742775Z'
  support: context_only
  summary: Selected identity, physical/classification text and existing literal spans;
    no whole-paper or detailed efficacy review.
  snapshot_sha256: c95f3feb7f4b5da233fe807c45007c507922ff19836879c19501130cb20492b7
- evidence_id: source-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-source-agent/source-access-limits.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T03:31:45.736803Z'
  support: context_only
  summary: Retained actual primary surfaces, historical access limits and one new
    canonical metadata request.
  snapshot_sha256: e977af323948b0be1e2780dc42b1b2faa93af1880e1aa66c42bf7f82a3cb6411
- evidence_id: source-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-source-agent/source-reuse-receipt.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T03:28:39.773314Z'
  support: context_only
  summary: Fourteen exact copies with flat original-access clocks and retained prior-receipt
    hashes.
  snapshot_sha256: 28a5f09354394e95015157be7b017dd23197395c0584c3e491f96f8ba813f98f
- evidence_id: source-native
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-source-agent/native-context.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T03:31:45.745160Z'
  support: context_only
  summary: Native one VERIFIED/two NOT_IN_ABSTRACT and separate manual three literal
    results.
  snapshot_sha256: 222ec876b48a95487865864c7f4378927e5e2db29ebd40a18f1e2c6800446143
- evidence_id: source-manifest
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-source-agent/evidence-manifest.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T03:31:45.754310Z'
  support: context_only
  summary: All thirty frozen source artifacts verified.
  snapshot_sha256: 2422029e5363edb1699c71cd842395aa3e827f0a194b7465a86036bd7201c8f3
- evidence_id: root-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-source-root/selected-primary-reading.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T03:31:14.779248Z'
  support: context_only
  summary: Root selected source/authority/owner readings; primary measurement and
    bounded cold-bin attribution distinguished.
  snapshot_sha256: 59e95bd824868402598822a9518f412aef716ed3347aaeb8c4e731d43e283b7b
- evidence_id: root-verification
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-source-root/root-current-verification.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T03:34:31.516832Z'
  support: context_only
  summary: Root 103 inputs, 57 frozen artifacts, 24 qualified prior-history bindings
    and all 101 current review arrays verified.
  snapshot_sha256: 34e845dac73f058c7f28906ef752cdb06f808c950e1e1cdefed3bb0c620ca6b0
- evidence_id: adjudication
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-014.q8m4v2cs/temperature-range-low-root-adjudication.json
  locator: Final root adjudication
  accessed_at: '2026-10-22T03:34:31.518466Z'
  support: supports
  summary: Exact two majors and two minors, four findings/actions and exact owner/field
    scopes control this combined review.
  snapshot_sha256: e02d16a5ddf64867aff2e3d3de4128e27904f626dc2e08e2b961f8338cbc401f
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: active bin and direct parent'
  outcome: supported
  target_ids:
  - METPO:1000449
  summary: Active METPO:1000449 and direct parent METPO:1000306 are positive. Copied
    upstream qualitative synonyms are faithful; exact biological equivalence remains
    unresolved, not a separate forced synonym defect. Generic raw numeric restrictions
    do not decide the operational quantity.
  evidence_ids:
  - identity
  - authority-primary
  - source-identities
  - record
- assessment_id: definition
  area: quantity
  topic: 'Native checklist: ambient interval versus range width'
  outcome: concern
  target_ids:
  - METPO:1000449
  summary: Definition and graph use 10–22 °C as an ambient growth interval, while
    the canonical note interprets the same numerical bin as a width. The source interval
    22–36 °C and arithmetic 36 minus 22 equals 14 are correct. One grouped major reconciles
    quantity meaning without rejecting the supported measurement or inferring endpoint/width
    semantics solely from generic existential has-value.
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
  - METPO:1000449
  summary: The assigned primary abstract supports Aestuariibius violaceus strain 2305UL40-4T,
    its reported 22–36 °C growth interval and derived width 14. Official species/type-material
    identity is positive. The source optimum is separate. Membership interpretation
    participates in the quantity finding; no false measurement, wrong organism or
    cultivation optimization is asserted.
  evidence_ids:
  - canonical
  - canonical-metadata
  - taxonomy
  - taxonomy-reading
  - adjudication
- assessment_id: source-support
  area: evidence
  topic: 'Native checklist: six works and eleven placements'
  outcome: concern
  target_ids:
  - METPO:1000449
  summary: All six identities resolve. Two D’Amico notes overstate nearest broad cold/near-freezing
    spans as exact 10–22 support, a bounded minor distinct from the quantity major.
    Selected Ramón physical context and Yang Bacillus simplex H-b UFA observation
    are qualified positives. Exact-bin mechanism sufficiency and detailed defense,
    survival, fitness, regulation, enhancement, cryoprotection and intervention efficacy
    remain unassessed; inaccessible AMTT body is not refuted.
  evidence_ids:
  - sources
  - source-identities
  - source-status
  - placements
  - notes
  - source-reading
  - source-access
  - cold-body
  - yang-metadata
  - amtt-prior-access
  - adjudication
- assessment_id: quotations
  area: evidence
  topic: 'Native checklist: three supplied literal snippets'
  outcome: supported
  target_ids:
  - METPO:1000449
  summary: All three current schema snippets are supported by retained author-repository
    PDF text; one needs ordinary pro-/teins line-break dehyphenation. Native one VERIFIED
    and two NOT_IN_ABSTRACT remain separate from manual primary matching. There is
    no copied-span finding, and literal phrases do not establish exact numerical-bin
    support in adjacent notes.
  evidence_ids:
  - snippets
  - source-native
  - damico-pdf
  - damico-derived
  - damico-extraction
  - notes
- assessment_id: nodes
  area: representation
  topic: 'Native checklist: all thirteen current referents'
  outcome: concern
  target_ids:
  - METPO:1000449
  summary: The child and ambient-condition descriptions participate in the grouped
    quantity conflict. PATO relatively-low condition, membrane-fluidity/proportion
    QUALITY and molecular-activity facets are otherwise positive. CHEBI osmolyte role
    versus material bearer is a maintained closeMatch qualification, not forced wrong
    identity. Two protein aggregates have explicit label-only rationales; detailed
    function and efficacy are unassessed.
  evidence_ids:
  - nodes-edges
  - source-nodes-edges
  - schema
  - local-authority
  - ontology-primary
  - authority-primary
  - chebi-ancestry
  - node-mapping
  - policy
  - adjudication
  details: "{\n  \"grounding\": [\n    {\n      \"index\": 0,\n      \"field\": \"\
    causal_graphs[0].nodes[0]\",\n      \"node\": {\n        \"node_id\": \"temperature_range_low_trait\"\
    ,\n        \"label\": \"temperature range low\",\n        \"node_type\": \"TRAIT\"\
    ,\n        \"grounding\": \"METPO:1000449\",\n        \"description\": \"Temperature\
    \ growth-supporting range approximately 10–22 °C.\"\n      },\n      \"outcome\"\
    : \"concern\",\n      \"judgment\": \"Active exact trait identity and direct parent\
    \ are positive; explicit ambient 10–22 °C wording conflicts with canonical range-width\
    \ interpretation (one grouped quantity finding).\"\n    },\n    {\n      \"index\"\
    : 1,\n      \"field\": \"causal_graphs[0].nodes[1]\",\n      \"node\": {\n   \
    \     \"node_id\": \"temperature_range\",\n        \"label\": \"temperature range\"\
    ,\n        \"node_type\": \"TRAIT\",\n        \"grounding\": \"METPO:1000306\"\
    ,\n        \"description\": \"Span of ambient temperatures supporting growth.\"\
    \n      },\n      \"outcome\": \"positive\",\n      \"judgment\": \"Active parent\
    \ temperature range identity; retained raw class has both numerical-temperature\
    \ and numerical-growth-range parents.\"\n    },\n    {\n      \"index\": 2,\n\
    \      \"field\": \"causal_graphs[0].nodes[2]\",\n      \"node\": {\n        \"\
    node_id\": \"psychrotolerant_adaptation\",\n        \"label\": \"psychrotolerant\
    \ adaptation\",\n        \"node_type\": \"BIOLOGICAL_PROCESS\",\n        \"description\"\
    : \"Mild cold-adaptation of membrane and enzyme function sustaining growth at\
    \ cool temperatures.\"\n      },\n      \"outcome\": \"qualified\",\n      \"\
    judgment\": \"Explicit adaptation process is process-compatible; exact numerical\
    \ calibration and biological efficacy unassessed.\"\n    },\n    {\n      \"index\"\
    : 3,\n      \"field\": \"causal_graphs[0].nodes[3]\",\n      \"node\": {\n   \
    \     \"node_id\": \"low_temperature\",\n        \"label\": \"low temperature\"\
    ,\n        \"node_type\": \"ENVIRONMENTAL_FACTOR\",\n        \"description\":\
    \ \"Cool ambient temperature in the approximately 10-22 C range.\",\n        \"\
    grounding\": \"PATO:0001306\"\n      },\n      \"outcome\": \"qualified\",\n \
    \     \"judgment\": \"PATO relatively-low-temperature condition fits environmental\
    \ exposure shorthand; not a decrease event. Absolute 10–22 wording participates\
    \ in the quantity-scope conflict, not a separate PATO defect.\"\n    },\n    {\n\
    \      \"index\": 4,\n      \"field\": \"causal_graphs[0].nodes[4]\",\n      \"\
    node\": {\n        \"node_id\": \"membrane_fluidity\",\n        \"label\": \"\
    membrane fluidity\",\n        \"node_type\": \"QUALITY\",\n        \"description\"\
    : \"Physical fluidity state of the cytoplasmic membrane lipid bilayer.\",\n  \
    \      \"grounding\": \"METPO:1007505\"\n      },\n      \"outcome\": \"positive\"\
    ,\n      \"judgment\": \"Physical membrane-fluidity quality matches v3 METPO1007505;\
    \ not a process.\"\n    },\n    {\n      \"index\": 5,\n      \"field\": \"causal_graphs[0].nodes[5]\"\
    ,\n      \"node\": {\n        \"node_id\": \"fatty_acid_desaturase_activity\"\
    ,\n        \"label\": \"fatty acid desaturase activity\",\n        \"node_type\"\
    : \"MOLECULAR_FUNCTION\",\n        \"description\": \"Enzymatic introduction of\
    \ double bonds into fatty acyl chains (fatty acid desaturases, EC 1.14.19.-).\"\
    \n      },\n      \"outcome\": \"positive\",\n      \"judgment\": \"Enzymatic\
    \ activity is process-compatible MOLECULAR_FUNCTION, not automatically a material\
    \ protein.\"\n    },\n    {\n      \"index\": 6,\n      \"field\": \"causal_graphs[0].nodes[6]\"\
    ,\n      \"node\": {\n        \"node_id\": \"unsaturated_fatty_acid_proportion\"\
    ,\n        \"label\": \"unsaturated fatty acid proportion\",\n        \"node_type\"\
    : \"QUALITY\",\n        \"description\": \"Relative abundance of unsaturated fatty\
    \ acids in membrane lipids.\"\n      },\n      \"outcome\": \"positive\",\n  \
    \    \"judgment\": \"Relative abundance/proportion is explicitly a QUALITY; the\
    \ node already preserves the correct quantity facet.\"\n    },\n    {\n      \"\
    index\": 7,\n      \"field\": \"causal_graphs[0].nodes[7]\",\n      \"node\":\
    \ {\n        \"node_id\": \"cold_shock_proteins\",\n        \"label\": \"cold-shock\
    \ proteins\",\n        \"node_type\": \"GENE_OR_PROTEIN\",\n        \"grounding_status\"\
    : \"REVIEWED_LABEL_ONLY\",\n        \"grounding_notes\": \"Reviewed as a contextual\
    \ protein or protein-complex label within a quantitative measurement graph; no\
    \ exact semantic family term was established for this aggregate use.\",\n    \
    \    \"description\": \"CspA/CspC family cold-shock proteins acting as RNA chaperones.\"\
    \n      },\n      \"outcome\": \"qualified\",\n      \"judgment\": \"Protein-family\
    \ material referent with explicit REVIEWED_LABEL_ONLY disposition; no exact accession\
    \ or instance required.\"\n    },\n    {\n      \"index\": 8,\n      \"field\"\
    : \"causal_graphs[0].nodes[8]\",\n      \"node\": {\n        \"node_id\": \"rna_chaperone_activity\"\
    ,\n        \"label\": \"RNA chaperone activity\",\n        \"node_type\": \"MOLECULAR_FUNCTION\"\
    ,\n        \"description\": \"Resolution of inhibitory RNA secondary structures\
    \ supporting translation at low temperature.\"\n      },\n      \"outcome\": \"\
    positive\",\n      \"judgment\": \"RNA secondary-structure resolution is a molecular\
    \ activity/process referent; no molecular efficacy assessed.\"\n    },\n    {\n\
    \      \"index\": 9,\n      \"field\": \"causal_graphs[0].nodes[9]\",\n      \"\
    node\": {\n        \"node_id\": \"compatible_solutes\",\n        \"label\": \"\
    compatible solutes\",\n        \"node_type\": \"CHEMICAL\",\n        \"description\"\
    : \"Glycine betaine, trehalose and glycerol accumulated as cryoprotectants.\"\
    ,\n        \"grounding\": \"CHEBI:25728\"\n      },\n      \"outcome\": \"qualified\"\
    ,\n      \"judgment\": \"Material solutes are clear in prose; CHEBI25728 has role\
    \ ancestry. Maintained closeMatch is looser than identity, so qualify role-versus-bearer\
    \ grounding rather than declare a wrong identifier.\"\n    },\n    {\n      \"\
    index\": 10,\n      \"field\": \"causal_graphs[0].nodes[10]\",\n      \"node\"\
    : {\n        \"node_id\": \"cryoprotection\",\n        \"label\": \"cryoprotection\"\
    ,\n        \"node_type\": \"BIOLOGICAL_PROCESS\",\n        \"description\": \"\
    Stabilization of proteins and membranes and protection against cold/freezing damage.\"\
    \n      },\n      \"outcome\": \"qualified\",\n      \"judgment\": \"Stabilization/protection\
    \ is a processual referent; detailed cryoprotection efficacy unassessed.\"\n \
    \   },\n    {\n      \"index\": 11,\n      \"field\": \"causal_graphs[0].nodes[11]\"\
    ,\n      \"node\": {\n        \"node_id\": \"molecular_chaperones\",\n       \
    \ \"label\": \"GroEL/DnaK molecular chaperones\",\n        \"node_type\": \"GENE_OR_PROTEIN\"\
    ,\n        \"grounding_status\": \"REVIEWED_LABEL_ONLY\",\n        \"grounding_notes\"\
    : \"Reviewed as a contextual protein or protein-complex label within a quantitative\
    \ measurement graph; no exact semantic family term was established for this aggregate\
    \ use.\",\n        \"description\": \"GroEL and DnaK chaperones assisting protein\
    \ folding under temperature stress.\"\n      },\n      \"outcome\": \"qualified\"\
    ,\n      \"judgment\": \"Chaperone protein-family material referent with explicit\
    \ REVIEWED_LABEL_ONLY disposition; no mandatory exemplar.\"\n    },\n    {\n \
    \     \"index\": 12,\n      \"field\": \"causal_graphs[0].nodes[12]\",\n     \
    \ \"node\": {\n        \"node_id\": \"protein_misfolding\",\n        \"label\"\
    : \"protein misfolding\",\n        \"node_type\": \"BIOLOGICAL_PROCESS\",\n  \
    \      \"description\": \"Cold-denaturation and misfolding of proteins at low\
    \ temperature.\"\n      },\n      \"outcome\": \"positive\",\n      \"judgment\"\
    : \"Misfolding is a biological process; negative direction targets the damaging\
    \ process, so no independent polarity inconsistency.\"\n    }\n  ],\n  \"source\"\
    : [\n    {\n      \"index\": 0,\n      \"field\": \"causal_graphs[0].nodes[0]\"\
    ,\n      \"node_id\": \"temperature_range_low_trait\",\n      \"label\": \"temperature\
    \ range low\",\n      \"description\": \"Temperature growth-supporting range approximately\
    \ 10–22 °C.\",\n      \"outcome\": \"CONCERN\",\n      \"scope\": \"Current10–22\
    \ ambient interval conflicts with explicit canonical width interpretation; no\
    \ source-derived replacement chosen.\"\n    },\n    {\n      \"index\": 1,\n \
    \     \"field\": \"causal_graphs[0].nodes[1]\",\n      \"node_id\": \"temperature_range\"\
    ,\n      \"label\": \"temperature range\",\n      \"description\": \"Span of ambient\
    \ temperatures supporting growth.\",\n      \"outcome\": \"SUPPORTED_WITH_QUALIFICATION\"\
    ,\n      \"scope\": \"Generic span of growth-supporting ambient temperatures is\
    \ coherent; endpoints versus scalar width must be distinguished in the child.\"\
    \n    },\n    {\n      \"index\": 2,\n      \"field\": \"causal_graphs[0].nodes[2]\"\
    ,\n      \"node_id\": \"psychrotolerant_adaptation\",\n      \"label\": \"psychrotolerant\
    \ adaptation\",\n      \"description\": \"Mild cold-adaptation of membrane and\
    \ enzyme function sustaining growth at cool temperatures.\",\n      \"outcome\"\
    : \"UNASSESSED_SCOPE\",\n      \"scope\": \"Broad cold-adaptation identity only;\
    \ membrane/enzyme efficacy for exact bin not assessed.\"\n    },\n    {\n    \
    \  \"index\": 3,\n      \"field\": \"causal_graphs[0].nodes[3]\",\n      \"node_id\"\
    : \"low_temperature\",\n      \"label\": \"low temperature\",\n      \"description\"\
    : \"Cool ambient temperature in the approximately 10-22 C range.\",\n      \"\
    outcome\": \"PARTIAL\",\n      \"scope\": \"Cold ambient physical context is supported\
    \ generically;10–22 calibration and quantity interpretation unresolved.\"\n  \
    \  },\n    {\n      \"index\": 4,\n      \"field\": \"causal_graphs[0].nodes[4]\"\
    ,\n      \"node_id\": \"membrane_fluidity\",\n      \"label\": \"membrane fluidity\"\
    ,\n      \"description\": \"Physical fluidity state of the cytoplasmic membrane\
    \ lipid bilayer.\",\n      \"outcome\": \"SUPPORTED\",\n      \"scope\": \"Generic\
    \ physical membrane-fluidity referent supported by selected D’Amico and Ramón\
    \ text.\"\n    },\n    {\n      \"index\": 5,\n      \"field\": \"causal_graphs[0].nodes[5]\"\
    ,\n      \"node_id\": \"fatty_acid_desaturase_activity\",\n      \"label\": \"\
    fatty acid desaturase activity\",\n      \"description\": \"Enzymatic introduction\
    \ of double bonds into fatty acyl chains (fatty acid desaturases, EC 1.14.19.-).\"\
    ,\n      \"outcome\": \"UNASSESSED_SCOPE\",\n      \"scope\": \"Existing desaturase\
    \ activity name retained; detailed intervention/fitness efficacy not evaluated.\"\
    \n    },\n    {\n      \"index\": 6,\n      \"field\": \"causal_graphs[0].nodes[6]\"\
    ,\n      \"node_id\": \"unsaturated_fatty_acid_proportion\",\n      \"label\"\
    : \"unsaturated fatty acid proportion\",\n      \"description\": \"Relative abundance\
    \ of unsaturated fatty acids in membrane lipids.\",\n      \"outcome\": \"PARTIAL\"\
    ,\n      \"scope\": \"Generic composition property and reported UFA cohort observation\
    \ positive; no universal or exact-bin inference.\"\n    },\n    {\n      \"index\"\
    : 7,\n      \"field\": \"causal_graphs[0].nodes[7]\",\n      \"node_id\": \"cold_shock_proteins\"\
    ,\n      \"label\": \"cold-shock proteins\",\n      \"description\": \"CspA/CspC\
    \ family cold-shock proteins acting as RNA chaperones.\",\n      \"outcome\":\
    \ \"UNASSESSED_SCOPE\",\n      \"scope\": \"Contextual CspA/CspC label retained;\
    \ detailed family function and cold-survival intervention efficacy unassessed.\"\
    \n    },\n    {\n      \"index\": 8,\n      \"field\": \"causal_graphs[0].nodes[8]\"\
    ,\n      \"node_id\": \"rna_chaperone_activity\",\n      \"label\": \"RNA chaperone\
    \ activity\",\n      \"description\": \"Resolution of inhibitory RNA secondary\
    \ structures supporting translation at low temperature.\",\n      \"outcome\"\
    : \"UNASSESSED_SCOPE\",\n      \"scope\": \"Existing RNA-chaperone name retained;\
    \ detailed efficacy unassessed.\"\n    },\n    {\n      \"index\": 9,\n      \"\
    field\": \"causal_graphs[0].nodes[9]\",\n      \"node_id\": \"compatible_solutes\"\
    ,\n      \"label\": \"compatible solutes\",\n      \"description\": \"Glycine\
    \ betaine, trehalose and glycerol accumulated as cryoprotectants.\",\n      \"\
    outcome\": \"UNASSESSED_SCOPE\",\n      \"scope\": \"Existing compatible-solute\
    \ names retained; detailed cryoprotective/defense claims unassessed.\"\n    },\n\
    \    {\n      \"index\": 10,\n      \"field\": \"causal_graphs[0].nodes[10]\"\
    ,\n      \"node_id\": \"cryoprotection\",\n      \"label\": \"cryoprotection\"\
    ,\n      \"description\": \"Stabilization of proteins and membranes and protection\
    \ against cold/freezing damage.\",\n      \"outcome\": \"UNASSESSED_SCOPE\",\n\
    \      \"scope\": \"Existing cryoprotection process label retained; detailed biological\
    \ efficacy unassessed.\"\n    },\n    {\n      \"index\": 11,\n      \"field\"\
    : \"causal_graphs[0].nodes[11]\",\n      \"node_id\": \"molecular_chaperones\"\
    ,\n      \"label\": \"GroEL/DnaK molecular chaperones\",\n      \"description\"\
    : \"GroEL and DnaK chaperones assisting protein folding under temperature stress.\"\
    ,\n      \"outcome\": \"UNASSESSED_SCOPE\",\n      \"scope\": \"Existing GroEL/DnaK\
    \ aggregate retained; detailed proteostasis intervention efficacy unassessed.\"\
    \n    },\n    {\n      \"index\": 12,\n      \"field\": \"causal_graphs[0].nodes[12]\"\
    ,\n      \"node_id\": \"protein_misfolding\",\n      \"label\": \"protein misfolding\"\
    ,\n      \"description\": \"Cold-denaturation and misfolding of proteins at low\
    \ temperature.\",\n      \"outcome\": \"UNASSESSED_SCOPE\",\n      \"scope\":\
    \ \"Existing cold-denaturation/misfolding process label retained; detailed stress\
    \ mechanism unassessed.\"\n    }\n  ]\n}"
- assessment_id: relations
  area: consistency
  topic: 'Native checklist: all eight current relations'
  outcome: concern
  target_ids:
  - METPO:1000449
  summary: RO2212/RO2213 process-to-process constraints conflict with explicit quality
    objects at edges 2/3/4 and material protein subject at edge 7. Correct activity/process
    facets are preserved; no biological intermediate or predicate replacement is invented.
    Edge 5 material-to-activity endpoint fit is positive without executor-efficacy
    validation. Broad v8 confers, exact subclass relation and lexical provides retain
    their separate scopes. Misfolding is a damaging process, so no extra polarity
    finding.
  evidence_ids:
  - nodes-edges
  - source-nodes-edges
  - ontology-primary
  - authority-primary
  - local-authority
  - adjudication
  details: "{\n  \"grounding\": [\n    {\n      \"index\": 0,\n      \"field\": \"\
    causal_graphs[0].edges[0]\",\n      \"edge\": {\n        \"subject\": \"psychrotolerant_adaptation\"\
    ,\n        \"predicate\": \"confers\",\n        \"object\": \"temperature_range_low_trait\"\
    ,\n        \"description\": \"Psychrotolerant adaptation enables growth across\
    \ 10–22 °C.\",\n        \"evidence\": [\n          {\n            \"reference\"\
    : \"DOI:10.1038/sj.embor.7400662\",\n            \"snippet\": \"Cold-shock proteins\
    \ have also been described\",\n            \"notes\": \"Supports cold-shock and\
    \ acclimation responses as the cool-range mechanism.\"\n          }\n        ],\n\
    \        \"predicate_id\": \"METPO:2007700\"\n      },\n      \"outcome\": \"\
    qualified\",\n      \"judgment\": \"Local v8 confers admits broad causal-node-to-trait\
    \ endpoints; adaptation process to trait fits. Numeric object scope needs the\
    \ grouped quantity reconciliation; detailed efficacy unassessed.\"\n    },\n \
    \   {\n      \"index\": 1,\n      \"field\": \"causal_graphs[0].edges[1]\",\n\
    \      \"edge\": {\n        \"subject\": \"temperature_range_low_trait\",\n  \
    \      \"predicate\": \"is a\",\n        \"object\": \"temperature_range\",\n\
    \        \"description\": \"Temperature range low is a quantitative bin of the\
    \ temperature-range phenotype.\",\n        \"evidence\": [\n          {\n    \
    \        \"reference\": \"DOI:10.1038/sj.embor.7400662\",\n            \"snippet\"\
    : \"growing well at temperatures around the freezing point of water\",\n     \
    \       \"notes\": \"Supports the 10–22 °C range as a value within the temperature-range\
    \ distribution.\"\n          }\n        ],\n        \"predicate_id\": \"rdfs:subClassOf\"\
    \n      },\n      \"outcome\": \"positive\",\n      \"judgment\": \"Actual rdfs:subClassOf\
    \ is present, and the exact child/parent relation is asserted in raw METPO; inheritance\
    \ is a valid positive control.\"\n    },\n    {\n      \"index\": 2,\n      \"\
    field\": \"causal_graphs[0].edges[2]\",\n      \"edge\": {\n        \"subject\"\
    : \"low_temperature\",\n        \"predicate\": \"decreases\",\n        \"object\"\
    : \"membrane_fluidity\",\n        \"description\": \"Low temperature reduces membrane\
    \ fluidity, triggering compensatory lipid remodeling.\",\n        \"evidence\"\
    : [\n          {\n            \"reference\": \"DOI:10.1007/s42770-023-01057-4\"\
    ,\n            \"notes\": \"Cold reduces membrane fluidity; changes in membrane\
    \ physical state mediate cold sensing.\"\n          }\n        ],\n        \"\
    predicate_id\": \"RO:0002212\"\n      },\n      \"outcome\": \"major\",\n    \
    \  \"judgment\": \"RO2212 inherits process/process. The current subject is a cool\
    \ condition and object an explicit fluidity QUALITY; quality object independently\
    \ violates range.\"\n    },\n    {\n      \"index\": 3,\n      \"field\": \"causal_graphs[0].edges[3]\"\
    ,\n      \"edge\": {\n        \"subject\": \"fatty_acid_desaturase_activity\"\
    ,\n        \"predicate\": \"increases\",\n        \"object\": \"membrane_fluidity\"\
    ,\n        \"description\": \"Fatty acid desaturase activity raises unsaturation\
    \ to restore membrane fluidity at low temperature.\",\n        \"evidence\": [\n\
    \          {\n            \"reference\": \"DOI:10.37256/amtt.5220244537\",\n \
    \           \"notes\": \"Genes for desaturation are upregulated; desaturases enhance\
    \ membrane fluidity via unsaturated/PUFA synthesis.\"\n          }\n        ],\n\
    \        \"predicate_id\": \"RO:0002213\"\n      },\n      \"outcome\": \"major\"\
    ,\n      \"judgment\": \"RO2213 inherits process/process. Activity subject is\
    \ compatible; fluidity QUALITY object independently violates range.\"\n    },\n\
    \    {\n      \"index\": 4,\n      \"field\": \"causal_graphs[0].edges[4]\",\n\
    \      \"edge\": {\n        \"subject\": \"low_temperature\",\n        \"predicate\"\
    : \"increases\",\n        \"object\": \"unsaturated_fatty_acid_proportion\",\n\
    \        \"description\": \"Growth at low temperature increases the proportion\
    \ of unsaturated fatty acids in membrane lipids.\",\n        \"evidence\": [\n\
    \          {\n            \"reference\": \"DOI:10.1128/aem.01928-22\",\n     \
    \       \"notes\": \"Proportion of unsaturated fatty acids was higher in strains\
    \ cultured at low temperatures while long-chain SFAs decreased.\"\n          }\n\
    \        ],\n        \"predicate_id\": \"RO:0002213\"\n      },\n      \"outcome\"\
    : \"major\",\n      \"judgment\": \"RO2213 inherits process/process. Current cool-condition\
    \ subject and relative-abundance QUALITY object are not processes; quality object\
    \ independently decides failure.\"\n    },\n    {\n      \"index\": 5,\n     \
    \ \"field\": \"causal_graphs[0].edges[5]\",\n      \"edge\": {\n        \"subject\"\
    : \"cold_shock_proteins\",\n        \"predicate\": \"enables\",\n        \"object\"\
    : \"rna_chaperone_activity\",\n        \"description\": \"Cold-shock proteins\
    \ act as RNA chaperones supporting translation at low temperature.\",\n      \
    \  \"evidence\": [\n          {\n            \"reference\": \"DOI:10.3389/fmicb.2023.1197797\"\
    ,\n            \"notes\": \"Cold shock proteins (Csps) can function as RNA chaperones,\
    \ supporting translation in the cold.\"\n          }\n        ],\n        \"predicate_id\"\
    : \"RO:0002327\"\n      },\n      \"outcome\": \"positive\",\n      \"judgment\"\
    : \"RO2327 inherited material/process endpoints fit protein-family subject and\
    \ molecular-activity object. This is domain/range compatibility only, not biological\
    \ executor/efficacy validation.\"\n    },\n    {\n      \"index\": 6,\n      \"\
    field\": \"causal_graphs[0].edges[6]\",\n      \"edge\": {\n        \"subject\"\
    : \"compatible_solutes\",\n        \"predicate\": \"provides\",\n        \"object\"\
    : \"cryoprotection\",\n        \"description\": \"Compatible solutes provide cryoprotection\
    \ by stabilizing membranes and proteins and lowering freezing point.\",\n    \
    \    \"evidence\": [\n          {\n            \"reference\": \"DOI:10.3389/fmicb.2023.1197797\"\
    ,\n            \"notes\": \"Compatible osmolytes prevent cell shrinkage, lower\
    \ freezing point, scavenge radicals, and stabilize membranes/proteins.\"\n   \
    \       }\n        ]\n      },\n      \"outcome\": \"qualified\",\n      \"judgment\"\
    : \"Lexical provides has no predicate_id; do not invent imported RO constraints.\
    \ Material-solute/process relation is not formally rejected; detailed efficacy\
    \ unassessed.\"\n    },\n    {\n      \"index\": 7,\n      \"field\": \"causal_graphs[0].edges[7]\"\
    ,\n      \"edge\": {\n        \"subject\": \"molecular_chaperones\",\n       \
    \ \"predicate\": \"prevents\",\n        \"object\": \"protein_misfolding\",\n\
    \        \"description\": \"GroEL/DnaK chaperones prevent cold-denaturation and\
    \ protein misfolding at low temperature.\",\n        \"evidence\": [\n       \
    \   {\n            \"reference\": \"DOI:10.37256/amtt.5220244537\",\n        \
    \    \"notes\": \"Chaperones are upregulated at low temperatures to prevent cold-denaturation\
    \ and misfolding.\"\n          }\n        ],\n        \"predicate_id\": \"RO:0002212\"\
    \n      },\n      \"outcome\": \"major\",\n      \"judgment\": \"RO2212 requires\
    \ process/process; current molecular-chaperone subject is a material protein family.\
    \ Process object is compatible, negative direction is internally coherent.\"\n\
    \    }\n  ],\n  \"source\": [\n    {\n      \"index\": 0,\n      \"field\": \"\
    causal_graphs[0].edges[0]\",\n      \"subject\": \"psychrotolerant_adaptation\"\
    ,\n      \"predicate\": \"confers\",\n      \"object\": \"temperature_range_low_trait\"\
    ,\n      \"description\": \"Psychrotolerant adaptation enables growth across 10–22\
    \ °C.\",\n      \"source_reference\": \"DOI:10.1038/sj.embor.7400662\",\n    \
    \  \"outcome\": \"UNASSESSED_SCOPE\",\n      \"scope\": \"Supplied cold-shock\
    \ phrase literal after PDF line-break dehyphenation; detailed acclimation efficacy\
    \ unassessed.\"\n    },\n    {\n      \"index\": 1,\n      \"field\": \"causal_graphs[0].edges[1]\"\
    ,\n      \"subject\": \"temperature_range_low_trait\",\n      \"predicate\": \"\
    is a\",\n      \"object\": \"temperature_range\",\n      \"description\": \"Temperature\
    \ range low is a quantitative bin of the temperature-range phenotype.\",\n   \
    \   \"source_reference\": \"DOI:10.1038/sj.embor.7400662\",\n      \"outcome\"\
    : \"PARTIAL\",\n      \"scope\": \"Near-freezing phrase literal; note overstates\
    \ its exact10–22 interval support.\"\n    },\n    {\n      \"index\": 2,\n   \
    \   \"field\": \"causal_graphs[0].edges[2]\",\n      \"subject\": \"low_temperature\"\
    ,\n      \"predicate\": \"decreases\",\n      \"object\": \"membrane_fluidity\"\
    ,\n      \"description\": \"Low temperature reduces membrane fluidity, triggering\
    \ compensatory lipid remodeling.\",\n      \"source_reference\": \"DOI:10.1007/s42770-023-01057-4\"\
    ,\n      \"outcome\": \"PARTIAL\",\n      \"scope\": \"Generic cooling/phase packing\
    \ context positive; sensing/regulatory efficacy unassessed.\"\n    },\n    {\n\
    \      \"index\": 3,\n      \"field\": \"causal_graphs[0].edges[3]\",\n      \"\
    subject\": \"fatty_acid_desaturase_activity\",\n      \"predicate\": \"increases\"\
    ,\n      \"object\": \"membrane_fluidity\",\n      \"description\": \"Fatty acid\
    \ desaturase activity raises unsaturation to restore membrane fluidity at low\
    \ temperature.\",\n      \"source_reference\": \"DOI:10.37256/amtt.5220244537\"\
    ,\n      \"outcome\": \"UNASSESSED_SCOPE\",\n      \"scope\": \"AMTT identity\
    \ positive; detailed desaturase upregulation/efficacy unassessed and body text\
    \ unavailable in retained access.\"\n    },\n    {\n      \"index\": 4,\n    \
    \  \"field\": \"causal_graphs[0].edges[4]\",\n      \"subject\": \"low_temperature\"\
    ,\n      \"predicate\": \"increases\",\n      \"object\": \"unsaturated_fatty_acid_proportion\"\
    ,\n      \"description\": \"Growth at low temperature increases the proportion\
    \ of unsaturated fatty acids in membrane lipids.\",\n      \"source_reference\"\
    : \"DOI:10.1128/aem.01928-22\",\n      \"outcome\": \"PARTIAL\",\n      \"scope\"\
    : \"Studied B.simplex H-b abstract supports higher UFA proportion; long-chain\
    \ SFA clause and generalization remain unverified by inspected text.\"\n    },\n\
    \    {\n      \"index\": 5,\n      \"field\": \"causal_graphs[0].edges[5]\",\n\
    \      \"subject\": \"cold_shock_proteins\",\n      \"predicate\": \"enables\"\
    ,\n      \"object\": \"rna_chaperone_activity\",\n      \"description\": \"Cold-shock\
    \ proteins act as RNA chaperones supporting translation at low temperature.\"\
    ,\n      \"source_reference\": \"DOI:10.3389/fmicb.2023.1197797\",\n      \"outcome\"\
    : \"UNASSESSED_SCOPE\",\n      \"scope\": \"Antarctic review identity positive;\
    \ detailed RNA-chaperone efficacy UNASSESSED_SCOPE.\"\n    },\n    {\n      \"\
    index\": 6,\n      \"field\": \"causal_graphs[0].edges[6]\",\n      \"subject\"\
    : \"compatible_solutes\",\n      \"predicate\": \"provides\",\n      \"object\"\
    : \"cryoprotection\",\n      \"description\": \"Compatible solutes provide cryoprotection\
    \ by stabilizing membranes and proteins and lowering freezing point.\",\n    \
    \  \"source_reference\": \"DOI:10.3389/fmicb.2023.1197797\",\n      \"outcome\"\
    : \"UNASSESSED_SCOPE\",\n      \"scope\": \"Antarctic review identity positive;\
    \ detailed osmolyte/cryoprotection/radical-defense efficacy UNASSESSED_SCOPE.\"\
    \n    },\n    {\n      \"index\": 7,\n      \"field\": \"causal_graphs[0].edges[7]\"\
    ,\n      \"subject\": \"molecular_chaperones\",\n      \"predicate\": \"prevents\"\
    ,\n      \"object\": \"protein_misfolding\",\n      \"description\": \"GroEL/DnaK\
    \ chaperones prevent cold-denaturation and protein misfolding at low temperature.\"\
    ,\n      \"source_reference\": \"DOI:10.37256/amtt.5220244537\",\n      \"outcome\"\
    : \"UNASSESSED_SCOPE\",\n      \"scope\": \"AMTT identity positive; detailed chaperone\
    \ regulation/efficacy UNASSESSED_SCOPE and body text unavailable.\"\n    }\n \
    \ ]\n}"
- assessment_id: owners
  area: ownership
  topic: 'Native checklist: exact canonical ledger and conditional predicate grounder'
  outcome: supported
  target_ids:
  - METPO:1000449
  summary: The exact SOURCES/TRANCHE canonical payload preserves a supported interval
    and width; coordinate its quantity interpretation with current record fields while
    retaining equality/no-op and nonempty-difference rejection guards. Predicate wildcard
    rows 60/61/65 can recreate incompatible roles in empty fields; the consumer skips
    current populated IDs, so ordinary replay is not a repair. Sibling node-type/review/connector
    hits are not promoted to current faulty owners.
  evidence_ids:
  - owners
  - owner-primary
  - canonical-writer
  - predicate-mapping
  - discovery
  - adjudication
- assessment_id: provenance
  area: provenance
  topic: 'Native checklist: bounded human acceptance link'
  outcome: concern
  target_ids:
  - METPO:1000449
  summary: Nine embedded events comprise eight AI-assisted events and a seed. All
    24 current history projections are AI and rely on exact qualified prior whole-body
    readings; zero new whole-history reads are claimed. Ignored- and hidden-inclusive
    search has 206 matching paths, 67 matching review arrays and 101 all-local arrays
    with zero exact target. Uncaptured leads remain matching-line context; private
    or remote acceptance is unknown.
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
  - METPO:1000449
  summary: The original catalog contains 20 organisms and 28 datasets; current selected-name
    comparison has no exact Aestuariibius violaceus or Bacillus simplex key. This
    does not establish global absence or permit B. subtilis/E. coli source-organism
    substitution. No module query was executed because the maintained runner is unavailable
    within bounded discovery. No strain/module/efficacy result is inferred.
  evidence_ids:
  - expression
  - expression-discovery
  - catalog-original
  - catalog-reuse
  - catalog-reading
  - source-reading
  - adjudication
- assessment_id: readiness
  area: completeness
  topic: 'Native checklist: NONMECHANISTIC context and optional instances'
  outcome: supported
  target_ids:
  - METPO:1000449
  summary: Five disconnected components with thirteen nodes and eight edges are permissible
    contextual NONMECHANISTIC structure. Two protein classes are explicitly label-only
    and have zero instances; no connector, token accession or dataset is mandatory.
    This structural disposition does not resolve the quantity, source-attribution
    or formal-role findings.
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
  - METPO:1000449
  summary: Current inspect, focused target validation, strict validation and snippet
    command completed successfully. B14 common diagnostics retain original execution
    intervals, historical attempts, product skips and omitted full suite. These bounded
    software checks do not establish scientific correctness, source efficacy or human
    acceptance.
  evidence_ids:
  - capture
  - fresh-common-completion
  - check-temperature-range-low-target-validate
  - check-temperature-range-low-target-strict
  - check-temperature-range-low-snippets-network
  - source-native
findings:
- finding_id: quantity-scope
  issue_key: temperature-range-low-quantity-scope
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Quantity scope
  description: The definition and graph use 10–22 °C as an absolute ambient growth
    interval, while canonical_examples[0].note explicitly treats 10–22 degrees as
    a range-width bin. The assigned primary abstract supports growth22–36 °C for the
    named strain, and36−22=14 is correct; it is a different quantity from ambient
    interval10–22. Raw METPO supplies an existential generic numeric value in[10,22]
    but does not specify endpoint versus width operationalization. Reconcile the quantity
    throughout this record and its exact maintained canonical ledger without rejecting
    the supported source measurement, choosing an unsupported ontology interpretation,
    or asserting a wrong organism.
  target_ids:
  - METPO:1000449
  field_paths:
  - definition
  - canonical_examples[0].note
  - causal_graphs[0].description
  - causal_graphs[0].nodes[0].description
  - causal_graphs[0].nodes[3].description
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
    path: data/traits/environment/temperature_range_low.yaml
    role: Current record assertions; separate authorized curation required
  - repository: CultureBotAI/TraitMech
    path: scripts/backfill_canonical_examples_444.py
    role: Exact maintained source/TRANCHE payload and equality/rejection guards; coordinate
      quantity interpretation while preserving the supported measurement
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: imported-process-roles
  issue_key: temperature-range-low-imported-process-roles
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Imported process roles
  description: RO:0002212 and RO:0002213 inherit process-to-process roles from RO:0002211.
    Current edges2/3/4 target explicitly stated fluidity or relative-abundance qualities;
    edges2/4 also use a cool ambient condition. Edge7 uses a material chaperone-protein
    subject with a process object. These existing referents conflict with the imported
    roles. Edge5 protein-to-molecular-activity endpoint fit is positive; direction
    and biological efficacy remain separate. Wildcard mapping rows60/61/65 can recreate
    these assignments in empty fields, while the grounder skips current populated
    IDs, so ordinary replay will not repair them.
  target_ids:
  - METPO:1000449
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
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_range_low.yaml
    role: Current record assertions; separate authorized curation required
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Wildcard closeMatch rows can recreate imported roles in future empty fields;
      coordinate formal referent support
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Conditional grounding consumer skips populated IDs; ordinary replay is not
      current-field repair
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: cold-bin-attribution
  issue_key: temperature-range-low-cold-bin-attribution
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Cold bin attribution
  description: These notes attribute exact 10–22 °C range support to broad cold/near-freezing
    passages. The supplied D’Amico phrases are literal, but the inspected introduction
    explicitly describes a continuum with wide or narrow ranges and uses psychrophiles
    broadly for near-freezing growth. This supports a bounded nearest-span attribution
    correction, not a claim that every part of the paper lacks calibration or that
    its biology is false.
  target_ids:
  - METPO:1000449
  field_paths:
  - evidence[0].notes
  - causal_graphs[0].edges[1].evidence[0].notes
  evidence_ids:
  - sources
  - placements
  - notes
  - damico-pdf
  - damico-derived
  - source-reading
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_range_low.yaml
    role: Current record assertions; separate authorized curation required
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: human-acceptance-link
  issue_key: temperature-range-low-human-acceptance-link
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Human acceptance link
  description: The record is REVIEWED, but its nine embedded events comprise eight
    AI-assisted events plus the METPO seed. All24 captured current actor projections
    are AI; their whole bodies are exact qualified prior readings, not new whole reads.
    The ignored- and hidden-inclusive bounded local search finds206matching paths,67matching
    review arrays and101all-local arrays with zero exact target. This local evidence
    does not provide an attributable human acceptance link. Private or remote acceptance
    remains unknown.
  target_ids:
  - METPO:1000449
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
    path: data/traits/environment/temperature_range_low.yaml
    role: Current record assertions; separate authorized curation required
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
actions:
- action_id: curate-quantity-scope
  description: In separately authorized curation, establish and document the measured-quantity
    contract, then reconcile definition, graph and canonical membership interpretation
    with the exact backfill ledger. Preserve the verified strain interval and distinguish
    derived width from absolute temperatures.
  finding_ids:
  - quantity-scope
  target_ids:
  - METPO:1000449
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_range_low.yaml
    role: Current record assertions; separate authorized curation required
  - repository: CultureBotAI/TraitMech
    path: scripts/backfill_canonical_examples_444.py
    role: Exact maintained source/TRANCHE payload and equality/rejection guards; coordinate
      quantity interpretation while preserving the supported measurement
  acceptance_checks:
  - Document source-backed intended quantity and unit semantics without deriving an
    endpoint/width contract solely from generic has-value.
  - Keep the22–36source interval and36−22=14arithmetic accurate and explicitly strain-scoped;
    make all affected fields use one consistent contract.
  - Coordinate SOURCES/TRANCHE and the existing equality/rejection guards; current
    correct source payload is not itself a false-measurement finding.
  - Use guarded curation/history and run focused strict validation plus applicable
    QC/products and regenerate affected products.
- action_id: curate-imported-process-roles
  description: Resolve the four relation identifiers against the actual existing referents;
    coordinate narrowly scoped mapping/consumer behavior to avoid recreating incompatible
    imported roles.
  finding_ids:
  - imported-process-roles
  target_ids:
  - METPO:1000449
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_range_low.yaml
    role: Current record assertions; separate authorized curation required
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Wildcard closeMatch rows can recreate imported roles in future empty fields;
      coordinate formal referent support
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Conditional grounding consumer skips populated IDs; ordinary replay is not
      current-field repair
  acceptance_checks:
  - For each edge2/3/4/7, document the retained subject/object referents and formal
    domain/range support of the chosen representation.
  - Preserve correct quality and molecular-activity facets; do not relabel them merely
    to pass a relation check or invent biological intermediates.
  - Demonstrate future empty-field grounding respects the revised semantic decision
    and explicitly repair current populated IDs through guarded curation; ordinary
    grounder replay skips them.
  - Retain positive edge5 endpoint fit and lexical-edge6 scope; run focused strict
    validation, applicable graph/QC/products checks and meaningful grounding regression
    checks.
- action_id: curate-cold-bin-attribution
  description: Revise the two evidence notes to distinguish the inspected generic
    cold/near-freezing support from any exact numerical-bin authority.
  finding_ids:
  - cold-bin-attribution
  target_ids:
  - METPO:1000449
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_range_low.yaml
    role: Current record assertions; separate authorized curation required
  acceptance_checks:
  - Each note accurately describes its nearest inspected source span; exact10–22 calibration
    requires an explicitly identified supporting source or remains qualified.
  - Retain all three literal snippets, including ordinary PDF line-break normalization,
    and preserve native1VERIFIED/2NOT_IN_ABSTRACT separately from manual full-text
    findings.
  - Do not infer whole-paper absence or biological falsity from the bounded passages;
    validate the separately curated record.
- action_id: curate-human-acceptance-link
  description: Link attributable human acceptance for the REVIEWED status or accurately
    qualify the review state in separately authorized curation.
  finding_ids:
  - human-acceptance-link
  target_ids:
  - METPO:1000449
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_range_low.yaml
    role: Current record assertions; separate authorized curation required
  acceptance_checks:
  - Retain actor identity, scope and retrievable acceptance reference rather than
    treating AI review or seed import as human signoff.
  - Preserve the bounded local-search limitation and private/remote uncertainty.
  - Use maintained guarded history/validation procedures if status or evidence changes.
limitations:
- Full just test was NOT_RUN under the selected review-only diagnostic scope; only
  the five focused Stage2 tests are recorded. Products retains 123 no-adapter skips.
  Common checks establish bounded software/data integrity, not scientific support.
- Detailed microbial heat/cold defense, survival/fitness, cultivation optimization,
  regulation, molecular enhancement and intervention efficacy remain UNASSESSED_SCOPE.
  No operational repair is proposed.
- Current quantity prose mixes absolute temperature interval and interval width; primary
  canonical measurement/arithmetic are positive but do not settle which quantity the
  record should encode.
- D’Amico selected introduction supports broad near-freezing classification with variable
  ranges, not the exact10–22 attribution made by current notes. No whole-paper absence
  assertion.
- All three snippets supported by retained author-repository PDF text; one requires
  ordinary linebreak dehyphenation. Native1VERIFIED2NOT_IN_ABSTRACT remains separate.
- Only selected primary text adopted. Full metadata abstract display included incidental
  canonical chemistry/taxonomic details; not adopted beyond identity/temperature/type
  strain.
- Ramón paragraph17 sentence5 was incidentally displayed while filtering; only sentences1–2
  physical phase/packing context adopted.
- Yang study is Bacillus simplex H-b; its selected abstract UFA observation is not
  general proof of all strains, long-chain-SFA clause, exact bin, or detailed adaptation
  efficacy. Historical body request failed.
- Frontiers1197797 retained XML is available but inspected current identity/title
  only; detailed RNA/cryoprotection passages deliberately unassessed.
- 'AMTT indexed zero-hit does not mean DOI missing: Crossref identity positive. Actual
  historical publisher/PDF access failure leaves body claims unresolved; no fresh
  body acquisition.'
- Metadata/publication notice observations remain tied to original request times;
  current copy/read times are not acquisitions.
- No exact-source species/catalog inference from uninspected body passages; source
  identity alone does not establish strain/module/phenotype coverage.
- Detailed biological efficacy, stress-defense, cold survival, cryoprotection, regulatory
  and cultivation optimization are UNASSESSED_SCOPE.
- CHEBI role/bearer closeMatch is qualified, not forced wrong-identifier finding.
- Raw numeric existential restriction does not specify interval versus width operationalization.
- All 24 history bodies are exact prior whole-reading qualifications, with current
  actor/event projections; no fresh whole-history claim.
- Uncaptured discovery leads remain matching-line context only; private/remote human
  review unknown.
- No common-corpus or database rehash repeated. Source findings are independently
  owned by source auditor.
- Active target/parent and copied upstream synonyms are positive; exact biological
  equivalence of broad aliases remains unresolved, not a separate forced synonym finding.
- Five disconnected components are permitted contextual NONMECHANISTIC structure;
  no forced connector, token protein instance or dataset.
- PATO relatively-low condition and v3fluidity quality are positive; CHEBI osmolyte
  role/bearer closeMatch is qualified rather than declared exact identity.
- Broad local v8confers does not inherit ROexecutor restrictions from its cross-reference.
  Edge5 formal endpoint fit does not verify physiological executor efficacy.
- Current canonical taxonomy is official species/type-material identity only. Retained20-organism28-dataset
  catalog has no exact selected canonical/B.simplex name; no B.subtilis/E.coli source-organism
  substitution or global absence inference.
- Publication remains separate from this local scientific review; no record, ontology,
  history, mapping, generated product or provider run is changed.
notes:
- Historical products failures/retry and original cache provenance remain in /private/tmp/traitmech-record-sweep-014.q8m4v2cs/new-base-diagnostic-independent-review-agent/fresh-products-completion.json.
  The earlier outstanding-products status is superseded by the actual fresh run; no
  blanket cross-batch reuse qualification is asserted.
- Final fields, categories, severities, owners and actions come only from actual root
  FINAL. The shared source/ground quantity conflict is counted once, alongside one
  formal-role major and two bounded minors.
- This serializer adopts frozen audits and root adjudication. Original source/catalog
  acquisitions, PDF extraction, current metadata request, exact copies/readings and
  failed/successful taxonomy requests retain separate clocks. Static serializer preparation
  does not claim another whole-paper review or fresh whole-history readings. Root
  execution and native output validation are separate; no scientific record, state,
  Git or publication change is performed.
tags:
- record-review
- temperature-range-low
- environment
- needs-curation
```
