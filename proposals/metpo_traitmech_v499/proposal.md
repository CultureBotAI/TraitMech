# Cytogamy: METPO Proposal v499

## Context

Lift `traitmech:000623 cytogamy`, a PROPOSED PHYSIOLOGY class. Pre-write
searches included ignored and hidden files across the whole repository and
available CommunityMech proposals, including labels, double-autogamy usage,
source identifiers, the local ID and the entire proposed block. Cytogamy
appeared only in autogamy scope notes and their supporting/generated artifacts,
not as an exact primary record. The related live autogamy discussion is updated
on this branch; its historical proposal and writer remain unchanged.

A fresh 399-record seed shares 344 identifiers with the 1,017-record pre-addition
corpus. The 55 absent identifiers comprise 38 supporting-field entries and 17
duplicates in the complete release-review joins. All 38 formerly unselected
active classes now have live records. Deprecated reproductive-process and
structure entries do not supply an active exact phenotype parent. This is not
an exhaustive microbial-trait inventory.

On 2026-10-05 an all-state upstream cytogamy issue search returned no result.
File inventories of METPO PRs #639, #638, #637 and #629 and TraitMech PRs
#1477, #1476, #973 and all 692 files of #924 showed no competing allocation.

## Scope and Hierarchy

| Scope | Count | Parent | Leaves |
| --- | ---: | --- | ---: |
| A: synthetic traits | 1 | METPO:1000059 phenotype | 1 |
| B: predicates | 0 | Not applicable | 0 |
| C: schema enums | 0 | Not applicable | 0 |

Paired-cell internal gametic-nuclear fusion without gametic-nuclear exchange is
distinct from ordinary conjugation with exchange and from the operationally
unpaired-cell definition of `traitmech:000622 autogamy`. Diller (1958) calls
his tentative observation double autogamy. Preserve that broader terminology
without asserting subsumption under our unpaired class or an exact synonym.
No universal homozygosity, hyperosmotic trigger, nuclear count, inability to
outcross, species-level disjointness or sequence-feature interpretation is used.
Local adversarial issue #1717 tightened the definition to exclude one-way
transfer too, using an individual paired-cell formulation rather than requiring
the same outcome in both partners. Historical source wording is unchanged.

Use released `METPO:1000059 phenotype`, beneath `METPO:1000188 quality`,
pending a narrower reproductive-phenotype parent. PHYSIOLOGY is a filesystem
category. Keep PROPOSED pending human curator signoff. No synonyms, xrefs,
SSSOM mappings, canonical taxa, protein accessions or causal graphs are asserted.

## Evidence and Limits

- `DOI:10.1017/S0016672300010740`, `PMID:4964874`: definition on p.39,
  directly checked in the typeset PDF. The surrounding Table 2 discussion
  offers cytogamy as an explanation for marker outliers, not direct observation
  in those clones. This passage supports terminology, not replication.
- `DOI:10.1111/j.1550-7408.1958.tb02567.x`: directly read Wiley scientific
  abstract. Preserve its tentative wording and double-autogamy terminology.
  Unobserved passage through paroral cones is not a genetic exclusion of
  exchange. The natural collection context does not remove that uncertainty.
  Full text and actual figures/tables remain unread.
- `DOI:10.1093/genetics/91.4.657`, `PMID:17248904`, `PMC1216858`: scientific
  abstract directly retrieved through Europe PMC and NCBI PMC EFetch.
  Hyperosmotic-shock-induced Tetrahymena results support the phenotype, but
  the source-specific homozygote interpretation is not imposed universally.
  Full text, Methods and actual figures/tables remain unread. PMC EFetch
  withholds body XML and public PDF attempts did not yield a readable PDF.
  No natural strain provenance or protein-resolved pathway is inferred.

All three citations have short contiguous snippets. Wichterman (1940),
`DOI:10.1002/jmor.1050660303`, is metadata-verified but otherwise unread;
it remains a discussion research lead, not counted evidence. Preserve actual
resolver verdicts separately from direct PDF and publisher/API checks.
The maintained resolver returns VERIFIED for Orias and Hamilton and UNRESOLVED
for the other two sources. An exact DOI query retrieves the matching 1967 PMID
without an abstract; the exact 1958 DOI query returns no Europe PMC record.
Neither outcome invalidates the directly read publisher sources.

## ID Space and Artifacts

Reserve `METPO:1057600` in fresh block `1057600-1057699` after v498, with
subset `metpo_traitmech_2026_10`. The class template has one row and two
11-column headers, following Knowledge-Graph-Hub/kg-microbe commit
`ea1c5f15e6c4dba6c72165367162b354e215f018` and CommunityMech v1.
No property or mapping template is needed. Citations are definition sources,
not equivalence mappings. Required empty trailing ROBOT-header cells are kept.

## Verification

```bash
just verify-proposal metpo_traitmech_v499
just robot-validate-proposal metpo_traitmech_v499
just audit-proposal-coverage
just validate-history
just validate-products
just qc
.venv/bin/python -m pytest -q
```

Require record/template parity and inspect the actual labeled w3id class,
phenotype parent and quality ancestor, not just ELK status. Run snippet
verification, regenerate discussions, QC dashboard, pages, priority outputs
and affected audits, and inspect desktop/mobile rendering. No taxonomy or
protein assertions were added or changed.

Local ROBOT/ELK passed without UNSAT (23,322 merged lines; 23,326 reasoned
lines). Structured inspection confirms the current definition and labeled
w3id cytogamy-to-phenotype-to-quality chain. Browser checks at 1440 and 390 px
confirm the local identifier's GitHub provenance link, three evidence snippets,
updated autogamy discussion and 1,018-record QC dashboard, with no horizontal
overflow or JavaScript errors. Both exact configured embedding-source paths
are absent, so embedding artifacts were not regenerated. The QC PNG was
regenerated but is byte-identical to the previous image.

## Upstream and Round Trip

Submit the verified template to `berkeleybop/metpo`. Until acceptance and
release, `traitmech:000623` remains primary and the proposed METPO ID is not
a released identifier. After release, refresh the pinned ontology, migrate
to the accepted CURIE, preserve the local ID in migration artifacts and
append-only history, and regenerate dependent products without a second
primary record.

## Change Log

- v501 follow-up, 2026-10-05: the coupled v501 template supersedes this
  standalone phenotype-parent assertion with the new automixis parent;
  cytogamy's definition and ID are unchanged.

- v499, 2026-10-05: propose cytogamy with three cited snippets and explicit
  pairing, tentative-observation, induced-system and source-access limits.
