# Aerotaxis: METPO proposal v466

## Context

TraitMech mints `traitmech:000589 aerotaxis` as a PROPOSED organismal
disposition with three primary DOI citations and verbatim evidence snippets.
It denotes oxygen-directed locomotion, not oxygen consumption, growth
preference, tolerance, a receptor family or a source-specific assay row.

The fresh temporary seed has 399 identifiers, 344 present and 55 absent in
the pre-change 983-record corpus. Structured review of the frozen release
tables and current OWL found no exact aerotaxis class. Whole-repository
searches included ignored and hidden files, lexical variants, oxygen-directed
phrases, citations, the new local ID and the entire placeholder block.
Neighboring research mentions aerotaxis, but no exact current record,
synonym or causal node needs reconciliation. Magnetoaerotaxis is related
to magnetotaxis in v53, not an equivalent of generic aerotaxis. An upstream
METPO issue search for aerotaxis returned no result.

## Scope

| Scope | Rows | Parent | Leaves |
| --- | ---: | --- | ---: |
| A: local trait lift | 1 | METPO:1000702 motile | 1 |
| B: predicates | 0 | Not applicable | 0 |
| C: schema enums | 0 | Not applicable | 0 |

One trait uses the new local identity. No predicate or enum needs lifting.

## Hierarchy Decisions

The active parent `METPO:1000702 motile` denotes independently powered
locomotion. No closer active METPO taxis class was found. The existing local
chemotaxis definition requires flagellar motor switching, so it is not used
to impose a universal apparatus. Aerotaxis covers attraction and repulsion
relative to preferred oxygen conditions; it does not require either a
positive gradient response at every concentration or both signs in every
organism. Nondirectional speed changes and oxygen growth requirements are
separate axes. Magnetic alignment is neither necessary nor sufficient.

No external equivalent xref or SSSOM mapping is asserted. A biological
process term is not automatically an exact organismal-disposition mapping.

## Evidence

- Shioi et al., DOI:10.1128/jb.169.7.3118-3123.1987, PMID:3036771:
  authoritative abstract supports high-oxygen repulsion as well as the
  contrast with lower-oxygen attraction. Full text was not inspected.
- Zhulin et al., DOI:10.1128/jb.178.17.5199-5204.1996, PMID:8752338:
  authoritative abstract supports return toward a preferred oxygen interval.
  The proton-motive-force signaling interpretation remains a hypothesis;
  no molecular causal graph or strain exemplar is inferred. Full text was
  not inspected.
- Bouvard et al., DOI:10.1103/PhysRevE.106.034404: published version dated
  2022-09-15, full text including appendices read from the author's copy at
  https://www.fast.universite-paris-saclay.fr/~moisy/papers/2022_bouvard_pre.pdf.
  Figures 1-2 and the mathematical snippet were visually checked. The
  canonical example remains qualified to the unnamed environmental strain
  and motile subpopulation; `NCBITaxon:488447` is species-level, not an
  isolate accession. The earlier preprint is not mixed into this evidence.

Protein-resolved mechanisms, exact isolate identity and external mappings
remain explicit open discussions. The record remains PROPOSED pending
human curation, not REVIEWED merely because automated checks pass.

## ID Space And Subset

Reserve `METPO:1054300` in block 1054300-1054399, following v465's block
1054200-1054299. Ignored-and-hidden searches found no collision. The live
CommunityMech v1 cohort has 96 class rows through 1008013 and 19 property
rows through 2008002, disjoint from this block. The subset is
`metpo_traitmech_2026_10`. This is an unaccepted placeholder, not the
record's public identity; that remains `traitmech:000589`.

## Files

| Artifact | Rows |
| --- | ---: |
| metpo_proposal_classes_robot.tsv | 1 class plus two header rows |
| Properties template | Omitted: no properties |
| SSSOM mappings | Omitted: no verified equivalent alignment |
| proposal.md | This narrative |

## Verification

The maintained proposal verifier and ROBOT template/merge/ELK validation
passed (23,328 merged and 23,334 reasoned lines, no unsatisfiable classes).
Nine focused writer tests passed, covering scope, proposal parity, dry run,
idempotence and fail-closed output guards. LinkML and strict record checks
passed. All three snippets were directly exact-matched; the abstract
resolver verified two and correctly left the published full-text quote
inconclusive. NCBI resolved the new example without warnings. Desktop and
mobile browser checks passed. Full-suite, corpus QC and generated-artifact
results are recorded in the PR receipt. Embeddings were not regenerated
because neither exact configured source path was available. The writer
preserves the canonical 11-column class template, including the three
trailing empty ROBOT directive cells.

## Upstream Path

After review, submit the class TSV to berkeleybop/metpo or the KG-Microbe
proposal pipeline. The placeholder must not be exported as an accepted ID.

## Round-Trip Plan

After upstream acceptance, refresh the pinned ontology and seed a temporary
tree. Migrate to the actual accepted CURIE, preserve the local identifier
in traceability metadata, and reconcile references and proposal status in
a separately reviewed change.

## Change Log

- v466, 2026-10-04: one evidence-backed aerotaxis class, curated by codex.
