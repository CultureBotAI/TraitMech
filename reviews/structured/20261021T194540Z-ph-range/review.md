# Whole-record review of pH range

- Review: 20261021T194540Z-ph-range
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-21T19:34:40.820444Z
- Finished UTC: 2026-10-21T19:45:40Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

One linked interval/gradient representation and imported-role major, one bounded Baker attribution minor and one human-acceptance minor. Canonical range, all six quotations and generic source context remain supported.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: Third record of the actual batch 011 queue. Entire target and successful 77-input capture precede substantive judgments. Current metadata was acquired before capture and interpreted afterward. Frozen source/grounding audits, independent challenge and final root adjudication govern this review.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8eee04a8c65609fbaff6df7c54597dcaf1b9d282.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| METPO:1000332 | data/traits/environment/ph_range.yaml | maintained | pH range |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full-corpus graph audit | passed | True | METPO:1000332 | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| Full-corpus snippet audit | passed | True | METPO:1000332 | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| Full-corpus pathway links | passed | True | METPO:1000332 | 19 links checked against the pinned PathwayMech snapshot. |
| Full-corpus history integrity | passed | True | METPO:1000332 | 1277 history records checked, zero invalid links at the 8eee source base; integrity does not establish science or human acceptance. |
| Initial full-product validation | failed | False | METPO:1000332 | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation with isolated local cache | failed | False | METPO:1000332 | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation after isolated-cache download | passed | True | METPO:1000332 | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| Focused native validation | passed | True | METPO:1000332 | Direct successful current-target schema validation; formal roles are assessed separately. |
| Focused strict validation | passed | True | METPO:1000332 | Direct successful current-target strict validation; no biological efficacy certification. |
| Focused snippet verification | passed | True | METPO:1000332 | Six fields over two references: five VERIFIED and one NOT_IN_ABSTRACT. Independent retained primary text verifies all six literal occurrences without changing the native result. |
| Reused maintained batch-ten QC | passed | True | METPO:1000332 | Actual B10 final QC at its original time, qualified against B11 bytes; not a fresh B11 execution. |
| Protein-instance metadata applicability | not_applicable | False | METPO:1000332 | Zero protein-class nodes and zero instances; explicit antiport activity is not a token protein class. |

## Scientific And Domain Assessments

### Native checklist: active identity, parents and replacements

identity: supported. Targets: METPO:1000332.

Active METPO:1000332 and both direct parents agree. Two deprecated terms explicitly point to it. Luke Wang is positive concept authorship, separately from current graph acceptance. No supplied synonym equivalence requires repair.

### Native checklist: minimum-to-maximum external growth pH

evidence: supported. Targets: METPO:1000332.

The definition is a synthesis consistent with the two measurement parents and generic external growth-pH source context. The target raw METPO class has no textual definition; it is not presented as an exact ontology quotation.

### Native checklist: quantitative environmental interval

scope: supported. Targets: METPO:1000332.

ENVIRONMENT, CLASS and NONMECHANISTIC fit the measured interval. Contextual branches are not automatically universal or sufficient biological mechanisms. No invented optimum/range equivalence is asserted.

### Native checklist: species-bound full interval

evidence: supported. Targets: METPO:1000332.

Actual assigned abstract supports NTOU-MSR1T growth range pH 7–10, distinct from optimum 7–8. Official species and type aliases match. Parent placement preserves the full interval, and no full methods or complete species-wide phenotype generalization is claimed.

### Native checklist: all works and placement scope

evidence: concern. Targets: METPO:1000332.

All four assigned identities and fourteen external placements resolve. The Baker membrane phrase supports acidophile low-pH context, while evidence[1].notes broadens that attribution to alkaline extremes. This is bounded source-scope precision; inaccessible full text is not evidence of false biology or total source absence.

{
  "completed_at": "2026-10-21T19:38:03.316462+00:00",
  "external_placements": [
    {
      "field_path": "definition_source",
      "reference": "DOI:10.1038/nrmicro2549",
      "claim": "A pH phenotype with numerical limits that bounds the minimum and maximum external pH supporting growth of an organism.",
      "assessment": "Generic growth-supporting external-pH concept consistent with actual Krulwich abstract and generic BioC opening; no imposed common endpoint or optimum/range equivalence."
    },
    {
      "field_path": "evidence[0]",
      "reference": "DOI:10.1038/nrmicro2549",
      "snippet": "pH homeostasis",
      "notes": "pH-homeostasis review supports the bounded external-pH span over which cytoplasmic pH homeostasis sustains growth as the basis of the pH-range phenotype.",
      "assessment": "Positive generic homeostasis context; literal short phrase does not independently establish complete organism-specific endpoints."
    },
    {
      "field_path": "evidence[1]",
      "reference": "DOI:10.1016/j.tim.2007.02.005",
      "snippet": "highly impermeable cell membranes",
      "notes": "pH-homeostasis review supports envelope-based proton barriers as the mechanism extending growth into acidic and alkaline extremes.",
      "assessment": "Exact membrane phrase is positive for acidophiles. The notes broaden this assigned acidophile attribution to alkaline extremes; bounded source-scope precision candidate, without claiming the inaccessible full paper contains no alkaline discussion."
    },
    {
      "field_path": "canonical_examples[0]",
      "reference": "DOI:10.1007/s10482-024-01948-y",
      "claim": "Oceanimonas pelagia NTOU-MSR1T grew at pH 7-10. The complete interval crosses the mid2/mid3 split, so #591 places this distinct claim on the pH-range parent.",
      "assessment": "Assigned actual abstract explicitly reports NTOU-MSR1T growth at pH 7.0\u201310.0 and optimum 7.0\u20138.0. Parent placement preserves the full interval rather than changing it to the optimum or a single child bin."
    },
    {
      "field_path": "causal_graphs[0].edges[0].evidence[0]",
      "reference": "DOI:10.1038/nrmicro2549",
      "snippet": "external pH",
      "notes": "Supports external pH as the axis bounding the growth window.",
      "assessment": "Generic external-pH axis is directly supported by the assigned abstract and BioC opening; exact measured boundaries remain organism-specific."
    },
    {
      "field_path": "causal_graphs[0].edges[1].evidence[0]",
      "reference": "DOI:10.1016/j.tim.2007.02.005",
      "snippet": "highly impermeable cell membranes",
      "notes": "Supports envelope proton barriers as the lower-bound mechanism for low-pH growth.",
      "assessment": "The exact assigned acidophile abstract supports low-pH membrane-barrier context. This is generic lower-bound context, not a universal single necessary or sufficient mechanism."
    },
    {
      "field_path": "causal_graphs[0].edges[2].evidence[0]",
      "reference": "DOI:10.1038/nrmicro2549",
      "snippet": "alkaliphiles",
      "notes": "Supports alkaline-tolerance physiology as the upper-bound mechanism for high-pH growth.",
      "assessment": "Assigned Krulwich text explicitly discusses alkaliphiles and growth at elevated external pH. Generic upper-bound context is supported; no universal single strategy or exact numerical cutoff is inferred."
    },
    {
      "field_path": "causal_graphs[0].edges[3].evidence[0]",
      "reference": "DOI:10.1038/nrmicro2549",
      "snippet": "pH homeostasis",
      "notes": "Supports the trait endpoint.",
      "assessment": "Generic pH-homeostasis context is supported; the measurement/trait relationship and local predicate semantics are assessed independently by grounding, not proved by the two-word snippet."
    },
    {
      "field_path": "causal_graphs[0].edges[4].evidence[0]",
      "reference": "DOI:10.1038/nrmicro2549",
      "notes": "PMF architecture (\u0394\u03c8 \u2212 59 \u0394pH) determines the range of pHout over which bacteria can tolerate or grow.",
      "assessment": "BioC offsets 2440 and 3214 support the two-component PMF and approximation under standard conditions. Offset 3940 supplies condition-specific illustrative patterns. The current note is contextual; the approximation alone does not calibrate a complete growth interval or prove biological sufficiency."
    },
    {
      "field_path": "causal_graphs[0].edges[5].evidence[0]",
      "reference": "DOI:10.1038/nrmicro2549",
      "notes": "Under strong pH stress the orientation of a PMF component can reverse to maintain homeostasis.",
      "assessment": "BioC offset 3940 explicitly illustrates reversed PMF components in distinct growth-pH contexts. Preserve source-specific illustrations and generic context; this does not certify a universal compensation response."
    },
    {
      "field_path": "causal_graphs[0].edges[6].evidence[0]",
      "reference": "DOI:10.1038/nrmicro2549",
      "notes": "Bacteria maintain a distinct cytoplasmic pH required for protein function, bounding the phenotype.",
      "assessment": "Generic BioC opening links internal-pH compatibility to protein function and distinguishes growth ranges from survival outside growth ranges. Generic context is supported; formal enables roles are a separate question."
    },
    {
      "field_path": "causal_graphs[0].edges[7].evidence[0]",
      "reference": "DOI:10.3389/fmicb.2020.556140",
      "notes": "Modification of membrane lipid composition to reduce proton permeability is a general acid-stress mechanism.",
      "assessment": "Assigned mixed-context perspective identity and acid-response scope verified. Detailed lipid/acid-defense/fitness efficacy is UNASSESSED_SCOPE; neither validated nor refuted from the abstract."
    },
    {
      "field_path": "causal_graphs[0].edges[8].evidence[0]",
      "reference": "DOI:10.1038/nrmicro2549",
      "notes": "Na+/H+ antiport is the principal strategy for cytoplasmic pH homeostasis at high external pH.",
      "assessment": "Assigned broad homeostasis review identity and generic alkaline-homeostasis context verified. Detailed antiporter efficacy, necessity and pathogen intervention biology are UNASSESSED_SCOPE; no replacement mechanism or source transfer is supplied."
    },
    {
      "field_path": "causal_graphs[0].edges[9].evidence[0]",
      "reference": "DOI:10.3389/fmicb.2020.556140",
      "notes": "Decarboxylation of glutamate or arginine is a recurring proton-consuming acid-response module.",
      "assessment": "Assigned mixed-context perspective identity and acid-response scope verified. Detailed decarboxylation/defense/fitness efficacy is UNASSESSED_SCOPE; no reaction optimization or causal repair is provided."
    }
  ],
  "ontology_grounding_fields": [
    {
      "field_path": "causal_graphs[0].nodes[0].grounding",
      "reference": "METPO:1000332",
      "assessment": "Ontology identity and role interpretation owned by the separate grounding audit."
    },
    {
      "field_path": "causal_graphs[0].nodes[7].grounding",
      "reference": "GO:0051453",
      "assessment": "Ontology identity and role interpretation owned by the separate grounding audit."
    }
  ],
  "counts": {
    "external_placements": 14,
    "ontology_grounding_fields": 2
  }
}

### Native checklist: all six current excerpts

evidence: supported. Targets: METPO:1000332.

Six literal occurrences are verified. Both Baker impermeable-membrane phrases match its abstract; prior uncertainty about different Baker body phrases is not copied here. Alkaliphiles is confirmed in retained Krulwich BioC. Original native five VERIFIED/one NOT_IN_ABSTRACT remains unchanged.

{
  "completed_at": "2026-10-21T19:38:03.330169+00:00",
  "snippets": [
    {
      "field_path": "evidence[0].snippet",
      "reference": "DOI:10.1038/nrmicro2549",
      "snippet": "pH homeostasis",
      "outcome": "literal_exact",
      "hits": [
        {
          "surface": "indexed abstract",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-metadata.json",
          "locator": "abstractText",
          "sha256": "484784a62fbb4c9d74a1feab4df2fdfdf37d4dd0ce3fa79f714c86a07d86d29c"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 58",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 671",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 2440",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 3309",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 3940",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 6577",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 9102",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 9746",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 9793",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 10376",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 12201",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 13430",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 13534",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 15086",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 15130",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 16479",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 17378",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 18903",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 19769",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 20611",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 26699",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 27057",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 27702",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 34345",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 36727",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 39253",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 40107",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 42119",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 44016",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 48281",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 49779",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 51883",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 52269",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 53261",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 59345",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 61189",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 61308",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 67006",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 67131",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        }
      ],
      "scope": "Literal occurrence only; not validation of every surrounding causal claim. Machine matching of retained passages does not imply whole-body reading."
    },
    {
      "field_path": "evidence[1].snippet",
      "reference": "DOI:10.1016/j.tim.2007.02.005",
      "snippet": "highly impermeable cell membranes",
      "outcome": "literal_exact",
      "hits": [
        {
          "surface": "indexed abstract",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/baker-metadata.json",
          "locator": "abstractText",
          "sha256": "a78777bc3bb6444b32e2e8a13ab72c56d80592b97e30c9b5520c67cc040c631b"
        }
      ],
      "scope": "Literal occurrence only; not validation of every surrounding causal claim. Machine matching of retained passages does not imply whole-body reading."
    },
    {
      "field_path": "causal_graphs[0].edges[0].evidence[0].snippet",
      "reference": "DOI:10.1038/nrmicro2549",
      "snippet": "external pH",
      "outcome": "literal_exact",
      "hits": [
        {
          "surface": "indexed abstract",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-metadata.json",
          "locator": "abstractText",
          "sha256": "484784a62fbb4c9d74a1feab4df2fdfdf37d4dd0ce3fa79f714c86a07d86d29c"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 58",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 671",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 3940",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 4950",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 6577",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 7370",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 17378",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 30207",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 39253",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 45441",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 45597",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 47480",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        }
      ],
      "scope": "Literal occurrence only; not validation of every surrounding causal claim. Machine matching of retained passages does not imply whole-body reading."
    },
    {
      "field_path": "causal_graphs[0].edges[1].evidence[0].snippet",
      "reference": "DOI:10.1016/j.tim.2007.02.005",
      "snippet": "highly impermeable cell membranes",
      "outcome": "literal_exact",
      "hits": [
        {
          "surface": "indexed abstract",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/baker-metadata.json",
          "locator": "abstractText",
          "sha256": "a78777bc3bb6444b32e2e8a13ab72c56d80592b97e30c9b5520c67cc040c631b"
        }
      ],
      "scope": "Literal occurrence only; not validation of every surrounding causal claim. Machine matching of retained passages does not imply whole-body reading."
    },
    {
      "field_path": "causal_graphs[0].edges[2].evidence[0].snippet",
      "reference": "DOI:10.1038/nrmicro2549",
      "snippet": "alkaliphiles",
      "outcome": "literal_exact",
      "hits": [
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 5466",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 15130",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 16479",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 39232",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 39253",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 41582",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 42119",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 45597",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 61656",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        }
      ],
      "scope": "Literal occurrence only; not validation of every surrounding causal claim. Machine matching of retained passages does not imply whole-body reading."
    },
    {
      "field_path": "causal_graphs[0].edges[3].evidence[0].snippet",
      "reference": "DOI:10.1038/nrmicro2549",
      "snippet": "pH homeostasis",
      "outcome": "literal_exact",
      "hits": [
        {
          "surface": "indexed abstract",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-metadata.json",
          "locator": "abstractText",
          "sha256": "484784a62fbb4c9d74a1feab4df2fdfdf37d4dd0ce3fa79f714c86a07d86d29c"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 58",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 671",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 2440",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 3309",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 3940",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 6577",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 9102",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 9746",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 9793",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 10376",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 12201",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 13430",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 13534",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 15086",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 15130",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 16479",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 17378",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 18903",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 19769",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 20611",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 26699",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 27057",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 27702",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 34345",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 36727",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 39253",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 40107",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 42119",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 44016",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 48281",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 49779",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 51883",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 52269",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 53261",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 59345",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 61189",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 61308",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 67006",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml",
          "locator": "passage offset 67131",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f"
        }
      ],
      "scope": "Literal occurrence only; not validation of every surrounding causal claim. Machine matching of retained passages does not imply whole-body reading."
    }
  ],
  "counts": {
    "fields": 6,
    "literal_exact": 6,
    "unknown": 0,
    "indexed_abstract_exact": 5
  },
  "native_result": {
    "verified": 5,
    "not_in_abstract": 1
  },
  "qualification": "The sixth occurrence, alkaliphiles, is confirmed in retained primary BioC. Original native abstract-only results are unchanged. Both Baker impermeable-membrane occurrences are exact in its abstract; prior other Baker PMF/body uncertainty is not copied onto these different phrases."
}

### Native checklist: all eleven explicit referents

grounding: concern. Targets: METPO:1000332.

Numerical interval node 4 and nonmaterial gradient/potential nodes 5/6 conflict with their declared process/chemical facets. Treat these once in the linked representation group. Capacity wording at nodes 2/3 is qualified shorthand, while explicit activity, quality and reaction-class nodes remain legitimate.

[
  {
    "index": 0,
    "field_path": "causal_graphs[0].nodes[0]",
    "node_id": "ph_range_trait",
    "label": "pH range",
    "node_type": "TRAIT",
    "grounding": "METPO:1000332",
    "description": "Span of external pH values supporting growth.",
    "assessment": "Active pH-range trait identity and two direct parents agree."
  },
  {
    "index": 1,
    "field_path": "causal_graphs[0].nodes[1]",
    "node_id": "external_ph",
    "label": "external pH",
    "node_type": "ENVIRONMENTAL_FACTOR",
    "description": "Ambient proton activity (pH) imposed on the cell.",
    "assessment": "Ambient proton activity is an environmental condition/axis, not a material proton molecule or automatically an event."
  },
  {
    "index": 2,
    "field_path": "causal_graphs[0].nodes[2]",
    "node_id": "acid_tolerance",
    "label": "acid tolerance",
    "node_type": "BIOLOGICAL_PROCESS",
    "description": "Capacity to maintain cytoplasmic pH against an inward H+ gradient at low external pH.",
    "assessment": "Capacity wording can abbreviate a maintenance process. Native CAPACITY denotes pool/reservoir notions, so no automatic CAPACITY retype is warranted; clarify the intended disposition versus maintenance facet if revising this graph."
  },
  {
    "index": 3,
    "field_path": "causal_graphs[0].nodes[3]",
    "node_id": "alkaline_tolerance",
    "label": "alkaline tolerance",
    "node_type": "BIOLOGICAL_PROCESS",
    "description": "Capacity to maintain cytoplasmic pH against an outward H+ gradient at high external pH.",
    "assessment": "Same bounded process-versus-tolerance shorthand as node 2. No automatic type finding or mechanism completion requirement."
  },
  {
    "index": 4,
    "field_path": "causal_graphs[0].nodes[4]",
    "node_id": "bounded_growth_window",
    "label": "bounded pH growth window",
    "node_type": "BIOLOGICAL_PROCESS",
    "description": "Span of external pH between the minimum and maximum that supports growth.",
    "assessment": "Explicit span between minimum and maximum is a numerical growth interval, not a biological process. This endpoint choice also affects local defines/manifests-as and imported relation objects; assess once within the grouped representation finding."
  },
  {
    "index": 5,
    "field_path": "causal_graphs[0].nodes[5]",
    "node_id": "ph_gradient",
    "label": "transmembrane pH gradient (\u0394pH)",
    "node_type": "CHEMICAL",
    "description": "Difference between external and cytoplasmic pH, a component of the proton motive force.",
    "assessment": "Explicit pH difference is a gradient/state or measurable attribute, not a chemical entity. Material protons and their gradient are distinct; current CHEMICAL typing is a firm representation mismatch."
  },
  {
    "index": 6,
    "field_path": "causal_graphs[0].nodes[6]",
    "node_id": "membrane_potential",
    "label": "membrane potential (\u0394\u03c8)",
    "node_type": "CHEMICAL",
    "description": "Electrical component of the proton motive force across the cell membrane.",
    "assessment": "Explicit electrical membrane potential is a bioenergetic state/attribute, not a chemical entity. The free-text edge does not make this material; group with the linked representation audit."
  },
  {
    "index": 7,
    "field_path": "causal_graphs[0].nodes[7]",
    "node_id": "cytoplasmic_ph_homeostasis",
    "label": "cytoplasmic pH homeostasis",
    "node_type": "BIOLOGICAL_PROCESS",
    "description": "Maintenance of a near-constant cytoplasmic pH compatible with macromolecular function.",
    "grounding": "GO:0051453",
    "assessment": "Explicit pH-maintenance process has positive active GO:0051453 closeMatch. It is not a material executor for RO2327 edge 6."
  },
  {
    "index": 8,
    "field_path": "causal_graphs[0].nodes[8]",
    "node_id": "membrane_proton_impermeability",
    "label": "membrane proton impermeability",
    "node_type": "QUALITY",
    "description": "Reduced proton leak across the cell membrane that limits passive H+ influx.",
    "assessment": "Membrane proton impermeability is a quality facet. Reference to reduced leak does not force a process type."
  },
  {
    "index": 9,
    "field_path": "causal_graphs[0].nodes[9]",
    "node_id": "mrp_antiporter_activity",
    "label": "Mrp Na+/H+ antiporter activity",
    "node_type": "MOLECULAR_FUNCTION",
    "description": "Cation/proton antiport that imports protons while exporting Na+ to support pH homeostasis.",
    "assessment": "Explicit Mrp antiport activity is a legitimate MOLECULAR_FUNCTION; no material protein or mandatory instance is inferred. Detailed defense/fitness efficacy remains unassessed."
  },
  {
    "index": 10,
    "field_path": "causal_graphs[0].nodes[10]",
    "node_id": "amino_acid_decarboxylation",
    "label": "amino-acid decarboxylation",
    "node_type": "BIOLOGICAL_PROCESS",
    "description": "Glutamate or arginine decarboxylation that consumes intracellular protons and alkalinizes the cytoplasm.",
    "assessment": "Explicit amino-acid decarboxylation reaction class is BIOLOGICAL_PROCESS under the maintained convention. No named pathway or detailed defense mechanism is reconstructed."
  }
]

### Native checklist: all ten edges and linked endpoints

consistency: concern. Targets: METPO:1000332.

RO edges 4/6 have firm material/process role mismatches based on actual gradient and homeostasis-process subjects. Their shared interval endpoint and local edges 0–3 belong to the same representation discussion. Local defines/manifests-as formally admit broad endpoints; their prose concerns feature/state-to-trait semantics, not a fabricated strict formal domain. Free-text edges receive no invented imported constraints.

[
  {
    "index": 0,
    "field_path": "causal_graphs[0].edges[0]",
    "subject": "external_ph",
    "predicate": "defines",
    "predicate_id": "METPO:2007500",
    "object": "bounded_growth_window",
    "assessment": "Local defines has broad causal-node formal endpoints, but semantic feature-to-trait parameterization is imprecise when the current object is a numerical interval declared as process. Include in shared node4 representation discussion, not an invented local-domain violation.",
    "biology_scope": "UNASSESSED_SCOPE for detailed acid-defense, AMR, fitness and intervention efficacy; generic identity/formal semantics only"
  },
  {
    "index": 1,
    "field_path": "causal_graphs[0].edges[1]",
    "subject": "acid_tolerance",
    "predicate": "defines",
    "predicate_id": "METPO:2007500",
    "object": "bounded_growth_window",
    "assessment": "Tolerance may constrain an endpoint, but current defines feature/trait semantics and numerical-window referent need clarification. No additional unsupported biological or formal-domain finding; shared representation issue.",
    "biology_scope": "UNASSESSED_SCOPE for detailed acid-defense, AMR, fitness and intervention efficacy; generic identity/formal semantics only"
  },
  {
    "index": 2,
    "field_path": "causal_graphs[0].edges[2]",
    "subject": "alkaline_tolerance",
    "predicate": "defines",
    "predicate_id": "METPO:2007500",
    "object": "bounded_growth_window",
    "assessment": "Same qualified endpoint-definition precision as edge1; avoid treating a contextual upper-bound explanation as universal measured proof.",
    "biology_scope": "UNASSESSED_SCOPE for detailed acid-defense, AMR, fitness and intervention efficacy; generic identity/formal semantics only"
  },
  {
    "index": 3,
    "field_path": "causal_graphs[0].edges[3]",
    "subject": "bounded_growth_window",
    "predicate": "manifests as",
    "predicate_id": "METPO:2007400",
    "object": "ph_range_trait",
    "assessment": "Local manifests as describes physiological/molecular state to observable trait with broad formal endpoints. Current interval-as-process subject is not that described state; include in shared interval/trait representation issue, not a false process-only domain claim.",
    "biology_scope": "UNASSESSED_SCOPE for detailed acid-defense, AMR, fitness and intervention efficacy; generic identity/formal semantics only"
  },
  {
    "index": 4,
    "field_path": "causal_graphs[0].edges[4]",
    "subject": "ph_gradient",
    "predicate": "contributes to",
    "predicate_id": "RO:0002326",
    "object": "bounded_growth_window",
    "assessment": "Confirmed grouped role mismatch: actual gradient subject is nonmaterial despite CHEMICAL enum, while RO2326 inherits material-entity to process constraints. Explicit bounded interval object is not a process. Current enum labels cannot rescue the actual referents.",
    "biology_scope": "UNASSESSED_SCOPE for detailed acid-defense, AMR, fitness and intervention efficacy; generic identity/formal semantics only"
  },
  {
    "index": 5,
    "field_path": "causal_graphs[0].edges[5]",
    "subject": "membrane_potential",
    "predicate": "compensates for",
    "predicate_id": null,
    "object": "external_ph",
    "assessment": "Free-text compensates for has no asserted imported predicate constraints. Current potential node has a representation issue, but no mandatory grounding or fabricated RO type error is added. Detailed adaptation efficacy unassessed.",
    "biology_scope": "UNASSESSED_SCOPE for detailed acid-defense, AMR, fitness and intervention efficacy; generic identity/formal semantics only"
  },
  {
    "index": 6,
    "field_path": "causal_graphs[0].edges[6]",
    "subject": "cytoplasmic_ph_homeostasis",
    "predicate": "enables",
    "predicate_id": "RO:0002327",
    "object": "bounded_growth_window",
    "assessment": "Confirmed grouped role mismatch independent of the window facet: RO2327 requires a material executor and process object, while the subject is explicitly GO-grounded homeostasis process. The current interval object further complicates the process range. No new mechanism proposed.",
    "biology_scope": "UNASSESSED_SCOPE for detailed acid-defense, AMR, fitness and intervention efficacy; generic identity/formal semantics only"
  },
  {
    "index": 7,
    "field_path": "causal_graphs[0].edges[7]",
    "subject": "membrane_proton_impermeability",
    "predicate": "extends",
    "predicate_id": null,
    "object": "acid_tolerance",
    "assessment": "Free-text extends remains ungrounded and is not assigned RO constraints. Quality to maintenance/tolerance context is documentary only; detailed acid-defense/fitness efficacy unassessed.",
    "biology_scope": "UNASSESSED_SCOPE for detailed acid-defense, AMR, fitness and intervention efficacy; generic identity/formal semantics only"
  },
  {
    "index": 8,
    "field_path": "causal_graphs[0].edges[8]",
    "subject": "mrp_antiporter_activity",
    "predicate": "supports",
    "predicate_id": null,
    "object": "alkaline_tolerance",
    "assessment": "Free-text supports remains ungrounded. Explicit activity subject is legitimate; no mandatory protein or imported-domain finding. Detailed acid-defense efficacy unassessed.",
    "biology_scope": "UNASSESSED_SCOPE for detailed acid-defense, AMR, fitness and intervention efficacy; generic identity/formal semantics only"
  },
  {
    "index": 9,
    "field_path": "causal_graphs[0].edges[9]",
    "subject": "amino_acid_decarboxylation",
    "predicate": "alkalinizes",
    "predicate_id": null,
    "object": "cytoplasmic_ph_homeostasis",
    "assessment": "Free-text alkalinizes has no imported relation type rule. Its process-object wording can be read as shorthand for supporting homeostasis; retain a semantic limitation rather than declaring wrong biology or prescribing a pathway.",
    "biology_scope": "UNASSESSED_SCOPE for detailed acid-defense, AMR, fitness and intervention efficacy; generic identity/formal semantics only"
  }
]

### Native checklist: generic context and exclusions

scope: unknown. Targets: METPO:1000332.

Generic pH-range and PMF attribution is assessed. Detailed acid-defense, pathogen fitness, AMR, antiporter/decarboxylation efficacy and intervention or perturbation effects remain UNASSESSED_SCOPE. Literal occurrence and role compatibility do not validate efficacy; no repaired mechanism, route or experimental recommendation is supplied.

{
  "completed_at": "2026-10-21T19:38:03.316677+00:00",
  "edges": [
    {
      "index": 0,
      "field_path": "causal_graphs[0].edges[0]",
      "subject": "external_ph",
      "predicate": "defines",
      "object": "bounded_growth_window",
      "predicate_id": "METPO:2007500",
      "description": "External pH defines the axis over which the growth window is bounded.",
      "evidence": [
        {
          "reference": "DOI:10.1038/nrmicro2549",
          "snippet": "external pH",
          "notes": "Supports external pH as the axis bounding the growth window."
        }
      ],
      "assessment": "Generic external-pH axis is directly supported by the assigned abstract and BioC opening; exact measured boundaries remain organism-specific.",
      "biological_scope": "Generic environmental context and source attribution only; no universal biological sufficiency claim"
    },
    {
      "index": 1,
      "field_path": "causal_graphs[0].edges[1]",
      "subject": "acid_tolerance",
      "predicate": "defines",
      "object": "bounded_growth_window",
      "predicate_id": "METPO:2007500",
      "description": "Acid tolerance sets the lower bound of the pH growth window.",
      "evidence": [
        {
          "reference": "DOI:10.1016/j.tim.2007.02.005",
          "snippet": "highly impermeable cell membranes",
          "notes": "Supports envelope proton barriers as the lower-bound mechanism for low-pH growth."
        }
      ],
      "assessment": "The exact assigned acidophile abstract supports low-pH membrane-barrier context. This is generic lower-bound context, not a universal single necessary or sufficient mechanism.",
      "biological_scope": "Generic environmental context and source attribution only; no universal biological sufficiency claim"
    },
    {
      "index": 2,
      "field_path": "causal_graphs[0].edges[2]",
      "subject": "alkaline_tolerance",
      "predicate": "defines",
      "object": "bounded_growth_window",
      "predicate_id": "METPO:2007500",
      "description": "Alkaline tolerance sets the upper bound of the pH growth window.",
      "evidence": [
        {
          "reference": "DOI:10.1038/nrmicro2549",
          "snippet": "alkaliphiles",
          "notes": "Supports alkaline-tolerance physiology as the upper-bound mechanism for high-pH growth."
        }
      ],
      "assessment": "Assigned Krulwich text explicitly discusses alkaliphiles and growth at elevated external pH. Generic upper-bound context is supported; no universal single strategy or exact numerical cutoff is inferred.",
      "biological_scope": "Generic environmental context and source attribution only; no universal biological sufficiency claim"
    },
    {
      "index": 3,
      "field_path": "causal_graphs[0].edges[3]",
      "subject": "bounded_growth_window",
      "predicate": "manifests as",
      "object": "ph_range_trait",
      "predicate_id": "METPO:2007400",
      "description": "The bounded pH growth window manifests the pH-range phenotype.",
      "evidence": [
        {
          "reference": "DOI:10.1038/nrmicro2549",
          "snippet": "pH homeostasis",
          "notes": "Supports the trait endpoint."
        }
      ],
      "assessment": "Generic pH-homeostasis context is supported; the measurement/trait relationship and local predicate semantics are assessed independently by grounding, not proved by the two-word snippet.",
      "biological_scope": "Generic environmental context and source attribution only; no universal biological sufficiency claim"
    },
    {
      "index": 4,
      "field_path": "causal_graphs[0].edges[4]",
      "subject": "ph_gradient",
      "predicate": "contributes to",
      "object": "bounded_growth_window",
      "predicate_id": "RO:0002326",
      "description": "The transmembrane pH gradient sets whether cytoplasmic pH can be maintained across the external pH range.",
      "evidence": [
        {
          "reference": "DOI:10.1038/nrmicro2549",
          "notes": "PMF architecture (\u0394\u03c8 \u2212 59 \u0394pH) determines the range of pHout over which bacteria can tolerate or grow."
        }
      ],
      "assessment": "BioC offsets 2440 and 3214 support the two-component PMF and approximation under standard conditions. Offset 3940 supplies condition-specific illustrative patterns. The current note is contextual; the approximation alone does not calibrate a complete growth interval or prove biological sufficiency.",
      "biological_scope": "Generic environmental context and source attribution only; no universal biological sufficiency claim"
    },
    {
      "index": 5,
      "field_path": "causal_graphs[0].edges[5]",
      "subject": "membrane_potential",
      "predicate": "compensates for",
      "object": "external_ph",
      "predicate_id": null,
      "description": "Adjustment or reversal of the membrane-potential PMF component offsets extreme external pH stress.",
      "evidence": [
        {
          "reference": "DOI:10.1038/nrmicro2549",
          "notes": "Under strong pH stress the orientation of a PMF component can reverse to maintain homeostasis."
        }
      ],
      "assessment": "BioC offset 3940 explicitly illustrates reversed PMF components in distinct growth-pH contexts. Preserve source-specific illustrations and generic context; this does not certify a universal compensation response.",
      "biological_scope": "Generic environmental context and source attribution only; no universal biological sufficiency claim"
    },
    {
      "index": 6,
      "field_path": "causal_graphs[0].edges[6]",
      "subject": "cytoplasmic_ph_homeostasis",
      "predicate": "enables",
      "object": "bounded_growth_window",
      "predicate_id": "RO:0002327",
      "description": "Keeping cytoplasmic pH compatible with protein function enables growth across the external pH range.",
      "evidence": [
        {
          "reference": "DOI:10.1038/nrmicro2549",
          "notes": "Bacteria maintain a distinct cytoplasmic pH required for protein function, bounding the phenotype."
        }
      ],
      "assessment": "Generic BioC opening links internal-pH compatibility to protein function and distinguishes growth ranges from survival outside growth ranges. Generic context is supported; formal enables roles are a separate question.",
      "biological_scope": "Generic environmental context and source attribution only; no universal biological sufficiency claim"
    },
    {
      "index": 7,
      "field_path": "causal_graphs[0].edges[7]",
      "subject": "membrane_proton_impermeability",
      "predicate": "extends",
      "object": "acid_tolerance",
      "predicate_id": null,
      "description": "Reduced proton leak helps maintain cytoplasmic pH and extends growth to lower external pH.",
      "evidence": [
        {
          "reference": "DOI:10.3389/fmicb.2020.556140",
          "notes": "Modification of membrane lipid composition to reduce proton permeability is a general acid-stress mechanism."
        }
      ],
      "assessment": "Assigned mixed-context perspective identity and acid-response scope verified. Detailed lipid/acid-defense/fitness efficacy is UNASSESSED_SCOPE; neither validated nor refuted from the abstract.",
      "biological_scope": "UNASSESSED_SCOPE detailed biological efficacy"
    },
    {
      "index": 8,
      "field_path": "causal_graphs[0].edges[8]",
      "subject": "mrp_antiporter_activity",
      "predicate": "supports",
      "object": "alkaline_tolerance",
      "predicate_id": null,
      "description": "Na+/H+ exchange imports protons and is a principal strategy for alkaline pH homeostasis.",
      "evidence": [
        {
          "reference": "DOI:10.1038/nrmicro2549",
          "notes": "Na+/H+ antiport is the principal strategy for cytoplasmic pH homeostasis at high external pH."
        }
      ],
      "assessment": "Assigned broad homeostasis review identity and generic alkaline-homeostasis context verified. Detailed antiporter efficacy, necessity and pathogen intervention biology are UNASSESSED_SCOPE; no replacement mechanism or source transfer is supplied.",
      "biological_scope": "UNASSESSED_SCOPE detailed biological efficacy"
    },
    {
      "index": 9,
      "field_path": "causal_graphs[0].edges[9]",
      "subject": "amino_acid_decarboxylation",
      "predicate": "alkalinizes",
      "object": "cytoplasmic_ph_homeostasis",
      "predicate_id": null,
      "description": "Glutamate or arginine decarboxylation consumes intracellular protons, supporting cytoplasmic pH at acidic external pH.",
      "evidence": [
        {
          "reference": "DOI:10.3389/fmicb.2020.556140",
          "notes": "Decarboxylation of glutamate or arginine is a recurring proton-consuming acid-response module."
        }
      ],
      "assessment": "Assigned mixed-context perspective identity and acid-response scope verified. Detailed decarboxylation/defense/fitness efficacy is UNASSESSED_SCOPE; no reaction optimization or causal repair is provided.",
      "biological_scope": "UNASSESSED_SCOPE detailed biological efficacy"
    }
  ],
  "scope": "All current edges accounted for. Source attribution is separate from formal ontology role correctness. Detailed pathogen acid-defense/fitness/AMR and intervention efficacy are unassessed."
}

### Native checklist: whole current record and optional evidence

completeness: supported. Targets: METPO:1000332.

All eleven nodes, ten edges, one component, one canonical, six excerpts and twelve record events are covered. There are zero protein-class nodes and zero instances. The nonmechanistic interval scope does not require token proteins, accessions, extra connectors or newly named pathways.

{
  "completed_at": "2026-10-21T19:38:03.317040+00:00",
  "nodes": [
    {
      "index": 0,
      "field_path": "causal_graphs[0].nodes[0]",
      "node": {
        "node_id": "ph_range_trait",
        "label": "pH range",
        "node_type": "TRAIT",
        "grounding": "METPO:1000332",
        "description": "Span of external pH values supporting growth."
      },
      "incident_edges": [
        3
      ],
      "source_references": [
        "DOI:10.1038/nrmicro2549"
      ],
      "assessment": "Current node and all incident evidence placements documented. Referent/facet and imported-ontology semantics belong to the grounding ledger. Generic physicochemical/measurement context assessed without asserting universal necessity or exact interval calibration."
    },
    {
      "index": 1,
      "field_path": "causal_graphs[0].nodes[1]",
      "node": {
        "node_id": "external_ph",
        "label": "external pH",
        "node_type": "ENVIRONMENTAL_FACTOR",
        "description": "Ambient proton activity (pH) imposed on the cell."
      },
      "incident_edges": [
        0,
        5
      ],
      "source_references": [
        "DOI:10.1038/nrmicro2549"
      ],
      "assessment": "Current node and all incident evidence placements documented. Referent/facet and imported-ontology semantics belong to the grounding ledger. Generic physicochemical/measurement context assessed without asserting universal necessity or exact interval calibration."
    },
    {
      "index": 2,
      "field_path": "causal_graphs[0].nodes[2]",
      "node": {
        "node_id": "acid_tolerance",
        "label": "acid tolerance",
        "node_type": "BIOLOGICAL_PROCESS",
        "description": "Capacity to maintain cytoplasmic pH against an inward H+ gradient at low external pH."
      },
      "incident_edges": [
        1,
        7
      ],
      "source_references": [
        "DOI:10.1016/j.tim.2007.02.005",
        "DOI:10.3389/fmicb.2020.556140"
      ],
      "assessment": "Current node and all incident evidence placements documented. Referent/facet and imported-ontology semantics belong to the grounding ledger. Generic physicochemical/measurement context assessed without asserting universal necessity or exact interval calibration."
    },
    {
      "index": 3,
      "field_path": "causal_graphs[0].nodes[3]",
      "node": {
        "node_id": "alkaline_tolerance",
        "label": "alkaline tolerance",
        "node_type": "BIOLOGICAL_PROCESS",
        "description": "Capacity to maintain cytoplasmic pH against an outward H+ gradient at high external pH."
      },
      "incident_edges": [
        2,
        8
      ],
      "source_references": [
        "DOI:10.1038/nrmicro2549"
      ],
      "assessment": "Current node and all incident evidence placements documented. Referent/facet and imported-ontology semantics belong to the grounding ledger. Generic physicochemical/measurement context assessed without asserting universal necessity or exact interval calibration."
    },
    {
      "index": 4,
      "field_path": "causal_graphs[0].nodes[4]",
      "node": {
        "node_id": "bounded_growth_window",
        "label": "bounded pH growth window",
        "node_type": "BIOLOGICAL_PROCESS",
        "description": "Span of external pH between the minimum and maximum that supports growth."
      },
      "incident_edges": [
        0,
        1,
        2,
        3,
        4,
        6
      ],
      "source_references": [
        "DOI:10.1016/j.tim.2007.02.005",
        "DOI:10.1038/nrmicro2549"
      ],
      "assessment": "Current node and all incident evidence placements documented. Referent/facet and imported-ontology semantics belong to the grounding ledger. Generic physicochemical/measurement context assessed without asserting universal necessity or exact interval calibration."
    },
    {
      "index": 5,
      "field_path": "causal_graphs[0].nodes[5]",
      "node": {
        "node_id": "ph_gradient",
        "label": "transmembrane pH gradient (\u0394pH)",
        "node_type": "CHEMICAL",
        "description": "Difference between external and cytoplasmic pH, a component of the proton motive force."
      },
      "incident_edges": [
        4
      ],
      "source_references": [
        "DOI:10.1038/nrmicro2549"
      ],
      "assessment": "Current node and all incident evidence placements documented. Referent/facet and imported-ontology semantics belong to the grounding ledger. Generic physicochemical/measurement context assessed without asserting universal necessity or exact interval calibration."
    },
    {
      "index": 6,
      "field_path": "causal_graphs[0].nodes[6]",
      "node": {
        "node_id": "membrane_potential",
        "label": "membrane potential (\u0394\u03c8)",
        "node_type": "CHEMICAL",
        "description": "Electrical component of the proton motive force across the cell membrane."
      },
      "incident_edges": [
        5
      ],
      "source_references": [
        "DOI:10.1038/nrmicro2549"
      ],
      "assessment": "Current node and all incident evidence placements documented. Referent/facet and imported-ontology semantics belong to the grounding ledger. Generic physicochemical/measurement context assessed without asserting universal necessity or exact interval calibration."
    },
    {
      "index": 7,
      "field_path": "causal_graphs[0].nodes[7]",
      "node": {
        "node_id": "cytoplasmic_ph_homeostasis",
        "label": "cytoplasmic pH homeostasis",
        "node_type": "BIOLOGICAL_PROCESS",
        "description": "Maintenance of a near-constant cytoplasmic pH compatible with macromolecular function.",
        "grounding": "GO:0051453"
      },
      "incident_edges": [
        6,
        9
      ],
      "source_references": [
        "DOI:10.1038/nrmicro2549",
        "DOI:10.3389/fmicb.2020.556140"
      ],
      "assessment": "Current node and all incident evidence placements documented. Referent/facet and imported-ontology semantics belong to the grounding ledger. Generic physicochemical/measurement context assessed without asserting universal necessity or exact interval calibration."
    },
    {
      "index": 8,
      "field_path": "causal_graphs[0].nodes[8]",
      "node": {
        "node_id": "membrane_proton_impermeability",
        "label": "membrane proton impermeability",
        "node_type": "QUALITY",
        "description": "Reduced proton leak across the cell membrane that limits passive H+ influx."
      },
      "incident_edges": [
        7
      ],
      "source_references": [
        "DOI:10.3389/fmicb.2020.556140"
      ],
      "assessment": "Current node and all incident evidence placements documented. Referent/facet and imported-ontology semantics belong to the grounding ledger. Detailed pathway/defense efficacy UNASSESSED_SCOPE."
    },
    {
      "index": 9,
      "field_path": "causal_graphs[0].nodes[9]",
      "node": {
        "node_id": "mrp_antiporter_activity",
        "label": "Mrp Na+/H+ antiporter activity",
        "node_type": "MOLECULAR_FUNCTION",
        "description": "Cation/proton antiport that imports protons while exporting Na+ to support pH homeostasis."
      },
      "incident_edges": [
        8
      ],
      "source_references": [
        "DOI:10.1038/nrmicro2549"
      ],
      "assessment": "Current node and all incident evidence placements documented. Referent/facet and imported-ontology semantics belong to the grounding ledger. Detailed pathway/defense efficacy UNASSESSED_SCOPE."
    },
    {
      "index": 10,
      "field_path": "causal_graphs[0].nodes[10]",
      "node": {
        "node_id": "amino_acid_decarboxylation",
        "label": "amino-acid decarboxylation",
        "node_type": "BIOLOGICAL_PROCESS",
        "description": "Glutamate or arginine decarboxylation that consumes intracellular protons and alkalinizes the cytoplasm."
      },
      "incident_edges": [
        9
      ],
      "source_references": [
        "DOI:10.3389/fmicb.2020.556140"
      ],
      "assessment": "Current node and all incident evidence placements documented. Referent/facet and imported-ontology semantics belong to the grounding ledger. Detailed pathway/defense efficacy UNASSESSED_SCOPE."
    }
  ]
}

### Native checklist: retained catalog applicability

evidence: unknown. Targets: METPO:1000332.

The complete retained 20-organism/28-dataset catalog has no match for the canonical Oceanimonas genus/species or verified strain aliases. This is bounded to the snapshot; no substitute organism or downstream defense gene/module query was used.

{
  "assessed_at": "2026-10-21T19:38:01.754511+00:00",
  "target": "data/traits/environment/ph_range.yaml",
  "status": "NO_CANONICAL_CATALOG_MATCH",
  "canonical_taxon": "NCBITaxon:3028314",
  "canonical_name": "Oceanimonas pelagia",
  "names_and_aliases_checked": [
    "Oceanimonas",
    "Oceanimonas pelagia",
    "Oceanimonas sp. NTOU-MSR1",
    "NTOU-MSR1",
    "BCRC 81403",
    "JCM 36023"
  ],
  "catalog_counts": {
    "organisms": 20,
    "datasets": 28
  },
  "matches": [],
  "original_access": {
    "started_at": "2026-10-21T07:36:12.732638+00:00",
    "finished_at": "2026-10-21T07:36:12.858149+00:00"
  },
  "catalog": {
    "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-grounding-agent/reused-datasets.json",
    "sha256": "155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693",
    "bytes": 2871
  },
  "reuse": {
    "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-grounding-agent/authority-reuse-receipts.json",
    "sha256": "99da6e94f5769c9ad5bd2d16565a49363d5552f77565d17b781c61bb5482ca14",
    "bytes": 2011
  },
  "scope": "Complete retained structured catalog checked for the official canonical genus/species and strain aliases only. No substitute organism, downstream gene/module query or detailed acid-defense/fitness/intervention analysis. Absence is bounded to this catalog snapshot.",
  "optional_proteins": "Zero protein-class nodes and zero instances do not create a completeness failure in this NONMECHANISTIC quantitative record."
}

### Native checklist: current owners and recurrence limits

provenance: supported. Targets: METPO:1000332.

The current record owns the interval/gradient declarations. Predicate mappings and the shared writer own assignment, with nonempty IDs skipped. No exact current gradient-repair writer was established; the ph_range_mid2 writer is sibling context only. Canonical backfill and reaction-class migration are positive, distinct owners of their own fields.

{
  "assessed_at": "2026-10-21T19:38:01.753184+00:00",
  "target": "data/traits/environment/ph_range.yaml",
  "counts": {
    "nodes": 11,
    "edges": 10,
    "components": 1,
    "protein_classes": 0,
    "label_only_proteins": 0,
    "protein_instances": 0,
    "canonical_examples": 1,
    "record_history_events": 12,
    "ai_record_events": 11,
    "seed_events": 1,
    "captured_histories": 7,
    "whole_histories_read": 7,
    "matching_paths": 325,
    "review_target_arrays": 68,
    "exact_target_review_arrays": 0
  },
  "search": {
    "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-grounding-agent/search-and-provenance.json",
    "sha256": "b7ed29d8b076b710ec708b7a2996120c3df0e0ca1e5b54156a2b3fca736a5cda",
    "bytes": 101712
  },
  "node_search": {
    "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-grounding-agent/all-node-owner-search.json",
    "sha256": "a5010a2c11125029ec472073eccab54ff3e2616fd4c9bd2db39ed1fe0ab5f759",
    "bytes": 6658
  },
  "exact_owner_search": {
    "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-grounding-agent/exact-owner-search.json",
    "sha256": "b1baaa328c01ebaf58525851ca19e31969803425e3e48a60926acfb1f9eccc8c",
    "bytes": 1291
  },
  "search_scope": "Entire repository including ignored/hidden files except .git internals and .venv; fixed-string case-insensitive target slug/hyphen/label/full and numeric ID. Because pH range overlaps sibling names, each structured target array was parsed exactly. All 11 node identifiers separately searched; seven history leads captured, none uncaptured.",
  "history_scope": "All seven captured histories read in full and actor/target projections checked. They are AI-authored infrastructure, canonical-batch or ph_range_mid2 sibling context; not linked human acceptance of the current graph. No full unlisted history read is claimed.",
  "human_acceptance": "Current created_by Luke Wang and upstream creator attribution are retained as positive human concept provenance. No linked acceptance of later AI-enriched current record/graph found in 325 matching paths, 68 structured target arrays with zero exact target, or seven AI histories. The 12 record events comprise 11 AI edits and an automated seed. This is a bounded acceptance-link gap, not a claim that no human ever reviewed the concept.",
  "owners": [
    {
      "path": "data/traits/environment/ph_range.yaml",
      "role": "Primary current owner of interval/gradient/electrical-potential declarations and affected edges; no exact maintained node-repair writer for current ph_range established in bounded search.",
      "sha256": "8a9cac2ea39eaf0aaafb950fce9b8119713bbef55c43e84550f22c3ee9d13d1a"
    },
    {
      "path": "mappings/predicate_grounding.tsv",
      "role": "Maintained RO2326/RO2327, defines and manifests-as mappings; wildcard gates do not remove imported semantics.",
      "sha256": "8e28c19e93aca3dc164a3befbe2612b289241de457c59f499e65936c03b7ce52"
    },
    {
      "path": "scripts/ground_causal_predicates.py",
      "role": "Shared assignment writer skips all already nonempty predicate_id values; changing a mapping alone does not repair current edges.",
      "sha256": "5a788eeaabf3a56b0d82c469a3e3fe28f1d51707d9382313b9a94289be7d1381"
    },
    {
      "path": "mappings/node_grounding.tsv",
      "role": "Positive GO0051453 closeMatch row27; not a current gradient retyping owner.",
      "sha256": "d7de9b3ab04960c4775a5bc295a945bd1a72d81467830459f4793e654f82b3d0"
    },
    {
      "path": "scripts/ground_causal_nodes.py",
      "role": "Shared node-grounding writer skips existing nonempty grounds; positive homeostasis mapping does not turn process into material executor.",
      "sha256": "204ce4162544154b1752b65da2136538847ea25ced26a52f5708eadff08f5d42"
    },
    {
      "path": "scripts/migrate_pathway_vs_process.py",
      "role": "Direct current amino_acid_decarboxylation facet maintainer: node-id table plus corpus traversal/upsert. Its BIOLOGICAL_PROCESS decision is positive; it is not an owner of current gradient/interval node corrections.",
      "sha256": "f236de7183048732e9001b7fac4367affff58d8b7a7d5c63286e6b058a4b38c2"
    },
    {
      "path": "scripts/backfill_canonical_examples_444.py",
      "role": "Exact environment/ph_range canonical entry at line433; live queue guard, identical-existing no-op and nonempty-drift rejection. Direct canonical owner only.",
      "sha256": "18ca0766789c239d693ef665e8b1d43c1209a0f414a326f1c5d890f88de7b20c"
    },
    {
      "path": "scripts/review_ph_range_mid2_graph_183.py",
      "role": "Sibling-only writer, explicit environment/ph_range_mid2 SLUG; its membrane_potential STATE replacement is comparator context, not current ph_range recurrence ownership.",
      "sha256": "2788c907439099c64cbc25c50b973e5ac0d2b93bc07ff7ed89e4cddaae500bd3"
    },
    {
      "path": "scripts/migrate_node_type_consistency.py",
      "role": "Generic STATE/PMF context; bounded exact-key search does not establish a current ph_gradient or membrane_potential replacement in this table.",
      "sha256": "a3e7bc170e60f406a73e06c893d74f5253671028d3d40cc15ecf882b6684a69e"
    },
    {
      "path": "scripts/migrate_process_quality_consistency.py",
      "role": "Related reversed-potential and permeability families are contextual; not exact owners of the current ph_range gradient/interval nodes.",
      "sha256": "1a83ad3dba79ed0c958b875a6fcc4b9e562259af26da2f248d32d5cf7784f80a"
    }
  ],
  "research_limit": "Only current Falcon frontmatter read: August4 artifact is contextual and does not establish the exact report version behind June23 enrichment.",
  "readiness": "Needs curation for grouped representation and relation roles. No target, writer, state or Git mutation; no native checks executed by this auditor."
}

### Native checklist: creator versus current acceptance

provenance: concern. Targets: METPO:1000332.

Luke Wang concept attribution remains positive. The bounded ignored-inclusive search found 325 paths and 68 parsed review target arrays, with zero exact target arrays. Seven captured AI histories were fully read. Twelve record events comprise eleven AI edits plus seed; none of these alone links human acceptance of the later current graph.

### Native checklist: actual checks and qualified common reuse

consistency: supported. Targets: METPO:1000332.

All 77 captured inputs and frozen artifacts match. Focused native, strict and snippet checks passed. Historical common failures, retries, skips and original times remain explicit under actual B10-to-B11 qualification. No new B11 QC execution is claimed.

## Findings

### linked-representation-roles: Interval and electrochemical states conflict with linked declared and imported roles

major / open / confirmed; issue key: ph-range-linked-representation-roles.

Node 4 explicitly denotes a numerical interval, while nodes 5/6 denote a nonmaterial pH gradient and electrical potential. Their process/chemical declarations conflict with these referents. RO:0002326 edge 4 and RO:0002327 edge 6 require material subjects and process objects; the actual gradient/process subjects and shared interval object fail these roles. Local edges 0–3 expose the same interval/trait referent choice, with broad formal proposal endpoints. This is one linked representation finding, not repeated penalties for each shared endpoint.

### baker-attribution-scope: Assigned acidophile attribution is broadened to alkaline extremes

minor / open / confirmed; issue key: ph-range-baker-attribution-scope.

The actual Baker abstract supports its exact impermeable-membrane phrase in acidophiles and low-pH growth. Evidence[1].notes extends this assigned attribution to both acidic and alkaline extremes. Clarify the supported source scope or substantiate the broader attribution. The inaccessible full article is not declared devoid of alkaline discussion, and the acid lower-bound placement and quotations remain positive.

### human-acceptance-link: Current graph lacks a linked acceptance reference within the bounded local search

minor / open / confirmed; issue key: ph-range-human-acceptance-link.

Known Luke Wang concept authorship is retained. REVIEWED status, AI enrichment and passing checks do not independently identify human acceptance of the current graph. The ignored-inclusive local search and exact target parsing bound this finding; remote or private human decisions are not declared absent.

## Recommended Actions And Acceptance Checks

### reconcile-representation

Reconcile the existing interval, gradient and potential referents with their declared facets and relation semantics during separately authorized curation.

- Resolve the shared interval endpoint once across local edges 0–3 and imported edges 4/6; preserve the distinction between broad formal local endpoints and descriptive feature/state-to-trait semantics.
- Keep legitimate activity and reaction-class nodes, qualified capacity shorthand and free-text predicates separate from the confirmed anchors. Do not impose an automatic replacement type or biological route.
- Inspect actual shared-writer nonempty-ID behavior; mapping-only edits do not repair existing assertions. No sibling writer is a current recurrence owner. Use guarded history, appropriate native/strict/grounding/QC checks and a successor review after changed inputs.

### qualify-baker-attribution

Qualify evidence[1].notes to the actually supported acidophile attribution or add separately verified support for the broader scope.

- Preserve both exact Baker phrases and the supported acid lower-bound context.
- Do not convert inaccessible full text into a false-quote or false-biology conclusion, and do not add detailed defense or intervention mechanisms.

### link-human-acceptance

Link existing attributable current acceptance if available, or clarify status while preserving known concept and AI provenance.

- Preserve Luke Wang attribution, bounded search counts and seven-history reading scope.
- No contact, automatic status promotion or inference of acceptance from validators is authorized.

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
| check-ph-range-native | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-native.log; Executed 2026-10-21T19:34:55.779565+00:00 through 2026-10-21T19:34:56.724090+00:00; metadata ph-range-native.json | context_only | Direct successful current-target schema validation; formal roles are assessed separately. |
| check-ph-range-strict | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-strict.log; Executed 2026-10-21T19:34:55.782628+00:00 through 2026-10-21T19:34:57.432414+00:00; metadata ph-range-strict.json | context_only | Direct successful current-target strict validation; no biological efficacy certification. |
| check-ph-range-snippets | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-snippets.log; Executed 2026-10-21T19:34:59.658831+00:00 through 2026-10-21T19:35:03.592067+00:00; metadata ph-range-snippets.json | context_only | Six fields over two references: five VERIFIED and one NOT_IN_ABSTRACT. Independent retained primary text verifies all six literal occurrences without changing the native result. |
| check-batch010-qc | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/batch010-qc.log; Executed 2026-10-21T19:06:27.731868+00:00 through 2026-10-21T19:08:11.219124+00:00; metadata batch010-qc.json | context_only | Actual B10 final QC at its original time, qualified against B11 bytes; not a fresh B11 execution. |
| record | data/traits/environment/ph_range.yaml; Entire current record | supports | All eleven nodes, ten edges, one canonical, six snippet fields and twelve record events are covered. |
| policy | docs/GROUNDING_POLICY.md; Captured maintained authority | supports | Native referents and optional protein evidence; no token class or accession requirement. |
| playbook | docs/CURATION_PLAYBOOK.md; Captured maintained authority | supports | Source scope and exact quotation; known concept creator is distinct from later human graph acceptance. |
| schema | src/traitmech/schema/traitmech.yaml; Captured maintained authority | supports | Actual process, state, chemical, quality and activity facets. |
| checklist | .claude/skills/curate-yaml-record/references/review-checklist.md; Captured maintained authority | supports | Whole-record identity, evidence, hierarchy, graph, provenance, owners and readiness coverage. |
| reuse | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-b10-qc-supplement-qualified.json; Actual B10-to-B11 qualification | supports | All trait/history/common comparisons and retained diagnostics are bound. |
| reuse-postcheck | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-output-verification-agent/post-execution-verification.json; Independent qualification postcheck | supports | Actual byte and output bindings verified without repeating QC. |
| capture | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-grounding-agent/capture-verification.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Successful 77-input capture independently rehashed. |
| identity | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-grounding-agent/identity-assessment.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Active identity, both parents, two explicit obsolete replacements, known human creator and official source identities. |
| node-edges | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-grounding-agent/node-edge-ledger.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | All current nodes and edges, with one linked interval/gradient/imported-role representation group. |
| owners | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-grounding-agent/owner-provenance-assessment.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Exact current owners and contextual writers distinguished; bounded human acceptance search. |
| expression | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-grounding-agent/expression-applicability.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Actual retained catalog checked against official genus/species and strain aliases. |
| authority-reuse | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-grounding-agent/authority-reuse-receipts.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Original catalog and runner times remain distinct from copying. |
| identity-reuse | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-grounding-agent/primary-identity-reuse.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Official taxon and GO original acquisitions, copies and earlier taxon failure retained. |
| local-authority | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-grounding-agent/local-authority-excerpts.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Broad local formal endpoints are distinguished from describes-feature/state-to-trait semantics. |
| ground-reading | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-grounding-agent/primary-reading-scope.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Actual authority/history reading scope. |
| ground-manifest | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-grounding-agent/evidence-manifest.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | All twenty-seven frozen grounding artifacts verified. |
| metpo-primary | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/repo/data/raw/metpo.owl; Actual target, parent and obsolete-term XML | supports | Both parents and two explicit replacement links are positive. The target has no textual raw definition; the current definition is assessed as a synthesis. Luke Wang concept authorship is retained. |
| ro-primary | /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/ro.db; RO:0002326 → 2216 → 2500 → 2595; RO:0002327 inheritance | supports | Contributes-to and enables inherit material-subject/process-object roles. Current gradient and homeostasis-process subjects are assessed by their actual referents, not rescued by enum labels. |
| taxonomy-primary | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-grounding-agent/taxon3028314.xml; Official NCBITaxon:3028314 response | supports | Oceanimonas pelagia species and NTOU-MSR1/BCRC 81403/JCM 36023 type aliases agree. Phenotype support comes separately from the cited abstract. |
| go-primary | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-grounding-agent/go0051453.response; Actual official GO:0051453 response | supports | Active regulation of intracellular pH is compatible with the maintained closeMatch to the homeostasis process; no material protein identity is inferred. |
| meta-krulwich | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-metadata.json; Actual current indexed metadata/abstract | supports | Actual assigned indexed identity, abstract and returned notice fields only; body evidence is separate. |
| meta-baker | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/baker-metadata.json; Actual current indexed metadata/abstract | supports | Actual acidophile abstract contains the exact impermeable-membrane phrase and low-pH context. Its full body remains unavailable; broader alkaline attribution is assessed with that limit. |
| meta-acid-review | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/acid-review-metadata.json; Actual current indexed metadata/abstract | supports | Actual mixed environmental/pathogen perspective identity and abstract scope only. Detailed defense, fitness, AMR and intervention efficacy remain unassessed. |
| meta-canonical | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/canonical-metadata.json; Actual current indexed metadata/abstract | supports | Actual benign marine species abstract reports NTOU-MSR1T growth range pH 7–10 versus optimum 7–8. Related Preprint in notice is not a correction; no full-body or assay validation claimed. |
| body-krulwich | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml; Retained BioC selected generic passages; locators in reading receipt | supports | Generic external/internal pH and PMF context plus literal alkaliphiles occurrence. Original acquisition is 07:57:33; current copying and reading are separate. Incidental pathogen/intervention detail is unassessed. |
| sources | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/source-assessment.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Four works, fourteen external placements, two ontology fields and complete node/edge coverage. |
| source-ledger | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/source-ledger.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Every assigned identity and actual available primary surface. |
| placements | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/placement-ledger.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | All citation placements and the bounded Baker attribution candidate. |
| snippets | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/snippet-ledger.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | All six excerpts are literal: five indexed-abstract matches plus retained BioC alkaliphiles. |
| node-sources | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/node-source-ledger.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Every node and incident source placement accounted for. |
| edge-sources | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/edge-source-ledger.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Generic context distinguished from unassessed detailed biological efficacy. |
| source-status | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/publication-status-ledger.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Bounded indexed notice fields; no exhaustive publication-status absence assertion. |
| source-reading | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/selected-primary-reading.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Actual selected generic passages and literal matching scope; no whole-body claim. |
| source-access | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/access-limitations.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Baker body unavailable; current snippets still exact in its abstract. |
| source-reuse | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/reuse-and-copy-receipt.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Original primary acquisition, metadata and current copy times remain separate. |
| canonical-source | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/canonical-assessment.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Full interval distinct from optimum, with species and type aliases positive. |
| native-checks | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/native-check-context.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Root-owned direct passes and unchanged native snippet outcomes. |
| source-manifest | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/evidence-manifest.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Twenty-six frozen source artifacts verified. |
| root-reading-46 | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-root/primary-generic-physicochemical-reading.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Only the actual bounded reading and chronology stated here, not inferred whole-body or detailed efficacy assessment. |
| root-reading-47 | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-root/primary-identity-formal-reading.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Only the actual bounded reading and chronology stated here, not inferred whole-body or detailed efficacy assessment. |
| root-reading-48 | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-root/primary-local-authority-reading.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Only the actual bounded reading and chronology stated here, not inferred whole-body or detailed efficacy assessment. |
| root-reading-49 | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-root/root-metadata-reading.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Only the actual bounded reading and chronology stated here, not inferred whole-body or detailed efficacy assessment. |
| root-reading-50 | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-root/whole-target-preinspect-reading.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Only the actual bounded reading and chronology stated here, not inferred whole-body or detailed efficacy assessment. |
| challenge | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-semantic-challenge-agent/semantic-severity-challenge.json; Final independent challenge | supports | Final recommendation and all bindings verified before serialization. |
| adjudication | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-root-adjudication.json; Final root disposition | supports | Root adjudication controls the final findings and qualifications. |

## Limits And Additional Notes

- Detailed pathogen acid-defense, fitness, AMR, antiporter/decarboxylation efficacy and intervention or perturbation effects remain UNASSESSED_SCOPE. No repaired mechanism or optimized condition is provided.
- Baker full text remains unavailable. The current impermeable-membrane phrase is nevertheless exact in the assigned abstract; the attribution concern does not establish false biology or whole-paper absence.
- Generic PMF context and its standard-condition approximation do not independently calibrate exact numerical growth endpoints or demonstrate universal biological sufficiency.
- Local defines and manifests-as proposals use broad formal endpoints. Their feature/state-to-trait wording differs from a hard imported material/process constraint.
- Capacity wording at nodes 2/3 can abbreviate maintenance processes; no automatic CAPACITY retype or separate defect is imposed. Free-text edges do not inherit unasserted RO constraints.
- The current record, mapping and shared writer are affected owners. A sibling writer, positive canonical owner and unrelated facet-maintenance context are not direct recurrence owners for the current gradient nodes.
- The target raw METPO term has no textual definition; current wording is a supported synthesis. Both direct parents and two explicit replacement links are positive.
- Official species/type aliases and current abstract support NTOU-MSR1T pH range 7–10, distinct from optimum 7–8. No full methods or all-strains generalization is claimed.
- Krulwich BioC original acquisition at 07:57:33, taxonomy success at 16:43:16 and earlier DNS failure remain distinct from current metadata at 19:34:30, copying and selected reading. No source network was repeated by this auditor.
- Catalog absence is bounded to the retained snapshot, and local acceptance search does not establish absence of private or remote decisions. Known human concept authorship remains positive.
- Final root adjudication and independent challenge are pinned. Root owns one execution after independent static review, followed by native validation, final artifact review and save.
- Coverage: 4 works, 14 external placements, 2 ontology fields, 11 nodes, 10 edges, 1 component, 0 protein classes/instances, 6 literal snippets, 1 canonical and 12 events (11 AI plus seed).
- Preparation changes no scientific record, Git state, sweep state or native review inventory.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T194540Z-ph-range
kind: record
repository: CultureBotAI/TraitMech
title: Whole-record review of pH range
started_at: '2026-10-21T19:34:40.820444Z'
finished_at: '2026-10-21T19:45:40Z'
reviewer:
  identity: codex
  kind: agent
  independence: independent
  independence_basis: Separate source and grounding audits, independent semantic challenge
    and bounded root primary readings. Generic environmental context, exact quotations,
    identity and formal roles are assessed. Detailed pathogen acid-defense, fitness,
    AMR and intervention efficacy are UNASSESSED_SCOPE. No scientific input was edited.
  model: GPT-6 (Codex)
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: One linked interval/gradient representation and imported-role major, one
  bounded Baker attribution minor and one human-acceptance minor. Canonical range,
  all six quotations and generic source context remain supported.
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
  - path: data/traits/environment/growth_range_phenotype_with_numerical_limits.yaml
    sha256: ad223791fa379c8f7302c8334153dbbd157fbf9a015a902a6ebb92f5513bfd9b
    role: context
  - path: data/traits/environment/ph_phenotype_with_numerical_limits.yaml
    sha256: 643abb9898dc920fe3aeeb0fa337c1d3a7efa6f0b540cb4ad979a3a28e0702d4
    role: context
  - path: data/traits/environment/ph_range.yaml
    sha256: 8a9cac2ea39eaf0aaafb950fce9b8119713bbef55c43e84550f22c3ee9d13d1a
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
  - path: history/infrastructure/disposition-typing-burndown/2026-08-08T014114Z-claude-code-5d4383.yaml
    sha256: 8fecb441b9374b0a0f69f131afce56f86ff69c212c52f45967c2e05ccb8ee98a
    role: context
  - path: history/infrastructure/inconsistent-node-type/2026-08-12T000912Z-claude-code-779670.yaml
    sha256: adb240d907348b52784c5e2f2e4b131af124877eeaaf1805c94713342763e5dd
    role: context
  - path: history/infrastructure/pathway-vs-process/2026-08-16T010630Z-claude-code-192557.yaml
    sha256: a45fff0e3ef24effb20c3b624dc14a6cab08f2094bc0f8033cd709c0cd60f012
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
  - path: history/records/ph_range_mid2/2026-09-04T024000Z-codex-3036b8.yaml
    sha256: 5ac1f0e4fed3207531b7a5db26c67ff29e3e2a5c06ec1127107311d9e194f6a2
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
  - path: proposals/metpo_traitmech_v4/metpo_proposal_properties_robot.tsv
    sha256: 55a96748c50b60ba0622170ef0eb09833f6d1e59431a4ab32b6fcb079103c0b7
    role: context
  - path: proposals/metpo_traitmech_v4/proposal.md
    sha256: c35d12fec87a3efdcfa320125446320315fca17bdb9228dd2b98ed00fe991bd8
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
  - path: research/traits/environment/ph_range-deep-research-falcon.md
    sha256: 0d3610a41b925db710c92320b754237bed4f8c435f3b0608d3198c3fdd9e21dc
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/add_ph_tropism_trait.py
    sha256: c52e1e735c802fa085194af0e2ca15761dfe52c8e5355ffdda0680ea4ea373a9
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
  - path: scripts/build_embedding_index.py
    sha256: d5ebf6612a04a67d74b2a245014a3624253d25f8d2b810e0b0ce528b7c851cd7
    role: context
  - path: scripts/connect_ph_delta_mid2_graph_183.py
    sha256: 21e16ff508b7448d6a60bf0729585a2fa1879ce9ac98562de4652689aec75d91
    role: context
  - path: scripts/connect_ph_delta_very_low_graph_183.py
    sha256: 5abcdea4fbf7793bc718406439e63203726284d2c2d3222b4bdd00d3de2b6390
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
  - path: scripts/repair_pr664_adversarial_review.py
    sha256: 5717a89bee383aa0e12aec9bf30434ccff74efcbe64684d13ef9b290b1accf96
    role: context
  - path: scripts/review_ph_delta_mid2_graph_183.py
    sha256: a7fcd17ebe8668b31f47c78b655ba908ffd537c3422f9bb2fd1cf3a66145b6c6
    role: context
  - path: scripts/review_ph_delta_mid3_graph_183.py
    sha256: 47d0d2b09f3acce565d9779443d8a5ee6784989ae34c23c6f0875f74ad4a1532
    role: context
  - path: scripts/review_ph_delta_very_low_graph_183.py
    sha256: 3fb1c239de9fb1bf91a5a97696053c7d652a619dc824ce160dd1063b44aad499
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
- target_id: METPO:1000332
  path: data/traits/environment/ph_range.yaml
  label: pH range
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_range.yaml
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
  selection: Third record of the actual batch 011 queue. Entire target and successful
    77-input capture precede substantive judgments. Current metadata was acquired
    before capture and interpreted afterward. Frozen source/grounding audits, independent
    challenge and final root adjudication govern this review.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - METPO:1000332
checks:
- check_id: audit-graphs
  name: Full-corpus graph audit
  status: passed
  required: true
  target_ids:
  - METPO:1000332
  command: just audit-graphs --out /private/tmp/traitmech-record-sweep.FU79Gr/causal_graph_audit.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  evidence_ids:
  - check-audit-graphs
  scope_note: 'Original common diagnostics ran at f25; history validation ran in batch
    003 at the 8eee base. Actual B10 final QC and the documented seven-file delta
    are qualified against B11 bytes, with an independent postcheck. These are reused
    executions; original failures, retries and skips remain explicit. Qualification:
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-b10-qc-supplement-qualified.json'
- check_id: audit-snippets
  name: Full-corpus snippet audit
  status: passed
  required: true
  target_ids:
  - METPO:1000332
  command: just audit-snippets --report /private/tmp/traitmech-record-sweep.FU79Gr/evidence_snippet_audit.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  evidence_ids:
  - check-audit-snippets
  scope_note: 'Original common diagnostics ran at f25; history validation ran in batch
    003 at the 8eee base. Actual B10 final QC and the documented seven-file delta
    are qualified against B11 bytes, with an independent postcheck. These are reused
    executions; original failures, retries and skips remain explicit. Qualification:
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-b10-qc-supplement-qualified.json'
- check_id: check-pathway-links
  name: Full-corpus pathway links
  status: passed
  required: true
  target_ids:
  - METPO:1000332
  command: just check-pathway-links
  exit_code: 0
  expected_exit_code: 0
  summary: 19 links checked against the pinned PathwayMech snapshot.
  evidence_ids:
  - check-check-pathway-links
  scope_note: 'Original common diagnostics ran at f25; history validation ran in batch
    003 at the 8eee base. Actual B10 final QC and the documented seven-file delta
    are qualified against B11 bytes, with an independent postcheck. These are reused
    executions; original failures, retries and skips remain explicit. Qualification:
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-b10-qc-supplement-qualified.json'
- check_id: validate-history
  name: Full-corpus history integrity
  status: passed
  required: true
  target_ids:
  - METPO:1000332
  command: just validate-history
  exit_code: 0
  expected_exit_code: 0
  summary: 1277 history records checked, zero invalid links at the 8eee source base;
    integrity does not establish science or human acceptance.
  evidence_ids:
  - check-validate-history
  scope_note: 'Original common diagnostics ran at f25; history validation ran in batch
    003 at the 8eee base. Actual B10 final QC and the documented seven-file delta
    are qualified against B11 bytes, with an independent postcheck. These are reused
    executions; original failures, retries and skips remain explicit. Qualification:
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-b10-qc-supplement-qualified.json'
- check_id: validate-products
  name: Initial full-product validation
  status: failed
  required: false
  target_ids:
  - METPO:1000332
  command: just validate-products
  exit_code: 2
  expected_exit_code: 0
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  evidence_ids:
  - check-validate-products
  scope_note: 'Original common diagnostics ran at f25; history validation ran in batch
    003 at the 8eee base. Actual B10 final QC and the documented seven-file delta
    are qualified against B11 bytes, with an independent postcheck. These are reused
    executions; original failures, retries and skips remain explicit. Qualification:
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-b10-qc-supplement-qualified.json'
- check_id: validate-products-retry-local
  name: Product validation with isolated local cache
  status: failed
  required: false
  target_ids:
  - METPO:1000332
  command: just validate-products
  exit_code: 2
  expected_exit_code: 0
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  evidence_ids:
  - check-validate-products-retry-local
  scope_note: 'Original common diagnostics ran at f25; history validation ran in batch
    003 at the 8eee base. Actual B10 final QC and the documented seven-file delta
    are qualified against B11 bytes, with an independent postcheck. These are reused
    executions; original failures, retries and skips remain explicit. Qualification:
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-b10-qc-supplement-qualified.json'
- check_id: validate-products-retry-network
  name: Product validation after isolated-cache download
  status: passed
  required: true
  target_ids:
  - METPO:1000332
  command: just validate-products
  exit_code: 0
  expected_exit_code: 0
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  evidence_ids:
  - check-validate-products-retry-network
  scope_note: 'Original common diagnostics ran at f25; history validation ran in batch
    003 at the 8eee base. Actual B10 final QC and the documented seven-file delta
    are qualified against B11 bytes, with an independent postcheck. These are reused
    executions; original failures, retries and skips remain explicit. Qualification:
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-b10-qc-supplement-qualified.json'
- check_id: ph-range-native
  name: Focused native validation
  status: passed
  required: true
  target_ids:
  - METPO:1000332
  command: just validate data/traits/environment/ph_range.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Direct successful current-target schema validation; formal roles are assessed
    separately.
  evidence_ids:
  - check-ph-range-native
- check_id: ph-range-strict
  name: Focused strict validation
  status: passed
  required: true
  target_ids:
  - METPO:1000332
  command: just validate-strict data/traits/environment/ph_range.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Direct successful current-target strict validation; no biological efficacy
    certification.
  evidence_ids:
  - check-ph-range-strict
- check_id: ph-range-snippets
  name: Focused snippet verification
  status: passed
  required: true
  target_ids:
  - METPO:1000332
  command: just verify-snippets --record data/traits/environment/ph_range.yaml --out
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-snippets.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 'Six fields over two references: five VERIFIED and one NOT_IN_ABSTRACT.
    Independent retained primary text verifies all six literal occurrences without
    changing the native result.'
  evidence_ids:
  - check-ph-range-snippets
- check_id: batch010-qc
  name: Reused maintained batch-ten QC
  status: passed
  required: true
  target_ids:
  - METPO:1000332
  command: just qc
  exit_code: 0
  expected_exit_code: 0
  summary: Actual B10 final QC at its original time, qualified against B11 bytes;
    not a fresh B11 execution.
  evidence_ids:
  - check-batch010-qc
- check_id: uniprot-applicability
  name: Protein-instance metadata applicability
  status: not_applicable
  required: false
  target_ids:
  - METPO:1000332
  summary: Zero protein-class nodes and zero instances; explicit antiport activity
    is not a token protein class.
  evidence_ids:
  - record
  - policy
  - node-edges
evidence:
- evidence_id: check-audit-graphs
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-graphs.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:29Z; metadata audit-graphs.json
  accessed_at: '2026-10-19T07:33:29Z'
  support: context_only
  summary: 74 baselined findings, zero new/blocking findings; connectivity report
    covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific
    verification of this target.
  snapshot_sha256: ecce27e6a8f8b8b1fc54a9a0564a27626ee33774da508665859c6d1429337f4d
- evidence_id: check-audit-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/audit-snippets.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:33Z; metadata audit-snippets.json
  accessed_at: '2026-10-19T07:33:33Z'
  support: context_only
  summary: 2419 baselined findings, zero new/blocking findings. Focused source checks
    and manual evidence review are recorded separately.
  snapshot_sha256: beafaa5c82645f5cf216142b6e0369d556202bcc72fdabbf35825fce955fd59f
- evidence_id: check-check-pathway-links
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/check-pathway-links.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:33:28Z; metadata check-pathway-links.json
  accessed_at: '2026-10-19T07:33:28Z'
  support: context_only
  summary: 19 links checked against the pinned PathwayMech snapshot.
  snapshot_sha256: e77729b8afd6ae02cd834e516c48dd5c72d10498802e7a1b0004eebb4831f6a0
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-003.4opxlhgf/validate-history.log
  locator: Executed 2026-10-21T07:03:25Z through 2026-10-21T07:03:30Z; metadata validate-history.json
  accessed_at: '2026-10-21T07:03:30Z'
  support: context_only
  summary: 1277 history records checked, zero invalid links at the 8eee source base;
    integrity does not establish science or human acceptance.
  snapshot_sha256: 02f94872992b2fbc3cc455c552d56a338dd449a315e02b1bf0226b68a8d2cfe3
- evidence_id: check-validate-products
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products.log
  locator: Executed 2026-10-19T07:33:16Z through 2026-10-19T07:34:01Z; metadata validate-products.json
  accessed_at: '2026-10-19T07:34:01Z'
  support: context_only
  summary: Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips.
    Superseded by successful network retry.
  snapshot_sha256: 697efcbe603c9a5e27f9726e688d1b9d9f621fa548f585d9005b5157d81dadae
- evidence_id: check-validate-products-retry-local
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-local.log
  locator: Executed 2026-10-19T07:34:53Z through 2026-10-19T07:35:24Z; metadata validate-products-retry-local.json
  accessed_at: '2026-10-19T07:35:24Z'
  support: context_only
  summary: Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful
    network retry.
  snapshot_sha256: b636ab6978cf8b8d4cc2cc4033f1cdca399cca46dc615a26073cfe680d44ebb5
- evidence_id: check-validate-products-retry-network
  kind: validation
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/validate-products-retry-network.log
  locator: Executed 2026-10-19T07:35:34Z through 2026-10-19T07:36:03Z; metadata validate-products-retry-network.json
  accessed_at: '2026-10-19T07:36:03Z'
  support: context_only
  summary: 'Passed: 361 canonical matches, two synonym matches, one exception, 123
    SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered.'
  snapshot_sha256: 67e91252adce1d441ad6b37d6904f0cbcea703575aec8011e65e94822fa810ea
- evidence_id: check-ph-range-native
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-native.log
  locator: Executed 2026-10-21T19:34:55.779565+00:00 through 2026-10-21T19:34:56.724090+00:00;
    metadata ph-range-native.json
  accessed_at: '2026-10-21T19:34:56.724090Z'
  support: context_only
  summary: Direct successful current-target schema validation; formal roles are assessed
    separately.
  snapshot_sha256: f4a0c006e62d3125362e9f82f5128454326c97bc3aa2dba54bc138158e7fe224
- evidence_id: check-ph-range-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-strict.log
  locator: Executed 2026-10-21T19:34:55.782628+00:00 through 2026-10-21T19:34:57.432414+00:00;
    metadata ph-range-strict.json
  accessed_at: '2026-10-21T19:34:57.432414Z'
  support: context_only
  summary: Direct successful current-target strict validation; no biological efficacy
    certification.
  snapshot_sha256: 50f17ff0f831606529fbbc7cd3419f47003f0152efae4c82f1f397054acca79e
- evidence_id: check-ph-range-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-snippets.log
  locator: Executed 2026-10-21T19:34:59.658831+00:00 through 2026-10-21T19:35:03.592067+00:00;
    metadata ph-range-snippets.json
  accessed_at: '2026-10-21T19:35:03.592067Z'
  support: context_only
  summary: 'Six fields over two references: five VERIFIED and one NOT_IN_ABSTRACT.
    Independent retained primary text verifies all six literal occurrences without
    changing the native result.'
  snapshot_sha256: d8a05eecd3e0eb33c9609837a1d9fa1b8009bf192a262c0d8e55df3dcfa9e395
- evidence_id: check-batch010-qc
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-010.m7q2v9cx/batch010-qc.log
  locator: Executed 2026-10-21T19:06:27.731868+00:00 through 2026-10-21T19:08:11.219124+00:00;
    metadata batch010-qc.json
  accessed_at: '2026-10-21T19:08:11.219124Z'
  support: context_only
  summary: Actual B10 final QC at its original time, qualified against B11 bytes;
    not a fresh B11 execution.
  snapshot_sha256: a97d2cc68e7db1ebd1a0edd19a7b0d03a4b1f45b55f8c6e6c2c48252f1705201
- evidence_id: record
  kind: record_content
  reference: data/traits/environment/ph_range.yaml
  locator: Entire current record
  accessed_at: '2026-10-21T19:34:41.621641Z'
  support: supports
  summary: All eleven nodes, ten edges, one canonical, six snippet fields and twelve
    record events are covered.
  snapshot_sha256: 8a9cac2ea39eaf0aaafb950fce9b8119713bbef55c43e84550f22c3ee9d13d1a
- evidence_id: policy
  kind: authority
  reference: docs/GROUNDING_POLICY.md
  locator: Captured maintained authority
  accessed_at: '2026-10-21T19:38:01.756393Z'
  support: supports
  summary: Native referents and optional protein evidence; no token class or accession
    requirement.
  snapshot_sha256: 891678c983c2283a47c81c47950b35753981e9339d105f3bbdda92a1f5ab7f42
- evidence_id: playbook
  kind: authority
  reference: docs/CURATION_PLAYBOOK.md
  locator: Captured maintained authority
  accessed_at: '2026-10-21T19:38:01.756393Z'
  support: supports
  summary: Source scope and exact quotation; known concept creator is distinct from
    later human graph acceptance.
  snapshot_sha256: 735e9b810471da9f7d8364e35ffe1e741edb3421480dac01727db6ea5aa65da9
- evidence_id: schema
  kind: authority
  reference: src/traitmech/schema/traitmech.yaml
  locator: Captured maintained authority
  accessed_at: '2026-10-21T19:38:01.756393Z'
  support: supports
  summary: Actual process, state, chemical, quality and activity facets.
  snapshot_sha256: 46c47fc627b80ccbba1e8ab3fb6f2aee93bc2aef7aaf72fe9aadc3257f2c02dd
- evidence_id: checklist
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Captured maintained authority
  accessed_at: '2026-10-21T19:38:01.756393Z'
  support: supports
  summary: Whole-record identity, evidence, hierarchy, graph, provenance, owners and
    readiness coverage.
  snapshot_sha256: da8896328a0fd6cc92f1adf0d8be8980d0ddd41f3172c7936f2c7f119b293ac1
- evidence_id: reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-b10-qc-supplement-qualified.json
  locator: Actual B10-to-B11 qualification
  accessed_at: '2026-10-21T19:08:29.388400Z'
  support: supports
  summary: All trait/history/common comparisons and retained diagnostics are bound.
  snapshot_sha256: a728777b9987b1283d7d1382168af40739074fce5c05f9a3bd93d3738f56880f
- evidence_id: reuse-postcheck
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-output-verification-agent/post-execution-verification.json
  locator: Independent qualification postcheck
  accessed_at: '2026-10-21T19:08:41.804361Z'
  support: supports
  summary: Actual byte and output bindings verified without repeating QC.
  snapshot_sha256: a3a6f33363e71b00e8db09cbc318cae0027844aba584f7b4cafb282d11ab027a
- evidence_id: capture
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-grounding-agent/capture-verification.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:34:58.840016Z'
  support: supports
  summary: Successful 77-input capture independently rehashed.
  snapshot_sha256: 62025c4ac81fa4dfddca00fb9948e5ec0731e0d7369ac239325681ad47a24446
- evidence_id: identity
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-grounding-agent/identity-assessment.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:38:01.751400Z'
  support: supports
  summary: Active identity, both parents, two explicit obsolete replacements, known
    human creator and official source identities.
  snapshot_sha256: 2c01d4ae10d2506cee22bd96b1f88e628ad58c76b81149338a14f17cb7d7048f
- evidence_id: node-edges
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-grounding-agent/node-edge-ledger.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:38:01.752877Z'
  support: supports
  summary: All current nodes and edges, with one linked interval/gradient/imported-role
    representation group.
  snapshot_sha256: 96e58e910c1693e8e4ce8863d9936f950d30aa90a1c9d38ea1fcf1cec81789a3
- evidence_id: owners
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-grounding-agent/owner-provenance-assessment.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:38:01.753184Z'
  support: supports
  summary: Exact current owners and contextual writers distinguished; bounded human
    acceptance search.
  snapshot_sha256: c3085c2f5cbf5329d465f74148f7f6faeaa541b72fe14540da6a03f909819659
- evidence_id: expression
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-grounding-agent/expression-applicability.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:38:01.754511Z'
  support: supports
  summary: Actual retained catalog checked against official genus/species and strain
    aliases.
  snapshot_sha256: 0367ce1d95064dec51dc147fb637fc7d0be678c20d37cd4a9b2bbd673cb03457
- evidence_id: authority-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-grounding-agent/authority-reuse-receipts.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:35:34.669072Z'
  support: supports
  summary: Original catalog and runner times remain distinct from copying.
  snapshot_sha256: 99da6e94f5769c9ad5bd2d16565a49363d5552f77565d17b781c61bb5482ca14
- evidence_id: identity-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-grounding-agent/primary-identity-reuse.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:35:56.845320Z'
  support: supports
  summary: Official taxon and GO original acquisitions, copies and earlier taxon failure
    retained.
  snapshot_sha256: 330ce3925a4b28960a3e6dee95f1a12446692a3f78390514a644ef4168acba41
- evidence_id: local-authority
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-grounding-agent/local-authority-excerpts.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:35:34.616859Z'
  support: supports
  summary: Broad local formal endpoints are distinguished from describes-feature/state-to-trait
    semantics.
  snapshot_sha256: 54645cda3706a773768d331727b859ba3c1cafdd9f4434a8f6771e3459ca33a7
- evidence_id: ground-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-grounding-agent/primary-reading-scope.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:38:01.755079Z'
  support: supports
  summary: Actual authority/history reading scope.
  snapshot_sha256: d3c7b68f96a99e83ffdc8a1a17992c898a85571a1a1433281dee2adca9b2115a
- evidence_id: ground-manifest
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-grounding-agent/evidence-manifest.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:38:01.761976Z'
  support: supports
  summary: All twenty-seven frozen grounding artifacts verified.
  snapshot_sha256: d7c1243142056c21ae580d538b4da7497c1101694706ce38fcf9055ffdbc72a2
- evidence_id: metpo-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/repo/data/raw/metpo.owl
  locator: Actual target, parent and obsolete-term XML
  accessed_at: '2026-10-21T19:35:33.918759Z'
  support: supports
  summary: Both parents and two explicit replacement links are positive. The target
    has no textual raw definition; the current definition is assessed as a synthesis.
    Luke Wang concept authorship is retained.
  snapshot_sha256: 8b6f8fe0510a698579e532658c8ace05da2550093365df9ca83feb0741778415
- evidence_id: ro-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/ro.db
  locator: RO:0002326 → 2216 → 2500 → 2595; RO:0002327 inheritance
  accessed_at: '2026-10-21T19:35:33.927575Z'
  support: supports
  summary: Contributes-to and enables inherit material-subject/process-object roles.
    Current gradient and homeostasis-process subjects are assessed by their actual
    referents, not rescued by enum labels.
  snapshot_sha256: 849e616c29fecd0d4a6c6dee0dc0f6f117ace7167dbfa1e0f043dc84868f83cb
- evidence_id: taxonomy-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-grounding-agent/taxon3028314.xml
  locator: Official NCBITaxon:3028314 response
  accessed_at: '2026-10-21T16:43:16.762138Z'
  support: supports
  summary: Oceanimonas pelagia species and NTOU-MSR1/BCRC 81403/JCM 36023 type aliases
    agree. Phenotype support comes separately from the cited abstract.
  snapshot_sha256: 17213af06e1b89f10c93a152bc8cfe6553b0ada3d5bb9a3d8a4c578b5f379a10
- evidence_id: go-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-grounding-agent/go0051453.response
  locator: Actual official GO:0051453 response
  accessed_at: '2026-10-21T15:29:38.343180Z'
  support: supports
  summary: Active regulation of intracellular pH is compatible with the maintained
    closeMatch to the homeostasis process; no material protein identity is inferred.
  snapshot_sha256: 52154295e213fc1d16dbb9ff32ab66f5ac905e481f64f5719101bf4fbeba6abe
- evidence_id: meta-krulwich
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-metadata.json
  locator: Actual current indexed metadata/abstract
  accessed_at: '2026-10-21T19:34:30.782245Z'
  support: supports
  summary: Actual assigned indexed identity, abstract and returned notice fields only;
    body evidence is separate.
  snapshot_sha256: 484784a62fbb4c9d74a1feab4df2fdfdf37d4dd0ce3fa79f714c86a07d86d29c
- evidence_id: meta-baker
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/baker-metadata.json
  locator: Actual current indexed metadata/abstract
  accessed_at: '2026-10-21T19:34:30.766603Z'
  support: supports
  summary: Actual acidophile abstract contains the exact impermeable-membrane phrase
    and low-pH context. Its full body remains unavailable; broader alkaline attribution
    is assessed with that limit.
  snapshot_sha256: a78777bc3bb6444b32e2e8a13ab72c56d80592b97e30c9b5520c67cc040c631b
- evidence_id: meta-acid-review
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/acid-review-metadata.json
  locator: Actual current indexed metadata/abstract
  accessed_at: '2026-10-21T19:34:30.787816Z'
  support: supports
  summary: Actual mixed environmental/pathogen perspective identity and abstract scope
    only. Detailed defense, fitness, AMR and intervention efficacy remain unassessed.
  snapshot_sha256: 73336b6a7880310eec04215abd0bb966f635477603426f833b8106dc16d02774
- evidence_id: meta-canonical
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/canonical-metadata.json
  locator: Actual current indexed metadata/abstract
  accessed_at: '2026-10-21T19:34:30.779057Z'
  support: supports
  summary: Actual benign marine species abstract reports NTOU-MSR1T growth range pH
    7–10 versus optimum 7–8. Related Preprint in notice is not a correction; no full-body
    or assay validation claimed.
  snapshot_sha256: 73ea00102769ce9782573737fb2b62eb6d86b441a248b0a55c045bb6a3c64a9e
- evidence_id: body-krulwich
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml
  locator: Retained BioC selected generic passages; locators in reading receipt
  accessed_at: '2026-10-21T07:57:33Z'
  support: supports
  summary: Generic external/internal pH and PMF context plus literal alkaliphiles
    occurrence. Original acquisition is 07:57:33; current copying and reading are
    separate. Incidental pathogen/intervention detail is unassessed.
  snapshot_sha256: 903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f
- evidence_id: sources
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/source-assessment.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:38:03.332802Z'
  support: supports
  summary: Four works, fourteen external placements, two ontology fields and complete
    node/edge coverage.
  snapshot_sha256: c2b5e998f6c232e844f30af93a0062b80fdf51ec24728698a79f087a1086ec1d
- evidence_id: source-ledger
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/source-ledger.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:38:03.316011Z'
  support: supports
  summary: Every assigned identity and actual available primary surface.
  snapshot_sha256: e884650f1a488a40d36ea9b9f6c4dd3ea09eff6ae603fd8ff9d2b1c836acc3ae
- evidence_id: placements
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/placement-ledger.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:38:03.316462Z'
  support: supports
  summary: All citation placements and the bounded Baker attribution candidate.
  snapshot_sha256: 275a2a8055228b1288a9851e7b9eb45855e190ccd12c1c1a2402087aea8a0b4d
- evidence_id: snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/snippet-ledger.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:38:03.330169Z'
  support: supports
  summary: 'All six excerpts are literal: five indexed-abstract matches plus retained
    BioC alkaliphiles.'
  snapshot_sha256: 4f64cf7c293ec07ebdf3b150a443c866402197cf63b8a3a26393219c45c61316
- evidence_id: node-sources
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/node-source-ledger.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:38:03.317040Z'
  support: supports
  summary: Every node and incident source placement accounted for.
  snapshot_sha256: b736508869f25c4598fc1eb171c93bf5d24e99d0fa8f1e3a94b670bc6cc0225c
- evidence_id: edge-sources
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/edge-source-ledger.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:38:03.316677Z'
  support: supports
  summary: Generic context distinguished from unassessed detailed biological efficacy.
  snapshot_sha256: 5820ffcbc008c31cee68875136c7104ab14937e9a379d6c358b418ef4160b9ab
- evidence_id: source-status
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/publication-status-ledger.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:38:03.316268Z'
  support: supports
  summary: Bounded indexed notice fields; no exhaustive publication-status absence
    assertion.
  snapshot_sha256: 73f6052b19a07f567553419e1f272b094997e99eae29b833aa100c6423da9b1e
- evidence_id: source-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/selected-primary-reading.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:38:03.331180Z'
  support: supports
  summary: Actual selected generic passages and literal matching scope; no whole-body
    claim.
  snapshot_sha256: 5927bfdf84190c00b88014b10c9d5029d0749ff03e725699aefe3ac8bc8a7ac0
- evidence_id: source-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/access-limitations.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:38:03.331335Z'
  support: supports
  summary: Baker body unavailable; current snippets still exact in its abstract.
  snapshot_sha256: aaf6c67ff0672aa142fec1ed4feeab705673b507c1990756c63c4ac4a5cf3c29
- evidence_id: source-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/reuse-and-copy-receipt.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:38:03.312412Z'
  support: supports
  summary: Original primary acquisition, metadata and current copy times remain separate.
  snapshot_sha256: 40ce9eedd5345f25def7cc7d09d915d6c810656ce632187da106d4f4cb4f3995
- evidence_id: canonical-source
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/canonical-assessment.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:38:03.330874Z'
  support: supports
  summary: Full interval distinct from optimum, with species and type aliases positive.
  snapshot_sha256: dc103c50c228dd92d4df03833f46e3faf8e92296b81a3fa2234d207dab279e5f
- evidence_id: native-checks
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/native-check-context.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:38:03.332479Z'
  support: supports
  summary: Root-owned direct passes and unchanged native snippet outcomes.
  snapshot_sha256: c2ba25d457e26c6cead96013efb3d3ca1e5ca27df1cae79a168414c217f28a3e
- evidence_id: source-manifest
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/evidence-manifest.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:38:03.349106Z'
  support: supports
  summary: Twenty-six frozen source artifacts verified.
  snapshot_sha256: 0d8bec782e4118e9a45b6c033edded958f752d53b5d67ed627c6f299f1872038
- evidence_id: root-reading-46
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-root/primary-generic-physicochemical-reading.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:38:48.688762Z'
  support: supports
  summary: Only the actual bounded reading and chronology stated here, not inferred
    whole-body or detailed efficacy assessment.
  snapshot_sha256: 9975672f221789e855e5378cd0bf9f48aaeda6e7fa9e6e5fdb9734a6b0eb2b5a
- evidence_id: root-reading-47
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-root/primary-identity-formal-reading.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:37:21.663770Z'
  support: supports
  summary: Only the actual bounded reading and chronology stated here, not inferred
    whole-body or detailed efficacy assessment.
  snapshot_sha256: 5743d5ebdd0ee5b0cdbb7c513f4edfbee0bcaa3fd46077efca35e52e7651863f
- evidence_id: root-reading-48
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-root/primary-local-authority-reading.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:35:38.201011Z'
  support: supports
  summary: Only the actual bounded reading and chronology stated here, not inferred
    whole-body or detailed efficacy assessment.
  snapshot_sha256: d71e6ce0579a5cf65b88fa0c121b5049a9c007206fc1ada7887b4a39561d6c1e
- evidence_id: root-reading-49
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-root/root-metadata-reading.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:36:00.153714Z'
  support: supports
  summary: Only the actual bounded reading and chronology stated here, not inferred
    whole-body or detailed efficacy assessment.
  snapshot_sha256: 9376702cbbeba224f7c3105429e46dfd77734a1edbb9df99d5e6f0991a3b8c2a
- evidence_id: root-reading-50
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-root/whole-target-preinspect-reading.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:34:30.067119Z'
  support: supports
  summary: Only the actual bounded reading and chronology stated here, not inferred
    whole-body or detailed efficacy assessment.
  snapshot_sha256: e9a4b962be1c64a572d9ec1a453f9c8ef09f0fb986572781286d61ff8c4bc337
- evidence_id: challenge
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-semantic-challenge-agent/semantic-severity-challenge.json
  locator: Final independent challenge
  accessed_at: '2026-10-21T19:42:43.658176Z'
  support: supports
  summary: Final recommendation and all bindings verified before serialization.
  snapshot_sha256: c2f2c533f1df140ebf8ffe18fb0302ce4dea6f57cac0d0a7a6b8ee6bbbbeceee
- evidence_id: adjudication
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-root-adjudication.json
  locator: Final root disposition
  accessed_at: '2026-10-21T19:43:50.067818Z'
  support: supports
  summary: Root adjudication controls the final findings and qualifications.
  snapshot_sha256: e76b51d91c7eab3e734b1012f55c3d259d38c84b083c3dc3903caea6b193b7dd
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: active identity, parents and replacements'
  outcome: supported
  target_ids:
  - METPO:1000332
  summary: Active METPO:1000332 and both direct parents agree. Two deprecated terms
    explicitly point to it. Luke Wang is positive concept authorship, separately from
    current graph acceptance. No supplied synonym equivalence requires repair.
  evidence_ids:
  - identity
  - metpo-primary
  - record
- assessment_id: definition
  area: evidence
  topic: 'Native checklist: minimum-to-maximum external growth pH'
  outcome: supported
  target_ids:
  - METPO:1000332
  summary: The definition is a synthesis consistent with the two measurement parents
    and generic external growth-pH source context. The target raw METPO class has
    no textual definition; it is not presented as an exact ontology quotation.
  evidence_ids:
  - identity
  - metpo-primary
  - sources
  - body-krulwich
- assessment_id: scope
  area: scope
  topic: 'Native checklist: quantitative environmental interval'
  outcome: supported
  target_ids:
  - METPO:1000332
  summary: ENVIRONMENT, CLASS and NONMECHANISTIC fit the measured interval. Contextual
    branches are not automatically universal or sufficient biological mechanisms.
    No invented optimum/range equivalence is asserted.
  evidence_ids:
  - record
  - policy
  - checklist
- assessment_id: canonical
  area: evidence
  topic: 'Native checklist: species-bound full interval'
  outcome: supported
  target_ids:
  - METPO:1000332
  summary: Actual assigned abstract supports NTOU-MSR1T growth range pH 7–10, distinct
    from optimum 7–8. Official species and type aliases match. Parent placement preserves
    the full interval, and no full methods or complete species-wide phenotype generalization
    is claimed.
  evidence_ids:
  - canonical-source
  - meta-canonical
  - taxonomy-primary
- assessment_id: bibliography
  area: evidence
  topic: 'Native checklist: all works and placement scope'
  outcome: concern
  target_ids:
  - METPO:1000332
  summary: All four assigned identities and fourteen external placements resolve.
    The Baker membrane phrase supports acidophile low-pH context, while evidence[1].notes
    broadens that attribution to alkaline extremes. This is bounded source-scope precision;
    inaccessible full text is not evidence of false biology or total source absence.
  evidence_ids:
  - sources
  - placements
  - source-status
  - meta-baker
  - source-access
  details: "{\n  \"completed_at\": \"2026-10-21T19:38:03.316462+00:00\",\n  \"external_placements\"\
    : [\n    {\n      \"field_path\": \"definition_source\",\n      \"reference\"\
    : \"DOI:10.1038/nrmicro2549\",\n      \"claim\": \"A pH phenotype with numerical\
    \ limits that bounds the minimum and maximum external pH supporting growth of\
    \ an organism.\",\n      \"assessment\": \"Generic growth-supporting external-pH\
    \ concept consistent with actual Krulwich abstract and generic BioC opening; no\
    \ imposed common endpoint or optimum/range equivalence.\"\n    },\n    {\n   \
    \   \"field_path\": \"evidence[0]\",\n      \"reference\": \"DOI:10.1038/nrmicro2549\"\
    ,\n      \"snippet\": \"pH homeostasis\",\n      \"notes\": \"pH-homeostasis review\
    \ supports the bounded external-pH span over which cytoplasmic pH homeostasis\
    \ sustains growth as the basis of the pH-range phenotype.\",\n      \"assessment\"\
    : \"Positive generic homeostasis context; literal short phrase does not independently\
    \ establish complete organism-specific endpoints.\"\n    },\n    {\n      \"field_path\"\
    : \"evidence[1]\",\n      \"reference\": \"DOI:10.1016/j.tim.2007.02.005\",\n\
    \      \"snippet\": \"highly impermeable cell membranes\",\n      \"notes\": \"\
    pH-homeostasis review supports envelope-based proton barriers as the mechanism\
    \ extending growth into acidic and alkaline extremes.\",\n      \"assessment\"\
    : \"Exact membrane phrase is positive for acidophiles. The notes broaden this\
    \ assigned acidophile attribution to alkaline extremes; bounded source-scope precision\
    \ candidate, without claiming the inaccessible full paper contains no alkaline\
    \ discussion.\"\n    },\n    {\n      \"field_path\": \"canonical_examples[0]\"\
    ,\n      \"reference\": \"DOI:10.1007/s10482-024-01948-y\",\n      \"claim\":\
    \ \"Oceanimonas pelagia NTOU-MSR1T grew at pH 7-10. The complete interval crosses\
    \ the mid2/mid3 split, so #591 places this distinct claim on the pH-range parent.\"\
    ,\n      \"assessment\": \"Assigned actual abstract explicitly reports NTOU-MSR1T\
    \ growth at pH 7.0\\u201310.0 and optimum 7.0\\u20138.0. Parent placement preserves\
    \ the full interval rather than changing it to the optimum or a single child bin.\"\
    \n    },\n    {\n      \"field_path\": \"causal_graphs[0].edges[0].evidence[0]\"\
    ,\n      \"reference\": \"DOI:10.1038/nrmicro2549\",\n      \"snippet\": \"external\
    \ pH\",\n      \"notes\": \"Supports external pH as the axis bounding the growth\
    \ window.\",\n      \"assessment\": \"Generic external-pH axis is directly supported\
    \ by the assigned abstract and BioC opening; exact measured boundaries remain\
    \ organism-specific.\"\n    },\n    {\n      \"field_path\": \"causal_graphs[0].edges[1].evidence[0]\"\
    ,\n      \"reference\": \"DOI:10.1016/j.tim.2007.02.005\",\n      \"snippet\"\
    : \"highly impermeable cell membranes\",\n      \"notes\": \"Supports envelope\
    \ proton barriers as the lower-bound mechanism for low-pH growth.\",\n      \"\
    assessment\": \"The exact assigned acidophile abstract supports low-pH membrane-barrier\
    \ context. This is generic lower-bound context, not a universal single necessary\
    \ or sufficient mechanism.\"\n    },\n    {\n      \"field_path\": \"causal_graphs[0].edges[2].evidence[0]\"\
    ,\n      \"reference\": \"DOI:10.1038/nrmicro2549\",\n      \"snippet\": \"alkaliphiles\"\
    ,\n      \"notes\": \"Supports alkaline-tolerance physiology as the upper-bound\
    \ mechanism for high-pH growth.\",\n      \"assessment\": \"Assigned Krulwich\
    \ text explicitly discusses alkaliphiles and growth at elevated external pH. Generic\
    \ upper-bound context is supported; no universal single strategy or exact numerical\
    \ cutoff is inferred.\"\n    },\n    {\n      \"field_path\": \"causal_graphs[0].edges[3].evidence[0]\"\
    ,\n      \"reference\": \"DOI:10.1038/nrmicro2549\",\n      \"snippet\": \"pH\
    \ homeostasis\",\n      \"notes\": \"Supports the trait endpoint.\",\n      \"\
    assessment\": \"Generic pH-homeostasis context is supported; the measurement/trait\
    \ relationship and local predicate semantics are assessed independently by grounding,\
    \ not proved by the two-word snippet.\"\n    },\n    {\n      \"field_path\":\
    \ \"causal_graphs[0].edges[4].evidence[0]\",\n      \"reference\": \"DOI:10.1038/nrmicro2549\"\
    ,\n      \"notes\": \"PMF architecture (\\u0394\\u03c8 \\u2212 59 \\u0394pH) determines\
    \ the range of pHout over which bacteria can tolerate or grow.\",\n      \"assessment\"\
    : \"BioC offsets 2440 and 3214 support the two-component PMF and approximation\
    \ under standard conditions. Offset 3940 supplies condition-specific illustrative\
    \ patterns. The current note is contextual; the approximation alone does not calibrate\
    \ a complete growth interval or prove biological sufficiency.\"\n    },\n    {\n\
    \      \"field_path\": \"causal_graphs[0].edges[5].evidence[0]\",\n      \"reference\"\
    : \"DOI:10.1038/nrmicro2549\",\n      \"notes\": \"Under strong pH stress the\
    \ orientation of a PMF component can reverse to maintain homeostasis.\",\n   \
    \   \"assessment\": \"BioC offset 3940 explicitly illustrates reversed PMF components\
    \ in distinct growth-pH contexts. Preserve source-specific illustrations and generic\
    \ context; this does not certify a universal compensation response.\"\n    },\n\
    \    {\n      \"field_path\": \"causal_graphs[0].edges[6].evidence[0]\",\n   \
    \   \"reference\": \"DOI:10.1038/nrmicro2549\",\n      \"notes\": \"Bacteria maintain\
    \ a distinct cytoplasmic pH required for protein function, bounding the phenotype.\"\
    ,\n      \"assessment\": \"Generic BioC opening links internal-pH compatibility\
    \ to protein function and distinguishes growth ranges from survival outside growth\
    \ ranges. Generic context is supported; formal enables roles are a separate question.\"\
    \n    },\n    {\n      \"field_path\": \"causal_graphs[0].edges[7].evidence[0]\"\
    ,\n      \"reference\": \"DOI:10.3389/fmicb.2020.556140\",\n      \"notes\": \"\
    Modification of membrane lipid composition to reduce proton permeability is a\
    \ general acid-stress mechanism.\",\n      \"assessment\": \"Assigned mixed-context\
    \ perspective identity and acid-response scope verified. Detailed lipid/acid-defense/fitness\
    \ efficacy is UNASSESSED_SCOPE; neither validated nor refuted from the abstract.\"\
    \n    },\n    {\n      \"field_path\": \"causal_graphs[0].edges[8].evidence[0]\"\
    ,\n      \"reference\": \"DOI:10.1038/nrmicro2549\",\n      \"notes\": \"Na+/H+\
    \ antiport is the principal strategy for cytoplasmic pH homeostasis at high external\
    \ pH.\",\n      \"assessment\": \"Assigned broad homeostasis review identity and\
    \ generic alkaline-homeostasis context verified. Detailed antiporter efficacy,\
    \ necessity and pathogen intervention biology are UNASSESSED_SCOPE; no replacement\
    \ mechanism or source transfer is supplied.\"\n    },\n    {\n      \"field_path\"\
    : \"causal_graphs[0].edges[9].evidence[0]\",\n      \"reference\": \"DOI:10.3389/fmicb.2020.556140\"\
    ,\n      \"notes\": \"Decarboxylation of glutamate or arginine is a recurring\
    \ proton-consuming acid-response module.\",\n      \"assessment\": \"Assigned\
    \ mixed-context perspective identity and acid-response scope verified. Detailed\
    \ decarboxylation/defense/fitness efficacy is UNASSESSED_SCOPE; no reaction optimization\
    \ or causal repair is provided.\"\n    }\n  ],\n  \"ontology_grounding_fields\"\
    : [\n    {\n      \"field_path\": \"causal_graphs[0].nodes[0].grounding\",\n \
    \     \"reference\": \"METPO:1000332\",\n      \"assessment\": \"Ontology identity\
    \ and role interpretation owned by the separate grounding audit.\"\n    },\n \
    \   {\n      \"field_path\": \"causal_graphs[0].nodes[7].grounding\",\n      \"\
    reference\": \"GO:0051453\",\n      \"assessment\": \"Ontology identity and role\
    \ interpretation owned by the separate grounding audit.\"\n    }\n  ],\n  \"counts\"\
    : {\n    \"external_placements\": 14,\n    \"ontology_grounding_fields\": 2\n\
    \  }\n}"
- assessment_id: snippets
  area: evidence
  topic: 'Native checklist: all six current excerpts'
  outcome: supported
  target_ids:
  - METPO:1000332
  summary: Six literal occurrences are verified. Both Baker impermeable-membrane phrases
    match its abstract; prior uncertainty about different Baker body phrases is not
    copied here. Alkaliphiles is confirmed in retained Krulwich BioC. Original native
    five VERIFIED/one NOT_IN_ABSTRACT remains unchanged.
  evidence_ids:
  - snippets
  - source-reading
  - native-checks
  details: "{\n  \"completed_at\": \"2026-10-21T19:38:03.330169+00:00\",\n  \"snippets\"\
    : [\n    {\n      \"field_path\": \"evidence[0].snippet\",\n      \"reference\"\
    : \"DOI:10.1038/nrmicro2549\",\n      \"snippet\": \"pH homeostasis\",\n     \
    \ \"outcome\": \"literal_exact\",\n      \"hits\": [\n        {\n          \"\
    surface\": \"indexed abstract\",\n          \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-metadata.json\"\
    ,\n          \"locator\": \"abstractText\",\n          \"sha256\": \"484784a62fbb4c9d74a1feab4df2fdfdf37d4dd0ce3fa79f714c86a07d86d29c\"\
    \n        },\n        {\n          \"surface\": \"retained BioC\",\n         \
    \ \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 58\",\n          \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    \n        },\n        {\n          \"surface\": \"retained BioC\",\n         \
    \ \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 671\",\n          \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    \n        },\n        {\n          \"surface\": \"retained BioC\",\n         \
    \ \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 2440\",\n          \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    \n        },\n        {\n          \"surface\": \"retained BioC\",\n         \
    \ \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 3309\",\n          \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    \n        },\n        {\n          \"surface\": \"retained BioC\",\n         \
    \ \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 3940\",\n          \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    \n        },\n        {\n          \"surface\": \"retained BioC\",\n         \
    \ \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 6577\",\n          \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    \n        },\n        {\n          \"surface\": \"retained BioC\",\n         \
    \ \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 9102\",\n          \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    \n        },\n        {\n          \"surface\": \"retained BioC\",\n         \
    \ \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 9746\",\n          \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    \n        },\n        {\n          \"surface\": \"retained BioC\",\n         \
    \ \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 9793\",\n          \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    \n        },\n        {\n          \"surface\": \"retained BioC\",\n         \
    \ \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 10376\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 12201\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 13430\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 13534\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 15086\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 15130\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 16479\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 17378\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 18903\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 19769\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 20611\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 26699\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 27057\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 27702\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 34345\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 36727\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 39253\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 40107\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 42119\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 44016\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 48281\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 49779\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 51883\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 52269\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 53261\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 59345\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 61189\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 61308\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 67006\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 67131\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        }\n\
    \      ],\n      \"scope\": \"Literal occurrence only; not validation of every\
    \ surrounding causal claim. Machine matching of retained passages does not imply\
    \ whole-body reading.\"\n    },\n    {\n      \"field_path\": \"evidence[1].snippet\"\
    ,\n      \"reference\": \"DOI:10.1016/j.tim.2007.02.005\",\n      \"snippet\"\
    : \"highly impermeable cell membranes\",\n      \"outcome\": \"literal_exact\"\
    ,\n      \"hits\": [\n        {\n          \"surface\": \"indexed abstract\",\n\
    \          \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/baker-metadata.json\"\
    ,\n          \"locator\": \"abstractText\",\n          \"sha256\": \"a78777bc3bb6444b32e2e8a13ab72c56d80592b97e30c9b5520c67cc040c631b\"\
    \n        }\n      ],\n      \"scope\": \"Literal occurrence only; not validation\
    \ of every surrounding causal claim. Machine matching of retained passages does\
    \ not imply whole-body reading.\"\n    },\n    {\n      \"field_path\": \"causal_graphs[0].edges[0].evidence[0].snippet\"\
    ,\n      \"reference\": \"DOI:10.1038/nrmicro2549\",\n      \"snippet\": \"external\
    \ pH\",\n      \"outcome\": \"literal_exact\",\n      \"hits\": [\n        {\n\
    \          \"surface\": \"indexed abstract\",\n          \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-metadata.json\"\
    ,\n          \"locator\": \"abstractText\",\n          \"sha256\": \"484784a62fbb4c9d74a1feab4df2fdfdf37d4dd0ce3fa79f714c86a07d86d29c\"\
    \n        },\n        {\n          \"surface\": \"retained BioC\",\n         \
    \ \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 58\",\n          \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    \n        },\n        {\n          \"surface\": \"retained BioC\",\n         \
    \ \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 671\",\n          \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    \n        },\n        {\n          \"surface\": \"retained BioC\",\n         \
    \ \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 3940\",\n          \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    \n        },\n        {\n          \"surface\": \"retained BioC\",\n         \
    \ \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 4950\",\n          \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    \n        },\n        {\n          \"surface\": \"retained BioC\",\n         \
    \ \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 6577\",\n          \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    \n        },\n        {\n          \"surface\": \"retained BioC\",\n         \
    \ \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 7370\",\n          \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    \n        },\n        {\n          \"surface\": \"retained BioC\",\n         \
    \ \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 17378\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 30207\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 39253\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 45441\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 45597\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 47480\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        }\n\
    \      ],\n      \"scope\": \"Literal occurrence only; not validation of every\
    \ surrounding causal claim. Machine matching of retained passages does not imply\
    \ whole-body reading.\"\n    },\n    {\n      \"field_path\": \"causal_graphs[0].edges[1].evidence[0].snippet\"\
    ,\n      \"reference\": \"DOI:10.1016/j.tim.2007.02.005\",\n      \"snippet\"\
    : \"highly impermeable cell membranes\",\n      \"outcome\": \"literal_exact\"\
    ,\n      \"hits\": [\n        {\n          \"surface\": \"indexed abstract\",\n\
    \          \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/baker-metadata.json\"\
    ,\n          \"locator\": \"abstractText\",\n          \"sha256\": \"a78777bc3bb6444b32e2e8a13ab72c56d80592b97e30c9b5520c67cc040c631b\"\
    \n        }\n      ],\n      \"scope\": \"Literal occurrence only; not validation\
    \ of every surrounding causal claim. Machine matching of retained passages does\
    \ not imply whole-body reading.\"\n    },\n    {\n      \"field_path\": \"causal_graphs[0].edges[2].evidence[0].snippet\"\
    ,\n      \"reference\": \"DOI:10.1038/nrmicro2549\",\n      \"snippet\": \"alkaliphiles\"\
    ,\n      \"outcome\": \"literal_exact\",\n      \"hits\": [\n        {\n     \
    \     \"surface\": \"retained BioC\",\n          \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 5466\",\n          \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    \n        },\n        {\n          \"surface\": \"retained BioC\",\n         \
    \ \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 15130\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 16479\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 39232\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 39253\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 41582\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 42119\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 45597\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 61656\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        }\n\
    \      ],\n      \"scope\": \"Literal occurrence only; not validation of every\
    \ surrounding causal claim. Machine matching of retained passages does not imply\
    \ whole-body reading.\"\n    },\n    {\n      \"field_path\": \"causal_graphs[0].edges[3].evidence[0].snippet\"\
    ,\n      \"reference\": \"DOI:10.1038/nrmicro2549\",\n      \"snippet\": \"pH\
    \ homeostasis\",\n      \"outcome\": \"literal_exact\",\n      \"hits\": [\n \
    \       {\n          \"surface\": \"indexed abstract\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-metadata.json\"\
    ,\n          \"locator\": \"abstractText\",\n          \"sha256\": \"484784a62fbb4c9d74a1feab4df2fdfdf37d4dd0ce3fa79f714c86a07d86d29c\"\
    \n        },\n        {\n          \"surface\": \"retained BioC\",\n         \
    \ \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 58\",\n          \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    \n        },\n        {\n          \"surface\": \"retained BioC\",\n         \
    \ \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 671\",\n          \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    \n        },\n        {\n          \"surface\": \"retained BioC\",\n         \
    \ \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 2440\",\n          \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    \n        },\n        {\n          \"surface\": \"retained BioC\",\n         \
    \ \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 3309\",\n          \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    \n        },\n        {\n          \"surface\": \"retained BioC\",\n         \
    \ \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 3940\",\n          \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    \n        },\n        {\n          \"surface\": \"retained BioC\",\n         \
    \ \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 6577\",\n          \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    \n        },\n        {\n          \"surface\": \"retained BioC\",\n         \
    \ \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 9102\",\n          \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    \n        },\n        {\n          \"surface\": \"retained BioC\",\n         \
    \ \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 9746\",\n          \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    \n        },\n        {\n          \"surface\": \"retained BioC\",\n         \
    \ \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 9793\",\n          \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    \n        },\n        {\n          \"surface\": \"retained BioC\",\n         \
    \ \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 10376\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 12201\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 13430\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 13534\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 15086\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 15130\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 16479\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 17378\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 18903\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 19769\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 20611\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 26699\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 27057\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 27702\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 34345\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 36727\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 39253\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 40107\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 42119\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 44016\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 48281\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 49779\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 51883\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 52269\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 53261\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 59345\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 61189\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 61308\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 67006\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        },\n\
    \        {\n          \"surface\": \"retained BioC\",\n          \"path\": \"\
    /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-source-agent/krulwich-bioc.xml\"\
    ,\n          \"locator\": \"passage offset 67131\",\n          \"sha256\": \"\
    903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\n        }\n\
    \      ],\n      \"scope\": \"Literal occurrence only; not validation of every\
    \ surrounding causal claim. Machine matching of retained passages does not imply\
    \ whole-body reading.\"\n    }\n  ],\n  \"counts\": {\n    \"fields\": 6,\n  \
    \  \"literal_exact\": 6,\n    \"unknown\": 0,\n    \"indexed_abstract_exact\"\
    : 5\n  },\n  \"native_result\": {\n    \"verified\": 5,\n    \"not_in_abstract\"\
    : 1\n  },\n  \"qualification\": \"The sixth occurrence, alkaliphiles, is confirmed\
    \ in retained primary BioC. Original native abstract-only results are unchanged.\
    \ Both Baker impermeable-membrane occurrences are exact in its abstract; prior\
    \ other Baker PMF/body uncertainty is not copied onto these different phrases.\"\
    \n}"
- assessment_id: nodes
  area: grounding
  topic: 'Native checklist: all eleven explicit referents'
  outcome: concern
  target_ids:
  - METPO:1000332
  summary: Numerical interval node 4 and nonmaterial gradient/potential nodes 5/6
    conflict with their declared process/chemical facets. Treat these once in the
    linked representation group. Capacity wording at nodes 2/3 is qualified shorthand,
    while explicit activity, quality and reaction-class nodes remain legitimate.
  evidence_ids:
  - node-edges
  - schema
  - go-primary
  - local-authority
  details: "[\n  {\n    \"index\": 0,\n    \"field_path\": \"causal_graphs[0].nodes[0]\"\
    ,\n    \"node_id\": \"ph_range_trait\",\n    \"label\": \"pH range\",\n    \"\
    node_type\": \"TRAIT\",\n    \"grounding\": \"METPO:1000332\",\n    \"description\"\
    : \"Span of external pH values supporting growth.\",\n    \"assessment\": \"Active\
    \ pH-range trait identity and two direct parents agree.\"\n  },\n  {\n    \"index\"\
    : 1,\n    \"field_path\": \"causal_graphs[0].nodes[1]\",\n    \"node_id\": \"\
    external_ph\",\n    \"label\": \"external pH\",\n    \"node_type\": \"ENVIRONMENTAL_FACTOR\"\
    ,\n    \"description\": \"Ambient proton activity (pH) imposed on the cell.\"\
    ,\n    \"assessment\": \"Ambient proton activity is an environmental condition/axis,\
    \ not a material proton molecule or automatically an event.\"\n  },\n  {\n   \
    \ \"index\": 2,\n    \"field_path\": \"causal_graphs[0].nodes[2]\",\n    \"node_id\"\
    : \"acid_tolerance\",\n    \"label\": \"acid tolerance\",\n    \"node_type\":\
    \ \"BIOLOGICAL_PROCESS\",\n    \"description\": \"Capacity to maintain cytoplasmic\
    \ pH against an inward H+ gradient at low external pH.\",\n    \"assessment\"\
    : \"Capacity wording can abbreviate a maintenance process. Native CAPACITY denotes\
    \ pool/reservoir notions, so no automatic CAPACITY retype is warranted; clarify\
    \ the intended disposition versus maintenance facet if revising this graph.\"\n\
    \  },\n  {\n    \"index\": 3,\n    \"field_path\": \"causal_graphs[0].nodes[3]\"\
    ,\n    \"node_id\": \"alkaline_tolerance\",\n    \"label\": \"alkaline tolerance\"\
    ,\n    \"node_type\": \"BIOLOGICAL_PROCESS\",\n    \"description\": \"Capacity\
    \ to maintain cytoplasmic pH against an outward H+ gradient at high external pH.\"\
    ,\n    \"assessment\": \"Same bounded process-versus-tolerance shorthand as node\
    \ 2. No automatic type finding or mechanism completion requirement.\"\n  },\n\
    \  {\n    \"index\": 4,\n    \"field_path\": \"causal_graphs[0].nodes[4]\",\n\
    \    \"node_id\": \"bounded_growth_window\",\n    \"label\": \"bounded pH growth\
    \ window\",\n    \"node_type\": \"BIOLOGICAL_PROCESS\",\n    \"description\":\
    \ \"Span of external pH between the minimum and maximum that supports growth.\"\
    ,\n    \"assessment\": \"Explicit span between minimum and maximum is a numerical\
    \ growth interval, not a biological process. This endpoint choice also affects\
    \ local defines/manifests-as and imported relation objects; assess once within\
    \ the grouped representation finding.\"\n  },\n  {\n    \"index\": 5,\n    \"\
    field_path\": \"causal_graphs[0].nodes[5]\",\n    \"node_id\": \"ph_gradient\"\
    ,\n    \"label\": \"transmembrane pH gradient (\\u0394pH)\",\n    \"node_type\"\
    : \"CHEMICAL\",\n    \"description\": \"Difference between external and cytoplasmic\
    \ pH, a component of the proton motive force.\",\n    \"assessment\": \"Explicit\
    \ pH difference is a gradient/state or measurable attribute, not a chemical entity.\
    \ Material protons and their gradient are distinct; current CHEMICAL typing is\
    \ a firm representation mismatch.\"\n  },\n  {\n    \"index\": 6,\n    \"field_path\"\
    : \"causal_graphs[0].nodes[6]\",\n    \"node_id\": \"membrane_potential\",\n \
    \   \"label\": \"membrane potential (\\u0394\\u03c8)\",\n    \"node_type\": \"\
    CHEMICAL\",\n    \"description\": \"Electrical component of the proton motive\
    \ force across the cell membrane.\",\n    \"assessment\": \"Explicit electrical\
    \ membrane potential is a bioenergetic state/attribute, not a chemical entity.\
    \ The free-text edge does not make this material; group with the linked representation\
    \ audit.\"\n  },\n  {\n    \"index\": 7,\n    \"field_path\": \"causal_graphs[0].nodes[7]\"\
    ,\n    \"node_id\": \"cytoplasmic_ph_homeostasis\",\n    \"label\": \"cytoplasmic\
    \ pH homeostasis\",\n    \"node_type\": \"BIOLOGICAL_PROCESS\",\n    \"description\"\
    : \"Maintenance of a near-constant cytoplasmic pH compatible with macromolecular\
    \ function.\",\n    \"grounding\": \"GO:0051453\",\n    \"assessment\": \"Explicit\
    \ pH-maintenance process has positive active GO:0051453 closeMatch. It is not\
    \ a material executor for RO2327 edge 6.\"\n  },\n  {\n    \"index\": 8,\n   \
    \ \"field_path\": \"causal_graphs[0].nodes[8]\",\n    \"node_id\": \"membrane_proton_impermeability\"\
    ,\n    \"label\": \"membrane proton impermeability\",\n    \"node_type\": \"QUALITY\"\
    ,\n    \"description\": \"Reduced proton leak across the cell membrane that limits\
    \ passive H+ influx.\",\n    \"assessment\": \"Membrane proton impermeability\
    \ is a quality facet. Reference to reduced leak does not force a process type.\"\
    \n  },\n  {\n    \"index\": 9,\n    \"field_path\": \"causal_graphs[0].nodes[9]\"\
    ,\n    \"node_id\": \"mrp_antiporter_activity\",\n    \"label\": \"Mrp Na+/H+\
    \ antiporter activity\",\n    \"node_type\": \"MOLECULAR_FUNCTION\",\n    \"description\"\
    : \"Cation/proton antiport that imports protons while exporting Na+ to support\
    \ pH homeostasis.\",\n    \"assessment\": \"Explicit Mrp antiport activity is\
    \ a legitimate MOLECULAR_FUNCTION; no material protein or mandatory instance is\
    \ inferred. Detailed defense/fitness efficacy remains unassessed.\"\n  },\n  {\n\
    \    \"index\": 10,\n    \"field_path\": \"causal_graphs[0].nodes[10]\",\n   \
    \ \"node_id\": \"amino_acid_decarboxylation\",\n    \"label\": \"amino-acid decarboxylation\"\
    ,\n    \"node_type\": \"BIOLOGICAL_PROCESS\",\n    \"description\": \"Glutamate\
    \ or arginine decarboxylation that consumes intracellular protons and alkalinizes\
    \ the cytoplasm.\",\n    \"assessment\": \"Explicit amino-acid decarboxylation\
    \ reaction class is BIOLOGICAL_PROCESS under the maintained convention. No named\
    \ pathway or detailed defense mechanism is reconstructed.\"\n  }\n]"
- assessment_id: relations
  area: consistency
  topic: 'Native checklist: all ten edges and linked endpoints'
  outcome: concern
  target_ids:
  - METPO:1000332
  summary: RO edges 4/6 have firm material/process role mismatches based on actual
    gradient and homeostasis-process subjects. Their shared interval endpoint and
    local edges 0–3 belong to the same representation discussion. Local defines/manifests-as
    formally admit broad endpoints; their prose concerns feature/state-to-trait semantics,
    not a fabricated strict formal domain. Free-text edges receive no invented imported
    constraints.
  evidence_ids:
  - node-edges
  - ro-primary
  - local-authority
  - challenge
  details: "[\n  {\n    \"index\": 0,\n    \"field_path\": \"causal_graphs[0].edges[0]\"\
    ,\n    \"subject\": \"external_ph\",\n    \"predicate\": \"defines\",\n    \"\
    predicate_id\": \"METPO:2007500\",\n    \"object\": \"bounded_growth_window\"\
    ,\n    \"assessment\": \"Local defines has broad causal-node formal endpoints,\
    \ but semantic feature-to-trait parameterization is imprecise when the current\
    \ object is a numerical interval declared as process. Include in shared node4\
    \ representation discussion, not an invented local-domain violation.\",\n    \"\
    biology_scope\": \"UNASSESSED_SCOPE for detailed acid-defense, AMR, fitness and\
    \ intervention efficacy; generic identity/formal semantics only\"\n  },\n  {\n\
    \    \"index\": 1,\n    \"field_path\": \"causal_graphs[0].edges[1]\",\n    \"\
    subject\": \"acid_tolerance\",\n    \"predicate\": \"defines\",\n    \"predicate_id\"\
    : \"METPO:2007500\",\n    \"object\": \"bounded_growth_window\",\n    \"assessment\"\
    : \"Tolerance may constrain an endpoint, but current defines feature/trait semantics\
    \ and numerical-window referent need clarification. No additional unsupported\
    \ biological or formal-domain finding; shared representation issue.\",\n    \"\
    biology_scope\": \"UNASSESSED_SCOPE for detailed acid-defense, AMR, fitness and\
    \ intervention efficacy; generic identity/formal semantics only\"\n  },\n  {\n\
    \    \"index\": 2,\n    \"field_path\": \"causal_graphs[0].edges[2]\",\n    \"\
    subject\": \"alkaline_tolerance\",\n    \"predicate\": \"defines\",\n    \"predicate_id\"\
    : \"METPO:2007500\",\n    \"object\": \"bounded_growth_window\",\n    \"assessment\"\
    : \"Same qualified endpoint-definition precision as edge1; avoid treating a contextual\
    \ upper-bound explanation as universal measured proof.\",\n    \"biology_scope\"\
    : \"UNASSESSED_SCOPE for detailed acid-defense, AMR, fitness and intervention\
    \ efficacy; generic identity/formal semantics only\"\n  },\n  {\n    \"index\"\
    : 3,\n    \"field_path\": \"causal_graphs[0].edges[3]\",\n    \"subject\": \"\
    bounded_growth_window\",\n    \"predicate\": \"manifests as\",\n    \"predicate_id\"\
    : \"METPO:2007400\",\n    \"object\": \"ph_range_trait\",\n    \"assessment\"\
    : \"Local manifests as describes physiological/molecular state to observable trait\
    \ with broad formal endpoints. Current interval-as-process subject is not that\
    \ described state; include in shared interval/trait representation issue, not\
    \ a false process-only domain claim.\",\n    \"biology_scope\": \"UNASSESSED_SCOPE\
    \ for detailed acid-defense, AMR, fitness and intervention efficacy; generic identity/formal\
    \ semantics only\"\n  },\n  {\n    \"index\": 4,\n    \"field_path\": \"causal_graphs[0].edges[4]\"\
    ,\n    \"subject\": \"ph_gradient\",\n    \"predicate\": \"contributes to\",\n\
    \    \"predicate_id\": \"RO:0002326\",\n    \"object\": \"bounded_growth_window\"\
    ,\n    \"assessment\": \"Confirmed grouped role mismatch: actual gradient subject\
    \ is nonmaterial despite CHEMICAL enum, while RO2326 inherits material-entity\
    \ to process constraints. Explicit bounded interval object is not a process. Current\
    \ enum labels cannot rescue the actual referents.\",\n    \"biology_scope\": \"\
    UNASSESSED_SCOPE for detailed acid-defense, AMR, fitness and intervention efficacy;\
    \ generic identity/formal semantics only\"\n  },\n  {\n    \"index\": 5,\n   \
    \ \"field_path\": \"causal_graphs[0].edges[5]\",\n    \"subject\": \"membrane_potential\"\
    ,\n    \"predicate\": \"compensates for\",\n    \"predicate_id\": null,\n    \"\
    object\": \"external_ph\",\n    \"assessment\": \"Free-text compensates for has\
    \ no asserted imported predicate constraints. Current potential node has a representation\
    \ issue, but no mandatory grounding or fabricated RO type error is added. Detailed\
    \ adaptation efficacy unassessed.\",\n    \"biology_scope\": \"UNASSESSED_SCOPE\
    \ for detailed acid-defense, AMR, fitness and intervention efficacy; generic identity/formal\
    \ semantics only\"\n  },\n  {\n    \"index\": 6,\n    \"field_path\": \"causal_graphs[0].edges[6]\"\
    ,\n    \"subject\": \"cytoplasmic_ph_homeostasis\",\n    \"predicate\": \"enables\"\
    ,\n    \"predicate_id\": \"RO:0002327\",\n    \"object\": \"bounded_growth_window\"\
    ,\n    \"assessment\": \"Confirmed grouped role mismatch independent of the window\
    \ facet: RO2327 requires a material executor and process object, while the subject\
    \ is explicitly GO-grounded homeostasis process. The current interval object further\
    \ complicates the process range. No new mechanism proposed.\",\n    \"biology_scope\"\
    : \"UNASSESSED_SCOPE for detailed acid-defense, AMR, fitness and intervention\
    \ efficacy; generic identity/formal semantics only\"\n  },\n  {\n    \"index\"\
    : 7,\n    \"field_path\": \"causal_graphs[0].edges[7]\",\n    \"subject\": \"\
    membrane_proton_impermeability\",\n    \"predicate\": \"extends\",\n    \"predicate_id\"\
    : null,\n    \"object\": \"acid_tolerance\",\n    \"assessment\": \"Free-text\
    \ extends remains ungrounded and is not assigned RO constraints. Quality to maintenance/tolerance\
    \ context is documentary only; detailed acid-defense/fitness efficacy unassessed.\"\
    ,\n    \"biology_scope\": \"UNASSESSED_SCOPE for detailed acid-defense, AMR, fitness\
    \ and intervention efficacy; generic identity/formal semantics only\"\n  },\n\
    \  {\n    \"index\": 8,\n    \"field_path\": \"causal_graphs[0].edges[8]\",\n\
    \    \"subject\": \"mrp_antiporter_activity\",\n    \"predicate\": \"supports\"\
    ,\n    \"predicate_id\": null,\n    \"object\": \"alkaline_tolerance\",\n    \"\
    assessment\": \"Free-text supports remains ungrounded. Explicit activity subject\
    \ is legitimate; no mandatory protein or imported-domain finding. Detailed acid-defense\
    \ efficacy unassessed.\",\n    \"biology_scope\": \"UNASSESSED_SCOPE for detailed\
    \ acid-defense, AMR, fitness and intervention efficacy; generic identity/formal\
    \ semantics only\"\n  },\n  {\n    \"index\": 9,\n    \"field_path\": \"causal_graphs[0].edges[9]\"\
    ,\n    \"subject\": \"amino_acid_decarboxylation\",\n    \"predicate\": \"alkalinizes\"\
    ,\n    \"predicate_id\": null,\n    \"object\": \"cytoplasmic_ph_homeostasis\"\
    ,\n    \"assessment\": \"Free-text alkalinizes has no imported relation type rule.\
    \ Its process-object wording can be read as shorthand for supporting homeostasis;\
    \ retain a semantic limitation rather than declaring wrong biology or prescribing\
    \ a pathway.\",\n    \"biology_scope\": \"UNASSESSED_SCOPE for detailed acid-defense,\
    \ AMR, fitness and intervention efficacy; generic identity/formal semantics only\"\
    \n  }\n]"
- assessment_id: biological-scope
  area: scope
  topic: 'Native checklist: generic context and exclusions'
  outcome: unknown
  target_ids:
  - METPO:1000332
  summary: Generic pH-range and PMF attribution is assessed. Detailed acid-defense,
    pathogen fitness, AMR, antiporter/decarboxylation efficacy and intervention or
    perturbation effects remain UNASSESSED_SCOPE. Literal occurrence and role compatibility
    do not validate efficacy; no repaired mechanism, route or experimental recommendation
    is supplied.
  evidence_ids:
  - edge-sources
  - source-reading
  - source-access
  details: "{\n  \"completed_at\": \"2026-10-21T19:38:03.316677+00:00\",\n  \"edges\"\
    : [\n    {\n      \"index\": 0,\n      \"field_path\": \"causal_graphs[0].edges[0]\"\
    ,\n      \"subject\": \"external_ph\",\n      \"predicate\": \"defines\",\n  \
    \    \"object\": \"bounded_growth_window\",\n      \"predicate_id\": \"METPO:2007500\"\
    ,\n      \"description\": \"External pH defines the axis over which the growth\
    \ window is bounded.\",\n      \"evidence\": [\n        {\n          \"reference\"\
    : \"DOI:10.1038/nrmicro2549\",\n          \"snippet\": \"external pH\",\n    \
    \      \"notes\": \"Supports external pH as the axis bounding the growth window.\"\
    \n        }\n      ],\n      \"assessment\": \"Generic external-pH axis is directly\
    \ supported by the assigned abstract and BioC opening; exact measured boundaries\
    \ remain organism-specific.\",\n      \"biological_scope\": \"Generic environmental\
    \ context and source attribution only; no universal biological sufficiency claim\"\
    \n    },\n    {\n      \"index\": 1,\n      \"field_path\": \"causal_graphs[0].edges[1]\"\
    ,\n      \"subject\": \"acid_tolerance\",\n      \"predicate\": \"defines\",\n\
    \      \"object\": \"bounded_growth_window\",\n      \"predicate_id\": \"METPO:2007500\"\
    ,\n      \"description\": \"Acid tolerance sets the lower bound of the pH growth\
    \ window.\",\n      \"evidence\": [\n        {\n          \"reference\": \"DOI:10.1016/j.tim.2007.02.005\"\
    ,\n          \"snippet\": \"highly impermeable cell membranes\",\n          \"\
    notes\": \"Supports envelope proton barriers as the lower-bound mechanism for\
    \ low-pH growth.\"\n        }\n      ],\n      \"assessment\": \"The exact assigned\
    \ acidophile abstract supports low-pH membrane-barrier context. This is generic\
    \ lower-bound context, not a universal single necessary or sufficient mechanism.\"\
    ,\n      \"biological_scope\": \"Generic environmental context and source attribution\
    \ only; no universal biological sufficiency claim\"\n    },\n    {\n      \"index\"\
    : 2,\n      \"field_path\": \"causal_graphs[0].edges[2]\",\n      \"subject\"\
    : \"alkaline_tolerance\",\n      \"predicate\": \"defines\",\n      \"object\"\
    : \"bounded_growth_window\",\n      \"predicate_id\": \"METPO:2007500\",\n   \
    \   \"description\": \"Alkaline tolerance sets the upper bound of the pH growth\
    \ window.\",\n      \"evidence\": [\n        {\n          \"reference\": \"DOI:10.1038/nrmicro2549\"\
    ,\n          \"snippet\": \"alkaliphiles\",\n          \"notes\": \"Supports alkaline-tolerance\
    \ physiology as the upper-bound mechanism for high-pH growth.\"\n        }\n \
    \     ],\n      \"assessment\": \"Assigned Krulwich text explicitly discusses\
    \ alkaliphiles and growth at elevated external pH. Generic upper-bound context\
    \ is supported; no universal single strategy or exact numerical cutoff is inferred.\"\
    ,\n      \"biological_scope\": \"Generic environmental context and source attribution\
    \ only; no universal biological sufficiency claim\"\n    },\n    {\n      \"index\"\
    : 3,\n      \"field_path\": \"causal_graphs[0].edges[3]\",\n      \"subject\"\
    : \"bounded_growth_window\",\n      \"predicate\": \"manifests as\",\n      \"\
    object\": \"ph_range_trait\",\n      \"predicate_id\": \"METPO:2007400\",\n  \
    \    \"description\": \"The bounded pH growth window manifests the pH-range phenotype.\"\
    ,\n      \"evidence\": [\n        {\n          \"reference\": \"DOI:10.1038/nrmicro2549\"\
    ,\n          \"snippet\": \"pH homeostasis\",\n          \"notes\": \"Supports\
    \ the trait endpoint.\"\n        }\n      ],\n      \"assessment\": \"Generic\
    \ pH-homeostasis context is supported; the measurement/trait relationship and\
    \ local predicate semantics are assessed independently by grounding, not proved\
    \ by the two-word snippet.\",\n      \"biological_scope\": \"Generic environmental\
    \ context and source attribution only; no universal biological sufficiency claim\"\
    \n    },\n    {\n      \"index\": 4,\n      \"field_path\": \"causal_graphs[0].edges[4]\"\
    ,\n      \"subject\": \"ph_gradient\",\n      \"predicate\": \"contributes to\"\
    ,\n      \"object\": \"bounded_growth_window\",\n      \"predicate_id\": \"RO:0002326\"\
    ,\n      \"description\": \"The transmembrane pH gradient sets whether cytoplasmic\
    \ pH can be maintained across the external pH range.\",\n      \"evidence\": [\n\
    \        {\n          \"reference\": \"DOI:10.1038/nrmicro2549\",\n          \"\
    notes\": \"PMF architecture (\\u0394\\u03c8 \\u2212 59 \\u0394pH) determines the\
    \ range of pHout over which bacteria can tolerate or grow.\"\n        }\n    \
    \  ],\n      \"assessment\": \"BioC offsets 2440 and 3214 support the two-component\
    \ PMF and approximation under standard conditions. Offset 3940 supplies condition-specific\
    \ illustrative patterns. The current note is contextual; the approximation alone\
    \ does not calibrate a complete growth interval or prove biological sufficiency.\"\
    ,\n      \"biological_scope\": \"Generic environmental context and source attribution\
    \ only; no universal biological sufficiency claim\"\n    },\n    {\n      \"index\"\
    : 5,\n      \"field_path\": \"causal_graphs[0].edges[5]\",\n      \"subject\"\
    : \"membrane_potential\",\n      \"predicate\": \"compensates for\",\n      \"\
    object\": \"external_ph\",\n      \"predicate_id\": null,\n      \"description\"\
    : \"Adjustment or reversal of the membrane-potential PMF component offsets extreme\
    \ external pH stress.\",\n      \"evidence\": [\n        {\n          \"reference\"\
    : \"DOI:10.1038/nrmicro2549\",\n          \"notes\": \"Under strong pH stress\
    \ the orientation of a PMF component can reverse to maintain homeostasis.\"\n\
    \        }\n      ],\n      \"assessment\": \"BioC offset 3940 explicitly illustrates\
    \ reversed PMF components in distinct growth-pH contexts. Preserve source-specific\
    \ illustrations and generic context; this does not certify a universal compensation\
    \ response.\",\n      \"biological_scope\": \"Generic environmental context and\
    \ source attribution only; no universal biological sufficiency claim\"\n    },\n\
    \    {\n      \"index\": 6,\n      \"field_path\": \"causal_graphs[0].edges[6]\"\
    ,\n      \"subject\": \"cytoplasmic_ph_homeostasis\",\n      \"predicate\": \"\
    enables\",\n      \"object\": \"bounded_growth_window\",\n      \"predicate_id\"\
    : \"RO:0002327\",\n      \"description\": \"Keeping cytoplasmic pH compatible\
    \ with protein function enables growth across the external pH range.\",\n    \
    \  \"evidence\": [\n        {\n          \"reference\": \"DOI:10.1038/nrmicro2549\"\
    ,\n          \"notes\": \"Bacteria maintain a distinct cytoplasmic pH required\
    \ for protein function, bounding the phenotype.\"\n        }\n      ],\n     \
    \ \"assessment\": \"Generic BioC opening links internal-pH compatibility to protein\
    \ function and distinguishes growth ranges from survival outside growth ranges.\
    \ Generic context is supported; formal enables roles are a separate question.\"\
    ,\n      \"biological_scope\": \"Generic environmental context and source attribution\
    \ only; no universal biological sufficiency claim\"\n    },\n    {\n      \"index\"\
    : 7,\n      \"field_path\": \"causal_graphs[0].edges[7]\",\n      \"subject\"\
    : \"membrane_proton_impermeability\",\n      \"predicate\": \"extends\",\n   \
    \   \"object\": \"acid_tolerance\",\n      \"predicate_id\": null,\n      \"description\"\
    : \"Reduced proton leak helps maintain cytoplasmic pH and extends growth to lower\
    \ external pH.\",\n      \"evidence\": [\n        {\n          \"reference\":\
    \ \"DOI:10.3389/fmicb.2020.556140\",\n          \"notes\": \"Modification of membrane\
    \ lipid composition to reduce proton permeability is a general acid-stress mechanism.\"\
    \n        }\n      ],\n      \"assessment\": \"Assigned mixed-context perspective\
    \ identity and acid-response scope verified. Detailed lipid/acid-defense/fitness\
    \ efficacy is UNASSESSED_SCOPE; neither validated nor refuted from the abstract.\"\
    ,\n      \"biological_scope\": \"UNASSESSED_SCOPE detailed biological efficacy\"\
    \n    },\n    {\n      \"index\": 8,\n      \"field_path\": \"causal_graphs[0].edges[8]\"\
    ,\n      \"subject\": \"mrp_antiporter_activity\",\n      \"predicate\": \"supports\"\
    ,\n      \"object\": \"alkaline_tolerance\",\n      \"predicate_id\": null,\n\
    \      \"description\": \"Na+/H+ exchange imports protons and is a principal strategy\
    \ for alkaline pH homeostasis.\",\n      \"evidence\": [\n        {\n        \
    \  \"reference\": \"DOI:10.1038/nrmicro2549\",\n          \"notes\": \"Na+/H+\
    \ antiport is the principal strategy for cytoplasmic pH homeostasis at high external\
    \ pH.\"\n        }\n      ],\n      \"assessment\": \"Assigned broad homeostasis\
    \ review identity and generic alkaline-homeostasis context verified. Detailed\
    \ antiporter efficacy, necessity and pathogen intervention biology are UNASSESSED_SCOPE;\
    \ no replacement mechanism or source transfer is supplied.\",\n      \"biological_scope\"\
    : \"UNASSESSED_SCOPE detailed biological efficacy\"\n    },\n    {\n      \"index\"\
    : 9,\n      \"field_path\": \"causal_graphs[0].edges[9]\",\n      \"subject\"\
    : \"amino_acid_decarboxylation\",\n      \"predicate\": \"alkalinizes\",\n   \
    \   \"object\": \"cytoplasmic_ph_homeostasis\",\n      \"predicate_id\": null,\n\
    \      \"description\": \"Glutamate or arginine decarboxylation consumes intracellular\
    \ protons, supporting cytoplasmic pH at acidic external pH.\",\n      \"evidence\"\
    : [\n        {\n          \"reference\": \"DOI:10.3389/fmicb.2020.556140\",\n\
    \          \"notes\": \"Decarboxylation of glutamate or arginine is a recurring\
    \ proton-consuming acid-response module.\"\n        }\n      ],\n      \"assessment\"\
    : \"Assigned mixed-context perspective identity and acid-response scope verified.\
    \ Detailed decarboxylation/defense/fitness efficacy is UNASSESSED_SCOPE; no reaction\
    \ optimization or causal repair is provided.\",\n      \"biological_scope\": \"\
    UNASSESSED_SCOPE detailed biological efficacy\"\n    }\n  ],\n  \"scope\": \"\
    All current edges accounted for. Source attribution is separate from formal ontology\
    \ role correctness. Detailed pathogen acid-defense/fitness/AMR and intervention\
    \ efficacy are unassessed.\"\n}"
- assessment_id: completeness
  area: completeness
  topic: 'Native checklist: whole current record and optional evidence'
  outcome: supported
  target_ids:
  - METPO:1000332
  summary: All eleven nodes, ten edges, one component, one canonical, six excerpts
    and twelve record events are covered. There are zero protein-class nodes and zero
    instances. The nonmechanistic interval scope does not require token proteins,
    accessions, extra connectors or newly named pathways.
  evidence_ids:
  - record
  - node-edges
  - node-sources
  - policy
  - checklist
  details: "{\n  \"completed_at\": \"2026-10-21T19:38:03.317040+00:00\",\n  \"nodes\"\
    : [\n    {\n      \"index\": 0,\n      \"field_path\": \"causal_graphs[0].nodes[0]\"\
    ,\n      \"node\": {\n        \"node_id\": \"ph_range_trait\",\n        \"label\"\
    : \"pH range\",\n        \"node_type\": \"TRAIT\",\n        \"grounding\": \"\
    METPO:1000332\",\n        \"description\": \"Span of external pH values supporting\
    \ growth.\"\n      },\n      \"incident_edges\": [\n        3\n      ],\n    \
    \  \"source_references\": [\n        \"DOI:10.1038/nrmicro2549\"\n      ],\n \
    \     \"assessment\": \"Current node and all incident evidence placements documented.\
    \ Referent/facet and imported-ontology semantics belong to the grounding ledger.\
    \ Generic physicochemical/measurement context assessed without asserting universal\
    \ necessity or exact interval calibration.\"\n    },\n    {\n      \"index\":\
    \ 1,\n      \"field_path\": \"causal_graphs[0].nodes[1]\",\n      \"node\": {\n\
    \        \"node_id\": \"external_ph\",\n        \"label\": \"external pH\",\n\
    \        \"node_type\": \"ENVIRONMENTAL_FACTOR\",\n        \"description\": \"\
    Ambient proton activity (pH) imposed on the cell.\"\n      },\n      \"incident_edges\"\
    : [\n        0,\n        5\n      ],\n      \"source_references\": [\n       \
    \ \"DOI:10.1038/nrmicro2549\"\n      ],\n      \"assessment\": \"Current node\
    \ and all incident evidence placements documented. Referent/facet and imported-ontology\
    \ semantics belong to the grounding ledger. Generic physicochemical/measurement\
    \ context assessed without asserting universal necessity or exact interval calibration.\"\
    \n    },\n    {\n      \"index\": 2,\n      \"field_path\": \"causal_graphs[0].nodes[2]\"\
    ,\n      \"node\": {\n        \"node_id\": \"acid_tolerance\",\n        \"label\"\
    : \"acid tolerance\",\n        \"node_type\": \"BIOLOGICAL_PROCESS\",\n      \
    \  \"description\": \"Capacity to maintain cytoplasmic pH against an inward H+\
    \ gradient at low external pH.\"\n      },\n      \"incident_edges\": [\n    \
    \    1,\n        7\n      ],\n      \"source_references\": [\n        \"DOI:10.1016/j.tim.2007.02.005\"\
    ,\n        \"DOI:10.3389/fmicb.2020.556140\"\n      ],\n      \"assessment\":\
    \ \"Current node and all incident evidence placements documented. Referent/facet\
    \ and imported-ontology semantics belong to the grounding ledger. Generic physicochemical/measurement\
    \ context assessed without asserting universal necessity or exact interval calibration.\"\
    \n    },\n    {\n      \"index\": 3,\n      \"field_path\": \"causal_graphs[0].nodes[3]\"\
    ,\n      \"node\": {\n        \"node_id\": \"alkaline_tolerance\",\n        \"\
    label\": \"alkaline tolerance\",\n        \"node_type\": \"BIOLOGICAL_PROCESS\"\
    ,\n        \"description\": \"Capacity to maintain cytoplasmic pH against an outward\
    \ H+ gradient at high external pH.\"\n      },\n      \"incident_edges\": [\n\
    \        2,\n        8\n      ],\n      \"source_references\": [\n        \"DOI:10.1038/nrmicro2549\"\
    \n      ],\n      \"assessment\": \"Current node and all incident evidence placements\
    \ documented. Referent/facet and imported-ontology semantics belong to the grounding\
    \ ledger. Generic physicochemical/measurement context assessed without asserting\
    \ universal necessity or exact interval calibration.\"\n    },\n    {\n      \"\
    index\": 4,\n      \"field_path\": \"causal_graphs[0].nodes[4]\",\n      \"node\"\
    : {\n        \"node_id\": \"bounded_growth_window\",\n        \"label\": \"bounded\
    \ pH growth window\",\n        \"node_type\": \"BIOLOGICAL_PROCESS\",\n      \
    \  \"description\": \"Span of external pH between the minimum and maximum that\
    \ supports growth.\"\n      },\n      \"incident_edges\": [\n        0,\n    \
    \    1,\n        2,\n        3,\n        4,\n        6\n      ],\n      \"source_references\"\
    : [\n        \"DOI:10.1016/j.tim.2007.02.005\",\n        \"DOI:10.1038/nrmicro2549\"\
    \n      ],\n      \"assessment\": \"Current node and all incident evidence placements\
    \ documented. Referent/facet and imported-ontology semantics belong to the grounding\
    \ ledger. Generic physicochemical/measurement context assessed without asserting\
    \ universal necessity or exact interval calibration.\"\n    },\n    {\n      \"\
    index\": 5,\n      \"field_path\": \"causal_graphs[0].nodes[5]\",\n      \"node\"\
    : {\n        \"node_id\": \"ph_gradient\",\n        \"label\": \"transmembrane\
    \ pH gradient (\\u0394pH)\",\n        \"node_type\": \"CHEMICAL\",\n        \"\
    description\": \"Difference between external and cytoplasmic pH, a component of\
    \ the proton motive force.\"\n      },\n      \"incident_edges\": [\n        4\n\
    \      ],\n      \"source_references\": [\n        \"DOI:10.1038/nrmicro2549\"\
    \n      ],\n      \"assessment\": \"Current node and all incident evidence placements\
    \ documented. Referent/facet and imported-ontology semantics belong to the grounding\
    \ ledger. Generic physicochemical/measurement context assessed without asserting\
    \ universal necessity or exact interval calibration.\"\n    },\n    {\n      \"\
    index\": 6,\n      \"field_path\": \"causal_graphs[0].nodes[6]\",\n      \"node\"\
    : {\n        \"node_id\": \"membrane_potential\",\n        \"label\": \"membrane\
    \ potential (\\u0394\\u03c8)\",\n        \"node_type\": \"CHEMICAL\",\n      \
    \  \"description\": \"Electrical component of the proton motive force across the\
    \ cell membrane.\"\n      },\n      \"incident_edges\": [\n        5\n      ],\n\
    \      \"source_references\": [\n        \"DOI:10.1038/nrmicro2549\"\n      ],\n\
    \      \"assessment\": \"Current node and all incident evidence placements documented.\
    \ Referent/facet and imported-ontology semantics belong to the grounding ledger.\
    \ Generic physicochemical/measurement context assessed without asserting universal\
    \ necessity or exact interval calibration.\"\n    },\n    {\n      \"index\":\
    \ 7,\n      \"field_path\": \"causal_graphs[0].nodes[7]\",\n      \"node\": {\n\
    \        \"node_id\": \"cytoplasmic_ph_homeostasis\",\n        \"label\": \"cytoplasmic\
    \ pH homeostasis\",\n        \"node_type\": \"BIOLOGICAL_PROCESS\",\n        \"\
    description\": \"Maintenance of a near-constant cytoplasmic pH compatible with\
    \ macromolecular function.\",\n        \"grounding\": \"GO:0051453\"\n      },\n\
    \      \"incident_edges\": [\n        6,\n        9\n      ],\n      \"source_references\"\
    : [\n        \"DOI:10.1038/nrmicro2549\",\n        \"DOI:10.3389/fmicb.2020.556140\"\
    \n      ],\n      \"assessment\": \"Current node and all incident evidence placements\
    \ documented. Referent/facet and imported-ontology semantics belong to the grounding\
    \ ledger. Generic physicochemical/measurement context assessed without asserting\
    \ universal necessity or exact interval calibration.\"\n    },\n    {\n      \"\
    index\": 8,\n      \"field_path\": \"causal_graphs[0].nodes[8]\",\n      \"node\"\
    : {\n        \"node_id\": \"membrane_proton_impermeability\",\n        \"label\"\
    : \"membrane proton impermeability\",\n        \"node_type\": \"QUALITY\",\n \
    \       \"description\": \"Reduced proton leak across the cell membrane that limits\
    \ passive H+ influx.\"\n      },\n      \"incident_edges\": [\n        7\n   \
    \   ],\n      \"source_references\": [\n        \"DOI:10.3389/fmicb.2020.556140\"\
    \n      ],\n      \"assessment\": \"Current node and all incident evidence placements\
    \ documented. Referent/facet and imported-ontology semantics belong to the grounding\
    \ ledger. Detailed pathway/defense efficacy UNASSESSED_SCOPE.\"\n    },\n    {\n\
    \      \"index\": 9,\n      \"field_path\": \"causal_graphs[0].nodes[9]\",\n \
    \     \"node\": {\n        \"node_id\": \"mrp_antiporter_activity\",\n       \
    \ \"label\": \"Mrp Na+/H+ antiporter activity\",\n        \"node_type\": \"MOLECULAR_FUNCTION\"\
    ,\n        \"description\": \"Cation/proton antiport that imports protons while\
    \ exporting Na+ to support pH homeostasis.\"\n      },\n      \"incident_edges\"\
    : [\n        8\n      ],\n      \"source_references\": [\n        \"DOI:10.1038/nrmicro2549\"\
    \n      ],\n      \"assessment\": \"Current node and all incident evidence placements\
    \ documented. Referent/facet and imported-ontology semantics belong to the grounding\
    \ ledger. Detailed pathway/defense efficacy UNASSESSED_SCOPE.\"\n    },\n    {\n\
    \      \"index\": 10,\n      \"field_path\": \"causal_graphs[0].nodes[10]\",\n\
    \      \"node\": {\n        \"node_id\": \"amino_acid_decarboxylation\",\n   \
    \     \"label\": \"amino-acid decarboxylation\",\n        \"node_type\": \"BIOLOGICAL_PROCESS\"\
    ,\n        \"description\": \"Glutamate or arginine decarboxylation that consumes\
    \ intracellular protons and alkalinizes the cytoplasm.\"\n      },\n      \"incident_edges\"\
    : [\n        9\n      ],\n      \"source_references\": [\n        \"DOI:10.3389/fmicb.2020.556140\"\
    \n      ],\n      \"assessment\": \"Current node and all incident evidence placements\
    \ documented. Referent/facet and imported-ontology semantics belong to the grounding\
    \ ledger. Detailed pathway/defense efficacy UNASSESSED_SCOPE.\"\n    }\n  ]\n}"
- assessment_id: expression
  area: evidence
  topic: 'Native checklist: retained catalog applicability'
  outcome: unknown
  target_ids:
  - METPO:1000332
  summary: The complete retained 20-organism/28-dataset catalog has no match for the
    canonical Oceanimonas genus/species or verified strain aliases. This is bounded
    to the snapshot; no substitute organism or downstream defense gene/module query
    was used.
  evidence_ids:
  - expression
  - authority-reuse
  - identity-reuse
  details: "{\n  \"assessed_at\": \"2026-10-21T19:38:01.754511+00:00\",\n  \"target\"\
    : \"data/traits/environment/ph_range.yaml\",\n  \"status\": \"NO_CANONICAL_CATALOG_MATCH\"\
    ,\n  \"canonical_taxon\": \"NCBITaxon:3028314\",\n  \"canonical_name\": \"Oceanimonas\
    \ pelagia\",\n  \"names_and_aliases_checked\": [\n    \"Oceanimonas\",\n    \"\
    Oceanimonas pelagia\",\n    \"Oceanimonas sp. NTOU-MSR1\",\n    \"NTOU-MSR1\"\
    ,\n    \"BCRC 81403\",\n    \"JCM 36023\"\n  ],\n  \"catalog_counts\": {\n   \
    \ \"organisms\": 20,\n    \"datasets\": 28\n  },\n  \"matches\": [],\n  \"original_access\"\
    : {\n    \"started_at\": \"2026-10-21T07:36:12.732638+00:00\",\n    \"finished_at\"\
    : \"2026-10-21T07:36:12.858149+00:00\"\n  },\n  \"catalog\": {\n    \"path\":\
    \ \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-grounding-agent/reused-datasets.json\"\
    ,\n    \"sha256\": \"155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693\"\
    ,\n    \"bytes\": 2871\n  },\n  \"reuse\": {\n    \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-grounding-agent/authority-reuse-receipts.json\"\
    ,\n    \"sha256\": \"99da6e94f5769c9ad5bd2d16565a49363d5552f77565d17b781c61bb5482ca14\"\
    ,\n    \"bytes\": 2011\n  },\n  \"scope\": \"Complete retained structured catalog\
    \ checked for the official canonical genus/species and strain aliases only. No\
    \ substitute organism, downstream gene/module query or detailed acid-defense/fitness/intervention\
    \ analysis. Absence is bounded to this catalog snapshot.\",\n  \"optional_proteins\"\
    : \"Zero protein-class nodes and zero instances do not create a completeness failure\
    \ in this NONMECHANISTIC quantitative record.\"\n}"
- assessment_id: ownership
  area: provenance
  topic: 'Native checklist: current owners and recurrence limits'
  outcome: supported
  target_ids:
  - METPO:1000332
  summary: The current record owns the interval/gradient declarations. Predicate mappings
    and the shared writer own assignment, with nonempty IDs skipped. No exact current
    gradient-repair writer was established; the ph_range_mid2 writer is sibling context
    only. Canonical backfill and reaction-class migration are positive, distinct owners
    of their own fields.
  evidence_ids:
  - owners
  - local-authority
  - ground-reading
  details: "{\n  \"assessed_at\": \"2026-10-21T19:38:01.753184+00:00\",\n  \"target\"\
    : \"data/traits/environment/ph_range.yaml\",\n  \"counts\": {\n    \"nodes\":\
    \ 11,\n    \"edges\": 10,\n    \"components\": 1,\n    \"protein_classes\": 0,\n\
    \    \"label_only_proteins\": 0,\n    \"protein_instances\": 0,\n    \"canonical_examples\"\
    : 1,\n    \"record_history_events\": 12,\n    \"ai_record_events\": 11,\n    \"\
    seed_events\": 1,\n    \"captured_histories\": 7,\n    \"whole_histories_read\"\
    : 7,\n    \"matching_paths\": 325,\n    \"review_target_arrays\": 68,\n    \"\
    exact_target_review_arrays\": 0\n  },\n  \"search\": {\n    \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-grounding-agent/search-and-provenance.json\"\
    ,\n    \"sha256\": \"b7ed29d8b076b710ec708b7a2996120c3df0e0ca1e5b54156a2b3fca736a5cda\"\
    ,\n    \"bytes\": 101712\n  },\n  \"node_search\": {\n    \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-grounding-agent/all-node-owner-search.json\"\
    ,\n    \"sha256\": \"a5010a2c11125029ec472073eccab54ff3e2616fd4c9bd2db39ed1fe0ab5f759\"\
    ,\n    \"bytes\": 6658\n  },\n  \"exact_owner_search\": {\n    \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-grounding-agent/exact-owner-search.json\"\
    ,\n    \"sha256\": \"b1baaa328c01ebaf58525851ca19e31969803425e3e48a60926acfb1f9eccc8c\"\
    ,\n    \"bytes\": 1291\n  },\n  \"search_scope\": \"Entire repository including\
    \ ignored/hidden files except .git internals and .venv; fixed-string case-insensitive\
    \ target slug/hyphen/label/full and numeric ID. Because pH range overlaps sibling\
    \ names, each structured target array was parsed exactly. All 11 node identifiers\
    \ separately searched; seven history leads captured, none uncaptured.\",\n  \"\
    history_scope\": \"All seven captured histories read in full and actor/target\
    \ projections checked. They are AI-authored infrastructure, canonical-batch or\
    \ ph_range_mid2 sibling context; not linked human acceptance of the current graph.\
    \ No full unlisted history read is claimed.\",\n  \"human_acceptance\": \"Current\
    \ created_by Luke Wang and upstream creator attribution are retained as positive\
    \ human concept provenance. No linked acceptance of later AI-enriched current\
    \ record/graph found in 325 matching paths, 68 structured target arrays with zero\
    \ exact target, or seven AI histories. The 12 record events comprise 11 AI edits\
    \ and an automated seed. This is a bounded acceptance-link gap, not a claim that\
    \ no human ever reviewed the concept.\",\n  \"owners\": [\n    {\n      \"path\"\
    : \"data/traits/environment/ph_range.yaml\",\n      \"role\": \"Primary current\
    \ owner of interval/gradient/electrical-potential declarations and affected edges;\
    \ no exact maintained node-repair writer for current ph_range established in bounded\
    \ search.\",\n      \"sha256\": \"8a9cac2ea39eaf0aaafb950fce9b8119713bbef55c43e84550f22c3ee9d13d1a\"\
    \n    },\n    {\n      \"path\": \"mappings/predicate_grounding.tsv\",\n     \
    \ \"role\": \"Maintained RO2326/RO2327, defines and manifests-as mappings; wildcard\
    \ gates do not remove imported semantics.\",\n      \"sha256\": \"8e28c19e93aca3dc164a3befbe2612b289241de457c59f499e65936c03b7ce52\"\
    \n    },\n    {\n      \"path\": \"scripts/ground_causal_predicates.py\",\n  \
    \    \"role\": \"Shared assignment writer skips all already nonempty predicate_id\
    \ values; changing a mapping alone does not repair current edges.\",\n      \"\
    sha256\": \"5a788eeaabf3a56b0d82c469a3e3fe28f1d51707d9382313b9a94289be7d1381\"\
    \n    },\n    {\n      \"path\": \"mappings/node_grounding.tsv\",\n      \"role\"\
    : \"Positive GO0051453 closeMatch row27; not a current gradient retyping owner.\"\
    ,\n      \"sha256\": \"d7de9b3ab04960c4775a5bc295a945bd1a72d81467830459f4793e654f82b3d0\"\
    \n    },\n    {\n      \"path\": \"scripts/ground_causal_nodes.py\",\n      \"\
    role\": \"Shared node-grounding writer skips existing nonempty grounds; positive\
    \ homeostasis mapping does not turn process into material executor.\",\n     \
    \ \"sha256\": \"204ce4162544154b1752b65da2136538847ea25ced26a52f5708eadff08f5d42\"\
    \n    },\n    {\n      \"path\": \"scripts/migrate_pathway_vs_process.py\",\n\
    \      \"role\": \"Direct current amino_acid_decarboxylation facet maintainer:\
    \ node-id table plus corpus traversal/upsert. Its BIOLOGICAL_PROCESS decision\
    \ is positive; it is not an owner of current gradient/interval node corrections.\"\
    ,\n      \"sha256\": \"f236de7183048732e9001b7fac4367affff58d8b7a7d5c63286e6b058a4b38c2\"\
    \n    },\n    {\n      \"path\": \"scripts/backfill_canonical_examples_444.py\"\
    ,\n      \"role\": \"Exact environment/ph_range canonical entry at line433; live\
    \ queue guard, identical-existing no-op and nonempty-drift rejection. Direct canonical\
    \ owner only.\",\n      \"sha256\": \"18ca0766789c239d693ef665e8b1d43c1209a0f414a326f1c5d890f88de7b20c\"\
    \n    },\n    {\n      \"path\": \"scripts/review_ph_range_mid2_graph_183.py\"\
    ,\n      \"role\": \"Sibling-only writer, explicit environment/ph_range_mid2 SLUG;\
    \ its membrane_potential STATE replacement is comparator context, not current\
    \ ph_range recurrence ownership.\",\n      \"sha256\": \"2788c907439099c64cbc25c50b973e5ac0d2b93bc07ff7ed89e4cddaae500bd3\"\
    \n    },\n    {\n      \"path\": \"scripts/migrate_node_type_consistency.py\"\
    ,\n      \"role\": \"Generic STATE/PMF context; bounded exact-key search does\
    \ not establish a current ph_gradient or membrane_potential replacement in this\
    \ table.\",\n      \"sha256\": \"a3e7bc170e60f406a73e06c893d74f5253671028d3d40cc15ecf882b6684a69e\"\
    \n    },\n    {\n      \"path\": \"scripts/migrate_process_quality_consistency.py\"\
    ,\n      \"role\": \"Related reversed-potential and permeability families are\
    \ contextual; not exact owners of the current ph_range gradient/interval nodes.\"\
    ,\n      \"sha256\": \"1a83ad3dba79ed0c958b875a6fcc4b9e562259af26da2f248d32d5cf7784f80a\"\
    \n    }\n  ],\n  \"research_limit\": \"Only current Falcon frontmatter read: August4\
    \ artifact is contextual and does not establish the exact report version behind\
    \ June23 enrichment.\",\n  \"readiness\": \"Needs curation for grouped representation\
    \ and relation roles. No target, writer, state or Git mutation; no native checks\
    \ executed by this auditor.\"\n}"
- assessment_id: human-acceptance
  area: provenance
  topic: 'Native checklist: creator versus current acceptance'
  outcome: concern
  target_ids:
  - METPO:1000332
  summary: Luke Wang concept attribution remains positive. The bounded ignored-inclusive
    search found 325 paths and 68 parsed review target arrays, with zero exact target
    arrays. Seven captured AI histories were fully read. Twelve record events comprise
    eleven AI edits plus seed; none of these alone links human acceptance of the later
    current graph.
  evidence_ids:
  - owners
  - playbook
  - identity
  - challenge
  - adjudication
- assessment_id: readiness
  area: consistency
  topic: 'Native checklist: actual checks and qualified common reuse'
  outcome: supported
  target_ids:
  - METPO:1000332
  summary: All 77 captured inputs and frozen artifacts match. Focused native, strict
    and snippet checks passed. Historical common failures, retries, skips and original
    times remain explicit under actual B10-to-B11 qualification. No new B11 QC execution
    is claimed.
  evidence_ids:
  - capture
  - reuse
  - reuse-postcheck
  - native-checks
  - check-ph-range-native
  - check-ph-range-strict
  - check-ph-range-snippets
findings:
- finding_id: linked-representation-roles
  issue_key: ph-range-linked-representation-roles
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Interval and electrochemical states conflict with linked declared and imported
    roles
  description: Node 4 explicitly denotes a numerical interval, while nodes 5/6 denote
    a nonmaterial pH gradient and electrical potential. Their process/chemical declarations
    conflict with these referents. RO:0002326 edge 4 and RO:0002327 edge 6 require
    material subjects and process objects; the actual gradient/process subjects and
    shared interval object fail these roles. Local edges 0–3 expose the same interval/trait
    referent choice, with broad formal proposal endpoints. This is one linked representation
    finding, not repeated penalties for each shared endpoint.
  target_ids:
  - METPO:1000332
  field_paths:
  - causal_graphs[0].nodes[4]
  - causal_graphs[0].nodes[5]
  - causal_graphs[0].nodes[6]
  - causal_graphs[0].edges[4]
  - causal_graphs[0].edges[6]
  evidence_ids:
  - node-edges
  - ro-primary
  - schema
  - local-authority
  - owners
  - challenge
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_range.yaml
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
- finding_id: baker-attribution-scope
  issue_key: ph-range-baker-attribution-scope
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Assigned acidophile attribution is broadened to alkaline extremes
  description: The actual Baker abstract supports its exact impermeable-membrane phrase
    in acidophiles and low-pH growth. Evidence[1].notes extends this assigned attribution
    to both acidic and alkaline extremes. Clarify the supported source scope or substantiate
    the broader attribution. The inaccessible full article is not declared devoid
    of alkaline discussion, and the acid lower-bound placement and quotations remain
    positive.
  target_ids:
  - METPO:1000332
  field_paths:
  - evidence[1].notes
  evidence_ids:
  - meta-baker
  - sources
  - placements
  - source-access
  - challenge
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_range.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: human-acceptance-link
  issue_key: ph-range-human-acceptance-link
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Current graph lacks a linked acceptance reference within the bounded local
    search
  description: Known Luke Wang concept authorship is retained. REVIEWED status, AI
    enrichment and passing checks do not independently identify human acceptance of
    the current graph. The ignored-inclusive local search and exact target parsing
    bound this finding; remote or private human decisions are not declared absent.
  target_ids:
  - METPO:1000332
  field_paths:
  - mapping_status
  - curation_history
  evidence_ids:
  - owners
  - identity
  - playbook
  - challenge
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_range.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
actions:
- action_id: reconcile-representation
  description: Reconcile the existing interval, gradient and potential referents with
    their declared facets and relation semantics during separately authorized curation.
  finding_ids:
  - linked-representation-roles
  target_ids:
  - METPO:1000332
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_range.yaml
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
  - Resolve the shared interval endpoint once across local edges 0–3 and imported
    edges 4/6; preserve the distinction between broad formal local endpoints and descriptive
    feature/state-to-trait semantics.
  - Keep legitimate activity and reaction-class nodes, qualified capacity shorthand
    and free-text predicates separate from the confirmed anchors. Do not impose an
    automatic replacement type or biological route.
  - Inspect actual shared-writer nonempty-ID behavior; mapping-only edits do not repair
    existing assertions. No sibling writer is a current recurrence owner. Use guarded
    history, appropriate native/strict/grounding/QC checks and a successor review
    after changed inputs.
- action_id: qualify-baker-attribution
  description: Qualify evidence[1].notes to the actually supported acidophile attribution
    or add separately verified support for the broader scope.
  finding_ids:
  - baker-attribution-scope
  target_ids:
  - METPO:1000332
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_range.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Preserve both exact Baker phrases and the supported acid lower-bound context.
  - Do not convert inaccessible full text into a false-quote or false-biology conclusion,
    and do not add detailed defense or intervention mechanisms.
- action_id: link-human-acceptance
  description: Link existing attributable current acceptance if available, or clarify
    status while preserving known concept and AI provenance.
  finding_ids:
  - human-acceptance-link
  target_ids:
  - METPO:1000332
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_range.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Preserve Luke Wang attribution, bounded search counts and seven-history reading
    scope.
  - No contact, automatic status promotion or inference of acceptance from validators
    is authorized.
limitations:
- Detailed pathogen acid-defense, fitness, AMR, antiporter/decarboxylation efficacy
  and intervention or perturbation effects remain UNASSESSED_SCOPE. No repaired mechanism
  or optimized condition is provided.
- Baker full text remains unavailable. The current impermeable-membrane phrase is
  nevertheless exact in the assigned abstract; the attribution concern does not establish
  false biology or whole-paper absence.
- Generic PMF context and its standard-condition approximation do not independently
  calibrate exact numerical growth endpoints or demonstrate universal biological sufficiency.
- Local defines and manifests-as proposals use broad formal endpoints. Their feature/state-to-trait
  wording differs from a hard imported material/process constraint.
- Capacity wording at nodes 2/3 can abbreviate maintenance processes; no automatic
  CAPACITY retype or separate defect is imposed. Free-text edges do not inherit unasserted
  RO constraints.
- The current record, mapping and shared writer are affected owners. A sibling writer,
  positive canonical owner and unrelated facet-maintenance context are not direct
  recurrence owners for the current gradient nodes.
- The target raw METPO term has no textual definition; current wording is a supported
  synthesis. Both direct parents and two explicit replacement links are positive.
- Official species/type aliases and current abstract support NTOU-MSR1T pH range 7–10,
  distinct from optimum 7–8. No full methods or all-strains generalization is claimed.
- Krulwich BioC original acquisition at 07:57:33, taxonomy success at 16:43:16 and
  earlier DNS failure remain distinct from current metadata at 19:34:30, copying and
  selected reading. No source network was repeated by this auditor.
- Catalog absence is bounded to the retained snapshot, and local acceptance search
  does not establish absence of private or remote decisions. Known human concept authorship
  remains positive.
notes:
- Final root adjudication and independent challenge are pinned. Root owns one execution
  after independent static review, followed by native validation, final artifact review
  and save.
- 'Coverage: 4 works, 14 external placements, 2 ontology fields, 11 nodes, 10 edges,
  1 component, 0 protein classes/instances, 6 literal snippets, 1 canonical and 12
  events (11 AI plus seed).'
- Preparation changes no scientific record, Git state, sweep state or native review
  inventory.
tags:
- record-review
- ph-range
- environment
- needs-curation
native_verdict: needs_curation
```
