# Mating-Type Switching: METPO Proposal v488

## Context

Lift `traitmech:000611 mating-type switching`, a PROPOSED PHYSIOLOGY class.
Whole-repository novelty searches included ignored and hidden files, labels,
synonyms, citations, graph nodes, discussions, research, proposals, pages and
history. No exact record was found. Homothallism names switching as one of
several mechanisms, not as an exact synonym, ungrounded node or parent TODO.
The existing heterothallism record addresses partner dependence instead.

The pinned 12,617-triple METPO graph has no matching term. A fresh 399-record
seed compared with the 1,005-record pre-addition corpus has 344 present and
55 absent IDs. Both frozen release-review tables classify those 55 as
38 supporting-field rows and 17 duplicates, not missing primary traits.
An all-state upstream issue search for mating type returned no results on
2026-10-04; current open local PRs reserve neither this trait nor this block.

## Scope

| Scope | Count | Parent | Leaves |
| --- | ---: | --- | ---: |
| A: synthetic trait | 1 | METPO:1000059 phenotype | 1 |
| B: predicates | 0 | Not applicable | 0 |
| C: schema enums | 0 | Not applicable | 0 |

## Hierarchy Decisions

Use released `METPO:1000059 phenotype`, under `METPO:1000188 quality`,
in the pinned ontology's `https://w3id.org/metpo/` namespace. The older
reproduction-process and reproduction-structure classes are obsolete.
PHYSIOLOGY is a filesystem category, not an ontology parent.

The capability includes reversible and irreversible mating-type conversion;
it is not a literal locus, gene, repeat or cassette. It is also not ordinary
segregation of mating types among sexual progeny. Homothallism, heterothallism,
ploidy, heterokaryosis and parasexuality are distinct rather than is-a parents.
No universal cassette architecture, endonuclease, reversibility, cell-cycle
stage or exactly-two-types requirement is asserted. No exact synonyms, xrefs
or SSSOM mappings are proposed before lexical and phenotype/process scope
is resolved.

## Evidence and Limitations

- `DOI:10.5598/imafungus.2015.06.01.13` (`PMID:26203424`) provides the
  general definition. Section s3 and both reversible/irreversible subsections
  were read as raw XML. The 25-word snippet is a full-text sentence, not
  an abstract quote. This review is terminology authority, not replication.
- `DOI:10.1534/genetics.107.076315` (`PMID:17660548`) provides an exact
  scientific-abstract sentence and a primary S. pombe mechanistic study.
  Its engineered mutant donor-cassette test does not establish natural
  isolate provenance. The full-text XML returned HTTP 500 and the public
  PDF mirror HTTP 403; methods, figures and supplements remain unread.
- `DOI:10.1371/journal.pgen.1006981` (`PMID:28892488`) provides a Conclusions
  clause about irreversible alteration in filamentous fungi. Scientific
  abstract, strain/culture Methods, Results sec005-sec007 and Discussion
  sec013/sec015 were read. Actual Figures 3 and 4 were inspected. Results
  and Figure 3 identify DR2 deletion; Discussion sec013 says DR1. The record
  keeps the figure-supported identity and explicitly notes the discrepancy.
  Fruit-body structures without ascospores are not completed sex, and the
  detailed nuclear-recognition mechanism remains a model. Other figures,
  supplements, unread experiments and natural strain provenance remain
  unverified.

Two CURATION_TODOs preserve assay-level, lexical, canonical-example and
native-protein gaps. No canonical example or causal graph is inferred.
Keep actual abstract-resolver outcomes separate from directly verified
full-text spans. The record remains PROPOSED pending human curator signoff.

## ID Space and Subset

Reserve `METPO:1056500` in `1056500-1056599`, after v487's block.
Ignored-and-hidden searches across TraitMech and CommunityMech proposals,
including CommunityMech v1 ranges, found no collision before writing.
Subset: `metpo_traitmech_2026_10`. Local `traitmech:000611` remains the
identifier pending upstream acceptance and release.

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
just verify-proposal metpo_traitmech_v488
just robot-validate-proposal metpo_traitmech_v488
just audit-proposal-coverage
just qc
```

Check record/template label, definition and parent parity and inspect emitted
OWL for the released w3id phenotype parent and quality ancestor. A successful
ELK run against a legacy OBO stub is insufficient.

## Upstream Path

Submit the validated class template to `berkeleybop/metpo` following local
review. A reserved placeholder is not upstream acceptance.

## Round-Trip Plan

After upstream acceptance and release, update the pinned ontology and migrate
to the accepted METPO CURIE. Preserve the local identifier in an explicit
migration artifact and append-only history, regenerate dependent artifacts,
and avoid creating a duplicate primary record.

## Change Log

- v488, 2026-10-04: propose mating-type switching with reversible and
  irreversible scope, three source snippets and explicit source discrepancy.
