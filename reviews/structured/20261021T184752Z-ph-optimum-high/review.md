# Whole-record review of pH optimum high

- Review: 20261021T184752Z-ph-optimum-high
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-21T18:32:47.818575Z
- Finished UTC: 2026-10-21T18:47:52Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Needs curation: two majors address exact-synonym scope and imported regulation roles; three minors address concentration/gradient facets, omitted model attribution and bounded human acceptance. Active identity, parent and author canonical classification remain positive. Unavailable bodies and detailed biological mechanisms are not declared false.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: Eighth record of batch 010 in path order. Whole-target reading and successful 73-input capture precede substantive assessment. Fresh metadata acquisition preceded capture; interpretation followed it. Final source and grounding manifests, separate synonym and history supplements, independent challenge and root adjudication are pinned before serialization.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8eee04a8c65609fbaff6df7c54597dcaf1b9d282.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| METPO:1000458 | data/traits/environment/ph_optimum_high.yaml | maintained | pH optimum high |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full-corpus graph audit | passed | True | METPO:1000458 | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| Full-corpus snippet audit | passed | True | METPO:1000458 | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| Full-corpus pathway links | passed | True | METPO:1000458 | 19 links checked against the pinned PathwayMech snapshot. Target asserts no pathway context link. |
| Full-corpus history integrity | passed | True | METPO:1000458 | 1277 history records checked, zero invalid links at the 8eee source base; integrity does not establish science or human acceptance. |
| Initial full-product validation | failed | False | METPO:1000458 | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation with isolated local cache | failed | False | METPO:1000458 | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation after isolated-cache download | passed | True | METPO:1000458 | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| Focused native validation | passed | True | METPO:1000458 | Passed at 18:33:06–18:33:08 UTC on the unchanged target. |
| Focused strict validation | passed | True | METPO:1000458 | Passed at 18:33:06–18:33:09 UTC; schema validity is distinct from imported relation meaning. |
| Initial focused snippet attempt | failed | False | METPO:1000458 | Exit 2 at 18:33:06–18:33:21 UTC from DNS failure. Optional superseded access attempt; no source conclusion follows. |
| Focused snippet network retry | passed | True | METPO:1000458 | Passed at 18:33:50–18:33:54 UTC: six fields, one VERIFIED and five NOT_IN_ABSTRACT. Manual primary checking finds four literal Krulwich snippets and two Baker body-unverified snippets. |
| Reused corpus protein/taxon audit | passed | True | METPO:1000458 | Original B4 08:55:04–08:55:10 UTC pass with unchanged inputs; zero current protein instances, so no fresh target instance audit is claimed. |
| Reused maintained batch-nine QC | passed | True | METPO:1000458 | Original B9 17:05:16–17:06:53 UTC pass, qualified against current B10 bytes; not a new B10 final QC execution. |
| Protein-instance metadata applicability | not_applicable | False | METPO:1000458 | Five label-only classes and zero instances. NONMECHANISTIC context does not require a token accession. |

## Scientific And Domain Assessments

### Native checklist: active identity, definition and hierarchy

identity: supported. Targets: METPO:1000458.

Active METPO:1000458, parent 1000331 and explicit obsolete 0000180 replacement agree. Formal bounds are inclusive 8–14; approximately above 8 is retained as a convention limitation, not another finding.

### Native checklist: exact synonym versus numerical class

identity: concern. Targets: METPO:1000458.

Alkali Tolerant is faithfully inherited as EXACT, but the assigned primary classification includes optima below the numerical high bin. Shared context does not establish equal class membership. Only synonyms[0] is a confirmed finding; other aliases are not silently promoted to extra findings.

### Native checklist: quantitative class and generic graph context

scope: supported. Targets: METPO:1000458.

ENVIRONMENT, CLASS and NONMECHANISTIC are coherent. Five components, five contextual label-only classes and zero instances are permissible; generic context is not automatically a universal mechanism claim.

### Native checklist: named canonical classification and limits

evidence: unknown. Targets: METPO:1000458.

Official Bacillus aequororis species identity and the source classification of 5-DB as facultatively alkaliphilic are positive. Exact best-growth measurement remains limited by inspected primary scope; taxonomy and metabolic endpoints do not supply a new quantitative optimum.

### Native checklist: seven works and fourteen placements

evidence: supported. Targets: METPO:1000458.

All seven assigned DOI identities resolve, including Minerals through exact Crossref and official PDF. Each of fourteen placements is assessed on its actual available surface. Zero Europe PMC hits did not establish absence.

{
  "completed_at": "2026-10-21T18:37:37.984747+00:00",
  "target": "data/traits/environment/ph_optimum_high.yaml",
  "target_sha256": "7c60e5e61ddbde6b115fbe4be96386696385e87040fb5924daa6c7d4da12cf6f",
  "capture": {
    "path": "/private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high.inspect.json",
    "sha256": "48fbe8e34988118efca214d50616cf2581e09f221ae34e26000d1ad5e0df3fd9",
    "bytes": 14788
  },
  "capture_inputs": 73,
  "counts": {
    "works": 7,
    "literal_reference_forms": 7,
    "external_placements": 14,
    "ontology_source_placements": 0,
    "nodes": 15,
    "edges": 10,
    "snippets": 6,
    "exact_snippets": 4,
    "unverified_snippets": 2,
    "canonical_examples": 1
  },
  "source_only_findings": [
    {
      "severity": "minor",
      "area": "evidence",
      "field_paths": [
        "causal_graphs[0].edges[7].evidence[0].notes"
      ],
      "summary": "The note omits the model-organism attribution attached to the numerical efficiency examples in the cited Introduction.",
      "primary_locator": "Respiration JATS body paragraph 3, introductory comparison of Rhodobacter and Thermus model oxidases.",
      "qualification": "The source values are present as contextual examples, not established measurements in the focal C. thermarum study or every member of the aggregate class. This is documentary precision only; it does not assert false values, a universal biological contradiction or any corrected oxygen/fitness mechanism.",
      "suggested_action": "Retain source attribution/model scope or qualify the note as comparative context; no biological target, efficacy correction, new condition or protocol is proposed."
    }
  ],
  "source_only_major_candidates": [],
  "unassessed_biological_edge_indices": [
    7
  ],
  "summary": "Seven assigned DOI identities resolve, including Minerals via exact Crossref and official public PDF. Four short snippets are literal and two Baker phrases remain body-unverified. One bounded source minor concerns omitted model-organism attribution of efficiency examples at edge7 notes; detailed oxygen/fitness biology is unassessed. Canonical author classification and Minerals generic statements remain positive, with precise best-growth and unavailable AEM/Rnf/Baker scope limitations.",
  "qualifications": [
    "No exact biological mechanism or universal-bin claim is inferred merely from generic graph labels.",
    "The review does not infer wrong citation from the Rnf or Baker title alone.",
    "EPMC indexing absence and inaccessible body are not publication absence or false quotation.",
    "Original Krulwich07:57:33 acquisition, current root metadata18:30:12\u201313, new primary responses18:33:30\u201331 and Minerals PDF18:34:54\u201355 remain separate from current reading.",
    "Canonical exact quantitative optimum is not reconstructed from metabolic or resistance readouts."
  ]
}

### Native checklist: six assigned quotations

evidence: unknown. Targets: METPO:1000458.

Four Krulwich snippets are literal and two Baker phrases remain body-unverified. Native abstract checking found one verified and five nonmatches; body evidence explains the distinct manual result without implying false quotation from unavailable text.

{
  "completed_at": "2026-10-21T18:37:37.982675+00:00",
  "counts": {
    "total": 6,
    "exact_literal": 4,
    "unverified_body": 2
  },
  "snippets": [
    {
      "field_path": "evidence[0].snippet",
      "reference": "DOI:10.1038/nrmicro2549",
      "snippet": "alkaliphiles",
      "status": "EXACT_LITERAL",
      "basis": {
        "body": {
          "path": "/private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/krulwich-bioc.xml",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
          "bytes": 174908
        },
        "BioC_offsets": [
          "5466",
          "15130",
          "16479",
          "39232",
          "39253",
          "41582",
          "42119",
          "45597"
        ]
      }
    },
    {
      "field_path": "evidence[1].snippet",
      "reference": "DOI:10.1016/j.tim.2007.02.005",
      "snippet": "proton motive force",
      "status": "UNVERIFIED_BODY",
      "basis": {
        "metadata": {
          "path": "/private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/baker-metadata.json",
          "sha256": "e12f1b09a1467a8985fae8d345351ad5ef2fc532f35fb10be67203ec41ea939b",
          "bytes": 4065
        },
        "retained_failure": {
          "path": "/private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/prior-ph-delta-additional-primary-body-accesses-root.json",
          "sha256": "2b59f554309b38f437bff006507e7703ec541aca6057897b3651ae1c0af76355",
          "bytes": 840
        },
        "qualification": "Unknown body wording, not a false-quotation assertion."
      }
    },
    {
      "field_path": "causal_graphs[0].edges[0].evidence[0].snippet",
      "reference": "DOI:10.1038/nrmicro2549",
      "snippet": "alkaliphiles",
      "status": "EXACT_LITERAL",
      "basis": {
        "body": {
          "path": "/private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/krulwich-bioc.xml",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
          "bytes": 174908
        },
        "BioC_offsets": [
          "5466",
          "15130",
          "16479",
          "39232",
          "39253",
          "41582",
          "42119",
          "45597"
        ]
      }
    },
    {
      "field_path": "causal_graphs[0].edges[1].evidence[0].snippet",
      "reference": "DOI:10.1016/j.tim.2007.02.005",
      "snippet": "proton motive force",
      "status": "UNVERIFIED_BODY",
      "basis": {
        "metadata": {
          "path": "/private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/baker-metadata.json",
          "sha256": "e12f1b09a1467a8985fae8d345351ad5ef2fc532f35fb10be67203ec41ea939b",
          "bytes": 4065
        },
        "retained_failure": {
          "path": "/private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/prior-ph-delta-additional-primary-body-accesses-root.json",
          "sha256": "2b59f554309b38f437bff006507e7703ec541aca6057897b3651ae1c0af76355",
          "bytes": 840
        },
        "qualification": "Unknown body wording, not a false-quotation assertion."
      }
    },
    {
      "field_path": "causal_graphs[0].edges[2].evidence[0].snippet",
      "reference": "DOI:10.1038/nrmicro2549",
      "snippet": "alkaliphiles",
      "status": "EXACT_LITERAL",
      "basis": {
        "body": {
          "path": "/private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/krulwich-bioc.xml",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
          "bytes": 174908
        },
        "BioC_offsets": [
          "5466",
          "15130",
          "16479",
          "39232",
          "39253",
          "41582",
          "42119",
          "45597"
        ]
      }
    },
    {
      "field_path": "causal_graphs[0].edges[3].evidence[0].snippet",
      "reference": "DOI:10.1038/nrmicro2549",
      "snippet": "cytoplasmic pH",
      "status": "EXACT_LITERAL",
      "basis": {
        "body": {
          "path": "/private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/krulwich-bioc.xml",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
          "bytes": 174908
        },
        "BioC_offsets": [
          "58",
          "671",
          "2440",
          "3940",
          "4950",
          "7133",
          "7180",
          "7328"
        ]
      }
    }
  ]
}

### Native checklist: all fifteen current node referents

grounding: concern. Targets: METPO:1000458.

Sodium concentration at node 6 and electrochemical gradient at node 9 differ from the declared chemical/process facets. Their intended meanings are readable, supporting one bounded precision minor. PMF STATE and label-only proteins are otherwise permitted.

[
  {
    "index": 0,
    "field_path": "causal_graphs[0].nodes[0]",
    "node": {
      "node_id": "ph_optimum_high_trait",
      "label": "pH optimum high",
      "node_type": "TRAIT",
      "grounding": "METPO:1000458",
      "description": "pH optimum above ~8."
    },
    "assessment": "Active exact numerical high-optimum trait. Raw METPO restricts the optimum to inclusive 8\u201314; approximately-above-8 wording remains a boundary convention limitation, not a demonstrated strict exclusion at 8."
  },
  {
    "index": 1,
    "field_path": "causal_graphs[0].nodes[1]",
    "node": {
      "node_id": "ph_optimum",
      "label": "pH optimum",
      "node_type": "TRAIT",
      "grounding": "METPO:1000331",
      "description": "External pH supporting maximal growth."
    },
    "assessment": "Active exact parent pH-optimum trait; hierarchy is directly asserted in raw METPO."
  },
  {
    "index": 2,
    "field_path": "causal_graphs[0].nodes[2]",
    "node": {
      "node_id": "alkaline_external_ph",
      "label": "alkaline external pH",
      "node_type": "ENVIRONMENTAL_FACTOR",
      "description": "External pH &gt; ~8, typical of soda lakes and other alkaline habitats.",
      "grounding": "PATO:0001430"
    },
    "assessment": "Environmental alkaline condition, coherently grounded to active PATO alkaline quality as a condition facet. The PATO term does not independently establish the numeric optimum boundary."
  },
  {
    "index": 3,
    "field_path": "causal_graphs[0].nodes[3]",
    "node": {
      "node_id": "na_h_antiporters",
      "label": "Na+/H+ antiporters",
      "node_type": "GENE_OR_PROTEIN",
      "grounding_status": "REVIEWED_LABEL_ONLY",
      "grounding_notes": "Reviewed as a contextual protein or protein-complex label within a quantitative measurement graph; no exact semantic family term was established for this aggregate use.",
      "description": "Membrane antiporters importing H+ in exchange for Na+ to acidify the cytoplasm at high external pH."
    },
    "assessment": "Explicit material membrane antiporter aggregate; reviewed label-only contextual class is permissible. No accession or extra component is required. Detailed biological efficacy is not certified."
  },
  {
    "index": 4,
    "field_path": "causal_graphs[0].nodes[4]",
    "node": {
      "node_id": "alkaliphile_homeostasis",
      "label": "alkaliphile cytoplasmic pH homeostasis",
      "node_type": "BIOLOGICAL_PROCESS",
      "description": "Maintenance of a less alkaline cytoplasm than the external environment by proton re-import."
    },
    "assessment": "Homeostasis is an explicit biological process. Source scope and exact-bin sufficiency are assessed separately."
  },
  {
    "index": 5,
    "field_path": "causal_graphs[0].nodes[5]",
    "node": {
      "node_id": "cpa_nha_antiporters",
      "label": "CPA/Nha family Na+/H+ antiporters",
      "node_type": "GENE_OR_PROTEIN",
      "grounding_status": "REVIEWED_LABEL_ONLY",
      "grounding_notes": "Reviewed as a contextual protein or protein-complex label within a quantitative measurement graph; no exact semantic family term was established for this aggregate use.",
      "description": "Monovalent cation/proton antiporter family exporting Na+ and importing H+."
    },
    "assessment": "Explicit material CPA/Nha antiporter family; label-only class remains permissible. Its function does not make the represented material itself a process."
  },
  {
    "index": 6,
    "field_path": "causal_graphs[0].nodes[6]",
    "node": {
      "node_id": "intracellular_na",
      "label": "intracellular Na+ concentration",
      "node_type": "CHEMICAL",
      "description": "Cytoplasmic sodium ion concentration."
    },
    "assessment": "Both label and description denote intracellular sodium concentration, a measurable attribute, whereas CHEMICAL denotes an entity. Bounded facet precision issue; the readable concentration referent remains clear. This is not a false sodium identity or biological-efficacy assertion."
  },
  {
    "index": 7,
    "field_path": "causal_graphs[0].nodes[7]",
    "node": {
      "node_id": "trkah_k_uptake",
      "label": "TrkAH K+ uptake system",
      "node_type": "GENE_OR_PROTEIN",
      "grounding_status": "REVIEWED_LABEL_ONLY",
      "grounding_notes": "Reviewed as a contextual protein or protein-complex label within a quantitative measurement graph; no exact semantic family term was established for this aggregate use.",
      "description": "Potassium uptake transport system aiding membrane potential and pH homeostasis."
    },
    "assessment": "Explicit material uptake-system aggregate. Label-only status has documentary support from maintained policy; no exact family accession is fabricated."
  },
  {
    "index": 8,
    "field_path": "causal_graphs[0].nodes[8]",
    "node": {
      "node_id": "rnf_complex",
      "label": "Rnf complex",
      "node_type": "GENE_OR_PROTEIN",
      "grounding_status": "REVIEWED_LABEL_ONLY",
      "grounding_notes": "Reviewed as a contextual protein or protein-complex label within a quantitative measurement graph; no exact semantic family term was established for this aggregate use.",
      "description": "Ferredoxin:NAD oxidoreductase that pumps Na+ to build a transmembrane Na+ gradient."
    },
    "assessment": "Explicit material Rnf complex, not merely an activity label. Biological details are outside the grounding assessment."
  },
  {
    "index": 9,
    "field_path": "causal_graphs[0].nodes[9]",
    "node": {
      "node_id": "transmembrane_na_gradient",
      "label": "transmembrane Na+ gradient",
      "node_type": "BIOLOGICAL_PROCESS",
      "description": "Electrochemical sodium ion gradient across the membrane."
    },
    "assessment": "Label and description denote an electrochemical sodium gradient, not its establishment. Native STATE explicitly separates a gradient from generating processes; BIOLOGICAL_PROCESS therefore needs bounded facet clarification. No additional Biolink hard range error follows."
  },
  {
    "index": 10,
    "field_path": "causal_graphs[0].nodes[10]",
    "node": {
      "node_id": "terminal_oxidases",
      "label": "branched respiratory chain terminal oxidases",
      "node_type": "GENE_OR_PROTEIN",
      "grounding_status": "REVIEWED_LABEL_ONLY",
      "grounding_notes": "Reviewed as a contextual protein or protein-complex label within a quantitative measurement graph; no exact semantic family term was established for this aggregate use.",
      "description": "Terminal oxidases (aa3/ba3/bb3) that pump protons with differing efficiencies."
    },
    "assessment": "Explicit material terminal-oxidase aggregate; no exact enzyme-family or subunit grounding is imposed."
  },
  {
    "index": 11,
    "field_path": "causal_graphs[0].nodes[11]",
    "node": {
      "node_id": "proton_motive_force",
      "label": "proton motive force",
      "node_type": "STATE",
      "description": "Electrochemical proton gradient powering bioenergetics.",
      "grounding": "METPO:1007500"
    },
    "assessment": "Explicit electrochemical proton-gradient STATE. Local v3 authority and maintained node-type migration agree; current local produces gate deliberately permits this state object."
  },
  {
    "index": 12,
    "field_path": "causal_graphs[0].nodes[12]",
    "node": {
      "node_id": "acidic_membrane_polymers",
      "label": "acidic plasma membrane polymers",
      "node_type": "CHEMICAL",
      "description": "Acidic cell-envelope polymers (teichuronopeptide, peptidoglycan, teichuronic acid)."
    },
    "assessment": "Chemical aggregate of acidic cell-envelope polymers; composition and effect are source questions, not decided by this declared chemical facet."
  },
  {
    "index": 13,
    "field_path": "causal_graphs[0].nodes[13]",
    "node": {
      "node_id": "organic_acid_secretion",
      "label": "organic acid secretion",
      "node_type": "BIOLOGICAL_PROCESS",
      "description": "Secretion of metabolic organic acids that helps counter alkaline stress."
    },
    "assessment": "Organic-acid secretion is an explicit process; detailed physiological efficacy is not certified."
  },
  {
    "index": 14,
    "field_path": "causal_graphs[0].nodes[14]",
    "node": {
      "node_id": "ph_balance",
      "label": "pH balance",
      "node_type": "BIOLOGICAL_PROCESS",
      "description": "Maintenance of cytoplasmic pH balance under alkaline stress."
    },
    "assessment": "pH balance is described as maintenance, an explicit process rather than the numeric pH value."
  }
]

### Native checklist: all ten relation meanings

consistency: concern. Targets: METPO:1000458.

Only edges 1 and 4 are confirmed imported-role errors: material antiporter classes occupy process-regulator roles, and edge 4 targets concentration. Edge 9 process endpoints fit. Local row 2 explicitly permits STATE for edge 7; older v9 prose alone does not negate maintained clarification. Biolink formal endpoints remain broad.

[
  {
    "index": 0,
    "field_path": "causal_graphs[0].edges[0]",
    "subject": "alkaline_external_ph",
    "predicate": "selects for",
    "predicate_id": "METPO:2007401",
    "object": "alkaliphile_homeostasis",
    "formal_status": "qualified_adaptation_context",
    "assessment": "Local v2 selects-for has broad causal-node endpoints and an evolutionary adaptation meaning. The process can name an adaptive physiological trait in this context; distinguish selection from immediate homeostatic response without inventing a hard domain exclusion.",
    "biological_scope": "Formal/documentary roles only. Detailed pathogen defense, fitness, acid tolerance, AMR and intervention efficacy remain UNASSESSED_SCOPE; no pathway reconstruction or optimization."
  },
  {
    "index": 1,
    "field_path": "causal_graphs[0].edges[1]",
    "subject": "na_h_antiporters",
    "predicate": "regulates",
    "predicate_id": "RO:0002211",
    "object": "alkaliphile_homeostasis",
    "formal_status": "confirmed_imported_role_mismatch",
    "assessment": "RO:0002211 requires process endpoints. The subject explicitly names material membrane antiporters, while the object is homeostasis process. Functional context does not silently substitute antiporter activity for the declared material.",
    "biological_scope": "Formal/documentary roles only. Detailed pathogen defense, fitness, acid tolerance, AMR and intervention efficacy remain UNASSESSED_SCOPE; no pathway reconstruction or optimization."
  },
  {
    "index": 2,
    "field_path": "causal_graphs[0].edges[2]",
    "subject": "alkaliphile_homeostasis",
    "predicate": "confers",
    "predicate_id": "METPO:2007700",
    "object": "ph_optimum_high_trait",
    "formal_status": "local_roles_compatible",
    "assessment": "Local v8 confers explicitly permits biological processes as subjects and TRAIT objects. Generic homeostasis context and exact numeric-bin sufficiency remain source-limited; role compatibility is not empirical proof of the bin.",
    "biological_scope": "Formal/documentary roles only. Detailed pathogen defense, fitness, acid tolerance, AMR and intervention efficacy remain UNASSESSED_SCOPE; no pathway reconstruction or optimization."
  },
  {
    "index": 3,
    "field_path": "causal_graphs[0].edges[3]",
    "subject": "ph_optimum_high_trait",
    "predicate": "is a",
    "predicate_id": "rdfs:subClassOf",
    "object": "ph_optimum",
    "formal_status": "hierarchy_supported",
    "assessment": "TRAIT-to-parent rdfs:subClassOf agrees with the direct upstream hierarchy. Literature snippets alone are not used as a formal hierarchy authority.",
    "biological_scope": "Formal/documentary roles only. Detailed pathogen defense, fitness, acid tolerance, AMR and intervention efficacy remain UNASSESSED_SCOPE; no pathway reconstruction or optimization."
  },
  {
    "index": 4,
    "field_path": "causal_graphs[0].edges[4]",
    "subject": "cpa_nha_antiporters",
    "predicate": "decreases",
    "predicate_id": "RO:0002212",
    "object": "intracellular_na",
    "formal_status": "confirmed_imported_role_mismatch",
    "assessment": "RO:0002212 inherits process-to-process roles from RO:0002211. Current subject is the material CPA/Nha family; object is intracellular sodium concentration represented as CHEMICAL. Neither the material nor concentration denotes the regulated process. The object facet is separately bounded wording precision.",
    "biological_scope": "Formal/documentary roles only. Detailed pathogen defense, fitness, acid tolerance, AMR and intervention efficacy remain UNASSESSED_SCOPE; no pathway reconstruction or optimization."
  },
  {
    "index": 5,
    "field_path": "causal_graphs[0].edges[5]",
    "subject": "trkah_k_uptake",
    "predicate": "maintains",
    "predicate_id": null,
    "object": "alkaliphile_homeostasis",
    "formal_status": "free_predicate_no_invented_constraint",
    "assessment": "Maintains is a free predicate without imported identifier. No mandatory external ID or arbitrary formal role restriction is imposed; physiological support is source-audited separately.",
    "biological_scope": "Formal/documentary roles only. Detailed pathogen defense, fitness, acid tolerance, AMR and intervention efficacy remain UNASSESSED_SCOPE; no pathway reconstruction or optimization."
  },
  {
    "index": 6,
    "field_path": "causal_graphs[0].edges[6]",
    "subject": "rnf_complex",
    "predicate": "generates",
    "predicate_id": "biolink:produces",
    "object": "transmembrane_na_gradient",
    "formal_status": "biolink_material_subject_compatible",
    "assessment": "Rnf material complex satisfies Biolink produces textual material-producer meaning. Formal inherited endpoints are broad named things, so no hard material-only product range is inferred for a gradient. Node 9 process-versus-state wording is a separate bounded issue.",
    "biological_scope": "Formal/documentary roles only. Detailed pathogen defense, fitness, acid tolerance, AMR and intervention efficacy remain UNASSESSED_SCOPE; no pathway reconstruction or optimization."
  },
  {
    "index": 7,
    "field_path": "causal_graphs[0].edges[7]",
    "subject": "terminal_oxidases",
    "predicate": "produces",
    "predicate_id": "METPO:2007800",
    "object": "proton_motive_force",
    "formal_status": "maintained_local_authority_allows_state",
    "assessment": "The older v9 proposed definition says chemical output, but maintained mapping row 2 explicitly adds STATE for this exact terminal-oxidases\u2192PMF edge, with #392/#393 histories explaining agent generation of a gradient. Formal proposed endpoints are broad causal nodes. This is a draft/maintained-authority qualification, not a confirmed record-role defect.",
    "biological_scope": "Formal/documentary roles only. Detailed pathogen defense, fitness, acid tolerance, AMR and intervention efficacy remain UNASSESSED_SCOPE; no pathway reconstruction or optimization."
  },
  {
    "index": 8,
    "field_path": "causal_graphs[0].edges[8]",
    "subject": "acidic_membrane_polymers",
    "predicate": "enhances",
    "predicate_id": null,
    "object": "proton_motive_force",
    "formal_status": "free_predicate_no_invented_constraint",
    "assessment": "Enhances is an ungrounded local predicate. Chemical aggregate to PMF state is not ruled out by an invented imported role constraint; no biological mechanism or intervention validation is claimed.",
    "biological_scope": "Formal/documentary roles only. Detailed pathogen defense, fitness, acid tolerance, AMR and intervention efficacy remain UNASSESSED_SCOPE; no pathway reconstruction or optimization."
  },
  {
    "index": 9,
    "field_path": "causal_graphs[0].edges[9]",
    "subject": "organic_acid_secretion",
    "predicate": "regulates",
    "predicate_id": "RO:0002211",
    "object": "ph_balance",
    "formal_status": "external_roles_compatible",
    "assessment": "RO:0002211 process-to-process endpoints fit organic-acid secretion and pH-balance maintenance. Formal compatibility does not validate detailed efficacy or universal applicability.",
    "biological_scope": "Formal/documentary roles only. Detailed pathogen defense, fitness, acid tolerance, AMR and intervention efficacy remain UNASSESSED_SCOPE; no pathway reconstruction or optimization."
  }
]

### Native checklist: attribution and biological scope

evidence: concern. Targets: METPO:1000458.

Edge 7 notes omit named model-organism attribution from numerical examples. The values are present and no new canonical measurements are asserted. Generic Minerals/homeostasis context is positive; detailed pathogen defense, oxygen/hypoxia, fitness, ROS, AMR and intervention mechanisms remain UNASSESSED_SCOPE.

### Native checklist: whole record and optional fields

completeness: supported. Targets: METPO:1000458.

All fifteen nodes, ten edges, five components, five label-only proteins, zero instances, one canonical and sixteen events are covered. No arbitrary protein, connector or dataset requirement is imposed.

### Native checklist: canonical catalog applicability

scope: not_applicable. Targets: METPO:1000458.

No focal Bacillus aequororis or verified type-alias match in the retained complete 20-organism/28-dataset catalog. Bacillus subtilis is a different species and was not substituted; no downstream defense query was made.

### Native checklist: maintained recurrence and clarification

ownership: supported. Targets: METPO:1000458.

Rows 11/61 can refill empty relation IDs while the grounder skips nonempty IDs. Row 2 and node-type migration support PMF STATE. Exact legacy-CURIE migration does not blindly rewrite a current local placeholder; shared history leads are not automatic target owners.

{
  "assessed_at": "2026-10-21T18:37:15.120293+00:00",
  "target": "data/traits/environment/ph_optimum_high.yaml",
  "counts": {
    "nodes": 15,
    "edges": 10,
    "components": 5,
    "protein_classes": 5,
    "label_only_proteins": 5,
    "protein_instances": 0,
    "canonical_examples": 1,
    "history_events": 16,
    "ai_events": 15,
    "seed_events": 1,
    "captured_history_files": 5,
    "matching_files": 238,
    "review_target_arrays": 68,
    "exact_target_arrays": 0
  },
  "search_basis": "Ignored/hidden-inclusive exact target slug, hyphenated slug, label, both ID forms, related synonym and all exact synonyms. Search and parsed target arrays retained in full. All-node owner/history discovery independently confirms five captured histories.",
  "whole_histories_read": [
    "history/infrastructure/inconsistent-node-type/2026-08-12T000912Z-claude-code-779670.yaml",
    "history/infrastructure/node-type-consistency/2026-08-15T014631Z-claude-code-9d7f4d.yaml",
    "history/infrastructure/pathway-vs-process/2026-08-16T010630Z-claude-code-192557.yaml",
    "history/infrastructure/predicate-gate-audit/2026-08-16T074719Z-claude-code-84d88d.yaml",
    "history/other/canonical-examples-six/2026-08-21T065406Z-codex-a1ab82.yaml"
  ],
  "reading_scope": "All five captured histories fully read after successful capture. They document AI infrastructure maintenance and canonical backfill, not attributable human scientific approval. No full scientific review of parent/sibling records is claimed.",
  "current_history": "Sixteen events comprise fifteen explicitly AI-assisted events and one seed event. REVIEWED is not itself a linked human acceptance decision.",
  "owners": [
    {
      "path": "data/traits/environment/ph_optimum_high.yaml",
      "role": "Maintained target; record-level corrections require separately authorized curation."
    },
    {
      "path": "mappings/predicate_grounding.tsv",
      "role": "Rows 11 and 61 can refill RO2211/2212 without type gates if identifiers are empty. Row 2 deliberately admits STATE for edge 7, so it is positive maintained authority, not a recurrence defect there."
    },
    {
      "path": "scripts/ground_causal_predicates.py",
      "role": "Lines 152\u2013180 skip nonempty predicate IDs and apply table gates only during initial filling; no automatic overwrite claim."
    },
    {
      "path": "scripts/migrate_node_type_consistency.py",
      "role": "Lines 52\u201368 preserve PMF as the gradient state, not its establishment."
    },
    {
      "path": "scripts/migrate_remaining_microbe_domain_edges.py",
      "role": "Lines 57\u201387 perform exact legacy-CURIE migration; a current placeholder edge is not blindly re-migrated."
    },
    {
      "path": "proposals/metpo_traitmech_v9/metpo_proposal_properties_robot.tsv",
      "role": "Older chemical-output prose should be interpreted alongside maintained row 2 and the explicit histories; do not declare current edge 7 invalid by selecting only the narrower draft."
    }
  ],
  "research_scope": "Current captured research is provenance and a lead, not direct literature evidence or proof of the exact historical report bytes. Shared-node scripts are contextual leads, not automatically target writers.",
  "human_traceability": "No exact target review array or attributable acceptance link was found in the stated local scope. Remote/private decisions remain unknown."
}

### Native checklist: bounded local acceptance traceability

provenance: concern. Targets: METPO:1000458.

Ignored-inclusive search found 238 paths, 68 parsed actual review arrays and zero exact target arrays. Sixteen record events comprise 15 AI events plus seed. Five captured histories were fully read and have AI actors; the separate singular-target correction preserves this basis. No linked human acceptance was found within these local bounds.

### Native checklist: focused passes and qualified common reuse

schema: supported. Targets: METPO:1000458.

Native and strict checks passed; focused snippets passed after a retained DNS attempt. All 73 inputs match. Initial uv-cache failure preceded successful inspect and was not a completed-review validation failure. Historical common/B4/B9 checks retain actual times, failures, retries, baselines and skips.

## Findings

### exact-tolerance-synonym: Exact tolerance synonym does not match the numerical optimum class

major / open / confirmed; issue key: ph-optimum-high-exact-tolerance-synonym.

The assigned primary classification includes alkali-tolerant optima below the inclusive 8–14 high bin, so Alkali Tolerant cannot be assumed extensionally equivalent to that whole class. Raw METPO supplies the same EXACT synonym: this is inherited semantic scope, not a local transcription mistake. The cited convention is not imposed universally on other publications.

### imported-regulation-roles: Material antiporter classes occupy imported process-regulator roles

major / open / confirmed; issue key: ph-optimum-high-imported-regulation-roles.

RO:0002211 requires process endpoints and RO:0002212 inherits those roles. Both current subjects at edges 1 and 4 explicitly denote material antiporter classes; edge 4 also targets concentration rather than a regulated process. Native structural validity does not resolve these declared-referent conflicts.

### concentration-gradient-facets: Concentration and gradient nodes have imprecise declared facets

minor / open / confirmed; issue key: ph-optimum-high-concentration-gradient-facets.

Node 6 explicitly denotes sodium concentration while its CHEMICAL type denotes an entity. Node 9 explicitly denotes an electrochemical gradient while BIOLOGICAL_PROCESS denotes a process and native STATE distinguishes a gradient from its establishment. The intended referents are clear; this is one bounded precision issue, without additional biological or predicate findings.

### model-attribution: Numerical examples omit their model-organism attribution

minor / open / confirmed; issue key: ph-optimum-high-model-attribution.

The assigned respiration Introduction attributes its numerical examples to named model organisms. Edge 7 notes omit that attribution, although the values are present and the record does not explicitly claim new measurements in the canonical organism. This is source precision only; detailed oxygen/fitness biology remains unassessed.

### human-acceptance-link: Local provenance lacks a linked human acceptance decision

minor / open / confirmed; issue key: ph-optimum-high-human-acceptance-link.

REVIEWED and AI maintenance do not identify attributable human acceptance. The bounded ignored-inclusive 238-path/68-array/zero-exact search, sixteen record events and five AI histories preserve positive maintenance while leaving remote/private decisions unknown. The target-projection correction is separately retained.

## Recommended Actions And Acceptance Checks

### reconcile-synonym-scope

During separately authorized curation, reconcile or qualify the inherited exact synonym against the numerical class and cited convention.

- Preserve upstream METPO provenance and the active numerical identity; do not characterize faithful import as local transcription error.
- Document the authority or scope behind exact equivalence without imposing one publication convention universally.
- Use guarded history and applicable identity, native, strict and QC checks; retain this immutable review and add a successor after changed inputs.

### reconcile-regulation-roles

Reconcile the two confirmed imported-role fields with their current declared referents during authorized curation.

- Verify the actual inherited process roles and incident relations; distinguish a material class from activity without constructing a repaired biological route.
- Review mapping refill behavior and nonempty-ID skips, preserving valid edge 9 and the explicit STATE allowance for local edge 7.
- Use guarded history and applicable native, strict, mapping and QC checks; no scientific source data are modified by this review.

### clarify-node-facets

Clarify concentration and gradient representation while preserving the current intended referents.

- Choose a documented native facet consistent with the intended quantity or state; no blanket enum replacement is prescribed.
- Reassess incident edges and guarded writer recurrence; do not add token proteins, connectors or mechanisms.
- Use guarded record/repository history and applicable native, strict and QC checks.

### retain-model-attribution

Qualify the existing numerical note with the source model attribution during authorized curation.

- Keep the values as attributed comparative context rather than asserting canonical measurements or universal efficacy.
- Do not supply an oxygen/fitness intervention, altered condition or repaired biological mechanism.
- Recheck the exact citation/quotation and applicable native, strict and evidence checks.

### link-human-acceptance

Link existing attributable human acceptance if available, or clarify status while retaining the bounded absence result.

- Preserve the 238-path/68-array/zero-exact search and distinguish sixteen record events from five fully read history records.
- Retain the projection correction; do not infer acceptance from AI work, ontology authorship or passing checks.
- No contact with another person or automatic status promotion is authorized by this proposed action.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| check-audit-graphs | /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; metadata audit-graphs.json | context_only | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| check-audit-snippets | /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; metadata audit-snippets.json | context_only | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| check-check-pathway-links | /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; metadata check-pathway-links.json | context_only | 19 links checked against the pinned PathwayMech snapshot. Target asserts no pathway context link. |
| check-validate-history | /private/tmp/traitmech-record-sweep-003.4opxlhgf/validate-history.log; Executed 2026-10-21T07:03:25Z through 2026-10-21T07:03:30Z; metadata validate-history.json | context_only | 1277 history records checked, zero invalid links at the 8eee source base; integrity does not establish science or human acceptance. |
| check-validate-products | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log; Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; metadata validate-products.json | context_only | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| check-validate-products-retry-local | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log; Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; metadata validate-products-retry-local.json | context_only | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| check-validate-products-retry-network | /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log; Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; metadata validate-products-retry-network.json | context_only | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| check-ph-optimum-high-validate | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-validate.log; Executed 2026-10-21T18:33:06.978537+00:00 through 2026-10-21T18:33:08.842892+00:00; metadata ph-optimum-high-validate.json | context_only | Passed at 18:33:06–18:33:08 UTC on the unchanged target. |
| check-ph-optimum-high-strict | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-strict.log; Executed 2026-10-21T18:33:06.957926+00:00 through 2026-10-21T18:33:09.667095+00:00; metadata ph-optimum-high-strict.json | context_only | Passed at 18:33:06–18:33:09 UTC; schema validity is distinct from imported relation meaning. |
| check-ph-optimum-high-snippets | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-snippets.log; Executed 2026-10-21T18:33:06.952290+00:00 through 2026-10-21T18:33:21.235005+00:00; metadata ph-optimum-high-snippets.json | context_only | Exit 2 at 18:33:06–18:33:21 UTC from DNS failure. Optional superseded access attempt; no source conclusion follows. |
| check-ph-optimum-high-snippets-network-retry | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-snippets-network-retry.log; Executed 2026-10-21T18:33:50.683403+00:00 through 2026-10-21T18:33:54.213249+00:00; metadata ph-optimum-high-snippets-network-retry.json | context_only | Passed at 18:33:50–18:33:54 UTC: six fields, one VERIFIED and five NOT_IN_ABSTRACT. Manual primary checking finds four literal Krulwich snippets and two Baker body-unverified snippets. |
| check-corpus-protein-taxa | /private/tmp/traitmech-record-sweep-004.f7_g5r4w/corpus-protein-taxa.log; Executed 2026-10-21T08:55:04Z through 2026-10-21T08:55:10Z; metadata corpus-protein-taxa.json | context_only | Original B4 08:55:04–08:55:10 UTC pass with unchanged inputs; zero current protein instances, so no fresh target instance audit is claimed. |
| check-batch009-qc | /private/tmp/traitmech-record-sweep-009.x21w9b3v/batch009-qc.log; Executed 2026-10-21T17:05:16Z through 2026-10-21T17:06:53Z; metadata batch009-qc.json | context_only | Original B9 17:05:16–17:06:53 UTC pass, qualified against current B10 bytes; not a new B10 final QC execution. |
| record | data/traits/environment/ph_optimum_high.yaml; Entire current target | supports | Fifteen nodes, ten edges, five components, five label-only protein classes, zero instances, one canonical and sixteen record events are covered. |
| checklist | .claude/skills/curate-yaml-record/references/review-checklist.md; Captured maintained policy | supports | Whole-record identity, source, graph, optional fields, ownership, provenance and readiness checklist. |
| policy | docs/GROUNDING_POLICY.md; Captured maintained policy | supports | Preserve actual referents and permitted functional facets; no token protein or connectivity requirement. |
| native-types | src/traitmech/schema/traitmech.yaml; Captured maintained policy | supports | Chemical entities, concentration attributes, states and processes are distinct representational facets. |
| human-policy | docs/CURATION_PLAYBOOK.md; Captured maintained policy | supports | AI maintenance and REVIEWED do not identify attributable human scientific acceptance. |
| reuse | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/common-reuse-b9-qc-supplement-qualified.json; Qualified B10 comparison and original B9 gates | supports | All 1,130 traits, 1,278 history files and nineteen common inputs match. Original timestamps, baselines, failures, retries and skips remain explicit. |
| capture | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-grounding-agent/final-capture-verification.json; Derived assessment or read receipt; primary acquisition is separately recorded | supports | All 73 current captured input hashes match. |
| identity | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-grounding-agent/identity-assessment.json; Derived assessment or read receipt; primary acquisition is separately recorded | supports | Active exact identity, direct parent and explicit obsolete replacement agree. Faithful synonym import is distinct from scientific equivalence. |
| node-edges | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-grounding-agent/node-edge-ledger.json; Derived assessment or read receipt; primary acquisition is separately recorded | supports | All fifteen nodes and ten edges; firm imported-role fields are edges 1 and 4, with two bounded node-facet issues. |
| owners | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-grounding-agent/owner-provenance-assessment.json; Derived assessment or read receipt; primary acquisition is separately recorded | supports | Exact maintained rows and writers, five fully read histories and bounded 238-path/68-array/zero-exact target search. |
| expression | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-grounding-agent/expression-applicability.json; Derived assessment or read receipt; primary acquisition is separately recorded | supports | No focal species/type-alias catalog match; no substitute species or downstream defense query. |
| authority-reuse | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-grounding-agent/authority-reuse-receipts.json; Derived assessment or read receipt; primary acquisition is separately recorded | supports | Original PATO and catalog access times remain distinct from current byte copies and reading. |
| local-authority | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-grounding-agent/local-authority-excerpts.json; Derived assessment or read receipt; primary acquisition is separately recorded | supports | Actual v2/v3/v8/v9 authorities and broad Biolink endpoints, read together with maintained mapping clarifications. |
| selected-ro | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-grounding-agent/selected-ro-primary-reading.json; Derived assessment or read receipt; primary acquisition is separately recorded | supports | Actual RO statements and inherited process roles; primary database hash is separate from query-receipt hash. |
| ground-manifest | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-grounding-agent/evidence-manifest.json; Derived assessment or read receipt; primary acquisition is separately recorded | supports | Twenty-three frozen grounding artifacts. |
| history-addendum | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-grounding-agent/history-target-projection-addendum.json; Derived assessment or read receipt; primary acquisition is separately recorded | supports | Corrects a plural-key history projection to actual singular targets. Five original AI actor inventories and scientific conclusions are unchanged. |
| metpo-primary | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/repo/data/raw/metpo.owl; METPO:1000458, direct parent 1000331, obsolete 0000180 and nested numerical restriction | supports | Active identity and parent agree; obsolete 0000180 explicitly links to the active term. The pinned class uses inclusive 8–14 and supplies the same exact synonym. Upstream import does not independently establish scientific equivalence. |
| ro-primary | /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/ro.db; RO:0002211 process domain/range; RO:0002212 inherits regulates | supports | Material antiporter subjects conflict with the process regulator role. The concentration object at edge 4 is also not a process. The secretion and maintenance processes at edge 9 fit these endpoint roles. |
| biolink-primary | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/repo/data/raw/biolink-model.yaml; produces textual material-producer description; inherited named-thing endpoints | supports | The material Rnf subject is compatible. Broad formal endpoints do not impose a material-only product range; no additional formal error is assigned to edge 6. |
| taxonomy-primary | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-grounding-agent/taxon1463663.xml; Official NCBITaxon:1463663 species identity and type aliases | supports | Bacillus aequororis identity is positive. Species taxonomy and the source isolate 5-DB remain distinct scopes; no exact optimum measurement is inferred from taxonomy. |
| pato-primary | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-grounding-agent/pato0001430.response; Official retained PATO:0001430 alkaline response | supports | The alkaline-quality facet is coherent; it does not by itself calibrate the exact numerical optimum bin. |
| meta-krulwich | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-root/krulwich-metadata.json; Europe PMC title/abstract/status surface for DOI:10.1038/nrmicro2549 | supports | Assigned bibliographic identity and returned abstract only. Selected body observations have separate evidence and acquisition times. |
| meta-baker | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-root/baker-metadata.json; Europe PMC title/abstract/status surface for DOI:10.1016/j.tim.2007.02.005 | supports | Assigned bibliographic identity and returned abstract only. Selected body observations have separate evidence and acquisition times. |
| meta-aem | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-root/aem-metadata.json; Europe PMC title/abstract/status surface for DOI:10.1128/AEM.00145-24 | supports | Assigned bibliographic identity and returned abstract only. Selected body observations have separate evidence and acquisition times. |
| meta-rnf | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-root/rnf-metadata.json; Europe PMC title/abstract/status surface for DOI:10.1515/hsz-2015-0137 | supports | Assigned bibliographic identity and returned abstract only. Selected body observations have separate evidence and acquisition times. |
| meta-respiration | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-root/respiration-metadata.json; Europe PMC title/abstract/status surface for DOI:10.3389/fmicb.2024.1468929 | supports | Assigned bibliographic identity and returned abstract only. Selected body observations have separate evidence and acquisition times. |
| meta-minerals | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-root/minerals-metadata.json; Europe PMC title/abstract/status surface for DOI:10.3390/min14090861 | context_only | Zero indexed hits are retained without inferring publication absence; exact Crossref and official PDF are separately bound. |
| meta-canonical | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-root/canonical-metadata.json; Europe PMC title/abstract/status surface for DOI:10.1155/2024/3087296 | supports | Assigned bibliographic identity and returned abstract only. Selected body observations have separate evidence and acquisition times. |
| body-krulwich | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/krulwich-bioc.xml; Retained BioC; selected generic passages and literal snippets | supports | Generic pH-homeostasis context and four short literal phrases; no detailed pathogen mechanism assessment or claim of universal exact-bin calibration. |
| body-canonical | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/canonical.xml; Introduction body paragraphs 0/3/4 and selected conclusion | supports | The author classification of 5-DB as a facultative alkaliphile is positive; exact best-growth measurement remains limited in the inspected scope. |
| body-respiration | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/respiration.xml; Introduction body paragraph 3; documentary attribution only | supports | Numerical examples are attributed to named model organisms. Values are present; the current note omits their model attribution. Detailed oxygen/fitness biology remains unassessed. |
| minerals-crossref | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/minerals-crossref.json; Exact DOI registration metadata | supports | Exact Minerals DOI and publication identity resolve independently of Europe PMC indexing. |
| synonym-primary | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/canonical.xml; Introduction body paragraph 0: stated tolerant versus alkaliphilic optimum conventions | refutes | The stated tolerance category includes optima below the numerical high bin, challenging exact synonym equivalence. This source convention is not imposed as a universal physiological classification. |
| body-minerals | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/minerals-public-cdn.pdf; Official PDF page 6, section 2.5; extracted lines 275–285 | supports | Existing generic polymer and organic-acid wording is present. This source check does not independently certify structural or detailed mechanistic interpretation. |
| sources | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/source-assessment.json; Derived assessment or read receipt; primary acquisition is separately recorded | supports | Frozen source-placement subset and one attribution minor; separate synonym assessment is appended without rewriting this subset. |
| source-ledger | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/source-ledger.json; Derived assessment or read receipt; primary acquisition is separately recorded | supports | Seven exact assigned identities; metadata, selected body scope and unavailable body limits remain distinct. |
| placements | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/placement-ledger.json; Derived assessment or read receipt; primary acquisition is separately recorded | supports | All fourteen external placements covered. |
| snippets | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/snippet-ledger.json; Derived assessment or read receipt; primary acquisition is separately recorded | supports | Four literal Krulwich phrases and two Baker body-unverified phrases; no false-absence claim. |
| node-sources | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/node-source-ledger.json; Derived assessment or read receipt; primary acquisition is separately recorded | supports | Every current node source facet covered with scope qualifications. |
| edge-sources | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/edge-source-ledger.json; Derived assessment or read receipt; primary acquisition is separately recorded | supports | All ten edges; documentary attribution at edge 7 is separate from unassessed detailed oxygen/fitness biology. |
| source-status | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/publication-status-ledger.json; Derived assessment or read receipt; primary acquisition is separately recorded | supports | Returned notice fields and exact Crossref metadata only; no exhaustive global notice search claimed. |
| source-reading | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/selected-primary-reading.json; Derived assessment or read receipt; primary acquisition is separately recorded | supports | Actual selected primary passages and metadata abstracts read, not entire articles. |
| source-access | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/access-limitations.json; Derived assessment or read receipt; primary acquisition is separately recorded | supports | Baker, AEM and Rnf body limitations remain unknown; a zero-byte Rnf HTML response is not a PDF body. |
| source-manifest | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/evidence-manifest.json; Derived assessment or read receipt; primary acquisition is separately recorded | supports | Thirty-six frozen source artifacts. |
| body-reuse | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/reuse-and-copy-receipt.json; Derived assessment or read receipt; primary acquisition is separately recorded | supports | Krulwich original 07:57:33 acquisition remains separate from current copies and reading. |
| native-checks | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/native-check-context.json; Derived assessment or read receipt; primary acquisition is separately recorded | supports | Initial uv-cache failure and snippet DNS failure are separate from successful inspect and focused retry. |
| canonical-source | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/canonical-assessment.json; Derived assessment or read receipt; primary acquisition is separately recorded | supports | Named author classification is positive; exact growth-optimum measurement is not reconstructed from metabolic or resistance endpoints. |
| synonym-supplement | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/synonym-scope-supplement.json; Derived assessment or read receipt; primary acquisition is separately recorded | supports | Append-only assessment outside the original placement subset: exact tolerance synonym conflicts with numerical-bin equivalence, while faithful upstream import is retained. |
| pdf-extraction | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/pdf-extraction-receipt.json; Derived assessment or read receipt; primary acquisition is separately recorded | supports | Local PDF extraction has its own input/output hashes; the primary evidence reference retains the PDF hash. |
| root-reading-37 | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-root/whole-target-preinspect-reading.json; Derived assessment or read receipt; primary acquisition is separately recorded | supports | Only the actual scope and chronology recorded in this root reading receipt; no later or full-body reading inferred. |
| root-reading-38 | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-root/primary-ro-reading.json; Derived assessment or read receipt; primary acquisition is separately recorded | supports | Only the actual scope and chronology recorded in this root reading receipt; no later or full-body reading inferred. |
| root-reading-39 | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-root/frozen-ledger-root-reading.json; Derived assessment or read receipt; primary acquisition is separately recorded | supports | Only the actual scope and chronology recorded in this root reading receipt; no later or full-body reading inferred. |
| root-reading-40 | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-root/primary-owner-root-reading.json; Derived assessment or read receipt; primary acquisition is separately recorded | supports | Only the actual scope and chronology recorded in this root reading receipt; no later or full-body reading inferred. |
| root-reading-41 | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-root/initial-primary-root-reading.json; Derived assessment or read receipt; primary acquisition is separately recorded | supports | Only the actual scope and chronology recorded in this root reading receipt; no later or full-body reading inferred. |
| root-synonym-supplement | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-root/synonym-supplement-reading.json; Derived assessment or read receipt; primary acquisition is separately recorded | supports | Root verified the later append-only synonym supplement and its eight bindings; final finding counts did not change. |
| initial-inspect-failure | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high.inspect-failed-retention.json; Retained initial failed uv launch and exact relocated stdout/stderr/command bytes | context_only | The initial default-cache launch failed before the native helper. Successful isolated-cache inspect followed; this is an optional superseded orchestration failure, not completed-review validation or serialization failure. |
| challenge | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-semantic-challenge-agent/semantic-severity-challenge.json; Final independent semantic review and verified bindings | supports | Independent disposition and qualifications; detailed biological efficacy is not certified. |
| adjudication | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-root-adjudication.json; Final root adjudication and verified bindings | supports | Final disposition governs five findings, preserving separate supplements and source limits. |

## Limits And Additional Notes

- Detailed pathogen defense, oxygen/hypoxia, fitness, ROS, AMR and intervention biology remains UNASSESSED_SCOPE. The respiration review checks literal numerical attribution only; no mechanism repair or optimization is supplied.
- The exact-synonym concern is inherited from pinned METPO. The cited physiological classification is a stated convention, not a universal rule; other aliases are not added findings.
- Formal METPO bounds are inclusive 8–14. Approximately above 8 does not unequivocally exclude 8, so that wording is a precision limitation rather than a separate defect.
- The canonical author classification of 5-DB is positive. Exact best-growth measurement is not reconstructed from taxonomy, metabolic or resistance endpoints.
- Two Baker snippets remain body-unverified; AEM and Rnf body scopes are limited. A zero-byte HTML response with a PDF filename is not article text. Titles, indexing absence and access failures alone do not establish wrong citations or false biology.
- Older v9 chemical-product prose is read together with explicit maintained row 2 STATE allowance and migration history. No automatic formal-role finding is assigned to edge 7. Biolink formal endpoints remain broad; free predicates have no invented imported restrictions.
- Original Krulwich 07:57:33, root metadata 18:30:12–18:30:13, fresh JATS/Crossref 18:33:30–18:33:31 and Minerals PDF 18:34:54–18:34:55 acquisition times remain separate from current copying and selected reading. No full-article reading is claimed.
- The initial uv-cache inspect launch and initial snippet DNS failure are retained separately from successful inspect and focused retry. They are not completed-review validation or serializer failures.
- The local ignored-inclusive search cannot establish absence of remote/private acceptance. All five history records were fully read by the grounding auditor; root read two. The separate singular-target projection addendum corrects a documentary extraction without changing original actor counts.
- Five components, five label-only protein classes and zero instances are permissible. No token accession, substitute species or downstream defense-expression query is required.
- Final disposition: two major findings, three minor findings, fourteen assessments and five linked proposed actions.
- Coverage: 73 captured inputs, 23 frozen grounding artifacts plus separate history correction, 36 frozen source artifacts plus separate synonym supplement, fifteen nodes, ten edges, five components, five label-only protein classes, zero instances, one canonical and sixteen record events. Seven works, fourteen placements and six snippets retain exact source scope.
- Serializer is single-use and guarded. Root owns one execution, native review validation and save after independent reading. Preparation does not alter scientific records, state or Git.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T184752Z-ph-optimum-high
kind: record
repository: CultureBotAI/TraitMech
title: Whole-record review of pH optimum high
started_at: '2026-10-21T18:32:47.818575Z'
finished_at: '2026-10-21T18:47:52Z'
reviewer:
  identity: codex
  kind: agent
  independence: independent
  independence_basis: Separate source and grounding audits, independent semantic challenge
    and root selected-primary reading support the disposition. Generic environmental
    classification, documentary attribution and formal roles are assessed. Detailed
    pathogen defense, oxygen/hypoxia, fitness, ROS, AMR and intervention biology remains
    unassessed; no scientific record was edited.
  model: GPT-6 (Codex)
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'Needs curation: two majors address exact-synonym scope and imported regulation
  roles; three minors address concentration/gradient facets, omitted model attribution
  and bounded human acceptance. Active identity, parent and author canonical classification
  remain positive. Unavailable bodies and detailed biological mechanisms are not declared
  false.'
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
  - path: data/traits/environment/ph_optimum.yaml
    sha256: 55981325e7e0e85fa5e1f52fc04cbc6de77b981783685c4bdab25e8bab26cfc4
    role: context
  - path: data/traits/environment/ph_optimum_high.yaml
    sha256: 7c60e5e61ddbde6b115fbe4be96386696385e87040fb5924daa6c7d4da12cf6f
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
  - path: history/infrastructure/inconsistent-node-type/2026-08-12T000912Z-claude-code-779670.yaml
    sha256: adb240d907348b52784c5e2f2e4b131af124877eeaaf1805c94713342763e5dd
    role: context
  - path: history/infrastructure/node-type-consistency/2026-08-15T014631Z-claude-code-9d7f4d.yaml
    sha256: 21f19561c0d4769e7acc62e05e41d0d395a0f239938f00829f79f2b9c3ac2510
    role: context
  - path: history/infrastructure/pathway-vs-process/2026-08-16T010630Z-claude-code-192557.yaml
    sha256: a45fff0e3ef24effb20c3b624dc14a6cab08f2094bc0f8033cd709c0cd60f012
    role: context
  - path: history/infrastructure/predicate-gate-audit/2026-08-16T074719Z-claude-code-84d88d.yaml
    sha256: d1ba848e155dbd3a65905f07af5539d3d22b8873b638cc6adb48b1a0e23c0a3d
    role: context
  - path: history/other/canonical-examples-six/2026-08-21T065406Z-codex-a1ab82.yaml
    sha256: 23be5f6ab519511e3e23feffa85813eec4fa3c7e6b900e77fd4a3adc0c26da0e
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
  - path: research/traits/environment/ph_optimum_high-deep-research-falcon.md
    sha256: b353291406e3a7a3f129d7e3cd57e6631340732330e0395117120ac6a11207fe
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
  - path: scripts/audit_uniprot_grounding.py
    sha256: 91eb2165c69b3a4fcb53154dc8c835ac1070577f88065a43dfc881284d3d1052
    role: context
  - path: scripts/backfill_canonical_examples_444.py
    sha256: 18ca0766789c239d693ef665e8b1d43c1209a0f414a326f1c5d890f88de7b20c
    role: context
  - path: scripts/connect_ph_delta_mid3_graph_183.py
    sha256: cf65890b2797032dcf9d2fa7b249a47cfe710501b3b2d8f610f323c6f27366e4
    role: context
  - path: scripts/connect_ph_phenotype_graph_183.py
    sha256: 7d13d108660bede28937d3f180e90c542c47869c10f34ca497f9ab6f8f5db4ba
    role: context
  - path: scripts/connect_phototrophy_graphs_183.py
    sha256: afdea1c107faa1d90b7f91adef4084cda801b8b60d139067e3796ab7b92c1fdc
    role: context
  - path: scripts/document_evidence_reference_churn.py
    sha256: 84f8638faa59e3909cdde0ccf2efbdf98521c8c423367fa78c139726ea545669
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
  - path: scripts/match_uniprot_to_proteins.py
    sha256: 7e953637d4221b021995cae93c55abfd6757ac85e83b35ade02962082d5adf37
    role: context
  - path: scripts/migrate_disposition_typing.py
    sha256: ebafdd145fc0729d32f3b8a45f570d97a8e001838afadd698e2b246cb8950714
    role: context
  - path: scripts/migrate_enables_range_edges.py
    sha256: 3d0d1bddcaa76baef5833973e2e979e4fee1f834c67d1abcc69a8d866ecb8f32
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
  - path: scripts/retype_causal_nodes.py
    sha256: c7eb961c1b04cd4b31635331003f432f889567282c4650adc4f1151f715417ab
    role: context
  - path: scripts/review_ph_delta_mid3_graph_183.py
    sha256: 47d0d2b09f3acce565d9779443d8a5ee6784989ae34c23c6f0875f74ad4a1532
    role: context
  - path: scripts/review_ph_phenotype_graph_183.py
    sha256: 651b46611c5e630e4db00f8d7525378ddb3a9f552c83e7f53387d14ab95dd2e2
    role: context
  - path: scripts/review_ph_range_mid2_graph_183.py
    sha256: 2788c907439099c64cbc25c50b973e5ac0d2b93bc07ff7ed89e4cddaae500bd3
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
- target_id: METPO:1000458
  path: data/traits/environment/ph_optimum_high.yaml
  label: pH optimum high
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_optimum_high.yaml
    role: Maintained target; read-only review.
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Predicate recurrence input.
  - repository: CultureBotAI/TraitMech
    path: mappings/node_grounding.tsv
    role: Node grounding context.
  record_class: TraitRecord
scope:
  description: One entire maintained TraitRecord. Contextual ontology, source, parent,
    writer and history inputs are not additional review targets.
  selection: Eighth record of batch 010 in path order. Whole-target reading and successful
    73-input capture precede substantive assessment. Fresh metadata acquisition preceded
    capture; interpretation followed it. Final source and grounding manifests, separate
    synonym and history supplements, independent challenge and root adjudication are
    pinned before serialization.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - METPO:1000458
checks:
- check_id: audit-graphs
  name: Full-corpus graph audit
  status: passed
  required: true
  target_ids:
  - METPO:1000458
  command: just audit-graphs --out /private/tmp/traitmech-record-sweep.FU79Gr/causal_graph_audit.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  evidence_ids:
  - check-audit-graphs
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    010 qualified byte comparison confirms all history, trait and common validation
    inputs unchanged. Other commands ran at f25; the Git delta to 8eee contains only
    seven added workflow/skill/infrastructure-history files. Original timestamps,
    failures and skips are retained; these are reused results, not new executions
    or certification against later ontology releases.
- check_id: audit-snippets
  name: Full-corpus snippet audit
  status: passed
  required: true
  target_ids:
  - METPO:1000458
  command: just audit-snippets --report /private/tmp/traitmech-record-sweep.FU79Gr/evidence_snippet_audit.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  evidence_ids:
  - check-audit-snippets
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    010 qualified byte comparison confirms all history, trait and common validation
    inputs unchanged. Other commands ran at f25; the Git delta to 8eee contains only
    seven added workflow/skill/infrastructure-history files. Original timestamps,
    failures and skips are retained; these are reused results, not new executions
    or certification against later ontology releases.
- check_id: check-pathway-links
  name: Full-corpus pathway links
  status: passed
  required: true
  target_ids:
  - METPO:1000458
  command: just check-pathway-links
  exit_code: 0
  expected_exit_code: 0
  summary: 19 links checked against the pinned PathwayMech snapshot. Target asserts
    no pathway context link.
  evidence_ids:
  - check-check-pathway-links
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    010 qualified byte comparison confirms all history, trait and common validation
    inputs unchanged. Other commands ran at f25; the Git delta to 8eee contains only
    seven added workflow/skill/infrastructure-history files. Original timestamps,
    failures and skips are retained; these are reused results, not new executions
    or certification against later ontology releases.
- check_id: validate-history
  name: Full-corpus history integrity
  status: passed
  required: true
  target_ids:
  - METPO:1000458
  command: just validate-history
  exit_code: 0
  expected_exit_code: 0
  summary: 1277 history records checked, zero invalid links at the 8eee source base;
    integrity does not establish science or human acceptance.
  evidence_ids:
  - check-validate-history
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    010 qualified byte comparison confirms all history, trait and common validation
    inputs unchanged. Other commands ran at f25; the Git delta to 8eee contains only
    seven added workflow/skill/infrastructure-history files. Original timestamps,
    failures and skips are retained; these are reused results, not new executions
    or certification against later ontology releases.
- check_id: validate-products
  name: Initial full-product validation
  status: failed
  required: false
  target_ids:
  - METPO:1000458
  command: just validate-products
  exit_code: 2
  expected_exit_code: 0
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  evidence_ids:
  - check-validate-products
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    010 qualified byte comparison confirms all history, trait and common validation
    inputs unchanged. Other commands ran at f25; the Git delta to 8eee contains only
    seven added workflow/skill/infrastructure-history files. Original timestamps,
    failures and skips are retained; these are reused results, not new executions
    or certification against later ontology releases.
- check_id: validate-products-retry-local
  name: Product validation with isolated local cache
  status: failed
  required: false
  target_ids:
  - METPO:1000458
  command: just validate-products
  exit_code: 2
  expected_exit_code: 0
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  evidence_ids:
  - check-validate-products-retry-local
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    010 qualified byte comparison confirms all history, trait and common validation
    inputs unchanged. Other commands ran at f25; the Git delta to 8eee contains only
    seven added workflow/skill/infrastructure-history files. Original timestamps,
    failures and skips are retained; these are reused results, not new executions
    or certification against later ontology releases.
- check_id: validate-products-retry-network
  name: Product validation after isolated-cache download
  status: passed
  required: true
  target_ids:
  - METPO:1000458
  command: just validate-products
  exit_code: 0
  expected_exit_code: 0
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  evidence_ids:
  - check-validate-products-retry-network
  scope_note: History validation ran in batch 003 at the same 8eee source base; batch
    010 qualified byte comparison confirms all history, trait and common validation
    inputs unchanged. Other commands ran at f25; the Git delta to 8eee contains only
    seven added workflow/skill/infrastructure-history files. Original timestamps,
    failures and skips are retained; these are reused results, not new executions
    or certification against later ontology releases.
- check_id: ph-optimum-high-validate
  name: Focused native validation
  status: passed
  required: true
  target_ids:
  - METPO:1000458
  command: just validate data/traits/environment/ph_optimum_high.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Passed at 18:33:06–18:33:08 UTC on the unchanged target.
  evidence_ids:
  - check-ph-optimum-high-validate
- check_id: ph-optimum-high-strict
  name: Focused strict validation
  status: passed
  required: true
  target_ids:
  - METPO:1000458
  command: just validate-strict data/traits/environment/ph_optimum_high.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Passed at 18:33:06–18:33:09 UTC; schema validity is distinct from imported
    relation meaning.
  evidence_ids:
  - check-ph-optimum-high-strict
- check_id: ph-optimum-high-snippets
  name: Initial focused snippet attempt
  status: failed
  required: false
  target_ids:
  - METPO:1000458
  command: just verify-snippets --record data/traits/environment/ph_optimum_high.yaml
    --out /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-snippets.tsv
  exit_code: 2
  expected_exit_code: 0
  summary: Exit 2 at 18:33:06–18:33:21 UTC from DNS failure. Optional superseded access
    attempt; no source conclusion follows.
  evidence_ids:
  - check-ph-optimum-high-snippets
- check_id: ph-optimum-high-snippets-network-retry
  name: Focused snippet network retry
  status: passed
  required: true
  target_ids:
  - METPO:1000458
  command: just verify-snippets --record data/traits/environment/ph_optimum_high.yaml
    --out /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-snippets-network-retry.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 'Passed at 18:33:50–18:33:54 UTC: six fields, one VERIFIED and five NOT_IN_ABSTRACT.
    Manual primary checking finds four literal Krulwich snippets and two Baker body-unverified
    snippets.'
  evidence_ids:
  - check-ph-optimum-high-snippets-network-retry
- check_id: corpus-protein-taxa
  name: Reused corpus protein/taxon audit
  status: passed
  required: true
  target_ids:
  - METPO:1000458
  command: just audit-graph-protein-taxa --out /private/tmp/traitmech-record-sweep-004.f7_g5r4w/corpus-protein-taxa.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: Original B4 08:55:04–08:55:10 UTC pass with unchanged inputs; zero current
    protein instances, so no fresh target instance audit is claimed.
  evidence_ids:
  - check-corpus-protein-taxa
- check_id: batch009-qc
  name: Reused maintained batch-nine QC
  status: passed
  required: true
  target_ids:
  - METPO:1000458
  command: just qc
  exit_code: 0
  expected_exit_code: 0
  summary: Original B9 17:05:16–17:06:53 UTC pass, qualified against current B10 bytes;
    not a new B10 final QC execution.
  evidence_ids:
  - check-batch009-qc
- check_id: uniprot-applicability
  name: Protein-instance metadata applicability
  status: not_applicable
  required: false
  target_ids:
  - METPO:1000458
  summary: Five label-only classes and zero instances. NONMECHANISTIC context does
    not require a token accession.
  evidence_ids:
  - record
  - policy
  - node-edges
evidence:
- evidence_id: check-audit-graphs
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; metadata audit-graphs.json
  accessed_at: '2026-10-21T18:47:52Z'
  support: context_only
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  snapshot_sha256: ecce27e6a8f8b8b1fc54a9a0564a27626ee33774da508665859c6d1429337f4d
- evidence_id: check-audit-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; metadata audit-snippets.json
  accessed_at: '2026-10-21T18:47:52Z'
  support: context_only
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  snapshot_sha256: beafaa5c82645f5cf216142b6e0369d556202bcc72fdabbf35825fce955fd59f
- evidence_id: check-check-pathway-links
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; metadata check-pathway-links.json
  accessed_at: '2026-10-21T18:47:52Z'
  support: context_only
  summary: 19 links checked against the pinned PathwayMech snapshot. Target asserts
    no pathway context link.
  snapshot_sha256: e77729b8afd6ae02cd834e516c48dd5c72d10498802e7a1b0004eebb4831f6a0
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-003.4opxlhgf/validate-history.log
  locator: Executed 2026-10-21T07:03:25Z through 2026-10-21T07:03:30Z; metadata validate-history.json
  accessed_at: '2026-10-21T18:47:52Z'
  support: context_only
  summary: 1277 history records checked, zero invalid links at the 8eee source base;
    integrity does not establish science or human acceptance.
  snapshot_sha256: 02f94872992b2fbc3cc455c552d56a338dd449a315e02b1bf0226b68a8d2cfe3
- evidence_id: check-validate-products
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; metadata validate-products.json
  accessed_at: '2026-10-21T18:47:52Z'
  support: context_only
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  snapshot_sha256: 697efcbe603c9a5e27f9726e688d1b9d9f621fa548f585d9005b5157d81dadae
- evidence_id: check-validate-products-retry-local
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log
  locator: Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; metadata validate-products-retry-local.json
  accessed_at: '2026-10-21T18:47:52Z'
  support: context_only
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  snapshot_sha256: b636ab6978cf8b8d4cc2cc4033f1cdca399cca46dc615a26073cfe680d44ebb5
- evidence_id: check-validate-products-retry-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log
  locator: Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; metadata validate-products-retry-network.json
  accessed_at: '2026-10-21T18:47:52Z'
  support: context_only
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  snapshot_sha256: 67e91252adce1d441ad6b37d6904f0cbcea703575aec8011e65e94822fa810ea
- evidence_id: check-ph-optimum-high-validate
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-validate.log
  locator: Executed 2026-10-21T18:33:06.978537+00:00 through 2026-10-21T18:33:08.842892+00:00;
    metadata ph-optimum-high-validate.json
  accessed_at: '2026-10-21T18:47:52Z'
  support: context_only
  summary: Passed at 18:33:06–18:33:08 UTC on the unchanged target.
  snapshot_sha256: 7068d72f8242e2e36f4888b58185f30d7c0567946de6376a0921f955b1c54c74
- evidence_id: check-ph-optimum-high-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-strict.log
  locator: Executed 2026-10-21T18:33:06.957926+00:00 through 2026-10-21T18:33:09.667095+00:00;
    metadata ph-optimum-high-strict.json
  accessed_at: '2026-10-21T18:47:52Z'
  support: context_only
  summary: Passed at 18:33:06–18:33:09 UTC; schema validity is distinct from imported
    relation meaning.
  snapshot_sha256: b3e1f3e47468bb3e4b763d0cb145bb7387748b829263bfad0ba690b2a4c3da87
- evidence_id: check-ph-optimum-high-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-snippets.log
  locator: Executed 2026-10-21T18:33:06.952290+00:00 through 2026-10-21T18:33:21.235005+00:00;
    metadata ph-optimum-high-snippets.json
  accessed_at: '2026-10-21T18:47:52Z'
  support: context_only
  summary: Exit 2 at 18:33:06–18:33:21 UTC from DNS failure. Optional superseded access
    attempt; no source conclusion follows.
  snapshot_sha256: ecbfeeec63b2cb4b25e6f71ce392ac0c7911199a2cb00775e136dbbc576bd1ed
- evidence_id: check-ph-optimum-high-snippets-network-retry
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-snippets-network-retry.log
  locator: Executed 2026-10-21T18:33:50.683403+00:00 through 2026-10-21T18:33:54.213249+00:00;
    metadata ph-optimum-high-snippets-network-retry.json
  accessed_at: '2026-10-21T18:47:52Z'
  support: context_only
  summary: 'Passed at 18:33:50–18:33:54 UTC: six fields, one VERIFIED and five NOT_IN_ABSTRACT.
    Manual primary checking finds four literal Krulwich snippets and two Baker body-unverified
    snippets.'
  snapshot_sha256: 7ddb918fb37087f4ebf3bfde26f449ef6943aaf7ae80962e8b215b6003607eaf
- evidence_id: check-corpus-protein-taxa
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-004.f7_g5r4w/corpus-protein-taxa.log
  locator: Executed 2026-10-21T08:55:04Z through 2026-10-21T08:55:10Z; metadata corpus-protein-taxa.json
  accessed_at: '2026-10-21T18:47:52Z'
  support: context_only
  summary: Original B4 08:55:04–08:55:10 UTC pass with unchanged inputs; zero current
    protein instances, so no fresh target instance audit is claimed.
  snapshot_sha256: f5f1a6be7789f2b3e487fcbc354361f8f1f0d0d0f90a9ba59864d26ed7ac49ef
- evidence_id: check-batch009-qc
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-009.x21w9b3v/batch009-qc.log
  locator: Executed 2026-10-21T17:05:16Z through 2026-10-21T17:06:53Z; metadata batch009-qc.json
  accessed_at: '2026-10-21T18:47:52Z'
  support: context_only
  summary: Original B9 17:05:16–17:06:53 UTC pass, qualified against current B10 bytes;
    not a new B10 final QC execution.
  snapshot_sha256: 1e73fe337dd10255851461d2d40b079ceeaf952d923b01ea8a16573963dcb05d
- evidence_id: record
  kind: record_content
  reference: data/traits/environment/ph_optimum_high.yaml
  locator: Entire current target
  accessed_at: '2026-10-21T18:37:15.120788Z'
  support: supports
  summary: Fifteen nodes, ten edges, five components, five label-only protein classes,
    zero instances, one canonical and sixteen record events are covered.
  snapshot_sha256: 7c60e5e61ddbde6b115fbe4be96386696385e87040fb5924daa6c7d4da12cf6f
- evidence_id: checklist
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Captured maintained policy
  accessed_at: '2026-10-21T18:37:15.120788Z'
  support: supports
  summary: Whole-record identity, source, graph, optional fields, ownership, provenance
    and readiness checklist.
  snapshot_sha256: da8896328a0fd6cc92f1adf0d8be8980d0ddd41f3172c7936f2c7f119b293ac1
- evidence_id: policy
  kind: authority
  reference: docs/GROUNDING_POLICY.md
  locator: Captured maintained policy
  accessed_at: '2026-10-21T18:37:15.120788Z'
  support: supports
  summary: Preserve actual referents and permitted functional facets; no token protein
    or connectivity requirement.
  snapshot_sha256: 891678c983c2283a47c81c47950b35753981e9339d105f3bbdda92a1f5ab7f42
- evidence_id: native-types
  kind: authority
  reference: src/traitmech/schema/traitmech.yaml
  locator: Captured maintained policy
  accessed_at: '2026-10-21T18:37:15.120788Z'
  support: supports
  summary: Chemical entities, concentration attributes, states and processes are distinct
    representational facets.
  snapshot_sha256: 46c47fc627b80ccbba1e8ab3fb6f2aee93bc2aef7aaf72fe9aadc3257f2c02dd
- evidence_id: human-policy
  kind: authority
  reference: docs/CURATION_PLAYBOOK.md
  locator: Captured maintained policy
  accessed_at: '2026-10-21T18:37:15.120788Z'
  support: supports
  summary: AI maintenance and REVIEWED do not identify attributable human scientific
    acceptance.
  snapshot_sha256: 735e9b810471da9f7d8364e35ffe1e741edb3421480dac01727db6ea5aa65da9
- evidence_id: reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/common-reuse-b9-qc-supplement-qualified.json
  locator: Qualified B10 comparison and original B9 gates
  accessed_at: '2026-10-21T17:07:14.407314Z'
  support: supports
  summary: All 1,130 traits, 1,278 history files and nineteen common inputs match.
    Original timestamps, baselines, failures, retries and skips remain explicit.
  snapshot_sha256: 515c688663a8a3f68f71fb2c3467217864338204f7f5197443642a81a8ec84c0
- evidence_id: capture
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-grounding-agent/final-capture-verification.json
  locator: Derived assessment or read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:37:15.121949Z'
  support: supports
  summary: All 73 current captured input hashes match.
  snapshot_sha256: 0b426278e05e78a3e1a1f882d5d3a4888df16e91fdd55a18d3dc6d79ff72b1df
- evidence_id: identity
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-grounding-agent/identity-assessment.json
  locator: Derived assessment or read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:37:14.981399Z'
  support: supports
  summary: Active exact identity, direct parent and explicit obsolete replacement
    agree. Faithful synonym import is distinct from scientific equivalence.
  snapshot_sha256: 8c0faf50b7ef84d95f7819474a4d41958b86848110db50d9680bf299746792cc
- evidence_id: node-edges
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-grounding-agent/node-edge-ledger.json
  locator: Derived assessment or read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:37:14.980505Z'
  support: supports
  summary: All fifteen nodes and ten edges; firm imported-role fields are edges 1
    and 4, with two bounded node-facet issues.
  snapshot_sha256: 77f8401504de351159e1cb79d7d6361d93f57f894ff6213e3d91e2934b6ecd2d
- evidence_id: owners
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-grounding-agent/owner-provenance-assessment.json
  locator: Derived assessment or read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:37:15.120293Z'
  support: supports
  summary: Exact maintained rows and writers, five fully read histories and bounded
    238-path/68-array/zero-exact target search.
  snapshot_sha256: ab6dc0c1b60ec97d625f5761a6066b95a5ec2fa6851fff38d5ca71fced4cbf07
- evidence_id: expression
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-grounding-agent/expression-applicability.json
  locator: Derived assessment or read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:37:15.120627Z'
  support: supports
  summary: No focal species/type-alias catalog match; no substitute species or downstream
    defense query.
  snapshot_sha256: 18d9afbb67d7c5c1ca82f221190df8139a87cd452ceb751febf92183318083a5
- evidence_id: authority-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-grounding-agent/authority-reuse-receipts.json
  locator: Derived assessment or read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:35:03.288866Z'
  support: supports
  summary: Original PATO and catalog access times remain distinct from current byte
    copies and reading.
  snapshot_sha256: 0e0c4306fcfeb99b1df13f29919ae67d4679e87324220bdb178677eeb66165d3
- evidence_id: local-authority
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-grounding-agent/local-authority-excerpts.json
  locator: Derived assessment or read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:35:03.269537Z'
  support: supports
  summary: Actual v2/v3/v8/v9 authorities and broad Biolink endpoints, read together
    with maintained mapping clarifications.
  snapshot_sha256: e4543a4c6e40677b4d5152c9cfbf4b26efbdc744923ed2ecd9f05a9ef6b98d96
- evidence_id: selected-ro
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-grounding-agent/selected-ro-primary-reading.json
  locator: Derived assessment or read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:35:03.053199Z'
  support: supports
  summary: Actual RO statements and inherited process roles; primary database hash
    is separate from query-receipt hash.
  snapshot_sha256: 70f1aa49d94c7ae7cfd641f49f7586f5c0a6a32b6fecffb8a79220f6ab24b0b7
- evidence_id: ground-manifest
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-grounding-agent/evidence-manifest.json
  locator: Derived assessment or read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:37:15.124783Z'
  support: supports
  summary: Twenty-three frozen grounding artifacts.
  snapshot_sha256: 38c8817d048d97a36bdd96618ba7c764196f04b877e197ed39dfc35fbc8bcd18
- evidence_id: history-addendum
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-grounding-agent/history-target-projection-addendum.json
  locator: Derived assessment or read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:37:33.601301Z'
  support: supports
  summary: Corrects a plural-key history projection to actual singular targets. Five
    original AI actor inventories and scientific conclusions are unchanged.
  snapshot_sha256: de223dc65239c1bb7d7c14748fb5d24b5db0285b620350a983a87ae2197b551d
- evidence_id: metpo-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/repo/data/raw/metpo.owl
  locator: METPO:1000458, direct parent 1000331, obsolete 0000180 and nested numerical
    restriction
  accessed_at: '2026-10-21T18:35:03.049470Z'
  support: supports
  summary: Active identity and parent agree; obsolete 0000180 explicitly links to
    the active term. The pinned class uses inclusive 8–14 and supplies the same exact
    synonym. Upstream import does not independently establish scientific equivalence.
  snapshot_sha256: 8b6f8fe0510a698579e532658c8ace05da2550093365df9ca83feb0741778415
- evidence_id: ro-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/ro.db
  locator: RO:0002211 process domain/range; RO:0002212 inherits regulates
  accessed_at: '2026-10-21T18:35:03.053199Z'
  support: supports
  summary: Material antiporter subjects conflict with the process regulator role.
    The concentration object at edge 4 is also not a process. The secretion and maintenance
    processes at edge 9 fit these endpoint roles.
  snapshot_sha256: 849e616c29fecd0d4a6c6dee0dc0f6f117ace7167dbfa1e0f043dc84868f83cb
- evidence_id: biolink-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/repo/data/raw/biolink-model.yaml
  locator: produces textual material-producer description; inherited named-thing endpoints
  accessed_at: '2026-10-21T18:35:03.269537Z'
  support: supports
  summary: The material Rnf subject is compatible. Broad formal endpoints do not impose
    a material-only product range; no additional formal error is assigned to edge
    6.
  snapshot_sha256: 4955709e1cac1d26fd657f7a0c29d6c8390f42e41f9ebfab859c82b102f2bebb
- evidence_id: taxonomy-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-grounding-agent/taxon1463663.xml
  locator: Official NCBITaxon:1463663 species identity and type aliases
  accessed_at: '2026-10-21T18:34:31.071598Z'
  support: supports
  summary: Bacillus aequororis identity is positive. Species taxonomy and the source
    isolate 5-DB remain distinct scopes; no exact optimum measurement is inferred
    from taxonomy.
  snapshot_sha256: 6850dbb8a9ae31734b4cb41712c76b39c8531dd39c45db812b94fd666bc96fb9
- evidence_id: pato-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-grounding-agent/pato0001430.response
  locator: Official retained PATO:0001430 alkaline response
  accessed_at: '2026-10-21T15:49:02.450641Z'
  support: supports
  summary: The alkaline-quality facet is coherent; it does not by itself calibrate
    the exact numerical optimum bin.
  snapshot_sha256: 7f77f57947754bacd75912291a9812f06bb31632dded25a78e64b29e6a2316f0
- evidence_id: meta-krulwich
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-root/krulwich-metadata.json
  locator: Europe PMC title/abstract/status surface for DOI:10.1038/nrmicro2549
  accessed_at: '2026-10-21T18:30:12.881155Z'
  support: supports
  summary: Assigned bibliographic identity and returned abstract only. Selected body
    observations have separate evidence and acquisition times.
  snapshot_sha256: 484784a62fbb4c9d74a1feab4df2fdfdf37d4dd0ce3fa79f714c86a07d86d29c
- evidence_id: meta-baker
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-root/baker-metadata.json
  locator: Europe PMC title/abstract/status surface for DOI:10.1016/j.tim.2007.02.005
  accessed_at: '2026-10-21T18:30:12.781736Z'
  support: supports
  summary: Assigned bibliographic identity and returned abstract only. Selected body
    observations have separate evidence and acquisition times.
  snapshot_sha256: e12f1b09a1467a8985fae8d345351ad5ef2fc532f35fb10be67203ec41ea939b
- evidence_id: meta-aem
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-root/aem-metadata.json
  locator: Europe PMC title/abstract/status surface for DOI:10.1128/AEM.00145-24
  accessed_at: '2026-10-21T18:30:12.863079Z'
  support: supports
  summary: Assigned bibliographic identity and returned abstract only. Selected body
    observations have separate evidence and acquisition times.
  snapshot_sha256: f6fa43f19bd85d5db0beacff59b7fc4df859e4c92b69afb200c514bf7d8e6fa6
- evidence_id: meta-rnf
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-root/rnf-metadata.json
  locator: Europe PMC title/abstract/status surface for DOI:10.1515/hsz-2015-0137
  accessed_at: '2026-10-21T18:30:12.744034Z'
  support: supports
  summary: Assigned bibliographic identity and returned abstract only. Selected body
    observations have separate evidence and acquisition times.
  snapshot_sha256: 09294233805c8717d791159e61ac464d1f92003aaf9d0f25662f77a5d67f69e3
- evidence_id: meta-respiration
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-root/respiration-metadata.json
  locator: Europe PMC title/abstract/status surface for DOI:10.3389/fmicb.2024.1468929
  accessed_at: '2026-10-21T18:30:13.438280Z'
  support: supports
  summary: Assigned bibliographic identity and returned abstract only. Selected body
    observations have separate evidence and acquisition times.
  snapshot_sha256: 8cd8f12652c14dba6b72917956fa191e90e7e7a6ce58d1a78b8964e4cd14d40b
- evidence_id: meta-minerals
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-root/minerals-metadata.json
  locator: Europe PMC title/abstract/status surface for DOI:10.3390/min14090861
  accessed_at: '2026-10-21T18:30:13.392445Z'
  support: context_only
  summary: Zero indexed hits are retained without inferring publication absence; exact
    Crossref and official PDF are separately bound.
  snapshot_sha256: 8215f109022bcbcd743fdf12908352d844612e44f116542cfed2e493bfc5a695
- evidence_id: meta-canonical
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-root/canonical-metadata.json
  locator: Europe PMC title/abstract/status surface for DOI:10.1155/2024/3087296
  accessed_at: '2026-10-21T18:30:13.568644Z'
  support: supports
  summary: Assigned bibliographic identity and returned abstract only. Selected body
    observations have separate evidence and acquisition times.
  snapshot_sha256: 2195f58575dcd56fc839f95a139c1e8107605b7342a070450d916776fa3476e7
- evidence_id: body-krulwich
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/krulwich-bioc.xml
  locator: Retained BioC; selected generic passages and literal snippets
  accessed_at: '2026-10-21T07:57:33Z'
  support: supports
  summary: Generic pH-homeostasis context and four short literal phrases; no detailed
    pathogen mechanism assessment or claim of universal exact-bin calibration.
  snapshot_sha256: 903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f
- evidence_id: body-canonical
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/canonical.xml
  locator: Introduction body paragraphs 0/3/4 and selected conclusion
  accessed_at: '2026-10-21T18:33:31.868395Z'
  support: supports
  summary: The author classification of 5-DB as a facultative alkaliphile is positive;
    exact best-growth measurement remains limited in the inspected scope.
  snapshot_sha256: 27ff0a4deeb4ee46f16eb6caea70872e0946110f4b013db496efb8cce87d6a73
- evidence_id: body-respiration
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/respiration.xml
  locator: Introduction body paragraph 3; documentary attribution only
  accessed_at: '2026-10-21T18:33:31.768247Z'
  support: supports
  summary: Numerical examples are attributed to named model organisms. Values are
    present; the current note omits their model attribution. Detailed oxygen/fitness
    biology remains unassessed.
  snapshot_sha256: 77319d67b9386d1626d76df21beeb6d7652ee2eb6368345f7dea72787c301150
- evidence_id: minerals-crossref
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/minerals-crossref.json
  locator: Exact DOI registration metadata
  accessed_at: '2026-10-21T18:33:31.058365Z'
  support: supports
  summary: Exact Minerals DOI and publication identity resolve independently of Europe
    PMC indexing.
  snapshot_sha256: ae4a572df20db6995948b016402c0983692f172b6178e14f7501ff6fede16f4c
- evidence_id: synonym-primary
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/canonical.xml
  locator: 'Introduction body paragraph 0: stated tolerant versus alkaliphilic optimum
    conventions'
  accessed_at: '2026-10-21T18:33:31.868395Z'
  support: refutes
  summary: The stated tolerance category includes optima below the numerical high
    bin, challenging exact synonym equivalence. This source convention is not imposed
    as a universal physiological classification.
  snapshot_sha256: 27ff0a4deeb4ee46f16eb6caea70872e0946110f4b013db496efb8cce87d6a73
- evidence_id: body-minerals
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/minerals-public-cdn.pdf
  locator: Official PDF page 6, section 2.5; extracted lines 275–285
  accessed_at: '2026-10-21T18:34:55.419963Z'
  support: supports
  summary: Existing generic polymer and organic-acid wording is present. This source
    check does not independently certify structural or detailed mechanistic interpretation.
  snapshot_sha256: 7040f3b4649074b12977c89b55e6dc0f28af1a9a411bed7938c9216a358d9017
- evidence_id: sources
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/source-assessment.json
  locator: Derived assessment or read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:37:37.984747Z'
  support: supports
  summary: Frozen source-placement subset and one attribution minor; separate synonym
    assessment is appended without rewriting this subset.
  snapshot_sha256: 8034b154841d44fa2512a83ca781c6fa254a7a27eb1186dc8311f255c976d5ba
- evidence_id: source-ledger
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/source-ledger.json
  locator: Derived assessment or read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:37:37.981782Z'
  support: supports
  summary: Seven exact assigned identities; metadata, selected body scope and unavailable
    body limits remain distinct.
  snapshot_sha256: 305e7a400bf0ac352fbd7350ca72758357beee0b5a4ce8085a82c2c357bb8cf0
- evidence_id: placements
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/placement-ledger.json
  locator: Derived assessment or read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:37:37.982029Z'
  support: supports
  summary: All fourteen external placements covered.
  snapshot_sha256: 444f0c6ea1f4034844a06bb56ecc948b01cfc6407586c1158f5c9551535f53c9
- evidence_id: snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/snippet-ledger.json
  locator: Derived assessment or read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:37:37.982675Z'
  support: supports
  summary: Four literal Krulwich phrases and two Baker body-unverified phrases; no
    false-absence claim.
  snapshot_sha256: 9b2fbc61abc52da2853ec2b833ff27fcdbf71b8fb884d2386f8d76b49a4b52c7
- evidence_id: node-sources
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/node-source-ledger.json
  locator: Derived assessment or read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:37:37.982855Z'
  support: supports
  summary: Every current node source facet covered with scope qualifications.
  snapshot_sha256: d36bb2bf7016ae50f513476d3f3950276a460862499fe6abb4e97b0db341f6c3
- evidence_id: edge-sources
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/edge-source-ledger.json
  locator: Derived assessment or read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:37:37.982765Z'
  support: supports
  summary: All ten edges; documentary attribution at edge 7 is separate from unassessed
    detailed oxygen/fitness biology.
  snapshot_sha256: 021eca258a73223f8ef0ddcf45aa6b707b647515cd40eb43aee711cbfbcce4b4
- evidence_id: source-status
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/publication-status-ledger.json
  locator: Derived assessment or read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:37:37.981888Z'
  support: supports
  summary: Returned notice fields and exact Crossref metadata only; no exhaustive
    global notice search claimed.
  snapshot_sha256: dbba11f61beb1da9bd20a7cc5bb6bbd4b1cec51e4225f853b90bdad316dd52a4
- evidence_id: source-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/selected-primary-reading.json
  locator: Derived assessment or read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:37:37.979795Z'
  support: supports
  summary: Actual selected primary passages and metadata abstracts read, not entire
    articles.
  snapshot_sha256: 3e7a4b8d8cce4def05c1893912bc9b90c4b3ab31cbe954abeb78c6113a347732
- evidence_id: source-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/access-limitations.json
  locator: Derived assessment or read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:37:37.984501Z'
  support: supports
  summary: Baker, AEM and Rnf body limitations remain unknown; a zero-byte Rnf HTML
    response is not a PDF body.
  snapshot_sha256: cb03db2d7d7f78fa07efaeac407c2f1c420a47a472c619df60f984de791d477e
- evidence_id: source-manifest
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/evidence-manifest.json
  locator: Derived assessment or read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:37:37.989933Z'
  support: supports
  summary: Thirty-six frozen source artifacts.
  snapshot_sha256: a40cf67f8262d6bcede8efde34d00a9a8d77492cd33ceb709cb0c6196b13ab6c
- evidence_id: body-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/reuse-and-copy-receipt.json
  locator: Derived assessment or read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:37:37.973261Z'
  support: supports
  summary: Krulwich original 07:57:33 acquisition remains separate from current copies
    and reading.
  snapshot_sha256: ffa0a7992f29889d080df62ee907feb9581b73c42f3b65274685c60be0044054
- evidence_id: native-checks
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/native-check-context.json
  locator: Derived assessment or read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:37:37.984282Z'
  support: supports
  summary: Initial uv-cache failure and snippet DNS failure are separate from successful
    inspect and focused retry.
  snapshot_sha256: 503976941e53fbaa20b2ba10d58fed982ff60a9e175ed7a9b76a002057c22635
- evidence_id: canonical-source
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/canonical-assessment.json
  locator: Derived assessment or read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:37:37.982927Z'
  support: supports
  summary: Named author classification is positive; exact growth-optimum measurement
    is not reconstructed from metabolic or resistance endpoints.
  snapshot_sha256: 2850a7be67d35b86832b717ecde1e55c4858cd00fb9590cbdddfebabfa6a84d5
- evidence_id: synonym-supplement
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/synonym-scope-supplement.json
  locator: Derived assessment or read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:42:17.078715Z'
  support: supports
  summary: 'Append-only assessment outside the original placement subset: exact tolerance
    synonym conflicts with numerical-bin equivalence, while faithful upstream import
    is retained.'
  snapshot_sha256: 54ddc73c69bff6043b722f80825b8860c37c14cfc88fda3bce384da9d343ee31
- evidence_id: pdf-extraction
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/pdf-extraction-receipt.json
  locator: Derived assessment or read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:37:37.980739Z'
  support: supports
  summary: Local PDF extraction has its own input/output hashes; the primary evidence
    reference retains the PDF hash.
  snapshot_sha256: 98ae04fbb68c97f2debae05ca3b975a9a61f1963dbe4ffd410c373b6d8e91410
- evidence_id: root-reading-37
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-root/whole-target-preinspect-reading.json
  locator: Derived assessment or read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:30:04.909304Z'
  support: supports
  summary: Only the actual scope and chronology recorded in this root reading receipt;
    no later or full-body reading inferred.
  snapshot_sha256: 3fd1357c4906651e8d153025b1abb1f657df47e2c481f78015690863e9f2fb84
- evidence_id: root-reading-38
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-root/primary-ro-reading.json
  locator: Derived assessment or read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:34:37.378205Z'
  support: supports
  summary: Only the actual scope and chronology recorded in this root reading receipt;
    no later or full-body reading inferred.
  snapshot_sha256: 5b3cd68aaace3174c5acd8045ae0e929a6e8018dcc9b5ba92c70129b7e8f9555
- evidence_id: root-reading-39
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-root/frozen-ledger-root-reading.json
  locator: Derived assessment or read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:42:14.935043Z'
  support: supports
  summary: Only the actual scope and chronology recorded in this root reading receipt;
    no later or full-body reading inferred.
  snapshot_sha256: d983a5f0b2a6ee0b22a4810f34b5b3ddca93286d3af99e916109a92ff5121553
- evidence_id: root-reading-40
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-root/primary-owner-root-reading.json
  locator: Derived assessment or read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:36:25.289877Z'
  support: supports
  summary: Only the actual scope and chronology recorded in this root reading receipt;
    no later or full-body reading inferred.
  snapshot_sha256: 83a5c99124dfbb7d5d14df23dfbf42e9d9d57366d3fc80ebd4535854e8d735cc
- evidence_id: root-reading-41
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-root/initial-primary-root-reading.json
  locator: Derived assessment or read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:34:25.470104Z'
  support: supports
  summary: Only the actual scope and chronology recorded in this root reading receipt;
    no later or full-body reading inferred.
  snapshot_sha256: 48099685c9465297d684abe75af00d6080db1d18bc286cfafcbda23976ef2220
- evidence_id: root-synonym-supplement
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-root/synonym-supplement-reading.json
  locator: Derived assessment or read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:42:54.067460Z'
  support: supports
  summary: Root verified the later append-only synonym supplement and its eight bindings;
    final finding counts did not change.
  snapshot_sha256: 3c2d443da388dee5b6c9d17cc8ff954f83649765e8d3f2d2a88c60a32047a09c
- evidence_id: initial-inspect-failure
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high.inspect-failed-retention.json
  locator: Retained initial failed uv launch and exact relocated stdout/stderr/command
    bytes
  accessed_at: '2026-10-21T18:32:47.818291Z'
  support: context_only
  summary: The initial default-cache launch failed before the native helper. Successful
    isolated-cache inspect followed; this is an optional superseded orchestration
    failure, not completed-review validation or serialization failure.
  snapshot_sha256: f318ff74ddfaf0e082076a8e9f6ecdd7f89daf96c069e58660080b9c74ca9084
- evidence_id: challenge
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-semantic-challenge-agent/semantic-severity-challenge.json
  locator: Final independent semantic review and verified bindings
  accessed_at: '2026-10-21T18:40:01.855463Z'
  support: supports
  summary: Independent disposition and qualifications; detailed biological efficacy
    is not certified.
  snapshot_sha256: 13d391541a952e22eda49fa82f980c1df1811feecc2aa818877fb9f4a4a65420
- evidence_id: adjudication
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-root-adjudication.json
  locator: Final root adjudication and verified bindings
  accessed_at: '2026-10-21T18:42:14.938335Z'
  support: supports
  summary: Final disposition governs five findings, preserving separate supplements
    and source limits.
  snapshot_sha256: d3ed0a6a999b7844d39b88b74c94ca94bcb1f2c9a26ae8143f39da04730779c6
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: active identity, definition and hierarchy'
  outcome: supported
  target_ids:
  - METPO:1000458
  summary: Active METPO:1000458, parent 1000331 and explicit obsolete 0000180 replacement
    agree. Formal bounds are inclusive 8–14; approximately above 8 is retained as
    a convention limitation, not another finding.
  evidence_ids:
  - identity
  - metpo-primary
  - record
- assessment_id: synonym-scope
  area: identity
  topic: 'Native checklist: exact synonym versus numerical class'
  outcome: concern
  target_ids:
  - METPO:1000458
  summary: Alkali Tolerant is faithfully inherited as EXACT, but the assigned primary
    classification includes optima below the numerical high bin. Shared context does
    not establish equal class membership. Only synonyms[0] is a confirmed finding;
    other aliases are not silently promoted to extra findings.
  evidence_ids:
  - synonym-supplement
  - synonym-primary
  - metpo-primary
  - challenge
  - adjudication
- assessment_id: scope
  area: scope
  topic: 'Native checklist: quantitative class and generic graph context'
  outcome: supported
  target_ids:
  - METPO:1000458
  summary: ENVIRONMENT, CLASS and NONMECHANISTIC are coherent. Five components, five
    contextual label-only classes and zero instances are permissible; generic context
    is not automatically a universal mechanism claim.
  evidence_ids:
  - record
  - policy
  - checklist
- assessment_id: canonical
  area: evidence
  topic: 'Native checklist: named canonical classification and limits'
  outcome: unknown
  target_ids:
  - METPO:1000458
  summary: Official Bacillus aequororis species identity and the source classification
    of 5-DB as facultatively alkaliphilic are positive. Exact best-growth measurement
    remains limited by inspected primary scope; taxonomy and metabolic endpoints do
    not supply a new quantitative optimum.
  evidence_ids:
  - identity
  - taxonomy-primary
  - canonical-source
  - body-canonical
- assessment_id: bibliography
  area: evidence
  topic: 'Native checklist: seven works and fourteen placements'
  outcome: supported
  target_ids:
  - METPO:1000458
  summary: All seven assigned DOI identities resolve, including Minerals through exact
    Crossref and official PDF. Each of fourteen placements is assessed on its actual
    available surface. Zero Europe PMC hits did not establish absence.
  evidence_ids:
  - source-ledger
  - placements
  - source-status
  - minerals-crossref
  details: "{\n  \"completed_at\": \"2026-10-21T18:37:37.984747+00:00\",\n  \"target\"\
    : \"data/traits/environment/ph_optimum_high.yaml\",\n  \"target_sha256\": \"7c60e5e61ddbde6b115fbe4be96386696385e87040fb5924daa6c7d4da12cf6f\"\
    ,\n  \"capture\": {\n    \"path\": \"/private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high.inspect.json\"\
    ,\n    \"sha256\": \"48fbe8e34988118efca214d50616cf2581e09f221ae34e26000d1ad5e0df3fd9\"\
    ,\n    \"bytes\": 14788\n  },\n  \"capture_inputs\": 73,\n  \"counts\": {\n  \
    \  \"works\": 7,\n    \"literal_reference_forms\": 7,\n    \"external_placements\"\
    : 14,\n    \"ontology_source_placements\": 0,\n    \"nodes\": 15,\n    \"edges\"\
    : 10,\n    \"snippets\": 6,\n    \"exact_snippets\": 4,\n    \"unverified_snippets\"\
    : 2,\n    \"canonical_examples\": 1\n  },\n  \"source_only_findings\": [\n   \
    \ {\n      \"severity\": \"minor\",\n      \"area\": \"evidence\",\n      \"field_paths\"\
    : [\n        \"causal_graphs[0].edges[7].evidence[0].notes\"\n      ],\n     \
    \ \"summary\": \"The note omits the model-organism attribution attached to the\
    \ numerical efficiency examples in the cited Introduction.\",\n      \"primary_locator\"\
    : \"Respiration JATS body paragraph 3, introductory comparison of Rhodobacter\
    \ and Thermus model oxidases.\",\n      \"qualification\": \"The source values\
    \ are present as contextual examples, not established measurements in the focal\
    \ C. thermarum study or every member of the aggregate class. This is documentary\
    \ precision only; it does not assert false values, a universal biological contradiction\
    \ or any corrected oxygen/fitness mechanism.\",\n      \"suggested_action\": \"\
    Retain source attribution/model scope or qualify the note as comparative context;\
    \ no biological target, efficacy correction, new condition or protocol is proposed.\"\
    \n    }\n  ],\n  \"source_only_major_candidates\": [],\n  \"unassessed_biological_edge_indices\"\
    : [\n    7\n  ],\n  \"summary\": \"Seven assigned DOI identities resolve, including\
    \ Minerals via exact Crossref and official public PDF. Four short snippets are\
    \ literal and two Baker phrases remain body-unverified. One bounded source minor\
    \ concerns omitted model-organism attribution of efficiency examples at edge7\
    \ notes; detailed oxygen/fitness biology is unassessed. Canonical author classification\
    \ and Minerals generic statements remain positive, with precise best-growth and\
    \ unavailable AEM/Rnf/Baker scope limitations.\",\n  \"qualifications\": [\n \
    \   \"No exact biological mechanism or universal-bin claim is inferred merely\
    \ from generic graph labels.\",\n    \"The review does not infer wrong citation\
    \ from the Rnf or Baker title alone.\",\n    \"EPMC indexing absence and inaccessible\
    \ body are not publication absence or false quotation.\",\n    \"Original Krulwich07:57:33\
    \ acquisition, current root metadata18:30:12\\u201313, new primary responses18:33:30\\\
    u201331 and Minerals PDF18:34:54\\u201355 remain separate from current reading.\"\
    ,\n    \"Canonical exact quantitative optimum is not reconstructed from metabolic\
    \ or resistance readouts.\"\n  ]\n}"
- assessment_id: snippets
  area: evidence
  topic: 'Native checklist: six assigned quotations'
  outcome: unknown
  target_ids:
  - METPO:1000458
  summary: Four Krulwich snippets are literal and two Baker phrases remain body-unverified.
    Native abstract checking found one verified and five nonmatches; body evidence
    explains the distinct manual result without implying false quotation from unavailable
    text.
  evidence_ids:
  - snippets
  - source-access
  - native-checks
  details: "{\n  \"completed_at\": \"2026-10-21T18:37:37.982675+00:00\",\n  \"counts\"\
    : {\n    \"total\": 6,\n    \"exact_literal\": 4,\n    \"unverified_body\": 2\n\
    \  },\n  \"snippets\": [\n    {\n      \"field_path\": \"evidence[0].snippet\"\
    ,\n      \"reference\": \"DOI:10.1038/nrmicro2549\",\n      \"snippet\": \"alkaliphiles\"\
    ,\n      \"status\": \"EXACT_LITERAL\",\n      \"basis\": {\n        \"body\"\
    : {\n          \"path\": \"/private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/krulwich-bioc.xml\"\
    ,\n          \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n          \"bytes\": 174908\n        },\n        \"BioC_offsets\": [\n    \
    \      \"5466\",\n          \"15130\",\n          \"16479\",\n          \"39232\"\
    ,\n          \"39253\",\n          \"41582\",\n          \"42119\",\n        \
    \  \"45597\"\n        ]\n      }\n    },\n    {\n      \"field_path\": \"evidence[1].snippet\"\
    ,\n      \"reference\": \"DOI:10.1016/j.tim.2007.02.005\",\n      \"snippet\"\
    : \"proton motive force\",\n      \"status\": \"UNVERIFIED_BODY\",\n      \"basis\"\
    : {\n        \"metadata\": {\n          \"path\": \"/private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/baker-metadata.json\"\
    ,\n          \"sha256\": \"e12f1b09a1467a8985fae8d345351ad5ef2fc532f35fb10be67203ec41ea939b\"\
    ,\n          \"bytes\": 4065\n        },\n        \"retained_failure\": {\n  \
    \        \"path\": \"/private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/prior-ph-delta-additional-primary-body-accesses-root.json\"\
    ,\n          \"sha256\": \"2b59f554309b38f437bff006507e7703ec541aca6057897b3651ae1c0af76355\"\
    ,\n          \"bytes\": 840\n        },\n        \"qualification\": \"Unknown\
    \ body wording, not a false-quotation assertion.\"\n      }\n    },\n    {\n \
    \     \"field_path\": \"causal_graphs[0].edges[0].evidence[0].snippet\",\n   \
    \   \"reference\": \"DOI:10.1038/nrmicro2549\",\n      \"snippet\": \"alkaliphiles\"\
    ,\n      \"status\": \"EXACT_LITERAL\",\n      \"basis\": {\n        \"body\"\
    : {\n          \"path\": \"/private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/krulwich-bioc.xml\"\
    ,\n          \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n          \"bytes\": 174908\n        },\n        \"BioC_offsets\": [\n    \
    \      \"5466\",\n          \"15130\",\n          \"16479\",\n          \"39232\"\
    ,\n          \"39253\",\n          \"41582\",\n          \"42119\",\n        \
    \  \"45597\"\n        ]\n      }\n    },\n    {\n      \"field_path\": \"causal_graphs[0].edges[1].evidence[0].snippet\"\
    ,\n      \"reference\": \"DOI:10.1016/j.tim.2007.02.005\",\n      \"snippet\"\
    : \"proton motive force\",\n      \"status\": \"UNVERIFIED_BODY\",\n      \"basis\"\
    : {\n        \"metadata\": {\n          \"path\": \"/private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/baker-metadata.json\"\
    ,\n          \"sha256\": \"e12f1b09a1467a8985fae8d345351ad5ef2fc532f35fb10be67203ec41ea939b\"\
    ,\n          \"bytes\": 4065\n        },\n        \"retained_failure\": {\n  \
    \        \"path\": \"/private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/prior-ph-delta-additional-primary-body-accesses-root.json\"\
    ,\n          \"sha256\": \"2b59f554309b38f437bff006507e7703ec541aca6057897b3651ae1c0af76355\"\
    ,\n          \"bytes\": 840\n        },\n        \"qualification\": \"Unknown\
    \ body wording, not a false-quotation assertion.\"\n      }\n    },\n    {\n \
    \     \"field_path\": \"causal_graphs[0].edges[2].evidence[0].snippet\",\n   \
    \   \"reference\": \"DOI:10.1038/nrmicro2549\",\n      \"snippet\": \"alkaliphiles\"\
    ,\n      \"status\": \"EXACT_LITERAL\",\n      \"basis\": {\n        \"body\"\
    : {\n          \"path\": \"/private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/krulwich-bioc.xml\"\
    ,\n          \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n          \"bytes\": 174908\n        },\n        \"BioC_offsets\": [\n    \
    \      \"5466\",\n          \"15130\",\n          \"16479\",\n          \"39232\"\
    ,\n          \"39253\",\n          \"41582\",\n          \"42119\",\n        \
    \  \"45597\"\n        ]\n      }\n    },\n    {\n      \"field_path\": \"causal_graphs[0].edges[3].evidence[0].snippet\"\
    ,\n      \"reference\": \"DOI:10.1038/nrmicro2549\",\n      \"snippet\": \"cytoplasmic\
    \ pH\",\n      \"status\": \"EXACT_LITERAL\",\n      \"basis\": {\n        \"\
    body\": {\n          \"path\": \"/private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-high-source-agent/krulwich-bioc.xml\"\
    ,\n          \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n          \"bytes\": 174908\n        },\n        \"BioC_offsets\": [\n    \
    \      \"58\",\n          \"671\",\n          \"2440\",\n          \"3940\",\n\
    \          \"4950\",\n          \"7133\",\n          \"7180\",\n          \"7328\"\
    \n        ]\n      }\n    }\n  ]\n}"
- assessment_id: node-facets
  area: grounding
  topic: 'Native checklist: all fifteen current node referents'
  outcome: concern
  target_ids:
  - METPO:1000458
  summary: Sodium concentration at node 6 and electrochemical gradient at node 9 differ
    from the declared chemical/process facets. Their intended meanings are readable,
    supporting one bounded precision minor. PMF STATE and label-only proteins are
    otherwise permitted.
  evidence_ids:
  - node-edges
  - native-types
  - policy
  - pato-primary
  - local-authority
  details: "[\n  {\n    \"index\": 0,\n    \"field_path\": \"causal_graphs[0].nodes[0]\"\
    ,\n    \"node\": {\n      \"node_id\": \"ph_optimum_high_trait\",\n      \"label\"\
    : \"pH optimum high\",\n      \"node_type\": \"TRAIT\",\n      \"grounding\":\
    \ \"METPO:1000458\",\n      \"description\": \"pH optimum above ~8.\"\n    },\n\
    \    \"assessment\": \"Active exact numerical high-optimum trait. Raw METPO restricts\
    \ the optimum to inclusive 8\\u201314; approximately-above-8 wording remains a\
    \ boundary convention limitation, not a demonstrated strict exclusion at 8.\"\n\
    \  },\n  {\n    \"index\": 1,\n    \"field_path\": \"causal_graphs[0].nodes[1]\"\
    ,\n    \"node\": {\n      \"node_id\": \"ph_optimum\",\n      \"label\": \"pH\
    \ optimum\",\n      \"node_type\": \"TRAIT\",\n      \"grounding\": \"METPO:1000331\"\
    ,\n      \"description\": \"External pH supporting maximal growth.\"\n    },\n\
    \    \"assessment\": \"Active exact parent pH-optimum trait; hierarchy is directly\
    \ asserted in raw METPO.\"\n  },\n  {\n    \"index\": 2,\n    \"field_path\":\
    \ \"causal_graphs[0].nodes[2]\",\n    \"node\": {\n      \"node_id\": \"alkaline_external_ph\"\
    ,\n      \"label\": \"alkaline external pH\",\n      \"node_type\": \"ENVIRONMENTAL_FACTOR\"\
    ,\n      \"description\": \"External pH > ~8, typical of soda lakes and other\
    \ alkaline habitats.\",\n      \"grounding\": \"PATO:0001430\"\n    },\n    \"\
    assessment\": \"Environmental alkaline condition, coherently grounded to active\
    \ PATO alkaline quality as a condition facet. The PATO term does not independently\
    \ establish the numeric optimum boundary.\"\n  },\n  {\n    \"index\": 3,\n  \
    \  \"field_path\": \"causal_graphs[0].nodes[3]\",\n    \"node\": {\n      \"node_id\"\
    : \"na_h_antiporters\",\n      \"label\": \"Na+/H+ antiporters\",\n      \"node_type\"\
    : \"GENE_OR_PROTEIN\",\n      \"grounding_status\": \"REVIEWED_LABEL_ONLY\",\n\
    \      \"grounding_notes\": \"Reviewed as a contextual protein or protein-complex\
    \ label within a quantitative measurement graph; no exact semantic family term\
    \ was established for this aggregate use.\",\n      \"description\": \"Membrane\
    \ antiporters importing H+ in exchange for Na+ to acidify the cytoplasm at high\
    \ external pH.\"\n    },\n    \"assessment\": \"Explicit material membrane antiporter\
    \ aggregate; reviewed label-only contextual class is permissible. No accession\
    \ or extra component is required. Detailed biological efficacy is not certified.\"\
    \n  },\n  {\n    \"index\": 4,\n    \"field_path\": \"causal_graphs[0].nodes[4]\"\
    ,\n    \"node\": {\n      \"node_id\": \"alkaliphile_homeostasis\",\n      \"\
    label\": \"alkaliphile cytoplasmic pH homeostasis\",\n      \"node_type\": \"\
    BIOLOGICAL_PROCESS\",\n      \"description\": \"Maintenance of a less alkaline\
    \ cytoplasm than the external environment by proton re-import.\"\n    },\n   \
    \ \"assessment\": \"Homeostasis is an explicit biological process. Source scope\
    \ and exact-bin sufficiency are assessed separately.\"\n  },\n  {\n    \"index\"\
    : 5,\n    \"field_path\": \"causal_graphs[0].nodes[5]\",\n    \"node\": {\n  \
    \    \"node_id\": \"cpa_nha_antiporters\",\n      \"label\": \"CPA/Nha family\
    \ Na+/H+ antiporters\",\n      \"node_type\": \"GENE_OR_PROTEIN\",\n      \"grounding_status\"\
    : \"REVIEWED_LABEL_ONLY\",\n      \"grounding_notes\": \"Reviewed as a contextual\
    \ protein or protein-complex label within a quantitative measurement graph; no\
    \ exact semantic family term was established for this aggregate use.\",\n    \
    \  \"description\": \"Monovalent cation/proton antiporter family exporting Na+\
    \ and importing H+.\"\n    },\n    \"assessment\": \"Explicit material CPA/Nha\
    \ antiporter family; label-only class remains permissible. Its function does not\
    \ make the represented material itself a process.\"\n  },\n  {\n    \"index\"\
    : 6,\n    \"field_path\": \"causal_graphs[0].nodes[6]\",\n    \"node\": {\n  \
    \    \"node_id\": \"intracellular_na\",\n      \"label\": \"intracellular Na+\
    \ concentration\",\n      \"node_type\": \"CHEMICAL\",\n      \"description\"\
    : \"Cytoplasmic sodium ion concentration.\"\n    },\n    \"assessment\": \"Both\
    \ label and description denote intracellular sodium concentration, a measurable\
    \ attribute, whereas CHEMICAL denotes an entity. Bounded facet precision issue;\
    \ the readable concentration referent remains clear. This is not a false sodium\
    \ identity or biological-efficacy assertion.\"\n  },\n  {\n    \"index\": 7,\n\
    \    \"field_path\": \"causal_graphs[0].nodes[7]\",\n    \"node\": {\n      \"\
    node_id\": \"trkah_k_uptake\",\n      \"label\": \"TrkAH K+ uptake system\",\n\
    \      \"node_type\": \"GENE_OR_PROTEIN\",\n      \"grounding_status\": \"REVIEWED_LABEL_ONLY\"\
    ,\n      \"grounding_notes\": \"Reviewed as a contextual protein or protein-complex\
    \ label within a quantitative measurement graph; no exact semantic family term\
    \ was established for this aggregate use.\",\n      \"description\": \"Potassium\
    \ uptake transport system aiding membrane potential and pH homeostasis.\"\n  \
    \  },\n    \"assessment\": \"Explicit material uptake-system aggregate. Label-only\
    \ status has documentary support from maintained policy; no exact family accession\
    \ is fabricated.\"\n  },\n  {\n    \"index\": 8,\n    \"field_path\": \"causal_graphs[0].nodes[8]\"\
    ,\n    \"node\": {\n      \"node_id\": \"rnf_complex\",\n      \"label\": \"Rnf\
    \ complex\",\n      \"node_type\": \"GENE_OR_PROTEIN\",\n      \"grounding_status\"\
    : \"REVIEWED_LABEL_ONLY\",\n      \"grounding_notes\": \"Reviewed as a contextual\
    \ protein or protein-complex label within a quantitative measurement graph; no\
    \ exact semantic family term was established for this aggregate use.\",\n    \
    \  \"description\": \"Ferredoxin:NAD oxidoreductase that pumps Na+ to build a\
    \ transmembrane Na+ gradient.\"\n    },\n    \"assessment\": \"Explicit material\
    \ Rnf complex, not merely an activity label. Biological details are outside the\
    \ grounding assessment.\"\n  },\n  {\n    \"index\": 9,\n    \"field_path\": \"\
    causal_graphs[0].nodes[9]\",\n    \"node\": {\n      \"node_id\": \"transmembrane_na_gradient\"\
    ,\n      \"label\": \"transmembrane Na+ gradient\",\n      \"node_type\": \"BIOLOGICAL_PROCESS\"\
    ,\n      \"description\": \"Electrochemical sodium ion gradient across the membrane.\"\
    \n    },\n    \"assessment\": \"Label and description denote an electrochemical\
    \ sodium gradient, not its establishment. Native STATE explicitly separates a\
    \ gradient from generating processes; BIOLOGICAL_PROCESS therefore needs bounded\
    \ facet clarification. No additional Biolink hard range error follows.\"\n  },\n\
    \  {\n    \"index\": 10,\n    \"field_path\": \"causal_graphs[0].nodes[10]\",\n\
    \    \"node\": {\n      \"node_id\": \"terminal_oxidases\",\n      \"label\":\
    \ \"branched respiratory chain terminal oxidases\",\n      \"node_type\": \"GENE_OR_PROTEIN\"\
    ,\n      \"grounding_status\": \"REVIEWED_LABEL_ONLY\",\n      \"grounding_notes\"\
    : \"Reviewed as a contextual protein or protein-complex label within a quantitative\
    \ measurement graph; no exact semantic family term was established for this aggregate\
    \ use.\",\n      \"description\": \"Terminal oxidases (aa3/ba3/bb3) that pump\
    \ protons with differing efficiencies.\"\n    },\n    \"assessment\": \"Explicit\
    \ material terminal-oxidase aggregate; no exact enzyme-family or subunit grounding\
    \ is imposed.\"\n  },\n  {\n    \"index\": 11,\n    \"field_path\": \"causal_graphs[0].nodes[11]\"\
    ,\n    \"node\": {\n      \"node_id\": \"proton_motive_force\",\n      \"label\"\
    : \"proton motive force\",\n      \"node_type\": \"STATE\",\n      \"description\"\
    : \"Electrochemical proton gradient powering bioenergetics.\",\n      \"grounding\"\
    : \"METPO:1007500\"\n    },\n    \"assessment\": \"Explicit electrochemical proton-gradient\
    \ STATE. Local v3 authority and maintained node-type migration agree; current\
    \ local produces gate deliberately permits this state object.\"\n  },\n  {\n \
    \   \"index\": 12,\n    \"field_path\": \"causal_graphs[0].nodes[12]\",\n    \"\
    node\": {\n      \"node_id\": \"acidic_membrane_polymers\",\n      \"label\":\
    \ \"acidic plasma membrane polymers\",\n      \"node_type\": \"CHEMICAL\",\n \
    \     \"description\": \"Acidic cell-envelope polymers (teichuronopeptide, peptidoglycan,\
    \ teichuronic acid).\"\n    },\n    \"assessment\": \"Chemical aggregate of acidic\
    \ cell-envelope polymers; composition and effect are source questions, not decided\
    \ by this declared chemical facet.\"\n  },\n  {\n    \"index\": 13,\n    \"field_path\"\
    : \"causal_graphs[0].nodes[13]\",\n    \"node\": {\n      \"node_id\": \"organic_acid_secretion\"\
    ,\n      \"label\": \"organic acid secretion\",\n      \"node_type\": \"BIOLOGICAL_PROCESS\"\
    ,\n      \"description\": \"Secretion of metabolic organic acids that helps counter\
    \ alkaline stress.\"\n    },\n    \"assessment\": \"Organic-acid secretion is\
    \ an explicit process; detailed physiological efficacy is not certified.\"\n \
    \ },\n  {\n    \"index\": 14,\n    \"field_path\": \"causal_graphs[0].nodes[14]\"\
    ,\n    \"node\": {\n      \"node_id\": \"ph_balance\",\n      \"label\": \"pH\
    \ balance\",\n      \"node_type\": \"BIOLOGICAL_PROCESS\",\n      \"description\"\
    : \"Maintenance of cytoplasmic pH balance under alkaline stress.\"\n    },\n \
    \   \"assessment\": \"pH balance is described as maintenance, an explicit process\
    \ rather than the numeric pH value.\"\n  }\n]"
- assessment_id: relations
  area: consistency
  topic: 'Native checklist: all ten relation meanings'
  outcome: concern
  target_ids:
  - METPO:1000458
  summary: 'Only edges 1 and 4 are confirmed imported-role errors: material antiporter
    classes occupy process-regulator roles, and edge 4 targets concentration. Edge
    9 process endpoints fit. Local row 2 explicitly permits STATE for edge 7; older
    v9 prose alone does not negate maintained clarification. Biolink formal endpoints
    remain broad.'
  evidence_ids:
  - node-edges
  - ro-primary
  - biolink-primary
  - local-authority
  - owners
  - challenge
  details: "[\n  {\n    \"index\": 0,\n    \"field_path\": \"causal_graphs[0].edges[0]\"\
    ,\n    \"subject\": \"alkaline_external_ph\",\n    \"predicate\": \"selects for\"\
    ,\n    \"predicate_id\": \"METPO:2007401\",\n    \"object\": \"alkaliphile_homeostasis\"\
    ,\n    \"formal_status\": \"qualified_adaptation_context\",\n    \"assessment\"\
    : \"Local v2 selects-for has broad causal-node endpoints and an evolutionary adaptation\
    \ meaning. The process can name an adaptive physiological trait in this context;\
    \ distinguish selection from immediate homeostatic response without inventing\
    \ a hard domain exclusion.\",\n    \"biological_scope\": \"Formal/documentary\
    \ roles only. Detailed pathogen defense, fitness, acid tolerance, AMR and intervention\
    \ efficacy remain UNASSESSED_SCOPE; no pathway reconstruction or optimization.\"\
    \n  },\n  {\n    \"index\": 1,\n    \"field_path\": \"causal_graphs[0].edges[1]\"\
    ,\n    \"subject\": \"na_h_antiporters\",\n    \"predicate\": \"regulates\",\n\
    \    \"predicate_id\": \"RO:0002211\",\n    \"object\": \"alkaliphile_homeostasis\"\
    ,\n    \"formal_status\": \"confirmed_imported_role_mismatch\",\n    \"assessment\"\
    : \"RO:0002211 requires process endpoints. The subject explicitly names material\
    \ membrane antiporters, while the object is homeostasis process. Functional context\
    \ does not silently substitute antiporter activity for the declared material.\"\
    ,\n    \"biological_scope\": \"Formal/documentary roles only. Detailed pathogen\
    \ defense, fitness, acid tolerance, AMR and intervention efficacy remain UNASSESSED_SCOPE;\
    \ no pathway reconstruction or optimization.\"\n  },\n  {\n    \"index\": 2,\n\
    \    \"field_path\": \"causal_graphs[0].edges[2]\",\n    \"subject\": \"alkaliphile_homeostasis\"\
    ,\n    \"predicate\": \"confers\",\n    \"predicate_id\": \"METPO:2007700\",\n\
    \    \"object\": \"ph_optimum_high_trait\",\n    \"formal_status\": \"local_roles_compatible\"\
    ,\n    \"assessment\": \"Local v8 confers explicitly permits biological processes\
    \ as subjects and TRAIT objects. Generic homeostasis context and exact numeric-bin\
    \ sufficiency remain source-limited; role compatibility is not empirical proof\
    \ of the bin.\",\n    \"biological_scope\": \"Formal/documentary roles only. Detailed\
    \ pathogen defense, fitness, acid tolerance, AMR and intervention efficacy remain\
    \ UNASSESSED_SCOPE; no pathway reconstruction or optimization.\"\n  },\n  {\n\
    \    \"index\": 3,\n    \"field_path\": \"causal_graphs[0].edges[3]\",\n    \"\
    subject\": \"ph_optimum_high_trait\",\n    \"predicate\": \"is a\",\n    \"predicate_id\"\
    : \"rdfs:subClassOf\",\n    \"object\": \"ph_optimum\",\n    \"formal_status\"\
    : \"hierarchy_supported\",\n    \"assessment\": \"TRAIT-to-parent rdfs:subClassOf\
    \ agrees with the direct upstream hierarchy. Literature snippets alone are not\
    \ used as a formal hierarchy authority.\",\n    \"biological_scope\": \"Formal/documentary\
    \ roles only. Detailed pathogen defense, fitness, acid tolerance, AMR and intervention\
    \ efficacy remain UNASSESSED_SCOPE; no pathway reconstruction or optimization.\"\
    \n  },\n  {\n    \"index\": 4,\n    \"field_path\": \"causal_graphs[0].edges[4]\"\
    ,\n    \"subject\": \"cpa_nha_antiporters\",\n    \"predicate\": \"decreases\"\
    ,\n    \"predicate_id\": \"RO:0002212\",\n    \"object\": \"intracellular_na\"\
    ,\n    \"formal_status\": \"confirmed_imported_role_mismatch\",\n    \"assessment\"\
    : \"RO:0002212 inherits process-to-process roles from RO:0002211. Current subject\
    \ is the material CPA/Nha family; object is intracellular sodium concentration\
    \ represented as CHEMICAL. Neither the material nor concentration denotes the\
    \ regulated process. The object facet is separately bounded wording precision.\"\
    ,\n    \"biological_scope\": \"Formal/documentary roles only. Detailed pathogen\
    \ defense, fitness, acid tolerance, AMR and intervention efficacy remain UNASSESSED_SCOPE;\
    \ no pathway reconstruction or optimization.\"\n  },\n  {\n    \"index\": 5,\n\
    \    \"field_path\": \"causal_graphs[0].edges[5]\",\n    \"subject\": \"trkah_k_uptake\"\
    ,\n    \"predicate\": \"maintains\",\n    \"predicate_id\": null,\n    \"object\"\
    : \"alkaliphile_homeostasis\",\n    \"formal_status\": \"free_predicate_no_invented_constraint\"\
    ,\n    \"assessment\": \"Maintains is a free predicate without imported identifier.\
    \ No mandatory external ID or arbitrary formal role restriction is imposed; physiological\
    \ support is source-audited separately.\",\n    \"biological_scope\": \"Formal/documentary\
    \ roles only. Detailed pathogen defense, fitness, acid tolerance, AMR and intervention\
    \ efficacy remain UNASSESSED_SCOPE; no pathway reconstruction or optimization.\"\
    \n  },\n  {\n    \"index\": 6,\n    \"field_path\": \"causal_graphs[0].edges[6]\"\
    ,\n    \"subject\": \"rnf_complex\",\n    \"predicate\": \"generates\",\n    \"\
    predicate_id\": \"biolink:produces\",\n    \"object\": \"transmembrane_na_gradient\"\
    ,\n    \"formal_status\": \"biolink_material_subject_compatible\",\n    \"assessment\"\
    : \"Rnf material complex satisfies Biolink produces textual material-producer\
    \ meaning. Formal inherited endpoints are broad named things, so no hard material-only\
    \ product range is inferred for a gradient. Node 9 process-versus-state wording\
    \ is a separate bounded issue.\",\n    \"biological_scope\": \"Formal/documentary\
    \ roles only. Detailed pathogen defense, fitness, acid tolerance, AMR and intervention\
    \ efficacy remain UNASSESSED_SCOPE; no pathway reconstruction or optimization.\"\
    \n  },\n  {\n    \"index\": 7,\n    \"field_path\": \"causal_graphs[0].edges[7]\"\
    ,\n    \"subject\": \"terminal_oxidases\",\n    \"predicate\": \"produces\",\n\
    \    \"predicate_id\": \"METPO:2007800\",\n    \"object\": \"proton_motive_force\"\
    ,\n    \"formal_status\": \"maintained_local_authority_allows_state\",\n    \"\
    assessment\": \"The older v9 proposed definition says chemical output, but maintained\
    \ mapping row 2 explicitly adds STATE for this exact terminal-oxidases\\u2192PMF\
    \ edge, with #392/#393 histories explaining agent generation of a gradient. Formal\
    \ proposed endpoints are broad causal nodes. This is a draft/maintained-authority\
    \ qualification, not a confirmed record-role defect.\",\n    \"biological_scope\"\
    : \"Formal/documentary roles only. Detailed pathogen defense, fitness, acid tolerance,\
    \ AMR and intervention efficacy remain UNASSESSED_SCOPE; no pathway reconstruction\
    \ or optimization.\"\n  },\n  {\n    \"index\": 8,\n    \"field_path\": \"causal_graphs[0].edges[8]\"\
    ,\n    \"subject\": \"acidic_membrane_polymers\",\n    \"predicate\": \"enhances\"\
    ,\n    \"predicate_id\": null,\n    \"object\": \"proton_motive_force\",\n   \
    \ \"formal_status\": \"free_predicate_no_invented_constraint\",\n    \"assessment\"\
    : \"Enhances is an ungrounded local predicate. Chemical aggregate to PMF state\
    \ is not ruled out by an invented imported role constraint; no biological mechanism\
    \ or intervention validation is claimed.\",\n    \"biological_scope\": \"Formal/documentary\
    \ roles only. Detailed pathogen defense, fitness, acid tolerance, AMR and intervention\
    \ efficacy remain UNASSESSED_SCOPE; no pathway reconstruction or optimization.\"\
    \n  },\n  {\n    \"index\": 9,\n    \"field_path\": \"causal_graphs[0].edges[9]\"\
    ,\n    \"subject\": \"organic_acid_secretion\",\n    \"predicate\": \"regulates\"\
    ,\n    \"predicate_id\": \"RO:0002211\",\n    \"object\": \"ph_balance\",\n  \
    \  \"formal_status\": \"external_roles_compatible\",\n    \"assessment\": \"RO:0002211\
    \ process-to-process endpoints fit organic-acid secretion and pH-balance maintenance.\
    \ Formal compatibility does not validate detailed efficacy or universal applicability.\"\
    ,\n    \"biological_scope\": \"Formal/documentary roles only. Detailed pathogen\
    \ defense, fitness, acid tolerance, AMR and intervention efficacy remain UNASSESSED_SCOPE;\
    \ no pathway reconstruction or optimization.\"\n  }\n]"
- assessment_id: source-context
  area: evidence
  topic: 'Native checklist: attribution and biological scope'
  outcome: concern
  target_ids:
  - METPO:1000458
  summary: Edge 7 notes omit named model-organism attribution from numerical examples.
    The values are present and no new canonical measurements are asserted. Generic
    Minerals/homeostasis context is positive; detailed pathogen defense, oxygen/hypoxia,
    fitness, ROS, AMR and intervention mechanisms remain UNASSESSED_SCOPE.
  evidence_ids:
  - sources
  - edge-sources
  - body-respiration
  - body-minerals
  - source-reading
- assessment_id: completeness
  area: completeness
  topic: 'Native checklist: whole record and optional fields'
  outcome: supported
  target_ids:
  - METPO:1000458
  summary: All fifteen nodes, ten edges, five components, five label-only proteins,
    zero instances, one canonical and sixteen events are covered. No arbitrary protein,
    connector or dataset requirement is imposed.
  evidence_ids:
  - record
  - node-edges
  - checklist
  - policy
- assessment_id: expression
  area: scope
  topic: 'Native checklist: canonical catalog applicability'
  outcome: not_applicable
  target_ids:
  - METPO:1000458
  summary: No focal Bacillus aequororis or verified type-alias match in the retained
    complete 20-organism/28-dataset catalog. Bacillus subtilis is a different species
    and was not substituted; no downstream defense query was made.
  evidence_ids:
  - expression
  - authority-reuse
- assessment_id: owners
  area: ownership
  topic: 'Native checklist: maintained recurrence and clarification'
  outcome: supported
  target_ids:
  - METPO:1000458
  summary: Rows 11/61 can refill empty relation IDs while the grounder skips nonempty
    IDs. Row 2 and node-type migration support PMF STATE. Exact legacy-CURIE migration
    does not blindly rewrite a current local placeholder; shared history leads are
    not automatic target owners.
  evidence_ids:
  - owners
  - local-authority
  - history-addendum
  - challenge
  details: "{\n  \"assessed_at\": \"2026-10-21T18:37:15.120293+00:00\",\n  \"target\"\
    : \"data/traits/environment/ph_optimum_high.yaml\",\n  \"counts\": {\n    \"nodes\"\
    : 15,\n    \"edges\": 10,\n    \"components\": 5,\n    \"protein_classes\": 5,\n\
    \    \"label_only_proteins\": 5,\n    \"protein_instances\": 0,\n    \"canonical_examples\"\
    : 1,\n    \"history_events\": 16,\n    \"ai_events\": 15,\n    \"seed_events\"\
    : 1,\n    \"captured_history_files\": 5,\n    \"matching_files\": 238,\n    \"\
    review_target_arrays\": 68,\n    \"exact_target_arrays\": 0\n  },\n  \"search_basis\"\
    : \"Ignored/hidden-inclusive exact target slug, hyphenated slug, label, both ID\
    \ forms, related synonym and all exact synonyms. Search and parsed target arrays\
    \ retained in full. All-node owner/history discovery independently confirms five\
    \ captured histories.\",\n  \"whole_histories_read\": [\n    \"history/infrastructure/inconsistent-node-type/2026-08-12T000912Z-claude-code-779670.yaml\"\
    ,\n    \"history/infrastructure/node-type-consistency/2026-08-15T014631Z-claude-code-9d7f4d.yaml\"\
    ,\n    \"history/infrastructure/pathway-vs-process/2026-08-16T010630Z-claude-code-192557.yaml\"\
    ,\n    \"history/infrastructure/predicate-gate-audit/2026-08-16T074719Z-claude-code-84d88d.yaml\"\
    ,\n    \"history/other/canonical-examples-six/2026-08-21T065406Z-codex-a1ab82.yaml\"\
    \n  ],\n  \"reading_scope\": \"All five captured histories fully read after successful\
    \ capture. They document AI infrastructure maintenance and canonical backfill,\
    \ not attributable human scientific approval. No full scientific review of parent/sibling\
    \ records is claimed.\",\n  \"current_history\": \"Sixteen events comprise fifteen\
    \ explicitly AI-assisted events and one seed event. REVIEWED is not itself a linked\
    \ human acceptance decision.\",\n  \"owners\": [\n    {\n      \"path\": \"data/traits/environment/ph_optimum_high.yaml\"\
    ,\n      \"role\": \"Maintained target; record-level corrections require separately\
    \ authorized curation.\"\n    },\n    {\n      \"path\": \"mappings/predicate_grounding.tsv\"\
    ,\n      \"role\": \"Rows 11 and 61 can refill RO2211/2212 without type gates\
    \ if identifiers are empty. Row 2 deliberately admits STATE for edge 7, so it\
    \ is positive maintained authority, not a recurrence defect there.\"\n    },\n\
    \    {\n      \"path\": \"scripts/ground_causal_predicates.py\",\n      \"role\"\
    : \"Lines 152\\u2013180 skip nonempty predicate IDs and apply table gates only\
    \ during initial filling; no automatic overwrite claim.\"\n    },\n    {\n   \
    \   \"path\": \"scripts/migrate_node_type_consistency.py\",\n      \"role\": \"\
    Lines 52\\u201368 preserve PMF as the gradient state, not its establishment.\"\
    \n    },\n    {\n      \"path\": \"scripts/migrate_remaining_microbe_domain_edges.py\"\
    ,\n      \"role\": \"Lines 57\\u201387 perform exact legacy-CURIE migration; a\
    \ current placeholder edge is not blindly re-migrated.\"\n    },\n    {\n    \
    \  \"path\": \"proposals/metpo_traitmech_v9/metpo_proposal_properties_robot.tsv\"\
    ,\n      \"role\": \"Older chemical-output prose should be interpreted alongside\
    \ maintained row 2 and the explicit histories; do not declare current edge 7 invalid\
    \ by selecting only the narrower draft.\"\n    }\n  ],\n  \"research_scope\":\
    \ \"Current captured research is provenance and a lead, not direct literature\
    \ evidence or proof of the exact historical report bytes. Shared-node scripts\
    \ are contextual leads, not automatically target writers.\",\n  \"human_traceability\"\
    : \"No exact target review array or attributable acceptance link was found in\
    \ the stated local scope. Remote/private decisions remain unknown.\"\n}"
- assessment_id: human-acceptance
  area: provenance
  topic: 'Native checklist: bounded local acceptance traceability'
  outcome: concern
  target_ids:
  - METPO:1000458
  summary: Ignored-inclusive search found 238 paths, 68 parsed actual review arrays
    and zero exact target arrays. Sixteen record events comprise 15 AI events plus
    seed. Five captured histories were fully read and have AI actors; the separate
    singular-target correction preserves this basis. No linked human acceptance was
    found within these local bounds.
  evidence_ids:
  - owners
  - history-addendum
  - human-policy
  - challenge
  - adjudication
- assessment_id: checks
  area: schema
  topic: 'Native checklist: focused passes and qualified common reuse'
  outcome: supported
  target_ids:
  - METPO:1000458
  summary: Native and strict checks passed; focused snippets passed after a retained
    DNS attempt. All 73 inputs match. Initial uv-cache failure preceded successful
    inspect and was not a completed-review validation failure. Historical common/B4/B9
    checks retain actual times, failures, retries, baselines and skips.
  evidence_ids:
  - capture
  - reuse
  - initial-inspect-failure
  - native-checks
  - check-ph-optimum-high-validate
  - check-ph-optimum-high-strict
  - check-ph-optimum-high-snippets-network-retry
findings:
- finding_id: exact-tolerance-synonym
  issue_key: ph-optimum-high-exact-tolerance-synonym
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Exact tolerance synonym does not match the numerical optimum class
  description: 'The assigned primary classification includes alkali-tolerant optima
    below the inclusive 8–14 high bin, so Alkali Tolerant cannot be assumed extensionally
    equivalent to that whole class. Raw METPO supplies the same EXACT synonym: this
    is inherited semantic scope, not a local transcription mistake. The cited convention
    is not imposed universally on other publications.'
  target_ids:
  - METPO:1000458
  field_paths:
  - synonyms[0]
  evidence_ids:
  - synonym-supplement
  - synonym-primary
  - metpo-primary
  - identity
  - challenge
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_optimum_high.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: imported-regulation-roles
  issue_key: ph-optimum-high-imported-regulation-roles
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Material antiporter classes occupy imported process-regulator roles
  description: RO:0002211 requires process endpoints and RO:0002212 inherits those
    roles. Both current subjects at edges 1 and 4 explicitly denote material antiporter
    classes; edge 4 also targets concentration rather than a regulated process. Native
    structural validity does not resolve these declared-referent conflicts.
  target_ids:
  - METPO:1000458
  field_paths:
  - causal_graphs[0].edges[1]
  - causal_graphs[0].edges[4]
  evidence_ids:
  - record
  - node-edges
  - ro-primary
  - owners
  - challenge
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_optimum_high.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: concentration-gradient-facets
  issue_key: ph-optimum-high-concentration-gradient-facets
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Concentration and gradient nodes have imprecise declared facets
  description: Node 6 explicitly denotes sodium concentration while its CHEMICAL type
    denotes an entity. Node 9 explicitly denotes an electrochemical gradient while
    BIOLOGICAL_PROCESS denotes a process and native STATE distinguishes a gradient
    from its establishment. The intended referents are clear; this is one bounded
    precision issue, without additional biological or predicate findings.
  target_ids:
  - METPO:1000458
  field_paths:
  - causal_graphs[0].nodes[6]
  - causal_graphs[0].nodes[9]
  evidence_ids:
  - node-edges
  - native-types
  - local-authority
  - challenge
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_optimum_high.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: scripts/migrate_node_type_consistency.py
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: model-attribution
  issue_key: ph-optimum-high-model-attribution
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Numerical examples omit their model-organism attribution
  description: The assigned respiration Introduction attributes its numerical examples
    to named model organisms. Edge 7 notes omit that attribution, although the values
    are present and the record does not explicitly claim new measurements in the canonical
    organism. This is source precision only; detailed oxygen/fitness biology remains
    unassessed.
  target_ids:
  - METPO:1000458
  field_paths:
  - causal_graphs[0].edges[7].evidence[0].notes
  evidence_ids:
  - sources
  - edge-sources
  - body-respiration
  - source-reading
  - challenge
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_optimum_high.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: human-acceptance-link
  issue_key: ph-optimum-high-human-acceptance-link
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Local provenance lacks a linked human acceptance decision
  description: REVIEWED and AI maintenance do not identify attributable human acceptance.
    The bounded ignored-inclusive 238-path/68-array/zero-exact search, sixteen record
    events and five AI histories preserve positive maintenance while leaving remote/private
    decisions unknown. The target-projection correction is separately retained.
  target_ids:
  - METPO:1000458
  field_paths:
  - mapping_status
  - curation_history
  evidence_ids:
  - owners
  - history-addendum
  - human-policy
  - challenge
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_optimum_high.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
actions:
- action_id: reconcile-synonym-scope
  description: During separately authorized curation, reconcile or qualify the inherited
    exact synonym against the numerical class and cited convention.
  finding_ids:
  - exact-tolerance-synonym
  target_ids:
  - METPO:1000458
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_optimum_high.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Preserve upstream METPO provenance and the active numerical identity; do not characterize
    faithful import as local transcription error.
  - Document the authority or scope behind exact equivalence without imposing one
    publication convention universally.
  - Use guarded history and applicable identity, native, strict and QC checks; retain
    this immutable review and add a successor after changed inputs.
- action_id: reconcile-regulation-roles
  description: Reconcile the two confirmed imported-role fields with their current
    declared referents during authorized curation.
  finding_ids:
  - imported-regulation-roles
  target_ids:
  - METPO:1000458
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_optimum_high.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Verify the actual inherited process roles and incident relations; distinguish
    a material class from activity without constructing a repaired biological route.
  - Review mapping refill behavior and nonempty-ID skips, preserving valid edge 9
    and the explicit STATE allowance for local edge 7.
  - Use guarded history and applicable native, strict, mapping and QC checks; no scientific
    source data are modified by this review.
- action_id: clarify-node-facets
  description: Clarify concentration and gradient representation while preserving
    the current intended referents.
  finding_ids:
  - concentration-gradient-facets
  target_ids:
  - METPO:1000458
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_optimum_high.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: scripts/migrate_node_type_consistency.py
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Choose a documented native facet consistent with the intended quantity or state;
    no blanket enum replacement is prescribed.
  - Reassess incident edges and guarded writer recurrence; do not add token proteins,
    connectors or mechanisms.
  - Use guarded record/repository history and applicable native, strict and QC checks.
- action_id: retain-model-attribution
  description: Qualify the existing numerical note with the source model attribution
    during authorized curation.
  finding_ids:
  - model-attribution
  target_ids:
  - METPO:1000458
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_optimum_high.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Keep the values as attributed comparative context rather than asserting canonical
    measurements or universal efficacy.
  - Do not supply an oxygen/fitness intervention, altered condition or repaired biological
    mechanism.
  - Recheck the exact citation/quotation and applicable native, strict and evidence
    checks.
- action_id: link-human-acceptance
  description: Link existing attributable human acceptance if available, or clarify
    status while retaining the bounded absence result.
  finding_ids:
  - human-acceptance-link
  target_ids:
  - METPO:1000458
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_optimum_high.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Preserve the 238-path/68-array/zero-exact search and distinguish sixteen record
    events from five fully read history records.
  - Retain the projection correction; do not infer acceptance from AI work, ontology
    authorship or passing checks.
  - No contact with another person or automatic status promotion is authorized by
    this proposed action.
limitations:
- Detailed pathogen defense, oxygen/hypoxia, fitness, ROS, AMR and intervention biology
  remains UNASSESSED_SCOPE. The respiration review checks literal numerical attribution
  only; no mechanism repair or optimization is supplied.
- The exact-synonym concern is inherited from pinned METPO. The cited physiological
  classification is a stated convention, not a universal rule; other aliases are not
  added findings.
- Formal METPO bounds are inclusive 8–14. Approximately above 8 does not unequivocally
  exclude 8, so that wording is a precision limitation rather than a separate defect.
- The canonical author classification of 5-DB is positive. Exact best-growth measurement
  is not reconstructed from taxonomy, metabolic or resistance endpoints.
- Two Baker snippets remain body-unverified; AEM and Rnf body scopes are limited.
  A zero-byte HTML response with a PDF filename is not article text. Titles, indexing
  absence and access failures alone do not establish wrong citations or false biology.
- Older v9 chemical-product prose is read together with explicit maintained row 2
  STATE allowance and migration history. No automatic formal-role finding is assigned
  to edge 7. Biolink formal endpoints remain broad; free predicates have no invented
  imported restrictions.
- Original Krulwich 07:57:33, root metadata 18:30:12–18:30:13, fresh JATS/Crossref
  18:33:30–18:33:31 and Minerals PDF 18:34:54–18:34:55 acquisition times remain separate
  from current copying and selected reading. No full-article reading is claimed.
- The initial uv-cache inspect launch and initial snippet DNS failure are retained
  separately from successful inspect and focused retry. They are not completed-review
  validation or serializer failures.
- The local ignored-inclusive search cannot establish absence of remote/private acceptance.
  All five history records were fully read by the grounding auditor; root read two.
  The separate singular-target projection addendum corrects a documentary extraction
  without changing original actor counts.
- Five components, five label-only protein classes and zero instances are permissible.
  No token accession, substitute species or downstream defense-expression query is
  required.
notes:
- 'Final disposition: two major findings, three minor findings, fourteen assessments
  and five linked proposed actions.'
- 'Coverage: 73 captured inputs, 23 frozen grounding artifacts plus separate history
  correction, 36 frozen source artifacts plus separate synonym supplement, fifteen
  nodes, ten edges, five components, five label-only protein classes, zero instances,
  one canonical and sixteen record events. Seven works, fourteen placements and six
  snippets retain exact source scope.'
- Serializer is single-use and guarded. Root owns one execution, native review validation
  and save after independent reading. Preparation does not alter scientific records,
  state or Git.
tags:
- record-review
- ph-optimum-high
- environment
- needs-curation
native_verdict: needs_curation
```
