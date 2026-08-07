# TraitMech METPO proposals

Each subdirectory is one **cohort** of proposed additions/edits to the upstream
[METPO ontology](https://github.com/berkeleybop/metpo). Cohorts are produced by
the [`metpo-proposal` skill](../.claude/skills/metpo-proposal/SKILL.md); read
the skill before adding or editing anything here.

## Directory layout

```
proposals/
├── README.md                          # this file
└── metpo_traitmech_v<N>/              # one cohort
    ├── proposal.md                    # reviewer narrative
    ├── metpo_proposal_classes_robot.tsv      # 11-col ROBOT template
    └── metpo_proposal_properties_robot.tsv   # 12-col ROBOT template
```

The two `*_robot.tsv` files are the **submittable artifacts** — they are
copy-pasted (or re-used as files) when filing the upstream METPO PR/issue.
`proposal.md` is the human-facing audit trail.

## Cohort naming

- Directory: `metpo_traitmech_v<N>` (e.g. `metpo_traitmech_v1`).
- Subset tag (`oboInOwl:inSubset` column in both TSVs): `metpo_traitmech_<YYYY>_<MM>`.
- ID block (placeholder, pre-mint): `METPO:1007400+` for classes,
  `METPO:2007400+` for predicates. The exact block used must be documented in
  the cohort's `proposal.md`.

See the skill's "ID-space conventions" and "Updating an existing proposal"
sections for the block-allocation rules across cohorts.

## Three legitimate proposal scopes

A. **Synthetic trait classes** — lift `traitmech:NNNNNN` records from
   `data/traits/` to METPO so the curator-minted fallback IDs can be retired.
B. **Causal-graph predicates** — when `CausalEdge.predicate_id` lacks an
   RO/OBI/upstream home. Rare; default to RO first.
C. **Schema-side controlled vocabularies** — currently only
   `CausalNodeTypeEnum` qualifies. Workflow enums
   (`PriorityEnum`, `MappingStatusEnum`, `TraitCategoryEnum`, `TermKindEnum`,
   `SynonymTypeEnum`) MUST NOT be lifted.

## Verifying a cohort

```bash
just verify-proposal metpo_traitmech_v1
```

Runs column-count checks, parent-integrity check, Scope-A citation resolution
and Scope-C enum coverage. Exits non-zero on any failure. See the skill for
the underlying scripts.

## See also

- Skill: `.claude/skills/metpo-proposal/SKILL.md`
- Cross-Mech analogue with a worked example:
  `CommunityMech/CommunityMech/proposals/metpo_communitymech_v1/`
- Upstream rules: `kg-microbe/.claude/skills/metpo-proposal/SKILL.md`
- Synthetic-ID policy: `.claude/skills/manage-identifiers/SKILL.md`
