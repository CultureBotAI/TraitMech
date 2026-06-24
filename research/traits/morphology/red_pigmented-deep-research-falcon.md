---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T09:19:29.100096'
end_time: '2026-06-18T09:47:15.833451'
duration_seconds: 1666.73
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: red pigmented
  trait_identifier: METPO:1003028
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: red_pigmented
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A pigmentation phenotype in which microbial colonies or cells appear
    red due to production of red pigments such as prodiginines or carotenoids.
  parent_traits: METPO:1003021
  synonyms: Pigment_red
  evidence_summary: 'DOI:10.1038/nrmicro1531: red-pigmented prodiginines (Supports
    red microbial pigmentation as a prodiginine-associated color phenotype in representative
    bacteria.)'
  causal_graph_summary: 'red_pigmented_prodiginine_pathway: 5 nodes, 4 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 40
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** red pigmented
- **METPO identifier:** METPO:1003028
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which microbial colonies or cells appear red due to production of red pigments such as prodiginines or carotenoids.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_red
- **Existing evidence:** DOI:10.1038/nrmicro1531: red-pigmented prodiginines (Supports red microbial pigmentation as a prodiginine-associated color phenotype in representative bacteria.)
- **Existing causal graph summary:** red_pigmented_prodiginine_pathway: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **red pigmented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/red_pigmented.yaml`.

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
- **Trait label:** red pigmented
- **METPO identifier:** METPO:1003028
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which microbial colonies or cells appear red due to production of red pigments such as prodiginines or carotenoids.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_red
- **Existing evidence:** DOI:10.1038/nrmicro1531: red-pigmented prodiginines (Supports red microbial pigmentation as a prodiginine-associated color phenotype in representative bacteria.)
- **Existing causal graph summary:** red_pigmented_prodiginine_pathway: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **red pigmented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/red_pigmented.yaml`.

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


## Microbial Trait Causal Graph Research Report: **red pigmented** (METPO:1003028)

### Scope summary (TraitMech curation view)
**Trait definition (operational):** A microbial colony/cell phenotype where biomass appears **red** due to accumulation or secretion of **endogenous pigments** (e.g., prodiginines/prodigiosin, carotenoids such as lycopene/torularhodin/torulene) under the assay conditions used. (barreto2023microbialpigmentsmajor pages 10-12, barreto2023microbialpigmentsmajor pages 4-6)

**What to include as “red pigmented”:**
- **Prodiginine/prodigiosin-type red tripyrroles** (common in *Serratia* and some actinomycetes/marine bacteria), where the pigment itself is described as red and the pathway is genetically encoded. (barreto2023microbialpigmentsmajor pages 10-12, lu2024prodigiosinunveilingthe pages 8-9)
- **Carotenoid-driven red coloration**, including **lycopene** (explicitly described as red) and red-yeast carotenoids (torularhodin/torulene/β-carotene mixtures that yield red/orange-red colonies). (barreto2023microbialpigmentsmajor pages 4-6, ochoavinals2024currentadvancesin pages 2-5)

**Boundary cases / cautions:**
- **Non-red pigments** that can look reddish depending on pH/oxidation state (some phenazines, porphyrins) should be curated only when the study explicitly ties a chemical species to a red phenotype.
- **Interaction-dependent red halos** (e.g., red pigments formed only in co-culture by chemical modification of a partner’s metabolite) are real but should be curated as **conditional**/contextual edges rather than defining the intrinsic trait of the organism. (iloabuchi2024bacillussp.g2112 pages 1-2, iloabuchi2024bacillussp.g2112 pages 2-4)

---

## 1) Key concepts and current mechanistic understanding

### A. Prodiginines / prodigiosin (canonical bacterial red pigmentation)
- **Prodiginines are described as “hydrophobic, red tripyrrole” pigments**, produced by *Serratia* spp., actinomycetes, and some marine bacteria; they are encoded by biosynthetic gene clusters (Pig/Red) and arise via a bifurcated pathway ending in condensation of intermediates (MAP + MBC). (barreto2023microbialpigmentsmajor pages 10-12)
- The pathway’s key chemical logic: an enzymatic condensation between **MBC (4-methoxy-2,2′-bipyrrole-5-carbaldehyde)** and a **monopyrrole** unit yields the red tripyrrole scaffold. (barreto2023biotechnologicalapplicationsof pages 11-14, barreto2023microbialpigmentsmajor pages 10-12)
- The review evidence identifies **PigC** as the **key ligase/condensation enzyme** that links MAP and MBC to form prodigiosin. (lu2024prodigiosinunveilingthe pages 8-9)

### B. Carotenoids (red coloration via polyenes; common in bacteria/yeasts/algae)
- Carotenoid biosynthesis proceeds from phytoene to **lycopene**, which is explicitly described as **“a red-colored pigment.”** (barreto2023microbialpigmentsmajor pages 4-6)
- Mechanistic outline: phytoene synthase condenses two GGPP units to phytoene; desaturation/isomerization yields **lycopene**; cyclization and oxygenation yield other carotenes/xanthophylls. (barreto2023microbialpigmentsmajor pages 4-6)
- In red yeasts (*Rhodotorula* spp.), major pigments include **torularhodin, torulene, and β-carotene**, which collectively confer red/orange-red coloration and antioxidant function. (ochoavinals2024currentadvancesin pages 2-5)

### C. Phenazines and “red phenazine derivatives” as conditional mechanisms
- Phenazines are often colored and can become red via chemical modification. A clear 2024 example shows **Pseudomonas-derived phenazine-1-carboxylic acid (PCA)** being converted by a *Bacillus* strain into **red, N5-glucosylated phenazine derivatives**, forming a visible red halo around colonies in co-culture. (iloabuchi2024bacillussp.g2112 pages 1-2, iloabuchi2024bacillussp.g2112 pages 2-4)

---

## 2) Recent developments (prioritizing 2023–2024)

### 2.1 Phage–host regulation of prodigiosin (2024)
A recent *Scientific Reports* study shows that **flagellotropic χ phage infection** is a strong inducer of red prodigiosin production in *Serratia marcescens* ATCC 274:
- χ addition caused **>5-fold** prodigiosin overproduction (qualitatively) and specifically **5.5-fold** increased pigment concentration when added in stationary phase (measured by A535 after extraction) after 18 h at 25 °C. (esteves2024serratiamarcescensatcc pages 1-2, esteves2024serratiamarcescensatcc pages 2-3)
- A χ-induced lysate increased **pig operon transcription ~3-fold** (reporter fusion) and pigment increases became significant within hours; replacing the native pig promoter abolished induction, implicating promoter-level regulation. (esteves2024serratiamarcescensatcc pages 1-2, esteves2024serratiamarcescensatcc pages 3-5)

**Curation value:** This provides recent, experiment-backed edges linking a **biotic stressor (phage infection/lysis products)** → **pig operon transcription** → **red prodigiosin phenotype** in a strain-conditional way. (esteves2024serratiamarcescensatcc pages 1-2, esteves2024serratiamarcescensatcc pages 3-5)

### 2.2 Bioprocess scale-up to high prodigiosin titers (2024)
A 2024 *Marine Drugs* study optimized and scaled prodigiosin production from a marine *Serratia rubidaea* strain:
- Shake-flask optimization increased prodigiosin **13-fold to 19.7 mg/L**. (pereira2024improvingbioprocessconditions pages 1-2)
- Scale-up to 2 L bioreactors using **kLa (oxygen mass transfer)** as criterion achieved **293.1 mg/L prodigiosin in 24 h** (bioreactor BE), with productivity **12.21 mg/(L·h)** reported. (pereira2024improvingbioprocessconditions pages 14-16, pereira2024improvingbioprocessconditions pages 16-17)
- Environmental/process factors causally connected to production include **oxygen availability/headspace**, **kLa**, agitation strategy, and vessel geometry. (pereira2024improvingbioprocessconditions pages 9-11, pereira2024improvingbioprocessconditions pages 14-16)

These results are supported by figures/tables extracted from the paper showing the kLa comparison and time-course titers (pereira2024improvingbioprocessconditions media 29e3a70c, pereira2024improvingbioprocessconditions media 9473e601, pereira2024improvingbioprocessconditions media 4b42c724, pereira2024improvingbioprocessconditions media 7545cc55).

### 2.3 Red-yeast carotenoid production strategies and stress induction (2024)
A 2024 *Fermentation* review synthesizes how *Rhodotorula* carotenoid production is increased by stress/process conditions:
- Light effects can increase carotenoid yields (examples include LED treatments with reported µg/L changes). (ochoavinals2024currentadvancesin pages 7-8)
- Aeration/agitation and acidic pH ranges are repeatedly associated with higher carotenoid accumulation. (ochoavinals2024currentadvancesin pages 7-8)
- Quantitative yields reported across studies include (examples): total carotenoids **7.3 mg/L** on olive mill waste, β-carotene **62 mg/L** from vegetable market waste (in *R. toruloides*), and other mg/L–µg/g examples depending on substrate and strain. (ochoavinals2024currentadvancesin pages 5-6)

### 2.4 Oxidative metabolism/ROS as a driver of carotenoid increases (2024)
A 2024 *Frontiers in Fungal Biology* study provides experimental evidence that oxidative metabolism increases carotenoids in *Rhodotorula mucilaginosa*:
- “Oxidative metabolism… induces oxidative stress, leading to increase synthesis of carotenoids.” (mosquedamartinez2024inrhodotorulamucilaginosa pages 8-9)
- The study also references typical minimal-medium composition dominated by torularhodin (60–80%) with β-carotene ~10–20%. (mosquedamartinez2024inrhodotorulamucilaginosa pages 8-9)

---

## 3) Current applications and real-world implementations

### A. Industrial and bioprocess production (red pigments as products)
- The 2024 *Marine Drugs* study demonstrates **scalable production** of red prodigiosin to **hundreds of mg/L** in 2 L bioreactors, with oxygen transfer (kLa) used explicitly as the scale-up rule—this is a direct bridge from trait (red pigmented) to industrial manufacturing. (pereira2024improvingbioprocessconditions pages 1-2, pereira2024improvingbioprocessconditions pages 14-16, pereira2024improvingbioprocessconditions media 9473e601)
- The *Rhodotorula* review highlights the use of low-cost substrates and process strategies (fed-batch, stressors) to increase carotenoid pigments (torularhodin/torulene/β-carotene) for food/cosmetics/pharma value chains. (ochoavinals2024currentadvancesin pages 1-2, ochoavinals2024currentadvancesin pages 5-6)

### B. Biosensing / synthetic biology (pigments as readouts)
- A 2024 review on colorimetric whole-cell biosensors describes microbial pigments as **human-eye-detectable outputs** and portable sensors (e.g., via lyophilization). While the cited example in the retrieved text emphasizes violacein (violet), the general application pattern (pigment output) applies to red pigments as well. (barreto2023biotechnologicalapplicationsof pages 7-9)

---

## 4) Expert interpretation (authoritative synthesis)

### What is “most curatable” as a TraitMech causal graph?
- **Core universal mechanism:** prodiginine/prodigiosin biosynthesis (Pig/Red clusters) and carotenoid biosynthesis (phytoene → lycopene; yeast torularhodin/torulene) are the most generalizable and should form the backbone of the causal graph for “red pigmented.” (barreto2023microbialpigmentsmajor pages 10-12, barreto2023microbialpigmentsmajor pages 4-6, ochoavinals2024currentadvancesin pages 2-5)
- **Regulatory layer:** Two-component systems and QS are repeatedly implicated in prodigiosin regulation (e.g., Cpx system repression; QS nodes), making them strong regulatory edges when strain evidence exists. (lu2024prodigiosinunveilingthe pages 9-10, lu2024prodigiosinunveilingthe pages 8-9)
- **Conditional/interaction-specific mechanisms:** PCA-to-red-phenazine conversion is well-supported mechanistically but is **contextual** (co-culture / metabolite exposure), so it should be curated as an “uncertain/conditional” subgraph rather than a general cause of red pigmentation for a single microbe in isolation. (iloabuchi2024bacillussp.g2112 pages 1-2, iloabuchi2024bacillussp.g2112 pages 4-6)

---

## 5) Data and statistics from recent studies

### Prodigiosin/prodiginines
- **19.7 mg/L** prodigiosin in shake flasks after optimization (marine *Serratia rubidaea*). (pereira2024improvingbioprocessconditions pages 1-2)
- **293.1 mg/L in 24 h** in a 2 L bioreactor (BE) with productivity **12.21 mg/(L·h)**; oxygen transfer and vessel geometry strongly affected outcomes. (pereira2024improvingbioprocessconditions pages 14-16, pereira2024improvingbioprocessconditions pages 16-17, pereira2024improvingbioprocessconditions media 9473e601)
- χ phage exposure in *S. marcescens* ATCC 274 increased pigment concentration **5.5-fold** when added to stationary phase; pig operon transcription increased about **3-fold** with χ-induced lysate. (esteves2024serratiamarcescensatcc pages 2-3, esteves2024serratiamarcescensatcc pages 1-2)

### Carotenoids (Rhodotorula-focused)
- Multiple mg/L-scale yields are summarized across studies (e.g., **7.3 mg/L** total carotenoids on olive mill waste; **62 mg/L β-carotene** from vegetable market waste in *R. toruloides*), illustrating real-world feasible production ranges. (ochoavinals2024currentadvancesin pages 5-6)

### Red phenazine derivatives (interaction-driven)
- PCA above **40 µg/mL** prevented *Bacillus* growth (germination) but already-grown cultures could survive and convert PCA into red pigments; the red pigments were structurally identified as novel **N5-glucosylated phenazine derivatives**. (iloabuchi2024bacillussp.g2112 pages 1-2, iloabuchi2024bacillussp.g2112 pages 2-4)

---

## Candidate nodes for `data/traits/morphology/red_pigmented.yaml`

### Phenotype node
- **METPO:1003028** red pigmented (given)

### Pigment chemicals (ChEBI grounding suggested; IDs to be looked up by curator)
- Prodigiosin / prodiginines (red tripyrrole pigments) (barreto2023microbialpigmentsmajor pages 10-12, lu2024prodigiosinunveilingthe pages 8-9)
- Lycopene (red carotenoid) (barreto2023microbialpigmentsmajor pages 4-6)
- β-carotene; torulene; torularhodin (red yeast carotenoids) (ochoavinals2024currentadvancesin pages 2-5, ochoavinals2024currentadvancesin pages 7-8)
- Phenazine-1-carboxylic acid (PCA) and N5-glucosylated phenazine derivatives (conditional) (iloabuchi2024bacillussp.g2112 pages 1-2, iloabuchi2024bacillussp.g2112 pages 2-4)

### Pathways/modules
- Prodigiosin/prodiginine biosynthesis (Pig/Red gene cluster pathways) (barreto2023microbialpigmentsmajor pages 10-12, lu2024prodigiosinunveilingthe pages 8-9)
- Carotenoid biosynthesis (GGPP → phytoene → lycopene → carotenes/xanthophylls) (barreto2023microbialpigmentsmajor pages 4-6)
- Phenazine modification/detoxification via N5-glucosylation (conditional) (iloabuchi2024bacillussp.g2112 pages 1-2)

### Genes / enzymes / regulators (label nodes; UniProt grounding should be done per strain)
- **pigC** (MAP–MBC ligase/condensation enzyme) (lu2024prodigiosinunveilingthe pages 8-9)
- **pigD, pigE, pigB** (MAP branch enzymes; stepwise MAP formation) (sakaikawada2020characterizationofprodiginine pages 23-29)
- QS system nodes: **SmaI/SmaR**, **SpnI/SpnR**, **LuxS/AI-2** (reviewed regulators) (lu2024prodigiosinunveilingthe pages 8-9)
- Two-component systems: **CpxA/CpxR**, **EnvZ/OmpR**, **RcsB/RcsC**; indirect regulation via **FlhDC** reported for RcsB in Serratia (lu2024prodigiosinunveilingthe pages 9-10, pan2021regulatorrcsbcontrols pages 10-12)
- Transcription factor **Fnr** (negative regulation described in review) (lu2024prodigiosinunveilingthe pages 8-9)

### Environmental/assay/process factor nodes (ENVO where possible; often assay descriptors)
- Temperature, pH, oxygen availability/kLa, agitation/aeration, light regime (prodigiosin; carotenoids) (lu2024prodigiosinunveilingthe pages 9-10, pereira2024improvingbioprocessconditions pages 19-20, ochoavinals2024currentadvancesin pages 7-8)
- Biotic stress: χ phage infection / phage-induced lysate (prodigiosin induction) (esteves2024serratiamarcescensatcc pages 1-2)
- Oxidative metabolism / ROS stress (carotenoid induction) (mosquedamartinez2024inrhodotorulamucilaginosa pages 8-9)

---

## Evidence-backed candidate causal edges (curation table)
The following table is intended to be directly usable during YAML curation.

| Edge (S–P–O) | Entity type notes (gene/pathway/environment/chemical) | Evidence snippet | Source (DOI, year, URL) | Confidence/curation notes |
|---|---|---|---|---|
| prodiginine biosynthetic gene cluster (Pig/Red) — enables — red-pigmented phenotype | pathway/gene cluster → phenotype | “Prodiginines are hydrophobic, red tripyrrole alkaloid pigments… Biosynthesis is genetically encoded by variable gene clusters (e.g., Pig in Serratia, Red in Streptomyces)” (barreto2023microbialpigmentsmajor pages 10-12) | 10.3390/microorganisms11122920 (2023), https://doi.org/10.3390/microorganisms11122920 | High confidence; broad cross-taxon mechanism for bacterial red pigmentation driven by prodiginines. |
| MBC + MAP condensation pathway — produces — prodigiosin/prodiginine red pigment | pathway/chemical intermediates → pigment | “Their biosynthesis follows a bifurcated pathway that culminates in an enzymatic condensation between a bipyrrole intermediate (4-methoxy-2-2′-bipyrrole-5-carbaldehyde, MBC) and a monopyrrole unit” (barreto2023biotechnologicalapplicationsof pages 11-14) | 10.20944/preprints202310.0121.v1 (2023), https://doi.org/10.20944/preprints202310.0121.v1 | High confidence for prodiginine-type red pigmentation; curate as pathway-level causal edge. |
| proline/serine/malonyl-CoA — contributes_to — MBC biosynthesis | metabolite precursors → pathway intermediate | “MBC arises from proline, serine, and malonyl-CoA” (barreto2023microbialpigmentsmajor pages 10-12) | 10.3390/microorganisms11122920 (2023), https://doi.org/10.3390/microorganisms11122920 | High confidence; useful as precursor edge if TraitMech includes metabolite nodes. |
| 2-octenal + pyruvate — contributes_to — MAP biosynthesis | metabolite precursors → pathway intermediate | “The monopyrrole MAP derives from the fatty-acid-related 2-octenal and pyruvate” (barreto2023microbialpigmentsmajor pages 10-12) | 10.3390/microorganisms11122920 (2023), https://doi.org/10.3390/microorganisms11122920 | High confidence; mechanistically specific but taxon-biased toward classical prodigiosin pathways. |
| pigC — catalyzes — MAP + MBC condensation to prodigiosin | gene/enzyme → pathway reaction | “The ligase encoded by pigC is the key enzyme that links MAP and MBC” (lu2024prodigiosinunveilingthe pages 8-9) | 10.3389/fmicb.2024.1412776 (2024), https://doi.org/10.3389/fmicb.2024.1412776 | High confidence; strong candidate core causal edge for red prodigiosin pigmentation. |
| pigD — involved_in — MAP formation | gene/enzyme → pathway intermediate | “PigD catalyzes addition of pyruvate to 2-octenal… to form 3-acetyloctanal” (sakaikawada2020characterizationofprodiginine pages 23-29) | 10.33043/ff.3.1.33-51 (2020), https://doi.org/10.33043/ff.3.1.33-51 | Moderate confidence; good mechanistic detail, but source is older and focused on one lineage. |
| pigE — involved_in — MAP formation | gene/enzyme → pathway intermediate | “PigE transfers an amino group to that aldehyde and cyclizes to H2MAP” (sakaikawada2020characterizationofprodiginine pages 23-29) | 10.33043/ff.3.1.33-51 (2020), https://doi.org/10.33043/ff.3.1.33-51 | Moderate confidence; taxon-specific enzymology but canonical pathway component. |
| pigB — oxidizes — H2MAP to MAP | gene/enzyme → pathway intermediate | “PigB oxidizes H2MAP to MAP” (sakaikawada2020characterizationofprodiginine pages 23-29) | 10.33043/ff.3.1.33-51 (2020), https://doi.org/10.33043/ff.3.1.33-51 | Moderate confidence; useful if graph models stepwise prodigiosin biosynthesis. |
| χ phage infection — increases_transcription_of — pig operon | environmental/biotic factor → operon expression | “addition of a χ-induced S. marcescens cell lysate to uninfected cultures produced a roughly threefold increase in transcription of the pig operon” (esteves2024serratiamarcescensatcc pages 1-2) | 10.1038/s41598-024-68747-3 (2024), https://doi.org/10.1038/s41598-024-68747-3 | High confidence but assay-specific; likely curate as conditional/experimental edge. |
| χ phage infection — increases — prodigiosin production | environmental/biotic factor → pigment phenotype | “greater than fivefold overproduction of the red pigment prodigiosin upon χ addition” (esteves2024serratiamarcescensatcc pages 1-2); “5.5-fold increase in pigment concentration” in stationary phase (esteves2024serratiamarcescensatcc pages 2-3) | 10.1038/s41598-024-68747-3 (2024), https://doi.org/10.1038/s41598-024-68747-3 | High confidence for S. marcescens ATCC 274; curate as strain- and phage-specific unless generalized carefully. |
| native pig promoter (Ppig) — mediates_response_to — phage-induced pigmentation increase | promoter/regulatory DNA → phenotype response | “replacing the native pig promoter with a constitutive promoter abolished the phage-associated pigmentation increase” (esteves2024serratiamarcescensatcc pages 1-2) | 10.1038/s41598-024-68747-3 (2024), https://doi.org/10.1038/s41598-024-68747-3 | High confidence; good regulatory edge if promoter nodes are allowed. |
| temperature (below 22°C or above 30°C) — decreases_activity_of — PigC condensing enzyme | environmental factor → enzyme activity | “temperature (pigC-produced condensing enzyme activity drops <22°C and is inactive >30°C)” (lu2024prodigiosinunveilingthe pages 8-9) | 10.3389/fmicb.2024.1412776 (2024), https://doi.org/10.3389/fmicb.2024.1412776 | Moderate confidence; phrased from review synthesis, but mechanistically valuable. |
| CpxA/CpxR system activation — inhibits_transcription_of — pig gene cluster | regulatory system → operon expression | “the sensor HK protein CpxA is activated, triggering a phosphorylation cascade that ultimately inhibits transcription of pig gene clusters and reduces PG production” (lu2024prodigiosinunveilingthe pages 9-10) | 10.3389/fmicb.2024.1412776 (2024), https://doi.org/10.3389/fmicb.2024.1412776 | High confidence; strong negative regulatory edge for prodigiosin-based redness. |
| oxygen transfer / high oxygen availability — increases — prodigiosin production | environmental/process factor → pigment production | “Oxygen availability was critical—high oxygen concentrations were necessary for growth and to maintain the oxidative state of the pigment” (pereira2024improvingbioprocessconditions pages 19-20); “maximum prodigiosin concentration… attained at 80% headspace” (pereira2024improvingbioprocessconditions pages 9-11) | 10.3390/md22040142 (2024), https://doi.org/10.3390/md22040142 | High confidence in marine Serratia bioprocess context; likely assay/process-sensitive. |
| day/night light cycle — increases — prodigiosin production relative to continuous dark | environmental factor → pigment production | “Light regime mattered: normal day/night cycles gave higher prodigiosin than continuous dark” (pereira2024improvingbioprocessconditions pages 19-20) | 10.3390/md22040142 (2024), https://doi.org/10.3390/md22040142 | Moderate confidence; likely strain- and culture-condition-specific. |
| supplemented marine broth + optimized bioreactor conditions — increases — prodigiosin titer | medium/process factor → quantitative phenotype | “shake-flask prodigiosin rose 13-fold to 19.7 mg/L… In the bioreactor… reached 293.1 mg/L in 24 h” (pereira2024improvingbioprocessconditions pages 1-2, pereira2024improvingbioprocessconditions media 29e3a70c) | 10.3390/md22040142 (2024), https://doi.org/10.3390/md22040142 | High confidence quantitative implementation edge; useful for assay/experimental factor node rather than intrinsic trait node. |
| phytoene synthase reaction (2 GGPP → phytoene) followed by desaturation/isomerization — produces — lycopene | carotenoid pathway/enzyme steps → red pigment | “two GGPP molecules are condensed by phytoene synthase to form phytoene… to yield lycopene, described as a red-colored pigment” (barreto2023microbialpigmentsmajor pages 4-6) | 10.3390/microorganisms11122920 (2023), https://doi.org/10.3390/microorganisms11122920 | High confidence; broad carotenoid mechanism for red pigmentation. |
| lycopene — confers_color — red pigmentation | chemical pigment → phenotype | “lycopene, described explicitly as ‘a red-colored pigment’” (barreto2023microbialpigmentsmajor pages 4-6) | 10.3390/microorganisms11122920 (2023), https://doi.org/10.3390/microorganisms11122920 | High confidence; suitable general pigment-to-color edge. |
| Rhodotorula carotenoid biosynthesis — produces — torularhodin/torulene/β-carotene | pathway/taxon-specific carotenoid set → pigments | “The excerpt identifies the principal red-yeast carotenoids as torulene, torularhodin and β-carotene” (ochoavinals2024currentadvancesin pages 2-5) | 10.3390/fermentation10040190 (2024), https://doi.org/10.3390/fermentation10040190 | High confidence; good for yeast red pigmentation branch. |
| oxidative metabolism / ROS stress — increases — carotenoid synthesis in Rhodotorula | environmental/physiological factor → pigment pathway | “oxidative metabolism in cells grown in YPLac induces oxidative stress, leading to increase synthesis of carotenoids” (mosquedamartinez2024inrhodotorulamucilaginosa pages 8-9) | 10.3389/ffunb.2024.1378590 (2024), https://doi.org/10.3389/ffunb.2024.1378590 | High confidence; strong conditional edge for stress-induced red yeast pigmentation. |
| light exposure (LED/UV/photoperiod) — increases — Rhodotorula carotenoid accumulation | environmental factor → pigment production | “light exposure (white LEDs, colored LEDs, UV; photoperiods)… increase carotenoid accumulation” with examples including “green LEDs 3473 µg/L and red LEDs 3497 µg/L” (ochoavinals2024currentadvancesin pages 7-8) | 10.3390/fermentation10040190 (2024), https://doi.org/10.3390/fermentation10040190 | Moderate-high confidence; likely species/strain-specific but well supported across studies. |
| low-to-moderate acidic pH — increases — Rhodotorula carotenoid accumulation | environmental factor → pigment production | “low-to-moderate acidic pH… optimal ranges ~5.0–6.0” with yields including “3.3 mg/L” and “63.37 µg/g at pH 6.1” (ochoavinals2024currentadvancesin pages 7-8) | 10.3390/fermentation10040190 (2024), https://doi.org/10.3390/fermentation10040190 | Moderate confidence; useful as conditional process edge. |
| increased aeration/agitation — increases — Rhodotorula carotenoid yields | environmental/process factor → pigment production | “higher agitation/aeration and aerobic conditions boosted carotenoid yields” (ochoavinals2024currentadvancesin pages 7-8) | 10.3390/fermentation10040190 (2024), https://doi.org/10.3390/fermentation10040190 | Moderate confidence; process-context dependent. |
| phenazine-1-carboxylic acid (PCA) exposure to Bacillus sp. G2112 — causes_conversion_to — red glucosylated phenazine derivatives | chemical + microbial interaction → red pigments | “PCA released by Pseudomonas sp. G124 was transformed by Bacillus sp. G2112 into red pigments” (iloabuchi2024bacillussp.g2112 pages 1-2) | 10.3390/molecules29030589 (2024), https://doi.org/10.3390/molecules29030589 | High confidence but niche interaction-specific; likely not a general standalone trait mechanism. |
| Bacillus sp. G2112 N5-glucosylation of PCA — produces — 5N-glucosylated red phenazine derivatives | chemical transformation pathway → red pigments | “identified as novel 5N-glucosylated phenazine derivatives” including “7-imino-5N-(1′β-D-glucopyranosyl)… and 3-imino-5N-(1′β-D-glucopyranosyl)…” (iloabuchi2024bacillussp.g2112 pages 1-2, iloabuchi2024bacillussp.g2112 pages 6-7) | 10.3390/molecules29030589 (2024), https://doi.org/10.3390/molecules29030589 | High confidence for this co-culture detoxification mechanism; curate as interaction-specific and uncertain for general trait graph. |
| PCA concentration above ~40 µg/mL — inhibits_growth_of — Bacillus sp. G2112 while surviving cells form red pigments | chemical stressor → growth inhibition / induced pigmentation | “Bacillus sp. G2112 could not grow in the presence of PCA concentrations greater than 40 µg/mL, whereas already-grown cultures… survived PCA exposure and converted PCA to red pigments” (iloabuchi2024bacillussp.g2112 pages 1-2) | 10.3390/molecules29030589 (2024), https://doi.org/10.3390/molecules29030589 | Moderate confidence; useful for experimental-factor edge, but not core universal red-pigment mechanism. |


*Table: This table lists evidence-backed candidate causal edges for the microbial trait 'red pigmented,' spanning prodiginine, carotenoid, and interaction-dependent phenazine mechanisms. It is designed to support TraitMech curation by linking genes, pathways, environmental factors, and chemicals to red pigmentation with source-specific confidence notes.*

---

## Visual evidence (bioprocess quantitation)
The following extracted figures/tables document the relationship between oxygen transfer (kLa), scale-up, and the achieved prodigiosin titers in 2 L bioreactors. (pereira2024improvingbioprocessconditions media 29e3a70c, pereira2024improvingbioprocessconditions media 9473e601, pereira2024improvingbioprocessconditions media 4b42c724, pereira2024improvingbioprocessconditions media 7545cc55)

---

## DOI-first bibliography (with publication dates and URLs)

1. **Pereira RFS, de Carvalho CCCR.** Improving Bioprocess Conditions for the Production of Prodigiosin Using a Marine *Serratia rubidaea* Strain. *Marine Drugs*. **Mar 2024**. DOI: **10.3390/md22040142**. URL: https://doi.org/10.3390/md22040142 (pereira2024improvingbioprocessconditions pages 1-2)
2. **Esteves NC, Scharf BE.** *Serratia marcescens* ATCC 274 increases production of the red pigment prodigiosin in response to Chi phage infection. *Scientific Reports*. **Jul 2024**. DOI: **10.1038/s41598-024-68747-3**. URL: https://doi.org/10.1038/s41598-024-68747-3 (esteves2024serratiamarcescensatcc pages 1-2)
3. **Lu Y, Liu D, Jiang R, Li Z, Gao X.** Prodigiosin: unveiling the crimson wonder – a comprehensive journey from diverse bioactivity to synthesis and yield enhancement. *Frontiers in Microbiology*. **Jun 2024**. DOI: **10.3389/fmicb.2024.1412776**. URL: https://doi.org/10.3389/fmicb.2024.1412776 (lu2024prodigiosinunveilingthe pages 8-9)
4. **Ochoa‑Viñals N, et al.** Current Advances in Carotenoid Production by *Rhodotorula* sp. *Fermentation*. **Mar 2024**. DOI: **10.3390/fermentation10040190**. URL: https://doi.org/10.3390/fermentation10040190 (ochoavinals2024currentadvancesin pages 1-2)
5. **Mosqueda‑Martínez E, et al.** In *Rhodotorula mucilaginosa*, active oxidative metabolism increases carotenoids to inactivate excess reactive oxygen species. *Frontiers in Fungal Biology*. **Sep 2024**. DOI: **10.3389/ffunb.2024.1378590**. URL: https://doi.org/10.3389/ffunb.2024.1378590 (mosquedamartinez2024inrhodotorulamucilaginosa pages 1-2)
6. **Iloabuchi K, Spiteller D.** Bacillus sp. G2112 Detoxifies Phenazine-1-carboxylic Acid by N5 Glucosylation. *Molecules*. **Jan 2024**. DOI: **10.3390/molecules29030589**. URL: https://doi.org/10.3390/molecules29030589 (iloabuchi2024bacillussp.g2112 pages 1-2)
7. **de Oliveira Barreto JV, et al.** Microbial Pigments: Major Groups and Industrial Applications. *Microorganisms*. **Dec 2023**. DOI: **10.3390/microorganisms11122920**. URL: https://doi.org/10.3390/microorganisms11122920 (barreto2023microbialpigmentsmajor pages 10-12)

---

## Warnings (do-not-curate-yet / uncertain edges)
1. **Co-culture/interaction-dependent red phenazines:** PCA → red N5-glucosylated phenazines is compelling but may not generalize outside the specific *Bacillus–Pseudomonas* interaction and exposure regime; curate as conditional. (iloabuchi2024bacillussp.g2112 pages 1-2, iloabuchi2024bacillussp.g2112 pages 4-6)
2. **Process/bioreactor factors vs intrinsic trait:** kLa, headspace, agitation strategy, vessel geometry, and day/night cycles are critical for pigment titers in industrial contexts, but may represent assay/process edges rather than a stable trait in all environments. (pereira2024improvingbioprocessconditions pages 9-11, pereira2024improvingbioprocessconditions pages 19-20, pereira2024improvingbioprocessconditions pages 14-16)
3. **Temperature-dependent enzyme statements:** Some temperature–activity claims for PigC are review-level synthesis; consider confirming with primary enzymology if you want to curate enzyme-kinetic bounds as hard constraints. (lu2024prodigiosinunveilingthe pages 8-9)


References

1. (barreto2023microbialpigmentsmajor pages 10-12): João Vitor de Oliveira Barreto, Livia Marques Casanova, Athayde Neves Junior, Maria Cristina Pinheiro Pereira Reis-Mansur, and Alane Beatriz Vermelho. Microbial pigments: major groups and industrial applications. Microorganisms, 11:2920, Dec 2023. URL: https://doi.org/10.3390/microorganisms11122920, doi:10.3390/microorganisms11122920. This article has 94 citations.

2. (barreto2023microbialpigmentsmajor pages 4-6): João Vitor de Oliveira Barreto, Livia Marques Casanova, Athayde Neves Junior, Maria Cristina Pinheiro Pereira Reis-Mansur, and Alane Beatriz Vermelho. Microbial pigments: major groups and industrial applications. Microorganisms, 11:2920, Dec 2023. URL: https://doi.org/10.3390/microorganisms11122920, doi:10.3390/microorganisms11122920. This article has 94 citations.

3. (lu2024prodigiosinunveilingthe pages 8-9): Yonglin Lu, Derun Liu, Renhui Jiang, Ziyun Li, and Xueyan Gao. Prodigiosin: unveiling the crimson wonder – a comprehensive journey from diverse bioactivity to synthesis and yield enhancement. Frontiers in Microbiology, Jun 2024. URL: https://doi.org/10.3389/fmicb.2024.1412776, doi:10.3389/fmicb.2024.1412776. This article has 28 citations and is from a peer-reviewed journal.

4. (ochoavinals2024currentadvancesin pages 2-5): Nayra Ochoa-Viñals, Dania Alonso-Estrada, Sandra Pacios-Michelena, Ariel García-Cruz, Rodolfo Ramos-González, Evelyn Faife-Pérez, Lourdes Georgina Michelena-Álvarez, José Luis Martínez-Hernández, and Anna Iliná. Current advances in carotenoid production by rhodotorula sp. Fermentation, 10:190, Mar 2024. URL: https://doi.org/10.3390/fermentation10040190, doi:10.3390/fermentation10040190. This article has 49 citations.

5. (iloabuchi2024bacillussp.g2112 pages 1-2): Kenechukwu Iloabuchi and Dieter Spiteller. Bacillus sp. g2112 detoxifies phenazine-1-carboxylic acid by n5 glucosylation. Molecules, 29:589, Jan 2024. URL: https://doi.org/10.3390/molecules29030589, doi:10.3390/molecules29030589. This article has 6 citations.

6. (iloabuchi2024bacillussp.g2112 pages 2-4): Kenechukwu Iloabuchi and Dieter Spiteller. Bacillus sp. g2112 detoxifies phenazine-1-carboxylic acid by n5 glucosylation. Molecules, 29:589, Jan 2024. URL: https://doi.org/10.3390/molecules29030589, doi:10.3390/molecules29030589. This article has 6 citations.

7. (barreto2023biotechnologicalapplicationsof pages 11-14): João Vitor de Oliveira Barreto, Livia Marques Casanova, Athayde Neves Junior, Maria Cristina Pinheiro Pereira Reis Mansur, and Alane Beatriz Vermelho. Biotechnological applications of microbial pigments. Unknown journal, Oct 2023. URL: https://doi.org/10.20944/preprints202310.0121.v1, doi:10.20944/preprints202310.0121.v1.

8. (esteves2024serratiamarcescensatcc pages 1-2): Nathaniel C. Esteves and Birgit E. Scharf. Serratia marcescens atcc 274 increases production of the red pigment prodigiosin in response to chi phage infection. Scientific Reports, Jul 2024. URL: https://doi.org/10.1038/s41598-024-68747-3, doi:10.1038/s41598-024-68747-3. This article has 6 citations and is from a peer-reviewed journal.

9. (esteves2024serratiamarcescensatcc pages 2-3): Nathaniel C. Esteves and Birgit E. Scharf. Serratia marcescens atcc 274 increases production of the red pigment prodigiosin in response to chi phage infection. Scientific Reports, Jul 2024. URL: https://doi.org/10.1038/s41598-024-68747-3, doi:10.1038/s41598-024-68747-3. This article has 6 citations and is from a peer-reviewed journal.

10. (esteves2024serratiamarcescensatcc pages 3-5): Nathaniel C. Esteves and Birgit E. Scharf. Serratia marcescens atcc 274 increases production of the red pigment prodigiosin in response to chi phage infection. Scientific Reports, Jul 2024. URL: https://doi.org/10.1038/s41598-024-68747-3, doi:10.1038/s41598-024-68747-3. This article has 6 citations and is from a peer-reviewed journal.

11. (pereira2024improvingbioprocessconditions pages 1-2): Ricardo F. S. Pereira and Carla C. C. R. de Carvalho. Improving bioprocess conditions for the production of prodigiosin using a marine serratia rubidaea strain. Marine Drugs, 22:142, Mar 2024. URL: https://doi.org/10.3390/md22040142, doi:10.3390/md22040142. This article has 19 citations.

12. (pereira2024improvingbioprocessconditions pages 14-16): Ricardo F. S. Pereira and Carla C. C. R. de Carvalho. Improving bioprocess conditions for the production of prodigiosin using a marine serratia rubidaea strain. Marine Drugs, 22:142, Mar 2024. URL: https://doi.org/10.3390/md22040142, doi:10.3390/md22040142. This article has 19 citations.

13. (pereira2024improvingbioprocessconditions pages 16-17): Ricardo F. S. Pereira and Carla C. C. R. de Carvalho. Improving bioprocess conditions for the production of prodigiosin using a marine serratia rubidaea strain. Marine Drugs, 22:142, Mar 2024. URL: https://doi.org/10.3390/md22040142, doi:10.3390/md22040142. This article has 19 citations.

14. (pereira2024improvingbioprocessconditions pages 9-11): Ricardo F. S. Pereira and Carla C. C. R. de Carvalho. Improving bioprocess conditions for the production of prodigiosin using a marine serratia rubidaea strain. Marine Drugs, 22:142, Mar 2024. URL: https://doi.org/10.3390/md22040142, doi:10.3390/md22040142. This article has 19 citations.

15. (pereira2024improvingbioprocessconditions media 29e3a70c): Ricardo F. S. Pereira and Carla C. C. R. de Carvalho. Improving bioprocess conditions for the production of prodigiosin using a marine serratia rubidaea strain. Marine Drugs, 22:142, Mar 2024. URL: https://doi.org/10.3390/md22040142, doi:10.3390/md22040142. This article has 19 citations.

16. (pereira2024improvingbioprocessconditions media 9473e601): Ricardo F. S. Pereira and Carla C. C. R. de Carvalho. Improving bioprocess conditions for the production of prodigiosin using a marine serratia rubidaea strain. Marine Drugs, 22:142, Mar 2024. URL: https://doi.org/10.3390/md22040142, doi:10.3390/md22040142. This article has 19 citations.

17. (pereira2024improvingbioprocessconditions media 4b42c724): Ricardo F. S. Pereira and Carla C. C. R. de Carvalho. Improving bioprocess conditions for the production of prodigiosin using a marine serratia rubidaea strain. Marine Drugs, 22:142, Mar 2024. URL: https://doi.org/10.3390/md22040142, doi:10.3390/md22040142. This article has 19 citations.

18. (pereira2024improvingbioprocessconditions media 7545cc55): Ricardo F. S. Pereira and Carla C. C. R. de Carvalho. Improving bioprocess conditions for the production of prodigiosin using a marine serratia rubidaea strain. Marine Drugs, 22:142, Mar 2024. URL: https://doi.org/10.3390/md22040142, doi:10.3390/md22040142. This article has 19 citations.

19. (ochoavinals2024currentadvancesin pages 7-8): Nayra Ochoa-Viñals, Dania Alonso-Estrada, Sandra Pacios-Michelena, Ariel García-Cruz, Rodolfo Ramos-González, Evelyn Faife-Pérez, Lourdes Georgina Michelena-Álvarez, José Luis Martínez-Hernández, and Anna Iliná. Current advances in carotenoid production by rhodotorula sp. Fermentation, 10:190, Mar 2024. URL: https://doi.org/10.3390/fermentation10040190, doi:10.3390/fermentation10040190. This article has 49 citations.

20. (ochoavinals2024currentadvancesin pages 5-6): Nayra Ochoa-Viñals, Dania Alonso-Estrada, Sandra Pacios-Michelena, Ariel García-Cruz, Rodolfo Ramos-González, Evelyn Faife-Pérez, Lourdes Georgina Michelena-Álvarez, José Luis Martínez-Hernández, and Anna Iliná. Current advances in carotenoid production by rhodotorula sp. Fermentation, 10:190, Mar 2024. URL: https://doi.org/10.3390/fermentation10040190, doi:10.3390/fermentation10040190. This article has 49 citations.

21. (mosquedamartinez2024inrhodotorulamucilaginosa pages 8-9): Edson Mosqueda-Martínez, Natalia Chiquete-Félix, Paulina Castañeda-Tamez, Carolina Ricardez-García, Manuel Gutiérrez-Aguilar, Salvador Uribe-Carvajal, and Ofelia Mendez-Romero. In rhodotorula mucilaginosa, active oxidative metabolism increases carotenoids to inactivate excess reactive oxygen species. Frontiers in Fungal Biology, Sep 2024. URL: https://doi.org/10.3389/ffunb.2024.1378590, doi:10.3389/ffunb.2024.1378590. This article has 20 citations.

22. (ochoavinals2024currentadvancesin pages 1-2): Nayra Ochoa-Viñals, Dania Alonso-Estrada, Sandra Pacios-Michelena, Ariel García-Cruz, Rodolfo Ramos-González, Evelyn Faife-Pérez, Lourdes Georgina Michelena-Álvarez, José Luis Martínez-Hernández, and Anna Iliná. Current advances in carotenoid production by rhodotorula sp. Fermentation, 10:190, Mar 2024. URL: https://doi.org/10.3390/fermentation10040190, doi:10.3390/fermentation10040190. This article has 49 citations.

23. (barreto2023biotechnologicalapplicationsof pages 7-9): João Vitor de Oliveira Barreto, Livia Marques Casanova, Athayde Neves Junior, Maria Cristina Pinheiro Pereira Reis Mansur, and Alane Beatriz Vermelho. Biotechnological applications of microbial pigments. Unknown journal, Oct 2023. URL: https://doi.org/10.20944/preprints202310.0121.v1, doi:10.20944/preprints202310.0121.v1.

24. (lu2024prodigiosinunveilingthe pages 9-10): Yonglin Lu, Derun Liu, Renhui Jiang, Ziyun Li, and Xueyan Gao. Prodigiosin: unveiling the crimson wonder – a comprehensive journey from diverse bioactivity to synthesis and yield enhancement. Frontiers in Microbiology, Jun 2024. URL: https://doi.org/10.3389/fmicb.2024.1412776, doi:10.3389/fmicb.2024.1412776. This article has 28 citations and is from a peer-reviewed journal.

25. (iloabuchi2024bacillussp.g2112 pages 4-6): Kenechukwu Iloabuchi and Dieter Spiteller. Bacillus sp. g2112 detoxifies phenazine-1-carboxylic acid by n5 glucosylation. Molecules, 29:589, Jan 2024. URL: https://doi.org/10.3390/molecules29030589, doi:10.3390/molecules29030589. This article has 6 citations.

26. (sakaikawada2020characterizationofprodiginine pages 23-29): FE Sakai-Kawada. Characterization of prodiginine biosynthetic pathway in pseudoalteromonas rubra ppb1 isolated from petrosia species. Unknown journal, 2020.

27. (pan2021regulatorrcsbcontrols pages 10-12): Xuewei Pan, Mi Tang, Jiajia You, Fei Liu, Changhao Sun, Tolbert Osire, Weilai Fu, Ganfeng Yi, Taowei Yang, Shang-Tian Yang, and Zhiming Rao. Regulator rcsb controls prodigiosin synthesis and various cellular processes in serratia marcescens jnb5-1. Jan 2021. URL: https://doi.org/10.1128/aem.02052-20, doi:10.1128/aem.02052-20. This article has 28 citations and is from a peer-reviewed journal.

28. (pereira2024improvingbioprocessconditions pages 19-20): Ricardo F. S. Pereira and Carla C. C. R. de Carvalho. Improving bioprocess conditions for the production of prodigiosin using a marine serratia rubidaea strain. Marine Drugs, 22:142, Mar 2024. URL: https://doi.org/10.3390/md22040142, doi:10.3390/md22040142. This article has 19 citations.

29. (iloabuchi2024bacillussp.g2112 pages 6-7): Kenechukwu Iloabuchi and Dieter Spiteller. Bacillus sp. g2112 detoxifies phenazine-1-carboxylic acid by n5 glucosylation. Molecules, 29:589, Jan 2024. URL: https://doi.org/10.3390/molecules29030589, doi:10.3390/molecules29030589. This article has 6 citations.

30. (mosquedamartinez2024inrhodotorulamucilaginosa pages 1-2): Edson Mosqueda-Martínez, Natalia Chiquete-Félix, Paulina Castañeda-Tamez, Carolina Ricardez-García, Manuel Gutiérrez-Aguilar, Salvador Uribe-Carvajal, and Ofelia Mendez-Romero. In rhodotorula mucilaginosa, active oxidative metabolism increases carotenoids to inactivate excess reactive oxygen species. Frontiers in Fungal Biology, Sep 2024. URL: https://doi.org/10.3389/ffunb.2024.1378590, doi:10.3389/ffunb.2024.1378590. This article has 20 citations.