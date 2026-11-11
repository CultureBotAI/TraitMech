# Whole-record review of low pH range

- Review: 20261021T200401Z-ph-range-low
- Repository: CultureBotAI/TraitMech
- Started UTC: 2026-10-21T19:53:31.919704Z
- Finished UTC: 2026-10-21T20:04:01Z
- Reviewer: codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Final root adjudication: two major findings for exact category/bin equivalence and RO2212 endpoint semantics; two bounded minors for quote omission and human traceability. Generic context and canonical species identity remain positive; exact canonical range support remains unknown.

## Scope And Provenance

One entire maintained TraitRecord. Contextual ontology, source, parent, writer and history inputs are not additional review targets.

Selection: Fifth record of the actual batch 011 queue. Whole target read before the original successful 82-input capture; source judgments followed hash verification. A newly discovered exact historical writer was added by a separate successful 83-input capture before its substantive reading. Original 82 bytes and receipts are retained unchanged; the final review uses 83 inputs.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 8eee04a8c65609fbaff6df7c54597dcaf1b9d282.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| METPO:1000460 | data/traits/environment/ph_range_low.yaml | maintained | pH range low |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full-corpus graph audit | passed | True | METPO:1000460 | 74 baselined findings, zero new/blocking findings; connectivity report covers 130 mechanistic graphs. This is a corpus diagnostic, not focused scientific verification of this target. |
| Full-corpus snippet audit | passed | True | METPO:1000460 | 2419 baselined findings, zero new/blocking findings. Focused source checks and manual evidence review are recorded separately. |
| Full-corpus pathway links | passed | True | METPO:1000460 | 19 links checked against the pinned PathwayMech snapshot. |
| Full-corpus history integrity | passed | True | METPO:1000460 | 1277 history records checked, zero invalid links at the 8eee source base; integrity does not establish science or human acceptance. |
| Initial full-product validation | failed | False | METPO:1000460 | Exit 2 during PATO/RO downloads; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation with isolated local cache | failed | False | METPO:1000460 | Exit 2; 36 adapter errors and 123 no-adapter skips. Superseded by successful network retry. |
| Product validation after isolated-cache download | passed | True | METPO:1000460 | Passed: 361 canonical matches, two synonym matches, one exception, 123 SKIPPED_NO_ADAPTER pairs. Not every target identifier is covered. |
| Focused native validation | passed | True | METPO:1000460 | Successful focused schema validation; formal scientific roles remain separately assessed. |
| Focused strict validation | passed | True | METPO:1000460 | Successful focused strict validation; no detailed biological efficacy certification. |
| Focused snippet verification | passed | True | METPO:1000460 | Three schema snippet fields: two VERIFIED and one NOT_IN_ABSTRACT. Six quoted note fields are separately assessed: three literal, two marked abridgments, one unmarked omission with positive meaning. Native results are preserved. |
| Reused maintained batch-ten QC | passed | True | METPO:1000460 | Actual B10 final QC at its original time, qualified against B11 bytes; not a fresh B11 execution. |
| Protein-instance metadata applicability | not_applicable | False | METPO:1000460 | One reviewed label-only contextual protein class and zero instances; no token accession required. |

## Scientific And Domain Assessments

### Native checklist: active identity and scientific exactness

identity: concern. Targets: METPO:1000460.

Active METPO identity, direct parent, obsolete replacement, numerical 4–6 bounds and related alias are supported. The four faithfully imported broad acidophile/tolerance aliases do not establish exact equivalence to this complete interval. Preserve source-specific cutoffs rather than inventing exhaustive facultative/obligate definitions.

### Native checklist: quantitative range and contextual sources

evidence: unknown. Targets: METPO:1000460.

Generic homeostasis and acidic-growth sources provide context, but do not independently calibrate an exact complete 4–6 interval. Published optimum categories and whole growth ranges differ. Retain the numerical bin and do not multiply this limitation into additional source or mechanism findings.

### Native checklist: environmental numerical phenotype

scope: supported. Targets: METPO:1000460.

ENVIRONMENT, CLASS and NONMECHANISTIC are coherent for this quantitative trait. Generic environmental physiology does not certify a universal mechanism, exact interval sufficiency or detailed defense efficacy.

### Native checklist: species identity versus assigned phenotype support

evidence: unknown. Targets: METPO:1000460.

Official NCBI 920 species identity is positive, but the assigned DOI resolves to a LAB review and its inspected abstract does not establish Acidithiobacillus ferrooxidans or a complete 4–6 growth interval. Publisher full body remains unavailable. Follow up by documenting an actually inspected species/strain interval source or qualifying the canonical claim in separately authorized curation; no forced finding, replacement organism or false-range claim follows from access failure.

{
  "completed_at": "2026-10-21T19:58:41.406748+00:00",
  "example": {
    "taxon_id": "NCBITaxon:920",
    "taxon_label": "Acidithiobacillus ferrooxidans",
    "reference": "DOI:10.3390/fermentation10060298",
    "note": "Acidophile growing in the low-pH range this record bounds, cited in its artifact for acidophile physiology."
  },
  "candidate": {
    "key": "canonical-source-placement-gap",
    "severity": "undetermined",
    "field_paths": [
      "canonical_examples[0]"
    ],
    "assessment": "Species identity is supported by official NCBI response. The assigned DOI resolves to a LAB food-products review whose inspected abstract does not establish A. ferrooxidans or its complete4\u20136 growth interval. Publisher body access remains unavailable; this is an explicit source/placement verification gap pending final root judgment.",
    "qualification": "Do not infer paper-wide organism absence from title/abstract, a false physiological range from access failure, or substitute an unassigned organism/source. Europe PMC zero hit is resolved bibliographically by Crossref, not treated as nonexistent DOI."
  },
  "crossref": {
    "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/canonical-crossref.json",
    "sha256": "8a989cead3090bece254aa0c5d41951d78e8f5f94998544671cefe11fe29476c",
    "bytes": 37483
  },
  "europepmc_zero_hit": {
    "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/canonical-metadata.json",
    "sha256": "79bba614dec9fe2829936edc0bb6f9738a9766190872b44d6310a4e0e533275a",
    "bytes": 195
  },
  "primary_taxonomy": {
    "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-grounding-agent/taxa46632-920.xml",
    "sha256": "1be9370b5b6116c77b07fe85c0d6979c812db23c2d00ff03d9369431d0ae844b",
    "scope": "Species identity only; actual acquisition/reuse receipt owned by grounding auditor."
  },
  "body_limit": "MDPI browser429, PDF inaccessible and directPDF403 retained. Search-generated publisher text is a lead/selected scope observation, not retained full body or a complete absence proof."
}

### Native checklist: all seven works and eleven placements

evidence: supported. Targets: METPO:1000460.

Every assigned DOI is resolved: six indexed hits and a canonical zero hit resolved through Crossref. Actual source types and scopes are preserved. CFA is documentary-only; yeast study identity and its existing generic background are distinct from excluded perturbation results.

{
  "completed_at": "2026-10-21T19:58:41.401477+00:00",
  "external_placements": [
    {
      "field_path": "definition_source",
      "reference": "DOI:10.1038/nrmicro2549",
      "claim": "A pH range phenotype in which the growth-supporting external pH range spans approximately 4\u20136, characteristic of acidophilic physiology.",
      "assessment": "Current review supports acidic-growth/homeostasis context, not exact equivalence between all acidophile categories and a complete4\u20136 interval."
    },
    {
      "field_path": "evidence[0]",
      "reference": "DOI:10.1038/nrmicro2549",
      "snippet": "cytoplasmic pH",
      "notes": "pH-homeostasis review supports moderately acidic pH-homeostasis as the basis of growth in the pH 4\u20136 range.",
      "assessment": "Literal cytoplasmic-pH occurrence positive; generic homeostasis is distinct from exact complete-bin calibration."
    },
    {
      "field_path": "causal_graphs[0].edges[0].evidence[0]",
      "reference": "DOI:10.1038/nrmicro2549",
      "snippet": "cytoplasmic pH",
      "notes": "Supports acidophile cytoplasmic pH homeostasis as the moderately-acidic growth-range mechanism.",
      "assessment": "Actual generic homeostasis context is positive, but acidophile categories and physiological mechanisms do not establish an exact complete4\u20136 interval. Group scope with category/bin assessment; no biological falsity or universal mechanism is inferred."
    },
    {
      "field_path": "causal_graphs[0].edges[1].evidence[0]",
      "reference": "DOI:10.1016/j.tim.2007.02.005",
      "snippet": "proton motive force",
      "notes": "Supports the pH 4\u20136 range as a value within the pH-range distribution.",
      "assessment": "Ontology supplies the parent/bin hierarchy. Baker abstract classifies acidophiles by optimum below3 and supports generic homeostasis; it does not directly calibrate a complete4\u20136 interval. Assigned PMF body phrase remains unknown; lack of abstract occurrence is not a false quotation."
    },
    {
      "field_path": "causal_graphs[0].edges[2].evidence[0]",
      "reference": "DOI:10.1111/1758-2229.70019",
      "notes": "\"That proton potential then drives the phosphorylation of ADP and the formation of ATP by the ATP synthase\"; general bioenergetic edge relevant to low-pH growth.",
      "assessment": "Existing generic PMF-to-ATP statement is supported at bioenergetics body21. The quoted note removes an intervening parenthesis without an ellipsis; meaning remains positive and no efficacy/intervention inference is made."
    },
    {
      "field_path": "causal_graphs[0].edges[3].evidence[0]",
      "reference": "DOI:10.4014/jmb.2303.03009",
      "notes": "\"decreasing membrane proton permeability prevents the accumulation of intracellular protons\" after conversion to cyclopropane fatty acids; generalizable membrane adaptation.",
      "assessment": "Current quoted fragment is literally present in CFA body6. Source title/abstract identify pathogenic Gram-negative acid-defense scope. Only identity, quote occurrence and separately audited formal roles are assessed; generalizable biological efficacy is UNASSESSED_SCOPE."
    },
    {
      "field_path": "causal_graphs[0].edges[4].evidence[0]",
      "reference": "DOI:10.1111/1758-2229.70019",
      "notes": "\"organic acids... occur in their undissociated form and can diffuse into the cell\"; boundary condition distinguishing low-pH growth from weak-acid inhibition.",
      "assessment": "Actual environmental review body25 supports the existing generic weak-acid permeability context. Quoted note is a marked noncontiguous abridgment with literal ordered fragments. It does not itself establish complete4\u20136 growth or a universal lineage response."
    },
    {
      "field_path": "causal_graphs[0].edges[5].evidence[0]",
      "reference": "DOI:10.1111/1758-2229.70019",
      "notes": "\"the higher pH of the cytoplasm will lead to dissociation of the acid, thus releasing protons and lowering the internal pH\"; strong causal edge.",
      "assessment": "Actual environmental review body25 contains the current quoted dissociation/pH sentence as a contiguous phrase. Generic acid-base chemistry is positive; no new intervention conditions or acid-defense efficacy assessment."
    },
    {
      "field_path": "causal_graphs[0].edges[6].evidence[0]",
      "reference": "DOI:10.3389/fmicb.2023.1149903",
      "notes": "Acidophile genomes encode \"a P-type ATPase proton efflux pump\"; active ATP-driven proton export underlies cytoplasmic pH homeostasis.",
      "assessment": "Actual environmental review body36 contains the quoted P-type-pump phrase in the named At. ferrivorans SS3 genome context, with absence in another reported MAG. Existing contextual presence is positive; genomic annotation is not direct functional validation or universal necessity."
    },
    {
      "field_path": "causal_graphs[0].edges[7].evidence[0]",
      "reference": "DOI:10.3390/microorganisms12030625",
      "notes": "\"acid stress tolerance... facilitated by an active export of protons via the expenditure of ATP... carried out by H+-ATPases\"; broad principle of homeostasis.",
      "assessment": "Actual yeast article body2 gives the generic existing proton-export background sentence. Note is marked abridgment; source context is S. cerevisiae and background citations, not the new engineered-pump result. No perturbation efficacy, optimization or exact4\u20136 calibration is adopted."
    },
    {
      "field_path": "canonical_examples[0]",
      "reference": "DOI:10.3390/fermentation10060298",
      "claim": {
        "taxon_id": "NCBITaxon:920",
        "taxon_label": "Acidithiobacillus ferrooxidans",
        "reference": "DOI:10.3390/fermentation10060298",
        "note": "Acidophile growing in the low-pH range this record bounds, cited in its artifact for acidophile physiology."
      },
      "assessment": "Official species identity positive; assigned DOI resolves to a LAB review. Inspected abstract and bounded publisher access do not establish this species complete4\u20136 interval. Preserve unresolved source/placement gap without declaring entire-paper absence or false species biology."
    }
  ],
  "ontology_grounding_fields": [
    {
      "field_path": "causal_graphs[0].nodes[0].grounding",
      "reference": "METPO:1000460"
    },
    {
      "field_path": "causal_graphs[0].nodes[1].grounding",
      "reference": "METPO:1000332"
    },
    {
      "field_path": "causal_graphs[0].nodes[3].grounding",
      "reference": "METPO:1007500"
    }
  ],
  "synonym_source_fields": [
    {
      "field_path": "synonyms[0]",
      "synonym": {
        "synonym_text": "Acid Tolerant",
        "synonym_type": "EXACT_SYNONYM",
        "source": "metpo.owl"
      }
    },
    {
      "field_path": "synonyms[1]",
      "synonym": {
        "synonym_text": "Acidophile",
        "synonym_type": "EXACT_SYNONYM",
        "source": "metpo.owl"
      }
    },
    {
      "field_path": "synonyms[2]",
      "synonym": {
        "synonym_text": "Facultative acidophile",
        "synonym_type": "EXACT_SYNONYM",
        "source": "metpo.owl"
      }
    },
    {
      "field_path": "synonyms[3]",
      "synonym": {
        "synonym_text": "Obligative acidophile",
        "synonym_type": "EXACT_SYNONYM",
        "source": "metpo.owl"
      }
    },
    {
      "field_path": "synonyms[4]",
      "synonym": {
        "synonym_text": "pHR_4_to_6",
        "synonym_type": "RELATED_SYNONYM",
        "source": "metpo.owl"
      }
    }
  ],
  "scope": "All seven assigned works across eleven external placements, including canonical and definition. Three structured ontology fields are distinct from five synonym provenance fields."
}

### Native checklist: three snippets and six quoted notes

evidence: concern. Targets: METPO:1000460.

Two schema snippets are literal and the Baker PMF snippet remains body-unknown. Separately, three quoted-note fields are literal, two are explicitly marked abridgments, and edge 2 removes a parenthetical without an ellipsis while preserving supported meaning. Do not combine the note denominator with native three-snippet results.

{
  "snippets": {
    "completed_at": "2026-10-21T19:58:41.405228+00:00",
    "snippets": [
      {
        "field_path": "evidence[0].snippet",
        "reference": "DOI:10.1038/nrmicro2549",
        "snippet": "cytoplasmic pH",
        "outcome": "literal_exact",
        "hits": [
          {
            "surface": "indexed abstract",
            "file": {
              "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-metadata.json",
              "sha256": "036607538c4110a45aeab78f8cad03b240ab3648075984f6f3e870b03692e3fd",
              "bytes": 4996
            },
            "locator": "abstractText"
          },
          {
            "surface": "retained BioC",
            "file": {
              "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml",
              "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
              "bytes": 174908
            },
            "locator": "passage offset 58"
          },
          {
            "surface": "retained BioC",
            "file": {
              "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml",
              "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
              "bytes": 174908
            },
            "locator": "passage offset 671"
          },
          {
            "surface": "retained BioC",
            "file": {
              "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml",
              "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
              "bytes": 174908
            },
            "locator": "passage offset 2440"
          },
          {
            "surface": "retained BioC",
            "file": {
              "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml",
              "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
              "bytes": 174908
            },
            "locator": "passage offset 3940"
          },
          {
            "surface": "retained BioC",
            "file": {
              "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml",
              "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
              "bytes": 174908
            },
            "locator": "passage offset 4950"
          },
          {
            "surface": "retained BioC",
            "file": {
              "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml",
              "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
              "bytes": 174908
            },
            "locator": "passage offset 7133"
          },
          {
            "surface": "retained BioC",
            "file": {
              "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml",
              "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
              "bytes": 174908
            },
            "locator": "passage offset 7180"
          },
          {
            "surface": "retained BioC",
            "file": {
              "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml",
              "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
              "bytes": 174908
            },
            "locator": "passage offset 7328"
          },
          {
            "surface": "retained BioC",
            "file": {
              "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml",
              "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
              "bytes": 174908
            },
            "locator": "passage offset 7370"
          },
          {
            "surface": "retained BioC",
            "file": {
              "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml",
              "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
              "bytes": 174908
            },
            "locator": "passage offset 8457"
          },
          {
            "surface": "retained BioC",
            "file": {
              "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml",
              "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
              "bytes": 174908
            },
            "locator": "passage offset 9102"
          },
          {
            "surface": "retained BioC",
            "file": {
              "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml",
              "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
              "bytes": 174908
            },
            "locator": "passage offset 17378"
          },
          {
            "surface": "retained BioC",
            "file": {
              "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml",
              "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
              "bytes": 174908
            },
            "locator": "passage offset 27057"
          },
          {
            "surface": "retained BioC",
            "file": {
              "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml",
              "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
              "bytes": 174908
            },
            "locator": "passage offset 37515"
          },
          {
            "surface": "retained BioC",
            "file": {
              "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml",
              "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
              "bytes": 174908
            },
            "locator": "passage offset 39253"
          },
          {
            "surface": "retained BioC",
            "file": {
              "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml",
              "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
              "bytes": 174908
            },
            "locator": "passage offset 47480"
          },
          {
            "surface": "retained BioC",
            "file": {
              "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml",
              "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
              "bytes": 174908
            },
            "locator": "passage offset 49122"
          },
          {
            "surface": "retained BioC",
            "file": {
              "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml",
              "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
              "bytes": 174908
            },
            "locator": "passage offset 67131"
          }
        ]
      },
      {
        "field_path": "causal_graphs[0].edges[0].evidence[0].snippet",
        "reference": "DOI:10.1038/nrmicro2549",
        "snippet": "cytoplasmic pH",
        "outcome": "literal_exact",
        "hits": [
          {
            "surface": "indexed abstract",
            "file": {
              "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-metadata.json",
              "sha256": "036607538c4110a45aeab78f8cad03b240ab3648075984f6f3e870b03692e3fd",
              "bytes": 4996
            },
            "locator": "abstractText"
          },
          {
            "surface": "retained BioC",
            "file": {
              "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml",
              "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
              "bytes": 174908
            },
            "locator": "passage offset 58"
          },
          {
            "surface": "retained BioC",
            "file": {
              "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml",
              "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
              "bytes": 174908
            },
            "locator": "passage offset 671"
          },
          {
            "surface": "retained BioC",
            "file": {
              "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml",
              "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
              "bytes": 174908
            },
            "locator": "passage offset 2440"
          },
          {
            "surface": "retained BioC",
            "file": {
              "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml",
              "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
              "bytes": 174908
            },
            "locator": "passage offset 3940"
          },
          {
            "surface": "retained BioC",
            "file": {
              "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml",
              "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
              "bytes": 174908
            },
            "locator": "passage offset 4950"
          },
          {
            "surface": "retained BioC",
            "file": {
              "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml",
              "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
              "bytes": 174908
            },
            "locator": "passage offset 7133"
          },
          {
            "surface": "retained BioC",
            "file": {
              "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml",
              "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
              "bytes": 174908
            },
            "locator": "passage offset 7180"
          },
          {
            "surface": "retained BioC",
            "file": {
              "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml",
              "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
              "bytes": 174908
            },
            "locator": "passage offset 7328"
          },
          {
            "surface": "retained BioC",
            "file": {
              "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml",
              "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
              "bytes": 174908
            },
            "locator": "passage offset 7370"
          },
          {
            "surface": "retained BioC",
            "file": {
              "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml",
              "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
              "bytes": 174908
            },
            "locator": "passage offset 8457"
          },
          {
            "surface": "retained BioC",
            "file": {
              "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml",
              "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
              "bytes": 174908
            },
            "locator": "passage offset 9102"
          },
          {
            "surface": "retained BioC",
            "file": {
              "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml",
              "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
              "bytes": 174908
            },
            "locator": "passage offset 17378"
          },
          {
            "surface": "retained BioC",
            "file": {
              "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml",
              "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
              "bytes": 174908
            },
            "locator": "passage offset 27057"
          },
          {
            "surface": "retained BioC",
            "file": {
              "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml",
              "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
              "bytes": 174908
            },
            "locator": "passage offset 37515"
          },
          {
            "surface": "retained BioC",
            "file": {
              "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml",
              "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
              "bytes": 174908
            },
            "locator": "passage offset 39253"
          },
          {
            "surface": "retained BioC",
            "file": {
              "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml",
              "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
              "bytes": 174908
            },
            "locator": "passage offset 47480"
          },
          {
            "surface": "retained BioC",
            "file": {
              "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml",
              "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
              "bytes": 174908
            },
            "locator": "passage offset 49122"
          },
          {
            "surface": "retained BioC",
            "file": {
              "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml",
              "sha256": "903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f",
              "bytes": 174908
            },
            "locator": "passage offset 67131"
          }
        ]
      },
      {
        "field_path": "causal_graphs[0].edges[1].evidence[0].snippet",
        "reference": "DOI:10.1016/j.tim.2007.02.005",
        "snippet": "proton motive force",
        "outcome": "body_unknown",
        "hits": []
      }
    ],
    "counts": {
      "fields": 3,
      "literal_exact": 2,
      "body_unknown": 1
    },
    "native_result": {
      "verified": 2,
      "not_in_abstract": 1
    },
    "scope": "Only schema snippet fields form this denominator. Quoted notes are separately checked; no false quote inferred from unavailable Baker body."
  },
  "quoted_notes": {
    "completed_at": "2026-10-21T19:58:41.406306+00:00",
    "quoted_note_fields": [
      {
        "field_path": "causal_graphs[0].edges[2].evidence[0].notes",
        "reference": "DOI:10.1111/1758-2229.70019",
        "quoted_fragment": "That proton potential then drives the phosphorylation of ADP and the formation of ATP by the ATP synthase",
        "outcome": "unmarked_omission_meaning_positive",
        "literal_exact": false,
        "ordered_fragments_match": false,
        "primary_file": {
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/bioenergetics.xml",
          "sha256": "481a4f647bc7a835d74f7ec75d5f5ee8fa54ac76294f3c721a6711fd941ec58e",
          "bytes": 324066
        },
        "locator": "zero-based body paragraph 21",
        "scope": "Existing generic/source-attribution scope only.",
        "qualification": "Source inserts a parenthetical between ATP and by the ATP synthase; current quotation omits it without an ellipsis. Meaning positive."
      },
      {
        "field_path": "causal_graphs[0].edges[3].evidence[0].notes",
        "reference": "DOI:10.4014/jmb.2303.03009",
        "quoted_fragment": "decreasing membrane proton permeability prevents the accumulation of intracellular protons",
        "outcome": "literal_exact",
        "literal_exact": true,
        "ordered_fragments_match": true,
        "primary_file": {
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/cfa.xml",
          "sha256": "f37423cf43c8cc6b8d9d64feacad8ec0407e625fce4293e3fab20fac5d1e8acb",
          "bytes": 75721
        },
        "locator": "zero-based body paragraph 6",
        "scope": "Literal occurrence only; detailed pathogen efficacy UNASSESSED_SCOPE.",
        "qualification": "Exact existing fragment; not a biological efficacy certification."
      },
      {
        "field_path": "causal_graphs[0].edges[4].evidence[0].notes",
        "reference": "DOI:10.1111/1758-2229.70019",
        "quoted_fragment": "organic acids... occur in their undissociated form and can diffuse into the cell",
        "outcome": "marked_abridgment",
        "literal_exact": false,
        "ordered_fragments_match": true,
        "primary_file": {
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/bioenergetics.xml",
          "sha256": "481a4f647bc7a835d74f7ec75d5f5ee8fa54ac76294f3c721a6711fd941ec58e",
          "bytes": 324066
        },
        "locator": "zero-based body paragraph 25",
        "scope": "Existing generic/source-attribution scope only.",
        "qualification": "Explicit ellipses mark omitted intervening words; no whole-sentence verbatim claim."
      },
      {
        "field_path": "causal_graphs[0].edges[5].evidence[0].notes",
        "reference": "DOI:10.1111/1758-2229.70019",
        "quoted_fragment": "the higher pH of the cytoplasm will lead to dissociation of the acid, thus releasing protons and lowering the internal pH",
        "outcome": "literal_exact",
        "literal_exact": true,
        "ordered_fragments_match": true,
        "primary_file": {
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/bioenergetics.xml",
          "sha256": "481a4f647bc7a835d74f7ec75d5f5ee8fa54ac76294f3c721a6711fd941ec58e",
          "bytes": 324066
        },
        "locator": "zero-based body paragraph 25",
        "scope": "Existing generic/source-attribution scope only.",
        "qualification": "Exact existing fragment; not a biological efficacy certification."
      },
      {
        "field_path": "causal_graphs[0].edges[6].evidence[0].notes",
        "reference": "DOI:10.3389/fmicb.2023.1149903",
        "quoted_fragment": "a P-type ATPase proton efflux pump",
        "outcome": "literal_exact",
        "literal_exact": true,
        "ordered_fragments_match": true,
        "primary_file": {
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/acid-genomes.xml",
          "sha256": "6f9494d7379f7f7914200f9ba87905a42e803d6173cd22dd1fa837ccefc1f1e0",
          "bytes": 295345
        },
        "locator": "zero-based body paragraph 36",
        "scope": "Existing generic/source-attribution scope only.",
        "qualification": "Exact existing fragment; not a biological efficacy certification."
      },
      {
        "field_path": "causal_graphs[0].edges[7].evidence[0].notes",
        "reference": "DOI:10.3390/microorganisms12030625",
        "quoted_fragment": "acid stress tolerance... facilitated by an active export of protons via the expenditure of ATP... carried out by H+-ATPases",
        "outcome": "marked_abridgment",
        "literal_exact": false,
        "ordered_fragments_match": true,
        "primary_file": {
          "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/homeostasis.xml",
          "sha256": "b5f6a85c09e160674f98031032880e7b52f8e22a465d2678ff48f94dcc95fd94",
          "bytes": 193700
        },
        "locator": "zero-based body paragraph 2",
        "scope": "Existing generic/source-attribution scope only.",
        "qualification": "Explicit ellipses mark omitted intervening words; no whole-sentence verbatim claim."
      }
    ],
    "counts": {
      "fields": 6,
      "literal_exact": 3,
      "marked_abridgment": 2,
      "unmarked_omission_meaning_positive": 1
    },
    "scope": "Separate from native three snippet fields. Quotation precision does not certify biological sufficiency."
  }
}

### Native checklist: all thirteen declared referents

grounding: supported. Targets: METPO:1000460.

The PMF gradient is STATE, ATP formation is a process, permeability/internal pH are measured qualities, and the chemical/protein nodes retain material referents. One reviewed label-only class is explicit. Their coherent individual facets do not excuse the process/process relation mismatch at edge 3.

[
  {
    "index": 0,
    "field_path": "causal_graphs[0].nodes[0]",
    "current": {
      "node_id": "ph_range_low_trait",
      "label": "pH range low",
      "node_type": "TRAIT",
      "grounding": "METPO:1000460",
      "description": "pH growth-supporting range approximately 4\u20136."
    },
    "status": "supported_identity",
    "assessment": "Active METPO identity, direct parent and declared numerical interval agree with the imported class. Scientific equivalence of the broad exact aliases is a separate source-classification question."
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
    "status": "supported_identity",
    "assessment": "The pH-range parent represents a span of external pH values; both imported parent branches provide the numerical-limit context."
  },
  {
    "index": 2,
    "field_path": "causal_graphs[0].nodes[2]",
    "current": {
      "node_id": "acidophile_homeostasis",
      "label": "acidophile pH homeostasis",
      "node_type": "BIOLOGICAL_PROCESS",
      "description": "Proton extrusion and envelope barriers maintaining cytoplasmic pH against a moderately acidic external pH."
    },
    "status": "supported_facet",
    "assessment": "The node denotes maintenance activity and has a coherent BIOLOGICAL_PROCESS referent. Detailed defense efficacy is unassessed."
  },
  {
    "index": 3,
    "field_path": "causal_graphs[0].nodes[3]",
    "current": {
      "node_id": "proton_motive_force",
      "label": "proton motive force",
      "node_type": "STATE",
      "description": "Transmembrane electrochemical proton gradient maintained by H+ extrusion.",
      "grounding": "METPO:1007500"
    },
    "status": "supported_facet",
    "assessment": "The gradient is explicitly STATE, matching the actual v3 local proposal, maintained row 44 and schema distinction between a state and its establishment."
  },
  {
    "index": 4,
    "field_path": "causal_graphs[0].nodes[4]",
    "current": {
      "node_id": "atp_synthase_atp_formation",
      "label": "ATP synthase-mediated ATP formation",
      "node_type": "BIOLOGICAL_PROCESS",
      "description": "Phosphorylation of ADP to ATP driven by the proton motive force."
    },
    "status": "supported_facet",
    "assessment": "ATP formation is explicitly a process, distinct from a material ATP-synthase complex. No copied material-node finding applies."
  },
  {
    "index": 5,
    "field_path": "causal_graphs[0].nodes[5]",
    "current": {
      "node_id": "cyclopropane_fatty_acids",
      "label": "cyclopropane fatty acids",
      "node_type": "CHEMICAL",
      "description": "Cyclopropane-fatty-acyl phospholipids produced by Cfa synthase that modify the membrane."
    },
    "status": "supported_facet",
    "assessment": "The node denotes material fatty-acyl chemicals, not the process that modifies a membrane. This distinction matters to the current regulation edge without assessing biological efficacy."
  },
  {
    "index": 6,
    "field_path": "causal_graphs[0].nodes[6]",
    "current": {
      "node_id": "proton_permeability",
      "label": "membrane proton permeability",
      "node_type": "QUALITY",
      "description": "Permeability of the cell membrane to protons."
    },
    "status": "supported_facet",
    "assessment": "Proton permeability is explicitly a measurable QUALITY. The maintained migration supports this sense; no forced process retype is justified."
  },
  {
    "index": 7,
    "field_path": "causal_graphs[0].nodes[7]",
    "current": {
      "node_id": "undissociated_weak_acids",
      "label": "undissociated weak organic acids",
      "node_type": "CHEMICAL",
      "description": "Protonated, membrane-permeant form of weak organic acids prevalent at low external pH."
    },
    "status": "supported_facet",
    "assessment": "The node denotes the chemical form of weak acids. The description does not require an environmental-condition retype."
  },
  {
    "index": 8,
    "field_path": "causal_graphs[0].nodes[8]",
    "current": {
      "node_id": "weak_acid_influx",
      "label": "weak organic acid influx into cell",
      "node_type": "BIOLOGICAL_PROCESS",
      "description": "Diffusion of undissociated weak organic acids across the membrane at low external pH."
    },
    "status": "supported_facet",
    "assessment": "Influx denotes a process; a free-text undergoes edge has no imported material-subject exclusion."
  },
  {
    "index": 9,
    "field_path": "causal_graphs[0].nodes[9]",
    "current": {
      "node_id": "weak_acid_dissociation",
      "label": "intracellular dissociation of weak organic acids",
      "node_type": "BIOLOGICAL_PROCESS",
      "description": "Dissociation of weak acids in the near-neutral cytoplasm, releasing protons."
    },
    "status": "supported_facet",
    "assessment": "Dissociation denotes a process. Detailed intracellular mechanism or fitness effects are unassessed."
  },
  {
    "index": 10,
    "field_path": "causal_graphs[0].nodes[10]",
    "current": {
      "node_id": "internal_ph",
      "label": "internal (cytoplasmic) pH",
      "node_type": "QUALITY",
      "description": "pH of the cytoplasm."
    },
    "status": "supported_facet",
    "assessment": "Internal pH is a measurable QUALITY, not a process."
  },
  {
    "index": 11,
    "field_path": "causal_graphs[0].nodes[11]",
    "current": {
      "node_id": "h_atpase",
      "label": "H+-ATPase proton efflux pump",
      "node_type": "GENE_OR_PROTEIN",
      "grounding_status": "REVIEWED_LABEL_ONLY",
      "grounding_notes": "Reviewed as a contextual protein or protein-complex label within a quantitative measurement graph; no exact semantic family term was established for this aggregate use.",
      "description": "ATP-driven proton-exporting ATPase (e.g. P-type H+-ATPase)."
    },
    "status": "supported_facet",
    "assessment": "The pump is a material protein class with explicit reviewed-label-only disposition; no token accession or instance is required."
  },
  {
    "index": 12,
    "field_path": "causal_graphs[0].nodes[12]",
    "current": {
      "node_id": "cytoplasmic_protons",
      "label": "cytoplasmic protons",
      "node_type": "CHEMICAL",
      "description": "Protons (hydrons) within the cytoplasm."
    },
    "status": "supported_facet",
    "assessment": "Cytoplasmic protons have a material chemical referent; no obligatory CAPACITY retype follows from localization."
  }
]

### Native checklist: all eight relations

consistency: concern. Targets: METPO:1000460.

RO2212 edge 3 inherits process/process semantics but links material cyclopropane fatty acids to permeability QUALITY. This formal representation issue is separate from unassessed defense efficacy. RO2326 edge 7 and local confers/exports fit current referents; free-text drives, undergoes and lowers receive no invented imported exclusions.

[
  {
    "index": 0,
    "field_path": "causal_graphs[0].edges[0]",
    "current": {
      "subject": "acidophile_homeostasis",
      "predicate": "confers",
      "object": "ph_range_low_trait",
      "description": "Acidophile pH-homeostasis enables growth across pH 4\u20136.",
      "evidence": [
        {
          "reference": "DOI:10.1038/nrmicro2549",
          "snippet": "cytoplasmic pH",
          "notes": "Supports acidophile cytoplasmic pH homeostasis as the moderately-acidic growth-range mechanism."
        }
      ],
      "predicate_id": "METPO:2007700"
    },
    "status": "supported_formal_scope",
    "assessment": "The local v8 confers relation accepts this process-to-trait shape. Source support for the exact numeric bin remains separate from this endpoint assessment."
  },
  {
    "index": 1,
    "field_path": "causal_graphs[0].edges[1]",
    "current": {
      "subject": "ph_range_low_trait",
      "predicate": "is a",
      "object": "ph_range",
      "description": "pH range low is a quantitative bin of the pH-range phenotype.",
      "evidence": [
        {
          "reference": "DOI:10.1016/j.tim.2007.02.005",
          "snippet": "proton motive force",
          "notes": "Supports the pH 4\u20136 range as a value within the pH-range distribution."
        }
      ],
      "predicate_id": "rdfs:subClassOf"
    },
    "status": "supported_identity",
    "assessment": "The subclass relation and current direct parent are supported. The source attribution for exact numeric calibration is assessed separately by the source audit."
  },
  {
    "index": 2,
    "field_path": "causal_graphs[0].edges[2]",
    "current": {
      "subject": "proton_motive_force",
      "predicate": "drives",
      "object": "atp_synthase_atp_formation",
      "description": "The proton motive force drives ATP synthase phosphorylation of ADP to ATP.",
      "evidence": [
        {
          "reference": "DOI:10.1111/1758-2229.70019",
          "notes": "\"That proton potential then drives the phosphorylation of ADP and the formation of ATP by the ATP synthase\"; general bioenergetic edge relevant to low-pH growth."
        }
      ]
    },
    "status": "supported_formal_scope",
    "assessment": "Free-text drives is not an asserted RO enables edge. STATE-to-process is not automatically prohibited, and no predicate grounding is mandatory."
  },
  {
    "index": 3,
    "field_path": "causal_graphs[0].edges[3]",
    "current": {
      "subject": "cyclopropane_fatty_acids",
      "predicate": "decreases",
      "object": "proton_permeability",
      "description": "Cyclopropane fatty acid membrane modification decreases proton permeability.",
      "evidence": [
        {
          "reference": "DOI:10.4014/jmb.2303.03009",
          "notes": "\"decreasing membrane proton permeability prevents the accumulation of intracellular protons\" after conversion to cyclopropane fatty acids; generalizable membrane adaptation."
        }
      ],
      "predicate_id": "RO:0002212"
    },
    "status": "major_formal_roles",
    "assessment": "RO:0002212 is a subproperty of RO:0002211, whose actual primary statements declare process domain and range. Current material cyclopropane fatty acids and permeability QUALITY are not the processes required by that relation. This is a formal representation issue, not a finding that the biological statement is false."
  },
  {
    "index": 4,
    "field_path": "causal_graphs[0].edges[4]",
    "current": {
      "subject": "undissociated_weak_acids",
      "predicate": "undergoes",
      "object": "weak_acid_influx",
      "description": "At low external pH weak organic acids are undissociated and diffuse into the cell.",
      "evidence": [
        {
          "reference": "DOI:10.1111/1758-2229.70019",
          "notes": "\"organic acids... occur in their undissociated form and can diffuse into the cell\"; boundary condition distinguishing low-pH growth from weak-acid inhibition."
        }
      ]
    },
    "status": "supported_formal_scope",
    "assessment": "Free-text undergoes permits the current material-to-influx documentary reading; no external formal range restriction is asserted."
  },
  {
    "index": 5,
    "field_path": "causal_graphs[0].edges[5]",
    "current": {
      "subject": "weak_acid_dissociation",
      "predicate": "lowers",
      "object": "internal_ph",
      "description": "Intracellular dissociation of weak organic acids releases protons and lowers cytoplasmic pH.",
      "evidence": [
        {
          "reference": "DOI:10.1111/1758-2229.70019",
          "notes": "\"the higher pH of the cytoplasm will lead to dissociation of the acid, thus releasing protons and lowering the internal pH\"; strong causal edge."
        }
      ]
    },
    "status": "supported_formal_scope",
    "assessment": "Free-text lowers has no imported process/process constraint. A process affecting a measured pH quality is not by itself a formal defect."
  },
  {
    "index": 6,
    "field_path": "causal_graphs[0].edges[6]",
    "current": {
      "subject": "h_atpase",
      "predicate": "exports",
      "object": "cytoplasmic_protons",
      "description": "H+-ATPases actively export protons from the cytoplasm using ATP.",
      "evidence": [
        {
          "reference": "DOI:10.3389/fmicb.2023.1149903",
          "notes": "Acidophile genomes encode \"a P-type ATPase proton efflux pump\"; active ATP-driven proton export underlies cytoplasmic pH homeostasis."
        }
      ],
      "predicate_id": "METPO:2007804"
    },
    "status": "supported_formal_scope",
    "assessment": "The actual v9 exports definition and maintained gate admit protein subject and chemical object, with movement from cytoplasm to exterior. Detailed transport efficacy is unassessed."
  },
  {
    "index": 7,
    "field_path": "causal_graphs[0].edges[7]",
    "current": {
      "subject": "h_atpase",
      "predicate": "contributes to",
      "object": "acidophile_homeostasis",
      "description": "ATP-driven proton export by H+-ATPases contributes to acidophile pH homeostasis.",
      "evidence": [
        {
          "reference": "DOI:10.3390/microorganisms12030625",
          "notes": "\"acid stress tolerance... facilitated by an active export of protons via the expenditure of ATP... carried out by H+-ATPases\"; broad principle of homeostasis."
        }
      ],
      "predicate_id": "RO:0002326"
    },
    "status": "supported_formal_scope",
    "assessment": "The material ATPase and maintenance-process object satisfy the inherited material/process requirements of RO:0002326. No blanket chemical or protein rule is applied."
  }
]

### Native checklist: bounded environmental and literal context

scope: unknown. Targets: METPO:1000460.

Existing generic environmental PMF and weak-acid chemistry, source-specific genomic presence and yeast background are considered only within inspected scope. CFA defense biology and all detailed pathogen fitness/AMR, perturbation and optimization efficacy remain UNASSESSED_SCOPE. No repaired route, improved condition or experiment is proposed.

{
  "completed_at": "2026-10-21T19:58:41.401685+00:00",
  "edges": [
    {
      "index": 0,
      "field_path": "causal_graphs[0].edges[0]",
      "subject": "acidophile_homeostasis",
      "predicate": "confers",
      "predicate_id": "METPO:2007700",
      "object": "ph_range_low_trait",
      "description": "Acidophile pH-homeostasis enables growth across pH 4\u20136.",
      "evidence": [
        {
          "reference": "DOI:10.1038/nrmicro2549",
          "snippet": "cytoplasmic pH",
          "notes": "Supports acidophile cytoplasmic pH homeostasis as the moderately-acidic growth-range mechanism."
        }
      ],
      "assessment": "Actual generic homeostasis context is positive, but acidophile categories and physiological mechanisms do not establish an exact complete4\u20136 interval. Group scope with category/bin assessment; no biological falsity or universal mechanism is inferred.",
      "biological_scope": "Existing generic environmental/chemical context only; no new mechanism or intervention efficacy."
    },
    {
      "index": 1,
      "field_path": "causal_graphs[0].edges[1]",
      "subject": "ph_range_low_trait",
      "predicate": "is a",
      "predicate_id": "rdfs:subClassOf",
      "object": "ph_range",
      "description": "pH range low is a quantitative bin of the pH-range phenotype.",
      "evidence": [
        {
          "reference": "DOI:10.1016/j.tim.2007.02.005",
          "snippet": "proton motive force",
          "notes": "Supports the pH 4\u20136 range as a value within the pH-range distribution."
        }
      ],
      "assessment": "Ontology supplies the parent/bin hierarchy. Baker abstract classifies acidophiles by optimum below3 and supports generic homeostasis; it does not directly calibrate a complete4\u20136 interval. Assigned PMF body phrase remains unknown; lack of abstract occurrence is not a false quotation.",
      "biological_scope": "Existing generic environmental/chemical context only; no new mechanism or intervention efficacy."
    },
    {
      "index": 2,
      "field_path": "causal_graphs[0].edges[2]",
      "subject": "proton_motive_force",
      "predicate": "drives",
      "predicate_id": null,
      "object": "atp_synthase_atp_formation",
      "description": "The proton motive force drives ATP synthase phosphorylation of ADP to ATP.",
      "evidence": [
        {
          "reference": "DOI:10.1111/1758-2229.70019",
          "notes": "\"That proton potential then drives the phosphorylation of ADP and the formation of ATP by the ATP synthase\"; general bioenergetic edge relevant to low-pH growth."
        }
      ],
      "assessment": "Existing generic PMF-to-ATP statement is supported at bioenergetics body21. The quoted note removes an intervening parenthesis without an ellipsis; meaning remains positive and no efficacy/intervention inference is made.",
      "biological_scope": "Existing generic environmental/chemical context only; no new mechanism or intervention efficacy."
    },
    {
      "index": 3,
      "field_path": "causal_graphs[0].edges[3]",
      "subject": "cyclopropane_fatty_acids",
      "predicate": "decreases",
      "predicate_id": "RO:0002212",
      "object": "proton_permeability",
      "description": "Cyclopropane fatty acid membrane modification decreases proton permeability.",
      "evidence": [
        {
          "reference": "DOI:10.4014/jmb.2303.03009",
          "notes": "\"decreasing membrane proton permeability prevents the accumulation of intracellular protons\" after conversion to cyclopropane fatty acids; generalizable membrane adaptation."
        }
      ],
      "assessment": "Current quoted fragment is literally present in CFA body6. Source title/abstract identify pathogenic Gram-negative acid-defense scope. Only identity, quote occurrence and separately audited formal roles are assessed; generalizable biological efficacy is UNASSESSED_SCOPE.",
      "biological_scope": "UNASSESSED_SCOPE"
    },
    {
      "index": 4,
      "field_path": "causal_graphs[0].edges[4]",
      "subject": "undissociated_weak_acids",
      "predicate": "undergoes",
      "predicate_id": null,
      "object": "weak_acid_influx",
      "description": "At low external pH weak organic acids are undissociated and diffuse into the cell.",
      "evidence": [
        {
          "reference": "DOI:10.1111/1758-2229.70019",
          "notes": "\"organic acids... occur in their undissociated form and can diffuse into the cell\"; boundary condition distinguishing low-pH growth from weak-acid inhibition."
        }
      ],
      "assessment": "Actual environmental review body25 supports the existing generic weak-acid permeability context. Quoted note is a marked noncontiguous abridgment with literal ordered fragments. It does not itself establish complete4\u20136 growth or a universal lineage response.",
      "biological_scope": "Existing generic environmental/chemical context only; no new mechanism or intervention efficacy."
    },
    {
      "index": 5,
      "field_path": "causal_graphs[0].edges[5]",
      "subject": "weak_acid_dissociation",
      "predicate": "lowers",
      "predicate_id": null,
      "object": "internal_ph",
      "description": "Intracellular dissociation of weak organic acids releases protons and lowers cytoplasmic pH.",
      "evidence": [
        {
          "reference": "DOI:10.1111/1758-2229.70019",
          "notes": "\"the higher pH of the cytoplasm will lead to dissociation of the acid, thus releasing protons and lowering the internal pH\"; strong causal edge."
        }
      ],
      "assessment": "Actual environmental review body25 contains the current quoted dissociation/pH sentence as a contiguous phrase. Generic acid-base chemistry is positive; no new intervention conditions or acid-defense efficacy assessment.",
      "biological_scope": "Existing generic environmental/chemical context only; no new mechanism or intervention efficacy."
    },
    {
      "index": 6,
      "field_path": "causal_graphs[0].edges[6]",
      "subject": "h_atpase",
      "predicate": "exports",
      "predicate_id": "METPO:2007804",
      "object": "cytoplasmic_protons",
      "description": "H+-ATPases actively export protons from the cytoplasm using ATP.",
      "evidence": [
        {
          "reference": "DOI:10.3389/fmicb.2023.1149903",
          "notes": "Acidophile genomes encode \"a P-type ATPase proton efflux pump\"; active ATP-driven proton export underlies cytoplasmic pH homeostasis."
        }
      ],
      "assessment": "Actual environmental review body36 contains the quoted P-type-pump phrase in the named At. ferrivorans SS3 genome context, with absence in another reported MAG. Existing contextual presence is positive; genomic annotation is not direct functional validation or universal necessity.",
      "biological_scope": "Existing generic environmental/chemical context only; no new mechanism or intervention efficacy."
    },
    {
      "index": 7,
      "field_path": "causal_graphs[0].edges[7]",
      "subject": "h_atpase",
      "predicate": "contributes to",
      "predicate_id": "RO:0002326",
      "object": "acidophile_homeostasis",
      "description": "ATP-driven proton export by H+-ATPases contributes to acidophile pH homeostasis.",
      "evidence": [
        {
          "reference": "DOI:10.3390/microorganisms12030625",
          "notes": "\"acid stress tolerance... facilitated by an active export of protons via the expenditure of ATP... carried out by H+-ATPases\"; broad principle of homeostasis."
        }
      ],
      "assessment": "Actual yeast article body2 gives the generic existing proton-export background sentence. Note is marked abridgment; source context is S. cerevisiae and background citations, not the new engineered-pump result. No perturbation efficacy, optimization or exact4\u20136 calibration is adopted.",
      "biological_scope": "Existing generic environmental/chemical context only; no new mechanism or intervention efficacy."
    }
  ]
}

### Native checklist: whole-record coverage and optional evidence

completeness: supported. Targets: METPO:1000460.

All thirteen nodes, eight edges, five components, twelve events, one canonical, three schema snippets and six quote-bearing notes are covered. One reviewed label-only protein class and zero instances are allowed; no token accession, extra connector, pathway or substitute canonical is required.

{
  "completed_at": "2026-10-21T19:58:41.401839+00:00",
  "nodes": [
    {
      "index": 0,
      "field_path": "causal_graphs[0].nodes[0]",
      "node": {
        "node_id": "ph_range_low_trait",
        "label": "pH range low",
        "node_type": "TRAIT",
        "grounding": "METPO:1000460",
        "description": "pH growth-supporting range approximately 4\u20136."
      },
      "incident_edges": [
        0,
        1
      ],
      "references": [
        "DOI:10.1016/j.tim.2007.02.005",
        "DOI:10.1038/nrmicro2549"
      ],
      "assessment": "All incident source placements accounted for. Complete4\u20136 interval is distinct from broad acidophily categories and contextual physiology."
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
        "DOI:10.1016/j.tim.2007.02.005"
      ],
      "assessment": "All incident source placements accounted for. Existing generic environmental, chemistry or documentary identity context only. No universal biological mechanism or exact-bin sufficient cause is inferred."
    },
    {
      "index": 2,
      "field_path": "causal_graphs[0].nodes[2]",
      "node": {
        "node_id": "acidophile_homeostasis",
        "label": "acidophile pH homeostasis",
        "node_type": "BIOLOGICAL_PROCESS",
        "description": "Proton extrusion and envelope barriers maintaining cytoplasmic pH against a moderately acidic external pH."
      },
      "incident_edges": [
        0,
        7
      ],
      "references": [
        "DOI:10.1038/nrmicro2549",
        "DOI:10.3390/microorganisms12030625"
      ],
      "assessment": "All incident source placements accounted for. Existing generic environmental, chemistry or documentary identity context only. No universal biological mechanism or exact-bin sufficient cause is inferred."
    },
    {
      "index": 3,
      "field_path": "causal_graphs[0].nodes[3]",
      "node": {
        "node_id": "proton_motive_force",
        "label": "proton motive force",
        "node_type": "STATE",
        "description": "Transmembrane electrochemical proton gradient maintained by H+ extrusion.",
        "grounding": "METPO:1007500"
      },
      "incident_edges": [
        2
      ],
      "references": [
        "DOI:10.1111/1758-2229.70019"
      ],
      "assessment": "All incident source placements accounted for. Existing generic environmental, chemistry or documentary identity context only. No universal biological mechanism or exact-bin sufficient cause is inferred."
    },
    {
      "index": 4,
      "field_path": "causal_graphs[0].nodes[4]",
      "node": {
        "node_id": "atp_synthase_atp_formation",
        "label": "ATP synthase-mediated ATP formation",
        "node_type": "BIOLOGICAL_PROCESS",
        "description": "Phosphorylation of ADP to ATP driven by the proton motive force."
      },
      "incident_edges": [
        2
      ],
      "references": [
        "DOI:10.1111/1758-2229.70019"
      ],
      "assessment": "All incident source placements accounted for. Existing generic environmental, chemistry or documentary identity context only. No universal biological mechanism or exact-bin sufficient cause is inferred."
    },
    {
      "index": 5,
      "field_path": "causal_graphs[0].nodes[5]",
      "node": {
        "node_id": "cyclopropane_fatty_acids",
        "label": "cyclopropane fatty acids",
        "node_type": "CHEMICAL",
        "description": "Cyclopropane-fatty-acyl phospholipids produced by Cfa synthase that modify the membrane."
      },
      "incident_edges": [
        3
      ],
      "references": [
        "DOI:10.4014/jmb.2303.03009"
      ],
      "assessment": "All incident source placements accounted for. CFA-linked detailed acid-defense/fitness/efficacy remains UNASSESSED_SCOPE; current label/quote/identity only."
    },
    {
      "index": 6,
      "field_path": "causal_graphs[0].nodes[6]",
      "node": {
        "node_id": "proton_permeability",
        "label": "membrane proton permeability",
        "node_type": "QUALITY",
        "description": "Permeability of the cell membrane to protons."
      },
      "incident_edges": [
        3
      ],
      "references": [
        "DOI:10.4014/jmb.2303.03009"
      ],
      "assessment": "All incident source placements accounted for. CFA-linked detailed acid-defense/fitness/efficacy remains UNASSESSED_SCOPE; current label/quote/identity only."
    },
    {
      "index": 7,
      "field_path": "causal_graphs[0].nodes[7]",
      "node": {
        "node_id": "undissociated_weak_acids",
        "label": "undissociated weak organic acids",
        "node_type": "CHEMICAL",
        "description": "Protonated, membrane-permeant form of weak organic acids prevalent at low external pH."
      },
      "incident_edges": [
        4
      ],
      "references": [
        "DOI:10.1111/1758-2229.70019"
      ],
      "assessment": "All incident source placements accounted for. Existing generic environmental, chemistry or documentary identity context only. No universal biological mechanism or exact-bin sufficient cause is inferred."
    },
    {
      "index": 8,
      "field_path": "causal_graphs[0].nodes[8]",
      "node": {
        "node_id": "weak_acid_influx",
        "label": "weak organic acid influx into cell",
        "node_type": "BIOLOGICAL_PROCESS",
        "description": "Diffusion of undissociated weak organic acids across the membrane at low external pH."
      },
      "incident_edges": [
        4
      ],
      "references": [
        "DOI:10.1111/1758-2229.70019"
      ],
      "assessment": "All incident source placements accounted for. Existing generic environmental, chemistry or documentary identity context only. No universal biological mechanism or exact-bin sufficient cause is inferred."
    },
    {
      "index": 9,
      "field_path": "causal_graphs[0].nodes[9]",
      "node": {
        "node_id": "weak_acid_dissociation",
        "label": "intracellular dissociation of weak organic acids",
        "node_type": "BIOLOGICAL_PROCESS",
        "description": "Dissociation of weak acids in the near-neutral cytoplasm, releasing protons."
      },
      "incident_edges": [
        5
      ],
      "references": [
        "DOI:10.1111/1758-2229.70019"
      ],
      "assessment": "All incident source placements accounted for. Existing generic environmental, chemistry or documentary identity context only. No universal biological mechanism or exact-bin sufficient cause is inferred."
    },
    {
      "index": 10,
      "field_path": "causal_graphs[0].nodes[10]",
      "node": {
        "node_id": "internal_ph",
        "label": "internal (cytoplasmic) pH",
        "node_type": "QUALITY",
        "description": "pH of the cytoplasm."
      },
      "incident_edges": [
        5
      ],
      "references": [
        "DOI:10.1111/1758-2229.70019"
      ],
      "assessment": "All incident source placements accounted for. Existing generic environmental, chemistry or documentary identity context only. No universal biological mechanism or exact-bin sufficient cause is inferred."
    },
    {
      "index": 11,
      "field_path": "causal_graphs[0].nodes[11]",
      "node": {
        "node_id": "h_atpase",
        "label": "H+-ATPase proton efflux pump",
        "node_type": "GENE_OR_PROTEIN",
        "grounding_status": "REVIEWED_LABEL_ONLY",
        "grounding_notes": "Reviewed as a contextual protein or protein-complex label within a quantitative measurement graph; no exact semantic family term was established for this aggregate use.",
        "description": "ATP-driven proton-exporting ATPase (e.g. P-type H+-ATPase)."
      },
      "incident_edges": [
        6,
        7
      ],
      "references": [
        "DOI:10.3389/fmicb.2023.1149903",
        "DOI:10.3390/microorganisms12030625"
      ],
      "assessment": "All incident source placements accounted for. Existing generic environmental, chemistry or documentary identity context only. No universal biological mechanism or exact-bin sufficient cause is inferred."
    },
    {
      "index": 12,
      "field_path": "causal_graphs[0].nodes[12]",
      "node": {
        "node_id": "cytoplasmic_protons",
        "label": "cytoplasmic protons",
        "node_type": "CHEMICAL",
        "description": "Protons (hydrons) within the cytoplasm."
      },
      "incident_edges": [
        6
      ],
      "references": [
        "DOI:10.3389/fmicb.2023.1149903"
      ],
      "assessment": "All incident source placements accounted for. Existing generic environmental, chemistry or documentary identity context only. No universal biological mechanism or exact-bin sufficient cause is inferred."
    }
  ]
}

### Native checklist: exact canonical catalog applicability

evidence: unknown. Targets: METPO:1000460.

The actual retained 20-organism/28-dataset catalog has no exact match for Acidithiobacillus ferrooxidans or its three official retained synonyms. This bounded catalog result is not global expression-data absence. No organism or strain substitution, detailed module query or phenotype inference is made.

{
  "completed_at": "2026-10-21T19:57:19.764268+00:00",
  "canonical_taxon": "NCBITaxon:920",
  "status": "NO_MATCH_IN_RETAINED_CANONICAL_CATALOG",
  "catalog_check": {
    "checked_at": "2026-10-21T19:55:46.535616+00:00",
    "catalog_path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-grounding-agent/reused-datasets.json",
    "catalog_sha256": "155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693",
    "original_access_receipt": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-grounding-agent/reused-catalog-accesses.json",
    "canonical_taxon": "NCBITaxon:920",
    "names": [
      "Acidithiobacillus ferrooxidans",
      "Ferrobacillus ferrooxidans",
      "Ferrobacillus sulfooxidans",
      "Thiobacillus ferrooxidans"
    ],
    "organisms": 20,
    "datasets": 28,
    "matches": [],
    "scope": "Exact supplied canonical species and official retained synonyms only. No substitute organism, strain or detailed gene/module query."
  },
  "assessment": "None of the exact current species name or three official retained synonyms matches the retained 20-organism, 28-dataset catalog. This bounded catalog absence is not a claim about all public expression data. No other species or strain is substituted.",
  "downstream_gene_module_queries": "NOT_RUN",
  "protein_instances": 0,
  "uniprot_instance_audit": "NOT_APPLICABLE",
  "scope": "Identity/applicability only; no detailed acid-defense, stress, fitness or AMR queries."
}

### Native checklist: direct writers and replay limits

provenance: supported. Targets: METPO:1000460.

Seeder owns exact-alias import. Permeability migration directly maintains QUALITY, while its edge rewrite is restricted to maximal-growth-rate enables and cannot repair current decreases. Shared predicate grounder skips nonempty IDs. Historical confers writer was whole-read only after the successful 83-input supplement; its old-RO2327 selection does not replay current confers. Current exports likewise does not match the old migration key.

{
  "completed_at": "2026-10-21T19:57:19.764268+00:00",
  "target": "data/traits/environment/ph_range_low.yaml",
  "owners": [
    {
      "path": "data/traits/environment/ph_range_low.yaml",
      "locators": [
        "causal_graphs[0].edges[3]"
      ],
      "role": "Maintained current assertion; other records with the same node are not automatically owners.",
      "sha256": "56a1489044011c883b75e007e5eb0d6a67984b791e77d8f02cf70c64e7fccff0"
    },
    {
      "path": "mappings/predicate_grounding.tsv",
      "locators": [
        "61",
        "91",
        "102"
      ],
      "role": "Exact decreases-to-RO2212, exports and confers rows. Wildcard local gates do not remove imported RO semantics.",
      "sha256": "8e28c19e93aca3dc164a3befbe2612b289241de457c59f499e65936c03b7ce52"
    },
    {
      "path": "scripts/ground_causal_predicates.py",
      "locators": [
        "136\u2013180"
      ],
      "role": "Grounds only empty predicate_id fields. The populated current relation is skipped, so changing a mapping row alone does not rewrite it.",
      "sha256": "5a788eeaabf3a56b0d82c469a3e3fe28f1d51707d9382313b9a94289be7d1381"
    },
    {
      "path": "scripts/migrate_process_quality_consistency.py",
      "locators": [
        "77\u201392",
        "148\u2013207"
      ],
      "role": "Direct proton_permeability QUALITY normalization owner. Its relation rewrite is restricted to maximal_growth_rate enables edges; it does not repair this current decreases edge.",
      "sha256": "1a83ad3dba79ed0c958b875a6fcc4b9e562259af26da2f248d32d5cf7784f80a"
    },
    {
      "path": "scripts/migrate_node_type_consistency.py",
      "locators": [
        "54\u201368",
        "135\u2013168"
      ],
      "role": "Direct PMF STATE normalization owner; positive context, not an additional current defect.",
      "sha256": "a3e7bc170e60f406a73e06c893d74f5253671028d3d40cc15ecf882b6684a69e"
    },
    {
      "path": "mappings/node_grounding.tsv",
      "locators": [
        "44"
      ],
      "role": "Current PMF STATE-to-local-class grounding owner.",
      "sha256": "d7de9b3ab04960c4775a5bc295a945bd1a72d81467830459f4793e654f82b3d0"
    },
    {
      "path": "scripts/seed_from_metpo.py",
      "locators": [
        "198\u2013209",
        "333\u2013348"
      ],
      "role": "Direct alias import owner, preserving upstream synonym types. Scientific exactness is a separate question.",
      "sha256": "0fb9c9f7ea6a8f137eecd5c319775b511c398dba6158c81b1fbfb94210f7d851"
    },
    {
      "path": "scripts/migrate_enables_trait_edges.py",
      "locators": [
        "77\u201399",
        "123\u2013162",
        "231\u2013262"
      ],
      "role": "Historical confers migration owner, read only after supplemental capture. It selects old RO2327 edges with TRAIT objects; already-current confers is not selected on replay.",
      "sha256": "a5e7965ee4f6b6ba5bae3a06bced2a83cbf755f3b9b150ce6acc0cd808cb1d88"
    },
    {
      "path": "scripts/migrate_remaining_microbe_domain_edges.py",
      "locators": [
        "57\u201389",
        "92\u2013121"
      ],
      "role": "Historical exports migration owner. Selection requires the old METPO2000209 plus exports key; current METPO2007804 is not selected on replay.",
      "sha256": "110542d49e25007122c7c254966ad87dc3f7f054358766e933aff89e8ef0a994"
    }
  ],
  "search": {
    "ignored_hidden_included": true,
    "matching_paths": 215,
    "parsed_review_target_arrays": 67,
    "exact_target_arrays": 0,
    "excluded": [
      ".git/**",
      ".venv/**"
    ],
    "scope": "Entire owned repository including ignored/hidden files, excluding Git internals and virtual environment. Exact target identity/slug/label and numerical synonym; broad physiological aliases are not treated as exact target signoff."
  },
  "all_node_search": {
    "nodes": 13,
    "captured_history_leads": 8,
    "uncaptured_history_leads": 0
  },
  "whole_histories_read": [
    "history/infrastructure/inconsistent-node-type/2026-08-12T000912Z-claude-code-779670.yaml",
    "history/infrastructure/node-type-consistency/2026-08-15T014631Z-claude-code-9d7f4d.yaml",
    "history/infrastructure/pathway-vs-process/2026-08-16T010630Z-claude-code-192557.yaml",
    "history/infrastructure/predicate-gate-audit/2026-08-16T074719Z-claude-code-84d88d.yaml",
    "history/infrastructure/process-quality-consistency/2026-08-21T073211Z-codex-174227.yaml",
    "history/other/canonical-examples-batch1/2026-08-20T074839Z-claude-code-6fb2f5.yaml",
    "history/other/canonical-examples-six/2026-08-21T065406Z-codex-a1ab82.yaml",
    "history/records/ph_range_mid2/2026-09-04T024000Z-codex-3036b8.yaml"
  ],
  "history_disposition": "All eight history files were read in full. All actors are AI. The canonical-examples-six history explicitly mentions recovery of this record\u2019s exemplar while preserving newer fields; it is positive target-specific curation context, not human acceptance. Infrastructure migrations and ph_range_mid2 history are direct family or sibling context, not independent exact-target signoff.",
  "record_events": {
    "total": 12,
    "ai": 11,
    "seed": 1
  },
  "human_traceability": "Within the bounded ignored-inclusive search, 67 actual structured-review target arrays contain no exact target array. Current REVIEWED status and AI curation do not establish a linked human acceptance; this does not claim that no human ever reviewed the record.",
  "report": {
    "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/repo/research/traits/environment/ph_range_low-deep-research-falcon.md",
    "sha256": "a9d2d36a3b7e1cbe5d6cb6dab50577315df72fc835514366d60c0f087238ab13",
    "bytes": 38451,
    "reading_scope": "Only frontmatter and initial target/template context, lines 1\u201370, were read as generated provenance/lead material. August 4 02:53:08.192544\u201303:01:36.402669 generation is not proof of the exact June 23 enrichment version. No report mechanism or intervention recommendation is adopted."
  },
  "context_only": "Shared PMF/permeability hits in ph_delta/ph_phenotype/ph_range_mid2 writers are sibling context. No exact current canonical insertion script was established by the bounded searches; the actual historical canonical-six receipt is retained instead.",
  "capture_chronology": {
    "path": "/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-grounding-agent/capture-supplement-verification.json",
    "sha256": "8f0f152275089fd1658c89af99c883144a11f325acfbd0076b910f4d650702a7",
    "bytes": 1015
  }
}

### Native checklist: bounded local acceptance traceability

provenance: concern. Targets: METPO:1000460.

The record has eleven AI-assisted events plus seed. Ground auditor whole-read eight AI history contexts; target-specific canonical recovery remains positive curation provenance. Ignored-inclusive search returned 215 paths and 67 actual review arrays, none exact to this target. These facts and REVIEWED status do not establish a linked current human acceptance; private/remote absence is not asserted.

### Native checklist: actual gates and 82-to-83 chronology

consistency: supported. Targets: METPO:1000460.

Original 82 inputs remain unchanged in the separately retained final 83-input capture. All frozen artifacts match and focused native/strict/snippet checks passed. Original common diagnostic failures/skips/retries and B10 QC times remain qualified reuse, not new B11 runs. Source zero hit and publisher-access failures remain distinct from native success.

## Findings

### category-versus-complete-interval: Broad acidophile categories are exact aliases for a numerical interval

major / open / confirmed; issue key: ph-range-low-category-versus-complete-interval.

The four broad category aliases are not coextensive with a complete 4–6 growth interval. Assigned environmental sources distinguish optimum-based categories from growth ranges, including moderate ranges extending outside 4–6 and extreme growth below 3. Preserve active numeric identity, source-specific cutoff conventions and generic acidic physiology; the inspected passages are not exhaustive definitions of every facultative or obligate term.

### regulation-endpoints: Process-regulation relation links a chemical to a measured quality

major / open / confirmed; issue key: ph-range-low-regulation-endpoints.

Current edge 3 asserts RO2212 between material cyclopropane fatty acids and permeability QUALITY. Its inherited RO2211 process domain and range do not describe those explicit referents. This is a formal representation issue; the source fragment occurrence does not validate excluded pathogen-defense efficacy, and no false biological meaning or mechanistic repair is inferred.

### unmarked-note-omission: Quoted note omits an intervening parenthesis without an ellipsis

minor / open / confirmed; issue key: ph-range-low-unmarked-note-omission.

The assigned generic PMF/ATP sentence contains an intervening parenthetical that the current edge 2 quotation omits without a marker. Its biological meaning remains supported; clarify literal quotation precision. Explicitly marked abridgments in notes 4 and 7 are separate and are not called false quotations.

### human-acceptance-link: Current local provenance lacks an attributable acceptance link

minor / open / confirmed; issue key: ph-range-low-human-acceptance-link.

Eleven AI events plus seed, eight AI history contexts and REVIEWED status do not independently identify current human acceptance. The retained ignored-inclusive search and 67 parsed review arrays bound this traceability concern; no private or remote absence is asserted.

## Recommended Actions And Acceptance Checks

### reconcile-category-aliases

Reconcile the four exact category aliases with the intended complete-interval bin during separately authorized curation.

- Retain faithful upstream import provenance, active numeric identity and per-source cutoff differences.
- Do not invent exhaustive facultative/obligate definitions, require a new canonical or duplicate this scope issue across contextual statements.
- Use guarded history, appropriate native/strict/source checks and a successor review after changed inputs.

### reconcile-regulation-role

Reconcile the current edge 3 relation with its explicit material and quality referents.

- Preserve the distinction between formal role semantics and excluded biological efficacy; do not force a new pathway or mechanism.
- Account for nonempty-ID preservation and the limited relation rewrite in the quality maintainer.
- Use appropriate guarded curation/history and follow-up review rather than assuming table edits rewrite populated edges.

### clarify-quoted-note

Mark the omitted parenthetical or use an accurate contiguous quotation in the edge 2 note.

- Keep positive source meaning and exact attribution.
- Keep the native snippet and quoted-note denominators separate; no biological correction or optimization is needed.

### link-human-acceptance

Link attributable acceptance of the current record if available, or clarify status while preserving provenance.

- Retain actual AI/seed and bounded local search evidence.
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
| check-ph-range-low-native | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-native.log; Executed 2026-10-21T19:53:47.173588+00:00 through 2026-10-21T19:53:47.774084+00:00; metadata ph-range-low-native.json | context_only | Successful focused schema validation; formal scientific roles remain separately assessed. |
| check-ph-range-low-strict | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-strict.log; Executed 2026-10-21T19:53:47.173589+00:00 through 2026-10-21T19:53:48.176273+00:00; metadata ph-range-low-strict.json | context_only | Successful focused strict validation; no detailed biological efficacy certification. |
| check-ph-range-low-snippets | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-snippets.log; Executed 2026-10-21T19:53:49.439585+00:00 through 2026-10-21T19:53:53.132889+00:00; metadata ph-range-low-snippets.json | context_only | Three schema snippet fields: two VERIFIED and one NOT_IN_ABSTRACT. Six quoted note fields are separately assessed: three literal, two marked abridgments, one unmarked omission with positive meaning. Native results are preserved. |
| check-batch010-qc | /private/tmp/traitmech-record-sweep-010.m7q2v9cx/batch010-qc.log; Executed 2026-10-21T19:06:27.731868+00:00 through 2026-10-21T19:08:11.219124+00:00; metadata batch010-qc.json | context_only | Actual B10 final QC at its original time, qualified against B11 bytes; not a fresh B11 execution. |
| record | data/traits/environment/ph_range_low.yaml; Entire current record | supports | All thirteen nodes, eight edges, three schema snippets, six quote-bearing notes, one canonical and twelve record events are covered. |
| policy | docs/GROUNDING_POLICY.md; Captured maintained authority | supports | Reviewed label-only protein classes and optional instances; declared material/activity referents remain distinct. |
| playbook | docs/CURATION_PLAYBOOK.md; Captured maintained authority | supports | Exact attribution, quotation precision, source scope and attributable current acceptance. |
| schema | src/traitmech/schema/traitmech.yaml; Captured maintained authority | supports | Actual process, state, chemical, quality and trait facets. |
| checklist | .claude/skills/curate-yaml-record/references/review-checklist.md; Captured maintained authority | supports | Complete identity, evidence, graph, ownership, optional evidence and readiness assessment. |
| reuse | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-b10-qc-supplement-qualified.json; Actual B10-to-B11 qualification | supports | Original diagnostic outcomes and current byte comparisons remain bound. |
| reuse-postcheck | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-output-verification-agent/post-execution-verification.json; Actual independent qualifier postcheck | supports | Byte and native-output bindings independently verified without new QC. |
| initial-capture | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low.inspect.json; Original 82-input native capture | supports | Retained original successful capture; all 82 inputs are unchanged in the final supplement. |
| supplement-command | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low.inspect-supplemented-command.json; Actual separate native supplement execution | supports | The newly discovered exact historical writer was captured before interpretation; no original capture was overwritten. |
| capture | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-grounding-agent/capture-supplement-verification.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Final 83-input capture verified against unchanged original 82. |
| identity | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-grounding-agent/identity-assessment.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Active identity, parent, predecessor, local PMF/relations and official canonical taxon identity. |
| node-edges | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-grounding-agent/node-edge-ledger.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Every current node and edge, with firm RO2212 process/process mismatch at edge 3 only. |
| owners | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-grounding-agent/owner-provenance-assessment.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Exact writer roles, nonempty-ID guards, eight whole history readings and bounded current acceptance search. |
| expression | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-grounding-agent/expression-assessment.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Exact canonical name and official synonyms absent from retained 20-organism/28-dataset catalog; no substitute query. |
| authority-reuse | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-grounding-agent/authority-reuse-receipts.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Original catalog/runner acquisitions retained. |
| local-authority | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-grounding-agent/local-authority-excerpts.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Actual v3 PMF, v8 confers, v9 exports and maintained mappings. |
| pmf-row | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-grounding-agent/pmf-maintained-row.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Current STATE grounding row; no copied process-state defect. |
| taxonomy-reuse | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-grounding-agent/taxonomy-reuse-receipt.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Original taxonomy acquisition versus current copy/read chronology. |
| ground-reading | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-grounding-agent/actual-reading-scope.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Actual authority, history and post-supplement writer reading scope. |
| ground-manifest | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-grounding-agent/evidence-manifest.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Twenty-seven frozen grounding artifacts verified. |
| metpo-primary | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/repo/data/raw/metpo.owl; Actual current target, direct parent and explicit predecessor XML | supports | Active 1000460, direct parent 1000332 and obsolete 0000182 replacement are supported. Numeric 4–6 bounds and related alias are retained; imported broad exact aliases require separate scientific scope assessment. |
| ro-primary | /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/ro.db; Actual RO2212 to RO2211 process/process inheritance; RO2326 material/process inheritance | supports | Current edge 3 chemical and permeability-quality referents do not meet process/process semantics. Edge 7 material ATPase to homeostasis process fits RO2326. No detailed efficacy judgment or blanket protein/chemical rule is inferred. |
| taxon-primary | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-grounding-agent/taxa46632-920.xml; Official NCBITaxon:920 species and aliases only | supports | Acidithiobacillus ferrooxidans and its three retained historical synonyms are positive identity evidence. This does not establish the canonical 4–6 phenotype or substitute the accompanying unrelated taxon. |
| meta-krulwich | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-metadata.json; Actual indexed response at its original acquisition time | supports | Actual generic pH-homeostasis indexed abstract; source classification/body readings are separate. |
| meta-baker | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/baker-metadata.json; Actual indexed response at its original acquisition time | supports | Actual acidophile abstract classifies by optimum and supports homeostasis context; its exact PMF phrase is body-unverified. |
| meta-bioenergetics | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/bioenergetics-metadata.json; Actual indexed response at its original acquisition time | supports | Actual environmental acidophilic sulphate-reducer review identity and abstract. No pathway or application optimization is adopted. |
| meta-cfa | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/cfa-metadata.json; Actual indexed response at its original acquisition time | context_only | Actual title/status identifies a pathogenic Gram-negative acid-resistance review; detailed defense, fitness and efficacy are UNASSESSED_SCOPE. |
| meta-acid-genomes | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/acid-genomes-metadata.json; Actual indexed response at its original acquisition time | supports | Actual environmental acidophile review abstract; source-specific genomic context is separately bounded. |
| meta-homeostasis | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/homeostasis-metadata.json; Actual indexed response at its original acquisition time | context_only | Actual yeast engineered-pump study identity/status only. Experimental improvements and optimization efficacy are unassessed. |
| meta-canonical | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/canonical-metadata.json; Actual indexed response at its original acquisition time | context_only | Actual Europe PMC zero-hit response retained. DOI identity is resolved separately by Crossref; zero hit is not DOI nonexistence. |
| canonical-crossref | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/canonical-crossref.json; Crossref actual title, DOI, abstract, notice and publisher-link metadata | supports | The assigned DOI resolves to a LAB food-products review. Its inspected abstract does not establish the named Acidithiobacillus complete 4–6 interval. Full-body absence or false species physiology is not inferred. |
| body-krulwich | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml; Selected existing generic classification/context only | supports | Retained BioC classification 5466/45441 and generic PMF 2440 only; incidental pathogen passages excluded. |
| body-acid-genomes | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/acid-genomes.xml; Selected existing generic classification/context only | supports | Retained JATS body 2 classification and first sentence of body 36 for the existing pump phrase. Genomic presence in a named strain is not universal necessity or direct efficacy proof. |
| body-bioenergetics | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/bioenergetics.xml; Body paragraphs 21 and 25 | supports | Existing generic PMF/ATP and weak-acid statements only. Edge 2 note omits an intervening parenthetical without an ellipsis; meaning remains positive. |
| body-cfa | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/cfa.xml; Body paragraph 6; exact current quoted fragment only | context_only | Literal occurrence only. No detailed pathogenic acid-defense/fitness/AMR mechanism or efficacy assessment. |
| body-homeostasis | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/homeostasis.xml; Body paragraph 2; existing background sentence only | supports | Generic yeast proton-export background only, with explicit marked abridgment in the current note. Engineered-pump results, improved conditions and optimization efficacy are unassessed. |
| sources | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/source-assessment.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Seven assigned works and all current placements; final root controls dispositions. |
| source-ledger | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/source-ledger.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Six Europe PMC hits and canonical Crossref resolution with exact original acquisition times. |
| placements | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/placement-ledger.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | All eleven external placements, three structured ontology fields and five synonym provenance fields. |
| snippets | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/snippet-ledger.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Three schema snippets: two literal, one Baker body-unknown. |
| quoted-notes | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/quoted-note-ledger.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Six quoted-note fields separately checked: three literal, two marked abridgments, one unmarked omission. |
| node-sources | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/node-source-ledger.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | All thirteen node-source contexts. |
| edge-sources | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/edge-source-ledger.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | All eight edge-source contexts, with explicit excluded efficacy scope. |
| source-status | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/publication-status-ledger.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Bounded returned publication-notice fields at actual acquisition times. |
| source-reading | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/selected-primary-reading.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Only actual selected generic and literal readings; no whole-article or pathogen-efficacy claim. |
| source-access | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/access-limitations.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Baker and canonical full-body limits retained; zero index hit resolved without false absence. |
| source-reuse | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/reuse-and-copy-receipt.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Original body and fresh metadata acquisitions remain separate from copies. |
| bin-scope | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/classification-and-bin-assessment.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Broad category versus complete interval; per-source cutoffs retained. |
| canonical-scope | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/canonical-assessment.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Official species identity positive; assigned-source exact range support remains unknown. |
| native-checks | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/native-check-context.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Actual focused native passes and separate manual quoted-note accounting. |
| source-capture | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/supplemental-capture-verification.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Final 83 inputs and original 82 unchanged; no source interpretation of the added writer. |
| source-manifest | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/evidence-manifest.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Forty-three frozen source artifacts verified. |
| canonical-browser | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/canonical-browser-observation.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Bounded failed publisher browser attempt; no primary body hash. |
| canonical-pdf-access | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/canonical-publisher-pdf-access.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Actual retained HTTP403 response; failure does not establish paper-wide absence. |
| new-source-accesses | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/new-source-accesses.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Actual Crossref and three XML acquisitions. Prior bioenergetics copy was also available; fresh acquisition is not misrepresented as reuse. |
| root-reading-40 | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-root/history-event-summary-reading.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Only the bounded reading scope and actual chronology recorded here; no inferred full body, whole-history or excluded efficacy review. |
| root-reading-41 | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-root/owner-window-reading.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Only the bounded reading scope and actual chronology recorded here; no inferred full body, whole-history or excluded efficacy review. |
| root-reading-42 | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-root/primary-classification-quote-canonical-reading.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Only the bounded reading scope and actual chronology recorded here; no inferred full body, whole-history or excluded efficacy review. |
| root-reading-43 | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-root/primary-identity-formal-reading.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Only the bounded reading scope and actual chronology recorded here; no inferred full body, whole-history or excluded efficacy review. |
| root-reading-44 | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-root/root-metadata-reading.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Only the bounded reading scope and actual chronology recorded here; no inferred full body, whole-history or excluded efficacy review. |
| root-reading-46 | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-root/whole-target-preinspect-reading.json; Derived audit or actual reading/access receipt; primary bytes are separate | supports | Only the bounded reading scope and actual chronology recorded here; no inferred full body, whole-history or excluded efficacy review. |
| challenge | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-semantic-challenge-agent/semantic-severity-challenge.json; Final independent challenge | supports | Final recommendation and all bound evidence verified. |
| adjudication | /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-root-adjudication.json; Final root disposition | supports | Final root controls finding anchors, severity, grouping and limitations. |

## Limits And Additional Notes

- Detailed pathogen acid-defense, fitness, AMR and yeast perturbation/engineering/optimization efficacy remain UNASSESSED_SCOPE. No biological repair or improved experimental conditions are supplied.
- Assigned canonical DOI is a verified LAB review, with a retained Europe PMC zero hit and successful Crossref identity. Its inspected abstract does not establish the named species or complete 4–6 interval; publisher full body unavailable is not whole-paper absence or false growth. Follow-up support or qualification is needed, without a forced finding solely from access failure.
- Baker full body and its PMF schema snippet remain unknown. Generic homeostasis does not independently calibrate the exact complete bin.
- Per-source acidophile cutoffs and optimum-versus-range distinctions are preserved; inspected classification is not an exhaustive definition of every facultative/obligate term.
- PMF STATE, ATP-formation process, permeability/internal-pH QUALITY and the other material facets are coherent. Free-text relations acquire no invented imported domain constraints; RO2326 edge 7 and local confers/exports fit current referents.
- No mandatory accession, connector, additional pathway or canonical substitute follows from this NONMECHANISTIC graph or its five components.
- Three schema snippets and six quoted-note fields remain distinct. CFA exact fragment matching is documentary only; marked ellipses are separate from edge 2 unmarked omission.
- The original 82-input capture is unchanged. The exact historical enables-to-trait writer was added by separate successful 83-input capture and interpreted afterward; final review input is the supplement.
- Eight whole-history readings belong to grounding; root/source reading scopes are separately receipted. Generated report lead does not establish the exact version used for earlier enrichment.
- Source acquisitions, current copies and actual readings retain their own times. Prior bioenergetics copy was discovered, but a fresh body was also acquired and is accurately identified as such.
- Exact catalog nonmatch for the supplied canonical is bounded to retained catalog bytes, not all public expression data; no substitute or downstream efficacy query.
- Final root/challenge guards are pinned. This serializer remains unexecuted during preparation; root owns one serialization after independent static review, native validation, final artifact review and save.
- Source coverage: seven assigned works, eleven external placements, thirteen nodes/eight edges, one canonical, three snippet fields and six quoted-note fields.
- Preparation changes no scientific record, Git state, sweep state or native inventory.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T200401Z-ph-range-low
kind: record
repository: CultureBotAI/TraitMech
title: Whole-record review of low pH range
started_at: '2026-10-21T19:53:31.919704Z'
finished_at: '2026-10-21T20:04:01Z'
reviewer:
  identity: codex
  kind: agent
  independence: independent
  independence_basis: Separate source and grounding audits, independent challenge
    and bounded root primary readings. Generic environmental classification, chemistry,
    literal quotation and formal semantics only; detailed pathogen acid-defense, fitness,
    AMR and perturbation/optimization efficacy are UNASSESSED_SCOPE. No scientific
    input was edited.
  model: GPT-6 (Codex)
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'Final root adjudication: two major findings for exact category/bin equivalence
  and RO2212 endpoint semantics; two bounded minors for quote omission and human traceability.
  Generic context and canonical species identity remain positive; exact canonical
  range support remains unknown.'
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
  - path: data/traits/environment/ph_range_low.yaml
    sha256: 56a1489044011c883b75e007e5eb0d6a67984b791e77d8f02cf70c64e7fccff0
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
  - path: research/traits/environment/ph_range_low-deep-research-falcon.md
    sha256: a9d2d36a3b7e1cbe5d6cb6dab50577315df72fc835514366d60c0f087238ab13
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
- target_id: METPO:1000460
  path: data/traits/environment/ph_range_low.yaml
  label: pH range low
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_range_low.yaml
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
  selection: Fifth record of the actual batch 011 queue. Whole target read before
    the original successful 82-input capture; source judgments followed hash verification.
    A newly discovered exact historical writer was added by a separate successful
    83-input capture before its substantive reading. Original 82 bytes and receipts
    are retained unchanged; the final review uses 83 inputs.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - METPO:1000460
checks:
- check_id: audit-graphs
  name: Full-corpus graph audit
  status: passed
  required: true
  target_ids:
  - METPO:1000460
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
  - METPO:1000460
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
  - METPO:1000460
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
  - METPO:1000460
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
  - METPO:1000460
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
  - METPO:1000460
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
  - METPO:1000460
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
- check_id: ph-range-low-native
  name: Focused native validation
  status: passed
  required: true
  target_ids:
  - METPO:1000460
  command: just validate data/traits/environment/ph_range_low.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Successful focused schema validation; formal scientific roles remain separately
    assessed.
  evidence_ids:
  - check-ph-range-low-native
- check_id: ph-range-low-strict
  name: Focused strict validation
  status: passed
  required: true
  target_ids:
  - METPO:1000460
  command: just validate-strict data/traits/environment/ph_range_low.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Successful focused strict validation; no detailed biological efficacy certification.
  evidence_ids:
  - check-ph-range-low-strict
- check_id: ph-range-low-snippets
  name: Focused snippet verification
  status: passed
  required: true
  target_ids:
  - METPO:1000460
  command: just verify-snippets --record data/traits/environment/ph_range_low.yaml
    --out /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-snippets.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 'Three schema snippet fields: two VERIFIED and one NOT_IN_ABSTRACT. Six
    quoted note fields are separately assessed: three literal, two marked abridgments,
    one unmarked omission with positive meaning. Native results are preserved.'
  evidence_ids:
  - check-ph-range-low-snippets
- check_id: batch010-qc
  name: Reused maintained batch-ten QC
  status: passed
  required: true
  target_ids:
  - METPO:1000460
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
  - METPO:1000460
  summary: One reviewed label-only contextual protein class and zero instances; no
    token accession required.
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
- evidence_id: check-ph-range-low-native
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-native.log
  locator: Executed 2026-10-21T19:53:47.173588+00:00 through 2026-10-21T19:53:47.774084+00:00;
    metadata ph-range-low-native.json
  accessed_at: '2026-10-21T19:53:47.774084Z'
  support: context_only
  summary: Successful focused schema validation; formal scientific roles remain separately
    assessed.
  snapshot_sha256: 578ba823ca86e574dd56014f35ac15da76edada110bd3a2731d3b5abebb0924a
- evidence_id: check-ph-range-low-strict
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-strict.log
  locator: Executed 2026-10-21T19:53:47.173589+00:00 through 2026-10-21T19:53:48.176273+00:00;
    metadata ph-range-low-strict.json
  accessed_at: '2026-10-21T19:53:48.176273Z'
  support: context_only
  summary: Successful focused strict validation; no detailed biological efficacy certification.
  snapshot_sha256: 135e40e170569aa66aa518d9a44faa04f8d369e0101e940f43b062b36eb97dbb
- evidence_id: check-ph-range-low-snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-snippets.log
  locator: Executed 2026-10-21T19:53:49.439585+00:00 through 2026-10-21T19:53:53.132889+00:00;
    metadata ph-range-low-snippets.json
  accessed_at: '2026-10-21T19:53:53.132889Z'
  support: context_only
  summary: 'Three schema snippet fields: two VERIFIED and one NOT_IN_ABSTRACT. Six
    quoted note fields are separately assessed: three literal, two marked abridgments,
    one unmarked omission with positive meaning. Native results are preserved.'
  snapshot_sha256: e799e978b617d8a6a9f928ae3819ee3db7dcbfb6c4c1dac562576d80c2c0017e
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
  reference: data/traits/environment/ph_range_low.yaml
  locator: Entire current record
  accessed_at: '2026-10-21T19:55:40.723324Z'
  support: supports
  summary: All thirteen nodes, eight edges, three schema snippets, six quote-bearing
    notes, one canonical and twelve record events are covered.
  snapshot_sha256: 56a1489044011c883b75e007e5eb0d6a67984b791e77d8f02cf70c64e7fccff0
- evidence_id: policy
  kind: authority
  reference: docs/GROUNDING_POLICY.md
  locator: Captured maintained authority
  accessed_at: '2026-10-21T19:57:19.764268Z'
  support: supports
  summary: Reviewed label-only protein classes and optional instances; declared material/activity
    referents remain distinct.
  snapshot_sha256: 891678c983c2283a47c81c47950b35753981e9339d105f3bbdda92a1f5ab7f42
- evidence_id: playbook
  kind: authority
  reference: docs/CURATION_PLAYBOOK.md
  locator: Captured maintained authority
  accessed_at: '2026-10-21T19:57:19.764268Z'
  support: supports
  summary: Exact attribution, quotation precision, source scope and attributable current
    acceptance.
  snapshot_sha256: 735e9b810471da9f7d8364e35ffe1e741edb3421480dac01727db6ea5aa65da9
- evidence_id: schema
  kind: authority
  reference: src/traitmech/schema/traitmech.yaml
  locator: Captured maintained authority
  accessed_at: '2026-10-21T19:57:19.764268Z'
  support: supports
  summary: Actual process, state, chemical, quality and trait facets.
  snapshot_sha256: 46c47fc627b80ccbba1e8ab3fb6f2aee93bc2aef7aaf72fe9aadc3257f2c02dd
- evidence_id: checklist
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Captured maintained authority
  accessed_at: '2026-10-21T19:57:19.764268Z'
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
  summary: Original diagnostic outcomes and current byte comparisons remain bound.
  snapshot_sha256: a728777b9987b1283d7d1382168af40739074fce5c05f9a3bd93d3738f56880f
- evidence_id: reuse-postcheck
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/common-reuse-output-verification-agent/post-execution-verification.json
  locator: Actual independent qualifier postcheck
  accessed_at: '2026-10-21T19:08:41.804361Z'
  support: supports
  summary: Byte and native-output bindings independently verified without new QC.
  snapshot_sha256: a3a6f33363e71b00e8db09cbc318cae0027844aba584f7b4cafb282d11ab027a
- evidence_id: initial-capture
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low.inspect.json
  locator: Original 82-input native capture
  accessed_at: '2026-10-21T19:53:32.672803Z'
  support: supports
  summary: Retained original successful capture; all 82 inputs are unchanged in the
    final supplement.
  snapshot_sha256: 9167d1a71c2860bbda72a5cd48a875f18d0d10c4d2c8877db4fd2a5d24e9c28a
- evidence_id: supplement-command
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low.inspect-supplemented-command.json
  locator: Actual separate native supplement execution
  accessed_at: '2026-10-21T19:55:40.723324Z'
  support: supports
  summary: The newly discovered exact historical writer was captured before interpretation;
    no original capture was overwritten.
  snapshot_sha256: 114a377635f539f2282a56d686a8d630ef6948bcc5d5e8ff31bd96057b8702de
- evidence_id: capture
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-grounding-agent/capture-supplement-verification.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:56:08.692259Z'
  support: supports
  summary: Final 83-input capture verified against unchanged original 82.
  snapshot_sha256: 8f0f152275089fd1658c89af99c883144a11f325acfbd0076b910f4d650702a7
- evidence_id: identity
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-grounding-agent/identity-assessment.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:57:19.764268Z'
  support: supports
  summary: Active identity, parent, predecessor, local PMF/relations and official
    canonical taxon identity.
  snapshot_sha256: 61ca692767cc12b328fb1479426f267d3b75ce12fcd1f176e0062224622b87e2
- evidence_id: node-edges
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-grounding-agent/node-edge-ledger.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:57:19.764268Z'
  support: supports
  summary: Every current node and edge, with firm RO2212 process/process mismatch
    at edge 3 only.
  snapshot_sha256: 6e88f716e74317f66b2ce839a662e3772197bacd430f97045bfb1f33b198284f
- evidence_id: owners
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-grounding-agent/owner-provenance-assessment.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:57:19.764268Z'
  support: supports
  summary: Exact writer roles, nonempty-ID guards, eight whole history readings and
    bounded current acceptance search.
  snapshot_sha256: 1e7fd94dbfaf547d67ad1d20359746bb2d003da9d6dc003fc8692606b0805561
- evidence_id: expression
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-grounding-agent/expression-assessment.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:57:19.764268Z'
  support: supports
  summary: Exact canonical name and official synonyms absent from retained 20-organism/28-dataset
    catalog; no substitute query.
  snapshot_sha256: 24729b269b5ec65485515c6f1e9dd3c5a5548985c53b944ad999e67bc97a86b3
- evidence_id: authority-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-grounding-agent/authority-reuse-receipts.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:54:15.801994Z'
  support: supports
  summary: Original catalog/runner acquisitions retained.
  snapshot_sha256: 1c3e8defed3d0702043cdfe35c369b515fd7b1924f42766aff42967c8abd0742
- evidence_id: local-authority
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-grounding-agent/local-authority-excerpts.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:54:15.751948Z'
  support: supports
  summary: Actual v3 PMF, v8 confers, v9 exports and maintained mappings.
  snapshot_sha256: a08d13d19f9c3b151567ca74f0e76ba8e076f41be81094ffbe3e21b7772b0be3
- evidence_id: pmf-row
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-grounding-agent/pmf-maintained-row.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:55:46.535066Z'
  support: supports
  summary: Current STATE grounding row; no copied process-state defect.
  snapshot_sha256: 7ff7493fccd460610bffe0f1081ad59c96ce0a984e17b6fe71bbb89eb648923a
- evidence_id: taxonomy-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-grounding-agent/taxonomy-reuse-receipt.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:54:22.212048Z'
  support: supports
  summary: Original taxonomy acquisition versus current copy/read chronology.
  snapshot_sha256: 481f5bade72546448790a146b147776806a51b443d568620a97ec6095289ba25
- evidence_id: ground-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-grounding-agent/actual-reading-scope.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:57:19.764268Z'
  support: supports
  summary: Actual authority, history and post-supplement writer reading scope.
  snapshot_sha256: 36262f91c7e9a313631942f1e0b61322450ebf308abe37dcc6b21a1c857e8224
- evidence_id: ground-manifest
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-grounding-agent/evidence-manifest.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:57:19.764268Z'
  support: supports
  summary: Twenty-seven frozen grounding artifacts verified.
  snapshot_sha256: 3457e9e4482c77bb2a5b0122e5cf042420a2f295eae802a1db3b154d70aca3f0
- evidence_id: metpo-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/repo/data/raw/metpo.owl
  locator: Actual current target, direct parent and explicit predecessor XML
  accessed_at: '2026-10-21T19:54:15.730585Z'
  support: supports
  summary: Active 1000460, direct parent 1000332 and obsolete 0000182 replacement
    are supported. Numeric 4–6 bounds and related alias are retained; imported broad
    exact aliases require separate scientific scope assessment.
  snapshot_sha256: 8b6f8fe0510a698579e532658c8ace05da2550093365df9ca83feb0741778415
- evidence_id: ro-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep.FU79Gr/pystow/oaklib/ro.db
  locator: Actual RO2212 to RO2211 process/process inheritance; RO2326 material/process
    inheritance
  accessed_at: '2026-10-21T19:54:15.742415Z'
  support: supports
  summary: Current edge 3 chemical and permeability-quality referents do not meet
    process/process semantics. Edge 7 material ATPase to homeostasis process fits
    RO2326. No detailed efficacy judgment or blanket protein/chemical rule is inferred.
  snapshot_sha256: 849e616c29fecd0d4a6c6dee0dc0f6f117ace7167dbfa1e0f043dc84868f83cb
- evidence_id: taxon-primary
  kind: authority
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-grounding-agent/taxa46632-920.xml
  locator: Official NCBITaxon:920 species and aliases only
  accessed_at: '2026-10-21T15:29:57.491983Z'
  support: supports
  summary: Acidithiobacillus ferrooxidans and its three retained historical synonyms
    are positive identity evidence. This does not establish the canonical 4–6 phenotype
    or substitute the accompanying unrelated taxon.
  snapshot_sha256: 1be9370b5b6116c77b07fe85c0d6979c812db23c2d00ff03d9369431d0ae844b
- evidence_id: meta-krulwich
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-metadata.json
  locator: Actual indexed response at its original acquisition time
  accessed_at: '2026-10-21T19:53:12.743016Z'
  support: supports
  summary: Actual generic pH-homeostasis indexed abstract; source classification/body
    readings are separate.
  snapshot_sha256: 036607538c4110a45aeab78f8cad03b240ab3648075984f6f3e870b03692e3fd
- evidence_id: meta-baker
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/baker-metadata.json
  locator: Actual indexed response at its original acquisition time
  accessed_at: '2026-10-21T19:53:12.798714Z'
  support: supports
  summary: Actual acidophile abstract classifies by optimum and supports homeostasis
    context; its exact PMF phrase is body-unverified.
  snapshot_sha256: a78777bc3bb6444b32e2e8a13ab72c56d80592b97e30c9b5520c67cc040c631b
- evidence_id: meta-bioenergetics
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/bioenergetics-metadata.json
  locator: Actual indexed response at its original acquisition time
  accessed_at: '2026-10-21T19:53:12.827502Z'
  support: supports
  summary: Actual environmental acidophilic sulphate-reducer review identity and abstract.
    No pathway or application optimization is adopted.
  snapshot_sha256: 7df1c41cc39187de12c7860968f74aeeedb0f5b1b9d483109a3b24497795ee34
- evidence_id: meta-cfa
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/cfa-metadata.json
  locator: Actual indexed response at its original acquisition time
  accessed_at: '2026-10-21T19:53:12.798808Z'
  support: context_only
  summary: Actual title/status identifies a pathogenic Gram-negative acid-resistance
    review; detailed defense, fitness and efficacy are UNASSESSED_SCOPE.
  snapshot_sha256: ccdbce1f68320dfd48c35b37f09beb47b6b3c321e15a265eff5e4a4e6e09410d
- evidence_id: meta-acid-genomes
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/acid-genomes-metadata.json
  locator: Actual indexed response at its original acquisition time
  accessed_at: '2026-10-21T19:53:12.768907Z'
  support: supports
  summary: Actual environmental acidophile review abstract; source-specific genomic
    context is separately bounded.
  snapshot_sha256: 50b00c6b5f093fad2f0c4efbaa6d95461f39655747939cef8b3f629a32b64e54
- evidence_id: meta-homeostasis
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/homeostasis-metadata.json
  locator: Actual indexed response at its original acquisition time
  accessed_at: '2026-10-21T19:53:13.654031Z'
  support: context_only
  summary: Actual yeast engineered-pump study identity/status only. Experimental improvements
    and optimization efficacy are unassessed.
  snapshot_sha256: ea06b51e2313dfe2a2654012428b39fad51baf0fde5259bde4aa243d97335c42
- evidence_id: meta-canonical
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/canonical-metadata.json
  locator: Actual indexed response at its original acquisition time
  accessed_at: '2026-10-21T19:53:13.533023Z'
  support: context_only
  summary: Actual Europe PMC zero-hit response retained. DOI identity is resolved
    separately by Crossref; zero hit is not DOI nonexistence.
  snapshot_sha256: 79bba614dec9fe2829936edc0bb6f9738a9766190872b44d6310a4e0e533275a
- evidence_id: canonical-crossref
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/canonical-crossref.json
  locator: Crossref actual title, DOI, abstract, notice and publisher-link metadata
  accessed_at: '2026-10-21T19:54:58.396626Z'
  support: supports
  summary: The assigned DOI resolves to a LAB food-products review. Its inspected
    abstract does not establish the named Acidithiobacillus complete 4–6 interval.
    Full-body absence or false species physiology is not inferred.
  snapshot_sha256: 8a989cead3090bece254aa0c5d41951d78e8f5f94998544671cefe11fe29476c
- evidence_id: body-krulwich
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml
  locator: Selected existing generic classification/context only
  accessed_at: '2026-10-21T07:57:33Z'
  support: supports
  summary: Retained BioC classification 5466/45441 and generic PMF 2440 only; incidental
    pathogen passages excluded.
  snapshot_sha256: 903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f
- evidence_id: body-acid-genomes
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/acid-genomes.xml
  locator: Selected existing generic classification/context only
  accessed_at: '2026-10-21T18:46:08.093450Z'
  support: supports
  summary: Retained JATS body 2 classification and first sentence of body 36 for the
    existing pump phrase. Genomic presence in a named strain is not universal necessity
    or direct efficacy proof.
  snapshot_sha256: 6f9494d7379f7f7914200f9ba87905a42e803d6173cd22dd1fa837ccefc1f1e0
- evidence_id: body-bioenergetics
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/bioenergetics.xml
  locator: Body paragraphs 21 and 25
  accessed_at: '2026-10-21T19:54:59.528514Z'
  support: supports
  summary: Existing generic PMF/ATP and weak-acid statements only. Edge 2 note omits
    an intervening parenthetical without an ellipsis; meaning remains positive.
  snapshot_sha256: 481a4f647bc7a835d74f7ec75d5f5ee8fa54ac76294f3c721a6711fd941ec58e
- evidence_id: body-cfa
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/cfa.xml
  locator: Body paragraph 6; exact current quoted fragment only
  accessed_at: '2026-10-21T19:54:59.628079Z'
  support: context_only
  summary: Literal occurrence only. No detailed pathogenic acid-defense/fitness/AMR
    mechanism or efficacy assessment.
  snapshot_sha256: f37423cf43c8cc6b8d9d64feacad8ec0407e625fce4293e3fab20fac5d1e8acb
- evidence_id: body-homeostasis
  kind: primary_source
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/homeostasis.xml
  locator: Body paragraph 2; existing background sentence only
  accessed_at: '2026-10-21T19:54:59.750904Z'
  support: supports
  summary: Generic yeast proton-export background only, with explicit marked abridgment
    in the current note. Engineered-pump results, improved conditions and optimization
    efficacy are unassessed.
  snapshot_sha256: b5f6a85c09e160674f98031032880e7b52f8e22a465d2678ff48f94dcc95fd94
- evidence_id: sources
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/source-assessment.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:58:41.408981Z'
  support: supports
  summary: Seven assigned works and all current placements; final root controls dispositions.
  snapshot_sha256: 940779ceef9b2df68f24270085a6c82aacfba6343e9819d8e5abac3c9774796a
- evidence_id: source-ledger
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/source-ledger.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:58:41.383624Z'
  support: supports
  summary: Six Europe PMC hits and canonical Crossref resolution with exact original
    acquisition times.
  snapshot_sha256: cf925e59706219ff8dba3ab0618d97f2873cb0e26df3480adeea5ddb3c130bcd
- evidence_id: placements
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/placement-ledger.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:58:41.401477Z'
  support: supports
  summary: All eleven external placements, three structured ontology fields and five
    synonym provenance fields.
  snapshot_sha256: 8ce1a5ed05fe4ca436ac15a2882f95497c6e2c8ab9599fae641b46ce3674a54e
- evidence_id: snippets
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/snippet-ledger.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:58:41.405228Z'
  support: supports
  summary: 'Three schema snippets: two literal, one Baker body-unknown.'
  snapshot_sha256: a90ccb065dcecd02a3ec541c903866bad6283437369a47f9123fd1029dce8e08
- evidence_id: quoted-notes
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/quoted-note-ledger.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:58:41.406306Z'
  support: supports
  summary: 'Six quoted-note fields separately checked: three literal, two marked abridgments,
    one unmarked omission.'
  snapshot_sha256: daf395274d3ad1ee6435cb3e613a0fffae7abf924df24997f4c1e5c5eb63980e
- evidence_id: node-sources
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/node-source-ledger.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:58:41.401839Z'
  support: supports
  summary: All thirteen node-source contexts.
  snapshot_sha256: 5ea4410b900cf44ca2e5098e8e5c45db73dc5ddfa662d2fa81cae281c4e4b3c1
- evidence_id: edge-sources
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/edge-source-ledger.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:58:41.401685Z'
  support: supports
  summary: All eight edge-source contexts, with explicit excluded efficacy scope.
  snapshot_sha256: 113ebb96103870f57e6f4240fcc6ec575c676d49e61569a432e5626e529d3fe5
- evidence_id: source-status
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/publication-status-ledger.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:58:41.383940Z'
  support: supports
  summary: Bounded returned publication-notice fields at actual acquisition times.
  snapshot_sha256: f5a3323b39ca7ca3a8116e0f75b9a8f84a700be289f6fb9f8ce80b6406054799
- evidence_id: source-reading
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/selected-primary-reading.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:58:41.406907Z'
  support: supports
  summary: Only actual selected generic and literal readings; no whole-article or
    pathogen-efficacy claim.
  snapshot_sha256: a2de279dcbc4522fbf708265ea0da1defca8164422019fa857168c58cca01687
- evidence_id: source-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/access-limitations.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:58:41.407500Z'
  support: supports
  summary: Baker and canonical full-body limits retained; zero index hit resolved
    without false absence.
  snapshot_sha256: 4b7693b499cf92295881ff9f813f413991a3bd794bb07ec4018bab75b75c918b
- evidence_id: source-reuse
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/reuse-and-copy-receipt.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:55:07.225105Z'
  support: supports
  summary: Original body and fresh metadata acquisitions remain separate from copies.
  snapshot_sha256: 701e9af4a8258737169610f78cf1b075eb319156f5389c4e9cf07bedcc6ecb7e
- evidence_id: bin-scope
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/classification-and-bin-assessment.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:58:41.406434Z'
  support: supports
  summary: Broad category versus complete interval; per-source cutoffs retained.
  snapshot_sha256: 5dd1fc12560f82dd39b0af33733f690e1b635b271b70db4e3d8bfd386b542722
- evidence_id: canonical-scope
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/canonical-assessment.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:58:41.406748Z'
  support: supports
  summary: Official species identity positive; assigned-source exact range support
    remains unknown.
  snapshot_sha256: 81cd59c9a04caf39f9aac1b557e0174506eea654e1f38fdd889a5727b04ada83
- evidence_id: native-checks
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/native-check-context.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:58:41.408696Z'
  support: supports
  summary: Actual focused native passes and separate manual quoted-note accounting.
  snapshot_sha256: 43eb2da37db38dd883984f4ca5031074538803dbab7d245b156a0179420761ae
- evidence_id: source-capture
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/supplemental-capture-verification.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:58:41.305392Z'
  support: supports
  summary: Final 83 inputs and original 82 unchanged; no source interpretation of
    the added writer.
  snapshot_sha256: 8485f2126d83ea0d1dd797bb6e381642bd73a5c2adcaf378e9727da4d5898336
- evidence_id: source-manifest
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/evidence-manifest.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:58:41.415145Z'
  support: supports
  summary: Forty-three frozen source artifacts verified.
  snapshot_sha256: 714b2e03ca1f5ac3430bdd36572e2deed19903074f86322bde6e6c796651406f
- evidence_id: canonical-browser
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/canonical-browser-observation.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:55:07.225399Z'
  support: supports
  summary: Bounded failed publisher browser attempt; no primary body hash.
  snapshot_sha256: 611ea709e30d4e9e993adf6c35fc9beeec515800249017f9465922f982d77f34
- evidence_id: canonical-pdf-access
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/canonical-publisher-pdf-access.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:55:58.698637Z'
  support: supports
  summary: Actual retained HTTP403 response; failure does not establish paper-wide
    absence.
  snapshot_sha256: 7e4d4675f93cc95659df9fd91a54929491f7e390db6ad838876988549df7c08a
- evidence_id: new-source-accesses
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/new-source-accesses.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:54:59.751377Z'
  support: supports
  summary: Actual Crossref and three XML acquisitions. Prior bioenergetics copy was
    also available; fresh acquisition is not misrepresented as reuse.
  snapshot_sha256: 5a481078625f7e2427f75a6e5ff09550cf598de5c2d5b4d50c498e5987c47f03
- evidence_id: root-reading-40
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-root/history-event-summary-reading.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:59:45.451850Z'
  support: supports
  summary: Only the bounded reading scope and actual chronology recorded here; no
    inferred full body, whole-history or excluded efficacy review.
  snapshot_sha256: cb5ad6021883fd803e3bf3b6a418fbb081eedfc551416b4e9b5f2e0e794e4627
- evidence_id: root-reading-41
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-root/owner-window-reading.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:59:56.120580Z'
  support: supports
  summary: Only the bounded reading scope and actual chronology recorded here; no
    inferred full body, whole-history or excluded efficacy review.
  snapshot_sha256: 8810271b3a77a531cd865d8e46f9a9b185ce2cf799144bbca7f2f14c8e549906
- evidence_id: root-reading-42
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-root/primary-classification-quote-canonical-reading.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:59:25.442896Z'
  support: supports
  summary: Only the bounded reading scope and actual chronology recorded here; no
    inferred full body, whole-history or excluded efficacy review.
  snapshot_sha256: 17bbb19d8226eafd0bd7b05dd1cf1f49b5883692fd9949fbcfd2a6a5ff3841fa
- evidence_id: root-reading-43
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-root/primary-identity-formal-reading.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:55:04.981204Z'
  support: supports
  summary: Only the bounded reading scope and actual chronology recorded here; no
    inferred full body, whole-history or excluded efficacy review.
  snapshot_sha256: 994ec325d3b550e71143f8fc513a29794728d391a7bfe2fb78e7817d538f6934
- evidence_id: root-reading-44
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-root/root-metadata-reading.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:54:47.258336Z'
  support: supports
  summary: Only the bounded reading scope and actual chronology recorded here; no
    inferred full body, whole-history or excluded efficacy review.
  snapshot_sha256: 5a5e8e38e978cb773ea12a1e19b4fa437731415c1c720a10fba0c06defed9c08
- evidence_id: root-reading-46
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-root/whole-target-preinspect-reading.json
  locator: Derived audit or actual reading/access receipt; primary bytes are separate
  accessed_at: '2026-10-21T19:52:48.968129Z'
  support: supports
  summary: Only the bounded reading scope and actual chronology recorded here; no
    inferred full body, whole-history or excluded efficacy review.
  snapshot_sha256: 9cd193758dd4146560fa8422c1259d7eb596100c28203a5c0df6d001718bcc4d
- evidence_id: challenge
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-semantic-challenge-agent/semantic-severity-challenge.json
  locator: Final independent challenge
  accessed_at: '2026-10-21T20:01:01.384369Z'
  support: supports
  summary: Final recommendation and all bound evidence verified.
  snapshot_sha256: cd1fbb82fed74db217ea2a101282674c3b880df44d61ce2a24c36ecf1117d6f8
- evidence_id: adjudication
  kind: validation
  reference: /private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-root-adjudication.json
  locator: Final root disposition
  accessed_at: '2026-10-21T20:01:24.317103Z'
  support: supports
  summary: Final root controls finding anchors, severity, grouping and limitations.
  snapshot_sha256: 9172e4ccd5f422906a370a353833d6da826940d11b0ede19e6896ee9468d137d
assessments:
- assessment_id: identity
  area: identity
  topic: 'Native checklist: active identity and scientific exactness'
  outcome: concern
  target_ids:
  - METPO:1000460
  summary: Active METPO identity, direct parent, obsolete replacement, numerical 4–6
    bounds and related alias are supported. The four faithfully imported broad acidophile/tolerance
    aliases do not establish exact equivalence to this complete interval. Preserve
    source-specific cutoffs rather than inventing exhaustive facultative/obligate
    definitions.
  evidence_ids:
  - identity
  - metpo-primary
  - bin-scope
  - record
- assessment_id: definition
  area: evidence
  topic: 'Native checklist: quantitative range and contextual sources'
  outcome: unknown
  target_ids:
  - METPO:1000460
  summary: Generic homeostasis and acidic-growth sources provide context, but do not
    independently calibrate an exact complete 4–6 interval. Published optimum categories
    and whole growth ranges differ. Retain the numerical bin and do not multiply this
    limitation into additional source or mechanism findings.
  evidence_ids:
  - bin-scope
  - body-acid-genomes
  - body-krulwich
  - meta-baker
  - record
- assessment_id: scope
  area: scope
  topic: 'Native checklist: environmental numerical phenotype'
  outcome: supported
  target_ids:
  - METPO:1000460
  summary: ENVIRONMENT, CLASS and NONMECHANISTIC are coherent for this quantitative
    trait. Generic environmental physiology does not certify a universal mechanism,
    exact interval sufficiency or detailed defense efficacy.
  evidence_ids:
  - record
  - policy
  - checklist
- assessment_id: canonical
  area: evidence
  topic: 'Native checklist: species identity versus assigned phenotype support'
  outcome: unknown
  target_ids:
  - METPO:1000460
  summary: Official NCBI 920 species identity is positive, but the assigned DOI resolves
    to a LAB review and its inspected abstract does not establish Acidithiobacillus
    ferrooxidans or a complete 4–6 growth interval. Publisher full body remains unavailable.
    Follow up by documenting an actually inspected species/strain interval source
    or qualifying the canonical claim in separately authorized curation; no forced
    finding, replacement organism or false-range claim follows from access failure.
  evidence_ids:
  - canonical-scope
  - canonical-crossref
  - taxon-primary
  - source-access
  details: "{\n  \"completed_at\": \"2026-10-21T19:58:41.406748+00:00\",\n  \"example\"\
    : {\n    \"taxon_id\": \"NCBITaxon:920\",\n    \"taxon_label\": \"Acidithiobacillus\
    \ ferrooxidans\",\n    \"reference\": \"DOI:10.3390/fermentation10060298\",\n\
    \    \"note\": \"Acidophile growing in the low-pH range this record bounds, cited\
    \ in its artifact for acidophile physiology.\"\n  },\n  \"candidate\": {\n   \
    \ \"key\": \"canonical-source-placement-gap\",\n    \"severity\": \"undetermined\"\
    ,\n    \"field_paths\": [\n      \"canonical_examples[0]\"\n    ],\n    \"assessment\"\
    : \"Species identity is supported by official NCBI response. The assigned DOI\
    \ resolves to a LAB food-products review whose inspected abstract does not establish\
    \ A. ferrooxidans or its complete4\\u20136 growth interval. Publisher body access\
    \ remains unavailable; this is an explicit source/placement verification gap pending\
    \ final root judgment.\",\n    \"qualification\": \"Do not infer paper-wide organism\
    \ absence from title/abstract, a false physiological range from access failure,\
    \ or substitute an unassigned organism/source. Europe PMC zero hit is resolved\
    \ bibliographically by Crossref, not treated as nonexistent DOI.\"\n  },\n  \"\
    crossref\": {\n    \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/canonical-crossref.json\"\
    ,\n    \"sha256\": \"8a989cead3090bece254aa0c5d41951d78e8f5f94998544671cefe11fe29476c\"\
    ,\n    \"bytes\": 37483\n  },\n  \"europepmc_zero_hit\": {\n    \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/canonical-metadata.json\"\
    ,\n    \"sha256\": \"79bba614dec9fe2829936edc0bb6f9738a9766190872b44d6310a4e0e533275a\"\
    ,\n    \"bytes\": 195\n  },\n  \"primary_taxonomy\": {\n    \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-grounding-agent/taxa46632-920.xml\"\
    ,\n    \"sha256\": \"1be9370b5b6116c77b07fe85c0d6979c812db23c2d00ff03d9369431d0ae844b\"\
    ,\n    \"scope\": \"Species identity only; actual acquisition/reuse receipt owned\
    \ by grounding auditor.\"\n  },\n  \"body_limit\": \"MDPI browser429, PDF inaccessible\
    \ and directPDF403 retained. Search-generated publisher text is a lead/selected\
    \ scope observation, not retained full body or a complete absence proof.\"\n}"
- assessment_id: bibliography
  area: evidence
  topic: 'Native checklist: all seven works and eleven placements'
  outcome: supported
  target_ids:
  - METPO:1000460
  summary: 'Every assigned DOI is resolved: six indexed hits and a canonical zero
    hit resolved through Crossref. Actual source types and scopes are preserved. CFA
    is documentary-only; yeast study identity and its existing generic background
    are distinct from excluded perturbation results.'
  evidence_ids:
  - source-ledger
  - placements
  - source-status
  - source-access
  details: "{\n  \"completed_at\": \"2026-10-21T19:58:41.401477+00:00\",\n  \"external_placements\"\
    : [\n    {\n      \"field_path\": \"definition_source\",\n      \"reference\"\
    : \"DOI:10.1038/nrmicro2549\",\n      \"claim\": \"A pH range phenotype in which\
    \ the growth-supporting external pH range spans approximately 4\\u20136, characteristic\
    \ of acidophilic physiology.\",\n      \"assessment\": \"Current review supports\
    \ acidic-growth/homeostasis context, not exact equivalence between all acidophile\
    \ categories and a complete4\\u20136 interval.\"\n    },\n    {\n      \"field_path\"\
    : \"evidence[0]\",\n      \"reference\": \"DOI:10.1038/nrmicro2549\",\n      \"\
    snippet\": \"cytoplasmic pH\",\n      \"notes\": \"pH-homeostasis review supports\
    \ moderately acidic pH-homeostasis as the basis of growth in the pH 4\\u20136\
    \ range.\",\n      \"assessment\": \"Literal cytoplasmic-pH occurrence positive;\
    \ generic homeostasis is distinct from exact complete-bin calibration.\"\n   \
    \ },\n    {\n      \"field_path\": \"causal_graphs[0].edges[0].evidence[0]\",\n\
    \      \"reference\": \"DOI:10.1038/nrmicro2549\",\n      \"snippet\": \"cytoplasmic\
    \ pH\",\n      \"notes\": \"Supports acidophile cytoplasmic pH homeostasis as\
    \ the moderately-acidic growth-range mechanism.\",\n      \"assessment\": \"Actual\
    \ generic homeostasis context is positive, but acidophile categories and physiological\
    \ mechanisms do not establish an exact complete4\\u20136 interval. Group scope\
    \ with category/bin assessment; no biological falsity or universal mechanism is\
    \ inferred.\"\n    },\n    {\n      \"field_path\": \"causal_graphs[0].edges[1].evidence[0]\"\
    ,\n      \"reference\": \"DOI:10.1016/j.tim.2007.02.005\",\n      \"snippet\"\
    : \"proton motive force\",\n      \"notes\": \"Supports the pH 4\\u20136 range\
    \ as a value within the pH-range distribution.\",\n      \"assessment\": \"Ontology\
    \ supplies the parent/bin hierarchy. Baker abstract classifies acidophiles by\
    \ optimum below3 and supports generic homeostasis; it does not directly calibrate\
    \ a complete4\\u20136 interval. Assigned PMF body phrase remains unknown; lack\
    \ of abstract occurrence is not a false quotation.\"\n    },\n    {\n      \"\
    field_path\": \"causal_graphs[0].edges[2].evidence[0]\",\n      \"reference\"\
    : \"DOI:10.1111/1758-2229.70019\",\n      \"notes\": \"\\\"That proton potential\
    \ then drives the phosphorylation of ADP and the formation of ATP by the ATP synthase\\\
    \"; general bioenergetic edge relevant to low-pH growth.\",\n      \"assessment\"\
    : \"Existing generic PMF-to-ATP statement is supported at bioenergetics body21.\
    \ The quoted note removes an intervening parenthesis without an ellipsis; meaning\
    \ remains positive and no efficacy/intervention inference is made.\"\n    },\n\
    \    {\n      \"field_path\": \"causal_graphs[0].edges[3].evidence[0]\",\n   \
    \   \"reference\": \"DOI:10.4014/jmb.2303.03009\",\n      \"notes\": \"\\\"decreasing\
    \ membrane proton permeability prevents the accumulation of intracellular protons\\\
    \" after conversion to cyclopropane fatty acids; generalizable membrane adaptation.\"\
    ,\n      \"assessment\": \"Current quoted fragment is literally present in CFA\
    \ body6. Source title/abstract identify pathogenic Gram-negative acid-defense\
    \ scope. Only identity, quote occurrence and separately audited formal roles are\
    \ assessed; generalizable biological efficacy is UNASSESSED_SCOPE.\"\n    },\n\
    \    {\n      \"field_path\": \"causal_graphs[0].edges[4].evidence[0]\",\n   \
    \   \"reference\": \"DOI:10.1111/1758-2229.70019\",\n      \"notes\": \"\\\"organic\
    \ acids... occur in their undissociated form and can diffuse into the cell\\\"\
    ; boundary condition distinguishing low-pH growth from weak-acid inhibition.\"\
    ,\n      \"assessment\": \"Actual environmental review body25 supports the existing\
    \ generic weak-acid permeability context. Quoted note is a marked noncontiguous\
    \ abridgment with literal ordered fragments. It does not itself establish complete4\\\
    u20136 growth or a universal lineage response.\"\n    },\n    {\n      \"field_path\"\
    : \"causal_graphs[0].edges[5].evidence[0]\",\n      \"reference\": \"DOI:10.1111/1758-2229.70019\"\
    ,\n      \"notes\": \"\\\"the higher pH of the cytoplasm will lead to dissociation\
    \ of the acid, thus releasing protons and lowering the internal pH\\\"; strong\
    \ causal edge.\",\n      \"assessment\": \"Actual environmental review body25\
    \ contains the current quoted dissociation/pH sentence as a contiguous phrase.\
    \ Generic acid-base chemistry is positive; no new intervention conditions or acid-defense\
    \ efficacy assessment.\"\n    },\n    {\n      \"field_path\": \"causal_graphs[0].edges[6].evidence[0]\"\
    ,\n      \"reference\": \"DOI:10.3389/fmicb.2023.1149903\",\n      \"notes\":\
    \ \"Acidophile genomes encode \\\"a P-type ATPase proton efflux pump\\\"; active\
    \ ATP-driven proton export underlies cytoplasmic pH homeostasis.\",\n      \"\
    assessment\": \"Actual environmental review body36 contains the quoted P-type-pump\
    \ phrase in the named At. ferrivorans SS3 genome context, with absence in another\
    \ reported MAG. Existing contextual presence is positive; genomic annotation is\
    \ not direct functional validation or universal necessity.\"\n    },\n    {\n\
    \      \"field_path\": \"causal_graphs[0].edges[7].evidence[0]\",\n      \"reference\"\
    : \"DOI:10.3390/microorganisms12030625\",\n      \"notes\": \"\\\"acid stress\
    \ tolerance... facilitated by an active export of protons via the expenditure\
    \ of ATP... carried out by H+-ATPases\\\"; broad principle of homeostasis.\",\n\
    \      \"assessment\": \"Actual yeast article body2 gives the generic existing\
    \ proton-export background sentence. Note is marked abridgment; source context\
    \ is S. cerevisiae and background citations, not the new engineered-pump result.\
    \ No perturbation efficacy, optimization or exact4\\u20136 calibration is adopted.\"\
    \n    },\n    {\n      \"field_path\": \"canonical_examples[0]\",\n      \"reference\"\
    : \"DOI:10.3390/fermentation10060298\",\n      \"claim\": {\n        \"taxon_id\"\
    : \"NCBITaxon:920\",\n        \"taxon_label\": \"Acidithiobacillus ferrooxidans\"\
    ,\n        \"reference\": \"DOI:10.3390/fermentation10060298\",\n        \"note\"\
    : \"Acidophile growing in the low-pH range this record bounds, cited in its artifact\
    \ for acidophile physiology.\"\n      },\n      \"assessment\": \"Official species\
    \ identity positive; assigned DOI resolves to a LAB review. Inspected abstract\
    \ and bounded publisher access do not establish this species complete4\\u20136\
    \ interval. Preserve unresolved source/placement gap without declaring entire-paper\
    \ absence or false species biology.\"\n    }\n  ],\n  \"ontology_grounding_fields\"\
    : [\n    {\n      \"field_path\": \"causal_graphs[0].nodes[0].grounding\",\n \
    \     \"reference\": \"METPO:1000460\"\n    },\n    {\n      \"field_path\": \"\
    causal_graphs[0].nodes[1].grounding\",\n      \"reference\": \"METPO:1000332\"\
    \n    },\n    {\n      \"field_path\": \"causal_graphs[0].nodes[3].grounding\"\
    ,\n      \"reference\": \"METPO:1007500\"\n    }\n  ],\n  \"synonym_source_fields\"\
    : [\n    {\n      \"field_path\": \"synonyms[0]\",\n      \"synonym\": {\n   \
    \     \"synonym_text\": \"Acid Tolerant\",\n        \"synonym_type\": \"EXACT_SYNONYM\"\
    ,\n        \"source\": \"metpo.owl\"\n      }\n    },\n    {\n      \"field_path\"\
    : \"synonyms[1]\",\n      \"synonym\": {\n        \"synonym_text\": \"Acidophile\"\
    ,\n        \"synonym_type\": \"EXACT_SYNONYM\",\n        \"source\": \"metpo.owl\"\
    \n      }\n    },\n    {\n      \"field_path\": \"synonyms[2]\",\n      \"synonym\"\
    : {\n        \"synonym_text\": \"Facultative acidophile\",\n        \"synonym_type\"\
    : \"EXACT_SYNONYM\",\n        \"source\": \"metpo.owl\"\n      }\n    },\n   \
    \ {\n      \"field_path\": \"synonyms[3]\",\n      \"synonym\": {\n        \"\
    synonym_text\": \"Obligative acidophile\",\n        \"synonym_type\": \"EXACT_SYNONYM\"\
    ,\n        \"source\": \"metpo.owl\"\n      }\n    },\n    {\n      \"field_path\"\
    : \"synonyms[4]\",\n      \"synonym\": {\n        \"synonym_text\": \"pHR_4_to_6\"\
    ,\n        \"synonym_type\": \"RELATED_SYNONYM\",\n        \"source\": \"metpo.owl\"\
    \n      }\n    }\n  ],\n  \"scope\": \"All seven assigned works across eleven\
    \ external placements, including canonical and definition. Three structured ontology\
    \ fields are distinct from five synonym provenance fields.\"\n}"
- assessment_id: excerpts
  area: evidence
  topic: 'Native checklist: three snippets and six quoted notes'
  outcome: concern
  target_ids:
  - METPO:1000460
  summary: Two schema snippets are literal and the Baker PMF snippet remains body-unknown.
    Separately, three quoted-note fields are literal, two are explicitly marked abridgments,
    and edge 2 removes a parenthetical without an ellipsis while preserving supported
    meaning. Do not combine the note denominator with native three-snippet results.
  evidence_ids:
  - snippets
  - quoted-notes
  - source-reading
  - native-checks
  details: "{\n  \"snippets\": {\n    \"completed_at\": \"2026-10-21T19:58:41.405228+00:00\"\
    ,\n    \"snippets\": [\n      {\n        \"field_path\": \"evidence[0].snippet\"\
    ,\n        \"reference\": \"DOI:10.1038/nrmicro2549\",\n        \"snippet\": \"\
    cytoplasmic pH\",\n        \"outcome\": \"literal_exact\",\n        \"hits\":\
    \ [\n          {\n            \"surface\": \"indexed abstract\",\n           \
    \ \"file\": {\n              \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-metadata.json\"\
    ,\n              \"sha256\": \"036607538c4110a45aeab78f8cad03b240ab3648075984f6f3e870b03692e3fd\"\
    ,\n              \"bytes\": 4996\n            },\n            \"locator\": \"\
    abstractText\"\n          },\n          {\n            \"surface\": \"retained\
    \ BioC\",\n            \"file\": {\n              \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml\"\
    ,\n              \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n              \"bytes\": 174908\n            },\n            \"locator\": \"\
    passage offset 58\"\n          },\n          {\n            \"surface\": \"retained\
    \ BioC\",\n            \"file\": {\n              \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml\"\
    ,\n              \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n              \"bytes\": 174908\n            },\n            \"locator\": \"\
    passage offset 671\"\n          },\n          {\n            \"surface\": \"retained\
    \ BioC\",\n            \"file\": {\n              \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml\"\
    ,\n              \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n              \"bytes\": 174908\n            },\n            \"locator\": \"\
    passage offset 2440\"\n          },\n          {\n            \"surface\": \"\
    retained BioC\",\n            \"file\": {\n              \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml\"\
    ,\n              \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n              \"bytes\": 174908\n            },\n            \"locator\": \"\
    passage offset 3940\"\n          },\n          {\n            \"surface\": \"\
    retained BioC\",\n            \"file\": {\n              \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml\"\
    ,\n              \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n              \"bytes\": 174908\n            },\n            \"locator\": \"\
    passage offset 4950\"\n          },\n          {\n            \"surface\": \"\
    retained BioC\",\n            \"file\": {\n              \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml\"\
    ,\n              \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n              \"bytes\": 174908\n            },\n            \"locator\": \"\
    passage offset 7133\"\n          },\n          {\n            \"surface\": \"\
    retained BioC\",\n            \"file\": {\n              \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml\"\
    ,\n              \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n              \"bytes\": 174908\n            },\n            \"locator\": \"\
    passage offset 7180\"\n          },\n          {\n            \"surface\": \"\
    retained BioC\",\n            \"file\": {\n              \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml\"\
    ,\n              \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n              \"bytes\": 174908\n            },\n            \"locator\": \"\
    passage offset 7328\"\n          },\n          {\n            \"surface\": \"\
    retained BioC\",\n            \"file\": {\n              \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml\"\
    ,\n              \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n              \"bytes\": 174908\n            },\n            \"locator\": \"\
    passage offset 7370\"\n          },\n          {\n            \"surface\": \"\
    retained BioC\",\n            \"file\": {\n              \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml\"\
    ,\n              \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n              \"bytes\": 174908\n            },\n            \"locator\": \"\
    passage offset 8457\"\n          },\n          {\n            \"surface\": \"\
    retained BioC\",\n            \"file\": {\n              \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml\"\
    ,\n              \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n              \"bytes\": 174908\n            },\n            \"locator\": \"\
    passage offset 9102\"\n          },\n          {\n            \"surface\": \"\
    retained BioC\",\n            \"file\": {\n              \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml\"\
    ,\n              \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n              \"bytes\": 174908\n            },\n            \"locator\": \"\
    passage offset 17378\"\n          },\n          {\n            \"surface\": \"\
    retained BioC\",\n            \"file\": {\n              \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml\"\
    ,\n              \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n              \"bytes\": 174908\n            },\n            \"locator\": \"\
    passage offset 27057\"\n          },\n          {\n            \"surface\": \"\
    retained BioC\",\n            \"file\": {\n              \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml\"\
    ,\n              \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n              \"bytes\": 174908\n            },\n            \"locator\": \"\
    passage offset 37515\"\n          },\n          {\n            \"surface\": \"\
    retained BioC\",\n            \"file\": {\n              \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml\"\
    ,\n              \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n              \"bytes\": 174908\n            },\n            \"locator\": \"\
    passage offset 39253\"\n          },\n          {\n            \"surface\": \"\
    retained BioC\",\n            \"file\": {\n              \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml\"\
    ,\n              \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n              \"bytes\": 174908\n            },\n            \"locator\": \"\
    passage offset 47480\"\n          },\n          {\n            \"surface\": \"\
    retained BioC\",\n            \"file\": {\n              \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml\"\
    ,\n              \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n              \"bytes\": 174908\n            },\n            \"locator\": \"\
    passage offset 49122\"\n          },\n          {\n            \"surface\": \"\
    retained BioC\",\n            \"file\": {\n              \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml\"\
    ,\n              \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n              \"bytes\": 174908\n            },\n            \"locator\": \"\
    passage offset 67131\"\n          }\n        ]\n      },\n      {\n        \"\
    field_path\": \"causal_graphs[0].edges[0].evidence[0].snippet\",\n        \"reference\"\
    : \"DOI:10.1038/nrmicro2549\",\n        \"snippet\": \"cytoplasmic pH\",\n   \
    \     \"outcome\": \"literal_exact\",\n        \"hits\": [\n          {\n    \
    \        \"surface\": \"indexed abstract\",\n            \"file\": {\n       \
    \       \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-metadata.json\"\
    ,\n              \"sha256\": \"036607538c4110a45aeab78f8cad03b240ab3648075984f6f3e870b03692e3fd\"\
    ,\n              \"bytes\": 4996\n            },\n            \"locator\": \"\
    abstractText\"\n          },\n          {\n            \"surface\": \"retained\
    \ BioC\",\n            \"file\": {\n              \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml\"\
    ,\n              \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n              \"bytes\": 174908\n            },\n            \"locator\": \"\
    passage offset 58\"\n          },\n          {\n            \"surface\": \"retained\
    \ BioC\",\n            \"file\": {\n              \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml\"\
    ,\n              \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n              \"bytes\": 174908\n            },\n            \"locator\": \"\
    passage offset 671\"\n          },\n          {\n            \"surface\": \"retained\
    \ BioC\",\n            \"file\": {\n              \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml\"\
    ,\n              \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n              \"bytes\": 174908\n            },\n            \"locator\": \"\
    passage offset 2440\"\n          },\n          {\n            \"surface\": \"\
    retained BioC\",\n            \"file\": {\n              \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml\"\
    ,\n              \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n              \"bytes\": 174908\n            },\n            \"locator\": \"\
    passage offset 3940\"\n          },\n          {\n            \"surface\": \"\
    retained BioC\",\n            \"file\": {\n              \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml\"\
    ,\n              \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n              \"bytes\": 174908\n            },\n            \"locator\": \"\
    passage offset 4950\"\n          },\n          {\n            \"surface\": \"\
    retained BioC\",\n            \"file\": {\n              \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml\"\
    ,\n              \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n              \"bytes\": 174908\n            },\n            \"locator\": \"\
    passage offset 7133\"\n          },\n          {\n            \"surface\": \"\
    retained BioC\",\n            \"file\": {\n              \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml\"\
    ,\n              \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n              \"bytes\": 174908\n            },\n            \"locator\": \"\
    passage offset 7180\"\n          },\n          {\n            \"surface\": \"\
    retained BioC\",\n            \"file\": {\n              \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml\"\
    ,\n              \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n              \"bytes\": 174908\n            },\n            \"locator\": \"\
    passage offset 7328\"\n          },\n          {\n            \"surface\": \"\
    retained BioC\",\n            \"file\": {\n              \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml\"\
    ,\n              \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n              \"bytes\": 174908\n            },\n            \"locator\": \"\
    passage offset 7370\"\n          },\n          {\n            \"surface\": \"\
    retained BioC\",\n            \"file\": {\n              \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml\"\
    ,\n              \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n              \"bytes\": 174908\n            },\n            \"locator\": \"\
    passage offset 8457\"\n          },\n          {\n            \"surface\": \"\
    retained BioC\",\n            \"file\": {\n              \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml\"\
    ,\n              \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n              \"bytes\": 174908\n            },\n            \"locator\": \"\
    passage offset 9102\"\n          },\n          {\n            \"surface\": \"\
    retained BioC\",\n            \"file\": {\n              \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml\"\
    ,\n              \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n              \"bytes\": 174908\n            },\n            \"locator\": \"\
    passage offset 17378\"\n          },\n          {\n            \"surface\": \"\
    retained BioC\",\n            \"file\": {\n              \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml\"\
    ,\n              \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n              \"bytes\": 174908\n            },\n            \"locator\": \"\
    passage offset 27057\"\n          },\n          {\n            \"surface\": \"\
    retained BioC\",\n            \"file\": {\n              \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml\"\
    ,\n              \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n              \"bytes\": 174908\n            },\n            \"locator\": \"\
    passage offset 37515\"\n          },\n          {\n            \"surface\": \"\
    retained BioC\",\n            \"file\": {\n              \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml\"\
    ,\n              \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n              \"bytes\": 174908\n            },\n            \"locator\": \"\
    passage offset 39253\"\n          },\n          {\n            \"surface\": \"\
    retained BioC\",\n            \"file\": {\n              \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml\"\
    ,\n              \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n              \"bytes\": 174908\n            },\n            \"locator\": \"\
    passage offset 47480\"\n          },\n          {\n            \"surface\": \"\
    retained BioC\",\n            \"file\": {\n              \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml\"\
    ,\n              \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n              \"bytes\": 174908\n            },\n            \"locator\": \"\
    passage offset 49122\"\n          },\n          {\n            \"surface\": \"\
    retained BioC\",\n            \"file\": {\n              \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/krulwich-bioc.xml\"\
    ,\n              \"sha256\": \"903213411c506c8991863c506167027a9472d4fb436d3c7e8b38e9d87f7b656f\"\
    ,\n              \"bytes\": 174908\n            },\n            \"locator\": \"\
    passage offset 67131\"\n          }\n        ]\n      },\n      {\n        \"\
    field_path\": \"causal_graphs[0].edges[1].evidence[0].snippet\",\n        \"reference\"\
    : \"DOI:10.1016/j.tim.2007.02.005\",\n        \"snippet\": \"proton motive force\"\
    ,\n        \"outcome\": \"body_unknown\",\n        \"hits\": []\n      }\n   \
    \ ],\n    \"counts\": {\n      \"fields\": 3,\n      \"literal_exact\": 2,\n \
    \     \"body_unknown\": 1\n    },\n    \"native_result\": {\n      \"verified\"\
    : 2,\n      \"not_in_abstract\": 1\n    },\n    \"scope\": \"Only schema snippet\
    \ fields form this denominator. Quoted notes are separately checked; no false\
    \ quote inferred from unavailable Baker body.\"\n  },\n  \"quoted_notes\": {\n\
    \    \"completed_at\": \"2026-10-21T19:58:41.406306+00:00\",\n    \"quoted_note_fields\"\
    : [\n      {\n        \"field_path\": \"causal_graphs[0].edges[2].evidence[0].notes\"\
    ,\n        \"reference\": \"DOI:10.1111/1758-2229.70019\",\n        \"quoted_fragment\"\
    : \"That proton potential then drives the phosphorylation of ADP and the formation\
    \ of ATP by the ATP synthase\",\n        \"outcome\": \"unmarked_omission_meaning_positive\"\
    ,\n        \"literal_exact\": false,\n        \"ordered_fragments_match\": false,\n\
    \        \"primary_file\": {\n          \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/bioenergetics.xml\"\
    ,\n          \"sha256\": \"481a4f647bc7a835d74f7ec75d5f5ee8fa54ac76294f3c721a6711fd941ec58e\"\
    ,\n          \"bytes\": 324066\n        },\n        \"locator\": \"zero-based\
    \ body paragraph 21\",\n        \"scope\": \"Existing generic/source-attribution\
    \ scope only.\",\n        \"qualification\": \"Source inserts a parenthetical\
    \ between ATP and by the ATP synthase; current quotation omits it without an ellipsis.\
    \ Meaning positive.\"\n      },\n      {\n        \"field_path\": \"causal_graphs[0].edges[3].evidence[0].notes\"\
    ,\n        \"reference\": \"DOI:10.4014/jmb.2303.03009\",\n        \"quoted_fragment\"\
    : \"decreasing membrane proton permeability prevents the accumulation of intracellular\
    \ protons\",\n        \"outcome\": \"literal_exact\",\n        \"literal_exact\"\
    : true,\n        \"ordered_fragments_match\": true,\n        \"primary_file\"\
    : {\n          \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/cfa.xml\"\
    ,\n          \"sha256\": \"f37423cf43c8cc6b8d9d64feacad8ec0407e625fce4293e3fab20fac5d1e8acb\"\
    ,\n          \"bytes\": 75721\n        },\n        \"locator\": \"zero-based body\
    \ paragraph 6\",\n        \"scope\": \"Literal occurrence only; detailed pathogen\
    \ efficacy UNASSESSED_SCOPE.\",\n        \"qualification\": \"Exact existing fragment;\
    \ not a biological efficacy certification.\"\n      },\n      {\n        \"field_path\"\
    : \"causal_graphs[0].edges[4].evidence[0].notes\",\n        \"reference\": \"\
    DOI:10.1111/1758-2229.70019\",\n        \"quoted_fragment\": \"organic acids...\
    \ occur in their undissociated form and can diffuse into the cell\",\n       \
    \ \"outcome\": \"marked_abridgment\",\n        \"literal_exact\": false,\n   \
    \     \"ordered_fragments_match\": true,\n        \"primary_file\": {\n      \
    \    \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/bioenergetics.xml\"\
    ,\n          \"sha256\": \"481a4f647bc7a835d74f7ec75d5f5ee8fa54ac76294f3c721a6711fd941ec58e\"\
    ,\n          \"bytes\": 324066\n        },\n        \"locator\": \"zero-based\
    \ body paragraph 25\",\n        \"scope\": \"Existing generic/source-attribution\
    \ scope only.\",\n        \"qualification\": \"Explicit ellipses mark omitted\
    \ intervening words; no whole-sentence verbatim claim.\"\n      },\n      {\n\
    \        \"field_path\": \"causal_graphs[0].edges[5].evidence[0].notes\",\n  \
    \      \"reference\": \"DOI:10.1111/1758-2229.70019\",\n        \"quoted_fragment\"\
    : \"the higher pH of the cytoplasm will lead to dissociation of the acid, thus\
    \ releasing protons and lowering the internal pH\",\n        \"outcome\": \"literal_exact\"\
    ,\n        \"literal_exact\": true,\n        \"ordered_fragments_match\": true,\n\
    \        \"primary_file\": {\n          \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/bioenergetics.xml\"\
    ,\n          \"sha256\": \"481a4f647bc7a835d74f7ec75d5f5ee8fa54ac76294f3c721a6711fd941ec58e\"\
    ,\n          \"bytes\": 324066\n        },\n        \"locator\": \"zero-based\
    \ body paragraph 25\",\n        \"scope\": \"Existing generic/source-attribution\
    \ scope only.\",\n        \"qualification\": \"Exact existing fragment; not a\
    \ biological efficacy certification.\"\n      },\n      {\n        \"field_path\"\
    : \"causal_graphs[0].edges[6].evidence[0].notes\",\n        \"reference\": \"\
    DOI:10.3389/fmicb.2023.1149903\",\n        \"quoted_fragment\": \"a P-type ATPase\
    \ proton efflux pump\",\n        \"outcome\": \"literal_exact\",\n        \"literal_exact\"\
    : true,\n        \"ordered_fragments_match\": true,\n        \"primary_file\"\
    : {\n          \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/acid-genomes.xml\"\
    ,\n          \"sha256\": \"6f9494d7379f7f7914200f9ba87905a42e803d6173cd22dd1fa837ccefc1f1e0\"\
    ,\n          \"bytes\": 295345\n        },\n        \"locator\": \"zero-based\
    \ body paragraph 36\",\n        \"scope\": \"Existing generic/source-attribution\
    \ scope only.\",\n        \"qualification\": \"Exact existing fragment; not a\
    \ biological efficacy certification.\"\n      },\n      {\n        \"field_path\"\
    : \"causal_graphs[0].edges[7].evidence[0].notes\",\n        \"reference\": \"\
    DOI:10.3390/microorganisms12030625\",\n        \"quoted_fragment\": \"acid stress\
    \ tolerance... facilitated by an active export of protons via the expenditure\
    \ of ATP... carried out by H+-ATPases\",\n        \"outcome\": \"marked_abridgment\"\
    ,\n        \"literal_exact\": false,\n        \"ordered_fragments_match\": true,\n\
    \        \"primary_file\": {\n          \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-source-agent/homeostasis.xml\"\
    ,\n          \"sha256\": \"b5f6a85c09e160674f98031032880e7b52f8e22a465d2678ff48f94dcc95fd94\"\
    ,\n          \"bytes\": 193700\n        },\n        \"locator\": \"zero-based\
    \ body paragraph 2\",\n        \"scope\": \"Existing generic/source-attribution\
    \ scope only.\",\n        \"qualification\": \"Explicit ellipses mark omitted\
    \ intervening words; no whole-sentence verbatim claim.\"\n      }\n    ],\n  \
    \  \"counts\": {\n      \"fields\": 6,\n      \"literal_exact\": 3,\n      \"\
    marked_abridgment\": 2,\n      \"unmarked_omission_meaning_positive\": 1\n   \
    \ },\n    \"scope\": \"Separate from native three snippet fields. Quotation precision\
    \ does not certify biological sufficiency.\"\n  }\n}"
- assessment_id: nodes
  area: grounding
  topic: 'Native checklist: all thirteen declared referents'
  outcome: supported
  target_ids:
  - METPO:1000460
  summary: The PMF gradient is STATE, ATP formation is a process, permeability/internal
    pH are measured qualities, and the chemical/protein nodes retain material referents.
    One reviewed label-only class is explicit. Their coherent individual facets do
    not excuse the process/process relation mismatch at edge 3.
  evidence_ids:
  - node-edges
  - schema
  - policy
  - pmf-row
  details: "[\n  {\n    \"index\": 0,\n    \"field_path\": \"causal_graphs[0].nodes[0]\"\
    ,\n    \"current\": {\n      \"node_id\": \"ph_range_low_trait\",\n      \"label\"\
    : \"pH range low\",\n      \"node_type\": \"TRAIT\",\n      \"grounding\": \"\
    METPO:1000460\",\n      \"description\": \"pH growth-supporting range approximately\
    \ 4\\u20136.\"\n    },\n    \"status\": \"supported_identity\",\n    \"assessment\"\
    : \"Active METPO identity, direct parent and declared numerical interval agree\
    \ with the imported class. Scientific equivalence of the broad exact aliases is\
    \ a separate source-classification question.\"\n  },\n  {\n    \"index\": 1,\n\
    \    \"field_path\": \"causal_graphs[0].nodes[1]\",\n    \"current\": {\n    \
    \  \"node_id\": \"ph_range\",\n      \"label\": \"pH range\",\n      \"node_type\"\
    : \"TRAIT\",\n      \"grounding\": \"METPO:1000332\",\n      \"description\":\
    \ \"Span of external pH values supporting growth.\"\n    },\n    \"status\": \"\
    supported_identity\",\n    \"assessment\": \"The pH-range parent represents a\
    \ span of external pH values; both imported parent branches provide the numerical-limit\
    \ context.\"\n  },\n  {\n    \"index\": 2,\n    \"field_path\": \"causal_graphs[0].nodes[2]\"\
    ,\n    \"current\": {\n      \"node_id\": \"acidophile_homeostasis\",\n      \"\
    label\": \"acidophile pH homeostasis\",\n      \"node_type\": \"BIOLOGICAL_PROCESS\"\
    ,\n      \"description\": \"Proton extrusion and envelope barriers maintaining\
    \ cytoplasmic pH against a moderately acidic external pH.\"\n    },\n    \"status\"\
    : \"supported_facet\",\n    \"assessment\": \"The node denotes maintenance activity\
    \ and has a coherent BIOLOGICAL_PROCESS referent. Detailed defense efficacy is\
    \ unassessed.\"\n  },\n  {\n    \"index\": 3,\n    \"field_path\": \"causal_graphs[0].nodes[3]\"\
    ,\n    \"current\": {\n      \"node_id\": \"proton_motive_force\",\n      \"label\"\
    : \"proton motive force\",\n      \"node_type\": \"STATE\",\n      \"description\"\
    : \"Transmembrane electrochemical proton gradient maintained by H+ extrusion.\"\
    ,\n      \"grounding\": \"METPO:1007500\"\n    },\n    \"status\": \"supported_facet\"\
    ,\n    \"assessment\": \"The gradient is explicitly STATE, matching the actual\
    \ v3 local proposal, maintained row 44 and schema distinction between a state\
    \ and its establishment.\"\n  },\n  {\n    \"index\": 4,\n    \"field_path\":\
    \ \"causal_graphs[0].nodes[4]\",\n    \"current\": {\n      \"node_id\": \"atp_synthase_atp_formation\"\
    ,\n      \"label\": \"ATP synthase-mediated ATP formation\",\n      \"node_type\"\
    : \"BIOLOGICAL_PROCESS\",\n      \"description\": \"Phosphorylation of ADP to\
    \ ATP driven by the proton motive force.\"\n    },\n    \"status\": \"supported_facet\"\
    ,\n    \"assessment\": \"ATP formation is explicitly a process, distinct from\
    \ a material ATP-synthase complex. No copied material-node finding applies.\"\n\
    \  },\n  {\n    \"index\": 5,\n    \"field_path\": \"causal_graphs[0].nodes[5]\"\
    ,\n    \"current\": {\n      \"node_id\": \"cyclopropane_fatty_acids\",\n    \
    \  \"label\": \"cyclopropane fatty acids\",\n      \"node_type\": \"CHEMICAL\"\
    ,\n      \"description\": \"Cyclopropane-fatty-acyl phospholipids produced by\
    \ Cfa synthase that modify the membrane.\"\n    },\n    \"status\": \"supported_facet\"\
    ,\n    \"assessment\": \"The node denotes material fatty-acyl chemicals, not the\
    \ process that modifies a membrane. This distinction matters to the current regulation\
    \ edge without assessing biological efficacy.\"\n  },\n  {\n    \"index\": 6,\n\
    \    \"field_path\": \"causal_graphs[0].nodes[6]\",\n    \"current\": {\n    \
    \  \"node_id\": \"proton_permeability\",\n      \"label\": \"membrane proton permeability\"\
    ,\n      \"node_type\": \"QUALITY\",\n      \"description\": \"Permeability of\
    \ the cell membrane to protons.\"\n    },\n    \"status\": \"supported_facet\"\
    ,\n    \"assessment\": \"Proton permeability is explicitly a measurable QUALITY.\
    \ The maintained migration supports this sense; no forced process retype is justified.\"\
    \n  },\n  {\n    \"index\": 7,\n    \"field_path\": \"causal_graphs[0].nodes[7]\"\
    ,\n    \"current\": {\n      \"node_id\": \"undissociated_weak_acids\",\n    \
    \  \"label\": \"undissociated weak organic acids\",\n      \"node_type\": \"CHEMICAL\"\
    ,\n      \"description\": \"Protonated, membrane-permeant form of weak organic\
    \ acids prevalent at low external pH.\"\n    },\n    \"status\": \"supported_facet\"\
    ,\n    \"assessment\": \"The node denotes the chemical form of weak acids. The\
    \ description does not require an environmental-condition retype.\"\n  },\n  {\n\
    \    \"index\": 8,\n    \"field_path\": \"causal_graphs[0].nodes[8]\",\n    \"\
    current\": {\n      \"node_id\": \"weak_acid_influx\",\n      \"label\": \"weak\
    \ organic acid influx into cell\",\n      \"node_type\": \"BIOLOGICAL_PROCESS\"\
    ,\n      \"description\": \"Diffusion of undissociated weak organic acids across\
    \ the membrane at low external pH.\"\n    },\n    \"status\": \"supported_facet\"\
    ,\n    \"assessment\": \"Influx denotes a process; a free-text undergoes edge\
    \ has no imported material-subject exclusion.\"\n  },\n  {\n    \"index\": 9,\n\
    \    \"field_path\": \"causal_graphs[0].nodes[9]\",\n    \"current\": {\n    \
    \  \"node_id\": \"weak_acid_dissociation\",\n      \"label\": \"intracellular\
    \ dissociation of weak organic acids\",\n      \"node_type\": \"BIOLOGICAL_PROCESS\"\
    ,\n      \"description\": \"Dissociation of weak acids in the near-neutral cytoplasm,\
    \ releasing protons.\"\n    },\n    \"status\": \"supported_facet\",\n    \"assessment\"\
    : \"Dissociation denotes a process. Detailed intracellular mechanism or fitness\
    \ effects are unassessed.\"\n  },\n  {\n    \"index\": 10,\n    \"field_path\"\
    : \"causal_graphs[0].nodes[10]\",\n    \"current\": {\n      \"node_id\": \"internal_ph\"\
    ,\n      \"label\": \"internal (cytoplasmic) pH\",\n      \"node_type\": \"QUALITY\"\
    ,\n      \"description\": \"pH of the cytoplasm.\"\n    },\n    \"status\": \"\
    supported_facet\",\n    \"assessment\": \"Internal pH is a measurable QUALITY,\
    \ not a process.\"\n  },\n  {\n    \"index\": 11,\n    \"field_path\": \"causal_graphs[0].nodes[11]\"\
    ,\n    \"current\": {\n      \"node_id\": \"h_atpase\",\n      \"label\": \"H+-ATPase\
    \ proton efflux pump\",\n      \"node_type\": \"GENE_OR_PROTEIN\",\n      \"grounding_status\"\
    : \"REVIEWED_LABEL_ONLY\",\n      \"grounding_notes\": \"Reviewed as a contextual\
    \ protein or protein-complex label within a quantitative measurement graph; no\
    \ exact semantic family term was established for this aggregate use.\",\n    \
    \  \"description\": \"ATP-driven proton-exporting ATPase (e.g. P-type H+-ATPase).\"\
    \n    },\n    \"status\": \"supported_facet\",\n    \"assessment\": \"The pump\
    \ is a material protein class with explicit reviewed-label-only disposition; no\
    \ token accession or instance is required.\"\n  },\n  {\n    \"index\": 12,\n\
    \    \"field_path\": \"causal_graphs[0].nodes[12]\",\n    \"current\": {\n   \
    \   \"node_id\": \"cytoplasmic_protons\",\n      \"label\": \"cytoplasmic protons\"\
    ,\n      \"node_type\": \"CHEMICAL\",\n      \"description\": \"Protons (hydrons)\
    \ within the cytoplasm.\"\n    },\n    \"status\": \"supported_facet\",\n    \"\
    assessment\": \"Cytoplasmic protons have a material chemical referent; no obligatory\
    \ CAPACITY retype follows from localization.\"\n  }\n]"
- assessment_id: relations
  area: consistency
  topic: 'Native checklist: all eight relations'
  outcome: concern
  target_ids:
  - METPO:1000460
  summary: RO2212 edge 3 inherits process/process semantics but links material cyclopropane
    fatty acids to permeability QUALITY. This formal representation issue is separate
    from unassessed defense efficacy. RO2326 edge 7 and local confers/exports fit
    current referents; free-text drives, undergoes and lowers receive no invented
    imported exclusions.
  evidence_ids:
  - node-edges
  - ro-primary
  - local-authority
  - challenge
  details: "[\n  {\n    \"index\": 0,\n    \"field_path\": \"causal_graphs[0].edges[0]\"\
    ,\n    \"current\": {\n      \"subject\": \"acidophile_homeostasis\",\n      \"\
    predicate\": \"confers\",\n      \"object\": \"ph_range_low_trait\",\n      \"\
    description\": \"Acidophile pH-homeostasis enables growth across pH 4\\u20136.\"\
    ,\n      \"evidence\": [\n        {\n          \"reference\": \"DOI:10.1038/nrmicro2549\"\
    ,\n          \"snippet\": \"cytoplasmic pH\",\n          \"notes\": \"Supports\
    \ acidophile cytoplasmic pH homeostasis as the moderately-acidic growth-range\
    \ mechanism.\"\n        }\n      ],\n      \"predicate_id\": \"METPO:2007700\"\
    \n    },\n    \"status\": \"supported_formal_scope\",\n    \"assessment\": \"\
    The local v8 confers relation accepts this process-to-trait shape. Source support\
    \ for the exact numeric bin remains separate from this endpoint assessment.\"\n\
    \  },\n  {\n    \"index\": 1,\n    \"field_path\": \"causal_graphs[0].edges[1]\"\
    ,\n    \"current\": {\n      \"subject\": \"ph_range_low_trait\",\n      \"predicate\"\
    : \"is a\",\n      \"object\": \"ph_range\",\n      \"description\": \"pH range\
    \ low is a quantitative bin of the pH-range phenotype.\",\n      \"evidence\"\
    : [\n        {\n          \"reference\": \"DOI:10.1016/j.tim.2007.02.005\",\n\
    \          \"snippet\": \"proton motive force\",\n          \"notes\": \"Supports\
    \ the pH 4\\u20136 range as a value within the pH-range distribution.\"\n    \
    \    }\n      ],\n      \"predicate_id\": \"rdfs:subClassOf\"\n    },\n    \"\
    status\": \"supported_identity\",\n    \"assessment\": \"The subclass relation\
    \ and current direct parent are supported. The source attribution for exact numeric\
    \ calibration is assessed separately by the source audit.\"\n  },\n  {\n    \"\
    index\": 2,\n    \"field_path\": \"causal_graphs[0].edges[2]\",\n    \"current\"\
    : {\n      \"subject\": \"proton_motive_force\",\n      \"predicate\": \"drives\"\
    ,\n      \"object\": \"atp_synthase_atp_formation\",\n      \"description\": \"\
    The proton motive force drives ATP synthase phosphorylation of ADP to ATP.\",\n\
    \      \"evidence\": [\n        {\n          \"reference\": \"DOI:10.1111/1758-2229.70019\"\
    ,\n          \"notes\": \"\\\"That proton potential then drives the phosphorylation\
    \ of ADP and the formation of ATP by the ATP synthase\\\"; general bioenergetic\
    \ edge relevant to low-pH growth.\"\n        }\n      ]\n    },\n    \"status\"\
    : \"supported_formal_scope\",\n    \"assessment\": \"Free-text drives is not an\
    \ asserted RO enables edge. STATE-to-process is not automatically prohibited,\
    \ and no predicate grounding is mandatory.\"\n  },\n  {\n    \"index\": 3,\n \
    \   \"field_path\": \"causal_graphs[0].edges[3]\",\n    \"current\": {\n     \
    \ \"subject\": \"cyclopropane_fatty_acids\",\n      \"predicate\": \"decreases\"\
    ,\n      \"object\": \"proton_permeability\",\n      \"description\": \"Cyclopropane\
    \ fatty acid membrane modification decreases proton permeability.\",\n      \"\
    evidence\": [\n        {\n          \"reference\": \"DOI:10.4014/jmb.2303.03009\"\
    ,\n          \"notes\": \"\\\"decreasing membrane proton permeability prevents\
    \ the accumulation of intracellular protons\\\" after conversion to cyclopropane\
    \ fatty acids; generalizable membrane adaptation.\"\n        }\n      ],\n   \
    \   \"predicate_id\": \"RO:0002212\"\n    },\n    \"status\": \"major_formal_roles\"\
    ,\n    \"assessment\": \"RO:0002212 is a subproperty of RO:0002211, whose actual\
    \ primary statements declare process domain and range. Current material cyclopropane\
    \ fatty acids and permeability QUALITY are not the processes required by that\
    \ relation. This is a formal representation issue, not a finding that the biological\
    \ statement is false.\"\n  },\n  {\n    \"index\": 4,\n    \"field_path\": \"\
    causal_graphs[0].edges[4]\",\n    \"current\": {\n      \"subject\": \"undissociated_weak_acids\"\
    ,\n      \"predicate\": \"undergoes\",\n      \"object\": \"weak_acid_influx\"\
    ,\n      \"description\": \"At low external pH weak organic acids are undissociated\
    \ and diffuse into the cell.\",\n      \"evidence\": [\n        {\n          \"\
    reference\": \"DOI:10.1111/1758-2229.70019\",\n          \"notes\": \"\\\"organic\
    \ acids... occur in their undissociated form and can diffuse into the cell\\\"\
    ; boundary condition distinguishing low-pH growth from weak-acid inhibition.\"\
    \n        }\n      ]\n    },\n    \"status\": \"supported_formal_scope\",\n  \
    \  \"assessment\": \"Free-text undergoes permits the current material-to-influx\
    \ documentary reading; no external formal range restriction is asserted.\"\n \
    \ },\n  {\n    \"index\": 5,\n    \"field_path\": \"causal_graphs[0].edges[5]\"\
    ,\n    \"current\": {\n      \"subject\": \"weak_acid_dissociation\",\n      \"\
    predicate\": \"lowers\",\n      \"object\": \"internal_ph\",\n      \"description\"\
    : \"Intracellular dissociation of weak organic acids releases protons and lowers\
    \ cytoplasmic pH.\",\n      \"evidence\": [\n        {\n          \"reference\"\
    : \"DOI:10.1111/1758-2229.70019\",\n          \"notes\": \"\\\"the higher pH of\
    \ the cytoplasm will lead to dissociation of the acid, thus releasing protons\
    \ and lowering the internal pH\\\"; strong causal edge.\"\n        }\n      ]\n\
    \    },\n    \"status\": \"supported_formal_scope\",\n    \"assessment\": \"Free-text\
    \ lowers has no imported process/process constraint. A process affecting a measured\
    \ pH quality is not by itself a formal defect.\"\n  },\n  {\n    \"index\": 6,\n\
    \    \"field_path\": \"causal_graphs[0].edges[6]\",\n    \"current\": {\n    \
    \  \"subject\": \"h_atpase\",\n      \"predicate\": \"exports\",\n      \"object\"\
    : \"cytoplasmic_protons\",\n      \"description\": \"H+-ATPases actively export\
    \ protons from the cytoplasm using ATP.\",\n      \"evidence\": [\n        {\n\
    \          \"reference\": \"DOI:10.3389/fmicb.2023.1149903\",\n          \"notes\"\
    : \"Acidophile genomes encode \\\"a P-type ATPase proton efflux pump\\\"; active\
    \ ATP-driven proton export underlies cytoplasmic pH homeostasis.\"\n        }\n\
    \      ],\n      \"predicate_id\": \"METPO:2007804\"\n    },\n    \"status\":\
    \ \"supported_formal_scope\",\n    \"assessment\": \"The actual v9 exports definition\
    \ and maintained gate admit protein subject and chemical object, with movement\
    \ from cytoplasm to exterior. Detailed transport efficacy is unassessed.\"\n \
    \ },\n  {\n    \"index\": 7,\n    \"field_path\": \"causal_graphs[0].edges[7]\"\
    ,\n    \"current\": {\n      \"subject\": \"h_atpase\",\n      \"predicate\":\
    \ \"contributes to\",\n      \"object\": \"acidophile_homeostasis\",\n      \"\
    description\": \"ATP-driven proton export by H+-ATPases contributes to acidophile\
    \ pH homeostasis.\",\n      \"evidence\": [\n        {\n          \"reference\"\
    : \"DOI:10.3390/microorganisms12030625\",\n          \"notes\": \"\\\"acid stress\
    \ tolerance... facilitated by an active export of protons via the expenditure\
    \ of ATP... carried out by H+-ATPases\\\"; broad principle of homeostasis.\"\n\
    \        }\n      ],\n      \"predicate_id\": \"RO:0002326\"\n    },\n    \"status\"\
    : \"supported_formal_scope\",\n    \"assessment\": \"The material ATPase and maintenance-process\
    \ object satisfy the inherited material/process requirements of RO:0002326. No\
    \ blanket chemical or protein rule is applied.\"\n  }\n]"
- assessment_id: biological-scope
  area: scope
  topic: 'Native checklist: bounded environmental and literal context'
  outcome: unknown
  target_ids:
  - METPO:1000460
  summary: Existing generic environmental PMF and weak-acid chemistry, source-specific
    genomic presence and yeast background are considered only within inspected scope.
    CFA defense biology and all detailed pathogen fitness/AMR, perturbation and optimization
    efficacy remain UNASSESSED_SCOPE. No repaired route, improved condition or experiment
    is proposed.
  evidence_ids:
  - edge-sources
  - source-reading
  - body-bioenergetics
  - body-cfa
  - body-homeostasis
  details: "{\n  \"completed_at\": \"2026-10-21T19:58:41.401685+00:00\",\n  \"edges\"\
    : [\n    {\n      \"index\": 0,\n      \"field_path\": \"causal_graphs[0].edges[0]\"\
    ,\n      \"subject\": \"acidophile_homeostasis\",\n      \"predicate\": \"confers\"\
    ,\n      \"predicate_id\": \"METPO:2007700\",\n      \"object\": \"ph_range_low_trait\"\
    ,\n      \"description\": \"Acidophile pH-homeostasis enables growth across pH\
    \ 4\\u20136.\",\n      \"evidence\": [\n        {\n          \"reference\": \"\
    DOI:10.1038/nrmicro2549\",\n          \"snippet\": \"cytoplasmic pH\",\n     \
    \     \"notes\": \"Supports acidophile cytoplasmic pH homeostasis as the moderately-acidic\
    \ growth-range mechanism.\"\n        }\n      ],\n      \"assessment\": \"Actual\
    \ generic homeostasis context is positive, but acidophile categories and physiological\
    \ mechanisms do not establish an exact complete4\\u20136 interval. Group scope\
    \ with category/bin assessment; no biological falsity or universal mechanism is\
    \ inferred.\",\n      \"biological_scope\": \"Existing generic environmental/chemical\
    \ context only; no new mechanism or intervention efficacy.\"\n    },\n    {\n\
    \      \"index\": 1,\n      \"field_path\": \"causal_graphs[0].edges[1]\",\n \
    \     \"subject\": \"ph_range_low_trait\",\n      \"predicate\": \"is a\",\n \
    \     \"predicate_id\": \"rdfs:subClassOf\",\n      \"object\": \"ph_range\",\n\
    \      \"description\": \"pH range low is a quantitative bin of the pH-range phenotype.\"\
    ,\n      \"evidence\": [\n        {\n          \"reference\": \"DOI:10.1016/j.tim.2007.02.005\"\
    ,\n          \"snippet\": \"proton motive force\",\n          \"notes\": \"Supports\
    \ the pH 4\\u20136 range as a value within the pH-range distribution.\"\n    \
    \    }\n      ],\n      \"assessment\": \"Ontology supplies the parent/bin hierarchy.\
    \ Baker abstract classifies acidophiles by optimum below3 and supports generic\
    \ homeostasis; it does not directly calibrate a complete4\\u20136 interval. Assigned\
    \ PMF body phrase remains unknown; lack of abstract occurrence is not a false\
    \ quotation.\",\n      \"biological_scope\": \"Existing generic environmental/chemical\
    \ context only; no new mechanism or intervention efficacy.\"\n    },\n    {\n\
    \      \"index\": 2,\n      \"field_path\": \"causal_graphs[0].edges[2]\",\n \
    \     \"subject\": \"proton_motive_force\",\n      \"predicate\": \"drives\",\n\
    \      \"predicate_id\": null,\n      \"object\": \"atp_synthase_atp_formation\"\
    ,\n      \"description\": \"The proton motive force drives ATP synthase phosphorylation\
    \ of ADP to ATP.\",\n      \"evidence\": [\n        {\n          \"reference\"\
    : \"DOI:10.1111/1758-2229.70019\",\n          \"notes\": \"\\\"That proton potential\
    \ then drives the phosphorylation of ADP and the formation of ATP by the ATP synthase\\\
    \"; general bioenergetic edge relevant to low-pH growth.\"\n        }\n      ],\n\
    \      \"assessment\": \"Existing generic PMF-to-ATP statement is supported at\
    \ bioenergetics body21. The quoted note removes an intervening parenthesis without\
    \ an ellipsis; meaning remains positive and no efficacy/intervention inference\
    \ is made.\",\n      \"biological_scope\": \"Existing generic environmental/chemical\
    \ context only; no new mechanism or intervention efficacy.\"\n    },\n    {\n\
    \      \"index\": 3,\n      \"field_path\": \"causal_graphs[0].edges[3]\",\n \
    \     \"subject\": \"cyclopropane_fatty_acids\",\n      \"predicate\": \"decreases\"\
    ,\n      \"predicate_id\": \"RO:0002212\",\n      \"object\": \"proton_permeability\"\
    ,\n      \"description\": \"Cyclopropane fatty acid membrane modification decreases\
    \ proton permeability.\",\n      \"evidence\": [\n        {\n          \"reference\"\
    : \"DOI:10.4014/jmb.2303.03009\",\n          \"notes\": \"\\\"decreasing membrane\
    \ proton permeability prevents the accumulation of intracellular protons\\\" after\
    \ conversion to cyclopropane fatty acids; generalizable membrane adaptation.\"\
    \n        }\n      ],\n      \"assessment\": \"Current quoted fragment is literally\
    \ present in CFA body6. Source title/abstract identify pathogenic Gram-negative\
    \ acid-defense scope. Only identity, quote occurrence and separately audited formal\
    \ roles are assessed; generalizable biological efficacy is UNASSESSED_SCOPE.\"\
    ,\n      \"biological_scope\": \"UNASSESSED_SCOPE\"\n    },\n    {\n      \"index\"\
    : 4,\n      \"field_path\": \"causal_graphs[0].edges[4]\",\n      \"subject\"\
    : \"undissociated_weak_acids\",\n      \"predicate\": \"undergoes\",\n      \"\
    predicate_id\": null,\n      \"object\": \"weak_acid_influx\",\n      \"description\"\
    : \"At low external pH weak organic acids are undissociated and diffuse into the\
    \ cell.\",\n      \"evidence\": [\n        {\n          \"reference\": \"DOI:10.1111/1758-2229.70019\"\
    ,\n          \"notes\": \"\\\"organic acids... occur in their undissociated form\
    \ and can diffuse into the cell\\\"; boundary condition distinguishing low-pH\
    \ growth from weak-acid inhibition.\"\n        }\n      ],\n      \"assessment\"\
    : \"Actual environmental review body25 supports the existing generic weak-acid\
    \ permeability context. Quoted note is a marked noncontiguous abridgment with\
    \ literal ordered fragments. It does not itself establish complete4\\u20136 growth\
    \ or a universal lineage response.\",\n      \"biological_scope\": \"Existing\
    \ generic environmental/chemical context only; no new mechanism or intervention\
    \ efficacy.\"\n    },\n    {\n      \"index\": 5,\n      \"field_path\": \"causal_graphs[0].edges[5]\"\
    ,\n      \"subject\": \"weak_acid_dissociation\",\n      \"predicate\": \"lowers\"\
    ,\n      \"predicate_id\": null,\n      \"object\": \"internal_ph\",\n      \"\
    description\": \"Intracellular dissociation of weak organic acids releases protons\
    \ and lowers cytoplasmic pH.\",\n      \"evidence\": [\n        {\n          \"\
    reference\": \"DOI:10.1111/1758-2229.70019\",\n          \"notes\": \"\\\"the\
    \ higher pH of the cytoplasm will lead to dissociation of the acid, thus releasing\
    \ protons and lowering the internal pH\\\"; strong causal edge.\"\n        }\n\
    \      ],\n      \"assessment\": \"Actual environmental review body25 contains\
    \ the current quoted dissociation/pH sentence as a contiguous phrase. Generic\
    \ acid-base chemistry is positive; no new intervention conditions or acid-defense\
    \ efficacy assessment.\",\n      \"biological_scope\": \"Existing generic environmental/chemical\
    \ context only; no new mechanism or intervention efficacy.\"\n    },\n    {\n\
    \      \"index\": 6,\n      \"field_path\": \"causal_graphs[0].edges[6]\",\n \
    \     \"subject\": \"h_atpase\",\n      \"predicate\": \"exports\",\n      \"\
    predicate_id\": \"METPO:2007804\",\n      \"object\": \"cytoplasmic_protons\"\
    ,\n      \"description\": \"H+-ATPases actively export protons from the cytoplasm\
    \ using ATP.\",\n      \"evidence\": [\n        {\n          \"reference\": \"\
    DOI:10.3389/fmicb.2023.1149903\",\n          \"notes\": \"Acidophile genomes encode\
    \ \\\"a P-type ATPase proton efflux pump\\\"; active ATP-driven proton export\
    \ underlies cytoplasmic pH homeostasis.\"\n        }\n      ],\n      \"assessment\"\
    : \"Actual environmental review body36 contains the quoted P-type-pump phrase\
    \ in the named At. ferrivorans SS3 genome context, with absence in another reported\
    \ MAG. Existing contextual presence is positive; genomic annotation is not direct\
    \ functional validation or universal necessity.\",\n      \"biological_scope\"\
    : \"Existing generic environmental/chemical context only; no new mechanism or\
    \ intervention efficacy.\"\n    },\n    {\n      \"index\": 7,\n      \"field_path\"\
    : \"causal_graphs[0].edges[7]\",\n      \"subject\": \"h_atpase\",\n      \"predicate\"\
    : \"contributes to\",\n      \"predicate_id\": \"RO:0002326\",\n      \"object\"\
    : \"acidophile_homeostasis\",\n      \"description\": \"ATP-driven proton export\
    \ by H+-ATPases contributes to acidophile pH homeostasis.\",\n      \"evidence\"\
    : [\n        {\n          \"reference\": \"DOI:10.3390/microorganisms12030625\"\
    ,\n          \"notes\": \"\\\"acid stress tolerance... facilitated by an active\
    \ export of protons via the expenditure of ATP... carried out by H+-ATPases\\\"\
    ; broad principle of homeostasis.\"\n        }\n      ],\n      \"assessment\"\
    : \"Actual yeast article body2 gives the generic existing proton-export background\
    \ sentence. Note is marked abridgment; source context is S. cerevisiae and background\
    \ citations, not the new engineered-pump result. No perturbation efficacy, optimization\
    \ or exact4\\u20136 calibration is adopted.\",\n      \"biological_scope\": \"\
    Existing generic environmental/chemical context only; no new mechanism or intervention\
    \ efficacy.\"\n    }\n  ]\n}"
- assessment_id: completeness
  area: completeness
  topic: 'Native checklist: whole-record coverage and optional evidence'
  outcome: supported
  target_ids:
  - METPO:1000460
  summary: All thirteen nodes, eight edges, five components, twelve events, one canonical,
    three schema snippets and six quote-bearing notes are covered. One reviewed label-only
    protein class and zero instances are allowed; no token accession, extra connector,
    pathway or substitute canonical is required.
  evidence_ids:
  - record
  - node-edges
  - node-sources
  - policy
  - checklist
  details: "{\n  \"completed_at\": \"2026-10-21T19:58:41.401839+00:00\",\n  \"nodes\"\
    : [\n    {\n      \"index\": 0,\n      \"field_path\": \"causal_graphs[0].nodes[0]\"\
    ,\n      \"node\": {\n        \"node_id\": \"ph_range_low_trait\",\n        \"\
    label\": \"pH range low\",\n        \"node_type\": \"TRAIT\",\n        \"grounding\"\
    : \"METPO:1000460\",\n        \"description\": \"pH growth-supporting range approximately\
    \ 4\\u20136.\"\n      },\n      \"incident_edges\": [\n        0,\n        1\n\
    \      ],\n      \"references\": [\n        \"DOI:10.1016/j.tim.2007.02.005\"\
    ,\n        \"DOI:10.1038/nrmicro2549\"\n      ],\n      \"assessment\": \"All\
    \ incident source placements accounted for. Complete4\\u20136 interval is distinct\
    \ from broad acidophily categories and contextual physiology.\"\n    },\n    {\n\
    \      \"index\": 1,\n      \"field_path\": \"causal_graphs[0].nodes[1]\",\n \
    \     \"node\": {\n        \"node_id\": \"ph_range\",\n        \"label\": \"pH\
    \ range\",\n        \"node_type\": \"TRAIT\",\n        \"grounding\": \"METPO:1000332\"\
    ,\n        \"description\": \"Span of external pH values supporting growth.\"\n\
    \      },\n      \"incident_edges\": [\n        1\n      ],\n      \"references\"\
    : [\n        \"DOI:10.1016/j.tim.2007.02.005\"\n      ],\n      \"assessment\"\
    : \"All incident source placements accounted for. Existing generic environmental,\
    \ chemistry or documentary identity context only. No universal biological mechanism\
    \ or exact-bin sufficient cause is inferred.\"\n    },\n    {\n      \"index\"\
    : 2,\n      \"field_path\": \"causal_graphs[0].nodes[2]\",\n      \"node\": {\n\
    \        \"node_id\": \"acidophile_homeostasis\",\n        \"label\": \"acidophile\
    \ pH homeostasis\",\n        \"node_type\": \"BIOLOGICAL_PROCESS\",\n        \"\
    description\": \"Proton extrusion and envelope barriers maintaining cytoplasmic\
    \ pH against a moderately acidic external pH.\"\n      },\n      \"incident_edges\"\
    : [\n        0,\n        7\n      ],\n      \"references\": [\n        \"DOI:10.1038/nrmicro2549\"\
    ,\n        \"DOI:10.3390/microorganisms12030625\"\n      ],\n      \"assessment\"\
    : \"All incident source placements accounted for. Existing generic environmental,\
    \ chemistry or documentary identity context only. No universal biological mechanism\
    \ or exact-bin sufficient cause is inferred.\"\n    },\n    {\n      \"index\"\
    : 3,\n      \"field_path\": \"causal_graphs[0].nodes[3]\",\n      \"node\": {\n\
    \        \"node_id\": \"proton_motive_force\",\n        \"label\": \"proton motive\
    \ force\",\n        \"node_type\": \"STATE\",\n        \"description\": \"Transmembrane\
    \ electrochemical proton gradient maintained by H+ extrusion.\",\n        \"grounding\"\
    : \"METPO:1007500\"\n      },\n      \"incident_edges\": [\n        2\n      ],\n\
    \      \"references\": [\n        \"DOI:10.1111/1758-2229.70019\"\n      ],\n\
    \      \"assessment\": \"All incident source placements accounted for. Existing\
    \ generic environmental, chemistry or documentary identity context only. No universal\
    \ biological mechanism or exact-bin sufficient cause is inferred.\"\n    },\n\
    \    {\n      \"index\": 4,\n      \"field_path\": \"causal_graphs[0].nodes[4]\"\
    ,\n      \"node\": {\n        \"node_id\": \"atp_synthase_atp_formation\",\n \
    \       \"label\": \"ATP synthase-mediated ATP formation\",\n        \"node_type\"\
    : \"BIOLOGICAL_PROCESS\",\n        \"description\": \"Phosphorylation of ADP to\
    \ ATP driven by the proton motive force.\"\n      },\n      \"incident_edges\"\
    : [\n        2\n      ],\n      \"references\": [\n        \"DOI:10.1111/1758-2229.70019\"\
    \n      ],\n      \"assessment\": \"All incident source placements accounted for.\
    \ Existing generic environmental, chemistry or documentary identity context only.\
    \ No universal biological mechanism or exact-bin sufficient cause is inferred.\"\
    \n    },\n    {\n      \"index\": 5,\n      \"field_path\": \"causal_graphs[0].nodes[5]\"\
    ,\n      \"node\": {\n        \"node_id\": \"cyclopropane_fatty_acids\",\n   \
    \     \"label\": \"cyclopropane fatty acids\",\n        \"node_type\": \"CHEMICAL\"\
    ,\n        \"description\": \"Cyclopropane-fatty-acyl phospholipids produced by\
    \ Cfa synthase that modify the membrane.\"\n      },\n      \"incident_edges\"\
    : [\n        3\n      ],\n      \"references\": [\n        \"DOI:10.4014/jmb.2303.03009\"\
    \n      ],\n      \"assessment\": \"All incident source placements accounted for.\
    \ CFA-linked detailed acid-defense/fitness/efficacy remains UNASSESSED_SCOPE;\
    \ current label/quote/identity only.\"\n    },\n    {\n      \"index\": 6,\n \
    \     \"field_path\": \"causal_graphs[0].nodes[6]\",\n      \"node\": {\n    \
    \    \"node_id\": \"proton_permeability\",\n        \"label\": \"membrane proton\
    \ permeability\",\n        \"node_type\": \"QUALITY\",\n        \"description\"\
    : \"Permeability of the cell membrane to protons.\"\n      },\n      \"incident_edges\"\
    : [\n        3\n      ],\n      \"references\": [\n        \"DOI:10.4014/jmb.2303.03009\"\
    \n      ],\n      \"assessment\": \"All incident source placements accounted for.\
    \ CFA-linked detailed acid-defense/fitness/efficacy remains UNASSESSED_SCOPE;\
    \ current label/quote/identity only.\"\n    },\n    {\n      \"index\": 7,\n \
    \     \"field_path\": \"causal_graphs[0].nodes[7]\",\n      \"node\": {\n    \
    \    \"node_id\": \"undissociated_weak_acids\",\n        \"label\": \"undissociated\
    \ weak organic acids\",\n        \"node_type\": \"CHEMICAL\",\n        \"description\"\
    : \"Protonated, membrane-permeant form of weak organic acids prevalent at low\
    \ external pH.\"\n      },\n      \"incident_edges\": [\n        4\n      ],\n\
    \      \"references\": [\n        \"DOI:10.1111/1758-2229.70019\"\n      ],\n\
    \      \"assessment\": \"All incident source placements accounted for. Existing\
    \ generic environmental, chemistry or documentary identity context only. No universal\
    \ biological mechanism or exact-bin sufficient cause is inferred.\"\n    },\n\
    \    {\n      \"index\": 8,\n      \"field_path\": \"causal_graphs[0].nodes[8]\"\
    ,\n      \"node\": {\n        \"node_id\": \"weak_acid_influx\",\n        \"label\"\
    : \"weak organic acid influx into cell\",\n        \"node_type\": \"BIOLOGICAL_PROCESS\"\
    ,\n        \"description\": \"Diffusion of undissociated weak organic acids across\
    \ the membrane at low external pH.\"\n      },\n      \"incident_edges\": [\n\
    \        4\n      ],\n      \"references\": [\n        \"DOI:10.1111/1758-2229.70019\"\
    \n      ],\n      \"assessment\": \"All incident source placements accounted for.\
    \ Existing generic environmental, chemistry or documentary identity context only.\
    \ No universal biological mechanism or exact-bin sufficient cause is inferred.\"\
    \n    },\n    {\n      \"index\": 9,\n      \"field_path\": \"causal_graphs[0].nodes[9]\"\
    ,\n      \"node\": {\n        \"node_id\": \"weak_acid_dissociation\",\n     \
    \   \"label\": \"intracellular dissociation of weak organic acids\",\n       \
    \ \"node_type\": \"BIOLOGICAL_PROCESS\",\n        \"description\": \"Dissociation\
    \ of weak acids in the near-neutral cytoplasm, releasing protons.\"\n      },\n\
    \      \"incident_edges\": [\n        5\n      ],\n      \"references\": [\n \
    \       \"DOI:10.1111/1758-2229.70019\"\n      ],\n      \"assessment\": \"All\
    \ incident source placements accounted for. Existing generic environmental, chemistry\
    \ or documentary identity context only. No universal biological mechanism or exact-bin\
    \ sufficient cause is inferred.\"\n    },\n    {\n      \"index\": 10,\n     \
    \ \"field_path\": \"causal_graphs[0].nodes[10]\",\n      \"node\": {\n       \
    \ \"node_id\": \"internal_ph\",\n        \"label\": \"internal (cytoplasmic) pH\"\
    ,\n        \"node_type\": \"QUALITY\",\n        \"description\": \"pH of the cytoplasm.\"\
    \n      },\n      \"incident_edges\": [\n        5\n      ],\n      \"references\"\
    : [\n        \"DOI:10.1111/1758-2229.70019\"\n      ],\n      \"assessment\":\
    \ \"All incident source placements accounted for. Existing generic environmental,\
    \ chemistry or documentary identity context only. No universal biological mechanism\
    \ or exact-bin sufficient cause is inferred.\"\n    },\n    {\n      \"index\"\
    : 11,\n      \"field_path\": \"causal_graphs[0].nodes[11]\",\n      \"node\":\
    \ {\n        \"node_id\": \"h_atpase\",\n        \"label\": \"H+-ATPase proton\
    \ efflux pump\",\n        \"node_type\": \"GENE_OR_PROTEIN\",\n        \"grounding_status\"\
    : \"REVIEWED_LABEL_ONLY\",\n        \"grounding_notes\": \"Reviewed as a contextual\
    \ protein or protein-complex label within a quantitative measurement graph; no\
    \ exact semantic family term was established for this aggregate use.\",\n    \
    \    \"description\": \"ATP-driven proton-exporting ATPase (e.g. P-type H+-ATPase).\"\
    \n      },\n      \"incident_edges\": [\n        6,\n        7\n      ],\n   \
    \   \"references\": [\n        \"DOI:10.3389/fmicb.2023.1149903\",\n        \"\
    DOI:10.3390/microorganisms12030625\"\n      ],\n      \"assessment\": \"All incident\
    \ source placements accounted for. Existing generic environmental, chemistry or\
    \ documentary identity context only. No universal biological mechanism or exact-bin\
    \ sufficient cause is inferred.\"\n    },\n    {\n      \"index\": 12,\n     \
    \ \"field_path\": \"causal_graphs[0].nodes[12]\",\n      \"node\": {\n       \
    \ \"node_id\": \"cytoplasmic_protons\",\n        \"label\": \"cytoplasmic protons\"\
    ,\n        \"node_type\": \"CHEMICAL\",\n        \"description\": \"Protons (hydrons)\
    \ within the cytoplasm.\"\n      },\n      \"incident_edges\": [\n        6\n\
    \      ],\n      \"references\": [\n        \"DOI:10.3389/fmicb.2023.1149903\"\
    \n      ],\n      \"assessment\": \"All incident source placements accounted for.\
    \ Existing generic environmental, chemistry or documentary identity context only.\
    \ No universal biological mechanism or exact-bin sufficient cause is inferred.\"\
    \n    }\n  ]\n}"
- assessment_id: expression
  area: evidence
  topic: 'Native checklist: exact canonical catalog applicability'
  outcome: unknown
  target_ids:
  - METPO:1000460
  summary: The actual retained 20-organism/28-dataset catalog has no exact match for
    Acidithiobacillus ferrooxidans or its three official retained synonyms. This bounded
    catalog result is not global expression-data absence. No organism or strain substitution,
    detailed module query or phenotype inference is made.
  evidence_ids:
  - expression
  - authority-reuse
  - taxonomy-reuse
  details: "{\n  \"completed_at\": \"2026-10-21T19:57:19.764268+00:00\",\n  \"canonical_taxon\"\
    : \"NCBITaxon:920\",\n  \"status\": \"NO_MATCH_IN_RETAINED_CANONICAL_CATALOG\"\
    ,\n  \"catalog_check\": {\n    \"checked_at\": \"2026-10-21T19:55:46.535616+00:00\"\
    ,\n    \"catalog_path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-grounding-agent/reused-datasets.json\"\
    ,\n    \"catalog_sha256\": \"155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693\"\
    ,\n    \"original_access_receipt\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-grounding-agent/reused-catalog-accesses.json\"\
    ,\n    \"canonical_taxon\": \"NCBITaxon:920\",\n    \"names\": [\n      \"Acidithiobacillus\
    \ ferrooxidans\",\n      \"Ferrobacillus ferrooxidans\",\n      \"Ferrobacillus\
    \ sulfooxidans\",\n      \"Thiobacillus ferrooxidans\"\n    ],\n    \"organisms\"\
    : 20,\n    \"datasets\": 28,\n    \"matches\": [],\n    \"scope\": \"Exact supplied\
    \ canonical species and official retained synonyms only. No substitute organism,\
    \ strain or detailed gene/module query.\"\n  },\n  \"assessment\": \"None of the\
    \ exact current species name or three official retained synonyms matches the retained\
    \ 20-organism, 28-dataset catalog. This bounded catalog absence is not a claim\
    \ about all public expression data. No other species or strain is substituted.\"\
    ,\n  \"downstream_gene_module_queries\": \"NOT_RUN\",\n  \"protein_instances\"\
    : 0,\n  \"uniprot_instance_audit\": \"NOT_APPLICABLE\",\n  \"scope\": \"Identity/applicability\
    \ only; no detailed acid-defense, stress, fitness or AMR queries.\"\n}"
- assessment_id: ownership
  area: provenance
  topic: 'Native checklist: direct writers and replay limits'
  outcome: supported
  target_ids:
  - METPO:1000460
  summary: Seeder owns exact-alias import. Permeability migration directly maintains
    QUALITY, while its edge rewrite is restricted to maximal-growth-rate enables and
    cannot repair current decreases. Shared predicate grounder skips nonempty IDs.
    Historical confers writer was whole-read only after the successful 83-input supplement;
    its old-RO2327 selection does not replay current confers. Current exports likewise
    does not match the old migration key.
  evidence_ids:
  - owners
  - ground-reading
  - local-authority
  - capture
  details: "{\n  \"completed_at\": \"2026-10-21T19:57:19.764268+00:00\",\n  \"target\"\
    : \"data/traits/environment/ph_range_low.yaml\",\n  \"owners\": [\n    {\n   \
    \   \"path\": \"data/traits/environment/ph_range_low.yaml\",\n      \"locators\"\
    : [\n        \"causal_graphs[0].edges[3]\"\n      ],\n      \"role\": \"Maintained\
    \ current assertion; other records with the same node are not automatically owners.\"\
    ,\n      \"sha256\": \"56a1489044011c883b75e007e5eb0d6a67984b791e77d8f02cf70c64e7fccff0\"\
    \n    },\n    {\n      \"path\": \"mappings/predicate_grounding.tsv\",\n     \
    \ \"locators\": [\n        \"61\",\n        \"91\",\n        \"102\"\n      ],\n\
    \      \"role\": \"Exact decreases-to-RO2212, exports and confers rows. Wildcard\
    \ local gates do not remove imported RO semantics.\",\n      \"sha256\": \"8e28c19e93aca3dc164a3befbe2612b289241de457c59f499e65936c03b7ce52\"\
    \n    },\n    {\n      \"path\": \"scripts/ground_causal_predicates.py\",\n  \
    \    \"locators\": [\n        \"136\\u2013180\"\n      ],\n      \"role\": \"\
    Grounds only empty predicate_id fields. The populated current relation is skipped,\
    \ so changing a mapping row alone does not rewrite it.\",\n      \"sha256\": \"\
    5a788eeaabf3a56b0d82c469a3e3fe28f1d51707d9382313b9a94289be7d1381\"\n    },\n \
    \   {\n      \"path\": \"scripts/migrate_process_quality_consistency.py\",\n \
    \     \"locators\": [\n        \"77\\u201392\",\n        \"148\\u2013207\"\n \
    \     ],\n      \"role\": \"Direct proton_permeability QUALITY normalization owner.\
    \ Its relation rewrite is restricted to maximal_growth_rate enables edges; it\
    \ does not repair this current decreases edge.\",\n      \"sha256\": \"1a83ad3dba79ed0c958b875a6fcc4b9e562259af26da2f248d32d5cf7784f80a\"\
    \n    },\n    {\n      \"path\": \"scripts/migrate_node_type_consistency.py\"\
    ,\n      \"locators\": [\n        \"54\\u201368\",\n        \"135\\u2013168\"\n\
    \      ],\n      \"role\": \"Direct PMF STATE normalization owner; positive context,\
    \ not an additional current defect.\",\n      \"sha256\": \"a3e7bc170e60f406a73e06c893d74f5253671028d3d40cc15ecf882b6684a69e\"\
    \n    },\n    {\n      \"path\": \"mappings/node_grounding.tsv\",\n      \"locators\"\
    : [\n        \"44\"\n      ],\n      \"role\": \"Current PMF STATE-to-local-class\
    \ grounding owner.\",\n      \"sha256\": \"d7de9b3ab04960c4775a5bc295a945bd1a72d81467830459f4793e654f82b3d0\"\
    \n    },\n    {\n      \"path\": \"scripts/seed_from_metpo.py\",\n      \"locators\"\
    : [\n        \"198\\u2013209\",\n        \"333\\u2013348\"\n      ],\n      \"\
    role\": \"Direct alias import owner, preserving upstream synonym types. Scientific\
    \ exactness is a separate question.\",\n      \"sha256\": \"0fb9c9f7ea6a8f137eecd5c319775b511c398dba6158c81b1fbfb94210f7d851\"\
    \n    },\n    {\n      \"path\": \"scripts/migrate_enables_trait_edges.py\",\n\
    \      \"locators\": [\n        \"77\\u201399\",\n        \"123\\u2013162\",\n\
    \        \"231\\u2013262\"\n      ],\n      \"role\": \"Historical confers migration\
    \ owner, read only after supplemental capture. It selects old RO2327 edges with\
    \ TRAIT objects; already-current confers is not selected on replay.\",\n     \
    \ \"sha256\": \"a5e7965ee4f6b6ba5bae3a06bced2a83cbf755f3b9b150ce6acc0cd808cb1d88\"\
    \n    },\n    {\n      \"path\": \"scripts/migrate_remaining_microbe_domain_edges.py\"\
    ,\n      \"locators\": [\n        \"57\\u201389\",\n        \"92\\u2013121\"\n\
    \      ],\n      \"role\": \"Historical exports migration owner. Selection requires\
    \ the old METPO2000209 plus exports key; current METPO2007804 is not selected\
    \ on replay.\",\n      \"sha256\": \"110542d49e25007122c7c254966ad87dc3f7f054358766e933aff89e8ef0a994\"\
    \n    }\n  ],\n  \"search\": {\n    \"ignored_hidden_included\": true,\n    \"\
    matching_paths\": 215,\n    \"parsed_review_target_arrays\": 67,\n    \"exact_target_arrays\"\
    : 0,\n    \"excluded\": [\n      \".git/**\",\n      \".venv/**\"\n    ],\n  \
    \  \"scope\": \"Entire owned repository including ignored/hidden files, excluding\
    \ Git internals and virtual environment. Exact target identity/slug/label and\
    \ numerical synonym; broad physiological aliases are not treated as exact target\
    \ signoff.\"\n  },\n  \"all_node_search\": {\n    \"nodes\": 13,\n    \"captured_history_leads\"\
    : 8,\n    \"uncaptured_history_leads\": 0\n  },\n  \"whole_histories_read\": [\n\
    \    \"history/infrastructure/inconsistent-node-type/2026-08-12T000912Z-claude-code-779670.yaml\"\
    ,\n    \"history/infrastructure/node-type-consistency/2026-08-15T014631Z-claude-code-9d7f4d.yaml\"\
    ,\n    \"history/infrastructure/pathway-vs-process/2026-08-16T010630Z-claude-code-192557.yaml\"\
    ,\n    \"history/infrastructure/predicate-gate-audit/2026-08-16T074719Z-claude-code-84d88d.yaml\"\
    ,\n    \"history/infrastructure/process-quality-consistency/2026-08-21T073211Z-codex-174227.yaml\"\
    ,\n    \"history/other/canonical-examples-batch1/2026-08-20T074839Z-claude-code-6fb2f5.yaml\"\
    ,\n    \"history/other/canonical-examples-six/2026-08-21T065406Z-codex-a1ab82.yaml\"\
    ,\n    \"history/records/ph_range_mid2/2026-09-04T024000Z-codex-3036b8.yaml\"\n\
    \  ],\n  \"history_disposition\": \"All eight history files were read in full.\
    \ All actors are AI. The canonical-examples-six history explicitly mentions recovery\
    \ of this record\\u2019s exemplar while preserving newer fields; it is positive\
    \ target-specific curation context, not human acceptance. Infrastructure migrations\
    \ and ph_range_mid2 history are direct family or sibling context, not independent\
    \ exact-target signoff.\",\n  \"record_events\": {\n    \"total\": 12,\n    \"\
    ai\": 11,\n    \"seed\": 1\n  },\n  \"human_traceability\": \"Within the bounded\
    \ ignored-inclusive search, 67 actual structured-review target arrays contain\
    \ no exact target array. Current REVIEWED status and AI curation do not establish\
    \ a linked human acceptance; this does not claim that no human ever reviewed the\
    \ record.\",\n  \"report\": {\n    \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/repo/research/traits/environment/ph_range_low-deep-research-falcon.md\"\
    ,\n    \"sha256\": \"a9d2d36a3b7e1cbe5d6cb6dab50577315df72fc835514366d60c0f087238ab13\"\
    ,\n    \"bytes\": 38451,\n    \"reading_scope\": \"Only frontmatter and initial\
    \ target/template context, lines 1\\u201370, were read as generated provenance/lead\
    \ material. August 4 02:53:08.192544\\u201303:01:36.402669 generation is not proof\
    \ of the exact June 23 enrichment version. No report mechanism or intervention\
    \ recommendation is adopted.\"\n  },\n  \"context_only\": \"Shared PMF/permeability\
    \ hits in ph_delta/ph_phenotype/ph_range_mid2 writers are sibling context. No\
    \ exact current canonical insertion script was established by the bounded searches;\
    \ the actual historical canonical-six receipt is retained instead.\",\n  \"capture_chronology\"\
    : {\n    \"path\": \"/private/tmp/traitmech-record-sweep-011.m6s8p2ra/ph-range-low-grounding-agent/capture-supplement-verification.json\"\
    ,\n    \"sha256\": \"8f0f152275089fd1658c89af99c883144a11f325acfbd0076b910f4d650702a7\"\
    ,\n    \"bytes\": 1015\n  }\n}"
- assessment_id: human-acceptance
  area: provenance
  topic: 'Native checklist: bounded local acceptance traceability'
  outcome: concern
  target_ids:
  - METPO:1000460
  summary: The record has eleven AI-assisted events plus seed. Ground auditor whole-read
    eight AI history contexts; target-specific canonical recovery remains positive
    curation provenance. Ignored-inclusive search returned 215 paths and 67 actual
    review arrays, none exact to this target. These facts and REVIEWED status do not
    establish a linked current human acceptance; private/remote absence is not asserted.
  evidence_ids:
  - owners
  - playbook
  - identity
  - challenge
  - adjudication
- assessment_id: readiness
  area: consistency
  topic: 'Native checklist: actual gates and 82-to-83 chronology'
  outcome: supported
  target_ids:
  - METPO:1000460
  summary: Original 82 inputs remain unchanged in the separately retained final 83-input
    capture. All frozen artifacts match and focused native/strict/snippet checks passed.
    Original common diagnostic failures/skips/retries and B10 QC times remain qualified
    reuse, not new B11 runs. Source zero hit and publisher-access failures remain
    distinct from native success.
  evidence_ids:
  - capture
  - initial-capture
  - supplement-command
  - source-capture
  - reuse
  - reuse-postcheck
  - native-checks
  - check-ph-range-low-native
  - check-ph-range-low-strict
  - check-ph-range-low-snippets
findings:
- finding_id: category-versus-complete-interval
  issue_key: ph-range-low-category-versus-complete-interval
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Broad acidophile categories are exact aliases for a numerical interval
  description: The four broad category aliases are not coextensive with a complete
    4–6 growth interval. Assigned environmental sources distinguish optimum-based
    categories from growth ranges, including moderate ranges extending outside 4–6
    and extreme growth below 3. Preserve active numeric identity, source-specific
    cutoff conventions and generic acidic physiology; the inspected passages are not
    exhaustive definitions of every facultative or obligate term.
  target_ids:
  - METPO:1000460
  field_paths:
  - synonyms[0]
  - synonyms[1]
  - synonyms[2]
  - synonyms[3]
  evidence_ids:
  - bin-scope
  - body-acid-genomes
  - body-krulwich
  - meta-baker
  - metpo-primary
  - owners
  - challenge
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_range_low.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: scripts/seed_from_metpo.py
    role: Direct importer preserves upstream exact/related synonym types; scientific
      equivalence is independently assessed.
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: regulation-endpoints
  issue_key: ph-range-low-regulation-endpoints
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Process-regulation relation links a chemical to a measured quality
  description: Current edge 3 asserts RO2212 between material cyclopropane fatty acids
    and permeability QUALITY. Its inherited RO2211 process domain and range do not
    describe those explicit referents. This is a formal representation issue; the
    source fragment occurrence does not validate excluded pathogen-defense efficacy,
    and no false biological meaning or mechanistic repair is inferred.
  target_ids:
  - METPO:1000460
  field_paths:
  - causal_graphs[0].edges[3]
  evidence_ids:
  - node-edges
  - ro-primary
  - schema
  - body-cfa
  - owners
  - challenge
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_range_low.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Decreases mapping context; wildcard native gates do not remove imported
      process/process semantics.
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Skips existing nonempty predicate IDs; changing the table alone does not
      rewrite this populated edge.
  - repository: CultureBotAI/TraitMech
    path: scripts/migrate_process_quality_consistency.py
    role: Direct permeability QUALITY maintainer; relation rewrite is restricted to
      maximal-growth-rate enables, not current decreases.
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: major
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: unmarked-note-omission
  issue_key: ph-range-low-unmarked-note-omission
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Quoted note omits an intervening parenthesis without an ellipsis
  description: The assigned generic PMF/ATP sentence contains an intervening parenthetical
    that the current edge 2 quotation omits without a marker. Its biological meaning
    remains supported; clarify literal quotation precision. Explicitly marked abridgments
    in notes 4 and 7 are separate and are not called false quotations.
  target_ids:
  - METPO:1000460
  field_paths:
  - causal_graphs[0].edges[2].evidence[0].notes
  evidence_ids:
  - quoted-notes
  - body-bioenergetics
  - playbook
  - challenge
  - adjudication
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_range_low.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
- finding_id: human-acceptance-link
  issue_key: ph-range-low-human-acceptance-link
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Current local provenance lacks an attributable acceptance link
  description: Eleven AI events plus seed, eight AI history contexts and REVIEWED
    status do not independently identify current human acceptance. The retained ignored-inclusive
    search and 67 parsed review arrays bound this traceability concern; no private
    or remote absence is asserted.
  target_ids:
  - METPO:1000460
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
    path: data/traits/environment/ph_range_low.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  rule_id: review-yaml-record Evidence Rules; native field-by-field checklist
  native_severity: minor
  normalization_reason: Major denotes material claim/source or representation errors;
    minor denotes bounded provenance or wording defects.
actions:
- action_id: reconcile-category-aliases
  description: Reconcile the four exact category aliases with the intended complete-interval
    bin during separately authorized curation.
  finding_ids:
  - category-versus-complete-interval
  target_ids:
  - METPO:1000460
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_range_low.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: scripts/seed_from_metpo.py
    role: Direct importer preserves upstream exact/related synonym types; scientific
      equivalence is independently assessed.
  acceptance_checks:
  - Retain faithful upstream import provenance, active numeric identity and per-source
    cutoff differences.
  - Do not invent exhaustive facultative/obligate definitions, require a new canonical
    or duplicate this scope issue across contextual statements.
  - Use guarded history, appropriate native/strict/source checks and a successor review
    after changed inputs.
- action_id: reconcile-regulation-role
  description: Reconcile the current edge 3 relation with its explicit material and
    quality referents.
  finding_ids:
  - regulation-endpoints
  target_ids:
  - METPO:1000460
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_range_low.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  - repository: CultureBotAI/TraitMech
    path: mappings/predicate_grounding.tsv
    role: Decreases mapping context; wildcard native gates do not remove imported
      process/process semantics.
  - repository: CultureBotAI/TraitMech
    path: scripts/ground_causal_predicates.py
    role: Skips existing nonempty predicate IDs; changing the table alone does not
      rewrite this populated edge.
  - repository: CultureBotAI/TraitMech
    path: scripts/migrate_process_quality_consistency.py
    role: Direct permeability QUALITY maintainer; relation rewrite is restricted to
      maximal-growth-rate enables, not current decreases.
  acceptance_checks:
  - Preserve the distinction between formal role semantics and excluded biological
    efficacy; do not force a new pathway or mechanism.
  - Account for nonempty-ID preservation and the limited relation rewrite in the quality
    maintainer.
  - Use appropriate guarded curation/history and follow-up review rather than assuming
    table edits rewrite populated edges.
- action_id: clarify-quoted-note
  description: Mark the omitted parenthetical or use an accurate contiguous quotation
    in the edge 2 note.
  finding_ids:
  - unmarked-note-omission
  target_ids:
  - METPO:1000460
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_range_low.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Keep positive source meaning and exact attribution.
  - Keep the native snippet and quoted-note denominators separate; no biological correction
    or optimization is needed.
- action_id: link-human-acceptance
  description: Link attributable acceptance of the current record if available, or
    clarify status while preserving provenance.
  finding_ids:
  - human-acceptance-link
  target_ids:
  - METPO:1000460
  owner_paths:
  - repository: CultureBotAI/TraitMech
    path: data/traits/environment/ph_range_low.yaml
    role: Maintained scientific input; authorized changes require guarded curation
      and history
  acceptance_checks:
  - Retain actual AI/seed and bounded local search evidence.
  - No contact with others or automatic status promotion is authorized.
limitations:
- Detailed pathogen acid-defense, fitness, AMR and yeast perturbation/engineering/optimization
  efficacy remain UNASSESSED_SCOPE. No biological repair or improved experimental
  conditions are supplied.
- Assigned canonical DOI is a verified LAB review, with a retained Europe PMC zero
  hit and successful Crossref identity. Its inspected abstract does not establish
  the named species or complete 4–6 interval; publisher full body unavailable is not
  whole-paper absence or false growth. Follow-up support or qualification is needed,
  without a forced finding solely from access failure.
- Baker full body and its PMF schema snippet remain unknown. Generic homeostasis does
  not independently calibrate the exact complete bin.
- Per-source acidophile cutoffs and optimum-versus-range distinctions are preserved;
  inspected classification is not an exhaustive definition of every facultative/obligate
  term.
- PMF STATE, ATP-formation process, permeability/internal-pH QUALITY and the other
  material facets are coherent. Free-text relations acquire no invented imported domain
  constraints; RO2326 edge 7 and local confers/exports fit current referents.
- No mandatory accession, connector, additional pathway or canonical substitute follows
  from this NONMECHANISTIC graph or its five components.
- Three schema snippets and six quoted-note fields remain distinct. CFA exact fragment
  matching is documentary only; marked ellipses are separate from edge 2 unmarked
  omission.
- The original 82-input capture is unchanged. The exact historical enables-to-trait
  writer was added by separate successful 83-input capture and interpreted afterward;
  final review input is the supplement.
- Eight whole-history readings belong to grounding; root/source reading scopes are
  separately receipted. Generated report lead does not establish the exact version
  used for earlier enrichment.
- Source acquisitions, current copies and actual readings retain their own times.
  Prior bioenergetics copy was discovered, but a fresh body was also acquired and
  is accurately identified as such.
- Exact catalog nonmatch for the supplied canonical is bounded to retained catalog
  bytes, not all public expression data; no substitute or downstream efficacy query.
notes:
- Final root/challenge guards are pinned. This serializer remains unexecuted during
  preparation; root owns one serialization after independent static review, native
  validation, final artifact review and save.
- 'Source coverage: seven assigned works, eleven external placements, thirteen nodes/eight
  edges, one canonical, three snippet fields and six quoted-note fields.'
- Preparation changes no scientific record, Git state, sweep state or native inventory.
tags:
- record-review
- ph-range-low
- environment
- needs-curation
native_verdict: needs_curation
```
