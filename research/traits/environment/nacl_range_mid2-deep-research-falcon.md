---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T01:57:11.893757'
end_time: '2026-08-04T02:06:08.543226'
duration_seconds: 536.65
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: NaCl range mid2
  trait_identifier: METPO:1000471
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: nacl_range_mid2
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A NaCl range phenotype in which the growth-supporting NaCl range spans\
    \ approximately 3\u20138% (w/v), characteristic of moderate-halophile organisms."
  parent_traits: METPO:1000334
  synonyms: Halotolerant, Moderate halophile, NaR_3_to_8
  evidence_summary: "DOI:10.1093/femsre/fuy009: moderate halophile (Osmoadaptation\
    \ review supports the 3\u20138% NaCl growth range as the moderate-halophile category.)"
  causal_graph_summary: 'nacl_range_mid2_moderate_halophile: 10 nodes, 9 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 31
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** NaCl range mid2
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000471
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl range phenotype in which the growth-supporting NaCl range spans approximately 3–8% (w/v), characteristic of moderate-halophile organisms.
- **Parent traits:** METPO:1000334
- **Synonyms:** Halotolerant, Moderate halophile, NaR_3_to_8
- **Existing evidence:** DOI:10.1093/femsre/fuy009: moderate halophile (Osmoadaptation review supports the 3–8% NaCl growth range as the moderate-halophile category.)
- **Existing causal graph summary:** nacl_range_mid2_moderate_halophile: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **NaCl range mid2** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_range_mid2.yaml`.

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
- **Trait label:** NaCl range mid2
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000471
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl range phenotype in which the growth-supporting NaCl range spans approximately 3–8% (w/v), characteristic of moderate-halophile organisms.
- **Parent traits:** METPO:1000334
- **Synonyms:** Halotolerant, Moderate halophile, NaR_3_to_8
- **Existing evidence:** DOI:10.1093/femsre/fuy009: moderate halophile (Osmoadaptation review supports the 3–8% NaCl growth range as the moderate-halophile category.)
- **Existing causal graph summary:** nacl_range_mid2_moderate_halophile: 10 nodes, 9 edges

## Research Objective

Research the microbial trait **NaCl range mid2** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_range_mid2.yaml`.

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


# Curation-focused research report: NaCl range mid2

## Executive summary

**Target trait:** “NaCl range mid2”  
**Identifier:** **METPO:1000471**  
**Category/kind:** ENVIRONMENT / CLASS  
**Parent:** METPO:1000334  
**Operational definition supplied for curation:** growth-supporting NaCl range of approximately **3–8% (w/v)**.

This term should be interpreted as an **assay-observed growth-range bin**, not as a universal mechanistic class. Classical moderate-halophile terminology is usually based on the **salinity optimum**: the authoritative Ventosa–Nieto–Oren review reports optimal growth at approximately **0.5–2.5 M salt** for moderate halophiles. It also distinguishes halotolerant organisms by their ability to grow without added salt. Medium composition, temperature, and measurement endpoint can shift reported boundaries (ventosa1998biologyofmoderately pages 2-3).

The strongest causal evidence relevant to the 3–8% interval comes from *Halomonas elongata*. Deleting **ectABC** sharply reduces the upper NaCl growth limit, while replacing ectoine with engineered proline or GABA accumulation restores growth within the target interval. These experiments support a compact core graph: **elevated extracellular NaCl → osmotic stress → compatible-solute accumulation → improved growth at 3–8% NaCl**. TeaABC-mediated ectoine uptake and mechanosensitive channels provide supporting uptake/retention and hypoosmotic-survival branches. K⁺ accumulation, glycine-betaine transport, ion transporters, and respiratory remodeling are biologically plausible but presently supported mainly by expression or metabolite correlations and should be marked uncertain (xing2024thepolyextremophilenatranaerobius pages 14-17, xing2024thepolyextremophilenatranaerobius pages 17-19, xing2024thepolyextremophilenatranaerobius pages 10-14).

## 1. Trait scope and boundary cases

### 1.1 What the phenotype represents

METPO:1000471 represents the experimentally observed capacity to grow over an NaCl interval whose salient span is approximately **3–8 g NaCl per 100 mL medium**. Depending on protocol, “growth-supporting” may mean detectable growth, a threshold optical density, colony formation, or positive growth relative to an uninoculated control. It does **not** by itself identify the optimum, growth rate, osmotic strategy, intracellular ion concentration, or environmental niche.

For reproducible YAML curation, the assay context should retain:

- NaCl concentration in **% w/v** and, if reported, molarity;
- medium composition and water activity;
- temperature, pH, oxygen regime, and incubation time;
- growth endpoint and detection threshold;
- whether 3% and 8% are tested points or interpolated boundaries;
- strain and genotype.

### 1.2 Nearby concepts

1. **Classical moderate halophile:** commonly an organism with an optimal-growth salinity of 0.5–2.5 M salt. This is not equivalent to a total growth range of 3–8% NaCl (ventosa1998biologyofmoderately pages 2-3).
2. **Halotolerant:** able to grow without salt and also at elevated salinity. Thus “halotolerant” should not be treated as an exact synonym unless zero-NaCl growth was tested (ventosa1998biologyofmoderately pages 2-3).
3. **Extreme or borderline-extreme halophile:** requires substantially higher salt; the classical review cites a borderline-extreme example requiring at least 2 M and growing optimally around 3.4 M (ventosa1998biologyofmoderately pages 2-3).
4. **Upper-limit phenotype:** growth at 8% does not prove that the complete range ends at 8%; *H. elongata*, for example, can grow above 10% NaCl, so it is a mechanistic model but may not instantiate this exact range bin (hobmeier2022adaptationtovarying pages 1-2).
5. **Transient salt survival:** survival after osmotic shock is not equivalent to sustained growth. Mechanosensitive-channel results should therefore form a supporting stress-survival branch, not the primary range-defining edge (vandrich2020contributionofmechanosensitive pages 6-8).

## 2. Current mechanistic understanding

Moderately halophilic bacteria generally balance extracellular osmotic pressure through combinations of two strategies:

- **“Salt-out”/compatible-solute strategy:** synthesis or uptake of organic osmolytes such as ectoine, glycine betaine, proline, glutamate, or GABA while limiting disruptive cytoplasmic Na⁺.
- **Ion accumulation or hybrid strategy:** controlled accumulation of K⁺ and other ions, coupled to ion transport and proteome adaptation.

Recent evidence argues against treating these as mutually exclusive. A 2024 multi-omics study of *Natranaerobius thermophilus* found simultaneous compatible-solute and K⁺ accumulation under increasing salinity. Glycine betaine increased from 52.7 to 893.1 mM, glutamate from 11.0 to 221.3 mM, and proline ranged from 67.0 to 130 mM across 2.5–4.3 M Na⁺ conditions. Because these results are expression/metabolite correlations in an organism adapted to much higher salinity than 3–8% NaCl, they support general mechanism nodes but not a direct edge to METPO:1000471 (xing2024thepolyextremophilenatranaerobius pages 14-17, xing2024thepolyextremophilenatranaerobius pages 17-19).

## 3. Candidate causal-graph nodes

### 3.1 Trait and environmental nodes

| Candidate node | Suggested grounding | Curation note |
|---|---|---|
| NaCl range mid2 | **METPO:1000471** | Preserve verbatim CURIE. |
| extracellular NaCl concentration | **CHEBI:26710** (sodium chloride) | Record concentration as an edge/assay attribute. |
| elevated salinity / hyperosmotic condition | Label-only unless the project has a preferred ENVO/METPO term | Do not conflate concentration with osmotic stress. |
| hypoosmotic downshock | Label-only | Supporting survival process, not the defining phenotype. |
| microbial growth in 3–8% NaCl | METPO:1000471 or label-only assay node | Prefer explicit measured-growth node if graph schema permits. |

### 3.2 Genes, proteins, and complexes

- **ectA** — diaminobutyrate acetyltransferase; label-only pending organism-specific accession.
- **ectB** — L-2,4-diaminobutyrate transaminase; label-only.
- **ectC** — ectoine synthase; label-only.
- **EctABC ectoine-biosynthesis module** — label-only composite node.
- **TeaABC** — ectoine-specific TRAP transporter; label-only composite node.
- **proBm1AC engineered cluster** — γ-glutamate kinase, γ-glutamyl-phosphate reductase, and pyrroline-5-carboxylate reductase; engineered, taxon-specific node.
- **putA** — proline catabolism enzyme; label-only.
- **HopGadBmut/GadB** — engineered glutamate decarboxylase; label-only.
- **MscK, MscS1, MscS2, MscS3** — small-conductance mechanosensitive-channel proteins; label-only.
- **OpuA/OpuB/ProU/BetT systems** — compatible-solute transporters; presently correlative in the retrieved 2024 evidence.
- **PutP** — Na⁺/proline symporter; correlative.
- **Mrp-family ion exchanger** — candidate ion-homeostasis node; exact substrate direction and causal relevance require strain-specific validation.
- **cytochrome bo′ and cytochrome bd quinol oxidases** — respiratory remodeling candidates; transcriptomic evidence only.

Organism-specific UniProt accessions should be added only after checking the exact strain proteome; gene names alone are safer than transferring accessions across *Halomonas* strains.

### 3.3 Chemicals and metabolites

| Metabolite | Suggested CURIE | Role |
|---|---|---|
| Ectoine | **CHEBI:43729** | Major compatible solute in *H. elongata*. |
| Potassium ion | **CHEBI:29103** | Inorganic osmotic counterion in hybrid/salt-in responses. |
| Glycine betaine | **CHEBI:17750** | Imported or synthesized compatible solute. |
| L-proline | **CHEBI:17203** | Compatible solute; engineered causal evidence at 8% NaCl. |
| L-glutamate | **CHEBI:29985** | Osmolyte and precursor of proline/GABA. |
| 4-aminobutanoate/GABA | **CHEBI:16865** | Engineered compatible solute and pH-homeostasis product. |
| Sodium ion | **CHEBI:29101** | Extracellular stressor and transported ion. |

### 3.4 Processes and localizations

- ectoine biosynthesis;
- compatible-solute accumulation;
- ectoine transmembrane uptake;
- proline biosynthesis and catabolism;
- glutamate decarboxylation;
- potassium-ion accumulation;
- sodium-ion efflux/ion homeostasis;
- osmotic-stress response;
- cytoplasmic osmotic balance;
- mechanosensitive-channel-mediated solute release;
- respiratory-chain remodeling.

Where exact GO identifiers have not been independently verified, retain labels rather than creating or guessing CURIEs.

## 4. Candidate evidence-backed edges

The following matrix summarizes the most conservative graph structure.

| Proposed subject-predicate-object edge | Evidence class | Taxon/strain | Quantitative result | DOI |
|---|---|---|---|---|
| `ectABC deletion` → `decreases ectoine biosynthesis` → `reduces NaCl tolerance` (conservative phenotype proxy for ectoine-dependent salt tolerance) (zou2024metabolicengineeringof pages 2-4, zou2024metabolicengineeringof pages 4-8) | direct perturbation | *Halomonas elongata* OUT30018 derivative KA1 (ΔectABC) | KA1 “could only grow” at `≤4% NaCl`; one excerpt states “cannot grow above 3% NaCl,” indicating assay-specific boundary variation across media/experiments | 10.1128/AEM.01905-23 |
| `proBm1AC insertion + putA deletion` → `increases intracellular proline` → `restores growth at high NaCl` (khanh2024metabolicpathwayengineering pages 1-2) | direct perturbation | *Halomonas elongata* HN6 (ΔectABC::proBm1AC ΔputA) | Engineered strain “thrived” at `8% NaCl`; intracellular proline `353.1 ± 40.5 µmol/g cell fresh weight`; ectoine-deficient control could not grow above `4% NaCl` | 10.1128/AEM.01195-24 |
| `HopGadBmut expression` → `increases GABA accumulation` → `improves salt tolerance` (zou2024metabolicengineeringof pages 2-4) | direct perturbation | *Halomonas elongata* GOP-Gad | GOP-Gad had higher salt tolerance than GOP strain; intracellular GABA reached `176.94 µmol/g cell dry weight` in `7% NaCl`; GOP restored growth to `6% NaCl` from ectoine-deficient background | 10.1128/AEM.01905-23 |
| `TeaABC` → `mediates ectoine uptake` → `supports ectoine retention/osmoregulation` (hobmeier2022adaptationtovarying pages 14-16, vandrich2020contributionofmechanosensitive pages 6-8, vandrich2020contributionofmechanosensitive pages 1-2) | direct perturbation | *Halomonas elongata* DSM 2581T / KB2.13 (ΔteaABC) | ΔteaABC strain described as “deficient in osmoregulatory uptake of ectoine”; disruption causes constant ectoine loss to medium; no uptake-rate constant retrieved here | 10.1007/s00792-020-01168-y |
| `MscK/MscS-family channels` → `promote survival after hypoosmotic downshock` → `prevent lysis` (vandrich2020contributionofmechanosensitive pages 6-8, vandrich2020contributionofmechanosensitive pages 1-2) | direct perturbation | *Halomonas elongata* MSC-1324 (ΔmscK ΔmscS1 ΔmscS2 ΔmscS3) | Survival after `1 M → 0.1 M NaCl` downshock: wild type `~10%` vs quadruple mutant `~0.1%`; complementation with MscK, MscS2, or MscS3 restored ~wild-type survival | 10.1007/s00792-020-01168-y |
| `quadruple mscS-family deletion` → `slightly reduces ectoine export but not abolishes it` → `unknown major ectoine export route remains` (vandrich2020contributionofmechanosensitive pages 6-8, vandrich2020contributionofmechanosensitive pages 1-2) | direct perturbation | *Halomonas elongata* KB2.13-MSC | All-four-channel knockout still exported `~80%` of ectoine compared with wild type/parental reference; growth at high salinity remained similar in tested conditions | 10.1007/s00792-020-01168-y |
| `increased salinity` → `increases K+ accumulation` → `supports osmoadaptation` (xing2024thepolyextremophilenatranaerobius pages 14-17, xing2024thepolyextremophilenatranaerobius pages 17-19, xing2024thepolyextremophilenatranaerobius pages 10-14) | correlative | *Natranaerobius thermophilus* DSM 2266 | Under `2.5–4.3 M Na+`, intracellular K+ increased with salinity; study concludes simultaneous compatible-solute and K+ accumulation during long-term salt adaptation | 10.1128/AEM.00145-24 |
| `increased salinity` → `increases compatible solutes (glycine betaine, glutamate, proline)` → `supports osmoadaptation` (xing2024thepolyextremophilenatranaerobius pages 14-17, xing2024thepolyextremophilenatranaerobius pages 17-19) | correlative | *Natranaerobius thermophilus* DSM 2266 | Glycine betaine `52.7–893.1 mM`, glutamate `11.0–221.3 mM`, proline `67.0–130 mM` across `2.5–4.3 M Na+`; transporter and biosynthesis genes were upregulated | 10.1128/AEM.00145-24 |
| `salt stress` → `upregulates cytochrome bo' / cytochrome bd quinol oxidases` → `alters respiratory adaptation to salinity` (hobmeier2022adaptationtovarying pages 1-2) | correlative | *Halomonas elongata* DSM 2581T | Transcriptomics at `0.17 M`, `1 M`, and `2 M NaCl` found bo' and bd pathways “seem to be upregulated” in salt-stressed cells; no perturbational causality yet | 10.3389/fmicb.2022.846677 |
| `moderate-halophile growth-range phenotype` → `approximately 3–8% (w/v) NaCl growth-supporting range` → `overlaps but is not identical to classical optimal-growth-based moderate halophily` (ventosa1998biologyofmoderately pages 2-3) | literature definition / boundary note | Trait-level interpretation vs classical halophile category | Classical scheme defines moderate halophiles by optimal growth at `0.5–2.5 M salt` rather than total growth range; therefore METPO:1000471 should be curated as an assay growth-range bin, not a strict synonym of all “moderately halophilic” taxa | 10.1128/MMBR.62.2.504-544.1998 |


*Table: This table summarizes conservative, curation-ready evidence for candidate causal edges underlying the NaCl range mid2 phenotype. It distinguishes direct perturbation results from correlative salt-response observations and highlights where trait-level scope differs from classical moderate-halophile terminology.*

### 4.1 Expanded edge table with supporting snippets

| # | Subject — predicate — object | Reference | Supporting snippet | Curation interpretation |
|---|---|---|---|---|
| 1 | **ectABC — enables biosynthesis of — ectoine** | Zou et al., 2024; DOI 10.1128/aem.01905-23 | “ectB encoding L-2,4-diaminobutyric acid transaminase… ectA encoding DABA acetyltransferase… ectC encoding ectoine synthase” | **Strong, direct biochemical annotation**, but demonstrated in *H. elongata*. (zou2024metabolicengineeringof pages 4-8) |
| 2 | **ectABC deletion — decreases — NaCl growth tolerance** | Zou et al., 2024 | The ΔectABC KA1 mutant “cannot grow above 3% NaCl” in the reported assay; another summary gives ≤4%, reflecting protocol/context differences. | **Strong perturbation edge.** Curate strain, medium, and threshold; do not encode a universal 3% cutoff. (zou2024metabolicengineeringof pages 2-4, zou2024metabolicengineeringof pages 4-8) |
| 3 | **ectoine accumulation — promotes — growth at elevated NaCl** | Zou et al., 2024; Khanh et al., 2024 | Loss of ectoine synthesis lowers the growth ceiling, whereas alternative osmolytes restore it. | Strong causal inference from loss-and-bypass experiments, although the alternative-solute rescue means ectoine is sufficient/important rather than uniquely required. (zou2024metabolicengineeringof pages 2-4, khanh2024metabolicpathwayengineering pages 1-2) |
| 4 | **proBm1AC expression plus putA deletion — increases — intracellular proline** | Khanh et al., 2024; DOI 10.1128/aem.01195-24 | HN6 accumulated “353.1 ± 40.5 µmol/g cell fresh weight.” | **Strong engineered perturbation**, specific to HN6. (khanh2024metabolicpathwayengineering pages 1-2) |
| 5 | **intracellular proline accumulation — promotes — growth at 8% NaCl** | Khanh et al., 2024 | Ectoine-deficient KA1 failed above 4%, whereas HN6 “thrived” at 8% NaCl. | **Highest-value edge for METPO:1000471**, because the endpoint lies exactly at the target upper boundary. Engineered context must be retained. (khanh2024metabolicpathwayengineering pages 1-2) |
| 6 | **HopGadBmut expression — converts glutamate toward — GABA accumulation** | Zou et al., 2024 | Salt-inducible mutant glutamate decarboxylase was introduced into the GOP strain. | Direct engineered-pathway edge. (zou2024metabolicengineeringof pages 2-4) |
| 7 | **GABA accumulation — increases — salt tolerance** | Zou et al., 2024 | GOP-Gad showed higher tolerance and accumulated 176.94 µmol GABA/g dry weight at 7% NaCl. | **Strong but engineered and assay-specific**; 7% falls within the trait interval. (zou2024metabolicengineeringof pages 2-4) |
| 8 | **TeaABC — mediates — osmoregulatory ectoine uptake** | Vandrich et al., 2020; DOI 10.1007/s00792-020-01168-y | ΔteaABC was “deficient in osmoregulatory uptake of ectoine”; disruption caused continual ectoine loss to the medium. | Strong transporter perturbation. The downstream edge to 3–8% growth was not directly quantified in the retrieved excerpt. (hobmeier2022adaptationtovarying pages 14-16, vandrich2020contributionofmechanosensitive pages 6-8, vandrich2020contributionofmechanosensitive pages 1-2) |
| 9 | **MscK/MscS-family channels — promote — survival after hypoosmotic downshock** | Vandrich et al., 2020 | Following 1 M→0.1 M NaCl downshock, survival was ~10% in wild type and ~0.1% in the quadruple mutant. | Strong direct edge for osmotic-transition survival, but **not direct evidence for sustained 3–8% growth**. (vandrich2020contributionofmechanosensitive pages 6-8) |
| 10 | **MscS-family channels — contribute partly to — ectoine export** | Vandrich et al., 2020 | The quadruple knockout still exported approximately 80% of wild-type ectoine. | Curate as a **minor contribution** or “not necessary for most export”; an unknown system is likely the principal route. (vandrich2020contributionofmechanosensitive pages 1-2) |
| 11 | **increasing salinity — increases — K⁺ accumulation** | Xing et al., 2024; DOI 10.1128/aem.00145-24 | Intracellular K⁺ rose with external salinity, alongside transporter expression. | **Correlative and taxon-specific**; organism grows at far higher salinity than the target interval. (xing2024thepolyextremophilenatranaerobius pages 14-17, xing2024thepolyextremophilenatranaerobius pages 17-19) |
| 12 | **increasing salinity — increases — glycine-betaine accumulation** | Xing et al., 2024 | Glycine betaine rose from 52.7 to 893.1 mM across 2.5–4.3 M Na⁺. | Strong quantitative association, but no knockout/rescue and outside the target concentration range. Mark uncertain. (xing2024thepolyextremophilenatranaerobius pages 17-19) |
| 13 | **Opu/ProU/BetT transport systems — contribute to — compatible-solute uptake** | Xing et al., 2024 | Glycine-betaine/proline transporter systems were salt-dependently upregulated. | Correlative multi-omics evidence only. Do not assert necessity. (xing2024thepolyextremophilenatranaerobius pages 14-17) |
| 14 | **salt stress — upregulates — cytochrome bo′/bd respiratory branches** | Hobmeier et al., 2022; DOI 10.3389/fmicb.2022.846677 | The two quinol-oxidase routes “seem to be upregulated” in salt-stressed cells. | **Uncertain:** transcriptomic response, not a demonstrated cause of salt-range growth. (hobmeier2022adaptationtovarying pages 1-2) |
| 15 | **controlled cytoplasmic ion accumulation — may promote — high-salinity adaptation** | Hobmeier et al., 2022 | Authors propose that ion accumulation plays a larger role than previously assumed. | Expert model based on transcriptome/proteome properties; do not curate as a universal direct edge without perturbation. (hobmeier2022adaptationtovarying pages 1-2) |

## 5. Recommended minimal TraitMech graph

A defensible initial graph should prioritize direct perturbation evidence:

1. **elevated extracellular NaCl** → *induces* → **osmotic stress**;
2. **ectABC** → *enables* → **ectoine biosynthesis**;
3. **ectoine biosynthesis** → *increases* → **intracellular ectoine accumulation**;
4. **intracellular compatible-solute accumulation** → *promotes* → **growth at 3–8% NaCl**;
5. **TeaABC** → *mediates* → **ectoine uptake/retention**;
6. **proBm1AC + ΔputA** → *increases* → **intracellular proline**;
7. **intracellular proline** → *promotes* → **growth at 8% NaCl**;
8. **HopGadBmut** → *increases* → **intracellular GABA**;
9. **intracellular GABA** → *promotes* → **growth at 7% NaCl**;
10. **MscK/MscS channels** → *promote* → **hypoosmotic-downshock survival**.

Edges 6–9 should carry qualifiers such as `engineered: true`, `taxon: Halomonas elongata`, and the exact strain/genotype. The mechanosensitive-channel branch should terminate in osmotic-transition survival rather than METPO:1000471 unless a sustained-growth assay is added.

## 6. Recent developments and quantitative findings

### 6.1 Alternative osmolytes can replace ectoine

Two 2024 studies provide unusually strong causal evidence because they combine ectoine-pathway deletion with metabolic rescue:

- A proline-producing strain, **HN6 (ΔectABC::proBm1AC ΔputA)**, accumulated **353.1 ± 40.5 µmol proline/g cell fresh weight** and grew at **8% NaCl**, whereas the ectoine-deficient control did not grow above approximately 4% (khanh2024metabolicpathwayengineering pages 1-2).
- A glutamate-overproducing suppressor restored growth to approximately **6–7% NaCl**. Adding salt-inducible **GadBmut** increased GABA accumulation and salt tolerance; the engineered strain accumulated **176.94 µmol GABA/g cell dry weight at 7% NaCl** (zou2024metabolicengineeringof pages 2-4, zou2024metabolicengineeringof pages 4-8).

These experiments show that the causal variable is not necessarily ectoine identity but attainment of adequate **compatible-solute capacity**, with pH homeostasis also relevant when acidic glutamate accumulates.

### 6.2 Hybrid salt-in/salt-out adaptation

The 2024 *N. thermophilus* study reported simultaneous K⁺ and compatible-solute accumulation and salt-dependent induction of Opu, ProU, BetT, PutP, and other transport systems. Some genes/proteins increased by more than 100-fold, and 90.8% of 109 co-upregulated genes had fold changes of at least 1.5 at P<0.05. This supports a distributed osmoadaptation architecture rather than a single-pathway explanation, but the salinity regime of 2.5–4.3 M Na⁺ is far above the METPO interval (xing2024thepolyextremophilenatranaerobius pages 14-17, xing2024thepolyextremophilenatranaerobius pages 10-14).

### 6.3 Osmotic transition management

The 2020 quadruple-channel knockout reduced survival after severe hypoosmotic downshock from approximately **10% to 0.1%**, a roughly 100-fold difference. Complementation with MscK, MscS2, or MscS3 restored near-wild-type survival, indicating redundancy. Yet deletion did not eliminate ectoine export and could improve growth at 2 M NaCl, demonstrating that mechanisms beneficial during downshock need not improve steady-state high-salt growth (vandrich2020contributionofmechanosensitive pages 6-8, vandrich2020contributionofmechanosensitive pages 1-2).

## 7. Applications and real-world implementations

- ***Halomonas elongata* as an ectoine cell factory:** ectoine is produced industrially at ton scale for cosmetic and medicinal formulations. Engineering precursor supply or TeaBC-associated export can increase ectoine secretion, although those production phenotypes should not automatically be included in the environmental-trait graph.
- **Proline- and GABA-rich cell factories:** the 2024 engineered strains were proposed for converting biomass-derived substrates into osmolytes or feed additives under saline processing conditions. The 8% NaCl HN6 result directly demonstrates operation within the METPO interval (khanh2024metabolicpathwayengineering pages 1-2).
- **Saline agriculture and bioremediation:** compatible-solute-producing and ion-tolerant microbes are candidates for saline-soil inoculants and high-salt waste treatment. However, genomic detection of tolerance genes alone is not sufficient to assign METPO:1000471; growth must be measured.
- **Low-sterility bioprocesses:** moderate salinity can suppress contaminants, making halophilic hosts attractive for open or reduced-sterility fermentation. This is an application of the phenotype, not a causal mechanism.

## 8. Expert interpretation

The literature supports three curation principles:

1. **Model the trait as a system-level outcome.** Ectoine is prominent, but ion transport, K⁺, respiration, envelope behavior, pH homeostasis, and alternative osmolytes can modify the growth range (hobmeier2022adaptationtovarying pages 1-2, xing2024thepolyextremophilenatranaerobius pages 14-17).
2. **Separate steady-state growth from osmotic-shock survival.** Mechanosensitive channels are decisive during downshock but are not proven determinants of the 3–8% sustained-growth interval (vandrich2020contributionofmechanosensitive pages 6-8).
3. **Prefer perturbation evidence over omics association.** ΔectABC and proline/GABA rescue experiments warrant causal edges; transporter induction and K⁺ correlations warrant qualified, taxon-specific edges only (zou2024metabolicengineeringof pages 2-4, khanh2024metabolicpathwayengineering pages 1-2, xing2024thepolyextremophilenatranaerobius pages 14-17).

## 9. Warnings: claims not yet ready for unconditional curation

- Do **not** treat “halotolerant,” “moderate halophile,” and `NaR_3_to_8` as exact synonyms without recording the defining assay.
- Do **not** equate the classical 0.5–2.5 M optimum-based definition with the supplied 3–8% total growth range (ventosa1998biologyofmoderately pages 2-3).
- Do **not** infer METPO:1000471 from the presence of `ectABC`, `teaABC`, `opu`, `proU`, `betT`, `putP`, antiporter, or mechanosensitive-channel genes alone.
- Do **not** curate Na⁺/H⁺ antiport as a specific causal edge from the present evidence set; exact transporter identity, directionality, and perturbation evidence remain insufficient.
- Treat K⁺ accumulation and glycine-betaine/proline/glutamate responses in *N. thermophilus* as **taxon-specific correlations at extreme salinity**, not direct evidence for a 3–8% phenotype (xing2024thepolyextremophilenatranaerobius pages 14-17, xing2024thepolyextremophilenatranaerobius pages 17-19).
- Treat cytochrome bo′/bd induction as **uncertain** until respiratory-branch knockouts or inhibitors are tied to growth across the target interval (hobmeier2022adaptationtovarying pages 1-2).
- Do not make MscS channels the direct cause of high-salt growth; the strongest result concerns hypoosmotic downshock, and most ectoine export persisted after channel deletion (vandrich2020contributionofmechanosensitive pages 6-8, vandrich2020contributionofmechanosensitive pages 1-2).
- Preserve conflicting KA1 thresholds—“above 3%” versus “above 4%”—as assay-specific observations rather than silently choosing one universal cutoff (zou2024metabolicengineeringof pages 2-4, zou2024metabolicengineeringof pages 4-8).
- Engineered bypasses demonstrate mechanistic sufficiency in particular genetic backgrounds; they do not establish that wild moderate halophiles naturally use proline or GABA as their dominant osmolyte.

## 10. DOI-first bibliography

1. **Khanh HC, Kaothien-Nakayama P, Zou Z, Nakayama H.** “Metabolic pathway engineering of high-salinity-induced overproduction of L-proline improves high-salinity stress tolerance of an ectoine-deficient *Halomonas elongata*.” *Applied and Environmental Microbiology* 90, September 2024. DOI: [10.1128/aem.01195-24](https://doi.org/10.1128/aem.01195-24). (khanh2024metabolicpathwayengineering pages 1-2)
2. **Zou Z, Kaothien-Nakayama P, Ogawa-Iwamura J, Nakayama H.** “Metabolic engineering of high-salinity-induced biosynthesis of γ-aminobutyric acid improves salt-stress tolerance in a glutamic acid-overproducing mutant of an ectoine-deficient *Halomonas elongata*.” *Applied and Environmental Microbiology* 90, January 2024. DOI: [10.1128/aem.01905-23](https://doi.org/10.1128/aem.01905-23). (zou2024metabolicengineeringof pages 2-4, zou2024metabolicengineeringof pages 4-8)
3. **Xing Q et al.** “The polyextremophile *Natranaerobius thermophilus* adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and K⁺.” *Applied and Environmental Microbiology* 90, May 2024. DOI: [10.1128/aem.00145-24](https://doi.org/10.1128/aem.00145-24). (xing2024thepolyextremophilenatranaerobius pages 14-17, xing2024thepolyextremophilenatranaerobius pages 17-19, xing2024thepolyextremophilenatranaerobius pages 10-14)
4. **Hobmeier K et al.** “Adaptation to Varying Salinity in *Halomonas elongata*: Much More Than Ectoine Accumulation.” *Frontiers in Microbiology* 13, March 2022. DOI: [10.3389/fmicb.2022.846677](https://doi.org/10.3389/fmicb.2022.846677). (hobmeier2022adaptationtovarying pages 1-2, hobmeier2022adaptationtovarying pages 14-16)
5. **Vandrich J, Pfeiffer F, Alfaro-Espinoza G, Kunte HJ.** “Contribution of mechanosensitive channels to osmoadaptation and ectoine excretion in *Halomonas elongata*.” *Extremophiles* 24:421–432, April 2020. DOI: [10.1007/s00792-020-01168-y](https://doi.org/10.1007/s00792-020-01168-y). (vandrich2020contributionofmechanosensitive pages 6-8, vandrich2020contributionofmechanosensitive pages 1-2)
6. **Ventosa A, Nieto JJ, Oren A.** “Biology of Moderately Halophilic Aerobic Bacteria.” *Microbiology and Molecular Biology Reviews* 62:504–544, June 1998. DOI: [10.1128/MMBR.62.2.504-544.1998](https://doi.org/10.1128/MMBR.62.2.504-544.1998). (ventosa1998biologyofmoderately pages 2-3)

The existing review evidence, DOI [10.1093/femsre/fuy009](https://doi.org/10.1093/femsre/fuy009), can remain attached to the trait’s terminology/background, but the direct 2024 *H. elongata* perturbation studies provide stronger support for causal edges within the 3–8% interval.

References

1. (ventosa1998biologyofmoderately pages 2-3): Antonio Ventosa, Joaquín J. Nieto, and Aharon Oren. Biology of moderately halophilic aerobic bacteria. Microbiology and Molecular Biology Reviews, 62:504-544, Jun 1998. URL: https://doi.org/10.1128/mmbr.62.2.504-544.1998, doi:10.1128/mmbr.62.2.504-544.1998. This article has 2011 citations and is from a domain leading peer-reviewed journal.

2. (xing2024thepolyextremophilenatranaerobius pages 14-17): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 20 citations and is from a peer-reviewed journal.

3. (xing2024thepolyextremophilenatranaerobius pages 17-19): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 20 citations and is from a peer-reviewed journal.

4. (xing2024thepolyextremophilenatranaerobius pages 10-14): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 20 citations and is from a peer-reviewed journal.

5. (hobmeier2022adaptationtovarying pages 1-2): Karina Hobmeier, Martina Cantone, Quynh Anh Nguyen, Katharina Pflüger-Grau, Andreas Kremling, Hans Jörg Kunte, Friedhelm Pfeiffer, and Alberto Marin-Sanguino. Adaptation to varying salinity in halomonas elongata: much more than ectoine accumulation. Frontiers in Microbiology, Mar 2022. URL: https://doi.org/10.3389/fmicb.2022.846677, doi:10.3389/fmicb.2022.846677. This article has 53 citations and is from a peer-reviewed journal.

6. (vandrich2020contributionofmechanosensitive pages 6-8): Jasmina Vandrich, Friedhelm Pfeiffer, Gabriela Alfaro-Espinoza, and Hans Jörg Kunte. Contribution of mechanosensitive channels to osmoadaptation and ectoine excretion in halomonas elongata. Extremophiles, 24:421-432, Apr 2020. URL: https://doi.org/10.1007/s00792-020-01168-y, doi:10.1007/s00792-020-01168-y. This article has 40 citations and is from a peer-reviewed journal.

7. (zou2024metabolicengineeringof pages 2-4): Ziyan Zou, Pulla Kaothien-Nakayama, Junpei Ogawa-Iwamura, and Hideki Nakayama. Metabolic engineering of high-salinity-induced biosynthesis of γ-aminobutyric acid improves salt-stress tolerance in a glutamic acid-overproducing mutant of an ectoine-deficient <i>halomonas elongata</i>. Applied and Environmental Microbiology, Jan 2024. URL: https://doi.org/10.1128/aem.01905-23, doi:10.1128/aem.01905-23. This article has 18 citations and is from a peer-reviewed journal.

8. (zou2024metabolicengineeringof pages 4-8): Ziyan Zou, Pulla Kaothien-Nakayama, Junpei Ogawa-Iwamura, and Hideki Nakayama. Metabolic engineering of high-salinity-induced biosynthesis of γ-aminobutyric acid improves salt-stress tolerance in a glutamic acid-overproducing mutant of an ectoine-deficient <i>halomonas elongata</i>. Applied and Environmental Microbiology, Jan 2024. URL: https://doi.org/10.1128/aem.01905-23, doi:10.1128/aem.01905-23. This article has 18 citations and is from a peer-reviewed journal.

9. (khanh2024metabolicpathwayengineering pages 1-2): Huynh Cong Khanh, Pulla Kaothien-Nakayama, Ziyan Zou, and Hideki Nakayama. Metabolic pathway engineering of high-salinity-induced overproduction of l-proline improves high-salinity stress tolerance of an ectoine-deficient <i>halomonas elongata</i>. Applied and Environmental Microbiology, Sep 2024. URL: https://doi.org/10.1128/aem.01195-24, doi:10.1128/aem.01195-24. This article has 11 citations and is from a peer-reviewed journal.

10. (hobmeier2022adaptationtovarying pages 14-16): Karina Hobmeier, Martina Cantone, Quynh Anh Nguyen, Katharina Pflüger-Grau, Andreas Kremling, Hans Jörg Kunte, Friedhelm Pfeiffer, and Alberto Marin-Sanguino. Adaptation to varying salinity in halomonas elongata: much more than ectoine accumulation. Frontiers in Microbiology, Mar 2022. URL: https://doi.org/10.3389/fmicb.2022.846677, doi:10.3389/fmicb.2022.846677. This article has 53 citations and is from a peer-reviewed journal.

11. (vandrich2020contributionofmechanosensitive pages 1-2): Jasmina Vandrich, Friedhelm Pfeiffer, Gabriela Alfaro-Espinoza, and Hans Jörg Kunte. Contribution of mechanosensitive channels to osmoadaptation and ectoine excretion in halomonas elongata. Extremophiles, 24:421-432, Apr 2020. URL: https://doi.org/10.1007/s00792-020-01168-y, doi:10.1007/s00792-020-01168-y. This article has 40 citations and is from a peer-reviewed journal.