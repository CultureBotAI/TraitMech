# Whole-record review of temperature range mid2

- Review: 20261022T042122Z-temperature-range-mid2
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-22T04:09:31.682492Z
- Finished UTC: 2026-10-22T04:21:22Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Whole-record review identifies three major issues: absolute-interval versus interval-width semantics, a proportion typed as chemical material, and incompatible imported process roles at two edges. Three bounded minors concern an organism-category facet, exact-bin attribution and a retrievable human-acceptance link. Active identity, canonical reported12–40 °C interval and derived width28, three literal snippets and selected formal endpoint facets are positive; detailed microbial efficacy remains unassessed.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: Second record in the actual B15 queue; current 270-line target and 107 captured inputs. Local review is independent of remote publication.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 508ee3089c93a36413969cd1ede7f9528a1940a4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| METPO:1000451 | data/traits/environment/temperature_range_mid2.yaml | maintained | temperature range mid2 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Reused B14 corpus QC | passed | True | METPO:1000451 | Actual just qc passed: strict validation of 1130 records with 0 errors; graph audit: 74 baselined, 0 new and 0 blocking findings; 135 connected graphs and 1588 wired nodes; protein coverage: 729 graphs (134 pass, 594 NONMECHANISTIC, 0 gaps, 1 protected); snippet audit: 2419 baselined, 0 new and 0 blocking findings; 19 PathwayMech links. These are corpus diagnostics, not scientific validation of this target. |
| Reused B14 history integrity | passed | True | METPO:1000451 | 1278 HistoryRecord YAMLs validated, 0 invalid; current history snapshot contains 1279 files. Integrity does not establish scientific correctness or human acceptance. |
| Reused B14 mapping identifier/label validation | passed | True | METPO:1000451 | 361 canonical matches, 2 exact-synonym matches, 1 exception and 123 SKIPPED_NO_ADAPTER pairs. Configured scope is the two grounding mappings, not every target identifier or scientific claim. |
| Reused B14 focused Stage2 writer tests | passed | False | METPO:1000451 | Five tests passed in the explicitly selected Stage2 test file. This is not a full just test run or biological validation. |
| Focused native validation | passed | True | METPO:1000451 | Native record validation passed; scientific interpretation is assessed separately. |
| Focused strict validation | passed | True | METPO:1000451 | The actual validate-strict command passed. |
| Focused network snippet check | passed | True | METPO:1000451 | Native command completed successfully with all three snippets VERIFIED. Separate manual primary matching also supports three literal spans; this does not establish adjacent numerical-bin claims. |
| One-target native review capture | passed | True | METPO:1000451 | One current target, 107 captured inputs, exact current base and successful native inspect. |
| Protein-instance metadata applicability | not_applicable | False | METPO:1000451 | One contextual protein aggregate is REVIEWED_LABEL_ONLY with an explicit rationale and zero instances; no token accession required. |
| Structured source-organism expression query availability | unavailable | False | METPO:1000451 | Bounded maintained-runner discovery found no available adapter. Retained catalog and selected source identities provide no strain/module or efficacy result. |

## Scientific And Domain Assessments

### Native checklist: active bin and direct parent

identity: supported. Targets: METPO:1000451.

Active METPO:1000451 and direct parent METPO:1000306 are positive. Historical Mesophilie retention is documented; broad exact biological equivalence to the unresolved numerical quantity remains unknown. Homeoviscous adaptation METPO:1016200 is locally proposed in v85, not asserted active in the captured upstream raw OWL.

### Native checklist: ambient interval versus range width

quantity: concern. Targets: METPO:1000451.

Definition, graph and edge 9 bracketing use 27–30 °C as ambient values while the canonical note uses an interval-width bin. Reported growth at 12–40 °C and arithmetic 40 minus 12 equals 28 are correct. One grouped major reconciles all seven fields while preserving the measurement and broad mesophile classification. Generic has-value restrictions do not choose endpoints or width.

### Native checklist: strain-scoped source measurement and identity

evidence: supported. Targets: METPO:1000451.

The retained original primary abstract supports Pseudomonas mangiferae DMKU BBB3-04T, type aliases TBRC 7080/JCM 32061, reported growth at 12–40 °C and derived width 28. Fresh official taxonomy supports identity only. Source optimum remains separate. Membership interpretation participates in quantity scope; no false measurement, wrong organism or cultivation optimization is asserted.

### Native checklist: six works and thirteen placements

evidence: concern. Targets: METPO:1000451.

All six identities resolve. Mendoza generic membrane physics and Tolner high-temperature thermophile spans do not establish adjacent exact 27–30-bin notes. Selected Ramón physical and broad mesophile classification clauses are qualified positives. Moon and the new RNA review provide identity only; nearest-source edge 3 support and detailed RNA, stress, chaperone, regulation, survival/fitness and intervention efficacy remain unassessed. No whole-paper absence or title-based citation mismatch is inferred.

### Native checklist: three supplied literal snippets

evidence: supported. Targets: METPO:1000451.

All three current schema snippets are literal in retained indexed abstracts, consistent with the actual native three-VERIFIED result. Literal text does not establish adjacent numerical-bin attribution. No copied-span finding is added.

### Native checklist: all thirteen current referents

representation: concern. Targets: METPO:1000451.

Node 5 explicitly denotes a measurable fatty-acid proportion but is typed CHEMICAL, an independent major. Node 12 denotes an organism category rather than the schema-defined cellular STATE, a bounded minor. Locally proposed homeoviscous process, fluidity quality, temperature-change events and material RNA are otherwise positive or qualified. The baseline adaptation/repertoire is mixed without an extra forced finding; the reviewed label-only protein aggregate needs no token accession.

{
  "grounding": [
    {
      "index": 0,
      "field": "causal_graphs[0].nodes[0]",
      "node": {
        "node_id": "temperature_range_mid2_trait",
        "label": "temperature range mid2",
        "node_type": "TRAIT",
        "grounding": "METPO:1000451",
        "description": "Temperature growth-supporting range approximately 27–30 °C."
      },
      "outcome": "concern",
      "judgment": "Active exact METPO identity, but ambient27–30 wording participates in interval-versus-width conflict."
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
      "judgment": "Exact active temperature-range parent; direct raw hierarchy positive."
    },
    {
      "index": 2,
      "field": "causal_graphs[0].nodes[2]",
      "node": {
        "node_id": "baseline_mesophile_adaptation",
        "label": "baseline mesophile adaptation",
        "node_type": "BIOLOGICAL_PROCESS",
        "description": "Standard mesophile membrane and enzyme repertoire supporting growth at moderate ambient temperatures."
      },
      "outcome": "qualified",
      "judgment": "Adaptation label suggests a process while description names membrane/enzyme repertoire. Mixed process/material context is legible but not resolved into a mandatory extra type finding; detailed efficacy unassessed."
    },
    {
      "index": 3,
      "field": "causal_graphs[0].nodes[3]",
      "node": {
        "node_id": "homeoviscous_adaptation",
        "label": "homeoviscous adaptation",
        "node_type": "BIOLOGICAL_PROCESS",
        "description": "Regulation of membrane lipid composition to maintain constant viscosity/fluidity across temperatures.",
        "grounding": "METPO:1016200"
      },
      "outcome": "positive",
      "judgment": "Explicit lipid-composition remodeling process agrees with locally proposed METPO1016200 in v85; raw upstream zero-match is not treated as invalid local grounding."
    },
    {
      "index": 4,
      "field": "causal_graphs[0].nodes[4]",
      "node": {
        "node_id": "membrane_fluidity",
        "label": "membrane fluidity",
        "node_type": "QUALITY",
        "description": "Fluid state of the lipid bilayer required for membrane function.",
        "grounding": "METPO:1007505"
      },
      "outcome": "positive",
      "judgment": "Explicit membrane fluidity property agrees with local v3 METPO1007505 quality; not a process."
    },
    {
      "index": 5,
      "field": "causal_graphs[0].nodes[5]",
      "node": {
        "node_id": "unsaturated_fatty_acid_fraction",
        "label": "unsaturated fatty acid fraction",
        "node_type": "CHEMICAL",
        "description": "Proportion of unsaturated fatty acids in membrane phospholipids."
      },
      "outcome": "major",
      "judgment": "Explicit fraction/proportion is a measurable compositional attribute, not the chemical entities being counted. CHEMICAL materially changes the declared referent; independent from imported relation repair."
    },
    {
      "index": 6,
      "field": "causal_graphs[0].nodes[6]",
      "node": {
        "node_id": "hopanoids_sterol_like",
        "label": "hopanoids / sterol-like molecules",
        "node_type": "CHEMICAL",
        "description": "Membrane-embedded sterol-like regulators of bilayer fluidity."
      },
      "outcome": "positive",
      "judgment": "Named membrane-embedded molecules have a material chemical referent. Their imported process relation at edge4 is assessed separately; efficacy unassessed."
    },
    {
      "index": 7,
      "field": "causal_graphs[0].nodes[7]",
      "node": {
        "node_id": "elevated_temperature",
        "label": "elevated temperature",
        "node_type": "ENVIRONMENTAL_FACTOR",
        "description": "Increase in ambient growth temperature."
      },
      "outcome": "positive",
      "judgment": "Description denotes an increase/change in ambient temperature. ENVIRONMENTAL_FACTOR permits exposure/condition shorthand and is not automatically invalid for this event."
    },
    {
      "index": 8,
      "field": "causal_graphs[0].nodes[8]",
      "node": {
        "node_id": "rna_thermometer",
        "label": "RNA thermometer 5′-UTR structure",
        "node_type": "RNA",
        "description": "Temperature-responsive mRNA 5′-UTR secondary structure controlling translation initiation."
      },
      "outcome": "positive",
      "judgment": "mRNA secondary structure is an RNA material referent; detailed regulatory activity and efficacy unassessed."
    },
    {
      "index": 9,
      "field": "causal_graphs[0].nodes[9]",
      "node": {
        "node_id": "temperature_shift",
        "label": "temperature shift / heat shock",
        "node_type": "ENVIRONMENTAL_FACTOR",
        "description": "Abrupt change in ambient temperature, including heat shock."
      },
      "outcome": "positive",
      "judgment": "Explicit abrupt temperature change/heat shock is an event, not automatically invalid by ENV enum."
    },
    {
      "index": 10,
      "field": "causal_graphs[0].nodes[10]",
      "node": {
        "node_id": "heat_shock_proteins",
        "label": "heat-shock proteins / chaperones",
        "node_type": "GENE_OR_PROTEIN",
        "grounding_status": "REVIEWED_LABEL_ONLY",
        "grounding_notes": "Reviewed as a contextual protein or protein-complex label within a quantitative measurement graph; no exact semantic family term was established for this aggregate use.",
        "description": "Molecular chaperones induced by thermal stress that maintain proteostasis."
      },
      "outcome": "qualified",
      "judgment": "Contextual aggregate chaperone protein label has explicit REVIEWED_LABEL_ONLY rationale, no accession/instance forced in a NONMECHANISTIC graph; detailed proteostasis efficacy unassessed."
    },
    {
      "index": 11,
      "field": "causal_graphs[0].nodes[11]",
      "node": {
        "node_id": "protein_denaturation",
        "label": "protein denaturation / aggregation",
        "node_type": "BIOLOGICAL_PROCESS",
        "description": "Loss of protein structure and aggregation under thermal stress."
      },
      "outcome": "positive",
      "judgment": "Explicit denaturation/aggregation is a biological process as a referent only; detailed stress efficacy unassessed."
    },
    {
      "index": 12,
      "field": "causal_graphs[0].nodes[12]",
      "node": {
        "node_id": "mesophilic_organisms",
        "label": "mesophilic organisms",
        "node_type": "STATE",
        "description": "Organisms growing at moderate temperatures (~20-45 °C)."
      },
      "outcome": "minor",
      "judgment": "Description denotes an organism category, not the schema-defined bioenergetic or molecular cellular STATE. Intent remains clear; bounded facet precision finding without prescribing a replacement enum."
    }
  ],
  "source": [
    {
      "index": 0,
      "field": "causal_graphs[0].nodes[0]",
      "node_id": "temperature_range_mid2_trait",
      "node_type": "TRAIT",
      "description": "Temperature growth-supporting range approximately 27–30 °C.",
      "outcome": "concern",
      "assessment": "Ambient27–30 description participates in shared quantity conflict; exact ontology identity assessed separately."
    },
    {
      "index": 1,
      "field": "causal_graphs[0].nodes[1]",
      "node_id": "temperature_range",
      "node_type": "TRAIT",
      "description": "Span of ambient temperatures supporting growth.",
      "outcome": "supported_generic",
      "assessment": "Ambient-temperature span is generic parent quantity; does not settle child endpoints versus width."
    },
    {
      "index": 2,
      "field": "causal_graphs[0].nodes[2]",
      "node_id": "baseline_mesophile_adaptation",
      "node_type": "BIOLOGICAL_PROCESS",
      "description": "Standard mesophile membrane and enzyme repertoire supporting growth at moderate ambient temperatures.",
      "outcome": "unknown",
      "assessment": "Generic membrane context only; exact baseline-mesophile mechanism and enzyme fitness efficacy unassessed."
    },
    {
      "index": 3,
      "field": "causal_graphs[0].nodes[3]",
      "node_id": "homeoviscous_adaptation",
      "node_type": "BIOLOGICAL_PROCESS",
      "description": "Regulation of membrane lipid composition to maintain constant viscosity/fluidity across temperatures.",
      "outcome": "partial_generic",
      "assessment": "Lipid composition/physical phase context positive; detailed regulation and constant-across-temperatures efficacy unassessed."
    },
    {
      "index": 4,
      "field": "causal_graphs[0].nodes[4]",
      "node_id": "membrane_fluidity",
      "node_type": "QUALITY",
      "description": "Fluid state of the lipid bilayer required for membrane function.",
      "outcome": "supported_generic",
      "assessment": "Fluid lipid-bilayer physical state supported by retained generic passages."
    },
    {
      "index": 5,
      "field": "causal_graphs[0].nodes[5]",
      "node_id": "unsaturated_fatty_acid_fraction",
      "node_type": "CHEMICAL",
      "description": "Proportion of unsaturated fatty acids in membrane phospholipids.",
      "outcome": "supported_generic",
      "assessment": "UFA proportion and physical-fluidity context positive in Mendoza; fraction-versus-chemical node typing belongs to independent formal audit."
    },
    {
      "index": 6,
      "field": "causal_graphs[0].nodes[6]",
      "node_id": "hopanoids_sterol_like",
      "node_type": "CHEMICAL",
      "description": "Membrane-embedded sterol-like regulators of bilayer fluidity.",
      "outcome": "supported_generic",
      "assessment": "Ramón row27 first two sentences support sterol-like hopanoid membrane physical properties."
    },
    {
      "index": 7,
      "field": "causal_graphs[0].nodes[7]",
      "node_id": "elevated_temperature",
      "node_type": "ENVIRONMENTAL_FACTOR",
      "description": "Increase in ambient growth temperature.",
      "outcome": "supported_generic",
      "assessment": "Ambient temperature increase is generic environmental event context; detailed RNA effect unassessed."
    },
    {
      "index": 8,
      "field": "causal_graphs[0].nodes[8]",
      "node_id": "rna_thermometer",
      "node_type": "RNA",
      "description": "Temperature-responsive mRNA 5′-UTR secondary structure controlling translation initiation.",
      "outcome": "UNASSESSED_SCOPE",
      "assessment": "RNA source identity only; detailed responsive structure/regulatory efficacy unassessed."
    },
    {
      "index": 9,
      "field": "causal_graphs[0].nodes[9]",
      "node_id": "temperature_shift",
      "node_type": "ENVIRONMENTAL_FACTOR",
      "description": "Abrupt change in ambient temperature, including heat shock.",
      "outcome": "supported_generic",
      "assessment": "Temperature change/heat-shock wording is generic event context; detailed response efficacy unassessed."
    },
    {
      "index": 10,
      "field": "causal_graphs[0].nodes[10]",
      "node_id": "heat_shock_proteins",
      "node_type": "GENE_OR_PROTEIN",
      "description": "Molecular chaperones induced by thermal stress that maintain proteostasis.",
      "outcome": "UNASSESSED_SCOPE",
      "assessment": "Aggregate chaperone label/source identity only; detailed induction/proteostasis efficacy unassessed."
    },
    {
      "index": 11,
      "field": "causal_graphs[0].nodes[11]",
      "node_id": "protein_denaturation",
      "node_type": "BIOLOGICAL_PROCESS",
      "description": "Loss of protein structure and aggregation under thermal stress.",
      "outcome": "UNASSESSED_SCOPE",
      "assessment": "Existing denaturation/aggregation process wording retained; detailed thermal-stress efficacy not independently assessed."
    },
    {
      "index": 12,
      "field": "causal_graphs[0].nodes[12]",
      "node_id": "mesophilic_organisms",
      "node_type": "STATE",
      "description": "Organisms growing at moderate temperatures (~20-45 °C).",
      "outcome": "supported_generic",
      "assessment": "Ramón broad mesophile growth20–45 clause supports classification context, not exact optimum or alias equivalence."
    }
  ]
}

### Native checklist: all ten current relations

consistency: concern. Targets: METPO:1000451.

RO2213/RO2211 require process-to-process roles: edges 3/4 have explicit fluidity-quality objects and proportion/chemical subjects. The object mismatch remains independent of the node 5 correction. Broad local confers permits current process/context and quality subjects with trait objects; direct subclass hierarchy is positive. Five lexical edges have no invented imported constraints. Edge 9 ambient bracketing joins the quantity group, not an additional relation finding. Detailed efficacy remains unassessed.

{
  "grounding": [
    {
      "index": 0,
      "field": "causal_graphs[0].edges[0]",
      "edge": {
        "subject": "baseline_mesophile_adaptation",
        "predicate": "confers",
        "object": "temperature_range_mid2_trait",
        "description": "Baseline mesophile adaptation enables growth across 27–30 °C.",
        "evidence": [
          {
            "reference": "DOI:10.1146/annurev-micro-091313-103612",
            "snippet": "more unsaturated fatty acids",
            "notes": "Supports baseline mesophile homeoviscous adaptation as the range mechanism."
          }
        ],
        "predicate_id": "METPO:2007700"
      },
      "outcome": "qualified",
      "judgment": "Local v8 confers has broad causal-node formal endpoints and trait-directed prose; process/context→trait is compatible. Ambiguous quantitative object and detailed efficacy are separately qualified."
    },
    {
      "index": 1,
      "field": "causal_graphs[0].edges[1]",
      "edge": {
        "subject": "temperature_range_mid2_trait",
        "predicate": "is a",
        "object": "temperature_range",
        "description": "Temperature range mid2 is a quantitative bin of the temperature-range phenotype.",
        "evidence": [
          {
            "reference": "DOI:10.1016/s0300-9629(97)00003-0",
            "snippet": "adapted to environments of high temperature",
            "notes": "Supports the 27–30 °C range as a value within the temperature-range distribution."
          }
        ],
        "predicate_id": "rdfs:subClassOf"
      },
      "outcome": "positive",
      "judgment": "Actual rdfs:subClassOf relation matches exact raw METPO child/parent hierarchy; evidence specificity does not change the positive direct hierarchy."
    },
    {
      "index": 2,
      "field": "causal_graphs[0].edges[2]",
      "edge": {
        "subject": "homeoviscous_adaptation",
        "predicate": "maintains",
        "object": "membrane_fluidity",
        "description": "Homeoviscous adaptation maintains membrane lipid viscosity/fluidity.",
        "evidence": [
          {
            "reference": "DOI:10.1007/s42770-023-01057-4",
            "notes": "Homeoviscous adaptation regulates membrane lipid viscosity; generic background mechanism for mesophilic temperature tolerance."
          }
        ]
      },
      "outcome": "qualified",
      "judgment": "Lexical maintains has no predicate_id. Explicit remodeling process→fluidity property is intelligible without importing RO roles; detailed efficacy unassessed."
    },
    {
      "index": 3,
      "field": "causal_graphs[0].edges[3]",
      "edge": {
        "subject": "unsaturated_fatty_acid_fraction",
        "predicate": "increases",
        "object": "membrane_fluidity",
        "description": "Increased unsaturated fatty acid fraction increases membrane fluidity.",
        "evidence": [
          {
            "reference": "DOI:10.1007/s12275-023-00031-x",
            "notes": "Higher unsaturated content increases fluidity; canonical general bacterial thermoadaptation mechanism."
          }
        ],
        "predicate_id": "RO:0002213"
      },
      "outcome": "major",
      "judgment": "RO2213 inherits RO2211 process/process. Explicit fraction subject and fluidity QUALITY object are not processes; object alone independently establishes violation even after node5 is clarified."
    },
    {
      "index": 4,
      "field": "causal_graphs[0].edges[4]",
      "edge": {
        "subject": "hopanoids_sterol_like",
        "predicate": "regulates",
        "object": "membrane_fluidity",
        "description": "Hopanoids / sterol-like molecules regulate membrane fluidity.",
        "evidence": [
          {
            "reference": "DOI:10.1007/s42770-023-01057-4",
            "notes": "Hopanoids and sterol-like molecules act as regulators of membrane fluidity; broad membrane-modulator edge."
          }
        ],
        "predicate_id": "RO:0002211"
      },
      "outcome": "major",
      "judgment": "RO2211 directly requires process/process. Chemical subject and explicit fluidity QUALITY object violate those roles; this persists independently of node5."
    },
    {
      "index": 5,
      "field": "causal_graphs[0].edges[5]",
      "edge": {
        "subject": "membrane_fluidity",
        "predicate": "confers",
        "object": "temperature_range_mid2_trait",
        "description": "Maintained membrane fluidity enables growth across the mid2 temperature range.",
        "evidence": [
          {
            "reference": "DOI:10.1146/annurev-micro-091313-103612",
            "notes": "Functional membrane fluidity underlies homeoviscous adaptation supporting the mesophile range."
          }
        ],
        "predicate_id": "METPO:2007700"
      },
      "outcome": "qualified",
      "judgment": "Local v8 confers admits QUALITY subject→TRAIT; no inherited RO2327 process-range constraint. Numerical bridge and biological efficacy remain unassessed."
    },
    {
      "index": 6,
      "field": "causal_graphs[0].edges[6]",
      "edge": {
        "subject": "elevated_temperature",
        "predicate": "opens",
        "object": "rna_thermometer",
        "description": "Elevated temperature melts/opens RNA thermometer 5′-UTR secondary structure.",
        "evidence": [
          {
            "reference": "DOI:10.1007/s12551-025-01290-1",
            "notes": "5′-UTR secondary structures melt upon heat exposure, exposing ribosome binding sites; broad review-level support."
          }
        ]
      },
      "outcome": "qualified",
      "judgment": "Lexical opens has no predicate_id. Current temperature-increase event and RNA material object are documentary referents only; no imported domain/range or detailed RNA efficacy claim."
    },
    {
      "index": 7,
      "field": "causal_graphs[0].edges[7]",
      "edge": {
        "subject": "temperature_shift",
        "predicate": "induces",
        "object": "heat_shock_proteins",
        "description": "Temperature shift / heat shock induces heat-shock proteins and chaperones.",
        "evidence": [
          {
            "reference": "DOI:10.1007/s12275-023-00031-x",
            "notes": "Temperature shifts induce heat- and cold-shock proteins; high-confidence general stress-response edge."
          }
        ]
      },
      "outcome": "qualified",
      "judgment": "Lexical induces has no predicate_id. Temperature-change event and contextual protein aggregate are not automatically invalid; detailed response efficacy unassessed."
    },
    {
      "index": 8,
      "field": "causal_graphs[0].edges[8]",
      "edge": {
        "subject": "heat_shock_proteins",
        "predicate": "counteracts",
        "object": "protein_denaturation",
        "description": "Heat-shock proteins / chaperones counteract protein denaturation and aggregation.",
        "evidence": [
          {
            "reference": "DOI:10.1007/s12275-023-00031-x",
            "notes": "Chaperones counteract denaturation and aid tolerance; strong general proteostasis edge."
          }
        ]
      },
      "outcome": "qualified",
      "judgment": "Lexical counteracts has no predicate_id. Protein aggregate/process endpoints and negative direction are intelligible; no detailed stress-defense efficacy assessed."
    },
    {
      "index": 9,
      "field": "causal_graphs[0].edges[9]",
      "edge": {
        "subject": "baseline_mesophile_adaptation",
        "predicate": "characterizes",
        "object": "mesophilic_organisms",
        "description": "Mesophilic organisms grow between ~20 °C and ~45 °C, bracketing the mid2 range.",
        "evidence": [
          {
            "reference": "DOI:10.1007/s42770-023-01057-4",
            "notes": "Mesophiles grow between room temperature (~20 °C) and ~45 °C; scope-defining edge placing 27-30 °C within mesophily."
          }
        ]
      },
      "outcome": "concern",
      "judgment": "Lexical characterizes has no imported role constraints. Organism-category type precision is node12 minor; description/note also explicitly embeds the ambient27–30 interval within broader mesophile growth temperatures, conflicting with canonical width interpretation."
    }
  ],
  "source": [
    {
      "index": 0,
      "field": "causal_graphs[0].edges[0]",
      "subject": "baseline_mesophile_adaptation",
      "predicate": "confers",
      "object": "temperature_range_mid2_trait",
      "description": "Baseline mesophile adaptation enables growth across 27–30 °C.",
      "references": [
        "DOI:10.1146/annurev-micro-091313-103612"
      ],
      "outcome": "unknown",
      "assessment": "Generic membrane remodeling supports context; exact baseline-mesophile bin mechanism unestablished. Edge description participates in quantity conflict."
    },
    {
      "index": 1,
      "field": "causal_graphs[0].edges[1]",
      "subject": "temperature_range_mid2_trait",
      "predicate": "is a",
      "object": "temperature_range",
      "description": "Temperature range mid2 is a quantitative bin of the temperature-range phenotype.",
      "references": [
        "DOI:10.1016/s0300-9629(97)00003-0"
      ],
      "outcome": "concern",
      "assessment": "Supplied phrase is literal and explicitly thermophile context; adjacent exact27–30 support note is a bounded attribution concern. Formal hierarchy separate."
    },
    {
      "index": 2,
      "field": "causal_graphs[0].edges[2]",
      "subject": "homeoviscous_adaptation",
      "predicate": "maintains",
      "object": "membrane_fluidity",
      "description": "Homeoviscous adaptation maintains membrane lipid viscosity/fluidity.",
      "references": [
        "DOI:10.1007/s42770-023-01057-4"
      ],
      "outcome": "partial_generic",
      "assessment": "Ramón selected phase/composition context supports generic membrane fluidity interpretation. Detailed adaptive efficacy and exact-bin sufficiency unassessed."
    },
    {
      "index": 3,
      "field": "causal_graphs[0].edges[3]",
      "subject": "unsaturated_fatty_acid_fraction",
      "predicate": "increases",
      "object": "membrane_fluidity",
      "description": "Increased unsaturated fatty acid fraction increases membrane fluidity.",
      "references": [
        "DOI:10.1007/s12275-023-00031-x"
      ],
      "outcome": "unknown_nearest_source",
      "assessment": "Assigned Moon identity only. Mendoza supplies independent generic UFA/fluidity context but does not verify the detailed nearest-source/general thermoadaptation note."
    },
    {
      "index": 4,
      "field": "causal_graphs[0].edges[4]",
      "subject": "hopanoids_sterol_like",
      "predicate": "regulates",
      "object": "membrane_fluidity",
      "description": "Hopanoids / sterol-like molecules regulate membrane fluidity.",
      "references": [
        "DOI:10.1007/s42770-023-01057-4"
      ],
      "outcome": "supported_generic",
      "assessment": "Ramón all-HTML row27 first two sentences directly support hopanoid/sterol-like physical membrane effects and phase modulation; no detailed adaptation intervention adopted."
    },
    {
      "index": 5,
      "field": "causal_graphs[0].edges[5]",
      "subject": "membrane_fluidity",
      "predicate": "confers",
      "object": "temperature_range_mid2_trait",
      "description": "Maintained membrane fluidity enables growth across the mid2 temperature range.",
      "references": [
        "DOI:10.1146/annurev-micro-091313-103612"
      ],
      "outcome": "unknown",
      "assessment": "Generic functional fluidity context does not establish the exact27–30 growth-bin mechanism; no forced source falsehood."
    },
    {
      "index": 6,
      "field": "causal_graphs[0].edges[6]",
      "subject": "elevated_temperature",
      "predicate": "opens",
      "object": "rna_thermometer",
      "description": "Elevated temperature melts/opens RNA thermometer 5′-UTR secondary structure.",
      "references": [
        "DOI:10.1007/s12551-025-01290-1"
      ],
      "outcome": "UNASSESSED_SCOPE",
      "assessment": "New2025 review identity positive. Existing RNA opening/regulatory efficacy claim deliberately unassessed; broad title not treated as citation mismatch."
    },
    {
      "index": 7,
      "field": "causal_graphs[0].edges[7]",
      "subject": "temperature_shift",
      "predicate": "induces",
      "object": "heat_shock_proteins",
      "description": "Temperature shift / heat shock induces heat-shock proteins and chaperones.",
      "references": [
        "DOI:10.1007/s12275-023-00031-x"
      ],
      "outcome": "UNASSESSED_SCOPE",
      "assessment": "Moon identity only; detailed induction/stress-regulation efficacy unassessed."
    },
    {
      "index": 8,
      "field": "causal_graphs[0].edges[8]",
      "subject": "heat_shock_proteins",
      "predicate": "counteracts",
      "object": "protein_denaturation",
      "description": "Heat-shock proteins / chaperones counteract protein denaturation and aggregation.",
      "references": [
        "DOI:10.1007/s12275-023-00031-x"
      ],
      "outcome": "UNASSESSED_SCOPE",
      "assessment": "Moon identity only; detailed chaperone/proteostasis efficacy unassessed."
    },
    {
      "index": 9,
      "field": "causal_graphs[0].edges[9]",
      "subject": "baseline_mesophile_adaptation",
      "predicate": "characterizes",
      "object": "mesophilic_organisms",
      "description": "Mesophilic organisms grow between ~20 °C and ~45 °C, bracketing the mid2 range.",
      "references": [
        "DOI:10.1007/s42770-023-01057-4"
      ],
      "outcome": "supported_generic_with_quantity_conflict",
      "assessment": "Ramón row10 broad mesophile growth20–45 clause positive; bracketing27–30 ambient values is distinct from canonical width28 and shares quantity conflict. No exact-alias biological equivalence inferred."
    }
  ]
}

### Native checklist: exact canonical ledger and conditional predicate grounder

ownership: supported. Targets: METPO:1000451.

The exact SOURCES/TRANCHE canonical payload retains supported interval and width; coordinate quantity interpretation while preserving equality/no-op, nonempty rejection and global queue guards. Increases row 65 and regulates row 11 can recreate incompatible roles in future empty fields; the consumer skips populated IDs, so replay is not current repair. Quantity and organism-category facet findings have only the current record as established faulty owner. Sibling writers remain qualified context.

### Native checklist: bounded human acceptance link

provenance: concern. Targets: METPO:1000451.

Eleven embedded events comprise ten AI-assisted events and a seed. All 25 current history projections are AI and use exact qualified prior whole readings, with zero new whole-history reads. Ignored- and hidden-inclusive search, excluding .git/.venv internals, has 188 matching paths and 68 matching arrays; all 93 actual local top-level review arrays have zero exact target. The append-only clarification corrects preliminary/frozen prose 67 without changing the manifest. Private/remote acceptance remains unknown.

### Native checklist: retained species catalog and bounded adapter availability

completeness: unknown. Targets: METPO:1000451.

The original catalog contains 20 organisms and 28 datasets, with no exact Pseudomonas mangiferae species/strain key. Other Pseudomonas species are not substitutes, and no currently adopted B. subtilis/E. coli source passage establishes coverage. No module query was executed because the runner was unavailable within bounded discovery. No global absence, strain/module or efficacy result is inferred.

### Native checklist: NONMECHANISTIC context and optional instances

completeness: supported. Targets: METPO:1000451.

Three components with thirteen nodes and ten edges are permissible contextual NONMECHANISTIC structure. One aggregate protein class has an explicit REVIEWED_LABEL_ONLY rationale and zero instances; no artificial connector, accession or dataset is required. These structural positives do not resolve the six adjudicated findings.

### Native checklist: current native checks and qualified B14 diagnostics

schema: supported. Targets: METPO:1000451.

Current inspect, target validation, strict validation and snippet checks are successful B15 executions. Four original B14 common diagnostics are qualified for unchanged B15 inputs, not relabeled as fresh B15 executions. Original intervals, historical attempts, product skips and omitted full just test remain explicit. These eight command checks do not establish scientific correctness or human acceptance.

## Findings

### quantity-scope: Quantity scope

major / open / confirmed; issue key: temperature-range-mid2-quantity-scope.

The definition and graph use 27–30 °C as an absolute ambient growth interval, including edge9 placing it inside broader mesophile temperatures; the canonical note treats 27–30 degrees as an interval-width bin. Primary PMID31429815 supports Pseudomonas mangiferae DMKU BBB3-04T growth at12–40 °C, and derived40−12=28 is correct. Raw METPO supplies an existential generic numeric value in[27,30] without specifying endpoints versus width. Reconcile the quantity throughout the record and exact maintained canonical ledger while retaining the supported strain measurement, derived arithmetic and broad mesophile classification.

### quantity-facet: Quantity facet

major / open / confirmed; issue key: temperature-range-mid2-quantity-facet.

The unsaturated_fatty_acid_fraction node explicitly denotes a proportion of unsaturated fatty acids in membrane phospholipids. CHEMICAL represents the material entities being counted, whereas the declared referent is a measurable compositional attribute. This changes the node meaning independently of the imported relation defects. No separate faulty exact writer was established in the bounded maintained-owner evidence.

### imported-process-roles: Imported process roles

major / open / confirmed; issue key: temperature-range-mid2-imported-process-roles.

RO:0002213 inherits process-to-process roles from RO:0002211. Both edges target membrane fluidity, explicitly a quality; edge3 has an explicit fraction/proportion subject and edge4 has a chemical subject. Neither declared referent is a process. The object mismatch persists independently of correcting node5. Wildcard increases row65 and regulates row11 in the maintained mapping can recreate these assignments for future empty predicate_id fields; the consumer skips populated IDs, so ordinary replay does not repair the current fields.

### organism-category-facet: Organism category facet

minor / open / confirmed; issue key: temperature-range-mid2-organism-category-facet.

The mesophilic_organisms node describes a category of organisms growing at moderate temperatures, but STATE is defined here as a bioenergetic or molecular state of the cell. The categorical intent remains legible. Clarify its representation without automatically imposing a replacement enum or adding a new taxon or mechanism.

### bin-attribution: Bin attribution

minor / open / confirmed; issue key: temperature-range-mid2-bin-attribution.

The Mendoza note attributes exact27–30 °C range support to a generic membrane-physics phrase. The Tolner note attributes that bin to a supplied phrase explicitly concerning high-temperature thermophiles. Both snippets are literal; these nearest inspected spans do not establish the adjacent numerical-bin claims. This is a bounded attribution finding without whole-paper absence, false-quotation or biological-refutation claims. The subclass relation has independent raw-ontology support.

### human-acceptance-link: Human acceptance link

minor / open / confirmed; issue key: temperature-range-mid2-human-acceptance-link.

The record is REVIEWED, but its11 embedded events comprise10 AI-assisted events and the METPO seed. All25 current captured history actor projections are AI; whole bodies are exact qualified prior readings. The ignored- and hidden-inclusive bounded local search, excluding .git/.venv internals, found188 matching paths and68 matching review arrays; all93 actual local top-level target arrays contain zero exact target matches. These observations do not supply attributable human acceptance. Private or remote acceptance remains unknown.

## Recommended Actions And Acceptance Checks

### curate-quantity-scope

In separately authorized curation, document the intended measured quantity and reconcile definition, graph and canonical membership with the exact backfill ledger.

- Establish source-backed quantity and unit semantics without deriving endpoints or width solely from generic has-value.
- Retain the strain-specific reported12–40 °C interval and derived width28; align all seven affected fields and preserve independently supported broad mesophile classification.
- Coordinate SOURCES196–200/TRANCHE601–605 and equality, nonempty-rejection and global queue guards. The source measurement is positive; ordinary rerun does not repair semantics.
- Use guarded curation/history, focused strict validation and applicable QC/products; regenerate affected products.

### curate-quantity-facet

Represent the explicit fatty-acid proportion consistently with its measurable-attribute meaning.

- Retain the stated proportion as the referent; distinguish it from its constituent chemical entities.
- Do not rename the node as material merely to hide the facet mismatch or invent biological intermediates.
- Use guarded record/history curation and focused strict/graph validation; assess relation identifiers separately.

### curate-imported-process-roles

Resolve the two relation identifiers against the retained referents and coordinate conditional mapping recurrence.

- Document subject/object referents and formal domain/range support for each of edges3 and4.
- Preserve the proportion, fluidity quality and chemical facets; do not relabel solely to pass a check or invent mechanism intermediates.
- Address both increases row65 and regulates row11 for future empty-field grounding; explicitly repair populated IDs through guarded curation.
- Run focused strict validation, applicable graph/QC/products and meaningful grounding regression checks. No intervention or efficacy claim is prescribed.

### curate-organism-category-facet

Clarify how the existing mesophile organism category is represented in this classification context.

- Document the category meaning and distinguish it from the schema-defined molecular or bioenergetic STATE.
- Choose a representation supported by the maintained schema without automatically prescribing another enum or adding unsupported organisms.
- Retain source-backed generic classification and validate the separately curated record.

### curate-bin-attribution

Qualify the two evidence notes to distinguish generic physical or thermophile context from exact numerical-bin authority.

- Describe the nearest inspected spans accurately; exact27–30 calibration needs identified support or remains qualified.
- Retain all three literal snippets and the actual native three-VERIFIED result.
- Preserve independently supported hierarchy; avoid whole-paper absence or biological-refutation claims and validate the separately curated record.

### curate-human-acceptance-link

Link attributable human acceptance for REVIEWED status or accurately qualify the review state in separately authorized curation.

- Retain actor identity, exact scope and a retrievable acceptance reference; AI review and seed import do not establish human signoff.
- Preserve bounded local-search limitations and private/remote uncertainty.
- Use maintained guarded history and validation procedures for any curation change.

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
| check-temperature-range-mid2-target-validate | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-target-validate.log; Executed 2026-10-22T04:10:02.459958+00:00 through 2026-10-22T04:10:03.242594+00:00; metadata temperature-range-mid2-target-validate.json | context_only | Native record validation passed; scientific interpretation is assessed separately. |
| check-temperature-range-mid2-target-strict | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-target-strict.log; Executed 2026-10-22T04:10:02.461036+00:00 through 2026-10-22T04:10:03.647140+00:00; metadata temperature-range-mid2-target-strict.json | context_only | The actual validate-strict command passed. |
| check-temperature-range-mid2-snippets-network | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-snippets-network.log; Executed 2026-10-22T04:10:12.727980+00:00 through 2026-10-22T04:10:16.134748+00:00; metadata temperature-range-mid2-snippets-network.json | context_only | Native command completed successfully with all three snippets VERIFIED. Separate manual primary matching also supports three literal spans; this does not establish adjacent numerical-bin claims. |
| capture | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2.inspect.json; Actual successful native inspect with 107 captured inputs | context_only | All current captured source hashes and the exact target are bound before serialization. |
| record | data/traits/environment/temperature_range_mid2.yaml; Whole current record | supports | Thirteen nodes, ten edges, eleven embedded events, one canonical example, one reviewed label-only protein class and zero instances. |
| local-init | /private/tmp/traitmech-record-sweep-015.67f2ce7a/batch015-local-initialization-receipt.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Actual local initialization and second queue target; publication remains separate. |
| policy | docs/GROUNDING_POLICY.md; Captured maintained authority | supports | Protein family/function grounding, reviewed label-only aggregates and optional instances. |
| playbook | docs/CURATION_PLAYBOOK.md; Captured maintained authority | supports | Source attribution and attributable acceptance. |
| schema | src/traitmech/schema/traitmech.yaml; Captured maintained authority | supports | Current material, molecular-activity, process, quality and quantitative NONMECHANISTIC facets. |
| predicate-mapping | mappings/predicate_grounding.tsv; Captured maintained authority | supports | Wildcard closeMatch increases row 65 and regulates row 11 can recreate incompatible imported roles in future empty fields; current populated IDs are skipped. |
| canonical-writer | scripts/backfill_canonical_examples_444.py; Captured maintained authority | supports | Exact Pseudomonas mangiferae SOURCES/TRANCHE payload and equality, rejection and global queue guards; positive interval and width with coordinated quantity interpretation. |
| identity | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-grounding-agent/identity-and-hierarchy.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Active target and parent; historical Mesophilie retention and unresolved broad qualitative equivalence. Generic numeric existential does not decide endpoints versus width. |
| nodes-edges | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-grounding-agent/node-edge-grounding-ledger.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | All thirteen current node referents and ten formal relation dispositions. |
| owners | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-grounding-agent/ownership-assessment.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Exact canonical ledger and conditional predicate mapping applicability; sibling writers remain qualified context. |
| owner-primary | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-grounding-agent/owner-primary-reading.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Selected current owner windows and exact replay guards without writer execution. |
| local-authority | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-grounding-agent/local-authority-reading.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Actual schema, policy, local proposals and mapping reading scope. |
| histories | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-grounding-agent/history-reading-provenance.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Twenty-five current actor/event projections with exact qualified prior whole readings; zero new whole-history reads. |
| embedded-history | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-grounding-agent/embedded-history-ledger.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Eleven embedded events: ten AI-assisted events and one seed. |
| human-search | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-grounding-agent/search-and-provenance.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Ignored- and hidden-inclusive local search: 188 matching paths, 68 matching arrays and 93 all-local review arrays, zero exact target. |
| discovery | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-grounding-agent/discovery-dispositions.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Uncaptured leads remain matching-line context; private or remote acceptance unknown. |
| expression | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-grounding-agent/expression-and-readiness.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Three NONMECHANISTIC components and one reviewed label-only protein aggregate are allowed; no exact canonical species/strain catalog key or module result. |
| expression-discovery | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-grounding-agent/adapter-discovery.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Bounded maintained-runner discovery found no available adapter; no query executed. |
| catalog-reuse | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-grounding-agent/catalog-reuse.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Original catalog acquisition preserved separately from current copying and selected-name reading. |
| ground-reading | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-grounding-agent/reading-scope-receipt.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Exact current reading scopes, qualified prior histories and owner qualifications. |
| ground-assessment | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-grounding-agent/grounding-assessment.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Three ground majors include the shared quantity finding counted once; category-facet and human minors. |
| ground-manifest | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-grounding-agent/evidence-manifest.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | All 26 immutable ground artifacts verified. |
| ontology-primary | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-source-root/selected-ontology-primary.json; Exact selected response; query 2026-10-22T04:10:52.267509+00:00 through 2026-10-22T04:10:52.276330+00:00 | supports | Current RO, raw METPO and local v3/v8/v85 selected authority. Copy/read time is not query time. Ground auditor did not repeat queries or database hashing; the serializer common guard separately verifies qualified inputs. |
| authority-primary | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-source-root/selected-authority-primary.json; Exact selected response; query 2026-10-22T04:10:52.277412+00:00 through 2026-10-22T04:10:52.325770+00:00 | supports | Current RO, raw METPO and local v3/v8/v85 selected authority. Copy/read time is not query time. Ground auditor did not repeat queries or database hashing; the serializer common guard separately verifies qualified inputs. |
| authority-provenance | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-grounding-agent/primary-reuse-provenance.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Actual current root query clocks and exact ground-auditor copies; separate reading completion. |
| catalog-original | https://imodulondb.org/api/datasets; Original retained 20-organism/28-dataset catalog | context_only | No exact Pseudomonas mangiferae species/strain key in this retained catalog. Other Pseudomonas entries are not substitutes. No current adopted B. subtilis/E. coli source passage establishes coverage; no strain/module or efficacy inference. |
| mendoza-metadata | DOI:10.1146/annurev-micro-091313-103612; Indexed identity and first abstract sentence | supports | Supplied generic membrane-physics snippets are literal; exact 27–30 bin attribution is not established by these nearest spans. |
| mendoza-publisher | DOI:10.1146/annurev-micro-091313-103612; Retained publisher browser-tool export; historical call interval, not raw HTML | supports | Selected abstract wording retained. Underlying cache fetch time is unknown; no current fresh publisher acquisition is claimed. |
| cold-metadata | DOI:10.1007/s42770-023-01057-4; Indexed identity and original notice fields | supports | Identity verified; detailed stress-defense and survival efficacy remain unassessed. |
| cold-body | DOI:10.1007/s42770-023-01057-4; Source/root adopted zero-based all-HTML row 17 first four physical sentences, row 27 first two physical sentences and row 10 mesophile clause | supports | Generic physical and broad classification context only. Later numerical, gene, adaptation and intervention text is incidental and unadopted. |
| tolner-metadata | DOI:10.1016/s0300-9629(97)00003-0; Indexed identity and first two thermophile abstract sentences | supports | Supplied snippet is literal and explicitly concerns high-temperature thermophiles; adjacent exact-bin support is not established. |
| tolner-crossref | DOI:10.1016/s0300-9629(97)00003-0; Original Crossref identifier/title | supports | Source identity positive; no detailed transport or regulatory efficacy assessed. |
| moon-metadata | DOI:10.1007/s12275-023-00031-x; Title/DOI/PMID/publication and notice fields only | supports | Detailed RNA/DNA topology regulation, survival/fitness and intervention efficacy remain UNASSESSED_SCOPE. |
| canonical-metadata | DOI:10.1099/ijsem.0.003657; Original indexed abstract named-strain opening, temperature-growth sentence and type-material statement | supports | Pseudomonas mangiferae DMKU BBB3-04T reported growth at 12–40 °C and derived width 28 are positive. Original metadata retrieval was October 21; no current fresh canonical acquisition or optimum inference. |
| rna-review-metadata | DOI:10.1007/s12551-025-01290-1; Current official title, identifiers and original notice fields only | supports | Source identity positive. Detailed RNA thermoregulation, structure/function, stress-response and intervention efficacy remain UNASSESSED_SCOPE; no current body acquired. |
| rna-review-access | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-source-agent/rna-review-metadata-access.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Actual current identity-only metadata request interval; distinct from the eight historical source acquisitions and current copying. |
| taxonomy | NCBITaxon:2593654; Fresh successful official species/type-material response | supports | Pseudomonas mangiferae species and DMKU BBB3-04 type-material identities positive; no quantitative phenotype inferred from taxonomy. |
| taxonomy-access | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-grounding-agent/taxonomy-retry-access.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Actual successful retry interval and hash. |
| taxonomy-reading | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-grounding-agent/taxonomy-identity.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Official identity, successful response and separate initial failed access. |
| taxonomy-initial-failure | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=2593654&amp;retmode=xml; Initial DNS error bytes, not taxonomy XML | context_only | Access failure is retained separately from successful retry and native validation. |
| sources | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-source-agent/source-assessment.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Six works; shared quantity conflict and bounded nearest-span attribution concern, with detailed efficacy unassessed. |
| source-identities | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-source-agent/source-ledger.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | All six identities and selected scopes; reused metadata notices retain original times, alongside one new RNA-review identity request. |
| source-status | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-source-agent/source-status-ledger.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Original-time notice observations, not an exhaustive fresh status search. |
| placements | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-source-agent/source-placement-ledger.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | All thirteen external placements; nine grounding fields are separately covered by node-edge audits. |
| snippets | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-source-agent/snippet-ledger.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | All three supplied snippets are literal in original indexed abstracts. |
| notes | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-source-agent/source-note-ledger.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Twelve notes including the singular canonical note; exact-bin attribution distinct from literal text. |
| source-nodes-edges | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-source-agent/node-edge-source-ledger.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | All thirteen nodes and ten edges with supported, partial, unknown and unassessed dispositions. |
| canonical | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-source-agent/canonical-assessment.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Named source interval and derived width positive, incompatible current quantity interpretations grouped once. |
| source-reading | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-source-agent/primary-reading-scope.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Selected identity, physical/classification text and literal spans; no whole-paper or detailed efficacy review. |
| source-access | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-source-agent/source-access-limits.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Retained primary surfaces and one new RNA-review metadata request; canonical metadata is reused, no new body access. |
| source-reuse | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-source-agent/source-reuse-receipt.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Eight exact copies with flat original-access clocks and prior-receipt hashes, including original canonical retrieval. |
| source-native | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-source-agent/native-context.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Native three VERIFIED and separate manual three literal results. |
| source-manifest | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-source-agent/evidence-manifest.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | All 24 frozen source artifacts verified. |
| search-count-clarification | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-grounding-agent/matching-array-count-clarification.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Append-only correction of preliminary/frozen prose 67 to actual 68 matching arrays; 93 all-local arrays, 188 matching paths and zero exact targets remain explicit. Frozen manifest unchanged. |
| root-reading | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-source-root/selected-primary-reading.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Root corrected selected source, authority and owner reading scopes, narrower than some source-auditor windows; incidental content not adopted. |
| root-verification | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-source-root/root-current-verification.json; Frozen current audit or retained receipt; original reading scope controls interpretation | context_only | Root exact current input, frozen artifact, qualified history and local review-array verification. |
| adjudication | /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-root-adjudication.json; Final root adjudication | supports | Exact three majors and three minors, six findings/actions and owner/field scopes control this combined review. |

## Limits And Additional Notes

- No fresh B15 common diagnostic execution is asserted. Full just test was NOT_RUN; only the five optional focused Stage2 tests are reused. Products retains 123 no-adapter skips and covers two configured mappings. Common checks establish bounded software/data integrity, not scientific support, current-target checks or prior-batch finalization. Serializers must append to these helper notes and limitations.
- Detailed stress-defense, regulatory adaptation, survival/fitness, molecular enhancement, cultivation optimization and intervention efficacy remain UNASSESSED_SCOPE; no operational repair proposed.
- Canonical source growth12–40 and derived width28 are positive; ambient27–30 versus width27–30 conflict is counted once. Generic ontology values are not assumed to choose the operationalization.
- Three snippets are literal; adjacent exact-bin note support is a separate bounded attribution concern. No whole-paper absence or biological refutation.
- Only selected original abstract/body clauses adopted; no full-body review claimed.
- Complete canonical abstract was displayed; cultivation, chemistry and other taxonomic comparisons were incidental and unadopted beyond named type strain/aliases and existing growth interval.
- Ramón term search displayed whole rows7/17/27, including detailed adaptation and a gene-target discussion. Only row17 first four physical sentences, row27 first two physical sentences and row10 mesophile classification clause adopted. No later numerical, gene or intervention text adopted.
- Tolner second indexed sentence includes wider transport/enzyme context; only explicit thermophile context and supplied literal fragment adopted.
- Moon and new2025 RNA-review work identity only; detailed RNA/stress/chaperone/proteostasis efficacy deliberately unassessed. Broad review title is not evidence of citation mismatch.
- No new current body acquisition. Reused publisher export is a historical tool response, not raw HTML; underlying cache fetch time unknown.
- Publication notice observations retain original request dates for reused sources. Null indexed notices do not establish exhaustive current absence.
- Broad mesophile growth20–45 classification does not establish exact optimum or exact-alias equivalence. Incidental named species outside selected clauses are not current source-organism evidence.
- Detailed temperature-response regulation, stress defense, fitness, efficacy and optimization are UNASSESSED_SCOPE.
- Generic numerical OWL restriction does not settle interval versus breadth; exact mesophilic alias equivalence remains unknown, not a separate finding.
- Baseline adaptation/repertoire description is mixed but not forced into an additional type finding.
- All25 current projections plus exactly qualified prior whole readings; no current whole-history claim.
- Uncaptured script/history discovery remains matching-line context; private/remote acceptance unknown.
- Ground auditor did not rerun common diagnostics, native checks or database hashing; root handles those separately. Source-specific findings remain separately adjudicated.
- Root adopted Ramón zero-based HTML p10 mesophile clause, p17 first four physical sentences and p27 first two physical sentences only; later numerical/gene/intervention text in displayed paragraphs is incidental and unadopted.
- Taxonomy initial DNS failure and successful retry retain separate observations; taxon identity alone does not establish phenotype.
- Ground frozen discovery scope says67 matching arrays; append-only count clarification and actual metadata establish68. All93 actual arrays were checked, with zero exact matches.
- Original B14 common diagnostics are qualified for unchanged B15 inputs, not fresh B15 executions. Current target inspect, target validation, strict validation and snippet checks are fresh B15 executions. The serializer common guard separately rechecks current inputs and five database pins.
- Full just test was not run; five focused Stage2 tests and product skips retain their original scope. Common software checks do not establish scientific correctness.
- Active exact METPO:1000451 identity and direct parent METPO:1000306 are positive. Historical Mesophilie retention is explicitly documented by active-review row105, release-delta row1273 and finalizer; biological exact equivalence to the unresolved quantity remains unknown.
- Homeoviscous adaptation METPO:1016200 is locally proposed v85, absent from the captured upstream raw OWL. Local v3 fluidity is a quality; broad v8 confers permits the current process/context and quality subjects with trait objects.
- Temperature increase and shift nodes describe actual events; the RNA thermometer structure is material RNA. Five lexical edges carry no invented RO/Biolink role constraints. Baseline adaptation/repertoire is mixed but not forced into an additional finding.
- Canonical primary metadata and official taxonomy support Pseudomonas mangiferae DMKU BBB3-04T, type aliases TBRC7080/JCM32061, reported12–40 °C and derived width28. Source optimum is separate and not adopted as the interval or width.
- Three components,13 nodes/10 edges and one explicitly reviewed label-only protein aggregate are permissible NONMECHANISTIC context; zero protein instances do not require invented connectors, accessions or datasets.
- The retained catalog contains20 organisms/28 datasets and no exact P.mangiferae species/strain entry. Other Pseudomonas species are not substitutes. No currently adopted B.subtilis/E.coli passage establishes source-species coverage. Bounded adapter discovery did not yield a runner; no module query or efficacy inference.
- Publication is separate from this local review. No scientific record, mapping, ontology, history, generated product or paid-provider run changes.
- Qualified reuse of four original B14 diagnostics is recorded in /private/tmp/traitmech-record-sweep-015.67f2ce7a/common-diagnostic-reuse-qualification.json. Historical products failures/retry and original cache provenance remain in /private/tmp/traitmech-record-sweep-014.q8m4v2cs/new-base-diagnostic-independent-review-agent/fresh-products-completion.json. B14 generated reports are retained output snapshots, not B15 source inputs or synthetic B15 reports. B15-to-B14 byte equality does not change the historical false B14-to-B13 comparison; B14 final gates/commit and continuation pins remain separate.
- Final fields, categories, severities, owners and actions come only from actual root FINAL. The shared quantity conflict is counted once; independent quantity-facet and process-role majors plus three bounded minors remain separate. Representation is a permitted review-schema category, so no category remapping is applied.
- Serializer preparation adopts frozen audits and root adjudication and does not claim another whole-paper or whole-history review. Original canonical/source/catalog acquisitions, current RNA metadata/taxonomy/query times and copying/reading clocks remain distinct. The ground auditor did not repeat common/database checks; the serializer common guard separately verifies qualified current inputs. Original B14 diagnostics remain qualified history, not fresh B15 execution.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T042122Z-temperature-range-mid2
kind: record
repository: CultureBotAI/TraitMech
title: Whole-record review of temperature range mid2
started_at: '2026-10-22T04:09:31.682492Z'
finished_at: '2026-10-22T04:21:22Z'
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
summary: 'Whole-record review identifies three major issues: absolute-interval versus
  interval-width semantics, a proportion typed as chemical material, and incompatible
  imported process roles at two edges. Three bounded minors concern an organism-category
  facet, exact-bin attribution and a retrievable human-acceptance link. Active identity,
  canonical reported12–40 °C interval and derived width28, three literal snippets
  and selected formal endpoint facets are positive; detailed microbial efficacy remains
  unassessed.'
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
  - path: data/traits/environment/temperature_range_mid2.yaml
    sha256: 8733cf17429fadfda65188c2dcf931a6b8d18de91f2556c5befb5fc993b0e6d6
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
  - path: reports/metpo_2026_06_12_active_review.tsv
    sha256: 45e9c6471475635ba1f2602cd636a119d490f5dbd8dd6ac8af1aab89a321379f
    role: context
  - path: reports/metpo_2026_06_12_release_delta.tsv
    sha256: afe858d2aa0ade08322c7808d5917ff370e069ba02c2642d483342db8e9323ac
    role: context
  - path: reports/ontology_snapshot_manifest.tsv
    sha256: 4a157279a8c4e3fc2afb5382a45c31961991bbd1f330f26d0061b0cfd0b4d213
    role: context
  - path: research/traits/environment/temperature_range_mid2-deep-research-falcon.md
    sha256: fcfa93d90e3ef895bd20d0dcb52aef05f95048b42b74a56d7b9e4b2800739558
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
- target_id: METPO:1000451
  path: data/traits/environment/temperature_range_mid2.yaml
  label: temperature range mid2
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_range_mid2.yaml
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
  selection: Second record in the actual B15 queue; current 270-line target and 107
    captured inputs. Local review is independent of remote publication.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - METPO:1000451
checks:
- check_id: new-base-qc
  name: Reused B14 corpus QC
  status: passed
  required: true
  target_ids:
  - METPO:1000451
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
  - METPO:1000451
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
  - METPO:1000451
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
  - METPO:1000451
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
- check_id: temperature-range-mid2-target-validate
  name: Focused native validation
  status: passed
  required: true
  target_ids:
  - METPO:1000451
  command: just validate data/traits/environment/temperature_range_mid2.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Native record validation passed; scientific interpretation is assessed
    separately.
  evidence_ids:
  - check-temperature-range-mid2-target-validate
- check_id: temperature-range-mid2-target-strict
  name: Focused strict validation
  status: passed
  required: true
  target_ids:
  - METPO:1000451
  command: just validate-strict data/traits/environment/temperature_range_mid2.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: The actual validate-strict command passed.
  evidence_ids:
  - check-temperature-range-mid2-target-strict
- check_id: temperature-range-mid2-snippets-network
  name: Focused network snippet check
  status: passed
  required: true
  target_ids:
  - METPO:1000451
  command: just verify-snippets --record data/traits/environment/temperature_range_mid2.yaml
    --out /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-snippets.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: Native command completed successfully with all three snippets VERIFIED.
    Separate manual primary matching also supports three literal spans; this does
    not establish adjacent numerical-bin claims.
  evidence_ids:
  - check-temperature-range-mid2-snippets-network
- check_id: native-inspect
  name: One-target native review capture
  status: passed
  required: true
  target_ids:
  - METPO:1000451
  command: uv run python scripts/record_review.py inspect --targets /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2.targets.json
    --input .claude/skills/curate-yaml-record/references/review-checklist.md --input
    .claude/skills/manage-identifiers/SKILL.md --input .claude/skills/review-yaml-record/SKILL.md
    --input CLAUDE.md --input DO_NOT_WORK.md --input conf/evidence_snippet_baseline.tsv
    --input conf/record_review.yaml --input data/raw/biolink-model.yaml --input data/raw/metpo.owl
    --input data/traits/environment/temperature_range.yaml --input docs/CURATION_PLAYBOOK.md
    --input docs/GROUNDING_POLICY.md --input docs/PATHWAY_LINKS.md --input docs/record-review-profile.md
    --input docs/record-reviews.md --input history/infrastructure/canonical-examples/2026-08-19T183734Z-claude-code-44a170.yaml
    --input history/infrastructure/node-type-consistency/2026-08-15T014631Z-claude-code-9d7f4d.yaml
    --input history/infrastructure/pr664-adversarial-review/2026-09-07T010000Z-codex-60bca2.yaml
    --input history/infrastructure/pr664-adversarial-review/2026-09-07T072500Z-codex-693abc.yaml
    --input history/infrastructure/prioritize-graph-research/2026-08-18T073129Z-claude-code-6ffbb9.yaml
    --input history/infrastructure/prioritize-graph-research/2026-08-20T072722Z-claude-code-5774c9.yaml
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
    --input proposals/metpo_traitmech_v3/metpo_proposal_classes_robot.tsv --input
    proposals/metpo_traitmech_v3/proposal.md --input proposals/metpo_traitmech_v8/metpo_proposal_properties_robot.tsv
    --input proposals/metpo_traitmech_v8/proposal.md --input proposals/metpo_traitmech_v85/metpo_proposal_classes_robot.tsv
    --input proposals/metpo_traitmech_v85/proposal.md --input reports/metpo_2026_06_12_active_review.tsv
    --input reports/metpo_2026_06_12_release_delta.tsv --input reports/ontology_snapshot_manifest.tsv
    --input research/traits/environment/temperature_range_mid2-deep-research-falcon.md
    --input schema/record_review.yaml --input scripts/add_homeoviscous_adaptation_trait.py
    --input scripts/audit_causal_graphs.py --input scripts/audit_graph_protein_taxa.py
    --input scripts/audit_predicate_domains.py --input scripts/audit_schema.py --input
    scripts/audit_unapplied_groundings.py --input scripts/audit_uniprot_grounding.py
    --input scripts/backfill_canonical_examples_444.py --input scripts/connect_mesophilic_graph_183.py
    --input scripts/connect_temperature_delta_high_graph_183.py --input scripts/connect_temperature_delta_very_low_graph_183.py
    --input scripts/connect_temperature_optimum_high_graph_183.py --input scripts/connect_temperature_optimum_very_low_graph_183.py
    --input scripts/connect_temperature_range_mid3_graph_183.py --input scripts/connect_temperature_range_mid4_graph_183.py
    --input scripts/connect_temperature_range_very_low_graph_183.py --input scripts/enrich_lateral_flagellation_trait.py
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
    --input scripts/review_temperature_optimum_high_graph_183.py --input scripts/review_temperature_optimum_very_low_graph_183.py
    --input scripts/review_temperature_range_mid3_graph_183.py --input scripts/review_temperature_range_mid4_graph_183.py
    --input scripts/review_temperature_range_very_low_graph_183.py --input scripts/seed_from_metpo.py
    --input scripts/trait_priority.py --input scripts/verify_metpo_proposal.py --input
    src/traitmech/schema/mech_shared.yaml --input src/traitmech/schema/traitmech.yaml
    --input src/traitmech/validation/write_validated.py
  exit_code: 0
  expected_exit_code: 0
  summary: One current target, 107 captured inputs, exact current base and successful
    native inspect.
  evidence_ids:
  - capture
- check_id: uniprot-applicability
  name: Protein-instance metadata applicability
  status: not_applicable
  required: false
  target_ids:
  - METPO:1000451
  summary: One contextual protein aggregate is REVIEWED_LABEL_ONLY with an explicit
    rationale and zero instances; no token accession required.
  evidence_ids:
  - record
  - policy
  - expression
- check_id: expression-adapter-availability
  name: Structured source-organism expression query availability
  status: unavailable
  required: false
  target_ids:
  - METPO:1000451
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
- evidence_id: check-temperature-range-mid2-target-validate
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-target-validate.log
  locator: Executed 2026-10-22T04:10:02.459958+00:00 through 2026-10-22T04:10:03.242594+00:00;
    metadata temperature-range-mid2-target-validate.json
  accessed_at: '2026-10-22T04:10:03.242594Z'
  support: context_only
  summary: Native record validation passed; scientific interpretation is assessed
    separately.
  snapshot_sha256: b5148633b8626eff45d0e790be0f84f8559e7fa22688b0a6c715deb9db3eb9ac
- evidence_id: check-temperature-range-mid2-target-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-target-strict.log
  locator: Executed 2026-10-22T04:10:02.461036+00:00 through 2026-10-22T04:10:03.647140+00:00;
    metadata temperature-range-mid2-target-strict.json
  accessed_at: '2026-10-22T04:10:03.647140Z'
  support: context_only
  summary: The actual validate-strict command passed.
  snapshot_sha256: 1efff25680a645a73ddf7b70f29b6313090df0bf8efc8217f9dde0bfee066f15
- evidence_id: check-temperature-range-mid2-snippets-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-snippets-network.log
  locator: Executed 2026-10-22T04:10:12.727980+00:00 through 2026-10-22T04:10:16.134748+00:00;
    metadata temperature-range-mid2-snippets-network.json
  accessed_at: '2026-10-22T04:10:16.134748Z'
  support: context_only
  summary: Native command completed successfully with all three snippets VERIFIED.
    Separate manual primary matching also supports three literal spans; this does
    not establish adjacent numerical-bin claims.
  snapshot_sha256: 7873a72f329fe96a0904e7a25a35e0bf8f484aa36f3196ea8d407f41843e9865
- evidence_id: capture
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2.inspect.json
  locator: Actual successful native inspect with 107 captured inputs
  accessed_at: '2026-10-22T04:09:32.441438Z'
  support: context_only
  summary: All current captured source hashes and the exact target are bound before
    serialization.
  snapshot_sha256: 9d43df016890e699926d48b3a323222bc72ae31bf05822d6f24c985c3955a16f
- evidence_id: record
  kind: record_content
  reference: data/traits/environment/temperature_range_mid2.yaml
  locator: Whole current record
  accessed_at: '2026-10-22T04:09:32.441438Z'
  support: supports
  summary: Thirteen nodes, ten edges, eleven embedded events, one canonical example,
    one reviewed label-only protein class and zero instances.
  snapshot_sha256: 8733cf17429fadfda65188c2dcf931a6b8d18de91f2556c5befb5fc993b0e6d6
- evidence_id: local-init
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/batch015-local-initialization-receipt.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T03:50:31.750633Z'
  support: context_only
  summary: Actual local initialization and second queue target; publication remains
    separate.
  snapshot_sha256: b5fc6d47e2719f9da11bad0719b933f4af76d4ccc30226c15a2a7c51c07e2283
- evidence_id: policy
  kind: authority
  reference: docs/GROUNDING_POLICY.md
  locator: Captured maintained authority
  accessed_at: '2026-10-22T04:13:13.296003Z'
  support: supports
  summary: Protein family/function grounding, reviewed label-only aggregates and optional
    instances.
  snapshot_sha256: 891678c983c2283a47c81c47950b35753981e9339d105f3bbdda92a1f5ab7f42
- evidence_id: playbook
  kind: authority
  reference: docs/CURATION_PLAYBOOK.md
  locator: Captured maintained authority
  accessed_at: '2026-10-22T04:13:13.296003Z'
  support: supports
  summary: Source attribution and attributable acceptance.
  snapshot_sha256: 735e9b810471da9f7d8364e35ffe1e741edb3421480dac01727db6ea5aa65da9
- evidence_id: schema
  kind: authority
  reference: src/traitmech/schema/traitmech.yaml
  locator: Captured maintained authority
  accessed_at: '2026-10-22T04:13:13.296003Z'
  support: supports
  summary: Current material, molecular-activity, process, quality and quantitative
    NONMECHANISTIC facets.
  snapshot_sha256: 46c47fc627b80ccbba1e8ab3fb6f2aee93bc2aef7aaf72fe9aadc3257f2c02dd
- evidence_id: predicate-mapping
  kind: authority
  reference: mappings/predicate_grounding.tsv
  locator: Captured maintained authority
  accessed_at: '2026-10-22T04:13:13.296003Z'
  support: supports
  summary: Wildcard closeMatch increases row 65 and regulates row 11 can recreate
    incompatible imported roles in future empty fields; current populated IDs are
    skipped.
  snapshot_sha256: 8e28c19e93aca3dc164a3befbe2612b289241de457c59f499e65936c03b7ce52
- evidence_id: canonical-writer
  kind: authority
  reference: scripts/backfill_canonical_examples_444.py
  locator: Captured maintained authority
  accessed_at: '2026-10-22T04:13:13.296003Z'
  support: supports
  summary: Exact Pseudomonas mangiferae SOURCES/TRANCHE payload and equality, rejection
    and global queue guards; positive interval and width with coordinated quantity
    interpretation.
  snapshot_sha256: 18ca0766789c239d693ef665e8b1d43c1209a0f414a326f1c5d890f88de7b20c
- evidence_id: identity
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-grounding-agent/identity-and-hierarchy.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:13:13.291618Z'
  support: context_only
  summary: Active target and parent; historical Mesophilie retention and unresolved
    broad qualitative equivalence. Generic numeric existential does not decide endpoints
    versus width.
  snapshot_sha256: fb1c3cf89a915c38c223da1239c888c888b967e7dba5498c9d4c4405f0cd8509
- evidence_id: nodes-edges
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-grounding-agent/node-edge-grounding-ledger.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:13:13.291253Z'
  support: context_only
  summary: All thirteen current node referents and ten formal relation dispositions.
  snapshot_sha256: e70db638ca047163a56ace29796f3a127c44a6f6879dcc0554f3614c774dcab2
- evidence_id: owners
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-grounding-agent/ownership-assessment.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:13:13.295030Z'
  support: context_only
  summary: Exact canonical ledger and conditional predicate mapping applicability;
    sibling writers remain qualified context.
  snapshot_sha256: 97f4be61da231df3213f5c4ee9370c01a3154288f04d9676fcf298aa5ac50035
- evidence_id: owner-primary
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-grounding-agent/owner-primary-reading.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:13:13.288450Z'
  support: context_only
  summary: Selected current owner windows and exact replay guards without writer execution.
  snapshot_sha256: 098a634e58c1f23d9e222b08a4a93d5bcf5e72cffe1534b380e4aee19dc3bb0c
- evidence_id: local-authority
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-grounding-agent/local-authority-reading.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:13:13.290425Z'
  support: context_only
  summary: Actual schema, policy, local proposals and mapping reading scope.
  snapshot_sha256: 9a497f02ef5d60d0222407b3d04be0a80b6b7d9fb02c720d71861c7efd1d3e7d
- evidence_id: histories
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-grounding-agent/history-reading-provenance.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:13:13.286703Z'
  support: context_only
  summary: Twenty-five current actor/event projections with exact qualified prior
    whole readings; zero new whole-history reads.
  snapshot_sha256: 738ee33af00b9386ed514c19a26f4a8b85d19bd849d90e4ae69ab3f0157c0b68
- evidence_id: embedded-history
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-grounding-agent/embedded-history-ledger.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:13:13.287216Z'
  support: context_only
  summary: 'Eleven embedded events: ten AI-assisted events and one seed.'
  snapshot_sha256: 09dec637b678a513c99d8c203ccc8ab619e1edc314f870ef58ba41f9b1d34457
- evidence_id: human-search
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-grounding-agent/search-and-provenance.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:10:09.680962Z'
  support: context_only
  summary: 'Ignored- and hidden-inclusive local search: 188 matching paths, 68 matching
    arrays and 93 all-local review arrays, zero exact target.'
  snapshot_sha256: dbf203e9970aba6fcefaaaf546c92196f9c3b82b8ca55be168a918e66a97dc5e
- evidence_id: discovery
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-grounding-agent/discovery-dispositions.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:13:13.294861Z'
  support: context_only
  summary: Uncaptured leads remain matching-line context; private or remote acceptance
    unknown.
  snapshot_sha256: 6c088e8b8e36d1f80fb36aa39e849bea56f708289762d0715fb4cf6e66146936
- evidence_id: expression
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-grounding-agent/expression-and-readiness.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:13:13.295839Z'
  support: context_only
  summary: Three NONMECHANISTIC components and one reviewed label-only protein aggregate
    are allowed; no exact canonical species/strain catalog key or module result.
  snapshot_sha256: 4821f4123ab71b00b27cf13a95779f2da2c8bac4a1645b75163be84775ac4419
- evidence_id: expression-discovery
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-grounding-agent/adapter-discovery.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:10:09.818175Z'
  support: context_only
  summary: Bounded maintained-runner discovery found no available adapter; no query
    executed.
  snapshot_sha256: d431b50462d44ca747e8e025919f34ba66fdf3d8ae286a7442fdb330c1b0ccd7
- evidence_id: catalog-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-grounding-agent/catalog-reuse.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:13:13.295738Z'
  support: context_only
  summary: Original catalog acquisition preserved separately from current copying
    and selected-name reading.
  snapshot_sha256: 19784c982689b77c242f7a92ccbf7872137c80fae8b2cc6dd05a5557ebf29c6d
- evidence_id: ground-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-grounding-agent/reading-scope-receipt.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:13:13.296161Z'
  support: context_only
  summary: Exact current reading scopes, qualified prior histories and owner qualifications.
  snapshot_sha256: b704994fd2b9df36bf2944bee47868f4c20379b7293767a1c9322909b507a127
- evidence_id: ground-assessment
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-grounding-agent/grounding-assessment.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:13:13.296003Z'
  support: context_only
  summary: Three ground majors include the shared quantity finding counted once; category-facet
    and human minors.
  snapshot_sha256: 8b6555e2dd11dc7ec5465e6ffb31f55ee5de3020b84bd269b3497afbba20f3e3
- evidence_id: ground-manifest
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-grounding-agent/evidence-manifest.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:13:14.839895Z'
  support: context_only
  summary: All 26 immutable ground artifacts verified.
  snapshot_sha256: 33d9133f1f1cb4388aee0278e1b6fd39be10ab38f65ef0ce596428957085f9fb
- evidence_id: ontology-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-source-root/selected-ontology-primary.json
  locator: Exact selected response; query 2026-10-22T04:10:52.267509+00:00 through
    2026-10-22T04:10:52.276330+00:00
  accessed_at: '2026-10-22T04:10:52.276330Z'
  support: supports
  summary: Current RO, raw METPO and local v3/v8/v85 selected authority. Copy/read
    time is not query time. Ground auditor did not repeat queries or database hashing;
    the serializer common guard separately verifies qualified inputs.
  snapshot_sha256: 9a4045f3891ad65ad8ce661ab4020667ee4dafe207342d760a2c79ec7fdee5a9
- evidence_id: authority-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-source-root/selected-authority-primary.json
  locator: Exact selected response; query 2026-10-22T04:10:52.277412+00:00 through
    2026-10-22T04:10:52.325770+00:00
  accessed_at: '2026-10-22T04:10:52.325770Z'
  support: supports
  summary: Current RO, raw METPO and local v3/v8/v85 selected authority. Copy/read
    time is not query time. Ground auditor did not repeat queries or database hashing;
    the serializer common guard separately verifies qualified inputs.
  snapshot_sha256: aeee534d6d03b9db2feff63d6def3b8a36761085e7a95b90d0a476e0a5d3f4ee
- evidence_id: authority-provenance
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-grounding-agent/primary-reuse-provenance.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:13:13.282687Z'
  support: context_only
  summary: Actual current root query clocks and exact ground-auditor copies; separate
    reading completion.
  snapshot_sha256: 14b05f89d663fce96da84d3be626012567cbe8791877e81a8e4ed791b1b25efa
- evidence_id: catalog-original
  kind: authority
  reference: https://imodulondb.org/api/datasets
  locator: Original retained 20-organism/28-dataset catalog
  accessed_at: '2026-10-21T07:36:12.858149Z'
  support: context_only
  summary: No exact Pseudomonas mangiferae species/strain key in this retained catalog.
    Other Pseudomonas entries are not substitutes. No current adopted B. subtilis/E.
    coli source passage establishes coverage; no strain/module or efficacy inference.
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: mendoza-metadata
  kind: primary_source
  reference: DOI:10.1146/annurev-micro-091313-103612
  locator: Indexed identity and first abstract sentence
  accessed_at: '2026-10-21T10:00:02.042457Z'
  support: supports
  summary: Supplied generic membrane-physics snippets are literal; exact 27–30 bin
    attribution is not established by these nearest spans.
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
  locator: Source/root adopted zero-based all-HTML row 17 first four physical sentences,
    row 27 first two physical sentences and row 10 mesophile clause
  accessed_at: '2026-10-21T22:07:50.938485Z'
  support: supports
  summary: Generic physical and broad classification context only. Later numerical,
    gene, adaptation and intervention text is incidental and unadopted.
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
- evidence_id: moon-metadata
  kind: primary_source
  reference: DOI:10.1007/s12275-023-00031-x
  locator: Title/DOI/PMID/publication and notice fields only
  accessed_at: '2026-10-21T09:25:42.394675Z'
  support: supports
  summary: Detailed RNA/DNA topology regulation, survival/fitness and intervention
    efficacy remain UNASSESSED_SCOPE.
  snapshot_sha256: c4ed17a04c2e85dfe16fee756b0f5347ae4599d17fc03622f63ff7c84a1ff8aa
- evidence_id: canonical-metadata
  kind: primary_source
  reference: DOI:10.1099/ijsem.0.003657
  locator: Original indexed abstract named-strain opening, temperature-growth sentence
    and type-material statement
  accessed_at: '2026-10-21T18:54:55.843450Z'
  support: supports
  summary: Pseudomonas mangiferae DMKU BBB3-04T reported growth at 12–40 °C and derived
    width 28 are positive. Original metadata retrieval was October 21; no current
    fresh canonical acquisition or optimum inference.
  snapshot_sha256: 5f587025ea2b441b1515ef89466ded6efb01f84f639a29d2b506b18054537609
- evidence_id: rna-review-metadata
  kind: primary_source
  reference: DOI:10.1007/s12551-025-01290-1
  locator: Current official title, identifiers and original notice fields only
  accessed_at: '2026-10-22T04:10:49.707921Z'
  support: supports
  summary: Source identity positive. Detailed RNA thermoregulation, structure/function,
    stress-response and intervention efficacy remain UNASSESSED_SCOPE; no current
    body acquired.
  snapshot_sha256: 27e9b4ecee22dd311b10484eebb541b8d503a4334ce5cb441057946002d3f2bd
- evidence_id: rna-review-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-source-agent/rna-review-metadata-access.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:10:49.707921Z'
  support: context_only
  summary: Actual current identity-only metadata request interval; distinct from the
    eight historical source acquisitions and current copying.
  snapshot_sha256: 206796f0717379598900c1e0b39246526d3f5d52f085489e491f62152bfa8d82
- evidence_id: taxonomy
  kind: authority
  reference: NCBITaxon:2593654
  locator: Fresh successful official species/type-material response
  accessed_at: '2026-10-22T04:10:33.301325Z'
  support: supports
  summary: Pseudomonas mangiferae species and DMKU BBB3-04 type-material identities
    positive; no quantitative phenotype inferred from taxonomy.
  snapshot_sha256: 0a1b6c810cca04cdf7edd35f6bd65acacff5d8c9d7d4d842e67a56819d2bfe8f
- evidence_id: taxonomy-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-grounding-agent/taxonomy-retry-access.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:10:33.301325Z'
  support: context_only
  summary: Actual successful retry interval and hash.
  snapshot_sha256: 88cef66dc0d7f094d76ab1a85d37bde27419504cd271b918a2db647b467e401f
- evidence_id: taxonomy-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-grounding-agent/taxonomy-identity.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:13:13.290955Z'
  support: context_only
  summary: Official identity, successful response and separate initial failed access.
  snapshot_sha256: 7589aad3a73608f600e040034157c8470659004eaf249984ef822a7661eb9308
- evidence_id: taxonomy-initial-failure
  kind: validation
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=2593654&retmode=xml
  locator: Initial DNS error bytes, not taxonomy XML
  accessed_at: '2026-10-22T04:10:09.833564Z'
  support: context_only
  summary: Access failure is retained separately from successful retry and native
    validation.
  snapshot_sha256: 35281279d8e2164cee8666d6f8aad891326911e887ab1b2ab778c8ac6d09dc6c
- evidence_id: sources
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-source-agent/source-assessment.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:13:03.480710Z'
  support: context_only
  summary: Six works; shared quantity conflict and bounded nearest-span attribution
    concern, with detailed efficacy unassessed.
  snapshot_sha256: aff25efb86c1084214d16997a600d8326d0d303d3441ac062381a7c13734fb7a
- evidence_id: source-identities
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-source-agent/source-ledger.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:13:03.477056Z'
  support: context_only
  summary: All six identities and selected scopes; reused metadata notices retain
    original times, alongside one new RNA-review identity request.
  snapshot_sha256: 8ab5c1df64ac57edd92c1730c9c6ff5fdc652f7e4c3c395df14d9f1c50d1db33
- evidence_id: source-status
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-source-agent/source-status-ledger.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:13:03.477056Z'
  support: context_only
  summary: Original-time notice observations, not an exhaustive fresh status search.
  snapshot_sha256: db4ee418ebb7a973fe93541726ea0b0716b872b9d903fb87440547b916c6b655
- evidence_id: placements
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-source-agent/source-placement-ledger.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:13:03.477056Z'
  support: context_only
  summary: All thirteen external placements; nine grounding fields are separately
    covered by node-edge audits.
  snapshot_sha256: 700b854e02f5c55933421cd239eb23f8a6366cf06a0399bffbbcf8bc522ea377
- evidence_id: snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-source-agent/snippet-ledger.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:13:03.477056Z'
  support: context_only
  summary: All three supplied snippets are literal in original indexed abstracts.
  snapshot_sha256: 885886544a51e495b38939815d6529bbc9d4e5622c958eeb8fb63252eb8f8cbe
- evidence_id: notes
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-source-agent/source-note-ledger.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:13:03.477056Z'
  support: context_only
  summary: Twelve notes including the singular canonical note; exact-bin attribution
    distinct from literal text.
  snapshot_sha256: b11461b684c0d751b75bc02babb7e5873da967f691e8bb94f63cccf0b919cfd1
- evidence_id: source-nodes-edges
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-source-agent/node-edge-source-ledger.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:13:03.477056Z'
  support: context_only
  summary: All thirteen nodes and ten edges with supported, partial, unknown and unassessed
    dispositions.
  snapshot_sha256: 92875e9bb7a4f585035711e4b8f26a757488d20fe221333425a477488e989368
- evidence_id: canonical
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-source-agent/canonical-assessment.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:13:03.477056Z'
  support: context_only
  summary: Named source interval and derived width positive, incompatible current
    quantity interpretations grouped once.
  snapshot_sha256: 57b2b122b6df9d0a9ee5fd4262507f9a8e92ef3c72a137b99e99439588dd4d14
- evidence_id: source-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-source-agent/primary-reading-scope.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:13:03.479679Z'
  support: context_only
  summary: Selected identity, physical/classification text and literal spans; no whole-paper
    or detailed efficacy review.
  snapshot_sha256: f35726d7a01c48e9274a0b939e14f3f9747a6c3914456412c6abe1b574153ebe
- evidence_id: source-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-source-agent/source-access-limits.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:13:03.477056Z'
  support: context_only
  summary: Retained primary surfaces and one new RNA-review metadata request; canonical
    metadata is reused, no new body access.
  snapshot_sha256: ee4747c04c8cffa45cf86eaa456ffe0438f3d1b45e43b6f46eab0cabf5a87045
- evidence_id: source-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-source-agent/source-reuse-receipt.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:10:26.246897Z'
  support: context_only
  summary: Eight exact copies with flat original-access clocks and prior-receipt hashes,
    including original canonical retrieval.
  snapshot_sha256: 5c2d31256b7a464447d249c127b0317dc5682d33a5bd7b468a5672b5d7bb7ff7
- evidence_id: source-native
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-source-agent/native-context.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:13:03.480342Z'
  support: context_only
  summary: Native three VERIFIED and separate manual three literal results.
  snapshot_sha256: 9adac52d3534e9d0e2bb3d8d57cd36ba2ccb54c681f06c6c76933165edf68bc6
- evidence_id: source-manifest
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-source-agent/evidence-manifest.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:13:03.481058Z'
  support: context_only
  summary: All 24 frozen source artifacts verified.
  snapshot_sha256: 53b659e20f4dbf0178efa35aee6e7011e833420121526a1c6c37324c115eb791
- evidence_id: search-count-clarification
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-grounding-agent/matching-array-count-clarification.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:13:25.372000Z'
  support: context_only
  summary: Append-only correction of preliminary/frozen prose 67 to actual 68 matching
    arrays; 93 all-local arrays, 188 matching paths and zero exact targets remain
    explicit. Frozen manifest unchanged.
  snapshot_sha256: 3aeb530898b1cb71d3a022b76d880b17ae23b7a225d0b36aa3865c5f669ff334
- evidence_id: root-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-source-root/selected-primary-reading.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:12:31.528287Z'
  support: context_only
  summary: Root corrected selected source, authority and owner reading scopes, narrower
    than some source-auditor windows; incidental content not adopted.
  snapshot_sha256: c143c4ab89183cca02c900a2361aa7fff1e4c4666a98dbf1b6dd1ffe3d9c027d
- evidence_id: root-verification
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-source-root/root-current-verification.json
  locator: Frozen current audit or retained receipt; original reading scope controls
    interpretation
  accessed_at: '2026-10-22T04:17:42.131119Z'
  support: context_only
  summary: Root exact current input, frozen artifact, qualified history and local
    review-array verification.
  snapshot_sha256: e7b07cdfda7ad4f46e48f8d87e03f61c0b98871dcd569b5ab093425cfe8381d3
- evidence_id: adjudication
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-015.67f2ce7a/temperature-range-mid2-root-adjudication.json
  locator: Final root adjudication
  accessed_at: '2026-10-22T04:17:42.135729Z'
  support: supports
  summary: Exact three majors and three minors, six findings/actions and owner/field
    scopes control this combined review.
  snapshot_sha256: 01576d48b237dd1966cb5931f7898cabfae19a6a040d74c58deca16c3bffe065
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: active bin and direct parent'
  outcome: supported
  target_ids:
  - METPO:1000451
  summary: Active METPO:1000451 and direct parent METPO:1000306 are positive. Historical
    Mesophilie retention is documented; broad exact biological equivalence to the
    unresolved numerical quantity remains unknown. Homeoviscous adaptation METPO:1016200
    is locally proposed in v85, not asserted active in the captured upstream raw OWL.
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
  - METPO:1000451
  summary: Definition, graph and edge 9 bracketing use 27–30 °C as ambient values
    while the canonical note uses an interval-width bin. Reported growth at 12–40
    °C and arithmetic 40 minus 12 equals 28 are correct. One grouped major reconciles
    all seven fields while preserving the measurement and broad mesophile classification.
    Generic has-value restrictions do not choose endpoints or width.
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
  - METPO:1000451
  summary: The retained original primary abstract supports Pseudomonas mangiferae
    DMKU BBB3-04T, type aliases TBRC 7080/JCM 32061, reported growth at 12–40 °C and
    derived width 28. Fresh official taxonomy supports identity only. Source optimum
    remains separate. Membership interpretation participates in quantity scope; no
    false measurement, wrong organism or cultivation optimization is asserted.
  evidence_ids:
  - canonical
  - canonical-metadata
  - taxonomy
  - taxonomy-reading
  - adjudication
- assessment_id: source-support
  area: evidence
  topic: 'Native checklist: six works and thirteen placements'
  outcome: concern
  target_ids:
  - METPO:1000451
  summary: All six identities resolve. Mendoza generic membrane physics and Tolner
    high-temperature thermophile spans do not establish adjacent exact 27–30-bin notes.
    Selected Ramón physical and broad mesophile classification clauses are qualified
    positives. Moon and the new RNA review provide identity only; nearest-source edge
    3 support and detailed RNA, stress, chaperone, regulation, survival/fitness and
    intervention efficacy remain unassessed. No whole-paper absence or title-based
    citation mismatch is inferred.
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
  - moon-metadata
  - rna-review-metadata
  - adjudication
- assessment_id: quotations
  area: evidence
  topic: 'Native checklist: three supplied literal snippets'
  outcome: supported
  target_ids:
  - METPO:1000451
  summary: All three current schema snippets are literal in retained indexed abstracts,
    consistent with the actual native three-VERIFIED result. Literal text does not
    establish adjacent numerical-bin attribution. No copied-span finding is added.
  evidence_ids:
  - snippets
  - source-native
  - mendoza-metadata
  - tolner-metadata
  - notes
- assessment_id: nodes
  area: representation
  topic: 'Native checklist: all thirteen current referents'
  outcome: concern
  target_ids:
  - METPO:1000451
  summary: Node 5 explicitly denotes a measurable fatty-acid proportion but is typed
    CHEMICAL, an independent major. Node 12 denotes an organism category rather than
    the schema-defined cellular STATE, a bounded minor. Locally proposed homeoviscous
    process, fluidity quality, temperature-change events and material RNA are otherwise
    positive or qualified. The baseline adaptation/repertoire is mixed without an
    extra forced finding; the reviewed label-only protein aggregate needs no token
    accession.
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
    causal_graphs[0].nodes[0]\",\n      \"node\": {\n        \"node_id\": \"temperature_range_mid2_trait\"\
    ,\n        \"label\": \"temperature range mid2\",\n        \"node_type\": \"TRAIT\"\
    ,\n        \"grounding\": \"METPO:1000451\",\n        \"description\": \"Temperature\
    \ growth-supporting range approximately 27–30 °C.\"\n      },\n      \"outcome\"\
    : \"concern\",\n      \"judgment\": \"Active exact METPO identity, but ambient27–30\
    \ wording participates in interval-versus-width conflict.\"\n    },\n    {\n \
    \     \"index\": 1,\n      \"field\": \"causal_graphs[0].nodes[1]\",\n      \"\
    node\": {\n        \"node_id\": \"temperature_range\",\n        \"label\": \"\
    temperature range\",\n        \"node_type\": \"TRAIT\",\n        \"grounding\"\
    : \"METPO:1000306\",\n        \"description\": \"Span of ambient temperatures\
    \ supporting growth.\"\n      },\n      \"outcome\": \"positive\",\n      \"judgment\"\
    : \"Exact active temperature-range parent; direct raw hierarchy positive.\"\n\
    \    },\n    {\n      \"index\": 2,\n      \"field\": \"causal_graphs[0].nodes[2]\"\
    ,\n      \"node\": {\n        \"node_id\": \"baseline_mesophile_adaptation\",\n\
    \        \"label\": \"baseline mesophile adaptation\",\n        \"node_type\"\
    : \"BIOLOGICAL_PROCESS\",\n        \"description\": \"Standard mesophile membrane\
    \ and enzyme repertoire supporting growth at moderate ambient temperatures.\"\n\
    \      },\n      \"outcome\": \"qualified\",\n      \"judgment\": \"Adaptation\
    \ label suggests a process while description names membrane/enzyme repertoire.\
    \ Mixed process/material context is legible but not resolved into a mandatory\
    \ extra type finding; detailed efficacy unassessed.\"\n    },\n    {\n      \"\
    index\": 3,\n      \"field\": \"causal_graphs[0].nodes[3]\",\n      \"node\":\
    \ {\n        \"node_id\": \"homeoviscous_adaptation\",\n        \"label\": \"\
    homeoviscous adaptation\",\n        \"node_type\": \"BIOLOGICAL_PROCESS\",\n \
    \       \"description\": \"Regulation of membrane lipid composition to maintain\
    \ constant viscosity/fluidity across temperatures.\",\n        \"grounding\":\
    \ \"METPO:1016200\"\n      },\n      \"outcome\": \"positive\",\n      \"judgment\"\
    : \"Explicit lipid-composition remodeling process agrees with locally proposed\
    \ METPO1016200 in v85; raw upstream zero-match is not treated as invalid local\
    \ grounding.\"\n    },\n    {\n      \"index\": 4,\n      \"field\": \"causal_graphs[0].nodes[4]\"\
    ,\n      \"node\": {\n        \"node_id\": \"membrane_fluidity\",\n        \"\
    label\": \"membrane fluidity\",\n        \"node_type\": \"QUALITY\",\n       \
    \ \"description\": \"Fluid state of the lipid bilayer required for membrane function.\"\
    ,\n        \"grounding\": \"METPO:1007505\"\n      },\n      \"outcome\": \"positive\"\
    ,\n      \"judgment\": \"Explicit membrane fluidity property agrees with local\
    \ v3 METPO1007505 quality; not a process.\"\n    },\n    {\n      \"index\": 5,\n\
    \      \"field\": \"causal_graphs[0].nodes[5]\",\n      \"node\": {\n        \"\
    node_id\": \"unsaturated_fatty_acid_fraction\",\n        \"label\": \"unsaturated\
    \ fatty acid fraction\",\n        \"node_type\": \"CHEMICAL\",\n        \"description\"\
    : \"Proportion of unsaturated fatty acids in membrane phospholipids.\"\n     \
    \ },\n      \"outcome\": \"major\",\n      \"judgment\": \"Explicit fraction/proportion\
    \ is a measurable compositional attribute, not the chemical entities being counted.\
    \ CHEMICAL materially changes the declared referent; independent from imported\
    \ relation repair.\"\n    },\n    {\n      \"index\": 6,\n      \"field\": \"\
    causal_graphs[0].nodes[6]\",\n      \"node\": {\n        \"node_id\": \"hopanoids_sterol_like\"\
    ,\n        \"label\": \"hopanoids / sterol-like molecules\",\n        \"node_type\"\
    : \"CHEMICAL\",\n        \"description\": \"Membrane-embedded sterol-like regulators\
    \ of bilayer fluidity.\"\n      },\n      \"outcome\": \"positive\",\n      \"\
    judgment\": \"Named membrane-embedded molecules have a material chemical referent.\
    \ Their imported process relation at edge4 is assessed separately; efficacy unassessed.\"\
    \n    },\n    {\n      \"index\": 7,\n      \"field\": \"causal_graphs[0].nodes[7]\"\
    ,\n      \"node\": {\n        \"node_id\": \"elevated_temperature\",\n       \
    \ \"label\": \"elevated temperature\",\n        \"node_type\": \"ENVIRONMENTAL_FACTOR\"\
    ,\n        \"description\": \"Increase in ambient growth temperature.\"\n    \
    \  },\n      \"outcome\": \"positive\",\n      \"judgment\": \"Description denotes\
    \ an increase/change in ambient temperature. ENVIRONMENTAL_FACTOR permits exposure/condition\
    \ shorthand and is not automatically invalid for this event.\"\n    },\n    {\n\
    \      \"index\": 8,\n      \"field\": \"causal_graphs[0].nodes[8]\",\n      \"\
    node\": {\n        \"node_id\": \"rna_thermometer\",\n        \"label\": \"RNA\
    \ thermometer 5′-UTR structure\",\n        \"node_type\": \"RNA\",\n        \"\
    description\": \"Temperature-responsive mRNA 5′-UTR secondary structure controlling\
    \ translation initiation.\"\n      },\n      \"outcome\": \"positive\",\n    \
    \  \"judgment\": \"mRNA secondary structure is an RNA material referent; detailed\
    \ regulatory activity and efficacy unassessed.\"\n    },\n    {\n      \"index\"\
    : 9,\n      \"field\": \"causal_graphs[0].nodes[9]\",\n      \"node\": {\n   \
    \     \"node_id\": \"temperature_shift\",\n        \"label\": \"temperature shift\
    \ / heat shock\",\n        \"node_type\": \"ENVIRONMENTAL_FACTOR\",\n        \"\
    description\": \"Abrupt change in ambient temperature, including heat shock.\"\
    \n      },\n      \"outcome\": \"positive\",\n      \"judgment\": \"Explicit abrupt\
    \ temperature change/heat shock is an event, not automatically invalid by ENV\
    \ enum.\"\n    },\n    {\n      \"index\": 10,\n      \"field\": \"causal_graphs[0].nodes[10]\"\
    ,\n      \"node\": {\n        \"node_id\": \"heat_shock_proteins\",\n        \"\
    label\": \"heat-shock proteins / chaperones\",\n        \"node_type\": \"GENE_OR_PROTEIN\"\
    ,\n        \"grounding_status\": \"REVIEWED_LABEL_ONLY\",\n        \"grounding_notes\"\
    : \"Reviewed as a contextual protein or protein-complex label within a quantitative\
    \ measurement graph; no exact semantic family term was established for this aggregate\
    \ use.\",\n        \"description\": \"Molecular chaperones induced by thermal\
    \ stress that maintain proteostasis.\"\n      },\n      \"outcome\": \"qualified\"\
    ,\n      \"judgment\": \"Contextual aggregate chaperone protein label has explicit\
    \ REVIEWED_LABEL_ONLY rationale, no accession/instance forced in a NONMECHANISTIC\
    \ graph; detailed proteostasis efficacy unassessed.\"\n    },\n    {\n      \"\
    index\": 11,\n      \"field\": \"causal_graphs[0].nodes[11]\",\n      \"node\"\
    : {\n        \"node_id\": \"protein_denaturation\",\n        \"label\": \"protein\
    \ denaturation / aggregation\",\n        \"node_type\": \"BIOLOGICAL_PROCESS\"\
    ,\n        \"description\": \"Loss of protein structure and aggregation under\
    \ thermal stress.\"\n      },\n      \"outcome\": \"positive\",\n      \"judgment\"\
    : \"Explicit denaturation/aggregation is a biological process as a referent only;\
    \ detailed stress efficacy unassessed.\"\n    },\n    {\n      \"index\": 12,\n\
    \      \"field\": \"causal_graphs[0].nodes[12]\",\n      \"node\": {\n       \
    \ \"node_id\": \"mesophilic_organisms\",\n        \"label\": \"mesophilic organisms\"\
    ,\n        \"node_type\": \"STATE\",\n        \"description\": \"Organisms growing\
    \ at moderate temperatures (~20-45 °C).\"\n      },\n      \"outcome\": \"minor\"\
    ,\n      \"judgment\": \"Description denotes an organism category, not the schema-defined\
    \ bioenergetic or molecular cellular STATE. Intent remains clear; bounded facet\
    \ precision finding without prescribing a replacement enum.\"\n    }\n  ],\n \
    \ \"source\": [\n    {\n      \"index\": 0,\n      \"field\": \"causal_graphs[0].nodes[0]\"\
    ,\n      \"node_id\": \"temperature_range_mid2_trait\",\n      \"node_type\":\
    \ \"TRAIT\",\n      \"description\": \"Temperature growth-supporting range approximately\
    \ 27–30 °C.\",\n      \"outcome\": \"concern\",\n      \"assessment\": \"Ambient27–30\
    \ description participates in shared quantity conflict; exact ontology identity\
    \ assessed separately.\"\n    },\n    {\n      \"index\": 1,\n      \"field\"\
    : \"causal_graphs[0].nodes[1]\",\n      \"node_id\": \"temperature_range\",\n\
    \      \"node_type\": \"TRAIT\",\n      \"description\": \"Span of ambient temperatures\
    \ supporting growth.\",\n      \"outcome\": \"supported_generic\",\n      \"assessment\"\
    : \"Ambient-temperature span is generic parent quantity; does not settle child\
    \ endpoints versus width.\"\n    },\n    {\n      \"index\": 2,\n      \"field\"\
    : \"causal_graphs[0].nodes[2]\",\n      \"node_id\": \"baseline_mesophile_adaptation\"\
    ,\n      \"node_type\": \"BIOLOGICAL_PROCESS\",\n      \"description\": \"Standard\
    \ mesophile membrane and enzyme repertoire supporting growth at moderate ambient\
    \ temperatures.\",\n      \"outcome\": \"unknown\",\n      \"assessment\": \"\
    Generic membrane context only; exact baseline-mesophile mechanism and enzyme fitness\
    \ efficacy unassessed.\"\n    },\n    {\n      \"index\": 3,\n      \"field\"\
    : \"causal_graphs[0].nodes[3]\",\n      \"node_id\": \"homeoviscous_adaptation\"\
    ,\n      \"node_type\": \"BIOLOGICAL_PROCESS\",\n      \"description\": \"Regulation\
    \ of membrane lipid composition to maintain constant viscosity/fluidity across\
    \ temperatures.\",\n      \"outcome\": \"partial_generic\",\n      \"assessment\"\
    : \"Lipid composition/physical phase context positive; detailed regulation and\
    \ constant-across-temperatures efficacy unassessed.\"\n    },\n    {\n      \"\
    index\": 4,\n      \"field\": \"causal_graphs[0].nodes[4]\",\n      \"node_id\"\
    : \"membrane_fluidity\",\n      \"node_type\": \"QUALITY\",\n      \"description\"\
    : \"Fluid state of the lipid bilayer required for membrane function.\",\n    \
    \  \"outcome\": \"supported_generic\",\n      \"assessment\": \"Fluid lipid-bilayer\
    \ physical state supported by retained generic passages.\"\n    },\n    {\n  \
    \    \"index\": 5,\n      \"field\": \"causal_graphs[0].nodes[5]\",\n      \"\
    node_id\": \"unsaturated_fatty_acid_fraction\",\n      \"node_type\": \"CHEMICAL\"\
    ,\n      \"description\": \"Proportion of unsaturated fatty acids in membrane\
    \ phospholipids.\",\n      \"outcome\": \"supported_generic\",\n      \"assessment\"\
    : \"UFA proportion and physical-fluidity context positive in Mendoza; fraction-versus-chemical\
    \ node typing belongs to independent formal audit.\"\n    },\n    {\n      \"\
    index\": 6,\n      \"field\": \"causal_graphs[0].nodes[6]\",\n      \"node_id\"\
    : \"hopanoids_sterol_like\",\n      \"node_type\": \"CHEMICAL\",\n      \"description\"\
    : \"Membrane-embedded sterol-like regulators of bilayer fluidity.\",\n      \"\
    outcome\": \"supported_generic\",\n      \"assessment\": \"Ramón row27 first two\
    \ sentences support sterol-like hopanoid membrane physical properties.\"\n   \
    \ },\n    {\n      \"index\": 7,\n      \"field\": \"causal_graphs[0].nodes[7]\"\
    ,\n      \"node_id\": \"elevated_temperature\",\n      \"node_type\": \"ENVIRONMENTAL_FACTOR\"\
    ,\n      \"description\": \"Increase in ambient growth temperature.\",\n     \
    \ \"outcome\": \"supported_generic\",\n      \"assessment\": \"Ambient temperature\
    \ increase is generic environmental event context; detailed RNA effect unassessed.\"\
    \n    },\n    {\n      \"index\": 8,\n      \"field\": \"causal_graphs[0].nodes[8]\"\
    ,\n      \"node_id\": \"rna_thermometer\",\n      \"node_type\": \"RNA\",\n  \
    \    \"description\": \"Temperature-responsive mRNA 5′-UTR secondary structure\
    \ controlling translation initiation.\",\n      \"outcome\": \"UNASSESSED_SCOPE\"\
    ,\n      \"assessment\": \"RNA source identity only; detailed responsive structure/regulatory\
    \ efficacy unassessed.\"\n    },\n    {\n      \"index\": 9,\n      \"field\"\
    : \"causal_graphs[0].nodes[9]\",\n      \"node_id\": \"temperature_shift\",\n\
    \      \"node_type\": \"ENVIRONMENTAL_FACTOR\",\n      \"description\": \"Abrupt\
    \ change in ambient temperature, including heat shock.\",\n      \"outcome\":\
    \ \"supported_generic\",\n      \"assessment\": \"Temperature change/heat-shock\
    \ wording is generic event context; detailed response efficacy unassessed.\"\n\
    \    },\n    {\n      \"index\": 10,\n      \"field\": \"causal_graphs[0].nodes[10]\"\
    ,\n      \"node_id\": \"heat_shock_proteins\",\n      \"node_type\": \"GENE_OR_PROTEIN\"\
    ,\n      \"description\": \"Molecular chaperones induced by thermal stress that\
    \ maintain proteostasis.\",\n      \"outcome\": \"UNASSESSED_SCOPE\",\n      \"\
    assessment\": \"Aggregate chaperone label/source identity only; detailed induction/proteostasis\
    \ efficacy unassessed.\"\n    },\n    {\n      \"index\": 11,\n      \"field\"\
    : \"causal_graphs[0].nodes[11]\",\n      \"node_id\": \"protein_denaturation\"\
    ,\n      \"node_type\": \"BIOLOGICAL_PROCESS\",\n      \"description\": \"Loss\
    \ of protein structure and aggregation under thermal stress.\",\n      \"outcome\"\
    : \"UNASSESSED_SCOPE\",\n      \"assessment\": \"Existing denaturation/aggregation\
    \ process wording retained; detailed thermal-stress efficacy not independently\
    \ assessed.\"\n    },\n    {\n      \"index\": 12,\n      \"field\": \"causal_graphs[0].nodes[12]\"\
    ,\n      \"node_id\": \"mesophilic_organisms\",\n      \"node_type\": \"STATE\"\
    ,\n      \"description\": \"Organisms growing at moderate temperatures (~20-45\
    \ °C).\",\n      \"outcome\": \"supported_generic\",\n      \"assessment\": \"\
    Ramón broad mesophile growth20–45 clause supports classification context, not\
    \ exact optimum or alias equivalence.\"\n    }\n  ]\n}"
- assessment_id: relations
  area: consistency
  topic: 'Native checklist: all ten current relations'
  outcome: concern
  target_ids:
  - METPO:1000451
  summary: 'RO2213/RO2211 require process-to-process roles: edges 3/4 have explicit
    fluidity-quality objects and proportion/chemical subjects. The object mismatch
    remains independent of the node 5 correction. Broad local confers permits current
    process/context and quality subjects with trait objects; direct subclass hierarchy
    is positive. Five lexical edges have no invented imported constraints. Edge 9
    ambient bracketing joins the quantity group, not an additional relation finding.
    Detailed efficacy remains unassessed.'
  evidence_ids:
  - nodes-edges
  - source-nodes-edges
  - ontology-primary
  - authority-primary
  - local-authority
  - adjudication
  details: "{\n  \"grounding\": [\n    {\n      \"index\": 0,\n      \"field\": \"\
    causal_graphs[0].edges[0]\",\n      \"edge\": {\n        \"subject\": \"baseline_mesophile_adaptation\"\
    ,\n        \"predicate\": \"confers\",\n        \"object\": \"temperature_range_mid2_trait\"\
    ,\n        \"description\": \"Baseline mesophile adaptation enables growth across\
    \ 27–30 °C.\",\n        \"evidence\": [\n          {\n            \"reference\"\
    : \"DOI:10.1146/annurev-micro-091313-103612\",\n            \"snippet\": \"more\
    \ unsaturated fatty acids\",\n            \"notes\": \"Supports baseline mesophile\
    \ homeoviscous adaptation as the range mechanism.\"\n          }\n        ],\n\
    \        \"predicate_id\": \"METPO:2007700\"\n      },\n      \"outcome\": \"\
    qualified\",\n      \"judgment\": \"Local v8 confers has broad causal-node formal\
    \ endpoints and trait-directed prose; process/context→trait is compatible. Ambiguous\
    \ quantitative object and detailed efficacy are separately qualified.\"\n    },\n\
    \    {\n      \"index\": 1,\n      \"field\": \"causal_graphs[0].edges[1]\",\n\
    \      \"edge\": {\n        \"subject\": \"temperature_range_mid2_trait\",\n \
    \       \"predicate\": \"is a\",\n        \"object\": \"temperature_range\",\n\
    \        \"description\": \"Temperature range mid2 is a quantitative bin of the\
    \ temperature-range phenotype.\",\n        \"evidence\": [\n          {\n    \
    \        \"reference\": \"DOI:10.1016/s0300-9629(97)00003-0\",\n            \"\
    snippet\": \"adapted to environments of high temperature\",\n            \"notes\"\
    : \"Supports the 27–30 °C range as a value within the temperature-range distribution.\"\
    \n          }\n        ],\n        \"predicate_id\": \"rdfs:subClassOf\"\n   \
    \   },\n      \"outcome\": \"positive\",\n      \"judgment\": \"Actual rdfs:subClassOf\
    \ relation matches exact raw METPO child/parent hierarchy; evidence specificity\
    \ does not change the positive direct hierarchy.\"\n    },\n    {\n      \"index\"\
    : 2,\n      \"field\": \"causal_graphs[0].edges[2]\",\n      \"edge\": {\n   \
    \     \"subject\": \"homeoviscous_adaptation\",\n        \"predicate\": \"maintains\"\
    ,\n        \"object\": \"membrane_fluidity\",\n        \"description\": \"Homeoviscous\
    \ adaptation maintains membrane lipid viscosity/fluidity.\",\n        \"evidence\"\
    : [\n          {\n            \"reference\": \"DOI:10.1007/s42770-023-01057-4\"\
    ,\n            \"notes\": \"Homeoviscous adaptation regulates membrane lipid viscosity;\
    \ generic background mechanism for mesophilic temperature tolerance.\"\n     \
    \     }\n        ]\n      },\n      \"outcome\": \"qualified\",\n      \"judgment\"\
    : \"Lexical maintains has no predicate_id. Explicit remodeling process→fluidity\
    \ property is intelligible without importing RO roles; detailed efficacy unassessed.\"\
    \n    },\n    {\n      \"index\": 3,\n      \"field\": \"causal_graphs[0].edges[3]\"\
    ,\n      \"edge\": {\n        \"subject\": \"unsaturated_fatty_acid_fraction\"\
    ,\n        \"predicate\": \"increases\",\n        \"object\": \"membrane_fluidity\"\
    ,\n        \"description\": \"Increased unsaturated fatty acid fraction increases\
    \ membrane fluidity.\",\n        \"evidence\": [\n          {\n            \"\
    reference\": \"DOI:10.1007/s12275-023-00031-x\",\n            \"notes\": \"Higher\
    \ unsaturated content increases fluidity; canonical general bacterial thermoadaptation\
    \ mechanism.\"\n          }\n        ],\n        \"predicate_id\": \"RO:0002213\"\
    \n      },\n      \"outcome\": \"major\",\n      \"judgment\": \"RO2213 inherits\
    \ RO2211 process/process. Explicit fraction subject and fluidity QUALITY object\
    \ are not processes; object alone independently establishes violation even after\
    \ node5 is clarified.\"\n    },\n    {\n      \"index\": 4,\n      \"field\":\
    \ \"causal_graphs[0].edges[4]\",\n      \"edge\": {\n        \"subject\": \"hopanoids_sterol_like\"\
    ,\n        \"predicate\": \"regulates\",\n        \"object\": \"membrane_fluidity\"\
    ,\n        \"description\": \"Hopanoids / sterol-like molecules regulate membrane\
    \ fluidity.\",\n        \"evidence\": [\n          {\n            \"reference\"\
    : \"DOI:10.1007/s42770-023-01057-4\",\n            \"notes\": \"Hopanoids and\
    \ sterol-like molecules act as regulators of membrane fluidity; broad membrane-modulator\
    \ edge.\"\n          }\n        ],\n        \"predicate_id\": \"RO:0002211\"\n\
    \      },\n      \"outcome\": \"major\",\n      \"judgment\": \"RO2211 directly\
    \ requires process/process. Chemical subject and explicit fluidity QUALITY object\
    \ violate those roles; this persists independently of node5.\"\n    },\n    {\n\
    \      \"index\": 5,\n      \"field\": \"causal_graphs[0].edges[5]\",\n      \"\
    edge\": {\n        \"subject\": \"membrane_fluidity\",\n        \"predicate\"\
    : \"confers\",\n        \"object\": \"temperature_range_mid2_trait\",\n      \
    \  \"description\": \"Maintained membrane fluidity enables growth across the mid2\
    \ temperature range.\",\n        \"evidence\": [\n          {\n            \"\
    reference\": \"DOI:10.1146/annurev-micro-091313-103612\",\n            \"notes\"\
    : \"Functional membrane fluidity underlies homeoviscous adaptation supporting\
    \ the mesophile range.\"\n          }\n        ],\n        \"predicate_id\": \"\
    METPO:2007700\"\n      },\n      \"outcome\": \"qualified\",\n      \"judgment\"\
    : \"Local v8 confers admits QUALITY subject→TRAIT; no inherited RO2327 process-range\
    \ constraint. Numerical bridge and biological efficacy remain unassessed.\"\n\
    \    },\n    {\n      \"index\": 6,\n      \"field\": \"causal_graphs[0].edges[6]\"\
    ,\n      \"edge\": {\n        \"subject\": \"elevated_temperature\",\n       \
    \ \"predicate\": \"opens\",\n        \"object\": \"rna_thermometer\",\n      \
    \  \"description\": \"Elevated temperature melts/opens RNA thermometer 5′-UTR\
    \ secondary structure.\",\n        \"evidence\": [\n          {\n            \"\
    reference\": \"DOI:10.1007/s12551-025-01290-1\",\n            \"notes\": \"5′-UTR\
    \ secondary structures melt upon heat exposure, exposing ribosome binding sites;\
    \ broad review-level support.\"\n          }\n        ]\n      },\n      \"outcome\"\
    : \"qualified\",\n      \"judgment\": \"Lexical opens has no predicate_id. Current\
    \ temperature-increase event and RNA material object are documentary referents\
    \ only; no imported domain/range or detailed RNA efficacy claim.\"\n    },\n \
    \   {\n      \"index\": 7,\n      \"field\": \"causal_graphs[0].edges[7]\",\n\
    \      \"edge\": {\n        \"subject\": \"temperature_shift\",\n        \"predicate\"\
    : \"induces\",\n        \"object\": \"heat_shock_proteins\",\n        \"description\"\
    : \"Temperature shift / heat shock induces heat-shock proteins and chaperones.\"\
    ,\n        \"evidence\": [\n          {\n            \"reference\": \"DOI:10.1007/s12275-023-00031-x\"\
    ,\n            \"notes\": \"Temperature shifts induce heat- and cold-shock proteins;\
    \ high-confidence general stress-response edge.\"\n          }\n        ]\n  \
    \    },\n      \"outcome\": \"qualified\",\n      \"judgment\": \"Lexical induces\
    \ has no predicate_id. Temperature-change event and contextual protein aggregate\
    \ are not automatically invalid; detailed response efficacy unassessed.\"\n  \
    \  },\n    {\n      \"index\": 8,\n      \"field\": \"causal_graphs[0].edges[8]\"\
    ,\n      \"edge\": {\n        \"subject\": \"heat_shock_proteins\",\n        \"\
    predicate\": \"counteracts\",\n        \"object\": \"protein_denaturation\",\n\
    \        \"description\": \"Heat-shock proteins / chaperones counteract protein\
    \ denaturation and aggregation.\",\n        \"evidence\": [\n          {\n   \
    \         \"reference\": \"DOI:10.1007/s12275-023-00031-x\",\n            \"notes\"\
    : \"Chaperones counteract denaturation and aid tolerance; strong general proteostasis\
    \ edge.\"\n          }\n        ]\n      },\n      \"outcome\": \"qualified\"\
    ,\n      \"judgment\": \"Lexical counteracts has no predicate_id. Protein aggregate/process\
    \ endpoints and negative direction are intelligible; no detailed stress-defense\
    \ efficacy assessed.\"\n    },\n    {\n      \"index\": 9,\n      \"field\": \"\
    causal_graphs[0].edges[9]\",\n      \"edge\": {\n        \"subject\": \"baseline_mesophile_adaptation\"\
    ,\n        \"predicate\": \"characterizes\",\n        \"object\": \"mesophilic_organisms\"\
    ,\n        \"description\": \"Mesophilic organisms grow between ~20 °C and ~45\
    \ °C, bracketing the mid2 range.\",\n        \"evidence\": [\n          {\n  \
    \          \"reference\": \"DOI:10.1007/s42770-023-01057-4\",\n            \"\
    notes\": \"Mesophiles grow between room temperature (~20 °C) and ~45 °C; scope-defining\
    \ edge placing 27-30 °C within mesophily.\"\n          }\n        ]\n      },\n\
    \      \"outcome\": \"concern\",\n      \"judgment\": \"Lexical characterizes\
    \ has no imported role constraints. Organism-category type precision is node12\
    \ minor; description/note also explicitly embeds the ambient27–30 interval within\
    \ broader mesophile growth temperatures, conflicting with canonical width interpretation.\"\
    \n    }\n  ],\n  \"source\": [\n    {\n      \"index\": 0,\n      \"field\": \"\
    causal_graphs[0].edges[0]\",\n      \"subject\": \"baseline_mesophile_adaptation\"\
    ,\n      \"predicate\": \"confers\",\n      \"object\": \"temperature_range_mid2_trait\"\
    ,\n      \"description\": \"Baseline mesophile adaptation enables growth across\
    \ 27–30 °C.\",\n      \"references\": [\n        \"DOI:10.1146/annurev-micro-091313-103612\"\
    \n      ],\n      \"outcome\": \"unknown\",\n      \"assessment\": \"Generic membrane\
    \ remodeling supports context; exact baseline-mesophile bin mechanism unestablished.\
    \ Edge description participates in quantity conflict.\"\n    },\n    {\n     \
    \ \"index\": 1,\n      \"field\": \"causal_graphs[0].edges[1]\",\n      \"subject\"\
    : \"temperature_range_mid2_trait\",\n      \"predicate\": \"is a\",\n      \"\
    object\": \"temperature_range\",\n      \"description\": \"Temperature range mid2\
    \ is a quantitative bin of the temperature-range phenotype.\",\n      \"references\"\
    : [\n        \"DOI:10.1016/s0300-9629(97)00003-0\"\n      ],\n      \"outcome\"\
    : \"concern\",\n      \"assessment\": \"Supplied phrase is literal and explicitly\
    \ thermophile context; adjacent exact27–30 support note is a bounded attribution\
    \ concern. Formal hierarchy separate.\"\n    },\n    {\n      \"index\": 2,\n\
    \      \"field\": \"causal_graphs[0].edges[2]\",\n      \"subject\": \"homeoviscous_adaptation\"\
    ,\n      \"predicate\": \"maintains\",\n      \"object\": \"membrane_fluidity\"\
    ,\n      \"description\": \"Homeoviscous adaptation maintains membrane lipid viscosity/fluidity.\"\
    ,\n      \"references\": [\n        \"DOI:10.1007/s42770-023-01057-4\"\n     \
    \ ],\n      \"outcome\": \"partial_generic\",\n      \"assessment\": \"Ramón selected\
    \ phase/composition context supports generic membrane fluidity interpretation.\
    \ Detailed adaptive efficacy and exact-bin sufficiency unassessed.\"\n    },\n\
    \    {\n      \"index\": 3,\n      \"field\": \"causal_graphs[0].edges[3]\",\n\
    \      \"subject\": \"unsaturated_fatty_acid_fraction\",\n      \"predicate\"\
    : \"increases\",\n      \"object\": \"membrane_fluidity\",\n      \"description\"\
    : \"Increased unsaturated fatty acid fraction increases membrane fluidity.\",\n\
    \      \"references\": [\n        \"DOI:10.1007/s12275-023-00031-x\"\n      ],\n\
    \      \"outcome\": \"unknown_nearest_source\",\n      \"assessment\": \"Assigned\
    \ Moon identity only. Mendoza supplies independent generic UFA/fluidity context\
    \ but does not verify the detailed nearest-source/general thermoadaptation note.\"\
    \n    },\n    {\n      \"index\": 4,\n      \"field\": \"causal_graphs[0].edges[4]\"\
    ,\n      \"subject\": \"hopanoids_sterol_like\",\n      \"predicate\": \"regulates\"\
    ,\n      \"object\": \"membrane_fluidity\",\n      \"description\": \"Hopanoids\
    \ / sterol-like molecules regulate membrane fluidity.\",\n      \"references\"\
    : [\n        \"DOI:10.1007/s42770-023-01057-4\"\n      ],\n      \"outcome\":\
    \ \"supported_generic\",\n      \"assessment\": \"Ramón all-HTML row27 first two\
    \ sentences directly support hopanoid/sterol-like physical membrane effects and\
    \ phase modulation; no detailed adaptation intervention adopted.\"\n    },\n \
    \   {\n      \"index\": 5,\n      \"field\": \"causal_graphs[0].edges[5]\",\n\
    \      \"subject\": \"membrane_fluidity\",\n      \"predicate\": \"confers\",\n\
    \      \"object\": \"temperature_range_mid2_trait\",\n      \"description\": \"\
    Maintained membrane fluidity enables growth across the mid2 temperature range.\"\
    ,\n      \"references\": [\n        \"DOI:10.1146/annurev-micro-091313-103612\"\
    \n      ],\n      \"outcome\": \"unknown\",\n      \"assessment\": \"Generic functional\
    \ fluidity context does not establish the exact27–30 growth-bin mechanism; no\
    \ forced source falsehood.\"\n    },\n    {\n      \"index\": 6,\n      \"field\"\
    : \"causal_graphs[0].edges[6]\",\n      \"subject\": \"elevated_temperature\"\
    ,\n      \"predicate\": \"opens\",\n      \"object\": \"rna_thermometer\",\n \
    \     \"description\": \"Elevated temperature melts/opens RNA thermometer 5′-UTR\
    \ secondary structure.\",\n      \"references\": [\n        \"DOI:10.1007/s12551-025-01290-1\"\
    \n      ],\n      \"outcome\": \"UNASSESSED_SCOPE\",\n      \"assessment\": \"\
    New2025 review identity positive. Existing RNA opening/regulatory efficacy claim\
    \ deliberately unassessed; broad title not treated as citation mismatch.\"\n \
    \   },\n    {\n      \"index\": 7,\n      \"field\": \"causal_graphs[0].edges[7]\"\
    ,\n      \"subject\": \"temperature_shift\",\n      \"predicate\": \"induces\"\
    ,\n      \"object\": \"heat_shock_proteins\",\n      \"description\": \"Temperature\
    \ shift / heat shock induces heat-shock proteins and chaperones.\",\n      \"\
    references\": [\n        \"DOI:10.1007/s12275-023-00031-x\"\n      ],\n      \"\
    outcome\": \"UNASSESSED_SCOPE\",\n      \"assessment\": \"Moon identity only;\
    \ detailed induction/stress-regulation efficacy unassessed.\"\n    },\n    {\n\
    \      \"index\": 8,\n      \"field\": \"causal_graphs[0].edges[8]\",\n      \"\
    subject\": \"heat_shock_proteins\",\n      \"predicate\": \"counteracts\",\n \
    \     \"object\": \"protein_denaturation\",\n      \"description\": \"Heat-shock\
    \ proteins / chaperones counteract protein denaturation and aggregation.\",\n\
    \      \"references\": [\n        \"DOI:10.1007/s12275-023-00031-x\"\n      ],\n\
    \      \"outcome\": \"UNASSESSED_SCOPE\",\n      \"assessment\": \"Moon identity\
    \ only; detailed chaperone/proteostasis efficacy unassessed.\"\n    },\n    {\n\
    \      \"index\": 9,\n      \"field\": \"causal_graphs[0].edges[9]\",\n      \"\
    subject\": \"baseline_mesophile_adaptation\",\n      \"predicate\": \"characterizes\"\
    ,\n      \"object\": \"mesophilic_organisms\",\n      \"description\": \"Mesophilic\
    \ organisms grow between ~20 °C and ~45 °C, bracketing the mid2 range.\",\n  \
    \    \"references\": [\n        \"DOI:10.1007/s42770-023-01057-4\"\n      ],\n\
    \      \"outcome\": \"supported_generic_with_quantity_conflict\",\n      \"assessment\"\
    : \"Ramón row10 broad mesophile growth20–45 clause positive; bracketing27–30 ambient\
    \ values is distinct from canonical width28 and shares quantity conflict. No exact-alias\
    \ biological equivalence inferred.\"\n    }\n  ]\n}"
- assessment_id: owners
  area: ownership
  topic: 'Native checklist: exact canonical ledger and conditional predicate grounder'
  outcome: supported
  target_ids:
  - METPO:1000451
  summary: The exact SOURCES/TRANCHE canonical payload retains supported interval
    and width; coordinate quantity interpretation while preserving equality/no-op,
    nonempty rejection and global queue guards. Increases row 65 and regulates row
    11 can recreate incompatible roles in future empty fields; the consumer skips
    populated IDs, so replay is not current repair. Quantity and organism-category
    facet findings have only the current record as established faulty owner. Sibling
    writers remain qualified context.
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
  - METPO:1000451
  summary: Eleven embedded events comprise ten AI-assisted events and a seed. All
    25 current history projections are AI and use exact qualified prior whole readings,
    with zero new whole-history reads. Ignored- and hidden-inclusive search, excluding
    .git/.venv internals, has 188 matching paths and 68 matching arrays; all 93 actual
    local top-level review arrays have zero exact target. The append-only clarification
    corrects preliminary/frozen prose 67 without changing the manifest. Private/remote
    acceptance remains unknown.
  evidence_ids:
  - human-search
  - search-count-clarification
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
  - METPO:1000451
  summary: The original catalog contains 20 organisms and 28 datasets, with no exact
    Pseudomonas mangiferae species/strain key. Other Pseudomonas species are not substitutes,
    and no currently adopted B. subtilis/E. coli source passage establishes coverage.
    No module query was executed because the runner was unavailable within bounded
    discovery. No global absence, strain/module or efficacy result is inferred.
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
  - METPO:1000451
  summary: Three components with thirteen nodes and ten edges are permissible contextual
    NONMECHANISTIC structure. One aggregate protein class has an explicit REVIEWED_LABEL_ONLY
    rationale and zero instances; no artificial connector, accession or dataset is
    required. These structural positives do not resolve the six adjudicated findings.
  evidence_ids:
  - record
  - nodes-edges
  - expression
  - policy
- assessment_id: validation
  area: schema
  topic: 'Native checklist: current native checks and qualified B14 diagnostics'
  outcome: supported
  target_ids:
  - METPO:1000451
  summary: Current inspect, target validation, strict validation and snippet checks
    are successful B15 executions. Four original B14 common diagnostics are qualified
    for unchanged B15 inputs, not relabeled as fresh B15 executions. Original intervals,
    historical attempts, product skips and omitted full just test remain explicit.
    These eight command checks do not establish scientific correctness or human acceptance.
  evidence_ids:
  - capture
  - common-reuse-qualification
  - original-b14-common-completion
  - check-temperature-range-mid2-target-validate
  - check-temperature-range-mid2-target-strict
  - check-temperature-range-mid2-snippets-network
  - source-native
findings:
- finding_id: quantity-scope
  issue_key: temperature-range-mid2-quantity-scope
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Quantity scope
  description: The definition and graph use 27–30 °C as an absolute ambient growth
    interval, including edge9 placing it inside broader mesophile temperatures; the
    canonical note treats 27–30 degrees as an interval-width bin. Primary PMID31429815
    supports Pseudomonas mangiferae DMKU BBB3-04T growth at12–40 °C, and derived40−12=28
    is correct. Raw METPO supplies an existential generic numeric value in[27,30]
    without specifying endpoints versus width. Reconcile the quantity throughout the
    record and exact maintained canonical ledger while retaining the supported strain
    measurement, derived arithmetic and broad mesophile classification.
  target_ids:
  - METPO:1000451
  field_paths:
  - definition
  - canonical_examples[0].note
  - causal_graphs[0].description
  - causal_graphs[0].nodes[0].description
  - causal_graphs[0].edges[0].description
  - causal_graphs[0].edges[9].description
  - causal_graphs[0].edges[9].evidence[0].notes
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
    path: data/traits/environment/temperature_range_mid2.yaml
    role: Current record assertions; separate authorized curation required
  - repository: CultureBotAI/TraitMech
    path: scripts/backfill_canonical_examples_444.py
    role: Exact maintained source/TRANCHE payload and equality/rejection/global queue
      guards; coordinate quantity interpretation while preserving supported measurement
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: quantity-facet
  issue_key: temperature-range-mid2-quantity-facet
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Quantity facet
  description: The unsaturated_fatty_acid_fraction node explicitly denotes a proportion
    of unsaturated fatty acids in membrane phospholipids. CHEMICAL represents the
    material entities being counted, whereas the declared referent is a measurable
    compositional attribute. This changes the node meaning independently of the imported
    relation defects. No separate faulty exact writer was established in the bounded
    maintained-owner evidence.
  target_ids:
  - METPO:1000451
  field_paths:
  - causal_graphs[0].nodes[5].node_type
  evidence_ids:
  - record
  - nodes-edges
  - schema
  - local-authority
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_range_mid2.yaml
    role: Current record assertions; separate authorized curation required
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: imported-process-roles
  issue_key: temperature-range-mid2-imported-process-roles
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Imported process roles
  description: RO:0002213 inherits process-to-process roles from RO:0002211. Both
    edges target membrane fluidity, explicitly a quality; edge3 has an explicit fraction/proportion
    subject and edge4 has a chemical subject. Neither declared referent is a process.
    The object mismatch persists independently of correcting node5. Wildcard increases
    row65 and regulates row11 in the maintained mapping can recreate these assignments
    for future empty predicate_id fields; the consumer skips populated IDs, so ordinary
    replay does not repair the current fields.
  target_ids:
  - METPO:1000451
  field_paths:
  - causal_graphs[0].edges[3].predicate_id
  - causal_graphs[0].edges[4].predicate_id
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
    path: data/traits/environment/temperature_range_mid2.yaml
    role: Current record assertions; separate authorized curation required
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Wildcard closeMatch increases row 65 and regulates row 11 can recreate imported
      roles in future empty fields; coordinate formal referent support
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Conditional grounding consumer skips populated IDs; ordinary replay is not
      current-field repair
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: organism-category-facet
  issue_key: temperature-range-mid2-organism-category-facet
  category: representation
  severity: minor
  status: open
  certainty: confirmed
  title: Organism category facet
  description: The mesophilic_organisms node describes a category of organisms growing
    at moderate temperatures, but STATE is defined here as a bioenergetic or molecular
    state of the cell. The categorical intent remains legible. Clarify its representation
    without automatically imposing a replacement enum or adding a new taxon or mechanism.
  target_ids:
  - METPO:1000451
  field_paths:
  - causal_graphs[0].nodes[12].node_type
  evidence_ids:
  - record
  - nodes-edges
  - schema
  - local-authority
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_range_mid2.yaml
    role: Current record assertions; separate authorized curation required
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: bin-attribution
  issue_key: temperature-range-mid2-bin-attribution
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Bin attribution
  description: The Mendoza note attributes exact27–30 °C range support to a generic
    membrane-physics phrase. The Tolner note attributes that bin to a supplied phrase
    explicitly concerning high-temperature thermophiles. Both snippets are literal;
    these nearest inspected spans do not establish the adjacent numerical-bin claims.
    This is a bounded attribution finding without whole-paper absence, false-quotation
    or biological-refutation claims. The subclass relation has independent raw-ontology
    support.
  target_ids:
  - METPO:1000451
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
    path: data/traits/environment/temperature_range_mid2.yaml
    role: Current record assertions; separate authorized curation required
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: human-acceptance-link
  issue_key: temperature-range-mid2-human-acceptance-link
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Human acceptance link
  description: The record is REVIEWED, but its11 embedded events comprise10 AI-assisted
    events and the METPO seed. All25 current captured history actor projections are
    AI; whole bodies are exact qualified prior readings. The ignored- and hidden-inclusive
    bounded local search, excluding .git/.venv internals, found188 matching paths
    and68 matching review arrays; all93 actual local top-level target arrays contain
    zero exact target matches. These observations do not supply attributable human
    acceptance. Private or remote acceptance remains unknown.
  target_ids:
  - METPO:1000451
  field_paths:
  - mapping_status
  - curation_history
  evidence_ids:
  - human-search
  - search-count-clarification
  - histories
  - embedded-history
  - discovery
  - ground-reading
  - root-reading
  - root-verification
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_range_mid2.yaml
    role: Current record assertions; separate authorized curation required
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
actions:
- action_id: curate-quantity-scope
  description: In separately authorized curation, document the intended measured quantity
    and reconcile definition, graph and canonical membership with the exact backfill
    ledger.
  finding_ids:
  - quantity-scope
  target_ids:
  - METPO:1000451
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_range_mid2.yaml
    role: Current record assertions; separate authorized curation required
  - repository: CultureBotAI/TraitMech
    path: scripts/backfill_canonical_examples_444.py
    role: Exact maintained source/TRANCHE payload and equality/rejection/global queue
      guards; coordinate quantity interpretation while preserving supported measurement
  acceptance_checks:
  - Establish source-backed quantity and unit semantics without deriving endpoints
    or width solely from generic has-value.
  - Retain the strain-specific reported12–40 °C interval and derived width28; align
    all seven affected fields and preserve independently supported broad mesophile
    classification.
  - Coordinate SOURCES196–200/TRANCHE601–605 and equality, nonempty-rejection and
    global queue guards. The source measurement is positive; ordinary rerun does not
    repair semantics.
  - Use guarded curation/history, focused strict validation and applicable QC/products;
    regenerate affected products.
- action_id: curate-quantity-facet
  description: Represent the explicit fatty-acid proportion consistently with its
    measurable-attribute meaning.
  finding_ids:
  - quantity-facet
  target_ids:
  - METPO:1000451
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_range_mid2.yaml
    role: Current record assertions; separate authorized curation required
  acceptance_checks:
  - Retain the stated proportion as the referent; distinguish it from its constituent
    chemical entities.
  - Do not rename the node as material merely to hide the facet mismatch or invent
    biological intermediates.
  - Use guarded record/history curation and focused strict/graph validation; assess
    relation identifiers separately.
- action_id: curate-imported-process-roles
  description: Resolve the two relation identifiers against the retained referents
    and coordinate conditional mapping recurrence.
  finding_ids:
  - imported-process-roles
  target_ids:
  - METPO:1000451
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_range_mid2.yaml
    role: Current record assertions; separate authorized curation required
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Wildcard closeMatch increases row 65 and regulates row 11 can recreate imported
      roles in future empty fields; coordinate formal referent support
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Conditional grounding consumer skips populated IDs; ordinary replay is not
      current-field repair
  acceptance_checks:
  - Document subject/object referents and formal domain/range support for each of
    edges3 and4.
  - Preserve the proportion, fluidity quality and chemical facets; do not relabel
    solely to pass a check or invent mechanism intermediates.
  - Address both increases row65 and regulates row11 for future empty-field grounding;
    explicitly repair populated IDs through guarded curation.
  - Run focused strict validation, applicable graph/QC/products and meaningful grounding
    regression checks. No intervention or efficacy claim is prescribed.
- action_id: curate-organism-category-facet
  description: Clarify how the existing mesophile organism category is represented
    in this classification context.
  finding_ids:
  - organism-category-facet
  target_ids:
  - METPO:1000451
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_range_mid2.yaml
    role: Current record assertions; separate authorized curation required
  acceptance_checks:
  - Document the category meaning and distinguish it from the schema-defined molecular
    or bioenergetic STATE.
  - Choose a representation supported by the maintained schema without automatically
    prescribing another enum or adding unsupported organisms.
  - Retain source-backed generic classification and validate the separately curated
    record.
- action_id: curate-bin-attribution
  description: Qualify the two evidence notes to distinguish generic physical or thermophile
    context from exact numerical-bin authority.
  finding_ids:
  - bin-attribution
  target_ids:
  - METPO:1000451
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_range_mid2.yaml
    role: Current record assertions; separate authorized curation required
  acceptance_checks:
  - Describe the nearest inspected spans accurately; exact27–30 calibration needs
    identified support or remains qualified.
  - Retain all three literal snippets and the actual native three-VERIFIED result.
  - Preserve independently supported hierarchy; avoid whole-paper absence or biological-refutation
    claims and validate the separately curated record.
- action_id: curate-human-acceptance-link
  description: Link attributable human acceptance for REVIEWED status or accurately
    qualify the review state in separately authorized curation.
  finding_ids:
  - human-acceptance-link
  target_ids:
  - METPO:1000451
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/temperature_range_mid2.yaml
    role: Current record assertions; separate authorized curation required
  acceptance_checks:
  - Retain actor identity, exact scope and a retrievable acceptance reference; AI
    review and seed import do not establish human signoff.
  - Preserve bounded local-search limitations and private/remote uncertainty.
  - Use maintained guarded history and validation procedures for any curation change.
limitations:
- No fresh B15 common diagnostic execution is asserted. Full just test was NOT_RUN;
  only the five optional focused Stage2 tests are reused. Products retains 123 no-adapter
  skips and covers two configured mappings. Common checks establish bounded software/data
  integrity, not scientific support, current-target checks or prior-batch finalization.
  Serializers must append to these helper notes and limitations.
- Detailed stress-defense, regulatory adaptation, survival/fitness, molecular enhancement,
  cultivation optimization and intervention efficacy remain UNASSESSED_SCOPE; no operational
  repair proposed.
- Canonical source growth12–40 and derived width28 are positive; ambient27–30 versus
  width27–30 conflict is counted once. Generic ontology values are not assumed to
  choose the operationalization.
- Three snippets are literal; adjacent exact-bin note support is a separate bounded
  attribution concern. No whole-paper absence or biological refutation.
- Only selected original abstract/body clauses adopted; no full-body review claimed.
- Complete canonical abstract was displayed; cultivation, chemistry and other taxonomic
  comparisons were incidental and unadopted beyond named type strain/aliases and existing
  growth interval.
- Ramón term search displayed whole rows7/17/27, including detailed adaptation and
  a gene-target discussion. Only row17 first four physical sentences, row27 first
  two physical sentences and row10 mesophile classification clause adopted. No later
  numerical, gene or intervention text adopted.
- Tolner second indexed sentence includes wider transport/enzyme context; only explicit
  thermophile context and supplied literal fragment adopted.
- Moon and new2025 RNA-review work identity only; detailed RNA/stress/chaperone/proteostasis
  efficacy deliberately unassessed. Broad review title is not evidence of citation
  mismatch.
- No new current body acquisition. Reused publisher export is a historical tool response,
  not raw HTML; underlying cache fetch time unknown.
- Publication notice observations retain original request dates for reused sources.
  Null indexed notices do not establish exhaustive current absence.
- Broad mesophile growth20–45 classification does not establish exact optimum or exact-alias
  equivalence. Incidental named species outside selected clauses are not current source-organism
  evidence.
- Detailed temperature-response regulation, stress defense, fitness, efficacy and
  optimization are UNASSESSED_SCOPE.
- Generic numerical OWL restriction does not settle interval versus breadth; exact
  mesophilic alias equivalence remains unknown, not a separate finding.
- Baseline adaptation/repertoire description is mixed but not forced into an additional
  type finding.
- All25 current projections plus exactly qualified prior whole readings; no current
  whole-history claim.
- Uncaptured script/history discovery remains matching-line context; private/remote
  acceptance unknown.
- Ground auditor did not rerun common diagnostics, native checks or database hashing;
  root handles those separately. Source-specific findings remain separately adjudicated.
- Root adopted Ramón zero-based HTML p10 mesophile clause, p17 first four physical
  sentences and p27 first two physical sentences only; later numerical/gene/intervention
  text in displayed paragraphs is incidental and unadopted.
- Taxonomy initial DNS failure and successful retry retain separate observations;
  taxon identity alone does not establish phenotype.
- Ground frozen discovery scope says67 matching arrays; append-only count clarification
  and actual metadata establish68. All93 actual arrays were checked, with zero exact
  matches.
- Original B14 common diagnostics are qualified for unchanged B15 inputs, not fresh
  B15 executions. Current target inspect, target validation, strict validation and
  snippet checks are fresh B15 executions. The serializer common guard separately
  rechecks current inputs and five database pins.
- Full just test was not run; five focused Stage2 tests and product skips retain their
  original scope. Common software checks do not establish scientific correctness.
- Active exact METPO:1000451 identity and direct parent METPO:1000306 are positive.
  Historical Mesophilie retention is explicitly documented by active-review row105,
  release-delta row1273 and finalizer; biological exact equivalence to the unresolved
  quantity remains unknown.
- Homeoviscous adaptation METPO:1016200 is locally proposed v85, absent from the captured
  upstream raw OWL. Local v3 fluidity is a quality; broad v8 confers permits the current
  process/context and quality subjects with trait objects.
- Temperature increase and shift nodes describe actual events; the RNA thermometer
  structure is material RNA. Five lexical edges carry no invented RO/Biolink role
  constraints. Baseline adaptation/repertoire is mixed but not forced into an additional
  finding.
- Canonical primary metadata and official taxonomy support Pseudomonas mangiferae
  DMKU BBB3-04T, type aliases TBRC7080/JCM32061, reported12–40 °C and derived width28.
  Source optimum is separate and not adopted as the interval or width.
- Three components,13 nodes/10 edges and one explicitly reviewed label-only protein
  aggregate are permissible NONMECHANISTIC context; zero protein instances do not
  require invented connectors, accessions or datasets.
- The retained catalog contains20 organisms/28 datasets and no exact P.mangiferae
  species/strain entry. Other Pseudomonas species are not substitutes. No currently
  adopted B.subtilis/E.coli passage establishes source-species coverage. Bounded adapter
  discovery did not yield a runner; no module query or efficacy inference.
- Publication is separate from this local review. No scientific record, mapping, ontology,
  history, generated product or paid-provider run changes.
notes:
- Qualified reuse of four original B14 diagnostics is recorded in /private/tmp/traitmech-record-sweep-015.67f2ce7a/common-diagnostic-reuse-qualification.json.
  Historical products failures/retry and original cache provenance remain in /private/tmp/traitmech-record-sweep-014.q8m4v2cs/new-base-diagnostic-independent-review-agent/fresh-products-completion.json.
  B14 generated reports are retained output snapshots, not B15 source inputs or synthetic
  B15 reports. B15-to-B14 byte equality does not change the historical false B14-to-B13
  comparison; B14 final gates/commit and continuation pins remain separate.
- Final fields, categories, severities, owners and actions come only from actual root
  FINAL. The shared quantity conflict is counted once; independent quantity-facet
  and process-role majors plus three bounded minors remain separate. Representation
  is a permitted review-schema category, so no category remapping is applied.
- Serializer preparation adopts frozen audits and root adjudication and does not claim
  another whole-paper or whole-history review. Original canonical/source/catalog acquisitions,
  current RNA metadata/taxonomy/query times and copying/reading clocks remain distinct.
  The ground auditor did not repeat common/database checks; the serializer common
  guard separately verifies qualified current inputs. Original B14 diagnostics remain
  qualified history, not fresh B15 execution.
tags:
- record-review
- temperature-range-mid2
- environment
- needs-curation
```
