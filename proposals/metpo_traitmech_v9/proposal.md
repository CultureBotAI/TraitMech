# METPO ROBOT Template Proposal — TraitMech Causal-Graph Chemical Interactions (v9, 2026-08)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535) alongside
> the v1–v8 cohorts — requesting real METPO IDs for this cohort.

## Context

[#301](https://github.com/CultureBotAI/TraitMech/issues/301): **366 causal-graph
edges assert microbe-domain METPO predicates on non-organism subjects.**

67 METPO object properties are transitively `rdfs:subPropertyOf METPO:2000001`
("organism interacts with chemical"), which declares
`rdfs:domain METPO:1000525` (**microbe**). The children mostly declare no domain
of their own, so they inherit it. OWL domain is an *inference rule, not a
constraint*: an edge `<biological process> produces <chemical>` does not fail
validation — it **entails that the BIOLOGICAL_PROCESS node is a microbe**.

`CausalNodeTypeEnum` has no organism member, so **no causal-graph edge can ever
satisfy that domain**. Every one of the 366 is a false entailment.

This is the sibling of the problem v8 solved. There, the corpus had no
range-correct relation whose *object* was a trait; here it has no domain-correct
relation whose *subject* is a causal-graph node.

## Scope

| Scope | Source | # rows | Lift status |
|---|---|---:|---|
| A (synthetic trait classes) | records whose `identifier:` starts with `traitmech:` | 0 | out of scope — 120 exist, tracked in [#319](https://github.com/CultureBotAI/TraitMech/issues/319) |
| B (causal-graph predicates) | the 366 microbe-domain edges (#301) | **14 predicates / 210 edges** | included |
| C (controlled vocabularies) | already lifted in v1 (`CausalNodeTypeEnum`) | 0 | already covered |

Total property rows in v9: **14**. Thirteen cover 200 of the 366 edges in #301; the
fourteenth (`encodes`) is unrelated to #301 and replaces a local coinage on 10 further
edges (#342). No class rows; v1 already proposed the domain
class (`METPO:1007401` *trait causal node*).

### Only 200 of the 366 need new terms

The 366 were triaged against what already exists before anything was minted.
165 of them (45%) already have a home, and only the remainder is proposed here:

| Family | Edges | Target | New term? |
|---|---:|---|---|
| A — any subject → **TRAIT** object | 62 | `METPO:2007700` *confers* (v8) | no — already proposed |
| B — **activity** subject `produces` X | 103 | `RO:0002234` *has output* | no — upstream, domain-correct |
| C+D+E — everything else | **200** | this cohort | **yes, 13 terms** |
| — one inverse-direction edge, deliberately uncovered | 1 | needs its own decision ([#327](https://github.com/CultureBotAI/TraitMech/issues/327)) | no |
| | **366** | | |

**Family B is the important negative result.** biolink gives `has output`
`domain: biological process or activity`
(`data/raw/biolink-model.yaml`), which a `BIOLOGICAL_PROCESS`, `PATHWAY` or
`MOLECULAR_FUNCTION` subject satisfies. Those 103 edges therefore need no METPO
term at all, and this cohort deliberately does not propose one that would
compete with `has output`. Only the subjects RO cannot cover — proteins, traits,
chemicals, states — fall through to `METPO:2007800`.

## Predicate proposals

All 13 take `domain = range = METPO:1007401` (*trait causal node*), the v1
convention that sidesteps the microbe domain.

| ID | Label | Edges | Mirrors |
|---|---|---:|---|
| `METPO:2007800` | produces | 84 | `METPO:2000202` |
| `METPO:2007801` | does not produce | 1 | `METPO:2000222` |
| `METPO:2007802` | reduces | 30 | `METPO:2000017` |
| `METPO:2007803` | oxidizes | 21 | `METPO:2000016` |
| `METPO:2007804` | exports | 14 | `METPO:2000209` |
| `METPO:2007805` | imports | 12 | `METPO:2000208` |
| `METPO:2007806` | has carbon source | 12 | `METPO:2000006` |
| `METPO:2007807` | has energy source | 8 | `METPO:2000010` |
| `METPO:2007808` | hydrolyzes | 6 | `METPO:2000013` |
| `METPO:2007809` | degrades | 6 | `METPO:2000007` |
| `METPO:2007810` | accumulates | 3 | `METPO:2000210` |
| `METPO:2007811` | disproportionates | 2 | `METPO:2000200` |
| `METPO:2007812` | transports | 1 | `METPO:2000207` |
| `METPO:2007813` | encodes | 10 | — (replaces the local coinage `biolink:encodes`) |
| | | **210** | |

### Why mirror rather than collapse

The obvious economy would be one catalytic relation covering
oxidizes/reduces/hydrolyzes/degrades/disproportionates, and one transport
relation covering imports/exports/transports. **That is exactly the mistake
[#303](https://github.com/CultureBotAI/TraitMech/issues/303) documents.**
Collapsing `uses as electron donor` and `uses as electron acceptor` onto a single
`enables` cost the donor/acceptor distinction, and recovering it took a further
proposal and a corpus migration. `oxidizes` and `reduces` are opposite directions
of electron flow; merging them would discard the same class of information for
the same reason. Each mirrored term therefore keeps its source predicate's exact
sense, and the only thing that changes is the domain.

### Why mirror rather than ask METPO to relax the domain

Removing or broadening `METPO:2000001`'s `rdfs:domain` would fix all 366 edges
with no corpus change at all, and it was seriously considered — #301 raises it as
the case where changing the ontology may beat changing the data.

It is rejected because the domain is **correct for the terms' original use**. At
the assertion site — `<organism> METPO:2000006 <CHEBI:17234>` — the subject
really is a microbe, and that is what the `domain:` is there to say. kg-microbe
consumes them that way. Relaxing it would weaken a true axiom for every existing
consumer in order to serve a second use case with different subjects. Two
sibling terms with explicit `skos:closeMatch` mappings keep both claims exact.

### Relabelling: `uses as X source` → `has X source`

`METPO:2007806`/`2007807` are the only two rows whose label departs from their
source. `uses as carbon source` reads from the organism's side; with a trait as
the subject, "the trait *uses*" is wrong — the trait *has* a carbon source. This
matches the v8 pair `has electron donor`/`has electron acceptor`, which made the
same move for the same reason.

### Pairing

`produces` (`METPO:2007800`) and `does not produce` (`METPO:2007801`) are a
genuine positive/negative pair on one axis and follow the kg-microbe paired
convention. The remaining 11 are siblings, not pairs.

### Hierarchy

The 12-column properties template carries no parent column, so all 13 land under
`owl:topObjectProperty`, as in v2 and v6. Conceptually they form a causal-graph
counterpart to the `METPO:2000001` subtree, and upstream may prefer to place them
under a shared parent such as *"causal-graph chemical interaction"* with
`domain: METPO:1007401`. Flagged here rather than encoded, since the template
cannot express it.

## ID space and subset

- Predicates: **`METPO:2007800`–`METPO:2007813`**. Block verified free: v2 holds
  `2007400`–`2007407`, v4 `2007500`, v6 `2007600`–`2007603`, v8
  `2007700`–`2007702`, and `grep` finds no `METPO:20078` in any other cohort or
  in `data/raw/metpo.owl` (highest real minted property: `METPO:2000516`).
- No class rows, so no `1007xxx` allocation. No collision with CommunityMech v1
  (`1007100`–`1007220`) or TraitMech v1/v3/v5/v7.
- Subset tag: **`metpo_traitmech_2026_12`** (v8 used `metpo_traitmech_2026_11`;
  tags are sequential per cohort, not calendar months).

## Files

| File | Rows (excl. 2 header rows) |
|---|---:|
| `metpo_proposal_properties_robot.tsv` | 13 |
| `metpo_proposal_mappings.sssom.tsv` | 13 |
| `proposal.md` | — |

## Verification

- `just verify-proposal metpo_traitmech_v9` — see PR body.
- `just robot-validate-proposal metpo_traitmech_v9` — see PR body.
- Column counts 12/12 on every properties row, 9/9 on every SSSOM row.
- `definition_source` hygiene ([#83](https://github.com/CultureBotAI/TraitMech/issues/83)):
  all 13 cite a TraitMech curation event, and **each anchor was checked to be a
  real `graph_id` carrying a real edge of that predicate**. Note the claim is not
  that every anchor has a *non-activity* subject: `METPO:2007812` (transports) has
  exactly one corpus edge and its subject is a `PATHWAY`. The term is still needed —
  `RO:0002234` is a production relation and covers no transport sense at all. Cross-ontology alignment lives in `xrefs` + the SSSOM file as
  `skos:closeMatch`, never in column 4.
- Edge counts computed by walking the `subPropertyOf` closure to `METPO:2000001`
  in `data/raw/metpo.owl` and matching against the corpus; the 62/103/200/1 split
  sums to the 366 independently reported by
  `reports/predicate_domain_audit.tsv`.

## Upstream path

Submit both TSVs to [berkeleybop/metpo](https://github.com/berkeleybop/metpo),
consolidated into issue #535 with v1–v8. `2007800`–`2007812` are TraitMech
placeholders; METPO maintainers mint the real IDs.

## Round-trip plan

The corpus migration follows as **two** PRs, deliberately not one — #301 warns a
single 366-edge sweep would be unreviewable, and the 164-edge v8 migration needed
three review rounds:

1. **Mechanical first (185 edges)** — family A (62 → `confers`, already minted),
   family B (103 → `RO:0002234`), and the two role predicates
   (`has carbon source` 12 + `has energy source` 8 = 20). Targets already decided or
   upstream. Expected: `MICROBE_DOMAIN_ON_NONORGANISM` **366 → 181**.
2. **Then the rest (181 edges)** — the enzyme, transport and remaining `produces`
   families onto the other 11 terms here (180 edges, = 200 − 20), plus the single
   inverse-direction `is hydrolyzed to` edge once #327 decides its direction.
   Expected: **181 → 0**, retiring the defect class.

Gate each with `subject_types`/`object_types` on the
`mappings/predicate_grounding.tsv` rows, as v8 did, so the grounding tool refuses
a shape the term does not admit.

After upstream mints real IDs: update `data/raw/metpo.owl`, re-seed, and swap the
placeholder CURIEs in `mappings/predicate_grounding.tsv` and `data/traits/**`.

## Change log

- v9, 2026-08: propose 13 causal-graph counterparts of the `METPO:2000001`
  subtree (`METPO:2007800`–`METPO:2007812`), covering 200 of the 366 edges in
  #301. The other 165 are routed to `METPO:2007700` (v8) and `RO:0002234` rather
  than to new terms. No corpus edges migrated in this cohort.
