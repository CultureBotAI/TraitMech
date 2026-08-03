# Next Tasks — TraitMech backlog

Deferred work, each entry with enough context to pick up cold. **Maintenance:**
update this file as work is started/finished — move done items out, add new
deferrals here. Keep the cross-Mech items in sync with the sibling repos'
`NEXT_TASKS.md` (CultureMech / MIM / CommunityMech).

Last reconciled: 2026-08-03. Everything merged in this repo through **#216**
(2026-08-03) — which now includes the whole CI/agent-workflow thread (#194, #196,
#201, #206, #207, #210, #216, section 7) that was absent from this file — plus the
claw-side architecture decisions through 2026-07-25.

Open PRs: **this one** (#213). #216 merged, so `claude-review` works again and
this PR is the first one it reviews post-merge — which is the real test of that
fix, since every check before it ran on a branch carrying its own copy.

Open issues, 14 of them — the last four filed by this reconcile and by #216's
own review:

| # | what | section |
|---|---|---|
| #151 | web design review — 2 residual front-end items | 6 |
| #183 | causal-graph fragmentation — detection landed, **backfill is what remains** | 5 |
| #191 | vendored `history.yaml` has no drift check against claw's canonical copy | 7 |
| #192 | justfile: the claw-module guard is implemented twice | 7 |
| #193 | QC dashboard embeds a generation timestamp, so staleness can't be rechecked | 7 |
| #197 | `vendored-sync` couples every PR to CultureMech's availability | 2 |
| #198 | **cross-Mech**: paths filter omits `chem_formula.py` + the 3 id_label tests in *every* repo | 2 |
| #203 | three major versions of `astral-sh/setup-uv` across workflows (v3/v5/v7) | 7 |
| #205 | `pr-shepherd` model resolution imports an undeclared PyYAML from system python | 7 |
| #208 | `pr-sanity` still scans 4-space-indented code blocks for links | 7 |
| #209 | `vendored-sync.yaml` is a fourth de-facto shared file with no drift protection | 7 |
| #214 | grounding residual reports drift from the corpus, nothing regenerates or checks them — **blocks the section 9 loop** | 9 |
| #217 | no workflow-authoring conventions page, so concurrency lessons keep being relearned | 7 |
| #218 | `pr-sanity` should *enforce* the concurrency rule #217 only documents | 7 |

Closed since the last reconcile: **#184** (by #196), **#199**, **#200** (by #201),
**#202** (by #207), **#204** (by #206), **#215** (by #216).

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

**Progress, re-measured 2026-08-02: 220 fragmented graphs remain, across 220 of
the 477 trait files.** Corpus totals are unchanged (353 graphs, 4136 nodes,
1264 nodes = 31% outside their graph's largest component), and
`conf/causal_graph_audit_baseline.tsv` still freezes **1314** findings. Note
that `cellulolysis.yaml` now verifies as a **single component**, so the fix did
land — the "1 of 220 done" framing in the previous revision of this file was
wrong arithmetic, not lost work: 220 is the count of what is *still* fragmented,
not the count before the fix. By category: environment 85, morphology 47,
metabolism 31, physiology 27, ecology 18, genomics 11, upper 1.

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

## 7. CI + agent-workflow thread — SHIPPED; 7 small review issues PENDING

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
| #203 | unify `astral-sh/setup-uv` (v3 ×4, v5, v7) | needs a version decision, then mechanical |
| #205 | declare PyYAML for `pr-shepherd`'s model-resolution step | same shape as #190's `matplotlib` gap |
| #208 | skip 4-space-indented code blocks in the link check | no impact today; narrower than #202 was |
| #209 | `vendored-sync.yaml` is triplicated across spokes, unguarded | hub has no copy to diff against — same hole as CommunityMech#278 |
| #191 | vendored `history.yaml` has no drift check vs claw canonical | |
| #192 | justfile claw-module guard implemented twice | |
| #193 | QC dashboard embeds a timestamp, defeating regenerate-to-check-staleness | |
| #217 | write down the workflow-authoring conventions | needs a home first — fleet knowledge, probably CultureMech or claw, not a fourth copy here |
| #218 | enforce the concurrency rule in `pr-sanity` | the stronger half of #217; `check_workflows` already parses triggers |

## 8. ⚠️ The paid Edison research sweep completed, but its output is GONE

`reports/trait_graph_audit_manifest.tsv` (362 rows, last written 2026-07-20)
records a **completed** sweep: **353 ok, 8 fail**. But `research/` is in
`.gitignore` (line 42, "large, regenerable"), nothing under it is tracked, and
only **11 traits' reports survive on this checkout**:

```
$ find research/traits -name '*-deep-research-falcon.md' | wc -l
11
$ uv run python scripts/run_trait_graph_audit.py --dry-run | tail -1
[342/342] upper/quality  (quality)
```

Resume detection in `scripts/run_trait_graph_audit.py` is **file-existence
based**, so from this checkout the sweep looks 3% done and would re-run — and
re-bill — 342 Edison calls that already succeeded once.

**Decide before running anything paid.** Either the reports exist on another
machine and should be recovered, or `.gitignore`'s "regenerable" premise needs
revisiting for outputs that cost money to regenerate (commit them, or push them
to shared storage with the manifest as the index). Until then, treat the
manifest's 353 `ok` rows as a record of spend, not as available input, and honour
the canary rule: one real trait end-to-end before any fan-out.

## 9. Predicate/node grounding backfill — PENDING, and cheaper than section 4 implied

Follows from the section 4 correction. The frequency-ranked residual in
`reports/predicate_grounding_residual.tsv` opens with labels that are *exact* RO
labels whose paraphrases are already mapped in
`mappings/predicate_grounding.tsv`:

| residual label | edges | is the exact OAK label of | already mapped as |
|---|--:|---|---|
| `positively regulates` | 37 | RO:0002213 | `promotes` → RO:0002213 |
| `negatively regulates` | 16 | RO:0002212 | `inhibits`/`suppresses`/`prevents` → RO:0002212 |
| `causally upstream of` | 13 | RO:0002411 | — |

All three were checked against OAK on 2026-08-02 (`get_adapter("sqlite:obo:ro")`,
`.label()`) and match exactly — this is not an eyeball guess. The paraphrase got
mapped and the canonical label did not, which is why they are still residual.

Below those sit judgement calls (`supports` 37, `induces` 34, `required for` 30,
`drives` 29, `maintains` 29, `mediates` 27) and then the genuine free-text floor.
Node side, the head of the residual is similar: `proton motive force` ×16,
`compatible solute accumulation` ×12, `Na+/H+ antiporter` ×8, `ATP` ×6.

Each mapping row is verified by the existing **blocking** `label-correspondence`
gate (`just validate-products`), which checks the CURIE's label against OAK — so
a wrong CURIE fails CI rather than landing silently. Apply with
`scripts/ground_causal_predicates.py --apply` / `ground_causal_nodes.py --apply`.
**Caveat (#214):** the residual TSVs are tracked but nothing regenerates them, so
they lag the corpus — `cellobiose` still appeared as ungrounded weeks after #185
grounded it. Regenerate before trusting the ranking as a work queue.
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
