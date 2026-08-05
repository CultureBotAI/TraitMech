# Next Tasks — TraitMech backlog

Deferred work, each entry with enough context to pick up cold. **Maintenance:**
update this file as work is started/finished — move done items out, add new
deferrals here. Keep the cross-Mech items in sync with the sibling repos'
`NEXT_TASKS.md` (CultureMech / MIM / CommunityMech).

Last reconciled: 2026-08-05. Everything merged in this repo through **#272**.

Since the last reconcile (2026-08-03) the **research-artifact thread closed out
end to end**: the paid Edison sweep landed (#240, #241 — 353 reports, 17 MB, now
tracked), the per-trait research block finally renders (#253), the CURIEs those
reports suggest are resolved against OAK (#260), evidence snippets are audited
(#267), and every GitHub Action is SHA-pinned behind a gate (#272).

Open PRs: **none**.

Open issues, 17. Eight of the fifteen listed at the last reconcile are now closed
(#192, #193, #203, #205, #208, #214, #218, #220); the newly-filed ones nearly all
come from the reviews of the five PRs above, which is the review loop working as
intended.

| # | what | section |
|---|---|---|
| #151 | web design review — 2 residual front-end items | 6 |
| #183 | causal-graph fragmentation — detection done, **backfill is what remains** | 5 |
| #191 | vendored `history.yaml` has no drift check against claw's canonical copy | 7 |
| #197 | `vendored-sync` couples every PR to CultureMech's availability | 2 |
| #198 | **cross-Mech**: `vendored-sync` paths filter omits 4 vendored files | 2 |
| #209 | `vendored-sync.yaml` is a fourth de-facto shared file with no drift protection | 7 |
| #217 | conventions page exists now (#272) but is TraitMech-local; **cross-Mech placement open** | 7 |
| #244 | `trait-graph-sweep --verify` checks report existence only | 8 |
| #245 | `cellulolysis` has a second, codex-provider report with no manifest row | 8 |
| #246 | two `-edison-literature-meta.yaml` files, and nothing in the repo writes them | 8 |
| #248 | absolute `/Users/marcin/...` path in 342 committed reports | 8 |
| #249 | citation sidecars are a broken extraction — 353/353 malformed | 8 |
| #252 | nothing checks that `qc.yaml`'s paths filter covers what `qc` reads — **3rd recurrence** | 7 |
| #266 | grounding audit: merged ontology terms read as "never existed" | 9 |
| #270 | snippet baseline keys on an array index, so improving the corpus can fail `qc` | 10 |
| #275 | conventions page duplicates the workflow header comments it restates | 7 |
| #283 | this file's reconciles touch headers but not the section bodies they label | — |

**Recommended next: #252.** It is the third recurrence of one bug class (#184,
#200, #250), the machinery to gate it is now fresh from #272's `ACTION_UNPINNED`
work, and `docs/WORKFLOW_CONVENTIONS.md` currently has to say "nothing checks
this invariant". #270 is the runner-up — it is ratchet rot in a mechanism landed
three days ago.

**Not actionable as "next":** #183's backfill is per-trait research curation,
not a single PR — it is the largest remaining item and wants its own campaign.
#191/#197/#198/#209/#217 are cross-Mech and want the hub, not this repo.

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

**#198 — the cross-Mech sweep HAS LANDED in the spokes; re-checked 2026-08-03.**
The previous revision of this file called this "still open, fleet-wide" and
described a sweep as pending. It happened. Verified against the sibling repos
rather than from memory:

| repo | issue | state | workflow |
|---|---|---|---|
| MediaIngredientMech | #160 | **closed** (PR #166 merged) | `vendored-sync.yaml`, `# DELIBERATELY NO paths: FILTER` |
| CommunityMech | #280 | **closed** (PR #302 merged) | same, byte-comparable |
| CommunityMech | #278 | **closed** | — |

Both spokes now carry the unfiltered `vendored-sync.yaml` that #196 pioneered
here, and both use `cancel-in-progress: ${{ github.event_name == 'pull_request' }}`
— the #199 fix. So the "every repo has a four-file hole" framing is out of date.

**What may remain is narrower and is a different workflow.** #198's body also
named CultureMech, but CultureMech is the hub: it has no `vendored-sync.yaml` and
no `check_vendored_sync.sh` at all (its workflows are `chebi-consistency`,
`curation-history`, `generate-pages`, `label-correspondence`, `tests`,
`validate-strict`, `weekly-compliance`). Its `label-correspondence.yaml` still
carries `paths: &trigger_paths` with `src/culturemech/schema/**`, so the original
observation — that `chem_formula.py` and the three `tests/test_id_label_*.py` do
not appear in that glob — has not been checked against whether `tests.yaml`
covers them by another route. **That, and only that, is what #198 should still
track.** Left open deliberately with the evidence posted to the issue.

Also open from #196's review: **#197** (running on every PR couples all PRs to
CultureMech's availability). Distinct from the closed CommunityMech#278, which
was about *what* is compared — the checker itself has no canonical copy in the
hub — where #197 is about *when* the comparison runs.

## 3. Trait promotion PROPOSED -> REVIEWED — DONE

All categories are promoted: the corpus is **427 REVIEWED + 50 DEPRECATED,
0 PROPOSED**. The 50 DEPRECATED are observation-value carriers, deliberately
out of scope (see `docs/DEPRECATED_REPLACEMENT_PROPOSAL.md`). No promotion work
remains.

## 4. METPO upstream round-trip (BLOCKED on upstream) + residual floor

- **Corrected 2026-08-02 — the old "predicates 85% (1094/1284) / nodes 62%
  (1024/1643)" figures do not reproduce under any metric and should not be
  quoted.** The repo's own scripts are ground truth; re-run them for the current
  number rather than trusting this file:

  ```
  uv run python scripts/ground_causal_predicates.py   # dry-run; writes reports/predicate_grounding_residual.tsv
  uv run python scripts/ground_causal_nodes.py        # dry-run; writes reports/node_grounding_residual.tsv
  ```

  As of 2026-08-02, over 477 YAMLs: **predicates 2128/3402 edges grounded (63%)**,
  residual 1274 edges across 572 distinct labels; **nodes 1461/4136 grounded
  (35%)**, residual 2675 across 2318 distinct (label, type) keys.

  These reproduce from the committed reports as of this revision. They did not
  before: `reports/node_grounding_residual.tsv` was stale by exactly one row —
  2319 keys summing to 2676 — because it still listed `cellobiose`, grounded to
  `CHEBI:17057` back in #185. The fresh figures are the ones that close
  (1461 + 2675 = 4136 nodes; 1461 + 2676 does not).

  **#214 is fixed**: `just audit-derived-reports` regenerates both TSVs into a
  temp dir and fails if either differs from the tracked copy, and it runs as part
  of `just qc`. So the reports can no longer drift silently, and reading the
  numbers no longer dirties a tracked file.
- **The "this is the quality floor" claim was also too generous.** Much of the
  residual genuinely is non-ontological graph narrative (adaptation states,
  composite descriptors) that should stay free-text — but not all of it. The
  frequency-ranked residual has **exact-label RO matches that were simply never
  added to `mappings/predicate_grounding.tsv`**, while their *paraphrases* were:
  `promotes` → RO:0002213 is mapped, but the literal label `positively regulates`
  (37 edges) is not; `inhibits` → RO:0002212 is mapped, but `negatively
  regulates` (16 edges) is not; `causally upstream of` (13 edges) is the literal
  RO:0002411 label. So the top of the residual is cheap, high-confidence,
  CI-verifiable work, and only the tail is the floor. See section 9.
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

## 5. Causal-graph connectivity (#183) — DETECTION MOSTLY DONE (#220); BACKFILL PENDING (corpus-wide)

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

**Progress, re-measured 2026-08-03.** Two numbers circulate here and they are
*not* the same measurement — quote whichever you mean, and say which:

| measure | value | source |
|---|--:|---|
| graphs with >1 connected component (undirected) | **220** files | recompute from `causal_graphs` |
| files with ≥1 `UNREACHABLE_FROM_TRAIT` finding | **219** files | `conf/causal_graph_audit_baseline.tsv` |
| `UNREACHABLE_FROM_TRAIT` findings (the ratchet's unit) | **1314** | same file |
| nodes outside their graph's largest component | **1264** (31% of 4136) | recompute |

Corpus totals are unchanged: 353 graphs, 4136 nodes. Per-category fragmented
files: environment 85, **morphology 47**, metabolism 31, physiology 27,
ecology 18, genomics 11, upper 1 — the baseline has morphology **46**, and that
one-file gap is real, not arithmetic: see **#220**. `morphology/dumbbell_shaped.yaml`
splits into two components that *each* contain a node typed `TRAIT`, so every node
reaches *a* trait node and the audit reports it clean while 7 of its 11 nodes have
no path to the trait the record is about.

`cellulolysis.yaml` now verifies as a **single component**, so the #185 fix did
land — the "1 of 220 done" framing in an earlier revision of this file was wrong
arithmetic, not lost work: 220 is what is *still* fragmented, not the count before
the fix.

`data/traits/metabolism/cellulolysis.yaml`
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

It is tracked in the cross-Mech design umbrella in culturebotai-claw. (The
previous revision of this file called #151 "the only open issue in the repo" —
that has not been true since 2026-07-30; see the header table.)

## 7. CI + agent-workflow thread — SHIPPED; residuals in #191/#197/#198/#209/#217/#252/#275

This whole thread post-dates the last reconcile and was previously unlogged here.
TraitMech is the fleet **pilot** for agent workflows because it is the smallest
surface. What landed, 2026-08-02/03:

- **#194 `pr-shepherd`** — the fleet's first agent workflow, deliberately
  **comment-only**. Two things fail *silently* until a writer/reviewer App split
  exists: pushes made with the built-in `GITHUB_TOKEN` do not trigger workflows
  (so an agent-pushed fix shows green because nothing evaluated it), and a single
  identity can approve its own work. Merging/pushing/editing/approving are
  refused in the prompt *and* withheld at the harness level via `--allowedTools`.
  No `schedule:` trigger, deliberately.
- **#206** — `dry_run` (the default) was enforced only by a prompt instruction
  while `Bash(gh pr comment:*)` was granted unconditionally. Now the tool is
  withheld in dry runs: capability, not persuasion, in an agent that reads
  untrusted PR diffs by design.
- **#201 `pr-sanity`** — before it, a PR touching only `docs/**`, `README.md`,
  `NEXT_TASKS.md`, or a *new workflow file* matched no `paths:` filter and ran
  **nothing**; `gh pr checks` prints `no checks`, which reads as "nothing to
  verify" but means "nothing was verified". #194 was a live instance. Runs
  unfiltered on every PR.
- **#207** — `pr-sanity`'s link check scanned line-by-line with no notion of
  fenced code, so a link written as an *example* inside a fence counted as a real
  link. Zero findings in the corpus today; the bug would have bitten the first
  person to document a link pattern.
- **#210** — adopted DisMech's Claude code-review workflow. **First workflow to
  use the `culturebot-reviewer` App**, which holds `contents: read` +
  `pull_requests: write` and so physically cannot change what it reviews. The
  token step has **no `continue-on-error`** on purpose: DisMech's fallback to
  `github.token` would silently restore the self-approval hole the split exists
  to close, and would look identical in the logs.

**#215 was the exception to "none of this blocks anything" — FIXED and merged in
#216 (2026-08-03).** `claude-code-review.yml` posts a progress
comment as it works; that comment fired `issue_comment: created`, which landed in
the *same* workflow-level concurrency group (`claude-review-<PR>` — the `||`
chain falls through to `github.event.issue.number` for the same PR) and, with
`cancel-in-progress: true`, cancelled the run that had just posted it. The comment
run then skipped itself on the job's `if:`, having done nothing. Every review,
every PR, since #210 merged.

It was green on `feat/claude-code-review` only because `issue_comment` workflows
run from the *default branch's* copy of the file, and `main` had no
`claude-code-review.yml` until #210 landed — a merge-activated regression no
pre-merge CI could have seen.

**The fix is not the obvious one.** Moving `concurrency:` onto the job — the
first thing to try, on the theory that a job skipped by `if:` never joins the
group — is *probably* right but rests on behaviour GitHub does not document:
the workflow-syntax reference describes `jobs.<job_id>.concurrency` without ever
saying how it interacts with a false `if:`. What #216 ships instead makes the
invariant structural, holding under any evaluation order:

```yaml
group: claude-review-${{ …pr number… }}-${{ github.event_name == 'pull_request' && 'push' || github.run_id }}
```

Only `pull_request` runs share a key, so rapid pushes to one PR still collapse.
Every comment and dispatch run gets `github.run_id`, unique per run, so it can
neither cancel nor be cancelled. (The block did also move onto the job, but that
is placement, not protection.) Keying merely by `github.event_name` is *not*
sufficient: it fixes the push path while leaving `/review` runs sharing one key
with every other comment on the PR, including ones the agent posts itself via the
allowlisted `gh pr comment`.

**This is a narrowing, not a restoration** — the original key spanned all three
triggers, so it also let a `/review` supersede a review already in flight, and
that is given up deliberately. Two reviews at once is a far cheaper failure than
the one it replaced: no review at all.

Verified, not just argued: before, both `pull_request` runs on #213 were cancelled
seconds after a `culturebot-reviewer` comment; after, both pushes to #216 gave
`pull_request → success` with the `issue_comment` runs skipping harmlessly
alongside. **Still unproven at the time of writing:** every one of those checks
ran on a branch carrying its own copy of the fix. `issue_comment` runs use
`main`'s copy, so the first genuine post-merge test is this PR.

`pr-shepherd.yml` was checked and is unaffected — `workflow_dispatch` only,
`cancel-in-progress: false`, no comment trigger. `claude-code-review.yml` is the
only workflow in the repo with an `issue_comment` trigger.

Third concurrency-scoping bug here after #199 and #196's review, which produced
two follow-ups rather than none: **#217** for the workflow-authoring conventions
page that has nowhere to live (`docs/` has no such page, and this is fleet
knowledge that belongs upstream rather than copied four times), and **#218** to
*enforce* the rule instead of only documenting it. #218 is the stronger of the
two — a docs page does not fail CI, and #215 got in past a reviewer who had
already fixed this class of bug twice. `pr_sanity.check_workflows` already parses
every workflow's triggers, so the guard drops in beside the existing
`NO_UNFILTERED_CI` check: a workflow with both `pull_request` and an
independently-firing trigger must key its concurrency group by `github.run_id`
or `github.event_name`.

**The other pending items are small, independent and fully specified**, each
verifiable by CI, none blocking anything:

| # | fix | note |
|---|---|---|
| #191 | vendored `history.yaml` has no drift check vs claw canonical | cross-Mech; wants the hub |
| #197 | `vendored-sync` couples every PR to CultureMech's availability | cross-Mech; wants the hub |
| #198 | `vendored-sync` paths filter omits 4 vendored files, in every repo | cross-Mech; wants the hub |
| #209 | `vendored-sync.yaml` is triplicated across spokes, unguarded | hub has no copy to diff against — same hole as CommunityMech#278 |
| #217 | conventions page is TraitMech-local; cross-Mech placement unsettled | the page landed in #272; #209 is the argument against a fourth copy |
| #252 | nothing checks `qc.yaml`'s paths filter covers what `qc` reads | **3rd recurrence** (#184, #200, #250); gate machinery fresh from #272 |
| #275 | conventions page duplicates the workflow header comments it restates | resolve with #217 — consolidate or cross-link, not both |

Closed since this section was written: **#192**, **#193**, **#203**, **#205**,
**#208**, **#218** (and #199, #200, #202, #204, #215 before them). Action pinning
and the conventions page landed in **#272**, which also added the
`ACTION_UNPINNED` gate.

## 8. The paid Edison sweep's output was lost — RE-RUN COMPLETE (#241), 353/353 tracked

`reports/trait_graph_audit_manifest.tsv` recorded a 2026-07-20 sweep that
**fully succeeded**: 353 distinct traits, every one `ok`.
The 8 `fail:1` rows are not 8 unfinished traits — each is a `(category, slug)`
that also appears as `ok`, i.e. a retry that then worked. Verified by set
difference: `fail − ok` is empty, so there are **zero outstanding failures**.
That makes the loss below worse, not better: nothing here is a partial run that
was going to need redoing anyway.

**RESOLVED as of 2026-08-04 — `research/` is now tracked (#240).** It had been
ignored as "large, regenerable", and the second half of that was the expensive
half: 342 of 353 reports existed only on one machine, so the manifest recorded
353 successes against 11 surviving files. The artifacts are provenance, not
build output, and are committed.

The re-run **completed** (#241): 353/353 reports plus citation sidecars, 17 MB,
tracked. It was launched through the `just trait-graph-sweep` recipe, which
exists for the credentials rather than convenience — `scripts/research_trait.py`
has no `load_dotenv`, so a sweep started outside `just` sees no `EDISON_API_KEY`
and every call fails instantly.

Canaried before fan-out and checked on side effects rather than the exit code:
one real unit produced a 50,846-byte report plus citations, `cached: false`, 57
references, and a manifest row.

**The manifest reads as a spend record.** 714 rows: 700 `ok` + 13 `fail:1`,
across five `run_id`s. All 13 failures later succeeded under a later `run_id` —
which is the distinction that column was added to make, after
`biofilm_formation` carried three indistinguishable rows.

The transitional inconsistency is gone. `--verify` is now clean and runs in
`just qc` as `audit-research-artifacts`:

```
$ just trait-graph-sweep --verify
targets: 353  already-researched: 353  pending: 0
manifest ok rows with a missing artifact: 0
reports carrying a malformed CURIE: 0 (0 matches; scanned 707 artifacts)
```

The malformed-CURIE line is a scan added in #242, not an assertion — four
reports had been regenerated for double-prefixed CURIEs, and a fifth was in
flight during the manual grep that found them, so it was missed and needed a
third paid pass.

### What the sweep left behind — all filed, none blocking

- **#244** — `--verify` checks report *existence* only: not the citation
  sidecars, not non-emptiness, and never disk→manifest. So the clean output
  above is narrower than it looks, and a report on disk with no `ok` row would
  silently suppress a call, since resume is file-existence keyed.
- **#245** — `cellulolysis` has a second, `-codex` report with no manifest row
  and no sidecar. #253's provider ranking stops it reaching a page.
- **#246** — two `-edison-literature-meta.yaml` files, for 2 of 353 traits, and
  nothing in the repo writes that filename.
- **#248** — `template_file: /Users/marcin/...` in 342 now-tracked reports.
- **#249** — the citation sidecars are a broken extraction: 353/353 carry
  malformed entries, 332/353 list the same reference more than once.

Cost per call is captured nowhere — `duration_seconds` is, but no USD figure —
which is worth adding before this is ever repeated.

## 9. Predicate/node grounding backfill — PENDING, and cheaper than section 4 implied

Follows from the section 4 correction. The frequency-ranked residual in
`reports/predicate_grounding_residual.tsv` opens with labels that are *exact* RO
labels whose paraphrases are already mapped in
`mappings/predicate_grounding.tsv`:

| residual label | edges | is the exact OAK label of | already mapped as |
|---|--:|---|---|
| `positively regulates` | 37 | RO:0002213 | `promotes` → RO:0002213 |
| `negatively regulates` | 16 | RO:0002212 | `inhibits`/`suppresses`/`prevents` → RO:0002212 |
| ~~`causally upstream of`~~ | ~~13~~ | ~~RO:0002411~~ | **WRONG — see below** |

The first two shipped in #235 (53 edges). The third **did not, and is the more
important entry**: `causally upstream of` is the exact OAK label of RO:0002411
and was still wrong. RO defines the relation over occurrents, while all 13
corpus edges connect material entities (6 `CHEMICAL→CHEMICAL`,
6 `GENE_OR_PROTEIN→CHEMICAL`, 1 `GENE_OR_PROTEIN→CAPACITY`). An exact label
match is **not** sufficient to ground a predicate.

Below those sit judgement calls (`supports` 37, `induces` 34, `required for` 30,
`drives` 29, `maintains` 29, `mediates` 27) and then the genuine free-text floor.
Node side, the head of the residual is similar: `proton motive force` ×16,
`compatible solute accumulation` ×12, `Na+/H+ antiporter` ×8, `ATP` ×6.

**Do not treat `label-correspondence` as making this loop safe.** It compares an
`(id, label)` pair against the ontology and nothing else — it has no view of the
edge a CURIE lands on, and `predicate_id` is an unbound string in the schema, so
nothing in `just qc` checks domain or range. That is exactly how the RO:0002411
mapping passed every gate while being wrong.

What does check it is the `subject_types`/`object_types` columns on
`mappings/predicate_grounding.tsv`, enforced by `ground_causal_predicates.py`
(#236): an edge outside a row's declared node types is refused, stays in the
residual, and is reported as `blocked_by_node_type` in the residual TSV. Rows
left at `*`/`*` are unconstrained, so a new mapping is only as safe as the
constraint written beside it. Apply with
`scripts/ground_causal_predicates.py --apply` / `ground_causal_nodes.py --apply`.
**The queue is now trustworthy (#214, fixed).** The residual TSVs used to lag the
corpus with nothing to catch it — `cellobiose` still appeared as ungrounded weeks
after #185 grounded it. `just audit-derived-reports` now regenerates both and
fails if the tracked copies differ, and it runs inside `just qc`, so the ranking
can be taken at face value rather than regenerated defensively first.
Where no ontology term fits, the actionable form is `metpo-proposal`, not a
force-match — the section 4 floor still stands for the tail.

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

## 10. Evidence snippets (#247) — AUDIT LANDED, BACKLOG FROZEN

`just audit-snippets` (#267) ratchets against `conf/evidence_snippet_baseline.tsv`.
Frozen backlog, 2,737 findings: **2,586 MISSING_SNIPPET** (63% of evidence items
assert a mechanism on a bare DOI), 71 UNSUPPORTIVE, 60 ELLIPTICAL (ERROR), 13
REUSED, 7 ECHOES_RESEARCH_REPORT.

The policy settled in #247: a research report is **not** a snippet source. Its
evidence text goes in `notes:`; `snippet:` requires opening the paper. Written up
in `docs/CURATION_PLAYBOOK.md`.

Burning this down is the same work as #183's backfill, on the same edges —
`cellulolysis` is in the ECHOES set and is #183's worked example, so it is the
natural first target. Residual: **#270** (baseline keys on an array index).
