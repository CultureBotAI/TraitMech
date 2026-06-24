---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T21:51:27.376210'
end_time: '2026-06-17T22:01:32.517858'
duration_seconds: 605.14
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: facultative oxygen preference
  trait_identifier: METPO:1000612
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: facultative_oxygen_preference
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: An oxygen preference that describes a microorganism that can grow with
    or without molecular oxygen.
  parent_traits: METPO:1000601
  synonyms: Ox_facultative_aerobe_anaerobe
  evidence_summary: 'DOI:10.1111/cmi.13338: cope with changing oxygen levels (Supports
    facultative oxygen preference as growth across oxygen regimes.) | DOI:10.1089/ars.2011.4051:
    adaptation of respiratory metabolism to changing environments (Supports oxygen-responsive
    metabolic switching.)'
  causal_graph_summary: 'facultative_oxygen_preference_switching: 5 nodes, 4 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 28
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** facultative oxygen preference
- **METPO identifier:** METPO:1000612
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An oxygen preference that describes a microorganism that can grow with or without molecular oxygen.
- **Parent traits:** METPO:1000601
- **Synonyms:** Ox_facultative_aerobe_anaerobe
- **Existing evidence:** DOI:10.1111/cmi.13338: cope with changing oxygen levels (Supports facultative oxygen preference as growth across oxygen regimes.) | DOI:10.1089/ars.2011.4051: adaptation of respiratory metabolism to changing environments (Supports oxygen-responsive metabolic switching.)
- **Existing causal graph summary:** facultative_oxygen_preference_switching: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **facultative oxygen preference** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/facultative_oxygen_preference.yaml`.

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
- **Trait label:** facultative oxygen preference
- **METPO identifier:** METPO:1000612
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An oxygen preference that describes a microorganism that can grow with or without molecular oxygen.
- **Parent traits:** METPO:1000601
- **Synonyms:** Ox_facultative_aerobe_anaerobe
- **Existing evidence:** DOI:10.1111/cmi.13338: cope with changing oxygen levels (Supports facultative oxygen preference as growth across oxygen regimes.) | DOI:10.1089/ars.2011.4051: adaptation of respiratory metabolism to changing environments (Supports oxygen-responsive metabolic switching.)
- **Existing causal graph summary:** facultative_oxygen_preference_switching: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **facultative oxygen preference** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/facultative_oxygen_preference.yaml`.

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


## Curation-focused Research Report: Facultative oxygen preference (METPO:1000612)

### Scope summary (TraitMech curation)
**Facultative oxygen preference** refers to the physiological capacity of a microorganism to **grow with or without molecular oxygen (O2)** by flexibly using **aerobic respiration when O2 is present** and **anaerobic respiration and/or fermentation when O2 is absent or limiting**. Mechanistically, this trait is enabled by oxygen/redox-responsive regulatory systems (e.g., ArcAB/ArcA, FNR) that reprogram central metabolism and respiratory-chain usage across changing electron acceptor availability. In infection and host-associated niches, the trait is strongly shaped by **spatial oxygen gradients** (e.g., gut nanoaerobic zones, hypoxic wounds, bloodstream/tissue gradients), and by availability of **alternative terminal electron acceptors** such as nitrate or fumarate. (brown2023conservedmetabolicregulator pages 1-3, brown2023conservedmetabolicregulator pages 12-14, butler2023bacteroidesfragilismaintains pages 1-2)

**Boundary cases / nearby traits that should not be conflated**:
- **Obligate anaerobes with oxygen tolerance**: Some strict anaerobes can survive (and sometimes grow somewhat) at low O2 by expressing **O2-reducing/ROS-detoxifying enzymes**, but they are not necessarily facultative in the sense of maintaining robust growth across oxic and anoxic conditions. For example, *Clostridioides difficile* uses multiple O2-reductases with distinct activity windows and can tolerate low O2 exposures along gut gradients; this supports oxygen tolerance, not canonical facultative oxygen preference. (caulat2024physiologicalroleand pages 1-2)
- **Microaerophily / “nanaerobiosis”**: Certain host-associated microbes experience trace oxygen regimes (e.g., gut epithelium). *Bacteroides fragilis* can run “nanaerobic” oxygen respiration via cytochrome bd at ~1,000–1,500 ppm O2 while maintaining anaerobic fumarate respiration concurrently. This illustrates a low-O2 ecological regime that interacts with, but does not replace, the broader facultative concept. (butler2023bacteroidesfragilismaintains pages 1-2)

---

## 1) Key concepts and definitions (current understanding)

### Core mechanistic idea
Facultative oxygen preference is best operationalized as **electron acceptor flexibility** coupled to **regulatory switching**:
- When O2 is available, cells can use it as a **high-energy terminal electron acceptor** via aerobic respiratory chains.
- When O2 is absent/low, cells maintain growth using **anaerobic respiration** (e.g., nitrate, fumarate, DMSO) and/or **fermentation**, often with distinct end products (e.g., lactate, acetate). (brown2023conservedmetabolicregulator pages 12-14, butler2023bacteroidesfragilismaintains pages 1-2)

### Environmental oxygen is heterogeneous and quantitatively relevant
Recent work underscores that oxygen availability is often a **gradient** rather than a binary condition:
- In the GI tract, longitudinal and lateral gradients can range from **4–5% O2 (small intestine)** down to **0.1–0.4% O2 (colon lumen)**, with lateral increases toward mucus and tissue (e.g., **1–2% O2** in mucus; **~5%** near tissue). (caulat2024physiologicalroleand pages 1-2)
- In the gut epithelium microzone, *B. fragilis* experiences “nanaerobic” oxygen levels of **~1,000–1,500 ppm O2** (reported as ~1–2 mmol O2/L) and adapts by using cytochrome bd while retaining anaerobic respiration. (butler2023bacteroidesfragilismaintains pages 1-2)

---

## 2) Recent developments & latest research (prioritizing 2023–2024)

### A. Canonical Gram-negative switching: ArcAB/ArcA and quinone/redox sensing
A 2023 mBio study emphasizes ArcA as a conserved metabolic regulator in facultative Enterobacterales, linking oxygen/redox cues and electron transport chain (ETC) activity to a **shift toward fermentation** when respiration is impaired. (brown2023conservedmetabolicregulator pages 1-3, brown2023conservedmetabolicregulator pages 12-14)

Mechanistic highlights suitable for curation:
- **ArcB senses respiratory/redox status** through changes in quinone electron flow and phosphorylates ArcA. (brown2023conservedmetabolicregulator pages 12-14)
- Activated ArcA represses respiratory operons (e.g., **nuo**, **shd**) and promotes fermentation-associated outputs, measurable as increased LDH activity and increased lactate/acetate under ETC/PMF uncoupling. (brown2023conservedmetabolicregulator pages 12-14)

Quantitative/statistical anchors:
- In bacteremia-relevant assays, chemical uncoupling with CCCP increased fermentative readouts, with species-specific CCCP doses (e.g., 15–25 µM) and ArcA-dependent components; an E. coli arcA mutant showed a **15.8% lower growth rate during anaerobic fermentation** in cited comparisons. (brown2023conservedmetabolicregulator pages 12-14)

### B. Concurrent anaerobic + nanaerobic respiration in *Bacteroides fragilis* (2023)
Butler et al. (2023) show *B. fragilis* maintains **simultaneous capability** for:
- **Anaerobic fumarate respiration**, and
- **Nanaerobic oxygen respiration** via **cytochrome bd oxidase**.

A key curatable statement is that **terminal enzyme usage depends on the terminal electron acceptor (O2 vs fumarate)** while both systems remain present, enabling rapid adaptation to fluctuating O2. (butler2023bacteroidesfragilismaintains pages 1-2)

Quantitative anchors:
- Nanaerobic O2: **~1,000–1,500 ppm** (often ~1,400 ppm in experiments). (butler2023bacteroidesfragilismaintains pages 1-2)
- Relative contributions of NADH:quinone oxidoreductases under nanaerobic: **NQR 77% / NDH2 23%** (similar to anaerobic ~70/30). (butler2023bacteroidesfragilismaintains pages 1-2)

### C. Oxygen-regime remodeling in an industrially relevant bacterium: *Propionibacterium freudenreichii* (2024)
Loivamaa et al. (2024) provide a strong multi-omics case study for oxygen-dependent metabolic remodeling in *P. freudenreichii*.

Quantitative transcriptomic statistics:
- Log phase: **1,375 genes (59.3%)** differentially expressed between conditions. (loivamaa2024aerobicadaptationand pages 9-12)
- Stationary: **906 genes (39.1%)** differentially expressed. (loivamaa2024aerobicadaptationand pages 9-12)
- Example operon: lactate utilization operon upregulated anaerobically with fold changes **~2.4–3.9**. (loivamaa2024aerobicadaptationand pages 9-12)

Quantitative phenotype data:
- Aerobic conditions increased final biomass (OD600/CFU) by **3.2× and 1.4×** respectively after 72 h. (loivamaa2024aerobicadaptationand pages 6-9)
- Cobamide profiles depended on oxygen regime (B12 vs pseudo-B12), and microaerobic conditions yielded **1.7–4.9× higher B12** than anaerobic in reported conditions. (loivamaa2024aerobicadaptationand pages 6-9)

### D. Anaerobiosis as an overlooked variable for phage therapy (2023)
Villamizar et al. (2023) analyze how oxygen availability reshapes both host physiology and phage infection dynamics in a facultative enteric model.

Mechanistic conclusions:
- Anaerobiosis activates **FNR and ArcA regulatory systems**, repressing aerobic energy pathways and inducing anaerobic metabolism genes. (villamizar2023anaerobiosisaneglected pages 13-16)

Quantitative transcriptomic statistics:
- Phage genes differentially expressed: **56** in aerobiosis vs **82** in anaerobiosis (with respective up/down splits). (villamizar2023anaerobiosisaneglected pages 11-13)
- Host genes during infection: **308 up / 26 down** in anaerobic infection vs **286 up / 124 down** in aerobic infection. (villamizar2023anaerobiosisaneglected pages 11-13)
- arcA upregulated with a marginal fold change **1.76** in anaerobiosis in this dataset. (villamizar2023anaerobiosisaneglected pages 11-13)

Functional outcome (qualitative but directly relevant to implementation): anaerobiosis was associated with longer eclipse/latent periods and smaller burst size, with reduced infection performance metrics despite increased receptor abundance. (villamizar2023anaerobiosisaneglected pages 13-16)

### E. Hypoxic wounds: nitrate respiration as a lever on virulence (2024)
Baker et al. (2024) connect oxygen limitation in diabetic foot-ulcer-like wounds to metabolic switching in *Staphylococcus aureus*.

Mechanistic claim:
- Lack of a terminal electron acceptor leads to impaired respiration, reduced menaquinone accumulation, **activation of SrrAB**, and a shift toward fermentative growth with increased virulence/biofilm outputs.
- Addition of nitrate as a terminal electron acceptor promotes anaerobic respiration and suppresses virulence factor expression via inactivation of two-component systems.

This work explicitly ties metabolic switching to an **in vivo diabetic pressure wound model** and demonstrates that dietary L-arginine (as nitrate source) attenuates disease severity. (baker2024largininesupplementationabrogates pages 1-3)

---

## 3) Current applications and real-world implementations

1. **Gut ecology and colonization**: Nanaerobic oxygen diffusing from intestinal epithelial cells provides trace O2 that can be used for respiration by gut microbes such as *B. fragilis*, while maintaining anaerobic respiration capacity for deeper anoxic regions. (butler2023bacteroidesfragilismaintains pages 1-2)

2. **Infection physiology in oxygen gradients**:
   - Enterobacterales bacteremia involves adaptation across host oxygen/iron stresses; ArcA-mediated switching is positioned as a fitness determinant under such conditions. (brown2023conservedmetabolicregulator pages 1-3, brown2023conservedmetabolicregulator pages 12-14)
   - Hypoxic chronic wounds (DFU contexts) can push pathogens into fermentative states that elevate virulence, potentially modulated by providing alternative electron acceptors (nitrate). (baker2024largininesupplementationabrogates pages 1-3)

3. **Biofilm control strategies**: In *E. coli*, perturbation of respiration/redox state (ArcA/B-linked) is associated with biofilm stimulation by sub-MIC bactericidal antibiotics, and **nitrate supplementation suppresses biofilm stimulation** in a dose-dependent manner in the reported assay. (yaeger2023centralmetabolismis pages 8-9)

4. **Phage therapy deployment**: Oxygen availability in intended application sites (intestine, wounds) can alter host metabolism and phage replication dynamics, indicating that phage therapy evaluations need anaerobic/microaerobic realism. (villamizar2023anaerobiosisaneglected pages 11-13, villamizar2023anaerobiosisaneglected pages 13-16)

5. **Industrial fermentation and food biotech**: Oxygen control (anaerobic, microaerobic, aerobic) can reshape metabolism and product profiles in industrially relevant organisms (e.g., *P. freudenreichii* cobamide profiles and biomass yields), motivating process-specific oxygen setpoints. (loivamaa2024aerobicadaptationand pages 6-9, loivamaa2024aerobicadaptationand pages 9-12)

---

## 4) Expert opinions / authoritative analyses embedded in recent sources

- The ArcAB system is framed as a “key mediator of metabolic adaptation” for Gram-negative facultative anaerobes during systemic infection conditions, consolidating diverse stress phenotypes into a respiratory-activity-centered model. (brown2023conservedmetabolicregulator pages 1-3)
- In gut-adapted respiration, maintaining both anaerobic and nanaerobic machinery is described as an “adaptation to an environment with low oxygen concentrations” to maximize energy conservation under fluctuation and spatial niche variation. (butler2023bacteroidesfragilismaintains pages 1-2)
- In phage-bacteria interaction research, anaerobiosis is argued to be an under-studied but important parameter because oxygen absence triggers metabolic changes in facultative bacteria that impact phage life cycle traits. (villamizar2023anaerobiosisaneglected pages 13-16)

---

## 5) Relevant statistics and data (curation-ready)

Selected quantitative values that can be directly incorporated into evidence notes:
- **Nanaerobic O2 in gut microzones**: ~1,000–1,500 ppm O2 (often ~1,400 ppm used in experiments). (butler2023bacteroidesfragilismaintains pages 1-2)
- **Relative NADH dehydrogenase contributions in *B. fragilis*** under nanaerobic conditions: NQR 77% / NDH2 23%. (butler2023bacteroidesfragilismaintains pages 1-2)
- **GI tract O2 gradients**: 4–5% (small intestine) down to 0.1–0.4% (colon lumen); lateral gradients to 1–2% (mucus) and ~5% (tissues). (caulat2024physiologicalroleand pages 1-2)
- **Transcriptomic remodeling in *P. freudenreichii***: 1,375 DEGs (59.3%) in log phase; 906 DEGs (39.1%) in stationary; lactate operon fold-change ~2.4–3.9. (loivamaa2024aerobicadaptationand pages 9-12)
- **Phage/host differential expression under O2 regimes** (Villamizar 2023): phage DE genes 56 (aerobic) vs 82 (anaerobic); host infection response 286 up/124 down (aerobic) vs 308 up/26 down (anaerobic); arcA fold change 1.76 under anaerobiosis. (villamizar2023anaerobiosisaneglected pages 11-13)

---

## Candidate nodes (grouped by type)

### Environmental / experimental factors
- Oxygen availability / oxygen tension (O2 gradient; nanaerobic O2; hypoxia/anoxia) (butler2023bacteroidesfragilismaintains pages 1-2, caulat2024physiologicalroleand pages 1-2)
- Terminal electron acceptor availability: nitrate, fumarate (butler2023bacteroidesfragilismaintains pages 1-2, baker2024largininesupplementationabrogates pages 1-3)
- Electron transport chain stress / PMF disruption (CCCP; respiratory stress) (brown2023conservedmetabolicregulator pages 12-14)

### Regulatory systems (proteins/complexes; label nodes unless taxon-specific UniProt is chosen)
- ArcB (sensor kinase), ArcA (response regulator) (brown2023conservedmetabolicregulator pages 12-14, brown2023conservedmetabolicregulator pages 1-3)
- FNR (oxygen-sensing transcription factor; enteric facultatives) (villamizar2023anaerobiosisaneglected pages 13-16)
- SrrAB (menaquinone/redox-responsive TCS in *S. aureus*) (baker2024largininesupplementationabrogates pages 1-3)

### Pathways / modules
- Aerobic respiration (ETC; TCA-linked respiration) (loivamaa2024aerobicadaptationand pages 9-12)
- Anaerobic respiration (nitrate respiration; fumarate respiration; DMSO respiration) (baker2024largininesupplementationabrogates pages 1-3, butler2023bacteroidesfragilismaintains pages 1-2, loivamaa2024aerobicadaptationand pages 18-20)
- Fermentation (lactate/acetate production; LDH activity readouts) (brown2023conservedmetabolicregulator pages 12-14)

### Enzymes / complexes
- Cytochrome bd oxidase (cyd; CydA) (butler2023bacteroidesfragilismaintains pages 1-2)
- Fumarate reductase (Frd) (butler2023bacteroidesfragilismaintains pages 1-2)
- NADH:quinone oxidoreductases: NQR, NDH2 (butler2023bacteroidesfragilismaintains pages 1-2)
- Nitrate reductase (NarG; Nar system) (loivamaa2024aerobicadaptationand pages 18-20)
- D-lactate dehydrogenase / LDH (phenotypic readout) (brown2023conservedmetabolicregulator pages 12-14)

### Chemicals / metabolites
- O2; nitrate; fumarate; menaquinone; NADH; FMN (for EET interface cases); lactate; acetate; H2O2/ROS (butler2023bacteroidesfragilismaintains pages 1-2, baker2024largininesupplementationabrogates pages 1-3, brown2023conservedmetabolicregulator pages 12-14)

---

## Candidate causal edges (evidence-backed)

| Edge (S–P–O) | Mechanistic rationale | Evidence snippet (short quote) | Source (DOI, year, URL) | Confidence/notes |
|---|---|---|---|---|
| Low oxygen / anaerobiosis → activates → ArcA/ArcAB regulon | ArcAB is a canonical redox-responsive system in facultative bacteria that helps reprogram metabolism as oxygen availability falls. | “ArcA is a global regulator for anaerobic metabolism in facultative bacteria” and anaerobiosis showed “arcA upregulation with a marginal fold2change of 1.76” (villamizar2023anaerobiosisaneglected pages 11-13) | Brown 2023 mBio, 10.1128/mbio.01448-23, https://doi.org/10.1128/mbio.01448-23; Villamizar 2023 AEM, 10.1128/aem.01491-23, https://doi.org/10.1128/aem.01491-23 | High for Enterobacterales/Salmonella; generalizable to many facultative bacteria, but exact sensing architecture is taxon-specific. |
| Anaerobiosis → activates → FNR-dependent anaerobic gene expression | FNR is a major oxygen-sensing regulator that turns on anaerobic functions when O2 is absent/low. | “absence of oxygen in enteric facultative bacteria activates the FNR and ArcA regulatory systems” (villamizar2023anaerobiosisaneglected pages 13-16) | Villamizar 2023 AEM, 10.1128/aem.01491-23, https://doi.org/10.1128/aem.01491-23 | High, but evidence here is review/summary-style and focused on enteric facultative bacteria. |
| FNR/ArcA activation → represses → aerobic energy-generating pathways | Facultative switching requires downregulating aerobic respiration modules during anaerobiosis. | FNR and ArcA “repress aerobic energy-generating pathways” under anaerobiosis (villamizar2023anaerobiosisaneglected pages 13-16) | Villamizar 2023 AEM, 10.1128/aem.01491-23, https://doi.org/10.1128/aem.01491-23 | Moderate-high; broad but not tied here to one exact operon. |
| FNR/ArcA activation → induces → anaerobic metabolism genes | Oxygen-responsive regulators enable use of anaerobic pathways needed for growth without O2. | FNR and ArcA “induce genes for anaerobic metabolism” (villamizar2023anaerobiosisaneglected pages 13-16) | Villamizar 2023 AEM, 10.1128/aem.01491-23, https://doi.org/10.1128/aem.01491-23 | High as a general regulatory edge for facultative enterics. |
| Decreased ETC activity / altered quinone electron flow → activates → ArcB sensor kinase | ArcB senses respiratory/redox status via the quinone pool, coupling oxygen limitation to transcriptional response. | “ArcB senses changes in quinone electron flow and phosphorylates ArcA” (brown2023conservedmetabolicregulator pages 12-14) | Brown 2023 mBio, 10.1128/mbio.01448-23, https://doi.org/10.1128/mbio.01448-23 | High for ArcAB-containing taxa; core mechanistic edge for facultative switching. |
| ArcB phosphorylation → activates → ArcA | Response regulator activation is the proximal control step connecting redox sensing to gene expression changes. | “ArcB senses changes in quinone electron flow and phosphorylates ArcA” (brown2023conservedmetabolicregulator pages 12-14) | Brown 2023 mBio, 10.1128/mbio.01448-23, https://doi.org/10.1128/mbio.01448-23 | High. |
| ArcA activation → represses → respiratory operons (e.g., nuo, shd/sdh) | A central part of facultative switching is reducing aerobic respiratory investment under low-ETC/low-O2 states. | ArcA “represses respiratory operons (nuo, shd)” (brown2023conservedmetabolicregulator pages 12-14); sdhC promoter is “repressed by phosphorylated ArcA” (yaeger2023centralmetabolismis pages 8-9) | Brown 2023 mBio, 10.1128/mbio.01448-23, https://doi.org/10.1128/mbio.01448-23; Yaeger 2023 PLOS Genet, 10.1371/journal.pgen.1011013, https://doi.org/10.1371/journal.pgen.1011013 | High for ArcA-positive Gram-negatives; exact target operons differ by taxon. |
| ArcA activation → promotes → fermentation | Fermentation provides ATP/redox balancing when respiration is impaired or O2 is unavailable. | ArcA “promotes a switch to fermentation when electron transport chain (ETC) activity or proton motive force (PMF) is disrupted” (brown2023conservedmetabolicregulator pages 12-14) | Brown 2023 mBio, 10.1128/mbio.01448-23, https://doi.org/10.1128/mbio.01448-23 | High in cited taxa; useful core TraitMech edge. |
| PMF disruption (e.g., CCCP) → activates → ArcA-mediated fermentation shift | PMF/ETC perturbation mimics respiratory limitation and drives facultative metabolic switching. | “Chemical uncoupling with CCCP… increased LDH and lactate/acetate production; some increases were ArcA-dependent” (brown2023conservedmetabolicregulator pages 12-14) | Brown 2023 mBio, 10.1128/mbio.01448-23, https://doi.org/10.1128/mbio.01448-23 | High for cited species; uncertain as universal mechanism outside ArcAB-bearing taxa. |
| ArcA-mediated fermentation shift → increases → lactate dehydrogenase activity and lactate/acetate production | Fermentative end products are measurable outputs of facultative switching. | CCCP “increased LDH and lactate/acetate production” (brown2023conservedmetabolicregulator pages 12-14) | Brown 2023 mBio, 10.1128/mbio.01448-23, https://doi.org/10.1128/mbio.01448-23 | High as phenotype readout; metabolite specifics vary among taxa. |
| Oxygen availability → increases → cytochrome bd oxidase activity | Cytochrome bd supports high-affinity O2 respiration at very low O2 and is a common facultative adaptation. | Under nanaerobic conditions, “both increased CydA protein and increased cytochrome bd activity” were observed (butler2023bacteroidesfragilismaintains pages 1-2) | Butler 2023 J Bacteriol, 10.1128/jb.00389-22, https://doi.org/10.1128/jb.00389-22 | High for Bacteroides fragilis; likely relevant broadly for low-O2 respiration, but taxon-specific implementation. |
| Oxygen presence (nanaerobic O2) → enables → cytochrome bd as terminal oxidase | Facultative cells can exploit trace oxygen as terminal electron acceptor without abandoning anaerobic capacity. | “which of these terminal enzymes is active in electron transfer depends on the availability of the final electron acceptor: fumarate or oxygen” (butler2023bacteroidesfragilismaintains pages 1-2) | Butler 2023 J Bacteriol, 10.1128/jb.00389-22, https://doi.org/10.1128/jb.00389-22 | High; strong direct support for electron-acceptor-dependent branch switching. |
| Fumarate availability → enables → fumarate reductase-dependent anaerobic respiration | Use of alternative terminal electron acceptors is a hallmark of facultative oxygen preference. | “Fumarate reductase and cytochrome bd are both present, and which of these terminal enzymes is active… depends on… fumarate or oxygen” (butler2023bacteroidesfragilismaintains pages 1-2) | Butler 2023 J Bacteriol, 10.1128/jb.00389-22, https://doi.org/10.1128/jb.00389-22 | High in B. fragilis; good candidate edge for facultative anaerobic respiration. |
| Concurrent synthesis of fumarate reductase and cytochrome bd → enables → rapid switching across fluctuating O2 | Pre-positioning both terminal pathways supports growth across oxygen regimes. | “The synthesis of cytochrome bd and fumarate reductase under both conditions serves as an adaptation to an environment with low oxygen concentrations” (butler2023bacteroidesfragilismaintains pages 1-2) | Butler 2023 J Bacteriol, 10.1128/jb.00389-22, https://doi.org/10.1128/jb.00389-22 | High, but especially relevant to nanaerobic gut-adapted taxa. |
| Nitrate (terminal electron acceptor) → promotes → anaerobic respiration | Nitrate can substitute for O2 as terminal electron acceptor, supporting non-fermentative growth under hypoxia/anoxia. | “addition of nitrate as a TEA promotes anaerobic respiration” (baker2024largininesupplementationabrogates pages 1-3); nitrate “suppressed biofilm stimulation in a dose-dependent manner” (yaeger2023centralmetabolismis pages 8-9) | Baker 2024 mSphere, 10.1128/msphere.00774-23, https://doi.org/10.1128/msphere.00774-23; Yaeger 2023 PLOS Genet, 10.1371/journal.pgen.1011013, https://doi.org/10.1371/journal.pgen.1011013 | High; broadly relevant across many facultative species with nitrate reductases. |
| Nitrate respiration → suppresses → fermentative / virulence-associated program | Providing an alternative TEA can shift cells away from fermentation-associated stress/virulence states. | Nitrate “promotes anaerobic respiration and suppresses the expression of S. aureus virulence factors” (baker2024largininesupplementationabrogates pages 1-3) | Baker 2024 mSphere, 10.1128/msphere.00774-23, https://doi.org/10.1128/msphere.00774-23 | Moderate; strong experimentally, but virulence linkage is species/context-specific. |
| Lack of terminal electron acceptor → activates → SrrAB and fermentative growth | When respiration is blocked, facultative cells can switch to fermentation through redox-responsive regulators. | “Lack of a TEA leads to impaired anaerobic respiration, accumulation of reduced menaquinone, and activation of the SrrAB… which drives fermentative growth” (baker2024largininesupplementationabrogates pages 1-3) | Baker 2024 mSphere, 10.1128/msphere.00774-23, https://doi.org/10.1128/msphere.00774-23 | Moderate; mechanistically strong but centered on S. aureus, not ArcA/FNR systems. |
| Oxygen exposure → induces → distinct O2-reductases by O2 range | Oxygen tolerance/survival across gradients can be partitioned among enzymes tuned to different O2 levels. | “revRbr2 is specific to low O2 tensions (<0.4%), FdpA to low and intermediate O2 tensions (0.4%–1%), revRbr1… (0.1%–4%), and finally FdpF… >4% and air” (caulat2024physiologicalroleand pages 1-2) | Caulat 2024 mBio, 10.1128/mbio.01591-24, https://doi.org/10.1128/mbio.01591-24 | Moderate for this trait: important boundary/warning because this is obligate anaerobe O2 tolerance, not facultative growth per se. |
| Oxygen exposure → induces → Spx-family regulator-dependent O2 defense genes | Oxidative stress defense modules help some microbes endure transient oxygen exposure. | “a regulator of the Spx family… plays a role in the induction of fdp and revrbr genes upon O2 exposure” (caulat2024physiologicalroleand pages 1-2) | Caulat 2024 mBio, 10.1128/mbio.01591-24, https://doi.org/10.1128/mbio.01591-24 | Moderate; useful for boundary cases, but not sufficient alone to define facultative oxygen preference. |
| Oxygen exposure → forms → MtrC disulfide that lowers FMN affinity | At oxic/anoxic interfaces, extracellular electron transfer machinery is tuned to avoid harmful O2 reduction. | “In the presence of oxygen, the disulfide forms, lowering the affinity for FMN and decreasing the rate of peroxide formation” (from Norman abstract in conversation) | Norman 2023 mBio, 10.1128/mbio.02589-22, https://doi.org/10.1128/mbio.02589-22 | Moderate; highly mechanistic and relevant to transition survival, but specific to Shewanella EET. |
| MtrC disulfide formation → decreases → peroxide formation / ROS damage | Oxygen-responsive protein chemistry can protect facultative cells during rapid oxic transitions. | “lowering the affinity for FMN and decreasing the rate of peroxide formation… allows the cell to respond to changes in oxygen level and survive” (Norman abstract in conversation) | Norman 2023 mBio, 10.1128/mbio.02589-22, https://doi.org/10.1128/mbio.02589-22 | Moderate; niche-specific to oxic/anoxic interface behavior. |
| Aerobic conditions → upregulate → respiratory chain modules (NDH-I, SDH/FDR, cytochrome bd, ATP synthase) | Facultative growth with O2 often involves induction of ETC components and TCA-linked respiration. | “a tentative aerobic electron transport chain includes ‘NADH dehydrogenase/complex I (NDH-I), succinate dehydrogenase/fumarate reductase (SDH/FDR), cytochrome bd complex (CytBD), and ATP synthase’” (loivamaa2024aerobicadaptationand pages 9-12) | Loivamaa 2024 mSystems, 10.1128/msystems.00615-24, https://doi.org/10.1128/msystems.00615-24 | Moderate-high; organism-specific but captures a plausible node set for facultative aerobic growth. |
| Anaerobic conditions → upregulate → nitrate/DMSO reductase modules | Alternative electron acceptors support growth when O2 is absent. | “Putative membrane spanning structures of nitrate and DMSO reductases possibly involved in anaerobic respiration are shown” and narG was “upregulated anaerobic” (loivamaa2024aerobicadaptationand pages 18-20, loivamaa2024aerobicadaptationand pages 9-12) | Loivamaa 2024 mSystems, 10.1128/msystems.00615-24, https://doi.org/10.1128/msystems.00615-24 | Moderate; good candidate edge, but current evidence is from one actinobacterial species. |


*Table: This table compiles evidence-backed candidate subject–predicate–object edges for curating a TraitMech causal graph of facultative oxygen preference. It emphasizes broadly reusable switching mechanisms while flagging taxon-specific or boundary-case claims.*

---

## Ontology grounding suggestions (CURIE-first; label when uncertain)

**Chemicals (CHEBI):**
- O2: CHEBI:15379
- Nitrate: CHEBI:17632
- Fumarate: CHEBI:18012
- Menaquinone: CHEBI:16389
- NADH: CHEBI:16908
- FMN: CHEBI:17621
- Lactate: CHEBI:24996
- Acetate: CHEBI:30089
- Hydrogen peroxide: CHEBI:16240

**Processes (GO):**
- Aerobic respiration: GO:0009060
- Anaerobic respiration: GO:0009061
- Fermentation: GO:0006113
- Response to oxygen levels: GO:0070482

**Enzymes (EC; use as node grounding where helpful):**
- Fumarate reductase: EC 1.3.5.4
- D-lactate dehydrogenase: EC 1.1.1.28
- NADH dehydrogenase I (complex I): EC 7.1.1.2
- Nitrate reductase (NarGHI; quinol/nitrate oxidoreductase): EC 7.2.2.1
- Cytochrome bd oxidase: EC varies by naming/annotation across resources; recommend using a label node + GO term (e.g., “cytochrome-bd ubiquinol oxidase activity”) during curation.

**Environments (ENVO; suggest candidate nodes, verify exact term IDs during curation):**
- Intestine / gut epithelium oxygen gradients: use ENVO anatomical environment terms or UBERON where appropriate; if ENVO IDs are uncertain, retain label nodes and map later. (butler2023bacteroidesfragilismaintains pages 1-2, caulat2024physiologicalroleand pages 1-2)

---

## Warnings / claims not ready for curation without additional taxon-specific support

1. **Do not curate oxygen-tolerance enzymes of obligate anaerobes as direct evidence of facultative oxygen preference** unless growth-with-and-without-O2 is demonstrated. The *C. difficile* O2-reductase network is best curated under an “oxygen tolerance” or “response to oxygen/oxidative stress” trait boundary, not the facultative growth trait. (caulat2024physiologicalroleand pages 1-2)

2. **Virulence modulation by nitrate is context- and taxon-specific**: the nitrate→respiration→virulence suppression edge is strong for *S. aureus* in the DFU-like model but should be marked as pathogen-context dependent if used in a general facultative oxygen preference graph. (baker2024largininesupplementationabrogates pages 1-3)

3. **Phage replication effects under anaerobiosis** are highly system-dependent (host strain, phage, media, oxygen control). These are valuable for an “oxygen regime modulates phage infection outcomes” subgraph but should be curated with assay context. (villamizar2023anaerobiosisaneglected pages 13-16)

---

## DOI-first bibliography (with dates and URLs)

1. Butler NL, Ito T, Foreman S, et al. *Bacteroides fragilis* Maintains Concurrent Capability for Anaerobic and Nanaerobic Respiration. **Journal of Bacteriology**. **Jan 2023**. DOI: **10.1128/jb.00389-22**. URL: https://doi.org/10.1128/jb.00389-22 (butler2023bacteroidesfragilismaintains pages 1-2)

2. Brown AN, Anderson MT, Smith SN, Bachman MA, Mobley HLT. Conserved metabolic regulator ArcA responds to oxygen availability, iron limitation, and cell envelope perturbations during bacteremia. **mBio**. **Oct 2023**. DOI: **10.1128/mbio.01448-23**. URL: https://doi.org/10.1128/mbio.01448-23 (brown2023conservedmetabolicregulator pages 1-3, brown2023conservedmetabolicregulator pages 12-14)

3. Villamizar SH, Cárdenas LAC, Mancera LTM, Florez MJV. Anaerobiosis, a neglected factor in phage-bacteria interactions. **Applied and Environmental Microbiology**. **Dec 2023**. DOI: **10.1128/aem.01491-23**. URL: https://doi.org/10.1128/aem.01491-23 (villamizar2023anaerobiosisaneglected pages 13-16, villamizar2023anaerobiosisaneglected pages 11-13)

4. Yaeger LN, French S, Brown ED, Côté JP, Burrows LL. Central metabolism is a key player in *E. coli* biofilm stimulation by sub-MIC antibiotics. **PLOS Genetics**. **Nov 2023**. DOI: **10.1371/journal.pgen.1011013**. URL: https://doi.org/10.1371/journal.pgen.1011013 (yaeger2023centralmetabolismis pages 8-9)

5. Baker CL, Seo KS, Park N, et al. L-arginine supplementation abrogates hypoxia-induced virulence of *Staphylococcus aureus* in a murine diabetic pressure wound model. **mSphere**. **Mar 2024**. DOI: **10.1128/msphere.00774-23**. URL: https://doi.org/10.1128/msphere.00774-23 (baker2024largininesupplementationabrogates pages 1-3)

6. Loivamaa I, Sillanpää A, Deptula P, et al. Aerobic adaptation and metabolic dynamics of *Propionibacterium freudenreichii* DSM 20271: insights from comparative transcriptomics and surfaceome analysis. **mSystems**. **Oct 2024**. DOI: **10.1128/msystems.00615-24**. URL: https://doi.org/10.1128/msystems.00615-24 (loivamaa2024aerobicadaptationand pages 9-12, loivamaa2024aerobicadaptationand pages 6-9)

7. Caulat LC, Lotoux A, Martins MC, et al. Physiological role and complex regulation of O2-reducing enzymes in the obligate anaerobe *Clostridioides difficile*. **mBio**. **Oct 2024**. DOI: **10.1128/mbio.01591-24**. URL: https://doi.org/10.1128/mbio.01591-24 (caulat2024physiologicalroleand pages 1-2)


References

1. (brown2023conservedmetabolicregulator pages 1-3): Aric N. Brown, Mark T. Anderson, Sara N. Smith, Michael A. Bachman, and Harry L. T. Mobley. Conserved metabolic regulator arca responds to oxygen availability, iron limitation, and cell envelope perturbations during bacteremia. Oct 2023. URL: https://doi.org/10.1128/mbio.01448-23, doi:10.1128/mbio.01448-23. This article has 11 citations and is from a domain leading peer-reviewed journal.

2. (brown2023conservedmetabolicregulator pages 12-14): Aric N. Brown, Mark T. Anderson, Sara N. Smith, Michael A. Bachman, and Harry L. T. Mobley. Conserved metabolic regulator arca responds to oxygen availability, iron limitation, and cell envelope perturbations during bacteremia. Oct 2023. URL: https://doi.org/10.1128/mbio.01448-23, doi:10.1128/mbio.01448-23. This article has 11 citations and is from a domain leading peer-reviewed journal.

3. (butler2023bacteroidesfragilismaintains pages 1-2): Nicole L. Butler, Takeshi Ito, Sara Foreman, Joel E. Morgan, Dmitry Zagorevsky, Michael H. Malamy, Laurie E. Comstock, and Blanca Barquera. <i>bacteroides fragilis</i> maintains concurrent capability for anaerobic and nanaerobic respiration. Journal of Bacteriology, Jan 2023. URL: https://doi.org/10.1128/jb.00389-22, doi:10.1128/jb.00389-22. This article has 24 citations and is from a peer-reviewed journal.

4. (caulat2024physiologicalroleand pages 1-2): Léo C. Caulat, Aurélie Lotoux, M. C. Martins, Nicolas Kint, Cyril Anjou, Miguel Sepúlveda Teixeira, Filipe Folgosa, C. Morvan, and Isabelle Martin-Verstraete. Physiological role and complex regulation of o <sub>2</sub> -reducing enzymes in the obligate anaerobe <i>clostridioides difficile</i>. Oct 2024. URL: https://doi.org/10.1128/mbio.01591-24, doi:10.1128/mbio.01591-24. This article has 8 citations and is from a domain leading peer-reviewed journal.

5. (loivamaa2024aerobicadaptationand pages 9-12): Iida Loivamaa, Annika Sillanpää, Paulina Deptula, Bhawani Chamlagain, Minnamari Edelmann, Petri Auvinen, Tuula A. Nyman, Kirsi Savijoki, Vieno Piironen, and Pekka Varmanen. Aerobic adaptation and metabolic dynamics of <i>propionibacterium freudenreichii</i> dsm 20271: insights from comparative transcriptomics and surfaceome analysis. Oct 2024. URL: https://doi.org/10.1128/msystems.00615-24, doi:10.1128/msystems.00615-24. This article has 5 citations and is from a peer-reviewed journal.

6. (loivamaa2024aerobicadaptationand pages 6-9): Iida Loivamaa, Annika Sillanpää, Paulina Deptula, Bhawani Chamlagain, Minnamari Edelmann, Petri Auvinen, Tuula A. Nyman, Kirsi Savijoki, Vieno Piironen, and Pekka Varmanen. Aerobic adaptation and metabolic dynamics of <i>propionibacterium freudenreichii</i> dsm 20271: insights from comparative transcriptomics and surfaceome analysis. Oct 2024. URL: https://doi.org/10.1128/msystems.00615-24, doi:10.1128/msystems.00615-24. This article has 5 citations and is from a peer-reviewed journal.

7. (villamizar2023anaerobiosisaneglected pages 13-16): Santiago Hernández Villamizar, Luis A. Chica Cárdenas, Laura T. Morales Mancera, and Martha J. Vives Florez. Anaerobiosis, a neglected factor in phage-bacteria interactions. Dec 2023. URL: https://doi.org/10.1128/aem.01491-23, doi:10.1128/aem.01491-23. This article has 10 citations and is from a peer-reviewed journal.

8. (villamizar2023anaerobiosisaneglected pages 11-13): Santiago Hernández Villamizar, Luis A. Chica Cárdenas, Laura T. Morales Mancera, and Martha J. Vives Florez. Anaerobiosis, a neglected factor in phage-bacteria interactions. Dec 2023. URL: https://doi.org/10.1128/aem.01491-23, doi:10.1128/aem.01491-23. This article has 10 citations and is from a peer-reviewed journal.

9. (baker2024largininesupplementationabrogates pages 1-3): Carol L. Baker, Keun Seok Seo, Nogi Park, Jaime K. Rutter, Justin A. Thornton, Stephen B. Pruett, and Joo Youn Park. L-arginine supplementation abrogates hypoxia-induced virulence of <i>staphylococcus aureus</i> in a murine diabetic pressure wound model. mSphere, Mar 2024. URL: https://doi.org/10.1128/msphere.00774-23, doi:10.1128/msphere.00774-23. This article has 5 citations and is from a peer-reviewed journal.

10. (yaeger2023centralmetabolismis pages 8-9): Luke N. Yaeger, Shawn French, Eric D. Brown, Jean Philippe Côté, and Lori L. Burrows. Central metabolism is a key player in e. coli biofilm stimulation by sub-mic antibiotics. PLOS Genetics, 19:e1011013, Nov 2023. URL: https://doi.org/10.1371/journal.pgen.1011013, doi:10.1371/journal.pgen.1011013. This article has 15 citations and is from a domain leading peer-reviewed journal.

11. (loivamaa2024aerobicadaptationand pages 18-20): Iida Loivamaa, Annika Sillanpää, Paulina Deptula, Bhawani Chamlagain, Minnamari Edelmann, Petri Auvinen, Tuula A. Nyman, Kirsi Savijoki, Vieno Piironen, and Pekka Varmanen. Aerobic adaptation and metabolic dynamics of <i>propionibacterium freudenreichii</i> dsm 20271: insights from comparative transcriptomics and surfaceome analysis. Oct 2024. URL: https://doi.org/10.1128/msystems.00615-24, doi:10.1128/msystems.00615-24. This article has 5 citations and is from a peer-reviewed journal.