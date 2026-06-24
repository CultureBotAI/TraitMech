---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T12:00:10.901731'
end_time: '2026-06-18T12:12:27.772206'
duration_seconds: 736.87
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: organoheterotrophic
  trait_identifier: METPO:1000664
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: organoheterotrophic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic type characterized by the use of organic compounds as both
    electron donors and primary carbon sources for energy generation and biosynthesis.
  parent_traits: METPO:1000631
  synonyms: organoheterotroph
  evidence_summary: 'DOI:10.1016/B978-012373944-5.00083-3: organic compounds as the
    primary sources of carbon and energy (Encyclopedia chapter supports organic compounds
    as carbon and energy sources in heterotrophy.) | DOI:10.1016/j.bbabio.2008.09.008:
    free energy of a redox reaction (Review supports energy conservation from electron
    donor oxidation through respiratory chains.)'
  causal_graph_summary: 'organoheterotrophic_organic_donor_carbon: 7 nodes, 7 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 27
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** organoheterotrophic
- **METPO identifier:** METPO:1000664
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type characterized by the use of organic compounds as both electron donors and primary carbon sources for energy generation and biosynthesis.
- **Parent traits:** METPO:1000631
- **Synonyms:** organoheterotroph
- **Existing evidence:** DOI:10.1016/B978-012373944-5.00083-3: organic compounds as the primary sources of carbon and energy (Encyclopedia chapter supports organic compounds as carbon and energy sources in heterotrophy.) | DOI:10.1016/j.bbabio.2008.09.008: free energy of a redox reaction (Review supports energy conservation from electron donor oxidation through respiratory chains.)
- **Existing causal graph summary:** organoheterotrophic_organic_donor_carbon: 7 nodes, 7 edges

## Research Objective

Research the microbial trait **organoheterotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/organoheterotrophic.yaml`.

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
- **Trait label:** organoheterotrophic
- **METPO identifier:** METPO:1000664
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type characterized by the use of organic compounds as both electron donors and primary carbon sources for energy generation and biosynthesis.
- **Parent traits:** METPO:1000631
- **Synonyms:** organoheterotroph
- **Existing evidence:** DOI:10.1016/B978-012373944-5.00083-3: organic compounds as the primary sources of carbon and energy (Encyclopedia chapter supports organic compounds as carbon and energy sources in heterotrophy.) | DOI:10.1016/j.bbabio.2008.09.008: free energy of a redox reaction (Review supports energy conservation from electron donor oxidation through respiratory chains.)
- **Existing causal graph summary:** organoheterotrophic_organic_donor_carbon: 7 nodes, 7 edges

## Research Objective

Research the microbial trait **organoheterotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/organoheterotrophic.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **organoheterotrophic** (METPO:1000664)

### Scope summary (TraitMech-ready)
**Organoheterotrophic** denotes a trophic type in which **organic compounds serve both as (i) the electron donor for energy generation and (ii) the primary carbon source for biosynthesis** (slowinski2019bioenergeticsofmixotrophic pages 11-15). In this framing, organoheterotrophy is an “end-member” metabolic mode contrasted with lithoautotrophy (inorganic electron donor + inorganic carbon) and lithoheterotrophy (inorganic electron donor + organic carbon), and can participate in **mixotrophy** when organisms simultaneously draw on inorganic and organic electron donors and/or carbon sources (slowinski2019bioenergeticsofmixotrophic pages 32-37, slowinski2019bioenergeticsofmixotrophic pages 15-21, slowinski2019bioenergeticsofmixotrophic pages 27-32).

**Boundary cases / distinctions relevant for curation**
- **Organoheterotrophy vs lithoheterotrophy:** both use organic carbon for biomass, but differ in electron donor (organic vs inorganic) (slowinski2019bioenergeticsofmixotrophic pages 15-21, slowinski2019bioenergeticsofmixotrophic pages 32-37).
- **Organoheterotrophy vs organotrophy (term usage):** organotrophy emphasizes the **electron donor** being organic, whereas heterotrophy emphasizes the **carbon source** being organic; organoheterotrophy combines both (slowinski2019bioenergeticsofmixotrophic pages 32-37).
- **Organoheterotrophy vs photoheterotrophy:** photoheterotrophs can supplement energy with light but still **require organic substrates for growth** (mujakic2023multienvironmentecogenomicsanalysis pages 1-2).
- **Organoheterotrophy vs mixotrophy:** mixotrophs can couple organoheterotrophy with lithotrophy and/or carbon fixation depending on substrates and energetics; e.g., environmental iron-oxidizing mats show combined organic-carbon use with iron oxidation and occasional carbon fixation (tothero2024leptothrixochraceagenomes pages 1-2, tothero2024leptothrixochraceagenomes pages 9-13).

### Key concepts and mechanistic definition (current understanding)
Microbial growth couples **catabolism** (energy-yielding redox reactions) to **anabolism** (biomass synthesis): microbes “couple a reaction for the creation of biomass (the anabolic reaction) to the reaction from which they derive energy (the catabolic reaction)” (slowinski2019bioenergeticsofmixotrophic pages 11-15). In respiratory organoheterotrophy, chemical energy from oxidation–reduction reactions is conserved via an **electron transport chain** and ultimately “stored intracellularly as ATP” (slowinski2019bioenergeticsofmixotrophic pages 15-21). Electron acceptors supporting organotrophic respiration in anoxic contexts include **nitrate, sulfate, iron(III), manganese(IV), and CO2**, indicating that organoheterotrophy frequently connects to broader biogeochemical cycling beyond oxygen respiration (slowinski2019bioenergeticsofmixotrophic pages 15-21).

### Candidate mechanistic entities (nodes), grouped by type
Below is a curation-oriented list of candidate nodes for `data/traits/physiology/organoheterotrophic.yaml`, emphasizing nodes evidenced in 2023–2024 studies.

#### A) Pathways / metabolic modules
- **Central carbon catabolism**: glycolysis (Embden–Meyerhof), pentose phosphate pathway (PPP), tricarboxylic acid cycle (TCA) (liu2023isolationandgenomics pages 7-8, liu2023isolationandgenomics pages 10-13)
- **Oxidative phosphorylation / aerobic respiration module**: NADH dehydrogenase (Complex I), succinate dehydrogenase (Complex II), cytochrome bc1 (Complex III), alternative complex III (ACIII; in some taxa), terminal oxidases (aa3-type and/or cbb3-type; cytochrome bd), ATP synthase (F-type; N-type in some taxa) (liu2023isolationandgenomics pages 8-10, tothero2024leptothrixochraceagenomes pages 9-13)
- **Anaerobic respiratory branches**: nitrate reduction to nitrite (narGHI); broader nitrate/nitrite/denitrification gene sets in some environments (liu2023isolationandgenomics pages 8-10, gutierrezpreciado2024extremelyacidicproteomes pages 7-9)
- **Carbon storage and mobilization**: poly(3-hydroxybutyrate) (PHB) synthesis (phbABC) and depolymerization (phaZ) (liu2023isolationandgenomics pages 8-10, liu2023isolationandgenomics pages 13-15)

#### B) Genes / proteins / complexes (examples with evidence)
- **Respiratory chain**: nuoABCDEFGHIJKLMN; sdhABCD; petABC; terminal oxidases coxABC (aa3) and ccoNOQP (cbb3); cydABX (cytochrome bd); F-type ATPase; N-type ATPase (strain-specific) (liu2023isolationandgenomics pages 8-10, tothero2024leptothrixochraceagenomes pages 9-13)
- **Organic substrate uptake and oxidation** (example: iron-mat bacterium *Leptothrix ochracea*): lactate permease **lctP**; lactate dehydrogenase **ykgEFG**; acetate transporter **actP**; acetate kinase **ackA**; sugar transport **gtsABC**; formate dehydrogenase (NAD-dependent) (tothero2024leptothrixochraceagenomes pages 15-16, tothero2024leptothrixochraceagenomes pages 13-15)
- **Organic nutrient transporters (amino acids/osmolytes)**: multiple ABC transporters for amino acids/betaine-family solutes in organoheterotrophic isolate *Futiania mangrovii* (liu2023isolationandgenomics pages 13-15, liu2023isolationandgenomics pages 8-10)

#### C) Chemicals / substrates / electron acceptors
- **Organic electron donors / carbon sources**: sugars; organic acids (acetate, lactate, formate); amino acids; polysaccharides (tothero2024leptothrixochraceagenomes pages 13-15, tothero2024leptothrixochraceagenomes pages 15-16, gutierrezpreciado2024extremelyacidicproteomes pages 7-9)
- **Electron acceptors**: O2; nitrate (NO3−); fumarate; sulfur species (and others environment-dependent) (slowinski2019bioenergeticsofmixotrophic pages 15-21, gutierrezpreciado2024extremelyacidicproteomes pages 7-9)
- **Energy currency**: ATP (slowinski2019bioenergeticsofmixotrophic pages 15-21)
- **Storage polymer**: PHB (liu2023isolationandgenomics pages 13-15)

#### D) Environmental / experimental factors
- **Oxygen gradients / microaerobic conditions** selecting for high-affinity terminal oxidases (cbb3-type, cytochrome bd) (tothero2024leptothrixochraceagenomes pages 9-13)
- **Extreme polyextreme brine conditions** (relevant for organoheterotrophic dominance at life limits): pH from −1.5 to 6; salinity ~30 to >70% w/v; temperature ~30°C to 110°C (gutierrezpreciado2024extremelyacidicproteomes pages 1-4)

### Recent developments and latest research (prioritizing 2023–2024)
1. **Organoheterotrophic respiration with multiple terminal oxidases (cultured isolate)**: *Futiania mangrovii* (Microbiology Spectrum, Feb 2023) encodes a full oxidative phosphorylation system including NADH dehydrogenase, succinate dehydrogenase, cytochrome bc1, and both **aa3-type (coxABC) and cbb3-type (ccoNOQP) terminal oxidases**, supporting aerobic respiration across variable oxygen regimes (liu2023isolationandgenomics pages 8-10). It also shows nitrate reduction to nitrite (narGHI) (liu2023isolationandgenomics pages 8-10).
2. **Organoheterotrophy integrated into iron-oxidizing mat ecology (genomes + in situ expression)**: *Leptothrix ochracea* (Applied and Environmental Microbiology, Sep 2024) shows high expression of organic-acid and sugar utilization genes (e.g., **lctP**, **actP**, **gtsA**) and high expression of cbb3-type cytochrome c oxidase genes, consistent with aerobic/microaerobic respiration while occupying iron-rich, organic-carbon–available niches (tothero2024leptothrixochraceagenomes pages 15-16, tothero2024leptothrixochraceagenomes pages 9-13).
3. **Community-level heterotrophy with broad electron-acceptor flexibility in near life-limiting brines**: In Danakil hypersaline geothermal lakes (Nature Ecology & Evolution, Aug 2024), organisms are described as relying “exclusively on heterotrophic processes,” with genomic prevalence of nitrate respiration genes exceeding oxygen-respiration genes in some settings and fumarate reductase being near-universal across MAGs—illustrating how organoheterotrophic systems can be organized around diverse terminal electron acceptors beyond oxygen (gutierrezpreciado2024extremelyacidicproteomes pages 1-4, gutierrezpreciado2024extremelyacidicproteomes pages 7-9).

### Current applications and real-world implementations (trait relevance)
- **Environmental metagenomics / trait inference**: 2023–2024 studies demonstrate practical pipelines where organoheterotrophy is inferred from the co-occurrence of central carbon catabolic modules (glycolysis/PPP/TCA), respiratory chain components, and organic-substrate transport/oxidation genes (liu2023isolationandgenomics pages 8-10, tothero2024leptothrixochraceagenomes pages 9-13).
- **Biogeochemical modeling and energy accounting**: Frameworks that partition organic substrate use between assimilation and dissimilation (growth yield) support quantitative modeling of organoheterotrophy and mixotrophy in environmental systems (slowinski2019bioenergeticsofmixotrophic pages 21-27, slowinski2019bioenergeticsofmixotrophic pages 1-7).
- **Ecological niche diagnostics**: In iron mats, relative dissolved organic carbon availability can shift dominance between taxa; *L. ochracea* is associated with higher DOC than some canonical FeOB (Gallionellaceae) and overtakes Gallionella when DOC increases, supporting the use of organoheterotrophic capacities as ecological discriminators (tothero2024leptothrixochraceagenomes pages 1-2).

### Relevant statistics and data points from recent studies
- **Danakil brines (2024, community composition)**: “haloarchaea and Nanohaloarchaeota encompass **99%** of microbial communities” in near life-limiting Western-Canyon Lakes (gutierrezpreciado2024extremelyacidicproteomes pages 1-4).
- **Danakil brines (2024, respiratory gene prevalence)**: nitrate reductase genes were “encoded in up to **20%** of genomes in Lake Assale,” and CO-dehydrogenase genes were present in “**3–7%** of genomes” (gutierrezpreciado2024extremelyacidicproteomes pages 7-9).
- **Iron mat geochemistry context (2024)**: reported Fe concentrations included **4–11 µM** (surface water) and **13–27 mM** (sediment), with Mn **0.7–1.2 µM** (surface) and **1.4–2.0 µM** (porewater), relevant to interpreting mixotrophic Fe-oxidizer niches that include organoheterotrophic growth (tothero2024leptothrixochraceagenomes pages 15-16).

### Evidence-backed candidate causal edges (triples)
The following table is designed for direct curation as candidate edges (with grounding suggestions and uncertainty flags).

| Edge (subject–predicate–object) | Evidence snippet (verbatim or near-verbatim) | Source (authors year, journal) | DOI/URL | Ontology grounding suggestions (CURIEs for subject/object when possible) | Notes/uncertainty |
|---|---|---|---|---|---|
| organic compounds — serve as electron donor for — organoheterotrophic metabolism | “Organoheterotrophic metabolisms use organic compounds for both energy generation (i.e., as an electron donor) and as a carbon source.” (slowinski2019bioenergeticsofmixotrophic pages 11-15) | Slowinski 2019, thesis/review-style analysis | n/a | subject: CHEBI:59999 organic molecular entity; object: METPO:1000664 organoheterotrophic | Definition-level edge; broad trait statement rather than a specific mechanism. |
| organic compounds — serve as carbon source for — organoheterotrophic metabolism | “Organoheterotrophic metabolisms use organic compounds for both energy generation (i.e., as an electron donor) and as a carbon source.” (slowinski2019bioenergeticsofmixotrophic pages 11-15) | Slowinski 2019, thesis/review-style analysis | n/a | subject: CHEBI:59999; object: METPO:1000664 | Core defining edge for the trait. |
| catabolic redox reaction — is coupled to — anabolic reaction/biomass formation | “they couple a reaction for the creation of biomass (the anabolic reaction) to the reaction from which they derive energy (the catabolic reaction).” (slowinski2019bioenergeticsofmixotrophic pages 11-15) | Slowinski 2019, thesis/review-style analysis | n/a | subject: GO:0045333 cellular respiration or label-only “catabolic redox reaction”; object: GO:0009058 biosynthetic process | Conceptual systems-biology edge; not tied to one gene. |
| electron transport chain — stores conserved energy as — ATP | “the energy lost by the chemicals in the system due to the reaction is then gained by the organism catalyzing the reaction using an electron transport chain, and stored intracellularly as ATP” (slowinski2019bioenergeticsofmixotrophic pages 15-21) | Slowinski 2019, thesis/review-style analysis | n/a | subject: GO:0022900 electron transport chain; object: CHEBI:15422 ATP | Broad mechanistic edge applicable to respiratory organoheterotrophy. |
| NADH dehydrogenase complex I (nuoABCDEFGHIJKLMN) — contributes to — oxidative phosphorylation | “a complete oxidative phosphorylation pathway is encoded, including NADH dehydrogenase (nuoABCDEFGHIJKLMN)” (liu2023isolationandgenomics pages 8-10) | Liu et al. 2023, Microbiology Spectrum | https://doi.org/10.1128/spectrum.04110-22 | subject: GO:0008137 NADH dehydrogenase activity / KEGG:K00330-K00346 complex I genes; object: GO:0006119 oxidative phosphorylation | Evidence from *Futiania mangrovii* FT118T; taxon-specific but mechanistically standard. |
| succinate dehydrogenase (sdhABCD) — contributes to — oxidative phosphorylation | “a complete oxidative phosphorylation pathway is encoded, including… succinate dehydrogenase (sdhABCD)” (liu2023isolationandgenomics pages 8-10) | Liu et al. 2023, Microbiology Spectrum | https://doi.org/10.1128/spectrum.04110-22 | subject: EC:1.3.5.1 / GO:0000104 succinate dehydrogenase activity; object: GO:0006119 | Supports respiratory coupling of TCA-derived electrons; taxon-specific genomic evidence. |
| cytochrome bc1 complex (petABC) — contributes to — oxidative phosphorylation | “a complete oxidative phosphorylation pathway is encoded, including… cytochrome bc1 (petABC)” (liu2023isolationandgenomics pages 8-10) | Liu et al. 2023, Microbiology Spectrum | https://doi.org/10.1128/spectrum.04110-22 | subject: GO:0008121 ubiquinol-cytochrome-c reductase activity / KEGG:petA petB petC; object: GO:0006119 | Strong genomic support in FT118T. |
| aa3-type cytochrome c oxidase (coxABC) — enables — aerobic respiration | “terminal oxidases heme aa3-type (coxABC) and cbb3-type (ccoNOQP)… [are] consistent with aerobic respiration” (liu2023isolationandgenomics pages 8-10) | Liu et al. 2023, Microbiology Spectrum | https://doi.org/10.1128/spectrum.04110-22 | subject: GO:0004129 cytochrome-c oxidase activity / KEGG:coxA coxB coxC; object: GO:0009060 aerobic respiration | Good evidence for one organism; terminal oxidase identity may vary across taxa. |
| cbb3-type cytochrome c oxidase (ccoNOQP) — enables — aerobic respiration under low O2 | “cbb3-type cytochrome c oxidase genes (ccoN/ccoO; ccoN ~96–99th percentile)” and genomes “encode high-affinity terminal oxidases: cbb3-type cytochrome c oxidase (ccoNOPQ)” (tothero2024leptothrixochraceagenomes pages 15-16, tothero2024leptothrixochraceagenomes pages 9-13) | Tothero et al. 2024, Applied and Environmental Microbiology | https://doi.org/10.1128/aem.00599-24 | subject: KEGG:ccoN ccoO ccoP ccoQ / GO:0004129; object: GO:0009060 | Strong for microaerobic organoheterotroph/mixotroph contexts. |
| cytochrome bd ubiquinol oxidase (cydABX) — enables — high-affinity aerobic respiration | “The genomes also contain… cytochrome bd ubiquinol oxidase (cydABX)” and are “adaptation to microaerobic niches.” (tothero2024leptothrixochraceagenomes pages 9-13) | Tothero et al. 2024, Applied and Environmental Microbiology | https://doi.org/10.1128/aem.00599-24 | subject: KEGG:cydA cydB cydX / GO:0015002 cytochrome-bd ubiquinol oxidase activity; object: GO:0009060 | More specifically supports low-O2 respiration than generic organoheterotrophy. |
| glycolysis pathway — enables — organic carbon catabolism | “Genome annotation identifies a complete glycolysis (Embden-Meyerhof) pathway” (liu2023isolationandgenomics pages 7-8) | Liu et al. 2023, Microbiology Spectrum | https://doi.org/10.1128/spectrum.04110-22 | subject: GO:0006096 glycolytic process; object: label-only “organic carbon catabolism” or GO:0016052 carbohydrate catabolic process | Generalizable but based on one taxon’s genome. |
| pentose phosphate pathway — enables — catabolism/processing of organic carbon substrates | “the genome supports… the pentose phosphate pathway” (liu2023isolationandgenomics pages 10-13, liu2023isolationandgenomics pages 7-8) | Liu et al. 2023, Microbiology Spectrum | https://doi.org/10.1128/spectrum.04110-22 | subject: GO:0006098 pentose-phosphate shunt; object: GO:0016052 carbohydrate catabolic process | PPP also serves anabolic redox/precursor roles; not exclusively catabolic. |
| tricarboxylic acid cycle — enables — oxidative catabolism of organic substrates | “A complete tricarboxylic acid (TCA) cycle is present, indicating capacity for oxidative catabolism of organic substrates.” (liu2023isolationandgenomics pages 7-8) | Liu et al. 2023, Microbiology Spectrum | https://doi.org/10.1128/spectrum.04110-22 | subject: GO:0006099 tricarboxylic acid cycle; object: label-only “organic substrate oxidation” | Strong central-metabolism edge; standard for respiratory heterotrophs. |
| lactate permease (lctP) and lactate dehydrogenase (ykgEFG) — enable — lactate utilization | “all MAGs contain lctP and L-lactate dehydrogenase (ykgEFG)… indicating lactate uptake and conversion to pyruvate” (tothero2024leptothrixochraceagenomes pages 13-15) | Tothero et al. 2024, Applied and Environmental Microbiology | https://doi.org/10.1128/aem.00599-24 | subject: KEGG:lctP; KEGG:ykgE/ykgF/ykgG or label-only LDH complex; object: CHEBI:24996 lactate | Strong mechanistic edge; derived from *Leptothrix ochracea* MAGs. |
| acetate symporter ActP and acetate kinase AckA — enable — acetate utilization | “Acetate uptake and metabolism are supported by actP and ackA… enabling acetate entry into pyruvate metabolism.” (tothero2024leptothrixochraceagenomes pages 13-15) | Tothero et al. 2024, Applied and Environmental Microbiology | https://doi.org/10.1128/aem.00599-24 | subject: KEGG:actP; EC:2.7.2.1 ackA; object: CHEBI:30089 acetate | Strong for acetate use; exact downstream route may vary among taxa. |
| NAD-dependent formate dehydrogenase — enables — formate oxidation | “NAD-dependent formate dehydrogenase is present across the group, suggesting formate oxidation to regenerate NADH.” (tothero2024leptothrixochraceagenomes pages 13-15) | Tothero et al. 2024, Applied and Environmental Microbiology | https://doi.org/10.1128/aem.00599-24 | subject: EC:1.17.1.9 formate dehydrogenase; object: CHEBI:15740 formate | Useful edge for organic C1 oxidation; taxon-specific genomic inference. |
| nitrate reductase (narGHI) — enables — anaerobic respiration / nitrate reduction to nitrite | “Nitrate is reduced to nitrite but not to nitrogen” and “nitrate reduction to nitrite (narGHI) was observed” (liu2023isolationandgenomics pages 8-10) | Liu et al. 2023, Microbiology Spectrum | https://doi.org/10.1128/spectrum.04110-22 | subject: KEGG:narG narH narI / EC:1.7.5.1; object: GO:0009061 anaerobic respiration or GO:0019250 anaerobic electron transport chain | Supports facultative anaerobic respiratory branch, not universal to all organoheterotrophs. |
| PHB synthesis genes (phbA/phbB/phbC) — enable — carbon and energy storage | “the genome encodes PHB synthesis” (liu2023isolationandgenomics pages 10-13) and “PHB synthesis/degradation genes were detected and transcribed” (liu2023isolationandgenomics pages 15-17) | Liu et al. 2023, Microbiology Spectrum | https://doi.org/10.1128/spectrum.04110-22 | subject: KEGG:phbA phbB phbC; object: CHEBI:60027 poly(3-hydroxybutyrate) / label-only “carbon-energy storage” | Storage trait is common but not defining for organoheterotrophy; curate as accessory edge. |
| PHB depolymerase (phaZ) — enables — utilization of stored PHB | “PHB could be a nutrient source for strain FT118T when necessary” and PHB depolymerase “phaZ” is present/transcribed (liu2023isolationandgenomics pages 13-15, liu2023isolationandgenomics pages 8-10) | Liu et al. 2023, Microbiology Spectrum | https://doi.org/10.1128/spectrum.04110-22 | subject: KEGG:phaZ; object: CHEBI:60027 poly(3-hydroxybutyrate) | Accessory storage-mobilization edge; strong within FT118T. |
| oxygen limitation / microaerobic niche — selects for — high-affinity terminal oxidases (ccoNOPQ, cydABX) | genomes “encode high-affinity terminal oxidases: cbb3-type cytochrome c oxidase (ccoNOPQ) and cytochrome bd ubiquinol oxidase (cydABX), but lack the low-affinity aa3-type (coxABCD), indicating adaptation to microaerobic niches.” (tothero2024leptothrixochraceagenomes pages 9-13) | Tothero et al. 2024, Applied and Environmental Microbiology | https://doi.org/10.1128/aem.00599-24 | subject: ENVO:01001043 microaerobic habitat or label-only “oxygen limitation”; object: KEGG:ccoNOPQ, KEGG:cydABX | Environmental-selection edge; valuable but more niche-specific than trait-defining. |
| organoheterotrophic communities — use alternative electron acceptors including — nitrate/fumarate/sulfur when O2 is limited | “nitrate respiration genes… were more prevalent than oxygen-respiration genes… fumarate reductase occurred in almost all MAGs” in communities that “rely exclusively on heterotrophic processes” (gutierrezpreciado2024extremelyacidicproteomes pages 7-9, gutierrezpreciado2024extremelyacidicproteomes pages 1-4) | Gutiérrez-Preciado et al. 2024, Nature Ecology & Evolution | https://doi.org/10.1038/s41559-024-02505-6 | subject: METPO:1000664 organoheterotrophic; object: CHEBI:17632 nitrate / CHEBI:18012 fumarate / CHEBI:26845 sulfur | Community-level, environment-specific evidence from hypersaline brines; curate cautiously as non-universal respiratory flexibility. |


*Table: This table lists candidate subject–predicate–object edges for curating the organoheterotrophic trait, with source-backed snippets, DOI/URL links, grounding suggestions, and uncertainty notes. It covers trait-defining edges, respiratory-chain modules, central carbon metabolism, substrate transport, storage metabolism, and environmental selection under low oxygen.*

### Visual evidence (useful for curator review)
Liu et al. (2023) provide a pathway schematic (“metabolic reconstruction”) highlighting carbon sources utilized in Biolog GENIII and connecting them to central metabolism and oxidative phosphorylation; this figure is useful for curators validating node inclusion and substrate evidence (liu2023isolationandgenomics media b4a990ce).

### Warnings / curation caveats (do not over-generalize)
- **Not all organoheterotrophs are strictly respiratory**: fermentative organoheterotrophy is common in microbiology, but the retrieved 2023–2024 mechanistic evidence here is dominated by **respiration-linked** energy conservation (ETC/oxidative phosphorylation). Fermentation-specific edges should be curated only with direct sources.
- **Terminal oxidase composition is taxon- and niche-specific**: e.g., *L. ochracea* MAGs lack low-affinity aa3-type oxidases (coxABCD) and instead encode high-affinity oxidases (cbb3, bd) associated with microaerobic niches (tothero2024leptothrixochraceagenomes pages 9-13). Do not treat any single terminal oxidase as defining of organoheterotrophy.
- **Community-level electron-acceptor prevalence is environment-specific**: the Danakil brine statistics (e.g., nitrate genes in up to 20% of genomes) should be curated as **environment-scoped** evidence (ENVO-context) rather than universal organoheterotrophic properties (gutierrezpreciado2024extremelyacidicproteomes pages 7-9).

---

## DOI-first bibliography (with dates and URLs where available)

1. **Tothero GK, Hoover RL, Farag IF, Kaplan DI, Weisenhorn P, Emerson D, Chan CS.** (2024-09) *Leptothrix ochracea genomes reveal potential for mixotrophic growth on Fe(II) and organic carbon.* **Applied and Environmental Microbiology** 90(9). DOI: **10.1128/aem.00599-24**. URL: https://doi.org/10.1128/aem.00599-24 (tothero2024leptothrixochraceagenomes pages 1-2, tothero2024leptothrixochraceagenomes pages 15-16, tothero2024leptothrixochraceagenomes pages 9-13)
2. **Gutiérrez-Preciado A, Dede B, Baker BA, Eme L, Moreira D, López-García P.** (2024-08) *Extremely acidic proteomes and metabolic flexibility in bacteria and highly diversified archaea thriving in geothermal chaotropic brines.* **Nature Ecology & Evolution** 8:1856–1869. DOI: **10.1038/s41559-024-02505-6**. URL: https://doi.org/10.1038/s41559-024-02505-6 (gutierrezpreciado2024extremelyacidicproteomes pages 1-4, gutierrezpreciado2024extremelyacidicproteomes pages 7-9)
3. **Mujakić I, Cabello-Yeves PJ, Villena-Alemany C, Piwosz K, Rodriguez-Valera F, Picazo A, Camacho A, Koblížek M.** (2023-10) *Multi-environment ecogenomics analysis of the cosmopolitan phylum Gemmatimonadota.* **Microbiology Spectrum** 11(5). DOI: **10.1128/spectrum.01112-23**. URL: https://doi.org/10.1128/spectrum.01112-23 (mujakic2023multienvironmentecogenomicsanalysis pages 1-2)
4. **Liu L, Huang W-C, Pan J, Li J, Huang Y, Zou D, Du H, Liu Y, Li M.** (2023-02) *Isolation and Genomics of Futiania mangrovii gen. nov., sp. nov., a Rare and Metabolically Versatile Member in the Class Alphaproteobacteria.* **Microbiology Spectrum** 11(1). DOI: **10.1128/spectrum.04110-22**. URL: https://doi.org/10.1128/spectrum.04110-22 (liu2023isolationandgenomics pages 8-10, liu2023isolationandgenomics pages 7-8, liu2023isolationandgenomics media b4a990ce)

Additional conceptual source used for trait framing (not 2023–2024):
- **Slowinski S.** (2019) *Bioenergetics of mixotrophic metabolisms: A theoretical analysis.* (Definition and conceptual distinctions; no DOI in retrieved text) (slowinski2019bioenergeticsofmixotrophic pages 11-15, slowinski2019bioenergeticsofmixotrophic pages 15-21, slowinski2019bioenergeticsofmixotrophic pages 32-37)


References

1. (slowinski2019bioenergeticsofmixotrophic pages 11-15): S Slowinski. Bioenergetics of mixotrophic metabolisms: a theoretical analysis. Unknown journal, 2019.

2. (slowinski2019bioenergeticsofmixotrophic pages 32-37): S Slowinski. Bioenergetics of mixotrophic metabolisms: a theoretical analysis. Unknown journal, 2019.

3. (slowinski2019bioenergeticsofmixotrophic pages 15-21): S Slowinski. Bioenergetics of mixotrophic metabolisms: a theoretical analysis. Unknown journal, 2019.

4. (slowinski2019bioenergeticsofmixotrophic pages 27-32): S Slowinski. Bioenergetics of mixotrophic metabolisms: a theoretical analysis. Unknown journal, 2019.

5. (mujakic2023multienvironmentecogenomicsanalysis pages 1-2): Izabela Mujakić, Pedro J. Cabello-Yeves, Cristian Villena-Alemany, Kasia Piwosz, Francisco Rodriguez-Valera, Antonio Picazo, Antonio Camacho, and Michal Koblížek. Multi-environment ecogenomics analysis of the cosmopolitan phylum gemmatimonadota. Oct 2023. URL: https://doi.org/10.1128/spectrum.01112-23, doi:10.1128/spectrum.01112-23. This article has 73 citations and is from a domain leading peer-reviewed journal.

6. (tothero2024leptothrixochraceagenomes pages 1-2): Gracee K. Tothero, Rene L. Hoover, Ibrahim F. Farag, Daniel I. Kaplan, Pamela Weisenhorn, David Emerson, and Clara S. Chan. <i>leptothrix ochracea</i> genomes reveal potential for mixotrophic growth on fe(ii) and organic carbon. Sep 2024. URL: https://doi.org/10.1128/aem.00599-24, doi:10.1128/aem.00599-24. This article has 21 citations and is from a peer-reviewed journal.

7. (tothero2024leptothrixochraceagenomes pages 9-13): Gracee K. Tothero, Rene L. Hoover, Ibrahim F. Farag, Daniel I. Kaplan, Pamela Weisenhorn, David Emerson, and Clara S. Chan. <i>leptothrix ochracea</i> genomes reveal potential for mixotrophic growth on fe(ii) and organic carbon. Sep 2024. URL: https://doi.org/10.1128/aem.00599-24, doi:10.1128/aem.00599-24. This article has 21 citations and is from a peer-reviewed journal.

8. (liu2023isolationandgenomics pages 7-8): Lirui Liu, Wen-Cong Huang, Jie Pan, Jiayi Li, Yuhan Huang, Dayu Zou, Huan Du, Yang Liu, and Meng Li. Isolation and genomics of <i>futiania mangrovii</i> gen. nov., sp. nov., a rare and metabolically versatile member in the class <i>alphaproteobacteria</i>. Feb 2023. URL: https://doi.org/10.1128/spectrum.04110-22, doi:10.1128/spectrum.04110-22. This article has 10 citations and is from a domain leading peer-reviewed journal.

9. (liu2023isolationandgenomics pages 10-13): Lirui Liu, Wen-Cong Huang, Jie Pan, Jiayi Li, Yuhan Huang, Dayu Zou, Huan Du, Yang Liu, and Meng Li. Isolation and genomics of <i>futiania mangrovii</i> gen. nov., sp. nov., a rare and metabolically versatile member in the class <i>alphaproteobacteria</i>. Feb 2023. URL: https://doi.org/10.1128/spectrum.04110-22, doi:10.1128/spectrum.04110-22. This article has 10 citations and is from a domain leading peer-reviewed journal.

10. (liu2023isolationandgenomics pages 8-10): Lirui Liu, Wen-Cong Huang, Jie Pan, Jiayi Li, Yuhan Huang, Dayu Zou, Huan Du, Yang Liu, and Meng Li. Isolation and genomics of <i>futiania mangrovii</i> gen. nov., sp. nov., a rare and metabolically versatile member in the class <i>alphaproteobacteria</i>. Feb 2023. URL: https://doi.org/10.1128/spectrum.04110-22, doi:10.1128/spectrum.04110-22. This article has 10 citations and is from a domain leading peer-reviewed journal.

11. (gutierrezpreciado2024extremelyacidicproteomes pages 7-9): Ana Gutiérrez-Preciado, Bledina Dede, Brittany A. Baker, Laura Eme, David Moreira, and Purificación López-García. Extremely acidic proteomes and metabolic flexibility in bacteria and highly diversified archaea thriving in geothermal chaotropic brines. Aug 2024. URL: https://doi.org/10.1038/s41559-024-02505-6, doi:10.1038/s41559-024-02505-6. This article has 23 citations and is from a highest quality peer-reviewed journal.

12. (liu2023isolationandgenomics pages 13-15): Lirui Liu, Wen-Cong Huang, Jie Pan, Jiayi Li, Yuhan Huang, Dayu Zou, Huan Du, Yang Liu, and Meng Li. Isolation and genomics of <i>futiania mangrovii</i> gen. nov., sp. nov., a rare and metabolically versatile member in the class <i>alphaproteobacteria</i>. Feb 2023. URL: https://doi.org/10.1128/spectrum.04110-22, doi:10.1128/spectrum.04110-22. This article has 10 citations and is from a domain leading peer-reviewed journal.

13. (tothero2024leptothrixochraceagenomes pages 15-16): Gracee K. Tothero, Rene L. Hoover, Ibrahim F. Farag, Daniel I. Kaplan, Pamela Weisenhorn, David Emerson, and Clara S. Chan. <i>leptothrix ochracea</i> genomes reveal potential for mixotrophic growth on fe(ii) and organic carbon. Sep 2024. URL: https://doi.org/10.1128/aem.00599-24, doi:10.1128/aem.00599-24. This article has 21 citations and is from a peer-reviewed journal.

14. (tothero2024leptothrixochraceagenomes pages 13-15): Gracee K. Tothero, Rene L. Hoover, Ibrahim F. Farag, Daniel I. Kaplan, Pamela Weisenhorn, David Emerson, and Clara S. Chan. <i>leptothrix ochracea</i> genomes reveal potential for mixotrophic growth on fe(ii) and organic carbon. Sep 2024. URL: https://doi.org/10.1128/aem.00599-24, doi:10.1128/aem.00599-24. This article has 21 citations and is from a peer-reviewed journal.

15. (gutierrezpreciado2024extremelyacidicproteomes pages 1-4): Ana Gutiérrez-Preciado, Bledina Dede, Brittany A. Baker, Laura Eme, David Moreira, and Purificación López-García. Extremely acidic proteomes and metabolic flexibility in bacteria and highly diversified archaea thriving in geothermal chaotropic brines. Aug 2024. URL: https://doi.org/10.1038/s41559-024-02505-6, doi:10.1038/s41559-024-02505-6. This article has 23 citations and is from a highest quality peer-reviewed journal.

16. (slowinski2019bioenergeticsofmixotrophic pages 21-27): S Slowinski. Bioenergetics of mixotrophic metabolisms: a theoretical analysis. Unknown journal, 2019.

17. (slowinski2019bioenergeticsofmixotrophic pages 1-7): S Slowinski. Bioenergetics of mixotrophic metabolisms: a theoretical analysis. Unknown journal, 2019.

18. (liu2023isolationandgenomics pages 15-17): Lirui Liu, Wen-Cong Huang, Jie Pan, Jiayi Li, Yuhan Huang, Dayu Zou, Huan Du, Yang Liu, and Meng Li. Isolation and genomics of <i>futiania mangrovii</i> gen. nov., sp. nov., a rare and metabolically versatile member in the class <i>alphaproteobacteria</i>. Feb 2023. URL: https://doi.org/10.1128/spectrum.04110-22, doi:10.1128/spectrum.04110-22. This article has 10 citations and is from a domain leading peer-reviewed journal.

19. (liu2023isolationandgenomics media b4a990ce): Lirui Liu, Wen-Cong Huang, Jie Pan, Jiayi Li, Yuhan Huang, Dayu Zou, Huan Du, Yang Liu, and Meng Li. Isolation and genomics of <i>futiania mangrovii</i> gen. nov., sp. nov., a rare and metabolically versatile member in the class <i>alphaproteobacteria</i>. Feb 2023. URL: https://doi.org/10.1128/spectrum.04110-22, doi:10.1128/spectrum.04110-22. This article has 10 citations and is from a domain leading peer-reviewed journal.