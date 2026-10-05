# Heterothallism: METPO Proposal v487

## Context

Lift `traitmech:000610 heterothallism`, a PROPOSED PHYSIOLOGY class.
Whole-repository searches included ignored and hidden files, labels, synonyms,
citations, graph nodes, discussions, research, proposals, pages and history.
No exact record was found. Homothallism mentions heterothallism as contrasting
evidence, not an exact synonym, unresolved graph node or parent TODO.

The pinned 12,617-triple METPO graph has no matching term. A fresh 399-record
seed compared with the 1,004-record pre-addition corpus has 344 present and
55 absent IDs. Both frozen release-review tables classify those 55 as
38 supporting-field rows and 17 duplicates, not missing primary traits.
An all-state upstream issue search for heterothall returned no results on
2026-10-04; current open local PRs reserve neither this trait nor this block.

## Scope

| Scope | Count | Parent | Leaves |
| --- | ---: | --- | ---: |
| A: synthetic trait | 1 | METPO:1000059 phenotype | 1 |
| B: predicates | 0 | Not applicable | 0 |
| C: schema enums | 0 | Not applicable | 0 |

## Hierarchy Decisions

Use released `METPO:1000059 phenotype`, under `METPO:1000188 quality`,
in the pinned ontology's `https://w3id.org/metpo/` namespace. The old
reproductive-process and reproductive-structure terms are obsolete, not
live candidate parents. PHYSIOLOGY is a filesystem category. Homothallism,
heterokaryosis, ploidy, hyphal fusion and parasexuality are not is-a parents.

The definition concerns organism-level partner dependence, not general
infertility or nuclear recognition inside a self-fertile individual. It
does not require exactly two mating types, a particular MAT architecture,
or universal compatibility. No exact synonyms, xrefs or SSSOM mappings are
asserted; self-sterility has broader uses that require a lexical-scope check.

## Evidence and Limitations

- `DOI:10.1038/nature07528` (`PMID:19043401`) supplies the definition
  authority and an exact scientific-abstract sentence. Observed sexual
  reproduction in A. fumigatus is distinct from prior sequence-based
  suggestions. Full methods, figures, supplements and individual strain
  provenance remain uninspected.
- `DOI:10.1534/genetics.111.136358` (`PMID:22298702`) supplies an exact
  scientific-abstract sentence about engineered receptor/pheromone
  coexpression in N. crassa. Attraction and barren perithecia do not establish
  self-fertility. This source supports readout limits, not a natural canonical
  example. Full text and supplementary experiments remain uninspected.
- `DOI:10.1371/journal.pgen.1006981` (`PMID:28892488`) supplies a sentence
  from scientific abstract `abstract1`, separate from the author summary.
  Partner-dependent C. spinulosa progeny can cross with homothallic strains;
  that compatibility pattern is not universalized. Strain/culture Methods
  and Conclusions were also read; nuclear-level heterothallic recognition
  does not make the self-fertile organism partner-dependent. Most experiments,
  actual figures, supplements and original strain provenance remain unverified.

Two CURATION_TODOs retain lexical, natural-isolate, mechanism and readout
limits. No canonical example or protein-resolved graph is asserted. The
record remains PROPOSED pending human curator signoff. All three snippets
were checked against directly retrieved source sections; retain the maintained
abstract resolver's actual verdict independently of those checks.

## ID Space and Subset

Reserve `METPO:1056400` in `1056400-1056499`, after v486's block.
Ignored-and-hidden searches across TraitMech and CommunityMech proposals,
including the CommunityMech v1 ranges, found no identifier collision before
writing. Subset: `metpo_traitmech_2026_10`. Keep local `traitmech:000610`
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
just verify-proposal metpo_traitmech_v487
just robot-validate-proposal metpo_traitmech_v487
just audit-proposal-coverage
just qc
```

Check record/template label, definition and parent parity and inspect emitted
OWL for the released w3id phenotype parent and quality ancestor. An ELK pass
against a detached legacy OBO parent stub is insufficient.

## Upstream Path

Submit the validated class template to `berkeleybop/metpo` following local
review. The reserved placeholder does not imply upstream acceptance.

## Round-Trip Plan

After upstream acceptance and release, update the pinned ontology and migrate
to the accepted METPO CURIE. Preserve the local identifier in an explicit
migration artifact and append-only history, regenerate dependent artifacts,
and avoid creating a duplicate primary record.

## Change Log

- v487, 2026-10-04: propose heterothallism with three source snippets and
  explicit organism/nuclear and completed-cycle scope limits.
