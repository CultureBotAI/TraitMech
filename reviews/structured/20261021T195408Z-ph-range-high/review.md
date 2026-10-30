# Whole-record review of high pH range

- Review: 20261021T195408Z-ph-range-high
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-21T19:45:19.695714Z
- Finished UTC: 2026-10-21T19:54:08Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Needs curation: one grouped category/complete-interval major and four bounded minors concerning Baker attribution, substrate/executor semantics, carbonate referent and human-acceptance traceability. Active identity, numerical bounds, generic environmental physiology and inorganic-carbon chemistry remain positive.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: Fourth record of the actual batch 011 queue. Whole target read before successful 78-input capture. AEM bibliographic collection began before capture; substantive judgments followed capture verification. Final source/grounding audits, independent challenge and root adjudication are mandatory.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8eee04a8c65609fbaff6df7c54597dcaf1b9d282.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| METPO:1000464 | data/traits/environment/ph_range_high.yaml | maintained | pH range high |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full-corpus graph audit | passed | True | METPO:1000464 | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| Full-corpus snippet audit | passed | True | METPO:1000464 | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| Full-corpus pathway links | passed | True | METPO:1000464 | 19 links checked against the pinned PathwayMech snapshot. |
| Full-corpus history integrity | passed | True | METPO:1000464 | 1277 history records checked, zero invalid links at the 8eee source base; integrity does not establish science or human acceptance. |
| Initial full-product validation | failed | False | METPO:1000464 | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation with isolated local cache | failed | False | METPO:1000464 | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation after isolated-cache download | passed | True | METPO:1000464 | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| Focused native validation | passed | True | METPO:1000464 | Direct successful current-target schema validation; formal roles are assessed separately. |
| Focused strict validation | passed | True | METPO:1000464 | Direct successful current-target strict validation; no biological efficacy certification. |
| Focused snippet verification | passed | True | METPO:1000464 | Four fields over two references, all NOT_IN_ABSTRACT. Retained primary body independently confirms two Krulwich excerpts; two Baker body phrases remain unknown. Original native results are unchanged. |
| Reused maintained batch-ten QC | passed | True | METPO:1000464 | Actual B10 final QC at its original time, qualified against B11 bytes; not a fresh B11 execution. |
| Protein-instance metadata applicability | not_applicable | False | METPO:1000464 | Three reviewed label-only contextual protein classes have no instances; no token accession is required by this measurement graph. |

## Scientific And Domain Assessments

### Native checklist: active bin and inherited aliases

identity: concern. Targets: METPO:1000464.

Active METPO identity, parent, predecessor and inherited text are checked against the pinned ontology. Faithful import of broad category aliases does not establish exact scientific equivalence with a complete growth interval contained within 10–14. Parent authorship is not copied into this target.

### Native checklist: numerical bin versus high-pH occurrence

evidence: concern. Targets: METPO:1000464.

The numerical interval itself is retained. Growing above 10 and belonging to a broad alkaliphile category do not establish a complete growth interval within 10–14. The record’s own canonical deferral preserves that distinction; group its above-10 shorthand and exact synonyms once rather than multiplying findings.

### Native checklist: quantitative environmental range

scope: supported. Targets: METPO:1000464.

ENVIRONMENT, CLASS and NONMECHANISTIC are compatible with the quantitative trait. Generic environmental context is not automatically universal necessity, exact endpoint calibration or proof of complete-bin membership.

### Native checklist: documented canonical gap

evidence: unknown. Targets: METPO:1000464.

No canonical organism is supplied. The existing deferral says above-10 examples can extend below the bin and therefore do not establish a complete contained interval. Preserve that bounded gap; no example, new experiment, optimized condition or substitute organism is required.

### Native checklist: all assigned works and separate supplement

evidence: concern. Targets: METPO:1000464.

Three assigned works resolve across twelve external placements. A separately identified classification supplement informs equivalence only. Baker’s inspected acidophile abstract does not establish the stated extreme-alkaliphile antiporter attribution; this is bounded attribution precision while its full body remains unavailable.

{
  "completed_at": "2026-10-21T19:48:47.211004+00:00",
  "external_placements": [
    {
      "field_path": "definition_source",
      "reference": "DOI:10.1038/nrmicro2549",
      "claim": "A pH range phenotype in which the growth-supporting external pH range spans approximately 10\u201314, characteristic of extreme-alkaliphile physiology.",
      "assessment": "Assigned review supports extreme alkaline growth examples and generic homeostasis. It does not equate all alkaliphiles with a complete growth interval contained10\u201314. Preserve the numerical bin itself and distinguish contextual category/above10 examples from exact bin membership."
    },
    {
      "field_path": "evidence[0]",
      "reference": "DOI:10.1038/nrmicro2549",
      "snippet": "alkaliphiles",
      "notes": "pH-homeostasis review supports extreme-alkaliphile physiology growing at external pH above 10.",
      "assessment": "Exact alkaliphiles occurrence and source-specific above10 context positive; this alone is not complete interval membership."
    },
    {
      "field_path": "evidence[1]",
      "reference": "DOI:10.1016/j.tim.2007.02.005",
      "snippet": "proton motive force",
      "notes": "pH-homeostasis review supports robust Na+/H+ antiporter activity as the extreme-alkaliphile mechanism sustaining the proton motive force above pH 10.",
      "assessment": "The inspected Baker abstract is acidophile-scoped. The alkaline antiporter attribution exceeds that inspected scope; bounded attribution precision only, not a full-paper absence or false-mechanism judgment."
    },
    {
      "field_path": "causal_graphs[0].edges[0].evidence[0]",
      "reference": "DOI:10.1016/j.tim.2007.02.005",
      "snippet": "proton motive force",
      "notes": "Supports antiporter-driven proton re-import as the extreme-alkaliphile mechanism.",
      "assessment": "Assigned Baker identity and acidophile abstract are verified, but the exact PMF snippet/body and alkaline antiporter attribution are not established by the inspected Baker surface. Krulwich separately supports generic environmental alkaline antiport context; that support is not silently transferred into the Baker citation. Above10 alone is not equivalent to a complete growth interval within10\u201314."
    },
    {
      "field_path": "causal_graphs[0].edges[1].evidence[0]",
      "reference": "DOI:10.1038/nrmicro2549",
      "snippet": "alkaliphiles",
      "notes": "Supports the pH 10\u201314 range as a value within the pH-range distribution.",
      "assessment": "Formal parent/bin hierarchy is an ontology question. Assigned Krulwich literal alkaliphiles context is positive, but the short excerpt does not calibrate this exact complete-interval category."
    },
    {
      "field_path": "causal_graphs[0].edges[2].evidence[0]",
      "reference": "DOI:10.1038/nrmicro2549",
      "notes": "The unusual hetero-oligomeric Mrp antiporter has an indispensable role at high pH.",
      "assessment": "Krulwich BioC40107 first two sentences directly discuss Mrp in extremely alkaliphilic Bacillus. Positive existing contextual attribution; preserve organism scope and do not assert necessity in every lineage or exact interval membership. Later mutation/mechanistic passages are unassessed."
    },
    {
      "field_path": "causal_graphs[0].edges[3].evidence[0]",
      "reference": "DOI:10.1038/nrmicro2549",
      "notes": "A large transmembrane potential is essential to drive electrogenic Na+/H+ and K+/H+ antiporters that import H+.",
      "assessment": "Krulwich BioC2440/3940 supports generic PMF electrical-component and condition-specific environmental context. The exact essential-potential sentence was not independently established in this selected-body window; that precision remains limited, not false. Detailed efficacy and new mechanistic repair are unassessed."
    },
    {
      "field_path": "causal_graphs[0].edges[4].evidence[0]",
      "reference": "DOI:10.1038/nrmicro2549",
      "notes": "The ongoing requirement for cytoplasmic Na+ to support high levels of alkaliphile antiport activity is met by numerous Na+/solute symporters.",
      "assessment": "Krulwich BioC41582 first sentence supports the existing Na+/solute symporter context for alkaliphile antiport. This generic contextual support does not certify every lineage or a complete10\u201314 interval."
    },
    {
      "field_path": "causal_graphs[0].edges[5].evidence[0]",
      "reference": "DOI:10.1038/nrmicro2549",
      "notes": "Cytoplasmic Na+ is required to support high levels of alkaliphile antiport activity.",
      "assessment": "Same existing BioC41582 context supports substrate availability wording. Formal executor-versus-substrate relation semantics are separately assessed by grounding; no new biological mechanism or efficacy test proposed."
    },
    {
      "field_path": "causal_graphs[0].edges[6].evidence[0]",
      "reference": "DOI:10.1038/nrmicro2549",
      "notes": "The proton uptake that accompanies ATP synthesis by the F1Fo-ATP synthase contributes to alkaliphile pH homeostasis.",
      "assessment": "Krulwich BioC42119 first sentence directly supports proton uptake during ATP synthesis contributing to pH homeostasis in aerobic alkaliphilic Bacillus. Preserve that source-specific context; later motif/mutation/optimization passages unassessed."
    },
    {
      "field_path": "causal_graphs[0].edges[7].evidence[0]",
      "reference": "DOI:10.1038/nrmicro2549",
      "notes": "Alkaline pH homeostasis underlies extreme-alkaliphile growth above pH 10.",
      "assessment": "Assigned generic environmental pH-homeostasis context positive. Growth above10 alone and complete growth interval10\u201314 are distinct, so this branch is not direct calibration of the full interval; group that scope issue with exact-category aliases."
    },
    {
      "field_path": "causal_graphs[0].edges[8].evidence[0]",
      "reference": "DOI:10.1128/AEM.01557-23",
      "notes": "DIC speciation shifts strongly with pH, toward CO3= above ~10.3.",
      "assessment": "Assigned AEM actual JATS body paragraph22 explicitly states carbonate predominates above about pH10.3. Positive existing inorganic-carbon chemistry; model/application/genome-toolkit methods and engineering implications are not assessed. No numerical correction or new experimental condition is proposed."
    }
  ],
  "ontology_grounding_fields": [
    {
      "field_path": "causal_graphs[0].nodes[0].grounding",
      "reference": "METPO:1000464"
    },
    {
      "field_path": "causal_graphs[0].nodes[1].grounding",
      "reference": "METPO:1000332"
    }
  ],
  "synonym_source_fields": [
    {
      "field_path": "synonyms[0]",
      "synonym": {
        "synonym_text": "Alkali Tolerant",
        "synonym_type": "EXACT_SYNONYM",
        "source": "metpo.owl"
      }
    },
    {
      "field_path": "synonyms[1]",
      "synonym": {
        "synonym_text": "Alkaliphile",
        "synonym_type": "EXACT_SYNONYM",
        "source": "metpo.owl"
      }
    },
    {
      "field_path": "synonyms[2]",
      "synonym": {
        "synonym_text": "Extreme Alkaliphile",
        "synonym_type": "EXACT_SYNONYM",
        "source": "metpo.owl"
      }
    },
    {
      "field_path": "synonyms[3]",
      "synonym": {
        "synonym_text": "10_to_14",
        "synonym_type": "RELATED_SYNONYM",
        "source": "metpo.owl"
      }
    }
  ],
  "scope": "Three assigned external works across12 placements; separate supplemental classification source used only for auditing equivalence. Two structured node grounds and four synonym provenance fields are tracked separately."
}

### Native checklist: all four current excerpts

evidence: unknown. Targets: METPO:1000464.

Both Krulwich alkaliphiles occurrences are literal in retained primary body. Both Baker proton-motive-force phrases remain body-unverified. Native four NOT_IN_ABSTRACT is retained; unavailable assigned body is not evidence of a false quotation, and occurrence in another source is not silently transferred.

{
  "completed_at": "2026-10-21T19:48:47.212874+00:00",
  "snippets": [
    {
      "field_path": "evidence[0].snippet",
      "reference": "DOI:10.1038/nrmicro2549",
      "snippet": "alkaliphiles",
      "outcome": "literal_exact",
      "hits": [
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/krulwich-bioc.xml",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
          "locator": "passage offset 5466"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/krulwich-bioc.xml",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
          "locator": "passage offset 15130"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/krulwich-bioc.xml",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
          "locator": "passage offset 16479"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/krulwich-bioc.xml",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
          "locator": "passage offset 39232"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/krulwich-bioc.xml",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
          "locator": "passage offset 39253"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/krulwich-bioc.xml",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
          "locator": "passage offset 41582"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/krulwich-bioc.xml",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
          "locator": "passage offset 42119"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/krulwich-bioc.xml",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
          "locator": "passage offset 45597"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/krulwich-bioc.xml",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
          "locator": "passage offset 61656"
        }
      ],
      "scope": "Literal occurrence only. Missing abstract match with unavailable assigned body is unknown, not a false-quote finding."
    },
    {
      "field_path": "evidence[1].snippet",
      "reference": "DOI:10.1016/j.tim.2007.02.005",
      "snippet": "proton motive force",
      "outcome": "body_unknown",
      "hits": [],
      "scope": "Literal occurrence only. Missing abstract match with unavailable assigned body is unknown, not a false-quote finding."
    },
    {
      "field_path": "causal_graphs[0].edges[0].evidence[0].snippet",
      "reference": "DOI:10.1016/j.tim.2007.02.005",
      "snippet": "proton motive force",
      "outcome": "body_unknown",
      "hits": [],
      "scope": "Literal occurrence only. Missing abstract match with unavailable assigned body is unknown, not a false-quote finding."
    },
    {
      "field_path": "causal_graphs[0].edges[1].evidence[0].snippet",
      "reference": "DOI:10.1038/nrmicro2549",
      "snippet": "alkaliphiles",
      "outcome": "literal_exact",
      "hits": [
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/krulwich-bioc.xml",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
          "locator": "passage offset 5466"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/krulwich-bioc.xml",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
          "locator": "passage offset 15130"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/krulwich-bioc.xml",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
          "locator": "passage offset 16479"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/krulwich-bioc.xml",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
          "locator": "passage offset 39232"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/krulwich-bioc.xml",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
          "locator": "passage offset 39253"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/krulwich-bioc.xml",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
          "locator": "passage offset 41582"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/krulwich-bioc.xml",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
          "locator": "passage offset 42119"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/krulwich-bioc.xml",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
          "locator": "passage offset 45597"
        },
        {
          "surface": "retained BioC",
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/krulwich-bioc.xml",
          "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
          "locator": "passage offset 61656"
        }
      ],
      "scope": "Literal occurrence only. Missing abstract match with unavailable assigned body is unknown, not a false-quote finding."
    }
  ],
  "counts": {
    "fields": 4,
    "literal_exact": 2,
    "body_unknown": 2
  },
  "native_result": {
    "verified": 0,
    "not_in_abstract": 4
  },
  "qualification": "Both Krulwich alkaliphiles occurrences are exact in retained body. Both Baker proton-motive-force occurrences remain unverified because assigned body is unavailable; occurrence elsewhere is not transferred between sources."
}

### Native checklist: all current node referents

grounding: concern. Targets: METPO:1000464.

All eleven nodes are assessed. Three contextual protein/complex classes are label-only and the sodium pool is material. Carbonate node 10 combines a material label/type with a description of a speciation shift; retain that bounded precision concern without diagnosing false chemistry.

[
  {
    "index": 0,
    "field_path": "causal_graphs[0].nodes[0]",
    "current": {
      "node_id": "ph_range_high_trait",
      "label": "pH range high",
      "node_type": "TRAIT",
      "grounding": "METPO:1000464",
      "description": "pH growth-supporting range extending above ~10."
    },
    "status": "scope_finding",
    "assessment": "Active trait identity is correct. The description extends the range above approximately 10, which is weaker than the complete-interval convention stated in the current canonical deferral. This is grouped with exact category aliases, not a second numerical-OWL error."
  },
  {
    "index": 1,
    "field_path": "causal_graphs[0].nodes[1]",
    "current": {
      "node_id": "ph_range",
      "label": "pH range",
      "node_type": "TRAIT",
      "grounding": "METPO:1000332",
      "description": "Span of external pH values supporting growth."
    },
    "status": "supported",
    "assessment": "Current pH range parent identity and span meaning agree with the imported hierarchy."
  },
  {
    "index": 2,
    "field_path": "causal_graphs[0].nodes[2]",
    "current": {
      "node_id": "extreme_alkaliphile_antiport",
      "label": "extreme-alkaliphile Na+/H+ antiport",
      "node_type": "BIOLOGICAL_PROCESS",
      "description": "Robust Na+/H+ antiporter activity importing H+ at strongly alkaline external pH."
    },
    "status": "supported_facet",
    "assessment": "The node explicitly denotes antiport activity; BIOLOGICAL_PROCESS is a coherent process facet. Detailed efficacy is outside this documentary assessment."
  },
  {
    "index": 3,
    "field_path": "causal_graphs[0].nodes[3]",
    "current": {
      "node_id": "mrp_antiporter_complex",
      "label": "Mrp Na+/H+ antiporter complex",
      "node_type": "GENE_OR_PROTEIN",
      "grounding_status": "REVIEWED_LABEL_ONLY",
      "grounding_notes": "Reviewed as a contextual protein or protein-complex label within a quantitative measurement graph; no exact semantic family term was established for this aggregate use.",
      "description": "Hetero-oligomeric CPA3-family Na+/H+ antiporter complex essential at high external pH.",
      "gene_symbols": [
        "mrpA",
        "mrpB",
        "mrpC",
        "mrpD",
        "mrpE",
        "mrpF",
        "mrpG"
      ],
      "operon": "mrpA-G"
    },
    "status": "supported_facet",
    "assessment": "Material protein-complex class is coherent. Gene symbols and operon metadata do not make a separate genetic-element node mandatory. Reviewed label-only disposition is explicit."
  },
  {
    "index": 4,
    "field_path": "causal_graphs[0].nodes[4]",
    "current": {
      "node_id": "membrane_potential",
      "label": "transmembrane potential (delta-psi)",
      "node_type": "QUALITY",
      "description": "Large transmembrane electrical potential energizing electrogenic cation/H+ antiport."
    },
    "status": "supported_facet",
    "assessment": "An electrical potential can be represented as a measurable QUALITY. The STATE alternative does not establish an automatic typing error."
  },
  {
    "index": 5,
    "field_path": "causal_graphs[0].nodes[5]",
    "current": {
      "node_id": "na_solute_symporters",
      "label": "Na+/solute symporters",
      "node_type": "GENE_OR_PROTEIN",
      "grounding_status": "REVIEWED_LABEL_ONLY",
      "grounding_notes": "Reviewed as a contextual protein or protein-complex label within a quantitative measurement graph; no exact semantic family term was established for this aggregate use.",
      "description": "Symporters re-importing Na+ with solutes to supply cytoplasmic Na+ for antiport."
    },
    "status": "supported_facet",
    "assessment": "Material symporter protein class and reviewed label-only disposition are coherent; no mandatory instance or functional grounding is inferred."
  },
  {
    "index": 6,
    "field_path": "causal_graphs[0].nodes[6]",
    "current": {
      "node_id": "cytoplasmic_na",
      "label": "cytoplasmic Na+",
      "node_type": "CHEMICAL",
      "description": "Intracellular sodium pool required to sustain alkaliphile antiport activity."
    },
    "status": "supported_facet",
    "assessment": "The intracellular sodium pool has a material chemical referent. No blanket CHEMICAL exclusion applies to causal executor relations."
  },
  {
    "index": 7,
    "field_path": "causal_graphs[0].nodes[7]",
    "current": {
      "node_id": "f1fo_atp_synthase",
      "label": "F1Fo-ATP synthase",
      "node_type": "GENE_OR_PROTEIN",
      "grounding_status": "REVIEWED_LABEL_ONLY",
      "grounding_notes": "Reviewed as a contextual protein or protein-complex label within a quantitative measurement graph; no exact semantic family term was established for this aggregate use.",
      "description": "Proton-translocating ATP synthase whose proton uptake contributes to pH homeostasis."
    },
    "status": "supported_facet",
    "assessment": "ATP synthase is a material protein complex, and the label-only disposition is explicit."
  },
  {
    "index": 8,
    "field_path": "causal_graphs[0].nodes[8]",
    "current": {
      "node_id": "alkaline_ph_homeostasis",
      "label": "alkaline pH homeostasis",
      "node_type": "BIOLOGICAL_PROCESS",
      "description": "Maintenance of a near-neutral cytoplasmic pH against a strongly alkaline exterior."
    },
    "status": "supported_facet",
    "assessment": "The description explicitly denotes maintenance, supporting a process reading. Source-specific physiological scope remains separate from ontology endpoint checks."
  },
  {
    "index": 9,
    "field_path": "causal_graphs[0].nodes[9]",
    "current": {
      "node_id": "external_ph_high",
      "label": "external pH &gt; 10.3",
      "node_type": "ENVIRONMENTAL_FACTOR",
      "description": "Strongly alkaline external pH above ~10.3."
    },
    "status": "supported_facet",
    "assessment": "External high pH is an environmental condition, and its current free-text relation does not import a process-domain restriction."
  },
  {
    "index": 10,
    "field_path": "causal_graphs[0].nodes[10]",
    "current": {
      "node_id": "carbonate_speciation",
      "label": "carbonate (CO3 2-) speciation",
      "node_type": "CHEMICAL",
      "description": "Shift of dissolved inorganic carbon toward carbonate at high pH."
    },
    "status": "minor_precision_candidate",
    "assessment": "CHEMICAL can denote carbonate material, but both the label and description also describe speciation or a shift in speciation. Clarify the intended material versus change referent without requiring a particular replacement enum or denying the source chemistry."
  }
]

### Native checklist: all nine formal and descriptive roles

consistency: concern. Targets: METPO:1000464.

Both imported RO relations have compatible material/process endpoints. Edge 5 nevertheless uses enables for a substrate pool, raising bounded executor-versus-substrate precision. Edge 6 is positive. Local confers and free-text relations receive no invented formal endpoint constraints; bin-membership support remains the separate grouped scope issue.

[
  {
    "index": 0,
    "field_path": "causal_graphs[0].edges[0]",
    "current": {
      "subject": "extreme_alkaliphile_antiport",
      "predicate": "confers",
      "object": "ph_range_high_trait",
      "description": "Robust Na+/H+ antiport enables growth at pH &gt; 10.",
      "evidence": [
        {
          "reference": "DOI:10.1016/j.tim.2007.02.005",
          "snippet": "proton motive force",
          "notes": "Supports antiporter-driven proton re-import as the extreme-alkaliphile mechanism."
        }
      ],
      "predicate_id": "METPO:2007700"
    },
    "status": "scope_finding",
    "assessment": "The local confers domain and range admit these causal nodes. Growth above 10 alone is weaker than membership under the current complete-interval convention; this is part of the grouped scope finding."
  },
  {
    "index": 1,
    "field_path": "causal_graphs[0].edges[1]",
    "current": {
      "subject": "ph_range_high_trait",
      "predicate": "is a",
      "object": "ph_range",
      "description": "pH range high is a quantitative bin of the pH-range phenotype.",
      "evidence": [
        {
          "reference": "DOI:10.1038/nrmicro2549",
          "snippet": "alkaliphiles",
          "notes": "Supports the pH 10\u201314 range as a value within the pH-range distribution."
        }
      ],
      "predicate_id": "rdfs:subClassOf"
    },
    "status": "supported_relation_scope_limit",
    "assessment": "The rdfs subclass relation and parent identity are correct. The assigned source note treating 10\u201314 as the source-supported range is part of the same bin-scope question, not a second hierarchy failure."
  },
  {
    "index": 2,
    "field_path": "causal_graphs[0].edges[2]",
    "current": {
      "subject": "mrp_antiporter_complex",
      "predicate": "confers",
      "object": "ph_range_high_trait",
      "description": "The hetero-oligomeric Mrp antiporter has an indispensable role in growth at high pH.",
      "evidence": [
        {
          "reference": "DOI:10.1038/nrmicro2549",
          "notes": "The unusual hetero-oligomeric Mrp antiporter has an indispensable role at high pH."
        }
      ],
      "predicate_id": "METPO:2007700"
    },
    "status": "scope_finding",
    "assessment": "The protein-to-trait confers endpoints fit the local broad relation. Generic high-pH context does not by itself establish the current complete-interval bin."
  },
  {
    "index": 3,
    "field_path": "causal_graphs[0].edges[3]",
    "current": {
      "subject": "membrane_potential",
      "predicate": "drives",
      "object": "mrp_antiporter_complex",
      "description": "A large transmembrane potential drives electrogenic Na+/H+ antiport that imports H+.",
      "evidence": [
        {
          "reference": "DOI:10.1038/nrmicro2549",
          "notes": "A large transmembrane potential is essential to drive electrogenic Na+/H+ and K+/H+ antiporters that import H+."
        }
      ]
    },
    "status": "supported_formal_scope",
    "assessment": "Free-text drives has no imported domain or range in this edge. The QUALITY subject is not an automatic error; detailed efficacy is unassessed."
  },
  {
    "index": 4,
    "field_path": "causal_graphs[0].edges[4]",
    "current": {
      "subject": "na_solute_symporters",
      "predicate": "supplies",
      "object": "cytoplasmic_na",
      "description": "Na+/solute symporters supply the cytoplasmic Na+ required to sustain antiport activity.",
      "evidence": [
        {
          "reference": "DOI:10.1038/nrmicro2549",
          "notes": "The ongoing requirement for cytoplasmic Na+ to support high levels of alkaliphile antiport activity is met by numerous Na+/solute symporters."
        }
      ]
    },
    "status": "supported_formal_scope",
    "assessment": "Free-text supplies has no imported domain or range in this edge. Material actor and chemical pool are coherent documentary referents."
  },
  {
    "index": 5,
    "field_path": "causal_graphs[0].edges[5]",
    "current": {
      "subject": "cytoplasmic_na",
      "predicate": "enables",
      "object": "extreme_alkaliphile_antiport",
      "description": "Cytoplasmic Na+ is the substrate that sustains high levels of alkaliphile antiport activity.",
      "evidence": [
        {
          "reference": "DOI:10.1038/nrmicro2549",
          "notes": "Cytoplasmic Na+ is required to support high levels of alkaliphile antiport activity."
        }
      ],
      "predicate_id": "RO:0002327"
    },
    "status": "minor_semantic_precision_candidate",
    "assessment": "RO:0002327 admits a material subject and process object here. Its definition additionally says the subject acts to execute the process, while this record expressly calls sodium the substrate. This is a bounded executor-versus-substrate precision issue, not a categorical type error or a denial that sodium supports the process."
  },
  {
    "index": 6,
    "field_path": "causal_graphs[0].edges[6]",
    "current": {
      "subject": "f1fo_atp_synthase",
      "predicate": "contributes to",
      "object": "alkaline_ph_homeostasis",
      "description": "Proton uptake accompanying ATP synthesis contributes to alkaliphile pH homeostasis.",
      "evidence": [
        {
          "reference": "DOI:10.1038/nrmicro2549",
          "notes": "The proton uptake that accompanies ATP synthesis by the F1Fo-ATP synthase contributes to alkaliphile pH homeostasis."
        }
      ],
      "predicate_id": "RO:0002326"
    },
    "status": "supported_formal_scope",
    "assessment": "The material ATP-synthase subject and maintenance-process object satisfy the actual inherited RO:0002326 endpoint constraints. The annotation usage note is not a global molecular-function-only range restriction."
  },
  {
    "index": 7,
    "field_path": "causal_graphs[0].edges[7]",
    "current": {
      "subject": "alkaline_ph_homeostasis",
      "predicate": "confers",
      "object": "ph_range_high_trait",
      "description": "Maintenance of cytoplasmic pH homeostasis enables growth at strongly alkaline external pH.",
      "evidence": [
        {
          "reference": "DOI:10.1038/nrmicro2549",
          "notes": "Alkaline pH homeostasis underlies extreme-alkaliphile growth above pH 10."
        }
      ],
      "predicate_id": "METPO:2007700"
    },
    "status": "scope_finding",
    "assessment": "Local confers admits the process and trait endpoints. The above-10 biological context is weaker than the complete-interval bin and is grouped with the same scope finding."
  },
  {
    "index": 8,
    "field_path": "causal_graphs[0].edges[8]",
    "current": {
      "subject": "external_ph_high",
      "predicate": "shifts speciation toward",
      "object": "carbonate_speciation",
      "description": "External pH above ~10.3 shifts dissolved inorganic carbon speciation toward carbonate.",
      "evidence": [
        {
          "reference": "DOI:10.1128/AEM.01557-23",
          "notes": "DIC speciation shifts strongly with pH, toward CO3= above ~10.3."
        }
      ]
    },
    "status": "minor_node_facet_context",
    "assessment": "The free-text predicate can target carbonate material. Node 10 wording also describes a shift, so the minor concerns referent clarity rather than an imported formal constraint or false chemistry."
  }
]

### Native checklist: generic environmental and inorganic-carbon support

scope: unknown. Targets: METPO:1000464.

Selected source-specific Bacillus homeostasis context and the AEM carbonate chemistry are positive. Detailed pathogen defense, fitness, AMR, mutation/perturbation efficacy, engineering and intervention optimization remain UNASSESSED_SCOPE. No new biological route, repair or experimental recommendation is supplied.

{
  "completed_at": "2026-10-21T19:48:47.211139+00:00",
  "edges": [
    {
      "index": 0,
      "field_path": "causal_graphs[0].edges[0]",
      "subject": "extreme_alkaliphile_antiport",
      "predicate": "confers",
      "predicate_id": "METPO:2007700",
      "object": "ph_range_high_trait",
      "description": "Robust Na+/H+ antiport enables growth at pH &gt; 10.",
      "evidence": [
        {
          "reference": "DOI:10.1016/j.tim.2007.02.005",
          "snippet": "proton motive force",
          "notes": "Supports antiporter-driven proton re-import as the extreme-alkaliphile mechanism."
        }
      ],
      "assessment": "Assigned Baker identity and acidophile abstract are verified, but the exact PMF snippet/body and alkaline antiporter attribution are not established by the inspected Baker surface. Krulwich separately supports generic environmental alkaline antiport context; that support is not silently transferred into the Baker citation. Above10 alone is not equivalent to a complete growth interval within10\u201314.",
      "scope": "Generic existing environmental context/documentary attribution; no detailed pathogen defense/fitness/AMR, perturbation efficacy or optimization."
    },
    {
      "index": 1,
      "field_path": "causal_graphs[0].edges[1]",
      "subject": "ph_range_high_trait",
      "predicate": "is a",
      "predicate_id": "rdfs:subClassOf",
      "object": "ph_range",
      "description": "pH range high is a quantitative bin of the pH-range phenotype.",
      "evidence": [
        {
          "reference": "DOI:10.1038/nrmicro2549",
          "snippet": "alkaliphiles",
          "notes": "Supports the pH 10\u201314 range as a value within the pH-range distribution."
        }
      ],
      "assessment": "Formal parent/bin hierarchy is an ontology question. Assigned Krulwich literal alkaliphiles context is positive, but the short excerpt does not calibrate this exact complete-interval category.",
      "scope": "Generic existing environmental context/documentary attribution; no detailed pathogen defense/fitness/AMR, perturbation efficacy or optimization."
    },
    {
      "index": 2,
      "field_path": "causal_graphs[0].edges[2]",
      "subject": "mrp_antiporter_complex",
      "predicate": "confers",
      "predicate_id": "METPO:2007700",
      "object": "ph_range_high_trait",
      "description": "The hetero-oligomeric Mrp antiporter has an indispensable role in growth at high pH.",
      "evidence": [
        {
          "reference": "DOI:10.1038/nrmicro2549",
          "notes": "The unusual hetero-oligomeric Mrp antiporter has an indispensable role at high pH."
        }
      ],
      "assessment": "Krulwich BioC40107 first two sentences directly discuss Mrp in extremely alkaliphilic Bacillus. Positive existing contextual attribution; preserve organism scope and do not assert necessity in every lineage or exact interval membership. Later mutation/mechanistic passages are unassessed.",
      "scope": "Generic existing environmental context/documentary attribution; no detailed pathogen defense/fitness/AMR, perturbation efficacy or optimization."
    },
    {
      "index": 3,
      "field_path": "causal_graphs[0].edges[3]",
      "subject": "membrane_potential",
      "predicate": "drives",
      "predicate_id": null,
      "object": "mrp_antiporter_complex",
      "description": "A large transmembrane potential drives electrogenic Na+/H+ antiport that imports H+.",
      "evidence": [
        {
          "reference": "DOI:10.1038/nrmicro2549",
          "notes": "A large transmembrane potential is essential to drive electrogenic Na+/H+ and K+/H+ antiporters that import H+."
        }
      ],
      "assessment": "Krulwich BioC2440/3940 supports generic PMF electrical-component and condition-specific environmental context. The exact essential-potential sentence was not independently established in this selected-body window; that precision remains limited, not false. Detailed efficacy and new mechanistic repair are unassessed.",
      "scope": "Generic existing environmental context/documentary attribution; no detailed pathogen defense/fitness/AMR, perturbation efficacy or optimization."
    },
    {
      "index": 4,
      "field_path": "causal_graphs[0].edges[4]",
      "subject": "na_solute_symporters",
      "predicate": "supplies",
      "predicate_id": null,
      "object": "cytoplasmic_na",
      "description": "Na+/solute symporters supply the cytoplasmic Na+ required to sustain antiport activity.",
      "evidence": [
        {
          "reference": "DOI:10.1038/nrmicro2549",
          "notes": "The ongoing requirement for cytoplasmic Na+ to support high levels of alkaliphile antiport activity is met by numerous Na+/solute symporters."
        }
      ],
      "assessment": "Krulwich BioC41582 first sentence supports the existing Na+/solute symporter context for alkaliphile antiport. This generic contextual support does not certify every lineage or a complete10\u201314 interval.",
      "scope": "Generic existing environmental context/documentary attribution; no detailed pathogen defense/fitness/AMR, perturbation efficacy or optimization."
    },
    {
      "index": 5,
      "field_path": "causal_graphs[0].edges[5]",
      "subject": "cytoplasmic_na",
      "predicate": "enables",
      "predicate_id": "RO:0002327",
      "object": "extreme_alkaliphile_antiport",
      "description": "Cytoplasmic Na+ is the substrate that sustains high levels of alkaliphile antiport activity.",
      "evidence": [
        {
          "reference": "DOI:10.1038/nrmicro2549",
          "notes": "Cytoplasmic Na+ is required to support high levels of alkaliphile antiport activity."
        }
      ],
      "assessment": "Same existing BioC41582 context supports substrate availability wording. Formal executor-versus-substrate relation semantics are separately assessed by grounding; no new biological mechanism or efficacy test proposed.",
      "scope": "Generic existing environmental context/documentary attribution; no detailed pathogen defense/fitness/AMR, perturbation efficacy or optimization."
    },
    {
      "index": 6,
      "field_path": "causal_graphs[0].edges[6]",
      "subject": "f1fo_atp_synthase",
      "predicate": "contributes to",
      "predicate_id": "RO:0002326",
      "object": "alkaline_ph_homeostasis",
      "description": "Proton uptake accompanying ATP synthesis contributes to alkaliphile pH homeostasis.",
      "evidence": [
        {
          "reference": "DOI:10.1038/nrmicro2549",
          "notes": "The proton uptake that accompanies ATP synthesis by the F1Fo-ATP synthase contributes to alkaliphile pH homeostasis."
        }
      ],
      "assessment": "Krulwich BioC42119 first sentence directly supports proton uptake during ATP synthesis contributing to pH homeostasis in aerobic alkaliphilic Bacillus. Preserve that source-specific context; later motif/mutation/optimization passages unassessed.",
      "scope": "Generic existing environmental context/documentary attribution; no detailed pathogen defense/fitness/AMR, perturbation efficacy or optimization."
    },
    {
      "index": 7,
      "field_path": "causal_graphs[0].edges[7]",
      "subject": "alkaline_ph_homeostasis",
      "predicate": "confers",
      "predicate_id": "METPO:2007700",
      "object": "ph_range_high_trait",
      "description": "Maintenance of cytoplasmic pH homeostasis enables growth at strongly alkaline external pH.",
      "evidence": [
        {
          "reference": "DOI:10.1038/nrmicro2549",
          "notes": "Alkaline pH homeostasis underlies extreme-alkaliphile growth above pH 10."
        }
      ],
      "assessment": "Assigned generic environmental pH-homeostasis context positive. Growth above10 alone and complete growth interval10\u201314 are distinct, so this branch is not direct calibration of the full interval; group that scope issue with exact-category aliases.",
      "scope": "Generic existing environmental context/documentary attribution; no detailed pathogen defense/fitness/AMR, perturbation efficacy or optimization."
    },
    {
      "index": 8,
      "field_path": "causal_graphs[0].edges[8]",
      "subject": "external_ph_high",
      "predicate": "shifts speciation toward",
      "predicate_id": null,
      "object": "carbonate_speciation",
      "description": "External pH above ~10.3 shifts dissolved inorganic carbon speciation toward carbonate.",
      "evidence": [
        {
          "reference": "DOI:10.1128/AEM.01557-23",
          "notes": "DIC speciation shifts strongly with pH, toward CO3= above ~10.3."
        }
      ],
      "assessment": "Assigned AEM actual JATS body paragraph22 explicitly states carbonate predominates above about pH10.3. Positive existing inorganic-carbon chemistry; model/application/genome-toolkit methods and engineering implications are not assessed. No numerical correction or new experimental condition is proposed.",
      "scope": "Generic existing environmental context/documentary attribution; no detailed pathogen defense/fitness/AMR, perturbation efficacy or optimization."
    }
  ]
}

### Native checklist: current graph and optional evidence

completeness: supported. Targets: METPO:1000464.

All eleven nodes, nine edges, two components, four excerpts and ten record events are covered. Three reviewed label-only protein classes and zero instances are appropriate contextual representation. The explicit canonical gap, lack of token accessions or additional connectors is not an automatic completeness defect.

{
  "completed_at": "2026-10-21T19:48:47.211294+00:00",
  "nodes": [
    {
      "index": 0,
      "field_path": "causal_graphs[0].nodes[0]",
      "node": {
        "node_id": "ph_range_high_trait",
        "label": "pH range high",
        "node_type": "TRAIT",
        "grounding": "METPO:1000464",
        "description": "pH growth-supporting range extending above ~10."
      },
      "incident_edges": [
        0,
        1,
        2,
        7
      ],
      "references": [
        "DOI:10.1016/j.tim.2007.02.005",
        "DOI:10.1038/nrmicro2549"
      ],
      "assessment": "All current incident source placements accounted for. The above10 description is broader than the complete-interval10\u201314 convention; grouped with synonym/bin scope."
    },
    {
      "index": 1,
      "field_path": "causal_graphs[0].nodes[1]",
      "node": {
        "node_id": "ph_range",
        "label": "pH range",
        "node_type": "TRAIT",
        "grounding": "METPO:1000332",
        "description": "Span of external pH values supporting growth."
      },
      "incident_edges": [
        1
      ],
      "references": [
        "DOI:10.1038/nrmicro2549"
      ],
      "assessment": "All current incident source placements accounted for. Generic contextual physiology and identity only; detailed intervention/defense efficacy unassessed. No universal mechanism or exact interval membership is inferred from a node label."
    },
    {
      "index": 2,
      "field_path": "causal_graphs[0].nodes[2]",
      "node": {
        "node_id": "extreme_alkaliphile_antiport",
        "label": "extreme-alkaliphile Na+/H+ antiport",
        "node_type": "BIOLOGICAL_PROCESS",
        "description": "Robust Na+/H+ antiporter activity importing H+ at strongly alkaline external pH."
      },
      "incident_edges": [
        0,
        5
      ],
      "references": [
        "DOI:10.1016/j.tim.2007.02.005",
        "DOI:10.1038/nrmicro2549"
      ],
      "assessment": "All current incident source placements accounted for. Generic contextual physiology and identity only; detailed intervention/defense efficacy unassessed. No universal mechanism or exact interval membership is inferred from a node label."
    },
    {
      "index": 3,
      "field_path": "causal_graphs[0].nodes[3]",
      "node": {
        "node_id": "mrp_antiporter_complex",
        "label": "Mrp Na+/H+ antiporter complex",
        "node_type": "GENE_OR_PROTEIN",
        "grounding_status": "REVIEWED_LABEL_ONLY",
        "grounding_notes": "Reviewed as a contextual protein or protein-complex label within a quantitative measurement graph; no exact semantic family term was established for this aggregate use.",
        "description": "Hetero-oligomeric CPA3-family Na+/H+ antiporter complex essential at high external pH.",
        "gene_symbols": [
          "mrpA",
          "mrpB",
          "mrpC",
          "mrpD",
          "mrpE",
          "mrpF",
          "mrpG"
        ],
        "operon": "mrpA-G"
      },
      "incident_edges": [
        2,
        3
      ],
      "references": [
        "DOI:10.1038/nrmicro2549"
      ],
      "assessment": "All current incident source placements accounted for. Generic contextual physiology and identity only; detailed intervention/defense efficacy unassessed. No universal mechanism or exact interval membership is inferred from a node label."
    },
    {
      "index": 4,
      "field_path": "causal_graphs[0].nodes[4]",
      "node": {
        "node_id": "membrane_potential",
        "label": "transmembrane potential (delta-psi)",
        "node_type": "QUALITY",
        "description": "Large transmembrane electrical potential energizing electrogenic cation/H+ antiport."
      },
      "incident_edges": [
        3
      ],
      "references": [
        "DOI:10.1038/nrmicro2549"
      ],
      "assessment": "All current incident source placements accounted for. Generic contextual physiology and identity only; detailed intervention/defense efficacy unassessed. No universal mechanism or exact interval membership is inferred from a node label."
    },
    {
      "index": 5,
      "field_path": "causal_graphs[0].nodes[5]",
      "node": {
        "node_id": "na_solute_symporters",
        "label": "Na+/solute symporters",
        "node_type": "GENE_OR_PROTEIN",
        "grounding_status": "REVIEWED_LABEL_ONLY",
        "grounding_notes": "Reviewed as a contextual protein or protein-complex label within a quantitative measurement graph; no exact semantic family term was established for this aggregate use.",
        "description": "Symporters re-importing Na+ with solutes to supply cytoplasmic Na+ for antiport."
      },
      "incident_edges": [
        4
      ],
      "references": [
        "DOI:10.1038/nrmicro2549"
      ],
      "assessment": "All current incident source placements accounted for. Generic contextual physiology and identity only; detailed intervention/defense efficacy unassessed. No universal mechanism or exact interval membership is inferred from a node label."
    },
    {
      "index": 6,
      "field_path": "causal_graphs[0].nodes[6]",
      "node": {
        "node_id": "cytoplasmic_na",
        "label": "cytoplasmic Na+",
        "node_type": "CHEMICAL",
        "description": "Intracellular sodium pool required to sustain alkaliphile antiport activity."
      },
      "incident_edges": [
        4,
        5
      ],
      "references": [
        "DOI:10.1038/nrmicro2549"
      ],
      "assessment": "All current incident source placements accounted for. Generic contextual physiology and identity only; detailed intervention/defense efficacy unassessed. No universal mechanism or exact interval membership is inferred from a node label."
    },
    {
      "index": 7,
      "field_path": "causal_graphs[0].nodes[7]",
      "node": {
        "node_id": "f1fo_atp_synthase",
        "label": "F1Fo-ATP synthase",
        "node_type": "GENE_OR_PROTEIN",
        "grounding_status": "REVIEWED_LABEL_ONLY",
        "grounding_notes": "Reviewed as a contextual protein or protein-complex label within a quantitative measurement graph; no exact semantic family term was established for this aggregate use.",
        "description": "Proton-translocating ATP synthase whose proton uptake contributes to pH homeostasis."
      },
      "incident_edges": [
        6
      ],
      "references": [
        "DOI:10.1038/nrmicro2549"
      ],
      "assessment": "All current incident source placements accounted for. Generic contextual physiology and identity only; detailed intervention/defense efficacy unassessed. No universal mechanism or exact interval membership is inferred from a node label."
    },
    {
      "index": 8,
      "field_path": "causal_graphs[0].nodes[8]",
      "node": {
        "node_id": "alkaline_ph_homeostasis",
        "label": "alkaline pH homeostasis",
        "node_type": "BIOLOGICAL_PROCESS",
        "description": "Maintenance of a near-neutral cytoplasmic pH against a strongly alkaline exterior."
      },
      "incident_edges": [
        6,
        7
      ],
      "references": [
        "DOI:10.1038/nrmicro2549"
      ],
      "assessment": "All current incident source placements accounted for. Generic contextual physiology and identity only; detailed intervention/defense efficacy unassessed. No universal mechanism or exact interval membership is inferred from a node label."
    },
    {
      "index": 9,
      "field_path": "causal_graphs[0].nodes[9]",
      "node": {
        "node_id": "external_ph_high",
        "label": "external pH &gt; 10.3",
        "node_type": "ENVIRONMENTAL_FACTOR",
        "description": "Strongly alkaline external pH above ~10.3."
      },
      "incident_edges": [
        8
      ],
      "references": [
        "DOI:10.1128/AEM.01557-23"
      ],
      "assessment": "All current incident source placements accounted for. Generic contextual physiology and identity only; detailed intervention/defense efficacy unassessed. No universal mechanism or exact interval membership is inferred from a node label."
    },
    {
      "index": 10,
      "field_path": "causal_graphs[0].nodes[10]",
      "node": {
        "node_id": "carbonate_speciation",
        "label": "carbonate (CO3 2-) speciation",
        "node_type": "CHEMICAL",
        "description": "Shift of dissolved inorganic carbon toward carbonate at high pH."
      },
      "incident_edges": [
        8
      ],
      "references": [
        "DOI:10.1128/AEM.01557-23"
      ],
      "assessment": "All current incident source placements accounted for. Actual inorganic-carbon shift is source-supported; material carbonate versus a shift/process referent is a separate grounding precision question."
    }
  ]
}

### Native checklist: organism applicability

evidence: unknown. Targets: METPO:1000464.

No canonical organism is supplied, so no organism is substituted to obtain an expression result. Retained catalog and runner provenance do not establish phenotype or pathway efficacy, and no detailed defense gene/module query is made.

{
  "completed_at": "2026-10-21T19:51:03.939860+00:00",
  "status": "NOT_APPLICABLE_TO_CURRENT_CANONICAL_MATCHING",
  "canonical_examples": 0,
  "catalog_organisms": 20,
  "catalog_datasets": 28,
  "catalog": {
    "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-grounding-agent/reused-datasets.json",
    "sha256": "155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693",
    "bytes": 2871
  },
  "original_access_receipts": {
    "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-grounding-agent/reused-catalog-accesses.json",
    "sha256": "8417116b63b7d42e7f4c6cba92ef0420fbc87b24ac4629c4c77286caf6293f4a",
    "bytes": 828
  },
  "assessment": "The retained catalog is available, but this record supplies no canonical organism or strain for exact matching. Model organisms mentioned in literature or the generated report are not substituted as canonical examples. This is not a claim that the catalog lacks every relevant organism.",
  "downstream_gene_or_module_queries": "NOT_RUN",
  "protein_instances": 0,
  "uniprot_instance_audit": "NOT_APPLICABLE",
  "scope": "No detailed defense, stress-response or fitness queries."
}

### Native checklist: current fields and maintained writers

provenance: supported. Targets: METPO:1000464.

The seeder directly preserves upstream exact/related synonym types. The canonical-gap writer documents the retained complete-interval convention and is not a required synonym repair. Edge 5 mapping/shared-grounder context preserves nonempty IDs; its historical migration matches the old sodium-to-Mrp key and does not automatically replay the current sodium-to-antiport assertion. Only the record is established as the current node 10 owner.

{
  "completed_at": "2026-10-21T19:51:03.939860+00:00",
  "target": "data/traits/environment/ph_range_high.yaml",
  "owners": [
    {
      "path": "scripts/seed_from_metpo.py",
      "locators": [
        "198\u2013209",
        "333\u2013348"
      ],
      "role": "Direct import owner for exact and related synonym types. It preserves the upstream synonym kind when serializing; scientific equivalence and import fidelity are separate.",
      "sha256": "0fb9c9f7ea6a8f137eecd5c319775b511c398dba6158c81b1fbfb94210f7d851"
    },
    {
      "path": "scripts/migrate_enables_range_edges.py",
      "locators": [
        "53\u201359",
        "204\u2013239"
      ],
      "role": "Direct historical edge owner: the decision matches the OLD cytoplasmic_na -&gt; mrp_antiporter_complex key and repoints the object to the antiport process while retaining enables. The replay requires that old key and RO:0002327, and returns failure when absent. It is not an automatic repair of the already-repointed current assertion.",
      "sha256": "3d0d1bddcaa76baef5833973e2e979e4fee1f834c67d1abcc69a8d866ecb8f32"
    },
    {
      "path": "scripts/ground_causal_predicates.py",
      "locators": [
        "136\u2013180"
      ],
      "role": "Maintained mapping consumer; existing nonempty predicate_id is skipped. A table change alone will not rewrite the current populated edge.",
      "sha256": "5a788eeaabf3a56b0d82c469a3e3fe28f1d51707d9382313b9a94289be7d1381"
    },
    {
      "path": "mappings/predicate_grounding.tsv",
      "locators": [
        "8",
        "9",
        "10",
        "102"
      ],
      "role": "Current subclass, enables, contributes-to and confers mapping context. Wildcard mapping rows do not remove imported relation semantics.",
      "sha256": "8e28c19e93aca3dc164a3befbe2612b289241de457c59f499e65936c03b7ce52"
    },
    {
      "path": "scripts/backfill_canonical_examples_444.py",
      "locators": [
        "819\u2013823",
        "995\u20131074"
      ],
      "role": "Exact current canonical-gap owner. Preserves the documented complete-interval gap under guarded queue/application logic; does not invent an example.",
      "sha256": "18ca0766789c239d693ef665e8b1d43c1209a0f414a326f1c5d890f88de7b20c"
    },
    {
      "path": "data/traits/environment/ph_range_high.yaml",
      "locators": [
        "causal_graphs[0].nodes[10]"
      ],
      "role": "Only established current recurrence owner for carbonate material/speciation wording. Broad migration or sibling-node hits are context, not proven owners of this exact field.",
      "sha256": "3bf384769f08dd98073a67742a098348aca91cfbea63ea35bcee2e9a1a1c1fec"
    }
  ],
  "search": {
    "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-grounding-agent/search-and-provenance.json",
    "matching_paths": 172,
    "structured_review_target_arrays": 67,
    "exact_target_arrays": 0,
    "ignored_and_hidden_included": true,
    "exclusions": [
      ".git/**",
      ".venv/**"
    ],
    "scope": "Entire owned repository including ignored/hidden files, excluding Git internals and virtual environment. Exact target identity/slug/label and numerical synonym; broad physiological aliases are not treated as exact target signoff."
  },
  "all_node_search": {
    "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-grounding-agent/all-node-owner-search.json",
    "node_ids": 11,
    "history_leads": 5,
    "uncaptured_history_leads": 0
  },
  "history_scope": {
    "captured_histories": 5,
    "whole_files_read": [
      "history/infrastructure/inconsistent-node-type/2026-08-12T000912Z-claude-code-779670.yaml",
      "history/infrastructure/process-quality-consistency/2026-08-21T073211Z-codex-174227.yaml",
      "history/other/canonical-examples-batch1/2026-08-20T074839Z-claude-code-6fb2f5.yaml",
      "history/other/canonical-examples-six/2026-08-21T065406Z-codex-a1ab82.yaml",
      "history/records/ph_range_mid2/2026-09-04T024000Z-codex-3036b8.yaml"
    ],
    "actors": "All five captured histories have AI actors; they are infrastructure, canonical-batch or sibling-record contexts, not exact current-target human acceptance."
  },
  "record_events": {
    "total": 10,
    "ai": 9,
    "seed": 1,
    "assessment": "AI-labelled curation and a non-LLM seed event are positive provenance. They do not constitute a linked human signoff for the current reviewed state."
  },
  "human_traceability": "Within this bounded ignored-inclusive current-target search and actual review-array parsing, no exact current-target human acceptance was established. This is a traceability minor, not a universal claim that no human ever reviewed the record.",
  "report": {
    "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/repo/research/traits/environment/ph_range_high-deep-research-falcon.md",
    "sha256": "3c959ba05254e48acb9a6e33a2d83b36ff95f40412e011f0cee54e884a32a300",
    "bytes": 48756,
    "scope": "Entire 426-line current report read as a generated lead and provenance artifact only. Its August 4 capture is not proof of the exact version used by the June 23 enrichment event; no biological recommendation or repair is adopted from it."
  },
  "context_only": [
    "Generic type-consistency and process/quality migrations do not by themselves prove ownership of current node 10.",
    "The ph_range_mid2 writer and captured sibling history remain comparator context.",
    "The historical encodes migration concerns an edge removed from the current graph."
  ],
  "no_mutations": true
}

### Native checklist: bounded acceptance traceability

provenance: concern. Targets: METPO:1000464.

The current record has nine explicitly AI-assisted events plus an automated seed. The grounding auditor read five whole AI context histories; root read their complete actor/target/event projections. The ignored-inclusive search found 172 paths and 67 actual review target arrays, with zero exact target arrays. These are bounded local observations; passing checks, REVIEWED and parent authorship do not link acceptance of current assertions.

### Native checklist: actual checks and acquisition chronology

consistency: supported. Targets: METPO:1000464.

All 78 captured inputs and frozen artifacts match. Focused native, strict and snippet checks passed directly. AEM source metadata DNS failure and successful retry are separately retained; historical common failures/skips/retries remain explicit under B10-to-B11 reuse without a new B11 QC claim.

## Findings

### category-versus-complete-interval: Broad alkaliphile categories and above-10 growth are equated with a contained numerical range

major / open / confirmed; issue key: ph-range-high-category-versus-complete-interval.

The current exact category synonyms and above-10 description are broader than a complete growth interval contained in 10–14. Published classification distinguishes alkali-tolerant and facultative alkaliphilic growth, while assigned Krulwich text names extreme alkaliphiles with growth below 10. Preserve the numerical bin and generic alkaline physiology; reconcile this one shared scope distinction without rejecting the class or forcing a canonical.

### baker-attribution: Assigned acidophile source is used for a stronger alkaline attribution

minor / open / confirmed; issue key: ph-range-high-baker-attribution.

The inspected Baker abstract supplies acidophile context, while the current notes attribute extreme-alkaliphile antiport and PMF support to that source. Qualify the attribution to actual inspected support or substantiate the broader claim. Its unavailable full body does not prove absence of alkaline discussion or false biology.

### substrate-executor-precision: Sodium substrate availability is expressed with an executor relation

minor / open / confirmed; issue key: ph-range-high-substrate-executor-precision.

The current sodium pool is material and the antiport node processual, so imported endpoint compatibility is positive. RO enables describes an executor relation, while the edge explicitly describes a substrate sustaining activity. This is bounded semantic precision, not a categorical endpoint or biological-efficacy failure.

### carbonate-referent-precision: Carbonate entity and speciation shift share one node referent

minor / open / confirmed; issue key: ph-range-high-carbonate-referent-precision.

Node 10 uses a material carbonate label/type while its description denotes a pH-dependent shift of inorganic-carbon speciation. The existing chemistry is directly source-supported. Clarify the intended entity-versus-change referent without claiming the carbonate statement is false or prescribing a new mechanism.

### human-acceptance-link: Current local provenance lacks an attributable acceptance link

minor / open / confirmed; issue key: ph-range-high-human-acceptance-link.

AI and seed maintenance, REVIEWED and passing checks do not independently identify acceptance of the current graph. The captured ignored-inclusive search and actual target/history parsing bound this result; no private or remote absence is asserted.

## Recommended Actions And Acceptance Checks

### separate-category-and-bin

Reconcile exact category synonyms and above-10 shorthand with the intended complete-interval bin during separately authorized curation.

- Preserve faithful upstream-import provenance separately from scientific equivalence, and retain the valid numerical bin.
- Do not duplicate the same scope issue across definition, synonyms and contextual edges. Do not require a token canonical or invent a whole interval from an upper-growth observation.
- Use guarded history, appropriate native/strict/source/QC checks and a successor review after changed inputs; no mechanistic intervention or experiment is requested.

### qualify-baker-attribution

Qualify or substantiate the assigned Baker attribution using an actually inspected relevant passage.

- Preserve unknown body-snippet status and separate positive Krulwich context.
- Do not infer whole-paper absence, false biology or detailed efficacy from unavailable text.

### clarify-executor-substrate

Clarify the intended sodium substrate relation while preserving the current compatible endpoint referents.

- Distinguish executor semantics from substrate availability without changing biology by inference.
- Preserve the historical migration’s old-key limit and shared grounder’s nonempty-ID guard; neither automatically repairs the current assertion. No forced protein replacement.

### clarify-carbonate-referent

Clarify whether node 10 denotes carbonate material or the described speciation change.

- Preserve the source-backed inorganic-carbon chemistry and approximate threshold.
- Do not add a new pathway, experimental recipe or unsupported causal step.

### link-human-acceptance

Link attributable current acceptance if available or clarify status while preserving the bounded provenance result.

- Retain actual AI/seed provenance and ignored-inclusive search scope.
- No contact with others or automatic status promotion is authorized.

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
| check-ph-range-high-native | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-native.log; Executed 2026-10-21T19:45:40.285098+00:00 through 2026-10-21T19:45:41.228977+00:00; metadata ph-range-high-native.json | context_only | Direct successful current-target schema validation; formal roles are assessed separately. |
| check-ph-range-high-strict | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-strict.log; Executed 2026-10-21T19:45:40.284936+00:00 through 2026-10-21T19:45:41.720209+00:00; metadata ph-range-high-strict.json | context_only | Direct successful current-target strict validation; no biological efficacy certification. |
| check-ph-range-high-snippets | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-snippets.log; Executed 2026-10-21T19:45:45.880189+00:00 through 2026-10-21T19:45:49.248349+00:00; metadata ph-range-high-snippets.json | context_only | Four fields over two references, all NOT_IN_ABSTRACT. Retained primary body independently confirms two Krulwich excerpts; two Baker body phrases remain unknown. Original native results are unchanged. |
| check-batch010-qc | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/batch010-qc.log; Executed 2026-10-21T19:06:27.731868+00:00 through 2026-10-21T19:08:11.219124+00:00; metadata batch010-qc.json | context_only | Actual B10 final QC at its original time, qualified against B11 bytes; not a fresh B11 execution. |
| record | data/traits/environment/ph_range_high.yaml; Entire current record | supports | All eleven nodes, nine edges, four excerpts and ten record events are covered; no canonical is supplied. |
| policy | docs/GROUNDING_POLICY.md; Captured maintained authority | supports | Reviewed label-only contextual protein classes and optional instances; actual activity/material referents remain distinct. |
| playbook | docs/CURATION_PLAYBOOK.md; Captured maintained authority | supports | Preserve exact attribution, source scope and actual acceptance provenance. |
| schema | src/traitmech/schema/traitmech.yaml; Captured maintained authority | supports | Actual trait, activity, material, quality and process facets. |
| checklist | .claude/skills/curate-yaml-record/references/review-checklist.md; Captured maintained authority | supports | Complete identity, evidence, graph, ownership, optional evidence and readiness assessment. |
| reuse | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-b10-qc-supplement-qualified.json; Actual B10-to-B11 qualification | supports | All retained diagnostic outcomes and byte comparisons remain bound. |
| reuse-postcheck | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-output-verification-agent/post-execution-verification.json; Actual independent qualifier postcheck | supports | Byte and native-output bindings independently verified without new QC. |
| capture | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-grounding-agent/capture-verification.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Successful 78-input capture independently verified. |
| identity | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-grounding-agent/identity-assessment.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Active identity, parent, predecessor and inherited aliases; import fidelity is separate from scientific equivalence. |
| node-edges | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-grounding-agent/node-edge-ledger.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Every current node and edge, with actual role compatibility and bounded precision qualifications. |
| owners | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-grounding-agent/owner-provenance-assessment.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Current owners, prior corrections and bounded human-acceptance evidence. |
| expression | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-grounding-agent/expression-assessment.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | No supplied canonical organism and no substitute expression query. |
| authority-reuse | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-grounding-agent/authority-reuse-receipts.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Original catalog/runner acquisition times retained. |
| local-authority | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-grounding-agent/local-authority-excerpts.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Local confers semantics and actual mapping rows; no invented endpoint exclusions. |
| ground-reading | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-grounding-agent/actual-reading-scope.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Actual authority and history reading scope. |
| ground-manifest | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-grounding-agent/evidence-manifest.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Frozen grounding artifacts verified. |
| metpo-primary | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/repo/data/raw/metpo.owl; Actual current target, parent and explicit obsolete replacement XML | supports | The active class retains inclusive 10–14 numeric bounds, its parent and inherited aliases. Scientific equivalence and the complete-interval convention are assessed separately from import fidelity; no target creator is copied from its parent. |
| ro-primary | /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/ro.db; RO:0002327 executor semantics; RO:0002326 material-to-process inheritance | supports | Both current imported edges have material subjects and process objects. Edge 5 raises bounded executor-versus-substrate precision rather than a categorical material/process endpoint failure. Edge 6 is compatible. |
| meta-krulwich | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/krulwich-metadata.json; Actual indexed abstract and metadata | supports | Actual retained indexed identity, abstract and notice fields only; original acquisition remains separate from current copying. |
| meta-baker | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/baker-metadata.json; Actual indexed abstract and metadata | supports | Actual retained acidophile abstract. The assigned PMF body phrase and extreme-alkaliphile antiporter attribution are not established by that inspected surface; no full-paper absence is inferred. |
| meta-aem | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/aem-metadata-network-retry.json; Actual new indexed identity/abstract | supports | Assigned DIC minireview identity and indexed abstract verified. This evidence item covers the returned metadata surface only; no toolkit engineering efficacy is assessed. |
| body-aem | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/aem.xml; Zero-based JATS body paragraph 22 | supports | Actual generic chemistry states carbonate predominates above about pH 10.3. Only the existing inorganic-carbon claim is assessed; genomic methods, toolkit optimization and engineering implications are excluded. |
| body-krulwich | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/krulwich-bioc.xml; BioC 2440/3940/39253; first sentences of 40107/41582/42119 | supports | Selected generic environmental classification and existing physiological context. Extreme-alkaliphile examples include growth below 10; contextual positive antiport and ATP-synthase support does not calibrate a complete 10–14 interval. Later mutation and intervention passages are unassessed. |
| classification-metadata | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/classification-supplement-metadata.json; Actual retained supplemental identity/abstract | supports | Retained supplemental work identity and returned metadata fields only; classification claims are separately supported by its selected body paragraph. |
| classification-body | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/classification-supplement.xml; Only zero-based body paragraph 0 | supports | Separate DOI:10.1155/2024/3087296 classification supplement, not an assigned citation or canonical. Body paragraph 0 distinguishes broad tolerant/alkaliphilic categories and facultative near-neutral growth; experimental adaptation details are not assessed. |
| sources | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/source-assessment.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Three assigned works plus a separately identified classification supplement; complete source coverage. |
| source-ledger | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/source-ledger.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Actual identities, original acquisitions and source-specific available surfaces. |
| placements | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/placement-ledger.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | All twelve external placements and distinct grounding/synonym provenance fields. |
| snippets | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/snippet-ledger.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Four excerpts: two exact Krulwich body occurrences and two Baker body-unknown phrases. |
| node-sources | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/node-source-ledger.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | All eleven nodes and incident evidence placements. |
| edge-sources | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/edge-source-ledger.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | All nine edge attributions, with generic context distinct from detailed efficacy. |
| source-status | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/publication-status-ledger.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Bounded indexed publication-notice observations at original acquisition times. |
| source-reading | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/selected-primary-reading.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Selected classification/chemistry scope; incidental detailed passages are unassessed. |
| source-access | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/access-limitations.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Baker body unknown; actual AEM DNS failure/retry preserved separately from native success. |
| source-reuse | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/reuse-and-copy-receipt.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Original acquisition and current copy times, including supplemental body provenance. |
| bin-scope | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/classification-and-bin-assessment.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | One grouped category-versus-complete-interval concern; no duplicate numeric-bin rejection. |
| canonical-gap | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/canonical-gap-assessment.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Explicit lack of a supplied full-interval example retained without a global absence claim. |
| native-checks | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/native-check-context.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Actual direct successful native checks and original inconclusive abstract matches. |
| source-manifest | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/evidence-manifest.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Thirty-two frozen source artifacts verified. |
| aem-first-access | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/aem-metadata-access.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Original DNS failure preserved; not a native or completed-review failure. |
| aem-retry-access | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/aem-metadata-network-retry-access.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Actual successful source metadata retry, separate from earlier failure. |
| root-reading-40 | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-root/history-event-summary-reading.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Only the actual bounded reading scope and chronology recorded here; no inferred whole-body or excluded efficacy review. |
| root-reading-42 | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-root/owner-window-reading.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Only the actual bounded reading scope and chronology recorded here; no inferred whole-body or excluded efficacy review. |
| root-reading-43 | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-root/primary-identity-formal-reading.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Only the actual bounded reading scope and chronology recorded here; no inferred whole-body or excluded efficacy review. |
| root-reading-45 | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-root/primary-ro-definitions-reading.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Only the actual bounded reading scope and chronology recorded here; no inferred whole-body or excluded efficacy review. |
| root-reading-46 | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-root/primary-source-classification-reading.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Only the actual bounded reading scope and chronology recorded here; no inferred whole-body or excluded efficacy review. |
| root-reading-48 | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-root/whole-target-preinspect-reading.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Only the actual bounded reading scope and chronology recorded here; no inferred whole-body or excluded efficacy review. |
| challenge | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-semantic-challenge-agent/semantic-severity-challenge.json; Final independent challenge | supports | Actual final recommendation and all bindings verified. |
| adjudication | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-root-adjudication.json; Final root disposition | supports | Final root adjudication controls severity, grouping and limitations. |

## Limits And Additional Notes

- Detailed pathogen defense, fitness, AMR, mutation/perturbation efficacy and intervention optimization remain UNASSESSED_SCOPE. No biological route or experimental repair is supplied.
- Baker full body and both current PMF phrases remain unknown. The source-attribution concern is bounded to inspected support, not whole-paper absence or false biology.
- Inherited ontology text may be faithfully imported while exact scientific category equivalence remains too broad. Do not infer a complete interval from growing above 10, or infer an empty bin from the absent canonical.
- Both current RO edges satisfy material/process endpoint categories. Executor/substrate precision is a semantic distinction, not a formal endpoint failure; ATP-synthase contribution remains compatible.
- Current local confers has broad documented endpoints. Generic contextual support is not automatically universal necessity or exact numerical-bin calibration.
- AEM paragraph 22 supports carbonate predominance above approximately 10.3; genome-toolkit methods and engineering implications are not adopted.
- Krulwich selected first-sentence environmental context retains its organism scope; later motif/mutation passages are unassessed. The supplemental classification article is not assigned evidence or a replacement canonical.
- Original source acquisitions, current copies and selected readings remain distinct. AEM metadata DNS failure and successful retry are not native/serializer failures.
- No supplied canonical means no organism/catalog substitution. Optional proteins, accessions, connectors and pathways are not added by quota.
- Target creator attribution is not copied from the pH-range parent. Bounded local acceptance search cannot establish absence of private or remote decisions.
- Exact large-potential necessity wording at edge 3 is not established by the selected primary windows; a bounded retained-sentence nonmatch is not full-paper absence or false physiology.
- The complete-interval convention is documented by the current record and guarded canonical-gap writer; the numeric existential OWL restriction alone is not a universal whole-interval containment axiom.
- Root selected primary reading covered the three assigned abstracts, Krulwich classification paragraph 39253, supplemental body paragraph 0 and AEM paragraph 22. Additional generic physiology first-sentence readings belong to the source auditor and independent challenger, not a root whole-article claim.
- Final root disposition is 1 major and 4 minor findings, with all source, grounding, challenge and root bindings verified. This preparation has not imported or executed the serializer. Root owns one serialization, native validation, final artifact review and save.
- Source coverage: 3 assigned works plus 1 explicit classification supplement; 12 external placements; 11 nodes/9 edges; 4 snippets (2 literal and 2 unknown); no canonical.
- Preparation changes no scientific record, Git state, sweep state or native inventory.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T195408Z-ph-range-high
kind: record
repository: CultureBotAI/TraitMech
title: Whole-record review of high pH range
started_at: '2026-10-21T19:45:19.695714Z'
finished_at: '2026-10-21T19:54:08Z'
reviewer:
  identity: codex
  kind: agent
  independence: independent
  independence_basis: Separate source and grounding audits, independent challenge
    and bounded root primary readings. Generic environmental classification, inorganic-carbon
    chemistry, literal evidence and formal semantics only; detailed pathogen defense,
    fitness, AMR and intervention efficacy are UNASSESSED_SCOPE. No scientific input
    was edited.
  model: GPT-6 (Codex)
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'Needs curation: one grouped category/complete-interval major and four bounded
  minors concerning Baker attribution, substrate/executor semantics, carbonate referent
  and human-acceptance traceability. Active identity, numerical bounds, generic environmental
  physiology and inorganic-carbon chemistry remain positive.'
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
    role: context
  - path: data/traits/environment/ph_range_high.yaml
    sha256: 3bf384769f08dd98073a67742a098348aca91cfbea63ea35bcee2e9a1a1c1fec
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
  - path: research/traits/environment/ph_range_high-deep-research-falcon.md
    sha256: 3c959ba05254e48acb9a6e33a2d83b36ff95f40412e011f0cee54e884a32a300
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
  - path: scripts/connect_ph_delta_mid3_graph_183.py
    sha256: cf65890b2797032dcf9d2fa7b249a47cfe710501b3b2d8f610f323c6f27366e4
    role: context
  - path: scripts/connect_ph_delta_very_low_graph_183.py
    sha256: 5abcdea4fbf7793bc718406439e63203726284d2c2d3222b4bdd00d3de2b6390
    role: context
  - path: scripts/connect_trophic_physiology_graphs_183.py
    sha256: 7189bebab88866f9f4bb2cdfa8ccf4e1a2c6e3086d7c37c5b04dbdc53685e1a4
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
  - path: scripts/review_nacl_optimum_graph_183.py
    sha256: 6d0de1ccb1604fb87294432692cc051e3a8a1d52e082eaff6aa1f8d3cb621ffd
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
- target_id: METPO:1000464
  path: data/traits/environment/ph_range_high.yaml
  label: pH range high
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_range_high.yaml
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
  selection: Fourth record of the actual batch 011 queue. Whole target read before
    successful 78-input capture. AEM bibliographic collection began before capture;
    substantive judgments followed capture verification. Final source/grounding audits,
    independent challenge and root adjudication are mandatory.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - METPO:1000464
checks:
- check_id: audit-graphs
  name: Full-corpus graph audit
  status: passed
  required: true
  target_ids:
  - METPO:1000464
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
  - METPO:1000464
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
  - METPO:1000464
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
  - METPO:1000464
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
  - METPO:1000464
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
  - METPO:1000464
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
  - METPO:1000464
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
- check_id: ph-range-high-native
  name: Focused native validation
  status: passed
  required: true
  target_ids:
  - METPO:1000464
  command: just validate data/traits/environment/ph_range_high.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Direct successful current-target schema validation; formal roles are assessed
    separately.
  evidence_ids:
  - check-ph-range-high-native
- check_id: ph-range-high-strict
  name: Focused strict validation
  status: passed
  required: true
  target_ids:
  - METPO:1000464
  command: just validate-strict data/traits/environment/ph_range_high.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Direct successful current-target strict validation; no biological efficacy
    certification.
  evidence_ids:
  - check-ph-range-high-strict
- check_id: ph-range-high-snippets
  name: Focused snippet verification
  status: passed
  required: true
  target_ids:
  - METPO:1000464
  command: just verify-snippets --record data/traits/environment/ph_range_high.yaml
    --out /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-snippets.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: Four fields over two references, all NOT_IN_ABSTRACT. Retained primary
    body independently confirms two Krulwich excerpts; two Baker body phrases remain
    unknown. Original native results are unchanged.
  evidence_ids:
  - check-ph-range-high-snippets
- check_id: batch010-qc
  name: Reused maintained batch-ten QC
  status: passed
  required: true
  target_ids:
  - METPO:1000464
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
  - METPO:1000464
  summary: Three reviewed label-only contextual protein classes have no instances;
    no token accession is required by this measurement graph.
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
- evidence_id: check-ph-range-high-native
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-native.log
  locator: Executed 2026-10-21T19:45:40.285098+00:00 through 2026-10-21T19:45:41.228977+00:00;
    metadata ph-range-high-native.json
  accessed_at: '2026-10-21T19:45:41.228977Z'
  support: context_only
  summary: Direct successful current-target schema validation; formal roles are assessed
    separately.
  snapshot_sha256: 34d764c0c2b94feaeb57d13d6040e6f3d8d4448c212e577de91d34f648978a11
- evidence_id: check-ph-range-high-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-strict.log
  locator: Executed 2026-10-21T19:45:40.284936+00:00 through 2026-10-21T19:45:41.720209+00:00;
    metadata ph-range-high-strict.json
  accessed_at: '2026-10-21T19:45:41.720209Z'
  support: context_only
  summary: Direct successful current-target strict validation; no biological efficacy
    certification.
  snapshot_sha256: 75eb7fe76045b1759056378edf84249a14855d9263296863e4413879e9dd2f3f
- evidence_id: check-ph-range-high-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-snippets.log
  locator: Executed 2026-10-21T19:45:45.880189+00:00 through 2026-10-21T19:45:49.248349+00:00;
    metadata ph-range-high-snippets.json
  accessed_at: '2026-10-21T19:45:49.248349Z'
  support: context_only
  summary: Four fields over two references, all NOT_IN_ABSTRACT. Retained primary
    body independently confirms two Krulwich excerpts; two Baker body phrases remain
    unknown. Original native results are unchanged.
  snapshot_sha256: 8f9ef4c3bd969036e50c4cdc10061857bb3c60684fe5826712e94dea09b9460e
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
  reference: data/traits/environment/ph_range_high.yaml
  locator: Entire current record
  accessed_at: '2026-10-21T19:45:20.556993Z'
  support: supports
  summary: All eleven nodes, nine edges, four excerpts and ten record events are covered;
    no canonical is supplied.
  snapshot_sha256: 3bf384769f08dd98073a67742a098348aca91cfbea63ea35bcee2e9a1a1c1fec
- evidence_id: policy
  kind: authority
  reference: docs/GROUNDING_POLICY.md
  locator: Captured maintained authority
  accessed_at: '2026-10-21T19:51:03.939860Z'
  support: supports
  summary: Reviewed label-only contextual protein classes and optional instances;
    actual activity/material referents remain distinct.
  snapshot_sha256: 891678c983c2283a47c81c47950b35753981e9339d105f3bbdda92a1f5ab7f42
- evidence_id: playbook
  kind: authority
  reference: docs/CURATION_PLAYBOOK.md
  locator: Captured maintained authority
  accessed_at: '2026-10-21T19:51:03.939860Z'
  support: supports
  summary: Preserve exact attribution, source scope and actual acceptance provenance.
  snapshot_sha256: 735e9b810471da9f7d8364e35ffe1e741edb3421480dac01727db6ea5aa65da9
- evidence_id: schema
  kind: authority
  reference: src/traitmech/schema/traitmech.yaml
  locator: Captured maintained authority
  accessed_at: '2026-10-21T19:51:03.939860Z'
  support: supports
  summary: Actual trait, activity, material, quality and process facets.
  snapshot_sha256: 46c47fc627b80ccbba1e8ab3fb6f2aee93bc2aef7aaf72fe9aadc3257f2c02dd
- evidence_id: checklist
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Captured maintained authority
  accessed_at: '2026-10-21T19:51:03.939860Z'
  support: supports
  summary: Complete identity, evidence, graph, ownership, optional evidence and readiness
    assessment.
  snapshot_sha256: da8896328a0fd6cc92f1adf0d8be8980d0ddd41f3172c7936f2c7f119b293ac1
- evidence_id: reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-b10-qc-supplement-qualified.json
  locator: Actual B10-to-B11 qualification
  accessed_at: '2026-10-21T19:08:29.388400Z'
  support: supports
  summary: All retained diagnostic outcomes and byte comparisons remain bound.
  snapshot_sha256: a728777b9987b1283d7d1382168af40739074fce5c05f9a3bd93d3738f56880f
- evidence_id: reuse-postcheck
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-output-verification-agent/post-execution-verification.json
  locator: Actual independent qualifier postcheck
  accessed_at: '2026-10-21T19:08:41.804361Z'
  support: supports
  summary: Byte and native-output bindings independently verified without new QC.
  snapshot_sha256: a3a6f33363e71b00e8db09cbc318cae0027844aba584f7b4cafb282d11ab027a
- evidence_id: capture
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-grounding-agent/capture-verification.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:45:57.677258Z'
  support: supports
  summary: Successful 78-input capture independently verified.
  snapshot_sha256: 70b4cb4a222d6fd3efe9c6b92dd6adaf319ce05d7d2d933820f9e75500acf697
- evidence_id: identity
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-grounding-agent/identity-assessment.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:51:03.939860Z'
  support: supports
  summary: Active identity, parent, predecessor and inherited aliases; import fidelity
    is separate from scientific equivalence.
  snapshot_sha256: f8c854ba52645e460b4f378150f8e3e01bab588894e493554b8c7f3084e36438
- evidence_id: node-edges
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-grounding-agent/node-edge-ledger.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:51:03.939860Z'
  support: supports
  summary: Every current node and edge, with actual role compatibility and bounded
    precision qualifications.
  snapshot_sha256: f33c8931573e8e1ca8646ce0c23c063bc110ba2aa91ed49a433064314741165a
- evidence_id: owners
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-grounding-agent/owner-provenance-assessment.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:51:03.939860Z'
  support: supports
  summary: Current owners, prior corrections and bounded human-acceptance evidence.
  snapshot_sha256: ffb2482acd148fe672a43b91213018a1a38dbead2e635626960c7879489037ea
- evidence_id: expression
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-grounding-agent/expression-assessment.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:51:03.939860Z'
  support: supports
  summary: No supplied canonical organism and no substitute expression query.
  snapshot_sha256: ca626d32d20a116587c14821cf12afee260f26baf8bcc5fca936ba780ab43bfc
- evidence_id: authority-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-grounding-agent/authority-reuse-receipts.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:46:10.254098Z'
  support: supports
  summary: Original catalog/runner acquisition times retained.
  snapshot_sha256: 1cf3f27f49ed285ff286c55b2a31e05d3b70c39c4dcebfcd51666bb34884f187
- evidence_id: local-authority
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-grounding-agent/local-authority-excerpts.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:46:10.237431Z'
  support: supports
  summary: Local confers semantics and actual mapping rows; no invented endpoint exclusions.
  snapshot_sha256: 5e3a879299c4920cab6bd2ea6517ffb393c595c81e95acef0b3d612be9d5ae62
- evidence_id: ground-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-grounding-agent/actual-reading-scope.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:51:03.939860Z'
  support: supports
  summary: Actual authority and history reading scope.
  snapshot_sha256: 2efd3bcb6fcbf6dab9ae2723f0dd0d1f241e367b0dac4ecb1193e1fadb299402
- evidence_id: ground-manifest
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-grounding-agent/evidence-manifest.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:51:03.939860Z'
  support: supports
  summary: Frozen grounding artifacts verified.
  snapshot_sha256: 3818558c5f665d350758e4d2d5d0cf972e077820579e45288f631dd7a1d09cd2
- evidence_id: metpo-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/repo/data/raw/metpo.owl
  locator: Actual current target, parent and explicit obsolete replacement XML
  accessed_at: '2026-10-21T19:46:10.228382Z'
  support: supports
  summary: The active class retains inclusive 10–14 numeric bounds, its parent and
    inherited aliases. Scientific equivalence and the complete-interval convention
    are assessed separately from import fidelity; no target creator is copied from
    its parent.
  snapshot_sha256: 8b6f8fe0510a698579e532658c8ace05da2550093365df9ca83feb0741778415
- evidence_id: ro-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/ro.db
  locator: RO:0002327 executor semantics; RO:0002326 material-to-process inheritance
  accessed_at: '2026-10-21T19:46:10.231929Z'
  support: supports
  summary: Both current imported edges have material subjects and process objects.
    Edge 5 raises bounded executor-versus-substrate precision rather than a categorical
    material/process endpoint failure. Edge 6 is compatible.
  snapshot_sha256: 849e616c29fecd0d4a6c6dee0dc0f6f117ace7167dbfa1e0f043dc84868f83cb
- evidence_id: meta-krulwich
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/krulwich-metadata.json
  locator: Actual indexed abstract and metadata
  accessed_at: '2026-10-21T19:34:30.782245Z'
  support: supports
  summary: Actual retained indexed identity, abstract and notice fields only; original
    acquisition remains separate from current copying.
  snapshot_sha256: 484784a62fbb4c9d74a1feab4df2fdfdf37d4dd0ce3fa79f714c86a07d86d29c
- evidence_id: meta-baker
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/baker-metadata.json
  locator: Actual indexed abstract and metadata
  accessed_at: '2026-10-21T19:34:30.766603Z'
  support: supports
  summary: Actual retained acidophile abstract. The assigned PMF body phrase and extreme-alkaliphile
    antiporter attribution are not established by that inspected surface; no full-paper
    absence is inferred.
  snapshot_sha256: a78777bc3bb6444b32e2e8a13ab72c56d80592b97e30c9b5520c67cc040c631b
- evidence_id: meta-aem
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/aem-metadata-network-retry.json
  locator: Actual new indexed identity/abstract
  accessed_at: '2026-10-21T19:45:33.132663Z'
  support: supports
  summary: Assigned DIC minireview identity and indexed abstract verified. This evidence
    item covers the returned metadata surface only; no toolkit engineering efficacy
    is assessed.
  snapshot_sha256: 970d059277060c22e22251680a6cefc06a50ff9b1a8b6a23d4208aa8a1bfea75
- evidence_id: body-aem
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/aem.xml
  locator: Zero-based JATS body paragraph 22
  accessed_at: '2026-10-21T19:45:55.640700Z'
  support: supports
  summary: Actual generic chemistry states carbonate predominates above about pH 10.3.
    Only the existing inorganic-carbon claim is assessed; genomic methods, toolkit
    optimization and engineering implications are excluded.
  snapshot_sha256: d782ddfee1ab3ef5610048dc0612104d6536e8857111109f3851f9c221d71eb7
- evidence_id: body-krulwich
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/krulwich-bioc.xml
  locator: BioC 2440/3940/39253; first sentences of 40107/41582/42119
  accessed_at: '2026-10-21T07:57:33Z'
  support: supports
  summary: Selected generic environmental classification and existing physiological
    context. Extreme-alkaliphile examples include growth below 10; contextual positive
    antiport and ATP-synthase support does not calibrate a complete 10–14 interval.
    Later mutation and intervention passages are unassessed.
  snapshot_sha256: 903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f
- evidence_id: classification-metadata
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/classification-supplement-metadata.json
  locator: Actual retained supplemental identity/abstract
  accessed_at: '2026-10-21T18:30:13.568644Z'
  support: supports
  summary: Retained supplemental work identity and returned metadata fields only;
    classification claims are separately supported by its selected body paragraph.
  snapshot_sha256: 2195f58575dcd56fc839f95a139c1e8107605b7342a070450d916776fa3476e7
- evidence_id: classification-body
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/classification-supplement.xml
  locator: Only zero-based body paragraph 0
  accessed_at: '2026-10-21T18:33:31.868395Z'
  support: supports
  summary: Separate DOI:10.1155/2024/3087296 classification supplement, not an assigned
    citation or canonical. Body paragraph 0 distinguishes broad tolerant/alkaliphilic
    categories and facultative near-neutral growth; experimental adaptation details
    are not assessed.
  snapshot_sha256: 27ff0a4deeb4ee46f16eb6caea70872e0946110f4b013db496efb8cce87d6a73
- evidence_id: sources
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/source-assessment.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:48:47.213948Z'
  support: supports
  summary: Three assigned works plus a separately identified classification supplement;
    complete source coverage.
  snapshot_sha256: 91697ad30d4c3de405be6bbb4a37ca84a94313d2d09d3074be8f9e313a8f46b9
- evidence_id: source-ledger
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/source-ledger.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:48:47.205274Z'
  support: supports
  summary: Actual identities, original acquisitions and source-specific available
    surfaces.
  snapshot_sha256: 6706f5e8acf1abba4e172c2b09866511d69b56cd5a224ea53c590a21ab5d9d15
- evidence_id: placements
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/placement-ledger.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:48:47.211004Z'
  support: supports
  summary: All twelve external placements and distinct grounding/synonym provenance
    fields.
  snapshot_sha256: 65d85b7f99996a7fa0fb73a20b0732550b5bc7531151578c749cde3b1db67181
- evidence_id: snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/snippet-ledger.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:48:47.212874Z'
  support: supports
  summary: 'Four excerpts: two exact Krulwich body occurrences and two Baker body-unknown
    phrases.'
  snapshot_sha256: 99fdf8e854025904e8ba8e2a9b35f856f2d991d8f62227502bbbf9f0f4e52830
- evidence_id: node-sources
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/node-source-ledger.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:48:47.211294Z'
  support: supports
  summary: All eleven nodes and incident evidence placements.
  snapshot_sha256: 9c43776a366919ff9cd23263b82a01fe337cfac44a62783f793297a78e6310da
- evidence_id: edge-sources
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/edge-source-ledger.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:48:47.211139Z'
  support: supports
  summary: All nine edge attributions, with generic context distinct from detailed
    efficacy.
  snapshot_sha256: 092cae6a6e5a543235fada3fd205cf09682a64952bd3d80b41838c30651ed6b4
- evidence_id: source-status
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/publication-status-ledger.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:48:47.205450Z'
  support: supports
  summary: Bounded indexed publication-notice observations at original acquisition
    times.
  snapshot_sha256: c406a8e09c14e3a0ff1ba16c9d4a275c47f1aa1c5d28e48ea0aabccb50768bdd
- evidence_id: source-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/selected-primary-reading.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:48:47.213285Z'
  support: supports
  summary: Selected classification/chemistry scope; incidental detailed passages are
    unassessed.
  snapshot_sha256: 96585b1c76020ea7a7f42b8e635351739f1857195f167ae67b53561f2d3c592b
- evidence_id: source-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/access-limitations.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:48:47.213594Z'
  support: supports
  summary: Baker body unknown; actual AEM DNS failure/retry preserved separately from
    native success.
  snapshot_sha256: c31bce384d92a4e22c6e19ce795811d928606d7f6b2da3628fd6bbc21d0ef756
- evidence_id: source-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/reuse-and-copy-receipt.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:47:03.018575Z'
  support: supports
  summary: Original acquisition and current copy times, including supplemental body
    provenance.
  snapshot_sha256: e153a88b71de6ade9b769c4730a1d5f6584d5e675d8f62ca3747fabdc1c8a798
- evidence_id: bin-scope
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/classification-and-bin-assessment.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:48:47.213002Z'
  support: supports
  summary: One grouped category-versus-complete-interval concern; no duplicate numeric-bin
    rejection.
  snapshot_sha256: 40c7c1dd52e0a4744a7fb9bff3a39673175b24b15f3abae011581a18d280466b
- evidence_id: canonical-gap
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/canonical-gap-assessment.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:48:47.213216Z'
  support: supports
  summary: Explicit lack of a supplied full-interval example retained without a global
    absence claim.
  snapshot_sha256: c9bfd0c65cd9fb86b96c7b924daae0eaa53eee7d25fb074230abd2c1fe441ecd
- evidence_id: native-checks
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/native-check-context.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:48:47.213843Z'
  support: supports
  summary: Actual direct successful native checks and original inconclusive abstract
    matches.
  snapshot_sha256: aa0fa78406d9a9d2c804daad55f93ec81df04ddfe780dba4ce16586f4d2cc3aa
- evidence_id: source-manifest
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/evidence-manifest.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:48:47.219602Z'
  support: supports
  summary: Thirty-two frozen source artifacts verified.
  snapshot_sha256: e30fbda04950e2d3cb8a15e4aec932d543c83ddadcb67f7e162ea0e76798c72f
- evidence_id: aem-first-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/aem-metadata-access.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:45:18.556475Z'
  support: supports
  summary: Original DNS failure preserved; not a native or completed-review failure.
  snapshot_sha256: 0430bc02be57ef496dde2d7843f04335a98974950887407e1b3467ac52322122
- evidence_id: aem-retry-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/aem-metadata-network-retry-access.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:45:33.132663Z'
  support: supports
  summary: Actual successful source metadata retry, separate from earlier failure.
  snapshot_sha256: 00e720860116637fd9eea557bbd42c58320a5be87ac2f2e8acd1289f90c1033a
- evidence_id: root-reading-40
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-root/history-event-summary-reading.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:47:31.129845Z'
  support: supports
  summary: Only the actual bounded reading scope and chronology recorded here; no
    inferred whole-body or excluded efficacy review.
  snapshot_sha256: 58c698571ee5b289fa8d09f4e498d855add4c1684a25ee2b44880084bc8e679e
- evidence_id: root-reading-42
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-root/owner-window-reading.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:48:27.764623Z'
  support: supports
  summary: Only the actual bounded reading scope and chronology recorded here; no
    inferred whole-body or excluded efficacy review.
  snapshot_sha256: 17e2f1b73a541215e80983636b921ec96c1030d82410e5bcb5fb0b26db727853
- evidence_id: root-reading-43
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-root/primary-identity-formal-reading.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:46:14.360597Z'
  support: supports
  summary: Only the actual bounded reading scope and chronology recorded here; no
    inferred whole-body or excluded efficacy review.
  snapshot_sha256: 1bc810dd5dd34f63a83d20ee846426b47c38ba77aa1bcf71e14e89108e2e78b9
- evidence_id: root-reading-45
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-root/primary-ro-definitions-reading.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:46:46.401905Z'
  support: supports
  summary: Only the actual bounded reading scope and chronology recorded here; no
    inferred whole-body or excluded efficacy review.
  snapshot_sha256: 371e66c098888bcc03a06195962db5f1fe358f088d65347b12cb572e203ecdb0
- evidence_id: root-reading-46
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-root/primary-source-classification-reading.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:47:14.863056Z'
  support: supports
  summary: Only the actual bounded reading scope and chronology recorded here; no
    inferred whole-body or excluded efficacy review.
  snapshot_sha256: ee1986e3a282fefbd40f7f1e81f8793e994110f63c00227b0a7b9f767fc40f2d
- evidence_id: root-reading-48
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-root/whole-target-preinspect-reading.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:44:17.734431Z'
  support: supports
  summary: Only the actual bounded reading scope and chronology recorded here; no
    inferred whole-body or excluded efficacy review.
  snapshot_sha256: 91bd35911590f20a19fcde4d953364871fb7ff3513ae9d403b05d9033e891014
- evidence_id: challenge
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-semantic-challenge-agent/semantic-severity-challenge.json
  locator: Final independent challenge
  accessed_at: '2026-10-21T19:51:54.566234Z'
  support: supports
  summary: Actual final recommendation and all bindings verified.
  snapshot_sha256: f699d556265cc1e5d104d239f89b7591284dd02266a6265dbd28c58fee941167
- evidence_id: adjudication
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-root-adjudication.json
  locator: Final root disposition
  accessed_at: '2026-10-21T19:52:26.961789Z'
  support: supports
  summary: Final root adjudication controls severity, grouping and limitations.
  snapshot_sha256: 3d6d81ced6873cdc5fb61ab8584ed5e0e9816986541834d60aeaf8a585eb71d2
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: active bin and inherited aliases'
  outcome: concern
  target_ids:
  - METPO:1000464
  summary: Active METPO identity, parent, predecessor and inherited text are checked
    against the pinned ontology. Faithful import of broad category aliases does not
    establish exact scientific equivalence with a complete growth interval contained
    within 10–14. Parent authorship is not copied into this target.
  evidence_ids:
  - identity
  - metpo-primary
  - bin-scope
  - record
- assessment_id: definition
  area: evidence
  topic: 'Native checklist: numerical bin versus high-pH occurrence'
  outcome: concern
  target_ids:
  - METPO:1000464
  summary: The numerical interval itself is retained. Growing above 10 and belonging
    to a broad alkaliphile category do not establish a complete growth interval within
    10–14. The record’s own canonical deferral preserves that distinction; group its
    above-10 shorthand and exact synonyms once rather than multiplying findings.
  evidence_ids:
  - bin-scope
  - canonical-gap
  - body-krulwich
  - classification-body
  - metpo-primary
- assessment_id: scope
  area: scope
  topic: 'Native checklist: quantitative environmental range'
  outcome: supported
  target_ids:
  - METPO:1000464
  summary: ENVIRONMENT, CLASS and NONMECHANISTIC are compatible with the quantitative
    trait. Generic environmental context is not automatically universal necessity,
    exact endpoint calibration or proof of complete-bin membership.
  evidence_ids:
  - record
  - policy
  - checklist
- assessment_id: canonical
  area: evidence
  topic: 'Native checklist: documented canonical gap'
  outcome: unknown
  target_ids:
  - METPO:1000464
  summary: No canonical organism is supplied. The existing deferral says above-10
    examples can extend below the bin and therefore do not establish a complete contained
    interval. Preserve that bounded gap; no example, new experiment, optimized condition
    or substitute organism is required.
  evidence_ids:
  - canonical-gap
  - record
  - body-krulwich
- assessment_id: bibliography
  area: evidence
  topic: 'Native checklist: all assigned works and separate supplement'
  outcome: concern
  target_ids:
  - METPO:1000464
  summary: Three assigned works resolve across twelve external placements. A separately
    identified classification supplement informs equivalence only. Baker’s inspected
    acidophile abstract does not establish the stated extreme-alkaliphile antiporter
    attribution; this is bounded attribution precision while its full body remains
    unavailable.
  evidence_ids:
  - source-ledger
  - placements
  - source-status
  - meta-baker
  - source-access
  details: "{\n  \"completed_at\": \"2026-10-21T19:48:47.211004+00:00\",\n  \"external_placements\"\
    : [\n    {\n      \"field_path\": \"definition_source\",\n      \"reference\"\
    : \"DOI:10.1038/nrmicro2549\",\n      \"claim\": \"A pH range phenotype in which\
    \ the growth-supporting external pH range spans approximately 10\\u201314, characteristic\
    \ of extreme-alkaliphile physiology.\",\n      \"assessment\": \"Assigned review\
    \ supports extreme alkaline growth examples and generic homeostasis. It does not\
    \ equate all alkaliphiles with a complete growth interval contained10\\u201314.\
    \ Preserve the numerical bin itself and distinguish contextual category/above10\
    \ examples from exact bin membership.\"\n    },\n    {\n      \"field_path\":\
    \ \"evidence[0]\",\n      \"reference\": \"DOI:10.1038/nrmicro2549\",\n      \"\
    snippet\": \"alkaliphiles\",\n      \"notes\": \"pH-homeostasis review supports\
    \ extreme-alkaliphile physiology growing at external pH above 10.\",\n      \"\
    assessment\": \"Exact alkaliphiles occurrence and source-specific above10 context\
    \ positive; this alone is not complete interval membership.\"\n    },\n    {\n\
    \      \"field_path\": \"evidence[1]\",\n      \"reference\": \"DOI:10.1016/j.tim.2007.02.005\"\
    ,\n      \"snippet\": \"proton motive force\",\n      \"notes\": \"pH-homeostasis\
    \ review supports robust Na+/H+ antiporter activity as the extreme-alkaliphile\
    \ mechanism sustaining the proton motive force above pH 10.\",\n      \"assessment\"\
    : \"The inspected Baker abstract is acidophile-scoped. The alkaline antiporter\
    \ attribution exceeds that inspected scope; bounded attribution precision only,\
    \ not a full-paper absence or false-mechanism judgment.\"\n    },\n    {\n   \
    \   \"field_path\": \"causal_graphs[0].edges[0].evidence[0]\",\n      \"reference\"\
    : \"DOI:10.1016/j.tim.2007.02.005\",\n      \"snippet\": \"proton motive force\"\
    ,\n      \"notes\": \"Supports antiporter-driven proton re-import as the extreme-alkaliphile\
    \ mechanism.\",\n      \"assessment\": \"Assigned Baker identity and acidophile\
    \ abstract are verified, but the exact PMF snippet/body and alkaline antiporter\
    \ attribution are not established by the inspected Baker surface. Krulwich separately\
    \ supports generic environmental alkaline antiport context; that support is not\
    \ silently transferred into the Baker citation. Above10 alone is not equivalent\
    \ to a complete growth interval within10\\u201314.\"\n    },\n    {\n      \"\
    field_path\": \"causal_graphs[0].edges[1].evidence[0]\",\n      \"reference\"\
    : \"DOI:10.1038/nrmicro2549\",\n      \"snippet\": \"alkaliphiles\",\n      \"\
    notes\": \"Supports the pH 10\\u201314 range as a value within the pH-range distribution.\"\
    ,\n      \"assessment\": \"Formal parent/bin hierarchy is an ontology question.\
    \ Assigned Krulwich literal alkaliphiles context is positive, but the short excerpt\
    \ does not calibrate this exact complete-interval category.\"\n    },\n    {\n\
    \      \"field_path\": \"causal_graphs[0].edges[2].evidence[0]\",\n      \"reference\"\
    : \"DOI:10.1038/nrmicro2549\",\n      \"notes\": \"The unusual hetero-oligomeric\
    \ Mrp antiporter has an indispensable role at high pH.\",\n      \"assessment\"\
    : \"Krulwich BioC40107 first two sentences directly discuss Mrp in extremely alkaliphilic\
    \ Bacillus. Positive existing contextual attribution; preserve organism scope\
    \ and do not assert necessity in every lineage or exact interval membership. Later\
    \ mutation/mechanistic passages are unassessed.\"\n    },\n    {\n      \"field_path\"\
    : \"causal_graphs[0].edges[3].evidence[0]\",\n      \"reference\": \"DOI:10.1038/nrmicro2549\"\
    ,\n      \"notes\": \"A large transmembrane potential is essential to drive electrogenic\
    \ Na+/H+ and K+/H+ antiporters that import H+.\",\n      \"assessment\": \"Krulwich\
    \ BioC2440/3940 supports generic PMF electrical-component and condition-specific\
    \ environmental context. The exact essential-potential sentence was not independently\
    \ established in this selected-body window; that precision remains limited, not\
    \ false. Detailed efficacy and new mechanistic repair are unassessed.\"\n    },\n\
    \    {\n      \"field_path\": \"causal_graphs[0].edges[4].evidence[0]\",\n   \
    \   \"reference\": \"DOI:10.1038/nrmicro2549\",\n      \"notes\": \"The ongoing\
    \ requirement for cytoplasmic Na+ to support high levels of alkaliphile antiport\
    \ activity is met by numerous Na+/solute symporters.\",\n      \"assessment\"\
    : \"Krulwich BioC41582 first sentence supports the existing Na+/solute symporter\
    \ context for alkaliphile antiport. This generic contextual support does not certify\
    \ every lineage or a complete10\\u201314 interval.\"\n    },\n    {\n      \"\
    field_path\": \"causal_graphs[0].edges[5].evidence[0]\",\n      \"reference\"\
    : \"DOI:10.1038/nrmicro2549\",\n      \"notes\": \"Cytoplasmic Na+ is required\
    \ to support high levels of alkaliphile antiport activity.\",\n      \"assessment\"\
    : \"Same existing BioC41582 context supports substrate availability wording. Formal\
    \ executor-versus-substrate relation semantics are separately assessed by grounding;\
    \ no new biological mechanism or efficacy test proposed.\"\n    },\n    {\n  \
    \    \"field_path\": \"causal_graphs[0].edges[6].evidence[0]\",\n      \"reference\"\
    : \"DOI:10.1038/nrmicro2549\",\n      \"notes\": \"The proton uptake that accompanies\
    \ ATP synthesis by the F1Fo-ATP synthase contributes to alkaliphile pH homeostasis.\"\
    ,\n      \"assessment\": \"Krulwich BioC42119 first sentence directly supports\
    \ proton uptake during ATP synthesis contributing to pH homeostasis in aerobic\
    \ alkaliphilic Bacillus. Preserve that source-specific context; later motif/mutation/optimization\
    \ passages unassessed.\"\n    },\n    {\n      \"field_path\": \"causal_graphs[0].edges[7].evidence[0]\"\
    ,\n      \"reference\": \"DOI:10.1038/nrmicro2549\",\n      \"notes\": \"Alkaline\
    \ pH homeostasis underlies extreme-alkaliphile growth above pH 10.\",\n      \"\
    assessment\": \"Assigned generic environmental pH-homeostasis context positive.\
    \ Growth above10 alone and complete growth interval10\\u201314 are distinct, so\
    \ this branch is not direct calibration of the full interval; group that scope\
    \ issue with exact-category aliases.\"\n    },\n    {\n      \"field_path\": \"\
    causal_graphs[0].edges[8].evidence[0]\",\n      \"reference\": \"DOI:10.1128/AEM.01557-23\"\
    ,\n      \"notes\": \"DIC speciation shifts strongly with pH, toward CO3= above\
    \ ~10.3.\",\n      \"assessment\": \"Assigned AEM actual JATS body paragraph22\
    \ explicitly states carbonate predominates above about pH10.3. Positive existing\
    \ inorganic-carbon chemistry; model/application/genome-toolkit methods and engineering\
    \ implications are not assessed. No numerical correction or new experimental condition\
    \ is proposed.\"\n    }\n  ],\n  \"ontology_grounding_fields\": [\n    {\n   \
    \   \"field_path\": \"causal_graphs[0].nodes[0].grounding\",\n      \"reference\"\
    : \"METPO:1000464\"\n    },\n    {\n      \"field_path\": \"causal_graphs[0].nodes[1].grounding\"\
    ,\n      \"reference\": \"METPO:1000332\"\n    }\n  ],\n  \"synonym_source_fields\"\
    : [\n    {\n      \"field_path\": \"synonyms[0]\",\n      \"synonym\": {\n   \
    \     \"synonym_text\": \"Alkali Tolerant\",\n        \"synonym_type\": \"EXACT_SYNONYM\"\
    ,\n        \"source\": \"metpo.owl\"\n      }\n    },\n    {\n      \"field_path\"\
    : \"synonyms[1]\",\n      \"synonym\": {\n        \"synonym_text\": \"Alkaliphile\"\
    ,\n        \"synonym_type\": \"EXACT_SYNONYM\",\n        \"source\": \"metpo.owl\"\
    \n      }\n    },\n    {\n      \"field_path\": \"synonyms[2]\",\n      \"synonym\"\
    : {\n        \"synonym_text\": \"Extreme Alkaliphile\",\n        \"synonym_type\"\
    : \"EXACT_SYNONYM\",\n        \"source\": \"metpo.owl\"\n      }\n    },\n   \
    \ {\n      \"field_path\": \"synonyms[3]\",\n      \"synonym\": {\n        \"\
    synonym_text\": \"10_to_14\",\n        \"synonym_type\": \"RELATED_SYNONYM\",\n\
    \        \"source\": \"metpo.owl\"\n      }\n    }\n  ],\n  \"scope\": \"Three\
    \ assigned external works across12 placements; separate supplemental classification\
    \ source used only for auditing equivalence. Two structured node grounds and four\
    \ synonym provenance fields are tracked separately.\"\n}"
- assessment_id: snippets
  area: evidence
  topic: 'Native checklist: all four current excerpts'
  outcome: unknown
  target_ids:
  - METPO:1000464
  summary: Both Krulwich alkaliphiles occurrences are literal in retained primary
    body. Both Baker proton-motive-force phrases remain body-unverified. Native four
    NOT_IN_ABSTRACT is retained; unavailable assigned body is not evidence of a false
    quotation, and occurrence in another source is not silently transferred.
  evidence_ids:
  - snippets
  - source-reading
  - native-checks
  - source-access
  details: "{\n  \"completed_at\": \"2026-10-21T19:48:47.212874+00:00\",\n  \"snippets\"\
    : [\n    {\n      \"field_path\": \"evidence[0].snippet\",\n      \"reference\"\
    : \"DOI:10.1038/nrmicro2549\",\n      \"snippet\": \"alkaliphiles\",\n      \"\
    outcome\": \"literal_exact\",\n      \"hits\": [\n        {\n          \"surface\"\
    : \"retained BioC\",\n          \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/krulwich-bioc.xml\"\
    ,\n          \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n          \"locator\": \"passage offset 5466\"\n        },\n        {\n   \
    \       \"surface\": \"retained BioC\",\n          \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/krulwich-bioc.xml\"\
    ,\n          \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n          \"locator\": \"passage offset 15130\"\n        },\n        {\n  \
    \        \"surface\": \"retained BioC\",\n          \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/krulwich-bioc.xml\"\
    ,\n          \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n          \"locator\": \"passage offset 16479\"\n        },\n        {\n  \
    \        \"surface\": \"retained BioC\",\n          \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/krulwich-bioc.xml\"\
    ,\n          \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n          \"locator\": \"passage offset 39232\"\n        },\n        {\n  \
    \        \"surface\": \"retained BioC\",\n          \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/krulwich-bioc.xml\"\
    ,\n          \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n          \"locator\": \"passage offset 39253\"\n        },\n        {\n  \
    \        \"surface\": \"retained BioC\",\n          \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/krulwich-bioc.xml\"\
    ,\n          \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n          \"locator\": \"passage offset 41582\"\n        },\n        {\n  \
    \        \"surface\": \"retained BioC\",\n          \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/krulwich-bioc.xml\"\
    ,\n          \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n          \"locator\": \"passage offset 42119\"\n        },\n        {\n  \
    \        \"surface\": \"retained BioC\",\n          \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/krulwich-bioc.xml\"\
    ,\n          \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n          \"locator\": \"passage offset 45597\"\n        },\n        {\n  \
    \        \"surface\": \"retained BioC\",\n          \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/krulwich-bioc.xml\"\
    ,\n          \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n          \"locator\": \"passage offset 61656\"\n        }\n      ],\n    \
    \  \"scope\": \"Literal occurrence only. Missing abstract match with unavailable\
    \ assigned body is unknown, not a false-quote finding.\"\n    },\n    {\n    \
    \  \"field_path\": \"evidence[1].snippet\",\n      \"reference\": \"DOI:10.1016/j.tim.2007.02.005\"\
    ,\n      \"snippet\": \"proton motive force\",\n      \"outcome\": \"body_unknown\"\
    ,\n      \"hits\": [],\n      \"scope\": \"Literal occurrence only. Missing abstract\
    \ match with unavailable assigned body is unknown, not a false-quote finding.\"\
    \n    },\n    {\n      \"field_path\": \"causal_graphs[0].edges[0].evidence[0].snippet\"\
    ,\n      \"reference\": \"DOI:10.1016/j.tim.2007.02.005\",\n      \"snippet\"\
    : \"proton motive force\",\n      \"outcome\": \"body_unknown\",\n      \"hits\"\
    : [],\n      \"scope\": \"Literal occurrence only. Missing abstract match with\
    \ unavailable assigned body is unknown, not a false-quote finding.\"\n    },\n\
    \    {\n      \"field_path\": \"causal_graphs[0].edges[1].evidence[0].snippet\"\
    ,\n      \"reference\": \"DOI:10.1038/nrmicro2549\",\n      \"snippet\": \"alkaliphiles\"\
    ,\n      \"outcome\": \"literal_exact\",\n      \"hits\": [\n        {\n     \
    \     \"surface\": \"retained BioC\",\n          \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/krulwich-bioc.xml\"\
    ,\n          \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n          \"locator\": \"passage offset 5466\"\n        },\n        {\n   \
    \       \"surface\": \"retained BioC\",\n          \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/krulwich-bioc.xml\"\
    ,\n          \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n          \"locator\": \"passage offset 15130\"\n        },\n        {\n  \
    \        \"surface\": \"retained BioC\",\n          \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/krulwich-bioc.xml\"\
    ,\n          \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n          \"locator\": \"passage offset 16479\"\n        },\n        {\n  \
    \        \"surface\": \"retained BioC\",\n          \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/krulwich-bioc.xml\"\
    ,\n          \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n          \"locator\": \"passage offset 39232\"\n        },\n        {\n  \
    \        \"surface\": \"retained BioC\",\n          \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/krulwich-bioc.xml\"\
    ,\n          \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n          \"locator\": \"passage offset 39253\"\n        },\n        {\n  \
    \        \"surface\": \"retained BioC\",\n          \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/krulwich-bioc.xml\"\
    ,\n          \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n          \"locator\": \"passage offset 41582\"\n        },\n        {\n  \
    \        \"surface\": \"retained BioC\",\n          \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/krulwich-bioc.xml\"\
    ,\n          \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n          \"locator\": \"passage offset 42119\"\n        },\n        {\n  \
    \        \"surface\": \"retained BioC\",\n          \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/krulwich-bioc.xml\"\
    ,\n          \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n          \"locator\": \"passage offset 45597\"\n        },\n        {\n  \
    \        \"surface\": \"retained BioC\",\n          \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-source-agent/krulwich-bioc.xml\"\
    ,\n          \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n          \"locator\": \"passage offset 61656\"\n        }\n      ],\n    \
    \  \"scope\": \"Literal occurrence only. Missing abstract match with unavailable\
    \ assigned body is unknown, not a false-quote finding.\"\n    }\n  ],\n  \"counts\"\
    : {\n    \"fields\": 4,\n    \"literal_exact\": 2,\n    \"body_unknown\": 2\n\
    \  },\n  \"native_result\": {\n    \"verified\": 0,\n    \"not_in_abstract\":\
    \ 4\n  },\n  \"qualification\": \"Both Krulwich alkaliphiles occurrences are exact\
    \ in retained body. Both Baker proton-motive-force occurrences remain unverified\
    \ because assigned body is unavailable; occurrence elsewhere is not transferred\
    \ between sources.\"\n}"
- assessment_id: nodes
  area: grounding
  topic: 'Native checklist: all current node referents'
  outcome: concern
  target_ids:
  - METPO:1000464
  summary: All eleven nodes are assessed. Three contextual protein/complex classes
    are label-only and the sodium pool is material. Carbonate node 10 combines a material
    label/type with a description of a speciation shift; retain that bounded precision
    concern without diagnosing false chemistry.
  evidence_ids:
  - node-edges
  - schema
  - policy
  - body-aem
  details: "[\n  {\n    \"index\": 0,\n    \"field_path\": \"causal_graphs[0].nodes[0]\"\
    ,\n    \"current\": {\n      \"node_id\": \"ph_range_high_trait\",\n      \"label\"\
    : \"pH range high\",\n      \"node_type\": \"TRAIT\",\n      \"grounding\": \"\
    METPO:1000464\",\n      \"description\": \"pH growth-supporting range extending\
    \ above ~10.\"\n    },\n    \"status\": \"scope_finding\",\n    \"assessment\"\
    : \"Active trait identity is correct. The description extends the range above\
    \ approximately 10, which is weaker than the complete-interval convention stated\
    \ in the current canonical deferral. This is grouped with exact category aliases,\
    \ not a second numerical-OWL error.\"\n  },\n  {\n    \"index\": 1,\n    \"field_path\"\
    : \"causal_graphs[0].nodes[1]\",\n    \"current\": {\n      \"node_id\": \"ph_range\"\
    ,\n      \"label\": \"pH range\",\n      \"node_type\": \"TRAIT\",\n      \"grounding\"\
    : \"METPO:1000332\",\n      \"description\": \"Span of external pH values supporting\
    \ growth.\"\n    },\n    \"status\": \"supported\",\n    \"assessment\": \"Current\
    \ pH range parent identity and span meaning agree with the imported hierarchy.\"\
    \n  },\n  {\n    \"index\": 2,\n    \"field_path\": \"causal_graphs[0].nodes[2]\"\
    ,\n    \"current\": {\n      \"node_id\": \"extreme_alkaliphile_antiport\",\n\
    \      \"label\": \"extreme-alkaliphile Na+/H+ antiport\",\n      \"node_type\"\
    : \"BIOLOGICAL_PROCESS\",\n      \"description\": \"Robust Na+/H+ antiporter activity\
    \ importing H+ at strongly alkaline external pH.\"\n    },\n    \"status\": \"\
    supported_facet\",\n    \"assessment\": \"The node explicitly denotes antiport\
    \ activity; BIOLOGICAL_PROCESS is a coherent process facet. Detailed efficacy\
    \ is outside this documentary assessment.\"\n  },\n  {\n    \"index\": 3,\n  \
    \  \"field_path\": \"causal_graphs[0].nodes[3]\",\n    \"current\": {\n      \"\
    node_id\": \"mrp_antiporter_complex\",\n      \"label\": \"Mrp Na+/H+ antiporter\
    \ complex\",\n      \"node_type\": \"GENE_OR_PROTEIN\",\n      \"grounding_status\"\
    : \"REVIEWED_LABEL_ONLY\",\n      \"grounding_notes\": \"Reviewed as a contextual\
    \ protein or protein-complex label within a quantitative measurement graph; no\
    \ exact semantic family term was established for this aggregate use.\",\n    \
    \  \"description\": \"Hetero-oligomeric CPA3-family Na+/H+ antiporter complex\
    \ essential at high external pH.\",\n      \"gene_symbols\": [\n        \"mrpA\"\
    ,\n        \"mrpB\",\n        \"mrpC\",\n        \"mrpD\",\n        \"mrpE\",\n\
    \        \"mrpF\",\n        \"mrpG\"\n      ],\n      \"operon\": \"mrpA-G\"\n\
    \    },\n    \"status\": \"supported_facet\",\n    \"assessment\": \"Material\
    \ protein-complex class is coherent. Gene symbols and operon metadata do not make\
    \ a separate genetic-element node mandatory. Reviewed label-only disposition is\
    \ explicit.\"\n  },\n  {\n    \"index\": 4,\n    \"field_path\": \"causal_graphs[0].nodes[4]\"\
    ,\n    \"current\": {\n      \"node_id\": \"membrane_potential\",\n      \"label\"\
    : \"transmembrane potential (delta-psi)\",\n      \"node_type\": \"QUALITY\",\n\
    \      \"description\": \"Large transmembrane electrical potential energizing\
    \ electrogenic cation/H+ antiport.\"\n    },\n    \"status\": \"supported_facet\"\
    ,\n    \"assessment\": \"An electrical potential can be represented as a measurable\
    \ QUALITY. The STATE alternative does not establish an automatic typing error.\"\
    \n  },\n  {\n    \"index\": 5,\n    \"field_path\": \"causal_graphs[0].nodes[5]\"\
    ,\n    \"current\": {\n      \"node_id\": \"na_solute_symporters\",\n      \"\
    label\": \"Na+/solute symporters\",\n      \"node_type\": \"GENE_OR_PROTEIN\"\
    ,\n      \"grounding_status\": \"REVIEWED_LABEL_ONLY\",\n      \"grounding_notes\"\
    : \"Reviewed as a contextual protein or protein-complex label within a quantitative\
    \ measurement graph; no exact semantic family term was established for this aggregate\
    \ use.\",\n      \"description\": \"Symporters re-importing Na+ with solutes to\
    \ supply cytoplasmic Na+ for antiport.\"\n    },\n    \"status\": \"supported_facet\"\
    ,\n    \"assessment\": \"Material symporter protein class and reviewed label-only\
    \ disposition are coherent; no mandatory instance or functional grounding is inferred.\"\
    \n  },\n  {\n    \"index\": 6,\n    \"field_path\": \"causal_graphs[0].nodes[6]\"\
    ,\n    \"current\": {\n      \"node_id\": \"cytoplasmic_na\",\n      \"label\"\
    : \"cytoplasmic Na+\",\n      \"node_type\": \"CHEMICAL\",\n      \"description\"\
    : \"Intracellular sodium pool required to sustain alkaliphile antiport activity.\"\
    \n    },\n    \"status\": \"supported_facet\",\n    \"assessment\": \"The intracellular\
    \ sodium pool has a material chemical referent. No blanket CHEMICAL exclusion\
    \ applies to causal executor relations.\"\n  },\n  {\n    \"index\": 7,\n    \"\
    field_path\": \"causal_graphs[0].nodes[7]\",\n    \"current\": {\n      \"node_id\"\
    : \"f1fo_atp_synthase\",\n      \"label\": \"F1Fo-ATP synthase\",\n      \"node_type\"\
    : \"GENE_OR_PROTEIN\",\n      \"grounding_status\": \"REVIEWED_LABEL_ONLY\",\n\
    \      \"grounding_notes\": \"Reviewed as a contextual protein or protein-complex\
    \ label within a quantitative measurement graph; no exact semantic family term\
    \ was established for this aggregate use.\",\n      \"description\": \"Proton-translocating\
    \ ATP synthase whose proton uptake contributes to pH homeostasis.\"\n    },\n\
    \    \"status\": \"supported_facet\",\n    \"assessment\": \"ATP synthase is a\
    \ material protein complex, and the label-only disposition is explicit.\"\n  },\n\
    \  {\n    \"index\": 8,\n    \"field_path\": \"causal_graphs[0].nodes[8]\",\n\
    \    \"current\": {\n      \"node_id\": \"alkaline_ph_homeostasis\",\n      \"\
    label\": \"alkaline pH homeostasis\",\n      \"node_type\": \"BIOLOGICAL_PROCESS\"\
    ,\n      \"description\": \"Maintenance of a near-neutral cytoplasmic pH against\
    \ a strongly alkaline exterior.\"\n    },\n    \"status\": \"supported_facet\"\
    ,\n    \"assessment\": \"The description explicitly denotes maintenance, supporting\
    \ a process reading. Source-specific physiological scope remains separate from\
    \ ontology endpoint checks.\"\n  },\n  {\n    \"index\": 9,\n    \"field_path\"\
    : \"causal_graphs[0].nodes[9]\",\n    \"current\": {\n      \"node_id\": \"external_ph_high\"\
    ,\n      \"label\": \"external pH > 10.3\",\n      \"node_type\": \"ENVIRONMENTAL_FACTOR\"\
    ,\n      \"description\": \"Strongly alkaline external pH above ~10.3.\"\n   \
    \ },\n    \"status\": \"supported_facet\",\n    \"assessment\": \"External high\
    \ pH is an environmental condition, and its current free-text relation does not\
    \ import a process-domain restriction.\"\n  },\n  {\n    \"index\": 10,\n    \"\
    field_path\": \"causal_graphs[0].nodes[10]\",\n    \"current\": {\n      \"node_id\"\
    : \"carbonate_speciation\",\n      \"label\": \"carbonate (CO3 2-) speciation\"\
    ,\n      \"node_type\": \"CHEMICAL\",\n      \"description\": \"Shift of dissolved\
    \ inorganic carbon toward carbonate at high pH.\"\n    },\n    \"status\": \"\
    minor_precision_candidate\",\n    \"assessment\": \"CHEMICAL can denote carbonate\
    \ material, but both the label and description also describe speciation or a shift\
    \ in speciation. Clarify the intended material versus change referent without\
    \ requiring a particular replacement enum or denying the source chemistry.\"\n\
    \  }\n]"
- assessment_id: relations
  area: consistency
  topic: 'Native checklist: all nine formal and descriptive roles'
  outcome: concern
  target_ids:
  - METPO:1000464
  summary: Both imported RO relations have compatible material/process endpoints.
    Edge 5 nevertheless uses enables for a substrate pool, raising bounded executor-versus-substrate
    precision. Edge 6 is positive. Local confers and free-text relations receive no
    invented formal endpoint constraints; bin-membership support remains the separate
    grouped scope issue.
  evidence_ids:
  - node-edges
  - ro-primary
  - local-authority
  - challenge
  details: "[\n  {\n    \"index\": 0,\n    \"field_path\": \"causal_graphs[0].edges[0]\"\
    ,\n    \"current\": {\n      \"subject\": \"extreme_alkaliphile_antiport\",\n\
    \      \"predicate\": \"confers\",\n      \"object\": \"ph_range_high_trait\"\
    ,\n      \"description\": \"Robust Na+/H+ antiport enables growth at pH > 10.\"\
    ,\n      \"evidence\": [\n        {\n          \"reference\": \"DOI:10.1016/j.tim.2007.02.005\"\
    ,\n          \"snippet\": \"proton motive force\",\n          \"notes\": \"Supports\
    \ antiporter-driven proton re-import as the extreme-alkaliphile mechanism.\"\n\
    \        }\n      ],\n      \"predicate_id\": \"METPO:2007700\"\n    },\n    \"\
    status\": \"scope_finding\",\n    \"assessment\": \"The local confers domain and\
    \ range admit these causal nodes. Growth above 10 alone is weaker than membership\
    \ under the current complete-interval convention; this is part of the grouped\
    \ scope finding.\"\n  },\n  {\n    \"index\": 1,\n    \"field_path\": \"causal_graphs[0].edges[1]\"\
    ,\n    \"current\": {\n      \"subject\": \"ph_range_high_trait\",\n      \"predicate\"\
    : \"is a\",\n      \"object\": \"ph_range\",\n      \"description\": \"pH range\
    \ high is a quantitative bin of the pH-range phenotype.\",\n      \"evidence\"\
    : [\n        {\n          \"reference\": \"DOI:10.1038/nrmicro2549\",\n      \
    \    \"snippet\": \"alkaliphiles\",\n          \"notes\": \"Supports the pH 10\\\
    u201314 range as a value within the pH-range distribution.\"\n        }\n    \
    \  ],\n      \"predicate_id\": \"rdfs:subClassOf\"\n    },\n    \"status\": \"\
    supported_relation_scope_limit\",\n    \"assessment\": \"The rdfs subclass relation\
    \ and parent identity are correct. The assigned source note treating 10\\u201314\
    \ as the source-supported range is part of the same bin-scope question, not a\
    \ second hierarchy failure.\"\n  },\n  {\n    \"index\": 2,\n    \"field_path\"\
    : \"causal_graphs[0].edges[2]\",\n    \"current\": {\n      \"subject\": \"mrp_antiporter_complex\"\
    ,\n      \"predicate\": \"confers\",\n      \"object\": \"ph_range_high_trait\"\
    ,\n      \"description\": \"The hetero-oligomeric Mrp antiporter has an indispensable\
    \ role in growth at high pH.\",\n      \"evidence\": [\n        {\n          \"\
    reference\": \"DOI:10.1038/nrmicro2549\",\n          \"notes\": \"The unusual\
    \ hetero-oligomeric Mrp antiporter has an indispensable role at high pH.\"\n \
    \       }\n      ],\n      \"predicate_id\": \"METPO:2007700\"\n    },\n    \"\
    status\": \"scope_finding\",\n    \"assessment\": \"The protein-to-trait confers\
    \ endpoints fit the local broad relation. Generic high-pH context does not by\
    \ itself establish the current complete-interval bin.\"\n  },\n  {\n    \"index\"\
    : 3,\n    \"field_path\": \"causal_graphs[0].edges[3]\",\n    \"current\": {\n\
    \      \"subject\": \"membrane_potential\",\n      \"predicate\": \"drives\",\n\
    \      \"object\": \"mrp_antiporter_complex\",\n      \"description\": \"A large\
    \ transmembrane potential drives electrogenic Na+/H+ antiport that imports H+.\"\
    ,\n      \"evidence\": [\n        {\n          \"reference\": \"DOI:10.1038/nrmicro2549\"\
    ,\n          \"notes\": \"A large transmembrane potential is essential to drive\
    \ electrogenic Na+/H+ and K+/H+ antiporters that import H+.\"\n        }\n   \
    \   ]\n    },\n    \"status\": \"supported_formal_scope\",\n    \"assessment\"\
    : \"Free-text drives has no imported domain or range in this edge. The QUALITY\
    \ subject is not an automatic error; detailed efficacy is unassessed.\"\n  },\n\
    \  {\n    \"index\": 4,\n    \"field_path\": \"causal_graphs[0].edges[4]\",\n\
    \    \"current\": {\n      \"subject\": \"na_solute_symporters\",\n      \"predicate\"\
    : \"supplies\",\n      \"object\": \"cytoplasmic_na\",\n      \"description\"\
    : \"Na+/solute symporters supply the cytoplasmic Na+ required to sustain antiport\
    \ activity.\",\n      \"evidence\": [\n        {\n          \"reference\": \"\
    DOI:10.1038/nrmicro2549\",\n          \"notes\": \"The ongoing requirement for\
    \ cytoplasmic Na+ to support high levels of alkaliphile antiport activity is met\
    \ by numerous Na+/solute symporters.\"\n        }\n      ]\n    },\n    \"status\"\
    : \"supported_formal_scope\",\n    \"assessment\": \"Free-text supplies has no\
    \ imported domain or range in this edge. Material actor and chemical pool are\
    \ coherent documentary referents.\"\n  },\n  {\n    \"index\": 5,\n    \"field_path\"\
    : \"causal_graphs[0].edges[5]\",\n    \"current\": {\n      \"subject\": \"cytoplasmic_na\"\
    ,\n      \"predicate\": \"enables\",\n      \"object\": \"extreme_alkaliphile_antiport\"\
    ,\n      \"description\": \"Cytoplasmic Na+ is the substrate that sustains high\
    \ levels of alkaliphile antiport activity.\",\n      \"evidence\": [\n       \
    \ {\n          \"reference\": \"DOI:10.1038/nrmicro2549\",\n          \"notes\"\
    : \"Cytoplasmic Na+ is required to support high levels of alkaliphile antiport\
    \ activity.\"\n        }\n      ],\n      \"predicate_id\": \"RO:0002327\"\n \
    \   },\n    \"status\": \"minor_semantic_precision_candidate\",\n    \"assessment\"\
    : \"RO:0002327 admits a material subject and process object here. Its definition\
    \ additionally says the subject acts to execute the process, while this record\
    \ expressly calls sodium the substrate. This is a bounded executor-versus-substrate\
    \ precision issue, not a categorical type error or a denial that sodium supports\
    \ the process.\"\n  },\n  {\n    \"index\": 6,\n    \"field_path\": \"causal_graphs[0].edges[6]\"\
    ,\n    \"current\": {\n      \"subject\": \"f1fo_atp_synthase\",\n      \"predicate\"\
    : \"contributes to\",\n      \"object\": \"alkaline_ph_homeostasis\",\n      \"\
    description\": \"Proton uptake accompanying ATP synthesis contributes to alkaliphile\
    \ pH homeostasis.\",\n      \"evidence\": [\n        {\n          \"reference\"\
    : \"DOI:10.1038/nrmicro2549\",\n          \"notes\": \"The proton uptake that\
    \ accompanies ATP synthesis by the F1Fo-ATP synthase contributes to alkaliphile\
    \ pH homeostasis.\"\n        }\n      ],\n      \"predicate_id\": \"RO:0002326\"\
    \n    },\n    \"status\": \"supported_formal_scope\",\n    \"assessment\": \"\
    The material ATP-synthase subject and maintenance-process object satisfy the actual\
    \ inherited RO:0002326 endpoint constraints. The annotation usage note is not\
    \ a global molecular-function-only range restriction.\"\n  },\n  {\n    \"index\"\
    : 7,\n    \"field_path\": \"causal_graphs[0].edges[7]\",\n    \"current\": {\n\
    \      \"subject\": \"alkaline_ph_homeostasis\",\n      \"predicate\": \"confers\"\
    ,\n      \"object\": \"ph_range_high_trait\",\n      \"description\": \"Maintenance\
    \ of cytoplasmic pH homeostasis enables growth at strongly alkaline external pH.\"\
    ,\n      \"evidence\": [\n        {\n          \"reference\": \"DOI:10.1038/nrmicro2549\"\
    ,\n          \"notes\": \"Alkaline pH homeostasis underlies extreme-alkaliphile\
    \ growth above pH 10.\"\n        }\n      ],\n      \"predicate_id\": \"METPO:2007700\"\
    \n    },\n    \"status\": \"scope_finding\",\n    \"assessment\": \"Local confers\
    \ admits the process and trait endpoints. The above-10 biological context is weaker\
    \ than the complete-interval bin and is grouped with the same scope finding.\"\
    \n  },\n  {\n    \"index\": 8,\n    \"field_path\": \"causal_graphs[0].edges[8]\"\
    ,\n    \"current\": {\n      \"subject\": \"external_ph_high\",\n      \"predicate\"\
    : \"shifts speciation toward\",\n      \"object\": \"carbonate_speciation\",\n\
    \      \"description\": \"External pH above ~10.3 shifts dissolved inorganic carbon\
    \ speciation toward carbonate.\",\n      \"evidence\": [\n        {\n        \
    \  \"reference\": \"DOI:10.1128/AEM.01557-23\",\n          \"notes\": \"DIC speciation\
    \ shifts strongly with pH, toward CO3= above ~10.3.\"\n        }\n      ]\n  \
    \  },\n    \"status\": \"minor_node_facet_context\",\n    \"assessment\": \"The\
    \ free-text predicate can target carbonate material. Node 10 wording also describes\
    \ a shift, so the minor concerns referent clarity rather than an imported formal\
    \ constraint or false chemistry.\"\n  }\n]"
- assessment_id: biological-scope
  area: scope
  topic: 'Native checklist: generic environmental and inorganic-carbon support'
  outcome: unknown
  target_ids:
  - METPO:1000464
  summary: Selected source-specific Bacillus homeostasis context and the AEM carbonate
    chemistry are positive. Detailed pathogen defense, fitness, AMR, mutation/perturbation
    efficacy, engineering and intervention optimization remain UNASSESSED_SCOPE. No
    new biological route, repair or experimental recommendation is supplied.
  evidence_ids:
  - edge-sources
  - source-reading
  - body-aem
  - body-krulwich
  - source-access
  details: "{\n  \"completed_at\": \"2026-10-21T19:48:47.211139+00:00\",\n  \"edges\"\
    : [\n    {\n      \"index\": 0,\n      \"field_path\": \"causal_graphs[0].edges[0]\"\
    ,\n      \"subject\": \"extreme_alkaliphile_antiport\",\n      \"predicate\":\
    \ \"confers\",\n      \"predicate_id\": \"METPO:2007700\",\n      \"object\":\
    \ \"ph_range_high_trait\",\n      \"description\": \"Robust Na+/H+ antiport enables\
    \ growth at pH > 10.\",\n      \"evidence\": [\n        {\n          \"reference\"\
    : \"DOI:10.1016/j.tim.2007.02.005\",\n          \"snippet\": \"proton motive force\"\
    ,\n          \"notes\": \"Supports antiporter-driven proton re-import as the extreme-alkaliphile\
    \ mechanism.\"\n        }\n      ],\n      \"assessment\": \"Assigned Baker identity\
    \ and acidophile abstract are verified, but the exact PMF snippet/body and alkaline\
    \ antiporter attribution are not established by the inspected Baker surface. Krulwich\
    \ separately supports generic environmental alkaline antiport context; that support\
    \ is not silently transferred into the Baker citation. Above10 alone is not equivalent\
    \ to a complete growth interval within10\\u201314.\",\n      \"scope\": \"Generic\
    \ existing environmental context/documentary attribution; no detailed pathogen\
    \ defense/fitness/AMR, perturbation efficacy or optimization.\"\n    },\n    {\n\
    \      \"index\": 1,\n      \"field_path\": \"causal_graphs[0].edges[1]\",\n \
    \     \"subject\": \"ph_range_high_trait\",\n      \"predicate\": \"is a\",\n\
    \      \"predicate_id\": \"rdfs:subClassOf\",\n      \"object\": \"ph_range\"\
    ,\n      \"description\": \"pH range high is a quantitative bin of the pH-range\
    \ phenotype.\",\n      \"evidence\": [\n        {\n          \"reference\": \"\
    DOI:10.1038/nrmicro2549\",\n          \"snippet\": \"alkaliphiles\",\n       \
    \   \"notes\": \"Supports the pH 10\\u201314 range as a value within the pH-range\
    \ distribution.\"\n        }\n      ],\n      \"assessment\": \"Formal parent/bin\
    \ hierarchy is an ontology question. Assigned Krulwich literal alkaliphiles context\
    \ is positive, but the short excerpt does not calibrate this exact complete-interval\
    \ category.\",\n      \"scope\": \"Generic existing environmental context/documentary\
    \ attribution; no detailed pathogen defense/fitness/AMR, perturbation efficacy\
    \ or optimization.\"\n    },\n    {\n      \"index\": 2,\n      \"field_path\"\
    : \"causal_graphs[0].edges[2]\",\n      \"subject\": \"mrp_antiporter_complex\"\
    ,\n      \"predicate\": \"confers\",\n      \"predicate_id\": \"METPO:2007700\"\
    ,\n      \"object\": \"ph_range_high_trait\",\n      \"description\": \"The hetero-oligomeric\
    \ Mrp antiporter has an indispensable role in growth at high pH.\",\n      \"\
    evidence\": [\n        {\n          \"reference\": \"DOI:10.1038/nrmicro2549\"\
    ,\n          \"notes\": \"The unusual hetero-oligomeric Mrp antiporter has an\
    \ indispensable role at high pH.\"\n        }\n      ],\n      \"assessment\"\
    : \"Krulwich BioC40107 first two sentences directly discuss Mrp in extremely alkaliphilic\
    \ Bacillus. Positive existing contextual attribution; preserve organism scope\
    \ and do not assert necessity in every lineage or exact interval membership. Later\
    \ mutation/mechanistic passages are unassessed.\",\n      \"scope\": \"Generic\
    \ existing environmental context/documentary attribution; no detailed pathogen\
    \ defense/fitness/AMR, perturbation efficacy or optimization.\"\n    },\n    {\n\
    \      \"index\": 3,\n      \"field_path\": \"causal_graphs[0].edges[3]\",\n \
    \     \"subject\": \"membrane_potential\",\n      \"predicate\": \"drives\",\n\
    \      \"predicate_id\": null,\n      \"object\": \"mrp_antiporter_complex\",\n\
    \      \"description\": \"A large transmembrane potential drives electrogenic\
    \ Na+/H+ antiport that imports H+.\",\n      \"evidence\": [\n        {\n    \
    \      \"reference\": \"DOI:10.1038/nrmicro2549\",\n          \"notes\": \"A large\
    \ transmembrane potential is essential to drive electrogenic Na+/H+ and K+/H+\
    \ antiporters that import H+.\"\n        }\n      ],\n      \"assessment\": \"\
    Krulwich BioC2440/3940 supports generic PMF electrical-component and condition-specific\
    \ environmental context. The exact essential-potential sentence was not independently\
    \ established in this selected-body window; that precision remains limited, not\
    \ false. Detailed efficacy and new mechanistic repair are unassessed.\",\n   \
    \   \"scope\": \"Generic existing environmental context/documentary attribution;\
    \ no detailed pathogen defense/fitness/AMR, perturbation efficacy or optimization.\"\
    \n    },\n    {\n      \"index\": 4,\n      \"field_path\": \"causal_graphs[0].edges[4]\"\
    ,\n      \"subject\": \"na_solute_symporters\",\n      \"predicate\": \"supplies\"\
    ,\n      \"predicate_id\": null,\n      \"object\": \"cytoplasmic_na\",\n    \
    \  \"description\": \"Na+/solute symporters supply the cytoplasmic Na+ required\
    \ to sustain antiport activity.\",\n      \"evidence\": [\n        {\n       \
    \   \"reference\": \"DOI:10.1038/nrmicro2549\",\n          \"notes\": \"The ongoing\
    \ requirement for cytoplasmic Na+ to support high levels of alkaliphile antiport\
    \ activity is met by numerous Na+/solute symporters.\"\n        }\n      ],\n\
    \      \"assessment\": \"Krulwich BioC41582 first sentence supports the existing\
    \ Na+/solute symporter context for alkaliphile antiport. This generic contextual\
    \ support does not certify every lineage or a complete10\\u201314 interval.\"\
    ,\n      \"scope\": \"Generic existing environmental context/documentary attribution;\
    \ no detailed pathogen defense/fitness/AMR, perturbation efficacy or optimization.\"\
    \n    },\n    {\n      \"index\": 5,\n      \"field_path\": \"causal_graphs[0].edges[5]\"\
    ,\n      \"subject\": \"cytoplasmic_na\",\n      \"predicate\": \"enables\",\n\
    \      \"predicate_id\": \"RO:0002327\",\n      \"object\": \"extreme_alkaliphile_antiport\"\
    ,\n      \"description\": \"Cytoplasmic Na+ is the substrate that sustains high\
    \ levels of alkaliphile antiport activity.\",\n      \"evidence\": [\n       \
    \ {\n          \"reference\": \"DOI:10.1038/nrmicro2549\",\n          \"notes\"\
    : \"Cytoplasmic Na+ is required to support high levels of alkaliphile antiport\
    \ activity.\"\n        }\n      ],\n      \"assessment\": \"Same existing BioC41582\
    \ context supports substrate availability wording. Formal executor-versus-substrate\
    \ relation semantics are separately assessed by grounding; no new biological mechanism\
    \ or efficacy test proposed.\",\n      \"scope\": \"Generic existing environmental\
    \ context/documentary attribution; no detailed pathogen defense/fitness/AMR, perturbation\
    \ efficacy or optimization.\"\n    },\n    {\n      \"index\": 6,\n      \"field_path\"\
    : \"causal_graphs[0].edges[6]\",\n      \"subject\": \"f1fo_atp_synthase\",\n\
    \      \"predicate\": \"contributes to\",\n      \"predicate_id\": \"RO:0002326\"\
    ,\n      \"object\": \"alkaline_ph_homeostasis\",\n      \"description\": \"Proton\
    \ uptake accompanying ATP synthesis contributes to alkaliphile pH homeostasis.\"\
    ,\n      \"evidence\": [\n        {\n          \"reference\": \"DOI:10.1038/nrmicro2549\"\
    ,\n          \"notes\": \"The proton uptake that accompanies ATP synthesis by\
    \ the F1Fo-ATP synthase contributes to alkaliphile pH homeostasis.\"\n       \
    \ }\n      ],\n      \"assessment\": \"Krulwich BioC42119 first sentence directly\
    \ supports proton uptake during ATP synthesis contributing to pH homeostasis in\
    \ aerobic alkaliphilic Bacillus. Preserve that source-specific context; later\
    \ motif/mutation/optimization passages unassessed.\",\n      \"scope\": \"Generic\
    \ existing environmental context/documentary attribution; no detailed pathogen\
    \ defense/fitness/AMR, perturbation efficacy or optimization.\"\n    },\n    {\n\
    \      \"index\": 7,\n      \"field_path\": \"causal_graphs[0].edges[7]\",\n \
    \     \"subject\": \"alkaline_ph_homeostasis\",\n      \"predicate\": \"confers\"\
    ,\n      \"predicate_id\": \"METPO:2007700\",\n      \"object\": \"ph_range_high_trait\"\
    ,\n      \"description\": \"Maintenance of cytoplasmic pH homeostasis enables\
    \ growth at strongly alkaline external pH.\",\n      \"evidence\": [\n       \
    \ {\n          \"reference\": \"DOI:10.1038/nrmicro2549\",\n          \"notes\"\
    : \"Alkaline pH homeostasis underlies extreme-alkaliphile growth above pH 10.\"\
    \n        }\n      ],\n      \"assessment\": \"Assigned generic environmental\
    \ pH-homeostasis context positive. Growth above10 alone and complete growth interval10\\\
    u201314 are distinct, so this branch is not direct calibration of the full interval;\
    \ group that scope issue with exact-category aliases.\",\n      \"scope\": \"\
    Generic existing environmental context/documentary attribution; no detailed pathogen\
    \ defense/fitness/AMR, perturbation efficacy or optimization.\"\n    },\n    {\n\
    \      \"index\": 8,\n      \"field_path\": \"causal_graphs[0].edges[8]\",\n \
    \     \"subject\": \"external_ph_high\",\n      \"predicate\": \"shifts speciation\
    \ toward\",\n      \"predicate_id\": null,\n      \"object\": \"carbonate_speciation\"\
    ,\n      \"description\": \"External pH above ~10.3 shifts dissolved inorganic\
    \ carbon speciation toward carbonate.\",\n      \"evidence\": [\n        {\n \
    \         \"reference\": \"DOI:10.1128/AEM.01557-23\",\n          \"notes\": \"\
    DIC speciation shifts strongly with pH, toward CO3= above ~10.3.\"\n        }\n\
    \      ],\n      \"assessment\": \"Assigned AEM actual JATS body paragraph22 explicitly\
    \ states carbonate predominates above about pH10.3. Positive existing inorganic-carbon\
    \ chemistry; model/application/genome-toolkit methods and engineering implications\
    \ are not assessed. No numerical correction or new experimental condition is proposed.\"\
    ,\n      \"scope\": \"Generic existing environmental context/documentary attribution;\
    \ no detailed pathogen defense/fitness/AMR, perturbation efficacy or optimization.\"\
    \n    }\n  ]\n}"
- assessment_id: completeness
  area: completeness
  topic: 'Native checklist: current graph and optional evidence'
  outcome: supported
  target_ids:
  - METPO:1000464
  summary: All eleven nodes, nine edges, two components, four excerpts and ten record
    events are covered. Three reviewed label-only protein classes and zero instances
    are appropriate contextual representation. The explicit canonical gap, lack of
    token accessions or additional connectors is not an automatic completeness defect.
  evidence_ids:
  - record
  - node-edges
  - node-sources
  - canonical-gap
  - policy
  - checklist
  details: "{\n  \"completed_at\": \"2026-10-21T19:48:47.211294+00:00\",\n  \"nodes\"\
    : [\n    {\n      \"index\": 0,\n      \"field_path\": \"causal_graphs[0].nodes[0]\"\
    ,\n      \"node\": {\n        \"node_id\": \"ph_range_high_trait\",\n        \"\
    label\": \"pH range high\",\n        \"node_type\": \"TRAIT\",\n        \"grounding\"\
    : \"METPO:1000464\",\n        \"description\": \"pH growth-supporting range extending\
    \ above ~10.\"\n      },\n      \"incident_edges\": [\n        0,\n        1,\n\
    \        2,\n        7\n      ],\n      \"references\": [\n        \"DOI:10.1016/j.tim.2007.02.005\"\
    ,\n        \"DOI:10.1038/nrmicro2549\"\n      ],\n      \"assessment\": \"All\
    \ current incident source placements accounted for. The above10 description is\
    \ broader than the complete-interval10\\u201314 convention; grouped with synonym/bin\
    \ scope.\"\n    },\n    {\n      \"index\": 1,\n      \"field_path\": \"causal_graphs[0].nodes[1]\"\
    ,\n      \"node\": {\n        \"node_id\": \"ph_range\",\n        \"label\": \"\
    pH range\",\n        \"node_type\": \"TRAIT\",\n        \"grounding\": \"METPO:1000332\"\
    ,\n        \"description\": \"Span of external pH values supporting growth.\"\n\
    \      },\n      \"incident_edges\": [\n        1\n      ],\n      \"references\"\
    : [\n        \"DOI:10.1038/nrmicro2549\"\n      ],\n      \"assessment\": \"All\
    \ current incident source placements accounted for. Generic contextual physiology\
    \ and identity only; detailed intervention/defense efficacy unassessed. No universal\
    \ mechanism or exact interval membership is inferred from a node label.\"\n  \
    \  },\n    {\n      \"index\": 2,\n      \"field_path\": \"causal_graphs[0].nodes[2]\"\
    ,\n      \"node\": {\n        \"node_id\": \"extreme_alkaliphile_antiport\",\n\
    \        \"label\": \"extreme-alkaliphile Na+/H+ antiport\",\n        \"node_type\"\
    : \"BIOLOGICAL_PROCESS\",\n        \"description\": \"Robust Na+/H+ antiporter\
    \ activity importing H+ at strongly alkaline external pH.\"\n      },\n      \"\
    incident_edges\": [\n        0,\n        5\n      ],\n      \"references\": [\n\
    \        \"DOI:10.1016/j.tim.2007.02.005\",\n        \"DOI:10.1038/nrmicro2549\"\
    \n      ],\n      \"assessment\": \"All current incident source placements accounted\
    \ for. Generic contextual physiology and identity only; detailed intervention/defense\
    \ efficacy unassessed. No universal mechanism or exact interval membership is\
    \ inferred from a node label.\"\n    },\n    {\n      \"index\": 3,\n      \"\
    field_path\": \"causal_graphs[0].nodes[3]\",\n      \"node\": {\n        \"node_id\"\
    : \"mrp_antiporter_complex\",\n        \"label\": \"Mrp Na+/H+ antiporter complex\"\
    ,\n        \"node_type\": \"GENE_OR_PROTEIN\",\n        \"grounding_status\":\
    \ \"REVIEWED_LABEL_ONLY\",\n        \"grounding_notes\": \"Reviewed as a contextual\
    \ protein or protein-complex label within a quantitative measurement graph; no\
    \ exact semantic family term was established for this aggregate use.\",\n    \
    \    \"description\": \"Hetero-oligomeric CPA3-family Na+/H+ antiporter complex\
    \ essential at high external pH.\",\n        \"gene_symbols\": [\n          \"\
    mrpA\",\n          \"mrpB\",\n          \"mrpC\",\n          \"mrpD\",\n     \
    \     \"mrpE\",\n          \"mrpF\",\n          \"mrpG\"\n        ],\n       \
    \ \"operon\": \"mrpA-G\"\n      },\n      \"incident_edges\": [\n        2,\n\
    \        3\n      ],\n      \"references\": [\n        \"DOI:10.1038/nrmicro2549\"\
    \n      ],\n      \"assessment\": \"All current incident source placements accounted\
    \ for. Generic contextual physiology and identity only; detailed intervention/defense\
    \ efficacy unassessed. No universal mechanism or exact interval membership is\
    \ inferred from a node label.\"\n    },\n    {\n      \"index\": 4,\n      \"\
    field_path\": \"causal_graphs[0].nodes[4]\",\n      \"node\": {\n        \"node_id\"\
    : \"membrane_potential\",\n        \"label\": \"transmembrane potential (delta-psi)\"\
    ,\n        \"node_type\": \"QUALITY\",\n        \"description\": \"Large transmembrane\
    \ electrical potential energizing electrogenic cation/H+ antiport.\"\n      },\n\
    \      \"incident_edges\": [\n        3\n      ],\n      \"references\": [\n \
    \       \"DOI:10.1038/nrmicro2549\"\n      ],\n      \"assessment\": \"All current\
    \ incident source placements accounted for. Generic contextual physiology and\
    \ identity only; detailed intervention/defense efficacy unassessed. No universal\
    \ mechanism or exact interval membership is inferred from a node label.\"\n  \
    \  },\n    {\n      \"index\": 5,\n      \"field_path\": \"causal_graphs[0].nodes[5]\"\
    ,\n      \"node\": {\n        \"node_id\": \"na_solute_symporters\",\n       \
    \ \"label\": \"Na+/solute symporters\",\n        \"node_type\": \"GENE_OR_PROTEIN\"\
    ,\n        \"grounding_status\": \"REVIEWED_LABEL_ONLY\",\n        \"grounding_notes\"\
    : \"Reviewed as a contextual protein or protein-complex label within a quantitative\
    \ measurement graph; no exact semantic family term was established for this aggregate\
    \ use.\",\n        \"description\": \"Symporters re-importing Na+ with solutes\
    \ to supply cytoplasmic Na+ for antiport.\"\n      },\n      \"incident_edges\"\
    : [\n        4\n      ],\n      \"references\": [\n        \"DOI:10.1038/nrmicro2549\"\
    \n      ],\n      \"assessment\": \"All current incident source placements accounted\
    \ for. Generic contextual physiology and identity only; detailed intervention/defense\
    \ efficacy unassessed. No universal mechanism or exact interval membership is\
    \ inferred from a node label.\"\n    },\n    {\n      \"index\": 6,\n      \"\
    field_path\": \"causal_graphs[0].nodes[6]\",\n      \"node\": {\n        \"node_id\"\
    : \"cytoplasmic_na\",\n        \"label\": \"cytoplasmic Na+\",\n        \"node_type\"\
    : \"CHEMICAL\",\n        \"description\": \"Intracellular sodium pool required\
    \ to sustain alkaliphile antiport activity.\"\n      },\n      \"incident_edges\"\
    : [\n        4,\n        5\n      ],\n      \"references\": [\n        \"DOI:10.1038/nrmicro2549\"\
    \n      ],\n      \"assessment\": \"All current incident source placements accounted\
    \ for. Generic contextual physiology and identity only; detailed intervention/defense\
    \ efficacy unassessed. No universal mechanism or exact interval membership is\
    \ inferred from a node label.\"\n    },\n    {\n      \"index\": 7,\n      \"\
    field_path\": \"causal_graphs[0].nodes[7]\",\n      \"node\": {\n        \"node_id\"\
    : \"f1fo_atp_synthase\",\n        \"label\": \"F1Fo-ATP synthase\",\n        \"\
    node_type\": \"GENE_OR_PROTEIN\",\n        \"grounding_status\": \"REVIEWED_LABEL_ONLY\"\
    ,\n        \"grounding_notes\": \"Reviewed as a contextual protein or protein-complex\
    \ label within a quantitative measurement graph; no exact semantic family term\
    \ was established for this aggregate use.\",\n        \"description\": \"Proton-translocating\
    \ ATP synthase whose proton uptake contributes to pH homeostasis.\"\n      },\n\
    \      \"incident_edges\": [\n        6\n      ],\n      \"references\": [\n \
    \       \"DOI:10.1038/nrmicro2549\"\n      ],\n      \"assessment\": \"All current\
    \ incident source placements accounted for. Generic contextual physiology and\
    \ identity only; detailed intervention/defense efficacy unassessed. No universal\
    \ mechanism or exact interval membership is inferred from a node label.\"\n  \
    \  },\n    {\n      \"index\": 8,\n      \"field_path\": \"causal_graphs[0].nodes[8]\"\
    ,\n      \"node\": {\n        \"node_id\": \"alkaline_ph_homeostasis\",\n    \
    \    \"label\": \"alkaline pH homeostasis\",\n        \"node_type\": \"BIOLOGICAL_PROCESS\"\
    ,\n        \"description\": \"Maintenance of a near-neutral cytoplasmic pH against\
    \ a strongly alkaline exterior.\"\n      },\n      \"incident_edges\": [\n   \
    \     6,\n        7\n      ],\n      \"references\": [\n        \"DOI:10.1038/nrmicro2549\"\
    \n      ],\n      \"assessment\": \"All current incident source placements accounted\
    \ for. Generic contextual physiology and identity only; detailed intervention/defense\
    \ efficacy unassessed. No universal mechanism or exact interval membership is\
    \ inferred from a node label.\"\n    },\n    {\n      \"index\": 9,\n      \"\
    field_path\": \"causal_graphs[0].nodes[9]\",\n      \"node\": {\n        \"node_id\"\
    : \"external_ph_high\",\n        \"label\": \"external pH > 10.3\",\n        \"\
    node_type\": \"ENVIRONMENTAL_FACTOR\",\n        \"description\": \"Strongly alkaline\
    \ external pH above ~10.3.\"\n      },\n      \"incident_edges\": [\n        8\n\
    \      ],\n      \"references\": [\n        \"DOI:10.1128/AEM.01557-23\"\n   \
    \   ],\n      \"assessment\": \"All current incident source placements accounted\
    \ for. Generic contextual physiology and identity only; detailed intervention/defense\
    \ efficacy unassessed. No universal mechanism or exact interval membership is\
    \ inferred from a node label.\"\n    },\n    {\n      \"index\": 10,\n      \"\
    field_path\": \"causal_graphs[0].nodes[10]\",\n      \"node\": {\n        \"node_id\"\
    : \"carbonate_speciation\",\n        \"label\": \"carbonate (CO3 2-) speciation\"\
    ,\n        \"node_type\": \"CHEMICAL\",\n        \"description\": \"Shift of dissolved\
    \ inorganic carbon toward carbonate at high pH.\"\n      },\n      \"incident_edges\"\
    : [\n        8\n      ],\n      \"references\": [\n        \"DOI:10.1128/AEM.01557-23\"\
    \n      ],\n      \"assessment\": \"All current incident source placements accounted\
    \ for. Actual inorganic-carbon shift is source-supported; material carbonate versus\
    \ a shift/process referent is a separate grounding precision question.\"\n   \
    \ }\n  ]\n}"
- assessment_id: expression
  area: evidence
  topic: 'Native checklist: organism applicability'
  outcome: unknown
  target_ids:
  - METPO:1000464
  summary: No canonical organism is supplied, so no organism is substituted to obtain
    an expression result. Retained catalog and runner provenance do not establish
    phenotype or pathway efficacy, and no detailed defense gene/module query is made.
  evidence_ids:
  - expression
  - authority-reuse
  - canonical-gap
  details: "{\n  \"completed_at\": \"2026-10-21T19:51:03.939860+00:00\",\n  \"status\"\
    : \"NOT_APPLICABLE_TO_CURRENT_CANONICAL_MATCHING\",\n  \"canonical_examples\"\
    : 0,\n  \"catalog_organisms\": 20,\n  \"catalog_datasets\": 28,\n  \"catalog\"\
    : {\n    \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-grounding-agent/reused-datasets.json\"\
    ,\n    \"sha256\": \"155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693\"\
    ,\n    \"bytes\": 2871\n  },\n  \"original_access_receipts\": {\n    \"path\"\
    : \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-grounding-agent/reused-catalog-accesses.json\"\
    ,\n    \"sha256\": \"8417116b63b7d42e7f4c6cba92ef0420fbc87b24ac4629c4c77286caf6293f4a\"\
    ,\n    \"bytes\": 828\n  },\n  \"assessment\": \"The retained catalog is available,\
    \ but this record supplies no canonical organism or strain for exact matching.\
    \ Model organisms mentioned in literature or the generated report are not substituted\
    \ as canonical examples. This is not a claim that the catalog lacks every relevant\
    \ organism.\",\n  \"downstream_gene_or_module_queries\": \"NOT_RUN\",\n  \"protein_instances\"\
    : 0,\n  \"uniprot_instance_audit\": \"NOT_APPLICABLE\",\n  \"scope\": \"No detailed\
    \ defense, stress-response or fitness queries.\"\n}"
- assessment_id: ownership
  area: provenance
  topic: 'Native checklist: current fields and maintained writers'
  outcome: supported
  target_ids:
  - METPO:1000464
  summary: The seeder directly preserves upstream exact/related synonym types. The
    canonical-gap writer documents the retained complete-interval convention and is
    not a required synonym repair. Edge 5 mapping/shared-grounder context preserves
    nonempty IDs; its historical migration matches the old sodium-to-Mrp key and does
    not automatically replay the current sodium-to-antiport assertion. Only the record
    is established as the current node 10 owner.
  evidence_ids:
  - owners
  - local-authority
  - ground-reading
  details: "{\n  \"completed_at\": \"2026-10-21T19:51:03.939860+00:00\",\n  \"target\"\
    : \"data/traits/environment/ph_range_high.yaml\",\n  \"owners\": [\n    {\n  \
    \    \"path\": \"scripts/seed_from_metpo.py\",\n      \"locators\": [\n      \
    \  \"198\\u2013209\",\n        \"333\\u2013348\"\n      ],\n      \"role\": \"\
    Direct import owner for exact and related synonym types. It preserves the upstream\
    \ synonym kind when serializing; scientific equivalence and import fidelity are\
    \ separate.\",\n      \"sha256\": \"0fb9c9f7ea6a8f137eecd5c319775b511c398dba6158c81b1fbfb94210f7d851\"\
    \n    },\n    {\n      \"path\": \"scripts/migrate_enables_range_edges.py\",\n\
    \      \"locators\": [\n        \"53\\u201359\",\n        \"204\\u2013239\"\n\
    \      ],\n      \"role\": \"Direct historical edge owner: the decision matches\
    \ the OLD cytoplasmic_na -> mrp_antiporter_complex key and repoints the object\
    \ to the antiport process while retaining enables. The replay requires that old\
    \ key and RO:0002327, and returns failure when absent. It is not an automatic\
    \ repair of the already-repointed current assertion.\",\n      \"sha256\": \"\
    3d0d1bddcaa76baef5833973e2e979e4fee1f834c67d1abcc69a8d866ecb8f32\"\n    },\n \
    \   {\n      \"path\": \"scripts/ground_causal_predicates.py\",\n      \"locators\"\
    : [\n        \"136\\u2013180\"\n      ],\n      \"role\": \"Maintained mapping\
    \ consumer; existing nonempty predicate_id is skipped. A table change alone will\
    \ not rewrite the current populated edge.\",\n      \"sha256\": \"5a788eeaabf3a56b0d82c469a3e3fe28f1d51707d9382313b9a94289be7d1381\"\
    \n    },\n    {\n      \"path\": \"mappings/predicate_grounding.tsv\",\n     \
    \ \"locators\": [\n        \"8\",\n        \"9\",\n        \"10\",\n        \"\
    102\"\n      ],\n      \"role\": \"Current subclass, enables, contributes-to and\
    \ confers mapping context. Wildcard mapping rows do not remove imported relation\
    \ semantics.\",\n      \"sha256\": \"8e28c19e93aca3dc164a3befbe2612b289241de457c59f499e65936c03b7ce52\"\
    \n    },\n    {\n      \"path\": \"scripts/backfill_canonical_examples_444.py\"\
    ,\n      \"locators\": [\n        \"819\\u2013823\",\n        \"995\\u20131074\"\
    \n      ],\n      \"role\": \"Exact current canonical-gap owner. Preserves the\
    \ documented complete-interval gap under guarded queue/application logic; does\
    \ not invent an example.\",\n      \"sha256\": \"18ca0766789c239d693ef665e8b1d43c1209a0f414a326f1c5d890f88de7b20c\"\
    \n    },\n    {\n      \"path\": \"data/traits/environment/ph_range_high.yaml\"\
    ,\n      \"locators\": [\n        \"causal_graphs[0].nodes[10]\"\n      ],\n \
    \     \"role\": \"Only established current recurrence owner for carbonate material/speciation\
    \ wording. Broad migration or sibling-node hits are context, not proven owners\
    \ of this exact field.\",\n      \"sha256\": \"3bf384769f08dd98073a67742a098348aca91cfbea63ea35bcee2e9a1a1c1fec\"\
    \n    }\n  ],\n  \"search\": {\n    \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-grounding-agent/search-and-provenance.json\"\
    ,\n    \"matching_paths\": 172,\n    \"structured_review_target_arrays\": 67,\n\
    \    \"exact_target_arrays\": 0,\n    \"ignored_and_hidden_included\": true,\n\
    \    \"exclusions\": [\n      \".git/**\",\n      \".venv/**\"\n    ],\n    \"\
    scope\": \"Entire owned repository including ignored/hidden files, excluding Git\
    \ internals and virtual environment. Exact target identity/slug/label and numerical\
    \ synonym; broad physiological aliases are not treated as exact target signoff.\"\
    \n  },\n  \"all_node_search\": {\n    \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-high-grounding-agent/all-node-owner-search.json\"\
    ,\n    \"node_ids\": 11,\n    \"history_leads\": 5,\n    \"uncaptured_history_leads\"\
    : 0\n  },\n  \"history_scope\": {\n    \"captured_histories\": 5,\n    \"whole_files_read\"\
    : [\n      \"history/infrastructure/inconsistent-node-type/2026-08-12T000912Z-claude-code-779670.yaml\"\
    ,\n      \"history/infrastructure/process-quality-consistency/2026-08-21T073211Z-codex-174227.yaml\"\
    ,\n      \"history/other/canonical-examples-batch1/2026-08-20T074839Z-claude-code-6fb2f5.yaml\"\
    ,\n      \"history/other/canonical-examples-six/2026-08-21T065406Z-codex-a1ab82.yaml\"\
    ,\n      \"history/records/ph_range_mid2/2026-09-04T024000Z-codex-3036b8.yaml\"\
    \n    ],\n    \"actors\": \"All five captured histories have AI actors; they are\
    \ infrastructure, canonical-batch or sibling-record contexts, not exact current-target\
    \ human acceptance.\"\n  },\n  \"record_events\": {\n    \"total\": 10,\n    \"\
    ai\": 9,\n    \"seed\": 1,\n    \"assessment\": \"AI-labelled curation and a non-LLM\
    \ seed event are positive provenance. They do not constitute a linked human signoff\
    \ for the current reviewed state.\"\n  },\n  \"human_traceability\": \"Within\
    \ this bounded ignored-inclusive current-target search and actual review-array\
    \ parsing, no exact current-target human acceptance was established. This is a\
    \ traceability minor, not a universal claim that no human ever reviewed the record.\"\
    ,\n  \"report\": {\n    \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/repo/research/traits/environment/ph_range_high-deep-research-falcon.md\"\
    ,\n    \"sha256\": \"3c959ba05254e48acb9a6e33a2d83b36ff95f40412e011f0cee54e884a32a300\"\
    ,\n    \"bytes\": 48756,\n    \"scope\": \"Entire 426-line current report read\
    \ as a generated lead and provenance artifact only. Its August 4 capture is not\
    \ proof of the exact version used by the June 23 enrichment event; no biological\
    \ recommendation or repair is adopted from it.\"\n  },\n  \"context_only\": [\n\
    \    \"Generic type-consistency and process/quality migrations do not by themselves\
    \ prove ownership of current node 10.\",\n    \"The ph_range_mid2 writer and captured\
    \ sibling history remain comparator context.\",\n    \"The historical encodes\
    \ migration concerns an edge removed from the current graph.\"\n  ],\n  \"no_mutations\"\
    : true\n}"
- assessment_id: human-acceptance
  area: provenance
  topic: 'Native checklist: bounded acceptance traceability'
  outcome: concern
  target_ids:
  - METPO:1000464
  summary: The current record has nine explicitly AI-assisted events plus an automated
    seed. The grounding auditor read five whole AI context histories; root read their
    complete actor/target/event projections. The ignored-inclusive search found 172
    paths and 67 actual review target arrays, with zero exact target arrays. These
    are bounded local observations; passing checks, REVIEWED and parent authorship
    do not link acceptance of current assertions.
  evidence_ids:
  - owners
  - playbook
  - identity
  - challenge
  - adjudication
- assessment_id: readiness
  area: consistency
  topic: 'Native checklist: actual checks and acquisition chronology'
  outcome: supported
  target_ids:
  - METPO:1000464
  summary: All 78 captured inputs and frozen artifacts match. Focused native, strict
    and snippet checks passed directly. AEM source metadata DNS failure and successful
    retry are separately retained; historical common failures/skips/retries remain
    explicit under B10-to-B11 reuse without a new B11 QC claim.
  evidence_ids:
  - capture
  - reuse
  - reuse-postcheck
  - native-checks
  - aem-first-access
  - aem-retry-access
  - check-ph-range-high-native
  - check-ph-range-high-strict
  - check-ph-range-high-snippets
findings:
- finding_id: category-versus-complete-interval
  issue_key: ph-range-high-category-versus-complete-interval
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Broad alkaliphile categories and above-10 growth are equated with a contained
    numerical range
  description: The current exact category synonyms and above-10 description are broader
    than a complete growth interval contained in 10–14. Published classification distinguishes
    alkali-tolerant and facultative alkaliphilic growth, while assigned Krulwich text
    names extreme alkaliphiles with growth below 10. Preserve the numerical bin and
    generic alkaline physiology; reconcile this one shared scope distinction without
    rejecting the class or forcing a canonical.
  target_ids:
  - METPO:1000464
  field_paths:
  - synonyms[0]
  - synonyms[1]
  - synonyms[2]
  - causal_graphs[0].nodes[0].description
  - causal_graphs[0].description
  evidence_ids:
  - bin-scope
  - classification-body
  - body-krulwich
  - metpo-primary
  - canonical-gap
  - owners
  - challenge
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_range_high.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: scripts/seed_from_metpo.py
    role: Direct import owner preserving upstream exact/related synonym types; scientific
      equivalence is separate from import fidelity.
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: baker-attribution
  issue_key: ph-range-high-baker-attribution
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Assigned acidophile source is used for a stronger alkaline attribution
  description: The inspected Baker abstract supplies acidophile context, while the
    current notes attribute extreme-alkaliphile antiport and PMF support to that source.
    Qualify the attribution to actual inspected support or substantiate the broader
    claim. Its unavailable full body does not prove absence of alkaline discussion
    or false biology.
  target_ids:
  - METPO:1000464
  field_paths:
  - evidence[1].notes
  - causal_graphs[0].edges[0].evidence[0].notes
  evidence_ids:
  - meta-baker
  - sources
  - placements
  - source-access
  - challenge
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_range_high.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: substrate-executor-precision
  issue_key: ph-range-high-substrate-executor-precision
  category: consistency
  severity: minor
  status: open
  certainty: confirmed
  title: Sodium substrate availability is expressed with an executor relation
  description: The current sodium pool is material and the antiport node processual,
    so imported endpoint compatibility is positive. RO enables describes an executor
    relation, while the edge explicitly describes a substrate sustaining activity.
    This is bounded semantic precision, not a categorical endpoint or biological-efficacy
    failure.
  target_ids:
  - METPO:1000464
  field_paths:
  - causal_graphs[0].edges[5]
  evidence_ids:
  - node-edges
  - ro-primary
  - owners
  - challenge
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_range_high.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: scripts/migrate_enables_range_edges.py
    role: Historical endpoint migration matches the old sodium-to-Mrp key; it does
      not automatically replay the current sodium-to-antiport assertion.
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Current enables mapping context; inspect role semantics rather than assuming
      the mapping repairs populated edges.
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Maintained mapping consumer skips existing nonempty predicate IDs; table
      changes alone do not rewrite the current edge.
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: carbonate-referent-precision
  issue_key: ph-range-high-carbonate-referent-precision
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Carbonate entity and speciation shift share one node referent
  description: Node 10 uses a material carbonate label/type while its description
    denotes a pH-dependent shift of inorganic-carbon speciation. The existing chemistry
    is directly source-supported. Clarify the intended entity-versus-change referent
    without claiming the carbonate statement is false or prescribing a new mechanism.
  target_ids:
  - METPO:1000464
  field_paths:
  - causal_graphs[0].nodes[10]
  evidence_ids:
  - node-edges
  - schema
  - body-aem
  - challenge
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_range_high.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: human-acceptance-link
  issue_key: ph-range-high-human-acceptance-link
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Current local provenance lacks an attributable acceptance link
  description: AI and seed maintenance, REVIEWED and passing checks do not independently
    identify acceptance of the current graph. The captured ignored-inclusive search
    and actual target/history parsing bound this result; no private or remote absence
    is asserted.
  target_ids:
  - METPO:1000464
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
    path: data/traits/environment/ph_range_high.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
actions:
- action_id: separate-category-and-bin
  description: Reconcile exact category synonyms and above-10 shorthand with the intended
    complete-interval bin during separately authorized curation.
  finding_ids:
  - category-versus-complete-interval
  target_ids:
  - METPO:1000464
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_range_high.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: scripts/seed_from_metpo.py
    role: Direct import owner preserving upstream exact/related synonym types; scientific
      equivalence is separate from import fidelity.
  acceptance_checks:
  - Preserve faithful upstream-import provenance separately from scientific equivalence,
    and retain the valid numerical bin.
  - Do not duplicate the same scope issue across definition, synonyms and contextual
    edges. Do not require a token canonical or invent a whole interval from an upper-growth
    observation.
  - Use guarded history, appropriate native/strict/source/QC checks and a successor
    review after changed inputs; no mechanistic intervention or experiment is requested.
- action_id: qualify-baker-attribution
  description: Qualify or substantiate the assigned Baker attribution using an actually
    inspected relevant passage.
  finding_ids:
  - baker-attribution
  target_ids:
  - METPO:1000464
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_range_high.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Preserve unknown body-snippet status and separate positive Krulwich context.
  - Do not infer whole-paper absence, false biology or detailed efficacy from unavailable
    text.
- action_id: clarify-executor-substrate
  description: Clarify the intended sodium substrate relation while preserving the
    current compatible endpoint referents.
  finding_ids:
  - substrate-executor-precision
  target_ids:
  - METPO:1000464
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_range_high.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: scripts/migrate_enables_range_edges.py
    role: Historical endpoint migration matches the old sodium-to-Mrp key; it does
      not automatically replay the current sodium-to-antiport assertion.
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Current enables mapping context; inspect role semantics rather than assuming
      the mapping repairs populated edges.
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Maintained mapping consumer skips existing nonempty predicate IDs; table
      changes alone do not rewrite the current edge.
  acceptance_checks:
  - Distinguish executor semantics from substrate availability without changing biology
    by inference.
  - Preserve the historical migration’s old-key limit and shared grounder’s nonempty-ID
    guard; neither automatically repairs the current assertion. No forced protein
    replacement.
- action_id: clarify-carbonate-referent
  description: Clarify whether node 10 denotes carbonate material or the described
    speciation change.
  finding_ids:
  - carbonate-referent-precision
  target_ids:
  - METPO:1000464
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_range_high.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Preserve the source-backed inorganic-carbon chemistry and approximate threshold.
  - Do not add a new pathway, experimental recipe or unsupported causal step.
- action_id: link-human-acceptance
  description: Link attributable current acceptance if available or clarify status
    while preserving the bounded provenance result.
  finding_ids:
  - human-acceptance-link
  target_ids:
  - METPO:1000464
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_range_high.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Retain actual AI/seed provenance and ignored-inclusive search scope.
  - No contact with others or automatic status promotion is authorized.
limitations:
- Detailed pathogen defense, fitness, AMR, mutation/perturbation efficacy and intervention
  optimization remain UNASSESSED_SCOPE. No biological route or experimental repair
  is supplied.
- Baker full body and both current PMF phrases remain unknown. The source-attribution
  concern is bounded to inspected support, not whole-paper absence or false biology.
- Inherited ontology text may be faithfully imported while exact scientific category
  equivalence remains too broad. Do not infer a complete interval from growing above
  10, or infer an empty bin from the absent canonical.
- Both current RO edges satisfy material/process endpoint categories. Executor/substrate
  precision is a semantic distinction, not a formal endpoint failure; ATP-synthase
  contribution remains compatible.
- Current local confers has broad documented endpoints. Generic contextual support
  is not automatically universal necessity or exact numerical-bin calibration.
- AEM paragraph 22 supports carbonate predominance above approximately 10.3; genome-toolkit
  methods and engineering implications are not adopted.
- Krulwich selected first-sentence environmental context retains its organism scope;
  later motif/mutation passages are unassessed. The supplemental classification article
  is not assigned evidence or a replacement canonical.
- Original source acquisitions, current copies and selected readings remain distinct.
  AEM metadata DNS failure and successful retry are not native/serializer failures.
- No supplied canonical means no organism/catalog substitution. Optional proteins,
  accessions, connectors and pathways are not added by quota.
- Target creator attribution is not copied from the pH-range parent. Bounded local
  acceptance search cannot establish absence of private or remote decisions.
- Exact large-potential necessity wording at edge 3 is not established by the selected
  primary windows; a bounded retained-sentence nonmatch is not full-paper absence
  or false physiology.
- The complete-interval convention is documented by the current record and guarded
  canonical-gap writer; the numeric existential OWL restriction alone is not a universal
  whole-interval containment axiom.
- Root selected primary reading covered the three assigned abstracts, Krulwich classification
  paragraph 39253, supplemental body paragraph 0 and AEM paragraph 22. Additional
  generic physiology first-sentence readings belong to the source auditor and independent
  challenger, not a root whole-article claim.
notes:
- Final root disposition is 1 major and 4 minor findings, with all source, grounding,
  challenge and root bindings verified. This preparation has not imported or executed
  the serializer. Root owns one serialization, native validation, final artifact review
  and save.
- 'Source coverage: 3 assigned works plus 1 explicit classification supplement; 12
  external placements; 11 nodes/9 edges; 4 snippets (2 literal and 2 unknown); no
  canonical.'
- Preparation changes no scientific record, Git state, sweep state or native inventory.
tags:
- record-review
- ph-range-high
- environment
- needs-curation
native_verdict: needs_curation
```
