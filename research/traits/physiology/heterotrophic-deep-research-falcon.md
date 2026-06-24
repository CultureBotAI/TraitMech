---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T11:24:59.779482'
end_time: '2026-06-18T11:47:48.518868'
duration_seconds: 1368.74
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: heterotrophic
  trait_identifier: METPO:1000644
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: heterotrophic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic type in which an organism obtains carbon from organic compounds
    rather than from carbon dioxide.
  parent_traits: METPO:1000631
  synonyms: TT_heterotroph, aerobic_heterotrophy, heterotroph
  evidence_summary: 'DOI:10.1016/B978-012373944-5.00083-3: organic compounds as the
    primary sources of carbon (Encyclopedia chapter supports organic compounds as
    heterotrophic carbon sources.) | DOI:10.1021/acsomega.3c02205: organic molecules
    ... carbon source (Review table supports organic molecules as carbon sources in
    heterotrophic growth modes.) | PMID:9278503: Escherichia coli K-12 (Organism example:
    Escherichia coli K-12 (MG1655) is the canonical chemoorganoheterotrophic model
    bacterium that grows on diverse organic substrates (Blattner et al. 1997, Science,
    complete genome).)'
  causal_graph_summary: 'heterotrophic_organic_carbon_assimilation: 7 nodes, 6 edges'
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
- **Trait label:** heterotrophic
- **METPO identifier:** METPO:1000644
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains carbon from organic compounds rather than from carbon dioxide.
- **Parent traits:** METPO:1000631
- **Synonyms:** TT_heterotroph, aerobic_heterotrophy, heterotroph
- **Existing evidence:** DOI:10.1016/B978-012373944-5.00083-3: organic compounds as the primary sources of carbon (Encyclopedia chapter supports organic compounds as heterotrophic carbon sources.) | DOI:10.1021/acsomega.3c02205: organic molecules ... carbon source (Review table supports organic molecules as carbon sources in heterotrophic growth modes.) | PMID:9278503: Escherichia coli K-12 (Organism example: Escherichia coli K-12 (MG1655) is the canonical chemoorganoheterotrophic model bacterium that grows on diverse organic substrates (Blattner et al. 1997, Science, complete genome).)
- **Existing causal graph summary:** heterotrophic_organic_carbon_assimilation: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **heterotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/heterotrophic.yaml`.

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
- **Trait label:** heterotrophic
- **METPO identifier:** METPO:1000644
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains carbon from organic compounds rather than from carbon dioxide.
- **Parent traits:** METPO:1000631
- **Synonyms:** TT_heterotroph, aerobic_heterotrophy, heterotroph
- **Existing evidence:** DOI:10.1016/B978-012373944-5.00083-3: organic compounds as the primary sources of carbon (Encyclopedia chapter supports organic compounds as heterotrophic carbon sources.) | DOI:10.1021/acsomega.3c02205: organic molecules ... carbon source (Review table supports organic molecules as carbon sources in heterotrophic growth modes.) | PMID:9278503: Escherichia coli K-12 (Organism example: Escherichia coli K-12 (MG1655) is the canonical chemoorganoheterotrophic model bacterium that grows on diverse organic substrates (Blattner et al. 1997, Science, complete genome).)
- **Existing causal graph summary:** heterotrophic_organic_carbon_assimilation: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **heterotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/heterotrophic.yaml`.

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


# Microbial trait causal-graph research report: **heterotrophic** (METPO:1000644)

**Trait label:** heterotrophic  
**METPO identifier:** METPO:1000644  
**Trait category:** PHYSIOLOGY (Term kind: CLASS; mapping status: REVIEWED)  
**Definition (curation target):** trophic type in which an organism obtains carbon from organic compounds rather than from CO2.

## 1) Scope summary (trait meaning and boundaries)

> Heterotrophy is a carbon-source trait: growth depends on organic substrates that must be imported and metabolized to supply ATP, reducing power, and biomass precursors. (stebegg2023heterotrophyamongcyanobacteria pages 2-4, stebegg2023heterotrophyamongcyanobacteria media 50757e9f)
>
> This trait should be distinguished from energy-source labels; many microbes are specifically chemoorganoheterotrophs, deriving energy and biosynthetic intermediates from dietary or host organic compounds. (muramatsu2024nutrientacquisitionstrategies pages 1-2, stebegg2023heterotrophyamongcyanobacteria media 50757e9f)
>
> Heterotrophic and mixotrophic states are not interchangeable: many cyanobacteria can switch among photoautotrophic, heterotrophic, and mixotrophic modes. (lucius2024theprimarycarbon pages 1-2, stebegg2023heterotrophyamongcyanobacteria media 50757e9f)
>
> Photomixotrophy is a key boundary case and “not a true form of heterotrophy” when growth still depends partly on photosynthesis. (stebegg2023heterotrophyamongcyanobacteria pages 2-4, stebegg2023heterotrophyamongcyanobacteria media 50757e9f)
>
> Table/Figure-level summaries support curation of heterotrophy as organic-carbon use, while warning that trophic labels also vary by light, electron donor, and electron acceptor context. (stebegg2023heterotrophyamongcyanobacteria media 50757e9f, stebegg2023heterotrophyamongcyanobacteria media f3a1b93c)


*Blockquote: This blockquote summarizes the core scope of the heterotrophic trait and the most important nearby boundary cases for curation. It is useful for separating organic-carbon use from related trophic, energetic, and light-dependent classifications.*

### Scope clarifications
- **What the trait represents:** A **carbon-source phenotype/capacity**: the organism can grow with **organic carbon** as the primary carbon source for biomass, coupled to energy conservation via respiration and/or fermentation. The trait is orthogonal to whether energy comes from light vs chemicals and whether electrons come from organic vs inorganic donors; those axes are separate from the METPO carbon-source definition (e.g., *chemoorganoheterotroph* as a combined descriptor). (muramatsu2024nutrientacquisitionstrategies pages 1-2, stebegg2023heterotrophyamongcyanobacteria media 50757e9f)
- **Assay-observed interpretation:** In laboratory phenotyping, heterotrophy is typically evidenced by growth on defined organic substrates (e.g., sugars, amino acids, organic acids) under conditions where CO2 fixation is not required (e.g., darkness for phototrophs). In cyanobacteria, a minimal requirement is that “the appropriate substrate must be imported into the cell” and metabolized to generate ATP and NAD(P)H without toxic byproducts. (stebegg2023heterotrophyamongcyanobacteria pages 2-4)

### Boundary cases / nearby traits (do not conflate)
- **Mixotrophy:** simultaneous or condition-dependent combination of inorganic carbon fixation and organic substrate utilization; this is *not* the same trait as heterotrophy alone. Cyanobacterial and microalgal literature emphasizes mixotrophy as a distinct physiological state requiring regulatory control because CO2 fixation and sugar catabolism share intermediates/enzymatic capacity. (lucius2024theprimarycarbon pages 1-2, liaqat2023mixotrophiccultivationof pages 13-13)
- **Photomixotrophy / photoheterotrophy (cyanobacteria):** Stebegg et al. (2023) explicitly warn that photomixotrophy is “not a true form of heterotrophy” when growth still depends partly on photosynthesis—important for curation decisions. (stebegg2023heterotrophyamongcyanobacteria pages 2-4)
- **Energy/electron acceptor dependence:** The same heterotrophic carbon source can be coupled to **aerobic respiration (O2)**, **anaerobic respiration (e.g., fumarate)**, or **fermentation**, which should be modeled as contextual edges rather than part of the core heterotrophic trait definition. (karnachuk2024novelthermophilicgenera pages 10-11, muramatsu2024nutrientacquisitionstrategies pages 1-2)

## 2) Candidate causal-graph nodes (grounded where possible)

### A. Carbon substrates / nutrients (CHEBI where obvious)
- **Glucose** (CHEBI:17234) (lucius2024theprimarycarbon pages 2-3, liaqat2023mixotrophiccultivationof pages 12-12)
- **Fructose** (label-only; used as optimal carbon in microalgae optimization) (sim2024highthroughputoptimizationof pages 1-2)
- **Glycerol** (label-only; cyanobacterial assays and archaeal transport annotation) (stebegg2023heterotrophyamongcyanobacteria pages 2-4, zhang2024metagenomiccharacterizationof pages 6-8)
- **Acetate / acetyl-CoA entry** (label-only; acetate routing to TCA/glyoxylate in microalgae; acetate oxidation signals in deep-sea metatranscriptomics) (liaqat2023mixotrophiccultivationof pages 13-13, zhang2024metagenomiccharacterizationof pages 4-6)
- **Amino acids** (label-only; e.g., tyrosine, phenylalanine etc. in cross-feeding) (coe2024emergenceofmetabolic pages 8-9)
- **Complex polymers / oligomers** (label-only; starch, xylan, chitin, chitosan) (karnachuk2024novelthermophilicgenera pages 10-11)

### B. Transport and uptake systems
- **Glucose permease GlcP** (label-only; cyanobacteria glucose uptake) (lucius2024theprimarycarbon pages 2-3)
- **ABC transporters (sugars/amino acids/glycerol)** (label-only; Group-3.unk Thaumarchaeota genomic inference) (zhang2024metagenomiccharacterizationof pages 6-8)

### C. Central carbon metabolism modules
- **Glycolysis (Embden–Meyerhof pathway)** (label-only; present in Limnochordia; used in heterotrophic microalgae) (karnachuk2024novelthermophilicgenera pages 10-11, liaqat2023mixotrophiccultivationof pages 12-12)
- **Pentose phosphate pathway (non-oxidative stage highlighted)** (label-only) (karnachuk2024novelthermophilicgenera pages 10-11, liaqat2023mixotrophiccultivationof pages 12-12)
- **Entner–Doudoroff pathway** (label-only; predicted glycolytic route with strong regulatory impact in cyanobacteria; absent in Limnochordia) (lucius2024theprimarycarbon pages 1-2, karnachuk2024novelthermophilicgenera pages 10-11)
- **TCA cycle** (label-only; encoded and used in Limnochordia; feeds heterotrophic growth) (karnachuk2024novelthermophilicgenera pages 5-8)
- **Glyoxylate cycle / glyoxylate shunt** (label-only; complete in Group-3.unk; acetate-to-biomass rationale in microalgae) (zhang2024metagenomiccharacterizationof pages 1-2, liaqat2023mixotrophiccultivationof pages 13-13)
- **Gluconeogenesis** (label-only; present in Limnochordia and Group-3.unk) (karnachuk2024novelthermophilicgenera pages 5-8, zhang2024metagenomiccharacterizationof pages 6-8)

### D. Energy conservation / respiration / fermentation
- **Aerobic respiration using oxygen (CHEBI:15379 O2)** (karnachuk2024novelthermophilicgenera pages 10-11)
- **Anaerobic respiration using fumarate (CHEBI:18012)** (label-only; electron acceptor in Limnochordia) (karnachuk2024novelthermophilicgenera pages 5-8, karnachuk2024novelthermophilicgenera pages 11-13)
- **Fermentation / substrate-level phosphorylation** (GO process label-only) (muramatsu2024nutrientacquisitionstrategies pages 1-2)
- **Electron transport chain components / terminal oxidases** (label-only; described for Limnochordia) (karnachuk2024novelthermophilicgenera pages 5-8)
- **Rnf complex** (label-only; energy conservation in Limnochordia genomes) (karnachuk2024novelthermophilicgenera pages 5-8)

### E. Regulatory nodes for trophic switching (cyanobacteria-focused)
- **CP12 protein** (label-only; inhibits Calvin-cycle enzymes in darkness; implicated in acclimation to external glucose) (lucius2024theprimarycarbon pages 1-2)
- **PirC** (label-only; regulates phosphoglycerate mutase, a branching point for carbon allocation) (lucius2024theprimarycarbon pages 1-2)
- **CCM regulators** (NdhR, CmpR, CyAbrB2; and SbtB) (label-only; connect carbon acclimation with CO2-fixation context) (lucius2024theprimarycarbon pages 2-3)

### F. Environmental / experimental factors (ENVO label-only)
- **Light vs darkness** (switch between phototrophy and heterotrophy/mixotrophy in phototrophs) (lucius2024theprimarycarbon pages 2-3, coe2024emergenceofmetabolic pages 1-2)
- **Inhibitors used to test photoheterotrophy (DCMU)** (label-only) (stebegg2023heterotrophyamongcyanobacteria pages 2-4)
- **Nitrate availability** (modulates photoheterotrophic growth dynamics in cyanobacteria) (stebegg2023heterotrophyamongcyanobacteria pages 2-4)
- **Temperature, pH, salinity** (growth windows for heterotrophic Limnochordia isolates) (karnachuk2024novelthermophilicgenera pages 10-11)

## 3) Candidate causal edges (evidence-backed triples)

The following table is designed to be directly curatable into a TraitMech-style YAML (edges + evidence). It includes mechanistic edges for: substrate availability → transport → central metabolism → energy + biomass, plus regulatory/context edges.

| Edge (subject–predicate–object) | Evidence snippet / quote | Source (DOI, year, URL) | Notes on strength / limitations |
|---|---|---|---|
| CHEBI:17234 glucose or other organic substrates **causally enables** METPO:1000644 heterotrophic growth | “the appropriate substrate must be imported into the cell” and it must be metabolized “to produce ATP and NAD(P)H without toxic byproducts” (stebegg2023heterotrophyamongcyanobacteria pages 2-4) | 10.1021/acsomega.3c02205, 2023, https://doi.org/10.1021/acsomega.3c02205 | Strong for minimal mechanistic requirement; review focused on cyanobacteria, but principle generalizes to heterotrophy. |
| External organic carbon **distinguishes from** strict autotrophy and supports heterotrophic or mixotrophic states | “Many cyanobacterial strains can live in different trophic modes, ranging from photoautotrophic and heterotrophic to mixotrophic growth” (lucius2024theprimarycarbon pages 1-2) | 10.3389/fpls.2024.1417680, 2024, https://doi.org/10.3389/fpls.2024.1417680 | Boundary-case edge; taxonomy-specific review but useful for scope curation. |
| photomixotrophy **is not equivalent to** true heterotrophy | “photomixotrophy is described as not a true form of heterotrophy because it retains partial dependence on photosynthesis” (stebegg2023heterotrophyamongcyanobacteria pages 2-4) | 10.1021/acsomega.3c02205, 2023, https://doi.org/10.1021/acsomega.3c02205 | Important warning edge for ontology scope; boundary-case statement from review. |
| GlcP (glucose permease; label-only / transporter) **imports** CHEBI:17234 glucose into cell | “Organic uptake mechanisms include the GlcP transporter for glucose” (lucius2024theprimarycarbon pages 2-3) | 10.3389/fpls.2024.1417680, 2024, https://doi.org/10.3389/fpls.2024.1417680 | Transporter-level evidence, but from cyanobacterial model context. |
| ABC transporters for oligo/monosaccharides, amino acids, glycerol **enable uptake of** organic carbon substrates | “Genomes encode transporters predicted to import extracellular amino acids and carbohydrates… including ATP-binding cassette (ABC) transporters annotated for oligo-/monosaccharides, amino acids, and glycerol” (zhang2024metagenomiccharacterizationof pages 6-8) | 10.1186/s40168-023-01728-2, 2024, https://doi.org/10.1186/s40168-023-01728-2 | Genomics-based inference in hadal Thaumarchaeota; no direct uptake assay. Mark uncertain for general curation. |
| hexokinase / Glk **phosphorylates** CHEBI:17234 glucose to enter central metabolism | “imported glucose is phosphorylated by hexokinase and enters central metabolism” (lucius2024theprimarycarbon pages 2-3) | 10.3389/fpls.2024.1417680, 2024, https://doi.org/10.3389/fpls.2024.1417680 | Strong mechanistic edge; taxon-specific but canonical. |
| glycogen degradation (GlgX/GlgP) **produces** glucose or glucose-1-phosphate feeding heterotrophic catabolism | “glycogen synthesis (GlgC, GlgA, GlgB) and degradation (GlgX, GlgP) release glucose or G1P… G6P is central to catabolic metabolism” (lucius2024theprimarycarbon pages 2-3) | 10.3389/fpls.2024.1417680, 2024, https://doi.org/10.3389/fpls.2024.1417680 | Relevant as endogenous carbon mobilization node supporting heterotrophic/mixotrophic growth; cyanobacterial context. |
| Embden–Meyerhof glycolysis and pentose phosphate pathway **catabolize** glucose during heterotrophic growth | “Glucose is highlighted as the most commonly used sugar; its catabolism proceeds via Embden-Meyerhof (EM) glycolysis and the Pentose Phosphate (PP) pathway” (liaqat2023mixotrophiccultivationof pages 12-12) | 10.1111/raq.12700, 2023, https://doi.org/10.1111/raq.12700 | Review in microalgae, but general central-metabolism support for heterotrophic carbon assimilation. |
| Entner–Doudoroff pathway **cooperates with** glycogen breakdown / lower glycolysis in some heterotrophic-capable cyanobacteria | “The Entner-Doudoroff (ED) pathway has been predicted as a glycolytic route, which cooperates with other pathways in glycogen breakdown… low carbon flux through the ED pathway… strong regulatory impact” (lucius2024theprimarycarbon pages 1-2) | 10.3389/fpls.2024.1417680, 2024, https://doi.org/10.3389/fpls.2024.1417680 | Useful pathway node, but not universal; more regulatory than bulk-flux role in cited system. |
| Absence of ED pathway **does not preclude** heterotrophy when EMP/PP/TCA are present | “members possess most of the genes of the Embden–Meyerhof pathway and the non-oxidative stage of the pentose phosphate pathway, while the Entner–Doudoroff pathway is absent” (karnachuk2024novelthermophilicgenera pages 10-11) | 10.3389/fmicb.2024.1441865, 2024, https://doi.org/10.3389/fmicb.2024.1441865 | Negative/constraint edge from Limnochordia; supports not over-curating ED as essential. |
| TCA cycle **supports** oxidation of imported organic carbon and biomass precursor generation | “both strains encode complete glycolysis, gluconeogenesis and TCA cycle enzymes” (karnachuk2024novelthermophilicgenera pages 5-8) | 10.3389/fmicb.2024.1441865, 2024, https://doi.org/10.3389/fmicb.2024.1441865 | Good mechanistic support from genomes plus physiology in cultivated thermophiles. |
| glyoxylate cycle **supports** heterotrophic growth on C2 / carbon-saving assimilation | “complete glyoxylate cycle is a distinctive feature of this clade in supplying intermediates of anabolic pathways” (zhang2024metagenomiccharacterizationof pages 1-2) | 10.1186/s40168-023-01728-2, 2024, https://doi.org/10.1186/s40168-023-01728-2 | Genomics-based inference in Group-3.unk Thaumarchaeota; no direct cultivation validation. |
| acetate / acetyl-CoA routing through glyoxylate shunt **enhances conversion of carbon into biomass** | “Acetate can be activated to acetyl-CoA… to enter the TCA cycle or be routed into the glyoxylate cycle. The glyoxylate shunt bypasses CO2-releasing TCA steps, enhancing conversion of carbon into biomass” (liaqat2023mixotrophiccultivationof pages 13-13) | 10.1111/raq.12700, 2023, https://doi.org/10.1111/raq.12700 | Strong conceptual edge for biomass assimilation; microalgal context and acetate-specific. |
| organic substrate oxidation **couples to** aerobic respiration using CHEBI:15379 O2 as electron acceptor | “Glucose, fructose, or sucrose are used as electron donors for aerobic respiration” (karnachuk2024novelthermophilicgenera pages 10-11) | 10.3389/fmicb.2024.1441865, 2024, https://doi.org/10.3389/fmicb.2024.1441865 | Cultivation-backed; thermophilic Limnochordia-specific but strong experimental evidence. |
| fumarate respiration **enables** anaerobic heterotrophic growth on organic donors | “Both genomes encode fumarate reductase enabling anaerobic fumarate respiration” and “LNT requires fumarate to grow on some substrates” (karnachuk2024novelthermophilicgenera pages 5-8) | 10.3389/fmicb.2024.1441865, 2024, https://doi.org/10.3389/fmicb.2024.1441865 | Strong strain-specific edge with both genomic and assay support. |
| fermentation **supports** heterotrophic energy conservation under anaerobic conditions | “the colon’s anaerobic conditions favor obligate anaerobes using substrate-level phosphorylation (fermentation)” (muramatsu2024nutrientacquisitionstrategies pages 1-2) | 10.1016/j.chom.2024.05.011, 2024, https://doi.org/10.1016/j.chom.2024.05.011 | Broad ecological review; gut-specific environmental framing rather than single-microbe assay. |
| darkness plus external glucose **enables** heterotrophic growth in cyanobacteria | “External glucose permits heterotrophic growth in darkness” (lucius2024theprimarycarbon pages 2-3) | 10.3389/fpls.2024.1417680, 2024, https://doi.org/10.3389/fpls.2024.1417680 | Strong assay-context edge; cyanobacteria only. Could ground darkness as ENVO-like environmental condition label-only. |
| CP12 **inhibits** Calvin-cycle enzymes, thereby favoring heterotrophic acclimation in darkness / external glucose conditions | “CP12… downregulates the CBB cycle in darkness by inhibiting phosphoribulokinase and glyceraldehyde 3-phosphate dehydrogenase” and is implicated in “acclimation to external glucose supply” (lucius2024theprimarycarbon pages 1-2) | 10.3389/fpls.2024.1417680, 2024, https://doi.org/10.3389/fpls.2024.1417680 | Regulatory edge; specific to cyanobacterial switch between autotrophic and heterotrophic/mixotrophic fluxes. |
| PirC **regulates** phosphoglycerate mutase, redirecting carbon toward lower glycolysis | “PirC was shown to be an important regulator of phosphoglycerate mutase, which identified this enzyme as central branching point for carbon allocation… towards lower glycolysis” (lucius2024theprimarycarbon pages 1-2) | 10.3389/fpls.2024.1417680, 2024, https://doi.org/10.3389/fpls.2024.1417680 | Strong regulatory edge, but applies to cyanobacterial carbon-allocation control rather than universal heterotrophy. |
| nitrate availability **modulates** extent of photoheterotrophic growth on glycerol in Cyanothece | “grow with 10 mM glycerol plus 20 μM DCMU… stationary at 3 days without nitrate vs. continued growth to ≥6 days with nitrate” (stebegg2023heterotrophyamongcyanobacteria pages 2-4) | 10.1021/acsomega.3c02205, 2023, https://doi.org/10.1021/acsomega.3c02205 | Assay-specific and taxon-specific; valuable as environmental-factor node, but weak for general TraitMech core edge. |
| hadal sediment organic-rich conditions **select for / associate with** heterotrophic Group-3.unk Thaumarchaeota | “This novel clade… supports heterotrophic characteristics… The enrichment of organic matter in hadal sediments might be attributed to the high recruitment of… heterotrophic Thaumarchaeota” (zhang2024metagenomiccharacterizationof pages 1-2, zhang2024metagenomiccharacterizationof pages 6-8) | 10.1186/s40168-023-01728-2, 2024, https://doi.org/10.1186/s40168-023-01728-2 | Environmental association from metagenomics, not direct causality; keep as contextual/uncertain edge. |
| mixotrophic growth **can exceed** the sum of strict autotrophic and heterotrophic growth states | “mixotrophic growth can exceed the combined yields of strictly photoautotrophic and heterotrophic growth, implying a distinct trophic state” (lucius2024theprimarycarbon pages 2-3) | 10.3389/fpls.2024.1417680, 2024, https://doi.org/10.3389/fpls.2024.1417680 | Boundary-case edge showing heterotrophy should not be conflated with mixotrophy; not a core heterotrophy mechanism. |


*Table: This table compiles evidence-backed candidate subject–predicate–object edges for curating a TraitMech graph for the heterotrophic trait. It emphasizes transport, central carbon metabolism, respiration/fermentation, regulation, and boundary cases, while flagging taxon-specific and genomics-only inferences.*

## 4) Recent developments (2023–2024 focus)

### 4.1 Expanded cataloging and definitions of heterotrophy in “non-classically heterotrophic” groups
- A 2023 review synthesized evidence that many cyanobacteria can show heterotrophic growth modes (including photoheterotrophy and chemoheterotrophy) and emphasized the practical need to specify **substrate and conditions** (e.g., inhibitors like DCMU; nitrate effects) when asserting heterotrophy. (stebegg2023heterotrophyamongcyanobacteria pages 2-4)
- A 2024 review of cyanobacterial primary carbon metabolism stresses that coexistence/switching between CO2 fixation (CBB) and sugar catabolism demands tight regulation because pathways share intermediates and enzymes, elevating regulatory proteins (CP12, PirC) as mechanistic “switch” nodes for mixotrophy/heterotrophy contexts. (lucius2024theprimarycarbon pages 1-2)

### 4.2 Genome-resolved discovery of deep-sea archaeal heterotrophs
- A 2024 Microbiome study described a novel non-ammonia-oxidizing Thaumarchaeota clade (“Group-3.unk”) inferred to be heterotrophic, with ABC transporters for uptake of amino acids/carbohydrates/glycerol and a complete glyoxylate cycle as a distinctive feature supplying anabolic intermediates—highlighting heterotrophy in archaeal lineages in hadal sediments. (zhang2024metagenomiccharacterizationof pages 1-2, zhang2024metagenomiccharacterizationof pages 6-8)

### 4.3 Cultivation evidence for versatile heterotrophic thermophiles coupling organic carbon to different electron acceptors
- A 2024 Frontiers in Microbiology paper isolated thermophilic Limnochordia (Geochorda/Carboxydochorda) that are facultatively anaerobic and **chemoorganoheterotrophic**, using sugars and polymers as donors, with **O2** as acceptor aerobically and **fumarate** anaerobically; ED pathway absent while EMP/PP/TCA present. (karnachuk2024novelthermophilicgenera pages 10-11, karnachuk2024novelthermophilicgenera pages 5-8)

### 4.4 Interaction-level heterotrophy: cross-feeding and dark survival
- Coe et al. (2024) showed Prochlorococcus dark survival can be promoted by **metabolic coupling to the heterotroph Alteromonas**, where Prochlorococcus shifts toward respiration and Alteromonas shifts toward using more reduced substrates/organic acids and degrades compounds consistent with Prochlorococcus exudates (amino acids, purines, benzoate), suggesting cross-feeding as an ecological mechanism supporting persistence in darkness. (coe2024emergenceofmetabolic pages 1-2, coe2024emergenceofmetabolic pages 8-9)

## 5) Current applications and real-world implementations

### 5.1 High-throughput optimization of heterotrophic/mixotrophic production (microalgae)
- Sim et al. (2024) demonstrate a microplate high-throughput workflow to optimize organic-carbon provisioning for production goals in microalgae: from 71 substrates screened, 4 were utilizable; **30 g/L fructose at 27°C** produced **13.05 ± 0.40 g/L biomass** and **97.98 ± 7.33 mg/L arachidonic acid**, improving biomass 9.6-fold and ARA 5.3-fold versus pre-optimization conditions—illustrating a direct implementation pathway from trait (heterotrophic substrate use) to bioprocess. (sim2024highthroughputoptimizationof pages 1-2)

### 5.2 Environmental/ecological modeling implications
- Gut microbiome reviews characterize many commensals as chemoorganoheterotrophs and describe how **oxygen availability** shifts feasible energy conservation modes (fermentation vs respiration), providing mechanistic context that can be incorporated into trait graphs when modeling heterotrophic behavior in host-associated habitats. (muramatsu2024nutrientacquisitionstrategies pages 1-2)

## 6) Statistics and data points from recent studies (2023–2024)

- **Prochlorococcus dark survival:** axenic Prochlorococcus “cannot survive more than a day in the dark,” but with Alteromonas can survive “up to **11 days** of darkness”; axenic cultures can survive up to **3 days** if amended with pyruvate and glucose. (coe2024emergenceofmetabolic pages 1-2)
- **Microalgae bioprocess optimization:** **13.05 ± 0.40 g/L** biomass and **97.98 ± 7.33 mg/L** ARA at **30 g/L** fructose and **27°C**; **9.6-fold** biomass and **5.3-fold** ARA increases vs pre-optimization. (sim2024highthroughputoptimizationof pages 1-2)
- **Cyanobacterial photoheterotrophy condition dependence:** Cyanothece strains grew with **10 mM glycerol + 20 μM DCMU**, with nitrate affecting growth duration (stationary at 3 days without nitrate vs continued growth to ≥6 days with nitrate). (stebegg2023heterotrophyamongcyanobacteria pages 2-4)

## 7) Expert analysis / curation guidance (what to curate vs caution)

### Strong, broadly reusable edges to curate as “core” heterotrophy
- Organic substrate import → entry to central metabolism → ATP/NAD(P)H generation → biomass synthesis as the mechanistic backbone (transport + central carbon metabolism + energy conservation). (stebegg2023heterotrophyamongcyanobacteria pages 2-4, liaqat2023mixotrophiccultivationof pages 12-12)
- Modeling heterotrophy should treat **electron acceptor** (O2 vs fumarate vs fermentation) as **contextual** rather than definitional. (karnachuk2024novelthermophilicgenera pages 10-11, muramatsu2024nutrientacquisitionstrategies pages 1-2)

### Edges to include but tag as context- or taxon-specific
- Cyanobacteria-specific transport/regulatory nodes (GlcP, CP12, PirC) are valuable for phototrophic taxa but should not be asserted as universal heterotrophy requirements. (lucius2024theprimarycarbon pages 2-3, lucius2024theprimarycarbon pages 1-2)
- Deep-sea Thaumarchaeota “Group-3.unk” heterotrophy is inferred primarily from genomics/transcriptomics; edges (ABC transporters, glyoxylate cycle enabling heterotrophy) should be tagged as **inferred** until validated by cultivation/physiology. (zhang2024metagenomiccharacterizationof pages 1-2, zhang2024metagenomiccharacterizationof pages 6-8)

### Warnings (do not curate as unconditional)
- Do not curate “ED pathway is required for heterotrophy”: Limnochordia heterotrophs explicitly lack ED while remaining chemoorganoheterotrophic, so ED is optional. (karnachuk2024novelthermophilicgenera pages 10-11)
- Do not conflate “photomixotrophy” with “heterotrophic”: treat photomixotrophy as a boundary-case state requiring explicit evidence that growth is not photosynthesis-dependent. (stebegg2023heterotrophyamongcyanobacteria pages 2-4)

## 8) DOI-first bibliography (with dates and URLs)

1. **Stebegg R, Schmetterer G, Rompel A.** *Heterotrophy among Cyanobacteria.* **ACS Omega** (Sep 2023). DOI: **10.1021/acsomega.3c02205**. URL: https://doi.org/10.1021/acsomega.3c02205 (stebegg2023heterotrophyamongcyanobacteria pages 2-4, stebegg2023heterotrophyamongcyanobacteria media 50757e9f, stebegg2023heterotrophyamongcyanobacteria media f3a1b93c)
2. **Lucius S, Hagemann M.** *The primary carbon metabolism in cyanobacteria and its regulation.* **Frontiers in Plant Science** (Jul 2024). DOI: **10.3389/fpls.2024.1417680**. URL: https://doi.org/10.3389/fpls.2024.1417680 (lucius2024theprimarycarbon pages 1-2, lucius2024theprimarycarbon pages 2-3)
3. **Muramatsu MK, Winter SE.** *Nutrient acquisition strategies by gut microbes.* **Cell Host & Microbe** (Jun 2024). DOI: **10.1016/j.chom.2024.05.011**. URL: https://doi.org/10.1016/j.chom.2024.05.011 (muramatsu2024nutrientacquisitionstrategies pages 1-2)
4. **Zhang R-Y et al.** *Metagenomic characterization of a novel non-ammonia-oxidizing Thaumarchaeota from hadal sediment.* **Microbiome** (Jan 2024). DOI: **10.1186/s40168-023-01728-2**. URL: https://doi.org/10.1186/s40168-023-01728-2 (zhang2024metagenomiccharacterizationof pages 1-2, zhang2024metagenomiccharacterizationof pages 6-8, zhang2024metagenomiccharacterizationof pages 4-6)
5. **Karnachuk OV et al.** *Novel thermophilic genera Geochorda gen. nov. and Carboxydochorda gen. nov. … (Limnochordia).* **Frontiers in Microbiology** (Sep 2024). DOI: **10.3389/fmicb.2024.1441865**. URL: https://doi.org/10.3389/fmicb.2024.1441865 (karnachuk2024novelthermophilicgenera pages 10-11, karnachuk2024novelthermophilicgenera pages 5-8, karnachuk2024novelthermophilicgenera pages 11-13)
6. **Coe A et al.** *Emergence of metabolic coupling to the heterotroph Alteromonas promotes dark survival in Prochlorococcus.* **ISME Communications** (Jan 2024). DOI: **10.1093/ismeco/ycae131**. URL: https://doi.org/10.1093/ismeco/ycae131 (coe2024emergenceofmetabolic pages 1-2, coe2024emergenceofmetabolic pages 8-9)
7. **Liaqat F et al.** *Mixotrophic cultivation of microalgae for carotenoid production.* **Reviews in Aquaculture** (May 2023). DOI: **10.1111/raq.12700**. URL: https://doi.org/10.1111/raq.12700 (liaqat2023mixotrophiccultivationof pages 13-13, liaqat2023mixotrophiccultivationof pages 12-12)
8. **Sim EJ et al.** *High-throughput optimization of organic carbon provision strategies enables enhanced arachidonic acid production in novel microalgae.* **Microbial Cell Factories** (Oct 2024). DOI: **10.1186/s12934-024-02560-5**. URL: https://doi.org/10.1186/s12934-024-02560-5 (sim2024highthroughputoptimizationof pages 1-2, sim2024highthroughputoptimizationof pages 9-11)

---

## Appendix: Visual evidence from literature
- **Stebegg et al. 2023 Figure 1**: schematic of uptake/metabolization of organic molecules in cyanobacteria (supporting transporter/enzyme node inclusion). (stebegg2023heterotrophyamongcyanobacteria media f3a1b93c)
- **Stebegg et al. 2023 Table 1**: trophic mode definitions (supports boundary-case distinctions for curation). (stebegg2023heterotrophyamongcyanobacteria media 50757e9f)


References

1. (stebegg2023heterotrophyamongcyanobacteria pages 2-4): Ronald Stebegg, Georg Schmetterer, and Annette Rompel. Heterotrophy among cyanobacteria. ACS Omega, 8:33098-33114, Sep 2023. URL: https://doi.org/10.1021/acsomega.3c02205, doi:10.1021/acsomega.3c02205. This article has 37 citations and is from a peer-reviewed journal.

2. (stebegg2023heterotrophyamongcyanobacteria media 50757e9f): Ronald Stebegg, Georg Schmetterer, and Annette Rompel. Heterotrophy among cyanobacteria. ACS Omega, 8:33098-33114, Sep 2023. URL: https://doi.org/10.1021/acsomega.3c02205, doi:10.1021/acsomega.3c02205. This article has 37 citations and is from a peer-reviewed journal.

3. (muramatsu2024nutrientacquisitionstrategies pages 1-2): Matthew K. Muramatsu and Sebastian E. Winter. Nutrient acquisition strategies by gut microbes. Cell host & microbe, 32 6:863-874, Jun 2024. URL: https://doi.org/10.1016/j.chom.2024.05.011, doi:10.1016/j.chom.2024.05.011. This article has 44 citations and is from a highest quality peer-reviewed journal.

4. (lucius2024theprimarycarbon pages 1-2): Stefan Lucius and Martin Hagemann. The primary carbon metabolism in cyanobacteria and its regulation. Frontiers in Plant Science, Jul 2024. URL: https://doi.org/10.3389/fpls.2024.1417680, doi:10.3389/fpls.2024.1417680. This article has 88 citations.

5. (stebegg2023heterotrophyamongcyanobacteria media f3a1b93c): Ronald Stebegg, Georg Schmetterer, and Annette Rompel. Heterotrophy among cyanobacteria. ACS Omega, 8:33098-33114, Sep 2023. URL: https://doi.org/10.1021/acsomega.3c02205, doi:10.1021/acsomega.3c02205. This article has 37 citations and is from a peer-reviewed journal.

6. (liaqat2023mixotrophiccultivationof pages 13-13): Fakhra Liaqat, Mahammed Ilyas Khazi, Ali Bahadar, Lu He, Ayesha Aslam, Rabia Liaquat, Spiros N. Agathos, and Jian Li. Mixotrophic cultivation of microalgae for carotenoid production. Reviews in Aquaculture, 15:35-61, May 2023. URL: https://doi.org/10.1111/raq.12700, doi:10.1111/raq.12700. This article has 60 citations and is from a domain leading peer-reviewed journal.

7. (karnachuk2024novelthermophilicgenera pages 10-11): Olga V. Karnachuk, Anastasia P. Lukina, Marat R. Avakyan, Vitaly V. Kadnikov, Shahjahon Begmatov, Alexey V. Beletsky, Ksenia G. Vlasova, Andrei A. Novikov, Viktoria A. Shcherbakova, Andrey V. Mardanov, and Nikolai V. Ravin. Novel thermophilic genera geochorda gen. nov. and carboxydochorda gen. nov. from the deep terrestrial subsurface reveal the ecophysiological diversity in the class limnochordia. Frontiers in Microbiology, Sep 2024. URL: https://doi.org/10.3389/fmicb.2024.1441865, doi:10.3389/fmicb.2024.1441865. This article has 16 citations and is from a peer-reviewed journal.

8. (lucius2024theprimarycarbon pages 2-3): Stefan Lucius and Martin Hagemann. The primary carbon metabolism in cyanobacteria and its regulation. Frontiers in Plant Science, Jul 2024. URL: https://doi.org/10.3389/fpls.2024.1417680, doi:10.3389/fpls.2024.1417680. This article has 88 citations.

9. (liaqat2023mixotrophiccultivationof pages 12-12): Fakhra Liaqat, Mahammed Ilyas Khazi, Ali Bahadar, Lu He, Ayesha Aslam, Rabia Liaquat, Spiros N. Agathos, and Jian Li. Mixotrophic cultivation of microalgae for carotenoid production. Reviews in Aquaculture, 15:35-61, May 2023. URL: https://doi.org/10.1111/raq.12700, doi:10.1111/raq.12700. This article has 60 citations and is from a domain leading peer-reviewed journal.

10. (sim2024highthroughputoptimizationof pages 1-2): Eun Jeong Sim, Yu Rim Lee, Su-Bin Park, Geonwoo Kim, Bum-Soo Shin, Jin-Ho Yun, Hong Il Choi, Dong-Yun Choi, Dae-Hyun Cho, Hee-Sik Kim, and Yong Jae Lee. High-throughput optimization of organic carbon provision strategies enables enhanced arachidonic acid production in novel microalgae. Microbial Cell Factories, Oct 2024. URL: https://doi.org/10.1186/s12934-024-02560-5, doi:10.1186/s12934-024-02560-5. This article has 2 citations and is from a peer-reviewed journal.

11. (zhang2024metagenomiccharacterizationof pages 6-8): Ru-Yi Zhang, Yan-Ren Wang, Ru-Long Liu, Sung-Keun Rhee, Guo-Ping Zhao, and Zhe-Xue Quan. Metagenomic characterization of a novel non-ammonia-oxidizing thaumarchaeota from hadal sediment. Microbiome, Jan 2024. URL: https://doi.org/10.1186/s40168-023-01728-2, doi:10.1186/s40168-023-01728-2. This article has 24 citations and is from a highest quality peer-reviewed journal.

12. (zhang2024metagenomiccharacterizationof pages 4-6): Ru-Yi Zhang, Yan-Ren Wang, Ru-Long Liu, Sung-Keun Rhee, Guo-Ping Zhao, and Zhe-Xue Quan. Metagenomic characterization of a novel non-ammonia-oxidizing thaumarchaeota from hadal sediment. Microbiome, Jan 2024. URL: https://doi.org/10.1186/s40168-023-01728-2, doi:10.1186/s40168-023-01728-2. This article has 24 citations and is from a highest quality peer-reviewed journal.

13. (coe2024emergenceofmetabolic pages 8-9): Allison Coe, Rogier Braakman, Steven J Biller, Aldo Arellano, Christina Bliem, Nhi N Vo, Konnor von Emster, Elaina Thomas, Michelle DeMers, Claudia Steglich, Jef Huisman, and Sallie W Chisholm. Emergence of metabolic coupling to the heterotroph alteromonas promotes dark survival in prochlorococcus. ISME Communications, Jan 2024. URL: https://doi.org/10.1093/ismeco/ycae131, doi:10.1093/ismeco/ycae131. This article has 7 citations and is from a peer-reviewed journal.

14. (karnachuk2024novelthermophilicgenera pages 5-8): Olga V. Karnachuk, Anastasia P. Lukina, Marat R. Avakyan, Vitaly V. Kadnikov, Shahjahon Begmatov, Alexey V. Beletsky, Ksenia G. Vlasova, Andrei A. Novikov, Viktoria A. Shcherbakova, Andrey V. Mardanov, and Nikolai V. Ravin. Novel thermophilic genera geochorda gen. nov. and carboxydochorda gen. nov. from the deep terrestrial subsurface reveal the ecophysiological diversity in the class limnochordia. Frontiers in Microbiology, Sep 2024. URL: https://doi.org/10.3389/fmicb.2024.1441865, doi:10.3389/fmicb.2024.1441865. This article has 16 citations and is from a peer-reviewed journal.

15. (zhang2024metagenomiccharacterizationof pages 1-2): Ru-Yi Zhang, Yan-Ren Wang, Ru-Long Liu, Sung-Keun Rhee, Guo-Ping Zhao, and Zhe-Xue Quan. Metagenomic characterization of a novel non-ammonia-oxidizing thaumarchaeota from hadal sediment. Microbiome, Jan 2024. URL: https://doi.org/10.1186/s40168-023-01728-2, doi:10.1186/s40168-023-01728-2. This article has 24 citations and is from a highest quality peer-reviewed journal.

16. (karnachuk2024novelthermophilicgenera pages 11-13): Olga V. Karnachuk, Anastasia P. Lukina, Marat R. Avakyan, Vitaly V. Kadnikov, Shahjahon Begmatov, Alexey V. Beletsky, Ksenia G. Vlasova, Andrei A. Novikov, Viktoria A. Shcherbakova, Andrey V. Mardanov, and Nikolai V. Ravin. Novel thermophilic genera geochorda gen. nov. and carboxydochorda gen. nov. from the deep terrestrial subsurface reveal the ecophysiological diversity in the class limnochordia. Frontiers in Microbiology, Sep 2024. URL: https://doi.org/10.3389/fmicb.2024.1441865, doi:10.3389/fmicb.2024.1441865. This article has 16 citations and is from a peer-reviewed journal.

17. (coe2024emergenceofmetabolic pages 1-2): Allison Coe, Rogier Braakman, Steven J Biller, Aldo Arellano, Christina Bliem, Nhi N Vo, Konnor von Emster, Elaina Thomas, Michelle DeMers, Claudia Steglich, Jef Huisman, and Sallie W Chisholm. Emergence of metabolic coupling to the heterotroph alteromonas promotes dark survival in prochlorococcus. ISME Communications, Jan 2024. URL: https://doi.org/10.1093/ismeco/ycae131, doi:10.1093/ismeco/ycae131. This article has 7 citations and is from a peer-reviewed journal.

18. (sim2024highthroughputoptimizationof pages 9-11): Eun Jeong Sim, Yu Rim Lee, Su-Bin Park, Geonwoo Kim, Bum-Soo Shin, Jin-Ho Yun, Hong Il Choi, Dong-Yun Choi, Dae-Hyun Cho, Hee-Sik Kim, and Yong Jae Lee. High-throughput optimization of organic carbon provision strategies enables enhanced arachidonic acid production in novel microalgae. Microbial Cell Factories, Oct 2024. URL: https://doi.org/10.1186/s12934-024-02560-5, doi:10.1186/s12934-024-02560-5. This article has 2 citations and is from a peer-reviewed journal.