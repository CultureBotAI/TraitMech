# METPO ROBOT Template Proposal — FAPROTAX Metabolic Strategies (v11, 2026-08)

> **Upstream submission:** to be consolidated into
> [berkeleybop/metpo#535](https://github.com/berkeleybop/metpo/issues/535) alongside
> the v1–v10 cohorts — requesting real METPO IDs for this cohort.

## Context

kg-microbe carries 5,224 microbedecoder labels it could not ground
(`kg-microbe#650`). TraitMech#453 triaged the 449 of them typed
`biolink:PhenotypicQuality` / `biolink:BiologicalProcess`. Most turned out not to be
TraitMech's problem — 137 are chemicals that MediaIngredientMech already resolves
(kg-microbe#837), 18 are ingest artifacts (kg-microbe#838), 40 enzyme activities were
grounded to GO/EC in TraitMech#454, and 3 resolved to existing traits as synonyms in
TraitMech#462.

**This cohort is what is left:** FAPROTAX metabolic strategies that name a real
microbial capability for which METPO has no class.

## ID block

`METPO:1008800`–`METPO:1008814` (classes). No predicates proposed.

The highest placeholder in use across cohorts v1–v10 is `METPO:1007721` (classes) and
`METPO:2007900` (predicates), so the next contiguous class block would be
`METPO:1007800`. **This cohort deliberately starts 1,000 above that, at
`METPO:1008800`**, to leave room for upstream minting and for in-flight cohorts to
land without collision. Per `proposals/README.md`, never reuse a block from a merged
cohort; this one is recorded here as required.

Collision-checked against `data/raw/metpo.owl` (357 classes parsed via XML, not
regex — see "A parsing failure worth recording" below), all prior proposal cohorts,
and `data/traits/`. No overlap.

Subset tag: `metpo_traitmech_2026_14`.

## Scope

| Scope | Rows | Why it belongs in METPO |
|---|---:|---|
| A — synthetic trait class lift | 0 | no `traitmech:` identifiers were minted for these; they have no local record yet |
| B — causal-graph predicate lift | 0 | nothing here is a relation |
| **New metabolic-capability classes** | **15** | FAPROTAX strategies with no METPO home, already loaded as synonyms elsewhere in METPO's trophic-type branch |

## The two highest-frequency labels are NOT proposed here

This is the most important result of the review, and it inverts the premise the
cohort started from.

`chemoheterotrophy` (**10,493 occurrences**, the single highest-frequency unmapped
label in the entire microbedecoder file) and `aerobic_chemoheterotrophy` (**7,875**)
were the motivating candidates. Neither is a new term:

```
METPO:1000636  chemoheterotrophic
       synonyms: aerobic_chemo_heterotrophy, chemoheterotroph
```

`METPO:1000636` already exists **and already carries a FAPROTAX-style synonym for the
second label** — `aerobic_chemo_heterotrophy` differs from
`aerobic_chemoheterotrophy` only in underscore placement.

An exact-match check missed this, because `chemoheterotrophy` ≠ `chemoheterotrophic`
under normalisation. Only reading METPO's trophic-type branch surfaced it.

**Requested instead: two synonym additions to an existing class.**

| target | add as `oboInOwl:hasExactSynonym` | occurrences |
|---|---|---:|
| `METPO:1000636` chemoheterotrophic | `chemoheterotrophy` | 10,493 |
| `METPO:1000636` chemoheterotrophic | `aerobic_chemoheterotrophy` | 7,875 |

These are not in the ROBOT template, which mints new terms; they are edits to a
merged class and need a maintainer to apply them. 18,368 occurrences resolve on the
strength of two strings.

**This is METPO's own established pattern, not an invention.** METPO's trophic-type
branch already ingests FAPROTAX labels verbatim as synonyms:

```
METPO:1000656 photoautotrophic  — photoautotrophy, anoxygenic_photoautotrophy,
                                  anoxygenic_photoautotrophy_sulfur_oxidation, …
METPO:1000644 heterotrophic     — aerobic_heterotrophy
METPO:1000660 phototrophic      — aerobic_anoxygenic_phototrophy
METPO:1000651 methylotrophic    — methylotrophy
```

So the underscored FAPROTAX spelling is already an accepted synonym form here, which
is why the 15 proposed classes below carry theirs the same way.

## The 15 proposed classes

Three families, each hung off a parent METPO already has.

### Anaerobic respiration by terminal electron acceptor — parent `METPO:1000802`

METPO has `Aerobic respiration` (`METPO:1000801`) and `Anaerobic respiration`
(`METPO:1000802`) but nothing distinguishing anaerobic respiration by what the
electrons land on, which is precisely what FAPROTAX records.

| ID | label | parent |
|---|---|---|
| `METPO:1008800` | nitrogen respiration | `METPO:1000802` |
| `METPO:1008801` | nitrate respiration | `METPO:1008800` |
| `METPO:1008802` | nitrite respiration | `METPO:1008800` |
| `METPO:1008803` | respiration of sulfur compounds | `METPO:1000802` |
| `METPO:1008804` | sulfur respiration | `METPO:1008803` |
| `METPO:1008805` | thiosulfate respiration | `METPO:1008803` |

The two-level shape is FAPROTAX's own: `nitrogen_respiration` is the union of the
nitrate and nitrite cases, `respiration_of_sulfur_compounds` the union of the sulfur
and thiosulfate cases. Flattening them would lose the generalisation an annotator
actually asserted when they could not specify the acceptor.

### Methanogenesis — parent `METPO:1000844`

| ID | label | parent |
|---|---|---|
| `METPO:1008806` | hydrogenotrophic methanogenesis | `METPO:1000844` |

**Two FAPROTAX labels collapse into one class here.**
`hydrogenotrophic_methanogenesis` (144) and `methanogenesis_by_CO2_reduction_with_H2`
(140) name the same process from opposite ends — the electron donor and the carbon
substrate. Proposing both would put a synonym pair in the hierarchy as siblings.

### Degradation and oxidation capabilities — parent `METPO:1000060`

| ID | label | parent |
|---|---|---|
| `METPO:1008807` | hydrocarbon degradation | `METPO:1000060` |
| `METPO:1008808` | aromatic hydrocarbon degradation | `METPO:1008807` |
| `METPO:1008809` | aromatic compound degradation | `METPO:1000060` |
| `METPO:1008810` | xylanolysis | `METPO:1000060` |
| `METPO:1008811` | dark hydrogen oxidation | `METPO:1000060` |
| `METPO:1008812` | dark oxidation of sulfur compounds | `METPO:1000060` |
| `METPO:1008813` | methanol oxidation | `METPO:1000060` |
| `METPO:1008814` | nitrate reduction | `METPO:1000060` |

These hang off `METPO:1000060 metabolism`, not `METPO:1000630 biological process`.
The first draft used the latter and that was wrong (#468): `METPO:1000630` has
exactly **one** child, `metabolism`, and every real process in METPO —
`respiration`, `Methanogenesis`, `Acetogenesis`, `Oxidative phosphorylation`,
`Disproportionation` — sits below it. Parenting to `1000630` would have made these
seven siblings of `metabolism` itself, a level above the processes they belong with.
The definitions take `metabolism` as their genus to match, which is how METPO's
existing children of that class are written ("A metabolism in which methane is
produced…").

### Two second parents, both left for a maintainer

`SC %` carries one parent. Two rows genuinely have a second, and both are recorded
here rather than silently dropped:

- **`aromatic hydrocarbon degradation`** is a child of both `hydrocarbon degradation`
  (asserted) and `aromatic compound degradation` — an aromatic hydrocarbon is both.
- **`nitrate respiration`** is a child of both `nitrogen respiration` (asserted, by
  mechanism) and `nitrate reduction` (by chemistry — respiratory reduction of nitrate
  is still reduction of nitrate). The same holds for `nitrite respiration`. This one
  was missed in the first draft (#469), which flagged only the aromatic case and so
  implied the nitrogen case had been considered and rejected.

`nitrate reduction` is deliberately **not** placed *under* `nitrate respiration`.
FAPROTAX separates them because nitrate reduction covers assimilatory reduction into
biomass as well as respiratory reduction; making it a child would assert every nitrate
reducer conserves energy that way. The relationship runs the other direction, which is
exactly the second parent noted above.

`degradation` is METPO's existing verb here — `METPO:2000007 degrades` — so the
labels use it rather than GO's "catabolic process", with the GO form recorded as a
mapping instead.

## Cross-ontology mappings

`metpo_proposal_mappings.sssom.tsv` carries 5 rows: 4 `skos:exactMatch` to GO and 1
`skos:closeMatch`. Emitted only where a GO term genuinely denotes the same process —
per the skill's rule, a cross-ontology equivalent is a mapping, not a
`definition_source`.

The closeMatch is `dark oxidation of sulfur compounds` → `GO:0019417 sulfur
oxidation`: GO admits phototrophic sulfur oxidation, which the FAPROTAX "dark"
qualifier exists to exclude, and GO has no light-independent sibling to point at.

**Ten of the fifteen get no mapping**, and that is a finding rather than an omission.
The anaerobic-respiration-by-acceptor family has no GO equivalents — searching
"nitrate respiration" returns `GO:0008940 nitrate reductase activity`, an enzyme
function, not the respiratory process. GO models the catalysis; FAPROTAX models the
organism-level strategy. That gap is the substantive argument for these six classes
existing in METPO at all.

`aromatic compound degradation` has no mapping for a different reason:
`GO:0019439 aromatic compound catabolic process` is **obsolete**.

## Verification

- `just verify-proposal metpo_traitmech_v11` — **PASS, 0 failures.**
- **Collision check** — `METPO:1008800`–`1008814` are unused across `metpo.owl`,
  all ten prior cohorts, and `data/traits/`.
- **Every parent read out of METPO's own hierarchy**, not assumed. That is what
  caught #468 — seven rows had been hung off `biological process`, which turns out to
  have a single child.
- **Every GO id round-tripped by identifier**, not accepted from a keyword search.
  That caught `GO:0019439` being obsolete; the same discipline caught five obsolete
  ids in TraitMech#454.
- **Every proposed label checked against METPO's 357 classes and 611 label+synonym
  strings**, which is what surfaced `METPO:1000636` and removed the cohort's two
  largest candidates.
- Occurrence counts in the `traits_addressed` column come from
  `kg-microbe/mappings/microbedecoder_unmapped_labels_to_curate.tsv`.

### A parsing failure worth recording

The first collision check reported all 23 candidates ABSENT — from an index of **zero
terms**. `metpo.owl` identifies terms as `https://w3id.org/metpo/1000636`, not
`METPO_1000636`, so a regex written for the OBO PURL form matched nothing and every
lookup returned "not found".

A clean "all absent" from a dead parser is indistinguishable from a real result, and
it points the wrong way: it would have proposed `chemoheterotrophy` as a new class
when METPO has had it all along. The check now parses the XML properly and prints the
index size so an empty index cannot pass silently.

## Upstream path

1. File/append to berkeleybop/metpo#535 with `metpo_proposal_classes_robot.tsv`.
2. Request the two `METPO:1000636` synonym additions in the same issue — they are
   the highest-value part of this cohort by occurrence count and need no new IDs.
3. On mint, replace the `METPO:1008800+` placeholders with the assigned IDs.
4. Re-seed `data/raw/metpo.owl` and create the corresponding TraitMech trait records.

## What is still unresolved after this cohort

The host-association labels — `animal_parasites_or_symbionts` (802),
`human_associated` (424), `intracellular_parasites` (169), `mammal_gut` (151),
`human_gut` (150). METPO has `pathogenic to host` (`METPO:1004000`), `animal
pathogen`, `plant pathogen`, `human pathogen`, all framed as **pathogenicity**.
FAPROTAX's terms are **habitat association**, which is a different axis — a gut
commensal is host-associated and not a pathogen. Proposing them under the pathogen
branch would assert harm that FAPROTAX does not claim, and METPO has no
host-association branch to hang them from. That needs a modelling decision from METPO
maintainers before a cohort can be written, so it is deliberately left out here.

Also excluded: `photosynthetic_cyanobacteria` (5,221), which names a taxon rather
than a trait, and `polar` (445), which is ambiguous between polar flagellation, polar
lipids, and polar habitat, with nothing in the source column to disambiguate it.
