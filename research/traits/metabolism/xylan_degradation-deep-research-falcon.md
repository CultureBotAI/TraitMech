---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T06:09:37.884044'
end_time: '2026-06-18T06:30:20.096364'
duration_seconds: 1242.21
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: xylan degradation
  trait_identifier: traitmech:000113
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: xylan_degradation
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A biopolymer-degradation metabolism in which an organism hydrolyzes
    xylan, the most abundant hemicellulose, into xylose and xylo-oligosaccharides
    using xylanases and accessory enzymes.
  parent_traits: traitmech:000110
  synonyms: xylanolytic, hemicellulose degradation
  evidence_summary: 'DOI:10.1111/j.1757-1707.2009.01004.x:  (Dodd & Cann review the
    enzymatic deconstruction of xylan, the major hemicellulosic polysaccharide.) |
    DOI:10.1016/j.cbpa.2015.10.018:  (Cragg et al. include hemicellulose (xylan) degradation
    within lignocellulose breakdown across organisms.)'
  causal_graph_summary: 'xylan_degradation_xylanase: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 33
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** xylan degradation
- **METPO identifier:** traitmech:000113
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biopolymer-degradation metabolism in which an organism hydrolyzes xylan, the most abundant hemicellulose, into xylose and xylo-oligosaccharides using xylanases and accessory enzymes.
- **Parent traits:** traitmech:000110
- **Synonyms:** xylanolytic, hemicellulose degradation
- **Existing evidence:** DOI:10.1111/j.1757-1707.2009.01004.x:  (Dodd & Cann review the enzymatic deconstruction of xylan, the major hemicellulosic polysaccharide.) | DOI:10.1016/j.cbpa.2015.10.018:  (Cragg et al. include hemicellulose (xylan) degradation within lignocellulose breakdown across organisms.)
- **Existing causal graph summary:** xylan_degradation_xylanase: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **xylan degradation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/xylan_degradation.yaml`.

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
- **Trait label:** xylan degradation
- **METPO identifier:** traitmech:000113
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biopolymer-degradation metabolism in which an organism hydrolyzes xylan, the most abundant hemicellulose, into xylose and xylo-oligosaccharides using xylanases and accessory enzymes.
- **Parent traits:** traitmech:000110
- **Synonyms:** xylanolytic, hemicellulose degradation
- **Existing evidence:** DOI:10.1111/j.1757-1707.2009.01004.x:  (Dodd & Cann review the enzymatic deconstruction of xylan, the major hemicellulosic polysaccharide.) | DOI:10.1016/j.cbpa.2015.10.018:  (Cragg et al. include hemicellulose (xylan) degradation within lignocellulose breakdown across organisms.)
- **Existing causal graph summary:** xylan_degradation_xylanase: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **xylan degradation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/xylan_degradation.yaml`.

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


# Microbial Trait Causal Graph Curation Report: Xylan Degradation (traitmech:000113)

## 0. Scope summary (curation-ready)

**Trait meaning.** Xylan degradation is a biopolymer-degradation metabolism comprising enzymatic deconstruction of substituted **β-1,4-linked xylopyranosyl** backbones (xylans) into **xylo-oligosaccharides and xylose**, typically requiring both backbone-cleaving enzymes (endo-xylanases) and **accessory/debranching** enzymes (e.g., arabinofuranosidases, glucuronidases, esterases). Xylan side groups include **arabinose, acetyl, glucuronic acids, ferulic acid, and p-coumaric acid**, and therefore “different types of enzymes are required” for hydrolysis (rakitin2024verrucomicrobiaofthe pages 2-3).

**Key boundary conditions.** 
* **Polymer vs oligomer utilization.** A common boundary is organisms that consume **xylo-oligosaccharides (XOS/AXOS)** but cannot depolymerize **intact xylan polymers**. Because polymers are too large for direct uptake, measurable polymer degradation requires **extracellular or cell-surface/periplasm-proximal depolymerization**, after which smaller oligosaccharides can be transported and catabolized (gonzalez‐alonso2026cerealarabinoxylans—theirenzymatic pages 9-10).
* **Decorated vs simple xylans.** For gut Bacteroidota, distinct **polysaccharide utilization loci (PULs)** can be specialized for simple linear XOS vs complex decorated glucuronoarabinoxylan, implying a boundary based on CAZyme complement and sensing/transport machinery (hinkley2025investigatingthemechanism pages 101-106).
* **Extracellular-only vs intracellular completion.** Some systems import decorated oligosaccharides and complete debranching/deacylation intracellularly (e.g., the *Ruminiclostridium cellulolyticum* Xua system) (liu2024intracellularremovalof pages 1-2).

**Assay modalities (evidence types).** Growth on xylan as sole carbon source, xylan-agar clearing, transcriptomic/qRT-PCR induction of CAZyme/transport genes, targeted gene disruption with growth phenotypes, enzyme activity assays on xylan/AXOS substrates, and environmental enrichment with xylan under defined conditions (mukherjee2023comprehensivegenomeanalysis pages 1-2, liu2024intracellularremovalof pages 1-2, rakitin2024verrucomicrobiaofthe pages 5-7).

## 1. Recent developments and current understanding (prioritizing 2023–2024)

### 1.1 Intracellular completion of decorated AXOS utilization (Gram-positive anaerobe model)
A clear, curatable mechanistic module is the **Xua (xylan utilization associated) system** in *Ruminiclostridium cellulolyticum*, which couples (i) **ABC import of arabinoxylodextrins** and (ii) intracellular GH/esterase steps removing arabinosyl and acyl decorations. The gene cluster is explicitly described as **xuaABCDD’EFGHIJ** and is regulated by a dedicated two-component system **XuaSR** (liu2024intracellularremovalof pages 1-2). A figure in the paper diagrams this operon and functional partitioning (liu2024intracellularremovalof media e38dc1f7).

### 1.2 PUL-mediated xylan utilization in Bacteroidota (outer-membrane capture, import, and periplasmic processing)
Recent cultivation/genome work in marine anaerobic Bacteroidota identifies multiple candidate **xylan PULs** encoding **SusC/SusD** capture-import components and xylan-active GHs; e.g., *Halosquirtibacter xylanolyticus* contains multiple candidate xylan loci (PUL9/PUL29) with predicted GH10 endoxylanase and periplasmic GH3 β-xylosidase-like enzymes (nguyen2024halosquirtibacterlaminarinigen. pages 15-17). This is consistent with broader models where **SusC/D TonB-dependent systems** import large oligosaccharides into the periplasm (novak2024currentmodelsin pages 2-4).

### 1.3 Regulation: HTCS, ECF-σ/anti-σ systems, and CCR
Regulation is increasingly treated as a first-class component of hemicellulose traits. A 2024 review synthesizes that **canonical regulatory mechanisms** for hemicellulase-encoding genes include **hybrid two-component systems (HTCS)**, **ECF-σ/anti-σ systems**, and **carbon catabolite repression (CCR)**, with explicit mechanistic descriptions (substrate sensing, σ release, glucose repression) (novak2024currentmodelsin pages 2-4, novak2024currentmodelsin pages 1-2).

### 1.4 Expanding ecological breadth: anoxic peat xylan degraders (Verrucomicrobiota)
A 2024 study shows that anoxic incubation of fen peat with xylan robustly enriches **Verrucomicrobiota** and reveals a dominant Chthoniobacteraceae lineage (“Candidatus *Chthoniomicrobium xylanophilum*” SH-KS-3) with predicted endoxylanase/xylosidase capacity (rakitin2024verrucomicrobiaofthe pages 5-7, rakitin2024verrucomicrobiaofthe pages 1-2). This extends xylan degradation beyond the classical gut/industrial organisms into peatland anaerobic consortia.

## 2. Candidate graph nodes (grouped by type)

### 2.1 Pathways / modules
* **Extracellular xylan depolymerization module** (endo-xylanases + accessory/debranching enzymes) (rakitin2024verrucomicrobiaofthe pages 2-3, gonzalez‐alonso2026cerealarabinoxylans—theirenzymatic pages 9-10).
* **PUL-mediated xylan utilization module (Bacteroidota):** SusD-like binding + SusC-like TonB-dependent transport + periplasmic/cell-surface CAZymes (novak2024currentmodelsin pages 2-4, nguyen2024halosquirtibacterlaminarinigen. pages 15-17).
* **Xua intracellular AXOS import and processing module (R. cellulolyticum):** xuaABCDD’EFGHIJ (ABC import + GH51/GH43/GH8/GH39 + esterases) regulated by XuaSR (liu2024intracellularremovalof pages 1-2, liu2024intracellularremovalof media e38dc1f7).
* **Accessory ester cleavage module** for lignin-carbohydrate complexes (CE15 glucuronoyl esterases cooperating with xylanases) (pentari2025exploringthesynergy pages 1-2).

### 2.2 Environmental / experimental factors
* **Anoxic/anaerobic conditions** (e.g., N2:CO2 80:20) in peat xylan enrichments (rakitin2024verrucomicrobiaofthe pages 2-3).
* **Substrate type and decoration complexity:** arabinoxylan vs glucuronoxylan vs glucuronoarabinoxylan; acetylation/feruloylation levels (rakitin2024verrucomicrobiaofthe pages 2-3, gonzalez‐alonso2026cerealarabinoxylans—theirenzymatic pages 9-10).
* **Carbon catabolite repression (glucose availability)** as negative regulator of hemicellulase genes (novak2024currentmodelsin pages 2-4).

### 2.3 Genes / proteins / enzymes (examples)
**Core backbone hydrolysis**
* Endo-1,4-β-xylanase (EC 3.2.1.8) (rakitin2024verrucomicrobiaofthe pages 2-3).

**Oligomer trimming**
* Xylan 1,4-β-D-xylosidase (EC 3.2.1.37) (rakitin2024verrucomicrobiaofthe pages 2-3).

**Debranching / accessory enzymes**
* α-L-arabinofuranosidase (EC 3.2.1.55) (rakitin2024verrucomicrobiaofthe pages 2-3).
* α-D-glucuronidase (EC 3.2.1.139) (rakitin2024verrucomicrobiaofthe pages 2-3).
* Acetyl xylan esterase (EC 3.1.1.72) (rakitin2024verrucomicrobiaofthe pages 2-3).
* Ferulic acid esterase (EC 3.1.1.73) and p-coumaroyl esterase activity (rakitin2024verrucomicrobiaofthe pages 2-3, liu2024intracellularremovalof pages 1-2).
* CE15 glucuronoyl esterases (cleaving lignin–carbohydrate ester linkages involving glucuronoxylan) and synergy with xylanases (pentari2025exploringthesynergy pages 1-2).

**Transport and sensing**
* **SusC/SusD** (TonB-dependent outer-membrane transport system) (novak2024currentmodelsin pages 2-4, nguyen2024halosquirtibacterlaminarinigen. pages 15-17).
* **ABC transporter for AXOS (XuaA/B/C)** in *R. cellulolyticum* (liu2024intracellularremovalof pages 1-2, liu2024intracellularremovalof media e38dc1f7).

**Regulators**
* **Two-component systems** (e.g., XuaSR) (liu2024intracellularremovalof pages 1-2).
* **HTCS, ECF-σ/anti-σ, CCR** as canonical regulatory mechanisms (novak2024currentmodelsin pages 2-4).

### 2.4 Chemicals / metabolites
* Xylan / arabinoxylan / glucuronoxylan (polymer substrates) (rakitin2024verrucomicrobiaofthe pages 2-3).
* Xylo-oligosaccharides / arabinoxylo-oligosaccharides (AXOS) (liu2024intracellularremovalof pages 1-2, friess2024twoextracellularαarabinofuranosidases pages 1-2).
* Xylose (monomer product) (rakitin2024verrucomicrobiaofthe pages 2-3).
* Ferulic acid and p-coumaric acid (decorations; liberated by esterases) (rakitin2024verrucomicrobiaofthe pages 2-3, liu2024intracellularremovalof pages 1-2).

## 3. Mechanistic evidence image (gene cluster schematic)
Figure evidence of the curatable **xua** gene cluster organization and functional partitioning (TCS, ABC importer, intracellular GHs, esterases): (liu2024intracellularremovalof media e38dc1f7).

## 4. Candidate causal edges (evidence-backed)
The table below is designed for direct use in `xylan_degradation.yaml` drafting (with uncertainty flags where appropriate).

| Edge (S–P–O) | Evidence snippet (quoted) | Source (DOI, year, URL) | Context/notes | Suggested ontology grounding |
|---|---|---|---|---|
| xua operon (xuaABCDD’EFGHIJ) — enabled_by — XuaSR two-component system | “This operon forms a functional unit regulated by the two-component system XuaSR.” (liu2024intracellularremovalof pages 1-2) | Liu et al. 2024. DOI:10.1186/s12934-024-02423-z. https://doi.org/10.1186/s12934-024-02423-z | Directly tested in *Ruminiclostridium cellulolyticum*; operon-level regulatory edge for intracellular AXOS utilization. | S: label-only `xua_operon`; O: GO:0000160 (phosphorelay signal transduction system), NCBITaxon:NCBITaxon_2460932 |
| arabinoxylan — induces/upregulates — xuaABCD genes | “xuaABCD are strongly upregulated on arabinoxylan” (liu2024intracellularremovalof pages 1-2) | Liu et al. 2024. DOI:10.1186/s12934-024-02423-z. https://doi.org/10.1186/s12934-024-02423-z | Substrate-specific expression response; assay-specific to growth on arabinoxylan in *R. cellulolyticum*. | S: CHEBI:61051 (xylan, approximate parent); O: label-only `xuaABCD` |
| xuaA disruption — impairs — growth on arabinoxylan | “disruption of xuaA… impairs growth on AX” (liu2024intracellularremovalof pages 1-2) | Liu et al. 2024. DOI:10.1186/s12934-024-02423-z. https://doi.org/10.1186/s12934-024-02423-z | Direct gene–phenotype link; note reported polar effect on downstream genes, so single-gene causality should be curated cautiously. | S: label-only `xuaA`; O: METPO:traitmech:000113 |
| XuaA — binds/import-enables — arabinoxylodextrins (AXOS) up to DP6 | “XuaA is a solute-binding protein that binds AXOS up to six sugars” (liu2024intracellularremovalof pages 1-2) | Liu et al. 2024. DOI:10.1186/s12934-024-02423-z. https://doi.org/10.1186/s12934-024-02423-z | Direct transporter-binding evidence; intracellular utilization pathway after extracellular depolymerization. | S: label-only `XuaA`; O: label-only `arabinoxylodextrins/AXOS` |
| XuaB/XuaC — forms transporter for — arabinoxylodextrin import | “XuaB and XuaC form the membrane channel” (liu2024intracellularremovalof pages 1-2) | Liu et al. 2024. DOI:10.1186/s12934-024-02423-z. https://doi.org/10.1186/s12934-024-02423-z | Direct structural/functional assignment in ABC-type importer; import step is intracellular branch of xylan utilization. | S: label-only `XuaB/XuaC`; O: GO:1902600 (proton-independent transmembrane transport, approximate) |
| XuaD (GH51) — removes arabinosyl decorations from — AXOS | “XuaD and XuaE (GH51 and GH43) remove arabinosyl decorations” (liu2024intracellularremovalof pages 1-2) | Liu et al. 2024. DOI:10.1186/s12934-024-02423-z. https://doi.org/10.1186/s12934-024-02423-z | Direct enzymatic role for intracellular debranching of imported oligosaccharides. | S: EC:3.2.1.55; O: CHEBI:16646 (arabinose, released substituent) |
| XuaE (GH43) — removes arabinosyl decorations from — AXOS | “XuaD and XuaE (GH51 and GH43) remove arabinosyl decorations” (liu2024intracellularremovalof pages 1-2) | Liu et al. 2024. DOI:10.1186/s12934-024-02423-z. https://doi.org/10.1186/s12934-024-02423-z | Direct intracellular accessory-enzyme role. | S: EC:3.2.1.55; O: CHEBI:16646 |
| XuaF/XuaG — hydrolyzes — xylosyl units/backbone in imported AXOS | “XuaF and XuaG (GH8 and GH39) act on xylosyl units/backbone.” (liu2024intracellularremovalof pages 1-2) | Liu et al. 2024. DOI:10.1186/s12934-024-02423-z. https://doi.org/10.1186/s12934-024-02423-z | Direct intracellular oligomer-processing step; exact substrate partitioning between XuaF and XuaG may need finer curation. | S: EC:3.2.1.8 and/or EC:3.2.1.37 (family-dependent approximate); O: CHEBI:53598 (xylo-oligosaccharide, approximate) |
| XuaJ — has_activity — acetyl xylan esterase activity | “XuaJ shows acetyl esterase activity on model substrates” (liu2024intracellularremovalof pages 1-2) | Liu et al. 2024. DOI:10.1186/s12934-024-02423-z. https://doi.org/10.1186/s12934-024-02423-z | Direct biochemical evidence; intracellular deacylation of imported decorated AXOS. | S: EC:3.1.1.72; O: GO:0008408 (acetylesterase activity) |
| XuaH — has_activity — feruloyl/p-coumaroyl esterase activity on AXOS | “XuaH is a feruloyl- and p-coumaroyl-esterase active on oligosaccharides from wheat bran/straw” (liu2024intracellularremovalof pages 1-2) | Liu et al. 2024. DOI:10.1186/s12934-024-02423-z. https://doi.org/10.1186/s12934-024-02423-z | Direct biochemical evidence; intracellular removal of hydroxycinnamate decorations. | S: EC:3.1.1.73; O: CHEBI:17334 (ferulic acid) / CHEBI:25901 (p-coumaric acid, approximate) |
| SusC/SusD system — imports — large xylan-derived oligosaccharides into periplasm | “TonB-dependent systems (SusC/D in Bacteroides) that import large oligosaccharides into the periplasm” (novak2024currentmodelsin pages 2-4) | Novak & Gardner 2024. DOI:10.1007/s00253-023-12977-4. https://doi.org/10.1007/s00253-023-12977-4 | Review-level mechanistic consensus; Gram-negative/Bacteroidota-specific outer-membrane transport edge. | S: label-only `SusC/SusD complex`; O: CHEBI:53598 |
| HTCS — activates expression of — xylanase/hemicellulase genes | “HTCS have been linked to regulation of genes encoding xylanases and related enzymes” (novak2024currentmodelsin pages 1-2) | Novak & Gardner 2024. DOI:10.1007/s00253-023-12977-4. https://doi.org/10.1007/s00253-023-12977-4 | Review synthesis across taxa; useful high-level regulatory edge, but often taxon/system-specific. | S: GO:0000155 (two-component sensor activity, approximate HTCS-related); O: GO:0016998 (cell wall macromolecule catabolic process, approximate) |
| ECF-σ/anti-σ system — regulates — TonB-dependent transporter genes | “ECF-σ/anti-σ systems… in Bacteroides frequently regulate TonB-dependent transporter genes” (novak2024currentmodelsin pages 2-4) | Novak & Gardner 2024. DOI:10.1007/s00253-023-12977-4. https://doi.org/10.1007/s00253-023-12977-4 | Review-level generalized edge; relevant to PUL expression and xylan sensing in Bacteroidota. | S: GO:0001076 (RNA polymerase sigma factor activity); O: label-only `TonB-dependent transporter genes` |
| carbon catabolite repression (CCR) — represses — hemicellulase gene expression during glucose availability | “carbon catabolite repression (CCR)… HPr/CcpA mediate glucose-dependent repression” (novak2024currentmodelsin pages 2-4) | Novak & Gardner 2024. DOI:10.1007/s00253-023-12977-4. https://doi.org/10.1007/s00253-023-12977-4 | Broad regulatory edge; not xylan-exclusive but directly relevant to trait expression conditions. | S: GO:0009401 (phosphoenolpyruvate-dependent sugar phosphotransferase system, approximate context); O: GO:0016998 |
| beechwood xylan — upregulates — GH67 α-glucuronosidase peg.549 | “enzymes targeting 4-O-methyl glucuronyl and acetyl esters are upregulated on beechwood xylan” (mukherjee2023comprehensivegenomeanalysis pages 10-12) | Mukherjee et al. 2023. DOI:10.1128/spectrum.05028-22. https://doi.org/10.1128/spectrum.05028-22 | qRT-PCR-supported substrate response in *Paenibacillus* sp. LS1; exact fold change not provided in current context. | S: CHEBI:61051; O: EC:3.2.1.139 |
| beechwood xylan — upregulates — acetyl xylan esterases CE2/CE7 (peg.3462/peg.3463) | “enzymes targeting 4-O-methyl glucuronyl and acetyl esters are upregulated on beechwood xylan” (mukherjee2023comprehensivegenomeanalysis pages 10-12) | Mukherjee et al. 2023. DOI:10.1128/spectrum.05028-22. https://doi.org/10.1128/spectrum.05028-22 | qRT-PCR-supported; taxon-specific to LS1. | S: CHEBI:61051; O: EC:3.1.1.72 |
| peg.1759 (GH43) — enables removal of — arabinose side chains from xylan | “the genome encodes 10 alpha-L-arabinofuranosidases… Specific genes: peg.1759 is a secreted GH43 multi-domain AbfB-containing enzyme” (mukherjee2023comprehensivegenomeanalysis pages 2-4) | Mukherjee et al. 2023. DOI:10.1128/spectrum.05028-22. https://doi.org/10.1128/spectrum.05028-22 | Genomic/annotation-based functional assignment in LS1; likely extracellular due to signal peptide. **Uncertain** at exact substrate scope unless biochemically tested. | S: label-only `peg.1759`; O: EC:3.2.1.55 |
| peg.549 (GH67) — removes — 4-O-methyl-glucuronyl substitutions from xylan oligosaccharides | “peg.549 is a GH67 xylan alpha-1,2-glucuronosidase… lacks a signal peptide (likely intracellular)” (mukherjee2023comprehensivegenomeanalysis pages 2-4) | Mukherjee et al. 2023. DOI:10.1128/spectrum.05028-22. https://doi.org/10.1128/spectrum.05028-22 | Likely intracellular debranching after oligomer uptake. **Uncertain** because current context emphasizes annotation/expression more than direct enzyme assay. | S: label-only `peg.549`; O: EC:3.2.1.139 |
| PUL9/PUL29 SusC/SusD — imports — xylan-derived oligosaccharides | “PUL9 and PUL29 contain SusC/SusD (oligosaccharide capture and import)” (nguyen2024halosquirtibacterlaminarinigen. pages 15-17) | Nguyen et al. 2024. DOI:10.1038/s41598-024-74787-6. https://doi.org/10.1038/s41598-024-74787-6 | PUL-level inference in *Halosquirtibacter xylanolyticus*; strong genomic prediction, phenotype supported by growth on xylan. **Uncertain** at direct transport assay level. | S: label-only `PUL9/PUL29 SusC/SusD`; O: CHEBI:53598 |
| PUL9 GH10 — hydrolyzes — xylan backbone | “a GH10 in PUL9 with similarity to endo-1,4-β-xylanase (backbone cleavage)” (nguyen2024halosquirtibacterlaminarinigen. pages 15-17) | Nguyen et al. 2024. DOI:10.1038/s41598-024-74787-6. https://doi.org/10.1038/s41598-024-74787-6 | Genomic similarity-based assignment within candidate xylan PUL. **Uncertain** until purified-enzyme validation. | S: GH10 endoxylanase / EC:3.2.1.8; O: CHEBI:61051 |
| PUL9/PUL29 GH3 — hydrolyzes — xylo-oligosaccharides to xylose | “a GH3 in PUL9/PUL29 with periplasmic localization consistent with β-xylosidase action on oligomers” (nguyen2024halosquirtibacterlaminarinigen. pages 15-17) | Nguyen et al. 2024. DOI:10.1038/s41598-024-74787-6. https://doi.org/10.1038/s41598-024-74787-6 | Periplasmic oligomer-processing edge inferred from localization and homology. **Uncertain**. | S: EC:3.2.1.37; O: CHEBI:53598 / CHEBI:27306 (xylose) |
| PUL29 GH5_46 — acts_on — xylan chain | “PUL29 encodes a multidomain GH5_46 likely acting on the xylan chain” (nguyen2024halosquirtibacterlaminarinigen. pages 15-17) | Nguyen et al. 2024. DOI:10.1038/s41598-024-74787-6. https://doi.org/10.1038/s41598-024-74787-6 | Homology-based functional inference in marine anaerobic Bacteroidota. **Uncertain**. | S: label-only `GH5_46 enzyme`; O: CHEBI:61051 |
| xylan amendment under anoxic peat conditions — enriches — Verrucomicrobiota | “Verrucomicrobiota constituted 43.7% and 40.9%… In the original peat, Verrucomicrobiota were ~6% and ~3%” (rakitin2024verrucomicrobiaofthe pages 5-7) | Rakitin et al. 2024. DOI:10.3390/microorganisms12112271. https://doi.org/10.3390/microorganisms12112271 | Community-level ecological edge under anaerobic xylan enrichment; trait-associated but not single-organism mechanistic proof. | S: ENVO:01001305 (peatland, approximate) + CHEBI:61051 + anaerobic condition label; O: NCBITaxon:74201 (Verrucomicrobiota) |
| xylan amendment under anoxic peat conditions — enriches — OTU1 (Chthoniobacteraceae-affiliated) | “A single Verrucomicrobiota OTU1 represented 42.2% and 40.1%… (original <0.1%)” (rakitin2024verrucomicrobiaofthe pages 5-7) | Rakitin et al. 2024. DOI:10.3390/microorganisms12112271. https://doi.org/10.3390/microorganisms12112271 | Strong enrichment evidence for taxon associated with xylan degradation in peat consortia. | S: CHEBI:61051 + anaerobic condition label; O: NCBITaxon:2034943 (Chthoniobacteraceae, approximate family grounding) |
| SH-KS-3 genome — encodes — endo-1,4-β-xylanase activity | “An analysis of the SH-KS-3 genome revealed potential endo-1,4-beta-xylanases” (rakitin2024verrucomicrobiaofthe pages 1-2) | Rakitin et al. 2024. DOI:10.3390/microorganisms12112271. https://doi.org/10.3390/microorganisms12112271 | Genome-predicted function in ‘Ca. *Chthoniomicrobium xylanophilum*’; **uncertain** because enzyme not directly characterized. | S: label-only `SH-KS-3 xylanase gene(s)`; O: EC:3.2.1.8 |
| SH-KS-3 genome — encodes — xylan 1,4-β-xylosidase activity | “as well as xylan beta-1,4-xylosidases and other enzymes involved in xylan utilization” (rakitin2024verrucomicrobiaofthe pages 1-2) | Rakitin et al. 2024. DOI:10.3390/microorganisms12112271. https://doi.org/10.3390/microorganisms12112271 | Genome-predicted oligomer-to-xylose conversion; **uncertain** without biochemical assay. | S: label-only `SH-KS-3 xylosidase gene(s)`; O: EC:3.2.1.37 |
| acid-stable GH10 xylanase Xyn10C — hydrolyzes — xylan at acidic pH/high temperature | “optimal activity at 80 °C and pH 5.0” (xia2024clusteredsurfaceamino pages 2-4) | Xia et al. 2024. DOI:10.1007/s00253-024-13045-1. https://doi.org/10.1007/s00253-024-13045-1 | Enzyme-property edge relevant to performance under acidic environments; fungal enzyme, not a whole-cell trait edge. | S: label-only `Xyn10C`; O: EC:3.2.1.8 |
| clustered surface amino acid substitutions — increases — GH10 xylanase thermostability/acid stability | “A mutational change increased Xyn10RE thermostability by more than sixfold” (xia2024clusteredsurfaceamino pages 1-2) | Xia et al. 2024. DOI:10.1007/s00253-024-13045-1. https://doi.org/10.1007/s00253-024-13045-1 | Protein-engineering edge; useful for application layer rather than canonical trait mechanism. | S: label-only `stability-determining surface residues`; O: GO:0030288 (outer surface, rough approximation not ideal) |
| CE15 glucuronoyl esterases — increase saccharification by — xylanases on pretreated biomass | “AeGE15 and TlGE15 ‘increas[ed] saccharification by 57 ± 1 μM and 61 ± 3 μM of xylose equivalents’” (pentari2025exploringthesynergy pages 1-2) | Pentari et al. 2025. DOI:10.1186/s13068-025-02639-0. https://doi.org/10.1186/s13068-025-02639-0 | Direct synergy on pretreated lignocellulosic substrates; application-relevant cooperative edge. | S: EC:3.1.1.- (glucuronoyl esterase family CE15, no specific EC assigned); O: label-only `enhanced xylan saccharification` |
| CE15 glucuronoyl esterases + GH11 AnXyn11 — increases — birchwood hemicellulose hydrolysis | “raised degradation by the GH11 xylanase AnXyn11 ‘from 6% to approximately 10%’” (pentari2025exploringthesynergy pages 1-2) | Pentari et al. 2025. DOI:10.1186/s13068-025-02639-0. https://doi.org/10.1186/s13068-025-02639-0 | Direct cooperative edge on pretreated birchwood; substrate-specific and assay-specific. | S: CE15 + GH11 complex action (label-only); O: label-only `pretreated birchwood xylan hydrolysis` |
| CE15 glucuronoyl esterases — promotes — GH30 glucuronoxylanase aldouronic acid release | “leading up to three-times higher release in aldouronic acids” (pentari2025exploringthesynergy pages 1-2) | Pentari et al. 2025. DOI:10.1186/s13068-025-02639-0. https://doi.org/10.1186/s13068-025-02639-0 | Direct synergy with GH30 specificity toward glucuronoxylan-derived products. | S: CE15 glucuronoyl esterase; O: label-only `aldouronic acids` |
| AeGE15 + TmXyn10 — increases release of — xylose and xylotriose from pretreated corn bran | “increasing xylose and xylotriose release by 27 ± 8% and 55 ± 15%, respectively” (pentari2025exploringthesynergy pages 1-2) | Pentari et al. 2025. DOI:10.1186/s13068-025-02639-0. https://doi.org/10.1186/s13068-025-02639-0 | Direct cooperative edge; useful evidence that accessory esterases causally enhance backbone-cleaving xylanases. | S: label-only `AeGE15 + TmXyn10`; O: CHEBI:27306 (xylose) / CHEBI:53598 (xylotriose approximate) |


*Table: This table lists curation-ready candidate causal edges for microbial xylan degradation, with direct quotes, source details, context notes, and suggested ontology grounding. It is designed to support TraitMech graph construction for traitmech:000113 while flagging inferred or taxon-specific claims as uncertain.*

## 5. Current applications and real-world implementations (with data)

### 5.1 Biorefineries and lignocellulose saccharification (xylanase + accessory enzymes)
Accessory esterases that cleave lignin–carbohydrate cross-links can **increase xylanase-driven saccharification**. In pretreated biomass, two CE15 glucuronoyl esterases (AeGE15, TlGE15) increased measurable saccharification by **57 ± 1 μM** and **61 ± 3 μM** xylose equivalents, respectively (pentari2025exploringthesynergy pages 1-2, pentari2025exploringthesynergy pages 5-6). On pretreated birchwood, degradation by GH11 xylanase AnXyn11 increased **from ~6% to ~10%** with esterases (pentari2025exploringthesynergy pages 1-2). On destarched corn bran, AeGE15 + GH10 TmXyn10 increased **xylose** and **xylotriose** release by **27 ± 8%** and **55 ± 15%** (pentari2025exploringthesynergy pages 1-2). These quantitative results support a causal edge from **lignin-carbohydrate ester cleavage → improved xylan hydrolysis**.

### 5.2 Industrial enzyme deployment (food/feed/pulp/juice) and enzyme engineering
Xylanases (especially GH10) are used across **biofuels, animal feed, fruit juice clarification, and pulp bleaching** applications (xia2024clusteredsurfaceamino pages 1-2). Enzyme-property statistics relevant to implementation include reported GH10 xylanases with **optimal temperatures 70–90 °C** and stability at **pH 2.0**; in one fungal GH10 example, Xyn10C shows optimal activity at **80 °C, pH 5.0**, with strong activity retention after incubation at **pH 2.0** (xia2024clusteredsurfaceamino pages 2-4). Protein engineering can substantially shift stability: a mutational change increased Xyn10RE thermostability by **>6-fold** (xia2024clusteredsurfaceamino pages 1-2).

### 5.3 Environmental and microbiome-linked implementations (resource turnover; trait detection by enrichment)
Anoxic peat incubation with xylan strongly enriches taxa implicated in xylan breakdown: Verrucomicrobiota increased from **~6% and ~3% in original peat** to **43.7% and 40.9%** in enrichments, while Firmicutes rose from **<0.1%** to **50.6% and 56.0%** (rakitin2024verrucomicrobiaofthe pages 5-7). One Verrucomicrobiota OTU rose to **42.2% and 40.1%** (from **<0.1%**) (rakitin2024verrucomicrobiaofthe pages 5-7). These data provide a real-world measurement modality for “xylan degradation potential” in ecosystems via enrichment and sequencing.

## 6. Expert interpretation / analysis (authoritative synthesis)

*Trait expression is modular and context-dependent.* Recent work and synthesis emphasize that xylan degradation is not a single enzyme function but a coordinated system comprising **(i) polymer access/deconstruction**, **(ii) transport**, and **(iii) intracellular completion**, with regulation tuned by substrate complexity and carbon catabolite repression (novak2024currentmodelsin pages 2-4, liu2024intracellularremovalof pages 1-2). From a curation standpoint, this argues for decomposing `traitmech:000113` into graph submodules (e.g., “xylan backbone hydrolysis”, “xylan debranching”, “xylan-derived oligosaccharide import”, “intracellular deacylation”).

*Accessory activities can be causally important for complex substrates.* The CE15 synergy data quantify how removing lignin–carbohydrate barriers changes downstream xylanase effectiveness (pentari2025exploringthesynergy pages 1-2, pentari2025exploringthesynergy pages 7-9). This supports curating edges where “lignin–carbohydrate ester cleavage” positively regulates “xylan saccharification rate/yield” for bioprocess contexts.

## 7. Curation warnings (do-not-curate-yet / uncertain)

1. **Homology-only functional assignments.** Many PUL/MAG enzyme roles are inferred from GH family and localization; curate as **‘predicted’** unless biochemical/genetic validation is present (e.g., PUL GH10/GH3/GH5_46 roles in *Halosquirtibacter*) (nguyen2024halosquirtibacterlaminarinigen. pages 15-17).
2. **Polar effects in gene disruption.** The xuaA disruption phenotype is reported with a polar effect on downstream genes; edges from xuaA alone to growth impairment should be curated with a note that the effect is not strictly single-gene (liu2024intracellularremovalof pages 1-2).
3. **Review-level regulatory edges.** HTCS/ECF-σ/CCR mechanisms are authoritative but generalized; curate at a higher abstraction level (e.g., “HTCS → activates hemicellulase gene expression”) and avoid claiming specific regulators for specific taxa without primary evidence (novak2024currentmodelsin pages 2-4).
4. **Non-peer-reviewed / unclear-source materials.** Some mechanistic detail in the retrieved evidence comes from a 2025 “unknown journal” thesis-like document; prioritize peer-reviewed 2023–2024 sources for curation decisions (hinkley2025investigatingthemechanism pages 101-106, hinkley2025investigatingthemechanisma pages 30-36).

---

## DOI-first bibliography (publication date + URL)

1. **Liu N. et al. (2024-05)**. *Intracellular removal of acetyl, feruloyl and p-coumaroyl decorations on arabinoxylo-oligosaccharides imported from lignocellulosic biomass degradation by Ruminiclostridium cellulolyticum.* **Microbial Cell Factories**. DOI:10.1186/s12934-024-02423-z. https://doi.org/10.1186/s12934-024-02423-z (liu2024intracellularremovalof pages 1-2, liu2024intracellularremovalof media e38dc1f7)
2. **Novak JK, Gardner JG (2024-01)**. *Current models in bacterial hemicellulase-encoding gene regulation.* **Applied Microbiology and Biotechnology**. DOI:10.1007/s00253-023-12977-4. https://doi.org/10.1007/s00253-023-12977-4 (novak2024currentmodelsin pages 2-4, novak2024currentmodelsin pages 1-2)
3. **Mukherjee S. et al. (2023-06)**. *Comprehensive Genome Analysis of Cellulose and Xylan-Active CAZymes from the Genus Paenibacillus: Special Emphasis on the Novel Xylanolytic Paenibacillus sp. LS1.* **Microbiology Spectrum**. DOI:10.1128/spectrum.05028-22. https://doi.org/10.1128/spectrum.05028-22 (mukherjee2023comprehensivegenomeanalysis pages 2-4, mukherjee2023comprehensivegenomeanalysis pages 10-12, mukherjee2023comprehensivegenomeanalysis pages 1-2)
4. **Nguyen TTH. et al. (2024-10)**. *Halosquirtibacter laminarini gen. nov., sp. nov. and Halosquirtibacter xylanolyticus sp. nov., marine anaerobic laminarin and xylan degraders in the phylum Bacteroidota.* **Scientific Reports**. DOI:10.1038/s41598-024-74787-6. https://doi.org/10.1038/s41598-024-74787-6 (nguyen2024halosquirtibacterlaminarinigen. pages 15-17)
5. **Rakitin AL. et al. (2024-11-08)**. *Verrucomicrobia of the Family Chthoniobacteraceae Participate in Xylan Degradation in Boreal Peat Soils.* **Microorganisms**. DOI:10.3390/microorganisms12112271. https://doi.org/10.3390/microorganisms12112271 (rakitin2024verrucomicrobiaofthe pages 5-7, rakitin2024verrucomicrobiaofthe pages 2-3, rakitin2024verrucomicrobiaofthe pages 1-2)
6. **Xia Y. et al. (2024-02)**. *Clustered surface amino acid residues modulate the acid stability of GH10 xylanase in fungi.* **Applied Microbiology and Biotechnology**. DOI:10.1007/s00253-024-13045-1. https://doi.org/10.1007/s00253-024-13045-1 (xia2024clusteredsurfaceamino pages 2-4, xia2024clusteredsurfaceamino pages 1-2)
7. **Pentari C. et al. (2025-03)**. *Exploring the synergy between fungal CE15 glucuronoyl esterases and xylanases for lignocellulose saccharification.* **Biotechnology for Biofuels and Bioproducts**. DOI:10.1186/s13068-025-02639-0. https://doi.org/10.1186/s13068-025-02639-0 (pentari2025exploringthesynergy pages 1-2, pentari2025exploringthesynergy pages 7-9)



References

1. (rakitin2024verrucomicrobiaofthe pages 2-3): Andrey L. Rakitin, Irina S. Kulichevskaya, Alexey V. Beletsky, Andrey V. Mardanov, Svetlana N. Dedysh, and Nikolai V. Ravin. Verrucomicrobia of the family chthoniobacteraceae participate in xylan degradation in boreal peat soils. Microorganisms, 12:2271, Nov 2024. URL: https://doi.org/10.3390/microorganisms12112271, doi:10.3390/microorganisms12112271. This article has 51 citations.

2. (gonzalez‐alonso2026cerealarabinoxylans—theirenzymatic pages 9-10): Víctor González‐Alonso, Marko Verce, Luc De Vuyst, and Frédéric Leroy. Cereal arabinoxylans—their enzymatic degradation and relevance for breadmaking and human health. Comprehensive Reviews in Food Science and Food Safety, Jan 2026. URL: https://doi.org/10.1111/1541-4337.70391, doi:10.1111/1541-4337.70391. This article has 3 citations and is from a domain leading peer-reviewed journal.

3. (hinkley2025investigatingthemechanism pages 101-106): CE Hinkley. Investigating the mechanism of dietary fibre breakdown by the human and animal gut microbiota. Unknown journal, 2025.

4. (liu2024intracellularremovalof pages 1-2): Nian Liu, Elise Odinot, Hélène David, Nicolas Vita, Felipe Mejia Otalvaro, Goetz Parsiegla, Yann Denis, Craig Faulds, Henri-Pierre Fierobe, and Stéphanie Perret. Intracellular removal of acetyl, feruloyl and p-coumaroyl decorations on arabinoxylo-oligosaccharides imported from lignocellulosic biomass degradation by ruminiclostridium cellulolyticum. Microbial Cell Factories, May 2024. URL: https://doi.org/10.1186/s12934-024-02423-z, doi:10.1186/s12934-024-02423-z. This article has 6 citations and is from a peer-reviewed journal.

5. (mukherjee2023comprehensivegenomeanalysis pages 1-2): Saumashish Mukherjee, Tushar Dilipchand Lodha, and Jogi Madhuprakash. Comprehensive genome analysis of cellulose and xylan-active cazymes from the genus <i>paenibacillus</i> : special emphasis on the novel xylanolytic <i>paenibacillus</i> sp. ls1. Microbiology Spectrum, Jun 2023. URL: https://doi.org/10.1128/spectrum.05028-22, doi:10.1128/spectrum.05028-22. This article has 11 citations and is from a domain leading peer-reviewed journal.

6. (rakitin2024verrucomicrobiaofthe pages 5-7): Andrey L. Rakitin, Irina S. Kulichevskaya, Alexey V. Beletsky, Andrey V. Mardanov, Svetlana N. Dedysh, and Nikolai V. Ravin. Verrucomicrobia of the family chthoniobacteraceae participate in xylan degradation in boreal peat soils. Microorganisms, 12:2271, Nov 2024. URL: https://doi.org/10.3390/microorganisms12112271, doi:10.3390/microorganisms12112271. This article has 51 citations.

7. (liu2024intracellularremovalof media e38dc1f7): Nian Liu, Elise Odinot, Hélène David, Nicolas Vita, Felipe Mejia Otalvaro, Goetz Parsiegla, Yann Denis, Craig Faulds, Henri-Pierre Fierobe, and Stéphanie Perret. Intracellular removal of acetyl, feruloyl and p-coumaroyl decorations on arabinoxylo-oligosaccharides imported from lignocellulosic biomass degradation by ruminiclostridium cellulolyticum. Microbial Cell Factories, May 2024. URL: https://doi.org/10.1186/s12934-024-02423-z, doi:10.1186/s12934-024-02423-z. This article has 6 citations and is from a peer-reviewed journal.

8. (nguyen2024halosquirtibacterlaminarinigen. pages 15-17): Tra T. H. Nguyen, Tien Q. Vuong, Ho Le Han, and Song-Gun Kim. Halosquirtibacter laminarini gen. nov., sp. nov. and halosquirtibacter xylanolyticus sp. nov., marine anaerobic laminarin and xylan degraders in the phylum bacteroidota. Scientific Reports, Oct 2024. URL: https://doi.org/10.1038/s41598-024-74787-6, doi:10.1038/s41598-024-74787-6. This article has 7 citations and is from a peer-reviewed journal.

9. (novak2024currentmodelsin pages 2-4): Jessica K. Novak and Jeffrey G. Gardner. Current models in bacterial hemicellulase-encoding gene regulation. Applied Microbiology and Biotechnology, Jan 2024. URL: https://doi.org/10.1007/s00253-023-12977-4, doi:10.1007/s00253-023-12977-4. This article has 8 citations and is from a domain leading peer-reviewed journal.

10. (novak2024currentmodelsin pages 1-2): Jessica K. Novak and Jeffrey G. Gardner. Current models in bacterial hemicellulase-encoding gene regulation. Applied Microbiology and Biotechnology, Jan 2024. URL: https://doi.org/10.1007/s00253-023-12977-4, doi:10.1007/s00253-023-12977-4. This article has 8 citations and is from a domain leading peer-reviewed journal.

11. (rakitin2024verrucomicrobiaofthe pages 1-2): Andrey L. Rakitin, Irina S. Kulichevskaya, Alexey V. Beletsky, Andrey V. Mardanov, Svetlana N. Dedysh, and Nikolai V. Ravin. Verrucomicrobia of the family chthoniobacteraceae participate in xylan degradation in boreal peat soils. Microorganisms, 12:2271, Nov 2024. URL: https://doi.org/10.3390/microorganisms12112271, doi:10.3390/microorganisms12112271. This article has 51 citations.

12. (pentari2025exploringthesynergy pages 1-2): Christina Pentari, Constantinos Katsimpouras, Mireille Haon, Jean-Guy Berrin, Anastasia Zerva, and Evangelos Topakas. Exploring the synergy between fungal ce15 glucuronoyl esterases and xylanases for lignocellulose saccharification. Biotechnology for Biofuels and Bioproducts, Mar 2025. URL: https://doi.org/10.1186/s13068-025-02639-0, doi:10.1186/s13068-025-02639-0. This article has 6 citations and is from a domain leading peer-reviewed journal.

13. (friess2024twoextracellularαarabinofuranosidases pages 1-2): Lisa Friess, Francesca Bottacini, Fionnuala M. McAuliffe, Ian J. O’Neill, Paul D. Cotter, Ciaran Lee, Jose Munoz-Munoz, and Douwe van Sinderen. Two extracellular α-arabinofuranosidases are required for cereal-derived arabinoxylan metabolism by bifidobacterium longum subsp. longum. Gut Microbes, May 2024. URL: https://doi.org/10.1080/19490976.2024.2353229, doi:10.1080/19490976.2024.2353229. This article has 13 citations and is from a peer-reviewed journal.

14. (mukherjee2023comprehensivegenomeanalysis pages 10-12): Saumashish Mukherjee, Tushar Dilipchand Lodha, and Jogi Madhuprakash. Comprehensive genome analysis of cellulose and xylan-active cazymes from the genus <i>paenibacillus</i> : special emphasis on the novel xylanolytic <i>paenibacillus</i> sp. ls1. Microbiology Spectrum, Jun 2023. URL: https://doi.org/10.1128/spectrum.05028-22, doi:10.1128/spectrum.05028-22. This article has 11 citations and is from a domain leading peer-reviewed journal.

15. (mukherjee2023comprehensivegenomeanalysis pages 2-4): Saumashish Mukherjee, Tushar Dilipchand Lodha, and Jogi Madhuprakash. Comprehensive genome analysis of cellulose and xylan-active cazymes from the genus <i>paenibacillus</i> : special emphasis on the novel xylanolytic <i>paenibacillus</i> sp. ls1. Microbiology Spectrum, Jun 2023. URL: https://doi.org/10.1128/spectrum.05028-22, doi:10.1128/spectrum.05028-22. This article has 11 citations and is from a domain leading peer-reviewed journal.

16. (xia2024clusteredsurfaceamino pages 2-4): Yanwei Xia, Wei Wang, Yaning Wei, Chuanxu Guo, Sisi Song, Siqi Cai, and Youzhi Miao. Clustered surface amino acid residues modulate the acid stability of gh10 xylanase in fungi. Applied Microbiology and Biotechnology, Feb 2024. URL: https://doi.org/10.1007/s00253-024-13045-1, doi:10.1007/s00253-024-13045-1. This article has 7 citations and is from a domain leading peer-reviewed journal.

17. (xia2024clusteredsurfaceamino pages 1-2): Yanwei Xia, Wei Wang, Yaning Wei, Chuanxu Guo, Sisi Song, Siqi Cai, and Youzhi Miao. Clustered surface amino acid residues modulate the acid stability of gh10 xylanase in fungi. Applied Microbiology and Biotechnology, Feb 2024. URL: https://doi.org/10.1007/s00253-024-13045-1, doi:10.1007/s00253-024-13045-1. This article has 7 citations and is from a domain leading peer-reviewed journal.

18. (pentari2025exploringthesynergy pages 5-6): Christina Pentari, Constantinos Katsimpouras, Mireille Haon, Jean-Guy Berrin, Anastasia Zerva, and Evangelos Topakas. Exploring the synergy between fungal ce15 glucuronoyl esterases and xylanases for lignocellulose saccharification. Biotechnology for Biofuels and Bioproducts, Mar 2025. URL: https://doi.org/10.1186/s13068-025-02639-0, doi:10.1186/s13068-025-02639-0. This article has 6 citations and is from a domain leading peer-reviewed journal.

19. (pentari2025exploringthesynergy pages 7-9): Christina Pentari, Constantinos Katsimpouras, Mireille Haon, Jean-Guy Berrin, Anastasia Zerva, and Evangelos Topakas. Exploring the synergy between fungal ce15 glucuronoyl esterases and xylanases for lignocellulose saccharification. Biotechnology for Biofuels and Bioproducts, Mar 2025. URL: https://doi.org/10.1186/s13068-025-02639-0, doi:10.1186/s13068-025-02639-0. This article has 6 citations and is from a domain leading peer-reviewed journal.

20. (hinkley2025investigatingthemechanisma pages 30-36): CE Hinkley. Investigating the mechanism of dietary fibre breakdown by the human and animal gut microbiota. Unknown journal, 2025.