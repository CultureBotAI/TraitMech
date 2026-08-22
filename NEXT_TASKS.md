# Next Tasks — TraitMech backlog

Deferred work, each entry with enough context to pick up cold. **Maintenance:**
update this file as work is started/finished — move done items out, add new
deferrals here. Keep the cross-Mech items in sync with the sibling repos'
`NEXT_TASKS.md` (CultureMech / MIM / CommunityMech).

Last reconciled: 2026-08-22 (hygiene bookkeeping on the 2026-08-21 full
reconcile). Everything merged in this repo through **#503**.
This reconcile supersedes PR #493, which described main at #487 and was outrun
by a burst of parallel sessions before it could merge — nine PRs (#492,
#494–#499, plus the Dependabot pair #441/#442) landed in under a day, and
#501/#502 followed while this replacement was in review. What the burst did:

- **#494** landed the README refresh that #493 flagged as sitting uncommitted
  on `main` (stale 354-era counts → 477, directory layout, plus
  `tests/test_readme_artifacts.py`).
- **#495** salvaged the six non-overlapping canonical-example records from the
  superseded PR #465, re-validated under the #474 standard; #465 and #461 are
  both **closed** now.
- **#496** settled the #480/#443 decision by **retiring the completeness-audit
  ranking**: `prioritize_graph_research.py`, its tests, skill and recipes are
  deleted; `graph_completeness_audit.tsv` + `graph_enrichment_backlog.md` are
  kept as historical paid-research snapshots; the live-state
  `scripts/trait_priority.py` queue owns prioritization, extended with
  research-artifact awareness. **#480 and #443 are closed.** Consequence:
  #471/#472/#479 were defects in the deleted script — closed 2026-08-22
  after verifying no successor surface.
- **#497** ran #356 tranche 5 (process-quality families): **112 → 83
  occurrences across 30 families.**
- **#498/#499** began the apply-campaign (#426): peritrichous and the
  predatory-bacterium lifecycle graphs — fragmentation 218 → 216 graphs,
  unreachable nodes 1296 → 1283.
- **#501** closed **#433 and #500** in one governed pass: Edison enrichment
  now invalidates a whole stale same-stem sidecar set, the capture/enrichment
  provenance behaviour got its ten regressions, and `_edison_capture.py` and
  friends came under the shared provider contract (with CultureMech#330).
- **#502** (merged 2026-08-21) fixed **#391**: `fermentation` was grounded
  METPO:1000845 (Acetogenesis, via its "Acetate fermentation" synonym) in
  `chemoorganoheterotrophic.yaml`; regrounded to GO:0006113 per the existing
  mapping row. Its adversarial review filed and fixed **#504** (the provenance
  text undercounted the GO:0006113 attestation: eight records, not six).

The history below (through the #487 wave) is retained from the superseded
reconcile:

Since the 2026-08-15 reconcile, five threads ran — this was the busiest stretch
in the file's history (~25 PRs), and four of the five threads were **new**,
i.e. unlogged here until now:

- **#356 burn-down, tranches 2–4** (the one pre-existing thread): #387 split
  protein from activity where one `node_id` meant both — the exact
  `GENE_OR_PROTEIN`/`MOLECULAR_FUNCTION` tranche the last reconcile recommended;
  #392 stated the `PATHWAY` vs `BIOLOGICAL_PROCESS` rule and applied it; #403
  gave oxygen one `node_id` per sense (the `CHEMICAL`/`ENVIRONMENTAL_FACTOR`
  two-ids case). **223 → 112 occurrences** in the baseline. See section 11 for
  what remains.
- **Research prioritization + provider triage** (new; section 12): #427 picks
  the research target *before* paying; #440 triaged providers ("available" no
  longer means "will work"); #449 ported DisMech's priority dashboard with the
  lumping rule inverted; #470 made the prioritiser rank every bin and refuse a
  stale completeness report. Headline verdict (#426): **no trait awaits a first
  deep-research pass — 351 need already-paid-for research APPLIED.**
- **canonical_examples** (new; section 13): #446 rendered + validated the slot
  and ran a one-record canary; #474 applied batch 1 (5 records filled, 6 honest
  skips, two adversarial review rounds → #476–#478). ~130-record gap remains
  (#444).
- **microbedecoder / FAPROTAX grounding** (new; section 14): #454 grounded 42
  enzyme-activity labels to GO/EC, #459/#462 resolved more, #473 applied the
  grounding backlog and gated it against rebuilding, #467 shipped METPO
  proposal v11 (15 FAPROTAX metabolic-strategy classes). #453/#464 remain.
- **Repository review follow-ups** (new): #487 implemented and closed
  #482–#486 (main-safe workflow concurrency, root CLAUDE.md consolidation,
  hermetic in-process history validation, Python 3.10–3.13 test matrix).
  The README-refresh continuation landed as **#494**.

Also closed since 2026-08-15: **#244** (via #396 — `--verify` now checks
emptiness and walks disk→manifest), **#249** (via #388 — citation sidecars no
longer requested, the 353 broken ones deleted), **#289** (via #406), **#292**
(via #408), **#402** (via #405), **#443/#480** (via #496), plus the review
findings on the PRs above.

Open PRs: **one** — **#493**, the superseded reconcile this file replaces;
close it unmerged. #492, the Dependabot pair, #501 and #502 merged; #461/#465
were closed with #465's salvageable records landed via #495.

Open issues, **30** (re-derived 2026-08-22, after the hygiene closes landed).
Closed since the #493 snapshot: #443, #480 (#496), #391 (#502), #433 and #500
(#501 — #500 was the five-Mech fleet sweep's sidecar-reattribution defect,
filed and fixed within a day), #504/#505 (review findings on #502/#503, fixed
pre-merge), and the six hygiene closes — #471/#472/#479 (verified moot:
nothing on main reads the completeness TSV, and `trait_priority.py` already
initialises `series_size: 0` uniformly), #476/#477 (verified fixed in #474
pre-merge), #448 (verified shipped: `app/dashboard/priority.*` + recipes).
#444/#445 were retitled to their residue rather than closed.

The pre-2026-08-15 residue is unchanged (first block); the rest were filed by
the threads above (second block).

| # | what | section |
|---|---|---|
| #151 | web design review — 2 residual front-end items | 6 |
| #183 | causal-graph fragmentation — detection done, **backfill is what remains** | 5 |
| #191 | vendored `history.yaml` has no drift check against claw's canonical copy | 7 |
| #197 | `vendored-sync` couples every PR to CultureMech's availability | 2 |
| #209 | `vendored-sync.yaml` is a de-facto shared file with no drift protection | 7 |
| #245 | `cellulolysis` has a second, codex-provider report with no manifest row | 8 |
| #246 | two `-edison-literature-meta.yaml` files, and nothing in the repo writes them | 8 |
| #266 | grounding audit: merged ontology terms read as "never existed" | 9 |
| #356 | one `node_id`, several `node_type`s — **83 of 294 remain** | 11 |
| #358 | vendored `history.yaml` states the pre-#325 enforcement policy | 7 |
| #364 | METPO has no generic salt-tolerance / low-pH-tolerance disposition | 11 |
| #377 | claw-is-private residue — the `check_vendored_sync.sh` half is cross-repo | 7 |

| # | what (filed since 2026-08-15) | section |
|---|---|---|
| #389 | `_edison_capture.py` documented as vendored byte-identical; differs everywhere — re-scope against #501's shared contract | 7 |
| #409 | Discussions/Knowledge Gaps rendered (#410) but only 2% populated | 12 |
| #423 | `just new-history` writes bare-number links, violating `range: uri` | 7 |
| #425 | `curate_knowledge_gaps.py` has no `--dry-run`/`--apply`, no justfile target | 12 |
| #426 | **~349 traits need paid-for research APPLIED** — campaign begun (#498/#499) | 12 |
| #435–#439 | provider-triage review findings (false "available", untested scoring, CLI tracebacks) — re-check against #501, which touched provider policy | 12 |
| #444 | canonical_examples backfill: 237 of ~353 records carry examples; render half shipped (#446) | 13 |
| #445 | `audit-canonical-examples` exists (#446) but is **not wired into `qc`/CI** | 13 |
| #453 | 40 microbedecoder enzyme-activity traits (47k occurrences) have no TraitMech term | 14 |
| #464 | 56 strings owned by >1 trait record — synonym lookup cannot disambiguate | 14 |
| #481 | irreproducible overlap figures — **now live in `trait_priority.py:23-24`**, the maintained tool | 12 |
| #475 | morphometric bins need a taxon-oriented source (mechanism artifacts answer *how*, not *who*) | 13 |
| #478 | bin-measured exemplars land on family parents — policy call | 13 |
| #491 | `.vendored_canon_ref` pinned before `history.yaml` existed in the hub — unblocked by #492's merge | 7 |

**Recommended next: the #435 cluster (#436–#439)** — one file, a handful of
small fixes, and the tool's headline recommendation can still route spend to
a provider that 402s. Check each against #501 first: it preserved the
configured/available distinction and touched provider policy, so parts may
already be narrowed. Then **#481** — correct the irreproducible figures in
the maintained `trait_priority.py`. (#500/#433, the previous recommendation,
were closed by #501 the same day they were recommended.)

**Ongoing campaigns, feed continuously:** the #426/#183 apply-campaign
(~349 remain; `trait_priority.py` is the sanctioned picker) and #356
(83 occurrences, 30 families; the decided families are thinning, the tail is
judgement calls).

**Hygiene DONE (2026-08-22):** #471/#472/#479, #476/#477 and #448 closed —
each claim verified against main before closing, with the evidence in the
closing comment. #444/#445 retitled to their residue. PR #493 closed unmerged.

**Not actionable as "next":** #364 and the v1–v11 cohorts are upstream METPO
(metpo#535, still no upstream activity). #191/#197/#209/#358 step 2/#377's
script half/#389 all want the hub or claw first — cross-repo, not
TraitMech-local. #491 is local and small now that #492 merged.

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
`.vendored_canon_ref` in each spoke.

**Correction (2026-08-15, #377): claw is PUBLIC**, and has been for some time —
`gh repo view CultureBotAI/culturebotai-claw --json visibility` returns `PUBLIC`.
This paragraph used to say "Claw remains private, and that is fine". The
conclusion still holds, but not for the reason given: the repoint stays
abandoned because claw is a **mirror, not the fleet enforcer** (claw#22 reverted
claw#21), which was never a visibility argument. What visibility *does* change
is that "the canonical hub for this file is private" is no longer a valid
blocker — which is the entire blocker on **#191** and **#358 step 2**.

**And a fifth de-facto shared file, found checking the above (#377, extends
#209).** `scripts/check_vendored_sync.sh` is byte-identical across TraitMech,
MediaIngredientMech and CommunityMech, does **not** exist in CultureMech, and is
**not in its own `FILES` list** — so nothing detects drift in it. The drift
checker is the one shared file with no drift protection. Editing its comments in
one repo silently diverges the other two, which is why #377's script half is
cross-repo work and only its `NEXT_TASKS.md` half landed here.

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

## 5. Causal-graph connectivity (#183) — DETECTION DONE; MEASUREMENT DONE (#363); BACKFILL 218 remain

**The gap this section opened with, for the record: `audit-graphs` used to miss
fragmentation entirely.** It flagged `DANGLING_EDGE` (an edge naming a node that
does not exist) and `ORPHAN_NODE` (a node no edge references at all), and
neither fires when every node has at least one edge but the graph still splits
into mutually unreachable components — the common case, because a node picks up
an edge to a neighbour long before it is wired back to the trait node. #185 and
#227 closed that; the detection half is done.

Measured over the corpus on 2026-07-30 (353 causal graphs, 4136 nodes), after
`cellulolysis` had already been repaired: **220 graphs (62%) have more than one
connected component**, and **1264 nodes
(31%) sit outside their graph's largest component**.

**Re-measured 2026-08-21** (after #498/#499, the first two apply-campaign
repairs): **216 graphs** split, **1283** `UNREACHABLE_FROM_TRAIT` — the
campaign has finally started moving this number; it had been frozen at 218
since 2026-08-08.

**Re-measured 2026-08-08** (after #294, #300, #351, #360): **218 graphs** still
split, **1296** `UNREACHABLE_FROM_TRAIT`. The headline number barely moved in
five weeks, and #359/#363 explain why it *cannot* be read as progress — see
section 11. The metric to use from now on is
`reports/causal_graph_connectivity.tsv`: **353 graphs, 861 components over 4129
wired nodes, 69.7% of wired nodes in their graph's largest component.** That is
the number a backfill has to move. The worst offenders are the
generated environment/physiology traits — e.g.
`environment/ph_delta_mid2.yaml` (15 nodes, 7 components),
`physiology/methanotrophic.yaml` (20 nodes, 5 components),
`morphology/black_pigmented.yaml` (18 nodes, 6 components) — each with 11–12
nodes unreachable from the main body. This is a content gap (missing edges), not
a schema defect — which is why the original audit was blind to it, and why
closing it needed a new defect class rather than a schema fix.

Two pieces of work, independent:

1. ~~**Add a connectivity defect to the audit.**~~ **DONE** — `audit-graphs` now
   emits `UNREACHABLE_FROM_TRAIT` (a node with edges but no undirected path to a
   `TRAIT` node), `FRAGMENTED_GRAPH` (#227 — a graph in several components at
   all, whatever each component contains) and `NO_TRAIT_NODE`. The invariant chosen was the stronger
   "every node reachable from the trait node", and reachability is **undirected**
   because curated predicates legitimately mix direction
   (`cellulase -enables-> trait` points inward, `trait -produces-> glucose`
   points outward). It landed non-blocking as required, but as a **ratchet**
   rather than a pure warning: `conf/causal_graph_audit_baseline.tsv` freezes the
   1541 known findings and `--fail-on` defaults to `new`, so pre-existing
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

**Progress, re-measured 2026-08-05 against `conf/causal_graph_audit_baseline.tsv`.**
Two numbers circulate here and they are *not* the same measurement — quote
whichever you mean, and say which:

| measure | value | source |
|---|--:|---|
| `FRAGMENTED_GRAPH` findings (one per fragmented graph) | **220** | `conf/causal_graph_audit_baseline.tsv` |
| files with ≥1 `UNREACHABLE_FROM_TRAIT` finding | **220** | same file |
| `UNREACHABLE_FROM_TRAIT` findings (the ratchet's per-node unit) | **1321** | same file |
| baseline total | **1541** | `just audit-graphs` |

Corpus totals unchanged: 353 graphs, 4136 nodes. Per-category `FRAGMENTED_GRAPH`:
environment 85, morphology 47, metabolism 31, physiology 27, ecology 18,
genomics 11, upper 1.

**#220 is closed** (#227). `FRAGMENTED_GRAPH` counts components directly rather
than inferring them from reachability, closing a blind spot reachability has by
construction: a graph splitting into components that *each* contain a `TRAIT`
node satisfies "every node reaches a trait node" while still being two
disconnected arguments.

`morphology/dumbbell_shaped.yaml` is the real worked case, and reading it today
is misleading unless you read `history/` with it. The record now declares one
`TRAIT` node and carries 7 `UNREACHABLE_FROM_TRAIT` rows — which looks like
reachability catching it fine. It is the opposite: `v_shaped_daughters` **was**
typed `TRAIT`, so both components were reachable-from-a-trait and the graph
reported clean, and #227 retyped it to `QUALITY` in the same change that added
`FRAGMENTED_GRAPH`. Those 7 rows are the fix working. See
`history/records/dumbbell_shaped/2026-08-03T230903Z-claude-code-90a277.yaml` and
the record's own `curation_history`.

An earlier revision of this section retracted that example as fabricated, on the
strength of the current node types alone, and filed #284 against the script's
comment. Both were wrong and #284 is closed with the correction — the lesson
being that `history/` is what explains why present data looks as it does.

The shape has no *live* instance: a sweep for graphs that are fragmented, carry
more than one `TRAIT` node, and have zero `UNREACHABLE_FROM_TRAIT` rows returns
0, and the two measures above cover the identical 220 files. That is #227 having
removed the one instance, not the check guarding against nothing.

**Backfill progress: 1 done, 220 remaining.** Not "1 of 220" — the arithmetic
matters here. `data/traits/metabolism/cellulolysis.yaml` was repaired *before*
the baseline was frozen, so it has **zero** rows in
`conf/causal_graph_audit_baseline.tsv` and the 220 there are all still to do.
The corpus was 221 fragmented graphs; #183's own 2026-07-30 figure of 220 is the
post-cellulolysis count, which is why it matches today's despite one file being
fixed in between.

It remains the worked example — 4 components, 9 of 14 nodes unreachable,
repaired with 7 evidence-backed edges. Note that it is also in #267's `ECHOES_RESEARCH_REPORT`
set (section 10), so it is simultaneously the template for the backfill and an
example of the snippet shortcut the backfill has to avoid.

After each batch, regenerate with `just audit-graphs --write-baseline` so the
ratchet tightens; at zero, switch to `--fail-on any` and drop the baseline.

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

## 7. CI + agent-workflow thread — SHIPPED; residuals in #191/#197/#209/#358 (+#389/#423/#491)

Update (2026-08-21): **#433 is closed** (#501 — ten regressions plus the
shared provider contract). **#389 remains but should be re-scoped**: #404
re-stated the false byte-identical claim honestly, and #501 put
`_edison_capture.py` under a shared contract, so what remains of #389 is
whatever that contract does not yet enforce.

Update (2026-08-20): **#289 is closed** (#406 — the qc chain resolves
transitively). Other residuals since 2026-08-15: **#423** (`new-history` link
format) and **#491** (the canon ref pin predates `history.yaml` landing in
the hub — filed off #492's review).

Update (2026-08-08): **#198, #217, #252 (→ #285) and #275 (→ #308) are closed.**
Two new residuals joined: **#289** (`audit-qc-paths` does not follow a chain
recipe's own dependencies when the recipe also has a body) and **#358**.

Update (2026-08-15): **#377** — `scripts/check_vendored_sync.sh:9` and this
file's own section 2 still say `culturebotai-claw` is private. It is **public**.
That does NOT revive the repoint (see section 2 — abandoned on architectural
grounds, claw#22 reverted claw#21), but it voids the stated blocker on **#191**
and **#358 step 2**, both of which were parked on "the canonical hub for this
file is private". Two comment edits; both issues are smaller than they read.

Also #372 (fixed in #371): the workflow header told readers to stop it via the
Actions tab, which #348/#354 had silently made wrong — the required set is
derived from the files, so the API toggle leaves the audit expecting a run that
can never happen.

Update (2026-08-13): **automatic `claude-review` is OFF** (#371) while
`CLAUDE_CODE_OAUTH_TOKEN` has no quota — an exhausted account turned every PR
red without saying anything about the PR. `/review` and manual dispatch still
work. Note the method: the trigger was removed from the FILE, because
`audit_required_workflows.py` derives its required set from the files and
`gh workflow disable` would have left the audit expecting a run that can never
happen (#372). Re-enable by restoring two commented lines in `on:`.

**#358 has an ordering constraint worth reading before starting it.**
`src/traitmech/schema/history.yaml` line 9 and lines 20-23 still state the
pre-#325 policy — "one record per session per target" and "presence of a record
is *advisory* — CI warns, it does not block". #357 made it blocking, so the
second is now false, and it is verbatim the argument #325 refuted *with
measurement* (of 134 commits touching trait records, 2 carried a history record;
nobody routed around a gate that did not exist).

#357 did not fix it because the file is vendored byte-identical from claw and
**nothing would detect the drift** — it sits outside `check_vendored_sync.sh`'s
checked set, which is the gap #209 tracks. So:

1. `../culturebotai-claw` **is checked out locally**, so fixing the canonical
   `shared/history/history.yaml` and re-vendoring into the four Mech repos is
   actionable today. Land it in claw first — a one-copy edit here is exactly the
   failure `vendored-sync` exists to prevent.
2. Adding `history.yaml` to `check_vendored_sync.sh` waits on #209 (the canonical
   hub for this file is private, so CI cannot reach it to diff).

`history/README.md` and `.github/workflows/curation-history.yaml` carry the
operative policy meanwhile, and say the schema prose is stale by design rather
than neglect.

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
alongside. **Now proven post-merge**, which it was not when this was written:
every check then had run on a branch carrying its own copy of the fix, and
`issue_comment` runs use `main`'s copy. Since #216 merged, `claude-review` has
run to completion on every PR through #282 without cancelling itself.

`pr-shepherd.yml` was checked and is unaffected — `workflow_dispatch` only,
`cancel-in-progress: false`, no comment trigger. `claude-code-review.yml` is the
only workflow in the repo with an `issue_comment` trigger.

Third concurrency-scoping bug here after #199 and #196's review, which produced
two follow-ups. **Both have since landed.** #218 shipped in #225 —
`pr_sanity.py` now emits `CONCURRENCY_SHARED_ACROSS_TRIGGERS`, so the rule fails
CI rather than only being written down, which mattered because #215 got past a
reviewer who had already fixed this class of bug twice. #217's page shipped in
#272 as `docs/WORKFLOW_CONVENTIONS.md`, carrying the concurrency lessons plus
the action-pinning policy and its own `ACTION_UNPINNED` gate.

**#217 stays open for one question only: where the page lives.** It is fleet
knowledge shared by all four Mech repos, and the copy that landed is
TraitMech-local — so it is either consolidated into CultureMech or claw with the
spokes linking to it, or it becomes the fourth copy #209 warns about. **#275** is
the same argument at file scope: the page restates header comments still sitting
in `pr-sanity.yaml`, `vendored-sync.yaml` and friends, which now cross-link to it
but were not consolidated into it.

**The other pending items are small, independent and fully specified**, each
verifiable by CI, none blocking anything:

| # | fix | note |
|---|---|---|
| #191 | vendored `history.yaml` has no drift check vs claw canonical | cross-Mech; wants the hub |
| #197 | `vendored-sync` couples every PR to CultureMech's availability | cross-Mech; wants the hub |
| #209 | `vendored-sync.yaml` is triplicated across spokes, unguarded | hub has no copy to diff against — same hole as CommunityMech#278 |
| #389 | `_edison_capture.py` claimed byte-identical, differs in every sibling | #404 corrected the claim; #501 added the shared contract — re-scope the residue |
| #423 | `new-history` writes bare-number links when claw is present | violates `range: uri`; TraitMech-local, small |
| ~~#433~~ | ~~Edison sidecar-provenance fix untested~~ | **DONE (2026-08-21, #501)** |
| #491 | `.vendored_canon_ref` predates `history.yaml` in the hub | found by #492's review; re-pin after hub catches up |

Closed since the 2026-08-15 revision of this table: **#289** (via #406 —
`audit-qc-paths` now resolves the qc chain transitively). Earlier: #198, #217,
#252, #275 (see below).

Closed since this section was written: **#192**, **#193**, **#203**, **#205**,
**#208**, **#218** (and #199, #200, #202, #204, #215 before them). Action pinning
and the conventions page landed in **#272**, which also added the
`ACTION_UNPINNED` gate.

## 8. The paid Edison sweep's output was lost — RE-RUN COMPLETE (#241), 353/353 tracked

`reports/trait_graph_audit_manifest.tsv` recorded a 2026-07-20 sweep that
**fully succeeded**: 353 distinct traits, every one `ok`.
The 13 `fail:1` rows are not 13 unfinished traits — each is a `(category, slug)`
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

### What the sweep left behind — two closed 2026-08-16, two remain

- **#244** — **DONE (2026-08-16, #396)**: `--verify` now checks non-emptiness
  and walks disk→manifest, closing the silent-suppression path where a report
  on disk with no `ok` row blocked a call via file-existence-keyed resume.
- **#245** — `cellulolysis` has a second, `-codex` report with no manifest row
  and no sidecar. #253's provider ranking stops it reaching a page.
- **#246** — two `-edison-literature-meta.yaml` files, for 2 of 353 traits, and
  nothing in the repo writes that filename.
- **#248** — `template_file: /Users/marcin/...` in 342 now-tracked reports.
- **#249** — **DONE (2026-08-16, #388)**: the sidecar request was removed and
  the 353 broken sidecars deleted, rather than fixing an extraction nothing
  consumed.

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

## 11. Corpus self-consistency in typing (#356, #364) — PENDING, 83 of 294 remain

The thread #352/#334 closed was one instance of a general problem: **the corpus
disagrees with itself about what a thing is, and the gates only catch it where a
predicate happens to have a domain or range.**

`audit-graphs` now flags `DISPOSITION_MISTYPED` (a `CAPACITY`/`STATE` node whose
description reads as a disposition) and `DUPLICATE_GROUNDING` (two nodes in one
graph on the same CURIE), both at 0 and gated. Neither looks *across* records.

**Measured 2026-08-08 — the issue understates this by 7x.** #356 reports
`proton_motive_force` typed four ways across 9 records. Actually:

| node_type | records |
|---|---|
| `STATE` | 18 |
| `BIOLOGICAL_PROCESS` | 13 |
| `CHEMICAL` | 2 |
| `CAPACITY` | 2 |

**35 records**, one concept. And it is not alone — **63 `node_id`s carry more
than one `node_type` across the corpus**, including `membrane_potential` (4
types), `membrane_lipid_composition` (3), and pairs like
`terminal_electron_acceptor` (`CHEMICAL`/`MOLECULAR_FUNCTION`) and
`superoxide_dismutase` (`GENE_OR_PROTEIN`/`MOLECULAR_FUNCTION`) where both
readings are defensible and the corpus should still pick one per record *and say
why*.

**Why it now has consequences.** #355 minted `METPO:2007900` (`powers`) gated to
`subject_types = BIOLOGICAL_PROCESS|STATE`. Two byte-identical assertions behave
differently purely by subject typing — `carboxydotrophic.yaml`'s
`proton_motive_force` (`STATE`) grounds, `phototrophic.yaml`'s (`CAPACITY`) is
`blocked_by_node_type`. Visible in `reports/predicate_grounding_residual.tsv`.
Three of those four blocks are *correct*; one is only the disagreement.

**The shape of the work** — the same one that has now succeeded three times
(#314 → migrations; #353 → #360):

1. **Detect — DONE (2026-08-13, PR #366).** `INCONSISTENT_NODE_TYPE`, keyed on
   `node_id` and baselined at **294 occurrences across 63 node_ids**. It is
   cross-record, so it does not fit the per-graph loop: `node_type_index()`
   pre-walks the corpus. Findings are emitted per OCCURRENCE rather than on a
   presumed-wrong minority, because nothing knows which type is right; and the
   detail leads with `node_id` rather than the type set, so a family part-way
   through a burn-down does not re-key and un-suppress rows nobody has reached.
   Left open by it: #373, the third full corpus walk — **DONE (2026-08-15, PR
   #378)**: one shared `load_corpus()`, 1431 → 477 parses.
2. **Decide, then normalise — TRANCHE 1 DONE (2026-08-15, PR #382), 294 → 223.**
   The `STATE` vs `BIOLOGICAL_PROCESS` question turned out **not** to be a
   judgement call: `CausalNodeTypeEnum` names `proton_motive_force`,
   `membrane_fluidity` and `reducing power` as its own canonical examples of
   STATE / QUALITY / CAPACITY, and says a state is "the gradient / steady-value,
   **not its establishment**". The corpus disagreed with its own schema in the
   schema's own examples. Five families normalised, 21 nodes, 20 records; the
   `powers` edge #356 was filed for now grounds (blocked 4 → 3, groundable
   2 → 3).

   Read every description before retyping — #352's lesson, and it bit twice
   here. `membrane_fluidity`'s lone BIOLOGICAL_PROCESS node *described*
   "Maintenance of optimal membrane fluidity" (a process, arguing for a rename)
   while its *edges* used it as the property, like all 24 peers. Three signals
   against one: the description was the defect.

3. **Burn down the rest — TRANCHES 2–5 DONE, 223 → 83 across 30 families.**
   Tranche detail: #387 took the `GENE_OR_PROTEIN`/`MOLECULAR_FUNCTION` group
   by splitting protein from activity where one `node_id` meant both (the #352
   rule, applied); #392 stated the `PATHWAY` vs `BIOLOGICAL_PROCESS` rule and
   then applied it; #403 resolved the oxygen family as the predicted two-ids
   case — one `node_id` per sense — and dropped a marine-water CURIE with it;
   #497 (2026-08-21) normalised eight process-quality families and merged four
   duplicate node ids (112 → 83), taking the `BIOLOGICAL_PROCESS`/`QUALITY`
   group (`maximal_growth_rate`, `membrane_rigidification`, `immune_evasion`)
   with it. Remaining as of this reconcile (from
   `conf/causal_graph_audit_baseline.tsv`): **83 occurrences**, headed by
   `terminal_electron_acceptor` (5), `rod_complex` (5), `oxidative_stress`
   (5), `membrane_potential` (4), `membrane_lipid_composition` (4),
   `compatible_solute_transport` (4), then a 3-and-under tail — increasingly
   genuine per-family judgement calls rather than decided rules.
   The table below is the 2026-08-15 plan, kept for the family-by-family
   rationale; its `GENE_OR_PROTEIN`/`MOLECULAR_FUNCTION`,
   `BIOLOGICAL_PROCESS`/`PATHWAY` and `CHEMICAL`/`ENVIRONMENTAL_FACTOR` rows
   are done:

   | signature | fam | occ | note |
   |---|---|---|---|
   | `GENE_OR_PROTEIN`/`MOLECULAR_FUNCTION` | 6 | 24 | **Next.** #352 settled the rule: a protein is not its activity |
   | `BIOLOGICAL_PROCESS`/`PATHWAY` | 10 | 51 | needs a stated rule; the schema only says "a pathway or pathway-like mechanism", which does not decide `ectoine_biosynthesis` |
   | `CHEMICAL`/`ENVIRONMENTAL_FACTOR` | 3 | 36 | genuine two-senses (O2 the molecule vs ambient O2) — likely **two ids**, not one type |
   | `BIOLOGICAL_PROCESS`/`QUALITY` | 8 | 26 | `maximal_growth_rate`, `membrane_rigidification`, `immune_evasion`; the QUALITY definition should carry most |
   | `GENE_OR_PROTEIN`/`PATHWAY` | 5 | 14 | `rod_complex`, `glutamate_decarboxylase_system` — complexes vs the pathways they run |
   | `BIOLOGICAL_PROCESS`/`MOLECULAR_FUNCTION` | 3 | 9 | `na_h_antiport` vs `na_h_antiporter` — see the row above |
   | long tail | 26 | ~63 | 2–9 occurrences each |

   Separate but adjacent: ~~`molecular_oxygen` (21) and `oxygen` (13) are two
   ids for one thing~~ — **DONE (2026-08-17, #403)**, resolved the other way:
   the two spellings were carrying two *senses* (the molecule vs ambient
   oxygen), so the fix was one `node_id` per sense, not a merge.

**Do not repeat #352's mistake.** The test is not "is this type distinct/defensible
in isolation" but "is it compatible with what the record and its predicates
already assert". #360 spent three review rounds learning that; `docs/CURATION_PLAYBOOK.md`
now carries it.

**#364 is the upstream residual of the same thread.** #360 merged away
`salt_tolerance` and `low_ph_tolerance` because METPO models only a *preference*
axis (`METPO:1000629` halophily preference, `METPO:1003000` pH growth
preference) and has no *tolerance* axis — `halotolerant`/`acidotolerant` are
phenotypes that each already anchor their own record. Actionable form is a
`metpo-proposal`, not curation here. Filed so the concepts are recorded rather
than silently lost in a merge.

## 12. Research prioritization: what to apply next, and with what (#426 + #435–#443, #448, #471–#481 subset) — NEW 2026-08-17..20

The question this thread answers: **the paid Edison sweep is complete (section
8), so which trait's research gets APPLIED next, and through which provider if
more research is ever bought?** What landed:

- **#427** (`prioritize-graph-research` skill + `scripts/prioritize_graph_research.py`)
  — rank causal-graph weakness *before* spending money. Its headline finding is
  **#426**: zero traits await a *first* research pass; **351 REVIEWED traits
  have a tracked research report whose findings are not yet applied to the
  YAML**. Applying is the same trait-by-trait work as #183's backfill and
  section 10's snippet burn-down — one campaign, three metrics.
- **#440** — provider triage; "available" now means a credential that can make
  a call, not one that merely exists. Review findings **#435–#439** are open
  (untested `_score`, tracebacks on unknown `--provider`, the "fit 100 is
  relative" caveat).
- **#449** — DisMech's priority dashboard ported (`app/`), lumping rule
  inverted for TraitMech; residuals in **#448**.
- **#470** — the prioritiser now ranks every bin separately (bins share only
  ~5–7% of content — the measured refutation of the family-collapse premise)
  and **refuses to rank on a stale `graph_completeness_audit.tsv`**. Which
  exposed **#443/#480**: the audit was stale for 347/353 traits and nothing in
  the repo could regenerate it.
- **RESOLVED 2026-08-21 (#496): the completeness-audit ranking is RETIRED.**
  `prioritize_graph_research.py`, its tests, skill and recipes are deleted;
  `graph_completeness_audit.tsv` and `graph_enrichment_backlog.md` stay as
  historical paid-research snapshots; the live-state `trait_priority.py` queue
  (from #449) owns prioritization, extended with research-artifact awareness.
  #443/#480 closed. Fallout: **#471/#472/#479 closed as moot** (2026-08-22,
  verified — no consumer of the completeness TSV remains, and
  `trait_priority.py` already keys `series_size` uniformly) and **#481 got
  promoted, not retired**: the
  irreproducible overlap figures (5%/20%/18-of-3256) now live in
  `scripts/trait_priority.py:23-24`, the maintained tool; re-derive (an
  independent review measured 6.9%/25%/3-of-470) and correct.
- PR #461 (the retire-the-prioritiser fork) was **closed** — #496 reached the
  same destination through the maintained tool.

Adjacent: **#409/#410** made Discussions and Knowledge Gaps visible and
answerable, but the corpus carries only 10 records with `discussions` (2%);
**#425** — `curate_knowledge_gaps.py` mutates trait YAML with no
`--dry-run`/`--apply` split, violating the safe-mutation contract.

**The apply-campaign (#426) is the largest open value in the repo**, is no
longer blocked on any ranking question — `trait_priority.py` is the sanctioned
picker — and has begun: #498 (peritrichous) and #499 (predatory-bacterium
lifecycle) are the first two applications; ~349 remain.

## 13. canonical_examples: render, validate, backfill (#444/#445 + #475–#478) — NEW 2026-08-19..20

226 records carried trait→organism links that **no page rendered and nothing
validated** (#444/#445). What landed: **#446** rendered the slot on trait
pages, added taxon-id validation scaffolding, and ran a one-record canary;
**#474** applied batch 1 — 5 records filled, 6 honest skips, after two
adversarial review rounds whose standard is now the rule:

- exemplars come **only from the trait's own deep-research artifact**, cited to
  a DOI present in that artifact;
- every `taxon_id` resolved and label-checked against the local OAK NCBITaxon
  build, labels verbatim;
- **a cultivation condition is not a stated optimum** (#476 — two fabricated
  exemplars were removed by review);
- contrast cases excluded by name.

**#495 (2026-08-21) salvaged the superseded PR #465**: its six non-overlapping
records re-validated under the #474 standard and landed; #465 closed. Coverage
now **237 records** carrying `canonical_examples`.

Open residue: **#444** (~116 records still to fill), **#445**
(`just audit-canonical-examples` exists but is **not in the `qc` chain or any
workflow** — wire it in), **#475** (cell-size bins cannot be filled from
mechanism artifacts — needs a taxon-oriented source), **#478** (bin-measured
exemplars land on family parents while the bin stays empty — policy call).
**#476/#477 closed (2026-08-22)** — records of findings fixed in #474
pre-merge, closure verified against the live records (one surviving
exemplar on `temperature_optimum_high`; the canary's slot repositioned).

## 14. microbedecoder / FAPROTAX residual (#453, #464) — NEW 2026-08-19..20; grounded and gated, terms still missing

microbedecoder's non-chemical residual landed here: **40 enzyme-activity
traits (47k occurrences) with no TraitMech term** (#453). What landed:

- **#454** grounded 42 enzyme-activity labels to GO/EC (reverted once for a
  review finding, re-landed same day); **#459** added the PROTEIN sense of
  `alcohol dehydrogenase`; **#462** resolved three FAPROTAX labels to existing
  traits.
- **#473** applied the accumulated grounding backlog **and gated it so it
  cannot rebuild** — the backlog reports are now freshness-checked like the
  residual TSVs (section 9).
- **#467** — METPO proposal v11: **15 FAPROTAX metabolic-strategy classes**,
  extending the upstream ask (section 4; metpo#535 still shows no upstream
  activity).

Open residue: **#453** (the 40 traits themselves — blocked on METPO minting
for the classes v11 proposes, or on a decision to mint `traitmech:` fallback
ids per `manage-identifiers`); **#464** (56 synonym strings owned by more than
one trait record, so reverse lookup from a microbedecoder label to a trait is
ambiguous — needs an ownership rule before any bulk import).
