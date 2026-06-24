---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T12:16:20.083053'
end_time: '2026-06-18T12:34:16.674043'
duration_seconds: 1076.59
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: photolithoautotrophic
  trait_identifier: METPO:1000665
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: photolithoautotrophic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic type in which an organism obtains energy from light and carbon
    from carbon dioxide using inorganic electron donors.
  parent_traits: METPO:1000631
  synonyms: photolithoautotroph
  evidence_summary: 'DOI:10.3389/fmicb.2011.00165: oxidize sulfide (Review supports
    sulfide oxidation coupled to phototrophic central carbon and energy metabolism.)
    | DOI:10.3390/antiox10060829: reduced sulfur compounds as an electron donor (Review
    supports reduced sulfur electron donors in photolithotrophic sulfur bacteria.)
    | DOI:10.1128/AEM.02473-10: autotrophic CO2 fixation (Review supports CO2 fixation
    as the autotrophic carbon-assimilation process.)'
  causal_graph_summary: 'photolithoautotrophic_light_inorganic_donor_fixation: 10
    nodes, 8 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 36
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** photolithoautotrophic
- **METPO identifier:** METPO:1000665
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy from light and carbon from carbon dioxide using inorganic electron donors.
- **Parent traits:** METPO:1000631
- **Synonyms:** photolithoautotroph
- **Existing evidence:** DOI:10.3389/fmicb.2011.00165: oxidize sulfide (Review supports sulfide oxidation coupled to phototrophic central carbon and energy metabolism.) | DOI:10.3390/antiox10060829: reduced sulfur compounds as an electron donor (Review supports reduced sulfur electron donors in photolithotrophic sulfur bacteria.) | DOI:10.1128/AEM.02473-10: autotrophic CO2 fixation (Review supports CO2 fixation as the autotrophic carbon-assimilation process.)
- **Existing causal graph summary:** photolithoautotrophic_light_inorganic_donor_fixation: 10 nodes, 8 edges

## Research Objective

Research the microbial trait **photolithoautotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/photolithoautotrophic.yaml`.

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
- **Trait label:** photolithoautotrophic
- **METPO identifier:** METPO:1000665
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy from light and carbon from carbon dioxide using inorganic electron donors.
- **Parent traits:** METPO:1000631
- **Synonyms:** photolithoautotroph
- **Existing evidence:** DOI:10.3389/fmicb.2011.00165: oxidize sulfide (Review supports sulfide oxidation coupled to phototrophic central carbon and energy metabolism.) | DOI:10.3390/antiox10060829: reduced sulfur compounds as an electron donor (Review supports reduced sulfur electron donors in photolithotrophic sulfur bacteria.) | DOI:10.1128/AEM.02473-10: autotrophic CO2 fixation (Review supports CO2 fixation as the autotrophic carbon-assimilation process.)
- **Existing causal graph summary:** photolithoautotrophic_light_inorganic_donor_fixation: 10 nodes, 8 edges

## Research Objective

Research the microbial trait **photolithoautotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/photolithoautotrophic.yaml`.

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


## Research report: Microbial trait **photolithoautotrophic** (METPO:1000665)

### 1) Scope summary (trait meaning, boundaries, assays)

**Definition (operational):** A photolithoautotroph uses **light** as the primary energy source, **inorganic electron donors** (lithotrophy) as the source of electrons/reducing power, and **CO2 (dissolved inorganic carbon)** as the carbon source via an autotrophic carbon fixation pathway. This matches the reviewed METPO definition and is consistent with current microbiology usage across both oxygenic and anoxygenic photosynthetic microbes. The defining features are explicit in recent reviews of anoxygenic photosynthesis (electron donor often H2S; carbon source CO2) and in recent engineering work demonstrating light-driven CO2 fixation when appropriate electron and energy modules are provided. (kushkevych2024anoxygenicphotosynthesiswith pages 1-2, tu2024engineeringrhodopsinbasedartificial pages 21-24, tu2023engineeringartificialphotosynthesis pages 3-4)

**Key boundary cases to distinguish during curation:**

1. **Photoautotroph vs photolithoautotroph:** Some phototrophs are photoautotrophic but not lithotrophic (if they use organic electron donors), so the *inorganic* electron donor constraint is essential.
2. **Photoheterotrophs / aerobic anoxygenic phototrophs (AAP):** These use light to supplement energy but rely on organic carbon; they should not be annotated as photolithoautotrophic unless CO2 fixation supports biomass carbon (not merely anaplerosis).
3. **Chemolithoautotrophs:** Fix CO2 using inorganic donors but do not use light; they are mechanistically adjacent (share CO2 fixation and DIC acquisition toolkits) but fall outside this trait.
4. **Engineered “artificial photosynthesis” systems:** Recent systems (e.g., rhodopsin + extracellular electron uptake) can exhibit **light-driven CO2-to-biomass** behavior, but these are **assay-/system-specific** and should be flagged as *uncertain* for general trait mechanism graphs unless the curation explicitly allows engineered analogs. (tu2023engineeringartificialphotosynthesis pages 3-4, tu2024engineeringrhodopsinbasedartificial pages 51-55)

**Assay signals typically indicating the trait:** light-dependent growth on CO2 with an inorganic electron donor; carbon fixation measured by isotopic labeling (e.g., Raman D2O incorporation under CO2 + light in an engineered system) or conventional 13C-bicarbonate incorporation; and presence/expression of (i) photochemical reaction center components and (ii) CO2 fixation pathways and DIC acquisition toolkits. (tu2023engineeringartificialphotosynthesis pages 3-4, scott2024widespreaddissolvedinorganic pages 2-4)

---

### 2) Key concepts & current mechanistic understanding (nodes for a TraitMech causal graph)

#### 2.1 Core process modules (high-level)

**Photochemical energy conversion and electron transport**
- Anoxygenic phototrophs include green sulfur bacteria (GSB) and purple sulfur bacteria (PSB), which use reduced inorganic compounds rather than water as electron donors; GSB have chlorosomes as light-harvesting antenna structures. (kushkevych2024anoxygenicphotosynthesiswith pages 1-2)
- Reaction centers are typically categorized as **Type I** vs **Type II**, with differing donor pigments and downstream carriers (e.g., ferredoxin, quinones), which is relevant to how reducing equivalents are produced for CO2 fixation and how electrons can be rewired for applications. (lawrence2023rewiringphotosyntheticelectron pages 4-7)

**Carbon fixation pathways relevant to photolithoautotrophy**
- **Reverse TCA (rTCA)** is highlighted as the CO2 assimilation route for GSB (e.g., *Chlorobium* spp.). (kushkevych2024anoxygenicphotosynthesiswith pages 1-2)
- The **Calvin–Benson–Bassham (CBB) cycle** is a widespread CO2 fixation pathway with **RuBisCO** as the key carboxylase; CBB can be supported by CO2-concentrating mechanisms. (scott2024widespreaddissolvedinorganic pages 1-2, scott2024widespreaddissolvedinorganic pages 4-7)

**DIC acquisition and CO2-concentrating mechanisms (CCM)**
- A 2024 minireview synthesizes the “DIC toolkit” that bridges environmental DIC supply to intracellular fixation demand, emphasizing **carbonic anhydrases (CAs; EC 4.2.1.1)** and **DIC transporters**. (scott2024widespreaddissolvedinorganic pages 1-2)
- DIC uptake modules are diverse, including HCO3− uptake systems **SbtA**, **BicA (SulP family)**, **CmpABCD**, and CO2-active complexes such as **DAC**; these are components of CCMs that elevate CO2 near RuBisCO and reduce oxygenation side reactions. (scott2024widespreaddissolvedinorganic pages 2-4, scott2024widespreaddissolvedinorganic pages 4-7)
- **Carboxysomes** are protein microcompartments containing RuBisCO and a **carboxysomal CA (CsoSCA)** that converts HCO3− to CO2 inside the compartment, thereby concentrating CO2 at RuBisCO. (scott2024widespreaddissolvedinorganic pages 2-4, scott2024widespreaddissolvedinorganic pages 10-13)

#### 2.2 Electron donors and oxidation machinery (lithotrophy side)

**Reduced sulfur compounds**
- In anoxygenic photosynthesis, **H2S is commonly used as the main electron donor**, and GSB oxidize H2S to elemental sulfur. (kushkevych2024anoxygenicphotosynthesiswith pages 1-2)
- Recent synthesis on rewiring photosynthetic electron transport highlights reduced sulfur donors (sulfide, thiosulfate) and associated oxidation machinery (e.g., **SQR** and **SoxAX**) that feed electrons into quinone pools and downstream carriers. (lawrence2023rewiringphotosyntheticelectron pages 4-7)

**Fe(II) as an electron donor (photoferrotrophy)**
- Photoferrotrophy is anoxygenic phototrophic **Fe(II) oxidation**; it is mechanistically within photolithoautotrophy when coupled to CO2 fixation, but it is restricted to specific taxa and geochemical conditions (ferruginous environments). (nikeleit2024inhibitionofphototrophic pages 1-2)

#### 2.3 Environmental and inhibitory factors

A 2024 Nature Geoscience study shows **nitric oxide (NO)** can inhibit phototrophic Fe(II) oxidation (photoferrotrophy) at very low concentrations and discusses the interaction between nitrate-reducing Fe(II) oxidizers and photoferrotrophs, implying that nitrogen-cycle intermediates can reshape photolithoautotrophic Fe cycling in ferruginous waters. (nikeleit2024inhibitionofphototrophic pages 3-4, nikeleit2024inhibitionofphototrophic pages 9-11)

**Visual evidence:** Extended Data Fig. 7 from Nikeleit et al. (2024) summarizes reaction-center markers (Type I *pshA*; Type II *pufL*) and NO detox genes (*norV*, *norB*, *hmpA*) across phototroph phylogeny, supporting gene-node inclusion and taxonomic boundary decisions. (nikeleit2024inhibitionofphototrophic media 262710d9)

---

### 3) Candidate causal graph nodes (grouped by type, with grounding suggestions)

#### A) Pathways / processes
- Photosynthetic electron transport chain (GO:0009767) (lawrence2023rewiringphotosyntheticelectron pages 4-7)
- CO2 fixation via reverse TCA cycle (candidate GO:0019646) (kushkevych2024anoxygenicphotosynthesiswith pages 1-2)
- Calvin–Benson–Bassham cycle (GO:0019253) (scott2024widespreaddissolvedinorganic pages 4-7)
- CO2-concentrating mechanism (label-only candidate; includes carboxysomes, DIC transporters, CO2-active complexes) (scott2024widespreaddissolvedinorganic pages 2-4)

#### B) Proteins / complexes / gene families
- RuBisCO large/small subunits: **cbbL/cbbS** (Scott review notes genomic colocation with carboxysome loci; RuBisCO named as CO2-specific carboxylase) (scott2024widespreaddissolvedinorganic pages 4-7, scott2024widespreaddissolvedinorganic pages 1-2)
- Carbonic anhydrase (EC:4.2.1.1) (scott2024widespreaddissolvedinorganic pages 1-2)
- Carboxysomal CA **CsoSCA** (label-only candidate) (scott2024widespreaddissolvedinorganic pages 2-4)
- DIC transporters: **SbtA**, **BicA**, **CmpABCD**, **SulP**, **DAC** (label-only candidates where no stable CURIE available) (scott2024widespreaddissolvedinorganic pages 2-4, scott2024widespreaddissolvedinorganic pages 7-10)
- Sulfur oxidation: **SQR** (EC:1.8.5.4), **SoxAX** (label-only complex) (lawrence2023rewiringphotosyntheticelectron pages 4-7)
- Reaction center markers: Type I (*pshA*), Type II (*pufL*) (nikeleit2024inhibitionofphototrophic pages 17-17, nikeleit2024inhibitionofphototrophic media 262710d9)
- NO detox genes: **norV**, **norB**, **hmpA** (label-only; distribution shown visually) (nikeleit2024inhibitionofphototrophic pages 17-17, nikeleit2024inhibitionofphototrophic media 262710d9)

#### C) Chemicals (electron donors/acceptors, inhibitors)
- CO2 (CHEBI:16526) and bicarbonate (CHEBI:17544) (scott2024widespreaddissolvedinorganic pages 1-2)
- Hydrogen sulfide H2S (CHEBI:16134) (kushkevych2024anoxygenicphotosynthesiswith pages 1-2)
- Thiosulfate (CHEBI:9568) (lawrence2023rewiringphotosyntheticelectron pages 4-7)
- Fe(II) / iron(2+) (CHEBI:29033) (nikeleit2024inhibitionofphototrophic pages 1-2)
- Nitric oxide NO (CHEBI:16480), nitrate NO3−, nitrite NO2−, nitrous oxide N2O (nikeleit2024inhibitionofphototrophic pages 4-5, nikeleit2024inhibitionofphototrophic pages 3-4)

#### D) Cellular structures
- Chlorosome (GO:0030096) (kushkevych2024anoxygenicphotosynthesiswith pages 1-2)
- Carboxysome (GO:0036464) (scott2024widespreaddissolvedinorganic pages 2-4)

#### E) Environmental/experimental factors
- Light intensity and spectrum (e.g., 720–780 nm referenced for GSB applications; 10 vs 25 kLx affects performance) (kushkevych2024anoxygenicphotosynthesiswith pages 16-17)
- pH-dependent DIC speciation affecting transporter choice (DAC absent above pH 8.3; SbtA/SulP absent below ~pH 4.3 in genome survey) (scott2024widespreaddissolvedinorganic pages 7-10)
- Ferruginous environments + nitrate/NOx availability as inhibitors/competitors for photoferrotrophy (nikeleit2024inhibitionofphototrophic pages 3-4, nikeleit2024inhibitionofphototrophic pages 1-2)

---

### 4) Evidence-backed candidate causal edges (curation table)

The following table is formatted for direct trait-mechanism curation.

| Edge (triple) | Evidence snippet (short quote/paraphrase) | Reference (DOI, year, URL) | Notes/uncertainty | Suggested ontology grounding (CURIEs for subject/object where possible) |
|---|---|---|---|---|
| light -- enables --> photolithoautotrophic energy metabolism | GSB are described as “light-driven microbes”; engineered R. eutropha showed “light-driven CO2 fixation” with rhodopsin-powered proton motive force (kushkevych2024anoxygenicphotosynthesiswith pages 1-2, tu2023engineeringartificialphotosynthesis pages 3-4) | 10.3389/fmicb.2024.1417714 (2024) https://doi.org/10.3389/fmicb.2024.1417714; 10.1038/s41467-023-43524-4 (2023) https://doi.org/10.1038/s41467-023-43524-4 | Core defining edge for trait; broad across oxygenic and anoxygenic photolithoautotrophs. | subject: ENVO:01001148 (light, candidate); object: METPO:1000665 |
| chlorosome -- captures --> light energy | GSB “possess chlorosomes… lipid-monolayer vesicles that act as light-collecting antennas” (kushkevych2024anoxygenicphotosynthesiswith pages 1-2) | 10.3389/fmicb.2024.1417714 (2024) https://doi.org/10.3389/fmicb.2024.1417714 | Strong for green sulfur bacteria; taxon-specific, not universal to all photolithoautotrophs. | subject: GO:0030096 (chlorosome); object: ENVO:01001148 (light, candidate) |
| hydrogen sulfide -- serves_as_electron_donor_for --> anoxygenic photolithoautotrophy | “H2S is commonly used as the main electron donor” and GSB “oxidize H2S to elemental sulfur” (kushkevych2024anoxygenicphotosynthesiswith pages 1-2) | 10.3389/fmicb.2024.1417714 (2024) https://doi.org/10.3389/fmicb.2024.1417714 | Strong for many sulfur phototrophs; not universal to cyanobacteria or all photolithoautotrophs. | subject: CHEBI:16134 (hydrogen sulfide); object: METPO:1000665 |
| ferrous iron [Fe(II)] -- serves_as_electron_donor_for --> photoferrotrophy | Photoferrotrophy is defined by Fe(II) oxidation via anoxygenic photosynthesis; stoichiometry given for phototrophic Fe(II) oxidation (nikeleit2024inhibitionofphototrophic pages 1-2) | 10.1038/s41561-024-01560-9 (2024) https://doi.org/10.1038/s41561-024-01560-9 | Strong but specific to photoferrotroph subset of photolithoautotrophs. | subject: CHEBI:29033 (iron(2+)); object: label-only candidate node: photoferrotrophy |
| reduced sulfur compounds -- donate_electrons_to --> photosynthetic electron transport chain | Lawrence review tabulates sulfide and thiosulfate as electron donors and notes SQR/SoxAX oxidation machinery linked to quinone pools (lawrence2023rewiringphotosyntheticelectron pages 4-7, lawrence2023rewiringphotosyntheticelectron pages 9-11) | 10.1038/s44222-023-00093-x (2023) https://doi.org/10.1038/s44222-023-00093-x | Mechanistically useful; taxon/module-specific. | subject: CHEBI:26806 (sulfur compound, broad candidate); object: GO:0009767 (photosynthetic electron transport chain) |
| green sulfur bacteria -- fixes --> carbon dioxide via reverse TCA cycle | “Green sulfur bacteria fix CO2 as their carbon source via the reverse tricarboxylic acid cycle” (kushkevych2024anoxygenicphotosynthesiswith pages 1-2) | 10.3389/fmicb.2024.1417714 (2024) https://doi.org/10.3389/fmicb.2024.1417714 | Strong for GSB; not universal to all photolithoautotrophs. | subject: NCBITaxon:1090 (Chlorobiaceae, approximate candidate); object: GO:0019646 (reverse TCA cycle, candidate) |
| Calvin-Benson-Bassham cycle -- fixes --> carbon dioxide | CBB is listed as a major CO2 fixation pathway; RuBisCO is the key carboxylase, and in engineered R. eutropha CO2 fixation occurred “via the Calvin cycle” (tu2024engineeringrhodopsinbasedartificial pages 21-24, tu2023engineeringartificialphotosynthesis pages 3-4) | 10.1038/s41467-023-43524-4 (2023) https://doi.org/10.1038/s41467-023-43524-4 | Strong as general autotrophic pathway edge, but pathway choice is taxon-specific. | subject: GO:0019253 (reductive pentose-phosphate cycle); object: CHEBI:16526 (carbon dioxide) |
| RuBisCO -- catalyzes --> carbon dioxide fixation in CBB cycle | Scott notes many autotrophic carboxylases are specific for CO2, “e.g., Ribulose 1,5-bisphosphate carboxylase/oxygenase”; Tu thesis identifies RuBisCO as key CBB enzyme (scott2024widespreaddissolvedinorganic pages 1-2, tu2024engineeringrhodopsinbasedartificial pages 21-24) | 10.1128/aem.01557-23 (2024) https://doi.org/10.1128/aem.01557-23 | Broadly accepted; cited here from review context rather than organism-specific experiment. | subject: EC:4.1.1.39; object: CHEBI:16526 |
| carbonic anhydrase -- interconverts --> carbon dioxide and bicarbonate | CA “catalyzes CO2 ⇄ H2CO3 ⇄ HCO3− interconversion,” accelerating DIC equilibration (scott2024widespreaddissolvedinorganic pages 2-4, scott2024widespreaddissolvedinorganic pages 1-2) | 10.1128/aem.01557-23 (2024) https://doi.org/10.1128/aem.01557-23 | Strong general mechanistic edge for CCM/DIC handling. | subject: EC:4.2.1.1; object: CHEBI:17544 (bicarbonate) / CHEBI:16526 (carbon dioxide) |
| DIC transporters (SbtA/BicA/CmpABCD/DAC/SulP) -- import --> inorganic carbon species | Scott lists HCO3− uptake systems SbtA, BicA, CmpABCD and DAC; transporters bridge environmental DIC supply to fixation demand (scott2024widespreaddissolvedinorganic pages 2-4, scott2024widespreaddissolvedinorganic pages 1-2) | 10.1128/aem.01557-23 (2024) https://doi.org/10.1128/aem.01557-23 | Strong for CCM-enabled autotrophy; transporter usage depends on pH and DIC speciation. | subject: UniProt/GO label-only candidates: SbtA, BicA, CmpABCD, DAC, SulP; object: CHEBI:17544 / CHEBI:16526 |
| extracellular carbonic anhydrase -- facilitates --> DIC transporter activity | “Many CBB genomes that encode DIC transporters also encode eCA, which could facilitate transporter activity” (scott2024widespreaddissolvedinorganic pages 13-15, scott2024widespreaddissolvedinorganic pages 7-10) | 10.1128/aem.01557-23 (2024) https://doi.org/10.1128/aem.01557-23 | Inference from comparative genomics/review; curate as supportive, not universal. | subject: EC:4.2.1.1; object: label-only candidate node: DIC transporter activity |
| carboxysome -- concentrates --> carbon dioxide near RuBisCO | Carboxysomes are microcompartments containing RubisCO and carboxysomal CA; they “concentrate CO2 for RubisCO by importing cytoplasmic HCO3−” (scott2024widespreaddissolvedinorganic pages 10-13, scott2024widespreaddissolvedinorganic pages 2-4) | 10.1128/aem.01557-23 (2024) https://doi.org/10.1128/aem.01557-23 | Strong for CBB-based CCMs; not relevant to all photolithoautotrophs. | subject: GO:0036464 (carboxysome); object: CHEBI:16526 |
| carboxysomal carbonic anhydrase CsoSCA -- supplies --> carbon dioxide inside carboxysome | Scott notes carboxysomal CA (CsoSCA) converts HCO3− to CO2 within the microcompartment (scott2024widespreaddissolvedinorganic pages 2-4, scott2024widespreaddissolvedinorganic pages 4-7) | 10.1128/aem.01557-23 (2024) https://doi.org/10.1128/aem.01557-23 | Strong for alpha-carboxysome systems; taxon/module-specific. | subject: label-only candidate: CsoSCA; object: CHEBI:16526 |
| cytoplasmic carbonic anhydrase + energy-coupled DIC transporter -- causes --> carbon dioxide leakage | Co-occurrence “can be detrimental” because cCA converts imported HCO3− to CO2 that diffuses out; mislocalized CA abolishes CCM function (scott2024widespreaddissolvedinorganic pages 10-13, scott2024widespreaddissolvedinorganic pages 2-4, scott2024widespreaddissolvedinorganic pages 15-18) | 10.1128/aem.01557-23 (2024) https://doi.org/10.1128/aem.01557-23 | Important negative edge/constraint; context-dependent and relevant for engineering. | subject: EC:4.2.1.1 + label-only DIC transporter; object: label-only candidate node: CO2 leakage |
| SQR (sulfide:quinone oxidoreductase) -- oxidizes --> sulfide and reduces quinone pool | Lawrence cites SQR as oxidation machinery linking sulfide oxidation to quinone pools in anoxygenic phototrophs (lawrence2023rewiringphotosyntheticelectron pages 4-7, lawrence2023rewiringphotosyntheticelectron pages 9-11) | 10.1038/s44222-023-00093-x (2023) https://doi.org/10.1038/s44222-023-00093-x | Good mechanistic edge for sulfur phototrophs; review-level evidence in provided context. | subject: EC:1.8.5.4; object: CHEBI:16134 / label-only candidate: quinone pool |
| SoxAX -- participates_in --> thiosulfate/reduced sulfur oxidation | Lawrence notes SoxAX among sulfur-oxidizing components in green sulfur bacteria and related systems (lawrence2023rewiringphotosyntheticelectron pages 4-7, lawrence2023rewiringphotosyntheticelectron pages 9-11) | 10.1038/s44222-023-00093-x (2023) https://doi.org/10.1038/s44222-023-00093-x | Mechanistically relevant but enzyme role may vary by sulfur substrate and taxon. | subject: label-only candidate: SoxAX complex; object: CHEBI:9568 (thiosulfate) |
| photosynthetic electron transport chain -- generates --> NADPH | Lawrence tabulates ferredoxin and FNR with NADPH as terminal reductant; Tu reports increased NADH/NADPH in light after GR+MtrCAB expression (lawrence2023rewiringphotosyntheticelectron pages 4-7, tu2023engineeringartificialphotosynthesis pages 3-4) | 10.1038/s44222-023-00093-x (2023) https://doi.org/10.1038/s44222-023-00093-x; 10.1038/s41467-023-43524-4 (2023) https://doi.org/10.1038/s41467-023-43524-4 | Strong general redox edge; engineered example strengthens causal interpretation. | subject: GO:0009767; object: CHEBI:57783 (NADPH) |
| nitric oxide -- inhibits --> photoferrotrophy | NO had “a strong inhibitory effect”; complete inhibition observed at 6.2 µM and suppression even at 12 nM in modelling/assays (nikeleit2024inhibitionofphototrophic pages 3-4, nikeleit2024inhibitionofphototrophic pages 9-11) | 10.1038/s41561-024-01560-9 (2024) https://doi.org/10.1038/s41561-024-01560-9 | Strong but specific to photoferrotrophic Fe(II) oxidizers in ferruginous settings. | subject: CHEBI:16480 (nitric oxide); object: label-only candidate node: photoferrotrophy |
| nitrate-reducing Fe(II) oxidizers -- produce --> nitric oxide | Nikeleit reports nitrate-reducing Fe(II) oxidizers generate reactive intermediates including NO and N2O during denitrification/chemodenitrification (nikeleit2024inhibitionofphototrophic pages 2-3, nikeleit2024inhibitionofphototrophic pages 4-5) | 10.1038/s41561-024-01560-9 (2024) https://doi.org/10.1038/s41561-024-01560-9 | Strong for studied systems; relevant environmental interaction rather than intrinsic trait requirement. | subject: label-only candidate node: nitrate-reducing Fe(II) oxidizers; object: CHEBI:16480 |
| NO detox genes (norV/norB/hmpA) -- may_mitigate --> nitric oxide stress | Photoferrotrophs were susceptible “despite having genomic capabilities for nitric oxide detoxification”; distribution of norV/norB/hmpA surveyed across phototrophs (nikeleit2024inhibitionofphototrophic pages 1-2, nikeleit2024inhibitionofphototrophic pages 17-17, nikeleit2024inhibitionofphototrophic media 262710d9) | 10.1038/s41561-024-01560-9 (2024) https://doi.org/10.1038/s41561-024-01560-9 | Weak/uncertain as positive causal edge because genes do not guarantee protection at inhibitory NO concentrations. | subject: label-only candidates: norV / norB / hmpA; object: CHEBI:16480 |
| MtrCAB extracellular electron conduit -- transfers_electrons_to --> R. eutropha electron transport chain | Tu 2023 states MtrCAB links intracellular ETC to extracellular substrates and enables uptake of cathodic electrons (tu2023engineeringartificialphotosynthesis pages 3-4) | 10.1038/s41467-023-43524-4 (2023) https://doi.org/10.1038/s41467-023-43524-4 | Engineered-system, assay-specific; uncertain for general photolithoautotrophic trait curation. | subject: label-only candidate: MtrCAB complex; object: GO:0009767 / label-only candidate: ETC |
| Gloeobacter rhodopsin -- generates --> proton motive force | GR “provides proton motive force” and harvests light around 530 nm in engineered photoelectrosynthesis (tu2023engineeringartificialphotosynthesis pages 3-4, tu2024engineeringrhodopsinbasedartificial pages 51-55) | 10.1038/s41467-023-43524-4 (2023) https://doi.org/10.1038/s41467-023-43524-4 | Engineered-system edge; not canonical for most natural photolithoautotrophs. | subject: label-only candidate: Gloeobacter rhodopsin; object: GO:0015992 (proton motive force generation, candidate) |
| proton motive force -- drives --> ATP synthesis | Tu dissertation summary notes GR-driven proton motive force powers ATP synthase and ATP synthesis during photoelectroautotrophy (tu2024engineeringrhodopsinbasedartificial pages 51-55) | 10.5287/ora-8jgz2nrvd (2024) https://doi.org/10.5287/ora-8jgz2nrvd | Outside requested DOI set except as context-derived thesis summary; use cautiously and mark uncertain if curated. | subject: GO:0015992 (candidate); object: GO:0006754 (ATP biosynthetic process) |
| MtrCAB + rhodopsin system -- increases --> NADH/NADPH pools | Co-expression of MtrCAB and GR led to increased NADH and NADPH after light incubation (tu2023engineeringartificialphotosynthesis pages 3-4) | 10.1038/s41467-023-43524-4 (2023) https://doi.org/10.1038/s41467-023-43524-4 | Engineered-system, assay-specific; useful mechanistic inspiration but uncertain for general trait graph. | subject: label-only candidate: MtrCAB+GR system; object: CHEBI:57945 (NADH) / CHEBI:57783 (NADPH) |
| increased NADH/NADPH + ATP -- promotes --> carbon dioxide fixation | In engineered R. eutropha, light-driven PMF and electron uptake regenerated reductant/energy and supported biomass synthesis from CO2; Raman D2O incorporation supported light + CO2 fixation (tu2023engineeringartificialphotosynthesis pages 3-4, tu2024engineeringrhodopsinbasedartificial pages 51-55) | 10.1038/s41467-023-43524-4 (2023) https://doi.org/10.1038/s41467-023-43524-4 | Engineered-system, assay-specific; uncertain for direct curation beyond generic energy/reductant support of autotrophy. | subject: CHEBI:57945 / CHEBI:57783 / CHEBI:15422; object: CHEBI:16526 |
| photolithoautotrophic metabolism -- can_be_applied_to --> H2S detoxification / desulfurization bioreactors | Review describes GSB-based bioreactors removing H2S from synthetic biogas; “from the 10th day 100% desulfurization was observed” and feed contained 70% CH4, 29.5% CO2, 0.5% H2S (kushkevych2024anoxygenicphotosynthesiswith pages 16-17) | 10.3389/fmicb.2024.1417714 (2024) https://doi.org/10.3389/fmicb.2024.1417714 | Application edge, not a mechanistic trait-defining edge; useful for report but likely not for core TraitMech graph. | subject: METPO:1000665; object: label-only candidate node: H2S detoxification / biodesulfurization |


*Table: This table lists candidate subject-predicate-object edges for curating the photolithoautotrophic trait, using only the specified recent sources and context evidence. It emphasizes core trait-defining mechanisms, supporting molecular modules, environmental inhibitors, and clearly flags engineered or taxon-specific edges as uncertain.*

---

### 5) Recent developments (2023–2024) and expert analysis

#### 5.1 Systems-level refinement: DIC “toolkits” across autotrophic pathways (2024)
Scott et al. (2024) reframes inorganic carbon acquisition as a modular “toolkit” (CAs, transporters, CO2-active complexes, carboxysomes) that bridges environmental supply and pathway-specific demand; it highlights strong mechanistic constraints (slow uncatalyzed CO2/HCO3− interconversion; HCO3− dominance at circumneutral pH; diffusion differences) and provides engineering-relevant guidance: transporter selection should match **pH/DIC speciation**, and CA localization/compartmentation (carboxysomal CA) is critical to avoid CO2 leakage that can occur with cytoplasmic CA plus energy-coupled transport. (scott2024widespreaddissolvedinorganic pages 1-2, scott2024widespreaddissolvedinorganic pages 10-13)

#### 5.2 Biogeochemical interaction insight: NO as a potent inhibitor of photoferrotrophy (2024)
Nikeleit et al. (2024) provide a mechanistic coupling between nitrogen cycling and phototrophic Fe(II) oxidation: nitrate-reducing Fe(II) oxidizers generate reactive nitrogen intermediates, especially NO, which can inhibit photoferrotrophs even when genomes encode NO detox genes (norV/norB/hmpA). This supports adding an **inhibitor module** (NO) and an **uncertain mitigation module** (NO detox genes) to the photolithoautotrophic causal graph—especially for ferruginous habitat context. (nikeleit2024inhibitionofphototrophic pages 3-4, nikeleit2024inhibitionofphototrophic pages 1-2, nikeleit2024inhibitionofphototrophic media 262710d9)

#### 5.3 Biotechnology and “rewiring” perspective (2023)
Lawrence et al. (2023) consolidates reaction-center types, redox potentials, and donor/acceptor modules in phototroph electron transport and explicitly identifies reduced sulfur donors (sulfide, thiosulfate) and enzymes (SQR, SoxAX) that connect lithotrophic sulfur oxidation to electron transport and NADPH generation, enabling mechanistic mapping to CO2 fixation and to electrochemical device interfacing (rewiring). (lawrence2023rewiringphotosyntheticelectron pages 4-7)

#### 5.4 Artificial/engineered photolithoautotrophy analogs (2023)
Tu et al. (2023) demonstrate a synthetic route to light-enabled CO2 fixation in a non-photosynthetic chemolithoautotroph by combining an **extracellular electron uptake conduit (MtrCAB)** with a **light-driven proton pump (Gloeobacter rhodopsin)** to overcome thermodynamic constraints in regenerating NAD(P)H. This is conceptually useful for trait mechanism graphs as an “existence proof” of module composability, but should be curated as engineered and host-specific. (tu2023engineeringartificialphotosynthesis pages 3-4)

---

### 6) Current applications and real-world implementations (with recent statistics)

#### A) Biodesulfurization / H2S detoxification using anoxygenic photolithoautotrophs
Kushkevych et al. (2024) summarize multiple phototrophic desulfurization implementations and provide quantitative performance metrics:
- Synthetic biogas composition used in tests: **70% CH4, 29.5% CO2, 0.5% H2S**; biogas H2S can be **up to 3%**. (kushkevych2024anoxygenicphotosynthesiswith pages 16-17)
- In a stirred batch reactor, **complete desulfurization after 7 days**; added H2S to **1%** was removed. (kushkevych2024anoxygenicphotosynthesiswith pages 16-17)
- Reported performance ranges: **81–95% desulfurization** in a concentric-tube column; **100% removal** at influent H2S up to **286 mg L−1 h−1**, with **92–95%** converted to **elemental sulfur** in a film reactor. (kushkevych2024anoxygenicphotosynthesiswith pages 15-16)
- Light dependency/optimization: **10 kLx** more effective than **25 kLx** in one comparison. (kushkevych2024anoxygenicphotosynthesiswith pages 16-17, kushkevych2024anoxygenicphotosynthesiswith pages 15-16)

These data support nodes/edges connecting light intensity, H2S donor oxidation, sulfur product formation, and reactor performance.

#### B) Microbial electrochemical cell (MEC) couplings with phototrophic sulfur bacteria
A GSB–*Geobacter* consortium exhibited rapid light-dependent current changes: **118 ± 16 μA** in the dark, dropping to **61 ± 11 μA within 10 min** in light, interpreted as electrons being diverted into elemental sulfur production during photosynthesis rather than anode current. (kushkevych2024anoxygenicphotosynthesiswith pages 16-17)

#### C) Ferruginous environments / early-Earth analogue constraints: NO inhibition of photoferrotrophy
Nikeleit et al. (2024) provide quantitative kinetics and inhibition thresholds relevant to Fe(II)-based photolithoautotrophy:
- A model photoferrotroph (*Rhodobacter ferrooxidans* SW2) oxidized **10 mM Fe(II)** in **28 days** with **1 mM NO3−** (NO3− unchanged). (nikeleit2024inhibitionofphototrophic pages 2-3)
- A nitrate-reducing Fe(II)-oxidizing enrichment reduced **1 mM NO3−** in ~**4 days** while oxidizing ~**5 mM Fe(II)**; in mixed culture, phototrophic Fe(II) oxidation ceased after ~**4–5 mM** Fe(II) was consumed (inhibition). (nikeleit2024inhibitionofphototrophic pages 2-3)
- NO sensitivity: complete inhibition reported at **6.2 μM NO**, and modelling/assays describe suppression at **12 nM** (parameter used for inhibition). (nikeleit2024inhibitionofphototrophic pages 3-4, nikeleit2024inhibitionofphototrophic pages 9-11)

These provide curation-ready quantitative edges linking NO exposure to decreased photoferrotrophic activity.

#### D) Engineered carbon capture / photoelectroautotrophy (proof-of-concept)
Tu et al. (2023) report key engineering conditions and mechanistic readouts:
- Cathodic potential **−500 mV (Ag/AgCl)**; **20 mM nitrate** pulse as electron acceptor; rhodopsin light absorption around **530 nm**; GR detected in **87%** induced cells; light-driven CO2 assimilation assessed at single-cell scale (n ≈ 294). (tu2023engineeringartificialphotosynthesis pages 3-4)
A related 2024 dissertation reports additional quantitative performance for rhodopsin-based photoelectrosynthesis (useful but non-peer-reviewed relative to the 2023 paper): **45%** maximum electron transfer efficiency for CO2-to-biomass conversion, and in a separate hydrogen production configuration **80.4 μmol H2 mg−1 protein day−1** with **80% Faradaic efficiency** at **−0.75 V vs SHE**. (tu2024engineeringrhodopsinbasedartificial pages 9-14)

---

### 7) Warnings / claims not yet suitable for TraitMech curation

1. **Engineered rhodopsin photoelectrosynthesis modules (MtrCAB + rhodopsin)** should be curated as **uncertain** for the *natural* photolithoautotrophic trait, unless the knowledge graph explicitly includes engineered analogs as mechanistic exemplars; they are nonetheless useful for proposing modular edges between light-driven ion pumping, electron transport, NAD(P)H generation, and CO2 fixation. (tu2023engineeringartificialphotosynthesis pages 3-4)
2. **NO detox genes as protection**: Nikeleit et al. emphasize susceptibility “despite” detox gene capacity; therefore, edges like “norV mitigates NO inhibition” should be treated as hypothesis-level or context-dependent rather than universal. (nikeleit2024inhibitionofphototrophic pages 1-2, nikeleit2024inhibitionofphototrophic media 262710d9)
3. **Taxon specificity:** Chlorosomes (GSB) and rTCA fixation are not universal across photolithoautotrophs; CBB + carboxysomes are likewise not universal. Prefer representing these as alternative branches under photolithoautotrophy conditioned on taxa/habitat. (kushkevych2024anoxygenicphotosynthesiswith pages 1-2, scott2024widespreaddissolvedinorganic pages 2-4)

---

## DOI-first bibliography (2023–2024 prioritized)

1. Nikeleit V, et al. **Inhibition of phototrophic iron oxidation by nitric oxide in ferruginous environments.** *Nature Geoscience* (Oct 2024). https://doi.org/10.1038/s41561-024-01560-9 (nikeleit2024inhibitionofphototrophic pages 2-3, nikeleit2024inhibitionofphototrophic pages 3-4, nikeleit2024inhibitionofphototrophic pages 1-2)
2. Scott KM, Payne RR, Gahramanova A. **Widespread dissolved inorganic carbon-modifying toolkits in genomes of autotrophic Bacteria and Archaea…** *Applied and Environmental Microbiology* (Feb 2024). https://doi.org/10.1128/aem.01557-23 (scott2024widespreaddissolvedinorganic pages 2-4, scott2024widespreaddissolvedinorganic pages 1-2)
3. Kushkevych I, et al. **Anoxygenic photosynthesis with emphasis on green sulfur bacteria and a perspective for hydrogen sulfide detoxification of anoxic environments.** *Frontiers in Microbiology* (Jul 2024). https://doi.org/10.3389/fmicb.2024.1417714 (kushkevych2024anoxygenicphotosynthesiswith pages 1-2, kushkevych2024anoxygenicphotosynthesiswith pages 16-17)
4. Tu W, Xu J, Thompson IP, Huang WE. **Engineering artificial photosynthesis based on rhodopsin for CO2 fixation.** *Nature Communications* (Dec 2023). https://doi.org/10.1038/s41467-023-43524-4 (tu2023engineeringartificialphotosynthesis pages 3-4)
5. Lawrence JM, et al. **Rewiring photosynthetic electron transport chains for solar energy conversion.** *Nature Reviews Bioengineering* (Aug 2023). https://doi.org/10.1038/s44222-023-00093-x (lawrence2023rewiringphotosyntheticelectron pages 4-7)

Additional (non-journal, use cautiously):
- Tu W. **Engineering rhodopsin-based artificial photosynthesis.** Dissertation (Jan 2024). https://doi.org/10.5287/ora-8jgz2nrvd (tu2024engineeringrhodopsinbasedartificial pages 9-14)


References

1. (kushkevych2024anoxygenicphotosynthesiswith pages 1-2): Ivan Kushkevych, Vít Procházka, Monika Vítězová, Dani Dordević, Mohamed Abd El-Salam, and Simon K.-M. R. Rittmann. Anoxygenic photosynthesis with emphasis on green sulfur bacteria and a perspective for hydrogen sulfide detoxification of anoxic environments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1417714, doi:10.3389/fmicb.2024.1417714. This article has 24 citations and is from a peer-reviewed journal.

2. (tu2024engineeringrhodopsinbasedartificial pages 21-24): Engineering rhodopsin-based artificial photosynthesis This article has 0 citations.

3. (tu2023engineeringartificialphotosynthesis pages 3-4): Weiming Tu, Jiabao Xu, Ian P. Thompson, and Wei E. Huang. Engineering artificial photosynthesis based on rhodopsin for co2 fixation. Nature Communications, Dec 2023. URL: https://doi.org/10.1038/s41467-023-43524-4, doi:10.1038/s41467-023-43524-4. This article has 68 citations and is from a highest quality peer-reviewed journal.

4. (tu2024engineeringrhodopsinbasedartificial pages 51-55): Engineering rhodopsin-based artificial photosynthesis This article has 0 citations.

5. (scott2024widespreaddissolvedinorganic pages 2-4): Kathleen M. Scott, Ren R. Payne, and Arin Gahramanova. Widespread dissolved inorganic carbon-modifying toolkits in genomes of autotrophic <i>bacteria</i> and <i>archaea</i> and how they are likely to bridge supply from the environment to demand by autotrophic pathways. Applied and Environmental Microbiology, Feb 2024. URL: https://doi.org/10.1128/aem.01557-23, doi:10.1128/aem.01557-23. This article has 7 citations and is from a peer-reviewed journal.

6. (lawrence2023rewiringphotosyntheticelectron pages 4-7): Joshua M. Lawrence, Rachel M. Egan, Thomas Hoefer, Alberto Scarampi, Linying Shang, Christopher J. Howe, and Jenny Z. Zhang. Rewiring photosynthetic electron transport chains for solar energy conversion. Nature Reviews Bioengineering, 1:887-905, Aug 2023. URL: https://doi.org/10.1038/s44222-023-00093-x, doi:10.1038/s44222-023-00093-x. This article has 52 citations and is from a peer-reviewed journal.

7. (scott2024widespreaddissolvedinorganic pages 1-2): Kathleen M. Scott, Ren R. Payne, and Arin Gahramanova. Widespread dissolved inorganic carbon-modifying toolkits in genomes of autotrophic <i>bacteria</i> and <i>archaea</i> and how they are likely to bridge supply from the environment to demand by autotrophic pathways. Applied and Environmental Microbiology, Feb 2024. URL: https://doi.org/10.1128/aem.01557-23, doi:10.1128/aem.01557-23. This article has 7 citations and is from a peer-reviewed journal.

8. (scott2024widespreaddissolvedinorganic pages 4-7): Kathleen M. Scott, Ren R. Payne, and Arin Gahramanova. Widespread dissolved inorganic carbon-modifying toolkits in genomes of autotrophic <i>bacteria</i> and <i>archaea</i> and how they are likely to bridge supply from the environment to demand by autotrophic pathways. Applied and Environmental Microbiology, Feb 2024. URL: https://doi.org/10.1128/aem.01557-23, doi:10.1128/aem.01557-23. This article has 7 citations and is from a peer-reviewed journal.

9. (scott2024widespreaddissolvedinorganic pages 10-13): Kathleen M. Scott, Ren R. Payne, and Arin Gahramanova. Widespread dissolved inorganic carbon-modifying toolkits in genomes of autotrophic <i>bacteria</i> and <i>archaea</i> and how they are likely to bridge supply from the environment to demand by autotrophic pathways. Applied and Environmental Microbiology, Feb 2024. URL: https://doi.org/10.1128/aem.01557-23, doi:10.1128/aem.01557-23. This article has 7 citations and is from a peer-reviewed journal.

10. (nikeleit2024inhibitionofphototrophic pages 1-2): Verena Nikeleit, Adrian Mellage, Giorgio Bianchini, Lea Sauter, Steffen Buessecker, Stefanie Gotterbarm, Manuel Schad, Kurt Konhauser, Aubrey L. Zerkle, Patricia Sánchez-Baracaldo, Andreas Kappler, and Casey Bryce. Inhibition of phototrophic iron oxidation by nitric oxide in ferruginous environments. Nature Geoscience, 17:1169-1174, Oct 2024. URL: https://doi.org/10.1038/s41561-024-01560-9, doi:10.1038/s41561-024-01560-9. This article has 2 citations and is from a highest quality peer-reviewed journal.

11. (nikeleit2024inhibitionofphototrophic pages 3-4): Verena Nikeleit, Adrian Mellage, Giorgio Bianchini, Lea Sauter, Steffen Buessecker, Stefanie Gotterbarm, Manuel Schad, Kurt Konhauser, Aubrey L. Zerkle, Patricia Sánchez-Baracaldo, Andreas Kappler, and Casey Bryce. Inhibition of phototrophic iron oxidation by nitric oxide in ferruginous environments. Nature Geoscience, 17:1169-1174, Oct 2024. URL: https://doi.org/10.1038/s41561-024-01560-9, doi:10.1038/s41561-024-01560-9. This article has 2 citations and is from a highest quality peer-reviewed journal.

12. (nikeleit2024inhibitionofphototrophic pages 9-11): Verena Nikeleit, Adrian Mellage, Giorgio Bianchini, Lea Sauter, Steffen Buessecker, Stefanie Gotterbarm, Manuel Schad, Kurt Konhauser, Aubrey L. Zerkle, Patricia Sánchez-Baracaldo, Andreas Kappler, and Casey Bryce. Inhibition of phototrophic iron oxidation by nitric oxide in ferruginous environments. Nature Geoscience, 17:1169-1174, Oct 2024. URL: https://doi.org/10.1038/s41561-024-01560-9, doi:10.1038/s41561-024-01560-9. This article has 2 citations and is from a highest quality peer-reviewed journal.

13. (nikeleit2024inhibitionofphototrophic media 262710d9): Verena Nikeleit, Adrian Mellage, Giorgio Bianchini, Lea Sauter, Steffen Buessecker, Stefanie Gotterbarm, Manuel Schad, Kurt Konhauser, Aubrey L. Zerkle, Patricia Sánchez-Baracaldo, Andreas Kappler, and Casey Bryce. Inhibition of phototrophic iron oxidation by nitric oxide in ferruginous environments. Nature Geoscience, 17:1169-1174, Oct 2024. URL: https://doi.org/10.1038/s41561-024-01560-9, doi:10.1038/s41561-024-01560-9. This article has 2 citations and is from a highest quality peer-reviewed journal.

14. (scott2024widespreaddissolvedinorganic pages 7-10): Kathleen M. Scott, Ren R. Payne, and Arin Gahramanova. Widespread dissolved inorganic carbon-modifying toolkits in genomes of autotrophic <i>bacteria</i> and <i>archaea</i> and how they are likely to bridge supply from the environment to demand by autotrophic pathways. Applied and Environmental Microbiology, Feb 2024. URL: https://doi.org/10.1128/aem.01557-23, doi:10.1128/aem.01557-23. This article has 7 citations and is from a peer-reviewed journal.

15. (nikeleit2024inhibitionofphototrophic pages 17-17): Verena Nikeleit, Adrian Mellage, Giorgio Bianchini, Lea Sauter, Steffen Buessecker, Stefanie Gotterbarm, Manuel Schad, Kurt Konhauser, Aubrey L. Zerkle, Patricia Sánchez-Baracaldo, Andreas Kappler, and Casey Bryce. Inhibition of phototrophic iron oxidation by nitric oxide in ferruginous environments. Nature Geoscience, 17:1169-1174, Oct 2024. URL: https://doi.org/10.1038/s41561-024-01560-9, doi:10.1038/s41561-024-01560-9. This article has 2 citations and is from a highest quality peer-reviewed journal.

16. (nikeleit2024inhibitionofphototrophic pages 4-5): Verena Nikeleit, Adrian Mellage, Giorgio Bianchini, Lea Sauter, Steffen Buessecker, Stefanie Gotterbarm, Manuel Schad, Kurt Konhauser, Aubrey L. Zerkle, Patricia Sánchez-Baracaldo, Andreas Kappler, and Casey Bryce. Inhibition of phototrophic iron oxidation by nitric oxide in ferruginous environments. Nature Geoscience, 17:1169-1174, Oct 2024. URL: https://doi.org/10.1038/s41561-024-01560-9, doi:10.1038/s41561-024-01560-9. This article has 2 citations and is from a highest quality peer-reviewed journal.

17. (kushkevych2024anoxygenicphotosynthesiswith pages 16-17): Ivan Kushkevych, Vít Procházka, Monika Vítězová, Dani Dordević, Mohamed Abd El-Salam, and Simon K.-M. R. Rittmann. Anoxygenic photosynthesis with emphasis on green sulfur bacteria and a perspective for hydrogen sulfide detoxification of anoxic environments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1417714, doi:10.3389/fmicb.2024.1417714. This article has 24 citations and is from a peer-reviewed journal.

18. (lawrence2023rewiringphotosyntheticelectron pages 9-11): Joshua M. Lawrence, Rachel M. Egan, Thomas Hoefer, Alberto Scarampi, Linying Shang, Christopher J. Howe, and Jenny Z. Zhang. Rewiring photosynthetic electron transport chains for solar energy conversion. Nature Reviews Bioengineering, 1:887-905, Aug 2023. URL: https://doi.org/10.1038/s44222-023-00093-x, doi:10.1038/s44222-023-00093-x. This article has 52 citations and is from a peer-reviewed journal.

19. (scott2024widespreaddissolvedinorganic pages 13-15): Kathleen M. Scott, Ren R. Payne, and Arin Gahramanova. Widespread dissolved inorganic carbon-modifying toolkits in genomes of autotrophic <i>bacteria</i> and <i>archaea</i> and how they are likely to bridge supply from the environment to demand by autotrophic pathways. Applied and Environmental Microbiology, Feb 2024. URL: https://doi.org/10.1128/aem.01557-23, doi:10.1128/aem.01557-23. This article has 7 citations and is from a peer-reviewed journal.

20. (scott2024widespreaddissolvedinorganic pages 15-18): Kathleen M. Scott, Ren R. Payne, and Arin Gahramanova. Widespread dissolved inorganic carbon-modifying toolkits in genomes of autotrophic <i>bacteria</i> and <i>archaea</i> and how they are likely to bridge supply from the environment to demand by autotrophic pathways. Applied and Environmental Microbiology, Feb 2024. URL: https://doi.org/10.1128/aem.01557-23, doi:10.1128/aem.01557-23. This article has 7 citations and is from a peer-reviewed journal.

21. (nikeleit2024inhibitionofphototrophic pages 2-3): Verena Nikeleit, Adrian Mellage, Giorgio Bianchini, Lea Sauter, Steffen Buessecker, Stefanie Gotterbarm, Manuel Schad, Kurt Konhauser, Aubrey L. Zerkle, Patricia Sánchez-Baracaldo, Andreas Kappler, and Casey Bryce. Inhibition of phototrophic iron oxidation by nitric oxide in ferruginous environments. Nature Geoscience, 17:1169-1174, Oct 2024. URL: https://doi.org/10.1038/s41561-024-01560-9, doi:10.1038/s41561-024-01560-9. This article has 2 citations and is from a highest quality peer-reviewed journal.

22. (kushkevych2024anoxygenicphotosynthesiswith pages 15-16): Ivan Kushkevych, Vít Procházka, Monika Vítězová, Dani Dordević, Mohamed Abd El-Salam, and Simon K.-M. R. Rittmann. Anoxygenic photosynthesis with emphasis on green sulfur bacteria and a perspective for hydrogen sulfide detoxification of anoxic environments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1417714, doi:10.3389/fmicb.2024.1417714. This article has 24 citations and is from a peer-reviewed journal.

23. (tu2024engineeringrhodopsinbasedartificial pages 9-14): Engineering rhodopsin-based artificial photosynthesis This article has 0 citations.