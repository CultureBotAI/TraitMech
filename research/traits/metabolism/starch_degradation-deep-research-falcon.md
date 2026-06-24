---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T05:54:12.798224'
end_time: '2026-06-18T06:09:33.144987'
duration_seconds: 920.35
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: starch degradation
  trait_identifier: traitmech:000115
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: starch_degradation
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A biopolymer-degradation metabolism in which an organism hydrolyzes
    starch (amylose and amylopectin) to maltooligosaccharides and glucose using amylases
    and related glycoside hydrolases.
  parent_traits: traitmech:000110
  synonyms: amylolytic
  evidence_summary: 'DOI:10.1016/S0168-1656(01)00407-2:  (van der Maarel et al. review
    starch-converting enzymes of the alpha-amylase family that hydrolyze starch to
    oligosaccharides and glucose.) | DOI:10.1093/nar/gkt1178:  (The CAZy database
    review classifies the glycoside hydrolases (including amylases) that microorganisms
    use to degrade starch and other polysaccharides.)'
  causal_graph_summary: 'starch_degradation_amylase: 3 nodes, 2 edges'
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
- **Trait label:** starch degradation
- **METPO identifier:** traitmech:000115
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biopolymer-degradation metabolism in which an organism hydrolyzes starch (amylose and amylopectin) to maltooligosaccharides and glucose using amylases and related glycoside hydrolases.
- **Parent traits:** traitmech:000110
- **Synonyms:** amylolytic
- **Existing evidence:** DOI:10.1016/S0168-1656(01)00407-2:  (van der Maarel et al. review starch-converting enzymes of the alpha-amylase family that hydrolyze starch to oligosaccharides and glucose.) | DOI:10.1093/nar/gkt1178:  (The CAZy database review classifies the glycoside hydrolases (including amylases) that microorganisms use to degrade starch and other polysaccharides.)
- **Existing causal graph summary:** starch_degradation_amylase: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **starch degradation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/starch_degradation.yaml`.

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
- **Trait label:** starch degradation
- **METPO identifier:** traitmech:000115
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A biopolymer-degradation metabolism in which an organism hydrolyzes starch (amylose and amylopectin) to maltooligosaccharides and glucose using amylases and related glycoside hydrolases.
- **Parent traits:** traitmech:000110
- **Synonyms:** amylolytic
- **Existing evidence:** DOI:10.1016/S0168-1656(01)00407-2:  (van der Maarel et al. review starch-converting enzymes of the alpha-amylase family that hydrolyze starch to oligosaccharides and glucose.) | DOI:10.1093/nar/gkt1178:  (The CAZy database review classifies the glycoside hydrolases (including amylases) that microorganisms use to degrade starch and other polysaccharides.)
- **Existing causal graph summary:** starch_degradation_amylase: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **starch degradation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/starch_degradation.yaml`.

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


## Research Report: Microbial TraitMech Causal Graph — **Starch degradation** (traitmech:000115)

### 1) Scope summary (curation-focused)
**Trait definition (operational):** microbial capacity to depolymerize **starch (amylose + amylopectin)** into **maltooligosaccharides and glucose** using **α-amylases and related glycoside hydrolases**, typically coupled to uptake of oligosaccharides and intracellular catabolism. Mechanistic descriptions explicitly define starch as a glucose α-glucan with an α-1,4 backbone (amylose) and α-1,6 branching (amylopectin). (brown2024acarboseimpairsgut pages 3-5)

**What is in-scope for traitmech:000115:**
- Enzymatic hydrolysis of starch to maltooligosaccharides (MOS)/maltodextrin and onward to glucose, including debranching/terminal steps (e.g., pullulanases, α-glucosidases) and oligosaccharide transport. (brown2024acarboseimpairsgut pages 3-5)
- Systems-level starch utilization loci such as the **Bacteroides Sus** archetype (binding, cleavage, import, periplasmic processing, regulation). (brown2024acarboseimpairsgut pages 3-5)
- Resistant starch (RS) breakdown when evidence explicitly ties enzymes/synergy to utilization of RS as a starch physical form. (pickens2024clostridiumbutyricumprazmowski pages 11-13)

**Boundary cases (keep distinct but allow as assay substrates):**
- **Glycogen**: an animal storage α-glucan; often yields similar breakdown products and can be used to probe related enzyme/transport modules, but should not be conflated with starch unless evidence connects it to the same utilization machinery. (brown2024acarboseimpairsgut pages 5-7, bhandari2023transportandutilization pages 1-2)
- **Pullulan**: a fungal α-glucan with repeating α-1,6-linked maltotriose units; useful for debranching/pullulanase activity that is mechanistically relevant to amylopectin branch removal, but is not starch per se. (brown2024acarboseimpairsgut pages 5-7, pickens2024clostridiumbutyricumprazmowski pages 11-13)
- **Cyclodextrins**: starch-derived cyclic oligosaccharides; may be used as “starch mimics” in some assays but are best handled as adjacent substrates. (albright2025developmentofa pages 9-12)

**Assay/readout types that map to this trait:**
- Growth on starch/amylopectin and sensitivity shifts under inhibitors (e.g., Δ lag time to OD600 threshold; substrate-specific inhibitory concentrations). (brown2024acarboseimpairsgut pages 5-7)
- Enzyme activity assays (e.g., amylase IC50 on fluorescent starch; pullulanase activity U/mL). (brown2024acarboseimpairsgut pages 7-9, dong2024extracellularoverexpressionof pages 1-2)
- Product profiling (TLC/HPLC) for MOS/glucose/trehalose in bioprocess contexts. (dong2024extracellularoverexpressionof pages 8-10)

---

### 2) Key concepts and current mechanistic understanding
#### 2.1 The Bacteroides Sus archetype (binding → cleavage → import → periplasmic processing → regulation)
A well-supported mechanistic template for starch degradation is the **starch utilization system (Sus)** in gut Bacteroides. It integrates:
- **Cell-surface binding:** outer-membrane lipoproteins (SusDEF) bind starch. (brown2024acarboseimpairsgut pages 3-5)
- **Initial depolymerization:** an outer-membrane, cell-associated **α-amylase SusG** generates maltooligosaccharides. (brown2024acarboseimpairsgut pages 3-5)
- **Import:** maltooligosaccharides are brought through **TonB-dependent SusC** into the **periplasm**. (brown2024acarboseimpairsgut pages 3-5)
- **Periplasmic hydrolysis:** **SusA (neopullulanase/α-amylase)** and **SusB (α-glucosidase/glucoamylase)** reduce imported oligosaccharides to glucose. (brown2024acarboseimpairsgut pages 3-5)
- **Regulation:** **SusR** senses periplasmic maltose and induces sus gene expression. (brown2024acarboseimpairsgut pages 3-5)

This modular decomposition is directly useful as a cross-taxon *graph pattern* (surface depolymerization + transporter + intracellular/periplasmic finishing steps), while individual proteins should be curated with taxon constraints (e.g., Bacteroides-specific). (brown2024acarboseimpairsgut pages 3-5)

#### 2.2 Enzyme families and functional roles
- **α-amylases (EC 3.2.1.1; often CAZy GH13):** cleave internal α-1,4 linkages to generate MOS/maltodextrin. (brown2024acarboseimpairsgut pages 3-5)
- **Type I pullulanases (EC 3.2.1.41; GH13_14):** debranch α-1,6 linkages; experimentally yield maltotriose from pullulan and can complement α-amylases in processing branched α-glucans. (pickens2024clostridiumbutyricumprazmowski pages 11-13)
- **α-glucosidases/glucoamylases (e.g., EC 3.2.1.20 / 3.2.1.3; GH97/GH31 contexts):** terminal hydrolysis to glucose; in Sus, SusB is a key step. (brown2024acarboseimpairsgut pages 3-5)

---

### 3) Recent developments (prioritizing 2023–2024)
#### 3.1 Drug–microbiome mechanistic interference with starch degradation (acarbose; montbretin A)
Brown et al. (2024) show that acarbose impacts Bacteroides starch utilization at multiple points (not only extracellular amylases), including periplasmic enzymes and even transport/regulatory processes: acarbose “competes for transport through the TonB-dependent SusC proteins and binds to the Sus transcriptional regulators,” while also targeting periplasmic GH97 enzymes. (brown2024acarboseimpairsgut pages 1-3)

**Quantitative inhibitor phenotype (growth):** substrate-dependent inhibitory concentrations demonstrate that larger/complex α-glucans can be much more sensitive to acarbose than small sugars, and that sensitivity differs between closely related species (Bo vs Bt). For example, inhibitory concentrations (as defined in the study) include: Bo amylopectin 125 µM vs Bt 37.5 µM; Bo pullulan 125 µM vs Bt 50 µM; Bo glycogen >250 µM vs Bt 50 µM. (brown2024acarboseimpairsgut pages 5-7)

**Quantitative enzyme inhibition:** acarbose inhibits outer-membrane amylases with markedly different IC50 values: **BoSusG IC50 = 2.2 ± 0.35 µM** vs **SusG IC50 = 68.2 ± 13.8 µM**. (brown2024acarboseimpairsgut pages 7-9)

Lui et al. (2023) provide a complementary high-throughput community method using fluorescent maltodextrin labeling and show that acarbose inhibited maltodextrin metabolism in **four gut species**, while **montbretin A** slowed growth of **only one** species, consistent with MbA being more selective. (lui2023characterizingtheeffect pages 1-2)

#### 3.2 Strain-variable starch degradation in Bifidobacterium pseudocatenulatum
Sanchez-Gallardo et al. (2024) found that starch utilization can be **strain-specific**: only **8 of 21** B. pseudocatenulatum isolates used starch, and they identified **three distinct extracellular α-amylases** implicated in this phenotype. (sanchezgallardo2024unveilingmetabolicpathways pages 3-6)

#### 3.3 Resistant starch (RS) utilization by a butyrate-producing probiotic candidate
Pickens & Cockburn (2024) demonstrate that **Clostridium butyricum** can “degrade and utilize resistant starch via a set of synergistically acting enzymes,” with combinations achieving **≥2× activity** compared with the best single enzyme (source-dependent). (pickens2024clostridiumbutyricumprazmowski pages 11-13)

---

### 4) Current applications and real-world implementations
#### 4.1 Industrial enzyme production and bioconversion (pullulanase → trehalose)
Dong et al. (2024) provide an industrially oriented implementation: engineered **Bacillus subtilis** strains were constructed for high extracellular production of a neutral pullulanase variant (PulA3E). In a 5 L bioreactor scale-up, extracellular pullulanase activity reached **2465.1 U/mL at 78 h**. (dong2024extracellularoverexpressionof pages 8-10)

In an enzymatic trehalose production system using **200 g/L maltodextrin**, adding PulA3E at **40 U/g maltodextrin** achieved **166 g/L trehalose** with **83% substrate conversion**. (dong2024extracellularoverexpressionof pages 8-10)

This provides a concrete “starch/maltodextrin degradation → value-added product” deployment pathway; it is relevant to TraitMech insofar as it demonstrates scalable conversion chemistry driven by starch-debranching enzymes. (dong2024extracellularoverexpressionof pages 8-10)

#### 4.2 Microbiome profiling and precision interventions
The fluorescent maltodextrin labeling + FACS + 16S workflow in Lui et al. (2023) is a practical approach to identify maltodextrin consumers and drug-perturbed taxa in complex communities, supporting real-world applications in microbiome–diet–drug interaction mapping. (lui2023characterizingtheeffect pages 3-5)

---

### 5) Expert opinions / authoritative interpretations (from sources)
- Brown et al. emphasize **unexpected complexities** in Sus function: even when extracellular enzyme inhibition does not explain whole-cell phenotypes, acarbose can perturb uptake and sensing, implying that *transport/regulatory nodes* are causal bottlenecks in starch utilization beyond hydrolysis alone. (brown2024acarboseimpairsgut pages 1-3)
- Pickens & Cockburn highlight that resistant starch utilization can require **synergistic multi-enzyme sets** and that the most effective combinations depend on starch source/structure, indicating that the “starch degradation” trait should allow edges capturing substrate physical-form dependence and enzyme cooperation rather than a single-enzyme explanation. (pickens2024clostridiumbutyricumprazmowski pages 11-13)

---

### 6) Candidate nodes for TraitMech curation (grouped)
#### 6.1 Pathways / modules
- Sus-like starch utilization module (binding → extracellular hydrolysis → import → periplasmic hydrolysis → regulation). (brown2024acarboseimpairsgut pages 3-5)
- Resistant-starch degradation synergy module (multi-enzyme cooperation). (pickens2024clostridiumbutyricumprazmowski pages 11-13)

#### 6.2 Environmental / experimental factors
- Substrate type: starch, amylopectin, amylose (implied), pullulan, glycogen, resistant starch, maltodextrin, malto-oligosaccharides. (brown2024acarboseimpairsgut pages 3-5, brown2024acarboseimpairsgut pages 5-7, pickens2024clostridiumbutyricumprazmowski pages 11-13)
- Small-molecule inhibitors: acarbose; montbretin A. (brown2024acarboseimpairsgut pages 1-3, lui2023characterizingtheeffect pages 1-2)

#### 6.3 Genes/proteins/enzymes/transporters
- SusG (outer-membrane α-amylase), SusC (TonB-dependent transporter), SusD/E/F (surface binding), SusA (neopullulanase/α-amylase), SusB (α-glucosidase/glucoamylase), SusR (regulator). (brown2024acarboseimpairsgut pages 3-5)
- Gardnerella ABC transporters: **MusEFGK2I**, **MalXFGK** (and operon-linked α-glucosidase/pullulanase). (bhandari2023transportandutilization pages 4-7)
- Resistant starch enzyme set in C. butyricum: GH13_28/GH13_19 α-amylases; GH13_14 pullulanase (Pul13A). (pickens2024clostridiumbutyricumprazmowski pages 11-13)

#### 6.4 Chemicals/metabolites
- Maltooligosaccharides/maltodextrin, maltose, glucose, trehalose. (brown2024acarboseimpairsgut pages 3-5, dong2024extracellularoverexpressionof pages 8-10)

#### 6.5 Localizations
- Outer membrane (surface binding/amylase), periplasm (imported MOS processing), extracellular secretion (industrial pullulanase), cytoplasm (downstream catabolism). (brown2024acarboseimpairsgut pages 3-5, dong2024extracellularoverexpressionof pages 8-10)

---

### 7) Candidate causal edges (curation-ready)
The table below is designed to be transcribed into `data/traits/metabolism/starch_degradation.yaml` after curator selection/normalization.

| Subject (node) | Predicate | Object (node) | Evidence snippet (short quote) | Source (DOI + year + URL) | Notes/uncertainty | Suggested grounding |
|---|---|---|---|---|---|---|
| SusDEF complex | binds | starch | “outer-membrane lipoproteins SusDEF (starch binding)” (brown2024acarboseimpairsgut pages 3-5) | Brown et al. 2024, DOI:10.1128/mbio.01506-24, https://doi.org/10.1128/mbio.01506-24 | Well supported in Bacteroides Sus; taxon-specific archetype | SusD/SusE/SusF label-only; GO:0009279 outer membrane; CHEBI:starch label-only; NCBITaxon:Bacteroides |
| SusG (outer-membrane α-amylase) | hydrolyzes | starch | “SusG is an outer-membrane-associated α-amylase that hydrolyzes the starch into maltooligosaccharides” (brown2024acarboseimpairsgut pages 27-27, albright2025developmentofa pages 9-12) | Brown et al. 2023, DOI:10.1007/s00018-023-04812-w, https://doi.org/10.1007/s00018-023-04812-w | Canonical Bacteroides mechanism; BoGH13A[Sus] is related but distinct | EC:3.2.1.1; GH13; GO:0004556 alpha-amylase activity; CHEBI:starch label-only |
| starch | is hydrolyzed to | maltooligosaccharides | “hydrolyzes the starch into maltooligosaccharides” (brown2024acarboseimpairsgut pages 27-27, lui2023characterizingtheeffect pages 1-2) | Brown et al. 2023, DOI:10.1007/s00018-023-04812-w, https://doi.org/10.1007/s00018-023-04812-w | Trait-level core edge, broad across taxa | CHEBI:starch label-only; maltooligosaccharides label-only |
| SusC (TonB-dependent transporter) | transports | maltooligosaccharides | “maltooligosaccharides are imported via a TonB-dependent SusC into the periplasm” (brown2024acarboseimpairsgut pages 3-5) | Brown et al. 2024, DOI:10.1128/mbio.01506-24, https://doi.org/10.1128/mbio.01506-24 | Strong for Bacteroides Sus; not universal in all bacteria | SusC label-only; TCDB TonB-dependent transporter label-only; GO:0042597 periplasm |
| SusA (periplasmic neopullulanase/α-amylase) | degrades | maltooligosaccharides | “SusA (neo-pullulanase/α-amylase) ... degrade them to glucose” (brown2024acarboseimpairsgut pages 3-5) | Brown et al. 2024, DOI:10.1128/mbio.01506-24, https://doi.org/10.1128/mbio.01506-24 | Periplasmic step in Sus pathway | EC:3.2.1.135 or related GH13 label-only; maltooligosaccharides label-only |
| SusB (periplasmic α-glucosidase/glucoamylase) | produces | glucose | “SusB (α-glucosidase/glucoamylase) degrade them to glucose” (brown2024acarboseimpairsgut pages 3-5, lui2023characterizingtheeffect pages 1-2) | Brown et al. 2024, DOI:10.1128/mbio.01506-24, https://doi.org/10.1128/mbio.01506-24 | Strong in Bacteroides; terminal glucose-release step | EC:3.2.1.20 / EC:3.2.1.3; GH97/GH31 context; CHEBI:glucose label-only |
| SusR | senses | maltose | “SusR senses periplasmic maltose and induces sus transcription” (brown2024acarboseimpairsgut pages 3-5, lui2023characterizingtheeffect pages 1-2) | Brown et al. 2024, DOI:10.1128/mbio.01506-24, https://doi.org/10.1128/mbio.01506-24 | Regulatory edge; Bacteroides-specific locus control | SusR label-only; CHEBI:maltose label-only |
| SusR | positively regulates | sus transcription | “SusR senses periplasmic maltose and induces sus transcription” (brown2024acarboseimpairsgut pages 3-5) | Brown et al. 2024, DOI:10.1128/mbio.01506-24, https://doi.org/10.1128/mbio.01506-24 | Regulatory, likely not curatable as universal trait edge without taxon qualifier | SusR label-only; GO:0006351 transcription, DNA-templated |
| acarbose | inhibits | Bacteroides starch growth | “Bt growth on starch polysaccharides is severely impaired by acarbose” (brown2024acarboseimpairsgut pages 3-5, brown2024acarboseimpairsgut pages 1-3) | Brown et al. 2024, DOI:10.1128/mbio.01506-24, https://doi.org/10.1128/mbio.01506-24 | Species-specific magnitude; growth inhibition context-dependent | CHEBI:acarbose label-only; NCBITaxon:Bacteroides thetaiotaomicron |
| acarbose | competitively inhibits transport through | SusC | “Acarbose competes for transport through the TonB-dependent SusC proteins” (brown2024acarboseimpairsgut pages 3-5, brown2024acarboseimpairsgut pages 1-3) | Brown et al. 2024, DOI:10.1128/mbio.01506-24, https://doi.org/10.1128/mbio.01506-24 | Strong mechanistic inhibitor edge; likely specific to Sus-type systems | CHEBI:acarbose label-only; SusC label-only |
| acarbose | inhibits | SusG | “BoSusG IC50 = 2.2 ± 0.35 µM and SusG IC50 = 68.2 ± 13.8 µM” (brown2024acarboseimpairsgut pages 7-9) | Brown et al. 2024, DOI:10.1128/mbio.01506-24, https://doi.org/10.1128/mbio.01506-24 | Quantitative enzyme inhibition; assay-specific fluorescent starch IC50 | CHEBI:acarbose label-only; SusG/BoSusG GH13 α-amylase EC:3.2.1.1 |
| montbretin A | slows growth of | one maltodextrin-consuming gut species | “montbretin A ... was more selective, slowing only one species” (lui2023characterizingtheeffect pages 1-2) | Lui et al. 2023, DOI:10.1021/acschembio.2c00791, https://doi.org/10.1021/acschembio.2c00791 | Weak for direct trait graph; community/assay-specific and species not named in excerpt | CHEBI:montbretin A label-only |
| MusEFGK2I transporter | transports | maltose and maltotriose | “MusEFGK2I (MUS) transporter ‘transports mainly maltose and maltotriose’” (bhandari2023transportandutilization pages 4-7, bhandari2023elucidatingthemechanisms pages 90-94) | Bhandari & Hill 2023, DOI:10.1128/spectrum.04435-22, https://doi.org/10.1128/spectrum.04435-22 | Gardnerella/glycogen study; still relevant as starch-breakdown-product uptake | TCDB family 3.A.1.1.45; CHEBI:maltose label-only; maltotriose label-only; NCBITaxon:Gardnerella |
| MalXFGK transporter | transports | maltodextrins / malto-oligosaccharides | “MalXFGK ... ‘is involved in the transport of maltose, maltotriose, malto-oligosaccharides (DP # 7), and maltodextrins’” (bhandari2023transportandutilization pages 4-7) | Bhandari & Hill 2023, DOI:10.1128/spectrum.04435-22, https://doi.org/10.1128/spectrum.04435-22 | Strong uptake edge for starch/glycogen hydrolysates; Gardnerella-specific | TCDB family 3.A.1.1.27; maltodextrin label-only; malto-oligosaccharides label-only |
| MalXFGK operon | encodes | α-glucosidase and pullulanase | “its operon also encodes an a-glucosidase and a pullulanase” (bhandari2023transportandutilization pages 4-7, bhandari2023elucidatingthemechanisms pages 90-94) | Bhandari & Hill 2023, DOI:10.1128/spectrum.04435-22, https://doi.org/10.1128/spectrum.04435-22 | Suggests coupled import plus intracellular debranching/hydrolysis; operon-level inference | EC:3.2.1.20; EC:3.2.1.41; NCBITaxon:Gardnerella |
| Gardnerella isolates | preferentially grow on | maltotetraose over glucose | “most isolates (10/15) grew significantly more on maltotetraose than on glucose” (bhandari2023transportandutilization pages 1-2, bhandari2023elucidatingthemechanismsa pages 76-82) | Bhandari & Hill 2023, DOI:10.1128/spectrum.04435-22, https://doi.org/10.1128/spectrum.04435-22 | Phenotypic edge showing preference for longer α-glucan products, not starch itself | CHEBI:maltotetraose label-only; CHEBI:glucose label-only; NCBITaxon:Gardnerella |
| Amy13A/B/C + Pul13A enzyme set | synergistically degrades | resistant starch | “best combos had ≥2× activity vs best single enzyme” (pickens2024clostridiumbutyricumprazmowski pages 11-13) | Pickens & Cockburn 2024, DOI:10.1128/msphere.00566-23, https://doi.org/10.1128/msphere.00566-23 | Strong for C. butyricum resistant starch; exact combinations vary by starch source | GH13_28/GH13_19 α-amylases; GH13_14 pullulanase; resistant starch label-only; NCBITaxon:Clostridium butyricum |
| Pul13A (type I pullulanase) | produces | maltotriose from pullulan | “Pul13A (Type I pullulanase) yields maltotriose from pullulan” (pickens2024clostridiumbutyricumprazmowski pages 11-13) | Pickens & Cockburn 2024, DOI:10.1128/msphere.00566-23, https://doi.org/10.1128/msphere.00566-23 | Boundary-case substrate; supports debranching chemistry relevant to branched starch | EC:3.2.1.41; GH13_14; CHEBI:pullulan label-only; maltotriose label-only |
| PulA3E (neutral pullulanase) | increases conversion of | maltodextrin to trehalose | “At PulA3E 40 U/g maltodextrin, trehalose production reached 166 g/L with an 83% conversion rate” (dong2024extracellularoverexpressionof pages 8-10, dong2024extracellularoverexpressionof pages 1-2) | Dong et al. 2024, DOI:10.3390/bioengineering11070661, https://doi.org/10.3390/bioengineering11070661 | Industrial application edge rather than natural trait mechanism; still useful for downstream evidence | EC:3.2.1.41; CHEBI:maltodextrin label-only; CHEBI:trehalose label-only |
| PD-ARY strain (B. subtilis expressing PulA3E) | produces | extracellular pullulanase activity | “PD-ARY ... reached 2465.1 U/mL at 78 h” (dong2024extracellularoverexpressionof pages 8-10, dong2024extracellularoverexpressionof pages 6-8) | Dong et al. 2024, DOI:10.3390/bioengineering11070661, https://doi.org/10.3390/bioengineering11070661 | Bioprocess metric; not a generic trait edge, but demonstrates scalable implementation | NCBITaxon:Bacillus subtilis; PulA3E EC:3.2.1.41; GO:0005576 extracellular region |


*Table: This table summarizes curation-ready causal edges for microbial starch degradation, covering the Bacteroides Sus system, inhibitor effects, resistant-starch enzyme synergy, Gardnerella oligosaccharide transporters, and industrial pullulanase implementation. It is useful as a draft edge set for TraitMech graph curation with source-linked evidence and grounding hints.*

---

### 8) Curation warnings (what not to curate yet)
1. **Montbretin A edges are assay-/community-specific** in the provided excerpts (species identity not specified in evidence snippet); curate only with explicit species-level backing. (lui2023characterizingtheeffect pages 1-2)
2. **Sus system edges should be taxon-qualified** (e.g., Bacteroides/Bacteroidota PULs). Overgeneralizing SusC/D to all bacteria would be incorrect; other taxa use different transporter architectures (ABC/MFS/PTS). (brown2024acarboseimpairsgut pages 3-5, lui2023characterizingtheeffect pages 1-2)
3. **Industrial PulA3E → trehalose conversion** is a strong real-world implementation but is not necessarily a natural ecological starch-utilization phenotype; curate as an application/bioprocess edge or annotate as “engineering/industrial context.” (dong2024extracellularoverexpressionof pages 8-10)
4. **Resistant starch utilization** appears rare in some ecosystems and depends on physical form; treat RS-specific synergy edges as conditional on RS substrate and the tested organism (C. butyricum). (pickens2024clostridiumbutyricumprazmowski pages 11-13)

---

## DOI-first bibliography (with dates and URLs)
- Brown HA, Morris AL, Pudlo NA, et al. **Acarbose impairs gut *Bacteroides* growth by targeting intracellular glucosidases.** *mBio*. **Dec 2024**. DOI: **10.1128/mbio.01506-24**. https://doi.org/10.1128/mbio.01506-24 (brown2024acarboseimpairsgut pages 1-3)
- Lui O, Dridi L, Gonzalez E, et al. **Characterizing the Effect of Amylase Inhibitors on Maltodextrin Metabolism by Gut Bacteria Using Fluorescent Glycan Labeling.** *ACS Chemical Biology*. **Feb 2023**. DOI: **10.1021/acschembio.2c00791**. https://doi.org/10.1021/acschembio.2c00791 (lui2023characterizingtheeffect pages 1-2)
- Sanchez-Gallardo R, Bottacini F, Friess L, et al. **Unveiling metabolic pathways of selected plant-derived glycans by *Bifidobacterium pseudocatenulatum*.** *Frontiers in Microbiology*. **Jul 2024**. DOI: **10.3389/fmicb.2024.1414471**. https://doi.org/10.3389/fmicb.2024.1414471 (sanchezgallardo2024unveilingmetabolicpathways pages 3-6)
- Pickens TL, Cockburn DW. ***Clostridium butyricum* Prazmowski can degrade and utilize resistant starch via a set of synergistically acting enzymes.** *mSphere*. **Jan 2024**. DOI: **10.1128/msphere.00566-23**. https://doi.org/10.1128/msphere.00566-23 (pickens2024clostridiumbutyricumprazmowski pages 11-13)
- Bhandari P, Hill JE. **Transport and Utilization of Glycogen Breakdown Products by *Gardnerella* spp. from the Human Vaginal Microbiome.** *Microbiology Spectrum*. **Apr 2023**. DOI: **10.1128/spectrum.04435-22**. https://doi.org/10.1128/spectrum.04435-22 (bhandari2023transportandutilization pages 1-2)
- Dong W, Fu X, Zhou D, et al. **Extracellular Overexpression of a Neutral Pullulanase in *Bacillus subtilis* through Multiple Copy Genome Integration and Atypical Secretion Pathway Enhancement.** *Bioengineering*. **Jun 2024**. DOI: **10.3390/bioengineering11070661**. https://doi.org/10.3390/bioengineering11070661 (dong2024extracellularoverexpressionof pages 1-2)


References

1. (brown2024acarboseimpairsgut pages 3-5): Haley A. Brown, Adeline L. Morris, Nicholas A. Pudlo, Ashley E. Hopkins, Eric C. Martens, Jonathan L. Golob, and Nicole M. Koropatkin. Acarbose impairs gut <i>bacteroides</i> growth by targeting intracellular glucosidases. Dec 2024. URL: https://doi.org/10.1128/mbio.01506-24, doi:10.1128/mbio.01506-24. This article has 3 citations and is from a domain leading peer-reviewed journal.

2. (pickens2024clostridiumbutyricumprazmowski pages 11-13): Tara L. Pickens and Darrell W. Cockburn. <i>clostridium butyricum</i> prazmowski can degrade and utilize resistant starch via a set of synergistically acting enzymes. Jan 2024. URL: https://doi.org/10.1128/msphere.00566-23, doi:10.1128/msphere.00566-23. This article has 4 citations and is from a peer-reviewed journal.

3. (brown2024acarboseimpairsgut pages 5-7): Haley A. Brown, Adeline L. Morris, Nicholas A. Pudlo, Ashley E. Hopkins, Eric C. Martens, Jonathan L. Golob, and Nicole M. Koropatkin. Acarbose impairs gut <i>bacteroides</i> growth by targeting intracellular glucosidases. Dec 2024. URL: https://doi.org/10.1128/mbio.01506-24, doi:10.1128/mbio.01506-24. This article has 3 citations and is from a domain leading peer-reviewed journal.

4. (bhandari2023transportandutilization pages 1-2): Pashupati Bhandari and Janet E. Hill. Transport and utilization of glycogen breakdown products by <i>gardnerella</i> spp. from the human vaginal microbiome. Apr 2023. URL: https://doi.org/10.1128/spectrum.04435-22, doi:10.1128/spectrum.04435-22. This article has 22 citations and is from a domain leading peer-reviewed journal.

5. (albright2025developmentofa pages 9-12): Claire E. Albright, Kelyah Spurgeon, Souzane Ntamubano, and Ariangela J. Kozik. Development of a basal media for carbon utilization assay and analysis of the starch utilization locus in prevotella melaninogenica. bioRxiv, Jul 2025. URL: https://doi.org/10.1101/2025.07.04.663206, doi:10.1101/2025.07.04.663206. This article has 0 citations.

6. (brown2024acarboseimpairsgut pages 7-9): Haley A. Brown, Adeline L. Morris, Nicholas A. Pudlo, Ashley E. Hopkins, Eric C. Martens, Jonathan L. Golob, and Nicole M. Koropatkin. Acarbose impairs gut <i>bacteroides</i> growth by targeting intracellular glucosidases. Dec 2024. URL: https://doi.org/10.1128/mbio.01506-24, doi:10.1128/mbio.01506-24. This article has 3 citations and is from a domain leading peer-reviewed journal.

7. (dong2024extracellularoverexpressionof pages 1-2): Wenkang Dong, Xiaoping Fu, Dasen Zhou, Jia Teng, Jun Yang, Jie Zhen, Xingya Zhao, Yihan Liu, Hongchen Zheng, and Wenqin Bai. Extracellular overexpression of a neutral pullulanase in bacillus subtilis through multiple copy genome integration and atypical secretion pathway enhancement. Bioengineering, 11:661, Jun 2024. URL: https://doi.org/10.3390/bioengineering11070661, doi:10.3390/bioengineering11070661. This article has 6 citations.

8. (dong2024extracellularoverexpressionof pages 8-10): Wenkang Dong, Xiaoping Fu, Dasen Zhou, Jia Teng, Jun Yang, Jie Zhen, Xingya Zhao, Yihan Liu, Hongchen Zheng, and Wenqin Bai. Extracellular overexpression of a neutral pullulanase in bacillus subtilis through multiple copy genome integration and atypical secretion pathway enhancement. Bioengineering, 11:661, Jun 2024. URL: https://doi.org/10.3390/bioengineering11070661, doi:10.3390/bioengineering11070661. This article has 6 citations.

9. (brown2024acarboseimpairsgut pages 1-3): Haley A. Brown, Adeline L. Morris, Nicholas A. Pudlo, Ashley E. Hopkins, Eric C. Martens, Jonathan L. Golob, and Nicole M. Koropatkin. Acarbose impairs gut <i>bacteroides</i> growth by targeting intracellular glucosidases. Dec 2024. URL: https://doi.org/10.1128/mbio.01506-24, doi:10.1128/mbio.01506-24. This article has 3 citations and is from a domain leading peer-reviewed journal.

10. (lui2023characterizingtheeffect pages 1-2): Olivia Lui, Lharbi Dridi, Emmanuel Gonzalez, Suraya Yasmine, Ryszard Kubinski, Hannah Billings, Joerg Bohlmann, Stephen G Withers, Corinne Maurice, and Bastien Castagner. Characterizing the effect of amylase inhibitors on maltodextrin metabolism by gut bacteria using fluorescent glycan labeling. ACS Chemical Biology, 18:356-366, Feb 2023. URL: https://doi.org/10.1021/acschembio.2c00791, doi:10.1021/acschembio.2c00791. This article has 10 citations and is from a domain leading peer-reviewed journal.

11. (sanchezgallardo2024unveilingmetabolicpathways pages 3-6): Rocio Sanchez-Gallardo, Francesca Bottacini, Lisa Friess, Maria Esteban-Torres, Clarissa Somers, Rebecca L. Moore, Fionnuala M. McAuliffe, Paul D. Cotter, and Douwe van Sinderen. Unveiling metabolic pathways of selected plant-derived glycans by bifidobacterium pseudocatenulatum. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1414471, doi:10.3389/fmicb.2024.1414471. This article has 5 citations and is from a peer-reviewed journal.

12. (lui2023characterizingtheeffect pages 3-5): Olivia Lui, Lharbi Dridi, Emmanuel Gonzalez, Suraya Yasmine, Ryszard Kubinski, Hannah Billings, Joerg Bohlmann, Stephen G Withers, Corinne Maurice, and Bastien Castagner. Characterizing the effect of amylase inhibitors on maltodextrin metabolism by gut bacteria using fluorescent glycan labeling. ACS Chemical Biology, 18:356-366, Feb 2023. URL: https://doi.org/10.1021/acschembio.2c00791, doi:10.1021/acschembio.2c00791. This article has 10 citations and is from a domain leading peer-reviewed journal.

13. (bhandari2023transportandutilization pages 4-7): Pashupati Bhandari and Janet E. Hill. Transport and utilization of glycogen breakdown products by <i>gardnerella</i> spp. from the human vaginal microbiome. Apr 2023. URL: https://doi.org/10.1128/spectrum.04435-22, doi:10.1128/spectrum.04435-22. This article has 22 citations and is from a domain leading peer-reviewed journal.

14. (brown2024acarboseimpairsgut pages 27-27): Haley A. Brown, Adeline L. Morris, Nicholas A. Pudlo, Ashley E. Hopkins, Eric C. Martens, Jonathan L. Golob, and Nicole M. Koropatkin. Acarbose impairs gut <i>bacteroides</i> growth by targeting intracellular glucosidases. Dec 2024. URL: https://doi.org/10.1128/mbio.01506-24, doi:10.1128/mbio.01506-24. This article has 3 citations and is from a domain leading peer-reviewed journal.

15. (bhandari2023elucidatingthemechanisms pages 90-94): P Bhandari. Elucidating the mechanisms of extracellular glycogen utilization in gardnerella spp. Unknown journal, 2023.

16. (bhandari2023elucidatingthemechanismsa pages 76-82): P Bhandari. Elucidating the mechanisms of extracellular glycogen utilization in gardnerella spp. Unknown journal, 2023.

17. (dong2024extracellularoverexpressionof pages 6-8): Wenkang Dong, Xiaoping Fu, Dasen Zhou, Jia Teng, Jun Yang, Jie Zhen, Xingya Zhao, Yihan Liu, Hongchen Zheng, and Wenqin Bai. Extracellular overexpression of a neutral pullulanase in bacillus subtilis through multiple copy genome integration and atypical secretion pathway enhancement. Bioengineering, 11:661, Jun 2024. URL: https://doi.org/10.3390/bioengineering11070661, doi:10.3390/bioengineering11070661. This article has 6 citations.