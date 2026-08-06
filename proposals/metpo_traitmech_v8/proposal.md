# METPO ROBOT Template Proposal — TraitMech Trait-Realization and Electron-Role Lift (v8, 2026-08)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535) alongside
> the v1–v7 cohorts — requesting real METPO IDs for this cohort.

## Context

Two open TraitMech defects share one root cause: the corpus has no
**range-correct relation whose object is a trait**.

`RO:0002327` (*enables*) has been doing that job by default. It is the corpus's
most-used causal predicate, and the repo's own vendored
`data/raw/biolink-model.yaml:5099-5110` defines it as:

```yaml
enables:
  domain: physical entity
  range: biological process or activity
```

A `TRAIT` node is a disposition, not a process. Every `enables` edge pointing at
a TRAIT therefore entails `trait ⊑ BiologicalProcessOrActivity` — a false type
entailment, the same shape as the `RO:0002411` defect fixed in
[#235](https://github.com/CultureBotAI/TraitMech/issues/235). There are
**164 such edges**
([#302](https://github.com/CultureBotAI/TraitMech/issues/302)).

The obvious alternative is worse. METPO's own chemical-interaction predicates
(`METPO:2000008` *uses as electron acceptor*, `METPO:2000009` *uses as electron
donor*, and 64 siblings) are transitively `rdfs:subPropertyOf METPO:2000001`,
whose `rdfs:domain` is `METPO:1000525` (**microbe**). `CausalNodeTypeEnum` has no
organism member, so **no causal-graph edge can ever satisfy that domain** — such
an edge entails that its subject *is a microbe*
([#301](https://github.com/CultureBotAI/TraitMech/issues/301), 366 edges).

That squeeze is what forced [PR #300](https://github.com/CultureBotAI/TraitMech/pull/300)
to reverse 15 electron edges from `<trait> uses electron donor|acceptor <chemical>`
onto `<chemical> enables <trait>`. Both source predicates collapsed onto one
generic relation, and for 7 of the 15 the donor/acceptor role now survives only
in free-text `description:`
([#303](https://github.com/CultureBotAI/TraitMech/issues/303)) — a real loss in a
KG whose purpose is machine-readable causal structure.

This cohort proposes the three predicates that resolve all of it, following the
v1 convention that causal-graph relations take `METPO:1007401` (*trait causal
node*) as both domain and range — the choice that sidesteps the microbe domain
and the process range at once.

## Scope

| Scope | Source | # rows | Lift status |
|---|---|---:|---|
| A (synthetic trait classes) | `data/traits/**/*.yaml` records whose `identifier:` starts with `traitmech:` | 0 | out of scope here — 120 exist in the corpus and none are lifted by any cohort, tracked in [#319](https://github.com/CultureBotAI/TraitMech/issues/319) |
| B (causal-graph predicates) | the 164 `RO:0002327`→TRAIT edges (#302) and the electron-role edges among them (#303) | **3 predicates / 164 edges** | included |
| C (controlled vocabularies) | already lifted in v1 (`CausalNodeTypeEnum`) | 0 | already covered |

Total property rows in v8: **3**. No class rows; v1 already proposed the domain
class (`METPO:1007401` *trait causal node*).

The 164 edges partition cleanly and exhaustively across the three predicates —
verified by walking every `causal_graphs[].edges[]` in the corpus:

| Proposed | Edges | Trait records | Shape |
|---|---:|---:|---|
| `METPO:2007700` confers | 146 | 114 | any causal node → trait |
| `METPO:2007701` has electron donor | 13 | 13 | trait → chemical acting as donor |
| `METPO:2007702` has electron acceptor | 5 | 3 | trait → chemical acting as acceptor |
| **total** | **164** | | |

`confers` subject types, as observed: BIOLOGICAL_PROCESS 81, GENE_OR_PROTEIN 32,
ENVIRONMENTAL_FACTOR 12, QUALITY 5, CELLULAR_LOCALIZATION 5, PATHWAY 4,
CHEMICAL 4, MOLECULAR_FUNCTION 2, STATE 1. The spread across nine node types is
the argument for one general relation rather than a per-type family: what the
edges have in common is that the subject is the *basis* of the trait, not what
kind of thing the subject is.

## Predicate proposals

| ID | Label | Domain | Range | Source record |
|---|---|---|---|---|
| `METPO:2007700` | confers | `METPO:1007401` | `METPO:1007401` | `genomics/crispr_cas_system.yaml#crispr_adaptive_immunity` |
| `METPO:2007701` | has electron donor | `METPO:1007401` | `METPO:1007401` | `physiology/lithotrophic.yaml#lithotrophic_inorganic_donor_energy` |
| `METPO:2007702` | has electron acceptor | `METPO:1007401` | `METPO:1007401` | `metabolism/dissimilatory_iron_reduction.yaml#dir_ferric_iron_respiration` |

### Why not RO, Biolink, or an existing METPO term?

| Proposed | Considered | Why rejected |
|---|---|---|
| `confers` | `RO:0002327` enables | Range is 'biological process or activity'; a trait is a disposition. This is the violation being fixed (#302), so reusing it is circular. |
| `confers` | `RO:0002200` has phenotype | Domain is an organism; the subject here is a causal-graph node (a protein, a process, a condition), not the organism. |
| `confers` | `biolink:contributes_to` | Too weak — states participation without asserting the subject is what makes the trait realizable. |
| `confers` | `METPO:2007400` manifests as (v2) | Closest existing proposal, but scoped to *physiological state → observable trait*. 114 of these 146 subjects are proteins, processes, or environmental conditions, which do not "manifest as" a trait. Kept distinct rather than widened. |
| `has electron donor` / `has electron acceptor` | `METPO:2000009` / `METPO:2000008` | Exactly the right sense, but their inherited `rdfs:domain` is microbe (#301), so a causal-graph subject entails `⊑ microbe`. Recorded as `skos:closeMatch` in the SSSOM file. |
| `has electron donor` / `has electron acceptor` | `METPO:2007603` serves as electron donor and acceptor (v6) | Deliberately the *combined* disproportionation case (one species in both roles). It cannot express the distinction #303 is about. |

### Direction, and why it is reversed relative to the current edges

The 18 electron edges currently read `<chemical> --enables--> <trait>`. Under
this proposal they read `<trait> --has electron donor|acceptor--> <chemical>`.

That restores the direction METPO:2000008/2000009 expressed before their
organism domain made them unusable here — the trait is the bearer, the chemical
fills the role. The reversal is the point: it is what lets one relation per role
replace a single generic relation.

`dissimilatory_iron_reduction` is the sharpest case. All three of its Fe(III)
species — `ferric_iron`, `solid_fe3_mineral`, `dissolved_fe3_om_complex` — are
terminal electron acceptors, and the file's own node descriptions say so
("Terminal electron acceptor reduced in DIR"). After PR #300 reversed two of them
onto `enables`, **nothing in predicate terms records the acceptor role at all**;
it survives only in free text. Under this proposal all three read
`dir_trait --has electron acceptor--> <Fe(III) species>`, which is both
range-correct and role-bearing.

### The declared OWL range is deliberately weaker than the definitions

All three rows take `domain = range = METPO:1007401` (*trait causal node*). That
is the v1 convention and is what dodges both the microbe domain and the process
range — but it means the object side is **unconstrained in OWL**, while the
definitions of `has electron donor`/`has electron acceptor` say "a chemical
species". Upstream should not read the declared range as tight.

Tightening the range to a chemical class was considered and rejected for this
cohort: `METPO:1007401`'s subclasses are the causal-node *type* vocabulary, and
committing the range to CHEBI would re-import the cross-ontology coupling the v1
convention exists to avoid. The constraint is instead enforced data-side, via
`subject_types`/`object_types` on the `mappings/predicate_grounding.tsv` rows
(see Round-trip plan), which is where the corpus's other node-type gates live and
is machine-checked by `just ground-predicates`.

### Pairing

`has electron donor` and `has electron acceptor` are **siblings, not a paired
positive/negative set**. The kg-microbe paired convention (`does not <stem>` +
shared related-synonym) applies to capability negation; donor and acceptor are
two distinct roles on the same axis, both positive. This matches the v2
treatment of `challenges`/`mitigates`, which that cohort likewise declined to
model as a positive/negative pair.

## ID space and subset

- Predicates: **`METPO:2007700`–`METPO:2007702`**. The `2007700` block is free —
  v2 occupies `2007400`–`2007407`, v4 `2007500`, v6 `2007600`–`2007603`.
- No class rows, so no allocation in the `1007xxx` space. Confirmed no collision
  with CommunityMech v1 (`1007100`–`1007220`) or with TraitMech v1–v7
  (`1007400`–`1007402`, `1007410`–`1007423`, `1007500`–`1007505`,
  `1007600`–`1007721`).
- Subset tag: **`metpo_traitmech_2026_11`** (v7 used `metpo_traitmech_2026_10`;
  tags are sequential per cohort, not calendar months).
- Verified against `data/raw/metpo.owl`: the highest minted METPO property is
  `METPO:2000516`, so the `2007700` placeholder block is clear of the real ID
  space.

## Files

| File | Rows (excl. 2 header rows) |
|---|---:|
| `metpo_proposal_properties_robot.tsv` | 3 |
| `metpo_proposal_mappings.sssom.tsv` | 3 |
| `proposal.md` | — |

No `metpo_proposal_classes_robot.tsv`: this cohort proposes no classes.

## Verification

- `just verify-proposal metpo_traitmech_v8` — **PASS** (`failures: 0`). Note this
  required fixing a pre-existing bug in `scripts/verify_metpo_proposal.py`: its
  Scope-A check ran even for cohorts with no classes template, so every
  predicate-only cohort (v2, v4, v6 — and this one) failed once the corpus gained
  its first `traitmech:` id. The script already announced it would skip that case
  and `check_scope_c` already honoured it. Fixed in the same PR; see
  [#318](https://github.com/CultureBotAI/TraitMech/issues/318). The separate
  finding that 120 corpus `traitmech:` ids remain un-lifted by any cohort — which
  is why v1 and v7 still fail this check — is tracked in
  [#319](https://github.com/CultureBotAI/TraitMech/issues/319).
- `just robot-validate-proposal metpo_traitmech_v8` — **PASS**: `props.owl`
  compiles, merges with `metpo.owl`, ELK reasons with no UNSAT
  (reasoned − merged = **+6** lines, matching v6's delta for 4 properties; no
  unintended inferred equivalences).
- Column counts: 12/12 on every row of the properties template, ROBOT header
  padded to full width.
- `definition_source` hygiene (#83): all three cite a TraitMech curation event
  (`TraitMech:data/traits/...#<graph_id>`), each anchor verified to be a real
  `graph_id` in that file. Cross-ontology alignments appear only in `xrefs` and
  the SSSOM file, never in column 4.
- Edge partition (146 + 13 + 5 = 164) computed from the corpus, and cross-checked
  against the independently-derived `ENABLES_RANGE_ON_TRAIT` count in
  `reports/predicate_domain_audit.tsv`.

## Appendix — the explicit 164-edge partition

Published in full so the buckets are checkable rather than inferrable from the
counts. Regenerate by walking every `causal_graphs[].edges[]` with
`predicate_id: RO:0002327` and a `TRAIT` object; a `CHEMICAL` subject whose label
or edge description names an electron donor/acceptor role goes to the role-bearing
pair, everything else to `confers`.

### `METPO:2007702` has electron acceptor — all 5 edges

| trait record | subject (chemical) | object (trait) |
|---|---|---|
| `metabolism/dissimilatory_iron_reduction.yaml` | iron(3+) | dissimilatory iron reduction |
| `metabolism/dissimilatory_iron_reduction.yaml` | solid Fe(III) mineral | dissimilatory iron reduction |
| `metabolism/dissimilatory_iron_reduction.yaml` | dissolved Fe(III)-organic-matter complex | dissimilatory iron reduction |
| `metabolism/dissimilatory_manganese_reduction.yaml` | Mn(IV) oxide | dissimilatory manganese reduction |
| `metabolism/dissimilatory_metal_reduction.yaml` | terminal electron acceptor | dissimilatory metal reduction |

### `METPO:2007701` has electron donor — all 13 edges

| trait record | subject (chemical) | object (trait) |
|---|---|---|
| `physiology/chemoautolithotrophic.yaml` | inorganic electron donor | chemoautolithotrophic |
| `physiology/chemolithoautotrophic.yaml` | inorganic electron donor | chemolithoautotrophic |
| `physiology/chemolithoheterotrophic.yaml` | inorganic chemical donor | chemolithoheterotrophic |
| `physiology/chemolithotrophic.yaml` | inorganic chemical electron donor | chemolithotrophic |
| `physiology/chemoorganoheterotrophic.yaml` | organic molecule | chemoorganoheterotrophic |
| `physiology/hydrogenotrophic.yaml` | molecular hydrogen | hydrogenotrophic |
| `physiology/lithoautotrophic.yaml` | inorganic electron donor | lithoautotrophic |
| `physiology/lithoheterotrophic.yaml` | inorganic electron donor | lithoheterotrophic |
| `physiology/lithotrophic.yaml` | inorganic electron donor | lithotrophic |
| `physiology/organoheterotrophic.yaml` | organic compound | organoheterotrophic |
| `physiology/organotrophic.yaml` | organic compound | organotrophic |
| `physiology/photolithotrophic.yaml` | inorganic electron donor | photolithotrophic |
| `physiology/photoorganoheterotrophic.yaml` | organic compound | photoorganoheterotrophic |

### `METPO:2007700` confers — 146 edges by subject node type

| subject `node_type` | edges |
|---|---:|
| BIOLOGICAL_PROCESS | 81 |
| GENE_OR_PROTEIN | 32 |
| ENVIRONMENTAL_FACTOR | 12 |
| CELLULAR_LOCALIZATION | 5 |
| QUALITY | 5 |
| CHEMICAL | 4 |
| PATHWAY | 4 |
| MOLECULAR_FUNCTION | 2 |
| STATE | 1 |
| **total** | **146** |

Grand total: 146 + 13 + 5 = 164

Two classification notes a reviewer will want:

- `environment/oxygen_preference.yaml#oxygen_terminal_electron_acceptor` is
  labelled *"O2 as terminal electron acceptor"* but typed `MOLECULAR_FUNCTION`
  (it denotes the *use* of O2, not O2 itself). It therefore lands in `confers`,
  as one of the two MOLECULAR_FUNCTION subjects — **not** under
  `has electron acceptor`, whose definition requires a chemical species. Retyping
  that node to `CHEMICAL`/`CHEBI:15379` is defensible but is a corpus change, so
  it is left for the migration PR rather than assumed here.
- All five `has electron acceptor` edges come from three dissimilatory-reduction
  records; all thirteen `has electron donor` edges are one-per-record across the
  lithotrophy/organotrophy family.

## Upstream path

Submit `metpo_proposal_properties_robot.tsv` and
`metpo_proposal_mappings.sssom.tsv` to
[berkeleybop/metpo](https://github.com/berkeleybop/metpo), consolidated into
issue #535 with the v1–v7 cohorts. `2007700`–`2007702` are TraitMech
placeholders; METPO maintainers mint the real IDs.

## Round-trip plan

This cohort is the *design* half. The corpus migration follows as a separate PR
(the 164-edge sweep is deliberately not bundled here — #301 notes that doing the
whole thing at once would be unreviewable):

1. Add the three predicates to `mappings/predicate_grounding.tsv` with
   `subject_types`/`object_types` gated to the node types each actually admits,
   so the grounding tool enforces the new shapes.
2. Repoint the 146 `confers` edges (direction unchanged) and reverse the 18
   electron edges onto the role-bearing pair.
3. Regenerate `reports/predicate_domain_audit.tsv` and rewrite
   `conf/predicate_domain_audit_baseline.tsv`: `ENABLES_RANGE_ON_TRAIT` should
   fall **164 → 0**, which is the machine-checkable proof that the migration
   landed.
4. After upstream mints real METPO IDs: update `data/raw/metpo.owl`, re-seed, and
   swap the placeholder CURIEs for the minted ones in
   `mappings/predicate_grounding.tsv` and the affected `data/traits/**` edges.

## Change log

- v8, 2026-08: propose `confers` (`METPO:2007700`) plus the role-bearing pair
  `has electron donor` / `has electron acceptor`
  (`METPO:2007701`–`METPO:2007702`), resolving the `enables` range violation
  (#302) and the donor/acceptor role loss (#303). No corpus edges grounded in
  this cohort; migration tracked separately.
