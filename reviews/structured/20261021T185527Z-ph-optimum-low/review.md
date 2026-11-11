# Whole-record review of pH optimum low

- Review: 20261021T185527Z-ph-optimum-low
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-21T18:43:15.841185Z
- Finished UTC: 2026-10-21T18:55:27Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Needs curation: two majors address exact-alias scope and imported regulation endpoints; two minors address gradient/process precision and bounded human acceptance. Active identity, parent and canonical optimum remain positive. All four snippets have literal or meaning-equivalent typography support.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: Ninth record of batch 010 in path order. Whole-target reading and successful 64-input capture precede substantive assessment. Metadata acquisition preceded capture, with interpretation afterwards. Frozen source and grounding manifests, independent challenge and final root adjudication are mandatory before serialization.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8eee04a8c65609fbaff6df7c54597dcaf1b9d282.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| METPO:1000455 | data/traits/environment/ph_optimum_low.yaml | maintained | pH optimum low |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full-corpus graph audit | passed | True | METPO:1000455 | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| Full-corpus snippet audit | passed | True | METPO:1000455 | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| Full-corpus pathway links | passed | True | METPO:1000455 | 19 links checked against the pinned PathwayMech snapshot. Target asserts no pathway context link. |
| Full-corpus history integrity | passed | True | METPO:1000455 | 1277 history records checked, zero invalid links at the 8eee source base; integrity does not establish science or human acceptance. |
| Initial full-product validation | failed | False | METPO:1000455 | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation with isolated local cache | failed | False | METPO:1000455 | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation after isolated-cache download | passed | True | METPO:1000455 | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| Focused native validation | passed | True | METPO:1000455 | Passed directly at 18:43:29–18:43:30 UTC on the unchanged target. |
| Focused strict validation | passed | True | METPO:1000455 | Passed directly at 18:43:29–18:43:30 UTC; structural validity is distinct from imported relation semantics. |
| Focused snippet verification | passed | True | METPO:1000455 | Passed directly at 18:43:34–18:43:37 UTC: four fields, two VERIFIED and two NOT_IN_ABSTRACT. Manual primary checking finds two literal and two hyphen/en-dash normalized phrases, with none unverified. |
| Reused corpus protein/taxon audit | passed | True | METPO:1000455 | Original B4 08:55:04–08:55:10 UTC pass with unchanged inputs; zero target instances, so no new instance audit is claimed. |
| Reused maintained batch-nine QC | passed | True | METPO:1000455 | Original B9 17:05:16–17:06:53 UTC pass with B10 byte qualification; not a new final QC execution. |
| Protein-instance metadata applicability | not_applicable | False | METPO:1000455 | One contextual label-only protein class and zero instances; no token accession requirement. |

## Scientific And Domain Assessments

### Native checklist: active term, definition and hierarchy

identity: supported. Targets: METPO:1000455.

Active METPO:1000455, parent 1000331 and explicit obsolete 0000177 replacement agree. The source numerical class is inclusive 0–6; at or below approximately 6 is coherent with its boundary.

### Native checklist: exact aliases versus numerical scope

identity: concern. Targets: METPO:1000455.

Acid Tolerant, Acidophile and Extreme Acidophile are faithfully inherited EXACT aliases, but the assigned primary distinction and definitions do not establish equivalence to the whole 0–6 optimum class. Only indices 0/1/2 are confirmed fields. Indices 3/4 remain unestablished source scope, not additional findings.

### Native checklist: quantitative phenotype and generic graph context

scope: supported. Targets: METPO:1000455.

ENVIRONMENT, CLASS and NONMECHANISTIC fit the quantitative bin. Five components and one label-only class without instances are allowed; generic context is not automatically a universal mechanism claim.

### Native checklist: named canonical identity and optimum

evidence: supported. Targets: METPO:1000455.

The actual Picrophilus oshimae abstract directly states optimum pH 0.7, within the current bin, separately from its growth limit. Current official taxonomy and historical source names are retained as distinct documentary scopes.

### Native checklist: four works and eleven placements

evidence: supported. Targets: METPO:1000455.

All assigned publication identities resolve and all eleven external placements are covered on actual abstract, publisher or selected JATS surfaces. Metadata timing is distinct from later primary-body reading.

{
  "completed_at": "2026-10-21T18:49:09.872527+00:00",
  "target": "data/traits/environment/ph_optimum_low.yaml",
  "target_sha256": "eda82a5cfdd4b820895dbe955872248a5ba07079b6aab93450d332b25498eb41",
  "capture": {
    "path": "/private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low.inspect.json",
    "sha256": "6d61baf2f440a83b5c33a393ec522f760377168dc08bed4891de4cc201244157",
    "bytes": 13044
  },
  "capture_inputs": 64,
  "counts": {
    "works": 4,
    "literal_reference_forms": 4,
    "external_placements": 11,
    "ontology_source_placements": 0,
    "nodes": 12,
    "edges": 7,
    "snippets": 4,
    "exact_snippets": 2,
    "typography_normalized_snippets": 2,
    "unverified_snippets": 0,
    "canonical_examples": 1
  },
  "source_only_findings": [
    {
      "severity": "major",
      "area": "identity",
      "field_paths": [
        "synonyms[0]",
        "synonyms[1]",
        "synonyms[2]"
      ],
      "summary": "The three supplied EXACT aliases do not establish equivalence to the entire numerical optimum interval.",
      "reasoning": "The publisher distinguishes near-neutral optimal growth from survival or growth during acidic exposure, so acid tolerance is not the same measurement as low optimum. The assigned Baker abstract calls organisms with growth optimum below pH 3 acidophiles; Frontiers uses that threshold for extreme acidophiles. These stated categories do not cover the entire pinned inclusive 0\u20136 bin. Exact equivalence therefore alters class membership/retrieval.",
      "qualifications": [
        "All aliases are faithfully inherited from pinned METPO; no local transcription error is claimed.",
        "The &lt;3 thresholds are the assigned sources' stated conventions, not a universal rule imposed across every publication.",
        "The current numeric identity and canonical optimum remain positive.",
        "Indices 3 and 4 were checked as supplied aliases but their exact scope is not established in inspected primary surfaces; they are not automatically added findings.",
        "No biological pathway, defense target, intervention or optimized condition is proposed."
      ],
      "bounded_action": "Reconcile or qualify the three exact aliases during separately authorized curation, preserving upstream provenance and numerical identity."
    }
  ],
  "source_only_major_candidates": [
    {
      "severity": "major",
      "area": "identity",
      "field_paths": [
        "synonyms[0]",
        "synonyms[1]",
        "synonyms[2]"
      ],
      "summary": "The three supplied EXACT aliases do not establish equivalence to the entire numerical optimum interval.",
      "reasoning": "The publisher distinguishes near-neutral optimal growth from survival or growth during acidic exposure, so acid tolerance is not the same measurement as low optimum. The assigned Baker abstract calls organisms with growth optimum below pH 3 acidophiles; Frontiers uses that threshold for extreme acidophiles. These stated categories do not cover the entire pinned inclusive 0\u20136 bin. Exact equivalence therefore alters class membership/retrieval.",
      "qualifications": [
        "All aliases are faithfully inherited from pinned METPO; no local transcription error is claimed.",
        "The &lt;3 thresholds are the assigned sources' stated conventions, not a universal rule imposed across every publication.",
        "The current numeric identity and canonical optimum remain positive.",
        "Indices 3 and 4 were checked as supplied aliases but their exact scope is not established in inspected primary surfaces; they are not automatically added findings.",
        "No biological pathway, defense target, intervention or optimized condition is proposed."
      ],
      "bounded_action": "Reconcile or qualify the three exact aliases during separately authorized curation, preserving upstream provenance and numerical identity."
    }
  ],
  "source_only_minor_candidates": [],
  "unassessed_biological_edge_indices": [
    5
  ],
  "summary": "Four assigned identities and all eleven external placements are covered. All four snippets are supported: two literal and two typography-normalized. Canonical optimum pH 0.7 is direct. One grouped source/identity major concerns exact synonym equivalence at indices 0/1/2; no quotation or canonical finding. Generic existing source context remains positive, while detailed acid-defense/fitness/intervention biology is unassessed.",
  "qualifications": [
    "Exact upstream import is positive provenance, not proof of physiological equivalence.",
    "Only the three independently grounded alias mismatches are finding fields; indices 3/4 remain scope limitations rather than inherited-major assumptions.",
    "Meaning-equivalent hyphen/en-dash normalization is not a false-quotation finding.",
    "Source context and the numeric bin are distinct; no universal mechanism, perturbation assay or new optimal condition is inferred.",
    "Original publication-body and metadata acquisition times are retained, distinct from current selected reading."
  ]
}

### Native checklist: four assigned quotations

evidence: supported. Targets: METPO:1000455.

Two phrases are literal and the two repeated growing-at-pH phrases differ only by hyphen versus en dash. Meaning is preserved; no extra typography or false-quotation finding is added. Native two verified/two abstract nonmatches is distinct from manual primary verification.

{
  "completed_at": "2026-10-21T18:49:09.868915+00:00",
  "counts": {
    "total": 4,
    "exact": 2,
    "typography_normalized": 2,
    "unverified": 0
  },
  "snippets": [
    {
      "field": "evidence[0].snippet",
      "reference": "DOI:10.1038/nrmicro2549",
      "snippet": "growing at pH 1.0-3.0",
      "status": "typography_normalized",
      "source": {
        "path": "/private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-agent/krulwich-publisher.html",
        "sha256": "4cd2836049dc36e43c7d3d33561d1aa0b33f542eac252b37dd8275cea7fceb66",
        "bytes": 634100
      },
      "locator": "Publisher second Key Point",
      "qualification": "Only ASCII hyphen versus en dash in the numerical interval differs; scientific meaning is unchanged, no additional finding."
    },
    {
      "field": "causal_graphs[0].edges[0].evidence[0].snippet",
      "reference": "DOI:10.1016/j.tim.2007.02.005",
      "snippet": "highly impermeable cell membranes",
      "status": "exact",
      "source": {
        "path": "/private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-agent/baker-metadata.json",
        "sha256": "a78777bc3bb6444b32e2e8a13ab72c56d80592b97e30c9b5520c67cc040c631b",
        "bytes": 4065
      },
      "locator": "Actual indexed primary-review abstract",
      "qualification": "Exact words; no body reading claimed."
    },
    {
      "field": "causal_graphs[0].edges[1].evidence[0].snippet",
      "reference": "DOI:10.1038/nrmicro2549",
      "snippet": "growing at pH 1.0-3.0",
      "status": "typography_normalized",
      "source": {
        "path": "/private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-agent/krulwich-publisher.html",
        "sha256": "4cd2836049dc36e43c7d3d33561d1aa0b33f542eac252b37dd8275cea7fceb66",
        "bytes": 634100
      },
      "locator": "Publisher second Key Point",
      "qualification": "Only ASCII hyphen versus en dash in the numerical interval differs; scientific meaning is unchanged, no additional finding."
    },
    {
      "field": "causal_graphs[0].edges[2].evidence[0].snippet",
      "reference": "DOI:10.1038/nrmicro2549",
      "snippet": "cytoplasmic pH",
      "status": "exact",
      "source": {
        "path": "/private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-agent/krulwich-publisher.html",
        "sha256": "4cd2836049dc36e43c7d3d33561d1aa0b33f542eac252b37dd8275cea7fceb66",
        "bytes": 634100
      },
      "locator": "Publisher abstract and Key Points",
      "qualification": "Literal short phrase does not itself establish a quantitative growth-optimum bin."
    }
  ]
}

### Native checklist: all twelve node referents

grounding: concern. Targets: METPO:1000455.

The explicit transmembrane gradient at node 5 is typed as a process rather than the gradient state. The intended meaning remains readable, so this is bounded facet precision. Native physical-component localization is allowed; no automatic membrane typing defect or compulsory protein is inferred.

[
  {
    "index": 0,
    "field_path": "causal_graphs[0].nodes[0]",
    "node": {
      "node_id": "ph_optimum_low_trait",
      "label": "pH optimum low",
      "node_type": "TRAIT",
      "grounding": "METPO:1000455",
      "description": "pH optimum at or below ~6."
    },
    "assessment": "Active exact numerical low-optimum trait. Pinned METPO explicitly constrains the optimum to inclusive 0\u20136. Approximate local wording is not an independently demonstrated boundary error."
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
    "assessment": "Active exact parent pH optimum; direct raw-METPO parent relation is positive."
  },
  {
    "index": 2,
    "field_path": "causal_graphs[0].nodes[2]",
    "node": {
      "node_id": "acidic_external_ph",
      "label": "acidic external pH",
      "node_type": "ENVIRONMENTAL_FACTOR",
      "description": "External pH \u2264 ~6, typical of acidic mine drainage and acidic soils.",
      "grounding": "PATO:0001429"
    },
    "assessment": "Environmental acidity condition with active PATO:0001429 acidic grounding. PATO describes acidity rather than independently calibrating this numerical bin."
  },
  {
    "index": 3,
    "field_path": "causal_graphs[0].nodes[3]",
    "node": {
      "node_id": "acidophile_proton_exclusion",
      "label": "acidophile proton-exclusion physiology",
      "node_type": "BIOLOGICAL_PROCESS",
      "description": "Low-permeability membranes and reversed membrane potential that exclude protons in acidophiles."
    },
    "assessment": "Physiological umbrella can denote proton-exclusion processes even though the description mentions membranes and a state. Retain this shorthand as a qualified limitation, not an automatic material/process finding."
  },
  {
    "index": 4,
    "field_path": "causal_graphs[0].nodes[4]",
    "node": {
      "node_id": "low_external_ph",
      "label": "low external pH",
      "node_type": "ENVIRONMENTAL_FACTOR",
      "description": "Acidic medium external pH below ~3 imposing a steep proton gradient."
    },
    "assessment": "External acidic condition, not an inferred new intervention or optimized growth instruction. Source scope remains separately assessed."
  },
  {
    "index": 5,
    "field_path": "causal_graphs[0].nodes[5]",
    "node": {
      "node_id": "transmembrane_ph_gradient",
      "label": "large transmembrane pH gradient",
      "node_type": "BIOLOGICAL_PROCESS",
      "description": "Steep outside-to-inside proton (delta pH) gradient maintained by acidophiles."
    },
    "assessment": "Bounded facet precision issue: the explicit label and description denote the maintained transmembrane gradient, while BIOLOGICAL_PROCESS denotes its establishment or another process. The native STATE definition expressly distinguishes these senses."
  },
  {
    "index": 6,
    "field_path": "causal_graphs[0].nodes[6]",
    "node": {
      "node_id": "reversed_membrane_potential",
      "label": "inside-positive (reversed) membrane potential",
      "node_type": "STATE",
      "description": "Reversed (inside-positive) membrane potential creating an electrochemical barrier to proton influx."
    },
    "assessment": "Inside-positive membrane potential is explicitly STATE; maintained migration and current description agree. No repeated process/state defect here."
  },
  {
    "index": 7,
    "field_path": "causal_graphs[0].nodes[7]",
    "node": {
      "node_id": "proton_influx",
      "label": "proton influx",
      "node_type": "BIOLOGICAL_PROCESS",
      "description": "Passive entry of protons into the cytoplasm down the pH gradient."
    },
    "assessment": "Proton influx is explicitly an entry process. Formal referent is coherent; this does not certify detailed efficacy in pathogenic organisms."
  },
  {
    "index": 8,
    "field_path": "causal_graphs[0].nodes[8]",
    "node": {
      "node_id": "proton_pumping_respiratory_complexes",
      "label": "proton-pumping respiratory complexes",
      "node_type": "GENE_OR_PROTEIN",
      "grounding_status": "REVIEWED_LABEL_ONLY",
      "grounding_notes": "Reviewed as a contextual protein or protein-complex label within a quantitative measurement graph; no exact semantic family term was established for this aggregate use.",
      "description": "Respiratory chain complexes (I, III, IV) that actively extrude cytoplasmic protons."
    },
    "assessment": "Reviewed label-only protein-complex aggregate is a material contextual class. No exact family or protein instance is required by the quantitative NONMECHANISTIC scope; detailed acid-defense/fitness/intervention efficacy remains UNASSESSED_SCOPE."
  },
  {
    "index": 9,
    "field_path": "causal_graphs[0].nodes[9]",
    "node": {
      "node_id": "cytoplasmic_proton_load",
      "label": "cytoplasmic proton load",
      "node_type": "STATE",
      "description": "Concentration of protons in the cytoplasm threatening near-neutral intracellular pH."
    },
    "assessment": "Cytoplasmic load is a steady molecular value represented as STATE; no additional automatic QUALITY finding is imposed."
  },
  {
    "index": 10,
    "field_path": "causal_graphs[0].nodes[10]",
    "node": {
      "node_id": "proton_impermeable_membrane",
      "label": "rigid proton-impermeable membrane",
      "node_type": "CELLULAR_LOCALIZATION",
      "description": "Rigid membrane highly resistant to proton influx, reducing passive proton permeability."
    },
    "assessment": "Explicit membrane is material, consistent with cellular component/localization. Its role as subject of RO:0002212 is separately incompatible with that processual relation."
  },
  {
    "index": 11,
    "field_path": "causal_graphs[0].nodes[11]",
    "node": {
      "node_id": "passive_proton_permeability",
      "label": "passive proton permeability",
      "node_type": "QUALITY",
      "description": "Rate of passive proton leakage across the cell membrane."
    },
    "assessment": "Permeability is explicitly a measurable QUALITY. Its role as object of RO:0002212 is separately incompatible with that processual relation."
  }
]

### Native checklist: all seven edge meanings

consistency: concern. Targets: METPO:1000455.

Edge 6 uses imported process regulation between a material membrane and a permeability quality. This is a firm referent conflict, independent of positive generic source context. Local predicates retain their approved broad meanings; free relations are not assigned invented RO restrictions.

[
  {
    "index": 0,
    "field_path": "causal_graphs[0].edges[0]",
    "edge": {
      "subject": "acidic_external_ph",
      "predicate": "selects for",
      "object": "acidophile_proton_exclusion",
      "description": "Acidic environments select for proton-exclusion physiology.",
      "evidence": [
        {
          "reference": "DOI:10.1016/j.tim.2007.02.005",
          "snippet": "highly impermeable cell membranes",
          "notes": "Supports envelope-based proton barriers as the selected acidophile mechanism."
        }
      ],
      "predicate_id": "METPO:2007401"
    },
    "disposition": "qualified",
    "assessment": "The local proposed selects-for relation has broad causal-node endpoints and evolutionary-selection semantics. The process umbrella can refer to adapted physiology. Do not invent a hard ENVIRONMENTAL_FACTOR exclusion or claim a newly demonstrated evolutionary experiment."
  },
  {
    "index": 1,
    "field_path": "causal_graphs[0].edges[1]",
    "edge": {
      "subject": "acidophile_proton_exclusion",
      "predicate": "confers",
      "object": "ph_optimum_low_trait",
      "description": "Acidophile proton-exclusion physiology yields an acidic pH-optimum setpoint.",
      "evidence": [
        {
          "reference": "DOI:10.1038/nrmicro2549",
          "snippet": "growing at pH 1.0-3.0",
          "notes": "Supports growth at strongly acidic pH as the acidophile outcome."
        }
      ],
      "predicate_id": "METPO:2007700"
    },
    "disposition": "compatible",
    "assessment": "Captured v8 confers explicitly permits a process subject and trait object. Generic physiological context does not independently establish exact-bin sufficiency, which remains a source limitation rather than a formal endpoint defect."
  },
  {
    "index": 2,
    "field_path": "causal_graphs[0].edges[2]",
    "edge": {
      "subject": "ph_optimum_low_trait",
      "predicate": "is a",
      "object": "ph_optimum",
      "description": "pH optimum low is a quantitative bin of the pH-optimum phenotype.",
      "evidence": [
        {
          "reference": "DOI:10.1038/nrmicro2549",
          "snippet": "cytoplasmic pH",
          "notes": "Supports an acidic optimum as a value within the pH-optimum distribution."
        }
      ],
      "predicate_id": "rdfs:subClassOf"
    },
    "disposition": "compatible",
    "assessment": "The trait-to-parent rdfs:subClassOf edge is directly supported by pinned raw METPO; its short scientific snippet need not independently prove the asserted ontology hierarchy."
  },
  {
    "index": 3,
    "field_path": "causal_graphs[0].edges[3]",
    "edge": {
      "subject": "low_external_ph",
      "predicate": "drives",
      "object": "transmembrane_ph_gradient",
      "description": "Acidic external pH forces acidophiles to sustain a large transmembrane pH gradient.",
      "evidence": [
        {
          "reference": "DOI:10.1038/nrmicro2549",
          "notes": "cytoplasmic pH ~6.0 while growing at external pH &lt;3; broad physiological input edge."
        }
      ]
    },
    "disposition": "qualified",
    "assessment": "Free drives has no imported formal endpoint rule. The object gradient/process precision is addressed once at node 5; no additional role-major or required mechanism is inferred."
  },
  {
    "index": 4,
    "field_path": "causal_graphs[0].edges[4]",
    "edge": {
      "subject": "reversed_membrane_potential",
      "predicate": "counteracts",
      "object": "proton_influx",
      "description": "A reversed inside-positive membrane potential electrostatically opposes proton entry.",
      "evidence": [
        {
          "reference": "DOI:10.1038/nrmicro2549",
          "notes": "sustain a large delta pH with a reversed inside-positive membrane potential; hallmark of extreme acidophiles."
        },
        {
          "reference": "DOI:10.3389/fmicb.2023.1149903",
          "notes": "inside positive membrane potential creates an electrochemical barrier to proton influx."
        }
      ]
    },
    "disposition": "compatible",
    "assessment": "Free counteracts has no imported formal process-only rule. STATE-to-process formal wording is not itself a defect; no detailed mechanism reconstruction is performed."
  },
  {
    "index": 5,
    "field_path": "causal_graphs[0].edges[5]",
    "edge": {
      "subject": "proton_pumping_respiratory_complexes",
      "predicate": "removes",
      "object": "cytoplasmic_proton_load",
      "description": "Proton-pumping respiratory complexes actively extrude protons to lower cytoplasmic proton load.",
      "evidence": [
        {
          "reference": "DOI:10.1038/nrmicro2549",
          "notes": "increased expression of proton-pumping respiratory chain complexes; broad mechanism, specific complexes vary by lineage."
        }
      ]
    },
    "disposition": "documentary_only",
    "assessment": "Free removes has no imported hard endpoint rule. Material complex to steady proton-load description is documented; detailed pathogen acid-defense/fitness/intervention efficacy is UNASSESSED_SCOPE."
  },
  {
    "index": 6,
    "field_path": "causal_graphs[0].edges[6]",
    "edge": {
      "subject": "proton_impermeable_membrane",
      "predicate": "decreases",
      "object": "passive_proton_permeability",
      "description": "A rigid proton-impermeable membrane reduces passive proton leak and the energetic burden of pH homeostasis.",
      "evidence": [
        {
          "reference": "DOI:10.3389/fmicb.2023.1149903",
          "notes": "rigid and impermeable membrane that is highly resistant to the influx of protons; high-level trait edge."
        }
      ],
      "predicate_id": "RO:0002212"
    },
    "disposition": "major",
    "assessment": "RO:0002212 negatively regulates inherits the process-to-process endpoints of RO:0002211. The current subject is explicitly a material membrane and the object an explicit permeability QUALITY; this is a confirmed representational role mismatch, independent of whether the described environmental biology is plausible."
  }
]

### Native checklist: generic source support and excluded biology

evidence: unknown. Targets: METPO:1000455.

Existing generic acidophile potential, membrane and homeostasis context remains positive. It does not alone calibrate every organism in the numerical class. Detailed respiratory acid-defense at edge 5 and pathogen fitness/AMR/intervention biology remain UNASSESSED_SCOPE; no repaired mechanism or optimized condition is provided.

### Native checklist: whole record and optional fields

completeness: supported. Targets: METPO:1000455.

All twelve nodes, seven edges, five components, one label-only class, zero instances, one canonical and twelve events are covered. No artificial connector, protein instance or dataset requirement is imposed.

### Native checklist: canonical catalog applicability

scope: not_applicable. Targets: METPO:1000455.

No Picrophilus oshimae, current P. torridus synonym or verified type-alias match appears in the retained complete 20-organism/28-dataset catalog. Sulfolobus acidocaldarius is a different organism and was not substituted; no downstream defense query was used.

### Native checklist: exact maintained recurrence and historical scope

ownership: supported. Targets: METPO:1000455.

Decreases mapping row 61 can fill an empty ID, while the grounder skips nonempty IDs. The process-quality migration preserves reversed-potential STATE but does not own node 5. The exact canonical writer leaves identical examples unchanged and rejects divergent nonempty examples. Shared history leads are not automatic target owners or human approval.

{
  "assessed_at": "2026-10-21T18:52:34.711472+00:00",
  "target": "data/traits/environment/ph_optimum_low.yaml",
  "counts": {
    "nodes": 12,
    "edges": 7,
    "components": 5,
    "protein_classes": 1,
    "label_only_proteins": 1,
    "protein_instances": 0,
    "canonical_examples": 1,
    "history_events": 12,
    "ai_events": 11,
    "seed_events": 1,
    "captured_history_files": 5,
    "matching_files": 237,
    "review_target_arrays": 70,
    "exact_target_arrays": 0
  },
  "search_basis": "Ignored/hidden-inclusive exact slug, hyphenated slug, label, both identifier forms and all supplied exact/related synonyms; 237 paths with 70 actual parsed review target arrays and zero exact target arrays. All-node query identifies four history paths; together with the exact-target discovery there are five captured context histories, all verified.",
  "whole_histories_read": [
    "history/infrastructure/disposition-typing-burndown/2026-08-08T060908Z-claude-code-f802c8.yaml",
    "history/infrastructure/pathway-vs-process/2026-08-16T010630Z-claude-code-192557.yaml",
    "history/infrastructure/predicate-gate-audit/2026-08-16T074719Z-claude-code-84d88d.yaml",
    "history/infrastructure/process-quality-consistency/2026-08-21T073211Z-codex-174227.yaml",
    "history/other/canonical-examples-six/2026-08-21T065406Z-codex-a1ab82.yaml"
  ],
  "reading_scope": "All five captured histories fully read after the successful current capture: disposition and process-quality histories in the earlier current-target pass, and the remaining pathway, predicate-gate and canonical histories reread during finalization. Exact singular target and session actors are preserved. Prior #8 readings are not falsely dated as new acquisitions.",
  "current_history": "Twelve events comprise eleven explicit AI-assisted events and one seed. Five context histories have AI session actors; infrastructure maintenance or REVIEWED status is not itself attributable human scientific acceptance.",
  "owners": [
    {
      "path": "mappings/predicate_grounding.tsv",
      "locators": "row 61 decreases; rows 33 and 102 local predicates",
      "assessment": "The decreases mapping is wildcard-gated and can refill an empty predicate identifier without establishing imported process roles. Local predicate rows preserve broad context."
    },
    {
      "path": "scripts/ground_causal_predicates.py",
      "locators": "lines 152\u2013180, especially 159\u2013161",
      "assessment": "The writer skips existing predicate IDs; mapping gates operate on initial filling, so a current nonempty identifier is not revalidated by rerunning the writer."
    },
    {
      "path": "scripts/migrate_process_quality_consistency.py",
      "locators": "lines 60\u201374 and 148\u2013200",
      "assessment": "The exact reversed_membrane_potential decision preserves STATE and documents gradient versus establishment. The script does not settle the separate current transmembrane_ph_gradient node; unrelated maximal-growth-rate rewrite is not attributed to this target."
    },
    {
      "path": "scripts/backfill_canonical_examples_444.py",
      "locators": "lines 190\u2013192, 415\u2013419 and 995\u20131048",
      "assessment": "Exact Picrophilus source and target entry are maintained. The writer checks queue/ledger, leaves an identical existing example unchanged and rejects nonempty divergent examples; it is not an unconditional overwrite."
    }
  ],
  "research_scope": "Existing provider report and search hits are provenance/research leads only. No uninspected report passage or sibling record is adopted as scientific authority.",
  "human_traceability": {
    "severity": "minor",
    "field_path": "curation_history",
    "basis": "No attributable human scientific acceptance was found in the bounded current record, five captured context histories and 70 actual matching review target arrays.",
    "limits": "This does not assert that no human review ever occurred or search private/remote systems."
  }
}

### Native checklist: bounded local human traceability

provenance: concern. Targets: METPO:1000455.

Ignored-inclusive search found 237 paths, 70 actual review target arrays and zero exact target arrays. Twelve record events comprise eleven AI events plus seed; five captured histories were fully read and have AI actors. Positive maintenance and REVIEWED do not identify attributable human acceptance; remote/private decisions remain unknown.

### Native checklist: focused passes and qualified common reuse

schema: supported. Targets: METPO:1000455.

Native, strict and snippet checks passed directly; all 64 captured inputs match. Common/B4/B9 reuse preserves actual historical times, failures, retries, baselines and skips, without claiming a new B10 final QC execution.

## Findings

### exact-alias-scope: Exact physiological aliases do not cover the same numerical optimum class

major / open / confirmed; issue key: ph-optimum-low-exact-alias-scope.

Acid tolerance concerns exposure and is not identical to optimal growth. Assigned Baker and Frontiers definitions delimit acidophile/extreme-acidophile categories below pH 3, rather than the whole inclusive 0–6 bin. Faithful METPO import preserves provenance but does not establish scientific equivalence. The finding is limited to indices 0/1/2 and does not impose one publication convention universally.

### imported-regulation-role: Imported process regulation has material and quality endpoints

major / open / confirmed; issue key: ph-optimum-low-imported-regulation-role.

RO:0002212 inherits process domain and range from RO:0002211. The current subject is a material membrane and the object is permeability quality, so their represented referents do not satisfy the imported process-regulation meaning. Positive generic membrane evidence does not resolve this ontology-role conflict.

### gradient-process-facet: A maintained gradient is represented as a biological process

minor / open / confirmed; issue key: ph-optimum-low-gradient-process-facet.

Node 5 describes a steep transmembrane pH gradient maintained by acidophiles, while its declared type denotes a process. Native STATE distinguishes a gradient from the process that establishes it. The intended referent is readable; this is bounded representation precision rather than a false biological claim.

### human-acceptance-link: Local provenance lacks a linked human acceptance decision

minor / open / confirmed; issue key: ph-optimum-low-human-acceptance-link.

Current REVIEWED status and AI maintenance establish local provenance but do not identify attributable human scientific acceptance of the current record. The ignored-inclusive 237-path/70-array/zero-exact search, twelve record events and five AI histories preserve positive ownership without asserting absence of remote/private decisions.

## Recommended Actions And Acceptance Checks

### reconcile-alias-equivalence

During separately authorized curation, reconcile or qualify the three exact aliases against the numerical class and the cited conventions.

- Preserve active numerical identity and faithful upstream METPO provenance; do not call this a local transcription error.
- Distinguish exposure tolerance from growth optimum and narrower source definitions from full-bin equivalence. Do not add unsupported findings for other aliases.
- Use guarded history and applicable identity, native, strict and QC checks; preserve this immutable review and add a successor after changed inputs.

### reconcile-regulation-endpoints

Reconcile edge 6 with its current material and quality referents during authorized curation.

- Check actual inherited regulation roles separately from generic source support; no repaired defense pathway or efficacy claim is prescribed.
- Inspect mapping refill/nonempty-ID behavior and incident edges while preserving the supported membrane referent.
- Use guarded history and applicable native, strict, mapping and QC checks.

### clarify-gradient-facet

Clarify the gradient versus gradient-establishment representation while preserving the intended source meaning.

- Choose a documented native facet for the intended state or activity, then review incident relations. The current record is the established owner; no direct node 5 recurrence writer was established.
- Do not add a new mechanism, token accession, compulsory connector or experimental condition.
- Use guarded record/repository history and applicable native, strict and QC checks.

### link-human-acceptance

Link attributable human acceptance if available, or clarify status while preserving bounded uncertainty.

- Retain the 237-path/70-array/zero-exact basis and distinguish twelve record events from five fully read history records with AI actors.
- Do not infer acceptance from AI work, passing validators or ontology authorship.
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
| check-ph-optimum-low-validate | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-validate.log; Executed 2026-10-21T18:43:29.334754+00:00 through 2026-10-21T18:43:30.051580+00:00; metadata ph-optimum-low-validate.json | context_only | Passed directly at 18:43:29–18:43:30 UTC on the unchanged target. |
| check-ph-optimum-low-strict | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-strict.log; Executed 2026-10-21T18:43:29.334890+00:00 through 2026-10-21T18:43:30.428021+00:00; metadata ph-optimum-low-strict.json | context_only | Passed directly at 18:43:29–18:43:30 UTC; structural validity is distinct from imported relation semantics. |
| check-ph-optimum-low-snippets | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-snippets.log; Executed 2026-10-21T18:43:34.031657+00:00 through 2026-10-21T18:43:37.600939+00:00; metadata ph-optimum-low-snippets.json | context_only | Passed directly at 18:43:34–18:43:37 UTC: four fields, two VERIFIED and two NOT_IN_ABSTRACT. Manual primary checking finds two literal and two hyphen/en-dash normalized phrases, with none unverified. |
| check-corpus-protein-taxa | /private/tmp/traitmech-record-sweep-004.f7_g5r4w/corpus-protein-taxa.log; Executed 2026-10-21T08:55:04Z through 2026-10-21T08:55:10Z; metadata corpus-protein-taxa.json | context_only | Original B4 08:55:04–08:55:10 UTC pass with unchanged inputs; zero target instances, so no new instance audit is claimed. |
| check-batch009-qc | /private/tmp/traitmech-record-sweep-009.x21w9b3v/batch009-qc.log; Executed 2026-10-21T17:05:16Z through 2026-10-21T17:06:53Z; metadata batch009-qc.json | context_only | Original B9 17:05:16–17:06:53 UTC pass with B10 byte qualification; not a new final QC execution. |
| record | data/traits/environment/ph_optimum_low.yaml; Entire current target | supports | Twelve nodes, seven edges, five components, one label-only protein class, zero instances, one canonical and twelve record events are covered. |
| checklist | .claude/skills/curate-yaml-record/references/review-checklist.md; Captured maintained policy | supports | Whole-record identity, sources, graph, optional fields, ownership, provenance and readiness checklist. |
| policy | docs/GROUNDING_POLICY.md; Captured maintained policy | supports | Preserve actual referents and permissible facets; no token protein or connectivity requirement. |
| native-types | src/traitmech/schema/traitmech.yaml; Captured maintained policy | supports | Physical components, gradients, processes and qualities are distinct declared facets. |
| human-policy | docs/CURATION_PLAYBOOK.md; Captured maintained policy | supports | AI maintenance and REVIEWED do not identify attributable human scientific acceptance. |
| reuse | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/common-reuse-b9-qc-supplement-qualified.json; Qualified B10 comparison and original B9 gates | supports | All 1,130 traits, 1,278 history files and nineteen common inputs match; original timestamps, baselines, failures, retries and skips remain explicit. |
| capture | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-grounding-agent/final-capture-verification.json; Derived assessment/read receipt; primary acquisition is separately recorded | supports | All 64 captured inputs remain unchanged. |
| identity | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-grounding-agent/identity-assessment.json; Derived assessment/read receipt; primary acquisition is separately recorded | supports | Active identity, direct parent and explicit obsolete predecessor agree; faithful synonym import is separate from scientific equivalence. |
| node-edges | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-grounding-agent/node-edge-ledger.json; Derived assessment/read receipt; primary acquisition is separately recorded | supports | Every current node and edge; firm regulation-role issue at edge 6 and bounded gradient/process precision at node 5. |
| owners | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-grounding-agent/owner-provenance-assessment.json; Derived assessment/read receipt; primary acquisition is separately recorded | supports | Actual maintained writer/mapping recurrence, captured history and bounded ignored-inclusive human acceptance search. |
| expression | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-grounding-agent/expression-applicability.json; Derived assessment/read receipt; primary acquisition is separately recorded | supports | Canonical names and official aliases checked against the complete retained catalog; no substitute organism or downstream defense query. |
| authority-reuse | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-grounding-agent/authority-reuse-receipts.json; Derived assessment/read receipt; primary acquisition is separately recorded | supports | Original PATO and catalog acquisitions retained separately from current copies/readings. |
| local-authority | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-grounding-agent/local-authority-excerpts.json; Derived assessment/read receipt; primary acquisition is separately recorded | supports | Actual local selects-for/confers authorities and maintained native facets; free predicates have no invented imported restrictions. |
| selected-ro | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-grounding-agent/selected-ro-primary-reading.json; Derived assessment/read receipt; primary acquisition is separately recorded | supports | Actual RO process-regulation definition and inherited endpoint roles; database and query hashes remain distinct. |
| ground-manifest | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-grounding-agent/evidence-manifest.json; Derived assessment/read receipt; primary acquisition is separately recorded | supports | Frozen grounding inventory, with every listed artifact hash checked. |
| metpo-primary | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/repo/data/raw/metpo.owl; METPO:1000455, direct parent 1000331, obsolete 0000177 and nested decimal restriction | supports | Current identity and parent agree; obsolete 0000177 explicitly links to the active term. The inclusive 0–6 bin and supplied synonyms are faithfully imported. Scientific synonym equivalence is assessed separately. |
| ro-primary | /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/ro.db; RO:0002212 inherits process domain and process range from RO:0002211 | supports | The current material membrane and permeability quality are not process endpoints. A source-supported generic membrane claim does not itself make the imported process-regulation relation fit. |
| taxonomy-primary | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-grounding-agent/taxon46632.xml; Official NCBITaxon:46632 current name and synonyms | supports | Official 46632 identifies Picrophilus oshimae and includes P. torridus and verified type aliases. The published optimum is separate from taxonomy metadata. |
| pato-primary | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-grounding-agent/pato0001429.response; Official retained PATO:0001429 acidic response | supports | Acidic-quality facet is coherent; the response does not independently calibrate the numerical optimum bin. |
| meta-krulwich | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-root/krulwich-metadata.json; Actual Europe PMC title/abstract/status surface for DOI:10.1038/nrmicro2549 | supports | Assigned identity and returned abstract only; later selected body reading is separately bound. |
| meta-baker | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-root/baker-metadata.json; Actual Europe PMC title/abstract/status surface for DOI:10.1016/j.tim.2007.02.005 | supports | Assigned identity and returned abstract only; later selected body reading is separately bound. |
| meta-frontiers | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-root/frontiers-metadata.json; Actual Europe PMC title/abstract/status surface for DOI:10.3389/fmicb.2023.1149903 | supports | Assigned identity and returned abstract only; later selected body reading is separately bound. |
| meta-canonical | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-root/canonical-metadata.json; Actual Europe PMC title/abstract/status surface for DOI:10.1007/s007920050044 | supports | Canonical actual abstract directly reports optimum pH 0.7. |
| body-krulwich-bioc.xml | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-agent/krulwich-bioc.xml; Selected primary surface; actual original acquisition retained | supports | Selected generic PMF/environmental classification passages only; no whole-article or detailed acid-defense efficacy validation. |
| body-krulwich-publisher.html | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-agent/krulwich-publisher.html; Selected primary surface; actual original acquisition retained | supports | First two Key Points distinguish near-neutral optimum from acidic exposure and supply the existing acidic-growth quotation. Later detailed defense text is not functionally assessed. |
| body-frontiers.xml | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-agent/frontiers.xml; Selected primary surface; actual original acquisition retained | supports | Body paragraph 0 and two existing generic potential/membrane clauses in paragraph 6. Other detailed gene/defense passages are not adopted. |
| tolerance-optimum-distinction | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-agent/krulwich-publisher.html; First publisher Key Point: near-neutral optimal growth versus acidic exposure | refutes | The primary text distinguishes optimum from tolerance of acidic exposure. It does not equate the tolerant phenotype to the entire low-optimum numerical class. |
| acidophile-convention | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-root/baker-metadata.json; Actual abstract definition | refutes | Assigned review defines acidophiles by an optimum below pH 3, which does not cover the entire numerical 0–6 bin. |
| extreme-acidophile-convention | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-root/frontiers-metadata.json; Actual abstract definition | refutes | Assigned review defines extreme acidophiles by an optimum below pH 3; this stated convention challenges exact equivalence to the whole bin without imposing universal nomenclature. |
| sources | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-agent/source-assessment.json; Derived assessment/read receipt; primary acquisition is separately recorded | supports | Four works, eleven placements and one grouped synonym-equivalence concern; canonical and existing generic context remain positive. |
| source-ledger | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-agent/source-ledger.json; Derived assessment/read receipt; primary acquisition is separately recorded | supports | All assigned publication identities, exact available surfaces and acquisition receipts. |
| placements | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-agent/placement-ledger.json; Derived assessment/read receipt; primary acquisition is separately recorded | supports | All eleven external placements covered; no ontology-source placement counted as a publication. |
| snippets | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-agent/snippet-ledger.json; Derived assessment/read receipt; primary acquisition is separately recorded | supports | Two literal phrases and two meaning-equivalent hyphen/en-dash matches; no unknown or false-quotation finding. |
| node-sources | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-agent/node-source-ledger.json; Derived assessment/read receipt; primary acquisition is separately recorded | supports | All twelve current node source facets covered with generic versus unassessed biological scope. |
| edge-sources | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-agent/edge-source-ledger.json; Derived assessment/read receipt; primary acquisition is separately recorded | supports | All seven current edges; detailed respiratory acid-defense interpretation at edge 5 remains unassessed. |
| source-status | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-agent/publication-status-ledger.json; Derived assessment/read receipt; primary acquisition is separately recorded | supports | Actual returned metadata notice fields and Frontiers related-article elements only, not exhaustive global absence. |
| source-reading | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-agent/selected-primary-reading.json; Derived assessment/read receipt; primary acquisition is separately recorded | supports | Actual selected passages, with no whole-article or detailed pathogen mechanism reading claim. |
| source-access | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-agent/access-limitations.json; Derived assessment/read receipt; primary acquisition is separately recorded | supports | Baker and canonical actual abstracts suffice for the reported definition, quotation and optimum; no unavailable body is claimed. |
| source-manifest | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-agent/evidence-manifest.json; Derived assessment/read receipt; primary acquisition is separately recorded | supports | Twenty-six frozen source artifacts. |
| body-reuse | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-agent/reuse-and-copy-receipt.json; Derived assessment/read receipt; primary acquisition is separately recorded | supports | Original publisher 07:56:32–07:56:36, BioC 07:57:33 and current Frontiers 18:46:06–18:46:08 acquisitions remain distinct from copying/reading. |
| native-checks | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-agent/native-check-context.json; Derived assessment/read receipt; primary acquisition is separately recorded | supports | All focused checks passed directly; no copied high-pH failure or network retry applies. |
| canonical-source | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-agent/canonical-assessment.json; Derived assessment/read receipt; primary acquisition is separately recorded | supports | Picrophilus source abstract directly distinguishes optimum pH 0.7 from the separate growth limit. |
| synonym-scope | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-agent/synonym-scope-assessment.json; Derived assessment/read receipt; primary acquisition is separately recorded | supports | Three confirmed alias fields only; indices 3/4 remain unestablished in inspected scope rather than automatic added findings. |
| source-metpo-reading | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-agent/metpo-synonym-primary-reading.json; Derived assessment/read receipt; primary acquisition is separately recorded | supports | Actual nested 0–6 class restriction and exact upstream synonyms independently read. |
| root-reading-29 | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-root/initial-primary-root-reading.json; Derived assessment/read receipt; primary acquisition is separately recorded | supports | Only the actual scope and chronology recorded in this root reading receipt; no later or whole-body reading inferred. |
| root-reading-30 | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-root/primary-ro-reading.json; Derived assessment/read receipt; primary acquisition is separately recorded | supports | Only the actual scope and chronology recorded in this root reading receipt; no later or whole-body reading inferred. |
| root-reading-41 | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-root/frozen-ground-ledger-reading.json; Derived assessment/read receipt; primary acquisition is separately recorded | supports | Only the actual scope and chronology recorded in this root reading receipt; no later or whole-body reading inferred. |
| root-reading-42 | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-root/frozen-source-ledger-reading.json; Derived assessment/read receipt; primary acquisition is separately recorded | supports | Only the actual scope and chronology recorded in this root reading receipt; no later or whole-body reading inferred. |
| root-reading-43 | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-root/official-identity-root-reading.json; Derived assessment/read receipt; primary acquisition is separately recorded | supports | Only the actual scope and chronology recorded in this root reading receipt; no later or whole-body reading inferred. |
| root-reading-44 | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-root/owner-guard-root-reading.json; Derived assessment/read receipt; primary acquisition is separately recorded | supports | Only the actual scope and chronology recorded in this root reading receipt; no later or whole-body reading inferred. |
| root-reading-45 | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-root/primary-owner-root-reading.json; Derived assessment/read receipt; primary acquisition is separately recorded | supports | Only the actual scope and chronology recorded in this root reading receipt; no later or whole-body reading inferred. |
| root-reading-46 | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-root/publisher-keypoints-root-reading.json; Derived assessment/read receipt; primary acquisition is separately recorded | supports | Only the actual scope and chronology recorded in this root reading receipt; no later or whole-body reading inferred. |
| root-reading-47 | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-root/selected-body-root-reading.json; Derived assessment/read receipt; primary acquisition is separately recorded | supports | Only the actual scope and chronology recorded in this root reading receipt; no later or whole-body reading inferred. |
| root-reading-48 | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-root/whole-target-preinspect-reading.json; Derived assessment/read receipt; primary acquisition is separately recorded | supports | Only the actual scope and chronology recorded in this root reading receipt; no later or whole-body reading inferred. |
| challenge | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-semantic-challenge-agent/semantic-severity-challenge.json; Final independent severity review and verified bindings | supports | Independent disposition and qualifications; excluded detailed biological efficacy is not certified. |
| adjudication | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-root-adjudication.json; Final root adjudication and verified bindings | supports | Final disposition governs four findings; no scientific edit or status promotion is performed. |

## Limits And Additional Notes

- Detailed acid-defense, pathogen fitness, AMR and intervention biology remains UNASSESSED_SCOPE. Generic environmental source context and documentary attribution do not certify detailed mechanism efficacy or supply optimization.
- The three exact-alias concerns are inherited from pinned METPO. Assigned &lt;3 definitions are source conventions, not universal nomenclature. Indices 3/4 are not added findings merely because their exact equivalence is unestablished in inspected scope.
- Two growing-at-pH snippets use a hyphen where the primary publisher uses an en dash; meaning is preserved, and counts distinguish normalized from literal matches.
- Canonical optimum pH 0.7 is directly stated; the separate growth limit and current taxonomy are not confused with that optimum measurement.
- Generic acidophile descriptions and typical internal-pH context do not establish the same exact mechanism in every organism throughout the 0–6 bin.
- The native physical-component localization facet permits a membrane. The formal-role finding does not force a separate membrane node-type error. Free predicates have no invented imported endpoint rules.
- Original publisher HTML 07:56:32–07:56:36 and BioC 07:57:33 access, current metadata 18:42:41 and Frontiers body 18:46:06–18:46:08 remain distinct from current copying and selected reading. No whole-article reading is claimed.
- All focused checks passed directly. No high-pH inspect-cache failure, snippet DNS failure or supplemental history correction is copied into this target. Historical common failures and skips remain explicitly qualified.
- The bounded ignored-inclusive search cannot establish absence of remote/private human acceptance. No token protein, compulsory connection, substitute species or downstream defense-expression query is required.
- Final disposition: two major findings, two minor findings, fourteen assessments and four linked proposed actions.
- Coverage: 64 captured inputs, 26 frozen source artifacts and 23 frozen grounding artifacts, twelve nodes, seven edges, five components, one label-only protein class, zero instances, one canonical and twelve record events. Four works, eleven external placements and four supported snippets retain exact source scope.
- Single-use serializer remains unexecuted during preparation. Root owns final authorization, one execution, native review validation and save; no scientific record, state or Git mutation is performed here.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T185527Z-ph-optimum-low
kind: record
repository: CultureBotAI/TraitMech
title: Whole-record review of pH optimum low
started_at: '2026-10-21T18:43:15.841185Z'
finished_at: '2026-10-21T18:55:27Z'
reviewer:
  identity: codex
  kind: agent
  independence: independent
  independence_basis: Separate source and grounding audits, independent challenge
    and root selected-primary reading support the disposition. Generic environmental
    classification, literal attribution and formal roles are reviewed. Detailed acid-defense,
    pathogen fitness, AMR and intervention biology remains unassessed; no scientific
    record was edited.
  model: GPT-6 (Codex)
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'Needs curation: two majors address exact-alias scope and imported regulation
  endpoints; two minors address gradient/process precision and bounded human acceptance.
  Active identity, parent and canonical optimum remain positive. All four snippets
  have literal or meaning-equivalent typography support.'
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
  - path: data/traits/environment/ph_optimum_low.yaml
    sha256: eda82a5cfdd4b820895dbe955872248a5ba07079b6aab93450d332b25498eb41
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
  - path: history/infrastructure/disposition-typing-burndown/2026-08-08T060908Z-claude-code-f802c8.yaml
    sha256: 8ede4f80f46395efb74643e1f4158975a119ffaec78b5b291f0fc3a520a11c59
    role: context
  - path: history/infrastructure/pathway-vs-process/2026-08-16T010630Z-claude-code-192557.yaml
    sha256: a45fff0e3ef24effb20c3b624dc14a6cab08f2094bc0f8033cd709c0cd60f012
    role: context
  - path: history/infrastructure/predicate-gate-audit/2026-08-16T074719Z-claude-code-84d88d.yaml
    sha256: d1ba848e155dbd3a65905f07af5539d3d22b8873b638cc6adb48b1a0e23c0a3d
    role: context
  - path: history/infrastructure/process-quality-consistency/2026-08-21T073211Z-codex-174227.yaml
    sha256: e35d99e8285d488d98584d046aa001825527609cfd62575b3b839c4a31230642
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
  - path: research/traits/environment/ph_optimum_low-deep-research-falcon.md
    sha256: 1870665b1a0575646057b75ee273f57001b4f7e7900dd865b49f530c1d8e1e68
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
- target_id: METPO:1000455
  path: data/traits/environment/ph_optimum_low.yaml
  label: pH optimum low
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_optimum_low.yaml
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
  selection: Ninth record of batch 010 in path order. Whole-target reading and successful
    64-input capture precede substantive assessment. Metadata acquisition preceded
    capture, with interpretation afterwards. Frozen source and grounding manifests,
    independent challenge and final root adjudication are mandatory before serialization.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - METPO:1000455
checks:
- check_id: audit-graphs
  name: Full-corpus graph audit
  status: passed
  required: true
  target_ids:
  - METPO:1000455
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
  - METPO:1000455
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
  - METPO:1000455
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
  - METPO:1000455
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
  - METPO:1000455
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
  - METPO:1000455
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
  - METPO:1000455
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
- check_id: ph-optimum-low-validate
  name: Focused native validation
  status: passed
  required: true
  target_ids:
  - METPO:1000455
  command: just validate data/traits/environment/ph_optimum_low.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Passed directly at 18:43:29–18:43:30 UTC on the unchanged target.
  evidence_ids:
  - check-ph-optimum-low-validate
- check_id: ph-optimum-low-strict
  name: Focused strict validation
  status: passed
  required: true
  target_ids:
  - METPO:1000455
  command: just validate-strict data/traits/environment/ph_optimum_low.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Passed directly at 18:43:29–18:43:30 UTC; structural validity is distinct
    from imported relation semantics.
  evidence_ids:
  - check-ph-optimum-low-strict
- check_id: ph-optimum-low-snippets
  name: Focused snippet verification
  status: passed
  required: true
  target_ids:
  - METPO:1000455
  command: just verify-snippets --record data/traits/environment/ph_optimum_low.yaml
    --out /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-snippets.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 'Passed directly at 18:43:34–18:43:37 UTC: four fields, two VERIFIED and
    two NOT_IN_ABSTRACT. Manual primary checking finds two literal and two hyphen/en-dash
    normalized phrases, with none unverified.'
  evidence_ids:
  - check-ph-optimum-low-snippets
- check_id: corpus-protein-taxa
  name: Reused corpus protein/taxon audit
  status: passed
  required: true
  target_ids:
  - METPO:1000455
  command: just audit-graph-protein-taxa --out /private/tmp/traitmech-record-sweep-004.f7_g5r4w/corpus-protein-taxa.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: Original B4 08:55:04–08:55:10 UTC pass with unchanged inputs; zero target
    instances, so no new instance audit is claimed.
  evidence_ids:
  - check-corpus-protein-taxa
- check_id: batch009-qc
  name: Reused maintained batch-nine QC
  status: passed
  required: true
  target_ids:
  - METPO:1000455
  command: just qc
  exit_code: 0
  expected_exit_code: 0
  summary: Original B9 17:05:16–17:06:53 UTC pass with B10 byte qualification; not
    a new final QC execution.
  evidence_ids:
  - check-batch009-qc
- check_id: uniprot-applicability
  name: Protein-instance metadata applicability
  status: not_applicable
  required: false
  target_ids:
  - METPO:1000455
  summary: One contextual label-only protein class and zero instances; no token accession
    requirement.
  evidence_ids:
  - record
  - policy
  - node-edges
evidence:
- evidence_id: check-audit-graphs
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; metadata audit-graphs.json
  accessed_at: '2026-10-21T18:55:27Z'
  support: context_only
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  snapshot_sha256: ecce27e6a8f8b8b1fc54a9a0564a27626ee33774da508665859c6d1429337f4d
- evidence_id: check-audit-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; metadata audit-snippets.json
  accessed_at: '2026-10-21T18:55:27Z'
  support: context_only
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  snapshot_sha256: beafaa5c82645f5cf216142b6e0369d556202bcc72fdabbf35825fce955fd59f
- evidence_id: check-check-pathway-links
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; metadata check-pathway-links.json
  accessed_at: '2026-10-21T18:55:27Z'
  support: context_only
  summary: 19 links checked against the pinned PathwayMech snapshot. Target asserts
    no pathway context link.
  snapshot_sha256: e77729b8afd6ae02cd834e516c48dd5c72d10498802e7a1b0004eebb4831f6a0
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-003.4opxlhgf/validate-history.log
  locator: Executed 2026-10-21T07:03:25Z through 2026-10-21T07:03:30Z; metadata validate-history.json
  accessed_at: '2026-10-21T18:55:27Z'
  support: context_only
  summary: 1277 history records checked, zero invalid links at the 8eee source base;
    integrity does not establish science or human acceptance.
  snapshot_sha256: 02f94872992b2fbc3cc455c552d56a338dd449a315e02b1bf0226b68a8d2cfe3
- evidence_id: check-validate-products
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; metadata validate-products.json
  accessed_at: '2026-10-21T18:55:27Z'
  support: context_only
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  snapshot_sha256: 697efcbe603c9a5e27f9726e688d1b9d9f621fa548f585d9005b5157d81dadae
- evidence_id: check-validate-products-retry-local
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log
  locator: Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; metadata validate-products-retry-local.json
  accessed_at: '2026-10-21T18:55:27Z'
  support: context_only
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  snapshot_sha256: b636ab6978cf8b8d4cc2cc4033f1cdca399cca46dc615a26073cfe680d44ebb5
- evidence_id: check-validate-products-retry-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log
  locator: Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; metadata validate-products-retry-network.json
  accessed_at: '2026-10-21T18:55:27Z'
  support: context_only
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  snapshot_sha256: 67e91252adce1d441ad6b37d6904f0cbcea703575aec8011e65e94822fa810ea
- evidence_id: check-ph-optimum-low-validate
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-validate.log
  locator: Executed 2026-10-21T18:43:29.334754+00:00 through 2026-10-21T18:43:30.051580+00:00;
    metadata ph-optimum-low-validate.json
  accessed_at: '2026-10-21T18:55:27Z'
  support: context_only
  summary: Passed directly at 18:43:29–18:43:30 UTC on the unchanged target.
  snapshot_sha256: 82c105edab7ce57f48052bcf2101ba7cfc8d2afc065684db14c5e62c86e70233
- evidence_id: check-ph-optimum-low-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-strict.log
  locator: Executed 2026-10-21T18:43:29.334890+00:00 through 2026-10-21T18:43:30.428021+00:00;
    metadata ph-optimum-low-strict.json
  accessed_at: '2026-10-21T18:55:27Z'
  support: context_only
  summary: Passed directly at 18:43:29–18:43:30 UTC; structural validity is distinct
    from imported relation semantics.
  snapshot_sha256: 0c01de41fbfe2c67fec4c8c985633eb33114839e7720796806e10eea9ba09a7a
- evidence_id: check-ph-optimum-low-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-snippets.log
  locator: Executed 2026-10-21T18:43:34.031657+00:00 through 2026-10-21T18:43:37.600939+00:00;
    metadata ph-optimum-low-snippets.json
  accessed_at: '2026-10-21T18:55:27Z'
  support: context_only
  summary: 'Passed directly at 18:43:34–18:43:37 UTC: four fields, two VERIFIED and
    two NOT_IN_ABSTRACT. Manual primary checking finds two literal and two hyphen/en-dash
    normalized phrases, with none unverified.'
  snapshot_sha256: e207be23ee98425c8bd6dcb470d62765c465947f67b386b403d4213eee89c66d
- evidence_id: check-corpus-protein-taxa
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-004.f7_g5r4w/corpus-protein-taxa.log
  locator: Executed 2026-10-21T08:55:04Z through 2026-10-21T08:55:10Z; metadata corpus-protein-taxa.json
  accessed_at: '2026-10-21T18:55:27Z'
  support: context_only
  summary: Original B4 08:55:04–08:55:10 UTC pass with unchanged inputs; zero target
    instances, so no new instance audit is claimed.
  snapshot_sha256: f5f1a6be7789f2b3e487fcbc354361f8f1f0d0d0f90a9ba59864d26ed7ac49ef
- evidence_id: check-batch009-qc
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-009.x21w9b3v/batch009-qc.log
  locator: Executed 2026-10-21T17:05:16Z through 2026-10-21T17:06:53Z; metadata batch009-qc.json
  accessed_at: '2026-10-21T18:55:27Z'
  support: context_only
  summary: Original B9 17:05:16–17:06:53 UTC pass with B10 byte qualification; not
    a new final QC execution.
  snapshot_sha256: 1e73fe337dd10255851461d2d40b079ceeaf952d923b01ea8a16573963dcb05d
- evidence_id: record
  kind: record_content
  reference: data/traits/environment/ph_optimum_low.yaml
  locator: Entire current target
  accessed_at: '2026-10-21T18:52:34.712663Z'
  support: supports
  summary: Twelve nodes, seven edges, five components, one label-only protein class,
    zero instances, one canonical and twelve record events are covered.
  snapshot_sha256: eda82a5cfdd4b820895dbe955872248a5ba07079b6aab93450d332b25498eb41
- evidence_id: checklist
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Captured maintained policy
  accessed_at: '2026-10-21T18:52:34.712663Z'
  support: supports
  summary: Whole-record identity, sources, graph, optional fields, ownership, provenance
    and readiness checklist.
  snapshot_sha256: da8896328a0fd6cc92f1adf0d8be8980d0ddd41f3172c7936f2c7f119b293ac1
- evidence_id: policy
  kind: authority
  reference: docs/GROUNDING_POLICY.md
  locator: Captured maintained policy
  accessed_at: '2026-10-21T18:52:34.712663Z'
  support: supports
  summary: Preserve actual referents and permissible facets; no token protein or connectivity
    requirement.
  snapshot_sha256: 891678c983c2283a47c81c47950b35753981e9339d105f3bbdda92a1f5ab7f42
- evidence_id: native-types
  kind: authority
  reference: src/traitmech/schema/traitmech.yaml
  locator: Captured maintained policy
  accessed_at: '2026-10-21T18:52:34.712663Z'
  support: supports
  summary: Physical components, gradients, processes and qualities are distinct declared
    facets.
  snapshot_sha256: 46c47fc627b80ccbba1e8ab3fb6f2aee93bc2aef7aaf72fe9aadc3257f2c02dd
- evidence_id: human-policy
  kind: authority
  reference: docs/CURATION_PLAYBOOK.md
  locator: Captured maintained policy
  accessed_at: '2026-10-21T18:52:34.712663Z'
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
  summary: All 1,130 traits, 1,278 history files and nineteen common inputs match;
    original timestamps, baselines, failures, retries and skips remain explicit.
  snapshot_sha256: 515c688663a8a3f68f71fb2c3467217864338204f7f5197443642a81a8ec84c0
- evidence_id: capture
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-grounding-agent/final-capture-verification.json
  locator: Derived assessment/read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:52:34.713963Z'
  support: supports
  summary: All 64 captured inputs remain unchanged.
  snapshot_sha256: d4a0b6c65dd83951205f55bfcd6c0e5c7b92c6a0e9c52280f14685a59570f92a
- evidence_id: identity
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-grounding-agent/identity-assessment.json
  locator: Derived assessment/read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:52:34.709469Z'
  support: supports
  summary: Active identity, direct parent and explicit obsolete predecessor agree;
    faithful synonym import is separate from scientific equivalence.
  snapshot_sha256: 28b458f703b4593f366485448017f0bc78fa149b2ed9825ff7248dd68810c77f
- evidence_id: node-edges
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-grounding-agent/node-edge-ledger.json
  locator: Derived assessment/read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:52:34.708575Z'
  support: supports
  summary: Every current node and edge; firm regulation-role issue at edge 6 and bounded
    gradient/process precision at node 5.
  snapshot_sha256: 8e7ce39825b32b73834614419eb8bf679b03494b2c3fc4ed92b8cd509b2557cc
- evidence_id: owners
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-grounding-agent/owner-provenance-assessment.json
  locator: Derived assessment/read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:52:34.711472Z'
  support: supports
  summary: Actual maintained writer/mapping recurrence, captured history and bounded
    ignored-inclusive human acceptance search.
  snapshot_sha256: 279f8c432efd3c7861d776a5bf65dbdeed77ead5cd54cc2d0e3d91971a7185e7
- evidence_id: expression
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-grounding-agent/expression-applicability.json
  locator: Derived assessment/read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:52:34.712370Z'
  support: supports
  summary: Canonical names and official aliases checked against the complete retained
    catalog; no substitute organism or downstream defense query.
  snapshot_sha256: a70af06224158f33476efa526d62a9f6aa2cc49f60bb447f43528e76e8d307f9
- evidence_id: authority-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-grounding-agent/authority-reuse-receipts.json
  locator: Derived assessment/read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:48:46.552867Z'
  support: supports
  summary: Original PATO and catalog acquisitions retained separately from current
    copies/readings.
  snapshot_sha256: 88749d2c7735c08117017fb02754ce12d3041360a9b1a1d1513d0ea10cd5832a
- evidence_id: local-authority
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-grounding-agent/local-authority-excerpts.json
  locator: Derived assessment/read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:48:46.532972Z'
  support: supports
  summary: Actual local selects-for/confers authorities and maintained native facets;
    free predicates have no invented imported restrictions.
  snapshot_sha256: d7039292265923f5602414da313350c8b3ee760b7a1f189ab9e666110bec8c92
- evidence_id: selected-ro
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-grounding-agent/selected-ro-primary-reading.json
  locator: Derived assessment/read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:48:46.531216Z'
  support: supports
  summary: Actual RO process-regulation definition and inherited endpoint roles; database
    and query hashes remain distinct.
  snapshot_sha256: 041492bf51e77575b1cf3f484430e1759e7e8e63635218ecf3646b8e4499ca02
- evidence_id: ground-manifest
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-grounding-agent/evidence-manifest.json
  locator: Derived assessment/read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:52:34.724828Z'
  support: supports
  summary: Frozen grounding inventory, with every listed artifact hash checked.
  snapshot_sha256: 42482e6bfe2bd000ea85eb146a121cf71ac6f3196c4d8a71123e1dd0ac4ba901
- evidence_id: metpo-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/repo/data/raw/metpo.owl
  locator: METPO:1000455, direct parent 1000331, obsolete 0000177 and nested decimal
    restriction
  accessed_at: '2026-10-21T18:48:46.529554Z'
  support: supports
  summary: Current identity and parent agree; obsolete 0000177 explicitly links to
    the active term. The inclusive 0–6 bin and supplied synonyms are faithfully imported.
    Scientific synonym equivalence is assessed separately.
  snapshot_sha256: 8b6f8fe0510a698579e532658c8ace05da2550093365df9ca83feb0741778415
- evidence_id: ro-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/ro.db
  locator: RO:0002212 inherits process domain and process range from RO:0002211
  accessed_at: '2026-10-21T18:48:46.531216Z'
  support: supports
  summary: The current material membrane and permeability quality are not process
    endpoints. A source-supported generic membrane claim does not itself make the
    imported process-regulation relation fit.
  snapshot_sha256: 849e616c29fecd0d4a6c6dee0dc0f6f117ace7167dbfa1e0f043dc84868f83cb
- evidence_id: taxonomy-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-grounding-agent/taxon46632.xml
  locator: Official NCBITaxon:46632 current name and synonyms
  accessed_at: '2026-10-21T18:48:17.418961Z'
  support: supports
  summary: Official 46632 identifies Picrophilus oshimae and includes P. torridus
    and verified type aliases. The published optimum is separate from taxonomy metadata.
  snapshot_sha256: d3301fb634b8dfc61b814e080afb6ac0973223501d8b47d1b3f96820458ec5cd
- evidence_id: pato-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-grounding-agent/pato0001429.response
  locator: Official retained PATO:0001429 acidic response
  accessed_at: '2026-10-21T15:29:38.353968Z'
  support: supports
  summary: Acidic-quality facet is coherent; the response does not independently calibrate
    the numerical optimum bin.
  snapshot_sha256: bb1409f203e8578cb4e93f05390340322da1cdf7aeabb530e7241a8b1160212f
- evidence_id: meta-krulwich
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-root/krulwich-metadata.json
  locator: Actual Europe PMC title/abstract/status surface for DOI:10.1038/nrmicro2549
  accessed_at: '2026-10-21T18:42:41.702382Z'
  support: supports
  summary: Assigned identity and returned abstract only; later selected body reading
    is separately bound.
  snapshot_sha256: 484784a62fbb4c9d74a1feab4df2fdfdf37d4dd0ce3fa79f714c86a07d86d29c
- evidence_id: meta-baker
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-root/baker-metadata.json
  locator: Actual Europe PMC title/abstract/status surface for DOI:10.1016/j.tim.2007.02.005
  accessed_at: '2026-10-21T18:42:41.747550Z'
  support: supports
  summary: Assigned identity and returned abstract only; later selected body reading
    is separately bound.
  snapshot_sha256: a78777bc3bb6444b32e2e8a13ab72c56d80592b97e30c9b5520c67cc040c631b
- evidence_id: meta-frontiers
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-root/frontiers-metadata.json
  locator: Actual Europe PMC title/abstract/status surface for DOI:10.3389/fmicb.2023.1149903
  accessed_at: '2026-10-21T18:42:41.738186Z'
  support: supports
  summary: Assigned identity and returned abstract only; later selected body reading
    is separately bound.
  snapshot_sha256: 50b00c6b5f093fad2f0c4efbaa6d95461f39655747939cef8b3f629a32b64e54
- evidence_id: meta-canonical
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-root/canonical-metadata.json
  locator: Actual Europe PMC title/abstract/status surface for DOI:10.1007/s007920050044
  accessed_at: '2026-10-21T18:42:41.761597Z'
  support: supports
  summary: Canonical actual abstract directly reports optimum pH 0.7.
  snapshot_sha256: 431f7272ceea838c52dd0fe0de0b0bbade3f433fcaf01fabe4d308de93b5272f
- evidence_id: body-krulwich-bioc.xml
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-agent/krulwich-bioc.xml
  locator: Selected primary surface; actual original acquisition retained
  accessed_at: '2026-10-21T07:57:33Z'
  support: supports
  summary: Selected generic PMF/environmental classification passages only; no whole-article
    or detailed acid-defense efficacy validation.
  snapshot_sha256: 903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f
- evidence_id: body-krulwich-publisher.html
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-agent/krulwich-publisher.html
  locator: Selected primary surface; actual original acquisition retained
  accessed_at: '2026-10-21T07:56:36Z'
  support: supports
  summary: First two Key Points distinguish near-neutral optimum from acidic exposure
    and supply the existing acidic-growth quotation. Later detailed defense text is
    not functionally assessed.
  snapshot_sha256: 4cd2836049dc36e43c7d3d33561d1aa0b33f542eac252b37dd8275cea7fceb66
- evidence_id: body-frontiers.xml
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-agent/frontiers.xml
  locator: Selected primary surface; actual original acquisition retained
  accessed_at: '2026-10-21T18:46:08.093450Z'
  support: supports
  summary: Body paragraph 0 and two existing generic potential/membrane clauses in
    paragraph 6. Other detailed gene/defense passages are not adopted.
  snapshot_sha256: 6f9494d7379f7f7914200f9ba87905a42e803d6173cd22dd1fa837ccefc1f1e0
- evidence_id: tolerance-optimum-distinction
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-agent/krulwich-publisher.html
  locator: 'First publisher Key Point: near-neutral optimal growth versus acidic exposure'
  accessed_at: '2026-10-21T07:56:36Z'
  support: refutes
  summary: The primary text distinguishes optimum from tolerance of acidic exposure.
    It does not equate the tolerant phenotype to the entire low-optimum numerical
    class.
  snapshot_sha256: 4cd2836049dc36e43c7d3d33561d1aa0b33f542eac252b37dd8275cea7fceb66
- evidence_id: acidophile-convention
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-root/baker-metadata.json
  locator: Actual abstract definition
  accessed_at: '2026-10-21T18:42:41.747550Z'
  support: refutes
  summary: Assigned review defines acidophiles by an optimum below pH 3, which does
    not cover the entire numerical 0–6 bin.
  snapshot_sha256: a78777bc3bb6444b32e2e8a13ab72c56d80592b97e30c9b5520c67cc040c631b
- evidence_id: extreme-acidophile-convention
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-root/frontiers-metadata.json
  locator: Actual abstract definition
  accessed_at: '2026-10-21T18:42:41.738186Z'
  support: refutes
  summary: Assigned review defines extreme acidophiles by an optimum below pH 3; this
    stated convention challenges exact equivalence to the whole bin without imposing
    universal nomenclature.
  snapshot_sha256: 50b00c6b5f093fad2f0c4efbaa6d95461f39655747939cef8b3f629a32b64e54
- evidence_id: sources
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-agent/source-assessment.json
  locator: Derived assessment/read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:49:09.872527Z'
  support: supports
  summary: Four works, eleven placements and one grouped synonym-equivalence concern;
    canonical and existing generic context remain positive.
  snapshot_sha256: 4bb1eb573107dbb50e21cc7fe181a58c548846bab556c245fff3c7dc131804a0
- evidence_id: source-ledger
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-agent/source-ledger.json
  locator: Derived assessment/read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:49:09.867668Z'
  support: supports
  summary: All assigned publication identities, exact available surfaces and acquisition
    receipts.
  snapshot_sha256: d39923ced1863ac0aaed3f46ab3bf21c2a9afd0a6ff8f4c85cb804c7113d9a1b
- evidence_id: placements
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-agent/placement-ledger.json
  locator: Derived assessment/read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:49:09.867902Z'
  support: supports
  summary: All eleven external placements covered; no ontology-source placement counted
    as a publication.
  snapshot_sha256: ba7c4abbe0f79e4f0099da45e1315fadf58875698fda0c9ebdee73a4dfb17145
- evidence_id: snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-agent/snippet-ledger.json
  locator: Derived assessment/read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:49:09.868915Z'
  support: supports
  summary: Two literal phrases and two meaning-equivalent hyphen/en-dash matches;
    no unknown or false-quotation finding.
  snapshot_sha256: 96ed983f03681d0bb1f8a06ab785349a2ae1518bd2b8cb0dce8c3a945b82c333
- evidence_id: node-sources
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-agent/node-source-ledger.json
  locator: Derived assessment/read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:49:09.869059Z'
  support: supports
  summary: All twelve current node source facets covered with generic versus unassessed
    biological scope.
  snapshot_sha256: 30efce3377d2d417c8b26af93fb72266c59f0e26acfcc370980a168c506a6850
- evidence_id: edge-sources
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-agent/edge-source-ledger.json
  locator: Derived assessment/read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:49:09.869169Z'
  support: supports
  summary: All seven current edges; detailed respiratory acid-defense interpretation
    at edge 5 remains unassessed.
  snapshot_sha256: 6b5a5c26ce720e19a263c22f911aead6e8b3c938be9bcfb44db094fc43493e0d
- evidence_id: source-status
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-agent/publication-status-ledger.json
  locator: Derived assessment/read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:49:09.869381Z'
  support: supports
  summary: Actual returned metadata notice fields and Frontiers related-article elements
    only, not exhaustive global absence.
  snapshot_sha256: 1ad3349783a7764cee9ac7b853987916f057702db52005b126885cf9a0100bed
- evidence_id: source-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-agent/selected-primary-reading.json
  locator: Derived assessment/read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:49:09.869707Z'
  support: supports
  summary: Actual selected passages, with no whole-article or detailed pathogen mechanism
    reading claim.
  snapshot_sha256: e74685cad37ba56143d83e55edeae28164e845263a433896713ad6271be6f278
- evidence_id: source-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-agent/access-limitations.json
  locator: Derived assessment/read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:49:09.871263Z'
  support: supports
  summary: Baker and canonical actual abstracts suffice for the reported definition,
    quotation and optimum; no unavailable body is claimed.
  snapshot_sha256: 5705dad9dfb00822aacc9e7d80d3f9f539b695d4c304271d56f3c4517f5564ae
- evidence_id: source-manifest
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-agent/evidence-manifest.json
  locator: Derived assessment/read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:49:09.875914Z'
  support: supports
  summary: Twenty-six frozen source artifacts.
  snapshot_sha256: 4d3b75978b159553ceef51b868164ab1c52719aabc6cc46a2be6673f77c924af
- evidence_id: body-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-agent/reuse-and-copy-receipt.json
  locator: Derived assessment/read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:49:09.826584Z'
  support: supports
  summary: Original publisher 07:56:32–07:56:36, BioC 07:57:33 and current Frontiers
    18:46:06–18:46:08 acquisitions remain distinct from copying/reading.
  snapshot_sha256: b2a3880b64d9b52ac625ad3645db4f75d59a7737f0f53d317c129215ad558b4d
- evidence_id: native-checks
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-agent/native-check-context.json
  locator: Derived assessment/read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:49:09.872407Z'
  support: supports
  summary: All focused checks passed directly; no copied high-pH failure or network
    retry applies.
  snapshot_sha256: b6bee84a0fc116887a1273d081184684ea111be0b79f585f5240afcb56d0e4c8
- evidence_id: canonical-source
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-agent/canonical-assessment.json
  locator: Derived assessment/read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:49:09.869547Z'
  support: supports
  summary: Picrophilus source abstract directly distinguishes optimum pH 0.7 from
    the separate growth limit.
  snapshot_sha256: 8bf54656cce6335cfb6a92cea3b39c2d78595dfeb67f7dc2d4607a2f59df2ab1
- evidence_id: synonym-scope
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-agent/synonym-scope-assessment.json
  locator: Derived assessment/read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:49:09.870319Z'
  support: supports
  summary: Three confirmed alias fields only; indices 3/4 remain unestablished in
    inspected scope rather than automatic added findings.
  snapshot_sha256: c40ff7e4c83a0579f61efc85099d7dabde979df966c611a948d77c77468cf510
- evidence_id: source-metpo-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-agent/metpo-synonym-primary-reading.json
  locator: Derived assessment/read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:49:09.866580Z'
  support: supports
  summary: Actual nested 0–6 class restriction and exact upstream synonyms independently
    read.
  snapshot_sha256: b56c3809c5beaf9a17f8f26526a1d6b4903c6fd38f7015c31463a5d9a5e2ab91
- evidence_id: root-reading-29
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-root/initial-primary-root-reading.json
  locator: Derived assessment/read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:44:10.612085Z'
  support: supports
  summary: Only the actual scope and chronology recorded in this root reading receipt;
    no later or whole-body reading inferred.
  snapshot_sha256: 88efc32c8d35db3ecac6ad8a156c2690835e87eb207191a878f1bbffb338e345
- evidence_id: root-reading-30
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-root/primary-ro-reading.json
  locator: Derived assessment/read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:44:10.609187Z'
  support: supports
  summary: Only the actual scope and chronology recorded in this root reading receipt;
    no later or whole-body reading inferred.
  snapshot_sha256: c3b2dc8490456ab82ac19e83b32b0b9797ac78f4435bd467d08e225b2b609429
- evidence_id: root-reading-41
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-root/frozen-ground-ledger-reading.json
  locator: Derived assessment/read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:53:13.601817Z'
  support: supports
  summary: Only the actual scope and chronology recorded in this root reading receipt;
    no later or whole-body reading inferred.
  snapshot_sha256: 6fca7bf3564e4884b5e91fa2edb51a0cf930eb974746048191897f540446e95a
- evidence_id: root-reading-42
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-root/frozen-source-ledger-reading.json
  locator: Derived assessment/read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:50:44.382615Z'
  support: supports
  summary: Only the actual scope and chronology recorded in this root reading receipt;
    no later or whole-body reading inferred.
  snapshot_sha256: 67c8408e1d7a5bc11e7e81e098b89df9ff058953938653fab74d6a9b258af069
- evidence_id: root-reading-43
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-root/official-identity-root-reading.json
  locator: Derived assessment/read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:50:37.511278Z'
  support: supports
  summary: Only the actual scope and chronology recorded in this root reading receipt;
    no later or whole-body reading inferred.
  snapshot_sha256: 36b1c3a373a7abb44775b0ce3195857dd5d6385138ed32b949d0c967e05a3a0f
- evidence_id: root-reading-44
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-root/owner-guard-root-reading.json
  locator: Derived assessment/read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:53:25.963569Z'
  support: supports
  summary: Only the actual scope and chronology recorded in this root reading receipt;
    no later or whole-body reading inferred.
  snapshot_sha256: 018c64eea281c338d6a6abd7f154de27bff42a7d7df835dbe458e5463e0ee614
- evidence_id: root-reading-45
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-root/primary-owner-root-reading.json
  locator: Derived assessment/read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:45:00.995748Z'
  support: supports
  summary: Only the actual scope and chronology recorded in this root reading receipt;
    no later or whole-body reading inferred.
  snapshot_sha256: a34a96b78dd2c18274cb8cdea0072e1f8712d24f8de0b97bb1ff5e9ba019e254
- evidence_id: root-reading-46
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-root/publisher-keypoints-root-reading.json
  locator: Derived assessment/read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:48:41.547531Z'
  support: supports
  summary: Only the actual scope and chronology recorded in this root reading receipt;
    no later or whole-body reading inferred.
  snapshot_sha256: a32c697d5eee95ab09735eeeed849eb59d58320d7a9f66f65baee0eb2f889f4b
- evidence_id: root-reading-47
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-root/selected-body-root-reading.json
  locator: Derived assessment/read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:46:45.175847Z'
  support: supports
  summary: Only the actual scope and chronology recorded in this root reading receipt;
    no later or whole-body reading inferred.
  snapshot_sha256: 0d1de49f70eb746575124d197af1e7a0d2a22939904dcc4a620e68efdddeff2d
- evidence_id: root-reading-48
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-root/whole-target-preinspect-reading.json
  locator: Derived assessment/read receipt; primary acquisition is separately recorded
  accessed_at: '2026-10-21T18:42:26.190474Z'
  support: supports
  summary: Only the actual scope and chronology recorded in this root reading receipt;
    no later or whole-body reading inferred.
  snapshot_sha256: c13fdce03d89c41b0a81b402f9b4c3866aa70de046a3760b40b74b32a057c8c3
- evidence_id: challenge
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-semantic-challenge-agent/semantic-severity-challenge.json
  locator: Final independent severity review and verified bindings
  accessed_at: '2026-10-21T18:53:41.741503Z'
  support: supports
  summary: Independent disposition and qualifications; excluded detailed biological
    efficacy is not certified.
  snapshot_sha256: 0384416da423b8d7db743402868aaafa2da11de64eb20e9e5313be6dd11909b4
- evidence_id: adjudication
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-root-adjudication.json
  locator: Final root adjudication and verified bindings
  accessed_at: '2026-10-21T18:54:18.274035Z'
  support: supports
  summary: Final disposition governs four findings; no scientific edit or status promotion
    is performed.
  snapshot_sha256: 27e6b4bfbca3f4611d1e999f08d55cc4a3564d6e9aafb79789dfeeeb8a10c79b
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: active term, definition and hierarchy'
  outcome: supported
  target_ids:
  - METPO:1000455
  summary: Active METPO:1000455, parent 1000331 and explicit obsolete 0000177 replacement
    agree. The source numerical class is inclusive 0–6; at or below approximately
    6 is coherent with its boundary.
  evidence_ids:
  - identity
  - metpo-primary
  - record
- assessment_id: synonyms
  area: identity
  topic: 'Native checklist: exact aliases versus numerical scope'
  outcome: concern
  target_ids:
  - METPO:1000455
  summary: Acid Tolerant, Acidophile and Extreme Acidophile are faithfully inherited
    EXACT aliases, but the assigned primary distinction and definitions do not establish
    equivalence to the whole 0–6 optimum class. Only indices 0/1/2 are confirmed fields.
    Indices 3/4 remain unestablished source scope, not additional findings.
  evidence_ids:
  - synonym-scope
  - tolerance-optimum-distinction
  - acidophile-convention
  - extreme-acidophile-convention
  - metpo-primary
  - challenge
- assessment_id: scope
  area: scope
  topic: 'Native checklist: quantitative phenotype and generic graph context'
  outcome: supported
  target_ids:
  - METPO:1000455
  summary: ENVIRONMENT, CLASS and NONMECHANISTIC fit the quantitative bin. Five components
    and one label-only class without instances are allowed; generic context is not
    automatically a universal mechanism claim.
  evidence_ids:
  - record
  - policy
  - checklist
- assessment_id: canonical
  area: evidence
  topic: 'Native checklist: named canonical identity and optimum'
  outcome: supported
  target_ids:
  - METPO:1000455
  summary: The actual Picrophilus oshimae abstract directly states optimum pH 0.7,
    within the current bin, separately from its growth limit. Current official taxonomy
    and historical source names are retained as distinct documentary scopes.
  evidence_ids:
  - taxonomy-primary
  - identity
  - canonical-source
  - meta-canonical
- assessment_id: bibliography
  area: evidence
  topic: 'Native checklist: four works and eleven placements'
  outcome: supported
  target_ids:
  - METPO:1000455
  summary: All assigned publication identities resolve and all eleven external placements
    are covered on actual abstract, publisher or selected JATS surfaces. Metadata
    timing is distinct from later primary-body reading.
  evidence_ids:
  - source-ledger
  - placements
  - source-status
  details: "{\n  \"completed_at\": \"2026-10-21T18:49:09.872527+00:00\",\n  \"target\"\
    : \"data/traits/environment/ph_optimum_low.yaml\",\n  \"target_sha256\": \"eda82a5cfdd4b820895dbe955872248a5ba07079b6aab93450d332b25498eb41\"\
    ,\n  \"capture\": {\n    \"path\": \"/private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low.inspect.json\"\
    ,\n    \"sha256\": \"6d61baf2f440a83b5c33a393ec522f760377168dc08bed4891de4cc201244157\"\
    ,\n    \"bytes\": 13044\n  },\n  \"capture_inputs\": 64,\n  \"counts\": {\n  \
    \  \"works\": 4,\n    \"literal_reference_forms\": 4,\n    \"external_placements\"\
    : 11,\n    \"ontology_source_placements\": 0,\n    \"nodes\": 12,\n    \"edges\"\
    : 7,\n    \"snippets\": 4,\n    \"exact_snippets\": 2,\n    \"typography_normalized_snippets\"\
    : 2,\n    \"unverified_snippets\": 0,\n    \"canonical_examples\": 1\n  },\n \
    \ \"source_only_findings\": [\n    {\n      \"severity\": \"major\",\n      \"\
    area\": \"identity\",\n      \"field_paths\": [\n        \"synonyms[0]\",\n  \
    \      \"synonyms[1]\",\n        \"synonyms[2]\"\n      ],\n      \"summary\"\
    : \"The three supplied EXACT aliases do not establish equivalence to the entire\
    \ numerical optimum interval.\",\n      \"reasoning\": \"The publisher distinguishes\
    \ near-neutral optimal growth from survival or growth during acidic exposure,\
    \ so acid tolerance is not the same measurement as low optimum. The assigned Baker\
    \ abstract calls organisms with growth optimum below pH 3 acidophiles; Frontiers\
    \ uses that threshold for extreme acidophiles. These stated categories do not\
    \ cover the entire pinned inclusive 0\\u20136 bin. Exact equivalence therefore\
    \ alters class membership/retrieval.\",\n      \"qualifications\": [\n       \
    \ \"All aliases are faithfully inherited from pinned METPO; no local transcription\
    \ error is claimed.\",\n        \"The <3 thresholds are the assigned sources'\
    \ stated conventions, not a universal rule imposed across every publication.\"\
    ,\n        \"The current numeric identity and canonical optimum remain positive.\"\
    ,\n        \"Indices 3 and 4 were checked as supplied aliases but their exact\
    \ scope is not established in inspected primary surfaces; they are not automatically\
    \ added findings.\",\n        \"No biological pathway, defense target, intervention\
    \ or optimized condition is proposed.\"\n      ],\n      \"bounded_action\": \"\
    Reconcile or qualify the three exact aliases during separately authorized curation,\
    \ preserving upstream provenance and numerical identity.\"\n    }\n  ],\n  \"\
    source_only_major_candidates\": [\n    {\n      \"severity\": \"major\",\n   \
    \   \"area\": \"identity\",\n      \"field_paths\": [\n        \"synonyms[0]\"\
    ,\n        \"synonyms[1]\",\n        \"synonyms[2]\"\n      ],\n      \"summary\"\
    : \"The three supplied EXACT aliases do not establish equivalence to the entire\
    \ numerical optimum interval.\",\n      \"reasoning\": \"The publisher distinguishes\
    \ near-neutral optimal growth from survival or growth during acidic exposure,\
    \ so acid tolerance is not the same measurement as low optimum. The assigned Baker\
    \ abstract calls organisms with growth optimum below pH 3 acidophiles; Frontiers\
    \ uses that threshold for extreme acidophiles. These stated categories do not\
    \ cover the entire pinned inclusive 0\\u20136 bin. Exact equivalence therefore\
    \ alters class membership/retrieval.\",\n      \"qualifications\": [\n       \
    \ \"All aliases are faithfully inherited from pinned METPO; no local transcription\
    \ error is claimed.\",\n        \"The <3 thresholds are the assigned sources'\
    \ stated conventions, not a universal rule imposed across every publication.\"\
    ,\n        \"The current numeric identity and canonical optimum remain positive.\"\
    ,\n        \"Indices 3 and 4 were checked as supplied aliases but their exact\
    \ scope is not established in inspected primary surfaces; they are not automatically\
    \ added findings.\",\n        \"No biological pathway, defense target, intervention\
    \ or optimized condition is proposed.\"\n      ],\n      \"bounded_action\": \"\
    Reconcile or qualify the three exact aliases during separately authorized curation,\
    \ preserving upstream provenance and numerical identity.\"\n    }\n  ],\n  \"\
    source_only_minor_candidates\": [],\n  \"unassessed_biological_edge_indices\"\
    : [\n    5\n  ],\n  \"summary\": \"Four assigned identities and all eleven external\
    \ placements are covered. All four snippets are supported: two literal and two\
    \ typography-normalized. Canonical optimum pH 0.7 is direct. One grouped source/identity\
    \ major concerns exact synonym equivalence at indices 0/1/2; no quotation or canonical\
    \ finding. Generic existing source context remains positive, while detailed acid-defense/fitness/intervention\
    \ biology is unassessed.\",\n  \"qualifications\": [\n    \"Exact upstream import\
    \ is positive provenance, not proof of physiological equivalence.\",\n    \"Only\
    \ the three independently grounded alias mismatches are finding fields; indices\
    \ 3/4 remain scope limitations rather than inherited-major assumptions.\",\n \
    \   \"Meaning-equivalent hyphen/en-dash normalization is not a false-quotation\
    \ finding.\",\n    \"Source context and the numeric bin are distinct; no universal\
    \ mechanism, perturbation assay or new optimal condition is inferred.\",\n   \
    \ \"Original publication-body and metadata acquisition times are retained, distinct\
    \ from current selected reading.\"\n  ]\n}"
- assessment_id: snippets
  area: evidence
  topic: 'Native checklist: four assigned quotations'
  outcome: supported
  target_ids:
  - METPO:1000455
  summary: Two phrases are literal and the two repeated growing-at-pH phrases differ
    only by hyphen versus en dash. Meaning is preserved; no extra typography or false-quotation
    finding is added. Native two verified/two abstract nonmatches is distinct from
    manual primary verification.
  evidence_ids:
  - snippets
  - source-reading
  - native-checks
  details: "{\n  \"completed_at\": \"2026-10-21T18:49:09.868915+00:00\",\n  \"counts\"\
    : {\n    \"total\": 4,\n    \"exact\": 2,\n    \"typography_normalized\": 2,\n\
    \    \"unverified\": 0\n  },\n  \"snippets\": [\n    {\n      \"field\": \"evidence[0].snippet\"\
    ,\n      \"reference\": \"DOI:10.1038/nrmicro2549\",\n      \"snippet\": \"growing\
    \ at pH 1.0-3.0\",\n      \"status\": \"typography_normalized\",\n      \"source\"\
    : {\n        \"path\": \"/private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-agent/krulwich-publisher.html\"\
    ,\n        \"sha256\": \"4cd2836049dc36e43c7d3d33561d1aa0b33f542eac252b37dd8275cea7fceb66\"\
    ,\n        \"bytes\": 634100\n      },\n      \"locator\": \"Publisher second\
    \ Key Point\",\n      \"qualification\": \"Only ASCII hyphen versus en dash in\
    \ the numerical interval differs; scientific meaning is unchanged, no additional\
    \ finding.\"\n    },\n    {\n      \"field\": \"causal_graphs[0].edges[0].evidence[0].snippet\"\
    ,\n      \"reference\": \"DOI:10.1016/j.tim.2007.02.005\",\n      \"snippet\"\
    : \"highly impermeable cell membranes\",\n      \"status\": \"exact\",\n     \
    \ \"source\": {\n        \"path\": \"/private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-agent/baker-metadata.json\"\
    ,\n        \"sha256\": \"a78777bc3bb6444b32e2e8a13ab72c56d80592b97e30c9b5520c67cc040c631b\"\
    ,\n        \"bytes\": 4065\n      },\n      \"locator\": \"Actual indexed primary-review\
    \ abstract\",\n      \"qualification\": \"Exact words; no body reading claimed.\"\
    \n    },\n    {\n      \"field\": \"causal_graphs[0].edges[1].evidence[0].snippet\"\
    ,\n      \"reference\": \"DOI:10.1038/nrmicro2549\",\n      \"snippet\": \"growing\
    \ at pH 1.0-3.0\",\n      \"status\": \"typography_normalized\",\n      \"source\"\
    : {\n        \"path\": \"/private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-agent/krulwich-publisher.html\"\
    ,\n        \"sha256\": \"4cd2836049dc36e43c7d3d33561d1aa0b33f542eac252b37dd8275cea7fceb66\"\
    ,\n        \"bytes\": 634100\n      },\n      \"locator\": \"Publisher second\
    \ Key Point\",\n      \"qualification\": \"Only ASCII hyphen versus en dash in\
    \ the numerical interval differs; scientific meaning is unchanged, no additional\
    \ finding.\"\n    },\n    {\n      \"field\": \"causal_graphs[0].edges[2].evidence[0].snippet\"\
    ,\n      \"reference\": \"DOI:10.1038/nrmicro2549\",\n      \"snippet\": \"cytoplasmic\
    \ pH\",\n      \"status\": \"exact\",\n      \"source\": {\n        \"path\":\
    \ \"/private/tmp/traitmech-record-sweep-010.m7q2v9cx/ph-optimum-low-source-agent/krulwich-publisher.html\"\
    ,\n        \"sha256\": \"4cd2836049dc36e43c7d3d33561d1aa0b33f542eac252b37dd8275cea7fceb66\"\
    ,\n        \"bytes\": 634100\n      },\n      \"locator\": \"Publisher abstract\
    \ and Key Points\",\n      \"qualification\": \"Literal short phrase does not\
    \ itself establish a quantitative growth-optimum bin.\"\n    }\n  ]\n}"
- assessment_id: nodes
  area: grounding
  topic: 'Native checklist: all twelve node referents'
  outcome: concern
  target_ids:
  - METPO:1000455
  summary: The explicit transmembrane gradient at node 5 is typed as a process rather
    than the gradient state. The intended meaning remains readable, so this is bounded
    facet precision. Native physical-component localization is allowed; no automatic
    membrane typing defect or compulsory protein is inferred.
  evidence_ids:
  - node-edges
  - native-types
  - policy
  - pato-primary
  details: "[\n  {\n    \"index\": 0,\n    \"field_path\": \"causal_graphs[0].nodes[0]\"\
    ,\n    \"node\": {\n      \"node_id\": \"ph_optimum_low_trait\",\n      \"label\"\
    : \"pH optimum low\",\n      \"node_type\": \"TRAIT\",\n      \"grounding\": \"\
    METPO:1000455\",\n      \"description\": \"pH optimum at or below ~6.\"\n    },\n\
    \    \"assessment\": \"Active exact numerical low-optimum trait. Pinned METPO\
    \ explicitly constrains the optimum to inclusive 0\\u20136. Approximate local\
    \ wording is not an independently demonstrated boundary error.\"\n  },\n  {\n\
    \    \"index\": 1,\n    \"field_path\": \"causal_graphs[0].nodes[1]\",\n    \"\
    node\": {\n      \"node_id\": \"ph_optimum\",\n      \"label\": \"pH optimum\"\
    ,\n      \"node_type\": \"TRAIT\",\n      \"grounding\": \"METPO:1000331\",\n\
    \      \"description\": \"External pH supporting maximal growth.\"\n    },\n \
    \   \"assessment\": \"Active exact parent pH optimum; direct raw-METPO parent\
    \ relation is positive.\"\n  },\n  {\n    \"index\": 2,\n    \"field_path\": \"\
    causal_graphs[0].nodes[2]\",\n    \"node\": {\n      \"node_id\": \"acidic_external_ph\"\
    ,\n      \"label\": \"acidic external pH\",\n      \"node_type\": \"ENVIRONMENTAL_FACTOR\"\
    ,\n      \"description\": \"External pH \\u2264 ~6, typical of acidic mine drainage\
    \ and acidic soils.\",\n      \"grounding\": \"PATO:0001429\"\n    },\n    \"\
    assessment\": \"Environmental acidity condition with active PATO:0001429 acidic\
    \ grounding. PATO describes acidity rather than independently calibrating this\
    \ numerical bin.\"\n  },\n  {\n    \"index\": 3,\n    \"field_path\": \"causal_graphs[0].nodes[3]\"\
    ,\n    \"node\": {\n      \"node_id\": \"acidophile_proton_exclusion\",\n    \
    \  \"label\": \"acidophile proton-exclusion physiology\",\n      \"node_type\"\
    : \"BIOLOGICAL_PROCESS\",\n      \"description\": \"Low-permeability membranes\
    \ and reversed membrane potential that exclude protons in acidophiles.\"\n   \
    \ },\n    \"assessment\": \"Physiological umbrella can denote proton-exclusion\
    \ processes even though the description mentions membranes and a state. Retain\
    \ this shorthand as a qualified limitation, not an automatic material/process\
    \ finding.\"\n  },\n  {\n    \"index\": 4,\n    \"field_path\": \"causal_graphs[0].nodes[4]\"\
    ,\n    \"node\": {\n      \"node_id\": \"low_external_ph\",\n      \"label\":\
    \ \"low external pH\",\n      \"node_type\": \"ENVIRONMENTAL_FACTOR\",\n     \
    \ \"description\": \"Acidic medium external pH below ~3 imposing a steep proton\
    \ gradient.\"\n    },\n    \"assessment\": \"External acidic condition, not an\
    \ inferred new intervention or optimized growth instruction. Source scope remains\
    \ separately assessed.\"\n  },\n  {\n    \"index\": 5,\n    \"field_path\": \"\
    causal_graphs[0].nodes[5]\",\n    \"node\": {\n      \"node_id\": \"transmembrane_ph_gradient\"\
    ,\n      \"label\": \"large transmembrane pH gradient\",\n      \"node_type\"\
    : \"BIOLOGICAL_PROCESS\",\n      \"description\": \"Steep outside-to-inside proton\
    \ (delta pH) gradient maintained by acidophiles.\"\n    },\n    \"assessment\"\
    : \"Bounded facet precision issue: the explicit label and description denote the\
    \ maintained transmembrane gradient, while BIOLOGICAL_PROCESS denotes its establishment\
    \ or another process. The native STATE definition expressly distinguishes these\
    \ senses.\"\n  },\n  {\n    \"index\": 6,\n    \"field_path\": \"causal_graphs[0].nodes[6]\"\
    ,\n    \"node\": {\n      \"node_id\": \"reversed_membrane_potential\",\n    \
    \  \"label\": \"inside-positive (reversed) membrane potential\",\n      \"node_type\"\
    : \"STATE\",\n      \"description\": \"Reversed (inside-positive) membrane potential\
    \ creating an electrochemical barrier to proton influx.\"\n    },\n    \"assessment\"\
    : \"Inside-positive membrane potential is explicitly STATE; maintained migration\
    \ and current description agree. No repeated process/state defect here.\"\n  },\n\
    \  {\n    \"index\": 7,\n    \"field_path\": \"causal_graphs[0].nodes[7]\",\n\
    \    \"node\": {\n      \"node_id\": \"proton_influx\",\n      \"label\": \"proton\
    \ influx\",\n      \"node_type\": \"BIOLOGICAL_PROCESS\",\n      \"description\"\
    : \"Passive entry of protons into the cytoplasm down the pH gradient.\"\n    },\n\
    \    \"assessment\": \"Proton influx is explicitly an entry process. Formal referent\
    \ is coherent; this does not certify detailed efficacy in pathogenic organisms.\"\
    \n  },\n  {\n    \"index\": 8,\n    \"field_path\": \"causal_graphs[0].nodes[8]\"\
    ,\n    \"node\": {\n      \"node_id\": \"proton_pumping_respiratory_complexes\"\
    ,\n      \"label\": \"proton-pumping respiratory complexes\",\n      \"node_type\"\
    : \"GENE_OR_PROTEIN\",\n      \"grounding_status\": \"REVIEWED_LABEL_ONLY\",\n\
    \      \"grounding_notes\": \"Reviewed as a contextual protein or protein-complex\
    \ label within a quantitative measurement graph; no exact semantic family term\
    \ was established for this aggregate use.\",\n      \"description\": \"Respiratory\
    \ chain complexes (I, III, IV) that actively extrude cytoplasmic protons.\"\n\
    \    },\n    \"assessment\": \"Reviewed label-only protein-complex aggregate is\
    \ a material contextual class. No exact family or protein instance is required\
    \ by the quantitative NONMECHANISTIC scope; detailed acid-defense/fitness/intervention\
    \ efficacy remains UNASSESSED_SCOPE.\"\n  },\n  {\n    \"index\": 9,\n    \"field_path\"\
    : \"causal_graphs[0].nodes[9]\",\n    \"node\": {\n      \"node_id\": \"cytoplasmic_proton_load\"\
    ,\n      \"label\": \"cytoplasmic proton load\",\n      \"node_type\": \"STATE\"\
    ,\n      \"description\": \"Concentration of protons in the cytoplasm threatening\
    \ near-neutral intracellular pH.\"\n    },\n    \"assessment\": \"Cytoplasmic\
    \ load is a steady molecular value represented as STATE; no additional automatic\
    \ QUALITY finding is imposed.\"\n  },\n  {\n    \"index\": 10,\n    \"field_path\"\
    : \"causal_graphs[0].nodes[10]\",\n    \"node\": {\n      \"node_id\": \"proton_impermeable_membrane\"\
    ,\n      \"label\": \"rigid proton-impermeable membrane\",\n      \"node_type\"\
    : \"CELLULAR_LOCALIZATION\",\n      \"description\": \"Rigid membrane highly resistant\
    \ to proton influx, reducing passive proton permeability.\"\n    },\n    \"assessment\"\
    : \"Explicit membrane is material, consistent with cellular component/localization.\
    \ Its role as subject of RO:0002212 is separately incompatible with that processual\
    \ relation.\"\n  },\n  {\n    \"index\": 11,\n    \"field_path\": \"causal_graphs[0].nodes[11]\"\
    ,\n    \"node\": {\n      \"node_id\": \"passive_proton_permeability\",\n    \
    \  \"label\": \"passive proton permeability\",\n      \"node_type\": \"QUALITY\"\
    ,\n      \"description\": \"Rate of passive proton leakage across the cell membrane.\"\
    \n    },\n    \"assessment\": \"Permeability is explicitly a measurable QUALITY.\
    \ Its role as object of RO:0002212 is separately incompatible with that processual\
    \ relation.\"\n  }\n]"
- assessment_id: relations
  area: consistency
  topic: 'Native checklist: all seven edge meanings'
  outcome: concern
  target_ids:
  - METPO:1000455
  summary: Edge 6 uses imported process regulation between a material membrane and
    a permeability quality. This is a firm referent conflict, independent of positive
    generic source context. Local predicates retain their approved broad meanings;
    free relations are not assigned invented RO restrictions.
  evidence_ids:
  - node-edges
  - ro-primary
  - local-authority
  - owners
  - challenge
  details: "[\n  {\n    \"index\": 0,\n    \"field_path\": \"causal_graphs[0].edges[0]\"\
    ,\n    \"edge\": {\n      \"subject\": \"acidic_external_ph\",\n      \"predicate\"\
    : \"selects for\",\n      \"object\": \"acidophile_proton_exclusion\",\n     \
    \ \"description\": \"Acidic environments select for proton-exclusion physiology.\"\
    ,\n      \"evidence\": [\n        {\n          \"reference\": \"DOI:10.1016/j.tim.2007.02.005\"\
    ,\n          \"snippet\": \"highly impermeable cell membranes\",\n          \"\
    notes\": \"Supports envelope-based proton barriers as the selected acidophile\
    \ mechanism.\"\n        }\n      ],\n      \"predicate_id\": \"METPO:2007401\"\
    \n    },\n    \"disposition\": \"qualified\",\n    \"assessment\": \"The local\
    \ proposed selects-for relation has broad causal-node endpoints and evolutionary-selection\
    \ semantics. The process umbrella can refer to adapted physiology. Do not invent\
    \ a hard ENVIRONMENTAL_FACTOR exclusion or claim a newly demonstrated evolutionary\
    \ experiment.\"\n  },\n  {\n    \"index\": 1,\n    \"field_path\": \"causal_graphs[0].edges[1]\"\
    ,\n    \"edge\": {\n      \"subject\": \"acidophile_proton_exclusion\",\n    \
    \  \"predicate\": \"confers\",\n      \"object\": \"ph_optimum_low_trait\",\n\
    \      \"description\": \"Acidophile proton-exclusion physiology yields an acidic\
    \ pH-optimum setpoint.\",\n      \"evidence\": [\n        {\n          \"reference\"\
    : \"DOI:10.1038/nrmicro2549\",\n          \"snippet\": \"growing at pH 1.0-3.0\"\
    ,\n          \"notes\": \"Supports growth at strongly acidic pH as the acidophile\
    \ outcome.\"\n        }\n      ],\n      \"predicate_id\": \"METPO:2007700\"\n\
    \    },\n    \"disposition\": \"compatible\",\n    \"assessment\": \"Captured\
    \ v8 confers explicitly permits a process subject and trait object. Generic physiological\
    \ context does not independently establish exact-bin sufficiency, which remains\
    \ a source limitation rather than a formal endpoint defect.\"\n  },\n  {\n   \
    \ \"index\": 2,\n    \"field_path\": \"causal_graphs[0].edges[2]\",\n    \"edge\"\
    : {\n      \"subject\": \"ph_optimum_low_trait\",\n      \"predicate\": \"is a\"\
    ,\n      \"object\": \"ph_optimum\",\n      \"description\": \"pH optimum low\
    \ is a quantitative bin of the pH-optimum phenotype.\",\n      \"evidence\": [\n\
    \        {\n          \"reference\": \"DOI:10.1038/nrmicro2549\",\n          \"\
    snippet\": \"cytoplasmic pH\",\n          \"notes\": \"Supports an acidic optimum\
    \ as a value within the pH-optimum distribution.\"\n        }\n      ],\n    \
    \  \"predicate_id\": \"rdfs:subClassOf\"\n    },\n    \"disposition\": \"compatible\"\
    ,\n    \"assessment\": \"The trait-to-parent rdfs:subClassOf edge is directly\
    \ supported by pinned raw METPO; its short scientific snippet need not independently\
    \ prove the asserted ontology hierarchy.\"\n  },\n  {\n    \"index\": 3,\n   \
    \ \"field_path\": \"causal_graphs[0].edges[3]\",\n    \"edge\": {\n      \"subject\"\
    : \"low_external_ph\",\n      \"predicate\": \"drives\",\n      \"object\": \"\
    transmembrane_ph_gradient\",\n      \"description\": \"Acidic external pH forces\
    \ acidophiles to sustain a large transmembrane pH gradient.\",\n      \"evidence\"\
    : [\n        {\n          \"reference\": \"DOI:10.1038/nrmicro2549\",\n      \
    \    \"notes\": \"cytoplasmic pH ~6.0 while growing at external pH <3; broad physiological\
    \ input edge.\"\n        }\n      ]\n    },\n    \"disposition\": \"qualified\"\
    ,\n    \"assessment\": \"Free drives has no imported formal endpoint rule. The\
    \ object gradient/process precision is addressed once at node 5; no additional\
    \ role-major or required mechanism is inferred.\"\n  },\n  {\n    \"index\": 4,\n\
    \    \"field_path\": \"causal_graphs[0].edges[4]\",\n    \"edge\": {\n      \"\
    subject\": \"reversed_membrane_potential\",\n      \"predicate\": \"counteracts\"\
    ,\n      \"object\": \"proton_influx\",\n      \"description\": \"A reversed inside-positive\
    \ membrane potential electrostatically opposes proton entry.\",\n      \"evidence\"\
    : [\n        {\n          \"reference\": \"DOI:10.1038/nrmicro2549\",\n      \
    \    \"notes\": \"sustain a large delta pH with a reversed inside-positive membrane\
    \ potential; hallmark of extreme acidophiles.\"\n        },\n        {\n     \
    \     \"reference\": \"DOI:10.3389/fmicb.2023.1149903\",\n          \"notes\"\
    : \"inside positive membrane potential creates an electrochemical barrier to proton\
    \ influx.\"\n        }\n      ]\n    },\n    \"disposition\": \"compatible\",\n\
    \    \"assessment\": \"Free counteracts has no imported formal process-only rule.\
    \ STATE-to-process formal wording is not itself a defect; no detailed mechanism\
    \ reconstruction is performed.\"\n  },\n  {\n    \"index\": 5,\n    \"field_path\"\
    : \"causal_graphs[0].edges[5]\",\n    \"edge\": {\n      \"subject\": \"proton_pumping_respiratory_complexes\"\
    ,\n      \"predicate\": \"removes\",\n      \"object\": \"cytoplasmic_proton_load\"\
    ,\n      \"description\": \"Proton-pumping respiratory complexes actively extrude\
    \ protons to lower cytoplasmic proton load.\",\n      \"evidence\": [\n      \
    \  {\n          \"reference\": \"DOI:10.1038/nrmicro2549\",\n          \"notes\"\
    : \"increased expression of proton-pumping respiratory chain complexes; broad\
    \ mechanism, specific complexes vary by lineage.\"\n        }\n      ]\n    },\n\
    \    \"disposition\": \"documentary_only\",\n    \"assessment\": \"Free removes\
    \ has no imported hard endpoint rule. Material complex to steady proton-load description\
    \ is documented; detailed pathogen acid-defense/fitness/intervention efficacy\
    \ is UNASSESSED_SCOPE.\"\n  },\n  {\n    \"index\": 6,\n    \"field_path\": \"\
    causal_graphs[0].edges[6]\",\n    \"edge\": {\n      \"subject\": \"proton_impermeable_membrane\"\
    ,\n      \"predicate\": \"decreases\",\n      \"object\": \"passive_proton_permeability\"\
    ,\n      \"description\": \"A rigid proton-impermeable membrane reduces passive\
    \ proton leak and the energetic burden of pH homeostasis.\",\n      \"evidence\"\
    : [\n        {\n          \"reference\": \"DOI:10.3389/fmicb.2023.1149903\",\n\
    \          \"notes\": \"rigid and impermeable membrane that is highly resistant\
    \ to the influx of protons; high-level trait edge.\"\n        }\n      ],\n  \
    \    \"predicate_id\": \"RO:0002212\"\n    },\n    \"disposition\": \"major\"\
    ,\n    \"assessment\": \"RO:0002212 negatively regulates inherits the process-to-process\
    \ endpoints of RO:0002211. The current subject is explicitly a material membrane\
    \ and the object an explicit permeability QUALITY; this is a confirmed representational\
    \ role mismatch, independent of whether the described environmental biology is\
    \ plausible.\"\n  }\n]"
- assessment_id: source-context
  area: evidence
  topic: 'Native checklist: generic source support and excluded biology'
  outcome: unknown
  target_ids:
  - METPO:1000455
  summary: Existing generic acidophile potential, membrane and homeostasis context
    remains positive. It does not alone calibrate every organism in the numerical
    class. Detailed respiratory acid-defense at edge 5 and pathogen fitness/AMR/intervention
    biology remain UNASSESSED_SCOPE; no repaired mechanism or optimized condition
    is provided.
  evidence_ids:
  - sources
  - edge-sources
  - source-reading
  - source-access
- assessment_id: completeness
  area: completeness
  topic: 'Native checklist: whole record and optional fields'
  outcome: supported
  target_ids:
  - METPO:1000455
  summary: All twelve nodes, seven edges, five components, one label-only class, zero
    instances, one canonical and twelve events are covered. No artificial connector,
    protein instance or dataset requirement is imposed.
  evidence_ids:
  - record
  - node-edges
  - node-sources
  - policy
  - checklist
- assessment_id: expression
  area: scope
  topic: 'Native checklist: canonical catalog applicability'
  outcome: not_applicable
  target_ids:
  - METPO:1000455
  summary: No Picrophilus oshimae, current P. torridus synonym or verified type-alias
    match appears in the retained complete 20-organism/28-dataset catalog. Sulfolobus
    acidocaldarius is a different organism and was not substituted; no downstream
    defense query was used.
  evidence_ids:
  - expression
  - authority-reuse
- assessment_id: owners
  area: ownership
  topic: 'Native checklist: exact maintained recurrence and historical scope'
  outcome: supported
  target_ids:
  - METPO:1000455
  summary: Decreases mapping row 61 can fill an empty ID, while the grounder skips
    nonempty IDs. The process-quality migration preserves reversed-potential STATE
    but does not own node 5. The exact canonical writer leaves identical examples
    unchanged and rejects divergent nonempty examples. Shared history leads are not
    automatic target owners or human approval.
  evidence_ids:
  - owners
  - local-authority
  - challenge
  details: "{\n  \"assessed_at\": \"2026-10-21T18:52:34.711472+00:00\",\n  \"target\"\
    : \"data/traits/environment/ph_optimum_low.yaml\",\n  \"counts\": {\n    \"nodes\"\
    : 12,\n    \"edges\": 7,\n    \"components\": 5,\n    \"protein_classes\": 1,\n\
    \    \"label_only_proteins\": 1,\n    \"protein_instances\": 0,\n    \"canonical_examples\"\
    : 1,\n    \"history_events\": 12,\n    \"ai_events\": 11,\n    \"seed_events\"\
    : 1,\n    \"captured_history_files\": 5,\n    \"matching_files\": 237,\n    \"\
    review_target_arrays\": 70,\n    \"exact_target_arrays\": 0\n  },\n  \"search_basis\"\
    : \"Ignored/hidden-inclusive exact slug, hyphenated slug, label, both identifier\
    \ forms and all supplied exact/related synonyms; 237 paths with 70 actual parsed\
    \ review target arrays and zero exact target arrays. All-node query identifies\
    \ four history paths; together with the exact-target discovery there are five\
    \ captured context histories, all verified.\",\n  \"whole_histories_read\": [\n\
    \    \"history/infrastructure/disposition-typing-burndown/2026-08-08T060908Z-claude-code-f802c8.yaml\"\
    ,\n    \"history/infrastructure/pathway-vs-process/2026-08-16T010630Z-claude-code-192557.yaml\"\
    ,\n    \"history/infrastructure/predicate-gate-audit/2026-08-16T074719Z-claude-code-84d88d.yaml\"\
    ,\n    \"history/infrastructure/process-quality-consistency/2026-08-21T073211Z-codex-174227.yaml\"\
    ,\n    \"history/other/canonical-examples-six/2026-08-21T065406Z-codex-a1ab82.yaml\"\
    \n  ],\n  \"reading_scope\": \"All five captured histories fully read after the\
    \ successful current capture: disposition and process-quality histories in the\
    \ earlier current-target pass, and the remaining pathway, predicate-gate and canonical\
    \ histories reread during finalization. Exact singular target and session actors\
    \ are preserved. Prior #8 readings are not falsely dated as new acquisitions.\"\
    ,\n  \"current_history\": \"Twelve events comprise eleven explicit AI-assisted\
    \ events and one seed. Five context histories have AI session actors; infrastructure\
    \ maintenance or REVIEWED status is not itself attributable human scientific acceptance.\"\
    ,\n  \"owners\": [\n    {\n      \"path\": \"mappings/predicate_grounding.tsv\"\
    ,\n      \"locators\": \"row 61 decreases; rows 33 and 102 local predicates\"\
    ,\n      \"assessment\": \"The decreases mapping is wildcard-gated and can refill\
    \ an empty predicate identifier without establishing imported process roles. Local\
    \ predicate rows preserve broad context.\"\n    },\n    {\n      \"path\": \"\
    scripts/ground_causal_predicates.py\",\n      \"locators\": \"lines 152\\u2013180,\
    \ especially 159\\u2013161\",\n      \"assessment\": \"The writer skips existing\
    \ predicate IDs; mapping gates operate on initial filling, so a current nonempty\
    \ identifier is not revalidated by rerunning the writer.\"\n    },\n    {\n  \
    \    \"path\": \"scripts/migrate_process_quality_consistency.py\",\n      \"locators\"\
    : \"lines 60\\u201374 and 148\\u2013200\",\n      \"assessment\": \"The exact\
    \ reversed_membrane_potential decision preserves STATE and documents gradient\
    \ versus establishment. The script does not settle the separate current transmembrane_ph_gradient\
    \ node; unrelated maximal-growth-rate rewrite is not attributed to this target.\"\
    \n    },\n    {\n      \"path\": \"scripts/backfill_canonical_examples_444.py\"\
    ,\n      \"locators\": \"lines 190\\u2013192, 415\\u2013419 and 995\\u20131048\"\
    ,\n      \"assessment\": \"Exact Picrophilus source and target entry are maintained.\
    \ The writer checks queue/ledger, leaves an identical existing example unchanged\
    \ and rejects nonempty divergent examples; it is not an unconditional overwrite.\"\
    \n    }\n  ],\n  \"research_scope\": \"Existing provider report and search hits\
    \ are provenance/research leads only. No uninspected report passage or sibling\
    \ record is adopted as scientific authority.\",\n  \"human_traceability\": {\n\
    \    \"severity\": \"minor\",\n    \"field_path\": \"curation_history\",\n   \
    \ \"basis\": \"No attributable human scientific acceptance was found in the bounded\
    \ current record, five captured context histories and 70 actual matching review\
    \ target arrays.\",\n    \"limits\": \"This does not assert that no human review\
    \ ever occurred or search private/remote systems.\"\n  }\n}"
- assessment_id: human-acceptance
  area: provenance
  topic: 'Native checklist: bounded local human traceability'
  outcome: concern
  target_ids:
  - METPO:1000455
  summary: Ignored-inclusive search found 237 paths, 70 actual review target arrays
    and zero exact target arrays. Twelve record events comprise eleven AI events plus
    seed; five captured histories were fully read and have AI actors. Positive maintenance
    and REVIEWED do not identify attributable human acceptance; remote/private decisions
    remain unknown.
  evidence_ids:
  - owners
  - human-policy
  - challenge
  - adjudication
- assessment_id: checks
  area: schema
  topic: 'Native checklist: focused passes and qualified common reuse'
  outcome: supported
  target_ids:
  - METPO:1000455
  summary: Native, strict and snippet checks passed directly; all 64 captured inputs
    match. Common/B4/B9 reuse preserves actual historical times, failures, retries,
    baselines and skips, without claiming a new B10 final QC execution.
  evidence_ids:
  - capture
  - reuse
  - native-checks
  - check-ph-optimum-low-validate
  - check-ph-optimum-low-strict
  - check-ph-optimum-low-snippets
findings:
- finding_id: exact-alias-scope
  issue_key: ph-optimum-low-exact-alias-scope
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Exact physiological aliases do not cover the same numerical optimum class
  description: Acid tolerance concerns exposure and is not identical to optimal growth.
    Assigned Baker and Frontiers definitions delimit acidophile/extreme-acidophile
    categories below pH 3, rather than the whole inclusive 0–6 bin. Faithful METPO
    import preserves provenance but does not establish scientific equivalence. The
    finding is limited to indices 0/1/2 and does not impose one publication convention
    universally.
  target_ids:
  - METPO:1000455
  field_paths:
  - synonyms[0]
  - synonyms[1]
  - synonyms[2]
  evidence_ids:
  - synonym-scope
  - tolerance-optimum-distinction
  - acidophile-convention
  - extreme-acidophile-convention
  - metpo-primary
  - challenge
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_optimum_low.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: imported-regulation-role
  issue_key: ph-optimum-low-imported-regulation-role
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Imported process regulation has material and quality endpoints
  description: RO:0002212 inherits process domain and range from RO:0002211. The current
    subject is a material membrane and the object is permeability quality, so their
    represented referents do not satisfy the imported process-regulation meaning.
    Positive generic membrane evidence does not resolve this ontology-role conflict.
  target_ids:
  - METPO:1000455
  field_paths:
  - causal_graphs[0].edges[6]
  evidence_ids:
  - node-edges
  - ro-primary
  - native-types
  - owners
  - challenge
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_optimum_low.yaml
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
- finding_id: gradient-process-facet
  issue_key: ph-optimum-low-gradient-process-facet
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: A maintained gradient is represented as a biological process
  description: Node 5 describes a steep transmembrane pH gradient maintained by acidophiles,
    while its declared type denotes a process. Native STATE distinguishes a gradient
    from the process that establishes it. The intended referent is readable; this
    is bounded representation precision rather than a false biological claim.
  target_ids:
  - METPO:1000455
  field_paths:
  - causal_graphs[0].nodes[5]
  evidence_ids:
  - node-edges
  - native-types
  - local-authority
  - challenge
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_optimum_low.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: human-acceptance-link
  issue_key: ph-optimum-low-human-acceptance-link
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Local provenance lacks a linked human acceptance decision
  description: Current REVIEWED status and AI maintenance establish local provenance
    but do not identify attributable human scientific acceptance of the current record.
    The ignored-inclusive 237-path/70-array/zero-exact search, twelve record events
    and five AI histories preserve positive ownership without asserting absence of
    remote/private decisions.
  target_ids:
  - METPO:1000455
  field_paths:
  - mapping_status
  - curation_history
  evidence_ids:
  - owners
  - human-policy
  - challenge
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_optimum_low.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
actions:
- action_id: reconcile-alias-equivalence
  description: During separately authorized curation, reconcile or qualify the three
    exact aliases against the numerical class and the cited conventions.
  finding_ids:
  - exact-alias-scope
  target_ids:
  - METPO:1000455
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_optimum_low.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Preserve active numerical identity and faithful upstream METPO provenance; do
    not call this a local transcription error.
  - Distinguish exposure tolerance from growth optimum and narrower source definitions
    from full-bin equivalence. Do not add unsupported findings for other aliases.
  - Use guarded history and applicable identity, native, strict and QC checks; preserve
    this immutable review and add a successor after changed inputs.
- action_id: reconcile-regulation-endpoints
  description: Reconcile edge 6 with its current material and quality referents during
    authorized curation.
  finding_ids:
  - imported-regulation-role
  target_ids:
  - METPO:1000455
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_optimum_low.yaml
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
  - Check actual inherited regulation roles separately from generic source support;
    no repaired defense pathway or efficacy claim is prescribed.
  - Inspect mapping refill/nonempty-ID behavior and incident edges while preserving
    the supported membrane referent.
  - Use guarded history and applicable native, strict, mapping and QC checks.
- action_id: clarify-gradient-facet
  description: Clarify the gradient versus gradient-establishment representation while
    preserving the intended source meaning.
  finding_ids:
  - gradient-process-facet
  target_ids:
  - METPO:1000455
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_optimum_low.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Choose a documented native facet for the intended state or activity, then review
    incident relations. The current record is the established owner; no direct node
    5 recurrence writer was established.
  - Do not add a new mechanism, token accession, compulsory connector or experimental
    condition.
  - Use guarded record/repository history and applicable native, strict and QC checks.
- action_id: link-human-acceptance
  description: Link attributable human acceptance if available, or clarify status
    while preserving bounded uncertainty.
  finding_ids:
  - human-acceptance-link
  target_ids:
  - METPO:1000455
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_optimum_low.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Retain the 237-path/70-array/zero-exact basis and distinguish twelve record events
    from five fully read history records with AI actors.
  - Do not infer acceptance from AI work, passing validators or ontology authorship.
  - No contact with another person or automatic status promotion is authorized by
    this proposed action.
limitations:
- Detailed acid-defense, pathogen fitness, AMR and intervention biology remains UNASSESSED_SCOPE.
  Generic environmental source context and documentary attribution do not certify
  detailed mechanism efficacy or supply optimization.
- The three exact-alias concerns are inherited from pinned METPO. Assigned <3 definitions
  are source conventions, not universal nomenclature. Indices 3/4 are not added findings
  merely because their exact equivalence is unestablished in inspected scope.
- Two growing-at-pH snippets use a hyphen where the primary publisher uses an en dash;
  meaning is preserved, and counts distinguish normalized from literal matches.
- Canonical optimum pH 0.7 is directly stated; the separate growth limit and current
  taxonomy are not confused with that optimum measurement.
- Generic acidophile descriptions and typical internal-pH context do not establish
  the same exact mechanism in every organism throughout the 0–6 bin.
- The native physical-component localization facet permits a membrane. The formal-role
  finding does not force a separate membrane node-type error. Free predicates have
  no invented imported endpoint rules.
- Original publisher HTML 07:56:32–07:56:36 and BioC 07:57:33 access, current metadata
  18:42:41 and Frontiers body 18:46:06–18:46:08 remain distinct from current copying
  and selected reading. No whole-article reading is claimed.
- All focused checks passed directly. No high-pH inspect-cache failure, snippet DNS
  failure or supplemental history correction is copied into this target. Historical
  common failures and skips remain explicitly qualified.
- The bounded ignored-inclusive search cannot establish absence of remote/private
  human acceptance. No token protein, compulsory connection, substitute species or
  downstream defense-expression query is required.
notes:
- 'Final disposition: two major findings, two minor findings, fourteen assessments
  and four linked proposed actions.'
- 'Coverage: 64 captured inputs, 26 frozen source artifacts and 23 frozen grounding
  artifacts, twelve nodes, seven edges, five components, one label-only protein class,
  zero instances, one canonical and twelve record events. Four works, eleven external
  placements and four supported snippets retain exact source scope.'
- Single-use serializer remains unexecuted during preparation. Root owns final authorization,
  one execution, native review validation and save; no scientific record, state or
  Git mutation is performed here.
tags:
- record-review
- ph-optimum-low
- environment
- needs-curation
native_verdict: needs_curation
```
