---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T22:42:58.403729'
end_time: '2026-06-17T22:53:27.504584'
duration_seconds: 629.1
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: mesophilic
  trait_identifier: METPO:1000615
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: mesophilic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A temperature preference in which growth is favored at intermediate\
    \ temperatures, typically ~20\u201345 \xB0C."
  parent_traits: METPO:1000613
  synonyms: ''
  evidence_summary: 'DOI:10.1016/j.bpj.2013.06.029: Escherichia coli, a mesophilic
    bacterium (Organism example: Escherichia coli is described as mesophilic.) | DOI:10.1146/annurev-micro-091313-103612:
    more unsaturated fatty acids (Membrane-adaptation review supports homoviscous
    membrane composition matched to ambient temperature as the basis of mesophile
    physiology.)'
  causal_graph_summary: 'mesophilic_homoviscous_adaptation: 6 nodes, 4 edges'
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
- **Trait label:** mesophilic
- **METPO identifier:** METPO:1000615
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature preference in which growth is favored at intermediate temperatures, typically ~20–45 °C.
- **Parent traits:** METPO:1000613
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/j.bpj.2013.06.029: Escherichia coli, a mesophilic bacterium (Organism example: Escherichia coli is described as mesophilic.) | DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports homoviscous membrane composition matched to ambient temperature as the basis of mesophile physiology.)
- **Existing causal graph summary:** mesophilic_homoviscous_adaptation: 6 nodes, 4 edges

## Research Objective

Research the microbial trait **mesophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/mesophilic.yaml`.

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
- **Trait label:** mesophilic
- **METPO identifier:** METPO:1000615
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature preference in which growth is favored at intermediate temperatures, typically ~20–45 °C.
- **Parent traits:** METPO:1000613
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/j.bpj.2013.06.029: Escherichia coli, a mesophilic bacterium (Organism example: Escherichia coli is described as mesophilic.) | DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports homoviscous membrane composition matched to ambient temperature as the basis of mesophile physiology.)
- **Existing causal graph summary:** mesophilic_homoviscous_adaptation: 6 nodes, 4 edges

## Research Objective

Research the microbial trait **mesophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/mesophilic.yaml`.

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


## Microbial trait causal-graph report: **mesophilic** (METPO:1000615)

### Scope summary (trait meaning and boundaries)
**Mesophilic** refers to a microbial temperature preference in which growth is favored at intermediate temperatures, commonly described as ~**20–45 °C**. A 2023 review explicitly frames mesophiles as organisms that “grow between room temperature (around 20 °C) and about 45 °C” (Ramón et al., 2023, doi:10.1007/s42770-023-01057-4; https://doi.org/10.1007/s42770-023-01057-4) (ramon2023ageneraloverview pages 1-2).

**Trait scope for curation.** In TraitMech terms, mesophily is best treated as a **growth-range/optimum phenotype** (environmental preference) rather than a single pathway. Mechanistically, mesophilic growth across 20–45 °C is enabled by coordinated control of (i) membrane physical state (“homeoviscous adaptation”), (ii) proteostasis (chaperones/proteases), and (iii) transcriptional/post-transcriptional thermosensing (sigma factors, RNA thermometers), among others (ramon2023ageneraloverview pages 2-4, moon2023temperaturemattersbacterial pages 7-9, moon2023temperaturemattersbacterial pages 3-5).

**Boundary cases.** Definitions vary by study design. For example, ecological analyses may define mesophiles by an *upper* boundary near ~45 °C and omit a lower bound, effectively grouping psychrophiles/psychrotolerants into “mesophiles” for modeling convenience (ramon2023ageneraloverview pages 1-2). This is a warning flag for ontology curation: always record the operational definition used in the source.

---

### Key concepts and definitions (current understanding)

#### 1) Homeoviscous adaptation (HVA)
A central organizing concept is that temperature shifts change membrane viscosity/phase behavior, and cells remodel lipids to keep membrane function within a viable physical regime. Ramón et al. summarize that low-temperature growth is supported by changes that “increase unsaturation” and by incorporation of “monounsaturated (cis) fatty acids,” alongside chain shortening, branched-chain lipids, and other lipid-class changes (ramon2023ageneraloverview pages 2-4).

Moon et al. (2023) provide a mechanistic overview in which membrane fatty-acid saturation changes oppositely in heat vs cold stress (schematized in Figure 2), consistent with HVA (moon2023temperaturemattersbacterial media 4ee4e3d5, moon2023temperaturemattersbacterial media 3a9de447).

#### 2) Heat-shock and cold-shock regulons
Bacteria employ canonical heat- and cold-shock systems within the mesophilic range (e.g., E. coli and Bacillus responses relevant to ~20–45 °C). Moon et al. describe heat-shock regulation centered on sigma factors (RpoH/σ32, RpoE/σ24), and note post-transcriptional thermosensing via RNA structures (RNA thermometers) controlling translation of heat-shock genes (moon2023temperaturemattersbacterial pages 3-5). Cold-shock responses include strong induction of cold shock proteins (e.g., CspA) that act as RNA chaperones to mitigate inhibitory RNA secondary structures (moon2023temperaturemattersbacterial pages 3-5).

#### 3) Membrane state as an upstream “thermosensor”
Beyond passive physics, membranes can drive signal transduction. Moon et al. report that the Bacillus subtilis two-component system **DesK/DesR** responds to membrane physical state changes when temperature falls “37→20 °C,” with DesK phosphorylating DesR, which activates transcription of a Δ5-desaturase (des) that changes fatty-acid unsaturation (moon2023temperaturemattersbacterial pages 7-9).

---

### Candidate causal-graph nodes (grouped by type)

#### A) Environmental / experimental factors
- Temperature (ambient/incubation temperature; cooling; heat shock) (ramon2023ageneraloverview pages 1-2, moon2023temperaturemattersbacterial pages 3-5)
- Heat shock example condition: ~42 °C for E. coli heat-shock phenotypes (moon2023temperaturemattersbacterial pages 9-10)
- Cooling example condition: 37→20 °C shift (B. subtilis DesK/DesR) (moon2023temperaturemattersbacterial pages 7-9)

#### B) Phenotypes / assays
- Growth favored at intermediate temperatures (~20–45 °C) (ramon2023ageneraloverview pages 1-2)
- Membrane fluidity / membrane physical state (homeoviscous adaptation) (ramon2023ageneraloverview pages 2-4, moon2023temperaturemattersbacterial media 4ee4e3d5)
- Temperature stress resistance (heat tolerance; cold tolerance) (moon2023temperaturemattersbacterial pages 3-5)
- Application phenotype: aerobic denitrification at low temperature (nitrate removal; nitrogen removal rate) (yang2023insightintothe pages 1-2)

#### C) Membrane lipid entities and processes
- Unsaturated fatty acids (increased in cold; decreased saturation) (ramon2023ageneraloverview pages 2-4, moon2023temperaturemattersbacterial media 4ee4e3d5)
- Specific fatty acids in E. coli: palmitic acid (16:0), cis-palmitoleic (16:1 Δ9), cis-vaccenic (18:1 Δ11); “only cis-vaccenic acid content increases” upon cooling (ramon2023ageneraloverview pages 2-4)
- Palmitoleic acid (C16:1) increase at 18 °C in multiple A. baumannii strains (dessenne2024lipidomicanalysesreveal pages 1-2)
- Phospholipid classes implicated (PE, PG, etc.) in temperature-dependent remodeling (A. baumannii) (dessenne2024lipidomicanalysesreveal pages 1-2)

#### D) Regulatory systems (genes/proteins; label-grounded)
- **Two-component system:** DesK (sensor kinase) → DesR (response regulator) → des (Δ5-desaturase) (B. subtilis) (moon2023temperaturemattersbacterial pages 7-9)
- **Heat shock sigma factors:** RpoH/σ32; RpoE/σ24; anti-sigma factors (RseAB) (moon2023temperaturemattersbacterial pages 3-5, moon2023temperaturemattersbacterial pages 1-3)
- **Cold shock proteins:** CspA (RNA chaperone) (moon2023temperaturemattersbacterial pages 3-5)
- **RNA helicase:** CsdA (supports translation under cold shock by ribosome association) (moon2023temperaturemattersbacterial pages 7-9)
- **Chaperone/protease network:** DnaK; proteases FtsH, ClpXP, Lon (controls σ32 and clears heat-aggregated proteins) (moon2023temperaturemattersbacterial pages 3-5)
- **Stationary-phase/low-temperature regulator:** RpoS controlling otsAB induction (trehalose biosynthesis) (moon2023temperaturemattersbacterial pages 9-10)

#### E) Chemicals / metabolites (stress protectants)
- Trehalose (compatible solute; membrane/protein stabilizer) (moon2023temperaturemattersbacterial pages 9-10)

#### F) Transport and metabolism (application-oriented)
- ABC transporters (upregulated at low temperature in Bacillus simplex H-b; linked to nitrate removal) (yang2023insightintothe pages 1-2, yang2023insightintothe pages 7-10)

---

### Evidence-backed candidate causal edges (curation table)
The following table is designed for direct translation into a candidate TraitMech causal graph (subject–predicate–object with snippet-backed evidence and grounding where feasible).

| Edge (subject—predicate—object) | Edge type | Suggested ontology grounding | Evidence source (first author year, DOI, URL) | Publication date (month/year if known) | Supporting snippet (short quote) | Notes/curation strength (strong/uncertain; taxon-specific) |
|---|---|---|---|---|---|---|
| temperature decrease — increases — unsaturated fatty acids | physiology | temperature decrease; unsaturated fatty acid [CHEBI:35566] | Ramón 2023, doi:10.1007/s42770-023-01057-4, https://doi.org/10.1007/s42770-023-01057-4 | 07/2023 | “The most common adaptation… is the incorporation of monounsaturated (cis) fatty acids” and low-temperature adaptation includes “increase unsaturation” of membrane acyl chains. (ramon2023ageneraloverview pages 2-4, ramon2023ageneraloverview pages 1-2) | Strong for broad bacterial cold adaptation/homeoviscous adaptation; supports mesophile cooling response but not uniquely mesophilic. |
| cooling / membrane rigidification — sensed by — DesK | regulation | cooling; membrane physical state; DesK sensor histidine kinase [label]; GO:0007165 | Moon 2023, doi:10.1007/s12275-023-00031-x, https://doi.org/10.1007/s12275-023-00031-x | 03/2023 | “DesK senses membrane physical state (37→20 °C)” in *Bacillus subtilis*. (moon2023temperaturemattersbacterial pages 7-9) | Strong, but taxon-specific to *B. subtilis*. |
| DesK — phosphorylates/activates — DesR | regulation | DesK [label]; DesR response regulator [label]; protein phosphorylation [GO:0006468] | Moon 2023, doi:10.1007/s12275-023-00031-x, https://doi.org/10.1007/s12275-023-00031-x | 03/2023 | “DesK senses membrane physical state (37→20 °C) and phosphorylates DesR.” (moon2023temperaturemattersbacterial pages 7-9) | Strong, taxon-specific to *B. subtilis* two-component system. |
| DesR — activates transcription of — des (Δ5-desaturase) | regulation | DesR [label]; des / Δ5-desaturase [label]; fatty acid desaturase activity [GO:0006636 as process-level related] | Moon 2023, doi:10.1007/s12275-023-00031-x, https://doi.org/10.1007/s12275-023-00031-x | 03/2023 | “DesK… phosphorylates DesR, which activates des (D5-desaturase) transcription.” (moon2023temperaturemattersbacterial pages 7-9) | Strong, taxon-specific; useful mechanistic edge for homeoviscous adaptation. |
| cooling in *Escherichia coli* — increases — cis-vaccenic acid | molecular | NCBITaxon:562; cis-vaccenic acid [label]; membrane lipid remodeling [label] | Ramón 2023, doi:10.1007/s42770-023-01057-4, https://doi.org/10.1007/s42770-023-01057-4 | 07/2023 | In *E. coli* phospholipids, “only cis-vaccenic acid content increases” when temperature drops. (ramon2023ageneraloverview pages 2-4) | Strong, species-specific example of mesophile cooling adaptation. |
| cold shock — induces — CspA | regulation | cold shock [label]; CspA [label]; RNA chaperone activity [GO:0003723 related] | Moon 2023, doi:10.1007/s12275-023-00031-x, https://doi.org/10.1007/s12275-023-00031-x | 03/2023 | “Cold shock responses include induction of Csp proteins (notably CspA ~15% of protein synthesis after cold shock).” (moon2023temperaturemattersbacterial pages 3-5) | Strong, especially in *E. coli* and related bacteria. |
| CspA — promotes — translation during cold shock | molecular | CspA [label]; translation [GO:0006412] | Moon 2023, doi:10.1007/s12275-023-00031-x, https://doi.org/10.1007/s12275-023-00031-x | 03/2023 | “CspA acts as an RNA chaperone preventing RNA secondary structures”; “bind/unwind RNA to promote single-strandedness and translation.” (moon2023temperaturemattersbacterial pages 7-9, moon2023temperaturemattersbacterial pages 3-5) | Strong for cold-shock mechanism; not mesophile-exclusive. |
| heat shock — induces — σ32/RpoH | regulation | heat shock [label]; rpoH/σ32 [label]; sigma factor activity [GO:0016987] | Moon 2023, doi:10.1007/s12275-023-00031-x, https://doi.org/10.1007/s12275-023-00031-x | 03/2023 | “Heat shock regulation centers on sigma factors RpoH (σ32)….” and “heat-induced synthesis of σ32 (rpoH) regulated via rpoH mRNA secondary structure.” (moon2023temperaturemattersbacterial pages 3-5, moon2023temperaturemattersbacterial pages 12-13) | Strong, canonical bacterial heat-shock regulation relevant to mesophiles near upper range. |
| σ32/RpoH — activates expression of — heat shock genes | regulation | rpoH/σ32 [label]; heat shock gene expression [label] | Moon 2023, doi:10.1007/s12275-023-00031-x, https://doi.org/10.1007/s12275-023-00031-x | 03/2023 | “Heat shock regulation centers on sigma factors RpoH (σ32)” and RNA thermometers “control translation initiation of heat-shock genes.” (moon2023temperaturemattersbacterial pages 3-5) | Strong but somewhat generalized in review wording; acceptable regulatory edge. |
| DnaK — negatively regulates via sequestration — RpoH/σ32 | regulation | DnaK [label]; rpoH/σ32 [label]; negative regulation of transcription factor activity [label] | Moon 2023, doi:10.1007/s12275-023-00031-x, https://doi.org/10.1007/s12275-023-00031-x | 03/2023 | “RpoH is controlled by… DnaK chaperone sequestration.” (moon2023temperaturemattersbacterial pages 3-5) | Strong, canonical mechanism in Gram-negative bacteria; wording implies indirect negative regulation. |
| RpoS-dependent otsAB trehalose synthesis — increases — trehalose | regulation | RpoS [label]; otsA [label]; otsB [label]; trehalose [CHEBI:16589] | Moon 2023, doi:10.1007/s12275-023-00031-x, https://doi.org/10.1007/s12275-023-00031-x | 03/2023 | “The otsAB operon… is induced by osmotic stress, cold shock, and stationary phase in an RpoS-dependent manner.” (moon2023temperaturemattersbacterial pages 9-10) | Strong in *E. coli*; operon/gene grounding clear at label level. |
| trehalose — stabilizes — membranes and proteins | physiology | trehalose [CHEBI:16589]; membrane stabilization [label]; protein stabilization [label] | Moon 2023, doi:10.1007/s12275-023-00031-x, https://doi.org/10.1007/s12275-023-00031-x | 03/2023 | “Trehalose can insert into membranes to stabilize them” and “stabilize proteins.” (moon2023temperaturemattersbacterial pages 9-10) | Strong physiological edge, though broader stress protection rather than mesophile-specific. |
| growth at 18°C in *Acinetobacter baumannii* — increases — palmitoleic acid (C16:1) | molecular | NCBITaxon:470; palmitoleic acid [CHEBI:32395] | Dessenne 2024, doi:10.1128/spectrum.00757-24, https://doi.org/10.1128/spectrum.00757-24 | 10/2024 | “At 18°C, five strains consistently show an increase in palmitoleic acid (C16:1).” (dessenne2024lipidomicanalysesreveal pages 1-2) | Strong primary-data edge, but strain-specific within *A. baumannii*. |
| low temperature / cold denitrification at 5–10°C — upregulates — ABC transporters | regulation | low temperature [label]; ABC transporter complex [GO:0043190 related / label] | Yang 2023, doi:10.1128/aem.01928-22, https://doi.org/10.1128/aem.01928-22 | 02/2023 | “the corresponding driving force for nitrate removal at 10°C was mainly attributed to the overexpression of ABC transporters” and low-temperature adaptation involved “adjustment of membrane transport.” (yang2023insightintothe pages 1-2, yang2023insightintothe pages 7-10) | Strong for *Bacillus simplex* H-b under cold denitrification; assay-specific. |
| ABC transporter upregulation at low temperature — contributes to — nitrate removal | physiology | ABC transporter [label]; nitrate removal [label] | Yang 2023, doi:10.1128/aem.01928-22, https://doi.org/10.1128/aem.01928-22 | 02/2023 | “the corresponding driving force for nitrate removal at 10°C was mainly attributed to the overexpression of ABC transporters.” (yang2023insightintothe pages 1-2) | Strong but application-specific; retain uncertainty if curating as general mesophile mechanism. |
| low temperature (5°C) — permits with adaptation — relatively high nitrogen removal rate (27.22%) | physiology | 5 °C [label]; nitrogen removal [label] | Yang 2023, doi:10.1128/aem.01928-22, https://doi.org/10.1128/aem.01928-22 | 02/2023 | “relatively high nitrogen removal rate (27.22%) of strain H-b at 5°C.” (yang2023insightintothe pages 1-2) | Strong quantitative phenotype, but trait-to-application edge is assay- and strain-specific rather than core mesophile definition. |


*Table: This table compiles candidate mechanistic and regulatory edges relevant to the mesophilic trait, emphasizing temperature-response systems and membrane adaptation with source-backed snippets. It is useful as a starting point for curating TraitMech nodes and edges, while flagging taxon-specific or assay-specific claims.*

---

### Recent developments and latest research (prioritizing 2023–2024)

1) **Integrated “multi-layer” temperature response frameworks (2023 review).** Moon et al. (Mar 2023) synthesize how mesophile-relevant temperature shifts are sensed and mitigated across DNA topology, RNA structure/processing, membrane remodeling, and proteostasis—including concrete regulatory chains (σ factors; DnaK/FtsH/ClpXP control of σ32; DesK/DesR for membrane sensing) (moon2023temperaturemattersbacterial pages 3-5, moon2023temperaturemattersbacterial pages 7-9).

2) **Lipidomics-based strain comparisons (2024 primary study).** Dessenne et al. (Oct 2024) use LC-HRMS/MS lipidomics to show strain-specific homeoviscous responses in *Acinetobacter baumannii* when comparing **18 °C vs 37 °C**, including consistent increase of **C16:1** in five strains and identification of candidate enzymatic determinants (FabA presence in some strains; candidate desaturases) (dessenne2024lipidomicanalysesreveal pages 1-2). This is directly actionable for causal graphs linking temperature → lipid remodeling → membrane function.

3) **Systems-level cold adaptation tied to real-world function (2023 primary study).** Yang et al. (Feb 2023) analyze aerobic denitrification by *Bacillus simplex* H-b at **5 °C, 20 °C, 30 °C**, associating cold performance with combined responses including higher unsaturated fatty acids and transporter/regulatory shifts; they report a “relatively high nitrogen removal rate (27.22%) … at 5 °C” and connect nitrate-removal driving force at **10 °C** to **ABC transporter overexpression** (yang2023insightintothe pages 1-2).

4) **Quantitative kinetics of lipidome adaptation (2023 preprint).** Safronova et al. (Nov 2023) present a time-resolved view of lipidome adaptation after temperature downshift, including a two-stage response (rapid cholesterol efflux then gradual acyl-chain remodeling) and quantitative changes in mol% of lipid classes/sterols (e.g., ~7 mol% cholesterol decrease and ~10 mol% PC change over hours) (safronova2023fromhotto pages 8-10). Because this is a preprint, it should be curated with an “uncertain” flag unless independently corroborated.

---

### Current applications and real-world implementations

1) **Wastewater nitrogen removal in cold conditions.** Cold-tolerant/psychrotolerant denitrifiers are of practical interest for nitrogen-contaminated wastewater treatment in cold climates. Yang et al. provide a specific example where aerobic denitrification at **5 °C** remains measurable (27.22% nitrogen removal rate) and is linked to molecular adaptations including membrane unsaturation changes and transporter overexpression (yang2023insightintothe pages 1-2). These data support curation of edges connecting temperature stress → membrane remodeling/transport rewiring → maintained metabolism under suboptimal temperatures, although this is not exclusive to mesophiles.

2) **Clinical/environmental persistence of opportunistic pathogens.** Temperature-driven lipid remodeling in *A. baumannii* (18 vs 37 °C) may support survival outside host settings, contributing to environmental fitness and dissemination (dessenne2024lipidomicanalysesreveal pages 1-2). This is a “real-world” implementation context: the same membrane adaptation machinery potentially affects persistence across hospital and ambient environments.

---

### Expert opinions and authoritative synthesis

- Ramón et al. frame cold adaptation as **multifactorial**, highlighting membrane remodeling, temperature-adapted proteins/enzymes, and regulatory changes (including two-component signaling triggered by membrane state) as core strategies; this provides a curation rationale that mesophily emerges from multiple interacting modules rather than a single defining mechanism (ramon2023ageneraloverview pages 1-2, ramon2023ageneraloverview pages 2-4).

- Moon et al. provide an authoritative, highly cited 2023 synthesis emphasizing that bacteria use layered regulation (DNA/RNA thermosensing, sigma factors, chaperones, membrane remodeling) to withstand temperature transitions within the mesophilic regime (moon2023temperaturemattersbacterial pages 3-5, moon2023temperaturemattersbacterial pages 7-9).

---

### Relevant recent statistics and data points (from included sources)
- **Mesophile definition anchor:** mesophiles “grow between room temperature (around 20 °C) and about 45 °C” (ramon2023ageneraloverview pages 1-2).
- **Specific regulatory temperature shift:** DesK/DesR system responds to “37→20 °C” (moon2023temperaturemattersbacterial pages 7-9).
- **Heat-shock example temperature:** heat shock at “42 °C” associated with RNase E BR-body formation (moon2023temperaturemattersbacterial pages 9-10).
- **Quantitative application outcome:** aerobic denitrifier *Bacillus simplex* H-b shows “nitrogen removal rate (27.22%) … at 5 °C” (yang2023insightintothe pages 1-2).
- **Quantitative lipid change (strain-dependent):** at **18 °C**, five *A. baumannii* strains increase palmitoleic acid (C16:1) (dessenne2024lipidomicanalysesreveal pages 1-2).
- **Visual evidence (schematic, but explicit directionality):** Moon et al. Figure 2 panel on membrane fatty acids depicts increased saturated fatty acids under heat stress and reduced saturated fatty acids under cold stress (moon2023temperaturemattersbacterial media 4ee4e3d5, moon2023temperaturemattersbacterial media 3a9de447).

---

### Warnings / items not yet safe to curate into TraitMech

1) **Not mesophile-exclusive.** Many mechanisms listed (HVA, heat-shock/cold-shock regulons, trehalose protection) are general bacterial stress systems and should be curated as **temperature-response mechanisms**, not as *defining* mesophily determinants (moon2023temperaturemattersbacterial pages 3-5, ramon2023ageneraloverview pages 2-4).

2) **Taxon-specific edges.** DesK/DesR (B. subtilis) and the specific *E. coli* fatty-acid species shift (cis-vaccenic acid increase) are strong mechanistic examples but should be tagged **taxon-specific** unless generalized via additional sources (moon2023temperaturemattersbacterial pages 7-9, ramon2023ageneraloverview pages 2-4).

3) **Assay/application specificity.** ABC-transporter–driven nitrate removal at 10 °C and nitrogen removal rate at 5 °C are compelling, quantitative phenotypes for a denitrification application, but not core to mesophily; curate with **assay-specific** or “application-context” flags (yang2023insightintothe pages 1-2).

4) **Preprint status.** Safronova et al. (2023 bioRxiv) contains useful quantitative lipidome-kinetics claims but should be curated as **uncertain** until peer-reviewed or corroborated (safronova2023fromhotto pages 8-10).

---

## DOI-first bibliography (with URLs; publication dates where available)

1) Moon S, Ham S, Jeong J, et al. **Temperature Matters: Bacterial Response to Temperature Change.** *Journal of Microbiology.* **Mar 2023.** doi:10.1007/s12275-023-00031-x. https://doi.org/10.1007/s12275-023-00031-x (moon2023temperaturemattersbacterial pages 3-5, moon2023temperaturemattersbacterial pages 7-9, moon2023temperaturemattersbacterial pages 9-10, moon2023temperaturemattersbacterial media 4ee4e3d5)

2) Ramón A, Esteves A, Villadóniga C, et al. **A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies.** *Brazilian Journal of Microbiology.* **Jul 2023.** doi:10.1007/s42770-023-01057-4. https://doi.org/10.1007/s42770-023-01057-4 (ramon2023ageneraloverview pages 1-2, ramon2023ageneraloverview pages 2-4)

3) Yang Q, Shi Y, Xin Y, et al. **Insight into the Cold Adaptation Mechanism of an Aerobic Denitrifying Bacterium: Bacillus simplex H-b.** *Applied and Environmental Microbiology.* **Feb 2023.** doi:10.1128/aem.01928-22. https://doi.org/10.1128/aem.01928-22 (yang2023insightintothe pages 1-2, yang2023insightintothe pages 7-10)

4) Dessenne C, Ménart B, Acket S, et al. **Lipidomic analyses reveal distinctive variations in homeoviscous adaptation among clinical strains of Acinetobacter baumannii.** *Microbiology Spectrum.* **Oct 2024.** doi:10.1128/spectrum.00757-24. https://doi.org/10.1128/spectrum.00757-24 (dessenne2024lipidomicanalysesreveal pages 1-2)

5) Safronova N, Junghans L, Saenz JP. **From hot to cold: dissecting lipidome adaptation in Mycoplasma mycoides and the Minimal Cell JCVI-Syn3B.** *bioRxiv.* **Nov 2023.** doi:10.1101/2023.11.10.566608. https://doi.org/10.1101/2023.11.10.566608 (preprint) (safronova2023fromhotto pages 8-10)

6) Purwar S, Srivastava S. **Adaptations of Psychrophilic Microorganism to Low-Temperature Environments.** *Applied Microbiology: Theory & Technology.* **Oct 2024.** doi:10.37256/amtt.5220244537. https://doi.org/10.37256/amtt.5220244537 (purwar2024adaptationsofpsychrophilic pages 6-7)


References

1. (ramon2023ageneraloverview pages 1-2): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

2. (ramon2023ageneraloverview pages 2-4): Ana Ramón, Adriana Esteves, Carolina Villadóniga, Cora Chalar, and Susana Castro-Sowinski. A general overview of the multifactorial adaptation to cold: biochemical mechanisms and strategies. Brazilian Journal of Microbiology, 54:2259-2287, Jul 2023. URL: https://doi.org/10.1007/s42770-023-01057-4, doi:10.1007/s42770-023-01057-4. This article has 19 citations and is from a peer-reviewed journal.

3. (moon2023temperaturemattersbacterial pages 7-9): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 98 citations and is from a peer-reviewed journal.

4. (moon2023temperaturemattersbacterial pages 3-5): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 98 citations and is from a peer-reviewed journal.

5. (moon2023temperaturemattersbacterial media 4ee4e3d5): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 98 citations and is from a peer-reviewed journal.

6. (moon2023temperaturemattersbacterial media 3a9de447): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 98 citations and is from a peer-reviewed journal.

7. (moon2023temperaturemattersbacterial pages 9-10): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 98 citations and is from a peer-reviewed journal.

8. (yang2023insightintothe pages 1-2): Qian Yang, Yi Shi, Yu Xin, Ting Yang, Liang Zhang, Zhenghua Gu, Youran Li, Zhongyang Ding, and Guiyang Shi. Insight into the cold adaptation mechanism of an aerobic denitrifying bacterium: bacillus simplex h-b. Feb 2023. URL: https://doi.org/10.1128/aem.01928-22, doi:10.1128/aem.01928-22. This article has 16 citations and is from a peer-reviewed journal.

9. (dessenne2024lipidomicanalysesreveal pages 1-2): Clara Dessenne, Benoît Ménart, Sébastien Acket, Gisèle Dewulf, Yann Guerardel, Olivier Vidal, and Yannick Rossez. Lipidomic analyses reveal distinctive variations in homeoviscous adaptation among clinical strains of <i>acinetobacter baumannii</i> , providing insights from an environmental adaptation perspective. Oct 2024. URL: https://doi.org/10.1128/spectrum.00757-24, doi:10.1128/spectrum.00757-24. This article has 7 citations and is from a domain leading peer-reviewed journal.

10. (moon2023temperaturemattersbacterial pages 1-3): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 98 citations and is from a peer-reviewed journal.

11. (yang2023insightintothe pages 7-10): Qian Yang, Yi Shi, Yu Xin, Ting Yang, Liang Zhang, Zhenghua Gu, Youran Li, Zhongyang Ding, and Guiyang Shi. Insight into the cold adaptation mechanism of an aerobic denitrifying bacterium: bacillus simplex h-b. Feb 2023. URL: https://doi.org/10.1128/aem.01928-22, doi:10.1128/aem.01928-22. This article has 16 citations and is from a peer-reviewed journal.

12. (moon2023temperaturemattersbacterial pages 12-13): Seongjoon Moon, Soojeong Ham, Juwon Jeong, Heechan Ku, Hyunhee Kim, and Changhan Lee. Temperature matters: bacterial response to temperature change. Journal of Microbiology, 61:343-357, Mar 2023. URL: https://doi.org/10.1007/s12275-023-00031-x, doi:10.1007/s12275-023-00031-x. This article has 98 citations and is from a peer-reviewed journal.

13. (safronova2023fromhotto pages 8-10): Nataliya Safronova, Lisa Junghans, and James P Saenz. From hot to cold: dissecting lipidome adaptation in mycoplasma mycoides and the minimal cell jcvi-syn3b. bioRxiv, Nov 2023. URL: https://doi.org/10.1101/2023.11.10.566608, doi:10.1101/2023.11.10.566608. This article has 1 citations.

14. (purwar2024adaptationsofpsychrophilic pages 6-7): Shalini Purwar and Shaili Srivastava. Adaptations of psychrophilic microorganism to low-temperature environments. Applied Microbiology: Theory ＆ Technology, pages 168-188, Oct 2024. URL: https://doi.org/10.37256/amtt.5220244537, doi:10.37256/amtt.5220244537. This article has 7 citations.