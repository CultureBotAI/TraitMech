# Parasexuality: METPO Proposal v484

## Context

Lift `traitmech:000607 parasexuality`, a PROPOSED PHYSIOLOGY class, into a
reserved upstream slot. This is an organismal reproductive phenotype, not a
ploidy measurement, gene, sequence feature or isolated mating experiment.
Three primary studies support nuclear-fusion/chromosome-loss cycling and
the distinction between conventional meiosis and shared molecular factors.

Whole-repository novelty searches included ignored and hidden files, labels,
spelling variants, citations, slugs, synonyms, graph nodes, discussions,
research, proposals, generated artifacts and history. No exact record was
found. The existing ploidy record (`traitmech:000100`) concerns genome-copy
number; hyphal-anastomosis evidence mentions possible genetic exchange but
does not assert an unresolved parasexuality node or synonym. Neither older
record requires mutation for this addition.

The pinned 12,617-triple METPO graph has no exact parasexuality class or
synonym. Its obsolete genetic-exchange class is not a valid parent. A fresh
399-record seed reconciled against the 1,001-record pre-addition corpus has
344 present and 55 absent IDs; both frozen 2026-06-12 review tables classify
the remainder as 38 supporting-field rows and 17 duplicates. This is not a
missing primary-trait queue. All-state upstream issue searches for
parasexual and parameiosis found no corresponding proposal on 2026-10-04.

## Scope

| Scope | Count | Parent | Leaves |
| --- | ---: | --- | ---: |
| A: synthetic trait | 1 | METPO:1000059 phenotype | 1 |
| B: predicates | 0 | Not applicable | 0 |
| C: schema enums | 0 | Not applicable | 0 |

No causal predicate or schema-enum lift is needed.

## Hierarchy Decisions

Use released `METPO:1000059 phenotype`, under `METPO:1000188 quality`, in
the pinned ontology's `https://w3id.org/metpo/` namespace. The definition's
genus is a fungal phenotype. Ploidy and hyphal anastomosis are not is-a
parents: genome-copy number and cell fusion alone do not entail a complete
parasexual reproductive capability.

The definition does not require haploid progeny or the absence of all
mating. It also does not claim that a species is incapable of conventional
meiosis under every condition. The 2019 parameiosis experiments distinguish
the absence of a conventional meiotic cycle from the presence and activity
of meiosis-associated proteins. Sequence homology is not a reproductive
phenotype assay. The fungal scope follows the evidence; broader uses of
parasexual terminology need separate interpretation.

No exact synonyms, xrefs or SSSOM mappings are asserted before external
phenotype/process scope and identifier authorities are resolved.

## Evidence and Limitations

- `DOI:10.1093/emboj/cdg235` (`PMID:12743044`): definition authority.
  Marked Candida albicans mating products undergo chromosome loss and
  produce diploid or near-diploid progeny that can mate again. The primary
  main text and Figures 1-9 were inspected in the author-hosted PDF linked
  in the record. Supplementary media, mating and PCR details remain unread.
  Marker loss alone can result from recombination, so it is not itself
  proof of chromosome loss. Unpublished gene-deletion observations are not
  used as causal proof.
- `DOI:10.1128/ec.00128-13` (`PMID:24123269`): a repeatable cycle in
  marked Candida tropicalis strains. Publisher Methods, Results,
  Discussion, strain tables and actual Figures 3-4 were inspected. The
  supplementary Figure S1 caption/labels were read as PDF text, but its
  plot was not visually inspected. The CAY2060 tester is arg4/arg4 despite
  the Figure 4 caption's wild-type wording; no natural canonical example
  is inferred from that caption. Medium effects cannot be transferred
  unqualified between Candida species.
- `DOI:10.1038/s41467-019-12376-2` (`PMID:31558727`): distinguishes
  chromosome loss and recombination endpoints, with functions for Spo11
  and Rec8 during C. albicans CCL. Publisher Introduction and Results were
  read; full Methods, actual figures and supplements remain uninspected.
  These results do not make the presence of a meiotic homologue proof of
  conventional meiosis or make all parasexual stages mechanistically equal.

All three snippets exact-match directly retrieved Europe PMC abstracts;
their DOI/PMID metadata were checked against the raw single-hit responses.
No canonical taxa or protein-resolved graph is asserted. Two CURATION_TODOs
retain trait-scope, source-access, strain-provenance and grounding limits.
NONMECHANISTIC is not used to bypass unresolved molecular mechanisms.

## ID Space and Subset

Reserve `METPO:1056100` in `1056100-1056199`, after v483's block.
Ignored-and-hidden whole-repository checks found no collision before
writing, and the block does not overlap CommunityMech v1 or its extensions.
Subset: `metpo_traitmech_2026_10`. Keep local `traitmech:000607` until the
upstream term is accepted and released.

## Files

| Artifact | Rows | Purpose |
| --- | ---: | --- |
| `metpo_proposal_classes_robot.tsv` | 1 class + 2 headers | Scope-A lift |
| `proposal.md` | Not applicable | Evidence, scope and migration |

No property or SSSOM template is needed. The 11-column class template
matches the upstream headers, including three trailing empty directive
cells. The upstream contract is pinned to Knowledge-Graph-Hub/kg-microbe
commit `1408e7099d039026d7611c240938d8e177753406`.

## Verification

```bash
just verify-proposal metpo_traitmech_v484
just robot-validate-proposal metpo_traitmech_v484
just audit-proposal-coverage
just qc
```

Check record/template label, definition and parent parity. Inspect the
emitted OWL for the released w3id phenotype parent and quality ancestor;
an ELK success with a legacy OBO METPO stub would not establish correct
parentage.

## Upstream Path

Submit the validated class template to `berkeleybop/metpo` following
TraitMech review. A reserved placeholder does not imply upstream acceptance.

## Round-Trip Plan

After acceptance and release, update the pinned ontology and migrate the
local identifier to the accepted METPO CURIE. Preserve the old local CURIE
in an explicit migration artifact and append-only history, regenerate
dependent artifacts, and do not create a duplicate primary record.

## Change Log

- v484, 2026-10-04: propose parasexuality with three primary snippets and
  explicit reproductive-stage, strain-provenance and mechanism limits.
