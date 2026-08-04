---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T02:20:57.224272'
end_time: '2026-08-04T02:29:07.900769'
duration_seconds: 490.68
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: pH delta low
  trait_identifier: METPO:1000474
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: ph_delta_low
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A pH delta phenotype with a growth-supporting pH breadth of approximately\
    \ 1\u20132 pH units, characteristic of organisms with limited pH-tolerance breadth."
  parent_traits: METPO:1000232
  synonyms: pHd_1_2
  evidence_summary: 'DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review
    supports limited pH-homeostasis flexibility as the basis for a narrow pH-tolerance
    breadth.)'
  causal_graph_summary: 'ph_delta_low_limited_breadth: 12 nodes, 7 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 42
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH delta low
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000474
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH delta phenotype with a growth-supporting pH breadth of approximately 1–2 pH units, characteristic of organisms with limited pH-tolerance breadth.
- **Parent traits:** METPO:1000232
- **Synonyms:** pHd_1_2
- **Existing evidence:** DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review supports limited pH-homeostasis flexibility as the basis for a narrow pH-tolerance breadth.)
- **Existing causal graph summary:** ph_delta_low_limited_breadth: 12 nodes, 7 edges

## Research Objective

Research the microbial trait **pH delta low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_delta_low.yaml`.

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
- **Trait label:** pH delta low
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000474
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH delta phenotype with a growth-supporting pH breadth of approximately 1–2 pH units, characteristic of organisms with limited pH-tolerance breadth.
- **Parent traits:** METPO:1000232
- **Synonyms:** pHd_1_2
- **Existing evidence:** DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review supports limited pH-homeostasis flexibility as the basis for a narrow pH-tolerance breadth.)
- **Existing causal graph summary:** ph_delta_low_limited_breadth: 12 nodes, 7 edges

## Research Objective

Research the microbial trait **pH delta low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_delta_low.yaml`.

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


# Curation-focused research report: microbial **pH delta low**

## Executive assessment

**Target trait:** **pH delta low**  
**Trait identifier:** **METPO:1000474**  
**Parent:** METPO:1000232  
**Synonym:** pHd_1_2  
**Recommended interpretation:** an **assay-observed growth phenotype** in which the interval between the lowest and highest tested pH supporting growth is approximately **1–2 pH units**. It is a breadth measurement, not a statement that the organism prefers low pH.

The literature strongly supports mechanisms that determine microbial pH tolerance—cytoplasmic-pH regulation, proton motive force (PMF), membrane proton permeability, cation/proton antiport, proton-consuming metabolism, and energetic capacity—but generally does **not** establish that any single mechanism causes an organism-wide breadth of exactly 1–2 units. The final edge from “limited pH-homeostasis capacity” to **METPO:1000474** should therefore remain an integrative, inferred edge unless it is supported by matched growth-range and perturbation experiments.

## 1. Trait scope and boundary conditions

### Operational scope

The phenotype should be calculated from growth measurements across a pH series under otherwise fixed conditions. A defensible implementation should record:

- minimum and maximum pH meeting a predefined growth threshold;
- pH spacing and whether endpoints were bracketed;
- medium composition, buffer identity and concentration;
- temperature, atmosphere, salinity, inoculum, incubation duration, and vessel format;
- growth metric—optical density, viable counts, biomass, growth rate, or substrate conversion;
- whether pH was measured initially, continuously, or only at the endpoint.

The 2024 methodological review emphasizes that acid-stress conclusions depend on methods spanning single cells through heterogeneous populations and that cytoplasmic-pH heterogeneity can alter apparent population tolerance. Consequently, a breadth from coarse one-unit pH steps may be interval-censored rather than a precise physiological limit. (atasoy2024methodsforstudying pages 36-37, atasoy2024methodsforstudying pages 37-37)

### Distinctions from nearby traits

1. **Not optimum pH.** An organism may have an acidic, neutral, or alkaline optimum and still have a 1–2-unit breadth.
2. **Not acidophily or alkaliphily.** These describe the location of the niche on the pH axis; pH delta describes its width.
3. **Not acid survival/resistance.** E. coli’s Gad system can permit survival for hours near pH 2.5 “without growth”; such evidence cannot establish a growth-supporting pH endpoint. (li2024responseofescherichia pages 2-4)
4. **Not acid-tolerance response alone.** A transient, inducible stress response does not prove sustained reproduction.
5. **Not intracellular pH range.** External growth breadth and cytoplasmic pH are related but different measurements. Many bacterial cells maintain internal pH around 7.0–7.5, while external pH may vary substantially. (poolman2023physicochemicalhomeostasisin pages 2-4)
6. **Not automatically a constitutive genotype.** Breadth may change with substrate availability, prior adaptation, weak-acid identity, buffering, biofilm state, or community composition.

A useful boundary example is *Bacillus pseudofirmus* OF4: complete cytoplasmic-pH homeostasis was reported over external pH 7.5–9.5, while optimal growth extended to approximately pH 10.5 and slower growth to at least pH 11. Thus, failure of “complete” homeostasis does not coincide exactly with cessation of growth. (krulwich2011molecularaspectsof pages 12-14)

## 2. Current mechanistic understanding

Microbial growth across pH depends on maintaining cytoplasmic chemistry and PMF within limits while retaining enough energy for biosynthesis. Acid stress increases inward proton pressure. Cells can reduce proton entry through low-permeability membranes, export protons through pumps, consume protons metabolically, and alter membrane potential. At alkaline pH, cells commonly use Na+/H+ or K+/H+ antiport to import protons. These processes are coupled to ATP supply, ion availability, membrane composition, and substrate availability. (krulwich2011molecularaspectsof pages 5-6, poolman2023physicochemicalhomeostasisin pages 2-4, guan2020microbialresponseto pages 2-4)

The energetic trade-off is important for a narrow-growth-breadth hypothesis. One study summarized in the acid-stress review found glycolytic rate increased by 70% as pH fell from 6.6 to 4.7, while biomass synthesis became 80% less efficient, consistent with diversion of energy toward maintenance and proton extrusion. This is evidence for an energetic constraint, but it is not a universal quantitative law. (guan2020microbialresponseto pages 4-5)

Amino-acid decarboxylation provides a particularly clear mechanism: decarboxylation consumes one cytoplasmic proton, while substrate/product antiport contributes to membrane potential. Poolman estimated the energetic equivalent as one proton translocated per molecule decarboxylated, approximately one-third to one-fifth of an ATP depending on coupling stoichiometry. (poolman2023physicochemicalhomeostasisin pages 2-4)

## 3. Candidate causal-graph nodes

Identifiers below are supplied only where grounding is sufficiently stable; label-only candidates are preferable to invented or strain-inappropriate CURIEs.

### Trait and assay nodes

- **pH delta low** — **METPO:1000474**
- **parent pH-delta phenotype** — **METPO:1000232**
- growth-supporting pH breadth — label-only operational node
- minimum growth pH; maximum growth pH — label-only assay endpoints
- growth rate — **GO:0040007**
- cell population growth — **GO:0008283** is eukaryote-biased in some uses; verify before microbial curation
- acid-stress survival — label-only; keep separate from growth
- assay pH spacing, growth threshold, incubation duration, buffer capacity — label-only experimental-factor nodes

### Environmental and chemical nodes

- proton — **CHEBI:15378**
- water — **CHEBI:15377**
- ATP — **CHEBI:15422**
- ADP — **CHEBI:16761**
- L-glutamate — **CHEBI:29985**
- 4-aminobutanoate/GABA — **CHEBI:16865**
- carbon dioxide — **CHEBI:16526**
- potassium cation — **CHEBI:29103**
- sodium cation — **CHEBI:29101**
- putrescine — **CHEBI:17148**
- glutamine, ammonia/ammonium, urea, arginine, lysine — useful candidates; identifier versions should be verified during YAML preparation
- extracellular acidic pH; extracellular alkaline pH — label-only environmental states rather than treating pH as a chemical entity

### Processes and functions

- cellular pH homeostasis — **GO:0006885**
- proton transmembrane transport — **GO:1902600**
- proton motive force — label-only candidate; verify current GO term before curation
- ATP synthesis coupled proton transport — **GO:0015986**
- glutamate decarboxylation — label-only process; enzyme can be grounded by EC
- membrane proton permeability
- membrane-lipid remodeling
- oxidative phosphorylation — **GO:0006119**
- biofilm formation — **GO:0042710**
- cell-wall integrity pathway — label-only for fungal context unless a suitable GO term is verified

### Genes, proteins, and complexes

- **GadA/GadB**, glutamate decarboxylase — **EC:4.1.1.15**; use taxon-specific UniProt accessions only for specified strains
- **GadC**, glutamate/GABA antiporter — label plus taxon-specific protein accession
- **YbaS**, glutaminase — enzyme/protein identifier should be taxon-specific
- F-type H+-transporting ATPase / F0F1 ATP synthase — complex-level label; individual subunits may be grounded with GO or strain-specific UniProt entries
- **NhaA**, electrogenic Na+/H+ antiporter — label plus taxon-specific UniProt
- **MrpABCDEFG** cation/proton antiporter complex; **MrpA** subunit — label plus taxon-specific UniProt
- K+/H+ antiporter; K+-uptake ATPase — family-level labels pending organism selection
- urease — **EC:3.5.1.5**
- arginine decarboxylase — **EC:4.1.1.19**
- lysine decarboxylase — **EC:4.1.1.18**
- membrane porins; fatty-acid desaturases; cyclopropane-fatty-acyl-phospholipid synthase — candidates requiring taxon-specific grounding
- Stb5, Mac1, Rtg1/Rtg3 — fungal regulatory candidates, presently hypothesis-generating rather than graph-ready for the generic trait

### Cellular locations

- cytoplasm — **GO:0005737**
- plasma membrane — **GO:0005886**
- cell envelope — **GO:0030313**
- periplasmic space — **GO:0042597**
- extracellular region — **GO:0005576**

## 4. Candidate causal edges

The table below separates direct perturbation evidence from generic reviews and inference. For TraitMech, direct genetic or chemical perturbations should be preferred; generic mechanisms should not be represented as universally present in every organism.

| candidate subject | predicate | object | evidence strength | taxon/assay context | supporting short verbatim snippet | DOI |
|---|---|---|---|---|---|---|
| environmental pH excursion (acidic external pH) | increases | proton influx / cytoplasmic acidification pressure | review-supported generic | broad microbial acid-stress physiology; pH-homeostasis reviews (guan2020microbialresponseto pages 2-4, krulwich2011molecularaspectsof pages 5-6) | “Protons travel into the cytoplasm through the plasma membrane” (guan2020microbialresponseto pages 2-4) | 10.1007/s00253-019-10226-1 |
| low membrane proton permeability | decreases | proton entry into cells | review-supported generic | acid-tolerant microbes broadly; membrane adaptation model (guan2020microbialresponseto pages 2-4) | “Acid-tolerant microbes are generally equipped with less permeable membranes to reduce the entry of protons” (guan2020microbialresponseto pages 2-4) | 10.1007/s00253-019-10226-1 |
| membrane fatty-acid / lipid remodeling | maintains | membrane integrity and fluidity under low pH | review-supported generic | bacteria under acid adaptation (guan2020microbialresponseto pages 4-5, guan2020microbialresponseto pages 2-4) | “cell membranes confer acid tolerance to cells through maintenance of their integrity and fluidity because of acid adaptation” (guan2020microbialresponseto pages 4-5) | 10.1007/s00253-019-10226-1 |
| F-type H+-ATPase / F0F1-ATPase | pumps out / consumes intracellular H+ | intracellular pH homeostasis | review-supported generic | bacteria and E. coli AR1 discussions (guan2020microbialresponseto pages 2-4, li2024responseofescherichia pages 2-4) | “excess protons are pumped out from the cytoplasm” (guan2020microbialresponseto pages 2-4) | 10.1007/s00253-019-10226-1 |
| F0F1-ATPase running in hydrolysis mode | consumes | ATP during acid stress | review-supported generic | E. coli acid-stress review (li2024responseofescherichia pages 2-4) | “rapidly shifts its mechanism to consume intracellular H+ by hydrolyzing ATP” (li2024responseofescherichia pages 2-4) | 10.3390/microorganisms12091774 |
| ATP depletion / higher energetic burden at low pH | limits | growth efficiency | review-supported generic with quantitative support | low-pH metabolism studies summarized in review (guan2020microbialresponseto pages 4-5, guan2020microbialresponseto pages 2-4) | “biomass synthesis was 80% less efficient at low pH” (guan2020microbialresponseto pages 4-5) | 10.1007/s00253-019-10226-1 |
| Na+/H+ and K+/H+ antiporters | contribute to | alkaline pH homeostasis | review-supported generic | broad bacterial physicochemical homeostasis (poolman2023physicochemicalhomeostasisin pages 2-4, krulwich2011molecularaspectsof pages 5-6) | “major mechanisms of bacterial pH homeostasis are Na+/H+ and K+/H+ antiporters” (poolman2023physicochemicalhomeostasisin pages 2-4) | 10.1093/femsre/fuad033 |
| potassium transport / reverse membrane potential | restrains | inward proton flow | review-supported generic | acidophiles and acid tolerance reviews (guan2020microbialresponseto pages 2-4, valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 4-6) | “Potassium transporters are reported to be the most efficient in generating chemiosmotic gradients” (guan2020microbialresponseto pages 2-4) | 10.1007/s00253-019-10226-1 |
| Mrp antiporter (mrpA-containing complex) | is required for | alkaliphily and alkaline pH homeostasis | direct perturbation summarized in review | Bacillus pseudofirmus OF4, high-pH growth/homeostasis (krulwich2011molecularaspectsof pages 12-14) | “point mutations in mrpA eliminate alkaliphily and alkaline pH homeostasis” (krulwich2011molecularaspectsof pages 12-14) | 10.1038/nrmicro2549 |
| GadB glutamate decarboxylase | consumes | intracellular proton during glutamate decarboxylation | direct biochemical/physiological mechanism | L. reuteri acid resistance model; also generic Gad system (su2011contributionofglutamate pages 8-10, li2024responseofescherichia pages 2-4) | “Decarboxylation of glutamate consumes an intracellular proton” (su2011contributionofglutamate pages 8-10) | 10.1186/1475-2859-10-S1-S8 |
| GadC glutamate:GABA antiport + GadB | generates | ΔΨ and ΔpH / proton motive force | review-supported with organism-specific model | L. reuteri and broader decarboxylation mechanisms (su2011contributionofglutamate pages 1-2, poolman2023physicochemicalhomeostasisin pages 2-4) | “The antiport of glutamate and GABA generates a ΔpH and ΔΨ” (su2011contributionofglutamate pages 1-2) | 10.1186/1475-2859-10-S1-S8 |
| gadB deletion | decreases | survival at pH 2.5 with glutamate | direct genetic perturbation | Lactobacillus reuteri 100-23 vs ΔgadB in phosphate buffer (su2011contributionofglutamate pages 1-2) | “Glutamate addition to phosphate buffer, pH 2.5, improved survival of L. reuteri 100-23 100-fold. However, survival of L. reuteri ΔgadB remained essentially unchanged.” (su2011contributionofglutamate pages 1-2) | 10.1186/1475-2859-10-S1-S8 |
| exogenous putrescine | increases | glutamate–GABA pathway, ATPase expression, and acid-side biofilm pH adaptability | uncertain; community-level observational/intervention | activated-sludge biofilm under acid vs alkali conditions (jiang2024exogenousputrescineplays pages 1-2, jiang2024exogenousputrescineplays pages 9-12) | “putrescine stimulated ATPase expression” and “significantly upregulated genes associated with the glutamine–glutamate–GABA metabolic pathway under acidic stress” (jiang2024exogenousputrescineplays pages 1-2, jiang2024exogenousputrescineplays pages 9-12) | 10.1128/aem.00569-24 |
| limited pH-homeostasis flexibility / high energetic cost of pH control | constrains | narrow growth-supporting pH breadth (METPO:1000474 pH delta low) | inferred integrative edge | cross-taxon synthesis from pH-homeostasis reviews and quantitative examples (krulwich2011molecularaspectsof pages 3-5, krulwich2011molecularaspectsof pages 12-14, guan2020microbialresponseto pages 4-5) | “The balance between protein adaptation, energetic costs, and PMF maintenance” constrains growth-supporting pH breadth (krulwich2011molecularaspectsof pages 3-5) | 10.1038/nrmicro2549 |


*Table: This table compiles compact candidate causal edges for curating METPO:1000474, distinguishing direct perturbation evidence from broader review-supported or inferred mechanisms. It is useful for selecting high-confidence nodes and edges while flagging uncertain community-level findings.*

### Highest-priority edges for initial curation

The most defensible core is:

1. **external acidic pH → increases → inward proton pressure**;
2. **membrane proton impermeability → decreases → proton influx**;
3. **F-type H+-ATPase in ATP-hydrolysis mode → increases → proton extrusion/cytoplasmic-pH maintenance**;
4. **proton extrusion → consumes → ATP/maintenance energy**;
5. **GadB-catalysed glutamate decarboxylation → consumes → cytoplasmic proton**;
6. **cytoplasmic-proton consumption → supports → cytoplasmic pH homeostasis**;
7. **limited ATP supply or excessive maintenance cost → decreases → growth away from optimum pH**;
8. **insufficient pH-homeostasis capacity at both range boundaries → constrains → growth-supporting pH breadth**;
9. **constrained breadth of approximately 1–2 units → realizes → METPO:1000474**.

Edges 1–7 have strong mechanistic support. Edges 8–9 are graph-level interpretations and should be marked **inferred** unless a matched experiment measures the complete growth curve before and after perturbation.

### Direct perturbation anchors

In *Lactobacillus reuteri* 100-23, an isogenic **gadB** deletion abolished glutamate-to-GABA conversion at pH 2.5. Glutamate improved wild-type survival approximately 100-fold but did not materially improve ΔgadB survival. The wild type also displaced the mutant after five back-slopping cycles in sourdough. However, gadB disruption did **not** affect growth in mMRS or single-batch sourdough, demonstrating why a survival edge must not be converted automatically into a growth-breadth edge. (su2011contributionofglutamate pages 1-2, su2011contributionofglutamate pages 8-10)

For alkaline adaptation, point mutations in **mrpA** eliminated alkaliphily and alkaline pH homeostasis in *B. pseudofirmus* OF4. Mutations in alkaliphile-specific ATP-synthase motifs disproportionately reduced activity at pH 10.5 and impaired pH homeostasis after alkaline shifts. These are strong causal anchors, but they support the high-pH side of tolerance in a specific alkaliphile rather than generic pH-delta-low status. (krulwich2011molecularaspectsof pages 12-14)

## 5. Recent developments, 2023–2024

### Better measurement and single-cell resolution

The 2024 FEMS methodological review highlights automated growth monitoring, fluorescent cytoplasmic-pH reporters, microfluidics, and single-cell analyses. A major implication is that population-average growth can hide subpopulations with different cytoplasmic pH or survival states. Trait curation should therefore record whether breadth was inferred from bulk growth, colony formation, or single-cell division. (atasoy2024methodsforstudying pages 36-37, atasoy2024methodsforstudying pages 40-41, atasoy2024methodsforstudying pages 37-37)

### Physicochemical integration

Poolman’s 2023 review places pH within a coupled physicochemical system involving PMF, ionic strength, crowding, turgor, and energy status. It reports intracellular K+ concentrations of approximately 0.2 M in *E. coli*, 0.8 M in *Lactococcus lactis*, and 2.1 M in *Haloferax volcanii*, illustrating that ion-homeostasis solutions vary greatly across taxa. Generic graphs should therefore represent K+ as a conditional mechanistic input rather than a universal concentration threshold. (poolman2023physicochemicalhomeostasisin pages 2-4)

### Community-level pH engineering with putrescine

A 2024 activated-sludge biofilm study found that exogenous putrescine had opposite effects across pH regimes. Under acidic conditions (pH 3–4), ATP and ADP increased by 58% and 26%, glutamine–glutamate–GABA genes and proton-pump-related genes were upregulated, and biofilm formation was promoted. Under alkaline conditions (pH 8–9), energy availability and biofilm development were inhibited. Because this is a mixed community with metagenomic/physiological associations, the edges should be marked **community-level, condition-specific, and uncertain**, not assigned to an individual microbial trait graph without validation. (jiang2024exogenousputrescineplays pages 1-2, jiang2024exogenousputrescineplays pages 9-12)

### Multi-strain transcriptomic discovery

A 2024 study profiled 12 *Issatchenkia orientalis* strains—six tolerant and six susceptible—and implicated energy metabolism, translation, cell-wall integrity, RTG retrograde signaling, glycolysis, and trehalose biosynthesis in low-pH response. The authors explicitly state that these candidates require experimental perturbation and engineering. Accordingly, Stb5, Mac1, Rtg1/Rtg3, glycolysis, and trehalose biosynthesis should remain **candidate nodes**, not causal edges for METPO:1000474. (dubinkina2024atranscriptomicatlas pages 1-2)

### Acidophile applications

A 2024 review of acidophilic sulfate-reducing bacteria describes K+/Na+ accumulation, positive-inside Donnan potential, low proton permeability, and proton-efflux systems as adaptations to low pH. These organisms are being applied to acid-mine-drainage treatment through sulfate reduction, sulfide generation, and metal precipitation. The review also estimates sulfate-transport cost at approximately one-quarter to one-third ATP per sulfate and emphasizes the additional energetic demand of pH homeostasis. These mechanisms are taxon- and metabolism-specific. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 4-6)

## 6. Applications and real-world implementations

- **Food fermentation:** GadB-dependent acid resistance improved persistence and competitiveness of *L. reuteri* in serially propagated sourdough, providing a direct ecological implementation. (su2011contributionofglutamate pages 1-2, su2011contributionofglutamate pages 8-10)
- **Organic-acid and lignocellulosic bioproduction:** Acid-tolerant yeasts can reduce neutralization requirements, salt by-products, sterility costs, and contamination risk. *I. orientalis* is being developed as a low-pH production chassis, although its causal tolerance mechanisms remain incompletely validated. (dubinkina2024atranscriptomicatlas pages 1-2)
- **Wastewater biofilms:** Putrescine supplementation has been proposed to improve acidic biofilm stability or suppress alkaline biofilm development, but dosage, community shifts, and transferability require validation. (jiang2024exogenousputrescineplays pages 1-2, jiang2024exogenousputrescineplays pages 9-12)
- **Acid-mine drainage:** Acidophilic sulfate reducers can generate sulfide and precipitate dissolved metals; consortia may be more practical than pure isolates. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 4-6)
- **Pathogen and food-safety control:** Distinguishing growth inhibition from survival is critical because acid-resistance systems may preserve infectivity even when growth is absent. E. coli can survive near pH 2–2.5 through Gad-dependent systems without reproducing. (krulwich2011molecularaspectsof pages 5-6, li2024responseofescherichia pages 2-4)

## 7. Recommended graph architecture

A compact, taxon-agnostic TraitMech graph should use modular alternatives rather than imply that all organisms possess every mechanism:

**Environmental branch:** external pH departure → transmembrane proton disequilibrium → cytoplasmic-pH stress.

**Barrier branch:** membrane composition/channel architecture → membrane proton permeability → proton influx.

**Transport branch:** F-type ATPase and cation/proton antiport → proton flux → cytoplasmic pH and PMF.

**Metabolic branch:** glutamate or other amino-acid decarboxylation → proton consumption/alkaline products → cytoplasmic-pH maintenance.

**Energetic branch:** ATP-generating metabolism → maintenance-energy availability → sustained growth under pH stress.

**Phenotype branch:** cytoplasmic-pH/PMF failure or excessive maintenance cost → growth-rate decline → lower or upper growth-pH boundary → narrow growth-supporting breadth → **METPO:1000474**.

Use `part_of`, `enables`, or biochemical reaction predicates for molecular relations; reserve `increases`, `decreases`, `required_for`, and `supports` for experimentally justified causal relations. Avoid encoding correlation from differential expression as causation.

## 8. Warnings: claims not yet ready for TraitMech

1. **No reviewed source directly defines a universal 1–2-pH-unit mechanistic threshold.** The numerical breadth is an ontology/assay category, not a known molecular breakpoint.
2. **Do not curate “GadB increases growth breadth” from survival evidence.** In *L. reuteri*, gadB deletion affected acid survival and serial-fermentation competitiveness but not growth in the tested mMRS or single-batch sourdough conditions. (su2011contributionofglutamate pages 1-2, su2011contributionofglutamate pages 8-10)
3. **Do not merge acid and alkaline mechanisms.** Proton export is generally useful during acid loading, whereas proton uptake through cation/proton antiport is central at alkaline pH; direction depends on transporter, PMF, and conditions. (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 12-14)
4. **Do not treat expression changes as necessity or sufficiency.** Putrescine-community metagenomics and *I. orientalis* transcriptomics are hypothesis-generating. (jiang2024exogenousputrescineplays pages 9-12, dubinkina2024atranscriptomicatlas pages 1-2)
5. **Do not generalize taxon-specific machinery.** GadBC, Mrp, NhaA, urease, and fungal RTG signaling are alternative modules, not universal components.
6. **Do not ignore weak-acid chemistry.** Equal extracellular pH values can impose different stresses because undissociated organic acids cross membranes and dissociate intracellularly.
7. **Do not curate assay endpoints without metadata.** Buffer capacity, pH drift, growth threshold, pH spacing, substrate, temperature, and adaptation history can change the measured breadth.
8. **Verify ontology versions and strain-specific accessions during YAML authoring.** Family labels are safer than assigning an incorrect UniProt, KEGG, or Rhea identifier.

## 9. DOI-first bibliography

1. **Atasoy M. et al.** “Methods for studying microbial acid stress responses: from molecules to populations.” *FEMS Microbiology Reviews* 48 (published May 2024). DOI: [10.1093/femsre/fuae015](https://doi.org/10.1093/femsre/fuae015). (atasoy2024methodsforstudying pages 36-37)
2. **Jiang G. et al.** “Exogenous putrescine plays a switch-like influence on the pH stress adaptability of biofilm-based activated sludge.” *Applied and Environmental Microbiology* 90(7) (published 25 June 2024; July issue). DOI: [10.1128/aem.00569-24](https://doi.org/10.1128/aem.00569-24). (jiang2024exogenousputrescineplays pages 1-2, jiang2024exogenousputrescineplays pages 9-12)
3. **Li Z., Huang Z., Gu P.** “Response of *Escherichia coli* to Acid Stress: Mechanisms and Applications—A Narrative Review.” *Microorganisms* 12:1774 (August 2024). DOI: [10.3390/microorganisms12091774](https://doi.org/10.3390/microorganisms12091774). (li2024responseofescherichia pages 2-4)
4. **Dubinkina V. et al.** “A transcriptomic atlas of acute stress response to low pH in multiple *Issatchenkia orientalis* strains.” *Microbiology Spectrum* 12(1) (online 29 November 2023; issue January 2024). DOI: [10.1128/spectrum.02536-23](https://doi.org/10.1128/spectrum.02536-23). (dubinkina2024atranscriptomicatlas pages 1-2)
5. **Valdez-Nuñez L.F. et al.** “Acidophilic sulphate-reducing bacteria: Diversity, ecophysiology, and applications.” *Environmental Microbiology Reports* 16(5) (October 2024). DOI: [10.1111/1758-2229.70019](https://doi.org/10.1111/1758-2229.70019). (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 4-6)
6. **Poolman B.** “Physicochemical homeostasis in bacteria.” *FEMS Microbiology Reviews* 47(4) (June 2023). DOI: [10.1093/femsre/fuad033](https://doi.org/10.1093/femsre/fuad033). (poolman2023physicochemicalhomeostasisin pages 2-4)
7. **Guan N., Liu L.** “Microbial response to acid stress: mechanisms and applications.” *Applied Microbiology and Biotechnology* 104:51–65 (online November 2019; 2020 volume). DOI: [10.1007/s00253-019-10226-1](https://doi.org/10.1007/s00253-019-10226-1). (guan2020microbialresponseto pages 4-5, guan2020microbialresponseto pages 2-4)
8. **Su M.S., Schlicht S., Gänzle M.G.** “Contribution of glutamate decarboxylase in *Lactobacillus reuteri* to acid resistance and persistence in sourdough fermentation.” *Microbial Cell Factories* 10(Suppl 1):S8 (August 2011). DOI: [10.1186/1475-2859-10-S1-S8](https://doi.org/10.1186/1475-2859-10-S1-S8). (su2011contributionofglutamate pages 1-2, su2011contributionofglutamate pages 8-10)
9. **Krulwich T.A., Sachs G., Padan E.** “Molecular aspects of bacterial pH sensing and homeostasis.” *Nature Reviews Microbiology* 9:330–343 (May 2011). DOI: [10.1038/nrmicro2549](https://doi.org/10.1038/nrmicro2549). (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 3-5, krulwich2011molecularaspectsof pages 12-14)

## Curation conclusion

The best-supported explanation for **METPO:1000474** is not one dedicated pathway but a systems-level failure to maintain cytoplasmic pH, PMF, membrane integrity, and sufficient growth energy outside a narrow external-pH interval. For an initial YAML graph, curate the mechanistically secure intermediate edges and mark the terminal relation—**limited pH-homeostasis flexibility → narrow 1–2-unit growth breadth**—as **inferred**. Upgrade that terminal edge only when a study measures the complete growth-supporting pH range under a defined assay and demonstrates that a genetic or chemical perturbation changes its width.

References

1. (atasoy2024methodsforstudying pages 36-37): Merve Atasoy, Simona Bartkova, Zeynep Çetecioğlu-Gürol, Nuno P Mira, Conor O'Byrne, Fernando Pérez-Rodríguez, Arícia Possas, Ott Scheler, J. Sedlakova-Kadukova, Mirka Sinčák, Matthias Steiger, Carmit Ziv, and Peter A Lund. Methods for studying microbial acid stress responses: from molecules to populations. FEMS Microbiology Reviews, May 2024. URL: https://doi.org/10.1093/femsre/fuae015, doi:10.1093/femsre/fuae015. This article has 10 citations and is from a domain leading peer-reviewed journal.

2. (atasoy2024methodsforstudying pages 37-37): Merve Atasoy, Simona Bartkova, Zeynep Çetecioğlu-Gürol, Nuno P Mira, Conor O'Byrne, Fernando Pérez-Rodríguez, Arícia Possas, Ott Scheler, J. Sedlakova-Kadukova, Mirka Sinčák, Matthias Steiger, Carmit Ziv, and Peter A Lund. Methods for studying microbial acid stress responses: from molecules to populations. FEMS Microbiology Reviews, May 2024. URL: https://doi.org/10.1093/femsre/fuae015, doi:10.1093/femsre/fuae015. This article has 10 citations and is from a domain leading peer-reviewed journal.

3. (li2024responseofescherichia pages 2-4): Zepeng Li, Zhaosong Huang, and Pengfei Gu. Response of escherichia coli to acid stress: mechanisms and applications—a narrative review. Microorganisms, 12:1774, Aug 2024. URL: https://doi.org/10.3390/microorganisms12091774, doi:10.3390/microorganisms12091774. This article has 41 citations.

4. (poolman2023physicochemicalhomeostasisin pages 2-4): Bert Poolman. Physicochemical homeostasis in bacteria. FEMS Microbiology Reviews, Jun 2023. URL: https://doi.org/10.1093/femsre/fuad033, doi:10.1093/femsre/fuad033. This article has 46 citations and is from a domain leading peer-reviewed journal.

5. (krulwich2011molecularaspectsof pages 12-14): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

6. (krulwich2011molecularaspectsof pages 5-6): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

7. (guan2020microbialresponseto pages 2-4): Ningzi Guan and Long Liu. Microbial response to acid stress: mechanisms and applications. Applied Microbiology and Biotechnology, 104:51-65, Nov 2020. URL: https://doi.org/10.1007/s00253-019-10226-1, doi:10.1007/s00253-019-10226-1. This article has 778 citations and is from a domain leading peer-reviewed journal.

8. (guan2020microbialresponseto pages 4-5): Ningzi Guan and Long Liu. Microbial response to acid stress: mechanisms and applications. Applied Microbiology and Biotechnology, 104:51-65, Nov 2020. URL: https://doi.org/10.1007/s00253-019-10226-1, doi:10.1007/s00253-019-10226-1. This article has 778 citations and is from a domain leading peer-reviewed journal.

9. (valdez‐nunez2024acidophilicsulphate‐reducingbacteria pages 4-6): Luis Felipe Valdez‐Nuñez, Andreas Kappler, Diana Ayala‐Muñoz, Idelso Jamín Chávez, and Muammar Mansor. Acidophilic sulphate‐reducing bacteria: diversity, ecophysiology, and applications. Environmental Microbiology Reports, Oct 2024. URL: https://doi.org/10.1111/1758-2229.70019, doi:10.1111/1758-2229.70019. This article has 18 citations and is from a peer-reviewed journal.

10. (su2011contributionofglutamate pages 8-10): Marcia S Su, Sabine Schlicht, and Michael G Gänzle. Contribution of glutamate decarboxylase in lactobacillus reuteri to acid resistance and persistence in sourdough fermentation. Microbial Cell Factories, 10:S8-S8, Aug 2011. URL: https://doi.org/10.1186/1475-2859-10-s1-s8, doi:10.1186/1475-2859-10-s1-s8. This article has 175 citations and is from a peer-reviewed journal.

11. (su2011contributionofglutamate pages 1-2): Marcia S Su, Sabine Schlicht, and Michael G Gänzle. Contribution of glutamate decarboxylase in lactobacillus reuteri to acid resistance and persistence in sourdough fermentation. Microbial Cell Factories, 10:S8-S8, Aug 2011. URL: https://doi.org/10.1186/1475-2859-10-s1-s8, doi:10.1186/1475-2859-10-s1-s8. This article has 175 citations and is from a peer-reviewed journal.

12. (jiang2024exogenousputrescineplays pages 1-2): Guanyu Jiang, Can Wang, Yongchao Wang, Jiayi Wang, Yi-Mei Xue, Yuting Lin, Xurui Hu, and Yahui Lv. Exogenous putrescine plays a switch-like influence on the ph stress adaptability of biofilm-based activated sludge. Applied and Environmental Microbiology, Jul 2024. URL: https://doi.org/10.1128/aem.00569-24, doi:10.1128/aem.00569-24. This article has 6 citations and is from a peer-reviewed journal.

13. (jiang2024exogenousputrescineplays pages 9-12): Guanyu Jiang, Can Wang, Yongchao Wang, Jiayi Wang, Yi-Mei Xue, Yuting Lin, Xurui Hu, and Yahui Lv. Exogenous putrescine plays a switch-like influence on the ph stress adaptability of biofilm-based activated sludge. Applied and Environmental Microbiology, Jul 2024. URL: https://doi.org/10.1128/aem.00569-24, doi:10.1128/aem.00569-24. This article has 6 citations and is from a peer-reviewed journal.

14. (krulwich2011molecularaspectsof pages 3-5): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1290 citations and is from a highest quality peer-reviewed journal.

15. (atasoy2024methodsforstudying pages 40-41): Merve Atasoy, Simona Bartkova, Zeynep Çetecioğlu-Gürol, Nuno P Mira, Conor O'Byrne, Fernando Pérez-Rodríguez, Arícia Possas, Ott Scheler, J. Sedlakova-Kadukova, Mirka Sinčák, Matthias Steiger, Carmit Ziv, and Peter A Lund. Methods for studying microbial acid stress responses: from molecules to populations. FEMS Microbiology Reviews, May 2024. URL: https://doi.org/10.1093/femsre/fuae015, doi:10.1093/femsre/fuae015. This article has 10 citations and is from a domain leading peer-reviewed journal.

16. (dubinkina2024atranscriptomicatlas pages 1-2): Veronika Dubinkina, Shounak Bhogale, Ping-Hung Hsieh, Payam Dibaeinia, Ananthan Nambiar, Sergei Maslov, Yasuo Yoshikuni, and Saurabh Sinha. A transcriptomic atlas of acute stress response to low ph in multiple <i>issatchenkia orientalis</i> strains. Jan 2024. URL: https://doi.org/10.1128/spectrum.02536-23, doi:10.1128/spectrum.02536-23. This article has 12 citations and is from a domain leading peer-reviewed journal.