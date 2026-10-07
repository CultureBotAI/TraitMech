# Pseudobipolar Mating System: METPO Proposal v494

## Context

Lift `traitmech:000617 pseudobipolar mating system`, a PROPOSED PHYSIOLOGY
class. Whole-repository novelty and allocation searches included ignored and
hidden files, citations, likely slugs, hyphenated terminology, discussions,
graphs, history, research and generated pages. No exact record, prior proposal
or identifier collision was found before writing. Sibling CommunityMech
proposals were also searched with ignored and hidden files included.

The pinned 12,617-triple METPO graph has no matching mating-system literal.
A fresh 399-record seed compared with the 1,011-record pre-addition corpus has
344 present and 55 absent IDs. Both frozen release-review tables classify those
55 as 38 supporting-field rows and 17 duplicates. The upstream all-state
pseudobipolar issue search returned no results on 2026-10-05. Paginated file
lists of open PRs #1477, #1476, #973 and #924 contain no competing allocation.
These checks establish candidate novelty, not exhaustion of trait discovery.

## Scope

| Scope | Count | Parent | Leaves |
| --- | ---: | --- | ---: |
| A: synthetic trait | 1 | METPO:1000059 phenotype | 1 |
| B: predicates | 0 | Not applicable | 0 |
| C: schema enums | 0 | Not applicable | 0 |

## Hierarchy Decisions

This is a reusable mating-system phenotype, not a literal MAT sequence feature.
The definition combines same-chromosome compatibility loci with the ability
to recombine, rather than using colocation alone as evidence of fertility.
The 2010 paper's pseudo-bipolar terminology emphasizes normally bipolar
behavior with occasional recombination. The 2025 paper also applies the term
to widely separated, potentially genetically unlinked loci. Preserve that
broader usage: do not require a fixed recombination frequency, degree of
partial genetic linkage, exactly two mating types, or an evolutionary
intermediate on a mandatory trajectory.

This is not equivalent to a single segregating factor (`traitmech:000616`
bipolar mating), nor to independent segregation without a chromosome-location
constraint (`traitmech:000615` tetrapolar mating). The latter can functionally
overlap the broader modern usage; no disjointness is asserted. Heterothallic
source framing also does not establish universal organism-level partner
dependence under `traitmech:000610`. Use released `METPO:1000059 phenotype`,
with `METPO:1000188 quality` ancestry, in both record and proposal. A narrower
hierarchy and lexical equivalents remain open; PHYSIOLOGY is a filesystem
category, not an ontology parent.

## Evidence and Limitations

- `DOI:10.1371/journal.pgen.1001052`, `PMID:20700437`, `PMC2916851`:
  native Sporidiobolus salmonicolor crossing and segregation evidence supports
  the original functional interpretation. The scientific abstract was checked
  against raw metadata and XML abstract1, distinct from the author summary.
  Results/Discussion and Methods were read, and actual Figures 3-5, Figure S5
  and both pages of Table S1 inspected. T7.1 differs from both parental
  compatibility types but mates with CBS 490. The figure scores clamps and
  teliospores; normal germination in compatible recombinant crosses is a
  prose-only report with results not shown. Eight teliospores from one parental
  cross are not eight independent parental crosses, and most colonies per
  teliospore are clonal. Linkage statistics require larger samples; Figure 5
  partly assumes a related species' synteny. Methods and Figure/Table labels
  disagree on the CBS 6832 HD allele. Other actual figures and supplements
  remain uninspected.
- `DOI:10.1371/journal.pbio.3003417`, `PMID:41042803`, `PMC12510652`:
  the directly read scientific abstract and Introduction establish broader
  terminology, not independent experimental replication of pseudobipolar
  fertility. First two Results subsections, actual Figure 1 and the relevant
  Discussion paragraph in XML sec017 were inspected. The abstract's claim of
  genetically unlinked loci is qualified by the Discussion: Kwoniella europaea
  crosses have not yielded sexual reproduction, persistent recombination is
  conditional, and distance alone cannot exclude suppression. Do not transfer
  sexual results in C. decagattii or K. mangrovensis to K. europaea. Other
  Results, Methods, figures and supplements remain uninspected.

No canonical example is asserted: ML 2241's original isolation context and
active taxon authority remain unresolved, and recombinant T7.1 is not an
independent natural isolate. Two CURATION_TODOs retain hierarchy, lexical,
strain, source and native mechanism gaps. No protein accession, external xref
or causal graph is introduced; no NONMECHANISTIC workaround is used. Snippet
resolver verdicts remain separate from manual source-section verification.
PROPOSED status awaits human curator signoff.

## ID Space and Subset

Reserve `METPO:1057100` in `1057100-1057199`, after v493's block.
Subset: `metpo_traitmech_2026_10`. This does not overlap CommunityMech v1's
`1007100-1007220` range. Keep `traitmech:000617` until upstream acceptance
and release; a placeholder reservation is not a released ontology term.

## Files

| Artifact | Rows | Purpose |
| --- | ---: | --- |
| `metpo_proposal_classes_robot.tsv` | 1 class + 2 headers | Scope-A lift |
| `proposal.md` | Not applicable | Scope, evidence and migration |

No property or SSSOM template is needed. The 11-column class header follows
Knowledge-Graph-Hub/kg-microbe commit
`ea1c5f15e6c4dba6c72165367162b354e215f018`, including three trailing empty
directive cells. The expected local contract is absent, so its pinned copy is
reused. CommunityMech v1 is the worked reference. Legacy OBO-prefix examples
do not override the pinned ontology's w3id IRIs.

## Verification

```bash
just verify-proposal metpo_traitmech_v494
just robot-validate-proposal metpo_traitmech_v494
just audit-proposal-coverage
just qc
```

Check record/template label, definition and parent parity. Inspect emitted
`https://w3id.org/metpo/` IRIs, including the actual phenotype label and quality
ancestry; ELK success with a detached, unlabeled parent is insufficient.

## Upstream Path

Submit the validated class template to `berkeleybop/metpo` after local review.

## Round-Trip Plan

After upstream acceptance and release, refresh the ontology and migrate the
record to the accepted METPO CURIE. Preserve its local ID in an explicit
migration artifact and append-only history, regenerate dependent artifacts,
and avoid creating a duplicate primary record.

## Change Log

- v494, 2026-10-05: propose pseudobipolar mating with two DOI-backed snippets,
  experimental and genomic evidence distinguished, and explicit source limits.
