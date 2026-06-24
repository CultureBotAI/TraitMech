---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T01:15:19.541906'
end_time: '2026-06-18T01:46:02.001022'
duration_seconds: 1842.46
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: salinity phenotype with numerical limits
  trait_identifier: METPO:1000532
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: salinity_phenotype_with_numerical_limits
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A phenotype characterized by specific salt concentration values or ranges
    that define growth or activity limits.
  parent_traits: METPO:1000059
  synonyms: ''
  evidence_summary: 'DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review
    supports quantitative salinity descriptors (optimum, range, delta) as the standard
    numerical phenotype framing for halophily classification.) | DOI:10.1093/femsre/fuy009:
    Hypersaline environments (Osmoadaptation review supports salinity as the physical
    axis underlying halophily classifications.)'
  causal_graph_summary: 'salinity_phenotype_numerical_axis: 5 nodes, 4 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 25
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** salinity phenotype with numerical limits
- **METPO identifier:** METPO:1000532
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype characterized by specific salt concentration values or ranges that define growth or activity limits.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review supports quantitative salinity descriptors (optimum, range, delta) as the standard numerical phenotype framing for halophily classification.) | DOI:10.1093/femsre/fuy009: Hypersaline environments (Osmoadaptation review supports salinity as the physical axis underlying halophily classifications.)
- **Existing causal graph summary:** salinity_phenotype_numerical_axis: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **salinity phenotype with numerical limits** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/salinity_phenotype_with_numerical_limits.yaml`.

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
- **Trait label:** salinity phenotype with numerical limits
- **METPO identifier:** METPO:1000532
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype characterized by specific salt concentration values or ranges that define growth or activity limits.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review supports quantitative salinity descriptors (optimum, range, delta) as the standard numerical phenotype framing for halophily classification.) | DOI:10.1093/femsre/fuy009: Hypersaline environments (Osmoadaptation review supports salinity as the physical axis underlying halophily classifications.)
- **Existing causal graph summary:** salinity_phenotype_numerical_axis: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **salinity phenotype with numerical limits** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/salinity_phenotype_with_numerical_limits.yaml`.

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


# Research Report: Microbial trait causal graph candidate — salinity phenotype with numerical limits (METPO:1000532)

## 1) Scope summary (Trait definition, boundaries, and current understanding)

**Target trait:** *salinity phenotype with numerical limits* (METPO:1000532) — a quantitative phenotype capturing **minimum**, **maximum**, and/or **optimum** salinity for microbial growth or activity, measured under defined assay conditions (medium composition, temperature, pH, oxygen availability, incubation time, inoculum). This trait is commonly operationalized by growth across a salinity series and reported in **% (w/v) salts/NaCl**, **g/L total salts**, **molar Na+/NaCl**, or occasionally **PSU** (environmental salinity) (galisteo2024thehypersalinesoils pages 4-5, oren2024novelinsightsinto pages 1-2, xing2024thepolyextremophilenatranaerobius pages 1-2).

**Operational domain framing:** A recent expert review defines “hypersaline environments” as **>100–150 g/L salts** and uses growth at such concentrations as an operational definition for halophiles in the context of ecosystem surveys (oren2024novelinsightsinto pages 1-2).

**Distinguish from adjacent traits:**
- *Halophile/halotolerant* labels are **qualitative** categories; METPO:1000532 requires **numerical limits** (oren2024novelinsightsinto pages 1-2).
- Mechanistic traits (e.g., “compatible solute accumulation”, “salt-in strategy”, transporter presence) are **causal determinants** of the numeric phenotype, not the phenotype itself (ionescu2024extremefluctuationsin pages 1-2, xing2024thepolyextremophilenatranaerobius pages 1-2).
- Habitat salinity measurements alone are out-of-scope unless linked to organism growth/activity limits.

**Important boundary condition:** Salinity is not a single variable; **salt composition** and **chaotropicity** (Mg/Ca/Li/Fe salts), **water activity (aw)**, and **pH/temperature** can shift effective growth limits even at similar NaCl totals (gutierrezpreciado2024extremelyacidicproteomes pages 1-4).

## 2) Recent developments and latest research (prioritizing 2023–2024)

### 2.1 Multi-omics evidence for hybrid osmoadaptation (2024)
A 2024 Applied and Environmental Microbiology study on the polyextremophilic bacterium *Natranaerobius thermophilus* provides unusually direct multi-layer evidence (proteomics + ddPCR + metabolite/ion measurements) that **long-term salinity adaptation can involve a hybrid “salt-in + compatible-solute” strategy**. The study explicitly links increasing external salinity to increased intracellular **glycine betaine, glutamate, and proline**, and to transport/ion homeostasis systems (xing2024thepolyextremophilenatranaerobius pages 1-2).

Mechanistic entities with evidence include:
- **Glycine betaine ABC transporters** (Opu/ProU families) and their components (e.g., proX/proV/proW; opuAC), and **betT** (choline/carnitine/betaine transporter) (xing2024thepolyextremophilenatranaerobius pages 6-7).
- **SSS family Na+/solute symporters** (e.g., putP, sdcS, nptA; plus specific symporter locus examples) (xing2024thepolyextremophilenatranaerobius pages 6-7).
- Ion-homeostasis components including **Na+/H+ antiporters (nhaC)** and **K+ uptake Trk system (trkA/trkH)** (xing2024thepolyextremophilenatranaerobius pages 6-7).
- A **Na+-translocating FOF1-ATPase** is described as part of the extreme-environment adaptation toolkit for this taxon (xing2024thepolyextremophilenatranaerobius pages 1-2).

### 2.2 Causal perturbation demonstrates osmolyte identity can shift growth limits (2024)
A 2024 AEM study provides particularly strong causal evidence for TraitMech edges because it uses engineered genotypes to show changes in **maximum salinity permitting growth**. In *Halomonas elongata*, an **ectoine-deficient mutant (ΔectABC)** could not grow above **4% NaCl**, whereas engineering **proline biosynthesis (proBm1AC)** plus deletion of **putA** enabled growth at **8% NaCl**, with high intracellular proline accumulation (khanh2024metabolicpathwayengineering pages 1-2).

This provides a clear mechanism: **compatible-solute availability and type (ectoine vs proline)** can be growth-limiting at high salt (khanh2024metabolicpathwayengineering pages 1-2).

### 2.3 Ecosystem-level synthesis and refined limits of life (2024)
A 2024 npj Biodiversity review highlights that the past ~5 years of metagenomics/cultivation expanded knowledge of halophile diversity and points to two key updates relevant to numerical salinity phenotyping:
- Operational framing of hypersalinity (**>100–150 g/L**) for “halophile” designation in ecosystem contexts (oren2024novelinsightsinto pages 1-2).
- Evidence that some haloarchaea typically thought to be “salt-in” (e.g., **Halomicroarcula**) can encode **compatible-solute biosynthesis pathways (trehalose, glycine betaine)**, implying mixed or context-dependent strategies that could change observed salinity optima/ranges (oren2024novelinsightsinto pages 1-2).

### 2.4 Proteome-level hallmarks of extreme halophily (2024)
A 2024 Nature Ecology & Evolution study emphasizes that salt-saturating growth is associated with a **“salt-in” strategy** (molar intracellular K+) and **highly acidified proteomes** (very low median pI values), and that **chaotropic brines** can be deleterious even where NaCl is saturating (gutierrezpreciado2024extremelyacidicproteomes pages 1-4).

### 2.5 Selection by fluctuating salinity and energetic constraints (2024)
A 2024 Frontiers in Microbiomes study argues that rapid salinity fluctuations select for organisms containing genes for both **energetically cheaper salt-in** and **more expensive salt-out** strategies, highlighting environment→mechanism edges relevant to causal graphs (ionescu2024extremefluctuationsin pages 1-2).

## 3) Current applications and real-world implementations

### 3.1 High-salinity bioprocessing and non-sterile production
Halophilic bacteria are of interest for industrial bioprocessing because high-salt conditions can reduce contamination risk and allow energy/resource-saving operation; this is discussed in the context of halophiles as biotechnological platforms in the Dead Sea/hypersaline literature (ionescu2024extremefluctuationsin pages 1-2).

### 3.2 Osmolytes as valuable products and engineering targets
The 2024 *Halomonas elongata* engineering study explicitly frames **proline** as a feed additive and demonstrates strain design principles for producing osmolytes under high salinity while maintaining growth (khanh2024metabolicpathwayengineering pages 1-2). This is a direct real-world pathway: **engineering osmolyte pathways → improved salt growth limits → production deployment**.

### 3.3 Agriculture: salt-tolerant microbes supporting plant performance
A 2023 genome+phenotype study reports a halophilic bacterium (*Virgibacillus halodenitrificans* ASH15) surviving up to **25% NaCl** and carrying genes for compatible-solute synthesis/transport alongside plant-growth-promoting traits, supporting the concept that microbial salt adaptation traits can be co-opted in saline agriculture contexts (sharma2023genomeanalysisof pages 1-2).

## 4) Expert opinions / authoritative synthesis

- **Oren (2024)** synthesizes the rapidly evolving census of halophilic taxa and underscores that modern “omics” is reshaping both diversity estimates and understanding of the **physiological limits of life** at high salinity, including impacts of **chaotropic ions** beyond NaCl (oren2024novelinsightsinto pages 1-2).
- **Gutiérrez-Preciado et al. (2024)** interpret extreme halophily as convergently associated with **salt-in physiology** and **proteome acidification**, while emphasizing water activity and chaotropicity as decisive physical constraints; this cautions curators not to treat “NaCl %” as sufficient without ionic context (gutierrezpreciado2024extremelyacidicproteomes pages 1-4).
- **Ionescu et al. (2024)** emphasize the energetic cost of osmoregulation and propose selection for scalable/hybrid strategies under fluctuating salinity regimes, a useful environment→mechanism concept for causal graphs (ionescu2024extremefluctuationsin pages 1-2).

## 5) Relevant statistics and quantitative data from recent studies

> - Hypersaline environments / halophilic scope in recent review: organisms growing at **>100–150 g/L dissolved salts** are operationally treated as halophiles in this context. (oren2024novelinsightsinto pages 1-2)
> - *Spiribacter* spp. are reported to grow at **3–27% (w/v) NaCl**, with an optimum of **10–15% (w/v) NaCl**; exceptions (*S. halobius*, “*S. salilacus*”) grow at **0.5–16% (w/v)** with optimum **3–6% (w/v)**. (leon2024integratinggenomicevidence pages 1-2)
> - *Natranaerobius thermophilus* has a growth range of **3.1–4.9 M Na+** and an optimum of **3.3–3.9 M Na+** at about **pH 9.5** and **53°C**. (xing2024thepolyextremophilenatranaerobius pages 1-2)
> - In the *N. thermophilus* proteomics experiment, salinity was tested at **2.5, 3.1, 3.7, and 4.3 M Na+**, corresponding to **14.63%, 18.14%, 21.65%, and 25.16% (wt/vol) Na+**. (xing2024thepolyextremophilenatranaerobius pages 1-2)
> - In engineered *Halomonas elongata*, deleting **ectABC** reduced growth to **≤4% NaCl**, whereas replacing ectoine synthesis with proline overproduction plus **putA** deletion enabled growth at **8% NaCl**; intracellular proline reached **353.1 ± 40.5 µmol/g** fresh weight. (khanh2024metabolicpathwayengineering pages 1-2)
> - *Virgibacillus halodenitrificans* ASH15 was reported to survive up to **25% (w/v) NaCl**, with genome evidence for compatible-solute synthesis/transport supporting this tolerance. (sharma2023genomeanalysisof pages 1-2)


*Blockquote: This blockquote condenses the most curation-relevant quantitative salinity phenotype values from 2023–2024 evidence. It is useful for defining numeric trait boundaries and selecting benchmark examples for TraitMech curation.*

Visual evidence for the *N. thermophilus* experimental salinity design and transporter/mechanism summary is available from cropped figures/tables retrieved from the 2024 AEM paper (xing2024thepolyextremophilenatranaerobius media 12691245, xing2024thepolyextremophilenatranaerobius media 7b23b5ec, xing2024thepolyextremophilenatranaerobius media 8dbe034b, xing2024thepolyextremophilenatranaerobius media 41b42098).

## 6) TraitMech curation: candidate nodes grouped by type (with suggested grounding)

### 6.1 Environmental / experimental factors (inputs)
- **Sodium chloride / total salts concentration** (CHEBI:26710 sodium chloride; note also Na+ as ion): reported in % (w/v), g/L, or molarity (galisteo2024thehypersalinesoils pages 4-5, xing2024thepolyextremophilenatranaerobius pages 1-2)
- **Salinity fluctuation regime** (label-only): variability in salinity, pH, oxygen (ionescu2024extremefluctuationsin pages 1-2)
- **Chaotropic ions**: Mg2+ (CHEBI:25107), Ca2+ (CHEBI:29108), Li+ (CHEBI:30145), Fe cations (CHEBI:18248) (gutierrezpreciado2024extremelyacidicproteomes pages 1-4)
- **Water activity (aw)** (label-only) (gutierrezpreciado2024extremelyacidicproteomes pages 1-4)
- **pH**, **temperature**, **oxygen** (label-only): known to shift observed salinity limits; explicit in *N. thermophilus* assays (pH ~9.5, 53°C) (xing2024thepolyextremophilenatranaerobius pages 1-2)

### 6.2 Assay / measurement nodes
- **Salinity series growth assay** (label-only): salts at multiple discrete concentrations to determine range/optimum (galisteo2024thehypersalinesoils pages 4-5)
- **OD600 growth kinetics** (label-only) (galisteo2024thehypersalinesoils pages 4-5)
- **Proteomics (iTRAQ/TMT-style quantitation)** and **ddPCR validation** (label-only) used to link mechanism to salinity conditions (xing2024thepolyextremophilenatranaerobius pages 1-2)

### 6.3 Mechanistic strategies (process nodes)
- **Salt-in strategy** (label-only; GO:0006970 response to osmotic stress as umbrella) (ionescu2024extremefluctuationsin pages 1-2, gutierrezpreciado2024extremelyacidicproteomes pages 1-4)
- **Salt-out / compatible-solute strategy** (label-only) (ionescu2024extremefluctuationsin pages 1-2)
- **Hybrid salt-in/salt-out strategy** (label-only) (xing2024thepolyextremophilenatranaerobius pages 1-2, ionescu2024extremefluctuationsin pages 1-2)

### 6.4 Ions and metabolites (chemical nodes)
- **K+** (CHEBI:29103), **Cl−** (CHEBI:17996), **Na+** (CHEBI:29101) (ionescu2024extremefluctuationsin pages 1-2, xing2024thepolyextremophilenatranaerobius pages 1-2)
- **Glycine betaine** (CHEBI:17750) (xing2024thepolyextremophilenatranaerobius pages 1-2)
- **L-proline** (CHEBI:26271) (khanh2024metabolicpathwayengineering pages 1-2, xing2024thepolyextremophilenatranaerobius pages 1-2)
- **L-glutamate** (CHEBI:29985), **glutamine** (CHEBI:28300) (xing2024thepolyextremophilenatranaerobius pages 1-2)
- **Trehalose** (CHEBI:16551) (oren2024novelinsightsinto pages 1-2)
- **Ectoine / hydroxyectoine** (CHEBI identifiers not provided in-source; label-only) (khanh2024metabolicpathwayengineering pages 1-2, sharma2023genomeanalysisof pages 1-2)

### 6.5 Genes / proteins / complexes (molecular function nodes)
- **Compatible-solute transporters:** Opu / ProU family ABC transporters (label-only), including **proX/proV/proW**, **opuAC**, and **betT** (xing2024thepolyextremophilenatranaerobius pages 6-7, xing2024thepolyextremophilenatranaerobius pages 1-2)
- **SSS-family Na+/solute symporters** (label-only; includes putP, sdcS, nptA as locus examples) (xing2024thepolyextremophilenatranaerobius pages 6-7)
- **Na+/H+ antiporter (nhaC)** (label-only) (xing2024thepolyextremophilenatranaerobius pages 6-7)
- **K+ uptake Trk system (trkA/trkH)** (label-only) (xing2024thepolyextremophilenatranaerobius pages 6-7)
- **Na+-translocating FOF1-ATPase** (label-only) (xing2024thepolyextremophilenatranaerobius pages 1-2)
- **Mechanosensitive channels** (label-only) (ionescu2024extremefluctuationsin pages 1-2)
- **Proline biosynthesis genes:** **proB/proA/proC** (enzymes γ-GK/GPR/P5CR; EC candidates: 2.7.2.11, 1.2.1.41, 1.5.1.2) (khanh2024metabolicpathwayengineering pages 1-2)
- **Ectoine biosynthesis operon:** **ectABC** (label-only) (khanh2024metabolicpathwayengineering pages 1-2)
- **Proline catabolism:** **putA** (label-only; PutA) (khanh2024metabolicpathwayengineering pages 1-2)

## 7) Evidence-backed candidate causal edges (triples)

The table below is designed for direct curation into a TraitMech/TraitGraph YAML. It includes mechanistic edges and assay edges with quotes, DOIs/URLs, dates, and uncertainty flags.

| Edge (S–P–O) | Node type(s) | Suggested grounding | Evidence snippet | Reference | Publication date | Notes/uncertainty |
|---|---|---|---|---|---|---|
| Extracellular salinity series — is_used_to_determine — salinity growth range/optimum | environment, assay, phenotype | CHEBI:26710 sodium chloride; METPO:1000532 salinity phenotype with numerical limits; label-only: salinity growth optimum/range assay | “supplemented with 0, 3, 4, 5, 6, 7, 7.5, 8, 9, 10, 12, 15, 17, 20, 22, and 25% (w/v) salts… in order to determine the range and optimum growth salinities” (galisteo2024thehypersalinesoils pages 4-5) | DOI:10.3390/microorganisms12020375 · https://doi.org/10.3390/microorganisms12020375 | Feb 2024 | Strong assay edge; directly supports how numerical salinity phenotype is measured. Taxon-specific protocol but generally curatable as assay logic. |
| OD600 growth kinetics — measures — salinity growth range/optimum | assay, phenotype | label-only: OD600 growth assay; METPO:1000532 | “via absorbance measurements at 600 nm every 2 h for 24 h” (galisteo2024thehypersalinesoils pages 4-5) | DOI:10.3390/microorganisms12020375 · https://doi.org/10.3390/microorganisms12020375 | Feb 2024 | Supports assay node rather than mechanism; useful for phenotyping provenance. |
| Compatible-solute strategy — maintains — intracellular osmotic balance across salinity | pathway/process, phenotype | GO:0006970 response to osmotic stress; label-only: compatible-solute strategy | “The second strategy, ‘salt-out’… relies on the accumulation of small organic compounds, generally referred to as compatible solutes” (ionescu2024extremefluctuationsin pages 1-2) | DOI:10.3389/frmbi.2023.1329925 · https://doi.org/10.3389/frmbi.2023.1329925 | Jan 2024 | General mechanistic edge; broad review-style statement from ecological paper. |
| Salt-in strategy — maintains — intracellular osmotic balance across salinity | pathway/process, phenotype | GO:0006970 response to osmotic stress; label-only: salt-in strategy; CHEBI:29103 potassium(1+) | “the ‘salt-in’ strategy as it involves a high intracellular concentration of salts, mainly potassium” (ionescu2024extremefluctuationsin pages 1-2) | DOI:10.3389/frmbi.2023.1329925 · https://doi.org/10.3389/frmbi.2023.1329925 | Jan 2024 | General mechanistic edge; broad but curation-worthy. |
| Glycine betaine — contributes_to — intracellular osmotic balance at high salinity | metabolite, phenotype | CHEBI:17750 glycine betaine | “The intracellular content of compatible solutes, including glycine betaine, glutamate, and proline, increases with rising salinity levels” (xing2024thepolyextremophilenatranaerobius pages 1-2) | DOI:10.1128/aem.00145-24 · https://doi.org/10.1128/aem.00145-24 | May 2024 | Strong metabolite-level edge with direct salinity response evidence; demonstrated in N. thermophilus, likely broadly generalizable. |
| L-proline — contributes_to — intracellular osmotic balance at high salinity | metabolite, phenotype | CHEBI:26271 L-proline | “The intracellular content of compatible solutes, including glycine betaine, glutamate, and proline, increases with rising salinity levels” (xing2024thepolyextremophilenatranaerobius pages 1-2) | DOI:10.1128/aem.00145-24 · https://doi.org/10.1128/aem.00145-24 | May 2024 | Strong metabolite-level edge; mostly generalizable though quantified in one taxon. |
| L-glutamate — contributes_to — intracellular osmotic balance at high salinity | metabolite, phenotype | CHEBI:29985 L-glutamate | “The intracellular content of compatible solutes, including glycine betaine, glutamate, and proline, increases with rising salinity levels” (xing2024thepolyextremophilenatranaerobius pages 1-2) | DOI:10.1128/aem.00145-24 · https://doi.org/10.1128/aem.00145-24 | May 2024 | Strong metabolite-level edge; likely generalizable. |
| Opu/ProU-family glycine betaine ABC transporters — enable_accumulation_of — glycine betaine | transporter/complex, metabolite | GO:0015893 drug transmembrane transporter activity not specific; label-only: Opu transporter, ProU transporter; CHEBI:17750 | “employs the glycine betaine ABC transporters (Opu and ProU families)… to adapt to high salinity” (xing2024thepolyextremophilenatranaerobius pages 1-2) | DOI:10.1128/aem.00145-24 · https://doi.org/10.1128/aem.00145-24 | May 2024 | Good mechanistic edge; transporter family-level grounding only. |
| Opu/ProU-family glycine betaine ABC transporters — promotes — adaptation to high salinity | transporter/complex, phenotype | label-only: Opu/ProU family; METPO:1000532 | “employs the glycine betaine ABC transporters (Opu and ProU families)… to adapt to high salinity” (xing2024thepolyextremophilenatranaerobius pages 1-2) | DOI:10.1128/aem.00145-24 · https://doi.org/10.1128/aem.00145-24 | May 2024 | Direct but somewhat broad; keep if graph allows pathway-to-phenotype links. |
| SSS-family Na+/solute symporters — promotes — adaptation to high salinity | transporter/complex, phenotype | label-only: SSS family Na+/solute symporter | “Na+/solute symporters (SSS family)… to adapt to high salinity” (xing2024thepolyextremophilenatranaerobius pages 1-2) | DOI:10.1128/aem.00145-24 · https://doi.org/10.1128/aem.00145-24 | May 2024 | Moderate evidence; taxon-specific demonstration in N. thermophilus. |
| Na+/K+/H+ transporters — maintains — intracellular K+ concentration | transporter/complex, ion homeostasis | label-only: Na+/K+/H+ transporter; CHEBI:29103 potassium(1+) | “the upregulation of Na+/ K+/ H+ transporters facilitates the maintenance of intracellular K+ concentration” (xing2024thepolyextremophilenatranaerobius pages 1-2) | DOI:10.1128/aem.00145-24 · https://doi.org/10.1128/aem.00145-24 | May 2024 | Strong causal wording. Good edge to osmotic-balance intermediate rather than directly to phenotype. |
| Intracellular K+ accumulation — supports — cellular ion homeostasis under varying salinities | ion, process/phenotype | CHEBI:29103 potassium(1+); label-only: cellular ion homeostasis | “ensuring cellular ion homeostasis under varying salinities” (xing2024thepolyextremophilenatranaerobius pages 1-2) | DOI:10.1128/aem.00145-24 · https://doi.org/10.1128/aem.00145-24 | May 2024 | Strong intermediate state edge. |
| TrkH K+ uptake system — increases — intracellular K+ homeostasis at high salinity | transporter/protein, ion homeostasis | label-only: TrkH potassium uptake protein | “K+ uptake (Trk system: trkA, trkH; trkH shows upregulation” (xing2024thepolyextremophilenatranaerobius pages 6-7) | DOI:10.1128/aem.00145-24 · https://doi.org/10.1128/aem.00145-24 | May 2024 | Useful but more inferred than directly quoted for causality; mark somewhat uncertain. Taxon-specific. |
| NhaC-family Na+/H+ antiporter — contributes_to — ion homeostasis under high salinity | transporter/protein, ion homeostasis | label-only: NhaC Na+/H+ antiporter | “Na+/H+ antiporters (nhaC; Nther_2723 shows large fold increase at higher salinities)” (xing2024thepolyextremophilenatranaerobius pages 6-7) | DOI:10.1128/aem.00145-24 · https://doi.org/10.1128/aem.00145-24 | May 2024 | Evidence is expression-based; causal role to phenotype is inferred from transporter function. Taxon-specific. |
| High intracellular K+ — is_associated_with — acidic proteome adaptation | ion, molecular phenotype | CHEBI:29103 potassium(1+); label-only: acidic proteome | “accumulate up to 4M K+ in their cytoplasm… proteome acidification is a hallmark of extreme halophily” (gutierrezpreciado2024extremelyacidicproteomes pages 1-4) | DOI:10.1038/s41559-024-02505-6 · https://doi.org/10.1038/s41559-024-02505-6 | Aug 2024 | General halophile adaptation edge; association stronger than direct mechanism. |
| Acidic proteome — enables — growth in salt-saturating conditions | molecular phenotype, phenotype | label-only: acidic proteome; ENVO:01000358 hypersaline environment | “proteome acidification is a hallmark of extreme halophily” and “thrive at salt-saturating conditions” (gutierrezpreciado2024extremelyacidicproteomes pages 1-4) | DOI:10.1038/s41559-024-02505-6 · https://doi.org/10.1038/s41559-024-02505-6 | Aug 2024 | Broad comparative inference; should be curated with caution because direct perturbation evidence is absent in this source. |
| Chaotropic ions (Mg/Ca/Li/Fe salts) — decreases — habitability at a given salinity | chemical environment, phenotype | CHEBI:25107 magnesium cation; CHEBI:29108 calcium(2+); CHEBI:30145 lithium(1+); CHEBI:18248 iron cation; label-only: chaotropicity | “Highly chaotropic brines are deleterious and seem devoid of microbial life” (gutierrezpreciado2024extremelyacidicproteomes pages 1-4) | DOI:10.1038/s41559-024-02505-6 · https://doi.org/10.1038/s41559-024-02505-6 | Aug 2024 | Important boundary-condition edge: salt composition modifies observed salinity limits. General environmental edge. |
| Water activity — constrains — salinity growth limits | environment, phenotype | label-only: water activity | “systems of even lower water activity (aw)… Highly chaotropic brines are deleterious” (gutierrezpreciado2024extremelyacidicproteomes pages 1-4) | DOI:10.1038/s41559-024-02505-6 · https://doi.org/10.1038/s41559-024-02505-6 | Aug 2024 | General abiotic edge; relevant for not over-interpreting NaCl-only limits. |
| Hybrid salt-in/salt-out strategy — is_selected_by — extreme salinity fluctuations | pathway/process, environment | label-only: hybrid osmoadaptation strategy; label-only: salinity fluctuation | “Extreme fluctuations in ambient salinity select for bacteria with a hybrid ‘salt-in’/’salt-out’ osmoregulation strategy” (ionescu2024extremefluctuationsin pages 1-2) | DOI:10.3389/frmbi.2023.1329925 · https://doi.org/10.3389/frmbi.2023.1329925 | Jan 2024 | Strong ecological selection edge; not a direct gene-to-phenotype statement but useful environment→mechanism edge. |
| Mechanosensitive channels — contributes_to — bacterial osmoregulation | protein/channel, process | label-only: mechanosensitive channel | “mechanosensitive channels used for osmoregulation by bacteria” (ionescu2024extremefluctuationsin pages 1-2) | DOI:10.3389/frmbi.2023.1329925 · https://doi.org/10.3389/frmbi.2023.1329925 | Jan 2024 | General but weak for salinity-limit phenotype specifically; candidate only. |
| proB/proA/proC proline biosynthesis pathway — produces — L-proline | pathway, genes, metabolite | KEGG: proline biosynthesis; EC 2.7.2.11 gamma-glutamyl kinase; EC 1.2.1.41 glutamate-5-semialdehyde dehydrogenase; EC 1.5.1.2 pyrroline-5-carboxylate reductase; CHEBI:26271 | “Pro is biosynthesized… by sequential actions of three enzymes… encoded by proB, proA, and proC genes” (khanh2024metabolicpathwayengineering pages 1-2) | DOI:10.1128/aem.01195-24 · https://doi.org/10.1128/aem.01195-24 | Sep 2024 | Strong biochemical edge. General across many bacteria. |
| L-proline accumulation — increases — high-salinity stress tolerance | metabolite, phenotype | CHEBI:26271 L-proline; METPO:1000532 | “overproduction of L-proline improves high-salinity stress tolerance” (khanh2024metabolicpathwayengineering pages 1-2) | DOI:10.1128/aem.01195-24 · https://doi.org/10.1128/aem.01195-24 | Sep 2024 | Strong causal perturbation evidence; especially valuable for curation. Mostly from engineered Halomonas, but mechanism broadly plausible. |
| ectABC deletion — decreases — maximum salinity permitting growth | gene cluster, phenotype | label-only: ectABC ectoine biosynthetic operon | “the Ect-deficient H. elongata KA1 could not grow in minimal media containing more than 4% NaCl” (khanh2024metabolicpathwayengineering pages 1-2) | DOI:10.1128/aem.01195-24 · https://doi.org/10.1128/aem.01195-24 | Sep 2024 | Strong taxon-specific causal perturbation; ideal as flagged species-specific evidence. |
| proBm1AC insertion plus putA deletion — increases — maximum salinity permitting growth | engineered gene cluster + gene deletion, phenotype | label-only: proBm1AC; label-only: putA | “H. elongata HN6 thrived in the medium containing 8% NaCl by accumulating Pro in the cell instead of Ect” (khanh2024metabolicpathwayengineering pages 1-2) | DOI:10.1128/aem.01195-24 · https://doi.org/10.1128/aem.01195-24 | Sep 2024 | Very strong taxon-specific causal edge from engineering; should be flagged as non-general but highly informative mechanistically. |
| PutA proline catabolism — decreases — intracellular L-proline available for osmoprotection | enzyme/gene, metabolite | label-only: PutA proline utilization A; CHEBI:26271 L-proline | “the putA gene, which encodes the key enzyme of Pro catabolism, was deleted” (khanh2024metabolicpathwayengineering pages 1-2) | DOI:10.1128/aem.01195-24 · https://doi.org/10.1128/aem.01195-24 | Sep 2024 | Causal direction inferred from known function plus engineering design; moderate confidence. |
| Spiribacter spp. — has_optimum_growth_at — 10–15% (w/v) NaCl | organism/taxon, phenotype | NCBITaxon: label-only Spiribacter; METPO:1000532 | “Species of the genus Spiribacter are moderate halophiles, growing at 3 to 27% (w/v) NaCl, with optimal growth between 10 and 15% (w/v) NaCl” (leon2024integratinggenomicevidence pages 1-2) | DOI:10.1038/s41598-024-80127-5 · https://doi.org/10.1038/s41598-024-80127-5 | Dec 2024 | Useful direct phenotype statement; not mechanistic but grounds trait semantics. Taxon-specific. |
| Spiribacter halobius / “S. salilacus” — has_optimum_growth_at — 3–6% (w/v) NaCl | organism/taxon, phenotype | label-only: Spiribacter halobius; METPO:1000532 | “both are able to grow from 0.5 to 16% (w/v) NaCl, showing optimal growth at 3–6% (w/v) NaCl” (leon2024integratinggenomicevidence pages 1-2) | DOI:10.1038/s41598-024-80127-5 · https://doi.org/10.1038/s41598-024-80127-5 | Dec 2024 | Boundary-case example showing within-genus heterogeneity; taxon-specific. |
| Compatible-solute synthesis/transport genes — supports — survival up to 25% NaCl | genes/pathway, phenotype | label-only: compatible-solute synthesis genes; label-only: compatible-solute transport genes | “could survive in high salinity up to 25% (w/v) NaCl… genes related to the synthesis and transport of compatible solutes” (sharma2023genomeanalysisof pages 1-2) | DOI:10.3389/fmicb.2023.1229955 · https://doi.org/10.3389/fmicb.2023.1229955 | Sep 2023 | Moderate evidence because genomic presence and phenotype co-occur but are not directly perturbed. Taxon-specific. |
| Halomicroarcula salt-in strategy — may_be_complemented_by — trehalose and glycine betaine biosynthesis | pathway/process, metabolites | CHEBI:16551 trehalose; CHEBI:17750 glycine betaine; label-only: Halomicroarcula | “typically use the ‘salt-in’ strategy… encode complete pathways for the biosynthesis of the osmotic solutes trehalose and glycine betaine” (oren2024novelinsightsinto pages 1-2) | DOI:10.1038/s44185-024-00050-w · https://doi.org/10.1038/s44185-024-00050-w | Aug 2024 | Suggests mixed strategy potential; evidence is comparative genomic and should be marked uncertain for direct function. |
| Growth at >100–150 g/L dissolved salts — operationally_defines — halophilic salinity phenotype scope | environment/phenotype definition | ENVO:01000358 hypersaline environment; METPO:1000532 | “operationally defined as organisms… growing at >100–150 g/L dissolved salts” (oren2024novelinsightsinto pages 1-2) | DOI:10.1038/s44185-024-00050-w · https://doi.org/10.1038/s44185-024-00050-w | Aug 2024 | Scope/definition edge, useful for ontology note rather than mechanism. |


*Table: This table lists candidate subject–predicate–object edges for curating a TraitMech graph of microbial salinity phenotype with numerical limits. It prioritizes general osmoadaptation mechanisms and assay edges, while also flagging a few strong but taxon-specific perturbation findings.*

## 8) Warnings / curation caveats (do not curate without more support)

1. **Generalizing from taxon-specific perturbations:** Edges such as ΔectABC → reduced max growth salinity and engineered proline overproduction → increased max growth salinity are extremely strong but demonstrated in *Halomonas elongata* under specific minimal-media conditions; curate as **taxon/assay-specific** unless replicated across taxa (khanh2024metabolicpathwayengineering pages 1-2).

2. **Proteome acidity as a causal determinant:** The association between acidified proteomes and salt-saturating growth is strong but often derived from comparative inference rather than direct intervention; curate as **enables/associated_with** unless experimental causality is available (gutierrezpreciado2024extremelyacidicproteomes pages 1-4).

3. **Salt composition confounding:** High Mg/Ca/Li/Fe can reduce habitability independent of NaCl concentration; numeric NaCl limits alone may be misleading across thalassohaline vs athalassohaline or chaotropic brines. Curate explicit **chemical context nodes** if available (gutierrezpreciado2024extremelyacidicproteomes pages 1-4).

4. **Foundational review not retrievable here:** The commonly cited osmoadaptation review DOI:10.1093/femsre/fuy009 (2018) was identified but not obtainable via tools in this run, so its specific classification schemes/quotes were not used as primary evidence.

## 9) DOI-first bibliography (with URLs, publication dates)

1. **Xing Q, Zhang S, Tao X, Mesbah NM, Mao X, Wang H, Wiegel J, Zhao B.** *The polyextremophile Natranaerobius thermophilus adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and K+.* **Applied and Environmental Microbiology**. Published **Apr 2024** (online); issue month **May 2024**. DOI: **10.1128/aem.00145-24**. URL: https://doi.org/10.1128/aem.00145-24 (xing2024thepolyextremophilenatranaerobius pages 1-2)

2. **Khanh HC, Kaothien-Nakayama P, Zou Z, Nakayama H.** *Metabolic pathway engineering of high-salinity-induced overproduction of L-proline improves high-salinity stress tolerance of an ectoine-deficient Halomonas elongata.* **Applied and Environmental Microbiology**. Published **Aug 2024** (online); issue month **Sep 2024**. DOI: **10.1128/aem.01195-24**. URL: https://doi.org/10.1128/aem.01195-24 (khanh2024metabolicpathwayengineering pages 1-2)

3. **Oren A.** *Novel insights into the diversity of halophilic microorganisms and their functioning in hypersaline ecosystems.* **npj Biodiversity**. **Aug 2024**. DOI: **10.1038/s44185-024-00050-w**. URL: https://doi.org/10.1038/s44185-024-00050-w (oren2024novelinsightsinto pages 1-2)

4. **Gutiérrez-Preciado A, Dede B, Baker BA, Eme L, Moreira D, López-García P.** *Extremely acidic proteomes and metabolic flexibility in bacteria and highly diversified archaea thriving in geothermal chaotropic brines.* **Nature Ecology & Evolution**. **Aug 2024**. DOI: **10.1038/s41559-024-02505-6**. URL: https://doi.org/10.1038/s41559-024-02505-6 (gutierrezpreciado2024extremelyacidicproteomes pages 1-4)

5. **Ionescu D, Zoccarato L, Cabello-Yeves PJ, Tikochinski Y.** *Extreme fluctuations in ambient salinity select for bacteria with a hybrid “salt-in”/”salt-out” osmoregulation strategy.* **Frontiers in Microbiomes**. **Jan 2024**. DOI: **10.3389/frmbi.2023.1329925**. URL: https://doi.org/10.3389/frmbi.2023.1329925 (ionescu2024extremefluctuationsin pages 1-2)

6. **León MJ, Vera-Gargallo B, de la Haba RR, Sánchez-Porro C, Ventosa A.** *Integrating genomic evidence for an updated taxonomy of the bacterial genus Spiribacter.* **Scientific Reports**. **Dec 2024**. DOI: **10.1038/s41598-024-80127-5**. URL: https://doi.org/10.1038/s41598-024-80127-5 (leon2024integratinggenomicevidence pages 1-2)

7. **Galisteo C, de la Haba RR, Ventosa A, Sánchez-Porro C.** *The Hypersaline Soils of the Odiel Saltmarshes Natural Area as a Source for Uncovering a New Taxon: Pseudidiomarina terrestris sp. nov.* **Microorganisms**. **Feb 2024**. DOI: **10.3390/microorganisms12020375**. URL: https://doi.org/10.3390/microorganisms12020375 (galisteo2024thehypersalinesoils pages 4-5)

8. **Sharma A, Singh RN, Song X-P, et al.** *Genome analysis of a halophilic Virgibacillus halodenitrificans ASH15 revealed salt adaptation, plant growth promotion, and isoprenoid biosynthetic machinery.* **Frontiers in Microbiology**. **Sep 2023**. DOI: **10.3389/fmicb.2023.1229955**. URL: https://doi.org/10.3389/fmicb.2023.1229955 (sharma2023genomeanalysisof pages 1-2)


References

1. (galisteo2024thehypersalinesoils pages 4-5): Cristina Galisteo, Rafael R. de la Haba, Antonio Ventosa, and Cristina Sánchez-Porro. The hypersaline soils of the odiel saltmarshes natural area as a source for uncovering a new taxon: pseudidiomarina terrestris sp. nov. Microorganisms, 12:375, Feb 2024. URL: https://doi.org/10.3390/microorganisms12020375, doi:10.3390/microorganisms12020375. This article has 8 citations.

2. (oren2024novelinsightsinto pages 1-2): Aharon Oren. Novel insights into the diversity of halophilic microorganisms and their functioning in hypersaline ecosystems. npj Biodiversity, Aug 2024. URL: https://doi.org/10.1038/s44185-024-00050-w, doi:10.1038/s44185-024-00050-w. This article has 65 citations and is from a peer-reviewed journal.

3. (xing2024thepolyextremophilenatranaerobius pages 1-2): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

4. (ionescu2024extremefluctuationsin pages 1-2): Danny Ionescu, Luca Zoccarato, Pedro J. Cabello-Yeves, and Yaron Tikochinski. Extreme fluctuations in ambient salinity select for bacteria with a hybrid “salt-in”/”salt-out” osmoregulation strategy. Frontiers in Microbiomes, Jan 2024. URL: https://doi.org/10.3389/frmbi.2023.1329925, doi:10.3389/frmbi.2023.1329925. This article has 11 citations.

5. (gutierrezpreciado2024extremelyacidicproteomes pages 1-4): Ana Gutiérrez-Preciado, Bledina Dede, Brittany A. Baker, Laura Eme, David Moreira, and Purificación López-García. Extremely acidic proteomes and metabolic flexibility in bacteria and highly diversified archaea thriving in geothermal chaotropic brines. Aug 2024. URL: https://doi.org/10.1038/s41559-024-02505-6, doi:10.1038/s41559-024-02505-6. This article has 23 citations and is from a highest quality peer-reviewed journal.

6. (xing2024thepolyextremophilenatranaerobius pages 6-7): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

7. (khanh2024metabolicpathwayengineering pages 1-2): Huynh Cong Khanh, Pulla Kaothien-Nakayama, Ziyan Zou, and Hideki Nakayama. Metabolic pathway engineering of high-salinity-induced overproduction of l-proline improves high-salinity stress tolerance of an ectoine-deficient <i>halomonas elongata</i>. Applied and Environmental Microbiology, Sep 2024. URL: https://doi.org/10.1128/aem.01195-24, doi:10.1128/aem.01195-24. This article has 12 citations and is from a peer-reviewed journal.

8. (sharma2023genomeanalysisof pages 1-2): Anjney Sharma, Ram Nageena Singh, Xiu-Peng Song, Rajesh Kumar Singh, Dao-Jun Guo, Pratiksha Singh, Krishan K. Verma, and Yang-Rui Li. Genome analysis of a halophilic virgibacillus halodenitrificans ash15 revealed salt adaptation, plant growth promotion, and isoprenoid biosynthetic machinery. Frontiers in Microbiology, Sep 2023. URL: https://doi.org/10.3389/fmicb.2023.1229955, doi:10.3389/fmicb.2023.1229955. This article has 25 citations and is from a peer-reviewed journal.

9. (leon2024integratinggenomicevidence pages 1-2): María José León, Blanca Vera-Gargallo, Rafael R. de la Haba, Cristina Sánchez-Porro, and Antonio Ventosa. Integrating genomic evidence for an updated taxonomy of the bacterial genus spiribacter. Scientific Reports, Dec 2024. URL: https://doi.org/10.1038/s41598-024-80127-5, doi:10.1038/s41598-024-80127-5. This article has 1 citations and is from a peer-reviewed journal.

10. (xing2024thepolyextremophilenatranaerobius media 12691245): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

11. (xing2024thepolyextremophilenatranaerobius media 7b23b5ec): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

12. (xing2024thepolyextremophilenatranaerobius media 8dbe034b): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

13. (xing2024thepolyextremophilenatranaerobius media 41b42098): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.