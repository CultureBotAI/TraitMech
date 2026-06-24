---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T23:50:23.636198'
end_time: '2026-06-18T00:05:52.652616'
duration_seconds: 929.02
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: obligately piezophilic
  trait_identifier: traitmech:000002
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: obligately_piezophilic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pressure growth preference in which an organism requires elevated
    hydrostatic pressure for growth and is unable to grow at atmospheric pressure
    (0.1 MPa).
  parent_traits: traitmech:000001
  synonyms: obligate piezophile
  evidence_summary: 'DOI:10.1038/srep27289: High hydrostatic pressure adaptive strategies
    in an obligate piezophile Pyrococcus yayanosii (Organism example: Pyrococcus yayanosii
    is an obligate piezophile that requires high hydrostatic pressure for growth.)
    | DOI:10.1099/ijsem.0.001671: growth range of 80-140 MPa (optimum, 120 MPa) at
    6 degrees C (Organism example: Colwellia marinimaniae MTCD1 grows only at high
    pressure (80-140 MPa) and does not grow near atmospheric pressure.)'
  causal_graph_summary: 'obligate_piezophily_high_pressure_requirement: 3 nodes, 2
    edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 38
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** obligately piezophilic
- **METPO identifier:** traitmech:000002
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pressure growth preference in which an organism requires elevated hydrostatic pressure for growth and is unable to grow at atmospheric pressure (0.1 MPa).
- **Parent traits:** traitmech:000001
- **Synonyms:** obligate piezophile
- **Existing evidence:** DOI:10.1038/srep27289: High hydrostatic pressure adaptive strategies in an obligate piezophile Pyrococcus yayanosii (Organism example: Pyrococcus yayanosii is an obligate piezophile that requires high hydrostatic pressure for growth.) | DOI:10.1099/ijsem.0.001671: growth range of 80-140 MPa (optimum, 120 MPa) at 6 degrees C (Organism example: Colwellia marinimaniae MTCD1 grows only at high pressure (80-140 MPa) and does not grow near atmospheric pressure.)
- **Existing causal graph summary:** obligate_piezophily_high_pressure_requirement: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **obligately piezophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/obligately_piezophilic.yaml`.

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
- **Trait label:** obligately piezophilic
- **METPO identifier:** traitmech:000002
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pressure growth preference in which an organism requires elevated hydrostatic pressure for growth and is unable to grow at atmospheric pressure (0.1 MPa).
- **Parent traits:** traitmech:000001
- **Synonyms:** obligate piezophile
- **Existing evidence:** DOI:10.1038/srep27289: High hydrostatic pressure adaptive strategies in an obligate piezophile Pyrococcus yayanosii (Organism example: Pyrococcus yayanosii is an obligate piezophile that requires high hydrostatic pressure for growth.) | DOI:10.1099/ijsem.0.001671: growth range of 80-140 MPa (optimum, 120 MPa) at 6 degrees C (Organism example: Colwellia marinimaniae MTCD1 grows only at high pressure (80-140 MPa) and does not grow near atmospheric pressure.)
- **Existing causal graph summary:** obligate_piezophily_high_pressure_requirement: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **obligately piezophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/obligately_piezophilic.yaml`.

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


## Curation-Focused Research Report: **obligately piezophilic** (METPO:traitmech:000002)

### 0. Scope summary (what the trait represents)
**Obligately piezophilic** organisms (also called **hyperpiezophiles** in some sources) are microorganisms that **require elevated hydrostatic pressure (HP) for growth and are unable to grow at ambient pressure (~0.1 MPa)**. This trait is typically operationalized by **growth assays across an HP range** showing **no growth at 0.1 MPa** but growth at elevated pressures. Scoma (2021) explicitly defines obligate piezophiles/hyperpiezophiles as “unable to grow at ambient pressure” and emphasizes that **temperature strongly modulates HP optima**, so classification should consider both HP and temperature rather than HP thresholds alone. (scoma2021functionalgroupsin pages 1-2, scoma2021functionalgroupsin pages 2-3, scoma2021functionalgroupsin pages 5-6)

**Boundary cases / nearby traits**:
- **Piezophilic (non-obligate)**: organisms with μmax (maximum growth rate) at HP > 0.1 MPa but that may still grow at 0.1 MPa (definition used widely, but Scoma critiques using HP>0.1 MPa as too low/overinclusive). (scoma2021functionalgroupsin pages 5-6)
- **Piezotolerant**: organisms that **can grow at 0.1 MPa** but can also tolerate and/or grow up to elevated HP; e.g., in Pseudothermotoga elfii comparison, one strain is “piezophilic” with HPopt 20 MPa while the other is “piezotolerant” with growth only up to 20 MPa. (roumagnac2020responsestothe pages 1-2)

**Representative obligate/extreme examples (pressure ranges)**:
- *Colwellia marinimaniae* **MTCD1**: described as extremely piezophilic with **growth range 80–140 MPa** and **optimum 120 MPa** (excludes ambient pressure). (peoples2020distinctivegeneand pages 1-2, peoples2020distinctivegeneand media c39a23c1)
- *Colwellia* sp. **MT41**: described as an obligate psychropiezophile with optimum ~103 MPa and **inability to grow below 35 MPa**. (peoples2020distinctivegeneand pages 1-2)
- *Pyrococcus yayanosii* CH1: described as “the first and only described obligate piezophilic hyperthermophilic archaeon”; one study determined an **optimal pressure of 52 MPa** (with 20 and 80 MPa treated as stressful). (michoud2016highhydrostaticpressure pages 1-2, scoma2021functionalgroupsin pages 5-6)

### 1. Key concepts & definitions (current understanding)
1) **Hydrostatic pressure as an environmental driver**
- Deep ocean pressure rises ~**1 MPa per 100 m** depth, and deep sea (>1,000 m) is typically **>10 MPa** and ~**2°C**, creating coupled pressure–temperature selection. (scoma2021functionalgroupsin pages 1-2, tamby2023microbialmembranelipid pages 1-2)

2) **Operational definition challenges**
- Multiple HP thresholds have been used historically (e.g., ≥10 MPa; ≥50 MPa; ≥60 MPa) to define piezophiles and hyperpiezophiles, but a central message is that **HP effects depend on temperature**, so single-threshold definitions can be misleading. (scoma2021functionalgroupsin pages 1-2, scoma2021functionalgroupsin pages 2-3, scoma2021functionalgroupsin pages 5-6)

3) **Mechanistic framing**
High pressure perturbs:
- **Membrane structure/fluidity** (compaction of fatty-acid chains; altered viscosity and phase behavior). (scheffer2023themysteryof pages 6-7, tamby2023microbialmembranelipid pages 2-4)
- **Protein folding and function** (pressure-driven water intrusion and denaturation; altered enzyme properties). (scheffer2023themysteryof pages 10-12, tamby2023microbialmembranelipid pages 1-2)
- **Cellular processes** including transcription/translation and motility. (malas2024biologicalfunctionsat pages 1-2, scheffer2023themysteryof pages 6-7)

### 2. Recent developments & latest research (prioritize 2023–2024)
#### 2.1 2023—Membrane lipid adaptation synthesis (marine focus)
Tamby et al. (Frontiers in Molecular Biosciences; **Jan 2023**) review membrane adaptations under HHP. A key cross-taxon trend is that **lipids with unsaturated and branched-chain fatty acids often increase with HHP**, but responses are **not universal**, and cold adaptation can confound pressure signals. They highlight **homeoviscous/homeophasic adaptation** and emphasize that omega‑3 PUFAs (notably **EPA C20:5** and **DHA C22:6**) are frequently associated with HHP adaptation in marine bacteria, with species-specific exceptions. (tamby2023microbialmembranelipid pages 1-2, tamby2023microbialmembranelipid pages 2-4)

#### 2.2 2023—Review of piezophile mechanisms across deep subsurface systems
Scheffer & Gieg (Microorganisms; **Jun 2023**) synthesize diverse adaptations, including:
- **Outer membrane porin OmpH** increasing **~10–100× between 0.1 and 28 MPa**, under **toxR** control in cited systems. (scheffer2023themysteryof pages 7-9)
- **Compatible solutes (“piezolytes”)** and preferential hydration as protein-protection mechanisms; examples include accumulation of **glutamate, betaine, β-hydroxybutyrate** at **20–30 MPa** in *Photobacterium profundum*, and discussion of **TMAO** as a piezolyte and/or energy-related metabolite depending on organism. (scheffer2023themysteryof pages 9-10)
- **Respiratory/energy metabolism reconfiguration** under pressure, including pressure-dependent shifts in respiratory components in *Shewanella* and Hmc complex gene increases in *Desulfovibrio*. (scheffer2023themysteryof pages 7-9)
- **Motility/chemotaxis involvement** (MCP and Che systems upregulated in some taxa), and mutant evidence in *Desulfovibrio alaskensis* linking flagellar genes (**ΔflaB3, ΔfliD, ΔfliA**) to reduced growth under high pressure. (scheffer2023themysteryof pages 6-7)

#### 2.3 2024—Transcriptomics under extreme pressure relevant to icy-ocean worlds
Malas et al. (Frontiers in Microbiology; **Feb 2024**) examined *Shewanella oneidensis* MR‑1 exposure to **158 MPa** (15 min and 2 h), reporting that MR‑1 was metabolically active and capable of viable growth after 2 h exposure and that **264 genes** were regulated in response to short-term HHP, with upregulation of **arginine biosynthesis genes (argA, argB, argC, argF)** plus stress-related responses including **cold-shock protein CspG** and antioxidant defense genes. (malas2024biologicalfunctionsat pages 1-2)

Although MR‑1 is not an obligate piezophile, this is a **recent, well-instrumented** study illustrating modern high-pressure systems and the overlap between HHP response modules and piezophile adaptations. (malas2024biologicalfunctionsat pages 1-2, malas2024biologicalfunctionsat pages 12-13)

#### 2.4 2024—Multi-omics metabolic adaptation at 30 MPa
Qiu et al. (Applied Microbiology and Biotechnology; **Jan 2024**) exposed *Microbacterium sediminis* YLB‑01 to **30 MPa at 4°C for 7 days** and used proteomics + NMR metabolomics. They report strong separation of HPLT vs NPLT metabolomes (OPLS‑DA **R2Y=0.988, Q2Y=0.974**) and **21 differential metabolites**, dominated by amino acids and carbohydrates (including **proline**, **trehalose**, and **UDP‑glucose**). They interpret the response as involving regulation of amino-acid and carbohydrate metabolism, increased cell wall synthesis, and improved membrane fluidity. (qiu2024metabolicadaptationsof pages 5-7, qiu2024metabolicadaptationsof pages 1-2)

### 3. Current applications and real-world implementations
1) **High-pressure cultivation and improved isolation of in situ organisms**
A recurring practical implication is that many deep-sea/subsurface organisms may be missed if cultured only at 0.1 MPa; pressure-aware cultivation is therefore key for isolation and correct phenotyping of pressure-adapted microbes. This underpins both ecological discovery and trait curation. (scoma2021functionalgroupsin pages 1-2, tamby2023microbialmembranelipid pages 1-2)

2) **Comparative genomics as a curation input for candidate mechanisms**
Comparative genomics in extremely piezophilic *Colwellia* identifies gene sets enriched/present only in piezophiles (e.g., **nuo operon**, **tad pilus**, **pfaABCD**, **delta‑9 desaturase**) and contrasts (e.g., **cis/trans isomerase only in piezosensitive strains**), providing mechanistic hypotheses that can be translated into TraitMech graph edges with appropriate association caveats. (peoples2020distinctivegeneand pages 1-2, peoples2020distinctivegeneand pages 5-7)

3) **Astrobiology / planetary analog studies**
High-pressure experimental systems are being used to probe habitability of icy ocean worlds (Titan/Europa/Enceladus) via microbial activity at pressures (e.g., **158 MPa**) that exceed many natural Earth habitats, extending the methodological toolbox and generating new gene/pathway candidates for pressure tolerance. (malas2024biologicalfunctionsat pages 1-2, malas2024biologicalfunctionsat pages 2-3)

### 4. Expert opinions and analysis (authoritative synthesis)
- **Temperature must be integrated**: Scoma (ISME J, 2021) argues that defining “piezophile” simply as μmax at HP>0.1 MPa is overly permissive and that functional groupings should incorporate temperature due to its strong influence on HPopt and growth comparisons. (scoma2021functionalgroupsin pages 5-6)
- **No single universal membrane rule**: Tamby et al. (2023) emphasize that while increased unsaturation/branched chains is common, it is not universal; pressure effects are intertwined with temperature and methodological choices. This implies membrane edges should often be curated as **“often increases”** rather than **necessary and sufficient**. (tamby2023microbialmembranelipid pages 2-4, tamby2023microbialmembranelipid pages 1-2)
- **Mechanisms can be taxon-specific**: Scheffer & Gieg (2023) compile examples where pressure causes respiratory switching, porin induction, motility changes, and solute accumulation; these mechanisms show common themes but are expressed differently by lineage and environment. (scheffer2023themysteryof pages 7-9, scheffer2023themysteryof pages 6-7)

### 5. Relevant statistics and data (recent studies and quantitative points)
- **Trait definition**: obligate piezophiles/hyperpiezophiles are **“unable to grow at ambient pressure.”** (scoma2021functionalgroupsin pages 1-2)
- **Extremely piezophilic growth ranges**:
  - *Colwellia marinimaniae* MTCD1: **80–140 MPa**, optimum **120 MPa** (also shown in figure). (peoples2020distinctivegeneand pages 1-2, peoples2020distinctivegeneand media c39a23c1)
  - *Colwellia* sp. MT41: optimum **103 MPa**, cannot grow below **35 MPa**. (peoples2020distinctivegeneand pages 1-2)
- **Porin induction**: OmpH abundance increases **~10–100×** from **0.1 → 28 MPa** in cited systems. (scheffer2023themysteryof pages 7-9)
- **Pressure-induced morphology**: *Pseudothermotoga elfii* DSM9442 shows chaining rising to **44% of cells** at **40 MPa**, interpreted as protective. (roumagnac2020responsestothe pages 1-2)
- **Transcriptomics under HHP**: MR‑1 at **158 MPa** regulates **264 genes** in short-term exposure; arginine biosynthesis genes (argA/B/C/F) are upregulated. (malas2024biologicalfunctionsat pages 1-2)
- **Metabolomics statistics under 30 MPa**: OPLS‑DA **R2Y=0.988, Q2Y=0.974**; **21 differential metabolites** reported. (qiu2024metabolicadaptationsof pages 5-7)

---

## Candidate causal-graph nodes (curation inventory)
The following artifact provides candidate nodes (grouped; with conservative grounding suggestions and “label only” placeholders where identifiers are unclear).

| Group | Label | Node type | Suggested grounding CURIE(s) | Brief relevance note |
|---|---|---|---|---|
| Trait/Phenotype | obligately piezophilic | trait/phenotype | METPO:traitmech:000002 | Requires elevated hydrostatic pressure for growth and is unable to grow at ambient pressure; core trait under curation (scoma2021functionalgroupsin pages 1-2, michoud2016highhydrostaticpressure pages 1-2, scoma2021functionalgroupsin pages 5-6) |
| Trait/Phenotype | hyperpiezophile | trait/phenotype | label only | Near-synonymous literature label for organisms unable to grow at ambient pressure; useful boundary term for curation notes (scoma2021functionalgroupsin pages 1-2, scoma2021functionalgroupsin pages 5-6) |
| Trait/Phenotype | piezotolerant | trait/phenotype | label only | Boundary case: grows at ambient pressure but tolerates or grows up to elevated pressure; should not be conflated with obligate piezophily (roumagnac2020responsestothe pages 1-2) |
| Environmental factor/assay | high hydrostatic pressure | environmental factor | ENVO:01000254 | Primary environmental driver selecting for the trait; deep-sea pressure rises with depth and perturbs proteins and membranes (scoma2021functionalgroupsin pages 1-2, tamby2023microbialmembranelipid pages 1-2) |
| Environmental factor/assay | ambient pressure (0.1 MPa) | environmental factor/assay condition | label only | Diagnostic assay condition used to separate obligate piezophiles from piezotolerant/facultative strains (scoma2021functionalgroupsin pages 1-2, michoud2016highhydrostaticpressure pages 1-2, scoma2021functionalgroupsin pages 5-6) |
| Environmental factor/assay | temperature interaction with pressure | environmental factor | label only | Pressure optimum depends strongly on temperature; needed for interpreting assays and boundary cases (scoma2021functionalgroupsin pages 2-3, tamby2023microbialmembranelipid pages 1-2) |
| Environmental factor/assay | deep-sea / hadal habitat | environmental factor | ENVO:00000319; ENVO:01000182 | Environmental context where obligate or extreme piezophiles are typically found, especially hadal/abyssal settings (peoples2020distinctivegeneand pages 1-2, scoma2021functionalgroupsin pages 5-6) |
| Cellular structures/processes | membrane fluidity | biological property/process | GO:0016042 | High pressure compresses membranes; maintenance of fluidity is a central adaptation axis (scheffer2023themysteryof pages 6-7, tamby2023microbialmembranelipid pages 2-4) |
| Cellular structures/processes | homeoviscous adaptation | biological process | GO:0042558 | Lipid remodeling process used to preserve membrane function under pressure/temperature stress (tamby2023microbialmembranelipid pages 2-4) |
| Cellular structures/processes | cell wall synthesis | biological process | GO:0009252 | High-pressure adaptation in some strains includes increased UDP-glucose and inferred enhanced cell-wall synthesis (qiu2024metabolicadaptationsof pages 1-2) |
| Cellular structures/processes | chemotaxis | biological process | GO:0006935 | Pressure-responsive signaling/motility process; MCP and Che systems are upregulated in piezophiles (scheffer2023themysteryof pages 6-7) |
| Cellular structures/processes | flagellum-dependent motility | biological process | GO:0071973 | Flagellar systems contribute to growth and fitness under high pressure in some taxa (scheffer2023themysteryof pages 6-7) |
| Cellular structures/processes | oxidative stress defense | biological process | GO:0006979 | Superoxide dismutase/catalase retained in piezophiles, supporting stress management under deep-sea conditions (peoples2020distinctivegeneand pages 7-9) |
| Cellular structures/processes | tRNA modification | biological process | GO:0006400 | Proposed role for piezophile-associated SAM-dependent methyltransferase in translation-related adaptation (peoples2020distinctivegeneand pages 1-2, peoples2020distinctivegeneand pages 7-9) |
| Cellular structures/processes | ribosome stabilization / translation under pressure | biological process | GO:0006412 | Translation machinery is pressure-sensitive; piezophiles show translation-associated enrichments and ribosomal adaptations (scheffer2023themysteryof pages 10-12, peoples2020distinctivegeneand pages 4-5) |
| Genes/Proteins/Complexes | OmpH porin | protein | label only | Outer membrane porin reported to increase ~10–100× with pressure in some piezophiles; candidate membrane-permeability node (scheffer2023themysteryof pages 7-9, scheffer2023themysteryof pages 6-7) |
| Genes/Proteins/Complexes | ToxR | transcriptional regulator | label only | Regulon controlling ompH expression in pressure response context (scheffer2023themysteryof pages 6-7) |
| Genes/Proteins/Complexes | pfaABCD operon | pathway gene set | KEGG:K18553/K18554/K18555/K18556 (candidate mapping) | Polyunsaturated fatty acid biosynthesis genes present in piezophilic Colwellia and linked to membrane adaptation (peoples2020distinctivegeneand pages 5-7, scheffer2023themysteryof pages 6-7) |
| Genes/Proteins/Complexes | delta-9 acyl-phospholipid desaturase | enzyme | EC:1.14.19.2 | Membrane lipid desaturase enriched/present in piezophilic Colwellia; candidate driver of increased unsaturation (peoples2020distinctivegeneand pages 5-7, peoples2020distinctivegeneand pages 9-11) |
| Genes/Proteins/Complexes | fatty acid cis/trans isomerase | enzyme | EC:5.2.1.5 | Present in piezosensitive Colwellia but absent in piezophiles; useful contrast node that may distinguish non-obligate strategies (peoples2020distinctivegeneand pages 5-7, peoples2020distinctivegeneand pages 9-11) |
| Genes/Proteins/Complexes | NADH dehydrogenase I (nuo operon) | respiratory complex | KEGG:K00330-K00346 | Respiratory complex present only in hadal piezophilic Colwellia; implicated in pressure-adapted respiration/energy conservation (peoples2020distinctivegeneand pages 5-7, peoples2020distinctivegeneand pages 1-2) |
| Genes/Proteins/Complexes | tad pilus operon | adhesion/pilus complex | label only | Piezophile-specific in Colwellia; candidate link to adhesion/extracellular structure under high pressure (peoples2020distinctivegeneand pages 1-2, peoples2020distinctivegeneand pages 7-9) |
| Genes/Proteins/Complexes | alanine dehydrogenase | enzyme | EC:1.4.1.1 | Piezophile-specific copy in Colwellia may support NADH/NAD+ homeostasis under pressure (peoples2020distinctivegeneand pages 1-2, peoples2020distinctivegeneand pages 7-9) |
| Genes/Proteins/Complexes | D-Ala-D-Ala ligase | enzyme | EC:6.3.2.4 | Extra copies in piezophiles; supports peptidoglycan/cell-wall biogenesis under high-pressure conditions (peoples2020distinctivegeneand pages 1-2, peoples2020distinctivegeneand pages 9-11) |
| Genes/Proteins/Complexes | SAM-dependent methyltransferase | enzyme/protein family | pfam:PF13659 | Piezophile-associated protein suggested to participate in tRNA modification and deep-sea adaptation (peoples2020distinctivegeneand pages 1-2, peoples2020distinctivegeneand pages 7-9) |
| Genes/Proteins/Complexes | argA | enzyme/gene | KEGG:K00620 | Arginine biosynthesis gene upregulated in 158 MPa transcriptomic response; candidate HHP stress-adaptation node (malas2024biologicalfunctionsat pages 1-2) |
| Genes/Proteins/Complexes | argB | enzyme/gene | KEGG:K00821 | Arginine biosynthesis gene upregulated under HHP (malas2024biologicalfunctionsat pages 1-2) |
| Genes/Proteins/Complexes | argC | enzyme/gene | KEGG:K00145 | Arginine biosynthesis gene upregulated under HHP (malas2024biologicalfunctionsat pages 1-2) |
| Genes/Proteins/Complexes | argF | enzyme/gene | KEGG:K00611 | Arginine biosynthesis gene upregulated under HHP (malas2024biologicalfunctionsat pages 1-2) |
| Genes/Proteins/Complexes | CspG cold-shock protein | protein | UniProtKB:P0A9X9 (generic bacterial homolog candidate) | Stress protein induced in 2024 HHP transcriptome study; candidate cross-stress adaptation node (malas2024biologicalfunctionsat pages 1-2) |
| Genes/Proteins/Complexes | superoxide dismutase | enzyme | EC:1.15.1.1 | Oxidative stress defense retained in piezophilic Colwellia (peoples2020distinctivegeneand pages 7-9) |
| Genes/Proteins/Complexes | catalase | enzyme | EC:1.11.1.6 | Oxidative stress defense retained in piezophilic Colwellia (peoples2020distinctivegeneand pages 7-9) |
| Genes/Proteins/Complexes | MCP methyl-accepting chemotaxis protein | signaling protein | GO:0006935 | Pressure-responsive chemotaxis component upregulated in some piezophiles (scheffer2023themysteryof pages 6-7) |
| Genes/Proteins/Complexes | CheACD / CheACDY | chemotaxis proteins | label only | Pressure-responsive chemotaxis/signaling modules implicated in adaptation (scheffer2023themysteryof pages 6-7) |
| Genes/Proteins/Complexes | flaB3 | flagellin/flagellar gene | label only | Flagellar gene required for full high-pressure growth in Desulfovibrio experiment (scheffer2023themysteryof pages 6-7) |
| Genes/Proteins/Complexes | fliD | flagellar cap protein | label only | Flagellar gene required for high-pressure growth in Desulfovibrio experiment (scheffer2023themysteryof pages 6-7) |
| Genes/Proteins/Complexes | fliA | sigma factor for flagellar genes | label only | Flagellar regulator required for high-pressure growth in Desulfovibrio experiment (scheffer2023themysteryof pages 6-7) |
| Metabolites/chemicals | unsaturated fatty acids | chemical class | CHEBI:51006 | Increased under pressure in many piezophiles; key membrane-fluidity adaptation node (scheffer2023themysteryof pages 6-7, tamby2023microbialmembranelipid pages 2-4) |
| Metabolites/chemicals | branched-chain fatty acids | chemical class | CHEBI:35819 | Often increased under HHP; alternative fluidity-maintenance strategy (tamby2023microbialmembranelipid pages 1-2) |
| Metabolites/chemicals | eicosapentaenoic acid (EPA, C20:5) | metabolite | CHEBI:28364 | Omega-3 PUFA repeatedly associated with HHP adaptation in marine bacteria (tamby2023microbialmembranelipid pages 2-4) |
| Metabolites/chemicals | docosahexaenoic acid (DHA, C22:6) | metabolite | CHEBI:28125 | Omega-3 PUFA increased under HHP in some deep-sea strains (tamby2023microbialmembranelipid pages 2-4) |
| Metabolites/chemicals | GDGT tetraethers | membrane lipid class | CHEBI:64716 (candidate) | Archaeal tetraether lipids implicated in membrane adaptation to pressure (tamby2023microbialmembranelipid pages 1-2, tamby2023microbialmembranelipid pages 2-4) |
| Metabolites/chemicals | glutamate | metabolite / piezolyte | CHEBI:29985 | Compatible solute that accumulates under pressure in several piezophiles (scheffer2023themysteryof pages 7-9, scheffer2023themysteryof pages 9-10) |
| Metabolites/chemicals | betaine | metabolite / piezolyte | CHEBI:17750 | Compatible solute accumulated under pressure and proposed to protect proteins (scheffer2023themysteryof pages 7-9, scheffer2023themysteryof pages 9-10) |
| Metabolites/chemicals | beta-hydroxybutyrate | metabolite / piezolyte | CHEBI:15996 | Produced only under high pressure in one cited example; candidate pressure-protective solute (scheffer2023themysteryof pages 7-9, scheffer2023themysteryof pages 9-10) |
| Metabolites/chemicals | trimethylamine N-oxide (TMAO) | metabolite | CHEBI:15724 | Can function as electron acceptor or piezolyte; role varies by taxon and should be curated cautiously (scheffer2023themysteryof pages 7-9, scheffer2023themysteryof pages 9-10) |
| Metabolites/chemicals | proline | metabolite / compatible solute | CHEBI:17203 | Increased strongly after high-pressure treatment in 2024 study; candidate osmolyte/piezolyte node (qiu2024metabolicadaptationsof pages 1-2) |
| Metabolites/chemicals | trehalose | metabolite | CHEBI:18150 | Differential metabolite under high-pressure treatment in 2024 study; candidate protective solute/carbohydrate reserve (qiu2024metabolicadaptationsof pages 5-7) |
| Metabolites/chemicals | UDP-glucose | metabolite | CHEBI:17211 | Accumulated under HHP in 2024 study, supporting increased cell-wall synthesis (qiu2024metabolicadaptationsof pages 1-2) |
| Pathways/modules | membrane lipid remodeling under HHP | pathway/module | GO:0006643 | Umbrella module for altered unsaturation/branching/headgroups to preserve membrane function (tamby2023microbialmembranelipid pages 1-2, tamby2023microbialmembranelipid pages 2-4) |
| Pathways/modules | polyunsaturated fatty acid biosynthesis | pathway/module | MetaCyc:PWY-6284 (candidate) | Biosynthetic module generating pressure-associated PUFAs such as EPA/DHA (tamby2023microbialmembranelipid pages 2-4, peoples2020distinctivegeneand pages 5-7) |
| Pathways/modules | arginine biosynthesis | pathway/module | KEGG:map00220 | Upregulated in 2024 HHP transcriptome response; candidate pressure-response pathway (malas2024biologicalfunctionsat pages 1-2) |
| Pathways/modules | peptidoglycan biosynthesis | pathway/module | KEGG:map00550 | Supported by D-Ala-D-Ala ligase enrichment and UDP-glucose/cell-wall synthesis signals (peoples2020distinctivegeneand pages 7-9, qiu2024metabolicadaptationsof pages 1-2) |
| Pathways/modules | respiratory chain reconfiguration under pressure | pathway/module | GO:0006119 | Pressure can alter use of NADH dehydrogenase and terminal oxidases; candidate energy adaptation process (scheffer2023themysteryof pages 7-9, peoples2020distinctivegeneand pages 5-7) |
| Pathways/modules | compatible solute accumulation / piezolyte response | pathway/module | GO:0015931 | Includes glutamate, betaine, beta-hydroxybutyrate, TMAO, proline, trehalose as candidate pressure-protective metabolites (scheffer2023themysteryof pages 7-9, scheffer2023themysteryof pages 9-10, qiu2024metabolicadaptationsof pages 5-7, qiu2024metabolicadaptationsof pages 1-2) |
| Pathways/modules | chemotaxis and motility response to pressure | pathway/module | KEGG:map02030; map02040 | Captures pressure-associated MCP/Che/flagellar responses (scheffer2023themysteryof pages 6-7) |
| Example taxa | Pyrococcus yayanosii CH1 | taxon | NCBITaxon:563177 | Foundational obligate piezophilic hyperthermophilic archaeon; optimal pressure ~52 MPa (michoud2016highhydrostaticpressure pages 1-2, scoma2021functionalgroupsin pages 5-6) |
| Example taxa | Colwellia marinimaniae MTCD1 | taxon | NCBITaxon:1942053 | Extreme obligate/hyperpiezophilic example with growth range 80–140 MPa and optimum 120 MPa (peoples2020distinctivegeneand pages 1-2, peoples2020distinctivegeneand media c39a23c1) |
| Example taxa | Colwellia sp. MT41 | taxon | label only | First known obligate psychropiezophile; optimum ~103 MPa and unable to grow below 35 MPa (peoples2020distinctivegeneand pages 1-2) |
| Example taxa | Pseudothermotoga elfii DSM9442 | taxon | NCBITaxon:651791 | Piezophilic but not obligate example; useful boundary comparator with optimum 20 MPa and growth at 0.1 MPa (roumagnac2020responsestothe pages 1-2) |


*Table: This table inventories candidate causal-graph nodes for obligate piezophily, grouped by biological type and grounded to stable identifiers where possible. It is useful for selecting curatable TraitMech nodes while distinguishing strong evidence-backed nodes from broader comparative or boundary-case concepts.*

---

## Evidence-backed candidate causal edges (triples)
The following artifact provides proposed subject–predicate–object edges with evidence snippets, DOI, URL, publication date, and curation notes.

| Edge ID | Subject | Predicate | Object | Evidence snippet (short quote) | Source (first author year, title) | DOI | URL | Publication date/month | Notes (certainty, taxon-specificity, assay conditions) |
|---|---|---|---|---|---|---|---|---|---|
| E1 | high hydrostatic pressure | increases requirement for | unsaturated/branched membrane lipids to maintain membrane fluidity | “the abundance of specific membrane lipids, such as those containing unsaturated and branched-chain fatty acids, rises with increasing HHP” | Tamby 2023, *Microbial membrane lipid adaptations to high hydrostatic pressure in the marine environment* | 10.3389/fmolb.2022.1058381 | https://doi.org/10.3389/fmolb.2022.1058381 | Jan 2023 | Strong review-level support; broad across marine piezophiles; mechanism framed as membrane adaptation/homeoviscous response rather than obligate-only specificity (tamby2023microbialmembranelipid pages 1-2, tamby2023microbialmembranelipid pages 2-4) |
| E2 | high hydrostatic pressure | induces increase in | omega-3 PUFAs (EPA C20:5, DHA C22:6) | “Piezophiles commonly increase fatty acyl chain unsaturation; polyunsaturated fatty acids (PUFAs) most associated with HHP adaptation are C20:5 and C22:6” | Tamby 2023, *Microbial membrane lipid adaptations to high hydrostatic pressure in the marine environment* | 10.3389/fmolb.2022.1058381 | https://doi.org/10.3389/fmolb.2022.1058381 | Jan 2023 | Strong but not universal; species-specific exceptions noted for Shewanella spp.; curate as common adaptation, not necessary/sufficient rule (tamby2023microbialmembranelipid pages 2-4) |
| E3 | high hydrostatic pressure | increases abundance of | OmpH porin | “outer membrane protein OmpH (ompH under toxR control) whose abundance increases ~10–100× between 0.1 and 28 MPa” | Scheffer 2023, *The Mystery of Piezophiles: Understudied Microorganisms from the Deep, Dark Subsurface* | 10.3390/microorganisms11071629 | https://doi.org/10.3390/microorganisms11071629 | Jun 2023 | Moderate strength; taxon-specific literature synthesis rather than obligate-specific universal mechanism; quantitative induction included (scheffer2023themysteryof pages 7-9) |
| E4 | ToxR | positively regulates | ompH expression under pressure response | “OmpH (ompH under toxR control)” | Scheffer 2023, *The Mystery of Piezophiles: Understudied Microorganisms from the Deep, Dark Subsurface* | 10.3390/microorganisms11071629 | https://doi.org/10.3390/microorganisms11071629 | Jun 2023 | Moderate; regulatory relation summarized in review; likely from specific bacterial systems, not universal across piezophiles (scheffer2023themysteryof pages 7-9, scheffer2023themysteryof pages 6-7) |
| E5 | piezophilic *Colwellia* | is associated with presence of | NADH dehydrogenase I (nuo operon) | “operons for a nuo dehydrogenase and a tad pilus only present in the piezophiles” | Peoples 2020, *Distinctive gene and protein characteristics of extremely piezophilic Colwellia* | 10.1186/s12864-020-07102-y | https://doi.org/10.1186/s12864-020-07102-y | Oct 2020 | Association evidence from comparative genomics; not direct perturbation/causation; strong within *Colwellia* only (peoples2020distinctivegeneand pages 1-2, peoples2020distinctivegeneand pages 5-7) |
| E6 | piezophilic *Colwellia* | is associated with presence of | tad pilus operon | “a tad pilus operon involved in adhesion is found only in piezophiles” | Peoples 2020, *Distinctive gene and protein characteristics of extremely piezophilic Colwellia* | 10.1186/s12864-020-07102-y | https://doi.org/10.1186/s12864-020-07102-y | Oct 2020 | Association evidence; candidate structural adaptation for adhesion/extracellular interaction under pressure; taxon-specific (peoples2020distinctivegeneand pages 7-9, peoples2020distinctivegeneand pages 1-2) |
| E7 | piezophilic *Colwellia* | encodes | delta-9 acyl-phospholipid desaturase | “all piezophiles encode delta-9 acyl-phospholipid desaturase and pfaABCD” | Peoples 2020, *Distinctive gene and protein characteristics of extremely piezophilic Colwellia* | 10.1186/s12864-020-07102-y | https://doi.org/10.1186/s12864-020-07102-y | Oct 2020 | Comparative-genomic association; supports membrane unsaturation module; note desaturase may also occur in some non-piezophilic *Colwellia* in broader discussion (peoples2020distinctivegeneand pages 5-7, peoples2020distinctivegeneand pages 9-11) |
| E8 | piezophilic *Colwellia* | encodes | pfaABCD PUFA biosynthesis genes | “all piezophiles encode delta-9 acyl-phospholipid desaturase and pfaABCD” | Peoples 2020, *Distinctive gene and protein characteristics of extremely piezophilic Colwellia* | 10.1186/s12864-020-07102-y | https://doi.org/10.1186/s12864-020-07102-y | Oct 2020 | Comparative-genomic association with membrane PUFA production; taxon-specific and not alone sufficient to define obligate piezophily (peoples2020distinctivegeneand pages 5-7) |
| E9 | piezosensitive *Colwellia* | encodes | fatty acid cis/trans isomerase | “a fatty acid cis/trans isomerase is encoded in all piezosensitive strains but absent in piezophiles” | Peoples 2020, *Distinctive gene and protein characteristics of extremely piezophilic Colwellia* | 10.1186/s12864-020-07102-y | https://doi.org/10.1186/s12864-020-07102-y | Oct 2020 | Negative association useful for boundary discrimination; should be curated cautiously because absence evidence is genus-comparative only (peoples2020distinctivegeneand pages 5-7, peoples2020distinctivegeneand pages 9-11) |
| E10 | high hydrostatic pressure | triggers accumulation of | glutamate, betaine, and β-hydroxybutyrate | “P. profundum accumulates glutamate, betaine and β-hydroxybutyrate at 20–30 MPa” | Scheffer 2023, *The Mystery of Piezophiles: Understudied Microorganisms from the Deep, Dark Subsurface* | 10.3390/microorganisms11071629 | https://doi.org/10.3390/microorganisms11071629 | Jun 2023 | Moderate; specific to cited taxa and pressure range 20–30 MPa; supports compatible-solute/piezolyte module (scheffer2023themysteryof pages 9-10) |
| E11 | β-hydroxybutyrate | is produced only under | high hydrostatic pressure | “β-hydroxybutyrate was produced only under high pressure” | Scheffer 2023, *The Mystery of Piezophiles: Understudied Microorganisms from the Deep, Dark Subsurface* | 10.3390/microorganisms11071629 | https://doi.org/10.3390/microorganisms11071629 | Jun 2023 | Specific to example system and dependent on glucose availability; useful but narrow (scheffer2023themysteryof pages 9-10) |
| E12 | TMAO | functions as | piezolyte and/or pressure-linked metabolite | “TMAO is noted as used energetically or as a piezolyte” | Scheffer 2023, *The Mystery of Piezophiles: Understudied Microorganisms from the Deep, Dark Subsurface* | 10.3390/microorganisms11071629 | https://doi.org/10.3390/microorganisms11071629 | Jun 2023 | Uncertain multifunctional role; taxon-specific distinction between electron acceptor versus piezolyte should be flagged in curation (scheffer2023themysteryof pages 9-10) |
| E13 | high-pressure treatment (30 MPa, 4°C, 7 d) | increases | proline and other differential metabolites | “significant shifts in amino acid, carbohydrate, and lipid metabolism under high pressure” and amino acids included “proline” | Qiu 2024, *Metabolic adaptations of Microbacterium sediminis YLB-01 in deep-sea high-pressure environments* | 10.1007/s00253-023-12906-5 | https://doi.org/10.1007/s00253-023-12906-5 | Jan 2024 | Moderate; *Microbacterium sediminis* is not obligately piezophilic; assay was 30 MPa at 4°C for 7 days; supports candidate compatible-solute node but indirect for obligate trait (qiu2024metabolicadaptationsof pages 5-7, qiu2024metabolicadaptationsof pages 1-2) |
| E14 | high hydrostatic pressure | alters | respiratory chain components in *Shewanella* | “at 60 MPa a membrane-bound cytochrome c-551 and a quinol oxidase expressed only at high pressure” | Scheffer 2023, *The Mystery of Piezophiles: Understudied Microorganisms from the Deep, Dark Subsurface* | 10.3390/microorganisms11071629 | https://doi.org/10.3390/microorganisms11071629 | Jun 2023 | Moderate; respiratory switching is taxon-specific but mechanistically relevant to pressure-adapted energy metabolism (scheffer2023themysteryof pages 7-9) |
| E15 | high hydrostatic pressure | increases expression of | Hmc complex genes in *Desulfovibrio* | “In Desulfovibrio, Hmc complex genes increase under pressure” | Scheffer 2023, *The Mystery of Piezophiles: Understudied Microorganisms from the Deep, Dark Subsurface* | 10.3390/microorganisms11071629 | https://doi.org/10.3390/microorganisms11071629 | Jun 2023 | Moderate; genus-specific respiratory/electron-transfer response; useful as candidate energy-metabolism edge (scheffer2023themysteryof pages 7-9) |
| E16 | high hydrostatic pressure | upregulates | chemotaxis proteins (MCP, CheACD/CheACDY) | “chemotaxis and signal proteins (MCP; CheACD/CheACDY) are upregulated” | Scheffer 2023, *The Mystery of Piezophiles: Understudied Microorganisms from the Deep, Dark Subsurface* | 10.3390/microorganisms11071629 | https://doi.org/10.3390/microorganisms11071629 | Jun 2023 | Moderate; repeated across reviewed taxa but not universal; supports motility/signaling node (scheffer2023themysteryof pages 6-7) |
| E17 | loss of flagellar genes (*flaB3*, *fliD*, *fliA*) | decreases | growth under high pressure | “ΔflaB3, ΔfliD, ΔfliA mutants become non-motile and show reduced growth” | Scheffer 2023, *The Mystery of Piezophiles: Understudied Microorganisms from the Deep, Dark Subsurface* | 10.3390/microorganisms11071629 | https://doi.org/10.3390/microorganisms11071629 | Jun 2023 | Stronger causal evidence due to mutant phenotype, but from *Desulfovibrio alaskensis* and thus taxon-specific (scheffer2023themysteryof pages 6-7) |
| E18 | high hydrostatic pressure | increases | cell chaining in *Pseudothermotoga elfii* DSM9442 | “44% of cells is chained when grown at 40 MPa” | Roumagnac 2020, *Responses to the Hydrostatic Pressure of Surface and Subsurface Strains of Pseudothermotoga elfii* | 10.3389/fmicb.2020.588771 | https://doi.org/10.3389/fmicb.2020.588771 | Dec 2020 | Quantitative phenotype; piezophilic boundary-case strain, not obligate; growth tested 0.1–50 MPa (roumagnac2020responsestothe pages 1-2) |
| E19 | cell chaining in *Pseudothermotoga elfii* DSM9442 | acts as | protective mechanism under pressure | “the viability of the chained cells increases with the increase in the hydrostatic pressure, indicating that chain formation is a protective mechanism” | Roumagnac 2020, *Responses to the Hydrostatic Pressure of Surface and Subsurface Strains of Pseudothermotoga elfii* | 10.3389/fmicb.2020.588771 | https://doi.org/10.3389/fmicb.2020.588771 | Dec 2020 | Explicit causal interpretation by authors; should still be marked taxon-specific and assay-specific (roumagnac2020responsestothe pages 1-2) |
| E20 | 158 MPa exposure in *Shewanella oneidensis* MR-1 | regulates | 264 genes | “264 genes regulated in response to short-term HHP” | Malas 2024, *Biological functions at high pressure: transcriptome response of Shewanella oneidensis MR-1 to hydrostatic pressure relevant to Titan and other icy ocean worlds* | 10.3389/fmicb.2024.1293928 | https://doi.org/10.3389/fmicb.2024.1293928 | Feb 2024 | Strong transcriptomic response but from non-piezophilic model under extreme assay (158 MPa, 15 min / 2 h); useful recent evidence for pressure-response modules (malas2024biologicalfunctionsat pages 1-2, malas2024biologicalfunctionsat pages 2-3) |
| E21 | 158 MPa exposure in *Shewanella oneidensis* MR-1 | upregulates | arginine biosynthesis genes (*argA, argB, argC, argF*) | “upregulation of arginine biosynthesis genes (argA, argB, argC, argF)” | Malas 2024, *Biological functions at high pressure: transcriptome response of Shewanella oneidensis MR-1 to hydrostatic pressure relevant to Titan and other icy ocean worlds* | 10.3389/fmicb.2024.1293928 | https://doi.org/10.3389/fmicb.2024.1293928 | Feb 2024 | Recent mechanistic evidence; model system rather than obligate piezophile; good candidate pathway edge with assay details retained (malas2024biologicalfunctionsat pages 1-2) |
| E22 | 158 MPa exposure in *Shewanella oneidensis* MR-1 | induces | cold-shock protein CspG and antioxidant defense genes | “induction of stress-protection systems such as cold-shock protein CspG and antioxidant defense genes” | Malas 2024, *Biological functions at high pressure: transcriptome response of Shewanella oneidensis MR-1 to hydrostatic pressure relevant to Titan and other icy ocean worlds* | 10.3389/fmicb.2024.1293928 | https://doi.org/10.3389/fmicb.2024.1293928 | Feb 2024 | Recent stress-response evidence; model-system inference to obligate piezophily should be cautious (malas2024biologicalfunctionsat pages 1-2) |
| E23 | obligate piezophiles / hyperpiezophiles | unable to grow at | ambient pressure (0.1 MPa) | “obligate piezophiles (or hyperpiezophiles) [are] unable to grow at ambient pressure” | Scoma 2021, *Functional groups in microbial ecology: updated definitions of piezophiles as suggested by hydrostatic pressure dependence on temperature* | 10.1038/s41396-021-00930-0 | https://doi.org/10.1038/s41396-021-00930-0 | Mar 2021 | Core trait-definition edge; strongest direct scope evidence for TraitMech phenotype boundary (scoma2021functionalgroupsin pages 1-2) |
| E24 | *Colwellia marinimaniae* MTCD1 | grows within | 80–140 MPa and excludes ambient pressure growth | “growth range of 80–140 MPa (optimum, 120 MPa)” | Peoples 2020, *Distinctive gene and protein characteristics of extremely piezophilic Colwellia* | 10.1186/s12864-020-07102-y | https://doi.org/10.1186/s12864-020-07102-y | Oct 2020 | Species-example edge supporting obligate/hyperpiezophily; range summarized from species literature and figure context (peoples2020distinctivegeneand pages 1-2, peoples2020distinctivegeneand media c39a23c1) |
| E25 | *Pyrococcus yayanosii* CH1 | is an example of | obligate piezophilic growth requiring elevated pressure | “the first and only described obligate piezophilic hyperthermophilic archaeon” | Michoud 2016, *High hydrostatic pressure adaptive strategies in an obligate piezophile Pyrococcus yayanosii* | 10.1038/srep27289 | https://doi.org/10.1038/srep27289 | Jun 2016 | Foundational species example; optimal pressure ~52 MPa in study, with 20 and 80 MPa treated as stressful conditions (michoud2016highhydrostaticpressure pages 1-2, scoma2021functionalgroupsin pages 5-6) |


*Table: This table lists evidence-backed subject-predicate-object edges relevant to curating the TraitMech graph for obligate piezophily. It combines direct trait-definition edges with mechanistic, taxon-specific, and assay-specific adaptations that should be prioritized or flagged cautiously during curation.*

**Image-backed evidence**: Peoples et al. 2020 figures include a visual summary of MTCD1 pressure optimum and a gene presence/absence table (nuo/tad/desaturase etc.), supporting organism-level and comparative-genomics nodes/edges. (peoples2020distinctivegeneand media c39a23c1, peoples2020distinctivegeneand media 9952b9a8)

---

## Warnings / curation notes (do not overgeneralize)
1) **Association ≠ causation**: Many gene differences in *Colwellia* are comparative-genomic associations (presence/absence) rather than direct demonstrations that a gene is required for obligate piezophily. Curate these edges as **“associated with”** unless functional tests are available. (peoples2020distinctivegeneand pages 1-2, peoples2020distinctivegeneand pages 5-7)
2) **Non-universality of membrane responses**: PUFA/unsaturation trends are common but not universal; avoid curating them as necessary/sufficient conditions for obligate piezophily. (tamby2023microbialmembranelipid pages 2-4)
3) **TMAO multifunctionality**: TMAO may serve as an electron acceptor or a piezolyte depending on organism and genomic context; edges involving TMAO should be marked **uncertain/taxon-specific**. (scheffer2023themysteryof pages 9-10)
4) **Model-system pressure tolerance vs obligate requirement**: 2024 MR‑1 (158 MPa) and 2024 *Microbacterium* studies provide valuable modern mechanistic modules but are not obligate piezophile demonstrations; curate them as **pressure-response evidence**, not direct obligate trait evidence. (malas2024biologicalfunctionsat pages 1-2, qiu2024metabolicadaptationsof pages 1-2)

---

## DOI-first bibliography (with URLs and publication dates)
- **Scoma A.** Functional groups in microbial ecology: updated definitions of piezophiles as suggested by hydrostatic pressure dependence on temperature. *The ISME Journal.* **Mar 2021**. DOI: **10.1038/s41396-021-00930-0**. URL: https://doi.org/10.1038/s41396-021-00930-0 (scoma2021functionalgroupsin pages 1-2, scoma2021functionalgroupsin pages 5-6)
- **Tamby A, Sinninghe Damsté JS, Villanueva L.** Microbial membrane lipid adaptations to high hydrostatic pressure in the marine environment. *Frontiers in Molecular Biosciences.* **Jan 2023**. DOI: **10.3389/fmolb.2022.1058381**. URL: https://doi.org/10.3389/fmolb.2022.1058381 (tamby2023microbialmembranelipid pages 1-2, tamby2023microbialmembranelipid pages 2-4)
- **Scheffer G, Gieg LM.** The Mystery of Piezophiles: Understudied Microorganisms from the Deep, Dark Subsurface. *Microorganisms.* **Jun 2023**. DOI: **10.3390/microorganisms11071629**. URL: https://doi.org/10.3390/microorganisms11071629 (scheffer2023themysteryof pages 7-9, scheffer2023themysteryof pages 6-7)
- **Malas J, Russo DC, Bollengier O, et al.** Biological functions at high pressure: transcriptome response of *Shewanella oneidensis* MR‑1 to hydrostatic pressure relevant to Titan and other icy ocean worlds. *Frontiers in Microbiology.* **Feb 2024**. DOI: **10.3389/fmicb.2024.1293928**. URL: https://doi.org/10.3389/fmicb.2024.1293928 (malas2024biologicalfunctionsat pages 1-2)
- **Qiu X, Hu X‑M, Tang X‑X, et al.** Metabolic adaptations of *Microbacterium sediminis* YLB‑01 in deep-sea high-pressure environments. *Applied Microbiology and Biotechnology.* **Jan 2024**. DOI: **10.1007/s00253-023-12906-5**. URL: https://doi.org/10.1007/s00253-023-12906-5 (qiu2024metabolicadaptationsof pages 1-2, qiu2024metabolicadaptationsof pages 5-7)
- **Peoples LM, Kyaw TS, Ugalde JA, et al.** Distinctive gene and protein characteristics of extremely piezophilic *Colwellia*. *BMC Genomics.* **Oct 2020**. DOI: **10.1186/s12864-020-07102-y**. URL: https://doi.org/10.1186/s12864-020-07102-y (peoples2020distinctivegeneand pages 1-2, peoples2020distinctivegeneand media c39a23c1)
- **Roumagnac M, Pradel N, Bartoli M, et al.** Responses to the Hydrostatic Pressure of Surface and Subsurface Strains of *Pseudothermotoga elfii*… *Frontiers in Microbiology.* **Dec 2020**. DOI: **10.3389/fmicb.2020.588771**. URL: https://doi.org/10.3389/fmicb.2020.588771 (roumagnac2020responsestothe pages 1-2)
- **Michoud G, Jebbar M.** High hydrostatic pressure adaptive strategies in an obligate piezophile *Pyrococcus yayanosii*. *Scientific Reports.* **Jun 2016**. DOI: **10.1038/srep27289**. URL: https://doi.org/10.1038/srep27289 (michoud2016highhydrostaticpressure pages 1-2)


References

1. (scoma2021functionalgroupsin pages 1-2): Alberto Scoma. Functional groups in microbial ecology: updated definitions of piezophiles as suggested by hydrostatic pressure dependence on temperature. The ISME Journal, 15:1871-1878, Mar 2021. URL: https://doi.org/10.1038/s41396-021-00930-0, doi:10.1038/s41396-021-00930-0. This article has 18 citations.

2. (scoma2021functionalgroupsin pages 2-3): Alberto Scoma. Functional groups in microbial ecology: updated definitions of piezophiles as suggested by hydrostatic pressure dependence on temperature. The ISME Journal, 15:1871-1878, Mar 2021. URL: https://doi.org/10.1038/s41396-021-00930-0, doi:10.1038/s41396-021-00930-0. This article has 18 citations.

3. (scoma2021functionalgroupsin pages 5-6): Alberto Scoma. Functional groups in microbial ecology: updated definitions of piezophiles as suggested by hydrostatic pressure dependence on temperature. The ISME Journal, 15:1871-1878, Mar 2021. URL: https://doi.org/10.1038/s41396-021-00930-0, doi:10.1038/s41396-021-00930-0. This article has 18 citations.

4. (roumagnac2020responsestothe pages 1-2): Marie Roumagnac, Nathalie Pradel, Manon Bartoli, Marc Garel, Aaron A. Jones, Fabrice Armougom, Romain Fenouil, Christian Tamburini, Bernard Ollivier, Zarath M. Summers, and Alain Dolla. Responses to the hydrostatic pressure of surface and subsurface strains of pseudothermotoga elfii revealing the piezophilic nature of the strain originating from an oil-producing well. Frontiers in Microbiology, Dec 2020. URL: https://doi.org/10.3389/fmicb.2020.588771, doi:10.3389/fmicb.2020.588771. This article has 20 citations and is from a peer-reviewed journal.

5. (peoples2020distinctivegeneand pages 1-2): Logan M. Peoples, Than S. Kyaw, Juan A. Ugalde, Kelli K. Mullane, Roger A. Chastain, A. Aristides Yayanos, Masataka Kusube, Barbara A. Methé, and Douglas H. Bartlett. Distinctive gene and protein characteristics of extremely piezophilic colwellia. BMC Genomics, Oct 2020. URL: https://doi.org/10.1186/s12864-020-07102-y, doi:10.1186/s12864-020-07102-y. This article has 53 citations and is from a peer-reviewed journal.

6. (peoples2020distinctivegeneand media c39a23c1): Logan M. Peoples, Than S. Kyaw, Juan A. Ugalde, Kelli K. Mullane, Roger A. Chastain, A. Aristides Yayanos, Masataka Kusube, Barbara A. Methé, and Douglas H. Bartlett. Distinctive gene and protein characteristics of extremely piezophilic colwellia. BMC Genomics, Oct 2020. URL: https://doi.org/10.1186/s12864-020-07102-y, doi:10.1186/s12864-020-07102-y. This article has 53 citations and is from a peer-reviewed journal.

7. (michoud2016highhydrostaticpressure pages 1-2): Grégoire Michoud and Mohamed Jebbar. High hydrostatic pressure adaptive strategies in an obligate piezophile pyrococcus yayanosii. Scientific Reports, Jun 2016. URL: https://doi.org/10.1038/srep27289, doi:10.1038/srep27289. This article has 89 citations and is from a peer-reviewed journal.

8. (tamby2023microbialmembranelipid pages 1-2): Anandi Tamby, Jaap S. Sinninghe Damsté, and Laura Villanueva. Microbial membrane lipid adaptations to high hydrostatic pressure in the marine environment. Frontiers in Molecular Biosciences, Jan 2023. URL: https://doi.org/10.3389/fmolb.2022.1058381, doi:10.3389/fmolb.2022.1058381. This article has 47 citations.

9. (scheffer2023themysteryof pages 6-7): Gabrielle Scheffer and Lisa M. Gieg. The mystery of piezophiles: understudied microorganisms from the deep, dark subsurface. Microorganisms, 11:1629, Jun 2023. URL: https://doi.org/10.3390/microorganisms11071629, doi:10.3390/microorganisms11071629. This article has 31 citations.

10. (tamby2023microbialmembranelipid pages 2-4): Anandi Tamby, Jaap S. Sinninghe Damsté, and Laura Villanueva. Microbial membrane lipid adaptations to high hydrostatic pressure in the marine environment. Frontiers in Molecular Biosciences, Jan 2023. URL: https://doi.org/10.3389/fmolb.2022.1058381, doi:10.3389/fmolb.2022.1058381. This article has 47 citations.

11. (scheffer2023themysteryof pages 10-12): Gabrielle Scheffer and Lisa M. Gieg. The mystery of piezophiles: understudied microorganisms from the deep, dark subsurface. Microorganisms, 11:1629, Jun 2023. URL: https://doi.org/10.3390/microorganisms11071629, doi:10.3390/microorganisms11071629. This article has 31 citations.

12. (malas2024biologicalfunctionsat pages 1-2): Judy Malas, Daniel C. Russo, Olivier Bollengier, Michael J. Malaska, Rosaly M. C. Lopes, Fabien Kenig, and D'Arcy R. Meyer-Dombard. Biological functions at high pressure: transcriptome response of shewanella oneidensis mr-1 to hydrostatic pressure relevant to titan and other icy ocean worlds. Frontiers in Microbiology, Feb 2024. URL: https://doi.org/10.3389/fmicb.2024.1293928, doi:10.3389/fmicb.2024.1293928. This article has 7 citations and is from a peer-reviewed journal.

13. (scheffer2023themysteryof pages 7-9): Gabrielle Scheffer and Lisa M. Gieg. The mystery of piezophiles: understudied microorganisms from the deep, dark subsurface. Microorganisms, 11:1629, Jun 2023. URL: https://doi.org/10.3390/microorganisms11071629, doi:10.3390/microorganisms11071629. This article has 31 citations.

14. (scheffer2023themysteryof pages 9-10): Gabrielle Scheffer and Lisa M. Gieg. The mystery of piezophiles: understudied microorganisms from the deep, dark subsurface. Microorganisms, 11:1629, Jun 2023. URL: https://doi.org/10.3390/microorganisms11071629, doi:10.3390/microorganisms11071629. This article has 31 citations.

15. (malas2024biologicalfunctionsat pages 12-13): Judy Malas, Daniel C. Russo, Olivier Bollengier, Michael J. Malaska, Rosaly M. C. Lopes, Fabien Kenig, and D'Arcy R. Meyer-Dombard. Biological functions at high pressure: transcriptome response of shewanella oneidensis mr-1 to hydrostatic pressure relevant to titan and other icy ocean worlds. Frontiers in Microbiology, Feb 2024. URL: https://doi.org/10.3389/fmicb.2024.1293928, doi:10.3389/fmicb.2024.1293928. This article has 7 citations and is from a peer-reviewed journal.

16. (qiu2024metabolicadaptationsof pages 5-7): Xu Qiu, Xiao-Min Hu, Xi-Xiang Tang, Cai-Hua Huang, Hua-Hua Jian, and Dong-Hai Lin. Metabolic adaptations of microbacterium sediminis ylb-01 in deep-sea high-pressure environments. Applied Microbiology and Biotechnology, 108:1-15, Jan 2024. URL: https://doi.org/10.1007/s00253-023-12906-5, doi:10.1007/s00253-023-12906-5. This article has 9 citations and is from a domain leading peer-reviewed journal.

17. (qiu2024metabolicadaptationsof pages 1-2): Xu Qiu, Xiao-Min Hu, Xi-Xiang Tang, Cai-Hua Huang, Hua-Hua Jian, and Dong-Hai Lin. Metabolic adaptations of microbacterium sediminis ylb-01 in deep-sea high-pressure environments. Applied Microbiology and Biotechnology, 108:1-15, Jan 2024. URL: https://doi.org/10.1007/s00253-023-12906-5, doi:10.1007/s00253-023-12906-5. This article has 9 citations and is from a domain leading peer-reviewed journal.

18. (peoples2020distinctivegeneand pages 5-7): Logan M. Peoples, Than S. Kyaw, Juan A. Ugalde, Kelli K. Mullane, Roger A. Chastain, A. Aristides Yayanos, Masataka Kusube, Barbara A. Methé, and Douglas H. Bartlett. Distinctive gene and protein characteristics of extremely piezophilic colwellia. BMC Genomics, Oct 2020. URL: https://doi.org/10.1186/s12864-020-07102-y, doi:10.1186/s12864-020-07102-y. This article has 53 citations and is from a peer-reviewed journal.

19. (malas2024biologicalfunctionsat pages 2-3): Judy Malas, Daniel C. Russo, Olivier Bollengier, Michael J. Malaska, Rosaly M. C. Lopes, Fabien Kenig, and D'Arcy R. Meyer-Dombard. Biological functions at high pressure: transcriptome response of shewanella oneidensis mr-1 to hydrostatic pressure relevant to titan and other icy ocean worlds. Frontiers in Microbiology, Feb 2024. URL: https://doi.org/10.3389/fmicb.2024.1293928, doi:10.3389/fmicb.2024.1293928. This article has 7 citations and is from a peer-reviewed journal.

20. (peoples2020distinctivegeneand pages 7-9): Logan M. Peoples, Than S. Kyaw, Juan A. Ugalde, Kelli K. Mullane, Roger A. Chastain, A. Aristides Yayanos, Masataka Kusube, Barbara A. Methé, and Douglas H. Bartlett. Distinctive gene and protein characteristics of extremely piezophilic colwellia. BMC Genomics, Oct 2020. URL: https://doi.org/10.1186/s12864-020-07102-y, doi:10.1186/s12864-020-07102-y. This article has 53 citations and is from a peer-reviewed journal.

21. (peoples2020distinctivegeneand pages 4-5): Logan M. Peoples, Than S. Kyaw, Juan A. Ugalde, Kelli K. Mullane, Roger A. Chastain, A. Aristides Yayanos, Masataka Kusube, Barbara A. Methé, and Douglas H. Bartlett. Distinctive gene and protein characteristics of extremely piezophilic colwellia. BMC Genomics, Oct 2020. URL: https://doi.org/10.1186/s12864-020-07102-y, doi:10.1186/s12864-020-07102-y. This article has 53 citations and is from a peer-reviewed journal.

22. (peoples2020distinctivegeneand pages 9-11): Logan M. Peoples, Than S. Kyaw, Juan A. Ugalde, Kelli K. Mullane, Roger A. Chastain, A. Aristides Yayanos, Masataka Kusube, Barbara A. Methé, and Douglas H. Bartlett. Distinctive gene and protein characteristics of extremely piezophilic colwellia. BMC Genomics, Oct 2020. URL: https://doi.org/10.1186/s12864-020-07102-y, doi:10.1186/s12864-020-07102-y. This article has 53 citations and is from a peer-reviewed journal.

23. (peoples2020distinctivegeneand media 9952b9a8): Logan M. Peoples, Than S. Kyaw, Juan A. Ugalde, Kelli K. Mullane, Roger A. Chastain, A. Aristides Yayanos, Masataka Kusube, Barbara A. Methé, and Douglas H. Bartlett. Distinctive gene and protein characteristics of extremely piezophilic colwellia. BMC Genomics, Oct 2020. URL: https://doi.org/10.1186/s12864-020-07102-y, doi:10.1186/s12864-020-07102-y. This article has 53 citations and is from a peer-reviewed journal.