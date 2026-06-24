---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T00:46:11.248357'
end_time: '2026-06-18T01:08:26.663202'
duration_seconds: 1335.41
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: pH range mid1
  trait_identifier: METPO:1000461
  trait_category: ENVIRONMENT
  trait_category_slug: environment
  trait_slug: ph_range_mid1
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: "A pH range phenotype in which the growth-supporting external pH range\
    \ spans approximately 6\u20137, characteristic of neutrophilic physiology."
  parent_traits: METPO:1000332
  synonyms: Alkali Tolerant, Facultative acidophile, Neutrophile, pHR_6_to_7
  evidence_summary: 'DOI:10.1038/nrmicro2549: cytoplasmic pH (pH-homeostasis review
    supports near-neutral cytoplasmic pH at near-neutral external pH as the neutrophilic
    regime.)'
  causal_graph_summary: 'ph_range_mid1_neutrophile_range: 3 nodes, 2 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 39
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH range mid1
- **METPO identifier:** METPO:1000461
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH range phenotype in which the growth-supporting external pH range spans approximately 6–7, characteristic of neutrophilic physiology.
- **Parent traits:** METPO:1000332
- **Synonyms:** Alkali Tolerant, Facultative acidophile, Neutrophile, pHR_6_to_7
- **Existing evidence:** DOI:10.1038/nrmicro2549: cytoplasmic pH (pH-homeostasis review supports near-neutral cytoplasmic pH at near-neutral external pH as the neutrophilic regime.)
- **Existing causal graph summary:** ph_range_mid1_neutrophile_range: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **pH range mid1** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_range_mid1.yaml`.

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
- **Trait label:** pH range mid1
- **METPO identifier:** METPO:1000461
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH range phenotype in which the growth-supporting external pH range spans approximately 6–7, characteristic of neutrophilic physiology.
- **Parent traits:** METPO:1000332
- **Synonyms:** Alkali Tolerant, Facultative acidophile, Neutrophile, pHR_6_to_7
- **Existing evidence:** DOI:10.1038/nrmicro2549: cytoplasmic pH (pH-homeostasis review supports near-neutral cytoplasmic pH at near-neutral external pH as the neutrophilic regime.)
- **Existing causal graph summary:** ph_range_mid1_neutrophile_range: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **pH range mid1** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_range_mid1.yaml`.

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


## Microbial Trait Causal Graph Research Report: pH range mid1 (METPO:1000461)

### Executive scope summary
The trait **pH range mid1** (METPO:1000461) is best interpreted as a **growth-supporting external pH range centered on mildly acidic to neutral conditions (~pH 6–7)**, characteristic of **neutrophilic/neutralophilic physiology**. A key mechanistic hallmark is **tight intracellular (cytoplasmic) pH homeostasis near neutrality** even when external pH varies; for many neutralophiles, growth can extend beyond the midrange (approx. pH 5.5–9.0) while maintaining cytoplasmic pH in a narrow band (~7.5–7.7). (krulwich2011molecularaspectsof pages 1-3)

This trait should be distinguished from:
- **Acidophily** (growth optimum and/or growth-supporting range predominantly ≤pH 5) and **alkaliphily** (optimum and/or growth-supporting range ≥pH 9), where additional specialized mechanisms (e.g., Mrp-dependent pH homeostasis at high pH) may be indispensable. (krulwich2011molecularaspectsof pages 12-14)
- **pH preference as realized niche** (maximum abundance along environmental gradients) vs. **in vitro growth optima/ranges**. Ramoneda et al. operationalize “pH preference” as a realized niche estimate rather than a pure physiological optimum, which matters for curating evidence types into TraitMech. (ramoneda2023buildingagenomebased pages 1-2)

### 1) Key concepts and definitions (current understanding)

#### 1.1 Neutralophile growth range and cytoplasmic pH homeostasis
A canonical synthesis (Krulwich, Sachs & Padan, 2011) emphasizes that **neutralophiles can grow across a broad external pH window (~5.5–9.0) yet maintain cytoplasmic pH in a comparatively narrow interval (~7.5–7.7)**, implying active homeostatic control rather than passive equilibration with the environment. (krulwich2011molecularaspectsof pages 1-3)

#### 1.2 Proton motive force (PMF) as a central organizing concept
pH homeostasis is coupled to the **proton motive force (PMF)**, which includes **ΔpH** and **Δψ** components and is generated by primary proton pumps (e.g., respiratory chain complexes) and proton-pumping ATPases. (krulwich2011molecularaspectsof pages 1-3, krulwich2011molecularaspectsof pages 3-5)

### 2) Recent developments and latest research (priority 2023–2024)

#### 2.1 Genome-based inference of bacterial pH preferences (environmental “realized niche”)
Ramoneda et al. (2023, Science Advances) compiled distributions across **five soil and freshwater datasets totaling 1,470 samples** to estimate taxon pH preferences from maximum abundance across gradients, and linked these preferences to genomic features via a machine-learning approach. (ramoneda2023buildingagenomebased pages 1-1, ramoneda2023buildingagenomebased pages 2-3)

Key mechanistic gene categories associated with pH preference include **ion transporters/antiporters and ATPases**. (ramoneda2023buildingagenomebased pages 6-7)

#### 2.2 Electrophysiological framing of pH homeostasis in a neutrophile (E. coli)
Terradot et al. (2024, PRX Life) propose a systems view in which **PMF strength and specific proton-ion antiporters jointly determine the external pH range over which both pH homeostasis and membrane potential are maintained**. They report that **“decreasing the PMF's strength impairs the cells' ability to maintain pH”** and connect this to measured PMF and pH in single cells. (terradot2024escherichiacolimaintains pages 1-2)

They also predict distinct operating pH regimes for antiporter “types” (ClcA-like, NhaB-like, NhaA-like), offering a modular way to represent pH-range boundaries in a causal graph. (terradot2024escherichiacolimaintains pages 8-9)

#### 2.3 Biofilm-level active extracellular pH regulation in minimally buffered environments
Tran et al. (2024, mBio) report that *Bacillus subtilis* biofilms can **“modulate their extracellular pH to the preferred neutrophile range… even when starting from acidic and alkaline initial conditions”**, associating this with a **dynamic interplay between acetate and acetoin biosynthesis** that buffers against biofilm acidification. (tran2024activephregulation pages 1-2)

#### 2.4 pH-driven adaptation in host niches (boundary case informing general principles)
Dechow & Abramovitch (2024) summarize that *Mycobacterium tuberculosis* can maintain **intrabacterial pH near ~7.2 even at external pH 4.5**, and that carbon source selection and anaplerotic remodeling influence growth at acidic pH; this is best treated as a boundary/contrast case for the mid1 trait (mechanistic principle: cytoplasmic neutrality under stress). (dechow2024targetingmycobacteriumtuberculosis pages 1-2)

### 3) Current applications and real-world implementations

1. **Cultivation and inoculant selection / predictive ecology:** Genome-based prediction of pH preferences can aid “selection of microbial inoculants,” improve species distribution models, and guide cultivation strategies. (ramoneda2023buildingagenomebased pages 1-2)
2. **Biofilm control in natural or industrial settings:** Mechanisms enabling biofilms to buffer toward neutrophile pH may represent targets to control unwanted biofilm growth outside buffered laboratory media. (tran2024activephregulation pages 1-2)
3. **Environmental monitoring and management:** In polluted paddy soils, random forest and regression analyses identify soil pH as a dominant driver—“the most important predictor of bacterial diversity.” (zou2024impactsofmultiple pages 1-2)
4. **Global biogeography of growth potential:** A global analysis of **176 soil metagenomes across 11 biomes and six continents** links bacterial growth potential patterns to environmental predictors including pH. (osburn2024globalpatternsin pages 1-2)

### 4) Expert opinions and authoritative synthesis

The Krulwich et al. Nature Reviews Microbiology review (2011; highly cited) provides a widely used conceptual framework: neutralophiles integrate **PMF management, transporter activity (especially cation/proton antiporters), respiratory chain modulation, ATP synthase regulation, and metabolic proton-consuming reactions** to maintain cytoplasmic pH within a narrow range despite external variation. (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 1-3)

A useful mechanistic schematic summarizing key modules (acid challenge vs. alkali challenge; GadB/GadC; NhaA; respiratory complexes; ATP synthase) is provided in the review’s Figure 1 (cropped region retrieved). (krulwich2011molecularaspectsof media 86e3a035)

### 5) Relevant statistics and quantitative data points

- **Neutralophile external growth range:** ~**pH 5.5–9.0**; **cytoplasmic pH** typically near **~7.5–7.7**. (krulwich2011molecularaspectsof pages 1-3)
- **Ramoneda et al. 2023 dataset size:** **1,470 environmental samples** across five datasets used to infer realized pH preferences. (ramoneda2023buildingagenomebased pages 1-1)
- **Osburn et al. 2024 global metagenomes:** **176 soil metagenomes**, **11 terrestrial biomes**, **six continents**. (osburn2024globalpatternsin pages 1-2)
- **Salt-affected soils context (important confounder for environmental pH effects):** cited global areas include **424 million ha surface** and **833 million ha subsurface** salt-affected soils; **85% of surface salt-affected soils** described as saline (context for distinguishing pH vs EC drivers). (mucsi2024responseofthe pages 1-2)

---

## Trait scope (curation-oriented)

### Phenotype interpretation for METPO:1000461
- **Phenotype:** Growth-supporting external pH range spans ~6–7 (midrange), consistent with neutrophilic physiology.
- **Assay/measurement:** Often derived from growth curves in defined media across pH; in environmental ecology, “pH preference” may be inferred from abundance maxima along gradients (realized niche). (ramoneda2023buildingagenomebased pages 1-2)

### Boundary cases to flag in curation
- **Broad-range neutralophiles:** Many “neutralophiles” grow beyond 6–7 (e.g., ~5.5–9.0) and therefore may require a separate trait for “broad pH tolerance,” while mid1 captures the canonical regime. (krulwich2011molecularaspectsof pages 1-3)
- **Biofilm vs planktonic:** Biofilms can actively regulate extracellular pH in ways planktonic cells cannot; trait assignment may be assay-specific. (tran2024activephregulation pages 1-2)
- **Pathogen niche pH vs laboratory pH:** Host niche adaptation (e.g., phagosomes) should be tagged as context-specific rather than generalized mid1 physiology. (dechow2024targetingmycobacteriumtuberculosis pages 1-2)

---

## Candidate causal-graph nodes (grouped by type)

### A) Environmental and experimental factors
- External pH (ENVO term label: environmental pH)
- Medium buffering capacity / minimally buffered vs buffered media (context variable for assays) (tran2024activephregulation pages 1-2)
- Oxygen availability (affects PMF; collapse impairs pH maintenance) (terradot2024escherichiacolimaintains pages 4-5)
- Carbon source identity (glycolytic vs anaplerotic substrates; host context) (dechow2024targetingmycobacteriumtuberculosis pages 1-2)
- Soil pH and covarying soil properties (CEC, EC/salinity, metals, texture) (zou2024impactsofmultiple pages 1-2, mucsi2024responseofthe pages 1-2)

### B) Cellular processes and physiological state
- Cytoplasmic pH homeostasis (label)
- Proton motive force (PMF), membrane potential (Δψ), transmembrane ΔpH (labels) (krulwich2011molecularaspectsof pages 1-3, terradot2024escherichiacolimaintains pages 1-2)
- Overflow metabolism / acidification in dense communities (biofilms) (tran2024activephregulation pages 1-2)

### C) Transporters and bioenergetic complexes
- F1Fo-ATP synthase / F1Fo-ATPase (GO:0045259; operational mode synthesis vs hydrolysis) (krulwich2011molecularaspectsof pages 5-6)
- Na+/H+ antiporters (e.g., NhaA; broader families MrpF/MnhG/PhaGF/YufB in comparative genomics) (krulwich2011molecularaspectsof pages 5-6, ramoneda2023buildingagenomebased pages 3-5)
- Mrp antiporter complex (alkaliphile boundary mechanism) (krulwich2011molecularaspectsof pages 12-14)
- Kdp K+ transporters (KdpACD; association with low-pH preference) (ramoneda2023buildingagenomebased pages 3-5)

### D) Metabolic modules and metabolites
- Glutamate decarboxylation / GABA system (CHEBI:16865 glutamate; CHEBI:16867 GABA) (krulwich2011molecularaspectsof pages 5-6)
- Hydrogenase-3 mediated proton consumption (label) (krulwich2011molecularaspectsof pages 5-6)
- Acetate (CHEBI:15366) and acetoin (CHEBI:15343) biosynthesis interplay (biofilm pH buffering) (tran2024activephregulation pages 1-2)

### E) Regulatory systems (labels; grounding often organism-specific)
- Two-component systems in pH adaptation (label) (krulwich2011molecularaspectsof pages 14-15)
- GadE (acid resistance regulator) (krulwich2011molecularaspectsof pages 17-18)

---

## Candidate causal edges (evidence-backed)

| Edge (Subject–Predicate–Object) | Suggested node grounding (CURIEs where possible) | Evidence (paper + year + DOI/URL) | Supporting snippet (short, verbatim-ish) | Notes/uncertainty |
|---|---|---|---|---|
| proton motive force (PMF) → enables → cytoplasmic pH homeostasis | GO:0015992 proton transport; GO:0006754 ATP biosynthetic process; label: proton motive force; label: cytoplasmic pH homeostasis | Terradot et al. 2024, *PRX Life*, DOI:10.1103/PRXLife.2.043015, https://doi.org/10.1103/PRXLife.2.043015 | “decreasing the PMF's strength impairs the cells' ability to maintain pH” (terradot2024escherichiacolimaintains pages 1-2, terradot2024escherichiacolimaintains pages 8-9) | Strong mechanistic edge for neutrophiles such as *E. coli*; broadly applicable but shown in a model organism. |
| ClcA-like/NhaB-like/NhaA-like proton antiporters → determine extracellular pH range for maintaining pHi ≈7 | label: ClcA-like antiporter; label: NhaB-like antiporter; label: NhaA-like Na+/H+ antiporter; GO:0006885 regulation of pH | Terradot et al. 2024, *PRX Life*, DOI:10.1103/PRXLife.2.043015, https://doi.org/10.1103/PRXLife.2.043015 | “ClcA-like ~pHe 2–5, NhaB-like ~5–9, and NhaA-like ~9–12” (terradot2024escherichiacolimaintains pages 8-9) | Useful as a candidate graph module linking transporter repertoire to pH-range boundaries; transporter labels may need organism-specific grounding. |
| NhaA Na+/H+ antiporter → supports proton entry at alkaline pH via electrogenic 2H+/1Na+ stoichiometry | label: NhaA; GO:0015385 sodium:proton antiporter activity | Krulwich et al. 2011, *Nat Rev Microbiol*, DOI:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549 | “stoichiometry for *E. coli* NhaA is 2H+/1Na+, enabling Δψ-driven proton entry” (krulwich2011molecularaspectsof pages 5-6) | Strong mechanistic contrast edge for alkaline side of neutralophile range; specific to NhaA-family systems. |
| GadB glutamate decarboxylase system (with GABA export) → consumes cytoplasmic protons → acid survival | label: GadB; label: GadC/GABA antiporter; CHEBI:16865 glutamate; CHEBI:16867 4-aminobutyric acid | Krulwich et al. 2011, *Nat Rev Microbiol*, DOI:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549 | “GadB-linked glutamate decarboxylation consume[s] cytoplasmic protons to support survival at very low pH” (krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof pages 15-17) | Strong acid-stress/survival mechanism, but more relevant to boundary tolerance below the trait’s core pH 6–7 than to optimal mid-range growth. |
| acid challenge → upregulates proton-pumping respiratory complexes / downregulates proton-importing ATP synthase → supports pH homeostasis | GO:0015992 proton transport; label: respiratory proton-pumping complexes; label: F1Fo-ATP synthase | Krulwich et al. 2011, *Nat Rev Microbiol*, DOI:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549 | “under acid challenge *E. coli* up-regulates proton-pumping respiratory complexes and down-regulates ATP synthase” (krulwich2011molecularaspectsof pages 5-6) | Good regulatory edge for neutralophile response to acidic excursions; review-backed rather than single-gene perturbation. |
| alkaline challenge → upregulates cation/proton antiporters and F1Fo-ATP synthase proton-capture functions → supports pH homeostasis | label: cation/proton antiporters; label: F1Fo-ATP synthase | Krulwich et al. 2011, *Nat Rev Microbiol*, DOI:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549 | “Under alkaline stress cells activate inward proton transport via… cation/proton antiporters… and increase F1Fo ATP synthase expression to enhance proton capture” (krulwich2011molecularaspectsof pages 5-6) | Relevant to upper boundary of neutralophile range and transition toward alkali tolerance. |
| Mrp Na+/H+ antiporter complex → required for alkaliphile pH homeostasis | label: Mrp antiporter complex; GO:0015385 sodium:proton antiporter activity | Krulwich et al. 2011, *Nat Rev Microbiol*, DOI:10.1038/nrmicro2549, https://doi.org/10.1038/nrmicro2549 | “Mrp antiporter being indispensable at high pH; all Mrp subunits are required” (krulwich2011molecularaspectsof pages 12-14, krulwich2011molecularaspectsof pages 20-22) | Contrast/boundary edge: important for distinguishing mid1 neutrophiles from true alkaliphiles; should be marked non-core/contrast for this trait. |
| Kdp K+ transporters (KdpACD) → associated with → low-pH preference taxa | label: KdpA/KdpC/KdpD family; GO:0015079 potassium ion transmembrane transporter activity | Ramoneda et al. 2023, *Science Advances*, DOI:10.1126/sciadv.adf8998, https://doi.org/10.1126/sciadv.adf8998 | “Kdp K+ membrane transporters (KdpACD) were overrepresented in taxa with low pH preference” (ramoneda2023buildingagenomebased pages 3-5) | Association edge from comparative genomics/ecology, not direct causal perturbation; useful but should be curated as statistical association/uncertain. |
| Na+/H+ antiporter gene families (MrpF/MnhG/PhaGF/YufB) → associated with → higher-pH preference taxa | label: MrpF; label: MnhG; label: PhaGF; label: YufB; GO:0015385 sodium:proton antiporter activity | Ramoneda et al. 2023, *Science Advances*, DOI:10.1126/sciadv.adf8998, https://doi.org/10.1126/sciadv.adf8998 | “Na+/H+ antiporters (PhaGF, MnhG, MrpF, YufB)… were overrepresented in taxa preferring higher pH” (ramoneda2023buildingagenomebased pages 3-5) | Statistical association across habitats; supports pH-range boundary mechanisms but not specific to pH 6–7 alone. |
| acetate and acetoin biosynthesis interplay → buffers extracellular pH → preferred neutrophile range in *B. subtilis* biofilms | label: acetate biosynthesis; label: acetoin biosynthesis; CHEBI:15366 acetate; CHEBI:15343 acetoin; NCBITaxon:1423 | Tran et al. 2024, *mBio*, DOI:10.1128/mbio.03387-23, https://doi.org/10.1128/mbio.03387-23 | “modulate their extracellular pH to the preferred neutrophile range… associate this behavior with dynamic interplay between acetate and acetoin biosynthesis” (tran2024activephregulation pages 1-2) | Strong, recent, phenotype-proximal edge; probably biofilm- and medium-buffering-specific, so mark context-specific. |
| anaplerotic substrates / carbon-source choice → enables growth at acidic pH and maintenance of intrabacterial pH ~7.2 at pH 4.5 in *M. tuberculosis* | label: anaplerosis; label: phosphoenolpyruvate; CHEBI:32816 pyruvate; CHEBI:30089 acetate; label: oxaloacetate; CHEBI:16113 cholesterol; label: pckA; label: icl; NCBITaxon:1773 | Dechow & Abramovitch 2024, *Microbiology*, DOI:10.1099/mic.0.001458, https://doi.org/10.1099/mic.0.001458 | “intrabacterial pH maintained near ~7.2 even at external pH 4.5” and “anaplerotic-node substrates… permit growth at acidic pH” (dechow2024targetingmycobacteriumtuberculosis pages 1-2) | Important boundary-case mechanism showing neutrality of cytoplasm despite acidic environment; pathogen-specific and outside core pH 6–7, so curate cautiously. |
| soil pH → is most important predictor of → bacterial diversity | ENVO:00001998 soil; label: soil pH; label: bacterial diversity | Zou et al. 2024, *Scientific Reports*, DOI:10.1038/s41598-024-65678-x, https://doi.org/10.1038/s41598-024-65678-x | “soil pH was the most important predictor of bacterial diversity” (zou2024impactsofmultiple pages 1-2) | Application/ecology edge rather than intracellular mechanism; useful for trait relevance and environmental deployment. |
| soil pH and productivity indicators → predict → global soil bacterial growth potential | ENVO:00001998 soil; label: soil pH; label: bacterial growth potential | Osburn et al. 2024, *Nature Communications*, DOI:10.1038/s41467-024-50382-1, https://doi.org/10.1038/s41467-024-50382-1 | “the strongest environmental predictors of growth potential… explicitly including pH” (osburn2024globalpatternsin pages 1-2) | Ecological/application edge at community scale; not a direct TraitMech intracellular mechanism, but useful context for real-world implementation. |


*Table: This table summarizes candidate causal edges relevant to the neutrophilic pH range mid1 trait, combining direct mechanistic evidence, boundary-case contrasts, and ecological/application-scale associations. It is intended to support TraitMech curation by separating stronger mechanistic edges from broader comparative or context-specific claims.*

Additionally, a mechanism summary diagram (useful for curator cross-checking of modules) is available from the Krulwich et al. review figure crop. (krulwich2011molecularaspectsof media 86e3a035)

---

## Warnings / curation notes (do not curate yet or curate as uncertain)

1. **Association vs causality:** Many gene–pH links from comparative ecology/genomics (e.g., KdpACD association with low-pH preference) are **statistical associations**, not direct perturbation evidence; represent as **“associated_with”** edges or mark as **UNCERTAIN** if TraitMech expects causal direction. (ramoneda2023buildingagenomebased pages 3-5)
2. **Biofilm-specific regulation:** The acetate/acetoin extracellular pH buffering mechanism is compelling but may be **biofilm- and medium-buffering-dependent**; curate with explicit context tags (biofilm; minimally buffered media). (tran2024activephregulation pages 1-2)
3. **Pathogen host-niche adaptation:** *M. tuberculosis* acidic pH adaptation is informative but not necessarily representative of general neutrophiles; curate only if you explicitly model “acid challenge in host phagosome” as a context node. (dechow2024targetingmycobacteriumtuberculosis pages 1-2)
4. **Alkaliphile mechanisms:** Mrp antiporter and alkaliphile ATP synthase motifs are more appropriate for **alkaliphily traits** than mid1; treat as boundary/contrast. (krulwich2011molecularaspectsof pages 12-14)

---

## DOI-first bibliography (with URLs and publication dates)

1. **Krulwich TA, Sachs G, Padan E.** *Molecular aspects of bacterial pH sensing and homeostasis.* **Nature Reviews Microbiology**. **May 2011**. DOI: **10.1038/nrmicro2549**. URL: https://doi.org/10.1038/nrmicro2549 (krulwich2011molecularaspectsof pages 1-3, krulwich2011molecularaspectsof pages 5-6, krulwich2011molecularaspectsof media 86e3a035)

2. **Ramoneda J, Stallard-Olivera E, Hoffert M, et al.** *Building a genome-based understanding of bacterial pH preferences.* **Science Advances**. **Apr 2023**. DOI: **10.1126/sciadv.adf8998**. URL: https://doi.org/10.1126/sciadv.adf8998 (ramoneda2023buildingagenomebased pages 1-1, ramoneda2023buildingagenomebased pages 1-2, ramoneda2023buildingagenomebased pages 3-5)

3. **Tran P, Lander SM, Prindle A.** *Active pH regulation facilitates Bacillus subtilis biofilm development in a minimally buffered environment.* **mBio**. **Mar 2024**. DOI: **10.1128/mbio.03387-23**. URL: https://doi.org/10.1128/mbio.03387-23 (tran2024activephregulation pages 1-2)

4. **Dechow SJ, Abramovitch RB.** *Targeting Mycobacterium tuberculosis pH-driven adaptation.* **Microbiology**. **May 2024**. DOI: **10.1099/mic.0.001458**. URL: https://doi.org/10.1099/mic.0.001458 (dechow2024targetingmycobacteriumtuberculosis pages 1-2)

5. **Terradot G, Krasnopeeva E, Swain PS, Pilizota T.** *Escherichia coli maintains pH via the membrane potential.* **PRX Life**. **Nov 2024**. DOI: **10.1103/PRXLife.2.043015**. URL: https://doi.org/10.1103/PRXLife.2.043015 (terradot2024escherichiacolimaintains pages 1-2, terradot2024escherichiacolimaintains pages 8-9)

6. **Zou M, Zhang Q, Li F, et al.** *Impacts of multiple environmental factors on soil bacterial community assembly in heavy metal polluted paddy fields.* **Scientific Reports**. **Jun 2024**. DOI: **10.1038/s41598-024-65678-x**. URL: https://doi.org/10.1038/s41598-024-65678-x (zou2024impactsofmultiple pages 1-2)

7. **Osburn ED, McBride SG, Bahram M, Strickland MS.** *Global patterns in the growth potential of soil bacterial communities.* **Nature Communications**. **Aug 2024**. DOI: **10.1038/s41467-024-50382-1**. URL: https://doi.org/10.1038/s41467-024-50382-1 (osburn2024globalpatternsin pages 1-2)

8. **Mucsi M, Borsodi AK, Megyes M, Szili-Kovács T.** *Response of the metabolic activity and taxonomic composition of bacterial communities to mosaically varying soil salinity and alkalinity.* **Scientific Reports**. **Mar 2024**. DOI: **10.1038/s41598-024-57430-2**. URL: https://doi.org/10.1038/s41598-024-57430-2 (mucsi2024responseofthe pages 1-2, mucsi2024responseofthe pages 2-3)


References

1. (krulwich2011molecularaspectsof pages 1-3): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

2. (krulwich2011molecularaspectsof pages 12-14): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

3. (ramoneda2023buildingagenomebased pages 1-2): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 88 citations and is from a highest quality peer-reviewed journal.

4. (krulwich2011molecularaspectsof pages 3-5): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

5. (ramoneda2023buildingagenomebased pages 1-1): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 88 citations and is from a highest quality peer-reviewed journal.

6. (ramoneda2023buildingagenomebased pages 2-3): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 88 citations and is from a highest quality peer-reviewed journal.

7. (ramoneda2023buildingagenomebased pages 6-7): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 88 citations and is from a highest quality peer-reviewed journal.

8. (terradot2024escherichiacolimaintains pages 1-2): Guillaume Terradot, Ekaterina Krasnopeeva, Peter S. Swain, and Teuta Pilizota. Escherichia coli maintains ph via the membrane potential. PRX Life, Nov 2024. URL: https://doi.org/10.1103/prxlife.2.043015, doi:10.1103/prxlife.2.043015. This article has 9 citations.

9. (terradot2024escherichiacolimaintains pages 8-9): Guillaume Terradot, Ekaterina Krasnopeeva, Peter S. Swain, and Teuta Pilizota. Escherichia coli maintains ph via the membrane potential. PRX Life, Nov 2024. URL: https://doi.org/10.1103/prxlife.2.043015, doi:10.1103/prxlife.2.043015. This article has 9 citations.

10. (tran2024activephregulation pages 1-2): Peter Tran, Stephen M. Lander, and Arthur Prindle. Active ph regulation facilitates <i>bacillus subtilis</i> biofilm development in a minimally buffered environment. Mar 2024. URL: https://doi.org/10.1128/mbio.03387-23, doi:10.1128/mbio.03387-23. This article has 24 citations and is from a domain leading peer-reviewed journal.

11. (dechow2024targetingmycobacteriumtuberculosis pages 1-2): Shelby J. Dechow and Robert B. Abramovitch. Targeting mycobacterium tuberculosis ph-driven adaptation. Microbiology, May 2024. URL: https://doi.org/10.1099/mic.0.001458, doi:10.1099/mic.0.001458. This article has 13 citations and is from a peer-reviewed journal.

12. (zou2024impactsofmultiple pages 1-2): Mengmeng Zou, Qi Zhang, Fengchun Li, Long Chen, Yifei Qiu, Qiqi Yin, and Shenglu Zhou. Impacts of multiple environmental factors on soil bacterial community assembly in heavy metal polluted paddy fields. Scientific Reports, Jun 2024. URL: https://doi.org/10.1038/s41598-024-65678-x, doi:10.1038/s41598-024-65678-x. This article has 27 citations and is from a peer-reviewed journal.

13. (osburn2024globalpatternsin pages 1-2): Ernest D. Osburn, Steven G. McBride, Mohammad Bahram, and Michael S. Strickland. Global patterns in the growth potential of soil bacterial communities. Nature Communications, Aug 2024. URL: https://doi.org/10.1038/s41467-024-50382-1, doi:10.1038/s41467-024-50382-1. This article has 41 citations and is from a highest quality peer-reviewed journal.

14. (krulwich2011molecularaspectsof pages 5-6): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

15. (krulwich2011molecularaspectsof media 86e3a035): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

16. (mucsi2024responseofthe pages 1-2): Márton Mucsi, Andrea K. Borsodi, Melinda Megyes, and Tibor Szili-Kovács. Response of the metabolic activity and taxonomic composition of bacterial communities to mosaically varying soil salinity and alkalinity. Scientific Reports, Mar 2024. URL: https://doi.org/10.1038/s41598-024-57430-2, doi:10.1038/s41598-024-57430-2. This article has 16 citations and is from a peer-reviewed journal.

17. (terradot2024escherichiacolimaintains pages 4-5): Guillaume Terradot, Ekaterina Krasnopeeva, Peter S. Swain, and Teuta Pilizota. Escherichia coli maintains ph via the membrane potential. PRX Life, Nov 2024. URL: https://doi.org/10.1103/prxlife.2.043015, doi:10.1103/prxlife.2.043015. This article has 9 citations.

18. (ramoneda2023buildingagenomebased pages 3-5): Josep Ramoneda, Elias Stallard-Olivera, Michael Hoffert, Claire C. Winfrey, Masumi Stadler, Juan Pablo Niño-García, and Noah Fierer. Building a genome-based understanding of bacterial ph preferences. Science Advances, Apr 2023. URL: https://doi.org/10.1126/sciadv.adf8998, doi:10.1126/sciadv.adf8998. This article has 88 citations and is from a highest quality peer-reviewed journal.

19. (krulwich2011molecularaspectsof pages 14-15): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

20. (krulwich2011molecularaspectsof pages 17-18): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

21. (krulwich2011molecularaspectsof pages 15-17): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

22. (krulwich2011molecularaspectsof pages 20-22): Terry A. Krulwich, George Sachs, and Etana Padan. Molecular aspects of bacterial ph sensing and homeostasis. Nature Reviews Microbiology, 9:330-343, May 2011. URL: https://doi.org/10.1038/nrmicro2549, doi:10.1038/nrmicro2549. This article has 1270 citations and is from a highest quality peer-reviewed journal.

23. (mucsi2024responseofthe pages 2-3): Márton Mucsi, Andrea K. Borsodi, Melinda Megyes, and Tibor Szili-Kovács. Response of the metabolic activity and taxonomic composition of bacterial communities to mosaically varying soil salinity and alkalinity. Scientific Reports, Mar 2024. URL: https://doi.org/10.1038/s41598-024-57430-2, doi:10.1038/s41598-024-57430-2. This article has 16 citations and is from a peer-reviewed journal.