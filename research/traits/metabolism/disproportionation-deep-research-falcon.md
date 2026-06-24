---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T04:31:39.331264'
end_time: '2026-06-18T04:55:30.507533'
duration_seconds: 1431.18
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: Disproportionation
  trait_identifier: METPO:1000806
  trait_category: METABOLISM
  trait_category_slug: metabolism
  trait_slug: disproportionation
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A metabolism in which a single substrate simultaneously undergoes both
    oxidation and reduction reactions, with part of the substrate serving as the electron
    donor and another part serving as the electron acceptor.
  parent_traits: METPO:1000060
  synonyms: ''
  evidence_summary: 'DOI:10.1080/17415990802105770: serve as both electron donor and
    acceptor (Review supports inorganic sulfur disproportionation as one substrate
    serving both donor and acceptor roles.) | DOI:10.1016/j.gca.2013.03.013: elemental
    sulfur disproportionation (Study supports elemental sulfur disproportionation
    in acidophilic microbial metabolism.)'
  causal_graph_summary: 'sulfur_disproportionation_redox_split: 8 nodes, 7 edges'
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
- **Trait label:** Disproportionation
- **METPO identifier:** METPO:1000806
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which a single substrate simultaneously undergoes both oxidation and reduction reactions, with part of the substrate serving as the electron donor and another part serving as the electron acceptor.
- **Parent traits:** METPO:1000060
- **Synonyms:** 
- **Existing evidence:** DOI:10.1080/17415990802105770: serve as both electron donor and acceptor (Review supports inorganic sulfur disproportionation as one substrate serving both donor and acceptor roles.) | DOI:10.1016/j.gca.2013.03.013: elemental sulfur disproportionation (Study supports elemental sulfur disproportionation in acidophilic microbial metabolism.)
- **Existing causal graph summary:** sulfur_disproportionation_redox_split: 8 nodes, 7 edges

## Research Objective

Research the microbial trait **Disproportionation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/disproportionation.yaml`.

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
- **Trait label:** Disproportionation
- **METPO identifier:** METPO:1000806
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which a single substrate simultaneously undergoes both oxidation and reduction reactions, with part of the substrate serving as the electron donor and another part serving as the electron acceptor.
- **Parent traits:** METPO:1000060
- **Synonyms:** 
- **Existing evidence:** DOI:10.1080/17415990802105770: serve as both electron donor and acceptor (Review supports inorganic sulfur disproportionation as one substrate serving both donor and acceptor roles.) | DOI:10.1016/j.gca.2013.03.013: elemental sulfur disproportionation (Study supports elemental sulfur disproportionation in acidophilic microbial metabolism.)
- **Existing causal graph summary:** sulfur_disproportionation_redox_split: 8 nodes, 7 edges

## Research Objective

Research the microbial trait **Disproportionation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/disproportionation.yaml`.

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


## Microbial Trait Causal Graph Curation Report: Disproportionation (METPO:1000806)

### Scope summary (trait definition, phenotype boundaries)
Disproportionation (METPO:1000806) is a metabolic phenotype in which a *single substrate* is simultaneously oxidized and reduced (i.e., it serves as both electron donor and acceptor), yielding at least two products at different oxidation states; for inorganic sulfur, this commonly means production of sulfate (oxidized) and sulfide (reduced). This is described as “simultaneously reducing and oxidizing a single sulfur compound to form two different products.” (d’ermo2024thecomplexinterplay pages 5-8)

**What the trait represents for curation:** a physiological *capacity* (often supporting energy conservation and growth) to use one compound as internal donor/acceptor. In sulfur cycling this typically targets intermediate-valence sulfur species (e.g., thiosulfate, sulfite, elemental sulfur, tetrathionate) rather than fully oxidized sulfate or fully reduced sulfide. (wang2023disproportionationofinorganic pages 1-2, yan2024characterizationofsulfur pages 49-52)

**Boundary cases / nearby traits:**
- **Not the same as sulfate reduction**: sulfate reduction uses sulfate as a terminal electron acceptor and requires an external electron donor. Many sulfur disproportionators share Dsr-pathway enzymes with sulfate reducers, so gene content alone may not distinguish them. (diao2023globaldiversityand pages 1-2)
- **Not the same as sulfur oxidation**: complete Sox oxidation to sulfate under oxic conditions is a boundary comparator and can dominate in engineered systems; it is not disproportionation because electrons are transferred to an external acceptor (e.g., O2). (whaleymartin2023o2partitioningof pages 7-9, whaleymartin2023o2partitioningof pages 1-2)
- **Single-enzyme vs pathway-level “dismutation”**: authoritative reviews emphasize that disproportionation can be a pathway-level phenomenon, potentially involving multiple enzymes and both oxidative and reductive steps rather than one dedicated enzyme. (d’ermo2024thecomplexinterplay pages 5-8)
- **Thermodynamic boundary for elemental sulfur (S0) disproportionation**: S0 disproportionation is often energetically marginal/endergonic under standard conditions and becomes favorable only if sulfide activity is kept low (e.g., by FeS precipitation). This should be represented explicitly as an environmental enabling edge. (yan2024characterizationofsulfur pages 49-52, wang2023disproportionationofinorganic pages 9-12)

### Current understanding (key concepts)
1. **Canonical sulfur disproportionation stoichiometry (example):** thiosulfate disproportionation yields sulfate and sulfide: “S2O3(2–) + H2O → SO4(2–) + HS– + H+.” (wang2023disproportionationofinorganic pages 9-12)
2. **Thermodynamics and environmental dependence:** thiosulfate and sulfite disproportionation are exergonic (ΔG0 = −21.9 and −58.9 kJ/mol respectively), whereas elemental sulfur disproportionation is endergonic (ΔG0 = +10.3 kJ/mol S0) unless coupled to sulfide removal (e.g., FeSx formation). (yan2024characterizationofsulfur pages 49-52)
3. **S0 bioavailability constraint:** elemental sulfur is poorly soluble (reported ~1 mg/L at 25°C; ~15 mg/L at 80°C), creating a mechanistic bottleneck in activation/uptake and motivating extracellular or nanoparticle-mediated mechanisms. (wang2023disproportionationofinorganic pages 12-13)

### Recent developments (prioritizing 2023–2024)
#### A. Expanded taxonomic distribution and “unknown pathway” evidence (2023)
A key 2023 advance is experimental evidence that **mesophilic chemolithoautotrophic Campylobacterota** (e.g., *Sulfurimonas* and *Sulfurovum*) can grow via disproportionation of thiosulfate and elemental sulfur. (wang2023disproportionationofinorganic pages 2-4, wang2023disproportionationofinorganic pages 1-2)

Mechanistically important for causal-graph curation, these isolates **lack canonical dissimilatory sulfate reduction genes** (aprAB, dsrABD, dsrC, dsrMKJOP), which implies the existence of an alternative, currently unresolved disproportionation pathway in these taxa (curate as *uncertain/inferred*). (wang2023disproportionationofinorganic pages 9-12)

#### B. S4I (tetrathionate intermediate) pathway partitioning and gene markers (2024)
Twible et al. 2024 provides a clear and curation-ready separation of the **S4I pathway** into two functional steps with distinct ecological distributions:
- **Step 1**: thiosulfate → tetrathionate formation by **tsdA** (broadly observed “across the entire pH range”). (twible2024phandthiosulfate pages 12-14)
- **Step 2**: tetrathionate processing by **tetH** (tetrathionate hydrolase), described as producing “S0, S2O32-, and SO42-,” and observed mainly in **Thiobacillus spp.** and more prevalent under **circumneutral pH**. (twible2024phandthiosulfate pages 5-6, twible2024phandthiosulfate pages 12-14)

These results create concrete candidate edges linking **pH → gene occurrence (tetH)** and **taxon → pathway completion** that can be curated with high confidence. (twible2024phandthiosulfate pages 12-14, twible2024phandthiosulfate pages 5-6)

#### C. Enzyme-level mechanistic synthesis for disproportionation-relevant steps (2024)
D’Ermo et al. 2024 (Springer) highlights specific enzymes that can be curated as mechanistic entities in disproportionation-adjacent causal graphs:
- **TetH**: “S4O62- is hydrolyzed by tetrathionate hydrolase TetH in the S4 intermediate (S4I) pathway.” (d’ermo2024thecomplexinterplay pages 15-17)
- **SOR**: “the SOR catalyzes an O2-dependent S0 disproportionation releasing SO32- and HS- (with thiosulfate chemically produced).” (d’ermo2024thecomplexinterplay pages 12-15)

The **SOR node should be curated carefully** because it is explicitly **O2-dependent** and may function more as substrate generation for downstream metabolism rather than direct energy conservation in all contexts. (d’ermo2024thecomplexinterplay pages 12-15)

### Environmental controls and statistics (recent data)
#### Oxygen, nitrate, and pH as primary selectors in engineered sulfur-rich waters
Mine tailings impoundment waters provide strong “real-world” evidence for how redox conditions select sulfur metabolic strategies:
- Over multiple years, the community remained dominated by neutrophilic chemolithoautotrophic SOB (~76% in 2015, ~55% in 2016/2017, ~60% in 2018). (whaleymartin2023o2partitioningof pages 1-2)
- **Oxic zones** favored *Halothiobacillus* with **complete Sox** coupled to O2 and were associated with lower pH (as low as 4.3) and lower thiosulfate. (whaleymartin2023o2partitioningof pages 1-2)
- **Anoxic/low-O2 zones** favored *Thiobacillus* with **incomplete Sox + rDSR** coupled to nitrate (NO3−), associated with higher thiosulfate and “no net significant acidity generation.” (whaleymartin2023o2partitioningof pages 1-2)
- Quantitative ranges reported include dissolved O2 from <LOD to 0.003 mM and pH ~7 to ~4 across depth in the impoundment water column. (whaleymartin2023o2partitioningof pages 7-9)

Supporting visual evidence of oxygen zoning and pathway partitioning in this system is available in retrieved figure crops. (whaleymartin2023o2partitioningof media fcb04f5b, whaleymartin2023o2partitioningof media c5778ec5, whaleymartin2023o2partitioningof media a7d06b55)

#### Global sulfur cycling statistics relevant to disproportionation context
While not exclusive to disproportionation, recent authoritative synthesis of dissimilatory sulfur metabolism provides framing statistics for sulfur-cycling environments where disproportionation is often embedded:
- Sulfate reduction accounts for about “one third” of organic matter mineralization at the seabed (of ~260 Tmol C/yr), and sulfide reoxidation is substantial (~90% reoxidized), contributing “25% of global oxygen consumption in sediments.” (diao2023globaldiversityand pages 1-2)

### Current applications and real-world implementations
#### A. Tailings-water management and “gene-based monitoring” (2023–2024)
Two 2023–2024 mine-water studies propose actionable monitoring/management strategies that directly inform TraitMech edge curation about environmental controls:
- Whaley-Martin et al. propose “prediction of acidification events using gene-based monitoring and in situ RNA detection” and identify pathway genes involved in intermediate sulfur transformations (e.g., TsdA/DoxDA, TetH, sulfur dioxygenase). (whaleymartin2023o2partitioningof pages 1-2)
- Gordon et al. 2024 demonstrate a 28-day, 500-L mesocosm diagnostic approach combining sensors, sulfur speciation, metagenomes and mRNA, and emphasize that using nitrate instead of oxygen as terminal electron acceptor lowers proton yield. (gordon2024microbialsulfurpathways pages 1-5, gordon2024microbialsulfurpathways pages 5-8)

A management-relevant quantitative relationship is explicitly provided: “pairing sulfur oxidation to nitrate rather than O2 greatly lowers proton yield (stoichiometry: with O2 ΔH+/ΔS = 1; with NO3− ΔH+/ΔS = 0).” (gordon2024microbialsulfurpathways pages 19-21)

#### B. Bioremediation in acidic pit lakes (2024)
Liu et al. 2024 show engineered stimulation of sulfur cycling to promote biosulfidogenesis and metal immobilization in an acidic pit lake, providing quantitative geochemistry constraints and community outcomes:
- Deep-layer waters had sulfate 11–12 g/L and Fe up to 6 g/L; As 15 mg/L, Zn ~100 mg/L, Al ~50 mg/L. (liu2024enrichmentofacidtolerant pages 1-2)
- Glycerol stimulated sulfate reduction faster than elemental sulfur alone, while glycerol + S0 produced the highest sulfide; *Desulfosporosinus acididurans* enriched to ~76–96% (glycerol) and ~93–99% (glycerol + S0). (liu2024enrichmentofacidtolerant pages 1-2)

### Candidate nodes for disproportionation causal graph
The following node inventory is designed for direct translation into `data/traits/metabolism/disproportionation.yaml`.

| Node label | Node type | Suggested ontology grounding (CURIE if known, else blank) | Notes/role in disproportionation | Key source IDs |
|---|---|---|---|---|
| Trait: microbial disproportionation | Trait/phenotype | METPO:1000806 | Metabolism where one substrate serves as both electron donor and acceptor, yielding more oxidized and more reduced products; sulfur-focused examples include thiosulfate, sulfite, elemental sulfur, and tetrathionate transformations. | (yan2024characterizationofsulfur pages 49-52, d’ermo2024thecomplexinterplay pages 5-8) |
| Sulfur disproportionation | Trait/phenotype |  | Candidate child/specialization of general disproportionation focused on inorganic sulfur intermediates; common in anoxic sulfur-cycling settings. | (wang2023disproportionationofinorganic pages 1-2, d’ermo2024thecomplexinterplay pages 5-8) |
| Thiosulfate disproportionation | Trait/phenotype |  | Often exergonic; can support growth in some sulfur-disproportionating bacteria; mechanistically overlaps with sulfur oxidation/reduction modules. | (yan2024characterizationofsulfur pages 49-52, wang2023disproportionationofinorganic pages 1-2) |
| Elemental sulfur disproportionation | Trait/phenotype |  | Thermodynamically marginal/endergonic unless sulfide is removed by Fe minerals or oxidation; important boundary case for curation. | (yan2024characterizationofsulfur pages 49-52, wang2023disproportionationofinorganic pages 1-2) |
| Sulfite disproportionation | Trait/phenotype |  | More favorable energetically than elemental sulfur disproportionation; often inferred to use Dsr-pathway-related enzymes. | (yan2024characterizationofsulfur pages 49-52) |
| Tetrathionate disproportionation/hydrolysis | Trait/phenotype |  | Often represented via S4I pathway second step, especially TetH-mediated tetrathionate turnover producing sulfate, thiosulfate, and sulfur intermediates. | (twible2024phandthiosulfate pages 12-14, d’ermo2024thecomplexinterplay pages 15-17) |
| Thiosulfate | Substrate/product | CHEBI:30087 | Major disproportionation substrate and sulfur intermediate; also precursor to tetrathionate in S4I pathway. | (wang2023disproportionationofinorganic pages 1-2, d’ermo2024thecomplexinterplay pages 15-17) |
| Elemental sulfur | Substrate/product | CHEBI:26806 | Insoluble substrate for disproportionation; low solubility constrains uptake/activation and may require polysulfide/nanoparticle intermediates. | (wang2023disproportionationofinorganic pages 12-13, wang2023disproportionationofinorganic pages 1-2) |
| Sulfite | Substrate/product | CHEBI:17980 | Product of some disproportionation/oxidation steps and substrate for further reduction to sulfide via Dsr-related systems. | (yan2024characterizationofsulfur pages 49-52, d’ermo2024thecomplexinterplay pages 12-15) |
| Sulfate | Substrate/product | CHEBI:16189 | Oxidized product of sulfur disproportionation; endpoint used in geochemical confirmation of activity. | (wang2023disproportionationofinorganic pages 2-4, d’ermo2024thecomplexinterplay pages 5-8) |
| Hydrogen sulfide / sulfide | Substrate/product | CHEBI:16199 | Reduced product; removal by Fe precipitation can make elemental sulfur disproportionation favorable. | (yan2024characterizationofsulfur pages 49-52, wang2023disproportionationofinorganic pages 1-2) |
| Tetrathionate | Substrate/product | CHEBI:29203 | Intermediate in S4I pathway; formed from thiosulfate by TsdA/DoxDA and hydrolyzed/disproportionated by TetH. | (twible2024phandthiosulfate pages 1-2, d’ermo2024thecomplexinterplay pages 15-17) |
| Polysulfide | Substrate/product | CHEBI:29265 | Candidate soluble activation/transport intermediate for elemental sulfur disproportionation and sulfur transfer. | (wang2023disproportionationofinorganic pages 12-13, d’ermo2024thecomplexinterplay pages 12-15) |
| Ferric iron [Fe(III)] | Substrate/product | CHEBI:29033 | External sulfide scavenger via FeS formation; can indirectly enable elemental sulfur disproportionation by lowering sulfide activity. | (yan2024characterizationofsulfur pages 49-52, wang2023disproportionationofinorganic pages 2-4) |
| Ferrous sulfide (FeS) | Substrate/product | CHEBI:75820 | Precipitation product indicating sulfide generation in enrichment cultures with ferrihydrite/iron scavengers. | (wang2023disproportionationofinorganic pages 2-4) |
| Sulfur disproportionation pathway | Pathway/module |  | Pathway-level process rather than single enzyme in many cases; may combine reductive and oxidative sulfur reactions. | (d’ermo2024thecomplexinterplay pages 5-8) |
| Dsr-associated sulfur disproportionation module | Pathway/module |  | In many classic disproportionators, Sat-AprAB-DsrAB-DsrC-DsrMK-associated machinery is implicated in sulfite/thiosulfate disproportionation. | (yan2024characterizationofsulfur pages 49-52, diao2023globaldiversityand pages 1-2) |
| Reverse Dsr (rDSR) pathway | Pathway/module |  | Oxidative use of Dsr machinery; relevant to incomplete sulfur oxidation and potentially linked to sulfur disproportionation in some taxa. | (whaleymartin2023o2partitioningof pages 7-9, d’ermo2024thecomplexinterplay pages 12-15) |
| Incomplete Sox pathway | Pathway/module |  | Non-csox route associated with sulfur intermediate recycling and, in some taxa, disproportionation-like sulfur handling. | (whaleymartin2023o2partitioningof pages 7-9, d’ermo2024thecomplexinterplay pages 5-8) |
| Complete Sox pathway (cSox) | Pathway/module |  | Useful boundary case: complete oxidation to sulfate under oxic conditions, generally not itself disproportionation. | (whaleymartin2023o2partitioningof pages 7-9, twible2024phandthiosulfate pages 1-2) |
| S4I (tetrathionate intermediate) pathway | Pathway/module |  | Two-part module: thiosulfate to tetrathionate (tsdA/doxDA), then tetrathionate hydrolysis/disproportionation (tetH). | (twible2024phandthiosulfate pages 1-2, d’ermo2024thecomplexinterplay pages 15-17) |
| Sulfur oxygenase reductase pathway | Pathway/module |  | Cytoplasmic O2-dependent sulfur disproportionation route in some thermoacidophiles; yields sulfite and sulfide, with thiosulfate formed chemically. | (d’ermo2024thecomplexinterplay pages 12-15) |
| Extracellular sulfur activation/uptake | Pathway/module |  | Candidate mechanistic module for insoluble elemental sulfur use; may involve contact, nanoparticles, polysulfide, or extracellular electron transfer. | (wang2023disproportionationofinorganic pages 12-13) |
| Dissimilatory sulfite reductase complex | Enzyme/complex | EC:1.8.99.5 | Core DsrAB system frequently associated with sulfur disproportionators and sulfite reduction; directionality can be hard to infer from genes alone. | (diao2023globaldiversityand pages 1-2, germe2023giuliadermo pages 21-24) |
| DsrA | Enzyme/complex |  | Alpha subunit of dissimilatory sulfite reductase; present in Dsr clusters linked to sulfur metabolism and inferred disproportionation modules. | (petushkova2024thecompletegenome pages 22-23, petushkova2024thecompletegenome pages 20-22) |
| DsrB | Enzyme/complex |  | Beta subunit of dissimilatory sulfite reductase. | (petushkova2024thecompletegenome pages 22-23, petushkova2024thecompletegenome pages 20-22) |
| DsrC | Enzyme/complex |  | Sulfur relay/cofactor protein interacting with DsrAB and DsrMKJOP in sulfite reduction/oxidation-associated sulfur metabolism. | (petushkova2024thecompletegenome pages 20-22, germe2023giuliadermo pages 21-24) |
| DsrMKJOP complex | Enzyme/complex |  | Membrane complex that re-reduces/recovers DsrC-linked sulfur intermediates in Dsr-associated pathways. | (wang2023disproportionationofinorganic pages 1-2, germe2023giuliadermo pages 21-24) |
| DsrEFH proteins | Enzyme/complex |  | Accessory sulfur transfer proteins that can co-occur with reductive/disproportionating Dsr systems. | (diao2023globaldiversityand pages 1-2, petushkova2024thecompletegenome pages 20-22) |
| DsrL | Enzyme/complex |  | Directionality-associated Dsr accessory protein; DsrL-2 occurs in reductive/disproportionating or oxidative sulfur metabolisms. | (diao2023globaldiversityand pages 1-2) |
| Sulfate adenylyltransferase | Enzyme/complex | EC:2.7.7.4 | Sat; activates sulfate to APS in sulfate reduction-related modules that can overlap genetically with disproportionators. | (yan2024characterizationofsulfur pages 49-52, germe2023giuliadermo pages 21-24) |
| Adenylylsulfate reductase | Enzyme/complex | EC:1.8.99.2 | AprAB; APS to sulfite step in dissimilatory sulfate reduction and related reversible sulfur metabolisms. | (yan2024characterizationofsulfur pages 49-52, germe2023giuliadermo pages 21-24) |
| QmoABC complex | Enzyme/complex |  | Quinone-interacting complex supplying electrons to AprAB in sulfate reduction-associated modules. | (wang2023disproportionationofinorganic pages 1-2, germe2023giuliadermo pages 21-24) |
| Thiosulfate dehydrogenase | Enzyme/complex |  | TsdA; catalyzes thiosulfate to tetrathionate, the first step of S4I. | (twible2024phandthiosulfate pages 1-2, d’ermo2024thecomplexinterplay pages 15-17) |
| Thiosulfate:quinone oxidoreductase | Enzyme/complex |  | DoxDA/TQO; alternative catalyst of thiosulfate to tetrathionate in S4I pathway, especially in acidophiles. | (d’ermo2024thecomplexinterplay pages 15-17, yan2024characterizationofsulfur pages 59-63) |
| Tetrathionate hydrolase | Enzyme/complex |  | TetH; catalyzes tetrathionate turnover to sulfur, thiosulfate, and sulfate; key candidate marker for tetrathionate disproportionation/hydrolysis. | (twible2024phandthiosulfate pages 12-14, d’ermo2024thecomplexinterplay pages 15-17) |
| Sulfur oxygenase reductase | Enzyme/complex | EC:1.13.11.55 | SOR (sor); cytoplasmic O2-dependent enzyme that disproportionates elemental sulfur in some thermoacidophiles. | (d’ermo2024thecomplexinterplay pages 12-15) |
| Thiosulfate reductase | Enzyme/complex |  | PhsABC; implicated in thiosulfate disproportionation/dismutation-like chemistry in some models; annotation may be confounded with Psr. | (germe2023giuliadermo pages 24-28, d’ermo2024thecomplexinterplay pages 5-8) |
| Polysulfide reductase | Enzyme/complex |  | PsrABC/PsrA; reduces polysulfide, overlaps mechanistically with thiosulfate/sulfur reduction modules and may connect to disproportionation networks. | (germe2023giuliadermo pages 24-28, germe2023giuliadermo pages 21-24) |
| SoxYZ sulfur carrier complex | Enzyme/complex |  | Core Sox sulfur carrier; present in sulfur-transforming taxa including Thiocapsa bogorovii. | (petushkova2024thecompletegenome pages 17-19, petushkova2024thecompletegenome pages 19-20) |
| SoxB | Enzyme/complex |  | Thiosulfohydrolase component of Sox system; in some contexts linked to tetrathionate turnover and thiosulfate disproportionation-related modules. | (yan2024characterizationofsulfur pages 59-63, petushkova2024thecompletegenome pages 19-20) |
| SoxXA | Enzyme/complex |  | Heme-containing Sox complex for substrate attachment to SoxYZ. | (petushkova2024thecompletegenome pages 19-20, germe2023giuliadermo pages 24-28) |
| SoxCD | Enzyme/complex |  | Marker of complete Sox oxidation; important negative/boundary marker distinguishing complete oxidation from disproportionation-like sulfur recycling. | (whaleymartin2023o2partitioningof pages 7-9, gordon2024microbialsulfurpathways pages 1-5) |
| Sulfur dioxygenase / persulfide dioxygenase | Enzyme/complex |  | sdo / PDO; participates in oxidation of sulfur/persulfides and downstream sulfur intermediate processing. | (whaleymartin2023o2partitioningof pages 1-2, d’ermo2024thecomplexinterplay pages 12-15) |
| Sulfide:quinone oxidoreductase | Enzyme/complex |  | sqr; generates polysulfide from sulfide and may feed soluble sulfur intermediates into disproportionation-linked networks. | (wang2023disproportionationofinorganic pages 12-13, d’ermo2024thecomplexinterplay pages 12-15) |
| Flavocytochrome c sulfide dehydrogenase | Enzyme/complex |  | FccAB; sulfide oxidation system generating soluble sulfur intermediates. | (petushkova2024thecompletegenome pages 20-22, d’ermo2024thecomplexinterplay pages 12-15) |
| Hdr-like sulfur oxidation complex | Enzyme/complex |  | sHdr/Hdr-like pathway proposed for cytoplasmic oxidation of protein-bound sulfane sulfur to sulfite. | (d’ermo2024thecomplexinterplay pages 12-15) |
| Rhodanese-family sulfurtransferase | Enzyme/complex |  | Rhd; candidate sulfur transfer/activation protein linked to protein-bound persulfide trafficking. | (petushkova2024thecompletegenome pages 20-22, d’ermo2024thecomplexinterplay pages 12-15) |
| TusA/TusBCD/TusE sulfur relay proteins | Enzyme/complex |  | Sulfur carrier proteins with analogies to DsrC-mediated persulfide trafficking. | (petushkova2024thecompletegenome pages 22-23, petushkova2024thecompletegenome pages 20-22) |
| Anoxic sediment environment | Environmental/external factor | ENVO:00002007 | Classic habitat where sulfur disproportionation is widespread and ecologically important. | (wang2023disproportionationofinorganic pages 1-2, diao2023globaldiversityand pages 1-2) |
| Hydrothermal vent / plume environment | Environmental/external factor | ENVO:00000215 | Deep-sea hydrothermal systems harbor Campylobacterota sulfur disproportionators and sulfur-rich geochemistry. | (wang2023disproportionationofinorganic pages 2-4, wang2023disproportionationofinorganic pages 1-2) |
| Circumneutral pH | Environmental/external factor |  | Favors Thiobacillus-associated non-csox/S4I functions including tetH occurrence in some tailings systems. | (twible2024phandthiosulfate pages 1-2) |
| Low pH / acidic conditions | Environmental/external factor |  | Acidophiles often use TetH/DoxDA and SOR-linked sulfur transformations; low pH can partition pathway usage. | (yan2024characterizationofsulfur pages 59-63, twible2024phandthiosulfate pages 1-2) |
| Low dissolved oxygen / anoxia | Environmental/external factor |  | Supports non-csox, nitrate-coupled, and disproportionation-associated sulfur metabolisms; suppresses full oxic sulfur oxidation. | (whaleymartin2023o2partitioningof pages 7-9, gordon2024microbialsulfurpathways pages 19-21) |
| Oxygen | Environmental/external factor | CHEBI:15379 | Terminal electron acceptor in oxic sulfur oxidation and also substrate for SOR; generally distinguishes oxidation from disproportionation boundary cases. | (whaleymartin2023o2partitioningof pages 7-9, d’ermo2024thecomplexinterplay pages 12-15) |
| Nitrate | Environmental/external factor | CHEBI:17632 | Alternative terminal electron acceptor in sulfur oxidation systems; can reduce net acidity compared with O2-coupled oxidation. | (whaleymartin2023o2partitioningof pages 7-9, gordon2024microbialsulfurpathways pages 19-21) |
| Ferrihydrite / iron oxide sulfide scavenger | Environmental/external factor | CHEBI:53400 | Experimental factor used to trap sulfide and facilitate observation/energetic favorability of elemental sulfur disproportionation. | (wang2023disproportionationofinorganic pages 2-4) |
| Sulfide scavenging by Fe minerals | Environmental/external factor |  | Mechanistic external condition that can shift elemental sulfur disproportionation from unfavorable to favorable. | (yan2024characterizationofsulfur pages 49-52, wang2023disproportionationofinorganic pages 1-2) |
| Tailings impoundment water | Environmental/external factor | ENVO:00000022 | Engineered sulfur-rich aquatic system used to observe pathway partitioning and gene-based monitoring opportunities. | (whaleymartin2023o2partitioningof pages 1-2, gordon2024microbialsulfurpathways pages 1-5) |
| Sulfurimonas | Example taxon/habitat | NCBITaxon:30207 | Campylobacterota genus newly shown to disproportionate thiosulfate and elemental sulfur. | (wang2023disproportionationofinorganic pages 2-4, wang2023disproportionationofinorganic pages 1-2) |
| Sulfurovum | Example taxon/habitat | NCBITaxon:268747 | Campylobacterota genus with demonstrated thiosulfate and elemental sulfur disproportionation in 2023 study. | (wang2023disproportionationofinorganic pages 2-4, wang2023disproportionationofinorganic pages 1-2) |
| Thiobacillus | Example taxon/habitat | NCBITaxon:1191 | Associated with incomplete Sox/rDSR and tetH-containing S4I step in circumneutral tailings waters. | (twible2024phandthiosulfate pages 1-2) |
| Halothiobacillus | Example taxon/habitat | NCBITaxon:927 | Boundary/control taxon representing complete Sox oxidation rather than disproportionation. | (whaleymartin2023o2partitioningof pages 7-9, twible2024phandthiosulfate pages 1-2) |
| Thiomonas | Example taxon/habitat | NCBITaxon:32012 | Often tsdA-positive and csox-dominant; relevant comparator for tetrathionate formation without confirmed full disproportionation step. | (twible2024phandthiosulfate pages 5-6, twible2024phandthiosulfate pages 1-2) |
| Sulfuriferula | Example taxon/habitat | NCBITaxon:1329905 | Non-csox sulfur oxidizer associated with circumneutral pH and higher thiosulfate pools. | (twible2024phandthiosulfate pages 1-2) |
| Thiocapsa bogorovii | Example taxon/habitat |  | Purple sulfur bacterium with Sox and Dsr-system genes discussed for thiosulfate disproportionation-related sulfur metabolism. | (petushkova2024thecompletegenome pages 17-19, petushkova2024thecompletegenome pages 20-22) |
| Desulfocapsa sulfexigens | Example taxon/habitat | NCBITaxon:883 | Canonical sulfur-disproportionating bacterium cited as early model organism. | (yan2024characterizationofsulfur pages 42-46) |
| Thermosulfurimonas dismutans | Example taxon/habitat | NCBITaxon:985225 | Thermophilic sulfur disproportionator cited as representative SDB. | (yan2024characterizationofsulfur pages 42-46) |
| Desulfobacterota | Example taxon/habitat | NCBITaxon:29547 | Major phylum containing many classical sulfur disproportionators and dsrAB-encoded sulfur metabolisms. | (wang2023disproportionationofinorganic pages 1-2, diao2023globaldiversityand pages 1-2) |
| Campylobacterota | Example taxon/habitat | NCBITaxon:29547 | Expanded 2023 evidence shows mesophilic chemolithoautotrophic Campylobacterota can disproportionate inorganic sulfur compounds. | (wang2023disproportionationofinorganic pages 2-4, wang2023disproportionationofinorganic pages 1-2) |


*Table: This table compiles candidate nodes for a sulfur-focused microbial disproportionation causal graph, including phenotypes, chemicals, pathways, enzymes, environmental factors, and representative taxa. It is designed to support ontology-grounded TraitMech curation and highlights both direct candidates and important boundary-case nodes.*

### Evidence-backed candidate causal edges (triples)
The following edge set prioritizes mechanistically explicit and curation-ready relationships, with uncertainty flags where inference is required.

| Subject node | Predicate (causal verb) | Object node | Evidence snippet (verbatim if possible) | Notes/assumptions/uncertainty | Source (with DOI if available) |
|---|---|---|---|---|---|
| Microbial disproportionation | converts | single sulfur substrate into oxidized and reduced products | "sulfur-disproportionating processes play an important role in the sulfur biogeochemical cycle and operate by simultaneously reducing and oxidizing a single sulfur compound to form two different products" (d’ermo2024thecomplexinterplay pages 5-8) | General pathway-level definition; supports trait scope more directly than a single molecular edge. | D’Ermo et al. 2024, https://doi.org/10.1007/978-3-031-54306-7_15 |
| Thiosulfate disproportionation | produces | sulfate + sulfide | "Thiosulfate disproportionation follows the stoichiometry S2O3(2–) + H2O → SO4(2–) + HS– + H+" (wang2023disproportionationofinorganic pages 9-12) | Strong direct biochemical edge. | Wang et al. 2023, https://doi.org/10.1128/msystems.00954-22 |
| Sulfite disproportionation | is more energetically favorable than | elemental sulfur disproportionation | "thiosulfate (∆G0 = −21.9 kJ/mol) and sulfite (∆G0 = −58.9 kJ/mol) disproportionation are exergonic, whereas elemental sulfur disproportionation is endergonic" (yan2024characterizationofsulfur pages 49-52) | Thermodynamic comparison, not organism-specific. | Yan 2024 (thesis/unknown journal) (yan2024characterizationofsulfur pages 49-52) |
| Elemental sulfur disproportionation | is enabled by | sulfide removal / FeSx formation | "elemental sulfur disproportionation is endergonic... and becomes energetically favorable only when coupled to sulfide removal (e.g., formation of FeSx; reaction 7, ∆G0 = −27.5 kJ/mol S0)" (yan2024characterizationofsulfur pages 49-52) | Strong enabling-condition edge; suitable environmental causation node. | Yan 2024 (thesis/unknown journal) (yan2024characterizationofsulfur pages 49-52) |
| Ferrihydrite | scavenges | produced sulfide | "ferrihydrite scavenges produced sulfide as Fe-sulfide" (wang2023disproportionationofinorganic pages 9-12) | Experimental support for sulfide-scavenging mechanism. | Wang et al. 2023, https://doi.org/10.1128/msystems.00954-22 |
| Ferrihydrite-mediated sulfide scavenging | enables growth on | elemental sulfur disproportionation | "Elemental sulfur disproportionation occurred with or without ferrihydrite, but growth was observed only when ferrihydrite was present" (wang2023disproportionationofinorganic pages 9-12) | Strong but strain-specific to studied Campylobacterota isolates. | Wang et al. 2023, https://doi.org/10.1128/msystems.00954-22 |
| Low elemental sulfur solubility | constrains | sulfur activation/uptake | "Elemental sulfur (S0) is poorly soluble ('1 mg L21 at 25°C and 15 mg L21 at 80°C'), so cells likely require activation mechanisms" (wang2023disproportionationofinorganic pages 12-13) | Good environmental-constraint edge; units reflect source OCR. | Wang et al. 2023, https://doi.org/10.1128/msystems.00954-22 |
| Direct contact with sulfur | enhances | elemental sulfur disproportionation efficiency | "direct contact with sulfur seems beneficial" (wang2023disproportionationofinorganic pages 12-13) | Mechanistic but somewhat qualitative; may be assay-specific. | Wang et al. 2023, https://doi.org/10.1128/msystems.00954-22 |
| Reduced dialysis membrane pore size | decreases | elemental sulfur disproportionation activity | "efficiency decreasing with smaller membrane pore sizes" (wang2023disproportionationofinorganic pages 9-12) | Supports involvement of nanoparticles/local transformation; indirect mechanism. | Wang et al. 2023, https://doi.org/10.1128/msystems.00954-22 |
| TsdA | catalyzes | thiosulfate → tetrathionate | "tsdA and doxDA catalyze the conversion of thiosulfate (S2O32-) to tetrathionate (S4O62-)" (twible2024phandthiosulfate pages 5-6) | Strong direct enzymatic edge. | Twible et al. 2024, https://doi.org/10.3389/fmicb.2024.1426584 |
| DoxDA/TQO | catalyzes | thiosulfate → tetrathionate | "thiosulfate (S2O32-) can be oxidized to tetrathionate (S4O62-) by DoxDA/TQO, ThdT, or TsdA" (yan2024characterizationofsulfur pages 59-63) | Alternative S4I entry enzyme; useful comparator edge. | Yan 2024 (thesis/unknown journal) (yan2024characterizationofsulfur pages 59-63) |
| TetH | disproportionates/hydrolyzes | tetrathionate to S0 + thiosulfate + sulfate | "can be subsequently disproportionated via tetH to form S0, S2O32-, and SO42-" (twible2024phandthiosulfate pages 5-6) | Strong direct mechanistic edge for S4I step 2. | Twible et al. 2024, https://doi.org/10.3389/fmicb.2024.1426584 |
| TetH | hydrolyzes | tetrathionate | "The produced S4O62- is hydrolyzed by tetrathionate hydrolase TetH in the S4 intermediate (S4I) pathway" (d’ermo2024thecomplexinterplay pages 15-17) | Reinforces prior edge with independent recent review source. | D’Ermo et al. 2024, https://doi.org/10.1007/978-3-031-54306-7_15 |
| SOR | disproportionates | elemental sulfur to sulfite + sulfide | "the SOR catalyzes an O2-dependent S0 disproportionation releasing SO32- and HS-" (d’ermo2024thecomplexinterplay pages 12-15) | Strong direct enzymatic edge; O2-dependent thermoacidophile context. | D’Ermo et al. 2024, https://doi.org/10.1007/978-3-031-54306-7_15 |
| Campylobacterota isolates ST-27/ST-29 | lack | aprAB + dsrABD + dsrC + dsrMKJOP | "strains encode sulfur-oxidation genes... but lack key dissimilatory sulfate-reduction genes (aprAB, dsrABD, dsrC, dsrMKJOP)" (wang2023disproportionationofinorganic pages 9-12) | Strong genotype observation. | Wang et al. 2023, https://doi.org/10.1128/msystems.00954-22 |
| Absence of apr/dsr pathway genes in ST-27/ST-29 | implies | alternative/unknown sulfur disproportionation pathway | "implying alternative mechanisms for disproportionation in these Campylobacterota" (wang2023disproportionationofinorganic pages 9-12) | Inference from genomic absence; curate as uncertain. | Wang et al. 2023, https://doi.org/10.1128/msystems.00954-22 |
| Oxic conditions / higher O2 | favor | Halothiobacillus with complete Sox pathway | "Under oxic conditions, novel Halothiobacillus drive lower pH conditions... via the complete Sox pathway coupled to O2" (whaleymartin2023o2partitioningof pages 1-2) | Strong ecological edge; tailings-water context. | Whaley-Martin et al. 2023, https://doi.org/10.1038/s41467-023-37426-8 |
| Lower-O2 / anoxic conditions | favor | Thiobacillus with incomplete Sox + rDSR | "Under anoxic conditions, Thiobacillus spp. dominate in activity, via the incomplete Sox and rDSR pathways coupled to NO3−" (whaleymartin2023o2partitioningof pages 1-2) | Strong ecological edge; tailings-water context. | Whaley-Martin et al. 2023, https://doi.org/10.1038/s41467-023-37426-8 |
| Complete Sox pathway | drives | acidity generation | "Halothiobacillus possess a complete Sox system... and are associated with more oxygenated waters, Sox-driven oxidation coupled to O2, higher H+/SO4(2-) ratios and net acid generation" (whaleymartin2023o2partitioningof pages 7-9) | Strong pathway-to-phenotype edge. | Whaley-Martin et al. 2023, https://doi.org/10.1038/s41467-023-37426-8 |
| Incomplete Sox + rDSR + nitrate coupling | results in | higher thiosulfate and less net acidity | "Thiobacillus used incomplete Sox and rDSR pathways coupled to NO3−, yielding higher thiosulfate and no net significant acidity generation" (whaleymartin2023o2partitioningof pages 1-2) | Strong pathway-outcome edge. | Whaley-Martin et al. 2023, https://doi.org/10.1038/s41467-023-37426-8 |
| Nitrate as terminal electron acceptor | lowers | proton yield / acidity generation | "pairing sulfur oxidation to nitrate rather than O2 greatly lowers proton yield (stoichiometry: with O2 ΔH+/ΔS = 1; with NO3- ΔH+/ΔS = 0)" (gordon2024microbialsulfurpathways pages 19-21) | Strong mechanistic management edge. | Gordon et al. 2024, https://doi.org/10.1007/s10230-024-01016-x |
| Circumneutral pH (~6.5–8.5) | associates with | tetH occurrence in Thiobacillus | "possible subsequent processing of S4O62- via tetH ... was limited to Thiobacillus spp., observed more prevalently in circumneutral pH values" (twible2024phandthiosulfate pages 12-14) | Strong pH-partitioning edge; ecological association. | Twible et al. 2024, https://doi.org/10.3389/fmicb.2024.1426584 |
| tsdA occurrence | is not constrained by | pH | "the tsdA gene, were observed in SOB genera from across the entire pH range" (twible2024phandthiosulfate pages 12-14) | Strong comparative edge vs tetH restriction. | Twible et al. 2024, https://doi.org/10.3389/fmicb.2024.1426584 |
| Lower pH (~5–6.5) | favors | csox-dominant SOB (Halothiobacillus, Thiomonas) | "csox dominant SOB... drove acidity generation and S2O32- consumption via the csox pathway at lower pH (pH ~5 to ~6.5)" (twible2024phandthiosulfate pages 1-2) | Strong ecological association; useful environmental node. | Twible et al. 2024, https://doi.org/10.3389/fmicb.2024.1426584 |
| Circumneutral pH (~6.5–8.5) | favors | non-csox SOB with higher thiosulfate and limited acidity | "At circumneutral pH (~6.5–8.5), non-csox SOB... correlated with higher [S2O32-] and limited acidity" (twible2024phandthiosulfate pages 1-2) | Supports pH partitioning among sulfur pathways, including S4I/rDSR-associated regimes. | Twible et al. 2024, https://doi.org/10.3389/fmicb.2024.1426584 |


*Table: This table compiles evidence-backed causal edges for sulfur disproportionation and closely related sulfur-intermediate processes. It is designed to support TraitMech curation by linking substrates, enzymes, pathways, and environmental controls to explicit literature-backed relationships.*

### Ontology grounding notes (practical)
- **Chemicals:** CHEBI grounding is straightforward for core substrates/products (e.g., thiosulfate CHEBI:30087; tetrathionate CHEBI:29203; sulfate CHEBI:16189; hydrogen sulfide CHEBI:16199; elemental sulfur CHEBI:26806). (artifact-00)
- **Enzymes:** EC grounding is available for some (e.g., DsrAB EC:1.8.99.5; SOR EC:1.13.11.55). (artifact-00)
- **Environments:** ENVO grounding may be applied for broad habitat nodes (e.g., sediments; hydrothermal vent environment), but some engineered environments (tailings impoundment waters) may require label-only nodes if no stable ENVO term is selected. (artifact-00)

### Expert synthesis and curation cautions (“warnings”)
1. **Gene markers are often non-specific across sulfur metabolisms.** Dsr-associated repertoires can occur in reductive, oxidative, and disproportionating contexts; DsrL/DsrD and dsrAB “types” can guide inference but do not fully resolve directionality. Do not curate a strong “dsrAB → disproportionation” edge without taxon- and context-specific evidence. (diao2023globaldiversityand pages 1-2)
2. **Campylobacterota disproportionation pathway is unresolved.** The inference that ST-27/ST-29 “must” use an alternative pathway is strong but remains mechanistically unidentified; edges should be curated as “unknown pathway present” rather than assigning Dsr/Sox/S4I modules. (wang2023disproportionationofinorganic pages 9-12)
3. **Elemental sulfur disproportionation is condition-dependent.** Include explicit edges for sulfide scavenging (Fe minerals) and low sulfur solubility/activation constraints; otherwise the graph will overpredict trait presence from gene content alone. (yan2024characterizationofsulfur pages 49-52, wang2023disproportionationofinorganic pages 12-13, wang2023disproportionationofinorganic pages 9-12)
4. **S4I pathway completion is taxon-structured.** Twible et al. show broad tsdA but narrow tetH distribution, implying possible community-level modularity (cross-feeding/complementation). Curate “tsdA-only taxa → tetrathionate production” and “tetH taxa → tetrathionate hydrolysis/disproportionation” as separate steps. (twible2024phandthiosulfate pages 5-6, twible2024phandthiosulfate pages 12-14)

### DOI-first bibliography (with URLs and dates)
| Citation (APA-ish) | Publication date (month/year) | DOI | URL | Study type | Key contribution to disproportionation trait curation |
|---|---|---|---|---|---|
| Wang, S., Jiang, L., Xie, S., Alain, K., Wang, Z., Wang, J., Liu, D., & Shao, Z. (2023). *Disproportionation of inorganic sulfur compounds by mesophilic chemolithoautotrophic Campylobacterota*. *mSystems*, 8(1). | Feb 2023 | 10.1128/msystems.00954-22 | https://doi.org/10.1128/msystems.00954-22 | Primary research | Direct experimental evidence that *Sulfurimonas* and *Sulfurovum* can disproportionate thiosulfate and elemental sulfur; shows Campylobacterota lack canonical apr/dsr modules, implying an alternative pathway; provides sulfur-contact and ferrihydrite/sulfide-scavenging mechanistic constraints. (wang2023disproportionationofinorganic pages 2-4, wang2023disproportionationofinorganic pages 1-2, wang2023disproportionationofinorganic pages 12-13, wang2023disproportionationofinorganic pages 9-12) |
| Whaley-Martin, K. J., Chen, L.-X., Nelson, T. C., Gordon, J., Kantor, R., Twible, L. E., Marshall, S., McGarry, S., Rossi, L., Bessette, B., Baron, C., Apte, S., Banfield, J. F., & Warren, L. A. (2023). *O2 partitioning of sulfur oxidizing bacteria drives acidity and thiosulfate distributions in mining waters*. *Nature Communications*, 14. | Apr 2023 | 10.1038/s41467-023-37426-8 | https://doi.org/10.1038/s41467-023-37426-8 | Primary research | Establishes environmental partitioning of Sox vs incomplete Sox+rDSR under oxic vs low-O2 conditions; links pathway choice to acidity and thiosulfate accumulation, useful for distinguishing disproportionation-adjacent sulfur recycling from complete oxidation. (whaleymartin2023o2partitioningof pages 1-2, whaleymartin2023o2partitioningof pages 7-9) |
| Diao, M., Dyksma, S., Koeksoy, E., Ngugi, D. K., Anantharaman, K., Loy, A., & Pester, M. (2023). *Global diversity and inferred ecophysiology of microorganisms with the potential for dissimilatory sulfate/sulfite reduction*. *FEMS Microbiology Reviews*, 47(5). | Sep 2023 | 10.1093/femsre/fuad058 | https://doi.org/10.1093/femsre/fuad058 | Review | Comprehensive framework for dsrAB-, dsrD-, and dsrL-based inference; clarifies that Dsr-associated gene sets can occur in reductive, oxidative, and disproportionating lineages, which is central for cautious node/edge curation. (diao2023globaldiversityand pages 1-2) |
| D’Ermo, G., Guiral, M., & Schoepp-Cothenet, B. (2024). *The Complex Interplay of Sulfur and Arsenic Bioenergetic Metabolisms in the Arsenic Geochemical Cycle*. In *Geomicrobiology: Natural and Anthropogenic Settings* (pp. 301–328). | Jan 2024 | 10.1007/978-3-031-54306-7_15 | https://doi.org/10.1007/978-3-031-54306-7_15 | Book chapter | Provides current mechanistic framing of sulfur disproportionation as simultaneous oxidation and reduction of one substrate; summarizes roles of SOR, TetH, TsdA/DoxDA, sHdr, and Dsr-linked sulfur transfer. (d’ermo2024thecomplexinterplay pages 5-8, d’ermo2024thecomplexinterplay pages 15-17, d’ermo2024thecomplexinterplay pages 12-15) |
| Twible, L. E., Whaley-Martin, K., Chen, L.-X., Nelson, T. C., Arrey, J. L. S., Jarolimek, C. V., King, J. J., Ramilo, L., Sonnenberg, H., Banfield, J. F., Apte, S. C., & Warren, L. A. (2024). *pH and thiosulfate dependent microbial sulfur oxidation strategies across diverse environments*. *Frontiers in Microbiology*, 15. | Jul 2024 | 10.3389/fmicb.2024.1426584 | https://doi.org/10.3389/fmicb.2024.1426584 | Primary research | Key 2024 source for S4I pathway partitioning: tsdA broadly distributed across pH, while tetH is mainly associated with *Thiobacillus* at circumneutral pH; useful for curating pH-dependent environmental edges and tetrathionate-processing nodes. (twible2024phandthiosulfate pages 1-2, twible2024phandthiosulfate pages 12-14, twible2024phandthiosulfate pages 5-6, twible2024phandthiosulfate pages 11-12) |
| Gordon, J., Apte, S. C., Nelson, T. E. C., Whaley-Martin, K. J., Twible, L. E., Chen, L., Liu, F., McGarry, S., Banfield, J. F., & Warren, L. A. (2024). *Microbial Sulfur Pathways and Outcomes in Tailings Impoundments: A Mesocosm Study*. *Mine Water and the Environment*, 43, 658–674. | Nov 2024 | 10.1007/s10230-024-01016-x | https://doi.org/10.1007/s10230-024-01016-x | Mesocosm study | Applied validation of gene- and transcript-based monitoring for sulfur pathways; quantifies that nitrate-coupled sulfur oxidation lowers proton yield versus O2-coupled oxidation, informing environmental-control edges and real-world implementation notes. (gordon2024microbialsulfurpathways pages 19-21, gordon2024microbialsulfurpathways pages 1-5, gordon2024microbialsulfurpathways pages 5-8) |
| Liu, Y., Macalady, J. L., Sánchez-España, J., & Burgos, W. D. (2024). *Enrichment of acid-tolerant sulfide-producing microbes from an acidic pit lake*. *Frontiers in Microbiology*, 15. | Oct 2024 | 10.3389/fmicb.2024.1475137 | https://doi.org/10.3389/fmicb.2024.1475137 | Primary research | Demonstrates engineered stimulation of sulfur cycling in acidic pit-lake bioremediation; supports importance of sulfur intermediates, electron-donor limitation, and sulfide production under extreme geochemistry. (liu2024enrichmentofacidtolerant pages 1-2) |
| Petushkova, E., Khasimov, M., Mayorova, E., Delegan, Y., Frantsuzova, E., Bogun, A., Galkina, E., & Tsygankov, A. (2024). *The Complete Genome of a Novel Typical Species Thiocapsa bogorovii and Analysis of Its Central Metabolic Pathways*. *Microorganisms*, 12(2), 391. | Feb 2024 | 10.3390/microorganisms12020391 | https://doi.org/10.3390/microorganisms12020391 | Primary genomics | Supplies candidate Sox and Dsr-system components in a purple sulfur bacterium discussed in relation to thiosulfate disproportionation-like sulfur transformations; useful for node expansion but weaker for direct trait assignment. (petushkova2024thecompletegenome pages 17-19, petushkova2024thecompletegenome pages 22-23, petushkova2024thecompletegenome pages 19-20, petushkova2024thecompletegenome pages 20-22) |
| Yan, Y. (2024). *Characterization of Sulfur Cycling in the First Oil Sands Pilot End Pit Lake, Base Mine Lake*. | 2024 |  |  | Thesis | Valuable synthesis for thermodynamics and candidate mechanisms: compares free energies of thiosulfate, sulfite, and elemental sulfur disproportionation; summarizes TetH, TsdA, and SOR roles and environmental distributions. Use cautiously because DOI/peer-review status is unclear. (yan2024characterizationofsulfur pages 49-52, yan2024characterizationofsulfur pages 42-46, yan2024characterizationofsulfur pages 59-63) |
| Lyons, T. W., Tino, C. J., Fournier, G. P., Anderson, R. E., Leavitt, W. D., Konhauser, K. O., & Stüeken, E. E. (2024). *Co-evolution of early Earth environments and microbial life*. *Nature Reviews Microbiology*, 22, 572–586. | May 2024 | 10.1038/s41579-024-01044-y | https://doi.org/10.1038/s41579-024-01044-y | Review | High-authority context source supporting the broader evolutionary significance of intermediate-valence sulfur pathways, including disproportionation, especially for interpreting habitat scope and ancient relevance. (whaleymartin2023o2partitioningof pages 1-2) |


*Table: This table lists the main sources used to curate the disproportionation trait, prioritizing recent DOI-based literature. It highlights each source’s study type and its specific value for defining scope, mechanisms, environmental controls, and curation-ready causal edges.*

### Visual evidence (figures)
Oxygen zoning and conceptual pathway partitioning in mine tailings impoundment waters is supported by retrieved figure crops from Whaley-Martin et al. 2023. (whaleymartin2023o2partitioningof media fcb04f5b, whaleymartin2023o2partitioningof media c5778ec5, whaleymartin2023o2partitioningof media a7d06b55)


References

1. (d’ermo2024thecomplexinterplay pages 5-8): Giulia D’Ermo, Marianne Guiral, and Barbara Schoepp-Cothenet. The complex interplay of sulfur and arsenic bioenergetic metabolisms in the arsenic geochemical cycle. Geomicrobiology: Natural and Anthropogenic Settings, pages 301-328, Jan 2024. URL: https://doi.org/10.1007/978-3-031-54306-7\_15, doi:10.1007/978-3-031-54306-7\_15. This article has 3 citations.

2. (wang2023disproportionationofinorganic pages 1-2): Shasha Wang, Lijing Jiang, Shaobin Xie, Karine Alain, Zhaodi Wang, Jun Wang, Delin Liu, and Zongze Shao. Disproportionation of inorganic sulfur compounds by mesophilic chemolithoautotrophic<i>campylobacterota</i>. Feb 2023. URL: https://doi.org/10.1128/msystems.00954-22, doi:10.1128/msystems.00954-22. This article has 36 citations and is from a peer-reviewed journal.

3. (yan2024characterizationofsulfur pages 49-52): Y Yan. Characterization of sulfur cycling in the first oil sands pilot end pit lake, base mine lake. Unknown journal, 2024.

4. (diao2023globaldiversityand pages 1-2): Muhe Diao, Stefan Dyksma, Elif Koeksoy, David Kamanda Ngugi, Karthik Anantharaman, Alexander Loy, and Michael Pester. Global diversity and inferred ecophysiology of microorganisms with the potential for dissimilatory sulfate/sulfite reduction. FEMS Microbiology Reviews, Sep 2023. URL: https://doi.org/10.1093/femsre/fuad058, doi:10.1093/femsre/fuad058. This article has 87 citations and is from a domain leading peer-reviewed journal.

5. (whaleymartin2023o2partitioningof pages 7-9): Kelly J. Whaley-Martin, Lin-Xing Chen, Tara Colenbrander Nelson, Jennifer Gordon, Rose Kantor, Lauren E. Twible, Stephanie Marshall, Sam McGarry, Laura Rossi, Benoit Bessette, Christian Baron, Simon Apte, Jillian F. Banfield, and Lesley A. Warren. O2 partitioning of sulfur oxidizing bacteria drives acidity and thiosulfate distributions in mining waters. Nature Communications, Apr 2023. URL: https://doi.org/10.1038/s41467-023-37426-8, doi:10.1038/s41467-023-37426-8. This article has 63 citations and is from a highest quality peer-reviewed journal.

6. (whaleymartin2023o2partitioningof pages 1-2): Kelly J. Whaley-Martin, Lin-Xing Chen, Tara Colenbrander Nelson, Jennifer Gordon, Rose Kantor, Lauren E. Twible, Stephanie Marshall, Sam McGarry, Laura Rossi, Benoit Bessette, Christian Baron, Simon Apte, Jillian F. Banfield, and Lesley A. Warren. O2 partitioning of sulfur oxidizing bacteria drives acidity and thiosulfate distributions in mining waters. Nature Communications, Apr 2023. URL: https://doi.org/10.1038/s41467-023-37426-8, doi:10.1038/s41467-023-37426-8. This article has 63 citations and is from a highest quality peer-reviewed journal.

7. (wang2023disproportionationofinorganic pages 9-12): Shasha Wang, Lijing Jiang, Shaobin Xie, Karine Alain, Zhaodi Wang, Jun Wang, Delin Liu, and Zongze Shao. Disproportionation of inorganic sulfur compounds by mesophilic chemolithoautotrophic<i>campylobacterota</i>. Feb 2023. URL: https://doi.org/10.1128/msystems.00954-22, doi:10.1128/msystems.00954-22. This article has 36 citations and is from a peer-reviewed journal.

8. (wang2023disproportionationofinorganic pages 12-13): Shasha Wang, Lijing Jiang, Shaobin Xie, Karine Alain, Zhaodi Wang, Jun Wang, Delin Liu, and Zongze Shao. Disproportionation of inorganic sulfur compounds by mesophilic chemolithoautotrophic<i>campylobacterota</i>. Feb 2023. URL: https://doi.org/10.1128/msystems.00954-22, doi:10.1128/msystems.00954-22. This article has 36 citations and is from a peer-reviewed journal.

9. (wang2023disproportionationofinorganic pages 2-4): Shasha Wang, Lijing Jiang, Shaobin Xie, Karine Alain, Zhaodi Wang, Jun Wang, Delin Liu, and Zongze Shao. Disproportionation of inorganic sulfur compounds by mesophilic chemolithoautotrophic<i>campylobacterota</i>. Feb 2023. URL: https://doi.org/10.1128/msystems.00954-22, doi:10.1128/msystems.00954-22. This article has 36 citations and is from a peer-reviewed journal.

10. (twible2024phandthiosulfate pages 12-14): Lauren E. Twible, Kelly Whaley-Martin, Lin-Xing Chen, Tara Colenbrander Nelson, James L.S. Arrey, Chad V. Jarolimek, Josh J. King, Lisa Ramilo, Helga Sonnenberg, Jillian F. Banfield, Simon C. Apte, and Lesley A. Warren. Ph and thiosulfate dependent microbial sulfur oxidation strategies across diverse environments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1426584, doi:10.3389/fmicb.2024.1426584. This article has 24 citations and is from a peer-reviewed journal.

11. (twible2024phandthiosulfate pages 5-6): Lauren E. Twible, Kelly Whaley-Martin, Lin-Xing Chen, Tara Colenbrander Nelson, James L.S. Arrey, Chad V. Jarolimek, Josh J. King, Lisa Ramilo, Helga Sonnenberg, Jillian F. Banfield, Simon C. Apte, and Lesley A. Warren. Ph and thiosulfate dependent microbial sulfur oxidation strategies across diverse environments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1426584, doi:10.3389/fmicb.2024.1426584. This article has 24 citations and is from a peer-reviewed journal.

12. (d’ermo2024thecomplexinterplay pages 15-17): Giulia D’Ermo, Marianne Guiral, and Barbara Schoepp-Cothenet. The complex interplay of sulfur and arsenic bioenergetic metabolisms in the arsenic geochemical cycle. Geomicrobiology: Natural and Anthropogenic Settings, pages 301-328, Jan 2024. URL: https://doi.org/10.1007/978-3-031-54306-7\_15, doi:10.1007/978-3-031-54306-7\_15. This article has 3 citations.

13. (d’ermo2024thecomplexinterplay pages 12-15): Giulia D’Ermo, Marianne Guiral, and Barbara Schoepp-Cothenet. The complex interplay of sulfur and arsenic bioenergetic metabolisms in the arsenic geochemical cycle. Geomicrobiology: Natural and Anthropogenic Settings, pages 301-328, Jan 2024. URL: https://doi.org/10.1007/978-3-031-54306-7\_15, doi:10.1007/978-3-031-54306-7\_15. This article has 3 citations.

14. (whaleymartin2023o2partitioningof media fcb04f5b): Kelly J. Whaley-Martin, Lin-Xing Chen, Tara Colenbrander Nelson, Jennifer Gordon, Rose Kantor, Lauren E. Twible, Stephanie Marshall, Sam McGarry, Laura Rossi, Benoit Bessette, Christian Baron, Simon Apte, Jillian F. Banfield, and Lesley A. Warren. O2 partitioning of sulfur oxidizing bacteria drives acidity and thiosulfate distributions in mining waters. Nature Communications, Apr 2023. URL: https://doi.org/10.1038/s41467-023-37426-8, doi:10.1038/s41467-023-37426-8. This article has 63 citations and is from a highest quality peer-reviewed journal.

15. (whaleymartin2023o2partitioningof media c5778ec5): Kelly J. Whaley-Martin, Lin-Xing Chen, Tara Colenbrander Nelson, Jennifer Gordon, Rose Kantor, Lauren E. Twible, Stephanie Marshall, Sam McGarry, Laura Rossi, Benoit Bessette, Christian Baron, Simon Apte, Jillian F. Banfield, and Lesley A. Warren. O2 partitioning of sulfur oxidizing bacteria drives acidity and thiosulfate distributions in mining waters. Nature Communications, Apr 2023. URL: https://doi.org/10.1038/s41467-023-37426-8, doi:10.1038/s41467-023-37426-8. This article has 63 citations and is from a highest quality peer-reviewed journal.

16. (whaleymartin2023o2partitioningof media a7d06b55): Kelly J. Whaley-Martin, Lin-Xing Chen, Tara Colenbrander Nelson, Jennifer Gordon, Rose Kantor, Lauren E. Twible, Stephanie Marshall, Sam McGarry, Laura Rossi, Benoit Bessette, Christian Baron, Simon Apte, Jillian F. Banfield, and Lesley A. Warren. O2 partitioning of sulfur oxidizing bacteria drives acidity and thiosulfate distributions in mining waters. Nature Communications, Apr 2023. URL: https://doi.org/10.1038/s41467-023-37426-8, doi:10.1038/s41467-023-37426-8. This article has 63 citations and is from a highest quality peer-reviewed journal.

17. (gordon2024microbialsulfurpathways pages 1-5): Jay Gordon, Simon C. Apte, Tara E. Colenbrander Nelson, Kelly J. Whaley-Martin, Lauren E. Twible, LinXing Chen, Felicia Liu, Samantha McGarry, Jillian F. Banfield, and Lesley A. Warren. Microbial sulfur pathways and outcomes in tailings impoundments: a mesocosm study. Mine Water and the Environment, 43:658-674, Nov 2024. URL: https://doi.org/10.1007/s10230-024-01016-x, doi:10.1007/s10230-024-01016-x. This article has 3 citations and is from a peer-reviewed journal.

18. (gordon2024microbialsulfurpathways pages 5-8): Jay Gordon, Simon C. Apte, Tara E. Colenbrander Nelson, Kelly J. Whaley-Martin, Lauren E. Twible, LinXing Chen, Felicia Liu, Samantha McGarry, Jillian F. Banfield, and Lesley A. Warren. Microbial sulfur pathways and outcomes in tailings impoundments: a mesocosm study. Mine Water and the Environment, 43:658-674, Nov 2024. URL: https://doi.org/10.1007/s10230-024-01016-x, doi:10.1007/s10230-024-01016-x. This article has 3 citations and is from a peer-reviewed journal.

19. (gordon2024microbialsulfurpathways pages 19-21): Jay Gordon, Simon C. Apte, Tara E. Colenbrander Nelson, Kelly J. Whaley-Martin, Lauren E. Twible, LinXing Chen, Felicia Liu, Samantha McGarry, Jillian F. Banfield, and Lesley A. Warren. Microbial sulfur pathways and outcomes in tailings impoundments: a mesocosm study. Mine Water and the Environment, 43:658-674, Nov 2024. URL: https://doi.org/10.1007/s10230-024-01016-x, doi:10.1007/s10230-024-01016-x. This article has 3 citations and is from a peer-reviewed journal.

20. (liu2024enrichmentofacidtolerant pages 1-2): Yutong Liu, Jennifer L. Macalady, Javier Sánchez-España, and William D. Burgos. Enrichment of acid-tolerant sulfide-producing microbes from an acidic pit lake. Frontiers in Microbiology, Oct 2024. URL: https://doi.org/10.3389/fmicb.2024.1475137, doi:10.3389/fmicb.2024.1475137. This article has 8 citations and is from a peer-reviewed journal.

21. (twible2024phandthiosulfate pages 1-2): Lauren E. Twible, Kelly Whaley-Martin, Lin-Xing Chen, Tara Colenbrander Nelson, James L.S. Arrey, Chad V. Jarolimek, Josh J. King, Lisa Ramilo, Helga Sonnenberg, Jillian F. Banfield, Simon C. Apte, and Lesley A. Warren. Ph and thiosulfate dependent microbial sulfur oxidation strategies across diverse environments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1426584, doi:10.3389/fmicb.2024.1426584. This article has 24 citations and is from a peer-reviewed journal.

22. (germe2023giuliadermo pages 21-24): SA Germe. Giulia d'ermo. Unknown journal, 2023.

23. (petushkova2024thecompletegenome pages 22-23): Ekaterina Petushkova, Makhmadyusuf Khasimov, Ekaterina Mayorova, Yanina Delegan, Ekaterina Frantsuzova, Alexander Bogun, Elena Galkina, and Anatoly Tsygankov. The complete genome of a novel typical species thiocapsa bogorovii and analysis of its central metabolic pathways. Microorganisms, 12:391, Feb 2024. URL: https://doi.org/10.3390/microorganisms12020391, doi:10.3390/microorganisms12020391. This article has 6 citations.

24. (petushkova2024thecompletegenome pages 20-22): Ekaterina Petushkova, Makhmadyusuf Khasimov, Ekaterina Mayorova, Yanina Delegan, Ekaterina Frantsuzova, Alexander Bogun, Elena Galkina, and Anatoly Tsygankov. The complete genome of a novel typical species thiocapsa bogorovii and analysis of its central metabolic pathways. Microorganisms, 12:391, Feb 2024. URL: https://doi.org/10.3390/microorganisms12020391, doi:10.3390/microorganisms12020391. This article has 6 citations.

25. (yan2024characterizationofsulfur pages 59-63): Y Yan. Characterization of sulfur cycling in the first oil sands pilot end pit lake, base mine lake. Unknown journal, 2024.

26. (germe2023giuliadermo pages 24-28): SA Germe. Giulia d'ermo. Unknown journal, 2023.

27. (petushkova2024thecompletegenome pages 17-19): Ekaterina Petushkova, Makhmadyusuf Khasimov, Ekaterina Mayorova, Yanina Delegan, Ekaterina Frantsuzova, Alexander Bogun, Elena Galkina, and Anatoly Tsygankov. The complete genome of a novel typical species thiocapsa bogorovii and analysis of its central metabolic pathways. Microorganisms, 12:391, Feb 2024. URL: https://doi.org/10.3390/microorganisms12020391, doi:10.3390/microorganisms12020391. This article has 6 citations.

28. (petushkova2024thecompletegenome pages 19-20): Ekaterina Petushkova, Makhmadyusuf Khasimov, Ekaterina Mayorova, Yanina Delegan, Ekaterina Frantsuzova, Alexander Bogun, Elena Galkina, and Anatoly Tsygankov. The complete genome of a novel typical species thiocapsa bogorovii and analysis of its central metabolic pathways. Microorganisms, 12:391, Feb 2024. URL: https://doi.org/10.3390/microorganisms12020391, doi:10.3390/microorganisms12020391. This article has 6 citations.

29. (yan2024characterizationofsulfur pages 42-46): Y Yan. Characterization of sulfur cycling in the first oil sands pilot end pit lake, base mine lake. Unknown journal, 2024.

30. (twible2024phandthiosulfate pages 11-12): Lauren E. Twible, Kelly Whaley-Martin, Lin-Xing Chen, Tara Colenbrander Nelson, James L.S. Arrey, Chad V. Jarolimek, Josh J. King, Lisa Ramilo, Helga Sonnenberg, Jillian F. Banfield, Simon C. Apte, and Lesley A. Warren. Ph and thiosulfate dependent microbial sulfur oxidation strategies across diverse environments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1426584, doi:10.3389/fmicb.2024.1426584. This article has 24 citations and is from a peer-reviewed journal.