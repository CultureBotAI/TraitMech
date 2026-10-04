# Phototaxis: METPO proposal v465

## Context

TraitMech mints `traitmech:000588 phototaxis` as a PROPOSED organismal
disposition, not a source-specific observation or receptor family. Three
primary papers support the directional phenotype and a qualified exemplar.
This closes the light-direction gap beside photokinesis and other motility
responses without asserting a universal photoreceptor or motility apparatus.

The fresh temporary seed has 399 identifiers: 344 are present and 55 absent
in the pre-change 982-record corpus. The frozen release-delta table marks
`METPO:1000241` as `NOT_SEEDED_DEPRECATED`. Live OWL confirms that it has no
definition or replacement. It is not revived, reused or declared replaced.

Whole-repository novelty searches included ignored and hidden files, exact
labels and variants, directional-light phrases, all three DOI/PMID pairs,
the local identifier, proposal cohort and placeholder block. Existing hits
are obsolete OWL copies and boundary discussions/research in motile,
photokinesis, phototrophy, photosynthesis and photoorganoheterotrophy. None
is an exact current record, synonym or ungrounded exact causal node needing
reconciliation. An upstream issue search for phototaxis returned no result.

## Scope

| Scope | Rows | Parent | Leaves |
| --- | ---: | --- | ---: |
| A: local trait lift | 1 | METPO:1000702 motile | 1 |
| B: predicates | 0 | Not applicable | 0 |
| C: schema enums | 0 | Not applicable | 0 |

Only one trait uses this new local identity. No predicate or schema enum
requires a proposal in this change.

## Hierarchy Decisions

The parent `METPO:1000702 motile` is active and denotes independent powered
locomotion. Phototaxis adds a directional response to illumination; it does
not require flagella, pili, swimming rather than surface movement, one
receptor, or positive rather than negative movement. No closer active taxis
parent was found. Photokinesis is not a parent or synonym: speed modulation
alone is insufficient. Photosynthesis and phototrophy concern different axes.

No external equivalent xref or SSSOM mapping is asserted. Biological-process
terms require a separate scope comparison with this organismal disposition.

## Evidence

- Schuergers et al., DOI:10.7554/eLife.12620, PMID:26858197: current publisher
  version 2 (2022-04-22), original publication 2016-02-09. Version-specific
  XML: https://cdn.elifesciences.org/articles/12620/elife-12620-v2.xml.
  Figure 1, methods and both optical supplements were inspected. The entry
  retains directional movement under oblique RGB illumination and the
  projected-gradient control. torA-gfp optical assays and the hypothetical
  PixJ1 signaling model are separate. Two supplement graphic/caption
  discrepancies remain documented, not silently corrected.
- Berthold et al., DOI:10.1105/tpc.108.057919, PMID:18552201: abstract snippet
  exact-matched at Europe PMC; PMC introduction and beginning of Results
  inspected. It distinguishes directional movement from photophobic reversal
  and identifies cell-wall-deficient CW2. Remaining full text/supplements
  were not inspected. No natural algal exemplar is asserted.
- Trautmann et al., DOI:10.1093/dnares/dss024, PMID:23069868: full-text
  Methods 2.1, Results 3.1 and Discussion establish the PCC-M lineage and
  native positive response while documenting laboratory microevolution and
  its lack of blue-light phototaxis. NCBI resolved `NCBITaxon:1148` to
  `Synechocystis sp. PCC 6803`; the example is explicitly PCC-M-qualified,
  not a universal phenotype of all descendants or an exact substrain ID.

All three evidence snippets were exact-matched to authoritative source text.
The record remains PROPOSED pending human curation. Protein-resolved causal
graphs and external mappings remain open discussions, not implied results.

## ID Space And Subset

Reserve `METPO:1054200` in the new 100-wide block 1054200-1054299, following
v464's block 1054100-1054199. Ignored-and-hidden searches found no collision
in this repository. The live CommunityMech v1 cohort has 96 class rows through
1008013 and 19 property rows through 2008002, disjoint from this block.
Subset: `metpo_traitmech_2026_10`. The METPO identifier remains an unaccepted
proposal placeholder; the record continues to use `traitmech:000588`.

## Files

| Artifact | Rows |
| --- | ---: |
| metpo_proposal_classes_robot.tsv | 1 class plus two header rows |
| Properties template | Omitted: no properties |
| SSSOM mappings | Omitted: no verified equivalent alignment |
| proposal.md | This narrative |

## Verification

The maintained proposal verifier and ROBOT template/merge/ELK validation
passed (23,328 merged and 23,334 reasoned triples, no unsatisfiable classes).
The guarded writer emits the canonical 11-column class header, including
three trailing empty ROBOT directive cells. Nine focused writer tests passed,
covering record/template identity, evidence boundaries, dry run, idempotence
and fail-closed handling of changed outputs. LinkML and strict record
validation passed. All three snippets were directly exact-matched; the
abstract resolver verified Berthold and correctly left the two full-text
quotes inconclusive. NCBI taxonomy resolution passed with no new-record
warning. Corpus QC, full-suite and generated-artifact results are recorded
in the PR receipt. Embeddings were not regenerated because neither exact
configured source path was available.

## Upstream Path

After review, submit the ROBOT class TSV to berkeleybop/metpo or the
KG-Microbe proposal pipeline. Maintainers must decide the intended treatment
of obsolete phototaxis independently; this cohort does not alter that class.

## Round-Trip Plan

After upstream acceptance, refresh the pinned METPO ontology and seed to a
temporary tree. Migrate the record to the actual accepted CURIE, preserve
the local identifier in traceability metadata, and reconcile references and
proposal status through a separately reviewed change. Do not publish the
placeholder as an accepted identity before that migration.

## Change Log

- v465, 2026-10-04: one evidence-backed phototaxis class, curated by codex.
