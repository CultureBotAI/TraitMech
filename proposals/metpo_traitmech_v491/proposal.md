# Primary Homothallism: METPO Proposal v491

## Context

Lift `traitmech:000614 primary homothallism`, a PROPOSED PHYSIOLOGY class.
Whole-repository searches included ignored and hidden files, names, possible
slugs, citations, synonyms, graph nodes, discussions, research, proposals,
pages and history. Existing homothallism mentions the narrower mode but has
no exact record, synonym or unresolved same-scope node requiring migration.

The pinned 12,617-triple METPO graph has no exact term. A fresh 399-record
seed compared with the 1,008-record pre-addition corpus has 344 present and
55 absent IDs. Both frozen release-review tables classify these as 38
supporting-field rows and 17 duplicates, not missing primary records.
An all-state upstream issue search for homothallism returned no results on
2026-10-04. Open local PRs do not reserve this trait or identifier block.
These checks establish this candidate's novelty, not discovery exhaustion.

## Scope

| Scope | Count | Parent | Leaves |
| --- | ---: | --- | ---: |
| A: synthetic trait | 1 | METPO:1000059 phenotype (standalone proposal) | 1 |
| B: predicates | 0 | Not applicable | 0 |
| C: schema enums | 0 | Not applicable | 0 |

## Hierarchy Decisions

The local record narrows `traitmech:000609 homothallism`: self-fertility is
supported by compatible mating-type determinants in one genome, without
requiring switching. This agrees with the parent's source-attributed umbrella
placement. It is not a sequence-inventory record: the parent's Chromocrea
example specifically warns that co-resident MAT genes alone are insufficient.

Pseudohomothallism `traitmech:000612` also narrows operational self-fertility,
but packages compatible nuclei within a spore. Switching `traitmech:000611`
and same-type outcrossing within unisexual reproduction `traitmech:000613`
do not alone imply single-founder self-fertility; their broader parents are
intentional, not a reason to flatten this narrower hierarchy. No disjointness
or universal absence of outcrossing is asserted. Linked loci, fixed spore
counts, one domain architecture and indispensability of every MAT gene are
not defining requirements. True-homothallism synonymy remains unresolved.

The standalone template uses released `METPO:1000059 phenotype`, under
`METPO:1000188 quality`, in the pinned w3id namespace. Pending homothallism
`METPO:1056300` from v486 is not imported as an unlabeled stub. Reconcile
the narrower hierarchy after that parent is accepted upstream. PHYSIOLOGY
is a filesystem category. No xrefs or SSSOM mappings are asserted.

## Evidence and Limitations

- `DOI:10.1371/journal.pgen.1006110`, `PMID:27327578`, `PMC4915694`:
  18-word Introduction definition clause. Abstract sections, Introduction,
  all Results and selected Methods were read; actual Figures 1/3/4, Table 1
  and supplementary Table S3 inspected. HD2 deletion retains vestigial
  sporulation and an obligatory HD heterodimer remains unproven. SPO11
  affects spore viability significantly, not basidia counts. Retain the
  6838/6938 strain-name discrepancy and incorrect figure-panel pointers.
- `DOI:10.5598/imafungus.2015.06.01.13`, `PMID:26203424`, `PMC4500084`:
  11-word section s2a phrase; the whole section was read in XML. Terminology
  authority, not experimental replication. Its ascomycete MAT nomenclature
  is not universal; actual Figure 1 remains uninspected.
- `DOI:10.1016/j.cub.2007.07.012`, `PMID:17669651`: 19-word scientific
  abstract clause from authoritative Europe PMC metadata. Aspergillus MAT
  expression and sexual development support self-fertility within one
  individual. Full text, figures and original strain provenance remain unread.
- `DOI:10.1128/EC.00019-10`, `PMID:20435701`, `PMC2901639`: 18-word
  Results clause from the author-institution published PDF. Its subjects
  are SmtA-1/SmtA-3 deletion strains, not all mutants. Actual Figures 1/2,
  Introduction, first two Results subsections and selected Methods were
  read. SmtA-2 loss blocks maturation and complementation restores it;
  co-occurring MAT genes are not all individually essential. Retain the
  abstract versus Introduction/Figure 1 disagreement about SmtA-3's domain.

Canonical example: `NCBITaxon:264483 Phaffia rhodozyma`, qualified to
wild-type CBS 6938. The reproductive study's Methods, Table 1 and images
support 6938 despite 6838 in parts of the prose. Natural provenance is
Table 1 at https://pmc.ncbi.nlm.nih.gov/articles/PMC5103461/
(`DOI:10.1186/s12864-016-3244-7`, `PMID:27829365`): UCD 77-61 from birch
stump sap in Finland. That table supports provenance, not independent trait
replication. DWR, temperature, time and separate viable-spore readouts remain
qualified in the record. Current NCBI taxonomy resolves the species label.

Unread material is disclosed. No unverified protein accession or mechanistic
graph is asserted; two CURATION_TODOs preserve mapping, interaction and
experimental gaps. Manual full-text matches do not override the actual
abstract-resolver verdict. PROPOSED status awaits human curator signoff.

## ID Space and Subset

Reserve `METPO:1056800` in `1056800-1056899`, after v490's block.
Ignored-and-hidden searches of TraitMech and CommunityMech proposals found
no collision before writing. Subset: `metpo_traitmech_2026_10`.
The record keeps `traitmech:000614` pending upstream acceptance and release.

## Files

| Artifact | Rows | Purpose |
| --- | ---: | --- |
| `metpo_proposal_classes_robot.tsv` | 1 class + 2 headers | Scope-A lift |
| `proposal.md` | Not applicable | Scope, evidence and migration |

No property or SSSOM template is needed. The 11-column class header matches
the upstream template at Knowledge-Graph-Hub/kg-microbe commit
`ea1c5f15e6c4dba6c72165367162b354e215f018`, including three trailing empty
directive cells. That pinned contract was retrieved because the current
main URL and expected local copy were unavailable. Legacy OBO-prefix
examples do not override the current ontology's w3id IRIs.

## Verification

```bash
just verify-proposal metpo_traitmech_v491
just robot-validate-proposal metpo_traitmech_v491
just audit-proposal-coverage
just qc
```

Check record/template label and definition parity, intentional local versus
released parent choice, and actual emitted OWL for phenotype/quality ancestry.
ELK success against an unlabeled parent is insufficient.

## Upstream Path

Submit the validated class template to `berkeleybop/metpo` after local
review. Placeholder reservation is not upstream acceptance.

## Round-Trip Plan

After acceptance and release, refresh the pinned ontology and migrate the
identifier and parent to accepted METPO CURIEs. Preserve the local ID in an
explicit migration artifact and append-only history, regenerate dependents,
and avoid a duplicate primary record.

## Change Log

- v491, 2026-10-04: propose primary homothallism with four DOI-backed
  snippets, a qualified natural example, and explicit source/scope limits.
