# Homothallism: METPO Proposal v486

## Context

Lift `traitmech:000609 homothallism`, a PROPOSED PHYSIOLOGY class.
Whole-repository searches included ignored and hidden files, labels, synonyms,
citations, graph nodes, discussions, research, proposals, pages and history.
No exact record was found. Heterokaryosis mentions self-fertility only as a
nonrequired property; it has no exact unresolved node or synonym to migrate.
Ploidy, hyphal fusion and parasexuality describe distinct traits.

The pinned 12,617-triple METPO graph contains no matching term. A fresh
399-record seed reconciled against the 1,003-record pre-addition corpus
has 344 present and 55 absent IDs. Both frozen release-review tables classify
those 55 as 38 supporting-field rows and 17 duplicates, not missing primary
traits. An all-state upstream issue search for homothall returned no result
on 2026-10-04; current open local PRs do not reserve this trait or block.

## Scope

| Scope | Count | Parent | Leaves |
| --- | ---: | --- | ---: |
| A: synthetic trait | 1 | METPO:1000059 phenotype | 1 |
| B: predicates | 0 | Not applicable | 0 |
| C: schema enums | 0 | Not applicable | 0 |

## Hierarchy Decisions

Use released `METPO:1000059 phenotype`, under `METPO:1000188 quality`, in
the pinned ontology's `https://w3id.org/metpo/` namespace. PHYSIOLOGY is a
filesystem category, not an ontology parent. The single-spore operational
definition accommodates different nuclear and mating-locus mechanisms;
it does not require a uninucleate spore or both MAT idiomorphs in one nucleus.
It neither forbids outcrossing nor requires obligate sexuality or universal
compatibility. Heterokaryosis, ploidy, hyphal fusion and parasexuality are
not is-a parents. No exact synonyms, xrefs or SSSOM mappings are asserted:
the scope of self-fertility/self-compatibility beyond fungi remains explicit.

## Evidence and Limitations

- `DOI:10.5598/imafungus.2015.06.01.13` (`PMID:26203424`) provides the
  historical operational definition and umbrella terminology. The snippet
  is from the directly read Introduction, not the abstract. This review is
  definition authority, not experimental replication.
- `DOI:10.1371/journal.pgen.1006981` (`PMID:28892488`) supplies a scientific
  abstract snippet and primary self-fertility evidence. Nuclear-level
  heterothallism can underlie organism-level self-fertility. Reference-strain
  natural provenance, most main-text experiments and supplements remain
  unverified; no canonical taxon is inferred from this study.
- `DOI:10.7554/elife.79114` (`PMID:35713948`) supplies a scientific-abstract
  clause checked directly in full-text XML, independently of the abstract
  resolver. Europe PMC returns the eLife digest instead. Figures 5 and 8
  were visually inspected from publisher version 2 assets; Supplementary
  file 1 was read with a structured spreadsheet reader. Wild-type CBS7841
  sporulation is separate from derivative-strain genetic assays. The
  record does not turn the digest's universal-compatibility wording into
  a trait requirement. Other figures and supplements remain uninspected.

The qualified example is active `NCBITaxon:1295531 Cryptococcus depauperatus
CBS 7841`. ATCC 36983 documents natural collection provenance, not a second
trait experiment. Two CURATION_TODOs retain lexical, mechanistic and readout
limits. No protein-resolved graph is asserted.

## ID Space and Subset

Reserve `METPO:1056300` in `1056300-1056399`, after v485's block.
Ignored-and-hidden searches across this repository and CommunityMech
proposals found no collision before writing, including the CommunityMech
v1 ranges. Subset: `metpo_traitmech_2026_10`. Keep local `traitmech:000609`
pending upstream acceptance and release.

## Files

| Artifact | Rows | Purpose |
| --- | ---: | --- |
| `metpo_proposal_classes_robot.tsv` | 1 class + 2 headers | Scope-A lift |
| `proposal.md` | Not applicable | Scope, evidence and migration |

No property or SSSOM template is needed. The 11-column class template follows
the upstream headers with three trailing empty directive cells. The upstream
contract is pinned to Knowledge-Graph-Hub/kg-microbe commit
`1408e7099d039026d7611c240938d8e177753406`.

## Verification

```bash
just verify-proposal metpo_traitmech_v486
just robot-validate-proposal metpo_traitmech_v486
just audit-proposal-coverage
just qc
```

Check record/template label, definition and parent parity. Inspect emitted
OWL for the released w3id phenotype parent and quality ancestor; an ELK
pass against a legacy OBO parent stub is insufficient. Keep abstract resolver
outcomes separate from manual full-text exact-span checks.

## Upstream Path

Submit the validated class template to `berkeleybop/metpo` following local
review. The reserved placeholder does not imply upstream acceptance.

## Round-Trip Plan

After acceptance and release, update the pinned ontology and migrate to
the accepted METPO CURIE. Preserve the local identifier in an explicit
migration artifact and append-only history, regenerate dependent artifacts,
and avoid creating a duplicate primary record.

## Change Log

- v486, 2026-10-04: propose homothallism with three source snippets and a
  qualified natural-strain example.
