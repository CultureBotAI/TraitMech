# Bipolar Mating System: METPO Proposal v493

## Context

Lift `traitmech:000616 bipolar mating system`, a PROPOSED PHYSIOLOGY class.
Novelty and allocation searches included ignored and hidden files throughout
TraitMech and sibling CommunityMech proposals: labels, likely slugs, synonyms,
citations, discussions, graphs, history and generated pages. The only bipolarity
hits concerned unrelated flagellar arrangements. No exact record or ID collision
was found before writing.

The pinned 12,617-triple METPO graph has no matching mating-system literal.
A fresh 399-record seed compared with the live 1,010-record pre-addition corpus
has 344 present and 55 absent IDs. Both frozen release-review tables classify
those 55 as 38 supporting-field rows and 17 duplicates, not missing primary
records. An all-state upstream issue search for bipolar returned no results on
2026-10-05. Paginated file lists of open local PRs #1477, #1476, #973 and #924
contain no competing trait or proposal allocation. This establishes candidate
novelty, not exhaustion of microbial trait discovery.

## Scope

| Scope | Count | Parent | Leaves |
| --- | ---: | --- | ---: |
| A: synthetic trait | 1 | METPO:1000059 phenotype | 1 |
| B: predicates | 0 | Not applicable | 0 |
| C: schema enums | 0 | Not applicable | 0 |

## Hierarchy Decisions

The definition denotes functional compatibility governed by one segregating
mating-type factor, not one gene or exactly two specificities across a species.
A complex linked MAT region and loss of mating-type specificity at another
factor can both yield this phenotype. No single molecular architecture is
required, and receptor gene presence does not demonstrate incompatibility.

Bakkeren describes recognition in heterothallic basidiomycetes. That attributed
scope does not prove universal separate-partner dependence under local
`traitmech:000610 heterothallism`, which distinguishes organismal self-fertility
from nuclear recognition. Both record and standalone proposal use released
`METPO:1000059 phenotype`, under `METPO:1000188 quality`. Tetrapolar mating
(`traitmech:000615`) instead requires differences at two independently
segregating factors. No disjointness with homothallism or universal fertility
is asserted. PHYSIOLOGY is a filesystem category; unifactorial terminology,
narrower hierarchy and external equivalences remain review questions.

## Evidence and Limitations

- `DOI:10.1073/pnas.91.15.7085`, `PMID:7913746`, `PMC44343`:
  directly retrieved Europe PMC scientific abstract defines bipolarity with
  one genetic factor and explicitly permits multiple alleles. Its Ustilago
  hordei linkage result establishes a reported architecture, not our independent
  inspection of native crosses. Full text, figures, methods, supplements and
  natural strain provenance remain uninspected.
- `DOI:10.1534/genetics.105.051128`, `PMID:16461425`, `PMC1456265`:
  a contiguous sentence in the first Results subsection on p. 1881 reports two mating types
  within each of 24 collections, not two across the species. Direct native
  crosses and marker segregation support the phenotype beyond gene inventory.
  The published author-institution PDF is
  https://public.websites.umich.edu/~mycology/resources/Publications/james2006.genetics.pdf.
  Pages 1877-1882 and actual Tables 1-3 were inspected; pp. 1883-1884 were
  text-extracted only. Actual figures, later Results/Discussion and supplements
  remain uninspected. Clamp/dikaryon scoring is not automatically completed
  fertile reproduction. Poor-mating progeny were excluded from tester selection;
  Table 3's plus/minus markers are PCR-RFLP genotypes, not gene absence.
  CDSTE3.4 lacks segregation data. Heterologous responses and native specificity
  are distinct; loss of specificity does not mean loss of all cellular function.

No canonical taxon assertion is made: the James Methods describe natural North
Carolina fruit-body provenance, but active taxonomy and the intersterile Japanese
group remain unresolved. No unsupported taxon or protein CURIE is added. Two
CURATION_TODOs retain scope, lexical, source, taxon and mechanism gaps. No causal
graph or NONMECHANISTIC workaround is used. Manual full-text checks remain
separate from actual abstract-resolver verdicts. PROPOSED status awaits human
curator signoff.

## ID Space and Subset

Reserve `METPO:1057000` in `1057000-1057099`, after v492's block.
Subset: `metpo_traitmech_2026_10`. Keep `traitmech:000616` until upstream
acceptance and release; reservation is not acceptance. The block does not
overlap CommunityMech v1's `1007100-1007220` range.

## Files

| Artifact | Rows | Purpose |
| --- | ---: | --- |
| `metpo_proposal_classes_robot.tsv` | 1 class + 2 headers | Scope-A lift |
| `proposal.md` | Not applicable | Scope, evidence and migration |

No property or SSSOM template is needed. The 11-column class header follows
Knowledge-Graph-Hub/kg-microbe commit
`ea1c5f15e6c4dba6c72165367162b354e215f018`, including three trailing empty
directive cells. The expected local contract is absent, so the pinned copy is
reused. CommunityMech v1 provides the reference structure. Legacy OBO-prefix
examples do not override the pinned ontology's w3id IRIs.

## Verification

```bash
just verify-proposal metpo_traitmech_v493
just robot-validate-proposal metpo_traitmech_v493
just audit-proposal-coverage
just qc
```

Check record/template identity and parent parity, and inspect emitted OWL for
`https://w3id.org/metpo/` identifiers and phenotype/quality ancestry. ELK success
with an unlabeled parent is not sufficient.

## Upstream Path

Submit the validated class template to `berkeleybop/metpo` after local review.

## Round-Trip Plan

After acceptance and release, refresh the ontology and migrate the identifier
to the accepted METPO CURIE. Preserve the local ID in an explicit migration
artifact and append-only history, regenerate dependent artifacts and avoid
creating a duplicate primary record.

## Change Log

- v493, 2026-10-05: propose bipolar mating with two primary DOI-backed snippets
  and explicit compatibility, readout and mechanism limitations.
