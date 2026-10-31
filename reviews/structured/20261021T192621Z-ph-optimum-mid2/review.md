# Whole-record review of pH optimum mid2

- Review: 20261021T192621Z-ph-optimum-mid2
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-21T19:16:15.706761Z
- Finished UTC: 2026-10-21T19:26:21Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Needs curation: two majors address exact-alias scope and imported relation subjects; two minors address bounded PATHWAY referent precision and human acceptance. Active identity, parent, canonical optimum, current activity/state facets and local powers remain positive.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: First record of batch 011 in actual queue order. Entire target and successful 75-input capture precede substantive judgment. Metadata was acquired before capture and interpreted after it. Frozen independent audits and final root adjudication are required before serialization.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8eee04a8c65609fbaff6df7c54597dcaf1b9d282.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| METPO:1000457 | data/traits/environment/ph_optimum_mid2.yaml | maintained | pH optimum mid2 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full-corpus graph audit | passed | True | METPO:1000457 | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| Full-corpus snippet audit | passed | True | METPO:1000457 | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| Full-corpus pathway links | passed | True | METPO:1000457 | 19 links checked against the pinned PathwayMech snapshot. |
| Full-corpus history integrity | passed | True | METPO:1000457 | 1277 history records checked, zero invalid links at the 8eee source base; integrity does not establish science or human acceptance. |
| Initial full-product validation | failed | False | METPO:1000457 | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation with isolated local cache | failed | False | METPO:1000457 | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation after isolated-cache download | passed | True | METPO:1000457 | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| Focused native validation | passed | True | METPO:1000457 | Direct pass at 19:16:35.094566–19:16:35.804540 UTC; shape validity is separate from scientific support. |
| Focused strict validation | passed | True | METPO:1000457 | Direct pass at 19:16:35.096817–19:16:36.193502 UTC with zero error rows. |
| Focused snippet verification | passed | True | METPO:1000457 | Direct pass at 19:16:38.115487–19:16:42.292545 UTC: four fields over two references, three VERIFIED and one NOT_IN_ABSTRACT. Manual primary assessment independently finds three literal phrases and one Baker body-unverified phrase. |
| Reused maintained batch-ten QC | passed | True | METPO:1000457 | Actual B10 19:06:27.731868–19:08:11.219124 UTC pass, qualified against B11 bytes; not a new B11 execution. |
| Protein-instance metadata applicability | not_applicable | False | METPO:1000457 | Three contextual protein classes, two reviewed label-only classes and zero instances; no token accession requirement. |

## Scientific And Domain Assessments

### Native checklist: active identity, definition and hierarchy

identity: supported. Targets: METPO:1000457.

Active METPO:1000457, direct parent 1000331 and explicit obsolete 0000179 replacement agree. The raw class is inclusive 7–8. Local definition synthesizes the parent and interval; it is not falsely presented as a verbatim raw-class definition.

### Native checklist: inherited aliases and scientific scope

identity: concern. Targets: METPO:1000457.

Alkali Tolerant and Alkaliphile are faithfully imported exact aliases, but actual primary classifications include optima beyond 7–8. The concern is limited to synonyms 0/1. Neutrophile is not independently refuted, and pHO_7_to_8 remains a related bin label.

### Native checklist: quantitative phenotype and generic graph

scope: supported. Targets: METPO:1000457.

ENVIRONMENT, CLASS and NONMECHANISTIC are appropriate to this quantitative optimum bin. Generic context is not automatically a universal necessary mechanism; no compulsory protein instance or connector is inferred.

### Native checklist: canonical identity and measured optimum

evidence: supported. Targets: METPO:1000457.

The assigned abstract directly states Rubellicoccus peritrichatus CR14T optimum pH 7.6, within the bin, separately from its growth range 6–9. Current official taxonomy and type aliases agree; no full-article phenotype claim is made.

### Native checklist: all works and placements

evidence: supported. Targets: METPO:1000457.

Four assigned works and one explicit supplemental classification work are resolved. Twelve external and four ontology-source placements are covered with actual available surfaces and bounded notice checks.

{
  "completed_at": "2026-10-21T19:20:21.220888+00:00",
  "target": "data/traits/environment/ph_optimum_mid2.yaml",
  "target_sha256": "6e2a9f141a0e75fc3f0f92643724bab5473f925edb95f778dbe9060a9b2e3506",
  "capture": {
    "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2.inspect.json",
    "sha256": "17483fa8b54ef68587431963dab834e8d95e9b24b1534a46431730aaf8b321e4",
    "inputs": 75
  },
  "counts": {
    "works": 4,
    "supplemental_works": 1,
    "literal_reference_forms": 4,
    "external_placements": 12,
    "ontology_source_placements": 4,
    "nodes": 12,
    "edges": 9,
    "snippets": 4,
    "exact_snippets": 3,
    "unverified_snippets": 1,
    "canonical_examples": 1
  },
  "coverage": "Entire current target read; every assigned work, all12 external placements, four ontology-source aliases, all12 nodes/nine edges and four snippet fields accounted for.",
  "source_only_findings": [
    {
      "severity": "major",
      "fields": [
        "synonyms[0]",
        "synonyms[1]"
      ],
      "summary": "The exact aliases Alkali Tolerant and Alkaliphile overstate scientific equivalence to the 7\u20138 external-optimum class.",
      "rationale": "Assigned Krulwich BioC39253 includes an alkaliphile with optimal growth extending to external pH~10.5. Explicit supplemental classification paragraph0 assigns alkali-tolerant optima7\u20139. The terms overlap or include different optimum regimes and are not coextensive with this exact bin. Faithful inheritance from METPO is a separate positive import-fidelity observation.",
      "evidence": [
        "synonym-scope-assessment.json",
        "krulwich-bioc.xml",
        "supplemental-alkali-classification.xml"
      ]
    }
  ],
  "positive_claims": [
    "Canonical CR14T abstract states optimum7.6 and measured range6\u20139; official NCBI3080537 XML confirms species and type-strain aliases. The optimum lies inside7\u20138; the broader growth range is not confused with the optimum.",
    "Three Krulwich snippet occurrences are literal; native results independently agree on those abstract phrases.",
    "Poolman assigned JATS generic paragraphs support existing background statements for buffering, pH-homeostasis regulators and energy relationships at a documentary level. No new mechanism is supplied.",
    "Four assigned DOI identities resolve in fresh indexed metadata; no correction/retraction notice was returned in those responses."
  ],
  "limitations": [
    "No source-only finding at Neutrophile: inspected growth-range/internal-pH language does not establish a precise contradictory external optimum band.",
    "Exact7\u20138 calibration, mild-homeostasis sufficiency and selected habitat generality remain unverified; this audit does not claim a universal mechanism or falsity from missing evidence.",
    "Baker full body was unavailable in retained bounded attempts; current abstract is real but is not full text. Its excerpt is unknown, not proven false. No new retry or exhaustive absence claim.",
    "Canonical phenotype evidence is actual abstract text only; no full-article claim.",
    "Supplemental classification metadata identity and introductory body paragraph0 were read; this additional work is not assigned by the current record. Its original acquisition time is preserved.",
    "Detailed pathogen defense/fitness/AMR, acid-stress interventions and optimization are UNASSESSED_SCOPE, including incidental displayed specific-organism/perturbation material. Generic documentary support is not experimental efficacy verification.",
    "Source auditor does not establish human acceptance or whole-record formal-role validity; those are separate grounding/provenance workstreams.",
    "Publication status is bounded to actual indexed responses, not an exhaustive notice search."
  ],
  "primary_access_provenance": "Original acquisition, current copy and selected-reading completion are separate in reuse-and-copy-receipt.json, taxonomy-copy-receipt.json and selected-primary-reading.json. All retained hashes were checked. No new public request was made by this source auditor.",
  "metadata_read_scope": "Actual abstracts of four fresh assigned works read; supplemental metadata identity/title/DOI inspected alongside actual body classification paragraph.",
  "proposed_followup_scope": "Resolve exact-synonym semantics with maintained ontology/record owners while retaining the quantitative bin, canonical optimum and supported generic context. No biological mechanism, experiment or optimized condition is proposed.",
  "native_check_receipts": "native-check-context.json preserves actual passing results; read-only guessed-filename incident separately retained, not a native or completed-review failure."
}

### Native checklist: four quoted fields

evidence: unknown. Targets: METPO:1000457.

Three repeated Krulwich phrases are literal. The Baker body phrase remains unverified in available scope, not false. Native three VERIFIED/one NOT_IN_ABSTRACT is distinguished from manual source verification.

{
  "completed_at": "2026-10-21T19:19:30.240283+00:00",
  "counts": {
    "occurrences": 4,
    "exact_literal": 3,
    "unknown": 1
  },
  "snippets": [
    {
      "field": "evidence[0].snippet",
      "reference": "DOI:10.1038/nrmicro2549",
      "snippet": "pH homeostasis",
      "status": "exact_literal",
      "locator": "Krulwich actual BioC text and indexed abstract",
      "interpretation": "Literal occurrence is separate from scope/causal sufficiency."
    },
    {
      "field": "causal_graphs[0].edges[0].evidence[0].snippet",
      "reference": "DOI:10.1016/j.tim.2007.02.005",
      "snippet": "proton motive force",
      "status": "unknown_body_unavailable",
      "locator": "Baker indexed abstract lacks this phrase; full body unavailable",
      "interpretation": "Literal occurrence is separate from scope/causal sufficiency."
    },
    {
      "field": "causal_graphs[0].edges[1].evidence[0].snippet",
      "reference": "DOI:10.1038/nrmicro2549",
      "snippet": "pH homeostasis",
      "status": "exact_literal",
      "locator": "Krulwich actual BioC text and indexed abstract",
      "interpretation": "Literal occurrence is separate from scope/causal sufficiency."
    },
    {
      "field": "causal_graphs[0].edges[2].evidence[0].snippet",
      "reference": "DOI:10.1038/nrmicro2549",
      "snippet": "cytoplasmic pH",
      "status": "exact_literal",
      "locator": "Krulwich actual BioC text and indexed abstract",
      "interpretation": "Literal occurrence is separate from scope/causal sufficiency."
    }
  ]
}

### Native checklist: all twelve node referents and native facets

grounding: concern. Targets: METPO:1000457.

Node 8 explicitly describes material components while typed PATHWAY; node 9 describes a reaction class rather than a named enumerable route. These are bounded documentary facet issues. Node 3 is explicit activity, buffering is CAPACITY, PMF is STATE and the permitted GO functional facet does not create a new grounding defect.

[
  {
    "index": 0,
    "field_path": "causal_graphs[0].nodes[0]",
    "current": {
      "node_id": "ph_optimum_mid2_trait",
      "label": "pH optimum mid2",
      "node_type": "TRAIT",
      "grounding": "METPO:1000457",
      "description": "pH optimum approximately 7\u20138."
    },
    "documentary_assessment": "Active METPO:1000457 is a class with inclusive numerical restriction 7\u20138. Current approximately 7\u20138 wording does not introduce a distinct boundary defect.",
    "status": "PASS_OR_BOUNDED",
    "biological_scope": "UNASSESSED_SCOPE for detailed pathogen/acid-defense/fitness/intervention mechanisms; identity and generic documentary facets only"
  },
  {
    "index": 1,
    "field_path": "causal_graphs[0].nodes[1]",
    "current": {
      "node_id": "ph_optimum",
      "label": "pH optimum",
      "node_type": "TRAIT",
      "grounding": "METPO:1000331",
      "description": "External pH supporting maximal growth."
    },
    "documentary_assessment": "Active METPO:1000331 is the exact declared upstream parent; it represents external conditions for efficient growth. No new parent requirement.",
    "status": "PASS_OR_BOUNDED",
    "biological_scope": "UNASSESSED_SCOPE for detailed pathogen/acid-defense/fitness/intervention mechanisms; identity and generic documentary facets only"
  },
  {
    "index": 2,
    "field_path": "causal_graphs[0].nodes[2]",
    "current": {
      "node_id": "slightly_alkaline_external_ph",
      "label": "slightly alkaline external pH",
      "node_type": "ENVIRONMENTAL_FACTOR",
      "description": "External pH 7\u20138, typical of seawater and many host body fluids."
    },
    "documentary_assessment": "Current referent is an external pH condition; ENVIRONMENTAL_FACTOR fits. Generic environmental/host wording does not establish any specific pathogen mechanism.",
    "status": "PASS_OR_BOUNDED",
    "biological_scope": "UNASSESSED_SCOPE for detailed pathogen/acid-defense/fitness/intervention mechanisms; identity and generic documentary facets only"
  },
  {
    "index": 3,
    "field_path": "causal_graphs[0].nodes[3]",
    "current": {
      "node_id": "modest_alkaline_homeostasis",
      "label": "modest alkaline pH homeostasis",
      "node_type": "BIOLOGICAL_PROCESS",
      "description": "Mild K+/H+ antiport and cytoplasmic acidification activity maintaining cytoplasmic pH at slightly basic external pH."
    },
    "documentary_assessment": "Explicit mild antiport and acidification activity is processual. BIOLOGICAL_PROCESS is supported by its stated referent; no inherited demand-amount finding from a sibling applies.",
    "status": "PASS_OR_BOUNDED",
    "biological_scope": "UNASSESSED_SCOPE for detailed pathogen/acid-defense/fitness/intervention mechanisms; identity and generic documentary facets only"
  },
  {
    "index": 4,
    "field_path": "causal_graphs[0].nodes[4]",
    "current": {
      "node_id": "cytoplasmic_buffering_capacity",
      "label": "cytoplasmic buffering capacity",
      "node_type": "CAPACITY",
      "description": "Buffering of the cytoplasm (e.g. phosphate pools) absorbing pH fluctuations."
    },
    "documentary_assessment": "CAPACITY fits the described buffering reservoir/pool. Captured playbook and direct type-normalization writer specifically recognize this current node; no forced retype.",
    "status": "PASS_OR_BOUNDED",
    "biological_scope": "UNASSESSED_SCOPE for detailed pathogen/acid-defense/fitness/intervention mechanisms; identity and generic documentary facets only"
  },
  {
    "index": 5,
    "field_path": "causal_graphs[0].nodes[5]",
    "current": {
      "node_id": "intracellular_ph_homeostasis",
      "label": "intracellular pH homeostasis",
      "node_type": "BIOLOGICAL_PROCESS",
      "description": "Regulation maintaining cytoplasmic pH near neutral."
    },
    "documentary_assessment": "The stated regulation/maintenance is processual. Near-neutral wording is generic contextual scope, not evidence of a universal exact internal setpoint.",
    "status": "PASS_OR_BOUNDED",
    "biological_scope": "UNASSESSED_SCOPE for detailed pathogen/acid-defense/fitness/intervention mechanisms; identity and generic documentary facets only"
  },
  {
    "index": 6,
    "field_path": "causal_graphs[0].nodes[6]",
    "current": {
      "node_id": "na_h_antiporters",
      "label": "Na+/H+ antiporters",
      "node_type": "GENE_OR_PROTEIN",
      "grounding_status": "REVIEWED_LABEL_ONLY",
      "grounding_notes": "Reviewed as a contextual protein or protein-complex label within a quantitative measurement graph; no exact semantic family term was established for this aggregate use.",
      "description": "Sodium:proton antiporters that acidify the cytoplasm when internal pH is too high."
    },
    "documentary_assessment": "Taxon-agnostic protein class with explicit REVIEWED_LABEL_ONLY disposition. No mandatory protein instance or exact family accession is imposed.",
    "status": "PASS_OR_BOUNDED",
    "biological_scope": "UNASSESSED_SCOPE for detailed pathogen/acid-defense/fitness/intervention mechanisms; identity and generic documentary facets only"
  },
  {
    "index": 7,
    "field_path": "causal_graphs[0].nodes[7]",
    "current": {
      "node_id": "k_h_antiporters",
      "label": "K+/H+ antiporters",
      "node_type": "GENE_OR_PROTEIN",
      "description": "Potassium:proton antiporters regulating bacterial internal pH.",
      "grounding": "GO:0015386"
    },
    "documentary_assessment": "Official GO:0015386 is potassium:proton antiporter activity, a molecular_function. Native policy and maintained closeMatch row permit this functional facet for a protein family; this does not convert the protein subject into a process for RO:0002211.",
    "status": "PASS_OR_BOUNDED",
    "biological_scope": "UNASSESSED_SCOPE for detailed pathogen/acid-defense/fitness/intervention mechanisms; identity and generic documentary facets only"
  },
  {
    "index": 8,
    "field_path": "causal_graphs[0].nodes[8]",
    "current": {
      "node_id": "respiratory_proton_pumping",
      "label": "proton-pumping respiratory chain components",
      "node_type": "PATHWAY",
      "description": "Respiratory electron transport chain components that pump protons."
    },
    "documentary_assessment": "Current label and description both identify respiratory chain components, while PATHWAY and the node ID suggest a route/activity. Bounded documentary facet precision is needed; clarify which existing referent is intended without reconstructing machinery.",
    "status": "MINOR_FACET_PRECISION",
    "biological_scope": "UNASSESSED_SCOPE for detailed pathogen/acid-defense/fitness/intervention mechanisms; identity and generic documentary facets only"
  },
  {
    "index": 9,
    "field_path": "causal_graphs[0].nodes[9]",
    "current": {
      "node_id": "metabolite_decarboxylation",
      "label": "metabolite decarboxylation pathways",
      "node_type": "PATHWAY",
      "description": "Decarboxylation reactions whose free-energy change can be stored as PMF."
    },
    "documentary_assessment": "Current description names decarboxylation reactions as a reaction class, not a named enumerable route. The captured PATHWAY convention therefore supports a bounded node-facet precision finding; no new pathway is supplied.",
    "status": "MINOR_FACET_PRECISION",
    "biological_scope": "UNASSESSED_SCOPE for detailed pathogen/acid-defense/fitness/intervention mechanisms; identity and generic documentary facets only"
  },
  {
    "index": 10,
    "field_path": "causal_graphs[0].nodes[10]",
    "current": {
      "node_id": "proton_motive_force",
      "label": "proton motive force",
      "node_type": "STATE",
      "description": "Electrochemical proton gradient (\u0394pH + \u0394\u03c8) across the membrane.",
      "grounding": "METPO:1007500"
    },
    "documentary_assessment": "STATE correctly represents the electrochemical proton gradient rather than its establishment. Local METPO:1007500 proposal is the retained provisional state authority, absent from the pinned upstream release.",
    "status": "PASS_OR_BOUNDED",
    "biological_scope": "UNASSESSED_SCOPE for detailed pathogen/acid-defense/fitness/intervention mechanisms; identity and generic documentary facets only"
  },
  {
    "index": 11,
    "field_path": "causal_graphs[0].nodes[11]",
    "current": {
      "node_id": "f0f1_atp_synthase",
      "label": "F0F1-ATP synthase",
      "node_type": "GENE_OR_PROTEIN",
      "grounding_status": "REVIEWED_LABEL_ONLY",
      "grounding_notes": "Reviewed as a contextual multisubunit ATP-synthase complex in a quantitative pH bin; no one component family represents the whole complex.",
      "description": "Proton-transporting ATP synthase complex that makes ATP from PMF."
    },
    "documentary_assessment": "Whole ATP-synthase complex is a valid protein/complex class with explicit REVIEWED_LABEL_ONLY disposition. A single component accession is not required or substituted.",
    "status": "PASS_OR_BOUNDED",
    "biological_scope": "UNASSESSED_SCOPE for detailed pathogen/acid-defense/fitness/intervention mechanisms; identity and generic documentary facets only"
  }
]

### Native checklist: all nine imported and free relations

consistency: concern. Targets: METPO:1000457.

Edge 5 imports process regulation with a protein subject. Edge 7 imports Biolink material-producer prose with a reaction/pathway subject, while formal endpoints remain NamedThing. Local confers and powers fit their actual proposals; free engages/stabilizes/maintains receive no invented RO restrictions.

[
  {
    "index": 0,
    "field_path": "causal_graphs[0].edges[0]",
    "current": {
      "subject": "slightly_alkaline_external_ph",
      "predicate": "engages",
      "object": "modest_alkaline_homeostasis",
      "description": "Slightly alkaline external pH engages modest alkaline pH-homeostasis.",
      "evidence": [
        {
          "reference": "DOI:10.1016/j.tim.2007.02.005",
          "snippet": "proton motive force",
          "notes": "Supports balanced proton motive force at slightly alkaline pH as the energetic setting of this regime."
        }
      ]
    },
    "status": "PASS_DOCUMENTARY",
    "documentary_assessment": "Free engages connects an external condition to an activity. It has no imported process-domain assertion; source-specific exact-bin causation and detailed biological mechanisms are not certified by this formal check.",
    "biological_scope": "Generic documentary/source context only; detailed acid-defense, pathogen fitness and intervention mechanisms UNASSESSED_SCOPE"
  },
  {
    "index": 1,
    "field_path": "causal_graphs[0].edges[1]",
    "current": {
      "subject": "modest_alkaline_homeostasis",
      "predicate": "confers",
      "object": "ph_optimum_mid2_trait",
      "description": "Modest alkaline pH-homeostasis yields a neutrophile / alkaline-tolerant pH-optimum setpoint.",
      "evidence": [
        {
          "reference": "DOI:10.1038/nrmicro2549",
          "snippet": "pH homeostasis",
          "notes": "Supports the 7\u20138 optimum as the neutrophile / mild-alkaliphile outcome."
        }
      ],
      "predicate_id": "METPO:2007700"
    },
    "status": "PASS_DOCUMENTARY",
    "documentary_assessment": "METPO:2007700 confers explicitly accepts activity/state/material causal subjects and TRAIT objects. This current process-to-trait shape fits; no compulsory universal mechanism is inferred.",
    "biological_scope": "Generic documentary/source context only; detailed acid-defense, pathogen fitness and intervention mechanisms UNASSESSED_SCOPE"
  },
  {
    "index": 2,
    "field_path": "causal_graphs[0].edges[2]",
    "current": {
      "subject": "ph_optimum_mid2_trait",
      "predicate": "is a",
      "object": "ph_optimum",
      "description": "pH optimum mid2 is a quantitative bin of the pH-optimum phenotype.",
      "evidence": [
        {
          "reference": "DOI:10.1038/nrmicro2549",
          "snippet": "cytoplasmic pH",
          "notes": "Supports the 7\u20138 optimum as a value within the pH-optimum distribution."
        }
      ],
      "predicate_id": "rdfs:subClassOf"
    },
    "status": "PASS_DOCUMENTARY",
    "documentary_assessment": "rdfs:subClassOf connects the current bin class to its actual upstream pH-optimum parent. Both are classes; the hierarchy is independently supported by pinned METPO.",
    "biological_scope": "Generic documentary/source context only; detailed acid-defense, pathogen fitness and intervention mechanisms UNASSESSED_SCOPE"
  },
  {
    "index": 3,
    "field_path": "causal_graphs[0].edges[3]",
    "current": {
      "subject": "cytoplasmic_buffering_capacity",
      "predicate": "stabilizes",
      "object": "intracellular_ph_homeostasis",
      "description": "Cytoplasmic buffering capacity stabilizes intracellular pH against fluctuations.",
      "evidence": [
        {
          "reference": "DOI:10.1093/femsre/fuad033",
          "notes": "Buffering capacity of the cytoplasm absorbs pH fluctuations; broad bacterial mechanism supporting near-neutral pHi at external pH 7-8."
        }
      ]
    },
    "status": "PASS_DOCUMENTARY",
    "documentary_assessment": "Free stabilizes imposes no imported domain/range. Buffering reservoir to homeostasis process is an intelligible generic documentary relation; detailed biological applicability remains bounded.",
    "biological_scope": "Generic documentary/source context only; detailed acid-defense, pathogen fitness and intervention mechanisms UNASSESSED_SCOPE"
  },
  {
    "index": 4,
    "field_path": "causal_graphs[0].edges[4]",
    "current": {
      "subject": "na_h_antiporters",
      "predicate": "maintains",
      "object": "intracellular_ph_homeostasis",
      "description": "Na+/H+ antiporters acidify the cytoplasm when pHi is too high, maintaining pH homeostasis.",
      "evidence": [
        {
          "reference": "DOI:10.1093/femsre/fuad033",
          "notes": "Proton-sensing antiporters acidify the cytoplasm by exporting Na+ for protons when internal pH gets too high; general mechanism relevant at external pH 7-8."
        }
      ]
    },
    "status": "PASS_DOCUMENTARY",
    "documentary_assessment": "Free maintains is not RO:0002211 or RO:0002327. Material antiporter class to process is not automatically a formal error.",
    "biological_scope": "Generic documentary/source context only; detailed acid-defense, pathogen fitness and intervention mechanisms UNASSESSED_SCOPE"
  },
  {
    "index": 5,
    "field_path": "causal_graphs[0].edges[5]",
    "current": {
      "subject": "k_h_antiporters",
      "predicate": "regulates",
      "object": "intracellular_ph_homeostasis",
      "description": "K+/H+ antiporters are key regulators of bacterial internal pH.",
      "evidence": [
        {
          "reference": "DOI:10.1093/femsre/fuad033",
          "notes": "Na+/H+ and K+/H+ antiporters are key regulators of bacterial pH homeostasis; general regulator."
        }
      ],
      "predicate_id": "RO:0002211"
    },
    "status": "MAJOR_IMPORTED_ROLE",
    "documentary_assessment": "RO:0002211 directly has BFO:0000015 process domain and range, and its definition describes execution of a regulating process. Object homeostasis is processual; current K+/H+ antiporter subject is a protein class. Allowed GO molecular-function grounding is a semantic facet, not a subject retyping.",
    "biological_scope": "Generic documentary/source context only; detailed acid-defense, pathogen fitness and intervention mechanisms UNASSESSED_SCOPE"
  },
  {
    "index": 6,
    "field_path": "causal_graphs[0].edges[6]",
    "current": {
      "subject": "respiratory_proton_pumping",
      "predicate": "maintains",
      "object": "intracellular_ph_homeostasis",
      "description": "Proton-pumping respiratory chain components prevent the internal pH from becoming too low.",
      "evidence": [
        {
          "reference": "DOI:10.1093/femsre/fuad033",
          "notes": "Activation of proton-pumping respiratory chains prevents internal pH becoming too low; broad statement across respiratory bacteria."
        }
      ]
    },
    "status": "MINOR_NODE_FACET_CONTEXT",
    "documentary_assessment": "Free maintains carries no imported process restriction. The bounded concern is node 8 components-versus-route wording/type, not a claimed invalid free relation or disproved mechanism.",
    "biological_scope": "Generic documentary/source context only; detailed acid-defense, pathogen fitness and intervention mechanisms UNASSESSED_SCOPE"
  },
  {
    "index": 7,
    "field_path": "causal_graphs[0].edges[7]",
    "current": {
      "subject": "metabolite_decarboxylation",
      "predicate": "generates",
      "object": "proton_motive_force",
      "description": "Metabolite decarboxylation pathways store free energy as proton motive force.",
      "evidence": [
        {
          "reference": "DOI:10.1093/femsre/fuad033",
          "notes": "The free energy change from decarboxylation reactions can be stored as a proton motive force; general, not taxon-specific."
        }
      ],
      "predicate_id": "biolink:produces"
    },
    "status": "MAJOR_TEXTUAL_RELATION_SEMANTICS",
    "documentary_assessment": "Biolink produces is defined for a material entity whose functioning generates a product. Current subject is a pathway/reaction class, so its imported meaning is mismatched. Formal inherited domain and range remain named thing; neither a formal material-only domain nor a material-only product range is asserted. Retyping this reaction class to BIOLOGICAL_PROCESS alone would not fix the subject meaning.",
    "biological_scope": "Generic documentary/source context only; detailed acid-defense, pathogen fitness and intervention mechanisms UNASSESSED_SCOPE"
  },
  {
    "index": 8,
    "field_path": "causal_graphs[0].edges[8]",
    "current": {
      "subject": "proton_motive_force",
      "predicate": "powers",
      "object": "f0f1_atp_synthase",
      "description": "Proton motive force powers F0F1-ATP synthase ATP synthesis.",
      "evidence": [
        {
          "reference": "DOI:10.1093/femsre/fuad033",
          "notes": "The proton motive force can be used by F0F1-ATP synthase to make ATP; strong general bioenergetic edge."
        }
      ],
      "predicate_id": "METPO:2007900"
    },
    "status": "PASS_DOCUMENTARY",
    "documentary_assessment": "METPO:2007900 powers explicitly models an energetic driver operating a molecular machine. Current STATE to GENE_OR_PROTEIN meets the v10 local gate and the proposed meaning; it is only closeMatch to RO:0002327, not identical to its process-object constraint.",
    "biological_scope": "Generic documentary/source context only; detailed acid-defense, pathogen fitness and intervention mechanisms UNASSESSED_SCOPE"
  }
]

### Native checklist: generic attribution and detailed biological exclusions

scope: unknown. Targets: METPO:1000457.

Existing generic Poolman environmental/homeostasis attribution remains positive, distinct from calibration of the exact bin or universal mechanism. Detailed pathogen acid-defense, fitness, AMR, perturbation and intervention mechanisms remain UNASSESSED_SCOPE; no repaired route, efficacy claim or optimization is provided.

{
  "completed_at": "2026-10-21T19:19:30.240283+00:00",
  "edges": [
    {
      "index": 0,
      "field": "causal_graphs[0].edges[0]",
      "subject": "slightly_alkaline_external_ph",
      "predicate": "engages",
      "object": "modest_alkaline_homeostasis",
      "reference": "DOI:10.1016/j.tim.2007.02.005",
      "status": "unknown",
      "source": "baker",
      "locator": "indexed abstract only",
      "assessment": "Baker abstract concerns acidophile pH homeostasis and does not establish slightly alkaline engagement or the exact current excerpt. Full body unavailable; no false-citation or false-quote finding solely from that limit.",
      "scope": "Generic statement/attribution and literal evidence only; detailed pathogen fitness, defense, AMR, interventions and optimization UNASSESSED_SCOPE."
    },
    {
      "index": 1,
      "field": "causal_graphs[0].edges[1]",
      "subject": "modest_alkaline_homeostasis",
      "predicate": "confers",
      "object": "ph_optimum_mid2_trait",
      "reference": "DOI:10.1038/nrmicro2549",
      "status": "supported_context_exact_bin_unverified",
      "source": "krulwich",
      "locator": "BioC58/671",
      "assessment": "Krulwich supports general pH homeostasis. The short excerpt does not establish a particular modest-homeostasis regime as sufficient for an external optimum of 7\u20138. Retain this as bounded calibration uncertainty, distinct from the concrete exact-synonym scope finding.",
      "scope": "Generic statement/attribution and literal evidence only; detailed pathogen fitness, defense, AMR, interventions and optimization UNASSESSED_SCOPE."
    },
    {
      "index": 2,
      "field": "causal_graphs[0].edges[2]",
      "subject": "ph_optimum_mid2_trait",
      "predicate": "is a",
      "object": "ph_optimum",
      "reference": "DOI:10.1038/nrmicro2549",
      "status": "context_only_hierarchy_grounded_elsewhere",
      "source": "krulwich",
      "locator": "BioC58/671",
      "assessment": "General pH discussion is context, not the formal source for the exact bin subclass. Current captured METPO hierarchy is assessed by grounding auditor; the source is not falsely described as empirical proof of that taxonomy.",
      "scope": "Generic statement/attribution and literal evidence only; detailed pathogen fitness, defense, AMR, interventions and optimization UNASSESSED_SCOPE."
    },
    {
      "index": 3,
      "field": "causal_graphs[0].edges[3]",
      "subject": "cytoplasmic_buffering_capacity",
      "predicate": "stabilizes",
      "object": "intracellular_ph_homeostasis",
      "reference": "DOI:10.1093/femsre/fuad033",
      "status": "generic_documentary_support",
      "source": "poolman",
      "locator": "body paragraph4 generic opening clause",
      "assessment": "The assigned text explicitly describes cytoplasmic buffering absorbing fluctuations. It does not calibrate a 7\u20138 optimum. Detailed organism-specific efficacy remains unassessed.",
      "scope": "Generic statement/attribution and literal evidence only; detailed pathogen fitness, defense, AMR, interventions and optimization UNASSESSED_SCOPE."
    },
    {
      "index": 4,
      "field": "causal_graphs[0].edges[4]",
      "subject": "na_h_antiporters",
      "predicate": "maintains",
      "object": "intracellular_ph_homeostasis",
      "reference": "DOI:10.1093/femsre/fuad033",
      "status": "generic_documentary_support",
      "source": "poolman",
      "locator": "body paragraph4 generic antiporter clause",
      "assessment": "The assigned generic background sentence matches the current direction of the existing antiporter claim. No organism-specific defense mechanism or intervention is validated.",
      "scope": "Generic statement/attribution and literal evidence only; detailed pathogen fitness, defense, AMR, interventions and optimization UNASSESSED_SCOPE."
    },
    {
      "index": 5,
      "field": "causal_graphs[0].edges[5]",
      "subject": "k_h_antiporters",
      "predicate": "regulates",
      "object": "intracellular_ph_homeostasis",
      "reference": "DOI:10.1093/femsre/fuad033",
      "status": "generic_documentary_support",
      "source": "poolman",
      "locator": "body paragraph1 overview",
      "assessment": "The assigned overview calls the listed antiporters regulators of bacterial pH homeostasis. This is generic contextual support, not proof of this bin or a particular protein.",
      "scope": "Generic statement/attribution and literal evidence only; detailed pathogen fitness, defense, AMR, interventions and optimization UNASSESSED_SCOPE."
    },
    {
      "index": 6,
      "field": "causal_graphs[0].edges[6]",
      "subject": "respiratory_proton_pumping",
      "predicate": "maintains",
      "object": "intracellular_ph_homeostasis",
      "reference": "DOI:10.1093/femsre/fuad033",
      "status": "generic_documentary_support",
      "source": "poolman",
      "locator": "body paragraph4 generic respiratory clause",
      "assessment": "The assigned background passage supports the current broad respiratory-homeostasis statement at documentary level. Formal PATHWAY/material-component referents are left to the grounding audit.",
      "scope": "Generic statement/attribution and literal evidence only; detailed pathogen fitness, defense, AMR, interventions and optimization UNASSESSED_SCOPE."
    },
    {
      "index": 7,
      "field": "causal_graphs[0].edges[7]",
      "subject": "metabolite_decarboxylation",
      "predicate": "generates",
      "object": "proton_motive_force",
      "reference": "DOI:10.1093/femsre/fuad033",
      "status": "generic_documentary_support",
      "source": "poolman",
      "locator": "body paragraph5",
      "assessment": "The assigned background states that decarboxylation free energy can be stored as PMF. The generic observation does not establish exact-bin specificity or universal sufficiency; detailed biological efficacy is unassessed.",
      "scope": "Generic statement/attribution and literal evidence only; detailed pathogen fitness, defense, AMR, interventions and optimization UNASSESSED_SCOPE."
    },
    {
      "index": 8,
      "field": "causal_graphs[0].edges[8]",
      "subject": "proton_motive_force",
      "predicate": "powers",
      "object": "f0f1_atp_synthase",
      "reference": "DOI:10.1093/femsre/fuad033",
      "status": "generic_documentary_support",
      "source": "poolman",
      "locator": "body paragraph5",
      "assessment": "The assigned background supports the existing generic PMF/ATP-synthase relationship. No exact family, organism or acid-defense intervention claim is validated.",
      "scope": "Generic statement/attribution and literal evidence only; detailed pathogen fitness, defense, AMR, interventions and optimization UNASSESSED_SCOPE."
    }
  ],
  "detailed_biology_scope": "No detailed pathogen or intervention efficacy assessed. Generic clauses may be documentary-supported without establishing an exact numeric optimum."
}

### Native checklist: whole record and optional evidence

completeness: supported. Targets: METPO:1000457.

All twelve nodes, nine edges, three components, three protein classes, two reviewed label-only classes, zero instances, one canonical and thirteen events are covered. No token instance, exact protein family, connector or dataset is required by this NONMECHANISTIC record.

{
  "completed_at": "2026-10-21T19:19:30.240283+00:00",
  "nodes": [
    {
      "index": 0,
      "node_id": "ph_optimum_mid2_trait",
      "label": "pH optimum mid2",
      "node_type": "TRAIT",
      "status": "quantitative_identity",
      "assessment": "Current exact quantitative bin comes from captured ontology; generic sources do not independently calibrate it.",
      "incident_edges": [
        1,
        2
      ],
      "direct_node_evidence_present": false
    },
    {
      "index": 1,
      "node_id": "ph_optimum",
      "label": "pH optimum",
      "node_type": "TRAIT",
      "status": "measurement_identity",
      "assessment": "External growth optimum differs from intracellular setpoint; the source preserves that distinction.",
      "incident_edges": [
        2
      ],
      "direct_node_evidence_present": false
    },
    {
      "index": 2,
      "node_id": "slightly_alkaline_external_ph",
      "label": "slightly alkaline external pH",
      "node_type": "ENVIRONMENTAL_FACTOR",
      "status": "qualified_context",
      "assessment": "Near-neutral/slightly alkaline external context is general; no full support claim for every named habitat/body-fluid example or a universal7\u20138 band.",
      "incident_edges": [
        0
      ],
      "direct_node_evidence_present": false
    },
    {
      "index": 3,
      "node_id": "modest_alkaline_homeostasis",
      "label": "modest alkaline pH homeostasis",
      "node_type": "BIOLOGICAL_PROCESS",
      "status": "context_exact_bin_unverified",
      "assessment": "General homeostasis context is supported; specific mildness, causal sufficiency and phenotype calibration are not established by the short sources.",
      "incident_edges": [
        0,
        1
      ],
      "direct_node_evidence_present": false
    },
    {
      "index": 4,
      "node_id": "cytoplasmic_buffering_capacity",
      "label": "cytoplasmic buffering capacity",
      "node_type": "CAPACITY",
      "status": "generic_documentary_support",
      "assessment": "Poolman paragraph4 generic buffering-capacity statement supports the described capacity.",
      "incident_edges": [
        3
      ],
      "direct_node_evidence_present": false
    },
    {
      "index": 5,
      "node_id": "intracellular_ph_homeostasis",
      "label": "intracellular pH homeostasis",
      "node_type": "BIOLOGICAL_PROCESS",
      "status": "generic_documentary_support",
      "assessment": "Generic pH-homeostasis context supported; near-neutral language is typical context, not universal exact numeric state.",
      "incident_edges": [
        3,
        4,
        5,
        6
      ],
      "direct_node_evidence_present": false
    },
    {
      "index": 6,
      "node_id": "na_h_antiporters",
      "label": "Na+/H+ antiporters",
      "node_type": "GENE_OR_PROTEIN",
      "status": "generic_documentary_support",
      "assessment": "Existing generic antiporter wording appears in assigned background; detailed organism-specific efficacy not assessed.",
      "incident_edges": [
        4
      ],
      "direct_node_evidence_present": false
    },
    {
      "index": 7,
      "node_id": "k_h_antiporters",
      "label": "K+/H+ antiporters",
      "node_type": "GENE_OR_PROTEIN",
      "status": "generic_documentary_support",
      "assessment": "Existing generic regulator wording appears in assigned overview; specific GO interpretation belongs to grounding auditor.",
      "incident_edges": [
        5
      ],
      "direct_node_evidence_present": false
    },
    {
      "index": 8,
      "node_id": "respiratory_proton_pumping",
      "label": "proton-pumping respiratory chain components",
      "node_type": "PATHWAY",
      "status": "generic_documentary_support",
      "assessment": "Respiratory-component background appears in source; pathway/material referent is a separate formal question.",
      "incident_edges": [
        6
      ],
      "direct_node_evidence_present": false
    },
    {
      "index": 9,
      "node_id": "metabolite_decarboxylation",
      "label": "metabolite decarboxylation pathways",
      "node_type": "PATHWAY",
      "status": "generic_documentary_support",
      "assessment": "Existing generic decarboxylation/energy-background statement has documentary support; no biological reconstruction.",
      "incident_edges": [
        7
      ],
      "direct_node_evidence_present": false
    },
    {
      "index": 10,
      "node_id": "proton_motive_force",
      "label": "proton motive force",
      "node_type": "STATE",
      "status": "generic_documentary_support",
      "assessment": "Actual generic PMF definitions preserve its electrochemical-gradient meaning.",
      "incident_edges": [
        7,
        8
      ],
      "direct_node_evidence_present": false
    },
    {
      "index": 11,
      "node_id": "f0f1_atp_synthase",
      "label": "F0F1-ATP synthase",
      "node_type": "GENE_OR_PROTEIN",
      "status": "generic_documentary_support",
      "assessment": "Existing generic synthase/PMF relation has documentary support; no protein instance or particular mechanism established.",
      "incident_edges": [
        8
      ],
      "direct_node_evidence_present": false
    }
  ]
}

### Native checklist: canonical-only catalog applicability

evidence: not_applicable. Targets: METPO:1000457.

No Rubellicoccus peritrichatus, Puniceicoccus sp. CR14 or verified type-strain alias matches the complete retained 20-organism/28-dataset catalog. No different organism or strain was substituted, and no detailed defense gene/module query was made.

### Native checklist: actual maintained recurrence and history

provenance: supported. Targets: METPO:1000457.

The predicate table and empty-ID grounder own mapping recurrence while preserving existing IDs. The current PMF and buffering type writer is a direct owner; the PATHWAY migration has neither current node 8 nor node 9 as an exact key, so it is context only for their facet finding. Canonical and functional-ground writers retain their exact guards.

{
  "completed_at": "2026-10-21T19:21:49.579415+00:00",
  "target": "data/traits/environment/ph_optimum_mid2.yaml",
  "counts": {
    "inputs": 75,
    "graphs": 1,
    "nodes": 12,
    "edges": 9,
    "components": 3,
    "protein_classes": 3,
    "label_only": 2,
    "protein_instances": 0,
    "canonical_examples": 1,
    "curation_events": 13,
    "ai_events": 12,
    "seed_events": 1,
    "captured_histories": 5,
    "matching_files": 180,
    "review_target_arrays": 67,
    "exact_target_arrays": 0
  },
  "search": {
    "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-grounding-agent/search-and-provenance.json",
    "sha256": "dbd38be5e966cfc4472faae4e6671db1ff85d1365dfd3895ec6b231b742a30fd",
    "bytes": 91862
  },
  "all_node_search": {
    "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-grounding-agent/all-node-owner-search.json",
    "sha256": "38df7d4f032ee61d9255502dc191cc07cadb45629f4ebd8f56c023b425a6ed05",
    "bytes": 21206
  },
  "history": {
    "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-grounding-agent/history-projections.json",
    "sha256": "b04a3b26888487b34a29d2d05d4cb128e72f294dda183965cabbec1cdbd59120",
    "bytes": 17794
  },
  "bounded_human_acceptance": "The exact target/ID/label/unique-bin-synonym case-insensitive ignored-inclusive repository search yielded 180 matching files and 67 parsed structured-review target arrays, with zero exact current-target arrays and no parse failures. Five captured histories were fully read; their actors are AI and they concern infrastructure/shared contexts. The 13 in-record events comprise 12 explicitly AI-assisted events and a machine seed. A linked current human acceptance/maintained signoff was not established within this stated repository scope; this is not a universal claim that no human ever reviewed the work.",
  "positive_provenance": "Current REVIEWED status, explicit curation history, mapped functional facets, normalization and canonical writer provenance remain positive. AI provenance is not erased or characterized as absent.",
  "history_dispositions": [
    {
      "path": "history/infrastructure/inconsistent-node-type/2026-08-12T000912Z-claude-code-779670.yaml",
      "sha256": "adb240d907348b52784c5e2f2e4b131af124877eeaaf1805c94713342763e5dd",
      "actors": [
        {
          "type": "ai_agent",
          "name": "claude-code"
        }
      ],
      "classification": "AI infrastructure/shared context, not exact target human signoff"
    },
    {
      "path": "history/infrastructure/node-type-consistency/2026-08-15T014631Z-claude-code-9d7f4d.yaml",
      "sha256": "21f19561c0d4769e7acc62e05e41d0d395a0f239938f00829f79f2b9c3ac2510",
      "actors": [
        {
          "type": "ai_agent",
          "name": "claude-code"
        }
      ],
      "classification": "AI infrastructure/shared context, not exact target human signoff"
    },
    {
      "path": "history/infrastructure/pathway-vs-process/2026-08-16T010630Z-claude-code-192557.yaml",
      "sha256": "a45fff0e3ef24effb20c3b624dc14a6cab08f2094bc0f8033cd709c0cd60f012",
      "actors": [
        {
          "type": "ai_agent",
          "name": "claude-code"
        }
      ],
      "classification": "AI infrastructure/shared context, not exact target human signoff"
    },
    {
      "path": "history/infrastructure/predicate-gate-audit/2026-08-16T074719Z-claude-code-84d88d.yaml",
      "sha256": "d1ba848e155dbd3a65905f07af5539d3d22b8873b638cc6adb48b1a0e23c0a3d",
      "actors": [
        {
          "type": "ai_agent",
          "name": "claude-code"
        }
      ],
      "classification": "AI infrastructure/shared context, not exact target human signoff"
    },
    {
      "path": "history/other/canonical-examples-six/2026-08-21T065406Z-codex-a1ab82.yaml",
      "sha256": "23be5f6ab519511e3e23feffa85813eec4fa3c7e6b900e77fd4a3adc0c26da0e",
      "actors": [
        {
          "type": "ai_agent",
          "name": "codex",
          "model": "gpt-5",
          "agent_tool": "codex"
        }
      ],
      "classification": "AI infrastructure/shared context, not exact target human signoff"
    }
  ],
  "owners": [
    {
      "path": "data/traits/environment/ph_optimum_mid2.yaml",
      "role": "Primary owner of current aliases, node wording/type, imported edge choices and acceptance traceability.",
      "sha256": "6e2a9f141a0e75fc3f0f92643724bab5473f925edb95f778dbe9060a9b2e3506"
    },
    {
      "path": "mappings/predicate_grounding.tsv",
      "role": "Maintained rows 11 regulates and 24 generates supply the imported edge meanings with wildcard gates; row 102 confers and row 111 powers are explicitly gated local mappings. A wildcard local gate does not establish external ontology compatibility.",
      "sha256": "8e28c19e93aca3dc164a3befbe2612b289241de457c59f499e65936c03b7ce52"
    },
    {
      "path": "scripts/ground_causal_predicates.py",
      "role": "Recurrence owner for filling missing predicate IDs; skips every existing nonempty predicate_id. Mapping corrections alone would not repair current edges 5/7.",
      "sha256": "5a788eeaabf3a56b0d82c469a3e3fe28f1d51707d9382313b9a94289be7d1381"
    },
    {
      "path": "mappings/node_grounding.tsv",
      "role": "Row 279 permits K+/H+ protein-family closeMatch to GO:0015386; supports valid functional facet, not process retyping.",
      "sha256": "d7de9b3ab04960c4775a5bc295a945bd1a72d81467830459f4793e654f82b3d0"
    },
    {
      "path": "scripts/ground_causal_nodes.py",
      "role": "Fills missing node grounds, skips existing nonempty grounds and respects reviewed label-only status. Current GO ground is preserved.",
      "sha256": "204ce4162544154b1752b65da2136538847ea25ced26a52f5708eadff08f5d42"
    },
    {
      "path": "scripts/migrate_uniprot_instance_groundings.py",
      "role": "Exact case-folded K+/H+ label replacement to GO:0015386; applies only when existing ground begins UniProtKB. Current GO grounding is already a no-op.",
      "sha256": "07d2a5405cff5857239757e0a3791f411b1d25709a5760c1e49553eed066993d"
    },
    {
      "path": "scripts/migrate_node_type_consistency.py",
      "role": "Direct current PMF\u2192STATE and cytoplasmic buffering\u2192CAPACITY RETYPE owner. It does not contain respiratory_proton_pumping or metabolite_decarboxylation as exact keys, so it is not assigned recurrence ownership of the facet finding.",
      "sha256": "a3e7bc170e60f406a73e06c893d74f5253671028d3d40cc15ecf882b6684a69e"
    },
    {
      "path": "scripts/migrate_pathway_vs_process.py",
      "role": "Convention and analogous reaction-class context only: TARGET contains electron_transport_chain, aa_decarboxylation and amino_acid_decarboxylation, but not either current node 8/9 key. Do not claim it currently rewrites those nodes.",
      "sha256": "f236de7183048732e9001b7fac4367affff58d8b7a7d5c63286e6b058a4b38c2"
    },
    {
      "path": "scripts/backfill_canonical_examples_444.py",
      "role": "Direct current canonical source/note table entry. Guarded live queue, exact-existing-example no-op and nonempty-drift rejection preserve its provenance.",
      "sha256": "18ca0766789c239d693ef665e8b1d43c1209a0f414a326f1c5d890f88de7b20c"
    },
    {
      "path": "research/traits/environment/ph_optimum_mid2-deep-research-falcon.md",
      "role": "Current August 4 Falcon report is contextual provenance, not proof that its exact current bytes were the June 23 enrichment input. No paid run or mechanistic recommendations adopted.",
      "sha256": "fd8bcade02db10fa4fe369f18863f876ac8c5bbc6559ff0d2d8ca29d00fca738"
    }
  ],
  "readiness": "The NONMECHANISTIC quantitative graph does not require token protein instances, extra connectors or mandatory expression datasets. Three protein classes, two reviewed label-only dispositions and zero instances are legitimate retained coverage. Three disconnected components are documented, not an automatic finding.",
  "proposed_facet_owner": [
    "data/traits/environment/ph_optimum_mid2.yaml"
  ],
  "proposed_relation_owners": [
    "data/traits/environment/ph_optimum_mid2.yaml",
    "mappings/predicate_grounding.tsv",
    "scripts/ground_causal_predicates.py"
  ],
  "proposed_human_owner": [
    "data/traits/environment/ph_optimum_mid2.yaml"
  ]
}

### Native checklist: bounded human acceptance traceability

provenance: concern. Targets: METPO:1000457.

Ignored-inclusive exact target/ID/label search found 180 files, 67 actual structured-review target arrays and zero exact target arrays. Thirteen record events comprise twelve AI events and a machine seed; five captured histories were fully read and have AI actors. Positive provenance and REVIEWED do not identify a linked human acceptance decision within this bounded scope.

### Native checklist: actual focused checks and qualified common reuse

consistency: supported. Targets: METPO:1000457.

Native, strict and snippet checks passed directly; all 75 captured inputs and frozen manifests match. B10 common results retain original failures, retries, skips and timestamps, with actual B11 byte qualification and independent verification; no new B11 final QC execution is claimed.

## Findings

### exact-alias-scope: Two exact aliases are not coextensive with the 7–8 optimum class

major / open / confirmed; issue key: ph-optimum-mid2-exact-alias-scope.

Actual assigned Krulwich classification includes an alkaliphile with optimum extending to about pH 10.5, and the explicit supplemental classification uses 7–9 for alkali-tolerant optima. Both exceed this numerical class. Faithful upstream import is positive provenance, not proof of scientific equivalence. No Neutrophile defect or universal nomenclature rule is added.

### imported-relation-subjects: Imported process and material-producer relations have mismatched subjects

major / open / confirmed; issue key: ph-optimum-mid2-imported-relation-subjects.

RO:0002211 requires a regulating process; the current K+/H+ antiporter subject is a protein class despite its allowed functional GO grounding. Biolink produces describes a material producer, while the current decarboxylation subject is a reaction/pathway. The latter is a textual semantic conflict; its inherited formal endpoints remain named thing and no material-only product range is asserted.

### pathway-referent-precision: Two PATHWAY nodes need bounded referent precision

minor / open / confirmed; issue key: ph-optimum-mid2-pathway-referent-precision.

Node 8 names respiratory chain components as material entities while its type and ID suggest a route/activity. Node 9 describes a reaction class while the native PATHWAY convention distinguishes named enumerable routes. Clarify the intended existing referents without reconstructing a pathway or assigning biological falsity. No exact recurrence key for these two nodes was established in the contextual migration writer.

### human-acceptance-link: Bounded local provenance lacks a linked human acceptance decision

minor / open / confirmed; issue key: ph-optimum-mid2-human-acceptance-link.

The 180-path/67-array/zero-exact search, thirteen record events and five AI histories preserve positive maintenance provenance but do not identify attributable current human scientific acceptance. This bounded result does not assert absence of remote or private decisions.

## Recommended Actions And Acceptance Checks

### reconcile-exact-aliases

Reconcile or qualify the two exact aliases during separately authorized curation while preserving the active numerical class.

- Preserve the faithful pinned-METPO import and the positive canonical optimum; distinguish source classification conventions from whole-bin equivalence.
- Limit the confirmed fields to synonyms 0/1 unless new evidence supports further change.
- Use guarded record/repository history, applicable native/strict/identity checks and a successor review after changed inputs.

### reconcile-imported-roles

Reconcile the imported edge meanings with the represented subjects during authorized curation.

- Distinguish the firm RO process domain from Biolink textual material-subject meaning and broad formal endpoints; preserve allowed GO functional grounding.
- Inspect empty-ID refill and nonempty-ID preservation so mapping edits are not misrepresented as repairing current edges.
- Do not prescribe a new biological pathway, intervention, experimental condition or efficacy claim; use guarded history and appropriate native/strict/QC checks.

### clarify-node-facets

Clarify the two existing PATHWAY referents against the native convention.

- Document whether node 8 intends existing components or a route/activity, and whether node 9 denotes a reaction class or a named route. Review incident relations consistently.
- The current record is the established owner; the pathway migration is context, not a proven direct-key recurrence writer.
- Do not add a token protein, new mechanism, forced connector or optimization; preserve source meaning and guarded history.

### link-human-acceptance

Link attributable human acceptance if available, or clarify status while preserving bounded uncertainty.

- Retain the 180/67/0 ignored-inclusive basis and distinguish thirteen record events from five fully read AI histories.
- Do not infer human acceptance from AI maintenance, REVIEWED, validators or ontology authorship.
- No contact with other people or automatic status promotion is authorized by this proposed action.

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
| check-ph-optimum-mid2-native | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-native.log; Executed 2026-10-21T19:16:35.094566+00:00 through 2026-10-21T19:16:35.804540+00:00; metadata ph-optimum-mid2-native.json | context_only | Direct pass at 19:16:35.094566–19:16:35.804540 UTC; shape validity is separate from scientific support. |
| check-ph-optimum-mid2-strict | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-strict.log; Executed 2026-10-21T19:16:35.096817+00:00 through 2026-10-21T19:16:36.193502+00:00; metadata ph-optimum-mid2-strict.json | context_only | Direct pass at 19:16:35.096817–19:16:36.193502 UTC with zero error rows. |
| check-ph-optimum-mid2-snippets | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-snippets.log; Executed 2026-10-21T19:16:38.115487+00:00 through 2026-10-21T19:16:42.292545+00:00; metadata ph-optimum-mid2-snippets.json | context_only | Direct pass at 19:16:38.115487–19:16:42.292545 UTC: four fields over two references, three VERIFIED and one NOT_IN_ABSTRACT. Manual primary assessment independently finds three literal phrases and one Baker body-unverified phrase. |
| check-batch010-qc | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/batch010-qc.log; Executed 2026-10-21T19:06:27.731868+00:00 through 2026-10-21T19:08:11.219124+00:00; metadata batch010-qc.json | context_only | Actual B10 19:06:27.731868–19:08:11.219124 UTC pass, qualified against B11 bytes; not a new B11 execution. |
| record | data/traits/environment/ph_optimum_mid2.yaml; Entire current target | supports | Twelve nodes, nine edges, three components, three protein classes including two label-only classes, zero instances, one canonical and thirteen record events are covered. |
| policy | docs/GROUNDING_POLICY.md; Captured maintained authority | supports | Taxon-agnostic GO molecular-function facets are allowed for enzyme classes; reviewed label-only classes and absent optional instances are legitimate. |
| playbook | docs/CURATION_PLAYBOOK.md; Captured maintained authority | supports | Named enumerable routes differ from reaction classes; reservoir and state facets remain distinct. AI maintenance does not establish human acceptance. |
| schema | src/traitmech/schema/traitmech.yaml; Captured maintained authority | supports | Current process, pathway, state, material protein and capacity meanings. |
| checklist | .claude/skills/curate-yaml-record/references/review-checklist.md; Captured maintained authority | supports | Whole-record identity, sources, nodes, edges, ownership, provenance, optional coverage and readiness checklist. |
| reuse | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-b10-qc-supplement-qualified.json; Actual qualified B10-to-B11 byte reuse | supports | All 1,130 traits, 1,278 history files and nineteen common inputs match; original diagnostic failures, retries and skips remain distinct from actual B10 gates and B11 qualification. |
| reuse-postcheck | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-output-verification-agent/post-execution-verification.json; Independent actual qualification verification | supports | The postcheck verifies actual input and native-output bindings without repeating QC. |
| capture | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-grounding-agent/capture-verification.json; Derived assessment or read/access receipt; actual primary surface remains separate | supports | All 75 captured inputs match, with whole-target reading before judgment. |
| identity | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-grounding-agent/identity-assessment.json; Derived assessment or read/access receipt; actual primary surface remains separate | supports | Active identity, inclusive 7–8 restriction, direct parent and explicit obsolete replacement; current official taxonomy and permissible GO facet. |
| node-edges | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-grounding-agent/node-edge-ledger.json; Derived assessment or read/access receipt; actual primary surface remains separate | supports | Every current node and edge, three components, firm imported-role and bounded facet distinctions. |
| owners | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-grounding-agent/owner-provenance-assessment.json; Derived assessment or read/access receipt; actual primary surface remains separate | supports | Exact maintained recurrence, five fully read AI histories, 180-path/67-array/zero-exact bounded human-acceptance search. |
| expression | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-grounding-agent/expression-applicability.json; Derived assessment or read/access receipt; actual primary surface remains separate | supports | Canonical species/historical/type aliases absent from the complete retained 20-organism/28-dataset catalog; no substitutes or downstream defense query. |
| authority-reuse | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-grounding-agent/authority-reuse-receipts.json; Derived assessment or read/access receipt; actual primary surface remains separate | supports | Catalog and runner receipts retain original acquisition times separately from present copying. |
| local-authority | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-grounding-agent/local-authority-excerpts.json; Derived assessment or read/access receipt; actual primary surface remains separate | supports | Actual v3 PMF, v8 confers, v10 powers, native mappings and Biolink inheritance. |
| ground-reading | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-grounding-agent/primary-reading-scope.json; Derived assessment or read/access receipt; actual primary surface remains separate | supports | Actual selected authority, full-target and five full-history reading scopes; read-only failed projections retained as corrected access limitations. |
| ground-manifest | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-grounding-agent/evidence-manifest.json; Derived assessment or read/access receipt; actual primary surface remains separate | supports | Twenty-one frozen grounding artifacts with verified hashes. |
| metpo-primary | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/repo/data/raw/metpo.owl; Actual METPO:1000457, 1000331 and obsolete 0000179 XML | supports | Active numerical class is inclusive 7–8, with direct parent 1000331 and explicit obsolete 0000179 replacement. The aliases are faithfully imported; semantic equivalence is separately assessed. |
| ro-primary | /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/ro.db; RO:0002211 direct definition, BFO:0000015 domain and range | supports | Regulation is processual. Current antiporter class remains material despite permissible functional grounding, while its homeostasis object is a process. |
| biolink-primary | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/repo/data/raw/biolink-model.yaml; produces and its full related-to inheritance chain | supports | The prose definition requires a material producer, while inherited formal domain and range are named thing. No hard material-only product range is inferred. |
| go-primary | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-grounding-agent/go0015386.response; Actual current official response | supports | Official GO:0015386 is potassium:proton antiporter activity in molecular_function. Native closeMatch functional grounding is allowed, without changing the represented protein subject into a process. |
| taxonomy-primary | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-grounding-agent/taxon3080537.xml; Actual current official response | supports | Official species Rubellicoccus peritrichatus includes Puniceicoccus sp. CR14 and type-strain aliases CR14, KCTC 72139 and MCCC 1K03845; taxonomy is distinct from the phenotype measurement. |
| meta-krulwich | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/krulwich-metadata.json; Actual indexed metadata surface | supports | Actual assigned publication identity, abstract and returned notice fields only; later primary-body observations are separately bound. |
| meta-baker | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/baker-metadata.json; Actual indexed metadata surface | supports | Actual assigned publication identity, abstract and returned notice fields only; later primary-body observations are separately bound. |
| meta-poolman | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/poolman-metadata.json; Actual indexed metadata surface | supports | Actual assigned publication identity, abstract and returned notice fields only; later primary-body observations are separately bound. |
| meta-canonical | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/canonical-metadata.json; Actual indexed metadata surface | supports | Actual canonical abstract states CR14T optimum pH 7.6 and separate growth range 6–9; no whole-body claim. |
| meta-supplemental-alkali-classification | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/supplemental-alkali-classification-metadata.json; Actual indexed metadata surface | supports | Explicit supplemental publication identity/title; not a current assigned reference and not body evidence under metadata timing. |
| body-krulwich-bioc.xml | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/krulwich-bioc.xml; Selected primary surface with original acquisition time | supports | Selected generic pH/PMF and external-versus-internal classification passages. Detailed pathogen/perturbation mechanisms are not assessed. |
| body-krulwich-publisher.html | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/krulwich-publisher.html; Selected primary surface with original acquisition time | supports | Retained publisher surface for generic classification and literal terms; no full-article mechanistic reading claim. |
| body-supplemental-alkali-classification.xml | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/supplemental-alkali-classification.xml; Selected primary surface with original acquisition time | supports | Introductory body paragraph 0 provides a stated alkali-tolerant optimum convention; this explicitly supplemental work is not assigned by the record. |
| body-homeostasis.xml | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/homeostasis.xml; Selected primary surface with original acquisition time | supports | Selected generic JATS paragraphs 0, 1, 4, 5 and 6 support existing background attribution, distinct from exact-bin calibration and detailed defense efficacy. |
| alkaliphile-scope | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/krulwich-bioc.xml; BioC offset 39253, classification counterexample only | refutes | The assigned review gives an alkaliphile optimum extending to external pH about 10.5, outside the 7–8 class. This challenges exact alias equivalence without assessing the described biological machinery. |
| alkali-tolerant-scope | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/supplemental-alkali-classification.xml; Zero-based body paragraph 0, introductory classification | refutes | The explicitly supplemental source describes alkali-tolerant optima 7–9, which is not coextensive with the inclusive 7–8 bin. This is a stated convention, not universal nomenclature. |
| sources | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/source-assessment.json; Derived assessment or read/access receipt; actual primary surface remains separate | supports | Four assigned works plus one explicit supplemental work; twelve external and four ontology-source placements, three literal snippets and one Baker unknown. |
| source-ledger | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/source-ledger.json; Derived assessment or read/access receipt; actual primary surface remains separate | supports | Every assigned and supplemental publication identity and exact available surface. |
| placements | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/placement-ledger.json; Derived assessment or read/access receipt; actual primary surface remains separate | supports | Every external and ontology-source placement, kept distinct. |
| snippets | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/snippet-ledger.json; Derived assessment or read/access receipt; actual primary surface remains separate | supports | Three literal Krulwich phrase occurrences and one Baker body-unverified phrase; unknown does not mean false. |
| node-sources | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/node-source-ledger.json; Derived assessment or read/access receipt; actual primary surface remains separate | supports | All twelve nodes with generic source context separated from detailed biological scope. |
| edge-sources | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/edge-source-ledger.json; Derived assessment or read/access receipt; actual primary surface remains separate | supports | All nine edges with documentary source support and explicit biological limits. |
| source-status | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/publication-status-ledger.json; Derived assessment or read/access receipt; actual primary surface remains separate | supports | Actual indexed response notice fields only, not exhaustive global absence. |
| source-reading | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/selected-primary-reading.json; Derived assessment or read/access receipt; actual primary surface remains separate | supports | Actual selected primary locators and current reading scope, distinct from acquisition and copying. |
| source-access | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/access-limitations.json; Derived assessment or read/access receipt; actual primary surface remains separate | supports | Retained Baker body-access limits and actual canonical abstract scope; no invented full text or unnecessary new retry. |
| source-reuse | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/reuse-and-copy-receipt.json; Derived assessment or read/access receipt; actual primary surface remains separate | supports | Original body and metadata times, exact byte copying and separate selected-reading chronology. |
| canonical-source | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/canonical-assessment.json; Derived assessment or read/access receipt; actual primary surface remains separate | supports | Current species and named type-strain optimum pH 7.6, with measured growth range separately retained. |
| synonym-scope | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/synonym-scope-assessment.json; Derived assessment or read/access receipt; actual primary surface remains separate | supports | Confirmed exact-alias scope is limited to indices 0 and 1; no independent Neutrophile finding. |
| native-checks | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/native-check-context.json; Derived assessment or read/access receipt; actual primary surface remains separate | supports | Direct passing native, strict and focused snippet receipts; no copied sibling retry event. |
| source-manifest | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/evidence-manifest.json; Derived assessment or read/access receipt; actual primary surface remains separate | supports | Thirty-two frozen source artifacts verified before serialization. |
| root-reading-62 | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-root/builder-draft-root-reading.json; Derived assessment or read/access receipt; actual primary surface remains separate | supports | Only the actual reading scope and chronology recorded in this receipt; no later or whole-article reading is inferred. |
| root-reading-64 | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-root/final-ground-ledger-reading.json; Derived assessment or read/access receipt; actual primary surface remains separate | supports | Only the actual reading scope and chronology recorded in this receipt; no later or whole-article reading is inferred. |
| root-reading-66 | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-root/ledger-and-history-reading.json; Derived assessment or read/access receipt; actual primary surface remains separate | supports | Only the actual reading scope and chronology recorded in this receipt; no later or whole-article reading is inferred. |
| root-reading-69 | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-root/primary-alkaliphile-scope-reading.json; Derived assessment or read/access receipt; actual primary surface remains separate | supports | Only the actual reading scope and chronology recorded in this receipt; no later or whole-article reading is inferred. |
| root-reading-70 | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-root/primary-classification-reading.json; Derived assessment or read/access receipt; actual primary surface remains separate | supports | Only the actual reading scope and chronology recorded in this receipt; no later or whole-article reading is inferred. |
| root-reading-71 | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-root/primary-identities-reading.json; Derived assessment or read/access receipt; actual primary surface remains separate | supports | Only the actual reading scope and chronology recorded in this receipt; no later or whole-article reading is inferred. |
| root-reading-72 | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-root/primary-krulwich-classification-reading.json; Derived assessment or read/access receipt; actual primary surface remains separate | supports | Only the actual reading scope and chronology recorded in this receipt; no later or whole-article reading is inferred. |
| root-reading-73 | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-root/primary-ro2211-reading.json; Derived assessment or read/access receipt; actual primary surface remains separate | supports | Only the actual reading scope and chronology recorded in this receipt; no later or whole-article reading is inferred. |
| root-reading-74 | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-root/root-metadata-and-preparation-reading.json; Derived assessment or read/access receipt; actual primary surface remains separate | supports | Only the actual reading scope and chronology recorded in this receipt; no later or whole-article reading is inferred. |
| root-reading-75 | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-root/whole-target-preinspect-reading.json; Derived assessment or read/access receipt; actual primary surface remains separate | supports | Only the actual reading scope and chronology recorded in this receipt; no later or whole-article reading is inferred. |
| challenge | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-semantic-challenge-agent/semantic-severity-challenge.json; Final independent scientific challenge and verified bindings | supports | Independent disposition preserves the scoped alias, role and facet distinctions. |
| adjudication | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-root-adjudication.json; Final root adjudication and verified bindings | supports | Final disposition governs four findings; no scientific edit or status promotion is performed. |

## Limits And Additional Notes

- Detailed pathogen acid-defense, fitness, AMR, perturbation and intervention biology remains UNASSESSED_SCOPE; generic documentary support is not efficacy certification or mechanism optimization.
- The exact alias finding is limited to Alkali Tolerant and Alkaliphile. Neutrophile is not independently refuted, and source conventions are not imposed as universal nomenclature.
- Three snippet occurrences are literal. Baker full-body wording remains unknown in the retained access scope, not false; canonical phenotype support is actual abstract text only.
- Generic background does not establish exact 7–8 calibration, sufficient mild homeostasis in every organism, or universal habitat claims. No full-article mechanistic reading is claimed.
- GO molecular-function grounding is allowed for a protein-family facet. Node 3 explicitly denotes activity; no prior sibling demand-amount finding applies. Local powers explicitly accepts the current state-to-machine shape.
- Biolink produces has broad named-thing formal endpoints. The imported subject finding concerns its textual material-producer meaning; no hard material product range is inferred.
- The node-facet minor is documentary precision, separate from the imported-role major. A process retype alone would not resolve the Biolink subject meaning. No exact writer key was established for current nodes 8/9.
- Original BioC 07:57:33, publisher HTML 07:56:32–07:56:36, Poolman JATS 10:34:33–10:34:34 and supplemental JATS 18:33:30–18:33:31 acquisitions remain distinct from current copying and selected reading. Fresh assigned metadata acquisition at 19:12:28 preceded capture; interpretation followed capture.
- All focused checks passed directly; no sibling inspect-cache failure, snippet DNS retry or taxonomy failure applies. Historical common failures/retries/skips and corrected read-only projection errors remain explicitly qualified.
- Ignored-inclusive repository search cannot establish absence of remote/private acceptance. The retained complete catalog has no canonical match; no substitute strain or detailed defense query was used.
- Final root disposition: two major findings, two minor findings, fourteen assessments and four linked proposed actions.
- Coverage: 75 inputs, 32 frozen source artifacts, 21 frozen grounding artifacts, twelve nodes, nine edges, three components, three protein classes, two label-only classes, zero instances, one canonical and thirteen events. Four assigned works plus one supplemental work, twelve external and four ontology-source placements, four snippets with three literal and one unknown.
- This review is emitted by the single-use serializer after its static preparation. The execution receipt records serialization; root owns native review validation and save. Serialization does not edit the scientific record, persistent sweep state or Git.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T192621Z-ph-optimum-mid2
kind: record
repository: CultureBotAI/TraitMech
title: Whole-record review of pH optimum mid2
started_at: '2026-10-21T19:16:15.706761Z'
finished_at: '2026-10-21T19:26:21Z'
reviewer:
  identity: codex
  kind: agent
  independence: independent
  independence_basis: Separate source and grounding audits, independent challenge
    and root selected-primary reading inform the disposition. Generic classification,
    literal attribution and formal roles are reviewed; detailed pathogen defense,
    fitness, AMR and intervention biology remains unassessed. No scientific input
    was edited.
  model: GPT-6 (Codex)
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'Needs curation: two majors address exact-alias scope and imported relation
  subjects; two minors address bounded PATHWAY referent precision and human acceptance.
  Active identity, parent, canonical optimum, current activity/state facets and local
  powers remain positive.'
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
  - path: data/traits/environment/ph_optimum_mid2.yaml
    sha256: 6e2a9f141a0e75fc3f0f92643724bab5473f925edb95f778dbe9060a9b2e3506
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
  - path: proposals/metpo_traitmech_v10/metpo_proposal_mappings.sssom.tsv
    sha256: 8b43356a9f4f41988bd6b0e134832bbdbc457ec3c05428b0e7b29266382a5862
    role: context
  - path: proposals/metpo_traitmech_v10/metpo_proposal_properties_robot.tsv
    sha256: 4003d5cf5eb94545145fd754263abae978ffed78a72bbb7ac3aa986705659a33
    role: context
  - path: proposals/metpo_traitmech_v10/proposal.md
    sha256: a659de8d7b842ea9e630b59e15153bedaaec868284f400e0169cb3f8b0509e8d
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
  - path: research/traits/environment/ph_optimum_mid2-deep-research-falcon.md
    sha256: fd8bcade02db10fa4fe369f18863f876ac8c5bbc6559ff0d2d8ca29d00fca738
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
  - path: scripts/audit_unapplied_groundings.py
    sha256: 5afa6a602f0d7d5107adebf8b067d61bde9ea9adb267f9dfaed8a0b7cc0cc76b
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
- target_id: METPO:1000457
  path: data/traits/environment/ph_optimum_mid2.yaml
  label: pH optimum mid2
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_optimum_mid2.yaml
    role: Maintained target; read-only review.
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Maintained predicate assignment context; exact recurrence assessed only
      after capture.
  - repository: CultureBotAI/TraitMech
    path: mappings/node_grounding.tsv
    role: Maintained grounding context; exact recurrence assessed only after capture.
  record_class: TraitRecord
scope:
  description: One entire maintained TraitRecord. Contextual ontology, source, parent,
    writer and history inputs are not additional review targets.
  selection: First record of batch 011 in actual queue order. Entire target and successful
    75-input capture precede substantive judgment. Metadata was acquired before capture
    and interpreted after it. Frozen independent audits and final root adjudication
    are required before serialization.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - METPO:1000457
checks:
- check_id: audit-graphs
  name: Full-corpus graph audit
  status: passed
  required: true
  target_ids:
  - METPO:1000457
  command: just audit-graphs --out /private/tmp/traitmech-record-sweep.FU79Gr/causal_graph_audit.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  evidence_ids:
  - check-audit-graphs
  scope_note: 'History validation ran in batch 003 at the 8eee base. Original common
    diagnostics ran at f25, with the documented seven-file workflow/skill/infrastructure-history
    delta to 8eee. Actual B10 final QC ran at 19:06:27.731868–19:08:11.219124 UTC
    on 2026-10-21. B11 qualification completed at 19:08:29.388400 UTC and independent
    postcheck at 19:08:41.804361 UTC. These are reused results, not a new B11 QC execution
    or scientific verification. Original failures, retries, skips and acquisition
    times remain explicit. Qualification: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-b10-qc-supplement-qualified.json'
- check_id: audit-snippets
  name: Full-corpus snippet audit
  status: passed
  required: true
  target_ids:
  - METPO:1000457
  command: just audit-snippets --report /private/tmp/traitmech-record-sweep.FU79Gr/evidence_snippet_audit.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  evidence_ids:
  - check-audit-snippets
  scope_note: 'History validation ran in batch 003 at the 8eee base. Original common
    diagnostics ran at f25, with the documented seven-file workflow/skill/infrastructure-history
    delta to 8eee. Actual B10 final QC ran at 19:06:27.731868–19:08:11.219124 UTC
    on 2026-10-21. B11 qualification completed at 19:08:29.388400 UTC and independent
    postcheck at 19:08:41.804361 UTC. These are reused results, not a new B11 QC execution
    or scientific verification. Original failures, retries, skips and acquisition
    times remain explicit. Qualification: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-b10-qc-supplement-qualified.json'
- check_id: check-pathway-links
  name: Full-corpus pathway links
  status: passed
  required: true
  target_ids:
  - METPO:1000457
  command: just check-pathway-links
  exit_code: 0
  expected_exit_code: 0
  summary: 19 links checked against the pinned PathwayMech snapshot.
  evidence_ids:
  - check-check-pathway-links
  scope_note: 'History validation ran in batch 003 at the 8eee base. Original common
    diagnostics ran at f25, with the documented seven-file workflow/skill/infrastructure-history
    delta to 8eee. Actual B10 final QC ran at 19:06:27.731868–19:08:11.219124 UTC
    on 2026-10-21. B11 qualification completed at 19:08:29.388400 UTC and independent
    postcheck at 19:08:41.804361 UTC. These are reused results, not a new B11 QC execution
    or scientific verification. Original failures, retries, skips and acquisition
    times remain explicit. Qualification: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-b10-qc-supplement-qualified.json'
- check_id: validate-history
  name: Full-corpus history integrity
  status: passed
  required: true
  target_ids:
  - METPO:1000457
  command: just validate-history
  exit_code: 0
  expected_exit_code: 0
  summary: 1277 history records checked, zero invalid links at the 8eee source base;
    integrity does not establish science or human acceptance.
  evidence_ids:
  - check-validate-history
  scope_note: 'History validation ran in batch 003 at the 8eee base. Original common
    diagnostics ran at f25, with the documented seven-file workflow/skill/infrastructure-history
    delta to 8eee. Actual B10 final QC ran at 19:06:27.731868–19:08:11.219124 UTC
    on 2026-10-21. B11 qualification completed at 19:08:29.388400 UTC and independent
    postcheck at 19:08:41.804361 UTC. These are reused results, not a new B11 QC execution
    or scientific verification. Original failures, retries, skips and acquisition
    times remain explicit. Qualification: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-b10-qc-supplement-qualified.json'
- check_id: validate-products
  name: Initial full-product validation
  status: failed
  required: false
  target_ids:
  - METPO:1000457
  command: just validate-products
  exit_code: 2
  expected_exit_code: 0
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  evidence_ids:
  - check-validate-products
  scope_note: 'History validation ran in batch 003 at the 8eee base. Original common
    diagnostics ran at f25, with the documented seven-file workflow/skill/infrastructure-history
    delta to 8eee. Actual B10 final QC ran at 19:06:27.731868–19:08:11.219124 UTC
    on 2026-10-21. B11 qualification completed at 19:08:29.388400 UTC and independent
    postcheck at 19:08:41.804361 UTC. These are reused results, not a new B11 QC execution
    or scientific verification. Original failures, retries, skips and acquisition
    times remain explicit. Qualification: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-b10-qc-supplement-qualified.json'
- check_id: validate-products-retry-local
  name: Product validation with isolated local cache
  status: failed
  required: false
  target_ids:
  - METPO:1000457
  command: just validate-products
  exit_code: 2
  expected_exit_code: 0
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  evidence_ids:
  - check-validate-products-retry-local
  scope_note: 'History validation ran in batch 003 at the 8eee base. Original common
    diagnostics ran at f25, with the documented seven-file workflow/skill/infrastructure-history
    delta to 8eee. Actual B10 final QC ran at 19:06:27.731868–19:08:11.219124 UTC
    on 2026-10-21. B11 qualification completed at 19:08:29.388400 UTC and independent
    postcheck at 19:08:41.804361 UTC. These are reused results, not a new B11 QC execution
    or scientific verification. Original failures, retries, skips and acquisition
    times remain explicit. Qualification: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-b10-qc-supplement-qualified.json'
- check_id: validate-products-retry-network
  name: Product validation after isolated-cache download
  status: passed
  required: true
  target_ids:
  - METPO:1000457
  command: just validate-products
  exit_code: 0
  expected_exit_code: 0
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  evidence_ids:
  - check-validate-products-retry-network
  scope_note: 'History validation ran in batch 003 at the 8eee base. Original common
    diagnostics ran at f25, with the documented seven-file workflow/skill/infrastructure-history
    delta to 8eee. Actual B10 final QC ran at 19:06:27.731868–19:08:11.219124 UTC
    on 2026-10-21. B11 qualification completed at 19:08:29.388400 UTC and independent
    postcheck at 19:08:41.804361 UTC. These are reused results, not a new B11 QC execution
    or scientific verification. Original failures, retries, skips and acquisition
    times remain explicit. Qualification: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-b10-qc-supplement-qualified.json'
- check_id: ph-optimum-mid2-native
  name: Focused native validation
  status: passed
  required: true
  target_ids:
  - METPO:1000457
  command: just validate data/traits/environment/ph_optimum_mid2.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Direct pass at 19:16:35.094566–19:16:35.804540 UTC; shape validity is separate
    from scientific support.
  evidence_ids:
  - check-ph-optimum-mid2-native
- check_id: ph-optimum-mid2-strict
  name: Focused strict validation
  status: passed
  required: true
  target_ids:
  - METPO:1000457
  command: just validate-strict data/traits/environment/ph_optimum_mid2.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Direct pass at 19:16:35.096817–19:16:36.193502 UTC with zero error rows.
  evidence_ids:
  - check-ph-optimum-mid2-strict
- check_id: ph-optimum-mid2-snippets
  name: Focused snippet verification
  status: passed
  required: true
  target_ids:
  - METPO:1000457
  command: just verify-snippets --record data/traits/environment/ph_optimum_mid2.yaml
    --out /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-snippets.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 'Direct pass at 19:16:38.115487–19:16:42.292545 UTC: four fields over two
    references, three VERIFIED and one NOT_IN_ABSTRACT. Manual primary assessment
    independently finds three literal phrases and one Baker body-unverified phrase.'
  evidence_ids:
  - check-ph-optimum-mid2-snippets
- check_id: batch010-qc
  name: Reused maintained batch-ten QC
  status: passed
  required: true
  target_ids:
  - METPO:1000457
  command: just qc
  exit_code: 0
  expected_exit_code: 0
  summary: Actual B10 19:06:27.731868–19:08:11.219124 UTC pass, qualified against
    B11 bytes; not a new B11 execution.
  evidence_ids:
  - check-batch010-qc
- check_id: uniprot-applicability
  name: Protein-instance metadata applicability
  status: not_applicable
  required: false
  target_ids:
  - METPO:1000457
  summary: Three contextual protein classes, two reviewed label-only classes and zero
    instances; no token accession requirement.
  evidence_ids:
  - record
  - policy
  - node-edges
evidence:
- evidence_id: check-audit-graphs
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; metadata audit-graphs.json
  accessed_at: '2026-10-21T19:26:21Z'
  support: context_only
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  snapshot_sha256: ecce27e6a8f8b8b1fc54a9a0564a27626ee33774da508665859c6d1429337f4d
- evidence_id: check-audit-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; metadata audit-snippets.json
  accessed_at: '2026-10-21T19:26:21Z'
  support: context_only
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  snapshot_sha256: beafaa5c82645f5cf216142b6e0369d556202bcc72fdabbf35825fce955fd59f
- evidence_id: check-check-pathway-links
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; metadata check-pathway-links.json
  accessed_at: '2026-10-21T19:26:21Z'
  support: context_only
  summary: 19 links checked against the pinned PathwayMech snapshot.
  snapshot_sha256: e77729b8afd6ae02cd834e516c48dd5c72d10498802e7a1b0004eebb4831f6a0
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-003.4opxlhgf/validate-history.log
  locator: Executed 2026-10-21T07:03:25Z through 2026-10-21T07:03:30Z; metadata validate-history.json
  accessed_at: '2026-10-21T19:26:21Z'
  support: context_only
  summary: 1277 history records checked, zero invalid links at the 8eee source base;
    integrity does not establish science or human acceptance.
  snapshot_sha256: 02f94872992b2fbc3cc455c552d56a338dd449a315e02b1bf0226b68a8d2cfe3
- evidence_id: check-validate-products
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; metadata validate-products.json
  accessed_at: '2026-10-21T19:26:21Z'
  support: context_only
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  snapshot_sha256: 697efcbe603c9a5e27f9726e688d1b9d9f621fa548f585d9005b5157d81dadae
- evidence_id: check-validate-products-retry-local
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log
  locator: Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; metadata validate-products-retry-local.json
  accessed_at: '2026-10-21T19:26:21Z'
  support: context_only
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  snapshot_sha256: b636ab6978cf8b8d4cc2cc4033f1cdca399cca46dc615a26073cfe680d44ebb5
- evidence_id: check-validate-products-retry-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log
  locator: Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; metadata validate-products-retry-network.json
  accessed_at: '2026-10-21T19:26:21Z'
  support: context_only
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  snapshot_sha256: 67e91252adce1d441ad6b37d6904f0cbcea703575aec8011e65e94822fa810ea
- evidence_id: check-ph-optimum-mid2-native
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-native.log
  locator: Executed 2026-10-21T19:16:35.094566+00:00 through 2026-10-21T19:16:35.804540+00:00;
    metadata ph-optimum-mid2-native.json
  accessed_at: '2026-10-21T19:26:21Z'
  support: context_only
  summary: Direct pass at 19:16:35.094566–19:16:35.804540 UTC; shape validity is separate
    from scientific support.
  snapshot_sha256: 52d84a367f19821d7d45812d98d9eecfc179e32afba3fc41dded3d72e9acf2a8
- evidence_id: check-ph-optimum-mid2-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-strict.log
  locator: Executed 2026-10-21T19:16:35.096817+00:00 through 2026-10-21T19:16:36.193502+00:00;
    metadata ph-optimum-mid2-strict.json
  accessed_at: '2026-10-21T19:26:21Z'
  support: context_only
  summary: Direct pass at 19:16:35.096817–19:16:36.193502 UTC with zero error rows.
  snapshot_sha256: 2f009411a9c1292c9c89a2f1df8e61aea9e5de11ed7400e098fb9e0888d1aea7
- evidence_id: check-ph-optimum-mid2-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-snippets.log
  locator: Executed 2026-10-21T19:16:38.115487+00:00 through 2026-10-21T19:16:42.292545+00:00;
    metadata ph-optimum-mid2-snippets.json
  accessed_at: '2026-10-21T19:26:21Z'
  support: context_only
  summary: 'Direct pass at 19:16:38.115487–19:16:42.292545 UTC: four fields over two
    references, three VERIFIED and one NOT_IN_ABSTRACT. Manual primary assessment
    independently finds three literal phrases and one Baker body-unverified phrase.'
  snapshot_sha256: ae4c405a627ed21867a871c95c508bf488018a16d2adadabab1abf09260f0b77
- evidence_id: check-batch010-qc
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/batch010-qc.log
  locator: Executed 2026-10-21T19:06:27.731868+00:00 through 2026-10-21T19:08:11.219124+00:00;
    metadata batch010-qc.json
  accessed_at: '2026-10-21T19:26:21Z'
  support: context_only
  summary: Actual B10 19:06:27.731868–19:08:11.219124 UTC pass, qualified against
    B11 bytes; not a new B11 execution.
  snapshot_sha256: a97d2cc68e7db1ebd1a0edd19a7b0d03a4b1f45b55f8c6e6c2c48252f1705201
- evidence_id: record
  kind: record_content
  reference: data/traits/environment/ph_optimum_mid2.yaml
  locator: Entire current target
  accessed_at: '2026-10-21T19:16:16.444447Z'
  support: supports
  summary: Twelve nodes, nine edges, three components, three protein classes including
    two label-only classes, zero instances, one canonical and thirteen record events
    are covered.
  snapshot_sha256: 6e2a9f141a0e75fc3f0f92643724bab5473f925edb95f778dbe9060a9b2e3506
- evidence_id: policy
  kind: authority
  reference: docs/GROUNDING_POLICY.md
  locator: Captured maintained authority
  accessed_at: '2026-10-21T19:21:49.582096Z'
  support: supports
  summary: Taxon-agnostic GO molecular-function facets are allowed for enzyme classes;
    reviewed label-only classes and absent optional instances are legitimate.
  snapshot_sha256: 891678c983c2283a47c81c47950b35753981e9339d105f3bbdda92a1f5ab7f42
- evidence_id: playbook
  kind: authority
  reference: docs/CURATION_PLAYBOOK.md
  locator: Captured maintained authority
  accessed_at: '2026-10-21T19:21:49.582096Z'
  support: supports
  summary: Named enumerable routes differ from reaction classes; reservoir and state
    facets remain distinct. AI maintenance does not establish human acceptance.
  snapshot_sha256: 735e9b810471da9f7d8364e35ffe1e741edb3421480dac01727db6ea5aa65da9
- evidence_id: schema
  kind: authority
  reference: src/traitmech/schema/traitmech.yaml
  locator: Captured maintained authority
  accessed_at: '2026-10-21T19:21:49.582096Z'
  support: supports
  summary: Current process, pathway, state, material protein and capacity meanings.
  snapshot_sha256: 46c47fc627b80ccbba1e8ab3fb6f2aee93bc2aef7aaf72fe9aadc3257f2c02dd
- evidence_id: checklist
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Captured maintained authority
  accessed_at: '2026-10-21T19:21:49.582096Z'
  support: supports
  summary: Whole-record identity, sources, nodes, edges, ownership, provenance, optional
    coverage and readiness checklist.
  snapshot_sha256: da8896328a0fd6cc92f1adf0d8be8980d0ddd41f3172c7936f2c7f119b293ac1
- evidence_id: reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-b10-qc-supplement-qualified.json
  locator: Actual qualified B10-to-B11 byte reuse
  accessed_at: '2026-10-21T19:08:29.388400Z'
  support: supports
  summary: All 1,130 traits, 1,278 history files and nineteen common inputs match;
    original diagnostic failures, retries and skips remain distinct from actual B10
    gates and B11 qualification.
  snapshot_sha256: a728777b9987b1283d7d1382168af40739074fce5c05f9a3bd93d3738f56880f
- evidence_id: reuse-postcheck
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-output-verification-agent/post-execution-verification.json
  locator: Independent actual qualification verification
  accessed_at: '2026-10-21T19:08:41.804361Z'
  support: supports
  summary: The postcheck verifies actual input and native-output bindings without
    repeating QC.
  snapshot_sha256: a3a6f33363e71b00e8db09cbc318cae0027844aba584f7b4cafb282d11ab027a
- evidence_id: capture
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-grounding-agent/capture-verification.json
  locator: Derived assessment or read/access receipt; actual primary surface remains
    separate
  accessed_at: '2026-10-21T19:16:40.167626Z'
  support: supports
  summary: All 75 captured inputs match, with whole-target reading before judgment.
  snapshot_sha256: 7fa2fee843e00c96d5b0e9b283f8864fdd75e45d9140b931db0c1987ad5cf73d
- evidence_id: identity
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-grounding-agent/identity-assessment.json
  locator: Derived assessment or read/access receipt; actual primary surface remains
    separate
  accessed_at: '2026-10-21T19:21:49.578939Z'
  support: supports
  summary: Active identity, inclusive 7–8 restriction, direct parent and explicit
    obsolete replacement; current official taxonomy and permissible GO facet.
  snapshot_sha256: 43874ea7766f2b45af4dff174209868d36aee25a733df5c0f4edec19bac202d7
- evidence_id: node-edges
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-grounding-agent/node-edge-ledger.json
  locator: Derived assessment or read/access receipt; actual primary surface remains
    separate
  accessed_at: '2026-10-21T19:21:49.578575Z'
  support: supports
  summary: Every current node and edge, three components, firm imported-role and bounded
    facet distinctions.
  snapshot_sha256: d27ba0f9ec084d64d5763d1fecfd355a7a18b720d00cca3e468656f7c50de364
- evidence_id: owners
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-grounding-agent/owner-provenance-assessment.json
  locator: Derived assessment or read/access receipt; actual primary surface remains
    separate
  accessed_at: '2026-10-21T19:21:49.579415Z'
  support: supports
  summary: Exact maintained recurrence, five fully read AI histories, 180-path/67-array/zero-exact
    bounded human-acceptance search.
  snapshot_sha256: 670c5cc3f9f6197532fdc15cdddf9c4677df58dc3740d098286b666a4909a96f
- evidence_id: expression
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-grounding-agent/expression-applicability.json
  locator: Derived assessment or read/access receipt; actual primary surface remains
    separate
  accessed_at: '2026-10-21T19:21:49.579991Z'
  support: supports
  summary: Canonical species/historical/type aliases absent from the complete retained
    20-organism/28-dataset catalog; no substitutes or downstream defense query.
  snapshot_sha256: 8216da7e59293b6d27902ca2e9b0e25685a0804e525f77b2a95add22e606de24
- evidence_id: authority-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-grounding-agent/authority-reuse-receipts.json
  locator: Derived assessment or read/access receipt; actual primary surface remains
    separate
  accessed_at: '2026-10-21T19:18:28.343257Z'
  support: supports
  summary: Catalog and runner receipts retain original acquisition times separately
    from present copying.
  snapshot_sha256: dd67c45a98231e41313852588e86c7af863179c8cf89425ab41e3eac159a053d
- evidence_id: local-authority
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-grounding-agent/local-authority-excerpts.json
  locator: Derived assessment or read/access receipt; actual primary surface remains
    separate
  accessed_at: '2026-10-21T19:18:28.287031Z'
  support: supports
  summary: Actual v3 PMF, v8 confers, v10 powers, native mappings and Biolink inheritance.
  snapshot_sha256: 205ff43ebda045d45e9a2f19f6af99bbc56c6e33b2ae1ebe715c0115f2a317cb
- evidence_id: ground-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-grounding-agent/primary-reading-scope.json
  locator: Derived assessment or read/access receipt; actual primary surface remains
    separate
  accessed_at: '2026-10-21T19:21:49.580605Z'
  support: supports
  summary: Actual selected authority, full-target and five full-history reading scopes;
    read-only failed projections retained as corrected access limitations.
  snapshot_sha256: e79b12c3eccd47547f631767c9256b35fc042fc92936b21852de2f1b8caf48df
- evidence_id: ground-manifest
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-grounding-agent/evidence-manifest.json
  locator: Derived assessment or read/access receipt; actual primary surface remains
    separate
  accessed_at: '2026-10-21T19:21:49.585739Z'
  support: supports
  summary: Twenty-one frozen grounding artifacts with verified hashes.
  snapshot_sha256: 4f899e3c9df220f08f50a52f8c677c37612d45933190f90af584330ae5faeb26
- evidence_id: metpo-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/repo/data/raw/metpo.owl
  locator: Actual METPO:1000457, 1000331 and obsolete 0000179 XML
  accessed_at: '2026-10-21T19:18:27.605526Z'
  support: supports
  summary: Active numerical class is inclusive 7–8, with direct parent 1000331 and
    explicit obsolete 0000179 replacement. The aliases are faithfully imported; semantic
    equivalence is separately assessed.
  snapshot_sha256: 8b6f8fe0510a698579e532658c8ace05da2550093365df9ca83feb0741778415
- evidence_id: ro-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/ro.db
  locator: RO:0002211 direct definition, BFO:0000015 domain and range
  accessed_at: '2026-10-21T19:18:27.618952Z'
  support: supports
  summary: Regulation is processual. Current antiporter class remains material despite
    permissible functional grounding, while its homeostasis object is a process.
  snapshot_sha256: 849e616c29fecd0d4a6c6dee0dc0f6f117ace7167dbfa1e0f043dc84868f83cb
- evidence_id: biolink-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/repo/data/raw/biolink-model.yaml
  locator: produces and its full related-to inheritance chain
  accessed_at: '2026-10-21T19:18:28.287031Z'
  support: supports
  summary: The prose definition requires a material producer, while inherited formal
    domain and range are named thing. No hard material-only product range is inferred.
  snapshot_sha256: 4955709e1cac1d26fd657f7a0c29d6c8390f42e41f9ebfab859c82b102f2bebb
- evidence_id: go-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-grounding-agent/go0015386.response
  locator: Actual current official response
  accessed_at: '2026-10-21T19:17:03.462783Z'
  support: supports
  summary: Official GO:0015386 is potassium:proton antiporter activity in molecular_function.
    Native closeMatch functional grounding is allowed, without changing the represented
    protein subject into a process.
  snapshot_sha256: 2b51f73370726f410049bc6f666659c2079d6799703068ca40f56af9b33af161
- evidence_id: taxonomy-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-grounding-agent/taxon3080537.xml
  locator: Actual current official response
  accessed_at: '2026-10-21T19:17:03.594173Z'
  support: supports
  summary: Official species Rubellicoccus peritrichatus includes Puniceicoccus sp.
    CR14 and type-strain aliases CR14, KCTC 72139 and MCCC 1K03845; taxonomy is distinct
    from the phenotype measurement.
  snapshot_sha256: 085775d264a021df38a3d57b0c325aa914bbda77bae6ddbd8ada508e8c263193
- evidence_id: meta-krulwich
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/krulwich-metadata.json
  locator: Actual indexed metadata surface
  accessed_at: '2026-10-21T19:12:28.935299Z'
  support: supports
  summary: Actual assigned publication identity, abstract and returned notice fields
    only; later primary-body observations are separately bound.
  snapshot_sha256: 484784a62fbb4c9d74a1feab4df2fdfdf37d4dd0ce3fa79f714c86a07d86d29c
- evidence_id: meta-baker
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/baker-metadata.json
  locator: Actual indexed metadata surface
  accessed_at: '2026-10-21T19:12:28.927796Z'
  support: supports
  summary: Actual assigned publication identity, abstract and returned notice fields
    only; later primary-body observations are separately bound.
  snapshot_sha256: a78777bc3bb6444b32e2e8a13ab72c56d80592b97e30c9b5520c67cc040c631b
- evidence_id: meta-poolman
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/poolman-metadata.json
  locator: Actual indexed metadata surface
  accessed_at: '2026-10-21T19:12:28.927890Z'
  support: supports
  summary: Actual assigned publication identity, abstract and returned notice fields
    only; later primary-body observations are separately bound.
  snapshot_sha256: b6bd97da470a088ef1ba8f5eef93a6513c77b3454dbd9f8e7e4ab12c492280ae
- evidence_id: meta-canonical
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/canonical-metadata.json
  locator: Actual indexed metadata surface
  accessed_at: '2026-10-21T19:12:28.927935Z'
  support: supports
  summary: Actual canonical abstract states CR14T optimum pH 7.6 and separate growth
    range 6–9; no whole-body claim.
  snapshot_sha256: d52e0fc0f66a769e68258a2ce912d517d95ab3f24b6b24b101f23c3f522bdbd4
- evidence_id: meta-supplemental-alkali-classification
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/supplemental-alkali-classification-metadata.json
  locator: Actual indexed metadata surface
  accessed_at: '2026-10-21T18:30:13.568644Z'
  support: supports
  summary: Explicit supplemental publication identity/title; not a current assigned
    reference and not body evidence under metadata timing.
  snapshot_sha256: 2195f58575dcd56fc839f95a139c1e8107605b7342a070450d916776fa3476e7
- evidence_id: body-krulwich-bioc.xml
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/krulwich-bioc.xml
  locator: Selected primary surface with original acquisition time
  accessed_at: '2026-10-21T07:57:33Z'
  support: supports
  summary: Selected generic pH/PMF and external-versus-internal classification passages.
    Detailed pathogen/perturbation mechanisms are not assessed.
  snapshot_sha256: 903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f
- evidence_id: body-krulwich-publisher.html
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/krulwich-publisher.html
  locator: Selected primary surface with original acquisition time
  accessed_at: '2026-10-21T07:56:36Z'
  support: supports
  summary: Retained publisher surface for generic classification and literal terms;
    no full-article mechanistic reading claim.
  snapshot_sha256: 4cd2836049dc36e43c7d3d33561d1aa0b33f542eac252b37dd8275cea7fceb66
- evidence_id: body-supplemental-alkali-classification.xml
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/supplemental-alkali-classification.xml
  locator: Selected primary surface with original acquisition time
  accessed_at: '2026-10-21T18:33:31.868395Z'
  support: supports
  summary: Introductory body paragraph 0 provides a stated alkali-tolerant optimum
    convention; this explicitly supplemental work is not assigned by the record.
  snapshot_sha256: 27ff0a4deeb4ee46f16eb6caea70872e0946110f4b013db496efb8cce87d6a73
- evidence_id: body-homeostasis.xml
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/homeostasis.xml
  locator: Selected primary surface with original acquisition time
  accessed_at: '2026-10-21T10:34:34.760964Z'
  support: supports
  summary: Selected generic JATS paragraphs 0, 1, 4, 5 and 6 support existing background
    attribution, distinct from exact-bin calibration and detailed defense efficacy.
  snapshot_sha256: d55dbd224dbf2723a6a8a3e24460453f558ded3e2a6d4a9043395e2cb861f012
- evidence_id: alkaliphile-scope
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/krulwich-bioc.xml
  locator: BioC offset 39253, classification counterexample only
  accessed_at: '2026-10-21T07:57:33Z'
  support: refutes
  summary: The assigned review gives an alkaliphile optimum extending to external
    pH about 10.5, outside the 7–8 class. This challenges exact alias equivalence
    without assessing the described biological machinery.
  snapshot_sha256: 903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f
- evidence_id: alkali-tolerant-scope
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/supplemental-alkali-classification.xml
  locator: Zero-based body paragraph 0, introductory classification
  accessed_at: '2026-10-21T18:33:31.868395Z'
  support: refutes
  summary: The explicitly supplemental source describes alkali-tolerant optima 7–9,
    which is not coextensive with the inclusive 7–8 bin. This is a stated convention,
    not universal nomenclature.
  snapshot_sha256: 27ff0a4deeb4ee46f16eb6caea70872e0946110f4b013db496efb8cce87d6a73
- evidence_id: sources
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/source-assessment.json
  locator: Derived assessment or read/access receipt; actual primary surface remains
    separate
  accessed_at: '2026-10-21T19:20:21.220888Z'
  support: supports
  summary: Four assigned works plus one explicit supplemental work; twelve external
    and four ontology-source placements, three literal snippets and one Baker unknown.
  snapshot_sha256: ff2a80800d9604dff3a783a261602cc8c0edee218e6a897bcdea133369147924
- evidence_id: source-ledger
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/source-ledger.json
  locator: Derived assessment or read/access receipt; actual primary surface remains
    separate
  accessed_at: '2026-10-21T19:19:30.240283Z'
  support: supports
  summary: Every assigned and supplemental publication identity and exact available
    surface.
  snapshot_sha256: 3745aa431180b2da75284a40e3e10c65fb531358b2a856cd6f15f78498c9cf04
- evidence_id: placements
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/placement-ledger.json
  locator: Derived assessment or read/access receipt; actual primary surface remains
    separate
  accessed_at: '2026-10-21T19:19:30.240283Z'
  support: supports
  summary: Every external and ontology-source placement, kept distinct.
  snapshot_sha256: ffb19c47754a9b6a1ce72bf40bc1ffb3135340eaa254cc4dc150f2fcc9135797
- evidence_id: snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/snippet-ledger.json
  locator: Derived assessment or read/access receipt; actual primary surface remains
    separate
  accessed_at: '2026-10-21T19:19:30.240283Z'
  support: supports
  summary: Three literal Krulwich phrase occurrences and one Baker body-unverified
    phrase; unknown does not mean false.
  snapshot_sha256: 5af1a1a0edd6d259b984b4a4fddf0c27fbb7e4b3a98c6a56ecf7e4bc651a9aad
- evidence_id: node-sources
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/node-source-ledger.json
  locator: Derived assessment or read/access receipt; actual primary surface remains
    separate
  accessed_at: '2026-10-21T19:19:30.240283Z'
  support: supports
  summary: All twelve nodes with generic source context separated from detailed biological
    scope.
  snapshot_sha256: 3fe9177da857f0880ff0d4de63d4874325db24016519bff12a710723ee307de7
- evidence_id: edge-sources
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/edge-source-ledger.json
  locator: Derived assessment or read/access receipt; actual primary surface remains
    separate
  accessed_at: '2026-10-21T19:19:30.240283Z'
  support: supports
  summary: All nine edges with documentary source support and explicit biological
    limits.
  snapshot_sha256: fc6211c2569b2cdb29231f7318c8726cb18340a2b1734f41be1846c4b62ef4b5
- evidence_id: source-status
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/publication-status-ledger.json
  locator: Derived assessment or read/access receipt; actual primary surface remains
    separate
  accessed_at: '2026-10-21T19:19:30.240283Z'
  support: supports
  summary: Actual indexed response notice fields only, not exhaustive global absence.
  snapshot_sha256: 77fcc676d766ac8128a1353cdf906ba1a77c3f45923229b866a5a6a4df4bdcd6
- evidence_id: source-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/selected-primary-reading.json
  locator: Derived assessment or read/access receipt; actual primary surface remains
    separate
  accessed_at: '2026-10-21T19:19:30.240283Z'
  support: supports
  summary: Actual selected primary locators and current reading scope, distinct from
    acquisition and copying.
  snapshot_sha256: ac4e6929e910b027e59127fbcd689843732cae758c3625f5f0a6278fa9a74cc3
- evidence_id: source-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/access-limitations.json
  locator: Derived assessment or read/access receipt; actual primary surface remains
    separate
  accessed_at: '2026-10-21T19:19:30.240283Z'
  support: supports
  summary: Retained Baker body-access limits and actual canonical abstract scope;
    no invented full text or unnecessary new retry.
  snapshot_sha256: d3a43dcd4189d11251e39e43f986d82dad97dccea8791e038305d1104dcf88c1
- evidence_id: source-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/reuse-and-copy-receipt.json
  locator: Derived assessment or read/access receipt; actual primary surface remains
    separate
  accessed_at: '2026-10-21T19:17:23.843190Z'
  support: supports
  summary: Original body and metadata times, exact byte copying and separate selected-reading
    chronology.
  snapshot_sha256: 0053c490707a61b714886112b2b5f4a1e7ce5ce2bb287b7eb8f11d502f02c0a5
- evidence_id: canonical-source
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/canonical-assessment.json
  locator: Derived assessment or read/access receipt; actual primary surface remains
    separate
  accessed_at: '2026-10-21T19:19:30.240283Z'
  support: supports
  summary: Current species and named type-strain optimum pH 7.6, with measured growth
    range separately retained.
  snapshot_sha256: ede445de729d209a22ec26f1f7370a05ea989c53103a1d05650b6a990a4a9e5b
- evidence_id: synonym-scope
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/synonym-scope-assessment.json
  locator: Derived assessment or read/access receipt; actual primary surface remains
    separate
  accessed_at: '2026-10-21T19:19:30.240283Z'
  support: supports
  summary: Confirmed exact-alias scope is limited to indices 0 and 1; no independent
    Neutrophile finding.
  snapshot_sha256: e625643c590e261d3e36a65ecebc91e6dc6274c15e925ea1549482bc6d3c0adf
- evidence_id: native-checks
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/native-check-context.json
  locator: Derived assessment or read/access receipt; actual primary surface remains
    separate
  accessed_at: '2026-10-21T19:20:21.203518Z'
  support: supports
  summary: Direct passing native, strict and focused snippet receipts; no copied sibling
    retry event.
  snapshot_sha256: 2b6076b43ed35617c445fbcd23bfa010bcfc3462a85ba964f8ac3fabe7149a6c
- evidence_id: source-manifest
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-agent/evidence-manifest.json
  locator: Derived assessment or read/access receipt; actual primary surface remains
    separate
  accessed_at: '2026-10-21T19:20:21.226004Z'
  support: supports
  summary: Thirty-two frozen source artifacts verified before serialization.
  snapshot_sha256: ae36edb711ae5ba086e1a6fbbb852b8081a703b500fcb9cf5a91ceb652dcabe0
- evidence_id: root-reading-62
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-root/builder-draft-root-reading.json
  locator: Derived assessment or read/access receipt; actual primary surface remains
    separate
  accessed_at: '2026-10-21T19:18:44.661922Z'
  support: supports
  summary: Only the actual reading scope and chronology recorded in this receipt;
    no later or whole-article reading is inferred.
  snapshot_sha256: 8d0ee3cbe613bd5c30d1a95345c1bdf5c3f5e7716d269181575461b0a39bbabb
- evidence_id: root-reading-64
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-root/final-ground-ledger-reading.json
  locator: Derived assessment or read/access receipt; actual primary surface remains
    separate
  accessed_at: '2026-10-21T19:22:06.801016Z'
  support: supports
  summary: Only the actual reading scope and chronology recorded in this receipt;
    no later or whole-article reading is inferred.
  snapshot_sha256: ef9345be2e76a42a3f138a36ffbd9a8cdda71e61e24e367d9cc26c64254d1c59
- evidence_id: root-reading-66
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-root/ledger-and-history-reading.json
  locator: Derived assessment or read/access receipt; actual primary surface remains
    separate
  accessed_at: '2026-10-21T19:21:19.816571Z'
  support: supports
  summary: Only the actual reading scope and chronology recorded in this receipt;
    no later or whole-article reading is inferred.
  snapshot_sha256: c7d899523de0667cc1d03ee1528dd28567e180f664ccd5914da69030cf1da919
- evidence_id: root-reading-69
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-root/primary-alkaliphile-scope-reading.json
  locator: Derived assessment or read/access receipt; actual primary surface remains
    separate
  accessed_at: '2026-10-21T19:20:28.613168Z'
  support: supports
  summary: Only the actual reading scope and chronology recorded in this receipt;
    no later or whole-article reading is inferred.
  snapshot_sha256: 6c93e278c98a1b0376fe8a05bcfd9e4318e1d6d8b550eb35ffc2028885b72afc
- evidence_id: root-reading-70
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-root/primary-classification-reading.json
  locator: Derived assessment or read/access receipt; actual primary surface remains
    separate
  accessed_at: '2026-10-21T19:17:25.296162Z'
  support: supports
  summary: Only the actual reading scope and chronology recorded in this receipt;
    no later or whole-article reading is inferred.
  snapshot_sha256: 62ba9da2303abfc163eab831f1c96eadfef8f6533300081b2b7c6693418bff18
- evidence_id: root-reading-71
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-root/primary-identities-reading.json
  locator: Derived assessment or read/access receipt; actual primary surface remains
    separate
  accessed_at: '2026-10-21T19:18:20.156016Z'
  support: supports
  summary: Only the actual reading scope and chronology recorded in this receipt;
    no later or whole-article reading is inferred.
  snapshot_sha256: 5eb83e58200ae0cf4fb441db8f7522e5f0d199235f8b4a334a866a6c8d810e87
- evidence_id: root-reading-72
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-root/primary-krulwich-classification-reading.json
  locator: Derived assessment or read/access receipt; actual primary surface remains
    separate
  accessed_at: '2026-10-21T19:17:35.919074Z'
  support: supports
  summary: Only the actual reading scope and chronology recorded in this receipt;
    no later or whole-article reading is inferred.
  snapshot_sha256: 9140c71dd1e77cec93f84a407709848a03dccc65fdb534bed8a3473df15b661d
- evidence_id: root-reading-73
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-root/primary-ro2211-reading.json
  locator: Derived assessment or read/access receipt; actual primary surface remains
    separate
  accessed_at: '2026-10-21T19:17:13.132061Z'
  support: supports
  summary: Only the actual reading scope and chronology recorded in this receipt;
    no later or whole-article reading is inferred.
  snapshot_sha256: d37d5af822591c1c9c4c8fc86ddef80032ec71996b31adc7ff248df8cb22bf7b
- evidence_id: root-reading-74
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-root/root-metadata-and-preparation-reading.json
  locator: Derived assessment or read/access receipt; actual primary surface remains
    separate
  accessed_at: '2026-10-21T19:17:05.684631Z'
  support: supports
  summary: Only the actual reading scope and chronology recorded in this receipt;
    no later or whole-article reading is inferred.
  snapshot_sha256: 41fc4b814052ad51defbfcd1a257a835a191056ed8fbe45cd4d5a97041e0e475
- evidence_id: root-reading-75
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-source-root/whole-target-preinspect-reading.json
  locator: Derived assessment or read/access receipt; actual primary surface remains
    separate
  accessed_at: '2026-10-21T19:12:12.943941Z'
  support: supports
  summary: Only the actual reading scope and chronology recorded in this receipt;
    no later or whole-article reading is inferred.
  snapshot_sha256: 12b16679a93315c2895095943610439c3dd3342c99fa81ed16946c405daf5f86
- evidence_id: challenge
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-semantic-challenge-agent/semantic-severity-challenge.json
  locator: Final independent scientific challenge and verified bindings
  accessed_at: '2026-10-21T19:24:20.266309Z'
  support: supports
  summary: Independent disposition preserves the scoped alias, role and facet distinctions.
  snapshot_sha256: 8b99e7882b3209284e16ce05b9d3543b8dbcbbc3c8fa057b0fc4075131c0e545
- evidence_id: adjudication
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-root-adjudication.json
  locator: Final root adjudication and verified bindings
  accessed_at: '2026-10-21T19:24:51.766833Z'
  support: supports
  summary: Final disposition governs four findings; no scientific edit or status promotion
    is performed.
  snapshot_sha256: bce66d99cc9c2c1676a66c38013fce49e2f1fe6d4f60080be15216fc924e798f
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: active identity, definition and hierarchy'
  outcome: supported
  target_ids:
  - METPO:1000457
  summary: Active METPO:1000457, direct parent 1000331 and explicit obsolete 0000179
    replacement agree. The raw class is inclusive 7–8. Local definition synthesizes
    the parent and interval; it is not falsely presented as a verbatim raw-class definition.
  evidence_ids:
  - identity
  - metpo-primary
  - record
- assessment_id: synonyms
  area: identity
  topic: 'Native checklist: inherited aliases and scientific scope'
  outcome: concern
  target_ids:
  - METPO:1000457
  summary: Alkali Tolerant and Alkaliphile are faithfully imported exact aliases,
    but actual primary classifications include optima beyond 7–8. The concern is limited
    to synonyms 0/1. Neutrophile is not independently refuted, and pHO_7_to_8 remains
    a related bin label.
  evidence_ids:
  - synonym-scope
  - alkaliphile-scope
  - alkali-tolerant-scope
  - metpo-primary
  - challenge
- assessment_id: scope
  area: scope
  topic: 'Native checklist: quantitative phenotype and generic graph'
  outcome: supported
  target_ids:
  - METPO:1000457
  summary: ENVIRONMENT, CLASS and NONMECHANISTIC are appropriate to this quantitative
    optimum bin. Generic context is not automatically a universal necessary mechanism;
    no compulsory protein instance or connector is inferred.
  evidence_ids:
  - record
  - policy
  - checklist
- assessment_id: canonical
  area: evidence
  topic: 'Native checklist: canonical identity and measured optimum'
  outcome: supported
  target_ids:
  - METPO:1000457
  summary: The assigned abstract directly states Rubellicoccus peritrichatus CR14T
    optimum pH 7.6, within the bin, separately from its growth range 6–9. Current
    official taxonomy and type aliases agree; no full-article phenotype claim is made.
  evidence_ids:
  - canonical-source
  - meta-canonical
  - taxonomy-primary
  - identity
- assessment_id: bibliography
  area: evidence
  topic: 'Native checklist: all works and placements'
  outcome: supported
  target_ids:
  - METPO:1000457
  summary: Four assigned works and one explicit supplemental classification work are
    resolved. Twelve external and four ontology-source placements are covered with
    actual available surfaces and bounded notice checks.
  evidence_ids:
  - source-ledger
  - placements
  - source-status
  - source-reuse
  details: "{\n  \"completed_at\": \"2026-10-21T19:20:21.220888+00:00\",\n  \"target\"\
    : \"data/traits/environment/ph_optimum_mid2.yaml\",\n  \"target_sha256\": \"6e2a9f141a0e75fc3f0f92643724bab5473f925edb95f778dbe9060a9b2e3506\"\
    ,\n  \"capture\": {\n    \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2.inspect.json\"\
    ,\n    \"sha256\": \"17483fa8b54ef68587431963dab834e8d95e9b24b1534a46431730aaf8b321e4\"\
    ,\n    \"inputs\": 75\n  },\n  \"counts\": {\n    \"works\": 4,\n    \"supplemental_works\"\
    : 1,\n    \"literal_reference_forms\": 4,\n    \"external_placements\": 12,\n\
    \    \"ontology_source_placements\": 4,\n    \"nodes\": 12,\n    \"edges\": 9,\n\
    \    \"snippets\": 4,\n    \"exact_snippets\": 3,\n    \"unverified_snippets\"\
    : 1,\n    \"canonical_examples\": 1\n  },\n  \"coverage\": \"Entire current target\
    \ read; every assigned work, all12 external placements, four ontology-source aliases,\
    \ all12 nodes/nine edges and four snippet fields accounted for.\",\n  \"source_only_findings\"\
    : [\n    {\n      \"severity\": \"major\",\n      \"fields\": [\n        \"synonyms[0]\"\
    ,\n        \"synonyms[1]\"\n      ],\n      \"summary\": \"The exact aliases Alkali\
    \ Tolerant and Alkaliphile overstate scientific equivalence to the 7\\u20138 external-optimum\
    \ class.\",\n      \"rationale\": \"Assigned Krulwich BioC39253 includes an alkaliphile\
    \ with optimal growth extending to external pH~10.5. Explicit supplemental classification\
    \ paragraph0 assigns alkali-tolerant optima7\\u20139. The terms overlap or include\
    \ different optimum regimes and are not coextensive with this exact bin. Faithful\
    \ inheritance from METPO is a separate positive import-fidelity observation.\"\
    ,\n      \"evidence\": [\n        \"synonym-scope-assessment.json\",\n       \
    \ \"krulwich-bioc.xml\",\n        \"supplemental-alkali-classification.xml\"\n\
    \      ]\n    }\n  ],\n  \"positive_claims\": [\n    \"Canonical CR14T abstract\
    \ states optimum7.6 and measured range6\\u20139; official NCBI3080537 XML confirms\
    \ species and type-strain aliases. The optimum lies inside7\\u20138; the broader\
    \ growth range is not confused with the optimum.\",\n    \"Three Krulwich snippet\
    \ occurrences are literal; native results independently agree on those abstract\
    \ phrases.\",\n    \"Poolman assigned JATS generic paragraphs support existing\
    \ background statements for buffering, pH-homeostasis regulators and energy relationships\
    \ at a documentary level. No new mechanism is supplied.\",\n    \"Four assigned\
    \ DOI identities resolve in fresh indexed metadata; no correction/retraction notice\
    \ was returned in those responses.\"\n  ],\n  \"limitations\": [\n    \"No source-only\
    \ finding at Neutrophile: inspected growth-range/internal-pH language does not\
    \ establish a precise contradictory external optimum band.\",\n    \"Exact7\\\
    u20138 calibration, mild-homeostasis sufficiency and selected habitat generality\
    \ remain unverified; this audit does not claim a universal mechanism or falsity\
    \ from missing evidence.\",\n    \"Baker full body was unavailable in retained\
    \ bounded attempts; current abstract is real but is not full text. Its excerpt\
    \ is unknown, not proven false. No new retry or exhaustive absence claim.\",\n\
    \    \"Canonical phenotype evidence is actual abstract text only; no full-article\
    \ claim.\",\n    \"Supplemental classification metadata identity and introductory\
    \ body paragraph0 were read; this additional work is not assigned by the current\
    \ record. Its original acquisition time is preserved.\",\n    \"Detailed pathogen\
    \ defense/fitness/AMR, acid-stress interventions and optimization are UNASSESSED_SCOPE,\
    \ including incidental displayed specific-organism/perturbation material. Generic\
    \ documentary support is not experimental efficacy verification.\",\n    \"Source\
    \ auditor does not establish human acceptance or whole-record formal-role validity;\
    \ those are separate grounding/provenance workstreams.\",\n    \"Publication status\
    \ is bounded to actual indexed responses, not an exhaustive notice search.\"\n\
    \  ],\n  \"primary_access_provenance\": \"Original acquisition, current copy and\
    \ selected-reading completion are separate in reuse-and-copy-receipt.json, taxonomy-copy-receipt.json\
    \ and selected-primary-reading.json. All retained hashes were checked. No new\
    \ public request was made by this source auditor.\",\n  \"metadata_read_scope\"\
    : \"Actual abstracts of four fresh assigned works read; supplemental metadata\
    \ identity/title/DOI inspected alongside actual body classification paragraph.\"\
    ,\n  \"proposed_followup_scope\": \"Resolve exact-synonym semantics with maintained\
    \ ontology/record owners while retaining the quantitative bin, canonical optimum\
    \ and supported generic context. No biological mechanism, experiment or optimized\
    \ condition is proposed.\",\n  \"native_check_receipts\": \"native-check-context.json\
    \ preserves actual passing results; read-only guessed-filename incident separately\
    \ retained, not a native or completed-review failure.\"\n}"
- assessment_id: snippets
  area: evidence
  topic: 'Native checklist: four quoted fields'
  outcome: unknown
  target_ids:
  - METPO:1000457
  summary: Three repeated Krulwich phrases are literal. The Baker body phrase remains
    unverified in available scope, not false. Native three VERIFIED/one NOT_IN_ABSTRACT
    is distinguished from manual source verification.
  evidence_ids:
  - snippets
  - source-reading
  - source-access
  - native-checks
  details: "{\n  \"completed_at\": \"2026-10-21T19:19:30.240283+00:00\",\n  \"counts\"\
    : {\n    \"occurrences\": 4,\n    \"exact_literal\": 3,\n    \"unknown\": 1\n\
    \  },\n  \"snippets\": [\n    {\n      \"field\": \"evidence[0].snippet\",\n \
    \     \"reference\": \"DOI:10.1038/nrmicro2549\",\n      \"snippet\": \"pH homeostasis\"\
    ,\n      \"status\": \"exact_literal\",\n      \"locator\": \"Krulwich actual\
    \ BioC text and indexed abstract\",\n      \"interpretation\": \"Literal occurrence\
    \ is separate from scope/causal sufficiency.\"\n    },\n    {\n      \"field\"\
    : \"causal_graphs[0].edges[0].evidence[0].snippet\",\n      \"reference\": \"\
    DOI:10.1016/j.tim.2007.02.005\",\n      \"snippet\": \"proton motive force\",\n\
    \      \"status\": \"unknown_body_unavailable\",\n      \"locator\": \"Baker indexed\
    \ abstract lacks this phrase; full body unavailable\",\n      \"interpretation\"\
    : \"Literal occurrence is separate from scope/causal sufficiency.\"\n    },\n\
    \    {\n      \"field\": \"causal_graphs[0].edges[1].evidence[0].snippet\",\n\
    \      \"reference\": \"DOI:10.1038/nrmicro2549\",\n      \"snippet\": \"pH homeostasis\"\
    ,\n      \"status\": \"exact_literal\",\n      \"locator\": \"Krulwich actual\
    \ BioC text and indexed abstract\",\n      \"interpretation\": \"Literal occurrence\
    \ is separate from scope/causal sufficiency.\"\n    },\n    {\n      \"field\"\
    : \"causal_graphs[0].edges[2].evidence[0].snippet\",\n      \"reference\": \"\
    DOI:10.1038/nrmicro2549\",\n      \"snippet\": \"cytoplasmic pH\",\n      \"status\"\
    : \"exact_literal\",\n      \"locator\": \"Krulwich actual BioC text and indexed\
    \ abstract\",\n      \"interpretation\": \"Literal occurrence is separate from\
    \ scope/causal sufficiency.\"\n    }\n  ]\n}"
- assessment_id: nodes
  area: grounding
  topic: 'Native checklist: all twelve node referents and native facets'
  outcome: concern
  target_ids:
  - METPO:1000457
  summary: Node 8 explicitly describes material components while typed PATHWAY; node
    9 describes a reaction class rather than a named enumerable route. These are bounded
    documentary facet issues. Node 3 is explicit activity, buffering is CAPACITY,
    PMF is STATE and the permitted GO functional facet does not create a new grounding
    defect.
  evidence_ids:
  - node-edges
  - schema
  - playbook
  - go-primary
  - policy
  details: "[\n  {\n    \"index\": 0,\n    \"field_path\": \"causal_graphs[0].nodes[0]\"\
    ,\n    \"current\": {\n      \"node_id\": \"ph_optimum_mid2_trait\",\n      \"\
    label\": \"pH optimum mid2\",\n      \"node_type\": \"TRAIT\",\n      \"grounding\"\
    : \"METPO:1000457\",\n      \"description\": \"pH optimum approximately 7\\u20138.\"\
    \n    },\n    \"documentary_assessment\": \"Active METPO:1000457 is a class with\
    \ inclusive numerical restriction 7\\u20138. Current approximately 7\\u20138 wording\
    \ does not introduce a distinct boundary defect.\",\n    \"status\": \"PASS_OR_BOUNDED\"\
    ,\n    \"biological_scope\": \"UNASSESSED_SCOPE for detailed pathogen/acid-defense/fitness/intervention\
    \ mechanisms; identity and generic documentary facets only\"\n  },\n  {\n    \"\
    index\": 1,\n    \"field_path\": \"causal_graphs[0].nodes[1]\",\n    \"current\"\
    : {\n      \"node_id\": \"ph_optimum\",\n      \"label\": \"pH optimum\",\n  \
    \    \"node_type\": \"TRAIT\",\n      \"grounding\": \"METPO:1000331\",\n    \
    \  \"description\": \"External pH supporting maximal growth.\"\n    },\n    \"\
    documentary_assessment\": \"Active METPO:1000331 is the exact declared upstream\
    \ parent; it represents external conditions for efficient growth. No new parent\
    \ requirement.\",\n    \"status\": \"PASS_OR_BOUNDED\",\n    \"biological_scope\"\
    : \"UNASSESSED_SCOPE for detailed pathogen/acid-defense/fitness/intervention mechanisms;\
    \ identity and generic documentary facets only\"\n  },\n  {\n    \"index\": 2,\n\
    \    \"field_path\": \"causal_graphs[0].nodes[2]\",\n    \"current\": {\n    \
    \  \"node_id\": \"slightly_alkaline_external_ph\",\n      \"label\": \"slightly\
    \ alkaline external pH\",\n      \"node_type\": \"ENVIRONMENTAL_FACTOR\",\n  \
    \    \"description\": \"External pH 7\\u20138, typical of seawater and many host\
    \ body fluids.\"\n    },\n    \"documentary_assessment\": \"Current referent is\
    \ an external pH condition; ENVIRONMENTAL_FACTOR fits. Generic environmental/host\
    \ wording does not establish any specific pathogen mechanism.\",\n    \"status\"\
    : \"PASS_OR_BOUNDED\",\n    \"biological_scope\": \"UNASSESSED_SCOPE for detailed\
    \ pathogen/acid-defense/fitness/intervention mechanisms; identity and generic\
    \ documentary facets only\"\n  },\n  {\n    \"index\": 3,\n    \"field_path\"\
    : \"causal_graphs[0].nodes[3]\",\n    \"current\": {\n      \"node_id\": \"modest_alkaline_homeostasis\"\
    ,\n      \"label\": \"modest alkaline pH homeostasis\",\n      \"node_type\":\
    \ \"BIOLOGICAL_PROCESS\",\n      \"description\": \"Mild K+/H+ antiport and cytoplasmic\
    \ acidification activity maintaining cytoplasmic pH at slightly basic external\
    \ pH.\"\n    },\n    \"documentary_assessment\": \"Explicit mild antiport and\
    \ acidification activity is processual. BIOLOGICAL_PROCESS is supported by its\
    \ stated referent; no inherited demand-amount finding from a sibling applies.\"\
    ,\n    \"status\": \"PASS_OR_BOUNDED\",\n    \"biological_scope\": \"UNASSESSED_SCOPE\
    \ for detailed pathogen/acid-defense/fitness/intervention mechanisms; identity\
    \ and generic documentary facets only\"\n  },\n  {\n    \"index\": 4,\n    \"\
    field_path\": \"causal_graphs[0].nodes[4]\",\n    \"current\": {\n      \"node_id\"\
    : \"cytoplasmic_buffering_capacity\",\n      \"label\": \"cytoplasmic buffering\
    \ capacity\",\n      \"node_type\": \"CAPACITY\",\n      \"description\": \"Buffering\
    \ of the cytoplasm (e.g. phosphate pools) absorbing pH fluctuations.\"\n    },\n\
    \    \"documentary_assessment\": \"CAPACITY fits the described buffering reservoir/pool.\
    \ Captured playbook and direct type-normalization writer specifically recognize\
    \ this current node; no forced retype.\",\n    \"status\": \"PASS_OR_BOUNDED\"\
    ,\n    \"biological_scope\": \"UNASSESSED_SCOPE for detailed pathogen/acid-defense/fitness/intervention\
    \ mechanisms; identity and generic documentary facets only\"\n  },\n  {\n    \"\
    index\": 5,\n    \"field_path\": \"causal_graphs[0].nodes[5]\",\n    \"current\"\
    : {\n      \"node_id\": \"intracellular_ph_homeostasis\",\n      \"label\": \"\
    intracellular pH homeostasis\",\n      \"node_type\": \"BIOLOGICAL_PROCESS\",\n\
    \      \"description\": \"Regulation maintaining cytoplasmic pH near neutral.\"\
    \n    },\n    \"documentary_assessment\": \"The stated regulation/maintenance\
    \ is processual. Near-neutral wording is generic contextual scope, not evidence\
    \ of a universal exact internal setpoint.\",\n    \"status\": \"PASS_OR_BOUNDED\"\
    ,\n    \"biological_scope\": \"UNASSESSED_SCOPE for detailed pathogen/acid-defense/fitness/intervention\
    \ mechanisms; identity and generic documentary facets only\"\n  },\n  {\n    \"\
    index\": 6,\n    \"field_path\": \"causal_graphs[0].nodes[6]\",\n    \"current\"\
    : {\n      \"node_id\": \"na_h_antiporters\",\n      \"label\": \"Na+/H+ antiporters\"\
    ,\n      \"node_type\": \"GENE_OR_PROTEIN\",\n      \"grounding_status\": \"REVIEWED_LABEL_ONLY\"\
    ,\n      \"grounding_notes\": \"Reviewed as a contextual protein or protein-complex\
    \ label within a quantitative measurement graph; no exact semantic family term\
    \ was established for this aggregate use.\",\n      \"description\": \"Sodium:proton\
    \ antiporters that acidify the cytoplasm when internal pH is too high.\"\n   \
    \ },\n    \"documentary_assessment\": \"Taxon-agnostic protein class with explicit\
    \ REVIEWED_LABEL_ONLY disposition. No mandatory protein instance or exact family\
    \ accession is imposed.\",\n    \"status\": \"PASS_OR_BOUNDED\",\n    \"biological_scope\"\
    : \"UNASSESSED_SCOPE for detailed pathogen/acid-defense/fitness/intervention mechanisms;\
    \ identity and generic documentary facets only\"\n  },\n  {\n    \"index\": 7,\n\
    \    \"field_path\": \"causal_graphs[0].nodes[7]\",\n    \"current\": {\n    \
    \  \"node_id\": \"k_h_antiporters\",\n      \"label\": \"K+/H+ antiporters\",\n\
    \      \"node_type\": \"GENE_OR_PROTEIN\",\n      \"description\": \"Potassium:proton\
    \ antiporters regulating bacterial internal pH.\",\n      \"grounding\": \"GO:0015386\"\
    \n    },\n    \"documentary_assessment\": \"Official GO:0015386 is potassium:proton\
    \ antiporter activity, a molecular_function. Native policy and maintained closeMatch\
    \ row permit this functional facet for a protein family; this does not convert\
    \ the protein subject into a process for RO:0002211.\",\n    \"status\": \"PASS_OR_BOUNDED\"\
    ,\n    \"biological_scope\": \"UNASSESSED_SCOPE for detailed pathogen/acid-defense/fitness/intervention\
    \ mechanisms; identity and generic documentary facets only\"\n  },\n  {\n    \"\
    index\": 8,\n    \"field_path\": \"causal_graphs[0].nodes[8]\",\n    \"current\"\
    : {\n      \"node_id\": \"respiratory_proton_pumping\",\n      \"label\": \"proton-pumping\
    \ respiratory chain components\",\n      \"node_type\": \"PATHWAY\",\n      \"\
    description\": \"Respiratory electron transport chain components that pump protons.\"\
    \n    },\n    \"documentary_assessment\": \"Current label and description both\
    \ identify respiratory chain components, while PATHWAY and the node ID suggest\
    \ a route/activity. Bounded documentary facet precision is needed; clarify which\
    \ existing referent is intended without reconstructing machinery.\",\n    \"status\"\
    : \"MINOR_FACET_PRECISION\",\n    \"biological_scope\": \"UNASSESSED_SCOPE for\
    \ detailed pathogen/acid-defense/fitness/intervention mechanisms; identity and\
    \ generic documentary facets only\"\n  },\n  {\n    \"index\": 9,\n    \"field_path\"\
    : \"causal_graphs[0].nodes[9]\",\n    \"current\": {\n      \"node_id\": \"metabolite_decarboxylation\"\
    ,\n      \"label\": \"metabolite decarboxylation pathways\",\n      \"node_type\"\
    : \"PATHWAY\",\n      \"description\": \"Decarboxylation reactions whose free-energy\
    \ change can be stored as PMF.\"\n    },\n    \"documentary_assessment\": \"Current\
    \ description names decarboxylation reactions as a reaction class, not a named\
    \ enumerable route. The captured PATHWAY convention therefore supports a bounded\
    \ node-facet precision finding; no new pathway is supplied.\",\n    \"status\"\
    : \"MINOR_FACET_PRECISION\",\n    \"biological_scope\": \"UNASSESSED_SCOPE for\
    \ detailed pathogen/acid-defense/fitness/intervention mechanisms; identity and\
    \ generic documentary facets only\"\n  },\n  {\n    \"index\": 10,\n    \"field_path\"\
    : \"causal_graphs[0].nodes[10]\",\n    \"current\": {\n      \"node_id\": \"proton_motive_force\"\
    ,\n      \"label\": \"proton motive force\",\n      \"node_type\": \"STATE\",\n\
    \      \"description\": \"Electrochemical proton gradient (\\u0394pH + \\u0394\\\
    u03c8) across the membrane.\",\n      \"grounding\": \"METPO:1007500\"\n    },\n\
    \    \"documentary_assessment\": \"STATE correctly represents the electrochemical\
    \ proton gradient rather than its establishment. Local METPO:1007500 proposal\
    \ is the retained provisional state authority, absent from the pinned upstream\
    \ release.\",\n    \"status\": \"PASS_OR_BOUNDED\",\n    \"biological_scope\"\
    : \"UNASSESSED_SCOPE for detailed pathogen/acid-defense/fitness/intervention mechanisms;\
    \ identity and generic documentary facets only\"\n  },\n  {\n    \"index\": 11,\n\
    \    \"field_path\": \"causal_graphs[0].nodes[11]\",\n    \"current\": {\n   \
    \   \"node_id\": \"f0f1_atp_synthase\",\n      \"label\": \"F0F1-ATP synthase\"\
    ,\n      \"node_type\": \"GENE_OR_PROTEIN\",\n      \"grounding_status\": \"REVIEWED_LABEL_ONLY\"\
    ,\n      \"grounding_notes\": \"Reviewed as a contextual multisubunit ATP-synthase\
    \ complex in a quantitative pH bin; no one component family represents the whole\
    \ complex.\",\n      \"description\": \"Proton-transporting ATP synthase complex\
    \ that makes ATP from PMF.\"\n    },\n    \"documentary_assessment\": \"Whole\
    \ ATP-synthase complex is a valid protein/complex class with explicit REVIEWED_LABEL_ONLY\
    \ disposition. A single component accession is not required or substituted.\"\
    ,\n    \"status\": \"PASS_OR_BOUNDED\",\n    \"biological_scope\": \"UNASSESSED_SCOPE\
    \ for detailed pathogen/acid-defense/fitness/intervention mechanisms; identity\
    \ and generic documentary facets only\"\n  }\n]"
- assessment_id: relations
  area: consistency
  topic: 'Native checklist: all nine imported and free relations'
  outcome: concern
  target_ids:
  - METPO:1000457
  summary: Edge 5 imports process regulation with a protein subject. Edge 7 imports
    Biolink material-producer prose with a reaction/pathway subject, while formal
    endpoints remain NamedThing. Local confers and powers fit their actual proposals;
    free engages/stabilizes/maintains receive no invented RO restrictions.
  evidence_ids:
  - node-edges
  - ro-primary
  - biolink-primary
  - local-authority
  - owners
  - challenge
  details: "[\n  {\n    \"index\": 0,\n    \"field_path\": \"causal_graphs[0].edges[0]\"\
    ,\n    \"current\": {\n      \"subject\": \"slightly_alkaline_external_ph\",\n\
    \      \"predicate\": \"engages\",\n      \"object\": \"modest_alkaline_homeostasis\"\
    ,\n      \"description\": \"Slightly alkaline external pH engages modest alkaline\
    \ pH-homeostasis.\",\n      \"evidence\": [\n        {\n          \"reference\"\
    : \"DOI:10.1016/j.tim.2007.02.005\",\n          \"snippet\": \"proton motive force\"\
    ,\n          \"notes\": \"Supports balanced proton motive force at slightly alkaline\
    \ pH as the energetic setting of this regime.\"\n        }\n      ]\n    },\n\
    \    \"status\": \"PASS_DOCUMENTARY\",\n    \"documentary_assessment\": \"Free\
    \ engages connects an external condition to an activity. It has no imported process-domain\
    \ assertion; source-specific exact-bin causation and detailed biological mechanisms\
    \ are not certified by this formal check.\",\n    \"biological_scope\": \"Generic\
    \ documentary/source context only; detailed acid-defense, pathogen fitness and\
    \ intervention mechanisms UNASSESSED_SCOPE\"\n  },\n  {\n    \"index\": 1,\n \
    \   \"field_path\": \"causal_graphs[0].edges[1]\",\n    \"current\": {\n     \
    \ \"subject\": \"modest_alkaline_homeostasis\",\n      \"predicate\": \"confers\"\
    ,\n      \"object\": \"ph_optimum_mid2_trait\",\n      \"description\": \"Modest\
    \ alkaline pH-homeostasis yields a neutrophile / alkaline-tolerant pH-optimum\
    \ setpoint.\",\n      \"evidence\": [\n        {\n          \"reference\": \"\
    DOI:10.1038/nrmicro2549\",\n          \"snippet\": \"pH homeostasis\",\n     \
    \     \"notes\": \"Supports the 7\\u20138 optimum as the neutrophile / mild-alkaliphile\
    \ outcome.\"\n        }\n      ],\n      \"predicate_id\": \"METPO:2007700\"\n\
    \    },\n    \"status\": \"PASS_DOCUMENTARY\",\n    \"documentary_assessment\"\
    : \"METPO:2007700 confers explicitly accepts activity/state/material causal subjects\
    \ and TRAIT objects. This current process-to-trait shape fits; no compulsory universal\
    \ mechanism is inferred.\",\n    \"biological_scope\": \"Generic documentary/source\
    \ context only; detailed acid-defense, pathogen fitness and intervention mechanisms\
    \ UNASSESSED_SCOPE\"\n  },\n  {\n    \"index\": 2,\n    \"field_path\": \"causal_graphs[0].edges[2]\"\
    ,\n    \"current\": {\n      \"subject\": \"ph_optimum_mid2_trait\",\n      \"\
    predicate\": \"is a\",\n      \"object\": \"ph_optimum\",\n      \"description\"\
    : \"pH optimum mid2 is a quantitative bin of the pH-optimum phenotype.\",\n  \
    \    \"evidence\": [\n        {\n          \"reference\": \"DOI:10.1038/nrmicro2549\"\
    ,\n          \"snippet\": \"cytoplasmic pH\",\n          \"notes\": \"Supports\
    \ the 7\\u20138 optimum as a value within the pH-optimum distribution.\"\n   \
    \     }\n      ],\n      \"predicate_id\": \"rdfs:subClassOf\"\n    },\n    \"\
    status\": \"PASS_DOCUMENTARY\",\n    \"documentary_assessment\": \"rdfs:subClassOf\
    \ connects the current bin class to its actual upstream pH-optimum parent. Both\
    \ are classes; the hierarchy is independently supported by pinned METPO.\",\n\
    \    \"biological_scope\": \"Generic documentary/source context only; detailed\
    \ acid-defense, pathogen fitness and intervention mechanisms UNASSESSED_SCOPE\"\
    \n  },\n  {\n    \"index\": 3,\n    \"field_path\": \"causal_graphs[0].edges[3]\"\
    ,\n    \"current\": {\n      \"subject\": \"cytoplasmic_buffering_capacity\",\n\
    \      \"predicate\": \"stabilizes\",\n      \"object\": \"intracellular_ph_homeostasis\"\
    ,\n      \"description\": \"Cytoplasmic buffering capacity stabilizes intracellular\
    \ pH against fluctuations.\",\n      \"evidence\": [\n        {\n          \"\
    reference\": \"DOI:10.1093/femsre/fuad033\",\n          \"notes\": \"Buffering\
    \ capacity of the cytoplasm absorbs pH fluctuations; broad bacterial mechanism\
    \ supporting near-neutral pHi at external pH 7-8.\"\n        }\n      ]\n    },\n\
    \    \"status\": \"PASS_DOCUMENTARY\",\n    \"documentary_assessment\": \"Free\
    \ stabilizes imposes no imported domain/range. Buffering reservoir to homeostasis\
    \ process is an intelligible generic documentary relation; detailed biological\
    \ applicability remains bounded.\",\n    \"biological_scope\": \"Generic documentary/source\
    \ context only; detailed acid-defense, pathogen fitness and intervention mechanisms\
    \ UNASSESSED_SCOPE\"\n  },\n  {\n    \"index\": 4,\n    \"field_path\": \"causal_graphs[0].edges[4]\"\
    ,\n    \"current\": {\n      \"subject\": \"na_h_antiporters\",\n      \"predicate\"\
    : \"maintains\",\n      \"object\": \"intracellular_ph_homeostasis\",\n      \"\
    description\": \"Na+/H+ antiporters acidify the cytoplasm when pHi is too high,\
    \ maintaining pH homeostasis.\",\n      \"evidence\": [\n        {\n         \
    \ \"reference\": \"DOI:10.1093/femsre/fuad033\",\n          \"notes\": \"Proton-sensing\
    \ antiporters acidify the cytoplasm by exporting Na+ for protons when internal\
    \ pH gets too high; general mechanism relevant at external pH 7-8.\"\n       \
    \ }\n      ]\n    },\n    \"status\": \"PASS_DOCUMENTARY\",\n    \"documentary_assessment\"\
    : \"Free maintains is not RO:0002211 or RO:0002327. Material antiporter class\
    \ to process is not automatically a formal error.\",\n    \"biological_scope\"\
    : \"Generic documentary/source context only; detailed acid-defense, pathogen fitness\
    \ and intervention mechanisms UNASSESSED_SCOPE\"\n  },\n  {\n    \"index\": 5,\n\
    \    \"field_path\": \"causal_graphs[0].edges[5]\",\n    \"current\": {\n    \
    \  \"subject\": \"k_h_antiporters\",\n      \"predicate\": \"regulates\",\n  \
    \    \"object\": \"intracellular_ph_homeostasis\",\n      \"description\": \"\
    K+/H+ antiporters are key regulators of bacterial internal pH.\",\n      \"evidence\"\
    : [\n        {\n          \"reference\": \"DOI:10.1093/femsre/fuad033\",\n   \
    \       \"notes\": \"Na+/H+ and K+/H+ antiporters are key regulators of bacterial\
    \ pH homeostasis; general regulator.\"\n        }\n      ],\n      \"predicate_id\"\
    : \"RO:0002211\"\n    },\n    \"status\": \"MAJOR_IMPORTED_ROLE\",\n    \"documentary_assessment\"\
    : \"RO:0002211 directly has BFO:0000015 process domain and range, and its definition\
    \ describes execution of a regulating process. Object homeostasis is processual;\
    \ current K+/H+ antiporter subject is a protein class. Allowed GO molecular-function\
    \ grounding is a semantic facet, not a subject retyping.\",\n    \"biological_scope\"\
    : \"Generic documentary/source context only; detailed acid-defense, pathogen fitness\
    \ and intervention mechanisms UNASSESSED_SCOPE\"\n  },\n  {\n    \"index\": 6,\n\
    \    \"field_path\": \"causal_graphs[0].edges[6]\",\n    \"current\": {\n    \
    \  \"subject\": \"respiratory_proton_pumping\",\n      \"predicate\": \"maintains\"\
    ,\n      \"object\": \"intracellular_ph_homeostasis\",\n      \"description\"\
    : \"Proton-pumping respiratory chain components prevent the internal pH from becoming\
    \ too low.\",\n      \"evidence\": [\n        {\n          \"reference\": \"DOI:10.1093/femsre/fuad033\"\
    ,\n          \"notes\": \"Activation of proton-pumping respiratory chains prevents\
    \ internal pH becoming too low; broad statement across respiratory bacteria.\"\
    \n        }\n      ]\n    },\n    \"status\": \"MINOR_NODE_FACET_CONTEXT\",\n\
    \    \"documentary_assessment\": \"Free maintains carries no imported process\
    \ restriction. The bounded concern is node 8 components-versus-route wording/type,\
    \ not a claimed invalid free relation or disproved mechanism.\",\n    \"biological_scope\"\
    : \"Generic documentary/source context only; detailed acid-defense, pathogen fitness\
    \ and intervention mechanisms UNASSESSED_SCOPE\"\n  },\n  {\n    \"index\": 7,\n\
    \    \"field_path\": \"causal_graphs[0].edges[7]\",\n    \"current\": {\n    \
    \  \"subject\": \"metabolite_decarboxylation\",\n      \"predicate\": \"generates\"\
    ,\n      \"object\": \"proton_motive_force\",\n      \"description\": \"Metabolite\
    \ decarboxylation pathways store free energy as proton motive force.\",\n    \
    \  \"evidence\": [\n        {\n          \"reference\": \"DOI:10.1093/femsre/fuad033\"\
    ,\n          \"notes\": \"The free energy change from decarboxylation reactions\
    \ can be stored as a proton motive force; general, not taxon-specific.\"\n   \
    \     }\n      ],\n      \"predicate_id\": \"biolink:produces\"\n    },\n    \"\
    status\": \"MAJOR_TEXTUAL_RELATION_SEMANTICS\",\n    \"documentary_assessment\"\
    : \"Biolink produces is defined for a material entity whose functioning generates\
    \ a product. Current subject is a pathway/reaction class, so its imported meaning\
    \ is mismatched. Formal inherited domain and range remain named thing; neither\
    \ a formal material-only domain nor a material-only product range is asserted.\
    \ Retyping this reaction class to BIOLOGICAL_PROCESS alone would not fix the subject\
    \ meaning.\",\n    \"biological_scope\": \"Generic documentary/source context\
    \ only; detailed acid-defense, pathogen fitness and intervention mechanisms UNASSESSED_SCOPE\"\
    \n  },\n  {\n    \"index\": 8,\n    \"field_path\": \"causal_graphs[0].edges[8]\"\
    ,\n    \"current\": {\n      \"subject\": \"proton_motive_force\",\n      \"predicate\"\
    : \"powers\",\n      \"object\": \"f0f1_atp_synthase\",\n      \"description\"\
    : \"Proton motive force powers F0F1-ATP synthase ATP synthesis.\",\n      \"evidence\"\
    : [\n        {\n          \"reference\": \"DOI:10.1093/femsre/fuad033\",\n   \
    \       \"notes\": \"The proton motive force can be used by F0F1-ATP synthase\
    \ to make ATP; strong general bioenergetic edge.\"\n        }\n      ],\n    \
    \  \"predicate_id\": \"METPO:2007900\"\n    },\n    \"status\": \"PASS_DOCUMENTARY\"\
    ,\n    \"documentary_assessment\": \"METPO:2007900 powers explicitly models an\
    \ energetic driver operating a molecular machine. Current STATE to GENE_OR_PROTEIN\
    \ meets the v10 local gate and the proposed meaning; it is only closeMatch to\
    \ RO:0002327, not identical to its process-object constraint.\",\n    \"biological_scope\"\
    : \"Generic documentary/source context only; detailed acid-defense, pathogen fitness\
    \ and intervention mechanisms UNASSESSED_SCOPE\"\n  }\n]"
- assessment_id: mechanism-scope
  area: scope
  topic: 'Native checklist: generic attribution and detailed biological exclusions'
  outcome: unknown
  target_ids:
  - METPO:1000457
  summary: Existing generic Poolman environmental/homeostasis attribution remains
    positive, distinct from calibration of the exact bin or universal mechanism. Detailed
    pathogen acid-defense, fitness, AMR, perturbation and intervention mechanisms
    remain UNASSESSED_SCOPE; no repaired route, efficacy claim or optimization is
    provided.
  evidence_ids:
  - sources
  - edge-sources
  - source-reading
  - source-access
  details: "{\n  \"completed_at\": \"2026-10-21T19:19:30.240283+00:00\",\n  \"edges\"\
    : [\n    {\n      \"index\": 0,\n      \"field\": \"causal_graphs[0].edges[0]\"\
    ,\n      \"subject\": \"slightly_alkaline_external_ph\",\n      \"predicate\"\
    : \"engages\",\n      \"object\": \"modest_alkaline_homeostasis\",\n      \"reference\"\
    : \"DOI:10.1016/j.tim.2007.02.005\",\n      \"status\": \"unknown\",\n      \"\
    source\": \"baker\",\n      \"locator\": \"indexed abstract only\",\n      \"\
    assessment\": \"Baker abstract concerns acidophile pH homeostasis and does not\
    \ establish slightly alkaline engagement or the exact current excerpt. Full body\
    \ unavailable; no false-citation or false-quote finding solely from that limit.\"\
    ,\n      \"scope\": \"Generic statement/attribution and literal evidence only;\
    \ detailed pathogen fitness, defense, AMR, interventions and optimization UNASSESSED_SCOPE.\"\
    \n    },\n    {\n      \"index\": 1,\n      \"field\": \"causal_graphs[0].edges[1]\"\
    ,\n      \"subject\": \"modest_alkaline_homeostasis\",\n      \"predicate\": \"\
    confers\",\n      \"object\": \"ph_optimum_mid2_trait\",\n      \"reference\"\
    : \"DOI:10.1038/nrmicro2549\",\n      \"status\": \"supported_context_exact_bin_unverified\"\
    ,\n      \"source\": \"krulwich\",\n      \"locator\": \"BioC58/671\",\n     \
    \ \"assessment\": \"Krulwich supports general pH homeostasis. The short excerpt\
    \ does not establish a particular modest-homeostasis regime as sufficient for\
    \ an external optimum of 7\\u20138. Retain this as bounded calibration uncertainty,\
    \ distinct from the concrete exact-synonym scope finding.\",\n      \"scope\"\
    : \"Generic statement/attribution and literal evidence only; detailed pathogen\
    \ fitness, defense, AMR, interventions and optimization UNASSESSED_SCOPE.\"\n\
    \    },\n    {\n      \"index\": 2,\n      \"field\": \"causal_graphs[0].edges[2]\"\
    ,\n      \"subject\": \"ph_optimum_mid2_trait\",\n      \"predicate\": \"is a\"\
    ,\n      \"object\": \"ph_optimum\",\n      \"reference\": \"DOI:10.1038/nrmicro2549\"\
    ,\n      \"status\": \"context_only_hierarchy_grounded_elsewhere\",\n      \"\
    source\": \"krulwich\",\n      \"locator\": \"BioC58/671\",\n      \"assessment\"\
    : \"General pH discussion is context, not the formal source for the exact bin\
    \ subclass. Current captured METPO hierarchy is assessed by grounding auditor;\
    \ the source is not falsely described as empirical proof of that taxonomy.\",\n\
    \      \"scope\": \"Generic statement/attribution and literal evidence only; detailed\
    \ pathogen fitness, defense, AMR, interventions and optimization UNASSESSED_SCOPE.\"\
    \n    },\n    {\n      \"index\": 3,\n      \"field\": \"causal_graphs[0].edges[3]\"\
    ,\n      \"subject\": \"cytoplasmic_buffering_capacity\",\n      \"predicate\"\
    : \"stabilizes\",\n      \"object\": \"intracellular_ph_homeostasis\",\n     \
    \ \"reference\": \"DOI:10.1093/femsre/fuad033\",\n      \"status\": \"generic_documentary_support\"\
    ,\n      \"source\": \"poolman\",\n      \"locator\": \"body paragraph4 generic\
    \ opening clause\",\n      \"assessment\": \"The assigned text explicitly describes\
    \ cytoplasmic buffering absorbing fluctuations. It does not calibrate a 7\\u20138\
    \ optimum. Detailed organism-specific efficacy remains unassessed.\",\n      \"\
    scope\": \"Generic statement/attribution and literal evidence only; detailed pathogen\
    \ fitness, defense, AMR, interventions and optimization UNASSESSED_SCOPE.\"\n\
    \    },\n    {\n      \"index\": 4,\n      \"field\": \"causal_graphs[0].edges[4]\"\
    ,\n      \"subject\": \"na_h_antiporters\",\n      \"predicate\": \"maintains\"\
    ,\n      \"object\": \"intracellular_ph_homeostasis\",\n      \"reference\": \"\
    DOI:10.1093/femsre/fuad033\",\n      \"status\": \"generic_documentary_support\"\
    ,\n      \"source\": \"poolman\",\n      \"locator\": \"body paragraph4 generic\
    \ antiporter clause\",\n      \"assessment\": \"The assigned generic background\
    \ sentence matches the current direction of the existing antiporter claim. No\
    \ organism-specific defense mechanism or intervention is validated.\",\n     \
    \ \"scope\": \"Generic statement/attribution and literal evidence only; detailed\
    \ pathogen fitness, defense, AMR, interventions and optimization UNASSESSED_SCOPE.\"\
    \n    },\n    {\n      \"index\": 5,\n      \"field\": \"causal_graphs[0].edges[5]\"\
    ,\n      \"subject\": \"k_h_antiporters\",\n      \"predicate\": \"regulates\"\
    ,\n      \"object\": \"intracellular_ph_homeostasis\",\n      \"reference\": \"\
    DOI:10.1093/femsre/fuad033\",\n      \"status\": \"generic_documentary_support\"\
    ,\n      \"source\": \"poolman\",\n      \"locator\": \"body paragraph1 overview\"\
    ,\n      \"assessment\": \"The assigned overview calls the listed antiporters\
    \ regulators of bacterial pH homeostasis. This is generic contextual support,\
    \ not proof of this bin or a particular protein.\",\n      \"scope\": \"Generic\
    \ statement/attribution and literal evidence only; detailed pathogen fitness,\
    \ defense, AMR, interventions and optimization UNASSESSED_SCOPE.\"\n    },\n \
    \   {\n      \"index\": 6,\n      \"field\": \"causal_graphs[0].edges[6]\",\n\
    \      \"subject\": \"respiratory_proton_pumping\",\n      \"predicate\": \"maintains\"\
    ,\n      \"object\": \"intracellular_ph_homeostasis\",\n      \"reference\": \"\
    DOI:10.1093/femsre/fuad033\",\n      \"status\": \"generic_documentary_support\"\
    ,\n      \"source\": \"poolman\",\n      \"locator\": \"body paragraph4 generic\
    \ respiratory clause\",\n      \"assessment\": \"The assigned background passage\
    \ supports the current broad respiratory-homeostasis statement at documentary\
    \ level. Formal PATHWAY/material-component referents are left to the grounding\
    \ audit.\",\n      \"scope\": \"Generic statement/attribution and literal evidence\
    \ only; detailed pathogen fitness, defense, AMR, interventions and optimization\
    \ UNASSESSED_SCOPE.\"\n    },\n    {\n      \"index\": 7,\n      \"field\": \"\
    causal_graphs[0].edges[7]\",\n      \"subject\": \"metabolite_decarboxylation\"\
    ,\n      \"predicate\": \"generates\",\n      \"object\": \"proton_motive_force\"\
    ,\n      \"reference\": \"DOI:10.1093/femsre/fuad033\",\n      \"status\": \"\
    generic_documentary_support\",\n      \"source\": \"poolman\",\n      \"locator\"\
    : \"body paragraph5\",\n      \"assessment\": \"The assigned background states\
    \ that decarboxylation free energy can be stored as PMF. The generic observation\
    \ does not establish exact-bin specificity or universal sufficiency; detailed\
    \ biological efficacy is unassessed.\",\n      \"scope\": \"Generic statement/attribution\
    \ and literal evidence only; detailed pathogen fitness, defense, AMR, interventions\
    \ and optimization UNASSESSED_SCOPE.\"\n    },\n    {\n      \"index\": 8,\n \
    \     \"field\": \"causal_graphs[0].edges[8]\",\n      \"subject\": \"proton_motive_force\"\
    ,\n      \"predicate\": \"powers\",\n      \"object\": \"f0f1_atp_synthase\",\n\
    \      \"reference\": \"DOI:10.1093/femsre/fuad033\",\n      \"status\": \"generic_documentary_support\"\
    ,\n      \"source\": \"poolman\",\n      \"locator\": \"body paragraph5\",\n \
    \     \"assessment\": \"The assigned background supports the existing generic\
    \ PMF/ATP-synthase relationship. No exact family, organism or acid-defense intervention\
    \ claim is validated.\",\n      \"scope\": \"Generic statement/attribution and\
    \ literal evidence only; detailed pathogen fitness, defense, AMR, interventions\
    \ and optimization UNASSESSED_SCOPE.\"\n    }\n  ],\n  \"detailed_biology_scope\"\
    : \"No detailed pathogen or intervention efficacy assessed. Generic clauses may\
    \ be documentary-supported without establishing an exact numeric optimum.\"\n}"
- assessment_id: completeness
  area: completeness
  topic: 'Native checklist: whole record and optional evidence'
  outcome: supported
  target_ids:
  - METPO:1000457
  summary: All twelve nodes, nine edges, three components, three protein classes,
    two reviewed label-only classes, zero instances, one canonical and thirteen events
    are covered. No token instance, exact protein family, connector or dataset is
    required by this NONMECHANISTIC record.
  evidence_ids:
  - record
  - node-edges
  - node-sources
  - policy
  - checklist
  details: "{\n  \"completed_at\": \"2026-10-21T19:19:30.240283+00:00\",\n  \"nodes\"\
    : [\n    {\n      \"index\": 0,\n      \"node_id\": \"ph_optimum_mid2_trait\"\
    ,\n      \"label\": \"pH optimum mid2\",\n      \"node_type\": \"TRAIT\",\n  \
    \    \"status\": \"quantitative_identity\",\n      \"assessment\": \"Current exact\
    \ quantitative bin comes from captured ontology; generic sources do not independently\
    \ calibrate it.\",\n      \"incident_edges\": [\n        1,\n        2\n     \
    \ ],\n      \"direct_node_evidence_present\": false\n    },\n    {\n      \"index\"\
    : 1,\n      \"node_id\": \"ph_optimum\",\n      \"label\": \"pH optimum\",\n \
    \     \"node_type\": \"TRAIT\",\n      \"status\": \"measurement_identity\",\n\
    \      \"assessment\": \"External growth optimum differs from intracellular setpoint;\
    \ the source preserves that distinction.\",\n      \"incident_edges\": [\n   \
    \     2\n      ],\n      \"direct_node_evidence_present\": false\n    },\n   \
    \ {\n      \"index\": 2,\n      \"node_id\": \"slightly_alkaline_external_ph\"\
    ,\n      \"label\": \"slightly alkaline external pH\",\n      \"node_type\": \"\
    ENVIRONMENTAL_FACTOR\",\n      \"status\": \"qualified_context\",\n      \"assessment\"\
    : \"Near-neutral/slightly alkaline external context is general; no full support\
    \ claim for every named habitat/body-fluid example or a universal7\\u20138 band.\"\
    ,\n      \"incident_edges\": [\n        0\n      ],\n      \"direct_node_evidence_present\"\
    : false\n    },\n    {\n      \"index\": 3,\n      \"node_id\": \"modest_alkaline_homeostasis\"\
    ,\n      \"label\": \"modest alkaline pH homeostasis\",\n      \"node_type\":\
    \ \"BIOLOGICAL_PROCESS\",\n      \"status\": \"context_exact_bin_unverified\"\
    ,\n      \"assessment\": \"General homeostasis context is supported; specific\
    \ mildness, causal sufficiency and phenotype calibration are not established by\
    \ the short sources.\",\n      \"incident_edges\": [\n        0,\n        1\n\
    \      ],\n      \"direct_node_evidence_present\": false\n    },\n    {\n    \
    \  \"index\": 4,\n      \"node_id\": \"cytoplasmic_buffering_capacity\",\n   \
    \   \"label\": \"cytoplasmic buffering capacity\",\n      \"node_type\": \"CAPACITY\"\
    ,\n      \"status\": \"generic_documentary_support\",\n      \"assessment\": \"\
    Poolman paragraph4 generic buffering-capacity statement supports the described\
    \ capacity.\",\n      \"incident_edges\": [\n        3\n      ],\n      \"direct_node_evidence_present\"\
    : false\n    },\n    {\n      \"index\": 5,\n      \"node_id\": \"intracellular_ph_homeostasis\"\
    ,\n      \"label\": \"intracellular pH homeostasis\",\n      \"node_type\": \"\
    BIOLOGICAL_PROCESS\",\n      \"status\": \"generic_documentary_support\",\n  \
    \    \"assessment\": \"Generic pH-homeostasis context supported; near-neutral\
    \ language is typical context, not universal exact numeric state.\",\n      \"\
    incident_edges\": [\n        3,\n        4,\n        5,\n        6\n      ],\n\
    \      \"direct_node_evidence_present\": false\n    },\n    {\n      \"index\"\
    : 6,\n      \"node_id\": \"na_h_antiporters\",\n      \"label\": \"Na+/H+ antiporters\"\
    ,\n      \"node_type\": \"GENE_OR_PROTEIN\",\n      \"status\": \"generic_documentary_support\"\
    ,\n      \"assessment\": \"Existing generic antiporter wording appears in assigned\
    \ background; detailed organism-specific efficacy not assessed.\",\n      \"incident_edges\"\
    : [\n        4\n      ],\n      \"direct_node_evidence_present\": false\n    },\n\
    \    {\n      \"index\": 7,\n      \"node_id\": \"k_h_antiporters\",\n      \"\
    label\": \"K+/H+ antiporters\",\n      \"node_type\": \"GENE_OR_PROTEIN\",\n \
    \     \"status\": \"generic_documentary_support\",\n      \"assessment\": \"Existing\
    \ generic regulator wording appears in assigned overview; specific GO interpretation\
    \ belongs to grounding auditor.\",\n      \"incident_edges\": [\n        5\n \
    \     ],\n      \"direct_node_evidence_present\": false\n    },\n    {\n     \
    \ \"index\": 8,\n      \"node_id\": \"respiratory_proton_pumping\",\n      \"\
    label\": \"proton-pumping respiratory chain components\",\n      \"node_type\"\
    : \"PATHWAY\",\n      \"status\": \"generic_documentary_support\",\n      \"assessment\"\
    : \"Respiratory-component background appears in source; pathway/material referent\
    \ is a separate formal question.\",\n      \"incident_edges\": [\n        6\n\
    \      ],\n      \"direct_node_evidence_present\": false\n    },\n    {\n    \
    \  \"index\": 9,\n      \"node_id\": \"metabolite_decarboxylation\",\n      \"\
    label\": \"metabolite decarboxylation pathways\",\n      \"node_type\": \"PATHWAY\"\
    ,\n      \"status\": \"generic_documentary_support\",\n      \"assessment\": \"\
    Existing generic decarboxylation/energy-background statement has documentary support;\
    \ no biological reconstruction.\",\n      \"incident_edges\": [\n        7\n \
    \     ],\n      \"direct_node_evidence_present\": false\n    },\n    {\n     \
    \ \"index\": 10,\n      \"node_id\": \"proton_motive_force\",\n      \"label\"\
    : \"proton motive force\",\n      \"node_type\": \"STATE\",\n      \"status\"\
    : \"generic_documentary_support\",\n      \"assessment\": \"Actual generic PMF\
    \ definitions preserve its electrochemical-gradient meaning.\",\n      \"incident_edges\"\
    : [\n        7,\n        8\n      ],\n      \"direct_node_evidence_present\":\
    \ false\n    },\n    {\n      \"index\": 11,\n      \"node_id\": \"f0f1_atp_synthase\"\
    ,\n      \"label\": \"F0F1-ATP synthase\",\n      \"node_type\": \"GENE_OR_PROTEIN\"\
    ,\n      \"status\": \"generic_documentary_support\",\n      \"assessment\": \"\
    Existing generic synthase/PMF relation has documentary support; no protein instance\
    \ or particular mechanism established.\",\n      \"incident_edges\": [\n     \
    \   8\n      ],\n      \"direct_node_evidence_present\": false\n    }\n  ]\n}"
- assessment_id: expression
  area: evidence
  topic: 'Native checklist: canonical-only catalog applicability'
  outcome: not_applicable
  target_ids:
  - METPO:1000457
  summary: No Rubellicoccus peritrichatus, Puniceicoccus sp. CR14 or verified type-strain
    alias matches the complete retained 20-organism/28-dataset catalog. No different
    organism or strain was substituted, and no detailed defense gene/module query
    was made.
  evidence_ids:
  - expression
  - authority-reuse
- assessment_id: ownership
  area: provenance
  topic: 'Native checklist: actual maintained recurrence and history'
  outcome: supported
  target_ids:
  - METPO:1000457
  summary: The predicate table and empty-ID grounder own mapping recurrence while
    preserving existing IDs. The current PMF and buffering type writer is a direct
    owner; the PATHWAY migration has neither current node 8 nor node 9 as an exact
    key, so it is context only for their facet finding. Canonical and functional-ground
    writers retain their exact guards.
  evidence_ids:
  - owners
  - local-authority
  - ground-reading
  details: "{\n  \"completed_at\": \"2026-10-21T19:21:49.579415+00:00\",\n  \"target\"\
    : \"data/traits/environment/ph_optimum_mid2.yaml\",\n  \"counts\": {\n    \"inputs\"\
    : 75,\n    \"graphs\": 1,\n    \"nodes\": 12,\n    \"edges\": 9,\n    \"components\"\
    : 3,\n    \"protein_classes\": 3,\n    \"label_only\": 2,\n    \"protein_instances\"\
    : 0,\n    \"canonical_examples\": 1,\n    \"curation_events\": 13,\n    \"ai_events\"\
    : 12,\n    \"seed_events\": 1,\n    \"captured_histories\": 5,\n    \"matching_files\"\
    : 180,\n    \"review_target_arrays\": 67,\n    \"exact_target_arrays\": 0\n  },\n\
    \  \"search\": {\n    \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-grounding-agent/search-and-provenance.json\"\
    ,\n    \"sha256\": \"dbd38be5e966cfc4472faae4e6671db1ff85d1365dfd3895ec6b231b742a30fd\"\
    ,\n    \"bytes\": 91862\n  },\n  \"all_node_search\": {\n    \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-grounding-agent/all-node-owner-search.json\"\
    ,\n    \"sha256\": \"38df7d4f032ee61d9255502dc191cc07cadb45629f4ebd8f56c023b425a6ed05\"\
    ,\n    \"bytes\": 21206\n  },\n  \"history\": {\n    \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-optimum-mid2-grounding-agent/history-projections.json\"\
    ,\n    \"sha256\": \"b04a3b26888487b34a29d2d05d4cb128e72f294dda183965cabbec1cdbd59120\"\
    ,\n    \"bytes\": 17794\n  },\n  \"bounded_human_acceptance\": \"The exact target/ID/label/unique-bin-synonym\
    \ case-insensitive ignored-inclusive repository search yielded 180 matching files\
    \ and 67 parsed structured-review target arrays, with zero exact current-target\
    \ arrays and no parse failures. Five captured histories were fully read; their\
    \ actors are AI and they concern infrastructure/shared contexts. The 13 in-record\
    \ events comprise 12 explicitly AI-assisted events and a machine seed. A linked\
    \ current human acceptance/maintained signoff was not established within this\
    \ stated repository scope; this is not a universal claim that no human ever reviewed\
    \ the work.\",\n  \"positive_provenance\": \"Current REVIEWED status, explicit\
    \ curation history, mapped functional facets, normalization and canonical writer\
    \ provenance remain positive. AI provenance is not erased or characterized as\
    \ absent.\",\n  \"history_dispositions\": [\n    {\n      \"path\": \"history/infrastructure/inconsistent-node-type/2026-08-12T000912Z-claude-code-779670.yaml\"\
    ,\n      \"sha256\": \"adb240d907348b52784c5e2f2e4b131af124877eeaaf1805c94713342763e5dd\"\
    ,\n      \"actors\": [\n        {\n          \"type\": \"ai_agent\",\n       \
    \   \"name\": \"claude-code\"\n        }\n      ],\n      \"classification\":\
    \ \"AI infrastructure/shared context, not exact target human signoff\"\n    },\n\
    \    {\n      \"path\": \"history/infrastructure/node-type-consistency/2026-08-15T014631Z-claude-code-9d7f4d.yaml\"\
    ,\n      \"sha256\": \"21f19561c0d4769e7acc62e05e41d0d395a0f239938f00829f79f2b9c3ac2510\"\
    ,\n      \"actors\": [\n        {\n          \"type\": \"ai_agent\",\n       \
    \   \"name\": \"claude-code\"\n        }\n      ],\n      \"classification\":\
    \ \"AI infrastructure/shared context, not exact target human signoff\"\n    },\n\
    \    {\n      \"path\": \"history/infrastructure/pathway-vs-process/2026-08-16T010630Z-claude-code-192557.yaml\"\
    ,\n      \"sha256\": \"a45fff0e3ef24effb20c3b624dc14a6cab08f2094bc0f8033cd709c0cd60f012\"\
    ,\n      \"actors\": [\n        {\n          \"type\": \"ai_agent\",\n       \
    \   \"name\": \"claude-code\"\n        }\n      ],\n      \"classification\":\
    \ \"AI infrastructure/shared context, not exact target human signoff\"\n    },\n\
    \    {\n      \"path\": \"history/infrastructure/predicate-gate-audit/2026-08-16T074719Z-claude-code-84d88d.yaml\"\
    ,\n      \"sha256\": \"d1ba848e155dbd3a65905f07af5539d3d22b8873b638cc6adb48b1a0e23c0a3d\"\
    ,\n      \"actors\": [\n        {\n          \"type\": \"ai_agent\",\n       \
    \   \"name\": \"claude-code\"\n        }\n      ],\n      \"classification\":\
    \ \"AI infrastructure/shared context, not exact target human signoff\"\n    },\n\
    \    {\n      \"path\": \"history/other/canonical-examples-six/2026-08-21T065406Z-codex-a1ab82.yaml\"\
    ,\n      \"sha256\": \"23be5f6ab519511e3e23feffa85813eec4fa3c7e6b900e77fd4a3adc0c26da0e\"\
    ,\n      \"actors\": [\n        {\n          \"type\": \"ai_agent\",\n       \
    \   \"name\": \"codex\",\n          \"model\": \"gpt-5\",\n          \"agent_tool\"\
    : \"codex\"\n        }\n      ],\n      \"classification\": \"AI infrastructure/shared\
    \ context, not exact target human signoff\"\n    }\n  ],\n  \"owners\": [\n  \
    \  {\n      \"path\": \"data/traits/environment/ph_optimum_mid2.yaml\",\n    \
    \  \"role\": \"Primary owner of current aliases, node wording/type, imported edge\
    \ choices and acceptance traceability.\",\n      \"sha256\": \"6e2a9f141a0e75fc3f0f92643724bab5473f925edb95f778dbe9060a9b2e3506\"\
    \n    },\n    {\n      \"path\": \"mappings/predicate_grounding.tsv\",\n     \
    \ \"role\": \"Maintained rows 11 regulates and 24 generates supply the imported\
    \ edge meanings with wildcard gates; row 102 confers and row 111 powers are explicitly\
    \ gated local mappings. A wildcard local gate does not establish external ontology\
    \ compatibility.\",\n      \"sha256\": \"8e28c19e93aca3dc164a3befbe2612b289241de457c59f499e65936c03b7ce52\"\
    \n    },\n    {\n      \"path\": \"scripts/ground_causal_predicates.py\",\n  \
    \    \"role\": \"Recurrence owner for filling missing predicate IDs; skips every\
    \ existing nonempty predicate_id. Mapping corrections alone would not repair current\
    \ edges 5/7.\",\n      \"sha256\": \"5a788eeaabf3a56b0d82c469a3e3fe28f1d51707d9382313b9a94289be7d1381\"\
    \n    },\n    {\n      \"path\": \"mappings/node_grounding.tsv\",\n      \"role\"\
    : \"Row 279 permits K+/H+ protein-family closeMatch to GO:0015386; supports valid\
    \ functional facet, not process retyping.\",\n      \"sha256\": \"d7de9b3ab04960c4775a5bc295a945bd1a72d81467830459f4793e654f82b3d0\"\
    \n    },\n    {\n      \"path\": \"scripts/ground_causal_nodes.py\",\n      \"\
    role\": \"Fills missing node grounds, skips existing nonempty grounds and respects\
    \ reviewed label-only status. Current GO ground is preserved.\",\n      \"sha256\"\
    : \"204ce4162544154b1752b65da2136538847ea25ced26a52f5708eadff08f5d42\"\n    },\n\
    \    {\n      \"path\": \"scripts/migrate_uniprot_instance_groundings.py\",\n\
    \      \"role\": \"Exact case-folded K+/H+ label replacement to GO:0015386; applies\
    \ only when existing ground begins UniProtKB. Current GO grounding is already\
    \ a no-op.\",\n      \"sha256\": \"07d2a5405cff5857239757e0a3791f411b1d25709a5760c1e49553eed066993d\"\
    \n    },\n    {\n      \"path\": \"scripts/migrate_node_type_consistency.py\"\
    ,\n      \"role\": \"Direct current PMF\\u2192STATE and cytoplasmic buffering\\\
    u2192CAPACITY RETYPE owner. It does not contain respiratory_proton_pumping or\
    \ metabolite_decarboxylation as exact keys, so it is not assigned recurrence ownership\
    \ of the facet finding.\",\n      \"sha256\": \"a3e7bc170e60f406a73e06c893d74f5253671028d3d40cc15ecf882b6684a69e\"\
    \n    },\n    {\n      \"path\": \"scripts/migrate_pathway_vs_process.py\",\n\
    \      \"role\": \"Convention and analogous reaction-class context only: TARGET\
    \ contains electron_transport_chain, aa_decarboxylation and amino_acid_decarboxylation,\
    \ but not either current node 8/9 key. Do not claim it currently rewrites those\
    \ nodes.\",\n      \"sha256\": \"f236de7183048732e9001b7fac4367affff58d8b7a7d5c63286e6b058a4b38c2\"\
    \n    },\n    {\n      \"path\": \"scripts/backfill_canonical_examples_444.py\"\
    ,\n      \"role\": \"Direct current canonical source/note table entry. Guarded\
    \ live queue, exact-existing-example no-op and nonempty-drift rejection preserve\
    \ its provenance.\",\n      \"sha256\": \"18ca0766789c239d693ef665e8b1d43c1209a0f414a326f1c5d890f88de7b20c\"\
    \n    },\n    {\n      \"path\": \"research/traits/environment/ph_optimum_mid2-deep-research-falcon.md\"\
    ,\n      \"role\": \"Current August 4 Falcon report is contextual provenance,\
    \ not proof that its exact current bytes were the June 23 enrichment input. No\
    \ paid run or mechanistic recommendations adopted.\",\n      \"sha256\": \"fd8bcade02db10fa4fe369f18863f876ac8c5bbc6559ff0d2d8ca29d00fca738\"\
    \n    }\n  ],\n  \"readiness\": \"The NONMECHANISTIC quantitative graph does not\
    \ require token protein instances, extra connectors or mandatory expression datasets.\
    \ Three protein classes, two reviewed label-only dispositions and zero instances\
    \ are legitimate retained coverage. Three disconnected components are documented,\
    \ not an automatic finding.\",\n  \"proposed_facet_owner\": [\n    \"data/traits/environment/ph_optimum_mid2.yaml\"\
    \n  ],\n  \"proposed_relation_owners\": [\n    \"data/traits/environment/ph_optimum_mid2.yaml\"\
    ,\n    \"mappings/predicate_grounding.tsv\",\n    \"scripts/ground_causal_predicates.py\"\
    \n  ],\n  \"proposed_human_owner\": [\n    \"data/traits/environment/ph_optimum_mid2.yaml\"\
    \n  ]\n}"
- assessment_id: human-acceptance
  area: provenance
  topic: 'Native checklist: bounded human acceptance traceability'
  outcome: concern
  target_ids:
  - METPO:1000457
  summary: Ignored-inclusive exact target/ID/label search found 180 files, 67 actual
    structured-review target arrays and zero exact target arrays. Thirteen record
    events comprise twelve AI events and a machine seed; five captured histories were
    fully read and have AI actors. Positive provenance and REVIEWED do not identify
    a linked human acceptance decision within this bounded scope.
  evidence_ids:
  - owners
  - playbook
  - challenge
  - adjudication
- assessment_id: readiness
  area: consistency
  topic: 'Native checklist: actual focused checks and qualified common reuse'
  outcome: supported
  target_ids:
  - METPO:1000457
  summary: Native, strict and snippet checks passed directly; all 75 captured inputs
    and frozen manifests match. B10 common results retain original failures, retries,
    skips and timestamps, with actual B11 byte qualification and independent verification;
    no new B11 final QC execution is claimed.
  evidence_ids:
  - capture
  - reuse
  - reuse-postcheck
  - native-checks
  - check-ph-optimum-mid2-native
  - check-ph-optimum-mid2-strict
  - check-ph-optimum-mid2-snippets
findings:
- finding_id: exact-alias-scope
  issue_key: ph-optimum-mid2-exact-alias-scope
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Two exact aliases are not coextensive with the 7–8 optimum class
  description: Actual assigned Krulwich classification includes an alkaliphile with
    optimum extending to about pH 10.5, and the explicit supplemental classification
    uses 7–9 for alkali-tolerant optima. Both exceed this numerical class. Faithful
    upstream import is positive provenance, not proof of scientific equivalence. No
    Neutrophile defect or universal nomenclature rule is added.
  target_ids:
  - METPO:1000457
  field_paths:
  - synonyms[0]
  - synonyms[1]
  evidence_ids:
  - synonym-scope
  - alkaliphile-scope
  - alkali-tolerant-scope
  - metpo-primary
  - challenge
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_optimum_mid2.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: imported-relation-subjects
  issue_key: ph-optimum-mid2-imported-relation-subjects
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Imported process and material-producer relations have mismatched subjects
  description: RO:0002211 requires a regulating process; the current K+/H+ antiporter
    subject is a protein class despite its allowed functional GO grounding. Biolink
    produces describes a material producer, while the current decarboxylation subject
    is a reaction/pathway. The latter is a textual semantic conflict; its inherited
    formal endpoints remain named thing and no material-only product range is asserted.
  target_ids:
  - METPO:1000457
  field_paths:
  - causal_graphs[0].edges[5]
  - causal_graphs[0].edges[7]
  evidence_ids:
  - node-edges
  - ro-primary
  - biolink-primary
  - go-primary
  - policy
  - owners
  - challenge
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_optimum_mid2.yaml
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
- finding_id: pathway-referent-precision
  issue_key: ph-optimum-mid2-pathway-referent-precision
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Two PATHWAY nodes need bounded referent precision
  description: Node 8 names respiratory chain components as material entities while
    its type and ID suggest a route/activity. Node 9 describes a reaction class while
    the native PATHWAY convention distinguishes named enumerable routes. Clarify the
    intended existing referents without reconstructing a pathway or assigning biological
    falsity. No exact recurrence key for these two nodes was established in the contextual
    migration writer.
  target_ids:
  - METPO:1000457
  field_paths:
  - causal_graphs[0].nodes[8]
  - causal_graphs[0].nodes[9]
  evidence_ids:
  - node-edges
  - schema
  - playbook
  - owners
  - challenge
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_optimum_mid2.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: human-acceptance-link
  issue_key: ph-optimum-mid2-human-acceptance-link
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Bounded local provenance lacks a linked human acceptance decision
  description: The 180-path/67-array/zero-exact search, thirteen record events and
    five AI histories preserve positive maintenance provenance but do not identify
    attributable current human scientific acceptance. This bounded result does not
    assert absence of remote or private decisions.
  target_ids:
  - METPO:1000457
  field_paths:
  - mapping_status
  - curation_history
  evidence_ids:
  - owners
  - playbook
  - challenge
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_optimum_mid2.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
actions:
- action_id: reconcile-exact-aliases
  description: Reconcile or qualify the two exact aliases during separately authorized
    curation while preserving the active numerical class.
  finding_ids:
  - exact-alias-scope
  target_ids:
  - METPO:1000457
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_optimum_mid2.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Preserve the faithful pinned-METPO import and the positive canonical optimum;
    distinguish source classification conventions from whole-bin equivalence.
  - Limit the confirmed fields to synonyms 0/1 unless new evidence supports further
    change.
  - Use guarded record/repository history, applicable native/strict/identity checks
    and a successor review after changed inputs.
- action_id: reconcile-imported-roles
  description: Reconcile the imported edge meanings with the represented subjects
    during authorized curation.
  finding_ids:
  - imported-relation-subjects
  target_ids:
  - METPO:1000457
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_optimum_mid2.yaml
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
  - Distinguish the firm RO process domain from Biolink textual material-subject meaning
    and broad formal endpoints; preserve allowed GO functional grounding.
  - Inspect empty-ID refill and nonempty-ID preservation so mapping edits are not
    misrepresented as repairing current edges.
  - Do not prescribe a new biological pathway, intervention, experimental condition
    or efficacy claim; use guarded history and appropriate native/strict/QC checks.
- action_id: clarify-node-facets
  description: Clarify the two existing PATHWAY referents against the native convention.
  finding_ids:
  - pathway-referent-precision
  target_ids:
  - METPO:1000457
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_optimum_mid2.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Document whether node 8 intends existing components or a route/activity, and whether
    node 9 denotes a reaction class or a named route. Review incident relations consistently.
  - The current record is the established owner; the pathway migration is context,
    not a proven direct-key recurrence writer.
  - Do not add a token protein, new mechanism, forced connector or optimization; preserve
    source meaning and guarded history.
- action_id: link-human-acceptance
  description: Link attributable human acceptance if available, or clarify status
    while preserving bounded uncertainty.
  finding_ids:
  - human-acceptance-link
  target_ids:
  - METPO:1000457
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_optimum_mid2.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Retain the 180/67/0 ignored-inclusive basis and distinguish thirteen record events
    from five fully read AI histories.
  - Do not infer human acceptance from AI maintenance, REVIEWED, validators or ontology
    authorship.
  - No contact with other people or automatic status promotion is authorized by this
    proposed action.
limitations:
- Detailed pathogen acid-defense, fitness, AMR, perturbation and intervention biology
  remains UNASSESSED_SCOPE; generic documentary support is not efficacy certification
  or mechanism optimization.
- The exact alias finding is limited to Alkali Tolerant and Alkaliphile. Neutrophile
  is not independently refuted, and source conventions are not imposed as universal
  nomenclature.
- Three snippet occurrences are literal. Baker full-body wording remains unknown in
  the retained access scope, not false; canonical phenotype support is actual abstract
  text only.
- Generic background does not establish exact 7–8 calibration, sufficient mild homeostasis
  in every organism, or universal habitat claims. No full-article mechanistic reading
  is claimed.
- GO molecular-function grounding is allowed for a protein-family facet. Node 3 explicitly
  denotes activity; no prior sibling demand-amount finding applies. Local powers explicitly
  accepts the current state-to-machine shape.
- Biolink produces has broad named-thing formal endpoints. The imported subject finding
  concerns its textual material-producer meaning; no hard material product range is
  inferred.
- The node-facet minor is documentary precision, separate from the imported-role major.
  A process retype alone would not resolve the Biolink subject meaning. No exact writer
  key was established for current nodes 8/9.
- Original BioC 07:57:33, publisher HTML 07:56:32–07:56:36, Poolman JATS 10:34:33–10:34:34
  and supplemental JATS 18:33:30–18:33:31 acquisitions remain distinct from current
  copying and selected reading. Fresh assigned metadata acquisition at 19:12:28 preceded
  capture; interpretation followed capture.
- All focused checks passed directly; no sibling inspect-cache failure, snippet DNS
  retry or taxonomy failure applies. Historical common failures/retries/skips and
  corrected read-only projection errors remain explicitly qualified.
- Ignored-inclusive repository search cannot establish absence of remote/private acceptance.
  The retained complete catalog has no canonical match; no substitute strain or detailed
  defense query was used.
notes:
- 'Final root disposition: two major findings, two minor findings, fourteen assessments
  and four linked proposed actions.'
- 'Coverage: 75 inputs, 32 frozen source artifacts, 21 frozen grounding artifacts,
  twelve nodes, nine edges, three components, three protein classes, two label-only
  classes, zero instances, one canonical and thirteen events. Four assigned works
  plus one supplemental work, twelve external and four ontology-source placements,
  four snippets with three literal and one unknown.'
- This review is emitted by the single-use serializer after its static preparation.
  The execution receipt records serialization; root owns native review validation
  and save. Serialization does not edit the scientific record, persistent sweep state
  or Git.
tags:
- record-review
- ph-optimum-mid2
- environment
- needs-curation
native_verdict: needs_curation
```
