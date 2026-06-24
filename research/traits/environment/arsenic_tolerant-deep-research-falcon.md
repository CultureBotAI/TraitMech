---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T21:22:11.412611'
end_time: '2026-06-17T21:46:22.165402'
duration_seconds: 1450.75
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: arsenic tolerant
  trait_identifier: traitmech:000017
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: arsenic_tolerant
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A metalloid tolerance in which an organism grows in the presence of
    elevated arsenic (arsenite/arsenate) concentrations, typically via the ars operon,
    whose ArsB pump extrudes arsenite from the cytoplasm.
  parent_traits: traitmech:000012
  synonyms: arsenic resistant
  evidence_summary: 'DOI:10.3389/fmicb.2018.02473: ArsB is an integral membrane protein
    able to extrude arsenite from the cell cytoplasm, thus diminishing arsenite accumulation
    (Review supports the ars operon as a near-ubiquitous arsenic-resistance determinant,
    "more common than genes for tryptophan biosynthesis".) | DOI:10.3389/fmicb.2020.00047:
    C. metallidurans BS1 conferred resistance to Zn2+ displaying a MIC of 20 mM, Cd2+
    (2.5 mM), Co2+ (20mM), Ni2+ (8 mM), As3+ (3.5 mM), Cu2+ (5 mM), Au3+ (1 uM) and
    Pb2+ (1.7 mM) (Organism example: Cupriavidus metallidurans BS1 tolerates arsenite
    (As3+) to a MIC of 3.5 mM.)'
  causal_graph_summary: 'arsenic_tolerance_ars_efflux: 4 nodes, 3 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 30
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** arsenic tolerant
- **METPO identifier:** traitmech:000017
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metalloid tolerance in which an organism grows in the presence of elevated arsenic (arsenite/arsenate) concentrations, typically via the ars operon, whose ArsB pump extrudes arsenite from the cytoplasm.
- **Parent traits:** traitmech:000012
- **Synonyms:** arsenic resistant
- **Existing evidence:** DOI:10.3389/fmicb.2018.02473: ArsB is an integral membrane protein able to extrude arsenite from the cell cytoplasm, thus diminishing arsenite accumulation (Review supports the ars operon as a near-ubiquitous arsenic-resistance determinant, "more common than genes for tryptophan biosynthesis".) | DOI:10.3389/fmicb.2020.00047: C. metallidurans BS1 conferred resistance to Zn2+ displaying a MIC of 20 mM, Cd2+ (2.5 mM), Co2+ (20mM), Ni2+ (8 mM), As3+ (3.5 mM), Cu2+ (5 mM), Au3+ (1 uM) and Pb2+ (1.7 mM) (Organism example: Cupriavidus metallidurans BS1 tolerates arsenite (As3+) to a MIC of 3.5 mM.)
- **Existing causal graph summary:** arsenic_tolerance_ars_efflux: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **arsenic tolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/arsenic_tolerant.yaml`.

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
- **Trait label:** arsenic tolerant
- **METPO identifier:** traitmech:000017
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metalloid tolerance in which an organism grows in the presence of elevated arsenic (arsenite/arsenate) concentrations, typically via the ars operon, whose ArsB pump extrudes arsenite from the cytoplasm.
- **Parent traits:** traitmech:000012
- **Synonyms:** arsenic resistant
- **Existing evidence:** DOI:10.3389/fmicb.2018.02473: ArsB is an integral membrane protein able to extrude arsenite from the cell cytoplasm, thus diminishing arsenite accumulation (Review supports the ars operon as a near-ubiquitous arsenic-resistance determinant, "more common than genes for tryptophan biosynthesis".) | DOI:10.3389/fmicb.2020.00047: C. metallidurans BS1 conferred resistance to Zn2+ displaying a MIC of 20 mM, Cd2+ (2.5 mM), Co2+ (20mM), Ni2+ (8 mM), As3+ (3.5 mM), Cu2+ (5 mM), Au3+ (1 uM) and Pb2+ (1.7 mM) (Organism example: Cupriavidus metallidurans BS1 tolerates arsenite (As3+) to a MIC of 3.5 mM.)
- **Existing causal graph summary:** arsenic_tolerance_ars_efflux: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **arsenic tolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/arsenic_tolerant.yaml`.

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


## Microbial trait causal graph curation report: **arsenic tolerant** (traitmech:000017)

### 1) Scope summary (TraitMech curation view)

**Trait definition (operational):** *Arsenic tolerant* (syn. arsenic resistant) should be curated as a **phenotypic growth/survival capacity** in the presence of elevated **arsenite (As(III))** and/or **arsenate (As(V))**, usually quantified as **MIC/MTC** (minimum inhibitory concentration / maximum tolerable concentration) under defined culture conditions. A clear recent operationalization is microtiter-plate growth screening across concentration gradients of sodium arsenate and sodium arsenite (0–320 mM As(V); 0–32 mM As(III)) to determine maximum tolerable concentrations (MTCs). (haghi2023arsenicpollutionand pages 3-4)

**Mechanistic core (current understanding):** The trait is most directly linked to **detoxification modules** (classically the **ars** operon), which combine (i) regulation by an arsenic-sensing repressor (**ArsR**), (ii) intracellular reduction of **As(V) → As(III)** by **ArsC**, and (iii) **As(III) efflux** by **ArsB** (optionally energized by **ArsA**) with accessory **ArsD** chaperoning As(III) to the pump. (rebelo2023unravelingtherole pages 11-13, william2023arsenicandmicroorganisms pages 4-6)

**Boundary cases / nearby traits (do not conflate):**
- **Arsenite oxidation** (aio/aox/arx systems) and **respiratory arsenate reduction** (arr system) are **arsenic energy metabolisms** that interconvert As species and can be detoxifying or bioenergetic depending on context; they should be curated as separate traits unless a study explicitly links them to *growth under arsenic stress* in the relevant assay. (william2023arsenicandmicroorganisms pages 4-6, rebelo2023unravelingtherole pages 11-13, rueangmongkolrat2024theroleof pages 1-2)
- **General metal tolerance** (multi-metal resistance islands) frequently co-occurs with arsenic tolerance but should not be merged into this trait unless mechanistically causal for As tolerance under the assay. (rebelo2023unravelingtherole pages 11-13)

---

### 2) Key concepts and definitions (current understanding)

#### 2.1 Core ars detoxification paradigm
- **Regulation:** ArsR binds an ars promoter to repress transcription in the absence of As(III); As(III) binding to ArsR causes conformational change and de-repression (activation) of downstream expression. (zhang2024wholecellbioreportertechnology pages 2-3, rebelo2023unravelingtherole pages 11-13)
- **Reduction:** ArsC reduces intracellular arsenate (As(V)) to arsenite (As(III)), which is typically the substrate for efflux. (rebelo2023unravelingtherole pages 11-13)
- **Efflux:** ArsB is an integral membrane arsenite efflux pump that extrudes arsenite from the cytoplasm; it can operate using membrane potential and can be coupled to ArsA for ATP-driven efflux. (rebelo2023unravelingtherole pages 11-13)
- **Accessory chaperoning:** ArsD can act as a metallochaperone transferring cytosolic arsenite to ArsA, improving efflux efficiency in extended ars operons. (rebelo2023unravelingtherole pages 11-13)
- **Alternative efflux:** **Acr3** is another inorganic arsenic efflux pump used by some microbes; it is frequently discussed as functionally analogous to ArsB but distinct in sequence and family. (william2023arsenicandmicroorganisms pages 4-6, rebelo2023unravelingtherole pages 11-13)

#### 2.2 Uptake routes that set intracellular arsenic burden
- **Arsenate entry:** arsenate can enter via **phosphate transporters** (Pit/Pst) due to chemical similarity to phosphate. (rebelo2023unravelingtherole pages 11-13)
- **Arsenite entry:** arsenite can enter via **aquaglyceroporins** (e.g., GlpF). (rebelo2023unravelingtherole pages 11-13)

These uptake edges are important because they influence how much substrate ArsC/efflux systems must handle, and can modulate measured MIC/MTC.

#### 2.3 Adjacent arsenic transformations
- **Methylation/volatilization (detoxification-associated in many contexts):** arsM encodes an arsenite S-adenosylmethionine methyltransferase producing volatile methylated arsenicals; in agricultural soils, authors interpret a “cooperative” detoxification sequence where arsC-mediated reduction supplies As(III) that is then methylated by arsM. (rueangmongkolrat2024theroleof pages 18-19, rueangmongkolrat2024theroleof pages 2-4)
- **Methylarsenical oxidation:** arsH and arsV oxidize methylated As(III) to methylated As(V). (zhuang2023biogeochemicalbehaviorand pages 5-6)
- **Demethylation:** ArsI (C–As lyase) demethylates MAs(III) to As(III). (zhuang2023biogeochemicalbehaviorand pages 5-6)

#### 2.4 Energy metabolisms (distinguish from tolerance trait)
- **Arsenite oxidation:** aioBA encodes arsenite oxidase subunits for aerobic As(III) oxidation; may contribute to detoxification or energy acquisition. (william2023arsenicandmicroorganisms pages 4-6)
- **Respiratory arsenate reduction:** arr genes encode respiratory arsenate reductase ArrAB, used in anaerobic respiration. (william2023arsenicandmicroorganisms pages 4-6)

---

### 3) Candidate nodes for `arsenic_tolerant.yaml` (grouped by type)

#### 3.1 Chemicals / ions / substrates
- **Arsenite (As(III))** — CHEBI:27563 (rebelo2023unravelingtherole pages 11-13)
- **Arsenate (As(V))** — CHEBI:30667 (rebelo2023unravelingtherole pages 11-13)
- Sodium arsenate (assay reagent; grounding uncertain) (haghi2023arsenicpollutionand pages 3-4)
- Sodium arsenite (assay reagent; grounding uncertain) (haghi2023arsenicpollutionand pages 3-4)
- Volatile methylated arsenic (label-only; product of arsM interpretation) (rueangmongkolrat2024theroleof pages 18-19)

#### 3.2 Genes/proteins/complexes (core detox)
- **ArsR** (ars operon repressor/sensor) (zhang2024wholecellbioreportertechnology pages 2-3)
- **ArsC** (arsenate reductase) (rebelo2023unravelingtherole pages 11-13)
- **ArsB** (arsenite efflux permease) (rebelo2023unravelingtherole pages 11-13)
- **ArsA** (ATPase energizing efflux with ArsB) (rebelo2023unravelingtherole pages 11-13)
- **ArsD** (metallochaperone transferring As(III) to ArsA) (rebelo2023unravelingtherole pages 11-13)
- **Acr3** (alternative inorganic arsenic efflux pump) (william2023arsenicandmicroorganisms pages 4-6)

#### 3.3 Genes/proteins (uptake)
- **Pit/Pst phosphate transporters** (arsenate uptake route) (rebelo2023unravelingtherole pages 11-13)
- **GlpF aquaglyceroporin** (arsenite uptake route) (rebelo2023unravelingtherole pages 11-13)

#### 3.4 Genes/proteins (methylation/detox adjunct)
- **ArsM** (arsenite methyltransferase) (rueangmongkolrat2024theroleof pages 2-4)
- **ArsH, ArsV** (methylarsenite oxidases) (zhuang2023biogeochemicalbehaviorand pages 5-6)
- **ArsI** (C–As lyase; demethylation) (zhuang2023biogeochemicalbehaviorand pages 5-6)
- **ArsP/ArsK/ArsW** (methylated arsenical efflux; label-only from review table) (zhuang2023biogeochemicalbehaviorand pages 5-6)

#### 3.5 Pathways/modules (adjacent; boundary)
- **aioBA / AioBA arsenite oxidase** (As(III) oxidation) (william2023arsenicandmicroorganisms pages 4-6)
- **arrAB / ArrAB respiratory arsenate reductase** (dissimilatory As(V) reduction) (william2023arsenicandmicroorganisms pages 4-6)

#### 3.6 Environmental/assay factors (important for causal graph)
- **Arsenic speciation**: As(III) vs As(V) (rebelo2023unravelingtherole pages 11-13)
- **Matrix**: agricultural soil (ENVO:00001998 candidate) (rueangmongkolrat2024theroleof pages 1-2)
- **Groundwater arsenic concentration** (0.23 mg/L in one dataset) (diba2023metagenomicandculturedependent pages 1-2)
- **Culture condition modifiers**: pH, salinity, temperature; can be explicitly represented as experimental factors where known (pH 9.5; 7.5% NaCl; 30°C in one isolation) (haghi2023arsenicpollutionand pages 3-4)

---

### 4) Evidence-backed candidate causal edges (curation-ready)

The table below lists **candidate subject–predicate–object edges** with **direct supporting snippets** and curation notes.

| Edge (subject–predicate–object) | Evidence snippet (short quote) | Source (DOI, year, URL) | Curation notes/uncertainty | Suggested grounding (CURIEs where possible) |
|---|---|---|---|---|
| As(III)–bound ArsR → relieves repression of → ars operon transcription | “arsR encodes the ArsR regulatory protein that binds the ParsR promoter (ABS) to repress transcription in the absence of As(III); binding of As(III) to ArsR changes its conformation and relieves repression” (zhang2024wholecellbioreportertechnology pages 2-3) | 10.3389/fmicb.2024.1494872, 2024, https://doi.org/10.3389/fmicb.2024.1494872 | Strong evidence for regulator-level edge; assay context from WCB review. Curate at protein/process level, not necessarily operon architecture for all taxa. | CHEBI:27563 arsenite; arsR (label); ParsR promoter (label); GO:0006355 regulation of DNA-templated transcription |
| ArsR → represses → ars promoter | “ArsR is a trans-acting transcriptional repressor that binds the ars promoter” (rebelo2023unravelingtherole pages 11-13) | 10.3390/antibiotics12091474, 2023, https://doi.org/10.3390/antibiotics12091474 | Strong review support; broadly applicable canonical ars operons. | arsR (label); ars promoter (label); GO:0001217 DNA-binding transcription repressor activity |
| ArsC → reduces → As(V) to As(III) | “ArsC is an arsenate reductase that converts intracellular As(V) to As(III)” (rebelo2023unravelingtherole pages 11-13) | 10.3390/antibiotics12091474, 2023, https://doi.org/10.3390/antibiotics12091474 | Core detoxification edge; central for trait scope. | arsC (label); CHEBI:30667 arsenate(3-); CHEBI:27563 arsenite; GO:0018802 arsenate reductase (glutaredoxin) activity |
| ArsB → exports → As(III) from cytoplasm | “ArsB is an integral membrane arsenite efflux pump that extrudes As(OH)3/As3+ from the cytoplasm” (rebelo2023unravelingtherole pages 11-13) | 10.3390/antibiotics12091474, 2023, https://doi.org/10.3390/antibiotics12091474 | Strong direct mechanistic support; near-core edge for TraitMech. | arsB (label); CHEBI:27563 arsenite; GO:0015386 arsenite transmembrane transporter activity |
| ArsA → energizes → ArsB-mediated As(III) efflux | “ArsA is an ATPase that hydrolyzes ATP to energize the ArsA–ArsB efflux complex” (rebelo2023unravelingtherole pages 11-13) | 10.3390/antibiotics12091474, 2023, https://doi.org/10.3390/antibiotics12091474 | Strong for extended ars operons; not universal because some ArsB pumps function without ArsA. | arsA (label); arsB (label); GO:0016887 ATP hydrolysis activity |
| ArsD → transfers As(III) to → ArsA | “ArsD acts as a metallochaperone transferring cytosolic arsenite to ArsA” (rebelo2023unravelingtherole pages 11-13) | 10.3390/antibiotics12091474, 2023, https://doi.org/10.3390/antibiotics12091474 | Strong but limited to arsD-containing systems; curate as optional/extended mechanism. | arsD (label); arsA (label); CHEBI:27563 arsenite |
| Acr3 → exports → As(III) | “some bacteria possess acr3, coding for an inorganic arsenic efflux pump” (william2023arsenicandmicroorganisms pages 4-6) | 10.3390/microorganisms12010074, 2023, https://doi.org/10.3390/microorganisms12010074 | Strong alternative efflux route; should be modeled alongside ArsB, not merged with it. | acr3 (label); CHEBI:27563 arsenite; GO:0015386 arsenite transmembrane transporter activity |
| Pit/Pst phosphate transporters → import → As(V) | “uptake via phosphate transporters (Pit/Pst) for arsenate” (rebelo2023unravelingtherole pages 11-13) | 10.3390/antibiotics12091474, 2023, https://doi.org/10.3390/antibiotics12091474 | Important boundary/input edge; promiscuous uptake, not tolerance per se. | Pit (label); Pst (label); CHEBI:30667 arsenate(3-) |
| GlpF aquaglyceroporin → imports → As(III) | “uptake via… GlpF aquaglyceroporins for arsenite” (rebelo2023unravelingtherole pages 11-13) | 10.3390/antibiotics12091474, 2023, https://doi.org/10.3390/antibiotics12091474 | Important entry route; in some contexts altered uptake affects tolerance. | glpF (label); CHEBI:27563 arsenite; GO:0015250 water channel activity |
| ArsM → methylates → As(III) | “arsM (arsenite S-adenosylmethionine methyltransferase) producing volatile methylated arsenicals” (rueangmongkolrat2024theroleof pages 2-4) | 10.7717/peerj.18383, 2024, https://doi.org/10.7717/peerj.18383 | Strong pathway edge; detoxifying in many contexts but can generate toxic intermediates. | arsM (label); CHEBI:27563 arsenite; CHEBI:34411 organoarsenic compound |
| ArsM-mediated methylation → leads to → volatile methylated arsenic | “the produced arsenite is then methylated by arsM to volatile methylated arsenic” (rueangmongkolrat2024theroleof pages 18-19) | 10.7717/peerj.18383, 2024, https://doi.org/10.7717/peerj.18383 | Good ecological/mechanistic support from 2024 soil metagenome interpretation; may be inferred rather than directly assayed in that study. | arsM (label); volatile methylated arsenic (label) |
| ArsH/ArsV → oxidize → methylated As(III) to methylated As(V) | “arsH and arsV oxidize methylated As(III) to methylated As(V)” (zhuang2023biogeochemicalbehaviorand pages 5-6) | 10.3389/fmicb.2023.1043024, 2023, https://doi.org/10.3389/fmicb.2023.1043024 | Strong review support; relevant for methylarsenical detoxification branch, not universal. | arsH (label); arsV (label); methylated As(III) (label); methylated As(V) (label) |
| ArsI → demethylates → MAs(III) to As(III) | “ArsI (ArsI C–As lyase) catalyzes demethylation of MAs(III) to As(III)” (zhuang2023biogeochemicalbehaviorand pages 5-6) | 10.3389/fmicb.2023.1043024, 2023, https://doi.org/10.3389/fmicb.2023.1043024 | Strong review support for detoxification of organoarsenicals; likely secondary branch for this trait. | arsI (label); MAs(III) (label); CHEBI:27563 arsenite |
| AioBA arsenite oxidase → oxidizes → As(III) to As(V) | “aioBA encodes AioA… and AioB… [and] catalyze aerobic As(III) oxidation” (william2023arsenicandmicroorganisms pages 4-6) | 10.3390/microorganisms12010074, 2023, https://doi.org/10.3390/microorganisms12010074 | Distinguish from tolerance core: oxidation can contribute to detoxification or energy metabolism depending taxon/context. Mark as adjacent trait mechanism unless linked to growth tolerance. | aioA (label); aioB (label); CHEBI:27563 arsenite; CHEBI:30667 arsenate(3-) |
| ArrAB respiratory reductase → reduces → As(V) in respiration | “arr genes encode the respiratory As(V) reductase ArrAB” (william2023arsenicandmicroorganisms pages 4-6) | 10.3390/microorganisms12010074, 2023, https://doi.org/10.3390/microorganisms12010074 | Important boundary edge: this is arsenate respiration/dissimilatory reduction, not canonical detox tolerance. Curate separately unless phenotype assay is tolerance-focused. | arrA (label); arrB (label); CHEBI:30667 arsenate(3-) |
| ParsR/ArsR sensing module fused to reporter → detects → As(III) in whole-cell bioreporters | “WCBs use sensing elements from the ars operon (typically ParsR/ArsR) fused to reporter genes… so that promoter de-repression by As(III) produces a measurable optical signal” (zhang2024wholecellbioreportertechnology pages 2-3) | 10.3389/fmicb.2024.1494872, 2024, https://doi.org/10.3389/fmicb.2024.1494872 | Application edge rather than native physiology; useful for implementation section, not core TraitMech unless engineering nodes are allowed. | ParsR promoter (label); ArsR (label); reporter gene (label); CHEBI:27563 arsenite |
| Increasing external As(V)/As(III) concentration in microtiter plates → assays → arsenic tolerance phenotype (MTC) | “MTC screening was performed across 0–320 mM sodium arsenate and 0–32 mM sodium arsenite in 96-well plates” (haghi2023arsenicpollutionand pages 3-4) | 10.3389/fenvs.2023.1195643, 2023, https://doi.org/10.3389/fenvs.2023.1195643 | Strong assay-definition edge for phenotype measurement; supports trait scope and experimental factor nodes. | sodium arsenate (CHEBI:45217 candidate); sodium arsenite (label); assay in 96-well plate (label); traitmech:000017 |
| arsC abundance → exceeds → aioA and arrA abundance in low-As agricultural soils | “among four key markers the ordering of relative abundance was: arsC > arsM > aioA > arrA” (rueangmongkolrat2024theroleof pages 10-14) | 10.7717/peerj.18383, 2024, https://doi.org/10.7717/peerj.18383 | Environmental prevalence edge, not direct causality. Useful for prioritizing core nodes (arsC) but should be marked inferred/non-mechanistic. | arsC (label); arsM (label); aioA (label); arrA (label); ENVO:00001998 agricultural soil |
| Deleting/altering efflux-reduction routes (aCR3/arsenate reductase) → increases → intracellular arsenic accumulation | “modifying the bacterial cell efflux routes (ACR3) enhanced arsenic …” and “removal increased Corynebacterium glutamicum accumulation by 28–30×” (naiel2024thearsenicbioremediation pages 6-7) | 10.1016/j.heliyon.2024.e36314, 2024, https://doi.org/10.1016/j.heliyon.2024.e36314 | Real-world engineering edge for bioremediation; not native causal graph for tolerance because loss of detox increases accumulation rather than tolerance. Mark application-specific. | acr3 (label); arsC (label); intracellular arsenic accumulation (label) |


*Table: This table summarizes candidate causal edges for curating the microbial trait ‘arsenic tolerant’ into a TraitMech-style graph. It emphasizes the core ars detoxification machinery, adjacent arsenic transformation pathways, assay definitions, and application-oriented edges, with supporting recent citations and suggested ontology grounding.*

---

### 5) Recent developments and latest research (prioritizing 2023–2024)

#### 5.1 2024: whole-cell bioreporters (WCBs) based on ars regulation
A 2024 Frontiers in Microbiology review synthesizes WCB designs that use **ParsR/ArsR** regulatory elements fused to reporter genes (e.g., luciferase/GFP), producing an optical signal when **As(III) de-represses ArsR-controlled transcription**. This represents a mature, real-world implementation of ars regulatory biology for **bioavailable arsenic risk assessment**. (zhang2024wholecellbioreportertechnology pages 2-3)

#### 5.2 2024: microbiome-scale evidence for dominant detoxification modules in low-As agricultural soils
Shotgun metagenomics in surface agricultural soils (Thailand) reported low soil arsenic **7.60–10.28 mg/kg**, with relative abundance ordering **arsC > arsM > aioA > arrA**, interpreted as a cooperative detoxification regime emphasizing **arsenate reduction (arsC)** and **arsenic methylation (arsM)** rather than oxidation/respiration. (rueangmongkolrat2024theroleof pages 1-2, rueangmongkolrat2024theroleof pages 10-14)

#### 5.3 2024: engineered microbial bioremediation trends and quantitative performance claims
A 2024 Heliyon overview compiled applications where engineered or selected strains remove/accumulate arsenic, including rapid reductions in aqueous arsenic (e.g., **Pseudomonas aeruginosa** reported to remove **90.72% in 30 min** and **97.92% in 2 h**) and bioaccumulation capacities reported in mg/g ranges, alongside genetic levers (efflux/reductase route modification; methylation pathways such as arsM). (naiel2024thearsenicbioremediation pages 6-7)

#### 5.4 2023: mechanistic consolidation and co-selection framing
A 2023 review in *Antibiotics* emphasizes canonical ars modules (ArsR/ArsC/ArsB, with ArsA and ArsD in extended operons), documents **uptake via Pit/Pst and GlpF**, and frames arsenic as a potential selective pressure contributing to **co-selection** with antibiotic resistance via mobile elements (plasmids/ICEs). (rebelo2023unravelingtherole pages 11-13)

---

### 6) Statistics and data (recent studies)

#### 6.1 Strain-level tolerance (Urmia Salt Lake isolates; 2023)
Six isolates from the drying Urmia Salt Lake show high arsenate tolerance and more modest arsenite tolerance. **As(V) MTCs** include **320 mM** in multiple strains; **As(III) MTCs** are mostly **4 mM**, with one strain reaching **16 mM**. Gene screening shows **arsC present in all isolates**, while **arsB is variably present**; **arrB** and **arxA** are absent across these isolates. (haghi2023arsenicpollutionand pages 7-9, haghi2023arsenicpollutionand media 3a263597)

#### 6.2 Groundwater arsenic and isolate MIC range (Bangladesh; 2023)
In one BMC Microbiology study, groundwater samples had **average As concentration 0.23 mg/L**, and isolates associated with arsenite metabolism showed **MIC_As spanning 2–32 mM**. The study reports detection of arsenic-related genes including ars operon components and efflux-related genes (arsB, acr3) in its functional gene set. (diba2023metagenomicandculturedependent pages 1-2)

#### 6.3 Soil arsenic levels and functional gene prevalence (Thailand agricultural soil; 2024)
Surface agricultural soils were reported with arsenic **7.60–10.28 mg/kg** and showed the gene-abundance ordering **arsC > arsM > aioA > arrA** (shotgun metagenomics), supporting detoxification gene predominance at low arsenic levels. (rueangmongkolrat2024theroleof pages 1-2, rueangmongkolrat2024theroleof pages 10-14)

---

### 7) Expert opinions / authoritative analysis (as phrased in sources)

- **Canonical detoxification is ars-centered:** A 2023 review describes core ars operon modules where ArsR/ArsC/ArsB underpin tolerance, with ArsA and ArsD improving efflux efficiency. (rebelo2023unravelingtherole pages 11-13)
- **Energy metabolisms are distinct:** 2023 mechanistic synthesis distinguishes ars detoxification (ArsC reduction + efflux) from energy-linked arsenic transformations via **arr** (respiratory reduction) and **aio** (oxidation). (william2023arsenicandmicroorganisms pages 4-6, rebelo2023unravelingtherole pages 11-13)
- **Metagenome-informed interpretation in soils:** 2024 soil metagenome authors interpret high arsC and arsM prevalence as “cooperative detoxification” via reduction plus methylation. (rueangmongkolrat2024theroleof pages 18-19, rueangmongkolrat2024theroleof pages 10-14)

---

### 8) Warnings / curation cautions

1. **Do not curate aio/arr edges as core to ‘arsenic tolerant’ unless linked to tolerance assays.** Multiple sources treat aio/arx and arr as energy metabolisms rather than canonical detox tolerance. (william2023arsenicandmicroorganisms pages 4-6, rebelo2023unravelingtherole pages 11-13)
2. **Environmental gene abundance ≠ causal sufficiency.** Ordering such as arsC > arsM > aioA > arrA supports prioritization but is not direct causal evidence for tolerance without phenotype measurement. (rueangmongkolrat2024theroleof pages 10-14)
3. **Engineering/application edges should be separated from native trait mechanism edges.** WCB biosensors and engineered bioremediation strategies are valuable for “applications” but may not belong in a native TraitMech causal graph unless the ontology supports engineered constructs. (zhang2024wholecellbioreportertechnology pages 2-3, naiel2024thearsenicbioremediation pages 6-7)
4. **Gene names are taxon-dependent for stable IDs.** Prefer label nodes (e.g., “arsB (arsenite efflux permease)”) unless curating to a specific organism/UniProt.

---

## DOI-first bibliography (with dates, URLs)

1. **Zhang X, Zhao X, Gu C, et al.** Whole-cell bioreporter technology: a promising approach for environmental risk assessment of As contamination in soil. *Frontiers in Microbiology*. **2024-11**. DOI: **10.3389/fmicb.2024.1494872**. https://doi.org/10.3389/fmicb.2024.1494872 (zhang2024wholecellbioreportertechnology pages 2-3)
2. **Naiel MAE, Taher ES, Rashed F, et al.** The arsenic bioremediation using genetically engineered microbial strains on aquatic environments: An updated overview. *Heliyon*. **2024-09**. DOI: **10.1016/j.heliyon.2024.e36314**. https://doi.org/10.1016/j.heliyon.2024.e36314 (naiel2024thearsenicbioremediation pages 6-7)
3. **Rueangmongkolrat N, Uthaipaisanwong P, Kusonmano K, et al.** The role of microbiomes in cooperative detoxification mechanisms of arsenate reduction and arsenic methylation in surface agricultural soil. *PeerJ*. **2024-10**. DOI: **10.7717/peerj.18383**. https://doi.org/10.7717/peerj.18383 (rueangmongkolrat2024theroleof pages 1-2)
4. **William VU, Magpantay HD.** Arsenic and Microorganisms: Genes, Molecular Mechanisms, and Recent Advances in Microbial Arsenic Bioremediation. *Microorganisms*. **2023-12**. DOI: **10.3390/microorganisms12010074**. https://doi.org/10.3390/microorganisms12010074 (william2023arsenicandmicroorganisms pages 8-9)
5. **Rebelo A, Almeida A, Peixe L, Antunes P, Novais C.** Unraveling the Role of Metals and Organic Acids in Bacterial Antimicrobial Resistance in the Food Chain. *Antibiotics*. **2023-09**. DOI: **10.3390/antibiotics12091474**. https://doi.org/10.3390/antibiotics12091474 (rebelo2023unravelingtherole pages 11-13)
6. **Zhuang F, Huang J, Li H, et al.** Biogeochemical behavior and pollution control of arsenic in mining areas: A review. *Frontiers in Microbiology*. **2023-03**. DOI: **10.3389/fmicb.2023.1043024**. https://doi.org/10.3389/fmicb.2023.1043024 (zhuang2023biogeochemicalbehaviorand pages 5-6)
7. **Haghi M, Diznabi SH, Karaboz I, Omeroglu EE.** Arsenic pollution and arsenic-resistant bacteria of drying Urmia Salt Lake. *Frontiers in Environmental Science*. **2023-06**. DOI: **10.3389/fenvs.2023.1195643**. https://doi.org/10.3389/fenvs.2023.1195643 (haghi2023arsenicpollutionand pages 7-9, haghi2023arsenicpollutionand media 3a263597)
8. **Diba F, Hoque MN, Rahman MS, et al.** Metagenomic and culture-dependent approaches unveil active microbial community and novel functional genes involved in arsenic mobilization and detoxification in groundwater. *BMC Microbiology*. **2023-08**. DOI: **10.1186/s12866-023-02980-0**. https://doi.org/10.1186/s12866-023-02980-0 (diba2023metagenomicandculturedependent pages 1-2)


References

1. (haghi2023arsenicpollutionand pages 3-4): Morteza Haghi, Salar H. Diznabi, Ismail Karaboz, and Esra Ersoy Omeroglu. Arsenic pollution and arsenic-resistant bacteria of drying urmia salt lake. Frontiers in Environmental Science, Jun 2023. URL: https://doi.org/10.3389/fenvs.2023.1195643, doi:10.3389/fenvs.2023.1195643. This article has 11 citations and is from a peer-reviewed journal.

2. (rebelo2023unravelingtherole pages 11-13): Andreia Rebelo, Agostinho Almeida, Luísa Peixe, Patrícia Antunes, and Carla Novais. Unraveling the role of metals and organic acids in bacterial antimicrobial resistance in the food chain. Antibiotics, 12:1474, Sep 2023. URL: https://doi.org/10.3390/antibiotics12091474, doi:10.3390/antibiotics12091474. This article has 33 citations.

3. (william2023arsenicandmicroorganisms pages 4-6): Vladimir U. William and Hilbert D. Magpantay. Arsenic and microorganisms: genes, molecular mechanisms, and recent advances in microbial arsenic bioremediation. Microorganisms, 12:74, Dec 2023. URL: https://doi.org/10.3390/microorganisms12010074, doi:10.3390/microorganisms12010074. This article has 58 citations.

4. (rueangmongkolrat2024theroleof pages 1-2): Nattanan Rueangmongkolrat, Pichahpuk Uthaipaisanwong, Kanthida Kusonmano, Sasipa Pruksangkul, and Prinpida Sonthiphand. The role of microbiomes in cooperative detoxification mechanisms of arsenate reduction and arsenic methylation in surface agricultural soil. PeerJ, 12:e18383, Oct 2024. URL: https://doi.org/10.7717/peerj.18383, doi:10.7717/peerj.18383. This article has 2 citations and is from a peer-reviewed journal.

5. (zhang2024wholecellbioreportertechnology pages 2-3): Xiaokai Zhang, Xinyu Zhao, Caiwen Gu, Zefeng Huang, Tao Gan, Boling Li, Evrim Elçin, and Lizhi He. Whole-cell bioreporter technology: a promising approach for environmental risk assessment of as contamination in soil. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1494872, doi:10.3389/fmicb.2024.1494872. This article has 2 citations and is from a peer-reviewed journal.

6. (rueangmongkolrat2024theroleof pages 18-19): Nattanan Rueangmongkolrat, Pichahpuk Uthaipaisanwong, Kanthida Kusonmano, Sasipa Pruksangkul, and Prinpida Sonthiphand. The role of microbiomes in cooperative detoxification mechanisms of arsenate reduction and arsenic methylation in surface agricultural soil. PeerJ, 12:e18383, Oct 2024. URL: https://doi.org/10.7717/peerj.18383, doi:10.7717/peerj.18383. This article has 2 citations and is from a peer-reviewed journal.

7. (rueangmongkolrat2024theroleof pages 2-4): Nattanan Rueangmongkolrat, Pichahpuk Uthaipaisanwong, Kanthida Kusonmano, Sasipa Pruksangkul, and Prinpida Sonthiphand. The role of microbiomes in cooperative detoxification mechanisms of arsenate reduction and arsenic methylation in surface agricultural soil. PeerJ, 12:e18383, Oct 2024. URL: https://doi.org/10.7717/peerj.18383, doi:10.7717/peerj.18383. This article has 2 citations and is from a peer-reviewed journal.

8. (zhuang2023biogeochemicalbehaviorand pages 5-6): Fan Zhuang, Jingyi Huang, Hongguang Li, Xing Peng, Ling Xia, Lei Zhou, Teng Zhang, Zhenghua Liu, Qiang He, Feng Luo, Huaqun Yin, and Delong Meng. Biogeochemical behavior and pollution control of arsenic in mining areas: a review. Frontiers in Microbiology, Mar 2023. URL: https://doi.org/10.3389/fmicb.2023.1043024, doi:10.3389/fmicb.2023.1043024. This article has 69 citations and is from a peer-reviewed journal.

9. (diba2023metagenomicandculturedependent pages 1-2): Farzana Diba, M. Nazmul Hoque, M. Shaminur Rahman, Farhana Haque, Khondaker Md. Jaminur Rahman, Md. Moniruzzaman, Mala Khan, M. Anwar Hossain, and Munawar Sultana. Metagenomic and culture-dependent approaches unveil active microbial community and novel functional genes involved in arsenic mobilization and detoxification in groundwater. BMC Microbiology, Aug 2023. URL: https://doi.org/10.1186/s12866-023-02980-0, doi:10.1186/s12866-023-02980-0. This article has 19 citations and is from a peer-reviewed journal.

10. (rueangmongkolrat2024theroleof pages 10-14): Nattanan Rueangmongkolrat, Pichahpuk Uthaipaisanwong, Kanthida Kusonmano, Sasipa Pruksangkul, and Prinpida Sonthiphand. The role of microbiomes in cooperative detoxification mechanisms of arsenate reduction and arsenic methylation in surface agricultural soil. PeerJ, 12:e18383, Oct 2024. URL: https://doi.org/10.7717/peerj.18383, doi:10.7717/peerj.18383. This article has 2 citations and is from a peer-reviewed journal.

11. (naiel2024thearsenicbioremediation pages 6-7): Mohammed A.E. Naiel, Ehab S. Taher, Fatema Rashed, Shakira Ghazanfar, Abdelrazeq M. Shehata, Nourelhuda A. Mohammed, Raul Pascalau, Laura Smuleac, Ateya Megahed Ibrahim, Ahmed Abdeen, and Mustafa Shukry. The arsenic bioremediation using genetically engineered microbial strains on aquatic environments: an updated overview. Sep 2024. URL: https://doi.org/10.1016/j.heliyon.2024.e36314, doi:10.1016/j.heliyon.2024.e36314. This article has 20 citations.

12. (haghi2023arsenicpollutionand pages 7-9): Morteza Haghi, Salar H. Diznabi, Ismail Karaboz, and Esra Ersoy Omeroglu. Arsenic pollution and arsenic-resistant bacteria of drying urmia salt lake. Frontiers in Environmental Science, Jun 2023. URL: https://doi.org/10.3389/fenvs.2023.1195643, doi:10.3389/fenvs.2023.1195643. This article has 11 citations and is from a peer-reviewed journal.

13. (haghi2023arsenicpollutionand media 3a263597): Morteza Haghi, Salar H. Diznabi, Ismail Karaboz, and Esra Ersoy Omeroglu. Arsenic pollution and arsenic-resistant bacteria of drying urmia salt lake. Frontiers in Environmental Science, Jun 2023. URL: https://doi.org/10.3389/fenvs.2023.1195643, doi:10.3389/fenvs.2023.1195643. This article has 11 citations and is from a peer-reviewed journal.

14. (william2023arsenicandmicroorganisms pages 8-9): Vladimir U. William and Hilbert D. Magpantay. Arsenic and microorganisms: genes, molecular mechanisms, and recent advances in microbial arsenic bioremediation. Microorganisms, 12:74, Dec 2023. URL: https://doi.org/10.3390/microorganisms12010074, doi:10.3390/microorganisms12010074. This article has 58 citations.