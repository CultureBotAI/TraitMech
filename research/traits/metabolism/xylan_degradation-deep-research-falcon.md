---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-30T00:04:09.666005'
end_time: '2026-06-30T00:22:33.708871'
duration_seconds: 1104.04
template_file: templates/trait_causal_graph_research.md
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
  causal_graph_summary: 'xylan_degradation_xylanase: 8 nodes, 5 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 41
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
- **Existing causal graph summary:** xylan_degradation_xylanase: 8 nodes, 5 edges

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
- **Existing causal graph summary:** xylan_degradation_xylanase: 8 nodes, 5 edges

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


# Xylan Degradation (traitmech:000113) — Curation-Focused Report

## 1. Trait Scope Summary

**Xylan degradation** is a biopolymer-degradation metabolism in which a microorganism hydrolyzes xylan — the most abundant hemicellulose in plant cell walls — into xylose and xylo-oligosaccharides using xylanases and a suite of accessory enzymes (christov1993esterasesofxylandegrading pages 1-2, leschonski2024structuredependentstimulationof pages 2-4). Xylan consists of a β-1,4-linked D-xylopyranosyl backbone that can be decorated with α-L-arabinofuranosyl residues, 4-O-methyl-D-glucuronic acid, acetyl groups, ferulic acid, and p-coumaric acid (liu2024intracellularremovalof pages 1-2, leschonski2024structuredependentstimulationof pages 2-4). Consequently, complete xylan degradation requires the synergistic action of backbone-cleaving endo-xylanases, exo-acting β-xylosidases, debranching enzymes (arabinofuranosidases, glucuronidases), and esterases (acetyl xylan esterase, feruloyl esterase) (christov1993esterasesofxylandegrading pages 1-2, lindic2025structuralandfunctional pages 9-10).

**Boundary cases:** Xylan degradation overlaps with but is distinct from cellulose degradation (parent: lignocellulose degradation) and pectin degradation. It includes degradation of arabinoxylan and glucuronoxylan as natural structural variants. Xyloglucan degradation is a separate trait, although shared GH families (e.g., GH5) may participate in both. The trait boundary extends to the release and import of xylo-oligosaccharides but does not include downstream fermentation of xylose to short-chain fatty acids or ethanol, which are separate metabolic traits.

---

## 2. Candidate Nodes Grouped by Type

The following table provides all candidate nodes for the xylan degradation causal graph, organized by entity type with suggested ontology identifiers where available.

| Node_Label | Node_Type | Suggested_CURIE | Notes |
|---|---|---|---|
| Xylan | substrate/chemical | CHEBI:18336 | Core hemicellulosic polymer degraded in this trait; β-1,4-linked xylopyranosyl backbone with variable substitutions (liu2024intracellularremovalof pages 1-2, leschonski2024structuredependentstimulationof pages 2-4) |
| Arabinoxylan | substrate/chemical | label-only | Decorated xylan bearing arabinofuranosyl substituents; common substrate in gut and rumen studies (liu2022selfishuptakeversus pages 1-2, leschonski2024structuredependentstimulationof pages 2-4) |
| Glucuronoxylan | substrate/chemical | label-only | Xylan decorated with glucuronic/4-O-methylglucuronic acid; relevant to GH30 glucuronoxylanases and CE15-linked contexts (liu2024intracellularremovalof pages 1-2, leschonski2024structuredependentstimulationof pages 2-4) |
| Xylooligosaccharides (XOS) | substrate/chemical | label-only | Soluble oligomeric products of endoxylanase action; imported or further hydrolyzed by β-xylosidases/exo-oligoxylanases (liu2022selfishuptakeversus pages 9-12, liu2022selfishuptakeversus pages 1-2) |
| Arabinoxylo-oligosaccharides (AXOS) | substrate/chemical | label-only | Decorated oligosaccharides produced from arabinoxylan; major imported intermediates in selfish uptake systems (liu2022selfishuptakeversus pages 9-12) |
| D-Xylose | substrate/chemical | CHEBI:15440 | Major monomer released from xylan and substrate for downstream catabolism (liu2022selfishuptakeversus pages 9-12, liu2023theweimbergpathway pages 1-3) |
| L-Arabinose | substrate/chemical | CHEBI:30851 | Side-chain sugar released by arabinofuranosidases during arabinoxylan debranching (liu2022selfishuptakeversus pages 9-12, liu2022selfishuptakeversus pages 6-9) |
| 4-O-Methyl-D-glucuronic acid | substrate/chemical | label-only | Uronic acid substituent on glucuronoxylan removed by α-glucuronidases; grounding uncertain here (christov1993esterasesofxylandegrading pages 1-2, leschonski2024structuredependentstimulationof pages 2-4) |
| Acetic acid | substrate/chemical | CHEBI:15366 | Product of acetyl xylan esterase activity on acetylated xylan/AXOS (liu2024intracellularremovalof pages 1-2, leschonski2024structuredependentstimulationof pages 2-4) |
| Ferulic acid | substrate/chemical | CHEBI:17620 | Phenolic substituent removed by feruloyl esterases; can cross-link arabinoxylans (liu2024intracellularremovalof pages 1-2, leschonski2024structuredependentstimulationof pages 2-4) |
| p-Coumaric acid | substrate/chemical | CHEBI:32974 | Phenolic decoration removed from acylated AXOS in some systems such as XuaH-containing clusters (liu2024intracellularremovalof pages 1-2) |
| D-Xylulose-5-phosphate | metabolite | label-only | Product of xylulose phosphorylation by XylB; entry point into PPP in isomerase pathway (liu2023theweimbergpathway pages 1-3, park2025xylosemetabolismand pages 2-3) |
| α-Ketoglutarate | metabolite | CHEBI:16810 | Downstream product of the Weimberg pathway in non-phosphorylative xylose catabolism (liu2023theweimbergpathway pages 1-3) |
| Endo-1,4-β-xylanase | enzyme | EC:3.2.1.8 | Main backbone-cleaving hydrolase; represented across GH5/GH10/GH11/GH30 families depending taxon/substrate (leschonski2024structuredependentstimulationof pages 2-4) |
| Glucuronoarabinoxylan endo-1,4-β-xylanase | enzyme | EC:3.2.1.136 | GH30 glucuronoxylanase activity specialized for substituted xylans (leschonski2024structuredependentstimulationof pages 2-4) |
| β-Xylosidase | enzyme | EC:3.2.1.37 | Hydrolyzes XOS to xylose; common in GH3/GH43/GH120 and often intracellular/periplasmic (christov1993esterasesofxylandegrading pages 1-2, leschonski2024structuredependentstimulationof pages 2-4) |
| Reducing-end xylose-releasing exo-oligoxylanase | enzyme | EC:3.2.1.156 | Rex-type exo-enzyme acting on oligoxylans from reducing end; reported in AX/AXOS systems (leschonski2024structuredependentstimulationof pages 2-4, liu2022selfishuptakeversus pages 6-9) |
| α-L-Arabinofuranosidase | enzyme | EC:3.2.1.55 | Removes arabinose decorations from arabinoxylan/AXOS; common in GH43/GH51/GH62 (christov1993esterasesofxylandegrading pages 1-2, leschonski2024structuredependentstimulationof pages 2-4) |
| α-Glucuronidase | enzyme | EC:3.2.1.139 | Removes glucuronic/4-O-methylglucuronic acid substituents from xylan (leschonski2024structuredependentstimulationof pages 2-4, lindic2025structuralandfunctional pages 9-10) |
| Acetyl xylan esterase | enzyme | EC:3.1.1.72 | Deacetylates xylan or AXOS; found extracellularly and intracellularly in Xua-like systems (leschonski2024structuredependentstimulationof pages 2-4, liu2024intracellularremovalof pages 1-2) |
| Feruloyl esterase | enzyme | EC:3.1.1.73 | Removes feruloyl esters from decorated xylans/AXOS; helps relieve steric recalcitrance (leschonski2024structuredependentstimulationof pages 2-4, liu2024intracellularremovalof pages 1-2) |
| Xylose isomerase | enzyme/gene product | EC:5.3.1.5 | Encoded by xylA; converts D-xylose to D-xylulose in bacterial isomerase pathway (liu2023theweimbergpathway pages 1-3, park2025xylosemetabolismand pages 2-3) |
| Xylulokinase | enzyme/gene product | EC:2.7.1.17 | Encoded by xylB; converts D-xylulose to D-xylulose-5-phosphate (liu2023theweimbergpathway pages 1-3, park2025xylosemetabolismand pages 2-3) |
| SusC/SusD-like system | transporter complex | label-only | Canonical Bacteroidetes glycan capture/import apparatus associated with xylan PULs and TonB-dependent uptake across outer membrane (panwar2025transcriptionaldelineationof pages 5-7, zhang2014xylanutilizationin pages 6-7) |
| ABC transporter (Xua system) | transporter complex | label-only | Gram-positive importer for AXOS/arabinoxylodextrins; includes XuaA/B/C in R. cellulolyticum-like selfish systems (liu2022selfishuptakeversus pages 9-12, liu2022selfishuptakeversus pages 2-4) |
| MFS transporter | transporter | label-only | Monosaccharide/small-solute transporter found in some xylan PUL-associated loci such as Segatella copri PUL15 (panwar2025transcriptionaldelineationof pages 5-7) |
| TonB-dependent transporter | transporter | label-only | Outer membrane transporter used by Bacteroidetes for oligosaccharide uptake into periplasm (martin2025metabolismofhemicelluloses pages 3-5, zhang2014xylanutilizationin pages 2-2) |
| HTCS | regulatory component | label-only | Hybrid two-component system widely used to sense oligosaccharides and activate hemicellulase/PUL genes (novak2024currentmodelsin pages 1-2, panwar2025transcriptionaldelineationof pages 5-7) |
| ECF-σ/anti-σ system | regulatory component | label-only | Alternative bacterial hemicellulase regulatory module documented in multiple Gram-positive systems (novak2024currentmodelsin pages 1-2, novak2024currentmodelsin pages 4-5) |
| XlnR/Xyr1 transcription factor | regulatory component | label-only | Fungal Zn2Cys6 activator controlling xylanolytic enzyme expression and often pentose/cellulase programs (kerkaert2023regulationofnutrient pages 36-38, kerkaert2023regulationofnutrient pages 5-6) |
| AraR/XylR repressors | regulatory component | label-only | LacI-family bacterial regulators co-controlling arabinan/xylan utilization genes, often integrated with CCR (novak2024currentmodelsin pages 4-5) |
| CCR / CcpA | regulatory component | label-only | Gram-positive carbon catabolite repression system that can repress xylan/xylose utilization under preferred carbon sources (novak2024currentmodelsin pages 1-2, novak2024currentmodelsin pages 2-4) |
| cAMP-CRP | regulatory component | label-only | Gram-negative carbon catabolite control complex promoting non-preferred carbon metabolism gene expression (novak2024currentmodelsin pages 2-4) |
| σI6/σI7 alternative sigma factors | regulatory component | label-only | Clostridial alternative sigma factors implicated in stronger xylanase/cellulosomal xylan gene expression on xylan (novak2024currentmodelsin pages 4-5, novak2024currentmodelsin pages 15-16) |
| Xylan utilization system (XUS) | biological process/module | label-only | Bacteroidetes xylan-degrading apparatus including SusC/D homologs, HTCS and GH10-rich loci (zhang2014xylanutilizationin pages 2-2, zhang2014xylanutilizationin pages 6-7) |
| Polysaccharide utilization locus (PUL) | biological process/module | label-only | Gene cluster architecture encoding binding, sensing, transport, and hydrolysis functions for specific glycans (panwar2025transcriptionaldelineationof pages 5-7, zhang2014xylanutilizationin pages 6-7) |
| Cellulosome | biological process/module | GO:0046177 | Extracellular multienzyme complex used by some anaerobes for coordinated plant cell wall/xylan deconstruction (lindic2025structuralandfunctional pages 9-10) |
| Pentose phosphate pathway | pathway | KEGG:map00030 | Central assimilation route for xylulose-5-phosphate generated from xylose isomerase pathway (liu2023theweimbergpathway pages 1-3, dvorak2024syntheticallyprimedadaptationof pages 3-4) |
| Weimberg pathway | pathway | label-only | Non-phosphorylative xylose oxidative pathway converting xylose to α-ketoglutarate (liu2023theweimbergpathway pages 1-3) |
| Extracellular | cellular localization | GO:0005576 | Frequent location for secreted xylanases, esterases, and cellulosomal attack on polymeric xylan (liu2022selfishuptakeversus pages 1-2, lindic2025structuralandfunctional pages 9-10) |
| Periplasm | cellular localization | GO:0042597 | Bacteroidetes compartment where imported xylan-derived oligosaccharides undergo further processing (zhang2014xylanutilizationin pages 2-2) |
| Cytoplasm | cellular localization | GO:0005737 | Site of Xua-mediated AXOS degradation and xylose catabolic pathways such as xylA/xylB or Weimberg (liu2022selfishuptakeversus pages 9-12, liu2023theweimbergpathway pages 1-3) |
| Cell surface (outer membrane) | cellular localization | GO:0009279 | Site of SusC/SusD-like binding, outer-membrane transport, and initial glycan capture in Bacteroidetes (martin2025metabolismofhemicelluloses pages 3-5, zhang2014xylanutilizationin pages 6-7) |


*Table: This table lists candidate causal graph nodes for microbial xylan degradation, grouped by entity type and annotated with suggested ontology identifiers where available. It is designed to support TraitMech curation by linking substrates, enzymes, transporters, regulators, pathways, and localizations to evidence-backed roles.*

### Key Notes on Node Selection

**Enzyme diversity across GH families.** Endo-1,4-β-xylanases span GH families 5, 8, 10, 11, and 30, each with distinct substrate specificity: GH10 xylanases accommodate arabinose-substituted residues and produce smaller oligosaccharides, while GH11 xylanases are more sensitive to substitution and produce larger AXOS fragments (leschonski2024structuredependentstimulationof pages 2-4). GH30 glucuronoxylanases (EC 3.2.1.136) specifically require glucuronic acid at the −2 subsite (leschonski2024structuredependentstimulationof pages 2-4). β-Xylosidases are predominantly found in GH3, GH43, and GH120 families (leschonski2024structuredependentstimulationof pages 2-4). Arabinofuranosidases occur in GH43, GH51, and GH62, while α-glucuronidases belong to GH67 and GH115 (lindic2025structuralandfunctional pages 9-10).

**Transport system diversity.** Transport of xylan-derived oligosaccharides follows two major paradigms: (i) in Bacteroidetes, SusC/SusD-like TonB-dependent transporters import oligosaccharides across the outer membrane into the periplasm, where further hydrolysis occurs (zhang2014xylanutilizationin pages 2-2, panwar2025transcriptionaldelineationof pages 5-7); (ii) in Gram-positive bacteria (e.g., Ruminiclostridium cellulolyticum), ABC transporters (the Xua system) import large arabinoxylo-dextrins directly into the cytoplasm for intracellular degradation, constituting a "selfish uptake" strategy (liu2022selfishuptakeversus pages 9-12, liu2022selfishuptakeversus pages 1-2, liu2022selfishuptakeversus pages 2-4). The Xua ABC transporter solute-binding protein XuaA binds AXOS with nanomolar affinity (KD 12–63 nM) but does not bind monosaccharides (liu2022selfishuptakeversus pages 9-12).

**Regulatory architecture.** Three canonical regulatory mechanisms govern xylanase gene expression in bacteria: hybrid two-component systems (HTCS), extracytoplasmic function (ECF)-σ/anti-σ systems, and carbon catabolite repression (CCR) (novak2024currentmodelsin pages 1-2). In Bacteroidetes, HTCS regulators encoded within xylan PULs sense oligosaccharide signals and activate transcription of adjacent degradation/transport genes (novak2024currentmodelsin pages 1-2, panwar2025transcriptionaldelineationof pages 5-7). In Gram-positive anaerobes such as Clostridium thermocellum, alternative sigma factors σI6 and σI7 enable stronger cellulosomal xylanase expression in the presence of xylans (novak2024currentmodelsin pages 4-5, novak2024currentmodelsin pages 15-16). In filamentous fungi, the zinc binuclear cluster transcription factor XlnR/Xyr1 activates xylanolytic gene expression by recruiting the mediator complex subunit Gal11/Med15 (kerkaert2023regulationofnutrient pages 5-6).

---

## 3. Candidate Causal Edges

The following table presents evidence-backed subject–predicate–object triples proposed for the xylan degradation causal graph.

| Subject | Predicate | Object | Reference (DOI) | Supporting Snippet | Notes/Confidence |
|---|---|---|---|---|---|
| Endo-1,4-β-xylanase | hydrolyzes | Xylan | 10.1080/19490976.2024.2430419 | “Endoxylanases (EC 3.2.1.8 and EC 3.2.1.136) are glycoside hydrolases that hydrolyze internal glycosidic linkages of the xylan backbone” (leschonski2024structuredependentstimulationof pages 2-4) | Strong; directly stated in recent review. |
| Xylan | is_substrate_of | Endo-1,4-β-xylanase | 10.1080/19490976.2024.2430419 | “Endoxylanases… hydrolyze internal glycosidic linkages of the xylan backbone” (leschonski2024structuredependentstimulationof pages 2-4) | Strong inverse formulation of same evidence. |
| Endo-1,4-β-xylanase | produces | Xylooligosaccharides (XOS) | 10.1186/s13068-022-02225-8 | “extracellular endoxylanases cleave arabinoxylan backbones, releasing xylo-oligosaccharides (XOS)” (liu2022selfishuptakeversus pages 1-2) | Strong for decorated xylan substrates; broadly generalizable. |
| Endo-1,4-β-xylanase | produces | Arabinoxylo-oligosaccharides (AXOS) | 10.1080/19490976.2024.2430419 | “GH10 endoxylanases predominantly produce AXOS products like A3X, A2+3XX, and A3A3X” (leschonski2024structuredependentstimulationof pages 2-4) | Strong; substrate- and family-dependent product profile. |
| β-Xylosidase | hydrolyzes | XOS to D-Xylose | 10.1016/0141-0229(93)90078-g | “β-xylosidase (EC 3.2.1.37) cleaves xylooligosaccharides to produce xylose” (christov1993esterasesofxylandegrading pages 1-2) | Strong; foundational review. |
| α-L-Arabinofuranosidase | removes_substituent_from | Arabinoxylan, releasing L-Arabinose | 10.1186/s13068-022-02225-8 | “XuaD and XuaE are arabinofuranosidases that remove arabinose decorations” (liu2022selfishuptakeversus pages 6-9) | Strong for arabinoxylan/AXOS debranching. |
| α-Glucuronidase | removes_substituent_from | Glucuronoxylan, releasing 4-O-Methyl-D-glucuronic acid | 10.1016/0141-0229(93)90078-g | “α-glucuronidase… removes… methylglucuronic acid substituents” (christov1993esterasesofxylandegrading pages 1-2) | Moderate; product stated generally, not always directly measured in cited systems. |
| Acetyl xylan esterase | removes_substituent_from | Xylan, releasing Acetic acid | 10.1186/s12934-024-02423-z | “XuaJ removes acetyl groups” (liu2024intracellularremovalof pages 1-2) | Strong for acetylated xylan/AXOS; release of acetate is mechanistically implied. |
| Feruloyl esterase | removes_substituent_from | Arabinoxylan, releasing Ferulic acid | 10.1186/s12934-024-02423-z | “XuaH removes feruloyl and p-coumaroyl decorations” (liu2024intracellularremovalof pages 1-2) | Strong for acylated arabinoxylan-derived oligosaccharides. |
| SusC/SusD system | imports | XOS into periplasm | 10.1073/pnas.1406156111 | “oligosaccharides… are then transported by TonB-dependent transporters into the periplasm” (zhang2014xylanutilizationin pages 2-2) | Moderate; SusC/SusD-like systems are the canonical outer-membrane apparatus in xylan PULs, but XOS specificity varies by system. |
| ABC transporter (Xua) | imports | AXOS into cytoplasm | 10.1186/s13068-022-02225-8 | “an ABC transporter dedicated to the import of large arabinoxylodextrins” (liu2022selfishuptakeversus pages 1-2) | Strong; directly characterized in Ruminiclostridium cellulolyticum. |
| HTCS | positively_regulates | Xylan PUL expression | 10.1007/s00253-023-12977-4 | “HTCS have been characterized for regulating xylanase genes” (novak2024currentmodelsin pages 1-2) | Strong at class level; exact regulons are taxon-specific. |
| XlnR/Xyr1 | positively_regulates | xylanase gene expression | 10.1007/s00253-023-12680-4 | “XlnR… regulates both xylanolytic and endoglucanase gene expression” (kerkaert2023regulationofnutrient pages 36-38) | Strong in filamentous fungi. |
| CCR/CcpA | negatively_regulates | xylan utilization genes | 10.1007/s00253-023-12977-4 | “In Gram-positive bacteria, this repression is controlled by the CcpA protein” (novak2024currentmodelsin pages 2-4) | Strong for preferred-carbon repression; applies broadly but with taxon-specific implementation. |
| D-Xylose | is_converted_by | Xylose isomerase (XylA) to D-Xylulose | 10.1186/s13068-023-02266-7 | “The isomerase pathway… converts d-xylose to d-xylulose” (liu2023theweimbergpathway pages 1-3) | Strong. |
| D-Xylulose | is_converted_by | Xylulokinase (XylB) to D-Xylulose-5-phosphate | 10.4014/jmb.2504.04021 | “xylB gene encoding xylulokinase (EC 2.7.1.17)” and xylA encodes xylose isomerase (park2025xylosemetabolismand pages 2-3) | Strong when combined with standard pathway knowledge from same source set; xylB product identity explicit. |
| D-Xylulose-5-phosphate | enters | Pentose phosphate pathway | 10.1186/s13068-023-02266-7 | “This product enters central metabolism through the pentose phosphate pathway (PPP)” (liu2023theweimbergpathway pages 1-3) | Strong. |
| Cellulosome | contains | Endo-1,4-β-xylanase | 10.3389/fmicb.2025.1638551 | “These include endo-β-1,4-xylanases… within cellulosomes” (lindic2025structuralandfunctional pages 9-10) | Moderate; direct for cellulosome-associated xylanases, but dockerin mediation is inferred from cellulosome organization. |
| Xylan | induces_expression_of | Endo-1,4-β-xylanase | 10.1073/pnas.1406156111 | “These genes are highly upregulated when bacteria are grown on xylan” (zhang2014xylanutilizationin pages 6-7) | Strong for xylan-inducible systems in gut Bacteroidetes. |
| Accessory enzymes | synergize_with | Endo-1,4-β-xylanase | 10.1016/0141-0229(93)90078-g | “Complete xylan degradation requires synergistic action of these enzymes to remove substituents from the polymer” (christov1993esterasesofxylandegrading pages 1-2) | Strong conceptually; broad mechanistic claim. |
| Acetyl xylan esterase | facilitates | Endo-1,4-β-xylanase | 10.3389/fmicb.2025.1638551 | “carbohydrate esterases… remove substituents that obstruct enzymatic hydrolysis” (lindic2025structuralandfunctional pages 9-10) | Moderate; facilitation is mechanistically well supported though often not tested as a direct binary edge. |
| σI6/σI7 | positively_regulates | cellulosomal xylanase genes | 10.1007/s00253-023-12977-4 | “xylanase-encoding genes are regulated by alternative sigma factors (σI6 and σI7)… enabling stronger expression in the presence of xylans” (novak2024currentmodelsin pages 4-5) | Strong but taxon-specific to Clostridium thermocellum-like systems. |
| D-Xylose | is_converted_by | Weimberg pathway to α-Ketoglutarate | 10.1186/s13068-023-02266-7 | “The Weimberg pathway… branches to produce α-ketoglutarate” (liu2023theweimbergpathway pages 1-3) | Strong for non-phosphorylative xylose users; should be curated as alternative/taxon-restricted, not universal. |


*Table: This table summarizes evidence-backed subject-predicate-object triples for a microbial xylan degradation causal graph, spanning hydrolysis, transport, regulation, and downstream xylose metabolism. It is useful for curating TraitMech edges while highlighting confidence and taxon-specific boundaries.*

### Highlights on Edge Confidence

- **Strong edges** (suitable for immediate curation): The core hydrolysis edges (xylanase → hydrolyzes → xylan; β-xylosidase → hydrolyzes → XOS to xylose) are supported by decades of enzymology and recently confirmed enzymatic product profiling (christov1993esterasesofxylandegrading pages 1-2, leschonski2024structuredependentstimulationof pages 2-4).
- **Strong regulatory edges**: HTCS-mediated PUL regulation is well established across Bacteroidetes (novak2024currentmodelsin pages 1-2, panwar2025transcriptionaldelineationof pages 5-7, zhang2014xylanutilizationin pages 6-7). CCR via CcpA in Gram-positive and cAMP-CRP in Gram-negative bacteria is broadly documented (novak2024currentmodelsin pages 2-4).
- **Moderate/taxon-specific edges**: The cellulosome-xylanase containment edge and the σI6/σI7 regulatory edge are specific to Clostridium-type anaerobes (novak2024currentmodelsin pages 4-5, lindic2025structuralandfunctional pages 9-10). The Weimberg pathway edge is limited to specific fungi and bacteria capable of non-phosphorylative xylose catabolism (liu2023theweimbergpathway pages 1-3). These should be curated with taxonomic qualifiers.
- **Synergy/facilitation edges**: The edge "acetyl xylan esterase facilitates endo-xylanase" is mechanistically well supported — removal of acetyl groups that sterically block xylanase access — but is often inferred rather than directly demonstrated via pairwise assays (christov1993esterasesofxylandegrading pages 1-2, lindic2025structuralandfunctional pages 9-10).

---

## 4. Existing Causal Graph Expansion Recommendations

The existing graph `xylan_degradation_xylanase` contains 8 nodes and 5 edges. Based on this curation report, the expanded graph should incorporate:

1. **Debranching and esterase enzymes** as distinct nodes (α-L-arabinofuranosidase, α-glucuronidase, acetyl xylan esterase, feruloyl esterase) with synergy edges to the backbone-cleaving xylanase (christov1993esterasesofxylandegrading pages 1-2, lindic2025structuralandfunctional pages 9-10).
2. **Transport systems** as nodes (SusC/SusD, ABC transporter, TonB-dependent transporter), connected to oligosaccharide intermediates (XOS, AXOS) via import edges (liu2022selfishuptakeversus pages 9-12, zhang2014xylanutilizationin pages 2-2).
3. **Regulatory nodes** (HTCS, CCR/CcpA, XlnR/Xyr1) with positive/negative regulation edges to enzyme expression nodes (novak2024currentmodelsin pages 1-2, novak2024currentmodelsin pages 2-4, kerkaert2023regulationofnutrient pages 5-6).
4. **Downstream metabolism nodes** (xylose isomerase/XylA, xylulokinase/XylB, pentose phosphate pathway) connecting D-xylose to central carbon metabolism (liu2023theweimbergpathway pages 1-3, park2025xylosemetabolismand pages 2-3).
5. **Chemical product nodes** (D-xylose, L-arabinose, acetic acid, ferulic acid) as outputs of the respective enzymatic reactions (liu2022selfishuptakeversus pages 9-12, liu2024intracellularremovalof pages 1-2).

---

## 5. DOI-First Bibliography

| DOI | Authors (short) | Year | Title (abbreviated) | Journal | Key Contribution |
|---|---|---:|---|---|---|
| 10.1016/0141-0229(93)90078-g | Christov & Prior | 1993 | Esterases of xylan-degrading microorganisms | Enzyme and Microbial Technology | Foundational review defining the core enzymatic toolkit for xylan breakdown, including endo-xylanase, β-xylosidase, arabinofuranosidase, α-glucuronidase, and esterases acting synergistically on substituted xylans. (christov1993esterasesofxylandegrading pages 1-2, christov1993esterasesofxylandegrading pages 6-7) |
| 10.1073/pnas.1406156111 | Zhang et al. | 2014 | Xylan utilization in human gut commensals | PNAS | Described the Bacteroidetes xylan utilization system (XUS), including PUL organization, SusC/SusD-like transport, HTCS-linked regulation, GH10/GH43-rich architecture, and xylan-induced expression. (zhang2014xylanutilizationin pages 2-2, zhang2014xylanutilizationin pages 6-7, zhang2014xylanutilizationin pages 2-3) |
| 10.1186/s13068-022-02225-8 | Liu et al. | 2022 | Selfish uptake versus extracellular AX degradation | Biotechnology for Biofuels and Bioproducts | Established the Xua system in Ruminiclostridium cellulolyticum as an ABC transporter-based intracellular arabinoxylodextrin uptake pathway complementing extracellular degradation. (liu2022selfishuptakeversus pages 9-12, liu2022selfishuptakeversus pages 1-2, liu2022selfishuptakeversus pages 2-4, liu2022selfishuptakeversus pages 6-9) |
| 10.1186/s12934-024-02423-z | Liu et al. | 2024 | Intracellular removal of acyl decorations on AXOS | Microbial Cell Factories | Characterized intracellular esterases XuaH and XuaJ, showing removal of feruloyl, p-coumaroyl, and acetyl decorations from imported AXOS in the Xua pathway. (liu2024intracellularremovalof pages 1-2) |
| 10.1080/19490976.2024.2430419 | Leschonski et al. | 2024 | AXOS structure-dependent stimulation of gut bacteria | Gut Microbes | Recent review summarizing AX/AXOS structures, GH family and EC classification of xylan-degrading enzymes, and product specificities of GH10/GH11/GH30 endoxylanases. (leschonski2024structuredependentstimulationof pages 2-4, leschonski2024structuredependentstimulationof pages 28-29) |
| 10.1007/s00253-023-12977-4 | Novak & Gardner | 2024 | Bacterial hemicellulase gene regulation | Applied Microbiology and Biotechnology | Current overview of bacterial regulation of xylan/hemicellulase genes, highlighting HTCS, ECF-σ/anti-σ systems, carbon catabolite repression, AraR/XylR, and sigma-factor control. (novak2024currentmodelsin pages 12-13, novak2024currentmodelsin pages 1-2, novak2024currentmodelsin pages 4-5, novak2024currentmodelsin pages 2-4, novak2024currentmodelsin pages 15-16, novak2024currentmodelsin pages 11-12) |
| 10.1007/s00253-023-12680-4 | Kerkaert & Huberman | 2023 | Regulation of nutrient utilization in filamentous fungi | Applied Microbiology and Biotechnology | Summarized fungal nutrient regulation with emphasis on XlnR/Xyr1 as a Zn2Cys6 transcription factor controlling xylanolytic and pentose-responsive gene expression. (kerkaert2023regulationofnutrient pages 36-38, kerkaert2023regulationofnutrient pages 5-6) |
| 10.1128/aem.01759-24 | Panwar et al. | 2025 | Transcriptional delineation of PULs in Segatella copri | Applied and Environmental Microbiology | Mapped xylan-responsive PULs in Segatella copri, including SusC/SusD pairs, GH10, GH43_1, carbohydrate esterase, MFS transporter, and HTCS regulators. (panwar2025transcriptionaldelineationof pages 5-7) |
| 10.3389/fmicb.2025.1638551 | Lindič & Vodovnik | 2025 | Structural and functional insights into cellulosomes | Frontiers in Microbiology | Reviewed cellulosomal hemicellulases, showing how endoxylanases, β-xylosidases, arabinofuranosidases, α-glucuronidases, and esterases are organized in synergistic multienzyme complexes. (lindic2025structuralandfunctional pages 9-10) |
| 10.1186/s13068-023-02266-7 | Liu et al. | 2023 | Weimberg pathway in Myceliophthora thermophila | Biotechnology for Biofuels and Bioproducts | Demonstrated the Weimberg pathway as a non-phosphorylative alternative for xylose utilization, converting xylose toward α-ketoglutarate. (liu2023theweimbergpathway pages 1-3) |
| 10.1038/s41467-024-46812-9 | Dvořák et al. | 2024 | Adaptation of Pseudomonas putida to D-xylose | Nature Communications | Quantified central metabolic flux during xylose utilization, showing major routing through xylulose-5-phosphate and the pentose phosphate pathway in an engineered bacterium. (dvorak2024syntheticallyprimedadaptationof pages 3-4, dvorak2024syntheticallyprimedadaptationof pages 5-6) |
| 10.4014/jmb.2504.04021 | Park | 2025 | Xylose metabolism and transport in Bacillus subtilis | Journal of Microbiology and Biotechnology | Reviewed the xylose operon in B. subtilis, including xylA (xylose isomerase) and xylB (xylulokinase), relevant for downstream assimilation of xylan-derived xylose. (park2025xylosemetabolismand pages 2-3) |
| 10.1093/ismejo/wraf022 | Martin et al. | 2025 | Metabolism of hemicelluloses by root-associated Bacteroidota | The ISME Journal | Showed that plant-associated Bacteroidota rely heavily on TonB-dependent transporters and SusD-like proteins in PUL-linked complex glycan acquisition. (martin2025metabolismofhemicelluloses pages 3-5) |
| 10.1111/j.1757-1707.2009.01004.x | Dodd & Cann | 2009 | Enzymatic deconstruction of xylan for biofuel production | GCB Bioenergy | Foundational xylan deconstruction review widely used for trait definition and mechanistic framing of xylanase plus accessory-enzyme synergy in biomass conversion. (christov1993esterasesofxylandegrading pages 1-2, zhang2014xylanutilizationin pages 1-2) |
| 10.1016/j.cbpa.2015.10.018 | Cragg et al. | 2015 | Lignocellulose degradation across organisms | Current Opinion in Chemical Biology | Broad comparative review situating xylan degradation within larger lignocellulose decomposition strategies across bacteria, fungi, and other organisms. (lindic2025structuralandfunctional pages 9-10) |


*Table: This table compiles the key literature supporting curation of the microbial xylan degradation trait. It is organized DOI-first and highlights each source's main mechanistic contribution to enzymes, transport, regulation, and downstream metabolism.*

---

## 6. Warnings and Curation Caveats

1. **Xyloglucan vs. xylan distinction**: Several studies (e.g., Grondin et al. 2022, Martin et al. 2025) describe xyloglucan utilization loci that share GH family members with xylan PULs but target a distinct substrate (xyloglucan). These should NOT be curated under the xylan degradation trait.

2. **Taxon-specific regulatory models**: The HTCS/PUL regulatory model is specific to Bacteroidetes; the σI6/σI7 model is specific to cellulosome-producing clostridia; the XlnR/Xyr1 model is specific to filamentous fungi. These should be flagged with taxonomic scope qualifiers if added to a universal causal graph.

3. **Weimberg pathway**: The non-phosphorylative Weimberg pathway for xylose catabolism (xylose → xylonate → 2-keto-3-deoxy-xylonate → α-ketoglutarate) is an alternative to the canonical isomerase pathway and is currently documented in limited taxa (liu2023theweimbergpathway pages 1-3). It should be curated as a taxon-restricted alternative.

4. **CE family assignments**: Carbohydrate esterase families (CE1, CE3, CE4, CE6, CE7, CE12) show overlapping activity profiles (acetyl xylan esterase vs. feruloyl esterase). CE1 enzymes, for example, can have both acetyl xylan esterase and feruloyl esterase activity. Edges involving specific CE families should note this ambiguity.

5. **Cellulosome-associated xylanases**: While cellulosomes contain xylanases (e.g., Xyn10C, Xyn11D, Xyn10Z in C. thermocellum), the dockerin-cohesin specificity varies, and not all cellulosome-producing organisms degrade xylan equivalently (lindic2025structuralandfunctional pages 9-10). These edges should be annotated as applicable to cellulosome-producing anaerobes only.

6. **Product profile variability**: The specific oligosaccharide products of endoxylanase action depend heavily on both the GH family and the xylan structural variant (arabinoxylan vs. glucuronoxylan vs. unsubstituted xylan) (leschonski2024structuredependentstimulationof pages 2-4). Edges specifying product types should note this substrate dependency.

7. **Prevotella/Segatella copri reclassification**: Prevotella copri DSM18205 has been reclassified to Segatella copri. PUL annotations from this organism should use the current nomenclature (panwar2025transcriptionaldelineationof pages 5-7).


References

1. (christov1993esterasesofxylandegrading pages 1-2): Lyudmil Pavlov Christov and Bernard Alexander Prior. Esterases of xylan-degrading microorganisms: production, properties, and significance. Enzyme and microbial technology, 15 6:460-75, Jun 1993. URL: https://doi.org/10.1016/0141-0229(93)90078-g, doi:10.1016/0141-0229(93)90078-g. This article has 244 citations and is from a peer-reviewed journal.

2. (leschonski2024structuredependentstimulationof pages 2-4): Kai P. Leschonski, Martin S. Mortensen, Lea B.S. Hansen, Kristian B.R.M. Krogh, Mirjam A. Kabel, and Martin F. Laursen. Structure-dependent stimulation of gut bacteria by arabinoxylo-oligosaccharides (axos): a review. Gut Microbes, Nov 2024. URL: https://doi.org/10.1080/19490976.2024.2430419, doi:10.1080/19490976.2024.2430419. This article has 27 citations and is from a peer-reviewed journal.

3. (liu2024intracellularremovalof pages 1-2): Nian Liu, Elise Odinot, Hélène David, Nicolas Vita, Felipe Mejia Otalvaro, Goetz Parsiegla, Yann Denis, Craig Faulds, Henri-Pierre Fierobe, and Stéphanie Perret. Intracellular removal of acetyl, feruloyl and p-coumaroyl decorations on arabinoxylo-oligosaccharides imported from lignocellulosic biomass degradation by ruminiclostridium cellulolyticum. Microbial Cell Factories, May 2024. URL: https://doi.org/10.1186/s12934-024-02423-z, doi:10.1186/s12934-024-02423-z. This article has 6 citations and is from a peer-reviewed journal.

4. (lindic2025structuralandfunctional pages 9-10): Nataša Lindič and Maša Vodovnik. Structural and functional insights into cellulosomes: masters of plant cell wall degradation. Frontiers in Microbiology, Sep 2025. URL: https://doi.org/10.3389/fmicb.2025.1638551, doi:10.3389/fmicb.2025.1638551. This article has 6 citations and is from a peer-reviewed journal.

5. (liu2022selfishuptakeversus pages 1-2): Nian Liu, Séverine Gagnot, Yann Denis, Deborah Byrne, Craig Faulds, Henri-Pierre Fierobe, and Stéphanie Perret. Selfish uptake versus extracellular arabinoxylan degradation in the primary degrader ruminiclostridium cellulolyticum, a new string to its bow. Biotechnology for Biofuels and Bioproducts, Nov 2022. URL: https://doi.org/10.1186/s13068-022-02225-8, doi:10.1186/s13068-022-02225-8. This article has 20 citations and is from a domain leading peer-reviewed journal.

6. (liu2022selfishuptakeversus pages 9-12): Nian Liu, Séverine Gagnot, Yann Denis, Deborah Byrne, Craig Faulds, Henri-Pierre Fierobe, and Stéphanie Perret. Selfish uptake versus extracellular arabinoxylan degradation in the primary degrader ruminiclostridium cellulolyticum, a new string to its bow. Biotechnology for Biofuels and Bioproducts, Nov 2022. URL: https://doi.org/10.1186/s13068-022-02225-8, doi:10.1186/s13068-022-02225-8. This article has 20 citations and is from a domain leading peer-reviewed journal.

7. (liu2023theweimbergpathway pages 1-3): Defei Liu, Yongli Zhang, Jingen Li, Wenliang Sun, Yonghong Yao, and Chaoguang Tian. The weimberg pathway: an alternative for myceliophthora thermophila to utilize d-xylose. Biotechnology for Biofuels and Bioproducts, Jan 2023. URL: https://doi.org/10.1186/s13068-023-02266-7, doi:10.1186/s13068-023-02266-7. This article has 13 citations and is from a domain leading peer-reviewed journal.

8. (liu2022selfishuptakeversus pages 6-9): Nian Liu, Séverine Gagnot, Yann Denis, Deborah Byrne, Craig Faulds, Henri-Pierre Fierobe, and Stéphanie Perret. Selfish uptake versus extracellular arabinoxylan degradation in the primary degrader ruminiclostridium cellulolyticum, a new string to its bow. Biotechnology for Biofuels and Bioproducts, Nov 2022. URL: https://doi.org/10.1186/s13068-022-02225-8, doi:10.1186/s13068-022-02225-8. This article has 20 citations and is from a domain leading peer-reviewed journal.

9. (park2025xylosemetabolismand pages 2-3): Yong-Cheol Park. Xylose metabolism and transport in bacillus subtilis and its application to d-ribose production. Journal of Microbiology and Biotechnology, Apr 2025. URL: https://doi.org/10.4014/jmb.2504.04021, doi:10.4014/jmb.2504.04021. This article has 8 citations and is from a peer-reviewed journal.

10. (panwar2025transcriptionaldelineationof pages 5-7): Deepesh Panwar, Jonathon Briggs, Alexander S. C. Fraser, William A. Stewart, and Harry Brumer. Transcriptional delineation of polysaccharide utilization loci in the human gut commensal <i>segatella copri</i> dsm18205 and co-culture with exemplar <i>bacteroides</i> species on dietary plant glycans. Jan 2025. URL: https://doi.org/10.1128/aem.01759-24, doi:10.1128/aem.01759-24. This article has 11 citations and is from a peer-reviewed journal.

11. (zhang2014xylanutilizationin pages 6-7): Meiling Zhang, Jonathan R. Chekan, Dylan Dodd, Pei-Ying Hong, Lauren Radlinski, Vanessa Revindran, Satish K. Nair, Roderick I. Mackie, and Isaac Cann. Xylan utilization in human gut commensal bacteria is orchestrated by unique modular organization of polysaccharide-degrading enzymes. Proceedings of the National Academy of Sciences, 111:E3708-E3717, Aug 2014. URL: https://doi.org/10.1073/pnas.1406156111, doi:10.1073/pnas.1406156111. This article has 213 citations and is from a highest quality peer-reviewed journal.

12. (liu2022selfishuptakeversus pages 2-4): Nian Liu, Séverine Gagnot, Yann Denis, Deborah Byrne, Craig Faulds, Henri-Pierre Fierobe, and Stéphanie Perret. Selfish uptake versus extracellular arabinoxylan degradation in the primary degrader ruminiclostridium cellulolyticum, a new string to its bow. Biotechnology for Biofuels and Bioproducts, Nov 2022. URL: https://doi.org/10.1186/s13068-022-02225-8, doi:10.1186/s13068-022-02225-8. This article has 20 citations and is from a domain leading peer-reviewed journal.

13. (martin2025metabolismofhemicelluloses pages 3-5): Hannah Martin, Lucy A Rogers, Laila Moushtaq, Amanda A Brindley, Polly Forbes, Amy R Quintion, Andrew R J Murphy, Helen Hipperson, Tim J Daniell, Didier Ndeh, Sam Amsbury, Andrew Hitchcock, and Ian D E A Lidbury. Metabolism of hemicelluloses by root-associated <i>bacteroidota</i> species. The ISME Journal, Feb 2025. URL: https://doi.org/10.1093/ismejo/wraf022, doi:10.1093/ismejo/wraf022. This article has 33 citations.

14. (zhang2014xylanutilizationin pages 2-2): Meiling Zhang, Jonathan R. Chekan, Dylan Dodd, Pei-Ying Hong, Lauren Radlinski, Vanessa Revindran, Satish K. Nair, Roderick I. Mackie, and Isaac Cann. Xylan utilization in human gut commensal bacteria is orchestrated by unique modular organization of polysaccharide-degrading enzymes. Proceedings of the National Academy of Sciences, 111:E3708-E3717, Aug 2014. URL: https://doi.org/10.1073/pnas.1406156111, doi:10.1073/pnas.1406156111. This article has 213 citations and is from a highest quality peer-reviewed journal.

15. (novak2024currentmodelsin pages 1-2): Jessica K. Novak and Jeffrey G. Gardner. Current models in bacterial hemicellulase-encoding gene regulation. Applied Microbiology and Biotechnology, Jan 2024. URL: https://doi.org/10.1007/s00253-023-12977-4, doi:10.1007/s00253-023-12977-4. This article has 8 citations and is from a domain leading peer-reviewed journal.

16. (novak2024currentmodelsin pages 4-5): Jessica K. Novak and Jeffrey G. Gardner. Current models in bacterial hemicellulase-encoding gene regulation. Applied Microbiology and Biotechnology, Jan 2024. URL: https://doi.org/10.1007/s00253-023-12977-4, doi:10.1007/s00253-023-12977-4. This article has 8 citations and is from a domain leading peer-reviewed journal.

17. (kerkaert2023regulationofnutrient pages 36-38): Joshua D. Kerkaert and Lori B. Huberman. Regulation of nutrient utilization in filamentous fungi. Applied Microbiology and Biotechnology, 107:5873-5898, Aug 2023. URL: https://doi.org/10.1007/s00253-023-12680-4, doi:10.1007/s00253-023-12680-4. This article has 32 citations and is from a domain leading peer-reviewed journal.

18. (kerkaert2023regulationofnutrient pages 5-6): Joshua D. Kerkaert and Lori B. Huberman. Regulation of nutrient utilization in filamentous fungi. Applied Microbiology and Biotechnology, 107:5873-5898, Aug 2023. URL: https://doi.org/10.1007/s00253-023-12680-4, doi:10.1007/s00253-023-12680-4. This article has 32 citations and is from a domain leading peer-reviewed journal.

19. (novak2024currentmodelsin pages 2-4): Jessica K. Novak and Jeffrey G. Gardner. Current models in bacterial hemicellulase-encoding gene regulation. Applied Microbiology and Biotechnology, Jan 2024. URL: https://doi.org/10.1007/s00253-023-12977-4, doi:10.1007/s00253-023-12977-4. This article has 8 citations and is from a domain leading peer-reviewed journal.

20. (novak2024currentmodelsin pages 15-16): Jessica K. Novak and Jeffrey G. Gardner. Current models in bacterial hemicellulase-encoding gene regulation. Applied Microbiology and Biotechnology, Jan 2024. URL: https://doi.org/10.1007/s00253-023-12977-4, doi:10.1007/s00253-023-12977-4. This article has 8 citations and is from a domain leading peer-reviewed journal.

21. (dvorak2024syntheticallyprimedadaptationof pages 3-4): Pavel Dvořák, Barbora Burýšková, Barbora Popelářová, Birgitta Elisabeth Ebert, Tibor Botka, Dalimil Bujdoš, Alberto Sánchez-Pascuala, Hannah Schöttler, Heiko Hayen, Víctor de Lorenzo, Lars M. Blank, and Martin Benešík. Synthetically-primed adaptation of pseudomonas putida to a non-native substrate d-xylose. Nature Communications, Mar 2024. URL: https://doi.org/10.1038/s41467-024-46812-9, doi:10.1038/s41467-024-46812-9. This article has 36 citations and is from a highest quality peer-reviewed journal.

22. (christov1993esterasesofxylandegrading pages 6-7): Lyudmil Pavlov Christov and Bernard Alexander Prior. Esterases of xylan-degrading microorganisms: production, properties, and significance. Enzyme and microbial technology, 15 6:460-75, Jun 1993. URL: https://doi.org/10.1016/0141-0229(93)90078-g, doi:10.1016/0141-0229(93)90078-g. This article has 244 citations and is from a peer-reviewed journal.

23. (zhang2014xylanutilizationin pages 2-3): Meiling Zhang, Jonathan R. Chekan, Dylan Dodd, Pei-Ying Hong, Lauren Radlinski, Vanessa Revindran, Satish K. Nair, Roderick I. Mackie, and Isaac Cann. Xylan utilization in human gut commensal bacteria is orchestrated by unique modular organization of polysaccharide-degrading enzymes. Proceedings of the National Academy of Sciences, 111:E3708-E3717, Aug 2014. URL: https://doi.org/10.1073/pnas.1406156111, doi:10.1073/pnas.1406156111. This article has 213 citations and is from a highest quality peer-reviewed journal.

24. (leschonski2024structuredependentstimulationof pages 28-29): Kai P. Leschonski, Martin S. Mortensen, Lea B.S. Hansen, Kristian B.R.M. Krogh, Mirjam A. Kabel, and Martin F. Laursen. Structure-dependent stimulation of gut bacteria by arabinoxylo-oligosaccharides (axos): a review. Gut Microbes, Nov 2024. URL: https://doi.org/10.1080/19490976.2024.2430419, doi:10.1080/19490976.2024.2430419. This article has 27 citations and is from a peer-reviewed journal.

25. (novak2024currentmodelsin pages 12-13): Jessica K. Novak and Jeffrey G. Gardner. Current models in bacterial hemicellulase-encoding gene regulation. Applied Microbiology and Biotechnology, Jan 2024. URL: https://doi.org/10.1007/s00253-023-12977-4, doi:10.1007/s00253-023-12977-4. This article has 8 citations and is from a domain leading peer-reviewed journal.

26. (novak2024currentmodelsin pages 11-12): Jessica K. Novak and Jeffrey G. Gardner. Current models in bacterial hemicellulase-encoding gene regulation. Applied Microbiology and Biotechnology, Jan 2024. URL: https://doi.org/10.1007/s00253-023-12977-4, doi:10.1007/s00253-023-12977-4. This article has 8 citations and is from a domain leading peer-reviewed journal.

27. (dvorak2024syntheticallyprimedadaptationof pages 5-6): Pavel Dvořák, Barbora Burýšková, Barbora Popelářová, Birgitta Elisabeth Ebert, Tibor Botka, Dalimil Bujdoš, Alberto Sánchez-Pascuala, Hannah Schöttler, Heiko Hayen, Víctor de Lorenzo, Lars M. Blank, and Martin Benešík. Synthetically-primed adaptation of pseudomonas putida to a non-native substrate d-xylose. Nature Communications, Mar 2024. URL: https://doi.org/10.1038/s41467-024-46812-9, doi:10.1038/s41467-024-46812-9. This article has 36 citations and is from a highest quality peer-reviewed journal.

28. (zhang2014xylanutilizationin pages 1-2): Meiling Zhang, Jonathan R. Chekan, Dylan Dodd, Pei-Ying Hong, Lauren Radlinski, Vanessa Revindran, Satish K. Nair, Roderick I. Mackie, and Isaac Cann. Xylan utilization in human gut commensal bacteria is orchestrated by unique modular organization of polysaccharide-degrading enzymes. Proceedings of the National Academy of Sciences, 111:E3708-E3717, Aug 2014. URL: https://doi.org/10.1073/pnas.1406156111, doi:10.1073/pnas.1406156111. This article has 213 citations and is from a highest quality peer-reviewed journal.