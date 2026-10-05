# Paedogamy: METPO Proposal v500

## Context

Lift `traitmech:000624 paedogamy`, a PROPOSED PHYSIOLOGY class. Whole-repository
novelty and allocation searches included ignored and hidden files, exact labels,
pedogamy spelling, gametangium terminology, source identifiers, the local ID and
the full proposed block. The only existing paedogamy mention was an unresolved
autogamy research lead and its historical/generated artifacts. Available
CommunityMech proposals had no competing term or allocation.

A fresh 399-record METPO seed shares 344 identifiers with the 1,018-record
pre-addition corpus. Complete release-delta and active-review joins classify
the 55 absent seed identifiers as 38 supporting-field entries and 17 duplicates.
All 38 formerly unselected active classes now have live records. This does not
establish exhaustion of microbial traits. The all-state upstream paedogamy/
pedogamy issue search returned no result on 2026-10-05; concurrent upstream
and consumer feature-PR inventories contain no competing allocation.

## Scope and Hierarchy

| Scope | Count | Parent | Leaves |
| --- | ---: | --- | ---: |
| A: synthetic traits | 1 | METPO:1000059 phenotype | 1 |
| B: predicates | 0 | Not applicable | 0 |
| C: schema enums | 0 | Not applicable | 0 |

This operational class captures separate gametes produced within one
gametangium and then fusing, as defined in the cited diatom literature. Pedogamy
is an exact spelling synonym used by the primary papers. It is not synonymous
with broader automixis, undivided-cell autogamy or paired-cell cytogamy.
Kaczmarska et al. sections 5.2.1-5.2.2 explicitly distinguish the first two
processes; Bagmet et al.'s broader homothallic terminology does not make our
fungal-scoped `traitmech:000609 homothallism` a parent.

Adversarial boundary issue #1719 is repaired in the same branch: autogamy
`traitmech:000622` and its v498 template explicitly exclude fusion of separate
gametes. The new wording preserves postmeiotic mitosis in the ciliate evidence,
does not prohibit later cell division, and imposes no universal immediate
post-meiosis-II fusion. Its formerly unread diatom terminology lead is resolved.
Historical writer behavior and append-only history are preserved. A second
local finding, #1720, restores the explicit same-cell origin of both nuclei;
fusion location alone would not establish self-fertilization.

Use released phenotype `METPO:1000059`, beneath quality `METPO:1000188`,
pending a suitable reproductive-phenotype parent. PHYSIOLOGY is a filesystem
category. Do not assert taxon-level disjointness, universal homozygosity,
recombination rate, environmental trigger, or inability to outcross. Broader
non-diatom usage and exact external equivalents remain curation questions.
No xrefs, SSSOM mappings, protein accessions or causal graphs are asserted.

## Evidence and Limits

- `DOI:10.1080/0269249X.2013.791344`: directly read author-posted terminology
  paper, p.271, sections 5.2.1-5.2.2. Strongest identity source, not independent
  replication of the cited 2008 experiment. Its actual diagrams remain
  uninspected; no numerical result is inferred from them.
- `DOI:10.3390/d14121133`: publisher XML, PDF and Table S1 directly read;
  actual Figure 3 and Results pp.8-9 visually inspected. Gamete-fusion
  interpretation supports the phenotype, not a molecular pathway. Preserve
  the authors' uncertainty around earlier chloroplast images. Four named
  clones were active and two showed no mating. Plastid-marker comparison
  is not a genome-wide recombination test.
- `DOI:10.1007/s12223-008-0018-x`, `PMID:18500631`: directly retrieved
  scientific abstract supports the qualified Neidium cf. ampliatum observation
  and delayed nuclear fusion. Full text, figures and strain provenance remain
  unread; no canonical Neidium taxon mapping is asserted.

Each citation has a short contiguous snippet. The terminology snippets across
both changed records total 24 words. Preserve actual automated resolver verdicts
separately from direct full-text checks; do not add frozen-baseline exceptions.

The canonical example is `NCBITaxon:1302829 Nitzschia acidoclinata`, qualified
to VCA-7. Table S1 links that active clone to naturally collected cave material;
NCBI taxonomy EFetch resolves its species name. Provenance is in the example
note and does not count as another independent trait experiment. No genome or
current strain accession is authenticated. The remaining open discussions cover
mechanisms, wider terminology, external mappings and a narrower parent.

## ID Space and Artifacts

Reserve `METPO:1057700` in fresh block `1057700-1057799` after v499, using
subset `metpo_traitmech_2026_10`. There is one new class row with two 11-column
headers, following Knowledge-Graph-Hub/kg-microbe commit
`ea1c5f15e6c4dba6c72165367162b354e215f018` and CommunityMech v1. No old
block is reassigned: v498 only receives the coupled definition/citation repair.
Definition sources are citations, not ontology mappings. Required empty
trailing ROBOT header cells are preserved.

## Verification

```bash
just verify-proposal metpo_traitmech_v500
just robot-validate-proposal metpo_traitmech_v500
just verify-proposal metpo_traitmech_v498
just robot-validate-proposal metpo_traitmech_v498
just audit-proposal-coverage
just validate-history
just validate-products
just qc
.venv/bin/python scripts/audit_canonical_examples.py --ncbi-api
.venv/bin/python -m pytest -q
```

Both proposal verifiers and ROBOT/ELK checks passed. v500 emitted 23,323
merged and 23,327 reasoned OWL lines; v498 emitted 23,322 and 23,326 lines.
Direct RDF parsing gives 12,629/12,633 triples for v500 and 12,628/12,632
for v498, respectively. This corrects the line/triple unit error in #1722. Structured
inspection confirmed matching definitions, the exact pedogamy synonym, and
labeled w3id phenotype-to-quality ancestry, without legacy METPO parent stubs.
The live taxonomy audit resolved 717 examples across 532 records with zero
errors and 24 existing label-drift warnings.

Snippet verification across both records returned two VERIFIED, one
NOT_IN_ABSTRACT and four UNRESOLVED rows over six references. The new 2013
and 2022 citations remain UNRESOLVED by that resolver; their quoted spans were
checked directly in full text. The 2008 abstract span was VERIFIED. These
manual checks do not replace the recorded resolver outcomes.

Discussions, QC dashboard, trait pages, priority outputs and affected audits
were regenerated. Desktop (1440px) and mobile (390px) browser checks confirmed
identity links, snippets, the canonical example, dashboard counts and no
horizontal overflow or JavaScript errors. The existing mobile theme control
can occlude a small body-text fragment and was not changed here. Of the
existing trait pages, 1,016 changed only in their corpus-count/embedding-coverage
footers; autogamy and phenotype also have expected substantive changes. Both
configured embedding input paths were absent, so embeddings were not rebuilt.

Full validation completed successfully: `just qc`, history/products validation,
repository-wide Ruff and 2,233 pytest tests (two dependency warnings). The 58
focused tests also passed. The ordinary staged whitespace check flags only
v500's three required empty ROBOT directive-header cells; structured 11-column
validation and the documented path-scoped whitespace checks pass.

## Upstream and Round Trip

Submit the verified template to `berkeleybop/metpo`; until acceptance and
release, `traitmech:000624` remains primary. After release, refresh the pinned
ontology, migrate to the accepted CURIE, retain local-ID provenance in migration
artifacts and append-only history, and regenerate products without introducing
a second primary record.

## Change Log

- v501 follow-up, 2026-10-05: the coupled v501 template supersedes this
  standalone phenotype-parent assertion with the new automixis parent;
  paedogamy's definition and ID are unchanged. Correct ROBOT count units (#1722).

- v500, 2026-10-05: propose paedogamy with cited terminology, qualified primary
  observations and a natural-isolate example; repair autogamy boundary #1719
  while retaining same-cell nuclear origin (#1720).
