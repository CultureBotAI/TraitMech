---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T10:52:43.215400'
end_time: '2026-06-18T11:16:34.651188'
duration_seconds: 1431.44
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: chemoheterotrophic
  trait_identifier: METPO:1000636
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: chemoheterotrophic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic type in which an organism obtains both energy and carbon from
    organic compounds.
  parent_traits: METPO:1000631
  synonyms: aerobic_chemo_heterotrophy, chemoheterotroph
  evidence_summary: 'DOI:10.1016/B978-012373944-5.00083-3: Chemoheterotroph (chemoorganoheterotroph)
    (Encyclopedia chapter maps chemoheterotrophy to chemical energy and reduced organic
    carbon.) | DOI:10.1021/acsomega.3c02205: chemoheterotrophic (Review table supports
    chemoheterotrophic use of organic molecules as energy and carbon sources.)'
  causal_graph_summary: 'chemoheterotrophic_organic_energy_carbon: 8 nodes, 9 edges'
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
- **Trait label:** chemoheterotrophic
- **METPO identifier:** METPO:1000636
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains both energy and carbon from organic compounds.
- **Parent traits:** METPO:1000631
- **Synonyms:** aerobic_chemo_heterotrophy, chemoheterotroph
- **Existing evidence:** DOI:10.1016/B978-012373944-5.00083-3: Chemoheterotroph (chemoorganoheterotroph) (Encyclopedia chapter maps chemoheterotrophy to chemical energy and reduced organic carbon.) | DOI:10.1021/acsomega.3c02205: chemoheterotrophic (Review table supports chemoheterotrophic use of organic molecules as energy and carbon sources.)
- **Existing causal graph summary:** chemoheterotrophic_organic_energy_carbon: 8 nodes, 9 edges

## Research Objective

Research the microbial trait **chemoheterotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/chemoheterotrophic.yaml`.

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
- **Trait label:** chemoheterotrophic
- **METPO identifier:** METPO:1000636
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains both energy and carbon from organic compounds.
- **Parent traits:** METPO:1000631
- **Synonyms:** aerobic_chemo_heterotrophy, chemoheterotroph
- **Existing evidence:** DOI:10.1016/B978-012373944-5.00083-3: Chemoheterotroph (chemoorganoheterotroph) (Encyclopedia chapter maps chemoheterotrophy to chemical energy and reduced organic carbon.) | DOI:10.1021/acsomega.3c02205: chemoheterotrophic (Review table supports chemoheterotrophic use of organic molecules as energy and carbon sources.)
- **Existing causal graph summary:** chemoheterotrophic_organic_energy_carbon: 8 nodes, 9 edges

## Research Objective

Research the microbial trait **chemoheterotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/chemoheterotrophic.yaml`.

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


# Microbial Trait Causal Graph Report: **chemoheterotrophic** (METPO:1000636)

## Scope summary (trait meaning, boundaries, and assay-readouts)

**Chemoheterotrophic (≈chemoorganoheterotrophic)** organisms obtain **energy and carbon from organic compounds**; in canonical phrasing from a recent review, for chemoorganoheterotrophic growth “organic molecules provide carbon, energy and electrons in the dark.” (stebegg2023heterotrophyamongcyanobacteria pages 1-2). In contrast, **photolithoautotrophy** uses **light as energy**, **water as electron donor**, and **CO2 as carbon source** (stebegg2023heterotrophyamongcyanobacteria pages 1-2); **photoheterotrophy/photoorganoheterotrophy** uses light energy but relies on organic carbon (stebegg2023heterotrophyamongcyanobacteria media 3460b4f2). 

**Boundary cases / nearby traits**:
- **Photomixotrophy** is described as “not a true form of heterotrophy” in cyanobacteria-focused definitions (stebegg2023heterotrophyamongcyanobacteria pages 2-4), emphasizing that annotation should not conflate facultative organic supplementation under light with true chemoheterotrophy.
- **Light-activated heterotrophic growth (LAHG)** is explicitly described as “a kind of chemoheterotrophic growth” in cyanobacteria, where limited illumination is required even though organic substrates support growth (stebegg2023heterotrophyamongcyanobacteria pages 2-2). This is a key boundary condition for phenotype assays.

**Operationalization / assays used in practice**:
- **Phenotype assays**: growth in **dark** (or extremely low light) on specified organic substrates, often quantified by doubling time or biomass increase (stebegg2023heterotrophyamongcyanobacteria pages 10-11, stebegg2023heterotrophyamongcyanobacteria pages 9-10).
- **Mechanistic assays**: gene knockout/functional genetics showing transporter or terminal oxidase requirements for dark growth (stebegg2023heterotrophyamongcyanobacteria pages 10-11).
- **Genome-based inference**: reconstruction of **central carbon catabolism** and substrate utilization modules, and (optionally) identification of **respiratory/fermentative** energy conservation systems and absence of dedicated carbon fixation pathways (rakitin2024verrucomicrobiaofthe pages 10-12).

## Key concepts and current understanding (2023–2024 emphasis)

### 1) The three-axis definition (carbon, energy, electrons)
Muramatsu & Winter (2024) summarize metabolic classification using **(i) carbon source (organic vs CO2), (ii) energy source (light vs chemical), and (iii) hydrogen/electron donor (organic vs H2O)**, and explicitly call most gut commensals **chemoorganoheterotrophs** that “degrade organic compounds to derive energy and biosynthetic intermediates.” (muramatsu2024nutrientacquisitionstrategies pages 1-2). This framing is helpful for curating boundaries between chemoheterotrophy and mixotrophy in environments like the gut.

### 2) Mechanistic core: “import → catabolize → conserve energy”
A concise mechanistic requirement captured in Stebegg et al. (2023) is that heterotrophic growth requires import and metabolism of organics “for the synthesis of ATP and NAD(P)H” without toxic accumulation (stebegg2023heterotrophyamongcyanobacteria pages 2-4). Figure 1 in the same review provides a schematic of organic substrate uptake/initial conversion steps (stebegg2023heterotrophyamongcyanobacteria media bbf47d3e), useful for curating upstream nodes (transport/kinases/isomerases).

### 3) Multiple terminal electron-acceptor regimes
Recent genome-centric studies emphasize that chemoheterotrophy is not restricted to aerobic respiration:
- In a peat-soil xylan degrader (Chthoniobacteraceae member SH-KS-3), central catabolism (glycolysis, pentose phosphate, TCA) co-occurs with **limited respiratory options**: cytochrome bd oxidase (microaerobic), and a **NapG-type nitrate reduction** module (nitrate→nitrite) but missing downstream nitrite reductases (rakitin2024verrucomicrobiaofthe pages 9-10).
- In cold seep sediments, the newly proposed phylum **Ca. Effluviviacota** is inferred to be **chemoheterotrophic and fermentative**, with **extracellular anaerobic respiration** apparently relying on **metals as electron acceptors** via multiheme cytochromes and a flavin-based EET system (NUO-DMK-EET-FMN) (su2024genomiccharacterizationof pages 1-3, su2024genomiccharacterizationof pages 10-12).

## Candidate causal graph entities (nodes) with grounding suggestions

A node inventory suitable for initial curation is provided here:

| Node label | Node type | Role in chemoheterotrophy | Evidence source(s) (DOI/year) | Suggested CURIE grounding |
|---|---|---|---|---|
| Candidate nodes for chemoheterotrophy graph | section | Scope marker for curation set | DOI:10.1021/acsomega.3c02205/2023; DOI:10.3390/microorganisms12112271/2024 | METPO:1000636 |
| Organic compounds | metabolite | Primary carbon and energy source defining chemoheterotrophy | DOI:10.1021/acsomega.3c02205/2023; DOI:10.1016/j.chom.2024.05.011/2024 (stebegg2023heterotrophyamongcyanobacteria pages 1-2, muramatsu2024nutrientacquisitionstrategies pages 1-2) | CHEBI:50860 |
| Glucose | metabolite | Common organic substrate used for growth/respiration | DOI:10.1021/acsomega.3c02205/2023 (stebegg2023heterotrophyamongcyanobacteria pages 9-10, stebegg2023heterotrophyamongcyanobacteria pages 2-4, stebegg2023heterotrophyamongcyanobacteria pages 13-14) | CHEBI:17234 |
| Fructose | metabolite | Organic substrate whose uptake supports dark chemoheterotrophic growth in cyanobacteria | DOI:10.1021/acsomega.3c02205/2023 (stebegg2023heterotrophyamongcyanobacteria pages 10-11) | CHEBI:15824 |
| Xylose | metabolite | Monosaccharide released from xylan and catabolized heterotrophically | DOI:10.3390/microorganisms12112271/2024; DOI:10.1021/acsomega.3c02205/2023 (rakitin2024verrucomicrobiaofthe pages 9-10, stebegg2023heterotrophyamongcyanobacteria pages 2-4) | CHEBI:27308 |
| Xylan | metabolite | Complex polysaccharide substrate supporting organotrophic growth | DOI:10.3390/microorganisms12112271/2024 (rakitin2024verrucomicrobiaofthe pages 9-10, rakitin2024verrucomicrobiaofthe pages 10-12) | CHEBI:37163 |
| Glycerol | metabolite | Importable reduced organic carbon source entering central metabolism | DOI:10.1021/acsomega.3c02205/2023 (stebegg2023heterotrophyamongcyanobacteria pages 1-2, stebegg2023heterotrophyamongcyanobacteria pages 2-4) | CHEBI:17754 |
| Mannitol | metabolite | Polyol substrate imported by PTS and funneled to glycolysis | DOI:10.1016/j.chom.2024.05.011/2024 (muramatsu2024nutrientacquisitionstrategies pages 2-4) | CHEBI:29864 |
| Peptides | metabolite | Organic carbon/nitrogen substrates degraded and assimilated by chemoheterotrophs | DOI:10.1128/mbio.00992-24/2024 (su2024genomiccharacterizationof pages 1-3, su2024genomiccharacterizationof pages 10-12) | CHEBI:16670 |
| Dissolved organic carbon (DOC) | metabolite | Community-level organic carbon pool that stimulates heterotrophic growth after reoxygenation | DOI:10.3389/fmicb.2023.1287477/2023 (parsons2023suboxicdomis pages 1-2, parsons2023suboxicdomis pages 2-3) | label only |
| Embden-Meyerhof(-Parnas) glycolysis | pathway | Core pathway extracting energy and precursors from organic substrates | DOI:10.3390/microorganisms12112271/2024; DOI:10.1128/mbio.00992-24/2024 (rakitin2024verrucomicrobiaofthe pages 9-10, su2024genomiccharacterizationof pages 1-3, rakitin2024verrucomicrobiaofthe pages 10-12) | KEGG:map00010 |
| Tricarboxylic acid cycle | pathway | Central oxidation pathway supporting respiratory chemoheterotrophy | DOI:10.3390/microorganisms12112271/2024 (rakitin2024verrucomicrobiaofthe pages 9-10, rakitin2024verrucomicrobiaofthe pages 10-12) | KEGG:map00020 |
| Non-oxidative pentose phosphate pathway | pathway | Sugar interconversion route supporting heterotrophic carbon assimilation | DOI:10.3390/microorganisms12112271/2024 (rakitin2024verrucomicrobiaofthe pages 9-10, rakitin2024verrucomicrobiaofthe pages 10-12) | KEGG:map00030 |
| Fermentation | process | Energy conservation route when external electron acceptors are limited | DOI:10.3390/microorganisms12112271/2024; DOI:10.1016/j.chom.2024.05.011/2024; DOI:10.1128/mbio.00992-24/2024 (rakitin2024verrucomicrobiaofthe pages 9-10, muramatsu2024nutrientacquisitionstrategies pages 1-2, su2024genomiccharacterizationof pages 10-12, muramatsu2024nutrientacquisitionstrategies pages 2-4) | GO:0006113 |
| Aerobic/anaerobic respiration | process | Electron transport-based energy conservation from organic substrates | DOI:10.1021/acsomega.3c02205/2023; DOI:10.3390/microorganisms12112271/2024 (stebegg2023heterotrophyamongcyanobacteria pages 1-2, rakitin2024verrucomicrobiaofthe pages 9-10, rakitin2024verrucomicrobiaofthe pages 10-12) | GO:0009060 |
| Extracellular electron transfer (EET) | process | Enables anaerobic chemoheterotrophy with external metal electron acceptors | DOI:10.1128/mbio.00992-24/2024 (su2024genomiccharacterizationof pages 1-3, su2024genomiccharacterizationof pages 10-12, su2024genomiccharacterizationof pages 17-17) | GO:0140657 |
| Oxidative phosphorylation / electron transport chain | process | Couples substrate oxidation to ATP synthesis | DOI:10.3390/microorganisms12112271/2024; DOI:10.1021/acsomega.3c02205/2023 (rakitin2024verrucomicrobiaofthe pages 9-10, stebegg2023heterotrophyamongcyanobacteria pages 10-11) | GO:0006119 |
| GlpK (glycerol kinase) | enzyme | Phosphorylates glycerol after uptake | DOI:10.1021/acsomega.3c02205/2023 (stebegg2023heterotrophyamongcyanobacteria pages 2-4) | EC:2.7.1.30 |
| Glk (glucokinase) | enzyme | Phosphorylates glucose for entry into central metabolism | DOI:10.1021/acsomega.3c02205/2023 (stebegg2023heterotrophyamongcyanobacteria pages 2-4) | EC:2.7.1.2 |
| XylA (xylose isomerase) | enzyme | Converts xylose to xylulose in heterotrophic pentose utilization | DOI:10.1021/acsomega.3c02205/2023; DOI:10.3390/microorganisms12112271/2024 (stebegg2023heterotrophyamongcyanobacteria pages 2-4, rakitin2024verrucomicrobiaofthe pages 9-10) | EC:5.3.1.5 |
| XylB (xylulokinase) | enzyme | Converts xylulose to xylulose-5-phosphate | DOI:10.1021/acsomega.3c02205/2023; DOI:10.3390/microorganisms12112271/2024 (stebegg2023heterotrophyamongcyanobacteria pages 2-4, rakitin2024verrucomicrobiaofthe pages 9-10) | EC:2.7.1.17 |
| slr0453 phosphoketolase | gene/enzyme | Supports acetate-forming carbon flux during heterotrophic metabolism | DOI:10.1021/acsomega.3c02205/2023 (stebegg2023heterotrophyamongcyanobacteria pages 9-10) | label only |
| Pyruvate dehydrogenase complex (PDH) | complex | Converts pyruvate to acetyl-CoA in central carbon metabolism | DOI:10.3390/microorganisms12112271/2024 (rakitin2024verrucomicrobiaofthe pages 9-10) | EC:1.2.4.1 |
| Pyruvate formate lyase (PFL) | enzyme | Fermentative pyruvate conversion to formate/acetyl-CoA | DOI:10.3390/microorganisms12112271/2024 (rakitin2024verrucomicrobiaofthe pages 9-10, rakitin2024verrucomicrobiaofthe pages 10-12) | EC:2.3.1.54 |
| Lactate dehydrogenase (LDH) | enzyme | Produces/consumes lactate during fermentative metabolism | DOI:10.3390/microorganisms12112271/2024 (rakitin2024verrucomicrobiaofthe pages 9-10) | EC:1.1.1.27 |
| Phosphate acetyltransferase (PTA) | enzyme | Converts acetyl-CoA toward acetate production | DOI:10.3390/microorganisms12112271/2024 (rakitin2024verrucomicrobiaofthe pages 9-10) | EC:2.3.1.8 |
| Acetate kinase (ACK) | enzyme | Generates acetate and ATP from acetyl-phosphate | DOI:10.3390/microorganisms12112271/2024 (rakitin2024verrucomicrobiaofthe pages 9-10) | EC:2.7.2.1 |
| frtABC fructose transporter | transporter/complex | Imports fructose needed for dark chemoheterotrophic growth | DOI:10.1021/acsomega.3c02205/2023 (stebegg2023heterotrophyamongcyanobacteria pages 10-11) | label only |
| frtR | gene/protein | Regulatory component linked to fructose uptake operon and dark growth on fructose | DOI:10.1021/acsomega.3c02205/2023 (stebegg2023heterotrophyamongcyanobacteria pages 10-11) | label only |
| glsC/glsP/glsD/glsQ/glsR | gene set | Putative sugar transport genes affecting fructose-supported heterotrophic growth | DOI:10.1021/acsomega.3c02205/2023 (stebegg2023heterotrophyamongcyanobacteria pages 10-11) | label only |
| Glycerol uptake facilitator | transporter | Supports glycerol import for chemoheterotrophic metabolism | DOI:10.3390/microorganisms12112271/2024; DOI:10.1021/acsomega.3c02205/2023 (rakitin2024verrucomicrobiaofthe pages 9-10, stebegg2023heterotrophyamongcyanobacteria pages 2-4) | GO:0015773 |
| SusC/TonB-dependent transporter system | transporter/complex | Imports oligosaccharides generated from complex carbohydrate degradation | DOI:10.1016/j.chom.2024.05.011/2024 (muramatsu2024nutrientacquisitionstrategies pages 2-4) | label only |
| PEP-dependent phosphotransferase system (mannitol PTS) | transporter/complex | Imports and phosphorylates mannitol during uptake | DOI:10.1016/j.chom.2024.05.011/2024 (muramatsu2024nutrientacquisitionstrategies pages 2-4) | GO:0009401 |
| Amino acid/carbohydrate ABC transporters | transporter/complex | Import soluble organic nutrients supporting chemoheterotrophy | DOI:10.1128/mbio.00992-24/2024; DOI:10.1186/s40168-023-01728-2/2024 (su2024genomiccharacterizationof pages 10-12) | GO:0015420 |
| aa3-type cytochrome c oxidase (coxBAC) | complex | Terminal oxidase required for fructose-based dark growth in cyanobacterial example | DOI:10.1021/acsomega.3c02205/2023 (stebegg2023heterotrophyamongcyanobacteria pages 10-11, stebegg2023heterotrophyamongcyanobacteria pages 9-10) | EC:7.1.1.9 |
| Cytochrome bd oxidase | complex | High-affinity terminal oxidase supporting microaerobic respiration | DOI:10.3390/microorganisms12112271/2024 (rakitin2024verrucomicrobiaofthe pages 9-10) | EC:7.1.1.7 |
| NapG-type nitrate reductase | enzyme/complex | Enables nitrate reduction as alternative electron-accepting process | DOI:10.3390/microorganisms12112271/2024 (rakitin2024verrucomicrobiaofthe pages 9-10) | EC:1.9.6.1 |
| Multiheme cytochromes | protein/complex | Mediate electron transfer to extracellular metal acceptors | DOI:10.1128/mbio.00992-24/2024 (su2024genomiccharacterizationof pages 1-3, su2024genomiccharacterizationof pages 10-12) | label only |
| NUO-DMK-EET-FMN complex | complex | Flavin-based EET machinery linked to anaerobic respiration on metals | DOI:10.1128/mbio.00992-24/2024 (su2024genomiccharacterizationof pages 1-3, su2024genomiccharacterizationof pages 10-12) | label only |
| Flavins / flavin shuttles | metabolite | Soluble/cofactor mediators in extracellular electron transfer | DOI:10.1128/mbio.00992-24/2024 (su2024genomiccharacterizationof pages 1-3, su2024genomiccharacterizationof pages 17-17) | CHEBI:17621 |
| Oxygen | environment | Major terminal electron acceptor in aerobic chemoheterotrophy | DOI:10.1021/acsomega.3c02205/2023; DOI:10.3390/microorganisms12112271/2024 (stebegg2023heterotrophyamongcyanobacteria pages 1-2, rakitin2024verrucomicrobiaofthe pages 9-10) | CHEBI:15379 |
| Nitrate | metabolite/environment | Alternative electron acceptor in some anaerobic/microaerobic chemoheterotrophs | DOI:10.3390/microorganisms12112271/2024 (rakitin2024verrucomicrobiaofthe pages 9-10, rakitin2024verrucomicrobiaofthe pages 10-12) | CHEBI:17632 |
| Metals (external metal acceptors) | environment | Terminal electron acceptors in EET-enabled anaerobic chemoheterotrophy | DOI:10.1128/mbio.00992-24/2024 (su2024genomiccharacterizationof pages 1-3, su2024genomiccharacterizationof pages 10-12) | CHEBI:33521 |
| Acetate | metabolite | Fermentation end product and central overflow metabolite | DOI:10.3390/microorganisms12112271/2024; DOI:10.1016/j.chom.2024.05.011/2024; DOI:10.1021/acsomega.3c02205/2023 (rakitin2024verrucomicrobiaofthe pages 9-10, muramatsu2024nutrientacquisitionstrategies pages 2-4, stebegg2023heterotrophyamongcyanobacteria pages 9-10) | CHEBI:30089 |
| Propionate | metabolite | Short-chain fatty acid produced by gut chemoorganoheterotrophs | DOI:10.1016/j.chom.2024.05.011/2024 (muramatsu2024nutrientacquisitionstrategies pages 2-4) | CHEBI:16526 |
| Succinate | metabolite | Fermentation product/intermediate in gut heterotrophs | DOI:10.1016/j.chom.2024.05.011/2024 (muramatsu2024nutrientacquisitionstrategies pages 2-4) | CHEBI:15741 |
| Lactate | metabolite | Fermentation product linked to LDH activity | DOI:10.3390/microorganisms12112271/2024 (rakitin2024verrucomicrobiaofthe pages 9-10) | CHEBI:24996 |
| Formate | metabolite | Fermentation product linked to PFL activity | DOI:10.3390/microorganisms12112271/2024 (rakitin2024verrucomicrobiaofthe pages 9-10) | CHEBI:15740 |
| Dark growth on organic substrates | assay | Classical phenotype readout for chemoheterotrophy | DOI:10.1021/acsomega.3c02205/2023 (stebegg2023heterotrophyamongcyanobacteria pages 10-11, stebegg2023heterotrophyamongcyanobacteria pages 1-2) | label only |
| Gene knockout of transport/oxidase genes | assay | Functional test linking frtR/frtABC/gls genes/coxBAC to chemoheterotrophic growth | DOI:10.1021/acsomega.3c02205/2023 (stebegg2023heterotrophyamongcyanobacteria pages 10-11) | label only |
| DOC removal during incubation | assay | Community-level assay for heterotrophic utilization of organic carbon | DOI:10.3389/fmicb.2023.1287477/2023 (parsons2023suboxicdomis pages 1-2, parsons2023suboxicdomis pages 2-3) | label only |
| Dark condition | environment | Diagnostic condition distinguishing chemoheterotrophy from phototrophy | DOI:10.1021/acsomega.3c02205/2023 (stebegg2023heterotrophyamongcyanobacteria pages 1-2, stebegg2023heterotrophyamongcyanobacteria pages 2-4) | ENVO:01000379 |
| Low oxygen / microaerobic condition | environment | Favors use of high-affinity oxidases such as cytochrome bd | DOI:10.3390/microorganisms12112271/2024 (rakitin2024verrucomicrobiaofthe pages 9-10) | label only |
| Reoxygenation | environment/process | Changes DOC bioavailability and stimulates heterotrophic community growth | DOI:10.3389/fmicb.2023.1287477/2023 (parsons2023suboxicdomis pages 1-2, parsons2023suboxicdomis pages 2-3) | label only |
| Gut anaerobiosis / anoxic colon | environment | Selects for fermentative chemoorganoheterotrophs | DOI:10.1016/j.chom.2024.05.011/2024 (muramatsu2024nutrientacquisitionstrategies pages 1-2, muramatsu2024nutrientacquisitionstrategies pages 2-4) | ENVO:01001006 |


*Table: This table lists candidate nodes for a chemoheterotrophy causal graph, spanning substrates, pathways, enzymes, transporters, electron acceptors, products, environments, and assays. It is useful for TraitMech curation because it links each node to recent evidence and suggests ontology grounding where available.*

Key takeaways for TraitMech curation:
- **Core pathways** likely to be broadly portable: glycolysis (EMP), fermentation, respiration/electron transport, central carbon metabolism (TCA varies by lineage and condition), and CAZyme-driven depolymerization for complex substrates (rakitin2024verrucomicrobiaofthe pages 9-10, su2024genomiccharacterizationof pages 1-3, muramatsu2024nutrientacquisitionstrategies pages 2-4).
- **Transporters** are often the trait-limiting step (substrate availability may not imply growth unless uptake exists) (stebegg2023heterotrophyamongcyanobacteria pages 2-4).

## Evidence-backed candidate edges (triples) for graph curation

A curation-oriented edge set (with uncertainty flags and grounding suggestions) is provided here:

| Subject node | Predicate | Object node | Evidence snippet (short quote) | Source (DOI, year, URL) | Notes/uncertainty | Suggested ontology grounding (CURIEs) |
|---|---|---|---|---|---|---|
| chemoheterotrophy | has_energy_source | organic compounds | “organic molecules provide carbon, energy and electrons in the dark” (stebegg2023heterotrophyamongcyanobacteria pages 1-2) | DOI:10.1021/acsomega.3c02205, 2023, https://doi.org/10.1021/acsomega.3c02205 | Trait-scope edge; wording from review excerpt, broadly applicable | subject: METPO:1000636; object: CHEBI:50860 |
| chemoheterotrophy | contrasted_with | photolithoautotrophy | “contrasts this with photolithoautotrophy, where light supplies energy… and CO2 is the sole carbon source” (stebegg2023heterotrophyamongcyanobacteria pages 1-2) | DOI:10.1021/acsomega.3c02205, 2023, https://doi.org/10.1021/acsomega.3c02205 | Boundary-case edge for curation scope; paraphrased from excerpt | subject: METPO:1000636; object: label only candidate photolithoautotrophy |
| frtABC fructose transporter | enables_uptake_of | fructose | “frtABC operon encodes a fructose transporter” (stebegg2023heterotrophyamongcyanobacteria pages 10-11) | DOI:10.1021/acsomega.3c02205, 2023, https://doi.org/10.1021/acsomega.3c02205 | Taxon-specific to cyanobacteria/Anabaena; transporter gene family grounding unclear | subject: label only frtABC; object: CHEBI:15824 |
| frtR | positively_regulates_requirement_for | chemoheterotrophic growth on fructose | “deletion of frtR abolishes dark growth on fructose” (stebegg2023heterotrophyamongcyanobacteria pages 10-11) | DOI:10.1021/acsomega.3c02205, 2023, https://doi.org/10.1021/acsomega.3c02205 | Taxon-specific and phenotype-specific; paraphrased from excerpt | subject: label only frtR; object: METPO:1000636 + CHEBI:15824 |
| coxBAC aa3-type cytochrome c oxidase | enables | fructose-based dark growth | “aa3-type cytochrome c oxidase… required for fructose-based dark growth” (stebegg2023heterotrophyamongcyanobacteria pages 10-11, stebegg2023heterotrophyamongcyanobacteria pages 9-10) | DOI:10.1021/acsomega.3c02205, 2023, https://doi.org/10.1021/acsomega.3c02205 | Strong mechanistic evidence but cyanobacteria-specific | subject: label only coxBAC; object: label only dark growth on fructose |
| glsC/glsP/glsD/glsQ/glsR sugar transport genes | promotes | chemoheterotrophic fructose growth | “knocked out reduce… chemoheterotrophic fructose growth” (stebegg2023heterotrophyamongcyanobacteria pages 10-11) | DOI:10.1021/acsomega.3c02205, 2023, https://doi.org/10.1021/acsomega.3c02205 | Taxon-specific; paraphrased from excerpt; group node may be preferable | subject: label only gls transporter set; object: METPO:1000636 + CHEBI:15824 |
| xylose isomerase + xylulose kinase | enables_catabolism_of | xylose | “xylose pathway enzymes (xylose isomerase, xylulose kinase)” (rakitin2024verrucomicrobiaofthe pages 9-10, rakitin2024verrucomicrobiaofthe pages 10-12) | DOI:10.3390/microorganisms12112271, 2024, https://doi.org/10.3390/microorganisms12112271 | Genome-inferred in MAG/cultured genome context; moderate confidence | subject: EC:5.3.1.5 + EC:2.7.1.17; object: CHEBI:27308 |
| xylanase/β-xylosidase/arabinofuranosidase/acetyl xylan esterase | degrades | xylan | “xylanases and side-chain cleaving enzymes… β-1,4-xylosidase… α-L-arabinofuranosidase, acetyl xylan esterase” (rakitin2024verrucomicrobiaofthe pages 9-10, rakitin2024verrucomicrobiaofthe pages 10-12) | DOI:10.3390/microorganisms12112271, 2024, https://doi.org/10.3390/microorganisms12112271 | Good node cluster for polymer-to-monomer edge; enzyme set collapsed | subject: EC:3.2.1.8 + label others; object: CHEBI:37163 |
| Embden–Meyerhof glycolysis pathway | contributes_to | chemoheterotrophic metabolism | “encodes… Embden–Meyerhof pathway” (rakitin2024verrucomicrobiaofthe pages 9-10); “harbor the Embden–Meyerhof–Parnas glycolysis pathway” (su2024genomiccharacterizationof pages 1-3) | DOI:10.3390/microorganisms12112271, 2024, https://doi.org/10.3390/microorganisms12112271; DOI:10.1128/mbio.00992-24, 2024, https://doi.org/10.1128/mbio.00992-24 | Broad mechanistic core; partly genome-inferred | subject: KEGG:map00010; object: METPO:1000636 |
| tricarboxylic acid cycle | contributes_to | chemoheterotrophic metabolism | “Embden–Meyerhof… and tricarboxylic acid cycle” (rakitin2024verrucomicrobiaofthe pages 9-10) | DOI:10.3390/microorganisms12112271, 2024, https://doi.org/10.3390/microorganisms12112271 | Inferred from genome reconstruction; may not be universal for all chemoheterotrophs | subject: KEGG:map00020; object: METPO:1000636 |
| pyruvate formate lyase | enables_fermentative_conversion_of | pyruvate to formate/acetyl-CoA | “pyruvate formate lyase” and likely “formate… fermentation products” (rakitin2024verrucomicrobiaofthe pages 9-10) | DOI:10.3390/microorganisms12112271, 2024, https://doi.org/10.3390/microorganisms12112271 | Product wording paraphrased from excerpt; genome-based inference | subject: EC:2.3.1.54; object: CHEBI:15361 |
| phosphate acetyltransferase + acetate kinase | enables_production_of | acetate | “acetyl–CoA can be converted to acetate via phosphate acetyltransferase and acetate kinase” (rakitin2024verrucomicrobiaofthe pages 9-10) | DOI:10.3390/microorganisms12112271, 2024, https://doi.org/10.3390/microorganisms12112271 | Strong mechanistic edge; genome-inferred in SH-KS-3 | subject: EC:2.3.1.8 + EC:2.7.2.1; object: CHEBI:30089 |
| cytochrome bd oxidase | supports_respiration_under | low oxygen / microaerobic conditions | “retaining cytochrome bd oxidase (high O2 affinity), consistent with microaerobic/anaerobic respiration” (rakitin2024verrucomicrobiaofthe pages 9-10) | DOI:10.3390/microorganisms12112271, 2024, https://doi.org/10.3390/microorganisms12112271 | Environmental-physiology edge; paraphrased from excerpt; not universal | subject: GO:0004129 or label cytochrome bd oxidase; object: ENVO:01001023 low oxygen? / label microaerobic condition |
| NapG-type periplasmic nitrate reductase | reduces | nitrate to nitrite | “NapG-type periplasmic nitrate reductase (nitrate → nitrite)” (rakitin2024verrucomicrobiaofthe pages 9-10) | DOI:10.3390/microorganisms12112271, 2024, https://doi.org/10.3390/microorganisms12112271 | Specific respiratory edge; restricted to some taxa/genomes | subject: EC:1.9.6.1 or label Nap-type nitrate reductase; object: CHEBI:17632 -> CHEBI:16301 |
| fermentation | generates | short-chain fatty acids | “subsequent fermentation to short-chain fatty acids (acetate, succinate, propionate)” (muramatsu2024nutrientacquisitionstrategies pages 2-4) | DOI:10.1016/j.chom.2024.05.011, 2024, https://doi.org/10.1016/j.chom.2024.05.011 | Gut-focused but broadly useful; SCFA set collapsed | subject: GO:0006113; object: CHEBI:26666 / CHEBI:30089 / CHEBI:15741 / CHEBI:16526 |
| PEP-dependent phosphotransferase system (mannitol PTS) | imports_and_phosphorylates | mannitol | “mannitol is imported/phosphorylated via a PEP-PTS to mannitol-1-phosphate” (muramatsu2024nutrientacquisitionstrategies pages 2-4) | DOI:10.1016/j.chom.2024.05.011, 2024, https://doi.org/10.1016/j.chom.2024.05.011 | Strong mechanistic uptake edge; gut-associated example | subject: GO:0009401 or label mannitol PTS; object: CHEBI:29864 |
| mtlD mannitol-1-phosphate dehydrogenase | converts | mannitol-1-phosphate to fructose-6-phosphate | “converted by mtlD to fructose-6-phosphate and enters glycolysis” (muramatsu2024nutrientacquisitionstrategies pages 2-4) | DOI:10.1016/j.chom.2024.05.011, 2024, https://doi.org/10.1016/j.chom.2024.05.011 | Good bridge from transport to central carbon metabolism; paraphrased from excerpt | subject: EC:1.1.1.17 or label mtlD; object: CHEBI:58175 -> CHEBI:61548 |
| Sus polysaccharide utilization system | enables_utilization_of | non-digestible dietary carbohydrates | “degraded by dedicated CAZymes and polysaccharide utilization loci (e.g., the Sus system in Bacteroides)” (muramatsu2024nutrientacquisitionstrategies pages 2-4) | DOI:10.1016/j.chom.2024.05.011, 2024, https://doi.org/10.1016/j.chom.2024.05.011 | Gut-specific but canonical organotrophic uptake/degradation module | subject: label Sus system; object: label non-digestible dietary carbohydrates |
| multiheme cytochromes + NUO-DMK-EET-FMN complex | transfers_electrons_to | metals as terminal electron acceptors | “Extracellular anaerobic respiration appears to rely on metals as electron acceptors… mediated by multiheme cytochromes and… NUO-DMK-EET-FMN complex” (su2024genomiccharacterizationof pages 1-3, su2024genomiccharacterizationof pages 10-12) | DOI:10.1128/mbio.00992-24, 2024, https://doi.org/10.1128/mbio.00992-24 | Genome-inferred and phylum-specific; strong for EET-enabled chemoheterotrophy in anoxic sediments | subject: label multiheme cytochromes/NUO-DMK-EET-FMN; object: CHEBI:33521 metals |
| dissolved organic carbon | stimulates_growth_of | surface heterotrophic prokaryotes after reoxygenation | “cell densities increasing 2.5-fold over 6 days while removing 5 μmol L−1 of DOC” (parsons2023suboxicdomis pages 1-2, parsons2023suboxicdomis pages 2-3) | DOI:10.3389/fmicb.2023.1287477, 2023, https://doi.org/10.3389/fmicb.2023.1287477 | Community-level ecological edge, not gene-level; useful environment-to-trait relation | subject: label dissolved organic carbon; object: label surface heterotrophic prokaryotes |
| glucose co-substrate | enhances | PFOA removal by bacteria | “48.1% removal by Pseudomonas parafulva YAB-1 over 96 h with 1 g/L glucose” (smorada2024bacterialdegradationof pages 1-3) | DOI:10.1016/j.copbio.2024.103170, 2024, https://doi.org/10.1016/j.copbio.2024.103170 | Application edge; likely strain- and assay-specific, not general chemoheterotrophy mechanism | subject: CHEBI:17234; object: CHEBI:6464 PFOA |
| aerobic heterotrophic bacteria | can_achieve | high biomass productivity and conversion efficiency | “10–200 g dry matter per litre per day,” “80%–100% nitrogen/protein conversion,” “55%–75% energy/COD conversion” (javourez2024ruminationsonsustainable pages 1-2) | DOI:10.1111/1751-7915.14436, 2024, https://doi.org/10.1111/1751-7915.14436 | Process-performance edge for applications; opinion/review source rather than direct experiment | subject: label aerobic heterotrophic bacteria; object: label high productivity/conversion efficiency |


*Table: This table compiles candidate subject-predicate-object edges for curating a chemoheterotrophy TraitMech graph, using only the provided 2023-2024 evidence. It highlights trait-defining scope edges, core metabolic mechanisms, taxon-specific genetic modules, and selected ecological/application edges with uncertainty notes and ontology suggestions.*

## Recent developments (2023–2024) and what is “new”

### A) Genome-centric trait inference is expanding chemoheterotrophy mechanisms beyond “aerobic respiration”
Recent metagenome-driven reconstructions are mapping chemoheterotrophy onto:
- **Polymer degradation + fermentation** in anoxic niches (e.g., EMP glycolysis plus fermentation in Ca. Effluviviacota) (su2024genomiccharacterizationof pages 1-3).
- **Metal-associated extracellular electron transfer** as a plausible terminal electron-acceptor strategy in cold seeps (su2024genomiccharacterizationof pages 1-3, su2024genomiccharacterizationof pages 10-12).
This broadens curation beyond oxygen-centric edges and motivates inclusion of **EET modules** and **metal acceptors** as environmental/mechanistic nodes.

### B) Increasing linkage of chemoheterotrophy to community shifts across redox transitions
In an oxygen minimum zone (OMZ) overturn simulation, reoxygenation made suboxic DOM bioavailable to surface prokaryotes: **cell densities increased 2.5-fold over 6 days while removing 5 µmol L−1 DOC** (parsons2023suboxicdomis pages 1-2). Such time-resolved data support environment→substrate availability→heterotrophic growth edges relevant to carbon-cycle modeling.

### C) Expanding phenotype-to-gene links for dark/chemoheterotrophic growth (cyanobacteria example)
Stebegg et al. (2023) compile cases where chemoheterotrophic growth in cyanobacteria depends on specific genetic modules:
- **frtABC** fructose transporter and regulator **frtR**; loss of frtR abolishes dark growth on fructose (stebegg2023heterotrophyamongcyanobacteria pages 10-11).
- **coxBAC** aa3-type cytochrome c oxidase required for fructose-based dark growth (stebegg2023heterotrophyamongcyanobacteria pages 10-11, stebegg2023heterotrophyamongcyanobacteria pages 9-10).
These are taxon-specific but exemplify how to encode “substrate uptake → respiratory chain” dependencies.

## Current applications and real-world implementations (with quantitative statistics)

### 1) Gut microbiome: chemoorganoheterotrophy as dominant lifestyle and fermentation as energy conservation
Most gut commensals are framed as chemoorganoheterotrophs (muramatsu2024nutrientacquisitionstrategies pages 1-2). Quantitative ecological context: microbial density increases from ~10^3–10^7 per gram in the small intestine to ~10^11–10^12 per gram in the colon (muramatsu2024nutrientacquisitionstrategies pages 1-2, muramatsu2024nutrientacquisitionstrategies pages 2-4). Mechanistically, complex carbohydrate utilization involves CAZymes and polysaccharide utilization loci such as the Sus system, with downstream fermentation to SCFAs (acetate/succinate/propionate) (muramatsu2024nutrientacquisitionstrategies pages 2-4).

### 2) Marine carbon cycling / OMZ reoxygenation: measurable DOC drawdown by heterotrophic communities
In the Devil’s Hole OMZ overturn simulation, surface communities removed **5 µmol L−1 DOC** and increased **2.5-fold** in 6 days (parsons2023suboxicdomis pages 1-2); experimental context includes suboxic oxygen levels (<20 µmol L−1) and DOC gradients (surface ~94.8 µmol C L−1 vs deep ~110.1 µmol C L−1) (parsons2023suboxicdomis pages 2-3). This supports use of chemoheterotrophic activity as a predictive process in reoxygenation events.

### 3) Bioremediation of PFAS/PFOA: co-metabolism and quantifiable removal
A 2024 Current Opinion in Biotechnology review reports multiple quantitative PFOA biodegradation outcomes, including **48.1% removal over 96 h with 1 g/L glucose** by *Pseudomonas parafulva* YAB-1 (and higher values in engineered variants), plus cases of fluoride release as evidence of defluorination (smorada2024bacterialdegradationof pages 1-3). These reports motivate edges connecting **organic co-substrates (electron donors)** to **xenobiotic transformation** (application-specific; not necessarily generalizable).

### 4) Industrial bioprocess / food biotech: high productivities for aerobic heterotroph-based biomass
A 2024 expert/opinion perspective highlights that aerobic heterotrophic bacteria can show high process efficiencies, quoting **10–200 g dry matter L−1 day−1** productivities and **80%–100% nitrogen/protein conversion** and **55%–75% energy/COD conversion** (javourez2024ruminationsonsustainable pages 1-2). While not a primary experimental report, it provides useful quantitative targets and highlights why chemoheterotrophy is central in “microbial protein” and residue-upgrading concepts.

## Expert synthesis / analysis (curation implications)

1. **Chemoheterotrophy is best curated as a trophic “class” trait**, but its mechanistic graph should likely be structured around a small set of **core necessary modules**: organic substrate uptake + organic carbon catabolism (glycolysis/fermentation/respiration) + ATP generation (substrate-level phosphorylation and/or electron transport), rather than any single pathway like TCA (which is variable across taxa/conditions) (rakitin2024verrucomicrobiaofthe pages 9-10, stebegg2023heterotrophyamongcyanobacteria pages 2-4).

2. **Electron acceptor diversity should be encoded explicitly** (O2, nitrate, metals via EET), since modern genome-centric work is uncovering lineage-specific strategies that still satisfy the high-level trait definition (rakitin2024verrucomicrobiaofthe pages 9-10, su2024genomiccharacterizationof pages 1-3, su2024genomiccharacterizationof pages 10-12).

3. **Assay context must be captured**: dark growth and “LAHG” demonstrate that some organisms labeled chemoheterotrophic may require minimal light, creating a risk of misannotation unless conditions are recorded (stebegg2023heterotrophyamongcyanobacteria pages 2-2, stebegg2023heterotrophyamongcyanobacteria media 3460b4f2).

## Warnings / claims not ready to curate (or curate as uncertain)

- **Taxon-specific gene–trait dependencies** (e.g., frtRABC, gls genes, coxBAC requirements) are strong within the cited cyanobacterial systems but should be marked as **lineage-specific** rather than universal chemoheterotrophy mechanisms (stebegg2023heterotrophyamongcyanobacteria pages 10-11).
- **Genome-inferred physiology** (MAG-derived or single-genome reconstruction) should be captured with an “inferred_from_genome” evidence tag and potential MAG incompleteness caveats, especially when asserting absence of pathways or terminal reductases (rakitin2024verrucomicrobiaofthe pages 9-10, rakitin2024verrucomicrobiaofthe pages 10-12).
- **Application edges** (e.g., glucose-enhanced PFOA removal) are often **assay- and strain-specific**, and may not represent a stable mechanistic edge for the trait itself (smorada2024bacterialdegradationof pages 1-3).

## DOI-first bibliography (2023–2024 prioritized)

1. **Stebegg R, Schmetterer G, Rompel A.** Heterotrophy among Cyanobacteria. *ACS Omega* (Sep 2023). DOI: **10.1021/acsomega.3c02205**. URL: https://doi.org/10.1021/acsomega.3c02205 (stebegg2023heterotrophyamongcyanobacteria pages 1-2, stebegg2023heterotrophyamongcyanobacteria media 3460b4f2, stebegg2023heterotrophyamongcyanobacteria media bbf47d3e)
2. **Rakitin AL, et al.** Verrucomicrobia of the family Chthoniobacteraceae participate in xylan degradation in boreal peat soils. *Microorganisms* (Nov 2024). DOI: **10.3390/microorganisms12112271**. URL: https://doi.org/10.3390/microorganisms12112271 (rakitin2024verrucomicrobiaofthe pages 9-10, rakitin2024verrucomicrobiaofthe pages 10-12)
3. **Su L, et al.** Genomic characterization of the bacterial phylum *Candidatus* Effluviviacota, a cosmopolitan member of the global seep microbiome. *mBio* (Aug 2024). DOI: **10.1128/mbio.00992-24**. URL: https://doi.org/10.1128/mbio.00992-24 (su2024genomiccharacterizationof pages 1-3, su2024genomiccharacterizationof pages 10-12)
4. **Muramatsu MK, Winter SE.** Nutrient acquisition strategies by gut microbes. *Cell Host & Microbe* (Jun 2024). DOI: **10.1016/j.chom.2024.05.011**. URL: https://doi.org/10.1016/j.chom.2024.05.011 (muramatsu2024nutrientacquisitionstrategies pages 1-2, muramatsu2024nutrientacquisitionstrategies pages 2-4)
5. **Parsons RJ, et al.** Suboxic DOM is bioavailable to surface prokaryotes in a simulated overturn of an oxygen minimum zone, Devil’s Hole, Bermuda. *Frontiers in Microbiology* (Dec 2023). DOI: **10.3389/fmicb.2023.1287477**. URL: https://doi.org/10.3389/fmicb.2023.1287477 (parsons2023suboxicdomis pages 1-2, parsons2023suboxicdomis pages 2-3)
6. **Smorada CM, Sima MW, Jaffé PR.** Bacterial degradation of perfluoroalkyl acids. *Current Opinion in Biotechnology* (Aug 2024). DOI: **10.1016/j.copbio.2024.103170**. URL: https://doi.org/10.1016/j.copbio.2024.103170 (smorada2024bacterialdegradationof pages 1-3)
7. **Javourez U, Matassa S, Vlaeminck SE, Verstraete W.** Ruminations on sustainable and safe food: Championing for open symbiotic cultures ensuring resource efficiency, eco‐sustainability and affordability. *Microbial Biotechnology* (Mar 2024). DOI: **10.1111/1751-7915.14436**. URL: https://doi.org/10.1111/1751-7915.14436 (javourez2024ruminationsonsustainable pages 1-2)


References

1. (stebegg2023heterotrophyamongcyanobacteria pages 1-2): Ronald Stebegg, Georg Schmetterer, and Annette Rompel. Heterotrophy among cyanobacteria. ACS Omega, 8:33098-33114, Sep 2023. URL: https://doi.org/10.1021/acsomega.3c02205, doi:10.1021/acsomega.3c02205. This article has 37 citations and is from a peer-reviewed journal.

2. (stebegg2023heterotrophyamongcyanobacteria media 3460b4f2): Ronald Stebegg, Georg Schmetterer, and Annette Rompel. Heterotrophy among cyanobacteria. ACS Omega, 8:33098-33114, Sep 2023. URL: https://doi.org/10.1021/acsomega.3c02205, doi:10.1021/acsomega.3c02205. This article has 37 citations and is from a peer-reviewed journal.

3. (stebegg2023heterotrophyamongcyanobacteria pages 2-4): Ronald Stebegg, Georg Schmetterer, and Annette Rompel. Heterotrophy among cyanobacteria. ACS Omega, 8:33098-33114, Sep 2023. URL: https://doi.org/10.1021/acsomega.3c02205, doi:10.1021/acsomega.3c02205. This article has 37 citations and is from a peer-reviewed journal.

4. (stebegg2023heterotrophyamongcyanobacteria pages 2-2): Ronald Stebegg, Georg Schmetterer, and Annette Rompel. Heterotrophy among cyanobacteria. ACS Omega, 8:33098-33114, Sep 2023. URL: https://doi.org/10.1021/acsomega.3c02205, doi:10.1021/acsomega.3c02205. This article has 37 citations and is from a peer-reviewed journal.

5. (stebegg2023heterotrophyamongcyanobacteria pages 10-11): Ronald Stebegg, Georg Schmetterer, and Annette Rompel. Heterotrophy among cyanobacteria. ACS Omega, 8:33098-33114, Sep 2023. URL: https://doi.org/10.1021/acsomega.3c02205, doi:10.1021/acsomega.3c02205. This article has 37 citations and is from a peer-reviewed journal.

6. (stebegg2023heterotrophyamongcyanobacteria pages 9-10): Ronald Stebegg, Georg Schmetterer, and Annette Rompel. Heterotrophy among cyanobacteria. ACS Omega, 8:33098-33114, Sep 2023. URL: https://doi.org/10.1021/acsomega.3c02205, doi:10.1021/acsomega.3c02205. This article has 37 citations and is from a peer-reviewed journal.

7. (rakitin2024verrucomicrobiaofthe pages 10-12): Andrey L. Rakitin, Irina S. Kulichevskaya, Alexey V. Beletsky, Andrey V. Mardanov, Svetlana N. Dedysh, and Nikolai V. Ravin. Verrucomicrobia of the family chthoniobacteraceae participate in xylan degradation in boreal peat soils. Microorganisms, 12:2271, Nov 2024. URL: https://doi.org/10.3390/microorganisms12112271, doi:10.3390/microorganisms12112271. This article has 51 citations.

8. (muramatsu2024nutrientacquisitionstrategies pages 1-2): Matthew K. Muramatsu and Sebastian E. Winter. Nutrient acquisition strategies by gut microbes. Cell host & microbe, 32 6:863-874, Jun 2024. URL: https://doi.org/10.1016/j.chom.2024.05.011, doi:10.1016/j.chom.2024.05.011. This article has 44 citations and is from a highest quality peer-reviewed journal.

9. (stebegg2023heterotrophyamongcyanobacteria media bbf47d3e): Ronald Stebegg, Georg Schmetterer, and Annette Rompel. Heterotrophy among cyanobacteria. ACS Omega, 8:33098-33114, Sep 2023. URL: https://doi.org/10.1021/acsomega.3c02205, doi:10.1021/acsomega.3c02205. This article has 37 citations and is from a peer-reviewed journal.

10. (rakitin2024verrucomicrobiaofthe pages 9-10): Andrey L. Rakitin, Irina S. Kulichevskaya, Alexey V. Beletsky, Andrey V. Mardanov, Svetlana N. Dedysh, and Nikolai V. Ravin. Verrucomicrobia of the family chthoniobacteraceae participate in xylan degradation in boreal peat soils. Microorganisms, 12:2271, Nov 2024. URL: https://doi.org/10.3390/microorganisms12112271, doi:10.3390/microorganisms12112271. This article has 51 citations.

11. (su2024genomiccharacterizationof pages 1-3): Lei Su, Ian P. G. Marshall, Andreas P. Teske, Huiqiang Yao, and Jiangtao Li. Genomic characterization of the bacterial phylum <i>candidatus</i> effluviviacota, a cosmopolitan member of the global seep microbiome. Aug 2024. URL: https://doi.org/10.1128/mbio.00992-24, doi:10.1128/mbio.00992-24. This article has 1 citations and is from a domain leading peer-reviewed journal.

12. (su2024genomiccharacterizationof pages 10-12): Lei Su, Ian P. G. Marshall, Andreas P. Teske, Huiqiang Yao, and Jiangtao Li. Genomic characterization of the bacterial phylum <i>candidatus</i> effluviviacota, a cosmopolitan member of the global seep microbiome. Aug 2024. URL: https://doi.org/10.1128/mbio.00992-24, doi:10.1128/mbio.00992-24. This article has 1 citations and is from a domain leading peer-reviewed journal.

13. (stebegg2023heterotrophyamongcyanobacteria pages 13-14): Ronald Stebegg, Georg Schmetterer, and Annette Rompel. Heterotrophy among cyanobacteria. ACS Omega, 8:33098-33114, Sep 2023. URL: https://doi.org/10.1021/acsomega.3c02205, doi:10.1021/acsomega.3c02205. This article has 37 citations and is from a peer-reviewed journal.

14. (muramatsu2024nutrientacquisitionstrategies pages 2-4): Matthew K. Muramatsu and Sebastian E. Winter. Nutrient acquisition strategies by gut microbes. Cell host & microbe, 32 6:863-874, Jun 2024. URL: https://doi.org/10.1016/j.chom.2024.05.011, doi:10.1016/j.chom.2024.05.011. This article has 44 citations and is from a highest quality peer-reviewed journal.

15. (parsons2023suboxicdomis pages 1-2): Rachel J. Parsons, Shuting Liu, Krista Longnecker, Kevin Yongblah, Carys Johnson, Luis M. Bolaños, Jacqueline Comstock, Keri Opalk, Melissa C. Kido Soule, Rebecca Garley, Craig A. Carlson, Ben Temperton, and Nicholas R. Bates. Suboxic dom is bioavailable to surface prokaryotes in a simulated overturn of an oxygen minimum zone, devil’s hole, bermuda. Frontiers in Microbiology, Dec 2023. URL: https://doi.org/10.3389/fmicb.2023.1287477, doi:10.3389/fmicb.2023.1287477. This article has 4 citations and is from a peer-reviewed journal.

16. (parsons2023suboxicdomis pages 2-3): Rachel J. Parsons, Shuting Liu, Krista Longnecker, Kevin Yongblah, Carys Johnson, Luis M. Bolaños, Jacqueline Comstock, Keri Opalk, Melissa C. Kido Soule, Rebecca Garley, Craig A. Carlson, Ben Temperton, and Nicholas R. Bates. Suboxic dom is bioavailable to surface prokaryotes in a simulated overturn of an oxygen minimum zone, devil’s hole, bermuda. Frontiers in Microbiology, Dec 2023. URL: https://doi.org/10.3389/fmicb.2023.1287477, doi:10.3389/fmicb.2023.1287477. This article has 4 citations and is from a peer-reviewed journal.

17. (su2024genomiccharacterizationof pages 17-17): Lei Su, Ian P. G. Marshall, Andreas P. Teske, Huiqiang Yao, and Jiangtao Li. Genomic characterization of the bacterial phylum <i>candidatus</i> effluviviacota, a cosmopolitan member of the global seep microbiome. Aug 2024. URL: https://doi.org/10.1128/mbio.00992-24, doi:10.1128/mbio.00992-24. This article has 1 citations and is from a domain leading peer-reviewed journal.

18. (smorada2024bacterialdegradationof pages 1-3): Chiara M Smorada, Matthew W Sima, and Peter R Jaffé. Bacterial degradation of perfluoroalkyl acids. Aug 2024. URL: https://doi.org/10.1016/j.copbio.2024.103170, doi:10.1016/j.copbio.2024.103170. This article has 70 citations and is from a peer-reviewed journal.

19. (javourez2024ruminationsonsustainable pages 1-2): Ugo Javourez, Silvio Matassa, Siegfried E. Vlaeminck, and Willy Verstraete. Ruminations on sustainable and safe food: championing for open symbiotic cultures ensuring resource efficiency, eco‐sustainability and affordability. Microbial Biotechnology, Mar 2024. URL: https://doi.org/10.1111/1751-7915.14436, doi:10.1111/1751-7915.14436. This article has 12 citations and is from a peer-reviewed journal.