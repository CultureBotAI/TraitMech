---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T23:41:14.934403'
end_time: '2026-06-18T00:01:14.486581'
duration_seconds: 1199.55
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: obligately aerobic
  trait_identifier: METPO:1000606
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: obligately_aerobic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "An oxygen preference that requires molecular oxygen (O\u2082) for growth."
  parent_traits: METPO:1000601
  synonyms: obligate aerobe, obligate aerobic
  evidence_summary: 'https://www.ncbi.nlm.nih.gov/books/NBK482349/: require oxygen
    as a terminal electron acceptor (Supports the requirement for oxygen in obligately
    aerobic organisms.) | PMID:27203084: M. tuberculosis is an obligate aerobe (Organism
    example: Mycobacterium tuberculosis is described as obligately aerobic.)'
  causal_graph_summary: 'obligate_aerobe_oxygen_respiration: 5 nodes, 4 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 36
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** obligately aerobic
- **METPO identifier:** METPO:1000606
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An oxygen preference that requires molecular oxygen (O₂) for growth.
- **Parent traits:** METPO:1000601
- **Synonyms:** obligate aerobe, obligate aerobic
- **Existing evidence:** https://www.ncbi.nlm.nih.gov/books/NBK482349/: require oxygen as a terminal electron acceptor (Supports the requirement for oxygen in obligately aerobic organisms.) | PMID:27203084: M. tuberculosis is an obligate aerobe (Organism example: Mycobacterium tuberculosis is described as obligately aerobic.)
- **Existing causal graph summary:** obligate_aerobe_oxygen_respiration: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **obligately aerobic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/obligately_aerobic.yaml`.

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
- **Trait label:** obligately aerobic
- **METPO identifier:** METPO:1000606
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An oxygen preference that requires molecular oxygen (O₂) for growth.
- **Parent traits:** METPO:1000601
- **Synonyms:** obligate aerobe, obligate aerobic
- **Existing evidence:** https://www.ncbi.nlm.nih.gov/books/NBK482349/: require oxygen as a terminal electron acceptor (Supports the requirement for oxygen in obligately aerobic organisms.) | PMID:27203084: M. tuberculosis is an obligate aerobe (Organism example: Mycobacterium tuberculosis is described as obligately aerobic.)
- **Existing causal graph summary:** obligate_aerobe_oxygen_respiration: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **obligately aerobic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/obligately_aerobic.yaml`.

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


## Research report: Microbial trait **obligately aerobic** (METPO:1000606)

### 0. Scope summary (curation-oriented)
The trait **obligately aerobic** denotes microbes that **do not grow in the absence of molecular oxygen (O₂)**; operationally, they are “defined by their lack of growth in the absence of oxygen” (ciemniecki2020thepotentialfor pages 1-2). Importantly, “obligate” should not be curated as “dies immediately without O₂”: literature emphasizes that **some obligate aerobes can remain metabolically active and survive anoxia without growth** (ciemniecki2020thepotentialfor pages 1-2). Mechanistically, the key constraint is that removal of O₂ interrupts electron transport chain (ETC) flux, challenging maintenance of **redox balance and proton motive force (PMF)** (ciemniecki2020thepotentialfor pages 1-2).

### 1. Key concepts and definitions (current understanding)

#### 1.1 Definition and assay interpretation
* **Trait meaning:** growth requirement for O₂ (O₂ preference category). “Obligate aerobe” is best curated as **“no growth without O₂”**, not “cannot survive anoxia” (ciemniecki2020thepotentialfor pages 1-2).
* **Mechanistic rationale:** in anoxia, obligate aerobes must sustain redox balance/PMF “despite interrupted flux through the electron transport chain (ETC) due to the absence of oxygen” (ciemniecki2020thepotentialfor pages 1-2).

#### 1.2 Boundary cases and distinctions (avoid miscuration)
* **Obligate aerobe vs facultative anaerobe:** facultative anaerobes can grow with or without O₂, via aerobic respiration and anaerobic strategies (alternative electron acceptors or fermentation) (ciemniecki2020thepotentialfor pages 1-2, andre2021theselectiveadvantage pages 2-4).
* **Obligate aerobe vs aerotolerant organisms:** an aerotolerant strict anaerobe can tolerate O₂ exposure but lacks aerobic respiration; André et al. describe a Shigella flexneri mutation abolishing O₂ consumption and converting a facultative anaerobe into an “aerotolerant strict anaerobe” (andre2021theselectiveadvantage pages 2-4).
* **Microaerophily / oxygen gradients:** oxygen-use phenotypes occur along gradients; oxygen tolerance is described as a **spectrum** spanning obligate anaerobiosis to obligate aerobiosis (khademian2021howmicrobesevolved pages 6-8), and many taxa exhibit growth/survival at low percent O₂ (lu2021whenanaerobesencounter pages 3-4).

### 2. Candidate causal-graph entities (nodes), grouped by type

#### 2.1 Environmental / experimental factors
* **Molecular oxygen availability** (CHEBI:15379), including hypoxia/microoxia/anoxia contexts (ciemniecki2020thepotentialfor pages 1-2, lu2021whenanaerobesencounter pages 3-4).
* **Gaseous inhibitors/stressors relevant to aerobic respiration:** nitric oxide (NO) and hydrogen sulfide (H₂S), which target terminal oxidases and can shape “effective” aerobiosis in vivo (nastasi2024cyanideinsensitiveoxidase pages 1-2, nastasi2024cyanideinsensitiveoxidase pages 16-17).

#### 2.2 Pathways / processes
* **Aerobic respiration / oxidative phosphorylation**, including ETC function and PMF maintenance (ciemniecki2020thepotentialfor pages 1-2, andre2021theselectiveadvantage pages 2-4).
* **Reactive oxygen species (ROS) detoxification and repair** (SOD/catalase/peroxidases; Fe–S repair; iron homeostasis; Mn substitution) (khademian2021howmicrobesevolved pages 6-8, khademian2021howmicrobesevolved pages 15-20).
* **O₂-dependent cofactor biosynthesis** (candidate oxygen-essential steps): NAD⁺, PLP, heme (mrnjavac2024theradicalimpact pages 33-36).

#### 2.3 Protein complexes / enzymes (examples of curatable mechanistic nodes)
* **Terminal oxidases (O₂ reductases):** heme–copper oxidases (aa3, cbb3, bo3) and cytochrome bd-type oxidases (including CIO) (nastasi2024cyanideinsensitiveoxidase pages 2-3, hu2024identificationofcomplex media 87b3d825).
* **Electron entry complexes/dehydrogenases:** complex I, NDH-2, NQR; plus SDH and other primary dehydrogenases (hu2024identificationofcomplex pages 1-3, hu2024identificationofcomplex media 87b3d825).
* **Complex III (bc1) and quinone pool** as ETC intermediates (jones2023mechanismsofbioleaching pages 2-5, hu2024identificationofcomplex pages 1-3).

#### 2.4 Genes / transporters / assembly factors (taxon-specific candidates)
* **E. coli MFS transporters** *yhjE, ydiM, yfcJ* required for active **bo3 quinol oxidase** production (khalfaouihassani2023theescherichiacoli pages 21-22, khalfaouihassani2023theescherichiacoli pages 1-2).

#### 2.5 Chemicals / cofactors
* **O₂** terminal electron acceptor (CHEBI:15379) (andre2021theselectiveadvantage pages 2-4).
* **Heme** and **Cu** cofactors for heme–Cu terminal oxidases (khalfaouihassani2023theescherichiacoli pages 1-2).
* **Superoxide and H₂O₂** as ROS (khademian2021howmicrobesevolved pages 6-8, khademian2021howmicrobesevolved pages 15-20).

### 3. Recent developments & latest research (prioritize 2023–2024)

#### 3.1 Branched aerobic respiratory chains and oxidase diversity (2024)
Hu et al. (Frontiers in Microbiology, **Feb 2024**) present a schematic of the *Pseudomonas aeruginosa* aerobic respiratory chain with multiple NADH dehydrogenases (NQR/complex I/NDH-2), other dehydrogenases (e.g., SDH), and multiple terminal oxidases (CIO, CYO/bo3, Cbb3-1, Cbb3-2, Caa3) (hu2024identificationofcomplex media 87b3d825). This branching provides mechanistic substrate for causal nodes/edges linking **O₂ availability → terminal oxidase usage → PMF/ATP generation**.

#### 3.2 Quantitative respiration phenotype under clinically relevant conditions (2024)
Hu et al. report that stationary-phase *P. aeruginosa* cells in urine-like media show a **3–4× higher respiratory rate** compared with logarithmic phase, indicating a strong reliance on aerobic oxidative phosphorylation during stationary phase in that condition (hu2024identificationofcomplex pages 1-3, hu2024identificationofcomplex media db9b648d). This is a concrete data point usable as a “respiration activity” node connected to environmental/media state.

#### 3.3 Terminal oxidases and tolerance to host-associated inhibitors (2024)
Nastasi et al. (Antioxidants, **Mar 2024**) emphasize that *P. aeruginosa* encodes **five terminal oxidases** (aa3, cbb3-1, cbb3-2, bo3, and bd-type CIO) and that these oxidases reduce O₂ to H₂O (four-electron process) to generate PMF (nastasi2024cyanideinsensitiveoxidase pages 2-3). They provide kinetics and microoxic genetics relevant to causal parameterization: CIO’s measured O₂ affinity is reported as **Km = 4.0 ± 2.1 µM**, and a mutant lacking both cbb3 oxidases can grow at **2% O₂**, whereas a triple mutant lacking cbb3 and CIO cannot (nastasi2024cyanideinsensitiveoxidase pages 2-3). They also show CIO-mediated **H₂S tolerance** (“O₂ consumption by CIO is unaltered…” with high H₂S) and fast recovery from NO inhibition, motivating edges linking bd-type oxidases to **respiration robustness** in host-like stressors (nastasi2024cyanideinsensitiveoxidase pages 1-2).

#### 3.4 Aerobic iron/sulfur oxidation and obligate aerobiosis by redox constraint (2023)
Jones & Santini (Essays in Biochemistry, **Aug 2023**) argue that for **acidophilic Fe²⁺ oxidation**, oxygen is effectively the **only usable electron acceptor**, citing redox potentials at pH 2: Fe²⁺/Fe³⁺ = **+0.77 V** versus O₂ = **+1.12 V**, thereby making these iron oxidation mechanisms aerobic (jones2023mechanismsofbioleaching pages 2-5). They also describe electron flow to the quinone pool and then to terminal oxidases **bo3 and/or bd**, or indirectly to **aa3** (jones2023mechanismsofbioleaching pages 2-5). This supports curating some chemolithotrophic energy metabolisms as mechanistically obligate-aerobic.

#### 3.5 Biogenesis of terminal oxidases: transporters and metal homeostasis (2023)
Khalfaoui-Hassani et al. (PLOS ONE, **Oct 2023**) show that *E. coli* bo3 quinol oxidase is a **heme–Cu oxygen reductase** that catalyzes four-electron reduction of O₂ to water, and that **biogenesis requires acquisition/integration of heme and copper cofactors** (khalfaouihassani2023theescherichiacoli pages 1-2). In strains engineered such that bo3 is the sole terminal oxidase, deletion of MFS transporter genes **yhjE, ydiM, yfcJ** prevents production of active bo3 (khalfaouihassani2023theescherichiacoli pages 2-3, khalfaouihassani2023theescherichiacoli pages 21-22). Metal-uptake assays further link these genes to cofactor homeostasis (e.g., ΔydiM slower **64Cu** uptake; ΔyhjE accumulates reduced **55Fe**) (khalfaouihassani2023theescherichiacoli pages 1-2). This provides concrete, recent, gene-level causal candidates to connect “metal import/homeostasis → active terminal oxidase → aerobic growth”.

### 4. Current applications and real-world implementations

* **Clinical infection physiology:** Aerobic respiration and terminal oxidase choice can shape pathogen colonization and survival in host oxygen gradients; André et al. emphasize aerobic respiration as central to oxygen consumption and infection-site hypoxia (andre2021theselectiveadvantage pages 2-4). Recent work on *P. aeruginosa* in urine-like medium connects aerobic oxidative phosphorylation to stationary-phase survival and proposes respiratory complexes as antibiotic targets (hu2024identificationofcomplex pages 1-3).
* **Biometallurgy / bioleaching:** Acidophilic bioleaching relies on aerobic iron/sulfur oxidation where O₂ is a required electron acceptor by redox constraint; mechanistic models route electrons to bo3/bd/aa3 terminal oxidases (jones2023mechanismsofbioleaching pages 2-5).
* **Antimicrobial targeting of respiration:** Because terminal oxidases and associated complexes maintain PMF and energy production, they are prominent drug-target discussions; for example, Hu et al. explicitly propose complex III, NQR and SDH as potential antibiotic targets in *P. aeruginosa* (hu2024identificationofcomplex pages 1-3).

### 5. Expert opinions / authoritative synthesis

* **“Obligate” does not mean “cannot survive without oxygen”:** Ciemniecki & Newman explicitly challenge the colloquial interpretation, stressing anaerobic survival metabolisms in obligate aerobes despite lack of growth (ciemniecki2020thepotentialfor pages 1-2).
* **Obligate aerobiosis is supported by more than “terminal oxidases”:** Mrnjavac et al. (FEBS Letters, **May 2024**) argue that oxygen’s physiological impact often came first via inhibition of anaerobic radical/Fe–S enzymes and later via evolution of O₂-tolerant and O₂-dependent **essential biosyntheses**, which could be prerequisites for aerobic respiratory chains (mrnjavac2024theradicalimpact pages 10-12, mrnjavac2024theradicalimpact pages 33-36).
* **Oxygen tolerance requires layered defenses:** Khademian & Imlay emphasize layered ROS defenses, iron homeostasis, repair systems, and manganese substitution as key enabling adaptations across the spectrum to obligate aerobiosis (khademian2021howmicrobesevolved pages 6-8, khademian2021howmicrobesevolved pages 15-20).

### 6. Relevant statistics and quantitative data (from recent studies where possible)
* **Respiration activation:** Stationary-phase *P. aeruginosa* in urine-like medium shows **3–4×** higher respiration rate than log phase (hu2024identificationofcomplex pages 1-3, hu2024identificationofcomplex media db9b648d).
* **Terminal oxidase kinetic parameter:** bd-type CIO O₂ affinity reported as **Km = 4.0 ± 2.1 µM** (nastasi2024cyanideinsensitiveoxidase pages 2-3).
* **Microoxic growth condition:** cco1/cco2 double mutant growth observed at **2% O₂**; triple mutant (cco1/cco2/cio) cannot (nastasi2024cyanideinsensitiveoxidase pages 2-3).
* **Redox potentials constraining aerobiosis:** at pH 2, Fe²⁺/Fe³⁺ **+0.77 V** vs O₂ **+1.12 V** (jones2023mechanismsofbioleaching pages 2-5).
* **ROS damage/repair kinetics (authoritative quantitative background):** Fe–S cluster oxidation rate constants ~**10⁶ M⁻¹ s⁻¹** (superoxide) and ~**10⁴ M⁻¹ s⁻¹** (H₂O₂); Fe–S repair half-time ~**5 min** (khademian2021howmicrobesevolved pages 15-20).

### 7. Candidate causal edges (evidence-backed table)
The following artifact is structured for direct translation into TraitMech YAML (with uncertainty flags for taxon-specific or inferred edges):

| Edge (subject–predicate–object) | Node types | Suggested ontology grounding | Evidence (first author year) | Publication date | DOI/URL | Supporting snippet (short quote) | Notes/uncertainty |
|---|---|---|---|---|---|---|---|
| molecular oxygen (O2) → enables → aerobic respiration | chemical → process | CHEBI:15379; GO:0009060 | André 2021 | 2021-04 | https://doi.org/10.1111/cmi.13338 | "Aerobic respiration is identified as the main cause of bacterial oxygen consumption" (andre2021theselectiveadvantage pages 2-4) | Broad, well-supported background edge for aerobes; not exclusive to obligate aerobes. |
| obligately aerobic phenotype → requires growth in presence of → molecular oxygen (O2) | phenotype → chemical/environment | METPO:1000606; CHEBI:15379 | Ciemniecki 2020 | 2020-02 | https://doi.org/10.1128/JB.00797-19 | "obligate aerobes" are "defined by their lack of growth in the absence of oxygen" (ciemniecki2020thepotentialfor pages 1-2) | Best operational scope edge for the trait. |
| absence of O2 (anoxia) → interrupts flux through → electron transport chain | environment → process | ENVO:01001002; GO:0022900 | Ciemniecki 2020 | 2020-02 | https://doi.org/10.1128/JB.00797-19 | "interrupted flux through the electron transport chain (ETC) due to the absence of oxygen" (ciemniecki2020thepotentialfor pages 1-2) | Mechanistic boundary case for obligate aerobes under anoxia. |
| interrupted electron transport chain flux → decreases/impairs → proton motive force maintenance | process → process | GO:0022900; GO:0009090 | Ciemniecki 2020 | 2020-02 | https://doi.org/10.1128/JB.00797-19 | obligate aerobes "must maintain redox balance and the proton motive force (PMF) despite interrupted flux through the electron transport chain" (ciemniecki2020thepotentialfor pages 1-2) | Supports why no-growth occurs without O2; PMF term grounded approximately. |
| terminal oxidase activity → reduces → O2 to H2O | enzyme complex/process → chemical | GO:0016676; CHEBI:15379; CHEBI:15377 | Nastasi 2024 | 2024-03 | https://doi.org/10.3390/antiox13030383 | "All reduce O2 to H2O via a four-electron process to generate the proton motive force" (nastasi2024cyanideinsensitiveoxidase pages 2-3) | General edge for aerobic terminal oxidases. |
| bo3 quinol oxidase → functions_as → terminal oxygen reductase in aerobic respiration | protein complex → process | EC:7.1.1.-; GO:0016676 | Khalfaoui-Hassani 2023 | 2023-10 | https://doi.org/10.1371/journal.pone.0293015 | "bo3-Qox is a heme-Cu oxygen reductase that functions as a terminal oxygen reductase in aerobic respiration" (khalfaouihassani2023theescherichiacoli pages 1-2) | Direct mechanistic edge; species-specific evidence from E. coli. |
| copper cofactor availability → required_for → active bo3 quinol oxidase biogenesis | chemical → protein complex | CHEBI:28694; EC:7.1.1.- | Khalfaoui-Hassani 2023 | 2023-10 | https://doi.org/10.1371/journal.pone.0293015 | "Biogenesis of heme-Cu oxidases requires acquisition and integration of heme and copper cofactors" (khalfaouihassani2023theescherichiacoli pages 1-2) | Strong for heme-Cu oxidases generally; bo3-specific assembly details partly inferred. |
| heme cofactor availability → required_for → active bo3 quinol oxidase biogenesis | chemical → protein complex | CHEBI:30413; EC:7.1.1.- | Khalfaoui-Hassani 2023 | 2023-10 | https://doi.org/10.1371/journal.pone.0293015 | "Biogenesis of heme-Cu oxidases requires acquisition and integration of heme and copper cofactors" (khalfaouihassani2023theescherichiacoli pages 1-2) | Same source supports both Cu and heme requirements. |
| YdiM/YhjE/YfcJ MFS transporters → required_for → active bo3 quinol oxidase production | transporter genes/proteins → protein complex |  | Khalfaoui-Hassani 2023 | 2023-10 | https://doi.org/10.1371/journal.pone.0293015 | "three Escherichia coli MFS-type transporter genes — yhjE, ydiM, and yfcJ — are required to produce an active bo3 quinol oxidase" (khalfaouihassani2023theescherichiacoli pages 21-22) | Strong but taxon-specific to E. coli; curate as conditional/mechanism example, not universal obligate-aerobe edge. |
| YdiM deletion → slows → Cu uptake | gene/protein → process | CHEBI:28694 | Khalfaoui-Hassani 2023 | 2023-10 | https://doi.org/10.1371/journal.pone.0293015 | "ΔydiM displays slower 64Cu uptake" (khalfaouihassani2023theescherichiacoli pages 1-2) | Taxon-specific and indirect; supports Cu-homeostasis-to-bo3 assembly pathway. |
| cytochrome bd/CIO oxidase → confers tolerance to → H2S during aerobic respiration | protein complex → chemical/stress | GO:0016676; CHEBI:16136 | Nastasi 2024 | 2024-03 | https://doi.org/10.3390/antiox13030383 | "O2 consumption by CIO is unaltered even in the presence of high levels of H2S" (nastasi2024cyanideinsensitiveoxidase pages 1-2) | Strong for P. aeruginosa CIO; not universal for all bd oxidases. |
| cytochrome bd/CIO oxidase → confers tolerance to → NO during aerobic respiration | protein complex → chemical/stress | GO:0016676; CHEBI:16480 | Nastasi 2024 | 2024-03 | https://doi.org/10.3390/antiox13030383 | "activity recovery after NO exhaustion is full and fast" (nastasi2024cyanideinsensitiveoxidase pages 1-2) | Strong but species-specific; useful resilience edge in oxic niches. |
| L-aspartate oxidase → enables → NAD+ biosynthesis in oxic conditions | enzyme → biosynthetic process | EC:1.4.3.16; KEGG:K00278 | Mrnjavac 2024 | 2024-05 | https://doi.org/10.1002/1873-3468.14906 | "L-aspartate oxidase (NAD+ synthesis; K00278; EC 1.4.3.16)" (mrnjavac2024theradicalimpact pages 33-36) | Plausible obligate-aerobiosis contributor where O2-dependent route replaces O2-independent alternatives; uncertain as universal trait edge. |
| pyridoxamine 5′-phosphate oxidase → enables → pyridoxal phosphate (PLP) biosynthesis in oxic conditions | enzyme → biosynthetic process | EC:1.4.3.5; KEGG:K00275; CHEBI:18405 | Mrnjavac 2024 | 2024-05 | https://doi.org/10.1002/1873-3468.14906 | "Pyridoxamine 5′-phosphate oxidase (PLP synthesis; K00275; EC 1.4.3.5)" (mrnjavac2024theradicalimpact pages 33-36) | Candidate oxygen-requirement edge; pathway dependence varies by taxon. |
| protoporphyrinogen oxidase → enables → heme biosynthesis in oxic conditions | enzyme → biosynthetic process | EC:1.3.3.4; KEGG:K00231; CHEBI:30413 | Mrnjavac 2024 | 2024-05 | https://doi.org/10.1002/1873-3468.14906 | "Protoporphyrinogen oxidase (heme synthesis; K00231; EC 1.3.3.4)" (mrnjavac2024theradicalimpact pages 33-36) | Candidate edge linking O2-dependent cofactor synthesis to oxic growth; taxon dependence uncertain. |
| superoxide dismutase activity → mitigates → superoxide stress | molecular function/enzyme → chemical stress | GO:0004784; CHEBI:18421 | Khademian 2021 | 2021-05 | https://doi.org/10.1016/j.tim.2020.10.001 | aerobes deploy "scavenging enzymes (SOD, catalase, other peroxidases)" (khademian2021howmicrobesevolved pages 6-8) | Broad defense edge; essentiality varies by lineage and niche. |
| catalase/catalase-peroxidase activity → mitigates → hydrogen peroxide stress | enzyme → chemical stress | EC:1.11.1.6; EC:1.11.1.21; CHEBI:16240 | Khademian 2021 / Mrnjavac 2024 | 2021-05 / 2024-05 | https://doi.org/10.1016/j.tim.2020.10.001 ; https://doi.org/10.1002/1873-3468.14906 | "scavenging enzymes (SOD, catalase, other peroxidases)"; "Catalase... Catalase-peroxidase" (khademian2021howmicrobesevolved pages 6-8, mrnjavac2024theradicalimpact pages 33-36) | Good generic ROS-defense edge for oxic growth competence. |
| superoxide or H2O2 exposure → oxidizes/inactivates → exposed Fe-S cluster enzymes | chemical → enzymes/process | CHEBI:18421; CHEBI:16240; GO:0051536 | Khademian 2021 | 2021-05 | https://doi.org/10.1016/j.tim.2020.10.001 | "rate constants for cluster oxidation are given (~106 M−1 s−1 for superoxide and ~104 M−1 s−1 for H2O2)" (khademian2021howmicrobesevolved pages 15-20) | Important mechanistic damage edge explaining need for ROS defense in aerobes. |
| manganese import/substitution for iron → reduces → ROS vulnerability of mononuclear enzymes | chemical/process → process | CHEBI:29035; CHEBI:18248 | Khademian 2021 | 2021-05 | https://doi.org/10.1016/j.tim.2020.10.001 | "replacement of Fe with Mn in enzymes and recruitment into SOD/catalase → reduced metal-centered ROS vulnerability" (khademian2021howmicrobesevolved pages 6-8) | Mechanistically strong but broad; specific transporter nodes not identified in current evidence set. |
| obligate aerobe under anoxia → can survive without growth via → anaerobic survival metabolism | phenotype/environment → process | METPO:1000606 | Ciemniecki 2020 | 2020-02 | https://doi.org/10.1128/JB.00797-19 | "lack of growth does not imply immediate death: 'anaerobic survival mechanisms in obligate aerobes are known'" (ciemniecki2020thepotentialfor pages 1-2) | Boundary-case edge; should not be miscurated as facultative anaerobiosis. |
| oxygen-dependent terminal oxidases / O2-dependent biosynthetic pathways → support colonization of → oxic niches | enzymes/processes → environment | GO:0016676; CHEBI:15379 | Mrnjavac 2024 | 2024-05 | https://doi.org/10.1002/1873-3468.14906 | acquisition of O2-tolerant cofactor biosynthesis "enables growth in oxic niches and precedes acquisition/origin of O2 respiratory terminal oxidases" (mrnjavac2024theradicalimpact pages 33-36) | Higher-level synthesis edge; useful summary but more evolutionary than assay-direct. |


*Table: This table compiles curation-ready candidate causal edges for the trait 'obligately aerobic' (METPO:1000606), spanning oxygen-dependent respiration, terminal oxidase biogenesis/function, ROS defense, and oxygen-dependent essential biosynthesis. It is useful as a starting scaffold for TraitMech YAML curation, while highlighting species-specific and uncertain edges.*

### 8. Visual evidence (for curation)
*Figure support for node selection and quantitative phenotypes:* Hu et al. provide a schematic of the *P. aeruginosa* aerobic respiratory chain (including terminal oxidases CIO/CYO/Cbb3/Caa3 and electron entry dehydrogenases), and a bar-plot panel showing higher oxygen consumption rate in stationary phase in urine-like media (hu2024identificationofcomplex media 87b3d825, hu2024identificationofcomplex media db9b648d).

### 9. Warnings / claims not ready for curation
1. **Do not encode “obligate aerobe = dies without oxygen.”** Sources explicitly separate “no growth” from “no survival,” and document anaerobic survival mechanisms (ciemniecki2020thepotentialfor pages 1-2).
2. **Do not generalize taxon-specific assembly genes to all obligate aerobes.** The *E. coli* requirement for *yhjE/ydiM/yfcJ* for active bo3 oxidase is strong but likely not universal; curate as conditional and taxon-specific (khalfaouihassani2023theescherichiacoli pages 21-22, khalfaouihassani2023theescherichiacoli pages 1-2).
3. **O₂-dependent cofactor biosynthesis as a *universal* driver of obligate aerobiosis is not established here.** Mrnjavac et al. list O₂-dependent enzymes in NAD⁺/PLP/heme synthesis (mrnjavac2024theradicalimpact pages 33-36), but whether these steps are strictly required vs bypassed by alternative pathways varies across lineages; curate these edges as **candidate mechanisms**.

---

## DOI-first bibliography (with dates and URLs)

1. Nastasi MR, et al. **Cyanide Insensitive Oxidase Confers Hydrogen Sulfide and Nitric Oxide Tolerance to *Pseudomonas aeruginosa* Aerobic Respiration.** *Antioxidants*. **2024-03**. DOI: **10.3390/antiox13030383**. https://doi.org/10.3390/antiox13030383 (nastasi2024cyanideinsensitiveoxidase pages 2-3, nastasi2024cyanideinsensitiveoxidase pages 1-2, nastasi2024cyanideinsensitiveoxidase pages 16-17)
2. Hu Y, et al. **Identification of complex III, NQR, and SDH as primary bioenergetic enzymes during the stationary phase of *Pseudomonas aeruginosa* cultured in urine-like conditions.** *Frontiers in Microbiology*. **2024-02**. DOI: **10.3389/fmicb.2024.1347466**. https://doi.org/10.3389/fmicb.2024.1347466 (hu2024identificationofcomplex pages 1-3, hu2024identificationofcomplex media 87b3d825, hu2024identificationofcomplex media db9b648d)
3. Mrnjavac N, et al. **The radical impact of oxygen on prokaryotic evolution—enzyme inhibition first, uninhibited essential biosyntheses second, aerobic respiration third.** *FEBS Letters*. **2024-05**. DOI: **10.1002/1873-3468.14906**. https://doi.org/10.1002/1873-3468.14906 (mrnjavac2024theradicalimpact pages 10-12, mrnjavac2024theradicalimpact pages 33-36, mrnjavac2024theradicalimpact pages 7-9)
4. Khalfaoui-Hassani B, et al. **The *Escherichia coli* MFS-type transporter genes *yhjE*, *ydiM*, and *yfcJ* are required to produce an active bo3 quinol oxidase.** *PLOS ONE*. **2023-10**. DOI: **10.1371/journal.pone.0293015**. https://doi.org/10.1371/journal.pone.0293015 (khalfaouihassani2023theescherichiacoli pages 1-2, khalfaouihassani2023theescherichiacoli pages 21-22, khalfaouihassani2023theescherichiacoli pages 2-3)
5. Jones S, Santini JM. **Mechanisms of bioleaching: iron and sulfur oxidation by acidophilic microorganisms.** *Essays in Biochemistry*. **2023-08**. DOI: **10.1042/ebc20220257**. https://doi.org/10.1042/ebc20220257 (jones2023mechanismsofbioleaching pages 2-5)
6. Lu Z, Imlay JA. **When anaerobes encounter oxygen: mechanisms of oxygen toxicity, tolerance and defence.** *Nature Reviews Microbiology*. **2021-06**. DOI: **10.1038/s41579-021-00583-y**. https://doi.org/10.1038/s41579-021-00583-y (lu2021whenanaerobesencounter pages 16-17, lu2021whenanaerobesencounter pages 3-4)
7. Khademian M, Imlay JA. **How Microbes Evolved to Tolerate Oxygen.** *Trends in Microbiology*. **2021-05**. DOI: **10.1016/j.tim.2020.10.001**. https://doi.org/10.1016/j.tim.2020.10.001 (khademian2021howmicrobesevolved pages 6-8, khademian2021howmicrobesevolved pages 15-20)
8. André AC, et al. **The selective advantage of facultative anaerobes relies on their unique ability to cope with changing oxygen levels during infection.** *Cellular Microbiology*. **2021-04**. DOI: **10.1111/cmi.13338**. https://doi.org/10.1111/cmi.13338 (andre2021theselectiveadvantage pages 2-4)
9. Ciemniecki JA, Newman DK. **The Potential for Redox-Active Metabolites To Enhance or Unlock Anaerobic Survival Metabolisms in Aerobes.** *Journal of Bacteriology*. **2020-02**. DOI: **10.1128/JB.00797-19**. https://doi.org/10.1128/JB.00797-19 (ciemniecki2020thepotentialfor pages 1-2)


References

1. (ciemniecki2020thepotentialfor pages 1-2): John A. Ciemniecki and Dianne K. Newman. The potential for redox-active metabolites to enhance or unlock anaerobic survival metabolisms in aerobes. Journal of Bacteriology, Feb 2020. URL: https://doi.org/10.1128/jb.00797-19, doi:10.1128/jb.00797-19. This article has 47 citations and is from a peer-reviewed journal.

2. (andre2021theselectiveadvantage pages 2-4): Antonin C. André, Lorine Debande, and Benoit S. Marteyn. The selective advantage of facultative anaerobes relies on their unique ability to cope with changing oxygen levels during infection. Cellular Microbiology, Apr 2021. URL: https://doi.org/10.1111/cmi.13338, doi:10.1111/cmi.13338. This article has 102 citations and is from a peer-reviewed journal.

3. (khademian2021howmicrobesevolved pages 6-8): Maryam Khademian and James A. Imlay. How microbes evolved to tolerate oxygen. May 2021. URL: https://doi.org/10.1016/j.tim.2020.10.001, doi:10.1016/j.tim.2020.10.001. This article has 125 citations and is from a domain leading peer-reviewed journal.

4. (lu2021whenanaerobesencounter pages 3-4): Zheng Lu and James A. Imlay. When anaerobes encounter oxygen: mechanisms of oxygen toxicity, tolerance and defence. Nature Reviews Microbiology, 19:774-785, Jun 2021. URL: https://doi.org/10.1038/s41579-021-00583-y, doi:10.1038/s41579-021-00583-y. This article has 341 citations and is from a highest quality peer-reviewed journal.

5. (nastasi2024cyanideinsensitiveoxidase pages 1-2): Martina R. Nastasi, Lorenzo Caruso, Francesca Giordano, Marta Mellini, Giordano Rampioni, Alessandro Giuffrè, and Elena Forte. Cyanide insensitive oxidase confers hydrogen sulfide and nitric oxide tolerance to pseudomonas aeruginosa aerobic respiration. Antioxidants, 13:383, Mar 2024. URL: https://doi.org/10.3390/antiox13030383, doi:10.3390/antiox13030383. This article has 8 citations.

6. (nastasi2024cyanideinsensitiveoxidase pages 16-17): Martina R. Nastasi, Lorenzo Caruso, Francesca Giordano, Marta Mellini, Giordano Rampioni, Alessandro Giuffrè, and Elena Forte. Cyanide insensitive oxidase confers hydrogen sulfide and nitric oxide tolerance to pseudomonas aeruginosa aerobic respiration. Antioxidants, 13:383, Mar 2024. URL: https://doi.org/10.3390/antiox13030383, doi:10.3390/antiox13030383. This article has 8 citations.

7. (khademian2021howmicrobesevolved pages 15-20): Maryam Khademian and James A. Imlay. How microbes evolved to tolerate oxygen. May 2021. URL: https://doi.org/10.1016/j.tim.2020.10.001, doi:10.1016/j.tim.2020.10.001. This article has 125 citations and is from a domain leading peer-reviewed journal.

8. (mrnjavac2024theradicalimpact pages 33-36): Natalia Mrnjavac, Falk S. P. Nagies, Jessica L. E. Wimmer, Nils Kapust, Michael R Knopp, Katharina Trost, L. Modjewski, Nicolas C. Bremer, Marek Mentel, Mauro Degli Esposti, Itzhak Mizrahi, John F Allen, and William F. Martin. The radical impact of oxygen on prokaryotic evolution—enzyme inhibition first, uninhibited essential biosyntheses second, aerobic respiration third. FEBS letters, 598:1692-1714, May 2024. URL: https://doi.org/10.1002/1873-3468.14906, doi:10.1002/1873-3468.14906. This article has 15 citations and is from a peer-reviewed journal.

9. (nastasi2024cyanideinsensitiveoxidase pages 2-3): Martina R. Nastasi, Lorenzo Caruso, Francesca Giordano, Marta Mellini, Giordano Rampioni, Alessandro Giuffrè, and Elena Forte. Cyanide insensitive oxidase confers hydrogen sulfide and nitric oxide tolerance to pseudomonas aeruginosa aerobic respiration. Antioxidants, 13:383, Mar 2024. URL: https://doi.org/10.3390/antiox13030383, doi:10.3390/antiox13030383. This article has 8 citations.

10. (hu2024identificationofcomplex media 87b3d825): Yuyao Hu, Ming Yuan, Alexander Julian, Karina Tuz, and Oscar Juárez. Identification of complex iii, nqr, and sdh as primary bioenergetic enzymes during the stationary phase of pseudomonas aeruginosa cultured in urine-like conditions. Frontiers in Microbiology, Feb 2024. URL: https://doi.org/10.3389/fmicb.2024.1347466, doi:10.3389/fmicb.2024.1347466. This article has 12 citations and is from a peer-reviewed journal.

11. (hu2024identificationofcomplex pages 1-3): Yuyao Hu, Ming Yuan, Alexander Julian, Karina Tuz, and Oscar Juárez. Identification of complex iii, nqr, and sdh as primary bioenergetic enzymes during the stationary phase of pseudomonas aeruginosa cultured in urine-like conditions. Frontiers in Microbiology, Feb 2024. URL: https://doi.org/10.3389/fmicb.2024.1347466, doi:10.3389/fmicb.2024.1347466. This article has 12 citations and is from a peer-reviewed journal.

12. (jones2023mechanismsofbioleaching pages 2-5): Sarah Jones and Joanne M. Santini. Mechanisms of bioleaching: iron and sulfur oxidation by acidophilic microorganisms. Essays in Biochemistry, 67:685-699, Aug 2023. URL: https://doi.org/10.1042/ebc20220257, doi:10.1042/ebc20220257. This article has 84 citations and is from a peer-reviewed journal.

13. (khalfaouihassani2023theescherichiacoli pages 21-22): Bahia Khalfaoui-Hassani, Crysten E. Blaby-Haas, Andreia Verissimo, and Fevzi Daldal. The escherichia coli mfs-type transporter genes yhje, ydim, and yfcj are required to produce an active bo3 quinol oxidase. PLOS ONE, 18:e0293015, Oct 2023. URL: https://doi.org/10.1371/journal.pone.0293015, doi:10.1371/journal.pone.0293015. This article has 8 citations and is from a peer-reviewed journal.

14. (khalfaouihassani2023theescherichiacoli pages 1-2): Bahia Khalfaoui-Hassani, Crysten E. Blaby-Haas, Andreia Verissimo, and Fevzi Daldal. The escherichia coli mfs-type transporter genes yhje, ydim, and yfcj are required to produce an active bo3 quinol oxidase. PLOS ONE, 18:e0293015, Oct 2023. URL: https://doi.org/10.1371/journal.pone.0293015, doi:10.1371/journal.pone.0293015. This article has 8 citations and is from a peer-reviewed journal.

15. (hu2024identificationofcomplex media db9b648d): Yuyao Hu, Ming Yuan, Alexander Julian, Karina Tuz, and Oscar Juárez. Identification of complex iii, nqr, and sdh as primary bioenergetic enzymes during the stationary phase of pseudomonas aeruginosa cultured in urine-like conditions. Frontiers in Microbiology, Feb 2024. URL: https://doi.org/10.3389/fmicb.2024.1347466, doi:10.3389/fmicb.2024.1347466. This article has 12 citations and is from a peer-reviewed journal.

16. (khalfaouihassani2023theescherichiacoli pages 2-3): Bahia Khalfaoui-Hassani, Crysten E. Blaby-Haas, Andreia Verissimo, and Fevzi Daldal. The escherichia coli mfs-type transporter genes yhje, ydim, and yfcj are required to produce an active bo3 quinol oxidase. PLOS ONE, 18:e0293015, Oct 2023. URL: https://doi.org/10.1371/journal.pone.0293015, doi:10.1371/journal.pone.0293015. This article has 8 citations and is from a peer-reviewed journal.

17. (mrnjavac2024theradicalimpact pages 10-12): Natalia Mrnjavac, Falk S. P. Nagies, Jessica L. E. Wimmer, Nils Kapust, Michael R Knopp, Katharina Trost, L. Modjewski, Nicolas C. Bremer, Marek Mentel, Mauro Degli Esposti, Itzhak Mizrahi, John F Allen, and William F. Martin. The radical impact of oxygen on prokaryotic evolution—enzyme inhibition first, uninhibited essential biosyntheses second, aerobic respiration third. FEBS letters, 598:1692-1714, May 2024. URL: https://doi.org/10.1002/1873-3468.14906, doi:10.1002/1873-3468.14906. This article has 15 citations and is from a peer-reviewed journal.

18. (mrnjavac2024theradicalimpact pages 7-9): Natalia Mrnjavac, Falk S. P. Nagies, Jessica L. E. Wimmer, Nils Kapust, Michael R Knopp, Katharina Trost, L. Modjewski, Nicolas C. Bremer, Marek Mentel, Mauro Degli Esposti, Itzhak Mizrahi, John F Allen, and William F. Martin. The radical impact of oxygen on prokaryotic evolution—enzyme inhibition first, uninhibited essential biosyntheses second, aerobic respiration third. FEBS letters, 598:1692-1714, May 2024. URL: https://doi.org/10.1002/1873-3468.14906, doi:10.1002/1873-3468.14906. This article has 15 citations and is from a peer-reviewed journal.

19. (lu2021whenanaerobesencounter pages 16-17): Zheng Lu and James A. Imlay. When anaerobes encounter oxygen: mechanisms of oxygen toxicity, tolerance and defence. Nature Reviews Microbiology, 19:774-785, Jun 2021. URL: https://doi.org/10.1038/s41579-021-00583-y, doi:10.1038/s41579-021-00583-y. This article has 341 citations and is from a highest quality peer-reviewed journal.