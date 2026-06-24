---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T21:28:08.388195'
end_time: '2026-06-17T21:51:16.635106'
duration_seconds: 1388.25
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: copper tolerant
  trait_identifier: traitmech:000018
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: copper_tolerant
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A metal tolerance in which an organism grows in the presence of elevated
    copper (Cu2+/Cu+) concentrations, typically via the cue, cus, pco, and cop systems
    and ATPase-driven cytoplasmic copper efflux.
  parent_traits: traitmech:000012
  synonyms: copper resistant
  evidence_summary: 'DOI:10.1007/s10565-013-9262-1: ATPase-driven copper efflux seems
    to be the main mechanism responsible for cytoplasmic copper detoxification in
    until now studied bacteria (Review supports active efflux via the cue, cus, pco,
    and cop systems as the basis of bacterial copper tolerance.) | DOI:10.3389/fmicb.2020.00047:
    C. metallidurans BS1 conferred resistance to Zn2+ displaying a MIC of 20 mM, Cd2+
    (2.5 mM), Co2+ (20mM), Ni2+ (8 mM), As3+ (3.5 mM), Cu2+ (5 mM), Au3+ (1 uM) and
    Pb2+ (1.7 mM) (Organism example: Cupriavidus metallidurans BS1 tolerates copper
    (Cu2+) to a MIC of 5 mM.)'
  causal_graph_summary: 'copper_tolerance_cop_efflux: 4 nodes, 3 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 35
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** copper tolerant
- **METPO identifier:** traitmech:000018
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metal tolerance in which an organism grows in the presence of elevated copper (Cu2+/Cu+) concentrations, typically via the cue, cus, pco, and cop systems and ATPase-driven cytoplasmic copper efflux.
- **Parent traits:** traitmech:000012
- **Synonyms:** copper resistant
- **Existing evidence:** DOI:10.1007/s10565-013-9262-1: ATPase-driven copper efflux seems to be the main mechanism responsible for cytoplasmic copper detoxification in until now studied bacteria (Review supports active efflux via the cue, cus, pco, and cop systems as the basis of bacterial copper tolerance.) | DOI:10.3389/fmicb.2020.00047: C. metallidurans BS1 conferred resistance to Zn2+ displaying a MIC of 20 mM, Cd2+ (2.5 mM), Co2+ (20mM), Ni2+ (8 mM), As3+ (3.5 mM), Cu2+ (5 mM), Au3+ (1 uM) and Pb2+ (1.7 mM) (Organism example: Cupriavidus metallidurans BS1 tolerates copper (Cu2+) to a MIC of 5 mM.)
- **Existing causal graph summary:** copper_tolerance_cop_efflux: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **copper tolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/copper_tolerant.yaml`.

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
- **Trait label:** copper tolerant
- **METPO identifier:** traitmech:000018
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metal tolerance in which an organism grows in the presence of elevated copper (Cu2+/Cu+) concentrations, typically via the cue, cus, pco, and cop systems and ATPase-driven cytoplasmic copper efflux.
- **Parent traits:** traitmech:000012
- **Synonyms:** copper resistant
- **Existing evidence:** DOI:10.1007/s10565-013-9262-1: ATPase-driven copper efflux seems to be the main mechanism responsible for cytoplasmic copper detoxification in until now studied bacteria (Review supports active efflux via the cue, cus, pco, and cop systems as the basis of bacterial copper tolerance.) | DOI:10.3389/fmicb.2020.00047: C. metallidurans BS1 conferred resistance to Zn2+ displaying a MIC of 20 mM, Cd2+ (2.5 mM), Co2+ (20mM), Ni2+ (8 mM), As3+ (3.5 mM), Cu2+ (5 mM), Au3+ (1 uM) and Pb2+ (1.7 mM) (Organism example: Cupriavidus metallidurans BS1 tolerates copper (Cu2+) to a MIC of 5 mM.)
- **Existing causal graph summary:** copper_tolerance_cop_efflux: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **copper tolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/copper_tolerant.yaml`.

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


## Research Report: Microbial trait “copper tolerant” (TraitMech: traitmech:000018)

### Scope summary (Trait scope and boundaries)
**Copper tolerant** denotes an experimentally observable microbial **growth/survival phenotype in the presence of elevated extracellular copper** (Cu(II)/Cu(I)), typically quantified by MIC/IC50, dose–response growth curves, lag-phase changes, or viability under copper salt stress (often CuSO4). Across recent studies, oxygenation is a key boundary condition: aerobic vs anaerobic conditions alter copper redox speciation and thus which detox systems are required (e.g., oxygen-dependent multicopper oxidases vs anaerobically important Cus/Pco routes) (rismondo2023thesensoryhistidine pages 5-8, hikal2024theacquiredpco pages 3-4, hirth2023fullcopperresistance pages 16-18).

**Notably distinct but nearby traits**:
- **Trace-level copper homeostasis** (micronutrient management) vs **high-copper tolerance/resistance**: many of the same components are involved, but high-copper tolerance requires additional capacity and is assay-defined (rebelo2023unravelingtherole pages 6-8, hirth2023fullcopperresistance pages 16-18).
- **Multimetal resistance**: copper genes can co-occur on islands/plasmids with other resistances; without phenotypic evidence, these should not be curated as causal for copper tolerance (elsen2024crossregulationandcrosstalk pages 9-11, hikal2024theacquiredpco pages 3-4).
- **Copper adsorption/sequestration** (e.g., EPS biosorption) can yield apparent “tolerance” by lowering bioavailable Cu without necessarily changing intracellular detox machinery; it is mechanistically separable from efflux/oxidation systems (yu2024isolationofhighly pages 6-8, yu2024isolationofhighly media 3f7f73b3).

---

## 1) Key concepts and definitions (current understanding)

### Copper toxicity drivers (why tolerance is needed)
At elevated levels, copper toxicity is linked to **Cu redox cycling and Cu(I) chemistry**, including **ROS generation** and damage to lipids/proteins/DNA, and **Fe–S cluster disruption** by Cu(I) binding to thiols/metalloproteins (review synthesis) (rebelo2023unravelingtherole pages 6-8).

### Canonical mechanistic “modules” underpinning copper tolerance
Recent primary and synthesis literature converge on several recurrent, mechanistically grounded modules:
1. **Cytoplasmic Cu(I) efflux via P-type (P1B-type) ATPases** (e.g., CopA/CupA): exports Cu(I) from cytoplasm to periplasm (hirth2023fullcopperresistance pages 16-18, wong2023coppereffluxsystem pages 1-2).
2. **Periplasmic Cu(I) detoxification/oxidation via multicopper oxidases** (CueO/CopA/PcoA/PcoA2): oxidizes Cu(I)→Cu(II) under aerobic conditions, reducing toxicity and uptake (hirth2023fullcopperresistance pages 16-18, rebelo2023unravelingtherole pages 6-8).
3. **Transenvelope efflux (CusCBA/CusCFBA)**: exports periplasmic Cu(I) directly out of the cell; becomes particularly important anaerobically when periplasmic oxidases are ineffective (rismondo2023thesensoryhistidine pages 5-8, hirth2023fullcopperresistance pages 16-18).
4. **Metallochaperones (CopZ, CusF, PcoC/E, CupC)**: bind Cu and deliver it to exporters/oxidases, limiting uncontrolled Cu(I) interactions (wong2023coppereffluxsystem pages 1-2, hirth2023fullcopperresistance pages 16-18, hikal2024theacquiredpco pages 7-9).
5. **Regulatory sensing and response**: MerR-like regulators (CueR/CupR) and two-component systems (CusRS/CopRS/PcoRS; cross-talk with Zn systems like CzcRS in some taxa) modulate expression of detox genes in response to copper compartmentalization signals (wong2023coppereffluxsystem pages 8-10, rismondo2023thesensoryhistidine pages 5-8, elsen2024crossregulationandcrosstalk pages 9-11).
6. **Extracellular polymeric substances (EPS) sequestration**: copper exposure can induce EPS production; EPS binds copper (biosorption), reducing free copper and supporting growth in high-copper environments (yu2024isolationofhighly pages 6-8, yu2024isolationofhighly media 3f7f73b3).

---

## 2) Recent developments and latest research (priority 2023–2024)

### 2.1 Network/interplay view of copper tolerance (Cupriavidus)
A 2023 systems genetics dissection in *Cupriavidus metallidurans* demonstrated that “full copper resistance” is an **emergent property of interacting systems**, with quantified hierarchy **Cup > Cop > Cus > glutathione (GSH) > Gig** (hirth2023fullcopperresistance pages 16-18). Mechanistically:
- **CupA** is a central **Cu(I)-exporting P-type ATPase**, with CupC and CupR involved (hirth2023fullcopperresistance pages 16-18).
- **CopA** functions as a periplasmic Cu(I) oxidase (CueO-like) and supports resistance particularly in oxygenated conditions (hirth2023fullcopperresistance pages 16-18).
- **CusCBA** can partially substitute for Cop-dependent detox and becomes especially important under anaerobiosis (hirth2023fullcopperresistance pages 16-18).
This “interplay” framing is important for TraitMech curation: copper tolerance is often not a single-gene trait but a **redundant/conditional network** (hirth2023fullcopperresistance pages 16-18).

### 2.2 Copper tolerance as a virulence/host-defense countermeasure (Haemophilus)
Wong et al. (2023) provided direct quantitative evidence that copper efflux contributes to both **copper tolerance and in vivo fitness** in a murine lung infection model (publication date: May 2023; URL: https://doi.org/10.1128/iai.00091-23) (wong2023coppereffluxsystem pages 8-10).
Key findings:
- **CueR→copZA induction**: a *Pcop*-lacZ reporter increased ~**12-fold** in response to copper; **cueR deletion abolished** induction (wong2023coppereffluxsystem pages 5-8).
- **Efflux controls intracellular Cu**: the ΔcopZA mutant accumulated **~97% more copper** than wild type at **0.5 mM CuSO4** (wong2023coppereffluxsystem pages 1-2).
- **In vivo fitness**: in mouse lung coinfection, ΔcopA and ΔcopZA were **~4-fold** and **~20-fold underrepresented**, respectively (wong2023coppereffluxsystem pages 8-10).
These data make copA/copZ/cueR high-confidence causal nodes/edges for copper tolerance (and a host-interaction application context) (wong2023coppereffluxsystem pages 8-10).

### 2.3 Demonstration of periplasmic copper sensing by CusS (E. coli)
Rismondo et al. (2023) experimentally supported the hypothesis that the CusRS two-component system **senses periplasmic copper** via the histidine kinase **CusS** (publication date: Apr 2023; URL: https://doi.org/10.1128/spectrum.00291-23) (rismondo2023thesensoryhistidine pages 1-2).
Quantitative phenotype supports conditional importance:
- Under anaerobic conditions in LB, WT IC50 was reported **>100 mM** vs **~25 mM** for ΔcusS, demonstrating CusS-dependent copper tolerance when oxygen is absent (rismondo2023thesensoryhistidine pages 5-8).
This strengthens a curatable regulatory edge (periplasmic Cu → CusS → cusCFBA expression → copper tolerance) (rismondo2023thesensoryhistidine pages 5-8).

### 2.4 Cross-regulation and ICE-acquired copper resistance circuitry (Pseudomonas)
Elsen et al. (2024) dissected how an **ICE-encoded CusRS** integrates with core copper systems in *Pseudomonas* through **cross-regulation and cross-talk**, including a shared palindromic binding site used by response regulators (publication date: Jun 2024; URL: https://doi.org/10.1371/journal.pgen.1011325) (elsen2024crossregulationandcrosstalk pages 3-5, elsen2024crossregulationandcrosstalk pages 9-11).
Mechanistic highlights for curation:
- CusR binds a **palindromic motif** (ATTCATnnATGTAAT) and controls a nine-gene operon including **pcoA2** (multicopper oxidase) and predicted chaperones/ATPase (elsen2024crossregulationandcrosstalk pages 3-5).
- Copper resistance phenotypes depend on combined regulators: loss of CopR/CusR increases sensitivity starting around **5 mM CuSO4** and is accentuated at higher copper (e.g., 20 mM) (elsen2024crossregulationandcrosstalk pages 5-7).
This provides high-confidence regulatory network edges, but they should be flagged as **taxon/strain-specific accessory locus** (ICE-borne) rather than universal (elsen2024crossregulationandcrosstalk pages 16-18).

### 2.5 Anaerobic-specific role for acquired pcoABCD (Salmonella)
Hikal et al. (2024) provided a clear, assay-grounded result: an acquired **pcoABCD** cassette mediates **anaerobic copper resistance** in *Salmonella enterica* (publication date: Sep 2024; URL: https://doi.org/10.3389/fmicb.2024.1454763) (hikal2024theacquiredpco pages 3-4).
Key quantitative data:
- Aerobic MIC: **8 mM CuSO4** for all tested strains.
- Anaerobic MIC: **7 mM** for pco+ strains vs **1 mM** for the ΔpcoABCD mutant (hikal2024theacquiredpco pages 3-4).
This is a strong example of **environment-dependent causality** (anaerobiosis → Cu(I) prevalence → pco importance), ideal for conditional edges in TraitMech (hikal2024theacquiredpco pages 7-9).

### 2.6 EPS sequestration as a copper tolerance mechanism in deep-sea isolates
Yu et al. (2024) reported high copper tolerance in deep-sea hydrothermal isolates (max **6–10 mM Cu(II)** for many strains) and linked copper exposure to increased EPS production and EPS-mediated copper biosorption (publication date: Aug 2024; URL: https://doi.org/10.3389/fmicb.2024.1390451) (yu2024isolationofhighly pages 2-3).
Quantitative examples:
- Halomonas sp. CuT3-1 EPS increased from **379.65 to 1013.00 mg/L** upon copper stimulation; EPS sorption capacities up to **~52.24 mg CuSO4/g EPS** (CuT6) (yu2024isolationofhighly pages 6-8).
- Figure/Table evidence: maximum copper tolerance values and EPS biosorption curves are shown in the extracted Table 1 and Figure 4 (yu2024isolationofhighly media cbe76ea6, yu2024isolationofhighly media 3f7f73b3).
This supports an extracellular sequestration branch of the causal graph, distinct from efflux/oxidation mechanisms (yu2024isolationofhighly pages 6-8).

---

## 3) Current applications and real-world implementations

### Host–pathogen interactions (copper as innate defense)
Copper tolerance modules can be directly relevant to infection: NTHi requires copA/copZ for fitness in the mouse lung, consistent with copper exposure as a host defense pressure (wong2023coppereffluxsystem pages 8-10).

### Agriculture and environmental selection pressures
Copper-based antimicrobials and long-term environmental copper can select for mobile copper resistance determinants and co-selection networks; mechanistically grounded synthesis emphasizes plasmid-borne pco/sil/cus/cue-related systems as tolerance routes in agri-food contexts (rebelo2023unravelingtherole pages 6-8). In plant-associated bacteria, copper resistance systems can be accessory and horizontally acquired; the Elsen et al. work illustrates how ICE loci can integrate into core regulation (elsen2024crossregulationandcrosstalk pages 16-18).

### Bioremediation / metal-rich niches
Isolation of microbes with high Cu tolerance (6–10 mM) from hydrothermal environments and their EPS binding capacities highlights potential application in copper sequestration/bioremediation and biomaterials contexts, although direct engineered implementations are not demonstrated in that study (yu2024isolationofhighly pages 2-3, yu2024isolationofhighly pages 6-8).

---

## 4) Expert opinions and analysis (authoritative interpretations)

### Copper tolerance is a conditional, multi-system trait
Hirth et al. explicitly frame copper resistance as a trait emerging from a **network of interacting systems**, rather than a single determinant, and demonstrate partial redundancy/compensation among Cop and Cus modules (hirth2023fullcopperresistance pages 16-18).

### Oxygen/redox context governs which modules matter
Primary studies show oxygen dependence:
- Oxygen-dependent periplasmic oxidases (CopA/CueO-like) cannot operate anaerobically, increasing reliance on Cus or pco modules (rismondo2023thesensoryhistidine pages 5-8, hikal2024theacquiredpco pages 3-4).
This should be encoded as environmental-condition nodes and conditional edges in TraitMech.

### Accessory loci and regulatory cross-talk complicate genotype→phenotype mapping
Elsen et al. show that ICE-acquired CusRS and a nine-gene pcoA2 operon can be integrated and cross-regulated by core systems (CopRS) and even Zn systems (CzcRS), implying “copper tolerant” can be conferred by modular acquisition and network rewiring (elsen2024crossregulationandcrosstalk pages 9-11, elsen2024crossregulationandcrosstalk pages 3-5).

---

## 5) Relevant statistics and data (recent primary studies)

- **NTHi copper accumulation**: ΔcopZA accumulated **~97% more copper** at **0.5 mM CuSO4**; cop promoter induction **~12-fold** with copper; in vivo attenuation **~4-fold** (ΔcopA) and **~20-fold** (ΔcopZA) (wong2023coppereffluxsystem pages 1-2, wong2023coppereffluxsystem pages 5-8, wong2023coppereffluxsystem pages 8-10).
- **Salmonella anaerobic MIC shift**: aerobic MIC **8 mM** for all strains; anaerobic MIC **7 mM** (pco+) vs **1 mM** (ΔpcoABCD) (hikal2024theacquiredpco pages 3-4).
- **E. coli CusS-dependent anaerobic tolerance**: WT IC50 **>100 mM** vs ΔcusS **~25 mM** anaerobically in LB (rismondo2023thesensoryhistidine pages 5-8).
- **Deep-sea isolates tolerance and EPS binding**: maximum copper tolerance **6–10 mM** (Table 1) and EPS biosorption measured over 0–400 mg/L Cu(II) (Figure 4) (yu2024isolationofhighly media cbe76ea6, yu2024isolationofhighly media 3f7f73b3).

---

# Candidate nodes (grouped by type; with grounding suggestions)

### Environmental / experimental factors
- Elevated copper (CuSO4 exposure; Cu(II)/Cu(I)) — **ChEBI**: copper(2+) CHEBI:29036; copper(I) CHEBI:29033; sulfate CHEBI:16189 (hikal2024theacquiredpco pages 3-4, wong2023coppereffluxsystem pages 5-8).
- Oxygen status: **aerobic vs anaerobic** (condition node; consider ENVO “anaerobic environment” candidate ENVO:01001029; aerobic environment candidate ENVO:01001037) (rismondo2023thesensoryhistidine pages 5-8, hikal2024theacquiredpco pages 3-4).
- Medium/context: LB, Mueller-Hinton agar, marine broth (MB), host lung infection environment (hikal2024theacquiredpco pages 3-4, yu2024isolationofhighly pages 6-8, wong2023coppereffluxsystem pages 8-10).

### Cellular compartments / locations
- Cytoplasm; periplasmic space (**GO:0042597**); inner membrane; outer membrane (**GO:0019867**) (rismondo2023thesensoryhistidine pages 5-8, rebelo2023unravelingtherole pages 6-8).

### Core molecular systems (genes/proteins/operons)
**Efflux / transport**
- P-type Cu(I) ATPases: CopA (Cu+-ATPase), CupA (PIB1-type ATPase), PcoF (putative P-type ATPase) (wong2023coppereffluxsystem pages 1-2, hirth2023fullcopperresistance pages 16-18, elsen2024crossregulationandcrosstalk pages 3-5).
- RND transenvelope efflux: CusCBA/CusCFBA; components CusS/CusR regulation; CusF chaperone (rismondo2023thesensoryhistidine pages 5-8, rismondo2023thesensoryhistidine pages 1-2).

**Oxidation/detoxification in periplasm**
- Multicopper oxidases: CopA (CueO-like in *Cupriavidus*), CueO, PcoA, PcoA2 (hirth2023fullcopperresistance pages 16-18, rebelo2023unravelingtherole pages 6-8, elsen2024crossregulationandcrosstalk pages 3-5).

**Chaperones / sequestration**
- CopZ metallochaperones (tandem copies in *H. influenzae*); CupC; PcoC; PcoE (“metal sponge”) (wong2023coppereffluxsystem pages 1-2, hirth2023fullcopperresistance pages 16-18, hikal2024theacquiredpco pages 2-3).
- EPS (polysaccharides, proteins) as extracellular copper-binding matrix (yu2024isolationofhighly pages 6-8).

**Regulators**
- MerR-like CueR/CupR (wong2023coppereffluxsystem pages 5-8, hirth2023fullcopperresistance pages 16-18).
- Two-component systems: CusRS, CopRS, PcoRS; Zn-responsive CzcRS as cross-regulator in *Pseudomonas* (elsen2024crossregulationandcrosstalk pages 9-11, elsen2024crossregulationandcrosstalk pages 3-5).

**Redox buffer / ancillary systems**
- Glutathione (GSH; gshA) as a contributor to resistance network (hirth2023fullcopperresistance pages 16-18).
- gig operon (function unknown; contributory) (hirth2023fullcopperresistance pages 16-18).

### Biological processes (GO candidates)
- Copper ion transmembrane transport (**GO:0006825**)
- Cellular copper ion homeostasis (**GO:0006878**)
- Response to copper ion (**GO:0090227**)
- Oxidation–reduction process (**GO:0055114**) (process-level support) (rebelo2023unravelingtherole pages 6-8, hirth2023fullcopperresistance pages 16-18)

---

# Candidate evidence-backed causal edges (curation table)

The table below is a curation-focused candidate edge list with snippets and notes.

| Edge (subject—predicate→object) | Evidence (short quote/snippet) | Study (first author year, journal) | DOI/URL | Notes |
|---|---|---|---|---|
| elevated copper—induces→CupA-mediated cytoplasmic Cu(I) efflux | “CupA… mediating efflux of cytoplasmic Cu(I) to the periplasm” and Cup was the most important contributor to resistance (hirth2023fullcopperresistance pages 16-18) | Hirth 2023, *Applied and Environmental Microbiology* | https://doi.org/10.1128/aem.00567-23 | Strong mechanistic edge in *Cupriavidus metallidurans*; mutant/dose-response evidence; taxon-specific but likely broadly relevant to bacterial Cu tolerance. |
| CupA activity—increases→copper resistance | “All five systems contributed to copper resistance in the order of importance: Cup, Cop, Cus, GSH, and Gig” (hirth2023fullcopperresistance pages 16-18) | Hirth 2023, *Applied and Environmental Microbiology* | https://doi.org/10.1128/aem.00567-23 | Strong; direct resistance phenotype in mutant backgrounds; useful core edge for TraitMech. |
| CopA periplasmic Cu(I) oxidase—decreases→periplasmic Cu(I) toxicity | “periplasmic Cu(I)-oxidase CopA… oxidizes Cu(I) to Cu(II), reducing reactive-oxygen-species-mediated membrane damage” (hirth2023fullcopperresistance pages 16-18) | Hirth 2023, *Applied and Environmental Microbiology* | https://doi.org/10.1128/aem.00567-23 | Strong in *C. metallidurans*; oxidase is oxygen-dependent, so context matters for aerobic conditions. |
| CusCBA transenvelope efflux system—exports→periplasmic Cu(I) | “The Cus system… exports periplasmic Cu(I) from the periplasm to the outside” (hirth2023fullcopperresistance pages 16-18) | Hirth 2023, *Applied and Environmental Microbiology* | https://doi.org/10.1128/aem.00567-23 | Strong; periplasm-focused detox edge; especially relevant when periplasmic Cu accumulates. |
| anaerobiosis—increases importance of→Cus-mediated copper resistance | “Cus system becomes especially important under anaerobic conditions where CopA is inactive” (hirth2023fullcopperresistance pages 16-18) | Hirth 2023, *Applied and Environmental Microbiology* | https://doi.org/10.1128/aem.00567-23 | Strong but condition-dependent; curate with oxygen-context note. |
| glutathione—contributes to→full copper resistance | “Gig and GSH cooperated with Cop, Cus, and Cup” (hirth2023fullcopperresistance pages 16-18) | Hirth 2023, *Applied and Environmental Microbiology* | https://doi.org/10.1128/aem.00567-23 | Moderate-strength edge; contribution shown genetically, but exact biochemical mechanism is less resolved than Cup/Cop/Cus. |
| CueR—activates→copZA operon expression in response to copper | “Pcop-lacZ reporter increased ~12-fold upon addition of 250 mM copper” and “deletion of cueR abolished the copper-mediated induction” (wong2023coppereffluxsystem pages 8-10, wong2023coppereffluxsystem pages 5-8) | Wong 2023, *Infection and Immunity* | https://doi.org/10.1128/iai.00091-23 | Strong; direct promoter-reporter evidence in *Haemophilus influenzae* / NTHi. |
| CopA Cu+-ATPase—decreases→intracellular copper accumulation | “ΔcopZA mutant accumulated 97% more copper than the wild type” under 0.5 mM CuSO4 (wong2023coppereffluxsystem pages 1-2, wong2023coppereffluxsystem pages 8-10) | Wong 2023, *Infection and Immunity* | https://doi.org/10.1128/iai.00091-23 | Strong for *H. influenzae*; measured copper accumulation supports efflux mechanism. |
| copA deletion—decreases→copper tolerance | “single copA… mutants exhibited decreased copper tolerance” (wong2023coppereffluxsystem pages 1-2, wong2023coppereffluxsystem pages 10-12, wong2023coppereffluxsystem pages 5-8) | Wong 2023, *Infection and Immunity* | https://doi.org/10.1128/iai.00091-23 | Strong; assay-specific to tested CuSO4 ranges and strain background. |
| copZ metallochaperones—promote→copper tolerance | “single copA and copZ mutants… especially the double deletion copZA mutant exhibited decreased copper tolerance” (wong2023coppereffluxsystem pages 1-2, wong2023coppereffluxsystem pages 10-12, wong2023coppereffluxsystem pages 5-8) | Wong 2023, *Infection and Immunity* | https://doi.org/10.1128/iai.00091-23 | Strong in *H. influenzae*; tandem copy number may be lineage-specific. |
| CusS sensor kinase—senses→periplasmic copper ions | “evidence was obtained that the two-component regulatory system CusSR… does indeed sense periplasmic copper ions” (rismondo2023thesensoryhistidine pages 1-2, rismondo2023thesensoryhistidine pages 2-5) | Rismondo 2023, *Microbiology Spectrum* | https://doi.org/10.1128/spectrum.00291-23 | Strong; topology + mutational + physiological data in *E. coli*. |
| CusS/CusR signaling—activates→cusCFBA expression | “CusSR regulates expression of cusF and cusCBA” and sensing by CusS is required for Cus-mediated copper resistance (rismondo2023thesensoryhistidine pages 1-2, rismondo2023thesensoryhistidine pages 2-5) | Rismondo 2023, *Microbiology Spectrum* | https://doi.org/10.1128/spectrum.00291-23 | Strong; regulatory edge directly supported; expression-to-phenotype link is explicit. |
| cusS deletion—decreases→anaerobic copper resistance | “wild-type IC50 was >100 mM anaerobically versus ~25 mM for the ΔcusS mutant” in LB (rismondo2023thesensoryhistidine pages 5-8) | Rismondo 2023, *Microbiology Spectrum* | https://doi.org/10.1128/spectrum.00291-23 | Strong, condition-specific; oxygen and medium dependence should be preserved in curation. |
| CusR—activates→pcoA2 nine-gene operon | “CusR’s primary target is the pcoA2 operon” and Cu induces cusR and pcoA2; in a cusR deletion, pcoA2 is not induced (elsen2024crossregulationandcrosstalk pages 9-11, elsen2024crossregulationandcrosstalk pages 3-5, elsen2024crossregulationandcrosstalk pages 5-7) | Elsen 2024, *PLOS Genetics* | https://doi.org/10.1371/journal.pgen.1011325 | Strong in *Pseudomonas paraeruginosa* IHMA87; operon is ICE-associated accessory locus. |
| pcoA2 operon expression—increases→copper resistance | “basal pcoA2 expression confers some resistance” and overexpression “improves growth” while disruption “increases copper sensitivity” (elsen2024crossregulationandcrosstalk pages 5-7, elsen2024crossregulationandcrosstalk pages 7-9) | Elsen 2024, *PLOS Genetics* | https://doi.org/10.1371/journal.pgen.1011325 | Strong but locus-specific; likely curatable as accessory route in some pseudomonads rather than universal mechanism. |
| CopR—represses→pcoA2 promoter activity | “CopR appears to act negatively on the divergent pcoA2 promoter by competing with CusR for the same palindrome” (elsen2024crossregulationandcrosstalk pages 7-9, elsen2024crossregulationandcrosstalk pages 9-11) | Elsen 2024, *PLOS Genetics* | https://doi.org/10.1371/journal.pgen.1011325 | Strong regulatory edge; useful for graphing control logic rather than trait-defining mechanism alone. |
| CzcR—activates→pcoA2/cus regulatory region | “CzcR… activates pcoA2 to levels comparable to copper-induced CusR activation” via the same palindromic site (elsen2024crossregulationandcrosstalk pages 9-11) | Elsen 2024, *PLOS Genetics* | https://doi.org/10.1371/journal.pgen.1011325 | Moderate; demonstrates Zn–Cu cross-regulation; may be too taxon-/network-specific for core TraitMech unless marked uncertain. |
| pcoABCD cluster—mediates→anaerobic copper resistance | “pco+ strains… had an MIC of 7 mM, whereas the SL-4ΔpcoABCD deletion mutant and WT had MICs of 1 mM” anaerobically; all strains 8 mM aerobically (hikal2024theacquiredpco pages 3-4, hikal2024theacquiredpco pages 7-9) | Hikal 2024, *Frontiers in Microbiology* | https://doi.org/10.3389/fmicb.2024.1454763 | Strong, assay-specific in *Salmonella enterica*; clear oxygen dependence makes this a high-confidence conditional edge. |
| copper exposure—induces→EPS production | “the addition of 1 mM Cu(II) significantly induced the production of EPS,” e.g., Halomonas CuT3-1 EPS from 379.65 to 1013.00 mg/L (yu2024isolationofhighly pages 6-8, yu2024isolationofhighly pages 4-6) | Yu 2024, *Frontiers in Microbiology* | https://doi.org/10.3389/fmicb.2024.1390451 | Strong for selected deep-sea isolates; mechanism likely sequestration rather than canonical efflux. |
| EPS biosorption—decreases→bioavailable copper | crude EPS “could absorb 40 to 50 mg·g−1 copper”; max binding 52.24 mg/g for CuT6 EPS (yu2024isolationofhighly pages 9-11, yu2024isolationofhighly pages 6-8) | Yu 2024, *Frontiers in Microbiology* | https://doi.org/10.3389/fmicb.2024.1390451 | Moderate-to-strong; support for extracellular sequestration mechanism; species/isolate-specific and not necessarily universal. |
| P1B-1/P-type ATPase copper efflux—decreases→cytoplasmic copper toxicity | “primary defense is active efflux via P1B-1 (P-type) ATPases” and in Gram-negatives “CopA pumps cytoplasmic Cu(I) to the periplasm” (rebelo2023unravelingtherole pages 6-8) | Rebelo 2023, *Antibiotics* | https://doi.org/10.3390/antibiotics12091474 | Review-level support; broad mechanistic edge suitable for high-level graph node, but primary-source backing is preferable for final curation. |
| CueO multicopper oxidase—oxidizes→Cu(I) to Cu(II) in the periplasm | “CueO… oxidizes Cu(I) to less-toxic Cu(II) in oxygen” (rebelo2023unravelingtherole pages 6-8) | Rebelo 2023, *Antibiotics* | https://doi.org/10.3390/antibiotics12091474 | Review-level, aerobic-context edge; useful as generalized mechanism with note that oxygen is required. |
| copper excess—causes→ROS/protein/DNA damage | “Cu(I) driving Fenton-like reactions… causing damage to lipids, proteins and DNA” and disrupting Fe–S clusters (rebelo2023unravelingtherole pages 6-8) | Rebelo 2023, *Antibiotics* | https://doi.org/10.3390/antibiotics12091474 | Background toxicity edge defines why tolerance mechanisms matter; review-derived and not itself trait-sufficient. |


*Table: This table compiles candidate causal edges for a TraitMech graph of microbial copper tolerance, emphasizing evidence-backed mechanisms from 2023–2024 studies and a recent mechanistic review. It highlights core efflux, sensing, oxidation, regulation, and sequestration routes, with notes on assay conditions and uncertainty for curation.*

---

## Ontology grounding notes (practical)
- Prefer curating **mechanistic nodes at the level of gene/protein complexes** (e.g., CusCBA complex, CopA ATPase) and **compartment-specific copper pools** (cytoplasmic Cu(I), periplasmic Cu(I)) when supported by evidence of periplasmic sensing/efflux (rismondo2023thesensoryhistidine pages 1-2, rismondo2023thesensoryhistidine pages 5-8).
- Encode oxygen as an **environmental condition node** driving conditional edges (e.g., “anaerobic environment → CueO inactive → Cus importance increases” and “anaerobic environment → pcoABCD mediates resistance”) (rismondo2023thesensoryhistidine pages 5-8, hikal2024theacquiredpco pages 3-4).

---

## Warnings / claims that should not yet be curated into TraitMech
1. **Review-derived generalizations without primary phenotypes**: statements like “primary defense is active efflux via P-type ATPases” are useful framing but should be curated as background unless paired with primary experimental evidence in the same taxon/assay (rebelo2023unravelingtherole pages 6-8).
2. **Accessory loci without phenotype linkage in the target organism/assay**: many pco/sil/cus loci are mobile and prevalent, but curation should require explicit demonstration of copper tolerance contribution (Elsen and Hikal provide this; many genomics-only studies would not) (elsen2024crossregulationandcrosstalk pages 9-11, hikal2024theacquiredpco pages 3-4).
3. **EPS sequestration as ‘tolerance’ vs ‘detoxification’**: EPS biosorption can confer apparent tolerance by reducing free copper; whether to encode it as part of the core copper tolerant trait depends on TraitMech scope (environmental tolerance vs intracellular detox). Mark as a separate mechanistic branch if included (yu2024isolationofhighly pages 6-8, yu2024isolationofhighly media 3f7f73b3).
4. **Cross-talk/cross-regulation edges may be strain-specific**: e.g., CzcR/CopR/CusR competition on a shared palindrome is likely limited to taxa encoding the accessory ICE locus studied; curate as “accessory regulatory integration” with uncertainty flags (elsen2024crossregulationandcrosstalk pages 9-11, elsen2024crossregulationandcrosstalk pages 16-18).

---

# DOI-first bibliography (with dates and URLs where available)

1. Elsen S, Simon V, Attrée I. **Cross-regulation and cross-talk of conserved and accessory two-component regulatory systems orchestrate Pseudomonas copper resistance.** *PLOS Genetics*. 2024-06. DOI: **10.1371/journal.pgen.1011325**. URL: https://doi.org/10.1371/journal.pgen.1011325 (elsen2024crossregulationandcrosstalk pages 3-5, elsen2024crossregulationandcrosstalk pages 5-7)
2. Hikal AF, Hasan S, Gudeta DD, et al. **The acquired pco gene cluster in Salmonella enterica mediates resistance to copper.** *Frontiers in Microbiology*. 2024-09. DOI: **10.3389/fmicb.2024.1454763**. URL: https://doi.org/10.3389/fmicb.2024.1454763 (hikal2024theacquiredpco pages 3-4, hikal2024theacquiredpco pages 7-9)
3. Yu T, Qin M, Shao Z, Zhao Y, Zeng X. **Isolation of highly copper-resistant bacteria from deep-sea hydrothermal fields and description of a novel species Marinobacter metalliresistant sp. nov.** *Frontiers in Microbiology*. 2024-08. DOI: **10.3389/fmicb.2024.1390451**. URL: https://doi.org/10.3389/fmicb.2024.1390451 (yu2024isolationofhighly pages 6-8, yu2024isolationofhighly media cbe76ea6, yu2024isolationofhighly media 3f7f73b3)
4. Wong SM, Gawronski J, Akerley BJ. **Copper Efflux System Required in Murine Lung Infection by Haemophilus influenzae Composed of a Canonical ATPase Gene and Tandem Chaperone Gene Copies.** *Infection and Immunity*. 2023-05. DOI: **10.1128/iai.00091-23**. URL: https://doi.org/10.1128/iai.00091-23 (wong2023coppereffluxsystem pages 8-10, wong2023coppereffluxsystem pages 5-8)
5. Hirth N, Gerlach M-S, Wiesemann N, et al. **Full Copper Resistance in Cupriavidus metallidurans Requires the Interplay of Many Resistance Systems.** *Applied and Environmental Microbiology*. 2023-06. DOI: **10.1128/aem.00567-23**. URL: https://doi.org/10.1128/aem.00567-23 (hirth2023fullcopperresistance pages 16-18)
6. Rismondo J, Große C, Nies DH. **The Sensory Histidine Kinase CusS of Escherichia coli Senses Periplasmic Copper Ions.** *Microbiology Spectrum*. 2023-04. DOI: **10.1128/spectrum.00291-23**. URL: https://doi.org/10.1128/spectrum.00291-23 (rismondo2023thesensoryhistidine pages 5-8, rismondo2023thesensoryhistidine pages 1-2)
7. Rebelo A, Almeida A, Peixe L, Antunes P, Novais C. **Unraveling the Role of Metals and Organic Acids in Bacterial Antimicrobial Resistance in the Food Chain.** *Antibiotics*. 2023-09. DOI: **10.3390/antibiotics12091474**. URL: https://doi.org/10.3390/antibiotics12091474 (rebelo2023unravelingtherole pages 6-8)

---

## Visual evidence used
- Yu et al. 2024 Table 1 (maximum copper tolerance across isolates) and Figure 4 (EPS copper biosorption curves, 0–400 mg/L Cu(II)) were retrieved and support quantitative EPS-mediated sequestration and tolerance levels (yu2024isolationofhighly media cbe76ea6, yu2024isolationofhighly media 3f7f73b3).

References

1. (rismondo2023thesensoryhistidine pages 5-8): Jeanine Rismondo, Cornelia Große, and Dietrich H. Nies. The sensory histidine kinase cuss of escherichia coli senses periplasmic copper ions. Apr 2023. URL: https://doi.org/10.1128/spectrum.00291-23, doi:10.1128/spectrum.00291-23. This article has 14 citations and is from a domain leading peer-reviewed journal.

2. (hikal2024theacquiredpco pages 3-4): Ahmed F. Hikal, Sameer Hasan, Dereje D. Gudeta, Shaohua Zhao, Steven L. Foley, and Ashraf A Khan. The acquired pco gene cluster in salmonella enterica mediates resistance to copper. Frontiers in Microbiology, Sep 2024. URL: https://doi.org/10.3389/fmicb.2024.1454763, doi:10.3389/fmicb.2024.1454763. This article has 15 citations and is from a peer-reviewed journal.

3. (hirth2023fullcopperresistance pages 16-18): Niklas Hirth, Michelle-Sophie Gerlach, Nicole Wiesemann, Martin Herzberg, Cornelia Große, and Dietrich H. Nies. Full copper resistance in cupriavidus metallidurans requires the interplay of many resistance systems. Jun 2023. URL: https://doi.org/10.1128/aem.00567-23, doi:10.1128/aem.00567-23. This article has 18 citations and is from a peer-reviewed journal.

4. (rebelo2023unravelingtherole pages 6-8): Andreia Rebelo, Agostinho Almeida, Luísa Peixe, Patrícia Antunes, and Carla Novais. Unraveling the role of metals and organic acids in bacterial antimicrobial resistance in the food chain. Antibiotics, 12:1474, Sep 2023. URL: https://doi.org/10.3390/antibiotics12091474, doi:10.3390/antibiotics12091474. This article has 33 citations.

5. (elsen2024crossregulationandcrosstalk pages 9-11): Sylvie Elsen, Victor Simon, and Ina Attrée. Cross-regulation and cross-talk of conserved and accessory two-component regulatory systems orchestrate pseudomonas copper resistance. PLOS Genetics, 20:e1011325, Jun 2024. URL: https://doi.org/10.1371/journal.pgen.1011325, doi:10.1371/journal.pgen.1011325. This article has 10 citations and is from a domain leading peer-reviewed journal.

6. (yu2024isolationofhighly pages 6-8): Tong Yu, Meng Qin, Zongze Shao, Yuemei Zhao, and Xiang Zeng. Isolation of highly copper-resistant bacteria from deep-sea hydrothermal fields and description of a novel species marinobacter metalliresistant sp. nov. Frontiers in Microbiology, Aug 2024. URL: https://doi.org/10.3389/fmicb.2024.1390451, doi:10.3389/fmicb.2024.1390451. This article has 13 citations and is from a peer-reviewed journal.

7. (yu2024isolationofhighly media 3f7f73b3): Tong Yu, Meng Qin, Zongze Shao, Yuemei Zhao, and Xiang Zeng. Isolation of highly copper-resistant bacteria from deep-sea hydrothermal fields and description of a novel species marinobacter metalliresistant sp. nov. Frontiers in Microbiology, Aug 2024. URL: https://doi.org/10.3389/fmicb.2024.1390451, doi:10.3389/fmicb.2024.1390451. This article has 13 citations and is from a peer-reviewed journal.

8. (wong2023coppereffluxsystem pages 1-2): Sandy M. Wong, Jeffrey Gawronski, and Brian J. Akerley. Copper efflux system required in murine lung infection by haemophilus influenzae composed of a canonical atpase gene and tandem chaperone gene copies. Infection and Immunity, May 2023. URL: https://doi.org/10.1128/iai.00091-23, doi:10.1128/iai.00091-23. This article has 7 citations and is from a peer-reviewed journal.

9. (hikal2024theacquiredpco pages 7-9): Ahmed F. Hikal, Sameer Hasan, Dereje D. Gudeta, Shaohua Zhao, Steven L. Foley, and Ashraf A Khan. The acquired pco gene cluster in salmonella enterica mediates resistance to copper. Frontiers in Microbiology, Sep 2024. URL: https://doi.org/10.3389/fmicb.2024.1454763, doi:10.3389/fmicb.2024.1454763. This article has 15 citations and is from a peer-reviewed journal.

10. (wong2023coppereffluxsystem pages 8-10): Sandy M. Wong, Jeffrey Gawronski, and Brian J. Akerley. Copper efflux system required in murine lung infection by haemophilus influenzae composed of a canonical atpase gene and tandem chaperone gene copies. Infection and Immunity, May 2023. URL: https://doi.org/10.1128/iai.00091-23, doi:10.1128/iai.00091-23. This article has 7 citations and is from a peer-reviewed journal.

11. (wong2023coppereffluxsystem pages 5-8): Sandy M. Wong, Jeffrey Gawronski, and Brian J. Akerley. Copper efflux system required in murine lung infection by haemophilus influenzae composed of a canonical atpase gene and tandem chaperone gene copies. Infection and Immunity, May 2023. URL: https://doi.org/10.1128/iai.00091-23, doi:10.1128/iai.00091-23. This article has 7 citations and is from a peer-reviewed journal.

12. (rismondo2023thesensoryhistidine pages 1-2): Jeanine Rismondo, Cornelia Große, and Dietrich H. Nies. The sensory histidine kinase cuss of escherichia coli senses periplasmic copper ions. Apr 2023. URL: https://doi.org/10.1128/spectrum.00291-23, doi:10.1128/spectrum.00291-23. This article has 14 citations and is from a domain leading peer-reviewed journal.

13. (elsen2024crossregulationandcrosstalk pages 3-5): Sylvie Elsen, Victor Simon, and Ina Attrée. Cross-regulation and cross-talk of conserved and accessory two-component regulatory systems orchestrate pseudomonas copper resistance. PLOS Genetics, 20:e1011325, Jun 2024. URL: https://doi.org/10.1371/journal.pgen.1011325, doi:10.1371/journal.pgen.1011325. This article has 10 citations and is from a domain leading peer-reviewed journal.

14. (elsen2024crossregulationandcrosstalk pages 5-7): Sylvie Elsen, Victor Simon, and Ina Attrée. Cross-regulation and cross-talk of conserved and accessory two-component regulatory systems orchestrate pseudomonas copper resistance. PLOS Genetics, 20:e1011325, Jun 2024. URL: https://doi.org/10.1371/journal.pgen.1011325, doi:10.1371/journal.pgen.1011325. This article has 10 citations and is from a domain leading peer-reviewed journal.

15. (elsen2024crossregulationandcrosstalk pages 16-18): Sylvie Elsen, Victor Simon, and Ina Attrée. Cross-regulation and cross-talk of conserved and accessory two-component regulatory systems orchestrate pseudomonas copper resistance. PLOS Genetics, 20:e1011325, Jun 2024. URL: https://doi.org/10.1371/journal.pgen.1011325, doi:10.1371/journal.pgen.1011325. This article has 10 citations and is from a domain leading peer-reviewed journal.

16. (yu2024isolationofhighly pages 2-3): Tong Yu, Meng Qin, Zongze Shao, Yuemei Zhao, and Xiang Zeng. Isolation of highly copper-resistant bacteria from deep-sea hydrothermal fields and description of a novel species marinobacter metalliresistant sp. nov. Frontiers in Microbiology, Aug 2024. URL: https://doi.org/10.3389/fmicb.2024.1390451, doi:10.3389/fmicb.2024.1390451. This article has 13 citations and is from a peer-reviewed journal.

17. (yu2024isolationofhighly media cbe76ea6): Tong Yu, Meng Qin, Zongze Shao, Yuemei Zhao, and Xiang Zeng. Isolation of highly copper-resistant bacteria from deep-sea hydrothermal fields and description of a novel species marinobacter metalliresistant sp. nov. Frontiers in Microbiology, Aug 2024. URL: https://doi.org/10.3389/fmicb.2024.1390451, doi:10.3389/fmicb.2024.1390451. This article has 13 citations and is from a peer-reviewed journal.

18. (hikal2024theacquiredpco pages 2-3): Ahmed F. Hikal, Sameer Hasan, Dereje D. Gudeta, Shaohua Zhao, Steven L. Foley, and Ashraf A Khan. The acquired pco gene cluster in salmonella enterica mediates resistance to copper. Frontiers in Microbiology, Sep 2024. URL: https://doi.org/10.3389/fmicb.2024.1454763, doi:10.3389/fmicb.2024.1454763. This article has 15 citations and is from a peer-reviewed journal.

19. (wong2023coppereffluxsystem pages 10-12): Sandy M. Wong, Jeffrey Gawronski, and Brian J. Akerley. Copper efflux system required in murine lung infection by haemophilus influenzae composed of a canonical atpase gene and tandem chaperone gene copies. Infection and Immunity, May 2023. URL: https://doi.org/10.1128/iai.00091-23, doi:10.1128/iai.00091-23. This article has 7 citations and is from a peer-reviewed journal.

20. (rismondo2023thesensoryhistidine pages 2-5): Jeanine Rismondo, Cornelia Große, and Dietrich H. Nies. The sensory histidine kinase cuss of escherichia coli senses periplasmic copper ions. Apr 2023. URL: https://doi.org/10.1128/spectrum.00291-23, doi:10.1128/spectrum.00291-23. This article has 14 citations and is from a domain leading peer-reviewed journal.

21. (elsen2024crossregulationandcrosstalk pages 7-9): Sylvie Elsen, Victor Simon, and Ina Attrée. Cross-regulation and cross-talk of conserved and accessory two-component regulatory systems orchestrate pseudomonas copper resistance. PLOS Genetics, 20:e1011325, Jun 2024. URL: https://doi.org/10.1371/journal.pgen.1011325, doi:10.1371/journal.pgen.1011325. This article has 10 citations and is from a domain leading peer-reviewed journal.

22. (yu2024isolationofhighly pages 4-6): Tong Yu, Meng Qin, Zongze Shao, Yuemei Zhao, and Xiang Zeng. Isolation of highly copper-resistant bacteria from deep-sea hydrothermal fields and description of a novel species marinobacter metalliresistant sp. nov. Frontiers in Microbiology, Aug 2024. URL: https://doi.org/10.3389/fmicb.2024.1390451, doi:10.3389/fmicb.2024.1390451. This article has 13 citations and is from a peer-reviewed journal.

23. (yu2024isolationofhighly pages 9-11): Tong Yu, Meng Qin, Zongze Shao, Yuemei Zhao, and Xiang Zeng. Isolation of highly copper-resistant bacteria from deep-sea hydrothermal fields and description of a novel species marinobacter metalliresistant sp. nov. Frontiers in Microbiology, Aug 2024. URL: https://doi.org/10.3389/fmicb.2024.1390451, doi:10.3389/fmicb.2024.1390451. This article has 13 citations and is from a peer-reviewed journal.