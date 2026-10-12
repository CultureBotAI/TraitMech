# Carbon-Source Memory (v582)

## Context

This cohort proposes an ontology home for `traitmech:000706`, carbon-source
memory, at `data/traits/physiology/carbon_source_memory.yaml`. It denotes a
conditional organismal phenotype, not a gene, operon, pathway, individual
observation, or a precomposed organism/chemical-use pair. It remains
`PROPOSED`: model-assisted curation is not human sign-off.

## Scope

| Scope | Records | Parent | Leaves |
| --- | ---: | --- | ---: |
| A: accepted local trait | 1 | `METPO:1000059` phenotype | 1 |
| B: causal predicates | 0 | Not applicable | 0 |
| C: schema vocabulary | 0 | Not applicable | 0 |

No negative companion, source-specific sugar class, or universal molecular
mechanism is proposed. Canonical examples, causal graphs, exact synonyms, xrefs
and SSSOM equivalences are deliberately unasserted.

## Evidence And Boundaries

- [Lambert and Kussell 2014](https://doi.org/10.1371/journal.pgen.1004556),
  PMID:25255314, PMC4177670, supplies the primary definition support. The
  [author-name correction](https://doi.org/10.1371/journal.pgen.1004793) was read;
  it is not a second experiment.
- [Cerulus et al. 2018](https://doi.org/10.7554/eLife.39234), PMID:30299256,
  PMC6211830, supplies independent growth-history evidence and cautions against
  imposing a single molecular mechanism or same-sugar requirement.
- [Zacharioudakis et al. 2007](https://doi.org/10.1016/j.cub.2007.10.044),
  PMID:17997309, supports the induction endpoint through its directly retrieved
  MED abstract. Full text and figures were not assessed.

The YAML records short verbatim snippets, precise source sections, assay
qualifications and access limits. Induction kinetics are not growth-rate
measurements. History dependence must be established under matched current test
conditions and genetic background; an isolated nutrient switch, persistent
fluorescence or a gene annotation is not enough. No duration, number of
generations, benefit or taxon-wide invariance is part of the definition.

## Hierarchy Decisions

Use `METPO:1000059` phenotype. Its pinned and current upstream RDF subjects
are active classes under `METPO:1000188`; the proposal must resolve them through
`https://w3id.org/metpo/`, not a legacy OBO stub.

`METPO:1000731` nutrient adaptation is a trophic-type class whose retained
local evidence frames chronic copiotrophic/oligotrophic regimes. That differs
from the temporal response here. Diauxic growth, carbon catabolite repression,
generalist/specialist niche breadth, stress priming, chemotactic sensing and
genetic adaptation are not exact equivalents. Broader uses of cellular,
metabolic, phenotypic or transcriptional memory are not exact synonyms. The
carbon-source qualifier is intentional; upstream hierarchy review remains open.

## Novelty And Reservation

Allocation was checked on 2026-10-12 against live main
`1cfd5903e8ca9396b3dcd3f35626522cb35f77c4`, all 22 registered TraitMech
worktrees, 581 proposal cohorts and 4,090 declared narrative intervals, plus
530 proposal files across 127 registered CommunityMech worktrees. Searches
included ignored and hidden files, labels, variants, slugs, citations, current
and historical IDs, records, history, proposals, research and generated pages.
They did not unpack archives, follow symlink directories, or claim coverage
of unregistered/private work. Matches concerning thermal hysteresis, other
forms of priming and quorum-sensing models are not this trait.

The fresh 399-record seed projection has 55 exact IDs absent from the
1,100-record baseline. Frozen release-delta and active-review tables were read
as historical decisions, not current absence proofs. The candidate has no
exact active or deprecated match in the pinned RDF or the current upstream
released ontology; the upstream edit root alone is insufficient to establish
this. No ontology refresh or deprecated-ID reuse is involved.

Fresh, fully paginated changed-file lists and immutable relevant blobs covered
TraitMech PRs #1782, #1476, #973 and draft #924; CommunityMech draft #935; and
METPO PRs #644, #643, #641, #640, #638 and #629. Their head SHAs and open sets
were stable through acquisition. All 644 METPO issue/PR bodies and 654 comments
were searched. Current upstream snapshots were verified by Git blob and SHA-256
hashes against unchanged heads:

- METPO: `1efc8c73009200b9cb74d125df6a0ea5dc36cb93`.
- CommunityMech: `80049bcc9195480a58633236169b62f86c23489a`.
- KG-Microbe: `1408e7099d039026d7611c240938d8e177753406`.

No conflicting reservation was found. Recheck current main, worktrees and all
pending heads immediately before publication; this cannot eliminate concurrent
allocation races. This bounded assessment is not global discovery exhaustion.

## ID Space And Subset

- Local ID: `traitmech:000706`.
- Cohort: `metpo_traitmech_v582`.
- Reserve the entire `METPO:1065900`-`METPO:1065999` block.
- Populate only `METPO:1065900`; it is a proposal placeholder, not a released ID.
- Subset: `metpo_traitmech_2026_10`, following adjacent monthly-tag convention.
- The block is separate from CommunityMech v1 `1007100`-`1007220` and all
  inspected later reservations; no old block is reused.

## Files

| File | Content |
| --- | --- |
| `metpo_proposal_classes_robot.tsv` | Two canonical headers, one class row, 11 columns |
| `proposal.md` | Scope, evidence, reservation and round-trip rationale |

Property and SSSOM files are omitted because this cohort proposes neither.
`scripts/add_carbon_source_memory_trait.py` is the guarded maintained writer
for the record and TSV. The TSV preserves the required trailing empty header
cells; citation columns contain citations, not external equivalence claims.

## Verification

Run the native proposal verifier and ROBOT template/merge/ELK wrapper, then
inspect emitted RDF for the expected IRI, label and parent hierarchy:

```bash
just verify-proposal metpo_traitmech_v582
just robot-validate-proposal metpo_traitmech_v582
just qc
just validate-history
just validate-products
```

The final saved structured review and PR report actual command outcomes,
source-access limits, generated-artifact checks and any findings. Normal
`git diff --check` flags required trailing TSV tabs; only that exact template
receives the documented `-blank-at-eol` check after column-width verification.
Neither global whitespace rules nor frozen QC baselines are weakened.

## Upstream Path And Round Trip

After review, submit this TSV and rationale to `berkeleybop/metpo` or the
KG-Microbe proposal pipeline. Curator `codex` added the local record with
`llm_assisted: true`; its curation event and append-only repository history
retain that provenance. Upstream maintainers choose the final ID and hierarchy.

After an explicitly reviewed ontology update includes the accepted term,
re-seed the approved release and migrate the identifier and dependent
references while preserving the old `traitmech:000706` as a traceable
identifier alias and retaining history. Do not emit the placeholder as a
released METPO identity or replace the pinned ontology automatically.

## Change Log

- v582, 2026-10-12: propose one evidence-backed carbon-source-memory class;
  keep induction and growth endpoints distinct and unresolved provenance explicit.
