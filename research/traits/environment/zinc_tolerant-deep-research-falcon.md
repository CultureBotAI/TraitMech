---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T02:55:18.492205'
end_time: '2026-06-18T03:05:44.515005'
duration_seconds: 626.02
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: zinc tolerant
  trait_identifier: traitmech:000014
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: zinc_tolerant
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A metal tolerance in which an organism grows in the presence of elevated
    zinc (Zn2+) concentrations, typically via cation-efflux resistance systems such
    as the czc determinant.
  parent_traits: traitmech:000012
  synonyms: ''
  evidence_summary: 'DOI:10.1111/j.1365-2958.2009.06792.x: CzcP exports transition
    metals Zn(2+), Cd(2+) and Co(2+) (The cobalt-zinc-cadmium (czc) efflux system
    of Cupriavidus metallidurans confers zinc resistance.) | DOI:10.3389/fmicb.2020.00047:
    C. metallidurans BS1 conferred resistance to Zn2+ displaying a MIC of 20 mM, Cd2+
    (2.5 mM), Co2+ (20mM), Ni2+ (8 mM), As3+ (3.5 mM), Cu2+ (5 mM), Au3+ (1 uM) and
    Pb2+ (1.7 mM) (Organism example: Cupriavidus metallidurans BS1 tolerates zinc
    to a MIC of 20 mM.)'
  causal_graph_summary: 'zinc_tolerance_czc_efflux: 4 nodes, 3 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 24
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** zinc tolerant
- **METPO identifier:** traitmech:000014
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metal tolerance in which an organism grows in the presence of elevated zinc (Zn2+) concentrations, typically via cation-efflux resistance systems such as the czc determinant.
- **Parent traits:** traitmech:000012
- **Synonyms:** 
- **Existing evidence:** DOI:10.1111/j.1365-2958.2009.06792.x: CzcP exports transition metals Zn(2+), Cd(2+) and Co(2+) (The cobalt-zinc-cadmium (czc) efflux system of Cupriavidus metallidurans confers zinc resistance.) | DOI:10.3389/fmicb.2020.00047: C. metallidurans BS1 conferred resistance to Zn2+ displaying a MIC of 20 mM, Cd2+ (2.5 mM), Co2+ (20mM), Ni2+ (8 mM), As3+ (3.5 mM), Cu2+ (5 mM), Au3+ (1 uM) and Pb2+ (1.7 mM) (Organism example: Cupriavidus metallidurans BS1 tolerates zinc to a MIC of 20 mM.)
- **Existing causal graph summary:** zinc_tolerance_czc_efflux: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **zinc tolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/zinc_tolerant.yaml`.

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
- **Trait label:** zinc tolerant
- **METPO identifier:** traitmech:000014
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metal tolerance in which an organism grows in the presence of elevated zinc (Zn2+) concentrations, typically via cation-efflux resistance systems such as the czc determinant.
- **Parent traits:** traitmech:000012
- **Synonyms:** 
- **Existing evidence:** DOI:10.1111/j.1365-2958.2009.06792.x: CzcP exports transition metals Zn(2+), Cd(2+) and Co(2+) (The cobalt-zinc-cadmium (czc) efflux system of Cupriavidus metallidurans confers zinc resistance.) | DOI:10.3389/fmicb.2020.00047: C. metallidurans BS1 conferred resistance to Zn2+ displaying a MIC of 20 mM, Cd2+ (2.5 mM), Co2+ (20mM), Ni2+ (8 mM), As3+ (3.5 mM), Cu2+ (5 mM), Au3+ (1 uM) and Pb2+ (1.7 mM) (Organism example: Cupriavidus metallidurans BS1 tolerates zinc to a MIC of 20 mM.)
- **Existing causal graph summary:** zinc_tolerance_czc_efflux: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **zinc tolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/zinc_tolerant.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **zinc tolerant** (traitmech:000014)

### Executive scope summary
The **zinc tolerant** trait (METPO: traitmech:000014) should be curated as a **growth/viability phenotype in elevated extracellular Zn(II)** relative to a comparator condition or strain, typically quantified by **dose–response growth curves (IC50)** or **MIC assays**. In the best-supported mechanistic model (*Cupriavidus metallidurans*), zinc tolerance is explained by a **layered zinc homeostasis network** whose core is a **flow equilibrium** of zinc import, cytoplasmic buffering, and efflux; zinc resistance emerges when efflux capacity and buffering prevent toxic zinc accumulation and mis-metalation. (nies2024aflowequilibrium pages 1-3, schulz2024theeffluxsystem pages 1-3)

A key boundary for curation is separating:
1) **Excess-Zn tolerance (this trait)**: primarily **efflux/export** systems (e.g., ZntA, CzcCBA, CdfX) and their regulation; versus
2) **Zinc-starvation homeostasis**: importer derepression (e.g., Zur→zupT) that increases uptake under low zinc; and
3) **Zn removal/biosorption**: environmental engineering endpoints that may occur even in strains with modest growth tolerance and does not necessarily imply this trait. (schulz2024theeffluxsystem pages 9-12, pagnucco2023metaltoleranceand pages 3-4)

---

## 1. Key concepts and definitions (current understanding)

### 1.1 Trait definition (assay-observed phenotype)
**Zinc tolerant** organisms can maintain growth when exposed to elevated Zn(II). Empirically:
- In *C. metallidurans* studies, zinc resistance is quantified by **IC50** from growth curves; for example, zinc IC50 differs strongly depending on presence of plasmid-borne resistance determinants (see below). (nies2024aflowequilibrium pages 1-3)
- In environmental isolate screening, **MIC** is explicitly defined as “**the lowest concentration of the metal that inhibited bacterial growth after an incubation of 24 h**,” assessed by OD measurements (OD595). (pagnucco2023metaltoleranceand pages 2-3)

### 1.2 Mechanistic definition (what “tolerance” means biologically)
A curation-friendly mechanistic framing is that zinc tolerance requires:
- **Efflux/export capacity** for Zn(II) (often P-type ATPases, CDF exporters, and RND tripartite efflux), plus
- **Regulatory systems** that activate efflux when zinc rises, and
- **Cytoplasmic metal-binding/buffering components** (e.g., glutathione, polyphosphate) that shape intracellular zinc pools and kinetics. (nies2024aflowequilibrium pages 1-3, schulz2024theeffluxsystem pages 9-12)

In *C. metallidurans*, zinc homeostasis is described as a **“flow equilibrium”**: simultaneous uptake and efflux combined with cytoplasmic binding components maintain steady zinc turnover and cellular content. (nies2024aflowequilibrium pages 1-3)

### 1.3 Boundary cases (distinguish from nearby traits)
- **Zinc homeostasis under starvation** (not zinc tolerant per se): Under low zinc, the regulator **Zur** derepresses **zupT** (ZIP-family importer), increasing uptake; this is mechanistically distinct from survival under zinc excess and should not be conflated with tolerance mechanisms. (schulz2024theeffluxsystem pages 9-12)
- **Multi-metal resistance vs zinc-specific tolerance**: Many systems (e.g., CzcCBA) export multiple metals (Co/Zn/Cd). Curate edges carefully as Zn tolerance may be a **co-selected phenotype** rather than zinc-specific adaptation. (nies2024aflowequilibrium pages 20-22)
- **Biosorption/removal vs tolerance**: Environmental isolates can remove Zn(II) from solution via cell surface interactions/EPS even when their Zn MICs are lower than other isolates; thus, “Zn removal” is not equivalent to “Zn tolerant growth.” (pagnucco2023metaltoleranceand pages 9-10)

---

## 2. Recent developments and latest research (prioritize 2023–2024)

### 2.1 2024: Quantitative “flow equilibrium” model of zinc handling (*C. metallidurans*)
Nies et al. (2024, *Journal of Bacteriology*) used **pulse–chase experiments with 65Zn and 67Zn** to demonstrate continuous turnover and to quantify uptake/efflux contributors. They report multiple quantitative parameters relevant to curation and assay design:
- Zn uptake kinetics (reported Km and vmax for uptake). (nies2024aflowequilibrium pages 1-3)
- Media zinc was quantified/controlled (e.g., adjusted to 200 nM in some experiments) and zinc export measured during chase after induction. (nies2024aflowequilibrium pages 20-22)
- A clear genotype-to-phenotype zinc tolerance shift due to plasmid-borne determinants: **IC50 ~1 mM (AE104) vs 3.4 mM (with pMOL30)**. (nies2024aflowequilibrium pages 1-3)
These results support a causal interpretation that zinc tolerance is an emergent property of interacting import, buffering, and efflux systems, not a single-gene phenotype. (nies2024aflowequilibrium pages 1-3)

### 2.2 2024: Discovery/characterization of a backup Zn exporter (CdfX) when ZntA is impaired
Schulz et al. (2024, *Journal of Bacteriology*) demonstrate that **CdfX (CDF-family)** provides residual zinc efflux in a strain deleted for previously known efflux systems and that deleting **cdfX** further reduces zinc resistance in that background. (schulz2024theeffluxsystem pages 1-3)
Key regulatory finding for curation:
- **ZntR (MerR-type)** mediates **zinc- and cadmium-dependent upregulation of cdfX**. (schulz2024theeffluxsystem pages 12-14)
This adds a new node/edge to zinc tolerance graphs beyond the canonical ZntA/CzcCBA framework. (schulz2024theeffluxsystem pages 1-3)

### 2.3 2024: Regulatory thresholds for activating key efflux
Schulz et al. report a quantitative activation threshold:
- “**At external zinc concentrations above 200 nM … expression of the zntA gene … is upregulated**.” (schulz2024theeffluxsystem pages 9-12)
This provides a strong, curatable **environment→regulation** edge linking Zn exposure to transporter deployment.

### 2.4 2023: Applied environmental evidence for Zn tolerance and Zn removal are separable
Pagnucco et al. (2023, *Frontiers in Microbiology*) provide a high-citation applied study in which:
- **Zn(II) MICs across isolates range 500–1,100 mg/L** (strain-specific). (pagnucco2023metaltoleranceand pages 3-4)
- Biosorption capacities for multiple metals (including Zn) were reported as **exceeding 50 mg metal per g dry cell mass** for the studied strains. (pagnucco2023metaltoleranceand pages 9-10)
- In multi-metal systems, competitive inhibition can reduce binding/removal, emphasizing real-world complexity for bioreactors and in situ remediation. (pagnucco2023metaltoleranceand pages 9-10)
These findings motivate curating “zinc tolerant” separately from “zinc biosorbent/removal-capable.” (pagnucco2023metaltoleranceand pages 9-10)

---

## 3. Current applications and real-world implementations (with recent data)

### 3.1 Bioremediation / metal removal in water and sediments
A practical implementation pathway is **biosorption-based removal** using environmental isolates or enriched consortia.
- Pagnucco et al. used dialysis-tubing-based biosorption assays at **10 mg/L** in mono- and multi-metal aqueous solutions and quantified uptake as **q (mg removed per g dry biomass)** with AAS measurements; they observed strong Zn tolerance by MIC and strong biosorption capacity, but also **metal–metal competition** in multi-metal mixtures. (pagnucco2023metaltoleranceand pages 3-4, pagnucco2023metaltoleranceand pages 9-10)

### 3.2 Model organism relevance to contaminated environments
*C. metallidurans* is repeatedly framed as adapted to metal-rich soils; mechanistic work indicates that plasmid-encoded and chromosomal efflux layers permit survival at high Zn, suggesting relevance for environmental settings (e.g., “zinc deserts”/metal-rich soils) and as a chassis for bioremediation-oriented engineering. (nies2024aflowequilibrium pages 1-3, schulz2024theeffluxsystem pages 1-3)

---

## 4. Expert opinions / authoritative analysis (from sources in scope)

### 4.1 Zinc tolerance is network-level and conditional
The 2024 *Journal of Bacteriology* work explicitly argues for zinc handling as a **systems property**: a “flow equilibrium” comprising uptake and efflux reactions plus cytoplasmic metal-binding components. This is effectively an expert mechanistic synthesis grounded in isotope-tracer experiments and mutant analyses, and it implies that curation should include **environmental modifiers (Mg, Co)** and **buffers (GSH, polyP)**, not only transporters. (nies2024aflowequilibrium pages 1-3)

### 4.2 Layering and redundancy of exporters
Schulz et al. (2024) present zinc homeostasis/tolerance as “adaptive layering,” where backup exporters (CadA/CdfX) compensate when primary export (ZntA) is inhibited or insufficient, supporting a causal graph with **parallel efflux routes** rather than a linear pathway. (schulz2024theeffluxsystem pages 1-3)

### 4.3 Caution on secondary-source mechanistic dependencies
A 2024 review notes that the **CzcCBA efflux system requires CadA** for expression upon zinc excess, but this statement appears in a secondary source; it should be curated as provisional until validated against the underlying primary study. (dong2024bacterialmetalion pages 12-14)

---

## 5. Statistics and quantitative data (recent studies)

### 5.1 Quantitative tolerance ranges (growth-based)
- *C. metallidurans* IC50 shifts with plasmid pMOL30: **~1 mM (AE104) vs 3.4 mM (with pMOL30)**. (nies2024aflowequilibrium pages 1-3)
- Environmental isolates from an urban watershed: **Zn(II) MIC range 500–1,100 mg/L** (24 h growth inhibition definition). (pagnucco2023metaltoleranceand pages 3-4, pagnucco2023metaltoleranceand pages 2-3)

### 5.2 Quantitative mechanistic/physiological parameters (systems-level)
- Zn uptake kinetics and quantitative uptake/efflux assay outputs (65Zn/67Zn pulse–chase) are reported for *C. metallidurans*, including controlled zinc media (e.g., 200 nM) and efflux reductions in efflux mutants. (nies2024aflowequilibrium pages 20-22)
- Regulatory threshold: **zntA upregulated above ~200 nM external Zn**. (schulz2024theeffluxsystem pages 9-12)

### 5.3 Quantitative Zn removal metrics (application; not equivalent to tolerance)
- Biosorption capacity in Pagnucco et al.: metal uptake capacities **exceeding 50 mg metal per g dry biomass** (including Zn among tested ions). (pagnucco2023metaltoleranceand pages 9-10)

---

## Candidate nodes for TraitMech curation (grouped)
A curated zinc_tolerant.yaml will likely need nodes spanning chemicals, transporters, regulators, and assay/environment factors.

| Node label | Type | Suggested grounding CURIE(s) | Example taxon/context | Evidence/supporting source |
|---|---|---|---|---|
| zinc(II) ion | Chemical | CHEBI:29105 | Core stressor/assayed metal in *Cupriavidus metallidurans* zinc homeostasis and resistance studies; also used in environmental isolate MIC/biosorption assays | 10.1128/jb.00080-24 (2024) https://doi.org/10.1128/jb.00080-24; 10.1128/jb.00299-24 (2024) https://doi.org/10.1128/jb.00299-24; 10.3389/fmicb.2023.1278886 (2023) https://doi.org/10.3389/fmicb.2023.1278886 (nies2024aflowequilibrium pages 1-3, schulz2024theeffluxsystem pages 1-3, pagnucco2023metaltoleranceand pages 9-10) |
| magnesium(II) ion | Chemical | CHEBI:6636 | Modifies Zn uptake/flow equilibrium in *C. metallidurans*; Mg limitation increases Zn import | 10.1128/jb.00080-24 (2024) https://doi.org/10.1128/jb.00080-24 (nies2024aflowequilibrium pages 1-3) |
| cobalt(II) ion | Chemical | CHEBI:27638 | Competes/interacts with Zn pools and is co-exported by CzcCBA in *C. metallidurans* | 10.1128/jb.00080-24 (2024) https://doi.org/10.1128/jb.00080-24 (nies2024aflowequilibrium pages 1-3, nies2024aflowequilibrium pages 20-22) |
| cadmium(II) ion | Chemical | CHEBI candidate unavailable from context | Co-substrate for ZntA/CadA/CzcCBA; important for cross-metal regulation in *C. metallidurans* | 10.1128/jb.00299-24 (2024) https://doi.org/10.1128/jb.00299-24; 10.1128/jb.00080-24 (2024) https://doi.org/10.1128/jb.00080-24 (schulz2024theeffluxsystem pages 12-14, nies2024aflowequilibrium pages 1-3) |
| glutathione | Chemical | CHEBI:16856 | Cytoplasmic metal-binding buffer influencing Zn flow equilibrium in *C. metallidurans* | 10.1128/jb.00080-24 (2024) https://doi.org/10.1128/jb.00080-24 (nies2024aflowequilibrium pages 1-3) |
| polyphosphate | Chemical | label-only candidate | Cytoplasmic metal-binding component affecting Zn flow equilibrium in *C. metallidurans* | 10.1128/jb.00080-24 (2024) https://doi.org/10.1128/jb.00080-24 (nies2024aflowequilibrium pages 1-3) |
| ZntA | Gene/Protein | label-only; P-type ATPase family | Central PIB2-type Zn efflux ATPase in *C. metallidurans*; also highlighted in other bacteria as major Zn exporter | 10.1128/jb.00080-24 (2024) https://doi.org/10.1128/jb.00080-24; 10.1128/jb.00299-24 (2024) https://doi.org/10.1128/jb.00299-24 (nies2024aflowequilibrium pages 1-3, schulz2024theeffluxsystem pages 9-12) |
| CadA | Gene/Protein | label-only; P-type ATPase family | Backup Zn/Cd exporter and regulator-linked component in *C. metallidurans* | 10.1128/jb.00299-24 (2024) https://doi.org/10.1128/jb.00299-24; 10.13343/j.cnki.wsxb.20230561 (2024) https://doi.org/10.13343/j.cnki.wsxb.20230561 (schulz2024theeffluxsystem pages 12-14, dong2024bacterialmetalion pages 12-14) |
| CdfX | Gene/Protein | label-only; CDF family exporter | Newly described backup Zn exporter in *C. metallidurans* when ZntA is insufficient | 10.1128/jb.00299-24 (2024) https://doi.org/10.1128/jb.00299-24 (schulz2024theeffluxsystem pages 12-14, schulz2024theeffluxsystem pages 1-3) |
| DmeF | Gene/Protein | label-only; CDF family exporter | Additional chromosomal efflux component included in multi-efflux mutant backgrounds in *C. metallidurans* | 10.1128/jb.00080-24 (2024) https://doi.org/10.1128/jb.00080-24; 10.1128/jb.00299-24 (2024) https://doi.org/10.1128/jb.00299-24 (nies2024aflowequilibrium pages 1-3, schulz2024theeffluxsystem pages 1-3) |
| FieF / YiiP | Gene/Protein | label-only; CDF family exporter | Additional chromosomal metal exporter relevant to Zn-flow models; cited comparatively with *E. coli* FieF/YiiP | 10.1128/jb.00080-24 (2024) https://doi.org/10.1128/jb.00080-24; 10.1128/jb.00299-24 (2024) https://doi.org/10.1128/jb.00299-24 (nies2024aflowequilibrium pages 1-3, schulz2024theeffluxsystem pages 14-15) |
| ZntR | Gene/Protein | label-only; MerR-family regulator | Zn/Cd-responsive regulator essential for zntA expression and upregulating cdfX in *C. metallidurans* | 10.1128/jb.00299-24 (2024) https://doi.org/10.1128/jb.00299-24 (schulz2024theeffluxsystem pages 1-3, schulz2024theeffluxsystem pages 9-12) |
| CadR | Gene/Protein | label-only; MerR-family regulator | Regulator controlling cadA expression in *C. metallidurans* | 10.1128/jb.00080-24 (2024) https://doi.org/10.1128/jb.00080-24; 10.1128/jb.00299-24 (2024) https://doi.org/10.1128/jb.00299-24 (nies2024aflowequilibrium pages 1-3, schulz2024theeffluxsystem pages 1-3) |
| Zur | Gene/Protein | label-only; zinc uptake regulator | Low-zinc regulator derepressing zupT, useful for boundary between starvation homeostasis and excess-Zn tolerance | 10.1128/jb.00299-24 (2024) https://doi.org/10.1128/jb.00299-24 (schulz2024theeffluxsystem pages 9-12) |
| ZupT | Gene/Protein | label-only; ZIP-family importer | Zinc importer in *C. metallidurans*; relevant for homeostasis and assay interpretation | 10.1128/jb.00395-23 (2024) https://doi.org/10.1128/jb.00395-23; 10.1128/jb.00299-24 (2024) https://doi.org/10.1128/jb.00299-24 (nies2024aflowequilibrium pages 1-3, schulz2024theeffluxsystem pages 1-3) |
| CzcCBA transenvelope efflux complex | System/Pathway | label-only; RND-type efflux system | Major plasmid-encoded Co/Zn/Cd transenvelope efflux system in *C. metallidurans* | 10.1128/jb.00080-24 (2024) https://doi.org/10.1128/jb.00080-24; 10.1093/mtomcs/mfae058 (2024) https://doi.org/10.1093/mtomcs/mfae058 (nies2024aflowequilibrium pages 20-22, schulz2024theeffluxsystem pages 12-14) |
| czc determinant / pMOL30-borne resistance region | System/Pathway | label-only mobile resistance determinant | Plasmid-linked Zn resistance module increasing IC50 in *C. metallidurans* | 10.1128/jb.00080-24 (2024) https://doi.org/10.1128/jb.00080-24 (nies2024aflowequilibrium pages 1-3) |
| ZntA–CadA–CdfX inner-membrane efflux layer | System/Pathway | label-only composite module | Cytoplasmic Zn/Cd efflux layer supporting Zn tolerance in *C. metallidurans* | 10.1128/jb.00299-24 (2024) https://doi.org/10.1128/jb.00299-24; 10.1128/jb.00080-24 (2024) https://doi.org/10.1128/jb.00080-24 (schulz2024theeffluxsystem pages 12-14, nies2024aflowequilibrium pages 1-3) |
| zinc uptake–efflux flow equilibrium | Process | label-only process | Systems-level model for Zn homeostasis/tolerance in *C. metallidurans* | 10.1128/jb.00080-24 (2024) https://doi.org/10.1128/jb.00080-24 (nies2024aflowequilibrium pages 1-3) |
| zinc efflux | Process | GO candidate unavailable from context | Central causal process underlying tolerance via ZntA, CdfX, CzcCBA | 10.1128/jb.00080-24 (2024) https://doi.org/10.1128/jb.00080-24; 10.1128/jb.00299-24 (2024) https://doi.org/10.1128/jb.00299-24 (nies2024aflowequilibrium pages 1-3, schulz2024theeffluxsystem pages 1-3) |
| zinc import / uptake | Process | GO candidate unavailable from context | Counterbalancing process shaped by ZupT and Mg status in *C. metallidurans* | 10.1128/jb.00080-24 (2024) https://doi.org/10.1128/jb.00080-24 (nies2024aflowequilibrium pages 1-3) |
| biosorption of Zn2+ | Process | label-only process | Environmental isolates remove Zn from solution; distinct from growth-based tolerance | 10.3389/fmicb.2023.1278886 (2023) https://doi.org/10.3389/fmicb.2023.1278886 (pagnucco2023metaltoleranceand pages 9-10, pagnucco2023metaltoleranceand pages 3-4) |
| elevated extracellular Zn2+ | Environmental/Assay factor | CHEBI:29105 | Stress condition defining the trait; zntA upregulated above ~200 nM Zn in *C. metallidurans* | 10.1128/jb.00299-24 (2024) https://doi.org/10.1128/jb.00299-24 (schulz2024theeffluxsystem pages 9-12) |
| low-zinc availability / zinc starvation | Environmental/Assay factor | label-only condition | Distinguishes homeostasis/import responses from excess-zinc tolerance | 10.1128/jb.00299-24 (2024) https://doi.org/10.1128/jb.00299-24; 10.1128/jb.00395-23 (2024) https://doi.org/10.1128/jb.00395-23 (schulz2024theeffluxsystem pages 9-12, nies2024aflowequilibrium pages 1-3) |
| magnesium limitation | Environmental/Assay factor | CHEBI:6636 candidate | Increases Zn import rates and shifts Zn pool behavior in *C. metallidurans* | 10.1128/jb.00080-24 (2024) https://doi.org/10.1128/jb.00080-24 (nies2024aflowequilibrium pages 1-3) |
| multi-metal co-exposure | Environmental/Assay factor | label-only condition | Competes for biosorption sites and reduces Zn removal efficiency in wastewater-style assays | 10.3389/fmicb.2023.1278886 (2023) https://doi.org/10.3389/fmicb.2023.1278886 (pagnucco2023metaltoleranceand pages 9-10, pagnucco2023metaltoleranceand pages 1-2) |
| MIC assay | Environmental/Assay factor | label-only assay | Defined as lowest metal concentration inhibiting growth after 24 h; used for Zn tolerance phenotyping | 10.3389/fmicb.2023.1278886 (2023) https://doi.org/10.3389/fmicb.2023.1278886 (pagnucco2023metaltoleranceand pages 2-3) |
| dose–response growth curve assay | Environmental/Assay factor | label-only assay | Used to quantify Zn resistance/IC50 in *C. metallidurans* | 10.1128/jb.00299-24 (2024) https://doi.org/10.1128/jb.00299-24 (schulz2024theeffluxsystem pages 14-15) |
| pulse–chase 65Zn/67Zn assay | Environmental/Assay factor | label-only assay | Measures Zn uptake/efflux kinetics and supports causal assignment of exporters | 10.1128/jb.00080-24 (2024) https://doi.org/10.1128/jb.00080-24; 10.1128/jb.00299-24 (2024) https://doi.org/10.1128/jb.00299-24 (nies2024aflowequilibrium pages 1-3, schulz2024theeffluxsystem pages 1-3) |
| *Cupriavidus metallidurans* CH34 / AE104 | Organism/taxon | NCBITaxon candidate unavailable from context | Primary mechanistic model organism for Zn tolerance and efflux layering | 10.1128/jb.00080-24 (2024) https://doi.org/10.1128/jb.00080-24; 10.1128/jb.00299-24 (2024) https://doi.org/10.1128/jb.00299-24 (nies2024aflowequilibrium pages 1-3, schulz2024theeffluxsystem pages 1-3) |
| *Serratia* sp. L2, *Raoultella* sp. L30, *Klebsiella* sp. R3/R19 | Organism/taxon | NCBITaxon unresolved from context | 2023 environmental isolates with Zn MIC range 500–1100 mg/L and measurable Zn biosorption | 10.3389/fmicb.2023.1278886 (2023) https://doi.org/10.3389/fmicb.2023.1278886 (pagnucco2023metaltoleranceand pages 9-10, pagnucco2023metaltoleranceand pages 3-4) |


*Table: This table lists candidate node types for a zinc tolerance causal graph, including transporters, regulators, chemicals, and assay/environment factors. It is useful for TraitMech curation because it separates direct tolerance machinery from homeostasis-only and application/assay context nodes, with evidence limited to the provided context IDs.*

---

## Evidence-backed candidate causal edges (triples) for zinc_tolerant.yaml
The following table is formatted for curation as subject–predicate–object edges with snippets and notes.

| Subject node (label + CURIE) | Predicate | Object node (label + CURIE) | Evidence snippet | Reference | Notes / uncertainty |
|---|---|---|---|---|---|
| zinc(II) ion exposure >200 nM (CHEBI:29105) | upregulates | zntA transcription / ZntA Zn-exporting P-type ATPase (GO:0005385 candidate; label-only gene/protein) | “At external zinc concentrations above 200 nM... expression of the zntA gene... is upregulated” (schulz2024theeffluxsystem pages 9-12) | Nies et al. / Schulz et al., 2024, doi:10.1128/jb.00299-24, https://doi.org/10.1128/jb.00299-24 | Strong quantitative trigger for zinc-responsive efflux; gene/protein CURIE not resolved from provided context. |
| ZntR MerR-family regulator (label-only; MerR-family TF) | required_for | zntA expression (label-only) | “ZntR was essential for zntA expression” (schulz2024theeffluxsystem pages 9-12) | Schulz et al., 2024, doi:10.1128/jb.00299-24, https://doi.org/10.1128/jb.00299-24 | Strong regulatory edge for zinc tolerance network. |
| ZntR MerR-family regulator (label-only) | upregulates | cdfX expression (label-only CDF exporter) | “ZntR... was responsible for zinc- and cadmium-dependent upregulation of cdfX expression” (schulz2024theeffluxsystem pages 12-14, schulz2024theeffluxsystem pages 1-3) | Schulz et al., 2024, doi:10.1128/jb.00299-24, https://doi.org/10.1128/jb.00299-24 | Strong; especially evident when primary exporters are absent. |
| CdfX CDF-family exporter (label-only) | exports | zinc(II) ion (CHEBI:29105) | “The efflux system CdfX exports zinc that cannot be transported by ZntA” (schulz2024theeffluxsystem pages 1-3) | Schulz et al., 2024, doi:10.1128/jb.00299-24, https://doi.org/10.1128/jb.00299-24 | Strong but currently taxon-specific to *Cupriavidus metallidurans*. |
| cdfX deletion in Δe4 background (experimental factor) | decreases | zinc resistance / zinc-tolerant growth (traitmech:000014) | “Deletion of cdfX in the Δe4 mutant resulted in a further decrease in zinc resistance” (schulz2024theeffluxsystem pages 1-3) | Schulz et al., 2024, doi:10.1128/jb.00299-24, https://doi.org/10.1128/jb.00299-24 | Strong genetic evidence; background-specific. |
| ZntA PIB2-type P-type ATPase (label-only) | exports | zinc(II) ion (CHEBI:29105) | “Efflux of zinc ions is mediated by the P IB2 -type ATPase, ZntA” (nies2024aflowequilibrium pages 1-3) | Nies et al., 2024, doi:10.1128/jb.00080-24, https://doi.org/10.1128/jb.00080-24 | Core mechanistic edge for cytoplasmic zinc efflux. |
| ZntA PIB2-type P-type ATPase (label-only) | increases | zinc resistance / zinc-tolerant growth (traitmech:000014) | “deletion of PIB2 ATPases sharply lowers IC50 (to 7.7 µM), showing their causal role in resistance” (nies2024aflowequilibrium pages 1-3) | Nies et al., 2024, doi:10.1128/jb.00080-24, https://doi.org/10.1128/jb.00080-24 | Strong but refers jointly to PIB2 ATPases (ZntA/CadA); assign with caution if splitting by gene. |
| CadA PIB2-type P-type ATPase (label-only) | exports | cadmium(II) ion (CHEBI candidate) | “CadA cadmium” / “CadA is a known backup system for ZntA” (schulz2024theeffluxsystem pages 12-14, schulz2024theeffluxsystem pages 9-12) | Schulz et al., 2024, doi:10.1128/jb.00299-24, https://doi.org/10.1128/jb.00299-24 | Primary support is for Cd export; relevance to zinc tolerance is indirect/backup. |
| CadA PIB2-type P-type ATPase (label-only) | contributes_to | zinc resistance / zinc-tolerant growth (traitmech:000014) | “CadA is a known backup system for ZntA” (schulz2024theeffluxsystem pages 9-12) | Schulz et al., 2024, doi:10.1128/jb.00299-24, https://doi.org/10.1128/jb.00299-24 | Moderate; backup role rather than primary zinc exporter in this context. |
| CzcCBA transenvelope efflux complex (label-only RND system) | exports | zinc(II) ion from periplasm (CHEBI:29105) | “the plasmid-encoded RND transenvelope pump CzcCBA exports Co(II), Zn(II), and Cd(II)” (nies2024aflowequilibrium pages 20-22) | Nies et al., 2024, doi:10.1128/jb.00080-24, https://doi.org/10.1128/jb.00080-24 | Strong; periplasm/export localization is important boundary detail. |
| CzcCBA transenvelope efflux complex (label-only) | increases | zinc resistance / zinc-tolerant growth (traitmech:000014) | “The most prominent polypeptides were... particularly the CzcCBA transenvelope efflux system” under metal shock; “Without plasmid pMOL30 or czc... zinc...” resistance decreases (nies2024aflowequilibrium pages 1-3, nies2024aflowequilibrium pages 20-22) | Nies et al., 2024, doi:10.1128/jb.00080-24, https://doi.org/10.1128/jb.00080-24 | Strong but largely from *C. metallidurans*; exact quantitative MIC shift not always isolated to CzcCBA alone. |
| pMOL30 plasmid / czc determinant (label-only mobile element) | increases | Zn IC50 from ~1 mM to 3.4 mM (trait assay outcome) | “IC50 ~1 mM in AE104 vs 3.4 mM when pMOL30 present” (nies2024aflowequilibrium pages 1-3) | Nies et al., 2024, doi:10.1128/jb.00080-24, https://doi.org/10.1128/jb.00080-24 | Strong phenotypic evidence for plasmid-borne zinc resistance determinants; not solely attributable to one gene. |
| Zur zinc uptake regulator (label-only) | derepresses | zupT expression (label-only ZIP-family importer) under low zinc | “Under conditions of low zinc availability, the Zur regulator... derepresses expression of the zupT gene” (schulz2024theeffluxsystem pages 9-12) | Schulz et al., 2024, doi:10.1128/jb.00299-24, https://doi.org/10.1128/jb.00299-24 | Strong for zinc-starvation homeostasis; contributes to scope distinction from tolerance under excess zinc. |
| low zinc availability (environmental factor) | derepresses | zupT expression via Zur (label-only) | “Under conditions of low zinc availability... derepresses expression of the zupT gene” (schulz2024theeffluxsystem pages 9-12) | Schulz et al., 2024, doi:10.1128/jb.00299-24, https://doi.org/10.1128/jb.00299-24 | Useful boundary edge: importer induction is a homeostasis/starvation response, not a direct tolerance mechanism to excess zinc. |
| ZupT ZIP-family importer (label-only) | imports | zinc(II) ion (CHEBI:29105) | “FolE_IB1 was important when zinc uptake was impaired in cells without the zinc importer ZupT (ZIP family)” (nies2024aflowequilibrium pages 1-3) | Schulz et al., 2024; Nies et al., 2024, doi:10.1128/jb.00395-23, https://doi.org/10.1128/jb.00395-23 | Import edge is inferred from explicit designation as “zinc importer”; useful for graph completeness but not a tolerance-increasing edge under Zn excess. |
| magnesium(II) limitation (CHEBI:6636 candidate; environmental factor) | increases | zinc import rates / uptake flux (label-only process) | “magnesium limitation increases import rates sevenfold” (nies2024aflowequilibrium pages 1-3) | Nies et al., 2024, doi:10.1128/jb.00080-24, https://doi.org/10.1128/jb.00080-24 | Strong quantitative systems-level interaction; assay-specific. |
| magnesium(II) ion (CHEBI:6636) | competitively_inhibits | zinc uptake (label-only process) | “Mg(II) competitively inhibits uptake” (nies2024aflowequilibrium pages 1-3) | Nies et al., 2024, doi:10.1128/jb.00080-24, https://doi.org/10.1128/jb.00080-24 | Strong physiological interaction shaping apparent tolerance. |
| cobalt(II) ion (CHEBI:27638) | affects | cellular zinc pools and zinc export (label-only process) | “Other metal cations, especially cobalt, affected the cellular zinc pools and zinc export” (nies2024aflowequilibrium pages 1-3) | Nies et al., 2024, doi:10.1128/jb.00080-24, https://doi.org/10.1128/jb.00080-24 | Moderate; mechanism not fully resolved. |
| polyphosphate (CHEBI:13858 candidate) | contributes_to | zinc flow equilibrium / buffering (label-only process) | “The absence of the metal-binding cytoplasmic components, polyphosphate and glutathione... influenced the flow equilibrium” (nies2024aflowequilibrium pages 1-3) | Nies et al., 2024, doi:10.1128/jb.00080-24, https://doi.org/10.1128/jb.00080-24 | Moderate systems-level support; not a direct transporter edge. |
| glutathione (CHEBI:16856) | contributes_to | zinc flow equilibrium / buffering (label-only process) | “polyphosphate and glutathione... influenced the flow equilibrium” (nies2024aflowequilibrium pages 1-3) | Nies et al., 2024, doi:10.1128/jb.00080-24, https://doi.org/10.1128/jb.00080-24 | Moderate; relevant as intracellular buffering node. |
| *Cupriavidus metallidurans* zinc homeostasis system (NCBITaxon:266265 candidate) | tolerates | zinc(II) range ~30 nM to 10 mM (CHEBI:29105) | “the organism can survive zinc from about 30 nM to 10 mM” (schulz2024theeffluxsystem pages 12-14) | Schulz et al., 2024, doi:10.1128/jb.00299-24, https://doi.org/10.1128/jb.00299-24 | Quantitative trait-scope edge; organism-specific survival window, not universal microbial threshold. |
| Zn shock / metal shock (environmental factor) | increases_abundance_of | CzcCBA polypeptides (label-only) | “Metal-shocked C. metallidurans strains had adjusted their proteomes... The most prominent polypeptides were... particularly the CzcCBA transenvelope efflux system” (schulz2024theeffluxsystem pages 12-14) | Galea et al., 2024, doi:10.1093/mtomcs/mfae058, https://doi.org/10.1093/mtomcs/mfae058 | Strong proteomic support for deployment of CzcCBA during metal stress; mixed-metal shock rather than pure Zn assay. |
| bacterial strains from urban watershed (label-only taxa set) | tolerate | Zn2+ 500–1100 mg/L (CHEBI:29105) | “Zn2+ tolerance across the isolates is reported as a range of 500–1,100 mg L−1” (pagnucco2023metaltoleranceand pages 9-10, pagnucco2023metaltoleranceand pages 3-4) | Pagnucco et al., 2023, doi:10.3389/fmicb.2023.1278886, https://doi.org/10.3389/fmicb.2023.1278886 | Useful recent assay benchmark for trait scope; strain-level phenotype without defined mechanism. |
| bacterial biomass / cell surface binding sites (label-only) | removes | zinc(II) ion from solution (CHEBI:29105) | “the four highlighted metal-tolerant strains could extract multiple metal ions, including Zn2+, at capacities ‘each exceeding 50 mg of metal per gram of cell dry mass’” (pagnucco2023metaltoleranceand pages 9-10) | Pagnucco et al., 2023, doi:10.3389/fmicb.2023.1278886, https://doi.org/10.3389/fmicb.2023.1278886 | Application edge for biosorption, not equivalent to growth-based zinc tolerance. |
| multi-metal co-presence (environmental factor) | decreases | zinc biosorption efficiency / metal binding (label-only process) | “In multi-metal (eight-metal) solutions, co-presence of cations produced inhibitory effects on binding, indicating competition” (pagnucco2023metaltoleranceand pages 9-10, pagnucco2023metaltoleranceand pages 1-2) | Pagnucco et al., 2023, doi:10.3389/fmicb.2023.1278886, https://doi.org/10.3389/fmicb.2023.1278886 | Important implementation caveat for bioremediation; not a direct tolerance mechanism. |
| extracellular Zn2+ excess (CHEBI:29105) | competitively_inhibits | manganese uptake (label-only process) | “elevated extracellular Zn2+, specifically competitive inhibition of manganese uptake” (dong2024bacterialmetalion pages 12-14) | Dong et al., 2024 review, doi:10.13343/j.cnki.wsxb.20230561, https://doi.org/10.13343/j.cnki.wsxb.20230561 | Review-level support; mechanistic but not trait-positive, shows toxicity boundary. |
| CadA P-type ATPase (label-only) | required_for_timed_expression_of | CzcCBA efflux system under zinc excess (label-only) | “The CzcCBA efflux system requires the CadA P-type ATPase” (dong2024bacterialmetalion pages 12-14) | Dong et al., 2024 review, doi:10.13343/j.cnki.wsxb.20230561, https://doi.org/10.13343/j.cnki.wsxb.20230561 | Potentially strong but review-derived and phrasing may summarize prior work; curate as secondary-support edge until primary source checked. |


*Table: This table compiles evidence-backed candidate causal edges for the microbial trait 'zinc tolerant' using only the provided context IDs, emphasizing 2023-2024 sources. It highlights transporters, regulators, environmental modifiers, and quantitative assay thresholds relevant for TraitMech curation.*

---

## DOI-first bibliography (with dates and URLs)

1. **Nies DH, Schleuder G, Galea D, Herzberg M.** *A flow equilibrium of zinc in cells of Cupriavidus metallidurans.* **Journal of Bacteriology** (May 2024). DOI: **10.1128/jb.00080-24**. URL: https://doi.org/10.1128/jb.00080-24 (nies2024aflowequilibrium pages 1-3, nies2024aflowequilibrium pages 20-22)

2. **Schulz V, Galea D, Schleuder G, Strohmeyer P, Große C, Herzberg M, Nies DH.** *The efflux system CdfX exports zinc that cannot be transported by ZntA in Cupriavidus metallidurans.* **Journal of Bacteriology** (Nov 2024). DOI: **10.1128/jb.00299-24**. URL: https://doi.org/10.1128/jb.00299-24 (schulz2024theeffluxsystem pages 1-3, schulz2024theeffluxsystem pages 9-12, schulz2024theeffluxsystem pages 12-14)

3. **Pagnucco G, Overfield D, Chamlee Y, et al.** *Metal tolerance and biosorption capacities of bacterial strains isolated from an urban watershed.* **Frontiers in Microbiology** (Oct 2023). DOI: **10.3389/fmicb.2023.1278886**. URL: https://doi.org/10.3389/fmicb.2023.1278886 (pagnucco2023metaltoleranceand pages 3-4, pagnucco2023metaltoleranceand pages 9-10, pagnucco2023metaltoleranceand pages 2-3)

4. **Dong X, Deng S, Song H, Xu J.** *Bacterial metal ion efflux systems and metal homeostasis.* (2024; journal not resolved in retrieved metadata). DOI: **10.13343/j.cnki.wsxb.20230561**. URL: https://doi.org/10.13343/j.cnki.wsxb.20230561 (dong2024bacterialmetalion pages 12-14)

---

## Warnings / curation caveats (what should not yet be curated as strong general edges)

1. **CadA→CzcCBA dependence**: The claim that “CzcCBA requires CadA” appears in a 2024 review excerpt; curate as **secondary evidence** until the primary experimental source is checked for mechanism and context (species/conditions). (dong2024bacterialmetalion pages 12-14)

2. **Taxon specificity of CdfX**: CdfX is well supported in *C. metallidurans* as a backup Zn exporter, but broad generalization across taxa should be marked **uncertain** until ortholog function is demonstrated. (schulz2024theeffluxsystem pages 1-3)

3. **Biosorption vs growth**: Nodes/edges describing **Zn removal (mg/g)** should not be used as direct evidence for “zinc tolerant” unless accompanied by growth tolerance assays under elevated Zn. (pagnucco2023metaltoleranceand pages 9-10)

4. **Metal mixture effects**: Multi-metal co-exposures can change apparent Zn tolerance/removal and may require explicit “assay condition” nodes if curating quantitative edges. (pagnucco2023metaltoleranceand pages 9-10)


References

1. (nies2024aflowequilibrium pages 1-3): Dietrich H. Nies, Grit Schleuder, Diana Galea, and Martin Herzberg. A flow equilibrium of zinc in cells of <i>cupriavidus metallidurans</i>. May 2024. URL: https://doi.org/10.1128/jb.00080-24, doi:10.1128/jb.00080-24. This article has 14 citations and is from a peer-reviewed journal.

2. (schulz2024theeffluxsystem pages 1-3): Vladislava Schulz, Diana Galea, Grit Schleuder, Philipp Strohmeyer, Cornelia Große, Martin Herzberg, and Dietrich H. Nies. The efflux system cdfx exports zinc that cannot be transported by znta in <i>cupriavidus metallidurans</i>. Nov 2024. URL: https://doi.org/10.1128/jb.00299-24, doi:10.1128/jb.00299-24. This article has 6 citations and is from a peer-reviewed journal.

3. (schulz2024theeffluxsystem pages 9-12): Vladislava Schulz, Diana Galea, Grit Schleuder, Philipp Strohmeyer, Cornelia Große, Martin Herzberg, and Dietrich H. Nies. The efflux system cdfx exports zinc that cannot be transported by znta in <i>cupriavidus metallidurans</i>. Nov 2024. URL: https://doi.org/10.1128/jb.00299-24, doi:10.1128/jb.00299-24. This article has 6 citations and is from a peer-reviewed journal.

4. (pagnucco2023metaltoleranceand pages 3-4): Grace Pagnucco, Dustin Overfield, Yanesa Chamlee, Claudia Shuler, Amin Kassem, Somie Opara, Hawraa Najaf, Lana Abbas, Oliver Coutinho, Aleksa Fortuna, Fatima Sulaiman, James Farinas, Reis Schittenhelm, Brian Catalfano, Xiaohua Li, and Sonia M. Tiquia-Arashiro. Metal tolerance and biosorption capacities of bacterial strains isolated from an urban watershed. Frontiers in Microbiology, Oct 2023. URL: https://doi.org/10.3389/fmicb.2023.1278886, doi:10.3389/fmicb.2023.1278886. This article has 104 citations and is from a peer-reviewed journal.

5. (pagnucco2023metaltoleranceand pages 2-3): Grace Pagnucco, Dustin Overfield, Yanesa Chamlee, Claudia Shuler, Amin Kassem, Somie Opara, Hawraa Najaf, Lana Abbas, Oliver Coutinho, Aleksa Fortuna, Fatima Sulaiman, James Farinas, Reis Schittenhelm, Brian Catalfano, Xiaohua Li, and Sonia M. Tiquia-Arashiro. Metal tolerance and biosorption capacities of bacterial strains isolated from an urban watershed. Frontiers in Microbiology, Oct 2023. URL: https://doi.org/10.3389/fmicb.2023.1278886, doi:10.3389/fmicb.2023.1278886. This article has 104 citations and is from a peer-reviewed journal.

6. (nies2024aflowequilibrium pages 20-22): Dietrich H. Nies, Grit Schleuder, Diana Galea, and Martin Herzberg. A flow equilibrium of zinc in cells of <i>cupriavidus metallidurans</i>. May 2024. URL: https://doi.org/10.1128/jb.00080-24, doi:10.1128/jb.00080-24. This article has 14 citations and is from a peer-reviewed journal.

7. (pagnucco2023metaltoleranceand pages 9-10): Grace Pagnucco, Dustin Overfield, Yanesa Chamlee, Claudia Shuler, Amin Kassem, Somie Opara, Hawraa Najaf, Lana Abbas, Oliver Coutinho, Aleksa Fortuna, Fatima Sulaiman, James Farinas, Reis Schittenhelm, Brian Catalfano, Xiaohua Li, and Sonia M. Tiquia-Arashiro. Metal tolerance and biosorption capacities of bacterial strains isolated from an urban watershed. Frontiers in Microbiology, Oct 2023. URL: https://doi.org/10.3389/fmicb.2023.1278886, doi:10.3389/fmicb.2023.1278886. This article has 104 citations and is from a peer-reviewed journal.

8. (schulz2024theeffluxsystem pages 12-14): Vladislava Schulz, Diana Galea, Grit Schleuder, Philipp Strohmeyer, Cornelia Große, Martin Herzberg, and Dietrich H. Nies. The efflux system cdfx exports zinc that cannot be transported by znta in <i>cupriavidus metallidurans</i>. Nov 2024. URL: https://doi.org/10.1128/jb.00299-24, doi:10.1128/jb.00299-24. This article has 6 citations and is from a peer-reviewed journal.

9. (dong2024bacterialmetalion pages 12-14): X DONG, S DENG, H SONG, and J XU. Bacterial metal ion efflux systems and metal homeostasis. Unknown journal, 2024. URL: https://doi.org/10.13343/j.cnki.wsxb.20230561, doi:10.13343/j.cnki.wsxb.20230561.

10. (schulz2024theeffluxsystem pages 14-15): Vladislava Schulz, Diana Galea, Grit Schleuder, Philipp Strohmeyer, Cornelia Große, Martin Herzberg, and Dietrich H. Nies. The efflux system cdfx exports zinc that cannot be transported by znta in <i>cupriavidus metallidurans</i>. Nov 2024. URL: https://doi.org/10.1128/jb.00299-24, doi:10.1128/jb.00299-24. This article has 6 citations and is from a peer-reviewed journal.

11. (pagnucco2023metaltoleranceand pages 1-2): Grace Pagnucco, Dustin Overfield, Yanesa Chamlee, Claudia Shuler, Amin Kassem, Somie Opara, Hawraa Najaf, Lana Abbas, Oliver Coutinho, Aleksa Fortuna, Fatima Sulaiman, James Farinas, Reis Schittenhelm, Brian Catalfano, Xiaohua Li, and Sonia M. Tiquia-Arashiro. Metal tolerance and biosorption capacities of bacterial strains isolated from an urban watershed. Frontiers in Microbiology, Oct 2023. URL: https://doi.org/10.3389/fmicb.2023.1278886, doi:10.3389/fmicb.2023.1278886. This article has 104 citations and is from a peer-reviewed journal.