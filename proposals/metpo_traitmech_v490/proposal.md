# Unisexual Reproduction: METPO Proposal v490

## Context

Lift `traitmech:000613 unisexual reproduction`, a PROPOSED PHYSIOLOGY class.
Whole-repository novelty searches included ignored and hidden files, labels,
synonyms, citations, graph nodes, discussions, research, proposals, pages and
history. Existing homothallism mentions unisexuality but has no exact synonym
or unresolved same-scope node. No exact record was found.

The pinned 12,617-triple METPO graph has no exact term. A fresh 399-record
seed compared with the 1,007-record pre-addition corpus has 344 present and
55 absent IDs. Both frozen release-review tables classify those 55 as
38 supporting-field rows and 17 duplicates, not missing primary traits.
An all-state upstream issue search for unisexual returned no results on
2026-10-04. Current open local PRs reserve neither this trait nor its block.

## Scope

| Scope | Count | Parent | Leaves |
| --- | ---: | --- | ---: |
| A: synthetic trait | 1 | METPO:1000059 phenotype | 1 |
| B: predicates | 0 | Not applicable | 0 |
| C: schema enums | 0 | Not applicable | 0 |

## Hierarchy Decisions

Both record and template use released `METPO:1000059 phenotype`, under
`METPO:1000188 quality`, in the pinned `https://w3id.org/metpo/` namespace.
PHYSIOLOGY is a filesystem category, not an ontology parent. Obsolete
reproduction-process and reproduction-structure classes are unsuitable.

One mating type does not imply one strain or genetic identity. The scope
includes solo selfing and non-isogenic same-type partners. Homothallism
`traitmech:000609` covers single-isolate self-fertility, not this whole class;
parasexuality `traitmech:000607` is also not a parent because meiotic cycles
are included. Pheromone helpers may be of the opposite mating type without
contributing genomes. MAT inventory or hyphal growth alone is insufficient.
Do not require a single diploidization mechanism, universal meiosis or
spores, obligate clonality, or absence of outcrossing.

Context-dependent same-sex mating terminology needs lexical review before
synonym assignment. No xrefs, property rows or SSSOM mappings are asserted.

## Evidence and Limitations

- `DOI:10.1371/journal.pgen.1003688` (`PMID:23966871`, `PMC3744442`):
  scientific abstract supplies the one-mating-type definition; Introduction
  includes Candida and helper-cell contexts. The 13-word snippet is not the
  separate Author Summary. Selected Results and Methods were read; actual
  figures, complete tables and supplements remain uninspected.
- `DOI:10.1038/nature03448` (`PMID:15846346`): directly retrieved scientific
  abstract supplies a 13-word sentence supporting non-isogenic same-type
  fusion and meiosis. Full text and strain provenance remain unread.
- `DOI:10.1038/nature08252` (`PMID:19675652`, `PMC2866515`): 17-word
  main-text clause, retrieved with NCBI efetch after Europe PMC failure.
  Main text and Methods Summary were read; Figures 3/4 and supplementary
  Figure 7 visually checked. Selected supplement text documents ploidy
  reduction after same-type mating, not uniform euploid offspring. Other
  figures and supplement sections remain uninspected.
- `DOI:10.1371/journal.pbio.1001653` (`PMID:24058295`, `PMC3769227`):
  18-word Results s2a clause supports solo meiosis in laboratory F1 XL280,
  not natural canonical provenance. Abstract sections, s2a and Methods s4b
  were read; actual figures, supplements and other experiments remain unread.

No canonical taxa or protein accessions are asserted. Laboratory crosses,
engineered deletions and marked strains retain those qualifications in
evidence. Two CURATION_TODOs preserve lexical, taxonomy, native-example and
mechanism gaps. No causal graph is inferred. Keep actual abstract-resolver
verdicts separate from manual full-text matches. PROPOSED status awaits
human curator signoff.

## ID Space and Subset

Reserve `METPO:1056700` in `1056700-1056799`, after v489's block.
Ignored-and-hidden searches across TraitMech and CommunityMech proposals,
including the fully read CommunityMech v1 narrative and templates, found no
collision before writing. Subset: `metpo_traitmech_2026_10`.
Local `traitmech:000613` remains the identifier pending acceptance and release.

## Files

| Artifact | Rows | Purpose |
| --- | ---: | --- |
| `metpo_proposal_classes_robot.tsv` | 1 class + 2 headers | Scope-A lift |
| `proposal.md` | Not applicable | Scope, evidence and migration |

No property or SSSOM template is needed. The 11-column class template follows
the upstream headers with three trailing empty directive cells. The upstream
contract and both templates were read at Knowledge-Graph-Hub/kg-microbe commit
`ea1c5f15e6c4dba6c72165367162b354e215f018`. Legacy OBO namespace examples
do not override the pinned ontology's w3id IRIs or local verification policy.

## Verification

```bash
just verify-proposal metpo_traitmech_v490
just robot-validate-proposal metpo_traitmech_v490
just audit-proposal-coverage
just qc
```

Check record/template label, definition and parent parity. Inspect emitted
OWL for the released w3id phenotype parent and quality ancestor. ELK success
against an unlabeled legacy stub is insufficient.

## Upstream Path

Submit the validated class template to `berkeleybop/metpo` following local
review. A reserved placeholder is not upstream acceptance.

## Round-Trip Plan

After acceptance and release, refresh the pinned ontology and migrate to the
accepted METPO CURIE. Preserve the local identifier in an explicit migration
artifact and append-only history, regenerate dependent artifacts, and avoid
a duplicate primary record.

## Change Log

- v490, 2026-10-04: propose unisexual reproduction with four DOI-backed
  snippets, meiotic/parasexual scope and explicit example/mechanism limits.
