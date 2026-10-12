# Replicative Aging (v585)

## Context And Scope

This cohort proposes an ontology home for `traitmech:000709`,
`data/traits/physiology/replicative_aging.yaml`. The record remains
`PROPOSED`, pending human scientific sign-off. It denotes an age-dependent
cellular performance phenotype, not a lifespan value, sequence feature or
individual experiment.

| Scope | Records | Parent | Leaves |
| --- | ---: | --- | ---: |
| A: accepted local trait | 1 | `METPO:1000059` phenotype | 1 |
| B: causal predicates | 0 | Not applicable | 0 |
| C: schema vocabulary | 0 | Not applicable | 0 |

No exact synonym, external equivalence, canonical taxon, protein-resolved
graph or negative companion is asserted. Property and SSSOM files are omitted.

## Evidence And Boundaries

The definition follows the performance-decline framework in
[Lapinska et al. 2019](https://doi.org/10.1098/rstb.2018.0442)
(PMID:31587633, PMC6792439). Its Figure 2 caption supplies a directly checked
full-text snippet; the plotted early trend and later flattening were visually
inspected in the author's PDF. The record retains the discrepancy between
the Introduction's BW21113 and Methods' BW25113 rather than assigning a taxon.

[Ackermann et al. 2007](https://doi.org/10.1186/1471-2148-7-126)
(PMID:17662151, PMC2174458) supplies separate bacterial evidence and an
abstract definition. Its combined survival/reproduction endpoint and mutant
strain provenance are preserved in the record.

[Spivey et al. 2017](https://doi.org/10.7554/eLife.20340)
(PMID:28139976, PMC5332158) provides boundary evidence, not a positive example:
finite lifespan does not establish the defined phenotype. Its snippet is from
the scientific abstract, not the editorial digest.

[Horkai et al. 2023](https://doi.org/10.1371/journal.pbio.3002245)
(PMID:37643155, PMC10464975) separates lifespan from functional decline in an
engineered yeast assay. Its Results snippet was checked in publisher text
and primary XML. The paper's broader use of replicative ageing includes
age progression without senescent decline. That is not an exact synonym of
this proposal's operational meaning; the label boundary remains an explicit
upstream curation question.

Age-specific performance or mortality risk is required. Endpoint death,
cumulative survival loss, old-pole identity, a sibling difference or a marker
alone is insufficient. A measured decline can plateau without being absent.
Neither universal aging nor a universal molecular cause is claimed.
Nondividing-culture survival and mammalian cell-cycle arrest are not equated
with this phenotype. Figures other than the 2019 Figure 2, supplements and
raw datasets were not independently assessed. MED/Crossref notice fields were
checked; incomplete publisher access prevents an exhaustive notice claim.

## Hierarchy Decisions

Use the active `METPO:1000059` phenotype class under `METPO:1000188`
quality. Both pinned and current released RDF resolve its IRI to
`https://w3id.org/metpo/1000059`; do not create a legacy OBO-namespace stub.
Existing records remain unchanged. In particular, the gram-variable
`culture_aging` node explicitly means stationary-phase conditions, not this
cell-lineage phenotype. No same-scope unresolved node or synonym was found.

## Novelty And Reservation

The 2026-10-12 check used main
`53188095ebb645d2e21bf2d5dbe6548046190279`. Whole surviving TraitMech
worktree roots were searched with ignored and hidden files included, covering
records, proposals, research, history, raw ontology and generated products.
There were 22 registered roots, four with usable Git metadata. For the other
18, surviving files and the registered historical tracked trees were checked
separately. Unavailable current ignored/untracked files cannot be reconstructed;
no claim covers unregistered work, binary internals or unpacked archives.

A known-positive control exposed unsupported word boundaries in the initial
historical extended-regex search. Those results were excluded from absence
reasoning and all affected trees were searched again with verified PCRE.
The later interval search also required literal Unicode dashes rather than
Python-style Unicode escapes; a fatal exit was not treated as no matches.

The live baseline has 1,103 records. A fresh 399-record seed projection has
344 IDs already present and 55 absent leads; none is an exact aging record.
The 1,546-row release delta and 153-row active review were treated as frozen
decisions, not current absence. Existing lifespan qualifications, host/nodule
senescence, old-pole morphology and culture-age staining mentions were read
and rejected as exact equivalents.

Reservation checks covered 584 TraitMech cohorts, 6,295 interval occurrences
across the inspected current/historical/upstream sources, and proposal files
from 127 registered CommunityMech roots plus available historical trees.
No collision was found for the local ID, cohort or full hundred block.

Fresh, paginated changed-file lists covered TraitMech PRs #1782, #1476,
#973 and draft #924 (692 files across seven pages); CommunityMech draft
#935; and METPO PRs #644, #643, #641, #640, #638 and #629. Open sets and
heads were stable. Complete changed METPO ontology/template blobs were
checked, not only patches. Discovery also checked 644 METPO issue/PR bodies
and 654 comments; the only aging-vocabulary hit concerned dependency-cache
lifespan, not microbial biology.

Fresh upstream heads matched immutable snapshots whose file bytes were
reverified using Git blob SHA and SHA-256:

- METPO: `1efc8c73009200b9cb74d125df6a0ea5dc36cb93`.
- CommunityMech: `80049bcc9195480a58633236169b62f86c23489a`.
- KG-Microbe: `bac582f4e131a7ba96b585996ae1fa759403f0b6` (`master`).

Pinned and current released METPO RDF, editable metadata, templates and
pending changes exposed no exact active or deprecated candidate. The sparse
editable root was not used alone to establish absence. No ontology upgrade
is included. Recheck main and pending reservations before publication; these
checks neither eliminate allocation races nor establish discovery exhaustion.

## ID Space And Subset

- Local identifier: `traitmech:000709`.
- Cohort: `metpo_traitmech_v585`.
- Full reserved block: `METPO:1066200`-`METPO:1066299`.
- Only populated placeholder: `METPO:1066200`, not a released METPO ID.
- Subset: `metpo_traitmech_2026_10`.
- No historical block is reused; CommunityMech v1 and subsequent inspected
  reservations are separate.

## Files And Verification

| File | Content |
| --- | --- |
| `metpo_proposal_classes_robot.tsv` | Two canonical headers and one class row, 11 columns |
| `proposal.md` | Scope, source limitations, allocation and migration rationale |

The guarded writer, `scripts/add_replicative_aging_trait.py`, defaults to a
validated dry run and refuses target, parent or template drift. Its headers
match the checked upstream class template. Citation fields are provenance,
not equivalence mappings. Required validation:

```bash
just verify-proposal metpo_traitmech_v585
just robot-validate-proposal metpo_traitmech_v585
just qc
just validate-history
just validate-products
```

Actual outcomes will be recorded in the saved structured review and PR.
Inspect the emitted RDF as well as ROBOT exits. Preserve required trailing
header cells; only the inspected TSV receives a scoped whitespace exception.

## Upstream Path And Round Trip

After local review, submit this template and rationale to `berkeleybop/metpo`
or the KG-Microbe proposal pipeline. Curator `codex`, the LLM-assisted event
and append-only history document authorship. Upstream maintainers decide
the final label, hierarchy and identifier.

After an explicitly reviewed ontology update contains the accepted term,
re-seed that release and migrate the record and dependent references while
retaining `traitmech:000709` as a traceable identifier alias and preserving
history. Do not silently refresh the pinned ontology or present the proposal
placeholder as an already released term.

## Change Log

- v585, 2026-10-12: propose one operational aging phenotype with four primary
  DOI references, checked snippets and explicit terminology/evidence limits.
