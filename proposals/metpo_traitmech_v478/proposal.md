# Aerotropism: METPO Proposal v478

## Context

TraitMech adds `traitmech:000601 aerotropism`, a PROPOSED PHYSIOLOGY
class for oxygen-gradient-directed polarized growth. Before this addition,
the live corpus contained 995 records. A fresh temporary METPO seed emitted
399 identifiers: 344 present and 55 absent. Joining both frozen release-review
tables classifies those absences as 38 supporting-field terms and 17
duplicates. The seed projection is not a missing-work queue.

Structured review of the pinned 12,617-triple ontology found no aerotropism
or oxytropism term. Whole-repository novelty and ID-collision searches included
ignored and hidden files, labels, variants, slugs, all three DOIs, PMID,
publisher identifiers, research, proposals and history. No exact record,
proposal or same-scope unresolved mention was found. Live upstream all-state
issue searches returned no aerotropism or oxytropism issue. Open TraitMech
PRs do not add the candidate; the long-lived embedding PR overlaps generated
pages only, and its output is not adopted here.

## Scope

| Scope | Rows | Parent | Leaves |
| --- | ---: | --- | ---: |
| A: local trait lift | 1 | METPO:1000059 phenotype | 1 |
| B: predicates | 0 | Not applicable | 0 |
| C: schema enums | 0 | Not applicable | 0 |

One record uses this local identity. This is a literature-named directional
growth phenotype, not a precomposed oxygen-use, tolerance or assay-result row.
The definition does not identify a protein, receptor, pathway or sequence feature.

## Hierarchy And Boundaries

The local parent is `traitmech:000597 chemotropism`: oxygen is the chemical
gradient that narrows that parent's directional polarized-growth definition.
Its reserved `METPO:1055100` in v474 is not in the released ontology.
Following the closest-existing-METPO-parent rule, this standalone proposal
uses `METPO:1000059 phenotype`, under `METPO:1000188 quality`. It does not
create an unlabeled pending-parent stub. Reconcile the narrower chemotropism
hierarchy upon upstream acceptance of v474. These are w3id METPO IRIs, not
the legacy OBO-prefix namespace. The definition now uses the released
phenotype genus, while the oxygen-gradient differentia preserves the
chemotropism narrowing (#1679).

Positive and negative responses belong in this polarity-neutral class;
both are not required in one organism. This is a scope decision, not a
verified negative-response observation: the Carlile avoidance lead is unread.
Aerotaxis is locomotion, whereas
this record concerns growth orientation. Oxygen demand, tolerance,
germination, biomass and extension rate alone are insufficient. The
oxygen-gradient usage is bounded to this proposal; air-flow
responses belong to rheotropism unless oxygen-gradient evidence also exists.
No unverified oxytropism/anemotropism synonym or external xref is asserted.

No canonical examples or causal graph are added. Two OPEN discussions retain
scope/mapping/hierarchy questions and unresolved control, strain-provenance
and molecular-mechanism questions. Human review is needed before promotion
from PROPOSED. No older source YAML, including protected spore_germination,
is changed.

## Evidence And Access

- DOI:10.1016/S0168-6496(03)00161-2, Damm et al. (2003), PMID:19719598:
  [publisher HTML](https://academic.oup.com/femsec/article/45/3/293/549782)
  methods, results and discussion were read. Section 3.2 separates orientation
  from germination. The modest tube-orientation result is qualified supporting
  evidence, not proof of a receptor or a formally significant bias against
  random orientation. Root signals and oxygen-dependent germination remain
  confounds. Figure captions were read, but images were not visually verified;
  no figure-based mechanism is asserted. The abstract snippet exact-matches
  the raw Europe PMC record. This directly read experimental paper replaces
  the unread Aoki citation as `definition_source` (#1681).
- DOI:10.1155/2012/517529, Brand (2012), PMID:22121367, PMC3216317:
  the [raw Europe PMC JATS full text](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3216317/fullTextXML)
  was directly retrieved. Section 3.2 names aerotropism in Candida under
  hypoxia. This is a review supporting terminology, not independent
  experimental replication or a quantified oxygen-gradient assay. The full
  sentence exact-matches the raw XML, quoted under the source's Creative
  Commons Attribution license. Its cathode and figure clauses describe
  galvanotropism, not aerotropism; the evidence notes make that explicit.
  The publication was online in 2011 and assigned to volume 2012.

Aoki et al. (1998), DOI:10.1007/BF02464003, and Carlile and Tew (1988),
DOI:10.1016/S0007-1536(88)80071-8, are qualified research leads in a
discussion, not counted evidence or definition authority (#1680, #1681).
Publisher retrieval returned 403 and Elsevier/Crossref supplied metadata
only. Indexed summaries suggested positive Candida reorientation and
negative Phytophthora aerotropism; original wording, figures and controls
remain unverified. Brand citing Aoki does not verify Aoki's original text.

Both counted evidence items now have directly checked contiguous snippets.
The original two indexed-text quotes were withdrawn, not relabeled as
verified. Earlier histories are retained with explicit corrections of the
source-provenance and evidence-authority claims.
No missing PMID is inferred from a DOI search failure. The 1973 Robinson
papers and 2023 MEMS oxygen-gradient device are leads, not additional
independently verified evidence or canonical exemplars in this record.

## ID Space And Files

Reserve `METPO:1055500` in the new 1055500-1055599 block after v477,
disjoint from the CommunityMech reference cohort. The local identity remains
`traitmech:000601`; the reserved METPO identifier is not a released term.
Subset: `metpo_traitmech_2026_10`.

| File | Rows |
| --- | ---: |
| metpo_proposal_classes_robot.tsv | 1 class plus 2 header rows |
| proposal.md | Reviewer narrative |

Properties and SSSOM files are omitted because no new predicates or verified
external equivalents are asserted. Both 11-column headers follow the live
upstream contract, including three required trailing directive cells.

## Verification

The guarded writer's seven focused tests pass: scope and evidence limitations,
local/pending parent handling, header parity, dry run, idempotent replay,
independent target/proposal drift refusal and closed-schema rejection before
writing either output. The first local finding (#1676) corrected stimulus
specificity. External review then identified the deeper quote-provenance
problem (#1678) and proposal-genus mismatch (#1679). A second review rejected
new-record baseline exceptions (#1680) and an unread definition authority
(#1681). The writer and tests now preserve directly read evidence, qualified
discussion leads, the released genus and append-only correction history.

The initial PR head passed 2,009 local tests and 45 artifact tests. The
first correction passed all 52 writer/README/priority/QC artifact tests,
34 snippet-audit tests and CI, but review rejected its baseline exceptions.
Those two baseline rows are removed: the baseline is byte-identical to the
base branch and audit logic is unchanged. A new append-only history
withdraws the prior baseline proposal instead of editing its old history.
Final-head checks and resolver outcomes are reported in the PR review log.

ROBOT/ELK adds four lines without unsatisfiable classes. Structured RDF
inspection confirms the w3id phenotype/quality parent chain, no legacy OBO
METPO IRIs and no stub for the pending chemotropism parent. Desktop/mobile
browser checks at 1440px and 390px pass for the new trait and QC dashboard:
correct local identifier link, loaded chart, no page errors or document
overflow. The final evidence presentation is rechecked after regeneration.

All 995 older trait pages were checked: 994 change only the corpus-count
footer; chemotropism also gains its first child. Shared generators match all
139 source files in the reviewed claw archive. Both configured embedding
inputs are absent, so embeddings were not regenerated. The QC chart and
dashboard HTML were regenerated for 996 records and their current slot counts.

Recipes used `UV_NO_SYNC=1` with the existing environment: an initial `uv`
synchronization attempt failed while building optional llvmlite, before
running the generators. No dependency or lockfile changes are included.
Staged whitespace checks pass except for the canonical ROBOT header's three
required trailing empty cells; other TSV lines and all other files are clean.

## Upstream And Round Trip

After review, submit the TSV through berkeleybop/metpo or the KG-Microbe
proposal pipeline. After acceptance, refresh the pinned ontology, seed a
temporary tree, migrate to the accepted CURIE while preserving local-ID
traceability, and reconcile chemotropism parent references and proposal status
in a reviewed change. No upstream issue substitutes for the proposal artifact.

## Change Log

- v478, 2026-10-04: add oxygen-gradient-directed growth with polarity-neutral
  scope, qualified primary-source access and explicit mechanism/exemplar gaps.
- PR #1677 review: withdraw two indexed-text snippets (#1678), align the
  definition genus (#1679), clarify the add-trait skill, and explicitly expose
  the two missing-quote baseline additions for fresh review.
- PR #1677 second review: reject those baseline additions (#1680), move the
  unread papers to research leads, use Damm as definition authority (#1681),
  and add directly read Brand review evidence with its distinct source role.
