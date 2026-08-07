# TraitMech Curation Playbook

Conventions for curating a `TraitRecord` YAML up to
`mapping_status: REVIEWED` with a DOI-backed `causal_graphs` block.
Extracted from the experience of curating 233 records across PRs
#24–#46.

This is a **practical guide**, not the formal schema — see
`src/traitmech/schema/traitmech.yaml` for what is structurally valid.
This playbook describes what reviewers (human and Copilot) will flag
beyond raw schema validity.

## What gets a causal graph

Add a `causal_graphs:` block **only when the trait has source-backed
mechanism structure**. Three healthy use cases:

1. **Concrete phenotype with literature mechanism** — e.g.,
   `halophilic`, `aerobic`, `thermophilic`. Build a 5–7 node graph
   with environmental factor → mechanism → trait edges.
2. **Umbrella class with a regulatory or developmental program** —
   e.g., `sporulation`, `metabolism`, `gc_content`. Build a graph
   that names the program and optionally includes `is a` edges to
   grounded child phenotypes.
3. **Quantitative bin** — e.g., `nacl_optimum_high`,
   `temperature_range_mid2`. Build a compact 3–4 node graph linking
   the numeric range (from the METPO synonym) to a representative
   mechanism, with a single `is a` edge back to the umbrella.

**Thin "classification axis" graphs** are appropriate for
administrative or regulatory classifications that don't have a
biological mechanism of their own — e.g., `biosafety_level_1`. These
get a 3–4 node graph framing the classification as a value on an
axis (hazard properties → classification → containment requirements),
not a phenotype mechanism. See use case 2 above and the
`biosafety_level` family for the established pattern.

**Skip causal graphs entirely when:**

- The record is `term_kind: OBJECT_PROPERTY` or
  `DATATYPE_PROPERTY` (relation carrier). These are predicates,
  not phenotypes — they get a definition + evidence but no graph.
  See "Chemical-use relations" below.
- The record's biology is fully covered by a more specific child
  trait and no umbrella-level mechanism is meaningful.

## Chemical-use relations: predicate + class composition

METPO carries OBJECT_PROPERTY records for chemical-use relations
(e.g. `METPO:2000006` "uses as carbon source", `METPO:2000009`
"uses as electron donor", `METPO:2000008` "uses as electron
acceptor"). The intended modelling pattern is **predicate + class
composition** at the assertion site, NOT a precomposed
substrate-specific TraitRecord per (relation × substrate) pair.

An assertion like "organism X uses glucose as a carbon source" is
modelled as the triple:

```
<organism>  METPO:2000006  CHEBI:17234
```

Curators **should not** create new records like
`uses_glucose_as_carbon_source` to express such pairings. Those
records were attempted briefly (PR #52, reverted) before being
recognised as off-pattern; see `docs/DEPRECATED_REPLACEMENT_PROPOSAL.md`
for the history.

What curators **should** do for the OBJECT_PROPERTY relation
records:

- Keep `mapping_status: REVIEWED` (not DEPRECATED).
- Set `domain:` to the organism class (typically the METPO
  organism URI).
- Set `range_:` to a CHEBI root broad enough to cover the
  predicate's intended substrates. Use `CHEBI:24431` ("chemical
  entity", the top CHEBI root) by default — most chemical-use
  predicates accept both organic and inorganic substrates (CO2 as
  carbon source, H2 / NH3 / Fe2+ as electron donors, nitrate /
  sulfate / O2 as electron acceptors, etc.). A narrower root like
  `CHEBI:50860` ("organic molecular entity") would incorrectly
  exclude these inorganic objects.
- Provide a DOI/PMID-backed `definition_source` and at least one
  literature `evidence` entry framing the relation as a recognised
  microbial-physiology descriptor.
- Do not add a `causal_graphs:` block — these are predicates, not
  phenotypes with mechanism.
- Add `xrefs:` to external ontology predicates where a *true*
  equivalence exists. Survey result (2026-05-17, OLS4 property
  search): six of the 71 un-deprecated metabolism predicates have a
  clean equivalent — `METPO:2000006`/`2000010`/`2000008`/`2000009`
  ↔ the matching MICRO `uses {carbon|energy|electron acceptor|
  electron donor} source` predicates; `METPO:2000103` (`capable_of`)
  ↔ `RO:0002215`; `METPO:2000202` (`produces`) ↔ `RO:0003000`.
  `METPO:2000001` (`organism_interacts_with_chemical`) was
  initially mapped to `MICRO:0000975` "uses chemical entity" but
  reverted on Copilot review: the METPO root covers `produces` and
  other non-use relations as subProperties, while MICRO's predicate
  is restricted to use relations, so the mapping is narrower-than
  rather than equivalent. The remaining predicates (ferments,
  oxidizes, reduces, hydrolyzes, transports, imports, exports,
  requires_for_growth, etc., plus all `does_not_*` negation
  companions) have no organism-level equivalent in RO, MICRO, OBI,
  IAO, or CHIRO. RO models transport/import/export at the *process*
  level, not the organism level, so those METPO predicates
  intentionally lack an RO xref. Treat the absence of an xref as
  documented rather than a gap — leave `xrefs:` unset on records
  without a confident match.

### Do not use these predicates inside causal graphs

Every one of these relations is `rdfs:subPropertyOf METPO:2000001`
("organism interacts with chemical"), whose `rdfs:domain` is
`METPO:1000525` (microbe). Domain is an *inference* rule, not a
check: writing

```yaml
# WRONG — entails that <some_trait> IS a microbe
- subject: <some_trait>
  predicate: uses carbon source        # METPO:2000006
  object: glucose
```

makes a reasoner conclude the trait node is an organism. `predicate_id`
is an unbound string, so `validate-strict` cannot see it — but
`just audit-predicate-domains` **does**, and it runs inside `just qc`.
That class is at zero and is `ERROR` severity, so a new one fails CI and
cannot be baselined away.

`CausalNodeTypeEnum` has no organism member — causal-graph nodes are
deliberately taxon-agnostic — so **no causal-graph edge can satisfy
that domain**.

`uses electron donor` (`METPO:2000009`) and `uses electron acceptor`
(`METPO:2000008`) are gated on this: their `subject_types` in
`mappings/predicate_grounding.tsv` is `NONE`, so
`ground_causal_predicates.py` will refuse to ground them onto any
edge and will report them as `blocked_by_node_type` (#295). No corpus
edge currently carries either label, so the gate is a forward guard —
do not expect a row for them in
`reports/predicate_grounding_residual.tsv`. The other 64 predicates
in this family were the subject of #301, which is **closed**: all 366
edges that carried them have been migrated to causal-graph counterparts
(`METPO:2007800`–`2007812`, proposals v9) or to upstream terms, and each
row in `mappings/predicate_grounding.tsv` is now gated to the node types
it actually admits. The count is **0** and the audit hard-fails on a new
one, so this section describes a mistake the tooling now prevents rather
than a backlog to work around.

### `enables` needs a process-or-activity object

Separately from the domain rule above, `enables` (`RO:0002327`) has a
**range**: biolink declares it `biological process or activity`. Of the
`CausalNodeTypeEnum` members, only these three satisfy it:

`BIOLOGICAL_PROCESS`, `PATHWAY`, `MOLECULAR_FUNCTION`

Any other object type is a range violation, flagged as
`ENABLES_RANGE_VIOLATION`. **33 pre-existing edges** are baselined and
tracked in #334; a *new* one fails `just qc`. What to write instead:

| you want to say | object type | write |
|---|---|---|
| X makes the organism able to exhibit a trait | `TRAIT` | `confers` — `METPO:2007700` |
| a process yields a chemical/entity | any | `has output` — `RO:0002234` |
| one chemical becomes another | `CHEMICAL` | `derives into` — `RO:0001001` |
| X reduces some quantity | any | `decreases` — `RO:0002212` |
| a gene/protein complex is assembled or activated | `GENE_OR_PROTEIN` | not settled — see #334 |
| X enables a tolerance or capability | `TRAIT` | **check the node type first.** A node described as a *capacity to*, an *ability to*, or a *tolerance of* is a disposition, i.e. a `TRAIT` — retype it and use `confers`. Ground it, like any TRAIT row (#334) |
| X generates a gradient, a state, an internal environment | `STATE` | `contributes to` — `RO:0002326`. Only where the subject really does contribute to the object's *occurrence or generation*; a subject that merely **powers** something it does not generate does not qualify (#341) |

If none fits, point `enables` at the graph's **process** node rather than
at the entity: `<gene> enables <the process it drives>` is almost always
both true and range-correct.

The organism-subject form stays valid at the *assertion* site —
`<organism> METPO:2000006 CHEBI:17234` — which is exactly what the
OBJECT_PROPERTY records' `domain:` describes. It is only the
causal-graph reuse that is wrong.

**Do not use `enables` for a TRAIT object.** biolink defines it with
`range: biological process or activity`
(`data/raw/biolink-model.yaml:5099`), and a TRAIT is a disposition,
not a process, so that form carries its own false entailment. #300
moved 15 electron edges onto `<chemical> enables <trait>` as an
interim shape; #302 and #303 settled the question and #323 migrated
all 164 such edges off it. **The count is now 0, and the audit
(`just audit-predicate-domains`) fails any new one.**

Use the `metpo_traitmech_v8` predicates instead. They take a
causal-node domain, so they avoid both the microbe domain above and
the process range:

| Shape | Predicate | `predicate_id` |
|---|---|---|
| any causal node → trait | `confers` | `METPO:2007700` |
| trait → chemical acting as electron donor | `has electron donor` | `METPO:2007701` |
| trait → chemical acting as electron acceptor | `has electron acceptor` | `METPO:2007702` |

Note the electron pair runs **trait → chemical**, which is the
direction `METPO:2000008/2000009` expressed before their inherited
microbe domain made them unusable here. That is what keeps the
donor/acceptor role machine-readable (#303) instead of collapsing
both onto one relation.

```yaml
edges:
- subject: glucose_oxidation           # any causal node
  predicate: confers                   # METPO:2007700
  object: chemoorganotrophy_trait      # the TRAIT
  description: <what makes the organism able to exhibit the trait>.
- subject: lithotrophic_trait          # the TRAIT is the subject here
  predicate: has electron donor        # METPO:2007701
  object: inorganic_electron_donor     # CHEMICAL
  description: <which chemical fills the donor role>.
```

`mappings/predicate_grounding.tsv` gates all three by node type, so
`just ground-predicates` refuses a `confers` edge whose object is not
a TRAIT, or an electron edge whose object is not a CHEMICAL. A node
that names a *function* rather than a substance — such as
`oxygen_preference`'s "O2 as terminal electron acceptor", typed
`MOLECULAR_FUNCTION` — is therefore not eligible for the electron
pair and takes `confers`.

These three ids are **placeholders** until METPO mints the real ones;
see `proposals/metpo_traitmech_v8/proposal.md` for the round-trip plan.

## File-level structure

Order fields in this sequence (matches what merged PRs use):

```yaml
identifier: METPO:XXXXXXX
label: ...
definition: ...
definition_source: DOI:...
trait_category: ...
term_kind: CLASS
mapping_status: REVIEWED      # promote from SEEDED when curating
parent_traits:
- METPO:XXXXXXX
synonyms: [...]               # if any
created_by: ...               # if seeded with one
evidence:
- reference: DOI:...
  snippet: <verbatim phrase>
  notes: <what the snippet supports>
causal_graphs:
- graph_id: ...
  title: ...
  description: ...
  nodes: [...]
  edges: [...]
curation_history:
- timestamp: ...
  curator: seed_from_metpo
  action: SEEDED_FROM_METPO
  ...
- timestamp: <today>
  curator: claude            # lowercase handle (claude, codex,
                             # or your-handle); not a full name
  action: CURATED_CAUSAL_GRAPH
  changes: <one-sentence summary of what was added>
  llm_assisted: true
```

## Definitions

- **Always set `definition_source`** to a DOI/PMID that supports the
  definition.
- **Bin records** without an upstream definition: derive one from the
  synonym threshold, e.g. synonym `NaO_>8` →
  *"NaCl optimum phenotype with best-growth NaCl concentration above
  approximately 8% (w/v)..."*.
- **Inherited grammar bugs**: fix subject-verb agreement and similar
  issues from the upstream seed (e.g., `"that pose"` → `"that poses"`).
  Copilot flags these consistently.
- **Match the synonym's numeric semantics**: if synonym says
  `pHd_5_9`, the definition says "5–9 pH units", not "above ~5"
  (Copilot flagged this on PR #32).

## Top-level `evidence:` block

Two to three entries are ideal. Each is a DOI/PMID, a **verbatim**
snippet, and a `notes:` line explaining what it supports.

- One entry should support the **definition**.
- One entry should support the **mechanism** appearing in the causal
  graph.
- For trait records of well-known biology, **add a representative
  organism example** as a third entry (PMID-backed), following
  `halophilic.yaml` / `aerobic.yaml`. This is high-value and
  Copilot does not require it, but it makes the record genuinely
  useful downstream.

## Causal graph mechanics

### `graph_id`, `title`, `description`

- `graph_id`: short, lowercase, underscore-separated, distinct across
  the repo. Pattern: `<trait_slug>_<mechanism_keyword>`.
- `title`: 5–7 words, human-readable.
- `description`: 1–2 sentences. **Must match what the graph actually
  models** — Copilot will flag if the description mentions a
  node/edge that isn't there. Recurring pitfall.

### Nodes

Required: `node_id` (unique within the graph), `label`,
`node_type`. Optional: `grounding` (CURIE), `description`.

**Pick the right `node_type`:**

| If the node represents… | Use |
|---|---|
| The trait itself | `TRAIT` with `grounding: METPO:...` |
| Another grounded trait (`is a` child, sibling) | `TRAIT` with `grounding: METPO:...` |
| Ambient temperature/pH/NaCl/light/nutrient level | `ENVIRONMENTAL_FACTOR` |
| A named biochemical pathway (TCA cycle, glycolysis, respiration) | `PATHWAY` |
| A biological process (osmotic balance, cytokinesis, etc.) | `BIOLOGICAL_PROCESS` |
| A named enzyme / protein / pathway component | `GENE_OR_PROTEIN` |
| A small-molecule (with optional `CHEBI:` grounding) | `CHEMICAL` |
| A cell-envelope structure, membrane, sacculus | `CELLULAR_LOCALIZATION` |
| A non-membrane organelle (e.g., endospore) | `ORGANELLE` |
| Laboratory practice / containment / experimental design | `EXPERIMENTAL_FACTOR` |
| A molecular role (e.g., "terminal electron acceptor") | `MOLECULAR_FUNCTION` |

`PATHWAY` vs `BIOLOGICAL_PROCESS`: use `PATHWAY` for named ordered
sequences of reactions/steps (TCA cycle, fermentation, respiration —
see `data/traits/metabolism/acetogenesis.yaml` for an example).
Use `BIOLOGICAL_PROCESS` for everything else process-like (a
response, a regulatory event, a state-change).

**Established convention: the bacterial cell wall is
`CELLULAR_LOCALIZATION`** with `node_id: peptidoglycan_cell_wall`
and `grounding: GO:0009274`. Do **not** use `ORGANELLE` for the
cell wall — see PR #26 / #44 precedent. (A small number of older
records may still type the cell wall as `ORGANELLE`; these are
legacy and should be migrated to `CELLULAR_LOCALIZATION` when
touched.)

**TRAIT labels** should match the canonical METPO label of the
trait being grounded — no stray `" phenotype"` suffix beyond what
METPO has (Copilot flagged this on PR #25).

**Every defined node must be referenced by at least one edge.**
Orphan nodes get dropped by the page renderer and Copilot flags
them. If a node feels orphan-y, either wire it in or remove it.

### Edges

Required: `subject`, `predicate`, `object`. Always include `evidence`
on causal edges — every edge needs at least one DOI/PMID-backed
support.

**Predicate vocabulary** (reuse for cross-trait consistency):

| Predicate | Use for |
|---|---|
| `selects for` | environment → trait (selection pressure) |
| `causes` / `triggers` / `produces` / `drives` | environment/factor → response |
| `enables` / `supports` / `contributes to` | mechanism → trait |
| `requires` | strict dependency |
| `maintains` / `mitigates` / `limits` | adaptive responses |
| `protects against` | defensive mechanisms |
| `has mechanistic process` | trait → defining process |
| `acts as` | role assignment |
| `manifests as` | mechanism → trait endpoint |
| `is a` | bin → umbrella, child → parent class |
| `defines` | axis variable → quantitative phenotype |

**Verb form: always third-person singular.** `enables`, not
`enable`. `delivers`, not `deliver`. `confers`, not `confer`.
`specializes`, not `specialize`. **No snake_case predicates** —
use spaces (`combines with`, not `combines_with`).

### Evidence on edges

- **Always include a `reference:`** (DOI/PMID/CHEBI/GO/METPO).
- **The `snippet:` should be a verbatim, contiguous quote** from
  the cited source (no ellipsis, no paraphrase). Copilot flags
  ellipses and paraphrased fragments.
- **Snippets must support the specific edge claim.** If three edges
  all cite the same review with the same one-word snippet, Copilot
  will flag low diversity. Each edge needs a distinct verbatim
  phrase that actually supports *that* edge's assertion. See PRs
  #28, #29, #32, #44 for examples.
- **The `notes:` line** explains *how* the snippet supports the
  claim — not a paraphrase of the snippet, but the reasoning
  linking quote to edge.

#### A deep-research report is not a snippet source (#247)

The reports under `research/traits/` carry an evidence column that
reads exactly like a `snippet:`, and pasting it is the obvious way to
work through #183's backfill. Do not. Nine reports state outright that
their evidence text *"closely paraphrases or quotes"* the source — so
which of the two you are copying is unknowable without opening the
paper, and a paraphrase in `snippet:` quietly converts an
anti-hallucination control into decoration.

The rule, which keeps everything the reports are genuinely good for:

- **`snippet:` requires opening the source.** It is a contiguous span
  copied from the paper, and nothing else earns that field.
- **The report's evidence text belongs in `notes:`**, which is where
  reasoning about a source is supposed to live and has no verbatim
  requirement.
- **The report's reference is reusable as-is** — a DOI is a DOI. What
  does not transfer is the quote.

`just audit-snippets` flags a snippet that also appears in its own
trait's research report (`ECHOES_RESEARCH_REPORT`). It is a prompt to
check, not a verdict: a report may quote the same sentence you did. It
already discounts the two ways a report can echo *you* — the front
matter and the `evidence_summary` fed into the prompt — so a finding
means the text is in the provider's own answer and was never handed to
it.

#### What the audit enforces

`just audit-snippets` runs in `qc` as a ratchet against
`conf/evidence_snippet_baseline.tsv`: today's 2,737 findings never
fail, anything new exits 1. The corpus cannot get worse while the
backlog is worked.

| defect | what it means |
|---|---|
| `ELLIPTICAL_SNIPPET` | contains `...` or `…`, so it is stitched, not contiguous |
| `UNSUPPORTIVE_SNIPPET` | too short to support any specific claim (`host`, `toxins`) |
| `REUSED_SNIPPET` | one snippet on 3+ evidence items of a graph — the low-diversity problem above |
| `MISSING_SNIPPET` | a reference with no quote at all |
| `ECHOES_RESEARCH_REPORT` | also in this trait's report answer — verify against the source |

The standing backlog is worth knowing before you start: **2,586 of
4,089 evidence items (63%) carry no snippet at all**, almost all of
them on causal-graph edges. `snippet:` is schema-optional, so those
are valid records — they simply assert a mechanism on a bare DOI.
Burning that down is the same job as #183's backfill, on the same
edges.

## Curation history

Append a `CurationEvent` for each significant change. Action vocabulary
in use across the repo (any of these is acceptable; prefer the
shorter form for new work):

- `SEEDED_FROM_METPO` — auto-import event (don't write this yourself).
- `CURATED_WITH_LITERATURE` — added definition/evidence from sources.
- `CURATED_WITH_ORGANISM_EXAMPLE` / `ADDED_ORGANISM_EXAMPLE` —
  added a PMID-backed organism example.
- `CURATED_CAUSAL_GRAPH` / `ADDED_CAUSAL_GRAPH` — added or revised
  the causal graph (use `CURATED_*` for first add; `ADDED_*` is
  legacy from earlier curation passes).
- `IMPROVED_CAUSAL_GRAPH_EVIDENCE` — added or strengthened
  edge-level evidence on an existing graph.
- `DEPRECATED_PROPERTY_RECORD` — marked a relation carrier as
  superseded.

`curator:` is a lowercase handle (`claude`, `codex`, or your own
short identifier) — not a full name — so history stays
machine-greppable.

Set `llm_assisted: true` when an LLM helped generate the content.

## Bin records (umbrella + child pattern)

Quantitative-bin records (`*_optimum_*`, `*_range_*`, `*_delta_*`)
share a recipe used across PRs #26, #31–#33:

1. The umbrella (`*_optimum`, `*_range`, `*_delta`) gets a full
   mechanism graph (5–7 nodes).
2. Each bin gets a compact graph (3–4 nodes) with:
   - The bin itself as a `TRAIT` node grounded to its METPO ID.
   - The umbrella as a `TRAIT` node grounded to the umbrella's
     METPO ID.
   - One mechanism node specific to the bin's range.
   - One `is a` edge from bin → umbrella.
3. Bin definitions are derived from the synonym threshold and cite
   one of the references used in the umbrella.

## Cross-axis / numerical-limits umbrellas

`*_phenotype_with_numerical_limits` records and their three-axis
parents (`optimum_phenotype_with_numerical_limits` etc.) get a
thin graph: an `ENVIRONMENTAL_FACTOR` axis node plus three
axis-specific `TRAIT` children (e.g., `nacl_optimum`, `ph_optimum`,
`temperature_optimum`) connected by `is a` edges and a single
`defines` edge from the axis to the umbrella.

## Common Copilot review items

The reviewer (`Copilot`) reliably catches:

1. **Bare-verb predicates** — `enable` instead of `enables`,
   `confer` instead of `confers`.
2. **Verbatim-quote violations** — snippets with ellipsis or
   paraphrase.
3. **Orphan nodes** — defined but never used in an edge.
4. **Low snippet diversity** — same short snippet across many edges
   of a single graph (a single repeated word like "virulence
   factors" or "type III secretion").
5. **Description / graph mismatch** — graph description claims a
   mechanism the graph doesn't actually model.
6. **Inappropriate node types** — `BIOLOGICAL_PROCESS` for things
   that are not processes (e.g., lab equipment, classifications).
7. **Cell-wall node convention** — `ORGANELLE` instead of
   `CELLULAR_LOCALIZATION` for the peptidoglycan wall.
8. **TRAIT label drift** — adding `" phenotype"` to a TRAIT node
   label when the METPO trait it grounds to doesn't carry that
   suffix.
9. **Subject-verb agreement** in inherited METPO definitions
   ("that pose" → "that poses").
10. **Numeric definitions** not matching the synonym threshold
    (e.g., "above ~5" when the synonym says `pHd_5_9`).

## Workflow

```bash
just install
just gen-schema                       # if schema changes
git checkout -b add-<theme>-causal-graphs
# ... edit records ...
just validate data/traits/<cat>/<file>.yaml      # spot-check
just validate-all                                # before commit
git add -p && git commit
git push -u origin <branch>
gh pr create --title "..." --body "..."
gh api repos/CultureBotAI/TraitMech/pulls/<N>/requested_reviewers \
  -X POST --input - <<<'{"reviewers":["Copilot"]}'
# wait for Copilot review, address, resolve threads, merge --delete-branch
```

**Branch hygiene**: always `git checkout main && git pull` before
creating a new feature branch. Otherwise the new branch will carry
prior PR commits and the diff scope leaks (this happened on PR #27,
and was a recurring issue in the early environment PRs).

## Verification

Before opening a PR:

- [ ] `just validate <file>` passes on every modified YAML.
- [ ] `just validate-all` is clean (catches schema regressions).
- [ ] Definitions match synonym thresholds for bin records.
- [ ] Every causal edge has at least one DOI/PMID-backed evidence.
- [ ] Evidence snippets are verbatim and diversified across edges.
- [ ] `mapping_status` set to `REVIEWED`.
- [ ] `curation_history` event appended with today's date.

## Reference: example records to study

- **Concrete phenotype**: `data/traits/environment/halophilic.yaml`,
  `data/traits/environment/aerobic.yaml`,
  `data/traits/morphology/sporulation.yaml`.
- **Umbrella with children**: `data/traits/physiology/trophic_type.yaml`,
  `data/traits/environment/oxygen_preference.yaml`.
- **Cross-axis numerical-limits umbrella**:
  `data/traits/environment/salinity_phenotype_with_numerical_limits.yaml`.
- **Quantitative bin**: `data/traits/environment/nacl_optimum_high.yaml`,
  `data/traits/morphology/cell_length_large.yaml`.
- **Negation/loss-of-function phenotype**:
  `data/traits/morphology/non_motile.yaml`,
  `data/traits/morphology/non_spore_forming.yaml`.
- **Classification axis (non-mechanistic)**:
  `data/traits/ecology/biosafety_level.yaml`.

When in doubt, mirror the closest example above and adapt the
mechanism, references, and bin thresholds.
