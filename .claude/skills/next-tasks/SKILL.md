---
name: next-tasks
description: Assess and maintain the TraitMech backlog. Reconciles NEXT_TASKS.md against what actually shipped (merged PRs, git log, open issues/PRs), separates genuinely-pending actionable work from done/stale/upstream-blocked items, surfaces a short prioritized menu with a recommendation, and — when asked — picks one up. Also the maintenance path for NEXT_TASKS.md itself — marking done items, adding new deferrals, bumping the reconcile date, and keeping cross-Mech items in sync. Use whenever the user asks "next tasks", "what's next", "is the backlog current", or after finishing a work thread.
category: workflow
requires_database: false
requires_internet: false
version: 1.0.0
---

# Next Tasks (backlog assessment + maintenance)

## Overview

**Purpose**: answer "what should I work on next?" *accurately*, and keep
`NEXT_TASKS.md` honest. The backlog drifts — items marked "pending" get shipped
in PRs, whole new threads never get logged, and some items are upstream-blocked
and will never be actionable here. This skill reconciles the written backlog
against reality, then produces a short, prioritized, *actionable* menu.

**Always reconcile before recommending** — never read `NEXT_TASKS.md` and relay
it verbatim.

**When to use**: the user says "next tasks" / "what's next" / "anything left?",
asks whether the backlog is current, or you've just closed a work thread.

**When NOT to use**: to discover brand-new traits. TraitMech has no in-repo
discovery skill — the trait set follows METPO, and a genuinely new term goes
through `metpo-proposal`. This skill works the *existing* backlog.

## Workflow

### Step 1 — Reconcile

```bash
sed -n '1,400p' NEXT_TASKS.md
git log --oneline -20
gh pr list --state merged --limit 20 --json number,title,mergedAt \
  -q '.[] | "\(.number)\t\(.mergedAt[:10])\t\(.title)"'
gh pr list  --state open  --limit 20 2>/dev/null | head
gh issue list --state open --limit 30 2>/dev/null | head -30
```

For each pending item: *is its deliverable already in a merged PR or in the
code?* If yes → DONE. Spot-check any slot/recipe/file the item names
(`grep -rl <slot> src/traitmech/schema/`) — backlog notes cite things that were
later renamed.

TraitMech-specific traps when judging "done":

- **Upstream-blocked is the common case here.** A trait needing a METPO term
  that doesn't exist yet cannot be finished in this repo. Keep such items listed
  (they explain gaps) but never recommend one as "next" — the actionable form is
  a `metpo-proposal`, not the curation itself.
- **Research output is not curated content.** Files under `research/traits/`
  are *inputs*. An item is only DONE when DOI-backed claims have been applied to
  the `TraitRecord` YAML, not when a report exists.
- **Traits are addressed `category/slug`.** Slugs are unique only within a
  category, so an item naming a bare slug may be ambiguous — resolve it before
  acting.

### Step 2 — Present the menu

- one line per PENDING & actionable item, ranked by value;
- call out what's newly DONE and what's UPSTREAM-BLOCKED (so gaps are explained);
- **recommend one** — usually the item that continues the active thread, is
  fully specified, or unblocks the most downstream work.

Use `AskUserQuestion` only when the directions genuinely diverge; otherwise
recommend and proceed on confirmation.

### Step 3 — Maintain NEXT_TASKS.md (every invocation, even if only bookkeeping)

- Mark shipped items **DONE (YYYY-MM-DD, PR #NNN)** in place, or move them out.
- Add unlogged threads as their own `##` section with cold-start context
  (what / why / next, PRs, key ids/paths).
- Convert relative dates to **absolute**; bump `Last reconciled:` to today.
- For **cross-Mech** items (kept in sync with CultureMech / MIM / CommunityMech),
  flag divergence — but do not edit sibling repos unless asked.

Commit the reconciliation. Doc-only changes hit path-filtered workflows and may
show "no checks reported" — that's `MERGEABLE`/`CLEAN`, not a failure.

### Step 4 — Pick it up (only if the user says to)

Hand off to the right skill, then drive it the usual way: branch → implement →
`just qc` → PR → watch CI → squash-merge `--delete-branch` → sync main. Re-run
Step 3 to record the new state.

## CI gates (what "green" actually means here)

Gates, from `.github/workflows/`:
`label-correspondence`, `validate-strict`, `qc`, `pytest`.

TraitMech is the leanest of the four — there is no evidence or SSSOM workflow
here, so nothing in CI checks research provenance. If a backlog item claims
citations validate, verify it locally.

## Conventions this skill enforces

- **Reconcile-before-relay**: the file is a starting point, not ground truth.
- **Honest classification**: don't recommend upstream-blocked items; don't hide
  them either.
- **Every invocation updates the file** (at minimum the reconcile date).
- **Absolute dates**, PR numbers on done items, cold-start context on new items.

## Notes & limitations

- `scripts/validate_id_label_correspondence.py`, `scripts/chem_formula.py`, and the
  three `tests/test_id_label_*.py` files are vendored **byte-identical** across the
  four Mech repos. The old self-generated sha256 pin was retired (it compared a copy
  to a hash from the *same* repo, so all four could pass while diverged). Drift is now
  caught by the `vendored-sync` CI job (`scripts/check_vendored_sync.sh`), which diffs
  these files against `CultureBotAI/CultureMech@<scripts/.vendored_canon_ref>`. To
  propagate a change: PR into that hub → merge → bump `.vendored_canon_ref` here.
  TraitMech has originated cross-repo fixes before (the `id(adapter)` cache-reuse
  fix), so a change may need to flow *out* to the hub, not just in — land it in
  CultureMech first, then re-pin the ref everywhere.
- `.claude/` is gitignored here — a new skill or command needs `git add -f`.
- Without `gh` or a network, reconcile from `git log` alone and say so.

## Related

- `metpo-proposal` — the actionable form of a "needs a METPO term" blocker.
- `deep-research-trait`, `research-causal-graphs`, `manage-identifiers`,
  `audit-schema-gaps`, `schema-gap-analysis` — the skills a chosen backlog item
  is usually handed off to.

## Related files

- `NEXT_TASKS.md` — the backlog this skill reads and maintains.
