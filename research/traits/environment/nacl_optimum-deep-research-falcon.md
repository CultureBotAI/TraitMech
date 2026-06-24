---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T23:07:21.162601'
end_time: '2026-06-17T23:23:36.668354'
duration_seconds: 975.51
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: NaCl optimum
  trait_identifier: METPO:1000333
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: nacl_optimum
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A salinity phenotype with numerical limits that supports the most efficient
    growth and reproduction of an organism.
  parent_traits: METPO:1000532, METPO:1000536
  synonyms: ''
  evidence_summary: 'DOI:10.1093/femsre/fuy009: optimal NaCl (Osmoadaptation review
    supports the NaCl concentration at which growth rate is maximal as a standard
    halophily descriptor.) | DOI:10.1186/1746-1448-4-2: ways they cope with the high
    salt concentrations (Saline-Systems review supports osmotic balance at the optimal
    NaCl as the mechanistic basis of the NaCl-optimum phenotype.)'
  causal_graph_summary: 'nacl_optimum_balanced_osmoadaptation: 6 nodes, 5 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 40
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** NaCl optimum
- **METPO identifier:** METPO:1000333
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A salinity phenotype with numerical limits that supports the most efficient growth and reproduction of an organism.
- **Parent traits:** METPO:1000532, METPO:1000536
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuy009: optimal NaCl (Osmoadaptation review supports the NaCl concentration at which growth rate is maximal as a standard halophily descriptor.) | DOI:10.1186/1746-1448-4-2: ways they cope with the high salt concentrations (Saline-Systems review supports osmotic balance at the optimal NaCl as the mechanistic basis of the NaCl-optimum phenotype.)
- **Existing causal graph summary:** nacl_optimum_balanced_osmoadaptation: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **NaCl optimum** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_optimum.yaml`.

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
- **Trait label:** NaCl optimum
- **METPO identifier:** METPO:1000333
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A salinity phenotype with numerical limits that supports the most efficient growth and reproduction of an organism.
- **Parent traits:** METPO:1000532, METPO:1000536
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuy009: optimal NaCl (Osmoadaptation review supports the NaCl concentration at which growth rate is maximal as a standard halophily descriptor.) | DOI:10.1186/1746-1448-4-2: ways they cope with the high salt concentrations (Saline-Systems review supports osmotic balance at the optimal NaCl as the mechanistic basis of the NaCl-optimum phenotype.)
- **Existing causal graph summary:** nacl_optimum_balanced_osmoadaptation: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **NaCl optimum** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_optimum.yaml`.

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


# Microbial Trait Causal Graph Curation Report: **NaCl optimum** (METPO:1000333)

## 1) Scope summary (trait meaning, boundaries, and assay context)

**Trait definition (curation-ready):** *NaCl optimum* is the **NaCl concentration (or salinity proxy such as % seawater)** at which an organism shows **maximal growth performance** under the defined experimental conditions (medium composition, temperature, pH, aeration, etc.). In recent experimental practice, this is operationalized by **growth curves and derived growth rate/doubling time**, typically from OD600 turbidity time courses across a salinity series (matarredona2024understandingthetolerance pages 2-4, matarredona2024understandingthetolerance pages 1-2).

**How it is measured in current studies:** A recent haloarchaeal study determined optimal salinity by running growth curves across a matrix of **10 salinity levels × 7 temperatures** (70 conditions) and computing growth descriptors (growth rate and doubling time), then selecting the salinity giving maximal growth (matarredona2024understandingthetolerance pages 2-4, matarredona2024understandingthetolerance pages 4-6). Visual summaries of growth rate vs salinity and temperature (Figures 1–3) provide an explicit “growth landscape” for locating the optimum (matarredona2024understandingthetolerance media 11286b50, matarredona2024understandingthetolerance media e30dd3a1, matarredona2024understandingthetolerance media 5268184b).

**Distinguish from nearby traits (boundary cases):**
- **NaCl requirement (minimum salinity for growth):** Some taxa “require a minimum salt concentration” for growth; this is distinct from the optimum (matarredona2024understandingthetolerance pages 1-2).
- **NaCl tolerance range (min–max salinity):** Growth across a range (e.g., 3–27% NaCl) does not specify the optimum; optimum is a point (or narrow band) within the range (leon2024integratinggenomicevidence pages 1-2).
- **Halophily class descriptors (moderate/extreme; obligately halophilic):** Many taxonomic descriptions report NaCl growth ranges and optima to categorize organisms (e.g., moderate halophiles vs extreme/obligate halophiles) (leon2024integratinggenomicevidence pages 1-2, garciaroldan2023genomicbasedphylogeneticand pages 1-2).
- **Water activity / osmolarity:** NaCl optimum is NaCl-specific and can differ from optima under other salts/osmolytes; e.g., chloride-specific toxicity can trigger distinct responses compared with MgSO4 even at comparable osmotic stress (corbett2021examiningtheosmotic pages 10-11). This is a warning against treating “osmolarity optimum” as identical to “NaCl optimum.”

## 2) Key concepts and current understanding (mechanistic framing)

### 2.1 Canonical mechanistic basis: osmoadaptation strategies
A widely used mechanistic framing distinguishes two major strategies for osmotic balance in high salt:

1. **“Salt-in” strategy:** cells **accumulate molar KCl** to match external osmolarity. This requires adaptation of intracellular enzymes to function at near-saturating salts; organisms using this strategy have a **highly acidic proteome** and often show poor survival at low salt because proteins denature (reang2024extremozymesandcompatible pages 1-2).

2. **“Salt-out / compatible-solute” strategy:** cells **exclude salt from the cytoplasm** and instead **synthesize and/or accumulate organic compatible solutes** that do not interfere with enzymatic activity, enabling broader salinity tolerance (reang2024extremozymesandcompatible pages 1-2).

These strategies (and hybrids of both) mechanistically set the position of **NaCl optimum** by determining where cellular homeostasis is least costly/most effective.

### 2.2 Hybrid strategies and scalable responses (2024 evidence)
A 2024 *Applied and Environmental Microbiology* study of the polyextremophile **Natranaerobius thermophilus** reports a **hybrid strategy** using both compatible solutes and K+ accumulation, with explicit molecular systems implicated: glycine betaine ABC transporters (Opu/ProU), Na+/solute symporters, glutamate and proline synthesis, and upregulation of Na+/K+/H+ transporters for ion homeostasis (xing2024thepolyextremophilenatranaerobius pages 1-2). Importantly, intracellular compatible solute content (including glycine betaine) increases with rising salinity (xing2024thepolyextremophilenatranaerobius pages 1-2), demonstrating a quantitative physiological axis that can shift the growth optimum.

### 2.3 Transporter-centered view: Na+ extrusion and osmolyte uptake
- **Na+/H+ antiport:** 2023 functional characterization of two NhaC-family antiporters from an extremely halophilic archaeon showed that heterologous expression in salt-sensitive *E. coli* increased NaCl tolerance from inability to grow at 0.2 M NaCl (control) to tolerance of 0.6–0.7 M NaCl, and also increased alkaline pH tolerance (wang2023characterizationoftwo pages 7-8). This supports antiport as a causal mechanism controlling Na+ toxicity and hence salinity performance.
- **Osmolyte transport vs de novo synthesis:** In *Halomonas elongata*, compatible-solute **uptake is preferred over de novo synthesis** (energetically) (hobmeier2022adaptationtovarying pages 1-2). This implies that media composition (presence of osmoprotectants) can shift observed NaCl optima—an important assay factor for curation.

## 3) Recent developments and latest research (prioritizing 2023–2024)

### 3.1 High-throughput “stress landscape” phenotyping of NaCl optima (2024)
Matarredona et al. (Nov 2024) quantified growth rates across salinity–temperature matrices for nine haloarchaea, defining optimal salinity empirically and providing derived tolerance metrics (e.g., “tolerance coefficient,” GR50 concepts) (matarredona2024understandingthetolerance pages 2-4, matarredona2024understandingthetolerance pages 4-6). Figures explicitly visualize optimal zones and tradeoffs between maximal growth rate and breadth of tolerance across conditions (matarredona2024understandingthetolerance media 11286b50, matarredona2024understandingthetolerance media e30dd3a1, matarredona2024understandingthetolerance media 5268184b).

### 3.2 Genomics-guided taxonomy links NaCl optimum to osmoprotectant gene repertoires (2024)
León et al. (Dec 2024) uses NaCl growth ranges and optima as phenotypic criteria in an updated taxonomy of **Spiribacter**, noting typical growth optima around **10–15% NaCl** for many species (moderate halophiles), with notable exceptions in some taxa with lower optima (3–6%) (leon2024integratinggenomicevidence pages 1-2). The study highlights genes involved in osmoprotectant metabolism (e.g., proline-related pathways) and transporters as part of osmotic balance in hypersaline environments (leon2024integratinggenomicevidence pages 1-2).

### 3.3 Proteome acidification and life near salt-saturation limits (2024)
Metagenome/MAG analysis of near life-limiting chaotropic brines reports that salt-in haloarchaea can accumulate very high cytoplasmic K+ and have extremely acidic proteomes (very low median pI), emphasizing proteome-level adaptation as a mechanistic determinant of extreme halophily (xing2024thepolyextremophilenatranaerobius pages 10-14).

### 3.4 Dual “salt-in/salt-out” systems as an adaptation to fluctuating salinity (2024)
Recent work also argues that fluctuating salinity can select for organisms carrying genes for both salt-in and salt-out strategies, reinforcing the need to represent *hybrid osmoregulation* as a causal-graph intermediate rather than forcing a binary classification (xing2024thepolyextremophilenatranaerobius pages 24-25).

## 4) Current applications and real-world implementations (NaCl optimum as a usable trait)

1. **Bioprocessing and enzyme/biocatalyst deployment at high salt:** Halophiles (including haloarchaea) are being positioned as robust chassis for “green chemistry” and extremozymes, where salinity optima/tolerance define operating windows and contamination resistance (matarredona2024understandingthetolerance pages 2-4).

2. **Environmental biotechnology in brines (bioremediation, metal tolerance):** Haloarchaeal stress landscape phenotyping combined growth and ionic measurements (ICP-MS) to connect physiological performance under optimal salinity with stressor tolerance profiles relevant to brine treatment contexts (matarredona2024understandingthetolerance pages 2-4).

3. **Agriculture and salinized soils (microbial inoculants):** A 2024 isolation/characterization study reports a bacterium with NaCl optimum around 6% and production of **proline (osmoprotectant)**, positioned as a candidate plant-growth-promoting bacterium to enhance plant salt tolerance (peng2024improvingplantsalt pages 1-2).

## 5) Expert opinions / authoritative synthesis (with curation cautions)

**Authoritative consensus:** Osmoadaptation strategy (salt-in vs salt-out) is the dominant mechanistic explanation for salinity growth behavior, including optima (reang2024extremozymesandcompatible pages 1-2). Recent primary studies support that **transport systems (antiporters and osmolyte transporters)** and **compatible-solute pools** provide a tunable physiological “control system” that shapes performance across salt gradients, consistent with this conceptual framework (xing2024thepolyextremophilenatranaerobius pages 1-2, wang2023characterizationoftwo pages 7-8).

**Curation caution (expert-style analysis):**
- NaCl optimum is **context-dependent**: temperature, pH, medium composition, and osmolyte availability can shift the measured optimum (matarredona2024understandingthetolerance pages 2-4, hobmeier2022adaptationtovarying pages 1-2, wang2023characterizationoftwo pages 7-8).
- Some responses are **anion-specific**: chloride toxicity can induce ectoine responses that may not appear under sulfate salts, so “NaCl optimum” should not be generalized to “osmotic optimum” without evidence (corbett2021examiningtheosmotic pages 10-11).

## 6) Candidate causal-graph nodes (ontology-grounded where possible)

| Type | Node label | Suggested grounding | Notes | Key supporting source (with DOI) |
|---|---|---|---|---|
| Environmental factor | external NaCl concentration / salinity | CHEBI:26710 (sodium chloride) | Primary environmental variable used to define NaCl optimum in growth assays (matarredona2024understandingthetolerance pages 2-4, matarredona2024understandingthetolerance pages 4-6, garciaroldan2023genomicbasedphylogeneticand pages 1-2) | Matarredona et al. 2024, doi:10.1111/1758-2229.70039 |
| Environmental factor | temperature | ENVO:09200014 (temperature) | Co-varies with salinity in growth landscapes and changes inferred optimum conditions (matarredona2024understandingthetolerance pages 2-4, matarredona2024understandingthetolerance media 11286b50) | Matarredona et al. 2024, doi:10.1111/1758-2229.70039 |
| Environmental factor | pH | ENVO:09200019 (pH) | Alters antiporter activity and salt-growth performance, especially in haloalkaliphiles (wang2023characterizationoftwo pages 7-8) | Wang et al. 2023, doi:10.3390/ijms241310786 |
| Environmental factor | ecological niche in hypersaline habitats | ENVO:01000309 (hypersaline habitat) | Habitat salinity distribution supports ecological relevance of measured NaCl optima (leon2024integratinggenomicevidence pages 1-2, garciaroldan2023genomicbasedphylogeneticand pages 1-2) | León et al. 2024, doi:10.1038/s41598-024-80127-5 |
| Assay factor | growth rate | GO:0016049 | Common operational criterion for locating optimum salinity in matrix assays (matarredona2024understandingthetolerance pages 2-4, matarredona2024understandingthetolerance pages 4-6) | Matarredona et al. 2024, doi:10.1111/1758-2229.70039 |
| Assay factor | optical density at 600 nm (OD600) | unmapped | Standard readout used to derive growth curves, rates, and doubling times (matarredona2024understandingthetolerance pages 1-2, wang2023characterizationoftwo pages 10-12) | Matarredona et al. 2024, doi:10.1111/1758-2229.70039 |
| Assay factor | doubling time | GO:0009848 | Secondary descriptor used with growth rate to compare salinity responses (matarredona2024understandingthetolerance pages 4-6) | Matarredona et al. 2024, doi:10.1111/1758-2229.70039 |
| Physiological state | intracellular K+ accumulation | CHEBI:29103 (potassium(1+)) | Canonical salt-in osmoadaptation feature under high salinity (reang2024extremozymesandcompatible pages 1-2, xing2024thepolyextremophilenatranaerobius pages 1-2) | Xing et al. 2024, doi:10.1128/aem.00145-24 |
| Physiological state | cytoplasmic Na+ homeostasis | GO:0055078 | Maintained by antiporters to prevent Na+ toxicity across salinities (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 19-21) | Xing et al. 2024, doi:10.1128/aem.00145-24 |
| Physiological state | acidic proteome / low-pI proteome | GO:0016987 | Proteome acidification supports function in high intracellular salt (reang2024extremozymesandcompatible pages 1-2, xing2024thepolyextremophilenatranaerobius pages 1-2) | Gutiérrez-Preciado et al. 2024, doi:10.1038/s41559-024-02505-6 |
| Physiological state | chloride toxicity response | CHEBI:17996 (chloride) | Cl− can specifically trigger ectoine-centered osmotic stress responses (corbett2021examiningtheosmotic pages 10-11) | Corbett et al. 2021, doi:10.3390/microorganisms10010022 |
| Physiological state | genome streamlining | GO:0016999 | Proposed adaptation associated with survival in hypersaline, nutrient-limited settings; indirect link to NaCl optimum (leon2024integratinggenomicevidence pages 1-2) | León et al. 2024, doi:10.1038/s41598-024-80127-5 |
| Pathway/process | salt-in strategy | GO:0006970 | Osmotic balance by accumulating inorganic ions, typically KCl (reang2024extremozymesandcompatible pages 1-2, xing2024thepolyextremophilenatranaerobius pages 1-2) | Oren 2008, doi:10.1186/1746-1448-4-2 |
| Pathway/process | compatible-solute accumulation / salt-out strategy | GO:0006970 | Osmotic balance by excluding salt and accumulating organic osmolytes (reang2024extremozymesandcompatible pages 1-2, abosamaha2022utilizationandaccumulation pages 1-2) | Oren 2008, doi:10.1186/1746-1448-4-2 |
| Pathway/process | compatible-solute biosynthesis | GO:0009073 | Includes de novo synthesis of ectoine, hydroxyectoine, proline, glutamate, betaine (xing2024thepolyextremophilenatranaerobius pages 1-2, abosamaha2022utilizationandaccumulation pages 1-2) | Xing et al. 2024, doi:10.1128/aem.00145-24 |
| Pathway/process | compatible-solute transport | GO:0015840 | Import often preferred over synthesis; transporter repertoire shapes salt adaptation (xing2024thepolyextremophilenatranaerobius pages 14-17, hobmeier2022adaptationtovarying pages 1-2) | Xing et al. 2024, doi:10.1128/aem.00145-24 |
| Pathway/process | metagenomic recruitment / niche occupancy | GO:0008150 | Environmental abundance at intermediate/high salinities supports trait relevance but is not mechanistic alone (leon2024integratinggenomicevidence pages 1-2, garciaroldan2023genomicbasedphylogeneticand pages 1-2) | García-Roldán et al. 2023, doi:10.3389/fmicb.2023.1109549 |
| Gene/protein/complex | NhaC-family Na+/H+ antiporter | TCDB:2.A.35 | Heterologous expression increases NaCl, LiCl, and alkaline pH tolerance (wang2023characterizationoftwo pages 7-8) | Wang et al. 2023, doi:10.3390/ijms241310786 |
| Gene/protein/complex | Na+(K+,Li+)/H+ antiporter | TCDB:2.A.35 | Broader cation/H+ exchange activity linked to salt and pH adaptation (wang2023characterizationoftwo pages 7-8) | Wang et al. 2023, doi:10.3390/ijms241310786 |
| Gene/protein/complex | Opu-family glycine betaine ABC transporter | TCDB:3.A.1 | Major uptake system for glycine betaine under high salinity (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 14-17) | Xing et al. 2024, doi:10.1128/aem.00145-24 |
| Gene/protein/complex | ProU-family glycine betaine/proline ABC transporter | TCDB:3.A.1 | Supports osmolyte import during high-salt adaptation (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 14-17) | Xing et al. 2024, doi:10.1128/aem.00145-24 |
| Gene/protein/complex | BetT choline transporter | TCDB:2.A.15 | Supports choline uptake for glycine betaine synthesis (xing2024thepolyextremophilenatranaerobius pages 14-17) | Xing et al. 2024, doi:10.1128/aem.00145-24 |
| Gene/protein/complex | PutP Na+/proline symporter | TCDB:2.A.21 | Links Na+ coupling to proline uptake during osmoadaptation (xing2024thepolyextremophilenatranaerobius pages 14-17, xing2024thepolyextremophilenatranaerobius pages 17-19) | Xing et al. 2024, doi:10.1128/aem.00145-24 |
| Gene/protein/complex | TeaABC TRAP transporter | TCDB:2.A.56 | Ectoine-specific transporter system relevant to ectoine flux in Halomonas; taxon-specific (hobmeier2022adaptationtovarying pages 1-2) | Hobmeier et al. 2022, doi:10.3389/fmicb.2022.846677 |
| Metabolite/ion | glycine betaine | CHEBI:17750 | Major compatible solute; intracellular levels rise with salinity (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 17-19) | Xing et al. 2024, doi:10.1128/aem.00145-24 |
| Metabolite/ion | ectoine | CHEBI:28885 | Canonical compatible solute; often induced by NaCl/Cl− stress (abosamaha2022utilizationandaccumulation pages 1-2, corbett2021examiningtheosmotic pages 10-11) | Corbett et al. 2021, doi:10.3390/microorganisms10010022 |
| Metabolite/ion | hydroxyectoine | CHEBI:60300 | Accumulates at very high salinity in some moderate halophiles (abosamaha2022utilizationandaccumulation pages 1-2) | Abosamaha et al. 2022, doi:10.1099/acmi.0.000359 |
| Metabolite/ion | proline | CHEBI:17203 | Functions as compatible solute and/or imported osmoprotectant (peng2024improvingplantsalt pages 1-2, xing2024thepolyextremophilenatranaerobius pages 1-2) | Peng et al. 2024, doi:10.3389/fmicb.2024.1466733 |
| Metabolite/ion | glutamate | CHEBI:18237 | Accumulates as osmolyte in hybrid salt-adaptation systems (xing2024thepolyextremophilenatranaerobius pages 1-2, xing2024thepolyextremophilenatranaerobius pages 17-19) | Xing et al. 2024, doi:10.1128/aem.00145-24 |
| Metabolite/ion | Na+ | CHEBI:29101 | External stressor and exchanged substrate for antiport-mediated homeostasis (wang2023characterizationoftwo pages 7-8, xing2024thepolyextremophilenatranaerobius pages 19-21) | Wang et al. 2023, doi:10.3390/ijms241310786 |
| Metabolite/ion | K+ | CHEBI:29103 | Principal intracellular counterion in salt-in adaptation (reang2024extremozymesandcompatible pages 1-2, xing2024thepolyextremophilenatranaerobius pages 1-2) | Oren 2008, doi:10.1186/1746-1448-4-2 |
| Metabolite/ion | Cl− | CHEBI:17996 | Counterion in salt-in systems and specific toxic trigger in some taxa (xing2024thepolyextremophilenatranaerobius pages 14-17, corbett2021examiningtheosmotic pages 10-11) | Corbett et al. 2021, doi:10.3390/microorganisms10010022 |


*Table: This table lists strongly supported candidate nodes for a TraitMech-style causal graph of NaCl optimum (METPO:1000333), grouped by node type. It highlights experimentally measured assay variables, osmoadaptation states, key pathways, transporters, and metabolites that recur across recent halophile studies.*

## 7) Candidate evidence-backed causal edges (triples) for TraitMech curation

| Subject node | Predicate | Object node | Evidence snippet | Source | Curation notes |
|---|---|---|---|---|---|
| external NaCl concentration | induces | osmotic stress | “Halophilic microorganisms use two strategies to balance their cytoplasm osmotically with their medium.” (reang2024extremozymesandcompatible pages 1-2) | Oren 2008. DOI: 10.1186/1746-1448-4-2. URL: https://doi.org/10.1186/1746-1448-4-2 | Broad review-level mechanism; supports upstream environmental driver rather than a gene-level edge. |
| salt-in strategy | increases | intracellular K+ accumulation | “The first involves accumulation of molar concentrations of KCl.” (reang2024extremozymesandcompatible pages 1-2) | Oren 2008. DOI: 10.1186/1746-1448-4-2. URL: https://doi.org/10.1186/1746-1448-4-2 | Strong general mechanism across extreme halophiles. |
| acidic proteome | enables | protein stability at high salt | “The proteome of such organisms is highly acidic” and this strategy “requires adaptation of the intracellular enzymatic machinery” at near-saturating salt concentrations. (reang2024extremozymesandcompatible pages 1-2) | Oren 2008. DOI: 10.1186/1746-1448-4-2. URL: https://doi.org/10.1186/1746-1448-4-2 | Mechanistic but somewhat coarse-grained; node could also be modeled as ‘adapted intracellular enzymatic machinery’. |
| acidic proteome | decreases | low-salt tolerance | “most proteins denature when suspended in low salt. Such microorganisms generally cannot survive in low salt media.” (reang2024extremozymesandcompatible pages 1-2) | Oren 2008. DOI: 10.1186/1746-1448-4-2. URL: https://doi.org/10.1186/1746-1448-4-2 | Strong for obligate salt-in organisms; not universal across all halophiles. |
| compatible-solute accumulation | maintains | osmotic balance | The second strategy is to “exclude salt from the cytoplasm and to synthesize and/or accumulate organic ‘compatible’ solutes that do not interfere with enzymatic activity.” (reang2024extremozymesandcompatible pages 1-2) | Oren 2008. DOI: 10.1186/1746-1448-4-2. URL: https://doi.org/10.1186/1746-1448-4-2 | Broad canonical mechanism; suitable central TraitMech edge. |
| compatible-solute accumulation | increases | growth at high salt | Addition of “glycine betaine (betaine) and ectoine … had a positive effect on growth of H. pacifica at 2 M NaCl.” (abosamaha2022utilizationandaccumulation pages 1-2) | Abosamaha et al. 2022. DOI: 10.1099/acmi.0.000359. URL: https://doi.org/10.1099/acmi.0.000359 | Taxon-specific experimental support in Halomonas pacifica; useful as direct phenotype link. |
| chloride toxicity | induces | ectC expression | “Exposure to high concentrations of Cl− resulted in the increase of ectC expression” and MgSO4 “did not trigger the same up-regulation of ectC.” (corbett2021examiningtheosmotic pages 10-11) | Corbett et al. 2021. DOI: 10.3390/microorganisms10010022. URL: https://doi.org/10.3390/microorganisms10010022 | Strong but taxon-specific to Acidihalobacter aeolianus; chloride-specific rather than NaCl-only. |
| ectC expression | increases | ectoine accumulation | “ectC expression is much higher under NaCl … and ectoine accumulates strongly under high NaCl (25.5-fold increase).” (corbett2021examiningtheosmotic pages 10-11) | Corbett et al. 2021. DOI: 10.3390/microorganisms10010022. URL: https://doi.org/10.3390/microorganisms10010022 | Taxon-specific; good gene-to-metabolite edge. |
| compatible solute uptake | associated_with | lower energetic cost than de novo synthesis | “uptake of compatible solute from the medium is preferred over de novo synthesis,” reflecting an energetically favored mechanism. (hobmeier2022adaptationtovarying pages 1-2) | Hobmeier et al. 2022. DOI: 10.3389/fmicb.2022.846677. URL: https://doi.org/10.3389/fmicb.2022.846677 | Good process-level edge; may be better modeled as preference/efficiency rather than direct trait edge. |
| NhaC-family antiporter expression | increases | NaCl tolerance | Expression of nhaC1 or nhaC2 allowed E. coli KNabc to tolerate “0.6 M/0.7 M NaCl,” whereas control “could not grow at 0.2 M NaCl.” (wang2023characterizationoftwo pages 7-8) | Wang et al. 2023. DOI: 10.3390/ijms241310786. URL: https://doi.org/10.3390/ijms241310786 | Strong functional evidence, but heterologous E. coli complementation assay; curate as assay-specific. |
| NhaC-family antiporter expression | increases | alkaline pH tolerance | “KNabc/nhaC1 grew to pH 8.5, while nhaC2 conferred resistance up to pH 9.5”; control was “almost unable to grow at pH 8.0.” (wang2023characterizationoftwo pages 7-8) | Wang et al. 2023. DOI: 10.3390/ijms241310786. URL: https://doi.org/10.3390/ijms241310786 | Useful context because pH modulates antiporter contribution to salt phenotype. |
| Na+/H+ antiport activity | maintains | cytoplasmic Na+ homeostasis | “Na+/H+ antiporters function to lower cytoplasmic Na+ to prevent toxicity” and likely contribute to salt acclimation. (xing2024thepolyextremophilenatranaerobius pages 19-21) | Xing et al. 2024. DOI: 10.1128/aem.00145-24. URL: https://doi.org/10.1128/aem.00145-24 | Strong mechanistic role; direct deletion evidence not shown in this excerpt. |
| Opu-family glycine betaine ABC transporter | increases | glycine betaine accumulation | “Specifically, N. thermophilus employs the glycine betaine ABC transporters (Opu and ProU families)… The intracellular content of compatible solutes, including glycine betaine … increases with rising salinity levels.” (xing2024thepolyextremophilenatranaerobius pages 1-2) | Xing et al. 2024. DOI: 10.1128/aem.00145-24. URL: https://doi.org/10.1128/aem.00145-24 | Strong, but transport-to-metabolite edge is inferred from co-occurrence/upregulation rather than transporter knockout. |
| ProU-family glycine betaine/proline ABC transporter | increases | glycine betaine accumulation | “glycine betaine ABC transporters (Opu and ProU families)” are part of adaptation, with glycine betaine increasing with salinity. (xing2024thepolyextremophilenatranaerobius pages 1-2) | Xing et al. 2024. DOI: 10.1128/aem.00145-24. URL: https://doi.org/10.1128/aem.00145-24 | Same caveat as Opu; transporter-specific direction is plausible but not individually dissected. |
| glycine betaine accumulation | associated_with | adaptation at higher Na+ | “The intracellular content of compatible solutes, including glycine betaine, glutamate, and proline, increases with rising salinity levels in N. thermophilus.” (xing2024thepolyextremophilenatranaerobius pages 1-2) | Xing et al. 2024. DOI: 10.1128/aem.00145-24. URL: https://doi.org/10.1128/aem.00145-24 | Strong correlation with salinity adaptation; direct causal sufficiency not isolated. |
| Na+/proline symporter PutP | enables | proline uptake | “Multiple transport systems relevant to uptake were detected … and the Na+/proline symporter PutP.” (xing2024thepolyextremophilenatranaerobius pages 14-17) | Xing et al. 2024. DOI: 10.1128/aem.00145-24. URL: https://doi.org/10.1128/aem.00145-24 | Transport function is clear; effect on NaCl optimum is indirect and taxon-specific. |
| temperature | associated_with | measured NaCl optimum | Growth curves were generated across “70 conditions (10 salinity levels × 7 temperatures)” and salinity giving maximal growth was identified within this landscape. (matarredona2024understandingthetolerance pages 2-4, matarredona2024understandingthetolerance media 11286b50) | Matarredona et al. 2024. DOI: 10.1111/1758-2229.70039. URL: https://doi.org/10.1111/1758-2229.70039 | Assay-factor edge; important for scope because NaCl optimum is condition-dependent. |
| pH | associated_with | measured NaCl optimum | NhaC antiport activities are “pH-dependent in the range of pH 7.0–10.0, and the optimal pH is 9.5.” (wang2023characterizationoftwo pages 7-8) | Wang et al. 2023. DOI: 10.3390/ijms241310786. URL: https://doi.org/10.3390/ijms241310786 | Assay/physiology interaction; pH modifies salinity performance especially in haloalkaliphiles. |
| ecological niche at intermediate salinity | associated_with | Spiribacter NaCl optimum | Spiribacter species are abundant “at intermediate salinities,” consistent with growth “between 10–15% NaCl” for most species. (leon2024integratinggenomicevidence pages 1-2) | León et al. 2024. DOI: 10.1038/s41598-024-80127-5. URL: https://doi.org/10.1038/s41598-024-80127-5 | Ecological association, not direct mechanism; useful supporting context only. |
| hypersaline habitat occupancy | associated_with | Natronomonas high NaCl optimum | Natronomonas species are “widely distributed in saline lakes and salterns as well as on saline soils” and are “extremely halophilic (optimal growth at 20–25% [w/v] NaCl).” (garciaroldan2023genomicbasedphylogeneticand pages 1-2) | García-Roldán et al. 2023. DOI: 10.3389/fmicb.2023.1109549. URL: https://doi.org/10.3389/fmicb.2023.1109549 | Ecological association; not itself a mechanistic edge to curate into core graph. |


*Table: This table compiles candidate evidence-backed causal edges for the microbial trait NaCl optimum, linking environmental salinity, osmoadaptation mechanisms, transporters, metabolites, and assay factors. It is designed to support TraitMech curation by separating strong mechanistic edges from taxon-specific or assay-specific associations.*

## 8) Quantitative statistics and data points (recent studies)

- **High-throughput NaCl optimum determination:** Growth landscapes were measured across **70 (salinity × temperature) conditions** per strain (10 salinity levels × 7 temperatures) to identify optimal salinity (matarredona2024understandingthetolerance pages 2-4, matarredona2024understandingthetolerance pages 4-6), with figures summarizing growth rates and optima across nine haloarchaea (matarredona2024understandingthetolerance media 11286b50, matarredona2024understandingthetolerance media e30dd3a1, matarredona2024understandingthetolerance media 5268184b).
- **Transporter functional effect size (direct):** NhaC antiporter expression in *E. coli* KNabc increased tolerance from no growth at **0.2 M NaCl** (control) to growth at **0.6–0.7 M NaCl** depending on the antiporter, and increased alkaline pH tolerance (to pH 8.5–9.5 vs ~8.0 control) (wang2023characterizationoftwo pages 7-8).
- **Compatible solute pool scaling with salinity (direct):** In *N. thermophilus*, intracellular glycine betaine increased dramatically with rising external Na+ (reported as 52.7 → 893.1 mM from 2.5 to 4.3 M Na+) alongside a dual strategy including K+ (xing2024thepolyextremophilenatranaerobius pages 17-19).

## 9) Warnings: claims that should not yet be curated into TraitMech (or should be marked uncertain)

1. **Ecological abundance ↔ NaCl optimum**: Metagenomic recruitment/abundance at certain salinities supports plausibility but is not a mechanistic causal edge; treat as contextual association, not core causation (leon2024integratinggenomicevidence pages 1-2, garciaroldan2023genomicbasedphylogeneticand pages 1-2).

2. **Transporter upregulation ↔ metabolite accumulation**: Edges linking Opu/ProU upregulation to glycine betaine accumulation are strongly plausible but often not demonstrated by knockouts in the cited excerpts; mark as **inferred unless genetic perturbation is available** (xing2024thepolyextremophilenatranaerobius pages 1-2).

3. **NhaC antiporter → NaCl optimum**: The 2023 evidence is strong but comes from **heterologous complementation in *E. coli***, not direct manipulation in the native archaeon; curate as mechanistic support for NaCl tolerance/Na+ homeostasis, but mark **assay-specific** and do not overinterpret as shifting a native organism’s exact optimum (wang2023characterizationoftwo pages 7-8).

---

# DOI-first bibliography (URLs and publication dates)

- **10.1111/1758-2229.70039** (Nov 2024). Matarredona L. et al. *Understanding the tolerance of halophilic archaea to stress landscapes*. Environmental Microbiology Reports. https://doi.org/10.1111/1758-2229.70039 (matarredona2024understandingthetolerance pages 2-4)
- **10.1038/s41598-024-80127-5** (Dec 2024). León M.J. et al. *Integrating genomic evidence for an updated taxonomy of the bacterial genus Spiribacter*. Scientific Reports. https://doi.org/10.1038/s41598-024-80127-5 (leon2024integratinggenomicevidence pages 1-2)
- **10.1128/aem.00145-24** (May 2024). Xing Q. et al. *Natranaerobius thermophilus adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and K+*. Applied and Environmental Microbiology. https://doi.org/10.1128/aem.00145-24 (xing2024thepolyextremophilenatranaerobius pages 1-2)
- **10.3390/ijms241310786** (Jun 2023). Wang Q. et al. *Characterization of Two Na+(K+, Li+)/H+ Antiporters from Natronorubrum daqingense*. International Journal of Molecular Sciences. https://doi.org/10.3390/ijms241310786 (wang2023characterizationoftwo pages 7-8)
- **10.3389/fmicb.2023.1109549** (Jan 2023). García-Roldán A. et al. *Genomic-based phylogenetic and metabolic analyses of the genus Natronomonas…*. Frontiers in Microbiology. https://doi.org/10.3389/fmicb.2023.1109549 (garciaroldan2023genomicbasedphylogeneticand pages 1-2)
- **10.3389/fmicb.2024.1466733** (Oct 2024). Peng Y. et al. *Improving plant salt tolerance through Algoriphagus halophytocola…*. Frontiers in Microbiology. https://doi.org/10.3389/fmicb.2024.1466733 (peng2024improvingplantsalt pages 1-2)
- **10.1038/s41559-024-02505-6** (Aug 2024). Gutiérrez-Preciado A. et al. *Extremely acidic proteomes and metabolic flexibility…*. Nature Ecology & Evolution. https://doi.org/10.1038/s41559-024-02505-6 (xing2024thepolyextremophilenatranaerobius pages 10-14)
- **10.3389/fmicb.2022.846677** (Mar 2022). Hobmeier K. et al. *Adaptation to varying salinity in Halomonas elongata: much more than ectoine accumulation*. Frontiers in Microbiology. https://doi.org/10.3389/fmicb.2022.846677 (hobmeier2022adaptationtovarying pages 1-2)
- **10.1099/acmi.0.000359** (May 2022). Abosamaha A. et al. *Utilization and accumulation of compatible solutes in Halomonas pacifica…*. Access Microbiology. https://doi.org/10.1099/acmi.0.000359 (abosamaha2022utilizationandaccumulation pages 1-2)
- **10.3390/microorganisms10010022** (Dec 2021). Corbett M.K. et al. *Examining the osmotic response of Acidihalobacter aeolianus after exposure to salt stress*. Microorganisms. https://doi.org/10.3390/microorganisms10010022 (corbett2021examiningtheosmotic pages 10-11)
- **10.1186/1746-1448-4-2** (Apr 2008). Oren A. *Microbial life at high salt concentrations: phylogenetic and metabolic diversity*. Saline Systems. https://doi.org/10.1186/1746-1448-4-2 (reang2024extremozymesandcompatible pages 1-2)


References

1. (matarredona2024understandingthetolerance pages 2-4): Laura Matarredona, Basilio Zafrilla, Mónica Camacho, María‐José Bonete, and Julia Esclapez. Understanding the tolerance of halophilic archaea to stress landscapes. Environmental Microbiology Reports, Nov 2024. URL: https://doi.org/10.1111/1758-2229.70039, doi:10.1111/1758-2229.70039. This article has 16 citations and is from a peer-reviewed journal.

2. (matarredona2024understandingthetolerance pages 1-2): Laura Matarredona, Basilio Zafrilla, Mónica Camacho, María‐José Bonete, and Julia Esclapez. Understanding the tolerance of halophilic archaea to stress landscapes. Environmental Microbiology Reports, Nov 2024. URL: https://doi.org/10.1111/1758-2229.70039, doi:10.1111/1758-2229.70039. This article has 16 citations and is from a peer-reviewed journal.

3. (matarredona2024understandingthetolerance pages 4-6): Laura Matarredona, Basilio Zafrilla, Mónica Camacho, María‐José Bonete, and Julia Esclapez. Understanding the tolerance of halophilic archaea to stress landscapes. Environmental Microbiology Reports, Nov 2024. URL: https://doi.org/10.1111/1758-2229.70039, doi:10.1111/1758-2229.70039. This article has 16 citations and is from a peer-reviewed journal.

4. (matarredona2024understandingthetolerance media 11286b50): Laura Matarredona, Basilio Zafrilla, Mónica Camacho, María‐José Bonete, and Julia Esclapez. Understanding the tolerance of halophilic archaea to stress landscapes. Environmental Microbiology Reports, Nov 2024. URL: https://doi.org/10.1111/1758-2229.70039, doi:10.1111/1758-2229.70039. This article has 16 citations and is from a peer-reviewed journal.

5. (matarredona2024understandingthetolerance media e30dd3a1): Laura Matarredona, Basilio Zafrilla, Mónica Camacho, María‐José Bonete, and Julia Esclapez. Understanding the tolerance of halophilic archaea to stress landscapes. Environmental Microbiology Reports, Nov 2024. URL: https://doi.org/10.1111/1758-2229.70039, doi:10.1111/1758-2229.70039. This article has 16 citations and is from a peer-reviewed journal.

6. (matarredona2024understandingthetolerance media 5268184b): Laura Matarredona, Basilio Zafrilla, Mónica Camacho, María‐José Bonete, and Julia Esclapez. Understanding the tolerance of halophilic archaea to stress landscapes. Environmental Microbiology Reports, Nov 2024. URL: https://doi.org/10.1111/1758-2229.70039, doi:10.1111/1758-2229.70039. This article has 16 citations and is from a peer-reviewed journal.

7. (leon2024integratinggenomicevidence pages 1-2): María José León, Blanca Vera-Gargallo, Rafael R. de la Haba, Cristina Sánchez-Porro, and Antonio Ventosa. Integrating genomic evidence for an updated taxonomy of the bacterial genus spiribacter. Scientific Reports, Dec 2024. URL: https://doi.org/10.1038/s41598-024-80127-5, doi:10.1038/s41598-024-80127-5. This article has 1 citations and is from a peer-reviewed journal.

8. (garciaroldan2023genomicbasedphylogeneticand pages 1-2): Alicia García-Roldán, Ana Durán-Viseras, Rafael R. de la Haba, Paulina Corral, Cristina Sánchez-Porro, and Antonio Ventosa. Genomic-based phylogenetic and metabolic analyses of the genus natronomonas, and description of natronomonas aquatica sp. nov. Frontiers in Microbiology, Jan 2023. URL: https://doi.org/10.3389/fmicb.2023.1109549, doi:10.3389/fmicb.2023.1109549. This article has 8 citations and is from a peer-reviewed journal.

9. (corbett2021examiningtheosmotic pages 10-11): Melissa K. Corbett, Liam Anstiss, April Gifford, Ross M. Graham, and Elizabeth L. J. Watkin. Examining the osmotic response of acidihalobacter aeolianus after exposure to salt stress. Microorganisms, 10:22, Dec 2021. URL: https://doi.org/10.3390/microorganisms10010022, doi:10.3390/microorganisms10010022. This article has 6 citations.

10. (reang2024extremozymesandcompatible pages 1-2): Likhindra Reang, Shraddha Bhatt, Rukam Singh Tomar, Kavita Joshi, Shital Padhiyar, Hiren Bhalani, JasminKumar Kheni, U. M. Vyas, and M. V. Parakhia. Extremozymes and compatible solute production potential of halophilic and halotolerant bacteria isolated from crop rhizospheric soils of southwest saurashtra gujarat. Scientific Reports, Jul 2024. URL: https://doi.org/10.1038/s41598-024-63581-z, doi:10.1038/s41598-024-63581-z. This article has 16 citations and is from a peer-reviewed journal.

11. (xing2024thepolyextremophilenatranaerobius pages 1-2): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

12. (wang2023characterizationoftwo pages 7-8): Qi Wang, Mengwei Qiao, and Jinzhu Song. Characterization of two na+(k+, li+)/h+ antiporters from natronorubrum daqingense. International Journal of Molecular Sciences, 24:10786, Jun 2023. URL: https://doi.org/10.3390/ijms241310786, doi:10.3390/ijms241310786. This article has 10 citations.

13. (hobmeier2022adaptationtovarying pages 1-2): Karina Hobmeier, Martina Cantone, Quynh Anh Nguyen, Katharina Pflüger-Grau, Andreas Kremling, Hans Jörg Kunte, Friedhelm Pfeiffer, and Alberto Marin-Sanguino. Adaptation to varying salinity in halomonas elongata: much more than ectoine accumulation. Frontiers in Microbiology, Mar 2022. URL: https://doi.org/10.3389/fmicb.2022.846677, doi:10.3389/fmicb.2022.846677. This article has 49 citations and is from a peer-reviewed journal.

14. (xing2024thepolyextremophilenatranaerobius pages 10-14): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

15. (xing2024thepolyextremophilenatranaerobius pages 24-25): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

16. (peng2024improvingplantsalt pages 1-2): Yuxin Peng, Dong Hyun Cho, Zalfa Humaira, Yu Lim Park, Ki Hyun Kim, Cha Young Kim, and Jiyoung Lee. Improving plant salt tolerance through algoriphagus halophytocola sp. nov., isolated from the halophyte salicornia europaea. Frontiers in Microbiology, Oct 2024. URL: https://doi.org/10.3389/fmicb.2024.1466733, doi:10.3389/fmicb.2024.1466733. This article has 9 citations and is from a peer-reviewed journal.

17. (wang2023characterizationoftwo pages 10-12): Qi Wang, Mengwei Qiao, and Jinzhu Song. Characterization of two na+(k+, li+)/h+ antiporters from natronorubrum daqingense. International Journal of Molecular Sciences, 24:10786, Jun 2023. URL: https://doi.org/10.3390/ijms241310786, doi:10.3390/ijms241310786. This article has 10 citations.

18. (xing2024thepolyextremophilenatranaerobius pages 19-21): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

19. (abosamaha2022utilizationandaccumulation pages 1-2): Abdolkader Abosamaha, Mike P. Williamson, and D. James Gilmour. Utilization and accumulation of compatible solutes in halomonas pacifica: a species of moderately halophilic bacteria isolated from a saline lake in south libya. May 2022. URL: https://doi.org/10.1099/acmi.0.000359, doi:10.1099/acmi.0.000359. This article has 16 citations.

20. (xing2024thepolyextremophilenatranaerobius pages 14-17): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.

21. (xing2024thepolyextremophilenatranaerobius pages 17-19): Qinghua Xing, Shanshan Zhang, Xinyi Tao, Noha M. Mesbah, Xinwei Mao, Haisheng Wang, Juergen Wiegel, and Baisuo Zhao. The polyextremophile <i>natranaerobius thermophilus</i> adopts a dual adaptive strategy to long-term salinity stress, simultaneously accumulating compatible solutes and k <sup>+</sup>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.00145-24, doi:10.1128/aem.00145-24. This article has 19 citations and is from a peer-reviewed journal.