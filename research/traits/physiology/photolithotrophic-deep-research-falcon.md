---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T12:17:04.838308'
end_time: '2026-06-18T12:29:36.788196'
duration_seconds: 751.95
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: photolithotrophic
  trait_identifier: METPO:1000658
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: photolithotrophic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic type in which an organism uses light as the energy source
    and inorganic compounds as electron donors, typically with carbon dioxide as the
    primary carbon source.
  parent_traits: METPO:1000631
  synonyms: photolithotroph
  evidence_summary: 'DOI:10.3390/antiox10060829: anoxygenic photosynthesis (Review
    supports light-driven oxidation of reduced sulfur compounds by photolithotrophic
    sulfur bacteria.) | DOI:10.3389/fmicb.2017.00323: light as an energy source and
    reduced iron (Review supports Fe(II) as an inorganic electron donor for photoferrotrophy.)'
  causal_graph_summary: 'photolithotrophic_inorganic_electron_donors: 8 nodes, 8 edges'
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
- **Trait label:** photolithotrophic
- **METPO identifier:** METPO:1000658
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism uses light as the energy source and inorganic compounds as electron donors, typically with carbon dioxide as the primary carbon source.
- **Parent traits:** METPO:1000631
- **Synonyms:** photolithotroph
- **Existing evidence:** DOI:10.3390/antiox10060829: anoxygenic photosynthesis (Review supports light-driven oxidation of reduced sulfur compounds by photolithotrophic sulfur bacteria.) | DOI:10.3389/fmicb.2017.00323: light as an energy source and reduced iron (Review supports Fe(II) as an inorganic electron donor for photoferrotrophy.)
- **Existing causal graph summary:** photolithotrophic_inorganic_electron_donors: 8 nodes, 8 edges

## Research Objective

Research the microbial trait **photolithotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/photolithotrophic.yaml`.

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
- **Trait label:** photolithotrophic
- **METPO identifier:** METPO:1000658
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism uses light as the energy source and inorganic compounds as electron donors, typically with carbon dioxide as the primary carbon source.
- **Parent traits:** METPO:1000631
- **Synonyms:** photolithotroph
- **Existing evidence:** DOI:10.3390/antiox10060829: anoxygenic photosynthesis (Review supports light-driven oxidation of reduced sulfur compounds by photolithotrophic sulfur bacteria.) | DOI:10.3389/fmicb.2017.00323: light as an energy source and reduced iron (Review supports Fe(II) as an inorganic electron donor for photoferrotrophy.)
- **Existing causal graph summary:** photolithotrophic_inorganic_electron_donors: 8 nodes, 8 edges

## Research Objective

Research the microbial trait **photolithotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/photolithotrophic.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **photolithotrophic** (METPO:1000658)

**Trait label:** photolithotrophic (syn. photolithotroph)  
**Trait category:** PHYSIOLOGY; **Term kind:** CLASS; **Mapping status:** REVIEWED  
**Working definition (for TraitMech):** capacity for **light-driven energy conservation** coupled to oxidation of **inorganic electron donors**, commonly paired with **CO2 fixation** (photolithoautotrophy), but including facultative/mixotrophic boundary cases in some anoxygenic phototrophs (notably purple sulfur bacteria). (kushkevych2024anoxygenicphotosynthesiswith pages 1-2, zhuang2024electrontransferin pages 6-8)

### 1) Trait scope (phenotype and boundaries)

**Core phenotype.** Photolithotrophy denotes light-powered metabolism in which electrons are obtained from inorganic substrates (for example, **H2S**, **H2**, **Fe(II)**, **elemental sulfur**, **thiosulfate**, and for oxygenic phototrophy **H2O**) and used to drive photochemical electron transfer and (often) carbon fixation. In a 2024 review focusing on green sulfur bacteria (GSB) and purple sulfur bacteria (PSB), anoxygenic photosynthesis is explicitly described as using **H2S as the main electron donor** (instead of water) and proceeding in environments where H2S is abundant (kushkevych2024anoxygenicphotosynthesiswith pages 1-2). A 2024 sulfur-cycle review states that colored sulfur bacteria “oxidize sulfide, thiosulfate, and elemental sulfur for photosynthetic growth (anoxygenic photosynthetic CO2 fixation)” (zhuang2024electrontransferin pages 6-8).

**Oxygenic vs anoxygenic photolithotrophy.** Oxygenic photolithotrophy (cyanobacteria and plastids) uses water as the electron donor, producing O2; anoxygenic photolithotrophy uses alternative electron donors (e.g., H2S, H2, Fe(II)) and does not produce O2 (kushkevych2024anoxygenicphotosynthesiswith pages 1-2). Gene-marker criteria used in recent work distinguish these modes: cyanobacteria carry genes for both photosystems (psaB, psbA), whereas anoxygenic phototrophs are identified by Type I (pshA) or Type II (pufL) reaction-center genes (nikeleit2024inhibitionofphototrophic pages 11-17).

**Distinguishing from nearby traits.**
- **Photoorganotrophy:** light as energy source but **organic** electron donors/carbon sources; PSB can use organic compounds, making them **facultative photolithotrophs**, i.e., boundary-case mixotrophy (zhuang2024electrontransferin pages 6-8).
- **Chemolithotrophy:** uses inorganic electron donors but energy from chemical reactions rather than light; treated here as a separate trophic mode despite overlapping donor sets.

**Boundary cases that require careful curation.**
- **Facultative photolithotrophy / mixotrophy:** PSB may switch between inorganic and organic electron donors depending on conditions (zhuang2024electrontransferin pages 6-8). Curate as conditional edges (environmental substrate availability → donor choice) rather than as constitutive trait nodes.
- **Electrotrophy/electrosynthesis interfaces:** electron uptake via direct interspecies electron transfer (DIET) or electrodes can support “syntrophic anaerobic photosynthesis” for a green sulfur bacterium (P. aestuarii), but this is assay- and partner-dependent (zhuang2024electrontransferin pages 6-8). Consider curating as an auxiliary module (EET-enabled phototrophy) rather than core photolithotrophy.

### 2) Current understanding: key concepts and mechanistic definitions

**Phototrophic sulfur bacteria (GSB/PSB).** A 2024 review summarizes that anoxygenic phototrophs—especially GSB (Chlorobiaceae) and PSB (Chromatiaceae)—use H2S as the principal electron donor, oxidize it to elemental sulfur, and use specialized antenna structures (**chlorosomes**) (kushkevych2024anoxygenicphotosynthesiswith pages 1-2). Chlorosomes are described as lipid-mono-layer vesicles serving as light-collecting antennas; the review highlights them as unusually efficient light-harvesting complexes (kushkevych2024anoxygenicphotosynthesiswith pages 1-2, kushkevych2024anoxygenicphotosynthesiswith pages 4-6). Carbon is commonly fixed from CO2 via the **reverse tricarboxylic acid (rTCA) cycle** in GSB (kushkevych2024anoxygenicphotosynthesiswith pages 1-2).

**Photoferrotrophy (iron-based photolithotrophy).** Photoferrotrophy is described as “oxidation of reduced iron via anoxygenic photosynthesis” (nishihara2024illuminatingthecoevolution pages 1-2) and experimentally investigated as phototrophic Fe(II) oxidation in modern ferruginous contexts (nikeleit2024inhibitionofphototrophic pages 9-11).

**Gene/marker-level definitions.** In recent photoferrotrophy work, phototrophic types are operationally identified via reaction-center genes: **pshA** (Type I RC) and **pufL** (Type II RC) for anoxygenic phototrophs, and **psaB** (PSI) plus **psbA** (PSII) for cyanobacteria (nikeleit2024inhibitionofphototrophic pages 11-17). This is useful for trait inference in genomes/metagenomes but should be curated as *annotation logic* rather than strict causality.

### 3) Recent developments (prioritizing 2023–2024)

**(a) Updated mechanistic synthesis for anoxygenic phototrophy and biotechnological framing.** Kushkevych et al. (published **11 July 2024**) frame anoxygenic phototrophs as potential tools for **hydrogen sulfide detoxification** in anoxic environments and discuss chlorosome-based light capture, sulfur oxidation to elemental sulfur, and rTCA carbon fixation (kushkevych2024anoxygenicphotosynthesiswith pages 1-2).

**(b) New insights into ecological electron-transfer couplings relevant to photolithotrophy.** Zhuang et al. (published **May 2024**) review syntrophic couplings where a phototrophic green sulfur bacterium accepts electrons via **DIET** from Geobacter or from electrodes; growth fails when the Geobacter partner lacks a “trans-outer membrane porin-cytochrome protein complex required for DIET” (zhuang2024electrontransferin pages 6-8). They also summarize long-distance electron transfer (LDET) in cable bacteria via conductive fibers containing a sulfur-ligated nickel group (zhuang2024electrontransferin pages 6-8). These findings motivate adding EET/DIET/LDET nodes as *environmental/consortial enabling mechanisms* rather than core photolithotrophy.

**(c) Strong inhibitor constraints on photoferrotrophy.** Nikeleit et al. (published **Oct 2024**) show that nitric oxide can suppress photoferrotrophic Fe(II) oxidation; model/experiment details indicate suppression for *Rhodobacter ferrooxidans* SW2 at **12 nM NO** (nikeleit2024inhibitionofphototrophic pages 9-11). This provides a concrete inhibitor node/edge that is highly curation-relevant.

**(d) Evolutionary synthesis tying donors and photosynthetic apparatus to early Earth.** Nishihara et al. (published **Jun 2024**) link chlorophototrophy to donor diversity including “H2O, H2S, and Fe2+” and co-evolution of reaction centers, pigment synthesis, and carbon fixation (Calvin-cycle components mentioned) (nishihara2024illuminatingthecoevolution pages 1-2, nishihara2024illuminatingthecoevolution pages 9-9). This supports cross-branch mechanistic nodes (reaction centers, pigment reductases, carbon fixation modules) even though TraitMech curation may focus on proximate physiology rather than deep evolution.

### 4) Candidate nodes for `photolithotrophic.yaml` (grouped by type)

#### A. Pathways / modules
- **Anoxygenic photosynthesis** (GO:0015979; candidate) (kushkevych2024anoxygenicphotosynthesiswith pages 1-2)
- **Photosystem I** (GO:0009522) and **Photosystem II** (GO:0009523) for oxygenic phototrophs (nikeleit2024inhibitionofphototrophic pages 11-17)
- **rTCA / reverse tricarboxylic acid cycle** (KEGG module candidate; label-only acceptable) (kushkevych2024anoxygenicphotosynthesiswith pages 1-2) (kushkevych2024anoxygenicphotosynthesiswith media 594d816a)
- **Sulfur oxidation / sulfur globule oxidation** (label-only; see Dsr system dependency) (zhuang2024electrontransferin pages 14-15)
- **Extracellular electron transfer (EET) / DIET / LDET** (label-only) (zhuang2024electrontransferin pages 6-8)

#### B. Genes / proteins / complexes (candidate grounding)
- **Reaction-center marker genes:** pshA (Type I RC), pufL (Type II RC); psaB (PSI), psbA (PSII) (nikeleit2024inhibitionofphototrophic pages 11-17)
- **Chlorosomes** (GSB antenna organelle; label-only) (kushkevych2024anoxygenicphotosynthesiswith pages 1-2)
- **FMO complex** (Fenna–Matthews–Olson; label-only) (supported by figure retrieval in the same review) (kushkevych2024anoxygenicphotosynthesiswith media d9f16891)
- **Dsr system**: dissimilatory sulfite reductase system (module; label-only / EC mapping uncertain at module level) (zhuang2024electrontransferin pages 14-15)
- **Porin–cytochrome complex (trans-outer membrane) required for DIET** (label-only; partner-dependent) (zhuang2024electrontransferin pages 6-8)
- **Conductive periplasmic fibers with sulfur-ligated nickel group** (label-only; cable bacteria) (zhuang2024electrontransferin pages 6-8)

#### C. Chemicals (CHEBI grounding where available)
- **Light** (CHEBI:25212; candidate)
- **CO2** (CHEBI:16526) (kushkevych2024anoxygenicphotosynthesiswith pages 1-2)
- **H2S** (CHEBI:16136) (kushkevych2024anoxygenicphotosynthesiswith pages 1-2)
- **Elemental sulfur (S0)** (CHEBI:26806) (kushkevych2024anoxygenicphotosynthesiswith pages 1-2)
- **Thiosulfate** (CHEBI identifier not provided in evidence; label-only) (zhuang2024electrontransferin pages 6-8)
- **Ferrous iron Fe(II)** (CHEBI:29033; candidate) (nikeleit2024inhibitionofphototrophic pages 9-11)
- **Nitric oxide (NO)** (CHEBI:16480) (nikeleit2024inhibitionofphototrophic pages 9-11)
- **Oxygen (O2)** (CHEBI:18420) and **nitrate** (CHEBI:17632) (as acceptors in cable bacteria redox separation) (zhuang2024electrontransferin pages 6-8)

#### D. Environmental / experimental factors (ENVO grounding often required; label-only here)
- **Anoxic, sulfidic environments** (“anoxic … characterized by both sulfide and light”; “ecosystems where H2S is abundant”) (zhuang2024electrontransferin pages 6-8, kushkevych2024anoxygenicphotosynthesiswith pages 1-2)
- **Ferruginous environments** (photoferrotrophy context) (nikeleit2024inhibitionofphototrophic pages 9-11)
- **Light intensity** (10 kLx vs 25 kLx affecting desulfurization performance) (kushkevych2024anoxygenicphotosynthesiswith pages 16-17)

### 5) Evidence-backed causal edges (curation-ready)

The following artifact provides candidate edges as subject–predicate–object triples with a direct evidence snippet and notes on strength/uncertainty.

| Subject (node + CURIE if available) | Predicate | Object (node + CURIE if available) | Evidence snippet (verbatim/near-verbatim quote) | Source (DOI, year, URL) | Strength/notes |
|---|---|---|---|---|---|
| light [CHEBI:25212, candidate] | excites / provides energy to | photosynthetic reaction center [GO:0009773] | “the process of anoxygenic photosynthesis from the capture of a light quantum through the transport of an excited electron” (kushkevych2024anoxygenicphotosynthesiswith pages 1-2) | 10.3389/fmicb.2024.1417714, 2024, https://doi.org/10.3389/fmicb.2024.1417714 | Strong for anoxygenic phototrophs; general process statement rather than a single gene-level mechanism. |
| chlorosome [label-only candidate] | enables | efficient light harvesting [GO:0009765, candidate] | “Chlorosomes are vesicles that are surrounded by a lipid monolayer that serve as light-collecting antennas” and are “the most efficient light-harvesting complexes known” (kushkevych2024anoxygenicphotosynthesiswith pages 1-2, kushkevych2024anoxygenicphotosynthesiswith pages 4-6) | 10.3389/fmicb.2024.1417714, 2024, https://doi.org/10.3389/fmicb.2024.1417714 | Strong but mostly for green sulfur bacteria (GSB). |
| chlorosome [label-only candidate] | supports | growth under low light [ENVO:low light, candidate] | “GSB can grow better under low light intensity” and possess chlorosomes as light-collecting antennas (kushkevych2024anoxygenicphotosynthesiswith pages 1-2) | 10.3389/fmicb.2024.1417714, 2024, https://doi.org/10.3389/fmicb.2024.1417714 | Moderate, inferred by combining adjacent statements in same source; taxon-specific to GSB. |
| hydrogen sulfide [CHEBI:16136] | acts_as_electron_donor_for | anoxygenic photosynthesis [GO:0015979] | “In anoxygenic photosynthesis, hydrogen sulfide (H2S) is used as the main electron donor” (kushkevych2024anoxygenicphotosynthesiswith pages 1-2) | 10.3389/fmicb.2024.1417714, 2024, https://doi.org/10.3389/fmicb.2024.1417714 | Strong; canonical edge for sulfur photolithotrophy. |
| green sulfur bacteria (Chlorobiaceae) [NCBITaxon:label-only candidate] | oxidizes | hydrogen sulfide [CHEBI:16136] | “GSB oxidize H2S to elemental sulfur” (kushkevych2024anoxygenicphotosynthesiswith pages 1-2) | 10.3389/fmicb.2024.1417714, 2024, https://doi.org/10.3389/fmicb.2024.1417714 | Strong; taxon-specific. |
| hydrogen sulfide oxidation [label-only candidate] | produces | elemental sulfur [CHEBI:26806] | “GSB oxidize H2S to elemental sulfur” (kushkevych2024anoxygenicphotosynthesiswith pages 1-2) | 10.3389/fmicb.2024.1417714, 2024, https://doi.org/10.3389/fmicb.2024.1417714 | Strong; product edge from same statement. |
| reduced sulfur compounds [CHEBI:label-only candidate] | supports | photosynthetic CO2 fixation [GO:0015977, candidate] | “oxidize sulfide, thiosulfate, and elemental sulfur for photosynthetic growth (anoxygenic photosynthetic CO2 fixation)” (zhuang2024electrontransferin pages 6-8) | 10.3390/life14050591, 2024, https://doi.org/10.3390/life14050591 | Strong for colored sulfur bacteria in anoxic sulfidic habitats. |
| carbon dioxide [CHEBI:16526] | is_assimilated_via | reverse tricarboxylic acid cycle [KEGG: M00173 candidate / label-only] | “The carbon source of GSB is carbon dioxide, which is assimilated through the reverse tricarboxylic acid cycle” (kushkevych2024anoxygenicphotosynthesiswith pages 1-2) | 10.3389/fmicb.2024.1417714, 2024, https://doi.org/10.3389/fmicb.2024.1417714 | Strong; GSB-focused. |
| reverse tricarboxylic acid cycle [KEGG:M00173 candidate / label-only] | enables | CO2 assimilation [GO:0015977, candidate] | “The carbon source of GSB is carbon dioxide, which is assimilated through the reverse tricarboxylic acid cycle” (kushkevych2024anoxygenicphotosynthesiswith pages 1-2) | 10.3389/fmicb.2024.1417714, 2024, https://doi.org/10.3389/fmicb.2024.1417714 | Strong; useful pathway-level node for photolithoautotrophy. |
| dissimilatory sulfite reductase system (Dsr) [GO:0000103 candidate / EC:1.8.99.5 related] | required_for | sulfur globule oxidation [label-only candidate] | “Sulfur globule oxidation in green sulfur bacteria is dependent on the dissimilatory sulfite reductase system” (zhuang2024electrontransferin pages 14-15) | 10.3390/life14050591, 2024, https://doi.org/10.3390/life14050591 | Strong; directly phrased as dependency, but specific to green sulfur bacteria. |
| pshA gene [label-only candidate] | marker_for | Type I reaction center [label-only candidate] | “Anoxygenic phototrophs were identified by possession of genes encoding for Type I (pshA) or Type II (pufL) reaction centers” (nikeleit2024inhibitionofphototrophic pages 11-17) | 10.1038/s41561-024-01560-9, 2024, https://doi.org/10.1038/s41561-024-01560-9 | Strong marker edge; identification/annotation rather than mechanistic causation. |
| pufL gene [label-only candidate] | marker_for | Type II reaction center [label-only candidate] | “Anoxygenic phototrophs were identified by possession of genes encoding for Type I (pshA) or Type II (pufL) reaction centers” (nikeleit2024inhibitionofphototrophic pages 11-17) | 10.1038/s41561-024-01560-9, 2024, https://doi.org/10.1038/s41561-024-01560-9 | Strong marker edge; identification/annotation rather than mechanistic causation. |
| psaB gene [label-only candidate] | marker_for | photosystem I [GO:0009522] | “Cyanobacteria are identified by the presence of genes for both types of reaction center, photosystem I (psaB) and photosystem II (psbA)” (nikeleit2024inhibitionofphototrophic pages 11-17) | 10.1038/s41561-024-01560-9, 2024, https://doi.org/10.1038/s41561-024-01560-9 | Strong marker edge for oxygenic photolithotrophs/cyanobacteria. |
| psbA gene [label-only candidate] | marker_for | photosystem II [GO:0009523] | “Cyanobacteria are identified by the presence of genes for both types of reaction center, photosystem I (psaB) and photosystem II (psbA)” (nikeleit2024inhibitionofphototrophic pages 11-17) | 10.1038/s41561-024-01560-9, 2024, https://doi.org/10.1038/s41561-024-01560-9 | Strong marker edge for oxygenic photolithotrophs/cyanobacteria. |
| Fe(II) oxidation [CHEBI:29033, candidate ferrous iron] | defines / supports | photoferrotrophy [METPO:label-only candidate] | “Anoxygenic phototrophic Fe(II) oxidizers (photoferrotrophs)” and “Photoferrotrophy is the oxidation of reduced iron via anoxygenic photosynthesis” (nikeleit2024inhibitionofphototrophic pages 17-17, nishihara2024illuminatingthecoevolution pages 1-2) | 10.1038/s41561-024-01560-9, 2024, https://doi.org/10.1038/s41561-024-01560-9 ; 10.1038/s41579-024-01044-y, 2024, https://doi.org/10.1038/s41579-024-01044-y | Strong definitional edge; specialized subtype of photolithotrophy. |
| nitric oxide [CHEBI:16480] | inhibits | phototrophic Fe(II) oxidation [label-only candidate] | “NO has a limiting effect on photoferrotrophy, even at very low …” and “the activity of R. ferrooxidans SW2 is suppressed at the NO concentration of 12 nM” (nikeleit2024inhibitionofphototrophic pages 17-17, nikeleit2024inhibitionofphototrophic pages 9-11) | 10.1038/s41561-024-01560-9, 2024, https://doi.org/10.1038/s41561-024-01560-9 | Strong but assay-specific to incubations; 12 nM value is model/experiment parameter for SW2. |
| trans-outer membrane porin-cytochrome protein complex [label-only candidate] | required_for | DIET to Prosthecochloris aestuarii [NCBITaxon:label-only candidate] | “P. aestuarii does not grow in co-culture with a G. sulfurreducens deletion mutant lacking a trans-outer membrane porin-cytochrome protein complex required for DIET” (zhuang2024electrontransferin pages 6-8) | 10.3390/life14050591, 2024, https://doi.org/10.3390/life14050591 | Strong, but specific to syntrophic anaerobic photosynthesis assay/coculture. |
| conductive periplasmic fibers with sulfur-ligated nickel group [label-only candidate] | enables | long-distance electron transfer [GO:0019646 candidate / label-only] | “electron transfer occurs via highly conductive fibers” and “the periplasmic fibers consist of a conductive protein core containing a sulfur-ligated nickel group” (zhuang2024electrontransferin pages 6-8) | 10.3390/life14050591, 2024, https://doi.org/10.3390/life14050591 | Strong for cable bacteria; not direct photolithotrophy but relevant inorganic-electron-transfer module. |
| long-distance electron transfer in cable bacteria [label-only candidate] | couples | H2S oxidation to O2/nitrate reduction [CHEBI:18420, CHEBI:17632 / label-only] | “the gradients in cytochrome redox states depended on an intact electrical connection between the electron donor H2S and the electron acceptor O2” and cable bacteria “reduce oxygen or nitrate” (zhuang2024electrontransferin pages 6-8) | 10.3390/life14050591, 2024, https://doi.org/10.3390/life14050591 | Strong for cable bacteria in sediments; adjacent ecological analog rather than core photolithotrophic trait. |
| lower light intensity (10 kLx) [label-only candidate] | increases | desulfurization effectiveness relative to 25 kLx [label-only candidate] | “At a light intensity of 10 kLx, desulfurization was more effective than at 25 kLx, when Cbi. limicola grew more slowly and A. vinosum stopped growing completely” (kushkevych2024anoxygenicphotosynthesiswith pages 16-17) | 10.3389/fmicb.2024.1417714, 2024, https://doi.org/10.3389/fmicb.2024.1417714 | Strong but reactor/assay-specific; likely species- and setup-dependent. |
| darkness [ENVO:label-only candidate] | increases | microbial electrochemical cell current [label-only candidate] | “When the consortium was cultivated in the dark, a current of 118 ± 16 μA was generated, but in the light it dropped to 61 ± 11 μA within 10 min” (kushkevych2024anoxygenicphotosynthesiswith pages 16-17) | 10.3389/fmicb.2024.1417714, 2024, https://doi.org/10.3389/fmicb.2024.1417714 | Strong quantitative application edge; coculture-specific and reflects electron partitioning, not universal photolithotrophic behavior. |


*Table: This table assembles curation-ready candidate causal edges for the photolithotrophic trait, using only the provided context IDs. It covers core mechanisms, gene markers, environmental controls, and application-relevant assay observations with quotable evidence and notes on scope or uncertainty.*

### 6) Current applications and real-world implementations (with recent quantitative data)

#### A. H2S detoxification and desulfurization (biogas/natural gas/wastewater)
- The 2024 GSB/PSB review explicitly motivates “biotechnological removal of H2S through microbial oxidation” and notes that the “product is most often elemental sulfur… easily separated” (kushkevych2024anoxygenicphotosynthesiswith pages 1-2). This supports curation of an *application edge* (H2S-rich waste stream → phototrophic sulfur bacteria growth/oxidation → elemental sulfur accumulation).
- For **biogas**, the review notes H2S can occur “up to 3%” depending on raw material (kushkevych2024anoxygenicphotosynthesiswith pages 16-17). In a synthetic biogas experiment (70% methane, 29.5% CO2, 0.5% H2S), “After 7 days… complete desulfurization occurred”; after increasing H2S to 1%, added H2S was removed (kushkevych2024anoxygenicphotosynthesiswith pages 16-17). These values can be curated as assay-specific edges linking gas composition and time to performance.
- **Light-intensity dependence:** “At a light intensity of 10 kLx, desulfurization was more effective than at 25 kLx” in an experiment comparing *Chlorobium limicola* (GSB) and *Allochromatium vinosum* (PSB) (kushkevych2024anoxygenicphotosynthesiswith pages 16-17). This supports an environmental-factor edge but should be flagged as system- and species-specific.

#### B. Microbial electrochemical cells (phototroph–electrogen partnership)
A microbial electrochemical consortium comprising GSB (*Cbi. limicola*) and *Geobacter sulfurreducens* generated measurable current without external organic substrate addition; reported currents were **118 ± 16 μA in the dark**, dropping to **61 ± 11 μA within 10 min in the light** (kushkevych2024anoxygenicphotosynthesiswith pages 16-17). Mechanistically, the authors hypothesize electron diversion to elemental sulfur in the light (kushkevych2024anoxygenicphotosynthesiswith pages 16-17). This is a real-world implementation concept (photobiocathode/anode consortia) and motivates nodes for glycogen cycling, acetate, anode electron acceptor, and sulfur recycling—though several of these were not fully grounded in the extracted snippets.

#### C. Geobiological modeling/interpretation (photoferrotrophy constraints)
Nikeleit et al. provide a quantitative inhibitory constraint: phototrophic Fe(II) oxidation activity for *R. ferrooxidans* SW2 “is suppressed at the NO concentration of **12 nM**” (nikeleit2024inhibitionofphototrophic pages 9-11). This supports incorporating **NO** (and potentially nitrite-driven NO production) as an inhibitor node that can shape photolithotrophic iron oxidation in ferruginous settings.

### 7) Expert synthesis and analysis (authoritative sources)

**Mechanistic consensus:** Recent reviews converge on a modular view of photolithotrophy: (i) light harvesting (chlorosomes in GSB), (ii) photochemical charge separation at reaction centers/photosystems, (iii) replenishment of electrons from inorganic donors (e.g., H2S; Fe(II) for photoferrotrophy), and (iv) CO2 fixation via a pathway suited to redox/energy constraints (rTCA in GSB) (kushkevych2024anoxygenicphotosynthesiswith pages 1-2, zhuang2024electrontransferin pages 6-8). Visual schematics in the 2024 GSB review support these modules, including differences between oxygenic and anoxygenic phototrophs and a dedicated rTCA diagram (kushkevych2024anoxygenicphotosynthesiswith media 594d816a).

**Systems-level insight:** The 2024 sulfur-cycle review emphasizes that microbial electron transfer can broaden phototroph metabolic possibilities (e.g., DIET-enabled syntrophic anaerobic photosynthesis) and that centimeter-scale LDET in cable bacteria can separate donor and acceptor zones in sediments (zhuang2024electrontransferin pages 6-8). While cable bacteria are not photolithotrophs, their mechanisms indicate how inorganic electron flow can be spatially organized—useful for curating environmental constraints in photolithotrophic communities.

**Constraint-based view of photoferrotrophy:** The Nature Geoscience 2024 study emphasizes that reactive nitrogen species (NO) can inhibit photoferrotrophy at very low concentrations (12 nM in their modeled parameterization), providing a concrete causal inhibitor edge for ferruginous environments (nikeleit2024inhibitionofphototrophic pages 9-11).

### 8) Warnings / claims that should be curated as uncertain or conditional

1. **Gene markers vs mechanistic necessity.** Reaction-center genes (pshA/pufL/psaB/psbA) are used for *identification* of phototroph types; curation should treat them as evidence for capability, but not as sufficient alone for the full photolithotrophic phenotype without considering donor-oxidation pathways and carbon fixation (nikeleit2024inhibitionofphototrophic pages 11-17).
2. **DIET-enabled phototrophy is consortial and conditional.** The DIET requirement for a porin–cytochrome complex is shown in a specific coculture system; do not generalize to all photolithotrophs (zhuang2024electrontransferin pages 6-8).
3. **Light-intensity performance effects are reactor- and strain-dependent.** The 10 kLx vs 25 kLx relationship should be stored as an experimental observation, not a general rule (kushkevych2024anoxygenicphotosynthesiswith pages 16-17).
4. **Cable bacteria edges are adjacent ecology, not photolithotrophy.** LDET/cable-bacteria mechanisms likely belong in a separate trait graph (electrogenic sulfur oxidation) unless explicitly modeling photolithotroph community electron exchange (zhuang2024electrontransferin pages 6-8).

---

## Key figure evidence (for curator reference)

The 2024 GSB review includes figures contrasting oxygenic vs anoxygenic phototrophy, depicting GSB electron transport and reaction-center complexes, and a schematic of the rTCA cycle (kushkevych2024anoxygenicphotosynthesiswith media 594d816a, kushkevych2024anoxygenicphotosynthesiswith media d9f16891).

---

## DOI-first bibliography (2023–2024 prioritized)

1. **Kushkevych I, Procházka V, Vítězová M, et al.** *Anoxygenic photosynthesis with emphasis on green sulfur bacteria and a perspective for hydrogen sulfide detoxification of anoxic environments.* **Frontiers in Microbiology**. Published **11 Jul 2024**. DOI: **10.3389/fmicb.2024.1417714**. URL: https://doi.org/10.3389/fmicb.2024.1417714 (kushkevych2024anoxygenicphotosynthesiswith pages 1-2, kushkevych2024anoxygenicphotosynthesiswith pages 16-17)
2. **Zhuang X, Wang S, Wu S.** *Electron transfer in the biogeochemical sulfur cycle.* **Life**. Published **May 2024**. DOI: **10.3390/life14050591**. URL: https://doi.org/10.3390/life14050591 (zhuang2024electrontransferin pages 6-8)
3. **Nikeleit V, Mellage A, Bianchini G, et al.** *Inhibition of phototrophic iron oxidation by nitric oxide in ferruginous environments.* **Nature Geoscience**. Published **Oct 2024**. DOI: **10.1038/s41561-024-01560-9**. URL: https://doi.org/10.1038/s41561-024-01560-9 (nikeleit2024inhibitionofphototrophic pages 9-11)
4. **Nishihara A, Tsukatani Y, Azai C, Nobu MK.** *Illuminating the coevolution of photosynthesis and Bacteria.* **PNAS**. Published **Jun 2024**. DOI: **10.1073/pnas.2322120121**. URL: https://doi.org/10.1073/pnas.2322120121 (nishihara2024illuminatingthecoevolution pages 1-2, nishihara2024illuminatingthecoevolution pages 9-9)

(Additional contextual review mentioned in evidence extraction)
5. **Lyons TW, Tino CJ, Fournier GP, et al.** *Co-evolution of early Earth environments and microbial life.* **Nature Reviews Microbiology**. Published **May 2024**. DOI: **10.1038/s41579-024-01044-y**. URL: https://doi.org/10.1038/s41579-024-01044-y (nishihara2024illuminatingthecoevolution pages 1-2)


References

1. (kushkevych2024anoxygenicphotosynthesiswith pages 1-2): Ivan Kushkevych, Vít Procházka, Monika Vítězová, Dani Dordević, Mohamed Abd El-Salam, and Simon K.-M. R. Rittmann. Anoxygenic photosynthesis with emphasis on green sulfur bacteria and a perspective for hydrogen sulfide detoxification of anoxic environments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1417714, doi:10.3389/fmicb.2024.1417714. This article has 24 citations and is from a peer-reviewed journal.

2. (zhuang2024electrontransferin pages 6-8): Xuliang Zhuang, Shijie Wang, and Shanghua Wu. Electron transfer in the biogeochemical sulfur cycle. Life, 14:591, May 2024. URL: https://doi.org/10.3390/life14050591, doi:10.3390/life14050591. This article has 22 citations.

3. (nikeleit2024inhibitionofphototrophic pages 11-17): Verena Nikeleit, Adrian Mellage, Giorgio Bianchini, Lea Sauter, Steffen Buessecker, Stefanie Gotterbarm, Manuel Schad, Kurt Konhauser, Aubrey L. Zerkle, Patricia Sánchez-Baracaldo, Andreas Kappler, and Casey Bryce. Inhibition of phototrophic iron oxidation by nitric oxide in ferruginous environments. Nature Geoscience, 17:1169-1174, Oct 2024. URL: https://doi.org/10.1038/s41561-024-01560-9, doi:10.1038/s41561-024-01560-9. This article has 2 citations and is from a highest quality peer-reviewed journal.

4. (kushkevych2024anoxygenicphotosynthesiswith pages 4-6): Ivan Kushkevych, Vít Procházka, Monika Vítězová, Dani Dordević, Mohamed Abd El-Salam, and Simon K.-M. R. Rittmann. Anoxygenic photosynthesis with emphasis on green sulfur bacteria and a perspective for hydrogen sulfide detoxification of anoxic environments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1417714, doi:10.3389/fmicb.2024.1417714. This article has 24 citations and is from a peer-reviewed journal.

5. (nishihara2024illuminatingthecoevolution pages 1-2): Arisa Nishihara, Yusuke Tsukatani, Chihiro Azai, and Masaru K. Nobu. Illuminating the coevolution of photosynthesis and bacteria. Proceedings of the National Academy of Sciences of the United States of America, Jun 2024. URL: https://doi.org/10.1073/pnas.2322120121, doi:10.1073/pnas.2322120121. This article has 33 citations and is from a highest quality peer-reviewed journal.

6. (nikeleit2024inhibitionofphototrophic pages 9-11): Verena Nikeleit, Adrian Mellage, Giorgio Bianchini, Lea Sauter, Steffen Buessecker, Stefanie Gotterbarm, Manuel Schad, Kurt Konhauser, Aubrey L. Zerkle, Patricia Sánchez-Baracaldo, Andreas Kappler, and Casey Bryce. Inhibition of phototrophic iron oxidation by nitric oxide in ferruginous environments. Nature Geoscience, 17:1169-1174, Oct 2024. URL: https://doi.org/10.1038/s41561-024-01560-9, doi:10.1038/s41561-024-01560-9. This article has 2 citations and is from a highest quality peer-reviewed journal.

7. (nishihara2024illuminatingthecoevolution pages 9-9): Arisa Nishihara, Yusuke Tsukatani, Chihiro Azai, and Masaru K. Nobu. Illuminating the coevolution of photosynthesis and bacteria. Proceedings of the National Academy of Sciences of the United States of America, Jun 2024. URL: https://doi.org/10.1073/pnas.2322120121, doi:10.1073/pnas.2322120121. This article has 33 citations and is from a highest quality peer-reviewed journal.

8. (kushkevych2024anoxygenicphotosynthesiswith media 594d816a): Ivan Kushkevych, Vít Procházka, Monika Vítězová, Dani Dordević, Mohamed Abd El-Salam, and Simon K.-M. R. Rittmann. Anoxygenic photosynthesis with emphasis on green sulfur bacteria and a perspective for hydrogen sulfide detoxification of anoxic environments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1417714, doi:10.3389/fmicb.2024.1417714. This article has 24 citations and is from a peer-reviewed journal.

9. (zhuang2024electrontransferin pages 14-15): Xuliang Zhuang, Shijie Wang, and Shanghua Wu. Electron transfer in the biogeochemical sulfur cycle. Life, 14:591, May 2024. URL: https://doi.org/10.3390/life14050591, doi:10.3390/life14050591. This article has 22 citations.

10. (kushkevych2024anoxygenicphotosynthesiswith media d9f16891): Ivan Kushkevych, Vít Procházka, Monika Vítězová, Dani Dordević, Mohamed Abd El-Salam, and Simon K.-M. R. Rittmann. Anoxygenic photosynthesis with emphasis on green sulfur bacteria and a perspective for hydrogen sulfide detoxification of anoxic environments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1417714, doi:10.3389/fmicb.2024.1417714. This article has 24 citations and is from a peer-reviewed journal.

11. (kushkevych2024anoxygenicphotosynthesiswith pages 16-17): Ivan Kushkevych, Vít Procházka, Monika Vítězová, Dani Dordević, Mohamed Abd El-Salam, and Simon K.-M. R. Rittmann. Anoxygenic photosynthesis with emphasis on green sulfur bacteria and a perspective for hydrogen sulfide detoxification of anoxic environments. Frontiers in Microbiology, Jul 2024. URL: https://doi.org/10.3389/fmicb.2024.1417714, doi:10.3389/fmicb.2024.1417714. This article has 24 citations and is from a peer-reviewed journal.

12. (nikeleit2024inhibitionofphototrophic pages 17-17): Verena Nikeleit, Adrian Mellage, Giorgio Bianchini, Lea Sauter, Steffen Buessecker, Stefanie Gotterbarm, Manuel Schad, Kurt Konhauser, Aubrey L. Zerkle, Patricia Sánchez-Baracaldo, Andreas Kappler, and Casey Bryce. Inhibition of phototrophic iron oxidation by nitric oxide in ferruginous environments. Nature Geoscience, 17:1169-1174, Oct 2024. URL: https://doi.org/10.1038/s41561-024-01560-9, doi:10.1038/s41561-024-01560-9. This article has 2 citations and is from a highest quality peer-reviewed journal.