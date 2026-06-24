# Updating an Existing Proposal (edit / extend / re-version)

*Reference for the **metpo-proposal** skill — see [`../SKILL.md`](../SKILL.md) for the overview, scopes, ID-space conventions, and workflow.*

---

## Updating an existing proposal

The workflow above produces a **new** cohort. When work on an existing cohort
isn't finished, pick one of three update paths instead of starting fresh.

### Decision rule

| Situation | Path | Why |
|---|---|---|
| Reviewer (human or Copilot) asks for changes on an open PR before merge | **Edit in place** | The IDs and subset tag are still proposal-stage; no downstream consumer has pinned them yet. |
| Cohort is merged on main and you want to add more lifts (e.g., a new wave of `traitmech:` synthetic IDs after the original cohort) | **Extend in place** | Append-only is non-breaking; reviewers can diff the new rows against the same cohort. |
| Cohort is merged and the underlying schema changed in a way that invalidates existing rows (e.g., a `CausalNodeTypeEnum` value was renamed or removed, or a `traitmech:` record was retracted before upstream minted its METPO ID) | **New cohort version** | A breaking semantic change needs a fresh subset tag and ID block so consumers can pin to the old or new version. |
| Real METPO IDs have been minted upstream and a row has been re-IDed | **New cohort version** | Mutating an already-minted ID is hostile to downstream consumers. Old cohort stays as the audit trail of what was proposed; new cohort tracks the post-mint state. |

### Path A — Edit in place (open PR)

Modify rows directly in `proposals/<cohort>/metpo_proposal_*.tsv`. Keep the
original `proposed_id`, `subset`, and column structure. Update
`definition`, `definition_source`, `parent`, `synonyms`, or `label` in
place. Re-run `just verify-proposal <cohort>`. Commit on the same branch and
let the Copilot review thread close.

If the edit is to the narrative only (no TSV change), edit `proposal.md`
and add a one-line note under the Change log section:
`- v1, 2026-05 (revised <date>): <one-line summary>`.

### Path B — Extend in place (merged cohort)

Add new rows to the **same** `metpo_proposal_*.tsv` files in the **same**
cohort directory. Append-only — never reorder or renumber existing rows.
Conventions:

- New rows use a **contiguous fresh block** within the same
  `METPO:1007NNN` / `METPO:2007NNN` range. Pick a block at least 10 above
  the highest existing ID to leave room for v1 patches. Document the new
  block in `proposal.md` under the ID space section.
- Same `subset` tag as the rest of the cohort. The tag identifies the
  cohort, not the round of additions.
- New `parent` references may point at existing rows in the cohort (this is
  the main reason to extend rather than re-version).
- Update `proposal.md`:
  - Add the new lift to the Scope table.
  - Add the new ID sub-block to the ID space section.
  - Append a Change log entry: `- v1.N, <date>: extended with <description>
    (+<row count> classes / +<row count> properties)`.

Open a new PR titled `Extend METPO proposal <cohort> with <description>`.
Re-request Copilot review.

### Path C — New cohort version

Create a fresh directory `proposals/<base-name>_v<N>/` (e.g.,
`metpo_traitmech_v2/`) with:

- Fresh `subset` tag: bump the month-year suffix
  (`metpo_traitmech_2026_05` → `metpo_traitmech_2026_07`).
- Fresh **ID block** in the `1007NNN` / `2007NNN` placeholder range, **not
  overlapping with v1**. Document the new block in v2's `proposal.md`.
- v2 `proposal.md` must include a `## Relationship to v1` section that
  names every v1 ID retired or redefined, with the reason.
- v1 stays on disk read-only. Add a top-of-file note to v1's `proposal.md`:
  `> Superseded by proposals/<base-name>_v<N>/proposal.md (<date>). v1 is
  retained for traceability.`

Use this path sparingly — the kg-microbe pipeline assumes one active cohort
per source repository at a time, and re-versioning forces downstream
consumers to switch their queries.

### What not to do

- Do **not** edit IDs after they've been merged on main (use Path B or C
  instead).
- Do **not** mix Path B (extend) and Path C (re-version) in the same PR —
  reviewers can't tell what's append-only vs. breaking.
- Do **not** delete rows in Path B. If a row is obsolete, mark it by
  setting `priority` to `LOW` and adding an `observations` note; let Path C
  retire it cleanly.

