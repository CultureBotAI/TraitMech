---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T10:09:59.665933'
end_time: '2026-06-18T10:24:31.921188'
duration_seconds: 872.26
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: swarming motility
  trait_identifier: traitmech:000062
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: swarming_motility
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A flagella-dependent, multicellular surface motility in which cells
    move rapidly and coordinately across a surface, typically accompanied by hyperflagellation
    and secretion of a wetting surfactant.
  parent_traits: METPO:1000702
  synonyms: swarming
  evidence_summary: 'DOI:10.1038/nrmicro2405:  (Kearns, "A field guide to bacterial
    swarming motility", defines swarming via increased flagella per cell, surfactant
    secretion, and movement in multicellular groups.) | DOI:10.1146/annurev.micro.57.030502.091014:  (Harshey,
    "Bacterial motility on a surface", places swarming among the surface-motility
    modes of bacteria.)'
  causal_graph_summary: 'swarming_hyperflagellation_surfactant: 4 nodes, 3 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 32
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** swarming motility
- **METPO identifier:** traitmech:000062
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A flagella-dependent, multicellular surface motility in which cells move rapidly and coordinately across a surface, typically accompanied by hyperflagellation and secretion of a wetting surfactant.
- **Parent traits:** METPO:1000702
- **Synonyms:** swarming
- **Existing evidence:** DOI:10.1038/nrmicro2405:  (Kearns, "A field guide to bacterial swarming motility", defines swarming via increased flagella per cell, surfactant secretion, and movement in multicellular groups.) | DOI:10.1146/annurev.micro.57.030502.091014:  (Harshey, "Bacterial motility on a surface", places swarming among the surface-motility modes of bacteria.)
- **Existing causal graph summary:** swarming_hyperflagellation_surfactant: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **swarming motility** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/swarming_motility.yaml`.

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
- **Trait label:** swarming motility
- **METPO identifier:** traitmech:000062
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A flagella-dependent, multicellular surface motility in which cells move rapidly and coordinately across a surface, typically accompanied by hyperflagellation and secretion of a wetting surfactant.
- **Parent traits:** METPO:1000702
- **Synonyms:** swarming
- **Existing evidence:** DOI:10.1038/nrmicro2405:  (Kearns, "A field guide to bacterial swarming motility", defines swarming via increased flagella per cell, surfactant secretion, and movement in multicellular groups.) | DOI:10.1146/annurev.micro.57.030502.091014:  (Harshey, "Bacterial motility on a surface", places swarming among the surface-motility modes of bacteria.)
- **Existing causal graph summary:** swarming_hyperflagellation_surfactant: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **swarming motility** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/swarming_motility.yaml`.

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


# Research Report: Swarming Motility (TraitMech / METPO)

**Target trait:** swarming motility (METPO identifier: traitmech:000062; category: MORPHOLOGY; class)  
**Working definition (curation scope):** a *flagella-dependent*, multicellular/collective surface motility on semi-solid substrates, typically requiring a wetting agent/biosurfactant to reduce surface tension and enable rapid coordinated expansion (often with tendrils), and frequently regulated by density-dependent signaling (quorum sensing) and intracellular second messengers (e.g., c-di-GMP). (bru2023swarmingofp. pages 1-2, warrell2024interspeciessurfactantsserve pages 1-2, zegadło2023bacterialmotilityand pages 4-5)

## 1) Trait scope (phenotype boundaries)

### 1.1 What the trait represents
Swarming is best treated as an *assay-observed collective surface migration phenotype* on semi-solid media, arising from coordinated behavior of many cells (often forming macroscopic patterns such as tendrils) and enabled by flagellar activity plus surfactant-mediated wetting in many taxa (especially *Pseudomonas*). (bru2023swarmingofp. pages 1-2, warrell2024interspeciessurfactantsserve pages 1-2)

A mechanistic and operational nuance emphasized in recent work is that “true swarming” may involve **volumetric expansion** (an increase in the liquid/biomass volume of the colony via influx of fluid and nutrients from the agar), distinguishing it from mere outward spreading without volume change. (bru2023swarmingofp. pages 11-12)

### 1.2 Distinguishing swarming from nearby traits
Swarming should be separated from other surface/near-surface motilities that may generate superficially similar colony expansion:

- **Swimming:** individual, flagella-driven movement in liquid; run/reorientation dynamics regulated by chemotaxis signaling. (zegadło2023bacterialmotilityand pages 4-5, zegadło2023bacterialmotilityand pages 2-4)
- **Twitching:** type IV pili (T4P) extension/retraction-driven movement, typically on harder surfaces. (warrell2024interspeciessurfactantsserve pages 1-2)
- **Sliding:** surface spreading that can occur without active motility appendages; in *P. aeruginosa*, summarized as requiring only rhamnolipids (surfactant) and no appendages—therefore not swarming under the trait’s flagella-dependent definition. (warrell2024interspeciessurfactantsserve pages 1-2, bru2023swarmingofp. pages 8-10)
- **Surfing (boundary case relevant to curation):** a mucin- (or exogenous surfactant-) enabled, flagella-dependent surface spreading that can occur with different regulation than canonical swarming; it may be mistaken for swarming in plate assays unless explicitly controlled for medium composition and regulators. (warrell2024interspeciessurfactantsserve pages 1-2)

### 1.3 Boundary cases / warnings for trait assignment
- **Mechanism convolution in Pseudomonas:** recent synthesis argues that *P. aeruginosa* “swarming” on plates may reflect a convolution of swarming- and sliding-like phases, so phenotype calls based solely on tendrils or colony size should be treated cautiously. (bru2023swarmingofp. pages 8-10)
- **Propulsion-independent surface spreading:** a 2024 preprint reports a propulsion-independent surface migration mechanism (“swashing”) in *E. coli* and *Salmonella*, underscoring that **surface expansion is not always flagella-driven** and that swarming should remain restricted to flagella-dependent phenotypes unless evidence indicates otherwise. (panich2024swashingmotilitya pages 13-15, panich2024swashingmotilitya pages 11-13)
- **Antimicrobial tolerance association (contextual, not a defining criterion):** swarming has been noted to be associated with greater resistance to antimicrobials in clinical contexts, but this should not be used as a mechanistic definition without direct experimental linkage in the organism/assay. (zegadło2023bacterialmotilityand pages 1-2)

## 2) Current understanding: key mechanistic concepts

### 2.1 Core requirement: flagellar activity + wetting agents (many taxa)
For *Pseudomonas aeruginosa* and many pseudomonads, swarming is summarized as requiring **flagella** and **rhamnolipid (RL) biosurfactant production**; tendrils and expansion are disrupted in RL-defective mutants. (bru2023swarmingofp. pages 1-2, bru2023swarmingofp. pages 2-3, warrell2024interspeciessurfactantsserve pages 1-2)

In *P. aeruginosa*, RLs and the rhamnolipid precursors/related molecules (e.g., HAAs) are treated as surfactants that reduce surface tension and contribute to forming a liquid-like zone associated with tendril growth. (bru2023swarmingofp. pages 2-3, bru2023swarmingofp. pages 1-2)

### 2.2 Regulatory control: quorum sensing and c-di-GMP as “mode switches”
Recent reviews emphasize that surfactant production (e.g., HAAs/RLs) can be **quorum-sensing regulated**, preventing swarming until high cell density. (bru2023swarmingofp. pages 11-12, bru2023swarmingofp. pages 2-3)

In *P. aeruginosa*, the **c-di-GMP network** is directly integrated with flagellar stator usage and swarming, via mechanistic links summarized as: FlgZ (a c-di-GMP effector) binding MotC to block MotCD recruitment and MotC interacting with SadC to increase c-di-GMP, creating feedback between stator composition and signaling. (anda2024howp.aeruginosa pages 13-14)

### 2.3 Biophysics and fluid mechanics (mechanistic hypotheses to curate cautiously)
A 2023 biophysics-oriented review argues that outward expansion cannot be explained solely by growth and flagellar motility; it implicates **fluid influx from agar**, **surface tension**, **osmolarity**, and **viscosity** as key variables, and discusses models including Marangoni flow and pressure-driven flow due to osmolyte accumulation. These are valuable *mechanistic hypotheses* but are not always directly tested causal links and should be flagged as uncertain edges. (bru2023swarmingofp. pages 2-3, bru2023swarmingofp. pages 11-12)

## 3) Recent developments (prioritizing 2023–2024)

### 3.1 Quantitative control of swarming by flagellar stator composition (mBio 2024)
A 2024 study on *P. aeruginosa* quantified how mixed populations with different stator configurations can collectively swarm. Key quantitative findings include:

- **MotAB-only motor:** ~13% flagellum-active cells and **swarming-deficient**. (anda2024howp.aeruginosa pages 8-10)
- **WT vs MotCD-only activity:** WT alone ~50% active flagella; MotCD-only ~90% active flagella. (anda2024howp.aeruginosa pages 8-10)
- **Swarming onset in mixtures:** MotCD swarming onset occurred when MotCD cells were ~0.1–0.3 of the population; estimated active-flagella fractions at swarming onset were ~0.18 (MotCD mixes) and ~0.15 (WT mixes). (anda2024howp.aeruginosa pages 8-10)
- **Stator induction effects:** MotCD overexpression (1% arabinose) increased swarming area by ~40% vs vector; MotAB induction in a MotCD background progressively reduced swarming and at 0.2% arabinose arrested swarming. (anda2024howp.aeruginosa pages 8-10)

Interpretation for TraitMech curation: **flagellar motor stator selection and the active-motile fraction** are candidate mechanistic nodes controlling swarming performance, and c-di-GMP-stator feedback offers a mechanistic bridge between signaling and physical motility output. (anda2024howp.aeruginosa pages 8-10, anda2024howp.aeruginosa pages 13-14)

### 3.2 Gac/Rsm pathway and biosurfactant identity in *P. fluorescens* (Microbiology Spectrum 2024)
A 2024 genetic study in *P. fluorescens* Pf0-1 shows that swarming capability can be “unmasked” by regulatory rewiring:

- Swarming is described as coordinated surface movement generally requiring a functional flagellum plus a wetting agent/biosurfactant. (pastora2024multiplepathwaysimpact pages 1-3)
- A ΔrsmA ΔrsmE ΔrsmI mutant (mimicking Gac/Rsm overstimulation) became **proficient at swarming**, supporting Rsm proteins as key repressors of swarming via effects on biosurfactant production/secretion. (pastora2024multiplepathwaysimpact pages 1-3)
- The alternative sigma factor **FliA** was required for swimming and swarming, consistent with its role in flagellar function. (pastora2024multiplepathwaysimpact pages 5-7)
- The cyclic lipopeptide **Gacamide A** was implicated as the biosurfactant utilized for swarming; mutants in Gacamide A biosynthesis or secretion impaired swarming, and exogenous addition promoted swarming. (pastora2024multiplepathwaysimpact pages 5-7)

Interpretation: swarming is not only “flagella + surfactant” but also a **regulatory state**, and the specific biosurfactant can be organism/strain-specific (e.g., RLs vs Gacamide A). (pastora2024multiplepathwaysimpact pages 5-7, bru2023swarmingofp. pages 1-2)

### 3.3 Interspecies/public-good surfactants change surface motility mode (J Bacteriology 2024)
A 2024 study demonstrated that exogenous surfactants from other microbes/hosts can enable *P. aeruginosa* surface spreading even on hard agar. The motility remained **flagella-dependent**, but known regulators were not essential, suggesting an uncharacterized regulatory mechanism and emphasizing polymicrobial context as a modifier of swarming-related behaviors. (warrell2024interspeciessurfactantsserve pages 1-2)

## 4) Current applications and real-world implementations

### 4.1 Anti-virulence discovery screens using swarming assays (MethodsX 2024)
A 2024 MethodsX protocol optimized a **swarming motility assay** for *Vibrio parahaemolyticus* to enable reproducible screening of anti-virulence products. Key implementation details include: LB Lennox + 2% NaCl with **0.4% agar**, OD600 = 1.00 ± 0.01 standardized inoculum (reported as ~10^9 CFU/mL), **3 µL** inoculum, and **5 min** drying time; halo diameters were measured every 2 h over 24 h, with six replicates and five independent assays to estimate reproducibility. (pozo2024optimizedswarmingmotility pages 2-4)

Visual materials from this MethodsX paper (workflow, optimization tables, and representative swarming curves/halos) provide a ready-to-adopt implementation reference for laboratory standardization and are included as image evidence. (pozo2024optimizedswarmingmotility media 55e33928, pozo2024optimizedswarmingmotility media 2e70544b, pozo2024optimizedswarmingmotility media c478a897, pozo2024optimizedswarmingmotility media 7e88c879, pozo2024optimizedswarmingmotility media 9f2b1952)

### 4.2 Quorum sensing inhibition as a route to suppress swarming in MDR pathogens (Infection and Drug Resistance 2023)
In MDR *Acinetobacter baumannii*, the flavonoid **glabridin** was tested as a quorum sensing inhibitor:

- MICs across eight clinical MDR isolates: **512–1024 µg/mL**. (lin2023glabridinfunctionsas pages 1-2)
- At sub-MIC doses (1/4–1/2 MIC), glabridin reduced surface/swarming motility by ~**44.27%** (1/4 MIC) and ~**50.64%** (1/2 MIC) (both P < 0.05). (lin2023glabridinfunctionsas pages 1-2, lin2023glabridinfunctionsas pages 4-8)
- qRT-PCR showed downregulation of QS genes **abaI** (up to ~39.12%) and **abaR** (up to ~25.19%), supporting a plausible chain: QSI → reduced QS gene expression → reduced motility/biofilm. (lin2023glabridinfunctionsas pages 4-8)

### 4.3 Iron-responsive regulation of swarming linked to virulence (Frontiers Vet Sci 2023)
In *Vibrio splendidus*, Fur knockdown linked iron regulation to flagellar gene expression and swarming-associated phenotypes:

- **Vsflic** (flagellum assembly gene) downregulated to **0.56-fold** in the Fur knockdown mutant. (shi2023vibriosplendidusfur pages 1-2, shi2023vibriosplendidusfur pages 5-7)
- Swarming motility reduced (reported ~0.68-fold under iron-replete conditions), and colony diameter ~79–81% of wild-type. (shi2023vibriosplendidusfur pages 7-9)
- Strong virulence shift: LD50 of WT **9.116 × 10^6 CFU·mL−1** vs knockdown **1.658 × 10^11 CFU·mL−1** in *Apostichopus japonicus*. (shi2023vibriosplendidusfur pages 1-2, shi2023vibriosplendidusfur pages 5-7)

These results support applications in aquaculture pathogen control where perturbing iron-responsive regulation may alter motility/biofilm and thereby pathogenicity. (shi2023vibriosplendidusfur pages 1-2)

## 5) Candidate causal-graph nodes (grouped; grounding suggestions)

### 5.1 Phenotype node
- **Swarming motility** (TraitMech/METPO: traitmech:000062) — assay-observed collective surface motility (flagella-dependent). (bru2023swarmingofp. pages 1-2, zegadło2023bacterialmotilityand pages 4-5)

### 5.2 Cellular machines / processes
- **Flagellum-dependent motility** (GO: “flagellum-dependent cell motility” — candidate GO term; do not curate without confirming exact GO ID). (bru2023swarmingofp. pages 1-2, zegadło2023bacterialmotilityand pages 4-5)
- **Flagellar motor stators**: MotAB, MotCD (*P. aeruginosa*). (anda2024howp.aeruginosa pages 8-10)
- **Alternative sigma factor FliA** (flagellar gene regulation). (pastora2024multiplepathwaysimpact pages 5-7)

### 5.3 Regulatory systems
- **Gac/Rsm pathway**; **RsmA, RsmE, RsmI** (*P. fluorescens* Pf0-1). (pastora2024multiplepathwaysimpact pages 1-3)
- **Quorum sensing (QS)** (general; and organism-specific systems). (bru2023swarmingofp. pages 2-3, bru2023swarmingofp. pages 11-12)
- **c-di-GMP signaling**; effectors **FlgZ**, diguanylate cyclase **SadC** (*P. aeruginosa*). (anda2024howp.aeruginosa pages 13-14)
- **Fur (ferric uptake regulator)** (*Vibrio splendidus*; gene Vsfur). (shi2023vibriosplendidusfur pages 1-2)

### 5.4 Chemicals / metabolites / surfactants
- **Rhamnolipids (RLs)** and **HAAs** (biosurfactants; *P. aeruginosa*). Suggest CHEBI grounding for “rhamnolipid” at generic level (exact CHEBI ID to be selected during curation). (bru2023swarmingofp. pages 2-3, bru2023swarmingofp. pages 1-2)
- **Gacamide A** (cyclic lipopeptide biosurfactant; *P. fluorescens*). (pastora2024multiplepathwaysimpact pages 5-7)
- **Exogenous surfactants/public goods** (including cross-species surfactants affecting motility mode). (warrell2024interspeciessurfactantsserve pages 1-2)
- **Glabridin** (QS inhibitor; impacts swarming in MDR *A. baumannii*). (lin2023glabridinfunctionsas pages 1-2)

### 5.5 Environment / assay factors (ENVO-style candidates)
- **Semi-solid agar surface** (e.g., 0.4–0.5% agar for swarming assays; candidate ENVO term for agar substrate). (pozo2024optimizedswarmingmotility pages 2-4, pastora2024multiplepathwaysimpact pages 1-3)
- **Viscosity / surface hardness** as motility mode determinants. (warrell2024interspeciessurfactantsserve pages 1-2)
- **NaCl concentration** (e.g., 2% NaCl for *Vibrio* assay). (pozo2024optimizedswarmingmotility pages 2-4)
- **Plate drying time; inoculum volume** (assay calibration nodes). (pozo2024optimizedswarmingmotility pages 2-4, pozo2024optimizedswarmingmotility media 55e33928)

## 6) Candidate causal edges for TraitMech curation

The following table provides subject–predicate–object triples with evidence and curation notes.

| Edge (subject–predicate–object) | Evidence summary (1 sentence) | Snippet (short quote-like paraphrase from evidence) | Source (DOI, year, URL) | Notes/uncertainty (taxon-specific, assay-specific, inferred) |
|---|---|---|---|---|
| Gac/Rsm pathway activation – positively regulates – swarming motility | In *Pseudomonas fluorescens* Pf0-1, activating the Gac/Rsm output state enabled a previously swarming-deficient strain to swarm. | “Pf0-1 can swarm if the Gac/Rsm pathway is activated.” (pastora2024multiplepathwaysimpact pages 1-3, pastora2024multiplepathwaysimpact pages 5-7) | 10.1128/spectrum.00166-24, 2024, https://doi.org/10.1128/spectrum.00166-24 | Taxon-specific to Pf0-1; regulatory effect inferred from mutant phenocopies. |
| RsmA – negatively regulates – swarming motility | Loss of RsmA was identified as relieving repression of swarming in Pf0-1. | “RsmA and RsmE are key repressors of swarming motility.” (pastora2024multiplepathwaysimpact pages 1-3, pastora2024multiplepathwaysimpact pages 5-7) | 10.1128/spectrum.00166-24, 2024, https://doi.org/10.1128/spectrum.00166-24 | Taxon-specific; likely via biosurfactant control rather than direct motility machinery. |
| RsmE – negatively regulates – swarming motility | RsmE functioned with RsmA as a major negative regulator of swarming in the Pf0-1 screen. | “RsmA and RsmE play a key role in this regulation.” (pastora2024multiplepathwaysimpact pages 1-3, pastora2024multiplepathwaysimpact pages 5-7) | 10.1128/spectrum.00166-24, 2024, https://doi.org/10.1128/spectrum.00166-24 | Taxon-specific; mechanism linked to surfactant production/secretion. |
| FliA – positively regulates – swarming motility | Deletion of the alternative sigma factor *fliA* abolished swarming while leaving biosurfactant production unchanged, supporting a flagellar-function edge. | “Loss of FliA results in a defect in flagellar function and impacts swarming.” (pastora2024multiplepathwaysimpact pages 5-7) | 10.1128/spectrum.00166-24, 2024, https://doi.org/10.1128/spectrum.00166-24 | Strong for Pf0-1; likely general for flagellar systems but curate as taxon-backed. |
| FliA – positively regulates – swimming motility | The *fliA* mutant lost both swimming and swarming, indicating upstream control of flagellar motility. | “Deletion of FliA abolished both swimming and swarming.” (pastora2024multiplepathwaysimpact pages 5-7) | 10.1128/spectrum.00166-24, 2024, https://doi.org/10.1128/spectrum.00166-24 | Assay-specific readout on swim/swarm agar. |
| Gacamide A biosynthesis – positively regulates – swarming motility | Genetic disruption of the Gacamide A biosynthetic pathway reduced or abolished swarming in Pf0-1. | “Loss of genes linked to Gacamide A biosynthesis impacts swarming motility.” (pastora2024multiplepathwaysimpact pages 1-3, pastora2024multiplepathwaysimpact pages 5-7) | 10.1128/spectrum.00166-24, 2024, https://doi.org/10.1128/spectrum.00166-24 | Taxon-specific biosurfactant; node label may remain compound-name level if CHEBI unavailable. |
| gamA – positively regulates – Gacamide A production | Deletion of *gamA* reduced the biosurfactant zone and impaired swarming. | “gamA deletion reduced biosurfactant and swarming.” (pastora2024multiplepathwaysimpact pages 5-7) | 10.1128/spectrum.00166-24, 2024, https://doi.org/10.1128/spectrum.00166-24 | Taxon-specific gene naming. |
| gamC – positively regulates – Gacamide A production | *gamC* loss abolished detectable biosurfactant and swarming in Pf0-1. | “gamC deletion abolished both [biosurfactant] and swarming.” (pastora2024multiplepathwaysimpact pages 5-7) | 10.1128/spectrum.00166-24, 2024, https://doi.org/10.1128/spectrum.00166-24 | Strong but strain-specific. |
| pleA/pleC export machinery – positively regulates – biosurfactant secretion | Predicted export genes were needed for biosurfactant-zone formation and full swarming. | “Loss of pleA or pleC eliminated biosurfactant zones and swarming.” (pastora2024multiplepathwaysimpact pages 5-7) | 10.1128/spectrum.00166-24, 2024, https://doi.org/10.1128/spectrum.00166-24 | Export function predicted; secretion role partly inferred. |
| Exogenous Gacamide A – positively regulates – swarming motility | Added biosurfactant partially restored or promoted swarming, supporting a direct wetting-agent role. | “The non-ribosomal cyclic lipopeptide Gacamide A promotes swarming when added exogenously.” (pastora2024multiplepathwaysimpact pages 5-7) | 10.1128/spectrum.00166-24, 2024, https://doi.org/10.1128/spectrum.00166-24 | Assay-specific complementation. |
| MotCD stator – positively regulates – swarming motility | In *P. aeruginosa*, MotCD availability increased the active-flagella fraction and supported swarm onset. | “Deletion of MotCD eliminates swarming… MotCD cells are ~10× more likely to have an active motor.” (anda2024howp.aeruginosa pages 8-10, anda2024howp.aeruginosa pages 13-14) | 10.1128/mbio.03322-23, 2024, https://doi.org/10.1128/mbio.03322-23 | Strong in *P. aeruginosa*; collective-population effect. |
| MotAB stator – negatively regulates – swarming motility | MotAB-only motor composition was associated with low active-flagella fraction and swarming deficiency. | “The MotAB-only motor has ~13% flagellum-active cells and is swarming-deficient.” (anda2024howp.aeruginosa pages 8-10) | 10.1128/mbio.03322-23, 2024, https://doi.org/10.1128/mbio.03322-23 | Taxon-specific; negative effect may depend on stator balance, not absolute presence. |
| MotCD overexpression – positively regulates – swarming motility | Increasing MotCD dosage enhanced swarming area in an arabinose-dependent manner. | “1% arabinose gave ~40% mean increase in swarming area versus vector.” (anda2024howp.aeruginosa pages 8-10) | 10.1128/mbio.03322-23, 2024, https://doi.org/10.1128/mbio.03322-23 | Overexpression system; assay-specific induction conditions. |
| MotAB overexpression – negatively regulates – swarming motility | Induced MotAB in a MotCD background progressively inhibited swarming and could arrest it. | “At 0.2% arabinose MotAB induction caused swarming arrest.” (anda2024howp.aeruginosa pages 8-10, anda2024howp.aeruginosa pages 13-14) | 10.1128/mbio.03322-23, 2024, https://doi.org/10.1128/mbio.03322-23 | Overexpression artifact possible; still strong causal evidence in assay. |
| FlgZ:c-di-GMP complex – negatively regulates – MotCD recruitment | The c-di-GMP effector FlgZ binds MotC and blocks MotCD recruitment to the motor. | “FlgZ binds MotC in a c-di-GMP-dependent manner to block MotCD recruitment.” (anda2024howp.aeruginosa pages 13-14) | 10.1128/mbio.03322-23, 2024, https://doi.org/10.1128/mbio.03322-23 | Mechanistic edge is from cited model within the paper; species-specific. |
| MotC – positively regulates – SadC diguanylate cyclase activity | MotC interaction with SadC increased c-di-GMP, creating feedback between stator usage and signaling. | “MotC interacts with SadC to increase cellular c-di-GMP.” (anda2024howp.aeruginosa pages 13-14) | 10.1128/mbio.03322-23, 2024, https://doi.org/10.1128/mbio.03322-23 | Strong in *P. aeruginosa*; signaling context dependent. |
| Quorum sensing – positively regulates – HAA/rhamnolipid production | The 2023 biophysics review summarizes that QS controls production of HAAs and rhamnolipids needed for swarm development. | “QS regulates HAA and RL production.” (bru2023swarmingofp. pages 2-3, bru2023swarmingofp. pages 11-12, bru2023swarmingofp. pages 1-2) | 10.1063/5.0128140, 2023, https://doi.org/10.1063/5.0128140 | Review-level synthesis, mainly *P. aeruginosa*. |
| Rhamnolipid/HAA production – positively regulates – swarm expansion | Surfactant-deficient mutants failed to expand normally or make tendrils, supporting a requirement for these wetting agents. | “Mutants defective in RL production are deficient in swarm expansion and fail to form tendrils.” (bru2023swarmingofp. pages 2-3, bru2023swarmingofp. pages 1-2) | 10.1063/5.0128140, 2023, https://doi.org/10.1063/5.0128140 | Review statement; strongest for *P. aeruginosa*. |
| Flagellar activity – positively regulates – swarm expansion | The review emphasizes that flagellar activity, alongside surfactant production, is required for dendritic swarming. | “Two activities are essential for forming dendritic swarms: surfactant production and flagellar activity.” (bru2023swarmingofp. pages 1-2) | 10.1063/5.0128140, 2023, https://doi.org/10.1063/5.0128140 | Broad but species- and assay-dependent in boundary cases. |
| Exogenous surfactant – positively regulates – flagella-dependent alternative surface spreading | Foreign surfactants from other microbes or hosts enabled *P. aeruginosa* to spread on surfaces where it was otherwise immotile. | “Exogenous surfactants allowed emergence of surface motility on hard agar; active flagella were required.” (warrell2024interspeciessurfactantsserve pages 1-2) | 10.1128/jb.00281-24, 2024, https://doi.org/10.1128/jb.00281-24 | Important boundary case: this is surfing-like spreading, not canonical swarming. |
| Rhamnolipid production – positively regulates – sliding motility | Warrell et al. summarize that sliding requires rhamnolipids but no motility appendages. | “Sliding requires only rhamnolipids without appendages.” (warrell2024interspeciessurfactantsserve pages 1-2) | 10.1128/jb.00281-24, 2024, https://doi.org/10.1128/jb.00281-24 | Useful for excluding sliding from swarming trait scope. |
| 0.4% agar + 2% NaCl medium – positively supports assay observation of – swarming halo expansion | The optimized *Vibrio parahaemolyticus* assay identified LB Lennox plus 2% NaCl and 0.4% agar as the best plate composition for reproducible swarming. | “LB Lennox with 0.4% Bacto agar was the most effective composition.” (pozo2024optimizedswarmingmotility pages 2-4, pozo2024optimizedswarmingmotility media 55e33928) | 10.1016/j.mex.2024.102622, 2024, https://doi.org/10.1016/j.mex.2024.102622 | Assay factor, not intrinsic mechanism; useful as environmental node. |
| 5-minute plate drying – positively supports assay observation of – rapid swarming migration | Drying time was experimentally optimized and affected the speed/readout of halo expansion. | “A 5-minute drying time was optimal for the fastest swarming migration.” (pozo2024optimizedswarmingmotility media 55e33928) | 10.1016/j.mex.2024.102622, 2024, https://doi.org/10.1016/j.mex.2024.102622 | Purely assay-specific. |
| 3 µL inoculum volume – positively supports assay observation of – rapid swarming migration | Inoculum volume was an optimized experimental factor in the swarming assay workflow. | “A 3 μL inoculum volume was optimal for achieving the fastest swarming migration.” (pozo2024optimizedswarmingmotility pages 2-4, pozo2024optimizedswarmingmotility media 55e33928) | 10.1016/j.mex.2024.102622, 2024, https://doi.org/10.1016/j.mex.2024.102622 | Purely assay-specific. |
| Fur (Vsfur) – positively regulates – fliC/Vsflic expression | In *Vibrio splendidus*, Fur knockdown reduced *Vsflic* expression, linking Fur to the flagellar program. | “Vsflic was downregulated to 0.56-fold… Fur positively regulates Vsflic to contribute to swarming.” (shi2023vibriosplendidusfur pages 1-2, shi2023vibriosplendidusfur pages 5-7, shi2023vibriosplendidusfur pages 9-10) | 10.3389/fvets.2023.1207831, 2023, https://doi.org/10.3389/fvets.2023.1207831 | Taxon-specific; direct binding predicted, not fully biochemically validated. |
| Fur (Vsfur) – positively regulates – swarming motility | The Vsfur knockdown mutant showed reduced swarm diameter under normal/iron-replete conditions. | “MTVs swarming motility was reduced; colony diameter was ~79–81% of WTVs.” (shi2023vibriosplendidusfur pages 1-2, shi2023vibriosplendidusfur pages 7-9, shi2023vibriosplendidusfur pages 9-10) | 10.3389/fvets.2023.1207831, 2023, https://doi.org/10.3389/fvets.2023.1207831 | Iron-condition dependent; effect absent under low-iron/no-spread condition. |
| Glabridin – negatively regulates – abaI/abaR expression | Sub-MIC glabridin decreased expression of the quorum-sensing genes *abaI* and *abaR* in MDR *A. baumannii*. | “abaI was lowered up to 39.12% and abaR up to 25.19%.” (lin2023glabridinfunctionsas pages 4-8, lin2023glabridinfunctionsas pages 1-2) | 10.2147/IDR.S417751, 2023, https://doi.org/10.2147/idr.s417751 | Strain-to-strain variability; no direct target identified. |
| Glabridin – negatively regulates – swarming motility | Glabridin reduced surface motility by ~44–51% at 1/4–1/2 MIC without affecting growth below MIC. | “Pooled motility reductions were ~44.3% at 1/4 MIC and ~50.6% at 1/2 MIC.” (lin2023glabridinfunctionsas pages 4-8, lin2023glabridinfunctionsas pages 1-2, lin2023glabridinfunctionsas pages 2-4) | 10.2147/IDR.S417751, 2023, https://doi.org/10.2147/idr.s417751 | Assay-specific and species-specific; mechanistic link via QS is plausible but partly inferred. |
| Osmolyte accumulation in swarm layer – positively regulates – fluid influx/volumetric expansion | Bru et al. discuss osmolyte-driven water influx from agar as one candidate mechanism for swarm expansion. | “Pressure-driven flow from agar due to osmolyte-induced influx may produce volumetric expansion.” (bru2023swarmingofp. pages 11-12) | 10.1063/5.0128140, 2023, https://doi.org/10.1063/5.0128140 | Hypothesis/review model; should be curated as uncertain until direct causal tests exist. |
| Marangoni surface-tension gradients – positively regulate – swarm expansion | Surfactant-generated surface-tension gradients are proposed as a physical driver of expansion in *P. aeruginosa* swarms. | “Fluid-mechanics models invoke Marangoni-driven expansion from surfactant gradients.” (bru2023swarmingofp. pages 2-3, bru2023swarmingofp. pages 11-12) | 10.1063/5.0128140, 2023, https://doi.org/10.1063/5.0128140 | Hypothesis/review model; likely not universally curatable as a biological edge. |


*Table: This table lists candidate subject-predicate-object edges for curating a TraitMech causal graph of swarming motility, with concise evidence, source citations, and uncertainty notes. It emphasizes experimentally supported regulatory, structural, surfactant, and assay-factor relationships while flagging physical-model hypotheses and boundary cases.*

## 7) Evidence-backed statistics (selected highlights)

- *P. aeruginosa* stator effects: MotAB-only ~13% active flagella and swarming-deficient; MotCD-only ~90% active flagella; MotCD induction (1% arabinose) ~40% mean increase in swarming area; MotAB induction (0.2% arabinose in MotCD background) swarming arrest. (anda2024howp.aeruginosa pages 8-10)
- *V. parahaemolyticus* assay standardization: OD600 1.00 ± 0.01 (~10^9 CFU/mL), 0.4% agar + 2% NaCl, 3 µL inoculum, halo measured every 2 h over 24 h; six replicates; five independent assays. (pozo2024optimizedswarmingmotility pages 2-4)
- MDR *A. baumannii* QS inhibition by glabridin: motility reduced ~44.27% (1/4 MIC) and ~50.64% (1/2 MIC); abaI down to ~39.12% and abaR down to ~25.19% (max effect; strain-dependent). (lin2023glabridinfunctionsas pages 4-8, lin2023glabridinfunctionsas pages 1-2)
- *V. splendidus* Fur knockdown: Vsflic down to 0.56-fold; LD50 shifted from 9.116×10^6 to 1.658×10^11 CFU·mL−1 (WT vs knockdown). (shi2023vibriosplendidusfur pages 1-2, shi2023vibriosplendidusfur pages 5-7)

## 8) Warnings / not-yet-curatable claims

1. **Fluid-mechanics drivers (Marangoni, osmolyte-driven influx) are often model-supported but not always demonstrated as direct causal biological edges**; curate as *uncertain* until organism- and assay-specific perturbations confirm necessity/sufficiency. (bru2023swarmingofp. pages 2-3, bru2023swarmingofp. pages 11-12)
2. **“Swarming” labels in the literature may include surfing-like or sliding-like spreading** depending on agar hardness, mucin/exogenous surfactants, and regulatory context; curators should encode assay context (medium, agar %, additives) as nodes to avoid conflating distinct modes. (warrell2024interspeciessurfactantsserve pages 1-2, bru2023swarmingofp. pages 8-10)
3. **Non-flagellar surface expansion mechanisms** (e.g., “swashing”) motivate strict adherence to the flagella-dependent definition for traitmech:000062 and careful exclusion of propulsion-independent phenotypes from the swarming node. (panich2024swashingmotilitya pages 13-15)

---

# DOI-first bibliography (with dates and URLs)

1. **de Anda J, et al.** (2024-04). *How P. aeruginosa cells with diverse stator composition collectively swarm*. **mBio** 15(4). DOI: **10.1128/mbio.03322-23**. https://doi.org/10.1128/mbio.03322-23 (anda2024howp.aeruginosa pages 8-10, anda2024howp.aeruginosa pages 13-14)
2. **Pastora AB, Rzasa KM, O’Toole GA.** (2024-06). *Multiple pathways impact the swarming motility of Pseudomonas fluorescens Pf0-1*. **Microbiology Spectrum** 12(6). DOI: **10.1128/spectrum.00166-24**. https://doi.org/10.1128/spectrum.00166-24 (pastora2024multiplepathwaysimpact pages 1-3, pastora2024multiplepathwaysimpact pages 5-7)
3. **Warrell DL, et al.** (2024-10). *Interspecies surfactants serve as public goods enabling surface motility in Pseudomonas aeruginosa*. **Journal of Bacteriology** 206(10). DOI: **10.1128/jb.00281-24**. https://doi.org/10.1128/jb.00281-24 (warrell2024interspeciessurfactantsserve pages 1-2)
4. **Pozo F, et al.** (2024-06). *Optimized swarming motility assay to identify anti-virulence products against Vibrio parahaemolyticus*. **MethodsX** 12:102622. DOI: **10.1016/j.mex.2024.102622**. https://doi.org/10.1016/j.mex.2024.102622 (pozo2024optimizedswarmingmotility pages 2-4, pozo2024optimizedswarmingmotility media 55e33928)
5. **Bru J-L, et al.** (2023-09). *Swarming of P. aeruginosa: Through the lens of biophysics*. **Biophysics Reviews** 4(3). DOI: **10.1063/5.0128140**. https://doi.org/10.1063/5.0128140 (bru2023swarmingofp. pages 2-3, bru2023swarmingofp. pages 11-12, bru2023swarmingofp. pages 1-2, bru2023swarmingofp. pages 8-10)
6. **Zegadło K, et al.** (2023-01). *Bacterial Motility and Its Role in Skin and Wound Infections*. **Int J Mol Sci** 24(2):1707. DOI: **10.3390/ijms24021707**. https://doi.org/10.3390/ijms24021707 (zegadło2023bacterialmotilityand pages 4-5, zegadło2023bacterialmotilityand pages 1-2)
7. **Lin H, et al.** (2023-08). *Glabridin functions as a quorum sensing inhibitor to inhibit biofilm formation and swarming motility of multidrug-resistant Acinetobacter baumannii*. **Infection and Drug Resistance** 16:5697–5705. DOI: **10.2147/IDR.S417751**. https://doi.org/10.2147/idr.s417751 (lin2023glabridinfunctionsas pages 4-8, lin2023glabridinfunctionsas pages 1-2)
8. **Shi Y, et al.** (2023-06). *Vibrio splendidus Fur regulates virulence gene expression, swarming motility, and biofilm formation*. **Frontiers in Veterinary Science** 10. DOI: **10.3389/fvets.2023.1207831**. https://doi.org/10.3389/fvets.2023.1207831 (shi2023vibriosplendidusfur pages 1-2, shi2023vibriosplendidusfur pages 5-7, shi2023vibriosplendidusfur pages 7-9)
9. **Panich J, et al.** (2024-08; preprint). *Swashing motility: A novel propulsion-independent mechanism for surface migration in Salmonella and E. coli*. **bioRxiv**. DOI: **10.1101/2024.08.21.609010**. https://doi.org/10.1101/2024.08.21.609010 (panich2024swashingmotilitya pages 13-15)


References

1. (bru2023swarmingofp. pages 1-2): Jean-Louis Bru, Summer J. Kasallis, Quantum Zhuo, Nina Molin Høyland-Kroghsbo, and Albert Siryaporn. Swarming of p. aeruginosa: through the lens of biophysics. Biophysics Reviews, Sep 2023. URL: https://doi.org/10.1063/5.0128140, doi:10.1063/5.0128140. This article has 29 citations.

2. (warrell2024interspeciessurfactantsserve pages 1-2): Delayna L. Warrell, Tiffany M. Zarrella, Christopher Machalek, and Anupama Khare. Interspecies surfactants serve as public goods enabling surface motility in <i>pseudomonas aeruginosa</i>. Journal of Bacteriology, Oct 2024. URL: https://doi.org/10.1128/jb.00281-24, doi:10.1128/jb.00281-24. This article has 13 citations and is from a peer-reviewed journal.

3. (zegadło2023bacterialmotilityand pages 4-5): Katarzyna Zegadło, Monika Gieroń, Paulina Żarnowiec, Katarzyna Durlik-Popińska, Beata Kręcisz, Wiesław Kaca, and Grzegorz Czerwonka. Bacterial motility and its role in skin and wound infections. International Journal of Molecular Sciences, 24:1707, Jan 2023. URL: https://doi.org/10.3390/ijms24021707, doi:10.3390/ijms24021707. This article has 100 citations.

4. (bru2023swarmingofp. pages 11-12): Jean-Louis Bru, Summer J. Kasallis, Quantum Zhuo, Nina Molin Høyland-Kroghsbo, and Albert Siryaporn. Swarming of p. aeruginosa: through the lens of biophysics. Biophysics Reviews, Sep 2023. URL: https://doi.org/10.1063/5.0128140, doi:10.1063/5.0128140. This article has 29 citations.

5. (zegadło2023bacterialmotilityand pages 2-4): Katarzyna Zegadło, Monika Gieroń, Paulina Żarnowiec, Katarzyna Durlik-Popińska, Beata Kręcisz, Wiesław Kaca, and Grzegorz Czerwonka. Bacterial motility and its role in skin and wound infections. International Journal of Molecular Sciences, 24:1707, Jan 2023. URL: https://doi.org/10.3390/ijms24021707, doi:10.3390/ijms24021707. This article has 100 citations.

6. (bru2023swarmingofp. pages 8-10): Jean-Louis Bru, Summer J. Kasallis, Quantum Zhuo, Nina Molin Høyland-Kroghsbo, and Albert Siryaporn. Swarming of p. aeruginosa: through the lens of biophysics. Biophysics Reviews, Sep 2023. URL: https://doi.org/10.1063/5.0128140, doi:10.1063/5.0128140. This article has 29 citations.

7. (panich2024swashingmotilitya pages 13-15): Justin Panich, Eric M. Dudebout, Navish Wadhwa, and David F. Blair. Swashing motility: a novel propulsion-independent mechanism for surface migration in salmonella and e. coli. bioRxiv, Aug 2024. URL: https://doi.org/10.1101/2024.08.21.609010, doi:10.1101/2024.08.21.609010. This article has 2 citations.

8. (panich2024swashingmotilitya pages 11-13): Justin Panich, Eric M. Dudebout, Navish Wadhwa, and David F. Blair. Swashing motility: a novel propulsion-independent mechanism for surface migration in salmonella and e. coli. bioRxiv, Aug 2024. URL: https://doi.org/10.1101/2024.08.21.609010, doi:10.1101/2024.08.21.609010. This article has 2 citations.

9. (zegadło2023bacterialmotilityand pages 1-2): Katarzyna Zegadło, Monika Gieroń, Paulina Żarnowiec, Katarzyna Durlik-Popińska, Beata Kręcisz, Wiesław Kaca, and Grzegorz Czerwonka. Bacterial motility and its role in skin and wound infections. International Journal of Molecular Sciences, 24:1707, Jan 2023. URL: https://doi.org/10.3390/ijms24021707, doi:10.3390/ijms24021707. This article has 100 citations.

10. (bru2023swarmingofp. pages 2-3): Jean-Louis Bru, Summer J. Kasallis, Quantum Zhuo, Nina Molin Høyland-Kroghsbo, and Albert Siryaporn. Swarming of p. aeruginosa: through the lens of biophysics. Biophysics Reviews, Sep 2023. URL: https://doi.org/10.1063/5.0128140, doi:10.1063/5.0128140. This article has 29 citations.

11. (anda2024howp.aeruginosa pages 13-14): Jaime de Anda, Sherry L. Kuchma, Shanice S. Webster, Arman Boromand, Kimberley A. Lewis, Calvin K. Lee, Maria Contreras, Victor F. Medeiros Pereira, William Schmidt, Deborah A. Hogan, Corey S. O’Hern, George A. O’Toole, and Gerard C. L. Wong. How <i>p. aeruginosa</i> cells with diverse stator composition collectively swarm. Apr 2024. URL: https://doi.org/10.1128/mbio.03322-23, doi:10.1128/mbio.03322-23. This article has 10 citations and is from a domain leading peer-reviewed journal.

12. (anda2024howp.aeruginosa pages 8-10): Jaime de Anda, Sherry L. Kuchma, Shanice S. Webster, Arman Boromand, Kimberley A. Lewis, Calvin K. Lee, Maria Contreras, Victor F. Medeiros Pereira, William Schmidt, Deborah A. Hogan, Corey S. O’Hern, George A. O’Toole, and Gerard C. L. Wong. How <i>p. aeruginosa</i> cells with diverse stator composition collectively swarm. Apr 2024. URL: https://doi.org/10.1128/mbio.03322-23, doi:10.1128/mbio.03322-23. This article has 10 citations and is from a domain leading peer-reviewed journal.

13. (pastora2024multiplepathwaysimpact pages 1-3): Alexander B. Pastora, Kara M. Rzasa, and George A. O’Toole. Multiple pathways impact the swarming motility of <i>pseudomonas fluorescens</i> pf0-1. Jun 2024. URL: https://doi.org/10.1128/spectrum.00166-24, doi:10.1128/spectrum.00166-24. This article has 5 citations and is from a domain leading peer-reviewed journal.

14. (pastora2024multiplepathwaysimpact pages 5-7): Alexander B. Pastora, Kara M. Rzasa, and George A. O’Toole. Multiple pathways impact the swarming motility of <i>pseudomonas fluorescens</i> pf0-1. Jun 2024. URL: https://doi.org/10.1128/spectrum.00166-24, doi:10.1128/spectrum.00166-24. This article has 5 citations and is from a domain leading peer-reviewed journal.

15. (pozo2024optimizedswarmingmotility pages 2-4): Francisco Pozo, Martha Borbor, Ramiro Solórzano, Stanislaus Sonnenholzner, and Bonny Bayot. Optimized swarming motility assay to identify anti-virulence products against vibrio parahaemolyticus, a pathogen of farmed shrimp. Jun 2024. URL: https://doi.org/10.1016/j.mex.2024.102622, doi:10.1016/j.mex.2024.102622. This article has 6 citations.

16. (pozo2024optimizedswarmingmotility media 55e33928): Francisco Pozo, Martha Borbor, Ramiro Solórzano, Stanislaus Sonnenholzner, and Bonny Bayot. Optimized swarming motility assay to identify anti-virulence products against vibrio parahaemolyticus, a pathogen of farmed shrimp. Jun 2024. URL: https://doi.org/10.1016/j.mex.2024.102622, doi:10.1016/j.mex.2024.102622. This article has 6 citations.

17. (pozo2024optimizedswarmingmotility media 2e70544b): Francisco Pozo, Martha Borbor, Ramiro Solórzano, Stanislaus Sonnenholzner, and Bonny Bayot. Optimized swarming motility assay to identify anti-virulence products against vibrio parahaemolyticus, a pathogen of farmed shrimp. Jun 2024. URL: https://doi.org/10.1016/j.mex.2024.102622, doi:10.1016/j.mex.2024.102622. This article has 6 citations.

18. (pozo2024optimizedswarmingmotility media c478a897): Francisco Pozo, Martha Borbor, Ramiro Solórzano, Stanislaus Sonnenholzner, and Bonny Bayot. Optimized swarming motility assay to identify anti-virulence products against vibrio parahaemolyticus, a pathogen of farmed shrimp. Jun 2024. URL: https://doi.org/10.1016/j.mex.2024.102622, doi:10.1016/j.mex.2024.102622. This article has 6 citations.

19. (pozo2024optimizedswarmingmotility media 7e88c879): Francisco Pozo, Martha Borbor, Ramiro Solórzano, Stanislaus Sonnenholzner, and Bonny Bayot. Optimized swarming motility assay to identify anti-virulence products against vibrio parahaemolyticus, a pathogen of farmed shrimp. Jun 2024. URL: https://doi.org/10.1016/j.mex.2024.102622, doi:10.1016/j.mex.2024.102622. This article has 6 citations.

20. (pozo2024optimizedswarmingmotility media 9f2b1952): Francisco Pozo, Martha Borbor, Ramiro Solórzano, Stanislaus Sonnenholzner, and Bonny Bayot. Optimized swarming motility assay to identify anti-virulence products against vibrio parahaemolyticus, a pathogen of farmed shrimp. Jun 2024. URL: https://doi.org/10.1016/j.mex.2024.102622, doi:10.1016/j.mex.2024.102622. This article has 6 citations.

21. (lin2023glabridinfunctionsas pages 1-2): Hang Lin, Cui Zhou, Kai-Hang Yu, Yi-Shuai Lin, Ling-Bo Wang, Ying Zhang, Shi-Xing Liu, Wen-Ya Xu, Yao Sun, Tie-Li Zhou, Jian-Ming Cao, and Jian-Zhong Ye. Glabridin functions as a quorum sensing inhibitor to inhibit biofilm formation and swarming motility of multidrug-resistant acinetobacter baumannii. Infection and Drug Resistance, 16:5697-5705, Aug 2023. URL: https://doi.org/10.2147/idr.s417751, doi:10.2147/idr.s417751. This article has 17 citations and is from a peer-reviewed journal.

22. (lin2023glabridinfunctionsas pages 4-8): Hang Lin, Cui Zhou, Kai-Hang Yu, Yi-Shuai Lin, Ling-Bo Wang, Ying Zhang, Shi-Xing Liu, Wen-Ya Xu, Yao Sun, Tie-Li Zhou, Jian-Ming Cao, and Jian-Zhong Ye. Glabridin functions as a quorum sensing inhibitor to inhibit biofilm formation and swarming motility of multidrug-resistant acinetobacter baumannii. Infection and Drug Resistance, 16:5697-5705, Aug 2023. URL: https://doi.org/10.2147/idr.s417751, doi:10.2147/idr.s417751. This article has 17 citations and is from a peer-reviewed journal.

23. (shi2023vibriosplendidusfur pages 1-2): Yue Shi, Changyu Liao, Fawen Dai, Yiwei Zhang, Chenghua Li, and Weikang Liang. Vibrio splendidus fur regulates virulence gene expression, swarming motility, and biofilm formation, affecting its pathogenicity in apostichopus japonicus. Frontiers in Veterinary Science, Jun 2023. URL: https://doi.org/10.3389/fvets.2023.1207831, doi:10.3389/fvets.2023.1207831. This article has 11 citations and is from a peer-reviewed journal.

24. (shi2023vibriosplendidusfur pages 5-7): Yue Shi, Changyu Liao, Fawen Dai, Yiwei Zhang, Chenghua Li, and Weikang Liang. Vibrio splendidus fur regulates virulence gene expression, swarming motility, and biofilm formation, affecting its pathogenicity in apostichopus japonicus. Frontiers in Veterinary Science, Jun 2023. URL: https://doi.org/10.3389/fvets.2023.1207831, doi:10.3389/fvets.2023.1207831. This article has 11 citations and is from a peer-reviewed journal.

25. (shi2023vibriosplendidusfur pages 7-9): Yue Shi, Changyu Liao, Fawen Dai, Yiwei Zhang, Chenghua Li, and Weikang Liang. Vibrio splendidus fur regulates virulence gene expression, swarming motility, and biofilm formation, affecting its pathogenicity in apostichopus japonicus. Frontiers in Veterinary Science, Jun 2023. URL: https://doi.org/10.3389/fvets.2023.1207831, doi:10.3389/fvets.2023.1207831. This article has 11 citations and is from a peer-reviewed journal.

26. (shi2023vibriosplendidusfur pages 9-10): Yue Shi, Changyu Liao, Fawen Dai, Yiwei Zhang, Chenghua Li, and Weikang Liang. Vibrio splendidus fur regulates virulence gene expression, swarming motility, and biofilm formation, affecting its pathogenicity in apostichopus japonicus. Frontiers in Veterinary Science, Jun 2023. URL: https://doi.org/10.3389/fvets.2023.1207831, doi:10.3389/fvets.2023.1207831. This article has 11 citations and is from a peer-reviewed journal.

27. (lin2023glabridinfunctionsas pages 2-4): Hang Lin, Cui Zhou, Kai-Hang Yu, Yi-Shuai Lin, Ling-Bo Wang, Ying Zhang, Shi-Xing Liu, Wen-Ya Xu, Yao Sun, Tie-Li Zhou, Jian-Ming Cao, and Jian-Zhong Ye. Glabridin functions as a quorum sensing inhibitor to inhibit biofilm formation and swarming motility of multidrug-resistant acinetobacter baumannii. Infection and Drug Resistance, 16:5697-5705, Aug 2023. URL: https://doi.org/10.2147/idr.s417751, doi:10.2147/idr.s417751. This article has 17 citations and is from a peer-reviewed journal.