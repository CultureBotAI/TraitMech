# Automixis: METPO Proposal v501

## Context

Add `traitmech:000625 automixis`, a PROPOSED PHYSIOLOGY class, and resolve
the parent gaps on autogamy, cytogamy and paedogamy. Ignored-and-hidden
whole-repository searches included labels, synonyms, meiotic-origin terminology,
source identifiers, the local ID and the full placeholder block. Existing
automixis mentions were broader-term discussions, not an exact primary record.
Available CommunityMech proposals had no conflicting term or allocation.

A fresh 399-record METPO seed shares 344 IDs with the pre-addition corpus of
1,019 records. Complete release-delta and active-review joins classify the
55 absent seed IDs as 38 supporting-field terms and 17 duplicates; all 38
formerly unselected active classes now have records. This is not an exhaustion
claim. The all-state upstream automixis/automictic/intratetrad issue search
returned no result on 2026-10-05. Full file inventories of the four open
TraitMech PRs and four open METPO PRs contained no competing allocation.

## Scope and Hierarchy

| Scope | New Classes | Existing Classes Updated | Parent |
| --- | ---: | ---: | --- |
| A: synthetic traits | 1 | 3 | METPO:1000059 phenotype |
| B: predicates | 0 | 0 | Not applicable |
| C: schema enums | 0 | 0 | Not applicable |

The genus is reproductive phenotype, not necessarily sexual reproduction.
The definition retains both fusion and non-fusion automixis, excludes ordinary
reduced meiotic progeny and distinguishes nuclear origin from cytoplasmic
exchange. It allows postmeiotic descendants and compensating premeiotic
endomitosis rather than requiring immediate fusion or constant somatic ploidy.

Autogamy `METPO:1057500`, cytogamy `METPO:1057600` and paedogamy
`METPO:1057700` retain their identifiers, definitions, evidence and examples.
Their narrower same-cell-origin reproductive events fit this parent. The
existing diatom terminology explicitly places autogamy and paedogamy beneath
automixis; the existing cytogamy evidence supports same-parent meiotic origin
despite pairing. Mogie's contrast with botanical/mycological autogamy from
different meioses does not contradict our narrower operational autogamy class.
None of these terms, all selfing, homothallism or intratetrad mating is asserted
as an exact synonym of the broad parent. Remaining mapping and terminology
questions keep the children's multipurpose discussions OPEN while their
parent gap is explicitly resolved.

This four-row cohort supplies the actual parent in the same ROBOT input.
v498-v500 remain standalone historical templates under released phenotype;
v501 supersedes their direct-parent assertions for the combined hierarchy.
Do not import the old flat templates instead of this coupled cohort when
reviewing the new hierarchy. Retained phenotype ancestry would be redundant,
not contradictory, if all cohorts were combined. No IDs are reassigned.

## Evidence and Limits

- `DOI:10.1111/j.1095-8312.1986.tb01761.x`: strongest broad identity
  authority; publisher scientific abstract directly read. Full text unread.
  A terminology argument, not independent microbial experimental replication.
- `DOI:10.1186/s13059-021-02521-w`, `PMID:34732243`, `PMC8567612`:
  primary yeast study; publisher HTML and Europe PMC XML read. Actual Figure 1
  and all three pages of Table S1 inspected. Main Methods read, detailed
  supplementary methods and other figures unread. No universal molecular
  mechanism or strain-specific automixis rate is claimed.

Both new evidence items carry short contiguous snippets. Canonical
`NCBITaxon:36035 Saccharomycodes ludwigii` is qualified to the NBRC 1721
strain family depicted in Figure 1C; Table S1 supplies wild-parent provenance,
not an independent phenotype experiment. NBRC 1722 is distinguished from the
wild diploid parent. NCBI EFetch resolved the species name. Provenance and
authority URLs are retained in the example note. No genome/protein accession,
external xref, SSSOM mapping or causal graph is added.

## ID Space and Artifacts

Reserve `METPO:1057800` in fresh block `1057800-1057899`, after v500,
with subset `metpo_traitmech_2026_10`. Preserve the three existing child IDs.
The template follows the pinned kg-microbe contract at
`ea1c5f15e6c4dba6c72165367162b354e215f018` and CommunityMech v1.
Two 11-column headers retain three required empty directive cells.
Definition sources contain citations, not ontology mappings.

| Artifact | Rows |
| --- | ---: |
| metpo_proposal_classes_robot.tsv | 4 classes |
| property template | Omitted, no predicates |
| SSSOM mappings | Omitted, no equivalent external class asserted |

## Verification

The maintained proposal verifier and ROBOT merge/ELK checks passed. Direct RDF
inspection confirmed all four definitions, labeled w3id parents and the full
automixis-to-phenotype-to-quality ancestry, without legacy METPO parent stubs.
v501 emitted 23,374 merged and 23,378 reasoned OWL lines; parsed graph
cardinalities are 12,659 and 12,663 triples, respectively.

LinkML for all four records, strict validation, `just qc`, history/products,
repository-wide Ruff and the skill validator passed. Full pytest: 2,252 passed
with two dependency warnings. The 19 new writer tests and 45 focused artifact
tests also passed. Live taxonomy resolved 718 examples across 533 records with
zero errors and 24 existing label-drift warnings.

Snippet verification returned UNRESOLVED for Mogie and NOT_IN_ABSTRACT for the
yeast Background quote. The exact Mogie DOI query returned zero Europe PMC
records; the publisher abstract was read directly. The yeast span was checked
in full-text XML. Neither manual check is relabeled as an automated VERIFIED
result, and the frozen snippet baseline is unchanged.

Discussions, QC dashboard and coverage image, pages, priority products and the
proposal citation audit were regenerated. Of the existing pages, 1,015 have
footer-only changes; three children and phenotype have expected hierarchy and
provenance changes. Both configured embedding input paths were absent, so
embeddings were not rebuilt. Playwright checks at 1440px and 390px passed
identity, evidence, provenance, parent links, dashboard counts/image, no
horizontal overflow and no JavaScript errors. The existing mobile theme button
can slightly occlude body text and is not claimed fixed here.

The ordinary staged whitespace check flags only the template's three required
empty ROBOT directive cells. Structured 11-column validation and the documented
path-scoped whitespace checks pass.

The same branch corrects #1722 in v500's narrative: ROBOT's 23,323/23,327
are physical OWL line counts, not RDF triple counts. Direct parsing found
12,629/12,633 triples for v500 and 12,628/12,632 for v498. No scientific data,
validator behavior or append-only history is altered by that reporting fix.
The add-trait skill now explicitly distinguishes those two count units.

## Upstream and Round Trip

Submit this coupled cohort to `berkeleybop/metpo`; all four local records
remain PROPOSED until human review. After acceptance and release, refresh the
pinned ontology, migrate to accepted METPO IDs, preserve old local-ID
provenance in migration artifacts and append-only history, and regenerate
products without adding duplicate primary records.

## Change Log

- v501, 2026-10-05: add broad automixis, reparent three operational children
  without changing their meanings, and correct v500 count units (#1722).
