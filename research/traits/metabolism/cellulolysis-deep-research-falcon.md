---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T04:20:54.877565'
end_time: '2026-06-18T04:39:56.549964'
duration_seconds: 1141.67
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: cellulolysis
  trait_identifier: traitmech:000111
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: cellulolysis
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A biopolymer-degradation metabolism in which an organism hydrolyzes
    cellulose to cellodextrins and glucose using cellulase systems, sometimes organized
    into cellulosomes.
  parent_traits: traitmech:000110
  synonyms: cellulolytic, cellulose degradation
  evidence_summary: 'DOI:10.1128/MMBR.66.3.506-577.2002:  (Lynd et al. review microbial
    cellulose utilization, its enzymology, and cellulosome systems.) | DOI:10.1016/j.cbpa.2015.10.018:  (Cragg
    et al. place cellulose deconstruction within lignocellulose degradation across
    diverse organisms.)'
  causal_graph_summary: 'cellulolysis_cellulase_systems: 3 nodes, 2 edges'
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
- **Trait label:** cellulolysis
- **METPO identifier:** traitmech:000111
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biopolymer-degradation metabolism in which an organism hydrolyzes cellulose to cellodextrins and glucose using cellulase systems, sometimes organized into cellulosomes.
- **Parent traits:** traitmech:000110
- **Synonyms:** cellulolytic, cellulose degradation
- **Existing evidence:** DOI:10.1128/MMBR.66.3.506-577.2002:  (Lynd et al. review microbial cellulose utilization, its enzymology, and cellulosome systems.) | DOI:10.1016/j.cbpa.2015.10.018:  (Cragg et al. place cellulose deconstruction within lignocellulose degradation across diverse organisms.)
- **Existing causal graph summary:** cellulolysis_cellulase_systems: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **cellulolysis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/cellulolysis.yaml`.

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
- **Trait label:** cellulolysis
- **METPO identifier:** traitmech:000111
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biopolymer-degradation metabolism in which an organism hydrolyzes cellulose to cellodextrins and glucose using cellulase systems, sometimes organized into cellulosomes.
- **Parent traits:** traitmech:000110
- **Synonyms:** cellulolytic, cellulose degradation
- **Existing evidence:** DOI:10.1128/MMBR.66.3.506-577.2002:  (Lynd et al. review microbial cellulose utilization, its enzymology, and cellulosome systems.) | DOI:10.1016/j.cbpa.2015.10.018:  (Cragg et al. place cellulose deconstruction within lignocellulose degradation across diverse organisms.)
- **Existing causal graph summary:** cellulolysis_cellulase_systems: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **cellulolysis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/cellulolysis.yaml`.

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


# Research Report: Microbial Trait “Cellulolysis” (traitmech:000111)

## 1) Scope summary (TraitMech curation view)
**Cellulolysis** is the microbial physiological capacity to depolymerize **cellulose (β-1,4-glucan)** into soluble **cellodextrins/cellobiose** and ultimately **glucose**, using extracellular hydrolytic cellulases and—in some organisms/conditions—**oxidative** cleavage enzymes (LPMOs). A minimal mechanistic definition supported by recent synthesis literature is that **complete conversion of cellulose to glucose requires concerted action of cellobiohydrolases, endoglucanases, and β‑glucosidases**. (gurovic2023regulationoflignocellulose pages 2-3)

**Boundary cases important for curation**:
- **Cellobiose utilization ≠ cellulolysis**: genes for cellobiose transport/utilization (e.g., PTS cel operon) can support growth on cellobiose without implying the organism can depolymerize insoluble cellulose. Conversely, extracellular cellulase activity without uptake/metabolism may appear “incomplete” in growth assays. (zhang2024transcriptionalregulationof pages 1-2, zhang2024transcriptionalregulationof pages 4-5, zhang2024unveilingaclassical pages 1-2)
- **Hemicellulolysis and ligninolysis are adjacent but distinct traits**: many cellulolytic systems co-express hemicellulases and oxidative enzymes acting on lignin, but those should be curated as neighboring traits/modules rather than conflated with cellulolysis. (gurovic2023regulationoflignocellulose pages 3-4, gurovic2023regulationoflignocellulose pages 2-3)
- **Oxygen effects**: cellulolysis is commonly studied under anoxic or aerobic bulk conditions; however, microoxic niches can enable oxygen-dependent oxidative enzymes that contribute to fiber depolymerization in situ (e.g., termite guts). (salgado2024unveilinglignocellulolyticpotential pages 1-2)

## 2) Key concepts and definitions (current understanding)
### 2.1 Canonical hydrolytic cellulase system
A widely used mechanistic schema is:
- **Endoglucanases** cleave internal β‑1,4 linkages,
- **Cellobiohydrolases/exoglucanases** release cellobiose/cellodextrins processively,
- **β‑glucosidases** hydrolyze cellobiose to glucose. (gurovic2023regulationoflignocellulose pages 2-3)

### 2.2 Cellulosomes (multienzyme complexes)
**Cellulosomes** are extracellular, multi-enzyme assemblies frequently found in anaerobic bacteria that can be **cell-attached or released**. Their architectural “rules” are:
- **Scaffoldin** forms the non-catalytic backbone,
- **Cohesin domains** on scaffoldin bind **dockerin domains** on catalytic subunits,
- Scaffoldins may include **carbohydrate-binding modules (CBMs)** to target the complex to substrate. (you2023insightsintolignocellulose pages 1-2, gurovic2023regulationoflignocellulose pages 3-4)

A soil cellulolysis review further details that cellulosomes can include **anchoring subunits** with **SLH (S-layer homology) domains** that adhere to the cell surface, strengthening proximity between the catalytic machinery and insoluble substrate. (datta2024enzymaticdegradationof pages 10-12)

**Recent 2024 genomic synthesis** indicates cellulosome systems are more phylogenetically and architecturally diverse than previously appreciated, with defined **cohesin (Coh1–Coh3)** and **dockerin (Doc1–Doc3)** domain types used as hallmarks. (minor2024agenomicanalysis pages 1-2)

### 2.3 Oxidative cellulolysis via LPMOs
**Lytic polysaccharide monooxygenases (LPMOs)** cleave polysaccharides (including cellulose) by **oxidation** rather than hydrolysis. In a 2024 study of fungal AA9 LPMOs:
- catalysis is framed as **Cu(II) → Cu(I) reduction** and reaction with **H2O2** to generate reactive species that oxidatively cleave crystalline cellulose, (raheja2024transcriptionalandsecretome pages 1-2)
- products include **C1/C4 oxidized oligosaccharides** (Type 3 LPMO behavior). (raheja2024transcriptionalandsecretome pages 1-2)

## 3) Recent developments and latest research (prioritizing 2023–2024)
### 3.1 Cellulosome diversity at scale (genome mining)
A 2024 comparative genomics analysis searched **305,693 bacterial genomes** for cellulosome hallmarks (dockerin-fused glycohydrolases and cohesin-containing scaffoldins) and found **33 bacterial species** with genomic capacity to produce cellulosomes, including **10 not previously reported**. (minor2024agenomicanalysis pages 1-2)

A key curation-relevant outcome is that “cellulosome” should be modeled as a **system** with alternative architectures (simple vs complex; differing cell-wall attachment strategies), not a single fixed complex. Figure evidence for these alternative architectures is available (minor2024agenomicanalysis media d1cb6ce8).

### 3.2 Regulation: carbon catabolite repression (CCR) and substrate-responsive control
A 2023 regulatory synthesis describes **carbon catabolite repression** as a central control layer for lignocellulose-catabolic genes, including in Gram-positive bacteria via **CcpA** binding **CRE sites** and repressing transcription when glucose-derived signals are high. (gurovic2023regulationoflignocellulose pages 5-7)

A 2024 mechanistic example in *Bacillus thuringiensis* shows:
- a cellobiose **PTS cel operon** mediates transport/utilization of cellobiose, (zhang2024transcriptionalregulationof pages 1-2)
- transcription is **induced by cellobiose** and **requires Sigma54**, and is **positively regulated by CelR**, (zhang2024transcriptionalregulationof pages 1-2)
- **glucose represses** cel operon transcription and **CcpA binds the promoter**, linking CCR directly to a cellodextrin utilization module. (zhang2024transcriptionalregulationof pages 1-2, zhang2024transcriptionalregulationof pages 6-8)

These results matter for cellulolysis trait assays because glucose repression can mask cellulolytic potential unless experimental design avoids strong CCR conditions. (gurovic2023regulationoflignocellulose pages 5-7)

### 3.3 Transport and downstream utilization modules (cellobiose/cellodextrins)
Transport and intracellular catabolism nodes are best curated as **supporting mechanisms** for the cellulolysis phenotype:
- In fungi, the major extracellular β‑glucosidase (GH3-3) and **cellodextrin transporters CDT‑1/CDT‑2** determine growth on cellobiose, and **Δcdt-2 is severely impaired for growth on cellulose** in *Neurospora crassa*. (zhang2024unveilingaclassical pages 1-2)
- In bacteria, cellobiose utilization may occur via **PTS** (celA/celB/celC) coupled to a **6‑phospho‑β‑glucosidase (celD)** step. (zhang2024transcriptionalregulationof pages 4-5)

### 3.4 Oxygen-linked cellulolysis niches in vivo
In termite gut ecosystems, metagenomic analysis reports **oxygen-dependent enzymes that oxidize cellulose or modify lignin**, highlighting “an unappreciated role of oxygen in the depolymerization of plant fiber and lignin in the microoxic periphery” during gut passage in higher termites. (salgado2024unveilinglignocellulolyticpotential pages 1-2)

## 4) Current applications and real-world implementations
### 4.1 Biomass saccharification for biorefineries (enzyme cocktails)
A 2024 applied study demonstrates industrially relevant outcomes from supplementing a cellulase preparation with recombinant AA9 LPMOs:
- saccharification of steam/acid pretreated unwashed rice straw slurry increased from **73.89%** (cellulase alone) to **87.94%** (with LPMO1) and **85.46%** (with LPMO2), and outperformed a commercial benchmark (**CellicCtec3: 68.26%**) at the same enzyme loading. (raheja2024transcriptionalandsecretome pages 12-13)
- the authors report increases in **total reducing sugar yield** of **19.01%** (LPMO1) and **15.66%** (LPMO2) and increases in **glucose release** of **28.57%** and **18.81%**, respectively. (raheja2024transcriptionalandsecretome pages 12-13)
- practical constraints are quantified: **~60% glucan hydrolysis** at **10 mg/g enzyme** and **15–17% solids**, with **>90% hydrolysis requiring ~30 mg/g** enzyme, described as commercially uneconomical. (raheja2024transcriptionalandsecretome pages 1-2)

These data support curating LPMO nodes/edges as “boosters” of saccharification in real process conditions rather than purely ecological curiosities. (raheja2024transcriptionalandsecretome pages 12-13)

### 4.2 Microbial platform engineering via cellulosome knowledge
The 2024 cellulosome genomics study motivates application by noting that understanding cellulosome structure/enzyme content can “facilitate the development of new microbial-based methods to produce renewable chemicals and materials.” (minor2024agenomicanalysis pages 1-2)

## 5) Expert opinions / synthesis perspectives (authoritative sources)
- **Cellulose-to-glucose conversion requires multiple enzyme classes acting together** (hydrolytic synergy concept). (gurovic2023regulationoflignocellulose pages 2-3)
- **Cellulosomes are modular, scaffoldin-centered machines** whose cohesin–dockerin specificity and attachment strategies shape function; they can be simple or complex architectures. (gurovic2023regulationoflignocellulose pages 3-4, minor2024agenomicanalysis pages 1-2, minor2024agenomicanalysis media d1cb6ce8)
- **CCR is a major regulatory constraint** that must be accounted for in both lab phenotype assays and industrial strain/enzyme deployment. (gurovic2023regulationoflignocellulose pages 5-7, zhang2024transcriptionalregulationof pages 1-2)

## 6) Candidate nodes for TraitMech causal graph (grounded where possible)
The following node inventory is designed to be transcribed into `data/traits/metabolism/cellulolysis.yaml`.

| Node label | Node type | Suggested grounding | Notes |
|---|---|---|---|
| cellulolysis | process | METPO:traitmech:000111; GO:0044246 | Trait node: microbial hydrolysis and/or oxidative depolymerization of cellulose to soluble oligosaccharides and glucose; broader than any one enzyme family or assay (gurovic2023regulationoflignocellulose pages 2-3, raheja2024transcriptionalandsecretome pages 1-2) |
| cellulose | substrate/metabolite | CHEBI:17057 | Primary polymeric substrate; β-1,4-D-glucose polymer degraded by cellulolytic systems (gurovic2023regulationoflignocellulose pages 2-3) |
| glucose | metabolite | CHEBI:17234 | Final soluble product of complete cellulose saccharification; also mediates catabolite repression in many systems (gurovic2023regulationoflignocellulose pages 2-3, gurovic2023regulationoflignocellulose pages 5-7) |
| cellobiose | metabolite | CHEBI:28053 | Major cellodextrin released from cellulose; inducer or transported intermediate depending on taxon (zhang2024transcriptionalregulationof pages 1-2, zhang2024unveilingaclassical pages 1-2) |
| cellodextrins | metabolite class | label only | Soluble cellulose-derived oligosaccharides specialized as substrates in several gut and clostridial systems (salgado2024unveilinglignocellulolyticpotential pages 1-2, you2024comprehensivetranscriptomicanalysis pages 7-10) |
| endoglucanase | enzyme | EC:3.2.1.4; GO:0008810 | Canonical hydrolytic cellulase class required for concerted cellulose depolymerization (gurovic2023regulationoflignocellulose pages 2-3, datta2024enzymaticdegradationof pages 10-12) |
| cellobiohydrolase / exoglucanase | enzyme | EC:3.2.1.91 or EC:3.2.1.176; GO:0008810 (broad cellulase activity if needed) | Processive cellulase class acting with endoglucanases and β-glucosidases in complete cellulose degradation (gurovic2023regulationoflignocellulose pages 2-3, datta2024enzymaticdegradationof pages 10-12) |
| β-glucosidase | enzyme | EC:3.2.1.21; GO:0008422 | Converts cellobiose to glucose; essential downstream hydrolytic step in many fungi/bacteria (gurovic2023regulationoflignocellulose pages 2-3, zhang2024unveilingaclassical pages 1-2) |
| GH3-3 β-glucosidase | enzyme/gene product | CAZy:GH3 | Major extracellular β-glucosidase in Neurospora crassa; taxon-specific but useful mechanistic node (zhang2024unveilingaclassical pages 1-2) |
| CelH | enzyme | label only | Example cellulosomal endoglucanase from Datta review; useful exemplar but likely too taxon-specific for core graph (datta2024enzymaticdegradationof pages 10-12) |
| CelK | enzyme | label only | Example cellobiohydrolase in cellulosome component lists; likely strain-specific exemplar (datta2024enzymaticdegradationof pages 10-12) |
| CelS | enzyme | label only | Example exoglucanase/cellobiohydrolase in cellulosome component lists; likely strain-specific exemplar (datta2024enzymaticdegradationof pages 10-12) |
| lytic polysaccharide monooxygenase (LPMO) | enzyme | EC:1.14.99.54; GO:0071722 | Oxidative cellulose-cleaving enzyme class using copper redox chemistry; complements hydrolytic cellulases (raheja2024transcriptionalandsecretome pages 1-2) |
| AA9 LPMO | enzyme family | CAZy:AA9 | Fungal LPMO family directly evidenced for C1/C4 oxidation and improved saccharification (raheja2024transcriptionalandsecretome pages 1-2) |
| AA3 auxiliary oxidoreductase | enzyme family | CAZy:AA3 | Redox partner class detected with LPMOs in secretomes; supports oxidative cellulolysis (raheja2024transcriptionalandsecretome pages 1-2) |
| AA7 auxiliary oxidoreductase | enzyme family | CAZy:AA7 | Auxiliary redox enzyme class co-secreted with LPMOs; candidate electron-transfer support node (raheja2024transcriptionalandsecretome pages 1-2) |
| catalase | enzyme | EC:1.11.1.6; GO:0004096 | Secretome component associated with LPMO/redox interplay and peroxide management (raheja2024transcriptionalandsecretome pages 1-2) |
| superoxide dismutase | enzyme | EC:1.15.1.1; GO:0004784 | Secretome component associated with oxidative enzyme systems in cellulolytic fungi (raheja2024transcriptionalandsecretome pages 1-2) |
| cellulosome | complex | GO:1990357 | Multienzyme extracellular complex for efficient cellulose degradation, especially in anaerobic bacteria (gurovic2023regulationoflignocellulose pages 3-4, minor2024agenomicanalysis pages 1-2) |
| scaffoldin | complex component | label only | Non-catalytic backbone of cellulosomes bearing cohesins and often CBMs (gurovic2023regulationoflignocellulose pages 3-4, minor2024agenomicanalysis pages 1-2) |
| CipA scaffoldin | complex component | label only | Named primary scaffoldin exemplar in clostridial cellulosomes; useful but taxon-specific (datta2024enzymaticdegradationof pages 10-12, datta2024enzymaticdegradationof pages 16-17) |
| cohesin domain | protein domain | label only | Scaffoldin domain that binds dockerins; key assembly module of cellulosomes (gurovic2023regulationoflignocellulose pages 3-4, minor2024agenomicanalysis pages 1-2) |
| dockerin domain | protein domain | label only | Enzyme-associated domain that docks catalytic subunits onto cohesins (gurovic2023regulationoflignocellulose pages 3-4, minor2024agenomicanalysis pages 1-2) |
| Coh1 / Coh2 / Coh3 | protein domain subtype | label only | Cohesin domain types recognized in comparative genomics of cellulosome bacteria; subtype nodes may be useful for detailed graphs (minor2024agenomicanalysis pages 1-2) |
| Doc1 / Doc2 / Doc3 | protein domain subtype | label only | Dockerin domain types recognized in comparative genomics; interact largely in species/type-specific manners (minor2024agenomicanalysis pages 1-2) |
| dockerin-fused glycohydrolase (DocGH) | enzyme/module | label only | Hallmark genomic signature for cellulosome-producing bacteria (minor2024agenomicanalysis pages 1-2) |
| carbohydrate-binding module (CBM) | protein domain | GO:0030246; CAZy:CBM | Substrate-targeting domain often found on scaffoldins or cellulases; enhances cellulose targeting (you2023insightsintolignocellulose pages 1-2, gurovic2023regulationoflignocellulose pages 3-4) |
| CBM3 | protein domain family | CAZy:CBM3 | Specific CBM family commonly associated with cellulose-binding in cellulosomal systems (datta2024enzymaticdegradationof pages 10-12) |
| SLH anchoring module | protein domain | label only | S-layer homology-based cell-surface anchoring component for some cellulosomes (datta2024enzymaticdegradationof pages 10-12, minor2024agenomicanalysis media d1cb6ce8) |
| cell surface attachment of cellulosome | cellular localization/process | GO:1905351 (approximate cell adhesion/anchoring unavailable); label only | Some cellulosomes are cell-attached, others released; attachment may affect substrate proximity (gurovic2023regulationoflignocellulose pages 3-4, minor2024agenomicanalysis media d1cb6ce8) |
| PTS cellobiose transporter (celABC) | transporter | KEGG Orthology not assigned here; label only | Bacillus cel operon encodes IIA/IIB/IIC components for cellobiose transport and utilization (zhang2024transcriptionalregulationof pages 1-2, zhang2024transcriptionalregulationof pages 4-5) |
| celA | transporter component | label only | Cellobiose-specific PTS enzyme IIB component in Bacillus thuringiensis cel operon (zhang2024transcriptionalregulationof pages 4-5) |
| celB | transporter component | label only | Cellobiose-specific PTS enzyme IIC membrane component (zhang2024transcriptionalregulationof pages 4-5) |
| celC | transporter component | label only | Cellobiose-specific PTS enzyme IIA component (zhang2024transcriptionalregulationof pages 4-5) |
| celD | enzyme | EC:3.2.1.86 | 6-phospho-β-glucosidase in Bacillus cel operon; hydrolyzes phosphorylated cellobiose derivative after PTS import (zhang2024transcriptionalregulationof pages 4-5) |
| celE | operon component | label only | Conserved cel operon gene of unknown/unclear role; avoid strong curation without primary functional evidence (zhang2024transcriptionalregulationof pages 4-5) |
| ABC transporter for cellodextrins/cellobiose | transporter | GO:0042887 (broad carbohydrate transport); label only | Major uptake route in Ruminiclostridium-type cellulolytic clostridia and Streptomyces-type systems (you2023insightsintolignocellulose pages 1-2, gurovic2023regulationoflignocellulose pages 7-7, you2024comprehensivetranscriptomicanalysis pages 7-10) |
| CebE | substrate-binding protein | label only | Cellobiose/cellotriose-binding lipoprotein in Streptomyces ABC uptake system; useful comparative node but not universal (gurovic2023regulationoflignocellulose pages 7-7) |
| CDT-1 | transporter | label only | Fungal cellodextrin transporter essential for growth on cellobiose when major β-glucosidases are absent (zhang2024unveilingaclassical pages 1-2) |
| CDT-2 | transporter | label only | Fungal cellodextrin transporter; Δcdt-2 severely impairs growth on cellulose in N. crassa (zhang2024unveilingaclassical pages 1-2) |
| cellobiose/cellodextrin phosphorylase | enzyme | EC:2.4.1.20 or EC:2.4.1.49 (context-dependent) | Intracellular catabolic step in Ruminiclostridium papyrosolvens after oligosaccharide import (you2024comprehensivetranscriptomicanalysis pages 7-10) |
| 6-phosphate-glucosidase | enzyme | EC:3.2.1.86 | Intracellular enzyme acting in phosphorylated cellobiose/cellodextrin route in clostridial and Bacillus systems (zhang2024transcriptionalregulationof pages 4-5, you2024comprehensivetranscriptomicanalysis pages 7-10) |
| CelR | regulator | label only | PRD-domain-containing Sigma54-dependent activator positively regulating the Bacillus cel operon in response to cellobiose (zhang2024transcriptionalregulationof pages 1-2, zhang2024transcriptionalregulationof pages 4-5) |
| Sigma54 / SigL | regulator | GO:0006355 (broad transcriptional regulation); label only | Alternative sigma factor required for transcription of the Bacillus cel operon (zhang2024transcriptionalregulationof pages 1-2, zhang2024transcriptionalregulationof pages 4-5) |
| CcpA | regulator | label only | Catabolite control protein A mediating glucose repression of cellobiose utilization genes (zhang2024transcriptionalregulationof pages 1-2, zhang2024transcriptionalregulationof pages 6-8, gurovic2023regulationoflignocellulose pages 5-7) |
| carbon catabolite repression (CCR) | regulatory process | GO:0046050 | Broad regulatory process repressing cellulolytic/cellobiose-utilization genes in presence of preferred carbon sources such as glucose (gurovic2023regulationoflignocellulose pages 2-3, gurovic2023regulationoflignocellulose pages 5-7) |
| glucose repression | regulatory process/environmental factor | label only | Operational node for experiments showing repression of cel operon and cellulolytic programs by glucose (zhang2024transcriptionalregulationof pages 6-8, gurovic2023regulationoflignocellulose pages 5-7) |
| two-component system (TCS) | regulator/system | GO:0000160 | Controls CAZyme and ABC transporter expression in Ruminiclostridium-type cellulolytic bacteria (you2023insightsintolignocellulose pages 1-2, you2024comprehensivetranscriptomicanalysis pages 7-10) |
| anti-sigma factor with extracellular CBM | regulator/sensor | label only | Proposed substrate-sensing regulator for cellulosomal gene induction in C. thermocellum-like bacteria (gurovic2023regulationoflignocellulose pages 7-7) |
| oxygen-dependent cellulose-oxidizing enzymes | enzyme class | label only | Metagenomic/ecological evidence in termite gut for oxygen-dependent enzymes that oxidize cellulose or modify lignin; mechanism needs finer grounding (salgado2024unveilinglignocellulolyticpotential pages 1-2) |
| oxygen | environmental factor | CHEBI:15379 | Relevant especially for oxidative depolymerization in microoxic niches; not required for all cellulolysis (salgado2024unveilinglignocellulolyticpotential pages 1-2) |
| microoxic periphery | environmental factor | ENVO:01000314 (microaerobic environment, approximate) | Termite hindgut peripheral niche associated with oxygen-linked fiber depolymerization (salgado2024unveilinglignocellulolyticpotential pages 1-2) |
| hydrogen peroxide | metabolite/co-substrate | CHEBI:16240 | Co-substrate supporting LPMO catalysis via Cu redox chemistry (raheja2024transcriptionalandsecretome pages 1-2) |
| Cu(II)/Cu(I) redox center | cofactor | CHEBI:29036 / CHEBI:29033 | Central catalytic metal state transition in LPMO mechanism; candidate mechanistic node if graph supports cofactors (raheja2024transcriptionalandsecretome pages 1-2) |
| ascorbate | reductant | CHEBI:22652 | Example small-molecule reductant that can drive LPMO activity (raheja2024transcriptionalandsecretome pages 1-2) |
| gallic acid | reductant | CHEBI:30778 | Example phenolic reductant supporting LPMO catalysis (raheja2024transcriptionalandsecretome pages 1-2) |
| methyl hydroquinone | reductant | label only | Example added reductant for LPMO activity; grounding uncertain (raheja2024transcriptionalandsecretome pages 1-2) |
| cello-oligosaccharides | metabolite class/regulatory factor | label only | Reported to negatively affect/downregulate LPMO expression in R. emersonii; may be taxon-specific (raheja2024transcriptionalandsecretome pages 1-2) |
| extracellular cellulase system (free enzymes) | process/complex system | label only | Non-cellulosomal strategy in aerobic fungi/bacteria using freely secreted enzymes (datta2024enzymaticdegradationof pages 10-12) |
| cell-attached cellulosome | complex subtype | label only | Architectural subtype attached to bacterial surface (gurovic2023regulationoflignocellulose pages 3-4, minor2024agenomicanalysis media d1cb6ce8) |
| cell-free cellulosome | complex subtype | label only | Architectural subtype released into environment; not always retained at surface (minor2024agenomicanalysis pages 1-2) |


*Table: This table lists candidate causal-graph nodes for the microbial trait cellulolysis, grouped across enzymes, complexes, transporters, regulators, metabolites, and environmental factors. It is designed for TraitMech curation and includes suggested ontology grounding plus notes on scope or taxon specificity.*

## 7) Candidate evidence-backed causal edges (triples)
Edges below are proposed for curation as subject–predicate–object statements with evidence excerpts and DOI-first references.

| Subject node | Predicate | Object node | Evidence snippet (short quote) | Reference (DOI, year, URL) | Notes/uncertainty |
|---|---|---|---|---|---|
| cellulose | is degraded by concerted action of | endoglucanase | “complete degradation to glucose requires a concerted action of cellobiohydrolases, endoglucanases and β-glucosidases” (gurovic2023regulationoflignocellulose pages 2-3) | 10.1093/jambio/lxac002, 2023, https://doi.org/10.1093/jambio/lxac002 | Strong review-level statement; broad, not taxon-specific. |
| cellulose | is degraded by concerted action of | cellobiohydrolase / exoglucanase | “complete degradation to glucose requires a concerted action of cellobiohydrolases, endoglucanases and β-glucosidases” (gurovic2023regulationoflignocellulose pages 2-3) | 10.1093/jambio/lxac002, 2023, https://doi.org/10.1093/jambio/lxac002 | Strong review-level statement; exoglucanase/cellobiohydrolase grouped here. |
| cellobiose | is hydrolyzed by | β-glucosidase | “β-glucosidase activity converting cellobiose into glucose” (zhang2024unveilingaclassical pages 1-2) | 10.1186/s13568-023-01658-0, 2024, https://doi.org/10.1186/s13568-023-01658-0 | Strong for fungal system; supports downstream saccharification step. |
| β-glucosidase | produces | glucose | “β-glucosidase activity converting cellobiose into glucose” (zhang2024unveilingaclassical pages 1-2) | 10.1186/s13568-023-01658-0, 2024, https://doi.org/10.1186/s13568-023-01658-0 | Product edge is directly stated. |
| cellulosome | has backbone component | scaffoldin | “they are multienzyme complexes built on scaffoldins” (gurovic2023regulationoflignocellulose pages 3-4) | 10.1093/jambio/lxac002, 2023, https://doi.org/10.1093/jambio/lxac002 | Strong architectural edge. |
| scaffoldin | contains | cohesin domain | “Scaffoldins are the non-catalytic backbone and ‘bear modules called cohesin’” (you2023insightsintolignocellulose pages 1-2) | 10.3389/fmicb.2023.1288286, 2023, https://doi.org/10.3389/fmicb.2023.1288286 | Strong mechanistic edge. |
| dockerin domain | binds to | cohesin domain | “dockerin modules interacting with scaffoldin cohesin modules” (gurovic2023regulationoflignocellulose pages 3-4) | 10.1093/jambio/lxac002, 2023, https://doi.org/10.1093/jambio/lxac002 | Canonical assembly interaction. |
| carbohydrate-binding module (CBM) | targets | cellulose substrate | “Scaffoldins can include a carbohydrate-binding module (CBM) that targets the complex to the substrate” (you2023insightsintolignocellulose pages 1-2) | 10.3389/fmicb.2023.1288286, 2023, https://doi.org/10.3389/fmicb.2023.1288286 | Strong, but substrate generalized as cellulose-rich lignocellulose. |
| cellulosome | can be attached to | bacterial cell surface | “Cellulosomes… can be cell-attached or released” (gurovic2023regulationoflignocellulose pages 3-4) | 10.1093/jambio/lxac002, 2023, https://doi.org/10.1093/jambio/lxac002 | Architectural subtype edge; not universal. |
| SLH anchoring module | mediates attachment of | cellulosome to cell surface | “can include anchoring subunits that adhere to the cell surface (SLH domains)” (datta2024enzymaticdegradationof pages 10-12) | 10.1016/j.heliyon.2024.e24022, 2024, https://doi.org/10.1016/j.heliyon.2024.e24022 | Strong for SLH-anchored systems; taxon-dependent. |
| cellulosome architecture | promotes synergistic action of | endoglucanases and cellobiohydrolases/exoglucanases | “The cellulosome architecture promotes synergistic action of endoglucanases, cellobiohydrolases/exoglucanases” (datta2024enzymaticdegradationof pages 10-12) | 10.1016/j.heliyon.2024.e24022, 2024, https://doi.org/10.1016/j.heliyon.2024.e24022 | Supports synergy edge; useful but from review synthesis. |
| LPMO | requires | Cu(II)/Cu(I) redox center | “reduction of Cu(II) to Cu(I)… generates reactive species that oxidatively cleave crystalline cellulose” (raheja2024transcriptionalandsecretome pages 1-2) | 10.1007/s00253-024-13240-0, 2024, https://doi.org/10.1007/s00253-024-13240-0 | Strong mechanistic edge for oxidative cellulolysis. |
| LPMO | uses co-substrate | hydrogen peroxide | “in presence of H2O2 generates reactive species that oxidatively cleave crystalline cellulose” (raheja2024transcriptionalandsecretome pages 1-2) | 10.1007/s00253-024-13240-0, 2024, https://doi.org/10.1007/s00253-024-13240-0 | Strong for this study’s mechanistic framing. |
| ascorbate / gallic acid / methyl hydroquinone | act as reductant for | LPMO | “added small-molecule reductants (ascorbate, gallic acid, methyl hydroquinone)” (raheja2024transcriptionalandsecretome pages 1-2) | 10.1007/s00253-024-13240-0, 2024, https://doi.org/10.1007/s00253-024-13240-0 | Strong but combine several reductants in one generalized edge. |
| AA9 LPMO | produces | C1/C4 oxidized oligosaccharides | “presence of C1/C4 oxidized oligosaccharides indicating them to be Type 3 LPMOs” (raheja2024transcriptionalandsecretome pages 1-2) | 10.1007/s00253-024-13240-0, 2024, https://doi.org/10.1007/s00253-024-13240-0 | Strong product edge for fungal AA9 LPMOs. |
| cellobiose | induces transcription of | cel operon | “cel operon transcription is induced by cellobiose” (zhang2024transcriptionalregulationof pages 1-2) | 10.3389/fmicb.2024.1160472, 2024, https://doi.org/10.3389/fmicb.2024.1160472 | Strong but specific to Bacillus thuringiensis. |
| CelR | positively regulates | cel operon transcription | “positively regulated by the PRD-domain-containing activator CelR” (zhang2024transcriptionalregulationof pages 1-2) | 10.3389/fmicb.2024.1160472, 2024, https://doi.org/10.3389/fmicb.2024.1160472 | Strong, taxon-specific regulatory edge. |
| Sigma54 (SigL) | is required for transcription of | cel operon | “cel operon transcription is induced by cellobiose, controlled by Sigma54” (zhang2024transcriptionalregulationof pages 1-2) | 10.3389/fmicb.2024.1160472, 2024, https://doi.org/10.3389/fmicb.2024.1160472 | Strong, taxon-specific. |
| celABC PTS transporter | transports | cellobiose | “a PEP:carbohydrate phosphotransferase system (PTS), encoded by a five-gene cel operon, mediates transport and utilization of cellobiose” (zhang2024transcriptionalregulationof pages 1-2) | 10.3389/fmicb.2024.1160472, 2024, https://doi.org/10.3389/fmicb.2024.1160472 | Strong for PTS-based uptake route. |
| PTS-mediated cellobiose uptake | produces intracellular | cellobiose-6-phosphate | “a PTS route… produces cellobiose-6-phosphate” (you2024comprehensivetranscriptomicanalysis pages 7-10) | 10.21203/rs.3.rs-5487263/v1, 2024, https://doi.org/10.21203/rs.3.rs-5487263/v1 | Preprint; mark as uncertain for direct curation. |
| celD / 6-phospho-β-glucosidase | hydrolyzes | phosphorylated cellobiose intermediate | “celD encoding a 6-phospho-beta-glucosidase” (zhang2024transcriptionalregulationof pages 4-5) | 10.3389/fmicb.2024.1160472, 2024, https://doi.org/10.3389/fmicb.2024.1160472 | Function inferred from enzyme name in operon context; good but not direct biochemical assay here. |
| ABC transporters | absorb | extracellular sugars | “Ruminiclostridium-type species mainly use ABC transporters regulated by two-component systems (TCSs) to absorb extracellular sugars” (you2023insightsintolignocellulose pages 1-2) | 10.3389/fmicb.2023.1288286, 2023, https://doi.org/10.3389/fmicb.2023.1288286 | Strong comparative-genomics edge. |
| two-component system (TCS) | regulates | ABC transporters and CAZyme genes | “CAZyme gene expression was regulated by TCSs, affecting sugar transporter systems” (you2024comprehensivetranscriptomicanalysis pages 7-10) | 10.21203/rs.3.rs-5487263/v1, 2024, https://doi.org/10.21203/rs.3.rs-5487263/v1 | Preprint; useful but uncertain for hard curation. |
| CDT-1 and CDT-2 | are required for growth on | cellobiose | “CDT-1 and CDT-2 are essential for growth on cellobiose when the three main N. crassa β-glucosidases are absent” (zhang2024unveilingaclassical pages 1-2) | 10.1186/s13568-023-01658-0, 2024, https://doi.org/10.1186/s13568-023-01658-0 | Strong fungal transport/utilization edge; conditional on β-glucosidase background. |
| glucose | represses transcription of | cel operon | “Glucose represses cel operon transcription” (zhang2024transcriptionalregulationof pages 1-2) | 10.3389/fmicb.2024.1160472, 2024, https://doi.org/10.3389/fmicb.2024.1160472 | Strong, taxon-specific example of CCR. |
| CcpA | mediates glucose repression of | cel operon | “CcpA binds the cel promoter to positively regulate this glucose-repressed process” (zhang2024transcriptionalregulationof pages 1-2) | 10.3389/fmicb.2024.1160472, 2024, https://doi.org/10.3389/fmicb.2024.1160472 | Strong but wording reflects regulation of repression process. |
| carbon catabolite repression (CCR) | represses | lignocellulose-catabolic / cellulolytic genes | “CcpA recognizing CRE sites to prevent transcription of lignocellulose-catabolic genes when glucose-derived signals are high” (gurovic2023regulationoflignocellulose pages 5-7) | 10.1093/jambio/lxac002, 2023, https://doi.org/10.1093/jambio/lxac002 | Broad regulatory edge; high-value for trait boundary. |
| microoxic periphery | supports activity of | oxygen-dependent cellulose-oxidizing enzymes | “a so far unappreciated role of oxygen in the depolymerization of plant fiber and lignin in the microoxic periphery” (salgado2024unveilinglignocellulolyticpotential pages 1-2) | 10.1186/s40168-024-01917-7, 2024, https://doi.org/10.1186/s40168-024-01917-7 | Strong ecological edge, but termite-gut-specific. |
| oxygen-dependent enzymes | oxidize | cellulose / modify lignin | “oxygen-dependent enzymes that oxidize cellulose or modify lignin” (salgado2024unveilinglignocellulolyticpotential pages 1-2) | 10.1186/s40168-024-01917-7, 2024, https://doi.org/10.1186/s40168-024-01917-7 | Strong ecological-genomic claim; exact enzyme identities unresolved in excerpt. |


*Table: This table lists evidence-backed candidate subject-predicate-object edges for curating a TraitMech causal graph of microbial cellulolysis. It covers hydrolytic and oxidative cellulose breakdown, cellulosome assembly, transport/utilization modules, and regulatory/environmental controls, with citations restricted to the provided context IDs.*

## 8) Visual evidence supporting a core mechanism (cellulosome architecture)
A labeled schematic comparing “simple” and “complex” cellulosomes—showing scaffoldins, dockerin-fused enzymes, cohesin–dockerin interactions, and cell-wall attachment modules—was retrieved from Minor et al. 2024 (Figure 1). (minor2024agenomicanalysis media d1cb6ce8)

## 9) Warnings / curation notes (do not curate as high-confidence without more primary evidence)
1. **Preprint-only edges**: The Ruminiclostridium transcriptomics/transport edges sourced from a preprint should be marked *uncertain* or deferred until peer-reviewed confirmation. (you2024comprehensivetranscriptomicanalysis pages 7-10)
2. **Function inferred from gene name/operon context**: celD is labeled as a 6‑phospho‑β‑glucosidase within a PTS operon; unless a direct biochemical assay is cited in the same paper section, curate as *putative* in organism-specific graphs. (zhang2024transcriptionalregulationof pages 4-5)
3. **Oxygen-dependent cellulose oxidation**: termite-gut MAG evidence highlights oxygen-linked oxidative enzymes but does not resolve specific enzyme identities in the excerpt; curate as a high-level environmental/enzymatic association or await enzyme-level annotation (e.g., AA families, EC). (salgado2024unveilinglignocellulolyticpotential pages 1-2)
4. **Over-specific exemplar enzyme names (CelH/CelK/CelS, CipA)**: useful for illustrating architecture but may be too strain-specific for a core trait graph unless TraitMech supports taxon-scoped subgraphs. (datta2024enzymaticdegradationof pages 10-12)

## 10) DOI-first bibliography (with dates and URLs)
- **Minor CM, et al.** “A genomic analysis reveals the diversity of cellulosome displaying bacteria.” *Frontiers in Microbiology* (Oct **2024**). DOI: **10.3389/fmicb.2024.1473396**. https://doi.org/10.3389/fmicb.2024.1473396 (minor2024agenomicanalysis pages 1-2, minor2024agenomicanalysis media d1cb6ce8)
- **Salgado JFM, et al.** “Unveiling lignocellulolytic potential: a genomic exploration of bacterial lineages within the termite gut.” *Microbiome* (Oct **2024**). DOI: **10.1186/s40168-024-01917-7**. https://doi.org/10.1186/s40168-024-01917-7 (salgado2024unveilinglignocellulolyticpotential pages 1-2)
- **Raheja Y, et al.** “Transcriptional and secretome analysis of *Rasamsonia emersonii* lytic polysaccharide mono-oxygenases.” *Applied Microbiology and Biotechnology* (Aug **2024**). DOI: **10.1007/s00253-024-13240-0**. https://doi.org/10.1007/s00253-024-13240-0 (raheja2024transcriptionalandsecretome pages 1-2, raheja2024transcriptionalandsecretome pages 12-13)
- **Zhang L, et al.** “Transcriptional regulation of cellobiose utilization by … CelR and CcpA in *Bacillus thuringiensis*.” *Frontiers in Microbiology* (Jan **2024**). DOI: **10.3389/fmicb.2024.1160472**. https://doi.org/10.3389/fmicb.2024.1160472 (zhang2024transcriptionalregulationof pages 1-2, zhang2024transcriptionalregulationof pages 4-5, zhang2024transcriptionalregulationof pages 6-8)
- **Datta R.** “Enzymatic degradation of cellulose in soil: A review.” *Heliyon* (Jan **2024**). DOI: **10.1016/j.heliyon.2024.e24022**. https://doi.org/10.1016/j.heliyon.2024.e24022 (datta2024enzymaticdegradationof pages 10-12)
- **Zhang Y, et al.** “Unveiling a classical mutant in the context of the GH3 β‑glucosidase family in *Neurospora crassa*.” *AMB Express* (Jan **2024**). DOI: **10.1186/s13568-023-01658-0**. https://doi.org/10.1186/s13568-023-01658-0 (zhang2024unveilingaclassical pages 1-2)
- **Gurovic MSV, et al.** “Regulation of lignocellulose degradation in microorganisms.” *Journal of Applied Microbiology* (Dec **2023**). DOI: **10.1093/jambio/lxac002**. https://doi.org/10.1093/jambio/lxac002 (gurovic2023regulationoflignocellulose pages 3-4, gurovic2023regulationoflignocellulose pages 2-3, gurovic2023regulationoflignocellulose pages 5-7, gurovic2023regulationoflignocellulose pages 7-7)

(Non-DOI note: no additional URLs beyond DOIs were present in the extracted evidence.)


References

1. (gurovic2023regulationoflignocellulose pages 2-3): María Soledad Vela Gurovic, Fatima Regina Viceconte, Maximiliano Andres Bidegain, and Julián Dietrich. Regulation of lignocellulose degradation in microorganisms. Journal of applied microbiology, Dec 2023. URL: https://doi.org/10.1093/jambio/lxac002, doi:10.1093/jambio/lxac002. This article has 34 citations and is from a peer-reviewed journal.

2. (zhang2024transcriptionalregulationof pages 1-2): Liangwei Zhang, Hong Xu, Haijian Cheng, Fuping Song, Jie Zhang, and Qi Peng. Transcriptional regulation of cellobiose utilization by prd-domain containing sigma54-dependent transcriptional activator (celr) and catabolite control protein a (ccpa) in bacillus thuringiensis. Frontiers in Microbiology, Jan 2024. URL: https://doi.org/10.3389/fmicb.2024.1160472, doi:10.3389/fmicb.2024.1160472. This article has 4 citations and is from a peer-reviewed journal.

3. (zhang2024transcriptionalregulationof pages 4-5): Liangwei Zhang, Hong Xu, Haijian Cheng, Fuping Song, Jie Zhang, and Qi Peng. Transcriptional regulation of cellobiose utilization by prd-domain containing sigma54-dependent transcriptional activator (celr) and catabolite control protein a (ccpa) in bacillus thuringiensis. Frontiers in Microbiology, Jan 2024. URL: https://doi.org/10.3389/fmicb.2024.1160472, doi:10.3389/fmicb.2024.1160472. This article has 4 citations and is from a peer-reviewed journal.

4. (zhang2024unveilingaclassical pages 1-2): Yuxin Zhang, Basant Nada, Scott E. Baker, James E. Evans, Chaoguang Tian, J. Philipp Benz, and Elisabeth Tamayo. Unveiling a classical mutant in the context of the gh3 β-glucosidase family in neurospora crassa. AMB Express, Jan 2024. URL: https://doi.org/10.1186/s13568-023-01658-0, doi:10.1186/s13568-023-01658-0. This article has 3 citations and is from a peer-reviewed journal.

5. (gurovic2023regulationoflignocellulose pages 3-4): María Soledad Vela Gurovic, Fatima Regina Viceconte, Maximiliano Andres Bidegain, and Julián Dietrich. Regulation of lignocellulose degradation in microorganisms. Journal of applied microbiology, Dec 2023. URL: https://doi.org/10.1093/jambio/lxac002, doi:10.1093/jambio/lxac002. This article has 34 citations and is from a peer-reviewed journal.

6. (salgado2024unveilinglignocellulolyticpotential pages 1-2): João Felipe M. Salgado, Vincent Hervé, Manuel A. G. Vera, Gaku Tokuda, and Andreas Brune. Unveiling lignocellulolytic potential: a genomic exploration of bacterial lineages within the termite gut. Microbiome, Oct 2024. URL: https://doi.org/10.1186/s40168-024-01917-7, doi:10.1186/s40168-024-01917-7. This article has 44 citations and is from a highest quality peer-reviewed journal.

7. (you2023insightsintolignocellulose pages 1-2): Mengcheng You, Qiuyun Zhao, Yuansheng Liu, Wenhao Zhang, Zhewei Shen, Zhenxing Ren, and Chenggang Xu. Insights into lignocellulose degradation: comparative genomics of anaerobic and cellulolytic ruminiclostridium-type species. Frontiers in Microbiology, Nov 2023. URL: https://doi.org/10.3389/fmicb.2023.1288286, doi:10.3389/fmicb.2023.1288286. This article has 22 citations and is from a peer-reviewed journal.

8. (datta2024enzymaticdegradationof pages 10-12): Rahul Datta. Enzymatic degradation of cellulose in soil: a review. Heliyon, 10:e24022, Jan 2024. URL: https://doi.org/10.1016/j.heliyon.2024.e24022, doi:10.1016/j.heliyon.2024.e24022. This article has 169 citations.

9. (minor2024agenomicanalysis pages 1-2): Christine M. Minor, Allen Takayesu, Sung Min Ha, Lukasz Salwinski, Michael R. Sawaya, Matteo Pellegrini, and Robert T. Clubb. A genomic analysis reveals the diversity of cellulosome displaying bacteria. Frontiers in Microbiology, Oct 2024. URL: https://doi.org/10.3389/fmicb.2024.1473396, doi:10.3389/fmicb.2024.1473396. This article has 17 citations and is from a peer-reviewed journal.

10. (raheja2024transcriptionalandsecretome pages 1-2): Yashika Raheja, Varinder Singh, Nitish Kumar, Dhruv Agrawal, Gaurav Sharma, Marcos Di Falco, Adrian Tsang, and Bhupinder Singh Chadha. Transcriptional and secretome analysis of rasamsonia emersonii lytic polysaccharide mono-oxygenases. Applied Microbiology and Biotechnology, Aug 2024. URL: https://doi.org/10.1007/s00253-024-13240-0, doi:10.1007/s00253-024-13240-0. This article has 11 citations and is from a domain leading peer-reviewed journal.

11. (minor2024agenomicanalysis media d1cb6ce8): Christine M. Minor, Allen Takayesu, Sung Min Ha, Lukasz Salwinski, Michael R. Sawaya, Matteo Pellegrini, and Robert T. Clubb. A genomic analysis reveals the diversity of cellulosome displaying bacteria. Frontiers in Microbiology, Oct 2024. URL: https://doi.org/10.3389/fmicb.2024.1473396, doi:10.3389/fmicb.2024.1473396. This article has 17 citations and is from a peer-reviewed journal.

12. (gurovic2023regulationoflignocellulose pages 5-7): María Soledad Vela Gurovic, Fatima Regina Viceconte, Maximiliano Andres Bidegain, and Julián Dietrich. Regulation of lignocellulose degradation in microorganisms. Journal of applied microbiology, Dec 2023. URL: https://doi.org/10.1093/jambio/lxac002, doi:10.1093/jambio/lxac002. This article has 34 citations and is from a peer-reviewed journal.

13. (zhang2024transcriptionalregulationof pages 6-8): Liangwei Zhang, Hong Xu, Haijian Cheng, Fuping Song, Jie Zhang, and Qi Peng. Transcriptional regulation of cellobiose utilization by prd-domain containing sigma54-dependent transcriptional activator (celr) and catabolite control protein a (ccpa) in bacillus thuringiensis. Frontiers in Microbiology, Jan 2024. URL: https://doi.org/10.3389/fmicb.2024.1160472, doi:10.3389/fmicb.2024.1160472. This article has 4 citations and is from a peer-reviewed journal.

14. (raheja2024transcriptionalandsecretome pages 12-13): Yashika Raheja, Varinder Singh, Nitish Kumar, Dhruv Agrawal, Gaurav Sharma, Marcos Di Falco, Adrian Tsang, and Bhupinder Singh Chadha. Transcriptional and secretome analysis of rasamsonia emersonii lytic polysaccharide mono-oxygenases. Applied Microbiology and Biotechnology, Aug 2024. URL: https://doi.org/10.1007/s00253-024-13240-0, doi:10.1007/s00253-024-13240-0. This article has 11 citations and is from a domain leading peer-reviewed journal.

15. (you2024comprehensivetranscriptomicanalysis pages 7-10): Mengcheng You, Zhenxing Ren, Letian Ye, Qiuyun Zhao, Ziyi Liu, Houhui Song, and Chenggang Xu. Comprehensive transcriptomic analysis of carbohydrate utilization in ruminiclostridium papyrosolvens dsm2782. Unknown journal, Dec 2024. URL: https://doi.org/10.21203/rs.3.rs-5487263/v1, doi:10.21203/rs.3.rs-5487263/v1.

16. (datta2024enzymaticdegradationof pages 16-17): Rahul Datta. Enzymatic degradation of cellulose in soil: a review. Heliyon, 10:e24022, Jan 2024. URL: https://doi.org/10.1016/j.heliyon.2024.e24022, doi:10.1016/j.heliyon.2024.e24022. This article has 169 citations.

17. (gurovic2023regulationoflignocellulose pages 7-7): María Soledad Vela Gurovic, Fatima Regina Viceconte, Maximiliano Andres Bidegain, and Julián Dietrich. Regulation of lignocellulose degradation in microorganisms. Journal of applied microbiology, Dec 2023. URL: https://doi.org/10.1093/jambio/lxac002, doi:10.1093/jambio/lxac002. This article has 34 citations and is from a peer-reviewed journal.