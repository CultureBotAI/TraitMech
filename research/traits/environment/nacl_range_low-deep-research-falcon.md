---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T01:50:44.811170'
end_time: '2026-08-04T02:01:21.446712'
duration_seconds: 636.64
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: NaCl range low
  trait_identifier: METPO:1000469
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: nacl_range_low
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A NaCl range phenotype in which the upper bound of growth-supporting
    NaCl concentration is at or below approximately 1% (w/v), characteristic of non-halophilic
    or halotolerant organisms.
  parent_traits: METPO:1000334
  synonyms: Halotolerant, Non-halophile, NaR_<=1
  evidence_summary: "DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review\
    \ supports growth limited to \u2264 ~1% NaCl as the non-halophilic / halotolerant\
    \ range.)"
  causal_graph_summary: 'nacl_range_low_non_halophile: 12 nodes, 7 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 34
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** NaCl range low
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000469
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl range phenotype in which the upper bound of growth-supporting NaCl concentration is at or below approximately 1% (w/v), characteristic of non-halophilic or halotolerant organisms.
- **Parent traits:** METPO:1000334
- **Synonyms:** Halotolerant, Non-halophile, NaR_<=1
- **Existing evidence:** DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review supports growth limited to ≤ ~1% NaCl as the non-halophilic / halotolerant range.)
- **Existing causal graph summary:** nacl_range_low_non_halophile: 12 nodes, 7 edges

## Research Objective

Research the microbial trait **NaCl range low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_range_low.yaml`.

## Required Findings

### 1. Trait Scope
- Clarify what phenotype, physiological capacity, environmental preference, or assay-observed
  property the trait represents.
- Identify boundary cases and distinguish the trait from nearby traits.

### 2. Causal Graph Entities
- Pathways and metabolic modules.
- Environmental factors and experimental factors.
- Genes, proteins, enzymes, transporters, and complexes.
- Chemicals, electron donors, electron acceptors, nutrients, metabolites, and inhibitors.
- Organelles, cellular localizations, molecular functions, and biological processes.

### 3. Evidence-Backed Edges
- Propose causal edges as subject-predicate-object triples.
- For every proposed edge, provide a reference, a short supporting quote/snippet, and notes
  explaining how the source supports the edge.
- Prefer DOI references. Use PMID only when a DOI is not available.
- Mark weak, taxon-specific, assay-specific, or inferred claims as uncertain.

### 4. Ontology Grounding
- Suggest CURIEs where available: METPO, GO, CHEBI, ENVO, NCBITaxon, EC, UniProt, Rhea,
  KEGG, MetaCyc, or other stable identifiers.
- Do not invent identifiers. Label-only candidate nodes are acceptable when grounding is unclear.

## Output Format

Return a curation-focused report with:
- A short scope summary.
- Candidate nodes grouped by type.
- Candidate causal edges in a table with reference, snippet, and notes.
- DOI-first bibliography.
- Warnings for claims that should not yet be curated into TraitMech.


## Output

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** NaCl range low
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000469
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl range phenotype in which the upper bound of growth-supporting NaCl concentration is at or below approximately 1% (w/v), characteristic of non-halophilic or halotolerant organisms.
- **Parent traits:** METPO:1000334
- **Synonyms:** Halotolerant, Non-halophile, NaR_<=1
- **Existing evidence:** DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review supports growth limited to ≤ ~1% NaCl as the non-halophilic / halotolerant range.)
- **Existing causal graph summary:** nacl_range_low_non_halophile: 12 nodes, 7 edges

## Research Objective

Research the microbial trait **NaCl range low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_range_low.yaml`.

## Required Findings

### 1. Trait Scope
- Clarify what phenotype, physiological capacity, environmental preference, or assay-observed
  property the trait represents.
- Identify boundary cases and distinguish the trait from nearby traits.

### 2. Causal Graph Entities
- Pathways and metabolic modules.
- Environmental factors and experimental factors.
- Genes, proteins, enzymes, transporters, and complexes.
- Chemicals, electron donors, electron acceptors, nutrients, metabolites, and inhibitors.
- Organelles, cellular localizations, molecular functions, and biological processes.

### 3. Evidence-Backed Edges
- Propose causal edges as subject-predicate-object triples.
- For every proposed edge, provide a reference, a short supporting quote/snippet, and notes
  explaining how the source supports the edge.
- Prefer DOI references. Use PMID only when a DOI is not available.
- Mark weak, taxon-specific, assay-specific, or inferred claims as uncertain.

### 4. Ontology Grounding
- Suggest CURIEs where available: METPO, GO, CHEBI, ENVO, NCBITaxon, EC, UniProt, Rhea,
  KEGG, MetaCyc, or other stable identifiers.
- Do not invent identifiers. Label-only candidate nodes are acceptable when grounding is unclear.

## Output Format

Return a curation-focused report with:
- A short scope summary.
- Candidate nodes grouped by type.
- Candidate causal edges in a table with reference, snippet, and notes.
- DOI-first bibliography.
- Warnings for claims that should not yet be curated into TraitMech.


# Curation-focused research report: NaCl range low

## Executive assessment

**Trait:** NaCl range low  
**Identifier:** `METPO:1000469`  
**Parent:** `METPO:1000334`

This trait should be treated as an **assay-observed upper growth boundary**, not as a single conserved molecular mechanism. Operationally, an organism belongs in this class when growth is supported up to approximately **1% (w/v) NaCl** but not above that range under a stated medium, temperature, pH, inoculum, aeration, incubation time, and growth endpoint. One percent NaCl is approximately **10 g/L or 171 mM NaCl**. The supplied threshold is approximate, so measurements near it should retain the original concentration series and uncertainty.

The strongest mechanistic interpretation is that low-range organisms have insufficient capacity to offset the combined effects of elevated extracellular osmolarity and, potentially, Na⁺-specific ionic stress. High external osmolality drives water efflux, lowers hydration and turgor, and increases cytoplasmic crowding; microorganisms normally counter these effects through K⁺ homeostasis and accumulation of compatible solutes by synthesis or import. These are authoritative general mechanisms, but the available literature does **not** establish that every organism with a ≤1% maximum lacks any particular transporter or pathway (bremer2019responsesofmicroorganisms pages 3-5).

## 1. Scope and boundary cases

### Included phenotype

`METPO:1000469` represents the **upper bound of growth-supporting NaCl concentration**. Evidence should ideally report growth across a NaCl series containing concentrations below, at, and above 1% (w/v), with an explicit no-growth or strongly inhibited-growth endpoint above the boundary.

### Important distinctions

1. **Tolerance is not requirement.** A non-halophile can grow without added NaCl; a halophile may require salt. The trait records the upper growth boundary, not the minimum or optimum.
2. **Maximum is not optimum.** An organism may grow best near 0% NaCl yet retain weak growth at 1%, or grow best at 1% and fail above it. These should not be conflated.
3. **“Halotolerant” is broader than ≤1%.** Published usage often describes non-halophiles capable of tolerating concentrations far above 1%. Consequently, the supplied synonym “Halotolerant” is ambiguous and should not be used alone to infer `METPO:1000469`.
4. **NaCl stress is not identical to osmotic stress.** An isosmotic sucrose or sorbitol control separates general water-activity effects from Na⁺/Cl⁻ toxicity and ion-homeostasis effects.
5. **Growth is not survival.** Persistence or colony recovery after salt exposure does not prove active growth at that concentration.
6. **Chronic hyperosmotic growth is not hypoosmotic-shock survival.** Mechanosensitive channels chiefly protect cells when osmolarity suddenly falls; they are mechanistically adjacent but do not directly explain a low upper NaCl growth limit (bremer2019responsesofmicroorganisms pages 3-5, goszcz2025bacterialosmoprotectants—away pages 4-5).
7. **Medium composition matters.** Peptides, yeast extract, choline, glycine betaine, proline, ectoine, K⁺, Mg²⁺, pH buffers, and carbon source can shift the observed maximum by supplying osmoprotectants or changing ionic activity.

## 2. Candidate causal-graph nodes

### Trait and assay nodes

- NaCl range low — `METPO:1000469`
- Parent NaCl-range phenotype — `METPO:1000334`
- Growth at or below approximately 1% NaCl — label-only assay state
- Growth inhibition above approximately 1% NaCl — label-only assay outcome
- NaCl concentration series — label-only experimental factor
- Medium composition, temperature, pH, aeration, inoculum, incubation time, growth endpoint — label-only covariates

### Environmental and chemical nodes

- Sodium chloride — `CHEBI:26710`
- Sodium ion — `CHEBI:29101`
- Potassium ion — `CHEBI:29103`
- Glycine betaine — `CHEBI:17750`
- L-proline — `CHEBI:17203`
- L-glutamate — `CHEBI:30796`
- 4-aminobutanoate/GABA — `CHEBI:16865`
- Ectoine — `CHEBI:142654`
- Trehalose, choline, water, and chloride — use validated CHEBI mappings during implementation rather than assigning unverified identifiers here
- High external osmolality, reduced water activity, ionic stress — label-only candidate states

### Processes and physiological states

- Response to osmotic stress — `GO:0006970`
- Response to salt stress — `GO:0009651`
- Water efflux
- Loss of cellular hydration
- Reduced turgor
- Increased cytoplasmic molecular crowding
- Compatible-solute accumulation
- Potassium homeostasis
- Sodium extrusion
- Cytoplasmic pH homeostasis
- Hypoosmotic-shock response
- Cell growth and growth inhibition

The literature identifies water efflux, reduced turgor, hydration loss, and crowding as central consequences of an osmotic upshift, and compatible-solute accumulation as a primary countermeasure (bremer2019responsesofmicroorganisms pages 3-5).

### Genes, proteins, transporters, and modules

These should be represented with organism context rather than as universal identifiers:

- `ectABC` / EctA–EctB–EctC — ectoine biosynthesis
- `proBm1AC` engineered module — proline biosynthesis in the 2024 *Halomonas* experiment
- `putA` — proline catabolism
- `gadB` / GadB — glutamate decarboxylase; glutamate-to-GABA conversion
- `betA`, `betB` or `gbsAB` — choline oxidation/glycine-betaine synthesis, depending on taxon
- OpuA, OpuC, OpuD — glycine-betaine/compatible-solute import systems
- OpuE, ProP, ProU — proline or compatible-solute uptake systems, with substrate and taxon qualification
- Kdp, Ktr, Trk — potassium-uptake systems
- NhaA — Na⁺/H⁺ antiporter
- MscL and MscS-family mechanosensitive channels
- c-di-AMP signaling machinery — relevant chiefly to Gram-positive K⁺ and osmolyte transport; not universal

EctABC supports de novo ectoine synthesis from aspartate-derived intermediates; BetA/BetB supports two-step choline oxidation to glycine betaine; and ProU, OpuD, and related systems mediate osmotically regulated compatible-solute uptake in specific taxa (lichty2024compatiblesolutesare pages 19-23).

## 3. Candidate causal edges

The table distinguishes **core physiological edges** from **taxon-specific perturbation evidence**. Importantly, most perturbation experiments shift growth limits between 3% and 8% NaCl. They validate causal modules for salt tolerance but do not directly prove the cause of a ≤1% phenotype.

| # | Proposed subject–predicate–object triple | Evidence and supporting snippet | Curation note |
|---|---|---|---|
| 1 | High external osmolality **causes** water efflux | Review evidence: high external osmolality causes water to leave through the semipermeable cytoplasmic membrane (DOI: [10.1146/annurev-micro-020518-115504](https://doi.org/10.1146/annurev-micro-020518-115504), September 2019) (bremer2019responsesofmicroorganisms pages 3-5). | **Strong general edge.** NaCl is one osmolyte; use an isosmotic nonionic control before making the relation NaCl-specific. |
| 2 | Water efflux **decreases** cellular hydration and turgor | The same authoritative review links osmotic water movement to cellular hydration, molecular crowding, turgor, and integrity (bremer2019responsesofmicroorganisms pages 3-5). | **Strong general edge.** Suitable as an intermediate physiological mechanism. |
| 3 | Reduced hydration/turgor and increased crowding **inhibit** microbial growth | Compatible-solute importers counter “water efflux,” “a drop in turgor,” and excessive crowding and thereby foster growth under unfavorable osmotic conditions; this supports the inverse relation (bremer2019responsesofmicroorganisms pages 3-5). | **Moderate-to-strong general edge.** The precise causal contribution of each state may be difficult to separate experimentally. |
| 4 | Compatible-solute accumulation **counteracts** high-osmolality stress | Compatible solutes—including proline, glycine betaine, ectoine and trehalose—maintain osmotic potential and hydration without disrupting cellular biochemistry (bremer2019responsesofmicroorganisms pages 3-5). | **Strong general edge.** Do not imply that all taxa use every listed solute. |
| 5 | Compatible-solute accumulation **increases** salt-growth capacity | Osmolyte synthesis/import enables adjustment across salinity ranges; direct 2024 engineering studies independently support this direction (zou2024metabolicengineeringof pages 4-8, fan2024improvementinsalt pages 12-14, bremer2019responsesofmicroorganisms pages 3-5). | **Strong direction; taxon-dependent implementation.** This is an inverse determinant of `METPO:1000469`, not proof that low-range strains lack it. |
| 6 | `ectABC` **enables** ectoine biosynthesis | EctA, EctB and EctC catalyze sequential steps in ectoine synthesis (lichty2024compatiblesolutesare pages 19-23). | **Strong biochemical edge.** Ground individual enzymes only after selecting the taxon/reference sequence. |
| 7 | Ectoine biosynthesis **increases** NaCl growth capacity | In *Halomonas elongata*, the Δ`ectABC` KA1 strain was salt-sensitive and unable to grow at 6–7% NaCl, whereas wild type grew across 3%, 6%, 7%, and 8% NaCl in M63 medium with 4% glycerol (DOI: [10.1128/aem.01905-23](https://doi.org/10.1128/aem.01905-23), January 2024) (zou2024metabolicengineeringof pages 2-4, zou2024metabolicengineeringof pages 4-8). | **Strong, taxon/background-specific.** Concentrations are well above the target trait boundary. |
| 8 | `ectABC` deletion **decreases** maximum growth-supporting NaCl | Supporting snippet: the ectoine-deficient mutant “could not grow” at 6–7% NaCl, while wild type retained growth (zou2024metabolicengineeringof pages 2-4, zou2024metabolicengineeringof pages 4-8). | **Direct perturbation edge.** Safe in a *H. elongata*-specific subgraph; not universal. |
| 9 | Glutamate overproduction **increases** intracellular glutamate | In the GOP suppressor, glutamate rose from **25.58 ± 1.94 μmol/g cell fresh weight at 3% NaCl** to **32.42 ± 2.27 μmol/g at 7% NaCl** (zou2024metabolicengineeringof pages 4-8). | **Strong quantitative edge** for this strain. |
| 10 | Intracellular glutamate accumulation **partially restores** salt-growth capacity in an ectoine-deficient strain | The GOP strain restored growth to 6–7% NaCl but failed at 8%; the authors interpret glutamate as the replacement osmolyte (zou2024metabolicengineeringof pages 4-8). | **Moderate-to-strong, taxon-specific.** “Partially” is important. |
| 11 | Excess glutamate accumulation **perturbs** cytoplasmic pH homeostasis | The study proposes that glutamate acidity limits further accumulation and contributes to failure at 8% NaCl (zou2024metabolicengineeringof pages 4-8, zou2024metabolicengineeringof pages 2-4). | **Uncertain/inferred.** Do not curate as established without direct intracellular-pH measurements. |
| 12 | GadB **converts** glutamate to GABA | The engineered broad-pH-range GadB was introduced specifically to decarboxylate glutamate to GABA (zou2024metabolicengineeringof pages 2-4). | **Strong biochemical edge.** Enzyme identifier should be sequence/taxon-specific. |
| 13 | Salt-inducible GadB expression **increases** GABA accumulation | The GOP-Gad strain accumulated GABA as a major osmolyte, reaching **176.94 μmol/g cell dry weight at 7% NaCl** (zou2024metabolicengineeringof pages 4-8, zou2024metabolicengineeringof pages 2-4). | **Strong engineering edge.** Note the dry-weight unit; do not compare directly with fresh-weight glutamate values. |
| 14 | GABA accumulation **increases** salt tolerance | GOP-Gad showed higher tolerance than the glutamate-overproducing parent (DOI: [10.1128/aem.01905-23](https://doi.org/10.1128/aem.01905-23)) (zou2024metabolicengineeringof pages 4-8, zou2024metabolicengineeringof pages 2-4). | **Strong within this engineered background.** Not evidence that GABA normally controls low-range phenotypes. |
| 15 | Feedback-insensitive proline synthesis plus `putA` deletion **increases** proline accumulation | A 2024 *H. elongata* strain carrying engineered `proBm1AC` and Δ`putA` accumulated **353.1 ± 40.5 μmol proline/g cell fresh weight** (DOI: [10.1128/aem.01195-24](https://doi.org/10.1128/aem.01195-24), September 2024). | **Strong recent engineering evidence.** This quantitative result comes from the paper abstract retrieved in the search corpus. |
| 16 | Proline accumulation **increases** maximum growth-supporting NaCl | The ectoine-deficient parent did not grow above 4% NaCl, whereas the engineered proline-producing strain thrived at 8% NaCl (DOI above). | **Strong, taxon-specific boundary control.** Indirect for `METPO:1000469`. |
| 17 | `betB` activity **promotes** glycine-betaine synthesis/accumulation | In *Pseudomonas putida* KT2440, `betB` encodes betaine-aldehyde dehydrogenase and its overexpression improved the 4% NaCl growth profile (DOI: [10.3390/biology13060404](https://doi.org/10.3390/biology13060404), June 2024) (fan2024improvementinsalt pages 12-14). | **Strong for the engineered strain.** Substrate availability and the upstream oxidation step matter. |
| 18 | NhaA Na⁺/H⁺ antiport **increases** NaCl tolerance | Heterologous *E. coli* `nhaA` significantly improved KT2440 growth at 4% NaCl (fan2024improvementinsalt pages 12-14). | **Strong engineering evidence**, but protein localization, pH and proton motive force should be modeled if the graph supports them. |
| 19 | NhaA expression plus `betB` overexpression **synergistically increases** maximum NaCl tolerance | Co-expression raised the KT2440 maximum from **4% to 5% (w/v) NaCl**; adding betaine and proline extended tolerance to **6%** (fan2024improvementinsalt pages 12-14). | **Strong combined-intervention edge.** Better modeled as two convergent mechanisms than a universal direct interaction. |
| 20 | Potassium uptake **supports** early osmotic adjustment | Reviews report rapid K⁺ uptake after osmotic upshift, often accompanied by glutamate accumulation; Trk is important for K⁺ accumulation and hyperosmotic growth in *Sinorhizobium meliloti* (goszcz2025bacterialosmoprotectants—away pages 5-5). | **Moderate, taxon-dependent.** Sustained high K⁺ may be cytotoxic, and many organisms later replace inorganic ions with compatible solutes. |
| 21 | MscL/MscS-family channel opening **causes** solute release during hypoosmotic shock | Mechanosensitive channels rapidly release organic and inorganic solutes to prevent rupture when external osmolarity falls (bremer2019responsesofmicroorganisms pages 3-5, goszcz2025bacterialosmoprotectants—away pages 4-5). | **Strong adjacent edge.** Place in a hypoosmotic-recovery branch, not as a direct cause of low high-salt tolerance. |
| 22 | Mechanosensitive-channel function **increases** hypoosmotic survival | In *H. elongata*, deletion of all four `mscS` genes rendered the mutant unable to cope with hypoosmotic shock (DOI: [10.1007/s00792-020-01168-y](https://doi.org/10.1007/s00792-020-01168-y), April 2020). | **Strong, taxon-specific**, but outside the primary chronic-NaCl phenotype. |
| 23 | Insufficient osmoadaptation capacity **contributes to** `METPO:1000469` | The direction is consistent with all reviewed and perturbational evidence: increasing compatible-solute synthesis/import or Na⁺ extrusion raises salt-growth ceilings (zou2024metabolicengineeringof pages 4-8, fan2024improvementinsalt pages 12-14, bremer2019responsesofmicroorganisms pages 3-5). | **Uncertain trait-level synthesis.** Retain as a high-level hypothesis, not a fully established direct edge. |

A compact evidence classification is provided below.

| candidate edge | evidence class | organism/assay | quantitative result | confidence/caveat |
|---|---|---|---|---|
| high external NaCl/osmolality -> water efflux, reduced turgor, increased crowding -> impaired growth | general inverse mechanism | Broad bacterial osmotic-stress physiology review | Review describes high external osmolality causing water efflux across the cytoplasmic membrane; compatible solutes counteract loss of hydration and turgor (bremer2019responsesofmicroorganisms pages 3-5) | High confidence for general mechanism; not direct evidence for the <=1% upper-bound trait |
| compatible-solute accumulation -> improved osmotic growth | general inverse mechanism | Broad bacterial osmotic-stress physiology review | Compatible solutes such as proline, glycine betaine, ectoine, trehalose, glucosylglycerol support growth under osmotically unfavorable conditions (bremer2019responsesofmicroorganisms pages 3-5) | High confidence general mechanism; taxon and solute usage vary |
| ectABC deletion -> reduced salt growth | boundary/control | *Halomonas elongata* KA1 (ΔectABC) in minimal medium with NaCl gradient | ΔectABC mutant “only grows well in minimal medium containing up to 3% NaCl”; cannot grow at 6–7% NaCl, whereas wild type grows at 3%, 6%, 7%, 8% NaCl (zou2024metabolicengineeringof pages 4-8, zou2024metabolicengineeringof pages 2-4) | Strong direct perturbation evidence for salt-growth capacity, but at much higher NaCl than the <=1% trait |
| glutamate accumulation -> partial restoration of salt growth in ectoine-deficient background | boundary/control | *H. elongata* GOP suppressor mutant under salt stress | GOP restored growth to 6–7% NaCl; intracellular glutamate increased from 25.58 ± 1.94 to 32.42 ± 2.27 μmol/g cell fresh weight between 3% and 7% NaCl; still failed at 8% NaCl (zou2024metabolicengineeringof pages 4-8) | Strong for this taxon/background; not direct for <=1% ceiling |
| GadB-mediated glutamate -> GABA conversion -> increased salt tolerance | boundary/control | *H. elongata* GOP-Gad engineered strain with salt-inducible *gadB* mutant | GOP-Gad accumulated GABA as major osmolyte and showed higher salt tolerance than GOP; reported GABA accumulation 176.94 μmol/g cell dry weight at 7% NaCl (zou2024metabolicengineeringof pages 4-8, zou2024metabolicengineeringof pages 2-4) | Strong engineering evidence; comparative growth gain is above low-NaCl range |
| engineered proline-biosynthesis module plus *putA* deletion -> proline accumulation -> higher NaCl growth maximum | boundary/control | *H. elongata* HN6 (ΔectABC::proBm1AC ΔputA) in minimal medium | Ectoine-deficient parent could not grow above 4% NaCl; engineered strain thrived at 8% NaCl and accumulated proline to 353.1 ± 40.5 μmol/g cell fresh weight (abstract data from retrieved paper) | Strong recent engineering result, but evidence is for expanded high-salt tolerance, not low-NaCl limitation |
| *betB* overexpression + heterologous *E. coli nhaA* -> increased NaCl tolerance | boundary/control | *Pseudomonas putida* KT2440 in minimal salts medium with 4–6% w/v NaCl | Wild type tolerated 4% NaCl; co-expression of *EcnhaA* and *betB* raised maximum tolerance to 5% NaCl; addition of betaine/proline increased tolerance to 6% NaCl (fan2024improvementinsalt pages 12-14) | Good recent engineering evidence for antiporter + compatible-solute synergy; not direct for <=1% trait |
| mechanosensitive channels -> release solutes and promote hypoosmotic survival | general inverse mechanism | Broad bacterial osmotic-stress review; *Halomonas elongata* channel-deletion study | Review: Msc channels rapidly release organic/inorganic solutes during hypoosmotic stress (bremer2019responsesofmicroorganisms pages 3-5); in *H. elongata*, deletion of four *mscS* genes made mutant unable to cope with hypoosmotic shock (paper summary from retrieval) | High confidence for hypoosmotic-shock survival; mechanism is adjacent but not explanatory for chronic low maximum NaCl growth |
| low maximum NaCl growth (<=1% w/v) likely reflects absence/insufficiency of broad osmoadaptation capacity | direct for <=1% trait (inferred) | Trait interpretation rather than single organism assay | No retrieved primary study directly perturbs a microbe from <=1% maximum to higher values while anchoring the phenotype definition itself (bremer2019responsesofmicroorganisms pages 3-5) | Low confidence for curation as a direct edge; should remain a scope-level inference until direct low-range evidence is found |


*Table: This table compiles compact curation-ready evidence relevant to METPO:1000469, separating direct low-range relevance from broader osmoadaptation mechanisms and higher-salt control experiments. It is useful for deciding which edges are safe to curate now and which remain indirect or taxon-specific.*

## 4. Recommended minimal TraitMech graph

For a conservative first version of `nacl_range_low.yaml`, the most defensible generic chain is:

1. `sodium chloride concentration above organism-specific tolerance`  
   **increases** → `external osmolality`
2. `external osmolality`  
   **causes** → `water efflux`
3. `water efflux`  
   **decreases** → `cellular hydration`
4. `water efflux`  
   **decreases** → `turgor pressure`
5. `decreased cellular hydration`  
   **increases** → `cytoplasmic molecular crowding`
6. `decreased turgor / increased crowding`  
   **inhibits** → `cell growth`
7. `cell-growth inhibition above approximately 1% NaCl`  
   **realizes** → `METPO:1000469`
8. `compatible-solute accumulation`  
   **counteracts** → `decreased cellular hydration`
9. `Na⁺ extrusion`  
   **decreases** → `intracellular sodium stress`
10. `insufficient compatible-solute accumulation or Na⁺ homeostasis`  
    **contributes to** → `growth inhibition above approximately 1% NaCl` **[uncertain]**

Taxon-specific branches for `ectABC`, Opu systems, `betB`, NhaA, Kdp/Ktr/Trk, or GadB should be added only when the organism being curated has direct genetic, biochemical, or expression-plus-phenotype evidence.

## 5. Recent developments and real-world applications

### 2024 mechanistic engineering

Two 2024 *H. elongata* studies provide unusually clear causal evidence that the identity and achievable concentration of an intracellular compatible solute can set a salt-growth boundary. Glutamate overproduction restored growth to 6–7% NaCl in an ectoine-deficient background, while conversion to GABA improved tolerance and yielded 176.94 μmol GABA/g dry biomass at 7% NaCl (zou2024metabolicengineeringof pages 4-8). A separate 2024 study replaced ectoine metabolism with engineered proline production; the strain accumulated 353.1 ± 40.5 μmol/g fresh biomass and grew at 8% NaCl.

Fan et al. combined ion homeostasis and osmolyte synthesis in *P. putida* KT2440. `EcnhaA` plus `betB` increased the maximum from 4% to 5% NaCl, and exogenous betaine/proline extended it to 6% (fan2024improvementinsalt pages 12-14). The engineered strain degraded **56.70% of benzoic acid** and **95.64% of protocatechuic acid** in 4% NaCl over 48 hours, whereas the parental strain showed no degradation under the same conditions. This is a direct real-world link between salt-tolerance engineering and saline-wastewater bioremediation (fan2024improvementinsalt pages 12-14).

### Applications

- **Saline bioremediation:** engineering NhaA and compatible-solute pathways can preserve aromatic-pollutant degradation in saline process streams (fan2024improvementinsalt pages 12-14).
- **Osmolyte biomanufacturing:** salt-responsive *Halomonas* platforms can produce GABA, proline, or ectoine while using high salinity as a selective process condition (zou2024metabolicengineeringof pages 4-8, zou2024metabolicengineeringof pages 2-4).
- **Low-salt fermentation design:** strains annotated with `METPO:1000469` may require low-salt media and careful control of salt-bearing feedstocks. Conversely, supplied betaine, proline, choline, or rich-medium components can mask the intrinsic phenotype.
- **Agriculture:** compatible-solute-producing bacteria are being investigated as inoculants for saline soils, but transfer from laboratory salt-growth assays to field efficacy remains incompletely established (goszcz2025bacterialosmoprotectants—away pages 5-5).

## 6. Curation warnings

1. **Do not curate “absence of `ectABC` causes `METPO:1000469`.”** The Δ`ectABC` *H. elongata* mutant still grew at approximately 3–4% NaCl, so it is not an example of the ≤1% trait (zou2024metabolicengineeringof pages 2-4, zou2024metabolicengineeringof pages 4-8).
2. **Do not make compatible-solute pathways universal.** Different bacteria and archaea use different solutes, transporters, regulation, and sometimes salt-in rather than salt-out strategies (goszcz2025bacterialosmoprotectants—away pages 5-5, bremer2019responsesofmicroorganisms pages 3-5).
3. **Do not use transcript induction alone as a causal edge.** For example, Kdp genes or an endogenous antiporter may be upregulated without overexpression increasing tolerance; perturbation and growth evidence are preferable (fan2024improvementinsalt pages 12-14).
4. **Do not equate `NaCl range low` with inability to osmoadapt.** A strain may possess functional osmoadaptation sufficient for mild stress but reach its physiological limit near 1% because of transport capacity, energetic cost, membrane properties, pH, nutrient limitation, or Na⁺ toxicity.
5. **Do not curate mechanosensitive channels as direct determinants of the upper NaCl limit** without direct chronic-growth evidence. Their best-established role is emergency solute release after hypoosmotic downshift (bremer2019responsesofmicroorganisms pages 3-5, goszcz2025bacterialosmoprotectants—away pages 4-5).
6. **Do not compare fresh-weight and dry-weight osmolyte measurements directly.** The glutamate values were reported per cell fresh weight, whereas the GABA value was reported per dry weight (zou2024metabolicengineeringof pages 4-8).
7. **Avoid threshold overprecision.** Approximately 1% is an ontology bin boundary, not a universal biological discontinuity. Record actual tested values and whether 1% was total or added NaCl.
8. **The existing citation DOI:10.1093/femsre/fuy009 should be checked manually.** It supports broad osmoadaptation concepts, but the retrieved evidence does not validate a universal ≤1% taxonomic definition from that source.
9. **Synonym warning:** “halotolerant” commonly includes organisms growing at much higher NaCl. It is not a safe stand-alone synonym for this narrow trait.
10. **Ontology identifiers should be validated against the project’s pinned ontology release** before YAML merge; gene-family nodes should remain label-only until an organism and sequence are specified.

## 7. DOI-first bibliography

1. Zou Z, Kaothien-Nakayama P, Ogawa-Iwamura J, Nakayama H. “Metabolic engineering of high-salinity-induced biosynthesis of γ-aminobutyric acid improves salt-stress tolerance in an ectoine-deficient *Halomonas elongata*.” *Applied and Environmental Microbiology* 90(1), **January 2024**. DOI: [10.1128/aem.01905-23](https://doi.org/10.1128/aem.01905-23) (zou2024metabolicengineeringof pages 4-8, zou2024metabolicengineeringof pages 2-4).
2. Khanh HC, Kaothien-Nakayama P, Zou Z, Nakayama H. “Metabolic pathway engineering of high-salinity-induced overproduction of L-proline improves high-salinity stress tolerance of an ectoine-deficient *Halomonas elongata*.” *Applied and Environmental Microbiology* 90(9), **September 2024**. DOI: [10.1128/aem.01195-24](https://doi.org/10.1128/aem.01195-24).
3. Fan M, Tan S, Wang W, Zhang X. “Improvement in Salt Tolerance Ability of *Pseudomonas putida* KT2440.” *Biology* 13:404, **June 2024**. DOI: [10.3390/biology13060404](https://doi.org/10.3390/biology13060404) (fan2024improvementinsalt pages 12-14).
4. Bruger EL et al. “Enhanced catabolism of glycine betaine and derivatives provides improved osmotic stress protection in *Methylorubrum extorquens* PA1.” *Applied and Environmental Microbiology* 90(7), **July 2024**. DOI: [10.1128/aem.00310-24](https://doi.org/10.1128/aem.00310-24).
5. Bremer E, Krämer R. “Responses of Microorganisms to Osmotic Stress.” *Annual Review of Microbiology* 73:313–334, **September 2019**. DOI: [10.1146/annurev-micro-020518-115504](https://doi.org/10.1146/annurev-micro-020518-115504) (bremer2019responsesofmicroorganisms pages 3-5).
6. Vandrich J et al. “Contribution of mechanosensitive channels to osmoadaptation and ectoine excretion in *Halomonas elongata*.” *Extremophiles* 24:421–432, **April 2020**. DOI: [10.1007/s00792-020-01168-y](https://doi.org/10.1007/s00792-020-01168-y).
7. Hoffmann T, Bremer E. “Guardians in a stressful world: the Opu family of compatible solute transporters from *Bacillus subtilis*.” *Biological Chemistry* 398:193–214, **February 2017**. DOI: [10.1515/hsz-2016-0265](https://doi.org/10.1515/hsz-2016-0265).
8. von Blohn C, Kempf B, Kappes RM, Bremer E. “Osmostress response in *Bacillus subtilis*: characterization of a proline uptake system (OpuE).” *Molecular Microbiology* 25:175–187, **July 1997**. DOI: [10.1046/j.1365-2958.1997.4441809.x](https://doi.org/10.1046/j.1365-2958.1997.4441809.x).
9. Kappes R, Kempf B, Bremer E. “Three transport systems for the osmoprotectant glycine betaine operate in *Bacillus subtilis*: characterization of OpuD.” *Journal of Bacteriology* 178:5071–5079, **September 1996**. DOI: [10.1128/jb.178.17.5071-5079.1996](https://doi.org/10.1128/jb.178.17.5071-5079.1996).
10. Booth IR. “Bacterial mechanosensitive channels: progress towards an understanding of their roles in cell physiology.” *Current Opinion in Microbiology* 18:16–22, **April 2014**. DOI: [10.1016/j.mib.2014.01.005](https://doi.org/10.1016/j.mib.2014.01.005).
11. Ventosa A, Nieto JJ, Oren A. “Biology of Moderately Halophilic Aerobic Bacteria.” *Microbiology and Molecular Biology Reviews* 62:504–544, **June 1998**. DOI: [10.1128/MMBR.62.2.504-544.1998](https://doi.org/10.1128/MMBR.62.2.504-544.1998).
12. Existing evidence supplied with the trait: FEMS Microbiology Reviews, DOI: [10.1093/femsre/fuy009](https://doi.org/10.1093/femsre/fuy009). Use for broad osmoadaptation context only until the exact threshold wording is manually verified.

## Conclusion

The defensible core of the TraitMech graph is a physiological chain from elevated NaCl/external osmolality through water loss, reduced hydration and turgor, molecular crowding, and growth inhibition, opposed by compatible-solute accumulation and ion homeostasis. Recent 2024 experiments strongly validate ectoine, glutamate/GABA, proline, glycine-betaine synthesis, and Na⁺/H⁺ antiport as causal determinants of salt-growth ceilings. However, those studies concern limits of 3–8% NaCl, not `METPO:1000469` directly. The low-range trait should therefore be curated as an assay-defined phenotype with these mechanisms represented as supported candidate contributors or inverse modifiers—not as universal causes—until direct ≤1% genetic or physiological perturbation studies are available.

References

1. (bremer2019responsesofmicroorganisms pages 3-5): Erhard Bremer and Reinhard Krämer. Responses of microorganisms to osmotic stress. Annual review of microbiology, 73:313-334, Sep 2019. URL: https://doi.org/10.1146/annurev-micro-020518-115504, doi:10.1146/annurev-micro-020518-115504. This article has 531 citations and is from a peer-reviewed journal.

2. (goszcz2025bacterialosmoprotectants—away pages 4-5): Aleksandra Goszcz, Karolina Furtak, Robert Stasiuk, Joanna Wójtowicz, Marcin Musiałowski, Michela Schiavon, and Klaudia Dębiec-Andrzejewska. Bacterial osmoprotectants—a way to survive in saline conditions and potential crop allies. FEMS Microbiology Reviews, May 2025. URL: https://doi.org/10.1093/femsre/fuaf020, doi:10.1093/femsre/fuaf020. This article has 55 citations and is from a domain leading peer-reviewed journal.

3. (lichty2024compatiblesolutesare pages 19-23): Compatible Solutes Are Accumulated in Response to Osmotic Stress and Are Used as an Abundant Nutrient Source in Marine Bacteria This article has 0 citations.

4. (zou2024metabolicengineeringof pages 4-8): Ziyan Zou, Pulla Kaothien-Nakayama, Junpei Ogawa-Iwamura, and Hideki Nakayama. Metabolic engineering of high-salinity-induced biosynthesis of γ-aminobutyric acid improves salt-stress tolerance in a glutamic acid-overproducing mutant of an ectoine-deficient <i>halomonas elongata</i>. Applied and Environmental Microbiology, Jan 2024. URL: https://doi.org/10.1128/aem.01905-23, doi:10.1128/aem.01905-23. This article has 18 citations and is from a peer-reviewed journal.

5. (fan2024improvementinsalt pages 12-14): Min Fan, Shuyu Tan, Wei Wang, and Xuehong Zhang. Improvement in salt tolerance ability of pseudomonas putida kt2440. Biology, 13:404, Jun 2024. URL: https://doi.org/10.3390/biology13060404, doi:10.3390/biology13060404. This article has 24 citations.

6. (zou2024metabolicengineeringof pages 2-4): Ziyan Zou, Pulla Kaothien-Nakayama, Junpei Ogawa-Iwamura, and Hideki Nakayama. Metabolic engineering of high-salinity-induced biosynthesis of γ-aminobutyric acid improves salt-stress tolerance in a glutamic acid-overproducing mutant of an ectoine-deficient <i>halomonas elongata</i>. Applied and Environmental Microbiology, Jan 2024. URL: https://doi.org/10.1128/aem.01905-23, doi:10.1128/aem.01905-23. This article has 18 citations and is from a peer-reviewed journal.

7. (goszcz2025bacterialosmoprotectants—away pages 5-5): Aleksandra Goszcz, Karolina Furtak, Robert Stasiuk, Joanna Wójtowicz, Marcin Musiałowski, Michela Schiavon, and Klaudia Dębiec-Andrzejewska. Bacterial osmoprotectants—a way to survive in saline conditions and potential crop allies. FEMS Microbiology Reviews, May 2025. URL: https://doi.org/10.1093/femsre/fuaf020, doi:10.1093/femsre/fuaf020. This article has 55 citations and is from a domain leading peer-reviewed journal.