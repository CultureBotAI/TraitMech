# METPO proposal v554: fungal adhesive-net trap formation

## Context, scope and hierarchy

Lift `traitmech:000678` as `METPO:1063100`: one reusable morphological
phenotype in one new record, kept `PROPOSED` pending human review.
Scope A: one class. Scope B: zero predicates. Scope C: zero schema enums.

Parent: phenotype `METPO:1000059`, below quality `METPO:1000188`.
This is a three-dimensional hyphal loop network serving as an adhesive
nematode trap, not generic mycelial growth, a root-associated Hartig net,
biofilm, hyphal fusion, individual-cell geometry, standalone adhesive ring,
knob, column, mechanically constricting ring, or generic nematophagy.
Existing mycelial growth is explicitly bacterial; hyphal anastomosis denotes
fusion rather than trap identity. No exact node/synonym/TODO requires repair.
Closer hierarchy remains open. No exact synonyms, xrefs, SSSOM equivalences
or organism-level disjointness are asserted. Trap formation alone does not
demonstrate adhesion or successful capture in every condition.

## Evidence and limits

- [Yang et al. 2011](https://doi.org/10.1371/journal.ppat.1002179): primary XML,
  Introduction, trap-formation Results, relevant strain/proteomics Methods,
  actual Figure 1 and Text S1 induction/interaction Methods were inspected.
  The contiguous snippet comes from **Author Summary**, not scientific abstract.
  Nematode-extract induction and subsequent live-prey interaction are distinct
  assays. Formation, adhesion, capture, penetration and digestion are distinct
  endpoints. Proteomic correlations are not causal gene requirements.
- [Zhang et al. 2022](https://doi.org/10.3390/jof8070671): published 26 June.
  Primary XML, isolation Methods, all six taxonomic descriptions and actual
  Figure 2 were inspected. The snippet is from the A. eryuanensis description,
  not the abstract. Figure 2i shows a network, not time-resolved capture.
  Source provenance distinguishes holotype CGMCC3.19715 from ex-type culture
  DLUCC 14-1. This corrects a draft-only conflation found in adversarial review
  [#1825](https://github.com/CultureBotAI/TraitMech/issues/1825), before YAML
  generation. Freshwater sediment material came from Xihu Lake, Eryuan.

Canonical example: `NCBITaxon:756982`, live exact strain label **Orbilia
oligospora ATCC 24927**. The 2011 Methods identify the historical A. oligospora
strain and soil origin in Sweden; [ATCC 24927](https://www.atcc.org/products/24927)
independently confirms origin and former name. ATCC is authority/provenance
support, not a third independent trait study. The source's O. auricolor
teleomorph wording is not imported as current equivalence. No universal prey,
medium, lectin requirement, all-isolate distribution or field efficacy is
asserted. Protein-resolved graphs require further perturbation/supplement and
taxon-paired accession review. Mechanism is deferred, not claimed absent.

## Allocation and novelty

Reserve **traitmech:000678**, cohort **v554**, and the entire
**METPO:1063100-1063199** block; only 1063100 is populated. This follows
v553's 1063000-1063099 block without CommunityMech v1 overlap.
Subset: `metpo_traitmech_2026_10`.

Allocation main: `dc6dcf61f9ef2f873c6379667108c18a1f983b9f`.
Ignored-and-hidden searches covered all 20 then-existing TraitMech worktrees,
the entire CommunityMech checkout, and a complete fresh open-PR curation
snapshot: 22 roots. Searches included adhesive/hyphal-net and trapping
variants, Arthrobotrys, Orbilia oligospora, both DOI/PMID/PMC identifiers,
strain identifiers, local ID, cohort and the full hundred block. Inspected
matches were generic networks, root Hartig nets, the constricting-ring scope
exclusion, cached prey-attraction citations, lexical coincidences and numeric
fixtures, not exact records or reservations. Parsed pinned METPO contains
12,617 triples and no exact class. A fresh 399-record seed has 55 IDs absent
from the 1,072-record corpus, none an exact adhesive-net term; it is not a
curation queue or a claim of exhausted trait discovery.

Complete paginated open-head inventory, including drafts, at allocation:

| PR | Head | Reservation |
| --- | --- | --- |
| #1802 | `a74d9278b3ce5971d773a4e81616373f795f2816` | existing Shedu; no new ID/block |
| #1782 | `35099af2b7d5347f2ca6e418c4a139979071644d` | none in changed curation paths |
| #1476 | `a138e46f803b5af9d48969217b86cf7c9a3b61bd` | none in changed curation paths |
| #973 | `331f9517bbdf4d2c9fa97b338ee59a8986f2f174` | none in changed curation paths |
| #924 (draft) | `e61ce120b8da953da097b9f94bfed7f292e5675a` | none in changed curation paths |

File counts, selected immutable curation blobs and head stability checked.
Recheck main and reservations before publication.

## Artifacts and verification

One class TSV has two 11-column headers and one class row; no properties or
SSSOM file is needed. Preserve three empty trailing ROBOT directive cells.
Upstream skill/templates at `1408e7099d039026d7611c240938d8e177753406` were
read and revalidated against live immutable GitHub blob identities: class
`b590cf303dc2fbdd57bed021668641cd0c32396d`, property
`b2f9f4ceb6b6893a8b27d7fe41e859f08c4b2990` (11/13 columns).
Use maintained w3id METPO prefix, not the upstream legacy OBO example.

Required verification: proposal verifier, ROBOT template/merge/ELK, parsed
OWL identities, strict/LinkML/history/QC/product gates, snippet resolver with
honest direct-source fallback, live NCBI, focused/full tests and browser QA.
Actual results belong in the PR receipt, not presumed here. Current add-trait
guidance already covers source sections, provenance, scope boundaries and
sequence-versus-phenotype limits; no skill change is required for this record.

## Upstream and round trip

After human signoff submit the TSV to berkeleybop/metpo. No upstream issue
or accepted METPO term is claimed. After release refresh pinned ontology,
re-seed the accepted term and migrate the local identifier while retaining
its provenance. Do not emit the reserved ID as an already released term.

## Change log

- v554, 2026-10-08: initial proposal; corrected draft culture roles (#1825).
