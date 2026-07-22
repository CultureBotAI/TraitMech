# Next Tasks — TraitMech backlog

Deferred work, each entry with enough context to pick up cold. **Maintenance:**
update this file as work is started/finished — move done items out, add new
deferrals here. Keep the cross-Mech items in sync with the sibling repos'
`NEXT_TASKS.md` (CultureMech / MIM / CommunityMech).

Last reconciled: 2026-07-22.

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
merge → bump `.vendored_canon_ref` here. `schema-pin` is a separate set, unaffected.

The 15 pre-existing MISMATCHES found at adoption were all wrong CURIEs in
`mappings/node_grounding.tsv` (e.g. `PATO:0000383` is "female", not "decreased
temperature"); corrected to the right CURIEs (verified vs OAK) and the trait-YAML
`grounding:` values re-migrated. One curator-accepted residual stays green via
`exceptions:` (`PATO:0001717` "light intensity" — OAK canonical is the awkward
"radiation emitting intensity quality"). Gate now reports 113 OK_CANONICAL +
2 OK_SYNONYM + 1 OK_EXCEPTION, 0 errors.

Update (2026-07-22): more vendored-file fixes landed through the hub-and-spoke
model, and the canonical *source* is being moved off CultureMech into claw.
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

**IN PROGRESS — canonical source CultureMech → claw (cross-Mech; blocked on a
human action).** Rationale: CultureMech (a data repo) was the hub only by
accident; the shared tooling belongs in claw (the coordination repo), so no Mech
is privileged. Done: **`culturebotai-claw#18` merged** — `shared/idlabel/` now
holds the one canonical copy (validator + `chem_formula` + 3 tests, byte-identical
to all four Mechs at convergence) with a README, MANIFEST, and an `id-label-canon`
CI job. Remaining (ready, not started): repoint each Mech's
`scripts/check_vendored_sync.sh` `CANON_REPO` → `CultureBotAI/culturebotai-claw`
with a `shared/idlabel/` path prefix, and set each `scripts/.vendored_canon_ref`
to a claw commit (currently `1ad5d40`); **CultureMech gains a `.vendored_canon_ref`
and becomes a peer spoke.** File content does not change — pure source relocation.
**BLOCKER: claw is private**, and the sync uses tokenless `raw.githubusercontent`
which 404s on private repos (works today only because CultureMech is public). The
agreed fix is to make claw public (history scanned clean of secrets 2026-07-22);
once public, run the four repoints (via worktrees, mech-CI-validated). Also
converge `check_vendored_sync.sh` itself — it had drifted in CommunityMech. Note:
claw Actions are currently failing account-wide (exhausted private-repo runner
minutes); going public clears that too.

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
