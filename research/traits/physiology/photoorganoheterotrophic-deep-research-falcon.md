---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T12:20:20.472615'
end_time: '2026-06-18T12:33:40.726251'
duration_seconds: 800.25
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: photoorganoheterotrophic
  trait_identifier: METPO:1000659
  trait_category: PHYSIOLOGY
  trait_category_slug: physiology
  trait_slug: photoorganoheterotrophic
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A trophic type in which an organism obtains energy from light and carbon
    from organic compounds.
  parent_traits: METPO:1000631
  synonyms: photoorganoheterotroph
  evidence_summary: 'DOI:10.1016/B978-0-12-809633-8.20672-9: light-induced redox chemistry
    (Phototrophy chapter supports light-driven reaction-center electron transfer.)
    | DOI:10.1021/acsomega.3c02205: photoorganoheterotrophic (Review table classifies
    photoorganoheterotrophy by light with organic electron and carbon sources.)'
  causal_graph_summary: 'photoorganoheterotrophic_light_organic_electrons: 8 nodes,
    8 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 44
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** photoorganoheterotrophic
- **METPO identifier:** METPO:1000659
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy from light and carbon from organic compounds.
- **Parent traits:** METPO:1000631
- **Synonyms:** photoorganoheterotroph
- **Existing evidence:** DOI:10.1016/B978-0-12-809633-8.20672-9: light-induced redox chemistry (Phototrophy chapter supports light-driven reaction-center electron transfer.) | DOI:10.1021/acsomega.3c02205: photoorganoheterotrophic (Review table classifies photoorganoheterotrophy by light with organic electron and carbon sources.)
- **Existing causal graph summary:** photoorganoheterotrophic_light_organic_electrons: 8 nodes, 8 edges

## Research Objective

Research the microbial trait **photoorganoheterotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/photoorganoheterotrophic.yaml`.

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
- **Trait label:** photoorganoheterotrophic
- **METPO identifier:** METPO:1000659
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy from light and carbon from organic compounds.
- **Parent traits:** METPO:1000631
- **Synonyms:** photoorganoheterotroph
- **Existing evidence:** DOI:10.1016/B978-0-12-809633-8.20672-9: light-induced redox chemistry (Phototrophy chapter supports light-driven reaction-center electron transfer.) | DOI:10.1021/acsomega.3c02205: photoorganoheterotrophic (Review table classifies photoorganoheterotrophy by light with organic electron and carbon sources.)
- **Existing causal graph summary:** photoorganoheterotrophic_light_organic_electrons: 8 nodes, 8 edges

## Research Objective

Research the microbial trait **photoorganoheterotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/photoorganoheterotrophic.yaml`.

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


## Research Report: Microbial Trait "photoorganoheterotrophic" (METPO:1000659)

### 1) Key concepts and definitions (current understanding)

**Trait definition (METPO)**: *Photoorganoheterotrophic* denotes a trophic type in which an organism obtains **energy from light** and **carbon from organic compounds**.

**Operational microbiology definition (curation-ready)**: In contemporary microbial physiology literature, *photoorganoheterotrophy / photoheterotrophy* is commonly treated as **facultative phototrophy by primarily heterotrophic organisms**, where **light supplements cellular energy budgets** while **organic substrates supply carbon (and often electrons)**. Two mechanistic implementations are highlighted: (i) **chlorophototrophy** (photochemical reaction centers using chlorophyll/bacteriochlorophyll) and (ii) **retinalophototrophy** (rhodopsin-based light-driven ion pumps). (tinguely2023diurnalcyclesdrive pages 1-2)

**Boundary cases / nearby traits**

- **Photomixotrophy (not photoorganoheterotrophy)**: cyanobacterial literature distinguishes *photomixotrophic* growth as partial use of organic substrates while maintaining photosynthetic carbon fixation, and explicitly warns that photomixotrophy can be mistaken for “true heterotrophy” if not carefully defined/assayed. (stebegg2023heterotrophyamongcyanobacteria pages 2-4)
- **Chemoorganoheterotrophy (not photoorganoheterotrophy)**: growth in darkness where organic compounds provide carbon, electrons, and energy. (stebegg2023heterotrophyamongcyanobacteria pages 1-2)
- **Photoautotrophy / photolithoautotrophy (not photoorganoheterotrophy)**: light energy with **inorganic carbon (CO2)** as carbon source and **water (or other inorganic donors)** as electron source in canonical oxygenic photosynthesis. (stebegg2023heterotrophyamongcyanobacteria pages 1-2)
- **Light-activated heterotrophic growth (LAHG; related subtype)**: cyanobacterial work describes LAHG as a **chemoheterotrophic mode requiring brief daily illumination** (minutes) and **strict dependence on an organic carbon source (e.g., glucose)**; it can be treated as a boundary/assay subtype within the broader photoheterotrophy umbrella. (stebegg2023heterotrophyamongcyanobacteria pages 2-2)

**Figure/table support for trophic classification**: In Stebegg et al. (2023), a curated trophic-mode table and a substrate-uptake/metabolism schematic provide a convenient conceptual reference for curating trophic-type boundaries and substrate-driven heterotrophy in phototrophs. (stebegg2023heterotrophyamongcyanobacteria media 63734baa, stebegg2023heterotrophyamongcyanobacteria media 01d54873)

### 2) Recent developments and latest research (prioritize 2023–2024)

#### 2.1 Reaction-center-based photoheterotrophy (chlorophototrophy) and diurnal physiology
A 2023 study/review of **facultative phototrophy** (Porphyrobacter; aerobic anoxygenic phototroph context) emphasizes that photoheterotrophy can be mediated by **photochemical reaction centers** (chlorophototrophy) or **rhodopsins** (retinalophototrophy) and that diurnal light cycles can drive **rhythmic transcription** and **survival strategies under nutrient limitation**. It reports that in a model aerobic anoxygenic phototroph, **stationary-phase survival relies on functional reaction centers** and survival depends on light regime. (tinguely2023diurnalcyclesdrive pages 1-2)

#### 2.2 Cyanobacterial photoorganoheterotrophy and assay controls (2023)
A 2023 ACS Omega review updates cyanobacterial heterotrophy concepts and provides mechanistic controls/assay interpretations:
- It explicitly equates *photoorganoheterotrophic growth* with *photoheterotrophic growth*. (stebegg2023heterotrophyamongcyanobacteria pages 2-2)
- It notes that chemical inhibition of PSII with **DCMU** is used to create/assay photoheterotrophy and states that DCMU “**blocks electron transfer from photosystem II to the quinone pool**.” (stebegg2023heterotrophyamongcyanobacteria pages 2-2)
- Under PSII absence/inhibition, it states **ATP from PSI is insufficient for CO2 fixation**, implying that **organic electron sources must support carbon assimilation**. (stebegg2023heterotrophyamongcyanobacteria pages 2-2)

These details are particularly useful for causal-graph edges that depend on experimental perturbations.

#### 2.3 Genomics and ecology of bacteriochlorophyll-based photoheterotrophy in Gemmatimonadota (2023–2024)
A 2023 large-scale ecogenomics analysis (>400 MAGs) provides quantitative evidence that bacteriochlorophyll-based photoheterotrophy is habitat-structured in Gemmatimonadota:
- Genes for Type II photosynthetic reaction centers (**pufM and/or pufL**) occur in **51.6%** of freshwater MAGs, **47.8%** of soda lake sediment MAGs, **30.7%** of other sediment MAGs, and **16.3%** of wastewater MAGs, and are absent in other surveyed environments. (mujakic2023multienvironmentecogenomicsanalysis pages 9-11)
- Photosynthesis gene clusters in phototrophic Gemmatimonadota include **bch/crt** (bacteriochlorophyll/carotenoid) and **puf/puh** operons (reaction center and light-harvesting complex subunits), consistent with anoxygenic photoheterotrophy requiring organic substrates. (mujakic2023multienvironmentecogenomicsanalysis pages 1-2)

A 2024 mSystems study on *Gemmatimonas phototrophica* adds regulatory and physiological nuance relevant to causal graphs:
- It describes the organism as **photoheterotrophic**: it “**requires organic carbon, but light provides energy for its metabolism and stimulates its growth**.” (kopejtka2024minimaltranscriptionalregulation pages 1-2)
- It reports oxygen/light regulation differences: *G. phototrophica* “**possesses neither the oxygen-dependent repression** … nor the **light-dependent repression** described in aerobic anoxygenic phototrophs” (comparative regulatory framing). (kopejtka2024minimaltranscriptionalregulation pages 1-2)
- It reports a quantitative light response: optimal growth at **~80 µmol photon m−2 s−1**, while **higher light intensities inhibit growth**. (kopejtka2024minimaltranscriptionalregulation pages 1-2)

Together, these sources support graph edges linking **PGC genes → phototrophic capacity**, and **environment/light/oxygen regimes → expression/fitness constraints**.

#### 2.4 Proteorhodopsin-based photoheterotrophy (retinalophototrophy) under nutrient repletion (2024)
A 2024 Journal of Microbiology and Biotechnology study on *Candidatus Puniceispirillum marinum* IMCC1322 reports experimentally grounded energetic effects of proteorhodopsin (PR) photoheterotrophy:
- Cellular ATP ranges: **0.0331–1.74 mM**, corresponding to **~13.9–367 zeptomoles ATP/cell** across light regimes. (oh2024effectoflight pages 1-2)
- It estimates additional PR-driven ATP synthesis: **~0.168 zmol/cell/h** on average, and discusses that this energy is small relative to estimated protein turnover demands. (oh2024effectoflight pages 13-14)
- It emphasizes a critical boundary condition: PR “**supplies only ATP**” and “**can never be harnessed to generate NAD(P)H**,” differentiating PR photoheterotrophy from reaction-center-based phototrophy that can provide reducing power. (oh2024effectoflight pages 13-14)
- It reports that stable isotope measurements showed **no significant differences in inorganic carbon assimilation** between constant light and constant dark in late log phase, indicating PR did not measurably increase autotrophic carbon fixation in this assay. (oh2024effectoflight pages 13-14, oh2024effectoflight pages 6-8)
- It links nutrient context to phenotype: PR photoheterotrophy was observed under **nutrient-replete conditions**, and PR photoheterotrophy signals increased with **higher inoculum density**. (oh2024effectoflight pages 1-2, oh2024effectoflight pages 8-9)

A 2024 transcriptomic study further indicates PR and retinoid genes can be **constitutively expressed** in IMCC1322, while subsets of genes respond to light/dark/stationary phase contexts (clustered expression behavior). (lee2024effectsoflight pages 1-2)

#### 2.5 Updated mechanistic structure of Type I reaction centers (2024)
A 2024 Biomolecules review synthesizes high-resolution structures of homodimeric Type I reaction-center photosystems in anoxygenic phototrophs and provides curatable mechanistic entities:
- Core architecture: homodimeric **PscA/PshA** cores with defined transmembrane helix organization. (niederman2024whatweare pages 1-2)
- Electron-transfer chain: “**electrons are transferred directly from A0 to FX**,” with downstream terminal acceptors **FA/FB [4Fe-4S] clusters** (housed by **PscB**). (niederman2024whatweare pages 5-7)
- Cytochrome donors: cytochromes (e.g., **cytochrome cZ/PscC** or **PscX/PscY**) donate electrons to re-reduce oxidized special pairs (P840+). (niederman2024whatweare pages 20-22, niederman2024whatweare pages 9-11)

These mechanistic statements are directly suitable for causal edges connecting light harvesting → charge separation → electron transfer → cyclic electron flow.

### 3) Current applications and real-world implementations

**Environmental microbiology / ecosystem modeling**: Evidence that diurnal light cycles modulate survival and transcription in facultative phototrophs suggests that photoheterotrophy can be a **fitness strategy under nutrient limitation**, relevant for ecosystem models that couple light regimes with microbial carbon demand and persistence. (tinguely2023diurnalcyclesdrive pages 1-2)

**Cultivation and biotechnology enabling conditions**: The cyanobacterial heterotrophy review explicitly frames the importance of recognizing heterotrophic/photoheterotrophic modes for **cultivation methods**, including controlling for light, organic substrates, and photosystem activity/inhibition in experimental design. (stebegg2023heterotrophyamongcyanobacteria pages 1-2, stebegg2023heterotrophyamongcyanobacteria pages 2-2)

**Wastewater/freshwater microbiomes**: Gemmatimonadota ecogenomics indicates that photoheterotrophic phototrophy genes (puf) are concentrated in fresh waters/wastewaters/soda lakes (not marine), supporting practical metagenomic screening in those habitats for photoheterotrophic contributions to carbon cycling. (mujakic2023multienvironmentecogenomicsanalysis pages 9-11, mujakic2023multienvironmentecogenomicsanalysis pages 1-2)

### 4) Expert opinions and analysis (authoritative synthesis)

**Fitness tradeoffs and regulation**: Recent synthesis emphasizes that while phototrophy can increase ATP and spare organic carbon, it has costs (pigment biosynthesis; reactive oxygen species under light+oxygen) and this drives regulatory strategies such as repressing bacteriochlorophyll synthesis under certain conditions—though regulatory patterns vary by lineage (e.g., *Gemmatimonas phototrophica* differs from many AAPs). (tinguely2023diurnalcyclesdrive pages 1-2, kopejtka2024minimaltranscriptionalregulation pages 1-2)

**Mechanistic separation of rhodopsin vs reaction-center photoheterotrophy**: PR-based photoheterotrophy should be curated distinctly from reaction-center phototrophy because it provides ATP (via PMF) but not reducing power for anabolism; experimental stable isotope results can show *no increase* in inorganic carbon assimilation under light even when ATP increases. (oh2024effectoflight pages 13-14, oh2024effectoflight pages 6-8)

### 5) Relevant statistics and data from recent studies

- **Prevalence of Type II RC genes in Gemmatimonadota MAGs**: pufM/pufL detected in **51.6%** freshwater MAGs; **47.8%** soda lake; **30.7%** other sediments; **16.3%** wastewater (absent elsewhere in the dataset). (mujakic2023multienvironmentecogenomicsanalysis pages 9-11)
- **Gemmatimonadota relative abundance**: *G. phototrophica* clade frequencies in lake hypolimnia/illuminated sediments estimated at **~0.1–1%** of bacteria by 16S rRNA frequencies (metagenomic context). (kopejtka2024minimaltranscriptionalregulation pages 8-10)
- **Proteorhodopsin photoheterotrophy energetics (IMCC1322)**:
  - ATP concentration: **0.0331–1.74 mM**; **~13.9–367 zmol ATP/cell**. (oh2024effectoflight pages 1-2)
  - Additional PR-driven ATP synthesis rate: **~0.168 zmol/cell/h** (average). (oh2024effectoflight pages 13-14)
  - Inorganic carbon assimilation: **no significant difference** between constant light and constant dark (13C bicarbonate labeling) in the reported assay. (oh2024effectoflight pages 13-14, oh2024effectoflight pages 6-8)

---

## Trait scope summary (curation-focused)

**Trait label**: photoorganoheterotrophic (METPO:1000659)

**Scope statement**: Capacity for **light-supported heterotrophic growth** where **organic compounds supply carbon** and light provides an **energy supplement**, implemented through either **(a) reaction-center-based anoxygenic phototrophy** (Type I or Type II reaction centers; bacteriochlorophyll/chlorophyll pigments, cyclic electron flow) or **(b) rhodopsin-based photoheterotrophy** (proteorhodopsin-like light-driven ion pumps generating PMF that can increase ATP). (tinguely2023diurnalcyclesdrive pages 1-2, stebegg2023heterotrophyamongcyanobacteria pages 2-2, oh2024effectoflight pages 13-14)

**Boundary notes**:
- Exclude pure photoautotrophy (CO2 carbon source). (stebegg2023heterotrophyamongcyanobacteria pages 1-2)
- Treat photomixotrophy separately; it may still rely substantially on CO2 fixation. (stebegg2023heterotrophyamongcyanobacteria pages 2-4)
- Treat LAHG as a related subtype if desired (brief illumination but strict organic carbon dependence). (stebegg2023heterotrophyamongcyanobacteria pages 2-2)

---

## Candidate causal-graph nodes (grouped by type)

### Environmental / experimental factors (ENVO candidates; label acceptable)
- Light intensity / irradiance; diel cycles / dark–light alternance (tinguely2023diurnalcyclesdrive pages 1-2, kopejtka2024minimaltranscriptionalregulation pages 1-2)
- Oxygen availability (aerobic vs semiaerobic); oxygen-dependent repression (kopejtka2024minimaltranscriptionalregulation pages 1-2)
- Nutrient limitation vs nutrient repletion; inoculum density (oh2024effectoflight pages 1-2, oh2024effectoflight pages 8-9)
- Chemical inhibitor: DCMU (CHEBI:42406) (stebegg2023heterotrophyamongcyanobacteria pages 2-2)

### Pathways / modules (GO/MetaCyc/KEGG candidates; label acceptable)
- Aerobic anoxygenic phototrophy (AAP) / bacteriochlorophyll-a-based photoheterotrophy (mujakic2023multienvironmentecogenomicsanalysis pages 9-11, mujakic2023multienvironmentecogenomicsanalysis pages 1-2)
- Proteorhodopsin photoheterotrophy (PRp) (oh2024effectoflight pages 1-2, oh2024effectoflight pages 13-14)
- Oxidative phosphorylation / F0F1-ATP synthase (oh2024effectoflight pages 10-11)

### Genes / proteins / complexes
**Type II reaction center / AAP markers**
- pufM / pufL (reaction center subunits; KEGG ortholog candidates) (mujakic2023multienvironmentecogenomicsanalysis pages 9-11)
- Photosynthesis gene cluster (PGC) containing bch/crt/puf/puh operons (mujakic2023multienvironmentecogenomicsanalysis pages 1-2)

**Type I reaction center components (curatable molecular entities)**
- PscA / PshA (Type I RC core) (niederman2024whatweare pages 1-2)
- PscB (houses FA/FB clusters) (niederman2024whatweare pages 5-7)
- Cytochromes: PscC (cytochrome cZ), PscX/PscY; cytochrome bc1 complex (niederman2024whatweare pages 20-22, niederman2024whatweare pages 9-11)

**Cyanobacterial photoheterotrophy / LAHG relevant entities**
- Photosystem II electron transfer (inhibited by DCMU) (stebegg2023heterotrophyamongcyanobacteria pages 2-2)
- Organic substrate transporters (e.g., glucose transporter homologs; FrtRABC fructose transporter) (stebegg2023heterotrophyamongcyanobacteria pages 2-2)

**Proteorhodopsin pathway**
- Proteorhodopsin (PR) (oh2024effectoflight pages 1-2, oh2024effectoflight pages 13-14)

### Chemicals / metabolites
- Glucose (CHEBI:17234) (stebegg2023heterotrophyamongcyanobacteria pages 2-2)
- ATP (CHEBI:15422) (oh2024effectoflight pages 12-13, oh2024effectoflight pages 1-2)
- Protons (CHEBI:15378) and periplasmic proton stress (oh2024effectoflight pages 10-11)

---

## Candidate causal edges (evidence-backed)

| Subject node (suggested CURIE) | Predicate | Object node (suggested CURIE) | Evidence snippet | Source (DOI, year, URL) | Notes/uncertainty |
|---|---|---|---|---|---|
| light (CHEBI:25030) | drives | Type I/II reaction center charge separation (label) | “Light absorption by LH pigments… funnels excitation to the special pair, initiating charge separation.” (niederman2024whatweare pages 1-2) | 10.3390/biom14030311, 2024, https://doi.org/10.3390/biom14030311 | General anoxygenic phototrophy mechanism; applies to chlorophototrophic photoheterotrophs. |
| Type I reaction center / RC-PS (GO:0030094 candidate) | enables | electron transfer to Fe–S acceptors (label) | “electrons are transferred directly from A0 to FX” and terminal acceptors include “FA and FB [4Fe-4S] clusters” (niederman2024whatweare pages 5-7, niederman2024whatweare pages 20-22) | 10.3390/biom14030311, 2024, https://doi.org/10.3390/biom14030311 | Strong mechanistic edge for Type I RC-containing photoheterotrophs. |
| phototrophy / reaction center activity (GO:0015979 candidate) | increases | intracellular ATP (CHEBI:15422) | “Phototrophy can raise intracellular ATP” (tinguely2023diurnalcyclesdrive pages 1-2) | 10.1038/s43705-023-00334-5, 2023, https://doi.org/10.1038/s43705-023-00334-5 | Review-level summary; does not specify a single molecular path to PMF in excerpt. |
| proteorhodopsin (label; UniProt family candidate) | pumps | proton (CHEBI:15378) | rhodopsins “act as light-driven ion pumps” creating “a proton motive force” (deng2025theroleof pages 47-51) | 2025 review excerpt, URL unavailable in context | Mechanistically useful but source is 2025 and journal metadata incomplete; curate cautiously if preferring 2023–2024 only. |
| proton motive force (GO:0006122 related process candidate) | drives | ATP synthase activity (GO:0016887) | rhodopsins create “a proton motive force that drives ATP synthesis via ATP synthase” (deng2025theroleof pages 47-51) | 2025 review excerpt, URL unavailable in context | Strong conceptually; metadata incomplete in context. |
| proteorhodopsin activity (label) | increases | cellular ATP (CHEBI:15422) | “Measured ATP under alternating light/dark… ranged 0.0331–1.74 mM… Light-conditioned cultures showed higher cellular ATP than dark” (oh2024effectoflight pages 12-13) | 10.4014/jmb.2410.10034, 2024, https://doi.org/10.4014/jmb.2410.10034 | Strong experimental support in IMCC1322; taxon-specific. |
| proteorhodopsin (label) | supplies | ATP but not NAD(P)H (CHEBI:16474 candidate for NADPH) | “the PR function of strain IMCC1322… supplies only ATP” and “PR can never be harnessed to generate NAD(P)H” (oh2024effectoflight pages 13-14) | 10.4014/jmb.2410.10034, 2024, https://doi.org/10.4014/jmb.2410.10034 | Important boundary edge distinguishing PR photoheterotrophy from reducing-power-generating chlorophototrophy. |
| DCMU (CHEBI:42406) | inhibits | photosystem II electron transfer (GO:0009773 candidate) | “DCMU… blocks electron transfer from photosystem II to the quinone pool” (stebegg2023heterotrophyamongcyanobacteria pages 2-2) | 10.1021/acsomega.3c02205, 2023, https://doi.org/10.1021/acsomega.3c02205 | Strong, assay-specific inhibitor edge. |
| photosystem II absent/inhibited (label) | requires | organic electron source (label) | “when PSII is absent… the ATP originating from photosystem I is not sufficient for carbon dioxide fixation, and an organic electron source is additionally used” (stebegg2023heterotrophyamongcyanobacteria pages 2-2) | 10.1021/acsomega.3c02205, 2023, https://doi.org/10.1021/acsomega.3c02205 | Strong for cyanobacterial photoheterotrophy; specific to oxygenic phototroph boundary case. |
| glucose (CHEBI:17234) | is required for | light-activated heterotrophic growth (label) | growth “is strictly dependent on the presence of glucose” (stebegg2023heterotrophyamongcyanobacteria pages 2-2) | 10.1021/acsomega.3c02205, 2023, https://doi.org/10.1021/acsomega.3c02205 | LAHG is related but may be narrower than generic photoorganoheterotrophy. |
| pufM / pufL (gene labels; KEGG ortholog candidates) | encode component of | Type II reaction center (label) | “Genes for type II photosynthetic reaction centers (pufM and/or pufL) were detected” (mujakic2023multienvironmentecogenomicsanalysis pages 9-11) | 10.1128/spectrum.01112-23, 2023, https://doi.org/10.1128/spectrum.01112-23 | Presence-based genomic evidence; direct encoding relation inferred from standard gene annotation. |
| pufM marker gene (label) | indicates | aerobic anoxygenic phototrophy (label) | “the pufM marker for AAP (encoding the M subunit of the type II reaction center) was confirmed” (mujakic2023multienvironmentecogenomicsanalysis pages 9-11) | 10.1128/spectrum.01112-23, 2023, https://doi.org/10.1128/spectrum.01112-23 | Useful biomarker edge for genomic curation; indicates potential, not always expressed phenotype. |
| photosynthesis gene cluster (PGC) with bch/crt/puf/puh genes (label) | enables | BChl-a-based photoheterotrophy / anoxygenic phototrophy (label) | PGCs “include bch and crt genes… and puf and puh operons” and support “anoxygenic phototrophy using bacteriochlorophyll-a-containing photosystems” (mujakic2023multienvironmentecogenomicsanalysis pages 1-2) | 10.1128/spectrum.01112-23, 2023, https://doi.org/10.1128/spectrum.01112-23 | Good graph backbone for bacteriochlorophyll-based photoorganoheterotrophy. |
| oxygen-dependent repression (label) | decreases | photosynthesis gene expression / BChl synthesis (label) | in purple bacteria, photosystem genes are “tightly controlled by oxygen,” whereas G. phototrophica “possesses neither the oxygen-dependent repression” (kopejtka2024minimaltranscriptionalregulation pages 1-2) | 10.1128/msystems.00706-24, 2024, https://doi.org/10.1128/msystems.00706-24 | Comparative regulatory edge; effect established by contrast, strongest for purple bacteria background. |
| illumination / light-dependent repression (label) | decreases | BChl synthesis (label) | AAP bacteria “rapidly downregulate photosynthesis genes on illumination to stop BChl synthesis and avoid ROS” (kopejtka2024minimaltranscriptionalregulation pages 1-2) | 10.1128/msystems.00706-24, 2024, https://doi.org/10.1128/msystems.00706-24 | Strong regulatory edge for many AAPs; not true in G. phototrophica. |
| high light intensity (200 µmol photons m−2 s−1) | inhibits | G. phototrophica growth / photoheterotrophic performance (label) | “higher light intensities had an inhibitory effect” (kopejtka2024minimaltranscriptionalregulation pages 1-2) | 10.1128/msystems.00706-24, 2024, https://doi.org/10.1128/msystems.00706-24 | Taxon-specific, but useful environmental-control edge. |
| nutrient repletion / augmented amino-acid pool (ENVO/label) | enables | proteorhodopsin photoheterotrophy (label) | “strain IMCC1322 exhibited proteorhodopsin photoheterotrophy” under nutrient-replete conditions and “augmentation of organic carbon and nitrogen” (oh2024effectoflight pages 1-2) | 10.4014/jmb.2410.10034, 2024, https://doi.org/10.4014/jmb.2410.10034 | Strong but species-specific. |
| higher inoculum density (label) | increases | PR photoheterotrophy signal / biomass response (label) | “PRp signals strengthened by higher inoculum/cell densities” (oh2024effectoflight pages 8-9) | 10.4014/jmb.2410.10034, 2024, https://doi.org/10.4014/jmb.2410.10034 | Experimental condition edge; likely assay-specific. |
| nutrient depletion (ENVO/label) | causes | excess periplasmic protons / acid stress during PR activity (label) | “Under nutrient depletion, PR activity can generate excessive periplasmic protons causing acid stress” (oh2024effectoflight pages 1-2) | 10.4014/jmb.2410.10034, 2024, https://doi.org/10.4014/jmb.2410.10034 | Useful cautionary edge; species-specific. |
| diurnal cycles / dark-light alternance (ENVO:01000687 candidate) | drives | rhythmic transcription (GO:0006351) | “cyclic variations with a pervasive pattern of rhythmic transcription” (tinguely2023diurnalcyclesdrive pages 1-2) | 10.1038/s43705-023-00334-5, 2023, https://doi.org/10.1038/s43705-023-00334-5 | Strong in Porphyrobacter model; likely broader to facultative phototrophs. |
| functional reaction centers (label) | promotes | survival in stationary phase (GO:0012501 candidate) | “survival in stationary phase relies on functional reaction centers” (tinguely2023diurnalcyclesdrive pages 1-2) | 10.1038/s43705-023-00334-5, 2023, https://doi.org/10.1038/s43705-023-00334-5 | Strong causal edge directly tied to phenotype. |
| PscA/PshA reaction-center core (gene/protein labels) | contains | A0 primary acceptor (label) | “PshA; PscA… Key cofactors comprise… two A0 chlorophyll acceptors” (niederman2024whatweare pages 1-2) | 10.3390/biom14030311, 2024, https://doi.org/10.3390/biom14030311 | Structural edge for Type I RCs. |
| A0 chlorophyll acceptor (label) | transfers electrons to | FX [4Fe-4S] cluster (CHEBI:30413 candidate) | “electrons are transferred directly from A0 to FX” (niederman2024whatweare pages 5-7) | 10.3390/biom14030311, 2024, https://doi.org/10.3390/biom14030311 | Strong mechanistic edge. |
| PscB (protein label) | houses | FA/FB [4Fe-4S] clusters (CHEBI:30413 candidate) | “PscB housing the FA and FB [4Fe-4S] clusters” (niederman2024whatweare pages 5-7) | 10.3390/biom14030311, 2024, https://doi.org/10.3390/biom14030311 | Structural membership edge. |
| cytochrome cZ / PscC or PscX/PscY (protein labels) | donates electrons to | P840+ special pair (label) | “Electrons are donated by cytochromes: cytochrome cZ… and a cytochrome c PscX-PscY heterodimer” and electrons are “returned to P840” (niederman2024whatweare pages 20-22, niederman2024whatweare pages 9-11) | 10.3390/biom14030311, 2024, https://doi.org/10.3390/biom14030311 | Strong mechanistic edge for re-reduction of oxidized RC donor. |
| cytochrome bc1 complex (GO:0005750 candidate) | supplies electrons to | cytochrome cZ / PscC (protein label) | cytochrome cZ “receive[s] electrons from the cytochrome bc1 complex” (niederman2024whatweare pages 9-11) | 10.3390/biom14030311, 2024, https://doi.org/10.3390/biom14030311 | Supports upstream donor chain in Type I RC phototrophy. |
| retinalophototrophy / rhodopsin-based photoheterotrophy (label) | differs from | chlorophototrophy in lacking reducing power generation (label) | “simple light-driven ion pumps that do not generate reducing power” (deng2025theroleof pages 47-51) | 2025 review excerpt, URL unavailable in context | Useful boundary-case edge; metadata incomplete. |


*Table: This table lists candidate subject-predicate-object edges for curating a TraitMech graph of photoorganoheterotrophy/photoheterotrophy. It emphasizes experimentally supported mechanisms, environmental controls, and reaction-center or rhodopsin pathways, while flagging taxon-specific or metadata-limited claims.*

---

## Curation notes from figures/tables

- **Trophic-mode classification and substrate uptake/metabolism**: Stebegg et al. (2023) includes a trophic-mode table and a cyanobacterial substrate-uptake/metabolism schematic that can be used as a conceptual scaffold for nodes representing “organic substrate import,” “organic substrate catabolism,” and trophic-mode boundary conditions. (stebegg2023heterotrophyamongcyanobacteria media 63734baa, stebegg2023heterotrophyamongcyanobacteria media 01d54873)

---

## Warnings / claims not yet ready for strong curation

1. **Rhodopsin mechanistic statements from incomplete-metadata source**: One rhodopsin/photoheterotrophy mechanistic excerpt in the evidence corpus has incomplete journal metadata (2025 review excerpt). Prefer to ground rhodopsin edges primarily in 2024 primary studies above (e.g., IMCC1322 ATP and isotope data) unless a fully citable 2023–2024 rhodopsin review is added to the evidence set. (deng2025theroleof pages 47-51)
2. **Gene presence vs expressed phenotype**: MAG- and marker-based prevalence (e.g., puf genes) indicates *potential* for AAP/photoheterotrophy; expression and physiological demonstration may require additional evidence for specific taxa/conditions. (mujakic2023multienvironmentecogenomicsanalysis pages 9-11)
3. **Taxon/assay specificity**: Edges involving DCMU (PSII inhibition), LAHG, and IMCC1322 PR energetics are strong for those systems but should be flagged as system-specific when curating a general trait graph. (stebegg2023heterotrophyamongcyanobacteria pages 2-2, oh2024effectoflight pages 13-14)

---

## DOI-first bibliography (with dates and URLs)

1. **Stebegg R, Schmetterer G, Rompel A.** Heterotrophy among Cyanobacteria. *ACS Omega.* **2023-09**. DOI: **10.1021/acsomega.3c02205**. URL: https://doi.org/10.1021/acsomega.3c02205 (stebegg2023heterotrophyamongcyanobacteria pages 2-4, stebegg2023heterotrophyamongcyanobacteria pages 2-2, stebegg2023heterotrophyamongcyanobacteria pages 13-14, stebegg2023heterotrophyamongcyanobacteria pages 1-2, stebegg2023heterotrophyamongcyanobacteria media 63734baa, stebegg2023heterotrophyamongcyanobacteria media 01d54873)
2. **Tinguely C, Paulméry M, Terrettaz C, Gonzalez D.** Diurnal cycles drive rhythmic physiology and promote survival in facultative phototrophic bacteria. *ISME Communications.* **2023-09**. DOI: **10.1038/s43705-023-00334-5**. URL: https://doi.org/10.1038/s43705-023-00334-5 (tinguely2023diurnalcyclesdrive pages 1-2)
3. **Mujakić I, Cabello-Yeves PJ, Villena-Alemany C, et al.** Multi-environment ecogenomics analysis of the cosmopolitan phylum Gemmatimonadota. *Microbiology Spectrum.* **2023-10**. DOI: **10.1128/spectrum.01112-23**. URL: https://doi.org/10.1128/spectrum.01112-23 (mujakic2023multienvironmentecogenomicsanalysis pages 9-11, mujakic2023multienvironmentecogenomicsanalysis pages 1-2, mujakic2023multienvironmentecogenomicsanalysis pages 11-13, mujakic2023multienvironmentecogenomicsanalysis pages 15-17)
4. **Niederman RA.** What We Are Learning from the Diverse Structures of the Homodimeric Type I Reaction Center-Photosystems of Anoxygenic Phototropic Bacteria. *Biomolecules.* **2024-03**. DOI: **10.3390/biom14030311**. URL: https://doi.org/10.3390/biom14030311 (niederman2024whatweare pages 11-13, niederman2024whatweare pages 20-22, niederman2024whatweare pages 5-7, niederman2024whatweare pages 1-2, niederman2024whatweare pages 4-5, niederman2024whatweare pages 9-11, niederman2024whatweare pages 22-23, niederman2024whatweare pages 7-9)
5. **Lee JH, Oh H-M.** Effects of Light and Dark Conditions on the Transcriptome of Aging Cultures of *Candidatus Puniceispirillum marinum* IMCC1322. *Journal of Microbiology.* **2024-04**. DOI: **10.1007/s12275-024-00125-0**. URL: https://doi.org/10.1007/s12275-024-00125-0 (lee2024effectsoflight pages 1-2)
6. **Oh H-M, Lee JH, Choi A, et al.** Effect of Light Regime on *Candidatus Puniceispirillum marinum* IMCC1322 in Nutrient-Replete Conditions. *Journal of Microbiology and Biotechnology.* **2024-11**. DOI: **10.4014/jmb.2410.10034**. URL: https://doi.org/10.4014/jmb.2410.10034 (oh2024effectoflight pages 1-2, oh2024effectoflight pages 8-9, oh2024effectoflight pages 12-13, oh2024effectoflight pages 13-14, oh2024effectoflight pages 10-11, oh2024effectoflight pages 6-8, oh2024effectoflight pages 2-3)
7. **Kopejtka K, Tomasch J, Shivaramu S, et al.** Minimal transcriptional regulation of horizontally transferred photosynthesis genes in phototrophic bacterium *Gemmatimonas phototrophica*. *mSystems.* **2024-09**. DOI: **10.1128/msystems.00706-24**. URL: https://doi.org/10.1128/msystems.00706-24 (kopejtka2024minimaltranscriptionalregulation pages 1-2, kopejtka2024minimaltranscriptionalregulation pages 8-10)


References

1. (tinguely2023diurnalcyclesdrive pages 1-2): Camille Tinguely, Mélanie Paulméry, Céline Terrettaz, and Diego Gonzalez. Diurnal cycles drive rhythmic physiology and promote survival in facultative phototrophic bacteria. ISME Communications, Sep 2023. URL: https://doi.org/10.1038/s43705-023-00334-5, doi:10.1038/s43705-023-00334-5. This article has 13 citations and is from a peer-reviewed journal.

2. (stebegg2023heterotrophyamongcyanobacteria pages 2-4): Ronald Stebegg, Georg Schmetterer, and Annette Rompel. Heterotrophy among cyanobacteria. ACS Omega, 8:33098-33114, Sep 2023. URL: https://doi.org/10.1021/acsomega.3c02205, doi:10.1021/acsomega.3c02205. This article has 37 citations and is from a peer-reviewed journal.

3. (stebegg2023heterotrophyamongcyanobacteria pages 1-2): Ronald Stebegg, Georg Schmetterer, and Annette Rompel. Heterotrophy among cyanobacteria. ACS Omega, 8:33098-33114, Sep 2023. URL: https://doi.org/10.1021/acsomega.3c02205, doi:10.1021/acsomega.3c02205. This article has 37 citations and is from a peer-reviewed journal.

4. (stebegg2023heterotrophyamongcyanobacteria pages 2-2): Ronald Stebegg, Georg Schmetterer, and Annette Rompel. Heterotrophy among cyanobacteria. ACS Omega, 8:33098-33114, Sep 2023. URL: https://doi.org/10.1021/acsomega.3c02205, doi:10.1021/acsomega.3c02205. This article has 37 citations and is from a peer-reviewed journal.

5. (stebegg2023heterotrophyamongcyanobacteria media 63734baa): Ronald Stebegg, Georg Schmetterer, and Annette Rompel. Heterotrophy among cyanobacteria. ACS Omega, 8:33098-33114, Sep 2023. URL: https://doi.org/10.1021/acsomega.3c02205, doi:10.1021/acsomega.3c02205. This article has 37 citations and is from a peer-reviewed journal.

6. (stebegg2023heterotrophyamongcyanobacteria media 01d54873): Ronald Stebegg, Georg Schmetterer, and Annette Rompel. Heterotrophy among cyanobacteria. ACS Omega, 8:33098-33114, Sep 2023. URL: https://doi.org/10.1021/acsomega.3c02205, doi:10.1021/acsomega.3c02205. This article has 37 citations and is from a peer-reviewed journal.

7. (mujakic2023multienvironmentecogenomicsanalysis pages 9-11): Izabela Mujakić, Pedro J. Cabello-Yeves, Cristian Villena-Alemany, Kasia Piwosz, Francisco Rodriguez-Valera, Antonio Picazo, Antonio Camacho, and Michal Koblížek. Multi-environment ecogenomics analysis of the cosmopolitan phylum gemmatimonadota. Oct 2023. URL: https://doi.org/10.1128/spectrum.01112-23, doi:10.1128/spectrum.01112-23. This article has 73 citations and is from a domain leading peer-reviewed journal.

8. (mujakic2023multienvironmentecogenomicsanalysis pages 1-2): Izabela Mujakić, Pedro J. Cabello-Yeves, Cristian Villena-Alemany, Kasia Piwosz, Francisco Rodriguez-Valera, Antonio Picazo, Antonio Camacho, and Michal Koblížek. Multi-environment ecogenomics analysis of the cosmopolitan phylum gemmatimonadota. Oct 2023. URL: https://doi.org/10.1128/spectrum.01112-23, doi:10.1128/spectrum.01112-23. This article has 73 citations and is from a domain leading peer-reviewed journal.

9. (kopejtka2024minimaltranscriptionalregulation pages 1-2): Karel Kopejtka, Jürgen Tomasch, Sahana Shivaramu, Mohit Kumar Saini, David Kaftan, and Michal Koblížek. Minimal transcriptional regulation of horizontally transferred photosynthesis genes in phototrophic bacterium <i>gemmatimonas phototrophica</i>. Sep 2024. URL: https://doi.org/10.1128/msystems.00706-24, doi:10.1128/msystems.00706-24. This article has 7 citations and is from a peer-reviewed journal.

10. (oh2024effectoflight pages 1-2): Hyun-Myung Oh, Ji Hyen Lee, Ahyoung Choi, Sung-Hyun Yang, Gyung-Hoon Shin, Sung Gyun Kang, Jang-Cheon Cho, Hak Jun Kim, and Kae-Kyoung Kwon. Effect of light regime on candidatus puniceispirillum marinum imcc1322 in nutrient-replete conditions. Journal of Microbiology and Biotechnology, Nov 2024. URL: https://doi.org/10.4014/jmb.2410.10034, doi:10.4014/jmb.2410.10034. This article has 1 citations and is from a peer-reviewed journal.

11. (oh2024effectoflight pages 13-14): Hyun-Myung Oh, Ji Hyen Lee, Ahyoung Choi, Sung-Hyun Yang, Gyung-Hoon Shin, Sung Gyun Kang, Jang-Cheon Cho, Hak Jun Kim, and Kae-Kyoung Kwon. Effect of light regime on candidatus puniceispirillum marinum imcc1322 in nutrient-replete conditions. Journal of Microbiology and Biotechnology, Nov 2024. URL: https://doi.org/10.4014/jmb.2410.10034, doi:10.4014/jmb.2410.10034. This article has 1 citations and is from a peer-reviewed journal.

12. (oh2024effectoflight pages 6-8): Hyun-Myung Oh, Ji Hyen Lee, Ahyoung Choi, Sung-Hyun Yang, Gyung-Hoon Shin, Sung Gyun Kang, Jang-Cheon Cho, Hak Jun Kim, and Kae-Kyoung Kwon. Effect of light regime on candidatus puniceispirillum marinum imcc1322 in nutrient-replete conditions. Journal of Microbiology and Biotechnology, Nov 2024. URL: https://doi.org/10.4014/jmb.2410.10034, doi:10.4014/jmb.2410.10034. This article has 1 citations and is from a peer-reviewed journal.

13. (oh2024effectoflight pages 8-9): Hyun-Myung Oh, Ji Hyen Lee, Ahyoung Choi, Sung-Hyun Yang, Gyung-Hoon Shin, Sung Gyun Kang, Jang-Cheon Cho, Hak Jun Kim, and Kae-Kyoung Kwon. Effect of light regime on candidatus puniceispirillum marinum imcc1322 in nutrient-replete conditions. Journal of Microbiology and Biotechnology, Nov 2024. URL: https://doi.org/10.4014/jmb.2410.10034, doi:10.4014/jmb.2410.10034. This article has 1 citations and is from a peer-reviewed journal.

14. (lee2024effectsoflight pages 1-2): Ji Hyen Lee and Hyun-Myung Oh. Effects of light and dark conditions on the transcriptome of aging cultures of candidatus puniceispirillum marinum imcc1322. Journal of microbiology, 62:297-314, Apr 2024. URL: https://doi.org/10.1007/s12275-024-00125-0, doi:10.1007/s12275-024-00125-0. This article has 2 citations and is from a peer-reviewed journal.

15. (niederman2024whatweare pages 1-2): Robert A. Niederman. What we are learning from the diverse structures of the homodimeric type i reaction center-photosystems of anoxygenic phototropic bacteria. Biomolecules, Mar 2024. URL: https://doi.org/10.3390/biom14030311, doi:10.3390/biom14030311. This article has 5 citations.

16. (niederman2024whatweare pages 5-7): Robert A. Niederman. What we are learning from the diverse structures of the homodimeric type i reaction center-photosystems of anoxygenic phototropic bacteria. Biomolecules, Mar 2024. URL: https://doi.org/10.3390/biom14030311, doi:10.3390/biom14030311. This article has 5 citations.

17. (niederman2024whatweare pages 20-22): Robert A. Niederman. What we are learning from the diverse structures of the homodimeric type i reaction center-photosystems of anoxygenic phototropic bacteria. Biomolecules, Mar 2024. URL: https://doi.org/10.3390/biom14030311, doi:10.3390/biom14030311. This article has 5 citations.

18. (niederman2024whatweare pages 9-11): Robert A. Niederman. What we are learning from the diverse structures of the homodimeric type i reaction center-photosystems of anoxygenic phototropic bacteria. Biomolecules, Mar 2024. URL: https://doi.org/10.3390/biom14030311, doi:10.3390/biom14030311. This article has 5 citations.

19. (kopejtka2024minimaltranscriptionalregulation pages 8-10): Karel Kopejtka, Jürgen Tomasch, Sahana Shivaramu, Mohit Kumar Saini, David Kaftan, and Michal Koblížek. Minimal transcriptional regulation of horizontally transferred photosynthesis genes in phototrophic bacterium <i>gemmatimonas phototrophica</i>. Sep 2024. URL: https://doi.org/10.1128/msystems.00706-24, doi:10.1128/msystems.00706-24. This article has 7 citations and is from a peer-reviewed journal.

20. (oh2024effectoflight pages 10-11): Hyun-Myung Oh, Ji Hyen Lee, Ahyoung Choi, Sung-Hyun Yang, Gyung-Hoon Shin, Sung Gyun Kang, Jang-Cheon Cho, Hak Jun Kim, and Kae-Kyoung Kwon. Effect of light regime on candidatus puniceispirillum marinum imcc1322 in nutrient-replete conditions. Journal of Microbiology and Biotechnology, Nov 2024. URL: https://doi.org/10.4014/jmb.2410.10034, doi:10.4014/jmb.2410.10034. This article has 1 citations and is from a peer-reviewed journal.

21. (oh2024effectoflight pages 12-13): Hyun-Myung Oh, Ji Hyen Lee, Ahyoung Choi, Sung-Hyun Yang, Gyung-Hoon Shin, Sung Gyun Kang, Jang-Cheon Cho, Hak Jun Kim, and Kae-Kyoung Kwon. Effect of light regime on candidatus puniceispirillum marinum imcc1322 in nutrient-replete conditions. Journal of Microbiology and Biotechnology, Nov 2024. URL: https://doi.org/10.4014/jmb.2410.10034, doi:10.4014/jmb.2410.10034. This article has 1 citations and is from a peer-reviewed journal.

22. (deng2025theroleof pages 47-51): L Deng. The role of microbial rhodopsins in the evolution and adaptation of a marine diatom. Unknown journal, 2025.

23. (stebegg2023heterotrophyamongcyanobacteria pages 13-14): Ronald Stebegg, Georg Schmetterer, and Annette Rompel. Heterotrophy among cyanobacteria. ACS Omega, 8:33098-33114, Sep 2023. URL: https://doi.org/10.1021/acsomega.3c02205, doi:10.1021/acsomega.3c02205. This article has 37 citations and is from a peer-reviewed journal.

24. (mujakic2023multienvironmentecogenomicsanalysis pages 11-13): Izabela Mujakić, Pedro J. Cabello-Yeves, Cristian Villena-Alemany, Kasia Piwosz, Francisco Rodriguez-Valera, Antonio Picazo, Antonio Camacho, and Michal Koblížek. Multi-environment ecogenomics analysis of the cosmopolitan phylum gemmatimonadota. Oct 2023. URL: https://doi.org/10.1128/spectrum.01112-23, doi:10.1128/spectrum.01112-23. This article has 73 citations and is from a domain leading peer-reviewed journal.

25. (mujakic2023multienvironmentecogenomicsanalysis pages 15-17): Izabela Mujakić, Pedro J. Cabello-Yeves, Cristian Villena-Alemany, Kasia Piwosz, Francisco Rodriguez-Valera, Antonio Picazo, Antonio Camacho, and Michal Koblížek. Multi-environment ecogenomics analysis of the cosmopolitan phylum gemmatimonadota. Oct 2023. URL: https://doi.org/10.1128/spectrum.01112-23, doi:10.1128/spectrum.01112-23. This article has 73 citations and is from a domain leading peer-reviewed journal.

26. (niederman2024whatweare pages 11-13): Robert A. Niederman. What we are learning from the diverse structures of the homodimeric type i reaction center-photosystems of anoxygenic phototropic bacteria. Biomolecules, Mar 2024. URL: https://doi.org/10.3390/biom14030311, doi:10.3390/biom14030311. This article has 5 citations.

27. (niederman2024whatweare pages 4-5): Robert A. Niederman. What we are learning from the diverse structures of the homodimeric type i reaction center-photosystems of anoxygenic phototropic bacteria. Biomolecules, Mar 2024. URL: https://doi.org/10.3390/biom14030311, doi:10.3390/biom14030311. This article has 5 citations.

28. (niederman2024whatweare pages 22-23): Robert A. Niederman. What we are learning from the diverse structures of the homodimeric type i reaction center-photosystems of anoxygenic phototropic bacteria. Biomolecules, Mar 2024. URL: https://doi.org/10.3390/biom14030311, doi:10.3390/biom14030311. This article has 5 citations.

29. (niederman2024whatweare pages 7-9): Robert A. Niederman. What we are learning from the diverse structures of the homodimeric type i reaction center-photosystems of anoxygenic phototropic bacteria. Biomolecules, Mar 2024. URL: https://doi.org/10.3390/biom14030311, doi:10.3390/biom14030311. This article has 5 citations.

30. (oh2024effectoflight pages 2-3): Hyun-Myung Oh, Ji Hyen Lee, Ahyoung Choi, Sung-Hyun Yang, Gyung-Hoon Shin, Sung Gyun Kang, Jang-Cheon Cho, Hak Jun Kim, and Kae-Kyoung Kwon. Effect of light regime on candidatus puniceispirillum marinum imcc1322 in nutrient-replete conditions. Journal of Microbiology and Biotechnology, Nov 2024. URL: https://doi.org/10.4014/jmb.2410.10034, doi:10.4014/jmb.2410.10034. This article has 1 citations and is from a peer-reviewed journal.