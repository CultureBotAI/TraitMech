---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T00:34:12.714633'
end_time: '2026-06-18T00:48:19.144669'
duration_seconds: 846.43
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: pH range
  trait_identifier: METPO:1000332
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: ph_range
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pH phenotype with numerical limits that bounds the minimum and maximum
    external pH supporting growth of an organism.
  parent_traits: METPO:1000531, METPO:1000535
  synonyms: ''
  evidence_summary: 'DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review
    supports the bounded external-pH span over which cytoplasmic pH homeostasis sustains
    growth as the basis of the pH-range phenotype.) | DOI:10.1016/j.tim.2007.02.005:
    highly impermeable cell membranes (pH-homeostasis review supports envelope-based
    proton barriers as the mechanism extending growth into acidic and alkaline extremes.)'
  causal_graph_summary: 'ph_range_bounded_homeostasis: 5 nodes, 4 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 43
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH range
- **METPO identifier:** METPO:1000332
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH phenotype with numerical limits that bounds the minimum and maximum external pH supporting growth of an organism.
- **Parent traits:** METPO:1000531, METPO:1000535
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review supports the bounded external-pH span over which cytoplasmic pH homeostasis sustains growth as the basis of the pH-range phenotype.) | DOI:10.1016/j.tim.2007.02.005: highly impermeable cell membranes (pH-homeostasis review supports envelope-based proton barriers as the mechanism extending growth into acidic and alkaline extremes.)
- **Existing causal graph summary:** ph_range_bounded_homeostasis: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **pH range** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_range.yaml`.

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
- **Trait label:** pH range
- **METPO identifier:** METPO:1000332
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH phenotype with numerical limits that bounds the minimum and maximum external pH supporting growth of an organism.
- **Parent traits:** METPO:1000531, METPO:1000535
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/nrmicro2549: pH homeostasis (pH-homeostasis review supports the bounded external-pH span over which cytoplasmic pH homeostasis sustains growth as the basis of the pH-range phenotype.) | DOI:10.1016/j.tim.2007.02.005: highly impermeable cell membranes (pH-homeostasis review supports envelope-based proton barriers as the mechanism extending growth into acidic and alkaline extremes.)
- **Existing causal graph summary:** ph_range_bounded_homeostasis: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **pH range** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_range.yaml`.

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


# Research Report: Microbial Trait “pH range” (METPO:1000332)

## Scope summary (what the trait represents)
The METPO trait **pH range** (METPO:1000332) represents the **bounded interval of external pH values (minimum–maximum) that supports microbial growth**, not merely short-term survival. A key boundary condition is that microbes may **survive** at pH values outside their growth range and then resume growth when returned to permissive pH; therefore, “pH range” should be curated as a **growth phenotype** rather than a viability phenotype. (krulwich2011molecularaspectsof pages 1-3)

### Distinguish from nearby traits
- **pH optimum / pH preference**: A single (or narrow) value where growth rate or abundance is maximal. In field datasets, “pH preference” has been operationalized as the **pH where relative abundance is highest** (a realized-niche measure that mixes physiology and ecological constraints), which is related to but not identical to lab-measured growth pH range. (ramoneda2023buildingagenomebased pages 6-7, ramoneda2023buildingagenomebased pages 1-2)
- **Acid tolerance / alkali tolerance**: Often refers to **stress response capacity** (survival, maintenance, or recovery under transient exposure) and may not imply sustained growth.
- **pH homeostasis**: A mechanistic capacity that underlies and constrains pH range; pH range is a phenotype emerging from the ability (and energy cost) of pH homeostasis systems. (krulwich2011molecularaspectsof pages 1-3, krulwich2011molecularaspectsof pages 3-5)

### Quantitative current understanding (representative values)
- Neutralophiles often grow across roughly **pHout ~5.5–9.0** while maintaining cytoplasmic pH near neutral. (krulwich2011molecularaspectsof pages 1-3)
- Extremes described in the pH-homeostasis synthesis literature include **acidophile growth at pH 1–3** and **alkaliphile growth at pH 10–13**. (krulwich2011molecularaspectsof pages 3-5)
- A concrete acidophile example: *Methylacidiphilum* sp. RTK17.1 grows across **external pH 1.5–3.0** while maintaining intracellular pH **~6.52 ± 0.04**. (carere2021growthonformic pages 1-2)

## Key concepts and mechanistic definitions (curation-relevant)
### The mechanistic “core” of the pH-range trait
Across taxa, pH range is fundamentally constrained by the ability to maintain a **cytoplasmic pH compatible with macromolecular function**, supported by **proton motive force (PMF)** architecture and active ion transport. The PMF is commonly expressed as **PMF (mV) = Δψ − 59ΔpH** and changes in ΔpH/Δψ usage occur across acidophiles, neutralophiles, and alkaliphiles. (krulwich2011molecularaspectsof pages 1-3, krulwich2011molecularaspectsof media 07c1b8d2)

**Figure evidence (visual):** The Krulwich et al. Box 1 figure summarizes how ΔpH and Δψ contribute differently to PMF and cytoplasmic pH patterns across acidophiles/neutralophiles/alkaliphiles, directly aligning with the bounded-growth concept of pH range. (krulwich2011molecularaspectsof media 07c1b8d2)

## Recent developments and latest research (prioritizing 2023–2024)
### 1) Genome-based inference of pH preference (2023)
Ramoneda et al. (Science Advances, **2023-04**, DOI:10.1126/sciadv.adf8998) inferred bacterial **pH preference** from distributions across natural pH gradients and linked those preferences to genomes, identifying sets of genes reproducibly associated with preference across habitats. They report a gradient-boosted model using **56 gene types** (presence/absence) with held-out performance (e.g., **MAE ~0.63** and average **R² ~0.80** across datasets; independent validation R² values lower depending on dataset), while also noting that predictions are limited by sparse data outside approximately pH 4–9. (ramoneda2023buildingagenomebased pages 6-7)

**Curation implication:** These are strong candidates for **comparative genomic prioritization** of nodes/edges but should be curated cautiously as **associations with realized pH preference**, not automatically as mechanistic determinants of growth pH range. (ramoneda2023buildingagenomebased pages 6-7, ramoneda2023buildingagenomebased pages 1-2)

### 2) Expanded ecophysiology of methanotroph pH ecotypes (2023)
Yao et al. (Frontiers in Microbiology, **2023-01**, DOI:10.3389/fmicb.2022.1034164) compiled growth pH optima and ranges across methanotroph clades, including extremes (e.g., acidophilic Verrucomicrobia with optima near ~2 and ranges reported down to ~0.5–0.8 and up to ~6; alkaliphilic isolates with optima ~8.5–9.5 and ranges extending to ~10.5–11). (yao2023howmethanotrophsrespond pages 4-5)

They also synthesize mechanism hypotheses linking pH ecotypes to:
- **Membrane proton permeability control** (e.g., acidophiles enriched for saturated fatty acids). (yao2023howmethanotrophsrespond pages 5-7)
- **Surface structures (S-layer) and phospholipid composition** that may increase proton accumulation at alkaline pH. (yao2023howmethanotrophsrespond pages 5-7, yao2023howmethanotrophsrespond pages 7-8)
- **Energy economics**: associations between pH conditions/PMF constraints and carbon fixation pathway choice (CBB vs RuMP vs serine pathway). (yao2023howmethanotrophsrespond pages 7-8)

### 3) Low-pH exploitation across human, industrial, and planetary health contexts (2024)
Atasoy et al. (FEMS Microbiology Reviews, **2024-11**, DOI:10.1093/femsre/fuad062) provides a 2024 state-of-the-art synthesis of **how low-pH microbial activity is exploited** in food systems, probiotics, waste valorization, and infection control. It includes quantitative process examples where pH is manipulated to shift outcomes, such as:
- Complete suppression of methanogenesis at **pH 4.0** (vs pH 7.0), and increased VFA production under acidic conditions (e.g., **4.4-fold** at **pH 5.0** vs pH 7). (atasoy2024exploitationofmicrobial pages 7-8)
- Probiotic selection/testing conditions including survival assays at **pH 2.5** (stomach mimic). (atasoy2024exploitationofmicrobial pages 5-6)
- Food/agricultural wastes frequently having low pH (e.g., **<4.0**). (atasoy2024exploitationofmicrobial pages 5-6)
These data provide real-world context for why the pH-range phenotype matters in practice. (atasoy2024exploitationofmicrobial pages 5-6, atasoy2024exploitationofmicrobial pages 7-8)

### 4) Community/biofilm modulation of pH stress adaptability (2024)
Jiang et al. (Applied and Environmental Microbiology, **2024-07**, DOI:10.1128/aem.00569-24) reports that exogenous putrescine can modulate biofilm community pH stress adaptability, including links to increased membrane permeability, stimulation of glutamate-based acid resistance/GABA metabolism, and increased ATPase expression to support H+ transport under acidic conditions. (jiang2024exogenousputrescineplays pages 1-2)

**Curation implication:** Valuable for **assay/ecosystem nodes** (biofilm state; exogenous polyamines; community shifts) but likely too context-specific for universal organism-level pH-range mechanisms. (jiang2024exogenousputrescineplays pages 1-2)

## Current applications and real-world implementations tied to pH range
1. **Food fermentation and preservation:** Manipulating pH (often by organic acids) shapes microbial growth windows for safety and shelf-life; low-pH environments select for acid-tolerant taxa and suppress pathogens. (atasoy2024exploitationofmicrobial pages 2-3, atasoy2024exploitationofmicrobial pages 1-2)
2. **Probiotics:** Screening for survival in stomach-like conditions (e.g., pH 2.5) and performance in acidic foods directly uses acid-side pH range/tolerance. (atasoy2024exploitationofmicrobial pages 5-6)
3. **Waste valorization and anaerobic processes:** Operating at acidic pH can shift fermentations toward VFAs and away from methanogenesis, affecting yields, downstream processing, and costs (including base addition costs). (atasoy2024exploitationofmicrobial pages 7-8)
4. **Infection control / antimicrobial efficacy:** Acidic microenvironments (biofilms, wound sites, urinary tract) can influence antimicrobial activity; the review highlights pH-dependent antibiotic performance windows (e.g., increased activity at pH 5–6 for some agents). (atasoy2024exploitationofmicrobial pages 17-18)

## Expert synthesis and analysis (authoritative sources)
### Foundational mechanistic synthesis (Krulwich, Sachs, Padan 2011)
Krulwich et al. (Nature Reviews Microbiology, **2011-05**, DOI:10.1038/nrmicro2549) provide a highly cited synthesis connecting the growth-supporting external pH span to:
- **PMF partitioning into ΔpH and Δψ** and how these components reverse or compensate under extremes (acidophile vs alkaliphile regimes). (krulwich2011molecularaspectsof pages 3-5, krulwich2011molecularaspectsof media 07c1b8d2)
- **Ion transport modules** (Na+/H+ antiport; K+/H+ antiport; electrogenic stoichiometries like NhaA) supporting pH homeostasis. (krulwich2011molecularaspectsof pages 5-6)
- **Structural/functional adaptations of F1F0-ATP synthase** that support function at high pH, with reported stronger defects of motif mutations at high pH vs neutral pH, indicating causal relevance to alkaline-side growth. (krulwich2011molecularaspectsof pages 12-14)
- **Trade-offs**: constitutive expression of pH-homeostasis machinery can impose energetic costs affecting growth outside the preferred range. (krulwich2011molecularaspectsof pages 3-5)

### Mechanistic anchor for alkaliphile pH range: Mrp antiporters
Ito et al. (Frontiers in Microbiology, **2017-11**, DOI:10.3389/fmicb.2017.02325) and Krulwich et al. (2011) converge on the Mrp system as a key determinant for alkaline-side pH homeostasis:
- Mrp was discovered via complementation of an **alkaline-sensitive mutant** and is described as contributing to **pH homeostasis in alkaline environments**; canonically **mrpA–G are required** for activity (with noted exceptions). (ito2017mrpantiportershave pages 1-2)
- Genetic evidence in alkaliphilic Bacillus indicates a **point mutation in mrpA** can cause loss of alkaline pH homeostasis and loss of Na+/H+ antiport activity. (krulwich2011molecularaspectsof pages 12-14)
These are among the strongest gene→mechanism→phenotype links available in the current evidence set.

## Relevant statistics and data points (recent studies emphasized)
- **Methanotroph growth pH ranges**: compiled ranges spanning extreme acidity and alkalinity across taxa, including reported ranges down to ~0.5–0.8 and up to ~10.5–11 in different groups. (yao2023howmethanotrophsrespond pages 4-5)
- **Acidophile intracellular pH maintenance**: *Methylacidiphilum* RTK17.1 intracellular pH **6.52 ± 0.04** across external pH **1.5–3.0**. (carere2021growthonformic pages 1-2)
- **pH preference prediction from genomes (2023)**: ML model using 56 gene types; held-out MAE ~0.63 and average R² ~0.80 across datasets (performance varies by external validation). (ramoneda2023buildingagenomebased pages 6-7)
- **Process-level pH impacts in applied systems (2024)**: methanogenesis suppression at **pH 4.0**, VFA production increases at **pH 5.0**, and reported lactic acid production metrics at **pH ~3.11** in one cited process context. (atasoy2024exploitationofmicrobial pages 7-8)

## Candidate causal-graph nodes (grouped by type)
The following table is a curation-oriented node inventory with suggested ontology grounding where possible.

| Node label | Type | Suggested grounding CURIE(s) if known | Rationale/role in pH range (1 sentence) | Key supporting source pqac IDs |
|---|---|---|---|---|
| pH range | Trait/Process | METPO:1000332 | The trait is the minimum-to-maximum external pH interval that still supports microbial growth, distinct from mere survival outside that interval. | (krulwich2011molecularaspectsof pages 1-3, krulwich2011molecularaspectsof pages 3-5) |
| pH homeostasis | Trait/Process | GO:0010447 | Maintenance of intracellular pH within a viable window is the core physiological basis that bounds growth across external pH values. | (krulwich2011molecularaspectsof pages 1-3, lund2020understandinghowmicroorganisms pages 3-5) |
| cytoplasmic pH | Trait/Process |  | Cytoplasmic pH is the immediate physiological variable that must remain compatible with protein function for growth across acidic or alkaline environments. | (krulwich2011molecularaspectsof pages 1-3, carere2021growthonformic pages 1-2) |
| proton motive force (PMF) | Trait/Process | GO:0015995 | PMF integrates membrane potential and transmembrane proton gradient, providing the energetic framework for pH homeostasis across the growth-supporting pH span. | (krulwich2011molecularaspectsof pages 1-3, krulwich2011molecularaspectsof media 07c1b8d2) |
| transmembrane pH gradient (ΔpH) | Trait/Process | GO:1902600 | ΔpH is a principal PMF component whose magnitude and orientation shift with environmental pH and constrain growth range limits. | (krulwich2011molecularaspectsof pages 1-3, krulwich2011molecularaspectsof pages 3-5) |
| membrane potential (Δψ) | Trait/Process | GO:1902600 | Δψ compensates for extreme acid or alkaline conditions and helps preserve usable PMF when ΔpH is unfavorable. | (krulwich2011molecularaspectsof pages 1-3, krulwich2011molecularaspectsof pages 3-5) |
| alkaline pH homeostasis | Trait/Process | GO:0090333 | Specialized alkaline pH homeostasis mechanisms extend the upper bound of pH range in alkaliphiles and alkali-tolerant taxa. | (krulwich2011molecularaspectsof pages 12-14) |
| acid resistance / acid stress response | Trait/Process | GO:0009268 | Acid-response systems reduce intracellular acidification and can extend the low-pH side of the growth range. | (lund2020understandinghowmicroorganisms pages 3-5, jiang2024exogenousputrescineplays pages 1-2) |
| amino acid decarboxylation | Pathway/module | GO:0004068 | Proton-consuming amino acid decarboxylation is a recurring acid-resistance module that helps maintain near-neutral cytosolic pH. | (lund2020understandinghowmicroorganisms pages 3-5, atasoy2024exploitationofmicrobial pages 3-4) |
| glutamate decarboxylase / GABA system | Pathway/module | EC:4.1.1.15, CHEBI:16865 | The GAD/GABA pathway consumes intracellular protons and is a well-supported mechanism for acid-side pH homeostasis. | (krulwich2011molecularaspectsof pages 15-17, jiang2024exogenousputrescineplays pages 1-2) |
| buffering compound production | Pathway/module |  | Production of buffering compounds can alkalinize the local microenvironment and broaden low-pH growth capacity. | (lund2020understandinghowmicroorganisms pages 3-5) |
| potassium uptake | Transporter | GO:0015079 | K+ uptake can help generate an internal positive potential in acidophiles and thereby reduce proton influx pressure. | (yao2023howmethanotrophsrespond pages 5-7) |
| Na+ cycling | Pathway/module |  | Continuous Na+ re-entry and re-export sustains Na+/H+ antiport-driven proton uptake in extreme alkaliphiles. | (krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 27-28) |
| membrane proton permeability | Trait/Process |  | The rate of proton leakage across the cytoplasmic membrane strongly influences whether intracellular pH can be stabilized at extreme external pH. | (lund2020understandinghowmicroorganisms pages 2-3, yao2023howmethanotrophsrespond pages 5-7) |
| membrane lipid remodeling | Pathway/module | GO:0006643 | Remodeling membrane lipids is a general adaptation that shifts proton permeability and stress tolerance at low or high pH. | (jiang2024exogenousputrescineplays pages 1-2, lund2020understandinghowmicroorganisms pages 2-3) |
| saturated fatty acids | Metabolite/Chemical | CHEBI:35366 | Enrichment of saturated fatty acids can reduce proton permeability and support acidophilic growth. | (yao2023howmethanotrophsrespond pages 5-7) |
| cyclopropane fatty acids | Metabolite/Chemical | CHEBI:61788 | Cyclopropane fatty acid enrichment is associated with reduced proton permeability during acid adaptation. | (lund2020understandinghowmicroorganisms pages 2-3) |
| S-layer | Cellular component | GO:0030115 | Surface-layer structures can increase negative surface charge and improve proton capture under alkaline conditions. | (yao2023howmethanotrophsrespond pages 5-7, yao2023howmethanotrophsrespond pages 7-8) |
| cytoplasmic membrane | Cellular component | GO:0005886 | The cytoplasmic membrane is the main barrier whose permeability and embedded transporters determine pH homeostasis capacity. | (krulwich2011molecularaspectsof pages 1-3, lund2020understandinghowmicroorganisms pages 2-3) |
| biofilm state | Assay factor | GO:0042710 | Biofilm growth can increase apparent pH stress resistance relative to planktonic cultures and thus affect observed pH range. | (jiang2024exogenousputrescineplays pages 1-2) |
| external pH | Environmental factor | ENVO:09200005 | External pH is the direct environmental determinant defining the observed growth-supporting range and shaping PMF demands. | (krulwich2011molecularaspectsof pages 1-3, ramoneda2023buildingagenomebased pages 1-2) |
| weak organic acid stress | Environmental factor |  | Weak organic acids impose pH-dependent stress beyond mineral-acid effects because their protonated forms can cross membranes. | (carere2021growthonformic pages 1-2, lund2020understandinghowmicroorganisms pages 2-3) |
| formic acid | Metabolite/Chemical | CHEBI:30751 | Formic acid is a clear example of a weak organic acid that diffuses into cells in protonated form and collapses pH homeostasis. | (carere2021growthonformic pages 1-2) |
| organic acid pKa | Assay factor |  | Organic-acid pKa determines the fraction present in membrane-permeant protonated form and therefore modifies effective acid stress in pH-range assays. | (carere2021growthonformic pages 1-2) |
| local buffering capacity | Assay factor |  | Buffering capacity influences how stable external pH remains during growth and therefore affects measured lower and upper growth limits. | (lund2020understandinghowmicroorganisms pages 3-5) |
| Na+/H+ antiport | Transporter | GO:0015385 | Na+/H+ antiport is a central alkaliphile mechanism for importing protons while exporting sodium to maintain cytoplasmic pH. | (krulwich2011molecularaspectsof pages 12-14, ito2017mrpantiportershave pages 1-2) |
| Mrp antiporter complex (MrpA-G) | Gene/Protein complex |  | The multicomponent Mrp complex is a principal Na+/H+ antiporter supporting alkaline pH homeostasis and high-pH growth. | (ito2017mrpantiportershave pages 1-2, krulwich2011molecularaspectsof pages 12-14) |
| mrp operon | Gene/Protein complex |  | The mrpABCDEFG operon encodes the hetero-oligomeric antiporter machinery required for strong alkaliphile pH homeostasis. | (ito2017mrpantiportershave pages 2-4, krulwich2011molecularaspectsof pages 27-28) |
| MrpA | Gene/Protein complex |  | MrpA is a core Mrp subunit with direct genetic evidence linking it to antiport activity and alkaline pH homeostasis. | (ito2017mrpantiportershave pages 9-10, krulwich2011molecularaspectsof pages 12-14) |
| MrpD | Gene/Protein complex |  | MrpD is a core Mrp subunit required for complex formation and/or H+ translocation in mechanistic models of the antiporter. | (ito2017mrpantiportershave pages 9-10, ito2017mrpantiportershave pages 4-5) |
| NhaA | Transporter |  | NhaA is an electrogenic Na+/H+ antiporter exemplar showing how antiporter stoichiometry can use Δψ to support pH homeostasis. | (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 15-17) |
| F1F0-ATP synthase | Gene/Protein complex | GO:0045263 | ATP synthase contributes to proton uptake/use and is structurally adapted in alkaliphiles to function under very high external pH. | (krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 15-17) |
| ATPase expression / proton pumping | Trait/Process | GO:0015986 | Elevated ATPase expression or activity can increase H+ transmembrane transport and improve acid-side pH stress adaptation. | (jiang2024exogenousputrescineplays pages 1-2, atasoy2024exploitationofmicrobial pages 3-4) |
| proton pumps of respiratory chain | Gene/Protein complex | GO:0015992 | Primary proton pumps generate PMF needed for downstream pH-homeostatic transport and are part of acidophile and alkaliphile strategies. | (krulwich2011molecularaspectsof pages 1-3, yao2023howmethanotrophsrespond pages 7-8) |
| protonated weak organic acid diffusion | Trait/Process |  | Diffusion of protonated weak acids across the membrane is a key boundary-case mechanism that can narrow the low-pH growth range. | (carere2021growthonformic pages 1-2) |
| cytosolic acidification | Trait/Process |  | Cytosolic acidification directly inhibits growth by denaturing proteins and collapsing PMF when homeostasis fails. | (carere2021growthonformic pages 1-2) |
| carbon fixation pathway choice | Pathway/module |  | Methanotroph pH ecotypes are associated with different carbon fixation strategies, suggesting energy economics can covary with pH adaptation. | (yao2023howmethanotrophsrespond pages 5-7, yao2023howmethanotrophsrespond pages 7-8) |
| Calvin-Benson-Bassham cycle | Pathway/module |  | The CBB cycle is associated with acidophilic verrucomicrobial methanotrophs and may fit high-PMF acidic lifestyles despite higher ATP cost. | (yao2023howmethanotrophsrespond pages 4-5, yao2023howmethanotrophsrespond pages 7-8) |
| ribulose monophosphate (RuMP) pathway | Pathway/module |  | The RuMP pathway is common in neutrophilic to alkaliphilic methanotrophs and is energetically favorable under those pH ecotypes. | (yao2023howmethanotrophsrespond pages 4-5, yao2023howmethanotrophsrespond pages 7-8) |
| serine pathway | Pathway/module |  | The serine pathway is linked to many mildly acidophilic and neutrophilic methanotrophs, making it a candidate ecotype-associated node. | (yao2023howmethanotrophsrespond pages 4-5, carere2021growthonformic pages 1-2) |
| bacterial pH preference | Trait/Process |  | Realized pH preference in nature is related but not identical to laboratory growth pH range and can help prioritize genomic correlates. | (ramoneda2023buildingagenomebased pages 6-7, ramoneda2023buildingagenomebased pages 1-2) |
| ML-predicted pH preference genes | Gene/Protein complex |  | A 56-gene feature set associated with natural pH preference is a useful abstract node category for comparative genomic inference, though not yet a direct mechanism node. | (ramoneda2023buildingagenomebased pages 6-7, ramoneda2023buildingagenomebased pages 1-2) |
| transmembrane cation/anion transport genes | Gene/Protein complex |  | Transport-associated genes were among the strongest genomic correlates of pH preference, consistent with ion-homeostasis control of pH range. | (ramoneda2023buildingagenomebased pages 6-7) |
| ATPase-associated pH preference genes | Gene/Protein complex |  | ATPase-related genes were part of the predictive genomic feature set for pH preference, matching known mechanistic roles in pH homeostasis. | (ramoneda2023buildingagenomebased pages 6-7) |


*Table: This table lists curation-ready candidate nodes for a microbial pH range causal graph, grouped by node type and annotated with suggested ontology grounding, mechanistic roles, and supporting evidence contexts. It is useful for selecting core vs. taxon-specific entities for TraitMech curation.*

## Evidence-backed candidate causal edges (triples)
The table below lists subject–predicate–object candidates with supporting snippets and curation notes. These edges are intended as a starting set for `data/traits/environment/ph_range.yaml`.

| Edge (Subject —predicate→ Object) | Mechanistic context (1 clause) | Evidence snippet (short quote) | Reference (first author year, DOI, URL) | Notes/uncertainty |
|---|---|---|---|---|
| External pH gradient (ΔpH) —contributes to→ growth-supporting pH range | PMF architecture sets whether cytoplasmic pH can be maintained across external pH | “the range of pHout values at which bacteria can tolerate or grow” and PMF “Δψ − 59 ΔpH” (krulwich2011molecularaspectsof pages 1-3, krulwich2011molecularaspectsof media 07c1b8d2) | Krulwich 2011, DOI:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549 | Broad, review-level edge; foundational rather than gene-specific |
| Membrane potential (Δψ) —compensates for→ extreme external pH stress | reversal/adjustment of PMF components offsets extreme ΔpH | “under strong pH stress the orientation of a PMF component can reverse” (krulwich2011molecularaspectsof pages 3-5) | Krulwich 2011, DOI:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549 | General physiological edge; curate as process-level |
| Cytoplasmic pH homeostasis —enables→ growth across external pH range | bounded phenotype reflects ability to keep pHin compatible with macromolecular function | “bacteria maintain a distinct cytoplasmic pH required for protein function” (krulwich2011molecularaspectsof pages 1-3) | Krulwich 2011, DOI:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549 | Strong, central edge; likely core TraitMech node |
| Increased membrane proton impermeability —extends→ low-pH growth | reduced proton leak helps acidophiles/acid-tolerant taxa maintain pHin | “modification of membrane lipid composition to reduce proton permeability” (lund2020understandinghowmicroorganisms pages 2-3) | Lund 2020, DOI:10.3389/fmicb.2020.556140, https://doi.org/10.3389/fmicb.2020.556140 | General acid-stress mechanism; not always directly quantified as range shift |
| Cyclopropane fatty acid enrichment —decreases→ proton permeability | membrane remodeling is part of acid adaptation | “increased cyclopropane fatty acids” reduce proton permeability (lund2020understandinghowmicroorganisms pages 2-3) | Lund 2020, DOI:10.3389/fmicb.2020.556140, https://doi.org/10.3389/fmicb.2020.556140 | Taxon/context dependent; stronger for acid stress than whole-range phenotype |
| Saturated membrane fatty acids —reduces→ proton permeability | acidophilic methanotroph membranes limit H+ influx | membranes “almost made up of saturated fatty acids” to “minimize proton permeability” (yao2023howmethanotrophsrespond pages 5-7) | Yao 2023, DOI:10.3389/fmicb.2022.1034164, https://doi.org/10.3389/fmicb.2022.1034164 | Taxon-specific to acidophilic verrucomicrobial methanotrophs |
| S-layer —increases→ proton capture at alkaline pH | negatively charged surface helps attract scarce external protons | “an S-layer… to increase net negative surface charge” and “To attract external protons” (yao2023howmethanotrophsrespond pages 5-7, yao2023howmethanotrophsrespond pages 7-8) | Yao 2023, DOI:10.3389/fmicb.2022.1034164, https://doi.org/10.3389/fmicb.2022.1034164 | Alkaliphile/methanotroph-focused; mechanistic but taxon-specific |
| Mrp antiporter complex —mediates→ Na+/H+ antiport activity | multi-subunit cation/proton antiport imports H+ while exporting Na+ | “Mrp functions as a Na+/H+ antiporter” and “all Mrp subunits, mrpA–G, are required” (ito2017mrpantiportershave pages 1-2) | Ito 2017, DOI:10.3389/fmicb.2017.02325, https://doi.org/10.3389/fmicb.2017.02325 | Strong for CPA3 Mrp systems; some exceptions where fewer subunits suffice |
| Mrp antiporter activity —supports→ alkaline pH homeostasis | Na+/H+ exchange is principal strategy in extreme alkaliphiles | “principal strategy used by extremely alkaliphilic Bacillus species” and “indispensable for survival at high pH” (krulwich2011molecularaspectsof pages 12-14) | Krulwich 2011, DOI:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549 | Strong but especially for extreme alkaliphilic Bacillus |
| mrpA point mutation —causes loss of→ alkaline pH homeostasis | gene-level evidence links antiporter subunit to phenotype | “a point mutation in mrpA… causes loss of alkaline pH homeostasis” (krulwich2011molecularaspectsof pages 12-14) | Krulwich 2011, DOI:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549 | Strong gene→phenotype edge; taxon-specific experiment |
| MrpA/MrpD subcomplex —is critical for→ Na+/H+ antiport | large subunits form core ion-translocation machinery | “MrpA/MrpD subcomplex is critical for catalyzing Na+/H+ antiport activity” (ito2017mrpantiportershave pages 5-8) | Ito 2017, DOI:10.3389/fmicb.2017.02325, https://doi.org/10.3389/fmicb.2017.02325 | Mechanistic subunit edge; useful for finer-grained graph if desired |
| NhaA antiporter stoichiometry (2H+/1Na+) —uses→ Δψ to drive proton import | electrogenic exchange supports pH homeostasis under alkali stress | “E. coli NhaA stoichiometry 2H+/1Na+” (krulwich2011molecularaspectsof pages 5-6) | Krulwich 2011, DOI:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549 | Evidence is mechanistic and model-organism specific; direct effect on trait range inferred |
| F1F0-ATP synthase adaptation —supports→ high-pH growth | specialized ATP synthase features aid proton capture/use at alkaline pH | “Adaptations of F1F0-ATP synthases” and motif mutations show “greater defect at pH 10.5 vs 7.5” (krulwich2011molecularaspectsof pages 12-14) | Krulwich 2011, DOI:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549 | Strong for alkaliphiles; subunit-motif details may be too fine for first-pass curation |
| ATPase expression/activity —promotes→ H+ transmembrane transport under acid stress | energy-linked pumping helps restore pHin | “stimulated ATPase expression… enhancing oxidative phosphorylation activity” (jiang2024exogenousputrescineplays pages 1-2) | Jiang 2024, DOI:10.1128/aem.00569-24, https://doi.org/10.1128/aem.00569-24 | Biofilm community study; assay/system-specific |
| Glutamate decarboxylase system (GAD/GABA) —consumes→ intracellular H+ | amino-acid decarboxylation alkalinizes cytoplasm | “maintain cytosolic pH homeostasis by consuming protons via GABA synthesis” (krulwich2011molecularaspectsof pages 15-17) | Wu 2017, DOI:10.3389/fmicb.2017.00206, https://doi.org/10.3389/fmicb.2017.00206 | Strong but from Lactobacillus brevis; source surfaced in search context, evidence summarized in current context |
| Glutamate-based acid resistance pathway —reduces→ acid stress | proton-consuming amino-acid metabolism broadens acid-side tolerance | “enhancing the glutamate-based acid resistance strategy and the γ-aminobutyric acid metabolic pathway to reduce acid stress” (jiang2024exogenousputrescineplays pages 1-2) | Jiang 2024, DOI:10.1128/aem.00569-24, https://doi.org/10.1128/aem.00569-24 | Biofilm/putrescine-modulated system; community-level and indirect |
| Arginine or glutamate decarboxylation —alkalinizes→ cell/microenvironment | decarboxylation is a recurring acid-response module | “decarboxylation of glutamate or arginine” (lund2020understandinghowmicroorganisms pages 3-5) | Lund 2020, DOI:10.3389/fmicb.2020.556140, https://doi.org/10.3389/fmicb.2020.556140 | More general than gene-specific; arginine genes not resolved in current context |
| Protonated weak organic acid —diffuses into→ cell | weak-acid entry depends on protonated state and pKa | “protonated form (CHOOH) can diffuse into cells” (carere2021growthonformic pages 1-2) | Carere 2021, DOI:10.3389/fmicb.2021.651744, https://doi.org/10.3389/fmicb.2021.651744 | Strong physicochemical edge; especially relevant for low external pH and organic acids |
| Intracellular deprotonation of formic acid —causes→ cytosolic acidification | weak-acid uncoupling collapses pH homeostasis | “deprotonation prompting cytosolic acidification” and “collapse of the proton motive force” (carere2021growthonformic pages 1-2) | Carere 2021, DOI:10.3389/fmicb.2021.651744, https://doi.org/10.3389/fmicb.2021.651744 | Strong, chemically explicit; taxon tested is Methylacidiphilum sp. RTK17.1 |
| Cytosolic acidification by formic acid —inhibits→ growth | inability to maintain pHin narrows usable external pH/acid conditions | “formic acid addition resulted in no observable cell growth and cell death” (carere2021growthonformic pages 1-2) | Carere 2021, DOI:10.3389/fmicb.2021.651744, https://doi.org/10.3389/fmicb.2021.651744 | Assay-specific to formic acid exposure; relevant boundary case for pH range assays |
| Organic acid pKa —modulates→ weak-acid membrane permeation | protonated fraction increases below pKa, affecting acid stress severity | “Formic acid has pKa ≈ 3.74 and at external pH <3 its protonated form… can diffuse” (carere2021growthonformic pages 1-2) | Carere 2021, DOI:10.3389/fmicb.2021.651744, https://doi.org/10.3389/fmicb.2021.651744 | Environmental/assay factor, not organismal mechanism |
| Buffering compound production —raises→ local pH | microbes can alkalinize surroundings to improve low-pH survival/growth | “alkalinization of the microenvironment via buffering compound production” (lund2020understandinghowmicroorganisms pages 3-5) | Lund 2020, DOI:10.3389/fmicb.2020.556140, https://doi.org/10.3389/fmicb.2020.556140 | Environmental microenvironment edge; often context dependent |
| Biofilm state —increases→ pH stress resistance | matrix/community state modifies effective tolerance window | “biofilms confer extra pH resistance” (jiang2024exogenousputrescineplays pages 1-2) | Jiang 2024, DOI:10.1128/aem.00569-24, https://doi.org/10.1128/aem.00569-24 | Assay/ecology-specific; may not generalize to planktonic trait measurements |
| Na+ re-entry systems —support→ continuous Mrp-dependent proton uptake | coupled Na+ cycling maintains antiporter operation at high pH | “Na+ re-entry… supports continuous antiport” (krulwich2011molecularaspectsof pages 27-28) | Krulwich 2011, DOI:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549 | Mechanistic systems edge; specific Na+/solute symporters/channels may be taxon-specific |
| Acid-side or alkali-side constitutive homeostasis machinery —imposes→ energetic cost near neutral pH | specialization can trade off with performance outside preferred range | “constitutively expressed, imposing energetic costs that can reduce growth near neutral pH” (krulwich2011molecularaspectsof pages 3-5) | Krulwich 2011, DOI:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549 | Useful cautionary edge; broad and inferred at phenotype level |


*Table: This table lists curation-ready candidate causal edges for the microbial trait pH range, covering PMF, membranes, antiporters, ATP synthase, decarboxylase systems, weak organic acids, and assay/environmental modifiers. It is useful as a starting point for selecting strongly supported versus taxon-specific edges for TraitMech curation.*

## Ontology grounding notes
- **Strong groundings** (examples): pH homeostasis (GO:0010447), proton motive force (GO:0015995), cytoplasmic membrane (GO:0005886), Na+/H+ antiporter activity (GO:0015385), ATP synthase complex (GO:0045263), formic acid (CHEBI:30751), saturated fatty acids (CHEBI:35366). (krulwich2011molecularaspectsof pages 1-3, carere2021growthonformic pages 1-2, yao2023howmethanotrophsrespond pages 5-7)
- **Weaker/placeholder groundings**: Mrp subunits (MrpA–G) are best kept as **labeled protein-family nodes** unless curated against a specific taxon’s UniProt accessions or transporter-family identifiers; methanotroph pathway associations (CBB/RuMP/serine) are best curated at the module/pathway level in the graph unless organism-specific gene sets are added. (ito2017mrpantiportershave pages 1-2, yao2023howmethanotrophsrespond pages 7-8)

## Warnings (claims not yet ready for strong TraitMech curation)
1. **Realized pH preference ≠ growth pH range**: Genome-based pH preference (relative abundance maximum) is influenced by ecology and may not directly encode min/max growth pH. Use as hypothesis generation and association nodes, not as mechanistic edges without additional validation. (ramoneda2023buildingagenomebased pages 6-7, ramoneda2023buildingagenomebased pages 1-2)
2. **Biofilm/community modifiers** (e.g., putrescine effects) are likely **assay- and ecosystem-specific**; curate as conditional edges (biofilm context) or keep as “uncertain” until replicated across systems. (jiang2024exogenousputrescineplays pages 1-2)
3. **Carbon fixation pathway associations** with pH ecotypes (methanotrophs) are plausible but may reflect **phylogeny and energy trade-offs** rather than direct causal determinants of pH range; curate with uncertainty unless direct perturbation evidence is added. (yao2023howmethanotrophsrespond pages 7-8)

## DOI-first bibliography (with URLs and publication months where available)
- Krulwich TA, Sachs G, Padan E. **Molecular aspects of bacterial pH sensing and homeostasis.** *Nature Reviews Microbiology* (2011-05). DOI: **10.1038/nrmicro2549**. https://doi.org/10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 1-3, krulwich2011molecularaspectsof pages 12-14)
- Ramoneda J, Stallard-Olivera E, Hoffert M, et al. **Building a genome-based understanding of bacterial pH preferences.** *Science Advances* (2023-04). DOI: **10.1126/sciadv.adf8998**. https://doi.org/10.1126/sciadv.adf8998 (ramoneda2023buildingagenomebased pages 1-2, ramoneda2023buildingagenomebased pages 6-7)
- Yao X, Wang J, Hu B. **How methanotrophs respond to pH: A review of ecophysiology.** *Frontiers in Microbiology* (2023-01). DOI: **10.3389/fmicb.2022.1034164**. https://doi.org/10.3389/fmicb.2022.1034164 (yao2023howmethanotrophsrespond pages 4-5, yao2023howmethanotrophsrespond pages 5-7)
- Atasoy M, Álvarez Ordóñez A, Cenian A, et al. **Exploitation of microbial activities at low pH to enhance planetary health.** *FEMS Microbiology Reviews* (2024-11). DOI: **10.1093/femsre/fuad062**. https://doi.org/10.1093/femsre/fuad062 (atasoy2024exploitationofmicrobial pages 1-2, atasoy2024exploitationofmicrobial pages 7-8)
- Jiang G, Wang C, Wang Y, et al. **Exogenous putrescine plays a switch-like influence on the pH stress adaptability of biofilm-based activated sludge.** *Applied and Environmental Microbiology* (2024-07). DOI: **10.1128/aem.00569-24**. https://doi.org/10.1128/aem.00569-24 (jiang2024exogenousputrescineplays pages 1-2)
- Ito M, Morino M, Krulwich TA. **Mrp Antiporters Have Important Roles in Diverse Bacteria and Archaea.** *Frontiers in Microbiology* (2017-11). DOI: **10.3389/fmicb.2017.02325**. https://doi.org/10.3389/fmicb.2017.02325 (ito2017mrpantiportershave pages 1-2)
- Carere CR, Hards K, Wigley K, et al. **Growth on Formic Acid Is Dependent on Intracellular pH Homeostasis for the Thermoacidophilic Methanotroph Methylacidiphilum sp. RTK17.1.** *Frontiers in Microbiology* (2021-03). DOI: **10.3389/fmicb.2021.651744**. https://doi.org/10.3389/fmicb.2021.651744 (carere2021growthonformic pages 1-2)
- Lund PA, De Biase D, Liran O, et al. **Understanding How Microorganisms Respond to Acid pH Is Central to Their Control and Successful Exploitation.** *Frontiers in Microbiology* (2020-09). DOI: **10.3389/fmicb.2020.556140**. https://doi.org/10.3389/fmicb.2020.556140 (lund2020understandinghowmicroorganisms pages 3-5)


References

1. (krulwich2011molecularaspectsof pages 1-3): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

2. (ramoneda2023buildingagenomebased pages 6-7): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 88 citations and is from a highest quality peer-reviewed journal.

3. (ramoneda2023buildingagenomebased pages 1-2): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 88 citations and is from a highest quality peer-reviewed journal.

4. (krulwich2011molecularaspectsof pages 3-5): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

5. (carere2021growthonformic pages 1-2): Carlo R. Carere, Kiel Hards, Kathryn Wigley, Luke Carman, Karen M. Houghton, Gregory M. Cook, and Matthew B. Stott. Growth on formic acid is dependent on intracellular ph homeostasis for the thermoacidophilic methanotroph methylacidiphilum sp. rtk17.1. Frontiers in Microbiology, Mar 2021. URL: https://doi.org/10.3389/fmicb.2021.651744, doi:10.3389/fmicb.2021.651744. This article has 22 citations and is from a peer-reviewed journal.

6. (krulwich2011molecularaspectsof media 07c1b8d2): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

7. (yao2023howmethanotrophsrespond pages 4-5): Xiangwu Yao, Jiaqi Wang, and Baolan Hu. How methanotrophs respond to ph: a review of ecophysiology. Frontiers in Microbiology, Jan 2023. URL: https://doi.org/10.3389/fmicb.2022.1034164, doi:10.3389/fmicb.2022.1034164. This article has 72 citations and is from a peer-reviewed journal.

8. (yao2023howmethanotrophsrespond pages 5-7): Xiangwu Yao, Jiaqi Wang, and Baolan Hu. How methanotrophs respond to ph: a review of ecophysiology. Frontiers in Microbiology, Jan 2023. URL: https://doi.org/10.3389/fmicb.2022.1034164, doi:10.3389/fmicb.2022.1034164. This article has 72 citations and is from a peer-reviewed journal.

9. (yao2023howmethanotrophsrespond pages 7-8): Xiangwu Yao, Jiaqi Wang, and Baolan Hu. How methanotrophs respond to ph: a review of ecophysiology. Frontiers in Microbiology, Jan 2023. URL: https://doi.org/10.3389/fmicb.2022.1034164, doi:10.3389/fmicb.2022.1034164. This article has 72 citations and is from a peer-reviewed journal.

10. (atasoy2024exploitationofmicrobial pages 7-8): Merve Atasoy, Avelino Álvarez Ordóñez, Adam Cenian, Aleksandra Djukić-Vuković, Peter A Lund, Fatih Ozogul, Janja Trček, Carmit Ziv, and Daniela De Biase. Exploitation of microbial activities at low ph to enhance planetary health. FEMS Microbiology Reviews, Nov 2024. URL: https://doi.org/10.1093/femsre/fuad062, doi:10.1093/femsre/fuad062. This article has 96 citations and is from a domain leading peer-reviewed journal.

11. (atasoy2024exploitationofmicrobial pages 5-6): Merve Atasoy, Avelino Álvarez Ordóñez, Adam Cenian, Aleksandra Djukić-Vuković, Peter A Lund, Fatih Ozogul, Janja Trček, Carmit Ziv, and Daniela De Biase. Exploitation of microbial activities at low ph to enhance planetary health. FEMS Microbiology Reviews, Nov 2024. URL: https://doi.org/10.1093/femsre/fuad062, doi:10.1093/femsre/fuad062. This article has 96 citations and is from a domain leading peer-reviewed journal.

12. (jiang2024exogenousputrescineplays pages 1-2): Guanyu Jiang, Can Wang, Yongchao Wang, Jiayi Wang, Yi-Mei Xue, Yuting Lin, Xurui Hu, and Yahui Lv. Exogenous putrescine plays a switch-like influence on the ph stress adaptability of biofilm-based activated sludge. Applied and Environmental Microbiology, Jul 2024. URL: https://doi.org/10.1128/aem.00569-24, doi:10.1128/aem.00569-24. This article has 6 citations and is from a peer-reviewed journal.

13. (atasoy2024exploitationofmicrobial pages 2-3): Merve Atasoy, Avelino Álvarez Ordóñez, Adam Cenian, Aleksandra Djukić-Vuković, Peter A Lund, Fatih Ozogul, Janja Trček, Carmit Ziv, and Daniela De Biase. Exploitation of microbial activities at low ph to enhance planetary health. FEMS Microbiology Reviews, Nov 2024. URL: https://doi.org/10.1093/femsre/fuad062, doi:10.1093/femsre/fuad062. This article has 96 citations and is from a domain leading peer-reviewed journal.

14. (atasoy2024exploitationofmicrobial pages 1-2): Merve Atasoy, Avelino Álvarez Ordóñez, Adam Cenian, Aleksandra Djukić-Vuković, Peter A Lund, Fatih Ozogul, Janja Trček, Carmit Ziv, and Daniela De Biase. Exploitation of microbial activities at low ph to enhance planetary health. FEMS Microbiology Reviews, Nov 2024. URL: https://doi.org/10.1093/femsre/fuad062, doi:10.1093/femsre/fuad062. This article has 96 citations and is from a domain leading peer-reviewed journal.

15. (atasoy2024exploitationofmicrobial pages 17-18): Merve Atasoy, Avelino Álvarez Ordóñez, Adam Cenian, Aleksandra Djukić-Vuković, Peter A Lund, Fatih Ozogul, Janja Trček, Carmit Ziv, and Daniela De Biase. Exploitation of microbial activities at low ph to enhance planetary health. FEMS Microbiology Reviews, Nov 2024. URL: https://doi.org/10.1093/femsre/fuad062, doi:10.1093/femsre/fuad062. This article has 96 citations and is from a domain leading peer-reviewed journal.

16. (krulwich2011molecularaspectsof pages 5-6): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

17. (krulwich2011molecularaspectsof pages 12-14): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

18. (ito2017mrpantiportershave pages 1-2): Masahiro Ito, Masato Morino, and Terry A. Krulwich. Mrp antiporters have important roles in diverse bacteria and archaea. Frontiers in Microbiology, Nov 2017. URL: https://doi.org/10.3389/fmicb.2017.02325, doi:10.3389/fmicb.2017.02325. This article has 141 citations and is from a peer-reviewed journal.

19. (lund2020understandinghowmicroorganisms pages 3-5): Peter A. Lund, Daniela De Biase, Oded Liran, Ott Scheler, Nuno Pereira Mira, Zeynep Cetecioglu, Estefanía Noriega Fernández, Sara Bover-Cid, Rebecca Hall, Michael Sauer, and Conor O’Byrne. Understanding how microorganisms respond to acid ph is central to their control and successful exploitation. Frontiers in Microbiology, Sep 2020. URL: https://doi.org/10.3389/fmicb.2020.556140, doi:10.3389/fmicb.2020.556140. This article has 359 citations and is from a peer-reviewed journal.

20. (atasoy2024exploitationofmicrobial pages 3-4): Merve Atasoy, Avelino Álvarez Ordóñez, Adam Cenian, Aleksandra Djukić-Vuković, Peter A Lund, Fatih Ozogul, Janja Trček, Carmit Ziv, and Daniela De Biase. Exploitation of microbial activities at low ph to enhance planetary health. FEMS Microbiology Reviews, Nov 2024. URL: https://doi.org/10.1093/femsre/fuad062, doi:10.1093/femsre/fuad062. This article has 96 citations and is from a domain leading peer-reviewed journal.

21. (krulwich2011molecularaspectsof pages 15-17): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

22. (krulwich2011molecularaspectsof pages 27-28): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

23. (lund2020understandinghowmicroorganisms pages 2-3): Peter A. Lund, Daniela De Biase, Oded Liran, Ott Scheler, Nuno Pereira Mira, Zeynep Cetecioglu, Estefanía Noriega Fernández, Sara Bover-Cid, Rebecca Hall, Michael Sauer, and Conor O’Byrne. Understanding how microorganisms respond to acid ph is central to their control and successful exploitation. Frontiers in Microbiology, Sep 2020. URL: https://doi.org/10.3389/fmicb.2020.556140, doi:10.3389/fmicb.2020.556140. This article has 359 citations and is from a peer-reviewed journal.

24. (ito2017mrpantiportershave pages 2-4): Masahiro Ito, Masato Morino, and Terry A. Krulwich. Mrp antiporters have important roles in diverse bacteria and archaea. Frontiers in Microbiology, Nov 2017. URL: https://doi.org/10.3389/fmicb.2017.02325, doi:10.3389/fmicb.2017.02325. This article has 141 citations and is from a peer-reviewed journal.

25. (ito2017mrpantiportershave pages 9-10): Masahiro Ito, Masato Morino, and Terry A. Krulwich. Mrp antiporters have important roles in diverse bacteria and archaea. Frontiers in Microbiology, Nov 2017. URL: https://doi.org/10.3389/fmicb.2017.02325, doi:10.3389/fmicb.2017.02325. This article has 141 citations and is from a peer-reviewed journal.

26. (ito2017mrpantiportershave pages 4-5): Masahiro Ito, Masato Morino, and Terry A. Krulwich. Mrp antiporters have important roles in diverse bacteria and archaea. Frontiers in Microbiology, Nov 2017. URL: https://doi.org/10.3389/fmicb.2017.02325, doi:10.3389/fmicb.2017.02325. This article has 141 citations and is from a peer-reviewed journal.

27. (ito2017mrpantiportershave pages 5-8): Masahiro Ito, Masato Morino, and Terry A. Krulwich. Mrp antiporters have important roles in diverse bacteria and archaea. Frontiers in Microbiology, Nov 2017. URL: https://doi.org/10.3389/fmicb.2017.02325, doi:10.3389/fmicb.2017.02325. This article has 141 citations and is from a peer-reviewed journal.