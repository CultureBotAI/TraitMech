# Next Tasks — TraitMech backlog

Deferred work, each entry with enough context to pick up cold. **Maintenance:**
update this file as work is started/finished — move done items out, add new
deferrals here. Keep the cross-Mech items in sync with the sibling repos'
`NEXT_TASKS.md` (CultureMech / MIM / CommunityMech).

Last reconciled: 2026-08-01. Open issues: **#151** (web design review — 2 residual
front-end items, section 6), **#183** (causal-graph fragmentation — detection has
landed, the backfill is what remains, section 5), **#191**/**#192**/**#193** (from
the #190 review — no drift check on the vendored history schema, the claw guard
implemented twice, the dashboard's embedded timestamp), and **#197**/**#198**/**#199**
(from the #196 review — hub-availability coupling, the same paths-filter gap in the
sibling repos, concurrency scoping; all section 2). **#184** is closed by #196.
Open PR: **#196**. Everything merged in this repo through **#190** (2026-07-31),
plus the claw-side architecture decisions through 2026-07-25, is reflected below.

## 1. Embedding coverage — DONE (98.3%); residual is legitimately absent

`just build-embeddings` now matches **469/477 TraitRecords (98.3%)**:
349 `direct_metpo` + 120 `parent_proxy`. The parent-proxy tier (added to
`scripts/build_embedding_index.py`) walks `parent_traits` transitively to the
nearest ancestor CURIE present in the deepwalk and borrows its embedding, so
the 120 synthetic `traitmech:` traits now get a UMAP point near their semantic
parent (clearly tagged `parent_proxy`).

The remaining **8 `no_match`** are abstract value-carrier properties
(`METPO:2000058`–`2000063`, `2000071`, `2000103` — `has value`, `has observed
spot value`, `capable of`, …); they have no meaningful node embedding and are
left absent by design. Re-deriving real embeddings for the newly-minted METPO
classes would need a fresh kg-microbe deepwalk run (post-2026-04-25). No
further action unless a newer deepwalk lands.

## 2. id↔label validator — ADOPTED + ENFORCING (Phase 2) — DONE

TraitMech joined the Mech group — the byte-identical vendoring is now a **4-repo
invariant** (CultureMech / MIM / CommunityMech / TraitMech): the validator + the
three shared tests + `chem_formula.py`.
`conf/id_label_targets.yaml` targets the two ontology grounding tables
(`mappings/node_grounding.tsv`, `mappings/predicate_grounding.tsv`) with
CHEBI/GO/ENVO/PATO/RO adapters; METPO/traitmech/biolink/rdfs/UniProtKB are
ignored prefixes. Recipes: `validate-products`, `report-label-drift`. CI workflow
`label-correspondence.yaml`: `vendored-sync` drift check + `validate-products`
both **blocking**.

Update (2026-07-21): the self-generated sha256 pin was **retired** (Phase 2 step
2d). It only compared a copy to a hash from the *same* repo, so all four could
pass while diverged. The `vendored-sync` job now runs `scripts/check_vendored_sync.sh`,
which diffs the vendored files against `CultureBotAI/CultureMech@<scripts/.vendored_canon_ref>`
— the reference lives in another repo, so a one-copy edit fails CI. Deleted:
`verify-/refresh-validator-pin`, the `VENDORED_IDLABEL_FILES` manifest, and
`scripts/.validate_id_label_correspondence.sha256`. Propagation: PR into the hub →
merge → bump `.vendored_canon_ref` here. (`schema-pin` was a separate set at the
time; it was retired the same way in #182 — see below.)

The 15 pre-existing MISMATCHES found at adoption were all wrong CURIEs in
`mappings/node_grounding.tsv` (e.g. `PATO:0000383` is "female", not "decreased
temperature"); corrected to the right CURIEs (verified vs OAK) and the trait-YAML
`grounding:` values re-migrated. One curator-accepted residual stays green via
`exceptions:` (`PATO:0001717` "light intensity" — OAK canonical is the awkward
"radiation emitting intensity quality"). Gate now reports 113 OK_CANONICAL +
2 OK_SYNONYM + 1 OK_EXCEPTION, 0 errors.

Update (2026-07-22): more vendored-file fixes landed through the hub-and-spoke
model.
- **`chem_formula.py` fixes** (TraitMech #174, propagated to all four): hydrate
  separators (`CaCl2 2H2O`, `CuSO4 . 5H2O`) and R-prefixed elements
  (`ClRb`/`RuCl3` no longer misread as generic R-groups). Validated byte-for-byte
  against CultureMech's 23,129 real ingredient labels — zero regressions.
- **Plausibility-gate CCCP fix** (hub CultureMech#110 → spokes TraitMech #178 /
  MIM #155 / CommunityMech #241): an exact match to a term's own label/synonym
  now short-circuits before the formula check, so an abbreviation that IS the
  canonical label (`CCCP` on CHEBI:3259, formula C9H5ClN4) is no longer flagged
  IMPLAUSIBLE_LABEL. Found by enabling the gate over MIM's corpus.
- **Plausibility gate ENABLED in MIM** (#155) — its ingredient labels are
  formulas like CultureMech's. TraitMech's own gate stays OFF by design (its
  groundings are GO/CHEBI/PATO with prose labels; enabling it surfaces nothing).

Update (2026-07-25): **the CultureMech → claw relocation was ABANDONED, not
deferred.** Do not treat "repoint each Mech's `CANON_REPO` to
`CultureBotAI/culturebotai-claw`" as ready-to-run work — it is superseded by the
claw-as-mirror decision, and the old "blocked on making claw public" framing was
wrong twice over. Sequence:
- **#181** repointed `check_vendored_sync.sh` at a *local* claw checkout
  (`$CLAW_ROOT` or sibling auto-discovery) after `culturebotai-claw#18` put a
  canonical copy in `shared/idlabel/`. Because claw is private, the tokenless
  `raw.githubusercontent` fetch 404s, so the network path was unavailable.
- That variant **skipped and exited 0 when no claw checkout was present**, which
  is always the case in CI — so TraitMech's `vendored-sync` job was silently
  passing without checking anything.
- **#182** (merged 2026-07-22) restored enforcement: `check_vendored_sync.sh` is
  back to the canonical CultureMech raw-fetch version (byte-identical to
  MIM/CommunityMech), `.vendored_canon_ref` reset from the claw commit
  (`1ad5d408`) to the CultureMech canon commit (`6be694f3`), and the check now
  diffs **6** files and fails on drift. Companion PRs: CultureMech #112,
  MIM #157, CommunityMech #247.
- Claw-side, the mirror briefly tried to become the enforcer: **claw#21**
  ("Enforce id-label vendored files match claw canonical", merged 2026-07-22) was
  **reverted by claw#22** (merged 2026-07-25) as off-model — claw is a mirror,
  not the fleet enforcer.

Also folded into #182: **`src/traitmech/schema/mech_shared.yaml` is now covered by
the drift check** (path-mapped to CultureMech's `src/culturemech/schema/`), and the
separate `schema-pin` mechanism was retired — `verify-/refresh-schema-pin`,
`SHARED_SCHEMA_MODULE`, and `src/traitmech/schema/.mech_shared.sha256` are deleted.
It had the same self-referential blind spot as the validator sha256 pin. There is
no remaining self-generated pin in this repo.

**Steady-state topology (claw#19, restated in claw#22).** CultureMech is the hub;
`claw/shared/idlabel/` is a **passive mirror** of it plus an isolated test-runner.
Two directions are covered, both nightly:
- **mechs == hub** — CultureMech's `scripts/audit_vendored_fleet.sh`, run by the
  `vendored-fleet-audit.yml` workflow.
- **mirror == hub** — claw's `matches-hub` job in `id-label-canon.yaml`. It used
  to trigger only on claw-side changes, so it could never see *the hub* moving —
  precisely the window it existed to close (claw#23); **claw#24** (merged
  2026-07-25) added the nightly schedule that fixes it.

Changing a vendored file still means: PR into CultureMech → merge → bump
`.vendored_canon_ref` in each spoke. Claw remains private, and that is fine — it
blocks nothing now that the repoint plan is gone.

Health as of 2026-07-30: CultureMech's `vendored-fleet-audit` has been green
nightly through today, claw's `id-label canonical` and `Cross-repo validation`
have both succeeded daily since 2026-07-25, and all three spokes (MIM,
CommunityMech, TraitMech) pin the same `scripts/.vendored_canon_ref`
= `6be694f3d6308ac0f4c2e0dcf196e2ff73f6468f` against `CultureBotAI/CultureMech`.
The 4-repo vendored invariant is healthy.

**The PR-time hole (#184) is FIXED here — #196.** The `vendored-sync` job sat
behind a `paths:` filter narrower than the list of files it checks: of the six
`check_vendored_sync.sh` compares, only
`scripts/validate_id_label_correspondence.py` was in `trigger_paths`. Nor were
`scripts/check_vendored_sync.sh` or `scripts/.vendored_canon_ref`, so editing the
checker or reverting the pin fired nothing — **#182 rewrote the checker and
changed the pin without this job running once**, and the workflow had not run at
all between 2026-07-22 and #196.

The cause was a 7s bash+curl job sharing a filter with a ~2min OAK-backed one.
#184's suggested fix — derive the filter from the checker's `FILES` array — is
**not implementable**: GitHub evaluates `paths:` from static YAML before
checkout, so it cannot read the repo. #196 therefore moved `vendored-sync` to its
own workflow with no filter at all, plus a 3-attempt retry (in the workflow, not
in `check_vendored_sync.sh`, which has no canonical copy in the hub to diff
against — CommunityMech#278).

**Still open, fleet-wide: #198.** Verifying #184 showed the gap is not
TraitMech-specific. CultureMech and CommunityMech also omit `chem_formula.py` and
all three `tests/test_id_label_*.py` — their `src/<pkg>/schema/**` glob covers
only `mech_shared.yaml`. So every repo readable on 2026-08-01 has a four-file
hole; TraitMech had a fifth, now closed. MIM is unverified (`gh api` 404s on its
workflow file). MIM#160 and CommunityMech#280 are the same defect; worth one
cross-Mech sweep (`cross-mech-sync`) with #196 as the reference implementation,
rather than three PRs. Also open from #196's review: **#197** (running on every
PR couples all PRs to CultureMech's availability). Distinct from
CommunityMech#278, which is about *what* is compared — the checker itself has no
canonical copy in the hub
— where these three are about *when* the comparison runs.

## 3. Trait promotion PROPOSED -> REVIEWED — DONE

All categories are promoted: the corpus is **427 REVIEWED + 50 DEPRECATED,
0 PROPOSED**. The 50 DEPRECATED are observation-value carriers, deliberately
out of scope (see `docs/DEPRECATED_REPLACEMENT_PROPOSAL.md`). No promotion work
remains.

## 4. METPO upstream round-trip (BLOCKED on upstream) + residual floor

- Causal-graph grounding now stands at **predicates 85% (1094/1284)** and
  **nodes 62% (1024/1643)**. The remaining residual is non-ontological
  graph-narrative phrases (adaptation states, composite descriptors) and vague
  verbs — these are NOT ontology concepts and should stay as free-text node/edge
  labels, not be force-matched or proposed. This is the quality floor.
- Genuinely-novel recurring concepts have been proposed: electron-transfer
  predicates ([v6](proposals/metpo_traitmech_v6/)) and 2 causal-mechanism
  classes ([v7](proposals/metpo_traitmech_v7/): salt-in strategy, reductive
  genome evolution).
- Upstream submission [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535)
  now requests real METPO IDs for cohorts **v1–v7 (145 classes + 13 predicates)**,
  with concrete suggested mintable ranges from the 2026-06-12 release
  (classes `1007094–1007238`, predicates `2000735–2000747`). **Blocked on the
  METPO maintainers minting.** When minted, run the documented round-trip (swap
  placeholder `1007xxx`/`2007xxx` for real CURIEs in `data/raw/metpo.owl` +
  groundings, re-seed).
- Still blocked as of 2026-07-30: **no upstream activity since 2026-06-16**, the
  date of the comment that carries the v7 cohort and the suggested ranges. Note
  the issue *title* is stale — it still reads "143 classes + 13 predicates
  (cohorts v1–v6)"; the v1–v7 / 145-class ask lives in that comment, not the
  body. If we ping upstream, the useful lever is the daylight argument already
  made there: METPO's 1-series frontier (`1007093`) is ~300 IDs below TraitMech's
  v1 placeholder block (`1007400`), so sequential minting will eventually collide
  with the placeholders.

## 5. Causal-graph connectivity (#183) — DETECTION DONE; BACKFILL PENDING (corpus-wide)

**The `audit-graphs` gate does not catch graph fragmentation.**
`scripts/audit_causal_graphs.py` flags `DANGLING_EDGE` (an edge naming a node that
does not exist) and `ORPHAN_NODE` (a node no edge references at all). Neither
fires when every node has at least one edge but the graph still splits into
several mutually unreachable components — which is the common case, because a
node picks up an edge to a neighbour long before it is wired back to the trait
node.

Measured over the corpus on 2026-07-30 (353 causal graphs, 4136 nodes):
**220 graphs (62%) have more than one connected component**, and **1264 nodes
(31%) sit outside their graph's largest component**. The worst offenders are the
generated environment/physiology traits — e.g.
`environment/ph_delta_mid2.yaml` (15 nodes, 7 components),
`physiology/methanotrophic.yaml` (20 nodes, 5 components),
`morphology/black_pigmented.yaml` (18 nodes, 6 components) — each with 11–12
nodes unreachable from the main body. This is a content gap (missing edges), not
a schema defect, so nothing currently reports it.

Two pieces of work, independent:

1. ~~**Add a connectivity defect to the audit.**~~ **DONE** — `audit-graphs` now
   emits `UNREACHABLE_FROM_TRAIT` (a node with edges but no undirected path to a
   `TRAIT` node) and `NO_TRAIT_NODE`. The invariant chosen was the stronger
   "every node reachable from the trait node", and reachability is **undirected**
   because curated predicates legitimately mix direction
   (`cellulase -enables-> trait` points inward, `trait -produces-> glucose`
   points outward). It landed non-blocking as required, but as a **ratchet**
   rather than a pure warning: `conf/causal_graph_audit_baseline.tsv` freezes the
   1314 known findings and `--fail-on` defaults to `new`, so pre-existing
   fragmentation never fails while any *newly introduced* island exits 1. Tighten
   with `just audit-graphs --fail-on any` once the backlog below is gone.

2. **Backfill the missing edges** — still **PENDING**, and now the whole of this
   item. This is deep-research work (`research-causal-graphs` /
   `deep-research-trait` skills), not something to mass-generate — every added
   edge needs a reference and a snippet like the existing ones. Work it trait by
   trait; each trait fixed should shrink the baseline, which is regenerated
   deliberately with `just audit-graphs --write-baseline`.

Tracked as **#183**, filed 2026-07-30 when the fragmentation was measured from the
hub. The issue was written before the detector landed, so its "add a connectivity
check" half is already satisfied by item 1 above — including the design question it
posed (one-component versus reachable-from-trait), which was answered in favour of
the stronger reachability invariant. What #183 still tracks is item 2, the backfill.

**Progress: 1 of 220 traits done.** `data/traits/metabolism/cellulolysis.yaml`
was the first instance of (2) and where the problem was found. A deep-research
audit (Edison/PaperQA3 + Codex, independently converging) found that graph split
into 4 components with 9 of 14 nodes unreachable from the trait node. The fix
adds **7 evidence-backed edges** to merge it into one graph (`cellulose →
cellobiose`, `cellobiohydrolase → cellobiose`, endoglucanase / cellobiohydrolase
/ beta_glucosidase `part_of` cellulase, `cellulosome → enables → trait`,
`cellulolytic_genes → encodes → cellulase`), grounds `cellobiose`
(`CHEBI:17057`), and retypes `cellulosome` `CELLULAR_LOCALIZATION` →
`GENE_OR_PROTEIN` (it is a complex, not a location; the `GO:0043263` grounding is
unchanged). A `CONNECT_CAUSAL_GRAPH` entry is appended to `curation_history`.

Its own deferred list, worth keeping: the LPMO / CBM / transport / phosphorolysis
branches, splitting `cellobiohydrolase` by chain end, and replacing the generic
catabolite-repression edge with taxon-specific `cip-cel` evidence. Splitting
`cellobiohydrolase` by chain end is **blocked**: it needs `EC:3.2.1.91` /
`EC:3.2.1.176`, and `EC` is not declared in the LinkML prefix map.

## 6. Web design review (#151) — 2 items PENDING

Front-end review of the TraitMech site against `dataviz` + `artifact-design`.
Nine findings were addressed across #148/#149/#150 (embedding click-through 404 on
all 477 points, dark theme + toggle, `prefers-reduced-motion`, vendored d3, footer
corrections, `<details>` data-table fallback, PaCMAP copy, marker radius). Two
remain open, both on the graph view:
- **`graph.html` advertises an sfdp force-directed *graph* but draws no edges** —
  it is visually identical to the PaCMAP page. Needs the edges emitted into the
  page data and drawn.
- **Redundant double category filter** — a dropdown above the plot and checkboxes
  below, with different semantics. Consolidate to one control.

This is the only open issue in the repo. It is tracked in the cross-Mech design
umbrella in culturebotai-claw.

## Adopt DisMech knowledge-gaps + datasets + QC dashboard (claw#7) — DONE (by 2026-07-22)

Coordinated cross-Mech adoption of DisMech's domain-general features (plan + locked
decisions in culturebotai-claw#7). All three of this repo's slices shipped:
- **Knowledge gaps** — `Discussion` supertype + `DiscussionKindEnum` in
  `src/traitmech/schema/mech_shared.yaml`; `discussions:` slot on `TraitRecord`
  (`traitmech.yaml:243`); `knowledge-gap-scan` recipe in the justfile over the
  Edison harness; **10 trait files already carry `discussions`**.
- **Datasets** — `datasets:` slot (`range: Dataset`) on `TraitRecord`
  (`traitmech.yaml:251`).
- **QC dashboard** — `gen-qc-dashboard` recipe rendering `dashboard/index.html`
  + `coverage.png`.

No further TraitMech work here. Any remaining coordination is cross-Mech in claw#7.
