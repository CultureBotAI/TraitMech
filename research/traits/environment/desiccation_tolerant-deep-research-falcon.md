---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T21:46:38.948144'
end_time: '2026-06-17T22:06:32.453351'
duration_seconds: 1193.51
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: desiccation tolerant
  trait_identifier: traitmech:000010
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: desiccation_tolerant
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: An environmental tolerance in which an organism survives extreme water
    loss and resumes growth after rehydration (anhydrobiosis), protecting cellular
    macromolecules during drying.
  parent_traits: METPO:1000059
  synonyms: anhydrobiotic
  evidence_summary: 'DOI:10.3390/microorganisms10020432: Anhydrobiosis (gr. life without
    water) is predominantly described as the ability of some organisms to lose all
    or almost all water and enter a state of suspension where the metabolism comes
    to a reversible standstill (Bacterial anhydrobiosis review supports desiccation
    tolerance as reversible survival of near-complete water loss.) | DOI:10.3390/genes14091803:
    Deinococcus radiodurans, a Gram-positive extremophilic bacterium, is a remarkable
    example of such an organism, showcasing an impressive resistance to a wide array
    of stressors, including ionizing radiation, desiccation, UV radiation, and oxidizing
    agents (Organism example: Deinococcus radiodurans is desiccation-tolerant, sharing
    DNA-repair machinery with its radiation tolerance.)'
  causal_graph_summary: 'desiccation_anhydrobiosis_repair: 4 nodes, 3 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 59
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** desiccation tolerant
- **METPO identifier:** traitmech:000010
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An environmental tolerance in which an organism survives extreme water loss and resumes growth after rehydration (anhydrobiosis), protecting cellular macromolecules during drying.
- **Parent traits:** METPO:1000059
- **Synonyms:** anhydrobiotic
- **Existing evidence:** DOI:10.3390/microorganisms10020432: Anhydrobiosis (gr. life without water) is predominantly described as the ability of some organisms to lose all or almost all water and enter a state of suspension where the metabolism comes to a reversible standstill (Bacterial anhydrobiosis review supports desiccation tolerance as reversible survival of near-complete water loss.) | DOI:10.3390/genes14091803: Deinococcus radiodurans, a Gram-positive extremophilic bacterium, is a remarkable example of such an organism, showcasing an impressive resistance to a wide array of stressors, including ionizing radiation, desiccation, UV radiation, and oxidizing agents (Organism example: Deinococcus radiodurans is desiccation-tolerant, sharing DNA-repair machinery with its radiation tolerance.)
- **Existing causal graph summary:** desiccation_anhydrobiosis_repair: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **desiccation tolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/desiccation_tolerant.yaml`.

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
- **Trait label:** desiccation tolerant
- **METPO identifier:** traitmech:000010
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An environmental tolerance in which an organism survives extreme water loss and resumes growth after rehydration (anhydrobiosis), protecting cellular macromolecules during drying.
- **Parent traits:** METPO:1000059
- **Synonyms:** anhydrobiotic
- **Existing evidence:** DOI:10.3390/microorganisms10020432: Anhydrobiosis (gr. life without water) is predominantly described as the ability of some organisms to lose all or almost all water and enter a state of suspension where the metabolism comes to a reversible standstill (Bacterial anhydrobiosis review supports desiccation tolerance as reversible survival of near-complete water loss.) | DOI:10.3390/genes14091803: Deinococcus radiodurans, a Gram-positive extremophilic bacterium, is a remarkable example of such an organism, showcasing an impressive resistance to a wide array of stressors, including ionizing radiation, desiccation, UV radiation, and oxidizing agents (Organism example: Deinococcus radiodurans is desiccation-tolerant, sharing DNA-repair machinery with its radiation tolerance.)
- **Existing causal graph summary:** desiccation_anhydrobiosis_repair: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **desiccation tolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/desiccation_tolerant.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **Desiccation tolerant / anhydrobiotic** (TraitMech:000010)

### 1) Scope summary (trait definition, assays, boundary cases)

**Trait meaning (curation target).** *Desiccation tolerance* (DT; often discussed with *anhydrobiosis*) is the capacity to **survive extreme drying to near-complete water loss, enter a reversible metabolically quiescent state, and resume activity/growth after rehydration**. A commonly used operational threshold for “true” DT is survival after drying to **≤0.1 g H\_2O per g dry mass** (≈ air-dryness at ~50% relative humidity, 20 °C; water potential ≤ −100 MPa), where remaining water is insufficient for essential hydration layers required for enzymatic activity. (romeroperez2023whenphasedwithout pages 3-4, romeroperez2023whenphasedwithout pages 2-3)

**Assay readouts used in the literature (microbe-relevant).** Typical measurements include: (i) **viable colony counts / survival fraction** after desiccation–rehydration; (ii) **return to growth/metabolic activity** after rewetting; (iii) damage markers such as **protein carbonylation** (oxidative damage), membrane leakage, and (in some systems) DNA damage repair readouts. DT often requires **priming/acclimation via gradual drying**; without it, many organisms fail to recover. (romeroperez2023whenphasedwithout pages 3-4, sek2023physiologicalandgenetic pages 4-6)

**Boundary cases and nearby traits.**
- **Osmotic stress tolerance**: dehydration via increased external osmolarity can overlap mechanistically but is not equivalent to DT because cells may remain metabolically active and do not necessarily reach the extreme water contents of anhydrobiosis. (romeroperez2023whenphasedwithout pages 2-3, sek2023physiologicalandgenetic pages 4-6)
- **Xerotolerance/xerophily**: growth at low water activity is distinct from the ability to dry to near-complete water loss and later resume growth. (romeroperez2023whenphasedwithout pages 2-3)
- **Dormancy/sporulation/cysts**: these are strategies that can create desiccation-resistant propagules; however, TraitMech:000010 should be curated as **the phenotype of reversible survival of extreme dehydration** (including vegetative-cell anhydrobiosis when present) rather than conflating it with developmental dormancy. (romeroperez2023whenphasedwithout pages 3-4, romeroperez2023whenphasedwithout pages 2-3)

### 2) Current understanding: key mechanistic concepts (2023–2024 emphasis)

#### 2.1 Core stressors produced by drying
Extreme water loss increases intracellular crowding/viscosity and perturbs macromolecular interactions; expected damage includes **membrane destabilization, protein denaturation/aggregation, and oxidative stress**. DT-capable systems can nonetheless recover after rehydration. (romeroperez2023whenphasedwithout pages 3-4, romeroperez2023whenphasedwithout pages 2-3)

A prominent, conserved feature is **enhanced oxidative-stress defense**, including upregulation of **SOD, catalases, glutathione peroxidases/reductases** and accumulation of antioxidants such as **glutathione and ascorbate**. Entry into dormancy with reduced respiration can also limit ROS production. (romeroperez2023whenphasedwithout pages 3-4)

#### 2.2 Major protective strategies (entities relevant for TraitMech graphs)

1) **Compatible solutes & chemical chaperones**
- In yeast, **trehalose** stabilizes membranes by interacting with phospholipid polar groups; compatible solutes/antioxidants include **glycerol** and **glutathione**. (sek2023physiologicalandgenetic pages 4-6)
- Yeast regulatory logic includes activation of trehalose synthase and inhibition of trehalase; trehalose/glycogen metabolism is integrated with signaling (e.g., cAMP, Snf1). (sek2023physiologicalandgenetic pages 10-11)

2) **Proteostasis via chaperones/heat shock proteins (HSPs)**
Heat shock proteins act as chaperones to prevent aggregation and aid repair upon rehydration in yeast anhydrobiosis. (sek2023physiologicalandgenetic pages 4-6)

3) **Intrinsically disordered proteins (IDPs) and materials biology of the dry cytoplasm**
Recent mechanistic work emphasizes IDPs (including **LEA** and **CAHS** families) and their interactions with **endogenous cosolutes** (trehalose/sucrose). In 2024, KC et al. show that desiccation-related IDPs **synergize best with endogenous cosolutes during drying**, and for CAHS proteins this synergy relates to **self-assembly/gel formation**. (kc2024disorderedproteinsinteract pages 1-2)

4) **Non-enzymatic antioxidant systems and metal homeostasis (Deinococcus paradigm)**
A mechanistic theme in radiation- and desiccation-resistant bacteria is **Mn(II)-metabolite antioxidant complexes** and an elevated **Mn/Fe ratio** that protect the proteome (including enzymes required for DNA repair) against ROS-driven oxidation. (abbaszadeh2024theecologyand pages 24-28, rai2024anovelionizing pages 13-14)

5) **Extracellular polymeric substances (EPS) and microenvironmental hydration**
In dryland systems, cyanobacteria and other microbes produce **EPS** that retain water and can delay desiccation, sustaining community activity during drying. (baubin2023divergenceofbiocrust pages 1-4)
Cyanobacterial EPS also provides a matrix for UV-protective pigments and can exhibit redox-active functional groups, linking EPS to oxidative/UV stress buffering in exposed environments. (silva2024cyanobacterialandmicroalgae pages 3-4, irankhahi2024theroleof pages 1-2)

### 3) Recent developments and latest research (prioritizing 2023–2024)

**(A) 2024 eLife: IDP–cosolute synergy and CAHS gelation as a tunable mechanism.** KC et al. (2024) provide a modern mechanistic framework: protection by LEA/CAHS-like IDPs is not purely intrinsic to the proteins but depends on the **chemical environment** and **cosolute context**; CAHS (but not all LEA proteins) shows synergy tied to **self-assembly and gel formation**. This points to a *design rule* for curating causal edges linking cosolute accumulation → IDP conformational/assembly changes → protection. (kc2024disorderedproteinsinteract pages 1-2)

**(B) 2024 AEM: regulatory sRNA DrsS connecting metal homeostasis and catalase activity.** Rai & Dutta (2024) identify **DrsS**, a stress-induced sRNA in *Deinococcus radiodurans*. drsS deletion decreased intracellular **Mn\*\*2+\*\*** (~70%) and **Fe\*\*2+\*\*** (~40%) with increased protein carbonylation; DrsS binds the **katA** transcript and supports **catalase-mediated ROS detoxification**. This provides a concrete, gene-regulatory edge for oxidative protection networks relevant to shared desiccation/radiation resistance. (rai2024anovelionizing pages 1-3)

**(C) 2023–2024 Chemical Reviews: unifying molecular biophysics of desiccation with condensates and glasses.** The Chemical Reviews synthesis highlights that desiccation tolerance is defined at extreme dryness thresholds and stresses the roles of **IDPs, vitrification/glassy matrices, and biomolecular condensates** as conceptual pillars for mechanistic graphs linking water loss → biophysical phase changes → protection and recovery. (romeroperez2023whenphasedwithout pages 3-4, olgenblum2024protectingproteinsfrom pages 2-3)

**(D) 2024 cyanobacterial EPS work: quantified EPS pools and stress phenotypes.** Irankhahi et al. (2024) report capsule polysaccharide (CPS) and released polysaccharide (RPS) quantities in Nostoc (~681.8 mg/L CPS and ~470.2 mg/L RPS) and show that UV resistance correlates strongly with scytonemin/pigmentation rather than induced EPS quantity, highlighting a boundary: EPS presence/structure can matter even when quantity is unchanged. (irankhahi2024theroleof pages 6-7)

### 4) Candidate nodes (ontology grounding suggestions)

| Type | Node label | Suggested grounding/CURIE | Rationale/evidence (1 sentence) | Key references (DOI, year, URL) |
|---|---|---|---|---|
| Environmental/assay factor | Relative humidity | ENVO candidate (label-only) | Air-dry desiccation tolerance is operationalized around ~50% RH at 20°C, corresponding to extreme low-water conditions compatible with anhydrobiosis assays (romeroperez2023whenphasedwithout pages 3-4). | 10.1021/acs.chemrev.2c00659, 2023, https://doi.org/10.1021/acs.chemrev.2c00659 |
| Environmental/assay factor | Water potential | ENVO candidate (label-only) | Desiccation-tolerant states are often defined below water potential ≤ −100 MPa, a threshold where hydration monolayers become insufficient for normal enzymatic activity (romeroperez2023whenphasedwithout pages 3-4). | 10.1021/acs.chemrev.2c00659, 2023, https://doi.org/10.1021/acs.chemrev.2c00659 |
| Environmental/assay factor | Drying rate / gradual drying priming | label-only candidate | Gradual drying or acclimation frequently determines whether cells survive desiccation, making drying rate a critical assay variable (romeroperez2023whenphasedwithout pages 3-4, sek2023physiologicalandgenetic pages 1-3). | 10.1021/acs.chemrev.2c00659, 2023, https://doi.org/10.1021/acs.chemrev.2c00659; 10.1007/s00203-023-03683-w, 2023, https://doi.org/10.1007/s00203-023-03683-w |
| Environmental/assay factor | Rehydration temperature | label-only candidate | Recovery depends strongly on rehydration conditions, and yeast dry-cell protocols recommend 35–40 °C rehydration to improve viability (sek2023physiologicalandgenetic pages 1-3). | 10.1007/s00203-023-03683-w, 2023, https://doi.org/10.1007/s00203-023-03683-w |
| Process | Anhydrobiosis / desiccation tolerance | METPO:traitmech:000010; GO candidate (label-only) | The core phenotype is reversible metabolic arrest after near-complete water loss followed by return to activity after rehydration (romeroperez2023whenphasedwithout pages 2-3, olgenblum2024protectingproteinsfrom pages 2-3). | 10.1021/acs.chemrev.2c00659, 2023, https://doi.org/10.1021/acs.chemrev.2c00659; 10.1021/acs.chemrev.3c00752, 2024, https://doi.org/10.1021/acs.chemrev.3c00752 |
| Process | Vitrification / molecular glass formation | label-only candidate | Molecular glasses are a major protective mechanism proposed to reduce molecular motion and preserve biomolecules in the dry state (olgenblum2024protectingproteinsfrom pages 2-3, packebush2023naturalandengineered pages 1-2). | 10.1021/acs.chemrev.3c00752, 2024, https://doi.org/10.1021/acs.chemrev.3c00752; 10.1038/s41598-023-31586-9, 2023, https://doi.org/10.1038/s41598-023-31586-9 |
| Process | Oxidative stress response | GO:0006979 | Oxidative stress defense is one of the most conserved responses in desiccation tolerance, with antioxidant enzymes and metabolites repeatedly upregulated (romeroperez2023whenphasedwithout pages 3-4, sek2023physiologicalandgenetic pages 4-6). | 10.1021/acs.chemrev.2c00659, 2023, https://doi.org/10.1021/acs.chemrev.2c00659; 10.1007/s00203-023-03683-w, 2023, https://doi.org/10.1007/s00203-023-03683-w |
| Process | Protein folding / chaperone-mediated proteostasis | GO:0006457; GO:0051082 | Chaperones and heat-shock proteins limit desiccation-induced denaturation and aggregation and assist repair upon rehydration (sek2023physiologicalandgenetic pages 4-6, sek2023physiologicalandgenetic pages 1-3). | 10.1007/s00203-023-03683-w, 2023, https://doi.org/10.1007/s00203-023-03683-w |
| Process | Autophagy / lipophagy | GO:0006914; GO candidate for lipophagy | Autophagy and lipophagy are implicated in recycling and stress adaptation during anhydrobiosis, especially alongside lipid-droplet remodeling (sek2023physiologicalandgenetic pages 10-11). | 10.1007/s00203-023-03683-w, 2023, https://doi.org/10.1007/s00203-023-03683-w |
| Process | Biomolecular condensates / phase separation | GO candidate (label-only) | Recent biophysical models propose that condensates and phase behavior help sequester or protect cellular machinery during drying (romeroperez2023whenphasedwithout pages 1-2, romeroperez2023whenphasedwithout pages 17-18). | 10.1021/acs.chemrev.2c00659, 2023, https://doi.org/10.1021/acs.chemrev.2c00659 |
| Metabolite | Trehalose | CHEBI:16551 | Trehalose is a central desiccation protectant that stabilizes membranes and proteins and participates in vitrification-like protection (sek2023physiologicalandgenetic pages 4-6, packebush2023naturalandengineered pages 1-2). | 10.1007/s00203-023-03683-w, 2023, https://doi.org/10.1007/s00203-023-03683-w; 10.1038/s41598-023-31586-9, 2023, https://doi.org/10.1038/s41598-023-31586-9 |
| Metabolite | Sucrose | CHEBI:17992 | Sucrose functions as a compatible cosolute/protectant and can preserve dry-state biomolecular activity similarly to trehalose in applied desiccation systems (kc2024disorderedproteinsinteract pages 1-2, packebush2023naturalandengineered pages 3-4). | 10.7554/eLife.97231, 2024, https://doi.org/10.7554/eLife.97231; 10.1038/s41598-023-31586-9, 2023, https://doi.org/10.1038/s41598-023-31586-9 |
| Metabolite | Glycerol | CHEBI:17754 | Glycerol is produced early during dehydration and is part of the compatible-solute response associated with anhydrobiotic preparation (sek2023physiologicalandgenetic pages 10-11, sek2023physiologicalandgenetic pages 4-6). | 10.1007/s00203-023-03683-w, 2023, https://doi.org/10.1007/s00203-023-03683-w |
| Metabolite | Glutathione | CHEBI:16856 | Glutathione is a major intracellular antioxidant whose elevated production is linked to improved survival after drying and rehydration (sek2023physiologicalandgenetic pages 10-11, romeroperez2023whenphasedwithout pages 3-4). | 10.1007/s00203-023-03683-w, 2023, https://doi.org/10.1007/s00203-023-03683-w; 10.1021/acs.chemrev.2c00659, 2023, https://doi.org/10.1021/acs.chemrev.2c00659 |
| Metabolite | Ascorbate | CHEBI:22652 | Ascorbate is cited among small-molecule antioxidants accumulated in desiccation-tolerant systems as part of oxidative-stress defense (romeroperez2023whenphasedwithout pages 3-4). | 10.1021/acs.chemrev.2c00659, 2023, https://doi.org/10.1021/acs.chemrev.2c00659 |
| Metabolite | Ergosterol | CHEBI:18157 | Ergosterol is highlighted in yeast as a membrane-stabilizing sterol associated with survival of dehydration stress (sek2023physiologicalandgenetic pages 4-6). | 10.1007/s00203-023-03683-w, 2023, https://doi.org/10.1007/s00203-023-03683-w |
| Metabolite | Mn2+ | CHEBI:29035 | Mn2+ participates in non-enzymatic antioxidant complexes and its intracellular abundance/homeostasis correlates with protection of proteins in stress-resistant bacteria (abbaszadeh2024theecologyand pages 24-28, rai2024anovelionizing pages 1-3). | 10.1128/aem.01538-23, 2024, https://doi.org/10.1128/aem.01538-23 |
| Metabolite | Fe2+ | CHEBI:29033 | Fe2+ balance relative to Mn2+ is mechanistically relevant because lower effective iron burden reduces Fenton-type oxidative damage in resistant bacteria (abbaszadeh2024theecologyand pages 24-28, rai2024anovelionizing pages 1-3). | 10.1128/aem.01538-23, 2024, https://doi.org/10.1128/aem.01538-23 |
| Metabolite | Scytonemin | CHEBI candidate (label-only) | In cyanobacteria, scytonemin accumulates in the extracellular matrix and helps form a protective shield against UV-associated oxidative stress in exposed dry habitats (irankhahi2024theroleof pages 1-2, irankhahi2024theroleof pages 6-7). | 10.1038/s41598-024-70002-8, 2024, https://doi.org/10.1038/s41598-024-70002-8 |
| Metabolite | EPS polysaccharides / extracellular polysaccharides | CHEBI:18154 polysaccharide; GO:0030312 external encapsulating structure | EPS retains water, creates a hydrated barrier, and can delay local desiccation while sustaining community activity in biocrusts (silva2024cyanobacterialandmicroalgae pages 3-4, baubin2023divergenceofbiocrust pages 1-4). | 10.1007/s42770-024-01452-5, 2024, https://doi.org/10.1007/s42770-024-01452-5; 10.1007/s00248-022-02063-z, 2023, https://doi.org/10.1007/s00248-022-02063-z |
| Gene/protein | TPS1 | S. cerevisiae gene label (no universal CURIE provided here) | TPS1 is repeatedly cited as a core trehalose-biosynthesis gene contributing to yeast anhydrobiosis (sek2023physiologicalandgenetic pages 1-3, sek2023physiologicalandgenetic pages 10-11). | 10.1007/s00203-023-03683-w, 2023, https://doi.org/10.1007/s00203-023-03683-w |
| Gene/protein | TPS2 | S. cerevisiae gene label (no universal CURIE provided here) | TPS2 is paired with TPS1 in the canonical trehalose-synthesis system highlighted for desiccation protection in yeast (sek2023physiologicalandgenetic pages 1-3). | 10.1007/s00203-023-03683-w, 2023, https://doi.org/10.1007/s00203-023-03683-w |
| Gene/protein | Trehalase | EC candidate / label-only | Regulation of trehalase activity is part of the switch that favors trehalose accumulation during dehydration (sek2023physiologicalandgenetic pages 10-11). | 10.1007/s00203-023-03683-w, 2023, https://doi.org/10.1007/s00203-023-03683-w |
| Gene/protein | Superoxide dismutase (SOD) | GO:0004784; EC 1.15.1.1 | SOD is among the conserved antioxidant enzymes increased or required in desiccation-tolerant responses and shared radiation/desiccation resistance systems (romeroperez2023whenphasedwithout pages 3-4, rai2024anovelionizing pages 13-14). | 10.1021/acs.chemrev.2c00659, 2023, https://doi.org/10.1021/acs.chemrev.2c00659; 10.1128/aem.01538-23, 2024, https://doi.org/10.1128/aem.01538-23 |
| Gene/protein | Catalase / katA | GO:0004096; D. radiodurans katA label | Catalase detoxifies ROS in desiccation-related oxidative stress, and katA is directly supported as a regulated ROS-defense target in D. radiodurans (rai2024anovelionizing pages 1-3, romeroperez2023whenphasedwithout pages 3-4). | 10.1128/aem.01538-23, 2024, https://doi.org/10.1128/aem.01538-23; 10.1021/acs.chemrev.2c00659, 2023, https://doi.org/10.1021/acs.chemrev.2c00659 |
| Gene/protein | Hsp12 | S. cerevisiae protein label | Hsp12p is specifically highlighted as a yeast anhydrobiosis-associated stress protein involved in dry-state tolerance (sek2023physiologicalandgenetic pages 1-3). | 10.1007/s00203-023-03683-w, 2023, https://doi.org/10.1007/s00203-023-03683-w |
| Gene/protein | Hsp70 | GO:0006457-associated chaperone; protein family label | Hsp70 is repeatedly cited among major protective proteins induced in anhydrobiotic or desiccation-related stress responses (sek2023physiologicalandgenetic pages 1-3, sadowskabartosz2024antioxidantdefensein pages 20-21). | 10.1007/s00203-023-03683-w, 2023, https://doi.org/10.1007/s00203-023-03683-w; 10.3390/ijms25158393, 2024, https://doi.org/10.3390/ijms25158393 |
| Gene/protein | Aquaporins | GO:0015250 water channel activity | Aquaporins are implicated in controlling water flux during dehydration/rehydration and therefore influence survival outcomes (sek2023physiologicalandgenetic pages 4-6). | 10.1007/s00203-023-03683-w, 2023, https://doi.org/10.1007/s00203-023-03683-w |
| Gene/protein | LEA proteins | protein family label; GO candidate (response to water deprivation) | LEA proteins are classic disordered desiccation-related protectants that can act with sugars and other cosolutes to stabilize biomolecules during drying (kc2024disorderedproteinsinteract pages 1-2, romeroperez2023whenphasedwithout pages 17-18). | 10.7554/eLife.97231, 2024, https://doi.org/10.7554/eLife.97231; 10.1021/acs.chemrev.2c00659, 2023, https://doi.org/10.1021/acs.chemrev.2c00659 |
| Gene/protein | CAHS proteins | protein family label | CAHS proteins are heat-soluble/disordered protectants whose self-assembly and gelation are tied to dry-state protection and engineering applications (kc2024disorderedproteinsinteract pages 1-2, packebush2023naturalandengineered pages 3-4). | 10.7554/eLife.97231, 2024, https://doi.org/10.7554/eLife.97231; 10.1038/s41598-023-31586-9, 2023, https://doi.org/10.1038/s41598-023-31586-9 |
| Gene/protein | DrsS sRNA | D. radiodurans sRNA label | DrsS is a recently characterized stress-induced sRNA that stabilizes katA-linked ROS defense and helps maintain Mn/Fe homeostasis in a Deinococcus stress-resistance network (rai2024anovelionizing pages 1-3, rai2024anovelionizing pages 13-14). | 10.1128/aem.01538-23, 2024, https://doi.org/10.1128/aem.01538-23 |


*Table: This table organizes candidate nodes for a TraitMech causal graph of microbial desiccation tolerance, grouped across assay factors, processes, metabolites, and genes/proteins. It is useful for prioritizing ontology-grounded entities with recent evidence for curation.*

### 5) Evidence-backed candidate causal edges (triples)

| Subject node (suggested CURIE/grounding) | Predicate | Object node (suggested CURIE/grounding) | Evidence snippet (short quote-like excerpt) | Reference (DOI, year, URL) | Notes/uncertainty |
|---|---|---|---|---|---|
| Low water content / desiccation (ENVO:desiccation [label]) | causes/increases | Oxidative stress / ROS (GO:0006979; CHEBI:33579) | “Despite expected damage… oxidative stress” and DT organisms recover after rehydration; low hydration is below the protective water monolayer threshold (romeroperez2023whenphasedwithout pages 3-4) | 10.1021/acs.chemrev.2c00659, 2023, https://doi.org/10.1021/acs.chemrev.2c00659 | Broad, cross-kingdom review evidence; direct microbial generalization is strong but not taxon-specific. |
| Desiccation priming / acclimation (label-only candidate) | positively_regulates | Desiccation survival / rehydration recovery (METPO:traitmech:000010 [trait]) | “priming/acclimation is often necessary; without it desiccation can be lethal” (romeroperez2023whenphasedwithout pages 3-4) | 10.1021/acs.chemrev.2c00659, 2023, https://doi.org/10.1021/acs.chemrev.2c00659 | Strong review claim; curate as process-level edge rather than species-specific mechanism. |
| Trehalose (CHEBI:16551) | stabilizes | Plasma membrane / phospholipid head groups (GO:0005886; CHEBI:phospholipid [label]) | “trehalose interacts with phospholipid polar groups to stabilize membranes” (sek2023physiologicalandgenetic pages 4-6) | 10.1007/s00203-023-03683-w, 2023, https://doi.org/10.1007/s00203-023-03683-w | Primarily yeast evidence; likely broader but mechanism is clearest in yeast. |
| Trehalose (CHEBI:16551) | promotes | Vitrification / molecular glass formation (label-only candidate) | “trehalose-mediated vitrification” and “vitrification to reduce molecular motion and prevent crystallization” (packebush2023naturalandengineered pages 1-2) | 10.1038/s41598-023-31586-9, 2023, https://doi.org/10.1038/s41598-023-31586-9 | Application-focused paper; vitrification mechanism is established but not directly measured in all microbes. |
| Trehalose-6-phosphate synthase activity / TPS1-TPS2 system (GO:0004805; S. cerevisiae TPS1/TPS2 [label]) | positively_regulates | Trehalose accumulation (CHEBI:16551) | “trehalose accumulation is driven by activation of trehalose synthase and inhibition of trehalase” and review highlights “TPS1 and TPS2” (sek2023physiologicalandgenetic pages 10-11, sek2023physiologicalandgenetic pages 1-3) | 10.1007/s00203-023-03683-w, 2023, https://doi.org/10.1007/s00203-023-03683-w | Strong for yeast; exact gene grounding is taxon-specific. |
| Glutathione (CHEBI:16856) | protects_against | Oxidative stress / ROS damage (GO:0006979) | “glutathione… major antioxidant” and overproducing glutathione “showed improved survival after drying/rehydration” (sek2023physiologicalandgenetic pages 10-11) | 10.1007/s00203-023-03683-w, 2023, https://doi.org/10.1007/s00203-023-03683-w | Good mechanistic and phenotype link in yeast/engineered yeast. |
| Glutathione (CHEBI:16856) | positively_regulates | Desiccation survival (METPO:traitmech:000010 [trait]) | “engineered H. polymorpha overproducing glutathione showed improved survival after drying/rehydration” (sek2023physiologicalandgenetic pages 10-11) | 10.1007/s00203-023-03683-w, 2023, https://doi.org/10.1007/s00203-023-03683-w | Species-specific experimental support; may be curated as taxon-scoped if needed. |
| Superoxide dismutase activity (GO:0004784) | negatively_regulates | Reactive oxygen species level / oxidative damage (GO:1903409 [response to oxidative stress], CHEBI:33579) | DT organisms show “upregulation of… superoxide dismutase… catalases” as conserved oxidative-stress defense (romeroperez2023whenphasedwithout pages 3-4) | 10.1021/acs.chemrev.2c00659, 2023, https://doi.org/10.1021/acs.chemrev.2c00659 | Broad review support; indirect link to tolerance through ROS detoxification. |
| Catalase activity (GO:0004096) | negatively_regulates | Reactive oxygen species / H2O2 toxicity (CHEBI:16240, CHEBI:33579) | DT organisms upregulate “catalases”; in D. radiodurans DrsS restores “catalase-mediated detoxification of ROS” (romeroperez2023whenphasedwithout pages 3-4, rai2024anovelionizing pages 1-3) | 10.1021/acs.chemrev.2c00659, 2023, https://doi.org/10.1021/acs.chemrev.2c00659; 10.1128/aem.01538-23, 2024, https://doi.org/10.1128/aem.01538-23 | Strong mechanistic support; direct desiccation phenotype is clearer in general review than in DrsS paper. |
| Heat shock proteins / chaperone activity (GO:0009408; GO:0051082) | negatively_regulates | Protein aggregation / denaturation (GO:0035966 [response to topologically incorrect protein]) | “heat shock proteins bind denatured proteins, preventing aggregation and aiding repair on rehydration” (sek2023physiologicalandgenetic pages 4-6) | 10.1007/s00203-023-03683-w, 2023, https://doi.org/10.1007/s00203-023-03683-w | Strong yeast evidence; generalizable proteostasis mechanism. |
| Heat shock proteins / chaperone activity (GO:0051082) | positively_regulates | Desiccation survival (METPO:traitmech:000010 [trait]) | Review lists Hsp12p/Hsp70p among “most important compounds” responsible for anhydrobiosis (sek2023physiologicalandgenetic pages 1-3) | 10.1007/s00203-023-03683-w, 2023, https://doi.org/10.1007/s00203-023-03683-w | More associative than causal in this snippet; curate with moderate confidence. |
| LEA/CAHS intrinsically disordered proteins (GO:0050896 response to stimulus [broad]; label-only family nodes) | synergizes_with | Trehalose or sucrose (CHEBI:16551; CHEBI:17992) | “desiccation-related IDPs… synergize with endogenous cosolutes to enhance protection during drying” (kc2024disorderedproteinsinteract pages 1-2) | 10.7554/eLife.97231, 2024, https://doi.org/10.7554/eLife.97231 | Strong recent mechanistic result; not microbe-native in all cases, but relevant causal design principle. |
| CAHS self-assembly / gelation (label-only candidate) | positively_regulates | Protection during dry storage (label-only candidate) | “for CAHS… synergy is related to self-assembly and gel formation” and CAHS variants tune protection (kc2024disorderedproteinsinteract pages 1-2, packebush2023naturalandengineered pages 3-4) | 10.7554/eLife.97231, 2024, https://doi.org/10.7554/eLife.97231; 10.1038/s41598-023-31586-9, 2023, https://doi.org/10.1038/s41598-023-31586-9 | Good support for storage/thermal protection; mechanism may differ from cycling survival. |
| CAHS hydrogel formation (label-only candidate) | negatively_regulates | Protection during repeated desiccation/rehydration cycling (label-only candidate) | “2X Linker… gelation inhibited protection during repeated drying but was protective under thermal stress” (packebush2023naturalandengineered pages 3-4) | 10.1038/s41598-023-31586-9, 2023, https://doi.org/10.1038/s41598-023-31586-9 | Important trade-off; application-specific and not native microbial trait evidence. |
| Mn2+-metabolite antioxidant complexes (CHEBI:29035 Mn2+; label-only complex) | protects | Proteome / DNA-repair enzymes from oxidation (GO:0006457 protein folding [broad], label-only proteome node) | “Mn2+-metabolite complexes… can protect enzymes needed to repair DNA” and form a “proteome shield” (abbaszadeh2024theecologyand pages 24-28, rai2024anovelionizing pages 13-14) | 10.1128/aem.01538-23, 2024, https://doi.org/10.1128/aem.01538-23 | Strong for shared radiation/desiccation logic in Deinococcus-like systems; direct desiccation assay may be indirect. |
| High intracellular Mn/Fe ratio (label-only candidate) | associated_with / positively_regulates | Radiation- and desiccation-resistance (label-only phenotype node) | “a high ratio of Mn/Fe is usually another indicator of radiation and desiccation-resistant organisms” (abbaszadeh2024theecologyand pages 24-28) | source context from 2024 ecology/history synthesis (no DOI available in context) | Use cautiously: correlative/generalized synthesis, not a direct causal perturbation experiment. |
| DrsS sRNA (D. radiodurans; label-only candidate) | positively_regulates | katA catalase transcript/activity (gene label; GO:0004096) | “DrsS… interacts with the katA transcript” and restores “catalase-mediated detoxification of ROS” (rai2024anovelionizing pages 1-3) | 10.1128/aem.01538-23, 2024, https://doi.org/10.1128/aem.01538-23 | Strong gene-regulatory mechanism, but shown under oxidative/radiation stress rather than direct desiccation assay. |
| DrsS sRNA (D. radiodurans; label-only candidate) | maintains | Intracellular Mn2+/Fe2+ homeostasis (CHEBI:29035; CHEBI:29033) | drsS deletion caused “drop in intracellular Mn2+ (~70%) and Fe2+ (~40%)” with increased protein carbonylation (rai2024anovelionizing pages 1-3) | 10.1128/aem.01538-23, 2024, https://doi.org/10.1128/aem.01538-23 | Strong mechanistic evidence for metal homeostasis and oxidative protection; desiccation link is inferred/shared-stress. |
| Extracellular polysaccharides, CPS/RPS/EPS (GO:0030312 external encapsulating structure; CHEBI:polysaccharide [label]) | retains_water / delays | Desiccation of biocrust microenvironment (ENVO:desiccation [label]) | hydration “increased… EPS production,” and EPS “delayed desiccation and temporarily sustained the biocrust community activity” (baubin2023divergenceofbiocrust pages 1-4) | 10.1007/s00248-022-02063-z, 2023, https://doi.org/10.1007/s00248-022-02063-z | Field/community-level inference, not single-gene mechanism; still highly relevant for environmental trait curation. |
| EPS layer with scytonemin / LPS-associated matrix (label-only candidate; scytonemin CHEBI:132997 [candidate]) | provides | UV shield / oxidative-stress defense (GO:0009411 response to UV; GO:0006979) | “scytonemin is located in the exopolysaccharide layer” and forms a “UV-protective shield”; UV-C increased antioxidant enzyme activity (irankhahi2024theroleof pages 1-2) | 10.1038/s41598-024-70002-8, 2024, https://doi.org/10.1038/s41598-024-70002-8 | Strong cyanobacterial stress-shield mechanism; not direct desiccation, but relevant neighboring protection in exposed dry habitats. |


*Table: This table lists evidence-backed candidate subject-predicate-object edges for curating a causal graph of microbial desiccation tolerance. It emphasizes mechanisms with recent support and flags where claims are taxon-specific, indirect, or better treated as shared stress-response analogies rather than direct desiccation evidence.*

### 6) Current applications and real-world implementations

#### 6.1 Industrial microbial implementation: active dry yeast
Yeast anhydrobiosis is directly relevant to industrial manufacturing of dried starters. Active dried brewing yeast typically has **~8% residual moisture**, and rehydration protocols (e.g., **35–40 °C**) strongly affect viability; rehydration can cause **up to ~30% weight loss** due to leakage, emphasizing assay factors that should appear in TraitMech as experimental conditions. (sek2023physiologicalandgenetic pages 1-3)

#### 6.2 Biologic/pharmaceutical stabilization without cold chain (anhydrobiotic mediators)
Packebush et al. (Scientific Reports, 2023) demonstrate that sugar protectants (trehalose/sucrose) and protein-based protectants (engineered tardigrade CAHS variants) can stabilize **human Factor VIII** through **6 desiccation/rehydration cycles** at **3.94–6.88% moisture**, quantified by aPTT (50% clotting time). In their dataset, healthy supplemented plasma is ~150 s and FVIII-deficient plasma ~300 s; protectants partially restore function, and a CAHS D linker-region variant maintained stability for **≥10 weeks** in the dry state. (packebush2023naturalandengineered pages 3-4)

The key application insight is that **protein-based mediators are engineerable**, and protective performance can be tuned via CAHS gelation behavior (trade-offs between cycling vs thermal stress). (packebush2023naturalandengineered pages 3-4)

**Supporting figure/table evidence.** Figures 2–3 show clotting-time outcomes across protectant types and concentrations under repeated desiccation/rehydration cycles. (packebush2023naturalandengineered media b0c9f6ad, packebush2023naturalandengineered media 0c8afe1e)

#### 6.3 EPS in sustainable materials and biofilm protection
Recent EPS reviews synthesize broad applications (food, pharma, biomaterials) and document that microbial EPS can have **antioxidant (ROS scavenging) activity** measurable by standard assays, supporting a mechanistic bridge from EPS chemistry → oxidative protection in dry/UV-exposed contexts. (mouro2024microbialexopolysaccharidesstructure pages 31-33)

### 7) Relevant statistics and quantitative data points for curation

- **Operational DT threshold:** ≤0.1 g H\_2O/g dry mass (≈50% RH, 20 °C; ≤ −100 MPa). (romeroperez2023whenphasedwithout pages 3-4)
- **Yeast anhydrobiosis markers:** intracellular water ~8–10% and water activity ~0.5 (review synthesis). (sek2023physiologicalandgenetic pages 1-3)
- **Industrial dried yeast:** residual moisture ~8%; recommended rehydration 35–40 °C; leakage can cause up to ~30% weight loss. (sek2023physiologicalandgenetic pages 1-3)
- **Nostoc EPS pools:** CPS ~681.8 mg/L; RPS ~470.2 mg/L; scytonemin rises to ~0.26–0.27 µg/mL in resistant strains after prolonged UV-C exposure. (irankhahi2024theroleof pages 6-7)
- **Factor VIII dry stabilization:** 6 desiccation/rehydration cycles at ~3.94–6.88% moisture; aPTT functional readouts (healthy ~150 s; deficient ~300 s) and **≥10-week** dry stability for a CAHS variant. (packebush2023naturalandengineered pages 3-4)
- **Deinococcus oxidative network:** drsS deletion reduces intracellular Mn2+ ~70% and Fe2+ ~40% with increased protein carbonylation; DrsS supports catalase-mediated ROS detoxification. (rai2024anovelionizing pages 1-3)

### 8) Expert synthesis (authoritative opinions) and mechanistic interpretation

Two 2023–2024 high-authority Chemical Reviews consolidate the field view that desiccation tolerance emerges from intertwined **biophysical** and **biochemical** strategies: cells must cope with crowding, altered phase behavior, and oxidative stress; therefore, causal graphs should include both (i) classical stress response modules (antioxidants/chaperones) and (ii) cytoplasmic materials/phase behavior (vitrification, gels, condensates). (romeroperez2023whenphasedwithout pages 3-4, olgenblum2024protectingproteinsfrom pages 2-3)

A practical curation implication is that *desiccation tolerance is not a single pathway*; it is a systems phenotype whose mechanisms can be **convergent** (e.g., oxidative defense) yet **implemented differently across taxa** (e.g., trehalose-centric in many microbes/yeast vs protein-centric IDP/gel strategies in some anhydrobiotic lineages). (romeroperez2023whenphasedwithout pages 3-4, kc2024disorderedproteinsinteract pages 1-2)

### 9) Warnings / claims that may be premature for TraitMech curation

1) **Mn/Fe ratio → desiccation tolerance** is frequently discussed as an indicator in syntheses, but can be correlative; curate as *associated_with* unless a perturbation experiment directly links Mn manipulation to desiccation survival in the target taxon. (abbaszadeh2024theecologyand pages 24-28)

2) **Radiation-resistance regulators (e.g., DrsS/katA)** are mechanistically strong for ROS defense, but **direct desiccation survival assays** are not always included; treat as *shared-stress mechanism* edges unless desiccation-specific evidence is available. (rai2024anovelionizing pages 1-3)

3) **EPS quantity vs stress tolerance**: EPS can matter via structure/location and through embedding pigments (scytonemin) even when bulk EPS amounts are unchanged; avoid curating simplistic “EPS increases → tolerance increases” edges without context. (irankhahi2024theroleof pages 6-7, irankhahi2024theroleof pages 1-2)

---

## DOI-first bibliography (with publication dates and URLs where available)

- Romero-Perez PS, et al. *When Phased without Water: Biophysics of Cellular Desiccation, from Biomolecules to Condensates.* **Chemical Reviews** (May 2023). DOI: **10.1021/acs.chemrev.2c00659**. https://doi.org/10.1021/acs.chemrev.2c00659 (romeroperez2023whenphasedwithout pages 3-4, romeroperez2023whenphasedwithout pages 2-3, romeroperez2023whenphasedwithout pages 1-2, romeroperez2023whenphasedwithout pages 17-18)
- Sęk W, et al. *Physiological and genetic regulation of anhydrobiosis in yeast cells.* **Archives of Microbiology** (Oct 2023). DOI: **10.1007/s00203-023-03683-w**. https://doi.org/10.1007/s00203-023-03683-w (sek2023physiologicalandgenetic pages 1-3, sek2023physiologicalandgenetic pages 4-6, sek2023physiologicalandgenetic pages 10-11)
- Packebush MH, et al. *Natural and engineered mediators of desiccation tolerance stabilize Human Blood Clotting Factor VIII in a dry state.* **Scientific Reports** (Nov 2023). DOI: **10.1038/s41598-023-31586-9**. https://doi.org/10.1038/s41598-023-31586-9 (packebush2023naturalandengineered pages 1-2, packebush2023naturalandengineered pages 3-4, packebush2023naturalandengineered media b0c9f6ad, packebush2023naturalandengineered media 0c8afe1e)
- Olgenblum GI, et al. *Protecting Proteins from Desiccation Stress Using Molecular Glasses and Gels.* **Chemical Reviews** (Apr 2024). DOI: **10.1021/acs.chemrev.3c00752**. https://doi.org/10.1021/acs.chemrev.3c00752 (olgenblum2024protectingproteinsfrom pages 2-3)
- Rai SN, Dutta T. *A novel ionizing radiation-induced small RNA, DrsS, promotes the detoxification of reactive oxygen species in Deinococcus radiodurans.* **Applied and Environmental Microbiology** (May 2024). DOI: **10.1128/aem.01538-23**. https://doi.org/10.1128/aem.01538-23 (rai2024anovelionizing pages 1-3, rai2024anovelionizing pages 13-14)
- da Silva MBF, Teixeira CMLL. *Cyanobacterial and microalgae polymers: antiviral activity and applications.* **Brazilian Journal of Microbiology** (Jul 2024). DOI: **10.1007/s42770-024-01452-5**. https://doi.org/10.1007/s42770-024-01452-5 (silva2024cyanobacterialandmicroalgae pages 3-4)
- Irankhahi P, et al. *The role of the protective shield against UV-C radiation and its molecular interactions in Nostoc species (Cyanobacteria).* **Scientific Reports** (Aug 2024). DOI: **10.1038/s41598-024-70002-8**. https://doi.org/10.1038/s41598-024-70002-8 (irankhahi2024theroleof pages 1-2, irankhahi2024theroleof pages 6-7)
- Nguyen H-T, et al. *Advances in Microbial Exopolysaccharides: Present and Future Applications.* **Biomolecules** (Sep 2024). DOI: **10.3390/biom14091162**. https://doi.org/10.3390/biom14091162 (nguyen2024advancesinmicrobial pages 11-13)
- Mouro C, et al. *Microbial Exopolysaccharides: Structure, Diversity, Applications, and Future Frontiers in Sustainable Functional Materials.* **Polysaccharides** (Jul 2024). DOI: **10.3390/polysaccharides5030018**. https://doi.org/10.3390/polysaccharides5030018 (mouro2024microbialexopolysaccharidesstructure pages 31-33)
- Baubin C, et al. *Divergence of Biocrust Active Bacterial Communities in the Negev Desert During a Hydration-Desiccation Cycle.* **Microbial Ecology** (Jul 2023). DOI: **10.1007/s00248-022-02063-z**. https://doi.org/10.1007/s00248-022-02063-z (baubin2023divergenceofbiocrust pages 1-4)
- KC S, et al. *Disordered proteins interact with the chemical environment to tune their protective function during drying.* **eLife** (Nov 2024). DOI: **10.7554/eLife.97231**. https://doi.org/10.7554/eLife.97231 (kc2024disorderedproteinsinteract pages 1-2, kc2024disorderedproteinsinteract pages 28-29)

*(Additional non-DOI context sources were present in retrieval but not used as primary evidence for curation claims.)*

References

1. (romeroperez2023whenphasedwithout pages 3-4): Paulette Sofia Romero-Perez, Yanniv Dorone, Eduardo Flores, Shahar Sukenik, and Steven Boeynaems. When phased without water: biophysics of cellular desiccation, from biomolecules to condensates. Chemical Reviews, 123:9010-9035, May 2023. URL: https://doi.org/10.1021/acs.chemrev.2c00659, doi:10.1021/acs.chemrev.2c00659. This article has 85 citations and is from a highest quality peer-reviewed journal.

2. (romeroperez2023whenphasedwithout pages 2-3): Paulette Sofia Romero-Perez, Yanniv Dorone, Eduardo Flores, Shahar Sukenik, and Steven Boeynaems. When phased without water: biophysics of cellular desiccation, from biomolecules to condensates. Chemical Reviews, 123:9010-9035, May 2023. URL: https://doi.org/10.1021/acs.chemrev.2c00659, doi:10.1021/acs.chemrev.2c00659. This article has 85 citations and is from a highest quality peer-reviewed journal.

3. (sek2023physiologicalandgenetic pages 4-6): Wioletta Sęk, Anna M. Kot, Alexander Rapoport, and Marek Kieliszek. Physiological and genetic regulation of anhydrobiosis in yeast cells. Archives of Microbiology, Oct 2023. URL: https://doi.org/10.1007/s00203-023-03683-w, doi:10.1007/s00203-023-03683-w. This article has 13 citations and is from a peer-reviewed journal.

4. (sek2023physiologicalandgenetic pages 10-11): Wioletta Sęk, Anna M. Kot, Alexander Rapoport, and Marek Kieliszek. Physiological and genetic regulation of anhydrobiosis in yeast cells. Archives of Microbiology, Oct 2023. URL: https://doi.org/10.1007/s00203-023-03683-w, doi:10.1007/s00203-023-03683-w. This article has 13 citations and is from a peer-reviewed journal.

5. (kc2024disorderedproteinsinteract pages 1-2): Shraddha KC, Kenny H Nguyen, Vincent Nicholson, Annie Walgren, Tony Trent, Edith Gollub, Paulette Sofia Romero-Perez, Alex S Holehouse, Shahar Sukenik, and Thomas C Boothby. Disordered proteins interact with the chemical environment to tune their protective function during drying. eLife, Nov 2024. URL: https://doi.org/10.7554/elife.97231, doi:10.7554/elife.97231. This article has 24 citations and is from a domain leading peer-reviewed journal.

6. (abbaszadeh2024theecologyand pages 24-28): J Abbaszadeh. The ecology and evolutionary history of the deinococcaceae family. Unknown journal, 2024.

7. (rai2024anovelionizing pages 13-14): Shiv Narayan Rai and Tanmay Dutta. A novel ionizing radiation-induced small rna, drss, promotes the detoxification of reactive oxygen species in <i>deinococcus radiodurans</i>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.01538-23, doi:10.1128/aem.01538-23. This article has 9 citations and is from a peer-reviewed journal.

8. (baubin2023divergenceofbiocrust pages 1-4): Capucine Baubin, Noya Ran, Hagar Siebner, and Osnat Gillor. Divergence of biocrust active bacterial communities in the negev desert during a hydration-desiccation cycle. Microbial Ecology, 86:474-484, Jul 2023. URL: https://doi.org/10.1007/s00248-022-02063-z, doi:10.1007/s00248-022-02063-z. This article has 16 citations and is from a domain leading peer-reviewed journal.

9. (silva2024cyanobacterialandmicroalgae pages 3-4): Mariana Barbalho Farias da Silva and Cláudia Maria Luz Lapa Teixeira. Cyanobacterial and microalgae polymers: antiviral activity and applications. Brazilian journal of microbiology : [publication of the Brazilian Society for Microbiology], 55:3287-3301, Jul 2024. URL: https://doi.org/10.1007/s42770-024-01452-5, doi:10.1007/s42770-024-01452-5. This article has 8 citations.

10. (irankhahi2024theroleof pages 1-2): Pardis Irankhahi, Hossein Riahi, Seyedeh Batool Hassani, Maryam Eskafi, Maryam Azimzadeh Irani, and Zeinab Shariatmadari. The role of the protective shield against uv-c radiation and its molecular interactions in nostoc species (cyanobacteria). Scientific Reports, Aug 2024. URL: https://doi.org/10.1038/s41598-024-70002-8, doi:10.1038/s41598-024-70002-8. This article has 13 citations and is from a peer-reviewed journal.

11. (rai2024anovelionizing pages 1-3): Shiv Narayan Rai and Tanmay Dutta. A novel ionizing radiation-induced small rna, drss, promotes the detoxification of reactive oxygen species in <i>deinococcus radiodurans</i>. Applied and Environmental Microbiology, May 2024. URL: https://doi.org/10.1128/aem.01538-23, doi:10.1128/aem.01538-23. This article has 9 citations and is from a peer-reviewed journal.

12. (olgenblum2024protectingproteinsfrom pages 2-3): Gil I. Olgenblum, Brent O. Hutcheson, Gary J. Pielak, and Daniel Harries. Protecting proteins from desiccation stress using molecular glasses and gels. Chemical Reviews, 124:5668-5694, Apr 2024. URL: https://doi.org/10.1021/acs.chemrev.3c00752, doi:10.1021/acs.chemrev.3c00752. This article has 38 citations and is from a highest quality peer-reviewed journal.

13. (irankhahi2024theroleof pages 6-7): Pardis Irankhahi, Hossein Riahi, Seyedeh Batool Hassani, Maryam Eskafi, Maryam Azimzadeh Irani, and Zeinab Shariatmadari. The role of the protective shield against uv-c radiation and its molecular interactions in nostoc species (cyanobacteria). Scientific Reports, Aug 2024. URL: https://doi.org/10.1038/s41598-024-70002-8, doi:10.1038/s41598-024-70002-8. This article has 13 citations and is from a peer-reviewed journal.

14. (sek2023physiologicalandgenetic pages 1-3): Wioletta Sęk, Anna M. Kot, Alexander Rapoport, and Marek Kieliszek. Physiological and genetic regulation of anhydrobiosis in yeast cells. Archives of Microbiology, Oct 2023. URL: https://doi.org/10.1007/s00203-023-03683-w, doi:10.1007/s00203-023-03683-w. This article has 13 citations and is from a peer-reviewed journal.

15. (packebush2023naturalandengineered pages 1-2): Maxwell H. Packebush, Silvia Sánchez-Martínez, Sourav Biswas, S. Kc, K. Nguyen, J. Ramirez, V. Nicholson, and T. Boothby. Natural and engineered mediators of desiccation tolerance stabilize human blood clotting factor viii in a dry state. Scientific Reports, Nov 2023. URL: https://doi.org/10.1038/s41598-023-31586-9, doi:10.1038/s41598-023-31586-9. This article has 32 citations and is from a peer-reviewed journal.

16. (romeroperez2023whenphasedwithout pages 1-2): Paulette Sofia Romero-Perez, Yanniv Dorone, Eduardo Flores, Shahar Sukenik, and Steven Boeynaems. When phased without water: biophysics of cellular desiccation, from biomolecules to condensates. Chemical Reviews, 123:9010-9035, May 2023. URL: https://doi.org/10.1021/acs.chemrev.2c00659, doi:10.1021/acs.chemrev.2c00659. This article has 85 citations and is from a highest quality peer-reviewed journal.

17. (romeroperez2023whenphasedwithout pages 17-18): Paulette Sofia Romero-Perez, Yanniv Dorone, Eduardo Flores, Shahar Sukenik, and Steven Boeynaems. When phased without water: biophysics of cellular desiccation, from biomolecules to condensates. Chemical Reviews, 123:9010-9035, May 2023. URL: https://doi.org/10.1021/acs.chemrev.2c00659, doi:10.1021/acs.chemrev.2c00659. This article has 85 citations and is from a highest quality peer-reviewed journal.

18. (packebush2023naturalandengineered pages 3-4): Maxwell H. Packebush, Silvia Sánchez-Martínez, Sourav Biswas, S. Kc, K. Nguyen, J. Ramirez, V. Nicholson, and T. Boothby. Natural and engineered mediators of desiccation tolerance stabilize human blood clotting factor viii in a dry state. Scientific Reports, Nov 2023. URL: https://doi.org/10.1038/s41598-023-31586-9, doi:10.1038/s41598-023-31586-9. This article has 32 citations and is from a peer-reviewed journal.

19. (sadowskabartosz2024antioxidantdefensein pages 20-21): Izabela Sadowska-Bartosz and Grzegorz Bartosz. Antioxidant defense in the toughest animals on the earth: its contribution to the extreme resistance of tardigrades. International Journal of Molecular Sciences, 25:8393, Aug 2024. URL: https://doi.org/10.3390/ijms25158393, doi:10.3390/ijms25158393. This article has 16 citations.

20. (packebush2023naturalandengineered media b0c9f6ad): Maxwell H. Packebush, Silvia Sánchez-Martínez, Sourav Biswas, S. Kc, K. Nguyen, J. Ramirez, V. Nicholson, and T. Boothby. Natural and engineered mediators of desiccation tolerance stabilize human blood clotting factor viii in a dry state. Scientific Reports, Nov 2023. URL: https://doi.org/10.1038/s41598-023-31586-9, doi:10.1038/s41598-023-31586-9. This article has 32 citations and is from a peer-reviewed journal.

21. (packebush2023naturalandengineered media 0c8afe1e): Maxwell H. Packebush, Silvia Sánchez-Martínez, Sourav Biswas, S. Kc, K. Nguyen, J. Ramirez, V. Nicholson, and T. Boothby. Natural and engineered mediators of desiccation tolerance stabilize human blood clotting factor viii in a dry state. Scientific Reports, Nov 2023. URL: https://doi.org/10.1038/s41598-023-31586-9, doi:10.1038/s41598-023-31586-9. This article has 32 citations and is from a peer-reviewed journal.

22. (mouro2024microbialexopolysaccharidesstructure pages 31-33): Cláudia Mouro, Ana P. Gomes, and Isabel C. Gouveia. Microbial exopolysaccharides: structure, diversity, applications, and future frontiers in sustainable functional materials. Polysaccharides, 5:241-287, Jul 2024. URL: https://doi.org/10.3390/polysaccharides5030018, doi:10.3390/polysaccharides5030018. This article has 113 citations.

23. (nguyen2024advancesinmicrobial pages 11-13): Huu-Thanh Nguyen, Thuy-Trang Pham, Phu-Tho Nguyen, Hélène Le-Buanec, Holy N. Rabetafika, and Hary L. Razafindralambo. Advances in microbial exopolysaccharides: present and future applications. Sep 2024. URL: https://doi.org/10.3390/biom14091162, doi:10.3390/biom14091162. This article has 74 citations.

24. (kc2024disorderedproteinsinteract pages 28-29): Shraddha KC, Kenny H Nguyen, Vincent Nicholson, Annie Walgren, Tony Trent, Edith Gollub, Paulette Sofia Romero-Perez, Alex S Holehouse, Shahar Sukenik, and Thomas C Boothby. Disordered proteins interact with the chemical environment to tune their protective function during drying. eLife, Nov 2024. URL: https://doi.org/10.7554/elife.97231, doi:10.7554/elife.97231. This article has 24 citations and is from a domain leading peer-reviewed journal.